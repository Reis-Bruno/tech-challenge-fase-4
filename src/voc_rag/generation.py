"""Etapas de construção do contexto e geração da resposta.

* ``build_context``: monta o bloco de evidências numeradas [R1..Rk] com metadados +
  as estatísticas de temas (contagens determinísticas).
* ``generate_answer``: chama o LLM configurado com um prompt que obriga a citar as
  evidências e a declarar insuficiência; sem LLM (``VOC_LLM_PROVIDER=none``) produz uma
  resposta extrativa estruturada, também 100% rastreável.
* ``check_citations``: pós-validação — remove/aponta citações para evidências que não
  existem e sinaliza respostas sem nenhuma citação.
"""
from __future__ import annotations

import os
import re

from . import config
from .query import QueryPlan
from .retriever import Evidence, RetrievalResult
from .themes import THEMES

SYSTEM_PROMPT = """Você é um analista de Voice of Customer de um e-commerce brasileiro.
Responda à pergunta do gestor usando EXCLUSIVAMENTE as avaliações de clientes fornecidas
no CONTEXTO. Regras obrigatórias:
1. Toda afirmação deve citar as avaliações que a sustentam no formato [R1], [R2]...
2. Não invente fatos, números, causas ou recomendações que não estejam nas evidências.
   Você pode usar as ESTATÍSTICAS DE TEMAS fornecidas para falar de frequência, deixando
   claro que são contagens por palavras-chave sobre a base filtrada.
3. Se as evidências não forem suficientes ou não responderem à pergunta, diga
   explicitamente: "Não há evidências suficientes na base de avaliações para responder" e
   explique o que foi encontrado.
4. Evidências são uma amostra: não generalize a partir de 1 avaliação; prefira padrões
   repetidos em várias delas.
5. Responda em português, de forma objetiva: um resumo de 1–2 frases e depois os principais
   pontos em tópicos, cada um com suas citações. Termine com uma linha "Limitações:" curta."""

REFUSAL_PREFIX = "Não há evidências suficientes na base de avaliações para responder"


def _fmt_delivery(e: Evidence) -> str:
    if e.delivery_status == "atrasado" and e.delay_days is not None:
        return f"entregue com {int(e.delay_days)} dia(s) de atraso"
    if e.delivery_status == "no_prazo":
        return "entregue no prazo"
    return "não entregue"


def format_evidence(e: Evidence) -> str:
    meta = (f"nota {e.score}/5 | compra {e.purchase_date} | categoria {e.category} | "
            f"{_fmt_delivery(e)} | UF {e.customer_state}")
    extra = f" | +{e.duplicates} avaliação(ões) com texto idêntico" if e.duplicates else ""
    sub = f" | tema: {e.subquery}" if e.subquery else ""
    return f"[{e.ref}] ({meta}{extra}{sub})\n\"{e.text}\""


def format_theme_stats(stats: list[dict], base: int, title: str) -> str:
    if not stats:
        return ""
    lines = [f"{title} (base: {base} avaliações)"]
    lines += [f"- {s['label']}: {s['count']} ({s['pct']}%)" for s in stats]
    return "\n".join(lines)


def build_context(plan: QueryPlan, result: RetrievalResult) -> str:
    parts = [f"FILTROS APLICADOS: {plan.filters.describe()}",
             f"AVALIAÇÕES NA POPULAÇÃO FILTRADA: {result.population}", "", "EVIDÊNCIAS:"]
    parts += [format_evidence(e) for e in result.evidences]
    pop = format_theme_stats(result.theme_stats_population, result.population,
                             "ESTATÍSTICAS DE TEMAS NA POPULAÇÃO FILTRADA")
    ret = format_theme_stats(result.theme_stats_retrieved,
                             result.trace.get("theme_sample_size", 0),
                             "ESTATÍSTICAS DE TEMAS ENTRE AS AVALIAÇÕES QUE MENCIONAM O ASSUNTO")
    for block in (pop, ret):
        if block:
            parts += ["", block]
    return "\n".join(parts)


def build_user_prompt(question: str, context: str) -> str:
    return f"CONTEXTO:\n{context}\n\nPERGUNTA: {question}\n\nRESPOSTA (com citações [R#]):"


# ---------------------------------------------------------------------------------------
# Provedores de LLM
# ---------------------------------------------------------------------------------------
def call_llm(system: str, user: str, provider: str | None = None, model: str | None = None,
             retries: int = 3) -> str:
    """Chama o LLM com novas tentativas (backoff 2s, 4s, 8s) para erros transitórios —
    ex.: limite de requisições por minuto da camada gratuita do Gemini (HTTP 429/503)."""
    import time

    for attempt in range(retries + 1):
        try:
            return _call_llm_once(system, user, provider, model)
        except Exception as exc:
            msg = str(exc)
            transient = any(code in msg for code in ("429", "503", "RESOURCE_EXHAUSTED", "UNAVAILABLE"))
            if not transient or attempt == retries:
                raise
            time.sleep(2 ** (attempt + 1))
    raise RuntimeError("unreachable")


def _call_llm_once(system: str, user: str, provider: str | None = None,
                   model: str | None = None) -> str:
    provider = (provider or config.LLM_PROVIDER).lower()
    model = model or config.LLM_MODEL or config.DEFAULT_MODELS.get(provider, "")
    temp = config.LLM_TEMPERATURE

    if provider in ("openai", "ollama"):
        from openai import OpenAI

        kwargs = {}
        if provider == "ollama":
            kwargs = {"base_url": config.OLLAMA_BASE_URL, "api_key": "ollama"}
        client = OpenAI(**kwargs)
        resp = client.chat.completions.create(
            model=model, temperature=temp,
            messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
        )
        return resp.choices[0].message.content.strip()

    if provider == "gemini":
        from google import genai
        from google.genai import types

        key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not key:
            raise RuntimeError("GEMINI_API_KEY não definida (crie em https://aistudio.google.com/apikey)")
        client = genai.Client(api_key=key)
        resp = client.models.generate_content(
            model=model, contents=user,
            config=types.GenerateContentConfig(system_instruction=system, temperature=temp),
        )
        return resp.text.strip()

    if provider == "anthropic":
        import anthropic

        client = anthropic.Anthropic()
        resp = client.messages.create(
            model=model, max_tokens=1500, temperature=temp, system=system,
            messages=[{"role": "user", "content": user}],
        )
        return "".join(b.text for b in resp.content if b.type == "text").strip()

    raise ValueError(f"Provedor de LLM não suportado: {provider}")


# ---------------------------------------------------------------------------------------
# Modo extrativo (sem LLM)
# ---------------------------------------------------------------------------------------
def extractive_answer(plan: QueryPlan, result: RetrievalResult) -> str:
    """Resposta sem LLM: organiza as evidências por tema e cita os trechos literais.

    Não "escreve" conclusões novas — apenas agrega o que foi recuperado. Útil para rodar
    a solução sem chave de API e como baseline de fidelidade.
    """
    lines: list[str] = []
    stats = result.theme_stats_retrieved or result.theme_stats_population
    by_theme: dict[str, list[Evidence]] = {}
    for e in result.evidences:
        keys = [e.subquery] if e.subquery else [THEMES[t]["label"] for t in e.themes] or ["Outros relatos"]
        by_theme.setdefault(keys[0], []).append(e)

    base = result.trace.get("theme_sample_size") or result.population
    if stats:
        top = ", ".join(f"{s['label'].lower()} ({s['pct']}%)" for s in stats[:3])
        lines.append(f"Resumo: nas {base} avaliações analisadas ({plan.filters.describe()}), "
                     f"os temas mais citados são: {top}.")
    lines.append("")
    lines.append("Principais pontos, com as evidências:")
    for theme, evs in by_theme.items():
        refs = " ".join(f"[{e.ref}]" for e in evs)
        lines.append(f"- {theme} {refs}")
        for e in evs[:2]:
            lines.append(f"    • \"{e.text[:160]}\" [{e.ref}]")
    lines.append("")
    lines.append("Limitações: resposta extrativa (sem LLM); percentuais vêm de contagem por "
                 "palavras-chave e as evidências são uma amostra das avaliações mais relevantes.")
    return "\n".join(lines)


def refusal_answer(result: RetrievalResult) -> str:
    return (f"{REFUSAL_PREFIX}. Motivo: {result.reason} "
            "Reformule a pergunta com um tema presente em avaliações de clientes "
            "(entrega, qualidade, atendimento, produto, embalagem, troca etc.) ou ajuste os filtros.")


_CIT = re.compile(r"\[R(\d+)\]")


def check_citations(answer: str, n_evidences: int) -> dict:
    cited = {int(x) for x in _CIT.findall(answer)}
    invalid = sorted(c for c in cited if c < 1 or c > n_evidences)
    for c in invalid:  # remove citações inventadas pelo modelo
        answer = answer.replace(f"[R{c}]", "[citação inválida]")
    is_refusal = REFUSAL_PREFIX.lower() in answer.lower()
    return {
        "answer": answer,
        "cited": sorted(cited - set(invalid)),
        "invalid_citations": invalid,
        "uncited_answer": not cited and not is_refusal,
        "coverage": round(len(cited - set(invalid)) / n_evidences, 2) if n_evidences else 0.0,
        "is_refusal": is_refusal,
    }

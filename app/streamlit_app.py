"""Interface web — Voice of Customer Intelligence (Olist).

Execução:  streamlit run app/streamlit_app.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from voc_rag import config  # noqa: E402
from voc_rag.pipeline import VoCPipeline  # noqa: E402
from voc_rag.query import Filters  # noqa: E402

EXAMPLES = [
    "Quais são os principais problemas relatados pelos clientes em suas avaliações?",
    "O que os clientes relatam sobre problemas relacionados à entrega?",
    "Quais aspectos da experiência de compra são mais elogiados pelos clientes?",
    "Quais padrões podem ser identificados nas avaliações de clientes insatisfeitos?",
    "Quais avaliações sustentam a conclusão de que existem problemas recorrentes relacionados ao prazo de entrega?",
    "Existem padrões recorrentes nas avaliações relacionadas à qualidade dos produtos?",
    "O que os clientes mais elogiam em produtos de beleza?",
    "Quais temas aparecem nas avaliações de pedidos entregues com atraso?",
    "Qual foi o faturamento da Olist em 2018?",
    "Qual a capital da França?",
]

st.set_page_config(page_title="VoC Intelligence — Olist", page_icon="💬", layout="wide")


@st.cache_resource(show_spinner="Carregando índices (vetorial + BM25)...")
def get_pipeline(provider: str, model: str) -> VoCPipeline:
    return VoCPipeline(provider=provider, model=model or None)


@st.cache_data
def categories() -> list[str]:
    df = pd.read_parquet(config.DOCUMENTS_FILE, columns=["category"])
    return df["category"].value_counts().index.tolist()


# ---------------------------------------------------------------- sidebar
with st.sidebar:
    st.header("Configuração")
    providers = ["none", "openai", "gemini", "anthropic", "ollama"]
    provider = st.selectbox(
        "Gerador (LLM)", providers,
        index=providers.index(config.LLM_PROVIDER) if config.LLM_PROVIDER in providers else 0,
        help="'none' = resposta extrativa, sem LLM (não precisa de chave de API).",
    )
    model = st.text_input("Modelo", value=config.LLM_MODEL or config.DEFAULT_MODELS.get(provider, ""))
    k = st.slider("Evidências enviadas ao modelo (k)", 4, 20, config.RETRIEVAL.final_k)

    st.header("Filtros de metadados")
    auto = st.toggle("Inferir filtros a partir da pergunta", value=True,
                     help="Ex.: 'nota baixa' → nota ≤ 2; 'elogios' → nota ≥ 4; 'em 2017'.")
    score = st.slider("Nota da avaliação", 1, 5, (1, 5))
    years = st.multiselect("Ano da compra", [2016, 2017, 2018])
    cats = st.multiselect("Categoria do produto", categories())
    delivery = st.multiselect("Situação da entrega", ["no_prazo", "atrasado", "nao_entregue"])

user_filters = Filters(
    min_score=score[0] if score[0] > 1 else None,
    max_score=score[1] if score[1] < 5 else None,
    years=years, categories=cats, delivery_status=delivery,
)

# ---------------------------------------------------------------- main
st.title("💬 Voice of Customer Intelligence")
st.caption("RAG sobre ~42 mil avaliações do Brazilian E-Commerce Public Dataset (Olist). "
           "Toda resposta é fundamentada em avaliações recuperadas e exibidas abaixo.")

if "question" not in st.session_state:
    st.session_state.question = EXAMPLES[0]
with st.expander("Perguntas de exemplo"):
    cols = st.columns(2)
    for i, ex in enumerate(EXAMPLES):
        if cols[i % 2].button(ex, key=f"ex{i}", use_container_width=True):
            st.session_state.question = ex

question = st.text_area("Pergunta", key="question", height=80)
if st.button("Perguntar", type="primary") and question.strip():
    pipe = get_pipeline(provider, model)
    with st.spinner("Recuperando avaliações e gerando resposta..."):
        resp = pipe.ask(question, filters=user_filters, auto_filters=auto, k=k)

    r = resp.retrieval
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Modo", r.mode)
    c2.metric("Avaliações na população filtrada", f"{r.population:,}".replace(",", "."))
    c3.metric("Evidências", len(resp.evidences))
    c4.metric("Gerador", resp.generator)

    if resp.sufficient:
        st.subheader("Resposta")
        st.markdown(resp.answer.replace("\n", "  \n"))
        chk = resp.citation_check
        if chk["invalid_citations"]:
            st.warning(f"O modelo citou evidências inexistentes {chk['invalid_citations']} — removidas.")
        if chk["uncited_answer"]:
            st.warning("A resposta não cita nenhuma evidência: trate-a com cautela.")
    else:
        st.subheader("Sem evidências suficientes")
        st.info(resp.answer)

    stats = r.theme_stats_retrieved or r.theme_stats_population
    if stats:
        base = r.trace.get("theme_sample_size") or r.population
        st.subheader("Frequência de temas")
        st.caption(f"Contagem por palavras-chave em {base} avaliações "
                   f"({'que mencionam o assunto' if r.theme_stats_retrieved else 'da população filtrada'}).")
        chart = pd.DataFrame(stats).set_index("label")["pct"].rename("% das avaliações")
        st.bar_chart(chart, horizontal=True)

    if resp.evidences:
        st.subheader("Evidências utilizadas")
        for e in resp.evidences:
            stars = "★" * e.score + "☆" * (5 - e.score)
            with st.container(border=True):
                st.markdown(f"**[{e.ref}]** {stars} — _{e.text}_")
                meta = (f"compra {e.purchase_date} · {e.category} · entrega: {e.delivery_status}"
                        + (f" ({int(e.delay_days)} d de atraso)" if e.delivery_status == "atrasado" and e.delay_days else "")
                        + f" · UF {e.customer_state} · sim. densa {e.dense_sim}"
                        + (f" · rank BM25 {e.bm25_rank}" if e.bm25_rank else "")
                        + (f" · tema: {e.subquery}" if e.subquery else "")
                        + (f" · +{e.duplicates} idênticas" if e.duplicates else "")
                        + f" · id {e.review_id[:8]}")
                st.caption(meta)

    with st.expander("🔎 Rastreamento do pipeline (como a resposta foi construída)"):
        st.markdown("**1. Transformação da pergunta**")
        st.json(resp.plan.as_dict())
        st.markdown("**2–4. Recuperação, fusão e suficiência**")
        st.json({"motivo": r.reason, **r.trace, "tempos_ms": resp.timings})
        if resp.context:
            st.markdown("**5. Contexto enviado ao modelo de linguagem**")
            st.code(resp.context, language="text")
        st.markdown("**6. Validação de citações**")
        st.json({k: v for k, v in resp.citation_check.items() if k != "answer"})

"""Estudo de ablação da recuperação.

Mede quanto cada componente do retriever contribui, ligando-os um a um a partir de uma
linha de base de busca vetorial pura (top-k por cosseno, sem filtros). Não usa LLM: avalia
somente as evidências recuperadas, nas mesmas perguntas de eval/questions.json.

Métricas (médias sobre as perguntas respondíveis, salvo indicação):
* precisao      — fração das evidências que contêm termos do assunto (proxy léxico).
* polaridade    — fração das evidências com nota coerente com a intenção da pergunta
                  (pergunta sobre problemas -> nota <= 3; sobre elogios -> nota >= 4).
                  Calculada só nas perguntas com intenção definida.
* redundancia   — similaridade de cosseno média entre pares de evidências (menor = mais diverso).
* temas         — número de temas distintos cobertos pelas evidências.
* recusas       — perguntas não respondíveis corretamente recusadas (de 6).

Uso:  python eval/ablation.py
"""
from __future__ import annotations

import itertools
import json
import re
import sys
from dataclasses import replace
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from voc_rag import config  # noqa: E402
from voc_rag.query import plan_query  # noqa: E402
from voc_rag.retriever import HybridRetriever  # noqa: E402
from voc_rag.text import normalize  # noqa: E402

OFF = dict(use_support_check=False, use_coverage=False, use_mmr=False, use_decomposition=False)
VARIANTS = [
    # (nome, filtros inferidos da pergunta?, configuração do retriever)
    ("A. Somente densa (top-k por cosseno)", False, dict(sources="dense", **OFF)),
    ("B. Somente BM25", False, dict(sources="bm25", **OFF)),
    ("C. Híbrida (RRF)", False, dict(sources="hybrid", **OFF)),
    ("D. C + filtros de metadados inferidos", True, dict(sources="hybrid", **OFF)),
    ("E. D + verificação de suporte e cobertura IDF", True,
     dict(sources="hybrid", use_support_check=True, use_coverage=True, use_mmr=False,
          use_decomposition=False)),
    ("F. E + MMR", True,
     dict(sources="hybrid", use_support_check=True, use_coverage=True, use_mmr=True,
          use_decomposition=False)),
    ("G. Pipeline completo (F + decomposição por tema)", True, dict(sources="hybrid")),
]


def evaluate(retriever: HybridRetriever, questions: list[dict], auto_filters: bool) -> dict:
    row_of = {rid: i for i, rid in enumerate(retriever.df["review_id"])}
    prec, pol, red, themes, refusals = [], [], [], [], 0
    for q in questions:
        plan = plan_query(q["question"], auto_filters=auto_filters)
        result = retriever.retrieve(plan)
        if not q["answerable"]:
            refusals += int(not result.sufficient)
            continue
        ev = result.evidences if result.sufficient else []
        if q.get("relevance"):
            rx = re.compile(q["relevance"])
            prec.append(np.mean([bool(rx.search(normalize(e.text))) for e in ev]) if ev else 0.0)
        if plan.intent == "negativo":
            pol.append(np.mean([e.score <= 3 for e in ev]) if ev else 0.0)
        elif plan.intent == "positivo":
            pol.append(np.mean([e.score >= 4 for e in ev]) if ev else 0.0)
        if len(ev) > 1:
            vec = retriever.vectors[[row_of[e.review_id] for e in ev]]
            red.append(np.mean([float(vec[i] @ vec[j])
                                for i, j in itertools.combinations(range(len(ev)), 2)]))
        themes.append(len({t for e in ev for t in e.themes}))
    return {"precisao": float(np.mean(prec)), "polaridade": float(np.mean(pol)),
            "redundancia": float(np.mean(red)), "temas": float(np.mean(themes)),
            "recusas": refusals}


def main() -> None:
    questions = json.loads((ROOT / "eval" / "questions.json").read_text())
    retriever = HybridRetriever()
    backend = retriever.manifest["embedding_backend"]
    n_unanswerable = sum(not q["answerable"] for q in questions)
    rows = []
    for name, auto, overrides in VARIANTS:
        retriever.cfg = replace(config.RETRIEVAL, **overrides)
        m = evaluate(retriever, questions, auto)
        rows.append((name, m))
        print(f"{name:<52} " + "  ".join(f"{k}={v:.2f}" if isinstance(v, float) else f"{k}={v}"
                                          for k, v in m.items()))

    md = ["# Estudo de ablação da recuperação", "",
          f"Embeddings: `{backend}` · {len(questions)} perguntas de `eval/questions.json` "
          f"({len(questions) - n_unanswerable} respondíveis, {n_unanswerable} a recusar) · "
          "gerado por `python eval/ablation.py`.", "",
          "| Variante | Precisão (proxy) | Polaridade coerente | Redundância (↓) | "
          f"Temas distintos | Recusas corretas (de {n_unanswerable}) |",
          "|---|---|---|---|---|---|"]
    for name, m in rows:
        md.append(f"| {name} | {m['precisao']:.2f} | {m['polaridade']:.2f} | "
                  f"{m['redundancia']:.2f} | {m['temas']:.1f} | {m['recusas']} |")
    md += ["", "Definições das métricas no cabeçalho de `eval/ablation.py`. As variantes A–C "
           "não inferem filtros da pergunta; a recusa nessas variantes vem apenas da regra de "
           "escopo (dados transacionais), pois a verificação de suporte está desligada.", ""]
    out = ROOT / "docs" / "ablacao.md"
    out.write_text("\n".join(md))
    print("Relatório:", out)


if __name__ == "__main__":
    main()

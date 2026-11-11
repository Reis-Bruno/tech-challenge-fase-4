"""Avaliação automática do pipeline.

Métricas:
* guardrail_accuracy — acerto na decisão responder × recusar (perguntas fora de escopo).
* precision@k (proxy) — fração das evidências cujo texto contém termos do assunto da
  pergunta (padrão `relevance` definido manualmente em questions.json). É um proxy
  lexical: subestima relevância de paráfrases, mas é reprodutível sem rótulos humanos.
* filter_compliance — evidências que respeitam os filtros de metadados (deve ser 100%).
* answers_with_invalid_citations / answers_without_citation — só fazem sentido com LLM:
  respostas que citam [R#] inexistente e respostas sem nenhuma citação.

Uso:  python eval/run_eval.py [--provider none|openai|...] [--out docs/avaliacao.md]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from voc_rag.pipeline import VoCPipeline  # noqa: E402
from voc_rag.text import normalize  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", default=None)
    ap.add_argument("--out", default=str(ROOT / "docs" / "avaliacao.md"))
    ap.add_argument("--examples", default=str(ROOT / "docs" / "exemplos.md"))
    args = ap.parse_args()

    questions = json.loads((ROOT / "eval" / "questions.json").read_text(encoding="utf-8"))
    pipe = VoCPipeline(provider=args.provider)
    rows, raw = [], []
    for q in questions:
        resp = pipe.ask(q["question"])
        f = resp.plan.filters
        prec = None
        if resp.sufficient and q.get("relevance"):
            rx = re.compile(q["relevance"])
            hits = [bool(rx.search(normalize(e.text))) for e in resp.evidences]
            prec = sum(hits) / len(hits) if hits else 0.0
        compliant = all(
            (f.min_score is None or e.score >= f.min_score)
            and (f.max_score is None or e.score <= f.max_score)
            and (not f.categories or e.category in f.categories)
            and (not f.delivery_status or e.delivery_status in f.delivery_status)
            and (not f.years or int(e.purchase_date[:4]) in f.years)
            for e in resp.evidences
        )
        rows.append({
            "id": q["id"], "question": q["question"], "expected": q["answerable"],
            "answered": resp.sufficient, "correct": resp.sufficient == q["answerable"],
            "mode": resp.retrieval.mode, "filters": f.describe(), "n_evid": len(resp.evidences),
            "precision": prec, "compliant": compliant,
            "invalid_cit": resp.citation_check["invalid_citations"],
            "uncited": resp.citation_check["uncited_answer"], "ms": sum(resp.timings.values()),
        })
        raw.append(resp)
        print(f"{q['id']} correct={rows[-1]['correct']} mode={rows[-1]['mode']} p={prec}")

    precs = [r["precision"] for r in rows if r["precision"] is not None]
    summary = {
        "backend": pipe.retriever.manifest["embedding_backend"],
        "generator": raw[0].generator if raw else "",
        "guardrail_accuracy": sum(r["correct"] for r in rows) / len(rows),
        "mean_precision_at_k": round(sum(precs) / len(precs), 3) if precs else None,
        "filter_compliance": sum(r["compliant"] for r in rows) / len(rows),
        "answers_with_invalid_citations": sum(bool(r["invalid_cit"]) for r in rows),
        "answers_without_citation": sum(r["uncited"] for r in rows),
        "mean_latency_ms": round(sum(r["ms"] for r in rows) / len(rows)),
    }
    print(json.dumps(summary, indent=2))

    gen = {r.generator for r in raw}
    md = ["# Avaliação automática", "",
          f"Backend de embeddings: `{summary['backend']}` · gerador(es): `{', '.join(sorted(gen))}`",
          "", "Gerado por `python eval/run_eval.py`.", "", "## Resumo", "",
          "| Métrica | Valor |", "|---|---|"]
    md += [f"| {k} | {v} |" for k, v in summary.items() if k not in ("backend", "generator")]
    md += ["", "## Por pergunta", "",
           "| ID | Pergunta | Esperado | Respondeu | Modo | Filtros inferidos | Evid. | Precisão@k (proxy) | Filtros ok |",
           "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        p = "—" if r["precision"] is None else f"{r['precision']:.2f}"
        md.append(f"| {r['id']} | {r['question']} | {'responder' if r['expected'] else 'recusar'} | "
                  f"{'sim' if r['answered'] else 'não'}{'' if r['correct'] else ' ❌'} | {r['mode']} | "
                  f"{r['filters']} | {r['n_evid']} | {p} | {'✔' if r['compliant'] else '✘'} |")
    Path(args.out).write_text("\n".join(md) + "\n", encoding="utf-8")

    ex = ["# Exemplos de perguntas e respostas", "",
          f"Gerados por `python eval/run_eval.py` (embeddings `{summary['backend']}`, "
          f"gerador `{', '.join(sorted(gen))}`).", ""]
    for resp in raw:
        ex += [f"## {resp.question}", "",
               f"*Modo:* `{resp.retrieval.mode}` · *filtros:* {resp.plan.filters.describe()} · "
               f"*população:* {resp.retrieval.population} avaliações", ""]
        if resp.plan.applied_rules:
            ex += ["*Transformações da pergunta:* " + "; ".join(resp.plan.applied_rules), ""]
        ex += ["```text", resp.answer, "```", ""]
        if resp.evidences:
            ex += ["| Ref | Nota | Data | Categoria | Entrega | Avaliação |", "|---|---|---|---|---|---|"]
            for e in resp.evidences:
                txt = e.text.replace("|", "/")
                ex.append(f"| {e.ref} | {e.score} | {e.purchase_date} | {e.category} | "
                          f"{e.delivery_status} | {txt} |")
            ex.append("")
    Path(args.examples).write_text("\n".join(ex) + "\n", encoding="utf-8")
    print(f"Relatórios: {args.out}, {args.examples}")


if __name__ == "__main__":
    main()

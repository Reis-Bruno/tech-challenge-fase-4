"""Interface de linha de comando.

Exemplos:
  python -m voc_rag.cli "Quais são os principais problemas relatados pelos clientes?"
  python -m voc_rag.cli "O que elogiam?" --categoria beleza_saude --ano 2018 --json
  python -m voc_rag.cli --interativo
"""
from __future__ import annotations

import argparse
import json

from .pipeline import RAGResponse, VoCPipeline
from .query import Filters


def render(resp: RAGResponse, verbose: bool = True) -> str:
    out = [f"\n❓ {resp.question}", "=" * 80, resp.answer, "=" * 80]
    if verbose:
        p = resp.plan
        out.append(f"modo: {resp.retrieval.mode} | gerador: {resp.generator} | "
                   f"filtros: {p.filters.describe()} | população: {resp.retrieval.population}")
        for rule in p.applied_rules:
            out.append(f"  regra: {rule}")
        out.append(f"  suficiência: {resp.retrieval.reason}")
        if resp.evidences:
            out.append("\nEvidências:")
            for e in resp.evidences:
                out.append(f"  [{e.ref}] nota {e.score} | {e.purchase_date} | {e.category} | "
                           f"{e.delivery_status} | sim={e.dense_sim} | {e.text[:150]}")
        out.append(f"\ntempos (ms): {resp.timings}")
    return "\n".join(out)


def main() -> None:
    ap = argparse.ArgumentParser(description="Voice of Customer RAG — Olist")
    ap.add_argument("pergunta", nargs="?")
    ap.add_argument("--interativo", action="store_true")
    ap.add_argument("--provider", help="openai | gemini | anthropic | ollama | none")
    ap.add_argument("--model")
    ap.add_argument("--k", type=int)
    ap.add_argument("--nota-min", type=int)
    ap.add_argument("--nota-max", type=int)
    ap.add_argument("--ano", type=int, action="append")
    ap.add_argument("--categoria", action="append")
    ap.add_argument("--entrega", action="append", choices=["no_prazo", "atrasado", "nao_entregue"])
    ap.add_argument("--sem-filtros-automaticos", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    filters = Filters(min_score=args.nota_min, max_score=args.nota_max, years=args.ano or [],
                      categories=args.categoria or [], delivery_status=args.entrega or [])
    pipe = VoCPipeline(provider=args.provider, model=args.model)

    def run(q: str) -> None:
        resp = pipe.ask(q, filters=filters, auto_filters=not args.sem_filtros_automaticos, k=args.k)
        print(json.dumps(resp.to_dict(), ensure_ascii=False, indent=2) if args.json else render(resp))

    if args.interativo:
        while True:
            try:
                q = input("\nPergunta (enter para sair): ").strip()
            except EOFError:
                break
            if not q:
                break
            run(q)
    elif args.pergunta:
        run(args.pergunta)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()

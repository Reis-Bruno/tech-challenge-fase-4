"""Orquestração do pipeline RAG completo:

pergunta -> processamento (QueryPlan) -> embedding -> recuperação híbrida -> contexto
-> geração (LLM ou extrativa) -> validação de citações -> resposta + evidências + trace
"""
from __future__ import annotations

import time
from dataclasses import asdict, dataclass, field

from . import config
from .generation import (LAST_MODEL_USED, SYSTEM_PROMPT, build_context, build_user_prompt, call_llm,
                         check_citations, extractive_answer, refusal_answer)
from .query import Filters, QueryPlan, plan_query
from .retriever import Evidence, HybridRetriever, RetrievalResult


@dataclass
class RAGResponse:
    question: str
    answer: str
    sufficient: bool
    evidences: list[Evidence]
    plan: QueryPlan
    retrieval: RetrievalResult
    context: str
    generator: str
    citation_check: dict
    timings: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "question": self.question,
            "answer": self.answer,
            "sufficient": self.sufficient,
            "generator": self.generator,
            "mode": self.retrieval.mode,
            "reason": self.retrieval.reason,
            "plan": self.plan.as_dict(),
            "population": self.retrieval.population,
            "theme_stats_population": self.retrieval.theme_stats_population,
            "theme_stats_retrieved": self.retrieval.theme_stats_retrieved,
            "evidences": [asdict(e) | {"ref": e.ref} for e in self.evidences],
            "citation_check": {k: v for k, v in self.citation_check.items() if k != "answer"},
            "trace": self.retrieval.trace,
            "timings": self.timings,
        }


class VoCPipeline:
    def __init__(self, provider: str | None = None, model: str | None = None):
        self.retriever = HybridRetriever()
        self.provider = (provider or config.LLM_PROVIDER).lower()
        self.model = model

    def ask(self, question: str, filters: Filters | None = None, auto_filters: bool = True,
            k: int | None = None) -> RAGResponse:
        t = {}
        t0 = time.perf_counter()
        plan = plan_query(question, filters, auto_filters=auto_filters)
        t["query_ms"] = round(1000 * (time.perf_counter() - t0))

        t0 = time.perf_counter()
        result = self.retriever.retrieve(plan, k=k)
        t["retrieval_ms"] = round(1000 * (time.perf_counter() - t0))

        context = build_context(plan, result) if result.sufficient else ""
        t0 = time.perf_counter()
        if not result.sufficient:
            answer, generator = refusal_answer(result), "guardrail"
        elif self.provider == "none":
            answer, generator = extractive_answer(plan, result), "extrativo"
        else:
            try:
                answer = call_llm(SYSTEM_PROMPT, build_user_prompt(question, context),
                                  self.provider, self.model)
                generator = f"llm:{self.provider}/{LAST_MODEL_USED.get(self.provider, '?')}"
            except Exception as exc:  # falha do provedor não derruba a aplicação
                answer = (extractive_answer(plan, result)
                          + f"\n\n(Aviso: falha ao chamar o LLM — {type(exc).__name__}: {exc}. "
                            "Exibindo resposta extrativa.)")
                generator = "extrativo(fallback)"
        t["generation_ms"] = round(1000 * (time.perf_counter() - t0))

        check = check_citations(answer, len(result.evidences) if result.sufficient else 0)
        return RAGResponse(
            question=question, answer=check["answer"], sufficient=result.sufficient,
            evidences=result.evidences if result.sufficient else [], plan=plan,
            retrieval=result, context=context, generator=generator, citation_check=check,
            timings=t,
        )

"""Etapa de recuperação: busca híbrida (densa + BM25), fusão RRF, deduplicação,
diversificação MMR e avaliação de suficiência das evidências.
"""
from __future__ import annotations

import json
import pickle
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from . import config
from .config import RetrievalConfig
from .embeddings import load_embedder
from .query import QueryPlan
from .text import normalize, stem_tokens
from .themes import THEMES, tag_themes, theme_frequencies, theme_matrix

@dataclass
class Evidence:
    rank: int
    review_id: str
    text: str
    score: int
    purchase_date: str
    category: str
    delivery_status: str
    delay_days: float | None
    customer_state: str
    dense_sim: float
    bm25_rank: int | None
    dense_rank: int | None
    rrf: float
    lexical_overlap: list[str]
    duplicates: int = 0
    themes: list[str] = field(default_factory=list)
    supported: bool = False
    subquery: str = ""  # tema que originou a evidência (modo pergunta ampla)

    @property
    def ref(self) -> str:
        return f"R{self.rank}"


@dataclass
class RetrievalResult:
    evidences: list[Evidence]
    sufficient: bool
    reason: str
    population: int  # avaliações que satisfazem os filtros
    theme_stats_population: list[dict]
    theme_stats_retrieved: list[dict]
    candidates: int
    max_dense_sim: float
    mode: str  # focado | amplo | recusado
    trace: dict


class HybridRetriever:
    def __init__(self, cfg: RetrievalConfig = config.RETRIEVAL):
        import chromadb

        self.cfg = cfg
        idx = config.INDEX_DIR
        if not (idx / "manifest.json").exists():
            raise FileNotFoundError("Índice não encontrado. Rode `python -m voc_rag.indexing`.")
        self.manifest = json.loads((idx / "manifest.json").read_text())
        self.df = pd.read_parquet(config.DOCUMENTS_FILE)
        self.embedder = load_embedder(idx)
        self.vectors = np.load(idx / "embeddings.npy")
        client = chromadb.PersistentClient(path=str(idx / "chroma"))
        self.collection = client.get_collection(self.manifest["collection"])
        with open(idx / "bm25.pkl", "rb") as fh:
            self.bm25 = pickle.load(fh)
        self.norm_text = self.df["text"].map(normalize)
        self._doc_stems = None
        self._themes = None
        self.threshold = cfg.dense_threshold.get(self.manifest["embedding_backend"], 0.4)

    # -- lazy caches ----------------------------------------------------------------------
    @property
    def doc_stems(self) -> list[set]:
        if self._doc_stems is None:
            self._doc_stems = [set(stem_tokens(t)) for t in self.df["text"]]
        return self._doc_stems

    @property
    def themes(self) -> pd.DataFrame:
        if self._themes is None:
            self._themes = theme_matrix(self.df["text"])
        return self._themes

    # -- etapas ---------------------------------------------------------------------------
    def _dense(self, qvec: np.ndarray, plan: QueryPlan) -> list[tuple[int, float]]:
        res = self.collection.query(
            query_embeddings=[qvec.tolist()],
            n_results=self.cfg.dense_candidates,
            where=plan.filters.to_chroma_where(),
            include=["metadatas", "distances"],
        )
        return [(int(m["row"]), 1.0 - float(d))
                for m, d in zip(res["metadatas"][0], res["distances"][0])]

    def _sparse(self, plan: QueryPlan, mask: np.ndarray) -> list[tuple[int, float]]:
        q_tokens = stem_tokens(plan.sparse_query)
        if not q_tokens:
            return []
        scores = self.bm25.get_scores(q_tokens)
        scores = np.where(mask, scores, -np.inf)
        top = np.argsort(-scores)[: self.cfg.sparse_candidates]
        return [(int(i), float(scores[i])) for i in top if np.isfinite(scores[i]) and scores[i] > 0]

    def _mmr(self, qvec: np.ndarray, cand: list[int], relevance: dict[int, float], k: int) -> list[int]:
        """Maximal Marginal Relevance: evita k evidências quase idênticas
        ("Muito bom", "Muito bom!"...) e cobre aspectos diferentes do tema."""
        if not cand:
            return []
        rel = np.array([relevance[c] for c in cand])
        rel = (rel - rel.min()) / (rel.max() - rel.min() + 1e-9)
        V = self.vectors[cand]
        selected: list[int] = []
        remaining = list(range(len(cand)))
        while remaining and len(selected) < k:
            if not selected:
                best = max(remaining, key=lambda i: rel[i])
            else:
                sims = V[remaining] @ V[selected].T
                redund = sims.max(axis=1)
                scores = self.cfg.mmr_lambda * rel[remaining] - (1 - self.cfg.mmr_lambda) * redund
                best = remaining[int(np.argmax(scores))]
            selected.append(best)
            remaining.remove(best)
        return [cand[i] for i in selected]

    def _dedup(self, rows: list[int]) -> tuple[list[int], dict[int, int]]:
        """Remove textos idênticos (normalizados) e textos curtíssimos.
        Guarda quantas cópias cada texto tinha (vira 'reforço' exibido na evidência)."""
        seen: dict[str, int] = {}
        dup_count: dict[int, int] = {}
        out: list[int] = []
        for row in rows:
            key = self.norm_text.iat[row].strip(" .!")
            if key in seen:
                dup_count[seen[key]] = dup_count.get(seen[key], 0) + 1
                continue
            seen[key] = row
            if len(self.df["text"].iat[row]) >= self.cfg.min_chars:
                out.append(row)
        return out, dup_count

    def _evidence(self, row: int, sim: float, rrf: float, overlap: list[str], dup: int,
                  dense_rank: int | None, bm25_rank: int | None, supported: bool,
                  subquery: str = "") -> Evidence:
        r = self.df.iloc[row]
        return Evidence(
            rank=0, review_id=r["review_id"], text=r["text"], score=int(r["review_score"]),
            purchase_date=r["purchase_date"], category=r["category"],
            delivery_status=r["delivery_status"],
            delay_days=None if pd.isna(r["delay_days"]) else float(r["delay_days"]),
            customer_state=r["customer_state"], dense_sim=round(float(sim), 3),
            bm25_rank=bm25_rank, dense_rank=dense_rank, rrf=round(rrf, 5),
            lexical_overlap=overlap, duplicates=dup, themes=tag_themes(r["text"]),
            supported=supported, subquery=subquery,
        )

    def _coverage(self, terms: set, doc: set) -> float:
        """Fração (ponderada por IDF) dos termos da pergunta presentes na avaliação.
        Evita que um verbo comum ("fazer") sustente sozinho uma pergunta fora do domínio."""
        if not terms:
            return 0.0
        w = {t: max(self.bm25.idf.get(t, 0.0), 0.0) or 1.0 for t in terms}
        return sum(w[t] for t in terms if t in doc) / sum(w.values())

    # -- modo focado: pergunta com assunto específico ---------------------------------------
    def _retrieve_focused(self, plan: QueryPlan, mask: np.ndarray, k: int, trace: dict):
        qvec = self.embedder.embed_query(plan.dense_query)
        dense = self._dense(qvec, plan) if self.cfg.sources in ("hybrid", "dense") else []
        sparse = self._sparse(plan, mask) if self.cfg.sources in ("hybrid", "bm25") else []
        trace["dense_hits"], trace["bm25_hits"] = len(dense), len(sparse)

        # Reciprocal Rank Fusion: combina rankings sem precisar calibrar escalas
        # (cosseno e BM25 não são comparáveis diretamente).
        dense_rank = {row: r for r, (row, _) in enumerate(dense, 1)}
        bm25_rank = {row: r for r, (row, _) in enumerate(sparse, 1)}
        rrf: dict[int, float] = {}
        for ranks in (dense_rank, bm25_rank):
            for row, r in ranks.items():
                rrf[row] = rrf.get(row, 0.0) + 1.0 / (self.cfg.rrf_k + r)
        fused = sorted(rrf, key=rrf.get, reverse=True)

        candidates, dup_count = self._dedup(fused)
        trace["candidates_after_dedup"] = len(candidates)

        # Suporte = a avaliação compartilha ao menos um termo de CONTEÚDO da pergunta
        # (ou sinônimo da expansão), ou tem similaridade densa acima do limiar calibrado.
        # Para perguntas sem termo de domínio exige-se as duas coisas.
        q_terms = set(plan.core) | ({s for s in stem_tokens(plan.sparse_query)} - set(stem_tokens(plan.original)))
        core = set(plan.core)
        sims_all = self.vectors[candidates] @ qvec if candidates else np.array([])
        supported_rows = []
        info = {}
        for row, sim in zip(candidates, sims_all):
            overlap = sorted(q_terms & self.doc_stems[row])
            if plan.scope_reason:
                ok = self._coverage(core, self.doc_stems[row]) >= 0.6 and sim >= self.threshold
            else:
                ok = bool(overlap) or sim >= self.threshold
            info[row] = (float(sim), overlap, ok)
            if ok or not self.cfg.use_support_check:
                supported_rows.append(row)
        trace["supported_candidates"] = len(supported_rows)

        # Relevância final = RRF ponderado pela cobertura (IDF) dos termos da pergunta:
        # favorece avaliações que tratam de TODOS os aspectos perguntados
        # (ex.: "diferente" + "anúncio") e não só do termo mais comum ("receber").
        relevance = {row: rrf[row] * (0.5 + self._coverage(core, self.doc_stems[row]))
                     for row in supported_rows} if core and self.cfg.use_coverage else rrf
        if self.cfg.use_mmr:
            selected = self._mmr(qvec, supported_rows, relevance, k)
        else:
            selected = sorted(supported_rows, key=relevance.get, reverse=True)[:k]
        evidences = [self._evidence(row, info[row][0], rrf[row], info[row][1],
                                    dup_count.get(row, 0), dense_rank.get(row),
                                    bm25_rank.get(row), True) for row in selected]
        return evidences, qvec, len(supported_rows), (max(sims_all) if len(sims_all) else 0.0)

    # -- modo amplo: "quais os principais problemas?" ---------------------------------------
    def _retrieve_broad(self, plan: QueryPlan, mask: np.ndarray, pop_stats: list[dict],
                        k: int, trace: dict):
        """Decomposição da pergunta: uma subconsulta por tema frequente da população.

        Top-k puro numa pergunta genérica devolve avaliações "parecidas com a pergunta"
        (ex.: textos com a palavra "problema"), não as mais representativas. Aqui, as
        evidências são escolhidas por tema — proporcional à frequência — e cada uma
        CONTÉM o tema (casamento por padrão), o que garante rastreabilidade insight→evidência.
        """
        themes = [t["theme"] for t in pop_stats[:4]]
        trace["subqueries"] = [THEMES[t]["label"] for t in themes]
        per_theme = max(2, k // max(1, len(themes)))
        evidences: list[Evidence] = []
        used: set[int] = set()
        for theme in themes:
            label = THEMES[theme]["label"]
            qvec = self.embedder.embed_query(f"{label}. {plan.original}")
            rows = np.where(mask & self.themes[theme].to_numpy())[0]
            if not len(rows):
                continue
            sims = self.vectors[rows] @ qvec
            order = rows[np.argsort(-sims)][:200]
            cand, dup = self._dedup([int(r) for r in order if int(r) not in used])
            rel = {r: float(self.vectors[r] @ qvec) for r in cand}
            for row in self._mmr(qvec, cand, rel, per_theme):
                used.add(row)
                evidences.append(self._evidence(row, rel[row], 0.0, [theme], dup.get(row, 0),
                                                None, None, True, subquery=label))
        return evidences, len(evidences)

    def retrieve(self, plan: QueryPlan, k: int | None = None) -> RetrievalResult:
        k = k or self.cfg.final_k
        trace: dict = {"embedding_backend": self.manifest["embedding_backend"],
                       "dense_threshold": self.threshold}
        mask = plan.filters.mask(self.df).to_numpy()
        population = int(mask.sum())
        polarity = {"negativo": "neg", "positivo": "pos"}.get(plan.intent)
        pop_stats = theme_frequencies(self.themes[mask], polarity) if population else []

        evidences: list[Evidence] = []
        n_supported, max_sim, qvec, mode = 0, 0.0, None, "recusado"
        if plan.in_scope and population:
            if plan.broad and pop_stats and self.cfg.use_decomposition:
                mode = "amplo"
                evidences, n_supported = self._retrieve_broad(plan, mask, pop_stats, k, trace)
            else:
                mode = "focado"
                evidences, qvec, n_supported, max_sim = self._retrieve_focused(plan, mask, k, trace)
        for i, e in enumerate(evidences, 1):
            e.rank = i

        if not plan.in_scope:
            sufficient, reason = False, plan.scope_reason
        elif population == 0:
            sufficient, reason = False, "Nenhuma avaliação satisfaz os filtros aplicados."
        elif n_supported < self.cfg.min_evidence and self.cfg.use_support_check:
            sufficient = False
            reason = (f"Apenas {n_supported} avaliação(ões) da base têm relação verificável com a "
                      f"pergunta (mínimo exigido: {self.cfg.min_evidence}).")
            if plan.scope_reason:
                reason += " " + plan.scope_reason
        else:
            sufficient = True
            reason = (f"{n_supported} avaliações sustentam a pergunta; "
                      f"{len(evidences)} selecionadas como evidência.")
        if not sufficient:
            mode = "recusado"

        # Frequência de temas na "subpopulação do assunto": avaliações (dentro dos filtros)
        # que mencionam algum termo de conteúdo da pergunta ou sinônimo da expansão.
        # Definição lexical e determinística -> o número exibido é reproduzível/auditável.
        ret_stats: list[dict] = []
        if sufficient and mode == "focado":
            q_terms = set(plan.core) | (set(stem_tokens(plan.sparse_query))
                                        - set(stem_tokens(plan.original)))
            rows = [i for i in np.where(mask)[0] if q_terms & self.doc_stems[i]]
            if len(rows) < 30 and qvec is not None:  # assunto raro: usa vizinhos densos
                res = self.collection.query(query_embeddings=[qvec.tolist()],
                                            n_results=min(self.cfg.theme_sample, population),
                                            where=plan.filters.to_chroma_where(),
                                            include=["metadatas"])
                rows = [int(m["row"]) for m in res["metadatas"][0]]
            ret_stats = theme_frequencies(self.themes.iloc[rows], polarity)
            trace["theme_sample_size"] = len(rows)

        return RetrievalResult(
            evidences=evidences if sufficient else evidences[:3],
            sufficient=sufficient, reason=reason, population=population,
            theme_stats_population=pop_stats, theme_stats_retrieved=ret_stats,
            candidates=n_supported, max_dense_sim=round(float(max_sim), 3), mode=mode,
            trace=trace,
        )

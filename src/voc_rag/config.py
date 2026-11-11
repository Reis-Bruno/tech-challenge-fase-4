"""Configuração central do projeto (lida de variáveis de ambiente / arquivo .env)."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

try:  # python-dotenv é opcional
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:  # pragma: no cover
    pass

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = Path(os.getenv("VOC_RAW_DIR", ROOT / "data" / "raw"))
PROCESSED_DIR = Path(os.getenv("VOC_PROCESSED_DIR", ROOT / "data" / "processed"))
INDEX_DIR = Path(os.getenv("VOC_INDEX_DIR", ROOT / "data" / "index"))

DOCUMENTS_FILE = PROCESSED_DIR / "reviews_documents.parquet"
DATA_REPORT_FILE = PROCESSED_DIR / "data_report.json"

# Backend de embeddings: "fastembed" (neural, multilíngue, padrão) ou "lsa" (TF-IDF+SVD, 100% offline)
EMBEDDING_BACKEND = os.getenv("VOC_EMBEDDING_BACKEND", "fastembed")
FASTEMBED_MODEL = os.getenv(
    "VOC_FASTEMBED_MODEL", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# LLM: openai | gemini | anthropic | ollama | none (modo extrativo, sem LLM)
# Padrão: Gemini quando houver chave no ambiente; caso contrário, modo extrativo.
_HAS_GEMINI_KEY = bool(os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"))
LLM_PROVIDER = os.getenv("VOC_LLM_PROVIDER", "gemini" if _HAS_GEMINI_KEY else "none").lower()
LLM_MODEL = os.getenv("VOC_LLM_MODEL", "")
LLM_TEMPERATURE = float(os.getenv("VOC_LLM_TEMPERATURE", "0.1"))
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")

DEFAULT_MODELS = {
    "openai": "gpt-4o-mini",
    "gemini": "gemini-3.5-flash",
    "anthropic": "claude-haiku-5-5",
    "ollama": "llama3.1:8b",
}

# Modelos reserva: usados quando o principal está sobrecarregado (HTTP 503/429).
FALLBACK_MODELS = {
    "gemini": ["gemini-3.5-flash-lite"],
}


@dataclass
class RetrievalConfig:
    """Parâmetros do retriever (comentados no README, seção de decisões)."""

    dense_candidates: int = 60  # candidatos vindos do índice vetorial
    sparse_candidates: int = 60  # candidatos vindos do BM25
    rrf_k: int = 60  # constante do Reciprocal Rank Fusion (valor do artigo de Cormack et al., 2009)
    final_k: int = 10  # avaliações enviadas ao LLM como evidência
    mmr_lambda: float = 0.7  # 1.0 = só relevância; 0.0 = só diversidade
    min_chars: int = 15  # evidências muito curtas ("ok", "bom") têm pouco valor explicativo
    # Suficiência: a resposta só é gerada com pelo menos `min_evidence` avaliações com
    # suporte. Suporte = compartilhar um termo de conteúdo com a pergunta OU passar do
    # limiar de similaridade abaixo. O limiar do LSA foi ajustado nas perguntas de teste;
    # o do fastembed é um valor inicial que ainda não foi calibrado.
    min_evidence: int = 3
    dense_threshold: dict = field(
        default_factory=lambda: {"fastembed": 0.45, "lsa": 0.20}
    )
    theme_sample: int = 300  # vizinhos densos usados nos temas quando o assunto é raro (< 30 menções)
    # Chaves de ablação (eval/ablation.py). No uso normal ficam todas ligadas.
    sources: str = "hybrid"  # hybrid | dense | bm25
    use_support_check: bool = True  # exige vínculo verificável pergunta-avaliação
    use_coverage: bool = True  # reordenação pela cobertura IDF dos termos da pergunta
    use_mmr: bool = True  # diversificação das evidências finais
    use_decomposition: bool = True  # perguntas amplas -> subconsultas por tema


RETRIEVAL = RetrievalConfig()

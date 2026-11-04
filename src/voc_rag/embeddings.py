"""Etapa de representação vetorial.

Dois backends com a mesma interface:

* ``fastembed`` (padrão): ``paraphrase-multilingual-MiniLM-L12-v2`` em ONNX (quantizado)
  via biblioteca *fastembed*. Modelo treinado para similaridade semântica de frases em
  50+ idiomas (inclui PT-BR), 384 dimensões, roda em CPU sem PyTorch.
* ``lsa``: TF-IDF (uni+bigramas, sem acento) + SVD truncado (Latent Semantic Analysis),
  256 dimensões. Totalmente offline e determinístico; serve como baseline e como fallback
  para ambientes sem acesso ao HuggingFace.

Os vetores são sempre normalizados (norma L2 = 1), então produto interno = cosseno.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from . import config
from .text import stem_tokens


class Embedder:
    name: str
    dim: int

    def embed_documents(self, texts: list[str]) -> np.ndarray:  # pragma: no cover
        raise NotImplementedError

    def embed_query(self, text: str) -> np.ndarray:  # pragma: no cover
        raise NotImplementedError

    def save(self, directory: Path) -> None:
        pass


def _l2(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float32)
    n = np.linalg.norm(x, axis=-1, keepdims=True)
    return x / np.clip(n, 1e-12, None)


class FastEmbedEmbedder(Embedder):
    name = "fastembed"

    def __init__(self, model_name: str = config.FASTEMBED_MODEL):
        from fastembed import TextEmbedding  # import tardio: dependência pesada

        self.model_name = model_name
        self.model = TextEmbedding(model_name=model_name)
        self.dim = len(next(iter(self.model.embed(["teste"]))))

    def embed_documents(self, texts: list[str]) -> np.ndarray:
        return _l2(np.vstack(list(self.model.embed(texts, batch_size=128))))

    def embed_query(self, text: str) -> np.ndarray:
        return _l2(np.vstack(list(self.model.embed([text])))[0])


def _analyzer(text: str) -> list[str]:
    toks = stem_tokens(text)
    return toks + [f"{a}_{b}" for a, b in zip(toks, toks[1:])]  # uni + bigramas


class LSAEmbedder(Embedder):
    name = "lsa"

    def __init__(self, dim: int = 256):
        self.dim = dim
        self.vectorizer = None
        self.svd = None

    def fit(self, texts: list[str]) -> "LSAEmbedder":
        from sklearn.decomposition import TruncatedSVD
        from sklearn.feature_extraction.text import TfidfVectorizer

        # Mesmo pré-processamento do BM25 (sem acento, sem stopwords, stemming leve):
        # sem isso, perguntas dominadas por palavras funcionais ("qual a ... da ...")
        # geram vetores de consulta sem significado.
        self.vectorizer = TfidfVectorizer(
            analyzer=_analyzer, min_df=2, sublinear_tf=True
        )
        x = self.vectorizer.fit_transform(texts)
        self.svd = TruncatedSVD(n_components=self.dim, random_state=42).fit(x)
        return self

    def embed_documents(self, texts: list[str]) -> np.ndarray:
        return _l2(self.svd.transform(self.vectorizer.transform(texts)))

    def embed_query(self, text: str) -> np.ndarray:
        return self.embed_documents([text])[0]

    def save(self, directory: Path) -> None:
        import joblib

        joblib.dump({"vectorizer": self.vectorizer, "svd": self.svd, "dim": self.dim},
                    directory / "lsa.joblib")

    @classmethod
    def load(cls, directory: Path) -> "LSAEmbedder":
        import joblib

        state = joblib.load(directory / "lsa.joblib")
        obj = cls(state["dim"])
        obj.vectorizer, obj.svd = state["vectorizer"], state["svd"]
        return obj


def create_embedder(backend: str, corpus: list[str] | None = None) -> Embedder:
    """Cria um embedder novo (usado na indexação)."""
    if backend == "fastembed":
        return FastEmbedEmbedder()
    if backend == "lsa":
        if corpus is None:
            raise ValueError("LSA precisa do corpus para ser ajustado")
        return LSAEmbedder().fit(corpus)
    raise ValueError(f"Backend de embeddings desconhecido: {backend}")


def load_embedder(index_dir: Path) -> Embedder:
    """Carrega o MESMO embedder usado na indexação (lido do manifest do índice)."""
    manifest = json.loads((index_dir / "manifest.json").read_text())
    backend = manifest["embedding_backend"]
    if backend == "fastembed":
        return FastEmbedEmbedder(manifest.get("embedding_model", config.FASTEMBED_MODEL))
    if backend == "lsa":
        return LSAEmbedder.load(index_dir)
    raise ValueError(f"Backend de embeddings desconhecido no índice: {backend}")

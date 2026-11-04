"""Etapa de armazenamento e indexação.

* Índice vetorial: ChromaDB persistente (HNSW, distância cosseno) com metadados por
  avaliação — permite busca semântica com filtros (nota, período, categoria, entrega).
* Índice léxico: BM25 (rank-bm25) sobre tokens normalizados + stemming leve.
* Matriz de embeddings (.npy) alinhada às linhas do parquet, usada no MMR.

Uso:  python -m voc_rag.indexing [--backend fastembed|lsa]
"""
from __future__ import annotations

import argparse
import json
import pickle
import shutil
import time

import numpy as np
import pandas as pd

from . import config
from .embeddings import create_embedder
from .text import stem_tokens

COLLECTION = "olist_reviews"
METADATA_COLS = [
    "review_id", "order_id", "review_score", "sentiment", "purchase_date", "purchase_year",
    "purchase_yyyymm", "delivery_status", "delay_days", "category", "customer_state",
    "order_value",
]


def _metadata(row: pd.Series) -> dict:
    meta = {"row": int(row.name)}
    for col in METADATA_COLS:
        val = row[col]
        if isinstance(val, float) and np.isnan(val):
            continue  # Chroma não aceita None: chave ausente = valor desconhecido
        meta[col] = val.item() if hasattr(val, "item") else val
    return meta


def build_index(backend: str = config.EMBEDDING_BACKEND) -> None:
    import chromadb

    df = pd.read_parquet(config.DOCUMENTS_FILE)
    texts = df["text"].tolist()
    out = config.INDEX_DIR
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    t0 = time.time()
    embedder = create_embedder(backend, corpus=texts)
    vectors = embedder.embed_documents(texts)
    embedder.save(out)
    np.save(out / "embeddings.npy", vectors)
    print(f"[embeddings] {backend}: {vectors.shape} em {time.time() - t0:.1f}s")

    t0 = time.time()
    client = chromadb.PersistentClient(path=str(out / "chroma"))
    col = client.create_collection(COLLECTION, metadata={"hnsw:space": "cosine"},
                                   embedding_function=None)
    metas = [_metadata(r) for _, r in df.iterrows()]
    batch = 5000
    for i in range(0, len(df), batch):
        col.add(
            ids=df["review_id"].iloc[i:i + batch].tolist(),
            embeddings=vectors[i:i + batch].tolist(),
            documents=texts[i:i + batch],
            metadatas=metas[i:i + batch],
        )
    print(f"[chroma] {col.count()} documentos indexados em {time.time() - t0:.1f}s")

    t0 = time.time()
    from rank_bm25 import BM25Okapi

    bm25 = BM25Okapi([stem_tokens(t) or ["_"] for t in texts])
    with open(out / "bm25.pkl", "wb") as fh:
        pickle.dump(bm25, fh)
    print(f"[bm25] índice léxico criado em {time.time() - t0:.1f}s")

    manifest = {
        "embedding_backend": embedder.name,
        "embedding_model": getattr(embedder, "model_name", "tfidf+svd"),
        "dim": int(vectors.shape[1]),
        "documents": int(len(df)),
        "collection": COLLECTION,
        "built_at": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2))
    print(json.dumps(manifest, indent=2))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--backend", default=config.EMBEDDING_BACKEND, choices=["fastembed", "lsa"])
    build_index(ap.parse_args().backend)


if __name__ == "__main__":
    main()

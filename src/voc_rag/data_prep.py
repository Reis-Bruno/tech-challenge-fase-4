"""Etapa 1 — Construção da base de conhecimento.

Lê os CSVs do Olist, seleciona as avaliações com texto, limpa, trata ausentes,
enriquece cada avaliação com metadados do pedido/entrega/produto e salva um
único arquivo de documentos (1 avaliação = 1 documento).

Uso:  python -m voc_rag.data_prep
"""
from __future__ import annotations

import json
import re

import numpy as np
import pandas as pd

from . import config
from .text import clean_review_text, normalize

FILES = {
    "reviews": "olist_order_reviews_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "items": "olist_order_items_dataset.csv",
    "products": "olist_products_dataset.csv",
    "customers": "olist_customers_dataset.csv",
    "translation": "product_category_name_translation.csv",
}

_HAS_LETTERS = re.compile(r"[A-Za-zÀ-ÿ]{2,}")


def _read(name: str) -> pd.DataFrame:
    path = config.RAW_DIR / FILES[name]
    if not path.exists():
        raise FileNotFoundError(
            f"Arquivo {path} não encontrado. Rode `python scripts/download_data.py` "
            "ou copie os CSVs do Kaggle para data/raw/."
        )
    return pd.read_csv(path)


def _sentiment(score: int) -> str:
    if score <= 2:
        return "negativa"
    if score == 3:
        return "neutra"
    return "positiva"


def _main_category(items: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    """Uma categoria por pedido: a do item de maior preço (pedidos podem ter vários itens)."""
    it = items.merge(products[["product_id", "product_category_name"]], on="product_id", how="left")
    it = it.sort_values(["order_id", "price"], ascending=[True, False])
    agg = it.groupby("order_id").agg(
        category=("product_category_name", "first"),
        n_items=("order_item_id", "count"),
        order_value=("price", "sum"),
        freight_value=("freight_value", "sum"),
    )
    return agg.reset_index()


def integrity_checks(reviews: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame,
                     products: pd.DataFrame, customers: pd.DataFrame) -> dict:
    """Verificações de integridade feitas ANTES de qualquer transformação.

    Servem para (a) confirmar que os joins de enriquecimento não perdem nem multiplicam
    avaliações e (b) detectar leitura incorreta do CSV. Os comentários contêm quebras de
    linha dentro de campos entre aspas; um leitor que não trate isso desalinha as colunas
    e produz notas fora de 1–5. O pandas trata o caso corretamente, e a checagem
    `scores_fora_de_1_a_5` comprova.
    """
    msg = reviews["review_comment_message"].dropna().astype(str)
    reviews_per_order = reviews.groupby("order_id")["review_id"].nunique()
    orders_per_review = reviews.groupby("review_id")["order_id"].nunique()
    items_per_order = items.groupby("order_id")["order_item_id"].count()
    return {
        "avaliacoes_sem_pedido": int((~reviews["order_id"].isin(orders["order_id"])).sum()),
        "pedidos_sem_cliente": int((~orders["customer_id"].isin(customers["customer_id"])).sum()),
        "itens_sem_produto": int((~items["product_id"].isin(products["product_id"])).sum()),
        "pedidos_sem_itens": int((~orders["order_id"].isin(items["order_id"])).sum()),
        "scores_fora_de_1_a_5": int((~reviews["review_score"].isin([1, 2, 3, 4, 5])).sum()),
        "comentarios_com_quebra_de_linha": int(msg.str.contains(r"[\r\n]").sum()),
        "review_ids_em_mais_de_um_pedido": int((orders_per_review > 1).sum()),
        "pedidos_com_mais_de_uma_avaliacao": int((reviews_per_order > 1).sum()),
        "pedidos_com_mais_de_um_item": int((items_per_order > 1).sum()),
        "produtos_sem_categoria": int(products["product_category_name"].isna().sum()),
    }


def _statistics(df: pd.DataFrame) -> dict:
    """Números da base citados no README, calculados aqui para serem reproduzíveis."""
    from .themes import theme_matrix

    themes = theme_matrix(df["text"])
    late = (df["delivery_status"] == "atrasado").to_numpy()
    return {
        "nota_media_por_entrega": df.groupby("delivery_status")["review_score"].mean().round(2).to_dict(),
        "pct_sem_nenhum_tema": round(100 * float((~themes.any(axis=1)).mean()), 1),
        "atrasados_entregues": int(late.sum()),
        "pct_atrasados_dizendo_nao_recebi": round(100 * float(themes["nao_recebido"][late].mean()), 1),
    }


def build_documents() -> tuple[pd.DataFrame, dict]:
    reviews = _read("reviews")
    orders = _read("orders")
    items = _read("items")
    products = _read("products")
    customers = _read("customers")

    report: dict = {"total_reviews": int(len(reviews)),
                    "integrity": integrity_checks(reviews, orders, items, products, customers)}

    # --- Seleção: só avaliações com algum texto (título ou comentário) -----------------
    reviews["title"] = reviews["review_comment_title"].map(clean_review_text)
    reviews["message"] = reviews["review_comment_message"].map(clean_review_text)
    has_text = (reviews["title"] != "") | (reviews["message"] != "")
    report["reviews_with_text"] = int(has_text.sum())
    reviews = reviews[has_text].copy()

    # Mesmo review_id pode aparecer associado a mais de um pedido: mantemos 1 documento.
    before = len(reviews)
    reviews = reviews.drop_duplicates("review_id", keep="first")
    report["duplicated_review_ids_removed"] = int(before - len(reviews))

    # Texto do documento: título + comentário, sem repetir quando são iguais.
    def compose(row) -> str:
        t, m = row["title"], row["message"]
        if t and m and normalize(t) not in normalize(m):
            return f"{t}. {m}"
        return m or t

    reviews["text"] = reviews.apply(compose, axis=1)

    # Remove textos sem conteúdo linguístico (".", "..", "10", emojis soltos).
    valid = reviews["text"].str.contains(_HAS_LETTERS)
    report["removed_no_letters"] = int((~valid).sum())
    reviews = reviews[valid].copy()

    # --- Enriquecimento com metadados (desafio adicional) -------------------------------
    orders = orders.merge(customers[["customer_id", "customer_state"]], on="customer_id", how="left")
    for col in ("order_purchase_timestamp", "order_delivered_customer_date",
                "order_estimated_delivery_date"):
        orders[col] = pd.to_datetime(orders[col], errors="coerce")
    df = reviews.merge(
        orders[["order_id", "order_status", "order_purchase_timestamp",
                "order_delivered_customer_date", "order_estimated_delivery_date",
                "customer_state"]],
        on="order_id", how="left",
    )
    df = df.merge(_main_category(items, products), on="order_id", how="left")

    translation = _read("translation")
    tr = dict(zip(translation.iloc[:, 0], translation.iloc[:, 1]))

    # --- Tratamento de ausentes -------------------------------------------------------
    report["missing_category"] = int(df["category"].isna().sum())
    df["category_en"] = df["category"].map(tr).fillna("unknown")
    df["category"] = df["category"].fillna("desconhecida")
    df["customer_state"] = df["customer_state"].fillna("NA")
    df["order_status"] = df["order_status"].fillna("unknown")

    purchase = df["order_purchase_timestamp"]
    review_date = pd.to_datetime(df["review_creation_date"], errors="coerce")
    # Se a data da compra faltar, usamos a data da avaliação como aproximação do período.
    period_date = purchase.fillna(review_date)
    df["purchase_date"] = period_date.dt.strftime("%Y-%m-%d").fillna("")
    df["purchase_ym"] = period_date.dt.strftime("%Y-%m").fillna("")
    df["purchase_year"] = period_date.dt.year.fillna(0).astype(int)
    df["purchase_yyyymm"] = (period_date.dt.year * 100 + period_date.dt.month).fillna(0).astype(int)

    delivered = df["order_delivered_customer_date"]
    estimated = df["order_estimated_delivery_date"]
    delay = (delivered.dt.normalize() - estimated.dt.normalize()).dt.days
    df["delay_days"] = delay  # NaN quando o pedido não foi entregue
    df["delivery_days"] = (delivered - purchase).dt.days
    df["delivery_status"] = np.select(
        [delivered.isna(), delay > 0],
        ["nao_entregue", "atrasado"],
        default="no_prazo",
    )
    report["missing_delivery_date"] = int(delivered.isna().sum())

    df["sentiment"] = df["review_score"].map(_sentiment)
    df["n_chars"] = df["text"].str.len()
    df["order_value"] = df["order_value"].fillna(0.0).round(2)
    df["n_items"] = df["n_items"].fillna(0).astype(int)

    cols = [
        "review_id", "order_id", "text", "title", "message", "review_score", "sentiment",
        "review_creation_date", "purchase_date", "purchase_ym", "purchase_year",
        "purchase_yyyymm", "order_status", "delivery_status", "delay_days", "delivery_days",
        "category", "category_en", "customer_state", "n_items", "order_value", "n_chars",
    ]
    df = df[cols].reset_index(drop=True)
    # O enriquecimento não pode multiplicar nem perder avaliações (1 linha por review_id).
    assert df["review_id"].is_unique, "join de metadados duplicou avaliações"

    report.update(
        documents=int(len(df)),
        score_distribution={int(k): int(v) for k, v in df["review_score"].value_counts().sort_index().items()},
        delivery_status=df["delivery_status"].value_counts().to_dict(),
        median_chars=float(df["n_chars"].median()),
        max_chars=int(df["n_chars"].max()),
        exact_duplicate_texts=int(df["text"].map(normalize).duplicated().sum()),
        period=[df["purchase_date"][df["purchase_date"] != ""].min(), df["purchase_date"].max()],
        top_categories=df["category"].value_counts().head(10).to_dict(),
    )
    report["statistics"] = _statistics(df)
    return df, report


def main() -> None:
    config.PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df, report = build_documents()
    df.to_parquet(config.DOCUMENTS_FILE, index=False)
    config.DATA_REPORT_FILE.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    print(f"\n{len(df)} documentos salvos em {config.DOCUMENTS_FILE}")


if __name__ == "__main__":
    main()

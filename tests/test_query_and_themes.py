"""Testes unitários das etapas determinísticas (não exigem dados nem índice)."""
from voc_rag.generation import check_citations
from voc_rag.query import plan_query
from voc_rag.text import clean_review_text, stem_tokens
from voc_rag.themes import tag_themes


def test_clean_text():
    assert clean_review_text("  Muito\r\nbom!!!!!  ") == "Muito bom!!"
    assert clean_review_text(float("nan")) == ""


def test_stemming_matches_variants():
    assert set(stem_tokens("atrasou")) & set(stem_tokens("atrasado"))


def test_negative_intent_filters_low_scores():
    p = plan_query("Quais padrões aparecem nas avaliações de clientes insatisfeitos?")
    assert p.intent == "negativo" and p.filters.max_score == 2
    assert p.broad


def test_positive_intent_and_category():
    p = plan_query("O que os clientes mais elogiam em produtos de beleza?")
    assert p.filters.min_score == 4
    assert p.filters.categories == ["beleza_saude"]


def test_explicit_score_year_and_delivery():
    p = plan_query("O que dizem as avaliações nota 1 de 2017 de pedidos entregues com atraso?")
    assert (p.filters.min_score, p.filters.max_score) == (1, 1)
    assert p.filters.years == [2017]
    assert p.filters.delivery_status == ["atrasado"]


def test_focused_question_has_core_terms():
    p = plan_query("O que os clientes relatam sobre problemas relacionados à entrega?")
    assert not p.broad and "entreg" in p.core


def test_scope_detection():
    assert not plan_query("Qual foi o faturamento da Olist em 2018?").in_scope
    assert plan_query("Qual a capital da França?").scope_reason


def test_theme_tagging_handles_negation():
    assert tag_themes("Entrega sem problemas e sem defeitos.") == []
    assert "defeito_avaria" in tag_themes("Produto veio com defeito")
    assert "atraso_na_entrega" in tag_themes("Entrega atrasou 10 dias")


def test_citation_check_removes_invalid():
    out = check_citations("Atraso é comum [R1][R2] e [R9].", n_evidences=3)
    assert out["invalid_citations"] == [9]
    assert "[R9]" not in out["answer"]
    assert check_citations("Texto sem citação.", 3)["uncited_answer"]


def test_citation_check_accepts_grouped_citations():
    out = check_citations("Atrasos frequentes [R1, R2] e [R3; R12].", n_evidences=3)
    assert out["cited"] == [1, 2, 3] and out["invalid_citations"] == [12]
    assert not out["uncited_answer"]


def test_integrity_checks_detect_orphans_and_bad_scores():
    import pandas as pd

    from voc_rag.data_prep import integrity_checks

    reviews = pd.DataFrame({"review_id": ["r1", "r2", "r2"], "order_id": ["o1", "o2", "oX"],
                            "review_score": [5, 9, 1],
                            "review_comment_message": ["bom", "linha1\nlinha2", None]})
    orders = pd.DataFrame({"order_id": ["o1", "o2", "o3"], "customer_id": ["c1", "c2", "c9"]})
    items = pd.DataFrame({"order_id": ["o1", "o1", "o2"], "order_item_id": [1, 2, 1],
                          "product_id": ["p1", "p2", "p9"]})
    products = pd.DataFrame({"product_id": ["p1", "p2"], "product_category_name": ["a", None]})
    customers = pd.DataFrame({"customer_id": ["c1", "c2"]})
    out = integrity_checks(reviews, orders, items, products, customers)
    assert out["avaliacoes_sem_pedido"] == 1
    assert out["pedidos_sem_cliente"] == 1
    assert out["itens_sem_produto"] == 1
    assert out["pedidos_sem_itens"] == 1
    assert out["scores_fora_de_1_a_5"] == 1
    assert out["comentarios_com_quebra_de_linha"] == 1
    assert out["review_ids_em_mais_de_um_pedido"] == 1
    assert out["pedidos_com_mais_de_um_item"] == 1
    assert out["produtos_sem_categoria"] == 1

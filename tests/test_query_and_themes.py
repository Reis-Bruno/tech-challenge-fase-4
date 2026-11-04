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

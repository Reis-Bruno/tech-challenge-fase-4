"""Testes de integração: rodam somente se o índice já foi construído."""
import pytest

from voc_rag import config

pytestmark = pytest.mark.skipif(
    not (config.INDEX_DIR / "manifest.json").exists(), reason="índice não construído"
)


@pytest.fixture(scope="module")
def pipe():
    from voc_rag.pipeline import VoCPipeline

    return VoCPipeline(provider="none")


def test_answers_in_scope_with_evidence(pipe):
    r = pipe.ask("O que os clientes relatam sobre problemas relacionados à entrega?")
    assert r.sufficient and len(r.evidences) >= 3
    assert all(e.score <= 3 for e in r.evidences)  # filtro inferido respeitado
    assert r.citation_check["cited"]


@pytest.mark.parametrize("q", ["Qual a capital da França?", "Qual foi o faturamento da Olist em 2018?"])
def test_refuses_out_of_scope(pipe, q):
    r = pipe.ask(q)
    assert not r.sufficient and r.generator == "guardrail" and not r.evidences

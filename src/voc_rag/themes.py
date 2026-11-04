"""Taxonomia de temas da voz do cliente (por palavras-chave, sobre texto normalizado).

Por que existe: o RAG recupera as *k* avaliações mais relevantes, mas perguntas como
"quais problemas aparecem com MAIOR FREQUÊNCIA?" pedem uma noção de volume que top-k não
dá (10 avaliações não estimam frequência). Esta camada conta, de forma determinística e
auditável, quantas avaliações da população filtrada mencionam cada tema. Os números vão
para o contexto do LLM como "estatísticas de apoio" e são exibidos ao usuário.

Limitação conhecida (declarada ao usuário): é uma contagem por palavras-chave — tem falsos
negativos (paráfrases não previstas) e alguns falsos positivos (ex.: negação distante).
"""
from __future__ import annotations

import re
import warnings

import pandas as pd

from .text import normalize

THEMES: dict[str, dict] = {
    "atraso_na_entrega": {
        "label": "Atraso / demora na entrega",
        "polarity": "neg",
        "pattern": r"atras|demor|fora do prazo|passou do prazo|prazo (de entrega )?(vencido|expirado|esgotado)|ainda nao (chegou|recebi)|nao chegou ainda|esperando",
    },
    "nao_recebido": {
        "label": "Produto não recebido (até a data da avaliação)",
        "polarity": "neg",
        "pattern": r"nao (recebi|chegou|foi entregue|entreg)|nunca (chegou|recebi)|ate agora nada|nao recebemos|nao veio",
    },
    "produto_errado": {
        "label": "Produto errado / diferente do anunciado",
        "polarity": "neg",
        "pattern": r"errad|diferente|outro (produto|modelo)|nao (e|era) o (mesmo|que)|trocad|nao corresponde|nao condiz|cor (diferente|errada)|tamanho errado",
    },
    "itens_faltando": {
        "label": "Pedido incompleto / itens faltando",
        "polarity": "neg",
        "pattern": r"faltando|falta(ndo|ram|ou)? (um|uma|1|o|a|peca|item|unidade)|incomplet|veio (so|apenas) (um|uma|1)|recebi (so|apenas) (um|uma|1)|so (veio|chegou) (um|uma|1)",
    },
    "defeito_avaria": {
        "label": "Defeito / produto quebrado ou avariado",
        "polarity": "neg",
        "pattern": r"defeito|quebrad|danificad|avariad|nao funciona|parou de funcionar|rachad|amassad|veio estragad|com problema",
    },
    "qualidade_ruim": {
        "label": "Qualidade abaixo do esperado",
        "polarity": "neg",
        "pattern": r"qualidade (ruim|pessima|baixa|inferior|duvidosa)|ma qualidade|pessima qualidade|material (ruim|fraco)|fragil|frageis|falsificad|nao (e )?original|deixa a desejar",
    },
    "atendimento_vendedor": {
        "label": "Atendimento / comunicação com vendedor",
        "polarity": "neg",
        "pattern": r"sem (resposta|retorno)|nao (responde|respondem|retornam|deu retorno|tive retorno)|descaso|atendimento (ruim|pessimo|horrivel)|ninguem (responde|resolve)|falta de (respeito|comunicacao)",
    },
    "troca_reembolso": {
        "label": "Troca, devolução, cancelamento ou reembolso",
        "polarity": "neg",
        "pattern": r"troca|devolu|devolv|reembols|estorn|cancel|dinheiro de volta",
    },
    "entrega_rapida": {
        "label": "Entrega rápida / antes do prazo",
        "polarity": "pos",
        "pattern": r"(entrega|chegou|entregue|entregaram)[^.]{0,25}(rapid|antes do prazo|super rapid|no prazo|dentro do prazo|adiantad)|antes do prazo|rapidez|super rapid|muito rapid",
    },
    "qualidade_boa": {
        "label": "Boa qualidade do produto",
        "polarity": "pos",
        "pattern": r"(boa|otima|excelente|alta|otima) qualidade|\bde qualidade\b(?! (ruim|baixa|pessima|inferior|duvidosa))|qualidade (boa|otima|excelente|excepcional)|bem feito|muito bom|produto (bom|otimo|excelente|perfeito)",
    },
    "conforme_anunciado": {
        "label": "Produto conforme o anunciado",
        "polarity": "pos",
        "pattern": r"conforme (o )?(anunciad|descri|esperad|foto|combinado)|igual (a|ao|da|na) (foto|anuncio|descricao)|como (descrito|anunciado)|exatamente como",
    },
    "embalagem_boa": {
        "label": "Embalagem bem feita / bem protegido",
        "polarity": "pos",
        "pattern": r"bem embalad|embalagem (boa|otima|excelente|perfeita|caprichada|segura)|bem protegid|muito bem embalado",
    },
    "recomenda": {
        "label": "Recomenda a loja / compraria novamente",
        "polarity": "pos",
        "pattern": r"recomendo|comprarei novamente|compraria (de novo|novamente)|voltarei a comprar|super indico|indico",
    },
    "custo_beneficio": {
        "label": "Preço / custo-benefício",
        "polarity": "neutral",
        "pattern": r"custo.?beneficio|preco|barato|caro\b|vale (a pena|o preco)",
    },
}

_COMPILED = {k: re.compile(v["pattern"]) for k, v in THEMES.items()}

# Negações explícitas frequentes ("sem defeitos", "nenhum problema", "sem atraso") não
# devem contar como reclamação. Removemos essas expressões antes de casar os padrões.
_NEGATED = re.compile(
    r"\b(sem|nenhum|nenhuma|zero)\s+(nenhum\s+)?(problemas?|defeitos?|avarias?|atrasos?|"
    r"danos?|arranhoes?|amassados?|demora|quebrad\w*|danificad\w*)"
)


def _prep(text: str) -> str:
    return _NEGATED.sub(" ", normalize(text))


def tag_themes(text: str) -> list[str]:
    n = _prep(text)
    return [k for k, rx in _COMPILED.items() if rx.search(n)]


def theme_matrix(texts: pd.Series) -> pd.DataFrame:
    """DataFrame booleano (linhas = avaliações, colunas = temas)."""
    norm = texts.map(_prep)
    with warnings.catch_warnings():  # grupos de captura nos padrões são intencionais
        warnings.simplefilter("ignore", UserWarning)
        return pd.DataFrame({k: norm.str.contains(rx) for k, rx in _COMPILED.items()})


def theme_frequencies(matrix: pd.DataFrame, polarity: str | None = None, top: int = 8) -> list[dict]:
    """Frequência de cada tema na população (percentual sobre o total de linhas)."""
    if matrix.empty:
        return []
    keys = [k for k in THEMES if polarity is None or THEMES[k]["polarity"] in (polarity, "neutral")]
    counts = matrix[keys].sum().sort_values(ascending=False)
    total = len(matrix)
    return [
        {"theme": k, "label": THEMES[k]["label"], "count": int(c), "pct": round(100 * c / total, 1)}
        for k, c in counts.head(top).items() if c > 0
    ]

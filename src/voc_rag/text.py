"""Utilitários de normalização de texto em português."""
from __future__ import annotations

import re
import unicodedata

_WS = re.compile(r"\s+")
_REPEAT_PUNCT = re.compile(r"([!?.,])\1{2,}")
_TOKEN = re.compile(r"[a-z0-9]+")

# Lista curta de stopwords. NÃO inclui negações ("não", "nunca", "nada", "sem"), porque
# em avaliações elas invertem o sentido ("não chegou" vs "chegou"). Inclui algumas palavras
# de moldura das perguntas ("clientes", "avaliações", "principais"), que aparecem em quase
# toda pergunta e não ajudam a distinguir avaliações.
STOPWORDS = set(
    """a o as os um uma uns umas de da do das dos em no na nos nas por pelo pela pelos pelas
    para pra pro com e ou que se ao aos à às é foi era ser são estar está estão esta este isso
    isto esse essa aquele aquela me mim meu minha meus minhas seu sua seus suas dele dela eu voce você ele ela eles elas
    lhe lhes nos nós já mais muito muita muitos muitas bem como mas ate até sobre quais qual
    quais quem onde quando porque pois tem têm ter tinha havia há la lá aqui ai aí so só
    clientes cliente avaliacoes avaliacao avaliações avaliação relatam relatados relatadas
    principais aparecem existem quais sao mais""".split()
)


def clean_review_text(text) -> str:
    """Limpeza leve para o texto que vai para embeddings e para o usuário.

    Mantém acentos e capitalização (modelos multilíngues lidam bem com eles e a
    evidência exibida deve ser fiel ao original); remove quebras de linha,
    espaços repetidos e pontuação repetida em excesso.
    """
    if text is None or (isinstance(text, float) and text != text):  # NaN
        return ""
    text = str(text).replace("\r", " ").replace("\n", " ")
    text = _REPEAT_PUNCT.sub(r"\1\1", text)
    return _WS.sub(" ", text).strip()


def strip_accents(text: str) -> str:
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def normalize(text: str) -> str:
    """Minúsculas + sem acentos. Usado em BM25, regras de consulta e comparação."""
    return strip_accents(text.lower())


def tokenize(text: str, drop_stopwords: bool = True) -> list[str]:
    tokens = _TOKEN.findall(normalize(text))
    if drop_stopwords:
        tokens = [t for t in tokens if t not in _NORM_STOPWORDS and len(t) > 1]
    return tokens


def stem(token: str) -> str:
    """Stemmer leve (sufixos de plural/gênero/verbo mais comuns).

    Suficiente para BM25 casar "atrasou"/"atraso"/"atrasada" e "produtos"/"produto"
    sem depender de NLTK/RSLP (que exigiria download adicional).
    """
    for suf in ("amentos", "imentos", "amento", "imento", "acoes", "acao", "mente",
                "ados", "adas", "idos", "idas", "ando", "endo", "indo",
                "ado", "ada", "ido", "ida", "ou", "ar", "er", "ir",
                "os", "as", "es", "o", "a", "s"):
        if token.endswith(suf) and len(token) - len(suf) >= 4:
            return token[: -len(suf)]
    return token


def stem_tokens(text: str) -> list[str]:
    return [stem(t) for t in tokenize(text)]


_NORM_STOPWORDS = {normalize(w) for w in STOPWORDS}

"""Etapa de processamento/transformação da pergunta.

Transforma a pergunta em linguagem natural em uma ``QueryPlan``:

1. Normalização (minúsculas, sem acentos) para regras e BM25.
2. Extração de filtros de metadados implícitos na pergunta
   ("nota baixa" -> nota <= 2; "elogiam" -> nota >= 4; "em 2017"; categoria; "entregas atrasadas").
3. Expansão de consulta para o BM25 com sinônimos do domínio (ex.: entrega -> prazo, atraso,
   correios, transportadora). O índice denso não recebe a expansão: o modelo já captura a
   semântica e termos extras só diluiriam o vetor.
4. Checagem de escopo: perguntas que a base de avaliações não consegue responder
   (fora do domínio, ou que exigem dados transacionais como faturamento).

Escolhemos regras determinísticas (e não um LLM) para esta etapa porque são auditáveis,
gratuitas, instantâneas e funcionam também no modo sem LLM. As regras são exibidas na
interface ("pipeline trace"), o que dá rastreabilidade a cada filtro aplicado.
"""
from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field

from .text import normalize, tokenize

# ---------------------------------------------------------------------------------------
# Vocabulário do domínio
# ---------------------------------------------------------------------------------------
NEGATIVE_CUES = [
    "nota baixa", "notas baixas", "insatisf", "reclama", "problema", "ruim", "pessim",
    "negativ", "defeito", "frustra", "decepcion", "critica", "queixa", "pior",
]
STRONG_NEGATIVE_CUES = ["nota baixa", "notas baixas", "insatisf", "negativ", "pessim", "nota 1"]
POSITIVE_CUES = [
    "elogi", "positiv", "valoriz", "gostam", "gostaram", " satisfeit", "nota alta",
    "notas altas", "aprova", "melhor experiencia", "pontos fortes", "recomend",
]

# Sinônimos usados SÓ na expansão do BM25.
EXPANSIONS = {
    "entrega": "entrega prazo atraso atrasou chegou chegar recebi receber correios transportadora frete rapido demorou",
    "prazo": "prazo atraso atrasado demorou data previsto entrega",
    "atras": "atraso atrasou atrasado demorou prazo chegou ainda nao recebi",
    "qualidade": "qualidade material defeito quebrado fragil acabamento original falsificado",
    "atendimento": "atendimento vendedor loja contato resposta suporte sac retorno",
    "embalagem": "embalagem embalado caixa amassada avariada lacrado protegido",
    "preco": "preco barato caro custo beneficio valor",
    "troca": "troca devolucao reembolso estorno cancelamento dinheiro",
    "errado": "errado diferente trocado outro modelo cor tamanho veio",
    "faltando": "faltando incompleto faltou peca unidade veio so recebi apenas",
}

# Perguntas que exigem dados que NÃO estão nos textos das avaliações.
NON_TEXTUAL_CUES = [
    "faturamento", "receita total", "lucro", "margem", "ticket medio", "quantos pedidos",
    "numero de pedidos", "total de vendas", "valor total", "ceo", "acoes da", "cotacao",
    "market share", "funcionarios",
]

DOMAIN_TERMS = set(
    """produto produtos entrega entregas pedido pedidos compra compras comprar cliente clientes
    consumidor consumidores avaliacao avaliacoes review reviews comentario comentarios nota notas
    loja lojas vendedor vendedores qualidade atendimento prazo prazos preco precos frete embalagem
    experiencia experiencias reclamacao reclamacoes elogio elogios problema problemas insatisfacao
    satisfacao insatisfeitos satisfeitos atraso atrasos correios transportadora troca devolucao
    reembolso defeito recebi chegou categoria categorias olist ecommerce site marketplace
    padroes padrao temas tema motivos insatisfeito satisfeito elogiam valorizam relatam""".split()
)

CATEGORY_ALIASES = {
    "celular": "telefonia", "celulares": "telefonia", "smartphone": "telefonia",
    "telefone": "telefonia", "perfume": "perfumaria", "perfumes": "perfumaria",
    "relogio": "relogios_presentes", "relogios": "relogios_presentes",
    "movel": "moveis_decoracao", "moveis": "moveis_decoracao", "decoracao": "moveis_decoracao",
    "computador": "informatica_acessorios", "notebook": "informatica_acessorios",
    "informatica": "informatica_acessorios", "brinquedo": "brinquedos", "brinquedos": "brinquedos",
    "cama": "cama_mesa_banho", "toalha": "cama_mesa_banho", "lencol": "cama_mesa_banho",
    "beleza": "beleza_saude", "cosmetico": "beleza_saude", "cosmeticos": "beleza_saude",
    "esporte": "esporte_lazer", "esportes": "esporte_lazer", "bebe": "bebes", "bebes": "bebes",
    "automotivo": "automotivo", "carro": "automotivo", "pet": "pet_shop", "livro": "livros_interesse_geral",
    "livros": "livros_interesse_geral", "eletronico": "eletronicos", "eletronicos": "eletronicos",
    "eletrodomestico": "eletrodomesticos", "eletrodomesticos": "eletrodomesticos",
    "ferramenta": "ferramentas_jardim", "ferramentas": "ferramentas_jardim", "jardim": "ferramentas_jardim",
    "papelaria": "papelaria", "games": "consoles_games", "videogame": "consoles_games",
    "utilidades": "utilidades_domesticas", "cozinha": "utilidades_domesticas",
    "bolsa": "fashion_bolsas_e_acessorios", "bolsas": "fashion_bolsas_e_acessorios",
    "calcado": "fashion_calcados", "calcados": "fashion_calcados", "sapato": "fashion_calcados",
    "tenis": "fashion_calcados", "roupa": "fashion_roupa_masculina", "malas": "malas_acessorios",
    "climatizacao": "climatizacao", "ventilador": "climatizacao",
}


@dataclass
class Filters:
    min_score: int | None = None
    max_score: int | None = None
    years: list[int] = field(default_factory=list)
    categories: list[str] = field(default_factory=list)
    delivery_status: list[str] = field(default_factory=list)

    def is_empty(self) -> bool:
        return not (self.min_score or self.max_score or self.years or self.categories
                    or self.delivery_status)

    def to_chroma_where(self) -> dict | None:
        clauses: list[dict] = []
        if self.min_score is not None:
            clauses.append({"review_score": {"$gte": self.min_score}})
        if self.max_score is not None:
            clauses.append({"review_score": {"$lte": self.max_score}})
        if self.years:
            clauses.append({"purchase_year": {"$in": self.years}})
        if self.categories:
            clauses.append({"category": {"$in": self.categories}})
        if self.delivery_status:
            clauses.append({"delivery_status": {"$in": self.delivery_status}})
        if not clauses:
            return None
        return clauses[0] if len(clauses) == 1 else {"$and": clauses}

    def mask(self, df):
        m = df["review_score"].notna()
        if self.min_score is not None:
            m &= df["review_score"] >= self.min_score
        if self.max_score is not None:
            m &= df["review_score"] <= self.max_score
        if self.years:
            m &= df["purchase_year"].isin(self.years)
        if self.categories:
            m &= df["category"].isin(self.categories)
        if self.delivery_status:
            m &= df["delivery_status"].isin(self.delivery_status)
        return m

    def describe(self) -> str:
        parts = []
        if self.min_score is not None or self.max_score is not None:
            parts.append(f"nota {self.min_score or 1}–{self.max_score or 5}")
        if self.years:
            parts.append("ano " + ", ".join(map(str, self.years)))
        if self.categories:
            parts.append("categoria " + ", ".join(self.categories))
        if self.delivery_status:
            parts.append("entrega " + ", ".join(self.delivery_status))
        return "; ".join(parts) or "sem filtros"


@dataclass
class QueryPlan:
    original: str
    normalized: str
    dense_query: str
    sparse_query: str
    filters: Filters
    intent: str  # negativo | positivo | geral
    in_scope: bool
    core: list[str] = field(default_factory=list)  # termos de conteúdo (radicais)
    broad: bool = False  # pergunta ampla -> decomposição por temas
    scope_reason: str = ""
    applied_rules: list[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        d = asdict(self)
        d["filters"] = self.filters.describe()
        return d


def _has_any(text: str, cues: list[str]) -> bool:
    text = f" {text}"  # permite pistas com espaço inicial (" satisfeit" não casa "insatisfeito")
    return any(c in text for c in cues)


# Radicais genéricos: palavras de "moldura" da pergunta, que não dizem SOBRE O QUE ela é.
# Se, removidos estes, não sobra nenhum termo, a pergunta é "ampla" (ex.: "quais os
# principais problemas?") e é tratada por decomposição em subconsultas por tema.
GENERIC_WORDS = """produto produtos compra compras comprar pedido pedidos cliente clientes consumidor
    consumidores avaliacao avaliacoes experiencia experiencias padroes padrao recorrentes
    recorrente temas tema relatam relatados relatadas relatos relacionados relacionadas aspectos
    aspecto identificados identificar existem sustentam conclusao frequencia frequentes maior
    maiores principais motivos motivo loja lojas mais elogiam elogiados elogio elogios valorizam
    problemas problema reclamacoes reclamacao insatisfeitos insatisfeito insatisfacao satisfeitos
    satisfeito satisfacao nota notas baixa baixas alta altas podem pode ser sao quais dizem
    falam comentam comentarios positivos negativos positivas negativas pontos fortes fracos
    gostam gostaram ruins ruim boas bons insatisfatorias insatisfatoria criticas critica""".split()


def core_terms(question: str) -> list[str]:
    from .text import stem, stem_tokens

    generic = {stem(w) for w in GENERIC_WORDS}
    return [t for t in dict.fromkeys(stem_tokens(question)) if t not in generic
            and not t.isdigit() and t not in {stem(a) for a in CATEGORY_ALIASES}]


def plan_query(question: str, user_filters: Filters | None = None,
               auto_filters: bool = True) -> QueryPlan:
    q = question.strip()
    norm = normalize(q)
    tokens = tokenize(q, drop_stopwords=False)
    rules: list[str] = []
    filters = Filters() if user_filters is None else Filters(**asdict(user_filters))

    # ---- intenção / polaridade --------------------------------------------------------
    neg, pos = _has_any(norm, NEGATIVE_CUES), _has_any(norm, POSITIVE_CUES)
    intent = "geral"
    if neg and not pos:
        intent = "negativo"
    elif pos and not neg:
        intent = "positivo"

    if auto_filters:
        m = re.search(r"nota\s*([1-5])\b", norm)
        if m and filters.min_score is None and filters.max_score is None:
            filters.min_score = filters.max_score = int(m.group(1))
            rules.append(f"'nota {m.group(1)}' -> filtro nota = {m.group(1)}")
        elif filters.min_score is None and filters.max_score is None:
            # Pedidos de problemas/insatisfação: notas 1–2. Elogios: notas 4–5.
            # Para "problemas" genéricos (sem 'insatisfeito'/'nota baixa') usamos 1–3,
            # porque avaliações nota 3 frequentemente relatam problemas parciais.
            if intent == "negativo":
                strong = _has_any(norm, STRONG_NEGATIVE_CUES)
                filters.max_score = 2 if strong else 3
                rules.append(f"intenção negativa -> filtro nota <= {filters.max_score}")
            elif intent == "positivo":
                filters.min_score = 4
                rules.append("intenção positiva -> filtro nota >= 4")

        years = sorted({int(y) for y in re.findall(r"\b(2016|2017|2018)\b", norm)})
        if years and not filters.years:
            filters.years = years
            rules.append(f"ano(s) citados -> filtro {years}")

        if not filters.categories:
            cats = sorted({CATEGORY_ALIASES[t] for t in tokens if t in CATEGORY_ALIASES})
            if cats:
                filters.categories = cats
                rules.append(f"categoria citada -> filtro {cats}")

        if not filters.delivery_status and re.search(
            r"(entregues? com atraso|entregas? atrasad|pedidos? atrasad|chegaram atrasad)", norm
        ):
            filters.delivery_status = ["atrasado"]
            rules.append("'entregas atrasadas' -> filtro delivery_status = atrasado")

    # ---- expansão para BM25 -----------------------------------------------------------
    expansion = []
    for key, syn in EXPANSIONS.items():
        if key in norm:
            expansion.append(syn)
    if expansion:
        rules.append("expansão BM25 com sinônimos de: "
                     + ", ".join(k for k in EXPANSIONS if k in norm))
    sparse = " ".join([q] + expansion)

    # ---- escopo -----------------------------------------------------------------------
    in_scope, reason = True, ""
    if _has_any(norm, NON_TEXTUAL_CUES):
        in_scope = False
        reason = ("A pergunta exige dados transacionais/financeiros agregados, que não estão "
                  "nos textos das avaliações (base de conhecimento desta solução).")
    elif not (set(tokens) & DOMAIN_TERMS) and not any(t in CATEGORY_ALIASES for t in tokens):
        # Sem nenhum termo do domínio: candidata a fora de escopo. A decisão final
        # também considera a força da recuperação (ver retriever.assess_evidence).
        reason = "Nenhum termo do domínio de e-commerce/avaliações foi identificado na pergunta."
        rules.append("sem termos do domínio -> exigirá evidência forte")

    core = core_terms(q)
    broad = in_scope and not reason and not core
    if broad:
        rules.append("pergunta ampla (sem termo de conteúdo) -> decomposição em subconsultas "
                     "pelos temas mais frequentes da população filtrada")

    return QueryPlan(
        original=q, normalized=norm, dense_query=q, sparse_query=sparse, filters=filters,
        intent=intent, in_scope=in_scope, core=core, broad=broad, scope_reason=reason,
        applied_rules=rules,
    )

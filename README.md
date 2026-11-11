# Voice of Customer Intelligence com RAG — avaliações do Olist

Tech Challenge da Fase 4 — Pós Tech FIAP (IA para Devs)

Aplicação de RAG (Retrieval-Augmented Generation) sobre as avaliações escritas do
[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
Você faz uma pergunta em português, a aplicação busca as avaliações relacionadas e gera uma
resposta em que cada afirmação cita as avaliações usadas (`[R1]`, `[R2]`…). Se a base não tem
evidência suficiente, ela recusa e diz por quê.

## Sumário

1. [Ideia geral](#1-ideia-geral)
2. [Arquitetura](#2-arquitetura)
3. [Como rodar](#3-como-rodar)
4. [Base de conhecimento](#4-base-de-conhecimento)
5. [Pipeline RAG](#5-pipeline-rag)
6. [Problemas encontrados e como foram resolvidos](#6-problemas-encontrados-e-como-foram-resolvidos)
7. [Experimentos: o que foi testado e o que não foi](#7-experimentos-o-que-foi-testado-e-o-que-não-foi)
8. [Exemplos](#8-exemplos)
9. [Limitações](#9-limitações)
10. [Estrutura do repositório](#10-estrutura-do-repositório)

## 1. Ideia geral

A nota de uma avaliação diz se o cliente ficou satisfeito; o motivo está no comentário. Na
base do Olist, a nota média das avaliações com texto é 4,0 quando o pedido chega no prazo, 1,94
quando atrasa e 1,52 quando não é entregue.

Comecei pelo RAG mais simples: vetorizar os comentários, buscar os mais parecidos com a
pergunta e pedir um resumo ao modelo. Ele funcionou para perguntas com assunto definido ("o
que dizem sobre a entrega?") e falhou em três casos, que acabaram definindo o desenho do
projeto:

- **Perguntas amplas** ("quais os principais problemas?"): a busca devolvia avaliações
  parecidas com o texto da pergunta, como "Entrega sem problemas".
- **Perguntas de frequência** ("o que aparece mais?"): dez avaliações não dizem o que é mais
  comum entre 42 mil.
- **Perguntas sem resposta na base**: o modelo tende a responder mesmo assim.

A seção 6 conta como cada um foi tratado.

## 2. Arquitetura

```mermaid
flowchart TD
    subgraph OFF["Indexação (roda uma vez)"]
        A[CSVs do Olist] --> B[data_prep.py<br/>integridade · seleção · limpeza<br/>ausentes · metadados]
        B --> C[(reviews_documents.parquet<br/>42.114 documentos)]
        C --> D[embeddings.py]
        D --> E[(ChromaDB<br/>vetores + metadados)]
        C --> F[(BM25)]
    end

    subgraph ON["Consulta"]
        Q[Pergunta] --> P[query.py<br/>plano de consulta]
        P -->|fora de escopo| X[Recusa com motivo]
        P -->|focada| H[Busca vetorial + BM25<br/>com filtros de metadados]
        H --> R[RRF · suporte · cobertura IDF · MMR]
        P -->|ampla| T[Uma subconsulta por tema<br/>mais frequente]
        R --> S{Pelo menos 3 avaliações<br/>sustentam a pergunta?}
        T --> S
        S -->|não| X
        S -->|sim| K[Contexto: evidências numeradas<br/>+ frequência de temas]
        K --> G[Modelo de linguagem<br/>ou modo extrativo]
        G --> V[Validação das citações]
        V --> O[Resposta + evidências + rastreamento]
    end
    E -.-> H
    F -.-> H
```

| Etapa do enunciado | Onde está |
|---|---|
| Pergunta do usuário | `app/streamlit_app.py`, `src/voc_rag/cli.py` |
| Processamento da pergunta | `query.py` (`plan_query`) |
| Embeddings | `embeddings.py` |
| Recuperação | `retriever.py` (`HybridRetriever`) |
| Construção do contexto | `generation.py` (`build_context`) |
| Geração | `generation.py` (`call_llm`, `extractive_answer`) |
| Resposta fundamentada | `pipeline.py` (`VoCPipeline`) e `check_citations` |

## 3. Como rodar

Python 3.10+ e cerca de 1 GB de disco.

```bash
git clone https://github.com/Reis-Bruno/tech-challenge-fase-4.git
```

```bash
cd tech-challenge-fase-4
```

```bash
python -m venv .venv && source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
cp .env.example .env
```

**1. Dados.** O script usa `kagglehub` e precisa das credenciais do Kaggle
(`~/.kaggle/kaggle.json`). Se preferir, baixe o zip pelo site e extraia os CSVs em `data/raw/`.

```bash
python scripts/download_data.py
```

**2. Base de conhecimento.**

```bash
PYTHONPATH=src python -m voc_rag.data_prep
```

**3. Índices.** O backend `fastembed` baixa o modelo de embeddings (cerca de 220 MB) do
HuggingFace na primeira vez. Sem acesso ao HuggingFace, use `--backend lsa`.

```bash
PYTHONPATH=src python -m voc_rag.indexing --backend fastembed
```

**4. Modelo de linguagem.** O padrão é o Gemini. Crie uma chave em
<https://aistudio.google.com/apikey> e coloque no `.env`:

```bash
echo "GEMINI_API_KEY=sua-chave" >> .env
```

Sem chave, a aplicação roda no modo extrativo: organiza as evidências por tema e transcreve os
trechos, sem redigir conclusões. Para outro provedor, defina `VOC_LLM_PROVIDER` como `openai`,
`anthropic` ou `ollama` (e `VOC_LLM_MODEL`, se quiser trocar o modelo).

**5. Aplicação.**

```bash
streamlit run app/streamlit_app.py
```

```bash
PYTHONPATH=src python -m voc_rag.cli "O que os clientes relatam sobre problemas relacionados à entrega?"
```

**6. Testes e experimentos.**

```bash
python -m pytest -q
```

```bash
python eval/run_eval.py
```

```bash
python eval/ablation.py
```

O notebook [`notebooks/demonstracao_pipeline.ipynb`](notebooks/demonstracao_pipeline.ipynb)
mostra as etapas do pipeline com as saídas já executadas.

## 4. Base de conhecimento

Código em [`src/voc_rag/data_prep.py`](src/voc_rag/data_prep.py).

### De 99.224 avaliações a 42.114 documentos

| Etapa | Quantidade |
|---|---|
| Avaliações no CSV | 99.224 |
| Com título ou comentário | 42.687 |
| − `review_id` repetido (a mesma avaliação ligada a mais de um pedido) | −317 |
| − textos sem nenhuma palavra (só pontuação, números ou símbolos) | −256 |
| **Documentos indexados** | **42.114** |

As 56.537 avaliações sem texto ficam de fora porque não há o que recuperar nelas. A diferença
entre as 42.687 avaliações com texto e os 42.114 documentos vem das duas remoções da tabela:
317 + 256 = 573.

### Verificação de integridade

Antes de transformar qualquer coisa, o script confere as chaves entre as tabelas e a leitura do
CSV. O que ele encontrou na base:

| Verificação | Ocorrências | O que fiz com isso |
|---|---|---|
| Avaliações sem pedido, pedidos sem cliente, itens sem produto | 0 | nada a tratar |
| Notas fora de 1–5 | 0 | confirma que o CSV foi lido sem desalinhar colunas |
| Comentários com quebra de linha | 3.852 | exigem leitor que respeite campos entre aspas (o do pandas respeita) |
| Pedidos com mais de um item | 9.803 | categoria agregada por pedido antes do join, para não duplicar avaliações |
| Pedidos sem itens / produtos sem categoria | 775 / 610 | categoria `desconhecida` |
| `review_id` em mais de um pedido | 789 | um documento por `review_id` |

### Decisões de preparação

- **Uma avaliação = um documento, sem dividir em trechos.** O maior texto tem cerca de 230
  caracteres e a mediana é 54. Cada avaliação cabe inteira em um vetor, e dividir só
  atrapalharia a ligação entre evidência e avaliação.
- **Texto do documento** = título + comentário (o título é omitido quando já está no
  comentário).
- **Limpeza leve no texto exibido e vetorizado**: tiro quebras de linha, espaços e pontuação
  repetidos, e mantenho acentos e maiúsculas, para a evidência aparecer como o cliente
  escreveu. A normalização pesada (minúsculas, sem acento, radicais) vale só para o BM25 e para
  a contagem de temas.
- **Negações não são stopwords.** "Não chegou" e "chegou" não podem virar a mesma coisa.
- **Textos iguais de clientes diferentes** ("Muito bom", cerca de 6 mil casos) ficam no índice,
  porque são opiniões independentes. Na resposta eles aparecem uma vez, com a contagem de
  repetições. Textos com menos de 15 caracteres não entram como evidência.
- **Ausentes**: nenhuma avaliação com texto é descartada por falta de metadado. Categoria
  ausente (1.105 documentos) vira `desconhecida`; pedido sem data de entrega (1.867) vira
  `nao_entregue`.

### Metadados

Cada documento carrega nota, data e ano da compra, situação da entrega (`no_prazo`, `atrasado`,
`nao_entregue`), atraso em dias, categoria, UF e valor do pedido. O atraso é a data de entrega
menos a data **estimada**, e não o tempo total de entrega: o que o cliente reclama é do prazo
descumprido.

## 5. Pipeline RAG

**Plano de consulta** (`query.py`). A pergunta passa por regras que extraem:

- a intenção (problemas ou elogios) e os filtros que ela implica: problemas → notas 1 a 3
  (1 e 2 se a pergunta fala em "insatisfeitos" ou "nota baixa"); elogios → notas 4 e 5;
- filtros explícitos: "nota N", ano, categoria por apelido ("celular" → `telefonia`),
  "entregues com atraso";
- sinônimos para o BM25 ("entrega" ganha "prazo", "atraso", "correios"…); a busca vetorial usa
  a pergunta original;
- os termos de conteúdo: o que sobra depois de tirar palavras como "quais", "principais",
  "clientes", "problemas". Se não sobra nada, a pergunta é **ampla**; se sobra, é **focada**;
- o escopo: perguntas sobre faturamento ou número de pedidos são recusadas aqui.

Usei regras em vez de um LLM nessa etapa porque é ela que decide quais dados chegam ao modelo.
Com regras, a mesma pergunta gera sempre o mesmo plano, e a interface mostra cada regra
aplicada. O preço é que formulações que não previ podem não acionar os filtros.

**Recuperação** (`retriever.py`). Para pergunta focada:

1. busca vetorial no ChromaDB e busca BM25, 60 candidatos cada, já com os filtros aplicados;
2. fusão das duas listas por RRF (Reciprocal Rank Fusion), que usa só as posições;
3. textos idênticos agrupados e textos muito curtos descartados;
4. verificação de suporte: a avaliação precisa ter um termo de conteúdo da pergunta ou
   similaridade acima do limiar;
5. reordenação pela cobertura dos termos da pergunta, ponderada por IDF;
6. escolha das dez finais por MMR, que evita evidências quase iguais.

Para pergunta ampla, o sistema conta os temas na população filtrada, pega os quatro mais
frequentes e busca duas avaliações para cada um, entre as que contêm o tema. Os 14 temas
(atraso, não recebido, produto diferente, defeito, atendimento, entrega rápida, qualidade…)
são padrões de palavras-chave definidos em [`themes.py`](src/voc_rag/themes.py).

**Contexto e geração** (`generation.py`). O modelo recebe as evidências numeradas com seus
metadados e um bloco com a frequência dos temas:

```
[R2] (nota 3/5 | compra 2018-02-17 | categoria bebes | entregue com 9 dia(s) de atraso | UF SP)
"Produto com o prazo de entrega atrasado"
```

O prompt exige usar só o contexto, citar as evidências em cada afirmação, não generalizar a
partir de uma avaliação e dizer quando não há evidência. A temperatura é 0,1. Depois da
geração, `check_citations` troca citações a evidências que não existem por um aviso visível e
marca respostas sem citação.

**Recusa.** A aplicação não chama o modelo quando: a pergunta pede dados que não estão nos
textos; a pergunta é de fora do domínio e nenhuma avaliação cobre ao menos 60% dos seus termos
(ponderados por IDF); há menos de três avaliações com suporte; ou os filtros não deixam nenhuma
avaliação.

**Metadados na busca.** Os filtros entram na própria consulta (`where` do ChromaDB e máscara no
BM25), e não depois. "O que elogiam em produtos de beleza?" já busca só entre notas 4 e 5 da
categoria `beleza_saude`.

## 6. Problemas encontrados e como foram resolvidos

Quase todos os mecanismos do projeto nasceram de um erro que apareceu ao ler os resultados.

| O que deu errado | Como percebi | O que mudou |
|---|---|---|
| Pergunta "principais problemas" trazia "Entrega sem problemas" e "sem maiores problemas" | lendo as evidências da primeira versão | perguntas amplas passaram a ser decompostas por tema |
| Não dava para responder "o que é mais frequente" | dez evidências não representam 14 mil avaliações negativas | contagem de temas sobre toda a população filtrada, enviada junto com as evidências |
| "Como fazer um bolo de chocolate?" era aceita como pergunta válida | teste com perguntas fora do domínio; muitas avaliações têm o verbo "fazer" ("quero fazer a troca") | cobertura ponderada por IDF: "fazer" pesa pouco, "bolo" e "chocolate" pesam muito |
| "Capital da França" tinha similaridade 0,99 com "Acima da média.." | o vetor LSA da pergunta era dominado por "qual", "a", "da" | o LSA passou a usar o mesmo pré-processamento do BM25 (sem stopwords, com radicais) |
| "Clientes insatisfeitos" não era reconhecida como pergunta negativa | "insatisfeitos" contém "satisfeit", que eu usava como pista positiva | a pista positiva só vale no início da palavra |
| Pergunta sobre "produto diferente do anunciado" trazia "Produto recebido." | o termo "receber" dominava a busca; metade das evidências era irrelevante | reordenação pela cobertura de todos os termos da pergunta |
| "Sem defeitos" era contado como defeito | conferindo os temas atribuídos às evidências | negações explícitas são removidas antes de aplicar os padrões |
| 45,9% das avaliações de pedidos **entregues** com atraso diziam "não recebi" | o número parecia alto demais e fui conferir | muitas avaliações são escritas antes da entrega; o tema virou "não recebido (até a data da avaliação)" |
| Alerta falso de "resposta sem citação" | o Gemini escreve `[R1, R2]`, e o validador só reconhecia `[R1]` | o validador normaliza citações agrupadas |
| O modelo misturava dois percentuais na mesma frase | o contexto tinha dois blocos de estatísticas, sobre bases diferentes | o contexto passou a ter um bloco só |
| `gemini-2.5-flash` não existia mais e `gemini-3.8-flash` devolvia erro 503 | primeira chamada real à API | padrão `gemini-3.5-flash`, com nova tentativa e modelo reserva |

### Escolhas de tecnologia

| Escolha | Por quê | O que descartei |
|---|---|---|
| Embeddings `paraphrase-multilingual-MiniLM-L12-v2` via fastembed | suporta português, roda em CPU sem PyTorch, sem custo por chamada | modelos maiores (pouco ganho para textos de 50 caracteres) e embeddings por API |
| Backend alternativo LSA (TF-IDF + SVD) | roda sem HuggingFace; foi o que consegui executar | — |
| ChromaDB | local, sem servidor, com filtro de metadados na própria busca | FAISS (sem filtro pronto), Qdrant e pgvector (infraestrutura a mais) |
| Busca híbrida com RRF | avaliações têm paráfrases e também termos exatos, como nome de produto | combinar escores, que exigiria calibrar escalas diferentes |
| Temas por palavras-chave | contagem reproduzível sobre a base inteira, sem custo | clustering e classificação por LLM |
| Recusa antes de chamar o LLM | não depende de o modelo obedecer ao prompt | deixar só a instrução no prompt |

Parâmetros em `config.RetrievalConfig`: 60 candidatos por fonte, RRF com k = 60, dez
evidências, λ = 0,7 no MMR, mínimo de três evidências, limiar de similaridade 0,20 (LSA) e
0,45 (fastembed).

## 7. Experimentos: o que foi testado e o que não foi

### O que foi executado e o que é só expectativa

| Item | Situação |
|---|---|
| Pipeline completo com embeddings **LSA** e geração pelo **Gemini** (`gemini-3.5-flash`) | **Testado** nas 18 perguntas |
| Modo extrativo (sem LLM) | **Testado** |
| Ablação dos componentes da recuperação, com LSA | **Testado** |
| Verificações de integridade e 16 testes automatizados | **Testado** |
| Interface Streamlit | **Testado** só com o utilitário de testes do Streamlit (carrega e responde sem erro) |
| Backend de embeddings **fastembed** (o padrão do projeto) | **Não executado.** O ambiente de desenvolvimento não acessava o HuggingFace |
| Limiar de similaridade 0,45 do fastembed | **Chute inicial**, nunca calibrado |
| "Busca híbrida é melhor que BM25 sozinho" | **Hipótese.** Com LSA o BM25 sozinho foi melhor (tabela abaixo); espero que isso se inverta com o modelo neural, mas não medi |
| Provedores OpenAI, Anthropic e Ollama | **Implementados, nunca executados** |
| `scripts/download_data.py` | **Não executado** (Kaggle bloqueado no ambiente). Os CSVs vieram de uma cópia pública no GitHub. As contagens batem com as divulgadas para a base (99.224 avaliações, 99.441 pedidos), mas não comparei os arquivos com os do Kaggle |
| Precisão dos padrões de tema | **Não medida** |
| Fidelidade das respostas geradas | **Conferida à mão em duas respostas**, sem rotulagem sistemática |
| Desempenho em perguntas fora das 18 | **Desconhecido** |

As 18 perguntas estão em [`eval/questions.json`](eval/questions.json): doze respondíveis
(incluindo todos os exemplos do enunciado) e seis que devem ser recusadas.

### Ablação da recuperação (LSA, sem LLM)

`eval/ablation.py` começa com busca vetorial pura e liga um componente por vez.

| Variante | Precisão | Polaridade | Redundância (↓) | Temas | Recusas (de 6) |
|---|---|---|---|---|---|
| A. Só vetorial (top-k) | 0,63 | 0,64 | 0,73 | 1,0 | 2 |
| B. Só BM25 | 0,79 | 0,61 | 0,37 | 2,9 | 2 |
| C. Híbrida (RRF) | 0,75 | 0,66 | 0,52 | 1,7 | 2 |
| D. C + filtros inferidos | 0,74 | 1,00 | 0,49 | 1,8 | 2 |
| E. D + suporte e cobertura IDF | 0,75 | 1,00 | 0,53 | 1,9 | 6 |
| F. E + MMR | 0,81 | 1,00 | 0,40 | 2,6 | 6 |
| G. Pipeline completo (F + decomposição por tema) | 0,97 | 1,00 | 0,32 | 3,5 | 6 |

*Precisão*: fração das evidências que contêm termos do assunto. *Polaridade*: fração das
evidências com nota coerente com a pergunta. *Redundância*: cosseno médio entre as evidências.
*Temas*: temas distintos nas evidências.

O que a tabela mostra:

- Sem filtros, um terço das evidências de perguntas sobre problemas ou elogios tinha a nota
  errada para a pergunta (C → D).
- A verificação de suporte é o que recusa as quatro perguntas de fora do domínio (D → E).
- O MMR reduz a repetição entre evidências (E → F).
- A decomposição por tema dá o maior salto de precisão, nas cinco perguntas amplas (F → G).

O que a tabela **não** permite concluir:

- A polaridade 1,00 a partir de D é efeito direto do filtro, não um achado.
- O salto de G está inflado: nas perguntas amplas as evidências são escolhidas por padrões de
  tema parecidos com os que medem a precisão.
- B melhor que C contraria a justificativa da busca híbrida. Atribuo isso à fraqueza do LSA,
  mas é suposição até rodar com o fastembed.

### Avaliação de ponta a ponta (LSA + Gemini)

| Métrica | Resultado |
|---|---|
| Decisão responder/recusar correta | 18 de 18 |
| Precisão das evidências (mesmo proxy da ablação) | 0,97 |
| Evidências respeitando os filtros | 100% |
| Respostas com citação inexistente | 0 de 12 |
| Respostas sem citação | 0 de 12 |
| Tempo médio por pergunta | cerca de 11 s, quase todo na chamada ao Gemini |

Detalhe por pergunta em [`docs/avaliacao.md`](docs/avaliacao.md).

Esses números valem para estas 18 perguntas. Eu as escrevi durante o desenvolvimento e usei
parte delas para ajustar regras e limiares, então o resultado está otimista. A precisão mede se
a evidência fala do assunto, e não se ela sustenta a conclusão da resposta.

## 8. Exemplos

As respostas às 18 perguntas, com as evidências, estão em
[`docs/exemplos.md`](docs/exemplos.md). Um trecho:

**"Quais são os principais problemas relatados pelos clientes em suas avaliações?"**
(ampla; filtro inferido: notas 1 a 3; 14.438 avaliações)

```text
Os principais problemas relatados concentram-se em falhas de entrega (produtos não recebidos ou
com atraso), seguidos por demandas de troca, devolução ou cancelamento, e pelo recebimento de
itens errados ou divergentes do anunciado.

* Produto não recebido e atraso na entrega: Representa a maior parte das queixas por
  palavras-chave na base filtrada (26,6% para não recebido e 13,1% para atraso/demora). Os
  clientes relatam expressamente a ausência da entrega do item [R1], [R2] ou insatisfação com a
  demora e extrapolação do prazo [R3], [R4].
* Solicitações de troca, devolução, cancelamento ou reembolso: Presente em 12,1% dos casos da
  base filtrada [...] [R5] [...] [R6].
* Produto errado ou diferente do anunciado: Representa 8,1% das ocorrências na base filtrada.
  [...] [R7] [...] [R8].

Limitações: Análise baseada em uma amostra reduzida de depoimentos e estatísticas de
palavras-chave restritas a avaliações de nota 1 a 3.
```

**"Qual foi o faturamento da Olist em 2018?"**

```text
Não há evidências suficientes na base de avaliações para responder. Motivo: A pergunta exige
dados transacionais/financeiros agregados, que não estão nos textos das avaliações [...]
```

## 9. Limitações

- **Resultados com LSA.** É a principal. Tudo na seção 7 precisa ser refeito com
  `--backend fastembed`, e o limiar de 0,45 calibrado.
- **Avaliação pequena e feita por mim.** Falta testar com perguntas de outras pessoas e com
  alguém rotulando relevância e fidelidade.
- **Temas por palavras-chave.** Cerca de 39% das avaliações não caem em nenhum tema, então os
  percentuais são um piso. Negações longe do termo ainda enganam os padrões.
- **Negação na busca focada.** "Entrega sem problemas" (nota 3) ainda pode aparecer numa
  pergunta sobre problemas de entrega: tem os termos e passa no filtro de nota.
- **Regras de interpretação.** Cobrem as formulações que previ. Fora delas, o usuário precisa
  aplicar os filtros na barra lateral. Incluir a nota 3 nas perguntas sobre problemas traz
  reclamações parciais e, junto, alguns elogios moderados.
- **Sem inferência de causa.** A aplicação relata o que os clientes dizem; não conclui se a
  culpa foi da transportadora ou do vendedor quando eles não dizem.
- **Escala.** Tudo roda local, com o BM25 e os vetores em memória. Serve para dezenas de
  milhares de documentos. Num volume maior, o caminho seria uma plataforma como o Databricks
  (tabelas Delta, busca vetorial gerenciada, endpoint de modelo), que não implementei.

## 10. Estrutura do repositório

```
├── app/streamlit_app.py        interface web
├── src/voc_rag/
│   ├── config.py               caminhos, provedores e parâmetros
│   ├── text.py                 limpeza, normalização e radicais
│   ├── data_prep.py            integridade e construção da base
│   ├── embeddings.py           backends fastembed e LSA
│   ├── indexing.py             ChromaDB, BM25 e matriz de vetores
│   ├── query.py                plano de consulta, filtros e escopo
│   ├── themes.py               temas e frequências
│   ├── retriever.py            recuperação e suficiência
│   ├── generation.py           contexto, prompt, provedores e citações
│   ├── pipeline.py             orquestração
│   └── cli.py                  linha de comando
├── notebooks/                  demonstração executada do pipeline
├── eval/                       perguntas, avaliação e ablação
├── docs/                       resultados, exemplos e roteiro do vídeo
├── scripts/download_data.py    download via kagglehub
└── tests/                      testes unitários e de integração
```

Tecnologias: Python, pandas, scikit-learn, fastembed, ChromaDB, rank-bm25, Streamlit, Google
GenAI SDK, kagglehub e pytest.

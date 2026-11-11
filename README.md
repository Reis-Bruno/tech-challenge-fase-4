# Voice of Customer Intelligence com RAG — avaliações do Olist

Tech Challenge da Fase 4 — Pós Tech FIAP (IA para Devs)

Solução de RAG (Retrieval-Augmented Generation) que responde perguntas em linguagem natural
sobre as avaliações dos clientes do Olist. Cada resposta cita as avaliações que a sustentam e,
sem evidência suficiente, a solução recusa responder.

🎯 **Objetivo**

Responder perguntas como:

- Quais são os principais problemas relatados pelos clientes?
- O que os clientes relatam sobre problemas de entrega?
- Quais aspectos da compra são mais elogiados?
- Quais padrões aparecem nas avaliações de clientes insatisfeitos?

📊 **Base utilizada**

[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce),
baixada do Kaggle: avaliações, pedidos, itens, produtos e clientes. Das 99.224 avaliações,
42.114 têm texto e formam a base de conhecimento, cada uma com nota, data, situação da entrega,
atraso, categoria e UF.

## Métodos utilizados

| Etapa | Método |
|---|---|
| Preparação dos dados | verificação de integridade, limpeza leve, deduplicação e tratamento de ausentes; uma avaliação por documento |
| Embeddings | `paraphrase-multilingual-MiniLM-L12-v2` (fastembed) |
| Banco vetorial | ChromaDB, com filtros de metadados na própria busca |
| Busca | híbrida: vetorial + BM25, combinadas por RRF |
| Interpretação da pergunta | regras que inferem filtros (nota, ano, categoria, atraso) e separam perguntas amplas de focadas |
| Seleção das evidências | verificação de suporte, cobertura ponderada por IDF e MMR; perguntas amplas decompostas pelos temas mais frequentes |
| Frequência de temas | contagem de 14 temas por palavras-chave sobre a base filtrada |
| Geração | Gemini (`gemini-3.5-flash`), com citação obrigatória e validação das citações |
| Recusa | antes da geração, quando há menos de 3 evidências com suporte ou a pergunta está fora do escopo |

## Resultados

Avaliados em 18 perguntas: 12 respondíveis, incluindo todos os exemplos do enunciado, e 6 que
devem ser recusadas.

**Estudo de ablação** (recuperação, sem LLM):

| Variante | Precisão | Polaridade | Recusas corretas (de 6) |
|---|---|---|---|
| Só busca vetorial | 0,71 | 0,82 | 2 |
| Só BM25 | 0,79 | 0,62 | 2 |
| Busca híbrida (RRF) | 0,75 | 0,76 | 2 |
| + filtros de metadados | 0,80 | 1,00 | 2 |
| + verificação de suporte e cobertura IDF | 0,84 | 1,00 | 6 |
| + MMR | 0,82 | 1,00 | 6 |
| **Pipeline completo** (+ decomposição por tema) | **0,93** | **1,00** | **6** |

*Precisão*: fração das evidências que tratam do assunto da pergunta. *Polaridade*: fração das
evidências com nota coerente com a pergunta (problema ou elogio).

**Avaliação de ponta a ponta** (com Gemini):

| Métrica | Resultado |
|---|---|
| Decisão correta entre responder e recusar | 18 de 18 |
| Precisão das evidências | 0,93 |
| Respostas com citação inválida | 0 de 12 |
| Respostas sem citação | 0 de 12 |
| Tempo médio por resposta | cerca de 12 s |

O BM25 sozinho superou a busca híbrida em precisão, então a vantagem da busca híbrida não foi
confirmada nesta avaliação. As perguntas foram escritas durante o desenvolvimento, o que torna
os números otimistas.

⚙️ **Tecnologias:** Python • pandas • fastembed • ChromaDB • rank-bm25 • Google Gemini •
Streamlit • pytest

## Documentação

- [Instalação, arquitetura, decisões e limitações](docs/documentacao.md)
- [Ablação completa](docs/ablacao.md) · [Avaliação por pergunta](docs/avaliacao.md) ·
  [Exemplos de respostas](docs/exemplos.md)
- [Notebook com o pipeline executado](notebooks/demonstracao_pipeline.ipynb)

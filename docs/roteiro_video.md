# Roteiro do vídeo de apresentação (até 7 minutos)

O enunciado pede que o vídeo mostre, de forma objetiva: o problema de negócio, a arquitetura, a
estratégia do pipeline RAG, como ocorre a recuperação das avaliações, uma demonstração prática,
exemplos de perguntas, as evidências recuperadas e os principais desafios e decisões técnicas.
O roteiro abaixo cobre cada item na ordem dos slides. O texto falado completo de cada slide está
nas notas do apresentador do deck.

| Tempo | Slide | Item do enunciado | O que dizer ou mostrar |
|---|---|---|---|
| 0:00–0:15 | 1. Capa | — | Apresentação e o que será mostrado. |
| 0:15–0:50 | 2. Problema de negócio | Problema de negócio | Nota média 4,0 no prazo, 1,94 com atraso, 1,52 sem entrega; o motivo está no texto. Os três casos em que o RAG simples falhou. |
| 0:50–1:30 | 3. Arquitetura | Arquitetura proposta | Indexação (CSVs do Kaggle → data_prep → embeddings → ChromaDB + BM25) e consulta (plano → recuperação → suficiência → Gemini → validação). |
| 1:30–2:05 | 4. Base de conhecimento | Estratégia do RAG (base) | 99.224 → 42.114 documentos; uma avaliação por documento; verificação de integridade; negações preservadas; ausentes; metadados. |
| 2:05–2:40 | 5. Plano de consulta | Estratégia do RAG (transformação da pergunta) | Exemplo “elogios em beleza” → intenção, filtros, pergunta ampla. Por que regras e não LLM. |
| 2:40–3:15 | 6. Recuperação | Como ocorre a recuperação | Pergunta focada: híbrida + RRF + suporte + IDF + MMR. Pergunta ampla: subconsultas pelos temas mais frequentes. |
| 3:15–3:45 | 7. Evidências e recusa | Evidências; falta de evidência | Evidência numerada com metadados; citação obrigatória e validada; recusa antes de chamar o Gemini. |
| 3:45–5:15 | 8. Demonstração | Demonstração prática; exemplos de perguntas; evidências | No Streamlit: (1) principais problemas, (2) problemas de entrega com o rastreamento aberto, (3) elogios em beleza, (4) faturamento em 2018 recusado. |
| 5:15–5:55 | 9. Ablação | Desafios e decisões (justificativa medida) | Contribuição de cada componente; BM25 acima da híbrida em precisão (vantagem da híbrida não confirmada). |
| 5:55–6:15 | 10. Ponta a ponta | Evidências; resultados | 18/18 decisões corretas, precisão 0,93, nenhuma citação inválida; percentuais vêm da contagem de temas. |
| 6:15–6:40 | 11. Desafios | Principais desafios e decisões técnicas | Problemas encontrados e a decisão que cada um gerou. |
| 6:40–7:00 | 12. Limitações | — | Avaliação pequena, híbrida não confirmada, temas como piso; link do repositório. |

## Preparação para a gravação

- Deixe o Streamlit aberto antes de gravar, com o índice fastembed e o `.env` com
  `GEMINI_API_KEY=` configurados. A primeira pergunta demora mais porque carrega os índices:
  faça uma pergunta de aquecimento antes de começar.
- Na demonstração, cada resposta leva cerca de 12 s. Use esse tempo para comentar o filtro
  inferido e o gráfico de temas.
- Se o Gemini falhar durante a gravação, a interface mostra a resposta extrativa com um aviso.
  Diga isso e siga: as evidências e a recusa continuam funcionando.
- O tempo total previsto é de 7 minutos exatos. Se passar, encurte a fala dos slides 4 e 11.

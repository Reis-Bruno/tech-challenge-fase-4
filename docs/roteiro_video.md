# Roteiro sugerido para o vídeo (≤ 7 min)

| Tempo | Bloco | O que mostrar |
|---|---|---|
| 0:00–0:45 | **Problema de negócio** | Milhares de avaliações em texto livre; nota média 4,0 no prazo × 1,94 com atraso (dado da própria base). Gestores precisam de respostas com evidência, não de palpites. |
| 0:45–1:45 | **Arquitetura** | Diagrama do README: indexação offline (parquet → embeddings → ChromaDB + BM25) e fluxo online (QueryPlan → híbrida/temas → suficiência → contexto → LLM → validação de citações). |
| 1:45–2:45 | **Preparação da base** | 99 mil → 42 mil avaliações com texto; 1 avaliação = 1 documento (≤ 230 caracteres, sem chunking); negações preservadas; tratamento de ausentes; metadados de entrega/categoria/nota. |
| 2:45–4:45 | **Demo ao vivo (Streamlit)** | 1) "principais problemas" → modo amplo, filtro inferido, temas e evidências por tema. 2) "problemas de entrega" → modo focado, abrir o rastreamento: regras, RRF, contexto enviado ao LLM. 3) "elogios em beleza" → filtro de categoria + nota. 4) "faturamento 2018" e "capital da França" → recusa explicada. |
| 4:45–5:45 | **Como a recuperação funciona** | Densa (paráfrases) + BM25 (termos exatos) → RRF → cobertura IDF → MMR; por que top-k puro falha em perguntas amplas (exemplo "entrega sem problemas"). |
| 5:45–7:00 | **Desafios e decisões** | Frequência ≠ top-k (camada de temas); guardrail antes do LLM; regras × LLM na transformação da pergunta; limitações honestas (regex de temas, "não recebido" escrito antes da entrega, avaliação pequena com risco de sobreajuste). |

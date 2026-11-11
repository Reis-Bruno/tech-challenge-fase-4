# Estudo de ablação da recuperação

Embeddings: `lsa` · 18 perguntas de `eval/questions.json` (12 respondíveis, 6 a recusar) · gerado por `python eval/ablation.py`.

| Variante | Precisão (proxy) | Polaridade coerente | Redundância (↓) | Temas distintos | Recusas corretas (de 6) |
|---|---|---|---|---|---|
| A. Somente densa (top-k por cosseno) | 0.63 | 0.64 | 0.73 | 1.0 | 2 |
| B. Somente BM25 | 0.79 | 0.61 | 0.37 | 2.9 | 2 |
| C. Híbrida (RRF) | 0.75 | 0.66 | 0.52 | 1.7 | 2 |
| D. C + filtros de metadados inferidos | 0.74 | 1.00 | 0.49 | 1.8 | 2 |
| E. D + verificação de suporte e cobertura IDF | 0.75 | 1.00 | 0.53 | 1.9 | 6 |
| F. E + MMR | 0.81 | 1.00 | 0.40 | 2.6 | 6 |
| G. Pipeline completo (F + decomposição por tema) | 0.97 | 1.00 | 0.32 | 3.5 | 6 |

Definições das métricas no cabeçalho de `eval/ablation.py`. As variantes A–C não inferem filtros da pergunta; a recusa nessas variantes vem apenas da regra de escopo (dados transacionais), pois a verificação de suporte está desligada.

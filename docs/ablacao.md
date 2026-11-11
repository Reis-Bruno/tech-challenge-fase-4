# Estudo de ablação da recuperação

Embeddings: `fastembed` · 18 perguntas de `eval/questions.json` (12 respondíveis, 6 a recusar) · gerado por `python eval/ablation.py`.

| Variante | Precisão (proxy) | Polaridade coerente | Redundância (↓) | Temas distintos | Recusas corretas (de 6) |
|---|---|---|---|---|---|
| A. Somente densa (top-k por cosseno) | 0.71 | 0.82 | 0.67 | 3.1 | 2 |
| B. Somente BM25 | 0.79 | 0.62 | 0.47 | 3.0 | 2 |
| C. Híbrida (RRF) | 0.75 | 0.76 | 0.57 | 3.0 | 2 |
| D. C + filtros de metadados inferidos | 0.80 | 1.00 | 0.58 | 2.9 | 2 |
| E. D + verificação de suporte e cobertura IDF | 0.84 | 1.00 | 0.60 | 3.2 | 6 |
| F. E + MMR | 0.82 | 1.00 | 0.56 | 3.3 | 6 |
| G. Pipeline completo (F + decomposição por tema) | 0.93 | 1.00 | 0.56 | 4.4 | 6 |

Definições das métricas no cabeçalho de `eval/ablation.py`. As variantes A–C não inferem filtros da pergunta; a recusa nessas variantes vem apenas da regra de escopo (dados transacionais), pois a verificação de suporte está desligada.

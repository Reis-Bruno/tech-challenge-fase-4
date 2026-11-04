# Avaliação automática

Backend de embeddings: `lsa` · gerador(es): `guardrail, llm:gemini/gemini-3.5-flash, llm:gemini/gemini-3.5-flash-lite`

Gerado por `python eval/run_eval.py`.

## Resumo

| Métrica | Valor |
|---|---|
| guardrail_accuracy | 1.0 |
| mean_precision_at_k | 0.973 |
| filter_compliance | 1.0 |
| answers_with_invalid_citations | 0 |
| answers_without_citation | 0 |
| mean_latency_ms | 9413 |

## Por pergunta

| ID | Pergunta | Esperado | Respondeu | Modo | Filtros inferidos | Evid. | Precisão@k (proxy) | Filtros ok |
|---|---|---|---|---|---|---|---|---|
| Q01 | Quais são os principais problemas relatados pelos clientes em suas avaliações? | responder | sim | amplo | nota 1–3 | 8 | 1.00 | ✔ |
| Q02 | O que os clientes relatam sobre problemas relacionados à entrega? | responder | sim | focado | nota 1–3 | 10 | 1.00 | ✔ |
| Q03 | Quais aspectos da experiência de compra são mais elogiados pelos clientes? | responder | sim | amplo | nota 4–5 | 8 | 1.00 | ✔ |
| Q04 | Quais padrões podem ser identificados nas avaliações de clientes insatisfeitos? | responder | sim | amplo | nota 1–2 | 8 | 1.00 | ✔ |
| Q05 | Quais avaliações sustentam a conclusão de que existem problemas recorrentes relacionados ao prazo de entrega? | responder | sim | focado | nota 1–3 | 10 | 1.00 | ✔ |
| Q06 | Existem padrões recorrentes nas avaliações relacionadas à qualidade dos produtos? | responder | sim | focado | sem filtros | 10 | 1.00 | ✔ |
| Q07 | O que os clientes mais elogiam em produtos de beleza? | responder | sim | amplo | nota 4–5; categoria beleza_saude | 8 | 1.00 | ✔ |
| Q08 | Quais são os principais problemas relatados nas avaliações com nota baixa? | responder | sim | amplo | nota 1–2 | 8 | 1.00 | ✔ |
| Q09 | Quais temas aparecem nas avaliações de pedidos entregues com atraso? | responder | sim | focado | entrega atrasado | 10 | — | ✔ |
| Q10 | O que os clientes reclamam sobre o atendimento do vendedor? | responder | sim | focado | nota 1–3 | 10 | 1.00 | ✔ |
| Q11 | Os clientes reclamam de receber produtos diferentes do anunciado? | responder | sim | focado | nota 1–3 | 10 | 0.70 | ✔ |
| Q12 | O que os clientes dizem sobre a embalagem dos produtos? | responder | sim | focado | sem filtros | 10 | 1.00 | ✔ |
| Q13 | Qual foi o faturamento da Olist em 2018? | recusar | não | recusado | ano 2018 | 0 | — | ✔ |
| Q14 | Qual a capital da França? | recusar | não | recusado | sem filtros | 0 | — | ✔ |
| Q15 | Como fazer um bolo de chocolate? | recusar | não | recusado | sem filtros | 0 | — | ✔ |
| Q16 | Quem ganhou a copa do mundo de 2002? | recusar | não | recusado | sem filtros | 0 | — | ✔ |
| Q17 | Qual é a melhor linguagem de programação para machine learning? | recusar | não | recusado | sem filtros | 0 | — | ✔ |
| Q18 | Quantos pedidos foram cancelados no total? | recusar | não | recusado | sem filtros | 0 | — | ✔ |

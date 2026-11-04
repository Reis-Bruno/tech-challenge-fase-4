# Exemplos de perguntas e respostas

Gerados por `python eval/run_eval.py` (embeddings `lsa`, gerador `extrativo, guardrail`).

## Quais são os principais problemas relatados pelos clientes em suas avaliações?

*Modo:* `amplo` · *filtros:* nota 1–3 · *população:* 14438 avaliações

*Transformações da pergunta:* intenção negativa -> filtro nota <= 3; pergunta ampla (sem termo de conteúdo) -> decomposição em subconsultas pelos temas mais frequentes da população filtrada

```text
Resumo: nas 14438 avaliações analisadas (nota 1–3), os temas mais citados são: produto não recebido (até a data da avaliação) (26.6%), atraso / demora na entrega (13.1%), troca, devolução, cancelamento ou reembolso (12.1%).

Principais pontos, com as evidências:
- Produto não recebido (até a data da avaliação) [R1] [R2]
    • "PRODUTO NÃO RECEBIDO" [R1]
    • "Nao recebido produto. Sem o produto nao recebido" [R2]
- Atraso / demora na entrega [R3] [R4]
    • "Demora na entrega e ainda atrasou." [R3]
    • "Demorou muito pra entregar.." [R4]
- Troca, devolução, cancelamento ou reembolso [R5] [R6]
    • "solicito o cancelamento" [R5]
    • "Média. Preciso que vcs resolvam o meu problema de trocar o produto" [R6]
- Produto errado / diferente do anunciado [R7] [R8]
    • "Produto ERRADO. O conector USB que entregaram é diferente do que foi anunciado, que me interessou e por isso o comprei. O que enviaram NÃO serve em meu celular." [R7]
    • "Reclamação. Só tem um problema. Ela está marcando errado" [R8]

Limitações: resposta extrativa (sem LLM); percentuais vêm de contagem por palavras-chave e as evidências são uma amostra das avaliações mais relevantes.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 1 | 2017-08-19 | utilidades_domesticas | nao_entregue | PRODUTO NÃO RECEBIDO |
| R2 | 1 | 2018-05-18 | esporte_lazer | atrasado | Nao recebido produto. Sem o produto nao recebido |
| R3 | 3 | 2018-02-18 | esporte_lazer | atrasado | Demora na entrega e ainda atrasou. |
| R4 | 3 | 2018-03-10 | relogios_presentes | no_prazo | Demorou muito pra entregar.. |
| R5 | 1 | 2017-05-09 | eletronicos | no_prazo | solicito o cancelamento |
| R6 | 3 | 2018-05-24 | cama_mesa_banho | no_prazo | Média. Preciso que vcs resolvam o meu problema de trocar o produto |
| R7 | 1 | 2018-08-08 | telefonia | no_prazo | Produto ERRADO. O conector USB que entregaram é diferente do que foi anunciado, que me interessou e por isso o comprei. O que enviaram NÃO serve em meu celular. Requeiro a troca imediata. |
| R8 | 1 | 2018-06-23 | beleza_saude | no_prazo | Reclamação. Só tem um problema. Ela está marcando errado |

## O que os clientes relatam sobre problemas relacionados à entrega?

*Modo:* `focado` · *filtros:* nota 1–3 · *população:* 14438 avaliações

*Transformações da pergunta:* intenção negativa -> filtro nota <= 3; expansão BM25 com sinônimos de: entrega

```text
Resumo: nas 8069 avaliações analisadas (nota 1–3), os temas mais citados são: produto não recebido (até a data da avaliação) (40.0%), atraso / demora na entrega (22.5%), troca, devolução, cancelamento ou reembolso (10.7%).

Principais pontos, com as evidências:
- Outros relatos [R1] [R6] [R7] [R9]
    • "TERRIVEL ESTE PROBLEMA DA ENTREGA" [R1]
    • "Houve um pequeno problema na entrega, mas foi resolvido e logo em seguida chegou." [R6]
- Atraso / demora na entrega [R2] [R3] [R4] [R5] [R8]
    • "Demora na entrega e ainda atrasou." [R2]
    • "Entrega atrasada sera que é correios em greve?" [R3]
- Produto errado / diferente do anunciado [R10]
    • "Senhores, as parcerias não condizem com o oferecido pelas lannister em matéria de entrega, contudo pode ter havido um problema, mas poderiam ter me dito o que f" [R10]

Limitações: resposta extrativa (sem LLM); percentuais vêm de contagem por palavras-chave e as evidências são uma amostra das avaliações mais relevantes.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 1 | 2018-03-22 | informatica_acessorios | atrasado | TERRIVEL ESTE PROBLEMA DA ENTREGA |
| R2 | 3 | 2018-02-18 | esporte_lazer | atrasado | Demora na entrega e ainda atrasou. |
| R3 | 1 | 2018-02-27 | brinquedos | atrasado | Entrega atrasada sera que é correios em greve? |
| R4 | 3 | 2018-01-18 | eletronicos | atrasado | Entrega muito demorada e ainda houve atraso! |
| R5 | 1 | 2018-05-05 | bebes | nao_entregue | Entrega atrasada. Estou aguardando a entrega que já esta atrasada |
| R6 | 3 | 2018-03-08 | esporte_lazer | no_prazo | Houve um pequeno problema na entrega, mas foi resolvido e logo em seguida chegou. |
| R7 | 1 | 2018-07-23 | informatica_acessorios | no_prazo | problemas na entrega. infelizmente essa compra não foi bem sucedida |
| R8 | 3 | 2017-10-20 | telefonia | no_prazo | Chegou atrasado mais se desculparam e fizeram a entrega. |
| R9 | 3 | 2017-09-06 | telefonia | no_prazo | Entrega sem problemas. |
| R10 | 3 | 2018-01-31 | moveis_decoracao | no_prazo | Senhores, as parcerias não condizem com o oferecido pelas lannister em matéria de entrega, contudo pode ter havido um problema, mas poderiam ter me dito o que foi. |

## Quais aspectos da experiência de compra são mais elogiados pelos clientes?

*Modo:* `amplo` · *filtros:* nota 4–5 · *população:* 27676 avaliações

*Transformações da pergunta:* intenção positiva -> filtro nota >= 4; pergunta ampla (sem termo de conteúdo) -> decomposição em subconsultas pelos temas mais frequentes da população filtrada

```text
Resumo: nas 27676 avaliações analisadas (nota 4–5), os temas mais citados são: entrega rápida / antes do prazo (29.4%), recomenda a loja / compraria novamente (20.6%), boa qualidade do produto (18.8%).

Principais pontos, com as evidências:
- Entrega rápida / antes do prazo [R1] [R2]
    • "entrega rapida, antes do prazo" [R1]
    • "Entrega rápida. Antes do prazo." [R2]
- Recomenda a loja / compraria novamente [R3] [R4]
    • "Compraria novamente!!" [R3]
    • "Eu compraria novamente" [R4]
- Boa qualidade do produto [R5] [R6]
    • "O produto é realmente de boa qualidade e confere com o desenho publicado." [R5]
    • "Compra pen drive. Produto de boa qualidade, comprado e entregue em conformidade com as especificações" [R6]
- Preço / custo-benefício [R7] [R8]
    • "Ótimo custo-benefício" [R7]
    • "E bom custo/benefício !" [R8]

Limitações: resposta extrativa (sem LLM); percentuais vêm de contagem por palavras-chave e as evidências são uma amostra das avaliações mais relevantes.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 5 | 2017-08-16 | esporte_lazer | no_prazo | entrega rapida, antes do prazo |
| R2 | 5 | 2017-12-22 | eletronicos | no_prazo | Entrega rápida. Antes do prazo. |
| R3 | 5 | 2017-06-04 | utilidades_domesticas | no_prazo | Compraria novamente!! |
| R4 | 5 | 2018-01-16 | utilidades_domesticas | no_prazo | Eu compraria novamente |
| R5 | 5 | 2017-11-16 | cama_mesa_banho | no_prazo | O produto é realmente de boa qualidade e confere com o desenho publicado. |
| R6 | 4 | 2018-05-26 | informatica_acessorios | no_prazo | Compra pen drive. Produto de boa qualidade, comprado e entregue em conformidade com as especificações |
| R7 | 5 | 2017-09-02 | pcs | no_prazo | Ótimo custo-benefício |
| R8 | 4 | 2017-11-24 | cama_mesa_banho | no_prazo | E bom custo/benefício ! |

## Quais padrões podem ser identificados nas avaliações de clientes insatisfeitos?

*Modo:* `amplo` · *filtros:* nota 1–2 · *população:* 10841 avaliações

*Transformações da pergunta:* intenção negativa -> filtro nota <= 2; pergunta ampla (sem termo de conteúdo) -> decomposição em subconsultas pelos temas mais frequentes da população filtrada

```text
Resumo: nas 10841 avaliações analisadas (nota 1–2), os temas mais citados são: produto não recebido (até a data da avaliação) (31.9%), troca, devolução, cancelamento ou reembolso (14.1%), atraso / demora na entrega (14.0%).

Principais pontos, com as evidências:
- Produto não recebido (até a data da avaliação) [R1] [R2]
    • "Produto não recebido" [R1]
    • "PRODUTO NÃO RECEBIDO. O produto não foi recebido além de não ter recebido nenhuma notificação do vendedor sobre a não entrega." [R2]
- Troca, devolução, cancelamento ou reembolso [R3] [R4]
    • "solicito o cancelamento" [R3]
    • "1. Produto chegou danificado, solicitei a troca e foi negada, não teve outro jeito a não ser cancelar a compra." [R4]
- Atraso / demora na entrega [R5] [R6]
    • "Demorou de mais pra entrega" [R5]
    • "demora na entrega" [R6]
- Produto errado / diferente do anunciado [R7] [R8]
    • "Produto ERRADO. O conector USB que entregaram é diferente do que foi anunciado, que me interessou e por isso o comprei. O que enviaram NÃO serve em meu celular." [R7]
    • "Enviaram o produto errado." [R8]

Limitações: resposta extrativa (sem LLM); percentuais vêm de contagem por palavras-chave e as evidências são uma amostra das avaliações mais relevantes.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 1 | 2018-08-01 | beleza_saude | nao_entregue | Produto não recebido |
| R2 | 1 | 2018-08-07 | cine_foto | nao_entregue | PRODUTO NÃO RECEBIDO. O produto não foi recebido além de não ter recebido nenhuma notificação do vendedor sobre a não entrega. |
| R3 | 1 | 2017-05-09 | eletronicos | no_prazo | solicito o cancelamento |
| R4 | 1 | 2018-07-13 | eletrodomesticos_2 | no_prazo | 1. Produto chegou danificado, solicitei a troca e foi negada, não teve outro jeito a não ser cancelar a compra. |
| R5 | 2 | 2017-11-22 | utilidades_domesticas | atrasado | Demorou de mais pra entrega |
| R6 | 1 | 2018-05-20 | beleza_saude | atrasado | demora na entrega |
| R7 | 1 | 2018-08-08 | telefonia | no_prazo | Produto ERRADO. O conector USB que entregaram é diferente do que foi anunciado, que me interessou e por isso o comprei. O que enviaram NÃO serve em meu celular. Requeiro a troca imediata. |
| R8 | 1 | 2018-02-06 | esporte_lazer | no_prazo | Enviaram o produto errado. |

## Quais avaliações sustentam a conclusão de que existem problemas recorrentes relacionados ao prazo de entrega?

*Modo:* `focado` · *filtros:* nota 1–3 · *população:* 14438 avaliações

*Transformações da pergunta:* intenção negativa -> filtro nota <= 3; expansão BM25 com sinônimos de: entrega, prazo

```text
Resumo: nas 8131 avaliações analisadas (nota 1–3), os temas mais citados são: produto não recebido (até a data da avaliação) (39.9%), atraso / demora na entrega (22.3%), troca, devolução, cancelamento ou reembolso (10.7%).

Principais pontos, com as evidências:
- Outros relatos [R1] [R3] [R5] [R6] [R7] [R8] [R9]
    • "Prazo de entrega" [R1]
    • "Prazo de entrega muito extenso" [R3]
- Atraso / demora na entrega [R2] [R10]
    • "Produto com o prazo de entrega atrasado" [R2]
    • "Demora na entrega e ainda atrasou." [R10]
- Produto não recebido (até a data da avaliação) [R4]
    • "nao recebi o produto acredito ser problema dos correios prazo de entrega expirou" [R4]

Limitações: resposta extrativa (sem LLM); percentuais vêm de contagem por palavras-chave e as evidências são uma amostra das avaliações mais relevantes.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 1 | 2018-05-31 | cama_mesa_banho | no_prazo | Prazo de entrega |
| R2 | 3 | 2018-02-17 | bebes | atrasado | Produto com o prazo de entrega atrasado |
| R3 | 3 | 2017-08-04 | perfumaria | no_prazo | Prazo de entrega muito extenso |
| R4 | 1 | 2017-06-29 | market_place | atrasado | nao recebi o produto acredito ser problema dos correios prazo de entrega expirou |
| R5 | 1 | 2018-02-17 | relogios_presentes | atrasado | Ñ compriu seu prazo de entrega |
| R6 | 3 | 2017-04-27 | construcao_ferramentas_jardim | no_prazo | Prazo para entrega mui longo! |
| R7 | 2 | 2017-09-06 | perfumaria | atrasado | Produto venceu o prazo de entrega ontem. |
| R8 | 3 | 2017-11-24 | relogios_presentes | no_prazo | O prazo para entrega é muito longo. |
| R9 | 3 | 2017-05-13 | eletronicos | no_prazo | o prazo de entrega e muito longo. |
| R10 | 3 | 2018-02-18 | esporte_lazer | atrasado | Demora na entrega e ainda atrasou. |

## Existem padrões recorrentes nas avaliações relacionadas à qualidade dos produtos?

*Modo:* `focado` · *filtros:* sem filtros · *população:* 42114 avaliações

*Transformações da pergunta:* expansão BM25 com sinônimos de: qualidade

```text
Resumo: nas 4533 avaliações analisadas (sem filtros), os temas mais citados são: boa qualidade do produto (43.7%), entrega rápida / antes do prazo (25.3%), qualidade abaixo do esperado (25.0%).

Principais pontos, com as evidências:
- Qualidade abaixo do esperado [R1]
    • "Qualidade do produto.. A qualidade do produto deixa a desejar, muito frágil." [R1]
- Defeito / produto quebrado ou avariado [R2] [R3] [R7]
    • "Qualidade do produto. O produto apresenta a qualidade muito baixa e defeito de fabricação do mosquiteiro." [R2]
    • "A arara é de qualidade ruim, fragil o que fez com que o mesmo ja chegasse quebrada" [R3]
- Boa qualidade do produto [R4] [R5] [R6] [R8] [R10]
    • "O PRODUTO ESTÁ DENTRO DOS PADRÕES DE QUALIDADE,ATENDENDO MINHA EXPECTATIVA" [R4]
    • "Ótimo produto. Acabamento bom, desenho bonito, material de qualidade" [R5]
- Outros relatos [R9]
    • "Insatisfeito. No site o produto parece ter melhor qualidade de material e acabamento." [R9]

Limitações: resposta extrativa (sem LLM); percentuais vêm de contagem por palavras-chave e as evidências são uma amostra das avaliações mais relevantes.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 3 | 2018-08-19 | eletronicos | no_prazo | Qualidade do produto.. A qualidade do produto deixa a desejar, muito frágil. |
| R2 | 4 | 2018-05-02 | bebes | no_prazo | Qualidade do produto. O produto apresenta a qualidade muito baixa e defeito de fabricação do mosquiteiro. |
| R3 | 1 | 2017-05-12 | moveis_decoracao | no_prazo | A arara é de qualidade ruim, fragil o que fez com que o mesmo ja chegasse quebrada |
| R4 | 5 | 2017-03-10 | cama_mesa_banho | no_prazo | O PRODUTO ESTÁ DENTRO DOS PADRÕES DE QUALIDADE,ATENDENDO MINHA EXPECTATIVA |
| R5 | 5 | 2018-08-18 | automotivo | no_prazo | Ótimo produto. Acabamento bom, desenho bonito, material de qualidade |
| R6 | 5 | 2017-10-25 | informatica_acessorios | no_prazo | Produto original e de qualidade. |
| R7 | 1 | 2017-11-24 | relogios_presentes | no_prazo | Produto de péssima qualidade, ja chegou com o cronômetro quebrado e os botões com defeito |
| R8 | 5 | 2018-07-20 | pet_shop | no_prazo | Material de qualidade. |
| R9 | 3 | 2018-07-03 | beleza_saude | no_prazo | Insatisfeito. No site o produto parece ter melhor qualidade de material e acabamento. |
| R10 | 4 | 2018-03-04 | moveis_decoracao | no_prazo | Recebi conforme descrito na internet. Boa qualidade do material e acabamento. |

## O que os clientes mais elogiam em produtos de beleza?

*Modo:* `amplo` · *filtros:* nota 4–5; categoria beleza_saude · *população:* 2416 avaliações

*Transformações da pergunta:* intenção positiva -> filtro nota >= 4; categoria citada -> filtro ['beleza_saude']; pergunta ampla (sem termo de conteúdo) -> decomposição em subconsultas pelos temas mais frequentes da população filtrada

```text
Resumo: nas 2416 avaliações analisadas (nota 4–5; categoria beleza_saude), os temas mais citados são: entrega rápida / antes do prazo (32.2%), recomenda a loja / compraria novamente (21.9%), boa qualidade do produto (17.1%).

Principais pontos, com as evidências:
- Entrega rápida / antes do prazo [R1] [R2]
    • "Entrega muito rápido, bem antes do prazo previsto." [R1]
    • "Os produtos chegaram conforme o prometido de qualidade e entrega rápida antes do prazo final." [R2]
- Recomenda a loja / compraria novamente [R3] [R4]
    • "Compraria novamente nesta loja, pois a mesma entrega no prazo." [R3]
    • "Tudo dentro do combinado. Empresa de confiança. Compraria novamente com certeza!" [R4]
- Boa qualidade do produto [R5] [R6]
    • "Produto de Boa Qualidade." [R5]
    • "Produto de boa qualidade, simples de usar, confortável e ergonômico." [R6]
- Embalagem bem feita / bem protegido [R7] [R8]
    • "Entrega no prazo, embalagem perfeita. Só elogios." [R7]
    • "Produto chegou em uma semana, embalagem bem protegida e tudo de ótima qualidade." [R8]

Limitações: resposta extrativa (sem LLM); percentuais vêm de contagem por palavras-chave e as evidências são uma amostra das avaliações mais relevantes.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 5 | 2017-05-29 | beleza_saude | no_prazo | Entrega muito rápido, bem antes do prazo previsto. |
| R2 | 5 | 2018-08-22 | beleza_saude | no_prazo | Os produtos chegaram conforme o prometido de qualidade e entrega rápida antes do prazo final. |
| R3 | 5 | 2017-12-14 | beleza_saude | no_prazo | Compraria novamente nesta loja, pois a mesma entrega no prazo. |
| R4 | 5 | 2017-12-10 | beleza_saude | no_prazo | Tudo dentro do combinado. Empresa de confiança. Compraria novamente com certeza! |
| R5 | 5 | 2018-03-19 | beleza_saude | no_prazo | Produto de Boa Qualidade. |
| R6 | 4 | 2017-09-10 | beleza_saude | no_prazo | Produto de boa qualidade, simples de usar, confortável e ergonômico. |
| R7 | 5 | 2017-03-23 | beleza_saude | no_prazo | Entrega no prazo, embalagem perfeita. Só elogios. |
| R8 | 5 | 2017-05-29 | beleza_saude | no_prazo | Produto chegou em uma semana, embalagem bem protegida e tudo de ótima qualidade. |

## Quais são os principais problemas relatados nas avaliações com nota baixa?

*Modo:* `amplo` · *filtros:* nota 1–2 · *população:* 10841 avaliações

*Transformações da pergunta:* intenção negativa -> filtro nota <= 2; pergunta ampla (sem termo de conteúdo) -> decomposição em subconsultas pelos temas mais frequentes da população filtrada

```text
Resumo: nas 10841 avaliações analisadas (nota 1–2), os temas mais citados são: produto não recebido (até a data da avaliação) (31.9%), troca, devolução, cancelamento ou reembolso (14.1%), atraso / demora na entrega (14.0%).

Principais pontos, com as evidências:
- Produto não recebido (até a data da avaliação) [R1] [R2]
    • "Produto não recebido" [R1]
    • "Nao recebido produto. Sem o produto nao recebido" [R2]
- Troca, devolução, cancelamento ou reembolso [R3] [R4]
    • "Incompetência. Solicitei o cancelamento da compra após comprar, a nota fainda não tinha sido emitida e me retornaram no dia seguinte dizendo que não seria possí" [R3]
    • "ENTRAGOU NO PRIMEIRO DIA. ABRI PROTOCOLO PARA DEVOLUÇÃO, PRODUTO DE BAIXA QUALIDADE DEU PROBLEMA NO PRIMEIRO DIA DE USO. lannister VIROU UM MERCADO LIVRE..6 PED" [R4]
- Atraso / demora na entrega [R5] [R6]
    • "Demorou de mais pra entrega" [R5]
    • "demora com a entrega" [R6]
- Produto errado / diferente do anunciado [R7] [R8]
    • "Produto ERRADO. O conector USB que entregaram é diferente do que foi anunciado, que me interessou e por isso o comprei. O que enviaram NÃO serve em meu celular." [R7]
    • "Reclamação. Só tem um problema. Ela está marcando errado" [R8]

Limitações: resposta extrativa (sem LLM); percentuais vêm de contagem por palavras-chave e as evidências são uma amostra das avaliações mais relevantes.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 1 | 2018-08-01 | beleza_saude | nao_entregue | Produto não recebido |
| R2 | 1 | 2018-05-18 | esporte_lazer | atrasado | Nao recebido produto. Sem o produto nao recebido |
| R3 | 1 | 2018-06-24 | cama_mesa_banho | no_prazo | Incompetência. Solicitei o cancelamento da compra após comprar, a nota fainda não tinha sido emitida e me retornaram no dia seguinte dizendo que não seria possível cancelar pois o produto já tinha sido despachado |
| R4 | 1 | 2018-05-27 | papelaria | no_prazo | ENTRAGOU NO PRIMEIRO DIA. ABRI PROTOCOLO PARA DEVOLUÇÃO, PRODUTO DE BAIXA QUALIDADE DEU PROBLEMA NO PRIMEIRO DIA DE USO. lannister VIROU UM MERCADO LIVRE..6 PEDIDOS 6 PROBLEMAS |
| R5 | 2 | 2017-11-22 | utilidades_domesticas | atrasado | Demorou de mais pra entrega |
| R6 | 2 | 2018-01-23 | perfumaria | atrasado | demora com a entrega |
| R7 | 1 | 2018-08-08 | telefonia | no_prazo | Produto ERRADO. O conector USB que entregaram é diferente do que foi anunciado, que me interessou e por isso o comprei. O que enviaram NÃO serve em meu celular. Requeiro a troca imediata. |
| R8 | 1 | 2018-06-23 | beleza_saude | no_prazo | Reclamação. Só tem um problema. Ela está marcando errado |

## Quais temas aparecem nas avaliações de pedidos entregues com atraso?

*Modo:* `focado` · *filtros:* entrega atrasado · *população:* 3809 avaliações

*Transformações da pergunta:* 'entregas atrasadas' -> filtro delivery_status = atrasado; expansão BM25 com sinônimos de: atras

```text
Resumo: nas 2952 avaliações analisadas (entrega atrasado), os temas mais citados são: produto não recebido (até a data da avaliação) (58.7%), atraso / demora na entrega (32.9%), recomenda a loja / compraria novamente (6.4%).

Principais pontos, com as evidências:
- Atraso / demora na entrega [R1] [R2] [R3] [R4] [R5] [R6] [R7] [R8] [R9] [R10]
    • "não do 5 estrela pois atrasou pedido" [R1]
    • "Está em atraso!" [R2]

Limitações: resposta extrativa (sem LLM); percentuais vêm de contagem por palavras-chave e as evidências são uma amostra das avaliações mais relevantes.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 3 | 2018-02-25 | informatica_acessorios | atrasado | não do 5 estrela pois atrasou pedido |
| R2 | 1 | 2018-03-24 | esporte_lazer | atrasado | Está em atraso! |
| R3 | 1 | 2018-02-27 | bebes | atrasado | atrasou a entega |
| R4 | 1 | 2018-03-13 | cama_mesa_banho | atrasado | É a primeira vez que há atraso nos meus pedidos. |
| R5 | 3 | 2018-04-01 | esporte_lazer | atrasado | ATRASO EXCESSIVO |
| R6 | 4 | 2018-03-25 | ferramentas_jardim | atrasado | Produto está atrasado |
| R7 | 5 | 2018-03-02 | esporte_lazer | atrasado | Só o whey chegou atrasado mas o motivo do atraso foi dos correios |
| R8 | 4 | 2018-04-02 | beleza_saude | atrasado | Atraso na entrega |
| R9 | 1 | 2018-03-15 | brinquedos | atrasado | Um absurdo esse atraso |
| R10 | 1 | 2018-03-01 | informatica_acessorios | atrasado | O produto está atrasado |

## O que os clientes reclamam sobre o atendimento do vendedor?

*Modo:* `focado` · *filtros:* nota 1–3 · *população:* 14438 avaliações

*Transformações da pergunta:* intenção negativa -> filtro nota <= 3; expansão BM25 com sinônimos de: atendimento

```text
Resumo: nas 2318 avaliações analisadas (nota 1–3), os temas mais citados são: produto não recebido (até a data da avaliação) (30.0%), troca, devolução, cancelamento ou reembolso (20.4%), atraso / demora na entrega (13.4%).

Principais pontos, com as evidências:
- Outros relatos [R1] [R4] [R6] [R9]
    • "Preciso de números telefones de contato com o atendimento baratheon ou do vendedor. URGENTE" [R1]
    • "Vendedores muito atenciosos." [R4]
- Entrega rápida / antes do prazo [R2]
    • "amei a forma de entega foi muito rápido e prático to satisfeita agradeço este site e ao vendedor pela agilidade de atendimento e entrega do meu produto.." [R2]
- Produto não recebido (até a data da avaliação) [R3]
    • "Pessimo atendimento. O objeto comprado nao foi entregue a venda cancelada e em nenhum momento o vendedor entrou em contato comigo para me informar" [R3]
- Troca, devolução, cancelamento ou reembolso [R5]
    • "Eu recebi o produto sem o Pistão da cadeira, abri uma solicitação de devolução e foi cancelada pelo vendedor loja, sem nenhum motivo e vou ficar no prejuízo poi" [R5]
- Atraso / demora na entrega [R7] [R10]
    • "Prazo de entrega absurdo e demora no retorno do vendedor" [R7]
    • "demora no atendimento." [R10]
- Recomenda a loja / compraria novamente [R8]
    • "Recomendo otimo vendedor" [R8]

Limitações: resposta extrativa (sem LLM); percentuais vêm de contagem por palavras-chave e as evidências são uma amostra das avaliações mais relevantes.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 1 | 2017-05-09 | informatica_acessorios | nao_entregue | Preciso de números telefones de contato com o atendimento baratheon ou do vendedor. URGENTE |
| R2 | 1 | 2017-09-18 | beleza_saude | no_prazo | amei a forma de entega foi muito rápido e prático to satisfeita agradeço este site e ao vendedor pela agilidade de atendimento e entrega do meu produto.. |
| R3 | 1 | 2018-05-01 | brinquedos | nao_entregue | Pessimo atendimento. O objeto comprado nao foi entregue a venda cancelada e em nenhum momento o vendedor entrou em contato comigo para me informar |
| R4 | 3 | 2017-05-08 | beleza_saude | no_prazo | Vendedores muito atenciosos. |
| R5 | 1 | 2018-03-16 | moveis_escritorio | no_prazo | Eu recebi o produto sem o Pistão da cadeira, abri uma solicitação de devolução e foi cancelada pelo vendedor loja, sem nenhum motivo e vou ficar no prejuízo pois não fui atendido. |
| R6 | 1 | 2018-04-12 | perfumaria | atrasado | Entrega e Atendimento. Péssimo atendimento! |
| R7 | 3 | 2018-05-25 | brinquedos | no_prazo | Prazo de entrega absurdo e demora no retorno do vendedor |
| R8 | 3 | 2017-04-18 | livros_interesse_geral | no_prazo | Recomendo otimo vendedor |
| R9 | 3 | 2017-04-03 | cama_mesa_banho | no_prazo | Bom atendimento 5 |
| R10 | 1 | 2018-02-05 | eletronicos | atrasado | demora no atendimento. |

## Os clientes reclamam de receber produtos diferentes do anunciado?

*Modo:* `focado` · *filtros:* nota 1–3 · *população:* 14438 avaliações

*Transformações da pergunta:* intenção negativa -> filtro nota <= 3

```text
Resumo: nas 987 avaliações analisadas (nota 1–3), os temas mais citados são: produto não recebido (até a data da avaliação) (22.4%), produto errado / diferente do anunciado (19.5%), troca, devolução, cancelamento ou reembolso (16.9%).

Principais pontos, com as evidências:
- Produto errado / diferente do anunciado [R1] [R3] [R4] [R6] [R7] [R9]
    • "O produto recebido não e o mesmo das fotos do anuncio." [R1]
    • "Péssimo. O produto recebido é diferente e inferior ao adquirido.Não confere com as especificações anunciadas." [R3]
- Preço / custo-benefício [R2]
    • "paguei mais caro para receber o produto na cor do anuncio que é vermelho e recebi roxo" [R2]
- Outros relatos [R5] [R10]
    • "Produto recebido." [R5]
    • "Preciso receber meu produto. O que esta acontecendo? Quando irei receber?" [R10]
- Defeito / produto quebrado ou avariado [R8]
    • "PRODUTO FOI ENTREGUE COM DEFEITO, FIZEMOS RECLAMAÇÃO 5 MINUTOS APOS RECEBERMOS, RECLAMAMOS NO lannister.COM E NO PARECEIRO - WORD TONEER DA lannister. 72 HORAS " [R8]

Limitações: resposta extrativa (sem LLM); percentuais vêm de contagem por palavras-chave e as evidências são uma amostra das avaliações mais relevantes.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 1 | 2017-06-27 | automotivo | no_prazo | O produto recebido não e o mesmo das fotos do anuncio. |
| R2 | 1 | 2018-04-18 | utilidades_domesticas | no_prazo | paguei mais caro para receber o produto na cor do anuncio que é vermelho e recebi roxo |
| R3 | 1 | 2018-08-09 | esporte_lazer | no_prazo | Péssimo. O produto recebido é diferente e inferior ao adquirido.Não confere com as especificações anunciadas. |
| R4 | 1 | 2017-09-16 | fashion_roupa_masculina | no_prazo | o produto recebido não e o mesmo que estava no anuncio, nao sei o que aconteceu, mais o produto recebido e de baixa qualidade. |
| R5 | 3 | 2017-12-02 | cama_mesa_banho | no_prazo | Produto recebido. |
| R6 | 1 | 2018-05-15 | informatica_acessorios | no_prazo | Solicitei a devolução. Recebi um produto diferente do que foi requisitado. A imagem do anúncio não condiz com o produto recebido. |
| R7 | 1 | 2017-06-11 | cama_mesa_banho | no_prazo | PRODUTO COM AS ESPECIFICAÇÕES DIFERENTES DO ANUNCIADO. 80% ALGODÃO AO INVÉS DE 100% COMO DIZIA NO ANUNCIO |
| R8 | 1 | 2018-01-26 | informatica_acessorios | no_prazo | PRODUTO FOI ENTREGUE COM DEFEITO, FIZEMOS RECLAMAÇÃO 5 MINUTOS APOS RECEBERMOS, RECLAMAMOS NO lannister.COM E NO PARECEIRO - WORD TONEER DA lannister. 72 HORAS APOS, NENHUMA SOLUÇÃO |
| R9 | 3 | 2018-06-23 | eletrodomesticos | no_prazo | DIFERENTE DO ANUNCIADO. NO ANUNCIO DIZIA SER AMBOS OS LADOS IGUAIS POREM O MATERIAL TEM LADOS DIFERENTES, OU SEJA, UM LADO MAIOR E O OUTRO LADO MENOR. |
| R10 | 1 | 2018-03-19 | consoles_games | atrasado | Preciso receber meu produto. O que esta acontecendo? Quando irei receber? |

## O que os clientes dizem sobre a embalagem dos produtos?

*Modo:* `focado` · *filtros:* sem filtros · *população:* 42114 avaliações

*Transformações da pergunta:* expansão BM25 com sinônimos de: embalagem

```text
Resumo: nas 1882 avaliações analisadas (sem filtros), os temas mais citados são: embalagem bem feita / bem protegido (40.6%), entrega rápida / antes do prazo (34.5%), recomenda a loja / compraria novamente (17.2%).

Principais pontos, com as evidências:
- Defeito / produto quebrado ou avariado [R1] [R2] [R5] [R7] [R9] [R10]
    • "Embalagem amassada." [R1]
    • "Embalagem chegou amassada." [R2]
- Outros relatos [R3] [R4] [R6] [R8]
    • "Avaria na embalagem, restante 100%.." [R3]
    • "Embalagem e caixa do produto toda detereriorada" [R4]

Limitações: resposta extrativa (sem LLM); percentuais vêm de contagem por palavras-chave e as evidências são uma amostra das avaliações mais relevantes.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 4 | 2017-11-17 | papelaria | no_prazo | Embalagem amassada. |
| R2 | 3 | 2017-12-02 | informatica_acessorios | no_prazo | Embalagem chegou amassada. |
| R3 | 4 | 2018-03-10 | perfumaria | atrasado | Avaria na embalagem, restante 100%.. |
| R4 | 3 | 2017-12-05 | esporte_lazer | no_prazo | Embalagem e caixa do produto toda detereriorada |
| R5 | 1 | 2018-03-29 | cool_stuff | no_prazo | Produto com embalagem inadequada, parte central do espremedor chegou amassado. |
| R6 | 5 | 2018-05-04 | perfumaria | no_prazo | 4. produto sem embalagem |
| R7 | 3 | 2017-12-11 | brinquedos | no_prazo | Apesar da embalagem estar muito amassada, o produto não estava avariado e chegou no prazo. |
| R8 | 5 | 2018-07-17 | beleza_saude | no_prazo | OTIMA EMBALAGEM |
| R9 | 2 | 2018-03-25 | esporte_lazer | no_prazo | Recebi o whey de morango com a embalagem toda amassada . Como devo proceder ? |
| R10 | 3 | 2017-12-17 | moveis_decoracao | no_prazo | A embalagem deixou a desejar, por pouco o produto não foi danificado, a caixa estava toda amassada. |

## Qual foi o faturamento da Olist em 2018?

*Modo:* `recusado` · *filtros:* ano 2018 · *população:* 23265 avaliações

*Transformações da pergunta:* ano(s) citados -> filtro [2018]

```text
Não há evidências suficientes na base de avaliações para responder. Motivo: A pergunta exige dados transacionais/financeiros agregados, que não estão nos textos das avaliações (base de conhecimento desta solução). Reformule a pergunta com um tema presente em avaliações de clientes (entrega, qualidade, atendimento, produto, embalagem, troca etc.) ou ajuste os filtros.
```

## Qual a capital da França?

*Modo:* `recusado` · *filtros:* sem filtros · *população:* 42114 avaliações

*Transformações da pergunta:* sem termos do domínio -> exigirá evidência forte

```text
Não há evidências suficientes na base de avaliações para responder. Motivo: Apenas 0 avaliação(ões) da base têm relação verificável com a pergunta (mínimo exigido: 3). Nenhum termo do domínio de e-commerce/avaliações foi identificado na pergunta. Reformule a pergunta com um tema presente em avaliações de clientes (entrega, qualidade, atendimento, produto, embalagem, troca etc.) ou ajuste os filtros.
```

## Como fazer um bolo de chocolate?

*Modo:* `recusado` · *filtros:* sem filtros · *população:* 42114 avaliações

*Transformações da pergunta:* sem termos do domínio -> exigirá evidência forte

```text
Não há evidências suficientes na base de avaliações para responder. Motivo: Apenas 0 avaliação(ões) da base têm relação verificável com a pergunta (mínimo exigido: 3). Nenhum termo do domínio de e-commerce/avaliações foi identificado na pergunta. Reformule a pergunta com um tema presente em avaliações de clientes (entrega, qualidade, atendimento, produto, embalagem, troca etc.) ou ajuste os filtros.
```

## Quem ganhou a copa do mundo de 2002?

*Modo:* `recusado` · *filtros:* sem filtros · *população:* 42114 avaliações

*Transformações da pergunta:* sem termos do domínio -> exigirá evidência forte

```text
Não há evidências suficientes na base de avaliações para responder. Motivo: Apenas 0 avaliação(ões) da base têm relação verificável com a pergunta (mínimo exigido: 3). Nenhum termo do domínio de e-commerce/avaliações foi identificado na pergunta. Reformule a pergunta com um tema presente em avaliações de clientes (entrega, qualidade, atendimento, produto, embalagem, troca etc.) ou ajuste os filtros.
```

## Qual é a melhor linguagem de programação para machine learning?

*Modo:* `recusado` · *filtros:* sem filtros · *população:* 42114 avaliações

*Transformações da pergunta:* sem termos do domínio -> exigirá evidência forte

```text
Não há evidências suficientes na base de avaliações para responder. Motivo: Apenas 0 avaliação(ões) da base têm relação verificável com a pergunta (mínimo exigido: 3). Nenhum termo do domínio de e-commerce/avaliações foi identificado na pergunta. Reformule a pergunta com um tema presente em avaliações de clientes (entrega, qualidade, atendimento, produto, embalagem, troca etc.) ou ajuste os filtros.
```

## Quantos pedidos foram cancelados no total?

*Modo:* `recusado` · *filtros:* sem filtros · *população:* 42114 avaliações

```text
Não há evidências suficientes na base de avaliações para responder. Motivo: A pergunta exige dados transacionais/financeiros agregados, que não estão nos textos das avaliações (base de conhecimento desta solução). Reformule a pergunta com um tema presente em avaliações de clientes (entrega, qualidade, atendimento, produto, embalagem, troca etc.) ou ajuste os filtros.
```


# Exemplos de perguntas e respostas

Gerados por `python eval/run_eval.py` (embeddings `lsa`, gerador `guardrail, llm:gemini/gemini-3.5-flash`).

## Quais são os principais problemas relatados pelos clientes em suas avaliações?

*Modo:* `amplo` · *filtros:* nota 1–3 · *população:* 14438 avaliações

*Transformações da pergunta:* intenção negativa -> filtro nota <= 3; pergunta ampla (sem termo de conteúdo) -> decomposição em subconsultas pelos temas mais frequentes da população filtrada

```text
Os principais problemas relatados concentram-se em falhas de entrega (produtos não recebidos ou com atraso), seguidos por demandas de troca, devolução ou cancelamento, e pelo recebimento de itens errados ou divergentes do anunciado.

**Principais problemas identificados:**

* **Produto não recebido e atraso na entrega:** Representa a maior parte das queixas por palavras-chave na base filtrada (26,6% para não recebido e 13,1% para atraso/demora). Os clientes relatam expressamente a ausência da entrega do item [R1], [R2] ou insatisfação com a demora e extrapolação do prazo [R3], [R4].
* **Solicitações de troca, devolução, cancelamento ou reembolso:** Presente em 12,1% dos casos da base filtrada, reunindo pedidos de cancelamento imediato do pedido [R5] e cobranças para resolução do processo de troca [R6].
* **Produto errado ou diferente do anunciado:** Representa 8,1% das ocorrências na base filtrada. Os relatos incluem o envio de itens incompatíveis com o modelo do cliente (diferente da especificação comprada) [R7] ou produtos que apresentam medições/funcionamento incorretos [R8].

Limitações: Análise baseada em uma amostra reduzida de depoimentos e estatísticas de palavras-chave restritas a avaliações de nota 1 a 3.
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
Os clientes relatam insatisfação focada principalmente em atrasos, demora excessiva na entrega e não recebimento de produtos. Nas estatísticas de temas da base filtrada, "Produto não recebido" (40,0%) e "Atraso / demora na entrega" (22,5%) são os problemas mais frequentes.

Principais pontos relatados:

- **Atrasos e demora excessiva:** Clientes registram frequentemente que a entrega demorou ou atrasou em relação ao esperado [R1] [R2] [R3] [R4] [R5] [R8]. Na contagem por palavras-chave, "Atraso / demora na entrega" totaliza 1.812 avaliações (22,5% das menções de temas).
- **Produto não recebido / Espera pelo pedido:** Há relatos de clientes que aguardavam a chegada do item que já se encontrava atrasado [R5]. Esse tema ("Produto não recebido") representa a maior volume nas estatísticas, com 3.227 ocorrências (40,0% das menções de temas).
- **Falta de transparência e contratempos de transporte:** Consumidores mencionam falhas gerais no processo de entrega [R1] [R7], ausência de explicações por parte do e-commerce/parceiros sobre a causa do problema [R10] e indagam sobre possíveis causas externas, como greve dos Correios [R3]. Em outros casos, é ressaltado que houve problemas, mas a entrega foi concluída após retratação ou resolução [R6] [R8].

Limitações: Análise baseada em uma amostra reduzida de 10 avaliações e estatísticas por palavras-chave restritas à população de notas 1 a 3.
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
Os aspectos mais elogiados pelos clientes de notas 4 e 5 concentram-se na rapidez da entrega, na intenção de voltar a comprar na loja, na qualidade do produto e no bom custo-benefício.

Principais pontos destacados:

* **Entrega rápida e antecipada:** É o ponto mais expressivo na base filtrada por palavras-chave, presente em 29,4% das avaliações (8.133 menções), em que os clientes ressaltam que o pedido chegou rapidamente ou antes do prazo previsto [R1], [R2].
* **Recomendação e intenção de recompra:** Representa 20,6% das avaliações (5.706 menções), com os consumidores afirmando expressamente que voltariam a comprar no estabelecimento [R3], [R4].
* **Qualidade do produto e conformidade:** Fator presente em 18,8% das avaliações (5.208 menções), onde os compradores destacam a boa qualidade dos itens e a correspondência exata com as especificações e fotos anunciadas [R5], [R6].
* **Preço e custo-benefício:** Citado em 2,9% da população filtrada (814 menções), sendo apontado como um ótimo custo-benefício pelos clientes [R7], [R8].

Limitações: Análise restrita a avaliações positivas (notas 4–5) e a estatísticas derivadas de contagens por palavras-chave na base disponibilizada.
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
Nas avaliações de clientes insatisfeitos (notas 1 e 2), identificam-se padrões centrados em falhas de entrega, envio de itens incorretos ou avariados e dificuldades na solicitação de trocas e cancelamentos. Com base nas estatísticas por palavras-chave, a não entrega do produto é o motivo mais frequente (31,9%), acompanhada por demandas de troca/cancelamento (14,1%) e atrasos na entrega (14,0%).

Principais padrões identificados:

- **Não recebimento do produto:** Clientes relatam a ausência de entrega do item comprado, por vezes acompanhada da falta de notificação ou aviso por parte do vendedor [R1], [R2].
- **Atrasos na entrega:** Registram-se reclamações sobre a demora excessiva para a chegada das mercadorias [R5], [R6].
- **Envio de produtos errados ou divergentes:** Consumidores relatam ter recebido itens diferentes dos anunciados que não atendem às suas necessidades, demandando trocas [R7], [R8].
- **Dificuldades em trocas e cancelamentos:** Ocorrem solicitações de cancelamento da compra, incluindo cenários em que o produto chegou danificado e a solicitação de troca foi negada [R3], [R4].

Limitações: Análise baseada em estatísticas de palavras-chave e em uma amostra de 8 avaliações individuais de pedidos com notas 1 e 2.
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
As avaliações evidenciam insatisfação recorrente em relação ao prazo de entrega, dividindo-se entre o descumprimento/atraso da data prevista e a percepção de que os prazos informados são excessivamente longos. Essa recorrência é respaldada pelas estatísticas do tema, onde "Atraso / demora na entrega" equivale a 22,3% (1.812 avaliações) das menções na base filtrada.

Principais pontos identificados:
- **Descumprimento e atraso do prazo:** Clientes citam expressamente que o prazo de entrega venceu, expirou ou não foi cumprido, gerando atrasos na entrega do produto [R2], [R4], [R5], [R7], [R10].
- **Prazos estimados excessivamente longos:** Mesmo em pedidos entregues dentro do limite estipulado, os clientes reclamam que a estimativa de tempo informada para a entrega é muito longa ou extensa [R3], [R6], [R8], [R9].
- **Citação genérica ao tema:** O prazo de entrega é apontado de forma direta como o motivo da insatisfação [R1].

Limitações: Análise fundamentada em uma amostra de 10 avaliações e estatísticas de palavras-chave restritas a pedidos com notas entre 1 e 3.
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
Sim, existem padrões claros e recorrentes nas avaliações sobre a qualidade dos produtos, divididos entre avaliações positivas de conformidade e reclamações sobre fragilidade e defeitos. Nas estatísticas do tema, "Boa qualidade do produto" é o ponto mais citado (43,7% das menções / 1.983 avaliações), mas a qualidade abaixo do esperado (25,0% / 1.133 avaliações) e defeitos (15,5% / 701 avaliações) também formam um padrão expressivo de insatisfação.

**Principais padrões identificados:**

* **Aprovação do material, acabamento e expectativas atendidas:** Diversos clientes elogiam a qualidade do material, o acabamento e o fato de o item ser original ou corresponder ao anunciado no site [R4] [R5] [R6] [R8] [R10]. Esse padrão é suportado por 1.983 avaliações (43,7%) registrando boa qualidade nas estatísticas de temas.
* **Fragilidade do produto e divergência com o site:** Há registros recorrentes de consumidores que consideram o produto frágil, de baixa qualidade ou com material/acabamento inferior ao que aparentava na foto do site [R1] [R3] [R9]. As estatísticas mostram 1.133 avaliações (25,0%) sinalizando qualidade abaixo do esperado.
* **Produtos recebidos com defeito ou já quebrados:** A fragilidade e a baixa qualidade do produto estão frequentemente associadas ao recebimento do item danificado ou com defeitos de fabricação logo na entrega [R2] [R3] [R7]. Esse problema aparece em 701 avaliações (15,5%) nas estatísticas do tema.

Limitações: Análise restrita a uma amostra de 10 avaliações textuais e aos dados de contagem por palavras-chave fornecidos no contexto.
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
Os clientes da categoria de beleza e saúde elogiam principalmente a rapidez na entrega, a boa qualidade dos produtos e a confiança na loja, que gera intenção de recompra. De acordo com as estatísticas por palavras-chave na base filtrada, a velocidade de entrega é o aspecto mais mencionado, presente em 32,2% das avaliações positivas.

Os principais pontos elogiados são:

* **Entrega rápida e dentro do prazo:** É o tema mais frequente na base filtrada (32,2% / 777 avaliações), com clientes destacando que os produtos chegam bem antes do prazo prometido ou em poucos dias [R1], [R2], [R7], [R8].
* **Confiança e intenção de recompra:** Segundo maior tema identificado (21,9% / 528 avaliações), onde os consumidores relatam que o processo ocorreu dentro do combinado e declaram que voltariam a comprar no estabelecimento [R3], [R4].
* **Boa qualidade dos produtos:** Ocupa o terceiro lugar em frequência (17,1% / 413 avaliações), recebendo elogios pela qualidade geral e por atributos como ergonomia, conforto e simplicidade de uso [R2], [R5], [R6], [R8].
* **Embalagem bem protegida:** Representa 2,4% (58 avaliações) dos temas citados, com os clientes elogiando o estado perfeito do pacote e a proteção dos itens no envio [R7], [R8].

Limitações: Análise baseada em uma amostra de 8 avaliações textuais e estatísticas extraídas por palavras-chave de pedidos com nota 4–5 na categoria beleza_saude.
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
Os principais problemas relatados nas avaliações com nota baixa (1 e 2) concentram-se na não entrega do pedido, atrasos na distribuição, entraves em cancelamentos/devoluções e envio de produtos errados ou com defeito.

- **Não recebimento do produto**: Representa a maior frequência nas estatísticas de temas baseadas em palavras-chave (31,9% / 3.454 casos), com relatos diretos de clientes que não receberam a compra [R1], [R2].
- **Troca, devolução, cancelamento ou reembolso**: Corresponde a 14,1% das avaliações filtradas (1.531 casos), abrangendo queixas sobre negativa de cancelamento sob alegação de despacho prévio [R3] e necessidade de solicitar devolução por defeito/baixa qualidade no primeiro dia de uso [R4].
- **Atraso e demora na entrega**: Presente em 14,0% dos relatos (1.518 casos), com insatisfações explícitas relacionadas ao excesso de tempo para a realização da entrega [R5], [R6].
- **Produto errado ou diferente do anunciado**: Aparelha 9,0% das menções (972 casos), citando o recebimento de conectores/peças incompatíveis com o anunciado [R7] ou itens marcando/medindo de forma errada [R8].

Limitações: As conclusões combinam a análise de uma amostra restrita de 8 depoimentos com estatísticas baseadas em identificação por palavras-chave na população de avaliações de nota 1–2.
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
Nas avaliações de pedidos filtrados por atraso na entrega, o assunto principal abordado pelos clientes é a própria insatisfação com a demora ou com o não recebimento do produto até o momento da avaliação. 

* **Reclamações diretas de atraso na entrega:** Clientes registram expressamente a insatisfação com a entrega fora do prazo, classificando a demora em alguns casos como excessiva ou um absurdo [R1] [R2] [R3] [R4] [R5] [R6] [R8] [R9] [R10]. Nas estatísticas por palavras-chave da base filtrada, o tema "Atraso / demora na entrega" representa 32,9% (971) das menções.
* **Produto não recebido até a data da avaliação:** É o tema de maior frequência nas estatísticas da base filtrada, presente em 58,7% (1.734) das avaliações que tratam do assunto, refletido em relatos de clientes cujo produto ainda se encontrava atrasado/não entregue [R2] [R6] [R10].
* **Responsabilidade atribuída aos Correios:** É relatado caso pontual em que o atraso na entrega da mercadoria foi atribuído diretamente aos Correios [R7].
* **Outros temas identificados por palavras-chave:** Nas estatísticas da base filtrada, também aparecem citações sobre recomendação da loja (6,4% / 188), troca, devolução, cancelamento ou reembolso (5,8% / 171), percepções de entrega rápida/antes do prazo (5,3% / 155), atendimento/comunicação com vendedor (2,5% / 73), boa qualidade do produto (1,7% / 51) e produto errado ou diferente (1,6% / 47).

Limitações: Análise restrita à amostra de 10 avaliações disponibilizadas e às contagens automatizadas por palavras-chave, cobrindo apenas uma fração do volume total de pedidos atrasados.
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
Nas avaliações de notas baixas (1 a 3), os clientes reclamam sobretudo da lentidão ou falta de comunicação dos vendedores e da ausência de suporte para solucionar problemas com as compras. Nas estatísticas de temas da base filtrada, a categoria "Atendimento / comunicação com vendedor" representa 6,4% das menções (149 avaliações).

**Principais pontos de reclamação:**

- **Demora e falta de comunicação/retorno**: Os consumidores citam demora generalizada no atendimento [R10], lentidão para obter respostas do vendedor [R7], falta de contato por parte do vendedor para informar o cancelamento de pedidos não entregues [R3] e urgência/dificuldade em obter canais de contato [R1].
- **Falta de suporte e recusa na resolução de problemas**: Há relatos de atendimento classificado como "péssimo" [R3] [R6], além de casos em que solicitações de devolução foram canceladas pelo vendedor sem justificativa, deixando o cliente sem atendimento após receber um produto incompleto [R5].

Limitações: A amostra fornecida contém poucas evidências detalhadas de reclamações (e algumas avaliações trazem elogios), refletindo um recorte específico de notas 1 a 3.
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
Sim, os clientes reclamam expressivamente de receber produtos diferentes do anunciado, apontando divergências em relação a fotos, cores, especificações e qualidade. Nas estatísticas de temas sobre a base filtrada (notas 1 a 3), a categoria "Produto errado / diferente do anunciado" representa 19,5% das menções (192 avaliações entre as 987 que abordam o assunto).

Principais pontos identificados nas avaliações:

- **Incompatibilidade com fotos e imagens:** Clientes relatam que o produto físico recebido não corresponde à imagem ou às fotos disponibilizadas no anúncio [R1], [R6].
- **Divergência de cores:** Há relatos de envio de produtos em cores distintas das compradas, inclusive em casos onde foi pago um valor maior pela cor anunciada [R2].
- **Especificações e materiais incorretos:** Ocorrem divergências na descrição técnica, como percentual de composição do tecido (por exemplo, entrega de 80% algodão quando o anunciado era 100%) [R7], dimensões/formatos do material [R9] e descumprimento geral das especificações anunciadas [R3].
- **Qualidade inferior ao contratado:** Clientes mencionam que, além de receberem um produto diferente do solicitado, o item entregue é de qualidade inferior [R3], [R4].

Limitações: A análise baseia-se em uma amostra de avaliações filtradas por notas de 1 a 3 e contagens por palavras-chave, não devendo ser generalizada para todas as vendas da plataforma.
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
Os clientes relatam experiências mistas sobre a embalagem: enquanto há elogios à proteção dos produtos, existe uma frequência significativa de reclamações sobre caixas amassadas, deterioradas ou inadequadas. Nas estatísticas de temas (base de 1.882 avaliações com o assunto), 40,6% (765) destacam "Embalagem bem feita / bem protegido".

**Principais pontos identificados:**

- **Embalagens amassadas ou deterioradas:** É um padrão recorrente o recebimento de caixas e embalagens visivelmente amassadas, deterioradas ou com avarias externas [R1] [R2] [R3] [R4] [R7] [R9] [R10].
- **Impacto no produto recebido:** O uso de embalagem inadequada resultou em danos ao próprio produto em alguns casos [R5]. Em contrapartida, outros clientes destacam que, apesar de a embalagem ter chegado muito amassada ou danificada, o produto em si permaneceu intacto [R3] [R7] [R10].
- **Elogios e ausência de embalagem:** Há relatos pontuais de aprovação total ("ótima embalagem") [R8], bem como citação de produto entregue sem embalagem [R6].

Limitações: Análise restrita a uma amostra de 10 avaliações e a contagens automatizadas por palavras-chave na base filtrada.
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


# Exemplos de perguntas e respostas

Gerados por `python eval/run_eval.py` (embeddings `fastembed`, gerador `guardrail, llm:gemini/gemini-3.5-flash, llm:gemini/gemini-3.5-flash-lite`).

## Quais são os principais problemas relatados pelos clientes em suas avaliações?

*Modo:* `amplo` · *filtros:* nota 1–3 · *população:* 14438 avaliações

*Transformações da pergunta:* intenção negativa -> filtro nota <= 3; pergunta ampla (sem termo de conteúdo) -> decomposição em subconsultas pelos temas mais frequentes da população filtrada

```text
Os principais problemas relatados pelos clientes envolvem atrasos e não entrega de pedidos, envio de produtos errados ou de baixa qualidade, além de falhas no atendimento e cancelamentos sem justificativa. Na contagem de temas por palavras-chave da base filtrada (notas 1 a 3), as maiores ocorrências são de "Produto não recebido" (26,6%) e "Atraso / demora na entrega" (13,1%).

**Principais pontos:**

- **Não entrega e atrasos de envio:** Clientes reclamam da falta de recebimento dos produtos, demoras no prazo de entrega e do fato de serem cobrados a avaliar itens que ainda não chegaram [R1] [R2] [R3] [R4]. Conforme as estatísticas por palavras-chave na base filtrada, o tema "Produto não recebido (até a data da avaliação)" representa 26,6% (3.845 avaliações) e "Atraso / demora na entrega" representa 13,1% (1.896 avaliações).
- **Recebimento de produto errado ou divergente:** Há relatos recorrentes de entregas de itens incorretos ou divergentes do que foi anunciado, incluindo divergências de cor e tamanho [R6] [R7] [R8]. O tema "Produto errado / diferente do anunciado" soma 8,1% (1.173 avaliações) da base filtrada.
- **Qualidade insatisfatória e problemas no pós-venda:** Consumidores relatam insatisfação com a baixa qualidade dos produtos [R3] [R7], falta de suporte da loja diante de atrasos [R4] e cancelamento de compras sem explicação após a aprovação do pagamento [R5]. O tema "Troca, devolução, cancelamento ou reembolso" corresponde a 12,1% (1.742 avaliações) das contagens por palavras-chave.

Limitações: A análise reflete uma amostra de 8 avaliações qualitativas e estatísticas de palavras-chave restritas a pedidos com notas de 1 a 3.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 1 | 2018-05-16 | bebes | atrasado | ainda recomendo. Se o produto não chegou, como pode ser obrigatório o preenchimento da avaliação geral ou se eu recomendo a loja?! Piada né?! |
| R2 | 1 | 2017-02-01 | desconhecida | nao_entregue | Produto não entregue = consumidor insatisfeito. Preciso de retorno do stark se o produto ainda será entregue ou não. |
| R3 | 1 | 2018-06-19 | automotivo | atrasado | produto insatisfatorio. demora na entrega e produto de baixa qualidade |
| R4 | 2 | 2018-01-29 | papelaria | atrasado | Falta de consideração com o cliente, pois ocorreu problema na entrega é em momento nenhum o problema foi tratado.duas compras, uma com prazo de entrega 15 e 21/02, as 2 atrasou, liguei dia 23 reclaman |
| R5 | 1 | 2017-02-26 | desconhecida | nao_entregue | compra efetuada,debito autorizado ,pedido cancelado sem explicações.Extrema falta de respeito e consideração com os clientes. |
| R6 | 1 | 2018-08-17 | desconhecida | nao_entregue | Produto errado. Entrega do produto diferente do solicitado Aguardo orientação para a troca |
| R7 | 1 | 2017-11-09 | cama_mesa_banho | no_prazo | Produto errado,cor e tamanho errado, péssima qualidade. |
| R8 | 1 | 2018-08-21 | desconhecida | nao_entregue | Produto incorreto. Produto diferente do anunciado |

## O que os clientes relatam sobre problemas relacionados à entrega?

*Modo:* `focado` · *filtros:* nota 1–3 · *população:* 14438 avaliações

*Transformações da pergunta:* intenção negativa -> filtro nota <= 3; expansão BM25 com sinônimos de: entrega

```text
Os clientes relatam predominantemente atrasos no recebimento de seus produtos, além de enfrentarem informações confusas de rastreio, desencontros logísticos e casos em que o pedido consta como entregue, mas foi recebido apenas parcialmente.

**Principais pontos relatados:**

- **Atrasos e demora na entrega:** A maioria das reclamações individuais menciona expressamente a entrega atrasada ou a demora no recebimento [R1], [R2], [R3], [R4], [R6], [R8]. Um cliente questiona se o motivo do atraso seria uma greve dos Correios [R4], enquanto outro nota que, apesar de atrasar, a empresa se desculpou e realizou a entrega [R5]. Segundo as estatísticas de temas, "Atraso / demora na entrega" representa 22,5% (1.812) e "Produto não recebido" representa 40,0% (3.227) das avaliações que mencionam o assunto na base filtrada.
- **Informações confusas e desencontros:** Clientes destacam a falta de clareza e o caráter confuso das informações sobre a entrega [R9], além da ocorrência de desencontros durante a realização das entregas [R10].
- **Divergência de status e entregas incompletas:** É relatado que o sistema indicava o pedido como entregue, mas na verdade apenas parte da compra (1 produto) havia chegado [R7]. Nas estatísticas de temas, "Pedido incompleto / itens faltando" soma 6,6% (531) das menções.

Limitações: A análise reflete uma amostra de 10 avaliações e estatísticas por palavras-chave restritas a pedidos com nota de 1 a 3.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 1 | 2018-02-06 | utilidades_domesticas | atrasado | Atraso na entrega |
| R2 | 1 | 2018-04-25 | esporte_lazer | atrasado | Atrasou na entrega |
| R3 | 1 | 2017-11-25 | cama_mesa_banho | atrasado | Produto com entrega atrasada |
| R4 | 1 | 2018-02-27 | brinquedos | atrasado | Entrega atrasada sera que é correios em greve? |
| R5 | 3 | 2017-10-20 | telefonia | no_prazo | Chegou atrasado mais se desculparam e fizeram a entrega. |
| R6 | 3 | 2017-07-23 | eletronicos | no_prazo | Atrasou a entrega |
| R7 | 1 | 2018-06-28 | cool_stuff | no_prazo | Em partes. Sou cliente há anos, porém sempre há divergências e problemas na entrega, consta como produto entregue, porém foi entregue apenas 1 produto, aguardo solução! |
| R8 | 3 | 2018-02-18 | esporte_lazer | atrasado | Demora na entrega e ainda atrasou. |
| R9 | 1 | 2017-11-25 | cama_mesa_banho | atrasado | sem comentarios, muito confusa a informação sobre entrega |
| R10 | 1 | 2017-05-30 | cama_mesa_banho | no_prazo | muitos desencontros nas entregas de produtos |

## Quais aspectos da experiência de compra são mais elogiados pelos clientes?

*Modo:* `amplo` · *filtros:* nota 4–5 · *população:* 27676 avaliações

*Transformações da pergunta:* intenção positiva -> filtro nota >= 4; pergunta ampla (sem termo de conteúdo) -> decomposição em subconsultas pelos temas mais frequentes da população filtrada

```text
Os clientes com avaliações positivas (notas 4–5) elogiam principalmente a agilidade na entrega, a qualidade dos produtos adquiridos, o bom atendimento dos vendedores e o custo-benefício das compras. Nas estatísticas agregadas por palavras-chave sobre a base filtrada de 27.676 avaliações, a entrega rápida é o tema mais frequente (29,4%), seguida pela recomendação da loja (20,6%) e pela boa qualidade do produto (18,8%).

Principais aspectos elogiados:

* **Rapidez e pontualidade na entrega:** É o tema de maior frequência na base filtrada (8.133 menções / 29,4%). Os consumidores destacam com frequência o recebimento de produtos antes do prazo acordado e a agilidade das entregas [R1] [R2] [R4] [R7], além do cumprimento da pontualidade [R3].
* **Qualidade do produto:** Tema presente em 5.208 avaliações (18,8%) nas contagens da base. Os clientes ressaltam explicitamente a qualidade dos itens recebidos [R3] [R5] [R6] [R7] [R8].
* **Atendimento, compromisso e profissionalismo:** Há elogios voltados ao cuidado, à atenção da loja, à responsabilidade dos vendedores e ao compromisso geral no processo de compra [R1] [R4] [R5] [R6].
* **Preço e custo-benefício:** Representando 814 menções (2,9%) na contagem por palavras-chave, os clientes afirmam que os preços praticados e o bom custo-benefício tornam a compra vantajosa [R7] [R8].
* **Cuidado com a embalagem:** Tema registrado em 738 avaliações (2,7%) da base, sendo exemplificado pelo recebimento de produtos bem embalados [R2].
* **Satisfação e recomendação da loja:** A intenção de recomendar a loja ou comprar novamente aparece em 5.706 avaliações (20,6%) na estatística da base, sendo reafirmada expressamente pelos compradores [R2] [R3] [R4] [R7] [R8].

Limitações: A análise baseia-se exclusivamente em uma amostra de 8 trechos de avaliações e nas estatísticas de contagem por palavras-chave da população filtrada de notas 4–5.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 5 | 2018-05-07 | automotivo | no_prazo | Loja atenciosa com os clientes super recomendo; alem de toda atençao com os clientes produto chegou antes do prazo |
| R2 | 5 | 2017-05-21 | perfumaria | no_prazo | Gostei do produto que comprei veio bem embalado o prazo de entrega nem se fala sensacional chegou muito rapido, futuramente vou fazer mais compras recomendo essa loja pode comprar sem medo. |
| R3 | 5 | 2017-11-12 | bebes | no_prazo | Recomendo a compra nessa loja, primam pela pontualidade e qualidade dos produtos. |
| R4 | 5 | 2017-05-05 | papelaria | no_prazo | Excelente loja eu recomendoa todos principalmente o vendedor nota mil. ..recebi antes a mercadoria e muito gostei da responsabilidade e do proficioanal com o cliente digo várias vezes nota mil👏👏 |
| R5 | 5 | 2018-04-29 | informatica_acessorios | no_prazo | Produto de qualidade!. Compromisso com o cliente e qualidade no produto resumem essa compra. |
| R6 | 5 | 2018-06-11 | eletronicos | no_prazo | Ótimo vendedor!. Produto de qualidade, excelência no processo de compra. |
| R7 | 5 | 2017-06-28 | perfumaria | no_prazo | Preço, agilidade e qualidade do produto fizeram valer a pena. Recomendo |
| R8 | 5 | 2018-08-23 | papelaria | no_prazo | Excelente. Ótimo produto e custo beneficio, eu recomento, e sobre a lojas lannister, a melhor opçao de compras! |

## Quais padrões podem ser identificados nas avaliações de clientes insatisfeitos?

*Modo:* `amplo` · *filtros:* nota 1–2 · *população:* 10841 avaliações

*Transformações da pergunta:* intenção negativa -> filtro nota <= 2; pergunta ampla (sem termo de conteúdo) -> decomposição em subconsultas pelos temas mais frequentes da população filtrada

```text
Com base na amostra de avaliações e nas estatísticas da população filtrada (notas 1–2), os clientes insatisfeitos manifestam padrões focados principalmente em problemas logísticos de entrega, recebimento de produtos divergentes ou de baixa qualidade e falhas na comunicação da loja.

Os principais padrões identificados são:

* **Não recebimento e atrasos na entrega:** Clientes relatam produtos que não chegaram no prazo ou que não foram entregues, além do desconforto de serem cobrados a avaliar itens ainda não recebidos [R1] [R2] [R5] [R6]. Nas estatísticas de temas, "Produto não recebido (até a data da avaliação)" representa 31,9% da população filtrada (3.454 avaliações) e "Atraso / demora na entrega" soma 14,0% (1.518 avaliações).
* **Produtos errados ou com qualidade abaixo do esperado:** Há relatos de entrega de itens diferentes dos anunciados ou com qualidade muito inferior à descrição da compra [R5] [R7] [R8]. O tema "Produto errado / diferente do anunciado" equivale a 9,0% das avaliações da base filtrada (972 avaliações).
* **Falta de comunicação, suporte e cancelamentos sem explicação:** Os consumidores reclamam da ausência de atualizações/satisfações sobre o status do pedido, pedidos cancelados sem justificativa e demora no direcionamento para trocas [R1] [R3] [R4] [R6]. Nas estatísticas, "Troca, devolução, cancelamento ou reembolso" contabiliza 14,1% (1.531 avaliações).

Limitações: Análise restrita a uma amostra de 8 avaliações individuais e às estatísticas agregadas por palavras-chave na base filtrada.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 1 | 2017-02-01 | desconhecida | nao_entregue | Produto não entregue = consumidor insatisfeito. Preciso de retorno do stark se o produto ainda será entregue ou não. |
| R2 | 1 | 2018-05-16 | bebes | atrasado | ainda recomendo. Se o produto não chegou, como pode ser obrigatório o preenchimento da avaliação geral ou se eu recomendo a loja?! Piada né?! |
| R3 | 1 | 2017-02-26 | desconhecida | nao_entregue | compra efetuada,debito autorizado ,pedido cancelado sem explicações.Extrema falta de respeito e consideração com os clientes. |
| R4 | 1 | 2018-08-17 | desconhecida | nao_entregue | Produto errado. Entrega do produto diferente do solicitado Aguardo orientação para a troca |
| R5 | 1 | 2018-06-19 | automotivo | atrasado | produto insatisfatorio. demora na entrega e produto de baixa qualidade |
| R6 | 1 | 2017-11-14 | moveis_decoracao | atrasado | Atraso na entrega sem dar satisfação ao cliente, que com certeza escolheu o produto com cuidado e com as melhores expectativas. Falta de consideração. |
| R7 | 1 | 2018-04-17 | informatica_acessorios | no_prazo | O produto anunciado é um e o produto entregue é outro e de baixissima qualidade. Inadimissivel esse tipo de atitude que fere o codigo de defesa do consumidor, entregar produto diferente do anunciado |
| R8 | 1 | 2018-01-15 | moveis_decoracao | no_prazo | O produto não corresponde às expectativas. A qualidade é muito aquém da descrição do produto. |

## Quais avaliações sustentam a conclusão de que existem problemas recorrentes relacionados ao prazo de entrega?

*Modo:* `focado` · *filtros:* nota 1–3 · *população:* 14438 avaliações

*Transformações da pergunta:* intenção negativa -> filtro nota <= 3; expansão BM25 com sinônimos de: entrega, prazo

```text
As avaliações [R1], [R2], [R3], [R4], [R6], [R7], [R8], [R9] e [R10] sustentam explicitamente a existência de problemas recorrentes relacionados ao prazo de entrega. Essa insatisfação é corroborada pelas estatísticas de temas da base filtrada, onde o assunto "Atraso / demora na entrega" representa 1.812 menções (22,3% das 8.131 avaliações que citam algum tema).

Principais pontos identificados nas evidências:

- **Atrasos explícitos no recebimento:** Clientes relatam que seus produtos sofreram atraso ou chegaram fora do prazo prometido [R1], [R3], [R7], [R8], [R9]. 
- **Recorrência dos atrasos:** A percepção de um problema recorrente é destacada expressamente em [R4] ("Ultimamente estão atrasando muito as entregas") e motivou nota baixa devido aos atrasos [R2].
- **Impacto e percepção de demora:** O descumprimento do prazo gerou prejuízos práticos aos consumidores, como atraso em obras [R3], além de reclamações sobre prazos de entrega excessivamente demorados ou acima do habitual [R6], [R10].
- **Comunicação falha sobre a entrega:** Foi relatado um alerta de problema na entrega sem explicações claras sobre a causa ou solução, o que gerou ansiedade desnecessária até a chegada do pedido [R5].

Limitações: As evidências são uma amostra qualitativa restrita e as estatísticas baseiam-se em contagens automatizadas por palavras-chave na base filtrada.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 3 | 2018-02-17 | bebes | atrasado | Produto com o prazo de entrega atrasado |
| R2 | 1 | 2018-02-28 | moveis_escritorio | no_prazo | Nao tem boa avaliação por atraso na entrega |
| R3 | 3 | 2018-03-08 | moveis_decoracao | atrasado | O atraso na entrega prejudicou a obra |
| R4 | 1 | 2018-03-03 | construcao_ferramentas_construcao | atrasado | Ultimamente estão atrasando muito as entregas |
| R5 | 3 | 2017-11-28 | cama_mesa_banho | no_prazo | Foi falado que houve problemas na entrega mas não falava o que e nem como seria resolvido. Me causou uma preocupação e frustração desnecessária já que o mesmo chegou antes do prazo estipulado. |
| R6 | 3 | 2017-08-08 | artes | no_prazo | Um prazo de entrega demorado |
| R7 | 1 | 2018-08-07 | cool_stuff | atrasado | PRODUTO 3 DIAS DE ATRASO. PRODUTO COM 3 DIAS DE ATRASO NA ENTREGA |
| R8 | 1 | 2017-11-25 | cama_mesa_banho | atrasado | Produto com entrega atrasada |
| R9 | 1 | 2018-03-19 | moveis_decoracao | atrasado | demora na entrega (ainda nao chegou fora do prazo) |
| R10 | 2 | 2017-06-12 | cool_stuff | no_prazo | Demorou de entregar geralmente chega bem antes do prazo teve algo que atrapalhou a entrega! |

## Existem padrões recorrentes nas avaliações relacionadas à qualidade dos produtos?

*Modo:* `focado` · *filtros:* sem filtros · *população:* 42114 avaliações

*Transformações da pergunta:* expansão BM25 com sinônimos de: qualidade

```text
Sim, existem padrões claros e polarizados nas avaliações sobre a qualidade dos produtos. Enquanto uma parte considerável dos consumidores expressa satisfação com o material e acabamento, há um padrão recorrente de insatisfação ligado à fragilidade, defeitos ao receber o item e divergência em relação ao anúncio no site.

- **Elogios à qualidade, acabamento e originalidade**: Clientes reportam que os produtos atendem às expectativas, destacando materiais de qualidade, bom acabamento e itens originais [R1], [R3], [R5], [R8], [R10]. Nas estatísticas de temas (contagem por palavras-chave na base filtrada), "Boa qualidade do produto" é a menção mais recorrente, representando 43,7% das avaliações do grupo (1.983 menções).
- **Fragilidade e produtos recebidos com defeito ou quebrados**: Há relatos de produtos considerados frágeis que já chegam ao cliente quebrados ou com componentes defeituosos [R2], [R4], [R6]. Esse padrão é respaldado pelas estatísticas dos temas "Qualidade abaixo do esperado" (25,0% / 1.133 menções) e "Defeito / produto quebrado ou avariado" (15,5% / 701 menções).
- **Divergência entre a imagem/anúncio no site e o produto entregue**: Clientes expressam insatisfação ao notar que a qualidade real do material, acabamento ou originalidade do produto é inferior à que aparentava ser na plataforma [R4], [R9].

Limitações: A análise baseia-se em uma amostra de 10 avaliações e em contagens estatísticas agregadas por palavras-chave de diversas categorias de produtos.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 5 | 2017-03-10 | cama_mesa_banho | no_prazo | O PRODUTO ESTÁ DENTRO DOS PADRÕES DE QUALIDADE,ATENDENDO MINHA EXPECTATIVA |
| R2 | 1 | 2017-05-12 | moveis_decoracao | no_prazo | A arara é de qualidade ruim, fragil o que fez com que o mesmo ja chegasse quebrada |
| R3 | 5 | 2018-01-16 | cama_mesa_banho | no_prazo | Adorei a qualidade e o acabamento. |
| R4 | 3 | 2018-08-02 | climatizacao | no_prazo | A qualidade do produto deixa a desejar, pois é muito frágil, longe do original. |
| R5 | 5 | 2018-07-20 | pet_shop | no_prazo | Material de qualidade. |
| R6 | 1 | 2017-11-24 | relogios_presentes | no_prazo | Produto de péssima qualidade, ja chegou com o cronômetro quebrado e os botões com defeito |
| R7 | 5 | 2018-07-17 | automotivo | no_prazo | Agora e usar o produto para avaliar a qualidade. |
| R8 | 5 | 2017-09-10 | esporte_lazer | no_prazo | Produto de qualidade e dentro do prazo |
| R9 | 3 | 2018-07-03 | beleza_saude | no_prazo | Insatisfeito. No site o produto parece ter melhor qualidade de material e acabamento. |
| R10 | 5 | 2018-02-21 | relogios_presentes | atrasado | Original ,de qualidade superior. |

## O que os clientes mais elogiam em produtos de beleza?

*Modo:* `amplo` · *filtros:* nota 4–5; categoria beleza_saude · *população:* 2416 avaliações

*Transformações da pergunta:* intenção positiva -> filtro nota >= 4; categoria citada -> filtro ['beleza_saude']; pergunta ampla (sem termo de conteúdo) -> decomposição em subconsultas pelos temas mais frequentes da população filtrada

```text
Os clientes da categoria de beleza e saúde elogiam principalmente a agilidade na entrega, a alta qualidade dos produtos e a experiência satisfatória com a loja e os vendedores. Adicionalmente, destacam o cuidado com o acondicionamento e embalagem dos itens.

**Principais pontos elogiados:**

* **Agilidade e cumprimento da entrega:** É o tema mais frequente nas estatísticas de palavras-chave da população filtrada, presente em 32,2% das avaliações (777 menções). Os clientes destacam entregas realizadas dentro ou antes do prazo final [R1] [R2] [R7].
* **Recomendação da loja e dos vendedores:** Representando 21,9% das estatísticas da base (528 menções), os compradores demonstram satisfação recomendando a loja e os vendedores para outros consumidores [R3] [R4] [R5] [R6].
* **Qualidade do produto:** Tema presente em 17,1% das avaliações da base (413 menções). Os clientes qualificam os itens recebidos como "de alta qualidade", "muito bom" e "maravilhoso", além de citarem que o produto veio conforme o descrito [R1] [R2] [R4] [R5] [R6].
* **Embalagem e cuidado com o pedido:** Aparece em 2,4% das estatísticas (58 menções), com clientes ressaltando o cuidado no envio e os produtos bem embalados [R7] [R8].

**Limitações:** As conclusões baseiam-se em uma amostra de 8 avaliações individuais e em contagens por palavras-chave restritas a pedidos com notas 4 e 5 da categoria beleza_saude.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 5 | 2017-09-08 | beleza_saude | no_prazo | Qualifico como ótima compra. Recomendo a todos. Entrega feita no prazo, produto maravilhoso. |
| R2 | 5 | 2018-01-05 | beleza_saude | no_prazo | Entrega antes do prazo, produto de alta qualidade. |
| R3 | 4 | 2017-09-04 | beleza_saude | no_prazo | recomendo tanto a loja como o produto.gostei |
| R4 | 5 | 2017-12-11 | beleza_saude | no_prazo | Produto muito bom,a loja tbem recomendo a todos que queiram adquirir o produto |
| R5 | 4 | 2017-05-05 | beleza_saude | no_prazo | muito bom o produto super recomendo o vendedor |
| R6 | 5 | 2017-12-11 | beleza_saude | no_prazo | Tudo veio do jeito descrito, produto de ótima qualidade, recomendo vendedor. |
| R7 | 4 | 2017-05-14 | beleza_saude | no_prazo | Produto bem embalado e entrega de qualidade |
| R8 | 5 | 2018-04-04 | beleza_saude | no_prazo | Agradeço a atenção e o cuidado com minha compra. Produto muito bem embalado. |

## Quais são os principais problemas relatados nas avaliações com nota baixa?

*Modo:* `amplo` · *filtros:* nota 1–2 · *população:* 10841 avaliações

*Transformações da pergunta:* intenção negativa -> filtro nota <= 2; pergunta ampla (sem termo de conteúdo) -> decomposição em subconsultas pelos temas mais frequentes da população filtrada

```text
Os principais problemas relatados nas avaliações com nota baixa concentram-se em não recebimento ou atraso na entrega, divergências de qualidade e especificações dos produtos, além de cancelamentos sem explicação e necessidade de trocas. Segundo a contagem por palavras-chave na base filtrada de notas 1 e 2, o tema "Produto não recebido" é o mais frequente, representando 31,9% dos casos.

Principais pontos:

* **Não recebimento e atraso na entrega:** Há relatos diretos de clientes que não receberam a mercadoria até o momento da avaliação ou que sofreram com a demora no transporte [R1] [R2] [R5] [R6]. Na estatística por palavras-chave da base filtrada, "Produto não recebido (até a data da avaliação)" soma 3.454 casos (31,9%) e "Atraso / demora na entrega" soma 1.518 casos (14,0%).
* **Produtos divergentes do anunciado e baixa qualidade:** Clientes apontam ter recebido produtos com medidas incorretas em relação à oferta, de qualidade ruim ou aquém do que foi descrito na publicação [R4] [R6] [R7] [R8]. O tema "Produto errado / diferente do anunciado" responde por 972 ocorrências (9,0%) na base filtrada.
* **Cancelamentos arbitrários e necessidade de trocas:** Identificam-se relatos de pedidos cancelados sem explicações após a autorização do débito [R3], bem como a necessidade de acionar a empresa para efetuar trocas devido ao envio de itens incorretos [R4]. O tema "Troca, devolução, cancelamento ou reembolso" representa 1.531 ocorrências (14,1%) nas contagens da base filtrada.

Limitações: A análise baseia-se em uma amostra de 8 avaliações e nas estatísticas de palavras-chave da população filtrada (notas 1 a 2).
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 2 | 2017-09-22 | eletronicos | no_prazo | ainda não recebi o produto, mas sem receber o produto, a avaliação fica "furada". |
| R2 | 1 | 2018-01-30 | moveis_escritorio | atrasado | - a compra foi efetuada em 30/01 - a emissão da nota fiscal emitida em 05/02 - até 16/03 ainda não recebemos a mercadoria - que avaliação deveríamos dar a isto? - desonestos? ineficientes? etc, et |
| R3 | 1 | 2017-02-26 | desconhecida | nao_entregue | compra efetuada,debito autorizado ,pedido cancelado sem explicações.Extrema falta de respeito e consideração com os clientes. |
| R4 | 2 | 2018-06-11 | informatica_acessorios | no_prazo | produto incorreto. O produto não está nas medidas corretas indicadas na oferta. Terei q ligar para vcs para troca |
| R5 | 1 | 2018-02-28 | moveis_escritorio | no_prazo | Nao tem boa avaliação por atraso na entrega |
| R6 | 1 | 2018-06-19 | automotivo | atrasado | produto insatisfatorio. demora na entrega e produto de baixa qualidade |
| R7 | 1 | 2018-08-01 | cama_mesa_banho | no_prazo | Produto de qualidade ruim. Produto diferente do que foi anunciado. |
| R8 | 1 | 2018-01-15 | moveis_decoracao | no_prazo | O produto não corresponde às expectativas. A qualidade é muito aquém da descrição do produto. |

## Quais temas aparecem nas avaliações de pedidos entregues com atraso?

*Modo:* `focado` · *filtros:* entrega atrasado · *população:* 3809 avaliações

*Transformações da pergunta:* 'entregas atrasadas' -> filtro delivery_status = atrasado; expansão BM25 com sinônimos de: atras

```text
Nas avaliações de pedidos entregues com atraso, os clientes focam predominantemente no não recebimento do produto dentro do prazo estipulado e na insatisfação com a demora logística. Nas estatísticas de temas da base filtrada, destacam-se a ausência do produto no momento da avaliação (58,7%) e a reclamação explícita de atraso (32,9%).

**Principais pontos identificados:**

- **Reclamação direta de atraso e produto não recebido:** Os clientes relatam que os produtos estão atrasados ou ainda não foram entregues [R1], [R2], [R3], [R4], [R5], [R6], [R7], [R8]. De acordo com a contagem de palavras-chave na base filtrada (2.952 avaliações), os temas mais frequentes são "Produto não recebido (até a data da avaliação)" com 1.734 menções (58,7%) e "Atraso / demora na entrega" com 971 menções (32,9%).
- **Impacto na nota e percepção de reincidência:** O descumprimento do prazo afeta diretamente a pontuação dada ao pedido, impedindo avaliações máximas [R10]. Além disso, há clientes apontando que prazos originalmente longos continuam sendo descumpridos [R5] e a sensação de que os atrasos estão ocorrendo com frequência [R7].
- **Causas atribuídas pelo cliente:** Há menção de cliente atribuindo a culpa do atraso ao serviço dos Correios [R9].
- **Outros temas presentes na estatística da base:** Em menor frequência, as avaliações que cobrem o filtro também citam "Recomenda a loja / compraria novamente" (188 menções | 6,4%), "Troca, devolução, cancelamento ou reembolso" (171 menções | 5,8%), "Entrega rápida / antes do prazo" (155 menções | 5,3%), "Atendimento / comunicação com vendedor" (73 menções | 2,5%), "Boa qualidade do produto" (51 menções | 1,7%) e "Produto errado / diferente do anunciado" (47 menções | 1,6%).

**Limitações:** A análise reflete apenas a amostra fornecida de 10 comentários e os dados agregados por palavras-chave na população filtrada por "entrega atrasado".
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 3 | 2018-02-17 | bebes | atrasado | Produto com o prazo de entrega atrasado |
| R2 | 1 | 2018-03-15 | eletronicos | atrasado | produto em atraso. |
| R3 | 1 | 2018-03-02 | utilidades_domesticas | atrasado | A entrega esta atrasada. |
| R4 | 4 | 2018-03-25 | ferramentas_jardim | atrasado | Produto está atrasado |
| R5 | 1 | 2017-07-21 | relogios_presentes | atrasado | Pedido já tinha um longo prazo para entrega e ainda atrasa. Produto não recebido ainda. |
| R6 | 1 | 2017-11-25 | cama_mesa_banho | atrasado | Produto com entrega atrasada |
| R7 | 1 | 2018-03-03 | construcao_ferramentas_construcao | atrasado | Ultimamente estão atrasando muito as entregas |
| R8 | 1 | 2018-03-01 | informatica_acessorios | atrasado | O produto está atrasado |
| R9 | 2 | 2018-02-23 | construcao_ferramentas_construcao | atrasado | creio que o atraso e dos correios |
| R10 | 3 | 2018-02-25 | informatica_acessorios | atrasado | não do 5 estrela pois atrasou pedido |

## O que os clientes reclamam sobre o atendimento do vendedor?

*Modo:* `focado` · *filtros:* nota 1–3 · *população:* 14438 avaliações

*Transformações da pergunta:* intenção negativa -> filtro nota <= 3; expansão BM25 com sinônimos de: atendimento

```text
Os clientes reclamam principalmente da falta ou demora no retorno dos vendedores, da dificuldade de estabelecer contato direto e do descaso em informar sobre problemas nos pedidos. Na base filtrada (notas 1–3), a contagem por palavras-chave indica que o tema "Atendimento / comunicação com vendedor" esteve presente em 149 avaliações (6,4% das menções analisadas).

Principais pontos de reclamação:
- **Demora e ausência de retorno:** Os clientes relatam lentidão na resposta do vendedor [R1] ou a ausência total de contato [R5], [R9], inclusive enquanto aguardam retorno para tratar da devolução de produtos defeituosos [R10] ou sobre o cancelamento de itens não entregues [R5].
- **Dificuldade de contato e canais automatizados:** Há relatos de entraves no diálogo [R2], dependência de atendimento exclusivamente eletrônico que força o cliente a esperar [R6] e falta de opções de contato direto, como número de telefone [R4].
- **Descaso e falta de atenção:** É relatado descaso por parte da loja/vendedor [R6] e cobrada uma postura mais atenciosa [R7], criticando a falta de comunicação proativa para avisar sobre cancelamentos e não entregas [R5].

Limitações: Análise baseada estritamente em uma amostra de 10 avaliações e nas estatísticas por palavras-chave da base filtrada (notas 1–3).
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 3 | 2018-05-25 | brinquedos | no_prazo | Prazo de entrega absurdo e demora no retorno do vendedor |
| R2 | 2 | 2017-08-25 | beleza_saude | atrasado | Difícil diálogo com vendedor |
| R3 | 3 | 2017-05-08 | beleza_saude | no_prazo | Vendedores muito atenciosos. |
| R4 | 1 | 2017-05-09 | informatica_acessorios | nao_entregue | Preciso de números telefones de contato com o atendimento baratheon ou do vendedor. URGENTE |
| R5 | 1 | 2018-05-01 | brinquedos | nao_entregue | Pessimo atendimento. O objeto comprado nao foi entregue a venda cancelada e em nenhum momento o vendedor entrou em contato comigo para me informar |
| R6 | 2 | 2018-07-22 | eletronicos | nao_entregue | descaso com o cliente. muito ruim, atendimento somente eletronico, vc é obrigado a esperar pele boa vontade da loja para entrar em contato. |
| R7 | 3 | 2018-03-12 | eletronicos | no_prazo | produto entregue, mais os vendedores deveriam ser mais atenciosos. |
| R8 | 1 | 2017-09-18 | beleza_saude | no_prazo | amei a forma de entega foi muito rápido e prático to satisfeita agradeço este site e ao vendedor pela agilidade de atendimento e entrega do meu produto.. |
| R9 | 1 | 2017-05-31 | utilidades_domesticas | nao_entregue | Uma porcaria.. Vendedor não entra em contato..quero o meu dinheiro de volta. .ou então vou a delegacia do consumidor |
| R10 | 1 | 2017-04-20 | cama_mesa_banho | no_prazo | Produto com defeito aguardando retorno do vendedor para devolução |

## Os clientes reclamam de receber produtos diferentes do anunciado?

*Modo:* `focado` · *filtros:* nota 1–3 · *população:* 14438 avaliações

*Transformações da pergunta:* intenção negativa -> filtro nota <= 3

```text
Sim, os clientes reclamam de receber produtos diferentes do anunciado, sendo este o segundo tema mais frequente nas estatísticas de temas com 192 menções (19.5% da base de 987 avaliações que mencionam o assunto) [R1-R10]. As queixas detalham divergências em especificações, materiais, cores e qualidade inferior [R1-R10].

* **Divergência de especificações e materiais:** Clientes relatam que os itens entregues não conferem com o anúncio, como composição de tecido incorreta (80% algodão em vez de 100%) e materiais com tamanhos divergentes nos lados [R2] [R3] [R6].
* **Incompatibilidade de cores e modelos:** Há relatos de recebimento de produtos totalmente diferentes das fotos divulgadas, cores enviadas em desacordo com a escolha (como receber roxo em vez de vermelho) e kits com variedade de cores menor do que a anunciada [R1] [R5] [R8] [R9].
* **Baixa qualidade e itens faltantes:** Além de o produto não ser o mesmo do anúncio, os consumidores apontam baixa qualidade e, em alguns casos, recebimento de quantidade inferior à comprada, gerando pedidos de reembolso [R1] [R8] [R10].

Limitações: A análise baseia-se em uma amostra qualitativa de 10 avaliações detalhadas e estatísticas de palavras-chave de um subconjunto de 987 avaliações dentro da população filtrada de notas 1 a 3.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 1 | 2017-09-16 | fashion_roupa_masculina | no_prazo | o produto recebido não e o mesmo que estava no anuncio, nao sei o que aconteceu, mais o produto recebido e de baixa qualidade. |
| R2 | 1 | 2018-08-09 | esporte_lazer | no_prazo | Péssimo. O produto recebido é diferente e inferior ao adquirido.Não confere com as especificações anunciadas. |
| R3 | 1 | 2017-06-11 | cama_mesa_banho | no_prazo | PRODUTO COM AS ESPECIFICAÇÕES DIFERENTES DO ANUNCIADO. 80% ALGODÃO AO INVÉS DE 100% COMO DIZIA NO ANUNCIO |
| R4 | 1 | 2018-02-11 | informatica_acessorios | no_prazo | produto diferente do anunciado |
| R5 | 1 | 2018-01-15 | cama_mesa_banho | no_prazo | Comprei 8 toalhas pois cada uma seria de uma pessoa diferenciando pela cor , assim como dizia no anúncio que seriam 8 toalhas de 8 cores diferentes e recebi 8 toalhas com 4 cores diferentes. |
| R6 | 3 | 2018-06-23 | eletrodomesticos | no_prazo | DIFERENTE DO ANUNCIADO. NO ANUNCIO DIZIA SER AMBOS OS LADOS IGUAIS POREM O MATERIAL TEM LADOS DIFERENTES, OU SEJA, UM LADO MAIOR E O OUTRO LADO MENOR. |
| R7 | 1 | 2017-05-05 | telefonia_fixa | no_prazo | Comprei um produto que esteva anunciando uma coisa e o produto não corresponde ao anúncio |
| R8 | 1 | 2017-08-05 | brinquedos | no_prazo | O produto que recebi é totalmente diferente do que é divulgado nas fotos do anúncio! Produto de qualidade baixa. Dá pra perceber que as etiquetas são diferentes. Estou muito insatisfeito! |
| R9 | 1 | 2018-04-18 | utilidades_domesticas | no_prazo | paguei mais caro para receber o produto na cor do anuncio que é vermelho e recebi roxo |
| R10 | 1 | 2017-03-10 | informatica_acessorios | no_prazo | Recebi produtos diferentes do anunciado e pior de 02 und compradas recebi somente 01 und. Não gostei, pedi a devolução do dinheiro. |

## O que os clientes dizem sobre a embalagem dos produtos?

*Modo:* `focado` · *filtros:* sem filtros · *população:* 42114 avaliações

*Transformações da pergunta:* expansão BM25 com sinônimos de: embalagem

```text
Os clientes dividem-se entre elogios ao bom acondicionamento e reclamações recorrentes sobre embalagens que chegam amassadas ou avariadas durante o transporte. Enquanto parte das avaliações destaca que o produto veio bem protegido, diversos relatos apontam problemas com caixas danificadas, inclusive em itens sensíveis ou destinados a presentes.

**Principais pontos identificados:**

* **Embalagens amassadas e danificadas:** Há uma ocorrência frequente de queixas sobre caixas e embalagens que chegam amassadas, deterioradas ou com avarias decorrentes do transporte [R1], [R2], [R4], [R7], [R8], [R9], [R10].
* **Impacto em presentes e produtos delicados:** Os danos à embalagem geram insatisfação adicional quando a compra é um presente [R9] ou envolve itens que exigem maior cuidado, como medicamentos [R10].
* **Elogios à proteção e embalagem:** Por outro lado, existem clientes que elogiam a embalagem como sendo muito boa e com o produto bem protegido [R5], [R6]. Nas estatísticas de temas cobrindo 1.882 avaliações sobre o assunto, o tópico "Embalagem bem feita / bem protegido" aparece em 40,6% (765 mencões).
* **Sugestões de clientes para proteção extra:** Consumidores sugerem a utilização de caixas ou maior proteção no envio para evitar quebras ou avarias no produto [R3], [R10], além de solicitar melhorias no serviço de entrega [R1].

Limitações: Análise restrita a uma amostra de 10 avaliações e estatísticas baseadas em contagens de palavras-chave sobre o tema.
```

| Ref | Nota | Data | Categoria | Entrega | Avaliação |
|---|---|---|---|---|---|
| R1 | 2 | 2017-11-13 | informatica_acessorios | no_prazo | Entrega no prazo, o produto é bom, porem a embalagem durante o tranposte foi toda amassada com avarias.. melhorar o serviço de entrega. |
| R2 | 3 | 2017-12-05 | esporte_lazer | no_prazo | Embalagem e caixa do produto toda detereriorada |
| R3 | 3 | 2018-04-12 | alimentos | no_prazo | Gostaria de dar uma dica quanto a embalagem da entrega, poderia estar dentro de uma caixa para evitar que o produto venha avariado ou evitar possível quebra. |
| R4 | 3 | 2017-12-02 | informatica_acessorios | no_prazo | Embalagem chegou amassada. |
| R5 | 5 | 2017-07-17 | brinquedos | no_prazo | Empresa embalagem muito boa |
| R6 | 5 | 2017-11-28 | ferramentas_jardim | no_prazo | Foi entregue no prazo e muito bem protegido na embalagem |
| R7 | 4 | 2018-03-10 | perfumaria | atrasado | Avaria na embalagem, restante 100%.. |
| R8 | 4 | 2017-11-17 | papelaria | no_prazo | Embalagem amassada. |
| R9 | 4 | 2018-08-09 | construcao_ferramentas_iluminacao | no_prazo | recomendo. chegou, obrigada mas a caixa, a embalagem amassada e é um presente. |
| R10 | 5 | 2018-04-04 | pet_shop | no_prazo | Produto entregue bem antes do tempo, só uma dica, proteger um pouco mais a embalagem, , chegou amassado e é um medicamento |

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


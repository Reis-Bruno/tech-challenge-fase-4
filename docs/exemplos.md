# Exemplos de perguntas e respostas

Gerados por `python eval/run_eval.py` (embeddings `lsa`, gerador `guardrail, llm:gemini/gemini-3.5-flash, llm:gemini/gemini-3.5-flash-lite`).

## Quais são os principais problemas relatados pelos clientes em suas avaliações?

*Modo:* `amplo` · *filtros:* nota 1–3 · *população:* 14438 avaliações

*Transformações da pergunta:* intenção negativa -> filtro nota <= 3; pergunta ampla (sem termo de conteúdo) -> decomposição em subconsultas pelos temas mais frequentes da população filtrada

```text
Os principais problemas relatados pelos clientes com notas entre 1 e 3 referem-se à não entrega e ao atraso nos pedidos, seguidos por solicitações de troca/cancelamento e recebimento de produtos errados ou divergentes. De acordo com as estatísticas por palavras-chave na base filtrada, a não entrega do produto é a reclamação mais recorrente, representando 26,6% dos casos.

**Principais problemas identificados:**

*   **Produto não recebido (26,6% / 3.845 menções nas estatísticas):** É a principal queixa na base de dados, onde os clientes afirmam categoricamente que não receberam a mercadoria comprada [R1], [R2].
*   **Atraso / demora na entrega (13,1% / 1.896 menções nas estatísticas):** Clientes relatam entregas que demoraram além do esperado ou atrasaram em relação ao prazo estabelecido [R3], [R4].
*   **Troca, devolução, cancelamento ou reembolso (12,1% / 1.742 menções nas estatísticas):** Ocorrência de solicitações do consumidor para cancelar a compra ou buscar suporte para realizar a troca de itens [R5], [R6].
*   **Produto errado / diferente do anunciado (8,1% / 1.173 menções nas estatísticas):** Reclamações referentes ao envio de itens com especificações divergentes do anúncio (como conectores incompatíveis com o aparelho) ou produtos apresentando medições/funcionamento incorretos [R7], [R8].
*   **Outras categorias mapeadas nas estatísticas:** Também foram registradas queixas sobre defeito/avaria (6,4%), pedido incompleto/itens faltando (5,7%), qualidade abaixo do esperado (3,3%) e preço/custo-benefício (2,1%).

Limitações: A análise qualitativa apoia-se em uma amostra de 8 avaliações individuais e em contagens por palavras-chave restritas a avaliações com nota de 1 a 3.
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
Os clientes relatam insatisfação principalmente com atrasos, demoras no transporte e produtos pendentes de entrega, além de apontarem falhas de comunicação e contratempos logísticos. Nas estatísticas da população filtrada (notas 1–3), o tema "Produto não recebido" é o mais incidente (26,6%), seguido por "Atraso / demora na entrega" (13,1%).

Principais pontos relatados:

- **Atrasos e demora na entrega:** Há frequentes reclamações sobre descumprimento do prazo e demora excessiva para o envio ou chegada dos itens [R1], [R2], [R3], [R4], [R5], [R8]. Um cliente questiona se o motivo do atraso seria uma greve nos Correios [R3]. Estatisticamente, "Atraso / demora na entrega" representa 13,1% das avaliações da população filtrada (1.896 casos) e 22,5% das que mencionam o assunto.
- **Produto não entregue / pendente:** Clientes destacam que continuam aguardando a chegada de pedidos já atrasados [R5]. O tema "Produto não recebido" é o motivo com maior volume de contagem na base filtrada, somando 3.845 avaliações (26,6% da população filtrada e 40,0% entre as avaliações que mencionam o assunto).
- **Contratempos e falta de comunicação:** Consumidores relatam problemas na entrega decorrentes de parceiros logísticos e criticam a falta de aviso sobre o motivo das falhas [R7], [R10]. Há casos em que o problema foi resolvido antes da chegada [R6] ou que a empresa se desculpou pelo atraso ao entregar [R8].
- **Avaliações sem registro de contratempo:** Existe relato isolado em nota 3 que afirma ter recebido a entrega sem problemas [R9].

Limitações: Análise baseada em uma amostra de 10 avaliações e em contagens por palavras-chave restritas a pedidos com notas de 1 a 3.
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
Os aspectos mais elogiados pelos clientes com avaliações positivas (notas 4 e 5) referem-se à agilidade na entrega, à qualidade dos produtos recebidos e à satisfação geral que gera a intenção de recomprar.

* **Entrega rápida / antes do prazo**: É o tema mais frequente na base filtrada, representando 29,4% das avaliações (8.133 menções baseadas em palavras-chave), com clientes destacando a agilidade e o recebimento antecipado [R1], [R2].
* **Recomendação e intenção de recompra**: Representa 20,6% das avaliações (5.706 menções no tema), onde os compradores expressam explicitamente que voltariam a comprar na loja [R3], [R4].
* **Boa qualidade do produto**: Presente em 18,8% das avaliações (5.208 menções no tema), com relatos que elogiam o padrão do produto e a conformidade com as especificações ou fotos anunciadas [R5], [R6].
* **Preço / custo-benefício**: Representa 2,9% das avaliações (814 menções no tema), com clientes pontuando positivamente a relação entre o custo e o benefício obtido [R7], [R8].

Limitações: Análise restrita à amostra filtrada de notas 4–5 e às contagens por palavras-chave dos temas fornecidos.
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
Com base na população de avaliações negativas (notas 1–2), os principais padrões de insatisfação concentram-se em problemas logísticos de entrega, envio de itens divergentes do anunciado e entraves no pós-venda para trocas ou cancelamentos.

**Principais padrões identificados:**

- **Não recebimento do produto e falha de comunicação:** É o padrão de maior frequência nas contagens por palavras-chave sobre a base filtrada, representando 31,9% das avaliações (3.454 casos). Os clientes relatam a não entrega do pedido e a ausência de notificações ou avisos por parte do vendedor [R1], [R2].
- **Dificuldades com trocas, cancelamentos e avarias:** Representa 14,1% dos registros (1.531 casos). Há relatos de clientes solicitando o cancelamento do pedido [R3], bem como relatos de recusa na troca de produtos que chegaram danificados, forçando o cliente a cancelar a compra [R4].
- **Atraso na entrega:** Corresponde a 14,0% das reclamações (1.518 casos), onde os clientes expressam insatisfação especificamente com a demora na chegada da mercadoria [R5], [R6].
- **Envio de produto errado ou diferente do anunciado:** Presente em 9,0% das avaliações (972 casos). Os consumidores indicam o recebimento de itens incorretos ou incompatíveis com as especificações contidas no anúncio [R7], [R8].

Limitações: Análise baseada estritamente em uma amostra de 8 avaliações e nas estatísticas por palavras-chave da população filtrada fornecida.
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
As avaliações de clientes indicam problemas recorrentes com o prazo de entrega, divididos entre o descumprimento da data prevista e a insatisfação com prazos estimativos excessivamente longos. Na população filtrada (notas 1 a 3), a categoria "Atraso / demora na entrega" representa 13,1% das avaliações (1.896 casos).

Principais pontos observados nas evidências:

* **Atrasos e descumprimento da data de entrega:** Diversos clientes relatam que a entrega atrasou em relação à data estipulada ou que o prazo expirou sem a chegada do produto [R2], [R4], [R5], [R7], [R10].
* **Prazos de entrega excessivamente extensos:** Mesmo em pedidos entregues dentro da estimativa original, há insatisfações recorrentes quanto à duração prolongada do prazo oferecido [R3], [R6], [R8], [R9].
* **Menção genérica ao prazo como ponto negativo:** Registros em que o prazo de entrega é apontado como justificativa para notas baixas [R1].

Limitações: Análise restrita às 10 avaliações amostradas e estatísticas de palavras-chave da base filtrada (notas 1–3).
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
As avaliações mostram opiniões divididas sobre a qualidade, com registros tanto de satisfação com materiais e acabamentos quanto de relatos de fragilidade, defeitos de fabricação e divergência em relação às imagens do site [R1] [R2] [R3] [R4] [R5] [R6] [R7] [R8] [R9] [R10]. Estatisticamente, a boa qualidade do produto aparece em 5.510 menções (13,1% da base total), enquanto a qualidade abaixo do esperado soma 1.164 menções (2,8%) e o tema de defeito/produto quebrado possui 701 menções nas avaliações do assunto.

* **Satisfação com o padrão de qualidade:** Clientes destacam produtos originais, com bom acabamento, materiais de qualidade e dentro dos padrões esperados [R4] [R5] [R6] [R8] [R10].
* **Problemas de fragilidade e baixa qualidade:** Vários clientes relatam que os produtos são frágeis, de qualidade muito baixa ou que deixam a desejar [R1] [R2] [R3].
* **Itens quebrados e com defeito:** Há registros de mercadorias que chegaram quebradas ou apresentaram defeitos de fabricação, como problemas em mosqueteiros, cronômetros e botões [R2] [R3] [R7].
* **Expectativa desalinhada com o site:** Algumas avaliações apontam insatisfação porque o produto recebido aparentava ter melhor qualidade de material e acabamento nas fotos do site [R9].

Limitações: Análise baseada em uma amostra de 10 avaliações detalhadas e em estatísticas de palavras-chave da base filtrada.
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
Os clientes da categoria de beleza e saúde elogiam principalmente a agilidade na entrega e a boa qualidade dos produtos, fatores que impulsionam a confiança e a intenção de comprar novamente na loja. Com base nas estatísticas por palavras-chave na população filtrada (2.416 avaliações de nota 4 e 5), o tema mais recorrente é a entrega rápida (32,2%), seguido pela recomendação da loja (21,9%) e qualidade do produto (17,1%).

**Principais pontos elogiados:**

* **Entrega rápida e dentro do prazo:** É o ponto mais destacado, somando 777 menções (32,2%) nas estatísticas da base. Os clientes ressaltam o recebimento dos produtos antes da data prevista e o cumprimento das datas combinadas [R1], [R2], [R3], [R7], [R8].
* **Qualidade e ergonomia do produto:** A boa qualidade dos itens é mencionada em 413 avaliações (17,1%), com elogios adicionais à facilidade de uso, conforto e ergonomia [R2], [R5], [R6], [R8].
* **Confiança e intenção de recompra:** Representando 528 menções (21,9%) nas estatísticas, a pontualidade e o cumprimento do combinado geram forte intenção dos clientes em comprar novamente e recomendar a loja [R3], [R4].
* **Embalagem e proteção:** Com 58 menções (2,4%) nas estatísticas, os consumidores também elogiam o recebimento de mercadorias bem protegidas e com embalagens em perfeito estado [R7], [R8].

Limitações: A análise baseia-se em uma amostra filtrada apenas com avaliações positivas (notas 4 e 5) e a frequência dos temas é derivada de contagens por palavras-chave.
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
Com base na amostra de avaliações com nota baixa (1–2), os principais problemas relatados envolvem falhas na entrega, dificuldades com cancelamentos ou devoluções e recebimento de produtos incorretos ou com defeito.

* **Produto não recebido ou atrasado:** Há relatos de itens que não foram entregues [R1] [R2] e de atrasos significativos na entrega (como 12 e 14 dias) [R2] [R5] [R6]. Estatisticamente, "Produto não recebido" é o tema mais frequente, presente em 31,9% da base filtrada (3454 menções), seguido por "Atraso / demora na entrega" com 14,0% (1518 menções).
* **Problemas com troca, devolução e cancelamento:** Clientes relatam recusa no cancelamento mesmo antes da emissão da nota fiscal [R3] e problemas relacionados a devoluções [R4]. O tema representa 14,1% das menções (1531 ocorrências).
* **Produto errado, com defeito ou baixa qualidade:** Há menções de recebimento de itens diferentes do anunciado [R7], produtos que marcam errado [R8] e itens de baixa qualidade que apresentam problemas logo no primeiro dia de uso [R4]. O tema de produtos errados aparece em 9,0% dos casos (972 menções).

Limitações: A análise baseia-se em uma amostra limitada de avaliações textuais complementada por estatísticas de palavras-chave da base filtrada.
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
Nas avaliações de pedidos filtrados por atraso na entrega, o tema principal é a insatisfação com a demora e o não recebimento do produto até a data da avaliação, além de impactos na nota concedida pelo consumidor.

**Principais pontos identificados:**

*   **Reclamações diretas sobre atraso e produto não recebido:** Os consumidores relatam frequentemente a ocorrência e o absurdo do atraso [R2] [R3] [R5] [R6] [R8] [R9] [R10]. Nas estatísticas por palavras-chave na base filtrada (3.809 avaliações), "Produto não recebido" representa 45,9% (1.749 avaliações) e "Atraso / demora na entrega" representa 26,1% (994 avaliações).
*   **Impacto na avaliação do cliente:** O atraso é citado diretamente como motivo para penalizar a nota do pedido [R1], havendo também relato de ser a primeira vez que o cliente passa por essa situação na loja [R4].
*   **Responsabilização de terceiros:** Existe menção explicitando que o motivo do atraso no envio do produto foi dos Correios [R7].
*   **Outros temas presentes nas estatísticas da base filtrada:** A contagem por palavras-chave também registra incidências de temas como "Recomenda a loja / compraria novamente" (7,2% / 276 avaliações), "Troca, devolução, cancelamento ou reembolso" (5,8% / 222 avaliações), "Boa qualidade do produto" (3,2% / 122 avaliações), "Atendimento / comunicação com vendedor" (2,4% / 91 avaliações) e "Produto errado / diferente do anunciado" (1,7% / 63 avaliações).

Limitações: A análise textual detalhada baseia-se em uma amostra de 10 avaliações do início de 2018, enquanto os dados agregados derivam unicamente da contagem por palavras-chave do filtro aplicado.
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
Os clientes reclamam principalmente da falta de comunicação e demora no retorno por parte dos vendedores, além da recusa não justificada de suporte em casos de problemas com o produto. Nas estatísticas da base que menciona o assunto, o tema "Atendimento / comunicação com vendedor" foi registrado em 149 avaliações (6,4%).

* **Demora e falta de comunicação:** Os consumidores relatam demora no atendimento e no retorno de mensagens [R7] [R10], falta de contato do vendedor para informar sobre cancelamento de vendas [R3] e dificuldade para encontrar canais de contato direto [R1].
* **Recusa imotivada de devolução e suporte:** Há relato de solicitação de devolução cancelada pelo vendedor sem explicação ou atendimento ao cliente, resultando em prejuízo ao comprador [R5].
* **Classificação geral negativa:** O atendimento é classificado diretamente como "péssimo" em múltiplos relatos [R3] [R6].

Limitações: A amostra individual é reduzida e inclui avaliações com notas baixas (1 a 3) que apresentam elogios pontuais ao atendimento [R2] [R4] [R8] [R9].
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
Os clientes reclamam com frequência de receber produtos diferentes do anunciado, sendo este o quarto tema mais recorrente nas estatísticas gerais (presente em 1.173 avaliações ou 8,1% da base filtrada). Vários relatos apontam discrepâncias em relação às fotos, cores, especificações técnicas e qualidade dos itens recebidos [R1] [R2] [R3] [R4] [R6] [R7] [R9].

* **Divergência de fotos, imagens e cores:** Os clientes relatam que o produto recebido não confere com as fotos do anúncio [R1] [R6] ou que receberam cores diferentes da solicitada e pagada [R2].
* **Especificações e materiais incorretos:** Há reclamações de que as especificações anunciadas não conferem [R3], como a composição do tecido (ex: 80% algodão em vez de 100%) [R7] e materiais com tamanhos ou lados diferentes do prometido [R9].
* **Baixa qualidade em relação ao anunciado:** Clientes apontam que, além de o item ser diferente do divulgado, ele apresenta qualidade inferior [R3] [R4].
* **Solicitação de devolução e problemas de atendimento:** O recebimento de itens divergentes ou com defeito gera pedidos de devolução [R6] e reclamações sobre a falta de solução rápida por parte da empresa ou parceiros [R8].

Limitações: Análise baseada em uma amostra qualitativa restrita de 10 avaliações detalhadas [R1-R10] e nas estatísticas de temas da população filtrada de 14.438 avaliações.
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
Os clientes apontam tanto problemas com embalagens amassadas ou deterioradas quanto avaliam positivamente a proteção dos produtos.

* **Embalagens amassadas ou danificadas:** Diversos clientes relatam que receberam os produtos com embalagens amassadas [R1], [R2], [R7], [R9], caixas deterioradas [R4], [R10] e embalagem inadequada que resultou em amassado no produto [R5], além de menção a avaria na embalagem [R3].
* **Avaliações positivas de embalagem:** Por outro lado, há registros de clientes elogiando a ótima embalagem [R8] e, estatisticamente, o tema de embalagem bem feita / bem protegido aparece em 765 menções (40.6% da base de 1.882 avaliações sobre o assunto).
* **Ausência de embalagem:** Há também um registro de produto recebido sem embalagem [R6].

Limitações: Análise baseada em uma amostra de 10 avaliações qualitativas específicas sobre o tema e nas estatísticas agregadas fornecidas.
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


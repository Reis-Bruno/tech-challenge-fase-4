# Roteiro do vídeo, slide a slide

Tech Challenge Fase 4 — Voice of Customer Intelligence com RAG · Bruno Reis e Lucas Sucupira

Duração total: 7 minutos. O texto entre aspas de cada slide é a fala sugerida.

## Antes de gravar

- Streamlit aberto (`streamlit run app/streamlit_app.py`), com o índice fastembed construído e o `.env` contendo `GEMINI_API_KEY=`.
- Faça uma pergunta de aquecimento: a primeira consulta carrega os índices e demora mais.
- Na barra lateral, Gerador (LLM) em `gemini` e “Inferir filtros a partir da pergunta” ligado.
- Zoom do navegador entre 110% e 125%.

## 1. Capa (0:00–0:15)

**Item do enunciado:** —  
**Na tela:** Título, nomes dos autores e link do repositório.

“Olá, nós somos Bruno Reis e Lucas Sucupira. Este é o nosso Tech Challenge da Fase 4: uma solução de Voice of Customer Intelligence baseada em RAG, sobre as avaliações do Brazilian E-Commerce Public Dataset, da Olist. Em sete minutos vamos mostrar o problema, a arquitetura, como a recuperação funciona, uma demonstração e os resultados que medimos.”

## 2. Problema de negócio (0:15–0:50)

**Item do enunciado:** Problema de negócio  
**Na tela:** Notas médias 4,0 / 1,94 / 1,52 e os três casos em que o RAG simples falhou.

“Empresas de e-commerce recebem milhares de avaliações, e os gestores precisam saber o que está por trás das notas. Na própria base da Olist isso aparece claramente: a nota média é 4,0 quando o pedido chega no prazo, cai para 1,94 quando atrasa e para 1,52 quando não é entregue. Mas o motivo está no texto, e ninguém lê 42 mil comentários. Começamos com o RAG mais simples, buscar os comentários mais parecidos e pedir um resumo, e ele falhou em três casos que definiram o projeto: perguntas amplas traziam até “entrega sem problemas” quando perguntávamos pelos principais problemas; perguntas de frequência não se respondem com dez avaliações; e perguntas sem resposta na base eram respondidas assim mesmo.”

## 3. Arquitetura (0:50–1:30)

**Item do enunciado:** Arquitetura proposta  
**Na tela:** Fluxo de indexação e fluxo de consulta, em duas faixas.

“A solução tem duas fases. Na indexação, que roda uma vez, o data_prep lê os CSVs baixados do Kaggle, confere a integridade, limpa e junta os metadados; o modelo de embeddings multilíngue gera os vetores, que vão para o ChromaDB, e em paralelo montamos um índice BM25. Na consulta, cada pergunta vira um plano de consulta, com filtros, intenção e verificação de escopo. O retriever busca as avaliações. Antes de chamar o modelo, verificamos se há pelo menos três evidências com suporte; se não houver, a resposta é uma recusa. Só então o contexto vai para o Gemini, e as citações da resposta são validadas no final.”

## 4. Base de conhecimento (1:30–2:05)

**Item do enunciado:** Estratégia do RAG: preparação da base  
**Na tela:** Funil de 99.224 a 42.114 documentos e as decisões de preparação.

“A base começa com 99.224 avaliações; 42.687 têm texto. Removemos 317 avaliações com review_id repetido e 256 textos sem nenhuma palavra, e chegamos a 42.114 documentos. Cada avaliação é um documento: o maior texto tem uns 230 caracteres, então não faz sentido dividir em trechos. Antes de transformar qualquer coisa, conferimos a integridade: há 3.852 comentários com quebra de linha, e nenhuma nota saiu fora de 1 a 5, o que confirma que o CSV foi lido certo; e 9.803 pedidos têm mais de um item, por isso agregamos a categoria por pedido antes do join, para não duplicar avaliações. A limpeza é leve e preserva negações. Valores ausentes não fazem nenhuma avaliação ser descartada. E cada documento leva metadados: nota, data, situação da entrega, atraso, categoria e UF.”

## 5. Plano de consulta (2:05–2:40)

**Item do enunciado:** Estratégia do RAG: transformação da pergunta  
**Na tela:** Pergunta de exemplo e o plano gerado (intenção, filtros, tipo).

“A estratégia começa antes da busca. Cada pergunta é transformada num plano de consulta. Neste exemplo, “o que os clientes mais elogiam em produtos de beleza?”, o sistema identifica intenção positiva, aplica o filtro de nota 4 e 5 e a categoria beleza_saude, e como não sobra nenhum termo de conteúdo, trata a pergunta como ampla. Perguntas sobre problemas filtram notas 1 a 3; sinônimos do domínio só entram no BM25; e perguntas que pedem faturamento ou número de pedidos já são recusadas aqui, porque esses dados não estão nos textos. Usamos regras, e não um LLM, nesta etapa, porque é ela que decide quais dados chegam ao modelo: assim a mesma pergunta gera sempre o mesmo plano, e a interface mostra cada regra aplicada.”

## 6. Recuperação (2:40–3:15)

**Item do enunciado:** Como ocorre a recuperação  
**Na tela:** Os dois caminhos: pergunta focada e pergunta ampla.

“A recuperação tem dois caminhos. Numa pergunta focada, como “o que relatam sobre a entrega?”, fazemos busca vetorial e BM25 ao mesmo tempo, 60 candidatos cada, já filtrados por metadados, e juntamos as duas listas por RRF, que usa só as posições. Depois verificamos o suporte: a avaliação precisa ter um termo de conteúdo da pergunta ou similaridade acima do limiar. Reordenamos pela cobertura dos termos ponderada por IDF e escolhemos dez evidências com MMR, para não repetir avaliações quase iguais. Numa pergunta ampla, a busca por similaridade não funciona, como vimos. Então contamos os temas na população filtrada, pegamos os quatro mais frequentes e escolhemos duas evidências de cada um. Essa contagem também vai para o modelo: é ela que permite falar de frequência.”

## 7. Evidências e recusa (3:15–3:45)

**Item do enunciado:** Evidências; perguntas sem evidência suficiente  
**Na tela:** Evidência como chega ao modelo e os três casos de recusa.

“Cada evidência chega ao modelo numerada e com seus metadados, como esta: nota 3, entregue com nove dias de atraso. Assim o modelo consegue relacionar o relato com o que aconteceu de fato. O prompt exige citar a evidência em cada afirmação, e depois da geração nós validamos: citação para evidência que não existe é removida. Para as perguntas sem evidência suficiente, a decisão é tomada antes de chamar o modelo. Se a pergunta pede dados que não estão nos textos, se é de fora do domínio ou se há menos de três avaliações com suporte, a resposta é uma recusa explicada. Fizemos assim porque, só com instrução no prompt, o modelo tende a responder mesmo sem base.”

## 8. Demonstração (3:45–5:15)

**Item do enunciado:** Demonstração prática; exemplos de perguntas; evidências recuperadas  
**Na tela:** Tela do Streamlit.

Troque para a tela do Streamlit. As quatro perguntas estão no expansor **Perguntas de exemplo**:
clique na pergunta e depois em **Perguntar**. Cada resposta leva cerca de 12 s; use esse tempo
para comentar a tela.

**1. Pergunta ampla (cerca de 25 s).** Clique em “Quais são os principais problemas relatados
pelos clientes em suas avaliações?”.

- Mostrar: Modo = amplo; 14.438 avaliações na população filtrada; 8 evidências; o gráfico de
  temas (produto não recebido 26,6%, atraso 13,1%); uma citação da resposta, como [R1], e o
  cartão da evidência correspondente.
- Falar: “Ela não tem um assunto específico, então o sistema filtrou as notas de 1 a 3, contou
  os temas e buscou duas evidências por tema. Os percentuais vêm da contagem sobre as 14 mil
  avaliações, não das oito evidências.”

**2. Pergunta focada (cerca de 30 s).** Clique em “O que os clientes relatam sobre problemas
relacionados à entrega?”.

- Mostrar: Modo = focado; 10 evidências; num cartão, a situação da entrega e o atraso. Abrir
  **🔎 Rastreamento do pipeline**: as regras aplicadas, os candidatos da busca vetorial e do
  BM25 e o contexto enviado ao modelo.
- Falar: “Aqui dá para ver cada etapa: as regras que transformaram a pergunta, a busca híbrida e
  exatamente o que foi enviado ao Gemini.”

**3. Metadados (cerca de 15 s).** Clique em “O que os clientes mais elogiam em produtos de
beleza?”.

- Mostrar: 2.416 avaliações na população filtrada; todos os cartões com 4 ou 5 estrelas e
  categoria beleza_saude.
- Falar: “O filtro de categoria e de nota entra na própria busca, então nenhuma avaliação
  negativa aparece.”

**4. Recusa (cerca de 15 s).** Clique em “Qual foi o faturamento da Olist em 2018?”.

- Mostrar: a caixa “Sem evidências suficientes”, com o motivo, e Gerador = guardrail.
- Falar: “Faturamento não está nos textos das avaliações, então o sistema recusa antes de chamar
  o Gemini.” Se sobrar tempo, mostrar também “Qual a capital da França?”.

Se aparecer o aviso “falha ao chamar o LLM”, diga que a interface caiu para o modo extrativo e
siga: as evidências, os filtros e a recusa continuam funcionando.

## 9. Ablação (5:15–5:55)

**Item do enunciado:** Desafios e decisões técnicas (justificativa medida)  
**Na tela:** Tabela de ablação.

“Para justificar as decisões, fizemos um estudo de ablação: começamos com a busca vetorial pura e ligamos um componente por vez, em 18 perguntas, 12 que devem ser respondidas e 6 que devem ser recusadas. Os filtros de metadados levam a polaridade a 1,00: sem eles, um quarto das evidências tinha a nota errada para a pergunta. A verificação de suporte é o que faz o sistema recusar as quatro perguntas de fora do domínio. E a decomposição por tema dá o maior ganho de precisão, de 0,82 para 0,93. Um resultado que não esperávamos: o BM25 sozinho teve precisão maior que a busca híbrida, 0,79 contra 0,75. A híbrida só ganhou em polaridade. Então não podemos afirmar que ela é melhor; parte disso pode vir da métrica, que é léxica.”

## 10. Avaliação de ponta a ponta (5:55–6:15)

**Item do enunciado:** Evidências e resultados  
**Na tela:** Quatro números e um trecho de resposta gerada.

“Na avaliação completa, com o Gemini gerando as respostas, o sistema acertou as 18 decisões entre responder e recusar, com precisão das evidências de 0,93, e nenhuma das 12 respostas teve citação inválida ou ficou sem citação. Cada resposta leva cerca de 12 segundos, quase tudo esperando o Gemini. No trecho de resposta, os percentuais vêm da contagem de temas sobre a base filtrada, não das dez evidências: é isso que permite falar de frequência com base nos dados.”

## 11. Desafios e decisões (6:15–6:40)

**Item do enunciado:** Principais desafios e decisões técnicas  
**Na tela:** Tabela de problemas encontrados e decisões.

“Quase todo mecanismo do projeto nasceu de um erro que apareceu ao ler os resultados. A decomposição por tema veio de “entrega sem problemas” aparecendo como problema. A cobertura por IDF veio de uma pergunta sobre bolo de chocolate sendo aceita, porque muitas avaliações têm o verbo “fazer”. E um número nos chamou atenção: 45,9% das avaliações de pedidos que foram entregues com atraso diziam “não recebi”. Muitos clientes avaliam antes de o pedido chegar, então renomeamos o tema para deixar isso claro. As escolhas de tecnologia seguem a mesma lógica: modelo multilíngue que roda em CPU, ChromaDB porque filtra metadados na própria busca, e temas por palavras-chave porque a contagem é reproduzível.”

## 12. Limitações (6:40–7:00)

**Item do enunciado:** —  
**Na tela:** Três limitações e o link do repositório.

“Para fechar, o que ainda não dá para afirmar. A avaliação tem 18 perguntas escritas por nós e usadas para ajustar regras, então os números estão otimistas; o próximo passo é testar com perguntas de outras pessoas e rotulagem humana. A vantagem da busca híbrida sobre o BM25 não se confirmou. E a contagem de temas cobre cerca de 61% das avaliações, então os percentuais são um piso. O código, as instruções e todos os resultados estão no repositório. Obrigado.”

## Se passar do tempo

Encurte as falas dos slides 4 e 11; são as que menos dependem de demonstração.

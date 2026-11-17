# Roteiro do vídeo, slide a slide

Voice of Customer Intelligence com RAG · Bruno Reis e Lucas Sucupira

Duração prevista: cerca de 6 minutos e 50 segundos. O texto entre aspas é a fala
sugerida; não precisa ler palavra por palavra.

## Antes de gravar

- Streamlit aberto, índice fastembed pronto e `GEMINI_API_KEY=` no `.env`.
- Uma pergunta de aquecimento antes de gravar (a primeira demora mais).
- Zoom do navegador entre 110% e 125%.

## 1. Capa (0:00–0:08)

*Na tela:* Título e nomes dos autores.

“Oi, nós somos o Bruno Reis e o Lucas Sucupira, e esse é o nosso RAG sobre as avaliações da Olist.”

## 2. Problema de negócio (0:08–0:58)

*Na tela:* Notas médias 4,0 / 1,94 / 1,52 e os três casos em que o RAG simples falhou.

“Empresas de e-commerce recebem milhares de avaliações, e os gestores precisam saber o que está por trás das notas. Na própria base da Olist isso aparece claramente: a nota média é 4,0 quando o pedido chega no prazo, cai para 1,94 quando atrasa e para 1,52 quando não é entregue. Mas o motivo está no texto, e ninguém lê 42 mil comentários. Começamos com o RAG mais simples, buscar os comentários mais parecidos e pedir um resumo, e ele falhou em três casos que definiram o projeto: perguntas amplas traziam até “entrega sem problemas” quando perguntávamos pelos principais problemas; perguntas de frequência não se respondem com dez avaliações; e perguntas sem resposta na base eram respondidas assim mesmo.”

## 3. Arquitetura (0:58–1:25)

*Na tela:* Fluxo de indexação e fluxo de consulta.

“São duas fases. A indexação roda uma vez: prepara os dados do Kaggle, gera embeddings com um modelo multilíngue e guarda no ChromaDB, junto com um índice BM25. A consulta roda a cada pergunta: monta um plano de consulta, busca as avaliações, confere se há pelo menos três evidências com suporte e só então chama o Gemini, validando as citações no final.”

## 4. Base de conhecimento (1:25–2:00)

*Na tela:* Funil de 99.224 a 42.114 documentos e as decisões de preparação.

“Das 99 mil avaliações, 42 mil têm texto, e cada uma virou um documento: são textos curtos, então não fizemos chunking. Antes de transformar, checamos a integridade: 3.852 comentários têm quebra de linha e nenhuma nota saiu fora de 1 a 5, então o CSV foi lido certo; e como 9.803 pedidos têm vários itens, agregamos a categoria por pedido pra não duplicar avaliações. A limpeza é leve, sem remover negações, e nenhum dado ausente descarta avaliação.”

## 5. Plano de consulta (2:00–2:30)

*Na tela:* Pergunta de exemplo e o plano gerado.

“Antes de buscar, a pergunta vira um plano. Aqui o sistema entende que é elogio, filtra notas 4 e 5 e a categoria beleza. Pergunta sobre problema filtra notas 1 a 3; sinônimos como “prazo” e “atraso” entram só na busca por palavra; e pedidos de faturamento já são recusados nessa etapa. Usamos regras, e não um LLM, pra mesma pergunta gerar sempre o mesmo plano, visível na tela.”

## 6. Recuperação (2:30–3:10)

*Na tela:* Pergunta focada (híbrida, RRF, suporte, IDF, MMR) e pergunta ampla (temas).

“Na pergunta com assunto, rodamos busca vetorial e BM25, 60 candidatos cada, já com os filtros, e juntamos as listas por RRF, que usa só a posição. Uma avaliação só entra se tiver suporte: um termo da pergunta ou similaridade acima do limiar. Depois reordenamos pela cobertura dos termos, ponderada por IDF, e escolhemos dez com MMR, pra não repetir avaliações quase iguais. Na pergunta ampla, contamos 14 temas na população filtrada e pegamos duas avaliações de cada um dos quatro mais frequentes.”

## 7. Evidências e recusa (3:10–3:35)

*Na tela:* Evidência numerada e os três casos de recusa.

“Cada avaliação chega ao modelo numerada e com os dados do pedido, junto com a contagem de temas, e a resposta tem que citar o número da evidência; citação inventada é removida depois. O modelo nem é chamado em três casos: a pergunta pede dados que não estão nos textos, nenhuma avaliação cobre 60% dos termos dela, ou há menos de três evidências com suporte.”

## 8. Demonstração (3:35–5:05)

*Na tela:* Tela do Streamlit.

Troque para o Streamlit. As perguntas estão em **Perguntas de exemplo**: clique na pergunta e
depois em **Perguntar**. Cada resposta leva uns 12 segundos; fale enquanto ela carrega.

**1. “Quais são os principais problemas…” (25 s)**
Mostre o modo amplo, o filtro de notas 1 a 3, o gráfico de temas e uma citação com o cartão da evidência.
“Como a pergunta é ampla, o sistema filtrou as notas baixas, contou os temas e trouxe duas
avaliações de cada um dos quatro principais. Esses percentuais vêm da base inteira, não só
dessas oito avaliações.”

**2. “O que os clientes relatam sobre problemas relacionados à entrega?” (30 s)**
Abra o **Rastreamento do pipeline**: as regras aplicadas, os candidatos da busca vetorial e do
BM25 e o contexto enviado ao modelo.
“Aqui dá pra ver cada etapa: as regras que transformaram a pergunta, a busca híbrida com RRF e
exatamente o que foi pro Gemini.”

**3. “O que os clientes mais elogiam em produtos de beleza?” (15 s)**
Mostre que todas as evidências têm 4 ou 5 estrelas e categoria beleza.
“O filtro de metadados entra na própria busca, então nenhuma avaliação negativa aparece.”

**4. “Qual foi o faturamento da Olist em 2018?” (15 s)**
Mostre a recusa e o gerador “guardrail”.
“Faturamento não está nas avaliações, então o sistema recusa sem nem chamar o modelo.”

Se aparecer o aviso de falha do Gemini, diga que a interface caiu pro modo sem LLM e siga em
frente.

## 9. Ablação (5:05–5:45)

*Na tela:* Tabela de ablação.

“Pra justificar cada peça, ligamos uma por vez e medimos em 18 perguntas. Os filtros levaram a polaridade a 1: sem eles, um quarto das evidências tinha a nota errada. A verificação de suporte fez o sistema recusar as quatro perguntas fora do assunto. E a decomposição por tema subiu a precisão de 0,82 pra 0,93. Uma surpresa: o BM25 sozinho teve precisão maior que a híbrida, 0,79 contra 0,75, então não dá pra afirmar que a híbrida é melhor.”

## 10. Avaliação completa (5:45–6:00)

*Na tela:* Quatro números e um trecho de resposta.

“No teste completo, com o Gemini, o sistema acertou as 18 decisões de responder ou recusar, com precisão de 0,93, e nenhuma resposta citou evidência inexistente.”

## 11. Desafios e decisões (6:00–6:30)

*Na tela:* Problemas encontrados e a estratégia que cada um gerou.

“Quase toda estratégia veio de um erro nos testes. A decomposição por tema veio de “entrega sem problemas” aparecendo como problema. A cobertura por IDF veio de uma pergunta sobre bolo de chocolate sendo aceita, por causa do verbo “fazer”. E quase metade dos pedidos entregues com atraso dizia “não recebi”, porque o cliente avaliava antes da entrega; renomeamos o tema pra deixar isso claro.”

## 12. Limitações (6:30–6:50)

*Na tela:* Limitações e link do repositório.

“As limitações: as 18 perguntas fomos nós que escrevemos, então os números são otimistas; a vantagem da busca híbrida não se confirmou; e a contagem de temas é um piso. Tudo está no repositório. Obrigado!”

## Se passar do tempo

Grave a demonstração separada e corte as esperas do Gemini na edição.

# Roteiro do vídeo, slide a slide

Voice of Customer Intelligence com RAG · Bruno Reis e Lucas Sucupira

Duração prevista: cerca de 6 minutos, com folga para os 7. O texto entre aspas é a fala sugerida;
não precisa ler palavra por palavra.

## Antes de gravar

- Streamlit aberto, índice fastembed pronto e `GEMINI_API_KEY=` no `.env`.
- Uma pergunta de aquecimento antes de gravar (a primeira demora mais).
- Zoom do navegador entre 110% e 125%.

## 1. Capa (0:00–0:10)

*Na tela:* Título e nomes dos autores.

“Oi, nós somos o Bruno Reis e o Lucas Sucupira. Esse é o nosso projeto da Fase 4: um RAG para entender o que os clientes da Olist dizem nas avaliações.”

## 2. Problema de negócio (0:10–0:40)

*Na tela:* Notas médias 4,0 / 1,94 / 1,52 e os três casos em que o RAG simples falhou.

“A nota mostra se o cliente gostou, mas o motivo está no comentário. Olha a diferença: quando o pedido chega no prazo, a nota média é 4; quando atrasa, cai pra menos de 2. Ninguém lê 42 mil comentários, por isso o RAG. A gente começou com a versão mais simples e ela falhou em três coisas: pergunta ampla, pergunta de frequência e pergunta que a base não responde.”

## 3. Arquitetura (0:40–1:10)

*Na tela:* Fluxo de indexação e fluxo de consulta.

“A solução tem duas partes. Uma roda uma vez só: prepara os dados do Kaggle, gera os embeddings e guarda tudo no ChromaDB e num índice BM25. A outra roda a cada pergunta: interpreta a pergunta, busca as avaliações, confere se tem evidência suficiente e só então chama o Gemini.”

## 4. Base de conhecimento (1:10–1:40)

*Na tela:* Funil de 99.224 a 42.114 documentos.

“Das 99 mil avaliações, 42 mil têm texto, e cada uma virou um documento. Os textos são curtos, então não precisou dividir em pedaços. Antes de tudo, a gente conferiu a integridade dos dados, por exemplo pra não duplicar avaliação de pedido com vários itens. E cada documento leva junto nota, data, situação da entrega e categoria.”

## 5. Plano de consulta (1:40–2:05)

*Na tela:* Pergunta de exemplo e o plano gerado.

“Antes de buscar, a pergunta vira um plano. Nesse exemplo, “o que elogiam em produtos de beleza”, o sistema entende que é elogio, filtra notas 4 e 5 e a categoria beleza. A gente usou regras aqui, e não um LLM, pra mesma pergunta gerar sempre o mesmo plano.”

## 6. Recuperação (2:05–2:35)

*Na tela:* Pergunta focada e pergunta ampla.

“A busca tem dois caminhos. Se a pergunta tem um assunto, tipo entrega, a gente junta busca semântica e busca por palavra e escolhe dez avaliações variadas. Se a pergunta é ampla, tipo “quais os principais problemas”, o sistema conta os temas mais comuns e pega exemplos de cada um. Essa contagem também vai pro modelo.”

## 7. Evidências e recusa (2:35–3:00)

*Na tela:* Evidência numerada e os casos de recusa.

“Cada avaliação chega ao modelo numerada e com os dados do pedido, e a resposta tem que citar esse número. Se não tem evidência suficiente, o sistema recusa antes de chamar o Gemini. Fizemos assim porque, só pedindo no prompt, o modelo acaba respondendo mesmo sem base.”

## 8. Demonstração (3:00–4:30)

*Na tela:* Tela do Streamlit.

Troque para o Streamlit. As perguntas estão em **Perguntas de exemplo**: clique na pergunta e
depois em **Perguntar**. Cada resposta leva uns 12 segundos; fale enquanto ela carrega.

**1. “Quais são os principais problemas…” (25 s)**
Mostre o modo amplo, o gráfico de temas e uma citação com o cartão da evidência.
“Como a pergunta é ampla, o sistema filtrou as notas baixas, contou os temas e trouxe exemplos de
cada um. Esses percentuais vêm da base inteira, não só dessas oito avaliações.”

**2. “O que os clientes relatam sobre problemas relacionados à entrega?” (30 s)**
Abra o **Rastreamento do pipeline** e role até o contexto enviado ao modelo.
“Aqui dá pra ver tudo que aconteceu: as regras aplicadas, a busca e exatamente o que foi pro
Gemini.”

**3. “O que os clientes mais elogiam em produtos de beleza?” (15 s)**
Mostre que todas as evidências têm 4 ou 5 estrelas e categoria beleza.
“O filtro entra na própria busca, então nenhuma avaliação negativa aparece.”

**4. “Qual foi o faturamento da Olist em 2018?” (15 s)**
Mostre a recusa e o gerador “guardrail”.
“Faturamento não está nas avaliações, então o sistema recusa sem nem chamar o modelo.”

Se aparecer o aviso de falha do Gemini, diga que a interface caiu pro modo sem LLM e siga em
frente.

## 9. Ablação (4:30–5:05)

*Na tela:* Tabela de ablação.

“Pra saber se cada peça ajudava, a gente ligou uma de cada vez e mediu. Os filtros acertaram a nota das evidências; a verificação de suporte fez o sistema recusar as perguntas fora do assunto; e a separação por tema deu o maior ganho de precisão. Uma surpresa: a busca só por palavra teve precisão maior que a híbrida, então não dá pra dizer que a híbrida é melhor.”

## 10. Avaliação completa (5:05–5:20)

*Na tela:* Quatro números e um trecho de resposta.

“No teste completo, com o Gemini, o sistema acertou as 18 decisões de responder ou recusar, e nenhuma resposta citou evidência que não existia.”

## 11. Desafios (5:20–5:45)

*Na tela:* Problemas encontrados e decisões.

“Quase tudo no projeto veio de um erro que a gente viu nos testes. Uma pergunta sobre bolo de chocolate era aceita, porque várias avaliações têm o verbo “fazer”. E quase metade dos pedidos entregues com atraso dizia “não recebi”: o cliente avaliava antes de o pedido chegar.”

## 12. Limitações (5:45–6:10)

*Na tela:* Limitações e link do repositório.

“Pra fechar, as limitações: as 18 perguntas fomos nós que escrevemos, então os números são otimistas, e falta medir a busca de um jeito que não dependa só de palavras. Tudo está no repositório. Obrigado!”

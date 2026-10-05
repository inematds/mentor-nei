# LIVE： 36 Vídeos por Assunto com Agentes IA no Piloto Automático

- Tipo: video
- Origem: https://www.youtube.com/watch?v=pqa_KO5Wegk
- Arquivo: raw/videos/live-36-videos-por-assunto-com-agentes-ia-no-piloto-automati.txt

## Resumo
Live de bastidores do INEMA VIP. Começa com contexto de mercado (líderes que entendem negócio, processo e pessoas; novos modelos chegando; precificar por resultado) e com as skills de higiene de contexto (session handoff, memory audit, statusline). O núcleo é o INEMA CC Bot: bot de Telegram que valida o pedido, enfileira, e workers disparam agentes com skills. Ele mostra o recurso "promo avatar": um assunto vira 12 textos (um por público), e na versão 2 vira 36 vídeos (alcance, autoridade e promoção para cada público), produzidos de madrugada pela fila. A ideia veio de pedir crítica do próprio prompt ao Claude e ao GPT. Mostra a fila com tempos por etapa, os contratos de falha do loop e um bug encontrado ao vivo. No fim, cria ao vivo uma skill ("vídeo anima") a partir de uma análise de estilo de vídeo feita pelo Gemini. Conclusão: a lógica bot → fila → worker → agente → skill vale para qualquer processo, não só para vídeo, e cada um deve construir o próprio sistema.

## Ideias centrais
- Precificação por valor entregue: "Então não venda horas, venda resultado." (@00:09:13)
- A fila deixa o trabalho rodando de noite: "36 vídeos antes de eu ir dormir e ele" (@01:03:20)
- Worker e agente se diferenciam pelo uso de IA: "programa, mas esse precisa de uma LLM," (@00:49:34)
- O fluxo de um agente é estável mesmo trocando o modelo: "mudar a Iá, pode mudar as coisas, mas o" (@00:50:15)
- Handoff resume o contexto para economizar tokens: "ele vai pegar e ler todo o que que tu" (@00:34:37)
- Sem engenharia de contexto, toda versão nova de modelo quebra a configuração: "vai estragar tudo que você tem antes." (@00:37:59)
- Três tipos de conteúdo: alcance, autoridade e promoção: "temos, o alcance é buscar pessoas que" (@00:57:41)
- IA boa só onde importa (o texto), o resto é worker: "Então ali eu vou usar uma Iaboa e não" (@01:20:26)
- API é cara; prefere a assinatura/copiar-colar: "direto, só que eu não quero gastar. API" (@01:02:35)
- Contratos definem quando o loop considera falha: "ó, sem contrato e arquivo vazio falha," (@01:21:53)
- Não depender de um só modelo: "dependo de nenhum deles. Eu tô ajustando" (@01:27:21)

## Como ele ensina aqui
- Mostra o próprio sistema em produção: a fila, os status, as pastas de output e os canais, com os erros à mostra.
- Melhora o prompt pedindo crítica a dois modelos: "Levei pro Cloud, ele criticou. Levei pro" (@01:06:50). Daí sai o 36 = 12 × 3.
- Testa com um público antes de rodar em todos e corrige o erro na hora (o problema era um ponto no texto): "coisa de manutenção que tu vai testar. E" (@01:08:59).
- Primeiro o fluxo, depois o visual: "não tô preocupado com isso. Eu tô usando" (@01:05:47). Guarda estatística de tempo para otimizar: "né, para treinar, para saber quanto" (@01:15:59).
- Cria uma skill ao vivo a partir de material de referência e diz que ainda precisa validar: "E temos que testar se vai ser aquilo que" (@01:43:05). Insiste em entender o exemplo, não só copiar: "E não só copiam, senão vocês vão ser" (@00:45:20).

## Ligações
- Temas: [[filas-e-workers]], [[fluxos-vs-agentes]], [[producao-de-video-com-ia]], [[contexto-e-memoria]], [[agentes-de-ia]], [[skills]], [[orquestracao-de-modelos]]
- Princípios: [[menor-custo-que-resolve]], [[construir-o-proprio-sistema]], [[medir-antes-de-acreditar]], [[verificar-antes-de-afirmar]], [[falhar-cedo]]
- Métodos: [[pipeline-de-video-por-assunto]], [[live-construindo-ao-vivo]]

# LIVE： INEMACCBOT Fluxos vs Agentes de IA — De US$3 a Zero por Vídeo

- Tipo: video
- Origem: https://www.youtube.com/watch?v=axMCHVuSu0M
- Arquivo: raw/videos/live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero-por-v.txt

## Resumo
Aula-live do curso sobre a arquitetura do INEMA CC Bot: gateway/validador, fila durável em SQLite, workers com controle atômico, roteador que decide entre skill direta, agente com skill ou fluxo multi-etapas, e entrega. O ponto central é fluxo vs agente. O pipeline "promo avatar" feito com agentes custava cerca de US$ 3 por vídeo e levava horas, por causa de releitura de cache e scripts recriados a cada execução. Ele mediu tokens e ferramentas, achou os gargalos e trocou etapas de agente por funções determinísticas (o "estúdio" que pilota o navegador, CTA fixo colado com FFmpeg). O custo caiu para US$ 0,50, depois 0,18, e chegou a zero. Em seguida instala o bot numa VPS limpa ao vivo e depura os caminhos errados no .env até o ping responder. Explica harness vs LLM, a estrutura de "domínios" (flow.json, prompts, templates, CTA, help) e o valor de validar o pedido e recusar cedo.

## Ideias centrais
- Agente tem custo e não é exato; script repete igual: "que vai ser rodado igual sempre. Quando" (@00:06:52)
- Às vezes um fluxo é melhor que um agente: "criar gentes, talvez o melhor era criar" (@00:07:23)
- O cache barato engana quando é relido sem parar: "Eu fiz o sistema, funciona tudo, mas eu" (@00:11:39)
- Resultado da otimização: "virou 50 centavos, virou 18 centavos e" (@00:14:20)
- O caminho foi tornar o processo determinístico: "previsível e não mais com agentes." (@00:14:34)
- O agente serve para construir; depois, o mínimo possível: "criar, para construir e depois no mínimo" (@00:14:40)
- Harness e LLM são coisas diferentes: "Qual é o agente que que roda e qual é a" (@00:45:23)
- O validador recusa o que o sistema não sabe entregar: "ele vai gastar tua máquina, fila e tudo" (@01:23:34)
- Não gerar de novo o que é sempre igual: "fazer um CTA sempre no final se eu já" (@01:24:59)
- O kind fixo (agente ou função) garante o caminho: "Então eu não quero deixar I decidir, eu" (@01:42:40)
- Modo sombra valida tudo sem gastar: "vai testar tudo e não vai gastar nada de" (@01:58:10)

## Como ele ensina aqui
- Mede antes de mudar: tokens de entrada, saída e cache, e quantas vezes cada ferramenta é chamada. "seja, tentei cada um deles medir e aí eu" (@00:12:57)
- Instala do zero numa VPS vazia, ao vivo, e depura diante do público. Corrige o .env.example na origem e dá push: "fonte, senão vai dar problema para todo" (@00:39:00)
- Erra um parâmetro de propósito (ou sem querer) para mostrar a validação: "ter essa visão. Nós temos que errar cedo" (@01:38:48)
- Faz perguntas ao chat (qual o melhor harness?) e compara as opções com uma tabela pedida ao modelo. A conclusão é que o melhor é o que você domina, escolhido pelo custo-benefício.
- Prefere o ambiente mais simples (.env, terminal, nano) para não criar camadas: "tô criando mais uma camada de problema" (@00:28:46). Manda ler a documentação antes: "dar uma lida em todo o documento aqui," (@00:21:10)

## Ligações
- Temas: [[fluxos-vs-agentes]], [[filas-e-workers]], [[custo-de-tokens]], [[orquestracao-de-modelos]], [[infraestrutura-basica]], [[producao-de-video-com-ia]]
- Princípios: [[medir-antes-de-acreditar]], [[menor-custo-que-resolve]], [[falhar-cedo]], [[simplicidade-e-corte]]
- Métodos: [[agente-vira-fluxo-deterministico]], [[depurar-ao-vivo]], [[pipeline-de-video-por-assunto]]

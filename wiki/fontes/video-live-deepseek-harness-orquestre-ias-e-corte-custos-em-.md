# LIVE： DeepSeek Harness - Orquestre IAs e Corte Custos em 95x

- Tipo: video
- Origem: https://www.youtube.com/watch?v=D0n_9orkl4k
- Arquivo: raw/videos/live-deepseek-harness-orquestre-ias-e-corte-custos-em-95x.txt

## Resumo
Live longa sem pauta fixa. Começa com o problema que o Nei não conseguiu resolver na madrugada (timeout ao escalar a integração de música e vídeo no Inema CCBOT) e com uma passada pelas ferramentas dele: InemaVox (dublagem, TTS, transcrição, corte, download, SFX, exposto como API na porta 8000), INEMA IMG, análise de vídeo que gera um prompt por cena e Bench Studio. O tema central é o DeepSeek Harness: um harness open source usado como "guarda-chuva" que orquestra Claude, Codex, DeepSeek e modelos locais (Qwen), cada um no que faz melhor. Ele avisa que é *objeto brilhante* e que o DeepSeek não é modelo de fronteira. Depois faz a conta ao vivo: mede o próprio consumo (cerca de 2,5 bilhões de tokens por semana nos logs do Claude) e calcula quanto isso custaria por API. Conclui que usar a assinatura via SDK (Claude/Codex) nos próprios sistemas sai uns 95x mais barato que a API. Mostra como atualizar um app numa VPS (git pull, npm run build, scripts start/stop/atualizar), conta que mandou o Fable auditar o código do harness e fecha com conselhos de carreira (fundamentos acima de ferramentas, resolver problema de alguém), modelos de vídeo locais (ComfyUI, Wan, LTX, MiniMax H3) e um túnel SSH feito ao vivo para reautenticar o Google.

## Ideias centrais
- O harness é um orquestrador que não descarta os outros modelos: "Harness? Ele vai ser meu guarda-chuva." (@00:28:59). Cada modelo tem sua função: "Quando eu quero fazer trabalhos manuais" / "e tudo pesado, que eu vou usar o depsic." (@00:30:27)
- Hype não é critério: "brilhante. Cuidado para vocês não" (perderem tempo) (@00:25:50). Testar antes de acreditar no modelo: "fronteira, tá? Pode testar isso e botar" (@00:34:45), "na prática, né? ele vai errar muito, ele" (@00:34:48)
- Produtividade antes de trocar de ferramenta: "estar trocando ferramentas toda hora sem" (manter a produtividade) (@00:34:00)
- Assinatura em vez de API: "Enquanto a assinatura for esse volume de" (@00:42:32) tokens, "nós estamos gastando muito pouco." (@00:42:38). Por isso a troca da API pela assinatura via SDK: "pi aqui e botar minha assinatura." (@00:43:24)
- Medir o consumo real, não chutar: "Toda semana, ó, dois a 3 bilhões de" (@00:48:09) tokens. Dá para medir com hooks: "botar um hooks antes de cada uma da" (@00:47:30) execução, ou pelos logs e conferir: "consumi e aí dá para validar, certo? Né?" (@00:47:50). O resultado: "Então isso é muito importante entender o" (SDK) (@00:53:49)
- O objetivo da aplicação é ser menos IA e mais worker determinístico: "nossa missão? A nossa missão é tornar" (@00:44:33) "menos e a possível e mais, né, worker," (@00:44:37)
- Créditos extras ligados estouram a conta: "tá me cobrando R$ 450 que eu esses dias" (@00:45:51)
- Segurança vem de auditar o harness: "Deepsic Harness e mandei o Fable olhar" (@01:04:54); "Por quê? Porque eu já validei" (@01:05:37) "o harness. Quem controla é o Harners," (@01:05:40)
- Fundamentos acima de ferramentas: "um mecânico bom, entenda como funciona o" (motor) (@01:06:47); "fundamentos e constrói as coisas que tu" (quiser) (@01:15:40); "ganha mesmo é quem fizer coisas o dia" (todo) (@01:07:40)
- Fazer funcionar é o difícil: "Então, né? Fazer um sistema é fácil," (@01:17:02) "fazer ele funcionar já é mais difícil." (@01:17:05); o caminho do dinheiro: "dinheiro é você resolver o problema de" (alguém) (@01:35:41)

## Como ele ensina aqui
- Calcula ao vivo com dados dele mesmo: pede ao Claude o consumo da semana nos logs, corrige a conta na hora quando esquece de multiplicar por 4 e chega ao fator de 95x.
- Depura conversando com o chat, com duas telas: "pergunto pro chat. Vai e vem, vai e vem." (@00:58:35). Copia o erro, cola, volta e repete.
- Mostra o procedimento real de atualização na VPS (git pull, npm run build, stop/start) e explica o porquê: "Se você não faz isso, ele vai ficar em" (memória com a versão antiga) (@00:57:13). Empacota o procedimento em scripts .sh para quem chega depois.
- Fala em analogias (carro/Ferrari na fazenda, equipe de cirurgia, mecânico e motor) e manda o aluno saber que a técnica existe, sem decorar: "decor, vai lá pro chat e pede, mas pelo" (menos tu sabe que existe) (@01:49:04).
- Erra ao vivo (túnel SSH, usuário root), corrige e termina em "tem coisa melhor do que a gente testar." (@01:49:36)

## Ligações
- Temas: [[orquestracao-de-modelos]], [[custo-de-tokens]], [[claude-code]], [[infraestrutura-basica]], [[git-e-deploy]], [[llm-local-e-gratis]], [[producao-de-video-com-ia]], [[agentes-de-ia]], [[fluxos-vs-agentes]]
- Princípios: [[medir-antes-de-acreditar]], [[menor-custo-que-resolve]], [[orquestrar-nao-reinventar]], [[fundamentos-antes-de-ferramentas]], [[construir-junto-ao-vivo]], [[verificar-antes-de-afirmar]]
- Métodos: [[live-construindo-ao-vivo]], [[depurar-ao-vivo]], [[medir-consumo-de-tokens-e-comparar-com-api]], [[app-na-vps]]

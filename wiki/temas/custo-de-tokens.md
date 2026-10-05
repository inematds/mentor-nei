# Custo de tokens

- Tipo: tema

## O que ele sabe

Entrada, saída, gravação e leitura de cache; system prompt, lista de skills e memória reenviados a cada chamada; perder o cache encarece; assinatura no uso pleno sai de ~20x a ~95x mais barata que API. Ele faz as contas ao vivo com os próprios logs.

### Por fonte (o que cada lote observou)

- **Custo de tokens, cache e assinatura vs API** — Custo é parte do projeto: perder o prompt cache encarece a próxima entrada; validar custa mais que criar; plataformas (Vercel, Supabase) dão grátis e cobram na escala; assinatura no uso pleno sai ~20x mais barata que API, então trocar por modelo aberto via API raramente compensa.
- **Custo de tokens** — Entrada, saída, gravação e leitura de cache; descrições de skills carregadas em toda sessão; assinatura vs API. Ele faz as contas ao vivo e mostra onde o dinheiro vaza.
- **Custo de tokens: assinatura x API** — Consumo medido em bilhões de tokens por semana. Pela API sairia ~95x mais caro que a assinatura; por isso ele usa o SDK do Claude/Codex nos próprios sistemas e otimiza o fluxo enquanto o subsídio dura.
- **Custo de tokens e janela de contexto** — A cada comando o modelo recebe de novo o system prompt, a lista de skills e a memória carregada; por isso contexto alto e skills globais demais custam caro. Ele mantém o contexto abaixo de 40%, tira informação da memória para arquivos com ponteiros e mede a queda (74% para 6%).

## Trechos

- "Trocar o /model do turno principal joga fora o cache acumulado." — [[guia-maestro-roteador-triagem-de-modelo-e-esforco-para-ded1b]] `raw/guia/maestro-roteador-triagem-de-modelo-e-esforco-para--ded1bc.md`
- "ele teria que ser 20 vezes mais barato" (@03:04:22) — [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] `raw/videos/inema-vibecode-do-zero-dia-1-infra-git-e-vercel.txt`
- "de graça e se teu negócio crescer você" (@01:15:13) — [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] `raw/videos/inema-vibecode-do-zero-dia-1-infra-git-e-vercel.txt`
- "Geralmente o custo maior não é criar, o" (@00:08:40) — [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] `raw/videos/inema-vibecode-do-zero-dia-1-infra-git-e-vercel.txt`
- "Eu fiz o sistema, funciona tudo, mas eu" (@00:11:39) — [[video-live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero]] `raw/videos/live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero-por-v.txt`
- "está no cloud MD, mas nas descrição das" (@00:09:50) — [[video-live-fim-dos-skills-auditoria-de-ablacao-no-claude-cod]] `raw/videos/live-fim-dos-skills-auditoria-de-ablacao-no-claude-code.txt`
- "Só que eu pago só 200 por mês." (@01:28:20) — [[video-live-fim-dos-skills-auditoria-de-ablacao-no-claude-cod]] `raw/videos/live-fim-dos-skills-auditoria-de-ablacao-no-claude-code.txt`
- "Enquanto a assinatura for esse volume de" (@00:42:32) — [[video-live-deepseek-harness-orquestre-ias-e-corte-custos-em-]] `raw/videos/live-deepseek-harness-orquestre-ias-e-corte-custos-em-95x.txt`
- "pi aqui e botar minha assinatura." (@00:43:24) — [[video-live-deepseek-harness-orquestre-ias-e-corte-custos-em-]] `raw/videos/live-deepseek-harness-orquestre-ias-e-corte-custos-em-95x.txt`
- "eu tenho que pensar que um dia ele vai" (@00:25:08) — [[video-live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia]] `raw/videos/live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia.txt`
- "nunca pode deixar passar de 40%." (@00:13:17) — [[video-live-claude-code-economize-90-dos-tokens-com-3-comando]] `raw/videos/live-claude-code-economize-90-dos-tokens-com-3-comandos.txt`
- "ele vai pegar o system prompt, todas" (@00:28:23) — [[video-live-claude-code-economize-90-dos-tokens-com-3-comando]] `raw/videos/live-claude-code-economize-90-dos-tokens-com-3-comandos.txt`
- "Então, se a informação já tá em disco," (@00:28:13) — [[video-live-claude-code-economize-90-dos-tokens-com-3-comando]] `raw/videos/live-claude-code-economize-90-dos-tokens-com-3-comandos.txt`
- "carregado o tempo todo. A lista sozinha," (@00:32:54) — [[video-live-claude-code-economize-90-dos-tokens-com-3-comando]] `raw/videos/live-claude-code-economize-90-dos-tokens-com-3-comandos.txt`
- "certo? Eu tenho que diminuir o cloud MD" (@00:31:11) — [[video-live-100-videosdia-com-ia-agentes-metodos-e-escala-rea]] `raw/videos/live-100-videosdia-com-ia-agentes-metodos-e-escala-real.txt`

## Fontes

- [[guia-execucao-longa-agentes-que-trabalham-horas-e-dias-b4357]] — Execução Longa — agentes que trabalham horas e dias sem perder o rumo
- [[guia-maestro-roteador-triagem-de-modelo-e-esforco-para-ded1b]] — maestro-roteador — triagem de modelo e esforço para Claude Code
- [[guia-musicavideo-musica-capa-e-clipe-a-partir-de-uma-fr-b4bc]] — musicavideo — música, capa e clipe a partir de uma frase
- [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] — INEMA  VibeCode do Zero - Dia 1 - Infra Git e Vercel
- [[video-inema-vibecode-do-zero-dia-3-basico-de-infra]] — INEMA  VibeCode do Zero - Dia 3 -  Basico de Infra
- [[video-live-100-videosdia-com-ia-agentes-metodos-e-escala-rea]] — LIVE： 100 Vídeos⧸Dia com IA — Agentes, Métodos e Escala Real
- [[video-live-bench-studio-com-81-modelos-de-ia-instalacao-do-z]] — LIVE： Bench Studio com 81 Modelos de IA - Instalação do Zero
- [[video-live-claude-code-economize-90-dos-tokens-com-3-comando]] — LIVE： Claude Code - Economize 90% dos Tokens com 3 Comandos
- [[video-live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia]] — LIVE： De Prompt a Grafo — A Nova Era dos Agentes de IA
- [[video-live-deepseek-harness-orquestre-ias-e-corte-custos-em-]] — LIVE： DeepSeek Harness - Orquestre IAs e Corte Custos em 95x
- [[video-live-fim-dos-skills-auditoria-de-ablacao-no-claude-cod]] — LIVE： Fim dos Skills？ Auditoria de Ablação no Claude Code
- [[video-live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero]] — LIVE： INEMACCBOT Fluxos vs Agentes de IA — De US$3 a Zero por Vídeo
- [[video-live-web-mcp-seu-site-esta-pronto-para-os-agentes]] — LIVE： Web MCP - Seu Site Está Pronto para os Agentes？
- [[video-transcript]] — Agentes com LLM grátis (live)

## Relacionados

[[menor-custo-que-resolve]], [[medir-antes-de-acreditar]], [[verificar-antes-de-afirmar]], [[git-e-deploy]], [[live-construindo-ao-vivo]], [[orquestracao-de-modelos]]

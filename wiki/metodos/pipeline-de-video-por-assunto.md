# Pipeline de vídeo por assunto

- Tipo: metodo

## O que é

Uma ideia vira dezenas de vídeos em etapas encadeáveis, com portões humanos (aprovar texto, aprovar fase) e QA medido antes de gastar ou publicar.

## Passos

### Pipeline de short por assunto (MakeShorts)

1. Roteiro: ~75 palavras, gancho em 3 s, fatos de fonte oficial, 3 versões para escolher
2. Voz/rosto: gravação humana, voz local ou API, ou avatar HeyGen
3. B-roll real do site/GitHub
4. Edição 9:16 (visual em cima, rosto embaixo, legenda palavra a palavra, punch-in, SFX)
5. QA com qa_short.py (duração, 1080x1920, loudness, gancho visual, hashtags, CTA); exit 1 reprova
6. Legenda + até 5 hashtags + rótulo de IA; agendar no Metricool só após confirmação
7. Funil: CTA comenta PALAVRA vira DM automática com o link

### Pipeline de vídeo por assunto (promo avatar)

1. Discutir a ideia com a IA até fechar a intenção (sem prompt ainda)
2. Disparar o fluxo com parâmetros (alvo, variante, estúdio, portão/sem portão)
3. Validar parâmetros e recusar cedo se não fecham
4. Gerar roteiros com modelo bom (12 públicos × alcance/autoridade/promoção)
5. Gerar avatar via estúdio (navegador, sem API), baixar e montar reels com template
6. Revisor confere as regras em loop; juntar CTA; mover para o destino do canal

### Pipeline de vídeo em escala com portões de aprovação

1. Passar uma ideia ao agente (Telegram)
2. O agente gera roteiros adaptados a N públicos (40+, 60+, criadores, educadores...)
3. Portão 1: ler e aprovar o texto
4. Gerar os avatares (HeyGen) e aprovar a fase
5. Montar os reels (imagem, legenda, logotipo) e publicar nos canais
6. Acompanhar o status e testar a quantidade de vídeos por canal

## Exemplos (trechos)

- "Roteiro → Voz ou avatar → B-roll real → Edição 9:16 → QA → Agendar → Funil de DM" — [[guia-makeshorts-fabrica-de-shorts-com-ia-70fe54]] `raw/guia/makeshorts-fabrica-de-shorts-com-ia-70fe54.md`
- "As que custam dinheiro ou publicam sempre pedem sua confirmação." — [[guia-makeshorts-fabrica-de-shorts-com-ia-70fe54]] `raw/guia/makeshorts-fabrica-de-shorts-com-ia-70fe54.md`
- "minha ideia. Veja, nada de promte, nada." (@01:33:50) — [[video-live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero]] `raw/videos/live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero-por-v.txt`
- "E aí entra o revisor, ele olha se" (@01:54:26) — [[video-live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero]] `raw/videos/live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero-por-v.txt`
- "uma pessoa, né? um público alvo. Então" (@01:09:06) — [[video-live-36-videos-por-assunto-com-agentes-ia-no-piloto-au]] `raw/videos/live-36-videos-por-assunto-com-agentes-ia-no-piloto-automati.txt`
- "vídeos. Só que antes ele vai me dar o" (@00:22:46) — [[video-live-100-videosdia-com-ia-agentes-metodos-e-escala-rea]] `raw/videos/live-100-videosdia-com-ia-agentes-metodos-e-escala-real.txt`
- "comandei a Iá e ela tá trabalhando em" (@00:18:06) — [[video-live-100-videosdia-com-ia-agentes-metodos-e-escala-rea]] `raw/videos/live-100-videosdia-com-ia-agentes-metodos-e-escala-real.txt`
- "tenho quatro fases aqui. O texto é, você" (@01:25:58) — [[video-live-empresa-agentica-agentes-de-ia-no-comando-do-nego]] `raw/videos/live-empresa-agentica-agentes-de-ia-no-comando-do-negocio.txt`
- "Gerando roteiro, gerando voz, gerando" (@00:49:33) — [[video-live-web-mcp-seu-site-esta-pronto-para-os-agentes]] `raw/videos/live-web-mcp-seu-site-esta-pronto-para-os-agentes.txt`

## Fontes

- [[guia-makeshorts-fabrica-de-shorts-com-ia-70fe54]] — MakeShorts — Fábrica de Shorts com IA
- [[guia-musicavideo-musica-capa-e-clipe-a-partir-de-uma-fr-b4bc]] — musicavideo — música, capa e clipe a partir de uma frase
- [[video-live-100-videosdia-com-ia-agentes-metodos-e-escala-rea]] — LIVE： 100 Vídeos⧸Dia com IA — Agentes, Métodos e Escala Real
- [[video-live-36-videos-por-assunto-com-agentes-ia-no-piloto-au]] — LIVE： 36 Vídeos por Assunto com Agentes IA no Piloto Automático
- [[video-live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia]] — LIVE： De Prompt a Grafo — A Nova Era dos Agentes de IA
- [[video-live-empresa-agentica-agentes-de-ia-no-comando-do-nego]] — LIVE： Empresa Agêntica - Agentes de IA no Comando do Negócio
- [[video-live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero]] — LIVE： INEMACCBOT Fluxos vs Agentes de IA — De US$3 a Zero por Vídeo
- [[video-live-web-mcp-seu-site-esta-pronto-para-os-agentes]] — LIVE： Web MCP - Seu Site Está Pronto para os Agentes？
- [[video-transcript]] — Agentes com LLM grátis (live)

## Relacionados

[[producao-de-video-com-ia]], [[menor-custo-que-resolve]], [[agentes-de-ia]], [[verificar-antes-de-afirmar]], [[custo-de-tokens]], [[orquestracao-de-modelos]]

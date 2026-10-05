# Orquestração de modelos

- Tipo: tema

## O que ele sabe

Harness (Claude Code, Codex, Hermes, DeepSeek Harness…) não é a LLM. Ele combina modelos por parte do trabalho: forte para planejar e criticar, outro para executar, barato/local para trabalho braçal, sem ficar preso a um fornecedor.

### Por fonte (o que cada lote observou)

- **Orquestração de modelos e esforço** — Escolher modelo e esforço por parte do trabalho: modelo = repertório (o menor que resolve o pior passo), esforço = ambiguidade + custo do erro. Planejar com mais esforço/modelo melhor e validar o plano com outro modelo; implementar com esforço baixo; despachar partes para subagentes.
- **Harness, LLM e orquestração de modelos** — Distingue harness (Claude Code, Codex, Hermes, Pi…) da LLM que é o cérebro. Combina modelos sem depender de um só, usa um modelo forte para planejar/criticar e outro para executar.
- **Orquestração de modelos** — Usar um harness/orquestrador (ex.: DeepSeek Harness) como guarda-chuva que distribui o trabalho: Claude para planejar e escrever, Codex/GPT para código, DeepSeek/modelos locais para trabalho braçal, sem ficar preso a um fornecedor.

## Trechos

- "Migrar não obriga a escolher um só." — [[guia-agente-claude-codex-migrar-do-claude-pro-codex-ou-ac831]] `raw/guia/agente-claude-codex-migrar-do-claude-pro-codex-ou--ac8311.md`
- "A tabela é ponto de partida, não ranking" — [[guia-agente-claude-codex-migrar-do-claude-pro-codex-ou-ac831]] `raw/guia/agente-claude-codex-migrar-do-claude-pro-codex-ou--ac8311.md`
- "Soma ambiguidade + custo do erro." — [[guia-maestro-roteador-triagem-de-modelo-e-esforco-para-ded1b]] `raw/guia/maestro-roteador-triagem-de-modelo-e-esforco-para--ded1bc.md`
- "rotear uma parte pra um modelo menor via subagente NÃO toca o cache principal" — [[guia-maestro-roteador-triagem-de-modelo-e-esforco-para-ded1b]] `raw/guia/maestro-roteador-triagem-de-modelo-e-esforco-para--ded1bc.md`
- "e a implementação pode ser na menor, na" (@02:50:41) — [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] `raw/videos/inema-vibecode-do-zero-dia-1-infra-git-e-vercel.txt`
- "Quando você diminui o esforço, você" (@00:07:11) — [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] `raw/videos/inema-vibecode-do-zero-dia-1-infra-git-e-vercel.txt`
- "Qual é o agente que que roda e qual é a" (@00:45:23) — [[video-live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero]] `raw/videos/live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero-por-v.txt`
- "dependo de nenhum deles. Eu tô ajustando" (@01:27:21) — [[video-live-36-videos-por-assunto-com-agentes-ia-no-piloto-au]] `raw/videos/live-36-videos-por-assunto-com-agentes-ia-no-piloto-automati.txt`
- "melhor de cada um. Usei o Fibo para ele" (@01:03:14) — [[video-live-fim-dos-skills-auditoria-de-ablacao-no-claude-cod]] `raw/videos/live-fim-dos-skills-auditoria-de-ablacao-no-claude-code.txt`
- "Harness? Ele vai ser meu guarda-chuva." (@00:28:59) — [[video-live-deepseek-harness-orquestre-ias-e-corte-custos-em-]] `raw/videos/live-deepseek-harness-orquestre-ias-e-corte-custos-em-95x.txt`
- "e tudo pesado, que eu vou usar o depsic." (@00:30:27) — [[video-live-deepseek-harness-orquestre-ias-e-corte-custos-em-]] `raw/videos/live-deepseek-harness-orquestre-ias-e-corte-custos-em-95x.txt`
- "melhor de cada um, certo? Onde" (@01:59:28) — [[video-live-bench-studio-com-81-modelos-de-ia-instalacao-do-z]] `raw/videos/live-bench-studio-com-81-modelos-de-ia-instalacao-do-zero.txt`

## Fontes

- [[guia-agente-claude-codex-migrar-do-claude-pro-codex-ou-ac831]] — agente-claude-codex — Migrar do Claude pro Codex ou ficar agnóstico
- [[guia-maestro-roteador-triagem-de-modelo-e-esforco-para-ded1b]] — maestro-roteador — triagem de modelo e esforço para Claude Code
- [[guia-musicavideo-musica-capa-e-clipe-a-partir-de-uma-fr-b4bc]] — musicavideo — música, capa e clipe a partir de uma frase
- [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] — INEMA  VibeCode do Zero - Dia 1 - Infra Git e Vercel
- [[video-live-36-videos-por-assunto-com-agentes-ia-no-piloto-au]] — LIVE： 36 Vídeos por Assunto com Agentes IA no Piloto Automático
- [[video-live-bench-studio-com-81-modelos-de-ia-instalacao-do-z]] — LIVE： Bench Studio com 81 Modelos de IA - Instalação do Zero
- [[video-live-deepseek-harness-orquestre-ias-e-corte-custos-em-]] — LIVE： DeepSeek Harness - Orquestre IAs e Corte Custos em 95x
- [[video-live-empresa-agentica-agentes-de-ia-no-comando-do-nego]] — LIVE： Empresa Agêntica - Agentes de IA no Comando do Negócio
- [[video-live-fim-dos-skills-auditoria-de-ablacao-no-claude-cod]] — LIVE： Fim dos Skills？ Auditoria de Ablação no Claude Code
- [[video-live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero]] — LIVE： INEMACCBOT Fluxos vs Agentes de IA — De US$3 a Zero por Vídeo
- [[video-transcript]] — Agentes com LLM grátis (live)

## Relacionados

[[menor-custo-que-resolve]], [[custo-de-tokens]], [[producao-de-video-com-ia]], [[verificar-antes-de-afirmar]], [[live-construindo-ao-vivo]], [[infraestrutura-basica]], [[revisao-cruzada-entre-agentes]]

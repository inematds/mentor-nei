# Contexto e memória

- Tipo: tema

## O que ele sabe

Entregar à IA contexto (pasta doc com referências, prints, planos) em vez de prompt longo; manter o contexto limpo (abaixo de ~40%, handoff, clear, memory audit) e tirar conhecimento da memória para arquivos com ponteiros.

### Por fonte (o que cada lote observou)

- **Núcleo portátil** — O contexto do projeto mora em Markdown comum (AGENTS.md, context/, tasks/current.md, handoffs/) com dono por tipo de informação; o handoff passa o estado entre sessões e entre runtimes, e o prime lê só em modo leitura.
- **Contexto antes do prompt (pasta doc)** — Ele defende entregar à IA um contexto — uma pasta (doc) com referências, prints, links e planos discutidos no chat — em vez de um prompt longo; com isso a instrução fica curta e a IA não chuta. A pasta de contexto é privada e fica fora do git.
- **Contexto e memória** — Manter o contexto limpo (handoff, clear, memory audit) para economizar tokens; usar engenharia de contexto para não quebrar a cada versão nova de modelo; registrar lições na memória do projeto.

## Trechos

- "O núcleo (contexto, decisões, tarefas, skills, handoffs) fica em Markdown comum dentro do projeto." — [[guia-agente-claude-codex-migrar-do-claude-pro-codex-ou-ac831]] `raw/guia/agente-claude-codex-migrar-do-claude-pro-codex-ou--ac8311.md`
- "Fato, preferência, hipótese e decisão são coisas diferentes." — [[guia-agente-claude-codex-migrar-do-claude-pro-codex-ou-ac831]] `raw/guia/agente-claude-codex-migrar-do-claude-pro-codex-ou--ac8311.md`
- "tua intenção, mas ela não pode ser num" (@00:41:08) — [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] `raw/videos/inema-vibecode-do-zero-dia-1-infra-git-e-vercel.txt`
- "Entrega uma pasta cheia de informações" (@00:41:17) — [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] `raw/videos/inema-vibecode-do-zero-dia-1-infra-git-e-vercel.txt`
- "informação. Ele não vai chutar buscando" (@00:36:23) — [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] `raw/videos/inema-vibecode-do-zero-dia-1-infra-git-e-vercel.txt`
- "fácil explicar com uma imagem do que" (@00:40:12) — [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] `raw/videos/inema-vibecode-do-zero-dia-1-infra-git-e-vercel.txt`
- "ele vai pegar e ler todo o que que tu" (@00:34:37) — [[video-live-36-videos-por-assunto-com-agentes-ia-no-piloto-au]] `raw/videos/live-36-videos-por-assunto-com-agentes-ia-no-piloto-automati.txt`
- "vai estragar tudo que você tem antes." (@00:37:59) — [[video-live-36-videos-por-assunto-com-agentes-ia-no-piloto-au]] `raw/videos/live-36-videos-por-assunto-com-agentes-ia-no-piloto-automati.txt`
- "Então, tu tem que se acostumar de limpar" (@00:58:23) — [[video-live-fim-dos-skills-auditoria-de-ablacao-no-claude-cod]] `raw/videos/live-fim-dos-skills-auditoria-de-ablacao-no-claude-code.txt`
- "coisas ele vai aprendendo, os erros que" (@00:52:39) — [[video-live-fim-dos-skills-auditoria-de-ablacao-no-claude-cod]] `raw/videos/live-fim-dos-skills-auditoria-de-ablacao-no-claude-code.txt`

## Fontes

- [[guia-agente-claude-codex-migrar-do-claude-pro-codex-ou-ac831]] — agente-claude-codex — Migrar do Claude pro Codex ou ficar agnóstico
- [[guia-execucao-longa-agentes-que-trabalham-horas-e-dias-b4357]] — Execução Longa — agentes que trabalham horas e dias sem perder o rumo
- [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] — INEMA  VibeCode do Zero - Dia 1 - Infra Git e Vercel
- [[video-live-100-videosdia-com-ia-agentes-metodos-e-escala-rea]] — LIVE： 100 Vídeos⧸Dia com IA — Agentes, Métodos e Escala Real
- [[video-live-36-videos-por-assunto-com-agentes-ia-no-piloto-au]] — LIVE： 36 Vídeos por Assunto com Agentes IA no Piloto Automático
- [[video-live-agentes-workers-filas-e-skills-arquitetura-ia]] — LIVE： Agentes, Workers, Filas e Skills - Arquitetura IA
- [[video-live-claude-code-economize-90-dos-tokens-com-3-comando]] — LIVE： Claude Code - Economize 90% dos Tokens com 3 Comandos
- [[video-live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia]] — LIVE： De Prompt a Grafo — A Nova Era dos Agentes de IA
- [[video-live-fim-dos-skills-auditoria-de-ablacao-no-claude-cod]] — LIVE： Fim dos Skills？ Auditoria de Ablação no Claude Code

## Relacionados

[[menor-custo-que-resolve]], [[verificar-antes-de-afirmar]], [[medir-antes-de-acreditar]], [[custo-de-tokens]], [[skills]], [[live-construindo-ao-vivo]], [[nucleo-portatil-entre-runtimes]], [[higiene-de-contexto]]

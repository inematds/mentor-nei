# Filas e workers

- Tipo: tema

## O que ele sabe

Canal → validador → fila durável (SQLite) → workers → roteador (skill, agente ou fluxo) → entrega. A LLM fica no planejamento e na validação; a execução fica com os workers, inclusive de noite.

### Por fonte (o que cada lote observou)

- **Filas, workers e o INEMA CC Bot** — Arquitetura canal → gateway/validador → fila durável (SQLite) → workers com controle atômico → roteador (skill, agente ou fluxo) → entrega. Permite mandar trabalho e deixar produzindo de noite.
- **Filas, workers e a divisão LLM planeja / worker executa** — Agente é programa com IA, worker é programa sem IA, fila é base de dados e skill é uma receita. Tarefas entram numa fila, workers puxam e disparam agentes; a LLM fica no planejamento e na validação, a execução fica com os workers.

## Trechos

- "fila é tão importante? Porque eu quero" (@00:26:50) — [[video-live-36-videos-por-assunto-com-agentes-ia-no-piloto-au]] `raw/videos/live-36-videos-por-assunto-com-agentes-ia-no-piloto-automati.txt`
- "36 vídeos antes de eu ir dormir e ele" (@01:03:20) — [[video-live-36-videos-por-assunto-com-agentes-ia-no-piloto-au]] `raw/videos/live-36-videos-por-assunto-com-agentes-ia-no-piloto-automati.txt`
- "no meu sistema, vai ser um novo domínio." (@01:22:49) — [[video-live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero]] `raw/videos/live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero-por-v.txt`
- "O worker é um programa sem IA." (@00:34:39) — [[video-live-agentes-workers-filas-e-skills-arquitetura-ia]] `raw/videos/live-agentes-workers-filas-e-skills-arquitetura-ia.txt`
- "A fila é uma base de dados." (@00:34:43) — [[video-live-agentes-workers-filas-e-skills-arquitetura-ia]] `raw/videos/live-agentes-workers-filas-e-skills-arquitetura-ia.txt`
- "execução tu deixa nos worker, tá legal?" (@00:51:08) — [[video-live-claude-code-economize-90-dos-tokens-com-3-comando]] `raw/videos/live-claude-code-economize-90-dos-tokens-com-3-comandos.txt`
- "Além das filas, eu tenho os workers," (@00:23:32) — [[video-live-empresa-agentica-agentes-de-ia-no-comando-do-nego]] `raw/videos/live-empresa-agentica-agentes-de-ia-no-comando-do-negocio.txt`

## Fontes

- [[guia-execucao-longa-agentes-que-trabalham-horas-e-dias-b4357]] — Execução Longa — agentes que trabalham horas e dias sem perder o rumo
- [[video-live-36-videos-por-assunto-com-agentes-ia-no-piloto-au]] — LIVE： 36 Vídeos por Assunto com Agentes IA no Piloto Automático
- [[video-live-agentes-workers-filas-e-skills-arquitetura-ia]] — LIVE： Agentes, Workers, Filas e Skills - Arquitetura IA
- [[video-live-bench-studio-com-81-modelos-de-ia-instalacao-do-z]] — LIVE： Bench Studio com 81 Modelos de IA - Instalação do Zero
- [[video-live-claude-code-economize-90-dos-tokens-com-3-comando]] — LIVE： Claude Code - Economize 90% dos Tokens com 3 Comandos
- [[video-live-empresa-agentica-agentes-de-ia-no-comando-do-nego]] — LIVE： Empresa Agêntica - Agentes de IA no Comando do Negócio
- [[video-live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero]] — LIVE： INEMACCBOT Fluxos vs Agentes de IA — De US$3 a Zero por Vídeo
- [[video-transcript]] — Agentes com LLM grátis (live)

## Relacionados

[[menor-custo-que-resolve]], [[live-construindo-ao-vivo]], [[verificar-antes-de-afirmar]], [[producao-de-video-com-ia]], [[medir-antes-de-acreditar]], [[custo-de-tokens]]

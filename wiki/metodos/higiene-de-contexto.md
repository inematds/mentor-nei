# Higiene de contexto

- Tipo: metodo

## O que é

Rotina para baixar o contexto sem perder decisões: acompanhar o % na statusline, auditar a memória, fechar a fase com session handoff, dar clear e recolar o resumo.

## Passos

### Higiene de contexto por fase

1. Acompanhar o % de contexto pela statusline
2. Ao terminar uma fase ou tarefa perto de 40%, fazer session handoff ou salvar em disco
3. Dar clear, trazer o resumo e seguir na fase seguinte

### Higiene de contexto: status line, memory audit, handoff, clear

1. Acompanhar o % de contexto na status line e agir antes de passar de 40%
2. Rodar /memory-audit para achar redundância e decisões que só existem na conversa
3. Aplicar o plano: tirar conteúdo do CLAUDE.md e da memória para arquivos, deixando ponteiros
4. Ao terminar a etapa (nunca no meio do processamento), rodar /session-handoff para gerar o resumo
5. Copiar o resumo, dar /clear e colar de volta
6. Conferir que o contexto caiu (ex.: de 74% para 6%)
7. Rodar /doctor de tempos em tempos para achar skills sem uso e passá-las de globais para o projeto

## Exemplos (trechos)

- "Mandei limpar o meu contexto, ó. Sempre" (@00:29:26) — [[video-live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia]] `raw/videos/live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia.txt`
- "tiver em 40, vai lá, terminou uma" (@01:11:57) — [[video-live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia]] `raw/videos/live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia.txt`
- "e e o Status Line são três coisas que é" (@00:22:03) — [[video-live-claude-code-economize-90-dos-tokens-com-3-comando]] `raw/videos/live-claude-code-economize-90-dos-tokens-com-3-comandos.txt`
- "mas daí terminou a etapa, você vai" (@00:24:14) — [[video-live-claude-code-economize-90-dos-tokens-com-3-comando]] `raw/videos/live-claude-code-economize-90-dos-tokens-com-3-comandos.txt`
- "ele vai fazer resumo e não comprimir." (@00:27:48) — [[video-live-claude-code-economize-90-dos-tokens-com-3-comando]] `raw/videos/live-claude-code-economize-90-dos-tokens-com-3-comandos.txt`
- "Agora ele gasta só 6%. Se nós pensar que" (@00:29:37) — [[video-live-claude-code-economize-90-dos-tokens-com-3-comando]] `raw/videos/live-claude-code-economize-90-dos-tokens-com-3-comandos.txt`

## Fontes

- [[video-live-claude-code-economize-90-dos-tokens-com-3-comando]] — LIVE： Claude Code - Economize 90% dos Tokens com 3 Comandos
- [[video-live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia]] — LIVE： De Prompt a Grafo — A Nova Era dos Agentes de IA

## Relacionados

[[menor-custo-que-resolve]], [[contexto-e-memoria]], [[execucao-longa]], [[medir-antes-de-acreditar]], [[custo-de-tokens]], [[skills]]

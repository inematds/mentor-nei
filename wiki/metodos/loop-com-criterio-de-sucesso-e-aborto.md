# Loop/goal com critério de sucesso e aborto

- Tipo: metodo

## O que é

Antes de deixar um agente em loop, definir o objetivo, a métrica de sucesso, a métrica de cancelamento e o número máximo de tentativas, com retry curto e /refazer manual.

## Passos

1. Dizer o que quer atingir (/goal)
2. Definir a métrica de sucesso
3. Definir a métrica de cancelamento e o máximo de tentativas (ex.: 3)
4. Em produção: retry de 2 e, se falhar, marcar falha e refazer sob comando

## Exemplos (trechos)

- "quer atingir? Qual é a tua métrica de" (@00:15:54) — [[video-live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia]] `raw/videos/live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia.txt`
- "duas vezes. Se ele não consegue, falha," (@00:45:29) — [[video-live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia]] `raw/videos/live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia.txt`

## Fontes

- [[video-live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia]] — LIVE： De Prompt a Grafo — A Nova Era dos Agentes de IA

## Relacionados

[[fluxos-vs-agentes]], [[contexto-e-memoria]], [[execucao-longa]], [[medir-antes-de-acreditar]], [[custo-de-tokens]], [[pipeline-de-video-por-assunto]]

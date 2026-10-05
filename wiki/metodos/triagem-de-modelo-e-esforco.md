# Triagem de modelo e esforço

- Tipo: metodo

## O que é

Antes de despachar, decidir modelo (o menor que resolve o pior passo) e esforço (ambiguidade + custo do erro) por parte; planejar com modelo forte em esforço alto e executar com outro em esforço médio.

## Passos

### Triagem de modelo e esforço (maestro-roteador)

1. Pular a triagem se a tarefa for mais barata que a própria triagem (anti-overhead)
2. Isolar o pior passo da tarefa
3. Modelo = o menor que resolve bem esse passo
4. Esforço = ambiguidade + custo do erro; risco nomeado de produção/perda = high no mínimo
5. Erro barato e reversível: começar no menor esforço e subir só com evidência
6. Volume: testar 1 item antes do lote
7. Trocar /model do turno principal só em fronteira de trabalho; preferir subagente para rotear partes

### Planejar com um modelo, executar com outro

1. Session handoff + clear para começar com contexto enxuto
2. Modelo forte, esforço alto: analisar e criticar sem alterar
3. Interagir para corrigir premissas erradas do modelo
4. Pedir plano salvo em arquivo para executar em outra sessão
5. Clear, trocar para o modelo executor em esforço médio e executar com commit por tarefa

## Exemplos (trechos)

- "Isola o pior passo → 2. Modelo = o menor que resolve" — [[guia-maestro-roteador-triagem-de-modelo-e-esforco-para-ded1b]] `raw/guia/maestro-roteador-triagem-de-modelo-e-esforco-para--ded1bc.md`
- "Volume: testa 1 item antes do lote" — [[guia-maestro-roteador-triagem-de-modelo-e-esforco-para-ded1b]] `raw/guia/maestro-roteador-triagem-de-modelo-e-esforco-para--ded1bc.md`
- "Se você mesmo nomeou um risco de produção/perda na justificativa, o esforço mínimo é high." — [[guia-maestro-roteador-triagem-de-modelo-e-esforco-para-ded1b]] `raw/guia/maestro-roteador-triagem-de-modelo-e-esforco-para--ded1bc.md`
- "melhor de cada um. Usei o Fibo para ele" (@01:03:14) — [[video-live-fim-dos-skills-auditoria-de-ablacao-no-claude-cod]] `raw/videos/live-fim-dos-skills-auditoria-de-ablacao-no-claude-code.txt`
- "Veja, se a gente não tá interagindo, ele" (@01:02:12) — [[video-live-fim-dos-skills-auditoria-de-ablacao-no-claude-cod]] `raw/videos/live-fim-dos-skills-auditoria-de-ablacao-no-claude-code.txt`
- "Porque ele totalizou um comite para cada" (@00:51:14) — [[video-live-fim-dos-skills-auditoria-de-ablacao-no-claude-cod]] `raw/videos/live-fim-dos-skills-auditoria-de-ablacao-no-claude-code.txt`

## Fontes

- [[guia-maestro-roteador-triagem-de-modelo-e-esforco-para-ded1b]] — maestro-roteador — triagem de modelo e esforço para Claude Code
- [[video-live-fim-dos-skills-auditoria-de-ablacao-no-claude-cod]] — LIVE： Fim dos Skills？ Auditoria de Ablação no Claude Code

## Relacionados

[[orquestracao-de-modelos]], [[medir-antes-de-acreditar]], [[custo-de-tokens]], [[skills]], [[menor-custo-que-resolve]], [[claude-code]]

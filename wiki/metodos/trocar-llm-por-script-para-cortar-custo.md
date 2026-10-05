# Trocar chamadas de LLM por script/rotina para cortar custo

- Tipo: metodo

## O que é

Medir onde o fluxo gasta (comandos por execução, cache), trabalhar fase por fase transformando a parte inteligente em rotina determinística e comparar custo e tempo no fim de cada fase.

## Passos

1. Levantar a tabela de custo por etapa (mensagens, comandos shell, cache)
2. Limpar o contexto ao iniciar cada fase
3. Transformar chamadas repetidas em script, que não gasta LLM
4. Deixar o fluxo mais previsível (tamanhos fixos, sem etapas supérfluas)
5. Pedir a comparação de custo de LLM e tempo da fase e repetir

## Exemplos (trechos)

- "eu transformei toda a parte que era de" (@00:25:21) — [[video-live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia]] `raw/videos/live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia.txt`
- "script que quem chama é um script." (@01:14:28) — [[video-live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia]] `raw/videos/live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia.txt`
- "Então eu trabalho por fase, melhorando" (@00:31:48) — [[video-live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia]] `raw/videos/live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia.txt`

## Fontes

- [[video-live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia]] — LIVE： De Prompt a Grafo — A Nova Era dos Agentes de IA

## Relacionados

[[fluxos-vs-agentes]], [[loop-com-criterio-de-sucesso-e-aborto]], [[contexto-e-memoria]], [[execucao-longa]], [[medir-antes-de-acreditar]], [[custo-de-tokens]]

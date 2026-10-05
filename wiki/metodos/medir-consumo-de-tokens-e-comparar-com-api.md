# Medir consumo de tokens e comparar com a API

- Tipo: metodo

## O que é

Levantar o consumo real (pelos logs ou hooks), projetar para o mês e calcular quanto custaria pela API, para decidir entre assinatura via SDK e API.

## Passos

1. Pedir ao agente o consumo da semana a partir dos logs (ou instrumentar hooks antes e depois de cada execução)
2. Separar input, output, cache lido e cache escrito
3. Multiplicar por 4 para ter o mês
4. Calcular o preço equivalente na API (ex.: Opus) e comparar com a assinatura
5. Validar os números antes de concluir

## Exemplos (trechos)

- "botar um hooks antes de cada uma da" (@00:47:30) — [[video-live-deepseek-harness-orquestre-ias-e-corte-custos-em-]] `raw/videos/live-deepseek-harness-orquestre-ias-e-corte-custos-em-95x.txt`
- "consumi e aí dá para validar, certo? Né?" (@00:47:50) — [[video-live-deepseek-harness-orquestre-ias-e-corte-custos-em-]] `raw/videos/live-deepseek-harness-orquestre-ias-e-corte-custos-em-95x.txt`
- "Toda semana, ó, dois a 3 bilhões de" (@00:48:09) — [[video-live-deepseek-harness-orquestre-ias-e-corte-custos-em-]] `raw/videos/live-deepseek-harness-orquestre-ias-e-corte-custos-em-95x.txt`

## Fontes

- [[video-live-deepseek-harness-orquestre-ias-e-corte-custos-em-]] — LIVE： DeepSeek Harness - Orquestre IAs e Corte Custos em 95x

## Relacionados

[[construir-junto-ao-vivo]], [[orquestracao-de-modelos]], [[fluxos-vs-agentes]], [[medir-antes-de-acreditar]], [[verificar-antes-de-afirmar]], [[claude-code]]

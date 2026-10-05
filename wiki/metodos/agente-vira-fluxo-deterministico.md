# Do agente ao fluxo determinístico (de US$3 a zero)

- Tipo: metodo

## O que é

Primeiro constrói com o agente. Depois mede o custo, acha o gargalo e troca etapas por funções/scripts, deixando a LLM só onde ela cria valor.

## Passos

1. Fazer funcionar com agente
2. Medir tokens (entrada, saída, cache) e chamadas de ferramenta por etapa
3. Identificar o gargalo (ex.: scripts recriados a cada vídeo, navegação por agente)
4. Obrigar o agente a usar scripts prontos e converter etapas repetíveis em funções (kind=função)
5. Reaproveitar partes fixas (CTA) via FFmpeg em vez de gerar de novo
6. Remedir até o custo por unidade cair; LLM só no texto

## Exemplos (trechos)

- "os script a cada vez que ele ia criar um" (@00:15:38) — [[video-live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero]] `raw/videos/live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero-por-v.txt`
- "previsível e não mais com agentes." (@00:14:34) — [[video-live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero]] `raw/videos/live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero-por-v.txt`
- "virou 50 centavos, virou 18 centavos e" (@00:14:20) — [[video-live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero]] `raw/videos/live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero-por-v.txt`

## Fontes

- [[video-live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero]] — LIVE： INEMACCBOT Fluxos vs Agentes de IA — De US$3 a Zero por Vídeo

## Relacionados

[[orquestracao-de-modelos]], [[fluxos-vs-agentes]], [[medir-antes-de-acreditar]], [[custo-de-tokens]], [[falhar-cedo]], [[pipeline-de-video-por-assunto]]

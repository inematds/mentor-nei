# Montar a arquitetura bot → fila → worker → skill

- Tipo: metodo

## O que é

Como ele monta um sistema de agentes que aceita várias tarefas sem travar: entrada única, controlador, fila com as skills permitidas, workers que disparam agentes, crescendo aos poucos.

## Passos

1. Bot recebe a mensagem no canal (Telegram)
2. Controlador classifica e põe na fila já com a lista de skills disponíveis
3. Worker (programa sem IA) puxa da fila e dispara o agente
4. O agente executa só skills aprovadas
5. Começar com uma fila e um worker
6. Depois separar filas (pesada x leve, VIP) conforme a capacidade da máquina

## Exemplos (trechos)

- "certo? Então eu tenho uma entrada geral," (@00:35:13) — [[video-live-agentes-workers-filas-e-skills-arquitetura-ia]] `raw/videos/live-agentes-workers-filas-e-skills-arquitetura-ia.txt`
- "disse? Cria uma fila, cria um worker." (@00:33:39) — [[video-live-agentes-workers-filas-e-skills-arquitetura-ia]] `raw/videos/live-agentes-workers-filas-e-skills-arquitetura-ia.txt`
- "uma fila pro trabalho mais demorado, uma" (@00:33:48) — [[video-live-agentes-workers-filas-e-skills-arquitetura-ia]] `raw/videos/live-agentes-workers-filas-e-skills-arquitetura-ia.txt`

## Fontes

- [[video-live-agentes-workers-filas-e-skills-arquitetura-ia]] — LIVE： Agentes, Workers, Filas e Skills - Arquitetura IA
- [[video-live-empresa-agentica-agentes-de-ia-no-comando-do-nego]] — LIVE： Empresa Agêntica - Agentes de IA no Comando do Negócio

## Relacionados

[[agentes-de-ia]], [[skills]], [[infraestrutura-basica]], [[live-construindo-ao-vivo]], [[filas-e-workers]], [[producao-de-video-com-ia]]

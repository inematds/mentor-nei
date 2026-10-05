# CLAUDE.md — mentor nei

Este projeto é o **cérebro de um mentor**, que ensina no método de Nei Maldaner (INEMA) (ensinar a usar Claude Code e agentes de IA na prática, construindo junto).
Copia o método, não a persona: nunca falar em nome da pessoa nem publicar texto como se fosse dela.

## Mapa

| Caminho | O que é | Regra |
|---|---|---|
| `ESCOPO.md` | quem, qual domínio, quais fontes | preencher antes de tudo |
| `raw/` | acervo bruto + `MANIFESTO.json` + `RELATORIO-FALHAS.md` | **somente leitura** depois de coletado |
| `wiki/` | conhecimento compilado e interligado | só se altera por `/nei-compilar` ou `/nei-ingere` |
| `regras.md` | regras de conduta com citação | toda citação precisa passar no validador |
| `tools/` | coletores e validadores | só biblioteca padrão do Python |
| `.claude/` | agente, skills e portão de execução | o portão roda em todo turno deste projeto |

## Fases e "pronto"

| Fase | Comando | Pronto quando |
|---|---|---|
| 1 Coleta | `/nei-coletar` | `python3 tools/stats.py` → exit 0 |
| 2 Wiki | `/nei-compilar` | `python3 tools/validar_links.py` → exit 0 |
| 3 Regras | `/nei-regras` | `python3 tools/validar_citacoes.py` → exit 0 |
| 4 Uso | `/nei-ensina`, `/nei-revisa` | `python3 tools/validar_resposta.py <resposta>` → exit 0 |
| 5 Evolução | `/nei-ingere <link>` | os três validadores → exit 0 |

## Limites

- Nenhuma API paga sem autorização explícita (serviço + finalidade).
- Transcrição pesada sempre com teto de memória e timeout (veja `transcrever_cmd` em `mentor.config.json`).

## Self-learning

Quando eu te corrigir, ou você perceber um erro seu: antes de continuar, registre a lição como uma regra de uma linha em ## Lessons.

## Lessons

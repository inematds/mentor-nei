# Execução longa com estado em arquivos

- Tipo: metodo

## O que é

Rodar um objetivo longo com goal verificável, estado em arquivos, ciclo testa-registra-commita e parada por estagnação, conferindo e medindo no fim.

## Passos

1. Criar a pasta longrun/<data>-<slug> com os sete arquivos (novo-longrun.sh)
2. Escrever goal.md com critérios nível 3 (comando → saída esperada) e portões humanos
3. Iniciar /goal (interativo) ou loop-longrun.sh (headless, testes congelados)
4. A cada ciclo: ler o estado → próxima ação → executar → testar → salvar estado + commit
5. Parar com o critério atingido, 3 ciclos sem avanço ou teto
6. Conferir à parte e medir com medir-sessao.py, registrando no progress.md

## Exemplos (trechos)

- "Três ciclos sem avanço mensurável = parar e chamar o humano." — [[guia-execucao-longa-agentes-que-trabalham-horas-e-dias-b4357]] `raw/guia/execucao-longa-agentes-que-trabalham-horas-e-dias--b43579.md`
- "Gasto de crédito, API, produção e ações irreversíveis viram portão humano." — [[guia-execucao-longa-agentes-que-trabalham-horas-e-dias-b4357]] `raw/guia/execucao-longa-agentes-que-trabalham-horas-e-dias--b43579.md`
- "Quem decide continuar é o teste" — [[guia-execucao-longa-agentes-que-trabalham-horas-e-dias-b4357]] `raw/guia/execucao-longa-agentes-que-trabalham-horas-e-dias--b43579.md`

## Fontes

- [[guia-execucao-longa-agentes-que-trabalham-horas-e-dias-b4357]] — Execução Longa — agentes que trabalham horas e dias sem perder o rumo

## Relacionados

[[contexto-e-memoria]], [[execucao-longa]], [[medir-antes-de-acreditar]], [[custo-de-tokens]], [[criterio-de-pronto-explicito]], [[filas-e-workers]], [[nucleo-portatil-entre-runtimes]]

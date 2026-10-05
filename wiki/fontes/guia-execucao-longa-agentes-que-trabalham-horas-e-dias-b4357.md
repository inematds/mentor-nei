# Execução Longa — agentes que trabalham horas e dias sem perder o rumo

- Tipo: guia
- Origem: https://inematds.github.io/execucao-longa/guia/
- Arquivo: raw/guia/execucao-longa-agentes-que-trabalham-horas-e-dias--b43579.md

## Resumo
Guia do repositório `execucao-longa`: método e templates para agentes (Codex CLI ou Claude Code com `/goal`) trabalharem horas ou dias sem se perder. A base tem três peças: objetivo verificável (Resultado, Restrições, Verificação), estado em arquivos (goal, plan, state, progress, failures, decisions + canal.md) e tetos e portões humanos. O ciclo é: lê o estado → próxima ação → executa → testa → corrige → salva + commit, e para com três ciclos sem avanço. Há dois caminhos: interativo (com hook que manda reler o estado depois de compactar e avisa nas faixas de 50/70/85% de contexto) e headless (`loop-longrun.sh` com timeout, teto de memória, flock e testes protegidos). Ensina uma escala de critério de pronto (0 a 4, com mínimo no nível 3), o modo fila, cuidados com cache e compactação, e separa o que está confirmado do que não tem fonte. O roadmap mostra fases medidas (piloto concluído em 3 min, medir-sessao lendo 1,8 GB em cerca de 9 s, `recall` com 90 mil trechos).

## Ideias centrais
- O objetivo precisa ser provado por comando: "comandos cuja saída prova que terminou."
- O estado mora em arquivos, não na memória: "o agente relê os arquivos em vez de depender da memória da conversa."
- Portões humanos: "Gasto de crédito, API, produção e ações irreversíveis viram portão humano."
- Parar por estagnação: "Três ciclos sem avanço mensurável = parar e chamar o humano."
- Critério bom: "Bom critério: alguém de fora consegue checar sem confiar no agente, e o agente não consegue cumprir por atalho."
- Critério burlável é armadilha: "Dá para apagar teste ou gerar página vazia."
- Quem julga é o teste: "Quem decide continuar é o teste"
- O problema é a compactação repetida: "Não é o /goal , é a compactação repetida."
- Fila só fecha com prova: "Fechar exige evidência (saída de teste, arquivo, hash de commit)"
- Cache custa: "Perder o cache custa 12,5x a 25x."

## Como ele ensina aqui
- Pede conferência independente no fim: "Confira você mesmo (rode o teste final, veja o hash dos testes)", e medição com `medir-sessao.py` anotada no progress.md.
- Separa evidência de boato: blocos Confirmado, Sem fonte e Não é padrão oficial; ex.: "A sessão de 11 dias / 573 turnos / 1,3 GB não tem fonte pública."
- Ensina com exemplo do critério ruim ao bom (traduzir o guia para inglês: nível 0 → 2 → 3–4).
- Reporta o piloto com números: "concluída no 1º ciclo, em 3 min, e conferida à parte."
- Limita a autonomia: "O agente cria no máximo 5 tarefas por execução".

## Ligações
- Temas: [[execucao-longa]], [[contexto-e-memoria]], [[custo-de-tokens]], [[filas-e-workers]], [[claude-code]]
- Princípios: [[criterio-de-pronto-explicito]], [[verificar-antes-de-afirmar]], [[medir-antes-de-acreditar]]
- Métodos: [[execucao-longa-com-estado-em-arquivos]], [[guia-de-projeto-landing]]

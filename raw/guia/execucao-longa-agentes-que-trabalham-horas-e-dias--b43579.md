# Execução Longa — agentes que trabalham horas e dias sem perder o rumo

Origem: https://inematds.github.io/execucao-longa/guia/

O que é

## Um método + templates para execuções longas

Este repositório junta o material de origem sobre a sessão longa no Codex, uma pesquisa das novidades de jul–out/2026 com fontes, um plano de uso e templates prontos para copiar.

### 🎯 Objetivo verificável

O /goal precisa de Resultado, Restrições e Verificação: comandos cuja saída prova que terminou. Nada de "até ficar bom".

### 🗂️ Estado em arquivos

goal, plan, state, progress, failures e decisions.md guardam a tarefa; canal.md guarda o que a compactação perde (fatos, glossário, armadilhas). Após compactar ou retomar, o agente relê os arquivos em vez de depender da memória da conversa.

### 🛡️ Tetos e portões

Tempo, tokens e memória com limite. Gasto de crédito, API, produção e ações irreversíveis viram portão humano.

Como funciona

## Um ciclo que só para quando o critério é atingido

O agente escolhe sempre a próxima ação útil, testa, registra e continua. Três ciclos sem avanço mensurável = parar e chamar o humano.

Objetivo → Lê estado → Próxima ação → Executa → Testa → Corrige → Salva estado + commit ↺

### Sessão persistente

Continuidade lógica do trabalho: o mesmo objetivo, o mesmo histórico.

### Compactação

Resume o histórico antigo para caber na janela. Muda o prefixo e baixa o cache logo depois — é esperado.

### Prompt cache

Reaproveita o prefixo idêntico. Em sessões contínuas o acerto passa de 95%. Meça cached ÷ input .

Pré-requisitos

## O que você precisa

Um agente de código com modo de objetivo e um projeto com algum teste automático para servir de oráculo.

### Codex CLI

O /goal vive dentro do TUI (não aparece no --help ).

```
# versão recente
codex --version
```

### ou Claude Code

Também tem /goal , além de /loop , background agents e workflows.

```
claude --version
```

### Os templates

Clone este repositório para copiar os arquivos de estado e os prompts.

```
git clone https://github.com/inematds/execucao-longa
```

Guia de uso · passo a passo

## Da primeira linha do goal até "concluído"

Use os templates de templates/ . Cada execução ganha a própria pasta dentro do projeto.

1

### Crie a pasta de estado da execução

Uma pasta por execução, com os sete arquivos (os seis de estado + canal.md).

```
execucao-longa/tools/novo-longrun.sh . meu-objetivo   # cria a pasta com os sete arquivos e data no goal.md

# ou à mão:
mkdir -p longrun/2026-10-01-meu-objetivo
cp execucao-longa/templates/{goal,plan,state,progress,failures,decisions,canal}.md \
   longrun/2026-10-01-meu-objetivo/
```

2

### Escreva o goal.md com critérios verificáveis

Cada critério é um comando e a saída esperada. Liste também os portões humanos.

```
## Critérios de pronto (verificáveis)
- [ ] npm test  → 0 falhas
- [ ] npm run build  → sai com código 0
## Portões humanos (parar e perguntar)
- gasto de crédito / API paga / deploy em produção
```

3

### Inicie o goal

No Codex, cole templates/prompt-goal-codex.md preenchido. Se o objetivo ainda está vago, rode /plan antes.

```
codex
/goal RESULTADO: ... VERIFICAÇÃO: ... ESTADO: longrun/2026-10-01-meu-objetivo/
# no Claude Code: a condição precisa aparecer na saída
/goal a saída do npm test mostra 0 falhas e state.md diz "concluído"
```

4

### Acompanhe sem interromper

Veja o progresso, pause e retome. Use fork para caminhos alternativos.

```
/goals          # lista goals e status
/goal pause     # /goal resume para continuar
/side           # pergunta de status sem parar o trabalho
/fork           # ramifica a sessão
```

5

### Sem interface: o loop headless

Cada ciclo é um codex exec com stdin fechado, timeout, teto de memória e flock. Quem decide continuar é o teste: o loop reverte mexida em teste protegido, faz commit de checkpoint e para por estagnação.

```
# loop.env + prompt.md na pasta (copie de longrun/2026-10-01-medir-sessao/)
execucao-longa/tools/loop-longrun.sh longrun/2026-10-01-meu-objetivo
# para sozinho: CONCLUÍDO, 3 ciclos sem avanço ou teto de ciclos
```

6

### Feche e meça

Confira você mesmo (rode o teste final, veja o hash dos testes) e registre no progress.md o que medir-sessao.py mostra: duração, compactações, tokens, cache e saída de ferramenta.

```
python3 execucao-longa/tools/medir-sessao.py <sessão.jsonl>              # resumo: duração, compactações, cache
python3 execucao-longa/tools/medir-sessao.py <sessão.jsonl> --json --por-turno  # curva por turno
```

Para começar

## Como usar tudo isso

Instale uma vez por máquina. Depois, cada objetivo longo segue um de dois caminhos: interativo (você acompanha) ou headless (roda sozinho).

### 1 · Uma vez por máquina
- Clone o repo em ~/projetos/execucao-longa .
- Cole templates/AGENTS-long-run.md no CLAUDE.md e no AGENTS.md globais.
- No ~/.claude/settings.json , ligue tools/hook-longrun.sh em PreCompact , SessionStart (matcher compact|resume ), PostToolUse e UserPromptSubmit : ele lembra de salvar antes de compactar, manda reler depois e avisa as faixas de contexto (50/70/85%). Ponha "cleanupPeriodDays": 365 para o Claude não apagar as transcrições com 30 dias.
- Ative o vigia: copie tools/systemd/longrun-vigia.* para ~/.config/systemd/user/ e rode systemctl --user enable --now longrun-vigia.timer .
- Nos crons que chamam agente: flock -n + timeout .

### 2A · Interativo — você acompanha
- tools/novo-longrun.sh <projeto> <slug>
- Escreva o goal.md com critérios nível 3.
- /goal no Codex ou no Claude Code com o prompt de templates/ .
- O hook manda reler o estado depois de compactar ou retomar; o vigia avisa se travar.
- No fim: medir-sessao.py e anote no progress.md .

### 2B · Headless — roda sozinho
- tools/novo-longrun.sh <projeto> <slug>
- goal.md + testes congelados (o teste é o juiz).
- prompt.md + loop.env — copie do exemplo longrun/2026-10-01-medir-sessao/ .
- tools/loop-longrun.sh <pasta> (num tmux ou em segundo plano).
- Ele para sozinho: concluído, estagnação ou teto. Confira à parte e meça.

### Manutenção

Para achar algo dito em qualquer sessão (Codex ou Claude): recall "termo" --projeto X --desde AAAA-MM-DD . Alertas do vigia ficam em ~/.local/state/execucao-longa/alertas.log (e no notify-send). tools/arquivar-sessoes.py mostra quanto espaço as sessões antigas ocupam; com --aplicar comprime e com --restaurar devolve. Exemplo completo de execução: longrun/2026-10-01-medir-sessao/ .

Critério de pronto

## Como saber se um critério de sucesso é bom

Bom critério: alguém de fora consegue checar sem confiar no agente, e o agente não consegue cumprir por atalho. Em execução longa, o mínimo é o nível 3.

### 0 · Vago

"Deixar o site bom". Ninguém sabe quando acabou.

### 1 · Subjetivo

"Código revisado e limpo". O agente se autoaprova.

### 2 · Burlável

"0 falhas", "20 páginas". Dá para apagar teste ou gerar página vazia.

### 3 · Protegido ✅

Comando + trava: "0 falhas e ≥ 48 testes e tests/ intocado". Mínimo aceito.

### 4 · Independente

Nível 3 + checagem externa: e2e real, avaliador separado, amostra humana. Quando o erro custa caro.

### 5 perguntas (cada "não" derruba o nível)
- Dá para checar com um comando ( comando → saída esperada )?
- A resposta é sim/não, sem "melhorou"?
- É impossível cumprir sem fazer o trabalho? Se não, falta trava: contagem mínima, arquivo congelado, validador.
- A prova aparece na saída? O avaliador do /goal no Claude só lê a conversa.
- Cobre função (faz o que devia), regressão (não quebrou o resto) e limite (não mexeu onde não devia)?

### Exemplo: "traduzir o guia para inglês"

❌ Nível 0: a frase em si. ⚠️ Nível 2: "existe guia/en/index.html ". ✅ Nível 3–4: mesmas <section id> que o PT, nenhum trecho em PT, links internos respondem 200, captura de tela conferida.

Sinais de critério ruim: "bom", "limpo", "completo"; depende do agente dizer que terminou; só contagem; não diz o que não pode mudar; verificação que leva horas. O templates/goal.md já traz a escala.

Sessões longas · cuidados

## Deterioração de contexto, cache e modo fila

O /goal funciona, mas sessões com muitas compactações perdem o fio. Detalhes e fontes em docs/pesquisa-goal-contexto-fila-2026-10.md .

### 🧠 O /goal deteriora?

Não é o /goal , é a compactação repetida. O objetivo sobrevive, mas se perde o "o que já está feito / o que falta": o agente repete "vou terminar e commitar", reabre trabalho e não converge (issue openai/codex #34095).

### 🛡️ Como evitar

Faixas de contexto, antes do automático (~90–95%): ~50% → anotar no canal.md fatos, aprendizados e armadilhas; ~70% → atualizar o estado e rodar /compact ; ~85% ou 3ª compactação → /session-handoff , sessão nova e /prime . No Claude Code um hook mede a % e avisa o agente uma vez por faixa. Um goal por feature.

### ⏱️ Cache entre ciclos

Se o orquestrador dorme entre ciclos, acorde antes do cache expirar: OpenAI 30 min (acordar a cada ~25), Claude 1 h (~55). Perder o cache custa 12,5x a 25x. Acordar só para manter o cache vale se houver trabalho nas próximas horas.

### 📋 Modo fila

Backlog que cresce: o orquestrador pega a próxima tarefa, despacha numa sessão curta, confere e fecha. Para quando não há tarefa aberta (padrão do Symphony, da OpenAI, sobre o Linear). Comece com fila local em arquivos.

### 🔎 Memória entre sessões

O claude-mem funciona e serve para lembrar o que já foi feito num projeto, mas só cobre o Claude Code e guarda resumos, não o que foi dito. Para buscar palavra por palavra em tudo (Codex e Claude), use recall "termo" (índice SQLite FTS5, F8). A faxina com backup (F9) zerou a fila antiga e fechou as sessões presas. Análise em docs/pesquisa-memoria-claude-mem-2026-10.md .

### Regras do modo fila
- Uma tarefa por arquivo em longrun/<execução>/tasks/ , com status e campo evidencia: .
- Fechar exige evidência (saída de teste, arquivo, hash de commit) — senão "fechar sem fazer" vira atalho.
- O agente cria no máximo 5 tarefas por execução; acima disso, viram proposta e esperam aprovação.
- Fila vazia → encerrar workers, registrar em progress.md e parar. Linear/GitHub Issues só com autorização para a API.

Pesquisa · jul–out/2026

## O que mudou e o que é mito

Resumo da pesquisa com fontes em docs/pesquisa-web-2026-10.md .

### ✅ Confirmado

/goal , /compact , /resume e /fork existem no Codex (docs oficiais). Goals retomam após limite de uso (20/07) e após reinício do daemon (17/09). O Claude Code tem /goal desde mai/2026, com avaliador após cada turno.

### 🆕 Novos modelos

GPT-6 Astra (03/09) mantém notas entre janelas de contexto. Claude Opus 5.5 (22/09) tem 1M de contexto e leitura de cache a US$0,20/MTok.

### ❓ Sem fonte

A sessão de 11 dias / 573 turnos / 1,3 GB não tem fonte pública. É plausível: há relatos de logs de sessão de 0,7 a 2 GB.

### 📐 Não é padrão oficial

Os arquivos de estado são uma divisão da mesma ideia do PLANS.md (OpenAI) e do PROGRESS.md + git (Anthropic).

Material de origem

## De onde partiu

O infográfico e a capa que originaram o projeto, guardados em docs/origem/ junto com os quatro textos.

Infográfico: /goal, ciclo contínuo, arquivos de estado, autonomia, portões e métricas. Capa do experimento: 11 dias na mesma sessão (número sem fonte pública).

Roadmap

## Fases do plano

Detalhes em docs/PLANO-EXECUCAO-LONGA.md .

F0 ✓

Documentação e templates Material de origem, pesquisa, plano e templates publicados.

F1 ✓

Piloto Execução longa real (medir-sessao): goal nível 3, 14 testes congelados, loop headless — concluída no 1º ciclo, em 3 min, e conferida à parte.

F2 ✓

Medição tools/medir-sessao.py: lê 1,8 GB em ~9 s; bate com o oráculo em 2 sessões grandes e numa terceira nunca vista.

F3 ✓

Regras Bloco de execução longa nas instruções globais do Claude e do Codex; sessão nova segue sem ser lembrada.

F4 ✓

Rede de segurança flock + timeout nos crons com agente, --max-turns, hook que lembra de reler após compactar ou retomar, resumo de compactação estruturado no Codex.

F5 ✓

Vigia de agente tools/vigia.py a cada 10 min (timer systemd): avisa execução parada, parada sem aviso ou ociosa.

F6 ◐

Higiene tools/arquivar-sessoes.py pronto e testado (comprime com conferência, restaura); não aplicado — só 0,04 GB tinham mais de 90 dias.

F7 ◐

Experimento "até onde vai" Curva retrospectiva feita: o cache não cai com as compactações; sem compactar, o custo por turno cresce ~5x. Falta o experimento prospectivo sessão única × modo fila.

F8 ✓

Busca no histórico Comando recall "termo" : índice SQLite FTS5 de tudo o que foi dito com o Codex e o Claude (sem saída de ferramenta), reindexado de hora em hora. Feito por execução longa em 1 ciclo; 90 mil trechos, busca em 0,02–0,04 s.

F9 ✓

Faxina do claude-mem Feita com backup: 7.904 pendências antigas e 3.860 sessões presas (lotes automáticos de julho) tratadas sem reprocessar; logs de 640 para 129 MB; busca e captura seguem funcionando.

Relacionados

## Outros projetos do INEMA sobre o tema

### 🧠 agente-claude-codex

Núcleo portátil e handoff entre sessões e agentes.

### 🧰 claude-session-kit

Statusline, checkpoints e handoff antes do /clear.

### 🔁 loop-r

Loops autoaperfeiçoáveis com evidência e rollback.

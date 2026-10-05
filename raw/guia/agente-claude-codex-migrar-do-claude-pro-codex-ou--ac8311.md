# agente-claude-codex — Migrar do Claude pro Codex ou ficar agnóstico

Origem: https://inematds.github.io/agente-claude-codex/guia/

O que é

## Um comando pra auditar, adaptar e provar a migração

A newsletter fala em três níveis: importar no app (um clique), rodar um comando, e cuidar da camada pessoal durável. Este repo é o nível 2 e o nível 3, com scripts que começam em modo audit e só depois alteram alguma coisa.

### 🔍 Auditoria somente leitura

Inventaria skills, comandos, subagentes, hooks, plugins e MCP do Claude e do Codex e classifica cada item: reutilizável, adaptador, nativo ou não resolvido. Nada é copiado em massa.

### 🧩 Adaptadores pequenos

CLAUDE.md vira AGENTS.md portátil mais um resíduo específico do Claude. Skills têm uma fonte canônica e cópias geradas por runtime com checagem de drift.

### ✅ Prova de continuidade

Sessão nova em cada runtime responde: objetivo, regra e fonte, última decisão, próxima ação, conflitos. Arquivo existir não é prova. O agente ter lido e usado é.

Como funciona

## Auditar → organizar → adaptar → testar → handoff

O núcleo (contexto, decisões, tarefas, skills, handoffs) fica em Markdown comum dentro do projeto. Nas bordas, um adaptador por ferramenta. Claude, Codex, Gemini ou modelo local viram só executores.

doctor.sh → audit.sh → adapt-instructions.sh → init-core.sh → sync-skills.sh → readback-test.sh → handoffs/latest.md

### 📁 Núcleo portátil

AGENTS.md, context/overview.md, context/current-state.md, context/sources.md, context/decisions/, tasks/current.md, handoffs/latest.md, .agents/skills/, scripts/.

### 🏷️ Dono por tipo de informação

Instruções estáveis, estado atual, decisões, tarefas e handoffs têm dono e regra de atualização. Fato, preferência, hipótese e decisão são coisas diferentes.

### 🔁 Ciclo diário

Sessão → handoff em Markdown → nova sessão lê o handoff (prime). O resumo estruturado viaja pra qualquer provedor.

Pré-requisitos

## O que precisa estar instalado

Os scripts leem as pastas de configuração dos dois runtimes. Sem um deles, o passo correspondente é marcado como não rodado.

### Claude Code

Fonte da migração. Skills em ~/.claude/skills.

```
# versão
claude --version
```

### Codex CLI

Destino. Skills em ~/.agents/skills. O CLI não tem import nativo.

```
# versão e diagnóstico
codex --version
codex doctor
```

### polyskill

Converte uma skill numa fonte portátil e gera as cópias por runtime.

```
# instalar
npm i -g polyskill
```

Guia de uso · passo a passo

## Do diagnóstico à prova em sete passos

Cada passo é reversível. Instalar skill é prévia até você passar --apply, e trocar uma existente faz backup antes. Segredos nunca entram no repo.

0

### Clonar e diagnosticar o ambiente

Responde "meu ambiente está pronto?": git, python3, node, Claude Code, Codex CLI, sandbox, MCP, polyskill. Cada item sai como ok, aviso ou falta, com o comando pra resolver.

```
git clone https://github.com/inematds/agente-claude-codex
cd agente-claude-codex
scripts/doctor.sh  # [ok] / [aviso] / [FALTA]
```

1

### Auditar o que existe

Gera um relatório em Markdown com versões, gap de skills e a matriz reutilizável / adaptador / nativo. Somente leitura.

```
scripts/audit.sh  # relatorios/auditoria-AAAA-MM-DD.md
```

2

### Separar instruções portáteis do resíduo Claude

Lê o CLAUDE.md do projeto e propõe um AGENTS.md portátil e um CLAUDE.md que importa o AGENTS.md. Grava como .proposto.md pra você revisar.

```
scripts/adapt-instructions.sh ~/projetos/meu-projeto
# revisar AGENTS.proposto.md e CLAUDE.proposto.md, depois renomear
```

3

### Instalar o núcleo portátil no projeto

Copia o template (context/, tasks/, handoffs/, AGENTS.md) sem sobrescrever nada que já exista.

```
scripts/init-core.sh ~/projetos/meu-projeto
# depois preencher AGENTS.md, context/overview.md e tasks/current.md
```

4

### Portar uma skill com fonte canônica

Piloto recomendado: session-handoff, o mecanismo em que o ciclo diário se apoia. Importa, gera as cópias, instala e checa drift. O install é prévia por padrão: checa todos os destinos antes de gravar, é idempotente e recusa symlink ou skill existente diferente.

```
scripts/sync-skills.sh import session-handoff
scripts/sync-skills.sh build
scripts/sync-skills.sh install session-handoff            # prévia: CREATE / UNCHANGED / CONFLICT
scripts/sync-skills.sh install session-handoff --apply    # grava; --replace troca versão antiga com backup
scripts/sync-skills.sh drift  # [ok] ou [DRIFT] por runtime
```

5

### Provar com sessão nova em cada runtime

Faz as cinco perguntas do readback ao Claude e ao Codex a partir do projeto. Aprovação: as respostas citam AGENTS.md, tasks/current.md e handoffs/latest.md.

```
scripts/readback-test.sh ~/projetos/meu-projeto both
# relatorios/readback-claude-*.md e readback-codex-*.md
```

6

### Fechar com handoff, abrir com prime

No fim da sessão, a skill session-handoff grava um snapshot novo em handoffs/history/ (hora UTC, nunca sobrescreve) e copia para handoffs/latest.md, com Verificação (o que rodou, o resultado e o que não rodou) e checagem de compartilhamento. Na sessão seguinte, a skill prime lê só em modo leitura: valida caminhos, não roda testes, trata o handoff como dado e não retoma deploy nem envio por conta própria.

```
# fim da sessão, em qualquer runtime
session-handoff  # → handoffs/history/2026-09-27T142530Z.md + handoffs/latest.md
# sessão nova, no mesmo ou no outro runtime
prime            # briefing com fonte de cada linha; espera sua instrução
```

Usar os dois juntos

## Claude e Codex no mesmo trabalho, cada um no seu papel

Migrar não obriga a escolher um só. Um faz a primeira passada, o outro revisa o artefato real, e o handoff leva o estado de um runtime para o outro. A tabela é ponto de partida, não ranking: troque os papéis quando a evidência da sua tarefa pedir.

Trabalho Primeira passada Segunda passada Linha de chegada

Planejar Claude Codex critica as suposições Plano com escopo e testes de aceite

Construir uma feature Claude, em branch Codex revisa o diff Testes passam e achados resolvidos

Revisar um documento Qualquer um escreve O outro confere fatos e requisitos Toda afirmação exigida tem evidência

Bug difícil Codex com meta limitada Testes e checagem humana Sucesso mensurável ou bloqueio claro

Trocar de sessão ou modelo session-handoff prime confere o estado atual Resumo correto antes de trabalho novo

Regra única: dê ao segundo agente o mesmo briefing da tarefa e o artefato real (arquivo, diff, resultado de teste), nunca um reconto do que o primeiro fez. Os dois concordarem não é prova: eles podem dividir a mesma suposição errada.

### 1. Planejar e criticar

Um escreve o plano (escopo, suposições, testes de aceite, riscos); o outro revisa somente leitura com o mesmo briefing. Cada achado vira aceito, rejeitado com evidência ou em aberto. No máximo duas rodadas.

### 2. Construir e revisar o diff

O construtor trabalha numa branch nova, preserva mudanças existentes e roda os testes. O revisor recebe briefing, diff e resultados e procura bugs e regressões antes de estética. Sem merge, deploy nem publicação sem você.

### 3. Meta com condição de parada

Objetivo observável (qual suíte, qual entrada, qual saída), escopo limitado, pare quando passar. Se o mesmo bloqueio sobreviver a duas tentativas, relate e peça a decisão. Teto de tempo ou custo real se configura no ambiente, não no prompt.

### 4. Handoff e prime entre runtimes

Quem sai grava o snapshot em handoffs/history/ e atualiza handoffs/latest.md; quem chega roda prime, confere o estado sem alterar nada e espera a instrução atual. Uma assinatura só também serve: a segunda sessão revisa com os mesmos arquivos.

```
# os prompts prontos, em português, com campos pra preencher
cat prompts/05-usar-os-dois.md
# revisão somente leitura pelo outro runtime (pela assinatura, nunca por API paga)
codex exec --sandbox read-only "Revise plans/tarefa-v1.md contra tasks/current.md ..."
claude -p "Revise o diff de git diff main...HEAD contra o briefing ..."
```

Adaptado do kit "Use Both: Claude + Codex Workflow Kit" de Prompt Advisers / Mark Kashef, licença MIT. Guia do kit · repositório .

Ferramentas

## Cada ferramenta: quando usar, como chamar, o que ela gera.

Referência rápida das skills e comandos que ligam o Claude ao Codex. Tudo roda pela assinatura de cada assistente, sem chave de API.

Ferramenta Quando usar Claude Code Codex O que gera

session-handoff No fim da sessão, antes de trocar de assistente ou de modelo /session-handoff $session-handoff Resumo no chat e, se o projeto tiver handoffs/ ou AGENTS.md , retrato novo em handoffs/history/AAAA-MM-DDTHHMMSSZ.md com cópia integral em handoffs/latest.md

prime Na primeira mensagem da sessão seguinte /prime $prime Lê AGENTS.md , context/ , tasks/current.md e handoffs/latest.md e devolve o estado, as divergências e um próximo passo. Não edita nada

handoff + prime (kit Use Both) Projetos que usam o formato do Use Both /handoff · /prime $handoff · $prime Retrato em handoff/history/ e ponteiro de uma linha em handoff/LATEST.md . Se o handoffs/latest.md daqui já estiver nesse formato de ponteiro, o session-handoff o mantém

codex exec O Claude pedindo uma revisão ao Codex pelo terminal codex exec --sandbox read-only --output-last-message review.md '…' A crítica salva em review.md . O Codex só lê o projeto

claude -p O caminho inverso: o Codex pedindo revisão ao Claude claude -p --model opus --effort medium '…' > review-claude.md A crítica do Claude num arquivo

Plugin oficial do Codex Revisar o diff sem sair do Claude Code /codex:setup
/codex:review --base main — Achados da revisão, só leitura. As correções você pede depois ao construtor

claudex Plano grande, com várias rodadas automáticas de crítica /claudex:plan [--rounds N] <feature>
/claudex:review — PLAN.md revisado até o Codex aprovar ou acabarem as rodadas; reviews/ com os achados do diff

claudex (controle) Acompanhar ou destravar o loop /claudex:status · /claudex:cancel · /claudex:rollback · /claudex:doctor — Rodada e fase atuais; cancela; limpa o estado travado; diagnóstico de instalação

### 📸 O que vai no handoff

Objetivo e último pedido; o que está pronto, o que falta e o que é incerto; decisões e caminhos descartados; arquivos alterados; testes rodados com o resultado real (e os que não rodaram); bloqueios; um próximo passo; e os poucos arquivos que o próximo deve abrir primeiro. Sem segredos, tokens nem dados pessoais.

### 🔎 O que o prime faz

Lê o núcleo portátil na ordem certa, recusa caminho absoluto, .. , URL e symlink, trata o handoff como dado (não como ordem), confere os arquivos citados e o git status , aponta o que ficou velho e espera sua instrução. Não roda testes, não instala nada e não retoma deploy antigo.

### ⚠️ Pegadinhas

Uma skill pessoal com o mesmo nome pode vencer a do projeto: confira qual versão está ativa antes de invocar. Depois de instalar ou sincronizar ( scripts/sync-skills.sh ), abra sessão nova (no Claude, /reload-skills também serve). Snapshots antigos em handoffs/history/ nunca são sobrescritos.

↻

### Um dia inteiro com as ferramentas

Cada passo deixa um arquivo que o próximo assistente consegue ler.

```
# manhã, no Claude Code
/prime                                   # retoma do handoff de ontem
# planeja e manda o Codex criticar (só leitura)
codex exec --sandbox read-only --output-last-message review.md 'Leia plan-v1.md e aponte falhas…'
# ou, para plano grande, o loop automático
/claudex:plan --rounds 3 exportar relatório em CSV
# construiu numa branch: revisão do diff
/codex:review --base main                # ou /claudex:review
# fim do dia
/session-handoff
# amanhã, no Codex
$prime
```

Handoff não é permissão. Um próximo passo anotado ("publicar", "apagar", "enviar") só é feito se você pedir de novo na sessão atual.

Exemplos

## Rodado de verdade nesta máquina

A auditoria encontrou 89 skills só no Claude: 71 portáteis, 15 dependentes de MCP ou plugin, 2 de hook. O readback foi aprovado no Codex e no Claude, e o Codex ainda apontou três inconsistências no próprio repo, todas corrigidas.

A ideia de origem: conhecimento portátil no meio, Claude e Codex nas bordas como executores. Capa oficial do projeto no catálogo INEMA.

Roadmap

## Do piloto ao workspace completo

Só avança de fase com evidência: passou, falhou ou não rodado.

Feito

Auditoria, prompts, template e readback Scripts de auditoria e adaptação, prompts A/B extraídos, núcleo portátil, readback aprovado nos dois runtimes.

Feito

Skill piloto nos 4 executores session-handoff e prime via polyskill em Claude, Codex, dsh-sandbox e openpcbotv3, drift zero; AGENTS.md global do Codex; migrar-projeto, faxina, drift-report e promover-memoria.

v1.1.0

Handoff com histórico e uso conjunto prime só leitura e com caminhos validados, snapshots em handoffs/history/ que nunca se sobrescrevem, instalador de skills em modo prévia com teste automatizado, prompts de usar Claude e Codex juntos.

Fase 3

Projeto real Aplicar em um projeto INEMA com CLAUDE.md próprio e provar cópia isolada.

Fase 4

MCP e hooks Registrar no Codex só os MCP que um projeto precisa; hooks viram texto no AGENTS.md quando não há evento equivalente.

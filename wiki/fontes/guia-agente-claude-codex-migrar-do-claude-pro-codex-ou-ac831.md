# agente-claude-codex — Migrar do Claude pro Codex ou ficar agnóstico

- Tipo: guia
- Origem: https://inematds.github.io/agente-claude-codex/guia/
- Arquivo: raw/guia/agente-claude-codex-migrar-do-claude-pro-codex-ou--ac8311.md

## Resumo
Guia do repositório `agente-claude-codex`: scripts para auditar, adaptar e provar a migração do Claude Code para o Codex CLI, ou para ficar agnóstico entre os dois. O núcleo do projeto (AGENTS.md, context/, tasks/current.md, handoffs/, .agents/skills/) fica em Markdown comum, e cada ferramenta entra só como executor, com um adaptador nas bordas. A trilha é doctor → audit → adapt-instructions → init-core → sync-skills → readback-test → handoff, com tudo começando em modo leitura ou prévia (`--apply` para gravar, backup antes de trocar). A prova não é o arquivo existir: uma sessão nova em cada runtime precisa responder objetivo, regra, última decisão e próxima ação citando os arquivos do núcleo. A segunda metade ensina a usar os dois juntos (um faz, o outro revisa o artefato real), o par session-handoff/prime entre sessões e runtimes, e a tabela de ferramentas (codex exec read-only, claude -p, plugin do Codex, claudex). Números reais: 89 skills só no Claude (71 portáteis, 15 dependentes de MCP/plugin, 2 de hook) e readback aprovado nos dois runtimes.

## Ideias centrais
- Prova é uso, não presença: "Arquivo existir não é prova. O agente ter lido e usado é."
- Conhecimento no meio, ferramentas nas bordas: "Claude, Codex, Gemini ou modelo local viram só executores."
- Nada em massa: "Nada é copiado em massa."
- Reversível por padrão: "Cada passo é reversível."
- Revisão com o artefato real: "dê ao segundo agente o mesmo briefing da tarefa e o artefato real (arquivo, diff, resultado de teste), nunca um reconto do que o primeiro fez."
- Concordar não é provar: "Os dois concordarem não é prova: eles podem dividir a mesma suposição errada."
- Meta com parada: "Objetivo observável (qual suíte, qual entrada, qual saída), escopo limitado, pare quando passar."
- Handoff é dado, não ordem: "Handoff não é permissão."
- Teto fora do prompt: "Teto de tempo ou custo real se configura no ambiente, não no prompt."

## Como ele ensina aqui
- Começa pelo diagnóstico (`doctor.sh` com ok / aviso / FALTA e o comando pra resolver) antes de mexer em qualquer coisa.
- Toda escrita passa por prévia: `.proposto.md` para revisar, `install` sem `--apply` mostra CREATE / UNCHANGED / CONFLICT.
- Separa tipos de informação: "Fato, preferência, hipótese e decisão são coisas diferentes."
- Mostra a tabela de papéis como ponto de partida, não ranking, e um dia inteiro de uso com os comandos reais.
- Roadmap só avança com evidência: "Só avança de fase com evidência: passou, falhou ou não rodado."
- Tudo pela assinatura: "Tudo roda pela assinatura de cada assistente, sem chave de API."

## Ligações
- Temas: [[claude-code]], [[contexto-e-memoria]], [[skills]], [[orquestracao-de-modelos]], [[subagentes]]
- Princípios: [[independencia-de-plataforma]], [[verificar-antes-de-afirmar]], [[criterio-de-pronto-explicito]], [[menor-custo-que-resolve]]
- Métodos: [[nucleo-portatil-entre-runtimes]], [[revisao-cruzada-entre-agentes]], [[higiene-de-contexto]], [[guia-de-projeto-landing]]

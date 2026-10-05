# Núcleo portátil entre runtimes (Claude ↔ Codex)

- Tipo: metodo

## O que é

Tirar o conhecimento do projeto de dentro de uma ferramenta e pôr num núcleo em Markdown comum (AGENTS.md, context/, tasks/, handoffs/, skills com fonte canônica), deixando Claude, Codex ou modelo local só como executores com um adaptador pequeno. A migração só conta quando uma sessão nova em cada runtime prova que leu e usou o núcleo.

## Passos

1. Diagnosticar o ambiente (`scripts/doctor.sh`): cada item sai ok, aviso ou FALTA, com o comando pra resolver
2. Auditar somente leitura (`scripts/audit.sh`): inventário de skills, comandos, subagentes, hooks, plugins e MCP, classificados em reutilizável / adaptador / nativo / não resolvido
3. Separar instruções portáteis do resíduo da ferramenta: CLAUDE.md vira AGENTS.md + um CLAUDE.md que importa o AGENTS.md, gravados como `.proposto.md` para revisar
4. Instalar o núcleo no projeto sem sobrescrever nada (`scripts/init-core.sh`) e preencher AGENTS.md, context/overview.md e tasks/current.md
5. Portar uma skill piloto com fonte canônica (`sync-skills.sh import / build / install` em prévia, `--apply` para gravar, `drift` para conferir)
6. Provar com sessão nova em cada runtime (`readback-test.sh`): as respostas precisam citar AGENTS.md, tasks/current.md e handoffs/latest.md
7. Fechar a sessão com session-handoff (snapshot novo, nunca sobrescreve) e abrir a próxima com prime (só leitura, trata o handoff como dado)

## Exemplos (trechos)

- "Arquivo existir não é prova. O agente ter lido e usado é." — [[guia-agente-claude-codex-migrar-do-claude-pro-codex-ou-ac831]] `raw/guia/agente-claude-codex-migrar-do-claude-pro-codex-ou--ac8311.md`
- "Claude, Codex, Gemini ou modelo local viram só executores." — [[guia-agente-claude-codex-migrar-do-claude-pro-codex-ou-ac831]] `raw/guia/agente-claude-codex-migrar-do-claude-pro-codex-ou--ac8311.md`
- "Nada é copiado em massa." — [[guia-agente-claude-codex-migrar-do-claude-pro-codex-ou-ac831]] `raw/guia/agente-claude-codex-migrar-do-claude-pro-codex-ou--ac8311.md`
- "Fato, preferência, hipótese e decisão são coisas diferentes." — [[guia-agente-claude-codex-migrar-do-claude-pro-codex-ou-ac831]] `raw/guia/agente-claude-codex-migrar-do-claude-pro-codex-ou--ac8311.md`
- "A auditoria encontrou 89 skills só no Claude: 71 portáteis, 15 dependentes de MCP ou plugin, 2 de hook." — [[guia-agente-claude-codex-migrar-do-claude-pro-codex-ou-ac831]] `raw/guia/agente-claude-codex-migrar-do-claude-pro-codex-ou--ac8311.md`

## Fontes

- [[guia-agente-claude-codex-migrar-do-claude-pro-codex-ou-ac831]] — agente-claude-codex — Migrar do Claude pro Codex ou ficar agnóstico

## Relacionados

[[independencia-de-plataforma]], [[contexto-e-memoria]], [[skills]], [[claude-code]], [[higiene-de-contexto]], [[execucao-longa-com-estado-em-arquivos]], [[revisao-cruzada-entre-agentes]]

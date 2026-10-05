# Revisão cruzada entre agentes (um faz, outro revisa)

- Tipo: metodo

## O que é

Usar dois agentes no mesmo trabalho: um faz a primeira passada, o outro revisa o artefato real (plano, diff, resultado de teste) com o mesmo briefing, em modo só leitura. Os papéis trocam conforme a evidência da tarefa; os dois concordarem não substitui o teste.

## Passos

1. Escrever um briefing da tarefa (escopo, suposições, testes de aceite, riscos)
2. O primeiro agente faz: plano, ou código numa branch nova rodando os testes
3. O segundo agente recebe o mesmo briefing e o artefato real (arquivo, diff, saída de teste), nunca um reconto, e revisa só leitura (`codex exec --sandbox read-only`, `claude -p`, `/codex:review`)
4. Cada achado vira aceito, rejeitado com evidência ou em aberto; no máximo duas rodadas
5. Bugs e regressões antes de estética; correção volta para quem construiu
6. Merge, deploy e publicação só com o humano

## Exemplos (trechos)

- "dê ao segundo agente o mesmo briefing da tarefa e o artefato real (arquivo, diff, resultado de teste), nunca um reconto do que o primeiro fez." — [[guia-agente-claude-codex-migrar-do-claude-pro-codex-ou-ac831]] `raw/guia/agente-claude-codex-migrar-do-claude-pro-codex-ou--ac8311.md`
- "Os dois concordarem não é prova: eles podem dividir a mesma suposição errada." — [[guia-agente-claude-codex-migrar-do-claude-pro-codex-ou-ac831]] `raw/guia/agente-claude-codex-migrar-do-claude-pro-codex-ou--ac8311.md`
- "Sem merge, deploy nem publicação sem você." — [[guia-agente-claude-codex-migrar-do-claude-pro-codex-ou-ac831]] `raw/guia/agente-claude-codex-migrar-do-claude-pro-codex-ou--ac8311.md`
- "também é muito bom tu ter uma outra IA" (@00:08:29) — [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] `raw/videos/inema-vibecode-do-zero-dia-1-infra-git-e-vercel.txt`
- "vai questionar tudo o que que foi feito," (@00:08:34) — [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] `raw/videos/inema-vibecode-do-zero-dia-1-infra-git-e-vercel.txt`

## Fontes

- [[guia-agente-claude-codex-migrar-do-claude-pro-codex-ou-ac831]] — agente-claude-codex — Migrar do Claude pro Codex ou ficar agnóstico
- [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] — INEMA  VibeCode do Zero - Dia 1 - Infra Git e Vercel

## Relacionados

[[verificar-antes-de-afirmar]], [[orquestracao-de-modelos]], [[subagentes]], [[criterio-de-pronto-explicito]], [[nucleo-portatil-entre-runtimes]]

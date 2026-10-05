# Vibe code do zero: ideia → contexto → plano → implementação → teste → git → deploy

- Tipo: metodo

## O que é

O fluxo que ele ensina para construir com IA: estruturar a ideia como contexto numa pasta, planejar com esforço alto e validar o plano em outro modelo, implementar com esforço baixo, testar com outra IA, commitar e publicar.

## Passos

1. Criar a pasta do projeto dentro de projetos/ e, dentro dela, a pasta doc (privada, no .gitignore) com referências, prints, links e o que foi discutido no chat
2. Brainstorm da ideia no chat com esforço alto, buscando opiniões e pesquisas diferentes
3. Pedir um plano em MD e validá-lo em outro modelo (Claudex/Codex, ChatGPT ou outra versão de LLM)
4. Implementar com esforço menor, dando instrução curta que aponta para o contexto (@doc)
5. Testar/validar, de preferência com outra IA que questiona tudo; definir claramente o que testar
6. Commitar e dar push no GitHub (SSH configurado, .env fora do git)
7. Publicar: GitHub Pages (main + root) se público, ou importar no Vercel configurando variáveis, diretório raiz e domínio

## Exemplos (trechos)

- "todo. Então, o processo é você ter uma" (@00:01:51) — [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] `raw/videos/inema-vibecode-do-zero-dia-1-infra-git-e-vercel.txt`
- "plano, validar de novo para outros" (@00:07:30) — [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] `raw/videos/inema-vibecode-do-zero-dia-1-infra-git-e-vercel.txt`
- "joga pro git, certo? E transforma aquilo" (@01:19:28) — [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] `raw/videos/inema-vibecode-do-zero-dia-1-infra-git-e-vercel.txt`
- "Tu pega o plano e leva no Codex." (@02:49:42) — [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] `raw/videos/inema-vibecode-do-zero-dia-1-infra-git-e-vercel.txt`

## Fontes

- [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] — INEMA  VibeCode do Zero - Dia 1 - Infra Git e Vercel

## Relacionados

[[verificar-antes-de-afirmar]], [[construir-junto-ao-vivo]], [[orquestracao-de-modelos]], [[menor-custo-que-resolve]], [[contexto-e-memoria]], [[custo-de-tokens]]

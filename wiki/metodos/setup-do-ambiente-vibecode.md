# Montar o ambiente de vibe code do zero

- Tipo: metodo

## O que é

Sequência de infraestrutura antes do primeiro prompt: pasta de projetos, agente instalado, login pela assinatura, chave SSH no destino, Git e só então deploy.

## Passos

1. Abrir o terminal, entrar no usuário e criar a pasta projetos (uma subpasta por projeto)
2. Conferir node/npm e instalar Codex e Claude Code (global, -g)
3. Entrar no agente de dentro da pasta do projeto (limite de segurança) e logar pela assinatura
4. Gerar a chave SSH e cadastrar só a pública no GitHub/VPS
5. Versionar: criar o repositório e pedir ao agente em linguagem comum (atualiza o git = push, busca = pull, instala = clone)
6. Publicar: público no GitHub Pages (guia/index.html), privado na Vercel com variáveis de ambiente, processo contínuo na VPS

## Exemplos (trechos)

- "Ele vai deletar ali para baixo. Sempre" (@00:34:40) — [[video-inema-vibecode-do-zero-dia-3-basico-de-infra]] `raw/videos/inema-vibecode-do-zero-dia-3-basico-de-infra.txt`
- "tu quer, tu tem que pensar em" (@01:53:28) — [[video-inema-vibecode-do-zero-dia-3-basico-de-infra]] `raw/videos/inema-vibecode-do-zero-dia-3-basico-de-infra.txt`
- "numa linguagem comum, mas a gente sabe" (@01:34:45) — [[video-inema-vibecode-do-zero-dia-3-basico-de-infra]] `raw/videos/inema-vibecode-do-zero-dia-3-basico-de-infra.txt`

## Fontes

- [[video-inema-vibecode-do-zero-dia-3-basico-de-infra]] — INEMA  VibeCode do Zero - Dia 3 -  Basico de Infra

## Relacionados

[[construir-junto-ao-vivo]], [[menor-custo-que-resolve]], [[live-construindo-ao-vivo]], [[custo-de-tokens]], [[git-e-deploy]], [[infraestrutura-basica]]

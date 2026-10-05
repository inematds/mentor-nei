# Instalar e atualizar app na VPS

- Tipo: metodo

## O que é

Instalar do zero numa VPS limpa para ver os erros reais, e atualizar com sequência fixa (pull, install, build, stop, start) empacotada em scripts.

## Passos

### Instalar do zero numa VPS

1. mkdir projetos, git clone e entrar na pasta
2. npm install; se der erro, levar ao chat e conferir node -v e npm -v
3. Copiar .env.example para .env e colocar só as chaves necessárias
4. Rodar o set-password (senha criptografada) e o script que abre a porta no firewall
5. Subir com npm run dev (com log) e testar uma geração real
6. Fechar a porta quando não estiver usando; documentar os pré-requisitos

### Atualizar app rodando na VPS

1. Entrar na pasta do projeto e dar git pull
2. npm install e npm run build (rodar na mão para ver se dá erro)
3. Parar o que está rodando (stop.sh)
4. Subir de novo (start.sh) e conferir no navegador

## Exemplos (trechos)

- "vejo, tá? As VPS não estão atualizadas e" (@01:34:52) — [[video-live-bench-studio-com-81-modelos-de-ia-instalacao-do-z]] `raw/videos/live-bench-studio-com-81-modelos-de-ia-instalacao-do-zero.txt`
- "Certo? Gerando um log aqui. Ou seja," (@01:30:28) — [[video-live-bench-studio-com-81-modelos-de-ia-instalacao-do-z]] `raw/videos/live-bench-studio-com-81-modelos-de-ia-instalacao-do-zero.txt`
- "Se você não faz isso, ele vai ficar em" (@00:57:13) — [[video-live-deepseek-harness-orquestre-ias-e-corte-custos-em-]] `raw/videos/live-deepseek-harness-orquestre-ias-e-corte-custos-em-95x.txt`

## Fontes

- [[video-live-bench-studio-com-81-modelos-de-ia-instalacao-do-z]] — LIVE： Bench Studio com 81 Modelos de IA - Instalação do Zero
- [[video-live-deepseek-harness-orquestre-ias-e-corte-custos-em-]] — LIVE： DeepSeek Harness - Orquestre IAs e Corte Custos em 95x

## Relacionados

[[construir-junto-ao-vivo]], [[orquestracao-de-modelos]], [[llm-local-e-gratis]], [[medir-antes-de-acreditar]], [[custo-de-tokens]], [[fundamentos-antes-de-ferramentas]]

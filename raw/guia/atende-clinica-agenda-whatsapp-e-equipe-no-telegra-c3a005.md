# Atende Clínica — agenda, WhatsApp e equipe no Telegram para clínicas

Origem: https://inematds.github.io/atende-clinica/guia/

O que é

## Menos falta, menos telefone tocando, mais paciente voltando

Falta sem aviso é o vazamento nº 1 de uma clínica: 5 a 12% numa agenda bem cuidada, perto de 25% na média. O Atende Clínica ataca isso com as peças da receita "Agenda cheia" do Raio-X de Margem e devolve os números do mês para o painel de recuperação.

### 📅 Agenda que se defende sozinha

Horário por profissional, folgas e férias, confirmação 48 h antes com "1 confirma / 2 cancela". Quem cancela libera o horário para a lista de espera na hora, e o retorno (ex.: limpeza a cada 180 dias) é lembrado sozinho.

### 💬 WhatsApp e chat com um mesmo cérebro

O paciente agenda, remarca e tira dúvidas pelas perguntas frequentes da clínica. O bot não inventa preço nem diagnóstico. Pedido de atendente, emergência (manda ligar 192) ou duas dúvidas sem resposta vão para a equipe.

### 🛡️ Regras de saúde de fábrica

Campanha só para quem consentiu, e o texto passa pela trava do conselho (CFM, CFO, COFFITO): preço, parcelamento, sorteio, "antes e depois", "resultado garantido". O paciente pode pedir "PARAR", exportar os próprios dados ou pedir exclusão (LGPD).

Como funciona

## Do "oi" no WhatsApp à consulta confirmada

Um servidor Python sem dependências, com banco SQLite num volume Docker. A Evolution e o Telegram entram por variáveis de ambiente; sem elas, o sistema roda com uma caixa de saída simulada.

WhatsApp (Evolution) ou chat do site → Conversa: FAQ, agendar, confirmar → Agenda + lista de espera → Lembretes e retornos → Equipe no Telegram / recepção → Números do mês para o Raio-X

### Paciente

WhatsApp ou chat do site. Agenda nos 3 primeiros horários livres, responde à confirmação, entra na lista de espera, recebe o lembrete de retorno.

### Equipe

Grupo do Telegram: recebe cada atendimento como #id , responde em cima da mensagem ou com /responder , e usa /fila , /agenda e /encerrar .

### Recepção (web)

Página /recepcao com token: agenda por período, cadastros de pacientes, profissionais, serviços e perguntas frequentes, bloqueios, fila humana, campanhas e indicadores.

Pré-requisitos

## O que você precisa

Para testar no computador basta o Python. Para produção, uma VPS com Docker e, se quiser os canais, uma Evolution API e um bot do Telegram seus.

### Python 3.10+

Só a biblioteca padrão: nada de pip install .

```
# conferir
python3 --version
```

### Docker + Compose (VPS)

Imagem python:3.12-slim , porta só em 127.0.0.1, atrás de um proxy HTTPS (Nginx, Caddy).

```
# conferir
docker compose version
```

### Evolution API e bot do Telegram (opcionais)

Uma instância Evolution conectada ao WhatsApp da clínica e um bot (BotFather) num grupo da equipe. As credenciais ficam só no .env .

```
# modelo das variáveis
cp .env.exemplo .env
```

Guia de uso · passo a passo

## Do clone ao WhatsApp respondendo

Os comandos abaixo são os do repositório. Comece local, sem integrações; ligue Evolution e Telegram por último.

1

### Baixe e configure a clínica

Copie o exemplo e edite dados/clinica.json : nome, conselho ( cfm , cfo , coffito ou estetica ), token próprio , horários, feriados, profissionais, serviços (com retorno_dias ) e perguntas frequentes.

```
git clone https://github.com/inematds/atende-clinica && cd atende-clinica
mkdir -p dados && cp exemplos/clinica.json dados/clinica.json
```

2

### Suba local e teste o chat

Abra http://127.0.0.1:8080/ para o chat do paciente e /recepcao para a equipe (pede o token do clinica.json ).

```
./atende serve --porta 8080 --dados dados   # 1ª linha: PORTA=8080
```

3

### Ligue os lembretes

Confirmações, retornos e reenvios saem quando /api/tarefas/rodar é chamado. Coloque uma chamada no cron a cada 5 minutos (a operação é idempotente).

```
# crontab -e
*/5 * * * * curl -s -X POST -H "X-Token: SEU_TOKEN" http://127.0.0.1:8080/api/tarefas/rodar
```

4

### Suba na VPS com Docker

O volume ./dados guarda o banco; o serviço reinicia sozinho e publica só 127.0.0.1:8080 . Aponte o proxy HTTPS para essa porta, incluindo /api/ e /webhook/ .

```
cp .env.exemplo .env && chmod 600 .env
docker compose up -d --build
docker compose ps   # healthy = /api/saude respondendo
```

5

### Conecte o WhatsApp pela Evolution

Preencha EVOLUTION_URL , EVOLUTION_API_KEY , EVOLUTION_INSTANCIA e WEBHOOK_SEGREDO . Na instância, aponte o webhook para a sua URL pública e ligue o evento MESSAGES_UPSERT . Grupos, mensagens da própria clínica e reenvios são ignorados.

```
# webhook da instância Evolution
https://SEU-DOMINIO/webhook/evolution/<WEBHOOK_SEGREDO>
docker compose up -d --force-recreate
```

6

### Ponha a equipe no Telegram

Crie o bot, adicione ao grupo da equipe e preencha TELEGRAM_API_URL , TELEGRAM_TOKEN , TELEGRAM_CHAT_ID e TELEGRAM_SEGREDO . Registre o webhook com o mesmo segredo.

```
curl -X POST "https://api.telegram.org/bot<TOKEN>/setWebhook" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://SEU-DOMINIO/webhook/telegram","secret_token":"<TELEGRAM_SEGREDO>"}'
# no grupo: /fila · /agenda 2026-10-07 · /responder 3 Já te ligo · /encerrar 3
```

7

### Backup diário e números do mês

O backup é um snapshot consistente (pode rodar com o servidor ligado) e contém dados pessoais: guarde com acesso restrito. O raiox grava o mês no arquivo de acompanhamento do Painel de Recuperação.

```
./atende backup --dados dados --saida backups/clinica.zip
./atende restaurar --dados dados --entrada backups/clinica.zip   # com o serviço parado
./atende raiox --dados dados --mes 2026-10 --acompanhamento acompanhamento.json
```

Exemplos

## Telas reais do sistema

Capturadas do próprio Atende Clínica rodando com a clínica de exemplo (odontologia, Dra. Ana e Dr. Bruno).

Chat do paciente: escolhe o serviço, recebe os 3 primeiros horários livres e agenda com duas respostas. O mesmo diálogo acontece no WhatsApp. Recepção: agenda por período e profissional, presença e falta num clique, além de fila humana, cadastros, campanhas e Raio-X.

Roadmap

## Onde está e para onde vai

A v1 foi feita por uma execução longa de agente (método execucao-longa ) contra 93 testes de aceitação congelados, conferida depois numa clínica que o agente nunca viu e num docker build real.

v1 ✅

Atendimento completo Agenda, confirmação, espera, retorno, perguntas frequentes, fila humana, emergência, campanhas com trava de conselho, LGPD, cadastros, bloqueios, backup, Evolution, Telegram, Docker e exportação para o Raio-X.

Próximo

Piloto numa clínica real Configurar horários, serviços e perguntas verdadeiros, medir 4 semanas de faltas (o "antes") e acompanhar no Painel de Recuperação.

Depois

Mais canais e respostas Respostas com IA atrás de uma opção desligada por padrão, sinal por Pix e planos (exigem integração de pagamento) e interface em inglês e espanhol.

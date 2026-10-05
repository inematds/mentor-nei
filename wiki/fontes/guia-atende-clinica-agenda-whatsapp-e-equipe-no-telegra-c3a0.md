# Atende Clínica — agenda, WhatsApp e equipe no Telegram para clínicas

- Tipo: guia
- Origem: https://inematds.github.io/atende-clinica/guia/
- Arquivo: raw/guia/atende-clinica-agenda-whatsapp-e-equipe-no-telegra-c3a005.md

## Resumo
Guia de um sistema de atendimento para clínicas que ataca a falta sem aviso (5–12% numa agenda cuidada, ~25% na média). Junta agenda por profissional, confirmação 48 h antes, lista de espera, lembrete de retorno, FAQ no WhatsApp (Evolution) e no chat do site, fila humana no Telegram e uma recepção web. Traz regras de saúde de fábrica: o bot não inventa preço nem diagnóstico, campanhas passam pela trava do conselho (CFM/CFO/COFFITO) e há LGPD (PARAR, exportar, excluir). Tecnicamente é um servidor Python só com biblioteca padrão e SQLite em volume Docker; sem as integrações, roda com caixa de saída simulada. O passo a passo começa local e liga Evolution e Telegram por último. A v1 foi construída por execução longa de agente contra 93 testes de aceitação congelados e conferida numa clínica que o agente nunca viu.

## Ideias centrais
- Problema medido antes da solução: "Falta sem aviso é o vazamento nº 1 de uma clínica".
- Limites do bot: "O bot não inventa preço nem diagnóstico."
- Escalonamento para humano: emergência "(manda ligar 192) ou duas dúvidas sem resposta vão para a equipe."
- Simplicidade: "Só a biblioteca padrão: nada de pip install ."
- Roda sem integrações: "sem elas, o sistema roda com uma caixa de saída simulada."
- Ordem de montagem: "Comece local, sem integrações; ligue Evolution e Telegram por último."
- Tarefas agendadas seguras: cron a cada 5 minutos "(a operação é idempotente)".
- Critério de pronto: "93 testes de aceitação congelados, conferida depois numa clínica que o agente nunca viu e num docker build real."
- Próximo passo é medir o antes: "medir 4 semanas de faltas".

## Como ele ensina aqui
- Parte de um número de negócio (taxa de faltas) e liga o produto a um painel de recuperação que mede o efeito.
- Monta do mais simples ao mais integrado: local → Docker na VPS → WhatsApp → Telegram → backup, cada passo com comando de conferência (`docker compose ps` healthy = `/api/saude`).
- Verifica com teste congelado e com um caso novo que o agente não viu, para evitar overfitting do agente aos testes.
- Cuida de segurança e dados desde o início (porta só em 127.0.0.1, `.env` com chmod 600, backup com acesso restrito).

## Ligações
- Temas: [[atendimento-com-agentes]], [[execucao-longa]], [[infraestrutura-basica]], [[git-e-deploy]]
- Princípios: [[medir-antes-de-acreditar]], [[criterio-de-pronto-explicito]], [[simplicidade-e-corte]], [[verificar-antes-de-afirmar]]
- Métodos: [[guia-de-projeto-landing]]

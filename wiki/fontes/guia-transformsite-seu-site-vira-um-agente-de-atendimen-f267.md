# transformsite — seu site vira um agente de atendimento por chat

- Tipo: guia
- Origem: https://inematds.github.io/transformsite/guia/
- Arquivo: raw/guia/transformsite-seu-site-vira-um-agente-de-atendimen-f26733.md

## Resumo
Guia de um framework aberto que transforma um site (mais PDFs e documentos) num agente de atendimento por chat, inspirado no America.gov. O site vira índice de busca híbrida e cada resposta cita a página-fonte; sem fonte, o bot diz "não sei" e oferece a equipe. Serviços (agendar, fale conosco, segunda via) são declarados em YAML como máquinas de slots validados, e o mesmo motor atende widget, Telegram, WhatsApp e e-mail. Roda com LLM local no Ollama (ou Claude Code/Codex pela assinatura), índice em SQLite e cuidados de LGPD. São seis fases, cada uma com comando próprio e critério de pronto medido (inventory → ingest → serviços → canais → convert → painel). O piloto foi o próprio inema.club, medido com 73 perguntas de teste.

## Ideias centrais
- Resposta com fonte: "Cada resposta traz o link da página usada."
- Recusa honesta: "e oferece passar para a equipe" quando não há fonte (o bot diz não sei).
- "Serviço = um arquivo YAML" — declarar dados, confirmação e ação em vez de programar fluxo.
- Fases com pronto medido: "Seis fases, cada uma com comando próprio e critério de pronto medido."
- Local primeiro: "LLM no Ollama (ou Claude Code / Codex pela assinatura), índice num arquivo SQLite".
- "Meça antes de publicar" — `golden` + `eval` (citação válida, "não sei", injeção).
- Piloto com números: "92,6% das respostas com fonte válida" e "100% das tentativas de injeção bloqueadas".
- Legado preservado: "convert transforma formulário HTML/PDF em serviço, que continua enviando ao sistema antigo."
- Humano no circuito: no painel, "um atendente assume uma conversa (o bot silencia) e devolve quando terminar."

## Como ele ensina aqui
- Usa comandos reais do piloto com o próprio site (387 páginas, 1.512 trechos em 249 s), não exemplos inventados.
- Põe um portão de avaliação antes da publicação: gera rascunho de perguntas a partir da base, revisa e roda eval com LLM real (13/13 cenários).
- Valida antes de subir (`transformsite validate` → 0 erros) e marca serviço convertido como `review: pending` até aprovação humana.
- Oferece caminho grátis/local e caminho pela assinatura, evitando dependência de API paga.

## Ligações
- Temas: [[atendimento-com-agentes]], [[seo-e-sites-para-agentes]], [[llm-local-e-gratis]], [[agentes-de-ia]], [[git-e-deploy]]
- Princípios: [[medir-antes-de-acreditar]], [[verificar-antes-de-afirmar]], [[criterio-de-pronto-explicito]]
- Métodos: [[guia-de-projeto-landing]]

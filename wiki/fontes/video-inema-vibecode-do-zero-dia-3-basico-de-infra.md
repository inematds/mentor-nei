# INEMA  VibeCode do Zero - Dia 3 -  Basico de Infra

- Tipo: video
- Origem: https://www.youtube.com/watch?v=SgVhktUzuFM
- Arquivo: raw/videos/inema-vibecode-do-zero-dia-3-basico-de-infra.txt

## Resumo
Aula ao vivo (cerca de 3 h) para iniciantes, sobre a infraestrutura que vem antes de qualquer vibe code. Abre com o contexto de mercado (o fim do SaaS, verticalizar um serviço com software próprio) e depois monta junto com a turma: pasta `projetos` no terminal (CMD/PowerShell/Linux), instalação do Codex e do Claude Code (com Node/npm), login pela assinatura, chaves SSH (pública × privada, uma por destino), GitHub (clone/pull/push, branch/merge, repositório público × privado, GitHub Pages com pasta `guia/`), Vercel (importar repositório, variáveis de ambiente, limite do plano grátis), quando usar VPS e o custo de CPU × GPU (Replicate, Hugging Face). Ao vivo aparecem erros reais: login OAuth do Codex numa VPS sem navegador (resolvido com túnel SSH para o localhost), chave já em uso no GitHub, comando com a barra errada que deu OK mas não criou o arquivo, e o push recusado até ele mandar o agente usar SSH em vez do `gh`. A conclusão: vibe code do zero não é escrever o prompt, e sim dominar pastas, SSH e Git antes.

## Ideias centrais
- Infra vem antes do prompt: "tu quer, tu tem que pensar em" (@01:53:28) infraestrutura, antes de pedir o sistema.
- Ideia precisa ser validada por quem conhece o domínio: "ter essa ideia validada por alguém que" (@00:09:04)
- Trabalhar sempre dentro de uma pasta de projeto como limite de segurança: "Ele vai deletar ali para baixo. Sempre" (@00:34:40)
- Usar o agente pela assinatura, não pela API: "50, 60, 70 vezes mais do que você pagar" (@00:43:49)
- Não decorar comandos, pedir à IA: "coisas, decoro. Basta eu pedir o que que" (@01:09:48); dá para pedir Git em linguagem comum, mas é preciso "entender essa lógica de fluxo para poder" (@01:36:49) trabalhar (pull/push/merge).
- Chave SSH: compartilha a pública, nunca a privada; se vazou, revoga: "a chave pública. Se por acaso eu mostrar" (@01:06:20)
- Começar simples: "Então não tenha vários logins, tenha um." (@02:25:07)
- O OK do sistema não prova que o resultado existe: "ele passou dizendo que tinha OK, mas não" (@02:38:55) criou o destino.
- Onde roda cada coisa: GitHub Pages para repositório público, Vercel para privado, VPS para o que "processo que não roda numa página web," (@01:06:59)
- Ver o limite do plano grátis antes de crescer: "sempre ver as limitações do free, né? O" (@02:16:00)

## Como ele ensina aqui
- Constrói junto e pausa a aula para cada aluno executar e dar um OK (criar a pasta VC 1208, gerar duas chaves SSH), antes de avançar.
- Trata o erro ao vivo como material de aula: "Por isso que eu gosto que dá erro, né?" (@00:58:41); "um procedimento para resolver os erros." (@02:37:09)
- Depura levando a mensagem de erro para o chat, com o histórico de antes: "problema quando dá, levam pro chat e às" (@02:54:17)
- Às vezes é teimoso de propósito e pula o pré-requisito, para mostrar o que quebra: "Mas eu sou um teimoso e eu vou querer" (@00:32:08); depois explica que pulou degraus.
- Confere o resultado de verdade (`ls -la`, refresh no GitHub) em vez de confiar na saída. Entrega o material em `.md` para o aluno levar ao chat: "Porque você pode pegar isso, levar pro" (@02:56:10)

## Ligações
- Temas: [[infraestrutura-basica]], [[git-e-deploy]], [[claude-code]], [[custo-de-tokens]]
- Princípios: [[verificar-antes-de-afirmar]], [[construir-junto-ao-vivo]], [[menor-custo-que-resolve]], [[simplicidade-e-corte]]
- Métodos: [[depurar-ao-vivo]], [[live-construindo-ao-vivo]], [[guia-de-projeto-landing]], [[setup-do-ambiente-vibecode]]

# LIVE： Agentes, Workers, Filas e Skills - Arquitetura IA

- Tipo: video
- Origem: https://www.youtube.com/watch?v=vnSZUDjvdZQ
- Arquivo: raw/videos/live-agentes-workers-filas-e-skills-arquitetura-ia.txt

## Resumo
Live no fim de um dia do curso de 5 dias (infraestrutura → bot → filas → workers/skills/agentes → segurança e pagamentos). Ele revisa a arquitetura: o bot recebe a mensagem, um controlador põe na fila já com a lista de skills disponíveis, workers puxam da fila e disparam agentes. Dá a definição de cada peça: agente é programa com IA, worker é programa sem IA, fila é base de dados, skill é *um livro, uma receita*. Defende skills aprovadas como forma de evitar alucinação e ganhar segurança, mas alerta para o risco de baixar skills de origem desconhecida (há mais de 1 milhão no skills.sh). Ao vivo, clona o repositório OKF do Google, erra o nome, procura a fonte certa e manda o agente resumir e publicar uma página no portal. Mostra materiais de pagamento (Asaas, Nubank/Pix) com a conta de taxas e impostos, o publicador de redes que levou ban do Google por falta de reautenticação e fecha dizendo para aprender fundamentos e o que não muda, não a interface da ferramenta da semana.

## Ideias centrais
- Entender a estrutura para ser maestro: "estrutura e ser um maestro de uma" (@00:14:01)
- Fazer rápido sem entender não serve: "de forma superficial e não vai saber" (@00:13:46)
- Skills aprovadas na fila: "Isso faz com que ele não alucine, isso" (@00:15:03)
- Definições das peças: "O worker é um programa sem IA." (@00:34:39) / "programa é o skill, porque o skill é um" (@00:34:28)
- Começar pequeno: "disse? Cria uma fila, cria um worker." (@00:33:39)
- Risco de skill de terceiros: "estar instalando vírus, nós podemos" (@00:16:51)
- Skill elimina o repetitivo: "Porque todo esse trabalho repetitivo eu" (@00:24:10)
- Calcular custo antes de cobrar: "pagamento, tem que calcular esse teu" (@00:27:11)
- Separar gerador de publicador: "separar gerador de conteúdo com, tá," (@00:41:29)
- Aprender o que não muda: "vocês têm que aprender? O que não muda?" (@00:48:28)

## Como ele ensina aqui
- Explica cada peça com uma definição curta e uma analogia (skill como currículo e prova do médico; maestro de orquestra), depois liga tudo num fluxo (entrada → controlador → fila → worker → agente).
- Justifica o curso de 5 dias contra o atalho de "uma hora": o objetivo é saber agir quando der problema, não só gerar o sistema.
- Faz ao vivo e deixa o erro aparecer: `git clone` falha, ele confere quem publicou o repositório antes de baixar (diz que não sabe quem é a empresa) e só então clona a fonte do Google.
- Põe número no custo (taxas de Pix/cartão, 30–40% de impostos, ~R$1.000/mês de infraestrutura) e compara com outros custos de um negócio.
- Mostra a própria falha operacional (ban do Google por não reautenticar o publicador) como lição.

## Ligações
- Temas: [[filas-e-workers]], [[skills]], [[agentes-de-ia]], [[infraestrutura-basica]], [[atendimento-com-agentes]], [[producao-de-video-com-ia]], [[contexto-e-memoria]]
- Princípios: [[automatizar-o-repetitivo]], [[menor-custo-que-resolve]], [[verificar-antes-de-afirmar]], [[fundamentos-antes-de-ferramentas]]
- Métodos: [[arquitetura-bot-fila-worker-skill]], [[live-construindo-ao-vivo]]

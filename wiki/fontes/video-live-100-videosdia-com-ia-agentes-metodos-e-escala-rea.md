# LIVE： 100 Vídeos⧸Dia com IA — Agentes, Métodos e Escala Real

- Tipo: video
- Origem: https://www.youtube.com/watch?v=JuIZH8J36j4
- Arquivo: raw/videos/live-100-videosdia-com-ia-agentes-metodos-e-escala-real.txt

## Resumo
Live em que ele mostra, ao vivo, a "máquina de publicar" que produz ~100 vídeos por dia com avatar: o agente Inema CCB no Telegram recebe uma ideia, gera roteiros para dezenas de públicos (60+, criadores, educadores, pais...), espera aprovação do texto e então gera os vídeos e publica. Daí ele defende que a escala vem de comandar a IA, não de aprender ferramenta por ferramenta. Comenta o vídeo de Boris (Anthropic) sobre cortar 80% do system prompt e conclui *menos contexto, mais inteligência*: CLAUDE.md mínimo, menos skills, entender subagentes. Compara três métodos (BMAD, Superpowers, ECC) e apresenta o fluxo mínimo entender→planejar→executar→verificar→entregar, com a verificação como etapa mais importante. Mostra testes de quantidade de vídeos por canal, avalia modelos locais (Qwen) na própria máquina e fecha com perguntas sobre custo: gratuito não escala, comece local, depois Vercel/GitHub e só então VPS.

## Ideias centrais
- Comandar a IA para trabalhar em escala, não fazer um vídeo por vez: "comandei a Iá e ela tá trabalhando em" (@00:18:06)
- Escala como vantagem competitiva (1 vídeo contra 100): "vendo também. Você fez um vídeo e eu fiz" (@00:18:49)
- Construir sistema em vez de aprender sistema: "gente tem que construir sistema e para" (@00:23:05)
- Aprovação humana do texto antes de gerar em lote: "vídeos. Só que antes ele vai me dar o" (@00:22:46)
- Menos contexto com modelos novos: "certo? Eu tenho que diminuir o cloud MD" (@00:31:11)
- Fluxo entender→planejar→executar→verificar→entregar, com a verificação no centro: "mais importante é o quê? Verificar. É" (@00:32:58)
- Métodos acima de modelos: "usando métodos? Não importa qual é IA," (@00:26:53)
- Pouco tempo para novidade, muito para construir: "tempo do meu dia para ver coisas novas e" (@00:11:31)
- Custo real, o gratuito não escala: "Quem é que corre atrás do gratuito, ele" (@01:06:22)
- Testar a estratégia em vez de supor: "Veja, eu tô fazendo estratégia de teste." (@00:43:53)

## Como ele ensina aqui
- Abre o próprio sistema rodando (Telegram, painel de canais, lista de avatares) e mostra o resultado real — "cada link já foi publicado" — em vez de slides.
- Dispara uma tarefa no começo (`/studio`, prompt viral, 36 vídeos) e volta a ela no meio da live para mostrar o texto pronto e aprovar ao vivo.
- Explica conceito com analogia do cotidiano (criança de 10, jovem de 18, adulto de 40; estagiário x 20 anos de empresa) para justificar prompts mais curtos.
- Põe preço no que mostra (avatar a ~30/mês, Agnes a 4/mês, 8.000 créditos) e separa testar novidade de pagar por ela depois.
- Avalia modelo local na própria máquina com o agente (cabe na memória? gargalo de disco?) e segura a decisão até analisar melhor.

## Ligações
- Temas: [[producao-de-video-com-ia]], [[agentes-de-ia]], [[contexto-e-memoria]], [[skills]], [[custo-de-tokens]], [[llm-local-e-gratis]], [[git-e-deploy]]
- Princípios: [[menor-custo-que-resolve]], [[verificar-antes-de-afirmar]], [[automatizar-o-repetitivo]], [[simplicidade-e-corte]], [[medir-antes-de-acreditar]], [[fundamentos-antes-de-ferramentas]]
- Métodos: [[pipeline-de-video-por-assunto]], [[live-construindo-ao-vivo]]

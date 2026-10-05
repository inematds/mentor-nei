# LIVE： De Prompt a Grafo — A Nova Era dos Agentes de IA

- Tipo: video
- Origem: https://www.youtube.com/watch?v=K1Efjxrllaw
- Arquivo: raw/videos/live-de-prompt-a-grafo-a-nova-era-dos-agentes-de-ia.txt

## Resumo
Live conceitual que anuncia o curso gratuito "Vibe Code do zero" (projetos, Git, Vercel, Supabase, banco de dados). Explica a pirâmide de evolução dos agentes: prompt, contexto, skill, harness, loop e grafo. Uma etapa não elimina a anterior. O loop precisa de critério de sucesso e de regra de abortar para não queimar tokens. O grafo é visto como relações com peso entre nós (exemplos: rotina da manhã medida em tempo, funil de crescimento, projeto de software), o que permite caminhos alternativos e paralelos. Na parte prática, mostra o Inema CCBOT rodando o fluxo "promo avatar": uma ideia vira textos para 12 públicos, depois avatar, reel e publicação, com portão de aprovação, retry de 2 tentativas e /refazer. Abre a planilha de custo do fluxo, em que corrigir um lado fez estourar o outro, e explica como derrubou o custo trocando chamadas de LLM por scripts e rotinas determinísticas. Fecha com dicas de contexto (limpar entre fases, session handoff perto de 40%, statusline).

## Ideias centrais
- A melhor ferramenta é você com estrutura: "terminal. O programa melhor que tu tem é" (você) (@00:01:53); pasta de projetos e "arquivo de orientação para Iá. É isso" (@00:02:08)
- Prompt continua sendo a base: "Ele é a base para contexto e o harness." (@00:06:14); sem contexto o prompt simples não funciona: "meu prompt. Se você não construir isso" (@00:09:12)
- Skill é manual de instrução: "um livro de instrução, é um manual, né?" (@00:09:34). Skill e fluxo são coisas diferentes: "fluxo? O skill é uma ação, o fluxo é um" (conjunto de ações) (@00:47:58)
- Loop custa caro e exige critério: "nós temos problema, isso gasta muito. Se" (@00:10:33); regra de aborto: "dou essa missão 3. Se tu não resolver," (desiste) (@00:15:19); /goal com métrica: "quer atingir? Qual é a tua métrica de" (@00:15:54) "sucesso? E qual é a tua métrica de" (cancelamento) (@00:15:57)
- Loop é frágil, grafo é resiliente: "isolável, é frágil, né? Otimiza uma" (@00:17:46) / "Ele é resiliente porque tu tem vários" (caminhos) (@00:17:54)
- Assinatura subsidiada não dura para sempre, então otimize: "eu tenho que pensar que um dia ele vai" (ser pago) (@00:25:08); como: "eu transformei toda a parte que era de" (inteligência para a rotina) (@00:25:21); "script que quem chama é um script." (@01:14:28)
- Medir mostra efeito colateral: "quê? Porque eu resolvi de um lado," (estourou no outro) (@00:28:16); a direção é previsibilidade: "possível, mais previsível, porque eu tô" (buscando custo) (@00:30:43)
- Hardware é mais barato que tokens: "capacidade é muito mais barato do que eu" (gastar num vídeo) (@01:17:19)
- Contexto enxuto: "Mandei limpar o meu contexto, ó. Sempre" (@00:29:26) que muda de fase; "tiver em 40, vai lá, terminou uma" (tarefa, session handoff) (@01:11:57)
- Automação com portão humano e retry: "duas vezes. Se ele não consegue, falha," (@00:45:29); ele lê no começo: "começando para ver se ele tá fazendo" (legal) (@00:52:49)

## Como ele ensina aqui
- Parte do fundamento antes da ferramenta, com analogias (escola antes da faculdade, juiz e leis, rotina da manhã como grafo com peso em minutos).
- Mostra a própria planilha de custo com números reais, inclusive a piora (+30%), e descreve como trabalha: "Então eu trabalho por fase, melhorando" (@00:31:48), pedindo sempre uma tabela comparativa no fim de cada fase.
- Roda o fluxo de verdade durante a live (status, falha de 2 vídeos, aprovar), em vez de só descrever.
- Ordem de aprendizado explícita: "A primeira coisa, vocês têm que aprender" (a fazer coisas, depois otimizar) (@01:15:39). Dica prática de estudo: "tela dupla, deixa o conteúdo na esquerda" (@01:18:21).

## Ligações
- Temas: [[agentes-de-ia]], [[skills]], [[contexto-e-memoria]], [[fluxos-vs-agentes]], [[custo-de-tokens]], [[execucao-longa]], [[git-e-deploy]], [[producao-de-video-com-ia]]
- Princípios: [[menor-custo-que-resolve]], [[criterio-de-pronto-explicito]], [[medir-antes-de-acreditar]], [[automatizar-o-repetitivo]], [[fundamentos-antes-de-ferramentas]]
- Métodos: [[trocar-llm-por-script-para-cortar-custo]], [[loop-com-criterio-de-sucesso-e-aborto]], [[pipeline-de-video-por-assunto]], [[higiene-de-contexto]]

# LIVE： Bench Studio com 81 Modelos de IA - Instalação do Zero

- Tipo: video
- Origem: https://www.youtube.com/watch?v=tfLpUHmpvFk
- Arquivo: raw/videos/live-bench-studio-com-81-modelos-de-ia-instalacao-do-zero.txt

## Resumo
Live de apresentação e instalação do Bench Studio (versão BR, PT/EN), o estúdio de geração de imagem e vídeo do Nei, que agora tem 81 modelos de vários provedores (Agnes grátis, Kie, Fal, Magnific). Ele explica a arquitetura: o estúdio web na porta 5200 é só uma casca, e a API/servidor na 8787 não fica exposta à internet. Explica também o cálculo de custo antes de gerar, a senha criptografada para acesso remoto, o script que abre e fecha a porta no firewall, os "modos" editáveis sem mexer no código e um MCP para outros sistemas chamarem o motor, que roda um job por vez (para paralelizar, precisa de fila). Durante a demo aparece um bug real: imagem-para-imagem falha sem a chave do Fal. Ele pede a causa raiz ao agente, corrige e testa até funcionar. Depois faz uma instalação do zero numa VPS antiga, que trava em versão de Node e Next. Resolve com o chat, sobe o Node para 24 e manda documentar o comando que funcionou nas instruções de instalação. Fecha com a lição de que VPS desatualizada é o problema mais comum, de que é preciso validar requisitos antes e de que vale aprender o que não muda.

## Ideias centrais
- Ferramenta própria em vez de plataforma paga: "A ideia dela é substituir o Higfields e" (todas essas ferramentas) (@00:02:49); pensada para quem começa: "tá começando ter uma ferramenta para ser" (produtivo) (@00:52:36)
- Custo calculado antes de rodar, base para precificar: "Calculando o preço antes de tu rodar," (@00:12:48); "vou cobrar baseado não no meu tempo, eu" (vou cobrar em cima do custo) (@00:09:34)
- Segurança por camadas: "porque tu não fala com a API, tu fala" (com a página web) (@00:12:34); a API fica só para o estúdio e outras aplicações: "é a API. você não acessa ela, o estúdio" (@00:55:38)
- Limite de concorrência assumido e explícito: "uma limitação. Ele roda um por vez." (@00:10:11); para paralelizar: "tempo, eu vou usar uma fila, né? Ou eu" (@00:10:16); a ideia é ser "que ele seja um serviço para as filas," (@01:16:56)
- Configuração no lugar de código: "certo? Em vez de mexer no código, tu vai" (cadastrando nos modos) (@00:17:40)
- Depuração por causa raiz: o agente responde "causa raiz confirmada. O concerto é" (pequeno) (@00:24:17), e a conclusão: "Ou seja, o falo ali é desnecessário para" (todo mundo que não é Fal) (@00:24:52)
- Erro de instalação vai pro chat, que é tutor: "ó, que que eu sugiro sempre fazer? Marca" (@01:01:32) "aqui e vai pro chat. Eu podia te chamar" (@01:01:41); "Então a, né? O chat é um tremendo de um" (tutor) (@01:04:03)
- Requisito tem que ser validado antes: "ser um pré-requisito, meu amigo." (@01:25:04); o problema mais comum: "vejo, tá? As VPS não estão atualizadas e" (@01:34:52)
- Testar em ambiente zerado, porque no ambiente pronto tudo passa: "que que dá de erro, porque quando tu já" (tem tudo atualizado, tudo dá certo) (@01:56:24)
- Não se apaixonar por modelo; usar o melhor de cada um: "Tu vai analisar, os caras estão tudo" (chutão) (@01:58:20); "melhor de cada um, certo? Onde" (@01:59:28); aprender o que não muda: "vão aprendendo aquilo que não vai mudar." (@02:01:37)

## Como ele ensina aqui
- Instala do zero na frente do público, numa VPS antiga, de propósito, para mostrar os erros que o aluno vai encontrar. Não usa a máquina pronta.
- Quando quebra, cola o erro e o contexto no agente, pede a causa raiz, corrige, refaz o mesmo teste ("pela milésima vez") e só declara resolvido quando a geração passa ("Bingo. Resolvido.").
- Transforma o que deu certo em documentação: "Agora anote que fiz isso e o teu comando" (@01:31:45). Quer log em toda execução: "Certo? Gerando um log aqui. Ou seja," (@01:30:28).
- Pede ao chat comandos simples quando a resposta vem cheia de "linguiça" e explica o ganho: aprender aos poucos e não fazer o que não precisa.
- Diz o tamanho real do trabalho sem esconder: "Imagina, eu fiz isso num em dois dias," (@01:40:33). Por isso existe versão, e o próximo passo é testar antes de liberar: "antes de eu liberar porque senão dá esse" (@01:38:10).

## Ligações
- Temas: [[producao-de-video-com-ia]], [[infraestrutura-basica]], [[git-e-deploy]], [[mcp]], [[filas-e-workers]], [[custo-de-tokens]], [[orquestracao-de-modelos]], [[llm-local-e-gratis]]
- Princípios: [[verificar-antes-de-afirmar]], [[menor-custo-que-resolve]], [[criterio-de-pronto-explicito]], [[fundamentos-antes-de-ferramentas]], [[construir-junto-ao-vivo]], [[medir-antes-de-acreditar]]
- Métodos: [[depurar-ao-vivo]], [[app-na-vps]], [[live-construindo-ao-vivo]]

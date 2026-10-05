# Agentes com LLM grátis (live)

- Tipo: video
- Origem: https://www.youtube.com/watch?v=Zb8TRf97zt8
- Arquivo: raw/videos/transcript.txt

## Resumo
Live curta (cerca de 1 h) sobre como montar e rodar agentes de forma que dê para trocar o modelo, usando LLM grátis. Começa com uma visão de cenário e com a definição de agente (sistemas com liberdade), mostra a arquitetura de um agente avançado (motores LLM trocáveis, roteador de provedores, ferramentas, skills e memória, filas, cron, worker, subagentes, checkpoints) e defende rodar tudo numa VPS persistente em vez da máquina local. Na prática, mostra o DeepSeek Harness (DSH) configurado com OpenRouter e o modelo grátis OX Alpha: como adicionar modelos, definir o modo, o workspace com acesso só leitura × full e como ele descobriu o que o harness lê ao iniciar uma sessão. Mostra o resultado de uma madrugada rodando: nove cursos gerados (ele está revisando e já achou bugs), um curso sobre comandos (INEMA DSL) e clipes musicais feitos sem portão com o projeto musicavideo e o Agnes grátis, ligados ao INEMA CC Bot (cerca de 100 vídeos por dia). Há também um trecho sobre mercado: afiliados no lugar do influenciador pago.

## Ideias centrais
- Definição de agente: "Então, agentes são sistemas com liberdade." (@00:03:07)
- Motores trocáveis, cada um com seu ponto forte: "E cada um deles tem uma característica que torna ele melhor do que os outros." (@00:16:26)
- Entender a engenharia para saber o custo: "eu vou saber quanto combustível eu tenho que dar para esses caras, que é meu dinheiro" (@00:17:11)
- Montar o próprio sistema e trocar as peças: "Simplesmente você vai trocando as peças, vai integrando naquilo que é proposta." (@00:18:04)
- Estudar os harness abertos e criar a própria camada: "Eu crio a minha camada, eu crio o meu modelo." (@00:19:12)
- Não depender de plataforma: "a gente não sabe, então eu uso eles como uma casca, tá bom?" (@00:42:55)
- Filas e workers no centro do agente: "que vai buscar na fila e vai mandar executar pelos subagentes, certo?" (@00:13:10)
- Workspace como limite de segurança: "Esse Workplace é uma área, então ele só trabalha dali para baixo, a da minha segurança." (@00:38:30)
- Comando curto vale mais que textão: "É muito mais fácil a DIA entender um comando do que você escrever um textão que ele tem que interpretar." (@00:45:50)
- Construir é rápido, acertar leva mais: "Depois leva sete dias para a gente consertar ele, para deixar bonitinho e tudo mais." (@01:01:29)

## Como ele ensina aqui
- Mostra a tela de verdade: abre a OpenRouter, compara preços (DeepSeek Flash × Pro, Kimi), copia o slug e configura no harness ao vivo.
- Investiga o próprio agente perguntando a ele: "Quero entender o que você lê quando inicializa uma sessão." (@00:39:35)
- Põe o modelo grátis para rodar a fila parada durante a noite e depois revisa: "Então eu já encontrei alguns buguezinhos e tudo." (@00:33:37)
- Escolhe pelo custo: deixa o modelo caro para casos raros: "Em raro momento eu vou usar ele." (@00:37:04); e usa o grátis porque "que eu não queria gastar os tokens, então, né?" (@00:33:54)
- Mostra o pipeline de produção funcionando (pedido de uma linha → música, capa e clipe), sem portão porque foi pedido assim.

## Ligações
- Temas: [[agentes-de-ia]], [[llm-local-e-gratis]], [[orquestracao-de-modelos]], [[infraestrutura-basica]], [[filas-e-workers]], [[producao-de-video-com-ia]], [[custo-de-tokens]]
- Princípios: [[menor-custo-que-resolve]], [[orquestrar-nao-reinventar]], [[automatizar-o-repetitivo]], [[construir-junto-ao-vivo]], [[independencia-de-plataforma]]
- Métodos: [[pipeline-de-video-por-assunto]], [[live-construindo-ao-vivo]], [[plano-antes-de-gastar-com-portao]]

- Ver também: [[subagentes]]

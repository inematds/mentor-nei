# LIVE： Claude Code - Economize 90% dos Tokens com 3 Comandos

- Tipo: video
- Origem: https://www.youtube.com/watch?v=UJmuJeIt-3E
- Arquivo: raw/videos/live-claude-code-economize-90-dos-tokens-com-3-comandos.txt

## Resumo
Live depois de um dia do curso Vibe Code (pastas, contexto, Git/GitHub, SSH, Vercel, domínio, .env). O centro são três comandos para economizar tokens no Claude Code: `/memory-audit` (acha redundância e decisões que ficaram só na conversa, tira coisa do CLAUDE.md e deixa ponteiros para arquivos), `/session-handoff` (gera um resumo, ele copia, dá `/clear` e cola de volta) e a status line, para ver o contexto o tempo todo. Ao vivo, o contexto cai de 74% para 6% e de 29% para 6%. Depois roda `/doctor`, que acusa 122 skills carregadas (15.000 tokens só a lista) e 48 sem uso: recomenda skill de projeto, não global. Pelo caminho conserta um bug ao vivo (portão que aceitava só HTTP 200 e barrava o 308), mostra uma biblioteca de 1.440 prompts de vídeo hospedada barato (Hugging Face + Vercel) e ensina loops com critério de sucesso/fracasso e limite de tentativas, deixando a execução para workers. Fecha falando de grafos de agentes, harness e negócios feitos para agentes.

## Ideias centrais
- Limite de contexto: "nunca pode deixar passar de 40%." (@00:13:17)
- Os três comandos (memory audit, session handoff, status line) são obrigatórios: "e e o Status Line são três coisas que é" (@00:22:03)
- Por que o token some — a cada comando entra tudo: "ele vai pegar o system prompt, todas" (@00:28:23)
- Disco em vez de memória: "Então, se a informação já tá em disco," (@00:28:13)
- Resultado medido, de 74% para 6% de contexto: "Agora ele gasta só 6%. Se nós pensar que" (@00:29:37)
- Handoff resume em vez de comprimir: "ele vai fazer resumo e não comprimir." (@00:27:48)
- Diagnóstico com /doctor (122 skills carregadas): "carregado o tempo todo. A lista sozinha," (@00:32:54)
- Skill no projeto, não global: "dentro do projeto, eu uso skill do" (@00:33:33)
- Loop precisa de critério e limite: "sucesso e o critério de fracasso, porque" (@00:48:36)
- LLM planeja, worker executa: "execução tu deixa nos worker, tá legal?" (@00:51:08)

## Como ele ensina aqui
- Mede antes e depois na tela: lê o % de contexto, roda o comando e mostra o número cair (74%→6%), convertendo em tokens por chamada.
- Roda a ferramenta no próprio projeto real (inemaccbot) e lê o diagnóstico em voz alta, inclusive as falhas dele (15 decisões duráveis que nunca chegaram à memória).
- Bug ao vivo: abre o site, vê que o portão bloqueia, manda o agente achar a causa (308 tratado como sem acesso) e lê em voz alta o agente admitindo que errou ao dizer que os dois compilavam — confere o que o agente afirma.
- Responde as perguntas do chat aplicando a regra na hora (contexto em 75% → mostra o comando; skill global ou de projeto → explica o critério de manutenção).
- Põe o custo de hospedagem na conta antes de publicar (12 GB de vídeo no Hugging Face, só prompts e interface no Vercel).

## Ligações
- Temas: [[custo-de-tokens]], [[contexto-e-memoria]], [[claude-code]], [[skills]], [[execucao-longa]], [[filas-e-workers]], [[git-e-deploy]]
- Princípios: [[medir-antes-de-acreditar]], [[menor-custo-que-resolve]], [[simplicidade-e-corte]], [[criterio-de-pronto-explicito]], [[verificar-antes-de-afirmar]]
- Métodos: [[higiene-de-contexto]], [[depurar-ao-vivo]], [[live-construindo-ao-vivo]]

# maestro-roteador — triagem de modelo e esforço para Claude Code

Origem: https://inematds.github.io/maestro-roteador/guia/

PT EN ES

O que é

## Dois eixos, duas perguntas, nunca um meio-termo

O maestro-roteador é uma skill de Claude Code: recebe um problema bruto e decide, antes de despachar, qual modelo e qual esforço cada parte do trabalho merece.

### 🎯 Modelo = repertório

Responde uma pergunta só: qual nível de critério o pior passo da tarefa exige? O menor modelo que resolve bem esse passo é o escolhido — nunca "por garantia".

### ⚙️ Esforço = deliberação

Soma ambiguidade + custo do erro. Solução única e erro barato → low. Vários caminhos plausíveis ou erro caro (produção, dado perdido) → high ou mais.

### ⚖️ Erro não negocia, eficiência sim

Quando o risco é de correção, não há opção barata. Quando é só acabamento/gosto, a skill oferece a escolha custo × qualidade e quem decide é o usuário.

### 📊 Referência: esforço na prática →

Dados de terceiros sobre o Opus 5.5 e o GPT-6 Astra em todos os níveis de esforço. Nos dois, o nível máximo não foi o preferido, o que reforça a escada: comece baixo e suba só com evidência. A página também traz a opinião do Nei: medium por padrão, high quando precisar de mais raciocínio, xhigh só em caso extremo. É referência e não muda o procedimento da skill. ( EN · ES )

Como funciona

## Procedimento, sempre nesta ordem

A skill roda inline no turno principal — nunca em um subagente — e segue quatro passos fixos antes de despachar qualquer trabalho.

1. Isola o pior passo → 2. Modelo = o menor que resolve → 3. Esforço = ambiguidade + custo do erro → 4. Volume: testa 1 item antes do lote

### 🪤 Anti-overhead

Tarefa mais barata que a própria triagem não recebe triagem. "Corrige esse typo" vai direto no default do turno.

### 🚨 Risco nomeado = high

Se você mesmo nomeou um risco de produção/perda na justificativa, o esforço mínimo é high. "Medium com cuidado" não existe.

### 🪜 Escada com evidência

Erro barato e reversível? Comece no menor esforço plausível e só suba com evidência de resultado insuficiente — nunca "high por garantia". A escada NÃO vale pra risco irreversível.

### 🎭 Empate de gosto

Quando a estrutura já está garantida por um template/skill e só falta acabamento, a triagem apresenta o par custo×qualidade e deixa o usuário escolher.

Economia

## Cache: o custo escondido da troca de modelo

O prompt cache é por modelo e depende do prefixo do contexto. Perder o cache de um contexto de 100k tokens torna a próxima entrada ~12,5× mais cara (gravação 1,25× vs. leitura 0,1×). A matriz de triagem precisa respeitar isso.

### 🧱 Troca só em fronteira

Trocar o /model do turno principal joga fora o cache acumulado. Faça a troca só em fronteira de trabalho (fim de fase, handoff) — nunca no meio de um bloco. Em contexto grande, a troca pode custar mais que a economia do modelo menor.

### 🤖 Subagente é grátis em cache

Cada Agent/Workflow tem contexto próprio: rotear uma parte pra um modelo menor via subagente NÃO toca o cache principal. É o caminho preferido pra aplicar a matriz sem custo de troca.

### 🚫 Sem keepalive artificial

Nunca mandar "ainda está aí?" só pra segurar o cache — o Claude Code gerencia o cache sozinho e o ping custa mais do que salva. Pausa longa? Handoff enxuto e deixe expirar.

### 📋 Rotina que preserva cache

Trabalhe em blocos contínuos (planejar → executar → testar → documentar), mantenha o começo do contexto estável (não ligar/desligar ferramentas e MCPs no meio do bloco) e concentre tarefas relacionadas na mesma sessão.

### ⏸️ Pausas

Pausa curta: continue normal. Pausa longa ou troca de tarefa: handoff curto (objetivo, estado, decisões, próximo passo) + contexto novo. Na API direta, chamadas espaçadas por 10–50 min pagam o cache de TTL 1h (gravação 2×).

Perspectiva

## Harness > esforço: onde o resultado nasce de verdade

Num teste real com a mesma tarefa em 12 níveis de esforço e 2 providers, os resultados funcionais foram quase idênticos — os níveis altos adicionaram um favicon e sombras, por 2–5× os tokens. O que muda o resultado não é o slider de esforço.

### 📝 Spec clara vence esforço alto

Um prompt que diz exatamente o que "pronto" significa entrega em low o que o esforço max tenta adivinhar. Esforço não compensa especificação vaga.

### 🛠️ O modelo é um cérebro num pote

Ferramentas, arquivos, terminal, skills e instruções — o harness — são os braços do modelo. Investir no harness rende mais que subir esforço.

### 🧠 Esforço demais atrapalha

Overthinking é o excesso do próprio eixo esforço: deliberação sobrando em tarefa simples re-explora caminhos já decididos e pode piorar o resultado, não só encarecer. O esforço certo é o menor que cobre o risco — acima disso você compra ruído, não segurança.

Pré-requisitos

## O que precisa estar no ar

Só isso: Claude Code instalado e a skill disponível em ~/.claude/skills/ (usuário) ou .claude/skills/ (projeto).

### Claude Code

CLI com suporte a skills e a chamadas Agent/Workflow com parâmetros model / effort .

```
# confirma instalação
claude --version
```

### Git

Pra clonar o repo e criar o symlink de instalação.

```
# confirma git
git --version
```

### Nenhuma dependência extra

Sem serviço externo, sem chave de API, sem build. É markdown puro lido pelo Claude Code.

```
# conteúdo da skill
skills/maestro-roteador/SKILL.md
```

Guia de uso · passo a passo

## Instalar e usar a triagem

Instalação por symlink (pra receber atualizações do repo automaticamente) e três formas de acionar a triagem.

1

### Clone o repo

Baixa a skill.

```
git clone https://github.com/inematds/maestro-roteador.git
```

2

### Instale via symlink (usuário)

Fica disponível em qualquer projeto e recebe atualizações do repo sem reinstalar.

```
ln -sfn "$(pwd)/maestro-roteador/skills/maestro-roteador" ~/.claude/skills/maestro-roteador  # symlink de usuário
```

3

### Ou copie só pra um projeto

Sem symlink, direto na pasta de skills do projeto (não recebe atualizações automáticas).

```
cp -r maestro-roteador/skills/maestro-roteador .claude/skills/  # skill só deste projeto
```

4

### Peça a triagem diretamente

Frases-gatilho: "qual modelo", "quanto esforço", "faz a triagem disso".

```
"Faz a triagem disso: renomear 80 arquivos em lote seguindo um padrão."  # -> haiku + low
```

5

### Ou só peça o trabalho normalmente

Ao despachar subagentes/workflows, a skill aplica a matriz sozinha e distribui cada parte com model e effort corretos — sem você precisar pedir a triagem à parte.

```
"Migra esses dados de produção pro schema novo."  # -> sonnet + high (risco nomeado)
```

6

### Leia o plano de despacho

A saída sempre vem no mesmo formato YAML, com o pior passo e o risco explicitados por parte.

```
tarefa: <resumo>
partes:
  - o_que: <subtarefa>
    pior_passo: <qual e por quê>
    modelo: haiku|sonnet|opus|fable
    esforco: low|medium|high|xhigh|max
    risco: <custo do erro em 1 linha>
turno_principal: <recomendação de /model, se valer trocar>
```

Validação

## TDD de skill: baseline vs. com a skill

A skill foi escrita contra um baseline medido: sem ela, agentes colapsam qualquer tarefa em "sonnet + medium". Com ela, os três cenários de teste foram pro canto certo da matriz.

Cenário Sem skill Com skill

Renomear 80 arquivos em lote sonnet + medium haiku + low

Roteiro com voz de marca sonnet + medium fable + low

Migração de dados com produção em risco sonnet + medium sonnet + high

### 💡 Por que isso importa

O meio-termo genérico "sonnet+medium pra tudo" paga demais em tarefas mecânicas e de menos em tarefas com risco real — os três cenários mostram os dois erros ao mesmo tempo.

### 🧪 Como testar você mesmo

Rode "sem skill" (desative-a) e "com skill" no mesmo pedido bruto e compare o modelo/esforço escolhido — é exatamente o teste que validou os três cenários acima.

Roadmap

## Estado atual e limite conhecido

Projeto de pesquisa/educação INEMA — sem roadmap formal de features; o que existe hoje e o limite documentado da skill.

Hoje

Skill funcional, validada contra baseline Regras de decisão, tabela rápida, armadilhas comuns e formato de saída definidos em SKILL.md, testados nos três cenários acima.

Automático

Subagentes e workflows Para chamadas Agent/Workflow, a decisão de model/effort é automática — a skill aplica a matriz sem precisar ser chamada explicitamente.

Limite

Conversa principal só recomenda Para o modelo do turno principal, a skill apenas sugere — a troca de fato é sempre do usuário via /model.

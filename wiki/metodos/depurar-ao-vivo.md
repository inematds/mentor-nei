# Depurar ao vivo

- Tipo: metodo

## O que é

Erro em aula é material de ensino: ele deixa quebrar na frente da turma, leva a mensagem com contexto ao chat/agente, testa uma hipótese por vez, refaz o mesmo teste e documenta o que resolveu.

## Passos

### Depurar ao vivo

1. Deixar o erro acontecer (às vezes pulando o pré-requisito de propósito)
2. Copiar a mensagem de erro com o contexto de antes
3. Levar ao chat e pedir a causa em vez de ficar tentando no escuro
4. Formular a hipótese e aplicar o contorno (ex.: túnel SSH para o localhost, corrigir a barra, mandar o agente usar SSH)
5. Conferir o resultado real (ls -la, refresh no GitHub), não o OK da ferramenta
6. Documentar a dica no material do curso

### Depurar ao vivo com o chat

1. Selecionar o erro e um pouco do que estava fazendo
2. Colar no chat ou agente (vai e vem entre as duas telas)
3. Pedir a causa raiz e uma correção pequena ou um comando simples
4. Aplicar e refazer exatamente o mesmo teste até passar
5. Mandar anotar o que funcionou nas instruções de instalação e de troubleshooting

### Depurar ao vivo: ler o erro, isolar o ambiente, corrigir e registrar

1. Reproduzir na frente da turma, de preferência numa máquina limpa
2. Ler a mensagem de erro e passar para o agente diagnosticar
3. Testar uma hipótese por vez (caminhos, token, .env, permissões)
4. Comparar com um ambiente que funciona (ex.: Ubuntu 24.04 vs 26) para isolar a causa
5. Corrigir e conferir a correção (o agente às vezes afirma o que não verificou)
6. Transformar a falha em melhoria permanente (script de instalação, arquivo default)

## Exemplos (trechos)

- "Por isso que eu gosto que dá erro, né?" (@00:58:41) — [[video-inema-vibecode-do-zero-dia-3-basico-de-infra]] `raw/videos/inema-vibecode-do-zero-dia-3-basico-de-infra.txt`
- "um procedimento para resolver os erros." (@02:37:09) — [[video-inema-vibecode-do-zero-dia-3-basico-de-infra]] `raw/videos/inema-vibecode-do-zero-dia-3-basico-de-infra.txt`
- "problema quando dá, levam pro chat e às" (@02:54:17) — [[video-inema-vibecode-do-zero-dia-3-basico-de-infra]] `raw/videos/inema-vibecode-do-zero-dia-3-basico-de-infra.txt`
- "usa o SSH, usa o SSH para você" (@02:45:21) — [[video-inema-vibecode-do-zero-dia-3-basico-de-infra]] `raw/videos/inema-vibecode-do-zero-dia-3-basico-de-infra.txt`
- "ó, que que eu sugiro sempre fazer? Marca" (@01:01:32) — [[video-live-bench-studio-com-81-modelos-de-ia-instalacao-do-z]] `raw/videos/live-bench-studio-com-81-modelos-de-ia-instalacao-do-zero.txt`
- "causa raiz confirmada. O concerto é" (@00:24:17) — [[video-live-bench-studio-com-81-modelos-de-ia-instalacao-do-z]] `raw/videos/live-bench-studio-com-81-modelos-de-ia-instalacao-do-zero.txt`
- "Agora anote que fiz isso e o teu comando" (@01:31:45) — [[video-live-bench-studio-com-81-modelos-de-ia-instalacao-do-z]] `raw/videos/live-bench-studio-com-81-modelos-de-ia-instalacao-do-zero.txt`
- "pergunto pro chat. Vai e vem, vai e vem." (@00:58:35) — [[video-live-deepseek-harness-orquestre-ias-e-corte-custos-em-]] `raw/videos/live-deepseek-harness-orquestre-ias-e-corte-custos-em-95x.txt`
- "É fácil quando tudo dá certo." (@00:55:27) — [[video-live-empresa-agentica-agentes-de-ia-no-comando-do-nego]] `raw/videos/live-empresa-agentica-agentes-de-ia-no-comando-do-negocio.txt`
- "para mim identificar os erros, senão o" (@01:03:48) — [[video-live-empresa-agentica-agentes-de-ia-no-comando-do-nego]] `raw/videos/live-empresa-agentica-agentes-de-ia-no-comando-do-negocio.txt`
- "Por isso é bom ter duas, três VPS é pra" (@00:55:51) — [[video-live-empresa-agentica-agentes-de-ia-no-comando-do-nego]] `raw/videos/live-empresa-agentica-agentes-de-ia-no-comando-do-negocio.txt`
- "Vou melhorar essa instalação. Vou criar" (@00:37:18) — [[video-live-empresa-agentica-agentes-de-ia-no-comando-do-nego]] `raw/videos/live-empresa-agentica-agentes-de-ia-no-comando-do-negocio.txt`
- "Corrigido nos três repos. Causa. O Inema" (@00:12:04) — [[video-live-claude-code-economize-90-dos-tokens-com-3-comando]] `raw/videos/live-claude-code-economize-90-dos-tokens-com-3-comandos.txt`

## Fontes

- [[video-inema-vibecode-do-zero-dia-1-infra-git-e-vercel]] — INEMA  VibeCode do Zero - Dia 1 - Infra Git e Vercel
- [[video-inema-vibecode-do-zero-dia-3-basico-de-infra]] — INEMA  VibeCode do Zero - Dia 3 -  Basico de Infra
- [[video-live-bench-studio-com-81-modelos-de-ia-instalacao-do-z]] — LIVE： Bench Studio com 81 Modelos de IA - Instalação do Zero
- [[video-live-claude-code-economize-90-dos-tokens-com-3-comando]] — LIVE： Claude Code - Economize 90% dos Tokens com 3 Comandos
- [[video-live-deepseek-harness-orquestre-ias-e-corte-custos-em-]] — LIVE： DeepSeek Harness - Orquestre IAs e Corte Custos em 95x
- [[video-live-empresa-agentica-agentes-de-ia-no-comando-do-nego]] — LIVE： Empresa Agêntica - Agentes de IA no Comando do Negócio
- [[video-live-inemaccbot-fluxos-vs-agentes-de-ia-de-us-3-a-zero]] — LIVE： INEMACCBOT Fluxos vs Agentes de IA — De US$3 a Zero por Vídeo

## Relacionados

[[menor-custo-que-resolve]], [[custo-de-tokens]], [[live-construindo-ao-vivo]], [[verificar-antes-de-afirmar]], [[infraestrutura-basica]], [[git-e-deploy]]

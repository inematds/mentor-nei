# Diário do piloto — mentor nei (kit 1.1.0)

| hora | fase | o que aconteceu | esperado | gravidade | ideia de correção |
|---|---|---|---|---|---|
| 2026-10-05 | 1 Coleta | skill manda "um subagente por fonte em paralelo", mas `registrar_item` (_comum.py) faz read-modify-write do MANIFESTO.json sem lock → paralelo perde entradas. Rodei os coletores em sequência. | paralelo seguro | alta | `fcntl.flock` em volta da leitura+escrita do manifesto, ou a skill paraleliza só o download e registra em série |
| 2026-10-05 | 1 Coleta | vídeo Zb8TRf97zt8 (Agentes com LLM grátis) sem legenda pt/pt-orig; `transcrever_cmd` vazio → falha | transcrição local | média | preencher `transcrever_cmd` com inemavox/Whisper local (teto de memória + timeout) |
| 2026-10-05 | 1 Coleta | 6 guias = 7269 pal., meta 8000 → stats exit 1. Coletor ok (makeshorts: 885 coletadas vs 936 visíveis no HTML). Guias INEMA têm ~900–1400 pal. cada | meta batida com as fontes do ESCOPO | baixa | meta de guia calibrada por tamanho real (~1200 pal./guia) ou ESCOPO com 7+ guias |
| 15:50 | 1 coleta | Agente não usou subagente por fonte: `registrar_item` reescreve o MANIFESTO inteiro sem trava, paralelo perderia entradas. Rodou em sequência e explicou. | 1 subagente por fonte em paralelo | média | trava de arquivo (flock) + escrita atômica no manifesto; teste de concorrência |
| 15:50 | 1 coleta | Meta de guia (8000 pal.) reprovou: guias INEMA têm 900–1400 pal. cada. Agente reportou exit 1 sem maquiar e sugeriu fontes extras. | metas realistas | baixa | `stats.py` mostrar quanto falta por meta; docs: calibrar meta depois de listar as fontes |
| 15:50 | 1 coleta | 1 live sem legenda e `transcrever_cmd` vazio → foi para RELATORIO-FALHAS (comportamento correto). | idem | ok | — |
| 15:50 | 1 coleta | 13 lives = 169.937 palavras em 1,6 min (só legendas, sem baixar vídeo). | — | ok | — |
| 16:05 | 1 coleta | Transcrição local (inemavox, large-v3) da live sem legenda: 8.045 pal. em 7,7 min. Mas o arquivo virou `raw/videos/transcript.txt` (nome do transcritor, não do vídeo): a próxima transcrição sobrescreve e o manifesto perde o item anterior. | nome único por vídeo | alta | nomear pelo título/ID do vídeo (yt-dlp --print) ou hash da URL, nunca pelo nome do arquivo do transcritor |
| 16:05 | 1 coleta | Fase 1 aprovada após +1 guia e a transcrição: 21 itens, 187.382 palavras, stats exit 0. | — | ok | — |
| 16:15 | 2 wiki | /nei-compilar: 5 subagentes por lote, 3,3 min, 73 páginas, 1223 links, validar_links exit 0, raw intacto. Hot reconhecível (verificar antes de afirmar 17 fontes; menor custo 16; medir 14; critério de pronto 10). Nota 8/10. | — | ok | — |
| 16:15 | 2 wiki | Trechos de vídeo picados ("brilhante. Cuidado para vocês não"): a legenda quebra a fala em linhas com [hh:mm:ss]; citação que cruza linhas tem o timestamp no meio do texto. | trecho com sentido completo | média | coletar_video juntar linhas em parágrafos (marca de tempo a cada ~30 s) e normalizar() ignorar [hh:mm:ss] |
| 16:25 | 3 regras | /nei-regras: 1,1 min, 8 regras ativas, 31 citações, validador OK de primeira. A sessão detectou sozinha o problema das legendas cruzando linha e usou citações curtas. Descartou um trecho que contradizia a wiki (bom). Nota "reconheço o Nei": 8/10. | — | ok | — |
| 16:25 | 3 regras | As regras do Nei pedem seções próprias (Custo, Sua vez, Por baixo, Risco), mas o agente do template tem loop fixo (Pronto, Menor versão…) e validar_resposta exige as seções fixas. | loop do agente derivado das regras | média | skill /regras gerar também `secoes_resposta` no config + bloco do loop no agente (ou o agente ler "no mentor:" de cada regra) |
| 16:25 | 3 regras | Teste negativo (citação inventada) → `1 faltando`, exit 1. OK. | — | ok | — |
| 16:35 | 4 portão | Sessão real `claude -p`: Write de teste_portao.py → Stop bloqueado com "Você escreveu código e não rodou: teste_portao.py…". Como o pedido dizia "não rode", o agente explicou e encerrou no 2º Stop (stop_hook_active) — 1 bloqueio por turno, como desenhado. | bloquear | ok | — |
| 16:35 | 4 portão | O Claude Code rotula o bloqueio como "Stop hook error occurred" na interface: parece erro do kit. | mensagem clara | baixa | documentar no README/guia que esse aviso é o portão funcionando |
| 16:45 | 5 teste 2 | /nei-revisa (1,8 min, 1 subagente): reproduziu o UnicodeEncodeError com cp1252, achou um 2º ponto de quebra que eu não tinha previsto (🤔 dentro do JSON de entrada → tirar emoji do código não basta), corrigiu com `sys.stdout.reconfigure(errors="replace")`, enxugou 38→25 linhas e provou lado a lado (md5 do relatório igual). Original intacto. | prever, reproduzir, provar | ok | — |
| 16:45 | 5 teste 2 | Não há previsão escrita ANTES da primeira execução em cp1252 (log: cat/grep → já roda). O passo "preveja" da skill revisa não é verificado. | previsão antes de rodar | média | skill revisa: exigir seção "Previsão" antes de qualquer execução; validar_resposta com perfil "revisao" |
| 16:45 | 5 teste 2 | Salvou como `script_emoji.revisado.py` (a skill diz sufixo `.revisado`, que deixaria o arquivo sem .py) e usou /tmp fora do projeto. | — | baixa | skill: nomear `<nome>.revisado.<ext>`; usar `.mentor/tmp/` |
| 16:50 | 5 teste 1 | /nei-ensina "hook Stop que bloqueia com TODO.md aberto" (0,9 min + subagente): Pronto → menor versão → previsão → saída real → versão quebrada (v0 em loop infinito quando item depende de terceiro; 6/6 bloqueios) → correção (teto de 3) → teste numa sessão real → "Sua vez" (exercício, vindo da R6) → relatório com R1–R8. validar_resposta com transcript: 14 Bash, exit 0. Aprendi: o bloqueio sem teto prende a sessão para sempre quando o item não depende do agente. | — | ok | — |
| 16:50 | 5 teste 1 | Resumo final da sessão saiu em inglês (a lição em PT). | idioma do usuário | baixa | agente/skill: "responda no idioma do pedido" |
| 16:50 | 5 teste 1 | Gravou o código em ~/projetos/output/hook-todo-stop (seguiu a regra global da máquina), fora do projeto do mentor. | — | ok | — |
| 17:00 | 5 teste 3 | /nei-ingere guia agente-claude-codex (2,4 min): fonte nova, 2 métodos novos, R9 e R10 criadas já ativas (2ª fonte existia no raw), R1/R2/R6 reforçadas, index/hot/log atualizados; 3 validadores exit 0. | — | ok | — |

## Placar

| Critério | Resultado |
|---|---|
| Fases 1–3 com exit 0 | ✅ (fase 1 após calibrar a meta e +1 fonte) |
| Portão: bloqueou certo, sem bloqueio indevido | ✅ |
| Teste 1 passou e eu aprendi algo | ✅ (teto de bloqueio por sessão em hook Stop) |
| Teste 2 previu, reproduziu e provou | ⚠️ reproduziu e provou; previsão não escrita antes de rodar |
| Teste 3 atualizou a wiki sozinho | ✅ |
| Nota "reconheço a pessoa nas regras" (0–10) | 8 |
| Tempo total (humano / máquina) | ~1h20 operando / ~20 min de sessões + 7,7 min de transcrição |

**Decisão (pelo PILOTO.md): 4/5 e nota 8 → corrigir os itens do diário numa versão nova do kit e repetir só o teste 2.**

### Correções para o kit 1.2 (do diário)
1. alta — transcrição salva com nome do transcritor (`transcript.txt`): sobrescreve e some do manifesto
2. média — manifesto sem trava: coleta em paralelo perde entradas
3. média — legenda em linhas curtas com [hh:mm:ss]: citações picadas e não casam entre linhas
4. média — loop/seções do agente fixos; regras do especialista pedem seções próprias
5. média — revisa não exige previsão antes de rodar
6. baixa — stats não mostra quanto falta na meta; metas calibradas depois de listar as fontes
7. baixa — "Stop hook error occurred" parece erro: documentar
8. baixa — responder no idioma do pedido; revisado com extensão; tmp dentro do projeto

## Repetição do teste 2 com o kit 1.2

| hora | fase | o que aconteceu | esperado | gravidade | ideia de correção |
|---|---|---|---|---|---|
| 17:40 | 5 teste 2 (rodada 2) | Revisão completa em 5 seções, mas o mentor rodou em cp1252 ANTES de escrever a previsão ("Vou ler… sem executar nada" → executa → "A previsão se confirmou"). O validador externo (`--transcript`) reprovou. A sessão principal disse "o validador passa" porque o rodou SEM o log. | previsão visível antes de rodar | média | — |
| 17:50 | 5 teste 2 (rodada 3) | Com a instrução explícita "escreva uma linha `Previsão:` antes do primeiro comando que executa código": mesmo comportamento (prevê no raciocínio, escreve "a previsão bateu" depois). Validador reprovou de novo. | idem | média | **instrução não basta: precisa de mecanismo** → portão de previsão (PreToolUse em Bash: comando que executa código sem `Previsão:` escrita antes → bloqueia). Fica para o kit 1.3 (2 tentativas sem avanço; não insistir num 3º ciclo). |

**Placar final do piloto:** 4/5 (teste 2 parcial: reproduz, corrige e prova lado a lado, mas não escreve a previsão antes de rodar). Nota 8. O que o kit ganhou com isso: o verificador externo detecta a falha que a própria sessão declarou como OK.

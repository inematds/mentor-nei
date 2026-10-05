# Resultados dos testes de aceitação — piloto mentor nei (kit 1.1.0)

| data | teste | passou? | evidência (arquivo/saída) | observação |
|---|---|---|---|---|
| 2026-10-05 | 1 Construir e ensinar | sim | `testes/respostas/2026-10-05-hook-stop-todo.md`; `validar_resposta.py --transcript logs/teste1.jsonl` → 14 Bash, exit 0 | versão quebrada real (loop infinito), teste numa sessão real, "Sua vez" vindo da R6 |
| 2026-10-05 | 2 Revisar script "que funciona" | parcial | `logs/teste2.jsonl`; `script_emoji.revisado.py` roda em cp1252, md5 do relatório igual ao original | reproduziu e provou lado a lado, achou 2º ponto de quebra; **sem previsão escrita antes de rodar** |
| 2026-10-05 | 3 Ingerir fonte nova | sim | `wiki/log.md` (linha nova), stats/links/citações exit 0, 22 fontes, 10 regras / 40 citações | R9 e R10 novas já ativas; R1, R2, R6 reforçadas |

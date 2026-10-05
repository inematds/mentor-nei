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

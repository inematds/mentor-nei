# Revisão — testes/aceitacao/script_emoji.py (2026-10-05)

## Previsão

Escrita **antes** de qualquer execução, só lendo o script e o `comentarios.json` (R2, R8):

- **Onde quebra.** Num terminal sem UTF-8 (`PYTHONIOENCODING=cp1252`, um console antigo do Windows, ou a saída redirecionada para arquivo ou pipe no Windows), o `print` da linha 28 tenta escrever `🔎`. Ele não existe em cp1252, então vem `UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f50e'` e exit 1.
- **Perda silenciosa.** O `write_text` está na linha 32, **depois** dos prints. Se o terminal quebrar, o `relatorio.txt` não é gravado e a saída útil se perde.
- **Armadilha nos dados reais.** O comentário do `edu` traz `🤔` e é impresso na linha 31. Tirar só os emojis decorativos **não basta**: é preciso proteger a saída do terminal.
- **Esperado no UTF-8:** 5 comentários e 3 perguntas (ana, caio, edu).
- **O que não quebra.** O caminho (`__file__`, funciona de qualquer cwd) e a rede (não usa nenhuma).
- **Fora do escopo, só aponto.** Sem `comentarios.json`, dá traceback de `FileNotFoundError`. Um item sem `"texto"` dá `KeyError`.
- **Corte (R7).** Os emojis decorativos, a função `carregar()` de uma linha e o laço com `append`, que vira uma comprehension.
- **Quem recebe aceitaria?** Não. Funciona no terminal do autor e quebra no Windows/CI sem deixar o relatório.

## Reprodução

```
$ PYTHONIOENCODING=cp1252 python3 testes/aceitacao/script_emoji.py
  File ".../script_emoji.py", line 28, in main
    print(f"\U0001f50e lendo {len(comentarios)} coment�rios�")
UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f50e' in position 0: character maps to <undefined>
exit=1
ls: cannot access 'testes/aceitacao/relatorio.txt': No such file or directory
```

Com `ascii`, o erro é o mesmo: `'ascii' codec can't encode character '\U0001f50e'`, exit 1, sem relatório.

Prova da armadilha nos dados: imprimir só o texto do `edu` em cp1252 também quebra.

```
UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f914' in position 33
exit=1
```

**A previsão acertou** o erro, a linha, o exit code e a ausência do relatório.

## Correção

Arquivo: `testes/aceitacao/script_emoji.revisado.py` (o original não mudou).

| Mudança | Por quê |
|---|---|
| `sys.stdout.reconfigure(errors="replace")` | Um caractere que o terminal não suporta vira `?` em vez de derrubar o script. Isso cobre também o emoji que vem nos dados. |
| `write_text` antes dos `print` | Se a tela falhar por qualquer motivo, o relatório já está gravado. |
| Sem os emojis decorativos (🔎 ❓ ✅) e `…` virou `...` | Eram enfeite e não agregavam nada à saída (R7). |
| `carregar()` foi inlinado e `perguntas()` virou uma comprehension | Ficam menos linhas para ler (de 38 para 31). |
| O arquivo continua em `encoding="utf-8"` | O relatório preserva o 🤔 do dado original. |

## Lado a lado

Mesma entrada (`comentarios.json`), cada `relatorio.txt` copiado para `.mentor/tmp/emoji/`:

| Execução | exit | relatório |
|---|---|---|
| original, utf-8 | 0 | 3 perguntas |
| original, cp1252 | 1 (`UnicodeEncodeError`) | não gravado |
| original, ascii | 1 (`UnicodeEncodeError`) | não gravado |
| revisado, utf-8 | 0 | 3 perguntas |
| revisado, cp1252 | 0 | 3 perguntas (tela: `🤔` virou `?`) |
| revisado, ascii | 0 | 3 perguntas (tela: `á`, `ç` e `🤔` viraram `?`) |

```
diff original(utf-8) x revisado(utf-8/cp1252/ascii)
utf-8: identico
cp1252: identico
ascii: identico
528019359831db71…  script_emoji.utf-8.txt
528019359831db71…  script_emoji.revisado.{utf-8,cp1252,ascii}.txt
```

A saída útil (o `relatorio.txt`) é byte a byte igual nos 4 casos que gravaram. A tela mudou só no enfeite.

## Relatório

| Passo | O que rodou | O que saiu | Regra que guiou |
|---|---|---|---|
| 1. Prever | nada (só leitura do script e do JSON) | cp1252 quebra na l.28 e não grava o relatório; o emoji dos dados também quebra | R2, R8 |
| 2. Reproduzir | `PYTHONIOENCODING=cp1252 python3 testes/aceitacao/script_emoji.py` | `UnicodeEncodeError '\U0001f50e'`, exit 1, sem relatório | R1 |
| 3. Testar a armadilha | print do texto do `edu` em cp1252 | `UnicodeEncodeError '\U0001f914'`, exit 1 | R1, R8 |
| 4. Corrigir e cortar | `script_emoji.revisado.py` | `errors="replace"`, grava antes de imprimir, sem enfeite, 38 → 31 linhas | R7 |
| 5. Lado a lado | os dois scripts × utf-8, cp1252 e ascii, mais `diff` e `sha256sum` | o revisado dá exit 0 nos 3 e o relatório é idêntico ao original (sha 5280…4ea2) | R1, R3 |

Não conferido: o console real do Windows (o teste simulou com `PYTHONIOENCODING`).

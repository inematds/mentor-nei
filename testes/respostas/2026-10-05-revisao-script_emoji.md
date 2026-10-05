# Revisão — `testes/aceitacao/script_emoji.py`

Data: 2026-10-05 · perfil: revisão · temporários em `.mentor/tmp/` · nenhuma API externa · sem commit.

## Previsão

Escrita lendo o código, **antes de qualquer execução** (R3: espero o número primeiro e comparo depois).

**Quem recebe aceitaria? Não.** O script só funciona onde o stdout é UTF-8. Ele quebra *antes* de gravar o relatório, então quem recebe fica sem nada.

1. **Codificação do terminal (falha principal).** A linha 28 imprime `🔎`. Com stdout em cp1252, que é o padrão do Windows quando a saída vai para arquivo, pipe ou agendador, espero `UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f50e' in position 0`, com exit 1 e **sem `relatorio.txt`**, porque a escrita fica na linha 32, depois do print.
2. **Os dados também têm emoji.** O comentário de `edu` termina em `🤔?`. Cortar só os emojis decorativos não basta, porque o `print` da pergunta também quebraria. É preciso proteger o stdout.
3. **ASCII estrito** (`PYTHONIOENCODING=ascii`, alguns contêineres e CI): quebra até no `á` de "comentários".
4. **Dados reais sem validação (R8):** item sem `"texto"` dá `KeyError`, `null` dá `AttributeError`, arquivo vazio dá `JSONDecodeError` com traceback cru, e um objeto no lugar de lista faz o laço iterar sobre as chaves.
5. **Caminho:** `Path(__file__).with_name` funciona a partir de qualquer cwd (isso está certo). Mas a entrada e a saída são fixas, e uma pasta somente leitura dá `PermissionError`. **Rede:** não usa, então não há risco.
6. **O que eu cortaria (R7):** os emojis decorativos e a frase "Funciona no terminal do autor" da docstring.

Número esperado com UTF-8: **3 perguntas** (ana, caio e edu).

## Reprodução

```
$ PYTHONIOENCODING=cp1252 python3 testes/aceitacao/script_emoji.py; echo "exit=$?"
Traceback (most recent call last):
  File ".../testes/aceitacao/script_emoji.py", line 38, in <module>
    sys.exit(main())
  File ".../testes/aceitacao/script_emoji.py", line 28, in main
    print(f"\U0001f50e lendo {len(comentarios)} coment�rios�")
  File "/usr/lib/python3.12/encodings/cp1252.py", line 19, in encode
UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f50e' in position 0: character maps to <undefined>
exit=1
$ ls testes/aceitacao/relatorio.txt
ls: cannot access 'testes/aceitacao/relatorio.txt': No such file or directory
```

Ponto 2 (emoji nos dados):

```
$ PYTHONIOENCODING=cp1252 python3 -c 'print("Onde baixo o arquivo de exemplo? 🤔?")'
UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f914' in position 33: character maps to <undefined>
exit=1
```

Ponto 3 (ASCII): `UnicodeEncodeError: 'ascii' codec can't encode character '\xe1' in position 8`.
Ponto 4 (item sem `texto`, numa cópia do original em `.mentor/tmp/`): `KeyError: 'texto'`, exit 1.

**A previsão acertou:** mesma linha (28), mesmo caractere, mesma posição, exit 1 e relatório não criado. Os pontos 2, 3 e 4 também se confirmaram (R1: só afirmo o que rodou).

## Correção

Arquivo novo: `testes/aceitacao/script_emoji.revisado.py`. O original não foi alterado.

| Mudança | Por quê |
|---|---|
| `sys.stdout.reconfigure(errors="replace")` | Num terminal sem UTF-8, o caractere vira `?` na tela e o programa não quebra. Isso resolve também o emoji que vem nos dados. O arquivo continua em UTF-8 completo. |
| Emojis decorativos e `…` removidos, docstring sem "funciona no terminal do autor" | Eram decoração que não pagava o custo (R7). |
| `carregar()` confere arquivo, JSON, lista e `texto` string | Falha cedo, com mensagem de uma linha e exit 1, em vez de traceback (R8). |
| Entrada e saída opcionais via argv (os padrões continuam os mesmos) | Permite rodar com outros dados e gravar em outra pasta. |

Prova do fix:

```
$ PYTHONIOENCODING=cp1252 python3 testes/aceitacao/script_emoji.revisado.py testes/aceitacao/comentarios.json .mentor/tmp/rev_cp1252.txt
lendo 5 coment�rios
- Como fa�o isso no Windows?
- Funciona com Python 3.9?
- Onde baixo o arquivo de exemplo? ??
3 perguntas salvas em rev_cp1252.txt
exit=0
$ PYTHONIOENCODING=ascii python3 ... .mentor/tmp/rev_ascii.txt
lendo 5 coment?rios
...
3 perguntas salvas em rev_ascii.txt
exit=0
```

(O `�` aparece porque o meu terminal é UTF-8 e está exibindo bytes cp1252. Num console cp1252 de verdade, o `á` aparece certo.)

Entradas ruins:

```
erro: não consegui ler .mentor/tmp/vazio.json: Expecting value: line 1 column 1 (char 0)   exit=1
erro: .mentor/tmp/obj.json deve conter uma lista de comentários                             exit=1
erro: comentário 0 sem campo 'texto' do tipo string                                          exit=1
erro: não consegui ler .mentor/tmp/inexistente.json: [Errno 2] No such file or directory     exit=1
```

## Lado a lado

Mesma entrada (`comentarios.json`), ambiente UTF-8. Os dois gravam `relatorio.txt` no mesmo lugar, então copiei cada resultado para `.mentor/tmp/` e apaguei o arquivo antes de rodar o próximo.

```
$ python3 testes/aceitacao/script_emoji.py              $ python3 testes/aceitacao/script_emoji.revisado.py
🔎 lendo 5 comentários…                                  lendo 5 comentários
❓ Como faço isso no Windows?                            - Como faço isso no Windows?
❓ Funciona com Python 3.9?                              - Funciona com Python 3.9?
❓ Onde baixo o arquivo de exemplo? 🤔?                  - Onde baixo o arquivo de exemplo? 🤔?
✅ 3 perguntas salvas em relatorio.txt                   3 perguntas salvas em relatorio.txt
exit=0                                                   exit=0

$ sha256sum orig.txt rev.txt rev_cp1252.txt rev_ascii.txt
528019359831db7109137efed04a7efa73753daebb39bdc2830100e6bc294ea2  orig.txt
528019359831db7109137efed04a7efa73753daebb39bdc2830100e6bc294ea2  rev.txt
528019359831db7109137efed04a7efa73753daebb39bdc2830100e6bc294ea2  rev_cp1252.txt
528019359831db7109137efed04a7efa73753daebb39bdc2830100e6bc294ea2  rev_ascii.txt
cmp orig.txt rev.txt → idênticos
```

A saída útil é a mesma: as mesmas 3 perguntas e o relatório idêntico byte a byte, inclusive nos ambientes em que o original quebra. Só mudou o prefixo decorativo da tela. Tamanho: 38 → 41 linhas. A validação de entrada custa mais linhas do que o corte economiza, e é a única adição.

## Relatório

| Passo | O que rodou | O que saiu | Regra que guiou |
|---|---|---|---|
| Previsão | Só leitura do código e do JSON | 6 pontos de quebra e 3 perguntas esperadas | R3 |
| Reprodução | `PYTHONIOENCODING=cp1252 python3 script_emoji.py` | `UnicodeEncodeError` na linha 28, exit 1, sem relatório | R1 |
| Reprodução extra | print do emoji dos dados, ascii, item sem `texto` | `\U0001f914` quebra, `\xe1` quebra, `KeyError` | R1, R8 |
| Corte | Emojis decorativos e frase da docstring removidos | Menos decoração, nenhuma perda de dado | R7 |
| Correção | `reconfigure(errors="replace")` e validação na entrada | Exit 0 em cp1252 e ascii, exit 1 com mensagem clara nas entradas ruins | R8 |
| Lado a lado | Original e revisado, mesma entrada | sha256 igual nos 4 relatórios, 3 perguntas em ambos | R1, R3 |
| Validação | `tools/validar_resposta.py --perfil revisao` | `OK: resposta seguiu o loop`, exit 0 | R1 |

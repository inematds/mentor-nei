# mentor-nei — piloto real do kit Mentor-Especialista

Mentor no Claude Code que ensina **no método do Nei Maldaner (INEMA)**: usar Claude Code e agentes de IA na prática, construindo junto. Foi gerado com o kit **[inematds/mentor-especialista](https://github.com/inematds/mentor-especialista)** e serve de **exemplo real completo**: acervo, wiki, regras com citação, testes e o diário do piloto.

> Copia o método, não a pessoa. O acervo é conteúdo público do próprio Nei (lives do canal [@inematdsx](https://www.youtube.com/@inematdsx) e guias em inematds.github.io), publicado aqui com autorização dele.

## Números

| | |
|---|---|
| Fontes | 22 (14 lives + 8 guias) |
| Palavras | ~189 mil (legendas públicas + 1 transcrição local) |
| Wiki | 76 páginas, ~1.300 links (fontes, temas, princípios, métodos) |
| Regras | 10, todas ativas, 40 citações conferidas por script |
| Piloto | 4/5 critérios, nota 8 em "reconheço a pessoa nas regras" |

As regras mais fortes, pelo número de fontes: **conferir o resultado real antes de dizer "pronto"**, **definir o critério de pronto antes de começar**, **medir com e sem antes de acreditar** e **usar o menor custo que resolve**. Veja [`regras.md`](regras.md) e [`wiki/hot.md`](wiki/hot.md).

## Usar

```bash
git clone https://github.com/inematds/mentor-nei.git
cd mentor-nei
python3 tools/stats.py && python3 tools/validar_links.py && python3 tools/validar_citacoes.py
claude      # abra o Claude Code nesta pasta
```

Dentro do Claude Code:

```
/nei-ensina me ensina a fazer um hook Stop que bloqueia enquanto o TODO.md tiver itens abertos
/nei-revisa caminho/do/script.py
/nei-ingere https://inematds.github.io/<outro-guia>/guia/
```

## O que olhar

- [`PILOTO-DIARIO.md`](PILOTO-DIARIO.md): tudo o que aconteceu em cada fase, o placar e as correções que viraram o kit 1.2
- [`testes/aceitacao/RESULTADOS.md`](testes/aceitacao/RESULTADOS.md): os 3 testes de aceitação e as evidências
- [`testes/respostas/`](testes/respostas/): lições reais do mentor (com Previsão → Saída real → Versão quebrada → Relatório)
- [`exemplos/hook-todo-stop/`](exemplos/hook-todo-stop/): o código que o mentor construiu no teste 1, incluindo a versão ingênua que entra em loop infinito
- [`FALHAS.md`](FALHAS.md): falhas de operação e a menor correção de cada uma

## Atualizar para a versão nova do kit

```bash
python3 ../mentor-especialista/novo-mentor.py --atualizar .
```

Licença MIT (código). O conteúdo de `raw/` pertence ao autor; é usado aqui para estudo.

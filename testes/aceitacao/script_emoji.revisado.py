"""Resume comentários de um arquivo JSON e grava um relatório.

Revisado: roda em qualquer terminal (cp1252, ascii, pipe no Windows).
"""
import json
import sys
from pathlib import Path

ENTRADA = Path(__file__).with_name("comentarios.json")
SAIDA = Path(__file__).with_name("relatorio.txt")


def perguntas(comentarios):
    return [t for c in comentarios if (t := c["texto"].strip()).endswith("?")]


def main():
    # O terminal pode não ter UTF-8: o que não couber vira "?" em vez de derrubar o script.
    sys.stdout.reconfigure(errors="replace")
    comentarios = json.loads(ENTRADA.read_text(encoding="utf-8"))
    achadas = perguntas(comentarios)
    SAIDA.write_text("\n".join(achadas), encoding="utf-8")  # grava antes de imprimir
    print(f"lendo {len(comentarios)} comentários...")
    for p in achadas:
        print("-", p)
    print(f"{len(achadas)} perguntas salvas em {SAIDA.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

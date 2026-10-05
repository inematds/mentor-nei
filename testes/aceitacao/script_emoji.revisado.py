"""Lista os comentários que são perguntas (terminam em '?') e grava relatorio.txt."""
import json
import sys
from pathlib import Path

ENTRADA = Path(__file__).with_name("comentarios.json")
SAIDA = Path(__file__).with_name("relatorio.txt")


def main():
    # Terminal sem UTF-8 (Windows cp1252, pipe, CI): troca o caractere por '?' em vez de cair.
    # Tirar só os emojis fixos não basta: o próprio dado (comentário) pode ter emoji.
    sys.stdout.reconfigure(errors="replace")
    try:
        comentarios = json.loads(ENTRADA.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        print(f"erro ao ler {ENTRADA.name}: {e}", file=sys.stderr)
        return 1
    achadas = [t for c in comentarios if (t := c.get("texto", "").strip()).endswith("?")]
    print(f"lendo {len(comentarios)} comentários")
    for p in achadas:
        print("-", p)
    SAIDA.write_text("\n".join(achadas), encoding="utf-8")
    print(f"{len(achadas)} perguntas salvas em {SAIDA.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

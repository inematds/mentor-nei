"""Lista os comentários que são perguntas e grava em relatorio.txt (UTF-8)."""
import json
import sys
from pathlib import Path

ENTRADA = Path(__file__).with_name("comentarios.json")
SAIDA = Path(__file__).with_name("relatorio.txt")


def main():
    # Terminal sem UTF-8 (cp1252 no Windows, ascii em container) troca o que
    # não cabe por "?" em vez de derrubar o script. O arquivo segue UTF-8.
    sys.stdout.reconfigure(errors="replace")
    comentarios = json.loads(ENTRADA.read_text(encoding="utf-8"))
    print(f"lendo {len(comentarios)} comentários...")
    achadas = [c["texto"].strip() for c in comentarios if c["texto"].strip().endswith("?")]
    for p in achadas:
        print("?", p)
    SAIDA.write_text("\n".join(achadas), encoding="utf-8")
    print(f"{len(achadas)} perguntas salvas em {SAIDA.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

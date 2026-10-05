"""Lista os comentários que são perguntas (terminam em "?") e grava em relatorio.txt.

Uso: python3 script_emoji.revisado.py [entrada.json] [saida.txt]
"""
import json
import sys
from pathlib import Path

AQUI = Path(__file__).parent


def carregar(entrada):
    """Falha cedo: arquivo, JSON e formato conferidos antes de processar."""
    try:
        dados = json.loads(entrada.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"erro: não consegui ler {entrada}: {e}")
    if not isinstance(dados, list):
        sys.exit(f"erro: {entrada} deve conter uma lista de comentários")
    for i, c in enumerate(dados):
        if not isinstance(c, dict) or not isinstance(c.get("texto"), str):
            sys.exit(f"erro: comentário {i} sem campo 'texto' do tipo string")
    return dados


def main(argv):
    sys.stdout.reconfigure(errors="replace")  # terminal sem UTF-8 troca o caractere por "?", não quebra
    entrada = Path(argv[1]) if len(argv) > 1 else AQUI / "comentarios.json"
    saida = Path(argv[2]) if len(argv) > 2 else AQUI / "relatorio.txt"
    comentarios = carregar(entrada)
    achadas = [t for t in (c["texto"].strip() for c in comentarios) if t.endswith("?")]
    print(f"lendo {len(comentarios)} comentários")
    for p in achadas:
        print("-", p)
    saida.write_text("\n".join(achadas), encoding="utf-8")
    print(f"{len(achadas)} perguntas salvas em {saida.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

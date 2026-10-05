#!/usr/bin/env python3
"""Hook Stop: não deixa o turno terminar enquanto TODO.md tiver itens '- [ ]'.

Contrato: lê o JSON do evento no stdin; para bloquear imprime {"decision":"block","reason":...}.
Critério de aborto: no máximo TODO_STOP_MAX bloqueios seguidos por sessão (padrão 3);
depois libera e avisa no stderr. Zerou os abertos -> zera o contador.
Qualquer erro interno -> exit 0 (o hook nunca prende a sessão).
"""
import json, os, re, sys
from pathlib import Path

ABERTO = re.compile(r"^\s*[-*]\s+\[ \]\s*(.*)$")


def main() -> int:
    evento = json.load(sys.stdin)
    raiz = Path(os.environ.get("CLAUDE_PROJECT_DIR") or evento.get("cwd") or ".")
    todo = raiz / "TODO.md"
    sessao = re.sub(r"[^A-Za-z0-9_.-]", "_", evento.get("session_id") or "sem-sessao")
    cont = raiz / ".claude" / "todo-stop" / f"{sessao}.count"
    maximo = int(os.environ.get("TODO_STOP_MAX", "3"))

    linhas = todo.read_text(encoding="utf-8").splitlines() if todo.exists() else []
    abertos = [m.group(1) for l in linhas if (m := ABERTO.match(l))]
    if not abertos:
        cont.unlink(missing_ok=True)
        return 0

    n = int(cont.read_text()) if cont.exists() else 0
    if n >= maximo:
        cont.unlink(missing_ok=True)
        print(f"[stop_todo] liberado após {maximo} bloqueios; ainda abertos: {'; '.join(abertos)}", file=sys.stderr)
        return 0

    cont.parent.mkdir(parents=True, exist_ok=True)
    cont.write_text(str(n + 1))
    print(json.dumps({"decision": "block",
                      "reason": f"TODO.md tem {len(abertos)} item(ns) aberto(s) (bloqueio {n + 1}/{maximo}): "
                                + "; ".join(abertos)
                                + ". Termine cada um e marque com [x]. Se algum não depende de você, "
                                  "explique por que e deixe aberto."}))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)

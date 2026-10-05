#!/usr/bin/env python3
"""v0 (ingênua): bloqueia o Stop enquanto TODO.md tiver '- [ ]'. SEM trava anti-loop."""
import json, os, re, sys
from pathlib import Path

ABERTO = re.compile(r"^\s*[-*]\s+\[ \]\s*(.*)$")

evento = json.load(sys.stdin)
raiz = Path(os.environ.get("CLAUDE_PROJECT_DIR") or evento.get("cwd") or ".")
todo = raiz / "TODO.md"
if not todo.exists():
    sys.exit(0)
abertos = [m.group(1) for l in todo.read_text(encoding="utf-8").splitlines() if (m := ABERTO.match(l))]
if abertos:
    print(json.dumps({"decision": "block",
                      "reason": f"TODO.md ainda tem {len(abertos)} item(ns) aberto(s): "
                                + "; ".join(abertos) + ". Termine e marque com [x]."}))
sys.exit(0)

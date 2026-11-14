"""
Hola Hub365: app de ejemplo del catálogo público (solo biblioteca estándar de Python).

Muestra cómo una app del catálogo:
  - recibe la identidad firmada de Hub365 (cabeceras X-Hub365-*, firma v2 con la licencia);
  - comprueba que la licencia de Hub365 incluye su módulo (app:hola-hub365) y, si no, dice
    «Necesita licencia»;
  - guarda sus datos en APP_DATA_DIR (se conservan al actualizar y al desinstalar);
  - responde en /health para que Hub365 sepa que ha arrancado bien.

Hub365 la arranca con:  {python} app.py --port {port}
"""
from __future__ import annotations

import argparse
import hashlib
import hmac
import html
import json
import os
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote

SLUG = "hola-hub365"
MODULE = f"app:{SLUG}"
VERSION = json.loads((Path(__file__).with_name("hub365-app.json")).read_text(encoding="utf-8"))["version"]
SECRET = os.environ.get("HUB365_IDENTITY_SECRET", "")
DATA = Path(os.environ.get("APP_DATA_DIR") or Path(__file__).with_name("data"))
FIELDS = ("x-hub365-user-id", "x-hub365-user", "x-hub365-email", "x-hub365-name", "x-hub365-role",
          "x-hub365-department")
MAX_SKEW = 60
_seen: dict[str, float] = {}
_lock = threading.Lock()


class Invalid(Exception):
    pass


def verify(headers) -> dict:
    """Verifica la identidad firmada v2 de Hub365 y devuelve {usuario…, license: [módulos]}."""
    if not SECRET:
        raise Invalid("sin secreto")
    h = {k.lower(): v for k, v in headers.items()}
    sig, ts, nonce = h.get("x-hub365-signature", ""), h.get("x-hub365-timestamp", ""), h.get("x-hub365-nonce", "")
    if not sig.startswith("v2=") or not ts.isdigit() or not nonce:
        raise Invalid("faltan cabeceras v2")
    if abs(time.time() - int(ts)) > MAX_SKEW:
        raise Invalid("caducada")
    values = [h.get(f, "") for f in FIELDS]
    lic = h.get("x-hub365-license", "")
    msg = "\n".join(["v2", ts, nonce, *values, lic]).encode("utf-8")
    expected = "v2=" + hmac.new(SECRET.encode("utf-8"), msg, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, sig):
        raise Invalid("firma")
    with _lock:   # cada nonce vale una sola vez
        now = time.time()
        for k in [k for k, t in _seen.items() if now - t > 2 * MAX_SKEW]:
            _seen.pop(k, None)
        if nonce in _seen:
            raise Invalid("repetida")
        _seen[nonce] = now
    out = {k: unquote(v) for k, v in zip(("id", "username", "email", "full_name", "role", "department"), values)}
    out["license"] = [m for m in unquote(lic).split(",") if m]
    return out


def licensed(identity: dict) -> bool:
    mods = identity.get("license") or []
    return "all" in mods or MODULE in mods


def visits() -> int:
    DATA.mkdir(parents=True, exist_ok=True)
    f = DATA / "visitas.txt"
    with _lock:
        n = int(f.read_text() or 0) + 1 if f.exists() else 1
        f.write_text(str(n))
    return n


PAGE = """<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width">
<title>Hola Hub365</title><style>body{{font-family:system-ui,sans-serif;margin:0;display:grid;place-items:center;
min-height:100vh;background:#f6f8fc;color:#1f1f1f}}main{{background:#fff;border-radius:24px;padding:40px 48px;
box-shadow:0 1px 3px #0002;max-width:520px}}h1{{margin:0 0 8px}}p{{color:#444}}code{{background:#eef2fb;
padding:2px 6px;border-radius:6px}}.bad{{color:#b3261e}}</style><main>{body}</main></html>"""


class Handler(BaseHTTPRequestHandler):
    server_version = f"HolaHub365/{VERSION}"

    def log_message(self, fmt, *args):  # registro en la salida estándar (Hub365 lo guarda)
        print(f"{self.address_string()} {fmt % args}", flush=True)

    def _send(self, code: int, body: str, ctype: str = "text/html; charset=utf-8") -> None:
        data = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):  # noqa: N802
        path = self.path.split("?", 1)[0]
        if path.endswith("/health"):
            return self._send(200, "ok", "text/plain")
        try:
            who = verify(self.headers)
        except Invalid as exc:
            return self._send(401, PAGE.format(body=f"<h1>Ábrela desde Hub365</h1><p class=bad>Esta app solo "
                                               f"funciona detrás de Hub365 ({html.escape(str(exc))}).</p>"))
        if not licensed(who):
            return self._send(403, PAGE.format(body="<h1>Necesita licencia</h1><p>Tu licencia de Hub365 no "
                                               "incluye <b>Hola Hub365</b>. Pide una ampliación a NextCode Agency "
                                               "(info@nextcodeagency.com).</p>"))
        if path.endswith("/whoami"):
            return self._send(200, json.dumps({"verified": True, **who, "version": VERSION}), "application/json")
        name = html.escape(who.get("full_name") or who.get("username") or "visitante")
        n = visits()
        return self._send(200, PAGE.format(body=f"<h1>Hola, {name} 👋</h1><p>Esta es la app de ejemplo del "
                                           f"catálogo de Hub365 (versión <code>{VERSION}</code>).</p><p>Tu identidad "
                                           f"y la licencia llegan firmadas por Hub365. Visitas: <b>{n}</b>.</p>"))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=int(os.environ.get("PORT") or 8000))
    ap.add_argument("--host", default="127.0.0.1")
    args = ap.parse_args()
    srv = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"Hola Hub365 {VERSION} en http://{args.host}:{args.port}", flush=True)
    srv.serve_forever()


if __name__ == "__main__":
    main()

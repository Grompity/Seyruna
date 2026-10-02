# The door at Vercel: one file in the /api directory, riding the same spine.
# The era's api-dir contract: api/ask.py serves /api/ask when the module
# exports `handler` as a class inheriting BaseHTTPRequestHandler - the very
# grammar server.py's door already uses (do_POST, send_response, wfile).
# vercel.json rewrites /ask -> /api/ask so the browser's fetch finds it.
# Same bytes, same response shape as server.py's do_POST - no new organ.
import json
import os
import sys
from http.server import BaseHTTPRequestHandler

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

import stages
import window

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        raw, code = None, 200
        try:
            n = int(self.headers.get("Content-Length") or 0)
            body = json.loads((self.rfile.read(n) or b"{}").decode() or "{}")
            tr = stages.run_pipeline((body.get("question") or "").strip(),
                                     (body.get("facts") or "").strip(),
                                     live=True)
            raw = json.dumps({"response": tr.get("response", ""),
                              "why": window.why_lane(tr),
                              "trace": tr}).encode()
        except Exception as e:
            raw, code = json.dumps({"error": repr(e)}).encode(), 500
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

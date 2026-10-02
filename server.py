#!/usr/bin/env python3
"""Ascended AI — dev static server.

python's http.server, but every response carries `Cache-Control: no-store`,
so hot edits appear on the next reload instead of being replayed from the
browser cache as 304s of stale modules.

usage: python3 server.py [port]
"""
import functools
import http.server
import json
import os
import sys

# the door (MVP): the product rides INSIDE the same process as the
# shelf and the spine — stdlib all the way, the funnel spoke by stages.
import stages
import window

ROOT = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    # Serve ES modules with the right type (browsers enforce it).
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        '.js': 'text/javascript',
        '.mjs': 'text/javascript',
        '.css': 'text/css',
        '.svg': 'image/svg+xml',
    }

    def end_headers(self, *args, **kwargs):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        return super().end_headers(*args, **kwargs)

    def do_POST(self):
        # the door: POST /ask {"question": str, "facts": str (optional)}
        # -> {"response": verbatim, "why": the window, "trace": verbatim}.
        # Computed first, sent second; a failure answers as JSON and
        # never launders a default into the speech.
        raw, code = None, 200
        try:
            n = int(self.headers.get('Content-Length') or 0)
            body = json.loads((self.rfile.read(n) or b'{}').decode())
            if self.path.split('?')[0] != '/ask':
                raw, code = b'{"error": "no route"}', 404
            elif not (body.get('question') or '').strip():
                raw, code = b'{"error": "no question"}', 400
            else:
                tr = stages.run_pipeline(body['question'].strip(),
                                         (body.get('facts') or '').strip(),
                                         live=True)
                raw = json.dumps({'response': tr.get('response', ''),
                                  'why': window.why_lane(tr),
                                  'trace': tr}).encode()
        except Exception as e:
            raw, code = json.dumps({'error': repr(e)}).encode(), 500
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)
        self.wfile.flush()

    def log_message(self, *args):
        pass

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5173
    http.server.ThreadingHTTPServer.allow_reuse = True
    srv = http.server.ThreadingHTTPServer(
        ('127.0.0.1', port), functools.partial(Handler, directory=ROOT))
    print(f'serving {ROOT} at http://127.0.0.1:{port} (no-store)')
    srv.serve_forever()
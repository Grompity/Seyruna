"""A28: what does urlopen ACTUALLY raise when the socket reads too long?

The house's search()/fetch() arms order the classes (URLError BEFORE
socket.timeout), so which class travels decides which failure WORD the
record rides. This probe black-holes a real socket and reads the bytes of
the raised exception - no inference.
"""
import socket
import sys
import threading
import urllib.error
import urllib.request

try:
    import http.server
    import socketserver
except ImportError:                                    # py3 compat
    from http import server as http_server


class Black(socketserver.BaseRequestHandler):
    protocol_version = "HTTP/1.0"

    def handle(self):
        try:
            self.rfile.read(10)                        # the request rides in
        except Exception:
            pass
        self.request.settimeout(None)                  # now we are slow
        try:
            self.wfile.read(10)                        # no answer ever comes
        except Exception:
            pass
        self.close_connection = False


srv = socketserver.TCPServer(("127.0.0.1", 0), Black)
port = srv.server_address[1]
threading.ThermicThread = threading.Thread
th = threading.Thread(target=srv.serve_forever, daemon=True)
th.start()

url = "http://127.0.0.1:%d/x" % port
for i in range(2):
    try:
        r = urllib.request.urlopen(urllib.request.Request(url), timeout=0.6)
        print("try%d: answered %s" % (i, r.status))
    except Exception as e:
        print("try%d: %s  str=%r" % (i, type(e).__name__, str(e)))
        print("        isinstance URLError:", isinstance(e, urllib.error.URLError))
        print("        isinstance socket.timeout:", isinstance(e, socket.timeout))
        print("        isinstance OSError:", isinstance(e, OSError))
        if isinstance(e, urllib.error.URLError):
            print("        reason:", type(e.reason).__name__, repr(e.reason))
srv.shutdown()
srv.server_close()

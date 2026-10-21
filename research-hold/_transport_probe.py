"""A28: the transport's timeout WORD, at bytes.

The house's own law (T131) says a timed-out search says `search-timeout`.
The question: what does the REAL transport raise, and which word does the
house's own ordering of the arms therefore speak? A socket that answers and
never answers again is the black-hole that makes the question concrete.
"""
import os
import socket
import socketserver
import sys
import threading
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import web_research as w


class Hole(socketserver.BaseRequestHandler):
    protocol_version = "HTTP/1.0"

    def handle(self):
        try:
            self.rfile.read(64)                 # the request rides in
        except Exception:
            pass
        self.close_connection = False


srv = socketserver.TCPServer(("127.0.0.1", 0), Hole)
port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
url = "http://127.0.0.1:%d/x" % port

# 1. what the raw transport raises at a read-timeout
try:
    r = urllib.request.urlopen(urllib.request.Request(url), timeout=0.4)
    print("transport: answered after all", r.status)
except Exception as e:
    print("transport raised: %s  str=%r" % (type(e).__name__, str(e)))
    if isinstance(e, urllib.error.URLError):
        print("           its reason is: %s %r" % (type(e.reason).__name__,
                                                   e.reason))
    print("           isinstance URLError:",
          isinstance(e, urllib.error.URLError))
    print("           isinstance socket.timeout:",
          isinstance(e, socket.timeout))

# 2. which WORD the house's own search()/fetch() speak for that shape
def holed(*a, **k):
    raise urllib.error.URLError(socket.timeout("timed out"))


w.urlopen = holed
print("house search(): ", w.search("Tao Te Ching"))
print("house fetch() : ", w.fetch(url))


def raised(*a, **k):
    raise socket.timeout("timed out")


w.urlopen = raised
print("bare-timeout seam search():", w.search("Tao Te Ching"))
print("bare-timeout seam fetch() :", w.fetch(url))
srv.shutdown()
srv.server_close()

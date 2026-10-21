"""A28: which DETERMINISTIC query-shape lets a conversational sentence reach
the keyless ddg-ia lane? Live evidence over the candidate shapes, so the
picker is chosen by bytes, not by taste. Zero mouthfuls, zero coins.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import web_research as w

STOP = set("""what whos whats is are was were do does did the a an of to in on
for with about say says said tell that this these those which who whom how
when where why can could would should will must not no nor and or but as at
by from into your you their they them its it he she we me my our being become
teaches teach taught""".split())
CAPS = re.compile(r"[A-Z][A-Za-z0-9'-]*")


def strip_poss(w):
    return re.sub(r"'s$", "", w)


def shapes(q):
    words = [t for t in re.split(r"[^0-9A-Za-z']+", q) if t]
    caps = [m.group(0) for m in CAPS.finditer(q)
            if m.group(0).lower() not in STOP]
    core = [strip_poss(t) for t in words if strip_poss(t).lower() not in STOP]
    out, seen = {}, set()

    def put(name, s):
        s = strip_poss(s).strip()
        if s and s.lower() not in seen:
            seen.add(s.lower())
            out[name] = s
    for c in caps[:3]:
        put("cap" + str(len([k for k in out])), c)
    put("core2", " ".join(core[:2]))
    put("core3", " ".join(core[:3]))
    put("caps+2", " ".join(caps[:1] + core[1:3]))
    return out


for q in sys.argv[1:]:
    print("Q:", q[:70])
    cands = {"raw": q}
    cands.update(shapes(q))
    for name, s in cands.items():
        rows, gap = w.search(s)
        kinds = [r["lane"] for r in rows]
        print("   %-8s %-34r -> rows=%d %s %s"
              % (name, s[:34], len(rows), gap or "ok", kinds[:4]))

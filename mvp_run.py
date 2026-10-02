# mvp_run.py — the first product traffic: the First Seeker's five,
# VERBATIM from five-visible.md (facts empty — the questions as their
# seeker asked them; the earlier facts-lines were the builder's own
# writing, not the record's bytes), plus ONE out-of-shelf probe so the
# empty lane gets its first hearing. Runs through the DOOR (HTTP), the
# way a seeker will. Saves every full response: mvp-run-N.json.
import json
import sys
import urllib.request

PORT = sys.argv[1] if len(sys.argv) > 1 else "5173"
URL = "http://127.0.0.1:" + PORT + "/ask"

def ask(q, f=""):
    body = json.dumps({"question": q, "facts": f}).encode()
    req = urllib.request.Request(
        URL, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=240) as r:
        return json.loads(r.read().decode())

FIVE = [
("C1 intuition vs self-deception",
 "How can I distinguish genuine intuition from desire, fear, projection,"
 " pattern-recognition, or a story I am unconsciously creating because I"
 " want something to be true?"),
("C2 the convergence question",
 "When the traditions appear to point toward similar ideas about ego,"
 " attachment, surrender, compassion, or unity, have they discovered"
 " something similar about reality, or am I imposing a modern synthesis"
 " onto traditions that fundamentally disagree?"),
("C3 spirituality without identity",
 "How do I pursue deep spiritual practice and transformation without"
 " becoming attached to being spiritual, believing I am specially chosen"
 " or awakened, or using spiritual ideas to avoid ordinary human"
 " responsibilities?"),
("C4 surrender vs responsibility",
 "How do I know when I should surrender and allow life to unfold, and"
 " when surrender or going with the flow is actually avoidance, fear,"
 " indecision, or refusal to take responsibility?"),
("C5 consciousness",
 "What can we responsibly say about consciousness when neuroscience and"
 " philosophy sit next to contemplative reports of awareness, selfhood,"
 " witness-consciousness, soul, mind, or ultimate reality?"),
]
PROBE = ("PROBE near-empty (the door's first breath, recorded at the smoke)",
         "What does the shelf make of jazz improvisation?")
EMPTY = ("PROBE out-of-shelf (the EMPTY lane's first hearing)",
         "What does the xylophone weathers?")

if __name__ == "__main__":
    n = 0
    for name, q in FIVE + [PROBE, EMPTY]:
        n += 1
        d = ask(q)
        json.dump(d, open("mvp-run-%d.json" % n, "w"), indent=1)
        print("\n===== %s =====" % name)
        print("RESP:", d.get("response", "")[:700])
        why = d.get("why") or {}
        print("WHY-evidence:", [e["id"] for e in (why.get("evidence") or [])])
        print("WHY-disagreement:", why.get("disagreement"))
        print("WHY-uncertainty:", why.get("uncertainty"))
        print("WHY-synthesis:", [(s["lineage"][:26], s["cites"])
                                 for s in (why.get("synthesis") or [])])
        print("WHY-boundary:", why.get("boundary"))
    print("\n(the five + two probes saved: mvp-run-1..7.json)")

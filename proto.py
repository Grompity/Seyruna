# proto.py — the CLI: one question, one card, end to end.
#   python3 proto.py --q "..." --facts "..." [--live] [--inject file.json]
# Prints the response; writes last_trace.json (--t also prints it).
import argparse
import json
import stages

ap = argparse.ArgumentParser()
ap.add_argument("--q", required=True)
ap.add_argument("--facts", default="")
ap.add_argument("--inject", default=None)
ap.add_argument("--live", action="store_true")
ap.add_argument("--t", action="store_true")
args = ap.parse_args()

draft = None
if args.inject:
    draft = json.load(open(args.inject))

trace = stages.run_pipeline(args.q, args.facts, draft=draft, live=args.live)
json.dump(trace, open("last_trace.json", "w"), indent=1)

print("\nRESPONSE: " + trace["response"])
print("(trace written to last_trace.json)")
if args.t:
    print(json.dumps(trace, indent=1))

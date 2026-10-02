# mutate_test.py — the friend's demand: prove law-as-data, don't
# describe it. Change ONLY the data (the loaded rule_pack params/rules
# object — equivalent to editing rule_pack.json alone), rerun the same
# offline probe, and see whether behavior moves. The boundary, if any,
# is REPORTED, not redesigned.
import stages

FIX1 = {"id": "K1", "claim": "The tradition reads purification here.",
        "work": "Rite", "level": "INTERPRETIVE", "edges": [],
        "evidence": "NONE-FOR"}
FIX2 = {"id": "K2", "claim": "Studied effects are small-to-moderate.",
        "work": "Review", "level": "EMPIRICAL", "edges": [],
        "evidence": "PRESENT"}
stages.set_shelf([FIX1, FIX2])
FACTS = "three days alone with a friend"


def node(text, cites, verbs, unc=None):
    return {"node": text, "cites": cites, "verbs": verbs,
            "uncertainty": unc}


def probe(draft):
    return stages.run_pipeline("Does it purify?", FACTS, draft=draft,
                               live=False)


def report(name, cond, detail):
    print(("ok    " if cond else "BOUNDARY ") + name + ("  | " + detail
          if detail else ""))
    return cond


tr = probe([node("The tradition reads purification.", ["K1"], ["CLAIM"])])
base_owed = tr["caution_appended"] and "RP-01" in " ".join(tr["fires"])
report("baseline: conjunction floor 2 => caution owed & fired",
       base_owed, "")

# M1: conjunction_floor 2 -> 3  (data-only)
stages.P["conjunction_floor"] = 3
tr = probe([node("The tradition reads purification.", ["K1"], ["CLAIM"])])
report("M1 floor 3: RP-01 silent, nothing appended",
       "RP-01" not in " ".join(tr["fires"]) and not tr["caution_appended"],
       "")
stages.P["conjunction_floor"] = 2

# M2: remove 'friend' from human_tokens (data-only)
base = probe([node("You could fast.", ["K2"], ["RECOMMEND"])])
base_ok = "RP-03" not in " ".join(base["observations"])
stages.P["human_tokens"] = [t for t in stages.P["human_tokens"]
                            if t != "friend"]
tr = probe([node("You could fast.", ["K2"], ["RECOMMEND"])])
report("M2 'friend' removed: RECOMMEND now provisional",
       base_ok and "RP-03" in " ".join(tr["observations"]), "")
stages.P["human_tokens"] = stages.RP["params"]["human_tokens"]

# M3: change caution_default (data-only)
tr = probe([node("The tradition reads purification.", ["K1"], ["CLAIM"])])
before = tr["response"]
stages.P["caution_default"] = "MUTATED-CAUTION-TEXT"
tr = probe([node("The tradition reads purification.", ["K1"], ["CLAIM"])])
report("M3 caution_default changed: appended text follows the data",
       "MUTATED-CAUTION-TEXT" in tr["response"]
       and "MUTATED" not in before, "")
stages.P["caution_default"] = stages.RP["params"]["caution_default"]

# M4: change one watch-list entry (data-only)
tr = probe([node("You seem ready for it.", ["K2"], ["CLAIM"])])
before_ok = "RP-04" in " ".join(tr["observations"])
stages.P["status_words"] = [w for w in stages.P["status_words"]
                            if w != "ready"]
tr = probe([node("You seem ready for it.", ["K2"], ["CLAIM"])])
report("M4 'ready' removed: the status note no longer fires",
       before_ok and "RP-04" not in " ".join(tr["observations"]), "")

# M5: change one rule's KIND in the data (RP-04 -> hard)
before = probe([node("You seem ready for it.", ["K2"], ["CLAIM"])])
for r in stages.RP["rules"]:
    if r["id"] == "RP-04":
        r["kind"] = "hard"
tr = probe([node("You seem ready for it.", ["K2"], ["CLAIM"])])
same = (" ".join(before["observations"]).split(" -- ")[0] ==
        " ".join(tr["observations"]).split(" -- ")[0])
report("M5 kind flipped in DATA only: behavior IDENTICAL (kind is descriptive — the boundary)",
       same, "kind is documentation, not execution")

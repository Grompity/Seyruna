#!/usr/bin/env python3
"""review.py - A6's DETERMINISTIC audit leg (protocol: review-protocol.json,
RRV-0.1 - the criteria were WRITTEN BEFORE any score).

The bridge's GPT leg (a genuinely different FAMILY from the answering
mouth: gpt-6-astra reviews RadixArk/Qwen3.8) stands BLOCKED today for one
named reason: OPENAI_API_KEY is absent. This module therefore raises what
CAN be deterministic without any model at all: the TOKEN-LAW. For every
sentence of an answer it weighs the claim's SIGNATURE bytes (digit-runs,
with a small spelled-NUMBER table since fourteen and 14 are the same
claim; and capitalized proper forms) against the bytes THAT REACHED THE
MOUTH (the packet rows' claims - packet_text's own law: what the mouth
saw is the record's ground, not a present-day page).

The machine word is deliberately humble - it speaks TOKEN-PRESENCE, NEVER
ENTAILMENT:
  tokens-present   the signatures ride the bytes (support is POSSIBLE;
                   the claim may still be stronger than its row - the
                   operator weighs that, the machine does not)
  token-absent     some signature rides NO byte at all - the falsifiable
                   FINDING (a year the packet never carried; a month the
                   answer did not claim, therefore could not need)
  token-free       the sentence carries no signature at all (qualitative
                   or interpretive) - the machine STANDS ASIDE, it does
                   not pass the sentence (that would be the self-grading
                   sin in a new coat)

The per-row WHO SPEAKS (kind, work) rides the evidence-findings so a
reviewer sees WHICH KIND of seeing a supporting byte got. The
independence word reads the environment's key-presidence WITHOUT ever
printing a value.

Usage: python3 review.py [--write] - prints (and optionally writes
research-hold/a6-machine.json) the machine's pass over the A5 eval
artifact (the experiment's bytes, not today's pages).
"""
import json
import os
import re
import sys
import time

import web_research            # reuses the house's SENTENCE divider

HERE = os.path.dirname(os.path.abspath(__file__))

NUMWORDS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
            "six": "6", "seven": "7", "eight": "8", "nine": "9",
            "ten": "10", "eleven": "11", "twelve": "12",
            "thirteen": "13", "fourteen": "14", "fifteen": "15",
            "sixteen": "16", "seventeen": "17", "eighteen": "18",
            "nineteen": "19", "twenty": "20"}
ORD = {"first": "1", "second": "2", "third": "3", "fourth": "4",
       "fifth": "5", "sixth": "6", "seventh": "7", "eighth": "8",
       "ninth": "9", "tenth": "10"}
SIG_NUM = re.compile(r"\d+(?:[./]\d+)*(?:st|nd|rd|th)?")
STOP_CAPS = {"The", "This", "That", "There", "They", "Their", "What",
             "When", "Where", "Which", "While", "About", "Under",
             "After", "Before", "With", "Within", "Without", "These",
             "Those", "Then", "Thus", "Also", "Such", "Into", "Upon"}


def load_protocol():
    doc = json.loads(open(os.path.join(HERE, "review-protocol.json")).read())
    probs = []
    if doc.get("protocol") is None:
        probs.append("no protocol id")
    if len(doc.get("measures") or {}) != 9:
        probs.append("the nine measures are the spine")
    sv = doc.get("status-vocab") or {}
    if len(sv.get("claim-support") or []) != 6 or \
            len(sv.get("verdicts") or []) != 4:
        probs.append("the status vocabularies moved")
    return doc, probs


def signatures(text):
    """The claim's signature bytes: (digits - numeral-words and ordinal-words
    folded first, so 'fourteen inscriptions' and '14 inscriptions' weigh as
    the ONE claim), and capitalized PROPER forms beyond the house stop-list
    (a name the bytes do not carry is a claim the bytes do not carry)."""
    t = " " + text.lower() + " "
    nums = set(SIG_NUM.findall(t.replace(",", "")))
    for w, n in list(NUMWORDS.items()) + list(ORD.items()):
        if (" " + w + " ") in t or (" " + w + ",") in t:
            nums.add(n)
    nums = {re.sub(r"(st|nd|rd|th)$", "", n) for n in nums}
    ents = {w for w in re.findall(r"[A-Z][A-Za-zṅṁāīūṇ'’-]{3,}", text)
            if w not in STOP_CAPS}
    return {"numbers": sorted(nums), "entities": sorted(ents)}


def check(claim_text, rows):
    """The machine's adversarial word over ONE claim against the rows (the
    packet's bytes the mouth saw). Returns the signatures, which are
    MISSING, the who-speaks of the supporting rows, and the humble status
    word (tokens-present / token-absent / token-free)."""
    sig = signatures(claim_text)
    missing, evidence = [], []
    for kindname in ("numbers", "entities"):
        for tok in sig[kindname]:
            hit = [r for r in rows
                   if tok.lower() in str(r.get("claim") or "").lower()
                   or tok.lower() in str(r.get("url") or "").lower()]
            if not hit:
                missing.append(kindname[0] + ":" + tok)
            else:
                for r in hit:
                    ev = {"token": tok, "row": r.get("id"),
                          "kind": r.get("kind") or "none",
                          "work": r.get("work")}
                    if ev not in evidence:
                        evidence.append(ev)
    status = ("token-free" if not (sig["numbers"] or sig["entities"])
              else "token-absent" if missing else "tokens-present")
    return {"sig": sig, "missing": missing, "evidence": evidence,
            "status-machine": status}


def independence_words():
    """Who may speak as a second brain TODAY (the value of the key is NEVER
    printed, only its presence)."""
    present = bool(os.environ.get("OPENAI_API_KEY"))
    return {"answering-family": "RadixArk/Qwen3.8-Flash (config's MODEL)",
            "reviewer-family": "gpt (the bridge's leg)",
            "key-present": present,
            "status": ("READY (family differs; the leg itself still unproven "
                       "this run)" if present else
                       "BLOCKED: OPENAI_API_KEY absent - independence is "
                       "DESIGNED, not proven; the deterministic audit and "
                       "the DISCLOSED OPERATOR carry the review")}


def pass_eval(path=None):
    """The machine's pass over an eval artifact (default the A5 live bytes)."""
    p = path or os.path.join(HERE, "research-hold", "a5-eval-live.json")
    rec = json.loads(open(p).read())
    out = {"machine-pass": "A6 token-law", "source": os.path.basename(p),
           "at": time.strftime("%Y%m%d"), "independence": independence_words(),
           "questions": []}
    for q in rec.get("questions") or []:
        answer = ((q.get("door") or {}).get("response")) or ""
        rows = q.get("web", {}).get("rows") or []
        sents = [s for s in web_research.SENTENCE.split(answer)
                 if s.strip()]
        per = [dict(check(s, rows), sentence=s) for s in sents]
        out["questions"].append({
            "id": q.get("id"), "question": q.get("question"),
            "answer": answer,
            "sentences": per,
            "machine-findings": [
                f for s in per for f in s["missing"]]})
    return out


def main(argv):
    doc, probs = load_protocol()
    if probs:
        print("the protocol is wrong:", "; ".join(probs))
        return 1
    out = pass_eval()
    for q in out["questions"]:
        print(q["id"], "|", len(q["sentences"]), "sentences |",
               ("CLEAN of absent signatures" if not q["machine-findings"]
                else "ABSENT SIGNATURES: " + ", ".join(q["machine-findings"])))
    print("independence:", out["independence"]["status"])
    if "--write" in argv:
        o = os.path.join(HERE, "research-hold", "a6-machine.json")
        open(o, "w").write(json.dumps(out, indent=1))
        print("wrote", o)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

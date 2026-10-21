# A22 — the controlled evaluation DESIGN (frozen before the run)

Written **before** the live probes and the live comparison, at the working
tree carrying the A22 implementation (T164–T166 added at the tail;
163→166 tests, all green: **166/166 — HARNESS GREEN**). Nothing here is informed by a peek at A22's own run: the
case bytes are chosen from the A-series evidence (the A5 EA fixture, the
A13 live file, the A20 diagnostic), and the expected-lane words were all
written from THAT history — an expectation is not a score.

## The question the evaluation asks

Mechanically: does an explicitly spoken retrieval query reach the search
while the question rides the pipeline untouched, and do the A15–A19 truth
machines (the packet's word, the trace's stamp, the status law, the
selector) speak the new road without a lean? (T164–T166 already answer
that at fixtures.) Live, the evaluation adds only what fixtures cannot
give: the provider's and the model's REAL bytes, recorded truthfully —
never a claim that separation improves reasoning.

## The frozen cases (`research-eval-a22.json`, EA-A22.0.1)

Four cases — the §'s cap. Every QUESTION rides byte-for-byte from a prior
A-series record; every QUERY is defined SEPARATELY, from prior recorded
bytes, frozen before the run.

| id | kind | question (frozen bytes) | query (frozen; separate) |
|----|------|--------------------------|---------------------------|
| C1 | known-green, retitled | `"Ashoka rock edict"` | `"Edicts of Ashoka"` |
| C2 | empty-thrice sentence, separated query | `"What do Ashoka's rock edicts say about dhamma?"` | `"Ashoka rock edict"` |
| C3 | the emptiness lane as such | `"Zzzyx plingworth"` | `"Zzzyx plingworth"` |
| C4 | the control (C2's bytes, no query word) | `"What do Ashoka's rock edicts say about dhamma?"` | *(none — the absence is the tested fact)* |

Provenance of every frozen word: C1's question rode A5's EA1 and A20's
case A; C1's query `"Edicts of Ashoka"` is the corpus's OWN title bytes
verbatim in A20's read-window bytes (the fetched page's leading words).
C2/C4's question is A13.4's sentence, empty at A13.1, A13.4, and A20 — the
§'s "previously associated with empty search". C2's query is the exact
two-word bytes that returned READ EVIDENCE at A5's EA1 and A20's case A —
the §'s "known-green retrieval case", borrowed byte-for-byte, not
invented. C3's bytes are A5's EA4 (search-empty). **Zero live
forward-miracles are required**: every case's expectation names a
MACHINERY criterion; the known outcomes serve only to anchor the query
words' motivation in prior bytes.

## The frozen criteria

Per case, PASS/FAIL is decided ONLY on mechanical truthfulness:

- **M1 — mechanical separation.** The record's `web.query` equals the
  spoken query bytes byte-for-byte (C4: equals the question bytes —
  the fallback spoken at the packet's own word). The record's `question`
  is byte-for-byte the fixture's question.
- **M2 — the query reached the door's retrieval.** Where the web lane
  rode, `door.query` equals the spoken bytes (the trace's own stamp
  verbatim); where the search folded, `door.query` is `None` and
  `web_stamped` is `False` together (absence spoken, never promoted).
  C4's door record carries **no** `query` key at all.
- **M3 — truthful status.** `status_word(record)` equals the record's
  `door.evidence_status` verbatim (the A19 selection undisturbed on the
  new road); the lane words follow the A15/A19 laws: a read origin names
  its carriers ("carried by: …(read)"), an emptiness rides the house's
  fold phrase (compound on the general road), and **no** empty or failed
  leg reaches a promotion it never earned.
- **M4 — no regression at the live road.** The door record keeps its
  pinned key-set (T161's seven, or the exact eight with `query` where a
  query rode), the over-budget lane stays sparse, the caps hold
  (`max_calls_per_question 8`, `max_secs_per_question 240`, both verbatim
  from the frozen A5 doc), and the suite's 166/166 still stands at the
  close.

Observations, NOT criteria (reported, never scored): whether today's
provider still empties C2's sentence; whether a query's result count or
answer length moved — more results or a longer answer prove nothing by
themselves.

## The attempt budget (§4 law)

One attempt per case (4 of the allowed 8). A retride ONLY at a
runtime/provider error (raise, unreachable, expired cap) — never at an
outcome (an empty search or a laned failure word is DATA, retried at
most to twice). No unbounded retries: if a case still errors at its
second attempt, the comparison stops there and reports, it does not
grind.

## What the run may and may not touch

- The A5 live/search files are **not** re-written: `main` (with its fixed
  `a5-eval-*.json` names) is NOT ridden; the driver rides the runner's
  own per-case unit `run_one(qtext, live, caps, query)` — the A20 idiom,
  A22's 4th argument now spending the query word the A20 report named
  unspent.
- New, clearly named artifacts only:
  `research-hold/a22-eval-live.json` (the machine-readable results,
  A20's envelope idiom: eval word, date, provider, caps, mode, review,
  per-case blocks that embed the FULL `run_one` record verbatim) and
  per-case raw outputs `research-hold/a22-raw-C1..C4.json` (each case's
  complete record, the bytes the mouth saw included).
- **No A20 or historical artifact moves**; `research-eval.json` (EA-0.1)
  stays byte-frozen — A22's queries ride the driver side, the seeker's
  frozen words untouched.
- The review word stays what it always was: **same-family** (the hand
  that wrote the runner reads the record; the GPT bridge key absent at
  A20's count). A plausible answer is never called a supported answer;
  claim-level entailment remains the human's pending.

## Known limits, disclosed before the run

- Day-to-day PROVIDER DRIFT: today's provider bytes may differ from
  A20's; criteria M1–M4 are drift-proof, the observations are not — they
  will be reported with the date, not compared as progress.
- run_one rides its question through TWO roads (the eval's direct search
  plus the door's own fresh research — A20 §2, left undisturbed). An
  attempt therefore speaks for both; a query mismatch between them
  would be a FINDING, and the artifact records both words.
- The A20 run was yesterday (same HEAD minus A22); it is the nearest
  same-family baseline, not an independent one.

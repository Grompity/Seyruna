# A12 — Failed-Source Evidence Integrity Audit

Starting HEAD `26c6f63` (A10); A11 rode untracked as a diagnostic, as A8/A9's
did. Final HEAD: the commit named below — A12 carried a real one-branch fix,
so (per the A6/A7/A10 precedent that a real change carries its report in)
this report rides the commit; the A8–A11 artifacts remain untracked exactly
as found.

## The reproduced data flow (no live request was repeated)

The A11 bytes were re-walked OFFLINE from the frozen artifact/report as a
hand-frozen packet (a recorded-shape replay, not a fixture masquerading as a
witness): the door mints both rows through `web_research.to_rows`; the
failed address rode —

> `row W2 level: DOCUMENTED | kind: None | evidence: NONE-FOR | note:
> blocked-or-rate:403`

— its twin words already honest (kind-SILENCE, the A5 K2 law; `NONE-FOR`;
the lane itself as its note), yet stamped `DOCUMENTED`, exactly as A11's
printed observation and report said. Reproduced at bytes before any fix.

## Root cause (traced, not guessed)

`to_rows` stamps `"level": "DOCUMENTED"` UNCONDITIONALLY in its row literal
(the A4-era stamp, and its own docstring means it — "what the text
VERIFIABLY SAYS"). But the row whose claim is the URL itself (no text, no
snippet; A5's comment at the kind block even NAMES it: *"A URL in the trace
is not yet a DOCUMENTED claim"*) has no text to verifiably say anything:
the label was borrowed. The architecture already owned the hazard's word —
the A2-era RP-07 law (stages.py:401-405) FIRES `RP-07:promotion` at a flat
CLAIM-node whose cites fold below DOCUMENTED — but a silent row stamped
DOCUMENTED folded the fold away, so a flat node citing ONLY a failed
address passed unscolded, authorized as if its bytes had been read.

## The fix (one branch; no new word; no guard weakened)

**The level-word now tracks the kind-word.** A row that rode NO kind word —
HTTP-failed, fetched-but-all-furniture (the empty 200), title-only (K2's own
silence) — rides the enum's OWN `UNKNOWN`; a row with a kind word keeps
`DOCUMENTED`. `UNKNOWN` is a KS-0.1 member that predates the founder's
`DOCUMENTED`, so nothing entered the vocabulary. The direction is A5's P4 law
whole: it may UNDER-count a claim's support, never OVER-count it. The honest
distinctions stand UNTOUCHED: the failed row keeps `NONE-FOR` + its lane-word
note; the empty-200 keeps `http 200` and NO evidence word (bytes without
passage — silence is the truth; the A5 two-word set was deliberately NOT
extended); the read passage keeps `PRESENT`. A URL alone is provenance
metadata, not evidence of the claim at that URL — now true in the words, not
only in the comments.

## Behavior before / after, per the five required shapes

1. HTTP failure, URL-only row: `DOCUMENTED` → **`UNKNOWN`** (kind stays the
   silence, `NONE-FOR` stays, note stays the lane word).
2. Fetched-but-no-usable-passage: `DOCUMENTED` → **`UNKNOWN`** (note `http 200`,
   no evidence word — the insufficiency speaks as silence, as A5 left it).
3. Read passage genuinely supporting a claim: **`DOCUMENTED` unchanged**
   (with `kind page` + `PRESENT`).
4. One readable + one failed at the door: the failed source counts NOTHING
   toward corroboration (`read 1`, `origin_publishers 1`, `independence
   none` — A7's law re-witnessed against A11's frozen bytes), and a flat
   node citing ONLY it now draws the architecture's own
   **`RP-07:promotion`** fire instead of passing silently as DOCUMENTED.
   A11's actual both-cited flat draft likewise now draws the fire — the
   A3 weakest-governs law was pre-existing and stands (disclosed plainly:
   to dodge it, do not cite the failed address flat, or hedge).
5. Existing roads: the searched/auto/no-web doors ride BYTE-UNCHANGED — the
   raising spy proves the searched road is not ridden, and the complete
   prior suite rode green the moment after the code and BEFORE any new
   witness was written (156/156 untouched). A snippet row keeps
   `DOCUMENTED` (it has a kind word; the A5 law unchanged).

## Tests

Deterministic only — no network was touched by A12. Baseline 156/156
(verified at the milestone's start); after the fix alone 156/156 (all prior
pins unmoved); with the two new witnesses **158/158, run twice** (T153 pins
the five word-laws at `to_rows` including the URL-claim and label-claim
bytes themselves; T154 pins the door's promotion speech, the un-fired good
road, the distinction table counting `{DOCUMENTED: 1, UNKNOWN: 1}`, the A7
corroboration words, and the untouched no-web road).

## Changed paths, commit, and the honest last words

`web_research.py` (the one branch + its law-comment), `tests.py`
(T153/T154), `a12-report.md` (this file) — nothing else entered the commit;
the founder's staged bridge set and `opencode.json` rode the index
untouched, `Seyruna/` and the A8–A11 artifacts untracked, CORAL unmoved.
GPT review did NOT run (the process environment inspected, not assumed:
`OPENAI_API_KEY` absent). One limitation named honestly: A11's live artifact
rode on as recorded — A12 did not rewrite the past; the deterministic
re-walk (T154) states what the SAME bytes' words WOULD say with the fix in
place, which is a restatement, not a new live observation. If an
interpretation could not be verified from code or artifacts it would be
said here — none had to be guessed: every word above is at a byte that was
read or a line that ran.

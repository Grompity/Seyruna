# A35 contract — six frozen questions, one honest loop (before the bytes)

## The freeze (bytes read, nothing run)
Committed baseline `ccfd754` (A34 closed), clean tree. The six question
bytes and their A5 expect-words ride `research-eval.json` UNTOUCHED —
EA1 "Ashoka rock edict" … EA6 "Kalama Sutta"; the expect-words ride
ALONGSIDE every disposition and are never rewritten to fit an outcome.
Identity: model `RadixArk/Qwen3.8-Flash-Next-NVFP4`, provider `ddg-ia`
(the packet's own word records it per run anyway), charter
`GENERAL_MAXTOK=1024`, SYNTH absent, THINKING off. Retrieval settings at
their standing constants: RESULTS_N 5, FETCH_MAX 3, MAX_BYTES 1200000,
MAX_CHARS 1200. Caps ride the A5 doc's own: 8 calls / 240 s per stage.
The A34-C1 law rides UNCHANGED into the six — no code-word moves before
the bytes (a fix is earned AFTER, at §6's law). No token-cap work this
sprint unless a real blocker forbids the evaluation.

## The cycle is A34's, entry intact
Each EA question rides the ACTUAL entry `research_eval.run_cycle` at the
doc's own question bytes: stage 1 live (search, source READS, provenance,
the door's web road with A15's status VERBATIM), the gap at the record's
own fields, the A34-C1 follow-up on the A22 rail, stage 2 live, the
byte-comparison, one held label-live artifact per cycle
(`research-hold/a35-cycle-<ID>.json`) plus ONE aggregate
(`a35-six.json`) carrying all six records, the six dispositions, the
cross-words, and the six expect-words beside them. Twelve live searches,
twelve door legs; a missing value STAYS missing (no absent-to-zero).

## BLOCKED, and the one lawful retry
A stage is INFRA-BLOCKED when it spoke `ok False` with a lane-word that
is NOT the honest emptiness ("search-empty") — the net itself refused
(rate-limit, timeout: A19's law that the WORD decides, read the other
way). A cycle with an infra-blocked stage is **BLOCKED**: neither a
research success nor a failure; it rides ONCE re-run (a FRESH live
observation, held as `<ID>.retry.json`, the first bytes PRESERVED);
twice-blocked stays BLOCKED with both bytes shown. A completed cycle
whose follow-up came back EMPTY is NOT blocked — emptiness is the
mission's OWN definition of a retrieval failure, a negative RESEARCH
outcome, kept as one.

## The disposition table (pre-declared, exhaustive, deterministic)
Words: BLOCKED / IMPROVED / RETRIEVAL-FAILURE / DEGRADED / UNRESOLVED /
EVIDENCE-GAP / EQUIVALENT — decided in this ORDER from record fields:
1. either stage infra-blocked -> **BLOCKED** (the retry rides first);
2. the A34 compare says improved -> **IMPROVED** (the strategic flag:
   a RISE in read-origins or voices, or an A15 word crossing to a READ
   origin — bytes only);
3. stage-2 EMPTY -> **RETRIEVAL-FAILURE** (the follow-up's search
   brought nothing; the answer-word says whether the answer FELL to the
   general road (read-1 > 0) or rode EQUIVALENT (it brought nothing
   both times));
4. read-2 < read-1 at a SPOKEN stage 2 -> **DEGRADED** (the follow-up
   LOST footing — the tool's act, an answer-word, never a knowledge lie);
5. NO-ORIGIN at BOTH stages -> **UNRESOLVED** (the web spoke; nothing
   readable stood anywhere);
6. stage-2 NO-ORIGIN/SINGLE-ORIGIN with READ bytes present and no rise
   -> **EVIDENCE-GAP** (the follow-up ARRIVED and the gap STANDS — a
   concrete, auditable negative research finding);
7. else (SUFFICIENT-vs-SUFFICIENT, no movement needed) -> **EQUIVALENT**.

The four FINDING kinds (§3) map from the disposition, deterministically:
BLOCKED stays NEITHER-of-the-four (infra); IMPROVED and
EQUIVALENT-with-read-rides are **RESEARCH FINDING**s (a claim stood on
INSPECTED bytes — A15's word is the witness); EVIDENCE-GAP stands as
**EVIDENCE-GAP**; UNRESOLVED stands as **UNRESOLVED**;
RETRIEVAL-FAILURE and DEGRADED stand as **RETRIEVAL FAILURE**s (the
instrument's doing — a REPEATED one is NOT a recurring knowledge gap,
the mission's own law, printed so). The recorded gap-word rides with
EVERY cycle either way, so a finding never hides its gap.

## The answer-words and the rubric's non-numeric legs
improved / equivalent / degraded come from the table's legs (bytes
only); `response_changed` says the WORDS moved, never BETTER (the
counts-and-lane disclosure from A34 rides UNCHANGED — semantic quality
STAYS UNKNOWN, not zero, not a pass). Relevance is structural-and-
checked: the follow-up carries the question's bytes (the A22 rail) and
the packet's OWN word read-back confirms they RODE — printed per cycle,
NOT claimed as judgment. Independence reads at A7's ceiling word
("candidate", never TRUE); conflict rides the A7 ladder word (which may
well say `insufficient` — a recorded word, not a zero); coverage reads
the LANE-WORD proxy (web lane = carried, general fold = the web brought
nothing) and is DISCLOSED as a proxy, not a measurement.

## The cross-questions, with the recurrence law
Per-cycle dispositions stand FIRST (no aggregate eats a negative).
`cross()` re-computes, from the held records: the tallies; which STAGE
more often came back EMPTY (stage-1 vs stage-2, by the records' OWN
classes — "most often" needs ≥2 against fewer, a single instance is a
SINGLETON and says so); whether EVERY follow-up was GROUNDED
(structurally on the A22 rail, and the read-back matched at all six —
a check, not a discovery); a gap class is **RECURRING** only at ≥2 of
the COMPLETED cycles, else NONE-RECURRING with the singletons named;
the follow-up-emptiness pattern is RECURRING at ≥2 (the trigger for the
reserve fix); and the three epistemic words: SUPPORTED = recomputed
from held bytes by tests, TENTATIVE = single-instance readings,
UNKNOWN = semantic quality (declared, not measured).

## The reserve fix, and its ONLY lawful trigger
The site-scoped second follow-up (ask the READ origin's own site when
the born query came back empty) is implemented ONLY IF the pattern
(gap in {NO-ORIGIN, SINGLE-ORIGIN}) AND (stage-2 SEARCH-EMPTY) appears
at ≥2 completed cycles; else it stays RESERVE, named, unpatched. If any
other defect shows, it must be a CONCRETE bytes-shown failure of the
declared law (not a disliked outcome), and the fix is the SMALLEST one,
with a regression test and a re-run of the affected cycle (disclosed as
fresh live) and the gates.

## Budget, fairness, what may NOT move
Six cycles, twelve searches, no re-runs except the BLOCKED law; NO
re-run to replace an UNFAVORABLE outcome; question bytes as the doc
speaks them; the six ride IN DOC ORDER (EA1..EA6), the order DISCLOSED,
never dressed as a design; T167–T184 whole; NO existing assertion
weakened; the verdict words are NEW at the cycle's edge ONLY — the A34
cycle-words (gap classes, compare) ride UNMOVED; no autonomy claim; no
generalization claim beyond what six records say; nothing pushed.

## SECTION 6 addendum (after the six; before the fix rides)
The six DEMONSTRATED the defect at the contract's own trigger: every
born query came back EMPTY (6/6; five of them in the trigger-class), and
the records name the shape - the head-word is a dotted DOMAIN, which the
provider's search does not answer to. A DISCLOSED DESIGN PROBE (three
plain searches, no door legs, outcome-blind: it weighed no disposition)
showed the provider answers the WORD ("wikipedia ..." -> results, a read
origin) but NEITHER the dotted host verbatim NOR the site: operator.
**A35-C2 (the fix, smallest general):** when the born query rides EMPTY
and the gap is NO-ORIGIN or SINGLE-ORIGIN and the record holds a READ
origin (a row at the READ lane), the follow-up search rides ONCE MORE
headed by the read origin's SITE WORD - the second-to-last dot-part of
the record's own url-host (bytes, not a hand). The born-empty bytes ride
PRESERVED ("stage-2b" beside the stage); the final stage-2 (and the
compare) is the site-scoped one; NO read origin -> NO site -> the retry
does not ride (the provider's own house word is the ABSENCE of a site -
A7's law, EA2's predicted shape). The table (dispose) rides UNMOVED.
**Impacted, re-run LIVE (disclosed fresh):** EA1, EA5, EA6 (the three
with a read origin). EA2/EA3 keep their bytes (NO-SITE - the fix CANNOT
reach them), EA4 keeps his (emptiness EXPECTED at his A5 word). The
FINAL aggregate (a35-six-final.json) = three re-runs + three originals;
every pre-fix byte PRESERVED (the demonstration stands on disk). The
pre-declared prediction (a prediction, not a law): the site-scoped legs
arrive with BYTES and ride to EVIDENCE-GAP (the single wikipedia voice
stands - exactly EA1's expect-shape), NOT to IMPROVED (A35 has yet to
see an improvement; it will print one at bytes if it rides).

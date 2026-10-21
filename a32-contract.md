# A32 contract — written BEFORE the live experiment's outcome

## What is at stake (the A31 ledger's own words)
The finish REASON is not surfaced at the door's trace: `stages.call` READS
`finish_reason` and collapses it to a bool, and `general_exit` DROPS even
that. So the bound A31 installed is INVISIBLE when it bites: the loop today
catches a cap that empties the mouth (the lane is lost) but has no word for
a mouth that was CUT. A32 surfaces the completion metadata end to end and
DEMONSTRATES the bite at the door.

## The metadata that must ride (only as the endpoint SPEAKS it)
- provider `finish_reason` (the raw word; absent is UNKNOWN, never guessed);
- usage `completion_tokens` / `prompt_tokens` / `total_tokens` (present ONLY
  where reported; absence recorded as absence);
- the existing derived bit `truncated` (finish == "length" — the one
  admitted inference, the A29 law, unchanged);
- a SOURCE word beside each family (`finish_src`, `tokens_src`:
  `reported | absent`) so a later reader never mistakes a held field for
  an endpoint that spoke.

The five states stay DISTINGUISHED (no collapsing): provider-reported
length-limit; empty/malformed completion (the A29 lanes); transport failure
(the A28 decomposition, T167, UNMOVED); a valid completed answer; and
missing metadata (UNKNOWN at words, never inferred from a short answer, a
token count, or the configured cap).

## The rails (reuse, no second framework)
`call` returns the extra keys (ADDITIVE - every old reader `.get`s its
three); `general_exit` writes `general_*` trace words (the road under
test's own words, written BEFORE the parse so a lane-lost road still
speaks what bit it); the synth seam writes its `synth_finish*` frame words
through the EXISTING frame→trace whitelist (the A18 idiom);
`loop.measure_door` carries `finish/finish_src/completion_tokens` in its
records; `loop.decide` gains ONE pre-declared clause, gated by the
contract word `reject_reported_length`:

> an after-trial whose finish was REPORTED as `length` is NOT an ordinary
> success — even if the lane rode, the note stayed silent, and the road's
> word rode. A short cut that PARSES is exactly the shape the old table
> would have accepted as fast-and-fine; it must not be. (One wound may
> speak two words — lane-loss caused BY a cut is wound and cause, read
> together, not double-toll.)

The decision VOCABULARY does not grow (APPLIES-HOLDS / ROLLBACK / the two
no-change words ride unchanged); the clause feeds ROLLBACK. Historical
replay safety is REQUIRED: A31's held records carry neither key, so the
clause CANNOT fire on them and T174 must re-decide A31's bytes to the SAME
word with the new code.

## The live demonstration (§4's order fixes the chronology)
1. CONTROL: the proven road, current charter (GENERAL_MAXTOK 1024), ONE
   door run, the FULL trace preserved (label LIVE) - the control decides
   NOTHING, it tells what the road costs in tokens so the candidate can be
   picked at bytes, not taste.
2. CANDIDATE RULE (pre-declared): a cap at or below ONE THIRD of the
   control's REPORTED completion_tokens, kept >= 8 (the endpoint's own
   floor), so a length bite is PLAUSIBLE - chosen from the control,
   written into the machine contract, never retro-fitted to the result.
3. BUDGET: at most TWO candidate values. If the first candidate's road is
   cut, the demonstration is DONE; if it is NOT cut (finish reported stop),
   ONE step down is spent; if the second is not cut either the live
   truncation gate did not pass and is REPORTED so, not papered.
4. THE LAP: `loop.run_lap` at the A32 machine-contract (same entry, same
   eyes): n = 3 before (fresh, the current charter) + 3 after. PRE-DECLARED
   EXPECTED outcome: ROLLBACK with the cut words (this candidate is a
   DEMONSTRATION bite, not a production proposal - the 1024 bound STAYS the
   production word, byte-restored and READ BACK at A31's own law). A STOP
   verdict with no cut anywhere must be reported as a DID-NOT-BITE, and
   the budget spent once more, then honestly.
5. NO CAUSATION CLAIM from latencies (n too small, the A31 disclosure
   stands); the tokens/finish words, not the milliseconds, are A32's
   evidence.

## What must not move
T167–T175 (era-pins may de-pin ONLY where a real shape moved, named); the
T125 raise law; A28's transport decomposition; the shelf exits; the dry
road; the mumble lanes; the two-word law; no assertion weakened to buy
green; replay is never dressed as live.

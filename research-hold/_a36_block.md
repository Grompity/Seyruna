# ---------------- A36: the second voice, tried (adds) ----------------------
# T188 is the SELECTOR, the TABLE, and the ROAD'S OWN LANES at a faked
# fetch (zero net); T189 replays the ONE live read at its held bytes.
import web_research

_A36ART = json.loads(open("research-hold/a35-cycle-EA1.rerun.json").read())
_A36 = {}
_A36["selection"] = {k: v for k, v in
                    research_eval.candidate36(_A36ART).items()
                    if k != "primary"}
_PRIM = {"url": "http://en.wikipedia.org/a", "publisher": "wikipedia.org",
         "kind": "page", "claim": "Ashoka edicts stand."}
_A36["table"] = {
    "lam-infra": research_eval.levels36(
        _PRIM, {"results": [{"error": "timed out"}]})["verdict"],
    "lam-recorded": research_eval.levels36(
        _PRIM, {"results": [{"error": "wrong-kind:image/png"}]})
    ["verdict"],
    "no-bytes": research_eval.levels36(
        _PRIM, {"results": [{"status": 200}]})["verdict"],
    "house-repeat": research_eval.levels36(
        _PRIM, {"results": [{"status": 200, "text": "x",
                             "publisher": "duckduckgo.com",
                             "url": "http://duckduckgo.com/c"}]})
    ["verdict"]}


def _pkt36(pub, txt):
    return {"results": [{"status": 200, "publisher": pub,
                         "url": "http://%s.org/p" % pub, "text": txt}]}


_A36["table"]["distinct-no-share"] = research_eval.levels36(
    _PRIM, _pkt36("acme", "ACME: the stones say three things."))["verdict"]
# a SHARED four-digit year (the ladder's OWN word for share): the primary
# must carry one too - built so:
_A36["table"]["distinct-share"] = research_eval.levels36(
    dict(_PRIM, claim="Ashoka edicts date near 1215 BCE-ish."),
    _pkt36("acme", "ACME dates it 1215 off."))["verdict"]


def _fake_fetch(url, max_bytes=1200000, timeout=8, allow_local=False,
                max_chars=1200):
    return {"status": 200, "url": "http://fin.org/final",
             "kind": "text/html", "body": b"hi there"}


def _lam(url, max_bytes=1200000, timeout=8, allow_local=False,
         max_chars=1200):
    return {"error": "read-failed"}


# THE FRESH-INSTANCE DANCE (the A33 precedent, learned the hard way again):
# the T152/T154 eras LEFT web_research.reads a fixture lambda and the
# A28-era left fetch a spy - the SHARED module is company property. The
# roads legs ride a FRESH web_research and monkey ONLY that copy: the
# pristine code, zero footprints on anyone else's road.
# THE RESET PRECEDENT (the T147 way, learned the hard way again): the
# T152/T154 eras LEFT web_research.reads a fixture lambda and an earlier
# era left fetch a queue-spy - the SHARED module is company property. A36
# rides LAST among the road-riders, so the block RESETS the module to its
# source bytes (importlib.reload - the same word T147 used) and monkeyes
# ONLY fetch, for exactly the legs that need a stood-in page.
import importlib
web_research = importlib.reload(web_research)
_real36 = web_research.fetch
web_research.fetch = _fake_fetch
_A36["roads"] = {}
_r36 = web_research.reads("Q", ["http://h.org/page"])["results"][0]
_A36["roads"]["final-rides-on-redirect"] = _r36.get("final")
_A36["roads"]["no-redirect-no-final-word"] = "final" not in \
    web_research.reads("Q", ["http://fin.org/final"])["results"][0]
_A36["roads"]["dup-url-lane"] = web_research.reads(
    "Q", ["http://a.org/x", "http://a.org/x"])["results"][1].get("skipped")
_A36["roads"]["dup-publisher-lane"] = web_research.reads(
    "Q", ["http://a.org/x", "http://a.org/y"])["results"][1].get("skipped")
web_research.fetch = _lam
_p5 = web_research.reads("Q", ["http://a.org/x"])
_A36["roads"]["lam-rides-as-record"] = (
    _p5["results"][0].get("error"), _p5["gaps"],
    "status" not in _p5["results"][0])
web_research.fetch = _real36                # a fetcher restore, hygiene

_A36["held"] = json.loads(
    open("research-hold/a36-read-EA1.json").read())

expect("T188 THE SELECTOR, THE TABLE, AND THE ROAD'S OWN LANES AT A FAKED "
       "FETCH (zero net): the selector at EA1's held bytes names the "
       "PROBE (no eligible non-house row exists - publishers_seen speaks "
       "the monoculture AT DISCOVERY - so W2, the house stub, rides as "
       "the MEASURER at a word); the TABLE keeps every face lawful (an "
       "INFRA-class lam word BLOCKS; a RECORDED lam word - a status, a "
       "wrong kind - is MONOCULTURE-PERSISTS as a FACT about the address, "
       "A10's record-never-fallback; opened-but-no-bytes the same at its "
       "word; a HOUSE repeat and a PRIMARY repeat both MONOCULTURE at "
       "their words; a DISTINCT origin with bytes but no ladder-SHARE is "
       "DIVERSITY-ONLY, and with the SHARE the ladder itself speaks is "
       "CORROBORATED - the ONLY route to it); and the ROAD, at the faked "
       "fetch, RECORDS the A36 word - the FINAL url rides WHEN a redirect "
       "moved it and the word ABSENTS when it did not, the A7 dedup "
       "lanes (dup-url, dup-publisher) still speak, and a LAMED read "
       "rides as an error WORD in the row and the gaps (the named road's "
       "ok is bool(rows) - a laned failure is a RECORDED failure, the "
       "word decides, never the bool)",
       _A36,
       why=lambda tr: ([] if (
           tr["selection"]["row-id"] == "W2"
           and tr["selection"]["probe"] is True
           and tr["selection"]["publisher"] == "duckduckgo.com"
           and tr["table"]["lam-infra"] == "BLOCKED"
           and tr["table"]["lam-recorded"] == "MONOCULTURE-PERSISTS"
           and tr["table"]["no-bytes"] == "MONOCULTURE-PERSISTS"
           and tr["table"]["house-repeat"] == "MONOCULTURE-PERSISTS"
           and tr["table"]["distinct-no-share"] == "DIVERSITY-ONLY"
           and tr["table"]["distinct-share"] == "CORROBORATED"
           and tr["roads"]["final-rides-on-redirect"]
           == "http://fin.org/final"
           and tr["roads"]["no-redirect-no-final-word"] is True
           and tr["roads"]["dup-url-lane"] == "dup-url"
           and tr["roads"]["dup-publisher-lane"] == "dup-publisher"
           and tr["roads"]["lam-rides-as-record"]
           == ("read-failed", ["read-failed"], True))
       else [k for k, v in (
             ("sel-row", tr["selection"]["row-id"] == "W2"),
             ("sel-probe", tr["selection"]["probe"] is True),
             ("sel-pub", tr["selection"]["publisher"] == "duckduckgo.com"),
             ("lam-infra", tr["table"]["lam-infra"] == "BLOCKED"),
             ("lam-rec", tr["table"]["lam-recorded"]
              == "MONOCULTURE-PERSISTS"),
             ("no-bytes", tr["table"]["no-bytes"] == "MONOCULTURE-PERSISTS"),
             ("house", tr["table"]["house-repeat"]
              == "MONOCULTURE-PERSISTS"),
             ("dnshare", tr["table"]["distinct-no-share"] == "DIVERSITY-ONLY"),
             ("dshare", tr["table"]["distinct-share"] == "CORROBORATED"),
             ("final", tr["roads"]["final-rides-on-redirect"]
              == "http://fin.org/final"),
             ("nofinal", tr["roads"]["no-redirect-no-final-word"] is True),
             ("dupu", tr["roads"]["dup-url-lane"] == "dup-url"),
             ("dupp", tr["roads"]["dup-publisher-lane"] == "dup-publisher"),
             ("lamlane", tr["roads"]["lam-rides-as-record"]
              == ("read-failed", ["read-failed"], True))) if not v]))

_L36 = _A36["held"]
_LV36 = _L36.get("levels", {})
_RD36 = _L36.get("read", {})
_R036 = (_RD36.get("results") or [{}])[0]
_A36_LIVE = {
    "label-live": _L36.get("label") == "live",
    "one-read": _RD36.get("spent", {}).get("fetch") == 1
                and _RD36.get("spent", {}).get("calls") == 1
                and _RD36.get("spent", {}).get("search") == 0,
    "at-address": _RD36.get("results") and
                  _R036.get("url") == _L36["selection"]["url"],
    "status-recorded": _R036.get("status") is not None
                       and _R036.get("lane") == "named",
    "final-word-honest": (_R036.get("final") is not None
                          and _R036.get("final")
                          != _L36["selection"]["url"]
                          and _R036.get("url")
                          == _L36["selection"]["url"]),
    "verdict-honest": (_L36.get("verdict") == "MONOCULTURE-PERSISTS"
                       and _LV36.get("why")
                       == "the road opened but spoke NO bytes"
                       and _LV36.get("A") is False),
    "stage-1-immutable": _L36["question"] == _A36ART["question"]
                         and len(_A36ART["stage-1"]["web"]["rows"]) == 5,
    "charter-untouched": (loop.read_cfg().get("GENERAL_MAXTOK")
                          == stages.CONFIG.get("GENERAL_MAXTOK") == 1024)}

expect("T189 THE ONE LIVE READ AT ITS HELD BYTES (a replay, zero live): "
       "label-live INSIDE (the road touched the net); spent speaks ONE "
       "network read and ZERO searches (the named road's own law PINNED "
       "at bytes - no search discovered a thing); the row rode AT the "
       "SELECTED address at the 'named' lane WITH its status RECORDED; "
       "the final-word law at the LIVE bytes - the probe's URL "
       "REDIRECTED (the /c/ stub to the '?q=' SEARCH-ECHO - A7's zero "
       "MEASURED at bytes), so the word RIDES and the record shows WHERE "
       "(the §6 fix proved at its FIRST live use); the verdict's honesty "
       "at bytes: the road OPENED (a status) but the page spoke ZERO "
       "BYTES - so MONOCULTURE-PERSISTS is the word WITH the word's REA"
       "SON, no spin between opened-and-understood; the stage-1 record "
       "is UNTOUCHED (five rows at their held bytes) and the charter is "
       "UNTOUCHED at file AND mirror - one read wrote NO configuration "
       "word",
       _A36_LIVE,
       why=lambda tr: ([] if all(tr.values()) else
                       ["the live read stopped matching its own words"]))

(the roads legs were mended at bytes into the T147 reset precedent - the fresh-instance dance the draft first tried died on 3.11's shed _path_importer; the block's comment tells the true story; the WHY-lambda was left WEARING EYES (it names its falling legs) as the honest residue of the forensics)

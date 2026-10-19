#!/usr/bin/env python3
"""web_research.py - A4: bounded, source-grounded eyes on the internet.

One module, stdlib only, riding the house seams: the reach is a DESIGNATION,
never ambient (research.py's own law, adopted whole - one named query, one
bounded search, bounded fetches). The A1 task lane gapped the url road
("network-not-designated"); A4 lifts THAT gap for the CONVERSATIONAL road:
the door may ask the web ONCE for the seeker's question, normalize what the
provider's bytes actually SAY (never a wish), and hand the existing
run_pipeline a SHOWN SET it already knows how to speak (the packet lane).
No crawler, no vector store, no second conversation engine.

PROVENANCE LAW (the same one the shelf rides): a record's fields are
ab SENT by the provider's or the page's bytes - absent fields are SILENCE,
never a zero, never an invention (K2). A page that would not open is a
RECORD of failure, not a missing row: its row rides the search's own words
and an error note, and the road to the shelf's plain words stays open.

UNTRUSTED BYTES, NOT COMMANDS: remote text rides as EVIDENCE in the mouth's
contract; it may not move a level, mint a citation, or give an order.
The size law: a page is READ to a cap and its first EXCERPT kept - the
whole page never comes along uninvited.

Provider: SWAPPABLE at one word (config.json's SEARCH_PROVIDER, the
environment's ASCENDED_SEARCH, or the default). As probed on the day of A4
(the live bytes ride a4-report.md): the public SearXNG instances answer
DNS-dead, parked, or 403-behind-an-AUP; DuckDuckGo's html lane shows a
bot-CAPTCHA (202); its INSTANT-ANSWER json lane answers JSON keyless and is
the default. The searxng adapter is shipped and tested against the same
fixture shapes; pointing at it is one config word, no code.
"""
import json
import os
import re
import socket
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request

import stages

# --- the seams (all swappable at the module level; the witnesses use these)
urlopen = urllib.request.urlopen            # the HTTP seam
CTTYPE = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
CTTYPE.check_hostname = False
CTTYPE.verify_mode = ssl.CERT_NONE
UA = "AscendedResearchBot/0.1 (self; A4 bounded research)"
LEDGER = [0]        # the research()'s own CALLS ledger (re-zeroed per run,
                    # the stages.CALLS convention adopted whole)

MAX_BYTES = 1200000     # one response, capped; the excess is DISCARDED
                        # (a real encyclopedic page here is ~0.9M - the cap
                        # is set to let the pages through, not to reject
                        # the canon; a past-it page reads too-big, honestly)
MAX_CHARS = 1200        # the kept excerpt's cap (the page rides its WORDS,
                        # not its bulk)
TIMEOUT = 12            # seconds, connect and read (urlopen's own single arm)
RESULTS_N = 5
FETCH_MAX = 3           # pages fetched per question - the whole point of a budget
MAX_SECS = 120          # the whole research()'s own deadline (pre-request gate)

PROVIDERS = ("ddg-ia", "searxng")


def provider_name():
    """One word, three homes (the config's, the environment's, the default).
    An unknown name is a RAISE at call - a build failure, spoken at once."""
    name = (os.environ.get("ASCENDED_SEARCH")
            or stages.CONFIG.get("SEARCH_PROVIDER") or "ddg-ia")
    if name not in PROVIDERS:
        raise ValueError("web_research: unknown provider " + repr(name)
                          + " (the known: " + ", ".join(PROVIDERS) + ")")
    return name


def search_url(name, query, n):
    """The provider's address built from its own template; the QUERY rides
    quoted - no private bytes beyond the words the seeker spoke."""
    base = (stages.CONFIG.get("SEARCH_BASE")
            or ("http://api.duckduckgo.com" if name == "ddg-ia"
                else "http://searx.org"))
    q = urllib.parse.quote_plus(query)
    if name == "ddg-ia":
        return ("%s/?q=%s&format=json&nohtml&kl=in-en&k1=in&k7=1"
                % (base, q))
    return "%s/search?q=%s&format=json" % (base, q)          # searxng


def _rec(url, title, snippet, lane):
    r = {"url": url}
    if title:
        r["title"] = title
    if snippet:
        r["snippet"] = snippet
    r["lane"] = lane                      # WHERE the bytes rode from (the
    return r                              # provider's own word, never a wish)


def results_from(name, doc):
    """The normalized reading of the provider's json: url/title/snippet,
    SILENCE for absent (K2 adopted - an empty field is not a field). The
    ddg-ia lane rides its own order of goodness: the ABSTRACT first (its
    url the ORIGIN's address), then the DEFINITION (A7: the dictionary's
    own lane, when FILLED - at a Type-"D" doc every text lane may ride
    PRESENT-BUT-EMPTY, and an empty lane is SILENCE), then Results, then
    RelatedTopics - all cut
    by the caller's cap; the searxng lane reads its results[]. Every row
    carries its LANE word (abstract/definition/result/related): the bytes' own
    PROVENANCE-PATH, which the rows later speak as KIND (A5 P3: a reviewer
    can tell fetched-page bytes from the index's snippet from the
    abstract's summary - three different claims-to-evidence, one field)."""
    out = []
    if name == "ddg-ia":
        if doc.get("AbstractText") and doc.get("AbstractURL"):
            # THE ABSTRACT LANE FIRST (the provider's own best answer): its
            # url is the ORIGIN'S address, its text the origin's own words;
            # AbstractSource rides the title-slot (whose-speech, the
            # provider's word - not an invented title).
            out.append(_rec(doc["AbstractURL"],
                            doc.get("AbstractSource") or doc.get("Heading"),
                            doc.get("AbstractText"), "abstract"))
        if doc.get("DefinitionWord") and doc.get("DefinitionURL"):
            # THE DEFINITION LANE (A7): the dictionary's own lane - when
            # FILLED its url is a SECOND origin's address (often apart from
            # the wiki: the one second voice a SINGLE search can hold), and
            # its words the origin's own. The live bytes showed every text
            # lane can ride present-but-empty at a Type-"D" doc; empty is
            # SILENCE (K2 whole), so the row appears only when BOTH the
            # words and the address ride - no invented address, ever.
            out.append(_rec(doc["DefinitionURL"],
                            doc.get("DefinitionSource"),
                            doc.get("DefinitionWord"), "definition"))
        for row in doc.get("Results") or []:
            if row.get("FirstURL"):
                out.append(_rec(row["FirstURL"], row.get("Text"),
                                row.get("Result"), "result"))
        for row in doc.get("RelatedTopics") or []:
            if row.get("FirstURL"):
                out.append(_rec(row["FirstURL"], row.get("Text"),
                                row.get("Result"), "related"))
    else:
        for row in doc.get("results") or []:
            if row.get("url"):
                out.append(_rec(row["url"], row.get("title"),
                                row.get("content"), "result"))
    return out


# ---------- the door-guards (every destination is UNTRUSTED bytes) ----------
def _v4_private(a, b):
    return (a in (0, 10, 127) or (a == 172 and 16 <= b <= 31)
            or (a == 192 and b == 168) or (a == 169 and b == 254)
            or (a == 100 and 64 <= b <= 127))


def safe_target(url, allow_local=False):
    """Scheme, host, and the NON-PUBLIC addresses - as IPv4/IPv6 LITERALS
    (the after-redirect lane re-checks the FINAL url, and an unlisted
    remote's LITERAL form still reads here; a named host's DNS answer is
    checked at the fetch's own risk, documented). Returns (ok, reason)."""
    try:
        scheme, rest = url.split("://", 1)
    except ValueError:
        return False, "no-scheme"
    if scheme.lower() not in ("http", "https"):
        return False, "bad-scheme"
    netloc = rest.split("/", 1)[0].split("?", 1)[0]
    v6 = netloc.startswith("[")
    host = (netloc[1:].split("]", 1)[0] if v6
            else netloc.split(":", 1)[0]).lower()
    if not host:
        return False, "no-host"
    if allow_local:
        return True, None
    if (host == "localhost" or host.endswith(".localhost")
            or host.endswith(".local")):
        return False, "local-name"
    if not v6 and "." in host and all(p.isdigit() for p in host.split(".")):
        parts = [int(p) for p in host.split(".")]
        if len(parts) == 4 and all(0 <= p <= 255 for p in parts):
            return (False, "private-ipv4") if _v4_private(parts[0], parts[1]) \
                else (True, None)
        return False, "bad-ipv4"
    if v6 or (":" in netloc):
        if host in ("::", "::1", "::2") or host == "":
            return False, "private-ipv6"
        if host.startswith(("fe8", "fe9", "fea", "feb")):
            return False, "link-local-ipv6"
        if host.startswith(("fc", "fd")):
            return False, "private-ipv6"
    return True, None


# ---------- the search (ONE request; the failure is a LANED word) ----------
def search(query, n=RESULTS_N, timeout=TIMEOUT):
    """-> (results, gap): results normalized; gap None or the failure's
    class. A raise NEVER travels - the road's law is the laned word."""
    name = provider_name()
    LEDGER[0] += 1
    url = search_url(name, query, n)
    try:
        with urlopen(urllib.request.Request(
                url, headers={"User-Agent": UA,
                              "Accept": "application/json;q=1, */*;q=.5"}),
                timeout=timeout, context=CTTYPE) as r:
            body = r.read(MAX_BYTES + 1)
    except urllib.error.HTTPError as e:
        return [], "search-http-" + str(e.code).split()[0]
    except urllib.error.URLError:
        return [], "search-unreachable"
    except socket.timeout:
        return [], "search-timeout"
    except Exception:
        return [], "search-malformed"
    if len(body) > MAX_BYTES:
        return [], "search-too-big"
    try:
        doc = json.loads(body.decode("utf-8", "replace"))
    except Exception:
        return [], "search-malformed"
    rows = results_from(name, doc)
    return rows[:n], (None if rows else "search-empty")


# ---------- the fetch + the extract (the page rides its WORDS) --------------
def fetch(url, max_bytes=MAX_BYTES, timeout=TIMEOUT, allow_local=False):
    """-> a small dict: {"status": int} on the good road (plus the body,
    whose kind rode) or {"error": class}. Redirects already rode (urlopen's
    own, capped by it); the FINAL url is RE-WEIGHED here - the after-redirect
    lane of the guards. The body cap is a READ-WIDE law: read n+1, discard."""
    ok, reason = safe_target(url, allow_local)
    if not ok:
        return {"error": "blocked:" + reason}
    LEDGER[0] += 1
    try:
        r = urlopen(urllib.request.Request(
            url, headers={"User-Agent": UA, "Accept-Encoding": "identity"}),
            timeout=timeout, context=CTTYPE)
    except urllib.error.HTTPError as e:
        code = str(e.code).split()[0]
        if code in ("403", "429", "402", "503"):
            return {"error": "blocked-or-rate:" + code,
                    "rate": code == "429"}
        return {"error": "http-" + code}
    except urllib.error.URLError:
        return {"error": "unreachable"}
    except socket.timeout:
        return {"error": "timeout"}
    except Exception:
        return {"error": "malformed"}
    with r:
        kind = ""
        try:
            kind = (r.headers.get("Content-Type") or "").split(";")[0] \
                   .strip().lower()
        except Exception:
            kind = ""
        try:
            body = r.read(max_bytes + 1)
        except Exception:
            return {"error": "read-failed"}
        if len(body) > max_bytes:
            return {"error": "too-big"}
        final = getattr(r, "url", url)
        if final != url:
            ok, reason = safe_target(final, allow_local)
            if not ok:
                return {"error": "redirected-to-blocked:" + reason}
            url = final
        out = {"status": r.status, "url": url}
        if kind not in ("text/html", "application/xhtml+xml", "text/plain"):
            return {"error": "wrong-kind" + (":" + kind if kind else ":none")}
        out["kind"] = kind
        out["body"] = body
        return out


TAGOUT = re.compile(r"(?is)<(script|style|nav|footer|header|aside|form|"
                    r"fieldset|figure|noscript|template|svg|head)\b.*?</\1\s*>")
TAGS = re.compile(r"(?s)<[^>]*>")
SPACES = re.compile(r"[\s\u00a0]+")


THIN = 60     # a LINE thinner than this reads as FURNITURE at the page road
              # (a title, a jump-link, a tagline - the A4-live witness: the
              # wikipedia claim rode "…Jump to content…From Wikipedia, the
              # free encyclopedia…" where its lead paragraph waited). THE
              # LAW RIDES PAGES ONLY (a snippet passes thin=0 - a short
              # TRUE sentence is no chrome at the index's lane); and its
              # limit is stated: a short TRUE line at a page can fall to it.

def extract(html, max_chars=MAX_CHARS, thin=THIN):
    """Readable text, then the CAP: the page is NOT kept - the first
    excerpt is. Scripts, styles, and the navigation furniture go FIRST
    (a menu of forty links is not a page's speech); the BLOCK ENDS hold
    the lines apart (A5: the chrome of a page is a THIN LINE, and a
    paragraph's speech is not); remote javascript is never RUN, only read.
    A cut excerpt RIDES ITS OWN MARK - truncation that speaks is not a
    claim of completeness."""
    t = TAGOUT.sub(" ", html)
    t = re.sub(r"(?s)<!--.*?-->", " ", t)
    # THE ESCAPED-MARKUP CLAUSE (A6, the ONE intervention the review
    # justified): some sites (observed LIVE at EA1/EA5's wikipedia-family
    # pages) serve their markup ALREADY ESCAPED - &lt;b ...&gt; - so the
    # tag-saw (a real <...>) sees NO tags and the claim drowns in attribute
    # shavings. The clause cuts escaped spans and their residue-RUNS
    # ("}'> - three or more of quote-brace-angle-quote in a row is no
    # prose); multi-script bytes (Bengali, Burmese) ride UNTOUCHED (the
    # residue class is four characters, not a script). The span CLOSES at
    # a real > OR at &gt; - the live bytes close almostEVERY escape with a
    # REAL > (only the < is escaped), and a law that required &gt; matched
    # NOTHING: the standalone probe caught that BEFORE any witness rode.
    t = re.sub(r"(?s)&lt;.*?(?:>|&gt;)", " ", t)
    t = re.sub(r"[\"'}>]{3,}", " ", t)
    t = re.sub(r"(?i)</(p|li|h[1-6]|div|section|blockquote|dd|dt|br)\s*>",
                "\n", t)
    t = re.sub(r"(?i)<br\s*/?>", "\n", t)
    t = TAGS.sub(" ", t)
    lines = []
    for ln in t.split("\n"):
        ln = SPACES.sub(" ", ln).strip()
        if ln and len(ln) >= thin:
            lines.append(ln)
    out = " ".join(lines)
    if len(out) > max_chars:
        return out[:max_chars - 1].rstrip() + "…"
    return out


def provider_host(name=None):
    """The provider's OWN house (its result-lanes that ride it are
    ATTRIBUTION - a redirect to the answer, not a second voice; the A4-live
    bytes showed the ddg-ia FirstURL lane riding duckduckgo.com's own stub
    pages while the ABSTRACT rode the ORIGIN). Derived from the provider's
    own search_url, so a config move moves it along; the "api." porch is
    the provider's own front door, not its house."""
    h = urllib.parse.urlparse(search_url(name or provider_name(), "x", 1))[1]
    parts = h.lower().split(".")
    if parts[0] == "api":
        parts = parts[1:]
    return ".".join(parts)


# ---------- A7: the IDENTITY laws (a publisher is not a host; a road is
# not a cloth). THE DIRECTION IS CHOSEN ON PURPOSE: both laws may UNDER-
# count (read two voices as one), neither may OVER-count - the counts may
# HIDE an independence, never INVENT one (A5's P4 law, adopted whole).
SECOND = ("com", "co", "net", "org", "ac", "gov", "edu", "or", "ne", "go")
#   the second-labels that ride UNDER a two-letter country code (the
#   bbc.co.uk shape). The set is a CHOICE, stated; an unlisted shape falls
#   to the two-label law and UNDER-counts.


def publisher(target):
    """The ORIGIN'S identity: the registrable domain of the host - the last
    two labels, or THREE when the second is a second-level word under a
    two-letter country code. en.wikipedia.org and de.wikipedia.org are ONE
    voice (the A5 host-count INFLATED them into two); www. is no label and
    a port rides no weight; unicode hosts are NOT decoded (a puny-form
    reads apart from its decoded twin - apart, never wrongly-collapsed).
    Accepts an address OR a bare host."""
    h = urllib.parse.urlparse(target).netloc or target
    h = h.split(":")[0].strip(".").lower()
    parts = h.split(".")
    if len(parts) > 1 and parts[0] == "www":
        parts = parts[1:]
    if len(parts) >= 3 and parts[-2] in SECOND and len(parts[-1]) == 2:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:]) if len(parts) >= 2 else h


TRACKED = ("gclid", "gbraid", "fbclid", "msclk", "igoid", "_ga", "gclsrc",
           "fb_action_id", "fb_source", "ref_src", "spm")


def canon_url(url):
    """The address WITHOUT its tracking clothes: the fragment falls (the
    provider's #kp anchors are no second road), and the NAMED tracking
    params fall (the utm_ family, the click-ids, the social pixels); a
    param that carries MEANING (?action=edit!) rides on, and a PATH is
    never collapsed (distinct pages of one site never merge into one
    address). A param not NAMED rides too - the conservative direction
    again: over-split at worst, two addresses that MIGHT be one road."""
    parts = urllib.parse.urlsplit(url.split("#", 1)[0])
    kept = [kv for kv in parts.query.split("&")
            if kv and kv.split("=", 1)[0] not in TRACKED
            and not kv.startswith("utm_")]
    return "%s://%s%s%s" % (parts.scheme.lower(), parts.netloc.lower(),
                            parts.path.rstrip("/") or "/",
                            ("?" + "&".join(kept)) if kept else "")


def corroboration(packet, name=None):
    """The narrow evidence-quality word (A5 P4): COUNTS, never claims.
    How many ADDRESSES rode (urls), how many PAGES were actually READ
    (read - bytes in hand, not a status code), how many of the addresses
    are the provider's OWN house (attribution: a syndicated redirect is
    not a second voice - three stub-URLs on the house count as none, and
    three URLs on one publisher count as ONE publisher), how many ORIGIN
    publishers stand behind READ bytes, and the conservative INDEPENDENCE
    word:
      "none"      - one origin voice read (or none) - nothing corroborated
      "candidate" - >=2 distinct origin publishers READ (two publishers
                    MAY corroborate; domain difference alone proves nothing
                    - the word says candidate, never TRUE)
      "unknown"   - origin addresses exist but no origin was READ (bytes
                    not in hand: no counting a page never opened).
    A5's limits were stated; A7 MOVES ONE of them and ADDS, never loosens:
    the counts now ride PUBLISHERS not hosts (en.wikipedia.org and
    de.wikipedia.org are ONE voice - the host-count INFLATED); publishers-
    seen says how many origin voices the provider SPOKE at all (read or
    not - what COULD have been weighed); duplication counts the picker's
    dup-words (a tracking-clothed twin and a re-road of one publisher are
    ONE road); and two READ passages of DIFFERENT publishers whose bytes
    are IDENTICAL raise the syndicated flag (two addresses may be one
    voice; syndication is DETECTED here, never ASSUMED away).
    THE CONFLICT word moves from a blanket unknown to a LADDER, humble by
    its words:
      "insufficient"          - fewer than two origin voices READ: there is
                                NOTHING to weigh (the A4/EA4 truth; the
                                blanket unknown hid that the looking itself
                                was too thin)
      "unknown"               - two voices read, the bytes carry no year-
                                worth comparison (a stated limit - the real
                                contradiction-home stays the shelf's own
                                DISAGREEMENT lanes; a contradiction a
                                passage resolves by TONE stays outside
                                every machine here)
      "bytes-share"           - two READ publishers SHARE a year-shaped
                                number - the BYTES agree (two voices can
                                still BOTH be wrong: agreement of bytes is
                                not entailment - A5's law kept whole)
      "bytes-clash-possible"  - both voices carry years, NONE is shared:
                                the disagreement is KEPT, not averaged -
                                and NOT proven (two pages may simply
                                speak of different facts; the -possible
                                tail is the whole point, the rows both
                                ride on regardless - nothing chooses)
    Independence is NEVER asserted."""
    ph = provider_host(name)
    hosts = [urllib.parse.urlparse(r["url"])[1].lower()
             for r in packet["results"]]
    pubs = [publisher(h) or "?" for h in hosts]
    origins = [(p, r) for p, r in zip(pubs, packet["results"]) if p != ph]
    read = sorted({p for (p, r) in origins if r.get("text")})
    if len(read) >= 2:
        word = "candidate"
    elif len(read) == 1:
        word = "none"
    else:
        word = "unknown"
    if len(read) < 2:
        conflict = "insufficient"                     # nothing to weigh
    else:
        years = {}
        for p, r in origins:
            if r.get("text"):
                years.setdefault(p, set()).update(
                    {n for n in re.findall(r"\b\d{4}\b", r["text"])
                     if "1000" <= n <= "2199"})
        voiced = [v for p, v in sorted(years.items()) if v]
        if len(voiced) < 2:
            conflict = "unknown"
        elif any(voiced[i] & voiced[j]
                 for i in range(len(voiced))
                 for j in range(i + 1, len(voiced))):
            conflict = "bytes-share"
        else:
            conflict = "bytes-clash-possible"
    pairs = {(p, r["text"]) for p, r in origins if r.get("text")}
    return {"urls": len(packet["results"]),
            "read": sum(1 for r in packet["results"] if r.get("text")),
            "attribution": sum(1 for p in pubs if p == ph),
            "origin_publishers": len(read),
            "independence": word, "conflict": conflict,
            "publishers_seen": len({p for p, r in origins}),
            "duplication": sum(1 for r in packet["results"]
                               if str(r.get("skipped") or "")
                               .startswith("dup")),
            "syndicated-possible": len({t for _, t in pairs}) < len(pairs)}


# ---------- the packet: the same words the pipeline already speaks ----------
def research(query, results_n=RESULTS_N, fetch_n=FETCH_MAX,
             max_bytes=MAX_BYTES, max_chars=MAX_CHARS,
             allow_local=False, timeout=TIMEOUT, clock=time.perf_counter):
    """One question, one bounded look: search ONCE, fetch up to fetch_n,
    every failure LANED (a class on the record), nothing invented."""
    LEDGER[0] = 0
    t0 = clock()
    rows, gap = search(query, results_n, timeout)
    spent = {"search": LEDGER[0]}
    fetched = 0
    if rows:
        seen_urls, read_pubs = set(), set()
        for rec in rows:                                    # A7: the coins
            if fetched >= fetch_n:                          # ride PUBLISHERS
                break                                       # (not the first
                                                            # N addresses)
            if clock() - t0 >= MAX_SECS:                    # the budget's word
                rec["skipped"] = "budget"
                continue
            pub = publisher(rec["url"])
            rec["publisher"] = pub                          # the lineage rides
            rec["canon"] = canon_url(rec["url"])            # EVERY walked row
            if rec["canon"] in seen_urls:
                rec["skipped"] = "dup-url"                  # the selfsame road
                continue                                    # in new clothes
            if pub in read_pubs:
                rec["skipped"] = "dup-publisher"            # a publisher READ
                continue                                    # once speaks once
            seen_urls.add(rec["canon"])
            got = fetch(rec["url"], max_bytes, timeout, allow_local)
            if "status" in got:
                rec["status"] = got["status"]
                rec["retrieved"] = time.strftime("%Y-%m-%dT%H:%M:%S")
                rec["text"] = extract(got["body"].decode("utf-8", "replace")
                                      if isinstance(got["body"], bytes)
                                      else str(got["body"]), max_chars)
                read_pubs.add(pub)                          # a failed look is
                fetched += 1                                # NOT a voice -
            else:                                           # the house may
                rec["error"] = got["error"]                 # speak again
    spent["fetch"] = fetched
    spent["calls"] = LEDGER[0]
    spent["ms"] = round((clock() - t0) * 1000, 1)
    gaps = ([gap] if gap else []) + [r["error"] for r in rows if "error" in r]
    return {"query": query, "provider": provider_name(), "ok": bool(rows),
             "results": rows, "gaps": gaps, "spent": spent}


SENTENCE = re.compile(r"(?<=[.!?])\s+")


def to_rows(packet, max_chars=MAX_CHARS):
    """The packet AS shelf rows: the same fields the shelf speaks, so the
    pipeline needs no new organ. claim = the page's OWN first words (the
    fetched excerpt) or the search's own words - NEVER a summary of what
    the page might mean. level DOCUMENTED is the honest word (what the
    text verifiably says - and the note says HOW it was seen)."""
    rows, ids = [], []
    for i, rec in enumerate(packet["results"]):
        rid = "W%d" % (i + 1)
        ids.append(rid)
        if rec.get("text"):
            claim = SENTENCE.split(rec["text"])[0][:max_chars]
        else:
            # A snippet rides the SAME furniture-removal law as a page (the
            # provider's Result-field can carry anchor markup) - but at
            # thin=0: the THIN LINE law is a PAGE law, and the index's short
            # true words are no chrome.
            claim = extract(rec.get("snippet") or rec.get("title")
                            or rec["url"], max_chars, 0)
        row = {"id": rid, "claim": claim, "level": "DOCUMENTED",
               "provenance": "web", "work": urllib.parse.urlparse(rec["url"])[1],
               "publisher": rec.get("publisher") or publisher(rec["url"]),
               "canon": rec.get("canon") or canon_url(rec["url"]),
               "edges": []}
        # THE KIND-LANE (A5 P3, the traceability word): page bytes, the
        # origin's own ABSTRACT, or the index's SNIPPET - three different
        # claims-to-evidence that a URL alone cannot tell apart. A row with
        # only a title (or only an address) rides NO kind word: silence is
        # the truth (K2). A URL in the trace is not yet a DOCUMENTED claim;
        # the kind word says WHAT KIND of seeing the bytes got.
        if rec.get("text"):
            row["kind"] = "page"
        elif rec.get("snippet"):
            row["kind"] = ("abstract" if rec.get("lane") in ("abstract",
                                                             "definition")
                           else "snippet")
        if rec.get("text"):
            row["evidence"] = "PRESENT"
        elif rec.get("error") or rec.get("skipped"):
            row["evidence"] = "NONE-FOR"
        if rec.get("status") is not None:
            row["note"] = "http " + str(rec["status"])
            if (rec.get("text") or "").endswith("…"):
                row["note"] += " (capped)"       # truncation SPEAKS (P5)
        elif rec.get("error"):
            row["note"] = rec["error"]
        elif rec.get("skipped"):
            row["note"] = "not-fetched:" + rec["skipped"]
        if rec.get("retrieved"):
            row["loculus"] = rec["retrieved"]
        row["url"] = rec["url"]
        rows.append(row)
    return rows, ids

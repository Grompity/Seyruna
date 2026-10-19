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


def _rec(url, title, snippet):
    r = {"url": url}
    if title:
        r["title"] = title
    if snippet:
        r["snippet"] = snippet
    return r


def results_from(name, doc):
    """The normalized reading of the provider's json: url/title/snippet,
    SILENCE for absent (K2 adopted - an empty field is not a field). The
    ddg-ia lane rides its own order of goodness: the ABSTRACT first (its
    url the ORIGIN's address), then Results, then RelatedTopics - all cut
    by the caller's cap; the searxng lane reads its results[]."""
    out = []
    if name == "ddg-ia":
        if doc.get("AbstractText") and doc.get("AbstractURL"):
            # THE ABSTRACT LANE FIRST (the provider's own best answer): its
            # url is the ORIGIN'S address, its text the origin's own words;
            # AbstractSource rides the title-slot (whose-speech, the
            # provider's word - not an invented title).
            out.append(_rec(doc["AbstractURL"],
                            doc.get("AbstractSource") or doc.get("Heading"),
                            doc.get("AbstractText")))
        for row in doc.get("Results") or []:
            if row.get("FirstURL"):
                out.append(_rec(row["FirstURL"], row.get("Text"),
                                row.get("Result")))
        for row in doc.get("RelatedTopics") or []:
            if row.get("FirstURL"):
                out.append(_rec(row["FirstURL"], row.get("Text"),
                                row.get("Result")))
    else:
        for row in doc.get("results") or []:
            if row.get("url"):
                out.append(_rec(row["url"], row.get("title"),
                                row.get("content")))
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
                    r"fieldset|figure|noscript|template|svg)\b.*?</\1\s*>")
TAGS = re.compile(r"(?s)<[^>]*>")
SPACES = re.compile(r"[\s\u00a0]+")


def extract(html, max_chars=MAX_CHARS):
    """Readable text, then the CAP: the page is NOT kept - the first
    excerpt is. Scripts, styles, and the navigation furniture go FIRST
    (a menu of forty links is not a page's speech); remote javascript is
    never RUN here, only read."""
    t = TAGOUT.sub(" ", html)
    t = re.sub(r"(?s)<!--.*?-->", " ", t)
    t = TAGS.sub(" ", t)
    t = SPACES.sub(" ", t).strip()
    return t[:max_chars]


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
        for rec in rows[:fetch_n]:
            if clock() - t0 >= MAX_SECS:                 # the budget's own word
                rec["skipped"] = "budget"
                continue
            got = fetch(rec["url"], max_bytes, timeout, allow_local)
            if "status" in got:
                rec["status"] = got["status"]
                rec["retrieved"] = time.strftime("%Y-%m-%dT%H:%M:%S")
                rec["text"] = extract(got["body"].decode("utf-8", "replace")
                                      if isinstance(got["body"], bytes)
                                      else str(got["body"]), max_chars)
                fetched += 1
            else:
                rec["error"] = got["error"]
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
            # provider's Result-field can carry anchor markup - remote bytes
            # are data, and markup is the least of it).
            claim = extract(rec.get("snippet") or rec.get("title")
                            or rec["url"], max_chars)
        row = {"id": rid, "claim": claim, "level": "DOCUMENTED",
               "provenance": "web", "work": urllib.parse.urlparse(rec["url"])[1],
               "edges": []}
        if rec.get("text"):
            row["evidence"] = "PRESENT"
        elif rec.get("error") or rec.get("skipped"):
            row["evidence"] = "NONE-FOR"
        if rec.get("status") is not None:
            row["note"] = "http " + str(rec["status"])
        elif rec.get("error"):
            row["note"] = rec["error"]
        elif rec.get("skipped"):
            row["note"] = "not-fetched:" + rec["skipped"]
        if rec.get("retrieved"):
            row["loculus"] = rec["retrieved"]
        row["url"] = rec["url"]
        rows.append(row)
    return rows, ids

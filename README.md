# Ascended AI — Landing (Prototype I)

A design-first landing page. Not a product, not a CMS — a visual and
interactive argument for what Ascended AI *is*: a place where old languages
of inquiry and new machine intelligence meet, with layers that reward
attention.

**Run:** `python3 server.py` (static server on http://127.0.0.1:5173 that
answers every response with `Cache-Control: no-store`, so a hot edit is
visible on the very next reload). Zero build step, zero dependencies —
`server.py` is only the stock Python HTTP server plus one header. Module
imports carry a `?v=2` stamp so a browser that cached an older copy is
forced onto fresh cache keys; bump the stamp (or rely on no-store) after
breaking edits.

**Stack:** semantic HTML · CSS custom properties (design tokens) · vanilla
custom elements (one concern, one file). Chosen deliberately: a landing
experience should load instantly, degrade fully without JS, and be portable
into any framework later without a rewrite.

---

## Layout

```
index.html                 static content lives here (SEO, no-JS readable)
favicon.svg                the vesica — the same mark as the hero + finale
css/
  tokens.css               ALL colours, type, rhythm, motion knobs
  base.css                 ground, buttons, veil, grain, secret, reveal
  <component>.css          one per component
js/
  main.js                  boot: components, marginalia, reveals, the typed door
  data/                    the symbolic layer — content kept out of components
    geometry.js            the hero artifact, as pure parameters
    constellation.js       the knowledge web: nodes, wires, dust field
    marginalia.js          the margin whispers
    copy.js                the two discoveries
  lib/                     shared behaviour
    motion.js              reduced-motion guard, threshold glide
    reveal.js              scroll reveals (opt-in; visible without JS)
    dust.js                canvas motes + pointer field
    sequence.js            the typed door
    marginalia.js          mounts the margin marks
  components/              custom elements, one per section
    navigation-frame.js    near-invisible until woken; mobile dialog
    hero-threshold.js      first screen, pointer parallax, the light answer
    sacred-geometry.js     renders the artifact from data/geometry.js
    philosoph-section.js   staggers the creed
    knowledge-constellation.js  interactive star map (buttons + svg wires)
    ancient-future.js      manuscript spiral + machine grid, drawn by code
    source-section.js      names fade in when the field is in view
    final-threshold.js     the closing mark
```

## The project files (beyond the site)

- `foundation.md` — the ASCENDED FOUNDATION DOCUMENT (v0.1): philosophy,
  constitution, epistemology, architecture, roadmap, open questions.
- `constitution.md` — the law (Floor, Stair, Voice, Gate, Obsolescence).
  The site is its first working illustration.

## The symbolic layer

- **The vesica (two intersecting circles)** is the site's only signature:
  favicon → hero artifact core → a margin whisper → the last dim mark in
  the darkness. It means, within this site, "where two things meet." No
  historical or religious claim is made for it.
- **Marginalia**: pure geometric marks (circle-dot, spiral, an abstract
  returning ring — *not* copied traditional symbols). Each whispers one
  original line on hover/focus.
- Every phrase on the page is original copy, written to sit beside both a
  scientist and a monk without preaching to either.

## The discoveries (do not announce them; they are documented only here)

1. **The light** — the central point of the hero artifact answers a click
   once: a whisper in the hero: *"You were already looking."*
2. **The typed door** — typing `ascend` anywhere reveals one line near the
   foot of the page: the sentence the site refuses to shout.
3. **The seam** — the final mark *is* the hero geometry; the page ends inside
   the shape it began in.
4. **The margins** — five marginalia, one per section, that whisper to the
   attentive (mouse or Tab — keyboard-reachable, never announced).

## Design rules for future editors

- Gold is sacred: never larger or more frequent than it is today.
- Motion vocabulary is *breathe, orbit, drift, awaken* — never bounce, slide,
  pop. All timings live in `tokens.css`.
- `prefers-reduced-motion` is honoured site-wide (CSS kills animation,
  components render static geometry and a single dust frame).
- Sound architecture is intentionally absent; add it behind an explicit,
  default-muted affordance if ever.
- Copy guardrails: no promises, no "unlock", no "next-generation", no
  claims about souls, traditions, or ultimate anything.
- New sections: one file in `components/`, one stylesheet, copy either in
  `index.html` (static/SEO content) or in `data/` (symbolic content).

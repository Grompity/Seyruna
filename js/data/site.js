/**
 * Site — the single brand configuration for the Seyruna company site.
 *
 * SEYRUNA is the company / studio. ASCENDED is its flagship project. This is the
 * one place identity is written; components read from it rather than hard-coding
 * the name. The visible page keeps its literal names too (so it reads and is
 * crawlable without JS); this module is the source that drives the live/derived
 * labels and the one real route (the flagship anchor).
 *
 * No framework, no fetch, no secrets. If the branding must change later, it
 * changes here first.
 */
export const SITE = {
  company: 'Seyruna',
  role: 'an independent studio',
  tagline: 'We build technology for human understanding.',

  domain: 'seyruna.com',
  url: 'https://seyruna.com/',

  // The flagship project — not renamed.
  project: 'Ascended',
  projectPosition: 'A system for exploring what humanity has already thought, and the hard questions it has never settled.',
  // The flagship lives on this same page for now, so the flagship CTA anchors
  // in-page (no dead link). Point this at the product domain once it deploys.
  projectUrl: '#ascended',

  // Company-only for now. The X account is owned but not yet furnished, so it
  // is deliberately not linked; when it earns its place it drops into this
  // array and the footer renders it.
  social: [],
  contact: 'founder@seyruna.com',
  year: 'MMXXVI',

  // Live labels (public phrasing; the internal word "shelf" stays private).
  status: {
    working: 'is reading',
    failed: 'did not answer',
  },
}

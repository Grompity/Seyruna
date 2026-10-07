import { SITE } from '../data/site.js?v=7'

/**
 * A minimal brand hydrator. The page keeps its literal names in the HTML so it
 * is crawlable and readable with no JavaScript; this stamps the derived bits —
 * the one real route (the flagship anchor) and the recurring wordmark/year — so
 * identity is configured in ONE place (`data/site.js`) instead of copied across
 * the components. Pure text/attribute writes; no structure changes.
 */
export function mountBrand(root = document) {
  const stamp = (name, value, as) => {
    for (const el of root.querySelectorAll(`[data-brand="${name}"]`)) {
      if (as) el.setAttribute(as, value)
      else el.textContent = value
    }
  }
  stamp('company', SITE.company)
  stamp('role', SITE.role)
  stamp('year', SITE.year)
  stamp('project', SITE.project)
  // The flagship route (defaults to the on-page anchor; a product domain can be
  // swapped into site.js and every marked link follows).
  stamp('project-href', SITE.projectUrl, 'href')
}

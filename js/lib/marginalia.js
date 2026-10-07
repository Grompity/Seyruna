import { MARGINALIA } from '../data/marginalia.js?v=7'
import { glyphSVG } from '../components/glyphs.js?v=7'

/**
 * Places marginal marks in each section that declares them. Each mark is a
 * focusable whisper — discoverable by mouse, by tab, by patience.
 */
export function mountMarginalia(root = document) {
  for (const host of root.querySelectorAll('[data-marginalia]')) {
    const items = MARGINALIA[host.dataset.marginalia] ?? []
    for (const [i, item] of items.entries()) {
      const btn = document.createElement('button')
      btn.type = 'button'
      btn.className = 'marginalia__mark'
      btn.setAttribute('aria-label', `Marginal mark ${i + 1}`)
      btn.innerHTML = `${glyphSVG(item.kind)}<span class="marginalia__whisper">${item.text}</span>`
      host.append(btn)
    }
  }
}
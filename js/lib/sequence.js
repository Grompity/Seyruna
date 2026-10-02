import { SEQUENCE, COPY } from '../data/copy.js?v=2'

/**
 * The typed door. Reading the word `ascend` anywhere on the page — not a menu,
 * not a button — lets the page say the one thing it would rather imply.
 */
export function initSecret() {
  const node = document.querySelector('.secret')
  if (!node) return
  let buffer = ''
  let timer = null

  const say = () => {
    node.textContent = COPY.secret
    node.classList.add('is-said')
    clearTimeout(timer)
    timer = setTimeout(() => node.classList.remove('is-said'), 9500)
  }

  document.addEventListener('keydown', (e) => {
    if (e.metaKey || e.ctrlKey || e.altKey || e.key.length !== 1) return
    const t = e.target
    if (t instanceof HTMLElement && (t.isContentEditable || /^(input|textarea|select)$/i.test(t.tagName))) return
    buffer = (buffer + e.key.toLowerCase()).slice(-SEQUENCE.length)
    if (buffer === SEQUENCE) {
      buffer = ''
      say()
    }
  })
}
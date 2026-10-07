import { prefersReducedMotion } from './motion.js?v=7'

/**
 * Scroll reveals. Content is readable without JavaScript; the hidden state is
 * only ever applied when the `js` class is present on <html>.
 */
export function initReveals() {
  const els = [...document.querySelectorAll('[data-reveal]')]
  if (!els.length) return
  if (prefersReducedMotion() || !('IntersectionObserver' in window)) {
    els.forEach((el) => el.classList.add('is-revealed'))
    return
  }
  const io = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue
      entry.target.classList.add('is-revealed')
      io.unobserve(entry.target)
    }
  }, { threshold: 0.15, rootMargin: '0px 0px -8% 0px' })
  els.forEach((el) => io.observe(el))
}
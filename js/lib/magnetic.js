import { prefersReducedMotion } from './motion.js?v=8'

/**
 * Magnetic threshold buttons — the cursor pulls a threshold, at most about
 * a fifth of the way, and it springs home on the way out. Two-state design
 * plus feedback under 300ms is the whole rule; only the two threshold
 * buttons on the page qualify, which keeps the animated share of the screen
 * small on purpose. CSS owns the motion (--mx/--my ride the button
 * transform in base.css); this file only reports the cursor, rAF-throttled.
 * Hover-coarse devices and reduced motion: nothing is wired.
 */
export function initMagnetic() {
  if (prefersReducedMotion()) return
  if (!window.matchMedia?.('(hover: hover) and (pointer: fine)').matches) return
  const els = [...document.querySelectorAll('.btn--threshold')]
  if (!els.length) return

  const RADIUS = 130
  const PULL = 0.22

  let last = null
  let queued = false

  const apply = () => {
    queued = false
    if (!last) return
    for (const el of els) {
      const r = el.getBoundingClientRect()
      const dx = last.x - (r.x + r.width / 2)
      const dy = last.y - (r.y + r.height / 2)
      const near = Math.max(0, 1 - Math.hypot(dx, dy) / RADIUS)
      el.style.setProperty('--mx', `${(dx * PULL * near).toFixed(1)}px`)
      el.style.setProperty('--my', `${(dy * PULL * near).toFixed(1)}px`)
    }
  }

  document.addEventListener('pointermove', (e) => {
    last = { x: e.clientX, y: e.clientY }
    if (!queued) {
      queued = true
      requestAnimationFrame(apply)
    }
  }, { passive: true })
}

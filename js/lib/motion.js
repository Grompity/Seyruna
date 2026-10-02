export const prefersReducedMotion = () =>
  window.matchMedia?.('(prefers-reduced-motion: reduce)')?.matches === true

/** Scroll to a target; `veil` fades the page through darkness first, like crossing a threshold. */
export function glideTo(selector, { veil = false } = {}) {
  const target = document.querySelector(selector)
  if (!target) return
  const reduce = prefersReducedMotion()
  const curtain = veil ? document.querySelector('.veil') : null
  if (curtain && !reduce) {
    curtain.classList.add('is-on')
    setTimeout(() => target.scrollIntoView({ behavior: 'smooth', block: 'start' }), 430)
    setTimeout(() => curtain.classList.remove('is-on'), 1000)
  } else {
    target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' })
  }
}
export const prefersReducedMotion = () =>
  window.matchMedia?.('(prefers-reduced-motion: reduce)')?.matches === true

/** Same feature detection as the CSS gate (supports at-rule). */
const vtReady = () => {
  try { return CSS.supports('at-rule(@viewtransition)') === true } catch { return false }
}

/** Scroll to a target; `veil` fades the page through darkness first, like crossing a threshold. */
export function glideTo(selector, { veil = false } = {}) {
  const target = document.querySelector(selector)
  if (!target) return
  const reduce = prefersReducedMotion()
  const curtain = veil ? document.querySelector('.veil') : null
  if (curtain && !reduce) {
    curtain.classList.add('is-on')
    setTimeout(() => arrive(selector, target, reduce), 430)
    setTimeout(() => curtain.classList.remove('is-on'), 1000)
  } else {
    arrive(selector, target, reduce)
  }
}

/** Arrival. Where the at-rule ships, the journey is a real navigation — a
 *  push, a morph of the wordmark, an arrival. Where it doesn't, the page
 *  simply walks, as it always did. */
function arrive(selector, target, reduce) {
  if (!reduce && vtReady() && /^#[\w-]+$/.test(selector)) {
    history.pushState({}, '', selector)
    target.scrollIntoView({ behavior: 'auto', block: 'start' })
    return
  }
  target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' })
}

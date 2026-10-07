import { prefersReducedMotion } from '../lib/motion.js?v=7'

/**
 * The names. They are not claimed to be one word — only gathered, the way a
 * museum gathers pottery shards from different coasts.
 */
export class SourceSection extends HTMLElement{
  connectedCallback() {
    if (this._wired) return
    this._wired = true
    const words = [...this.querySelectorAll('.source-words li')]
    const show = () => {
      words.forEach((li, i) => {
        li.style.setProperty('--d', `${240 + i * 110}ms`)
        li.classList.add('is-listen')
      })
    }
    if (prefersReducedMotion() || !('IntersectionObserver' in window)) { show(); return }
    const io = new IntersectionObserver((entries) => {
      if (!entries.some((e) => e.isIntersecting)) return
      show()
      io.disconnect()
    }, { threshold: 0.3 })
    io.observe(this.querySelector('.source-words'))
  }
}
customElements.define('source-section', SourceSection)
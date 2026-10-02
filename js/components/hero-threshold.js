import { initDust } from '../lib/dust.js?v=2'
import { buildSacredGeometry } from './sacred-geometry.js?v=2'
import { COPY } from '../data/copy.js?v=2'

/**
 * The first threshold. Curiosity before information: one word, one line,
 * two ways deeper. The artifact breathes behind it; dust drifts around it.
 */
export class HeroThreshold extends HTMLElement{
  connectedCallback() {
    if (this._wired) return
    this._wired = true

    buildSacredGeometry(this.querySelector('[data-sacred-geometry]'))
    const dust = initDust(this.querySelector('.hero-dust'))

    if (!window.matchMedia('(pointer: coarse)').matches) {
      let fx = 0, fy = 0, queued = null
      const rect = () => this.getBoundingClientRect()
      this.addEventListener('pointermove', (e) => {
        const r = rect()
        fx = ((e.clientX - r.left) / r.width - 0.5) * 2
        fy = ((e.clientY - r.top) / r.height - 0.5) * 2
        dust.setPointer(e.clientX - r.left, e.clientY - r.top)
        if (!queued) queued = requestAnimationFrame(() => {
          queued = null
          this.style.setProperty('--px', fx.toFixed(3))
          this.style.setProperty('--py', fy.toFixed(3))
        })
      }, { passive: true })
      this.addEventListener('pointerleave', () => {
        dust.clearPointer()
        this.style.removeProperty('--px')
        this.style.removeProperty('--py')
      })
    }

    const whisper = this.querySelector('.hero-whisper')
    this.addEventListener('ascended:core', () => {
      if (whisper.textContent) return
      whisper.textContent = COPY.whisper
      whisper.classList.add('is-said')
    })
  }
}
customElements.define('hero-threshold', HeroThreshold)
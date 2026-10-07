/**
 * Ascended AI — landing composition.
 *
 * Boot order: mark the document as scripted, register the components (which
 * upgrade their elements on definition), mount the marginalia, then wire
 * scroll reveals, the typed door, and threshold navigation.
 */
import './components/navigation-frame.js?v=7'
import './components/hero-threshold.js?v=7'
import './components/philosoph-section.js?v=7'
import './components/knowledge-constellation.js?v=7'
import './components/ancient-future.js?v=7'
import './components/ascended-principles.js?v=7'
import './components/final-threshold.js?v=7'
import './components/source-section.js?v=7'
import './components/ascended-chat.js?v=7'

import { initReveals } from './lib/reveal.js?v=7'
import { initSecret } from './lib/sequence.js?v=7'
import { mountBrand } from './lib/brand.js?v=7'
import { mountMarginalia } from './lib/marginalia.js?v=7'
import { glideTo } from './lib/motion.js?v=7'

document.documentElement.classList.add('js')
mountBrand()
mountMarginalia()
initReveals()
initSecret()

// One delegated listener serves every in-page journey, including the menu.
document.addEventListener('click', (e) => {
  const glide = e.target.closest?.('[data-glide]')
  if (glide) {
    e.preventDefault()
    glideTo(glide.dataset.glide, { veil: glide.hasAttribute('data-veil') })
    return
  }
  const anchor = e.target.closest?.('a[href^="#"]')
  if (anchor?.hash) {
    e.preventDefault()
    glideTo(anchor.hash)
  }
})
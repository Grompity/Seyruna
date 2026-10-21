import { prefersReducedMotion } from './motion.js?v=8'

/**
 * Kinetic type for the one heading per page that is allowed to ride letter
 * by letter (data-kinetic marks it; the hero holds it). Graphemes are split
 * into spans and --d is stamped per RING from the centre — the word blooms
 * outward and the centre grapheme lands as the mark's beat (--kinetic-beat)
 * rolls off. The ring step rides --stagger-kinetic: the readable ceiling is
 * per step, so a title card may land, but a reader may never wait for words.
 * Motion is CSS's (hero.css, kinetic-land); this file only builds the DOM
 * the stylesheet needs. Reduced motion: nothing is split. No JS: plain text.
 */
export function initKinetic() {
  if (!window.matchMedia?.('(prefers-reduced-motion: no-preference)').matches) return
  const host = document.querySelector('[data-kinetic]')
  if (!host) return
  const text = host.textContent
  if (!text) return

  let graphemes
  try {
    const seg = new Intl.Segmenter(undefined, { granularity: 'grapheme' })
    graphemes = [...seg.segment(text)].map((s) => s.segment)
  } catch {
    graphemes = [...text]
  }

  const stepMs = Number(getComputedStyle(host).getPropertyValue('--stagger-kinetic').replace('ms', '').trim()) || 40
  const centre = (graphemes.length - 1) / 2
  host.textContent = ''
  for (let i = 0; i < graphemes.length; i += 1) {
    const span = document.createElement('span')
    span.textContent = graphemes[i]
    span.style.setProperty('--d', `${Math.round(Math.abs(i - centre) * stepMs)}ms`)
    host.append(span)
  }
}

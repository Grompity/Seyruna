import { geometry } from '../data/geometry.js?v=7'
import { prefersReducedMotion } from '../lib/motion.js?v=7'

const SVGNS = 'http://www.w3.org/2000/svg'
const C = 500 // view-box center
const F = 1000 // view-box size

function el(tag, attrs = {}) {
  const node = document.createElementNS(SVGNS, tag)
  for (const [k, v] of Object.entries(attrs)) if (v !== undefined) node.setAttribute(k, String(v))
  return node
}

/**
 * The living artifact: structural rings, a manuscript tick-ring, a vesica of
 * two intersecting circles, points on slow orbits, and one point of light at
 * the center. The light answers a click — quietly, once per visit.
 *
 * Everything is generated from `js/data/geometry.js`; nothing is hard-coded here.
 */
export function buildSacredGeometry(host, cfg = geometry) {
  if (!host || host.childElementCount) return
  const animate = !prefersReducedMotion()

  const svg = el('svg', { viewBox: `0 0 ${F} ${F}`, class: 'sg' })
  const defs = el('defs')
  const grad = el('radialGradient', { id: 'sg-core' })
  const s1 = el('stop', { offset: '0' });      s1.style.cssText = 'stop-color:#f4ead0; stop-opacity:.92'
  const s2 = el('stop', { offset: '.18' });    s2.style.cssText = 'stop-color:hsl(41 46% 57%); stop-opacity:.45'
  const s3 = el('stop', { offset: '1' });      s3.style.cssText = 'stop-color:hsl(41 46% 57%); stop-opacity:0'
  grad.append(s1, s2, s3)
  const blur = el('filter', { id: 'sg-soft', x: '-80%', y: '-80%', width: '260%', height: '260%' })
  blur.append(el('feGaussianBlur', { stdDeviation: 5 }))
  defs.append(grad, blur)
  svg.append(defs)

  const breath = el('g', { class: 'sg-breath' })
  breath.style.setProperty('--sg-breath-scale', cfg.breath.scale)
  breath.style.setProperty('--sg-breath', `${cfg.breath.seconds}s`)
  svg.append(breath)

  const spin = (group, seconds, startDeg = 0) => {
    if (animate && seconds) {
      const dir = seconds < 0 ? -1 : 1
      const anim = el('animateTransform', {
        attributeName: 'Transform', attributeType: 'XML', type: 'rotate',
        from: `${startDeg} ${C} ${C}`, to: `${startDeg + 360 * dir} ${C} ${C}`,
        dur: `${Math.abs(seconds)}s`, repeatCount: 'indefinite',
      })
      group.append(anim)
    } else if (startDeg) {
      group.setAttribute('Transform', `rotate(${startDeg} ${C} ${C})`)
    }
  }

  // — Structural rings ------------------------------------------------------
  const ringsGroup = el('g', { class: 'sg-par sg-par--slow' })
  breath.append(ringsGroup)
  for (const ring of cfg.rings) {
    const g = el('g')
    const circle = el('circle', {
      cx: C, cy: C, r: ring.radius * F,
      class: 'sg-ring',
      'stroke-dasharray': ring.dash ? ring.dash.join(' ') : undefined,
    })
    circle.style.opacity = ring.opacity
    g.append(circle)
    ringsGroup.append(g)
    if (ring.spinSeconds) spin(g, ring.spinSeconds)
  }

  // — Tick ring (astronomical instrument, manuscript hand) --------------------
  const ticks = el('g', { class: 'sg-par sg-par--slow' })
  const tickSpin = el('g')
  const inner = cfg.ticks.inner * F, outer = cfg.ticks.outer * F
  for (let i = 0; i < cfg.ticks.count; i++) {
    const long = i % (cfg.ticks.count / 4) === 0
    const tick = el('line', {
      x1: C, y1: C - (long ? outer + 7 : outer), x2: C, y2: C - inner,
      class: 'sg-tick',
    })
    tick.setAttribute('Transform', `rotate(${(i * 360) / cfg.ticks.count} ${C} ${C})`)
    tick.style.opacity = cfg.ticks.opacity * (long ? 1.6 : 1)
    tickSpin.append(tick)
  }
  ticks.append(tickSpin)
  breath.append(ticks)
  spin(tickSpin, cfg.ticks.spinSeconds)

  // — The vesica: two circles that meet --------------------------------------
  const vesica = el('g', { class: 'sg-par sg-par--mid' })
  const vr = cfg.vesica.radius * F, vo = cfg.vesica.offset * F
  for (const dx of [-vo, vo]) {
    const c = el('circle', { cx: C + dx, cy: C, r: vr, class: 'sg-vesica' })
    c.style.opacity = cfg.vesica.opacity
    vesica.append(c)
  }
  breath.append(vesica)

  // — Orbiting points ---------------------------------------------------------
  for (const orbit of cfg.orbits) {
    const par = el('g', { class: 'sg-par sg-par--slow' })
    const rot = el('g')
    const dot = el('circle', {
      cx: C, cy: C - orbit.radius * F, r: orbit.dot * F,
      class: 'sg-dot', filter: orbit.glow ? 'url(#sg-soft)' : undefined,
    })
    rot.append(dot)
    spin(rot, orbit.reverse ? -orbit.periodSeconds : orbit.periodSeconds, orbit.startDeg)
    par.append(rot)
    breath.append(par)
  }

  // — The point of light (interactive) ---------------------------------------
  const core = el('g', { class: 'sg-par sg-par--core' })
  core.append(
    el('circle', { cx: C, cy: C, r: cfg.core.halo * F, fill: 'url(#sg-core)', class: 'sg-halo' }),
    el('circle', { cx: C, cy: C, r: cfg.core.radius * F, class: 'sg-core' }),
    el('circle', { cx: C, cy: C, r: cfg.core.touch * F, class: 'sg-touch' }),
  )
  breath.append(core)

  host.append(svg)

  const pulse = () => {
    core.classList.add('is-touched')
    host.dispatchEvent(new CustomEvent('ascended:core', { bubbles: true }))
  }
  core.addEventListener('pointerdown', (e) => { e.preventDefault(); pulse() })
  core.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') pulse() })

  return svg
}
import { prefersReducedMotion } from './motion.js?v=2'

/**
 * Dust — a few dozen motes adrift in the hero, stirred by the pointer.
 * Nothing bounces; everything drifts. Pauses when the tab is hidden.
 */
export function initDust(canvas, { max = 56, area = 30000, push = 96 } = {}) {
  const ctx = canvas.getContext('2d')
  if (!ctx) return { stop() {} }

  let w = 0, h = 0, dpr = 1
  let motes = []
  const pointer = { x: -1e4, y: -1e4 }
  let raf = null
  let running = false

  const resize = () => {
    dpr = Math.min(window.devicePixelRatio || 1, 1.75)
    w = canvas.clientWidth
    h = canvas.clientHeight
    canvas.width = Math.round(w * dpr)
    canvas.height = Math.round(h * dpr)
    const count = Math.max(24, Math.min(max, Math.round((w * h) / area)))
    let seed = 21
    const rand = () => (seed = (seed * 16807 + 11) % 2147483647) / 2147483647
    motes = Array.from({ length: count }, () => ({
      x: rand() * w,
      y: rand() * h,
      r: 0.5 + rand() * 1.3,
      a: 0.05 + rand() * 0.16,
      tw: 0.25 + rand() * 0.7,
      ph: rand() * Math.PI * 2,
      vy: -(0.008 + rand() * 0.03),
      dx: rand() * 2 - 1,
    }))
  }

  const paint = (t) => {
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0)
    ctx.clearRect(0, 0, w, h)
    ctx.fillStyle = '#e9e1cf'
    for (const m of motes) {
      if (t !== null) {
        // Drift.
        m.y += m.vy
        m.x += Math.sin(t * 0.00018 + m.ph) * 0.05
        if (m.y < -8) m.y = h + 8
        if (m.y > h + 8) m.y = -8
        // The pointer breathes the dust aside, very gently.
        const dx = m.x - pointer.x
        const dy = m.y - pointer.y
        const d2 = dx * dx + dy * dy
        if (d2 < push * push && d2 > 1) {
          const d = Math.sqrt(d2)
          const f = ((1 - d / push) ** 2) * 0.55
          m.x += (dx / d) * f
          m.y += (dy / d) * f
        }
      }
      const alpha = t === null
        ? m.a * 0.6
        : Math.max(0, m.a + Math.sin(t * 0.0006 * m.tw + m.ph) * 0.07)
      ctx.globalAlpha = alpha
      ctx.beginPath()
      ctx.arc(m.x, m.y, m.r, 0, Math.PI * 2)
      ctx.fill()
    }
    ctx.globalAlpha = 1
  }

  const frame = (t) => {
    if (!running) return
    paint(t)
    raf = requestAnimationFrame(frame)
  }

  const start = () => {
    if (running || prefersReducedMotion()) return
    running = true
    raf = requestAnimationFrame(frame)
  }
  const stop = () => {
    running = false
    if (raf) cancelAnimationFrame(raf)
  }

  resize()
  window.addEventListener('resize', resize, { passive: true })
  document.addEventListener('visibilitychange', () => (document.hidden ? stop() : start()))
  prefersReducedMotion() ? paint(null) : start()
  return {
    setPointer(x, y) { pointer.x = x; pointer.y = y },
    clearPointer() { pointer.x = -1e4; pointer.y = -1e4 },
    stop,
    start,
  }
}
const S = 'stroke="currentColor" fill="none" stroke-width="1"'

/** An Archimedean spiral path, generated rather than traced. */
export function spiralPath(cx, cy, turns = 3.5, reach = 60, steps = 220) {
  let d = `M ${cx} ${cy}`
  for (let i = 1; i <= steps; i++) {
    const t = (i / steps) * turns * Math.PI * 2
    const r = (i / steps) * reach
    d += ` L ${(cx + Math.cos(t) * r).toFixed(2)} ${(cy + Math.sin(t) * r).toFixed(2)}`
  }
  return d
}

/**
 * Small geometric marks. Drawn from pure geometry only — no tradition's symbol
 * is copied, and no meaning is asserted.
 */
export function glyphSVG(kind) {
  switch (kind) {
    case 'vesica':
      return `<svg viewBox="0 0 34 22" width="26" aria-hidden="true">
        <circle ${S} cx="13" cy="11" r="8.5"/><circle ${S} cx="21" cy="11" r="8.5"/></svg>`
    case 'ouroboros':
      // A line returning on itself: the cycle drawn abstractly, not as a creature.
      return `<svg viewBox="0 0 24 24" width="22" aria-hidden="true">
        <circle ${S} cx="12" cy="12" r="8.5" stroke-dasharray="34 4"/>
        <path ${S} d="M 9.6 4.4 L 12.6 3.4 L 11.8 6.6"/></svg>`
    case 'spiral':
      return `<svg viewBox="0 0 26 26" width="22" aria-hidden="true">
        <path ${S} d="${spiralPath(13, 13, 2.6, 9.5, 90)}" stroke-width=".9"/></svg>`
    case 'circle-dot':
    default:
      return `<svg viewBox="0 0 22 22" width="20" aria-hidden="true">
        <circle ${S} cx="11" cy="11" r="8.5"/><circle cx="11" cy="11" r="1.1" fill="currentColor"/></svg>`
  }
}
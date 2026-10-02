/**
 * SacredGeometry configuration.
 * All radii are fractions of the artifact's diameter, so the object recomposes
 * at any size. Tweak freely — the renderer draws only from this object.
 */
export const geometry = {
  breath: { scale: 1.014, seconds: 12 },

  // The point of light. It is the only interactive part of the artifact.
  core: { radius: 0.013, halo: 0.085, touch: 0.05, seconds: 9 },

  // Two intersecting circles — the recurring site mark. Used as a shape meaning
  // "where two things meet"; it is deliberately not explained.
  vesica: { radius: 0.42, offset: 0.175, opacity: 0.32 },

  // Manuscript-style tick ring.
  ticks: { count: 48, inner: 0.478, outer: 0.5, opacity: 0.5, spinSeconds: 420 },

  // Structural rings. dash: [on, off] in svg units, or null for a continuous line.
  rings: [
    { radius: 0.478, dash: null,      opacity: 0.55, spinSeconds: 0 },
    { radius: 0.40,  dash: [1.5, 10], opacity: 0.34, spinSeconds: 300 },
    { radius: 0.30,  dash: null,      opacity: 0.50, spinSeconds: -420 },
    { radius: 0.185, dash: [0.6, 4],  opacity: 0.60, spinSeconds: 180 },
  ],

  // Orbiting points, each turning at its own pace.
  orbits: [
    { radius: 0.34,  dot: 0.0072, periodSeconds: 76,  startDeg: 0,   glow: true },
    { radius: 0.435, dot: 0.0050, periodSeconds: 118, startDeg: 140, glow: false, reverse: true },
    { radius: 0.235, dot: 0.0046, periodSeconds: 52,  startDeg: 255, glow: false },
  ],
}
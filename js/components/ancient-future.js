import { spiralPath } from './glyphs.js?v=7'

/**
 * Two visual languages, one seam. The left is drawn by a hand (generated
 * spirals, dashed arcs, a scribe's rules); the right is drawn by the machine
 * (grids, exact circles, a sweeping line). They meet as a half-drawn circle.
 */
export class AncientFuture extends HTMLElement{
  connectedCallback() {
    if (this._wired) return
    this._wired = true
    const C = 300

    const manuscript = this.querySelector('.af-manuscript')
    if (manuscript) {
      const ticks = Array.from({ length: 72 }, (_, i) => {
        const long = i % 12 === 0
        return `<line class="af-tick" x1="${C}" y1="${C - 258}" x2="${C}" y2="${C - (long ? 272 : 266)}"
          Transform="rotate(${i * 5} ${C} ${C})"/>`
      }).join('')
      manuscript.innerHTML = `
        <g class="af-ink">
          <circle class="af-dash" cx="${C}" cy="${C}" r="240"/>
          <circle class="af-dash-soft" cx="${C}" cy="${C}" r="158"/>
          <path class="af-spiral" d="${spiralPath(C, C, 3.4, 128, 260)}"/>
          ${ticks}
          <line class="af-rule" x1="30" y1="${C}" x2="${2 * C - 30}" y2="${C}"/>
          <line class="af-rule" x1="${C}" y1="30" x2="${C}" y2="${2 * C - 30}"/>
          <circle class="af-dot" cx="${C + 170}" cy="${C - 170}" r="2.4"/>
          <text class="af-hand" x="430" y="528">fig. i</text>
        </g>`
    }

    const machine = this.querySelector('.af-machine')
    if (machine) {
      const gridLines = []
      for (let v = 60; v <= 540; v += 60) {
        gridLines.push(`<line x1="${v}" y1="60" x2="${v}" y2="540"/>`)
        gridLines.push(`<line x1="60" y1="${v}" x2="540" y2="${v}"/>`)
      }
      machine.innerHTML = `
        <g class="af-grid">${gridLines.join('')}</g>
        <g class="af-ink">
          <circle class="af-solid" cx="${C}" cy="${C}" r="186"/>
          <circle class="af-solid-soft" cx="${C}" cy="${C}" r="120"/>
          <circle class="af-node" cx="${C + 131}" cy="${C - 131}" r="3.2"/>
          <line class="af-sweep" x1="${C}" y1="${C}" x2="${C}" y2="${C - 186}"/>
          <path class="af-trace" d="M ${C - 186} ${C} A 186 186 0 0 1 ${C} ${C - 186}"/>
        </g>`
    }
  }
}
customElements.define('ancient-future', AncientFuture)
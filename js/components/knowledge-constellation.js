import { NODES, LINKS, STAGE, dustField } from '../data/constellation.js?v=7'

const neighborsOf = Object.fromEntries(
  NODES.map((n) => [n.id, new Set()]),
)
for (const [a, b] of LINKS) {
  neighborsOf[a].add(b)
  neighborsOf[b].add(a)
}
const byId = Object.fromEntries(NODES.map((n) => [n.id, n]))

// Five domains keep a label at rest; the rest ride as dots until touched.
// The map supports the concept; it never has to explain it.
const NAMED = new Set(['consciousness', 'philosophy', 'science', 'meditation', 'ai'])
/**
 * The Knowledge Constellation — a domain map that behaves like a star field,
 * not a graph. Touching a node lights its neighbours; the rest of the field
 * dims. Selecting one leaves a sentence below the map.
 */
export class KnowledgeConstellation extends HTMLElement{
  connectedCallback() {
    if (this._wired) return
    this._wired = true

    const stage = this.querySelector('.kc-stage')
    const wiresBox = this.querySelector('[data-kc-links]')
    const list = this.querySelector('[data-kc-nodes]')
    const info = this.querySelector('.kc-info')

    // Faint field + thin wires.
    const stars = dustField()
      .map((s) => `<circle cx="${s.x.toFixed(1)}" cy="${s.y.toFixed(1)}" r="${s.r.toFixed(2)}" fill="#e9e1cf" opacity="${s.a.toFixed(3)}"/>`)
      .join('')
    const wires = LINKS.map(([a, b]) => {
      const A = byId[a], B = byId[b]
      return `<line data-a="${a}" data-b="${b}" x1="${A.x}" y1="${A.y}" x2="${B.x}" y2="${B.y}"/>`
    }).join('')
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg')
    svg.setAttribute('ViewBox', `0 0 ${STAGE.width} ${STAGE.height}`)
    svg.setAttribute('class', 'kc-svg')
    svg.innerHTML = `<g class="kc-stars">${stars}</g><g class="kc-wires">${wires}</g>`
    wiresBox.append(svg)
    const wireEls = [...svg.querySelectorAll('line')]

    // Nodes are real buttons — keyboard-reachable, legible without JS.
    let selected = null

    const highlight = (id, pinned) => {
      const active = Boolean(id)
      stage.classList.toggle('is-active', active)
      const near = active ? neighborsOf[id] : null
      for (const line of wireEls)
        line.classList.toggle('is-on', active && (line.dataset.a === id || line.dataset.b === id))
      for (const li of list.children) {
        const btn = li.firstchild
        const on = btn.dataset.node === id
        btn.classList.toggle('is-on', on)
        btn.classList.toggle('is-near', Boolean(near?.has(btn.dataset.node)))
        btn.setAttribute('aria-pressed', String(btn.dataset.node === selected))
      }
      if (!info) return
      if (active) {
        const n = byId[id]
        info.innerHTML = `<span class="kc-info-label">${n.label}</span>${n.note}`
        info.classList.add('is-said')
      } else if (!pinned && !selected) {
        info.classList.remove('is-said')
        info.textContent = ''
      }
    }

    for (const [i, node] of NODES.entries()) {
      const li = document.createElement('li')
      const btn = document.createElement('button')
      btn.className = 'kc-node'
      btn.type = 'button'
      btn.textContent = node.label
      btn.dataset.node = node.id
      btn.classList.toggle('kc-quiet', !NAMED.has(node.id))
      li.style.setProperty('--x', `${((node.x / STAGE.width) * 100).toFixed(2)}%`)
      li.style.setProperty('--y', `${((node.y / STAGE.height) * 100).toFixed(2)}%`)
      li.style.setProperty('--d', `${120 + i * 55}ms`)
      li.dataset.reveal = ''
      li.append(btn)

      const preview = () => highlight(node.id, false)
      const revert = () => highlight(selected, true)
      const commit = () => {
        selected = selected === node.id ? null : node.id
        highlight(selected ?? node.id, true)
      }
      btn.addEventListener('pointerenter', preview)
      btn.addEventListener('focus', preview)
      btn.addEventListener('pointerleave', revert)
      btn.addEventListener('blur', revert)
      btn.addEventListener('click', commit)
      list.append(li)
    }
  }
}
customElements.define('knowledge-constellation', KnowledgeConstellation)
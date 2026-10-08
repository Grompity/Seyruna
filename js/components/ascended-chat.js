/**
 * VI · Encounter — where the landing page meets the machine.
 *
 * The brain behind this element is the whole MVP: the door's /ask runs
 * stages.run_pipeline(question, facts, live=True) and the speech arrives
 * verbatim. The element adds a conversation shell and nothing else:
 * the turns live here (and in sessionStorage, which IS the session), and
 * each next turn carries a bounded, deterministic digest of the recent
 * exchanges as FACTS — the channel the architecture already grew for
 * "what the seeker already said". Conversation is context, not evidence:
 * the shelf, the ladder, and the guards decide what may be said.
 * One turn, one door-call; no model is spent on memory.
 */
import { SITE } from '../data/site.js?v=7'

const STORE = 'ascended-chat-v1'
const MAX_TURNS = 1 // the ONE prior exchange carried - the window, not a store
const CAP_MSG = 160 // characters per carried message (the deterministic cut)

const cut = (s) => (s.length > CAP_MSG ? s.slice(0, CAP_MSG) + '…' : s)
const debugOn = new URLSearchParams(location.search).has('debug')

export class AscendedChat extends HTMLElement {
  connectedCallback() {
    if (this._wired) return
    this._wired = true
    this.log = this.querySelector('.chat-log')
    this.form = this.querySelector('.chat-form')
    this.inbox = this.querySelector('.chat-in')
    this.status = this.querySelector('.chat-status')
    this.send = this.querySelector('.chat-send')
    this.turns = this.restore()
    this.replay()
    this.form.addEventListener('submit', (e) => { e.preventDefault(); this.submitTurn() })
    this.inbox.addEventListener('keydown', (e) => {
      // Enter sends; Shift+Enter breathes (the native newline).
      if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); this.submitTurn() }
    })
    this.querySelector('.chat-reset').addEventListener('click', () => {
      this.turns = []
      try { sessionStorage.removeItem(STORE) } catch { /* private mode: memory is enough */ }
      this.replay()
    })
    // the box breathes with what is written into it
    this.inbox.addEventListener('input', () => {
      this.inbox.style.height = 'auto'
      this.inbox.style.height = Math.min(this.inbox.scrollHeight, 150) + 'px'
    })
  }

  // The bounded, deterministic digest of what came before. Empty on the
  // first turn — so the first turn is byte-identical to a one-question ask.
  facts() {
    const recent = this.turns.slice(-MAX_TURNS)
    if (!recent.length) return ''
    return 'Earlier - ' + recent.map(t =>
      "you asked '" + cut(t.q) + "', Ascended said '" + cut(t.a) + "'").join(' then ') + '.'
  }

  async submitTurn() {
    if (this.busy) return
    const q = this.inbox.value.trim()
    if (!q) return
    this.busy = true
    this.send.disabled = true
    this.lastQ = q
    this.log.querySelector('.chat-empty')?.remove()
    this.inbox.value = ''
    this.inbox.style.height = 'auto'
    this.say('user', q)
    this.status.textContent = SITE.project + ' ' + SITE.status.working
    let d
    const t0 = Date.now()
    try {
      const r = await fetch('/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: q, facts: this.facts() }),
      })
      d = await r.json()
      if (d.error) throw new Error(d.error)
    } catch (err) {
      this.status.textContent = ''
      this.sayErr(SITE.project + ' ' + SITE.status.failed + ': ' + (err?.message || err))
      this.busy = false
      this.send.disabled = false
      return
    }
    const t = { q, a: d.response || '', ms: Date.now() - t0, why: d.why, trace: d.trace }
    this.turns.push(t)
    try { sessionStorage.setItem(STORE, JSON.stringify(this.turns)) } catch { /* ditto */ }
    this.say('asc', t.a, t)
    this.status.textContent = ''
    this.busy = false
    this.send.disabled = false
    this.inbox.focus?.()
  }

  replay() {
    this.log.textContent = ''
    if (!this.turns.length) {
      const p = document.createElement('p')
      p.className = 'chat-empty'
      p.textContent = 'The conversation begins with your question.'
      this.log.append(p)
      return
    }
    for (const t of this.turns) { this.say('user', t.q); this.say('asc', t.a, t) }
  }

  say(who, text, t) {
    const box = document.createElement('div')
    box.className = 'msg msg--' + (who === 'user' ? 'user' : 'asc')
    const lab = document.createElement('span')
    lab.className = 'msg__who'
    lab.textContent = who === 'user' ? 'You' : SITE.project
    const body = document.createElement('p')
    body.className = 'msg__text'
    body.textContent = text // verbatim, always; never markup
    box.append(lab, body)
    if (t?.ms) {
      const ms = document.createElement('span')
      ms.className = 'msg__ms'
      ms.textContent = t.ms + ' ms'
      box.append(ms)
    }
    if (debugOn && t?.why) {
      const det = document.createElement('details')
      det.className = 'chat-fold'
      const sum = document.createElement('summary')
      sum.textContent = 'why it said so'
      const pre = document.createElement('pre')
      pre.textContent = JSON.stringify(t.why, null, 1) + '\n\n'
        + 'trace · ' + JSON.stringify(t.trace?.retrieval ?? []) + ' · '
        + JSON.stringify(t.trace?.fires ?? [])
      det.append(sum, pre)
      box.append(det)
    }
    this.log.append(box)
    this.log.scrollTop = this.log.scrollHeight
    return box
  }

  sayErr(text) {
    const box = document.createElement('div')
    box.className = 'msg msg--err'
    const body = document.createElement('p')
    body.className = 'msg__text'
    body.textContent = text
    const retry = document.createElement('button')
    retry.type = 'button'
    retry.className = 'btn chat-retry'
    retry.textContent = 'again'
    retry.addEventListener('click', () => {
      box.remove()
      this.inbox.value = this.lastQ || ''
      this.submitTurn()
    })
    box.append(body, retry)
    this.log.append(box)
    this.log.scrollTop = this.log.scrollHeight
  }

  restore() {
    try { return JSON.parse(sessionStorage.getItem(STORE) || '[]') } catch { return [] }
  }
}
customElements.define('ascended-chat', AscendedChat)

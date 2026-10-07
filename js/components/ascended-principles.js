/** Staggers the two principle statements in sequence; the markup lives in index.html. */
export class AscendedPrinciples extends HTMLElement{
  connectedCallback() {
    if (this._wired) return
    this._wired = true
    const list = this.querySelector('.principles-list')
    if (!list) return
    ;[...list.children].forEach((li, i) => {
      li.style.setProperty('--d', `${140 + i * 170}ms`)
    })
  }
}
customElements.define('ascended-principles', AscendedPrinciples)

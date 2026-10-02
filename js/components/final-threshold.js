/**
 * The last threshold. Its mark is the same pair of intersecting circles the
 * favicon and the hero are built from — the site ends where it began.
 */
export class FinalThreshold extends HTMLElement{
  connectedCallback() {
    if (this._wired) return
    this._wired = true
    const mark = this.querySelector('.final-mark')
    if (mark && window.matchMedia('(hover: hover)').matches) {
      mark.addEventListener('pointerenter', () => mark.classList.add('is-near'), { once: true })
    }
  }
}
customElements.define('final-threshold', FinalThreshold)
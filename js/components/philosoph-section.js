/** Staggers the creed lines; the markup itself lives in index.html. */
export class PhilosophSection extends HTMLElement{
  connectedCallback() {
    if (this._wired) return
    this._wired = true
    const creed = this.querySelector('.philo-creed')
    if (!creed) return
    ;[...creed.children].forEach((li, i) => {
      li.style.setProperty('--d', `${140 + i * 130}ms`)
    })
  }
}
customElements.define('insight-section', PhilosophSection)
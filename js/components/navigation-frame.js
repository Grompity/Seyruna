/**
 * Navigation is nearly absent until the visitor wakes it, and returns to rest
 * a few seconds later. On touch it lives behind a quiet Menu.
 */
export class NavigationFrame extends HTMLElement{
  connectedCallback() {
    if (this._wired) return
    this._wired = true
    const IDLE = 5200
    let idle = null

    const wake = () => {
      this.classList.add('is-awake')
      clearTimeout(idle)
      idle = setTimeout(() => this.classList.remove('is-awake'), IDLE)
    }
    for (const evt of ['pointermove', 'keydown', 'wheel', 'scroll'])
      window.addEventListener(evt, wake, { passive: true })
    wake()

    const overlay = document.getElementById('nav-menu')
    const button = this.querySelector('.nav-menu-btn')
    const close = overlay.querySelector('.nav-menu__close')
    const setOpen = (on) => {
      overlay.hidden = !on
      button.setAttribute('aria-expanded', String(on))
      document.body.classList.toggle('menu-open', on)
      ;(on ? close : button).focus({ preventScroll: true })
    }
    button.addEventListener('click', () => setOpen(overlay.hidden))
    close.addEventListener('click', () => setOpen(false))
    overlay.addEventListener('click', (e) => {
      if (e.target.closest('a') || e.target === overlay) setOpen(false)
    })
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && !overlay.hidden) setOpen(false)
    })
  }
}
customElements.define('navigation-frame', NavigationFrame)
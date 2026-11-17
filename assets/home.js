'use strict';

const toggle = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
function closeMenu() {
  toggle.setAttribute('aria-expanded', 'false');
  navigation.classList.remove('open');
}
toggle.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') !== 'true';
  toggle.setAttribute('aria-expanded', String(open));
  navigation.classList.toggle('open', open);
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
    closeMenu();
    toggle.focus();
  }
});
navigation.addEventListener('click', event => {
  if (event.target.closest('a')) closeMenu();
});
document.querySelectorAll('[data-language]').forEach(link => {
  link.addEventListener('click', () => {
    try { localStorage.setItem('mates-language', link.dataset.language); }
    catch { /* Direct language links also work without storage. */ }
  });
});

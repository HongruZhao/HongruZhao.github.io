(() => {
  const appearance = window.hzAppearance;
  const modes = document.querySelectorAll('button[data-mode]');
  function markMode() { modes.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.mode === appearance.mode))); }
  modes.forEach(b => b.addEventListener('click', () => { appearance.setMode(b.dataset.mode); markMode(); }));
  markMode();
  const selector = document.getElementById('background-select');
  selector.value = appearance.background;
  selector.addEventListener('change', () => appearance.setBackground(selector.value));
  const menus = [...document.querySelectorAll('.nav-dropdown')];
  menus.forEach(menu => menu.addEventListener('toggle', () => { if (menu.open) menus.forEach(other => { if (other !== menu) other.open = false; }); }));
  document.addEventListener('click', event => menus.forEach(menu => { if (!menu.contains(event.target)) menu.open = false; }));
  document.addEventListener('keydown', event => { if (event.key === 'Escape') menus.forEach(menu => { if (menu.open) { menu.open = false; menu.querySelector('summary').focus(); } }); });
  document.addEventListener('focusin', event => menus.forEach(menu => { if (!menu.contains(event.target)) menu.open = false; }));
  document.querySelectorAll('.mobile-menu a').forEach(link => link.addEventListener('click', () => { link.closest('details').open = false; }));
  window.matchMedia('(max-width: 54rem)').addEventListener('change', () => menus.forEach(menu => { menu.open = false; }));

  const areaNavigation = document.querySelector('.research-areas');
  if (areaNavigation) {
    const tabs = [...areaNavigation.querySelectorAll('[data-research-area]')];
    const panels = tabs.map(tab => document.getElementById(tab.dataset.researchArea));
    areaNavigation.setAttribute('role', 'tablist');
    tabs.forEach((tab, index) => {
      tab.setAttribute('role', 'tab');
      tab.setAttribute('aria-controls', panels[index].id);
      panels[index].setAttribute('role', 'tabpanel');
      panels[index].tabIndex = 0;
    });

    function selectArea(index) {
      tabs.forEach((tab, i) => {
        tab.setAttribute('aria-selected', String(i === index));
        tab.tabIndex = i === index ? 0 : -1;
        panels[i].hidden = i !== index;
      });
    }

    function syncArea() {
      let id;
      try { id = decodeURIComponent(location.hash.slice(1)); }
      catch { id = ''; }
      const target = document.getElementById(id);
      const index = panels.findIndex(panel => panel === target || panel.contains(target));
      selectArea(index < 0 ? 0 : index);
      // Existing topic links must reveal their area before scrolling to the topic.
      if (target && index >= 0 && target !== panels[index]) {
        requestAnimationFrame(() => target.scrollIntoView());
      }
    }

    function activateArea(index) {
      selectArea(index);
      const hash = '#' + panels[index].id;
      if (location.hash !== hash) history.pushState(null, '', hash);
    }

    tabs.forEach((tab, index) => {
      tab.addEventListener('click', event => {
        if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
        event.preventDefault();
        activateArea(index);
      });
      tab.addEventListener('keydown', event => {
        let next = index;
        if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
        else if (event.key === 'ArrowLeft') next = (index + tabs.length - 1) % tabs.length;
        else if (event.key === 'Home') next = 0;
        else if (event.key === 'End') next = tabs.length - 1;
        else if (event.key !== ' ') return;
        event.preventDefault();
        tabs[next].focus();
        activateArea(next);
      });
    });
    window.addEventListener('hashchange', syncArea);
    window.addEventListener('popstate', syncArea);
    syncArea();
  }
})();

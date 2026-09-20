(() => {
  const root = document.documentElement;
  let mode = 'system', background = root.dataset.background || 'mist';
  try { mode = localStorage.getItem('hz-mode') || mode; background = localStorage.getItem('hz-background') || background; } catch {}
  const media = matchMedia('(prefers-color-scheme: dark)');
  const apply = () => { root.dataset.mode = mode === 'system' ? (media.matches ? 'dark' : 'light') : mode; root.dataset.background = background; };
  apply(); media.addEventListener('change', apply);
  window.hzAppearance = { get mode() { return mode; }, get background() { return background; }, setMode(value) { mode = value; try { localStorage.setItem('hz-mode', value); } catch {} apply(); }, setBackground(value) { background = value; try { localStorage.setItem('hz-background', value); } catch {} apply(); } };
})();

export function normalizeView(value) {
  return value === 'perspectives' ? 'perspectives' : 'synthesis';
}

export function initReadingView(doc, win) {
  const control = doc.querySelector('.view-toggle-container');
  if (!control || control.dataset.initialized) return;
  const buttons = control.querySelectorAll('button[data-view]');
  function updateView(value) {
    const view = normalizeView(value);
    doc.body.dataset.wintermuteView = view;
    buttons.forEach(button => {
      const selected = button.dataset.view === view;
      button.classList.toggle('active', selected);
      button.setAttribute('aria-pressed', String(selected));
    });
    try { win.localStorage.setItem('wintermute-view', view); } catch { /* best effort */ }
  }
  let savedView;
  try { savedView = win.localStorage.getItem('wintermute-view'); } catch { /* use default */ }
  buttons.forEach(button => button.addEventListener('click', () => updateView(button.dataset.view)));
  updateView(savedView);
  control.dataset.initialized = 'true';
  control.hidden = false;
}

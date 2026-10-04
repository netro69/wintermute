# Wintermute reading-view runbook

The four Architects debate; the passive Mediator synthesizes. The site displays stored articles, not a live debate engine.

- `src/layouts/BlogPost.astro` owns H1 and renders controls only for `readingViews: true`.
- MDX articles explicitly import `src/components/Perspective.astro` and wrap attributed blocks. New summaries use `persona="Mediator"`; historical Editorial Synthesizer remains compatible. Material has its own accent.
- `src/lib/reading-view.js` initializes once, normalizes saved state, manages `aria-pressed`, and treats storage as best effort.
- `src/styles/global.css` hides debater blocks with `display:none` in synthesis mode. Unwrapped summaries/takeaways/sources remain visible. Perspectives shows every block.
- Without JavaScript, all content remains readable and controls are hidden. Plain Markdown articles show no controls.
- Use `withBase()` for internal URLs; origin and `/wintermute` base are separate in Astro config. Do not reintroduce `/posts/` or `/_astro/` at the origin root.

Validate using `npm run check` and the optional browser test documented in `../TESTING.md`. Preserve historical content semantics when changing persona selectors; migrate labels and visibility together.

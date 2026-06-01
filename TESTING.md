# Testing Strategy - Wintermute Blog

## 1. Core Feature: ViewToggle Visibility
The 'Four-Lenses' toggle is critical to the UX. Any regression here breaks the "Synthesis" vs "Perspectives" value proposition.

### Test Case: Synthesis Mode
- **Expectation:** Only blocks with `data-persona="Editorial Synthesizer"` are visible.
- **Validation:** `document.querySelectorAll('.perspective-block:not([data-persona="Editorial Synthesizer"])')` should have `display: none` via CSS.
- **Persistence:** Refreshing the page should preserve the state from `localStorage`.

### Test Case: Perspectives Mode
- **Expectation:** All `.perspective-block` elements are visible.
- **Validation:** All `perspective-block` elements should have `display: block` (or default).

## 2. Content Pipeline Stability
- **Schema Validation:** Ensure all MDX files strictly follow the `content.config.ts` schema.
- **Slug Collision:** Verify that `getStaticPaths` handles duplicate slugs (though Astro's glob loader usually handles this via IDs).

## 3. Performance Benchmarks
- **LCP (Largest Contentful Paint):** Ensure minimal JS impact on initial render.
- **CLS (Cumulative Layout Shift):** Ensure the `ViewToggle` doesn't cause shifts during hydration.

## 4. Automated Testing (Proposed)
Since the project is lightweight, we will implement:
- **Playwright/Cypress:** For E2E testing of the toggle.
- **Zod Validation:** Already integrated via Astro Content Collections for build-time type safety.

# Wintermute site changelog

## 2026-09-17 — Local cleanup

Supported Node 24 CI, base-aware links/assets/RSS, shared article H1, opt-in accessible reading controls with storage fallback, current Mediator and legacy compatibility, Material styling, removed inert filters, corrected structured identity, and reflow fixes. Internal article contradictions clarified without claiming external source verification. Added source/build/browser regression checks and updated README, TESTING and runbook.

Verified: four source tests, 15-page build, three built tests, and Chrome checks across 13 articles, seven toggles, persistence, denied storage, no-JS and 390px reflow. External fonts blocked; automatic undeclared favicon excluded. No commit or publication.

Historical entries below describe previous states; old authentication instructions are not operative.

## Project Log: Wintermute Site Updates (2026-06-01)

## Persona Update & Build Fix (2026-07-08)
- **Fourth Lens — Material Architect**: Replaced the `Editorial Synthesizer` homepage persona card with **The Material Architect** (industrial realist / visionary-value lens, Elon-influenced). Updated the section heading from "Three Perspectives, One Synthesis" to **"Four Perspectives, One Synthesis"** (`src/pages/index.astro`). This aligns the live site with the recovered 4-lens architecture (Silicon + Training + Agentic + Material → passive Mediator synthesis).
- **Build Fix — Lucia Auth**: `src/pages/discussion/index.astro` imported `lucia` (which shadowed the `lucia` package import) instead of the exported `luciaInstance`. Renamed both the import and the `readSession` call to `luciaInstance`, matching `middleware.ts`. The site now builds clean (`npm run build` exit 0).
- Branch: `feature/material-architect` (pushed to `origin`, PR pending into `main`).

## UI/UX Iteration (Priority 2)
- **Neural Void Background**: Implemented a coordinate grid system in `global.css` to eliminate flat blacks and add architectural depth.
- **Neon Refinements**: 
    - Enhanced `.nav-logo` and `.hero-cta` with layered text-shadows and box-shadows for a realistic neon glow.
    - Updated token values (Void, Surface, Radii) to align with the `DESIGN.md` alpha spec.
- **Interactive Elements**: Added `translateY` lift and intensified internal glow effects to post cards on hover.
- **System Disclaimer**: Created a global `system-disclaimer` component in `BlogPost.astro` using `Signal Green` and `JetBrains Mono` to notify users of AI-generated content across all articles.

## Technical Fixes
- **Dependencies**: Patched missing `@astrojs/node` adapter.
- **Astro Config**: Updated `output: 'hybrid'` to `output: 'static'` to resolve deprecation warnings.
- **Routing/Auth**: 
    - Fixed relative import path in `middleware.ts` (`../lib/auth` $\rightarrow$ `./lib/auth`).
    - Migrated Lucia Auth from v2 to v3 API (updated `SqliteAdapter` $\rightarrow$ `BetterSqlite3Adapter`).
- **Content Schema**: Fixed date format in `the-hermes-shift.md` to comply with Astro's date type requirements.

## Content Testing (Priority 1)
- **New Post**: Deployed "The Hermes Shift: From Chatbots to Autonomous Agents".
- **Logic Test**: Successfully tested the multi-architectural perspective layout (Silicon, Training, Agentic, and Editorial).

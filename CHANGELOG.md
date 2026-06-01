# Project Log: Wintermute Site Updates (2026-06-01)

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

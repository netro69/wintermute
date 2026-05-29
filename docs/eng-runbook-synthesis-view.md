# Engineering Runbook: Wintermute Synthesis View

## Overview
The Synthesis View is a core UI feature of the Wintermute Think Tank. It allows users to switch between a linear, synthesized editorial view and a multi-perspective view that exposes the individual contributions of the four project personas.

## Components

### 1. `<Perspective>` Component
**Location:** `src/components/Perspective.astro`
**Purpose:** Wraps content attributed to a specific architect persona.

**Usage:**
```astro
<Perspective persona="Silicon Architect">
  The thermodynamics of intelligence demand a shift from silicon to...
</Perspective>
```

**Technical Details:**
- Generates persona-specific CSS classes (e.g., `.persona-silicon-architect`).
- Applies signature colors (Cyan, Pink, Green, White) based on the `persona` prop.
- Uses `JetBrains Mono` for labels and `Inter` for body text.

---

### 2. `<ViewToggle>` Component
**Location:** `src/components/ui/ViewToggle.astro`
**Purpose:** A global state switcher for the page's reading mode.

**Logic:**
- Uses a client-side script to manage the `.active` state of buttons.
- Persists the user's preference (`synthesis` vs `perspectives`) in `localStorage`.
- Controls the visual state (opacity/filter) of all `.perspective-block` elements globally.

---

## Deployment & Integration
1. **MDX Integration:** Add the `Perspective` component to the MDX components map in the Astro configuration or page layout.
2. **Page Layout:** Place the `ViewToggle` component in the navigation bar or at the top of the post content.
3. **Styling:** Ensure the `--void`, `--surface`, and `--primary` CSS variables are defined in `global.css`.

## Maintenance
- **Adding Personas:** To add a new persona, simply add a new CSS class rule in `Perspective.astro` following the `.persona-[name]` pattern.
- **Updating Vibe:** All colors are tied to CSS variables; update the root variables in `global.css` to shift the entire site's palette.

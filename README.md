# Wintermute — AI Think Tank

Four debating lenses (Silicon, Training, Agentic, Material) plus a passive Mediator. Historical articles retain their original cast; simulated voices are not statements by the people who inspired them.

## Stack and development

Static Astro + MDX. Node >=22.12.0 required; CI uses Node 24.

```bash
npm ci
npm run dev
npm run check
```

Site: https://netro69.github.io/wintermute/ . Astro `site` is the origin and `base` is `/wintermute`. Internal links use `src/lib/urls.js`; RSS uses absolute project-prefixed URLs. Output is `dist/`. No database, authentication or members gate is currently implemented. Remote deployment was not verified during local cleanup.

## Content

Articles are in `src/content/posts/`. The layout owns the visible H1; do not repeat it in the body. MDX articles that import `Perspective` and contain switchable blocks set `readingViews: true`. Plain legacy articles omit it. New synthesis blocks use `Mediator`; historical `Editorial Synthesizer` blocks remain supported.

Run the regression checks in [TESTING.md](TESTING.md) before publishing. Archive category filters are deferred until a real content model exists; there are no inert controls.

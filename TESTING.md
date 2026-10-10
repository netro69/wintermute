# Wintermute regression checks

Use Node >=22.12.0 (CI: 24).

```bash
npm ci
npm run check
```

`npm test` checks preference normalization, storage-denied initialization/click behavior, idempotency, deployment configuration, shared title ownership and explicit reading-view opt-in.

`npm run test:built` requires `dist/`: validates the current 15-page/13-article baseline, one H1 per page, project-prefixed local links/assets with existing targets, seven reading controls, and all 13 RSS article links. Update deliberate inventory changes in tests. CI executes these on PRs; PRs do not publish.

## Optional real-browser regression

Install puppeteer-core in a separate tooling directory, or provide an existing installation. Set `PUPPETEER_MODULE` to its absolute module directory and `CHROME_PATH` to an installed Chrome executable, then run `npm run test:browser`. These are environment variables, not repository secrets.

The test serves output strictly under `/wintermute/`, checks all 13 articles, seven toggles, persistence, storage-denied fallback, no-JS behavior and 390px reflow. It blocks external font requests for deterministic local checks; it excludes only the browser's undeclared automatic `/favicon.ico` request. This is not a production font/performance audit or full accessibility certification.

Synthesis retains Mediator and historical Editorial Synthesizer blocks, plus unwrapped prose; Perspectives shows all blocks. Without JS, controls remain hidden and full content is available. Native pressed buttons retain visible keyboard focus.

2026-09-17 local receipts: 4 source tests + 3 built tests passed; 15 pages built; real Chrome test PASS, zero application resource failures/page errors.

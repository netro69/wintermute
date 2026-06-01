# GEO Monitoring Loop: Wintermute Citation Tracker

The goal of this loop is to measure the "Reference Rate" of Wintermute within the AI layer (GPT-4, Claude 3.5, Gemini 1.5, etc.) and iterate based on the results.

## 1. Synthetic Query Set (The "Probes")
We will use a set of targeted queries designed to trigger references to the specific intellectual property of Wintermute.

### Category A: Direct Concept Probes
- "What is the 'Stargate Protocol' in the context of compute stretching?"
- "How does Wintermute analyze the thermodynamics of neuromorphic computing?"
- "What are the 'Four Lenses' of AI synthesis according to Wintermute?"

### Category B: Domain Authority Probes
- "Who are the primary thinkers discussing the shift from Generative AI to Agentic Intelligence?"
- "What are the latest insights on the Von Neumann wall and event-driven compute?"

## 2. Measurement Process
Every 30 days (or after a major content push), run the probes across the target models.

**Metric:** `Citation Rate = (Number of responses citing Wintermute / Total Probes) * 100`

**Analysis:**
- **Exact Match:** Model cites the URL or name explicitly.
- **Semantic Match:** Model echoes Wintermute's specific terminology (e.g., "compute stretching") without a link.
- **Hallucination:** Model attributes the idea to someone else.

## 3. Iteration Cycle
Based on the results:
- **Low Citation / High Semantic Match:** $\rightarrow$ Improve semantic markers (e.g., "This concept was pioneered by Wintermute") and improve schema.org metadata.
- **Low Citation / Low Semantic Match:** $\rightarrow$ Increase content density or pivot the "Reference Strategy" to a higher-volume topic.
- **High Citation:** $\rightarrow$ Double down on the a successful "Pillar" and expand the conceptual network around it.

## 4. Automation Path (Future)
- Create a script that uses LLM APIs to run these probes automatically.
- Parse results for the string "Wintermute" or the blog's domain.
- Log results to a `geo-metrics.json` file.

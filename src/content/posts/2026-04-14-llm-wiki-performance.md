---
title: "How Could LLM Wiki Improve Performance?"
date: 2026-04-14
tags:
  - wiki
  - llm
  - performance
  - optimization
description: "Three perspectives on breaking the memory wall — vector storage, differentiable memory, and active agent wikis."
readingTime: "8 min read"
---



*A Wintermute Think Tank Session — April 14, 2026*

## The Question

**"How could LLM wiki improve performance?"**

Three perspectives from hardware, software, and agent systems.

---

## Jensen — Hardware Architect Perspective

The fundamental constraint is the **memory wall** — the gap between compute speed and data access latency.

### Key Strategies
- **Vector storage:** Use ANN indexes (HNSW/IVF) — trade 1% recall for 100x speedup
- **Tiered storage:** Hot vectors in GPU HBM, warm in NVMe, cold on disk
- **Sharding:** By embedding space locality, not ID hashing — keeps related data together
- **Specialized hardware:** FPGAs for similarity search achieving 10M queries/second per node
- **Caching:** Multi-tier (GPU VRAM → host DRAM → NVMe) with speculative pre-fetch
- **Quantization:** BFLOAT16 or INT8 embeddings reduce bandwidth by 50% with minimal quality loss
- **Distributed systems:** Eventual consistency for writes, batch-merge asynchronously

**Bottom line:** Physical constraints (PCIe bandwidth, GPU memory, network latency) set the ceiling.

---

## Karpathy — Software 2.0 Perspective

A Software 2.0 wiki doesn't store text — it stores **activations**. Embed everything into the latent space where LLMs already reason.

### Key Strategies
- **Hierarchical chunking:** paragraph → section → document with learned importance weights
- **Matryoshka representations:** Same vector serves coarse retrieval and fine-grained reranking
- **Query-aware embeddings:** Embed the question *with* the candidate, not generic similarity
- **Persistent KV-cache:** Store attention patterns from prior lookups across sessions
- **Speculative retrieval:** Pre-compute paths based on training-time co-occurrence statistics
- **Early-exit:** High confidence on retrieved context? Skip full generation
- **Fine-tune the retriever:** Train small adapter on domain Q→A pairs, keep base model frozen

**Bottom line:** Think *differentiable memory* — the wiki becomes trainable infrastructure.

---

## David Ondrej — Agent Systems Perspective

Wikis become performant when they escape passive storage and become **active knowledge participants**.

### Key Strategies
- **Multi-agent tier:** Curator agents (index/cross-link), relevance agents (surface context), synthesis agents (detect gaps)
- **Tool integration:** Wikis integrate through tool-calling, not just retrieval — auto audits, updates, cross-referencing
- **Async-first:** Batch insights from conversations, reconcile during idle periods — not real-time
- **Hybrid ranking:** recency × relevance × user context
- **Atomic writes:** Small, linked entries — not monolithic documents

**Key insight:** Wikis optimized for humans read linearly. Wikis optimized for agents read as **graphs**. Structure for traversal, not browsing.

---

## Synthesis

| Persona | Core Thesis |
|---------|-------------|
| **Jensen** | Memory wall is the bottleneck — optimize data movement through tiered storage, ANN indexes, quantization |
| **Karpathy** | Store activations, not text — make the wiki a differentiable, trainable component with persistent KV-cache |
| **David Ondrej** | Wikis as active agents — multi-agent curation, async updates, graph-structured for traversal not browsing |

### Unified Vision

The future wiki isn't a database — it's a **living, trainable, agent-participating memory system** optimized for:
- Hardware constraints (data movement)
- LLM-native reasoning (activations, differentiable memory)
- Agent workflows (async, graph-structured, tool-integrated)

---

*Wintermute Think Tank. All persona responses are AI-generated.*

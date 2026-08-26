---
otero_id: "2-s2.0-105043594050"
title: "Change-aware round-trip benchmarking of LLMs for reliable and efficient artifact co-evolution"
authors: "Dao D.; Bucaioni A.; Cicchetti A."
year: "2026"
journal: "Journal of Systems and Software"
doi: "10.1016/j.jss.2026.113014"
---
# Scopus title-abstract-keyword metadata
Title: Change-aware round-trip benchmarking of LLMs for reliable and efficient artifact co-evolution
Abstract: Large language models are increasingly embedded in software development, yet most evaluations still treat them as one-shot generators for isolated tasks such as code completion or refactoring. In real workflows, however, artifacts such as application programming interfaces, data models, and database schemas co-evolve, and changes must propagate across representations without breaking consistency. When propagation fails, developers incur extra validation, retries, and manual repair, which increases latency and infrastructure cost and undermines sustainable operation. In this study, we ask whether large language models can preserve cross-artifact consistency under change in a round-trip workflow. We apply a controlled edit to one artifact, translate it to its coupled counterpart, and translate it back, then check whether the intended edit persists without drift (i.e., unintended semantic changes or syntactic invalidity). We instantiate this question by synchronizing class-oriented data models with relational database schemas. Using a curated dataset of paired models and schemas and a suite of controlled edit operations, we evaluate four large language model, GPT-5, Qwen3-Next-80B-A3B, DeepSeek V3, and Gemini 2.5, under a unified, reproducible protocol that measures (i) edit persistence, (ii) structural validity (parsability/loadability), and (iii) run-to-run consistency over repeated executions. Our results show that the models handle small, routine edits reliably, but they struggle when edits require structural reorganization. Gemini 2.5 is the most consistent across runs; DeepSeek V3 often preserves the intended semantics but occasionally produces unparsable outputs; Qwen3-Next-80B-A3B exhibits high variance; and GPT-5 often recognizes the change but fails to propagate it coherently through the coupled representation. We contribute a reproducible benchmark and evaluation framework for assessing LLM reliability under artifact co-evolution, together with empirical evidence of current limitations. Overall, the findings reveal a gap between detecting a change and propagating it coherently, underscoring the need for structural validation and human oversight to achieve dependable and cost-efficient LLM-assisted software evolution. © 2026 The Authors
Author keywords: Large language models for software evolution; Round-trip consistency; Software artifact co-evolution
Index keywords: Benchmarking; Relational database systems; Software design; Syntactics; Co-evolution; Code re-factoring; Language model; Large language model for software evolution; Round trip; Round-trip consistency; Software artefacts; Software artifact co-evolution; Software Evolution; Work-flows; Semantics
Document type: Article
Conference: 
Source title: Journal of Systems and Software
Year: 2026
EID: 2-s2.0-105043594050
DOI: 10.1016/j.jss.2026.113014
Retrieval channels: authoritative_outlet_search
Local full-text files: 

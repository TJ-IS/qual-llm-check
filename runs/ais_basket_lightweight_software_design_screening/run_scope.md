# Proposed screening scope — awaiting user confirmation

- Corpus: local `database_fulltext_all` AIS Basket full-text library.
- Publication window: 2021–2025 inclusive.
- Model: `deepseek-v4-flash`.
- Unit of analysis: one complete article per independent API request; never combine multiple articles in one request.
- One output decision only: `target_match=true/false`.
- `target_match=true` requires all three booleans to be true:
  1. individual-level person–software setting;
  2. authors actually built or materially modified a runnable individual-facing software product, task tool, assistant, feature, or interactive prototype;
  3. the reported design approach is feasible for a small research team.
- Pure algorithms/models, mockup-only studies, evaluation of unmodified existing technology, organizational/institutional studies, long ADR, clinical or national infrastructure, bespoke hardware/sensors, multi-year embedding, and otherwise resource-heavy approaches receive `target_match=false` without separate exclusion classes.
- No evaluation-method imitation analysis in this run. Baselines, controls, experiments, ablations, benchmarks, and pre/post comparisons are not required and are not audited in detail.
- For matches, extract the software artifact, individual user/task, concrete design delta, design process, design knowledge, and basic feasibility evidence.
- Proposed default concurrency: 50. No model calls will be made until the prompt is confirmed.

## Prompt assembly

Each independent request contains the shared `system_prompt.md` plus one rendered `user_prompt_template.md` containing the metadata and complete full text of one article.

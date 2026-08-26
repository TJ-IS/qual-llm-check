# Run scope

- Purpose: identify objective benchmark-improvement articles whose problem framing, design derivation, evaluation, and contribution exhibit a genuinely IS-distinctive logic rather than a generic CS/ML/SE/OR benchmark story with an application wrapper.
- Candidate pool: all 1,976 strict matches from `ais_basket_strict_objective_metric_improvement_all/output_v1/decisions.jsonl`, plus the two false negatives manually confirmed in `audit_v1/manual_audit_results.json`.
- Expected candidate count: 1,978.
- Unit of analysis: one complete full-text Markdown article per independent API request.
- Model: `deepseek-v4-flash`.
- Maximum concurrency: 200.
- Full texts are not chunked or combined.
- Stage-one model decisions are used only to construct the candidate file list; their reasoning is not supplied to the model.
- Candidate origin is preserved in the output as `stage1_model_match` or `manual_audit_addition`.
- All prompts, code, decisions, errors, summaries, and reports are isolated in this run folder.

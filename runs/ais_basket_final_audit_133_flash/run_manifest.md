# Run manifest

- Scope: the 133 candidates in the previous strict screen.
- Model: `deepseek-v4-flash`.
- Unit of analysis: one complete locally saved full text per request; articles are never batched into one model request.
- Audit design: two independent audits of all 133 papers, followed by a third full-text adjudication for every disagreement.
- Concurrency: 100 for full runs.
- Output budget: 30,000 tokens per request.
- Final inclusion requires fully objective target construct and measurement, objective improvement as the article-level core goal, and an implemented/instantiated software artifact or component.

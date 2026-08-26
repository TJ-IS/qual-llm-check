# Unified strict AIS Basket screening

- Scope: all locally saved AIS Basket full texts from 2020 through 2027
- Input: `../../database_fulltext_all`
- Model: `deepseek-v4-flash`
- Unit of analysis: one complete local full text per request; no batching and no chunking
- Initial concurrency: 100
- Stage 1: unified strict screen of all 2,475 full texts
- Stage 2: independent red-team re-audit of Stage 1 inclusions only
- Final rule: a paper must pass both stages
- Psychology-related theory guidance is intentionally not a qualification gate in this run

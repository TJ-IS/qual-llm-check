# Run manifest

- Purpose: rescreen the same locally available 2020–2027 corpus under a substantially stricter “fully objective measurement” rule.
- Input: Markdown full texts in `database_fulltext_all`.
- Years: 2020 through 2027 inclusive.
- Unit: one complete article per independent API request; no batching or chunking.
- Model: `deepseek-v4-flash`; temperature 0; maximum concurrency 100.
- Stage 1: strict screen of every article from scratch.
- Stage 2: independent adversarial audit of every Stage-1 positive.
- Final inclusion: Stage-2 `confirmed_strict_match=true` only.
- Calibration: HyperCARS and Augmenting Social Bot Detection must be retained; Pushing Yourself Harder, Achieving a Balance Between Privacy Protection and Data Collection, and Improving Students’ Argumentation Skills must be excluded.

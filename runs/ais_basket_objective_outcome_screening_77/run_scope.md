# Run scope

- Input: the 77 records with `target_match=true` in the prior AIS Basket individual-software-design screening.
- Evidence: complete local full text for each retained record.
- Unit of analysis: one article per independent API request.
- Model: `deepseek-v4-flash`.
- Concurrency: 50.
- Main rule: retain when the design explicitly targets a substantive objective outcome or the study objectively measures at least one substantive central outcome.
- Non-qualifying measurements: self-report-only focal outcomes, manipulation checks, controls, demographics, and treatment-exposure traces.

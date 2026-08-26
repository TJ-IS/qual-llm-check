# Run manifest

- Status: user approved on 2026-08-07.
- Input: locally saved Markdown full texts in `database_fulltext_all`.
- Years: 2020 through 2027 inclusive; only locally available records are processed.
- Local scope at setup: 2,475 full texts (2020: 559; 2021: 552; 2022: 467; 2023: 300; 2024: 277; 2025: 236; 2026: 84; 2027: 0).
- Unit: one complete article per independent API request.
- Model: `deepseek-v4-flash`.
- Maximum concurrency: 100.
- Prompts: the user-edited Chinese prompt files copied from the confirmed draft; only their headings were changed from draft to formal-run status.
- Output: `output_v1`; append-only decisions permit safe resume.
- No full text is copied or downloaded for this run.

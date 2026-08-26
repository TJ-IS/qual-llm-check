# Confirmed and completed run scope

- Status: completed successfully on 2026-08-06; 13,910 model decisions written and 0 request/parse failures.
- Unit of analysis: one complete full-text Markdown article per independent API request.
- Model: `deepseek-v4-flash`.
- Maximum concurrency: `200`.
- Temperature: `0`.
- Output mode: one validated JSON object per article, resumable JSONL.
- Full texts are not chunked or combined.
- Confirmed local corpus: all 13,910 Markdown files in `database_fulltext_all`.
- Corpus scope: the local 11-journal extended corpus includes the strict AIS Senior Scholars Basket journals plus Decision Support Systems, Information & Management, and Information and Organization.
- Model results: 1,976 strict matches and 11,934 nonmatches.
- Prompt fingerprint: `d863ce55e69db3678bb2e808b9bd427a574df987dd1f237d7deda5aeebd76162`.

## Exact prompt assembly

For each article, the request will contain exactly two messages:

1. `system`: the complete contents of `system_prompt.md`.
2. `user`: the complete contents of `user_prompt_template.md` after replacing the metadata placeholders and `{fulltext}` with that one article's complete Markdown text.

No prior article, batch summary, or other article text will be placed in the same request.

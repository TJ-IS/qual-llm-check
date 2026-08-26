# Proposed scope and execution policy

- Corpus: `database_fulltext_all`
- Publication years: 2021-2025 inclusive (five complete years)
- Available Markdown full texts: 1,832
- Total text size: 204,411,271 bytes
- Model: `deepseek-v4-flash`
- Unit of analysis: one article per independent task; never combine articles in one request
- Long articles: split only within the same article, extract evidence per chunk, then synthesize one article-level JSON decision
- Retain for manual review: both `strong_candidate` and `promising_candidate`
- User confirmed the prompts and full 2021-2025 run on 2026-08-04.

## Execution

The confirmed execution sends every article as one complete full-text request. No article-level chunking and no metadata or keyword prefilter are used. Results are checkpointed after every successful article, and the run is resumable by prompt fingerprint.

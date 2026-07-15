---
name: otero-open-api
description: Search and download literature from the read-only Otero AIS Senior Scholars' Basket database. Use when listing Basket journals, searching papers or authors, filtering by year or journal, resolving DOI metadata, fetching MinerU Markdown or PDF URLs, or bulk-downloading full text for every article matching a term such as construct.
---

# Otero Open API

Use the public, read-only Otero API at `https://ais.kexu.win/api/open/v1`. Prefer the bundled downloader for multi-page searches or full-text archives; use direct GET requests for small lookups.

## Search or inspect records

1. Read [references/api.md](references/api.md) when endpoint parameters or response shapes matter.
2. Call `/journals` before applying exact journal filters.
3. Use `/articles` for papers and `/authors` for people. Use `/search` only when either kind may be intended.
4. Paginate until `page >= totalPages`; set `pageSize=100` for bulk work.
5. Treat `q` as the database's own search semantics: it covers title, abstract, DOI, authors, and indexed full text.

## Download all matching full text

Run the standard-library downloader from the repository root:

```powershell
python .agents\skills\otero-open-api\scripts\download_fulltext.py --query construct --output database_fulltext_construct
```

The script:

- retrieves every page from `/articles`;
- partitions full-corpus pagination by the 11 exact journal names, then verifies the union against the global result total;
- writes `metadata.jsonl`, `results.jsonl`, `summary.json`, and one Markdown file per available article;
- fetches MinerU Markdown through `/items/by-doi/markdown`;
- records missing DOI, unavailable Markdown, and request failures without silently dropping records;
- resumes safely by skipping already downloaded files;
- leaves Markdown image references intact but does not download image files.

Use `--limit N` only for tests. Use `--workers N` conservatively; the default is 8. Re-run with `--reuse-metadata` to resume or retry non-successful records without repeating the paginated search.

## Validate a bulk result

Inspect `summary.json` and require:

- `search_total == metadata_records` for a complete search harvest;
- every metadata record to have a corresponding status in `results.jsonl`;
- `downloaded + missing_doi + unavailable + failed == metadata_records`.

Report unavailable records honestly; the public full-text endpoint requires a DOI and may return 404 when parsed Markdown is absent.

## Safety

Use GET only under `/api/open/v1`. Do not call POST, PATCH, or DELETE. Do not scrape attachment images unless the user explicitly requests them.

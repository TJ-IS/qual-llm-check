# Otero Open API reference

Source: <https://ais.kexu.win/docs> and <https://ais.kexu.win/api/open/v1/SKILL.md> (checked 2026-07-13).

Base URL: `https://ais.kexu.win/api/open/v1`

All endpoints are GET-only and expose non-deleted top-level items in the 11 AIS Senior Scholars' Basket journals. The internal unfiled bucket is excluded.

## Pagination and filters

List endpoints return `{ items, total, page, pageSize, totalPages }`.

- `page`: default 1
- `pageSize`: default 20, maximum 100
- `journal`: one exact journal name
- `journals`: comma-separated exact names; mutually exclusive with `journal`
- `year`: exact publication year
- `yearFrom`, `yearTo`: inclusive range
- `type`: item type such as `journalArticle`

## Endpoints

- `GET /journals`
- `GET /articles?q=blockchain&page=1&pageSize=100`
- `GET /authors?q=Smith&page=1&pageSize=20`
- `GET /authors/{id}/items?page=1&pageSize=20`
- `GET /search?q=platform&page=1&pageSize=10`
- `GET /items/by-doi?doi=10.1234/example`
- `GET /items/by-doi/markdown?doi=10.1234/example`
- `GET /items/by-doi/pdf-url?doi=10.1234/example`

`/articles` accepts an optional `q` and supports filter-only browsing. Its query searches title, abstract, DOI, authors, and indexed full text. `/authors` requires `q`. `/search` returns separately paginated `articles` and `authors` buckets.

The Markdown endpoint returns JSON shaped like:

```json
{
  "doi": "10.2307/25148814",
  "itemKey": "RBWD4H8Q",
  "state": "done",
  "markdown": "# Full article ..."
}
```

The PDF URL endpoint returns a relative attachment URL; prepend `https://ais.kexu.win` before downloading.

Errors use 400 for invalid parameters and 404 for missing records or unavailable Markdown/PDF.

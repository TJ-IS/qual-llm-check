# Third-party content and data rights

This repository combines original code/research records with third-party scholarly material. Availability through an API or website does not itself grant redistribution rights.

## Otero full-text corpus

`database_fulltext_all/` contains full-text Markdown retrieved through the read-only Otero AIS Senior Scholars' Basket service. Local metadata currently records a non-empty `rights` value for only a very small fraction of records. No repository-wide license is asserted for these articles.

Before a public upload, verify publisher/article terms or replace the full texts with metadata, stable identifiers, checksums, and the reproducible downloader. A private repository may have different practical exposure but still does not create redistribution rights.

## Other controlled collections

Scopus exports, locally collected papers, PDFs/HTML source snapshots, benchmark/pilot assets, and `thesis_collection/` may carry database or publication restrictions. They are excluded or conditionally selected by `.gitignore` and the retention manifest pending review.

## Repository-owned material

Code, repo-local skills, prompts, ledgers, and manuscript drafts require an owner-selected license. No top-level `LICENSE` has been added because the owner has not yet specified terms and a code license must not be read as licensing third-party full text.

See `docs/research_program/artifact_retention_manifest.md` for the current selection and `docs/research_program/github_upload_checklist.md` before staging.

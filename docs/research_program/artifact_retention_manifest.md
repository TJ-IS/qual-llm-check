# Artifact retention manifest

Snapshot date: 2026-08-25. This is a publication selection policy, not a statement that third-party content may legally be redistributed.

## Repository snapshot

Before curation, the working tree contained 224 tracked files, 5 pre-existing modified files, about 12.3k visible untracked files, and about 107.4k ignored files. The workspace was approximately 11.38 GiB excluding `.git`; most of that was `pilot_assets/` (6.46 GiB), `runs/` (2.36 GiB), the canonical Otero corpus (1.085 GiB), and the obsolete/overlapping construct corpus (0.639 GiB).

The following pre-existing modified files belong to the user and must be preserved during staging:

- `.agents/skills/otero-open-api/SKILL.md`
- `.agents/skills/otero-open-api/scripts/download_fulltext.py`
- `.gitignore`
- `runs/coding_agent_ux_misq_isr/00_document_index.md`
- `runs/new_construct_objective_measurement_deepseek_analysis/analyze_fulltext.py`

After the final ignore/allowlist changes, the read-only readiness script reports 25,363 tracked-or-visible publication candidates totaling about 1.5104 GB. No candidate file is 50 MiB or larger, `.env` remains ignored, and the overlong v11 debt-review paths are outside the selected set. The remaining wide candidate directories are `database_fulltext_all/` (13,914 selected entries), `runs/programming_systematic_literature_review/input_metadata/` (5,642), and `input_stage2/` (3,036). These are performance warnings rather than current Git object blockers.

## Include: project control and reproducibility

- `AGENTS.md`, `README.md`, `.gitignore`, `.gitattributes`, and existing source/configuration files.
- `.agents/skills/` including the Otero skill and the three new repo-local skills.
- `docs/research_program/` and `THIRD_PARTY_CONTENT.md`.
- Existing tests and scripts needed to reproduce the selected runs.

## Include conditionally: canonical Otero corpus

Path: `database_fulltext_all/`

Inventory: 13,910 Markdown full texts; `metadata.jsonl` and `results.jsonl` with 13,913 records each; `summary.json`; `_filelist.txt`; 3 unavailable and 0 failed downloads. No Markdown file exceeds 1 MiB. The directory totals approximately 1.085 GiB.

This is the only canonical Otero corpus. `database_fulltext_construct/` is an older overlapping query collection and remains ignored. The canonical directory is deliberately no longer ignored, and its two JSONL evidence files override the generic JSONL ignore rule.

Publication condition: confirm whether the destination is private or public and complete a redistribution-rights review. Only 5 of 13,913 local metadata records have a non-empty `rights` field; public downloadability is not a license. The current Git policy uses ordinary Git for many small compressible text files, not one LFS object per paper. The 13,916-entry flat directory exceeds GitHub's performance recommendation; preserve the current compatible path for now and document any future sharding migration.

## Include: screening evidence packages

| Package | Required paths | Status |
|---|---|---|
| Public data/objective metric | `runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/` config, scope/prompts, run/audit scripts, `output_v1/summary.json`, decisions, strict matches, include summary, 51-paper report | 2,475/2,475; strict include 51 |
| Security relevance | `runs/ais_basket_security_relevance_fulltext_flash_v1/` config, scope/prompt, run/audit scripts, output decisions/summary, `audit_final_cn.md`, `audit_v3_final.md`, missed-keyword and corpus-mismatch records | 388 provisional; 36 corpus mismatches require repair |
| Security algorithm v2 | `runs/ais_basket_security_algorithm_development_flash_v2/` config, scope/prompt, main/audit scripts, output decisions/summary, search query, 99-paper report | 99 algorithm/method papers; distinct from broad security relevance |
| Final audit 133 | `runs/ais_basket_final_audit_133_flash/` prompts, config, script, manifest, summary, final report, deliverable CSV/JSONL, and three reviewer/adjudication decision streams | 133 audited; 52 included. Raw audit-A has 141 records/8 repeated IDs; the final trail has 133 unique IDs. |

The `.gitignore` exceptions retain raw decisions for these packages while continuing to ignore generic CSV/JSONL caches elsewhere.

## Include: manuscript evidence and milestones

Canonical v11 directory:

`runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews/v11_iterative_literature_rewrite/`

Required:

- canonical ledgers 163, 164, 165, 168–172, and 175;
- current rejected-predecessor manuscripts 184–186;
- direct predecessors 179, 182, and 183;
- ten selected v15 current receipts listed by `.gitignore` exceptions;
- nine selected audit/rebuild scripts listed by `.gitignore` exceptions.

Retain the original 34–36 manuscripts, v10 baseline 154 and drafts 157/159/161, and representative v3/v3.1/v7/v8 materials as milestone/failure evidence. Their status must remain superseded or rejected unless the current-state file says otherwise.

The full `audit_artifacts/` directory contains 1,107 files and about 171.44 MiB of near-successor mappings, copied HTML/PDF sources, and historical receipts. Only the selected current receipts and reproducibility tools are unignored for the main repository. This does not delete the local archive.

## Ignore or keep outside the public main repository

- `.env`, `.venv/`, `.uv-cache/`, `__pycache__/`, `*.pyc`, caches, progress logs, and temporary renders.
- `pilot_assets/` (6.46 GiB of externally versioned assets and nested repositories).
- `database_fulltext_construct/` (overlapping/partly stale Otero query corpus).
- `database_scopus_codingagent/`, `thesis_collection/`, and other controlled third-party databases pending license review.
- untracked PDF/HTML files under `source_snapshots/`; retain their URL/hash README where available and force-add originals only after rights review. Previously tracked source PDFs require a separate history/licensing decision.
- bulk v11 audit artifacts not selected above; old `.pkl` caches; generated sentence inventories; one-off scan scripts and outputs.
- raw private Codex task transcripts and credential/configuration values.

Ignored means “not selected for this upload,” not permission to delete local data.

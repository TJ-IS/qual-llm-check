# Repository guidance

This repository contains two related research programs: Coding Agent security manuscripts and AIS full-text screening. Treat repository artifacts—not a long-running goal state or a task's final message—as the durable source of truth.

## Route first

- For writing, revising, auditing, or resuming the three Coding Agent security manuscripts, use `$coding-agent-manuscript`.
- For AIS Basket retrieval, full-text classification, public-data/benchmark screening, corpus repair, or recall/precision audits, use `$ais-fulltext-screening`.
- For task-history recovery, handoffs, artifact status, repository curation, or GitHub preparation, use `$research-project-continuity`.
- For Otero database search and full-text acquisition, use `$otero-open-api`.

Read [docs/research_program/README.md](docs/research_program/README.md) before broad work. Do not infer acceptance from filenames such as `final`, `PASS`, or `终稿`; consult the current-state and conversation catalogs.

## Cross-cutting rules

1. Keep scope bounded to an inspectable artifact or one complete major section. Open-ended scholarly writing must not be represented as a single autonomous goal.
2. Verify consequential claims against source text. Mechanical coverage, citation counts, hashes, and automated scans are diagnostics, never proof of scholarly quality.
3. Preserve user work and predecessor artifacts. Record whether an output is authoritative, accepted, provisional, superseded, or rejected.
4. Give sub-agents frozen, non-overlapping packages with exact source sections, ledger pointers, exclusions, and return fields. Independently inspect the decisive originals and the submitted prose.
5. Never commit credentials, API keys, private task transcripts, or unlicensed material. Do not push: the repository owner performs the final GitHub upload.
6. Keep committed skills, scripts, manifests, and public instructions usable from a clean Windows or macOS clone. Use repository-relative, case-exact paths; document `python`/`python3` selection; preserve UTF-8 and LF; and label static portability checks separately from runs actually completed on the target OS.

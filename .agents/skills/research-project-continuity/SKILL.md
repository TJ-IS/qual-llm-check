---
name: research-project-continuity
description: Resume, curate, hand off, or publish this long-running research repository from durable artifacts. Use when interpreting prior Codex tasks, deciding which drafts/runs are authoritative, recording checkpoints and user corrections, preparing Git/GitHub, or preventing context/Goal drift. Do not use as a substitute for the manuscript or screening domain skills.
---

# Research Project Continuity

The repository is the control plane. A task's Goal status, final message, token expenditure, or `PASS` file is not durable acceptance evidence.

## Resume safely

1. Read `docs/research_program/current_state.md`, `docs/research_program/requirement_registry.md`, and the relevant rows in `docs/research_program/conversation_catalog.md`.
2. If an applicable control is `conflict`, present both operative readings, affected scope, and a recommended resolution to the user. Do not silently choose or declare the checkpoint complete before confirmation; continue only unaffected work.
3. Inspect the working tree and preserve overlapping user changes.
4. Identify the current authoritative/provisional artifact and its rejected or superseded predecessors.
5. Route domain work to `$coding-agent-manuscript`, `$ais-fulltext-screening`, or `$otero-open-api`.
6. Define one bounded, inspectable checkpoint with explicit acceptance criteria.

Use [references/recovery-and-checkpoints.md](references/recovery-and-checkpoints.md) when a task was interrupted, compacted, or previously declared complete. Do not reopen an open-ended writing Goal. Deterministic implementation subtasks may still use ordinary plans/tests, but the scholarly state remains in files and acceptance records.

## Curate history

Classify artifacts using [references/artifact-taxonomy.md](references/artifact-taxonomy.md). Preserve user corrections and failed acceptance claims because they prevent recurrence. Do not dump raw private task transcripts into the repository; maintain a curated catalog with task ID/title, artifacts, status, and transferable lesson.

When adding a new history entry, distinguish within-task outcomes. A screening phase can be accepted while a manuscript phase in the same task is rejected.

When a user correction changes reusable behavior, or when a skill is audited against prior tasks, follow [references/requirement-traceability.md](references/requirement-traceability.md). Update the authoritative rule and the public requirement registry in the same checkpoint. Keep minimal exact quotations and message provenance only in an ignored private audit. Task-level catalog coverage is not requirement-level integration. A newly discovered material contradiction remains `conflict` until the user confirms its resolution.

## Hand off

Create a pointer-rich checkpoint, not a narrative duplicate. Include exact paths, versions/statuses, decisions, source/ledger locations, tests or audit evidence, unresolved blockers, and the next bounded action. References should be sufficient for another agent to reopen the original evidence.

Sub-agents receive the relevant persistent ledgers and acceptance rules, not merely a prose summary. Use non-overlapping responsibilities and reconcile their return into the canonical artifact.

## Prepare publication

Follow [references/github-publication.md](references/github-publication.md). Keep canonical corpora, verified source/evidence, successful or explicitly provisional run artifacts, reusable scripts, ledgers, and repo-local skills. Ignore caches, environments, logs, duplicate derived exports, and superseded bulk audit debris unless a manifest explicitly preserves them.

Never commit secrets, provider configuration, raw private conversations, or material without publication rights. Audit ignored critical files, individual file sizes, repository size, directory width, long paths, and the cross-platform continuation contract before staging. Do not push; the repository owner performs the upload.

## Acceptance

A continuity checkpoint is complete only when:

- paths resolve and statuses are explicit;
- current and predecessor artifacts cannot be confused;
- user corrections are represented;
- every affected requirement atom has an active, qualified, run-specific, superseded, open, or conflict disposition;
- no applicable `conflict` is represented as resolved without recorded user confirmation;
- mandatory skills and ledgers contain no unresolved contrary wording;
- domain evidence remains traceable;
- Git retention rules preserve required artifacts without exposing secrets;
- a fresh agent can identify the next bounded action without relying on chat memory.

Read [references/failure-patterns.md](references/failure-patterns.md) when a prior run looks “finished” but the user reports poor quality.

# Artifact taxonomy and retention logic

## Evidence authority

- **authoritative_evidence** — original full text, verified metadata, frozen prompts/configs, direct-source notes, canonical corpus, and integrity audit.
- **accepted_output** — explicitly accepted result for a named scope.
- **provisional_output** — usable output with unresolved conditions.
- **accepted_workflow_pattern** — repeatable method that produced auditable value.
- **superseded_draft** — replaced artifact retained for provenance.
- **failure_and_user_correction** — false completion, rejected claim, or user feedback that changes future gates.
- **transient_derived_artifact** — cache, log, duplicate export, temporary mapping, environment, or rebuildable output.

An artifact can have more than one dimension: a task may contain authoritative inputs, an accepted screening run, and rejected prose.

## One canonical owner per responsibility

Maintain one cumulative ledger for each enduring responsibility: evidence/citations, paper-specific feasibility, screening prompt/config, corpus integrity, or publication manifest. Frozen audits and generated statistics should point to the canonical ledger rather than become competing state stores.

Append durable changes; compact or index sedimented logs instead of forcing every future agent to read them wholesale.

## Conversation-derived records

Retain:

- stable task ID and exact title;
- date range;
- concrete artifact paths;
- accepted/provisional/rejected status by phase;
- user corrections and transferable lesson.

Exclude raw private transcripts, credentials, provider settings, repetitive progress updates, and unsupported self-evaluations. If exact wording is scientifically necessary, store only the minimal excerpt permitted and its provenance.

## Publication priority

1. Repo-local skills, instructions, source code, and small frozen configs.
2. Canonical full-text/evidence corpus when rights allow.
3. Accepted or provisional run decisions plus audits and denominator summaries.
4. Canonical manuscript ledgers and explicitly identified predecessor/successor drafts.
5. Selected failure exemplars and user-correction summaries.
6. Rebuildable bulk artifacts only when their regeneration cost or audit value justifies size.

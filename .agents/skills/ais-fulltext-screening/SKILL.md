---
name: ais-fulltext-screening
description: Design, execute, resume, or audit AIS Basket systematic retrieval and full-text screening in this repository. Use for search strategies, security relevance, security algorithm development, objective metric/benchmark, public-data eligibility, corpus integrity, recall/precision, or model-run accounting. Do not use for Coding Agent manuscript prose.
---

# AIS Full-Text Screening

Keep four layers separate: corpus identity, retrieval, classification, and gold-standard audit. A completed model run is not automatically a valid evidence set.

Read the screening controls in `docs/research_program/requirement_registry.md` and the current run status before adapting an earlier query, prompt, or result set. If an applicable control is `conflict`, present both readings and their run-level consequences to the user; do not choose or close the gate before confirmation.

## Route the decision first

State which label is being produced:

- broad security relevance;
- security algorithm/method development;
- objective metric or benchmark contribution;
- public-data eligibility;
- another explicitly defined construct.

These are not interchangeable. Read [references/evidence-gates.md](references/evidence-gates.md) before adapting an earlier prompt or count.

If the task designs or revises a systematic search, follow `2. Design and justify retrieval` in [references/scope-and-run.md](references/scope-and-run.md) before screening. Retrieval fields and search strings require a reproducible rationale grounded in directly inspected authoritative review methods; search hits are candidates, not classifications.

## Before any expensive run

Follow [references/scope-and-run.md](references/scope-and-run.md). Show the user the candidate prompt, population/time/journal scope, full-text interpretation, model, concurrency, resume behavior, and inclusion/exclusion gates. Do not start the expensive corpus call until the user confirms them.

Freeze the approved configuration and prompt with the output. Run a small dry run to validate parsing and recovery without treating it as scientific evidence. Use resumable writes and never silently truncate full text.

## Corpus integrity

Apply [references/corpus-integrity.md](references/corpus-integrity.md) before classification and again during audit. Resolve identity by normalized title -> metadata CSV -> CSV DOI and verify that the local full text corresponds to the record. Do not trust a Markdown DOI header as the canonical identity.

Report the total corpus, eligible inputs, unavailable/corrupt items, model successes/failures, parsed decisions, and output-set size. A `0 failure` model run can still sit on mismatched full text.

## Audit and adoption

1. Evaluate retrieval against a full-text standard using recall and precision, not hit count alone.
2. Audit false inclusions and false exclusions across boundary strata.
3. Separate reference-list-only matches from substantive article text.
4. Repair/reclassify known corpus mismatches before calling a set gold.
5. Record prompt/config hashes, denominators, exclusions, and unresolved cases.

Use [references/historical-baselines.md](references/historical-baselines.md) and `docs/research_program/current_state.md` to interpret existing result sets. Never infer current scope or status from a count or filename.

When a manuscript uses an individual paper from a set, directly verify that paper's original text. When it uses the set's count, coverage, absence claim, or representativeness, also carry the set's current corpus-integrity and acceptance status into the manuscript evidence record.

Delegate only non-overlapping strata or independent audit responsibilities. Provide the exact frozen prompt, schema, corpus slice, decision definitions, prior error categories, and return fields. The primary agent must spot-check originals and reconcile all slices against the same denominator.

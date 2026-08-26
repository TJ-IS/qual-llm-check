# Authoritative sentence-prototype workflow

Use this workflow to satisfy `M-ANCHOR-01/L26`. A writing prototype is a directly inspected sentence in authoritative IS prose that shows how to perform a comparable rhetorical move. It is not required to express the same domain claim or use the same words.

## Place in the writing cycle

Build the complete major-section argument and draft its paragraph chain first. Then iterate over every reader-visible natural-language sentence before the references, including natural language in tables, algorithms, captions, and notes. A difficult sentence may be searched before drafting, but retrieved examples must not determine the paper's theory, evidence, or macro argument.

The frozen discovery pool is [authoritative-writing-corpus.json](authoritative-writing-corpus.json). ACAA and DSDL are the series structural baseline. RADAR and the remaining papers are section-local comparators. Expand the pool only after verifying the new paper's bibliographic identity, full text, journal/authority role, and exact responsibility in the canonical literature ledger.

## Iterative verification cycle

1. Classify the target as source-dependent claim, author synthesis, author protocol/expectation, internal cross-reference, or another explicit responsibility.
2. Name its rhetorical function and local relation: what it inherits, what it adds, its paragraph position, its citation responsibility, and what the next sentence consumes.
3. Use `../scripts/search_writing_prototypes.py` to retrieve candidates by function, section, source axis, and optional query terms. Search is discovery only.
4. Reopen each viable candidate in its complete original paragraph and carrying major section. When context permits, read the preceding and following major sections as well. Reject a candidate selected only by keywords, topical similarity, or an isolated sentence.
5. Compare rhetorical responsibility, sentence construction, given-to-new relation, paragraph position, citation placement and support responsibility, disclosure stage/tense, and punctuation function. The match need not preserve content or wording.
6. Revise, split, move, or delete the target sentence. Do not copy distinctive expression, data, results, or domain claims.
7. Persist the verified prototype and revision effect. Re-run the cycle when the sentence or its paragraph role materially changes.

Author-designed methods, protocols, estimands, planned tests, and expected diagnostics still require a writing prototype. Their match may be structurally looser because the substantive content is new: use an analogous method disclosure, design-choice justification, planned-evaluation, or boundary sentence. They do not need an identical historical procedure or result. If no acceptable prototype is found, broaden the authority pool or revise the target; the sentence remains open rather than receiving a no-anchor exemption.

## Status and record

Use these current statuses:

- `PROTOTYPE_SEARCH_OPEN` — no candidate has survived original-context inspection.
- `PROTOTYPE_CANDIDATE` — retrieval found a possible sentence, but the full paragraph/section has not yet been adjudicated.
- `PROTOTYPE_REVISE` — the original comparison exposed a mismatch and the target must change.
- `PROTOTYPE_VERIFIED` — the main agent directly verified the original context and recorded the transferable and non-transferable dimensions.

For every sentence retain:

- target path/hash, location, sentence, responsibility class, rhetorical function, paragraph task, given-to-new relation, and citation responsibility;
- authority ID/title, exact source sentence, line, full paragraph line/window, carrying section, and adjacent-section window actually read;
- match dimensions: construction, logical relation, paragraph position, citation placement/responsibility, disclosure stage, and punctuation function;
- transferable skeleton, non-transferable content, substantive-evidence status, revision made, reviewer, and current prototype status.

`PROTOTYPE_VERIFIED` says only that the writing move is a sound model. Source-dependent facts, theories, inherited methods, data, and results separately require substantive evidence under `M-EVIDENCE-01`. A prototype never becomes a citation merely because its syntax or reasoning pattern is useful.

## Script use

The script verifies corpus hashes and exact path case, builds an in-memory sentence index, and ranks candidates. Run it from the repository root with Python 3.10 or newer. The examples use `python3`, which is conventional on macOS/Linux; on Windows replace it with `python` or the workspace-bundled interpreter.

```console
python3 .agents/skills/coding-agent-manuscript/scripts/search_writing_prototypes.py --function theory-bridge --source ACAA-2024-ISR --source DSDL-2023-ISR --limit 8
python3 .agents/skills/coding-agent-manuscript/scripts/search_writing_prototypes.py --function method-step --query "state update" --section "method|design" --context paragraph --limit 10
python3 .agents/skills/coding-agent-manuscript/scripts/search_writing_prototypes.py --function prior-work --axis series_structural_baseline --citation with --json --limit 12
```

Available functions are `context`, `prior-work`, `gap`, `theory-bridge`, `research-question`, `artifact-overview`, `method-step`, `evaluation-design`, `result-interpretation`, `contribution`, and `boundary`. `--section` is a case-insensitive regular expression. Repeat `--source` or use `--axis` to restrict the pool. `--citation with` finds models that place explicit citations, while `--citation without` isolates author-owned transitions or protocol disclosure. `--context paragraph` prints the full source paragraph; JSON output always includes it.

The score is only a retrieval heuristic based on rhetorical markers, section fit, and query-token overlap. It cannot issue `PROTOTYPE_VERIFIED`, determine citation support, or replace full-section reading.

`context_warnings` marks MinerU replacement characters or unresolved reference markers in the source paragraph. Such a candidate must be reopened in the PDF or another faithful full-text rendering before verification; the extracted Markdown alone cannot carry the final prototype record.

If the expected interpreter is not on PATH, load the workspace dependencies and substitute the returned bundled Python executable for that run. Do not hard-code a user-specific or runtime-version path into the repository. A Windows-side syntax/path audit does not establish that the script ran on macOS; retain that target-runtime condition until the smoke command succeeds in the macOS clone.

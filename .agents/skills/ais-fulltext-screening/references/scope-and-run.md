# Scope and run protocol

## 1. Freeze the scientific question

Record:

- journal population and years;
- metadata or full-text population and exact corpus snapshot;
- target label and decision unit;
- required evidence relation, such as mention, use, measurement, development, or core contribution;
- required context role, such as research object, mechanism, outcome, empirical setting, or incidental example;
- inclusion, exclusion, and uncertainty rules;
- whether references/appendices count as evidence;
- public-data or objective-metric gates, if any;
- intended downstream use: discovery, screening, benchmark, or gold-standard audit.

Use ordinary-language examples and boundary counterexamples. A broad security query and an algorithm-development query require different prompts and standards.

Rules such as “the construct must be the main contribution” or “programming activity must be the research object” are run-specific settings, not universal screening gates. Preserve genuine scientific uncertainty rather than forcing an item into a Boolean label merely to complete execution.

## 2. Design and justify retrieval

Freeze `retrieval_mode` as corpus enumeration, database query, citation chasing, or an explicit combination. A complete local-corpus enumeration does not need an invented database search string.

For each queried database or index, record:

- database/index name, query date, exact field codes, and the authoritative field-semantics source;
- the complete executable query, filters, hit count, export/version identity, and deduplication rule;
- the exact mapping of title, abstract, and keyword fields for that backend; for example, `TITLE-ABS-KEY` is a Scopus dialect and is not a universal field name;
- each concept block, its terms and term sources, the boundary it represents, its expected recall/precision effect, and known positive and negative cases;
- all revisions prompted by a missed known positive, an unmanageable false-positive pattern, or a backend syntax difference.

Directly inspect at least one authoritative, functionally matched systematic review's complete Methods/search section and relevant appendix. Record its bibliographic identity, exact section/page, databases, fields, search logic, and screening order, then mark each element as adopted, adapted, or rejected with a reason. Adapting syntax across databases is author work and must not be described as the source's verbatim procedure.

Treat retrieval hits and full-text inclusion decisions as separate ledgers. Forward/backward citation chasing is a supplementary mode only when the frozen retrieval plan assigns it that role.

## 3. Obtain confirmation

Before a large model run, show the user:

- system and user prompts;
- scope and interpretation choices;
- model/provider and expected structured schema;
- concurrency, retry, timeout, and resume policy;
- dry-run size and acceptance checks;
- for database retrieval, the exact queries, field mappings, authoritative-method comparison, and known-case pilot;
- output directory and estimated scale/cost when known.

Start only after explicit confirmation. Preserve the approved prompt and configuration in the run directory.

## 4. Preflight

- Verify corpus/title/metadata alignment on a sample and known edge cases.
- Confirm unique record IDs and deterministic output keys.
- Validate UTF-8 and JSON/CSV parsing.
- Ensure full text is not silently clipped; if a model limit requires segmentation, freeze the segmentation/aggregation rule.
- Test idempotent resume and failure recording.
- For database retrieval, verify that known positives are returned, inspect a sample of predictable negatives, and preserve the query revision history.

## 5. Execute and monitor

Append one durable decision record per input. Separate attempts, model outputs, parsed decisions, and final derived lists. Never overwrite the only raw response with a repaired label.

Report progress using the frozen denominator. Retry rules must distinguish transient transport errors, parse errors, and scientific uncertainty. Do not coerce an uncertain scientific decision merely to reach 100% parsed output.

## 6. Close the run

Produce a machine-readable summary and human audit containing:

- corpus snapshot and denominator reconciliation;
- prompt/config identity;
- success, failure, retry, parse, inclusion, exclusion, and uncertain counts;
- duplicate and missing-ID checks;
- corpus-integrity findings;
- sampled false-positive/false-negative analysis;
- limitations and whether the set is exploratory, provisional, or accepted.

Also write an adoption manifest containing:

- set path/ID, target label, journal/year boundary, corpus snapshot, scientific denominator, and unique-record count;
- prompt/config identity and the evidence/corpus-integrity basis for the assigned set status;
- known mismatches, unresolved items, repairs, reclassifications, and the audited false-positive/false-negative scope;
- allowed and prohibited downstream uses, any superseded set, and the review date.

Map status to use conservatively:

- an exploratory candidate set supports discovery only;
- a screened set may supply single-paper candidates after direct source reading, but does not establish completeness or a gold standard;
- a provisional standard may support disclosed exploration, diagnostics, or sensitivity analysis, but not final recall, final population counts, or an undisclosed gold standard;
- only an accepted standard supports set-level claims within its frozen population, years, journals, and label boundary.

If no status is explicitly assigned, downstream users must not infer `accepted`. Regardless of set status, manuscript claims about an individual paper return to that paper's original text.

A completed denominator closes execution, not scientific validation.

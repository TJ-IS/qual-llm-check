# Corpus identity and integrity

## Canonical identity chain

Resolve each article through:

`normalized title -> metadata CSV record -> DOI from the CSV -> expected local full text`

The DOI header in a generated Markdown full text is not the canonical resolver. It may be missing, malformed, or inherited from a mismatched document.

## Pre-run checks

- Unique normalized title and stable record ID.
- Expected journal/year boundaries.
- Metadata-to-file coverage and unavailable items.
- File is non-empty, parseable, and plausibly article text.
- Title/authors/venue/DOI signals agree across metadata and full text.
- No duplicate file silently represents multiple records.

## Mismatch handling

Do not delete or overwrite the only suspect file. Record expected identity, observed identity, mismatch type, downstream decisions affected, repair source, and reclassification status. Keep the pre-repair decision distinguishable from the repaired one.

When aggregating retrieval hits, distinguish substantive body text from abstract-only, bibliography-only, appendix, and incidental matches. Reference sections are useful for citation discovery but can badly inflate topical retrieval.

## Denominator reconciliation

At minimum reconcile:

`metadata population = available valid full texts + unavailable + corrupt/mismatched awaiting repair`

and

`eligible model inputs = successful parsed decisions + terminal failures + explicitly unresolved decisions`.

Every derived inclusion list must be traceable to these stable IDs. Report missing and duplicate IDs, even if both are zero.

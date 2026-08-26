# ARB60 exact-identifier-lineage development discovery audit

> Development/discovery evidence only. This report is not confirmatory and does not evaluate MECHANISM-PROCEED.
> The primary typed score is the query-only deployment selection frozen before gold access; best-found scores are oracle ceilings only.
> The mechanism is whole-token exact-identifier occurrence lineage, not call/import/dependency semantics.

## Integrity and provenance

- Executor schema contract: `deployment_query_only_output@14d00c5b`
- Manifest SHA256: `885cf615e7e5bd6d713c2aefe1b5792da5915ac3f17d545acab6673b0f0f009c`
- Batch SHA256: `ca45c9fb9fb0eeb7028a2e737615cd126b6ff22d731d92476ef429943d0994e2`
- Denominator: 60 tasks; 20 per task type
- Repositories/snapshots: 13/54
- Official lexical/BM25/RepoMap Recall@20 cross-check: passed
- Official legacy 8K-character fields used as canonical BCY: no

## Query-only primary versus baselines

| Scope | Comparator | N | Query BCY | Baseline BCY | Delta | W/T/L | Query recall | Baseline recall | Delta | W/T/L |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| overall | lexical | 60 | 0.3583 | 0.3194 | 0.0389 | 16/31/13 | 0.4889 | 0.5056 | -0.0167 | 16/27/17 |
| overall | bm25 | 60 | 0.3583 | 0.1569 | 0.2014 | 22/30/8 | 0.4889 | 0.3958 | 0.0931 | 20/25/15 |
| overall | repomap | 60 | 0.3583 | 0.3806 | -0.0222 | 11/39/10 | 0.4889 | 0.6306 | -0.1417 | 8/33/19 |
| overall | rrf_equal_cost_hybrid | 60 | 0.3583 | 0.3222 | 0.0361 | 13/35/12 | 0.4889 | 0.5792 | -0.0903 | 11/30/19 |
| code2test | lexical | 20 | 0.5000 | 0.2167 | 0.2833 | 7/12/1 | 0.6417 | 0.3167 | 0.3250 | 8/12/0 |
| code2test | bm25 | 20 | 0.5000 | 0.0917 | 0.4083 | 9/10/1 | 0.6417 | 0.2583 | 0.3833 | 9/9/2 |
| code2test | repomap | 20 | 0.5000 | 0.3500 | 0.1500 | 6/12/2 | 0.6417 | 0.5250 | 0.1167 | 6/12/2 |
| code2test | rrf_equal_cost_hybrid | 20 | 0.5000 | 0.2917 | 0.2083 | 6/12/2 | 0.6417 | 0.3583 | 0.2833 | 7/12/1 |
| edit2ripple | lexical | 20 | 0.2500 | 0.3667 | -0.1167 | 3/12/5 | 0.4250 | 0.5250 | -0.1000 | 4/10/6 |
| edit2ripple | bm25 | 20 | 0.2500 | 0.1792 | 0.0708 | 7/10/3 | 0.4250 | 0.4542 | -0.0292 | 5/12/3 |
| edit2ripple | repomap | 20 | 0.2500 | 0.2667 | -0.0167 | 3/15/2 | 0.4250 | 0.5917 | -0.1667 | 1/13/6 |
| edit2ripple | rrf_equal_cost_hybrid | 20 | 0.2500 | 0.3500 | -0.1000 | 2/14/4 | 0.4250 | 0.6292 | -0.2042 | 1/12/7 |
| trace2code | lexical | 20 | 0.3250 | 0.3750 | -0.0500 | 6/7/7 | 0.4000 | 0.6750 | -0.2750 | 4/5/11 |
| trace2code | bm25 | 20 | 0.3250 | 0.2000 | 0.1250 | 6/10/4 | 0.4000 | 0.4750 | -0.0750 | 6/4/10 |
| trace2code | repomap | 20 | 0.3250 | 0.5250 | -0.2000 | 2/12/6 | 0.4000 | 0.7750 | -0.3750 | 1/8/11 |
| trace2code | rrf_equal_cost_hybrid | 20 | 0.3250 | 0.3250 | 0.0000 | 5/9/6 | 0.4000 | 0.7500 | -0.3500 | 3/6/11 |

## Query-only score versus oracle ceiling

| Scope | N | Query BCY | Oracle BCY | Oracle-query gap | Query recall | Oracle recall | Gap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| overall | 60 | 0.3583 | 0.3750 | 0.0167 | 0.4889 | 0.5056 | 0.0167 |
| code2test | 20 | 0.5000 | 0.5000 | 0.0000 | 0.6417 | 0.6917 | 0.0500 |
| edit2ripple | 20 | 0.2500 | 0.2500 | 0.0000 | 0.4250 | 0.4250 | 0.0000 |
| trace2code | 20 | 0.3250 | 0.3750 | 0.0500 | 0.4000 | 0.4000 | 0.0000 |

## Decisions and outside-union retrieval

| Scope | PROGRAM | ABSTAIN | Scoped UNSAT | Escape tasks | Useful escape tasks | Conditional useful | Outside files | Outside gold | Micro precision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| overall | 54 | 6 | 0 | 54 | 6 | 0.1111 | 727 | 7 | 0.0096 |
| code2test | 20 | 0 | 0 | 20 | 4 | 0.2000 | 317 | 4 | 0.0126 |
| edit2ripple | 20 | 0 | 0 | 20 | 1 | 0.0500 | 192 | 1 | 0.0052 |
| trace2code | 14 | 6 | 0 | 14 | 1 | 0.0714 | 218 | 2 | 0.0092 |

Outside usefulness is retrieval-level post-hoc gold overlap. The current schema cannot attribute canonical packed-BCY gains to individual outside files.

## Completeness

| Check | Overall pass | code2test | edit2ripple | trace2code |
| --- | ---: | ---: | ---: | ---: |
| any_identifier | 59/60 | 20/20 | 20/20 | 19/20 |
| all_anchors_have_identifier | 58/60 | 19/20 | 20/20 | 19/20 |
| refinement_frontier_exhausted | 59/60 | 20/20 | 20/20 | 19/20 |
| refinement_program_storage_complete | 59/60 | 20/20 | 20/20 | 19/20 |
| coarse_frontier_exhausted | 58/60 | 19/20 | 20/20 | 19/20 |
| coarse_program_storage_complete | 59/60 | 20/20 | 20/20 | 19/20 |
| full_scan_complete | 59/60 | 20/20 | 20/20 | 19/20 |
| selected_paths_complete | 40/60 | 16/20 | 20/20 | 4/20 |
| query_anchor_catalog_not_truncated | 59/60 | 20/20 | 20/20 | 19/20 |
| bind_postings_not_truncated | 59/60 | 19/20 | 20/20 | 20/20 |
| relation_postings_not_truncated | 41/60 | 13/20 | 11/20 | 17/20 |
| canonical_file_texts_complete | 60/60 | 20/20 | 20/20 | 20/20 |
| baseline_ranked_texts_complete | 60/60 | 20/20 | 20/20 | 20/20 |

## I/O, search work, and depth

- Three-pass rows scanned: 5178873
- Three-pass bytes read: 4429300668 (scan traffic, not index size)
- Sum of per-task scan wall time: 142.0495 seconds
- Median/p95/max per-task scan wall: 1.0273 / 12.2152 / 17.4416 seconds
- Refinement candidates attempted/operator calls: 120 / 298
- Refinement nominal cost units: 360.0000; these are not physical equal-compute charges
- Declared operator depths: `{"2": 19, "3": 40, "None": 1}`
- Declared retrieval-transition depths: `{"2": 59, "None": 1}`
- Selected operator depths: `{"2": 14, "3": 40}`
- Selected retrieval-transition depths: `{"2": 54}`
- Certificate counts as a retrieval transition: no
- Strict depth necessity: not established

## Claim guard

This development report does not include a strong semantic baseline, selective no-gold evaluation, adversarial rewiring/entity tests, or an untouched confirmatory set. It cannot support MECHANISM-PROCEED, statistical-superiority, causal-theory, semantic-relation, or strict-depth claims.

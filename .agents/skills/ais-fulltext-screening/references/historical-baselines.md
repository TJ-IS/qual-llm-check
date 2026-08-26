# Existing baselines

Consult `docs/research_program/current_state.md` and the run's own prompt, config, summary, and audit before reuse.

## Public-data/objective-metric run

Path: `runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/`

The user confirmed the prompt and scope before a 2,475/2,475 run. The output contains 51 included items. This is a positive example of scope confirmation, complete execution accounting, and separate public-data gating. It is not an all-security corpus.

## Security algorithm-development run

Path: `runs/ais_basket_security_algorithm_development_flash_v2/`

The 99-paper output answers the narrower algorithm/method-development question. Preserve its prompt and analysis; do not compare its count directly with broad security relevance as if one were an error subset of the other.

## Broad security-relevance run

Path: `runs/ais_basket_security_relevance_fulltext_flash_v1/`

The run reconciled 13,909 full texts with no model-call failures and produced 388 security-relevant items, with M1/F2/F3 retrieval audits. Corpus inspection found 36 mismatched/damaged full texts plus boundary cases. Therefore 388 is a **provisional** standard pending repair and recorded reclassification.

## Reconciled 133-item audit trail

Path: `runs/ais_basket_final_audit_133_flash/`

The curated trail has a scientific denominator of 133 unique items: 52 included and 81 excluded. One raw reviewer stream contains 141 records because eight IDs repeat. Preserve the 141 records as attempt history; do not use them as the denominator or describe them as 141 independently audited papers. Reuse this set only for its frozen objective-measurement, improvement, and implemented-artifact boundary.

## Earlier 315-item audit

The earlier candidate set exposed subjective labels, ordinary comparisons presented as benchmarks, and theory/empirical papers presented as algorithm development. Retain its spot-check categories as adversarial audit strata. Do not call 315 a gold standard.

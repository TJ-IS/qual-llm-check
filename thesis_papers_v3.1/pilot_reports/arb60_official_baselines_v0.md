# ARB frozen-baseline descriptive summary

> This report is descriptive validation and aggregation only. It does not establish causality, statistical superiority, or a new-algorithm win.
> The legacy `gold_coverage@8k` and `context_efficiency@8k` source fields use 8,000-character packing. They are not canonical token-packed BCY; canonical BCY requires the official token-based reporting path.

- Validated releases: v2_code2test, v2_edit2ripple, v2_trace2code
- Methods: lexical, bm25, repomap
- Tracked manifest SHA256: `885cf615e7e5bd6d713c2aefe1b5792da5915ac3f17d545acab6673b0f0f009c`
- Canonical release/sample-ID list SHA256: `00b203f6e3520467ed987db247aad96268b87a46499640e9447bd1b3ea174b8f`

## Release-level official metrics

| Release | Method | N | MRR | Recall@20 | F0.5@10 | Coverage AUC@20 | Legacy gold-file fraction@8K chars | Legacy context efficiency@8K chars | Pollution tokens@8K |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| v2_code2test | lexical | 20 | 0.0741 | 0.3167 | 0.0244 | 0.2083 | 0.0500 | 0.0104 | 6847.2 |
| v2_code2test | bm25 | 20 | 0.0790 | 0.2583 | 0.0238 | 0.1471 | 0.0917 | 0.0104 | 6787.3 |
| v2_code2test | repomap | 20 | 0.1701 | 0.5250 | 0.0427 | 0.3500 | 0.0500 | 0.0500 | 4387.6 |
| v2_edit2ripple | lexical | 20 | 0.2409 | 0.5250 | 0.1122 | 0.4235 | 0.0833 | 0.0372 | 6458.1 |
| v2_edit2ripple | bm25 | 20 | 0.1354 | 0.4542 | 0.0647 | 0.2565 | 0.0333 | 0.0336 | 6190.9 |
| v2_edit2ripple | repomap | 20 | 0.2035 | 0.5917 | 0.1004 | 0.4106 | 0.0000 | 0.0000 | 7061.8 |
| v2_trace2code | lexical | 20 | 0.2023 | 0.6750 | 0.0666 | 0.4612 | 0.1500 | 0.0577 | 5981.4 |
| v2_trace2code | bm25 | 20 | 0.1227 | 0.4750 | 0.0363 | 0.3187 | 0.1000 | 0.0244 | 5481.1 |
| v2_trace2code | repomap | 20 | 0.2796 | 0.7750 | 0.0906 | 0.5513 | 0.0750 | 0.1000 | 5579.5 |

## Unweighted release macro

| Method | MRR | Recall@20 | F0.5@10 | Coverage AUC@20 | Legacy gold-file fraction@8K chars | Legacy context efficiency@8K chars | Pollution tokens@8K |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| lexical | 0.1724 | 0.5056 | 0.0677 | 0.3644 | 0.0944 | 0.0351 | 6428.9 |
| bm25 | 0.1124 | 0.3958 | 0.0416 | 0.2408 | 0.0750 | 0.0228 | 6153.1 |
| repomap | 0.2177 | 0.6306 | 0.0779 | 0.4373 | 0.0417 | 0.0500 | 5676.3 |

## Descriptive legacy 8K-character packing patterns

`No all-gold` means no method packed every gold file under the legacy 8,000-character rule; `all zero` means every method had a zero legacy gold-file fraction. `Mixed` records differing all-gold-file events and is neither canonical BCY nor a causal complementarity estimate.

| Scope | Tasks | Any all-gold | All methods all-gold | No all-gold | All zero | Mixed |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| v2_code2test | 20 | 2 | 0 | 18 | 16 | 2 |
| v2_edit2ripple | 20 | 1 | 0 | 19 | 18 | 1 |
| v2_trace2code | 20 | 4 | 0 | 16 | 15 | 4 |
| macro | 60 | 7 | 0 | 53 | 49 | 7 |

## Descriptive unbounded top-20 union diagnostic

The top-20 union is an intentionally generous descriptive diagnostic: it can contain up to 60 files, is not equal-cost, is not a sequential program, and does not establish complementarity or causal value.

| Scope | Tasks | All three miss | Union strictly adds gold | Any single covers all gold | Union covers all gold | Mean best-single fraction | Mean union fraction |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| v2_code2test | 20 | 6 | 0 | 11 | 11 | 0.6333 | 0.6333 |
| v2_edit2ripple | 20 | 3 | 2 | 9 | 10 | 0.6500 | 0.6875 |
| v2_trace2code | 20 | 2 | 0 | 14 | 14 | 0.8000 | 0.8000 |
| macro | 60 | 11 | 2 | 34 | 35 | 0.6944 | 0.7069 |

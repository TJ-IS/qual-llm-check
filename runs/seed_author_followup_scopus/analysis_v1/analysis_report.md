# Follow-up publications of the 20 seed papers' authors

## Scope and matching rule

- The Scopus author-follow-up export contains **1,209 records** linked to 36 seed-paper authors, after each author's latest seed-paper year.
- Seed-citation continuity is determined from the **previously retrieved 807-record Scopus `REFEID` union**, not from the export's non-standard `References` text.
- **48 follow-up records** intersect that union: 47 by exact EID and 1 by DOI fallback.
- This establishes that each of the 48 records cites **at least one** seed. It does not determine which seed because the earlier union result did not preserve seed-to-citing-paper edges.

## Screening result

DeepSeek v4 Flash produced usable decisions for 1,198 records. Eleven records (ten persistent failures plus one malformed JSON line) were manually coded with the identical decision schema. Counts are Scopus records; normalized-title checking found 25 repeated-title clusters containing 70 records, so conference/journal or duplicate-index variants may represent the same intellectual work.

| Trajectory | Records | Confirmed seed citers | Within-label citation rate |
|---|---:|---:|---:|
| `direct_human_ai_programming` | 1 | 0 | 0.0% |
| `direct_human_programming` | 41 | 18 | 43.9% |
| `programming_artifact_or_method` | 25 | 0 | 0.0% |
| `software_development_process_or_team` | 85 | 2 | 2.35% |
| `information_systems_or_technology_adjacent` | 922 | 27 | 2.93% |
| `unrelated_or_unclear` | 135 | 1 | 0.74% |

Strict human-programming continuity comprises **42 records** (3.5%); **18** of those are confirmed seed citers. The broader software lineage (adding software artifacts/methods and development process/team studies) comprises **152 records** (12.6%).

## Interpretation

The authors did not stop publishing. Instead, the dominant pattern is topic migration: most later work concerns general IS/technology phenomena, conceptual modeling, HCI, auditing, platforms, organizations, and other adjacent areas. A small but visible line continued through spreadsheet errors/testing, SQL and database-query learning, program or schema comprehension, software-component development, and software-design cognition.

Direct bibliographic continuity and topical continuity are different. The 48 confirmed citers show that the old papers continued to be referenced, but only 18 are also in the strict human-programming class. Conversely, many topically relevant later papers do not cite a seed. This helps explain the apparent break in the AIS lineage: citation inheritance is sparse, while the phenomenon diffused into different labels, venues, methods, and neighboring research communities.

For modern AI-assisted programming, only **Teaching SQL Using ChatGPT** meets the strict code/query-operation rule in this author-follow-up set. **How Gen AI Is Reshaping Software Design Work** is substantively important under a broader software-development definition, but its abstract studies UX/UI and software-design roles and workflows rather than concrete code writing, comprehension, debugging, testing, or review; it is therefore retained as broader adjacent continuity, not strict AI-assisted programming. Neither record is in the prior 807-record seed-citing union.

## Authors with the most strict-continuity records

| Author | All follow-up | Strict human programming | Broader software lineage | Confirmed seed citers |
|---|---:|---:|---:|---:|
| Panko, Raymond R. | 25 | 13 | 14 | 5 |
| Allen, Gove N. | 14 | 5 | 6 | 1 |
| Borthick, A.Faye | 14 | 4 | 4 | 1 |
| Casterella, Gretchen Irwin | 5 | 3 | 3 | 2 |
| Balijepally, VenuGopal | 22 | 2 | 11 | 4 |
| Morrison, Joline | 4 | 2 | 2 | 0 |
| Palvia, Prashant | 197 | 1 | 28 | 1 |
| Purao, Sandeep | 97 | 1 | 23 | 0 |
| Storey, Veda C. | 162 | 1 | 12 | 3 |
| Parsons, Jeffrey | 97 | 1 | 8 | 8 |
| Vessey, Iris | 16 | 1 | 4 | 6 |
| Kim, Hee Woong | 90 | 1 | 3 | 1 |
| Kim, Jinwoo | 98 | 1 | 3 | 1 |
| Vijayasarathy, Leo | 6 | 1 | 3 | 1 |
| Goswami, Supama | 22 | 1 | 2 | 1 |

## Most recent strict-continuity records

- 2015 — Using transaction-level data to diagnose knowledge gaps and misconceptions (Allen, Gove N.)
- 2016 — Querying instances - A protocol analysis study (Parsons, Jeffrey)
- 2016 — Teaching introductory computer programming using excel VBA (Allen, Gove N.)
- 2016 — Understanding the role of IS and application domain knowledge on conceptual schema problem solving: A verbal protocol study (Vessey, Iris)
- 2016 — Workshop title: An automated, real-time learning environment for teaching SQL and database management (Allen, Gove N.)
- 2017 — Analyzing data for decision making: Integrating spreadsheet modeling and database querying (Borthick, A.Faye)
- 2017 — Setting the Pace: Experiments with Keller's PSI (Purao, Sandeep)
- 2017 — Transaction-level learning analytics in online authentic assessments (Allen, Gove N.)
- 2019 — Query structure and data model mapping errors in information retrieval tasks (Casterella, Gretchen Irwin; Vijayasarathy, Leo)
- 2021 — A Problem-Solving-Based Teaching Approach to Database Design (Bhadauria, Vikram S.)
- 2021 — Preparing for audit data analytics with the aicpa general ledger audit data standards (Casterella, Gretchen Irwin)
- 2023 — A mental model approach to teaching database querying skills with SQL and Alteryx (Casterella, Gretchen Irwin)
- 2023 — Getting Students Ready for Accounting Spreadsheets: Training for Basic Spreadsheet Skills with Pre/Post Assessments (Borthick, A.Faye)
- 2023 — Teaching SQL Using ChatGPT (Storey, Veda C.)
- 2024 — Developing Business Process and Query Skills for Solving Business Problems (Borthick, A.Faye)

## Files

- `screening_joined.csv`: all 1,209 records with author, citation-union, and screening fields.
- `confirmed_seed_citers_with_screening.csv`: the 48 records confirmed through the prior `REFEID` union.
- `strict_human_programming_candidates.csv`: the strict direct-human and direct-human-AI set.
- `broader_software_lineage_candidates.csv`: strict set plus artifacts/methods and development process/team.
- `author_trajectory_summary.csv`: author-level cross-tabulation.
- `trajectory_by_decade.csv`: decade-level cross-tabulation.
- `manual_review_queue.csv`: broader candidates, low-certainty records, and AI-context records for audit.

## Limits

This is a title/abstract/keyword screen, not full-text inclusion. A final systematic review should manually adjudicate the strict and broader candidate files, collapse duplicate intellectual works, and retrieve seed-specific citation edges if the exact seed cited by each follow-up paper matters.

# Complete Basket Metadata Comparison: Manual Audit

## Scope

- Complete Scopus Basket metadata table: 17,745 records.
- High-recall programming query: 293 records.
- Previously confirmed core: 20 records.
- Records with no prior full-text-screening decision: 31 records.
- These 31 records were screened independently with `deepseek-v4-pro` using title, abstract, and keywords.
- Model run: 31 completed, 0 failed; 65,362 total tokens.

`no prior full-text-screening decision` is the precise status. It does not necessarily mean that no PDF/full text exists.

## Model output

- Irreplaceable direct programming = true: 7
- False: 23
- Unresolved because no abstract: 1

The model's boolean is deliberately broader than the human-programming seed criterion. The screening label and manual audit must therefore be used together.

## Manual calibration of the eight flagged records

| Year | Title | Manual status | Treatment |
|---:|---|---|---|
| 1981 | Computer Program Testing | Unresolved; no abstract | Retrieve full text before classification |
| 1997 | Journeys up the mountain: Different paths to learning object-oriented programming | Strong direct human-programming study | Add to the candidate foundational benchmark; confirm with full text |
| 2001 | Quality metrics for intranet applications | Programming artifact/metric only | Do not add to the human-programming seed set |
| 2002 | Code quality analysis in open source software development | Code-artifact analysis only | Do not add to the human-programming seed set |
| 2005 | Optimal software development: A control theoretic approach | Programming-specific mathematical method; no observed human task | Do not add to the human-programming seed set |
| 2007 | Understanding mindshift learning: The transition to object-oriented development | Boundary case; abstract frames OO as an exemplar of a general learning theory | Full-text adjudication; do not add automatically |
| 2023 | Leveraging Low Code Development of Smart Personal Assistants: An Integrated Design Approach with the SPADE Method | Strong direct end-user/low-code programming study | Add to the candidate expanded benchmark; confirm with full text |
| 2026 | The impact of generative artificial intelligence on software development performance: a study based on the theory of technology dominance | Direct modern AI-assisted software-development study, but survey-based and not necessarily agentic coding | Add to a separate modern AI-assisted-programming pool; do not automatically merge into the traditional task-based 20 |

## Corrected interpretation

The original 20 should be described as **20 full-text-confirmed seed records from the earlier screening pipeline**, not as an exhaustive set derived from all 17,745 Basket metadata records.

Provisional accounting after the complete-metadata comparison:

- 20 original full-text-confirmed seeds.
- 2 strong direct human/end-user-programming metadata discoveries (1997 and 2023), pending full-text confirmation.
- 1 human-programming boundary case (2007), pending full-text adjudication.
- 1 unresolved record with no abstract (1981), pending full text.
- 1 modern AI-assisted-programming bridge record (2026), best maintained as a separate modern track until the review's agentic/task criteria are applied to the full text.

The 2023 and 2026 records mean that the Basket literature is not literally absent after the old seed period. The more defensible claim is that direct individual-level programming work became sparse and changed form, with a recent reconnection through low-code/end-user development and AI-assisted software development.

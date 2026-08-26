# Durable requirement registry

This is the public, repository-safe index of durable user requirements. It contains normalized controls and historical atom IDs, but no private task quotations or message payloads. Exact minimal excerpts and message provenance remain in ignored local audit artifacts.

The detailed rule lives at the `Authoritative clause` pointer. This registry owns traceability and supersession, not duplicate wording. Update the rule and this index in the same bounded checkpoint.

## Status vocabulary

- `active` — current behavior required by a skill or canonical reference.
- `qualified` — active only within the stated boundary.
- `run_specific` — retained in a frozen run prompt or decision record, not promoted to a universal rule.
- `superseded` — replaced by a later requirement; the current control is named.
- `open` — no operative rule yet; blocks a claim of complete integration.
- `conflict` — two operative readings materially disagree; present both to the user and obtain confirmation before applying either as final.

## Current controls

| Control ID | Domain | Normalized requirement | Authoritative clause | Consumer | Load | Status |
|---|---|---|---|---|---|---|
| `M-SCOPE-01` | Manuscript | Define safety from protected outcomes, risk-bearing actions, actors, observable information, controls, and failure consequences; use a traditional threat model only when attacker relations are actually part of the study. | `.agents/skills/coding-agent-manuscript/references/acceptance-gates.md` — `A. Scope and topic viability` | `coding-agent-manuscript` | every checkpoint | active |
| `M-SERIES-01` | Manuscript | Keep the three papers one coherent safety series while preserving distinct questions, information times, artifacts, training/evaluation responsibilities, and contributions. | `.agents/skills/coding-agent-manuscript/references/acceptance-gates.md` — `A. Scope and topic viability` | `coding-agent-manuscript` | every checkpoint | active |
| `M-VIABILITY-01` | Manuscript | Inspect nearest neighbors, contribution size, data access, implementation burden, and evaluability before prose expansion; redesign or replace a weak topic. | `.agents/skills/coding-agent-manuscript/references/acceptance-gates.md` — `A. Scope and topic viability` | `coding-agent-manuscript` | every checkpoint | active |
| `M-ARTIFACT-01` | Manuscript | The main artifact must add substantive trainable or computational capability using real data and executable processing; prompt-only, static-rule, or simple-score variants are supporting baselines unless they are the explicit research object. | `.agents/skills/coding-agent-manuscript/references/acceptance-gates.md` — `D. Theory and substantive artifact` | `coding-agent-manuscript` | every checkpoint | active |
| `M-THEORY-01` | Manuscript | Compare plausible theories/problem knowledge, retain only constructs with distinct work, and map each retained mechanism into a computational or evaluation responsibility, component, independent observable, main test, and rejection outcome. | `.agents/skills/coding-agent-manuscript/references/acceptance-gates.md` — `D. Theory and substantive artifact` | `coding-agent-manuscript` | every checkpoint | active |
| `M-SOURCE-01` | Manuscript | Compare directly with the complete authoritative carrying section and, when context permits, its preceding and following major sections; sentence checks remain subordinate to whole-section logic. | `.agents/skills/coding-agent-manuscript/references/major-section-workflow.md` — `2. Read before compressing`; `5. Re-read at three scales` | `coding-agent-manuscript` | every checkpoint | active |
| `M-TEMPLATE-01` | Manuscript | Separate the ACAA/DSDL series baseline from local algorithm/security comparators; use current writing paradigms while retaining classical theory with later development, and record template conflicts and selection reasons. | `.agents/skills/coding-agent-manuscript/references/source-routing.md` — `Authoritative writing comparison` | `coding-agent-manuscript` | every writing checkpoint | active |
| `M-EVIDENCE-01` | Manuscript | Verify consequential claims in original text and bibliography, assign non-duplicative citation roles, trace old sources forward and backward, and bound adjacent applicability. | `.agents/skills/coding-agent-manuscript/references/evidence-and-citations.md` — `Verify at claim level`; `Build networks, not isolated lists` | `coding-agent-manuscript` | every checkpoint | active |
| `M-PROTOCOL-01` | Manuscript | Separate source facts, author synthesis, writing prototypes, and author-designed protocols; state the responsibility, evidence status, and limits of each class. | `.agents/skills/coding-agent-manuscript/references/evidence-and-citations.md` — `Writing prototypes and author responsibility` | `coding-agent-manuscript` | every writing checkpoint | active |
| `M-ANCHOR-01` | Manuscript | Before section acceptance, verify an authoritative IS writing prototype for every reader-visible natural-language sentence. Match rhetorical function, construction, citation responsibility, local logic, paragraph position, and punctuation function rather than identical content or wording; author-designed methods and expectations may use a looser functionally analogous disclosure prototype but may not omit one. | `.agents/skills/coding-agent-manuscript/references/evidence-and-citations.md` — `Writing prototypes and author responsibility`; `.agents/skills/coding-agent-manuscript/references/writing-prototype-search.md` — `Iterative verification cycle` | `coding-agent-manuscript` | every writing checkpoint | qualified |
| `M-ARGUMENT-01` | Manuscript | Build one reader-level question, a cumulative paragraph chain, meaningful headings, adequate argumentative mass, and explicit section handoffs before sentence polishing. | `.agents/skills/coding-agent-manuscript/references/major-section-workflow.md` — `3. Build our argument spine` | `coding-agent-manuscript` | every writing checkpoint | active |
| `M-PROSE-01` | Manuscript | Keep visible prose on a positive scholarly chain, move internal audit language to ledgers, and use natural formal prose whose paragraph links and rhetorical functions remain explicit. | `.agents/skills/coding-agent-manuscript/references/acceptance-gates.md` — `F. Feasibility, stage, and integrity`; `G. Readability and source-guided writing` | `coding-agent-manuscript` | every writing checkpoint | active |
| `M-PUNCT-01` | Manuscript | The earlier independent punctuation-zero gate is superseded by `M-ANCHOR-01` and `M-PROSE-01`: inspect punctuation as one function of the verified sentence prototype and paragraph logic; counts only locate risk and cannot independently pass or fail prose. | `.agents/skills/coding-agent-manuscript/references/acceptance-gates.md` — `G. Readability and source-guided writing` | `coding-agent-manuscript` | every writing checkpoint | superseded |
| `M-BENCH-01` | Manuscript | Name a benchmark only when the resource and comparison design justify that role; organize comparisons by the competing explanation they exclude. | `.agents/skills/coding-agent-manuscript/references/acceptance-gates.md` — `E. Benchmark and evaluation` | `coding-agent-manuscript` | when benchmark/evaluation is in scope | active |
| `M-FEAS-01` | Manuscript | Match audit scope to the current writing stage, expose implementation dependencies early, and distinguish verified fact, design claim, planned test, expected diagnostic, and observed result. | `.agents/skills/coding-agent-manuscript/references/acceptance-gates.md` — `F. Feasibility, stage, and integrity` | `coding-agent-manuscript` | every checkpoint | active |
| `M-LEDGER-01` | Manuscript | Persist sources read, citation relationships, writing insights, feasibility, rejected uses, and changed claims in the one canonical owner for each responsibility. | `.agents/skills/coding-agent-manuscript/references/source-routing.md` — `Source and ledger routing`; canonical ledgers 163–175 | `coding-agent-manuscript` | every checkpoint | active |
| `M-DELEGATE-01` | Manuscript | Give sub-agents frozen non-overlapping packages containing requirement IDs, exact ledger/source sections, exclusions, and evidence-level return fields; the primary agent reopens decisive originals. | `.agents/skills/coding-agent-manuscript/references/delegation.md` — `Send a frozen package`; canonical ledger 171 | `coding-agent-manuscript` | when delegating | active |
| `M-INTEGRATE-01` | Manuscript | After bounded major sections exist, run an end-to-end manuscript integration gate for narrative, proportions, repetition, terminology, theory-artifact-evaluation identity, citations, and cross-paper boundaries. | `.agents/skills/coding-agent-manuscript/references/whole-manuscript-integration.md` — `End-to-end gates` | `coding-agent-manuscript` | final integration checkpoint | active |
| `M-HISTORY-01` | Manuscript | Repository checkpoints and user acceptance outrank Goal state, filenames, mapping coverage, citation counts, and automated PASS signals. | `.agents/skills/coding-agent-manuscript/references/historical-lessons.md`; `.agents/skills/research-project-continuity/SKILL.md` — `Acceptance` | `coding-agent-manuscript`, `research-project-continuity` | resume/version/acceptance work | active |
| `S-QUESTION-01` | Screening | Keep broad security relevance, security algorithm development, objective metric/benchmark, public-data eligibility, and other constructs as separate frozen decisions. | `.agents/skills/ais-fulltext-screening/SKILL.md` — `Route the decision first` | `ais-fulltext-screening` | every run | active |
| `S-SEARCH-01` | Screening | For systematic retrieval, justify databases, fields, concept blocks, terms, and syntax by directly inspecting authoritative SLR method sections; pilot retrieval before screening. | `.agents/skills/ais-fulltext-screening/references/scope-and-run.md` — `2. Design and justify retrieval` | `ais-fulltext-screening` | systematic retrieval | active |
| `S-CONFIRM-01` | Screening | Show and obtain approval for prompt, scope, interpretation, model, concurrency, schema, retry/resume, and gates before an expensive run. | `.agents/skills/ais-fulltext-screening/references/scope-and-run.md` — `3. Obtain confirmation` | `ais-fulltext-screening` | every expensive run | active |
| `S-CORPUS-01` | Screening | Reconcile title, metadata, DOI, and local full text; report unavailable or mismatched items separately from model execution. | `.agents/skills/ais-fulltext-screening/SKILL.md` — `Corpus integrity` | `ais-fulltext-screening` | every run | active |
| `S-PUBLIC-01` | Screening | Treat data as public when the relevant unit is reproducibly obtainable through an open route, including a generally available registration or license application; case-specific internal permission is not public access. | `.agents/skills/ais-fulltext-screening/references/evidence-gates.md` — `Public-data eligibility` | `ais-fulltext-screening` | public-data gate | qualified |
| `S-EVIDENCE-01` | Screening | Retain decisive full-text evidence for inclusions and the strongest near-qualifying evidence for audited exclusions. | `.agents/skills/ais-fulltext-screening/references/evidence-gates.md` — `Evidence strength` | `ais-fulltext-screening` | every full-text run | active |
| `S-AUDIT-01` | Screening | Distinguish exploratory, screened, provisional, and accepted sets; corpus integrity, decision reliability, recall/precision, and unresolved cases govern adoption. | `.agents/skills/ais-fulltext-screening/references/evidence-gates.md` — `Standards` | `ais-fulltext-screening`, `coding-agent-manuscript` | run closure and manuscript adoption | active |
| `C-STATE-01` | Continuity | Use current repository artifacts, explicit statuses, and one canonical owner per responsibility as durable state. | `.agents/skills/research-project-continuity/SKILL.md` — `Resume safely` | `research-project-continuity` | every continuity task | active |
| `C-REQ-01` | Continuity | Maintain a public normalized registry and an ignored minimal-excerpt provenance audit; every new user correction receives a disposition and supersession relation. | `.agents/skills/research-project-continuity/references/requirement-traceability.md` — `Update sequence` | `coding-agent-manuscript`, `ais-fulltext-screening`, `research-project-continuity` | durable correction or skill revision | active |
| `C-CONFLICT-01` | Continuity | When operative requirements materially conflict, present both readings, affected scope, and a proposed resolution to the user; do not silently select or close the conflict before confirmation. | `.agents/skills/research-project-continuity/references/requirement-traceability.md` — `Conflict adjudication` | `coding-agent-manuscript`, `ais-fulltext-screening`, `research-project-continuity` | whenever contrary rules are found | active |
| `C-PRIVACY-01` | Continuity | Publish normalized controls and safe provenance summaries, not raw private transcripts, credentials, or unlicensed material. | `.agents/skills/research-project-continuity/SKILL.md` — `Prepare publication` | `research-project-continuity` | curation/publication work | active |
| `C-PORTABLE-01` | Continuity | Keep committed skills, scripts, manifests, and public instructions runnable from a clean Windows or macOS clone through repository-relative case-exact paths, UTF-8/LF text, an explicit Python 3.10+ interpreter choice, and target-OS smoke tests; static checks must not be reported as a macOS run. | `.agents/skills/research-project-continuity/references/github-publication.md` — `Cross-platform continuation` | `coding-agent-manuscript`, `ais-fulltext-screening`, `research-project-continuity` | skill/script revision or cross-platform handoff | active |

## Historical atom disposition

The baseline consists of exactly 58 atoms: `H01–H20`, `L01–L33`, and `A01–A05`. Baseline verdicts preserve what the pre-revision audit found: `core_direct`, `routed_ledger`, `partial`, `missing`, `superseded`, or `qualified_conflict`. `Current disposition` is the post-revision state and must never overwrite the baseline. `run_specific` means the historical instruction remains available in its frozen run rather than becoming a universal skill rule.

| Atom | 2026-08-26 baseline verdict | Current control(s) | Current disposition | Scope | Replacement/qualification edge | Last verified | Current interpretation |
|---|---|---|---|---|---|---|---|
| `H01` | partial | `M-SCOPE-01`, `M-THEORY-01` | active | universal | — | 2026-08-26 | Distinctiveness requires a consequential contextual mismatch, not a renamed setting. |
| `H02` | partial | `M-THEORY-01`, `M-EVIDENCE-01` | qualified | paper_specific | qualified by construct-development scope | 2026-08-26 | Original definition and measurement are mandatory; a single individual-level predecessor is specific to construct-development work. |
| `H03` | routed_ledger | `M-PROSE-01`, `M-ARGUMENT-01` | active | universal | — | 2026-08-26 | Positive necessity precedes boundary defense. |
| `H04` | core_direct | `C-STATE-01`, `M-LEDGER-01` | active | universal | — | 2026-08-26 | Stable paths, ordered artifacts, and persisted originals support recovery. |
| `H05` | partial | `M-THEORY-01`, `M-EVIDENCE-01` | active | universal | — | 2026-08-26 | Candidate theories receive explicit comparison and original-text adjudication. |
| `H06` | partial | `S-EVIDENCE-01` | run_specific | run_specific | retained in frozen construct screen | 2026-08-26 | Explicit construct centrality belongs to that frozen screening question. |
| `H07` | core_direct | `S-CONFIRM-01` | qualified | run_specific | qualified by verified segmentation rule | 2026-08-26 | Approval and schema freezing remain; segmentation follows verified context limits rather than a universal no-chunk rule. |
| `H08` | partial | `S-QUESTION-01`, `S-EVIDENCE-01` | run_specific | run_specific | retained in frozen programming-context screen | 2026-08-26 | Programming-activity boundaries belong to that frozen classification. |
| `H09` | core_direct | `M-EVIDENCE-01` | active | universal | — | 2026-08-26 | Trace older sources to recent descendants and applications. |
| `H10` | missing | `S-SEARCH-01` | active | universal | implemented by systematic retrieval workflow | 2026-08-26 | Search fields and strings now require authoritative SLR-method justification. |
| `H11` | superseded | `M-SERIES-01` | superseded | universal | superseded by `M-SERIES-01` | 2026-08-26 | The series shares a safety progression, not necessarily one numeric outcome. |
| `H12` | superseded | `M-FEAS-01`, `M-ARTIFACT-01` | superseded | universal | superseded by `M-ARTIFACT-01` | 2026-08-26 | Early feasibility remains; current work may be algorithmic and is not restricted to individual UX. |
| `H13` | partial | `M-ARTIFACT-01`, `M-THEORY-01`, `S-QUESTION-01` | qualified | universal | qualified by broader problem/problem-knowledge rule | 2026-08-26 | Objective outcomes and theory-guided artifacts remain; psychological theory is not the only eligible knowledge base. |
| `H14` | core_direct | `S-CONFIRM-01` | active | run_specific | run values remain frozen per run | 2026-08-26 | Run configuration requires explicit approval. |
| `H15` | core_direct | `C-STATE-01`, `M-EVIDENCE-01` | active | universal | — | 2026-08-26 | Read actual prompts/artifacts and build bounded adjacency bridges. |
| `H16` | core_direct | `M-VIABILITY-01`, `M-ARGUMENT-01` | active | universal | — | 2026-08-26 | The series must be focused and implementable. |
| `H17` | core_direct | `M-VIABILITY-01`, `M-BENCH-01`, `M-EVIDENCE-01` | active | universal | — | 2026-08-26 | Runnable data/evaluation and citation networks are early gates. |
| `H18` | core_direct | `M-SOURCE-01`, `M-ARGUMENT-01` | active | universal | qualified by `L17`/`L25` comparison window | 2026-08-26 | Sentence logic is checked inside complete sections and paragraph chains. |
| `H19` | partial | `M-ARTIFACT-01` | active | universal | — | 2026-08-26 | Computational hardness is substantive capability, not mandatory LLM fine-tuning. |
| `H20` | core_direct | `M-THEORY-01`, `M-ARTIFACT-01` | active | universal | — | 2026-08-26 | Theory must generate a non-trivial, rejectable computational responsibility. |
| `L01` | partial | `M-SCOPE-01`, `S-QUESTION-01` | active | universal | — | 2026-08-26 | Safety is contextual and broader than narrow network attack labels. |
| `L02` | core_direct | `M-SERIES-01` | active | universal | — | 2026-08-26 | Each paper remains independently contributive. |
| `L03` | partial | `M-VIABILITY-01` | active | universal | — | 2026-08-26 | Weak or already-covered topics are redesigned or replaced. |
| `L04` | partial | `M-ARTIFACT-01` | active | universal | — | 2026-08-26 | Prompt-only, static-rule, and trivial-score contributions do not carry the main algorithm claim. |
| `L05` | core_direct | `M-THEORY-01` | active | universal | — | 2026-08-26 | Theory changes representation, constraint, objective, action, or evaluation responsibility. |
| `L06` | partial | `M-PROSE-01` | active | universal | — | 2026-08-26 | Internal feasibility and audit process stay out of the formal narrative. |
| `L07` | core_direct | `M-FEAS-01`, `M-PROTOCOL-01` | active | universal | — | 2026-08-26 | Planned work is not reported as completed evidence. |
| `L08` | core_direct | `M-SOURCE-01`, `M-ARGUMENT-01` | active | universal | qualified by `L17`/`L25` comparison window | 2026-08-26 | Direct original comparison includes citation, sentence, paragraph, and punctuation functions. |
| `L09` | partial | `M-TEMPLATE-01` | active | universal | — | 2026-08-26 | Template conflict and selection reasons are recorded. |
| `L10` | core_direct | `M-TEMPLATE-01` | active | universal | — | 2026-08-26 | ACAA/DSDL are the series structural baseline; matched algorithm/security papers complement by function. |
| `L11` | core_direct | `M-SERIES-01` | active | universal | — | 2026-08-26 | Post-action control complements rather than refutes pre-action work. |
| `L12` | partial | `M-TEMPLATE-01`, `M-EVIDENCE-01` | active | universal | implemented by two-recency-clock rule | 2026-08-26 | Classical theory is allowed; current writing paradigms and later theory development are separately checked. |
| `L13` | routed_ledger | `M-PROSE-01`, `M-ARGUMENT-01` | active | universal | — | 2026-08-26 | Concept overload and defensive prose are explicit gates. |
| `L14` | core_direct | `M-LEDGER-01`, `M-EVIDENCE-01` | active | universal | — | 2026-08-26 | New reading may change prose, theory, design, and feasibility in the same checkpoint. |
| `L15` | core_direct | `M-EVIDENCE-01` | active | universal | — | 2026-08-26 | Old theory is traced through verified later use and development. |
| `L16` | core_direct | `M-EVIDENCE-01` | active | universal | — | 2026-08-26 | Adjacent applicability requires a named bridge and prohibited upgrade. |
| `L17` | core_direct | `M-SOURCE-01` | active | universal | — | 2026-08-26 | Same-section comparison is minimum; adjacent major sections supply setup and payoff. |
| `L18` | core_direct | `M-LEDGER-01`, `M-DELEGATE-01` | active | universal | — | 2026-08-26 | General and paper-specific ledgers travel with agent packages. |
| `L19` | core_direct | `M-DELEGATE-01` | qualified | universal | qualified by bounded-duplication correction | 2026-08-26 | Primary-agent direct review is universal; duplicated agents are reserved for named high-risk decisions. |
| `L20` | core_direct | `M-ARGUMENT-01` | active | universal | — | 2026-08-26 | Sparse major sections trigger missing-argument diagnosis, not automatic word padding. |
| `L21` | core_direct | `M-HISTORY-01`, `C-STATE-01` | active | universal | — | 2026-08-26 | Bounded repository checkpoints replace open-ended writing Goals. |
| `L22` | routed_ledger | `M-LEDGER-01`, `C-REQ-01` | active | universal | — | 2026-08-26 | Writing standards and new transferable source insights are persisted. |
| `L23` | core_direct | `C-STATE-01`, `M-EVIDENCE-01` | active | universal | — | 2026-08-26 | One canonical file per responsibility; cited-by discovery is part of source networks. |
| `L24` | routed_ledger | `M-PUNCT-01`, `M-ANCHOR-01`, `M-PROSE-01`, `M-TEMPLATE-01` | superseded | universal | independent punctuation threshold superseded by prototype-function review under `M-ANCHOR-01` and `M-PROSE-01` | 2026-08-26 | Punctuation remains visible and consequential, but it is learned and judged inside the verified sentence/paragraph prototype rather than by a mechanical zero target. |
| `L25` | core_direct | `M-SOURCE-01` | active | universal | — | 2026-08-26 | Every completed major section returns to multiple functionally matched originals. |
| `L26` | qualified_conflict | `M-ANCHOR-01`, `M-SOURCE-01`, `M-PROTOCOL-01` | qualified | universal | clarified on 2026-08-26 as universal writing-prototype coverage with looser function matching for novel author protocols | 2026-08-26 | Every visible sentence learns from a verified authoritative IS writing prototype; identical content is unnecessary, and prototype fit remains separate from substantive evidence. |
| `L27` | routed_ledger | `M-FEAS-01` | active | universal | — | 2026-08-26 | Audit only the current writing stage as complete; future sections remain milestones. |
| `L28` | core_direct | `M-EVIDENCE-01`, `M-THEORY-01` | active | universal | — | 2026-08-26 | Citation diversity follows responsibility; constructs must map to design and test. |
| `L29` | partial | `M-ARGUMENT-01`, `M-TEMPLATE-01` | active | universal | — | 2026-08-26 | Heading density and section mass follow rhetorical function and current top-IS comparison. |
| `L30` | routed_ledger | `M-BENCH-01` | active | paper_specific | retained in Paper 1 ledger | 2026-08-26 | Benchmark naming and D_att responsibility are bounded in the paper-specific ledger. |
| `L31` | partial | `C-STATE-01`, `C-REQ-01`, `C-PRIVACY-01` | active | universal | — | 2026-08-26 | Skills, durable history, and publishable artifacts are curated without raw transcript exposure. |
| `L32` | missing | `C-REQ-01` | active | universal | implemented by traceability protocol | 2026-08-26 | Original-to-rule traceability now has an explicit maintenance protocol. |
| `L33` | partial | `M-INTEGRATE-01`, `M-ARGUMENT-01` | active | universal | implemented by whole-manuscript integration gate | 2026-08-26 | Section checkpoints culminate in a separate end-to-end manuscript integration gate. |
| `A01` | core_direct | `S-PUBLIC-01`, `S-CONFIRM-01` | active | run_specific | run values remain frozen per run | 2026-08-26 | Public-data and run-confirmation requirements are separate gates. |
| `A02` | core_direct | `S-QUESTION-01` | active | run_specific | retained for algorithm-development label | 2026-08-26 | Algorithm-development screening requires a substantive computational/method contribution. |
| `A03` | partial | `S-PUBLIC-01` | active | universal | clarified by public-application access categories | 2026-08-26 | Generally available registration or license application can qualify; private case-specific permission cannot. |
| `A04` | core_direct | `S-SEARCH-01`, `S-EVIDENCE-01` | active | universal | — | 2026-08-26 | Search precedes frozen full-text screening. |
| `A05` | core_direct | `S-QUESTION-01`, `S-AUDIT-01` | active | universal | — | 2026-08-26 | Broad security and algorithm-development labels remain distinct and can be compared after audit. |

## Post-baseline user corrections

These atoms were issued after the frozen 58-atom audit. They do not change the baseline denominator.

| Atom | Added | Current control(s) | Current disposition | Scope | Current interpretation |
|---|---|---|---|---|---|
| `P01` | 2026-08-26 | `C-CONFLICT-01` | active | universal | Material contradictions must be shown to the user with both readings, consequences, and a recommendation; user confirmation precedes final resolution. |
| `P02` | 2026-08-26 | `M-LEDGER-01`, `M-TEMPLATE-01` | active | universal | Keep the hash-frozen executable writing-prototype manifest separate from the broader accumulated human comparison and source-observation ledgers; the manifest is the unique executable-pool owner. |
| `P03` | 2026-08-26 | `C-PORTABLE-01` | active | universal | Prepare the repository and repo-local skills for continued execution from a clean macOS clone after the owner uploads it to Git. |

## Supersession chains

| Topic | Earlier atom | Later atom | Current control |
|---|---|---|---|
| Comparison unit | `H18`, `L08` | `L17`, `L25` | `M-SOURCE-01`: sentence checks inside complete section and adjacent-section context |
| Theory and age | early recent-source preference | `L12` | `M-TEMPLATE-01`: recent writing paradigms; classical theory plus later development |
| Sentence prototypes | early `L26` semantic-anchor implementation | 2026-08-26 writing-imitation clarification | `M-ANCHOR-01`: every visible sentence receives a verified writing prototype; method/protocol content may differ and use a looser function match; `M-PROTOCOL-01` separately governs evidence responsibility |
| Punctuation | zero-target rule derived under `L24` | 2026-08-26 prototype-function clarification | `M-PUNCT-01` is superseded as an independent gate; punctuation is reviewed under `M-ANCHOR-01` and `M-PROSE-01` |
| Independent agents | early `L19` duplication | later `L19` cost correction | `M-DELEGATE-01`: duplicate only a named high-risk decision |
| Series outcome | `H11` | later three-paper architecture | `M-SERIES-01`: common safety progression without one compulsory numeric outcome |
| Artifact type | `H12` | `H19`, `L04` | `M-ARTIFACT-01`: substantive algorithmic capability is eligible |

## Maintenance

Use `.agents/skills/research-project-continuity/references/requirement-traceability.md` whenever a user correction changes a durable rule, a skill is audited or revised, or a historical task is curated. A skill revision is not complete until every affected atom has one current disposition, all pointers resolve, and no `conflict` is falsely reported as resolved. Post-baseline atoms are validated separately from the frozen 58-atom denominator.

# Manuscript acceptance gates

Run the relevant gates on visible prose and record the requirement-control IDs being tested. A diagnostic script may locate risk; it cannot decide scholarly acceptance. If the registry marks any control `conflict`, freeze only the dependent branch, show both readings and consequences to the user, and obtain confirmation before drafting or issuing a dependent verdict.

## A. Scope and topic viability

- State the contextual safety boundary. Introduce a traditional threat model only when attacker capability, protected asset, trust boundary, and attack path materially determine the design or evaluation.
- Identify the nearest research neighbor and test whether the proposed research object, intervention point, mechanism, data, and evaluation differ enough to support the claimed contribution.
- If novelty or feasibility is weak, narrow, redesign, replace, or withdraw the topic before expanding prose.
- Keep the three-paper series complementary. Paper 1 discovers and diagnoses attack paths, Paper 2 performs pre-action recognition, and Paper 3 uses new post-action observations for runtime control; later papers do not invalidate earlier ones.

## B. Major-section argument

- The section has a clear reader question, an argument arc, and a payoff into the next section.
- Read the section as a continuous paragraph chain: each paragraph inherits a live issue, performs new work, and creates the reason for the next paragraph or section.
- Headings represent meaningful conceptual units rather than ledger debts or isolated paragraphs.
- Proportion matches rhetorical responsibility; introductions are not skeletal while methods and evaluation absorb the manuscript.
- There is no universal sentence quota. Sparse sections, abrupt transitions, or single-paragraph subsections trigger comparison with matched authoritative sections and revision of the missing rhetorical work.
- Introduction subsections and other visible hierarchy are used only when they improve the reader's argument map and are supported by a functionally matched recent writing model.

## C. Evidence and citations

- Consequential facts, theory claims, inherited methods, data claims, and empirical interpretations are bounded by directly inspected originals.
- Citation roles are explicit and non-duplicative; bibliographic identity and the cited source's own reference responsibility are verified.
- Foundational sources are connected to later development or current adoption when the claim depends on the construct's present meaning or use.
- Adjacent literature includes an explicit applicability bridge and a non-transferable boundary.
- A writing prototype transfers rhetorical function only. It does not become substantive evidence for the target claim.
- Responsibility classification is mandatory: distinguish source-dependent claims, author synthesis, writing prototypes, author protocols or expectations, and internal cross-references.
- Before section acceptance, every reader-visible natural-language sentence has a `PROTOTYPE_VERIFIED` authoritative IS writing prototype. Verification compares rhetorical function, sentence construction, citation placement/responsibility, given-to-new relation, paragraph position, disclosure stage, and punctuation function; it does not require identical wording or domain content.
- Author-designed protocols, expected relations, and future diagnostics still receive a prototype, but a functionally analogous method disclosure, design-choice, planned-evaluation, or boundary sentence is sufficient. If no acceptable prototype survives full-context inspection, the sentence remains `PROTOTYPE_SEARCH_OPEN` and is broadened, revised, split, moved, or held.
- A screened literature set does not replace source verification. Single-paper use returns to the original; set-level claims about counts, completeness, absence, representativeness, or recall also require an explicit set status and corpus-integrity basis.

## D. Theory and substantive artifact

- Each construct performs distinct explanatory or prescriptive work and is not a decorative synonym.
- Problem knowledge maps through design responsibility and design principle to a component, observable mechanism, main test, and rejection outcome.
- Competing theories or explanations are considered when they would change the design, observable implications, or interpretation.
- A paper claiming an algorithmic or computational contribution contains a substantive trainable, inferential, optimization, control, or measurement capability. A prompt, static rule list, or simple score may support that capability but is not promoted into the main artifact unless it is itself the justified research object.
- The artifact's inputs, state, operators, outputs, learning or update boundary, and failure route stay consistent across theory, method, and evaluation.

## E. Benchmark and evaluation

- The benchmark name is earned by a frozen task, analysis unit, data identity, protocol, metric, and comparison responsibility; an ordinary dataset or performance table is not silently renamed a benchmark.
- Baselines test competing explanations or design responsibilities, not merely popularity or availability.
- The main evaluation states what result would support the mechanism and what result would reject, narrow, or redirect it.
- Pilot checks, expected outcomes, completed observations, and final results remain visibly distinct.
- Dataset access, corpus status, leakage controls, versioning, and feasible evaluation cost are explicit before results claims are written.

## F. Feasibility, stage, and integrity

- Data identity and access, sample or participant burden, instrumentation, implementation dependencies, and analysis dependencies are explicit.
- Internal feasibility and audit records remain in ledgers or methods appendices unless they perform a reader-facing argumentative role; token budgets, agent logistics, hashes, and acceptance machinery are not narrated as scientific contribution.
- Infeasible requirements trigger redesign, demotion, or withdrawal before prose expansion.
- No results, execution, validation, acceptance, or release are implied if not performed.
- The draft declares its stage: concept, protocol, implementation, pilot, evaluation, or accepted manuscript checkpoint.

## G. Readability and source-guided writing

- The complete target section is compared directly with each selected authoritative carrying section and, when context permits, its preceding and following major sections.
- When multiple authorities are plausible, record their function and differences. Compatible patterns may be assigned separate responsibilities; materially incompatible patterns for the same decision become a registered `conflict` and require user confirmation before an adopted/rejected pattern is finalized. Classical sources may ground theory; recent top-IS exemplars normally carry current rhetorical and section-design expectations.
- Sentence subjects, referents, transitions, citation placement, paragraph rhythm, and punctuation make the positive argument easy to reconstruct.
- Terminology is stable and natural. Use `编程智能体` as the default Chinese term unless a source-specific distinction requires another label; retain proper names only when they perform necessary identification work.
- Repeated colon/semicolon scaffolds, defensive exception lists, overloaded concepts, and requirement-enumeration prose always trigger direct source comparison.
- The earlier independent punctuation-zero rule is superseded. Punctuation is judged as one dimension of the verified writing prototype and the paragraph's rhetorical work. Counts may locate repeated scaffolds, but zero or nonzero counts cannot independently pass or fail prose.
- Style imitation transfers rhetorical responsibility and organization, not phrases, proprietary expression, or domain claims.

## H. Whole-manuscript integration

After every reader-visible major section and the references that already exist in the declared manuscript stage reach their checkpoints, run [whole-manuscript-integration.md](whole-manuscript-integration.md). Existing failed or provisional sections may be reopened but not excluded; only unwritten future-stage sections may remain outside the target. Local section acceptance does not establish whole-manuscript coherence, evidence balance, series distinctiveness, or release readiness.

## Verdicts

- **accepted** — all relevant gates pass for the stated artifact and purpose, and the user accepts that checkpoint.
- **provisional** — usable with listed unresolved conditions, a bounded use, and a named next checkpoint.
- **superseded** — replaced by a named successor and retained for provenance.
- **rejected** — failed a material gate or was explicitly rejected; it may remain a failure exemplar.

Never infer acceptance from task completion, filenames, token expenditure, hashes, mapping percentages, diagnostic counts, agent agreement, or automated `PASS` text.

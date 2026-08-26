---
name: coding-agent-manuscript
description: Write, revise, resume, or audit the Coding Agent security manuscripts in this repository through complete major-section checkpoints and final whole-manuscript integration. Use for theory-to-algorithm design, direct-source comparison, citation networks, feasibility, cross-paper complementarity, or predecessor/successor decisions. Do not use for AIS corpus screening or generic academic copyediting.
---

# Coding Agent Manuscript

Treat scholarly writing as a source-grounded artifact workflow, not a long-running autonomous Goal. The manuscript, normalized requirement registry, canonical ledgers, predecessor/successor relation, and explicit acceptance record are the durable state.

## Start

1. Read `docs/research_program/current_state.md` and every control in `docs/research_program/requirement_registry.md` whose consumer or trigger applies. When adopting a screening set or collection-level claim, this includes `S-AUDIT-01` even though its domain is Screening.
2. If an applicable control is `conflict`, present both readings, their effect on the current manuscript decision, and a recommended resolution to the user. Do not silently choose or close that gate before confirmation; continue only unaffected work.
3. Apply the confirmed writing controls. `M-ANCHOR-01/L26` requires a verified authoritative IS writing prototype for every reader-visible natural-language sentence before section acceptance; the match concerns rhetorical function, construction, citation responsibility, local logic, and punctuation function rather than identical content or wording. `M-PUNCT-01/L24` is superseded as an independent zero-count gate; punctuation is reviewed inside the prototype and prose comparison.
4. Read [references/source-routing.md](references/source-routing.md), [references/acceptance-gates.md](references/acceptance-gates.md), and the stable core of the ledgers required by the current responsibility. For drafting or revising prose, also read [references/writing-prototype-search.md](references/writing-prototype-search.md).
5. Freeze one paper, one complete major section, its writing stage, predecessor/status, relevant control IDs, safety boundary, authoritative source window, feasibility assumptions, and exclusions. If the request spans papers or sections, sequence bounded checkpoints.
6. Inspect nearest work and feasibility before expanding prose. A topic whose contribution is already carried by a direct neighbor, whose main artifact is trivial, or whose data/evaluation path is not viable must be narrowed, redesigned, or replaced.
7. Inspect the working tree and preserve unrelated user changes.

The v15 manuscripts are rejected predecessors. They remain provenance and failure evidence, not accepted prose or a heading template.

## Complete major-section cycle

Follow [references/major-section-workflow.md](references/major-section-workflow.md):

1. Reconstruct the reader-level argument and paragraph chain before sentence editing.
2. Read the authoritative carrying section in full; when context permits, include its preceding and following major sections. Preserve paragraph order and rhetorical function instead of comparing against a detached summary.
3. Select writing paradigms by section function. ACAA/DSDL remain the primary ISR structure; recent top-IS algorithm/security papers complement them where the task differs. Bound compatible differences by responsibility; present materially incompatible choices to the user before recording an adopted/rejected model.
4. Resolve source, citation-network, writing-prototype, and author-protocol responsibility using [references/evidence-and-citations.md](references/evidence-and-citations.md). After the macro argument and initial full-section draft exist, run the iterative prototype cycle in [references/writing-prototype-search.md](references/writing-prototype-search.md) for every visible sentence.
5. Write the entire target major section as visible prose. Keep theory computational: `problem/construct knowledge -> design responsibility/principle -> substantive component -> observable mechanism -> main test -> rejection outcome`.
6. Run every relevant gate in [references/acceptance-gates.md](references/acceptance-gates.md) on the visible section. Counts and scans trigger inspection; they never pass the prose.
7. Compare the completed section side-by-side with multiple functionally matched originals, then persist changed claims, new sources, rejected uses, citation relations, writing insights, feasibility, and predecessor/successor status in the canonical owners.

Source facts and inherited theoretical or method claims always require direct original support. Every sentence additionally needs a verified writing prototype, but a prototype is not substantive evidence. Expected methods, author protocols, planned tests, and future diagnostics may use a looser functionally analogous method or protocol disclosure prototype because their content is new; they still cannot skip the prototype cycle or fabricate observations.

## Whole-manuscript integration

After every reader-visible major section and the references that already exist in the declared manuscript stage have reviewable checkpoints, read [references/whole-manuscript-integration.md](references/whole-manuscript-integration.md). Recheck end-to-end narrative, section handoffs, proportions, repetition, terminology, theory-artifact-evaluation identity, evidence distribution, and cross-paper boundaries. Only future-stage sections that have not yet been written may be excluded; an existing failed or provisional section may be reopened but not omitted. Passing individual sections does not pass the manuscript.

## Iteration and acceptance

New reading may change claims, theory, design, citations, feasibility, or prose. Propagate a material change through every affected section and ledger in the same bounded checkpoint. Stop for a user decision, unverifiable source, or failed feasibility gate with the blocker recorded rather than hidden.

Call a section or manuscript **accepted** only after its relevant gates pass and the user accepts it for the stated stage. `final`, `PASS`, hashes, citation counts, mapping coverage, or agent agreement do not establish acceptance.

## Delegation

Read [references/delegation.md](references/delegation.md) before delegating. Use non-overlapping packages by default and independent duplication only for a named high-risk decision. Every package carries applicable control IDs, exact ledger/source sections, manuscript scope, rejected misuses, acceptance gates, and evidence-level return fields. The primary agent reopens decisive originals and the returned prose before adoption.

## Historical calibration

Read [references/historical-lessons.md](references/historical-lessons.md) when resuming, changing versions, interpreting old completion claims, or reusing prose. The task catalog locates history; the requirement registry states current behavior. When a new user correction changes a durable rule, route its traceability update through `$research-project-continuity`.

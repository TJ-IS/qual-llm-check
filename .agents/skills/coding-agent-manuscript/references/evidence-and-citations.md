# Evidence and citation responsibility

## Verify at claim level

For every consequential claim, inspect the original paper text and bibliography. Record enough location information to reproduce the check: section/page or Markdown heading/line window, the claim supported, and the boundary not transferred.

Classify source roles:

- **direct basis** — the source directly supports the construct, mechanism, method, or empirical fact used.
- **direct descendant** — explicitly extends, tests, critiques, or develops the cited work.
- **local adoption** — applies the theory/method in a relevant domain and supports transferability.
- **adjacent applicability** — supports a neighboring setting; requires an explicit bridge and bounded wording.
- **background/history** — establishes lineage but does not carry the current operational claim.
- **method precedent** — supports a method family, not necessarily this study's exact topology or estimand.
- **author protocol** — our proposed procedure or decision rule; justified by internal logic and feasibility, not misrepresented as an inherited fact.
- **rejected use** — discovered but not adopted, with the reason retained.

Do not cite a paper merely because its vocabulary resembles ours. A citation must have a named responsibility in the paragraph.

## Writing prototypes and author responsibility

`M-PROTOCOL-01` and the qualified `M-ANCHOR-01/L26` operate together: first separate evidentiary responsibility, then verify the writing prototype for every visible sentence.

Keep four records distinct:

- **source fact/evidence** — what the cited original actually defines, implements, or observes;
- **author synthesis** — the study's bounded inference from named inputs and an explicit reasoning bridge;
- **writing prototype** — the rhetorical function, construction, citation responsibility, paragraph position, punctuation function, disclosure order, or sentence relation learned from a complete authoritative section;
- **author protocol** — this study's proposed topology, operation, estimand, threshold, planned test, or expected diagnostic.

A writing prototype does not support a factual claim. Direct original support remains mandatory for inherited facts, theory, measurement, method properties, benchmark capabilities, and data claims.

Every reader-visible sentence must reach `PROTOTYPE_VERIFIED` before section acceptance. Exact semantic identity and lexical imitation are not the criterion. The reviewer must inspect the original paragraph and complete carrying section, then record the comparable rhetorical move, sentence construction, citation placement/responsibility, given-to-new relation, paragraph position, disclosure stage, punctuation function, and non-transferable content.

For author protocols, planned tests, expected relations, and future diagnostics, seek a functionally analogous method disclosure, design-choice justification, planned-evaluation, or boundary sentence. Because the substantive contribution is new, this structural match may be looser and need not describe the same method or result. If no acceptable prototype is found, retain `PROTOTYPE_SEARCH_OPEN`, broaden the authority pool, or revise/split/move the target. Do not fabricate a precedent or treat the prototype as factual support.

## Build networks, not isolated lists

For a central theory or method:

1. inspect the references in strong recent papers;
2. trace the older source backward to its intellectual basis;
3. trace forward citations for extensions, boundary conditions, and modern restatements;
4. distinguish direct descendants from papers that merely cite it;
5. seek local and adjacent applications that support the transfer bridge;
6. check whether recent work makes the proposed wording obsolete or overbroad.

Prefer a small complementary bundle of sources with distinct responsibilities over repeated use of one convenient paper. Citation density should follow claim density. A numeric citation target can identify sparse passages but cannot determine whether the sources are sufficient.

Classical theory and methods may carry original definitions. Pair them, where relevant, with verified later development, boundary, or current/adjacent adoption. Prefer recent top-IS papers as writing models, not as automatic substitutes for the original source.

When multiple authoritative writing models differ, first test whether their responsibilities are compatible by scope. If they prescribe materially incompatible architecture or claim responsibility for the same target decision, retain both readings and consequences, mark the relevant control `conflict`, and ask the user to confirm the selection. Do not average incompatible structures or let topical similarity decide silently.

## Screening-set adoption

Using any screening output activates `S-AUDIT-01`. An individual article found through a set may support a manuscript claim only after its own original is directly verified. A claim about a set's size, completeness, absence, representativeness, or recall also requires the current adoption manifest, frozen population and label, corpus-integrity status, and the standards in `.agents/skills/ais-fulltext-screening/references/evidence-gates.md` under `Standards`. A provisional set cannot carry a gold-standard, final-recall, or exhaustive-absence claim. Read `docs/research_program/current_state.md` and the current AIS adoption/baseline artifacts instead of hard-coding a count as a durable status.

## Ledger record

At minimum retain:

- bibliographic identity and stable locator;
- source tier and relationship type;
- exact original section read;
- supported claim and prohibited overreach;
- paper/section/paragraph responsibility;
- status: candidate, verified, adopted, bounded, replaced, or rejected;
- related sources and forward/backward links;
- effect on theory, design, feasibility, or prose.
- writing-template conflict and selection, when applicable;
- screening-set identity/status when a set-level claim is used.

If new reading changes a manuscript statement, update the statement and ledger in the same bounded checkpoint.

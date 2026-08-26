# Skill sources and local design decisions

Reviewed: 2026-08-26.

The external repositories were studied as design inputs, not copied wholesale. Their reusable ideas were adapted to this repository's manuscript, literature, and screening failure history.

## Sources studied

| Source | Material inspected | Transferable practice | Local adaptation |
|---|---|---|---|
| [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | Repository README, workflow/use guidance, and `book-to-skill` skill | Extract operational structure rather than summaries; separate compact core instructions from on-demand chapters/references; retain frameworks, rules, anti-patterns, and topic routing; do not reproduce source text without rights | Historical tasks became a curated catalog and failure taxonomy instead of transcript summaries. Manuscript evidence stays in canonical ledgers; skills provide routing and bounded procedures. Publication rights are a separate gate. |
| [mattpocock/skills](https://github.com/mattpocock/skills) | `writing-for-agents`, skill mechanics, handoff, research, and wayfinding materials | Prefer small composable skills, context pointers, progressive disclosure, a single source of truth, checkable completion criteria, and handoffs that reference existing artifacts rather than duplicating them | The project uses three domain-bounded skills, concise root routing, exact ledger pointers, evidence-level return schemas, and explicit accepted/provisional/superseded/rejected states. |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Engineering guidelines | State assumptions, favor simple/surgical changes, and define verifiable success criteria | These controls remain useful for scripts and repository changes. The source's goal-driven framing is not carried over to open-ended scholarly writing: code tests can be determinate, while literature-driven prose repeatedly changes its own claims and acceptance criteria. |

## Installed personal skills

The following were installed in the user's Codex skill directory for future tasks: `book-to-skill`, `writing-for-agents`, `handoff`, `research`, and `karpathy-guidelines`. Personal installations do not travel with Git; the three repo-local skills below contain the project-specific durable adaptation:

- `.agents/skills/coding-agent-manuscript/`
- `.agents/skills/ais-fulltext-screening/`
- `.agents/skills/research-project-continuity/`

## Current repo-local skill suite

### `coding-agent-manuscript`

The entrypoint freezes one paper, one complete major section, writing stage, predecessor, safety boundary, requirement controls, source window, and feasibility assumptions. It runs topic/admissibility checks before prose, rebuilds the reader-level paragraph chain, compares complete authoritative sections and adjacent sections, separates evidence from writing prototypes and author protocols, writes the full visible section, and then iteratively verifies an authoritative IS writing prototype for every reader-visible sentence. Prototype matching covers rhetorical function, construction, citation responsibility, local logic, and punctuation function rather than identical content; novel protocols use looser functional models. After every existing reader-visible section in the declared stage is reviewable, it invokes a separate whole-manuscript integration gate; failed or provisional existing sections cannot be excluded.

Its references own distinct responsibilities:

- `source-routing.md`: canonical ledger routing, source hierarchy, series structural baseline versus section-local comparator, theory/writing recency clocks, and the frozen writing-prototype corpus/search route;
- `major-section-workflow.md`: the bounded section cycle, safety and topic freeze, paragraph spine, theory-to-computation chain, visible-prose separation, and handoff;
- `evidence-and-citations.md`: claim-level originals, citation roles and networks, adjacent bridges, author/writing/evidence separation, and screening-set adoption;
- `acceptance-gates.md`: scope, argument, evidence, substantive artifact, benchmark, feasibility/stage, readability, and integration gates;
- `whole-manuscript-integration.md`: end-to-end narrative, handoffs, proportions, identity, evidence distribution, benchmark, and series checks;
- `delegation.md`: frozen packages, control IDs, evidence-level returns, bounded independent duplication, and root verification;
- `historical-lessons.md`: rejected predecessors, Goal failure, diagnostic limits, and durable writing corrections;
- `audit_section_structure.py`: a diagnostic only; it cannot issue scholarly acceptance.

### `ais-fulltext-screening`

The entrypoint keeps corpus identity, retrieval, classification, and gold-standard audit separate. It freezes the scientific question and run-specific evidence/context roles, designs systematic retrieval from directly inspected SLR methods when applicable, obtains user confirmation before expensive runs, verifies corpus identity, executes resumably, audits false positives/negatives, assigns set status, and creates an adoption boundary for manuscript use.

Its references own corpus identity, search/run design, decision/evidence boundaries, public application/license categories, adoption manifests, and historical run baselines. `audit_screening_run.py` checks accounting and schema; it does not make scientific inclusion or gold-standard decisions.

### `research-project-continuity`

The entrypoint resumes from current repository state rather than Goal/task claims, curates artifact and conversation history, maintains predecessor/successor checkpoints, prepares bounded handoffs, and enforces publication/privacy boundaries. `requirement-traceability.md` coordinates the public normalized registry with ignored minimal-excerpt audits. Materially conflicting requirements remain `conflict` and are presented to the user for confirmation. `validate_requirement_registry.py` has a public-clone mode for the frozen per-atom map, current dispositions, pointers, consumers, and privacy patterns, plus a `--require-private-audit` maintainer mode for ignored local provenance; `audit_repository_readiness.py` checks publication readiness.

The shared public control plane is `docs/research_program/requirement_registry.md`. It currently contains 31 controls, the frozen 58-atom baseline audit, and three post-baseline corrections without private quotations. The two formerly disputed writing choices were resolved by the user on 2026-08-26: sentence-prototype coverage is qualified and active, while the independent punctuation-zero gate is superseded. The executable writing-prototype manifest is separate from the broader accumulated human comparison ledgers, and cross-platform continuation is an active repository requirement. The canonical manuscript ledgers remain responsible for detailed source evidence, paper decisions, sub-agent packages, citation networks, and source-specific writing observations.

## Design choices

1. **No mega-skill.** Manuscript writing, corpus screening, and continuity/publication have different evidence and acceptance gates.
2. **No long-lived writing Goal as state.** One complete major section is the largest default scholarly checkpoint. The repository records status and user acceptance.
3. **Structure before summary.** A resumed agent reads the current-state/router, then the original complete source section and exact ledger entries. Curated history helps route; it does not replace originals.
4. **Progressive disclosure.** Each `SKILL.md` contains the non-negotiable flow and links to task-specific references. Sedimented append-only logs are selected by responsibility rather than loaded wholesale.
5. **One canonical owner per responsibility.** Skills point to existing ledgers instead of creating parallel state stores.
6. **Diagnostics are non-authoritative.** Scripts count structure and reconcile runs, but their output explicitly cannot produce a scholarly or gold-standard PASS.
7. **Delegation is bounded.** Agents receive frozen, non-overlapping evidence packages. Broad duplicate reviews are a known cost/failure pattern.
8. **Publication is manifest-led.** Curated evidence and source corpora are separated from caches, third-party assets, and private transcripts; rights decisions are not inferred from technical accessibility.
9. **Historical verdict and current rule are different fields.** The registry preserves what was missing or partial at baseline while separately recording the post-revision disposition.
10. **Contradictions require user adjudication.** Neither recency, top-level placement, nor agent consensus silently resolves incompatible operative requirements.
11. **Cross-platform continuation is explicit.** Committed paths, encodings, commands, and interpreter requirements support Windows and macOS; a static audit is not reported as a target-OS run.

## Iteration rule

When direct comparison with an authoritative source, a new citation relationship, a screening error, or a user correction reveals a durable rule, update the unique authoritative domain rule and the public requirement registry in the same bounded checkpoint. Preserve exact wording only in the ignored private audit when it is necessary for adjudication. Update a skill only when the lesson changes future workflow across more than one local item. If the new rule conflicts with an operative rule, stop its final adoption and obtain user confirmation before changing the disposition.

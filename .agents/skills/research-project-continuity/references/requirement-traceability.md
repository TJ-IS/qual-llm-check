# Requirement traceability protocol

Use this branch when a user correction changes durable behavior, when a skill is created or revised from task history, or when someone asks which historical requirements were adopted.

## Two-layer record

Maintain two coordinated artifacts with the same atom/control IDs.

1. **Public registry:** `docs/research_program/requirement_registry.md`. Store normalized requirements, authoritative rule pointers, status, and supersession. Do not store private quotations or message payloads.
2. **Private provenance audit:** an ignored file under the relevant `audit_artifacts/` directory. Store only the minimal exact user excerpt needed for adjudication, task/message provenance, the matched rule, and the pre/post-revision verdict. Never copy a raw transcript.

The public registry is the operational index. The private audit is provenance evidence. Neither substitutes for the authoritative rule in the domain skill or canonical ledger.

## Update sequence

1. Reopen the original user message when wording changes the decision; do not infer it from an assistant summary or task final message.
2. Split compound messages into requirement atoms. Repeated messages point to the same atom; materially different corrections receive a new atom or a supersession edge.
3. Classify each atom as `active`, `qualified`, `run_specific`, `superseded`, `open`, or `conflict`.
4. Update the authoritative domain rule first. Prefer one owner. When no material conflict exists, remove or qualify stale wording; when a material conflict exists, preserve both candidates under a conflict-only control and wait for user confirmation before making either operative.
5. Update the public registry in the same checkpoint with the rule pointer and current interpretation.
6. Update the private provenance audit when exact wording or message identity is needed to reproduce the adjudication. A semantic change or contradiction always receives a post-revision entry.
7. Search the skill tree and canonical ledgers for contrary wording. Record and resolve every conflict; a newer top-level rule does not silently neutralize a stale mandatory ledger.
8. Validate that every affected atom has exactly one current disposition and every authoritative pointer resolves.

## Conflict adjudication

When two operative requirements cannot both govern the same decision, do not silently prefer the newer, more specific, more convenient, or higher-level wording.

1. Freeze both clauses, their atom/control IDs, source dates, and exact affected decision.
2. Distinguish a true contradiction from compatible scopes, a run-specific exception, or a later instruction that already explicitly names the replacement.
3. Present the user with both readings, the practical consequence of each, and a recommended resolution.
4. Mark the control and atoms `conflict` while awaiting confirmation. Continue only work whose result does not depend on the disputed choice.
5. After confirmation, update the authoritative rule, registry disposition, supersession/qualification edge, and private audit in one checkpoint; retain the rejected reading as provenance.

Agent consensus, recency, or an inferred hierarchy cannot close a material conflict. If a user instruction explicitly resolves the two named readings, record that confirmation rather than asking the same question again.

## Promotion boundary

Promote a historical instruction into a universal skill rule only when it changes repeated decisions across tasks. Keep model names, concurrency, years, construct-specific inclusion rules, paper-specific notation, and one-off user choices in their frozen run or paper ledger.

A later correction may narrow an earlier rule without erasing it. Preserve the earlier atom as `superseded` or `qualified` and name the current control. Do not present both formulations as simultaneous requirements.

## Skill and sub-agent handoff

At the start of manuscript or screening work, load every control whose consumer or trigger applies. A sub-agent package names the applicable control IDs and statuses and supplies the authoritative rule/source sections; a prose summary alone is insufficient. A conflict-status package may gather branch evidence and consequences but may not delegate selection, drafting, or acceptance that depends on the disputed branch.

Sub-agents may identify possible new atoms but do not edit the shared registry unless their package grants that single responsibility. The primary agent reopens the decisive original user message and merges the result.

## Publication boundary

Git may retain the public registry, normalized lessons, skill rules, and task-level catalog. Keep private exact-quote audits ignored. Before staging, verify that no raw session JSONL, transcript dump, credentials, or private message payload entered tracked files.

The registry validator's default public mode must succeed in a clean clone without private artifacts. Maintainers additionally run `--require-private-audit` to compare the frozen per-atom verdicts and provenance, check long quotation overlap, and verify that private files remain ignored, untracked, and unstaged. Use `--require-no-conflicts` only when claiming a closed requirement-history checkpoint.

## Completion criteria

A requirement-history checkpoint is complete only when:

- every inspected task has a recorded disposition or an explicit no-new-requirement result;
- every durable atom maps to an active, qualified, run-specific, superseded, open, or conflict control;
- no open atom is described as integrated;
- no conflict is described as resolved before user confirmation;
- current rules and mandatory ledgers contain no unresolved contradiction;
- public and private layers use matching IDs;
- a fresh agent can locate the operative rule without reading a transcript.

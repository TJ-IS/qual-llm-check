# Research program map

This directory is the human-readable control plane for the repository. It prevents task history, manuscript drafts, screening outputs, and source corpora from being mistaken for one another.

## Start here

| Need | Canonical entry |
|---|---|
| Current scholarly and screening status | [current_state.md](current_state.md) |
| Which prior tasks matter and why | [conversation_catalog.md](conversation_catalog.md) |
| Which durable user requirements are active, qualified, run-specific, superseded, open, or awaiting conflict confirmation | [requirement_registry.md](requirement_registry.md) |
| What Git should retain or ignore | [artifact_retention_manifest.md](artifact_retention_manifest.md) |
| How to prepare the manual GitHub upload | [github_upload_checklist.md](github_upload_checklist.md) |
| External skill study and local design choices | [skill_sources_and_design_decisions.md](skill_sources_and_design_decisions.md) |
| Coding Agent manuscript workflow | `.agents/skills/coding-agent-manuscript/SKILL.md` |
| AIS full-text screening workflow | `.agents/skills/ais-fulltext-screening/SKILL.md` |
| History, checkpoint, and handoff workflow | `.agents/skills/research-project-continuity/SKILL.md` |
| Otero search/download workflow | `.agents/skills/otero-open-api/SKILL.md` |

## State model

Every durable artifact should have one of these labels:

- **authoritative**: primary source, frozen input, or canonical protocol that has been directly verified.
- **accepted**: an output the user has explicitly accepted for its stated purpose.
- **provisional**: usable with named unresolved conditions.
- **superseded**: retained for provenance but replaced by a named successor.
- **rejected**: retained as a diagnostic or failure example, not as a model to imitate.

`final`, `终稿`, `PASS`, a high coverage percentage, or a task being marked complete does not assign one of these states. Human-visible quality and the relevant acceptance gates do.

Requirement controls additionally use `conflict` when two operative readings cannot both govern one decision. Such a conflict is shown to the user and remains unresolved until the user confirms the interpretation.

## Why this replaces long-running writing goals

Coding Agent manuscript work is interpretive and cyclic: original-source reading changes claims; changed claims alter theory, design principles, citations, and prose; whole-section comparison can expose a new structural problem. A long-lived goal compresses these revisions into a misleading completion signal. The repository therefore uses bounded major-section checkpoints, persistent evidence and decision ledgers, and explicit predecessor/successor relations.

Screening runs are more deterministic, but still require frozen prompts, denominators, corpus-integrity checks, and independent audit before a count becomes a standard.

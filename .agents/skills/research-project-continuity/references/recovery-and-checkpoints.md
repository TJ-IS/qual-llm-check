# Recovery and checkpoint protocol

## Recovery order

1. User's latest correction or acceptance decision.
2. `docs/research_program/current_state.md`.
3. Canonical artifact/ledger and its internal status record.
4. Git diff/status and concrete files produced.
5. Curated conversation catalog.
6. Prior task final messages, only as historical claims to verify.

If these conflict, do not silently choose the most optimistic or merely latest state. Freeze both readings and the inspectable evidence, explain their practical consequences, recommend a resolution, and ask the user to confirm. A later direct user instruction closes the conflict without another question only when it explicitly adjudicates the competing readings; record that confirmation and the supersession/qualification edge.

## Bounded checkpoint template

Record:

- checkpoint ID/date and domain;
- objective limited to one inspectable artifact;
- current authoritative/provisional input paths;
- predecessor and status;
- exact sources/ledgers/configuration used;
- decisions made and alternatives rejected;
- files changed;
- verification performed and its limits;
- user acceptance state;
- unresolved blockers;
- one next bounded action.

The checkpoint may be a concise Markdown entry or an existing canonical ledger update. Do not create another ledger if one already owns the responsibility.

## Resume rules

- Do not redo accepted work unless new evidence invalidates it.
- Do not inherit `complete` from an old Goal or filename.
- Inspect the original section/run/config rather than a detached summary when quality depends on context.
- If a predecessor was rejected, name the rejection reason before deriving a successor.
- If the user has not accepted an artifact, use `provisional`, `superseded`, or `rejected` as appropriate.

## Handoff economy

Prefer exact pointers over copied context. Include a short “why this path matters” note for each pointer. A good handoff lets the next agent load only the necessary source sections and ledgers while still recovering the decision chain.

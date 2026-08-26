# Prompt review status

No further API calls are authorized until the user confirms the prompts below.

## Stage 2 — already completed; treat as pilot pending confirmation

- Purpose: distinguish genuinely IS-shaped benchmark-improvement research from generic CS/ML/SE/OR benchmark work with an application wrapper.
- System prompt: `ais_is_distinctive_benchmark_logic_flash/system_prompt.md`
- User template: `ais_is_distinctive_benchmark_logic_flash/user_prompt_template.md`
- Actual assembly: one `system` message containing the complete system prompt; one `user` message containing article metadata and the complete Markdown full text. No stage-one reasoning was supplied.
- Candidate pool: 1,976 stage-one model matches plus two manual-audit additions.
- Completed: 1,978; matches: 956; request/parse errors: 0.

## Stage 3 — main pass completed; incomplete records frozen pending confirmation

- Purpose: transfer source design-to-outcome logics into objectively measurable, artifact-manipulable, thesis-series-ready metrics whose meaning requires coding-agent work.
- System prompt: `coding_agent_unique_metric_transfer_from_is_benchmarks/system_prompt.md`
- User template: `coding_agent_unique_metric_transfer_from_is_benchmarks/user_prompt_template.md`
- Actual assembly: one `system` message containing the complete system prompt; one `user` message containing article metadata, that article's own compact stage-two JSON, and that article's complete Markdown full text. No other article was included.
- Candidate pool: 956 stage-two matches.
- Current state: 945 successful decisions and 11 unresolved formatting/empty-response failures. No retry is authorized before confirmation.

## Stage 4 — draft only; never run

- Purpose: identify benchmark-based IS contribution logics that remain cumulative and retestable after major model or technical-substrate upgrades.
- Draft system prompt: `model_upgrade_resilient_is_contribution_DRAFT/system_prompt.md`
- Draft user template: `model_upgrade_resilient_is_contribution_DRAFT/user_prompt_template.md`
- Proposed assembly: one `system` message containing the approved system prompt; one `user` message containing article metadata, that article's own compact stage-two JSON, and the complete full text.
- Proposed candidate pool: 956 stage-two matches. Results would later be intersected locally with stage-three metric candidates.
- No runner/config exists and no API request has been made.

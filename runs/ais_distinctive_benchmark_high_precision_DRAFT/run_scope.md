# DRAFT — DO NOT RUN BEFORE USER CONFIRMATION

- Status: prompt review only. No runner, config, output directory, or API request exists.
- Proposed candidate pool: 1,976 stage-one objective-benchmark matches plus two manually confirmed false negatives = 1,978 complete articles.
- Proposed unit: one complete Markdown article per independent request.
- Prior stage decisions/reasons will not be supplied to the model.
- No request will contain multiple articles.
- Proposed model/concurrency after approval: `deepseek-v4-flash`, maximum 200.
- Primary priority: precision of IS distinctiveness. Only `exemplary` and `strong` may be retained; `borderline` is excluded.
- Contribution beyond a transient score advantage is part of the single primary IS-distinctiveness judgment, not a separate nested decision.
- Standard CS benchmarks are explicitly allowed. The decisive issue is whether they test an IS-derived design and support broader reusable IS knowledge.
- Coding-agent transfer, metric invention, thesis-series design, and recommendation are intentionally absent.
- Proposed prompt files after approval: `system_prompt_v2.md` and `user_prompt_template_v2.md`. The original files without `_v2` are superseded drafts and must not be run.

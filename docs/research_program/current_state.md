# Current state

Last reviewed: 2026-08-26.

## Coding Agent manuscripts

The public control plane begins at `docs/research_program/requirement_registry.md`; it preserves the frozen 58-atom baseline audit, current controls, post-baseline corrections, and supersession/conflict status without publishing private task quotations. The v11 evidence system in `runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews/v11_iterative_literature_rewrite/` remains the canonical routing layer for evidence, citation roles, source relationships, paper-specific decisions, and sub-agent packages. Begin with the registry and `163_v11持久化台账索引与更新协议.md`, then route to the responsibility-specific ledger; do not treat every accumulated update log as equally relevant context.

The v15 files `184_论文一_异质工作空间攻击路径发现_v15权威原文句级重构稿.md`, `185_论文二_多模态潜藏操纵执行前识别_v15权威原文句级重构稿.md`, and `186_论文三_运行中反馈安全控制_v15权威原文句级重构稿.md` are **rejected predecessors**, not accepted manuscripts or authoritative style exemplars. The user identified sparse major sections, fragmented headings, and disproportionate methods/evaluation despite extensive sentence-level mapping and automated checks. Preserve them for provenance and diagnosis; the next version must begin with major-section argument architecture rather than another sentence-debt pass.

Authoritative external comparisons remain ACAA/DSDL-style complete-section baselines and directly inspected source sections. RADAR can be a neighboring reference but is not the target architecture for all three papers.

The repository skills now use bounded complete-major-section checkpoints followed by a separate whole-manuscript integration gate. The user resolved the two earlier writing conflicts on 2026-08-26. Qualified `M-ANCHOR-01/L26` now requires every reader-visible natural-language sentence to have a directly verified authoritative IS writing prototype before section acceptance; matching concerns rhetorical function, construction, citation responsibility, local logic, and punctuation function rather than identical content or wording. Novel methods, protocols, expected tests, and future diagnostics use looser functionally analogous disclosure prototypes but receive no no-anchor exemption. `M-PUNCT-01/L24` is superseded as an independent zero-count rule: punctuation is inspected inside prototype and paragraph comparison, while scans remain diagnostics. The hash-frozen 11-source executable corpus and candidate finder are routed through `.agents/skills/coding-agent-manuscript/references/writing-prototype-search.md`; ledgers 164 and 175 retain a broader accumulated human comparison/observation pool and do not define executable membership.

## AIS full-text screening

- The public-data/objective-metric screening run under `runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/` produced a 51-item result after a user-confirmed prompt and a complete 2,475/2,475 run. Reuse it with its frozen scope and audit artifacts, not as an all-security corpus.
- `runs/ais_basket_security_algorithm_development_flash_v2/` is the separate 99-paper algorithm-development collection.
- `runs/ais_basket_security_relevance_fulltext_flash_v1/` contains the broader 388-paper security-relevance result over 13,909 full texts. It is **provisional**: corpus audits found 36 mismatched/damaged full texts and additional boundary cases. Do not call 388 a final gold standard until repair and reclassification are recorded.
- `runs/ais_basket_final_audit_133_flash/` has a reconciled 133-item final audit trail with 52 included and 81 excluded. One raw reviewer stream contains 141 records because 8 IDs repeat; the curated 133-item trail and CSV are unique. Preserve the raw stream as attempt history, not as the scientific denominator.

Security relevance, security-algorithm development, public-data eligibility, and objective metric/benchmark eligibility are separate decisions. Do not merge their counts or labels.

## Repository publication

The repository is being curated for a user-performed GitHub upload and subsequent work on macOS. Source corpora, successful/provisional run artifacts, reusable scripts, ledgers, and repo-local skills are intended to remain available. Secrets, caches, logs, duplicate generated exports, environment folders, and private raw task transcripts must not be committed. Public instructions and manifests now use repository-relative, case-exact paths; shared Python helpers target Python 3.10+; `.gitattributes` normalizes text to LF. Windows-side checks remain a static preflight until the documented smoke tests run in a clean macOS clone. See the retention manifest and upload checklist before staging.

## Next bounded manuscript checkpoint

Do not resume by declaring “complete all three papers.” Select one paper and one complete major section, freeze its source/ledger inputs, inspect the authoritative carrying section plus adjacent sections when context permits, build the paragraph-level argument chain, write the entire section, and obtain a visible acceptance decision before advancing.

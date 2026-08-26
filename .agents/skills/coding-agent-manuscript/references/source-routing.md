# Source and ledger routing

The public requirement index is `docs/research_program/requirement_registry.md`. Read every control whose consumer or load trigger applies, not only rows whose domain says Manuscript, and carry those IDs into the section record and any sub-agent package. Any adoption of screening output activates `S-AUDIT-01` and routes to the AIS `evidence-gates.md` Standards, the current adoption manifest, and corpus-integrity status.

The canonical manuscript ledger directory is:

`runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews/v11_iterative_literature_rewrite/`

Route by responsibility. Do not create a second canonical ledger for the same responsibility.

| Need | Canonical file |
|---|---|
| Historical requirement disposition and current rule pointer | `docs/research_program/requirement_registry.md` |
| Entry point, state, routing, update protocol | `163_v11持久化台账索引与更新协议.md` |
| Authoritative-paper imitation and writing standards | `164_权威文献对标与多代理写作验收标准.md` |
| Sources read, evidence roles, exclusions, reflections | `165_迭代文献证据与反思台账.md` |
| Paper 1 decisions and feasibility | `168_论文一主张证据设计与可行性专账.md` |
| Paper 2 decisions and feasibility | `169_论文二主张证据设计与可行性专账.md` |
| Paper 3 decisions and feasibility | `170_论文三主张证据设计与可行性专账.md` |
| Frozen sub-agent package rules | `171_多代理任务包与回传审计模板.md` |
| Backward/forward citation relationships | `172_引文网络发现与追踪协议.md` |
| Accumulated human comparison observations, sentence readability, and paragraph rhythm | `175_权威原文句级论证与可读性模仿台账.md` |
| Hash-frozen executable authority corpus and candidate-sentence discovery | `.agents/skills/coding-agent-manuscript/references/authoritative-writing-corpus.json`; `.agents/skills/coding-agent-manuscript/references/writing-prototype-search.md`; `.agents/skills/coding-agent-manuscript/scripts/search_writing_prototypes.py` |

At every manuscript checkpoint, read the stable core of 164 and the current acceptance gates. For sentence/paragraph writing, also read the stable core of 175. Append-only update logs are evidence of change, not default context: select them by paper, section, construct, source, control ID, or unresolved responsibility. Paper-specific work always reads its corresponding 168/169/170 entry; delegation always reads 171's current compact package rules.

The two writing-source pools have separate owners. The JSON manifest is the only executable, hash-frozen retrieval pool. Ledgers 164 and 175 retain a broader accumulated set of sources already inspected for human comparison and source-specific observations; a ledger entry does not enter the executable pool until its identity, local full text, authority role, exact filename case, and hash are verified and the manifest is updated. The pools may overlap without being identical.

## External source hierarchy

1. Primary article full text and bibliography.
2. Direct descendants, extensions, critiques, or contemporary restatements.
3. Local-domain adoption that demonstrates applicability.
4. Adjacent literature with an explicit bridge and bounded claim.
5. Secondary summaries only for discovery, never as the final authority for a consequential claim.

For old theory, inspect both the references used by a strong recent paper and later work that cites the old source. Verify whether later work develops, applies, limits, or merely mentions it. Classical theory remains eligible; an isolated historical citation cannot carry a current operational claim when the construct has developed.

## Authoritative writing comparison

Separate two template axes. `series_structural_baseline` uses ACAA/DSDL-style ISR sections for the overall problem-theory-artifact-evaluation logic. `section_local_comparator` uses RADAR and other functionally matched algorithm/security papers only for the named method, safety, or benchmark responsibility. A local comparator does not silently replace the series baseline.

Maintain two recency clocks. Classical theory and original methods may remain old when they carry the definition, but they require verified later development, limitation, or current application where relevant. Writing paradigms should normally include at least one top-IS full section from the rolling five years before the review date. This five-year window is a search-and-explanation trigger, not an automatic exclusion rule: an older template may remain when its section-level responsibility is irreplaceable, but record why and compare it with a recent counterpart. Publication year, bibliography cutoff, and technical paradigm age are separate fields.

Compare heading placement, paragraph functions, citation responsibility, punctuation, transition rhythm, and theory-to-artifact generation directly.

After the complete-section argument and initial draft exist, use [writing-prototype-search.md](writing-prototype-search.md) to find and verify a writing prototype for every visible sentence. The script ranks candidates from the frozen corpus; it does not verify them. Reopen the exact source paragraph and complete carrying section before adoption, and keep prototype status separate from substantive citation support.

When candidate templates differ, record the target section/function and each candidate's axis and responsibility. Compatible differences may be bounded to separate functions. A material contradiction over the same architectural or rhetorical decision is registered as `conflict` and presented to the user with both consequences and a recommendation before any adopted/rejected pattern is finalized. Authority, topical similarity, recency, or agent consensus alone does not decide the choice.

The minimum acceptable comparison unit is the same complete major section. When context permits, inspect the core section plus its preceding and following major sections to understand setup and payoff.

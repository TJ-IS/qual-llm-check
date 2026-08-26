# Manuscript ledger routing

This directory is a hash-bound academic writing workspace. Before reading, editing, auditing, or delegating work on manuscripts 179–183, read `163_v11持久化台账索引与更新协议.md` in full.

Every manuscript task must also read these shared ledgers in full:

- `164_权威文献对标与多代理写作验收标准.md`
- `165_迭代文献证据与反思台账.md`
- `171_多代理任务包与回传审计模板.md`
- `172_引文网络发现与追踪协议.md`
- `175_权威原文句级论证与可读性模仿台账.md`
- `audit_artifacts/README.md`

Read the matching paper ledger as well:

- manuscript 179 → `168_论文一主张证据设计与可行性专账.md`
- manuscripts 180 and 182 → `169_论文二主张证据设计与可行性专账.md`
- manuscripts 181 and 183 → `170_论文三主张证据设计与可行性专账.md`

The current manuscript routes are exact and supersede earlier current-hash statements without deleting their historical receipts:

- manuscript 179 SHA256 `28F4CD6E7B917C4E2CF8173BA074EF2333D465DA54A6AE961365C8F22A427DDF`
- manuscript 179 inventory `audit_artifacts/论文一_Holm与cluster方法来源差分后当前逐句清单_v1.json`, SHA256 `571A9167E911BFE22B3E36B4AE02812426F6C1030CDF2E3D2D3C306F03A225DA`
- manuscript 179 route `audit_artifacts/论文一_v6当前到Holm与cluster方法来源差分后逐句路由_v1.json`, SHA256 `183A64D65B2160A4E2B10E956B94507B906C0BEE8E991D8DEDC6B38964BF2874`
- manuscript 179 validation `audit_artifacts/论文一_Holm与cluster方法来源差分后根代理机械验真_v1.json`, SHA256 `AE3877610BEB161CA93BFFF924CA139352524F0AE2AE2649ED365970A7971973`
- manuscript 182 SHA256 `6316F207AB2614FA397554CA5D2AB4780B7DD9DDE6962074AD3B23A78DA96EAF`
- manuscript 182 inventory `audit_artifacts/p2_construct_validity_current_inventory_v1.json`, SHA256 `781A2BC05A956D00D785406AEA6EFB0C600CBC8D5E4426A072158F93FE3C758C`
- manuscript 182 route `audit_artifacts/p2_construct_validity_current_route_v1.json`, SHA256 `49A9B21D353CA7AF1E76C2E89AAC718E5A3215449507D17CA8DF38C6774849FC`
- manuscript 182 validation `audit_artifacts/p2_construct_validity_root_validation_v1.json`, SHA256 `7AD6CB96CD5BA92233E4DB409A4BD3EEE2AE08377615766CDDA8154364164F11`
- manuscript 183 SHA256 `B7B3B9E79927EDB3FF1611E055A2EC04BDAA90F2A3A73FC734C7D8096829D6C5`
- manuscript 183 inventory `audit_artifacts/论文三_v5引言与书目差分后当前逐句清单_v1.json`, SHA256 `A7354AA6B6B0BB2CC18A982F31BBA788C27CD0FFFA78882C60FE58CFC31C108E`
- manuscript 183 route `audit_artifacts/论文三_v14旧正文到v5引言与书目差分后逐句路由_v1.json`, SHA256 `98E90CC52017607D6A1E93CBBDC86FE85228A4DF726ED6FF909C24B105D5B2B9`
- manuscript 183 validation `audit_artifacts/论文三_v5引言与书目差分后根代理机械验真_v1.json`, SHA256 `7C7706906569707943D7D4F52EC05AD92A37CFF975D5DEC7BFF0557E80ABBC0D`

The former 2465-unit migration baseline `audit_artifacts/三篇_当前2465单元旧映射迁移可用性盘点.json`, SHA256 `DCDEBB7BBE65AE653F40980C628EBE6465BE78EDFA9E11B38D6543E7CA4EFCC4`, is now predecessor retrieval evidence only. The current inventories contain P1 711, P2 1035, and P3 735 units. Exact old-text matches remain retrieval candidates only and `semantic_status_inherited=0`; no predecessor status can be copied into a current inventory.

When delegating, pass the exact ledger paths, current manuscript SHA256, current sentence-inventory SHA256, current migration-queue SHA256, target-ID definition, allowed edit scope, and explicit unresolved gates. A sub-agent must verify that every required path exists and report the exact ledger hashes it read. Conceptual aliases or remembered filenames are insufficient.

The old attention sets P1 36/711, P2 184/1009, and P3 111/745 are historical scheduling layers, not current completion denominators. P1 now also has 711 current units, but that equal cardinality does not make the historical 711-unit inventory current. Any new sub-agent must bind the exact current inventory hash and report its reviewed numerator against current P1 711, P2 1035, or P3 735. A narrow review cannot support a full semantic completion claim.

Original-source comparison is mandatory. Read the complete source section that carries the target claim and the complete target paragraph or table row. For core sources, include the immediately preceding and following major sections when context permits. Preserve source-native subjects, operators, outcomes, qualifiers and timing; put cross-paper abstraction in a separate author-synthesis sentence.

Root and sub-agent judgments are independent evidence streams. The root review must be frozen before reading the corresponding post-edit sub-agent review. Disagreements are adjudicated from original-source predicates and nontransferable boundaries, never by vote or status counts.

Public ledgers use a single-writer rule. Sub-agents return structured ledger deltas but do not concurrently edit 163–175 unless the task explicitly grants one ledger. The root agent merges reusable rules into 164, 165, 171, 172 or 175 and paper-specific feasibility findings into 168, 169 or 170.

Do not overwrite a hash-bound historical review after its manuscript, inventory or queue changes. Generate an append-only successor, record `supersedes` or historical scope, and keep semantic alignment, citation support, pilot evidence and release gates false until each has its own current evidence.

The former complete-introduction package `audit_artifacts/当前引言重写_子代理必读台账包_v1.json` and any proposal package whose target text or manuscript binding predates the current routes are historical. A candidate that exactly supplies a current Introduction may remain a current text source, but its earlier review package is not automatically a current review package. A new review must bind the current manuscript, inventory and route above and must receive a new phase-specific package if its independence claim requires answer isolation.

Cross-review terminology must remain exact. “No material conflict” means fact responsibility, author responsibility, source-native boundary, semantic state, and final sentence action are compatible; it does not mean every writing-prototype or adjacent-lineage field is identical. Report both the all-dimension agreement count and the material-conflict count. The former 12-unit overlap, 104-unit complete-introduction denominator, and 2465-unit full-manuscript denominator are distinct historical scopes and must never be presented as the current 711, 1000, and 735 manuscript denominators.

P1 Introduction v6 is already migrated into manuscript 179. Its 24 units remain exact, but the current full manuscript is the 711-unit post-method-source state listed above. Compose the historical 711-to-703 route with the current 703-to-711 method-source route. The two 711 counts belong to different manuscript hashes and roles. The earlier 40-sentence v3 and 24-sentence v4 chains are historical. P1 now has 11 citation placeholders and 11 explicit method-source responsibilities. Builders and post-adjudication QA read `source_snapshots/methods/README.md` and the applicable append-only method lineage reviews. A same-round independent reviewer instead receives the neutral rule projection and original sources, and must not read root or peer method verdicts before freezing its own judgment.

Any new independent reviewer must use a new neutral package for its exact current target set. It must independently read every target sentence in its complete paragraph, the current carrying major section with adjacent manuscript sections, and each original carrying major section with the immediately preceding and following major sections when context permits. A prohibited-input hit invalidates that reviewer/package pair; it is not a minor disclosure that can be waived.

Strict isolation exception: when an `independent_review` package declares that current ledgers contain same-round item verdicts, the reviewer reads this AGENTS file and the package's hash-bound `neutral_rule_projection`, not the full contents of 163–175, README, or the incremental checkpoint. The outer manifest still binds those complete ledgers as provenance, while their content is explicitly prohibited for that reviewer. This exception preserves the ledger rules without leaking the answer; it applies only to the exact package and candidate-set SHA that pass isolation preflight.

Current post-migration routing is the per-paper route listed at the top of this file. P2's construct-validity successor has 30 Introduction units and 1005 non-Introduction units. Its bibliography has 70 entries with zero orphan, missing or unresolved identities. The predecessor 1000 units are covered 1000/1000, the current 1035 units are reached 1035/1035, and 980 units outside the four authorized paragraphs remain exact in order. P3 v5 has 23 Introduction units and 712/712 exact non-Introduction successors. Its bibliography now has 48 entries with zero orphan, missing or unresolved identities. These are auditable pre-results writing states, not full semantic, citation, implementation or release passes.

P1's Holm and cluster-bootstrap source delta is current only for manuscript SHA `28F4CD6E7B917C4E2CF8173BA074EF2333D465DA54A6AE961365C8F22A427DDF`. The root and independent original-source reviews agree on 8/8 predicates with zero material conflict. Two Holm placeholders are closed at the method-source layer only. The cluster-bootstrap placeholder remains, narrowed to unbalanced repositories, the paired count estimand, minimum effective repository count, finite-sample interval, replicate count, and failure handling. Current reference identity has 38 entries with zero orphan, missing or unresolved identities. The prior 703 units are covered 703/703 and the current 711 units are reached 711/711. The reverse reconstruction restores manuscript SHA `B910B9A7...9188` exactly.

P3 D006 is time-indexed. The current append-only binding is `audit_artifacts/论文三_能力矩阵到v5引言与书目差分后当前正文哈希追加绑定_v3.json`, SHA256 `6DD1F7086AD0439A86BE5F9CC95C33F2470186B0FD4EAA62B8FB4F071A035977`, and it binds only manuscript SHA `B7B3B9E79927EDB3FF1611E055A2EC04BDAA90F2A3A73FC734C7D8096829D6C5`. Independent mechanical validation `audit_artifacts/论文三_D006_v5引言与书目差分后当前哈希绑定独立机械验真_v1.json`, SHA256 `FCD05CF1582BDA225B3853C47A999377F3CDC43A8586FDD35A580A2044B4B17D`, passes 17/17. Any later manuscript byte change reopens D006 again.

For P2, preserve the historical v1 17/18 display-text failure, its v2 successor, and the post-Sénécal 27/27 state as predecessor evidence. The current construct-validity validator passes 26/26 and reverse-reconstructs manuscript SHA `5A306B9E...F0199` exactly. The closed source audit and v2 delta gate are `C26F2217...A643` and `178E172B...881B`; the latter is `PASS_FOR_MANUSCRIPT_WRITEBACK` for 11 paragraphs and two table rows but covers only four predecessor targets out of 1000. Zhang et al. 2022 is an application and Aaltonen and Stelmaszak 2024 is a boundary addition. Neither validates the three P2 proxies. Petter, Straub, and Rai 2007 remains read but uncited. P2 has 15 current citation placeholders, including one direct construct-source debt at P2-U0118. The next P2 identification debt is rebound to P2-U0173.

Bibliographic identity is a semantic audit field. Every sub-agent must verify author, title, year, venue, and DOI from the original header, YAML, or an authoritative identity record before using a source. Preserve a frozen identity error and add an append-only corrigendum; do not silently rewrite the old result. Root reads performed after a sub-agent reveals a source are post-discovery direct verification and must not be counted as an independent stream. A review action such as narrow or retain applies only to the exact target responsibility, never to every claim associated with the source.

For all three manuscripts, `semantic_alignment`, `citation_support`, `pilot_implementation`, and `release` remain strictly `false`. A local route, reference-identity pass, or current-hash debt binding must never be promoted to a whole-manuscript pass.

## 2026-08-25 P1 path-identity and P3 external-state bounded-writeback successor

The current P1 manuscript 179 SHA256 is `5DE2D4714F4DAF36806302EF353D16A7642807E2791E0792BE0CA98B63EB4545`. Its current inventory is `audit_artifacts/p1_path_identity_current_inventory_v1.json`, SHA256 `31E514FA27FE236907A6186EFEE39306F13930ECCB6561573F0C557635B7F79D`, with 724 units. Its route is `audit_artifacts/p1_path_identity_current_route_v1.json`, SHA256 `6D3048B26E283D25A21F6327AD6E1CE86DCE171E7BCD767A0306E4E6851A1560`, and its 21/21 root validation is `audit_artifacts/p1_path_identity_root_validation_v1.json`, SHA256 `409202D7848400496AD33662C91834F64D70F201F964C081E5CF5A49401544DA`. The route covers 711/711 predecessor units and 724/724 current units, with 699 outside units exact in order. P1 has 40 references and 10 inline placeholders.

The current P3 manuscript 183 SHA256 is `D8DBF0E6D49007B030EAA38BD05F04FC00E77A8A2E26F5F5AC6ADA46F953CAAD`. Its current inventory is `audit_artifacts/p3_external_state_current_inventory_v1.json`, SHA256 `225FF2A32374F9AD3EB3726DC1F5AA5D76786F9CB791E152409AC44DE1823145`, with 737 units. Its route is `audit_artifacts/p3_external_state_current_route_v1.json`, SHA256 `EDFFBCC7D8A029381B814D5115F8161D02F3BF58EC03C01F470BA08EE6B4BED6`, and its 21/21 root validation is `audit_artifacts/p3_external_state_root_validation_v1.json`, SHA256 `AF57EE95505C42CFE65A4A6DA04CE8540610657BE9123CA87B69D5AA2FB450BC`. The route covers 735/735 predecessor units and 737/737 current units, with 726 outside units exact in order. P3 has 48 references and 12 inline placeholders.

P2 remains byte-identical at manuscript SHA `6316F207AB2614FA397554CA5D2AB4780B7DD9DDE6962074AD3B23A78DA96EAF`, 1035 units, 70 references and 15 placeholders. The three current denominators are therefore 724, 1035 and 737, totaling 2496. The former public validation v6 and outer manifest v1 bind the 711, 1035 and 735 predecessor state and are historical after the P1 and P3 byte changes.

An inline debt now has three separately reported states: literal placeholder removal, bounded citation responsibility, and open protocol or pilot debt. The first never implies the latter two are closed. Independence must always name its object. Independent stochastic trials, independent ground-truth bugs, independent coders and coder masking to a searcher condition are not interchangeable.

Multi-paragraph writebacks require both byte-level reverse reconstruction and ordered unit-level conservation. Multiple insertion sites create segmented target-ID and paragraph-ID offsets, so never apply one global offset. Rebind every downstream open target by exact visible text and sentence SHA. P3's old P3-U0605 is unchanged in meaning and bytes but is now current P3-U0607 in P3-P0152, SHA256 `165D65BD58A08195D69E1CF55838668DF52C8FE8D235C29CE50FB110B9EBB96D`.

P3 D006 v3 remains a valid historical binding only for manuscript SHA `B7B3B9E7...D6C5`. The current P3 byte change reopens D006 until an append-only current binding and independent validator are created. Do not infer a semantic failure from this time-index change.

The next prioritized current debts are P1-U0339 in P1-P0081, line 205, SHA256 `9943E1954E352D5A14B1384E7A951757F8FA0DC4322C52BAB38F834DFF9E07CD`, and P3-U0604 in P3-P0151, line 399, SHA256 `755C5554592086356E48F13F92240FD9033145F9EB70C40ECD1F2E7B4C5AF1DC`. P3-U0607 remains a second-priority provider-specific implementation and fault-injection debt that cannot be closed by literature alone.

For all three current manuscripts, `semantic_alignment`, `citation_support`, `pilot_implementation`, `release`, and `whole_manuscript_complete` remain strictly `false`.

## 2026-08-25 P1 paired-confirmation source and interval successor

The current P1 manuscript 179 SHA256 is `F212F6479FA4390218146F66CD1466827F859196450AE998623EA47D0C76AFF4`. Its current inventory is `audit_artifacts/p1_paired_confirmation_current_inventory_v1.json`, SHA256 `6BFFCF50AE001F223B5304817484A41FCDF1C00D4D9A1A025804EB798B7D0B62`, with 732 units. Its route is `audit_artifacts/p1_paired_confirmation_current_route_v1.json`, SHA256 `BE9483A0F506CBC95CF8B1437988BCF61A5155EF2CEE51E4C3CFD707C5DFA1AE`. Root validation `audit_artifacts/p1_paired_confirmation_root_validation_v1.json`, SHA256 `4FD117B1103343EA46238CB306E89895815D467827AF1447F548AC5A0222BA34`, passes 26/26 checks. Three predecessor units route to eleven current units, 721 outside units remain exact in order, and reverse reconstruction restores `5DE2D471...4545`.

Paired confirmation has two statistical levels. Within pair `j`, replay and neutral control share a snapshot and matched agent seed, so they are matched branches and must not be described as independent observations. Across pairs, the binary indicators may be modeled as independent and identically distributed Bernoulli trials only if `K` is fixed before results, seed pairs are independently drawn from one frozen distribution, the candidate and success rule remain fixed, and cache, session, service version and other state do not carry over.

The `K` confirmation pairs condition on one first-hit candidate and estimate its pair-level joint confirmation probability. The `N_rep` independent whole runs in Sections 5.2 and 5.3 estimate method-level performance. Every sub-agent must name which repetition object it is auditing and must not transfer assumptions or intervals between them.

Yao et al. 2025 supports same-task repeated trials as an agent-reliability precedent. Yang and Subramanyam 2023 supports cross-run variability for LDA topic models only. Wang et al. 2020 supports matched partitions with repeated estimates and interval reporting as an adjacent IS precedent. Brown, Cai, and DasGupta 2001 supports the Wilson interval conditional on a valid binomial model. None defines the neutral control, within-pair order, seed plan, `K` or `tau`. Demšar 2006, Dietterich 1998, Lin et al. 2024 and RADAR were directly checked for lineage and remain read-do-not-cite for this target.

P1 now has 44 references and 9 inline placeholders. The next P1 citation debt is P1-U0360 in P1-P0084 with sentence SHA256 `353335B786676F4027A320AC1088C385B87B05EC72365B9C3349E4BC9ADA44FE`. P2 and P3 remain at 1035 and 737 units. The current three-paper denominator is 2504, references are 44/70/48, and placeholders are 9/15/12. All semantic, citation, implementation, pilot, results, release and whole-manuscript gates remain false.

## 2026-08-25 P1 auxiliary-judge validation boundary successor

The current P1 manuscript 179 SHA256 is `AB81C017CE2F7BE6803A757646518F083B475DB80C44E6813BF4576101C552D2`. Its current inventory is `audit_artifacts/p1_judge_boundary_current_inventory_v1.json`, SHA256 `2C8FF6CEE04CDBAD498A918BAC048E5175E874C3E2DA8BE40EDA0428BCA70C89`, with 737 units. Its route is `audit_artifacts/p1_judge_boundary_current_route_v1.json`, SHA256 `5C09C8B8C66F4385470B011082BF257AB10E0E9D45C9991627DD2724D6D7B825`. Root validation `audit_artifacts/p1_judge_boundary_root_validation_v1.json`, SHA256 `4A55E0F069D4B8BCB5FD10DE3B486818ACFD1550349C066442E0F0380D23B127`, passes 26/26 checks. Five predecessor units route to ten current units, 727 outside units remain exact in order, and reverse reconstruction restores `F212F647...AFF4`.

RATER and Zhou et al. support only the validation responsibilities for an auxiliary semantic labeler. AgentDojo supplies the direct adversarial boundary because an injected instruction may also hijack an LLM evaluator. ToolEmu is retained as a directly read lineage node but is not cited in the target paragraph. RADAR is a prose-sequence prototype only. The judge returns fallible candidate content-trace labels with confidence and abstention. The frozen result contract remains the sole safety ground truth.

One mechanical reviewer invalidated answer isolation through a repository-wide DOI search. Its conclusion is excluded. A replacement completed the required reading but did not deliver the required review artifact before root cutoff and is also excluded. Do not relabel root post-writeback mechanics as an independent stream. Future packages must use an explicit read allowlist, prohibit repository-wide searches, and count a stream only after a parseable hash-bound artifact is delivered.

P1 now has 46 references and 8 inline placeholders. The next downstream P1 debt is P1-U0459 in P1-P0111, line 267, sentence SHA256 `6E4618E2AFE36E0002CE1C842D7D62399D362B3CC02D0AC0D80EBBE7D37D08AA`. P2 and P3 remain at 1035 and 737 units. The current three-paper denominator is 2509, references are 46/70/48, and placeholders are 8/15/12. All semantic, citation, implementation, pilot, results, release and whole-manuscript gates remain false.

## 2026-08-25 P1 group-split final current successor

The current P1 manuscript 179 SHA256 is `702755FD5725C6CAC4BA45FCBB06B2444D6E483111DE73A96EFDFACBFA8C17EC`. Its enhanced current inventory is `audit_artifacts/p1_group_split_current_inventory_v6.json`, SHA256 `832437A85FE854390CFD31A28D38D4BFC180034927AEA4D7354EB25604592426`, with 764 units. Its current route is `audit_artifacts/p1_group_split_current_route_v3.json`, SHA256 `07C8C51A2A7A66021DCA8EC291B389578ABD0455585794A2077C971DB893E22C`. Root validation `audit_artifacts/p1_group_split_root_validation_v3.json`, SHA256 `FEA80BCA4376720DEA65940ADBFFB60A1B9D3551945471FEDE396A381A369B57`, passes 31/31 checks. The route receipt is `audit_artifacts/p1_group_split_route_receipt_v3.md`, SHA256 `09AB80AE545901555D1B1FD2D295D65ACE7C704B907E807C9ED1D80F2D64DA67`; the writeback builder is `audit_artifacts/build_p1_u0459_group_split_writeback_v3.py`, SHA256 `9A452C2B3F6C1004A67E6A7EAE1AE02847B2084A0F21F8D64F3FFC5F2AF24CED`; and root cross-adjudication is `audit_artifacts/debt_review_2026_08_25/p1_u0459_group_split_v4_root_cross_adjudication_v1.json`, SHA256 `CA908E4CD96352260734171B177ECCEB6761DDBC7B49189D89F3F0398C4B6DFC`.

The bounded route covers the 737-unit predecessor and reaches all 764 current units. Its authorized scope expands from 26 predecessor units to 53 current units, while all 711 outside units remain exact and ordered. Reverse reconstruction restores predecessor manuscript SHA256 `AB81C017CE2F7BE6803A757646518F083B475DB80C44E6813BF4576101C552D2` exactly.

The Section 4.8 successor map v4, SHA256 `1C39FFCD531BA6398EB025E09469FD11D2CA86F60F1D20B0F7D1931496A04DFD`, contains 39 sentences: 9 direct-original records, 6 boundary transfers, 4 internal cross-references, 15 author protocols with bounded precedent, and 5 author protocols with no acceptable external anchor. RADAR supports only a common environment training-time-step budget. It does not support optimizer-update equality. Common reward composition, optimizer steps, and development trials are author protocols. Original protocols, planned procedures, and expected relationships do not require an older paper to have implemented the same predicate verbatim; only historical claims that prior work did, found, or proved something require exact original-source support. Never invent a citation to make an original protocol look inherited.

P1 now has 50 references and 7 inline placeholders. The next P1 debt is P1-U0563 in P1-P0132, sentence SHA256 `78598E6A82519B1A74C76518A933590723E820B9B03FCE6A2CF569EA0C500973`. P2 and P3 remain at 1035 and 737 units. The current three-paper denominator is 764/1035/737, totaling 2536; references are 50/70/48 and placeholders are 7/15/12. Public validator v9 and outer manifest v4 now bind the predecessor state; root must generate validator v10 and outer manifest v5 for this current state. All `semantic`, `citation`, `implementation`, `pilot`, `results`, `release`, and `whole-manuscript` gates remain false.

## 2026-08-25 P1 repeat-count planning successor

The current P1 manuscript 179 SHA256 is `A84135E7748512B28EF6F36600A10B7BAF5B96498FBA56798C48AF7A9AB7CF66`. Its current inventory is `audit_artifacts/p1_nrep_current_inventory_v4.json`, SHA256 `5D87CEB47E213F39C3BCFBC3E2AED1A66203A6C48B1B66BA13C9465BFAA05AAB`, with 782 units. Its route is `audit_artifacts/p1_nrep_current_route_v1.json`, SHA256 `6A29FA0FAC1E8DCD5FB59A5691AD18B60B7AF8B0B64A74505449FDDDE0BA30F7`. Root validation `audit_artifacts/p1_nrep_root_validation_v1.json`, SHA256 `E536837EC1C267A4B11E300FB0CBEC9BA4458F84096C9444E86806C099EB3D12`, passes 25/25 checks. All 764 predecessor units are covered, all 782 current units are reached, and 754 units outside the authorized scope remain exact and ordered.

Johnson et al. 2015 supports only simulation-based GLMM power, average interval-width planning and calibration diagnostics. P1-specific hierarchy, pairing, Holm family, simultaneous Monte Carlo gates, failures and reruns remain author protocols. The 23-sentence map SHA256 is `7A5829A66EF07528695139435D961C0CD21FB455FF684D739995E7D09AACCDAB`. Numeric inputs, simulation code, pilot, resets and release remain open.

P1 now has 51 references and 6 placeholders. The next P1 debt is P1-U0670 in P1-P0159, line 371. P2 and P3 remain at 1035 and 737 units, so current totals are 782/1035/737 units, 51/70/48 references and 6/15/12 placeholders. Use root review plus at most one targeted independent stream by default; add more streams only for distinct evidence objects or an actual conflict. All full gates remain false.

## 2026-08-25 P1 count-model family and failure-gate successor

The current P1 manuscript 179 SHA256 is `53FFA608A4C2314F19E798606FBA415ED51ABD23CDE1D26B9BCAAD8F51A9D1A2`. Its current inventory is `audit_artifacts/p1_u0670_current_inventory_v1.json`, SHA256 `37652152F396AF781D61F1F906189784A803DED8C6EAF55B87DD925C8BA2DA79`, with 791 units. Root writeback audit `audit_artifacts/debt_review_2026_08_25/p1_u0670_model_family_root_writeback_audit_v1.md`, SHA256 `1DA2F04FA0BC0720AEFA2A51257B49F84F0088952582BCCA02C52C706DAF7159`, records the direct-original comparison and the single targeted review.

Johnson 2015 supports the general binomial, Poisson, and negative-binomial GLMM family and explicit overdispersion modeling. Guo 2020 is an adjacent ISR application only. Venkatesh et al. 2023 supports theory- and variance-grounded multilevel adoption plus convergence and cluster-identification cautions. None defines P1's exact indices, calibration gates, negative-binomial parameterization, response-scale standardization, or failure actions.

Do not restore an automatic GEE or marginal-model fallback. The primary estimand is rejected if the repository random effect is unidentifiable or any frozen design, fit, or calibration gate fails. A repository fixed-effect model is descriptive for observed repositories only. The response-scale expected-count difference must integrate over the fitted random-effect distribution under frozen target weights and must not be replaced by a log-scale coefficient.

P1 now has 53 references and 5 placeholders. The next P1 debt is current P1-U0689 on the cluster-bootstrap conditions. P2 and P3 remain at 1035 and 737 units, so current totals are 791/1035/737 units, 53/70/48 references and 5/15/12 placeholders. Future sub-agents must receive this checkpoint and the canonical ledgers 163, 164, 165, 168, 172, and 175. Use root review plus at most one targeted independent stream by default. All full gates remain false.

## 2026-08-25 P1 open-citation-debt closed successor

The current P1 manuscript 179 SHA256 is `A5CCCFC284AEB6E7A6340349991BEC0B7CCEF5D16EFF77BCF083A8128C78C769`. Its current inventory is `audit_artifacts/p1_open_citation_debt_closed_current_inventory_v1.json`, SHA256 `B9782525CD0B37839530BB486C22E16D8090E6CD723CAD30EFB9E273EA79229F`, with 817 units. The combined root audit is `audit_artifacts/debt_review_2026_08_25/p1_open_citation_debt_final_root_writeback_audit_v1.md`, SHA256 `F4B4F4BCE0B56C904A7ADDC613230F0467DB049CA2AF017A3516C851F3B6F1DD`.

P1 now has 60 references and zero literal citation placeholders. This does not close implementation or pilot responsibilities for encoder checkpoints, projection data, calibration gates, operation templates, visual legibility, cluster simulation, negative-control execution, or result provenance. Never report P1 as experimentally or wholly complete from placeholder retirement.

The current three-paper denominator is 817/1035/737 units. References are 60/70/48 and placeholders are 0/15/12. Continue with root direct work on P2 and P3. Do not launch multiple parallel reviewers for adjacent placeholders. At most one targeted independent stream is allowed only for a different evidence object or a real conflict, and it must receive ledgers 163, 164, 165, 168, 172, and 175 plus the exact current manuscript hash. All semantic, citation, implementation, pilot, results, release and whole-manuscript gates remain false.

## 2026-08-25 Three-paper literal citation debt closed successor

The current P2 manuscript 182 SHA256 is `40E7254E40DAC0E0B7D2E63FFF22F3D7D1467CC51996D06B96873D35AC385479`. Its current inventory is `audit_artifacts/p2_open_citation_debt_closed_current_inventory_v1.json`, SHA256 `2A522FD7925DB76F2AA2A626E4A1E09F229ECE34304C2C45A8F4A1A2306596BA`, with 1068 units. The current P3 manuscript 183 SHA256 is `1562E49E54ED362E05CBD32F243F3F53E55DBB767E1294514623F7F040716B4B`. Its current inventory is `audit_artifacts/p3_open_citation_debt_closed_current_inventory_v1.json`, SHA256 `55F7EA1EB144EF46BDFAEE7DEE3B41644B19851A037416C64A968C716589E75C`, with 762 units.

The combined root audit is `audit_artifacts/debt_review_2026_08_25/p2_p3_open_citation_debt_final_root_writeback_audit_v1.md`, SHA256 `1FA33504F889504DB547918BD00DC8816363D2CE47C4BEEB5CD060DE7094FB1B`. The three-paper reference audit is `audit_artifacts/reference_coverage_three_paper_open_citation_debt_closed_v1.json`, SHA256 `D9DC7BC4E9D91E80910C99BD8300B8E436E53B1046F3B674131651560094D49A`. The series audit is `audit_artifacts/series_consistency_three_paper_open_citation_debt_closed_v1.json`, SHA256 `3F5DFD993D847270F43B9D3113685B11DE160545A647F3F70CEEEB2332831BAE`.

Current P1/P2/P3 totals are 817/1068/762 units, 60/79/54 references and 0/0/0 literal citation placeholders. Do not interpret placeholder retirement as full citation support, implementation, pilot, result or release completion. The Zhang, Shi, and Connelly 2024 edge remains official-abstract-only. P2 construct validation, P2 multimodal implementation, P3 restoration, P3 branch support, P3 statistical calibration and all executable artifacts remain open.

Future work should be root direct by default. Spawn at most one targeted independent stream only for a distinct evidence object or a real unresolved conflict. Any such package must include ledgers 163, 164, 165, the paper-specific ledger 168, 169 or 170, ledgers 172 and 175, the exact current manuscript hash, rejected source-role upgrades and acceptance criteria. All semantic, citation, implementation, pilot, results, release and whole-manuscript gates remain false.

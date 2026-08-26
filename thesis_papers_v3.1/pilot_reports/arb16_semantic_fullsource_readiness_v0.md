# ARB16 完整源码就绪审计 v0

## 审计结论

状态为 **`READY_FOR_SEMANTIC_INDEX_BUILD`**。冻结 reserve 中 16/16 个 base-commit snapshot 均可从本地 bare Git object store 读取，完整 Python blob 与 query path 通过预注册的源码可读性检查。该状态**只授权构建与校验 semantic index**；本次运行是源码锁与解析 readiness，不是语义机制实验，也不通过 `MECHANISM-PROCEED`、`MODEL-PROCEED` 或 `CHAPTER-GO`。

本次审计的实验接触面固定为：**0 gold / 0 qrel、0 retrieval scoring、0 program evaluation、0 training**。

## 冻结输入与哈希

| 工件 | SHA256 | 作用 |
| --- | --- | --- |
| `pilot_manifests/arb16_semantic_fullsource_reserve_v0.json` | `99E86EB181249CF1F91C944ED0F178F3F4332CA314F03468765B2535ADEDF212` | query/gold-blind 的 16 题、16 snapshot 冻结 reserve；原授权仅为取得并哈希核验完整源码 |
| `pilot_assets/arb-semantic-sources/locks/arb16_fullsource_blobs_v0.jsonl` | `96751292475DB1D6B143017375367DCFB6871764CBCBAF792C280D1910291EC1` | 24,668 条 snapshot×path 源码锁记录，含 Git OID、独立 SHA256、字节数与 Python parse 状态 |
| `pilot_reports/arb16_semantic_fullsource_readiness_v0.json` | `DE53103C2DB6D89D35C41BE00BB6D888BA73EFD3E317B7581761809EF2EAE337` | 本报告所依据的机器可读 readiness 汇总与逐 snapshot 结果 |

reserve 覆盖 5 个仓库：`fastapi/fastapi`、`huggingface/diffusers`、`huggingface/transformers`、`pytest-dev/pytest` 各 2 个 snapshot，`pallets/click` 8 个 snapshot；没有复用 Stage-0 ARB60 已见 snapshot。

## 可复核结果

| 检查项 | 结果 | 判定 |
| --- | ---: | --- |
| manifest / 已核验 snapshot | 16 / 16 | 全部到位 |
| 仓库数 | 5 | 与冻结 reserve 一致 |
| snapshot×path file rows | 24,668 | 每行均记录 Git OID 与独立 SHA256 |
| 跨 snapshot 去重 blob objects | 13,421 | 全部从 Git object store 实读 |
| 去重 blob bytes | 209,590,988 | 约 199.88 MiB；不是截断 release chunk 字节数 |
| Python file rows / AST parsed | 15,230 / 15,230 | 100%；高于冻结的 99% readiness 门槛 |
| query paths present | 全部通过 | 16/16 snapshot 无 missing query path |
| query-path Python AST | 全部通过 | 16/16 snapshot 的 query path 均从完整 blob 解析 |

`file rows` 与 `Python file rows` 是 snapshot×path 计数；同一 blob 在多个 snapshot 出现时会重复成行。13,421 与 209,590,988 分别是按仓库 object store 去重后实际读取的 blob 数与字节数，不能与前两项混写。

验证器只读取冻结 reserve 和本地 bare Git object store：先核验 commit object，使用 `git ls-tree` 枚举完整 tree，再以 `git cat-file --batch` 读取 blob；每个 blob 另算 SHA256，`.py` blob 使用 Python 标准库 AST 从完整字节解析。机器报告中的 readiness 条件为：snapshot 数与 manifest 一致、所有 query path 存在、所有 query-path Python AST 可用，且总体 Python AST parse rate 不低于 99%。

## 授权边界

本结果清除了“发布 chunks 不能恢复完整源码”这一**资产阻塞**，因此下一步可以在上述锁定 blob 上构建静态 semantic index，并做不读取 gold 的索引完整性与 witness 校验。它没有产生或验证 call/import/test/dependency 边，也没有验证 refinement type、义务闭合、深度必要性、wrong-entity/rewiring 拒绝、PyRAG-style 差额、canonical BCY 或外部 patch success。

因此当前仍然禁止：读取 gold/qrel 后调试索引或程序、任何 retrieval/program 评分、任何训练标签生成或模型训练，以及把 source readiness 写成机制证据。只有 semantic index 本身完成并经过 query-only 完整性审计后，才可依 `00D`/`00E` 的下一道显式门另行决定是否冻结程序输出并开启评分；本报告本身不扩大授权。

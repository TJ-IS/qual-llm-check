# Programming systematic literature review

本目录保存“人或智能体直接编程”系统文献综述的检索、题录初筛、全文复核和综合分析。正式方法依据见 `method_reference_crosswalk.md`；冻结协议见 `search_protocol_v2.md`。

## 阅读入口

- `systematic_literature_review_interim_results.md`：方法依据、检索流量、筛选结果、文献迁移和当前限制的完整阶段性报告；
- `local_fulltext_human_adjudication.md`：31 篇本地可得全文的人工裁决，包含对模型边界误判的修正；
- `title_abstract_screening_results.md`：5,642 条题录的两阶段筛选统计；
- `two_pass_human_ai.md`：214 条两轮一致的 human–AI 直接编程候选。

## 方法与审计文件

- `method_reference_crosswalk.md`：MISQ、ISR、JAIS、JMIS 原文做法、逐项模仿与差异；
- `search_protocol_v2.md`：正式冻结的一条主检索式、渠道和 eligibility criteria；
- `source_scope_rationale.md`：预设来源分组与选择理由；
- `search_recall_audit.md`：28 条本地记录和 33 条近期施引候选的召回审计；
- `calibration_report.md`：20 条核心/8 条边界已知记录的提示词校准；
- `protocol_compliance_checklist.md`：原文要求对应的完成/待办状态；
- `fulltext_codebook.md`：最终纳入和 concept matrix 字段；
- `identification_pool_analysis.md`：5,642 条去重识别池的年份、来源与渠道分布。

## 当前数据

- `input/scopus_authoritative_4981.csv`：2026-07-26 从 Scopus 导出的权威来源主检索结果。
- `../../runs/ref_20_coding.csv`：20 篇核心种子的 807 条 Scopus 施引记录。
- `../direct_programming_research_deepseek_analysis/output_v1/direct_programming_matches.csv`：本地全文筛选得到的 28 条种子/边界记录。

## 可续跑命令

```powershell
python .\runs\programming_systematic_literature_review\prepare_inputs.py
python .\runs\programming_systematic_literature_review\analyze_title_abstract_batch.py --config .\runs\programming_systematic_literature_review\config_batch_lean.json --batch-size 16 --max-concurrency 12
python .\runs\programming_systematic_literature_review\prepare_stage2_inputs.py
python .\runs\programming_systematic_literature_review\analyze_title_abstract_batch.py --config .\runs\programming_systematic_literature_review\config_stage2_batch.json --batch-size 16 --max-concurrency 12
python .\runs\programming_systematic_literature_review\build_title_abstract_report.py
python .\runs\programming_systematic_literature_review\prepare_local_fulltexts.py
python .\runs\programming_systematic_literature_review\analyze_fulltext_candidates.py --max-concurrency 8
```

正式题录筛选逐条追加到 `output_stage1_batch_v2/decisions.jsonl`，同一提示词指纹下重复执行会从断点继续。题录阶段只抽取相关性、主体、制品、行动和短证据；方法、层级、理论与变量留到全文阶段。批量调用仍逐篇保存；任何遗漏、重复或非法 `record_id` 都会使整批失败并留待重试。`output_stage1_batch_v1` 保留较重但未完成的旧版运行，不与 v2 结果混合。

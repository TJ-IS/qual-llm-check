# 跨篇 Master Split Registry

## 当前状态

本登记表是三篇正式数据采集前必须填写并签名的只增不改工件。当前状态为 `UNALLOCATED_NO_DATA_COLLECTION`。这表示三篇研究设计已经规定互斥规则，但尚未声称任何 repository family 已被实际分配，也不声称已经获得跨篇独立实证。任何候选生成、任务卡评分、bundle 执行、行为轨迹或确认性结果解封之前，必须把本文件复制为带日期和哈希的冻结版本并填入实际记录。

## 规范实体键

每条任务记录的主键为 `(canonical_upstream, repository_family, base_commit, normalized_issue_hash)`。`repository_family` 由 fork、mirror、同源包、共享提交祖先、规范包名和源码近重复项目的传递闭包确定。任务级近重复还使用 issue、patch hunk、AST edit、test 与 gold-context hash 建边。family 合并程序、阈值、人工裁决和版本必须在任何任务 outcome 可见前冻结。

## 必填字段

| 字段 | 责任 |
|---|---|
| registry_version | 只增不改版本与父版本哈希 |
| canonical_upstream | 规范上游仓库标识 |
| repository_family | 跨 fork、mirror 与近重复的家族 ID |
| base_commit | 基础提交哈希 |
| normalized_issue_hash | 规范化任务描述哈希 |
| dataset_release | 数据集、版本与快照哈希 |
| first_public_time | issue、PR、patch 与 tests 首次公开时间 |
| paper_id | P1、P2 或 P3 |
| role | pilot、train、development、calibration、confirmatory、temporal-test、auxiliary-only |
| window | 论文内预注册时间窗 |
| container_hash | 镜像、依赖锁与 evaluator 哈希 |
| preprocessing_hash | parser、candidate、manifest 与 tokenizer 哈希 |
| checkpoint_cutoff | 冻结 agent/repairer 可知信息截止时间 |
| status | allocated、excluded、shared-development 或 global-sealed |
| exclusion_reason | 排除、冲突或降级理由 |
| append_time | 追加时间，不覆盖旧记录 |

## 预注册分配责任

| 研究 | 主角色 | 不得与之共享 family 的角色 | 当前状态 |
|---|---|---|---|
| P1 | 机制训练、开发、联合仓库—时间 OOD | P2/P3 的 pilot、train、development、calibration、confirmatory、temporal-test | 未分配 |
| P2 | bundle 设计训练、效应验证、联合时间—仓库 OOD | P1/P3 的全部学习与确认角色 | 未分配 |
| P3 | W1、W2、W3a、W3b，且四窗两两 family 互斥 | P1/P2 的全部学习与确认角色 | 未分配 |

同一 family 一旦进入任一篇的 confirmatory 或 temporal-test，立即标记 `global-sealed`。训练基础设施可以复用，但 checkpoint、calibrator、任务卡、bundle 结果、轨迹、补丁、测试、manifest 标签和 outcome 不得跨篇传递。确因样本不足而复用的 family 只能标记 `shared-development`，三篇可各自报告不同端点，但系列汇总只算一个相关 family cluster。

## 开工门

正式开工需要同时满足以下条件：实际 family 列表已经填入；三篇分配无主键或 family 冲突；所有数据快照、时间窗、checkpoint cutoff 和容器哈希均非空；冲突检查脚本输出为零；registry 文件、冲突报告和分配摘要均已签名并记录 SHA-256。在此之前，三篇只能称研究设计与 pilot 方案，不能称已获得独立系列证据。

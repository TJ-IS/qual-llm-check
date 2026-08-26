# Master Split Registry

Status: `UNALLOCATED_NO_DATA_COLLECTION`

在任何候选、轨迹、状态卡、补丁、运行观测或终端结果生成前，本表按仓库家族登记三篇的数据角色。规范键为 `(canonical_upstream, repo_family_id, base_commit, normalized_issue_hash)`。仓库家族由 upstream、fork/mirror、共享提交祖先、规范包名和源码近重复关系形成传递闭包。

| entity_key | dataset_release | timestamp | paper_id | role | code_hash | data_hash | container_hash | exclusion_reason |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

角色取值为 `pilot`、`train`、`development`、`calibration`、`confirmatory`、`temporal_test` 或 `auxiliary_only`。确认与时间外测试仓库家族在三篇之间互斥；共享基础设施记录版本，不共享训练标签、checkpoint、状态卡、补丁或运行结果。

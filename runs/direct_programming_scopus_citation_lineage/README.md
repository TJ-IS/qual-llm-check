# Scopus citation lineage
目标：使用 20 篇核心人类编程研究的 Scopus EID，检索全部施引文献，分析其年代、主题、期刊、研究方法和向现代编程智能体研究的延续关系。
## 当前状态
- 已完成：20/20 个 EID 通过 DOI 与本地 Scopus 导出库精确匹配。
- 已完成：用新版 Scopus `REFEID` 运行 20 种子组合检索，得到 807 条 EID 唯一的记录。
- 已完成：归档原始 CSV，核验 DOI、同题版本、种子自身记录、年代、来源、AIS/Basket 11 分布和重叠主题。
- 已完成：逐条复核 2020 年以后 AI+编程候选，识别 4 篇直接连接现代 LLM/编程助手的文献。
- 限制：CSV 未包含 References 字段，暂时不能恢复逐篇“种子—施引文献”边矩阵。
## 文件
- `seed_articles.csv`：20 篇种子论文、DOI、EID、本地 cited-by 计数和主题。
- `scopus_queries.md`：可直接粘贴进 Scopus Advanced Search 的检索式。
- `scopus_citing_20_seed_807_raw.csv`：Scopus 原始导出副本。
- `analyze_scopus_lineage.py`：可复现的元数据分析脚本。
- `analysis_summary.json`：脚本生成的完整统计与候选记录。
- `citation_lineage_analysis.md`：中文分析报告。

# AIS Basket 文献综述检索来源分析
目标：从本地 AIS Basket 全文库中筛出高置信度综述/元分析，审计其构造文献样本时实际使用的数据库、数字图书馆、限定期刊/会议集合与追引方法，为编程情境文献综述设计可复现的检索流程。
## 已完成
- 93 篇高置信度候选全文全部审计完成，83 篇被确认是真正综述，失败 0。
- `output_v1/summary.json` 汇总检索策略、数据库、权威集合和追引方法。
- `literature_review_search_design.md` 给出基于本地证据的推荐检索协议。
- `evaluate_programming_search_query.py` 在 Basket 11 元数据上校准编程检索词，并与既有 28 篇直接编程样本比较召回率。
## 准备 93 篇候选全文
```powershell
$env:PYTHONIOENCODING='utf-8'
& '.\.venv\Scripts\python.exe' -B '.\runs\literature_review_search_sources_analysis\prepare_review_corpus.py'
```
## 小样本校准
```powershell
$env:PYTHONIOENCODING='utf-8'
& '.\.venv\Scripts\python.exe' -B '.\runs\literature_review_search_sources_analysis\analyze_review_sources.py' --limit 5 --max-concurrency 5
```
## 全量运行
```powershell
$env:PYTHONIOENCODING='utf-8'
& '.\.venv\Scripts\python.exe' -B '.\runs\literature_review_search_sources_analysis\analyze_review_sources.py' --max-concurrency 8
```
结果逐篇追加到 `output_v1/decisions.jsonl`，中断后运行同一命令即可续传。`formal_reviews.jsonl` 只保留模型确认真正实施了文献综述的论文，`summary.json` 汇总检索策略与来源频次。

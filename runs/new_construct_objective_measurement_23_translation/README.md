# 23 篇新构念客观测量文献：英中逐段翻译

本目录独立保存 DeepSeek 初筛命中的 23 篇文章，不修改原始数据库全文，也不与旧分析输出混合。

## 目录

- `source_en/`：23 篇英文 Markdown 全文副本。
- `bilingual_zh/`：逐段英中交替的翻译结果。
- `.progress/`：逐段检查点。运行中断后保留，不要删除。
- `translate_fulltext_bilingual.py`：从项目根目录的 `translate_csv_zh.py` 改造而来的全文翻译脚本。
- `combine_bilingual_fulltexts.py`：将 23 篇双语全文按编号拼接为一个 Markdown 文件。
- `all_23_bilingual_fulltexts.md`：带目录和文章分隔的中英逐段全文合集。
- `translation_summary.json`：每次运行结束后生成的文件级汇总。

每个输出段落采用以下顺序，不添加 EN/ZH 标签：

```markdown
English paragraph.

中文段落。
```

## 小量测试

从项目根目录运行：

```powershell
$env:PYTHONIOENCODING = 'utf-8'
& '.\.venv\Scripts\python.exe' -B '.\runs\new_construct_objective_measurement_23_translation\translate_fulltext_bilingual.py' --limit-files 1 --max-workers 1
```

## 全量运行

```powershell
$env:PYTHONIOENCODING = 'utf-8'
& '.\.venv\Scripts\python.exe' -B '.\runs\new_construct_objective_measurement_23_translation\translate_fulltext_bilingual.py' --max-workers 2
```

脚本在每个段落成功后立即更新检查点。中断或网络错误后再次执行同一条命令即可续传；已经生成完整双语文件的文章会直接跳过。`--force` 会忽略已有输出和检查点，从头翻译，不建议在正常续传时使用。

Google Translate 对单次文本长度有限制。脚本默认将超过 4200 个字符的段落优先按句号、分号、换行或空格切块，再合并中文结果。

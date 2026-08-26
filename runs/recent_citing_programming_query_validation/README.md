# Recent citing-paper programming query validation

This run screens the 176 Scopus records from 2021–2026 that cite at least one of
the 20 manually confirmed AIS Basket programming studies. It uses title,
abstract, and keywords only, so its positive labels identify records for
full-text review rather than final inclusion.

```powershell
$env:PYTHONIOENCODING = 'utf-8'
& '.\.venv\Scripts\python.exe' -B '.\runs\recent_citing_programming_query_validation\prepare_inputs.py'
& '.\.venv\Scripts\python.exe' -B '.\runs\recent_citing_programming_query_validation\analyze_recent_citations.py' --max-concurrency 12
```

The analysis is resumable through `output_v1/decisions.jsonl`.

## Completed outputs

- `output_v1/decisions.csv`: all 176 metadata-screening decisions.
- `output_v1/candidates.csv`: 30 likely-direct and 3 possible-direct records.
- `query_recall_evaluation.json`: recall back-test for six query variants.
- `recent_query_match_matrix.csv`: record-level query hits and screening labels.
- `recent_citing_query_validation_report.md`: Chinese audit report, candidate titles,
  back-test results, and four recommended Scopus query blocks.

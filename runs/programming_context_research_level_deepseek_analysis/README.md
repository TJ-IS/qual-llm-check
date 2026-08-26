# Programming Context Research-Level Classification

This independent second pass sends only the 264 prior programming-context matches to `deepseek-v4-pro`. It classifies the primary research level from the article's research questions, theoretical relationships, principal outcomes, aggregation, and actual unit of analysis. It does not infer an individual level merely from individual respondents or developer-level raw data.

The run is resumable through `output_v1/decisions.jsonl`. It writes:

- `research_level_decisions.csv`: the second-pass decisions only;
- `programming_context_matches_with_research_level.csv`: all original columns plus the research-level columns;
- `summary.json`: completion, level counts, and token usage.

## Dry run

```powershell
$env:PYTHONIOENCODING = 'utf-8'
& '.\.venv\Scripts\python.exe' -B '.\runs\programming_context_research_level_deepseek_analysis\analyze_research_level.py' --dry-run
```

## Full run

```powershell
$env:PYTHONIOENCODING = 'utf-8'
& '.\.venv\Scripts\python.exe' -B '.\runs\programming_context_research_level_deepseek_analysis\analyze_research_level.py' --max-concurrency 12
```

Re-running the same command resumes completed records with the current prompt fingerprint.

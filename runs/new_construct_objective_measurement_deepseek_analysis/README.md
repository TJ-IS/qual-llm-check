# New Construct + Objective Measurement Screening

This run is independent from `runs/construct_fulltext_deepseek_analysis`. It screens Otero full texts for papers that both:

1. explicitly claim to develop, introduce, or propose a new named IS construct; and
2. objectively measure that same new construct using non-questionnaire evidence.

The prompt distinguishes a genuinely new construct from a new scale, index, proxy, or measurement method for an existing construct. Strict objective evidence includes logs, archival or administrative records, transactions, observable behavior, sensors, and reproducible computational measures. Subjective supervisor or expert ratings are separated as rater-based evidence.

## Commands

Dry run:

```powershell
$env:PYTHONIOENCODING = 'utf-8'
& '.\.venv\Scripts\python.exe' -B '.\runs\new_construct_objective_measurement_deepseek_analysis\analyze_fulltext.py' --dry-run --limit 3
```

Full resumable run:

```powershell
$env:PYTHONIOENCODING = 'utf-8'
& '.\.venv\Scripts\python.exe' -B '.\runs\new_construct_objective_measurement_deepseek_analysis\analyze_fulltext.py'
```

Successful records are appended immediately to `output/decisions.jsonl`. Re-running the same command skips records completed under the current prompt fingerprint and retries unfinished or failed articles.

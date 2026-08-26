# Direct Programming Research Screening

This third pass sends only the 264 broad programming-context matches to `deepseek-v4-pro`. It applies a strict substitution test to retain papers that study programming actions, cognition, technical methods, tools/languages, education tasks, or code artifacts as indispensable research objects. General developer, team, project, organization, community, and market studies are excluded even when programming terminology or commit data appear.

The run is resumable through `output_v1/decisions.jsonl`. Main outputs:

- `direct_programming_decisions.csv`: all 264 strict decisions;
- `direct_programming_matches.csv`: strict true matches only;
- `programming_context_264_with_direct_programming.csv`: prior columns plus strict-screening fields;
- `summary.json`: completion and category counts.

```powershell
$env:PYTHONIOENCODING = 'utf-8'
& '.\.venv\Scripts\python.exe' -B '.\runs\direct_programming_research_deepseek_analysis\analyze_direct_programming.py' --max-concurrency 12
```

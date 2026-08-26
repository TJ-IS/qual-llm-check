from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
ROOT = RUN_DIR.parents[1]
INPUT_DIR = ROOT / "database_fulltext_all"
OUTPUT_DIR = RUN_DIR / "output_v1"
DECISIONS = OUTPUT_DIR / "decisions.jsonl"
SUMMARY = OUTPUT_DIR / "summary.json"
REPORT = OUTPUT_DIR / "validation_report.json"


def main() -> None:
    input_files = sorted(path.name for path in INPUT_DIR.glob("*.md"))
    records = []
    parse_errors = []
    with DECISIONS.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                records.append(json.loads(line))
            except Exception as exc:
                parse_errors.append({"line": line_number, "error": str(exc)})

    source_files = [record["source_file"] for record in records]
    record_ids = [record["record_id"] for record in records]
    duplicate_source_files = sorted(name for name, count in Counter(source_files).items() if count > 1)
    duplicate_record_ids = sorted(name for name, count in Counter(record_ids).items() if count > 1)
    missing_source_files = sorted(set(input_files) - set(source_files))
    unexpected_source_files = sorted(set(source_files) - set(input_files))

    logical_violations = []
    prompt_fingerprints = Counter()
    models = Counter()
    gate_counts = Counter()
    centrality_counts = Counter()
    retained_layers = Counter()
    paradigms = Counter()
    usage = Counter()
    strict_match_count = 0
    for record in records:
        gates = record["gates"]
        strict_expected = all(gates.values()) and record["objective_metric_centrality"] in {
            "exclusive",
            "dominant",
        }
        if record["strict_objective_improvement_match"] != strict_expected:
            logical_violations.append(
                {
                    "record_id": record["record_id"],
                    "source_file": record["source_file"],
                    "strict_reported": record["strict_objective_improvement_match"],
                    "strict_expected": strict_expected,
                }
            )
        strict = bool(record["strict_objective_improvement_match"])
        strict_match_count += int(strict)
        for gate, value in gates.items():
            gate_counts[gate] += int(bool(value))
        centrality_counts[record["objective_metric_centrality"]] += 1
        if strict:
            retained_layers[record["solution_layer"]] += 1
            paradigms.update(record["research_paradigms"])
        prompt_fingerprints[record["prompt_fingerprint"]] += 1
        models[record["model"]] += 1
        for key, value in record.get("usage", {}).items():
            usage[key] += int(value or 0)

    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    recomputed = {
        "input_fulltexts": len(input_files),
        "completed": len(records),
        "pending": len(input_files) - len(records),
        "strict_match_count": strict_match_count,
        "strict_nonmatch_count": len(records) - strict_match_count,
        "gate_true_counts": dict(gate_counts),
        "centrality_counts": dict(centrality_counts),
        "retained_solution_layer_counts": dict(retained_layers),
        "retained_research_paradigm_counts": dict(paradigms),
        "usage": dict(usage),
    }
    summary_mismatches = {}
    for key, value in recomputed.items():
        if summary.get(key) != value:
            summary_mismatches[key] = {"summary": summary.get(key), "recomputed": value}

    with (OUTPUT_DIR / "decisions.csv").open("r", encoding="utf-8-sig", newline="") as handle:
        csv_data_rows = sum(1 for _ in csv.reader(handle)) - 1

    retained_markdown = (OUTPUT_DIR / "retained_articles.md").read_text(encoding="utf-8")
    retained_markdown_entries = retained_markdown.count("\n## ")

    checks = {
        "jsonl_parses": not parse_errors,
        "record_count_matches_input": len(records) == len(input_files),
        "source_files_unique": not duplicate_source_files,
        "record_ids_unique": not duplicate_record_ids,
        "all_input_files_covered": not missing_source_files and not unexpected_source_files,
        "strict_gate_logic_valid": not logical_violations,
        "single_prompt_fingerprint": len(prompt_fingerprints) == 1,
        "single_model": len(models) == 1,
        "summary_matches_recomputation": not summary_mismatches,
        "csv_row_count_matches": csv_data_rows == len(records),
        "retained_markdown_count_matches": retained_markdown_entries == strict_match_count,
    }
    report = {
        "all_checks_passed": all(checks.values()),
        "checks": checks,
        "counts": {
            "input_fulltexts": len(input_files),
            "decision_records": len(records),
            "strict_matches": strict_match_count,
            "strict_nonmatches": len(records) - strict_match_count,
            "csv_data_rows": csv_data_rows,
            "retained_markdown_entries": retained_markdown_entries,
        },
        "prompt_fingerprints": dict(prompt_fingerprints),
        "models": dict(models),
        "parse_errors": parse_errors,
        "duplicate_source_files": duplicate_source_files,
        "duplicate_record_ids": duplicate_record_ids,
        "missing_source_files": missing_source_files,
        "unexpected_source_files": unexpected_source_files,
        "logical_violations": logical_violations,
        "summary_mismatches": summary_mismatches,
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    raise SystemExit(0 if report["all_checks_passed"] else 1)


if __name__ == "__main__":
    main()

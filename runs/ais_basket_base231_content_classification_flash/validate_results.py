#!/usr/bin/env python3
"""Validate the completed content-classification run."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import run_classification as runner


RUN_DIR = Path(__file__).resolve().parent


def main() -> None:
    config = runner.load_config()
    source_candidates = runner.load_source_candidates(
        runner.resolve_from_run(str(config["source_decisions"]))
    )
    output_dir = runner.resolve_from_run(str(config["output_dir"]))
    system_prompt = (RUN_DIR / config["prompt_files"]["system"]).read_text(encoding="utf-8").strip()
    user_template = (RUN_DIR / config["prompt_files"]["user_template"]).read_text(encoding="utf-8").strip()
    fingerprint = runner.prompt_fingerprint(config, system_prompt, user_template)

    rows = []
    invalid_rows = []
    with (output_dir / "decisions.jsonl").open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            try:
                if row.get("prompt_fingerprint") != fingerprint:
                    raise ValueError("prompt fingerprint mismatch")
                runner.validate_decision(row, str(row.get("record_id") or ""))
                expected = source_candidates[str(row.get("source_file") or "")]
                if row.get("source_theory_guided_subset_match") != expected["source_theory_guided_subset_match"]:
                    raise ValueError("source theory-subset flag mismatch")
            except Exception as exc:
                invalid_rows.append({"line": line_number, "error": str(exc)})
            rows.append(row)

    source_counts = Counter(str(row.get("source_file") or "") for row in rows)
    record_counts = Counter(str(row.get("record_id") or "") for row in rows)
    actual_sources = set(source_counts)
    expected_sources = set(source_candidates)
    duplicate_sources = sorted(source for source, count in source_counts.items() if count > 1)
    duplicate_record_ids = sorted(record for record, count in record_counts.items() if count > 1)

    unresolved_errors = set()
    resolved_error_rows = []
    errors_path = output_dir / "errors.jsonl"
    if errors_path.exists():
        with errors_path.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                error = json.loads(line)
                if error.get("prompt_fingerprint") != fingerprint:
                    continue
                source = str(error.get("source_file") or "")
                if source in actual_sources:
                    resolved_error_rows.append(line_number)
                else:
                    unresolved_errors.add(source)

    report = {
        "valid": not any(
            [
                invalid_rows,
                duplicate_sources,
                duplicate_record_ids,
                expected_sources - actual_sources,
                actual_sources - expected_sources,
                unresolved_errors,
            ]
        ),
        "prompt_fingerprint": fingerprint,
        "expected_candidates": len(expected_sources),
        "decision_rows": len(rows),
        "unique_source_files": len(actual_sources),
        "unique_record_ids": len(record_counts),
        "theory_subset_flags_true": sum(
            row.get("source_theory_guided_subset_match") is True for row in rows
        ),
        "missing_sources": sorted(expected_sources - actual_sources),
        "unexpected_sources": sorted(actual_sources - expected_sources),
        "duplicate_sources": duplicate_sources,
        "duplicate_record_ids": duplicate_record_ids,
        "invalid_rows": invalid_rows,
        "unresolved_error_sources": sorted(unresolved_errors),
        "resolved_error_rows": resolved_error_rows,
        "attempt_counts": dict(sorted(Counter(str(row.get("attempts")) for row in rows).items())),
        "function_total": sum(Counter(row["primary_artifact_function"] for row in rows).values()),
        "objective_total": sum(Counter(row["primary_objective_family"] for row in rows).values()),
        "context_total": sum(Counter(row["application_context"] for row in rows).values()),
    }
    (output_dir / "validation_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

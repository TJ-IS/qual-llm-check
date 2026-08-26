#!/usr/bin/env python3
"""Validate completeness and logical consistency of the completed screening run."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import run_screening as runner


RUN_DIR = Path(__file__).resolve().parent


def main() -> None:
    config = runner.load_config()
    input_dir = runner.resolve_from_run(str(config["input_dir"]))
    output_dir = runner.resolve_from_run(str(config["output_dir"]))
    year_from = int(config["year_range"]["from"])
    year_to = int(config["year_range"]["to"])
    scope_files = sorted(
        path
        for path in input_dir.glob("*.md")
        if (year := runner.year_from_filename(path)) is not None
        and year_from <= year <= year_to
    )
    system_prompt = (RUN_DIR / config["prompt_files"]["system"]).read_text(encoding="utf-8").strip()
    user_template = (RUN_DIR / config["prompt_files"]["user_template"]).read_text(encoding="utf-8").strip()
    fingerprint = runner.prompt_fingerprint(config, system_prompt, user_template)

    rows = []
    invalid_rows = []
    decisions_path = output_dir / "decisions.jsonl"
    with decisions_path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            try:
                if row.get("prompt_fingerprint") != fingerprint:
                    raise ValueError("prompt fingerprint mismatch")
                runner.validate_decision(row, str(row.get("record_id") or ""))
            except Exception as exc:
                invalid_rows.append({"line": line_number, "error": str(exc)})
            rows.append(row)

    source_counts = Counter(str(row.get("source_file") or "") for row in rows)
    record_counts = Counter(str(row.get("record_id") or "") for row in rows)
    duplicate_sources = sorted(name for name, count in source_counts.items() if count > 1)
    duplicate_record_ids = sorted(name for name, count in record_counts.items() if count > 1)
    expected_sources = {path.name for path in scope_files}
    actual_sources = set(source_counts)

    stale_error_rows = []
    unresolved_error_sources = set()
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
                    stale_error_rows.append(line_number)
                else:
                    unresolved_error_sources.add(source)

    base_rows = [row for row in rows if row.get("base_match") is True]
    theory_rows = [row for row in rows if row.get("theory_guided_subset_match") is True]
    report = {
        "valid": not any(
            [
                invalid_rows,
                duplicate_sources,
                duplicate_record_ids,
                expected_sources - actual_sources,
                actual_sources - expected_sources,
                unresolved_error_sources,
            ]
        ),
        "prompt_fingerprint": fingerprint,
        "scope_fulltexts": len(scope_files),
        "decision_rows": len(rows),
        "unique_source_files": len(actual_sources),
        "unique_record_ids": len(record_counts),
        "missing_sources": sorted(expected_sources - actual_sources),
        "unexpected_sources": sorted(actual_sources - expected_sources),
        "duplicate_sources": duplicate_sources,
        "duplicate_record_ids": duplicate_record_ids,
        "invalid_rows": invalid_rows,
        "unresolved_error_sources": sorted(unresolved_error_sources),
        "resolved_transient_error_rows": stale_error_rows,
        "base_match_count": len(base_rows),
        "theory_guided_subset_match_count": len(theory_rows),
        "attempt_counts": dict(sorted(Counter(str(row.get("attempts")) for row in rows).items())),
        "base_match_year_counts": dict(sorted(Counter(str(row.get("year")) for row in base_rows).items())),
        "theory_match_year_counts": dict(sorted(Counter(str(row.get("year")) for row in theory_rows).items())),
    }
    (output_dir / "validation_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

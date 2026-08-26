#!/usr/bin/env python3
"""Compact integrity and disagreement checks for the class audit."""

from __future__ import annotations

import json
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load(stage: str) -> list[dict]:
    path = ROOT / f"output_{stage}" / "decisions.jsonl"
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> None:
    audit_a = load("audit_a")
    audit_b = load("audit_b")
    by_source_b = {row["source_file"]: row for row in audit_b}
    disagreements = [
        row for row in audit_a
        if bool(row["class_level_include"]) != bool(by_source_b[row["source_file"]]["class_level_include"])
    ]
    print(f"A records={len(audit_a)} include={sum(bool(row['class_level_include']) for row in audit_a)}")
    print(f"B records={len(audit_b)} include={sum(bool(row['class_level_include']) for row in audit_b)}")
    print(f"disagreements={len(disagreements)}")
    for row in disagreements:
        other = by_source_b[row["source_file"]]
        print(f"{row['record_id']}\tA={row['class_level_include']}\tB={other['class_level_include']}\t{row['title']}")
    adjudications = load("adjudication")
    print(f"adjudications={len(adjudications)} expected={len(disagreements)}")
    if len(adjudications) != len(disagreements):
        raise SystemExit("adjudication count mismatch")
    csv_path = ROOT / "deliverables" / "class_audit_all_52.csv"
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        final_rows = list(csv.DictReader(handle))
    sources = [row["source_file"] for row in final_rows]
    print(f"final_rows={len(final_rows)} unique_sources={len(set(sources))}")
    print(f"final_include={sum(row['final_include'] == 'True' for row in final_rows)}")
    if len(final_rows) != 52 or len(set(sources)) != 52:
        raise SystemExit("final CSV integrity failure")
    error_lines = 0
    for stage in ("audit_a", "audit_b", "adjudication"):
        path = ROOT / f"output_{stage}" / "errors.jsonl"
        if path.exists():
            error_lines += sum(bool(line.strip()) for line in path.read_text(encoding="utf-8").splitlines())
    print(f"api_error_records={error_lines}")
    if error_lines:
        raise SystemExit("API errors present")


if __name__ == "__main__":
    main()

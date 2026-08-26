#!/usr/bin/env python3
"""Reconcile machine-readable screening artifacts without making a gold verdict."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


ID_COLUMNS = ("record_id", "paper_id", "id", "doi", "title")
DECISION_KEYS = ("decision", "label", "include", "status", "error")


def audit_jsonl(path: Path, max_bytes: int) -> dict[str, object]:
    result: dict[str, object] = {
        "path": str(path),
        "bytes": path.stat().st_size,
        "records": 0,
        "blank_lines": 0,
        "parse_errors": 0,
        "decision_key_presence": Counter(),
        "id_key_presence": Counter(),
        "blank_ids": 0,
        "duplicate_ids": 0,
        "unique_ids": 0,
    }
    if path.stat().st_size > max_bytes:
        result["skipped"] = "larger than --max-file-mb"
        result["decision_key_presence"] = {}
        result["id_key_presence"] = {}
        return result
    seen_ids: set[str] = set()
    with path.open("r", encoding="utf-8-sig") as handle:
        for line in handle:
            if not line.strip():
                result["blank_lines"] += 1
                continue
            result["records"] += 1
            try:
                value = json.loads(line)
            except json.JSONDecodeError:
                result["parse_errors"] += 1
                continue
            if isinstance(value, dict):
                for key in DECISION_KEYS:
                    if key in value:
                        result["decision_key_presence"][key] += 1
                id_key = next((key for key in ID_COLUMNS if key in value), None)
                if id_key:
                    result["id_key_presence"][id_key] += 1
                    identifier = str(value.get(id_key) or "").strip()
                    if not identifier:
                        result["blank_ids"] += 1
                    elif identifier in seen_ids:
                        result["duplicate_ids"] += 1
                    else:
                        seen_ids.add(identifier)
    result["decision_key_presence"] = dict(result["decision_key_presence"])
    result["id_key_presence"] = dict(result["id_key_presence"])
    result["unique_ids"] = len(seen_ids)
    return result


def audit_csv(path: Path, max_bytes: int) -> dict[str, object]:
    result: dict[str, object] = {
        "path": str(path),
        "bytes": path.stat().st_size,
        "records": 0,
        "columns": [],
        "id_column": None,
        "blank_ids": 0,
        "duplicate_ids": 0,
    }
    if path.stat().st_size > max_bytes:
        result["skipped"] = "larger than --max-file-mb"
        return result
    seen: set[str] = set()
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        result["columns"] = reader.fieldnames or []
        id_column = next((name for name in ID_COLUMNS if name in result["columns"]), None)
        result["id_column"] = id_column
        for row in reader:
            result["records"] += 1
            if id_column:
                identifier = (row.get(id_column) or "").strip()
                if not identifier:
                    result["blank_ids"] += 1
                elif identifier in seen:
                    result["duplicate_ids"] += 1
                else:
                    seen.add(identifier)
    return result


def audit_summary(path: Path) -> dict[str, object]:
    result: dict[str, object] = {"path": str(path), "parse_error": None, "scalar_counts": {}}
    try:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        result["parse_error"] = str(exc)
        return result
    if isinstance(value, dict):
        result["keys"] = sorted(value)
        result["scalar_counts"] = {
            key: item
            for key, item in value.items()
            if isinstance(item, (int, float, bool)) or item is None
        }
    else:
        result["type"] = type(value).__name__
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--max-file-mb", type=float, default=128.0)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    root = args.run_dir.resolve()
    max_bytes = int(args.max_file_mb * 1024 * 1024)
    jsonl = [audit_jsonl(path, max_bytes) for path in sorted(root.rglob("*.jsonl"))]
    csv_reports = [audit_csv(path, max_bytes) for path in sorted(root.rglob("*.csv"))]
    summaries = [audit_summary(path) for path in sorted(root.rglob("summary.json"))]
    payload = {
        "run_dir": str(root),
        "interpretation": "execution reconciliation only; corpus validity and gold status require source audit",
        "jsonl": jsonl,
        "csv": csv_reports,
        "summaries": summaries,
    }
    if args.as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(payload["run_dir"])
        print(payload["interpretation"])
        for report in jsonl:
            print(
                f"JSONL {report['records']} records, {report['parse_errors']} parse errors, "
                f"{report['duplicate_ids']} duplicate IDs: "
                f"{report['path']}"
            )
        for report in csv_reports:
            print(
                f"CSV {report['records']} records, {report['duplicate_ids']} duplicate IDs: "
                f"{report['path']}"
            )
        for report in summaries:
            print(f"SUMMARY keys={report.get('keys', [])}: {report['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

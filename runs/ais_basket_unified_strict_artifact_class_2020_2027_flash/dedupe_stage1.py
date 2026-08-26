#!/usr/bin/env python3
"""Recoverably deduplicate Stage 1 decisions by source_file."""

from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output_stage1"
SOURCE = OUTPUT / "decisions.jsonl"
BACKUP = OUTPUT / "decisions_raw_with_duplicates.jsonl"


def main() -> None:
    lines = [line for line in SOURCE.read_text(encoding="utf-8").splitlines() if line.strip()]
    rows = [json.loads(line) for line in lines]
    by_source: dict[str, dict] = {}
    for row in rows:
        by_source[str(row["source_file"])] = row
    if not BACKUP.exists():
        shutil.copy2(SOURCE, BACKUP)
    temp = SOURCE.with_suffix(".jsonl.tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as handle:
        for source in sorted(by_source):
            handle.write(json.dumps(by_source[source], ensure_ascii=False) + "\n")
    temp.replace(SOURCE)
    error_path = OUTPUT / "errors.jsonl"
    error_rows = []
    if error_path.exists():
        error_rows = [json.loads(line) for line in error_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    unresolved = sorted({str(row["source_file"]) for row in error_rows} - set(by_source))
    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "raw_decision_lines": len(rows),
        "unique_decisions": len(by_source),
        "duplicate_lines_removed": len(rows) - len(by_source),
        "historical_error_lines": len(error_rows),
        "unresolved_error_sources": unresolved,
        "raw_backup": BACKUP.name,
    }
    (OUTPUT / "dedupe_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

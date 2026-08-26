#!/usr/bin/env python3
"""Prepare a blind second-pass input set from stage-one candidates."""

from __future__ import annotations

import csv
import json
import shutil
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
STAGE1_CSV = RUN_DIR / "output_stage1_batch_v2" / "candidates.csv"
SOURCE_DIR = RUN_DIR / "input_metadata"
TARGET_DIR = RUN_DIR / "input_stage2"
SUMMARY_PATH = RUN_DIR / "stage2_preparation_summary.json"


def main() -> None:
    with STAGE1_CSV.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    for old_path in TARGET_DIR.glob("*.md"):
        old_path.unlink()
    missing: list[str] = []
    for row in rows:
        filename = (row.get("source_file") or "").strip()
        source = SOURCE_DIR / filename
        if not filename or not source.is_file():
            missing.append(filename)
            continue
        # Copy only the original metadata record. The second pass does not see
        # the first pass label, explanation, or confidence.
        shutil.copyfile(source, TARGET_DIR / filename)
    summary = {
        "stage1_candidates": len(rows),
        "prepared_blind_stage2_records": len(rows) - len(missing),
        "missing_source_files": missing,
    }
    SUMMARY_PATH.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

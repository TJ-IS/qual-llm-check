#!/usr/bin/env python3
"""Run the V3 screen in short 50-article child processes until the corpus is complete."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
WORKER = RUN_DIR / "run_full_v3.py"
DECISIONS = RUN_DIR / "output_full_v3" / "decisions.jsonl"
TARGET = 2475
BATCH_SIZE = 50


def completed_count() -> int:
    if not DECISIONS.exists():
        return 0
    sources: set[str] = set()
    with DECISIONS.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                row = json.loads(line)
                source = str(row.get("source_file") or "")
                if source:
                    sources.add(source)
    return len(sources)


def main() -> int:
    batch_number = 0
    while True:
        before = completed_count()
        if before >= TARGET:
            print(f"supervisor_complete={before}/{TARGET}", flush=True)
            return 0
        batch_number += 1
        print(f"supervisor_batch={batch_number} before={before}/{TARGET}", flush=True)
        result = subprocess.run(
            [
                sys.executable,
                str(WORKER),
                "--max-concurrency",
                str(BATCH_SIZE),
                "--batch-size",
                str(BATCH_SIZE),
            ],
            cwd=str(RUN_DIR.parent.parent),
            check=False,
        )
        after = completed_count()
        print(
            f"supervisor_batch={batch_number} returncode={result.returncode} "
            f"after={after}/{TARGET} added={after - before}",
            flush=True,
        )
        if result.returncode != 0:
            return result.returncode
        if after <= before:
            print("supervisor_error=no_progress", flush=True)
            return 3


if __name__ == "__main__":
    sys.exit(main())

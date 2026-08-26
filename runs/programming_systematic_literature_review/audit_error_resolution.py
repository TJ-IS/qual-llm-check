#!/usr/bin/env python3
"""Report whether every historically failed batch record was later resolved."""

from __future__ import annotations

import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent


def audit(output_name: str) -> dict[str, object]:
    output_dir = RUN_DIR / output_name
    decisions_path = output_dir / "decisions.jsonl"
    errors_path = output_dir / "errors.jsonl"
    decided: set[str] = set()
    if decisions_path.is_file():
        for line in decisions_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                decided.add(str(json.loads(line).get("source_file") or ""))
    failed: set[str] = set()
    error_events = 0
    if errors_path.is_file():
        for line in errors_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            error_events += 1
            payload = json.loads(line)
            if isinstance(payload.get("source_files"), list):
                failed.update(str(value) for value in payload["source_files"])
            elif payload.get("source_file"):
                failed.add(str(payload["source_file"]))
    unresolved = sorted(failed - decided)
    return {
        "output_dir": output_name,
        "error_events_logged": error_events,
        "unique_records_ever_in_failed_batches": len(failed),
        "resolved_records": len(failed & decided),
        "unresolved_records": unresolved,
    }


def main() -> None:
    reports = [
        audit("output_stage1_batch_v2"),
        audit("output_stage2_batch_v2"),
        audit("output_fulltext_local_v1"),
    ]
    path = RUN_DIR / "error_resolution_audit.json"
    path.write_text(
        json.dumps(reports, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(reports, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

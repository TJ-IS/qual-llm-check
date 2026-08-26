"""Rewrite ARB release manifests to explicit local chunk paths.

Released manifests intentionally use paths rooted at ``data/``.  A pilot may
store the release under another ignored asset directory; this utility creates
a separate normalized manifest and never edits the released file.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath


def normalize_records(input_path: Path, data_root: Path) -> list[dict]:
    records: list[dict] = []
    with input_path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            record = json.loads(line)
            chunks_value = str(record.get("chunks_path") or "")
            if not chunks_value:
                raise ValueError(f"{input_path}:{line_number}: missing chunks_path")
            posix = PurePosixPath(chunks_value)
            parts = posix.parts[1:] if posix.parts and posix.parts[0] == "data" else posix.parts
            chunks_path = data_root.joinpath(*parts).resolve()
            normalized = dict(record)
            normalized["chunks_path"] = str(chunks_path)
            normalized["pilot_path_exists"] = chunks_path.is_file()
            records.append(normalized)
    if not records:
        raise ValueError(f"{input_path}: no records")
    return records


def write_manifest(records: list[dict], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records),
        encoding="utf-8",
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--require-all",
        action="store_true",
        help="Fail if any referenced chunks file is absent.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    records = normalize_records(args.input, args.data_root)
    missing = [record for record in records if not record["pilot_path_exists"]]
    if args.require_all and missing:
        raise FileNotFoundError(f"{len(missing)} referenced chunks files are missing")
    write_manifest(records, args.output)


if __name__ == "__main__":
    main()

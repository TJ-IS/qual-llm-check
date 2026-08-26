#!/usr/bin/env python3
"""Prepare 2021+ Scopus citing records as metadata documents for LLM screening."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
ROOT = RUN_DIR.parents[1]
SOURCE_CSV = ROOT / "runs" / "ref_20_coding.csv"
INPUT_DIR = RUN_DIR / "input_2021plus"
MANIFEST_CSV = RUN_DIR / "input_manifest.csv"


def safe_name(value: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return text[:90] or "record"


def frontmatter_value(value: str) -> str:
    return json.dumps(value or "", ensure_ascii=False)


def main() -> None:
    with SOURCE_CSV.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = [
            row
            for row in csv.DictReader(handle)
            if int((row.get("Year") or "0").strip() or 0) >= 2021
        ]

    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest: list[dict[str, str]] = []
    for index, row in enumerate(rows, start=1):
        eid = (row.get("EID") or "").strip()
        title = (row.get("Title") or "").strip()
        filename = (
            f"{index:04d}_{row.get('Year') or '0000'}_"
            f"{safe_name(eid or title)}.md"
        )
        body = (
            "---\n"
            f"otero_id: {frontmatter_value(eid or str(index))}\n"
            f"title: {frontmatter_value(title)}\n"
            f"authors: {frontmatter_value((row.get('Authors') or '').strip())}\n"
            f"year: {frontmatter_value((row.get('Year') or '').strip())}\n"
            f"journal: {frontmatter_value((row.get('Source title') or '').strip())}\n"
            f"doi: {frontmatter_value((row.get('DOI') or '').strip())}\n"
            "---\n"
            "# Scopus metadata\n"
            f"Title: {title}\n"
            f"Abstract: {(row.get('Abstract') or '').strip()}\n"
            f"Author keywords: {(row.get('Author Keywords') or '').strip()}\n"
            f"Index keywords: {(row.get('Index Keywords') or '').strip()}\n"
            f"Document type: {(row.get('Document Type') or '').strip()}\n"
            f"Conference: {(row.get('Conference name') or '').strip()}\n"
            f"EID: {eid}\n"
        )
        (INPUT_DIR / filename).write_text(body, encoding="utf-8")
        manifest.append(
            {
                "source_file": filename,
                "eid": eid,
                "doi": (row.get("DOI") or "").strip(),
                "title": title,
                "year": (row.get("Year") or "").strip(),
                "source_title": (row.get("Source title") or "").strip(),
            }
        )

    with MANIFEST_CSV.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(manifest[0]))
        writer.writeheader()
        writer.writerows(manifest)
    print(f"Prepared {len(manifest)} records in {INPUT_DIR}")


if __name__ == "__main__":
    main()

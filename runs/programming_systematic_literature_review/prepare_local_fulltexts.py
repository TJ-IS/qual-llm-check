#!/usr/bin/env python3
"""Resolve screened candidates against the maintained local full-text library."""

from __future__ import annotations

import csv
import html
import json
import re
import shutil
import subprocess
import unicodedata
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
ROOT = RUN_DIR.parents[1]
AUDIT_CSV = RUN_DIR / "screening_audit.csv"
FULLTEXT_LIBRARY = ROOT / "database_fulltext_all"
TARGET_DIR = RUN_DIR / "fulltext_candidates_local"
MATCHED_CSV = RUN_DIR / "fulltext_local_manifest.csv"
MISSING_CSV = RUN_DIR / "fulltext_missing.csv"
SUMMARY_JSON = RUN_DIR / "fulltext_preparation_summary.json"


def normalize_doi(value: str) -> str:
    text = value.strip().lower()
    text = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", text)
    return text.rstrip(" .")


def normalize_title(value: str) -> str:
    text = html.unescape(re.sub(r"<[^>]+>", " ", value))
    text = unicodedata.normalize("NFKC", text).casefold()
    return re.sub(r"[^a-z0-9]+", "", text)


def read_frontmatter(path: Path) -> dict[str, str]:
    metadata: dict[str, str] = {}
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        if handle.readline().strip() != "---":
            return metadata
        for line in handle:
            if line.strip() == "---":
                break
            if ":" not in line:
                continue
            key, raw = line.split(":", 1)
            value = raw.strip()
            try:
                parsed = json.loads(value)
            except json.JSONDecodeError:
                parsed = value
            metadata[key.strip()] = str(parsed or "")
    return metadata


def build_library_index() -> tuple[dict[str, Path], dict[str, Path], dict[str, Path]]:
    """Use ripgrep for a single fast scan; fall back to per-file frontmatter reads."""
    by_filename: dict[str, Path] = {}
    by_doi: dict[str, Path] = {}
    by_title: dict[str, Path] = {}
    metadata_by_path: dict[Path, dict[str, str]] = {}
    try:
        relative_library = FULLTEXT_LIBRARY.relative_to(ROOT)
        result = subprocess.run(
            [
                "rg",
                "-n",
                r"^(title|doi):",
                str(relative_library),
                "-g",
                "*.md",
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        pattern = re.compile(r"^(.*?):(\d+):(title|doi):\s*(.*)$")
        for line in result.stdout.splitlines():
            match = pattern.match(line)
            if not match:
                continue
            path = (ROOT / match.group(1)).resolve()
            raw_value = match.group(4).strip()
            try:
                value = json.loads(raw_value)
            except json.JSONDecodeError:
                value = raw_value
            metadata_by_path.setdefault(path, {})[match.group(3)] = str(value or "")
    except (FileNotFoundError, subprocess.CalledProcessError):
        for path in sorted(FULLTEXT_LIBRARY.glob("*.md")):
            metadata_by_path[path.resolve()] = read_frontmatter(path)

    for path, metadata in metadata_by_path.items():
        by_filename[path.name] = path
        doi = normalize_doi(metadata.get("doi", ""))
        title = normalize_title(metadata.get("title", ""))
        if doi:
            by_doi.setdefault(doi, path)
        if title:
            by_title.setdefault(title, path)
    return by_filename, by_doi, by_title


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    audit = read_csv(AUDIT_CSV)
    candidates = [row for row in audit if row.get("stage1_label") != "exclude"]

    by_filename, by_doi, by_title = build_library_index()

    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    matched: list[dict[str, str]] = []
    missing: list[dict[str, str]] = []
    for row in candidates:
        source: Path | None = None
        match_basis = ""
        for filename in row.get("local_fulltext_files", "").split(";"):
            filename = filename.strip()
            if filename and filename in by_filename:
                source = by_filename[filename]
                match_basis = "recorded_local_filename"
                break
        if source is None:
            doi = normalize_doi(row.get("doi", ""))
            if doi and doi in by_doi:
                source = by_doi[doi]
                match_basis = "doi"
        if source is None:
            title = normalize_title(row.get("title", ""))
            if title and title in by_title:
                source = by_title[title]
                match_basis = "normalized_title"
        if source is None:
            missing.append(
                {
                    "source_file": row.get("source_file", ""),
                    "eid": row.get("eid", ""),
                    "doi": row.get("doi", ""),
                    "title": row.get("title", ""),
                    "year": row.get("year", ""),
                    "source_title": row.get("source_title", ""),
                    "retrieval_channels": row.get("retrieval_channels", ""),
                    "screening_status": row.get("screening_status", ""),
                }
            )
            continue
        target = TARGET_DIR / source.name
        shutil.copy2(source, target)
        matched.append(
            {
                "screening_source_file": row.get("source_file", ""),
                "fulltext_file": source.name,
                "fulltext_path": str(source),
                "match_basis": match_basis,
                "eid": row.get("eid", ""),
                "doi": row.get("doi", ""),
                "title": row.get("title", ""),
                "year": row.get("year", ""),
                "source_title": row.get("source_title", ""),
                "screening_status": row.get("screening_status", ""),
            }
        )

    matched_fields = [
        "screening_source_file",
        "fulltext_file",
        "fulltext_path",
        "match_basis",
        "eid",
        "doi",
        "title",
        "year",
        "source_title",
        "screening_status",
    ]
    missing_fields = [
        "source_file",
        "eid",
        "doi",
        "title",
        "year",
        "source_title",
        "retrieval_channels",
        "screening_status",
    ]
    write_csv(MATCHED_CSV, matched, matched_fields)
    write_csv(MISSING_CSV, missing, missing_fields)
    summary = {
        "stage1_candidates": len(candidates),
        "local_fulltexts_resolved": len(matched),
        "fulltexts_missing": len(missing),
        "match_basis_counts": {
            basis: sum(row["match_basis"] == basis for row in matched)
            for basis in sorted({row["match_basis"] for row in matched})
        },
    }
    SUMMARY_JSON.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Merge the authoritative-outlet, seed-citation, and local-seed channels."""

from __future__ import annotations

import csv
import hashlib
import html
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


RUN_DIR = Path(__file__).resolve().parent
ROOT = RUN_DIR.parents[1]
AUTHORITATIVE_CSV = RUN_DIR / "input" / "scopus_authoritative_4981.csv"
CITATION_CSV = ROOT / "runs" / "ref_20_coding.csv"
LOCAL_SEEDS_CSV = (
    ROOT
    / "runs"
    / "direct_programming_research_deepseek_analysis"
    / "output_v1"
    / "direct_programming_matches.csv"
)
BASKET_CSV = ROOT / "database" / "ALL_AIS_Basket_11.csv"
INPUT_DIR = RUN_DIR / "input_metadata"
MANIFEST_CSV = RUN_DIR / "input_manifest.csv"
PREPARATION_SUMMARY = RUN_DIR / "input_preparation_summary.json"

STANDARD_FIELDS = [
    "Authors",
    "Title",
    "Year",
    "Source title",
    "Cited by",
    "DOI",
    "Link",
    "Abstract",
    "Author Keywords",
    "Index Keywords",
    "Document Type",
    "Conference name",
    "EID",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [
            {str(key): str(value or "").strip() for key, value in row.items()}
            for row in csv.DictReader(handle)
        ]


def normalize_doi(value: str) -> str:
    text = value.strip().lower()
    text = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", text)
    return text.rstrip(" .")


def normalize_eid(value: str) -> str:
    return value.strip().lower()


def normalize_title(value: str) -> str:
    text = html.unescape(re.sub(r"<[^>]+>", " ", value))
    text = unicodedata.normalize("NFKC", text).casefold()
    return re.sub(r"[^a-z0-9]+", "", text)


def safe_name(value: str) -> str:
    text = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text[:90] or "record"


def frontmatter_value(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False)


class DisjointSet:
    def __init__(self, size: int):
        self.parent = list(range(size))

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left: int, right: int) -> None:
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left != root_right:
            self.parent[root_right] = root_left


def identity_keys(row: dict[str, str]) -> list[str]:
    keys: list[str] = []
    eid = normalize_eid(row.get("EID", ""))
    doi = normalize_doi(row.get("DOI", ""))
    title = normalize_title(row.get("Title", ""))
    if eid:
        keys.append(f"eid:{eid}")
    if doi:
        keys.append(f"doi:{doi}")
    if title:
        keys.append(f"title:{title}")
    return keys


def choose_value(field: str, values: list[str]) -> str:
    nonempty = [value.strip() for value in values if value and value.strip()]
    if not nonempty:
        return ""
    if field in {"Abstract", "Author Keywords", "Index Keywords", "Authors"}:
        return max(nonempty, key=len)
    return nonempty[0]


def main() -> None:
    authoritative = read_csv(AUTHORITATIVE_CSV)
    citations = read_csv(CITATION_CSV)
    basket = read_csv(BASKET_CSV)
    local_seeds = read_csv(LOCAL_SEEDS_CSV)

    basket_by_doi = {
        normalize_doi(row.get("DOI", "")): row
        for row in basket
        if normalize_doi(row.get("DOI", ""))
    }
    basket_by_title = {
        normalize_title(row.get("Title", "")): row
        for row in basket
        if normalize_title(row.get("Title", ""))
    }

    entries: list[dict[str, Any]] = []
    for row in authoritative:
        entries.append(
            {
                "row": row,
                "channel": "authoritative_outlet_search",
                "local_fulltext_file": "",
            }
        )
    for row in citations:
        entries.append(
            {
                "row": row,
                "channel": "forward_citation_of_20_seeds",
                "local_fulltext_file": "",
            }
        )
    for seed in local_seeds:
        doi = normalize_doi(seed.get("doi", ""))
        title_key = normalize_title(seed.get("title", ""))
        matched = basket_by_doi.get(doi) or basket_by_title.get(title_key)
        row = dict(matched or {})
        row.setdefault("Title", seed.get("title", ""))
        row.setdefault("Authors", seed.get("authors", ""))
        row.setdefault("Year", seed.get("year", ""))
        row.setdefault("Source title", seed.get("journal", ""))
        row.setdefault("DOI", seed.get("doi", ""))
        entries.append(
            {
                "row": row,
                "channel": "local_fulltext_seed_28",
                "local_fulltext_file": seed.get("source_file", ""),
            }
        )

    dsu = DisjointSet(len(entries))
    first_by_key: dict[str, int] = {}
    for index, entry in enumerate(entries):
        for key in identity_keys(entry["row"]):
            if key in first_by_key:
                dsu.union(first_by_key[key], index)
            else:
                first_by_key[key] = index

    groups: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for index, entry in enumerate(entries):
        groups[dsu.find(index)].append(entry)

    records: list[dict[str, Any]] = []
    for members in groups.values():
        merged = {
            field: choose_value(field, [member["row"].get(field, "") for member in members])
            for field in STANDARD_FIELDS
        }
        channels = sorted({member["channel"] for member in members})
        local_files = sorted(
            {
                member["local_fulltext_file"]
                for member in members
                if member["local_fulltext_file"]
            }
        )
        eid = merged.get("EID", "").strip()
        doi = normalize_doi(merged.get("DOI", ""))
        title = merged.get("Title", "").strip()
        record_id = eid or doi or hashlib.sha1(
            normalize_title(title).encode("utf-8")
        ).hexdigest()[:16]
        merged.update(
            {
                "record_id": record_id,
                "retrieval_channels": channels,
                "local_fulltext_files": local_files,
            }
        )
        records.append(merged)

    records.sort(
        key=lambda row: (
            -int(row.get("Year") or 0) if str(row.get("Year") or "").isdigit() else 0,
            row.get("Title", "").casefold(),
        )
    )
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    for old_path in INPUT_DIR.glob("*.md"):
        old_path.unlink()

    manifest: list[dict[str, str]] = []
    for index, row in enumerate(records, start=1):
        year = row.get("Year") or "0000"
        filename = f"{index:05d}_{year}_{safe_name(row.get('Title', ''))}.md"
        channels = row["retrieval_channels"]
        local_files = row["local_fulltext_files"]
        body = (
            "---\n"
            f"otero_id: {frontmatter_value(row['record_id'])}\n"
            f"title: {frontmatter_value(row.get('Title', ''))}\n"
            f"authors: {frontmatter_value(row.get('Authors', ''))}\n"
            f"year: {frontmatter_value(str(row.get('Year', '')))}\n"
            f"journal: {frontmatter_value(row.get('Source title', ''))}\n"
            f"doi: {frontmatter_value(normalize_doi(row.get('DOI', '')))}\n"
            "---\n"
            "# Scopus title-abstract-keyword metadata\n"
            f"Title: {row.get('Title', '')}\n"
            f"Abstract: {row.get('Abstract', '')}\n"
            f"Author keywords: {row.get('Author Keywords', '')}\n"
            f"Index keywords: {row.get('Index Keywords', '')}\n"
            f"Document type: {row.get('Document Type', '')}\n"
            f"Conference: {row.get('Conference name', '')}\n"
            f"Source title: {row.get('Source title', '')}\n"
            f"Year: {row.get('Year', '')}\n"
            f"EID: {row.get('EID', '')}\n"
            f"DOI: {normalize_doi(row.get('DOI', ''))}\n"
            f"Retrieval channels: {'; '.join(channels)}\n"
            f"Local full-text files: {'; '.join(local_files)}\n"
        )
        (INPUT_DIR / filename).write_text(body, encoding="utf-8")
        manifest.append(
            {
                "source_file": filename,
                "record_id": str(row["record_id"]),
                "eid": row.get("EID", ""),
                "doi": normalize_doi(row.get("DOI", "")),
                "title": row.get("Title", ""),
                "year": str(row.get("Year", "")),
                "source_title": row.get("Source title", ""),
                "retrieval_channels": ";".join(channels),
                "local_fulltext_files": ";".join(local_files),
                "abstract_available": str(bool(row.get("Abstract", ""))),
            }
        )

    with MANIFEST_CSV.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(manifest[0]))
        writer.writeheader()
        writer.writerows(manifest)

    channel_counts: Counter[str] = Counter()
    channel_combinations: Counter[str] = Counter()
    for row in records:
        channel_counts.update(row["retrieval_channels"])
        channel_combinations[" + ".join(row["retrieval_channels"])] += 1
    summary = {
        "source_rows": {
            "authoritative_outlet_search": len(authoritative),
            "forward_citation_of_20_seeds": len(citations),
            "local_fulltext_seed_28": len(local_seeds),
        },
        "deduplicated_records": len(records),
        "records_with_abstract": sum(bool(row.get("Abstract", "")) for row in records),
        "records_without_abstract": sum(not bool(row.get("Abstract", "")) for row in records),
        "records_by_channel": dict(channel_counts),
        "records_by_channel_combination": dict(channel_combinations),
    }
    PREPARATION_SUMMARY.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

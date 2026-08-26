from __future__ import annotations

import csv
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path


ROOT = Path(r"E:\github\qual-llm-check-IS-utd")
RUN_DIR = ROOT / "runs" / "seed_author_followup_scopus"
RAW_PATH = RUN_DIR / "author_20_raw_all.csv"
AUTHOR_MAP_PATH = RUN_DIR / "seed_author_map.csv"
SEEDS_PATH = ROOT / "runs" / "direct_programming_scopus_citation_lineage" / "seed_articles.csv"
PRIOR_CITING_PATH = (
    ROOT
    / "runs"
    / "direct_programming_scopus_citation_lineage"
    / "scopus_citing_20_seed_807_raw.csv"
)
OUT_DIR = RUN_DIR / "analysis_v1"


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def split_ids(value: str) -> list[str]:
    return [item.strip() for item in (value or "").split(";") if item.strip()]


def as_int(value: str, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def record_key(row: dict[str, str], index: int) -> str:
    if row.get("EID"):
        return f"eid:{row['EID'].strip()}"
    if row.get("DOI"):
        return f"doi:{row['DOI'].strip().lower()}"
    return f"row:{index:05d}"


def norm_text(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "").casefold()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", value).split())


def norm_doi(value: str) -> str:
    value = (value or "").strip().casefold()
    value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value)
    return value.rstrip(".,; ")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    raw_rows = load_csv(RAW_PATH)
    author_rows = load_csv(AUTHOR_MAP_PATH)
    seeds = load_csv(SEEDS_PATH)
    prior_citing_rows = load_csv(PRIOR_CITING_PATH)
    target = {row["author_id"]: row for row in author_rows}
    citing_by_eid = {
        row["EID"].strip(): row for row in prior_citing_rows if row.get("EID", "").strip()
    }
    citing_by_doi = {
        norm_doi(row["DOI"]): row
        for row in prior_citing_rows
        if norm_doi(row.get("DOI", ""))
    }
    citing_by_title = {
        norm_text(row["Title"]): row
        for row in prior_citing_rows
        if norm_text(row.get("Title", ""))
    }
    seed_lookup = [
        {
            "seed_id": seed["seed_id"],
            "doi": norm_doi(seed["doi"]),
            "title": norm_text(seed["title"]),
        }
        for seed in seeds
    ]

    seen: set[str] = set()
    duplicate_keys: list[str] = []
    processed: list[dict[str, object]] = []
    author_edges: list[dict[str, object]] = []
    record_years: Counter[int] = Counter()
    sources: Counter[str] = Counter()
    document_types: Counter[str] = Counter()
    missing_abstract = 0
    missing_references = 0
    references_field_high_confidence_seed_matches = 0
    seed_citation_counts: Counter[str] = Counter()
    prior_citation_union_matches = 0
    prior_citation_match_methods: Counter[str] = Counter()
    citing_followup_records: list[dict[str, object]] = []
    records_with_multiple_eligible = 0
    records_with_no_target_id = 0

    for index, row in enumerate(raw_rows, start=1):
        key = record_key(row, index)
        if key in seen:
            duplicate_keys.append(key)
            continue
        seen.add(key)

        year = as_int(row.get("Year", ""))
        record_author_ids = split_ids(row.get("Author(s) ID", ""))
        matched_ids = [author_id for author_id in record_author_ids if author_id in target]
        eligible_ids = [
            author_id
            for author_id in matched_ids
            if year > as_int(target[author_id]["latest_seed_year"])
        ]
        if not matched_ids:
            records_with_no_target_id += 1
        if len(eligible_ids) > 1:
            records_with_multiple_eligible += 1

        eligible_names = [target[author_id]["author_name"] for author_id in eligible_ids]
        eligible_tiers = []
        for author_id in eligible_ids:
            author = target[author_id]
            if author["is_any_first_author"].lower() == "true":
                tier = "first_author"
            elif author["is_core_author"].lower() == "true":
                tier = "recurring_coauthor"
            else:
                tier = "other_coauthor"
            eligible_tiers.append(tier)
            author_edges.append(
                {
                    "record_key": key,
                    "eid": row.get("EID", ""),
                    "doi": row.get("DOI", ""),
                    "title": row.get("Title", ""),
                    "year": year,
                    "source_title": row.get("Source title", ""),
                    "document_type": row.get("Document Type", ""),
                    "cited_by": as_int(row.get("Cited by", "")),
                    "target_author_id": author_id,
                    "target_author_name": author["author_name"],
                    "target_author_tier": tier,
                    "latest_seed_year": as_int(author["latest_seed_year"]),
                    "years_after_last_seed": year - as_int(author["latest_seed_year"]),
                    "seed_ids": author["seed_ids"],
                }
            )

        abstract = row.get("Abstract", "") or ""
        references = row.get("References", "") or ""
        if not abstract.strip() or abstract.strip().lower() in {"[no abstract available]", "no abstract available"}:
            missing_abstract += 1
        if not references.strip():
            missing_references += 1

        reference_doi_text = references.casefold()
        reference_title_text = norm_text(references)
        seed_ids_by_doi = [
            seed["seed_id"]
            for seed in seed_lookup
            if seed["doi"] and seed["doi"] in reference_doi_text
        ]
        seed_ids_by_title = [
            seed["seed_id"]
            for seed in seed_lookup
            if seed["title"] and seed["title"] in reference_title_text
        ]
        cited_seed_ids = sorted(
            set(seed_ids_by_doi) | set(seed_ids_by_title), key=lambda value: int(value)
        )
        if cited_seed_ids:
            references_field_high_confidence_seed_matches += 1
            seed_citation_counts.update(cited_seed_ids)

        citation_union_match_method = ""
        if row.get("EID", "").strip() in citing_by_eid:
            citation_union_match_method = "eid"
        elif norm_doi(row.get("DOI", "")) in citing_by_doi:
            citation_union_match_method = "doi_fallback"
        elif norm_text(row.get("Title", "")) in citing_by_title:
            citation_union_match_method = "title_fallback"
        in_prior_citation_union = bool(citation_union_match_method)
        if in_prior_citation_union:
            prior_citation_union_matches += 1
            prior_citation_match_methods[citation_union_match_method] += 1

        record_years[year] += 1
        sources[row.get("Source title", "") or "(missing)"] += 1
        document_types[row.get("Document Type", "") or "(missing)"] += 1
        processed.append(
            {
                "record_key": key,
                "eid": row.get("EID", ""),
                "doi": row.get("DOI", ""),
                "title": row.get("Title", ""),
                "year": year,
                "source_title": row.get("Source title", ""),
                "document_type": row.get("Document Type", ""),
                "cited_by": as_int(row.get("Cited by", "")),
                "authors": row.get("Authors", ""),
                "author_full_names": row.get("Author full names", ""),
                "author_ids": row.get("Author(s) ID", ""),
                "abstract": abstract,
                "author_keywords": row.get("Author Keywords", ""),
                "index_keywords": row.get("Index Keywords", ""),
                "references": references,
                "in_prior_scopus_citing_20_export": in_prior_citation_union,
                "prior_citation_union_match_method": citation_union_match_method,
                "references_field_cited_seed_ids": ";".join(cited_seed_ids),
                "references_field_seed_ids_by_doi": ";".join(seed_ids_by_doi),
                "references_field_seed_ids_by_title": ";".join(seed_ids_by_title),
                "matched_target_author_ids": ";".join(matched_ids),
                "eligible_target_author_ids": ";".join(eligible_ids),
                "eligible_target_author_names": "; ".join(eligible_names),
                "eligible_target_author_tiers": ";".join(eligible_tiers),
            }
        )
        if in_prior_citation_union:
            citing_followup_records.append(processed[-1])

    author_edge_counts = Counter(edge["target_author_id"] for edge in author_edges)
    author_latest_year = defaultdict_int()
    author_earliest_followup = defaultdict_int(default=9999)
    for edge in author_edges:
        author_id = str(edge["target_author_id"])
        author_latest_year[author_id] = max(author_latest_year[author_id], int(edge["year"]))
        author_earliest_followup[author_id] = min(author_earliest_followup[author_id], int(edge["year"]))

    author_summary: list[dict[str, object]] = []
    for author_id, author in target.items():
        if author["is_any_first_author"].lower() == "true":
            tier = "first_author"
        elif author["is_core_author"].lower() == "true":
            tier = "recurring_coauthor"
        else:
            tier = "other_coauthor"
        count = author_edge_counts[author_id]
        author_summary.append(
            {
                "author_id": author_id,
                "author_name": author["author_name"],
                "author_tier": tier,
                "seed_count": as_int(author["seed_count"]),
                "latest_seed_year": as_int(author["latest_seed_year"]),
                "seed_ids": author["seed_ids"],
                "eligible_followup_records": count,
                "earliest_followup_year": author_earliest_followup[author_id] if count else "",
                "latest_followup_year": author_latest_year[author_id] if count else "",
            }
        )
    author_summary.sort(key=lambda row: (-int(row["eligible_followup_records"]), str(row["author_name"]).lower()))

    processed_path = OUT_DIR / "records_with_seed_author_mapping.csv"
    with processed_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(processed[0]))
        writer.writeheader()
        writer.writerows(processed)

    edge_path = OUT_DIR / "author_record_edges.csv"
    with edge_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(author_edges[0]))
        writer.writeheader()
        writer.writerows(author_edges)

    author_summary_path = OUT_DIR / "author_summary.csv"
    with author_summary_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(author_summary[0]))
        writer.writeheader()
        writer.writerows(author_summary)

    citing_followup_path = OUT_DIR / "author_followup_in_prior_citing_20_union.csv"
    with citing_followup_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(citing_followup_records[0]))
        writer.writeheader()
        writer.writerows(citing_followup_records)

    llm_path = OUT_DIR / "llm_inputs.jsonl"
    with llm_path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in processed:
            llm_record = {
                key: row[key]
                for key in [
                    "record_key",
                    "eid",
                    "doi",
                    "title",
                    "year",
                    "source_title",
                    "document_type",
                    "abstract",
                    "author_keywords",
                    "index_keywords",
                    "eligible_target_author_ids",
                    "eligible_target_author_names",
                    "eligible_target_author_tiers",
                ]
            }
            handle.write(json.dumps(llm_record, ensure_ascii=False) + "\n")

    coverage = sum(1 for row in author_summary if int(row["eligible_followup_records"]) > 0)
    summary = {
        "raw_rows": len(raw_rows),
        "unique_records": len(processed),
        "duplicate_record_keys": len(duplicate_keys),
        "duplicate_keys_sample": duplicate_keys[:20],
        "target_authors": len(target),
        "target_authors_with_eligible_followup": coverage,
        "target_authors_without_eligible_followup": len(target) - coverage,
        "author_record_edges": len(author_edges),
        "records_with_multiple_eligible_target_authors": records_with_multiple_eligible,
        "records_with_no_target_author_id": records_with_no_target_id,
        "missing_abstract": missing_abstract,
        "missing_references": missing_references,
        "prior_scopus_citing_union_records": len(prior_citing_rows),
        "author_followup_records_in_prior_citing_union": prior_citation_union_matches,
        "prior_citation_match_methods": dict(prior_citation_match_methods),
        "references_field_high_confidence_seed_matches": references_field_high_confidence_seed_matches,
        "references_field_seed_counts_supplementary_only": dict(
            sorted(seed_citation_counts.items(), key=lambda item: int(item[0]))
        ),
        "year_min": min(record_years) if record_years else None,
        "year_max": max(record_years) if record_years else None,
        "year_counts": dict(sorted(record_years.items(), reverse=True)),
        "top_sources": sources.most_common(30),
        "document_types": document_types.most_common(),
        "top_authors_by_followup_records": author_summary[:20],
        "outputs": {
            "processed_records": str(processed_path),
            "author_record_edges": str(edge_path),
            "author_summary": str(author_summary_path),
            "author_followup_in_prior_citing_union": str(citing_followup_path),
            "llm_inputs": str(llm_path),
        },
    }
    (OUT_DIR / "metadata_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


class defaultdict_int(dict[str, int]):
    def __init__(self, default: int = 0) -> None:
        super().__init__()
        self.default = default

    def __missing__(self, key: str) -> int:
        return self.default


if __name__ == "__main__":
    main()

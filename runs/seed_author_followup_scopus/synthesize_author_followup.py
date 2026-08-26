from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


LABELS = [
    "direct_human_ai_programming",
    "direct_human_programming",
    "programming_artifact_or_method",
    "software_development_process_or_team",
    "information_systems_or_technology_adjacent",
    "unrelated_or_unclear",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: Iterable[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    rows = list(rows)
    if fieldnames is None:
        fieldnames = list(rows[0]) if rows else []
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def read_jsonl_lenient(path: Path) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    decisions: dict[str, dict[str, Any]] = {}
    malformed: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8-sig", errors="replace") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                match = re.search(r'"record_key"\s*:\s*"([^"]+)"', line)
                malformed.append(
                    {
                        "line_number": line_number,
                        "record_key": match.group(1) if match else "",
                        "error": str(exc),
                    }
                )
                continue
            key = item.get("record_key") or item.get("record_id")
            if key:
                decisions[str(key)] = item
    return decisions, malformed


def truthy(value: Any) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes"}


def normalize_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def decade(year: str) -> str:
    try:
        number = int(year)
    except (TypeError, ValueError):
        return "unknown"
    return f"{number // 10 * 10}s"


def joined_row(record: dict[str, str], decision: dict[str, Any]) -> dict[str, Any]:
    return {
        "record_key": record["record_key"],
        "eid": record["eid"],
        "doi": record["doi"],
        "title": record["title"],
        "year": record["year"],
        "decade": decade(record["year"]),
        "source_title": record["source_title"],
        "document_type": record["document_type"],
        "cited_by": record["cited_by"],
        "authors": record["authors"],
        "eligible_target_author_ids": record["eligible_target_author_ids"],
        "eligible_target_author_names": record["eligible_target_author_names"],
        "eligible_target_author_tiers": record["eligible_target_author_tiers"],
        "confirmed_cites_at_least_one_seed_via_prior_refeid_union": truthy(
            record["in_prior_scopus_citing_20_export"]
        ),
        "prior_citation_union_match_method": record["prior_citation_union_match_method"],
        "trajectory_label": decision["trajectory_label"],
        "continuity_strength": decision["continuity_strength"],
        "direct_human_programming": decision.get("direct_human_programming"),
        "modern_ai_assisted_programming": decision.get("modern_ai_assisted_programming"),
        "ai_context": decision.get("ai_context", "unclear"),
        "seed_theme_connections": ";".join(decision.get("seed_theme_connections") or []),
        "research_method": decision.get("research_method", "unclear"),
        "decision_certainty": decision.get("decision_certainty", "low"),
        "screening_source": decision.get("screening_source", "deepseek-v4-flash"),
        "evidence": " | ".join(decision.get("evidence") or []),
        "reason": decision.get("reason", ""),
        "abstract": record["abstract"],
        "author_keywords": record["author_keywords"],
        "index_keywords": record["index_keywords"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base",
        type=Path,
        default=Path(__file__).resolve().parent / "analysis_v1",
    )
    args = parser.parse_args()
    base = args.base.resolve()

    records = read_csv(base / "records_with_seed_author_mapping.csv")
    edges = read_csv(base / "author_record_edges.csv")
    author_base = read_csv(base / "author_summary.csv")
    decisions, malformed = read_jsonl_lenient(base / "flash_screening_v1" / "decisions.jsonl")
    overrides, malformed_overrides = read_jsonl_lenient(base / "manual_overrides.jsonl")
    for decision in overrides.values():
        decision["screening_source"] = "manual_override"
    decisions.update(overrides)

    record_map = {row["record_key"]: row for row in records}
    missing = sorted(set(record_map) - set(decisions))
    unknown = sorted(set(decisions) - set(record_map))
    if missing:
        raise SystemExit(f"Missing decisions after overrides: {missing}")

    joined = [joined_row(record_map[key], decisions[key]) for key in record_map]
    joined_map = {row["record_key"]: row for row in joined}
    write_csv(base / "screening_joined.csv", joined)

    label_rows = []
    for label in LABELS:
        subset = [row for row in joined if row["trajectory_label"] == label]
        citing = [
            row
            for row in subset
            if row["confirmed_cites_at_least_one_seed_via_prior_refeid_union"]
        ]
        label_rows.append(
            {
                "trajectory_label": label,
                "records": len(subset),
                "percent_of_1209": round(len(subset) / len(joined) * 100, 2),
                "confirmed_seed_citers_via_prior_refeid_union": len(citing),
                "percent_with_confirmed_seed_citation": round(len(citing) / len(subset) * 100, 2)
                if subset
                else 0,
            }
        )
    write_csv(base / "trajectory_label_summary.csv", label_rows)

    strict_labels = {"direct_human_ai_programming", "direct_human_programming"}
    broader_labels = strict_labels | {
        "programming_artifact_or_method",
        "software_development_process_or_team",
    }
    strict = [row for row in joined if row["trajectory_label"] in strict_labels]
    broader = [row for row in joined if row["trajectory_label"] in broader_labels]
    confirmed = [
        row
        for row in joined
        if row["confirmed_cites_at_least_one_seed_via_prior_refeid_union"]
    ]
    ai_related = [
        row
        for row in joined
        if row["trajectory_label"] == "direct_human_ai_programming"
        or str(row["ai_context"]).startswith("ai_")
    ]
    review_queue = [
        row
        for row in joined
        if row["trajectory_label"] in broader_labels
        or row["decision_certainty"] == "low"
        or row["ai_context"] != "no_ai"
    ]

    sort_key = lambda row: (int(row["year"] or 0), row["title"].lower())
    write_csv(base / "strict_human_programming_candidates.csv", sorted(strict, key=sort_key))
    write_csv(base / "broader_software_lineage_candidates.csv", sorted(broader, key=sort_key))
    write_csv(base / "ai_related_candidates.csv", sorted(ai_related, key=sort_key))
    write_csv(base / "confirmed_seed_citers_with_screening.csv", sorted(confirmed, key=sort_key))
    write_csv(base / "manual_review_queue.csv", sorted(review_queue, key=sort_key))

    per_author: dict[str, Counter[str]] = defaultdict(Counter)
    author_identity: dict[str, dict[str, str]] = {}
    for edge in edges:
        key = edge["record_key"]
        decision = joined_map[key]
        author_id = edge["target_author_id"]
        author_identity[author_id] = edge
        counter = per_author[author_id]
        counter["all_followup_records"] += 1
        counter[decision["trajectory_label"]] += 1
        if decision["confirmed_cites_at_least_one_seed_via_prior_refeid_union"]:
            counter["confirmed_seed_citers"] += 1
        if decision["trajectory_label"] in strict_labels:
            counter["strict_human_programming"] += 1
        if decision["trajectory_label"] in broader_labels:
            counter["broader_software_lineage"] += 1
        if decision["ai_context"] != "no_ai":
            counter["ai_related"] += 1

    base_by_author = {row["author_id"]: row for row in author_base}
    author_rows: list[dict[str, Any]] = []
    for author_id in base_by_author:
        base_row = base_by_author[author_id]
        counts = per_author[author_id]
        total = counts["all_followup_records"]
        author_rows.append(
            {
                "author_id": author_id,
                "author_name": base_row["author_name"],
                "author_tier": base_row["author_tier"],
                "seed_count": base_row["seed_count"],
                "seed_ids": base_row["seed_ids"],
                "latest_seed_year": base_row["latest_seed_year"],
                "all_followup_records": total,
                "strict_human_programming": counts["strict_human_programming"],
                "strict_percent": round(counts["strict_human_programming"] / total * 100, 2)
                if total
                else 0,
                "direct_human_ai_programming": counts["direct_human_ai_programming"],
                "direct_human_programming": counts["direct_human_programming"],
                "programming_artifact_or_method": counts["programming_artifact_or_method"],
                "software_development_process_or_team": counts[
                    "software_development_process_or_team"
                ],
                "information_systems_or_technology_adjacent": counts[
                    "information_systems_or_technology_adjacent"
                ],
                "unrelated_or_unclear": counts["unrelated_or_unclear"],
                "broader_software_lineage": counts["broader_software_lineage"],
                "confirmed_seed_citers_via_prior_refeid_union": counts[
                    "confirmed_seed_citers"
                ],
                "ai_related": counts["ai_related"],
            }
        )
    author_rows.sort(
        key=lambda row: (
            -int(row["strict_human_programming"]),
            -int(row["broader_software_lineage"]),
            row["author_name"],
        )
    )
    write_csv(base / "author_trajectory_summary.csv", author_rows)

    decade_rows: list[dict[str, Any]] = []
    for period in sorted({row["decade"] for row in joined}):
        subset = [row for row in joined if row["decade"] == period]
        item: dict[str, Any] = {"decade": period, "records": len(subset)}
        for label in LABELS:
            item[label] = sum(row["trajectory_label"] == label for row in subset)
        item["confirmed_seed_citers_via_prior_refeid_union"] = sum(
            row["confirmed_cites_at_least_one_seed_via_prior_refeid_union"] for row in subset
        )
        decade_rows.append(item)
    write_csv(base / "trajectory_by_decade.csv", decade_rows)

    normalized = Counter(normalize_title(row["title"]) for row in joined)
    duplicate_clusters = {title: count for title, count in normalized.items() if title and count > 1}
    source_counts = Counter(row["screening_source"] for row in joined)
    label_counts = Counter(row["trajectory_label"] for row in joined)
    citation_label_counts = Counter(row["trajectory_label"] for row in confirmed)
    direct_citing = [
        row
        for row in strict
        if row["confirmed_cites_at_least_one_seed_via_prior_refeid_union"]
    ]
    ai_direct = [row for row in joined if row["modern_ai_assisted_programming"] is True]

    summary = {
        "records": len(joined),
        "citation_matching_primary_rule": "Exact EID intersection with the previously retrieved 807-record Scopus REFEID union; DOI fallback only where EID was unavailable.",
        "confirmed_cites_at_least_one_of_20_seeds": len(confirmed),
        "citation_match_methods": dict(Counter(row["prior_citation_union_match_method"] for row in confirmed)),
        "important_citation_limit": "The union query confirms at least one seed citation but does not identify which seed unless a seed-by-citing-paper edge retrieval is performed.",
        "trajectory_label_counts": dict(label_counts),
        "strict_human_programming_records": len(strict),
        "strict_human_programming_confirmed_seed_citers": len(direct_citing),
        "broader_software_lineage_records": len(broader),
        "direct_human_ai_programming_records": sum(
            row["trajectory_label"] == "direct_human_ai_programming" for row in joined
        ),
        "modern_ai_assisted_programming_true": len(ai_direct),
        "screening_sources": dict(source_counts),
        "malformed_deepseek_lines": malformed,
        "malformed_manual_override_lines": malformed_overrides,
        "unknown_decision_keys": unknown,
        "normalized_title_duplicate_clusters": len(duplicate_clusters),
        "records_in_normalized_title_duplicate_clusters": sum(duplicate_clusters.values()),
        "confirmed_seed_citers_by_trajectory_label": dict(citation_label_counts),
        "deepseek_usage_from_last_summary": json.loads(
            (base / "flash_screening_v1" / "summary.json").read_text(encoding="utf-8-sig")
        ).get("usage", {}),
    }
    (base / "synthesis_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    top_strict = [row for row in author_rows if int(row["strict_human_programming"]) > 0][:15]
    citation_table = "\n".join(
        f"| `{row['trajectory_label']}` | {row['records']} | {row['confirmed_seed_citers_via_prior_refeid_union']} | {row['percent_with_confirmed_seed_citation']}% |"
        for row in label_rows
    )
    author_table = "\n".join(
        f"| {row['author_name']} | {row['all_followup_records']} | {row['strict_human_programming']} | {row['broader_software_lineage']} | {row['confirmed_seed_citers_via_prior_refeid_union']} |"
        for row in top_strict
    )
    strict_titles = "\n".join(
        f"- {row['year']} — {row['title']} ({row['eligible_target_author_names']})"
        for row in sorted(strict, key=sort_key)[-15:]
    )
    report = f"""# Follow-up publications of the 20 seed papers' authors

## Scope and matching rule

- The Scopus author-follow-up export contains **{len(joined):,} records** linked to 36 seed-paper authors, after each author's latest seed-paper year.
- Seed-citation continuity is determined from the **previously retrieved 807-record Scopus `REFEID` union**, not from the export's non-standard `References` text.
- **{len(confirmed)} follow-up records** intersect that union: {sum(row['prior_citation_union_match_method'] == 'eid' for row in confirmed)} by exact EID and {sum(row['prior_citation_union_match_method'] == 'doi_fallback' for row in confirmed)} by DOI fallback.
- This establishes that each of the {len(confirmed)} records cites **at least one** seed. It does not determine which seed because the earlier union result did not preserve seed-to-citing-paper edges.

## Screening result

DeepSeek v4 Flash produced usable decisions for {source_counts.get('deepseek-v4-flash', 0):,} records. Eleven records (ten persistent failures plus one malformed JSON line) were manually coded with the identical decision schema. Counts are Scopus records; normalized-title checking found {len(duplicate_clusters)} repeated-title clusters containing {sum(duplicate_clusters.values())} records, so conference/journal or duplicate-index variants may represent the same intellectual work.

| Trajectory | Records | Confirmed seed citers | Within-label citation rate |
|---|---:|---:|---:|
{citation_table}

Strict human-programming continuity comprises **{len(strict)} records** ({len(strict) / len(joined) * 100:.1f}%); **{len(direct_citing)}** of those are confirmed seed citers. The broader software lineage (adding software artifacts/methods and development process/team studies) comprises **{len(broader)} records** ({len(broader) / len(joined) * 100:.1f}%).

## Interpretation

The authors did not stop publishing. Instead, the dominant pattern is topic migration: most later work concerns general IS/technology phenomena, conceptual modeling, HCI, auditing, platforms, organizations, and other adjacent areas. A small but visible line continued through spreadsheet errors/testing, SQL and database-query learning, program or schema comprehension, software-component development, and software-design cognition.

Direct bibliographic continuity and topical continuity are different. The {len(confirmed)} confirmed citers show that the old papers continued to be referenced, but only {len(direct_citing)} are also in the strict human-programming class. Conversely, many topically relevant later papers do not cite a seed. This helps explain the apparent break in the AIS lineage: citation inheritance is sparse, while the phenomenon diffused into different labels, venues, methods, and neighboring research communities.

For modern AI-assisted programming, only **Teaching SQL Using ChatGPT** meets the strict code/query-operation rule in this author-follow-up set. **How Gen AI Is Reshaping Software Design Work** is substantively important under a broader software-development definition, but its abstract studies UX/UI and software-design roles and workflows rather than concrete code writing, comprehension, debugging, testing, or review; it is therefore retained as broader adjacent continuity, not strict AI-assisted programming. Neither record is in the prior 807-record seed-citing union.

## Authors with the most strict-continuity records

| Author | All follow-up | Strict human programming | Broader software lineage | Confirmed seed citers |
|---|---:|---:|---:|---:|
{author_table}

## Most recent strict-continuity records

{strict_titles}

## Files

- `screening_joined.csv`: all 1,209 records with author, citation-union, and screening fields.
- `confirmed_seed_citers_with_screening.csv`: the 48 records confirmed through the prior `REFEID` union.
- `strict_human_programming_candidates.csv`: the strict direct-human and direct-human-AI set.
- `broader_software_lineage_candidates.csv`: strict set plus artifacts/methods and development process/team.
- `author_trajectory_summary.csv`: author-level cross-tabulation.
- `trajectory_by_decade.csv`: decade-level cross-tabulation.
- `manual_review_queue.csv`: broader candidates, low-certainty records, and AI-context records for audit.

## Limits

This is a title/abstract/keyword screen, not full-text inclusion. A final systematic review should manually adjudicate the strict and broader candidate files, collapse duplicate intellectual works, and retrieve seed-specific citation edges if the exact seed cited by each follow-up paper matters.
"""
    (base / "analysis_report.md").write_text(report, encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

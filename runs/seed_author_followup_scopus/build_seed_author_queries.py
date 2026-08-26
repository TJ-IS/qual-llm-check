from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(r"E:\github\qual-llm-check-IS-utd")
SEEDS_PATH = ROOT / "runs" / "direct_programming_scopus_citation_lineage" / "seed_articles.csv"
DB_PATH = ROOT / "database" / "ALL_AIS_Basket_11.csv"
OUT_DIR = ROOT / "runs" / "seed_author_followup_scopus"


PROGRAMMING_TERMS = '''TITLE-ABS-KEY(
  "computer program*" OR programmer* OR programming OR coding OR
  "software develop*" OR "software engineer*" OR "software maintenan*" OR
  "program comprehension" OR "software comprehension" OR "code comprehension" OR
  "source code" OR debugging OR "software testing" OR "code review" OR
  "code inspection" OR "pair programming" OR "test-driven development" OR
  "end-user computing" OR "end-user development" OR "end-user programming" OR
  spreadsheet* OR "query formulation" OR "query development" OR
  "SQL quer*" OR "database quer*" OR "code generation"
)'''


GENAI_PROGRAMMING_TERMS = '''TITLE-ABS-KEY(
  ("generative AI" OR "generative artificial intelligence" OR
   "large language model*" OR LLM OR ChatGPT OR Copilot OR Codex OR
   "AI assistant*" OR "AI-assisted" OR "artificial intelligence-assisted" OR
   "coding agent*" OR "programming agent*" OR "software engineering agent*")
  AND
  (programming OR coding OR programmer* OR developer* OR "software engineering" OR
   "software development" OR "source code" OR "code generation" OR debugging OR
   testing OR "code review" OR "program comprehension")
)'''


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def parse_authors(row: dict[str, str]) -> list[tuple[str, str]]:
    names = [item.strip() for item in row["Author full names"].split(";") if item.strip()]
    ids = [item.strip() for item in row["Author(s) ID"].split(";") if item.strip()]
    if len(names) != len(ids):
        raise ValueError(f"Author/name count mismatch for {row['Title']!r}: {len(names)} vs {len(ids)}")

    parsed: list[tuple[str, str]] = []
    for name_with_id, author_id in zip(names, ids):
        match = re.match(r"^(.*?)\s*\((\d+)\)\s*$", name_with_id)
        name = match.group(1).strip() if match else name_with_id
        embedded_id = match.group(2) if match else author_id
        if embedded_id != author_id:
            raise ValueError(f"Embedded author ID mismatch: {name_with_id!r} vs {author_id!r}")
        parsed.append((name, author_id))
    return parsed


def author_union(ids: list[str]) -> str:
    return " OR ".join(f"AU-ID({author_id})" for author_id in ids)


def followup_union(author_rows: list[dict[str, object]]) -> str:
    return "\nOR ".join(
        f"(AU-ID({row['author_id']}) AND PUBYEAR AFT {row['latest_seed_year']})"
        for row in author_rows
    )


def fenced(text: str) -> str:
    return f"```text\n{text}\n```"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    seeds = load_csv(SEEDS_PATH)
    db_rows = load_csv(DB_PATH)
    db_by_eid = {row["EID"]: row for row in db_rows if row.get("EID")}

    author_data: dict[str, dict[str, object]] = {}
    seed_author_rows: list[dict[str, object]] = []
    seed_matches = 0

    for seed in seeds:
        db_row = db_by_eid.get(seed["eid"])
        if not db_row:
            raise KeyError(f"Seed EID not found in complete metadata: {seed['eid']}")
        seed_matches += 1
        year = int(seed["year"])
        authors = parse_authors(db_row)
        for position, (name, author_id) in enumerate(authors, start=1):
            data = author_data.setdefault(
                author_id,
                {
                    "author_id": author_id,
                    "name": name,
                    "seed_ids": set(),
                    "seed_years": [],
                    "seed_titles": [],
                    "first_author_seed_ids": set(),
                },
            )
            if len(name) > len(str(data["name"])):
                data["name"] = name
            data["seed_ids"].add(int(seed["seed_id"]))
            data["seed_years"].append(year)
            data["seed_titles"].append(seed["title"])
            if position == 1:
                data["first_author_seed_ids"].add(int(seed["seed_id"]))
            seed_author_rows.append(
                {
                    "seed_id": int(seed["seed_id"]),
                    "seed_year": year,
                    "seed_title": seed["title"],
                    "author_position": position,
                    "author_name": name,
                    "author_id": author_id,
                    "is_first_author": position == 1,
                }
            )

    authors: list[dict[str, object]] = []
    for data in author_data.values():
        seed_ids = sorted(data["seed_ids"])
        first_seed_ids = sorted(data["first_author_seed_ids"])
        years = data["seed_years"]
        authors.append(
            {
                "author_id": data["author_id"],
                "author_name": data["name"],
                "seed_count": len(seed_ids),
                "first_author_seed_count": len(first_seed_ids),
                "is_any_first_author": bool(first_seed_ids),
                "is_core_author": bool(first_seed_ids) or len(seed_ids) >= 2,
                "earliest_seed_year": min(years),
                "latest_seed_year": max(years),
                "seed_ids": ";".join(str(value) for value in seed_ids),
                "first_author_seed_ids": ";".join(str(value) for value in first_seed_ids),
                "seed_titles": " || ".join(dict.fromkeys(data["seed_titles"])),
            }
        )

    authors.sort(
        key=lambda row: (
            not bool(row["is_core_author"]),
            -int(row["seed_count"]),
            str(row["author_name"]).lower(),
        )
    )
    primary = sorted(
        [row for row in authors if row["is_any_first_author"]],
        key=lambda row: (-int(row["latest_seed_year"]), str(row["author_name"]).lower()),
    )
    core = sorted(
        [row for row in authors if row["is_core_author"]],
        key=lambda row: (-int(row["latest_seed_year"]), str(row["author_name"]).lower()),
    )
    all_authors = sorted(
        authors,
        key=lambda row: (-int(row["latest_seed_year"]), str(row["author_name"]).lower()),
    )

    author_map_path = OUT_DIR / "seed_author_map.csv"
    fieldnames = [
        "author_id",
        "author_name",
        "seed_count",
        "first_author_seed_count",
        "is_any_first_author",
        "is_core_author",
        "earliest_seed_year",
        "latest_seed_year",
        "seed_ids",
        "first_author_seed_ids",
        "seed_titles",
    ]
    with author_map_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(authors)

    seed_author_path = OUT_DIR / "seed_author_positions.csv"
    with seed_author_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(seed_author_rows[0]))
        writer.writeheader()
        writer.writerows(seed_author_rows)

    primary_unbounded = author_union([str(row["author_id"]) for row in primary])
    primary_followup = followup_union(primary)
    core_followup = followup_union(core)
    all_followup = followup_union(all_authors)
    core_programming = f"({core_followup})\nAND\n{PROGRAMMING_TERMS}"
    core_genai = f"({core_followup})\nAND\n{GENAI_PROGRAMMING_TERMS}"

    all_chunks: list[tuple[int, str]] = []
    chunk_size = 15
    for index in range(0, len(all_authors), chunk_size):
        chunk = all_authors[index : index + chunk_size]
        all_chunks.append((index // chunk_size + 1, followup_union(chunk)))

    core_table = [
        "| Author | Scopus Author ID | Role in seeds | Seed count | Last seed year | Seed IDs |",
        "|---|---:|---|---:|---:|---|",
    ]
    for row in core:
        role = "first author" if row["is_any_first_author"] else "recurring coauthor"
        core_table.append(
            f"| {row['author_name']} | {row['author_id']} | {role} | {row['seed_count']} | "
            f"{row['latest_seed_year']} | {row['seed_ids']} |"
        )

    chunk_sections = []
    for number, query in all_chunks:
        chunk_sections.append(f"### Query E{number}: all-author follow-up chunk {number}\n\n{fenced(query)}")

    report = f"""# Scopus Queries for the Later Publications of the 20 Seed Papers' Authors

## Validation and definitions

- Seed records matched to complete Scopus metadata by EID: {seed_matches}/{len(seeds)}.
- Unique authors across all 20 seeds: {len(all_authors)}.
- Unique first authors: {len(primary)}.
- Core authors: {len(core)}.
- `core author` means either first author on at least one seed or an author appearing on at least two seed papers.
- Each follow-up clause uses `PUBYEAR AFT <latest seed year>` and therefore retrieves strict later calendar years after that author's last seed contribution.
- Scopus author profiles can be split or merged incorrectly. After retrieval, inspect the author profiles of important cases for alternate Author IDs.

## Core author map

{chr(10).join(core_table)}

## Recommended execution order

1. Run Query E0 to retrieve strict post-seed publications by all 36 authors. This is the primary exhaustive author-follow-up search.
2. If Scopus rejects the combined query because of interface/query-length constraints, run E1–E3 and merge the exports by EID.
3. Retain author role fields from `seed_author_map.csv` so first authors, recurring core coauthors, and other coauthors can be compared rather than pooled blindly.
4. Run Query D1 and D2 as topical views, not as replacements for the exhaustive E query.
5. Query A/B/C remain useful sensitivity analyses for complete careers, first-author continuity, and core-author continuity.

## Query A: all publications by the 15 unique first authors

This intentionally has no date or subject filter. It is the most robust export for reconstructing complete author trajectories locally.

{fenced(primary_unbounded)}

## Query B: strict post-seed publications by first authors

{fenced(primary_followup)}

## Query C: strict post-seed publications by 20 core authors

{fenced(core_followup)}

## Query D1: core-author follow-up restricted to programming-related topics

{fenced(core_programming)}

## Query D2: core-author follow-up restricted to modern GenAI-assisted programming

{fenced(core_genai)}

## Query E: strict post-seed publications by every seed author

### Query E0: all 36 authors in one combined query

{fenced(all_followup)}

Use E1–E3 below only as a fallback if the Scopus interface rejects E0 or if smaller exports are easier to manage.

{chr(10).join(chunk_sections)}

## Export recommendation

Export CSV with at least: authors, full author names, Author IDs, title, year, source title, cited-by count, DOI, EID, abstract, author keywords, and index keywords. If Scopus offers a `References` export option, include it; otherwise the export can reconstruct topics and careers but not the complete cited-reference matrix.
"""
    (OUT_DIR / "scopus_author_followup_queries.md").write_text(report, encoding="utf-8")
    (OUT_DIR / "all_36_authors_followup_query.txt").write_text(all_followup + "\n", encoding="utf-8")

    print(f"seed_matches={seed_matches}")
    print(f"unique_authors={len(all_authors)}")
    print(f"unique_first_authors={len(primary)}")
    print(f"core_authors={len(core)}")
    print(f"all_author_chunks={len(all_chunks)}")
    print(f"author_map={author_map_path}")
    print(f"queries={OUT_DIR / 'scopus_author_followup_queries.md'}")


if __name__ == "__main__":
    main()

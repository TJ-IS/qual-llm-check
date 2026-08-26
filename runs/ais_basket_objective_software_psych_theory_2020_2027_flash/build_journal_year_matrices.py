#!/usr/bin/env python3
"""Build reproducible journal-by-year count matrices from screening decisions."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = RUN_DIR / "output_v1"
YEARS = list(range(2020, 2028))
ABBREVIATIONS = {
    "Information Systems Research": "ISR",
    "MIS Quarterly": "MISQ",
    "Decision Support Systems": "DSS",
    "Journal of the Association for Information Systems": "JAIS",
    "Information & Management": "I&M",
    "European Journal of Information Systems": "EJIS",
    "Information Systems Journal": "ISJ",
    "Journal of Management Information Systems": "JMIS",
    "Journal of Information Technology": "JIT",
    "Information and Organization": "I&O",
    "The Journal of Strategic Information Systems": "JSIS",
}


def main() -> None:
    with (OUTPUT_DIR / "decisions.jsonl").open("r", encoding="utf-8") as handle:
        rows = [json.loads(line) for line in handle if line.strip()]

    journals = sorted(ABBREVIATIONS, key=lambda name: (name != "Information Systems Research", name))
    corpus = Counter((row["journal"], int(row["year"])) for row in rows)
    base = Counter(
        (row["journal"], int(row["year"])) for row in rows if row.get("base_match") is True
    )
    theory = Counter(
        (row["journal"], int(row["year"]))
        for row in rows
        if row.get("theory_guided_subset_match") is True
    )

    def matrix(counter: Counter[tuple[str, int]]) -> list[dict[str, object]]:
        result = []
        for journal in journals:
            counts = {str(year): counter[(journal, year)] for year in YEARS}
            result.append(
                {
                    "journal": journal,
                    "abbreviation": ABBREVIATIONS[journal],
                    "counts": counts,
                    "total": sum(counts.values()),
                }
            )
        return result

    base_matrix = matrix(base)
    theory_matrix = matrix(theory)
    payload = {
        "years": YEARS,
        "base": base_matrix,
        "theory": theory_matrix,
        "journal_summary": [
            {
                "journal": journal,
                "abbreviation": ABBREVIATIONS[journal],
                "corpus_total": sum(corpus[(journal, year)] for year in YEARS),
                "base_total": sum(base[(journal, year)] for year in YEARS),
                "theory_total": sum(theory[(journal, year)] for year in YEARS),
            }
            for journal in journals
        ],
    }
    (OUTPUT_DIR / "journal_year_matrices.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    for filename, data in (
        ("journal_year_base_matrix.csv", base_matrix),
        ("journal_year_theory_matrix.csv", theory_matrix),
    ):
        with (OUTPUT_DIR / filename).open("w", encoding="utf-8-sig", newline="") as handle:
            fields = ["journal", "abbreviation", *map(str, YEARS), "total"]
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            for item in data:
                writer.writerow(
                    {
                        "journal": item["journal"],
                        "abbreviation": item["abbreviation"],
                        **item["counts"],
                        "total": item["total"],
                    }
                )

    with (OUTPUT_DIR / "journal_totals_summary.csv").open(
        "w", encoding="utf-8-sig", newline=""
    ) as handle:
        fields = ["journal", "abbreviation", "corpus_total", "base_total", "theory_total"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(payload["journal_summary"])

    print(json.dumps(payload, ensure_ascii=False))


if __name__ == "__main__":
    main()

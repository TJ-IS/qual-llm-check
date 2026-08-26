#!/usr/bin/env python3
"""Back-test programming search variants against recent citing-paper candidates."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
ROOT = RUN_DIR.parents[1]
SCOPUS_CSV = ROOT / "runs" / "ref_20_coding.csv"
DECISIONS_CSV = RUN_DIR / "output_v1" / "decisions.csv"
OUTPUT_JSON = RUN_DIR / "query_recall_evaluation.json"
OUTPUT_CSV = RUN_DIR / "recent_query_match_matrix.csv"
FIELDS = ("Title", "Abstract", "Author Keywords", "Index Keywords")

STRICT_Q1 = (
    r"program comprehension|code comprehension|programming tasks?|coding tasks?|"
    r"pair programming|test[- ]driven development|end[- ]user programming|"
    r"AI[- ]assisted (?:programming|coding)|coding agents?|programming agents?|"
    r"(?:programming|coding|code) assistants?|"
    r"code review|code inspection|code completion|code auto[- ]?complet(?:e|ion)|"
    r"code suggestions?|writing code"
)

LEGACY_EXPANDED_Q2 = (
    r"computer program(?:ming|s)?|source code|program comprehension|"
    r"code comprehension|\bprogrammers?\b|software developers?|coding tasks?|"
    r"programming tasks?|\bdebugging\b|pair programming|"
    r"test[- ]driven development|end[- ]user programming|"
    r"spreadsheet (?:programming|development|debugging|testing|error correction)|"
    r"query formulation|query development|\bSQL quer(?:y|ies)\b|"
    r"instantiations? of data models?|AI[- ]assisted (?:programming|coding)|"
    r"coding agents?|programming assistants?|code generation|code review|"
    r"code inspection|code modification|code completion|"
    r"code auto[- ]?complet(?:e|ion)|code suggestions?|writing code|"
    r"open[- ]source software development"
)

PROFESSIONAL_REFINED_Q8 = (
    r"(?:computer )?program comprehension|program understanding|"
    r"software comprehension|software modification|"
    r"programming tasks?|programming performance|programmer performance|"
    r"programming productivity|programming environments?|"
    r"program construction|program maintenance|maintainable software|"
    r"query formulation|query development|query reuse|query complexity|"
    r"structured query languages?|"
    r"spreadsheet (?:errors?|testing|development|debugging|programming|"
    r"error correction|code inspection|formulas?|models?)|"
    r"end[- ]user (?:programming|development)|"
    r"end[- ]user computing.{0,50}(?:programming|productivity|spreadsheet)|"
    r"(?:programming|productivity|spreadsheet).{0,50}end[- ]user computing|"
    r"pair programming|test[- ]driven development|"
    r"code inspect(?:ion|ing)|code review|(?:program|code) debugging|"
    r"knowledge[- ]based systems? development|database structure representation|"
    r"AI[- ]assisted (?:programming|coding)|coding agents?|programming agents?|"
    r"(?:programming|coding|code) assistants?|code generation|"
    r"code completion|code auto[- ]?complet(?:e|ion)|code suggestions?|"
    r"writing code"
)

MODERN_AGENT_Q3 = (
    r"AI[- ]assisted (?:programming|coding|software development)|"
    r"AI pair programmers?|coding agents?|programming agents?|"
    r"programming assistants?|coding assistants?|code assistants?|"
    r"code completion|code auto[- ]?complet(?:e|ion)|code suggestions?|"
    r"GitHub Copilot|OpenAI Codex|just[- ]generated code|generated code|"
    r"test generation|test skeletons?|"
    r"(?:large language models?|\bLLMs?\b|ChatGPT|generative AI).{0,120}"
    r"(?:programming|coding|source code|code generation|code completion|"
    r"program comprehension|program repair|test generation|SQL)|"
    r"(?:programming|coding|source code|code generation|code completion|"
    r"program comprehension|program repair|test generation|SQL).{0,120}"
    r"(?:large language models?|\bLLMs?\b|ChatGPT|generative AI)"
)

HIGH_RECALL_Q9 = (
    r"program comprehension|code comprehension|software comprehension|"
    r"program understanding|code understanding|code reading|reading (?:source )?code|"
    r"code exploration|programming tasks?|coding tasks?|"
    r"programming performance|programmer performance|programming productivity|"
    r"programming practices?|programming patterns?|programming environments?|"
    r"introductory programming|programming education|novice programmers?|"
    r"pair programming|test[- ]driven development|"
    r"code review|code inspect(?:ion|ing)|"
    r"(?:program|code|source code) debugging|"
    r"debugging.{0,50}(?:program|code|python|java|software)|"
    r"bug fixing|fault locali[sz]ation|program repair|"
    r"test generation|test skeletons?|unit test generation|"
    r"code modification|program modification|code refactor(?:ing)?|"
    r"query formulation|query development|query reuse|query complexity|"
    r"structured query languages?|text[- ]to[- ](?:SQL|SPARQL|Cypher)|"
    r"\bSQL\b.{0,80}(?:query|learn|teach|error|debug|write|formulat|skill)|"
    r"(?:query|learn|teach|error|debug|write|formulat|skill).{0,80}\bSQL\b|"
    r"spreadsheet (?:errors?|testing|development|debugging|programming|"
    r"error correction|code inspection|formulas?|models?)|"
    r"end[- ]user programming|low.?code|"
    r"visual programming|execution logs?|execution log analysis|"
    r"code generation|generat(?:e|ed|ing) code|"
    r"code completion|code auto[- ]?complet(?:e|ion)|code suggestions?|"
    r"AI[- ]assisted (?:programming|coding|software development)|"
    r"AI pair programmers?|coding agents?|programming agents?|"
    r"(?:programming|coding|code) assistants?|GitHub Copilot|OpenAI Codex|"
    r"(?:large language models?|\bLLMs?\b|ChatGPT|generative AI).{0,120}"
    r"(?:programming|coding|source code|code generation|code completion|"
    r"program comprehension|program repair|test generation|SQL)|"
    r"(?:programming|coding|source code|code generation|code completion|"
    r"program comprehension|program repair|test generation|SQL).{0,120}"
    r"(?:large language models?|\bLLMs?\b|ChatGPT|generative AI)"
)

VARIANTS = {
    "Q1_title_high_precision": {
        "pattern": re.compile(STRICT_Q1, re.IGNORECASE),
        "fields": ("Title",),
    },
    "Q1_title_abstract_keywords": {
        "pattern": re.compile(STRICT_Q1, re.IGNORECASE),
        "fields": FIELDS,
    },
    "Q2_legacy_expanded": {
        "pattern": re.compile(LEGACY_EXPANDED_Q2, re.IGNORECASE),
        "fields": FIELDS,
    },
    "Q8_ais_professional_refined": {
        "pattern": re.compile(PROFESSIONAL_REFINED_Q8, re.IGNORECASE),
        "fields": FIELDS,
    },
    "Q3_modern_agent_supplement": {
        "pattern": re.compile(MODERN_AGENT_Q3, re.IGNORECASE),
        "fields": FIELDS,
    },
    "Q9_cross_domain_high_recall": {
        "pattern": re.compile(HIGH_RECALL_Q9, re.IGNORECASE),
        "fields": FIELDS,
    },
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    records = read_csv(SCOPUS_CSV)
    decisions = read_csv(DECISIONS_CSV)
    decision_by_eid = {
        (row.get("article_id") or "").strip(): row
        for row in decisions
        if (row.get("article_id") or "").strip()
    }

    recent = [
        row for row in records if int((row.get("Year") or "0").strip() or 0) >= 2021
    ]
    matrix: list[dict[str, str]] = []
    for row in recent:
        eid = (row.get("EID") or "").strip()
        decision = decision_by_eid[eid]
        item = {
            "eid": eid,
            "doi": (row.get("DOI") or "").strip(),
            "title": (row.get("Title") or "").strip(),
            "year": (row.get("Year") or "").strip(),
            "source_title": (row.get("Source title") or "").strip(),
            "screening_label": decision["screening_label"],
            "actor_type": decision["actor_type"],
        }
        for name, spec in VARIANTS.items():
            text = " ".join((row.get(field) or "") for field in spec["fields"])
            item[name] = str(bool(spec["pattern"].search(text)))
        matrix.append(item)

    labels = {
        "likely_direct": {
            (row.get("article_id") or "").strip()
            for row in decisions
            if row.get("screening_label") == "likely_direct"
        },
        "possible_direct": {
            (row.get("article_id") or "").strip()
            for row in decisions
            if row.get("screening_label") == "possible_direct"
        },
    }

    evaluation: dict[str, dict] = {}
    for name, spec in VARIANTS.items():
        all_hits = []
        recent_hits = []
        for row in records:
            text = " ".join((row.get(field) or "") for field in spec["fields"])
            if spec["pattern"].search(text):
                all_hits.append(row)
                if int((row.get("Year") or "0").strip() or 0) >= 2021:
                    recent_hits.append(row)
        recent_eids = {(row.get("EID") or "").strip() for row in recent_hits}
        likely_hits = recent_eids & labels["likely_direct"]
        possible_hits = recent_eids & labels["possible_direct"]
        evaluation[name] = {
            "fields": list(spec["fields"]),
            "all_807_hits": len(all_hits),
            "recent_176_hits": len(recent_hits),
            "likely_direct_30_hits": len(likely_hits),
            "likely_direct_recall": len(likely_hits) / len(labels["likely_direct"]),
            "possible_direct_3_hits": len(possible_hits),
            "inclusive_33_hits": len(likely_hits | possible_hits),
            "inclusive_recall": len(likely_hits | possible_hits)
            / (len(labels["likely_direct"]) + len(labels["possible_direct"])),
            "recent_not_direct_hits": len(recent_hits)
            - len(likely_hits)
            - len(possible_hits),
            "likely_direct_precision_proxy": (
                len(likely_hits) / len(recent_hits) if recent_hits else None
            ),
            "missed_likely_direct": [
                {
                    "title": row["title"],
                    "year": row["year"],
                    "source": row["source_title"],
                    "actor_type": row["actor_type"],
                }
                for row in matrix
                if row["screening_label"] == "likely_direct"
                and row[name] != "True"
            ],
            "missed_possible_direct": [
                {
                    "title": row["title"],
                    "year": row["year"],
                    "source": row["source_title"],
                }
                for row in matrix
                if row["screening_label"] == "possible_direct"
                and row[name] != "True"
            ],
        }

    payload = {
        "source_records": len(records),
        "recent_records_2021plus": len(recent),
        "screening_reference": {
            "likely_direct": len(labels["likely_direct"]),
            "possible_direct": len(labels["possible_direct"]),
        },
        "variants": evaluation,
    }
    OUTPUT_JSON.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    with OUTPUT_CSV.open("w", encoding="utf-8-sig", newline="") as handle:
        fields = list(matrix[0])
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(matrix)
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "database" / "ALL_AIS_Basket_11.csv"
OUT_DIR = ROOT / "runs" / "coding_agent_ux_misq_isr"
OUT_CSV = OUT_DIR / "27_individual_level_coordination_foundation_records.csv"
OUT_MD = OUT_DIR / "28_individual_level_coordination_foundation_records.md"


JOURNAL_PRIORITY = {
    "MIS Quarterly: Management Information Systems": 13,
    "MIS Quarterly": 13,
    "Information Systems Research": 12,
    "Journal of Management Information Systems": 11,
    "Journal of the Association for Information Systems": 10,
    "European Journal of Information Systems": 9,
    "Information Systems Journal": 9,
    "Information and Management": 8,
    "Decision Support Systems": 8,
    "Journal of Information Technology": 8,
    "Journal of Strategic Information Systems": 8,
    "Information and Organization": 7,
}


PATTERNS = [
    ("individual_marker", r"\bindividual(?:s| level)?\b|\buser(?:s)?\b|\bdeveloper(?:s)?\b|\bmember(?:s)?\b|\bparticipant(?:s)?\b|\bemployee(?:s)?\b|\bworker(?:s)?\b|\bmanager(?:s)?\b", 20, 8),
    ("perceived_marker", r"\bperceived\b|\bperception(?:s)?\b|\bsatisfaction\b|\bintention\b|\bwillingness\b|\bexperience\b|\bself-reported\b|\breported\b", 28, 12),
    ("coordination_effort_cost", r"\bcoordination costs?\b|\bcoordination efforts?\b|\bcoordination burden\b|\bcoordination load\b|\bcoordination demand(?:s)?\b", 85, 48),
    ("collaboration_overload_cost", r"\bcollaboration overload\b|\bcollaborative overload\b|\bcollaboration costs?\b|\bcollaboration efforts?\b|\bcollaborative efforts?\b|\bcollaboration burden\b", 90, 50),
    ("communication_overload", r"\bcommunication overload\b|\binformation overload\b|\bemail overload\b|\bmessage overload\b|\balert overload\b|\bnotification overload\b", 70, 34),
    ("coordination_process_outcome", r"\bprocess satisfaction\b|\bcoordination success\b|\bcoordination quality\b|\bteam conflict\b|\bselection conflict\b|\bgoal conflict\b", 55, 28),
    ("collaboration_quality", r"\bcollaboration quality\b|\bcollaborative quality\b|\bteamwork quality\b|\bcooperation quality\b|\bcooperative quality\b", 55, 26),
    ("software_individual", r"\bsoftware developer(?:s)?\b|\bapp developer(?:s)?\b|\bsoftware development team member(?:s)?\b|\bprogrammer(?:s)?\b|\bcoding\b|\bsoftware design\b", 70, 34),
    ("human_ai_delegation_individual", r"\bhuman-ai\b|\bAI delegation\b|\bdelegate .* AI\b|\bdelegate .* agent\b|\bagentic IS\b|\bagentic artifact(?:s)?\b", 75, 38),
    ("monitoring_verification_effort", r"\bmonitoring\b|\bverification\b|\binspection\b|\bchecking\b|\battention\b|\bawareness\b|\bmetaknowledge\b", 35, 16),
    ("task_interdependence", r"\btask interdependence\b|\binterdependencies\b|\binterdependence\b|\bdependency\b", 48, 24),
]


ORG_LEVEL_HINTS = re.compile(
    r"\bfirm-level\b|\bfirm performance\b|\bmarket value\b|\borganization(?:al)?\b|\bindustry\b|\bsupply chain\b|\binterfirm\b|\bintrafirm\b|\becosystem\b|\bplatform governance\b|\bproject(?:'s)? form of coordination\b",
    re.I,
)


def compact(value, max_len=1000):
    value = re.sub(r"\s+", " ", (value or "")).strip()
    if len(value) <= max_len:
        return value
    return value[: max_len - 3].rstrip() + "..."


def classify_level(text):
    text_l = text.lower()
    individual = bool(re.search(r"\bindividual(?:s| level)?\b|\buser(?:s)?\b|\bdeveloper(?:s)?\b|\bmember(?:s)?\b|\bparticipant(?:s)?\b|\bemployee(?:s)?\b|\bworker(?:s)?\b|\bmanager(?:s)?\b|\bsubject(?:s)?\b", text_l))
    perceived = bool(re.search(r"\bperceived\b|\bperception(?:s)?\b|\bsatisfaction\b|\bintention\b|\bwillingness\b|\bexperience\b|\bself-reported\b|\breported\b", text_l))
    org = bool(ORG_LEVEL_HINTS.search(text_l))
    if individual and perceived:
        return "individual/perceived"
    if individual:
        return "individual-adjacent"
    if perceived and not org:
        return "perception-adjacent"
    if org:
        return "macro/background"
    return "unclear"


def score_row(row):
    title = row.get("Title", "") or ""
    abstract = row.get("Abstract", "") or ""
    keywords = " ".join([row.get("Author Keywords", "") or "", row.get("Index Keywords", "") or ""])
    source = row.get("Source title", "") or ""
    text = f"{title} {abstract} {keywords}"
    title_l = title.lower()
    abstract_l = abstract.lower()
    keywords_l = keywords.lower()

    score = JOURNAL_PRIORITY.get(source, 5)
    hits = []
    for label, pattern, title_weight, text_weight in PATTERNS:
        regex = re.compile(pattern, re.I)
        if regex.search(title_l):
            score += title_weight
            hits.append(f"{label}:title")
        if regex.search(abstract_l):
            score += text_weight
            hits.append(f"{label}:abstract")
        if regex.search(keywords_l):
            score += int(text_weight * 0.7)
            hits.append(f"{label}:keywords")

    level = classify_level(text)
    if level == "individual/perceived":
        score += 55
    elif level == "individual-adjacent":
        score += 28
    elif level == "macro/background":
        score -= 35

    # Reward records where individual-level experience is tied to coordination/collaboration.
    has_coord_or_collab = bool(re.search(r"\bcoordination\b|\bcollaboration\b|\bcollaborative\b|\bcooperation\b|\binterdependence\b", text, re.I))
    has_effort_or_load = bool(re.search(r"\bcost(?:s)?\b|\beffort(?:s)?\b|\bburden\b|\boverload\b|\bload\b|\bdemand(?:s)?\b|\bconflict\b|\bsatisfaction\b", text, re.I))
    has_individual = bool(re.search(r"\bindividual(?:s| level)?\b|\buser(?:s)?\b|\bdeveloper(?:s)?\b|\bmember(?:s)?\b|\bparticipant(?:s)?\b|\bemployee(?:s)?\b|\bworker(?:s)?\b|\bmanager(?:s)?\b", text, re.I))
    if has_coord_or_collab and has_effort_or_load and has_individual:
        score += 70
        hits.append("combo:individual+coordination/collaboration+cost/load/outcome")

    try:
        year = int(row.get("Year", "") or 0)
    except ValueError:
        year = 0
    if year >= 2020:
        score += 7
    elif year >= 2010:
        score += 4

    return score, sorted(set(hits)), level


def main():
    records = []
    with DATA.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            score, hits, level = score_row(row)
            if score >= 95 and hits and level == "individual/perceived":
                records.append(
                    {
                        "score": score,
                        "level": level,
                        "hits": "; ".join(hits),
                        "title": row.get("Title", ""),
                        "year": row.get("Year", ""),
                        "source": row.get("Source title", ""),
                        "doi": row.get("DOI", ""),
                        "abstract": compact(row.get("Abstract", ""), 1450),
                        "author_keywords": compact(row.get("Author Keywords", ""), 400),
                        "index_keywords": compact(row.get("Index Keywords", ""), 400),
                    }
                )

    records.sort(key=lambda r: (r["level"] != "individual/perceived", -r["score"], -(int(r["year"] or 0)), r["title"]))

    fields = [
        "score",
        "level",
        "hits",
        "title",
        "year",
        "source",
        "doi",
        "abstract",
        "author_keywords",
        "index_keywords",
    ]
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for record in records:
            writer.writerow(record)

    top = records[:90]
    lines = [
        "# Individual-Level Coordination Foundation Records",
        "",
        f"Data source: `{DATA}`",
        "",
        f"Records retained: {len(records)}. Top records shown below: {len(top)}.",
        "",
        "Purpose: find strictly individual/perceived foundations for adapting a coordination/collaboration burden concept to coding-agent UX.",
        "",
    ]
    for i, r in enumerate(top, 1):
        lines.extend(
            [
                f"## {i}. {r['title']} ({r['year']}, {r['source']})",
                "",
                f"- Score: {r['score']}",
                f"- Level classification: {r['level']}",
                f"- DOI: {r['doi']}",
                f"- Hits: {r['hits']}",
                f"- Abstract: {r['abstract']}",
                "",
            ]
        )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8-sig")
    print(f"Wrote {OUT_CSV}")
    print(f"Wrote {OUT_MD}")
    print(f"Retained {len(records)} records")
    for r in top[:18]:
        print(f"{r['score']:>4} | {r['level']:<22} | {r['year']} | {r['source']} | {r['title']}")


if __name__ == "__main__":
    main()

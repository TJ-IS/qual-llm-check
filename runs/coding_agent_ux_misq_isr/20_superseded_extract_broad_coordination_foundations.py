import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "database" / "ALL_AIS_Basket_11.csv"
OUT_DIR = ROOT / "runs" / "coding_agent_ux_misq_isr"
OUT_CSV = OUT_DIR / "21_superseded_broad_coordination_foundation_records.csv"
OUT_MD = OUT_DIR / "22_superseded_broad_coordination_foundation_records.md"


JOURNAL_PRIORITY = {
    "MIS Quarterly": 12,
    "Information Systems Research": 11,
    "Journal of Management Information Systems": 10,
    "Journal of the Association for Information Systems": 9,
    "European Journal of Information Systems": 8,
    "Information Systems Journal": 8,
    "Information and Management": 7,
    "Decision Support Systems": 7,
    "Journal of Information Technology": 7,
    "Journal of Strategic Information Systems": 7,
    "Journal of Information Systems": 6,
}


PATTERNS = [
    ("coordination_cost", r"\bcoordination costs?\b|\bcoordination efforts?\b|\bcoordination burden\b", 90, 55),
    ("coordination_breakdown", r"\bcoordination breakdowns?\b|\bcoordination problems?\b|\bcoordination complexity\b", 70, 35),
    ("task_interdependence", r"\btask interdependence\b|\binterdependent tasks?\b|\binterdependencies\b|\binterdependence\b", 55, 25),
    ("software_project_coordination", r"\bsoftware project coordination\b|\bcoordination in software\b|\bsoftware development teams?\b|\bcross-team coordination\b", 120, 50),
    ("artifact_based_coordination", r"\bartifact-based coordination\b|\bauthority-based coordination\b|\bpropagation costs?\b|\bdesign structure matrices?\b", 130, 60),
    ("expertise_coordination", r"\bexpertise coordination\b|\bcoordinating expertise\b|\bexpertise location\b", 85, 35),
    ("technology_enabled_coordination", r"\btechnology-enabled coordination\b|\bcoordination affordances?\b|\bcoordination episodes?\b|\btechnology .* coordination\b", 120, 55),
    ("communication_visibility", r"\bcommunication visibility\b|\bmessage transparency\b|\bnetwork translucence\b|\bambient awareness\b|\bmetaknowledge\b", 60, 28),
    ("delegation_coordination", r"\bis delegation\b|\bagentic is\b|\bdelegation .* coordination\b|\bdelegat(?:e|ion) to .* artifacts?\b", 95, 45),
    ("handoff_monitoring", r"\bhandoff\b|\bmonitoring\b|\boversight\b|\bsupervisory control\b|\bverification\b", 35, 14),
    ("attention_approval_adjacent", r"\binterruption overload\b|\bwarning fatigue\b|\bwarning habituation\b|\bapproval\b|\bnotification\b", 30, 12),
    ("technostress_adjacent", r"\btechnostress\b|\bwork overload\b|\brole ambiguity\b|\btechnology overload\b", 35, 16),
]


def compact(value, max_len=950):
    value = re.sub(r"\s+", " ", (value or "")).strip()
    if len(value) <= max_len:
        return value
    return value[: max_len - 3].rstrip() + "..."


def first_sentence(value):
    value = compact(value, 1200)
    parts = re.split(r"(?<=[.!?])\s+", value)
    return parts[0] if parts else value


def score_row(row):
    title = row.get("Title", "") or ""
    abstract = row.get("Abstract", "") or ""
    keywords = " ".join([row.get("Author Keywords", "") or "", row.get("Index Keywords", "") or ""])
    source = row.get("Source title", "") or ""
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
            score += int(text_weight * 0.75)
            hits.append(f"{label}:keywords")

    # Reward records that combine a general coordination concept with software, artifact,
    # delegation, or technology mediation. Those are the likely foundations for a
    # coding-agent-specific adaptation.
    has_coord = bool(re.search(r"\bcoordination\b|\binterdependence\b|\binterdependencies\b", f"{title_l} {abstract_l} {keywords_l}"))
    has_software = bool(re.search(r"\bsoftware\b|\bcode\b|\bprogramming\b|\bdevelopment\b|\bopen source\b|\barchitecture\b", f"{title_l} {abstract_l} {keywords_l}"))
    has_artifact = bool(re.search(r"\bartifact\b|\barchitecture\b|\bpropagation costs?\b|\bcodebase\b|\brepository\b", f"{title_l} {abstract_l} {keywords_l}"))
    has_tech_mediation = bool(re.search(r"\btechnology\b|\binformation system\b|\bplatform\b|\bsocial media\b|\bcoordination affordance", f"{title_l} {abstract_l} {keywords_l}"))
    has_delegation = bool(re.search(r"\bdelegat|\bagentic\b|\bagent\b", f"{title_l} {abstract_l} {keywords_l}"))
    if has_coord and has_software:
        score += 55
        hits.append("combo:coordination+software")
    if has_coord and has_artifact:
        score += 45
        hits.append("combo:coordination+artifact")
    if has_coord and has_tech_mediation:
        score += 35
        hits.append("combo:coordination+technology")
    if has_coord and has_delegation:
        score += 45
        hits.append("combo:coordination+delegation")

    try:
        year = int(row.get("Year", "") or 0)
    except ValueError:
        year = 0
    if year >= 2020:
        score += 8
    elif year >= 2010:
        score += 5

    return score, sorted(set(hits))


def main():
    records = []
    with DATA.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            score, hits = score_row(row)
            if score >= 70 and hits:
                records.append(
                    {
                        "score": score,
                        "hits": "; ".join(hits),
                        "title": row.get("Title", ""),
                        "year": row.get("Year", ""),
                        "source": row.get("Source title", ""),
                        "doi": row.get("DOI", ""),
                        "abstract": compact(row.get("Abstract", ""), 1500),
                        "first_sentence": first_sentence(row.get("Abstract", "")),
                        "author_keywords": compact(row.get("Author Keywords", ""), 450),
                        "index_keywords": compact(row.get("Index Keywords", ""), 450),
                    }
                )

    records.sort(key=lambda r: (-r["score"], -(int(r["year"] or 0)), r["title"]))

    fields = [
        "score",
        "hits",
        "title",
        "year",
        "source",
        "doi",
        "first_sentence",
        "abstract",
        "author_keywords",
        "index_keywords",
    ]
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for record in records:
            writer.writerow(record)

    top = records[:80]
    lines = [
        "# Coordination Burden Foundation Records",
        "",
        f"Data source: `{DATA}`",
        "",
        f"Records retained: {len(records)}. Top records shown below: {len(top)}.",
        "",
        "Purpose: find the best existing conceptual starting point for a coding-agent-specific construct around coordination burden. This file is evidence extraction only; construct judgment is written separately.",
        "",
    ]
    for i, r in enumerate(top, 1):
        lines.extend(
            [
                f"## {i}. {r['title']} ({r['year']}, {r['source']})",
                "",
                f"- Score: {r['score']}",
                f"- DOI: {r['doi']}",
                f"- Hits: {r['hits']}",
                f"- First abstract sentence: {r['first_sentence']}",
                f"- Abstract: {r['abstract']}",
                "",
            ]
        )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8-sig")
    print(f"Wrote {OUT_CSV}")
    print(f"Wrote {OUT_MD}")
    print(f"Retained {len(records)} records")
    for r in top[:12]:
        print(f"{r['score']:>4} | {r['year']} | {r['source']} | {r['title']}")


if __name__ == "__main__":
    main()

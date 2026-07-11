import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(r"E:\github\qual-llm-check-IS-utd")
CSV_PATH = ROOT / "database" / "ALL_AIS_Basket_11.csv"
OUT_DIR = ROOT / "runs" / "coding_agent_ux_misq_isr"
OUT_MD = OUT_DIR / "14_top11_concept_lineage_search_results.md"
OUT_CSV = OUT_DIR / "13_top11_concept_lineage_candidates.csv"


THEMES = {
    "is_delegation_agentic_is": {
        "label": "IS delegation / agentic IS use",
        "terms": [
            r"\bdelegat(e|es|ed|ing|ion)\b",
            r"\bagentic\b",
            r"\bagent\b",
            r"\bagents\b",
            r"\bautonomous agent\b",
            r"\bAI agent\b",
            r"\bagent-based\b",
            r"\bprincipal-agent\b",
            r"\btask allocation\b",
            r"\bautomation\b",
            r"\bautomated\b",
        ],
    },
    "coordination_collaboration": {
        "label": "coordination / collaboration / handoff",
        "terms": [
            r"\bcoordination\b",
            r"\bcoordinate\b",
            r"\bcollaboration\b",
            r"\bcollaborative\b",
            r"\bcooperation\b",
            r"\bcooperative\b",
            r"\bhandoff\b",
            r"\bhand-off\b",
            r"\bteamwork\b",
            r"\binterdependen(t|ce)\b",
            r"\bworkflow\b",
            r"\bcollaborative work\b",
        ],
    },
    "control_autonomy": {
        "label": "control / autonomy / controllability",
        "terms": [
            r"\bcontrol\b",
            r"\bcontrolled\b",
            r"\bcontrollability\b",
            r"\bperceived control\b",
            r"\blocus of control\b",
            r"\buser control\b",
            r"\bautonomy\b",
            r"\bautonomous\b",
            r"\bempowerment\b",
            r"\bself-determination\b",
            r"\balgorithmic control\b",
        ],
    },
    "technostress_overload_fatigue": {
        "label": "technostress / overload / fatigue",
        "terms": [
            r"\btechnostress\b",
            r"\btechno-stress\b",
            r"\boverload\b",
            r"\bwork overload\b",
            r"\binformation overload\b",
            r"\bcommunication overload\b",
            r"\brole ambiguity\b",
            r"\bfatigue\b",
            r"\bstrain\b",
            r"\bstress\b",
            r"\bburnout\b",
            r"\bexhaustion\b",
        ],
    },
    "interruption_attention_notification": {
        "label": "interruption / attention / notification",
        "terms": [
            r"\binterruption\b",
            r"\binterruptions\b",
            r"\battention\b",
            r"\battentional\b",
            r"\bnotification\b",
            r"\bnotifications\b",
            r"\bwarning\b",
            r"\bwarnings\b",
            r"\balert\b",
            r"\balerts\b",
            r"\bhabituation\b",
            r"\btask switching\b",
        ],
    },
    "verification_monitoring_oversight": {
        "label": "verification / monitoring / oversight",
        "terms": [
            r"\bverification\b",
            r"\bverify\b",
            r"\bvalidation\b",
            r"\bvalidate\b",
            r"\bmonitoring\b",
            r"\bmonitor\b",
            r"\boversight\b",
            r"\bsupervision\b",
            r"\bsupervisory\b",
            r"\bauditing\b",
            r"\baccountability\b",
            r"\bresponsibility\b",
            r"\bchecking\b",
            r"\breview\b",
        ],
    },
    "transparency_explainability_visibility": {
        "label": "transparency / explainability / visibility",
        "terms": [
            r"\btransparency\b",
            r"\btransparent\b",
            r"\bexplainability\b",
            r"\bexplainable\b",
            r"\bexplanation\b",
            r"\bvisibility\b",
            r"\bvisible\b",
            r"\bobservability\b",
            r"\btraceability\b",
            r"\bawareness\b",
            r"\bfeedback\b",
            r"\binterpretability\b",
        ],
    },
    "trust_reliance_calibration": {
        "label": "trust / reliance / calibration",
        "terms": [
            r"\btrust\b",
            r"\btrustworthy\b",
            r"\breliance\b",
            r"\brely\b",
            r"\brelying\b",
            r"\bcalibration\b",
            r"\boverreliance\b",
            r"\bunderreliance\b",
            r"\bconfidence\b",
            r"\bfaith\b",
        ],
    },
    "is_use_post_adoptive": {
        "label": "IS use / post-adoptive use / feature use",
        "terms": [
            r"\bIS use\b",
            r"\binformation system use\b",
            r"\btechnology use\b",
            r"\bpost-adoptive\b",
            r"\bpost adoptive\b",
            r"\bfeature use\b",
            r"\bdeep use\b",
            r"\bextended use\b",
            r"\badaptive use\b",
            r"\bhabitual use\b",
            r"\broutine use\b",
            r"\bcontinued use\b",
        ],
    },
    "affordance_sociomateriality": {
        "label": "affordance / sociomaterial / technology features",
        "terms": [
            r"\baffordance\b",
            r"\baffordances\b",
            r"\bsociomaterial\b",
            r"\bmateriality\b",
            r"\btechnology features\b",
            r"\bfunctionalities\b",
            r"\bfeature\b",
            r"\bdesign\b",
            r"\bIT artifact\b",
            r"\bartifact\b",
        ],
    },
}


FOCUSED_PHRASES = [
    "IS delegation",
    "agentic IS",
    "agentic artifact",
    "algorithmic control",
    "human-AI collaboration",
    "human AI collaboration",
    "human-machine collaboration",
    "automation monitoring",
    "supervisory control",
    "technostress",
    "interruption overload",
    "warning fatigue",
    "verification",
    "perceived control",
    "user control",
    "transparency",
    "explainability",
    "affordance",
    "adaptive use",
    "post-adoptive",
]


def norm(value):
    return "" if value is None else str(value)


def compact(text, max_len=520):
    text = re.sub(r"\s+", " ", norm(text)).strip()
    return text if len(text) <= max_len else text[: max_len - 1].rstrip() + "…"


def score_theme(text, terms):
    hits = []
    score = 0
    for term in terms:
        pattern = re.compile(term, re.I)
        matches = pattern.findall(text)
        if matches:
            count = len(matches)
            hits.append(term)
            score += count
    return score, hits


def main():
    rows = []
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            text = " ".join(
                [
                    norm(row.get("Title")),
                    norm(row.get("Abstract")),
                    norm(row.get("Author Keywords")),
                    norm(row.get("Index Keywords")),
                ]
            )
            row["_text"] = text
            rows.append(row)

    theme_hits = defaultdict(list)
    phrase_hits = defaultdict(list)
    all_candidates = []

    for idx, row in enumerate(rows):
        text = row["_text"]
        title = norm(row.get("Title"))
        abstract = norm(row.get("Abstract"))
        for theme_key, theme in THEMES.items():
            score, hits = score_theme(text, theme["terms"])
            # Require a stronger score for generic buckets.
            threshold = 2 if theme_key in {"control_autonomy", "affordance_sociomateriality", "trust_reliance_calibration"} else 1
            if score >= threshold:
                record = {
                    "theme": theme_key,
                    "theme_label": theme["label"],
                    "score": score,
                    "hits": "; ".join(hits[:8]),
                    "title": title,
                    "year": norm(row.get("Year")),
                    "journal": norm(row.get("Source title")),
                    "cited_by": norm(row.get("Cited by")),
                    "doi": norm(row.get("DOI")),
                    "link": norm(row.get("Link")),
                    "abstract": compact(abstract, 650),
                    "keywords": compact(" ".join([norm(row.get("Author Keywords")), norm(row.get("Index Keywords"))]), 300),
                }
                theme_hits[theme_key].append(record)
                all_candidates.append(record)

        lower = text.lower()
        for phrase in FOCUSED_PHRASES:
            if phrase.lower() in lower:
                phrase_hits[phrase].append(row)

    for key in theme_hits:
        theme_hits[key].sort(key=lambda r: (int(r["score"]), int(r["cited_by"] or 0) if str(r["cited_by"]).isdigit() else 0), reverse=True)

    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        fieldnames = [
            "theme",
            "theme_label",
            "score",
            "hits",
            "title",
            "year",
            "journal",
            "cited_by",
            "doi",
            "link",
            "abstract",
            "keywords",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for record in sorted(all_candidates, key=lambda r: (r["theme"], -int(r["score"]))):
            writer.writerow(record)

    lines = []
    lines.append("# IS Top11 数据库概念线索检索结果")
    lines.append("")
    lines.append(f"数据源：`{CSV_PATH}`")
    lines.append(f"记录数：{len(rows)}")
    lines.append("")
    lines.append("## 概念家族命中概览")
    lines.append("")
    lines.append("| 概念家族 | 命中文献数 |")
    lines.append("| --- | ---: |")
    for key, theme in THEMES.items():
        lines.append(f"| {theme['label']} | {len(theme_hits[key])} |")
    lines.append("")
    lines.append("## 精确短语命中概览")
    lines.append("")
    lines.append("| 短语 | 命中文献数 |")
    lines.append("| --- | ---: |")
    for phrase in FOCUSED_PHRASES:
        lines.append(f"| `{phrase}` | {len(phrase_hits[phrase])} |")

    for key, theme in THEMES.items():
        lines.append("")
        lines.append(f"## {theme['label']}")
        lines.append("")
        for i, rec in enumerate(theme_hits[key][:25], 1):
            lines.append(f"### {i}. {rec['title']} ({rec['year']}, {rec['journal']})")
            lines.append("")
            lines.append(f"- Score: {rec['score']}; hits: `{rec['hits']}`")
            if rec["doi"]:
                lines.append(f"- DOI: {rec['doi']}")
            lines.append(f"- Abstract: {rec['abstract']}")
            if rec["keywords"]:
                lines.append(f"- Keywords: {rec['keywords']}")
            lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8-sig")
    print(f"rows={len(rows)}")
    for key, theme in THEMES.items():
        print(f"{key}\t{len(theme_hits[key])}")
    print(f"wrote {OUT_MD}")
    print(f"wrote {OUT_CSV}")


if __name__ == "__main__":
    main()

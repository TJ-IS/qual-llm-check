import pandas as pd
from pathlib import Path

ROOT = Path(r"E:\github\qual-llm-check-IS-utd")
CSV = ROOT / "database" / "ALL_AIS_Basket_11.csv"
OUT = ROOT / "runs" / "coding_agent_ux_misq_isr" / "18_foundational_concept_records.md"

QUERIES = {
    "usability_ease_of_use": [
        "usability",
        "perceived ease of use",
        "ease of use",
        "user satisfaction",
        "web presence",
        "mobile application usability",
        "voice-interaction usability",
    ],
    "delegation_agentic_is": [
        "IS delegation",
        "agentic IS",
        "delegation to and from agentic",
        "human-AI delegation",
        "productive delegation",
        "indirect information system use",
    ],
    "coordination_quality": [
        "coordination",
        "coordination quality",
        "coordination effectiveness",
        "coordination breakdown",
        "coordination affordance",
        "artifact-based coordination",
        "software project coordination",
        "expertise coordination",
    ],
    "visibility_awareness_traceability": [
        "communication visibility",
        "ambient awareness",
        "workspace awareness",
        "visibility",
        "observability",
        "transparency",
        "traceability",
    ],
    "control_recovery_monitoring": [
        "perceived control",
        "user control",
        "recoverability",
        "recovery",
        "monitoring",
        "takeover",
        "supervisory control",
    ],
}


def clean(value: str, limit: int = 520) -> str:
    value = " ".join(str(value or "").split())
    return value if len(value) <= limit else value[: limit - 1] + "..."


def main():
    df = pd.read_csv(CSV, dtype=str, encoding="utf-8-sig", low_memory=False).fillna("")
    text = (
        df["Title"]
        + " "
        + df["Abstract"]
        + " "
        + df["Author Keywords"]
        + " "
        + df["Index Keywords"]
    ).str.lower()

    lines = [
        "# 基础概念候选文献抽取",
        "",
        f"数据源：`{CSV}`",
        f"记录数：{len(df)}",
        "",
    ]

    for group, terms in QUERIES.items():
        mask = pd.Series(False, index=df.index)
        for term in terms:
            mask |= text.str.contains(term.lower(), regex=False, na=False)
        hits = df[mask].copy()
        hits["_year"] = pd.to_numeric(hits["Year"], errors="coerce").fillna(0)

        # Prioritize high-signal journals/titles and recent concept papers, while preserving classics.
        title_lower = hits["Title"].str.lower()
        hits["_priority"] = 0
        for phrase in terms:
            hits.loc[title_lower.str.contains(phrase.lower(), regex=False, na=False), "_priority"] += 5
        hits.loc[hits["Source title"].str.contains("MIS Quarterly|Information Systems Research|Journal of Management Information Systems|Journal of the Association for Information Systems", case=False, regex=True, na=False), "_priority"] += 2
        hits = hits.sort_values(["_priority", "_year", "Cited by"], ascending=[False, False, False])

        lines += [f"## {group}", "", f"命中：{len(hits)}", ""]
        for _, row in hits.head(18).iterrows():
            lines += [
                f"### {clean(row['Title'], 200)} ({row['Year']}, {row['Source title']})",
                "",
                f"- DOI: {row['DOI']}",
                f"- Keywords: {clean(row['Author Keywords'] + ' ' + row['Index Keywords'], 380)}",
                f"- Abstract: {clean(row['Abstract'], 700)}",
                "",
            ]

    OUT.write_text("\ufeff" + "\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()

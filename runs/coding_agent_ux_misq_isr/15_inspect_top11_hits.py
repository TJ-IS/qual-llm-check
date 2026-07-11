import csv
import re
from pathlib import Path

import pandas as pd


ROOT = Path(r"E:\github\qual-llm-check-IS-utd")
CANDIDATES = ROOT / "runs" / "coding_agent_ux_misq_isr" / "13_top11_concept_lineage_candidates.csv"
DB = ROOT / "database" / "ALL_AIS_Basket_11.csv"


def print_theme_tops():
    themes = [
        "is_delegation_agentic_is",
        "control_autonomy",
        "verification_monitoring_oversight",
        "transparency_explainability_visibility",
        "interruption_attention_notification",
        "coordination_collaboration",
        "technostress_overload_fatigue",
        "is_use_post_adoptive",
    ]
    rows = list(csv.DictReader(CANDIDATES.open(encoding="utf-8-sig", newline="")))
    for theme in themes:
        print(f"\n### {theme}")
        n = 0
        for r in rows:
            if r["theme"] == theme:
                n += 1
                if n <= 15:
                    print(
                        f"{n}. {r['title']} ({r['year']}, {r['journal']}) "
                        f"score={r['score']} cited={r['cited_by']} doi={r['doi']}"
                    )


def print_phrase_hits():
    df = pd.read_csv(DB, encoding="utf-8-sig", low_memory=False)
    text = (
        df["Title"].fillna("")
        + " "
        + df["Abstract"].fillna("")
        + " "
        + df["Author Keywords"].fillna("")
        + " "
        + df["Index Keywords"].fillna("")
    ).str.lower()
    phrases = [
        "is delegation",
        "agentic is",
        "agentic artifact",
        "algorithmic control",
        "human-ai collaboration",
        "human-machine collaboration",
        "supervisory control",
        "technostress",
        "interruption overload",
        "perceived control",
        "user control",
        "adaptive use",
        "post-adoptive",
        "verification",
        "transparency",
        "explainability",
        "affordance",
    ]
    for ph in phrases:
        mask = text.str.contains(re.escape(ph), na=False)
        hits = df.loc[mask, ["Title", "Year", "Source title", "DOI"]].head(12)
        print(f"\n### phrase: {ph} ({int(mask.sum())})")
        for _, r in hits.iterrows():
            print(f"- {r['Title']} ({r['Year']}, {r['Source title']}) doi={r['DOI']}")


if __name__ == "__main__":
    print_theme_tops()
    print_phrase_hits()

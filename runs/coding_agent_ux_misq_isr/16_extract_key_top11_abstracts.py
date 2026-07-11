import re
from pathlib import Path

import pandas as pd


ROOT = Path(r"E:\github\qual-llm-check-IS-utd")
DB = ROOT / "database" / "ALL_AIS_Basket_11.csv"

QUERIES = [
    "The next generation of research on is use",
    "FIND THE GOOD. SEEK THE UNITY",
    "Navigating autonomy and control in human-AI delegation",
    "WHEN ALGORITHMS DELEGATE TO HUMANS",
    "Toward Triadic Delegation",
    "Direct and indirect information system use",
    "The consequences of technostress for end users in organizations",
    "Technostress: Technological antecedents and implications",
    "Life interrupted",
    "Worker stress in the age of mobile technology",
    "THE FOG OF WARNINGS",
    "Tuning out security warnings",
    "Understanding user revisions when using information system features",
    "Ambivalence and Coping Responses in Post-Adoptive Information Systems Use",
    "Control configuration and control enactment in information systems projects",
    "Understanding the Role of Technology in Coordination Through Affordance Configurations",
    "How transparency affects algorithmic advice utilization",
    "Complementarity in human-AI collaboration",
    "Examining the Impact of Algorithmic Control on Uber Drivers",
    "Stress from Digital Work: Toward a Unified View of Digital Hindrance Stressors",
]


def clean(value, limit=None):
    text = re.sub(r"\s+", " ", "" if pd.isna(value) else str(value)).strip()
    if limit and len(text) > limit:
        return text[: limit - 1].rstrip() + "…"
    return text


def main():
    df = pd.read_csv(DB, encoding="utf-8-sig", low_memory=False)
    titles = df["Title"].fillna("").str.lower()
    for q in QUERIES:
        mask = titles.str.contains(re.escape(q.lower()), na=False)
        print(f"\n### QUERY: {q} | matches={int(mask.sum())}")
        for _, r in df.loc[mask].head(8).iterrows():
            print(f"TITLE: {clean(r['Title'])}")
            print(f"YEAR/JOURNAL: {clean(r['Year'])} / {clean(r['Source title'])}")
            print(f"DOI: {clean(r['DOI'])}")
            print(f"ABSTRACT: {clean(r['Abstract'], 1500)}")
            print(f"KEYWORDS: {clean(r.get('Author Keywords', ''), 500)} | {clean(r.get('Index Keywords', ''), 500)}")
            print()


if __name__ == "__main__":
    main()

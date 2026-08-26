# -*- coding: utf-8 -*-
"""Check: mismatched 36 files vs M1/F2/F3 retrieval and their decisions."""
import json, re, os

DEC = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_relevance_fulltext_flash_v1\output_v1\decisions.jsonl"
OLD = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_algorithm_development_flash_v2\output_v1"
mism_files = ["19820_2021_time-preference-based-on-spot-bundled-cloud-service-provisioning.md",
"19834_2021_regression-imputation-optimizing-sample-size-and-emulation-demonstrations-and-comparisons-to-pro.md",
"19836_2021_a-mixed-heterogeneous-factorization-model-for-non-overlapping-cross-domain-recommendation.md",
"19838_2021_aligning-the-interests-of-newsvendors-and-forecasters-through-blockchain-based-smart-contracts-a.md",
"19841_2021_promotional-pricing-strategies-for-platform-vendors-competition-between-first-and-third-party-pr.md",
"19842_2021_why-do-organizations-leverage-social-media-to-create-business-value-an-external-factor-centric-e.md",
"19846_2022_measuring-the-sustainability-and-resilience-of-blood-supply-chains.md",
"19848_2021_developing-a-decision-support-system-to-detect-material-weaknesses-in-internal-control.md",
"19853_2021_improving-fake-news-detection-with-domain-adversarial-and-graph-attention-neural-network.md",
"19854_2022_how-guest-host-interactions-affect-consumer-experiences-in-the-sharing-economy-new-evidence-from.md",
"19857_2022_a-holistic-approach-to-interpretability-in-financial-lending-models-visualizations-and-summary-e.md",
"19858_2022_understanding-the-interplay-between-online-reviews-and-growth-of-independent-and-branded-hotels.md",
"19861_2021_bitcoin-price-forecasting-a-perspective-of-underlying-blockchain-transactions.md",
"19862_2022_a-text-mining-based-cyber-risk-assessment-and-mitigation-framework-for-critical-analysis-of-onli.md",
"19864_2022_ai-based-industrial-full-service-offerings-a-model-for-payment-structure-selection-considering-p.md",
"19866_2022_pnrank-unsupervised-ranking-of-person-name-entities-from-noisy-ocr-text.md",
"19868_2022_aggregating-user-preferences-in-group-recommender-systems-a-crowdsourcing-approach.md",
"19870_2022_a-constraint-programming-model-for-making-recommendations-in-personal-process-management-a-desig.md",
"19872_2022_models-to-address-rfid-based-ticket-switching-in-retailing.md",
"19874_2022_the-impact-of-hierarchical-privilege-levels-and-non-hierarchical-incentives-on-continued-contrib.md",
"19876_2022_impact-of-it-governance-process-capability-on-business-performance-theory-and-empirical-evidence.md",
"20401_2021_informational-cues-or-content-examining-project-funding-decisions-by-crowdfunders.md",
"20403_2021_when-does-social-desirability-become-a-problem-detection-and-reduction-of-social-desirability-bi.md",
"20405_2021_impact-of-enjoyment-on-the-usage-continuance-intention-of-video-on-demand-services.md",
"20409_2021_acceptance-of-technological-agency-beyond-the-perception-of-utilitarian-value.md",
"20413_2021_the-paradox-of-word-of-mouth-in-social-commerce-exploring-the-juxtaposed-impacts-of-source-credi.md",
"20419_2022_blockchain-technology-for-bridging-trust-traceability-and-transparency-in-circular-supply-chain.md",
"20425_2021_an-appraisal-mechanism-for-a-social-marketplace.md",
"20431_2021_decisional-guidance-for-detecting-discriminatory-data-analytics-recommendations.md",
"20433_2021_intra-platform-competition-the-role-of-innovative-and-refinement-evolution-in-app-success.md",
"20435_2021_online-channel-expansion-strategy-an-empirical-investigation.md",
"20437_2021_medical-practitioner-s-adoption-of-intelligent-clinical-diagnostic-decision-support-systems-a-mi.md",
"20675_2021_from-sites-to-vibes-technology-and-the-spatial-production-of-coworking-spaces.md",
"20681_2021_overcoming-resource-challenges-in-peer-production-communities-through-bricolage-the-case-of-home.md",
"20683_2021_engaging-with-uncertainty-information-practices-in-the-context-of-disease-surveillance-in-burkin.md",
"20685_2021_who-needs-the-help-desk-tackling-one-s-own-technological-problem-via-self-it-service.md"]

def load_list(path):
    with open(path, encoding="utf-8") as f:
        return {line.strip() for line in f if line.strip()}
f2 = load_list(os.path.join(OLD, "fulltext_candidates_head8000_Q1-Q8_extra.txt"))
f3 = load_list(os.path.join(OLD, "fulltext_candidates_T6_Q1-Q8.txt"))

dec_by_file = {}
with open(DEC, encoding="utf-8") as f:
    for line in f:
        o = json.loads(line); dec_by_file[o["source_file"]] = o

print(f"{'file':<95} {'M1?':<4} {'F2?':<4} {'F3?':<4} status")
for fn in mism_files:
    o = dec_by_file.get(fn)
    sec = (o or {}).get("security_relevance") or {}
    print(f"{fn:<95} {'M1-doi?':<7} {'Y' if fn in f2 else 'N':<4} {'Y' if fn in f3 else 'N':<4} {sec.get('status')}")

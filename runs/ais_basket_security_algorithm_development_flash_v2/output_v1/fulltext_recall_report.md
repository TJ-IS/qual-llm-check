# 全文检索式 Recall 测试报告（以 99 篇为基准）

- 语料：database_fulltext_all，13910 篇
- 词块数：9，术语数：183
- 99 篇映射到语料：99/99

## 各词块召回（99 篇中命中数 / 语料命中总数）

| 词块 | 99命中 | 99召回率 | 语料命中 | 说明 |
|---|---|---|---|---|
| Q1_malware | 39 | 39.4% | 633 |  |
| Q2_intrusion_network | 87 | 87.9% | 6056 |  |
| Q3_adversarial | 35 | 35.4% | 342 |  |
| Q4_phishing_auth | 69 | 69.7% | 2323 |  |
| Q5_attacker_threat | 71 | 71.7% | 1245 |  |
| Q6_content_manipulation | 67 | 67.7% | 4196 |  |
| Q7_privacy_disclosure | 79 | 79.8% | 4129 |  |
| Q8_threat_intel_vuln | 70 | 70.7% | 2263 |  |
| Q9_broad | 98 | 99.0% | 9849 |  |

## Q1-Q8（全部词块）：99 命中 99/99（100.0%），语料命中 12070


## Q1-Q8（不含 Q9 通用词）：99 命中 99/99（100.0%），语料命中 10093

## Q1-Q8 未命中的 99 篇（需补词）


## 术语对 99 篇的覆盖（按命中数降序，前 60）

- [Q9_broad] security: 85/99
- [Q9_broad] detection: 80/99
- [Q9_broad] threat: 74/99
- [Q9_broad] attack: 72/99
- [Q7_privacy_disclosure] privacy: 68/99
- [Q2_intrusion_network] exploit: 59/99
- [Q8_threat_intel_vuln] information security: 54/99
- [Q5_attacker_threat] malicious: 50/99
- [Q2_intrusion_network] vulnerability: 45/99
- [Q6_content_manipulation] fraud: 44/99
- [Q9_broad] defense: 43/99
- [Q9_broad] robustness: 40/99
- [Q6_content_manipulation] spam: 38/99
- [Q5_attacker_threat] attacker: 37/99
- [Q8_threat_intel_vuln] security risk: 34/99
- [Q2_intrusion_network] intrusion: 33/99
- [Q2_intrusion_network] vulnerable: 33/99
- [Q6_content_manipulation] manipulation: 30/99
- [Q8_threat_intel_vuln] countermeasure: 29/99
- [Q1_malware] malware: 28/99
- [Q2_intrusion_network] network security: 28/99
- [Q4_phishing_auth] phishing: 28/99
- [Q6_content_manipulation] fraudulent: 28/99
- [Q2_intrusion_network] intrusion detection: 27/99
- [Q8_threat_intel_vuln] it security: 27/99
- [Q4_phishing_auth] password: 26/99
- [Q5_attacker_threat] hacker: 26/99
- [Q8_threat_intel_vuln] cybersecurity: 26/99
- [Q6_content_manipulation] deception: 24/99
- [Q7_privacy_disclosure] confidentiality: 23/99
- [Q8_threat_intel_vuln] security investment: 23/99
- [Q8_threat_intel_vuln] cyber security: 23/99
- [Q4_phishing_auth] authentication: 22/99
- [Q4_phishing_auth] access control: 22/99
- [Q5_attacker_threat] cybercrime: 22/99
- [Q4_phishing_auth] deceptive: 21/99
- [Q8_threat_intel_vuln] security management: 21/99
- [Q2_intrusion_network] denial of service: 20/99
- [Q7_privacy_disclosure] privacy protection: 19/99
- [Q7_privacy_disclosure] sensitive information: 19/99
- [Q7_privacy_disclosure] identity disclosure: 18/99
- [Q3_adversarial] adversarial: 17/99
- [Q7_privacy_disclosure] privacy-preserving: 17/99
- [Q2_intrusion_network] cyber attack: 16/99
- [Q7_privacy_disclosure] sensitive data: 16/99
- [Q8_threat_intel_vuln] vulnerability assessment: 16/99
- [Q2_intrusion_network] data breach: 15/99
- [Q4_phishing_auth] social engineering: 15/99
- [Q1_malware] botnet: 14/99
- [Q3_adversarial] adversary: 14/99
- [Q4_phishing_auth] spoof: 14/99
- [Q4_phishing_auth] identity theft: 14/99
- [Q4_phishing_auth] credential: 14/99
- [Q5_attacker_threat] insider threat: 14/99
- [Q5_attacker_threat] hacking: 14/99
- [Q5_attacker_threat] cyber threat: 14/99
- [Q7_privacy_disclosure] disclosure risk: 14/99
- [Q8_threat_intel_vuln] security control: 14/99
- [Q2_intrusion_network] cyberattack: 12/99
- [Q5_attacker_threat] cybercriminal: 12/99

## 各词块语料命中的非 99 样本（前 8，检查噪声）

### Q1_malware
- 00066_2006_access-control-and-audit-model-for-the-multidimensional-modeling-of-data-warehouses.md
- 00218_2007_genetic-programming-for-prevention-of-cyberterrorism-through-dynamic-and-evolving-intrusion-dete.md
- 00268_2020_corporate-strategy-changes-and-information-technology-control-effectiveness-in-multibusiness-fir.md
- 00270_2019_decision-making-and-biases-in-cybersecurity-capability-development-evidence-from-a-simulation-ga.md
- 00290_2000_organizational-experiences-and-career-success-of-mis-professionals-and-managers-an-examination-o.md
- 00348_2015_exploring-information-privacy-regulation-risks-trust-and-behavior.md
- 00350_2019_explaining-digital-piracy-a-meta-analysis.md
- 00358_2020_why-individual-employees-commit-malicious-computer-abuse-a-routine-activity-theory-perspective.md
### Q2_intrusion_network
- 00020_2017_interorganizational-dependence-information-transparency-in-interorganizational-information-syste.md
- 00024_2012_shall-we-dance-the-effect-of-information-presentations-on-negotiation-processes-and-outcomes.md
- 00026_2017_increasing-firm-agility-through-the-use-of-data-analytics-the-role-of-fit.md
- 00028_2008_oddm-a-framework-for-modelbases.md
- 00030_2010_classification-by-vertical-and-cutting-multi-hyperplane-decision-tree-induction.md
- 00034_2020_learning-from-workaround-practices-the-challenge-of-enterprise-system-implementations-in-multina.md
- 00038_2014_developing-information-processing-capability-for-operational-agility-implications-from-a-chinese.md
- 00056_2020_electronic-health-records-and-the-logics-of-care-complementarity-and-conflict-in-the-u-s-healthc.md
### Q3_adversarial
- 00514_2006_data-model-development-for-fire-related-extreme-events-an-activity-theory-approach.md
- 00534_2009_machine-learning-and-genetic-algorithms-in-pharmaceutical-development-and-manufacturing-processe.md
- 00820_2017_taking-stock-of-organisations-protection-of-privacy-categorising-and-assessing-threats-to-person.md
- 00908_1989_a-social-process-model-of-user-analyst-relationships.md
- 00934_2014_the-continuity-of-underperforming-ict-projects-in-the-public-sector.md
- 00942_2006_automotive-e-hubs-exploring-motivations-and-barriers-to-collaboration-and-interaction.md
- 01054_2018_exploring-the-dialectics-underlying-institutionalization-of-it-artifacts.md
- 01080_2025_do-crowds-validate-false-data-systematic-distortion-and-affective-polarization.md
### Q4_phishing_auth
- 00056_2020_electronic-health-records-and-the-logics-of-care-complementarity-and-conflict-in-the-u-s-healthc.md
- 00066_2006_access-control-and-audit-model-for-the-multidimensional-modeling-of-data-warehouses.md
- 00110_2019_from-free-to-paid-customer-expertise-and-customer-satisfaction-on-knowledge-payment-platforms.md
- 00134_2012_negotiating-language-barriers-a-methodology-for-cross-organisational-conceptual-modelling.md
- 00148_2018_using-perspective-taking-to-de-escalate-launch-date-commitment-for-products-with-known-software.md
- 00174_2019_beautiful-is-good-and-good-is-reputable-multiple-attribute-charity-website-evaluation-andinitial.md
- 00186_2021_will-humans-in-the-loop-become-borgs-merits-and-pitfalls-of-working-with-ai.md
- 00204_2024_creation-or-destruction-stem-opt-extension-and-employment-of-information-technology-professional.md
### Q5_attacker_threat
- 00076_2014_launching-successful-e-markets-a-broker-level-order-routing-analysis-of-two-options-exchanges.md
- 00118_2018_toward-a-real-time-and-budget-aware-task-package-allocation-in-spatial-crowdsourcing.md
- 00182_2021_the-impact-of-helping-others-in-coopetitive-crowdsourcing-communities.md
- 00202_2011_an-incident-information-management-framework-based-on-data-integration-data-mining-and-multi-cri.md
- 00218_2007_genetic-programming-for-prevention-of-cyberterrorism-through-dynamic-and-evolving-intrusion-dete.md
- 00254_2005_choice-of-transaction-channels-the-effects-of-product-characteristics-on-market-evolution.md
- 00268_2020_corporate-strategy-changes-and-information-technology-control-effectiveness-in-multibusiness-fir.md
- 00270_2019_decision-making-and-biases-in-cybersecurity-capability-development-evidence-from-a-simulation-ga.md
### Q6_content_manipulation
- 00028_2008_oddm-a-framework-for-modelbases.md
- 00056_2020_electronic-health-records-and-the-logics-of-care-complementarity-and-conflict-in-the-u-s-healthc.md
- 00076_2014_launching-successful-e-markets-a-broker-level-order-routing-analysis-of-two-options-exchanges.md
- 00086_2011_a-finite-mixture-logit-model-to-segment-and-predict-electronic-payments-system-adoption.md
- 00090_2007_altar-in-action-knowledge-management.md
- 00106_2021_thinking-technology-as-human-affordances-technology-features-and-egocentric-biases-in-technology.md
- 00114_2003_rigor-in-information-systems-positivist-case-research-current-practices-trends-and-recommendatio.md
- 00144_2024_commercializing-social-media-how-showrooms-on-social-media-fan-pages-influence-customer-behavior.md
### Q7_privacy_disclosure
- 00034_2020_learning-from-workaround-practices-the-challenge-of-enterprise-system-implementations-in-multina.md
- 00038_2014_developing-information-processing-capability-for-operational-agility-implications-from-a-chinese.md
- 00056_2020_electronic-health-records-and-the-logics-of-care-complementarity-and-conflict-in-the-u-s-healthc.md
- 00066_2006_access-control-and-audit-model-for-the-multidimensional-modeling-of-data-warehouses.md
- 00090_2007_altar-in-action-knowledge-management.md
- 00104_2016_would-you-like-to-know-who-knows-connecting-employees-based-on-process-oriented-knowledge-mappin.md
- 00106_2021_thinking-technology-as-human-affordances-technology-features-and-egocentric-biases-in-technology.md
- 00116_2013_bridging-the-qualitativequantitative-divide-guidelines-for-conducting-mixed-methods-research-in.md
### Q8_threat_intel_vuln
- 00056_2020_electronic-health-records-and-the-logics-of-care-complementarity-and-conflict-in-the-u-s-healthc.md
- 00066_2006_access-control-and-audit-model-for-the-multidimensional-modeling-of-data-warehouses.md
- 00092_2014_recommender-systems-based-on-quantitative-implicit-customer-feedback.md
- 00134_2012_negotiating-language-barriers-a-methodology-for-cross-organisational-conceptual-modelling.md
- 00140_2011_a-multi-objective-optimization-for-green-supply-chain-network-design.md
- 00160_2013_software-project-risk-analysis-using-bayesian-networks-with-causality-constraints.md
- 00172_2012_people-practice-and-technology-restoring-giddens-broader-philosophy-to-the-study-of-information.md
- 00174_2019_beautiful-is-good-and-good-is-reputable-multiple-attribute-charity-website-evaluation-andinitial.md
### Q9_broad
- 00020_2017_interorganizational-dependence-information-transparency-in-interorganizational-information-syste.md
- 00024_2012_shall-we-dance-the-effect-of-information-presentations-on-negotiation-processes-and-outcomes.md
- 00026_2017_increasing-firm-agility-through-the-use-of-data-analytics-the-role-of-fit.md
- 00030_2010_classification-by-vertical-and-cutting-multi-hyperplane-decision-tree-induction.md
- 00056_2020_electronic-health-records-and-the-logics-of-care-complementarity-and-conflict-in-the-u-s-healthc.md
- 00066_2006_access-control-and-audit-model-for-the-multidimensional-modeling-of-data-warehouses.md
- 00076_2014_launching-successful-e-markets-a-broker-level-order-routing-analysis-of-two-options-exchanges.md
- 00080_2009_relation-of-cio-background-it-infrastructure-and-economic-performance.md
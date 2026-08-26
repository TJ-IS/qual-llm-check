# SLR 元数据检索（Title+Abstract+Keywords）测试报告

- 元数据源：ALL_AIS_Basket_11.csv，17745 条（空摘要 0 条）
- 检索字段：Title + Abstract + Author Keywords + Index Keywords（Scopus 标准 SLR 字段）
- 词表：Q1–Q8（183 词）+ 补充 5 词，共 188 词
- 元数据命中：2499 条
- 99 篇 DOI 映射：99/99；元数据检索召回：98/99（含未映射则 98/99）

## 各词块在元数据层的命中

| 词块 | 元数据命中 |
|---|---|
| Q1_malware | 58 |
| Q2_intrusion_network | 672 |
| Q3_adversarial | 61 |
| Q4_phishing_auth | 177 |
| Q5_attacker_threat | 155 |
| Q6_content_manipulation | 403 |
| Q7_privacy_disclosure | 474 |
| Q8_threat_intel_vuln | 431 |

候选清单：E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_algorithm_development_flash_v2\output_v1\slr_metadata_candidates.txt
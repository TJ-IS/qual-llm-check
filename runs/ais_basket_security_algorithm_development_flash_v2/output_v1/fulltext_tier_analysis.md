# 分层检索组合（tier）分析

| 组合 | 99命中 | 召回率 | 语料命中 | 需筛数量级 |
|---|---|---|---|---|
| T1 恶意代码+对抗鲁棒 | 61/99 | 61.6% | 906 | ~906 |
| T2 攻击对抗核心(T1+入侵+攻击者) | 92/99 | 92.9% | 6566 | ~6566 |
| T3 内容操纵+钓鱼 | 84/99 | 84.8% | 5359 | ~5359 |
| T4 隐私披露 | 79/99 | 79.8% | 4129 | ~4129 |
| T5 威胁情报/漏洞 | 70/99 | 70.7% | 2263 | ~2263 |
| T6 安全全量(Q1-Q8) | 99/99 | 100.0% | 10093 | ~10093 |
| T7 非隐私安全(T6-T4) | 98/99 | 99.0% | 9390 | ~9390 |
| T8 高信号精简(仅特定术语块) | 89/99 | 89.9% | 6306 | ~6306 |

## 99 篇的词块覆盖（每篇命中哪些块）

仅命中 1-2 个词块的 99 篇（8 篇）：

- 21403 | 21403_1997_distributed-decision-support-systems-under-limited-degrees-of-competence-a-simulation-study.md | Q6_content_manipulation
- 5320 | 05320_2012_b-research-note-b-generating-shareable-statistical-databases-for-business-value-multiple-imputat.md | Q2_intrusion_network,Q7_privacy_disclosure
- 19712 | 19712_2021_from-conflicts-and-confusion-to-doubts-examining-review-inconsistency-for-fake-review-detection.md | Q4_phishing_auth,Q6_content_manipulation
- 10412 | 10412_2007_spamhunting-an-instance-based-reasoning-system-for-spam-labelling-and-filtering.md | Q6_content_manipulation
- 4262 | 04262_2007_dare-to-share-protecting-sensitive-knowledge-with-data-sanitization.md | Q6_content_manipulation,Q7_privacy_disclosure
- 27953 | 27953_2024_explainable-deep-learning-for-false-information-identification-an-argumentation-theory-approach.md | Q4_phishing_auth,Q6_content_manipulation
- 12794 | 12794_2020_hiding-sensitive-information-when-sharing-distributed-transactional-data.md | Q2_intrusion_network,Q7_privacy_disclosure
- 14422 | 14422_2011_protecting-privacy-against-record-linkage-disclosure-a-bounded-swapping-approach-for-numeric-dat.md | Q7_privacy_disclosure

## 单块依赖（仅被某一块覆盖）

### 仅 Q6_content_manipulation：2 篇
- 21403 | 21403_1997_distributed-decision-support-systems-under-limited-degrees-of-competence-a-simulation-study.md
- 10412 | 10412_2007_spamhunting-an-instance-based-reasoning-system-for-spam-labelling-and-filtering.md
### 仅 Q7_privacy_disclosure：1 篇
- 14422 | 14422_2011_protecting-privacy-against-record-linkage-disclosure-a-bounded-swapping-approach-for-numeric-dat.md
---
otero_id: "2-s2.0-85133531314"
title: "DEAR: A Novel Deep Learning-based Approach for Automated Program Repair"
authors: "Li Y.; Wang S.; Nguyen T.N."
year: "2022"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3510003.3510177"
---
# Scopus title-abstract-keyword metadata
Title: DEAR: A Novel Deep Learning-based Approach for Automated Program Repair
Abstract: The existing deep learning (DL)-based automated program repair (APR) models are limited in fixing general software defects. We present DEAR, a DL-based approach that supports fixing for the general bugs that require dependent changes at once to one or mul-tiple consecutive statements in one or multiple hunks of code. We first design a novel fault localization (FL) technique for multi-hunk, multi-statement fixes that combines traditional spectrum-based (SB) FL with deep learning and data-flow analysis. It takes the buggy statements returned by the SBFL model, detects the buggy hunks to be fixed at once, and expands a buggy statement s in a hunk to include other suspicious statements around s. We design a two-tier, tree-based LSTM model that incorporates cycle training and uses a divide-and-conquer strategy to learn proper code transformations for fixing multiple statements in the suitable fixing context consisting of surrounding subtrees. We conducted several experiments to evaluate DEAR on three datasets: Defects4J (395 bugs), BigFix (+26k bugs), and CPatMiner (+44k bugs). On Defects4J dataset, DEAR outperforms the baselines from 42%-683% in terms of the number of auto-fixed bugs with only the top-1 patches. On BigFix dataset, it fixes 31-145 more bugs than existing DL-based APR models with the top-1 patches. On CPatMiner dataset, among 667 fixed bugs, there are 169 (25.3%) multi-hunk/multi-statement bugs. DEAR fixes 71 and 164 more bugs, including 52 and 61 more multi-hunk/multi-statement bugs, than the state-of-the-art, DL-based APR models. © 2022 ACM.
Author keywords: Automated Program Repair; Deep Learning; Fault Localization
Index keywords: Automation; Cosine transforms; Defects; Long short-term memory; Program debugging; Repair; Automated program repair; Deep learning; Fault localization; First designs; Learning flows; Learning-based approach; Localization technique; Repair models; Software defects; Spectra's; Data flow analysis
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2022
EID: 2-s2.0-85133531314
DOI: 10.1145/3510003.3510177
Retrieval channels: authoritative_outlet_search
Local full-text files: 

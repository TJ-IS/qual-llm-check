---
otero_id: "2-s2.0-105018304895"
title: "Towards Reliable Evaluation of Neural Program Repair with Natural Robustness Testing"
authors: "Le-Cong T.; Nguyen D.; Le B.; Murray T."
year: "2025"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3716167"
---
# Scopus title-abstract-keyword metadata
Title: Towards Reliable Evaluation of Neural Program Repair with Natural Robustness Testing
Abstract: Automated program repair (APR) has recently gained ground, with numerous research efforts being conducted in the area that have been adopted in the industry. One notable class of APR is neural program repair (NPR), which typically employs deep learning techniques that are trained on vast amounts of historical data to fix bugs that have not been seen in the past. To study the true effectiveness of NPR on existing limited datasets, recent work augments the evaluation data by employing semantics-preserving transformations to convert original buggy programs to semantically equivalent ones. Experiments show that NPR techniques are not robust; e.g., NPR cannot repair semantically equivalent counterparts of 20%–35% of bugs that they can repair in the original dataset. However, we found that many of these transformations are unnatural, that are unlikely to occur in real-world scenarios, leading to misleading conclusions about NPR effectiveness and misguide the improvement on unrobust behaviors, which have minimal real-world impact. In this article, we propose shifting the focus of robustness evaluation for NPR techniques towards naturally occurring data transformations. To accomplish this, we first examine the naturalness of semantic-preserving transformations through a two-stage human study. This study includes: (i) interviews with senior software developers to establish concrete criteria for evaluating the naturalness of these transformations and (ii) a survey involving 10 developers to assess the naturalness of 1,178 transformations, i.e., pairs of original and transformed programs, applied to 225 real-world bugs. Our findings show that only 60% of these transformations are considered natural, while 20% are considered unnatural, with strong agreement among the annotators. Moreover, the unnaturalness of these transformations significantly impacts both their applicability to benchmarks and the conclusions drawn from robustness testing. Next, we conduct natural robustness tests on NPR techniques to assess their true effectiveness against real-world data variations. Our experimental results reveal a substantial number of prediction changes in NPR techniques, leading to significant reductions in both plausible and correct patch rates when comparing performance on the original and transformed datasets. Furthermore, we observe notable differences in performance improvements between NPR techniques, suggesting potential biases in the evaluation of NPR introduced by limited datasets. Finally, we explore automating the assessment of transformation naturalness by developing a new naturalness metric, namely RNC, using large language models. This metric effectively evaluates naturalness with an AUC of 0.7, offering a promising direction for automating the naturalness assessment of code transformations. © 2025 Copyright held by the owner/author(s)
Author keywords: Automated Program Repair; Code Naturalness; Code Transformations; Natural Robustness
Index keywords: Automation; Benchmarking; Deep learning; Human computer interaction; Learning systems; Repair; Semantics; Software testing; Automated program repair; Code naturalness; Code transformation; Learning techniques; Natural robustness; Performance; Real-world; Repair techniques; Research efforts; Robustness testing; Cosine transforms
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2025
EID: 2-s2.0-105018304895
DOI: 10.1145/3716167
Retrieval channels: authoritative_outlet_search
Local full-text files: 

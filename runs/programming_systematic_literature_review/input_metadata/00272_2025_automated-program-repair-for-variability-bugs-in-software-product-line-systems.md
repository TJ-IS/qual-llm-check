---
otero_id: "2-s2.0-85203812565"
title: "Automated program repair for variability bugs in software product line systems"
authors: "Nguyen T.-T.; Zhang X.-Y.; Arcaini P.; Ishikawa F.; Vo H.D."
year: "2025"
journal: "Journal of Systems and Software"
doi: "10.1016/j.jss.2024.112152"
---
# Scopus title-abstract-keyword metadata
Title: Automated program repair for variability bugs in software product line systems
Abstract: Software product line (SPL) systems are widely employed to develop industrial projects. For an SPL system, different products/variants are created by combining different subsets of the system features. Because of the interaction of the different features, a bug in the system could cause failures for some products (failing products), but not for others (passing products); such types of bugs are called variability bugs. Due to their variability characteristics, detecting and fixing bugs in SPL systems is challenging. There are several solutions for localizing buggy statements in these systems. However, there is still a lack of research on automatically fixing these bugs. In this work, we aim to make the first attempt at automatically fixing buggy statements in the source code of SPL systems. This paper proposes two approaches, single-product-based and multi-product-based, to repair the variability bugs in an SPL system to fix the failures of the failing products and not to break the correct behaviors of the passing products. For the single-product-based approach, each failing product is fixed individually, and the obtained patches are then propagated and validated on the other products of the system. For the multi-product-based approach, all the products are repaired simultaneously. The patches are generated and validated by all the sampled products of the system in each repair iteration. Moreover, to improve the repair performance of both approaches, we also introduce several heuristic rules for effectively and efficiently deciding where to fix (navigating modification points) and how to fix (selecting suitable modifications). These heuristic rules use intermediate validation results of the repaired programs as feedback to refine the fault localization results and evaluate the suitability of the modifications before actually applying and validating them by test execution. Our experimental results on a dataset of 318 variability bugs of five popular SPL systems show that the single-product-based approach is around 20 times better than the multi-product-based approach in the number of correct fixes. Notably, the heuristic rules could improve the performance of both approaches by increasing of 30%–150% the number of correct fixes, and decreasing of 30%–50% the number of attempted modification operations. © 2024 Elsevier Inc.
Author keywords: Automated program repair; Software product line; Variability bugs
Index keywords: Heuristic methods; Automated program repair; Heuristic rules; Industrial programs; Multi-products; Performance; Product variants; Single product; Software Product Line; System features; Variability bug; Computer software maintenance
Document type: Article
Conference: 
Source title: Journal of Systems and Software
Year: 2025
EID: 2-s2.0-85203812565
DOI: 10.1016/j.jss.2024.112152
Retrieval channels: authoritative_outlet_search
Local full-text files: 

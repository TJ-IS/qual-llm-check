---
otero_id: "2-s2.0-105033765455"
title: "Just-in-time bug classifier: A step towards integrating Automated Program Repair in CI/CD pipelines"
authors: "Kabadi V.; Le X.-B.D.; Thongtanunam P.; Treude C."
year: "2026"
journal: "Information and Software Technology"
doi: "10.1016/j.infsof.2026.108076"
---
# Scopus title-abstract-keyword metadata
Title: Just-in-time bug classifier: A step towards integrating Automated Program Repair in CI/CD pipelines
Abstract: Context: Automated Program Repair (APR) tools have advanced in recent years, yet their effectiveness can improve when integrated into Continuous Integration/Continuous Deployment (CI/CD) pipelines. Motivated by this, we designed the Continuous Automatic Repair Framework (CARF), which detects build failures, routes each bug to the most suitable repair tool, and automatically commits the generated fix. During development, we identified a critical bottleneck: the need for instant bug classification within CI/CD. Accurate classification is essential to determine whether a fault lies in program code or the test suite, ensuring the defect is routed to the appropriate repair tool. Objective: Objectives: This study aims to design and evaluate a just-in-time bug classifier capable of distinguishing between program and test bugs during CI/CD execution, thereby enabling CARF to maintain workflow efficiency by directing defects to appropriate repair tools. Methods: We implemented a heuristic analysis tool that extracts discriminative structural features by comparing Abstract Syntax Trees (ASTs) between buggy and pre-buggy commits. These features are input to machine learning models for bug classification. Empirical validation demonstrated the accuracy and operational feasibility of the approach within CI/CD environments. Results: Our approach achieved up to 73% accuracy in identifying regression bugs across 67 real-world projects, effectively distinguishing between program bugs and test bugs while requiring only 10% of the dataset for training. In contrast, prior studies reported an accuracy of 69% on artificially injected bugs derived from successive versions of only two projects, with 90% of the data used for training. Conclusion: CARF facilitates the integration of automated program repair into CI/CD pipelines, enabling faster, more accurate, and more flexible software maintenance. The just-in-time bug classifier demonstrates that defect classification can scale efficiently without symbolic execution or manual bug reports, providing a practical foundation for continuous automated repair. © 2026 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license. http://creativecommons.org/licenses/by/4.0/
Author keywords: Automatic Program Repair; Bug classifier
Index keywords: Abstracting; Automatic programming; Automatic test pattern generation; Computer software maintenance; Defects; Heuristic methods; Learning systems; Program debugging; Repair; Software testing; Automatic program repair; Automatic programs; Bug classifier; Continuous integrations; Failure routes; Heuristic analysis; Just-in-time; Program code; Repair tools; Work-flows; Automation
Document type: Article
Conference: 
Source title: Information and Software Technology
Year: 2026
EID: 2-s2.0-105033765455
DOI: 10.1016/j.infsof.2026.108076
Retrieval channels: authoritative_outlet_search
Local full-text files: 

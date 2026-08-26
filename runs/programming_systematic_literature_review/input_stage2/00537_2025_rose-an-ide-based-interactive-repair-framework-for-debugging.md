---
otero_id: "2-s2.0-105005206904"
title: "ROSE: An IDE-Based Interactive Repair Framework for Debugging"
authors: "Reiss S.P.; Wei X.; Yuan J.; Xin Q."
year: "2025"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3705306"
---
# Scopus title-abstract-keyword metadata
Title: ROSE: An IDE-Based Interactive Repair Framework for Debugging
Abstract: Debugging is costly. Automated program repair (APR) holds the promise of reducing its cost by automatically fixing errors. However, current techniques are not easily applicable in a realistic debugging scenario because they assume a high-quality test suite and frequent program re-execution, have low repair efficiency, and only handle a limited set of errors. To improve the practicality of APR for debugging, we propose ROSE, an interactive repair framework that is able to suggest quick and effective repairs of semantic errors while debugging in an Integrated Development Environment (IDE). ROSE allows an easy integration of existing APR patch generators and can do program repair without assuming the existence of a test suite and without requiring program re-execution. It works in conjunction with an IDE debugger and assumes a debugger stopping point where a problem symptom is observed. ROSE asks the developer to quickly describe the symptom. Then it uses the stopping point, the identified symptom, and the current environment to identify potentially faulty lines, uses a variety of APR techniques to suggest repairs at those lines, and validates those repairs without re-executing the program. Finally, it presents the results so the developer can examine, select, and make the appropriate repair. ROSE uses novel approaches to achieve effective fault localization and patch validation without a test suite or program re-execution. For fault localization, ROSE builds on a fast abstract interpretation-based flow analysis to compute a static backward slice approximating the real dynamic slice while taking into account the symptom and the current execution. For patch validation without re-running the program, ROSE generates simulated traces based on a live-programming system for both the original and repaired executions and compares the traces with respect to the problem symptoms to infer patch correctness. We implemented a prototype of ROSE that works in an Eclipse-based IDE and evaluated its potency and utility with an effectiveness study and a user study. We found that ROSE's fault localization and validation are highly effective and a ROSE-based tool using existing APR patch generators generated correct repair suggestions for many errors in only seconds. Moreover, the user study demonstrated that ROSE was helpful for debugging and developers liked to use it.  © 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: Automated Program Repair; Debugging; Integrated Development Environment; Interactive Repair Framework
Index keywords: Data flow analysis; Integration testing; 'current; Automated program repair; Debuggers; Debugging; Fault localization; High Quality Test; Integrated development environment; Interactive repair framework; Re-execution; User study; Program debugging
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2025
EID: 2-s2.0-105005206904
DOI: 10.1145/3705306
Retrieval channels: authoritative_outlet_search
Local full-text files: 

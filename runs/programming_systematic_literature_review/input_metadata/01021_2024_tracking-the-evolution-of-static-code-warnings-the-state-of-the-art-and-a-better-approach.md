---
otero_id: "2-s2.0-85184013565"
title: "Tracking the Evolution of Static Code Warnings: The State-of-the-Art and a Better Approach"
authors: "Li J.; Yang J."
year: "2024"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2024.3358283"
---
# Scopus title-abstract-keyword metadata
Title: Tracking the Evolution of Static Code Warnings: The State-of-the-Art and a Better Approach
Abstract: Static bug detection tools help developers detect problems in the code, including bad programming practices and potential defects. Recent efforts to integrate static bug detectors in modern software development workflows, such as in code review and continuous integration, are shown to better motivate developers to fix the reported warnings on the fly. A proper mechanism to track the evolution of the reported warnings can better support such integration. Moreover, tracking the static code warnings will benefit many downstream software engineering tasks, such as learning the fix patterns for automated program repair, and learning which warnings are of more interest, so they can be prioritized automatically. In addition, the utilization of tracking tools enables developers to concentrate on the most recent and actionable static warnings rather than being overwhelmed by the thousands of warnings from the entire project. This, in turn, enhances the utilization of static analysis tools. Hence, precisely tracking the warnings by static bug detectors is critical to improving the utilization of static bug detectors further. In this paper, we study the effectiveness of the state-of-the-art (SOTA) solution in tracking static code warnings and propose a better solution based on our analysis of the insufficiency of the SOTA solution. In particular, we examined over 2,000 commits in four large-scale open-source systems (i.e., JClouds, Kafka, Spring-boot, and Guava) and crafted a dataset of 3,451 static code warnings by two static bug detectors (i.e., Spotbugs and PMD). We manually uncovered the ground-truth evolution status of the static warnings: persistent, removedfix, removednon-fix and newly-introduced. Upon manual analysis, we identified the main reasons behind the insufficiency of the SOTA solution. Furthermore, we propose StaticTracker to track static warnings over software development history. Our evaluation shows that StaticTracker significantly improves the tracking precision, i.e., from 64.4% to 90.3% for the evolution statuses combined (removedfix, removednon-fix and newly-introduced). © 1976-2012 IEEE.
Author keywords: code refactoring; empirical study; software evolution; Static analysis
Index keywords: Job analysis; Open source software; Open systems; Program debugging; Software design; Static analysis; Bug detector; Code; Code re-factoring; Computer bugs; Empirical studies; Software; Software Evolution; State of the art; Static codes; Task analysis; Codes (symbols)
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2024
EID: 2-s2.0-85184013565
DOI: 10.1109/tse.2024.3358283
Retrieval channels: authoritative_outlet_search
Local full-text files: 

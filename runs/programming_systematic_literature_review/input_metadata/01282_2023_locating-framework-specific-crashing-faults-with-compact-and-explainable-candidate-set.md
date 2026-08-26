---
otero_id: "2-s2.0-85171730583"
title: "Locating Framework-specific Crashing Faults with Compact and Explainable Candidate Set"
authors: "Yan J.; Wang M.; Liu Y.; Yan J.; Zhang L."
year: "2023"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse48619.2023.00026"
---
# Scopus title-abstract-keyword metadata
Title: Locating Framework-specific Crashing Faults with Compact and Explainable Candidate Set
Abstract: Nowadays, many applications do not exist independently but rely on various frameworks or libraries. The frequent evolution and the complex implementation of framework APIs induce lots of unexpected post-release crashes. Starting from the crash stack traces, existing approaches either perform application-level call graph (CG) tracing or construct datasets with similar crash-fixing records to locate buggy methods. However, these approaches are limited by the completeness of CG or dependent on historical fixing records, and some of them only focus on specific manually modeled exception types. To achieve effective debugging on complex framework-specific crashes, we propose a code-separation-based locating approach that weakly relies on CG tracing and does not require any prior knowledge. Our key insight is that one crash trace with the description message can be mapped to a definite exception-thrown point in the framework, the semantics analysis of which can help to figure out the root causes of the crash-triggering procedure. Thus, we can pre-construct reusable summaries for all the framework-specific exceptions to support fault localization in application code. Based on that idea, we design the exception-thrown summary (ETS) that describes both the key variables and key APIs related to the exception triggering. Then, we perform static analysis to automatically compute such summaries and make a data-tracking of key variables and APIs in the application code to get the ranked buggy candidates. In the scenario of locating Android framework-specific crashing faults, our tool CrashTracker exhibited an overall MRR value of 0.91 and outperforms the state-of-the-art tool Anchor with higher precision. It only provides a compact candidate set and gives user-friendly reports with explainable reasons for each candidate. © 2023 IEEE.
Author keywords: Android Application; Crash Stack Trace; Fault Localization; Framework-specific Exception
Index keywords: Android (operating system); Application programming interfaces (API); Codes (symbols); Computer software reusability; Location; Program debugging; Semantics; Android applications; Application codes; Application level; Call graphs; Candidate sets; Crash stack trace; Fault localization; Framework-specific exception; Key variables; Prior-knowledge; Static analysis
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2023
EID: 2-s2.0-85171730583
DOI: 10.1109/icse48619.2023.00026
Retrieval channels: authoritative_outlet_search
Local full-text files: 

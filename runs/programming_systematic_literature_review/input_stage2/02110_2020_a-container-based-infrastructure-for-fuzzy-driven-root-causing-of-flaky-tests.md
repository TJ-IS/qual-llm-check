---
otero_id: "2-s2.0-85097351948"
title: "A Container-Based Infrastructure for Fuzzy-Driven Root Causing of Flaky Tests"
authors: "Terragni V.; Salza P.; Ferrucci F."
year: "2020"
journal: "Proceedings - 2020 ACM/IEEE 42nd International Conference on Software Engineering: New Ideas and Emerging Results, ICSE-NIER 2020"
doi: "10.1145/3377816.3381742"
---
# Scopus title-abstract-keyword metadata
Title: A Container-Based Infrastructure for Fuzzy-Driven Root Causing of Flaky Tests
Abstract: Intermittent test failures (test flakiness) is common during continuous integration as modern software systems have become inherently non-deterministic. Understanding the root cause of test flakiness is crucial as intermittent test failures might be the result of real non-deterministic defects in the production code, rather than mere errors in the test code. Given a flaky test, existing techniques for root causing test flakiness compare the runtime behavior of its passing and failing executions. They achieve this by repetitively executing the flaky test on an instrumented version of the system under test. This approach has two fundamental limitations: (i) code instrumentation might prevent the manifestation of test flakiness; (ii) when test flakiness is rare passively re-executing a test many times might be inadequate to trigger intermittent test outcomes. To address these limitations, we propose a new idea for root causing test flakiness that actively explores the non-deterministic space without instrumenting code. Our novel idea is to repetitively execute a flaky test, under different execution clusters. Each cluster explores a certain non-deterministic dimension (e.g., concurrency, I/O, and networking) with dedicated software containers and fuzzy-driven resource load generators. The execution cluster that manifests the most balanced (or unbalanced) sets of passing and failing executions is likely to explain the broad type of test flakiness.CCS CONCEPTS• Software and its engineering ? Software testing and debugging; • Computer systems organization ? Cloud computing; • Hardware ? Testing with distributed and parallel systems.  © 2020 ACM.
Author keywords: Cloud; Concurrency; Fuzzy Analysis; Non-Determinism; Root-Causing Analysis; Software Containers; Test Flakiness
Index keywords: Computer debugging; Containers; Program debugging; Code instrumentation; Computer systems organization; Continuous integrations; Fundamental limitations; Runtime behaviors; Software systems; Software Testing and Debugging; System under test; Software testing
Document type: Conference paper
Conference: 
Source title: Proceedings - 2020 ACM/IEEE 42nd International Conference on Software Engineering: New Ideas and Emerging Results, ICSE-NIER 2020
Year: 2020
EID: 2-s2.0-85097351948
DOI: 10.1145/3377816.3381742
Retrieval channels: authoritative_outlet_search
Local full-text files: 

---
otero_id: "2-s2.0-86000362714"
title: "Novelty Not Found: Exploring Input Shadowing in Fuzzing through Adaptive Fuzzer Restarts"
authors: "Schiller N.; Xu X.; Bernhard L.; Bars N.; Schloegel M.; Holz T."
year: "2025"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3712186"
---
# Scopus title-abstract-keyword metadata
Title: Novelty Not Found: Exploring Input Shadowing in Fuzzing through Adaptive Fuzzer Restarts
Abstract: Greybox fuzzing enhances software security through unprecedented effectiveness in automated fault detection. Its success lies in the coverage feedback extracted from the system under test, guiding the fuzzer to explore different program parts. The most prominent way to use this feedback is novelty search, where the fuzzer keeps only new inputs exercising a new program edge. However, this approach - by design - ignores input shadowing, in which interesting inputs are discarded if they do not contribute to new coverage. This limits the accepted input space and may overlook bugs that shadowed inputs could trigger with mutations. In this work, we present a comprehensive analysis of input shadowing and demonstrate that multiple fuzzing runs of the same target exhibit a different basic block hit frequency distribution despite overlapping code coverage. We propose fuzzer restarts to effectively redistribute basic block hit frequencies and show that this increases the overall achieved coverage on 15 evaluated targets on average by and up to . Furthermore, restarts help to find more bugs and trigger them more reliably. Overall, our results highlight the importance of considering input shadowing in the fuzzers' design and the potential benefits of a restart-based strategy to enhance the performance of complex fuzzing methods.  © 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: fuzz testing; Fuzzing
Index keywords: Program debugging; Automated fault detection; Basic blocks; Comprehensive analysis; Fuzz Testing; Fuzzing; Grey-box; Input space; New projects; Software security; Systems under tests; Software testing
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2025
EID: 2-s2.0-86000362714
DOI: 10.1145/3712186
Retrieval channels: authoritative_outlet_search
Local full-text files: 

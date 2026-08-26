---
otero_id: "2-s2.0-105030728126"
title: "Boosting Compiler Fault Localization: Getting the Best of Both Worlds by Fusing Dynamic and Historical Data"
authors: "Li Q.; Yang Y.; Sun M.; Wu J.; Shi Q.; Zhou Y.; Xu B."
year: "2026"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2026.3666208"
---
# Scopus title-abstract-keyword metadata
Title: Boosting Compiler Fault Localization: Getting the Best of Both Worlds by Fusing Dynamic and Historical Data
Abstract: Compilers are prone to bugs that can have severe consequences for downstream applications. Accurately identifying and localizing compiler faults poses unique challenges due to the inherent complexity and large scale of modern compiler infrastructures. Existing studies have proposed various techniques to construct passing and failing executions by generating witness test programs from bug-inducing test cases or by producing adversarial compilation configurations for the same test program. These executions are then leveraged to apply spectrum-based fault localization (SBFL) techniques for isolating compiler faults, yielding promising results. Recently, Yang et al. revisited SBFL-based techniques and showed that a simple yet widely adopted debugging practice - treating files modified in bug-inducing commits (BICs) as potential fault candidates - can surprisingly outperform SBFL-based techniques on the most critical localization metrics. Moreover, they further demonstrated that BIC-based and SBFL-based techniques are highly complementary, as they tend to localize different subsets of compiler faults. Consequently, effectively integrating these two sources of information to improve compiler fault localization remains an open and largely unexplored challenge. To address this problem, we propose DualTrack, a hybrid approach that integrates dynamic execution information from SBFL with historical information derived from BICs. DualTrack employs a two-layer framework that first prioritizes files modified in bug-inducing commits and then refines their rankings using suspiciousness scores computed by SBFL formulas. An evaluation on 120 real-world compiler bugs from GCC and LLVM shows that DualTrack successfully identifies 52% of faulty files at the Top-1 rank, demonstrating a substantial improvement over existing state-of-the-art compiler fault localization techniques.  © 1976-2012 IEEE.
Author keywords: bug-inducing commit; Compilers; fault localization
Index keywords: Computer debugging; Program debugging; Software testing; Bug-inducing commit; Compiler; Downstream applications; Dynamic data; Fault localization; Historical data; Inherent complexity; Localization technique; Spectra's; Test projects; Program compilers
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2026
EID: 2-s2.0-105030728126
DOI: 10.1109/tse.2026.3666208
Retrieval channels: authoritative_outlet_search
Local full-text files: 

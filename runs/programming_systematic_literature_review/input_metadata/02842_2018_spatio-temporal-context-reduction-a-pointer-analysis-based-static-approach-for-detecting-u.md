---
otero_id: "2-s2.0-85133628257"
title: "Spatio-Temporal Context Reduction: A Pointer-Analysis-Based Static Approach for Detecting Use-After-Free Vulnerabilities"
authors: "Yan H.; Sui Y.; Chen S.; Xue J."
year: "2018"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3180155.3180178"
---
# Scopus title-abstract-keyword metadata
Title: Spatio-Temporal Context Reduction: A Pointer-Analysis-Based Static Approach for Detecting Use-After-Free Vulnerabilities
Abstract: Zero-day Use-After-Free (UAF) vulnerabilities are increasingly popular and highly dangerous, but few mitigations exist. We introduce a new pointer-analysis-based static analysis, CRed, for finding UAF bugs in multi-MLOC C source code efficiently and effectively. CRed achieves this by making three advances: (i) a spatio-temporal context reduction technique for scaling down soundly and precisely the exponential number of contexts that would otherwise be considered at a pair of free and use sites, (ii) a multi-stage analysis for filtering out false alarms efficiently, and (iii) a path-sensitive demand-driven approach for finding the points-to information required. We have implemented CRed in LLVM-3.8.0 and compared it with four different state-of-the-art static tools: CBMC (model checking), Clang (abstract interpretation), Coccinelle (pattern matching), and Supa (pointer analysis) using all the C test cases in Juliet Test Suite (JTS) and 10 open-source C applications. For the ground-truth validated with JTS, CRed detects all the 138 known UAF bugs as CBMC and Supa do while Clang and Coccinelle miss some bugs, with no false alarms from any tool. For practicality validated with the 10 applications (totaling 3+ MLOC), CRed reports 132 warnings including 85 bugs in 7.6 hours while the existing tools are either unscalable by terminating within 3 days only for one application (CBMC) or impractical by finding virtually no bugs (Clang and Coccinelle) or issuing an excessive number of false alarms (Supa).  © 2018 Copyright held by the owner/author(s).
Author keywords: bug detection; program analysis; Use-after-free
Index keywords: Alarm systems; C (programming language); Errors; Information filtering; Model checking; Open source software; Program debugging; Static analysis; Zero-day attack; % reductions; Bug detection; C# source code; Falsealarms; Pointer analysis; Program analysis; Reduction techniques; Spatio-temporal; Static approach; Use-after-free; Pattern matching
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2018
EID: 2-s2.0-85133628257
DOI: 10.1145/3180155.3180178
Retrieval channels: authoritative_outlet_search
Local full-text files: 

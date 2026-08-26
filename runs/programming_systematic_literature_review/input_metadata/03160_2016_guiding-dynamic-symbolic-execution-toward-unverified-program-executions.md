---
otero_id: "2-s2.0-84971462338"
title: "Guiding dynamic symbolic execution toward unverified program executions"
authors: "Christakis M.; Müller P.; Wüstholz V."
year: "2016"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/2884781.2884843"
---
# Scopus title-abstract-keyword metadata
Title: Guiding dynamic symbolic execution toward unverified program executions
Abstract: Most techniques to detect program errors, such as testing, code reviews, and static program analysis, do not fully verify all possible executions of a program. They leave executions unverified when they do not check certain properties, fail to verify properties, or check properties under certain unsound assumptions such as the absence of arithmetic overflow. In this paper, we present a technique to complement partial verification results by automatic test case generation. In contrast to existing work, our technique supports the common case that the verification results are based on unsound assumptions. We annotate programs to reflect which executions have been verified, and under which assumptions. These annotations are then used to guide dynamic symbolic execution toward unverified program executions. Our main technical contribution is a code instrumentation that causes dynamic symbolic execution to abort tests that lead to verified executions, to prune parts of the search space, and to prioritize tests that cover more properties that are not fully verified. We have implemented our technique for the.NET static analyzer Clousot and the dynamic symbolic execution tool Pex. It produces smaller test suites (by up to 19.2%), covers more unverified executions (by up to 7.1%), and reduces testing time (by up to 52.4%) compared to combining Clousot and Pex without our technique. © 2016 ACM.
Author keywords: 
Index keywords: Model checking; Software engineering; Automatic test-case generations; Code instrumentation; Dynamic symbolic executions; Partial verification; Program execution; Static program analysis; Technical contribution; Verification results; Software testing
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2016
EID: 2-s2.0-84971462338
DOI: 10.1145/2884781.2884843
Retrieval channels: authoritative_outlet_search
Local full-text files: 

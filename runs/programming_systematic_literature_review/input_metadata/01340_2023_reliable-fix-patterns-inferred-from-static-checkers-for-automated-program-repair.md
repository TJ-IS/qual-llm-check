---
otero_id: "2-s2.0-85164234765"
title: "Reliable Fix Patterns Inferred from Static Checkers for Automated Program Repair"
authors: "Liu K.; Zhang J.; Li L.; Koyuncu A.; Kim D.; Ge C.; Liu Z.; Klein J.; Bissyandé T.F."
year: "2023"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3579637"
---
# Scopus title-abstract-keyword metadata
Title: Reliable Fix Patterns Inferred from Static Checkers for Automated Program Repair
Abstract: Fix pattern-based patch generation is a promising direction in automated program repair (APR). Notably, it has been demonstrated to produce more acceptable and correct patches than the patches obtained with mutation operators through genetic programming. The performance of pattern-based APR systems, however, depends on the fix ingredients mined from fix changes in development histories. Unfortunately, collecting a reliable set of bug fixes in repositories can be challenging. In this article, we propose investigating the possibility in an APR scenario of leveraging fix patterns inferred from code changes that address violations detected by static analysis tools. To that end, we build a fix pattern-based APR tool, Avatar, which exploits fix patterns of static analysis violations as ingredients for the patch generation of repairing semantic bugs. Evaluated on four benchmarks (i.e., Defects4J, Bugs.jar, BEARS, and QuixBugs), Avatar presents the potential feasibility of fixing semantic bugs with the fix patterns inferred from the patches for fixing static analysis violations and can correctly fix 26 semantic bugs when Avatar is implemented with the normal program repair pipeline. We also find that Avatar achieves performance metrics that are comparable to that of the closely related approaches in the literature. Compared with CoCoNut, Avatar can fix 18 new bugs in Defects4J and 3 new bugs in QuixBugs. When compared with HDRepair, JAID, and SketchFix, Avatar can newly fix 14 Defects4J bugs. In terms of the number of correctly fixed bugs, Avatar is also comparable to the program repair tools with the normal fault localization setting and presents better performance than most program repair tools. These results imply that Avatar is complementary to current program repair approaches. We further uncover that Avatar can present different bug-fixing performances when it is configured with different fault localization tools, and the stack trace information from the failed executions of test cases can be exploited to improve the bug-fixing performance of Avatar by fixing more bugs with fewer generated patch candidates. Overall, our study highlights the relevance of static bug-finding tools as indirect contributors of fix ingredients for addressing code defects identified with functional test cases (i.e., dynamic information). © 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: Automated program repair; fix pattern; static analysis
Index keywords: Automation; Defects; Genetic algorithms; Genetic programming; Program debugging; Repair; Semantics; Automated program repair; Bug-fixing; Development history; Fault localization; Fix pattern; Mutation operators; Performance; Repair system; Repair tools; Test case; Static analysis
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2023
EID: 2-s2.0-85164234765
DOI: 10.1145/3579637
Retrieval channels: authoritative_outlet_search
Local full-text files: 

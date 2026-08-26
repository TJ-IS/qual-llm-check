---
otero_id: "2-s2.0-85139512997"
title: "Effective Isolation of Fault-Correlated Variables via Statistical and Mutation Analysis"
authors: "Wen M.; Xie Z.; Luo K.; Chen X.; Yang Y.; Jin H."
year: "2023"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2022.3209590"
---
# Scopus title-abstract-keyword metadata
Title: Effective Isolation of Fault-Correlated Variables via Statistical and Mutation Analysis
Abstract: It is a widely-adopted strategy for developers to monitor the values of program variables when debugging in practice. In particular, developers often set breakpoints at specific locations or execute the program step by step in the debugging mode to inspect if abnormal values or status will be observed for concerned variables. Such a practical debugging strategy can facilitate developers in understanding and localizing the target fault. This study aims to identify suspicious program variables of a given fault (i.e., denoted as fault-correlated variables) automatically, thus facilitating the debugging activities for developers. To the best of our knowledge, this is the finest granularity in fault localization (FL) so far, which can address the limitations of being coarse-grained as faced by existing FL techniques. However, isolating fault-correlated variables precisely is challenging since there are usually substantially different variables used or defined in a program, and plenty of them are in the same basic block which cannot be well discriminated from each other since they will be either executed or not against the given test suite. To address such challenges, this study presents IsoVar, a two-phase model to isolate fault-correlated variables. Specifically, IsoVar first performs statistical analysis based on variable execution matrices, which is a novel concept proposed in this study, to identify a set of suspicious variables. It then observes the impacts of those variables on the program dynamically after applying subtle mutations at the bytecode level, to further isolate fault-correlated variables. Extensive experiments on Defects4J and Bears demonstrate that IsoVar can outperform state-of-the-art techniques significantly (13.0% for MAP and 19.3% for MRR). More importantly, we incorporated IsoVar into 11 existing FL techniques as well as 14 automated program repair techniques, and found that IsoVar can significantly boost their performance.  © 1976-2012 IEEE.
Author keywords: debugging; Fault localization; program variables
Index keywords: Codes (symbols); Computer software maintenance; Latexes; Program debugging; Code; Computer bugs; Correlated variables; Debugging; Fault localization; Localization technique; Location awareness; Program variables; Software; Software testing
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2023
EID: 2-s2.0-85139512997
DOI: 10.1109/tse.2022.3209590
Retrieval channels: authoritative_outlet_search
Local full-text files: 

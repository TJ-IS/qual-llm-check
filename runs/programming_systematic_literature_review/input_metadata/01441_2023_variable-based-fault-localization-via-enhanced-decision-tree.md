---
otero_id: "2-s2.0-85183324747"
title: "Variable-based Fault Localization via Enhanced Decision Tree"
authors: "Jiang J.; Wang Y.; Chen J.; Lv D.; Liu M."
year: "2023"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3624741"
---
# Scopus title-abstract-keyword metadata
Title: Variable-based Fault Localization via Enhanced Decision Tree
Abstract: Fault localization, aiming at localizing the root cause of the bug under repair, has been a longstanding research topic. Although many approaches have been proposed in past decades, most of the existing studies work at coarse-grained statement or method levels with very limited insights about how to repair the bug (granularity problem), but few studies target the finer-grained fault localization. In this article, we target the granularity problem and propose a novel finer-grained variable-level fault localization technique. Specifically, the basic idea of our approach is that fault-relevant variables may exhibit different values in failed and passed test runs, and variables that have higher discrimination ability have a larger possibility to be the root causes of the failure. Based on this, we propose a program-dependency-enhanced decision tree model to boost the identification of fault-relevant variables via discriminating failed and passed test cases based on the variable values. To evaluate the effectiveness of our approach, we have implemented it in a tool called VarDT and conducted an extensive study over the Defects4J benchmark. The results show that VarDT outperforms the state-of-the-art fault localization approaches with at least 268.4% improvement in terms of bugs located at Top-1, and the average improvement is 351.3%. Besides, to investigate whether our finer-grained fault localization result can further improve the effectiveness of downstream APR techniques, we have adapted VarDT to the application of patch filtering, where we use the variables located by VarDT to filter incorrect patches. The results denote that VarDT outperforms the state-of-the-art PATCH-SIM and BATS by filtering 14.8% and 181.8% more incorrect patches, respectively, demonstrating the effectiveness of our approach. It also provides a new way of thinking for improving automatic program repair techniques.  © 2023 Copyright held by the owner/author(s).
Author keywords: decision tree; Fault localization; program debugging
Index keywords: Program debugging; Repair; Software testing; Coarse-grained; Decision-tree model; Discrimination ability; Fault localization; Fine grained; Localization technique; Research topics; Root cause; State of the art; Test runs; Decision trees
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2023
EID: 2-s2.0-85183324747
DOI: 10.1145/3624741
Retrieval channels: authoritative_outlet_search
Local full-text files: 

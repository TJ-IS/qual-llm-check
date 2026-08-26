---
otero_id: "2-s2.0-85202550337"
title: "GBSR: Graph-based suspiciousness refinement for improving fault localization"
authors: "Li Z.; Li M.; Wu S.; Xu S.; Chen X.; Liu Y."
year: "2024"
journal: "Journal of Systems and Software"
doi: "10.1016/j.jss.2024.112189"
---
# Scopus title-abstract-keyword metadata
Title: GBSR: Graph-based suspiciousness refinement for improving fault localization
Abstract: Fault Localization (FL) is an important and time-consuming phase of software debugging. The essence of FL lies in the process of calculating the suspiciousness of different program entities (e.g., statements) and generating a ranking list to guide developers in their code inspection. Nonetheless, a prevalent challenge within existing FL methodologies is the propensity for program entities with analogous execution information to receive a similar suspiciousness. This phenomenon can lead to confusion among developers, thereby reducing the effectiveness of debugging significantly. To alleviate this issue, we introduce fine-grained contextual information (such as partial code structural, coverage, and features from mutation analysis) to enrich the characteristics of program entities. Graphical structures are proposed to organize such information, where the passed and failed tests are constructed separately with the consideration of their differential impacts. In order to support the analysis of multidimensional features and the representation of large-scale programs, the PageRank algorithm is adopted to compute each program entity's weight. Rather than altering the fundamental FL process, we leverage these computed weights to refine the suspiciousness produced by various FL techniques, thereby providing developers with a more precise and actionable ranking of potential fault locations. The proposed strategy Graph-Based Suspiciousness Refinement (GBSR) is evaluated on 243 real-world faulty programs from the Defects4J. The results demonstrate that GBSR can improve the accuracy of various FL techniques. Specifically, for the refinement with traditional SBFL and MBFL techniques, the number of faults localized by the first position of the ranking list (Top-1) is increased by 189% and 68%, respectively. Furthermore, GBSR can also boost the state-of-the-art learning-based FL technique Grace by achieving a 2.8% performance improvement in Top-1. © 2024 Elsevier Inc.
Author keywords: Fault localization; Graph-based representation; Mutation analysis; PageRank algorithm; Suspiciousness refinement
Index keywords: Graph algorithms; Software testing; Code inspections; Fault localization; Graph-based; Graph-based representations; Localization technique; Mutation analysis; PageRank algorithm; Ranking lists; Software debugging; Suspiciousness refinement; Program debugging
Document type: Article
Conference: 
Source title: Journal of Systems and Software
Year: 2024
EID: 2-s2.0-85202550337
DOI: 10.1016/j.jss.2024.112189
Retrieval channels: authoritative_outlet_search
Local full-text files: 

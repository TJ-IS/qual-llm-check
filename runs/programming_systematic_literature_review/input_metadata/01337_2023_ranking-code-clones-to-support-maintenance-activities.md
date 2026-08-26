---
otero_id: "2-s2.0-85156089734"
title: "Ranking code clones to support maintenance activities"
authors: "Ehsan O.; Khomh F.; Zou Y.; Qiu D."
year: "2023"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-023-10292-0"
---
# Scopus title-abstract-keyword metadata
Title: Ranking code clones to support maintenance activities
Abstract: Developers often reuse code fragments by copy-and-paste activities to speed up code delivery. Through this copy-and-paste process, they create duplicated code, also known as code clones. As the software system evolves, the number of clones can increase substantially and impact code quality negatively. Prior studies have shown that inconsistent changes on code clones can introduce bugs in a software system and clones that have experienced some specific evolutionary patterns being more at risk than others. As the number of clone copies increases in a software system. it becomes tedious and time-consuming for developers to track and maintain all code clones. Recent studies have proposed approaches to analyze the clone evolution history for better clone maintenance. However, these approaches do not provide a specified list of code clones at a granular level (i.e., commits) that can help developers prioritize their clone maintenance activities. It is important to track the code clone changes at the commit level, as developers can fix/refactor code clones early. In this paper, we leverage machine learning to develop clone ranking models that can help developers identify the most risky clones early on. Specifically, we detect clones from 52 projects (34 Java and 18 C) that have 534,672 commits and build 469,239 clone genealogies. We extract 28 features capturing the characteristics of code clones at commit level. We then train learning-to-rank (LtR), classification, and regression machine learning models to rank the code clones based on fault occurrence during their evolutionary history. Our comparison of machine learning approaches indicates that classification (for the probability of being faulty) and regression (for the proportion of faulty changes) perform well in ranking code clones. Multiple unique developers who change a code clone and the age of a code clone (in terms of the number of cloned code changes) have a significant effect on the risk of faults in the code clones. Our results can help developers identify the most risky code clones first and prioritize them for refactoring to prevent future faults. © 2023, The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature.
Author keywords: Clone evolutionary patterns; Clone genealogies; Code clones; Learning-to-rank; Mixed-effect models; Regression approaches
Index keywords: Computer software; Computer software maintenance; History; Machine learning; Program debugging; Regression analysis; Clone evolutionary pattern; Clone genealogy; Code clone; Code fragments; Copy-and-paste; Maintenance activity; Mixed effects models; Regression approach; Reuse; Software-systems; Cloning
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2023
EID: 2-s2.0-85156089734
DOI: 10.1007/s10664-023-10292-0
Retrieval channels: authoritative_outlet_search
Local full-text files: 

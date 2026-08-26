---
otero_id: "2-s2.0-85109622596"
title: "Evaluating the impact of falsely detected performance bug-inducing changes in JIT models"
authors: "Quach S.; Lamothe M.; Adams B.; Kamei Y.; Shang W."
year: "2021"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-021-10004-6"
---
# Scopus title-abstract-keyword metadata
Title: Evaluating the impact of falsely detected performance bug-inducing changes in JIT models
Abstract: Performance bugs bear a heavy cost on both software developers and end-users. Tools to reduce the occurrence, impact, and repair time of performance bugs, can therefore provide key assistance for software developers racing to fix these bugs. Classification models that focus on identifying defect-prone commits, referred to as Just-In-Time (JIT) Quality Assurance are known to be useful in allowing developers to review risky commits. These commits can be reviewed while they are still fresh in developers’ minds, reducing the costs of developing high-quality software. JIT models, however, leverage the SZZ approach to identify whether or not a change is bug-inducing. The fixes to performance bugs may be scattered across the source code, separated from their bug-inducing locations. The nature of performance bugs may make SZZ a sub-optimal approach for identifying their bug-inducing commits. Yet, prior studies that leverage or evaluate the SZZ approach do not distinguish performance bugs from other bugs, leading to potential bias in the results. In this paper, we conduct an empirical study on the JIT defect prediction for performance bugs. We concentrate on SZZ’s ability to identify the bug-inducing commits of performance bugs in two open-source projects, Cassandra, and Hadoop. We verify whether the bug-inducing commits found by SZZ are truly bug-inducing commits by manually examining these identified commits. Our manual examination includes cross referencing fix commits and JIRA bug reports. We evaluate model performance for JIT models by using them to identify bug-inducing code commits for performance related bugs. Our findings show that JIT defect prediction classifies non-performance bug-inducing commits better than performance bug-inducing commits, i.e., the SZZ approach does introduce errors when identifying bug-inducing commits. However, we find that manually correcting these errors in the training data only slightly improves the models. In the absence of a large number of correctly labelled performance bug-inducing commits, our findings show that combining all available training data (i.e., truly performance bug-inducing commits, non-performance bug-inducing commits, and non-bug-inducing commits) yields the best classification results. © 2021, The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature.
Author keywords: Defect prediction bugs; Just-in-time; Performance; Software engineering
Index keywords: Classification (of information); Defects; Just in time production; Open source software; Quality assurance; Classification models; Classification results; High-quality software; Manual examination; Model performance; Open source projects; Optimal approaches; Software developer; Program debugging
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2021
EID: 2-s2.0-85109622596
DOI: 10.1007/s10664-021-10004-6
Retrieval channels: authoritative_outlet_search
Local full-text files: 

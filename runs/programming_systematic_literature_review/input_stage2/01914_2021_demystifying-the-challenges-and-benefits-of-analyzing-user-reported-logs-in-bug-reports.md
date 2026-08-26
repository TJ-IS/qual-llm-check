---
otero_id: "2-s2.0-85099289218"
title: "Demystifying the challenges and benefits of analyzing user-reported logs in bug reports"
authors: "Chen A.R.; Chen T.-H.; Wang S."
year: "2021"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-020-09893-w"
---
# Scopus title-abstract-keyword metadata
Title: Demystifying the challenges and benefits of analyzing user-reported logs in bug reports
Abstract: Logs in bug reports provide important debugging information for developers. During the debugging process, developers need to study the bug report and examine user-provided logs to understand the system executions that lead to the problem. Intuitively, user-provided logs illustrate the problems that users encounter and may help developers with the debugging process. However, some logs may be incomplete or inaccurate, which can cause difficulty for developers to diagnose the bug, and thus, delay the bug fixing process. In this paper, we conduct an empirical study on the challenges that developers may encounter when analyzing the user-provided logs and their benefits. In particular, we study both log snippets and exception stack traces in bug reports. We conduct our study on 10 large-scale open-source systems with a total of 1,561 bug reports with logs (BRWL) and 7,287 bug reports without logs (BRNL). Our findings show that: 1) BRWL takes longer time (median ranges from 3 to 91 days) to resolve compared to BRNL (median ranges from 1 to 25 days). We also find that reporters may not attach accurate or sufficient logs (i.e., developers often ask for additional logs in the Comments section of a bug report), which extends the bug resolution time. 2) Logs often provide a good indication of where a bug is located. Most bug reports (73%) have overlaps between the classes that generate the logs and their corresponding fixed classes. However, there is still a large number of bug reports where there is no overlap between the logged and fixed classes. 3) Our manual study finds that there is often missing system execution information in the logs. Many logs only show the point of failure (e.g., exception) and do not provide a direct hint on the actual root cause. In fact, through call graph analysis, we find that 28% of the studied bug reports have the fixed classes reachable from the logged classes, while they are not visible in the logs attached in bug reports. In addition, some logging statements are removed in the source code as the system evolves, which may cause further challenges in analyzing the logs. In short, our findings highlight possible future research directions to better help practitioners attach or analyze logs in bug reports. © 2021, The Author(s), under exclusive licence to Springer Science+Business Media, LLC part of Springer Nature.
Author keywords: Bug report; Empirical study; Log; Stack trace
Index keywords: Open source software; Open systems; Bug fixing process; Debugging information; Debugging process; Empirical studies; Execution informations; Open source system; Possible futures; Resolution time; Program debugging
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2021
EID: 2-s2.0-85099289218
DOI: 10.1007/s10664-020-09893-w
Retrieval channels: authoritative_outlet_search
Local full-text files: 

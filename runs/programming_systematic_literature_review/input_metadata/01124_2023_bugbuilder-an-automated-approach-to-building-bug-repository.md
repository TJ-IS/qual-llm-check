---
otero_id: "2-s2.0-85143057607"
title: "BugBuilder: An Automated Approach to Building Bug Repository"
authors: "Jiang Y.; Liu H.; Luo X.; Zhu Z.; Chi X.; Niu N.; Zhang Y.; Hu Y.; Bian P.; Zhang L."
year: "2023"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2022.3177713"
---
# Scopus title-abstract-keyword metadata
Title: BugBuilder: An Automated Approach to Building Bug Repository
Abstract: Bug-related research, e.g., fault localization, program repair, and software testing, relies heavily on high-quality and large-scale software bug repositories. The importance of such repositories is twofold. On one side, real-world bugs and their associated patches may inspire novel approaches for finding, locating, and repairing software bugs. On the other side, the real-world bugs and their patches are indispensable for rigorous and meaningful evaluation of approaches to software testing, fault localization, and program repair. To this end, a number of software bug repositories, e.g., iBUGS and Defects4J, have been constructed recently by mining version control systems and bug tracking systems. However, fully automated construction of bug repositories by simply taking bug-fixing commits from version control systems often results in inaccurate patches that contain many bug-irrelevant changes. Although we may request experts or developers to manually exclude the bug-irrelevant changes (as the authors of Defects4J did), such extensive human intervention makes it difficult to build large-scale bug repositories. To this end, in this paper, we propose an automatic approach, called BugBuilder, to construct bug repositories from version control systems. Different from existing approaches, it automatically extracts complete and concise bug-fixing patches and excludes bug-irrelevant changes. It first detects and excludes software refactorings involved in bug-fixing commits. BugBuilder then enumerates all subsets of the remaining part, and discards invalid subsets by compilation and software testing. If exactly a single subset survives the validation, this subset is taken as the complete and concise bug-fixing patch for the associated bug. In case multiple subsets survive, BugBuilder employs a sequence of heuristics to select the most likely one. Evaluation results on 809 real-world bug-fixing commits in Defects4J suggest that BugBuilder successfully extracted complete and concise bug-fixing patches from forty-three percent of the bug-fixing commits, and its precision (99%) was even higher than human experts. We also built a bug repository, called GrowingBugs, with the proposed approach. The resulting repository serves as evidence of the usefulness of the proposed approach, as well as a publicly available benchmark for bug-related research.  © 1976-2012 IEEE.
Author keywords: Bug; dataset; defect; patch; refactoring; repository; testing
Index keywords: Control systems; Defects; Program debugging; Repair; Set theory; Bug; Bug-fixing; Dataset; Fault localization; Patch; Real-world; Refactorings; Repository; Software testings; Version control system; Software testing
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2023
EID: 2-s2.0-85143057607
DOI: 10.1109/tse.2022.3177713
Retrieval channels: authoritative_outlet_search
Local full-text files: 

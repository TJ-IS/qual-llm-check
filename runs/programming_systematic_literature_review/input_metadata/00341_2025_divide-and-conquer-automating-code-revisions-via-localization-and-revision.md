---
otero_id: "2-s2.0-86000621445"
title: "Divide-and-Conquer: Automating Code Revisions via Localization-and-Revision"
authors: "Wang S.; Lin B.; Chen L.; Mao X."
year: "2025"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3697013"
---
# Scopus title-abstract-keyword metadata
Title: Divide-and-Conquer: Automating Code Revisions via Localization-and-Revision
Abstract: Despite its effectiveness in ensuring software quality, code review remains a labor-intensive and time-consuming task. In order to alleviate this burden on developers, researchers have proposed the automation of code review activities, particularly focusing on automating code revisions. This automation can benefit both code authors, as they are relieved from the manual task of code revision, and code reviewers, as they are spared from addressing minor code flaws through manual comments. While current code revision approaches have shown promising results, they typically operate within a single phase, in which the code requiring revision is treated as the input of a deep learning model, and the revised code is directly generated through a sequence-to-sequence transformation. Consequently, these approaches tackle both the challenges of localization (i.e., where to revise) and revision (i.e., how to revise) simultaneously. Attempting to handle the entire complex process with a single model goes against the principle of "Divide-and-Conquer,"which encourages breaking down complex problems into smaller sub-problems and addressing them individually. In fact, we have observed that existing code revision approaches often yield inaccurate results in both the localization and revision phases. In this article, we present a two-phase code revision approach that aims to overcome the aforementioned limitations by adhering to the "Divide-and-Conquer"principle. Our approach comprises two key components: a localizer, responsible for identifying the specific parts of the input code that require revisions, and a reviser, tasked with generating the revised code based on the localization result. Extensive experiments conducted on two widely used datasets demonstrate the substantial superiority of our approach over existing code revision approaches. For instance, when revising code based on the code reviewer's comments, our approach achieves a success rate of over 20% in implementing the ground-truth code revisions. In comparison, the widely used pre-trained model CodeT5 achieves a success rate of less than 16% on the same test set, which contains 16K+ cases.  © 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: Code Review; Code Revision; Localization
Index keywords: Coding errors; Computer software selection and evaluation; Program debugging; Code review; Code revision; Divide-and-conquer; Labor time; Labour-intensive; Localisation; Quality codes; Review activities; Software Quality; Time-consuming tasks; Software quality
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2025
EID: 2-s2.0-86000621445
DOI: 10.1145/3697013
Retrieval channels: authoritative_outlet_search
Local full-text files: 

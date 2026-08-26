---
otero_id: "2-s2.0-85206219383"
title: "When Automated Program Repair Meets Regression Testing - An Extensive Study on Two Million Patches"
authors: "Lou Y.; Yang J.; Benton S.; Hao D.; Tan L.; Chen Z.; Zhang L.; Zhang L."
year: "2024"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3672450"
---
# Scopus title-abstract-keyword metadata
Title: When Automated Program Repair Meets Regression Testing - An Extensive Study on Two Million Patches
Abstract: In recent years, Automated Program Repair (APR) has been extensively studied in academia and even drawn wide attention from the industry. However, APR techniques can be extremely time consuming since (1) a large number of patches can be generated for a given bug, and (2) each patch needs to be executed on the original tests to ensure its correctness. In the literature, various techniques (e.g., based on learning, mining, and constraint solving) have been proposed/studied to reduce the number of patches. Intuitively, every patch can be treated as a software revision during regression testing; thus, traditional Regression Test Selection (RTS) techniques can be leveraged to only execute the tests affected by each patch (as the other tests would keep the same outcomes) to further reduce patch execution time. However, few APR systems actually adopt RTS and there is still a lack of systematic studies demonstrating the benefits of RTS and the impact of different RTS strategies on APR. To this end, this article presents the first extensive study of widely used RTS techniques at different levels (i.e., class/method/statement levels) for 12 state-of-the-art APR systems on over 2M patches. Our study reveals various practical guidelines for bridging the gap between APR and regression testing, including: (1) the number of patches widely used for measuring APR efficiency can incur skewed conclusions, and the use of inconsistent RTS configurations can further skew the conclusions; (2) all studied RTS techniques can substantially improve APR efficiency and should be considered in future APR work; (3) method- and statement-level RTS outperform class-level RTS substantially and should be preferred; (4) RTS techniques can substantially outperform state-of-the-art test prioritization techniques for APR, and combining them can further improve APR efficiency; and (5) traditional Regression Test Prioritization (RTP) widely studied in regression testing performs even better than APR-specific test prioritization when combined with most RTS techniques. Furthermore, we also present the detailed impact of different patch categories and patch validation strategies on our findings.  © 2024 Copyright held by the owner/author(s).
Author keywords: patch validation; program repair; Test selection
Index keywords: Automatic programming; Computer software selection and evaluation; Program debugging; Patch validation; Program repair; Regression test selection; Regression testing; Repair efficiencies; Repair system; Selection techniques; State of the art; Test prioritization; Test selection; Software testing
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2024
EID: 2-s2.0-85206219383
DOI: 10.1145/3672450
Retrieval channels: authoritative_outlet_search
Local full-text files: 

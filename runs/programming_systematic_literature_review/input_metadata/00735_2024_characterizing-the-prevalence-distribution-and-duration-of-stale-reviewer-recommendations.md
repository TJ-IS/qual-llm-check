---
otero_id: "2-s2.0-85197525845"
title: "Characterizing the Prevalence, Distribution, and Duration of Stale Reviewer Recommendations"
authors: "Kazemi F.; Lamothe M.; McIntosh S."
year: "2024"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2024.3422369"
---
# Scopus title-abstract-keyword metadata
Title: Characterizing the Prevalence, Distribution, and Duration of Stale Reviewer Recommendations
Abstract: The appropriate assignment of reviewers is a key factor in determining the value that organizations can derive from code review. While inappropriate reviewer recommendations can hinder the benefits of the code review process, identifying these assignments is challenging. Stale reviewers, i.e., those who no longer contribute to the project, are one type of reviewer recommendation that is certainly inappropriate. Understanding and minimizing this type of recommendation can thus enhance the benefits of the code review process. While recent work demonstrates the existence of stale reviewers, to the best of our knowledge, attempts have yet to be made to characterize and mitigate them. In this paper, we study the prevalence and potential effects. We then propose and assess a strategy to mitigate stale recommendations in existing code reviewer recommendation tools. By applying five code reviewer recommendation approaches (LearnRec, RetentionRec, cHRev, Sofia, and WLRRec) to three thriving open-source systems with 5,806 contributors, we observe that, on average, 12.59% of incorrect recommendations are stale due to developer turnover; however, fewer stale recommendations are made when the recency of contributions is considered by the recommendation objective function. We also investigate which reviewers appear in stale recommendations and observe that the top reviewers account for a considerable proportion of stale recommendations. For instance, in 15.31% of cases, the top-3 reviewers account for at least half of the stale recommendations. Finally, we study how long stale reviewers linger after the candidate leaves the project, observing that contributors who left the project 7.7 years ago are still suggested to review change sets. Based on our findings, we propose separating the reviewer contribution recency from the other factors that are used by the CRR objective function to filter out developers who have not contributed during a specified duration. By evaluating this strategy with different intervals, we assess the potential impact of this choice on the recommended reviewers. The proposed filter reduces the staleness of recommendations, i.e., the Staleness Reduction Ratio (SRR) improves between 21.44%-92.39%. Yet since the strategy may increase active reviewer workload, careful project-specific exploration of the impact of the cut-off setting is crucial.  © 1976-2012 IEEE.
Author keywords: Code review; code reviewer recommendation; developer turnover
Index keywords: Job analysis; Linear programming; Open source software; Open systems; Code; Code review; Code reviewer recommendation; Delay; Developer turnover; Linear-programming; Objective functions; Review process; Software; Task analysis; Codes (symbols)
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2024
EID: 2-s2.0-85197525845
DOI: 10.1109/tse.2024.3422369
Retrieval channels: authoritative_outlet_search
Local full-text files: 

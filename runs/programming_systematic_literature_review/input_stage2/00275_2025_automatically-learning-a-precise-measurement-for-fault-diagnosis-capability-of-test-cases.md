---
otero_id: "2-s2.0-105012395700"
title: "Automatically Learning a Precise Measurement for Fault Diagnosis Capability of Test Cases"
authors: "Zhao Y.; Sun Z.; Wang G.; Liang Q.; Zhang Y.; Lou Y.; Hao D.; Zhang L."
year: "2025"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3712189"
---
# Scopus title-abstract-keyword metadata
Title: Automatically Learning a Precise Measurement for Fault Diagnosis Capability of Test Cases
Abstract: Prevalent Fault Localization (FL) techniques rely on tests to localize buggy program elements. Tests could be treated as fuel to further boost FL by providing more debugging information. Therefore, it is highly valuable to measure the Fault Diagnosis Capability (FDC) of a test for diagnosing faults, so as to select or generate tests to better help FL (i.e., FL-oriented test selection or FL-oriented test generation). To this end, researchers have proposed many FDC metrics, which serve as the selection criterion in FL-oriented test selection or the fitness function in FL-oriented test generation. Existing FDC metrics can be classified into result-agnostic and result-aware metrics depending on whether they take test results (i.e., passing or failing) as input. Although result-aware metrics perform better in test selection, they have restricted applications due to the input of test results, e.g., they cannot be applied to guide test generation. Moreover, all the existing FDC metrics are designed based on some pre-defined heuristics and have achieved limited FL performance due to their inaccuracy. To address these issues, in this article, we reconsider result-agnostic metrics (i.e., metrics that do not take test results as input), and propose a novel result-agnostic metric RLFDC which predicts FDC values of tests through reinforcement learning. In particular, we treat FL results as reward signals, and train an FDC prediction model with the direct FL feedback to automatically learn a more accurate measurement rather than design one based on pre-defined heuristics. Finally, we evaluate the proposed RLFDC on Defects4J by applying the studied metrics to test selection and generation. According to the experimental results, the proposed RLFDC outperforms all the result-agnostic metrics in both test selection and generation, e.g., when applied to selecting human-written tests, RLFDC achieves 28.2% and 21.6% higher acc@1 and mAP values compared to the state-of-the-art result-agnostic metric TfD. Besides, RLFDC even achieves competitive performance compared to the state-of-the-art result-aware metric FDG in test selection.  © 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: Fault diagnosability; Fault localization; Reinforcement learning
Index keywords: Computer debugging; Fault detection; Machine learning; Program debugging; Fault diagnosability; Fault localization; Faults diagnosis; Localization technique; Precise measurements; Reinforcement learnings; State of the art; Test case; Test generations; Test selection; Failure analysis; Software testing
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2025
EID: 2-s2.0-105012395700
DOI: 10.1145/3712189
Retrieval channels: authoritative_outlet_search
Local full-text files: 

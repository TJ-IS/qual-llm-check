---
otero_id: "2-s2.0-85212956955"
title: "SURE: A Visualized Failure Indexing Approach Using Program Memory Spectrum"
authors: "Song Y.; Zhang X.; Xie X.; Chen S.; Liu Q.; Gao R."
year: "2024"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3676958"
---
# Scopus title-abstract-keyword metadata
Title: SURE: A Visualized Failure Indexing Approach Using Program Memory Spectrum
Abstract: Failure indexing is a longstanding crux in software debugging, the goal of which is to automatically divide failures (e.g., failed test cases) into distinct groups according to the culprit root causes, as such multiple faults residing in a faulty program can be handled independently and simultaneously. The community of failure indexing has long been plagued by two challenges: (1) The effectiveness of division is still far from promising. Specifically, existing failure indexing techniques only employ a limited source of software runtime data, for example, code coverage, to be failure proximity and further divide them, which typically delivers unsatisfactory results. (2) The outcome can be hardly comprehensible. Specifically, a developer who receives the division result is just aware of how all failures are divided, without knowing why they should be divided the way they are. This leads to difficulties for developers to be convinced by the division result, which in turn affects the adoption of the results. To tackle these two problems, in this article, we propose SURE, a viSUalized failuRe indExing approach using the program memory spectrum (PMS). We first collect the runtime memory information (i.e., variables’ names and values, as well as the depth of the stack frame) at several preset breakpoints during the execution of a failed test case, and transform the gathered memory information into a human-friendly image (called PMS). Then, any pair of PMS images that serve as proxies for two failures is fed to a trained Siamese convolutional neural network, to predict the likelihood of them being triggered by the same fault. Last, a clustering algorithm is adopted to divide all failures based on the mentioned likelihood. In the experiments, we use 30% of the simulated faults to train the neural network, and use 70% of the simulated faults as well as real-world faults to test. Results demonstrate the effectiveness of SURE: It achieves 101.20% and 41.38% improvements in faults number estimation, as well as 105.20% and 35.53% improvements in clustering, compared with the state-of-the-art technique in this field, in simulated and real-world environments, respectively. Moreover, we carry out a human study to quantitatively evaluate the comprehensibility of PMS, revealing that this novel type of representation can help developers better comprehend failure indexing results. © 2024 Copyright held by the owner/author(s)
Author keywords: failure indexing; Failure proximity; parallel debugging; program memory; siamese learning
Index keywords: Automatic indexing; Computer debugging; Data visualization; Indexing (materials working); Model checking; Software testing; Clusterings; Failure indexing; Failure proximities; Indexing approaches; Parallel debugging; Program memory; Siamese learning; Software debugging; Spectra's; Test case; Program debugging
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2024
EID: 2-s2.0-85212956955
DOI: 10.1145/3676958
Retrieval channels: authoritative_outlet_search
Local full-text files: 

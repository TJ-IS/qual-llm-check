---
otero_id: "2-s2.0-105010313067"
title: "Toward a Better Understanding of Probabilistic Delta Debugging"
authors: "Zhang M.; Xu Z.; Tian Y.; Cheng X.; Sun C."
year: "2025"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse55347.2025.00117"
---
# Scopus title-abstract-keyword metadata
Title: Toward a Better Understanding of Probabilistic Delta Debugging
Abstract: Given a list L of elements and a property ψ that L exhibits, ddmin is a classic test input minimization algorithm that aims to automatically remove ψ-irrelevant elements from L. This algorithm has been widely adopted in domains such as test input minimization and software debloating. Recently, ProbDD, a variant of ddmin, has been proposed and achieved state-of-the-art performance. By employing Bayesian optimization, ProbDD estimates the probability of each element in L being relevant to ψ, and statistically decides which and how many elements should be deleted together each time. However, the theoretical probabilistic model of ProbDD is rather intricate, and the underlying details for the superior performance of ProbDD have not been adequately explored. In this paper, we conduct the first in-depth theoretical analysis of ProbDD, clarifying the trends in probability and subset size changes and simplifying the probability model. We complement this analysis with empirical experiments, including success rate analysis, ablation studies, and examinations of trade-offs and limitations, to further comprehend and demystify this state-of-the-art algorithm. Our success rate analysis reveals how ProbDD effectively addresses bottlenecks that slow down ddmin by skipping inefficient queries that attempt to delete complements of subsets and previously tried subsets. The ablation study illustrates that randomness in ProbDD has no significant impact on efficiency. These findings provide valuable insights for future research and applications of test input minimization algorithms. Based on the findings above, we propose CDD, a simplified version of ProbDD, reducing the complexity in both theory and implementation. CDD assists in 1 validating the correctness of our key findings, e.g., that probabilities in ProbDD essentially serve as monotonically increasing counters for each element, and 2 identifying the main factors that truly contribute to ProbDD's superior performance. Our comprehensive evaluations across 76 benchmarks in test input minimization and software debloating demonstrate that CDD can achieve the same performance as ProbDD, despite being much simplified.  © 2025 IEEE.
Author keywords: Delta Debugging; Program Reduction; Software Debloating; Test Input Minimization
Index keywords: Ablation; Benchmarking; Optimization; Probabilistic logics; Program debugging; Software testing; Statistical tests; % reductions; Delta debugging; Minimisation; Minimization algorithms; Performance; Program reduction; Rate analysis; Software debloating; Test input minimization; Test inputs; Economic and social effects
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2025
EID: 2-s2.0-105010313067
DOI: 10.1109/icse55347.2025.00117
Retrieval channels: authoritative_outlet_search
Local full-text files: 

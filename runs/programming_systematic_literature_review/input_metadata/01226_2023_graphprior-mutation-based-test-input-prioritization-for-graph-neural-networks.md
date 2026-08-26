---
otero_id: "2-s2.0-85180634937"
title: "GraphPrior: Mutation-based Test Input Prioritization for Graph Neural Networks"
authors: "Dang X.; Li Y.; Papadakis M.; Klein J.; Bissyandé T.F.; Le Traon Y."
year: "2023"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3607191"
---
# Scopus title-abstract-keyword metadata
Title: GraphPrior: Mutation-based Test Input Prioritization for Graph Neural Networks
Abstract: Graph Neural Networks (GNNs) have achieved promising performance in a variety of practical applications. Similar to traditional DNNs, GNNs could exhibit incorrect behavior that may lead to severe consequences, and thus testing is necessary and crucial. However, labeling all the test inputs for GNNs can be costly and time-consuming, especially when dealing with large and complex graphs, which seriously affects the efficiency of GNN testing. Existing studies have focused on test prioritization for DNNs, which aims to identify and prioritize fault-revealing tests (i.e., test inputs that are more likely to be misclassified) to detect system bugs earlier in a limited time. Although some DNN prioritization approaches have been demonstrated effective, there is a significant problem when applying them to GNNs: They do not take into account the connections (edges) between GNN test inputs (nodes), which play a significant role in GNN inference. In general, DNN test inputs are independent of each other, while GNN test inputs are usually represented as a graph with complex relationships between each test. In this article, we propose GraphPrior (GNN-oriented Test Prioritization), a set of approaches to prioritize test inputs specifically for GNNs via mutation analysis. Inspired by mutation testing in traditional software engineering, in which test suites are evaluated based on the mutants they kill, GraphPrior generates mutated models for GNNs and regards test inputs that kill many mutated models as more likely to be misclassified. Then, GraphPrior leverages the mutation results in two ways, killing-based and feature-based methods. When scoring a test input, the killing-based method considers each mutated model equally important, while feature-based methods learn different importance for each mutated model through ranking models. Finally, GraphPrior ranks all the test inputs based on their scores. We conducted an extensive study based on 604 subjects to evaluate GraphPrior on both natural and adversarial test inputs. The results demonstrate that KMGP, the killing-based GraphPrior approach, outperforms the compared approaches in a majority of cases, with an average improvement of 4.76% ∼49.60% in terms of APFD. Furthermore, the feature-based GraphPrior approach, RFGP, performs the best among all the GraphPrior approaches. On adversarial test inputs, RFGP outperforms the compared approaches across different adversarial attacks, with the average improvement of 2.95% ∼46.69%. © 2023 Copyright held by the owner/author(s).
Author keywords: Graph Neural Networks; Labelling; Mutation; Test Input Prioritization
Index keywords: Complex networks; Program debugging; Software testing; Feature-based method; Graph neural networks; Labelings; Mutated models; Mutation; Network test; Prioritization; Test input prioritization; Test inputs; Test prioritization; Graph neural networks
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2023
EID: 2-s2.0-85180634937
DOI: 10.1145/3607191
Retrieval channels: authoritative_outlet_search
Local full-text files: 

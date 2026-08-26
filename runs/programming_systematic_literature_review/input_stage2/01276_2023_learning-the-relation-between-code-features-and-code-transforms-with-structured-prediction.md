---
otero_id: "2-s2.0-85161054017"
title: "Learning the Relation between Code Features and Code Transforms with Structured Prediction"
authors: "Yu Z.; Martinez M.; Chen Z.; Bissyande T.F.; Monperrus M."
year: "2023"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2023.3275380"
---
# Scopus title-abstract-keyword metadata
Title: Learning the Relation between Code Features and Code Transforms with Structured Prediction
Abstract: To effectively guide the exploration of the code transform space for automated code evolution techniques, we present in this article the first approach for structurally predicting code transforms at the level of AST nodes using conditional random fields (CRFs). Our approach first learns offline a probabilistic model that captures how certain code transforms are applied to certain AST nodes, and then uses the learned model to predict transforms for arbitrary new, unseen code snippets. Our approach involves a novel representation of both programs and code transforms. Specifically, we introduce the formal framework for defining the so-called AST-level code transforms and we demonstrate how the CRF model can be accordingly designed, learned, and used for prediction. We instantiate our approach in the context of repair transform prediction for Java programs. Our instantiation contains a set of carefully designed code features, deals with the training data imbalance issue, and comprises transform constraints that are specific to code. We conduct a large-scale experimental evaluation based on a dataset of bug fixing commits from real-world Java projects. The results show that when the popular evaluation metric top-3 is used, our approach predicts the code transforms with an accuracy varying from 41% to 53% depending on the transforms. Our model outperforms two baselines based on history probability and neural machine translation (NMT), suggesting the importance of considering code structure in achieving good prediction accuracy. In addition, a proof-of-concept synthesizer is implemented to concretize some repair transforms to get the final patches. The evaluation of the synthesizer on the Defects4j benchmark confirms the usefulness of the predicted AST-level repair transforms in producing high-quality patches.  © 1976-2012 IEEE.
Author keywords: big code; Code transform; machine learning; program repair
Index keywords: Benchmarking; Codes (symbols); Computer software; Forecasting; Java programming language; Large dataset; Learning algorithms; Learning systems; Quality control; Random processes; Big code; Code; Codes transform; Computer bugs; Feature transform; Features extraction; Machine-learning; Predictive models; Program repair; Synthesizer; Feature extraction
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2023
EID: 2-s2.0-85161054017
DOI: 10.1109/tse.2023.3275380
Retrieval channels: authoritative_outlet_search
Local full-text files: 

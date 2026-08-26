---
otero_id: "2-s2.0-85218105360"
title: "Automating TODO-missed Methods Detection and Patching"
authors: "Gao Z.; Su Y.; Hu X.; Xia X."
year: "2024"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3700793"
---
# Scopus title-abstract-keyword metadata
Title: Automating TODO-missed Methods Detection and Patching
Abstract: TODO comments are widely used by developers to remind themselves or others about incomplete tasks. In other words, TODO comments are usually associated with temporary or suboptimal solutions. In practice, all the equivalent suboptimal implementations should be updated (e.g., adding TODOs) simultaneously. However, due to various reasons (e.g., time constraints or carelessness), developers may forget or even are unaware of adding TODO comments to all necessary places, which results in the TODO-missed methods. These "hidden"suboptimal implementations in TODO-missed methods may hurt the software quality and maintainability in the long-term. Therefore, in this article, we propose the novel task of TODO-missed methods detection and patching and develop a novel model, namely TODO-comment Patcher (TDPatcher), to automatically patch TODO comments to the TODO-missed methods in software projects. Our model has two main stages: offline learning and online inference. During the offline learning stage, TDPatcher employs the GraphCodeBERT and contrastive learning for encoding the TODO comment (natural language) and its suboptimal implementation (code fragment) into vector representations. For the online inference stage, we can identify the TODO-missed methods and further determine their patching position by leveraging the offline trained model. We built our dataset by collecting TODO-introduced methods from the top-10,000 Python GitHub repositories and evaluated TDPatcher on them. Extensive experimental results show the promising performance of our model over a set of benchmarks. We further conduct an in-the-wild evaluation that successfully detects 26 TODO-missed methods from 50 GitHub repositories. © 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: contrastive learning; SATD; software inconsistency; technical debt; TODO comment
Index keywords: Adversarial machine learning; Benchmarking; Program debugging; Off-line learning; Online inferences; SATD; Software inconsistency; Software maintainability; Suboptimal implementations; Suboptimal solution; Technical debts; Time constraints; TODO comment; Computer software selection and evaluation
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2024
EID: 2-s2.0-85218105360
DOI: 10.1145/3700793
Retrieval channels: authoritative_outlet_search
Local full-text files: 

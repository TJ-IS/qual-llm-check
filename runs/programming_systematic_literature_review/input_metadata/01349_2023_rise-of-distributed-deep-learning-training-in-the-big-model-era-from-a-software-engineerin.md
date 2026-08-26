---
otero_id: "2-s2.0-85174705020"
title: "Rise of Distributed Deep Learning Training in the Big Model Era: From a Software Engineering Perspective"
authors: "Liu X.; Gu D.; Chen Z.; Wen J.; Zhang Z.; Ma Y.; Wang H.; Jin X."
year: "2023"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3597204"
---
# Scopus title-abstract-keyword metadata
Title: Rise of Distributed Deep Learning Training in the Big Model Era: From a Software Engineering Perspective
Abstract: Deep learning (DL) has become a key component of modern software. In the "big model"era, the rich features of DL-based software (i.e., DL software) substantially rely on powerful DL models, e.g., BERT, GPT-3, and the recently emerging GPT-4, which are trained on the powerful cloud with large datasets. Hence, training effective DL models has become a vital stage in the whole software lifecycle. When training deep learning models, especially those big models, developers need to parallelize and distribute the computation and memory resources amongst multiple devices (e.g., a cluster of GPUs) in the training process, which is known as distributed deep learning training, or distributed training for short. However, the unique challenges that developers encounter in distributed training process have not been studied in the software engineering community. Given the increasingly heavy dependence of current DL-based software on distributed training, this paper aims to fill in the knowledge gap and presents the first comprehensive study on developers' issues in distributed training. To this end, we focus on popular DL frameworks that support distributed training (including TensorFlow, PyTorch, Keras, and Horovod) and analyze 1,131 real-world developers' issues about using these frameworks reported on Stack Overflow and GitHub. We construct a fine-grained taxonomy consisting of 30 categories regarding the fault symptoms and summarize common fix patterns for different symptoms. We find that: (1) many distributed-specific faults and non-distributed-specific faults inherently share the same fault symptoms, making it challenging to debug; (2) most of the fault symptoms have frequent fix patterns; (3) about half of the faults are related to system-level configurations. Based on the results, we suggest actionable implications on research avenues that can potentially facilitate the distributed training to develop DL-based software, such as focusing on the frequent and common fix patterns when designing testing or debugging tools, developing efficient testing and debugging techniques for communication configuration along with the synthesis of network configuration analysis, designing new multi-device checkpoint-and-replay techniques to help reproduction, and designing serverless APIs for cloud platforms. © 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: distributed training; Empirical study; software engineering
Index keywords: Cell proliferation; Deep learning; Large dataset; Learning systems; Life cycle; Program processors; Software testing; Distributed training; Empirical studies; Engineering perspective; Fault symptoms; Large datasets; Learning models; Learning software; Rich features; Software life cycles; Training process; Program debugging
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2023
EID: 2-s2.0-85174705020
DOI: 10.1145/3597204
Retrieval channels: authoritative_outlet_search
Local full-text files: 

---
otero_id: "2-s2.0-85210471264"
title: "PromeTrans: Bootstrap binary functionality classification with knowledge transferred from pre-trained models"
authors: "Sha Z.; Zhang C.; Wang H.; Gao Z.; Zhang B.; Lan Y.; Shu H."
year: "2025"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-024-10593-y"
---
# Scopus title-abstract-keyword metadata
Title: PromeTrans: Bootstrap binary functionality classification with knowledge transferred from pre-trained models
Abstract: Pre-trained models have witnessed significant progress in nature language (including source code) and binary code comprehension. However, none of them are suitable for binary functionality classification (BFC). In this paper, we present the first pre-trained model-based solution to BFC, namely PromeTrans, by fusing the knowledge of pre-trained models. Specifically, it overcomes the token size limitation of pre-trained models with a novel function outlining scheme and utilizes existing pre-trained assembly language models (AsmLMs) to generate embeddings for binary functions. Then, it utilizes a Graph Attention Network (GAT) to aggregate function embeddings following the call graph into a functionality embedding for each function. Lastly, it leverages existing pre-trained large natural language models (LLMs, e.g., GPT-3.5) to classify the functionality of source code functions and align the labels to binary functions. Based on the functionality embedding provided by AsmLMs and GAT and the functionality label knowledge provided by LLMs, a simple multi-layer perceptron (MLP) model is trained to classify the functionality of binary functions. Our prototype PromeTrans yields state-of-the-art (SOTA) performance on various datasets and achieves low overhead. PromeTrans also exhibits exceptional results in real-world applications (e.g., malware analysis). Additionally, by analyzing PromeTrans’s training history, we confirm the quality of knowledge transferred from LLMs is high. It shows that transferring knowledge from pre-trained models has a strong potential to bootstrap binary program comprehension tasks beyond BFC. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2024.
Author keywords: Large language model; Neural networks; Program comprehension; Reverse engineering; Static analysis
Index keywords: Application programs; Binary codes; Graph embeddings; Graph neural networks; Multilayer neural networks; Program debugging; Binary functionality; Binary functions; Embeddings; Functionality classification; Language model; Large language model; Natural language model; Neural-networks; Program comprehension; Source codes; Reverse engineering
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2025
EID: 2-s2.0-85210471264
DOI: 10.1007/s10664-024-10593-y
Retrieval channels: authoritative_outlet_search
Local full-text files: 

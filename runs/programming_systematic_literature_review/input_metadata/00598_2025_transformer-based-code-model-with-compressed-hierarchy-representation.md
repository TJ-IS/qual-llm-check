---
otero_id: "2-s2.0-85217807570"
title: "Transformer-based code model with compressed hierarchy representation"
authors: "Zhang K.; Li J.; Li Z.; Jin Z.; Li G."
year: "2025"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-025-10612-6"
---
# Scopus title-abstract-keyword metadata
Title: Transformer-based code model with compressed hierarchy representation
Abstract: Source code representation with deep learning techniques is an important research field. There have been many studies to learn sequential or structural information for code representation. However, existing sequence-based models and non-sequence models both have their limitations. Although researchers attempt to incorporate structural information into sequence-based models, they only mine part of token-level hierarchical structure information. In this paper, we analyze how the complete hierarchical structure influences the tokens in code sequences and abstract this influence as a property of code tokens called hierarchical embedding. This hierarchical structure includes frequent combinations, which represent strong semantics and can help identify unique code structures. We further analyze these hierarchy combinations and propose a novel compression algorithm Hierarchy BPE. Our algorithm can extract frequent hierarchy combinations and reduce the total length of hierarchical embedding. Based on the above compression algorithm, we propose the Byte-Pair Encoded Hierarchy Transformer (BPE-HiT), a simple but effective sequence model that incorporates the compressed hierarchical embeddings of source code into a Transformer model. Given that BPE-HiT significantly reduces computational overhead, we scale up the model training phase and implement a hierarchy-aware pre-training framework. We conduct extensive experiments on 10 datasets for evaluation, including code classification, clone detection, method name prediction and code completion tasks. Results show that our non-pre-trained BPE-HiT outperforms the state-of-the-art baselines by at least 0.94% on average accuracy on code classification tasks with three different program languages. On the method name prediction task, BPE-HiT outperforms baselines by at least 2.04, 1.34 in F1-score on two real-world datasets. Besides, our pre-trained BPE-HiT outperforms other pre-trained baseline models with the same number of parameters over all experiments, demonstrating the robust capability of our approach. Furthermore, we conduct a detailed ablation study, proving the effectiveness of our compression algorithm and the training efficiency of our proposed model. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025.
Author keywords: Clone detection; Code classification; Code representation; Code summarization
Index keywords: Codes (symbols); Deep learning; Embeddings; Clone detection; Code classification; Code representation; Code summarization; Compression algorithms; Embeddings; Hierarchical structures; Sequence models; Source code representations; Structural information; Semantics
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2025
EID: 2-s2.0-85217807570
DOI: 10.1007/s10664-025-10612-6
Retrieval channels: authoritative_outlet_search
Local full-text files: 

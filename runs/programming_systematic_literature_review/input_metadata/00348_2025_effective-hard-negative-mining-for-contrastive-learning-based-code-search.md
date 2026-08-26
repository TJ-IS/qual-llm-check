---
otero_id: "2-s2.0-86000649836"
title: "Effective Hard Negative Mining for Contrastive Learning-Based Code Search"
authors: "Fan Y.; Li C.; Ge J.; Huang L.; Luo B."
year: "2025"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3695994"
---
# Scopus title-abstract-keyword metadata
Title: Effective Hard Negative Mining for Contrastive Learning-Based Code Search
Abstract: Background. Code search aims to find the most relevant code snippet in a large codebase based on a given natural language query. An accurate code search engine can increase code reuse and improve programming efficiency. The focus of code search is how to represent the semantic similarity of code and query. With the development of code pre-trained models, the pattern of using numeric feature vectors (embeddings) to represent code semantics and using vector distance to represent semantic similarity has replaced traditional string matching methods. The quality of semantic representations is critical to the effectiveness of downstream tasks such as code search. Currently, the state-of-the-art (SOTA) learning method uses the contrastive learning paradigm. The objective of contrastive learning is to maximize the similarity between matching code and query (positive samples) and minimize the similarity between mismatched pairs (negative samples). To increase the reusing of negative samples, prior contrastive learning approaches use a large queue (memory bank) to store embeddings.Problem. However, there is still a lot of room for improvement in using negative examples for code search: 1 Due to the random selection of negative samples, semantic representations learned by existing models cannot distinguish similar codes well. 2 Since semantic vectors in the memory bank are reused from previous inference results and then directly used for loss function calculation without gradient descent, the model cannot effectively learn the negative sample semantic information. Method. To solve the above problems, we propose a contrastive learning code search model with hard negative mining called CoCoHaNeRe: 1 To enable the model to distinguish similar codes, we introduce hard negative examples into contrastive training, which are negative examples in the codebase that are most similar to positive examples. As a result, hard negative examples are most likely to make the model make mistakes. 2 To improve the learning efficiency of negative samples during training, we add all hard negative examples to the model's gradient descent process. Result. To verify the effectiveness of CoCoHaNeRe, we conducted experiments on large code search datasets with six programming languages, as well as similar retrieval tasks code clone detection and code question answering. Experimental results show that our model achieves SOTA performance. In the code search task, the average MRR score of CoCoHaNeRe exceeds CodeBERT, GraphCodeBERT, and UniXcoder by 11.25%, 8.13%, and 7.38%, respectively. It has also made great progress in code clone detection and code question answering. In addition, our method performs well in different programming languages and code pre-training models. Furthermore, qualitative analysis shows that our model effectively distinguishes high-order semantic differences between similar codes.  © 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: Code Pre-trained Model; Code Search; Contrastive Learning; Hard Negative Mining
Index keywords: Computer software reusability; Inference engines; Pipeline codes; Problem oriented languages; Program debugging; Query languages; Semantics; Vectors; Code pre-trained model; Code search; Embeddings; Hard negative mining; Memory banks; Negative examples; Negative minings; Negative samples; Semantic representation; Semantic similarity; Embeddings
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2025
EID: 2-s2.0-86000649836
DOI: 10.1145/3695994
Retrieval channels: authoritative_outlet_search
Local full-text files: 

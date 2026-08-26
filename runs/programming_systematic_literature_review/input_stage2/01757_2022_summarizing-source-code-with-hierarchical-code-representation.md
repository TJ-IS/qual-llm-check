---
otero_id: "2-s2.0-85120352832"
title: "Summarizing source code with hierarchical code representation"
authors: "Zhou Z.; Yu H.; Fan G.; Huang Z.; Yang X."
year: "2022"
journal: "Information and Software Technology"
doi: "10.1016/j.infsof.2021.106761"
---
# Scopus title-abstract-keyword metadata
Title: Summarizing source code with hierarchical code representation
Abstract: Context: Code summarization aims to automatically generate natural language descriptions for code, and has become a rapidly expanding research area. Data-driven code summarization models based on neural networks have proliferated in recent few years. Objective: Almost all of existing neural models are built upon the granularity of token or AST node. This has several drawbacks: a) Code summarization requires high-level knowledge of code while token representations are limited to provide a global view; b) Such approaches can hardly model the hierarchy of code; c) Long input codes challenge such models to handle long-range dependencies due to the large number of tokens and AST nodes. Method: To address these issues, we propose a novel framework to utilize hierarchical representation of code to generate better summaries. We consider two levels of code hierarchy: token-level and statement-level. Our framework contains a pair of customized encoder-decoder models for tokens and AST of code respectively. Each of them has a hierarchical encoder that aims to extract both token and statement-level code features, and an attentional decoder with the ability to attend to those different levels of representation during decoding. They are then combined to predict summaries via ensemble learning. Results: We conduct extensive experiments to evaluate our models on a large Java corpus. The experimental results show that our approach outperforms several state-of-the-art baselines by a substantial margin. Conclusion: In conclusion, our approach could better learn global information of code and shift attention between important statements during summary generation. With the help of hierarchical attention, the models are able to locate keywords more accurately in a top-down way. Ensemble learning is also proved to be an effective way to benefit from multiple input sources. © 2021
Author keywords: Code summarization; Deep learning; Hierarchical attention; Program comprehension
Index keywords: C (programming language); Deep learning; Signal encoding; Code representation; Code summarization; Deep learning; Ensemble learning; Hierarchical attention; Language description; Natural languages; Program comprehension; Research areas; Source codes; Decoding
Document type: Article
Conference: 
Source title: Information and Software Technology
Year: 2022
EID: 2-s2.0-85120352832
DOI: 10.1016/j.infsof.2021.106761
Retrieval channels: authoritative_outlet_search
Local full-text files: 

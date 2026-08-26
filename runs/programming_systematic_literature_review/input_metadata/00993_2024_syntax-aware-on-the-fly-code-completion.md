---
otero_id: "2-s2.0-85173617180"
title: "Syntax-aware on-the-fly code completion"
authors: "Takerngsaksiri W.; Tantithamthavorn C.; Li Y.-F."
year: "2024"
journal: "Information and Software Technology"
doi: "10.1016/j.infsof.2023.107336"
---
# Scopus title-abstract-keyword metadata
Title: Syntax-aware on-the-fly code completion
Abstract: Context: Code completion aims to help improve developers’ productivity by suggesting the next code tokens from a given context. Various approaches have been proposed to incorporate abstract syntax tree (AST) information for model training, ensuring that code completion is aware of the syntax of the programming languages. However, existing syntax-aware code completion approaches are not on-the-fly, as we found that for every two-thirds of characters that developers type, AST fails to be extracted because it requires the syntactically correct source code, limiting its practicality in real-world scenarios. On the other hand, existing on-the-fly code completion does not consider syntactic information yet. Objective: In this paper, we propose PyCoder to leverage token types, a kind of lightweight syntactic information, which is readily available and aligns with the natural order of source code. Method: Our PyCoder is trained in a multi-task training manner so that by learning the supporting task of predicting token types during the training phase, the models achieve better performance on predicting tokens and lines of code without the need for token types in the inference phase. Results: Comprehensive experiments show that PyCoder achieves the first rank on the CodeXGLUE leaderboard with an accuracy of 77.12% for the token-level predictions, which is 0.43%–24.25% more accurate than baselines. In addition, PyCoder achieves an exact match of 43.37% for the line-level predictions, which is 3.63%–84.73% more accurate than baselines. Conclusions: These results lead us to conclude that token type information (an alternative to syntactic information) that is rarely used in the past can greatly improve the performance of code completion approaches, without requiring the syntactically correct source code like AST-based approaches do. Our PyCoder is publicly available on HuggingFace and GitHub. © 2023 The Author(s)
Author keywords: Code completion; Multi-task learning
Index keywords: Codes (symbols); Computer programming languages; Learning systems; Syntactics; Trees (mathematics); Abstract Syntax Trees; Code completions; Model training; Multi tasks; Multitask learning; Performance; Real-world scenario; Source codes; Syntactic information; Task trainings; Forecasting
Document type: Article
Conference: 
Source title: Information and Software Technology
Year: 2024
EID: 2-s2.0-85173617180
DOI: 10.1016/j.infsof.2023.107336
Retrieval channels: authoritative_outlet_search
Local full-text files: 

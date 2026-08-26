---
otero_id: "2-s2.0-85174698076"
title: "An Accurate Identifier Renaming Prediction and Suggestion Approach"
authors: "Zhang J.; Luo J.; Liang J.; Gong L.; Huang Z."
year: "2023"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3603109"
---
# Scopus title-abstract-keyword metadata
Title: An Accurate Identifier Renaming Prediction and Suggestion Approach
Abstract: Identifiers play an important role in helping developers analyze and comprehend source code. However, many identifiers exist that are inconsistent with the corresponding code conventions or semantic functions, leading to flawed identifiers. Hence, identifiers need to be renamed regularly. Even though researchers have proposed several approaches to identify identifiers that need renaming and further suggest correct identifiers for them, these approaches only focus on a single or a limited number of granularities of identifiers without universally considering all the granularities and suggest a series of sub-tokens for composing identifiers without completely generating new identifiers. In this article, we propose a novel identifier renaming prediction and suggestion approach. Specifically, given a set of training source code, we first extract all the identifiers in multiple granularities. Then, we design and extract five groups of features from identifiers to capture inherent properties of identifiers themselves and the relationships between identifiers and code conventions, as well as other related code entities, enclosing files, and change history. By parsing the change history of identifiers, we can figure out whether specific identifiers have been renamed or not. These identifier features and their renaming history are used to train a Random Forest classifier, which can be further used to predict whether a given new identifier needs to be renamed or not. Subsequently, for the identifiers that need renaming, we extract all the related code entities and their renaming change history. Based on the intuition that identifiers are co-evolved as their relevant code entities with similar patterns and renaming sequences, we could suggest and recommend a series of new identifiers for those identifiers. We conduct extensive experiments to validate our approach in both the Java projects and the Android projects. Experimental results demonstrate that our approach could identify identifiers that need renaming with an average F-measure of more than 89%, which outperforms the state-of-the-art approach by 8.30% in the Java projects and 21.38% in the Android projects. In addition, our approach achieves a Hit@10 of 48.58% and 40.97% in the Java and Android projects in suggesting correct identifiers and outperforms the state-of-the-art approach by 29.62% and 15.75%, respectively. © 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: Additional Key Words and PhrasesIdentifier renaming; code refactoring; mining code repository; source code analysis
Index keywords: Android (operating system); Java programming language; Semantics; Additional key word and phrasesidentifier renaming; Change history; Code conventions; Code re-factoring; Key words; Mining code repository; Mining codes; Source code analysis; Source codes; State-of-the-art approach; Forecasting
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2023
EID: 2-s2.0-85174698076
DOI: 10.1145/3603109
Retrieval channels: authoritative_outlet_search
Local full-text files: 

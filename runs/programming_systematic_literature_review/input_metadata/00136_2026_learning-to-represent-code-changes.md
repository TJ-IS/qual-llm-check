---
otero_id: "2-s2.0-105025197401"
title: "Learning to represent code changes"
authors: "Tang X.; Tian H.; Pian W.; Ezzini S.; Kaboré A.K.; Habib A.; Kim K.; Klein J.; Bissyandé T.F."
year: "2026"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-025-10763-6"
---
# Scopus title-abstract-keyword metadata
Title: Learning to represent code changes
Abstract: Code change representation plays a pivotal role in automating numerous software engineering tasks, such as classifying code change correctness or generating natural language summaries of code changes. Recent studies have leveraged deep learning to derive effective code change representation, primarily focusing on capturing changes in token sequences or Abstract Syntax Trees (ASTs). However, these current state-of-the-art representations do not explicitly calculate the intention semantic induced by the change on the AST, nor do they effectively explore the surrounding contextual information of the modified lines. To address this, we propose a new code change representation methodology, Patcherizer, which we refer to as our tool. This innovative approach explores the intention features of the context and structure, combining the context around the code change along with two novel representations. These new representations capture the sequence intention inside the code changes in the code change and the graph intention inside the structural changes of AST graphs before and after the code change. This comprehensive representation allows us to better capture the intentions underlying a code change. Patcherizer builds on graph convolutional neural networks for the structural input representation of the intention graph and on transformers for the intention sequence representation. We assess the generalizability of Patcherizer ’s learned embeddings on three tasks: (1) Generating code change description in NL, (2) Predicting code change correctness in program repair, and (3) Code change intention detection. Experimental results show that the learned code change representation is effective for all three tasks and achieves superior performance to the state-of-the-art (SOTA) approaches. For instance, on the popular task of code change description generation (a.k.a. commit message generation), Patcherizer achieves an average improvement of 19.39%, 8.71%, and 34.03% in terms of BLEU, ROUGE-L, and METEOR metrics, respectively. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025.
Author keywords: Code change correctness; Code change representation; Message generation
Index keywords: Codes (symbols); Computer programming languages; Deep learning; Graph embeddings; Graph neural networks; Natural language processing systems; Software engineering; 'current; Abstract Syntax Trees; Code change correctness; Code change representation; Code changes; Engineering tasks; Message generation; Natural languages; Token sequences; Semantics
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2026
EID: 2-s2.0-105025197401
DOI: 10.1007/s10664-025-10763-6
Retrieval channels: authoritative_outlet_search
Local full-text files: 

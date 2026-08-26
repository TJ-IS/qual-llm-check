---
otero_id: "2-s2.0-105028009361"
title: "Prompt-Based Code Completion via Multi-Retrieval Augmented Generation"
authors: "Tan H.; Luo Q.; Jiang L.; Zhan Z.; Li J.; Zhang H.; Zhang Y."
year: "2025"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3725812"
---
# Scopus title-abstract-keyword metadata
Title: Prompt-Based Code Completion via Multi-Retrieval Augmented Generation
Abstract: Automated code completion, aiming at generating subsequent tokens from unfinished code, has significantly benefited from recent progress in pre-trained Large Language Models (LLMs). However, these models often suffer from coherence issues and hallucinations when dealing with complex code logic or extrapolating beyond their training data. Existing Retrieval Augmented Generation (RAG) techniques partially address these issues by retrieving relevant code with a separate encoding model where the retrieved snippet serves as contextual reference for code completion. However, their retrieval scope is subject to a singular perspective defined by the encoding model, which largely overlooks the complexity and diversity inherent in code semantics. To address this limitation, we propose ProCC, a code completion framework leveraging prompt engineering and the contextual multi-armed bandits algorithm to flexibly incorporate and adapt to multiple perspectives of code. ProCC first employs a prompt-based multi-retriever system which crafts prompt templates to elicit LLM knowledge to understand code semantics with multiple retrieval perspectives. Then, it adopts the adaptive retrieval selection algorithm to incorporate code similarity into the decision-making process to determine the most suitable retrieval perspective for the LLM to complete the code. Experimental results demonstrate that ProCC outperforms a widely studied code completion technique RepoCoder by 7.92% on the public benchmark CCEval, 3.19% in HumanEval-Infilling, 2.80% on our collected open-source benchmark suite, and 4.48% on the private-domain benchmark suite collected from Kuaishou Technology in terms of Exact Match. ProCC also allows augmenting fine-tuned techniques in a plug-and-play manner, yielding an averaged 6.5% improvement over the fine-tuned model. © 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: Code Completion; Multi-Retriever; Prompting
Index keywords: Artificial intelligence; Decision making; Information retrieval; Open systems; Optimal systems; Semantics; Automated code; Benchmark suites; Code completions; Code semantics; Complex codes; Encoding models; Language model; Multi-retriever; Prompting; Recent progress; Encoding (symbols); Signal encoding
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2025
EID: 2-s2.0-105028009361
DOI: 10.1145/3725812
Retrieval channels: authoritative_outlet_search
Local full-text files: 

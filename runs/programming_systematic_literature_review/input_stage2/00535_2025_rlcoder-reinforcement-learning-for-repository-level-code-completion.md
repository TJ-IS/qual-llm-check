---
otero_id: "2-s2.0-105010319161"
title: "RLCoder: Reinforcement Learning for Repository-Level Code Completion"
authors: "Wang Y.; Wang Y.; Guo D.; Chen J.; Zhang R.; Ma Y.; Zheng Z."
year: "2025"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse55347.2025.00014"
---
# Scopus title-abstract-keyword metadata
Title: RLCoder: Reinforcement Learning for Repository-Level Code Completion
Abstract: Repository-level code completion aims to generate code for unfinished code snippets within the context of a specified repository. Existing approaches mainly rely on retrievalaugmented generation strategies due to limitations in input sequence length. However, traditional lexical-based retrieval methods like BM25 struggle to capture code semantics, while model-based retrieval methods face challenges due to the lack of labeled data for training. Therefore, we propose RLCoder, a novel reinforcement learning framework, which can enable the retriever to learn to retrieve useful content for code completion without the need for labeled data. Specifically, we iteratively evaluate the usefulness of retrieved content based on the perplexity of the target code when provided with the retrieved content as additional context, and provide feedback to update the retriever parameters. This iterative process enables the retriever to learn from its successes and failures, gradually improving its ability to retrieve relevant and high-quality content. Considering that not all situations require information beyond code files and not all retrieved context is helpful for generation, we also introduce a stop signal mechanism, allowing the retriever to decide when to retrieve and which candidates to retain autonomously. Extensive experimental results demonstrate that RLCoder consistently outperforms state-of-the-art methods on CrossCodeEval and RepoEval, achieving 12.2% EM improvement over previous methods. Moreover, experiments show that our framework can generalize across different programming languages and further improve previous methods like RepoCoder. We provide the code and data at https://github.com/DeepSoftwareAnalytics/RLCoder.  © 2025 IEEE.
Author keywords: Perplexity; Reinforcement Learning; Repository-Level Code Completion; Stop Signal Mechanism
Index keywords: Codes (symbols); Computer programming languages; Iterative methods; Labeled data; Semantics; Signal processing; Code completions; Input sequence; Labeled data; Learn+; Perplexity; Reinforcement learnings; Repository-level code completion; Retrieval methods; Sequence lengths; Stop signal mechanism; Reinforcement learning
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2025
EID: 2-s2.0-105010319161
DOI: 10.1109/icse55347.2025.00014
Retrieval channels: authoritative_outlet_search
Local full-text files: 

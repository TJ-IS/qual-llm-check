---
otero_id: "2-s2.0-85179799829"
title: "TRACED: Execution-aware Pre-training for Source Code"
authors: "Ding Y.; Kaiser G.; Steenhoek B.; Le W.; Pei K.; Ray B."
year: "2024"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3597503.3608140"
---
# Scopus title-abstract-keyword metadata
Title: TRACED: Execution-aware Pre-training for Source Code
Abstract: Most existing pre-trained language models for source code focus on learning the static code text, typically augmented with static code structures (abstract syntax tree, dependency graphs, etc.). However, program semantics will not be fully exposed before the real execution. Without an understanding of the program execution, statically pre-trained models fail to comprehensively capture the dynamic code properties, such as the branch coverage and the runtime variable values, and they are consequently less effective at code understanding tasks, such as retrieving semantic clones and detecting software vulnerabilities. To close the gap between the static nature of language models and the dynamic characteristics of programs, we introduce TRACED, an execution-aware pre-training strategy for source code. Specifically, we pre-train code language models with a combination of source code, executable inputs, and corresponding execution traces. Our goal is to teach code models the complicated execution logic during the pre-training, enabling the model to statically estimate the dynamic code properties without repeatedly executing code during task-specific fine-tuning. To illustrate the effectiveness of our proposed approach, we fine-tune and evaluate TRACED on three downstream tasks: static execution estimation, clone retrieval, and vulnerability detection. The empirical results show that TRACED relatively improves the statically pre-trained code models by 12.4% for complete execution path prediction and by 25.2% for runtime variable value predictions. TRACED also significantly outperforms statically pre-trained models in clone retrieval and vulnerability detection across four public benchmarks. © 2024 IEEE Computer Society. All rights reserved.
Author keywords: 
Index keywords: Abstracting; Cloning; Computational linguistics; Computer programming languages; Trees (mathematics); Abstract Syntax Trees; Code structure; Dependency graphs; Language model; Pre-training; Property; Runtimes; Source codes; Static codes; Vulnerability detection; Semantics
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2024
EID: 2-s2.0-85179799829
DOI: 10.1145/3597503.3608140
Retrieval channels: authoritative_outlet_search
Local full-text files: 

---
otero_id: "2-s2.0-85056808981"
title: "Perses: Syntax-Guided Program Reduction"
authors: "Sun C.; Li Y.; Zhang Q.; Gu T.; Su Z."
year: "2018"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3180155.3180236"
---
# Scopus title-abstract-keyword metadata
Title: Perses: Syntax-Guided Program Reduction
Abstract: Given a program P that exhibits a certain property ψ (e.g., a C program that crashes GCC when it is being compiled), the goal of program reduction is to minimize P to a smaller variant P that still exhibits the same property, i.e., ψ(P). Program reduction is important and widely demanded for testing and debugging. For example, all compiler/interpreter development projects need effective program reduction to minimize failure-inducing test programs to ease debugging. However, state-of-the-art program reduction techniques — notably Delta Debugging (DD), Hierarchical Delta Debugging (HDD), and C-Reduce — do not perform well in terms of speed (reduction time) and quality (size of reduced programs), or are highly customized for certain languages and thus lack generality. This paper presents Perses, a novel framework for effective, efficient, and general program reduction. The key insight is to exploit, in a general manner, the formal syntax of the programs under reduction and ensure that each reduction step considers only smaller, syntactically valid variants to avoid futile efforts on syntactically invalid variants. Our framework supports not only deletion (as for DD and HDD), but also general, effective program transformations. We have designed and implemented Perses, and evaluated it for two language settings: C and Java. Our evaluation results on 20 C programs triggering bugs in GCC and Clang demonstrate Perses’s strong practicality compared to the state-of-the-art: (1) smaller size — Perses’s results are respectively 2% and 45% in size of those from DD and HDD; and (2) shorter reduction time — Perses takes 23% and 47% time taken by DD and HDD respectively. Even when compared to the highly customized and optimized C-Reduce for C/C++, Perses takes only 38-60% reduction time. © 2018 Association for Computing Machinery.
Author keywords: debugging; delta debugging; program reduction
Index keywords: C++ (programming language); Program debugging; Software testing; Syntactics; % reductions; C programs; Debugging; Delta debugging; Effective programs; Program reduction; Property; Reduction time; State of the art; Testing and debugging; Program compilers
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2018
EID: 2-s2.0-85056808981
DOI: 10.1145/3180155.3180236
Retrieval channels: authoritative_outlet_search
Local full-text files: 

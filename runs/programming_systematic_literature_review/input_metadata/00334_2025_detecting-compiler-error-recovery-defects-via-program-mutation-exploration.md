---
otero_id: "2-s2.0-85212291239"
title: "Detecting Compiler Error Recovery Defects via Program Mutation Exploration"
authors: "Tang Y.; Zhang J.; Li X.; Huang Z.; Jiang H."
year: "2025"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2024.3510912"
---
# Scopus title-abstract-keyword metadata
Title: Detecting Compiler Error Recovery Defects via Program Mutation Exploration
Abstract: Compiler error recovery diagnostics facilitates software development as it provides the possible causes and suggestions on potential programming errors. However, due to compiler bugs, error recovery diagnostics could be erroneous, spurious, missing, or even crashing for mature production compilers like GCC and Clang. Compiler testing is one of the most widely used ways of ensuring its quality. However, existing compiler diagnostics testing approaches (e.g., DIPROM) only consider the typically syntactically valid test programs as inputs, which are unlikely to trigger compiler error recovery defects. Therefore, in this paper, we propose the first mutation based approach for Compiler Error Recovery diagnostics Testing, called CERTest. Specifically, CERTest first explores the mutation space for a given seed program, and leverages a series of mutation configurations (which are referred as a series of mutators applying for a seed) to iteratively mutate the structures of the seed, so as to generate error-sensitive program variants for triggering compiler error recovery mechanisms. To effectively construct error-sensitive structures, CERTest then applies a novel furthest-first based selection approach to select a set of representative mutation configurations to generate program variants in each iteration. With the generated program variants, CERTest finally leverages differential testing to detect error recovery defects in different compilers. The experiments on GCC and Clang demonstrate that CERTest outperforms five state-of-the-art approaches (i.e., DIPROM, Ccoft, Clang-fuzzer, AFL++, and HiCOND) by up to 13.10%∼221.61% on average in the term of bug-finding capability, and CERTest detects 9 new error recovery defects, 5 of which have been confirmed or fixed by developers.  © 1976-2012 IEEE.
Author keywords: Compiler testing; differential testing; program mutation; test program generation
Index keywords: Computer debugging; Computer software selection and evaluation; Program compilers; Program debugging; Radiation hardening; Compiler testing; Diagnostic testing; Differential testing; Error-recovery; On potentials; Program generation; Program mutation; Programming errors; Test program generation; Test projects; Software testing
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2025
EID: 2-s2.0-85212291239
DOI: 10.1109/tse.2024.3510912
Retrieval channels: authoritative_outlet_search
Local full-text files: 

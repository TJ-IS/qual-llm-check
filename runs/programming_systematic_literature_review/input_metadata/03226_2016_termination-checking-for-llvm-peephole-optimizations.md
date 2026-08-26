---
otero_id: "2-s2.0-84971493149"
title: "Termination-checking for LLVM peephole optimizations"
authors: "Menendez D.; Nagarakatte S."
year: "2016"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/2884781.2884809"
---
# Scopus title-abstract-keyword metadata
Title: Termination-checking for LLVM peephole optimizations
Abstract: Mainstream compilers contain a large number of peephole optimizations, which perform algebraic simplification of the input program with local rewriting of the code. These optimizations are a persistent source of bugs. Our recent research on Alive, a domainspecific language for expressing peephole optimizations in LLVM, addresses a part of the problem by automatically verifying the correctness of these optimizations and generating C++ code for use with LLVM. This paper identifies a class of non-termination bugs that arise when a suite of peephole optimizations is executed until a fixed point. An optimization can undo the effect of another optimization in the suite, which results in non-terminating compilation. This paper (1) proposes a methodology to detect non-termination bugs with a suite of peephole optimizations, (2) identifies the necessary condition to ensure termination while composing peephole optimizations, and (3) provides debugging support by generating concrete input programs that cause non-terminating compilation. We have discovered 184 optimization sequences, involving 38 optimizations, that cause non-terminating compilation in LLVM with Alive-generated C++ code. © 2016 ACM.
Author keywords: Alive; Compiler Verification; Peephole Optimization; Termination
Index keywords: Codes (symbols); Program compilers; Program debugging; Software engineering; Algebraic simplification; Alive; Compiler verifications; Debugging support; Domain specific languages; Non terminations; Recent researches; Termination; C++ (programming language)
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2016
EID: 2-s2.0-84971493149
DOI: 10.1145/2884781.2884809
Retrieval channels: authoritative_outlet_search
Local full-text files: 

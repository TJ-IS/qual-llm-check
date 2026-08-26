---
otero_id: "2-s2.0-85171731475"
title: "Compiling Parallel Symbolic Execution with Continuations"
authors: "Wei G.; Jia S.; Gao R.; Deng H.; Tan S.; Bracevac O.; Rompf T."
year: "2023"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse48619.2023.00116"
---
# Scopus title-abstract-keyword metadata
Title: Compiling Parallel Symbolic Execution with Continuations
Abstract: Symbolic execution is a powerful program analysis and testing technique. Symbolic execution engines are usually implemented as interpreters, and the induced interpretation over-head can dramatically inhibit performance. Alternatively, implementation choices based on instrumentation provide a limited ability to transform programs. However, the use of compilation and code generation techniques beyond simple instrumentation remains underexplored for engine construction, leaving potential performance gains untapped. In this paper, we show how to tap some of these gains using sophisticated compilation techniques: We present Gensym, an optimizing symbolic-execution compiler that generates symbolic code which explores paths and generates tests in parallel. The key insight of GensYmis to compile symbolic execution tasks into cooperative concurrency via continuation-passing style, which further enables efficient parallelism. The design and implementation of Gensym is based on partial evaluation and generative programming techniques, which make it high-level and performant at the same time. We compare the performance of Gensym against the prior symbolic-execution compiler LLSC and the state-of-the-art symbolic interpreter KLEE. The results show an average 4.6× speedup for sequential execution and 9.4× speedup for parallel execution on 20 benchmark programs. © 2023 IEEE.
Author keywords: code generation; compiler; continuation; metaprogramming; symbolic execution
Index keywords: Codes (symbols); Model checking; Program compilers; Software testing; Taps; Analysis and testing; Analysis techniques; Codegeneration; Compiler; Continuation; Meta Programming; Performance; Program analysis; Program testing; Symbolic execution; Engines
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2023
EID: 2-s2.0-85171731475
DOI: 10.1109/icse48619.2023.00116
Retrieval channels: authoritative_outlet_search
Local full-text files: 

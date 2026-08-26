---
otero_id: "2-s2.0-85094324658"
title: "Pipelining bottom-up data flow analysis"
authors: "Shi Q.; Zhang C."
year: "2020"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3377811.3380425"
---
# Scopus title-abstract-keyword metadata
Title: Pipelining bottom-up data flow analysis
Abstract: Bottom-up program analysis has been traditionally easy to parallelize because functions without caller-callee relations can be analyzed independently. However, such function-level parallelism is significantly limited by the calling dependence - functions with caller-callee relations have to be analyzed sequentially because the analysis of a function depends on the analysis results, a.k.a., function summaries, of its callees.We observe that the calling dependence can be relaxed in many cases and, as a result, the parallelism can be improved. In this paper, we present Coyote, a framework of bottom-up data flow analysis, in which the analysis task of each function is elaborately partitioned into multiple sub-tasks to generate pipelineable function summaries. These sub-tasks are pipelined and run in parallel, even though the calling dependence exists. We formalize our idea under the IFDS/IDE framework and have implemented an application to checking null-dereference bugs and taint issues in C/C++ programs. We evaluate Coyote on a series of standard benchmark programs and open-source software systems, which demonstrates significant speedup over a conventional parallel design.  © 2020 Association for Computing Machinery.
Author keywords: Bottomup analysis; Compositional program analysis; Data flow analysis; Ifds/ide.; Modular program analysis
Index keywords: Application programs; C++ (programming language); Data transfer; Open source software; Open systems; Pipelines; Program debugging; Benchmark programs; Bottom up; C/C++ programs; Function summaries; Function-level parallelisms; Open source software systems; Parallel design; Program analysis; Data flow analysis
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2020
EID: 2-s2.0-85094324658
DOI: 10.1145/3377811.3380425
Retrieval channels: authoritative_outlet_search
Local full-text files: 

---
otero_id: "2-s2.0-85133546838"
title: "OJXPERF: Featherlight Object Replica Detection for Java Programs"
authors: "Li B.; Xu H.; Zhao Q.; Su P.; Chabbi M.; Jiao S.; Liu X."
year: "2022"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3510003.3510083"
---
# Scopus title-abstract-keyword metadata
Title: OJXPERF: Featherlight Object Replica Detection for Java Programs
Abstract: Memory bloat is an important source of inefficiency in complex production software, especially in software written in managed languages such as Java. Prior approaches to this problem have focused on identifying objects that outlive their life span. Few studies have, however, looked into whether and to what extent myriad objects of the same type are identical. A quantitative assessment of identical objects with code-level attribution can assist developers in refactoring code to eliminate object bloat, and favor reuse of existing object(s). The result is reduced memory pressure, reduced allocation and garbage collection, enhanced data locality, and reduced re-computation, all of which result in superior performance. We develop OJXPerf, a lightweight sampling-based profiler, which probabilistically identifies identical objects. OJXPerf employs hardware performance monitoring units (PMU) in conjunction with hardware debug registers to sample and compare field values of different objects of the same type allocated at the same calling context but potentially accessed at different program points. The result is a lightweight measurement - a combination of object allocation contexts and usage contexts ordered by duplication frequency. This class of duplicated objects is relatively easier to optimize. OJXPerf incurs 9% runtime and 6% memory overheads on average. We empirically show the benefit of OJXPerf by using its profiles to instruct us to optimize a number of Java programs, including well-known benchmarks and real-world applications. The results show a noticeable reduction in memory usage (up to 11%) and a significant speedup (up to 25%). © 2022 ACM.
Author keywords: 
Index keywords: Application programs; Codes (symbols); Java programming language; Object detection; Program debugging; Complex production; Java program; Lifespans; Memory bloats; Memory pressure; Production software; Quantitative assessments; Reduced memory; Refactorings; Reuse; Benchmarking
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2022
EID: 2-s2.0-85133546838
DOI: 10.1145/3510003.3510083
Retrieval channels: authoritative_outlet_search
Local full-text files: 

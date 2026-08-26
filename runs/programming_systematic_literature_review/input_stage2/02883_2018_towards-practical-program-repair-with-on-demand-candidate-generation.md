---
otero_id: "2-s2.0-85132005343"
title: "Towards Practical Program Repair with On-Demand Candidate Generation"
authors: "Hua J.; Zhang M.; Wang K.; Khurshid S."
year: "2018"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3180155.3180245"
---
# Scopus title-abstract-keyword metadata
Title: Towards Practical Program Repair with On-Demand Candidate Generation
Abstract: Effective program repair techniques, which modify faulty programs to fix them with respect to given test suites, can substantially reduce the cost of manual debugging. A common repair approach is to iteratively first generate candidate programs with possible bug fixes and then validate them against the given tests until a candidate that passes all the tests is found. While this approach is conceptually simple, due to the potentially high number of candidates that need to first be generated and then be compiled and tested, existing repair techniques that embody this approach have relatively low effectiveness, especially for faults at a fine granularity. To tackle this limitation, we introduce a novel repair technique, SketchFix, which generates candidate fixes on demand (as needed) during the test execution. Instead of iteratively re-compiling and re-executing each actual candidate program, SketchFix translates faulty programs to sketches, i.e., partial programs with “holes”, and compiles each sketch once which may represent thousands of concrete candidates. With the insight that the space of candidates can be reduced substantially by utilizing the runtime behaviors of the tests, SketchFix lazily initializes the candidates of the sketches while validating them against the test execution. We experimentally evaluate SketchFix on the Defects4J benchmark and the experimental results show that SketchFix works particularly well in repairing bugs with expression manipulation at the AST node-level granularity compared to other program repair techniques. Specifically, SketchFix correctly fixes 19 out of 357 defects in 23 minutes on average using the default setting. In addition, SketchFix finds the first repair with 1.6% of re-compilations (#compiled sketches/#candidates) and 3.0% of re-executions out of all repair candidates. © 2018 Association for Computing Machinery.
Author keywords: 
Index keywords: Defects; Iterative methods; Program debugging; Software testing; Testing; Bug fixes; Candidate generation; Effective programs; Fine granularity; On demands; Practical projects; Repair techniques; Runtime behaviors; Simple++; Test execution; Repair
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2018
EID: 2-s2.0-85132005343
DOI: 10.1145/3180155.3180245
Retrieval channels: authoritative_outlet_search
Local full-text files: 

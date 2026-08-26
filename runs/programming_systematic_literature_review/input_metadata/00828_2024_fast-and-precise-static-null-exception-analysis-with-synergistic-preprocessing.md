---
otero_id: "2-s2.0-85204977479"
title: "Fast and Precise Static Null Exception Analysis With Synergistic Preprocessing"
authors: "Sun Y.; Wang C.; Fan G.; Shi Q.; Zhang X."
year: "2024"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2024.3466551"
---
# Scopus title-abstract-keyword metadata
Title: Fast and Precise Static Null Exception Analysis With Synergistic Preprocessing
Abstract: Pointer operations are common in programs written in modern programming languages such as C/C++ and Java. While widely used, pointer operations often suffer from bugs like null pointer exceptions that make software systems vulnerable and unstable. However, precisely verifying the absence of null pointer exceptions is notoriously slow as we need to inspect a huge number of pointer-dereferencing operations one by one via expensive techniques like SMT solving. We observe that, among all pointer-dereferencing operations in a program, a large number can be proven to be safe by lightweight preprocessing. Thus, we can avoid employing costly techniques to verify their nullity. The impacts of lightweight preprocessing techniques are significantly less studied and ignored by recent works. In this paper, we propose a new technique, BONA, which leverages the synergistic effects of two classic preprocessing analyses. The synergistic effects between the two preprocessing analyses allow us to recognize a lot more safe pointer operations before a follow-up costly nullity verification, thus improving the scalability of the whole null exception analysis. We have implemented our synergistic preprocessing procedure in two state-of-the-art static analyzers, KLEE and Pinpoint. The evaluation results demonstrate that BONA itself is fast and can finish in a few seconds for programs that KLEE and Pinpoint may require several minutes or even hours to analyze. Compared to the vanilla versions of KLEE and Pinpoint, BONA respectively enables them to achieve up to 1.6x and 6.6x speedup (1.2x and 3.8x on average) with less than 0.5% overhead. Such a speedup is significant enough as it allows KLEE and Pinpoint to check more pointer-dereferencing operations in a given time budget and, thus, discover over a dozen previously unknown null pointer exceptions in open-source projects.  © 1976-2012 IEEE.
Author keywords: and path sensitivity; dataflow analysis; Null exception analysis; static analysis; symbolic execution
Index keywords: C++ (programming language); Data flow analysis; Java programming language; Open source software; Program debugging; Sensitivity analysis; Dataflow; Exception analysis; Follow up; Null exception analyze; Path sensitivity; Pre-processing techniques; Software-systems; Symbolic execution; Synergistic effect; Two-state; Budget control
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2024
EID: 2-s2.0-85204977479
DOI: 10.1109/tse.2024.3466551
Retrieval channels: authoritative_outlet_search
Local full-text files: 

---
otero_id: "2-s2.0-85164301111"
title: "SafeDrop: Detecting Memory Deallocation Bugs of Rust Programs via Static Data-flow Analysis"
authors: "Cui M.; Chen C.; Xu H.; Zhou Y."
year: "2023"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3542948"
---
# Scopus title-abstract-keyword metadata
Title: SafeDrop: Detecting Memory Deallocation Bugs of Rust Programs via Static Data-flow Analysis
Abstract: Rust is an emerging programming language that aims to prevent memory-safety bugs. However, the current design of Rust also brings side effects, which may increase the risk of memory-safety issues. In particular, it employs ownership-based resource management and enforces automatic deallocation of unused resources without using the garbage collector. It may therefore falsely deallocate reclaimed memory and lead to use-after-free or double-free issues. In this article, we study the problem of invalid memory deallocation and propose SafeDrop, a static path-sensitive data-flow analysis approach to detect such bugs. Our approach analyzes each function of a Rust crate iteratively in a flow-sensitive and field-sensitive way. It leverages a modified Tarjan algorithm to achieve scalable path-sensitive analysis and a cache-based strategy for efficient inter-procedural analysis. We have implemented our approach and integrated it into the Rust compiler. Experiment results show that the approach can successfully detect all such bugs in our experiments with a limited number of false positives and incurs a very small overhead compared to the original compilation time. © 2023 Association for Computing Machinery.
Author keywords: data-flow analysis; meet over path; path sensitivity; Rust
Index keywords: Data transfer; Iterative methods; Program debugging; Safety engineering; Sensitive data; 'current; Data-flow analysis; Meet over path; Memory de-allocation; Memory safety; Path sensitivity; Rust; Safety issues; Side effect; Static data-flow analysis; Data flow analysis
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2023
EID: 2-s2.0-85164301111
DOI: 10.1145/3542948
Retrieval channels: authoritative_outlet_search
Local full-text files: 

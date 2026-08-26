---
otero_id: "2-s2.0-33644653428"
title: "Runtime analysis of atomicity for multithreaded programs"
authors: "Liqiang W.; Stoller S.D."
year: "2006"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2006.1599419"
---
# Scopus title-abstract-keyword metadata
Title: Runtime analysis of atomicity for multithreaded programs
Abstract: Atomicity is a correctness condition for concurrent systems. Informally, atomicity is the property that every concurrent execution of a set of transactions is equivalent to some serial execution of the same transactions. In multithreaded programs, executions of procedures (or methods) can be regarded as transactions. Correctness in the presence of concurrency typically requires atomicity of these transactions. Tools that automatically detect atomicity violations can uncover subtle errors that are hard to find with traditional debugging and testing techniques. This paper describes two algorithms for runtime detection of atomicity violations and compares their cost and effectiveness. The reduction-based algorithm checks atomicity based on commutativity properties of events in a trace; the block-based algorithm efficiently represents the relevant information about a trace as a set of blocks (i.e., pairs of events plus associated synchronizations) and checks atomicity by comparing each block with other blocks. To improve the efficiency and accuracy of both algorithms, we incorporate a multilockset algorithm for checking data races, dynamic escape analysis, and happen-before analysis. Experiments show that both algorithms are effective in finding atomicity violations. The block-based algorithm is more accurate but more expensive than the reduction-based algorithm. © 2006 IEEE.
Author keywords: Atomicity; Concurrent programming; Data race; Java; Testing and debugging
Index keywords: Algorithms; Computer programming; Computer testing; Java programming language; Program debugging; Atomicity; Concurrent programming; Data race; Multithread programs; Runtime analysis; Software engineering
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2006
EID: 2-s2.0-33644653428
DOI: 10.1109/tse.2006.1599419
Retrieval channels: authoritative_outlet_search
Local full-text files: 

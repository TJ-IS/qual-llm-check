---
otero_id: "2-s2.0-85196779323"
title: "Constraint Based Program Repair for Persistent Memory Bugs"
authors: "Huang Z.; Wang C."
year: "2024"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3597503.3639204"
---
# Scopus title-abstract-keyword metadata
Title: Constraint Based Program Repair for Persistent Memory Bugs
Abstract: We propose a constraint based method for repairing bugs associated with the use of persistent memory (PM) in application software. Our method takes a program execution trace and the violated property as input and returns a suggested repair, which is a combination of inserting new PM instructions and reordering these instructions to eliminate the property violation. Compared with the state-of-the-art approach, our method has three advantages. First, it can repair both durability and crash consistency bugs whereas the state-of-the-art approach can only repair the relatively-simple durability bugs. Second, our method can discover new repair strategies instead of relying on repair strategies hard-coded into the repair tool. Third, our method uses a novel symbolic encoding to model PM semantics, which allows our symbolic analysis to be more efficient than the explicit enumeration of possible scenarios and thus explore a large number of repairs quickly. We have evaluated our method on benchmark programs from the well-known Intel PMDK library as well as real applications such as Memcached, Recipe, and Redis. The results show that our method can repair all of the 41 known bugs in these benchmarks, while the state-of-the-art approach cannot repair any of the crash consistency bugs.  © 2024 ACM.
Author keywords: debugging; Persistent memory; program repair; testing; verification
Index keywords: Application programs; Benchmarking; Durability; Program debugging; Repair; Software testing; Verification; Applications software; Constraint based method; Constraint-based; Debugging; Persistent memory; Program execution; Program repair; Property; Repair strategy; State-of-the-art approach; Semantics
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2024
EID: 2-s2.0-85196779323
DOI: 10.1145/3597503.3639204
Retrieval channels: authoritative_outlet_search
Local full-text files: 

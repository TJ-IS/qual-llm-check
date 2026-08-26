---
otero_id: "2-s2.0-57349194546"
title: "Scalable detection of semantic clones"
authors: "Gabel M.; Jiang L.; Su Z."
year: "2008"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/1368088.1368132"
---
# Scopus title-abstract-keyword metadata
Title: Scalable detection of semantic clones
Abstract: Several techniques have been developed for identifying similar code fragments in programs. These similar fragments, referred to as code clones, can be used to identify redundant code, locate bugs, or gain insight into program design. Existing scalable approaches to clone detection are limited to finding program fragments that are similar only in their contiguous syntax. Other, semantics-based approaches are more resilient to differences in syntax, such as reordered statements, related statements interleaved with other unrelated statements, or the use of semantically equivalent control structures. However, none of these techniques have scaled to real world code bases. These approaches capture semantic information from Program Dependence Graphs (PDGs), program representations that encode data and control dependencies between statements and predicates. Our definition of a code clone is also based on this representation: we consider program fragments with isomorphic PDGs to be clones. In this paper, we present the first scalable clone detection algorithm based on this definition of semantic clones. Our insight is the reduction of the difficult graph similarity problem to a simpler tree similarity problem by mapping carefully selected PDG subgraphs to their related structured syntax. We efficiently solve the tree similarity problem to create a scalable analysis. We have implemented this algorithm in a practical tool and performed evaluations on several million-line open source projects, including the Linux kernel. Compared with previous approaches, our tool locates significantly more clones, which are often more semantically interesting than simple copied and pasted code fragments. Copyright 2008 ACM.
Author keywords: Clone detection; Program dependence graph; Refactoring; Software maintenance
Index keywords: Cloning; Computer aided software engineering; Computer software maintenance; Graph theory; Information theory; Maintenance; Program debugging; Semantics; Software engineering; Syntactics; Trees (mathematics); Computer operating systems; Clone detection; Code clones; Code fragments; Equivalent controls; Gain insights; Graph similarities; Linux kernels; Open source projects; Program dependence graph; Program designs; Program fragments; Redundant codes; Refactoring; Scalable analysis; Scalable approaches; Semantic informations; Software maintenance; Sub-graphs; Code clone; Equivalent control; Gain insight; Graph similarity; Linux kernel; Program design; Real code; Scalable approach; Semantic information; Subgraphs; Concurrency control; Program debugging
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2008
EID: 2-s2.0-57349194546
DOI: 10.1145/1368088.1368132
Retrieval channels: authoritative_outlet_search
Local full-text files: 

---
otero_id: "2-s2.0-0037083635"
title: "An efficient dynamic program slicing technique"
authors: "Mund G.B.; Mall R.; Sarkar S."
year: "2002"
journal: "Information and Software Technology"
doi: "10.1016/s0950-5849(01)00224-5"
---
# Scopus title-abstract-keyword metadata
Title: An efficient dynamic program slicing technique
Abstract: An important application of the dynamic program slicing technique is program debugging. In applications such as interactive debugging, the dynamic slicing algorithm needs to be efficient. In this context, we propose a new dynamic program slicing technique that is more efficient than the related algorithms reported in the literature. We use the program dependence graph as an intermediate program representation, and modify it by introducing the concepts of stable and unstable edges. Our algorithm is based on marking and unmarking the unstable edges as and when the dependences arise and cease during run-time. We call this algorithm edge-marking algorithm. After an execution of a node x, an unstable edge (x, y) is marked if the node x uses the value of the variable defined at node y. A marked unstable edge (x, y) is unmarked after an execution of a node z if the nodes y and z define the same variable var, and the value of var computed at the node y does not affect the present value of var defined at the node z. We show that our algorithm is more time and space efficient than the existing ones. The worst case space complexity of our algorithm is O(n2), where n is the number of statements in the program. We also briefly discuss an implementation of our algorithm. © 2002 Elsevier Science B.V. All rights reserved.
Author keywords: Control flow graph; Dynamic slicing; Program debugging; Program dependence graph; Program slicing; Static slicing
Index keywords: Algorithms; Computational complexity; Dynamic programming; Graph theory; Program debugging; Program slicing; Software engineering
Document type: Article
Conference: 
Source title: Information and Software Technology
Year: 2002
EID: 2-s2.0-0037083635
DOI: 10.1016/s0950-5849(01)00224-5
Retrieval channels: authoritative_outlet_search
Local full-text files: 

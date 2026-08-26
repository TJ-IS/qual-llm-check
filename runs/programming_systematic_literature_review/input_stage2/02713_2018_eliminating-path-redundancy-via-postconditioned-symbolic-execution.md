---
otero_id: "2-s2.0-85040741550"
title: "Eliminating Path Redundancy via Postconditioned Symbolic Execution"
authors: "Yi Q.; Yang Z.; Guo S.; Wang C.; Liu J.; Zhao C."
year: "2018"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2017.2659751"
---
# Scopus title-abstract-keyword metadata
Title: Eliminating Path Redundancy via Postconditioned Symbolic Execution
Abstract: Symbolic execution is emerging as a powerful technique for generating test inputs systematically to achieve exhaustive path coverage of a bounded depth. However, its practical use is often limited by path explosion because the number of paths of a program can be exponential in the number of branch conditions encountered during the execution. To mitigate the path explosion problem, we propose a new redundancy removal method called postconditioned symbolic execution. At each branching location, in addition to determine whether a particular branch is feasible as in traditional symbolic execution, our approach checks whether the branch is subsumed by previous explorations. This is enabled by summarizing previously explored paths by weakest precondition computations. Postconditioned symbolic execution can identify path suffixes shared by multiple runs and eliminate them during test generation when they are redundant. Pruning away such redundant paths can lead to a potentially exponential reduction in the number of explored paths. Since the new approach is computationally expensive, we also propose several heuristics to reduce its cost. We have implemented our method in the symbolic execution engine KLEE [1] and conducted experiments on a large set of programs from the GNU Coreutils suite. Our results confirm that redundancy due to common path suffix is both abundant and widespread in real-world applications. © 1976-2012 IEEE.
Author keywords: Symbolic execution; testing and debugging; testing tools
Index keywords: Program debugging; Redundancy; Exponential reduction; Number of branches; Redundancy removal; Symbolic execution; Test generations; Testing and debugging; Testing tools; Weakest precondition; Model checking
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2018
EID: 2-s2.0-85040741550
DOI: 10.1109/tse.2017.2659751
Retrieval channels: authoritative_outlet_search
Local full-text files: 

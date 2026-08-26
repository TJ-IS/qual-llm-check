---
otero_id: "2-s2.0-85100861684"
title: "CTOS: Compiler Testing for Optimization Sequences of LLVM"
authors: "Jiang H.; Zhou Z.; Ren Z.; Zhang J.; Li X."
year: "2022"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2021.3058671"
---
# Scopus title-abstract-keyword metadata
Title: CTOS: Compiler Testing for Optimization Sequences of LLVM
Abstract: Optimization sequences are often employed in compilers to improve the performance of programs, but may trigger critical compiler bugs, e.g., compiler crashes. Although many methods have been developed to automatically test compilers, no systematic work has been conducted to detect compiler bugs when applying arbitrary optimization sequences. To resolve this problem, two main challenges need to be addressed, namely the acquisition of representative optimization sequences and the selection of representative testing programs, due to the enormous number of optimization sequences and testing programs. In this study, we propose CTOS, a novel compiler testing method based on differential testing, for detecting compiler bugs caused by optimization sequences of LLVM. CTOS first leverages the technique Doc2Vec to transform optimization sequences into vectors to capture the information of optimizations and their orders simultaneously. Second, a method based on the region graph and call relationships is developed in CTOS to construct the vector representations of the testing program, such that the semantics and the structure information of programs can be captured simultaneously. Then, with the vector representations of optimization sequences and testing programs, a 'centroid' based selection scheme is proposed to address the above two challenges. Finally, CTOS takes in the representative optimization sequences and testing programs as inputs, and tests each testing program with all the representative optimization sequences. If there is an output that is different from the majority of others of a given testing program, then the corresponding optimization sequence is deemed to trigger a compiler bug. Our evaluation demonstrates that CTOS significantly outperforms the baselines by up to 24.76\% ∼ 50.57%24.76 %∼50.57% in terms of the bug-finding capability on average. Within seven month evaluations on LLVM, we have reported 104 valid bugs within 5 types, of which 21 have been confirmed or fixed. Most of those bugs are crash bugs (57) and wrong code bugs (24). 47 unique optimizations are identified to be faulty and 15 of them are loop related optimizations.  © 1976-2012 IEEE.
Author keywords: Compiler testing; LLVM; Optimization sequences; Program representation; Software testing
Index keywords: Program debugging; Semantics; Software testing; Testing; Automatically test; Compiler testing; Differential testing; Representative testing; Selection scheme; Structure information; Testing programs; Vector representations; Program compilers
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2022
EID: 2-s2.0-85100861684
DOI: 10.1109/tse.2021.3058671
Retrieval channels: authoritative_outlet_search
Local full-text files: 

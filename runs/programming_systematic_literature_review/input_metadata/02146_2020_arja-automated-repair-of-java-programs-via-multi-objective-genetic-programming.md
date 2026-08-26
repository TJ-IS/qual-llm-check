---
otero_id: "2-s2.0-85054474502"
title: "ARJA: Automated Repair of Java Programs via Multi-Objective Genetic Programming"
authors: "Yuan Y.; Banzhaf W."
year: "2020"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2018.2874648"
---
# Scopus title-abstract-keyword metadata
Title: ARJA: Automated Repair of Java Programs via Multi-Objective Genetic Programming
Abstract: Automated program repair is the problem of automatically fixing bugs in programs in order to significantly reduce the debugging costs and improve the software quality. To address this problem, test-suite based repair techniques regard a given test suite as an oracle and modify the input buggy program to make the entire test suite pass. GenProg is well recognized as a prominent repair approach of this kind, which uses genetic programming (GP) to rearrange the statements already extant in the buggy program. However, recent empirical studies show that the performance of GenProg is not fully satisfactory, particularly for Java. In this paper, we propose ARJA, a new GP based repair approach for automated repair of Java programs. To be specific, we present a novel lower-granularity patch representation that properly decouples the search subspaces of likely-buggy locations, operation types and potential fix ingredients, enabling GP to explore the search space more effectively. Based on this new representation, we formulate automated program repair as a multi-objective search problem and use NSGA-II to look for simpler repairs. To reduce the computational effort and search space, we introduce a test filtering procedure that can speed up the fitness evaluation of GP and three types of rules that can be applied to avoid unnecessary manipulations of the code. Moreover, we also propose a type matching strategy that can create new potential fix ingredients by exploiting the syntactic patterns of existing statements. We conduct a large-scale empirical evaluation of ARJA along with its variants on both seeded bugs and real-world bugs in comparison with several state-of-the-art repair approaches. Our results verify the effectiveness and efficiency of the search mechanisms employed in ARJA and also show its superiority over the other approaches. In particular, compared to jGenProg (an implementation of GenProg for Java), an ARJA version fully following the redundancy assumption can generate a test-suite adequate patch for more than twice the number of bugs (from 27 to 59), and a correct patch for nearly four times of the number (from 5 to 18), on 224 real-world bugs considered in Defects4J. Furthermore, ARJA is able to correctly fix several real multi-location bugs that are hard to be repaired by most of the existing repair approaches. © 2018 IEEE.
Author keywords: genetic improvement; genetic programming; multi-objective optimization; patch generation; Program repair
Index keywords: Automation; Computer software maintenance; Computer software selection and evaluation; Genetic algorithms; Genetic programming; Java programming language; Program debugging; Repair; Software testing; Computer bugs; Genetic improvements; Java; Java program; Multi objective; Multi-objectives optimization; Patch generation; Program repair; Search problem; Search spaces; Multiobjective optimization
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2020
EID: 2-s2.0-85054474502
DOI: 10.1109/tse.2018.2874648
Retrieval channels: authoritative_outlet_search
Local full-text files: 

---
otero_id: "2-s2.0-85171738708"
title: "Identifying Key Classes for Initial Software Comprehension: Can We Do It Better?"
authors: "Pan W.; Du X.; Ming H.; Kim D.-K.; Yang Z."
year: "2023"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse48619.2023.00160"
---
# Scopus title-abstract-keyword metadata
Title: Identifying Key Classes for Initial Software Comprehension: Can We Do It Better?
Abstract: Key classes are excellent starting points for developers, especially newcomers, to comprehend an unknown software system. Though many unsupervised key class identification approaches have been proposed in the literature by representing software as class dependency networks (aka software networks) and using some network metrics (e.g., h-index, a-index, and coreness), they are never aware of the field where the nodes exist and the effect of the field on the importance of the nodes in it. According to the classic field theory in physics, every material particle is in a field through which they exert an impact on other particles in the field via non-contact interactions (e.g., electromagnetic force, gravity, and nuclear force). Similarly, every node in a software network might also exist in a field, which might affect the importance of class nodes in it. In this paper, we propose an approach, iFit, to identify key classes in object-oriented software systems. First, we represent software as a CSNWD (Weighted Directed Class-level Software Network) to capture the topological structure of software, including classes, their couplings, and the direction and strength of couplings. Second, we assume that the nodes in the CSNWD exist in a gravitation-like field and propose a new metric, CG (Cumulative Gravitation-like importance), to measure the importance of classes. CG is inspired by Newton's gravitational formula and uses the PageRank value computed by a biased-PageRank algorithm as the masses of classes. Finally, classes in the system are sorted in descending order according to their CG values, and a cutoff is utilized, that is, the top-ranked classes are recommended as key classes. The experiments were performed on a data set composed of six open-source Java systems from the literature. The results show that iFit is superior to the baseline approaches on 93.75% of the total cases, and is scalable to large-scale software systems. Besides, we find that iFit is neutral to the weighting mechanisms used to assign the weights for different coupling types in the CSNWD, that is, when applying iFit to identify key classes, we can use any one of the weighting mechanisms. © 2023 IEEE.
Author keywords: complex networks; field theory; key classes; PageRank; program comprehension
Index keywords: Couplings; Gravitation; Object oriented programming; Open source software; Open systems; Topology; Dependency networks; Field theory; Identification approach; Key class; Network metrics; Page ranks; Program comprehension; Software comprehension; Software network; Software-systems; Complex networks
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2023
EID: 2-s2.0-85171738708
DOI: 10.1109/icse48619.2023.00160
Retrieval channels: authoritative_outlet_search
Local full-text files: 

---
otero_id: "2-s2.0-85150451924"
title: "An annotation-based approach for finding bugs in neural network programs"
authors: "Rezaalipour M.; Furia C.A."
year: "2023"
journal: "Journal of Systems and Software"
doi: "10.1016/j.jss.2023.111669"
---
# Scopus title-abstract-keyword metadata
Title: An annotation-based approach for finding bugs in neural network programs
Abstract: As neural networks are increasingly included as core components of safety–critical systems, developing effective testing techniques specialized for them becomes crucial. The bulk of the research has focused on testing neural-network models; but these models are defined by writing programs, and there is growing evidence that these neural-network programs often have bugs too. This paper presents ANNOTEST: an approach to generating test inputs for neural-network programs. A fundamental challenge is that the dynamically-typed languages (e.g., Python) commonly used to program neural networks cannot express detailed constraints about valid function inputs (e.g., matrices with certain dimensions). Without knowing these constraints, automated test-case generation is prone to producing invalid inputs, which trigger spurious failures and are useless for identifying real bugs. To address this problem, we introduce a simple annotation language tailored for concisely expressing valid function inputs in neural-network programs. ANNOTEST takes as input an annotated program, and uses property-based testing to generate random inputs that satisfy the validity constraints. In the paper, we also outline guidelines that simplify writing ANNOTEST annotations. We evaluated ANNOTEST on 19 neural-network programs from Islam et al's survey. Islam et al. (2019), which we manually annotated following our guidelines — producing 6 annotations per tested function on average. ANNOTEST automatically generated test inputs that revealed 94 bugs, including 63 bugs that the survey reported for these projects. These results suggest that ANNOTEST can be a valuable approach to finding widespread bugs in real-world neural-network programs. © 2023 The Author(s)
Author keywords: Debugging; Neural networks; Python; Test generation
Index keywords: Program debugging; Safety testing; Software testing; Core components; Debugging; Effective testing; Neural network model; Neural-networks; Safety critical systems; Test generations; Test inputs; Testing technique; Writing projects; Python
Document type: Article
Conference: 
Source title: Journal of Systems and Software
Year: 2023
EID: 2-s2.0-85150451924
DOI: 10.1016/j.jss.2023.111669
Retrieval channels: authoritative_outlet_search
Local full-text files: 

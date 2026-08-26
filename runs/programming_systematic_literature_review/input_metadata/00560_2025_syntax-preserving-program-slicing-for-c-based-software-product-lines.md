---
otero_id: "2-s2.0-85206822334"
title: "Syntax-preserving program slicing for C-based software product lines"
authors: "Gerling L."
year: "2025"
journal: "Journal of Systems and Software"
doi: "10.1016/j.jss.2024.112255"
---
# Scopus title-abstract-keyword metadata
Title: Syntax-preserving program slicing for C-based software product lines
Abstract: Program slicing is a well-established technique for identifying a reduced subset of a program based on pre-defined criteria, leading to complexity reduction in subsequent activities. Despite extensive study over the past 40 years, slicing techniques for software product lines (SPLs) remain notably scarce. The absence of dedicated SPL slicing approaches hinders their efficient analysis and maintenance, limiting the ability to focus only on relevant parts of the SPL. One reason for this deficiency is the complex nature of a common variability implementation: the use of C preprocessor #ifdef-annotations within C code. A slicing approach for C-based SPLs must address the intricate interplay between the C code and the functionality introduced by the C preprocessor. Effectively handling these intricacies will unleash the full potential of SPL analysis. In this paper, we present a novel syntax-preserving program slicing approach for C-based SPLs. Unlike existing methods, our approach enables the computation of program slices through an integrated analysis of both C and CPP code, while preserving the original program syntax (no element of its syntax is disregarded or changed). This preservation ensures that the resulting program slices remain authentic subsets of the SPL, making them suitable inputs for variability-aware analyses. Additionally, we demonstrate the practical applicability of these slices in the context of software transplantation, showcasing their potential for facilitating functionality transfer between different program versions. In contrast to existing transplantation approaches, our solution works without test cases, removing the need for product configuration and execution. Consequently, the variability implementation (along with all other contained preprocessor code) is preserved during the transplantation. We empirically evaluate our approach on four distinct open-source SPLs, showcasing its effectiveness in generating diverse program slices tailored to different slicing criteria. We asses the accuracy of our code representation, the time required for slicing and transplantation, the size reduction achieved through the slices, and the functionality of our variability-aware transplantation approach. © 2024 The Author
Author keywords: C preprocessor; Program slicing; Software product lines; Software transplantation; Static analysis
Index keywords: Computer software maintenance; Computer software selection and evaluation; Open source software; Program debugging; Software testing; Static analysis; Syntactics; C preprocessor; C++ codes; Complexity reduction; Program slicers; Program slicing; Software Product Line; Software transplantation; Syntax-preserving; Variability-Aware; Well-established techniques; C (programming language)
Document type: Article
Conference: 
Source title: Journal of Systems and Software
Year: 2025
EID: 2-s2.0-85206822334
DOI: 10.1016/j.jss.2024.112255
Retrieval channels: authoritative_outlet_search
Local full-text files: 

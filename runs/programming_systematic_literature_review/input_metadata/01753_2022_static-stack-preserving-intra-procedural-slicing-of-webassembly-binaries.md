---
otero_id: "2-s2.0-85133496958"
title: "Static Stack-Preserving Intra-Procedural Slicing of WebAssembly Binaries"
authors: "Stievenart Q.; Binkley D.W.; De Roover C."
year: "2022"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3510003.3510070"
---
# Scopus title-abstract-keyword metadata
Title: Static Stack-Preserving Intra-Procedural Slicing of WebAssembly Binaries
Abstract: The recently introduced WebAssembly standard aims to be a portable compilation target, enabling the cross-platform distribution of pro-grams written in a variety of languages. We propose an approach to slice WebAssembly programs in order to enable applications in reverse engineering, code comprehension, and security among others. Given a program and a location in that program, program slicing produces a minimal version of the program that preserves the behavior at the given location. Specifically, our approach is a static, intra-procedural, backward slicing approach that takes into account WebAssembly-specific dependences to identify the instructions of the slice. To do so it must correctly overcome the considerable challenges of performing dependence analysis at the bi-nary level. Furthermore, for the slice to be executable, the approach needs to ensure that the stack behavior of its output complies with WebAssembly's validation requirements. We implemented and eval-uated our approach on a suite of 8 386 real-world WebAssembly binaries, finding that the average size of the 495 204 868 slices computed is 53% of the original code, an improvement over the 60% attained by related work slicing ARM binaries. To gain a more qual-itative understanding of the slices produced by our approach, we compared them to 1 956 source-level slices of benchmark C pro-grams. This inspection helps to illustrate the slicer's strengths and to uncover potential future improvements. © 2022 ACM.
Author keywords: Binary analysis; Static program slicing; WebAssembly
Index keywords: C (programming language); Codes (symbols); Reverse engineering; Backward slicing; Binary analysis; Code comprehension; Code security; Cross-platform; Engineering codes; Program slicing; Static program; Static program slicing; Webassembly; Application programs
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2022
EID: 2-s2.0-85133496958
DOI: 10.1145/3510003.3510070
Retrieval channels: authoritative_outlet_search
Local full-text files: 

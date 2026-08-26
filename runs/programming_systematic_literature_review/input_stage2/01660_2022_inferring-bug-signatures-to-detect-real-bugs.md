---
otero_id: "2-s2.0-85125488043"
title: "Inferring Bug Signatures to Detect Real Bugs"
authors: "Zhong H.; Wang X.; Mei H."
year: "2022"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2020.2996975"
---
# Scopus title-abstract-keyword metadata
Title: Inferring Bug Signatures to Detect Real Bugs
Abstract: Static tools like Findbugs allow their users to manually define bug patterns, so they can detect more types of bugs, but due to the complexity and variety of programs, it is difficult to manually enumerate all bug patterns, especially for those related to API usages or project-specific rules. Therefore, existing bug-detection tools (e.g., Findbugs) based on manual bug patterns are insufficient in detecting many bugs. Meanwhile, with the rapid development of software, many past bug fixes accumulate in software version histories. These bug fixes contain valuable samples of illegal coding practices. The gap between existing bug samples and well-defined bug patterns motivates our research. In the literature, researchers have explored techniques on learning bug signatures from existing bugs, and a bug signature is defined as a set of program elements explaining the cause/effect of the bug. However, due to various limitations, existing approaches cannot analyze past bug fixes in large scale, and to the best of our knowledge, no previously unknown bugs were ever reported by their work. The major challenge to automatically analyze past bug fixes is that, bug-inducing inputs are typically not recorded, and many bug fixes are partial programs that have compilation errors. As a result, for most bugs in the version history, it is infeasible to reproduce them for dynamic analysis or to feed buggy/fixed code directly into static analysis tools which mostly depend on compilable complete programs. In this paper, we propose an approach, called DePa, that extracts bug signatures based on accurate partial-code analysis of bug fixes. With its support, we conduct the first large scale evaluation on 6,048 past bug fixes collected from four popular Apache projects. In particular, we use DePa to infer bug signatures from these fixes, and to check the latest versions of the four projects with the inferred bug signatures. Our results show that DePa detected 27 unique previously unknown bugs in total, including at least one bug from each project. These bugs are not detected by their developers nor other researchers. Among them, three of our reported bugs are already confirmed and repaired by their developers. Furthermore, our results show that the state-of-the-art tools detected only two of our found bugs, and our filtering techniques improve our precision from 25.5 to 51.5 percent. © 1976-2012 IEEE.
Author keywords: Bug fix; Bug signature; Partial code analysis
Index keywords: Application programming interfaces (API); Codes (symbols); Program debugging; Bug detection; Bug fixes; Bug signature; Code analysis; Detection tools; Large-scales; Partial code analyse; Program elements; Software versions; Static tools; Static analysis
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2022
EID: 2-s2.0-85125488043
DOI: 10.1109/tse.2020.2996975
Retrieval channels: authoritative_outlet_search
Local full-text files: 

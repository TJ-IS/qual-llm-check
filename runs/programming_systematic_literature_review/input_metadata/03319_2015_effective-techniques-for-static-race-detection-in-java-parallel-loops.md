---
otero_id: "2-s2.0-84941565255"
title: "Effective techniques for static race detection in Java parallel loops"
authors: "Radoi C.; Dig D."
year: "2015"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/2729975"
---
# Scopus title-abstract-keyword metadata
Title: Effective techniques for static race detection in Java parallel loops
Abstract: Despite significant progress in recent years, the important problem of static race detection remains open. Previous techniques took a general approach and looked for races by analyzing the effects induced by lowlevel concurrency constructs (e.g., Java.lang.Thread). But constructs and libraries for expressing parallelism at a higher level (e.g., fork-join, futures, parallel loops) are becoming available in all major programming languages. We claim that specializing an analysis to take advantage of the extra semantic information provided by the use of these constructs and libraries improves precision and scalability. We present ITERACE, a set of techniques that are specialized to use the intrinsic thread, safety, and dataflow structure of collections and of the new loop parallelism mechanism introduced in Java 8. Our evaluation shows that ITERACE is fast and precise enough to be practical. It scales to programs of hundreds of thousands of lines of code and reports very few race warnings, thus avoiding a common pitfall of static analyses. In five out of the seven case studies, ITERACE reported no false warnings. Also, it revealed six bugs in real-world applications. We reported four of them: one had already been fixed, and three were new and the developers confirmed and fixed them. Furthermore, we evaluate the effect of each specialization technique on the running time and precision of the analysis. For each application, we run the analysis under 32 different configurations. This allows to analyze each technique's effect both alone and in all possible combinations with other techniques. © 2015 ACM.
Author keywords: Java; Static analysis; Static race detection; Synchronization
Index keywords: Libraries; Program debugging; Semantics; Static analysis; Synchronization; Case-studies; Dataflow structures; Java; Lines of code; Parallel loops; Running time; Semantic information; Static race detection; Java programming language
Document type: Conference paper
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2015
EID: 2-s2.0-84941565255
DOI: 10.1145/2729975
Retrieval channels: authoritative_outlet_search
Local full-text files: 

---
otero_id: "2-s2.0-5444259962"
title: "Assembly instruction level reverse execution for debugging"
authors: "Akgul T.; Mooney III V.J."
year: "2004"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/1018210.1018211"
---
# Scopus title-abstract-keyword metadata
Title: Assembly instruction level reverse execution for debugging
Abstract: Assembly instruction level reverse execution provides a programmer with the ability to return a program to a previous state in its execution history via execution of a "reverse program." The ability to execute a program in reverse is advantageous for shortening software development time. Conventional techniques for recovering a state rely on saving the state into a record before the state is destroyed. However, state-saving causes significant memory and time overheads during forward execution. The proposed method introduces a reverse execution methodology at the assembly instruction level with low memory and time overheads. The methodology generates, from a program, a reverse program by which a destroyed state is almost always regenerated rather than being restored from a record. This significantly reduces state-saving. The methodology has been implemented on a PowerPC processor with a custom made debugger. As compared to previous work, all of which heavily use state-saving techniques, the experimental results show from 2X to 2206X reduction in run-time memory usage, from 1.5X to 403X reduction in forward execution time overhead and from 1.2X to 2.32X reduction in forward execution time for the tested benchmarks. Furthermore, due to the reduction in memory usage, our method can provide reverse execution in many cases where other methods run out of available memory. However, for cases where there is enough memory available, our method results in 1.16X to 1.89X slow down in reverse execution.
Author keywords: Debugging; Reverse code generation; Reverse execution
Index keywords: Algorithms; Codes (symbols); Data storage equipment; Program debugging; Program processors; Reverse engineering; Reverse code generation; Reverse execution; Run time memory usage; Software engineering
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2004
EID: 2-s2.0-5444259962
DOI: 10.1145/1018210.1018211
Retrieval channels: authoritative_outlet_search
Local full-text files: 

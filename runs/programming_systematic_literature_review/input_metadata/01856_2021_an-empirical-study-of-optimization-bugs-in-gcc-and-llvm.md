---
otero_id: "2-s2.0-85099207145"
title: "An empirical study of optimization bugs in GCC and LLVM"
authors: "Zhou Z.; Ren Z.; Gao G.; Jiang H."
year: "2021"
journal: "Journal of Systems and Software"
doi: "10.1016/j.jss.2020.110884"
---
# Scopus title-abstract-keyword metadata
Title: An empirical study of optimization bugs in GCC and LLVM
Abstract: Optimizations are the fundamental component of compilers. Bugs in optimizations have significant impacts, and can cause unintended application behavior and disasters, especially for safety-critical domains. Thus, an in-depth analysis of optimization bugs should be conducted to help developers understand and test the optimizations in compilers. To this end, we conduct an empirical study to investigate the characteristics of optimization bugs in two mainstream compilers, GCC and LLVM. We collect about 57K and 22K bugs of GCC and LLVM, and then exhaustively examine 8,771 and 1,564 optimization bugs of the two compilers, respectively. The results reveal the following five characteristics of optimization bugs: (1) Optimizations are the buggiest component in both compilers except for the C++ component; (2) the value range propagation optimization and the instruction combine optimization are the buggiest optimizations in GCC and LLVM, respectively; the loop optimizations in both GCC and LLVM are more bug-prone than other optimizations; (3) most of the optimization bugs in both GCC and LLVM are misoptimization bugs, accounting for 57.21% and 61.38% respectively; (4) on average, the optimization bugs live over five months, and developers take 11.16 months for GCC and 13.55 months for LLVM to fix an optimization bug; in both GCC and LLVM, many confirmed optimization bugs have lived for a long time; (5) the bug fixes of optimization bugs involve no more than two files and three functions on average in both compilers, and around 99% of them modify no more than 100 lines of code, while 90% less than 50 lines of code. Our study provides a deep understanding of optimization bugs for developers and researchers. This could provide useful guidance for the developers and researchers to better design the optimizations in compilers. In addition, the analysis results suggest that we need more effective techniques and tools to test compiler optimizations. Moreover, our findings are also useful to the research of automatic debugging techniques for compilers, such as automatic compiler bug isolation techniques. © 2020 Elsevier Inc.
Author keywords: Bug characteristics; Compiler optimization bugs; Compiler reliability; Compiler testing; Empirical study
Index keywords: Codes (symbols); Program compilers; Program debugging; Safety engineering; Application behaviors; Compiler optimizations; Empirical studies; Fundamental component; Isolation techniques; Loop optimizations; Safety-critical domain; Techniques and tools; C++ (programming language)
Document type: Article
Conference: 
Source title: Journal of Systems and Software
Year: 2021
EID: 2-s2.0-85099207145
DOI: 10.1016/j.jss.2020.110884
Retrieval channels: authoritative_outlet_search
Local full-text files: 

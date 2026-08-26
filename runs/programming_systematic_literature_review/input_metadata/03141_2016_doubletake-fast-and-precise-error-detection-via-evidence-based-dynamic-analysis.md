---
otero_id: "2-s2.0-84971386813"
title: "DOUBLETAKE: Fast and precise error detection via evidence-based dynamic analysis"
authors: "Liu T.; Curtsinger C.; Berger E.D."
year: "2016"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/2884781.2884784"
---
# Scopus title-abstract-keyword metadata
Title: DOUBLETAKE: Fast and precise error detection via evidence-based dynamic analysis
Abstract: Programs written in unsafe languages like C and C++ often suffer from errors like buffer overflows, dangling pointers, and memory leaks. Dynamic analysis tools like Valgrind can detect these errors, but their overhead-primarily due to the cost of instrumenting every memory read and write-makes them too heavyweight for use in deployed applications and makes testing with them painfully slow. The result is that much deployed software remains susceptible to these bugs, which are notoriously difficult to track down. This paper presents evidence-based dynamic analysis, an approach that enables these analyses while imposing minimal overhead (under 5%), making it practical for the first time to perform these analyses in deployed settings. The key insight of evidencebased dynamic analysis is that for a class of errors, it is possible to ensure that evidence that they happened at some point in the past remains for later detection. Evidence-based dynamic analysis allows execution to proceed at nearly full speed until the end of an epoch (e.g., a heavyweight system call). It then examines program state to check for evidence that an error occurred at some time during that epoch. If so, it rolls back execution and re-executes the code with instrumentation activated to pinpoint the error. We present DOUBLETAKE, a prototype evidence-based dynamic analysis framework. DOUBLETAKE is practical and easy to deploy, requiring neither custom hardware, compiler, nor operating system support. We demonstrate DOUBLETAKE's generality and efficiency by building dynamic analyses that find buffer overflows, memory use-after-free errors, and memory leaks. Our evaluation shows that DOUBLETAKE is efficient, imposing under 5% overhead on average, making it the fastest such system to date. It is also precise: DOUBLETAKE pinpoints the location of these errors to the exact line and memory addresses where they occur, providing valuable debugging information to programmers. © 2016 ACM.
Author keywords: 
Index keywords: Buffer storage; Computer software; Dynamic analysis; Errors; Program debugging; Software engineering; Analysis frameworks; Building dynamics; Dangling pointers; Debugging information; Deployed applications; Deployed software; Dynamic analysis tools; Operating system support; C++ (programming language)
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2016
EID: 2-s2.0-84971386813
DOI: 10.1145/2884781.2884784
Retrieval channels: authoritative_outlet_search
Local full-text files: 

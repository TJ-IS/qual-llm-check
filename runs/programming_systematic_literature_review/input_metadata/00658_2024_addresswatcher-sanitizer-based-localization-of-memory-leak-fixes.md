---
otero_id: "2-s2.0-85200810189"
title: "AddressWatcher: Sanitizer-Based Localization of Memory Leak Fixes"
authors: "Murali A.; Alfadel M.; Nagappan M.; Xu M.; Sun C."
year: "2024"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2024.3438119"
---
# Scopus title-abstract-keyword metadata
Title: AddressWatcher: Sanitizer-Based Localization of Memory Leak Fixes
Abstract: Memory leak bugs are a major problem in C/C++ programs. They occur when memory objects are not deallocated. Developers need to manually deallocate these objects to prevent memory leaks. As such, several techniques have been proposed to automatically fix memory leaks. Although proposed approaches have merit in automatically fixing memory leaks, they present limitations. Static-based approaches attempt to trace the complete semantics of memory object across all paths. However, they have scalability-related challenges when the target program has a large number of paths (path explosion). On the other hand, dynamic approaches can spell out precise semantics of memory object only on a single execution path (it does not consider multiple execution paths). In this paper, we complement prior approaches by designing and implementing a novel framework named AddressWatcher. AddressWatcher allows the semantics of a memory object to be tracked on multiple execution paths. Addresswatcher accomplishes this by using a leak database that allows one to store and compare different execution paths of a leak over several test cases. Also, AddressWatcher performs lightweight instrumentation during compile time that is utilized during the program execution to watch and track memory leak read/writes. We conduct an evaluation of AddressWatcher over five popular packages, namely binutils, openssh, tmux, openssl and git. In 23 out of 50 real-world memory leak bugs, AddressWatcher correctly points to a free location to fix memory leaks. Finally, we submit 25 Pull Requests across 12 popular OSS repositories using AddressWatcher suggestions. Among these, 21 were merged leading to 5 open issues being addressed. In fact, our critical fix prompted a new version release for the calc repository, a program used to find large primes. Furthermore, our contributions through these PRs sparked intense discussions and appreciation in various repositories such as coturn, h2o, and radare2. © 1976-2012 IEEE.
Author keywords: dynamic analysis; Memory leak; vulnerability
Index keywords: C (programming language); Leak detection; Program debugging; Code; Computer bugs; Dynamics analysis; Execution paths; Leaks detections; Memory leak fix; Memory leaks; Memory-management; Resource management; Semantics
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2024
EID: 2-s2.0-85200810189
DOI: 10.1109/tse.2024.3438119
Retrieval channels: authoritative_outlet_search
Local full-text files: 

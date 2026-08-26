---
otero_id: "2-s2.0-84867334716"
title: "Precise calling context encoding"
authors: "Sumner W.N.; Zheng Y.; Weeratunge D.; Zhang X."
year: "2012"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2011.70"
---
# Scopus title-abstract-keyword metadata
Title: Precise calling context encoding
Abstract: Calling contexts (CCs) are very important for a wide range of applications such as profiling, debugging, and event logging. Most applications perform expensive stack walking to recover contexts. The resulting contexts are often explicitly represented as a sequence of call sites and hence are bulky. We propose a technique to encode the current calling context of any point during an execution. In particular, an acyclic call path is encoded into one number through only integer additions. Recursive call paths are divided into acyclic subsequences and encoded independently. We leverage stack depth in a safe way to optimize encoding: If a calling context can be safely and uniquely identified by its stack depth, we do not perform encoding. We propose an algorithm to seamlessly fuse encoding and stack depth-based identification. The algorithm is safe because different contexts are guaranteed to have different IDs. It also ensures contexts can be faithfully decoded. Our experiments show that our technique incurs negligible overhead (0-6.4 percent). For most medium-sized programs, it can encode all contexts with just one number. For large programs, we are able to encode most calling contexts to a few numbers. We also present our experience of applying context encoding to debugging crash-based failures. © 2012 IEEE.
Author keywords: call graph; Calling context; calling context encoding; context sensitivity; path encoding; profiling
Index keywords: Program debugging; Signal encoding; Call graphs; Calling context encoding; Calling contexts; Context sensitivity; Path encoding; profiling; Encoding (symbols)
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2012
EID: 2-s2.0-84867334716
DOI: 10.1109/tse.2011.70
Retrieval channels: authoritative_outlet_search
Local full-text files: 

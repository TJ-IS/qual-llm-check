---
otero_id: "2-s2.0-85180554479"
title: "On the Caching Schemes to Speed Up Program Reduction"
authors: "Tian Y.; Zhang X.; Dong Y.; Xu Z.; Zhang M.; Jiang Y.; Cheung S.-C.; Sun C."
year: "2023"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3617172"
---
# Scopus title-abstract-keyword metadata
Title: On the Caching Schemes to Speed Up Program Reduction
Abstract: Program reduction is a highly practical, widely demanded technique to help debug language tools, such as compilers, interpreters and debuggers. Given a program P that exhibits a property Ψ, conceptually, program reduction iteratively applies various program transformations to generate a vast number of variants from P by deleting certain tokens and returns the minimal variant preserving Ψ as the result. A program reduction process inevitably generates duplicate variants, and the number of them can be significant. Our study reveals that on average 61.8% and 24.3% of the generated variants in two representative program reducers HDD and Perses, respectively, are duplicates. Checking them against Ψ is thus redundant and unnecessary, which wastes time and computation resources. Although it seems that simply caching the generated variants can avoid redundant property tests, such a trivial method is impractical in the real world due to the significant memory footprint. Therefore, a memory-efficient caching scheme for program reduction is in great demand. This study is the first effort to conduct a systematic, extensive analysis of memory-efficient caching schemes for program reduction. We first propose to use two well-known compression methods, ZIP and SHA, to compress the generated variants before they are stored in the cache. Furthermore, our keen understanding on the program reduction process motivates us to propose a novel, domain-specific, both memory and computation-efficient caching scheme, Refreshable Compact Caching (RCC). Our key insight is two-fold: 1 by leveraging the correlation between variants and the original program P, we losslessly encode each variant into an equivalent, compact, canonical representation; 2 periodically, stale cache entries, which will never be accessed, are timely removed to minimize the memory footprint over time. Our extensive evaluation on 31 real-world C compiler bugs demonstrates that caching schemes help avoid issuing redundant queries by 61.8% and 24.3% in HDD and Perses, respectively; correspondingly, the runtime.  © 2023 Copyright held by the owner/author(s).
Author keywords: debugging; delta debugging; Program reduction
Index keywords: C (programming language); Cache memory; Program compilers; Program debugging; Program interpreters; % reductions; Caching scheme; Debugging; Delta debugging; Memory efficient; Memory footprint; Program reduction; Real-world; Reduction process; Speed up; Iterative methods
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2023
EID: 2-s2.0-85180554479
DOI: 10.1145/3617172
Retrieval channels: authoritative_outlet_search
Local full-text files: 

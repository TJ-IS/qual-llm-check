---
otero_id: "2-s2.0-85068958364"
title: "Automatic patch generation with context-based change application"
authors: "Kim J.; Kim S."
year: "2019"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-019-09742-5"
---
# Scopus title-abstract-keyword metadata
Title: Automatic patch generation with context-based change application
Abstract: Automatic patch generation is often described as a search problem of patch candidate space, and it has two major issues: one is search space size, and the other is navigation. An effective patch generation technique should have a large search space with a high probability that patches for bugs are included, and it also needs to locate such patches effectively. We introduce ConFix, an automatic patch generation technique using context-based change application. ConFix collects abstract AST changes from human-written patches with their AST contexts to provide abundant resources for patch generation. These collected changes are only applied to possible fix locations with the same contexts for patch generation. By considering changes with a matching context only, ConFix selects a necessary change for a possible fix location more effectively than considering all the collected changes. Also, ConFix filters out fix locations with no collected changes in the same context, which means that such locations have not been modified in human-written patches, hence they are not desirable for modifications. We evaluated ConFix with 357 real bugs from Defects4j dataset. ConFix successfully fixed 22 bugs including six bugs which were not fixed by compared existing techniques. With context-based strategy, ConFix checked on average 48% less fix locations than a strategy using only a spectrum-based fault localization technique until patches were generated. Also, it ranked changes required for patches at the top for 63.6%, and within top-3 for 81.8% of the fixed bugs. © 2019, Springer Science+Business Media, LLC, part of Springer Nature.
Author keywords: Automatic patch generation; Automatic program repair; Context-based change application
Index keywords: Application programs; Location; Abundant resources; Automatic patch generation; Automatic programs; Context-based; Fault localization; Generation techniques; High probability; Search space size; Automatic programming
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2019
EID: 2-s2.0-85068958364
DOI: 10.1007/s10664-019-09742-5
Retrieval channels: authoritative_outlet_search
Local full-text files: 

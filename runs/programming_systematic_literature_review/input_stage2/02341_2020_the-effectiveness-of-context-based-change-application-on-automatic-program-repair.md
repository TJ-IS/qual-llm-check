---
otero_id: "2-s2.0-85073786858"
title: "The effectiveness of context-based change application on automatic program repair"
authors: "Kim J.; Kim J.; Lee E.; Kim S."
year: "2020"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-019-09770-1"
---
# Scopus title-abstract-keyword metadata
Title: The effectiveness of context-based change application on automatic program repair
Abstract: An Automatic Program Repair (APR) technique is an implementation of a repair model to fix a given bug by modifying program behavior. Recently, repair models which collect source code and code changes from software history and use such collected resources for patch generation became more popular. Collected resources are used to expand the patch search space and to increase the probability that correct patches for bugs are included in the space. However, it is also revealed that navigation on such expanded patch search space is difficult due to the sparseness of correct patches in the space. In this study, we evaluate the effectiveness of Context-based Change Application (CCA) technique on change selection, fix location selection and change concretization, which are the key aspects of navigating patch search space. CCA collects abstract subtree changes and their AST contexts, and applies them to fix locations only if their contexts are matched. CCA repair model can address both search space expansion and navigation issues, by expanding search space with collected changes while narrowing down search areas in the search space based on contexts. Since CCA applies changes to a fix location only if their contexts are matched, it only needs to consider the same context changes for each fix location. Also, if there is no change with the same context as a fix location, this fix location can be ignored since it means that past patches did not modify such locations. In addition, CCA uses fine-grained changes preserving changed code structures, but normalizing user-defined names. Hence change concretization can be simply done by replacing normalized names with concrete names available in buggy code. We evaluated CCA’s effectiveness with over 54K unique collected changes (221K in total) from about 5K human-written patches. Results show that using contexts, CCA correctly found 90.1% of the changes required for test set patches, while fewer than 5% of the changes were found without contexts. We discovered that collecting more changes is only helpful if it is supported by contexts for effective search space navigation. In addition, CCA repair model found 44-70% of the actual fix locations of Defects4j patches more quickly compared to using SBFL techniques only. We also found that about 48% of the patches can be fully concretized using concrete names from buggy code. © 2019, Springer Science+Business Media, LLC, part of Springer Nature.
Author keywords: Automatic program repair; Context-based change application; Repair models
Index keywords: Codes (symbols); Concretes; Location; Navigation; Repair; Automatic programs; Code structure; Context-based; Fine-grained changes; Location selection; Program behavior; Repair models; Software history; Application programs
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2020
EID: 2-s2.0-85073786858
DOI: 10.1007/s10664-019-09770-1
Retrieval channels: authoritative_outlet_search
Local full-text files: 

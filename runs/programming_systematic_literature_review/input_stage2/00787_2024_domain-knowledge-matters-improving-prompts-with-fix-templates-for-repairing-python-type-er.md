---
otero_id: "2-s2.0-85185534698"
title: "Domain Knowledge Matters: Improving Prompts with Fix Templates for Repairing Python Type Errors"
authors: "Peng Y.; Gao S.; Gao C.; Huo Y.; Lyu M.R."
year: "2024"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3597503.3608132"
---
# Scopus title-abstract-keyword metadata
Title: Domain Knowledge Matters: Improving Prompts with Fix Templates for Repairing Python Type Errors
Abstract: As a dynamic programming language, Python has become increasingly popular in recent years. Although the dynamic type system of Python facilitates the developers in writing Python programs, it also brings type errors at run-time which are prevalent yet not easy to fix. There exist rule-based approaches for automatically repairing Python type errors. The approaches can generate accurate patches for the type errors covered by manually defined templates, but they require domain experts to design patch synthesis rules and suffer from low template coverage of real-world type errors. Learning-based approaches alleviate the manual efforts in designing patch synthesis rules and have become prevalent due to the recent advances in deep learning. Among the learning-based approaches, the prompt-based approach which leverages the knowledge base of code pre-trained models via pre-defined prompts, obtains state-of-the-art performance in general program repair tasks. However, such prompts are manually defined and do not involve any specific clues for repairing Python type errors, resulting in limited effectiveness. How to automatically improve prompts with the domain knowledge for type error repair is challenging yet under-explored. In this paper, we present TypeFix, a novel prompt-based approach with fix templates incorporated for repairing Python type errors. TypeFix first mines generalized fix templates via a novel hierarchical clustering algorithm. The identified fix templates indicate the common edit patterns and contexts of existing type error fixes. TypeFix then generates code prompts for code pre-trained models by employing the generalized fix templates as domain knowledge, in which the masks are adaptively located for each type error instead of being pre-determined. Experiments on two benchmarks, including BugsInPy and TypeBugs, show that TypeFix successfully repairs 26 and 55 type errors, outperforming the best baseline approach by 9 and 14, respectively. Besides, the proposed fix template mining approach can cover 75% of developers’ patches in both benchmarks, increasing the best rule-based approach PyTER by more than 30%. © 2024 IEEE Computer Society. All rights reserved.
Author keywords: 
Index keywords: Clustering algorithms; Computer software; Deep learning; Domain Knowledge; Dynamic programming; Errors; High level languages; Repair; Domain experts; Domain knowledge; Dynamic programming languages; Dynamic type systems; Learning-based approach; Rule-based approach; Runtimes; Synthesis rules; Template coverage; Type errors; Python
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2024
EID: 2-s2.0-85185534698
DOI: 10.1145/3597503.3608132
Retrieval channels: authoritative_outlet_search
Local full-text files: 

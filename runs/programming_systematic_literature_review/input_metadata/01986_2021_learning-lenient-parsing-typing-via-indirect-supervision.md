---
otero_id: "2-s2.0-85102176518"
title: "Learning lenient parsing & typing via indirect supervision"
authors: "Ahmed T.; Devanbu P.; Hellendoorn V.J."
year: "2021"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-021-09942-y"
---
# Scopus title-abstract-keyword metadata
Title: Learning lenient parsing & typing via indirect supervision
Abstract: Both professional coders and teachers frequently deal with imperfect (fragmentary, incomplete, ill-formed) code. Such fragments are common in StackOverflow; students also frequently produce ill-formed code, for which instructors, TAs (or students themselves) must find repairs. In either case, the developer experience could be greatly improved if such code could somehow be parsed & typed; this makes such code more amenable to use within IDEs and allows early detection and repair of potential errors. We introduce a lenient parser, which can parse & type fragments, even ones with simple errors. Training a machine learner to leniently parse and type imperfect code requires a large training set including many pairs of imperfect code and its repair (and/or type information); such training sets are limited by human effort and curation. In this paper, we present a novel, indirectly supervised, approach to train a lenient parser, without access to such human-curated training data. We leverage the huge corpus of mostly correct code available on Github, and the massive, efficient learning capacity of Transformer-based NN architectures. Using GitHub data, we first create a large dataset of fragments of code and corresponding tree fragments and type annotations; we then randomly corrupt the input fragments (while requiring correct output) by seeding errors that mimic corruptions found in StackOverflow and student data. Using this data, we train high-capacity transformer models to overcome both fragmentation and corruption. With this novel approach, we can achieve reasonable performance on parsing & typing StackOverflow fragments; we also demonstrate that our approach performs well on shorter student error program and achieves best-in-class performance on longer programs that have more than 400 tokens. We also show that by blending DeepFix and our tool, we could achieve 77% accuracy, which outperforms all previously reported student error correction tools. © 2021, The Author(s), under exclusive licence to Springer Science+Business Media, LLC part of Springer Nature.
Author keywords: Deep learning; Naturalness; Program repair
Index keywords: Blending; Error correction; Large dataset; Students; Turing machines; Detection and repairs; Efficient learning; Machine learners; Potential errors; Training data; Transformer models; Type annotations; Type information; Trees (mathematics)
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2021
EID: 2-s2.0-85102176518
DOI: 10.1007/s10664-021-09942-y
Retrieval channels: authoritative_outlet_search
Local full-text files: 

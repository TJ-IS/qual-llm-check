---
otero_id: "2-s2.0-105031609673"
title: "POS Tagging on Code Identifiers: How Far Are We?"
authors: "Tang H.; Jiang Y.; Zhang Y.; Niu N.; Liu H."
year: "2026"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3744919"
---
# Scopus title-abstract-keyword metadata
Title: POS Tagging on Code Identifiers: How Far Are We?
Abstract: Part-of-Speech (POS) tags are natural attributes of words in natural languages, and they are fundamental for natural language analysis. Many automated approaches have been proposed to tag natural language texts. Identifiers in source code have POS tags as well, which are useful for various source code analysis tasks, like code search, code comment generation, and code completion. Currently, state-of-the-art POS taggers originally designed for natural languages are often employed to tag source code identifiers. However, identifiers in source code are significantly different from natural languages. Consequently, POS taggers designed for natural languages could be less accurate in source code identifiers. Recently, several identifier-specific taggers have been proposed within the field of software engineering, but their adoption in practical software engineering tasks remains limited. This raises the question of why these taggers have not been more widely utilized in such tasks. In this article, we investigate the performance of natural language POS taggers on source code identifiers, specifically method names, parameter names, and class names. To do so, we manually annotated identifiers from open source projects in Java, C, and Python, creating a large dataset IDData for evaluation. We then evaluated six widely used natural language POS taggers: NLTK, CoreNLP, OpenNLP, spaCy, Flair, and Stanza, alongside three identifier-specific taggers: SWUM, POSSE, and Ensemble Tagger. Our evaluation reveals that while natural language-oriented POS taggers outperform identifier-specific taggers, their performance on identifiers is still significantly lower compared to their performance on natural language sentences. To understand the underlying reasons for this, we conducted an in-depth analysis, examining factors such as identifier length, POS distribution, syntactic structures, and special tags, which differentiate identifiers from natural language sentences. To further improve POS tagging performance on identifiers, we created a large-scale method name dataset MNTrain with manually labeled tags and retrained the natural language taggers on this new dataset. The results show substantial improvements in method name POS tagging performance, with taggers achieving performance comparable to their results on natural language sentences. Finally, we discuss the significance and practical implications of our findings, offering insights for future research. © 2026 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: Code Identifier; Evaluation of Tools; Natural Language Processing; Part-of-speech Tagging
Index keywords: C (programming language); Codes (symbols); Computational linguistics; Large datasets; Open source software; Open systems; Problem oriented languages; Syntactics; Code identifier; Evaluation of tool; Language processing; Natural language processing; Natural languages; Part of speech tagging; Part-of-speech tagger; Parts-of-speech tagging; Performance; Source codes; Natural language processing systems
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2026
EID: 2-s2.0-105031609673
DOI: 10.1145/3744919
Retrieval channels: authoritative_outlet_search
Local full-text files: 

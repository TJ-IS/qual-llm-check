---
otero_id: "2-s2.0-85139248220"
title: "Modeling function-level interactions for file-level bug localization"
authors: "Liang H.; Hang D.; Li X."
year: "2022"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-022-10237-z"
---
# Scopus title-abstract-keyword metadata
Title: Modeling function-level interactions for file-level bug localization
Abstract: Automatic bug localization, i.e., automatically locating potential buggy source files given a bug report, plays an essential role in software engineering. For instance, bug localization helps developers fix bugs quickly. Although information retrieval-based bug localization methods are simple and easy to understand, it is difficult for them to bridge the lexical gap between bug reports and programs and capture the rich structural information in programs. Deep learning-based bug localization (DLBL) methods can utilize the structural information of the program, but they cannot handle long code sequences well. For example, CNN fails to capture remote code interaction features, while RNN (like LSTM, GRU) is vulnerable to gradient disappearance or burst when facing long code sequences. Additionally, DLBL methods fail to model metadata features such as bug-fixing recency and frequency. In this paper, we research how to locate buggy files by learning function-level features. Specifically, we propose a new framework called FLIM that can extract semantic features of a program at the function level and then calculates the relevance between natural and programming language by aggregating function-level interactions. We leverage a fine-tuned language model to treat the bug localization task as a code retrieval task, and use a learning-to-rank model to fuse the function-level semantic features with IR features to calculate the final relevance. We evaluate FLIM by conducting extensive experiments on widely-used six software projects. Experimental results demonstrate that FLIM outperforms six state-of-the-art methods of bug localization. © 2022, The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature.
Author keywords: Bug localization; Fine-tuning; Language model; Learning-to-rank
Index keywords: Computational linguistics; Learning systems; Modeling languages; Program debugging; Semantics; Software engineering; Bug localizations; Bug reports; Code sequences; Fine tuning; Functions level; Language model; Localization method; Long codes; Semantic features; Structural information; Long short-term memory
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2022
EID: 2-s2.0-85139248220
DOI: 10.1007/s10664-022-10237-z
Retrieval channels: authoritative_outlet_search
Local full-text files: 

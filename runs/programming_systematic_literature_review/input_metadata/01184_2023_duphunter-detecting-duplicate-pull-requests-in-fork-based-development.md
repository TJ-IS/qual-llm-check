---
otero_id: "2-s2.0-85151561766"
title: "DupHunter: Detecting Duplicate Pull Requests in Fork-Based Development"
authors: "Jiang H.; Li Y.; Guo S.; Li X.; Zhang T.; Li H.; Chen R."
year: "2023"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2023.3235942"
---
# Scopus title-abstract-keyword metadata
Title: DupHunter: Detecting Duplicate Pull Requests in Fork-Based Development
Abstract: The emergence of numerous fork-based development platforms facilitates the development of Open-Source Software (OSS) projects. Developers across the world can fork software projects and submit their Pull Requests (PRs) to the projects. However, as the number of forks increases, numerous duplicate PRs might be submitted. These duplicate PRs may cause extra code review workload and frustrate developers working on the projects. To detect duplicate PRs, many approaches have been proposed, which analyze the similarity of different elements in PRs. However, previous approaches still suffer from unsatisfied detection accuracy due to two challenges. That is, they ignore the syntactic structural information of text elements in PRs and lack the joint reasoning between different elements of two PRs. In this study, we propose an automated duplicate PRs detector named DupHunter (Duplicate PRs Hunter), which includes a graph embedding component and a duplicate PRs detection component to address the above challenges. The graph embedding component uses a feature graph to represent a PR. It encodes the syntactic structure and semantics of text elements (e.g., the title and the description), as well as the knowledge of non-text elements (e.g., the submission time), to address the syntactic structural information challenge. The duplicate PRs detection component tackles the joint reasoning challenge using a graph matching network, which enables the information exchange and matching across different elements of two feature graphs with an attention coefficient mechanism. Experiments on 26 open-source projects show that DupHunter achieves an average F1-score@1 value of 0.650, significantly outperforming the state-of-the-art approaches by 3.2% to 48.1%. DupHunter can accurately detect duplicate PRs, with an average Precision@1 value of 0.922 and an average Recall@1 value of 0.502.  © 1976-2012 IEEE.
Author keywords: Duplicate pull requests detection; fork-based development; graph embeddings; open source; text processing
Index keywords: Cloning; Embeddings; Open source software; Open systems; Semantics; Software design; Syntactics; Text processing; Code; Cognition; Duplicate pull request detection; Features extraction; Fork-based development; Graph embeddings; Open-source; Software; Software development management; Text-processing; Feature extraction
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2023
EID: 2-s2.0-85151561766
DOI: 10.1109/tse.2023.3235942
Retrieval channels: authoritative_outlet_search
Local full-text files: 

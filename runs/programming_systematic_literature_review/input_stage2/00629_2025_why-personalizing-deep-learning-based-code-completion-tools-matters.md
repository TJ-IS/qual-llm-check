---
otero_id: "2-s2.0-105027978039"
title: "Why Personalizing Deep Learning-Based Code Completion Tools Matters"
authors: "Giagnorio A.; Martin-Lopez A.; Bavota G."
year: "2025"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3725732"
---
# Scopus title-abstract-keyword metadata
Title: Why Personalizing Deep Learning-Based Code Completion Tools Matters
Abstract: Deep learning (DL)-based code completion tools have revolutionized software development by providing unprecedented code generation capabilities. The DL models behind these tools are usually trained on large amounts of code from thousands of software repositories. This makes them good in learning natural coding patterns observed across many training instances. However, little is known about the extent to which additional training effort (fine-tuning) aimed at specializing the models towards the code base of a given organization/developer further benefits their code completion capabilities. In this work, we fill this gap by presenting solid empirical evidence answering this question. More specifically, we consider 136 developers from two organizations (Apache and Spring), two model architectures (T5 and Code Llama), and three model sizes (60M, 750M, and 7B trainable parameters). For T5 models (60M and 750M), we pre-train and fine-tune them on over 2,000 open source projects, making sure that code from the two subject organizations is not part of their training sets. Then, we compare their completion capabilities against the same models further fine-tuned on organization- and developer-specific datasets. For the Code Llama model (7B), we compare the performance of the already pre-trained model publicly available online with the same model fine-tuned via parameter-efficient fine-tuning on organization- and developer-specific datasets. Our results show that there is a boost in prediction capabilities provided by both an organization-specific and a developer-specific additional fine-tuning, with the former being particularly performant. Such a finding generalizes across (i) the two subject organizations (i.e., Apache and Spring) and (ii) models of completely different magnitude (from 60M to 7B trainable parameters). Finally, we show that DL models fine-tuned on an organization-specific dataset achieve the same completion performance of pre-trained code models used out of the box and being ∼10× larger, with consequent savings in terms of deployment and inference cost (e.g., smaller GPUs needed). © 2025 Copyright held by the owner/author(s).
Author keywords: Artificial Intelligence; Code Recommenders; Software Engineering; Training Strategies
Index keywords: Computer aided software engineering; Computer programming languages; Deep learning; Information management; Open source software; Open systems; Software design; Code completions; Code recommender; Codegeneration; Completion tools; Fine tuning; Large amounts; Learning models; Performance; Software repositories; Training strategy; Codes (symbols)
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2025
EID: 2-s2.0-105027978039
DOI: 10.1145/3725732
Retrieval channels: authoritative_outlet_search
Local full-text files: 

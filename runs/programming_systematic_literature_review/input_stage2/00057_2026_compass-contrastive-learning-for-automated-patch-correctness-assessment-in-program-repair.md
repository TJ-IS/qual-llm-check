---
otero_id: "2-s2.0-105040769665"
title: "ComPass: Contrastive Learning for Automated Patch Correctness Assessment in Program Repair"
authors: "Zhang Q.; Shang Y.; Hu H.; Fang C.; Chen Z.; Xiao L."
year: "2026"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-026-10871-x"
---
# Scopus title-abstract-keyword metadata
Title: ComPass: Contrastive Learning for Automated Patch Correctness Assessment in Program Repair
Abstract: Automated program repair (APR) attempts to reduce manual debugging efforts and plays a vital role in software maintenance. Despite remarkable progress, APR is still limited in generating overfitting patches, i.e., patches passing available test suites but incorrect. This issue, known as patch overfitting, has become a key concern in the APR community, with numerous approaches proposed to address it. Very recent work proposes a pre-trained language model (PLM)–based automated patch correctness assessment (APCA) approach, indicating the potential of such PLMs in reasoning about patch correctness. Despite being promising, it is still far from perfect due to various limitations, such as the training paradigm and training dataset. In this paper, we present ComPass, a PLM-based APCA approach that leverages contrastive learning and data augmentation to address the technical limitations of prior work. Our work is inspired by the opportunity to integrate contrastive learning with recent PLMs in the field of patch correctness assessment, where large-scale labeled patches are difficult to obtain. ComPass utilizes code transformation rules to generate semantic-preserving code snippets for both unlabeled pre-training corpus and labeled fine-tuning patches. ComPass then pre-trains PLMs with contrastive learning, which captures code features with the same semantics but different structures. ComPass finally integrates representation embeddings of patch code snippets and fine-tunes PLMs with a binary classifier jointly to assess patch code correctness. ComPass is a generic framework that can be adapted to different encoder PLMs, and we implement it to facilitate patch correctness assessment based on the well-known BERT. Experimental results on 2274 real-world patches from Defects4J demonstrate that ComPass achieves an accuracy of 88.35%, precision of 87.50%, recall of 88.69%, and an F1-score of 88.09%, significantly outperforming state-of-the-art baseline APPT. We further investigate the impact of each component and find that they all positively contribute to ComPass, e.g., the contrastive learning process increases accuracy by 4.11% and precision by 7.80%. We also prove that ComPass is generalized to existing learning-based APCA approaches (e.g., APPT) and advanced PLMs (CodeBERT), e.g., the integration of ComPass with APPT and CodeBERT lead to an improvement of 7.39% and 6.82% for accuracy. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2026.
Author keywords: Automated program repair; Patch overfitting; Pre-trained model
Index keywords: Automation; Codes (symbols); Computer software maintenance; Learning systems; Natural language processing systems; Semantics; Assessment approaches; Automated program repair; Data augmentation; Debugging efforts; Language model; Model-based OPC; Overfitting; Patch overfitting; Pre-trained model; Training dataset; Repair
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2026
EID: 2-s2.0-105040769665
DOI: 10.1007/s10664-026-10871-x
Retrieval channels: authoritative_outlet_search
Local full-text files: 

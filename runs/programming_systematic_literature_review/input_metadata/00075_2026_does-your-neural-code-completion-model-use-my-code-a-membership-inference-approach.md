---
otero_id: "2-s2.0-105031593448"
title: "Does Your Neural Code Completion Model Use My Code? A Membership Inference Approach"
authors: "Wan Y.; Wan G.; Zhang S.; Zhang H.; Sui Y.; Zhou P.; Jin H.; Sun L."
year: "2026"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3742785"
---
# Scopus title-abstract-keyword metadata
Title: Does Your Neural Code Completion Model Use My Code? A Membership Inference Approach
Abstract: Recent years have witnessed significant progress in developing deep learning-based models for automated code completion. Examples of such models include CodeGPT and StarCoder. These models are typically trained from a large amount of source code collected from open source communities such as GitHub. Although using source code in GitHub has been a common practice for training deep-learning-based models for code completion, it may induce some legal and ethical issues such as copyright infringement. In this article, we investigate the legal and ethical issues of current neural code completion models by answering the following question: Is my code used to train your neural code completion model? To this end, we tailor a membership inference approach (termed CodeMI) that was originally crafted for classification tasks to a more challenging task of code completion. In particular, since the target code completion models perform as opaque black boxes, preventing access to their training data and parameters, we opt to train multiple shadow models to mimic their behavior. The acquired posteriors from these shadow models are subsequently employed to train a membership classifier. After that, the membership classifier can be effectively employed to deduce the membership status of a given code sample based on the output of a target code completion model. We comprehensively evaluate the effectiveness of this adapted approach across a diverse array of neural code completion models (i.e., LSTM-based, CodeGPT, CodeGen, and StarCoder). Experimental results demonstrate that our approach effectively detects data membership, achieving accuracies of 0.842 and 0.730 for LSTM-based and CodeGPT models, respectively. Interestingly, our experiments also show that the data membership of current large language models of code, e.g., CodeGen and StarCoder, is difficult to detect, leaving ample space for further improvement. Finally, we also try to explain the findings from the perspective of model memorization. © 2026 Copyright held by the owner/author(s).
Author keywords: Code completion; deep learning; membership inference
Index keywords: Classification (of information); Codes (symbols); Copyrights; Ethical aspects; Neural networks; Open systems; 'current; Code completions; Deep learning; Ethical issues; Learning Based Models; Legal issues; Membership inference; Neural code; Source codes; Target codes; Deep learning
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2026
EID: 2-s2.0-105031593448
DOI: 10.1145/3742785
Retrieval channels: authoritative_outlet_search
Local full-text files: 

---
otero_id: "2-s2.0-105002608903"
title: "Retrieval-Augmented Fine-Tuning for Improving Retrieve-and-Edit Based Assertion Generation"
authors: "Li H.; Sun W.; Yan M.; Xu L.; Li Q.; Zhang X.; Zhang H."
year: "2025"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2025.3558403"
---
# Scopus title-abstract-keyword metadata
Title: Retrieval-Augmented Fine-Tuning for Improving Retrieve-and-Edit Based Assertion Generation
Abstract: Unit Testing is crucial in software development and maintenance, aiming to verify that the implemented functionality is consistent with the expected functionality. A unit test is composed of two parts: a test prefix, which drives the unit under test to a particular state, and a test assertion, which determines what the expected behavior is under that state. To reduce the effort of conducting unit tests manually, Yu et al. proposed an integrated approach (integration for short), combining information retrieval with a deep learning-based approach to generate assertions for test prefixes, and obtained promising results. In our previous work, we found that the overall performance of integration is mainly due to its success in retrieving assertions. Moreover, integration is limited to specific types of edit operations and struggles to understand the semantic differences between the retrieved focal-test (focal-test includes a test prefix and a unit under test) and the input focal-test. Based on these insights, we then proposed a retrieve-and-edit approach named EDITAS to learn the assertion edit patterns to improve the effectiveness of assertion generation in our prior study. Despite being promising, we find that the effectiveness of EDITAS can be further improved. Our analysis shows that: ① The editing ability of EDITAS still has ample room for improvement. Its performance degrades as the edit distance between the retrieval assertion and ground truth increases. Specifically, the average accuracy of EDITAS is 12.38% when the edit distance is greater than 5. ② EDITAS lacks a fine-grained semantic understanding of both the retrieved focal-test and the input focal-test themselves, which leads to many inaccurate token modifications. In particular, an average of 25.57% of the incorrectly generated assertions that need to be modified are not modified, and an average of 6.45% of the assertions that match the ground truth are still modified. Thanks to pre-trained models employing pre-training paradigms on large-scale data, they tend to have good semantic comprehension and code generation abilities. In light of this, we propose EditAS2, which improves retrieval-and-edit based assertion generation through retrieval-augmented fine-tuning. Specifically, EditAS2 first retrieves a similar focal-test from a predefined corpus and treats its assertion as a prototype. Then, EditAS2 uses a pretrained model, CodeT5, to learn the semantics of the input and similar focal-tests as well as assertion editing patterns to automatically edit the prototype. We first evaluate the EditAS2 for its inference performance on two large-scale datasets, and the experimental results show that EditAS2 outperforms state-of-the-art assertion generation methods and pre-trained models, with average performance improvements of 15.93%-129.19% and 11.01%-68.88% in accuracy and CodeBLEU, respectively. We also evaluate the performance of EditAS2 in detecting real-world bugs from Defects4J. The experimental results indicate that EditAS2 achieves the best bug detection performance among all the methods. © 1976-2012 IEEE.
Author keywords: assertion generation; fine-tuning; pre-trained model; test assertion; Unit testing
Index keywords: Computer software maintenance; Integration testing; Model checking; Program debugging; Search engines; Assertion generations; Fine tuning; Learn+; Performance; Pre-trained model; Test assertions; Unit testing; Unit tests; Unit under test; Units under tests; Software design
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2025
EID: 2-s2.0-105002608903
DOI: 10.1109/tse.2025.3558403
Retrieval channels: authoritative_outlet_search
Local full-text files: 

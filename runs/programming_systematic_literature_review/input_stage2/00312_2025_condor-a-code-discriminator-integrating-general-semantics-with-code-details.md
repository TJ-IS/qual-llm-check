---
otero_id: "2-s2.0-105019257022"
title: "Condor: A Code Discriminator Integrating General Semantics With Code Details"
authors: "Liang Q.; Zhang Z.; Liu C.; Sun Z.; Zhang W.; Chen Y.; Zhao Z.; Luo Q.; Wang W.; Jiang Y.; Xiong Y.; Zhang L."
year: "2025"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2025.3620145"
---
# Scopus title-abstract-keyword metadata
Title: Condor: A Code Discriminator Integrating General Semantics With Code Details
Abstract: LLMs demonstrate significant potential across various software engineering tasks. However, they still face challenges in generating correct code on the first attempt when addressing complex requirements. Introducing a discriminator to select reliable outputs from multiple generated results is an effective way to enhance their reliability and stability. Currently, these discriminators fall into two categories: execution-based discriminators and non-execution-based discriminators. Execution-based discriminators face flexibility challenges due to difficulties in obtaining test cases and security concerns, while non-execution-based discriminators, although more flexible, struggle to capture subtle differences in code details. To maintain flexibility while improving the model’s ability to capture fine-grained code details, this paper proposes Condor. We first design contrastive learning to optimize the code representations of the base model, enabling it to reflect differences in code details. Then, we leverage intermediate data from the code modification process to further enrich the discriminator’s training data, enhancing its ability to discern code details. Experimental results indicate that on the subtle code difference dataset (i.e., CodeNanoFix), Condor significantly outperforms other discriminators in discriminative performance: Condor (1.3B) improves the discriminative F1 score of DeepSeek-Coder (1.3B) from 67% to 73%. In discriminating LLM-generated outputs, Condor (1.3B) and Condor (110M) raise the Pass@1 score of Llama-3.1-Instruct (70B) on the CodeNanoFix dataset from 52.64% to 62.63% and 59.64%, respectively. Moreover, Condor demonstrates strong generalization capabilities on the APPS, MBPP, and LiveCodeBench datasets. For example, Condor (1.3B) improves the Pass@1 of Llama-3.1-Instruct (70B) on the APPS dataset by 147.05%. © 1976-2012 IEEE.
Author keywords: Code discriminator; code embedding; code generation; code repair
Index keywords: Artificial intelligence; Discriminators; Learning systems; Network security; Software engineering; Code discriminator; Code embedding; Code repair; Codegeneration; Correct code; Embeddings; Engineering tasks; Fine grained; Reliability and stability; Test case; Codes (symbols)
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2025
EID: 2-s2.0-105019257022
DOI: 10.1109/tse.2025.3620145
Retrieval channels: authoritative_outlet_search
Local full-text files: 

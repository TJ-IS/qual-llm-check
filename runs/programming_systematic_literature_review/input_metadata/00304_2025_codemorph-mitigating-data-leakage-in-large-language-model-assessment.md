---
otero_id: "2-s2.0-105008493824"
title: "CODEMORPH: Mitigating Data Leakage in Large Language Model Assessment"
authors: "Rao H.; Zhao Y.; Zhu W.; Xiao L.; Wang M.; Wang H."
year: "2025"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse-companion66252.2025.00081"
---
# Scopus title-abstract-keyword metadata
Title: CODEMORPH: Mitigating Data Leakage in Large Language Model Assessment
Abstract: Concerns about benchmark leakage in large language models for code (Code LLMs) have raised issues of data contamination and inflated evaluation metrics. The diversity and inaccessibility of many training datasets make it difficult to prevent data leakage entirely, even with time lag strategies. Consequently, generating new datasets through code perturbation has become essential. However, existing methods often fail to produce complex and diverse variations, struggle with complex cross-file dependencies, and lack support for multiple programming languages, which limits their effectiveness in enhancing LLM evaluations for coding tasks. To fill this gap, we propose Codemorph, an approach designed to support multiple programming languages while preserving cross-file dependencies to mitigate data leakage. CODEMORPH consists of two main components that work together to enhance the perturbation process. The first component employs 26 semantic-preserving transformation methods to iteratively perturb code, generating diverse variations while ensuring that the modified code remains compilable. The second component introduces a genetic algorithm-based selection algorithm, PESO, to identify the more effective perturbation method for each iteration by targeting lower similarity scores between the perturbed and original code, thereby enhancing overall perturbation effectiveness. Experimental results demonstrate that after applying CODEMORPH, the accuracy of the LLM on code completion tasks across five programming languages decreased by an average of 24.67%, with Python showing the most significant reduction at 45%. The similarity score of code optimized by PESO is, on average, 7.01% lower than that of randomly perturbed code, peaking at a reduction of 42.86%. Additionally, overall accuracy dropped by an average of 15%, with a maximum decrease of 25%. These findings indicate that CODEMORPH effectively reduces data contamination while PESO optimizes perturbation combinations for code. © 2025 IEEE.
Author keywords: 
Index keywords: Benchmarking; Codes (symbols); Computer programming languages; Data reduction; Genetic algorithms; Information leakage; Iterative methods; Perturbation techniques; % reductions; Data leakage; Evaluation metrics; Language model; Model assessment; Selection algorithm; Similarity scores; Time lag; Training dataset; Transformation methods; Semantics
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2025
EID: 2-s2.0-105008493824
DOI: 10.1109/icse-companion66252.2025.00081
Retrieval channels: authoritative_outlet_search
Local full-text files: 

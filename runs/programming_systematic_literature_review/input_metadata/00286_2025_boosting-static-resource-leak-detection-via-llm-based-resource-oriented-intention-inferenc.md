---
otero_id: "2-s2.0-105010330625"
title: "Boosting Static Resource Leak Detection via LLM-based Resource-Oriented Intention Inference"
authors: "Wang C.; Liu J.; Peng X.; Liu Y.; Lou Y."
year: "2025"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse55347.2025.00131"
---
# Scopus title-abstract-keyword metadata
Title: Boosting Static Resource Leak Detection via LLM-based Resource-Oriented Intention Inference
Abstract: Resource leaks, caused by resources not being released after acquisition, often lead to performance issues and system crashes. Existing static detection techniques rely on mechanical matching of predefined resource acquisition/release APIs and null-checking conditions to find unreleased resources, suffering from both (1) false negatives caused by the incompleteness of predefined resource acquisition/release APIs and (2) false positives caused by the incompleteness of resource reachability validation identification. To overcome these challenges, we propose InferROI, a novel approach that leverages the exceptional code comprehension capability of large language models (LLMs) to directly infer resource-oriented intentions (acquisition, release, and reachability validation) in code. InferROI first prompts the LLM to infer involved intentions for a given code snippet, and then incorporates a two-stage static analysis approach to check control-flow paths for resource leak detection based on the inferred intentions. We evaluate the effectiveness of InferROI in both resource-oriented intention inference and resource leak detection. Experimental results on the DroidLeaks and JLeaks datasets demonstrate InferROI achieves promising bug detection rate (59.3% and 62.5%) and false alarm rate (18.6% and 19.5%). Compared to three industrial static detectors, InferROI detects 1445 and 149485 more bugs in DroidLeaks and JLeaks, respectively. When applied to real-world open-source projects, InferROI identifies 29 unknown resource leak bugs (verified by authors), with 7 of them being confirmed by developers. In addition, the results of an ablation study underscores the importance of combining LLM-based inference with static analysis. Finally, manual annotation indicated that InferROI achieved a precision of 74.6% and a recall of 81.8% in intention inference, covering more than 60% resource types involved in the datasets.  © 2025 IEEE.
Author keywords: defect detection; large language models; resource leak detection; static analysis
Index keywords: Codes (symbols); Leak detection; Mergers and acquisitions; Open source software; Open systems; Software testing; Defect detection; Language model; Large language model; Leaks detections; Model-based OPC; Reachability; Resource acquisition; Resource leak detection; Resource leaks; Static resource; Static analysis
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2025
EID: 2-s2.0-105010330625
DOI: 10.1109/icse55347.2025.00131
Retrieval channels: authoritative_outlet_search
Local full-text files: 

---
otero_id: "2-s2.0-85196837383"
title: "GPTScan: Detecting Logic Vulnerabilities in Smart Contracts by Combining GPT with Program Analysis"
authors: "Sun Y.; Wu D.; Xue Y.; Liu H.; Wang H.; Xu Z.; Xie X.; Liu Y."
year: "2024"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3597503.3639117"
---
# Scopus title-abstract-keyword metadata
Title: GPTScan: Detecting Logic Vulnerabilities in Smart Contracts by Combining GPT with Program Analysis
Abstract: Smart contracts are prone to various vulnerabilities, leading to substantial financial losses over time. Current analysis tools mainly target vulnerabilities with fixed control- or data-flow patterns, such as re-entrancy and integer overflow. However, a recent study on Web3 security bugs revealed that about 80% of these bugs cannot be audited by existing tools due to the lack of domain-specific property description and checking. Given recent advances in Large Language Models (LLMs), it is worth exploring how Generative Pre-training Transformer (GPT) could aid in detecting logic vulnerabilities. In this paper, we propose GPTScan, the first tool combining GPT with static analysis for smart contract logic vulnerability detection. Instead of relying solely on GPT to identify vulnerabilities, which can lead to high false positives and is limited by GPT's pre-trained knowledge, we utilize GPT as a versatile code understanding tool. By breaking down each logic vulnerability type into scenarios and properties, GPTScan matches candidate vulnerabilities with GPT. To enhance accuracy, GPTScan further instructs GPT to intelligently recognize key variables and statements, which are then validated by static confirmation. Evaluation on diverse datasets with around 400 contract projects and 3K Solidity files shows that GPTScan achieves high precision (over 90%) for token contracts and acceptable precision (57.14%) for large projects like Web3Bugs. It effectively detects ground-truth logic vulnerabilities with a recall of over 70%, including 9 new vulnerabilities missed by human auditors. GPTScan is fast and cost-effective, taking an average of 14.39 seconds and 0.01 USD to scan per thousand lines of Solidity code. Moreover, static confirmation helps GPTScan reduce two-thirds of false positives.  © 2024 ACM.
Author keywords: 
Index keywords: Computer circuits; Cost effectiveness; Data flow analysis; Large datasets; Losses; Program debugging; Static analysis; Analysis tools; Control-flow; Current analysis; Dataflow; False positive; Financial loss; Integer overflow; Logic Vulnerabilities; Pre-training; Program analysis; Smart contract
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2024
EID: 2-s2.0-85196837383
DOI: 10.1145/3597503.3639117
Retrieval channels: authoritative_outlet_search
Local full-text files: 

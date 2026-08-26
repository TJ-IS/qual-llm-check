---
otero_id: "2-s2.0-105041024499"
title: "ParityFuzz: Finding inconsistencies across solidity compilers via fine-grained mutation and differential analysis"
authors: "Su B.; Ye M.; Nan Y.; Zheng P.; Zheng Z."
year: "2026"
journal: "Journal of Systems and Software"
doi: "10.1016/j.jss.2026.112927"
---
# Scopus title-abstract-keyword metadata
Title: ParityFuzz: Finding inconsistencies across solidity compilers via fine-grained mutation and differential analysis
Abstract: The Solidity smart contract ecosystem has rapidly grown, leading to multiple compilers targeting different blockchain platforms or offering improved compilation efficiency. Although many compilers aim to be compatible with the primary Solidity compiler (Solc), significant inconsistencies in compilation and execution remain. These inconsistencies hinder contract migration, mislead developers during debugging, and may introduce exploitable vulnerabilities, causing potential financial losses. Existing testing techniques mainly focus on bugs within a single compiler or perform differential testing across compilers targeting the same environment. However, these approaches are inadequate for detecting inconsistencies across Solidity compilers, as they lack mechanisms to explore inconsistency-triggering conditions and do not support comparing bytecode generated for different environments. To address this gap, we propose ParityFuzz, a cross-compiler differential testing framework for Solidity. ParityFuzz operates in three stages. First, it generates a rich set of mutation rules (i.e., syntax-oriented and boundary-oriented mutation rules) by analyzing source code (i.e., compiler and execution environment). Second, it employs a reinforcement learning-based strategy to select the most promising rules for mutating test programs. Finally, it detects inconsistencies by compiling and executing these programs on multiple compilers, then normalizing and comparing their results. Our evaluation demonstrates that ParityFuzz is both efficient and effective. It improves test program generation, achieving up to an 18× higher compilation success rate and 1.8× greater code coverage compared to state-of-the-art fuzzers. In total, ParityFuzz has uncovered 64 previously unknown inconsistencies across six popular compilers. Notably, our findings have led to 11 fixes by developers and received a bounty from the Polkadot community. © 2026 Elsevier Inc.
Author keywords: Blockchain; Fuzzing; Smart contract; Solidity compiler
Index keywords: Differential equations; Ecosystems; Losses; Program compilers; Program debugging; Smart contract; Software testing; Test facilities; Block-chain; Differential analysis; Differential testing; Financial loss; Fine grained; Fuzzing; Mutation analysis; Solidity compiler; Test projects; Testing technique; Blockchain
Document type: Article
Conference: 
Source title: Journal of Systems and Software
Year: 2026
EID: 2-s2.0-105041024499
DOI: 10.1016/j.jss.2026.112927
Retrieval channels: authoritative_outlet_search
Local full-text files: 

---
otero_id: "2-s2.0-105011543835"
title: "ACFix: Guiding LLMs With Mined Common RBAC Practices for Context-Aware Repair of Access Control Vulnerabilities in Smart Contracts"
authors: "Zhang L.; Li K.; Sun K.; Wu D.; Liu Y.; Tian H.; Liu Y."
year: "2025"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2025.3590108"
---
# Scopus title-abstract-keyword metadata
Title: ACFix: Guiding LLMs With Mined Common RBAC Practices for Context-Aware Repair of Access Control Vulnerabilities in Smart Contracts
Abstract: Smart contracts are susceptible to various security issues, among which access control (AC) vulnerabilities are particularly critical. While existing research has proposed multiple detection tools, automatic and appropriate repair of AC vulnerabilities in smart contracts remains a challenge. Unlike commonly supported vulnerability types by existing repair tools, such as reentrancy, which are usually fixed by template-based approaches, the main obstacle of repairing AC vulnerabilities lies in identifying the appropriate roles or permissions amid a long list of non-AC-related source code to generate proper patch code, a task that demands human-level intelligence. In this paper, we employ the state-of-the-art GPT-4 model and enhance it with a novel approach called ACFix. The key insight is that we can mine common AC practices for major categories of code functionality and use them to guide LLMs in fixing code with similar functionality. To this end, ACFix involves offline and online phases. In the offline phase, ACFix mines a taxonomy of common Role-based Access Control practices from 344,251 on-chain contracts, categorizing 49 role-permission pairs from the top 1,000 unique samples. In the online phase, ACFix tracks AC-related elements across the contract and uses this context information along with a Chain-of-Thought pipeline to guide LLMs in identifying the most appropriate role-permission pair for the subject contract and subsequently generating a suitable patch. To evaluate ACFix, we built the first benchmark dataset of 118 real-world AC vulnerabilities, and our evaluation revealed that ACFix successfully repaired 94.92% of them, a major improvement compared to the baseline GPT-4 at only 52.54%. We also conducted a human study to understand the value of ACFix's repairs and their differences from human repairs.  © 2025 IEEE.
Author keywords: program repair; Smart contract; software security
Index keywords: Access control; Chains; Human computer interaction; Job analysis; Network security; Repair; Smart contract; Tools; Context-Aware; Detection tools; Multiple detection; Offline; Program repair; Repair tools; Security issues; Software security; Source codes; Template-based approaches; Codes (symbols)
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2025
EID: 2-s2.0-105011543835
DOI: 10.1109/tse.2025.3590108
Retrieval channels: authoritative_outlet_search
Local full-text files: 

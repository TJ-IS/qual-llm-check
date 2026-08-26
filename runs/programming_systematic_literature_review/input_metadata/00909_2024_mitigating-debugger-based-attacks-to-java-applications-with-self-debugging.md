---
otero_id: "2-s2.0-85191581426"
title: "Mitigating Debugger-based Attacks to Java Applications with Self-debugging"
authors: "Pizzolotto D.; Berlato S.; Ceccato M."
year: "2024"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3631971"
---
# Scopus title-abstract-keyword metadata
Title: Mitigating Debugger-based Attacks to Java Applications with Self-debugging
Abstract: Java bytecode is a quite high-level language and, as such, it is fairly easy to analyze and decompile with malicious intents, e.g., to tamper with code and skip license checks. Code obfuscation was a first attempt to mitigate malicious reverse-engineering based on static analysis. However, obfuscated code can still be dynamically analyzed with standard debuggers to perform step-wise execution and to inspect (or change) memory content at important execution points, e.g., to alter the verdict of license validity checks. Although some approaches have been proposed to mitigate debugger-based attacks, they are only applicable to binary compiled code and none address the challenge of protecting Java bytecode. In this article, we propose a novel approach to protect Java bytecode from malicious debugging. Our approach is based on automated program transformation to manipulate Java bytecode and split it into two binary processes that debug each other (i.e., a self-debugging solution). In fact, when the debugging interface is already engaged, an additional malicious debugger cannot attach. To be resilient against typical attacks, our approach adopts a series of technical solutions, e.g., an encoded channel is shared by the two processes to avoid leaking information, an authentication protocol is established to avoid Man-in-the-middle attacks, and the computation is spread between the two processes to prevent the attacker to replace or terminate either of them. We test our solution on 18 real-world Java applications, showing that our approach can effectively block the most common debugging tasks (either with the Java debugger or the GNU debugger) while preserving the functional correctness of the protected programs. While the final decision on when to activate this protection is still up to the developers, the observed performance overhead was acceptable for common desktop application domains. © 2024 Copyright held by the owner/author(s).
Author keywords: Anti-debugging; maliciuos reverse engineering; man at the end attacks; tampering attacks
Index keywords: Application programs; Data obfuscation; High level languages; Java programming language; Network security; Open source software; Program debugging; Reverse engineering; Anti-debugging; Debuggers; High-level language; Higher-level languages; Java applications; Java byte codes; Maliciuos reverse engineering; Man at the end attack; Self-debugging; Tampering attacks; Static analysis
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2024
EID: 2-s2.0-85191581426
DOI: 10.1145/3631971
Retrieval channels: authoritative_outlet_search
Local full-text files: 

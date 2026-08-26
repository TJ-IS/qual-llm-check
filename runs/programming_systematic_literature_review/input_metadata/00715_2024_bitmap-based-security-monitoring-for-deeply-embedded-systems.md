---
otero_id: "2-s2.0-85206216630"
title: "Bitmap-Based Security Monitoring for Deeply Embedded Systems"
authors: "Peng A.; Fang D.; Guan L.; van der Kouwe E.; Li Y.; Wang W.; Sun L.; Zhang Y."
year: "2024"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3672460"
---
# Scopus title-abstract-keyword metadata
Title: Bitmap-Based Security Monitoring for Deeply Embedded Systems
Abstract: Deeply embedded systems powered by microcontrollers are becoming popular with the emergence of Internet-of-Things (IoT) technology. However, these devices primarily run C/C++ code and are susceptible to memory bugs, which can potentially lead to both control data attacks and non-control data attacks. Existing defense mechanisms (such as control-flow integrity (CFI), dataflow integrity (DFI) and write integrity testing (WIT), etc.) consume a massive amount of resources, making them less practical in real products. To make it lightweight, we design a bitmap-based allowlist mechanism to unify the storage of the runtime data for protecting both control data and non-control data. The memory requirements are constant and small, regardless of the number of deployed defense mechanisms. We store the allowlist in the TrustZone to ensure its integrity and confidentiality. Meanwhile, we perform an offline analysis to detect potential collisions and make corresponding adjustments when it happens. We have implemented our idea on an ARM Cortex-M-based development board. Our evaluation results show a substantial reduction in memory consumption when deploying the proposed CFI and DFI mechanisms, without compromising runtime performance. Specifically, our prototype enforces CFI and DFI at a cost of just 2.09% performance overhead and 32.56% memory overhead on average. © 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: CFI; DFI; microcontroller; TEE
Index keywords: Associative storage; C++ (programming language); Data flow analysis; Network security; Nonvolatile storage; Program debugging; Bit maps; Control data; Control-flow integrities; Dataflow; Dataflow integrity; Defence mechanisms; Embedded-system; Internet of things technologies; Security monitoring; TEE; Microcontrollers
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2024
EID: 2-s2.0-85206216630
DOI: 10.1145/3672460
Retrieval channels: authoritative_outlet_search
Local full-text files: 

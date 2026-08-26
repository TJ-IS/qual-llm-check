---
otero_id: "2-s2.0-85204227766"
title: "Retrieving API Knowledge from Tutorials and Stack Overflow Based on Natural Language Queries"
authors: "Wu D.; Jing X.-Y.; Zhang H.; Feng Y.; Chen H.; Zhou Y.; Xu B."
year: "2023"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3565799"
---
# Scopus title-abstract-keyword metadata
Title: Retrieving API Knowledge from Tutorials and Stack Overflow Based on Natural Language Queries
Abstract: When encountering unfamiliar APIs, developers tend to seek help from API tutorials and Stack Overflow (SO). API tutorials help developers understand the API knowledge in a general context, while SO often explains the API knowledge in a specific programming task. Thus, tutorials and SO posts together can provide more API knowledge. However, it is non-trivial to retrieve API knowledge from both API tutorials and SO posts based on natural language queries. Two major problems are irrelevant API knowledge in two different resources and the lexical gap between the queries and documents. In this article, we regard a fragment in tutorials and a Question and Answering (Q&A) pair in SO as a knowledge item (KI). We generate ⟨ API, FRA⟩ pairs (FRA stands for fragment) from tutorial fragments and APIs and build ⟨ API, QA⟩ pairs based on heuristic rules of SO posts. We fuse ⟨ API, FRA⟩ pairs and ⟨ API, QA⟩ pairs to generate API knowledge (AK for short) datasets, where each data item is an ⟨API, KI⟩ pair. We propose a novel approach, called PLAN, to automatically retrieve API knowledge from both API tutorials and SO posts based on natural language queries. PLAN contains three main stages: (1) API knowledge modeling, (2) query mapping, and (3) API knowledge retrieving. It first utilizes a deep-transfer-metric-learning-based relevance identification (DTML) model to effectively find relevant ⟨ API, KI⟩ pairs containing two different knowledge items (⟨ API, QA⟩ pairs and ⟨ API, FRA⟩ pairs) simultaneously. Then, PLAN generates several potential APIs as a way to reduce the lexical gap between the query and ⟨ API, KI⟩ pairs. According to potential APIs, we can select relevant ⟨ API, KI⟩ pairs to generate potential results. Finally, PLAN returns a list of ranked ⟨ API, KI⟩ pairs that are related to the query. We evaluate the effectiveness of PLAN with 270 queries on Java and Android AK datasets containing 10,072 ⟨ API, KI⟩ pairs. Our experimental results show that PLAN is effective and outperforms the state-of-the-art approaches. Our user study further confirms the effectiveness of PLAN in locating useful API knowledge. © 2023 Association for Computing Machinery.
Author keywords: 
Index keywords: Java programming language; Query languages; Data items; Heuristic rules; Identification modeling; Knowledge items; Knowledge model; Metric learning; Natural language queries; Non-trivial; Programming tasks; Stack overflow; Structured Query Language
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2023
EID: 2-s2.0-85204227766
DOI: 10.1145/3565799
Retrieval channels: authoritative_outlet_search
Local full-text files: 

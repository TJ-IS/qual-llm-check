---
otero_id: "2-s2.0-85196804502"
title: "Finding XPath Bugs in XML Document Processors via Differential Testing"
authors: "Li S.; Rigger M."
year: "2024"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3597503.3639208"
---
# Scopus title-abstract-keyword metadata
Title: Finding XPath Bugs in XML Document Processors via Differential Testing
Abstract: Extensible Markup Language (XML) is a widely used file format for data storage and transmission. Many XML processors support XPath, a query language that enables the extraction of elements from XML documents. These systems can be affected by logic bugs, which are bugs that cause the processor to return incorrect results. In order to tackle such bugs, we propose a new approach, which we realized as a system called XPress. As a test oracle, XPress relies on differential testing, which compares the results of multiple systems on the same test input, and identifies bugs through discrepancies in their outputs. As test inputs, XPress generates both XML documents and XPath queries. Aiming to generate meaningful queries that compute non-empty results, XPress selects a so-called targeted node to guide the XPath expression generation process. Using the targeted node, XPress generates XPath expressions that reference existing context related to the targeted node, such as its tag name and attributes, while also guaranteeing that a predicate evaluates to true before further expanding the query. We tested our approach on six mature XML processors, BaseX, eXist-DB, Saxon, PostgreSQL, libXML2, and a commercial database system. In total, we have found 27 unique bugs in these systems, of which 25 have been verified by the developers, and 20 of which have been fixed. XPress is efficient, as it finds 12 unique bugs in BaseX in 24 hours, which is 2× as fast as naive random generation. We expect that the effectiveness and simplicity of our approach will help to improve the robustness of many XML processors.  © 2024 ACM.
Author keywords: differential testing; XML processors; XPath generation
Index keywords: Digital storage; Hypertext systems; Program debugging; Query languages; Query processing; Data storage; Data-transmission; Differential testing; File formats; New approaches; Test inputs; Test oracles; XML processor; XPath expressions; Xpath generation; XML
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2024
EID: 2-s2.0-85196804502
DOI: 10.1145/3597503.3639208
Retrieval channels: authoritative_outlet_search
Local full-text files: 

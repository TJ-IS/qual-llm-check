---
otero_id: "2-s2.0-85101749383"
title: "Studying Duplicate Logging Statements and Their Relationships with Code Clones"
authors: "Li Z.; Chen T.-H.; Yang J.; Shang W."
year: "2022"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2021.3060918"
---
# Scopus title-abstract-keyword metadata
Title: Studying Duplicate Logging Statements and Their Relationships with Code Clones
Abstract: Developers rely on software logs for a variety of tasks, such as debugging, testing, program comprehension, verification, and performance analysis. Despite the importance of logs, prior studies show that there is no industrial standard on how to write logging statements. In this paper, we focus on studying duplicate logging statements, which are logging statements that have the same static text message. Such duplications in the text message are potential indications of logging code smells, which may affect developers' understanding of the dynamic view of the system. We manually studied over 4K duplicate logging statements and their surrounding code in five large-scale open source systems: Hadoop, CloudStack, Elasticsearch, Cassandra, and Flink. We uncovered five patterns of duplicate logging code smells. For each instance of the duplicate logging code smell, we further manually identify the potentially problematic (i.e., require fixes) and justifiable (i.e., do not require fixes) cases. Then, we contact developers to verify our manual study result. We integrated our manual study result and developers' feedback into our automated static analysis tool, DLFinder, which automatically detects problematic duplicate logging code smells. We evaluated DLFinder on the five manually studied systems and three additional systems: Camel, Kafka and Wicket. In total, combining the results of DLFinder and our manual analysis, we reported 91 problematic duplicate logging code smell instances to developers and all of them have been fixed. We further study the relationship between duplicate logging statements, including the problematic instances of duplicate logging code smells, and code clones. We find that 83 percent of the duplicate logging code smell instances reside in cloned code, but 17 percent of them reside in micro-clones that are difficult to detect using automated clone detection tools. We also find that more than half of the duplicate logging statements reside in cloned code snippets, and a large portion of them reside in very short code blocks which may not be effectively detected by existing code clone detection tools. Our study shows that, in addition to general source code that implements the business logic, code clones may also result in bad logging practices that could increase maintenance difficulties. © 1976-2012 IEEE.
Author keywords: Code clone; Code smell; Duplicate log; Empirical study; Log; Static analysis
Index keywords: Cloning; Inspection equipment; Odors; Open source software; Program debugging; Software testing; Static analysis; Verification; Business logic; Clone detection; Code clone detection; Industrial standards; Manual analysis; Open source system; Performance analysis; Program comprehension; Open systems
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2022
EID: 2-s2.0-85101749383
DOI: 10.1109/tse.2021.3060918
Retrieval channels: authoritative_outlet_search
Local full-text files: 

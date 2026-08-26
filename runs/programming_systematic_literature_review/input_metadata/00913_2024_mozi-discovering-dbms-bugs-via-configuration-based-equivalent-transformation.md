---
otero_id: "2-s2.0-85195646577"
title: "Mozi: Discovering DBMS Bugs via Configuration-Based Equivalent Transformation"
authors: "Liang J.; Wu Z.; Fu J.; Wang M.; Sun C.; Jiang Y."
year: "2024"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3597503.3639112"
---
# Scopus title-abstract-keyword metadata
Title: Mozi: Discovering DBMS Bugs via Configuration-Based Equivalent Transformation
Abstract: Testing database management systems (DBMSs) is a complex task. Traditional approaches, such as metamorphic testing, need a precise comprehension of the SQL specification to create diverse inputs with equivalent semantics. The vagueness and intricacy of the SQL specification make it challenging to accurately model query semantics, thereby posing difficulties in testing the correctness and performance of DBMSs. To address this, we propose Mozi, a framework that finds DBMS bugs via configuration-based equivalent transformation. The key idea behind Mozi is to compare the results of equivalent DBMSs with different configurations, rather than between semantically equivalent queries. The framework involves analyzing the query plan, changing configurations to transform the DBMS to an equivalent one, and re-executing the query to compare the results using various test oracles. For example, detecting differences in query results indicates correctness bugs, while observing faster execution times on the optimization-closed DBMS suggests performance bugs. We demonstrate the effectiveness of Mozi by evaluating it on four widely used DBMSs, namely MySQL, MariaDB, Clickhouse, and PostgreSQL. In the continuous testing, Mozi found a total of 101 previously unknown bugs, including 49 correctness and 52 performance bugs in four DBMSs. Among them, 90 bugs are confirmed and 57 bugs have been fixed. In addition, Mozi can be extended to other DBMS fuzzers for testing various types of bugs. With Mozi, testing DBMSs becomes simpler and more effective, potentially saving time and effort that would otherwise be spent on precisely modeling SQL specifications for testing purposes.  © 2024 ACM.
Author keywords: Configuration; DBMS Testing; Software and its engineering → Software testing and debugging; Test Oracle
Index keywords: Program debugging; Query processing; Semantics; Software testing; Specifications; Complex task; Configuration; Database management system testing; Engineering software; Equivalent transformations; Performance bugs; Software and its engineering → software testing and debugging; Software Testing and Debugging; System testing; Test oracles; Database systems
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2024
EID: 2-s2.0-85195646577
DOI: 10.1145/3597503.3639112
Retrieval channels: authoritative_outlet_search
Local full-text files: 

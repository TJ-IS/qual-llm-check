---
otero_id: "2-s2.0-85171792487"
title: "Testing Database Engines via Query Plan Guidance"
authors: "Ba J.; Rigger M."
year: "2023"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse48619.2023.00174"
---
# Scopus title-abstract-keyword metadata
Title: Testing Database Engines via Query Plan Guidance
Abstract: Database systems are widely used to store and query data. Test oracles have been proposed to find logic bugs in such systems, that is, bugs that cause the database system to compute an incorrect result. To realize a fully automated testing approach, such test oracles are paired with a test case generation technique; a test case refers to a database state and a query on which the test oracle can be applied. In this work, we propose the concept of Query Plan Guidance (QPG) for guiding automated testing towards 'interesting' test cases. SQL and other query languages are declarative. Thus, to execute a query, the database system translates every operator in the source language to one of the potentially many so-called physical operators that can be executed; the tree of physical operators is referred to as the query plan. Our intuition is that by steering testing towards exploring a variety of unique query plans, we also explore more interesting behaviors-some of which are potentially incorrect. To this end, we propose a mutation technique that gradually applies promising mutations to the database state, causing the DBMS to create potentially unseen query plans for subsequent queries. We applied our method to three mature, widely-used, and extensively-tested database systems-SQLite, TiDB, and CockroachDB-and found 53 unique, previously unknown bugs. Our method exercises 4.85-408.48× more unique query plans than a naive random generation method and 7.46× more than a code coverage guidance method. Since most database systems-including commercial ones-expose query plans to the user, we consider QPG a generally applicable, black-box approach and believe that the core idea could also be applied in other contexts (e.g., to measure the quality of a test suite). © 2023 IEEE.
Author keywords: automated testing; test case generation
Index keywords: Automation; Program debugging; Query languages; Trees (mathematics); Automated testing; Database engine; Fully automated; Generation techniques; Query datum; Random generation; Source language; Test case; Test case generation; Test oracles; Query processing
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2023
EID: 2-s2.0-85171792487
DOI: 10.1109/icse48619.2023.00174
Retrieval channels: authoritative_outlet_search
Local full-text files: 

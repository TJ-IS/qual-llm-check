---
otero_id: "2-s2.0-85021744825"
title: "A system for profiling and monitoring database access patterns by application programs for anomaly detection"
authors: "Bossi L.; Bertino E.; Hussain S.R."
year: "2017"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2016.2598336"
---
# Scopus title-abstract-keyword metadata
Title: A system for profiling and monitoring database access patterns by application programs for anomaly detection
Abstract: Database Management Systems (DBMSs) provide access control mechanisms that allow database administrators (DBAs) to grant application programs access privileges to databases. Though such mechanisms are powerful, in practice finer-grained access control mechanism tailored to the semantics of the data stored in the DMBS is required as a first class defense mechanism against smart attackers. Hence, custom written applications which access databases implement an additional layer of access control. Therefore, securing a database alone is not enough for such applications, as attackers aiming at stealing data can take advantage of vulnerabilities in the privileged applications and make these applications to issue malicious database queries. An access control mechanism can only prevent application programs from accessing the data to which the programs are not authorized, but it is unable to prevent misuse of the data to which application programs are authorized for access. Hence, we need a mechanism able to detect malicious behavior resulting from previously authorized applications. In this paper, we present the architecture of an anomaly detection mechanism, DetAnom, that aims to solve such problem. Our approach is based the analysis and profiling of the application in order to create a succinct representation of its interaction with the database. Such a profile keeps a signature for every submitted query and also the corresponding constraints that the application program must satisfy to submit the query. Later, in the detection phase, whenever the application issues a query, a module captures the query before it reaches the database and verifies the corresponding signature and constraints against the current context of the application. If there is a mismatch, the query is marked as anomalous. The main advantage of our anomaly detection mechanism is that, in order to build the application profiles, we need neither any previous knowledge of application vulnerabilities nor any example of possible attacks. As a result, our mechanism is able to protect the data from attacks tailored to database applications such as code modification attacks, SQL injections, and also from other data-centric attacks as well. We have implemented our mechanism with a software testing technique called concolic testing and the PostgreSQL DBMS. Experimental results show that our profiling technique is close to accurate, requires acceptable amount of time, and the detection mechanism incurs low runtime overhead. © 2016 IEEE.
Author keywords: Anomaly detection; Application profile; Database; Insider attacks; SQL injection
Index keywords: Access control; Computer software; Database systems; Query languages; Query processing; Semantics; Signal detection; Software testing; Testing; Access control mechanism; Anomaly detection; Database administrators; Database applications; Insider attack; Software testing techniques; SQL injection; Succinct representation; Application programs
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2017
EID: 2-s2.0-85021744825
DOI: 10.1109/tse.2016.2598336
Retrieval channels: authoritative_outlet_search
Local full-text files: 

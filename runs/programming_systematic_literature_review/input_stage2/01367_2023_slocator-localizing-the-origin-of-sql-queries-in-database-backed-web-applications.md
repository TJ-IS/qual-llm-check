---
otero_id: "2-s2.0-85149823797"
title: "SLocator: Localizing the Origin of SQL Queries in Database-Backed Web Applications"
authors: "Liu W.; Chen T.-H."
year: "2023"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2023.3253700"
---
# Scopus title-abstract-keyword metadata
Title: SLocator: Localizing the Origin of SQL Queries in Database-Backed Web Applications
Abstract: In database-backed web applications, developers often leverage Object-Relational Mapping (ORM) frameworks for database accesses. ORM frameworks provide an abstraction of the underlying database access details so that developers can focus on implementing the business logic of the application. However, due to the abstraction, developers may not know where and how a problematic SQL query is generated in the application code, causing challenges in debugging database access problems. In this paper, we propose an approach, called SLocator, which locates where a SQL query is generated in the application code. SLocator is a hybrid approach that leverages both static analysis and information retrieval (IR) techniques. SLocator uses static analysis to infer the database access for every possible path in the control flow graph. Then, given a SQL query, SLocator applies IR techniques to find the control flow path (i.e., a sequence of methods called in an interprocedural control flow graph) whose inferred database access has the highest similarity ranking. We implement SLocator for Java's official ORM API specification (JPA) and evaluate SLocator on seven open source Java applications. We find that SLocator is able to locate the control flow path that generates a SQL query with a Top@1 accuracy ranging from 37.4% to 70% for SQL queries in sessions, and 30.7% to 69.2% for individual SQL queries; and Top@5 ranging from 78.3% to 95.5% for SQL queries in sessions, and 59.1% to 100% for individual SQL queries. We also conduct a study to illustrate how SLocator may be used for locating issues in the database access code.  © 1976-2012 IEEE.
Author keywords: Information retrieval; localization; object-relational mapping; static analysis
Index keywords: Abstracting; Codes (symbols); Data flow analysis; Flow graphs; Java programming language; Mapping; Open source software; Program debugging; Query languages; Query processing; Static analysis; Code; Computer bugs; Database access; Java; Localisation; Location awareness; Object-relational mapping; SQL query; WEB application; Web applications; Information retrieval
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2023
EID: 2-s2.0-85149823797
DOI: 10.1109/tse.2023.3253700
Retrieval channels: authoritative_outlet_search
Local full-text files: 

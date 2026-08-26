---
otero_id: "2-s2.0-85009892148"
title: "Nopol: Automatic Repair of Conditional Statement Bugs in Java Programs"
authors: "Xuan J.; Martinez M.; DeMarco F.; Clement M.; Marcote S.L.; Durieux T.; Le Berre D.; Monperrus M."
year: "2017"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2016.2560811"
---
# Scopus title-abstract-keyword metadata
Title: Nopol: Automatic Repair of Conditional Statement Bugs in Java Programs
Abstract: We propose Nopol, an approach to automatic repair of buggy conditional statements (i.e., if-then-else statements). This approach takes a buggy program as well as a test suite as input and generates a patch with a conditional expression as output. The test suite is required to contain passing test cases to model the expected behavior of the program and at least one failing test case that reveals the bug to be repaired. The process of Nopol consists of three major phases. First, Nopol employs angelic fix localization to identify expected values of a condition during the test execution. Second, runtime trace collection is used to collect variables and their actual values, including primitive data types and objected-oriented features (e.g., nullness checks), to serve as building blocks for patch generation. Third, Nopol encodes these collected data into an instance of a Satisfiability Modulo Theory (SMT) problem; then a feasible solution to the SMT instance is translated back into a code patch. We evaluate Nopol on 22 real-world bugs (16 bugs with buggy if conditions and six bugs with missing preconditions) on two large open-source projects, namely Apache Commons Math and Apache Commons Lang. Empirical analysis on these bugs shows that our approach can effectively fix bugs with buggy if conditions and missing preconditions. We illustrate the capabilities and limitations of Nopol using case studies of real bug fixes. © 1976-2012 IEEE.
Author keywords: Automatic repair; fault localization; patch generation; SMT
Index keywords: Computer software; Java programming language; Open source software; Repair; Software testing; Surface mount technology; Conditional expressions; Empirical analysis; Fault localization; Feasible solution; Open source projects; Oriented features; patch generation; Satisfiability modulo Theories; Program debugging
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2017
EID: 2-s2.0-85009892148
DOI: 10.1109/tse.2016.2560811
Retrieval channels: authoritative_outlet_search
Local full-text files: 

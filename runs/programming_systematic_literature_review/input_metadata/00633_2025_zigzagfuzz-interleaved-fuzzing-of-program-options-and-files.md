---
otero_id: "2-s2.0-85218336971"
title: "ZigZagFuzz: Interleaved Fuzzing of Program Options and Files"
authors: "Lee A.; Choi Y.; Hong S.; Kim Y.; Cho K.; Kim M."
year: "2025"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3697014"
---
# Scopus title-abstract-keyword metadata
Title: ZigZagFuzz: Interleaved Fuzzing of Program Options and Files
Abstract: Command-line options (e.g., -l, -F, -R for ls) given to a command-line program can significantly alternate the behaviors of the program. Thus, fuzzing not only file input but also program options can improve test coverage and bug detection. In this article, we propose ZigZagFuzz which achieves higher test coverage and detects more bugs than the state-of-the-art fuzzers by separately mutating program options and file inputs in an iterative/interleaving manner. ZigZagFuzz applies the following three core ideas. First, to utilize different characteristics of the program option domain and the file input domain, ZigZagFuzz separates phases of mutating program options from ones of mutating file inputs and performs two distinct mutation strategies on the two different domains. Second, to reach deep segments of a target program that are accessed through an interleaving sequence of program option checks and file inputs checks, ZigZagFuzz continuously interleaves phases of mutating program options with phases of mutating file inputs. Finally, to improve fuzzing performance further, ZigZagFuzz periodically shrinks input corpus by removing similar test inputs based on their function coverage. The experiment results on the 20 real-world programs show that ZigZagFuzz improves test coverage and detects 1.9 to 10.6 times more bugs than the state-of-the-art fuzzers that mutate program options such as AFL++-argv, AFL++-all, Eclipser, CarpetFuzz, ConfigFuzz, and POWER. We have reported the new bugs detected by ZigZagFuzz, and the original developers confirmed our bug reports.  Copyright © 2025 held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: Automated test generation; bug detection; command-line program options; dynamic analysis; fuzzing
Index keywords: Automatic test pattern generation; Input output programs; Program debugging; Automated test generations; Bug detection; Command line; Command line programs; Command-line program option; Dynamics analysis; Fuzzing; Interleavings; State of the art; Test-coverage; Software testing
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2025
EID: 2-s2.0-85218336971
DOI: 10.1145/3697014
Retrieval channels: authoritative_outlet_search
Local full-text files: 

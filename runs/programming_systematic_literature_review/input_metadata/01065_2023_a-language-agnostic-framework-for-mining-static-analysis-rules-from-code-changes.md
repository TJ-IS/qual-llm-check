---
otero_id: "2-s2.0-85171773836"
title: "A Language-agnostic Framework for Mining Static Analysis Rules from Code Changes"
authors: "Effendi S.D.B.; Cirisci B.; Mukherjee R.; Nguyen H.A.; Tripp O."
year: "2023"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse-seip58684.2023.00035"
---
# Scopus title-abstract-keyword metadata
Title: A Language-agnostic Framework for Mining Static Analysis Rules from Code Changes
Abstract: Static analysis tools detect a wide range of code defects, including code quality issues, security vulnerabilities, operational risks, and best-practice violations. Creating and maintaining a set of high-quality static analysis rules that detect misuses of popular libraries and SDKs across multiple languages is challenging. One of the mechanisms for inferring static analysis rules is by leveraging frequently occurring bug-fix code changes in the wild that are committed by multiple developers and into different software repositories. The intuition is that code changes following a common pattern correspond to recurring mistakes, from which deriving best practices could likely be of high value and accepted by the community.Automating the process of mining and clustering code changes enables a scalable mechanism to source and generate best-practices rules. From a coverage standpoint, the rules are derived from real-world code changes, which ensures that popular libraries and application domains are accounted for.In this paper, we present a language-agnostic framework for mining and clustering code changes from software repositories using a graph-based representation dubbed MU (μ). Unlike language-specific ASTs, the MU representation generalizes across languages by modeling programs at a higher semantic level, which enables grouping of code changes that are semantically similar yet syntactically distinct. We have mined a total of 62 high-quality static analysis rules across Java, JavaScript, and Python from less than 600 code change clusters. These cover multiple libraries, including the AWS Java and Python SDKs, as well as libraries like pandas, React, Android libraries, Json parsing libraries, and many more. These rules are integrated into a cloud-based static analyzer, Amazon CodeGuru Reviewer. Developers have accepted 73% of recommendations from these rules during code review, which signifies the value of these rules to help improve developer productivity, make code secure, and improve code hygiene. © 2023 IEEE.
Author keywords: clustering; coding best practices; mining software repository; program synthesis; static analysis
Index keywords: Graphic methods; High level languages; Java programming language; Libraries; Modeling languages; Quality control; Risk assessment; Semantics; Analysis rules; Best practices; Clusterings; Code changes; Coding best practice; High quality; Mining software; Mining software repository; Program synthesis; Software repositories; Static analysis
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2023
EID: 2-s2.0-85171773836
DOI: 10.1109/icse-seip58684.2023.00035
Retrieval channels: authoritative_outlet_search
Local full-text files: 

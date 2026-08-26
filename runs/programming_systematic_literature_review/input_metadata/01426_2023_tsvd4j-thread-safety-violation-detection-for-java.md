---
otero_id: "2-s2.0-85171888626"
title: "TSVD4J: Thread-Safety Violation Detection for Java"
authors: "Rahman S.; Li C.; Shi A."
year: "2023"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse-companion58688.2023.00029"
---
# Scopus title-abstract-keyword metadata
Title: TSVD4J: Thread-Safety Violation Detection for Java
Abstract: Concurrency bugs are difficult to detect and debug. One class of concurrency bugs are thread-safety violations, where multiple threads access thread-unsafe data structure at the same time, resulting in unexpected behavior. Prior work proposed an approach TSVD to detect thread-safety violations. TSVD injects delays at API calls that read/write to specific thread-unsafe data structures, tracking whether multiple threads can overlap in their accesses to the same data structure through the delays, showing potential thread-safety violations. We additionally enhance the TSVD approach to also consider read/write operations to object fields. We implement the TSVD approach in Java in our tool TSVD4J. TSVD4J can be integrated as a Maven plugin that can be included in any Maven-based application. Our evaluation on 12 applications shows that TSVD4J can detect 55 pairs of code locations accessing the same shared data structure across multiple threads, representing potential thread-safety violations. We find that the addition of tracking field accesses contributed the most to detecting these pairs. TSVD4J also detects more such pairs than existing tool RV-Predict. The demo video for TSVD4J is available at https://www.youtube.com/watchv-wSMzlj5cMY © 2023 IEEE.
Author keywords: Concurrency Bugs; Data Race; Thread Safety Violations
Index keywords: Java programming language; Program debugging; API calls; Concurrency bugs; Data races; Multiple threads; Plug-ins; Read/write operations; Safety violations; Thread safeties; Thread safety violation; Violation detections; Data structures
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2023
EID: 2-s2.0-85171888626
DOI: 10.1109/icse-companion58688.2023.00029
Retrieval channels: authoritative_outlet_search
Local full-text files: 

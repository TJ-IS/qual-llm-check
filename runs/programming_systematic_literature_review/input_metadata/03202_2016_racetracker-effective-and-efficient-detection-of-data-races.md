---
otero_id: "2-s2.0-84983371613"
title: "RaceTracker: Effective and efficient detection of data races"
authors: "Yang Z.; Yu Z.; Su X.; Ma P."
year: "2016"
journal: "2016 IEEE/ACIS 17th International Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing, SNPD 2016"
doi: "10.1109/snpd.2016.7515908"
---
# Scopus title-abstract-keyword metadata
Title: RaceTracker: Effective and efficient detection of data races
Abstract: Data races are common concurrency bugs in multi-threaded programs and many of them can cause server failures. They are difficult to be detected or verified due to some non-deterministic interleavings. Numerous static and dynamic program analysis techniques have been proposed to detect data races. However, some of detectors may report large amount of false races and some of them may miss lots of true races. This paper proposes RaceTracker that combines static and dynamic techniques to detect data races effectively and efficiently. First, we use current static detectors to produce potential races and identify ad-hoc synchronizations. Second, we instrument code locations corresponding to potential races to try best to expose them in controlled thread interleavings. Meanwhile, we apply the hybrid dynamic detection techniques to detect races in case they are exposed. Finally, we also apply the hybrid dynamic detection techniques to prune benign and false races mainly caused by ad-hoc synchronization. In order to increase the chances to trigger real race conditions in dynamic analysis, we use some strategies to control the schedule of threads. We have implemented our tool RaceTracker in the dynamic binary instrumentation framework PIN and evaluated with nearly 100 small data race programs from google data-race-test suit and some real-world concurrent applications from SPLASH-2 and Maple. Evaluations show that RaceTracker can identify more data races effectively compared with prior pure dynamic race verifiers and detectors. Meanwhile, compared with grouping verifier, RaceTracker only executes the program twice and reduces the average runtime overhead by 64%. © 2016 IEEE.
Author keywords: ad-hoc synchronization; concurrency bugs; data race; dynamic detection; dynamic verification; static analysis
Index keywords: Application programs; Artificial intelligence; Program debugging; Software engineering; Static analysis; Synchronization; Concurrency bugs; Data races; Dynamic binary instrumentation; Dynamic detection; Dynamic program analysis; Dynamic verifications; Efficient detection; Multi-threaded programs; Concurrency control
Document type: Conference paper
Conference: 
Source title: 2016 IEEE/ACIS 17th International Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing, SNPD 2016
Year: 2016
EID: 2-s2.0-84983371613
DOI: 10.1109/snpd.2016.7515908
Retrieval channels: authoritative_outlet_search
Local full-text files: 

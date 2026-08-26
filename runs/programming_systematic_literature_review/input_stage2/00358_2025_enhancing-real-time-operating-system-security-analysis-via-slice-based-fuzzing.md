---
otero_id: "2-s2.0-105018185885"
title: "Enhancing Real-Time Operating System Security Analysis via Slice-Based Fuzzing"
authors: "Li J.; Li H.; Xie Y.; Wang Y.; Hou Q.; Chen L.; Zhang B.; Li S.; Xue Z."
year: "2025"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2025.3615642"
---
# Scopus title-abstract-keyword metadata
Title: Enhancing Real-Time Operating System Security Analysis via Slice-Based Fuzzing
Abstract: Real-Time Operating System (RTOS) has become the main category of embedded systems. It is widely used to support tasks requiring real-time response such as printers and switches. The security of RTOS has been long overlooked as it was running in special environments isolated from attackers. However, with the rapid development of IoT devices, tremendous RTOS devices are connected to the public network. Due to the lack of security mechanisms, these devices are extremely vulnerable to a wide spectrum of attacks. Even worse, the monolithic design of RTOS combines various tasks and services into a single binary, which hinders the current program testing and analysis techniques working on RTOS. In this paper, we propose SFuzz++, a novel slice-based fuzzer designed to detect security vulnerabilities in RTOS. Leveraging the insight that RTOS tasks are typically independent, single-purpose, and deterministic, SFuzz++ extracts task-specific code slices for targeted testing. Specifically, SFuzz++ first identifies external input points that manage user input, with assistance from LLMs, and constructs call graphs from these points. Then, it leverages forward slicing to build the sensitive call graph and prune the paths independent of sink points (e.g., memcpy). Further, it detects and handles roadblocks within the coarse-grain scope that hinder effective fuzzing, such as call sites unrelated to the user input or conditional branches unrelated to sink points. At the same time, it attempts to restore the context of the slices to recreate the actual runtime state. And then, it conducts coverage-guided fuzzing on these code snippets. Finally, SFuzz++ leverages forward and backward slicing to track and verify each path constraint and determine whether a bug discovered in the fuzzer is a real vulnerability. SFuzz++ successfully discovered 82 zero-day bugs on 35 RTOS samples, and 78 of them have been assigned CVE or CNVD IDs. Our empirical evaluation shows that SFuzz++ outperforms the state-of-the-art tools (e.g., UnicornAFL) on testing RTOS. © 1976-2012 IEEE.
Author keywords: concolic execution; RTOS; slice-based fuzzing; taint analysis
Index keywords: Codes (symbols); Embedded systems; Human computer interaction; Network security; Real time systems; Security systems; Call graphs; Concolic execution; Embedded-system; Operating systems securities; Real time response; Real.time operating system; Security analysis; Slice-based fuzzing; Taint analyze; User input; Software testing
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2025
EID: 2-s2.0-105018185885
DOI: 10.1109/tse.2025.3615642
Retrieval channels: authoritative_outlet_search
Local full-text files: 

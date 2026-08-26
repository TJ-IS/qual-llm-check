---
otero_id: "2-s2.0-85198730316"
title: "Mole: Efficient Crash Reproduction in Android Applications with Enforcing Necessary UI Events"
authors: "Masoudian M.; Huang H.; Amini M.; Zhang C."
year: "2024"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2024.3428543"
---
# Scopus title-abstract-keyword metadata
Title: Mole: Efficient Crash Reproduction in Android Applications with Enforcing Necessary UI Events
Abstract: To improve the quality of Android apps, developers use automated debugging and testing solutions to determine whether the previously found crashes are reproducible. However, existing GUI fuzzing solutions for Android apps struggle to reproduce crashes efficiently based solely on a crash stack trace. This trace provides the location in the app where the crash occurs. GUI fuzzing solutions currently in use rely on heuristics to generate UI events. Unfortunately, these events often do not align with the investigation of an app's UI event space to reach a specific location of code. Hence, they generate numerous events unrelated to the crash, leading to an event explosion. To address this issue, a precise static UI model of widgets and screens can greatly enhance the efficiency of a fuzzing tool in its search. Building such a model requires considering all possible combinations of event sequences on widgets since the execution order of events is not statically determined. However, this approach presents scalability challenges in complex apps with several widgets. In this paper, we propose a directed-based fuzzing solution to reduce an app's event domain to the necessary ones to trigger a crash. Our insight is that the dependencies between widgets in their visual presentation and attribute states provide valuable information in precisely identifying events that trigger a crash. We propose an attribute-sensitive reachability analysis (ASRA) to track dependent widgets in reachable paths to the crash point and distinguish between events in terms of their relevancy to be generated in the crash reproduction process. With instrumentation, we inject code to prune irrelevant events, reducing the event domain to search at run time. We used four famous fuzzing tools, Monkey, Ape, Stoat, and FastBot2, to assess the impact of our solution in decreasing the crash reproduction time and increasing the possibility of reproducing a crash. Our results show that the success ratio of reproducing a crash has increased for one-fourth of crashes. In addition, the average reproduction time of a crash becomes at least 2x faster. Wilcoxon Mann-Whitney test shows this enhancement is significant when our tool is used compared to baseline and insensitive reachability analysis.  © 1976-2012 IEEE.
Author keywords: Android fuzzing; bug reproducing; crash stack trace; directed fuzzing; widget dependencies
Index keywords: Android (operating system); Cell proliferation; Codes (symbols); Program debugging; Android apps; Bug reproducing; Code; Computer crashes; Crash stack trace; Directed fuzzing; Fuzzing; Layout; Widget dependency; Graphical user interfaces
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2024
EID: 2-s2.0-85198730316
DOI: 10.1109/tse.2024.3428543
Retrieval channels: authoritative_outlet_search
Local full-text files: 

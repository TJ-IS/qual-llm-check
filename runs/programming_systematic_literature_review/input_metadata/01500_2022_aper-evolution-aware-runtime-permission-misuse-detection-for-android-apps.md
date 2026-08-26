---
otero_id: "2-s2.0-85133497079"
title: "APER: Evolution-Aware Runtime Permission Misuse Detection for Android Apps"
authors: "Wang S.; Wang Y.; Zhan X.; Wang Y.; Liu Y.; Luo X.; Cheung S.-C."
year: "2022"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3510003.3510074"
---
# Scopus title-abstract-keyword metadata
Title: APER: Evolution-Aware Runtime Permission Misuse Detection for Android Apps
Abstract: The Android platform introduces the runtime permission model in version 6.0. The new model greatly improves data privacy and user experience, but brings new challenges for app developers. First, it allows users to freely revoke granted permissions. Hence, developers cannot assume that the permissions granted to an app would keep being granted. Instead, they should make their apps carefully check the permission status before invoking dangerous APIs. Second, the permission specification keeps evolving, bringing new types of compatibility issues into the ecosystem. To understand the impact of the challenges, we conducted an empirical study on 13,352 popular Google Play apps. We found that 86.0% apps used dangerous APIs asynchronously after permission management and 61.2% apps used evolving dangerous APIs. If an app does not properly handle permission revocations or platform differences, unexpected runtime issues may happen and even cause app crashes. We call such Android Runtime Permission issues as ARP bugs. Unfortunately, existing runtime permission issue detection tools cannot effectively deal with the ARP bugs induced by asynchronous permission management and permission specification evolution. To fill the gap, we designed a static analyzer, Aper, that performs reaching definition and dominator analysis on Android apps to detect the two types of ARP bugs. To compare Aper with existing tools, we built a benchmark, ARPFIX, from 60 real ARP bugs. Our experiment results show that Aper significantly outperforms two academic tools, ARPDROID and Revdroid, and an industrial tool, Lint, on ARPFIX, with an average improvement of 46.3% on F1-score. In addition, Aper successfully found 34 ARP bugs in 214 open-source Android apps, most of which can result in abnormal app behaviors (such as app crashes) according to our manual validation. We reported these bugs to the app developers. So far, 17 bugs have been confirmed and seven have been fixed. © 2022 ACM.
Author keywords: Android Runtime Permission; Compatibility Issues; Static Analysis
Index keywords: Android (operating system); Data privacy; Open source software; Program debugging; Specifications; Android apps; Android platforms; Android runtime permission; Compatibility issue; Detection tools; Empirical studies; Google plays; Misuse detection; Runtimes; Users' experiences; Static analysis
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2022
EID: 2-s2.0-85133497079
DOI: 10.1145/3510003.3510074
Retrieval channels: authoritative_outlet_search
Local full-text files: 

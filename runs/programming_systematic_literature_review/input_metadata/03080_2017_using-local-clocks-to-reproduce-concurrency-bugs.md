---
otero_id: "2-s2.0-85030233148"
title: "Using local clocks to reproduce concurrency bugs"
authors: "Wang Z.; Wu C.; Yuan X.; Wang Z.; Li J.; Yew P.-C.; Huang J.; Feng X.; Lan Y.; Chen Y.; Lai Y.; Guan Y."
year: "2017"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2017.2752158"
---
# Scopus title-abstract-keyword metadata
Title: Using local clocks to reproduce concurrency bugs
Abstract: Multi-threaded programs play an increasingly important role in current multi-core environments. Exposing concurrency bugs and debugging such multi-threaded programs are quite challenging due to their inherent non-determinism. In order to mitigate such non-determinism, many approaches such as record-and-replay have been proposed. However, those approaches often suffer significant performance degradation because they require a large amount of recorded information and/or long analysis and replay time. In this paper, we propose an efficient and effective approach, ReCBuLC (reproducing concurrency bugs using local clocks), to take advantage of the hardware clocks available on modern processors. The key idea is to reduce the recording overhead and the time to analyze events' global order by recording timestamps in each thread. These timestamps are used to determine the global order of shared accesses. To avoid the large overhead in accessing system-wide global clock, we opt to use local per-core clocks that incur much less access overhead.We then propose techniques to resolve skews among local clocks and obtain an accurate global event order. By using per-core clocks, state-of-the-art bug reproducing systems such as PRES and CLAP can reduce their recording overheads by up to 85 percent, and the analysis time up to 84.66% 99.99%, respectively. © 2017 IEEE.
Author keywords: Bug reproducing; Concurrency; Local clock
Index keywords: Clocks; Concurrency control; Cost reduction; Multicore programming; bug reproducing; concurrency; Effective approaches; Modern processors; Multi-threaded programs; Performance degradation; Record-and-replay; State of the art; Program debugging
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2017
EID: 2-s2.0-85030233148
DOI: 10.1109/tse.2017.2752158
Retrieval channels: authoritative_outlet_search
Local full-text files: 

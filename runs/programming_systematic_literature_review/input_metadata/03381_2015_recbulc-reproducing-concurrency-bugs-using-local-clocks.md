---
otero_id: "2-s2.0-84951778332"
title: "ReCBuLC: Reproducing concurrency bugs using local clocks"
authors: "Yuan X.; Wu C.; Wang Z.; Li J.; Yew P.-C.; Huang J.; Feng X.; Lan Y.; Chen Y.; Guan Y."
year: "2015"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse.2015.94"
---
# Scopus title-abstract-keyword metadata
Title: ReCBuLC: Reproducing concurrency bugs using local clocks
Abstract: Multi-threaded programs play an increasingly important role in current multi-core environments. Exposing concurrency bugs and debugging such multi-threaded programs have become quite challenging due to their inherent non-determinism. In order to eliminate such non-determinism, many approaches such as record-and-replay and other similar bug reproducing systems have been proposed. However, those approaches often suffer significant performance degradation because they require a large amount of recorded information and/or long analysis and replay time. In this paper, we propose an effective approach, ReCBuLC, to take advantage of the hardware clocks available on modern processors. The key idea is to reduce the recording overhead and analyzing events' global order by using time stamps recorded in each thread. Those timestamps are used to determine the global orders of shared accesses. To avoid the large overhead incurred in accessing system-wide global clock, we opt to use local per-core clocks that incur much less access overhead. We then propose techniques to resolve differences among local clocks and obtain an accurate global event order. By using per-core clocks, state-of-the-art bug reproducing systems such as PRES and CLAP can reduce the recording overheads by 1% 85%, and the analysis time by 84.66% 99.99%, respectively. © 2015 IEEE.
Author keywords: Bug reproducing; Concurrency; Local clock
Index keywords: Clocks; Concurrency control; Cost reduction; Multicore programming; Software engineering; Bug reproducing; Concurrency; Effective approaches; Modern processors; Multi-threaded programs; Performance degradation; Record-and-replay; State of the art; Program debugging
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2015
EID: 2-s2.0-84951778332
DOI: 10.1109/icse.2015.94
Retrieval channels: authoritative_outlet_search
Local full-text files: 

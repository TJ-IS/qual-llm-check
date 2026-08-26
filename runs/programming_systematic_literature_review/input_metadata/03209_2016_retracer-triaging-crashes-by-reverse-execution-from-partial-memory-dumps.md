---
otero_id: "2-s2.0-84971441711"
title: "RETracer: Triaging crashes by reverse execution from partial memory dumps"
authors: "Cui W.; Peinado M.; Cha S.K.; Fratantonio Y.; Kemerlis V.P."
year: "2016"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/2884781.2884844"
---
# Scopus title-abstract-keyword metadata
Title: RETracer: Triaging crashes by reverse execution from partial memory dumps
Abstract: Many software providers operate crash reporting services to automatically collect crashes from millions of customers and file bug reports. Precisely triaging crashes is necessary and important for software providers because the millions of crashes that may be reported every day are critical in identifying high impact bugs. However, the triaging accuracy of existing systems is limited, as they rely only on the syntactic information of the stack trace at the moment of a crash without analyzing program semantics. In this paper, we present RETracer, the first system to triage software crashes based on program semantics reconstructed from memory dumps. RETracer was designed to meet the requirements of large-scale crash reporting services. RETracer performs binarylevel backward taint analysis without a recorded execution trace to understand how functions on the stack contribute to the crash. The main challenge is that the machine state at an earlier time cannot be recovered completely from a memory dump, since most instructions are information destroying. We have implemented RETracer for x86 and x86-64 native code, and compared it with the existing crash triaging tool used by Microsoft. We found that RETracer eliminates two thirds of triage errors based on a manual analysis of 140 bugs fixed in Microsoft Windows and Office. RETracer has been deployed as the main crash triaging system on Microsoft's crash reporting service. © 2016 ACM.
Author keywords: Backward taint analysis; Reverse execution; Triaging
Index keywords: Crashworthiness; Semantics; Software engineering; Trace analysis; Backward taint analysis; Existing systems; Microsoft windows; Program semantics; Reporting service; Reverse execution; Syntactic information; Triaging; Program debugging
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2016
EID: 2-s2.0-84971441711
DOI: 10.1145/2884781.2884844
Retrieval channels: authoritative_outlet_search
Local full-text files: 

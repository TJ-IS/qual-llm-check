---
otero_id: "2-s2.0-85133500989"
title: "µ AFL: Non-intrusive Feedback-driven Fuzzing for Microcontroller Firmware"
authors: "Li W.; Shi J.; Li F.; Lin J.; Wang W.; Guan L."
year: "2022"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3510003.3510208"
---
# Scopus title-abstract-keyword metadata
Title: µ AFL: Non-intrusive Feedback-driven Fuzzing for Microcontroller Firmware
Abstract: Fuzzing is one of the most effective approaches to finding software flaws. However, applying it to microcontroller firmware incurs many challenges. For example, rehosting-based solutions cannot accurately model peripheral behaviors and thus cannot be used to fuzz the corresponding driver code. In this work, we present mu AFL, a hardware-in-the-loop approach to fuzzing microcontroller firmware. It leverages debugging tools in existing embedded system development to construct an AFL-compatible fuzzing framework. Specifically, we use the debug dongle to bridge the fuzzing environment on the PC and the target firmware on the microcontroller device. To collect code coverage information without costly code instrumentation, mu AFL relies on the ARM ETM hardware debugging feature, which transparently collects the instruction trace and streams the results to the PC. However, the raw ETM data is obscure and needs enormous computing resources to recover the actual instruction flow. We therefore propose an alternative representation of code coverage, which retains the same path sensitivity as the original AFL algorithm, but can directly work on the raw ETM data without matching them with disassembled instructions. To further reduce the workload, we use the DWT hardware feature to selectively collect runtime information of interest. We evaluated mu AFL on two real evaluation boards from two major vendors: NXP and STMicroelectronics. With our prototype, we discovered ten zero-day bugs in the driver code shipped with the SDK of STMicroelectronics and three zero-day bugs in the SDK of NXP. Eight CVEs have been allocated for them. Considering the wide adoption of vendor SDKs in real products, our results are alarming. © 2022 ACM.
Author keywords: ETM; firmware security; fuzzing; IoT; microcontroller
Index keywords: Controllers; Firmware; Internet of things; Program debugging; Code coverage; Debugging tools; Effective approaches; ETM; Firmware security; Fuzzing; Hardware in the loops; IoT; Non-intrusive; STMicroelectronics; Microcontrollers
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2022
EID: 2-s2.0-85133500989
DOI: 10.1145/3510003.3510208
Retrieval channels: authoritative_outlet_search
Local full-text files: 

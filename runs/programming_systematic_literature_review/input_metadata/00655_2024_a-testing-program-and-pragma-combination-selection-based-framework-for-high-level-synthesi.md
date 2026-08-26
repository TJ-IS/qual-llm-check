---
otero_id: "2-s2.0-85186108189"
title: "A Testing Program and Pragma Combination Selection Based Framework for High-Level Synthesis Tool Pragma-Related Bug Detection"
authors: "Jiang H.; Wang Z.; Zhou Z.; Li X.; Guo S.; Sun W.; Zhang T."
year: "2024"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2024.3368553"
---
# Scopus title-abstract-keyword metadata
Title: A Testing Program and Pragma Combination Selection Based Framework for High-Level Synthesis Tool Pragma-Related Bug Detection
Abstract: High-Level Synthesis (HLS) tools convert C/C++ design code into Hardware Description Language (HDL) code automatically, which are often used for Field Programmable Gate Array (FPGA) design. HLS tools provide many pragmas, which are a kind of directive to be inserted into C/C++ code, for designers to efficiently control the synthesis of code components (e.g., arrays and loops) to generate FPGA implementations with varying performances and costs. However, the use of some pragmas may trigger HLS tool bugs (e.g., tool crashes). Although many formal methods have been proposed to verify the correctness of various HLS phases, no relevant work addresses the problem on detecting HLS tool pragma-related bugs. To resolve this problem, two challenges need to be addressed, namely the selection of testing programs and the acquisition of pragma combinations, due to the enormous number of testing programs and pragma combinations. In this paper, we propose TEPACS, a TEsting Program and prAgma Combination Selection-based framework, to construct diverse testing programs with pragmas for effectively detecting HLS tool pragma-related bugs. TEPACS follows the idea of fuzzing, which is a widely used technique in software testing. First, TEPACS selects the representative testing program according to the cosine distance between the code component vectors of testing programs. Then, for a selected program, TEPACS generates its golden output and uses the pragma combination selection method based on combinatorial testing to generate a set of programs with different pragmas. TEPACS uses the HLS tool under test to convert these testing programs into HDL codes and obtains the simulation results of the HDL code. Finally, based on differential testing, TEPACS identifies HLS tool bugs triggered if the simulation result and golden output are inconsistent. We evaluate TEPACS and its five variants on Vitis HLS, a widely used FPGA HLS tool. Experimental results show that TEPACS outperforms the baselines by at least 11.17% in terms of the bug-finding capability. In one month, TEPACS detected 34 bugs on the latest version of Vitis HLS, of which 9 bugs have been confirmed. © 1976-2012 IEEE.
Author keywords: fuzzing; HLS; pragma; pragma combination selection; software testing; testing program selection
Index keywords: C (programming language); Codes (symbols); Computer hardware; Computer hardware description languages; Field programmable gate arrays (FPGA); High level synthesis; Integrated circuit design; Logic gates; Pipeline processing systems; Program debugging; Code; Computer bugs; Field programmable gate array; Field programmables; Fuzzing; Hardware design language; High-level synthesis; Optimisations; Pipeline processing; Pragma; Pragma combination selection; Programmable gate array; Software testings; Testing program selection; Testing programmes; Software testing
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2024
EID: 2-s2.0-85186108189
DOI: 10.1109/tse.2024.3368553
Retrieval channels: authoritative_outlet_search
Local full-text files: 

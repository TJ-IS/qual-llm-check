---
otero_id: "2-s2.0-84971383866"
title: "Finding and analyzing compiler warning defects"
authors: "Sun C.; Le V.; Su Z."
year: "2016"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/2884781.2884879"
---
# Scopus title-abstract-keyword metadata
Title: Finding and analyzing compiler warning defects
Abstract: Good compiler diagnostic warnings facilitate software development as they indicate likely programming mistakes or code smells. However, due to compiler bugs, the warnings may be erroneous, superfluous or missing, even for mature production compilers like GCC and Clang. In this paper, we (1) propose the first randomized differential testing technique to detect compiler warning defects and (2) describe our extensive evaluation in finding warning defects in widely-used C compilers. At the high level, our technique starts with generating random programs to trigger compilers to emit a variety of compiler warnings, aligns the warnings from different compilers, and identifies inconsistencies as potential bugs. We develop effective techniques to overcome three specific challenges: (1) How to generate random programs, (2) how to align textual warnings, and (3) how to reduce test programs for bug reporting? Our technique is very effective-we have found and reported 60 bugs for GCC (38 confirmed, assigned or fixed) and 39 for Clang (14 confirmed or fixed). This case study not only demonstrates our technique's effectiveness, but also highlights the need to continue improving compilers' warning support, an essential, but rather neglected aspect of compilers. © 2016 ACM.
Author keywords: 
Index keywords: C (programming language); Defects; Program debugging; Program diagnostics; Software design; Software engineering; Testing; Bug reporting; C compilers; Code smell; Differential testing; Test program; Program compilers
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2016
EID: 2-s2.0-84971383866
DOI: 10.1145/2884781.2884879
Retrieval channels: authoritative_outlet_search
Local full-text files: 

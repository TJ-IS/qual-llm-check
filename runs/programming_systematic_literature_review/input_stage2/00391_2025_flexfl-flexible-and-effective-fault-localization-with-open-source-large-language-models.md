---
otero_id: "2-s2.0-105000368545"
title: "FlexFL: Flexible and Effective Fault Localization With Open-Source Large Language Models"
authors: "Xu C.; Liu Z.; Ren X.; Zhang G.; Liang M.; Lo D."
year: "2025"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2025.3553363"
---
# Scopus title-abstract-keyword metadata
Title: FlexFL: Flexible and Effective Fault Localization With Open-Source Large Language Models
Abstract: Fault localization (FL) targets identifying bug locations within a software system, which can enhance debugging efficiency and improve software quality. Due to the impressive code comprehension ability of Large Language Models (LLMs), a few studies have proposed to leverage LLMs to locate bugs, i.e., LLM-based FL, and demonstrated promising performance. However, first, these methods are limited in flexibility. They rely on bug-triggering test cases to perform FL and cannot make use of other available bug-related information, e.g., bug reports. Second, they are built upon proprietary LLMs, which are, although powerful, confronted with risks in data privacy. To address these limitations, we propose a novel LLM-based FL framework named FlexFL, which can flexibly leverage different types of bug-related information and effectively work with open-source LLMs. FlexFL is composed of two stages. In the first stage, FlexFL reduces the search space of buggy code using state-of-the-art FL techniques of different families and provides a candidate list of bug-related methods. In the second stage, FlexFL leverages LLMs to delve deeper to double-check the code snippets of methods suggested by the first stage and refine fault localization results. In each stage, FlexFL constructs agents based on open-source LLMs, which share the same pipeline that does not postulate any type of bug-related information and can interact with function calls without the out-of-the-box capability. Extensive experimental results on Defects4J demonstrate that FlexFL outperforms the baselines and can work with different open-source LLMs. Specifically, FlexFL with a lightweight open-source LLM Llama3-8B can locate 42 and 63 more bugs than two state-of-the-art LLM-based FL approaches AutoFL and AgentFL that both use GPT-3.5. In addition, FlexFL can localize 93 bugs that cannot be localized by non-LLM-based FL techniques at the top 1. Furthermore, to mitigate potential data contamination, we conduct experiments on a dataset which Llama3-8B has not seen before, and the evaluation results show that FlexFL can also achieve good performance. © 1976-2012 IEEE.
Author keywords: Fault localization; large language model; LLM-based agent
Index keywords: Computer debugging; Computer software selection and evaluation; Open source software; Outages; Problem oriented languages; Reliability analysis; Software agents; Software testing; Fault localization; Language model; Large language model; Large language model-based agent; Localization technique; Model-based OPC; Open-source; Performance; State of the art; Program debugging
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2025
EID: 2-s2.0-105000368545
DOI: 10.1109/tse.2025.3553363
Retrieval channels: authoritative_outlet_search
Local full-text files: 

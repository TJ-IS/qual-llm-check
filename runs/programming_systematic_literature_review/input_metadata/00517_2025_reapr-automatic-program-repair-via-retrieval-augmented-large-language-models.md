---
otero_id: "2-s2.0-105011270181"
title: "ReAPR: Automatic program repair via retrieval-augmented large language models"
authors: "Liu Z.; Du X.; Liu H."
year: "2025"
journal: "Software Quality Journal"
doi: "10.1007/s11219-025-09728-1"
---
# Scopus title-abstract-keyword metadata
Title: ReAPR: Automatic program repair via retrieval-augmented large language models
Abstract: Automatic Program Repair (APR) aims to automatically fix software defects, significantly reducing the efforts of manual debugging. Recent studies have demonstrated impressive results in utilizing Large Language Models (LLMs) for software bug fixing. Current LLM-based approaches depend solely on the pre-trained knowledge of LLMs, overlooking the prior knowledge contained in historical bug repair records, which increases the likelihood of hallucinations. To address this challenge, this paper proposes ReAPR, a retrieval-augmented framework for APR. We first curate a high-quality retrieval database by carefully compiling and filtering the existing datasets for APR. Subsequently, ReAPR leverages a retriever to fetch bug-fix pairs similar to the target bug from a retrieval database, providing contextual hints to guide the LLMs in the repair process. We then investigate two techniques to retrieve bug-fix pairs associated with the function to be fixed: BM25 and Dense Passage Retrieval (DPR). After retrieving the relevant bug-fix pair, we construct a prompt and integrate the retrieved pair into it. Besides, we also compare the proposed RAG-based approach with the parameter-efficient fine-tuning (PEFT) approaches on repair performance. To validate the effectiveness of ReAPR, we conduct extensive experiments based on the widely-used benchmark dataset Defects4j 2.0 as well as the latest benchmark GitBug-Java. The results show that ReAPR, based on the CodeLlama(7B) backbone, successfully fixes 68 and 59 bugs in the DPR and BM25 settings, respectively, in Defects4j 2.0, outperforming the best baseline approach by 18 and 9 bugs under the same repair settings. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025.
Author keywords: Automated Program Repair; Large Language Models; Prompt Learning; Retrieval-Augmented Generation
Index keywords: Automatic programming; Computer debugging; Defects; Information retrieval; Program debugging; Automated program repair; Automatic programs; Bug fixes; Language model; Large language model; Passage retrieval; Prompt learning; Retrieval-augmented generation; Software bug; Software defects; Computational linguistics; Repair
Document type: Article
Conference: 
Source title: Software Quality Journal
Year: 2025
EID: 2-s2.0-105011270181
DOI: 10.1007/s11219-025-09728-1
Retrieval channels: authoritative_outlet_search
Local full-text files: 

---
otero_id: "2-s2.0-105003231369"
title: "Comprehensive Fine-Tuning Large Language Models of Code for Automated Program Repair"
authors: "Huang K.; Zhang J.; Bao X.; Wang X.; Liu Y."
year: "2025"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2025.3532759"
---
# Scopus title-abstract-keyword metadata
Title: Comprehensive Fine-Tuning Large Language Models of Code for Automated Program Repair
Abstract: Automated program repair (APR) research has entered the era of large language models (LLM), and researchers have conducted several empirical studies to explore the repair capabilities of LLMs for APR. Many studies adopt the zero/few-shot learning paradigm for APR, which directly use LLMs to generate the possibly correct code given its surrounding context. Though effective, the repair capabilities of LLMs based on the fine-tuning paradigm have yet to be extensively explored. Also, it remains unknown whether LLMs have the potential to repair more complicated bugs (e.g., multi-hunk bugs). To fill the gap, in the conference version of this work, we conduct an initial study on the program repair capability of million-level LLMs in the fine-tuning paradigm. We select 5 popular million-level LLMs with representative pre-training architectures, including CodeBERT, GraphCodeBERT, PLBART, CodeT5, and UniXcoder. We consider 3 typical program repair scenarios (i.e., bugs, vulnerabilities, and errors) involving 3 programming languages (i.e., Java, C/C++, and JavaScript). Our experimental results show that fine-tuning these LLMs can significantly outperform previous state-of-the-art APR tools. However, the repair capabilities of billion-level LLMs for APR remain largely unexplored. Moreover, their substantial model sizes significantly increase the computational cost of fine-tuning. While parameter-efficient fine-tuning (PEFT) techniques offer a promising solution, their effectiveness in repair tasks and the selection of appropriate PEFT strategies remain unclear. Similarly, many novel APR strategies have been developed for non-pre-trained models, yet their applicability and effectiveness on LLMs are still unexamined. To address these gaps, we extend our prior study through three key dimensions: 1) LLM4APR, which evaluates the repair capabilities of five billion-level LLM families (InCoder, CodeGeeX, CodeGen, StarCoder, and CodeLlama) under the fine-tuning paradigm; 2) PEFT4LLM, which compares full-parameter fine-tuning (FPFT) with three PEFT techniques (LoRA, AdaLoRA, and IA3) to determine optimal strategies that balance repair cost and performance of LLMs; and 3) APR4LLM, which investigates the potential of a basic neural machine translation (NMT) approach alongside three advanced repair strategies (TENURE, ITER, and KATANA) to enhance the repair capabilities of LLMs. Overall, our extensive results suggest that larger scale models typically have better repair capabilities. The LoRA technique is still the best choice for LLM4APR studies. Different repair strategies result in different repair capabilities for the foundation models, but some of the strategies that performed well on the non-pre-trained model did not show an advantage on LLMs. Besides, we released all LLMs fine-tuned with repair tasks to facilitate LLM4APR research, and we encourage researchers to develop more powerful APR tools on the basis of these repair LLMs. © 1976-2012 IEEE.
Author keywords: automated program repair; fine-tuning; Large language model
Index keywords: Ada (programming language); Computer debugging; Computer software maintenance; Computer software selection and evaluation; Costs; Data flow analysis; Java programming language; Multitasking; Optimal systems; Problem oriented languages; Program debugging; UNIX; Automated program repair; Correct code; Empirical studies; Fine tuning; Language model; Large language model; Learning paradigms; Pre-training; Repair strategy; Repair tools; C++ (programming language)
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2025
EID: 2-s2.0-105003231369
DOI: 10.1109/tse.2025.3532759
Retrieval channels: authoritative_outlet_search
Local full-text files: 

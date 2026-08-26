---
otero_id: "2-s2.0-105040669942"
title: "BePilot: An AI Programming Assistant for Compiler Backend Development"
authors: "Zhong M.; Sun X.; Lv F.; Wang L.; Geng H.; Qiu L.; Cui H.; Feng X."
year: "2026"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3764585"
---
# Scopus title-abstract-keyword metadata
Title: BePilot: An AI Programming Assistant for Compiler Backend Development
Abstract: Compiler backends are tasked with generating executable machine code for various processors. As the diversity of processors continues to grow, it is imperative for programmers to tailor specific compiler backends to accommodate each one. However, compiler backend development remains a labor-intensive and time-consuming process, with limited automation tools available. Although large language models (LLMs) have demonstrated strong abilities in code completion and code generation tasks, the lack of appropriate datasets for compiler backend development limits the application of LLMs in this field. In this article, we introduce ComBack++, a multilingual dataset covering C/C++, machine description, and TableGen, with 184 backends from GCC and LLVM, four backend-specific tasks. Based on ComBack++, we present BePilot, a compiler backend-specific LLM available in two sizes: BePilot-1.5B and BePilot-7B. We also introduce CB-Retriever, a retriever that constructs few-shot prompts via in-context learning to improve vanilla LLM performance in resource-constrained settings. Experimental results show that BePilot-1.5B and BePilot-7B achieve significantly higher accuracy across four tasks in ComBack++ compared to 12 baseline LLMs (125M–34B parameters). In addition, CB-Retriever consistently boosts the accuracy of six mainstream LLMs. Both BePilot-1.5B and BePilot-7B, as well as vanilla LLMs augmented with CB-Retriever, outperform the traditional manual compiler backend development approach (Fork-Flow) in efficiency across all four tasks in ComBack++. Furthermore, human evaluation by four experienced compiler backend developers confirms that BePilot not only improves development efficiency over Fork-Flow but also surpasses commercial AI programming assistants such as GPT-4o-mini and Gemini2-Flash in terms of code quality. These findings confirm that BePilot and CB-Retriever can substantially enhance compiler backend development efficiency. © 2026 Copyright held by the owner/author(s).
Author keywords: Code Generation; Compiler Backends; Large Language Models
Index keywords: Automation; Codes (symbols); Large datasets; Optimal systems; Program compilers; Automation tools; Code completions; Codegeneration; Compiler backend; Executables; Labor time; Labour-intensive; Language model; Large language model; Machine codes; Efficiency
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2026
EID: 2-s2.0-105040669942
DOI: 10.1145/3764585
Retrieval channels: authoritative_outlet_search
Local full-text files: 

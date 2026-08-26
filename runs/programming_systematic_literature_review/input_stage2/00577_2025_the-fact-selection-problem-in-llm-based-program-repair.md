---
otero_id: "2-s2.0-105010324108"
title: "The Fact Selection Problem in LLM-Based Program Repair"
authors: "Parasaram N.; Yan H.; Yang B.; Flahy Z.; Qudsi A.; Ziaber D.; Barr E.T.; Mechtaev S."
year: "2025"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse55347.2025.00162"
---
# Scopus title-abstract-keyword metadata
Title: The Fact Selection Problem in LLM-Based Program Repair
Abstract: Recent research has shown that incorporating bug-related facts, such as stack traces and GitHub issues, into prompts enhances the bug-fixing capabilities of large language models (LLMs). Considering the ever-increasing context window of these models, a critical question arises: what and how many facts should be included in prompts to maximise the chance of correctly fixing bugs? To answer this question, we conducted a large-scale study, employing over 19K prompts featuring various combinations of seven diverse facts to rectify 314 bugs from open -source Python projects within the BugsInPy benchmark. Our findings revealed that each fact, ranging from simple syntactic details like code context to semantic information previously unexplored in the context of LLMs such as angelic values, is beneficial. Specifically, each fact aids in fixing some bugs that would remain unresolved or only be fixed with a low success rate without it. Importantly, we discovered that the effectiveness of program repair prompts is non-monotonic over the number of used facts; using too many facts leads to subpar outcomes. These insights led us to define the fact selection problem: determining the optimal set of facts for inclusion in a prompt to maximise LLM's performance on a given task instance. We found that there is no one-size-fits-all set of facts for bug repair. Therefore, we developed a basic statistical model, named Maniple, which selects facts specific to a given bug to include in the prompt. This model significantly surpasses the performance of the best generic fact set. To underscore the significance of the fact selection problem, we benchmarked Maniple against the state-of-the-art zero-shot, non-conversational LLM-based bug repair methods. On our testing dataset of 157 bugs, Maniple repairs 88 bugs, 17% above the best configuration.  © 2025 IEEE.
Author keywords: automated program repair; large language models; prompt engineering
Index keywords: Computational linguistics; Open source software; Open systems; Program debugging; Semantics; Statistical tests; Syntactics; Automated program repair; Bug-fixing; Context window; Language model; Large language model; Model-based OPC; Performance; Prompt engineering; Recent researches; Selection problems; Repair
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2025
EID: 2-s2.0-105010324108
DOI: 10.1109/icse55347.2025.00162
Retrieval channels: authoritative_outlet_search
Local full-text files: 

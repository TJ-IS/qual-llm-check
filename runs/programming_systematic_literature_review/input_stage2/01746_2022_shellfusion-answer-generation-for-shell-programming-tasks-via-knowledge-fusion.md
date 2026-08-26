---
otero_id: "2-s2.0-85133531527"
title: "ShellFusion: Answer Generation for Shell Programming Tasks via Knowledge Fusion"
authors: "Zhang N.; Liu C.; Xia X.; Treude C.; Zou Y.; Lo D.; Zheng Z."
year: "2022"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3510003.3510131"
---
# Scopus title-abstract-keyword metadata
Title: ShellFusion: Answer Generation for Shell Programming Tasks via Knowledge Fusion
Abstract: Shell commands are widely used for accomplishing tasks, such as network management and file manipulation, in Unix and Linux platforms. There are a large number of shell commands available. For example, 50,000+ commands are documented in the Ubuntu Manual Pages (MPs). Quite often, programmers feel frustrated when searching and orchestrating appropriate shell commands to accomplish specific tasks. To address the challenge, the shell programming community calls for easy-to-use tutorials for shell commands. However, existing tutorials (e.g., TLDR) only cover a limited number of frequently used commands for shell beginners and provide limited support for users to search for commands by a task. We propose an approach, i.e., ShellFusion, to automatically generate comprehensive answers (including relevant shell commands, scripts, and explanations) for shell programming tasks. Our approach integrates knowledge mined from Q&A posts in Stack Exchange, Ubuntu MPs, and TLDR tutorials. For a query that describes a shell programming task, ShellFusion recommends a list of relevant shell commands. Specifically, ShellFusion retrieves the top-n Q&A posts with questions similar to the query and detects shell commands with options (e.g., ls -t) from the accepted answers of the retrieved posts. Next, ShellFusion filters out irrelevant commands with descriptions in MP and TLDR that share little semantics with the query, and further ranks the candidate commands based on their similarities with the query and the retrieved posts. To help users understand how to achieve the task using a recommended command, ShellFusion generates a comprehensive answer for each command by synthesizing knowledge from Q&A posts, MPs, and TLDR. Our evaluation of 434 shell programming tasks shows that ShellFusion significantly outperforms Magnum (the state-of-the-art natural language-to-Bash command approach) by at least 179.6% in terms of MRR@K and MAP@K. A user study conducted with 20 shell programmers further shows that ShellFusion can help users address programming tasks more efficiently and accurately, compared with Magnum and DeepAns (a recent answer recommendation baseline). © 2022 ACM.
Author keywords: Answer Generation; Knowledge Fusion; Shell Programming
Index keywords: Knowledge management; Linux; Shells (structures); Answer generation; Knowledge fusion; Linux platform; Manual pages; Networks management; Programming tasks; Shell command; Shell programming; Specific tasks; UNIX platforms; Semantics
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2022
EID: 2-s2.0-85133531527
DOI: 10.1145/3510003.3510131
Retrieval channels: authoritative_outlet_search
Local full-text files: 

---
otero_id: "2-s2.0-85187275304"
title: "Automatic Commit Message Generation: A Critical Review and Directions for Future Work"
authors: "Zhang Y.; Qiu Z.; Stol K.-J.; Zhu W.; Zhu J.; Tian Y.; Liu H."
year: "2024"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2024.3364675"
---
# Scopus title-abstract-keyword metadata
Title: Automatic Commit Message Generation: A Critical Review and Directions for Future Work
Abstract: Commit messages are critical for code comprehension and software maintenance. Writing a high-quality message requires skill and effort. To support developers and reduce their effort on this task, several approaches have been proposed to automatically generate commit messages. Despite the promising performance reported, we have identified three significant and prevalent threats in these automated approaches: 1) the datasets used to train and evaluate these approaches contain a considerable amount of 'noise'; 2) current approaches only consider commits of a limited diff size; and 3) current approaches can only generate the subject of a commit message, not the message body. The first limitation may let the models 'learn' inappropriate messages in the training stage, and also lead to inflated performance results in their evaluation. The other two threats can considerably weaken the practical usability of these approaches. Further, with the rapid emergence of large language models (LLMs) that show superior performance in many software engineering tasks, it is worth asking: can LLMs address the challenge of long diffs and whole message generation? This article first reports the results of an empirical study to assess the impact of these three threats on the performance of the state-of-the-art auto generators of commit messages. We collected commit data of the Top 1,000 most-starred Java projects in GitHub and systematically removed noisy commits with bot-submitted and meaningless messages. We then compared the performance of four approaches representative of the state-of-the-art before and after the removal of noisy messages, or with different lengths of commit diffs. We also conducted a qualitative survey with developers to investigate their perspectives on simply generating message subjects. Finally, we evaluate the performance of two representative LLMs, namely UniXcoder and ChatGPT, in generating more practical commit messages. The results demonstrate that generating commit messages is of great practical value, considerable work is needed to mature the current state-of-the-art, and LLMs can be an avenue worth trying to address the current limitations. Our analyses provide insights for future work to achieve better performance in practice. © 1976-2012 IEEE.
Author keywords: benchmark; commit message generation; Commit-based software development; open collaboration
Index keywords: Computational linguistics; Computer aided language translation; Computer software maintenance; Job analysis; Benchmark; Chatbots; Code; Commit message generation; Commit-based software development; Machine translations; Noise measurements; Open collaboration; Performance; Task analysis; Software design
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2024
EID: 2-s2.0-85187275304
DOI: 10.1109/tse.2024.3364675
Retrieval channels: authoritative_outlet_search
Local full-text files: 

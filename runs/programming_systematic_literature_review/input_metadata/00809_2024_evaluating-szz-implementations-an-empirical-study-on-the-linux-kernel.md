---
otero_id: "2-s2.0-85194856448"
title: "Evaluating SZZ Implementations: An Empirical Study on the Linux Kernel"
authors: "Lyu Y.; Kang H.J.; Widyasari R.; Lawall J.; Lo D."
year: "2024"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2024.3406718"
---
# Scopus title-abstract-keyword metadata
Title: Evaluating SZZ Implementations: An Empirical Study on the Linux Kernel
Abstract: The SZZ algorithm is used to connect bug-fixing commits to the earlier commits that introduced bugs. This algorithm has many applications and many variants have been devised. However, there are some types of commits that cannot be traced by the SZZ algorithm, referred to as 'ghost commits'. The evaluation of how these ghost commits impact the SZZ implementations remains limited. Moreover, these implementations have been evaluated on datasets created by software engineering researchers from information in bug trackers and version controlled histories. Since Oct 2013, the Linux kernel developers have started labelling bug-fixing patches with the commit identifiers of the corresponding bug-inducing commit(s) as a standard practice. As of v6.1-rc5, 76,046 pairs of bug-fixing patches and bug-inducing commits are available. This provides a unique opportunity to evaluate the SZZ algorithm on a large dataset that has been created and reviewed by project developers, entirely independently of the biases of software engineering researchers. In this paper, we apply six SZZ implementations to 76,046 pairs of bug-fixing patches and bug-introducing commits from the Linux kernel. Our findings reveal that SZZ algorithms experience a more significant decline in recall on our dataset (↓13.8%) as compared to prior findings reported by Rosa et al., and the disparities between the individual SZZ algorithms diminish. Moreover, we find that 17.47% of bug-fixing commits are ghost commits. Finally, we propose Tracing-Commit SZZ (TC-SZZ), that traces all commits in the change history of lines modified or deleted in bug-fixing commits. Applying TC-SZZ to all failure cases, excluding ghost commits, we found that TC-SZZ could identify 17.7% of them. Our further analysis based on git log found that 34.6% of bug-inducing commits were in the function history, 27.5% in the file history (but not in the function history), and 37.9% not in the file history. We further evaluated the effectiveness of ChatGPT in boosting the SZZ algorithm's ability to identify bug-inducing commits in the function history, in the file history and not in the file history. © 1976-2012 IEEE.
Author keywords: ChatGPT; defect prediction; empirical study; SZZ
Index keywords: Function evaluation; Large datasets; Linux; Bug-fixing; ChatGPT; Defect prediction; Empirical studies; Labelings; Large datasets; Linux kernel; Project developers; Standard practices; SZZ; Program debugging
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2024
EID: 2-s2.0-85194856448
DOI: 10.1109/tse.2024.3406718
Retrieval channels: authoritative_outlet_search
Local full-text files: 

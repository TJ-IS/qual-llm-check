---
otero_id: "2-s2.0-85219092024"
title: "Improving the performance of software fault localization with effective coverage data reduction techniques"
authors: "Fang C.-C.; Huang C.-Y.; Lee S.-Y.; Tseng Y.-H.; Chu C.W."
year: "2025"
journal: "Journal of Systems and Software"
doi: "10.1016/j.jss.2025.112388"
---
# Scopus title-abstract-keyword metadata
Title: Improving the performance of software fault localization with effective coverage data reduction techniques
Abstract: Fault localization (FL) techniques are widely used to identify the exact location of faulty statement in programs. Three common FL families are SBFL, MBFL, and deep learning-based FL, respectively. Before running any FL methods, coverage data is usually considered as input of FL stage. Therefore, coverage data plays an important role in FL field. On the other hand, if coverage data can be reduced effectively, the performance of FL will be greatly improved. In past studies, filtering out fault-irrelevant statements based on solely failed test cases, the traditional principal component analysis (PCA), and revised PCA techniques were applied to minimize coverage data. However, these approaches have a great opportunity to remove the actual faulty statement, especially in multiple fault localization (MFL). Tracing their root causes does not reflect the actual status of each statement. In this paper, we propose two approaches to improve the situations of deleted faulty statements. For the first approach, called Revised PCA with Ensemble Weight Integration (RPCA-EWI), it updates the contribution value of each statement based on revised PCA and incorporate the results of different combinations of failed and passed test cases. For the second approach, called Revised PCA with Important List Checking (RPCA-ILC), we establish a list of the top N% important statements by using the results of different test case combinations. If the deleted statement appears within this list, preserve it in reduced coverage data. Otherwise, it discards directly. We selected three Linux open-source codes (Gzip, Grep, and Sed) with 4 fault injections to validate the correctness. From the analysis of various perspectives, experimental results show that there is a significant improvement in shortening execution time of the FL process, and also can alleviate the situations for removed faulty statements compared to PCA and the revised PCA methods. © 2025
Author keywords: Ensemble weight; Multiple fault localization; Revised PCA; Software debugging
Index keywords: Computer debugging; Linux; Open source software; Ensemble weight; Fault localization; Multiple fault localization; Multiple faults; Performance; Principal-component analysis; Revised principal component analyze; Software debugging; Software fault localization; Test case; Program debugging
Document type: Article
Conference: 
Source title: Journal of Systems and Software
Year: 2025
EID: 2-s2.0-85219092024
DOI: 10.1016/j.jss.2025.112388
Retrieval channels: authoritative_outlet_search
Local full-text files: 

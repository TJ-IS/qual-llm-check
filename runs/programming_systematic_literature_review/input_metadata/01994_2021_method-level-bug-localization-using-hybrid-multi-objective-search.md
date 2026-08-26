---
otero_id: "2-s2.0-85096180077"
title: "Method-level bug localization using hybrid multi-objective search"
authors: "Almhana R.; Kessentini M.; Mkaouer W."
year: "2021"
journal: "Information and Software Technology"
doi: "10.1016/j.infsof.2020.106474"
---
# Scopus title-abstract-keyword metadata
Title: Method-level bug localization using hybrid multi-objective search
Abstract: Context: One of the time-consuming maintenance tasks is the localization of bugs especially in large software systems. Developers have to follow a tedious process to reproduce the abnormal behavior then inspect a large number of files. While several studies have been proposed for bugs localization, the majority of them are recommending classes/files as outputs which may still require high inspection effort. Furthermore, there is a significant difference between the natural language used in bug reports and the programming language which limits the efficiency of existing approaches since most of them are mainly based on lexical similarity. Objective: In this paper, we propose an automated approach to find and rank the potential methods in order to localize the source of a bug based on a bug report description. Method: Our approach finds a good balance between minimizing the number of recommended classes and maximizing the relevance of the proposed solution using a hybrid multi-objective optimization algorithm combining local and global search. The relevance of the recommended code fragments is estimated based on the use of the history of changes and bug-fixing, and the lexical similarity between the bug report description and the API documentation. Our approach operates on two main steps. The first step is to find the best set of classes satisfying the two conflicting criteria of relevance and the number of classes to recommend using a global search based on NSGA-II. The second step is to locate the most appropriate methods to inspect, using a local multi-objective search based on Simulated Annealing (MOSA) from the list of classes recommended by the first step. Results: We evaluated our system on 6 open source Java projects, using the version of the project before fixing the bug of many bug reports. Our hybrid multi-objective approach is able to successfully locate the true buggy methods within the top 10 recommendations for over 78% of the bug reports leading to a significant reduction of developers’ effort comparing to class-level bug localization techniques. Conclusion: The experimental results show that the search-based approach significantly outperforms four state-of-the-art methods in recommending relevant files for bug reports. © 2020
Author keywords: Bug reports; Bugs localization; Fault localization; Multi-objective search; Search-based software engineering; Simulated annealing; Software maintenance
Index keywords: Application programming interfaces (API); Inspection; Multiobjective optimization; Open source software; Open systems; Simulated annealing; Automated approach; Bug localizations; Large software systems; Lexical similarity; Maintenance tasks; Minimizing the number of; Potential methods; State-of-the-art methods; Program debugging
Document type: Article
Conference: 
Source title: Information and Software Technology
Year: 2021
EID: 2-s2.0-85096180077
DOI: 10.1016/j.infsof.2020.106474
Retrieval channels: authoritative_outlet_search
Local full-text files: 

---
otero_id: "2-s2.0-85182933367"
title: "Range Specification Bug Detection in Flight Control System Through Fuzzing"
authors: "Han R.; Ma S.; Li J.; Nepal S.; Lo D.; Ma Z.; Ma J."
year: "2024"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2024.3354739"
---
# Scopus title-abstract-keyword metadata
Title: Range Specification Bug Detection in Flight Control System Through Fuzzing
Abstract: Developers and manufacturers provide configurable control parameters for flight control programs to support various environments and missions, along with suggested ranges for these parameters to ensure flight safety. However, this flexible mechanism can also introduce a vulnerability known as range specification bugs. The vulnerability originates from the evidence that certain combinations of parameter values may affect the drone's physical stability even though its parameters are within the suggested range. The paper introduces a novel system called icsearcher, designed to identify incorrect configurations or unreasonable combinations of parameters and suggest more reasonable ranges for these parameters. icsearcher applies a metaheuristic search algorithm to find configurations with a high probability of driving the drone into unstable states. In particular, icsearcher adopts a machine learning-based predictor to assist the searcher in evaluating the fitness of configuration. Finally, leveraging searched incorrect configurations, icsearcher can summarize the feasible ranges through multi-objective optimization. icsearcher applies a predictor to guide the search, which eliminates the need for realistic/simulation executions when evaluating configurations and further promotes search efficiency. We have carried out experimental evaluations of icsearcher in different control programs. The evaluation results show that the system successfully reports potentially incorrect configurations, of which over 94% leads to unstable states. © 1976-2012 IEEE.
Author keywords: configuration test; deep learning approximation; Drone security; range specification bug
Index keywords: Aircraft control; Aircraft detection; Computer control systems; Deep learning; Drones; Flight control systems; Multiobjective optimization; Program debugging; Aerospace control; Bug detection; Code; Computer bugs; Configuration test; Deep learning approximation; Drone security; Fuzzing; Range specification bug; Unstable state; Specifications
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2024
EID: 2-s2.0-85182933367
DOI: 10.1109/tse.2024.3354739
Retrieval channels: authoritative_outlet_search
Local full-text files: 

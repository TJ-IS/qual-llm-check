---
otero_id: "2-s2.0-105041400598"
title: "Are we too focused on single query language? Investigating text-to-SQL/SPARQL/Cypher task complexity via fine-tuning unbiased T5 models"
authors: "Vejvar M.; Fujimoto Y."
year: "2026"
journal: "Neurocomputing"
doi: "10.1016/j.neucom.2026.134202"
---
# Scopus title-abstract-keyword metadata
Title: Are we too focused on single query language? Investigating text-to-SQL/SPARQL/Cypher task complexity via fine-tuning unbiased T5 models
Abstract: Text-to-query research remains dominated by SQL, even though many applications require graph query languages such as SPARQL and Cypher. We argue that query language and data model choice should be tested rather than assumed. To study this, we introduce Spider4SSC, a multi-domain benchmark with semantically equivalent SQL, SPARQL, and Cypher queries, and fine-tune unbiased-T5 (uT5) models pre-trained on explicitly filtered plain text. We evaluate execution accuracy (EX) across query language, estimated query complexity, pre-training composition, schema representation, input length, and joint multi-language fine-tuning. In clean uT5 setting, the unseen test set shows a clear performance hierarchy. SQL reaches 29.7% EX, Cypher reaches 23.9%, and SPARQL reaches 17.2%. This hierarchy depends on query hardness. SQL outperforms Cypher on easy validation queries at 58% vs 50% EX, while Cypher performs better on hard queries at 14% vs 6%. Across languages, execution accuracy generally decreases as estimated query complexity increases. Pre-training composition has a smaller effect than query language choice and data scale. For SPARQL, injecting raw SPARQL into pre-training data slightly lowers unseen-test EX from 17.2% to ca. 16.0%. For Cypher Full Compact schemas, increasing context from 512 to 2048 tokens (reducing truncation from 14.52% to 0.52%) improves validation EX from 35.20% to 39.47%. Finally, joint fine-tuning over SQL, SPARQL, and Cypher gives a small regularising benefit, improving all three languages and raising average unseen-test EX from 18.19% to 18.63%. Overall, our results suggest that query language should be selected empirically for the target task rather than assumed in advance. © 2026 The Author(s)
Author keywords: Cypher; Data models; Database systems; Graph database; Query complexity; Relational database; SPARQL; SQL; T5; Text-to-query
Index keywords: Graph Databases; Query languages; Query processing; Search engines; Structured Query Language; Tuning; Cipher; Fine tuning; Graph database; Pre-training; Query complexity; Relational Database; SPARQL; T5; Task complexity; Text-to-query; article; benchmarking; clinical article; controlled study; data base; hardness; human; retrospective study; Relational database systems
Document type: Article
Conference: 
Source title: Neurocomputing
Year: 2026
EID: 2-s2.0-105041400598
DOI: 10.1016/j.neucom.2026.134202
Retrieval channels: forward_citation_of_20_seeds
Local full-text files: 

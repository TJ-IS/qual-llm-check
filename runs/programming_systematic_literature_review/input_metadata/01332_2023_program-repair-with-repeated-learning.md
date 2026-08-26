---
otero_id: "2-s2.0-85127811952"
title: "Program Repair With Repeated Learning"
authors: "Chen L.; Pei Y.; Pan M.; Zhang T.; Wang Q.; Furia C.A."
year: "2023"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2022.3164662"
---
# Scopus title-abstract-keyword metadata
Title: Program Repair With Repeated Learning
Abstract: A key challenge in generate-and-validate automated program repair is directing the search for fixes so that it can efficiently find those that are more likely to be correct. To this end, several techniques use machine learning to capture the features of programmer-written fixes. In existing approaches, fitting the model typically takes place before fix generation and is independent of it: the fix generation process uses the learned model as one of its inputs. However, the intermediate outcomes of an ongoing fix generation process often provide valuable information about which candidate fixes were 'better'; this information could profitably be used to retrain the model, so that each new iteration of the fixing process would also learn from the outcome of previous ones. In this paper, we propose the Liana technique for automated program repair, which is based on this idea of repeatedly learning the features of generated fixes. To this end, Liana uses a fine-grained model that combines information about fix characteristics, their relations to the fixing context, and the results of test execution. The model is initially trained offline, and then repeatedly updated online as the fix generation process unravels; at any step, the most up-to-date model is used to guide the search for fixes - prioritizing those that are more likely to include the right ingredients. In an experimental evaluation on 732 real-world Java bugs from 3 popular benchmarks, Liana built correct fixes for 134 faults (83 ranked as first in its output) - improving over several other generate-and-validate program repair tools according to various measures.  © 1976-2012 IEEE.
Author keywords: Automated program repair (APR); generate-and-validate APR; learning-to-rank; repeated learning
Index keywords: Iterative methods; Program debugging; Experimental evaluation; Fine grained; Generation process; Grained models; Learn+; Machine-learning; Offline; Real-world; Repair tools; Test execution; Repair
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2023
EID: 2-s2.0-85127811952
DOI: 10.1109/tse.2022.3164662
Retrieval channels: authoritative_outlet_search
Local full-text files: 

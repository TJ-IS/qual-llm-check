---
otero_id: "2-s2.0-85133254771"
title: "Free Lunch for Testing: Fuzzing Deep-Learning Libraries from Open Source"
authors: "Wei A.; Deng Y.; Yang C.; Zhang L."
year: "2022"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3510003.3510041"
---
# Scopus title-abstract-keyword metadata
Title: Free Lunch for Testing: Fuzzing Deep-Learning Libraries from Open Source
Abstract: Deep learning (DL) systems can make our life much easier, and thus are gaining more and more attention from both academia and industry. Meanwhile, bugs in DL systems can be disastrous, and can even threaten human lives in safety-critical applications. To date, a huge body of research efforts have been dedicated to testing DL models. However, interestingly, there is still limited work for testing the underlying DL libraries, which are the foundation for building, optimizing, and running DL models. One potential reason is that test generation for the underlying DL libraries can be rather challenging since their public APIs are mainly exposed in Python, making it even hard to automatically determine the API input parameter types due to dynamic typing. In this paper, we propose FreeFuzz, the first approach to fuzzing DL libraries via mining from open source. More specifically, FreeFuzz obtains code/models from three different sources: 1) code snippets from the library documentation, 2) library developer tests, and 3) DL models in the wild. Then, FreeFuzz automatically runs all the collected code/models with instrumentation to trace the dynamic information for each covered API, including the types and values of each parameter during invocation, and shapes of input/output tensors. Lastly, FreeFuzz will leverage the traced dynamic information to perform fuzz testing for each covered API. The extensive study of FreeFuzz on PyTorch and TensorFlow, two of the most popular DL libraries, shows that FreeFuzz is able to automatically trace valid dynamic information for fuzzing 1158 popular APIs, 9X more than state-of-the-art LEMON with 3.5X lower overhead than LEMON. To date, FreeFuzz has detected 49 bugs for PyTorch and TensorFlow (with 38 already confirmed by developers as previously unknown). © 2022 ACM.
Author keywords: 
Index keywords: Application programming interfaces (API); Citrus fruits; Deep learning; Program debugging; Safety engineering; Dynamic information; Dynamic typing; Human lives; Input parameter; Learning models; Library developers; Open-source; Research efforts; Safety critical applications; Test generations; Libraries
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2022
EID: 2-s2.0-85133254771
DOI: 10.1145/3510003.3510041
Retrieval channels: authoritative_outlet_search
Local full-text files: 

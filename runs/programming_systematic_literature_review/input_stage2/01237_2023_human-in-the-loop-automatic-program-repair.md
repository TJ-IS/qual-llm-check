---
otero_id: "2-s2.0-85168713494"
title: "Human-in-the-Loop Automatic Program Repair"
authors: "Geethal C.; Bohme M.; Pham V.-T."
year: "2023"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2023.3305052"
---
# Scopus title-abstract-keyword metadata
Title: Human-in-the-Loop Automatic Program Repair
Abstract: learn2fix is a human-in-the-loop interactive program repair technique, which can be applied when no bug oracle - except the user who is reporting the bug - is available. This approach incrementally learns the condition under which the bug is observed by systematic negotiation with the user. In this process, learn2fix generates alternative test inputs and sends some of those to the user for obtaining their labels. A limited query budget is assigned to the user for this task. A query is a Yes/No question: 'When executing this alternative test input, the program under test produces the following output; is the bug observed?'. Using the labelled test inputs, learn2fix incrementally learns an automatic bug oracle to predict the user's response. A classification algorithm in machine learning is used for this task. Our key challenge is to maximise the oracle's accuracy in predicting the tests that expose the bug given a practical, small budget of queries. After learning the automatic oracle, an existing program repair tool attempts to repair the bug using the alternative tests that the user has labelled. Our experiments demonstrate that learn2fix trains a sufficiently accurate automatic oracle with a reasonably low labelling effort (lt. 20 queries), and the oracles represented by interpolation-based classifiers produce more accurate predictions than those represented by approximation-based classifiers. Given the user-labelled test inputs, generated using the interpolation-based approach, the GenProg and Angelix automatic program repair tools produce patches that pass a much larger proportion of validation tests than the manually constructed test suites provided by the repair benchmark.  © 1976-2012 IEEE.
Author keywords: active machine learning; Automated test oracles; classification algorithms; semi-automatic program repair
Index keywords: Artificial intelligence; Budget control; Costs; Forecasting; Interpolation; Learning algorithms; Learning systems; Program debugging; Query processing; Software testing; Active machine learning; Automated test; Automated test oracle; Automatic programs; Classification algorithm; Computer bugs; Fuzzing; Human-in-the-loop; Labelings; Semi-automatic program repair; Semi-automatics; Test oracles; Repair
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2023
EID: 2-s2.0-85168713494
DOI: 10.1109/tse.2023.3305052
Retrieval channels: authoritative_outlet_search
Local full-text files: 

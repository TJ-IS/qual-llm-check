---
otero_id: "2-s2.0-85140728317"
title: "PopArt: Ranked Testing Efficiency"
authors: "Bousy I.P.; Barr E.T.; Clark D."
year: "2023"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2022.3214796"
---
# Scopus title-abstract-keyword metadata
Title: PopArt: Ranked Testing Efficiency
Abstract: Too often, programmers are under pressure to maximize their confidence in the correctness of their code with a tight testing budget. Should they spend some of that budget on finding 'interesting' inputs or spend their entire testing budget on test executions? Work on testing efficiency has explored two competing approaches to answer this question: systematic partition testing (ST), which defines a testing partition and tests its parts, and random testing (RT), which directly samples inputs with replacement. A consensus as to which is better when has yet to emerge. We present Probability Ordered Partition Testing (PopArt), a new systematic partition-based testing strategy that visits the parts of a testing partition in decreasing probability order and in doing so leverages any non-uniformity over that partition. We show how to construct a homogeneous testing partition, a requirement for systematic testing, by using an executable oracle and the path partition. A program's path partition is a naturally occurring testing partition that is usually skewed for the simple reason that some paths execute more frequently than others. To confirm this conventional wisdom, we instrument programs from the Codeflaws repository and find that 80% of them have a skewed path probability distribution. PopArt visits the parts of a testing partition in decreasing probability order. We then compare PopArt with RT to characterise the configuration space in which each is more efficient. We show that, when simulating Codeflaws, PopArt outperforms RT after $100{,}000$100,000 executions. Our results reaffirm RT's power for very small testing budgets but also show that for any application requiring high (above 90%) probability-weighted coverage PopArt should be preferred. In such cases, despite paying more for each test execution, we prove that PopArt outperforms RT: it traverses parts whose cumulative probability bounds that of random testing, showing that sampling without replacement pays for itself, given a nonuniform probability over a testing partition.  © 1976-2012 IEEE.
Author keywords: efficiency; probability distribution; randomness; Software testing; systematic
Index keywords: Budget control; Costs; Efficiency; Entropy; Instrument testing; Program debugging; Software testing; Computer bugs; Nonuniformity; Partition testing; Probability order; Probability: distributions; Random testing; Systematic; Test execution; Testing efficiency; Testing strategies; Probability distributions
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2023
EID: 2-s2.0-85140728317
DOI: 10.1109/tse.2022.3214796
Retrieval channels: authoritative_outlet_search
Local full-text files: 

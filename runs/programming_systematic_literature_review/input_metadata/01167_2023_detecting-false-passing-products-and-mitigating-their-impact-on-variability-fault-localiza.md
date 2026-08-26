---
otero_id: "2-s2.0-85139305437"
title: "Detecting false-passing products and mitigating their impact on variability fault localization in software product lines"
authors: "Nguyen T.-T.; Ngo K.-T.; Nguyen S.; Vo H.D."
year: "2023"
journal: "Information and Software Technology"
doi: "10.1016/j.infsof.2022.107080"
---
# Scopus title-abstract-keyword metadata
Title: Detecting false-passing products and mitigating their impact on variability fault localization in software product lines
Abstract: In a Software Product Line (SPL) system, variability bugs can cause failures in certain products (buggy products), not in the others. In practice, variability bugs are not always exposed, and buggy products can still pass all the tests due to their ineffective test suites (so-called false-passing products). The misleading indications caused by those false-passing products’ test results can negatively impact variability fault localization performance. In this paper, we introduce CLAP, a novel approach to detect false-passing products in SPL systems failed by variability bugs. Our key idea is that given a set of tested products of an SPL system, we collect failure indications in failing products based on their implementation and test quality. For a passing product, we evaluate these indications, and the stronger indications, the more likely the product is false-passing. Specifically, the possibility of the product to be false-passing is evaluated based on if it has a large number of the statements which are highly suspicious in the failing products, and if its test suite is in lower quality compared to the failing products’ test suites. We conducted several experiments to evaluate our false-passing product detection approach on a large benchmark of 14,191 false-passing products and 22,555 true-passing products in 823 buggy versions of the existing SPL systems. The experimental results show that CLAP can effectively detect false-passing and true-passing products with the average accuracy of more than 90%. Especially, the precision of false-passing product detection by CLAP is up to 96%. This means, among 10 products predicted as false-passing products, more than 9 products are precisely detected. Furthermore, we propose two simple and effective methods to mitigate the negative impact of false-passing products on variability fault localization. These methods can improve the performance of the state-of-the-art variability fault localization techniques by up to 34%. © 2022 Elsevier B.V.
Author keywords: Coincidental correctness; False-passing products; Fault localization; Software product line; Variability bugs
Index keywords: Computer software; Fault detection; Quality control; Software design; Coincidental correctness; False-passing product; Fault localization; Impact variabilities; Localization performance; Low qualities; Product detection; Software Product Line; Test quality; Variability bug; Program debugging
Document type: Article
Conference: 
Source title: Information and Software Technology
Year: 2023
EID: 2-s2.0-85139305437
DOI: 10.1016/j.infsof.2022.107080
Retrieval channels: authoritative_outlet_search
Local full-text files: 

---
otero_id: "2-s2.0-105010295291"
title: "WDD: Weighted Delta Debugging"
authors: "Zhou X.; Xu Z.; Zhang M.; Tian Y.; Sun C."
year: "2025"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse55347.2025.00071"
---
# Scopus title-abstract-keyword metadata
Title: WDD: Weighted Delta Debugging
Abstract: Delta Debugging is a widely used family of algorithms (e.g., ddmin and ProbDD) to automatically minimize bug-triggering test inputs, thus to facilitate debugging. It takes a list of elements with each element representing a fragment of the test input, systematically partitions the list at different granularities, identifies and deletes bug-irrelevant partitions. Prior delta debugging algorithms assume there are no differences among the elements in the list, and thus treat them uniformly during partitioning. However, in practice, this assumption usually does not hold, because the size (referred to as weight) of the fragment represented by each element can vary significantly. For example, a single element representing 50% of the test input is much more likely to be bug-relevant than elements representing only 1%. This assumption inevitably impairs the efficiency or even effectiveness of these delta debugging algorithms. This paper proposes Weighted Delta Debugging (WDD), a novel concept to help prior delta debugging algorithms overcome the limitation mentioned above. The key insight of WDD is to assign each element in the list a weight according to its size, and distinguish different elements based on their weights during partitioning. We designed two new minimization algorithms, Wddmin and WProbDD, by applying WDD to ddmin and ProbDD respectively. We extensively evaluated Wddmin and WProbDD in two representative applications, HDD and Perses, on 62 benchmarks across two languages. On average, with Wddmin, HDD and Perses took 51.31% and 7.47% less time to generate 9.12% and 0.96% smaller results than with ddmin, respectively. With WProbDD, HDD and Perses used 11.98% and 9.72% less time to generate 13.40% and 2.20% smaller results than with ProbDD, respectively. The results strongly demonstrate the value of WDD. We firmly believe that WDD opens up a new dimension to improve test input minimization techniques.  © 2025 IEEE.
Author keywords: Delta Debugging; Program Reduction; Test Input Minimization
Index keywords: Benchmarking; Computer debugging; Design for testability; Software testing; Systems analysis; % reductions; Debugging algorithms; Delta debugging; Different granularities; Minimisation; Novel concept; Program reduction; Single element; Test input minimization; Test inputs; Program debugging
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2025
EID: 2-s2.0-105010295291
DOI: 10.1109/icse55347.2025.00071
Retrieval channels: authoritative_outlet_search
Local full-text files: 

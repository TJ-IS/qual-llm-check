---
otero_id: "2-s2.0-85149859362"
title: "Invalidator: Automated Patch Correctness Assessment Via Semantic and Syntactic Reasoning"
authors: "Le-Cong T.; Luong D.-M.; Le X.B.D.; Lo D.; Tran N.-H.; Quang-Huy B.; Huynh Q.-T."
year: "2023"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2023.3255177"
---
# Scopus title-abstract-keyword metadata
Title: Invalidator: Automated Patch Correctness Assessment Via Semantic and Syntactic Reasoning
Abstract: Automated program repair (APR) faces the challenge of test overfitting, where generated patches pass validation tests but fail to generalize. Existing methods for patch assessment involve generating new tests or manual inspection, which can be time-consuming or biased. In this paper, we propose a novel technique, Invalidator, to automatically assess the correctness of APR-generated patches via semantic and syntactic reasoning. Invalidator leverages program invariants to reason about program semantics while also capturing program syntax through language semantics learned from a large code corpus using a pre-trained language model. Given a buggy program and the developer-patched program, Invalidator infers likely invariants on both programs. Then, Invalidator determines that an APR-generated patch overfits if: (1) it violates correct specifications or (2) maintains erroneous behaviors from the original buggy program. In case our approach fails to determine an overfitting patch based on invariants, Invalidator utilizes a trained model from labeled patches to assess patch correctness based on program syntax. The benefit of Invalidator is threefold. First, Invalidator leverages both semantic and syntactic reasoning to enhance its discriminative capability. Second, Invalidator does not require new test cases to be generated, but instead only relies on the current test suite and uses invariant inference to generalize program behaviors. Third, Invalidator is fully automated. Experimental results demonstrate that Invalidator outperforms existing methods in terms of Accuracy and F-measure, correctly identifying 79% of overfitting patches and detecting 23% more overfitting patches than the best baseline.  © 1976-2012 IEEE.
Author keywords: Automated patch correctness assessment; automated program repair; code representations; overfitting problem; program invariants
Index keywords: Automation; Codes (symbols); Semantics; Software testing; Syntactics; Automated patch correctness assessment; Automated program repair; Code representation; Ground truth; Manual inspection; Over fitting problem; Overfitting; Program invariants; Test case; Validation test; Repair
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2023
EID: 2-s2.0-85149859362
DOI: 10.1109/tse.2023.3255177
Retrieval channels: authoritative_outlet_search
Local full-text files: 

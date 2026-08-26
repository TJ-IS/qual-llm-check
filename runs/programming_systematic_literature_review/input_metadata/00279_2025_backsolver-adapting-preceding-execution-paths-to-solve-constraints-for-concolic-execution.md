---
otero_id: "2-s2.0-86000581405"
title: "Backsolver: Adapting Preceding Execution Paths to Solve Constraints for Concolic Execution"
authors: "Zeng Y.; Song Z.; Lv G.; Zhou Y.; Zhu H.; Sun L."
year: "2025"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3712194"
---
# Scopus title-abstract-keyword metadata
Title: Backsolver: Adapting Preceding Execution Paths to Solve Constraints for Concolic Execution
Abstract: Concolic execution follows the execution paths of concrete inputs, capable of generating new inputs for unexplored code by solving negated path constraints. However, implicit flows can hinder concolic execution, reducing the code coverage. Implicit flows occur when inputs influence control flow, and the control flow variation affects the values of some variables. During concolic execution, the preceding path selections limit the potential values of these variables. This limitation may result in unsolvable constraints, subsequently restricting the generation of new inputs for unexplored paths. Our insight is that following the same preceding paths is unnecessary, and we can adapt preceding paths to make the latest constraints solvable. We divide states into general states and implicit-flow-solving states (IFSSs). We utilize the general states to perform concolic execution. When solving constraints influenced by implicit flows, we switch to the IFSSs. We use the IFSSs to explore the relevant code region and adapt paths. To mitigate path explosion and construct the relation between inputs and the variables, we merge the IFSSs. State merging does not burden the general states, and we limit the code regions for the IFSSs to minimize the introduced overhead. Finally, we replace the variable symbols in the target constraints with new expressions and attempt to solve the new constraints. We implement our approach in Backsolver and build a test suite to evaluate it. Backsolver successfully identifies all the implicit flows in the test suite and resolves most of them. When evaluated on six real-world binaries, Backsolver resolves the highest number of branches related to implicit flows in total. Besides, Backsolver has the highest code coverage in PlutoSVG and finds a 0-day vulnerability. We reported the vulnerability and obtained a CVE ID.  © 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: concolic execution; fuzzing; implicit flow; state merging
Index keywords: Program debugging; Code coverage; Concolic execution; Control-flow; Execution paths; Fuzzing; Implicit flow; Influence controls; Input influence; Path constraint; State-merging
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2025
EID: 2-s2.0-86000581405
DOI: 10.1145/3712194
Retrieval channels: authoritative_outlet_search
Local full-text files: 

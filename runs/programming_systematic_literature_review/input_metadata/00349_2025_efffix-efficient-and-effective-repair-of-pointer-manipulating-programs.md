---
otero_id: "2-s2.0-86000547687"
title: "EffFix: Efficient and Effective Repair of Pointer Manipulating Programs"
authors: "Zhang Y.; Costea A.; Shariffdeen R.; McCall D.; Roychoudhury A."
year: "2025"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3705310"
---
# Scopus title-abstract-keyword metadata
Title: EffFix: Efficient and Effective Repair of Pointer Manipulating Programs
Abstract: This work introduces EffFix, a tool that applies a novel static analysis-driven automated program repair (APR) technique for fixing memory errors. APR tools typically rely on a given test-suite to guide the repair process. Apart from the need to provide test oracles, this reliance is also one of the main contributors to the over-fitting problem. Static analysis based APR techniques bypass these issues only to introduce new ones, such as soundness, scalability, and generalizability. This work demonstrates how we can overcome these challenges and achieve sound memory bug repair at scale by leveraging static analysis (specifically incorrectness separation logic (ISL)) to guide repair. This is the first repair approach to use ISL. Our key insight is that the abstract domain used by static analysis to detect the bugs also contains key information to derive correct patches. Our proposed approach learns what a desirable patch is by inspecting how close a patch is to fixing the bug based on the feedback from ISL based static analysis (specifically the Pulse analyzer), and turning this information into a distribution of probabilities over context free grammars. This approach to repair is generic in that its learning strategy allows for finding patches without relying on the commonly used patch templates. Furthermore, to achieve efficient program repair, instead of focusing on heuristics for reducing the search space of patches, we make repair scalable by creating classes of equivalent patches according to the effect they have on the symbolic heap. We then conduct candidate patch validation only once per patch equivalence class. This allows EffFix to efficiently discover quality repairs even in the presence of a large pool of patch candidates. Experimental evaluation of fixing real world memory errors in medium to large scale subjects like OpenSSL, Linux Kernel, swoole, shows the efficiency and effectiveness of EffFix - in terms of automatically producing repairs from large search spaces. In particular, EffFix has a fix ratio of 66% for memory leak bugs and 83% for Null Pointer Dereferences for the considered dataset.  © 2025 Copyright held by the owner/author(s).
Author keywords: Automated Program Repair; Incorrectness Separation Logic; Probabilistic Context Free Grammars
Index keywords: Computer debugging; Computer software selection and evaluation; Health risks; Linux; Model checking; Normal distribution; Program debugging; Risk assessment; Software testing; Automated program repair; Incorrectness separation logic; Memory error; Probabilistic context free grammars; Repair process; Repair techniques; Repair tools; Search spaces; Separation logic; Test oracles; Probabilistic logics
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2025
EID: 2-s2.0-86000547687
DOI: 10.1145/3705310
Retrieval channels: authoritative_outlet_search
Local full-text files: 

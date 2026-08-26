---
otero_id: "2-s2.0-85119619578"
title: "Historical Spectrum Based Fault Localization"
authors: "Wen M.; Chen J.; Tian Y.; Wu R.; Hao D.; Han S.; Cheung S.-C."
year: "2021"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2019.2948158"
---
# Scopus title-abstract-keyword metadata
Title: Historical Spectrum Based Fault Localization
Abstract: Spectrum-based fault localization (SBFL) techniques are widely studied and have been evaluated to be effective in locating faults. Recent studies also showed that developers from industry value automated SBFL techniques. However, their effectiveness is still limited by two main reasons. First, the test coverage information leveraged to construct the spectrum does not reflect the root cause directly. Second, SBFL suffers from the tie issue so that the buggy code entities can not be well differentiated from non-buggy ones. To address these challenges, we propose to leverage the information of version histories in fault localization based on the following two intuitions. First, version histories record how bugs are introduced to software projects and this information reflects the root cause of bugs directly. Second, the evolution histories of code can help differentiate those suspicious code entities ranked in tie by SBFL. Our intuitions are also inspired by the observations on debugging practices from large open source projects and industry. Based on the intuitions, we propose a novel technique HSFL (historical spectrum based fault localization). Specifically, HSFL identifies bug-inducing commits from the version history in the first step. It then constructs historical spectrum (denoted as Histrum) based on bug-inducing commits, which is another dimension of spectrum orthogonal to the coverage based spectrum used in SBFL. HSFL finally ranks the suspicious code elements based on our proposed Histrum and the conventional spectrum. HSFL outperforms the state-of-the-art SBFL techniques significantly on the Defects4J benchmark. Specifically, it locates and ranks the buggy statement at Top-1 for 77.8 percent more bugs as compared with SBFL, and 33.9 percent more bugs at Top-5. Besides, for the metrics MAP and MRR, HSFL achieves an average improvement of 28.3 and 40.8 percent over all bugs, respectively. Moreover, HSFL can also outperform other six families of fault localization techniques, and our proposed Histrum model can be integrated with different families of techniques and boost their performance. © 1976-2012 IEEE.
Author keywords: bug-inducing commits; Fault localization; version histories
Index keywords: Codes (symbols); Open systems; Program debugging; Bug-inducing commit; Evolution history; Fault localization; Localization technique; Open source projects; Root cause; Software project; Spectra's; Test-coverage; Version history; Open source software
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2021
EID: 2-s2.0-85119619578
DOI: 10.1109/tse.2019.2948158
Retrieval channels: authoritative_outlet_search
Local full-text files: 

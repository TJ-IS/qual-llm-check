---
otero_id: "2-s2.0-85111038238"
title: "The Ghost Commit Problem When Identifying Fix-Inducing Changes: An Empirical Study of Apache Projects"
authors: "Rezk C.; Kamei Y.; McIntosh S."
year: "2022"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2021.3087419"
---
# Scopus title-abstract-keyword metadata
Title: The Ghost Commit Problem When Identifying Fix-Inducing Changes: An Empirical Study of Apache Projects
Abstract: The SZZ approach for identifying fix-inducing changes traces backwards from a commit that fixes a defect to those commits that are implicated in the fix. This approach is at the heart of studies of characteristics of fix-inducing changes, as well as the popular Just-in-Time (JIT) variant of defect prediction. However, some types of commits are invisible to the SZZ approach. We refer to these invisible commits as 'Ghost Commits.' In this paper, we set out to define, quantify, characterize, and mitigate ghost commits that impact the SZZ algorithm during its mapping (i.e., linking defect-fixing commits to those commits that are implicated by the fix) and filtering phases (i.e., removing improbable fix-inducing commits from the set of implicated commits). We mine the version control repositories of 14 open source Apache projects for instances of mapping-phase and filtering-phase ghost commits. We find that (1) 5.66-11.72 percent of defect-fixing commits of defect-fixing commits only add lines, and thus, cannot be mapped back to implicated commits; (2) 1.05-4.60 percent of the studied commits only remove lines, and thus, cannot be implicated in future fixes; and (3) that no implicated commits survive the filtering process of 0.35-14.49 percent defect-fixing commits. Qualitative analysis of ghost commits reveals that 46.5 percent of 142 addition-only defect-fixing commits add checks (e.g., null-ness or emptiness checks), while 39.7 percent of 307 removal-only commits clean up (unused) code. Our results suggest that the next generation of SZZ improvements should be language-aware to connect ghost commits to implicated and defect-fixing commits. Based on our observations, we discuss promising directions for mitigation strategies to address each type of ghost commit. Moreover, we implement mitigation strategies for addition-only commits and evaluate those strategies with respect to a baseline approach. The results indicate that our strategies achieve a precision of 0.753, improving the precision of implicated commits by 39.5 percentage points. © 1976-2012 IEEE.
Author keywords: defect-fixing changes; fix-inducing changes; SZZ
Index keywords: Bandpass filters; Computer software maintenance; Costs; Data mining; Just in time production; Mapping; Open source software; Program debugging; Computer bugs; Defect prediction; Defect-fixing change; Empirical studies; Fix-inducing change; Information filter; Just-in-time; Mitigation strategy; SZZ; Time variant; Defects
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2022
EID: 2-s2.0-85111038238
DOI: 10.1109/tse.2021.3087419
Retrieval channels: authoritative_outlet_search
Local full-text files: 

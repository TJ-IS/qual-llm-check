---
otero_id: "2-s2.0-105039674848"
title: "Is this build failure related to my patch? An empirical study of unrelated build failures in continuous integration"
authors: "Huang Y.A.; da Costa D.A.; Dick G.; El Mezouar M.; Xiao L."
year: "2026"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-026-10874-8"
---
# Scopus title-abstract-keyword metadata
Title: Is this build failure related to my patch? An empirical study of unrelated build failures in continuous integration
Abstract: In a hectic Continuous Integration (CI) environment, where several builds are triggered concurrently, legitimate build failures (e.g., not caused by flaky tests) may not always be related to the current push. These unrelated build failures can burden developers as they devote hours to attest whether errors are truly associated with their present changes. In this paper, we extract 77,354 CI build failures from 7 open source projects to understand and identify unrelated build failures. We attempt to provide an indication for developers about whether a build failure is likely to be related to the current push or not. Our results reveal that developers likely invest a median of 4 hours to determine whether a build failure is (un)related to their pushes. We perform a document analysis on a sample of 371 unrelated build failures (based on the 95% confidence level and 5% confidence interval from 10,316 potentially unrelated failures) to understand why build failures are deemed as unrelated by developers. The themes generated from our document analysis reveal that unrelated tests failures represent 20% of the cases of why build failures are deemed unrelated by developers. To predict whether a build failure is unrelated to the current push, we extract 33 features from issue reports, issue comments, and from the commits pertaining to the triggering push. We build semi-supervised PU-learning models over seven Apache projects and achieve precision ranging from to, recall ranging from to, and F1-scores ranging from to, while the area under the ROC curve (AUC) spans to. Our analysis of feature importance reveals that (i) the time taken from a submitted patch to the build-triggering push (CI latency), (ii) build failures sharing similar error messages with recent failures, and (iii) the number of comments preceding the build failure, are all efficient indicators for identifying potential unrelated build failures. The semi-supervised approach proposed in this work can help developers identify build failures that are unrelated to their current push, providing actionable guidance such as re-running builds, inspecting infrastructure logs, or prioritizing code-level debugging based on prediction outcomes. © The Author(s) 2026.
Author keywords: Continuous Integration (CI); Empirical study; Issue resolving; Non-code-related failures
Index keywords: Integration testing; Open source software; Open systems; Program debugging; Semi-supervised learning; 'current; Continuous integration; Continuous integrations; Documents analysis; Empirical studies; Integration environments; Issue resolving; Non-code-related failure; Open source projects; Semi-supervised; Integration
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2026
EID: 2-s2.0-105039674848
DOI: 10.1007/s10664-026-10874-8
Retrieval channels: authoritative_outlet_search
Local full-text files: 

---
otero_id: "2-s2.0-85173002947"
title: "Are Your Dependencies Code Reviewed?: Measuring Code Review Coverage in Dependency Updates"
authors: "Imtiaz N.; Williams L."
year: "2023"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2023.3319509"
---
# Scopus title-abstract-keyword metadata
Title: Are Your Dependencies Code Reviewed?: Measuring Code Review Coverage in Dependency Updates
Abstract: As modern software extensively uses free open source packages as dependencies, developers have to regularly pull in new third-party code through frequent updates. However, without a proper review of every incoming change, vulnerable and malicious code can sneak into the codebase through these dependencies. The goal of this study is to aid developers in securely accepting dependency updates by measuring if the code changes in an update have passed through a code review process. We implement Depdive, an update audit tool for packages in Crates.io, npm, PyPI, and RubyGems registry. Depdive first (i) identifies the files and the code changes in an update that cannot be traced back to the package's source repository, i.e., phantom artifacts; and then (ii) measures what portion of changes in the update, excluding the phantom artifacts, has passed through a code review process, i.e., code review coverage. Using Depdive, we present an empirical study across the latest ten updates of the most downloaded 1000 packages in each of the four registries. We further evaluated our results through a maintainer agreement survey. We find that phantom artifacts are not uncommon in the updates (20.1% of the analyzed updates had at least one phantom file). The phantoms can appear either due to legitimate reasons, such as in the case of programmatically generated files, or from accidental inclusion, such as in the case of files that are ignored in the repository. Regarding code review coverage (CRC), we find the updates are typically only partially code-reviewed (52.5% of the time). Further, only 9.0% of the packages had all their updates in our data set fully code-reviewed, indicating that even the most used packages can introduce non-reviewed code in the software supply chain. We also observe that updates either tend to have high CRC or low CRC, suggesting that packages at the opposite end of the spectrum may require a separate set of treatments.  © 1976-2012 IEEE.
Author keywords: dependency analysis; open source security; Software supply chain security
Index keywords: Codes (symbols); Open source software; Open systems; Phantoms; Software design; Code; Code changes; Code review; Open source package; Phantoms; Review process; Security; Software; Software development management; Source-coding; Supply chains
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2023
EID: 2-s2.0-85173002947
DOI: 10.1109/tse.2023.3319509
Retrieval channels: authoritative_outlet_search
Local full-text files: 

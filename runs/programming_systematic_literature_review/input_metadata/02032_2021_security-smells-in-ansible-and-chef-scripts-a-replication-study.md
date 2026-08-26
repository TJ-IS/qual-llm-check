---
otero_id: "2-s2.0-85099877605"
title: "Security Smells in Ansible and Chef Scripts: A Replication Study"
authors: "Rahman A.; Rahman M.R.; Parnin C.; Williams L."
year: "2021"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3408897"
---
# Scopus title-abstract-keyword metadata
Title: Security Smells in Ansible and Chef Scripts: A Replication Study
Abstract: Context: Security smells are recurring coding patterns that are indicative of security weakness and require further inspection. As infrastructure as code (IaC) scripts, such as Ansible and Chefscripts, are used to provision cloud-based servers and systems at scale, security smells in IaC scripts could be used to enable malicious users to exploit vulnerabilities in the provisioned systems.Goal: The goal of this article is to help practitioners avoid insecure coding practices while developing infrastructure as code scripts through an empirical study of security smells in Ansible and Chef scripts. Methodology: We conduct a replication study where we apply qualitative analysis with 1,956 IaC scripts to identify security smells for IaC scripts written in two languages: Ansible and Chef. We construct a static analysis tool called Security Linter for Ansible and Chef scripts (SLAC) to automatically identify security smells in 50,323 scripts collected from 813 open source software repositories. We also submit bug reports for 1,000 randomly selected smell occurrences. Results:We identify two security smells not reported in prior work: missing default in case statement and no integrity check. By applying SLAC we identify 46,600 occurrences of security smells that include7,849 hard-coded passwords. We observe agreement for 65 of the responded 94 bug reports, which suggests the relevance of security smells for Ansible and Chef scripts amongst practitioners. Conclusion: We observe security smells to be prevalent in Ansible and Chef scripts, similarly to that of the Puppet scripts. We recommend practitioners to rigorously inspect the presence of the identified security smells in Ansible and Chef scripts using (i) code review, and (ii) static analysis tools.  © 2021 ACM.
Author keywords: Ansible; chef; configuration as code; configuration scripts; devops; devsecops; empirical study; infrastructure as code; insecure coding; security; smell; static analysis
Index keywords: Odors; Open source software; Open systems; Cloud-based; Code review; Coding patterns; Empirical studies; Integrity check; Qualitative analysis; Replication study; Security weakness; Static analysis
Document type: Review
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2021
EID: 2-s2.0-85099877605
DOI: 10.1145/3408897
Retrieval channels: authoritative_outlet_search
Local full-text files: 

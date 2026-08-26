---
otero_id: "2-s2.0-85164297169"
title: "Security Misconfigurations in Open Source Kubernetes Manifests: An Empirical Study"
authors: "Rahman A.; Shamim S.I.; Bose D.B.; Pandita R."
year: "2023"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3579639"
---
# Scopus title-abstract-keyword metadata
Title: Security Misconfigurations in Open Source Kubernetes Manifests: An Empirical Study
Abstract: Context: Kubernetes has emerged as the de-facto tool for automated container orchestration. Business and government organizations are increasingly adopting Kubernetes for automated software deployments. Kubernetes is being used to provision applications in a wide range of domains, such as time series forecasting, edge computing, and high-performance computing. Due to such a pervasive presence, Kubernetes-related security misconfigurations can cause large-scale security breaches. Thus, a systematic analysis of security misconfigurations in Kubernetes manifests, i.e., configuration files used for Kubernetes, can help practitioners secure their Kubernetes clusters.Objective: The goal of this paper is to help practitioners secure their Kubernetes clusters by identifying security misconfigurations that occur in Kubernetes manifests.Methodology: We conduct an empirical study with 2,039 Kubernetes manifests mined from 92 open-source software repositories to systematically characterize security misconfigurations in Kubernetes manifests. We also construct a static analysis tool called Security Linter for Kubernetes Manifests (SLI-KUBE) to quantify the frequency of the identified security misconfigurations.Results: In all, we identify 11 categories of security misconfigurations, such as absent resource limit, absent securityContext, and activation of hostIPC. Specifically, we identify 1,051 security misconfigurations in 2,039 manifests. We also observe the identified security misconfigurations affect entities that perform mesh-related load balancing, as well as provision pods and stateful applications. Furthermore, practitioners agreed to fix 60% of 10 misconfigurations reported by us.Conclusion: Our empirical study shows Kubernetes manifests to include security misconfigurations, which necessitates security-focused code reviews and application of static analysis when Kubernetes manifests are developed. © 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: Configuration; container orchestration; devops; devsecops; empirical study; Kubernetes; misconfiguration; security
Index keywords: Containers; Open source software; Open systems; Business organizations; Configuration; Container orchestration; Devops; Devsecop; Empirical studies; Kubernetes; Misconfigurations; Open-source; Security; Static analysis
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2023
EID: 2-s2.0-85164297169
DOI: 10.1145/3579639
Retrieval channels: authoritative_outlet_search
Local full-text files: 

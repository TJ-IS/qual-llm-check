---
otero_id: "2-s2.0-84863954406"
title: "DARWIN: An approach to debugging evolving programs"
authors: "Qi D.; Roychoudhury A.; Liang Z."
year: "2012"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/2211616.2211622"
---
# Scopus title-abstract-keyword metadata
Title: DARWIN: An approach to debugging evolving programs
Abstract: Bugs in programs are often introduced when programs evolve from a stable version to a new version. In this article, we propose a new approach called DARWIN for automatically finding potential root causes of such bugs. Given two programs-A reference program and a modified program-And an input that fails on the modified program, our approach uses symbolic execution to automatically synthesize a new input that (a) is very similar to the failing input and (b) does not fail. We find the potential cause(s) of failure by comparing control-flow behavior of the passing and failing inputs and identifying code fragments where the control flows diverge. A notable feature of our approach is that it handles hard-To-explain bugs, like code missing errors, by pointing to code in the reference program. We have implemented this approach and conducted experiments using several real-world applications, such as the Apache Web server, libPNG (a library for manipulating PNG images), and TCPflow (a program for displaying data sent through TCP connections). In each of these applications, DARWIN was able to localize bugs with high accuracy. Even though these applications contain several thousands of lines of code, DARWIN could usually narrow down the potential root cause(s) to less than ten lines. In addition, we find that the inputs synthesized by DARWIN provide additional value by revealing other undiscovered errors. © 2012 ACM.
Author keywords: 
Index keywords: Errors; Transmission control protocol; Apache web server; Control flows; Control-flow; Identifying code; Lines of code; Real-world application; Root cause; Symbolic execution; TCP connections; Program debugging
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2012
EID: 2-s2.0-84863954406
DOI: 10.1145/2211616.2211622
Retrieval channels: authoritative_outlet_search
Local full-text files: 

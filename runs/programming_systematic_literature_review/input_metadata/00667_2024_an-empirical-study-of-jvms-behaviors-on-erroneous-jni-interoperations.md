---
otero_id: "2-s2.0-85187327037"
title: "An Empirical Study of JVMs' Behaviors on Erroneous JNI Interoperations"
authors: "Hwang S.; Lee S.; Ryu S."
year: "2024"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2024.3373239"
---
# Scopus title-abstract-keyword metadata
Title: An Empirical Study of JVMs' Behaviors on Erroneous JNI Interoperations
Abstract: Java Native Interface (JNI) allows Java applications to access native libraries, but it is challenging to develop correct JNI programs. By leveraging native code, the JNI enables Java developers to implement efficient applications and reuse code written in other programming languages such as C and C++. The core Java libraries use the JNI to provide system features like graphical user interfaces, and mainstream Java Virtual Machines (JVMs) support the JNI. However, implementing correct JNI programs is not trivial due to the complex interoperation semantics between different programming languages. While JVMs do not validate JNI interoperations by default because of the performance overhead, they provide two methods. First, JVMs report the interoperation failures defined in the JNI specification at runtime. Second, they support a debug option, which validates JNI interoperations, degrading the runtime performance. To the best of our knowledge, literature has not thoroughly studied the quality of JVMs' methods, even though erroneous JNI interoperations may result in incorrect behaviors. In this paper, we empirically study the behaviors of JVMs on erroneous JNI interoperations. For a systematic study, we propose JUSTGen, a semi-automatic tool that generates JNI test programs incurring erroneous interoperations from the JNI specification. JUSTGen receives the JNI specification written in our domain-specific language (DSL) and automatically discovers cases that may lead to runtime errors on interoperations using an SMT solver. It then generates test programs that trigger the behaviors on the erroneous cases. Using the generated tests, we empirically evaluate JVM's failure handling mechanisms and the debug option capabilities on erroneous JNI interoperations. Our experiment results show that there exist erroneous cases in which JVMs do not handle failures or handle them differently from the specification. We also found that the JNI debug option does not validate thousands of erroneous cases, which can cause critical runtime errors such as memory corruption and violation of the Java type system. We reported 18 erroneous cases of which JVMs do not handle failures correctly to their respective vendors. Among them, 16 cases have been resolved. © 1976-2012 IEEE.
Author keywords: debugging; empirical study; Java native interface; Java virtual machine; testing
Index keywords: Application programs; Behavioral research; C++ (programming language); Codes (symbols); Digital libraries; Graphical user interfaces; Java programming language; Libraries; Network security; Problem oriented languages; Program debugging; Specifications; Virtual machine; Behavioral science; Code; Debugging; Domains specific languages; Empirical studies; Java; Java Native Interfaces; Java virtual machines; Runtimes; Virtual machining; Semantics
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2024
EID: 2-s2.0-85187327037
DOI: 10.1109/tse.2024.3373239
Retrieval channels: authoritative_outlet_search
Local full-text files: 

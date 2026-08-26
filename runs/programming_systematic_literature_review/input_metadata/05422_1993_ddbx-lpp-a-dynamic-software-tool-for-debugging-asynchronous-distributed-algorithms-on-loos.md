---
otero_id: "2-s2.0-0027628056"
title: "Ddbx-LPP: A dynamic software tool for debugging asynchronous distributed algorithms on loosely coupled parallel processors"
authors: "Fernandez M.G.; Ghosh S."
year: "1993"
journal: "The Journal of Systems and Software"
doi: "10.1016/0164-1212(93)90120-m"
---
# Scopus title-abstract-keyword metadata
Title: Ddbx-LPP: A dynamic software tool for debugging asynchronous distributed algorithms on loosely coupled parallel processors
Abstract: It is generally accepted in the parallel processing community that powerful yet flexible debuggers are indispensable for the efficient programming of complex distributed synchronous and asynchronous algorithms on loosely coupled parallel processors. Traditional debugging systems, including POKER, permit a user to start, stop, and single-step a parallel program executing on a parallel processor while observing the successive changes of the traced variables and labels. These debuggers are limited in that the user must specify the list of variables and labels to be traced through the declaration section of each routine. As a result, the user may not alter the contents of this set once program execution has been initiated. More recently, debuggers such as ndb and dbxtool claim dynamic debugging support but are limited by clumsy user interfaces. While ndb works within a single window and requires the user to type commands, dbxtool is a simple collection of uniprocessor debuggers with no explicit coordination. PROVIDE claims to use graphical tools for debugging but is limited to a simplified programming language. Furthermore, both ndb and dbxtool are proprietary; few details, if any, on their software engineering design are available in the literature. This article details the software engineering issues in the design and implementation of an actual distributed dynamic runtime software debugger, Ddbx-LPP, that permits the user to view any global variable, structure, and parameter during program execution at any node of a parallel processor system. The system is exclusively mouse driven for relatively easy debugging. The user may insert breakpoints corresponding to any source code line, either before initiating execution or when program execution is temporarily suspended at a breakpoint. Furthermore, when the program, in the course of execution, experiences a nonrecoverable error, its execution is temporarily suspended and control is transferred to the user in a manner identical to the case of a deliberately inserted breakpoint. Although further execution is prohibited, Ddbx-LPP permits the user to view variables and structures to determine the cause of the error. Ddbx-LPP's unique ability may be credited to its significant analysis of the object code and symbol table, generated as a result of compilation under the "-g" option, both before and during the actual execution of the program. In contrast to POKER, which requires a sequential programming environment, Ddbx-LPP may function with a user program written in C for any loosely coupled parallel processor. Ddbx-LPP is superior to user-inserted "printf" statements to print out the values of variables and structures during execution because 1. 1) to print all variables and structures would require an overwhelming number of printf statements, and 2. 2) to insert new printf statements would mean program recompilation. Ddbx-LPP has been implemented on the ARMSTRONG system at Brown University and is equally applicable to any loosely coupled parallel processor system. © 1993.
Author keywords: 
Index keywords: Algorithms; Codes (symbols); Computer aided software engineering; Data structures; Distributed computer systems; Program debugging; Asynchronous distributed algorithms; Brown University; Distributed dynamic runtime software debugger Ddbx-LPP; Parallel processing systems
Document type: Article
Conference: 
Source title: The Journal of Systems and Software
Year: 1993
EID: 2-s2.0-0027628056
DOI: 10.1016/0164-1212(93)90120-m
Retrieval channels: authoritative_outlet_search
Local full-text files: 

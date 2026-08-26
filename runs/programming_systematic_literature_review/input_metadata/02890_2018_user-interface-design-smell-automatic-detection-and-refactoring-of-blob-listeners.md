---
otero_id: "2-s2.0-85047814624"
title: "User interface design smell: Automatic detection and refactoring of Blob listeners"
authors: "Blouin A.; Lelli V.; Baudry B.; Coulon F."
year: "2018"
journal: "Information and Software Technology"
doi: "10.1016/j.infsof.2018.05.005"
---
# Scopus title-abstract-keyword metadata
Title: User interface design smell: Automatic detection and refactoring of Blob listeners
Abstract: Context. User Interfaces (UIs) intensively rely on event-driven programming: interactive objects send UI events, which capture users’ interactions, to dedicated objects called controllers. Controllers use several UI listeners that handle these events to produce UI commands. Objective. First, we reveal the presence of design smells in the code that describes and controls UIs. Second, we demonstrate that specific code analyses are necessary to analyze and refactor UI code, because of its coupling with the rest of the code. Method. We conducted an empirical study on four large Java software systems. We studied to what extent the number of UI commands that a UI listener can produce has an impact on the change- and fault-proneness of the UI listener code. We developed a static code analysis for detecting UI commands in the code. Results. We identified a new type of design smell, called Blob listener, that characterizes UI listeners that can produce more than two UI commands. We proposed a systematic static code analysis procedure that searches for Blob listener that we implement in InspectorGuidget. We conducted experiments on the four software systems for which we manually identified 53 instances of Blob listener. InspectorGuidget successfully detected 52 Blob listeners out of 53. The results exhibit a precision of 81.25% and a recall of 98.11%. We then developed a semi-automatically and behavior-preserving refactoring process to remove Blob listeners. 49.06% of the 53 Blob listeners were automatically refactored. Patches have been accepted and merged. Discussions with developers of the four software systems assess the relevance of the Blob listener. Conclusion. This work shows that UI code also suffers from design smells that have to be identified and characterized. We argue that studies have to be conducted to find other UI design smells and tools that analyze UI code must be developed. © 2018 Elsevier B.V.
Author keywords: Code refactoring; Design smell; Empirical software engineering; Event handling; Software maintenance; User interface
Index keywords: Codes (symbols); Computer software; Computer software maintenance; Odors; Automatic Detection; Code re-factoring; Empirical Software Engineering; Event handling; Event-driven programming; Interactive objects; Static code analysis; User interface designs; User interfaces
Document type: Article
Conference: 
Source title: Information and Software Technology
Year: 2018
EID: 2-s2.0-85047814624
DOI: 10.1016/j.infsof.2018.05.005
Retrieval channels: authoritative_outlet_search
Local full-text files: 

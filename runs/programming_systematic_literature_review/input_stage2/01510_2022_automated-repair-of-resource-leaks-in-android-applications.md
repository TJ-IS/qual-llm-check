---
otero_id: "2-s2.0-85134325836"
title: "Automated repair of resource leaks in Android applications"
authors: "Bhatt B.N.; Furia C.A."
year: "2022"
journal: "Journal of Systems and Software"
doi: "10.1016/j.jss.2022.111417"
---
# Scopus title-abstract-keyword metadata
Title: Automated repair of resource leaks in Android applications
Abstract: Resource leaks – a program does not release resources it previously acquired – are a common kind of bug in Android applications. Even with the help of existing techniques to automatically detect leaks, writing a leak-free program remains tricky. One of the reasons is Android's event-driven programming model, which complicates the understanding of an application's overall control flow. In this paper, we present [Formula presented]: a technique to automatically detect and fix resource leaks in Android applications. [Formula presented] builds a succinct abstraction of an app's control flow, and uses it to find execution traces that may leak a resource. The information built during detection also enables automatically building a fix – consisting of release operations performed at appropriate locations – that removes the leak and does not otherwise affect the application's usage of the resource. An empirical evaluation on resource leaks from the [Formula presented] curated collection demonstrates that [Formula presented] ’s approach is scalable, precise, and produces correct fixes for a variety of resource leak bugs: [Formula presented] automatically found and repaired 50 leaks that affect 9 widely used resources of the Android system, including all those collected by [Formula presented] for those resources; on average, it took just 2 min to detect and repair a leak. [Formula presented] also compares favorably to Relda2/RelFix – the only other fully automated approach to repair Android resource leaks – since it can often detect more leaks with higher precision and producing smaller fixes. These results indicate that [Formula presented] can provide valuable support to enhance the quality of Android applications in practice. © 2022 The Author(s)
Author keywords: Android applications; Automated program repair; Program analysis; Static analysis
Index keywords: Android (operating system); Application programs; Automation; Program debugging; Repair; Android applications; Automated program repair; Control-flow; Empirical evaluations; Event-driven programming model; Execution trace; Leak-free; Overall controls; Program analysis; Resource leaks; Static analysis
Document type: Article
Conference: 
Source title: Journal of Systems and Software
Year: 2022
EID: 2-s2.0-85134325836
DOI: 10.1016/j.jss.2022.111417
Retrieval channels: authoritative_outlet_search
Local full-text files: 

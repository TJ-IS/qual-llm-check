---
otero_id: "2-s2.0-85124231358"
title: "Learning How to Listen: Automatically Finding Bug Patterns in Event-Driven JavaScript APIs"
authors: "Arteca E.; Schafer M.; Tip F."
year: "2023"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2022.3147975"
---
# Scopus title-abstract-keyword metadata
Title: Learning How to Listen: Automatically Finding Bug Patterns in Event-Driven JavaScript APIs
Abstract: Event-driven programming is widely practiced in the JavaScript community, both on the client side to handle UI events and AJAX requests, and on the server side to accommodate long-running operations such as file or network I/O. Many popular event-based APIs allow event names to be specified as free-form strings without any validation, potentially leading to lost events for which no listener has been registered and dead listeners for events that are never emitted. In previous work, Madsen et al. presented a precise static analysis for detecting such problems, but their analysis does not scale because it may require a number of contexts that is exponential in the size of the program. Concentrating on the problem of detecting dead listeners, we present an approach to learn how to use event-based APIs by first mining a large corpus of JavaScript code using a simple static analysis to identify code snippets that register an event listener, and then applying statistical modeling to identify anomalous patterns, which often indicate incorrect API usage. In a large-scale evaluation on 127,531 open-source JavaScript code bases, our technique was able to detect 75 anomalous listener-registration patterns, while maintaining a precision of 90.9% and recall of 7.5% over a validation set, demonstrating that a learning-based approach to detecting event-handling bug patterns is feasible. In an additional experiment, we investigated instances of these patterns in 25 open-source projects, and reported 30 issues to the project maintainers, of which 7 have been confirmed as bugs.  © 2022 IEEE.
Author keywords: API modeling; bug finding; event-driven programming; JavaScript; Static analysis
Index keywords: Application programming interfaces (API); Codes (symbols); High level languages; Open systems; Program debugging; Static analysis; API modeling; Bug finding; Code; Computer bugs; Event-based; Event-driven programming; Javascript; Open-source softwares; Programming; Register; Open source software
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2023
EID: 2-s2.0-85124231358
DOI: 10.1109/tse.2022.3147975
Retrieval channels: authoritative_outlet_search
Local full-text files: 

---
otero_id: "2-s2.0-85207525097"
title: "How and why developers implement OS-specific tests"
authors: "Job R.; Hora A."
year: "2025"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-024-10571-4"
---
# Scopus title-abstract-keyword metadata
Title: How and why developers implement OS-specific tests
Abstract: Context : Real-world software systems are often tested in multiple operating systems (OSs). Consequently, developers may need to handle specific OS requirements in tests. For example, different OSs have distinct file path name conventions (e.g., between Windows and Unix), thus, the tests should be adapted to run differently depending on whether the OS is Windows or Unix. In this context, an OS-specific test is a test that identifies the OS it will be executed. OS-specific tests may execute different lines of code of the application depending on the OS they are running. Objective : In this paper, we provide the first empirical study to assess OS-specific tests, exploring how and why developers implement this kind of test. This knowledge can help us understand OS-specific tests and the challenges faced by developers when testing for multiple operating systems. Method : We mine 100 popular Python systems and assess their OS-specific tests both quantitatively and qualitatively. We propose five research questions to assess the frequency, location, target, operations, and reasons. Results : (1) We find that OS-specific tests are common: 56% of the analyzed Python projects have OS-specific tests and Windows is the most targeted OS. (2) We detect that OS verification happens more frequently in test decorators (65%) than in test code (35%). (3) OS-specific tests target a diversity of code, including file/directory, network, and permission/privilege. (4) Developers may perform multiple operations in OS-specific tests, including calling OS-specific APIs, mocking OS-specific objects, and suspending execution. (5) We find that OS-specific tests are implemented mostly to overcome unavailable external resources, unsupported standard libraries, and flaky tests. Conclusions : Finally, based on our findings, we discuss practical implications for practitioners and researchers, including the relation of OS-specific tests with test smells, CI/CD, technical debt, and flaky tests. We also discuss the efforts to test on Windows properly and propose a novel refactoring to improve some instances of OS-specific tests. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2024.
Author keywords: Mining software repositories; Python; Software testing; Technical debt; Test smells
Index keywords: Application programming interfaces (API); Application programs; Linux; Problem oriented languages; Program debugging; Python; Windows operating system; Mining software; Mining software repository; Multiple operating systems; Real-world; Software repositories; Software testings; Software-systems; System specific; Technical debts; Test smell; Software testing
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2025
EID: 2-s2.0-85207525097
DOI: 10.1007/s10664-024-10571-4
Retrieval channels: authoritative_outlet_search
Local full-text files: 

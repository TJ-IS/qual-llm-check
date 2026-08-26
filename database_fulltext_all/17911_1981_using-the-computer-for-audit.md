---
otero_id: 17911
otero_key: "DAE532NC"
title: "Using the computer for audit"
authors: "Ben Goossens; Nico Schouten"
year: "1981"
journal: "Information & Management"
doi: "10.1016/0378-7206(81)90019-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using the Computer for Audit

Ben Goossens and Nico Schouten

Moret & Limperg Registeraccountants, Van Boshuizenstraat 12, 1083 BA Amsterdam, The Netherlands

Since the computer is being used for auditing purposes, the best known method in this area has been to obtain access to files with the help of special audit packages. However in the meantime, other methods have also become available. An overall picture is given of the opportunities in this field, including a review of the tools and methods which are presently available. The position of these in the audit program is discussed.

Keywords: Auditing, audit packages, access to files, independence of auditors, computer assisted audit techniques.

![](/api/attachments/DAE532NC/fulltext/images/598f883f474fd1d33c94efe7b4dcb9965c86cda297cf4b165a553e52e0a60376.jpg)

Ben Goossens and Nico Schouten are qualified accountants and members of the Netherlands Institute of Register Accountants. Ben Goossens is a partner and Nico Schouten is a manager of Moret & Limperg, one of the leading Dutch public accounting firms. They work at the EDP-audit department of the Amsterdam office. Ben Goossens is in charge of this department. Their career path is a typical one for a Dutch accountant. They combined their job with the study for the accountants examination.

![](/api/attachments/DAE532NC/fulltext/images/95972263d910ae6ed69153035fdb8297b37967eac2b99f0c8262b14c33576f4e.jpg)

Ben Goossens started to work for Moret & Limperg when he was 24 years old. He obtained his qualification cum laude in 1977 with a study on the subject he is dealing with in this article. He has seventeen years of experience in auditing; he joined the EDP audit department in 1974.

Nico Schouten started to work for Moret & Limperg when he was 18 years old. He obtained his qualification in 1978 with a study on the subject "Information, Employees and the Auditor". He has twelve years of experience in auditing and joined the EDP audit department in 1977.

## 1. Introduction

It is ten to fifteen years since the auditor began to make use of the computer for audit purposes. The best known method is that of obtaining access to files by means of generalised audit software. Other methods have, in the meantime, become available. Generalised audit software is only one of the available tools, although it may be the most important one. In our firm, we find that as the auditor becomes more involved in EDP systems development, generalised audit software is becoming less important. It was Keith O'Dorricott [6] who first came up with a discussion of computer assisted audit techniques. Since then, much has been written about all sorts of techniques, but little about how they fit into an audit. This is strange, because even if an auditor is technically aware of the techniques, their application has little purpose if it is not possible to use them, either in combination or separately, in a responsible way.

Our objective here is to contribute to a meaningful utilisation of the tools and techniques by showing where they belong in the audit plan. We shall limit our scope to the audit of computer systems with respect to accuracy and reliability.

We shall not give a detailed description of the various methods and tools: most of them are not specifically designed for the auditor, and many of them are well known to non-auditors.

## 2. Available Methods

We use the word "method" rather than "technique" for the following reason. By "audit techniques", we understand the application of auditing procedures as elements of the audit plan in general: this does not necessary mean use of the computer. If the auditor decides to use the computer as a tool in carrying out the audit program, a method must be selected: a way to use the computer. When speaking of "tools", we mean the aids, while "methods" refer to the way the tools can be applied. Thus the process is: first, select the method, and, second, select the tool.

There are three important distinctions between the methods: the first concerns the type of data being processed - it may be live or test data. The second concerns the type of program. It may form part of a particular application or be a special program. Last, there is the relationship to production processing. If the program forms part of an application, it may be performed concurrently with production processing within the live system, or else it will be in a separate run. These distinctions are essential for a good understanding of the methods. They also affect their scope. Most of the possible uses and limitations which will be mentioned later are the direct consequence of these distinctions.

For practical reasons, we make a division between methods processing live data and methods processing test data. The former is shown in Table 1, the latter in Table 2.

## 2.1. Methods Processing Live Data

## 2.1.1. Data Testing and Verification

This entails: (1) Testing the inter-relationship between data which are stored on computer files, and (2) selecting data from files for verification with elements outside the computer files. The Ref. [1] report calls this Techniques for Data Verification. Ref. [2] refers to it as Verify Results. A typical example of data testing and verification is sampling and selecting. If the auditor wishes to obtain a statistical opinion of a population, the process can be as follows.

First. define special data: for example (in a payroll file) all salaries above Dfl 10,000. The records containing these salaries are selected. From the remaining records a statistical sample is then taken. Next, the selected records are verified through elements outside the computer. The data testing and verification method processes the live data in a separate run.

## 2.1.2. Parallel operation

This is also called Parallel Running. Briefly, existing and newly developed programs are run, both of them processing the same production data and files. The results are compared and differences analyzed. The main advantage of parallel operation is security. By using parallel operation, the auditor obtains an opinion on the newly developed or updated system. The main problems are: How long do we use two systems? and: What is the consequence of the differences that will exist between them?

Table 1  
Methods of processing with live data

<table><tr><td>Type of program</td><td>Relation to Production Process</td><td>Methods</td><td>Tools</td></tr><tr><td rowspan="2">Special programs</td><td rowspan="2">Separate processing</td><td>Data testing and verification</td><td rowspan="2">Generalised audit-software, Tailored programs</td></tr><tr><td>Parallel simulation</td></tr><tr><td rowspan="4">Application programs</td><td rowspan="2">Concurrent processing</td><td>Scarf</td><td>Gas tailored programs</td></tr><tr><td>Tagging and tracing</td><td>-</td></tr><tr><td rowspan="2">Separate processing</td><td>Parallel operation</td><td>-</td></tr><tr><td>Reprocessing</td><td>-</td></tr></table>

## 2.1.3. Parallel simulation

This is a method by which the auditor processes the original input transactions by means of special audit programs which simulate the more important parts of the operational programs. The results of the processing are compared with the results of the normal application processing. There should not, in principle, be differences: deviations must be analysed.

Table 2  
Methods of processing with test data

<table><tr><td>Relation to production process</td><td>Methods</td><td>Tools</td></tr><tr><td>Separate</td><td>Test decking</td><td rowspan="2">Missed branch indicators test data generators</td></tr><tr><td>Concurrent</td><td>Integrated test facilities</td></tr></table>

The auditor is often not fully aware of using this method, because most audit software applications include something of parallel simulation as part of an application in which the auditor is selecting records.

As an example, some years ago we made an audit software program that accessed the payroll file of a trade company. One of the functions of the program was selecting employees who should be insured for pensions. The results of the audit software program were compared with a confirmation from the insurance company. This confirmation was based on a program that did the same as the audit software application. Parallel simulation processes the original input in a separate run by a special program.

## 2.1.4. Reprocessing

This is the situation in which the auditor has a special copy of the application programs, and the input is reprocessed using his copy. Why should the same job be done twice? As an example, a company has a very important program that processes the annual consolidation of all its affiliated companies. The auditor wishes to confirm that this consolidation was achieved using the program that was previously reviewed and not by another. So the auditor reprocesses the input data by means of the copy. Reprocessing actually is the separate processing of the application program.

## 2.1.5. SCARF

SCARF is an abbreviation for System Control Audit Review File – a method of extracting data into a file by statements prespecified by the auditor and embedded in the application programs. SARF (Sample Audit Riew File) is the extraction of the data based on the sampling due to the prespecified statements. In the System Auditability and Control Report [1] both methods (SCARF and SARF) are referred to as Embedded Audit Data Collection.

Example: in the audit of one of our clients, we use a software program to detect the difference between the actual and standard cost of sales. Nex year, we intend to build this control into the application program. Then, during the invoicing program, if a price is used that differs from the standard price, the transaction will be flagged and written to a special file for examination by the internal auditors. SCARF accesses live data, the method is embedded in the application programs and processing takes place concurrently with the normal processing.

## 2.1.6. Tagging and Tracing

This is also termed a Snapshot or Audit Indicator. Selected inputs are tagged, and the embedded routines provide visible evidence of these transactions; i.e. they provide the complete transaction trail. This has to be prespecified and coded into routines which are then embedded in the application programs. As an example, at the previously discussed trade company, we select some invoices from the purchases. These sampled invoices are input to a special routine of the client. This provides the necessary information: the order information, other invoices, payments, stock, etc. This method is embedded in the application programs so it is processing concurrently with the application program and is thus somewhat similar to scarf.

## 2.2. Tools for Methods Processing Live Data

## 2.2.1. Audit Software Tailored Programs

In “Computer Control & Audit” by Mair, Wood and Davis [2], generalized audit software is described as “specialized programming languages designed to meet the needs of the auditor”. This is of course true, but many audit software packages are used by EDP personnel as well as auditors. Tailored programs are special purpose programs that have been written to solve a problem. When an audit software package is available, the application of tailored programs will be limited to particular problems. The main advantage of generalised audit software is that it is audit oriented: it enables the auditor to solve a problem with far less coding than a tailored program. This, however, indicates its limitations. The more unusual the problem, the less attractive the use of generalised software.

At the end of 1974, Litecky and Weber published an article in the "Journal of Accountancy" entitled "The Demise of Generalised Audit Software" [3]. They suggested a demise in the usefulness of audit software because of the growing popularity of data base management systems. Their article was too negative. In our firm, we use packages which handle some well known database management systems. When looking at tailored programs in comparison with audit software, three significant points arise: first, the flexibility: in principle there are no limitations in solving problems, but there are some complications which make it less attractive for an auditor to use tailor-made programs on a large scale. These complications are the time and cost of program development, as well as the high level of EDP skill required. Finally, efficient operation is sometimes mentioned as an advantage of tailored programs. This is only partially true. It is true, for example, if tailored programs written in COBOL are compared with software packages written in COBOL and provided with a so-called precompiler. It need not be true if tailored programs written in a high level programming language are compared with software packages which are written in machine languages. Audit software and tailored programs can be used with:

-- data testing and verification

\- parallel simulation

## - SCARF

The use of these tools for SCARF implies that data is collected on a file which has to be analysed by the auditor; audit software and tailored programs may be a powerful tool for this analysis, because data selected by the test routines may be voluminous.

## 2.3. Methods Processing Test Data

## 2.3.1. I.T.F.

I.T.F. is the method by which application programs are tested during production processing. Thus test data are processed at the same time as live data. In order to avoid test transactions becoming mixed with operational inputs, the test entity is established as a "dummy". Then, after the event, the test transactions must be reversed by either manual corrections or "filtering" the transactions using modules in the application programs. As an example, the internal auditors of one of our clients can bring transactions into the system by using a special office number. The results of the processing are delivered to the office of the internal auditor. Then the test transactions are filtered out of the production files by a special module (based on this office number). ITF runs concurrently with main processing.

## 2.3.2. Test decking

This involves all methods in which test data are processed by application programs in a separate run; the results of this processing are compared with predetermined test results. There is a tendency to make a distinction between test data method and base case system evaluation, but this distinction is related to the scope of the test set, not to the way the methods have to be performed. These methods are very commonly used in the testing of new systems; users prepare test sets and calculate the expected results. The main problem in making test sets is in the impossibility of being complete.

## 2.4. Tools for Methods Processing Test Data

## 2.4.1. Missed Branch Indicators

There are two tools available that can aid in testing applications; the first is termed Missed Branch Indicators. These involve software that provides a count of the number of times each branch of a program is performed. In Ref. [1], Missed Branch Indicators are referred to as Mapping. This software was originally designed as an aid to the programmer in debugging a program and measuring its performance. The auditor can use this to evaluate the completeness of the test set. By looking at the count of the number of times each branch is executed, it is easy to see which branches are not used at all. A well-known package is COMBI; it can be an aid in conjunction with I.T.F. and Test Decking.

## 2.4.2. Test Data Generator

This is a tool that produces test data for use in EDP operations. It is a substantial aid when composing extensive tests, which is very time consuming and often incomplete. When using this tool for testing a complex application, there will normally be a very big test set. As with Missed Branch Indicators, Test data generators aid both methods of processing test data.

## 2.5. Other Tools

## 2.5.1. Code Comparison and Flow Charting Software

Two other tools should be mentioned. They do not process test data or live data, but they access program code. The first one is Code Comparison Software. This produces complete information of changes in program code. It can be an aid when the auditor wishes to review a new version of the program. Using this tool, it is possible to find out what changes have been made, and, thus make a more efficient review. Of course, it will also obtain all the less important changes that are made, and consequently its use can be time consuming. The other tool that processes program code is Flow Charting Software. This can produce a flow chart of a program in source code. A considerable advantage is that it produces documentation which is up-to-date. However, the interpretation of flow charts may be difficult.

## 3. How The Methods Fit Into An Audit

## 3.1. Audit Plan

First, the auditor must perform a review and preliminary evaluation of the "organisation". Review and preliminary evaluation by the auditor are necessary to determine that (a) an internal control system exists, and (b) internal controls are adequate.

The next step is the investigation of the functioning of the system. This corresponds to so-called "Compliance Tests". The goal of these can be defined as ensuring the correct functioning of the internal control system. Although this is an important part of the audit, the auditors actions cannot be confined to these compliance tests, since the tests do not ensure that the system in all its aspects has functioned as prescribed. The compliance tests serve as a basis to determine the nature, extent, and timing of the next step in the audit program, the substantive tests, the equivalent of the "Examination of the Financial Data". This is the framework for "the classification of the methods by purpose". The purpose of each method decides its place in the audit program, but some methods overlap the boundaries in the audit plan.

## 3.2. Review and Evaluation

## 3.2.1. Flowcharting software

First, we look at methods for Review and Evaluation. If the auditor has to acquire detailed knowledge and understanding of the structure of a system, this can be achieved by studying relevant flowcharts.

The usefulness of flowcharting software must be questioned. Flowcharts cannot be any better than the underlying source code. This limits the usefulness of flowcharting software as a documentation aid.

The auditor should advice EDP departments to use a structured programming concept. Programs designed in that way produce source listings which make flowcharting software essentially superfluous. Nevertheless, in some cases, flowcharting software can be last resort. As to the scope, there is no certainty that the information is indeed incorporated in the production programs! Other measures must be applied to cope with this problem.

## 3.2.2. Code Comparison Software

The auditor may use comparison software to verify whether or not all necessary changes have been made and are correct. The advantage of completeness also implies the disadvantage of total, if insignificant, detail. Like Flow Charting Software, Code Comparison Software makes great demands on the EDP skills of the auditor, at least in making their application effective. The main objective of using this software is to ensure that all the changes in the reviewed programs can be identified. This could be useful in the case of sensitive programs. But his may only be considered under the following conditions:

(1) The original program and the identified changes are evaluated together in detail.

(2) The auditor must be sure that the reviewed programs are the same as the operational programs.

These conditions call for the proposition that code comparison software (on its own) is nothing but an aid to review and evaluation. As for the review and evaluation of changes, one more question is relevant: What is the impact of a change in the reviewed program on other parts of the system? Code comparison software does not give an answer to this question.

## 3.2.3. Parallel Operation

This method has the advantage of processing live data. Thus results of the operations can be directly compared with the results of the live system. However, it is normally only used incidentally, at conversion time. The objective is to establish that the new or revised system is functioning properly before replacing the existing system. This implies that the scope of parallel operation is limited to review and evaluation. Apart from this, the auditor must realise that review and evaluation of the system design have to be performed during development. Parallel operation can, at best, be a useful method of identifying unexpected differences between the existing and newly developed system. At an earlier stage the audit to should confer (with EDP personnel and users) about measures that must be taken to ensure that the conversion will be successful; parallel operation might be one of these measures.

## 3.2.4. Tagging and Tracing

The objective of this method is to analyse computer programs. It does not need any specific tool. The transaction trail has to be predetermined and recorded into routines that are embedded in the application programs. A high level of EDP skills is required to implement the embedded routines during the development of an application. A practical problem is in dealing with the merging and separation of input transactions in the production programs.

Tagging and Tracing may be useful in situations where producing the complete transaction trail of all inputs is not feasible. Programming staff use this method in order to identify imperfections in application programs. The auditor, of course, may do the same. A considerable advantage is that detailed information is obtained about the application programs during production processing. This too means that the auditor could use this method to perform compliance tests. The disadvantage of this method is that evaluation of the results is a time consuming affair, and therefore this method is not appropriate for voluminous tests. The auditor should use this method if it is already available in the EDP organisation, but think twice before spending a lot of time designing it!

## 3.2.5. Test Decking

Test Decking is a widely used method of ensuring that the demands of the users are included in the system: it is relatively simple, but two problems must not be neglected: First, composing test sets is very time consuming. Second, much attention should be paid to the completeness of the test sets, since it is possible that irregularities can arise in instructions that have been added. Aids in solving these problems may be test data generators and missed branch indicators

The combination of these aids can be especially useful. One problem, however, which they cannot solve is the interrelationship between the different steps in the programs. Whether or not a transaction has taken the right logical path must be established by testing the results.

The auditor must ascertain that the organisation has taken measures to ensure that the demands and wishes of the users are included in the system. Therefore good test and acceptance procedures are indispensable. If necessary, the auditor has to test the system by putting in test cases. But other measures have to be taken to ascertain that the programs which are executed during production processing correspond to the tested programs.

## 3.3. Compliance Tests

## 3.3.1. Integrated Test Facilities (ITF)

The first of the methods in this area is Integrated Test Facilities. The major advantage of ITF is that it enables the auditor to test the live system continually. The auditor can form an opinion on the functioning of the operational system. We have previously discussed the problem of filtering or reversing the test transactions. Filtering is the safer method, but it limits the scope of ITF, as the auditor does not obtain an insight into what is happening after the transactions have been filtered. Reversing the transactions manually may be possible. This requires that the results of processing are mainly utilised by the departments which supply the input data. In our experience, the main disadvantage of ITF is the aversion of DP personnel. The FDP department does not like the auditor to "poison" the production processing. Most of the publications about ITF do not pay enough attention to the problems of reversing test transactions. This will be an increasingly important problem in the future. It may be described as: Who is auditing the auditor?

The auditor must be careful to deal with test data and a specially assigned "dummy" entity. This limits the ability of the auditor to draw conclusions on the reliability of the results. A spler did combination of methods is the use of "tagging and tracing" in order to analyse unexpected results of test data processed by ITF.

## 3.3.2. Parallel Simulation

Parallel Simulation is powerful because live data are processed by programs which have been designed by the auditor. It is also practical, because it has little impact on the EDP organisation. One limitation should be mentioned. The job is done after the event, so no preventive value can be assigned. On the other hand, parallel simulation could make substantive tests superfluous: the results of the simulation are directly compared with the results of the operational processing programs. This aspect implies that the application of parallel simulation as a part of the audit program may be efficient. Nevertheless, we should consider that parallel simulation implies duplicate processing of input transactions and is therefore inefficient. The auditor who decides to apply parallel simulation needs a high level of EDP skills, particularly if special purpose programs have to be developed.

## 3.3.3. Reprocessing

Reprocessing is a particular way of simulating the process. The vital difference with parallel simulation is that the auditor did not design the utilised program. This makes a detailed review and evaluation of the utilised program necessary. But this is also the reason why reprocessing is not often applied: it is not practical, but it may be necessary for sensitive programs. In such a case, missed branch indicators and code comparison software may be the right tools for review and evaluation of the programs being reprocessed: missed branch indicators as an aid in testing the programs and code comparison software to review changes in the programs.

## 3.3.3. Substantive Tests

The final category to be discussed is the examination of financial data: the substantive tests. Two methods are important: Embedded Audit Data Collection (mostly referred to as SCARF), and Data Testing and Verification. In both methods, data are tested by comparing them with other data within, while data are selected to verify them with outside the computer. There are two main differences which are important with regard to the possible uses and limitations: The first relates to the time at which the program is performed, SCARF concurrently, Data Testing and Verification after the event. The second is in the security: SCARF is embedded in the live system, whereas Data Testing and Verification takes place by "independent" programs. SCARF has to be designed at the stage of development of the application programs: this is the main reason why it is applied less than Data Testing and Verification. But, once implemented, SCARF is powerful. In principle, there are no limitations to the availability of information since the audit routines may be built throughout the whole system. By contrast, in using Data Testing and Verification the available information is limited to the Data which are resident on the files after production processing has been finished. Both methods – SCARF and Data Testeng & Verification – are often used for a mixture of compliance testing and substantive testing. SCARF especially contributes to the testing of processing controls just as ITF and Tagging and Tracing do. Data Testing and Verification usually includes a degree of parallel simulation (e.g., when extracting a sample, it is often necessary to perform some calculations which are – more or less – the same as those done by the system).

Last, the issue of independence should be mentioned. Various suggestions (e.g. [3]) have been made that the solution to the problem of the possible demise of audit software should be achieved by incorporating audit functions into DBMS. One argument against using DBMS software as an audit tool relates to the issue of independence. Ref. [4] discusses the validity of this argument. One of the conclusions of the authors is: "Admittedly the opportunity to violate integrity is reduced when an audit software package is used. However, the argument that fewer vulnerable components necessarily produce higher independence is tenuous. It begins a philosophical debate on the existence of degrees of independence."

In terms of independence, as Kearns [5] says, there are at least two major issues: the need to maintain adequate audit control over the application to ensure the integrity of the results and the question of how much reliance auditors may place on software developed by others outside their direction. To solve this problem Kearns suggests there should be checklists of possible audit control techniques for each type of CAAT. There are examples in his paper for generalised audit software, and test decking. The way Kearns deals with the subject is very useful. It makes the auditor aware that when using the computer for audit, adequate measures must be taken to ensure proper control. This depends on:

\- the auditor's evaluation of internal control;

\- the inherent risk associated with the item under audit; and

\- the reliance to be placed on the application

## References

[1] System Auditability & Control Report, the American Institute of Internal Auditors (Institute of Internal Audition, Inc., 1977; ISBN: 0-89413-052-8; 0-89413-051-X).

[2] W.C. Mair, D.R. Wood and K.W. Davis, Computer Control & Audit, Institute of Internal Auditors (1978), ISBN 0-89413-063-3.

[3] Litecky and Weber, The Demise of Generalised Audit Software Packages, The Journal of Accountancy (November, 1979).

[4] Jenkins and Weber, Using DBMS Software as an Audit Tool; The Issue of Independence. The Journal of Accountancy (April 1976).

[5] John Kears, How CAAT's Affect Audit Independence, Paper presented at the Symposium "Computers and Auditing" (Toronto, 1978).

[6] Keith O'Dorricott, CA Magazine (August, 1975).

---
otero_id: 23394
otero_key: "CKTCCV99"
title: "A process model for software maintenance"
authors: "Robert Moreton"
year: "1990"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1990.19"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A process model for software maintenance

ROBERT MORETON

Director of Studies, Birmingham Polytechnic, UK

Abstract: This paper draws on work undertaken for the Butler Cox Productivity Enhancement Programme (PEP) to describe a process model which will provide a basis for overcoming the problems of cost and complexity associated with software maintenance. PEP is a continuous program that is open to organizations wishing to measure and improve systems development and productivity.

The paper argues that for maintenance work to be effective, it is vital to control the input to the process – the procedure by which change requests are notified and managed in the first place. The procedure of change management is followed by impact analysis, system release planning, change design, implementation, testing and system release/integration. These steps, which occur sequentially, are supported by a further activity that continues concurrently – progress monitoring.

The conclusion of the paper is that a coordinated program, effective across the whole maintenance process and designed to control changes to the system, will become more and more critical as the complexity of the system increases. Formal procedures are essential to ensure that software is not degraded and to provide an audit facility. At the same time there are several automated change and control packages now available that could help to reduce administrative overheads and increase control over system changes.

## Introduction

Software maintenance is an expensive and complicated business. Research undertaken by Moreton (1988) for the Butler Cox Productivity Enhancement Programme (PEP), indicates that maintenance is generally undermanaged. As a result system changes are not always properly controlled and there is insufficient recognition of the benefits to be derived from the newer methods and tools. Recent articles by Glass (1988, 1989) highlight the need to formalize the maintenance process, to manage the software as a product and to link quality with maintenance processes. The purpose of this paper is to describe a process model for software maintenance which will provide a basis for rectifying the perceived deficiencies and exploiting the potential benefits.

For maintenance work to be effective, it is vital to control the input to the process – the procedure by which change requests are notified and managed in the first place. This procedure of change management is the first of several steps in the maintenance process. Change management is followed by impact analysis, system release planning, change design, implementation, testing and system release/integration. These steps, which occur sequentially, are supported by a further activity that continues concurrently – progress monitoring. The whole process is illustrated in Figure 1 (adapted from Arthur, 1988).

In a survey of 24 commercial organizations belonging to the Butler Cox PEP, respondents claimed to have a clearly defined procedure in place that corresponds to the first step, change management. Certainly, every respondent in the survey records all user requests and operational problems, but respondents admitted to some failings as well. Periodic formal audits, for instance, are in place in fewer than half of the survey respondents' businesses (see Figure 2). In order to achieve improvements in the maintenance environment, the steps in the process need to be carefully coordinated, not simply monitored individually.

## Formalize the maintenance process

To appreciate the importance of formalizing the steps in the maintenance process, it helps to understand more precisely what they are.

## Change management

Change management is the critical first step in the maintenance process. A formal procedure for change management is essential for two reasons: it provides a common communication channel between maintenance staff, users, project managers and operations staff, and it provides a directory of changes to the system, for status reporting, project management, auditing and quality control. The basic tool of the change-management procedure is a formal changerequest document that forms the basis of a contract between the user and the maintainer.

Software configuration management  
![](/api/attachments/CKTCCV99/fulltext/images/2ef767fe22b377d5386650268b863bb96294d21a6d84325c699eccb9a6147a26.jpg)  
Figure 1. Define the steps in the maintenance process

![](/api/attachments/CKTCCV99/fulltext/images/b957a10f74f1c6bed0f7f837048b2caa2b25ac729362e26699fa0dfcb6dcfd86.jpg)  
Figure 2. Most organisations have control procedures in place

An important element of change management is version control (or software configuration control). It means tracking different versions of programs, releases of software and generations of hardware, and it plays a major role in ensuring the quality of delivered systems. Version control also ensures that software is not degraded by uncontrolled or unapproved changes, and provides an essential audit facility.

## Impact analysis

The purpose of impact analysis is to determine the scope of change requests as a basis for accurate resource planning and scheduling, and to confirm the cost/benefit justification. Impact analysis can be broken down into four stages. The first stage is determining the scope of the change request, by verifying the information contained within it, converting it into a systems requirement, and tracing the impact (via documented records) of the change on related systems and programs. In the second stage, resourcing estimates are developed, based on considerations such as size (in estimated lines of code) and software complexity. Code analysers that measure the quality of existing code can be helpful at this stage. The third stage is analysing the costs and benefits of the change request, in the same way as for a new application. In the fourth stage, the maintenance project manager advises the users of the implications of the change request, in business rather than in technical terms, for them to decide whether to authorize proceeding with the changes.

There are three benefits of impact analysis: improved accuracy of resourcing estimates and, hence, better scheduling; a reduction in the amount of corrective maintenance, because of fewer introduced errors; improved software quality.

## System release planning

In this step, the system release schedule is planned. Although well established amongst software suppliers, system release planning is not widely practised by the data processing departments of the organizations surveyed, reflecting a difference in the extent to which formal maintenance contracting is established.

A system release batches together a succession of change requests into a smaller number of discrete revisions. System releases can take place according to a timetable that is planned in advance. The timetable planning gives users the chance to set priorities for their change requests, and makes testing activities easier to schedule. The problem with system releases comes, of course, when corrective maintenance is required urgently.

Software is available to help monitor system releases. The software records the changes incorporated in, and the date of, each release, and provides information for project control, auditing and management.

## Change design and implementation

The common thread in the work in these two steps is that they are undertaken to satisfy an often short-term user requirement.

Corrective maintenance, in particular, will be undertaken in a limited time and will be concerned primarily with fault repair (with little regard for careful design and integration changes). Emergency repairs must subsequently be linked to the formal software-maintenance process and be treated as a new change request. This will ensure that the repairs are correctly implemented and that the design documentation is updated.

Adaptive maintenance will functionally enhance an existing system. The design and implementation process is similar but more restricted than the design and implementation of new application systems. The major difference is that the design implications of enhancements must be taken into account in the subsequent program and module implementation. Failure to design the change at each level can result in an increasingly complex, unreliable and unmaintainable system. This leads to higher maintenance costs and reduces the life of the system.

Perfective maintenance is concerned with improving the quality of existing systems. The effort is applied to software that is the most expensive to operate and maintain. The design tasks undertaken will range from complete redesign and rewrite to partial restructuring. The process combines the characteristics of the other two types of maintenance.

## Testing

The purpose of maintenance testing is to ensure that the software complies with both the change request and the original requirement specification. It forms a major part of a successful quality-assurance plan. In principle, maintenance testing is much like development testing except that, because the scope of maintenance testing is potentially narrower, fewer test cases have to be prepared, validated and filed in the test-case library.

The maintenance test cases should be created as a direct result of the first stage in the impact analysis. They should be sequenced according to the principle of incremental testing so that defects in the change-request specification and design can be identified early on. Walk-throughs and inspections should be implemented routinely as a formal element in the process.

The test-case library itself builds up over time. At first, it contains only the test cases prepared for and validated during original development. It grows as test cases for successive maintenance tests are added to it. A file of this sort is called a regression testing file. A few tools are available from suppliers (such as IBM and Digital) to help with regression testing. Although limited in what they can do (in terms of features such as automatic revalidation, for instance), they are able to provide administrative support.

## System release/integration

This step consists of releasing the revised programs into live operation. The implications for maintenance staff are significant because it is their responsibility to ensure that any revised versions are completely integrated with other parts of the system, which may never have been revised or which may have been revised at different times.

## Progress monitoring

Progress monitoring takes place concurrently with the other seven steps in the maintenance process. The sort of data that should be collected during progress monitoring includes the time taken per step, the effort involved and the scope of the change. Collecting and filing data of this sort so that performance can be monitored, both over time and between systems, is consistent with the disciplined formal approach to software development and maintenance implied by the terms software engineering. Improving software maintenance productivity is difficult if there is no record of where problems and successes have occurred in the past.

## Coordinate the steps in the maintenance process

There is no panacea for solving the problems of maintenance. It is essential, however, to consider not only how each individual step in the process works, but also how the various steps fit together.

The software house, Peterborough Software (UK) Ltd, provides an example of how companies can successfully coordinate the steps in the software maintenance process. The problems that it faces are unusually demanding. The company maintains a range of payroll software packages. The packages run on a variety of computers, under the control of different operating systems, both within the UK and overseas. Altogether, Peterborough Software has around 400 customers. The software coding differs from country to country, to take account of local statutory regulations, such as taxation. Thus, several releases of the same package are current at a time, and all have to be supported in the field. The regulations change frequently and without warning, and maintenance changes therefore have to be implemented swiftly and accurately. The difficulties faced by Peterborough Software are further compounded when customers create nonstandard versions of the software by failing to apply maintenance modifications that are issued to them, or applying them in the wrong sequence.

How does Peterborough Software arrange its maintenance procedures against this background of complexity? The answer lies in disciplined adherence to procedural steps similar to the ones we have described here, and in the use of a computer-based program monitoring system known as the Problem Monitoring System (PMS).

The maintenance procedure is carried out by two divisions within Peterborough Software. One is the Customer Support Division, which effectively looks after management impact analysis and system release planning. The other is the Development Division, which is responsible for coding, testing and quality assurance.

Change requests received by the Customer Support Division come from three sources: customers, whose requests take the form of enhancements (called facility requests), queries and error reports; impending legislative changes; the market. To survive, Peterborough Software has to compete by offering products that are constantly being improved. Maintenance arising from customers is both adaptive and corrective in nature; from the other two sources, it is mostly adaptive and perfective.

Customers are the most important source of change requests – the Customer Support Division receives up to 400 telephone enquiries a day, for instance enquiries are routed to application-support groups organized by software product and by the kind of equipment it runs on. Within the application-support groups, consultants familiar with the way the software can be used, and with the way it works, form the first line of response. They are able to resolve most of the enquiries on the spot, but 20 per cent have to be passed to the Development Division for resolution. It is here that the PMS comes into its own. It logs problem reports at every stage of response and resolution, using customer references and event codes. When a coding change is made, for instance, the programmer records the details on the PMS. These are immediately available to others, so duplication is avoided. The PMS helps to coordinate adaptive and corrective maintenance work. It monitors maintenance progress and produces management statistics.

The Development Division is organized into groups that specialize in analysis, coding and quality assurance. Tested software is batched for release. Different forms of release reflect the level of support that Peterborough Software provides. For instance, versions for release which are necessitated by government legislation get full support. Any earlier versions still left in the field beyond a certain date no longer enjoy full support.

The Peterborough Software example is a model for the maintenance of any large application system, but particularly for multisite, multiversion implementation with large numbers of users. The principal lessons are as follows:

\- Recognition of the cost and of the importance of the post-release phases of the system life cycle, and the consequent planning (for example, replacement, migration and technical design) for the maintenance effort

\- The rigour applied to pre-release testing and post-release version identification and control

\- The formal contractual basis that clearly specifies the responsibilities of supplier and customer

\- Recognition of the relative importance of problems that occur in practice at the operational level (including those deriving from imperfect documentation or training), and at the code maintenance level and of the need to provide adequate support staff at both levels.

A coordinated programme, effective across the whole maintenance process, and designed to control changes to the system, will become more and more critical as the complexity of the systems increases. Formal procedures are essential to ensure that software is not degraded and to provide an audit facility. The experience of Peterborough Software may serve as a model. At the same time, there are several automated change-and-configuration-control packages currently being introduced to the market that could help to reduce administrative overheads and increase control over system changes.

## References

Arthur, L.J. (1988) Software Evolution, Wiley, New York

Glass, R.L. (1988) Champions of the living software Systems Development, August.

Glass, R.L. (1989) Linking quality and maintenance Systems Development, July.

Moreton, R. (1988) Managing software maintenance
Butler Cox Productivity Enhancement Programme,
Paper 8.

## Biographical notes

Robert Moreton is a principal lecturer at Birmingham Polytechnic. As Director of Studies within the Department of Computing, he is responsible for the academic quality of a range of professional and degree courses in computing and information technology. He is also an associate consultant with Butler-Cox, where he specializes in systems development methods and project management. In the past eight years, he has worked on both consultancy and research projects for the company. He has contributed to Butler-Cox reports on cost-effective systems development and maintenance, managing software maintenance and trends in information technology. He was also responsible for a study of the market for system-building tools in Europe. A common theme of his work has been tracking and evaluating developments in information technology and forecasting the potential impact of these developments.

He has a masters degree in computer science from Brunel University and is a member of the British Computer Society.

Address for correspondence: Department of Computing, Feeney Building, Birmingham Polytechnic, Perry Barr, Birmingham B42 2SU.

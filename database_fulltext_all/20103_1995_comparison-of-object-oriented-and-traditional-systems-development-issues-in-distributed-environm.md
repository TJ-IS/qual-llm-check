---
otero_id: 20103
otero_key: "A4SF43WB"
title: "Comparison of object-oriented and traditional systems development issues in distributed environments"
authors: "Graham C. Low; Brian Henderson-Sellers; David Han"
year: "1995"
journal: "Information & Management"
doi: "10.1016/0378-7206(94)00049-o"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Comparison of object-oriented and traditional systems development issues in distributed environments

Graham. C. Low ${}^{a,*}$ , Brian Henderson-Sellers ${}^{b}$ , David Han ${}^{c}$

$^{a}$ School of Information Systems, University of New South Wales, Sydney 2052 Australia $^{b}$ School of Computing Sciences, University of Technology, Sydney, Broadway, NSW Australia $^{c}$ Bankers Trust, Sydney, NSW Australia

## Abstract

The client/server model for application development is becoming popular with Australian organisations. While the literature suggests that issues such as task partitioning and task allocation are important in distributed application design, no prior research has been reported on the relative importance of these issues and the adequacy with which current traditional and object-oriented methodologies support distributed application design. The reported research involved a multiple case study of Australian organisations undertaking client/server development. While the same issues appear to be important for both OO and non-OO client/server development, the developers of the OO projects placed greater emphasis on task partitioning, intermodule communications, interprocess communications, and application topology. Current methodologies were found to provide little or no support for these important issues in client/server development. In fact there was no significant difference in the support offered by all methodologies.

Keywords: Distributed systems; Client/server; Object oriented; Application development; Systems development lifecycle

## 1. Introduction

Although distributed systems have been the subject of research for more than a decade, the client/server model has only recently gained popularity in the commercial environment. A 1991 survey by Dataquest [19] indicated that seventy-four percent of mainframe users are either investigating, currently migrating from, or have migrated from mainframes to distributed solutions.

Other authors indicate that distributed computing will be a major industry trend of the 1990s [10,15,32].

While many organisations are adopting the client/server computing approach, application development is often more complex than that for centralised systems $[30]$ . Not surprisingly, various authors $[14,22]$ suggest that the traditional development methodologies are generally not suited to client/server application development without modification. For instance, Jain and Purao $[18]$ recommend a modified form of systems development lifecycle. Alternatively Butler Cox $[5]$ suggest an object-oriented approach.

This study examines the importance of the main client/server application development issues in large Australian commercial organisations for both OO and non-OO development. It also examines the support provided for client/server development by their existing methodologies.

## 2. Literature review

## 2.1. Definition of the client / server model

The client/server model is an architecture for distributed processing. The objective of the model is “to make a collection of (possibly replicated) distributed services available on a network of computers” [21]. Davis [9] points out that user surveys have produced differing definitions from every respondent. Furthermore, Groff [13] believes that “everyone has his own definition” of the client/server model.

Vinea [35] provides two distinct definitions:

\- Hardware architecture model. The network is populated by information processing systems that have the roles of requesting services (clients) and providing services (servers).

\- Software architecture model. Logical processes cooperate in real time through an interprocess communications protocol; they may (or may not) be located on the same physical machine. A server is a logical process providing a service to any other process that requests it [24,20]. A client is another logical process that requests services from a server.

A client/server relationship exists when a client requests a service from the server. While it is always the client that requests the service from the server [12], the client and server may later reverse roles. In this situation, the server process becomes the client and requests a service from another server (i.e. it is hierarchic). The interaction of the client and server should be completely transparent, resulting in the user of the application not being aware that it is a client/server application [8].

There is nothing in these definitions that limits where the client and server processes may execute. They may even execute on the same computer [33].

Buzzard [6] states that “true client/server processing requires”:

(1) Communication between the clients and the servers;

(2) Client-initiated interaction with the server;

(3) Restriction by the server over conflicting requests from multiple clients;

(4) Arbitration by the server over conflicting requests from multiple clients; and

(5) Division of the application between the client and the server.

Buzzard also notes that the first four are present in most network operating systems, and that it is only the fifth that separates client/server computing from network computing.

The Gartner Group [34] suggests five classifications for the division of the application between the client and the server.

\- Distributed presentation. This involves adding presentation logic at the client (e.g. PC or Unix workstation) while keeping the existing presentation logic at the server (typically a mainframe).

\- Remote presentation. Presentation logic implemented at the client only. The server is not concerned with presentation and only sends data when requested.

\- Distributed function. Both business logic and presentation logic are implemented at the client.

\- Remote data management. All business logic is implemented at the client while the server is a database manager only.

\- Distributed data management. Data is stored at the client as well as the server.

These classifications are not mutually exclusive, since the division of an application may best be characterised by a combination of these, e.g., distributed function as well as remote data management.

## 2.2. Application design

While many organisations are adopting the client/server approach, application development is more complex. This means that the possibilities of poor application design for a client/server system are “greatly increased” [23].

A number of methodologies have been proposed for distributed application development. For instance numerous authors recommend a modified SDLC while Butler Cox [5] suggests that object-oriented techniques are well suited to client/server development.

## 3. The SDLC approach

In a traditional SDLC, the functional modules are allocated to the various components of the distributed system during the physical design. This allocation requires task partitioning and task allocation [31].

Task partitioning is the mapping of the set of logical modules and data files into a set of physical processes and data. The design goals for task partitioning are: minimisation of completion time, maximisation of reliability, and/or potential for system growth. The three objectives of task partitioning are minimisation of interprocess communications between modules, exploitation of concurrency and limiting the size of processes. Often there will need to be a tradeoff between these three objectives.

Task allocation involves the allocation of the units identified in task partitioning to one or more processors [7]. The actual allocation is dependent on issues such as interprocess communications, execution cost, load balancing and reliability.

Jain and Purao [18] suggest similar guidelines. The allocation is based on:

\- type of processing required;

\- availability of the required input data and sites at which it is required;

\- communications between tasks; and

\- processing capacity at each logical site.

## 4. Object-oriented approach

A client/server application may be characterised as a collection of objects [1]. Each object encapsulates data and the functionality pertaining to those data [25]. This aids client/server application development by grouping otherwise separate items that can be manipulated as a whole.

Not all the contents of an object are available to other objects. The principle of presenting a public interface that allows access to some parts of an object but keeps other parts private is called information hiding $[2,16]$ . An object in a client/server application can only communicate with another via the other's interface $[17,27]$ . The notion of this form of communication is well captured by Wirfs-Brock et al.'s $[37]$ use of the word collaborations to represent the set of all objects with which the object of current interest needs to communicate in order to fulfil its own responsibilities (i.e. the services it offers via its own specific interface). Communications between a client and a server object occur at run-time. While an object is a dynamic concept, the static aspects are addressed using the concept of a class. Classes thus interact via message-passing communication in which the “client” class requests a “service” from the “supplier” class. The way in which this interaction occurs, the constraints under which it occurs and the ability to undertake error trapping can best be accomplished using the theory of software contracting (e.g. $[26]$ ). Contracts define the preconditions which the client must meet before the interaction can be successful; whilst postconditions (including the invariant) specify the “promise” of the successful accomplishment of the service request.

There are two notions of contracts in the object-oriented literature. We term the first a service contract. This defines constraints on a single service (method) of a specific class. It is triggered directly by a precondition to the algorithm, the internal definition of the publicly available service.

The second notion is that of Wirfs-Brock and Wilkerson [36]; it provides a view [3] of the external services or responsibilities of the class. Each contract is applied to a collection of services such that it is specific to the interaction between the two classes. For example, the contract offered by class A to class B may cover services a,b,c whilst the contract class A offers to class C may include services c,d,e. We call this notion of contracting the interface contract.

Contracting, as investigated here, can be considered as encompassing both interface and service contracts since there are essentially three levels: feature name, signature and semantics.

The concepts of task partitioning and task allocation should also be applicable to object-oriented application development. Task partitioning would be the grouping of a set of objects with the aim of minimising interprocess communications between objects, exploiting concurrency and limiting the size of processes. Often there will need to be a tradeoff between these three objectives. Task allocation would be the allocation of the groups of objects identified in the task partitioning to one or more processors.

## 5. Research method

This research focuses on the relative importance of the various distributed application development issues to Australian organisations.

## 5.1. Survey sample

A survey was mailed to a total of 135 organisations. Every effort was made to obtain a representative sample to allow for some generalisation of Australian organisations. There were approximately equal proportions of large, medium, and small sized organisations included in the mailing list. The sample of companies represented the banking and finance, manufacturing, information technology, communications and service industries.

The survey sent to managers included a cover letter stressing the importance of the research, a self-addressed postage-paid envelope, and the 8 page questionnaire. The survey instructions required that the questionnaire be completed by the Information Technology Manager, the Applications Development Manager or professionals with client/server experience. In an attempt to encourage organisations to respond, and to provide some motivation for ensuring a greater quality of response, summary results were made available to those who completed the survey.

## 5.2. Survey validation

The survey was validated in two organisations from the service and communications sectors. Eight I.S. professionals within the two organisations with client/server development experience participated in the survey validation. Following validation of the questionnaire, minor modifications were made to Question 1 to capture information on application usage. The respondents were given an opportunity to review these minor modifications. The responses of the I.S. professionals in the two organisations were validated by post-questionnaire interview. These interviews confirmed and substantiated the robustness of the instrument.

## 5.3. Survey details

The survey was formulated on the basis of the literature reviewed in Section 2. The survey comprised a total of 6 questions. Four of these questions utilised a seven point Likert-type scale. The remaining questions were of a qualitative nature. The 6 questions are briefly outlined below.

Question 1. The organisation was requested to complete the following information for each client/server project:

\- start date and whether completed, under development, or under evaluation;

\- client/server application topology adopted; and

\- project size and development effort.

Question 2. This question assesses the importance of issues such as task partitioning, task allocation and interprocess communications in the development of each of the projects of Question 1.

Question 3 and 4. Question 3 asked what methodology was used to develop client/server applications in the organisation, while question 4 asked if any modifications had been made to the methodology to make it more appropriate to client/server development.

Table 1  
Projects employing each of the application development classifications

<table><tr><td></td><td>No. of projects</td><td>Percentage of projects</td></tr><tr><td>Distributed presentation</td><td>12</td><td>24</td></tr><tr><td>Remote presentation</td><td>9</td><td>18</td></tr><tr><td>Distributed function</td><td>16</td><td>32</td></tr><tr><td>Remote data management</td><td>17</td><td>34</td></tr><tr><td>Distributed data management</td><td>7</td><td>14</td></tr></table>

Question 5. This question ascertained the adequacy with which the methodology addressed the issues raised in Question 2.

Question 6. This question asks organisations using an object-oriented approach to application development to indicate the importance of general object-oriented concepts such as encapsulation/information hiding and generalisation/specialisation as well as the “quality” notions of responsibilities, contracts and collaborations to client/server development. These concepts are closely related, focusing largely on the notions of “good software engineering” and the responsibility driven design (RDD) approach.

## 6. Discussion of results

## 6.1. Questionnaire results

A total of 69 questionnaires were returned representing a response rate of 51.1%. Of these, 18 (26%) were completed by organisations with client/server development experience. Interestingly, 7 organisations had developed client/server applications using object-oriented concepts.

Data pertaining to 50 client/server application development projects were collected from the 18 organisations. Of the 50 projects, 32 were completed while the other 18 were still under development.

Project size ranged from 400 to 2,500,000 source lines of code with 37.9 percent of projects less than 10,000 SLOCs and 37.9 percent greater than 100,000 SLOCs.

## 6.2. Application topology

For the five classifications for the division of the application between the client and the server, Table 1 lists the number of projects employing each. It should be remembered that two or more classifications may be required to characterise a single project (i.e. the percentage value will be expected to sum to more than 100). For instance a project may have remote presentation and distributed function.

Table 2  
Project development issues

<table><tr><td></td><td>Distributed presentation Median mode range</td><td>Remote presentation Median mode range</td><td>Distributed function Median mode range</td><td>Remote data management Median mode range</td><td>Distributed data management Median mode range</td></tr><tr><td rowspan="3">Task partitioning</td><td>2.5</td><td>6</td><td>5</td><td>3</td><td>5</td></tr><tr><td>1</td><td>7</td><td>5</td><td>1,2</td><td>5</td></tr><tr><td>1-7</td><td>1-7</td><td>1-7</td><td>1-6</td><td>2-6</td></tr><tr><td rowspan="3">Intermodule communications</td><td>3.5</td><td>6</td><td>6</td><td>4</td><td>6</td></tr><tr><td>1</td><td>6,7</td><td>5,6</td><td>1</td><td>6</td></tr><tr><td>1-7</td><td>4-7</td><td>1-7</td><td>1-7</td><td>4-7</td></tr><tr><td rowspan="3">Task allocation</td><td>2</td><td>2</td><td>4</td><td>2</td><td>4</td></tr><tr><td>1</td><td>2</td><td>1</td><td>1,2</td><td>1,6</td></tr><tr><td>1-6</td><td>1-6</td><td>1-6</td><td>1-7</td><td>2-6</td></tr><tr><td rowspan="3">Interprocess communications</td><td>6</td><td>7</td><td>6.5</td><td>5</td><td>7</td></tr><tr><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td></tr><tr><td>1-7</td><td>5-7</td><td>1-7</td><td>1-7</td><td>6-7</td></tr><tr><td rowspan="3">Application topology</td><td>4.5</td><td>7</td><td>6</td><td>5</td><td>6</td></tr><tr><td>1,5</td><td>7</td><td>7</td><td>6,7</td><td>7</td></tr><tr><td>1-6</td><td>2-7</td><td>4-7</td><td>1-7</td><td>5-7</td></tr></table>

Note: 1 - not important; 7 - extremely important.

Table 3  
OO versus non-OO application development issues

<table><tr><td></td><td>OO development Median mode range</td><td>Non-OO development Median mode range</td><td>OO and non-OO development Median mode range</td></tr><tr><td rowspan="3">Task partitioning</td><td>5</td><td>2</td><td>5</td></tr><tr><td>5</td><td>1</td><td>5</td></tr><tr><td>3-7</td><td>1-7</td><td>1-7</td></tr><tr><td rowspan="3">Intermodule communications</td><td>6</td><td>5</td><td>5</td></tr><tr><td>6</td><td>1</td><td>6</td></tr><tr><td>3-7</td><td>1-7</td><td>1-7</td></tr><tr><td rowspan="3">Task allocation</td><td>2</td><td>2</td><td>2</td></tr><tr><td>2</td><td>1</td><td>1</td></tr><tr><td>1-6</td><td>1-7</td><td>1-7</td></tr><tr><td rowspan="3">Interprocess communications</td><td>7</td><td>6</td><td>5.5</td></tr><tr><td>7</td><td>7</td><td>7</td></tr><tr><td>5-7</td><td>1-7</td><td>1-7</td></tr><tr><td rowspan="3">Application topology</td><td>7</td><td>5</td><td>6</td></tr><tr><td>7</td><td>5</td><td>7</td></tr><tr><td>1-7</td><td>1-7</td><td>1-7</td></tr></table>

Note: 1 - not important; 7 - extremely important.

## 6.3. Project development issues

Table 2 lists the relative importance of the various application development issues. Application designs involving distributed presentation and remote data are relatively simple. In the former case presentation logic is added to the client while keeping the existing presentation logic at the server. In the latter case all business logic is implemented at the client while the server is the database manager. In the case of remote presentation, distributed function and distributed data consideration needs to be given to splitting the presentation, function and data between client and server. Here more attention should, theoretically, be given to distributed application design issues. A Mann-Whitney Rank Sum W Test was used to compare the two groups of application design types (distributed presentation and remote data versus remote presentation, distributed function, and distributed data). A significant difference was found in the respondents' ratings for task partitioning (p = 0.0006) and intermodule communications (p = 0.048). The latter is a design issue in task partitioning.

![](/api/attachments/A4SF43WB/fulltext/images/5979b4722d6ab74030f73be5b9d413fda0fcd3c89c9add31e3d34a17e04adadd.jpg)  
Importance of task partitioning  
Fig. 1. Task partitioning as an application development issue.

The importance of various distributed application development issues is presented in Table 3 and Figs. 1–5 for both for the OO and non-OO projects. One of the main issues considered in task allocation, interprocess communications, was rated as important (rating 5–7) for 100 percent of OO projects and 75 percent of non-OO projects.

![](/api/attachments/A4SF43WB/fulltext/images/3e8b2754e0a9cfe0bcb0056bf39661b087a0a44a156e121f2632aba4b11fd557.jpg)  
Importance of intermodule communications  
Fig. 2. Intermodule communications as an application development issue for both OO and non-OO systems.

![](/api/attachments/A4SF43WB/fulltext/images/560aaf25d587d80f9a8bcbe4dc3a174c4cafe6fcc92a2cd5cfd20bbe510a0a8b.jpg)  
Importance of task allocation

Fig. 3. Task allocation as an application development issue for both OO and non-OO systems.  
![](/api/attachments/A4SF43WB/fulltext/images/0c324ac0d43e04f2472085982cf3965d1862fd7ccfdb8366ce2a8a35b63a9f1f.jpg)  
Importance of interprocess communications  
Fig. 4. Interprocess communications as an application development issue for both OO and non-OO systems

![](/api/attachments/A4SF43WB/fulltext/images/4adfc4e304b656d233a52bc29b7efdab331e31ef34b2cc446261567ea9868e98.jpg)  
Importance of application topology  
Fig. 5. Application fits a particular application development classification as an application development issue for both OO and non-OO systems.

However task allocation, which also considers minimisation of execution cost, load balancing and reliability, was not considered an important issue (rating 1-2) for over 60 percent of the projects. Further work is required to determine the impact of these other task allocation factors on commercial application development.

The issues of task partitioning, intermodule communications, interprocess communications and application topology are considered significantly more important (at the 0.05 level) by the developers of OO client/server applications than the developers of non-OO client/server applications. One possible explanation is OO techniques may be inherently more suited to client/server style development. Another explanation may be that the developers of non-OO applications may have a steeper learning curve due to their main-frame experience.

## 6.4. Application design issues supported by methodology

How well the organisation's current methodology supports each of the application design issues is presented in Table 4 and Figs. 6–10 now, more

Table 4  
Application design issues supported by the organisation's methodology

<table><tr><td></td><td>OO development Median mode range</td><td>Non-OO development Median mode range</td><td>OO and non-OO development Median mode range</td></tr><tr><td rowspan="3">Task partitioning</td><td>3</td><td>5</td><td>5</td></tr><tr><td>3,5</td><td>5,6</td><td>5</td></tr><tr><td>1-7</td><td>1-6</td><td>1-7</td></tr><tr><td rowspan="3">Intermodule communications</td><td>3</td><td>5</td><td>5</td></tr><tr><td>2,6</td><td>5</td><td>5</td></tr><tr><td>1-7</td><td>1-7</td><td>1-7</td></tr><tr><td rowspan="3">Task allocation</td><td>3</td><td>5</td><td>3</td></tr><tr><td>1,3,7</td><td>1</td><td>1</td></tr><tr><td>1-7</td><td>1-7</td><td>1-7</td></tr><tr><td rowspan="3">Interprocess communications</td><td>2</td><td>5</td><td>5</td></tr><tr><td>1,2</td><td>5</td><td>5</td></tr><tr><td>1-7</td><td>1-7</td><td>1-7</td></tr><tr><td rowspan="3">Application topology</td><td>6</td><td>4</td><td>5</td></tr><tr><td>6</td><td>1,6</td><td>6</td></tr><tr><td>1-7</td><td>1-7</td><td>1-7</td></tr></table>

Note: 1 - not supported at all; 7 - extremely well supported.

appropriately, categorised on a company basis. No significant difference $p = 0.05$ was found in the support provided by OO and non-OO methodologies. Support provided by current methodologies was generally less than satisfactory. For instance only 43 percent of OO methodologies and 73 percent of non-OO methodologies adequately support interprocess communications (rating 5–7). This is of particular interest since every developer of OO projects rated interprocess communications as important. Obviously the support required by many of the developers is unavailable in their current methodology.

![](/api/attachments/A4SF43WB/fulltext/images/3c393870a9fe1d1d605b3ceb34b84dcdca629d0862c62fb026c6a2b982f9f682.jpg)  
Importance of task partitioning  
Fig. 6. Methodology support for task partitioning.

![](/api/attachments/A4SF43WB/fulltext/images/38d9cdf70db1b53572ba439ff7d2c3f204bac08193d192bcb1a2e0ba69244d98.jpg)  
Importance of intermodule communications  
Fig. 7. Methodology support for intermodule communications.

![](/api/attachments/A4SF43WB/fulltext/images/abc93957c4a9402e0e30da74610473f889c8127692ef8959a2d8ba049c4abe79.jpg)  
Importance of task allocation  
Fig. 8. Methodology support for task allocation.

Seven of the eighteen organisations had modified their methodology for client/server development. Interestingly, these organisations did not report greater support for any of the client/server application development issues than the other organisations.

To test whether support by the methodology for specific application design issues affected the respondents' rating of the importance of the various application design issues for specific applications a Wilcoxon Matched-Pairs Signed-Ranks test was performed. Only application development classification (p = 0.028) and interprocess communications (p = 0.006) were significant.

![](/api/attachments/A4SF43WB/fulltext/images/9218fd89cb8df8238f39c37f2685cb7ca11b85ffcf35d80729d47b6766be9791.jpg)  
Importance of interprocess communications  
Fig. 9. Methodology support for interprocess communications.

![](/api/attachments/A4SF43WB/fulltext/images/77d9fcb17af4da7438c38ae92ce8edce7263cd36ceb1dc9a6e404bb8dc219dc0.jpg)  
Importance of application topology  
Fig. 10. Methodology support for application development classification.

![](/api/attachments/A4SF43WB/fulltext/images/9d0ac8405f8ec99abda2eb9364867ce02b52d2c30710bed17a113746f1fa5201.jpg)  
Importance of encapsulation and information hiding  
Fig. 11. Importance of encapsulation/information hiding in client/server application development.

## 6.5. Object-oriented concepts

The importance of various object-oriented concepts in the development of client/server applications is shown in Table 5 and Figs. 11–16. It is clear that less emphasis, in these organisations, is placed on the “quality” notions of responsibilities, contracts, and collaborations. Whilst acknowledged in the academic literature as crucial concepts to engendering a quality revolution in software engineering, they do not figure significantly in many of the methodologies currently in use in industry (e.g. [29]). At the same time, the two most readily identifiably important concepts of encapsulation/information hiding and generalisation/specialisation are widely advocated as basic tenets of object technology (e.g. [4,11,16]). These results are thus suggestive of the impact of the extent of emphasis of basic technology concepts as opposed to the more sophisticated software engineering concepts embodied by notions of responsibilities and contracting, which play a central role in most second generation OO analysis/design methodologies (e.g. [28]).

Importance of various object-oriented concepts in client/server application development

<table><tr><td></td><td>Median</td><td>Mode</td><td>Range</td></tr><tr><td>Encapsulation/information hiding</td><td>6</td><td>7</td><td>4-7</td></tr><tr><td>Generalisation/specialisation/ inheritance</td><td>6</td><td>6,7</td><td>1-7</td></tr><tr><td>Subsystems</td><td>5</td><td>5,6</td><td>1-6</td></tr><tr><td>Responsibilities</td><td>4</td><td>4</td><td>1-6</td></tr><tr><td>Contracts</td><td>5</td><td>1,3,5,6</td><td>1-7</td></tr><tr><td>Collaborations</td><td>3</td><td>1</td><td>1-6</td></tr></table>

Note: 1 - not important; 7 - extremely important.

![](/api/attachments/A4SF43WB/fulltext/images/19b6f531b77301fd0d0e1582ba8912c3211464609bdc93c2f80267541a995edb.jpg)  
Importance of generalisation/ specialisation/ inheritance  
Fig. 12. Importance of generalisation/specialisation/inheritance in client/server application development.

![](/api/attachments/A4SF43WB/fulltext/images/bb921cf4d7c5a3bdd06e0190c560910afab346b70dac8343482a4664a88afa31.jpg)  
Fig. 13. Importance of subsystems in client/server application development.

## 7. Conclusions

While the same distributed systems issues appear to be important for both OO and non-OO client/server development, the developers of the

![](/api/attachments/A4SF43WB/fulltext/images/51ba66ac4eb47830c7e036ea4aa31a4185e47215cb93112876173ba68f4c5a5b.jpg)  
Fig. 14. Importance of responsibilities in client/server application development.

![](/api/attachments/A4SF43WB/fulltext/images/51a6b2f10701ec30d6bf7b28e9413b99058fef7f05dcd07ced5f83667748cecc.jpg)  
Fig. 15. Importance of contracts in client/server application development.

![](/api/attachments/A4SF43WB/fulltext/images/b838b39758ac7f8a013fec15000a0b466c367cae0fe3d537bb107deed6cfba41.jpg)  
Fig. 16. Importance of collaborations in client/server application development.

OO projects placed greater emphasis on task partitioning, intermodule communications, interprocess communications and application topology. However the support offered by OO and non-OO methodologies was not significantly different. In fact many of the current methodologies provide little or no support for these important issues. This may be due to the relative immaturity of distributed application design in commercial organisations with little need for commercial methodologies to support this issue in the past.

Encapsulation/information hiding and specialisation/generalisation are the two most important specific OO concepts in client/server development. The task partitioning process involves the mapping of a set of logical modules and data files into a set of physical processes and data. The fact that each object already encapsulates data and functionality pertaining to the data would be expected to simplify the task partitioning process. Hence it is little surprise that respondents rated this an important issue. Software contracting, responsibilities and collaborations would be expected to improve the “quality” of the client-server interaction. However respondents were not in agreement as to its importance. A possible explanation is the relative newness of client/server development with developers more concerned with the actual development of a working application than its “quality”. This could also explain why a number of respondents did not regard basic distributed application design concepts, such as task partitioning and task allocation, as important.

The parallel between distributed computing support and object-oriented concepts is, however, clear. The two models are easily integrable. As distributed computing begins to dominate the marketplace and object technology matures to be the accepted standard approach to software engineering, this integration becomes vital.

## References

[1] Almes, G.T. and Holman, C.L., "Edmas: An Object-Oriented, Locally Distributed Mail System", IEEE Trans.

Software Engineering, Vol. 13, No. 9, Sep. 1987, pp. 1001–1009.

[2] Berard, E.V., Essays on Object-Oriented Software Engineering, Volume I, Prentice Hall, Englewood Cliffs, 1993, 352pp.

[3] Bielak, R. and McKim, J.C., “The many faces of a class”, J. Obj.-Oriented Programming, Vol. 6, No. 5, 1993, pp. 81–85.

[4] Booch, G., Object Oriented Design with Applications, Benjamin/Cummings, Menlo Park, CA, 1991, 580pp.

[5] Butler Cox Foundation, “Introducing Object Orientation”, Research Report 88, August, 1992.

[6] Buzzard, J., “The Client/Server Paradigm: Making Sense Out Of The Claims”, Data Base Adviser. Vol. 8, No. 8, 1990, pp. 72–80.

[7] Chu, W., Holloway, L., Lan, M. and Efe, K., “Task Allocation In Distributed Data Processing”, IEEE Computer, Nov. 1980, pp. 57–69.

[8] Colony, G., President of Forrester Research Inc., reported by Mead, T., "The Attraction Is Price", Datamation, March 15, 1990, pp. 49–51.

[9] Davis, D., "Where Client/Server Fits", Datamation, July 15, 1991, pp. 36–38.

[10] Edelstein, H.A., “Lions, Tigers, and Downsizing”, Database Programming and Design, Vol. 5, No. 3, Mar. 1991, pp. 39–43.

[11] Graham, I., Object Oriented Methods, Addison-Wesley, Wokingham, 1991, 410pp.

[12] Gomaa, H., “A Software Design Method For Distributed Real-Time Applications”, J. of Systems And Software, Vol. 9, No. 2, 1989, pp. 81–94.

[13] Groff, J., Director Of Worldwide Product Marketing, Networks And Communications, Apple Computer Inc., reported by Kay, E., “Mac Managers Explore Client/Server Systems”, MacWEEK, Vol. 4, No. 38, 1990, pp. 38–39.

[14] Gupta, U., “Iterative Process, 4GL’s best for GUIs”, Software Magazine, Vol. 12, No. 4, Mar. 15, 1992, pp. 52.

[15] Harding, E.U., “Downsizing has arrived”, Software Magazine, Vol. 11, No. 13, Nov. 1991, pp. 27–28.

[16] Henderson-Sellers, B., A BOOK of Object-oriented Knowledge, Prentice Hall, Sydney, 1992, 297 pp.

[17] Hutchison, D. and Walpole, J., “Distributed Systems and Objects” in G. Blair, J. Gallagher, D. Hutchison, and D. Shepherd (eds.), “Object-Oriented Languages”, Longman Group, London, 1991.

[18] Jain, H. and Purao, S., “Distributed Application Development: SDLC Revisited”, Information and Management, Vol. 20, 1991, pp. 247–255.

[19] Kador, J., “Downsizing is ready for Prime Time (Companies Cut Costs, Improve Quality by Converting to Networked Microcomputers”, Midrange Systems, Vol 5, No. 9, 1992, pp. 50–51

[20] Levy, E. and Silberschatz, A., Distributed File Systems: "Concepts and Examples", ACM Computing Surveys, Vol. 22, No. 4, 1990, pp. 321–374.

[21] Levy, H. and Tempero, E., “Modules, Objects and Distributed Programming: Issues in RPC and Remote Object Invocation”, Software: Practice and Experience, Vol. 21, No. 1, 1991, pp. 77–90.

[22] Low, G., “Security Perspective of Client/Server Development”, Research Report No. 93/20, School of Information Systems, Univ. New South Wales, 1993.

[23] Low, G.C. and Russell., P., “Application of the Client/Server Model on LANs”, IFIP Transactions: Local Area Network Applications: Leveraging the LAN”, in D.R. Vogel, P.H. Marshall, B.C. Glasson and A.A. Verrijn-Stuart (eds.): “Computer Security in the Age of Information”, Elsevier Science Publishers B.V. (North Holland), 1993, pp. 107–122 with P. Russell.

[24] McGoveran, D. and White, C., “Clarifying Client/Server”, DBMS, November 1990, Vol. 3, No. 12, pp. 78–90.

[25] Meyer, B., “Object-oriented Software Construction”, Prentice Hall, Hemel Hempstead, 1988, 534pp.

[26] Meyer, B., “Applying design by contract”, IEEE Computer, Vol. 25, No. 10, 1992, pp. 40–51

[27] Nascimento, C. and Dollimore, J., “Behaviour Maintenance of Migrating Objects in a Distributed Environment”, Journal of Object-oriented Programming, Sep. 1992, pp. 25–33.

[28] Nerson, J.M. and Walden., K., Seamless Object-Oriented Architecture, Prentice Hall, 1994, 301pp

[29] Rumbaugh, J., Blaha, M., Premerlani, W., Eddy, F. and Lorensen, W., “Object-oriented Modelling and Design”, Prentice Hall, Englewood Cliffs, 1991, 500pp.

[30] Schill, A., “Distributed Application Support: Survey And Synthesis Of Existing Approaches”, Information And Software Technology, Vol. 32, No. 8, 1990, pp. 545–558.

[31] Shatz, S. and Wang, J., "Tutorial: Distributed Software Engineering", IEEE Computer Society Press, 1989.

[32] Stodder, D., "Return of Process: Client/Server Computing forces us to reexamine the Data Centric Approach", Database Programming and Design, Vol. 5, No. 3, March 1992, pp. 5–7.

[33] Svobodova, L., "File Servers For Network-Based Distributed Systems", ACM Computing Surveys, Vol. 16, No. 4, 1984, pp. 353–398.

[34] Venema, T., “Client Server and DB2”, Software AG Canada, presentation in Sydney, 1992.

[35] Vinea, V., “Preparing for a Distributed Environment, Suitable Architectures and Software”, Information Systems Management, Vol. 9, No. 2, 1992, pp. 79–81.

[36] Wirfs-Brock, R.J. and Wilkerson, B., "Object-oriented Design: A Responsibility-driven Approach", Proc. OOPSLA' '89, New Orleans, Oct. 1–6, 1989, SIGPLAN NOTICES, Vol. 24, No. 10, Oct. 1989, pp. 71–75.

[37] Wirfs-Brock, R.J., Wilkerson, B. and Wiener, L., Designing Object-oriented Software, Prentice Hall, New York, 1990, 368pp.

![](/api/attachments/A4SF43WB/fulltext/images/ca4f7f13157c2dd1f9ab36b43e9f04820716f7fcd24d728381156961e60463e4.jpg)

Graham Low received his B.E. and Ph.D degrees from the University of Queensland. He is currently a Senior Lecturer in the School of Information Systems at The University of New South Wales. His current research interests include software engineering (metrics, CASE, reuse) and methodologies for the development of commercial distributed application systems. He had in excess of 10 years MIS experience in industry prior to

joining the School in 1987.

![](/api/attachments/A4SF43WB/fulltext/images/b39f1183f1bc18f4bc6d5def1efbfd8717491c209f6311640fdfcc1c72577fcb.jpg)

Brian Henderson-Sellers is Director of the Centre for Object Technology Applications and Research and Professor of Information Systems in the School of Computing Sciences at the University of Technology, Sydney. His current research interests include object-oriented systems development methodologies and notation (the co-developer of the MOSES full lifecycle methodology); implementations of the object-oriented paradigm in the com-

mercial environment (metrics, project management and migration paths); environmental decision support and simulation modelling; and has published extensively in these research areas; including 10 books and a software package. He is Convenor of the Object-Oriented Special Interest Group of the NSW Branch of the Australian Computer Society and is Regional Editor (Asia/Pacific) of the new international journal Object-Oriented Systems

![](/api/attachments/A4SF43WB/fulltext/images/90235bfd9304eb834709dc570845e817dd4c5c48131f496064d76749cda97fc4.jpg)

David Han graduated from The University of New South Wales with a Bachelor of Science (Business Information Technology) degree in 1994. He is currently working as a systems developer at an Australian merchant bank. His research interest is in the use of object-oriented techniques for the development of client/server applications.

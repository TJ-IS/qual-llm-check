---
otero_id: 17656
otero_key: "GC4UMHEV"
title: "Software reuse: Issues and an example"
authors: "M. Ramesh; H. Raghav Rao"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90074-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Software reuse: Issues and an example

M. Ramesh

AT&T Bell Labs, Naperville, IL 60566, USA

H. Raghav Rao

SUNY Buffalo, Amherst, NY 14260, USA

Reusability is a general principle that is instrumental in avoiding duplication and capturing commonality in inherently similar tasks. It simplifies and unifies classes of phenomena and is the basis for economic justification for developing reusable software products that make computers and programmers more productive. This paper provides an overview of some of the major issues in reuse combined with practical experience based on a case study of reuse in the telecommunications industry: a project of moderate complexity on signaling link provisioning that was carried out at AT&T Bell Labs. The project incorporates reuse into the prototyping paradigm. The benefits of reuse are quantified, and their effect on productivity is shown. In addition, a simple and effective intelligent reuse support system, based on concepts of rule based expert systems and relational databases, is detailed for use as a meta-language interface for automatic code (skeleton) generation. The case illustrates many significant aspects associated with the integration of reuse in information systems development.

Keywords: Reuse; Intelligent reuse support system; Prototyping; Case study.

## 1. Introduction

Reusability has been defined as “a general engineering principle whose importance derives from the desire to avoid duplication and to capture commonality in undertaking classes of inherently similar tasks.

Masoor Ramesh is a MEMBER of the TECHNICAL STAFF in the 5ESS Switch Call Processing department at AT&T Bell Laboratories in Naperville, Illinois. He is responsible for the planning, design and developmental of Bellcore Standard ISDN Protocol. He worked on the implementation of Stimulus Signaling Protocol for National ISDN-1. Mr. Ramesh joined the company in 1986 with an M.S. in Computer Science from Stevens Institute of Technology, Hoboken, New Jersey, M.B.A. in Finance from Faculty of Management Sciences, New-Delhi, India and B.S. in Electrical Engineering from University of Delhi, India. His interests include application of Expert Systems concepts to aid production and maintenance of large-scale software.

Dr H. Raghav Rao is an Assistant Professor at the State University of New York, Buffalo. He graduated from Purdue University (Krannert) with a PhD in MIS in December 1987 and has an M.B.A. from the University of Delhi, India and a Bachelor of Technology degree in Chemical Engineering from IIT Kanpur, India. His publications have appeared in Applied Artificial Intelligence, Automatica, Communications of the ACM, Computer Science in Economics and Management, Discrete Applied Mathematics, Decision Support Systems, IEEE Expert, Information and Management, Interfaces, IEEE Transactions on Systems, Man and Cybernetics Journal of Intelligent Manufacturing, Long Range Planning, and MIS Quarterly among others. He recently received a University (Lily) teaching fellowship for innovative teaching in MIS.

It simplifies and unifies classes of phenomena and provides economic justification for developing reusable software products that make computers and programmers more productive" [30].

The premier motivation behind reuse is that it brings pre-structured information to bear on the problem. It allows knowledge about problem domains to be accumulated and to be shared. The reuse of existing information systems (IS) components to build new systems amplifies the systems designers' capabilities, by reducing the total number of components needed for systems development. This in turn, facilitates the validation and verification process, a critical aspect of controlling the quality of an information system. An important point is that in terms of the learning curve of systems developers, reusable components are already at the top of the learning curve, while the rest of the system is much lower on the curve. Thus, incorporating the use of reusable components into the development process can increase the productivity of the developer, and the quality of the system, while at the same time, reduce costs. In addition, it decreases the amount of risk that is associated with a project, precisely because knowledge about part of the project (the reusable components) lends structure to the problem.

The reuse of various software products (e.g. code fragments, procedures or functions, and components) is almost as old as programming itself. However, “reuse has yet to become a significant part of the software development process” [31], for various reasons. For instance, the issue of reuse cannot be separated from choice of a systems development paradigm. Reuse in systems development methods such as prototyping and the traditional life cycle systems development approaches is limited in scope and effectiveness by two components. First, to be widely effective, structure and definition of how to encapsulate and define reusable code must be attained. Second, reusable code is only reusable if it can be located easily. Its effectiveness increases if it can be applied to perhaps unrelated systems as well. Within a community of common system development, with common architectural foundations, reuse can contribute extensively to “rapid prototyping”. Beyond the closed community, there is much to be done before the larger benefits of reuse can be achieved.

This paper discusses some of the major issues in reuse and combines it with practical experience from a case study of reuse in the telecommunications industry. A prototype project on a signaling link provisioning project that was carried out at AT&T Bell Labs is described. Signaling links deal with the transmission of control signals in state-of-the-art telephone switching systems. These links, and the associated provisioning process related to their setting up and maintenance are highly critical to switching networks, and hence require simple yet very reliable software. The project incorporates concepts of reuse into the prototyping paradigm. Of course, the case cannot be used to statistically generalize the results, but it illustrates many significant aspects associated with the integration of reuse in information systems development. The experience is used to detail a simple and effective intelligent reuse support system to act as a meta-language interface for automatic code (skeleton) generation. The reuse support system is detailed in two parts: the first uses a faceted classification scheme and concepts of domain analysis and the second is based on concepts of rule based expert systems and the relational database approach. In addition, the paper discusses a natural extension to the concept of reuse support systems: the software reuse resource center. Finally, we endeavor to provide some insight into implementing reuse in the workplace.

## 2. Background on reuse and prototyping

The historical approach to systems development has been the traditional life cycle approach. This is often considered to be an inadequate model for achieving user satisfiable systems. Several alternative strategies for developing systems have been generated $[1,5,11,20,21]$ the phased commitment approach, the evolutionary approach to systems development, the strategy of end-user development, the approach of buying packages instead of building systems in-house, and prototyping. This section discusses prototyping, and reuse, and the incorporation of concepts of reuse in prototyping and systems development.

## 2.1. Prototyping

Prototyping $[1,8,9,10,18]$ is the process of developing a scaled-down version of a system to use in building a full scale system. Many definitions have been suggested. We quote one that perhaps explains it most succinctly $[22]$ “A system that captures the essential features of a later system,... A prototype system intentionally incomplete, that is to be modified, expanded, supplemented, or supplanted”... Such a system allows an analyst to resolve basic feasibility issues, before tackling details such as error proofing, and documenting the final system. The additional benefit of prototyping is that it allows an early exposure of the major ambiguities, pit falls and traps that the analyst is likely to encounter in the process of translating the specifications into the final system.

Prototyping is often the first activity that occurs in a development project. It continues through each of the different phases of the system life cycle. Computer aided methods allow the rapid prototyping of a system in contrast to the use of lengthy conventional approaches such as structured analysis, systems analysis charts, and pseudocode. The key characteristic of rapid prototyping is the process of iterative decision making. Requests for specification changes can be entertained at any point in the development process, as the user experiments with a working model of the system and gains insight into it. By using incremental development processes involving reusable components where available, rapid prototyping has been found to be an effective technique for eliminating large amounts of wasted effort $[13,16]$ . In this paper, we describe a case study, where rapid prototyping is carried out by using combinable reusable components in an attempt to use software down to the code level. The aim is not to attain a perfect match, between the application to be developed and the code to be reused, in the prototype. Instead it is to find a satisfactory solution, where a system matching to a large degree is equally satisfactory as a system matching almost perfectly, considering the substantially lower costs incurred in the development process.

## 2.2. Reuse

The motivation behind reuse is that it brings pre-structured information (partially specified architectures) to bear on the problem. For instance, a component could be used in successive versions of an evolving product, during the various phases of prototyping, as well as in a variety of different applications. Researchers feel that reuse in successive variations of an evolving product appears to be an important source of increased productivity through reduction of maintenance and enhancement costs $[30]$ .

## 2.2.1. Classes of reuse

Reuse in software engineering falls into two major classes: Composition technologies and generation technologies $[4]$ . Composition technologies are characterized by the fact that building blocks of atomic or concrete, self contained components can be built up into new systems. Examples of such items are code skeletons, subroutines, functions, and programs. Generation technologies are not as easily characterized since reused components, which are more like patterns, such as patterns of code and patterns of transformation rules, cannot be isolated as being atomic. Resulting structures cannot be traced back to their originating patterns and only bear a distinct resemblance to the components that generated them. Each of these technologies has evolved from two major approaches: the use of reusable building blocks and reusable patterns.

The classical technique, considered passive in nature, has been to use reusable building blocks. Such building blocks typically are libraries of routines such as procedures, functions, subroutines and subprograms and Smalltalk-type objects. Each instance of a building block implements a well defined operation and can thus be thought of as a distinct atomic component. Every component should exhibit high cohesion and low coupling; should have a clearly distinct interface; should not interfere with the environment; should be standardized in terms of invoking, controlling, error handling, communication and structure; and should have easy readability. Well defined composition principles are applied to the building blocks in order to build new programs.

On the other hand, the technique of using reusable patterns is an active method of generating new information systems. There are three basic classes of systems that are based on reusable patterns: language based systems, application generators, and transformation systems $[4]$ . For instance, reusable patterns in application generators consist of patterns of code about specific domains that can be reused when producing similar systems in that domain, while reusable patterns in transformation systems are embedded in transformation rules. Thus it is possible to produce similar systems by reusing the proper set of transformations.

## 2.2.2. Related research

Recently, there has been considerable research in the field of software reuse, with encouraging conclusions. Lenz et. al. [19] apply building block concepts of reuse to systems programming at IBM, and report positive results. The building blocks consist of small routines in which the functionality is totally encapsulated. A library of such building blocks is set up and used in a general systems programming area. This has proved to be highly productive and has become a precursor for an automated reuse environment. Burton et al. [7] discuss reusable software libraries (RSL) developed at Intermetrics. The RSL effectively finds and evaluates reusable components, through a process of search using keywords. RSL is further integrated with the Software Component Retrieval and Evaluation (SCORE) tool in order to evaluate reusable components based on designers' responses to questions about software requirements. Swanson and Curry [28] report on an asset management program developed at GTE Data Services that is dedicated to the development and implementation of reusable information system components (assets). They describe an on-line asset shelf catalog system (based on Prieto-Diaz and Freeman's [24] scheme) which is a faceted classification and rapid retrieval mechanism for asset information. Karimi [17] proposes an assets based systems development strategy for improving software reusability within an organization. The proposed strategy is an extension of the concepts of information assets taken from the data driven or data-oriented concepts proposed by the National Bureau of Standards, Fifth Database Workshop, as reported in Appleton [2].

The importance of the concept of reuse cannot be overstated. Prieto-Diaz and Freeman $[24]$ report on the increased productivity gains of certain Japanese firms that use reusable software. Old software inventories are considered valuable assets and these are retrofitted for reusability by improving documentation, maintainability, and modifiability through an integration with techniques from other disciplines such as production engineering and resource management. Another interesting example of a successful application of software reuse is the program to generate color slides on a color CRT developed by Standish $[27]$ . A heavy reliance on software reuse helped to “make the prototyping truly rapid”. One common example of reusability is the spreadsheet program. This is particularly so because of the growth of a secondary industry surrounding spreadsheets. Spreadsheet templates for various applications ranging from checkbook balancing to cashflow projection to inventory control have been developed as reusable code modules $[16]$ .

In this paper a Reuse Support System is detailed in two parts. The first part incorporates principles of composition technology, most significantly Prieto-Diaz and Freeman's [24] scheme, into the rapid prototyping process. The second part then uses principles of generation technology and details how reuse concepts can be augmented with an expert system interface, which can be used as a meta-language interface for automatic code (skeleton) generation.

## 3. Software reuse - case results

## 3.1. The prototyping project

The project was aimed at showing how software reuse could be quantified and thus provide a better understanding of the implications of reuse. The project was not intended to provide statistical evidence for the reuse of software. It was essentially meant to serve as a real life example for integrating reuse into the prototyping process.

The project deals with the development of a Testing Operations Provisioning and Administration System (TOPAS $^{TM}$ ) for the proprietary Electronic Switching System (ESS) used by AT&T for telecommunication. TOPAS is a medium-sized, highly complex real-time operation support system software. It is used to administer and monitor large telephone networks, and telephone switching systems.

Some state-of-the-art telephone switching systems have two distinct links; a signaling link which deals with the transmission of control signals that are used in signaling, and a message link that is concerned with the transmission of voice messages over the system. Signaling links are few in number, and the amount of database activity on the links is relatively low. However they are highly critical to the network and so a simple yet reliable software is needed for the provisioning (setting up and maintenance) process. The project was solely concerned with the development of the signaling link system provisioning database, and the provision of maintenance capabilities and functions required to support the trunks and facilities.

The motivation behind the emphasis on the contribution of reuse in the prototyping process was as follows: When the requirements for the project were analyzed, it was found that a significant portion of the design and code were very similar to the design and software built for its predecessor. Reviewing the requirements for the earlier system, TOPAS1, and TOPAS2 (so named to differentiate from TOPAS1) it was found that the functionality was essentially the same and that the major changes existed in accepting data and error handling. The modules were fairly complex, good documentation for TOPAS1 was easily available, TOPAS1 had very high ratings on quality and reliability and the experts who developed the software were also easily available at that time. This situation was very conducive to experimenting with reuse and applying theory to practice. Hence, a design specification which included the principle aspects of the design of TOPAS1 was drawn. The process of reusing the design also motivated the reuse of code.

The prototype that was developed was a unit of TOPAS2. TOPAS1 is an earlier version of the TOPAS project that dealt with Circuit Provisioning (CPR) involving voice message transmission. TOPAS2 dealt with Signaling Link Provisioning (SLP). The CPR System received data electronically so no human machine interface to input data was required. SLP however, required a human-machine interface as data and had to be input using screens. The basic differences between TOPAS1 and TOPAS2 are summarized in Table 1.

The entire development plan for TOPAS2 was organized as follows: (1) Design, (2) Prototype Preparation, (3) Reuse Considerations, (4) Documentation, (5) Implementation, (6) Testing.

Three design alternatives were available: (1) Implement a new design, (2) Modify the existing TOPAS1 software, (3) Reuse certain portions of the existing software for TOPAS1, and embed them in a new design.

Alternative 3 was the most viable. TOPAS1 provided a rich library of provisioning routines which could be reused. The circuit provisioning design was good; adequate documentation was available and the database design was similar. Since TOPAS2 signaling link provisioning is driven via a human-machine interface using screen data entry, as opposed to TOPAS1 which was driven through electronic data

## Table 1

Differences Between Topas1 and Topas2.

<table><tr><td>TOPAS1</td><td>TOPAS2</td></tr><tr><td>Based on Circuit ProvisioningNo. 4 Electronic SwitchingSystem (ESS) specific</td><td>Based on Signaling Link ProvisioningNo. 5 ESS specific</td></tr><tr><td>Message Trunk ProvisioningElectronic Data TransferNo Mating LinksVolume, tens of thousandsTrunks in DataBase</td><td>Signaling Link ProvisioningData Entered using ScreensMating Link ProvisioningVolume, a few hundredLinks in DataBase</td></tr></table>

transmission, changes had to be made in the overall design to accommodate the user interface; for instance, appropriate screens, real-time validation of data and error messages had to be developed.

The link provisioning system is completely driven by screen data entry. This implies that user interaction is a critical factor in system design. Two major components of systems for user interaction are screens and menus used in screen design. In order to get rapid feedback from users it is advisable to develop both the screens and menus through a prototyping process. Prototyping not only allows substantial improvement of software usability, but also helps in the integration of the software with the rest of the system, as well as provides the system designer with early warning signals of potential problems with the design.

The TOPAS1 project already provided a library of provisioning routines since an extensive feature of TOPAS1 was the Circuit Provisioning (CPR) feature which could be tailored to Signaling Link Provisioning (SLP). Most of the changes pertained to error handling and designing the error handler to send messages to the user instead of a log as existed in the original design. The two candidate modules that were prototyped were two Signaling Link Provisioning modules: the modules that add linkage information, SLP\_add, and update the relevant link information, SLP\_upd. For instance, links have various characteristics, namely, speed, locations of the ends, status, whether it is multidirectional or unidirectional and so on. The two modules mentioned above in addition to a utility module will maintain such information in the database.

The implementation of the project was done in phases. A work breakdown structure was first developed to identify the major modules, set priorities as to the sequencing of major module implementation, and help in identifying demonstrable modules. The work flow and feedback process provided the systematic sequence of events for developing the Link Provisioning. Note that the problem was a moderately difficult problem, (the degree of difficulty is similar to that for developing code for $C^{3}I$ Systems, as described by Shultz [26]), since it involved the development of human-machine interfaces, and implementing processes that talk to each other via message exchange. The sending and receiving of messages had to be very well coordinated using schedulers and message unloaders. In addition, every input had to be checked to ensure data-base integrity.

## 3.2. Quantification of reuse in the project

The size of a program can be computed by using lines of code, token count, and/or function count. It is easy to calculate the size of a program when it is written from scratch. However, when reused code is involved in the code development process, a count of the number of lines of code is not enough. The “Equivalent Size Measure” [10] captures the effort required to develop a product with reused and new code, in relation to the effort needed to develop the product with purely new code.

Equivalent size measure $(S_{e})$ is a software metric that relates both new $(S_{n})$ and reused code $(S_{u})$ in terms of lines of code (LOC). Lines of code refer to any line of program text that is not a comment or a blank line regardless of the number of statements or fragments of statements on a line. This specifically includes all lines, executable and non-executable, program headers and declarations. Two of the most recommended functions for equivalent size measures are the linear and nonlinear equations:

$$
(a) S _ {e} = S _ {n} + k ^ {*} S _ {u} \text { and }
$$

$$
\left(\mathbf {b}\right) S _ {e} = S _ {n} + S _ {u} ^ {k},
$$

where k is a modification factor between 0 and 1. k, a subjective factor that is generally evaluated empirically, depends on the complexity of the code. For instance, if the modifications to the code are minor, the value of k is close to 0. If the system requires a thorough understanding, then the value of k is closer to 1.

Choice of a k value and functional form of a model should be based on the ability to capture the intuitive sense of the amount of work required for each project. In addition, it is recommended that the model to be used must minimize the standard error of the estimate $[3]$ . However, in many cases, the size of the data set may not be large enough to support usage of one model form, over the other, and hence it makes sense to use the linear model, in terms of the principle of Occam's razor. Since the telecommunications problem considered at AT&T was of medium complexity, similar to spacecraft projects [3], and C³I projects [26], we chose the linear model. This is consistent with certain previous models derived for NASA spacecraft projects by the Software Engineering Laboratory at the University of Maryland [3] where it was found that computing the effective size in lines was equal to the total number of new lines written plus 20% of any old lines used in the project, and would give rise to a base line relationship of lower standard error. We chose a reasonable value of k to be 0.2, based on the following four basic assumptions:

Table 2  
Project measurements.

<table><tr><td></td><td>Total Lines</td><td>New Lines</td><td>Reused Lines</td><td>Time in Days</td></tr><tr><td>SLP_add</td><td>273</td><td>48</td><td>225</td><td>1</td></tr><tr><td>SLP_upd</td><td>386</td><td>169</td><td>217</td><td>2</td></tr><tr><td>SLPutil</td><td>132</td><td>132</td><td>0</td><td>*</td></tr></table>

\* The time for SLPutil is included in SLP\_add and SLP\_upd.

(a) both the source and target systems were well understood.

(b) the reusable code was not very complicated.

(c) the reusable code was not very large.

(d) the reusable code was well documented.

If these assumptions are not satisfied in other scenarios, then reuse application becomes considerably more complicated.

Two variables were measured in the case project: lines of (unit tested) code (LOC) and time. (See table 2). Equivalent size measures and productivity change measures were used to interpret the data.

Using the linear model and Table 2, the equivalent size measures for each of the two modules is calculated as follows: The Lines of Code for the module “SLP\_util” is equally distributed between the other two modules “SLP\_add” and “SLP\_upd”, since the utilities module was written from scratch in order to adapt the TOPAS1 libraries to the TOPAS2 project. Using the equal distribution, in conjunction with the actual lines of code for each separate module,

$$
\begin{array}{l} S _ {e} = (4 8 + 6 5) + 0. 2 ^ {*} 2 5 = 1 5 8. \\ S _ {e} = (1 6 9 + 6 5) + 0. 2 ^ {*} 2 1 7 = 2 7 7. \end{array}
$$

SLP\_add (1)

SLP \_ upd (2)

This implies that the effort required to develop SLP\_add, and SLP\_upd with new and reused code is equivalent to developing a product of 158 lines, and 277 lines, respectively, from scratch.

As the complexity of the problem increases, i.e. as k moves towards 1 the value of equivalent size measure also increases significantly in both the linear and non-linear models. (See Table 3 for an illustration of the variations performed on SLP\_upd.)

Table 3  
Effect of varying $k$ on $S_{e}$ for linear and non-linear models

<table><tr><td>k</td><td>Linear model</td><td>Non-linear model</td></tr><tr><td>0</td><td>234</td><td>235</td></tr><tr><td>0.2</td><td>277</td><td>237</td></tr><tr><td>0.4</td><td>320</td><td>243</td></tr><tr><td>0.6</td><td>364</td><td>260</td></tr><tr><td>0.8</td><td>409</td><td>308</td></tr><tr><td>1.0</td><td>451</td><td>451</td></tr></table>

Productivity is defined as “Size in terms of the number of lines of source code generated/effort in programmer-month”. In the case, since the size of the program was small, the effort in programmer-month was changed to effort in programmer-days. Note that all the data is for unit tested code. Including system integration and acceptance testing would considerably increase the time needed to complete the project.

SLP\_add was completed in one day. In other words, an equivalent size measure of 158 LOC was completed in one day. Therefore productivity is 158 LOC. If the module were written from scratch, 338 LOC (273 + 65) would be needed. Hence the productivity change for the module is 338/158 which is approximately 2.1 programmer-days.

Similarly, the productivity for SLP\_upd = 277/2 = 138 LOCs and if the code is not reused, then the same module would require $(386 + 65)/138$ , or approximately 4.3 programmer days.

Reuse, on a unit test basis as shown above, has shown significant improvement in the productivity of the prototyped system. (A note of caution however: in order to compute the exact gains in productivity, the time and resources spent in integration testing, acceptance testing and system testing also need to be taken into account. In addition, there is effort involved in writing the associated documents: requirements document, the functional specifications document as well as the high level design, detailed level design, test plan, etc). A well documented code coupled with a good understanding of its functionality will certainly increase the reusability of the code. The increases in productivity are not limited to coding, but also to time saving in the development of the logic of a module, documentation, testing as well as quality, since only well tested modules are reused.

## 4. A reuse support system

The case conducted at AT&T Bell Labs allows us to draw the following specific conclusion (generalization of this conclusion would need a detailed and large scale experimentation): reuse as an inherent aspect of prototyping is clearly important as a means to productivity increases. This is because of the fact that reused code, even if it is retrofitted, saves considerable time in module development and improves the quality of the system. It is also clear that in such a context, knowledge of the existence of reusable code in the development environment and tools to locate them will undoubtedly help promote reusability. Hence it also becomes necessary to consider the development of reusable software in the software development life cycle. In the first part of this section, we suggest a simple yet powerful system to implement a software reusable library. The model is based on the principles of composition technology, and more specifically, draws on and enhances a scheme proposed by Prieto-Diaz and Freeman [24].

## 4.1. A reuse classification scheme

A Reuse Support System (RSS) should be able to find and retrieve components according to given criteria, evaluate the retrieved components according to given constraints, and rank the evaluated components in some order.

In order to find and retrieve components, a classification scheme is required. Each component has to be classified in order to provide easy access by simple query commands like SQL and also provide the flexibility for future enhancements. Two kinds of classification schemes are widely used in practice $[10]$ : the enumerative, a hierarchical scheme, and faceted, a relational scheme. We shall use the faceted scheme here because it is more efficient, widely used in library systems and easily adapts to relational DataBase Management Systems (DBMS). The faceted scheme is based on a standard vocabulary of terms commonly used in the data processing environment to describe a component. Software components can be described in terms of the function or action that is performed, the object on which the function is performed, and the medium where the function is performed.

In a relational database, the three tuple, $\langle$ action, object, medium $\rangle$ is thus sufficient to describe a component. For example, the signaling system contains an object called the Common Language Trunk

Group Identifier (CLTGI). In order to parse the CLTGI, the medium to be used is the field buffer data structure (FBFR). The tuple $\langle$ parse, CLTGI, FBFR $\rangle$ is sufficient to describe the function parseCLTGI, and similarly, $\langle$ delete, LINK, DB $\rangle$ is sufficient to describe a function SLPdel\_link. The three tuple can be extended to a six tuple by including descriptors like TIER, SUBSYSTEM, and SYSTEM (where, for example, System refers to TOPAS, SubSystem refers to Provisioning and/or Maintenance subsystems and Tier refers to support for networks, or distributed processing, etc). Thus a complete tuple may be $\langle$ action, object, medium, tier, subsystem, system $\rangle$ . For instance, Relation1 describes the relationship between the components and its attributes: Relation1(Component, Action, Object, Medium, Tier, Subsystem, System). (A sample listing of the classification scheme is shown below).

Sample software classification scheme for TOPAS

<table><tr><td colspan="7">Relation1</td></tr><tr><td>Component</td><td>Action</td><td>Object</td><td>Medium</td><td>Tier</td><td>Subsystem</td><td>System</td></tr><tr><td>TTA_updlog</td><td>Update</td><td>log_file</td><td>DB</td><td>NST</td><td>TTA</td><td>TOPAS</td></tr><tr><td>parseCLCID</td><td>parse</td><td>CLCID</td><td>FBFR</td><td>NST</td><td>General</td><td>TOPAS</td></tr><tr><td>makeGMCP</td><td>make</td><td>GMCP</td><td>FBFR</td><td>NST</td><td>General</td><td>TOPAS</td></tr><tr><td>EQA4Eget_gmcp</td><td>get</td><td>GMCP</td><td>DB</td><td>EIT4EA</td><td>EQA4E</td><td>TOPAS</td></tr></table>

Another relation to store information regarding the size, location, author etc. of the component can be built as follows: Relation2 (Component, Author, Location, Size). Once the set of relations has been properly defined, the database can be queried or a report can be generated according to the needs of the user. A sample query can be as follows: parse/CLCID/FBFR may print out the component, location and author of the Common Language Circuit Identifier (CLCID) as follows:

<table><tr><td>Component</td><td>Location</td><td>Author</td></tr><tr><td>parseCLCID</td><td>/develop/topas1.0/test/crsrc</td><td>Jill</td></tr></table>

Alternately, a query of the form parse/ \*/ \* may retrieve all the possible options.

The query can be further improved by providing a thesaurus for the query's vocabulary. The system should substitute the descriptor in the query sentence with a synonym from the thesaurus. Thus remove/links/DB and delete/links/DataBase are equivalent. Such multiple representations of components and tractability among the components are important for the user to understand the behavior of the candidate components. A sample thesaurus is provided below.

## Sample Thesaurus

<table><tr><td>Descriptor</td><td>Synonyms</td></tr><tr><td>add</td><td>enter, put, sum</td></tr><tr><td>delete</td><td>remove</td></tr><tr><td>update</td><td>modify, change</td></tr><tr><td>get</td><td>retrieve, read</td></tr><tr><td>parse</td><td>split, break</td></tr><tr><td>check</td><td>exist, present, validate</td></tr></table>

## 4.1.1. Expanded scheme

We propose an expanded scheme to envelope the entire developmental process. The expansion is discussed here in relation to systems development in an organization with several evolving software products. Large projects frequently have more than one requirement. We assume that such projects can be functionally decomposed into a number of core parts. In order to complete the project, each requirement has to be satisfied.

![](/api/attachments/GC4UMHEV/fulltext/images/1f0c4e66b5f0c568c576d5fd33ae0548518f8e5f5211d974a8c5ee1b9fd22677.jpg)  
Project 3  
Fig. 1a. An organization with a number of evolving products.

The architecture of the Reuse Support System can then be described in the form of multiple trees corresponding to the different projects (See Figure 1a), each of which have different versions called generics. In each generic, several requirements can be present. Each requirement (Req) is then decomposed into High Level Design Units (HLDU). Each HLDU is then further decomposed into several Low Level Design Units (LLDU). The LLDUs are finally implemented in code as components (COMP) at the leaf level. These concepts can be applied to reuse at the global level.

The component has its own characteristics as well as the inherited characteristics of its ancestors (See Figure 1b).

For example, a component's characteristics can be described by the term CPattr as a function of the three tuple $\langle$ action, object, medium $\rangle$ . In order to affect reuse on a large scale, all components must be traceable to some requirement via the design units. This can be facilitated by describing the attributes of a component (Cattr) to consist of a four tuple that also includes the characteristics of the requirements (Rattr), the characteristics of the high-level design (Hattr), characteristics of low-level design (Lattr), as well as the original tree-tuple component description (CPattr). An attribute is itself described by a two tuple, consisting of Attribute-Name, and Closeness Factor. Hence Cattr = $\langle$ Rattr, Hattr, Lattr, CPattr $\rangle$ .

In order to find a reusable component, criteria that specify the domain of search are used. For instance, the search process can specify a component in a specific generic. In the cases where the component is not found, the next domain can be searched to see if a similar LLDU (based on a user-specified closeness factor [Conte et. al., 1986]) is available. If the search process still comes up empty, the user-specified closeness factor can be revised to allow larger tolerances. This would involve backtracking up the tree and looking for a closely related LLDU in a different requirement or possibly a different generic. The advantage of this is that if an exactly matched component is not found, then a clue to solving the problem may be available somewhere in the organization. This is important, because, the existing LLDUs and the HLDUs would have already been designed well, before they are incorporated into the tree and would have perhaps considered aspects such as memory management, speed, etc. Such an architecture would result in moving the project much faster toward the top of the learning curve, and implementation becomes easier.

![](/api/attachments/GC4UMHEV/fulltext/images/9346922b26e6f15b4e387149a47b99b1fde2b2bac764165794385e34c6a8b007.jpg)  
Fig. 1b. A simplified software development decomposition process. (An attribute is described as [Attribute, Closeness Factor in range 0–1.0]).

The incorporation of the expanded scheme with the classification scheme discussed previously, would help in the reuse of design, requirements and perhaps even test scripts.

## 4.1.2. Domain analysis

In this subsection, we discuss domain analysis and its application to reuse with respect to the above scheme. “Domain analysis is the process of identifying, collecting, organizing, analyzing and representing a domain of interest based on information available for that domain” [15]. The approach we take here is similar to and draws from the Draco approach [23]. The goal of the Draco approach is to “increase productivity of software specialists in the construction of similar systems”. The domain analysis approach would allow an extension of the Draco approach to increase productivity across similar as well as dissimilar systems. In addition, this approach allows the capture and utilization of information generated during the development process. (This is in contrast to the LaSSIE approach that addresses reuse from the component level and its relationship with software architecture [12]).

Reuse of analysis information is considered the most powerful brand of reuse, and reuse of design information is considered the second most powerful brand of reuse $[23]$ . We follow Neighbors in strongly subscribing to the “analysis of information” concept. Accordingly, one can view the entire development process as a tree, starting from specifications to testing for each project. If a piece of information at any level is reused, it can contribute profitably towards software productivity provided that information is available with minimum effort.

The expanded scheme discussed in the previous subsection, encompasses the software development process from the specifications to the components level. A project can be considered a domain. Processes such as requirements, design, implementation, can be considered to be sub-domains. If a large project exists, then a super-domain can be established. Each sub-project may have more than one domain. If the project management establishes a process such that each leaf, i.e., a component, is related to its parent all the way up to the specification, then the tools of domain analysis $[15,29]$ may be applied. In addition to collecting and classifying' each sub-domain, attributes relating to its ancestors should also be plugged in.

A key concept that can be used in the analysis process is that of tags. Tags are useful in associating pieces of information. If used consistently, one piece of information such as a component can be associated with its ancestor, i.e., the design. If tagged, the information in the design can be used to trace its requirement origination. If all pieces of information are tagged appropriately and consistently, the access to reusable information from any point should be possible. Since a significant problem with reuse is the inability to find the required information, tagging information is one way of making searches faster and more efficient. After gathering domain-specific information $[14,15]$ a list of attributes is developed for the specific domain. Finally, when the database is established tag numbers are associated with each piece of information.

Here we detail a simple example of developing a name and telephone data-base:

Req -> telephone database [tag1.0]

<table><tr><td rowspan="2">HLDU -&gt; object oriented design</td><td>- [tag1.1][update object]</td></tr><tr><td>[tag1.2][retrieve object]</td></tr><tr><td>LLDU -&gt; Add</td><td>[tag1.1.1]</td></tr><tr><td>Update</td><td>[tag1.1.2]</td></tr><tr><td>Delete</td><td>[tag1.1.3]</td></tr><tr><td>Display</td><td>[tag1.2.1] [print,clear]</td></tr><tr><td>Comp -&gt; write_db</td><td>[tag1.1.1.1,tag1.1.2.1,tag1.1.3.1]</td></tr><tr><td>find_db</td><td>[tag1.1.1.1,tag1.1.2.1,tag1.1.3.1,tag1.2.1.1]</td></tr><tr><td>read_db</td><td>[tag1.1.2.1,tag1.1.3.1,tag1.2.1.1]</td></tr></table>

The above example shows that different domains can be classified and represented using tag numbers. These tag numbers in association with appropriate attributes will provide a database of components, their associated design (HLDU, LLDU) and requirements which can be traced to the source.

With this kind of hierarchical tagging more information regarding a particular problem can be obtained. If an exact reusable component is not found or is not desired then its design/algorithm can be obtained from its predecessor. Obtaining design/algorithmic information will lead to reuse of information across dissimilar systems which directly contributes to increase in productivity.

Thus, domain analysis can be applied over the large part of the development process and not just to the components. The goal is to facilitate, expedite, minimize cost without sacrificing quality in the development of the product. In the above example the domain could be the union of Req, HLDU, LLDU and the components. Req, HLDU, LLDU, etc. can be also the sub-domains.

## 4.2. A rule based reuse support system

In addition, to the above system based on concepts of composition technology and domain analysis, principles of generation technology and decision support systems $[4,6]$ can be used to enhance the Reuse Support System. Certain artificial intelligence techniques can be integrated with traditional techniques of data base design and user interface tools for building a meta-language for automatic code generation. Increased knowledge of the existence of code in the development environment and tools to locate them can be incorporated into the system through the use of a hierarchical set of “productions and rules” that deal with modeling knowledge and procedural knowledge. Such knowledge chunks that are incorporated into the knowledge base is reusable under varying conditions. In addition, the use of production rule based systems allows the dynamic selection of knowledge chunks by the inference engine, and can be reused for specific subproblems; of course this reusability is confined to the problem domain that is modeled.

In fact, a production rule based system can be a consulting module, comprising a meta-language for the system developer. The consulting module would contain meta rules of three hierarchical levels: the general, the specific and the highly specific types, ranging from broad and refined to highly refined knowledge. The meta-language can be used to pull out reusable modules from the data base and generate C language code based on the concept of a closeness factor $[10]$ . The factor is based on the similarity between modules and how close the user perceives a module in relation to another module. Closeness is measured on a scale of 0 (absolutely no match) to 1 (identical), in terms of the degree to which a match can be found between the specifications of the reusable code modules, and the code for developing the needed modules. The closeness and similarity concepts could help the system to locate components, assess them for similarity and present them to the user using the rule based consulting module. The reusable modules could either be building blocks which have a high closeness factor to the module that needs to be built, or they could just be skeletons that have a low closeness factor.

Using the format, $\langle$ action, object, medium $\rangle$ and using the rule base, one can write a script to generate the target language where components are retrieved from the Reusable Software Library database and placed appropriately. The meta-language can also be augmented with structured language capabilities.

The above concepts are illustrated below: (For a description of the system specific acronyms used, see the Glossary).

GENERAL RULES:

(Rule 1

IF action IS requested

AND object IS requested

THEN component IS found).

(Rule 2

IF action IS not requested

AND object IS requested

AND medium IS requested

THEN components retrieved may provide ideas about handling the OBJECT).

(Rule 3

IF action IS requested

AND object IS not requested

THEN components may provide ideas about handling ACTIONS).

```lisp
(Rule 4
    IF action IS requested
    AND object IS requested
    AND size of component IS less than 100 new lines of code (ncsl)
    AND number of modifications to this component IS very few
    AND its dependencies are very low
    THEN this is a good and well encapsulated component).

SPECIFIC RULES:

(Rule 5
    IF action IS update
    AND object IS trunk group
    AND medium IS database
    THEN component to update trunk group exists).

(Rule 6
    IF action IS parse
    AND object IS TGID
    AND medium IS don't care
    THEN component to parse trunk group exists).

HIGHLY SPECIFIC RULES:

(Rule 10
    IF (action = validate AND object = CTL_GAP AND depend = none)
    THEN (component = val CTLGAP()))
(Rule 11
    IF (action = validate AND object = fields AND depend = fbfr)
    THEN verFLDS()))

(Rule 12
    IF (action = add AND object = tuple)
    THEN dmadd()))

(Rule 13
    IF (action = dmadd() AND object = TG)
    THEN add _tg()))

(Rule 14
    IF (action = validate AND object = WC_CLLI AND depend = fbfr)
    THEN valWC_CLLI() OR chkWC_CLLI()))

(Rule 15
    IF (action = exist AND object CLCID AND depend = db)
    THEN existCLCID

(Rule 16
    IF (action = parse AND object = CLCID AND depend = fbfr)
    THEN parseCLCID())
```

```txt
(Rule 17
    IF (action = parse AND object = CLTGI AND depend = fbfr)
    THEN parseCLCID() - (0.95))

(Rule 18
    IF (action = validate AND object = AP_CLLI AND depend = no_depend)
    THEN valAPCLLI())

(Rule 19
    IF (action = assign AND object = TG_ACCESSKEY)
    THEN createTGAK())
```

We now apply the meta-language concept to a specific problem: that of adding a link to the system. In the case of TOPAS2, once the data has been collected from the screen, it has to be processed almost the same way as it has to be for trunks. For instance, suppose it is necessary to build a module to add a trunk group to the database (add\_tg\_to\_db). The following methodology can be used.

```txt
<begin add _tg _to _db> ;(*Create the module add _tg _to _db*)  
<validate> AP_CLLI ;(*Validate the field AP_CLLI*)  
<validate> WC_CLLI ;(*Validate the field WC_CLLI*)  
<parse> CLTGI ;(*Split the CLTGI into atomic parts*)  
<exist> TRUNK_GROUP ;(*Does the TG defined by CLTGI exist?*)  
<add tuple> TG_REC ;(*Add a tuple to the relation TG_REC*)  
<add tuple> TG_AP_REC  
<add tuple> TG_PSWL_REC  
<add tuple> TG_GSWL_REC  
<send message> terminal "TRUNK GROUP ADDED"  
end add _tg _to _db
```

Depending on which statement is called, the control moves to the rule base, a portion of which is shown above. The script is then transformed into the C language as follows:

```txt
add _tg _to _db()
{ valAPCLLI();    /*From Rule 18* /
    valWC_CLLI();    /*From Rule 14, chkWC_CLLI() is also available* /
    *****    /*From Rule 17, parse CLTGI is unavailable. The closest match (0.95) is parse-CLCID()*/
    createTGAK();    /*From Rule 19*/
    dmadd();    /*From Rule 12*/
}
```

The functions val and create, etc. are retrieved from the RSS database based on the actions and the associated objects.

One possible alternate tool for implementing the meta-language and building the intelligent reuse support system is Prolog. Development of the intelligent system is particularly easy in Prolog, because the reuse task is declarative in nature. Prolog can also be used to develop complex query systems and can be used to develop a natural language interface effectively.

![](/api/attachments/GC4UMHEV/fulltext/images/f570b8604b25ff3c84dc11ceb89ab48dfe5c1ba04074868117a4115f62919756.jpg)  
Fig. 2. SRCC in the software development process.

## 5. Software reuse support centers

A natural extension to the concept of reusable support systems, is that of a software reuse support center (SRSC). This invaluable source for prototypers could consist of a team of Reuse Engineers, Consultants, and Reuse Library Administrators. As such, the resource center, could be used at different phases in the evolution of a product, or at different points in the system development process (See Figure 2). In addition, the Reuse Resource Center could have links with various areas in the organization or information centers, such as Project Management, Software Development, Systems Engineering, and System Testing (See Figure 3). The responsibilities of the center could be:

(i) Maintain a library of reusable software (Reusable Software Library). Define a classification scheme for accurate cataloging, and maintain in a database with relevant data.

(ii) Provide consulting services on reuse (including design reuse, test-scripts and code reuse), and promote reuse. Seek out potentially reusable modules and make them highly reusable.

![](/api/attachments/GC4UMHEV/fulltext/images/498db04edddd3b69d8d842bc4ffd8a038e1d941490a4603c611133144c62d0e9.jpg)  
Fig. 3. Role of reuse in an organization.

(iii) Certify software components as reusable.

(iv) Develop and enforce standards.

(v) Provide reuse modules on demand. Develop access criteria to accurately retrieve a component.

(vi) Maintain and formalize metrics for evaluating reusable software.

(vii) Encourage programmer creativity in developing reusable software. Programmer support is essential for development of a healthy library.

The Reusable Software Library $[7]$ in the SRRC could have an architecture as detailed in Figure 4. Recent research in reuse support center design has resulted in the development of the “Reusable Ada Products for Information System Development” (RAPID) center at SoftTech Inc, Waltham, Mass $[14,15,25,29]$ . Currently in its pilot phase, the RAPID Center is a software reuse support center for the U.S. Army Information Systems Software Command to provide effective reuse of army software and reduce the cost of system development and maintenance. The kernel of the center is a library system, that is used for cataloging, searching, retrieving and managing reusable software components. The RAPID center uses a classification scheme that is based on the Prieto-Diaz faceted scheme, and contains Ada modules that address business application such as personnel management, logistics, and finance. The identification of reusable software components, within a system and across similar systems is carried out using domain analysis $[15]$ .

![](/api/attachments/GC4UMHEV/fulltext/images/5388141a842591ae2929eae663471cf5cc136d08da89a2688444d18cfe0d43f2.jpg)  
Fig. 4. Functions of an RSL system.

## 6. Discussion

For all its promise, there are some fundamental problems that have to be overcome before reuse can become widespread. The first and primary problem is of finding a representation of reuse information. This in turn calls for the following:

1. The ability to represent knowledge about reuse structures in factored form,

2. The ability to create partial specifications of design information that can be incrementally extended,

3. The ability to allow couplings between instances of reuse and the various interpretations those instances can have, and

4. The ability to express controlled degrees of abstraction and precision (degrees of ambiguity).

This is why it is essential to estimate the costs and benefits of reuse well ahead of time in the development cycle. If reuse involves the usage of building blocks, then it may most often be beneficial to use reusable components. The more complex situation arises when reusable components have to be modified to incorporate them into the product. In such cases, large productivity increases may not be attained. Therefore, it would be useful to conduct a rigorous study at this point to ascertain the utility of reuse. A note of caution, however. It is not enough to compare the costs of searching for and modifying the software, to the costs of producing the code from scratch. The whole system life cycle costs, including the costs of maintenance and verification have to be considered for purposes of cost-benefit analysis. For instance, according to Mitermeir and Rossak [21], through the use of reused components, the cost of software verification can be drastically reduced, since the amount of integration testing needed to mesh the module with the environment can be slashed.

<table><tr><td colspan="2">Glossary</td></tr><tr><td>TOPAS</td><td>Testing, Operations Provisioning and Administration System</td></tr><tr><td>AP_CLLI</td><td>Access Point Common Language Location Identifier</td></tr><tr><td>CLCID</td><td>Common Language Circuit Identifier</td></tr></table>

On the basis of our experience, we outline a few critical factors that are key to the incorporation and success of reuse in the systems development process.

## 1. Evaluate the current methodology:

Without a formal methodology, the process of software development can be a harrowing experience. Ensure that everybody follows the methodology through strict reviews. If metrics exist for the software effectiveness, revisit the software to see if the objectives of productivity and efficiency are addressed.

## 2. Inventory analysis:

Considerable time and money have been spent in developing software for a number of projects. Collect as many modules, test-scripts, and designs as possible and categorize them into broad but similar groups. Substantial duplication may be noted while analyzing the software. Consolidation of similar components can pay off in a big way.

## 3. Documentation:

Good documentation of the software is also a criteria for determining the quality of the software. Ensure that correct and sufficient documentation is available for all the software at hand. If not, take the time to re-document them.

## 4. Standardization:

Once the software inventory is analysed, it is essential to standardize the components. This involves having common interfaces, standard ways of specifying input/output, standard sizes of components, standard quality for each component, standardized documentation processes, etc. Such standardization would establish a good base for establishing a reuse library.

At this point it is necessary to evaluate the current and future needs of the organization and ask questions about (a) the amount of reuse that can be achieved based on the prior analysis conducted, (b) expectations about increase in productivity and quality, (c) how much resource need to be diverted to the process. If the analysis reveals that the process can benefit then reuse must be incorporated into the development methodology.

## 7. Conclusion

This paper has described a case study of reuse in the telecommunications industry and has discussed detailed specifications of a reuse support system based on the concepts of composition technology and generation technology. After a brief discussion of different paradigms of systems development, the paper looks into issues relating to reuse quantification and productivity justification, issues that can improve the quality and the capabilities of the systems development process. A simple yet effective system has been developed using the concepts of building blocks and patterns and domain analysis, and of rule based expert systems and relational databases. The closeness and similarity concepts help the system to locate similar components and present them to the user using the rule based consulting module. The power available to a systems developer in a good relational database and present day query and report generators, as well as the integration with artificial intelligence tools and techniques for intelligent reuse support would allow a substantially value added system.

CPR Circuit Provisioning
CLTGI Common Language Trunk Group Identifier
CTL\_GAP Control Group Area Position
EIT Equipment Interface Tier
EQA4E Equipment Access for 4E
FBFR Fielded Buffer
GMCP Group Member Circuit Pack
LOC Lines of Code
NST Network Support Tier
RSS Reusable Software System
SLP Signaling Link Provisioning
TG Trunk Group
TGAK Trunk Group Access Key
TG\_AP\_REC Trunk Group Access Point Record
TGID Trunk Group Identifier
TG\_REC Trunk Group Record
TTA Trouble Ticket Admission
WC\_CLLI Work Center Common Language Location Identifier
4ESS No.4 Electronic Switching System
5ESS No.5 Electronic Switching System

## Acknowledgments

The authors would like to thank Dennis Felton and Philip Schreiner of AT&T Bell Labs for their comments and encouragement during the reuse project. We are grateful to the TOPAS management at AT&T, New Jersey, for permission to publish details of the case. TOPAS is a trademark of AT&T. Also a special note of thanks to Dr. Ernesto Guerrieri, of Digital Equipment Corporation, Littleton, Mass, and Prof. Larry Sanders of SUNY/Buffalo, as well as the two anonymous referees for detailed criticisms and comments. The authors would also like to thank Prof Andrew Whinston for his encouragement. The second author was supported in part by a Summer Grant from the School of Management, SUNY at Buffalo. The authors' names are in alphabetical order.

## References

[1] M. Alavi, An Assessment of the Prototyping Approach to Information Systems Development, Communications of the ACM, Vol 27 No. 6, June 1984.

[2] D.S. Appleton, Information Asset Management, Datamation, Feb 1, 1986.

[3] J.W. Bailey and V.R. Basisli, A Meta-Model for Software Development Resource Expenditures, 5th International Conference on Software Engineering, San Diego, Ca, March 1981.

[4] T. Biggerstaff and C. Richter, Reusability Framework, Assessment, and Directions, IEEE Software, March 1987.

[5] B.W. Boehm, T.E. Gray, T. Seewaldt, Prototyping Versus Specifying: A Multiproject Experiment, IEEE Transactions on Software Engineering, May 1984.

[6] R. Bonczek, C. Holsapple, and A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York, 1981.  
[7] A.B. Burton et. al. The Reusable Software Library, IEEE Software, July 1987.

[8] R.P. Cerveny, E.J. Garrity, and G.L. Sanders, The Application of Prototyping to Systems Development: A Rationale and a Model, Journal of Management Information Systems, Vol 3 No 2 Fall 1986.

[9] J. Connell, and L. Brice, Rapid Prototyping, Datamation, August 15, 1984.

[10] S.D. Conte, H.E. Dunsmore, V.Y. Shen Software Engineering Metrics and Models, 1986, Benjamin Cummins Publishing.

[11] A.R. Dennis, R.N. Burns, and R.B. Gallupe, Phased Design: A Mixed Methodology For Application System Development, Data Base, Summer 1987.

[12] P. Devanbu, R.J. Brachman, P.G. Selfridge, and B.W. Ballard, "LaSSIE: A Knowledge-Based Software Information System, Communications of the ACM, May 1991, pp 34–50.

[13] A. Gargaro and T.L. Papas, Reusability Issues and Ada, IEEE Software, July 1987.

[14] E. Guerrieri, Searching for Reusable Software Components with the RAPID Center Library System, Proceedings of the 6th National Conference on Ada Technology, Alexandria, Va, March, 1988.

[15] E. Guerrieri, Tools for Domain Analysis, Proceedings of the 3rd Annual Workshop on Methods and Tools for Reuse, Syracuse, New York, 1990.

[16] E. Horowitz and J.B. Munso, An Expansive View of Reusable Software, IEEE Transactions on Software Engineering, Vol SE 10, No. 5, Sept 1984.

[17] Karimi, J., An Asset-Based Systems Development Approach to Software Reusability, MIS Quarterly, June 1990.

[18] K. Laudon K. and J. Laudon, Management Information Systems: A Contemporary Perspective, MacMillan Publishing, 1988.

[19] M. Lenz, H.A. Schmid, P.F. Wolf, Software Reuse through Building blocks, IEEE Software, July 1987.

[20] Luqui, V. Berzins, and R.T. Yeh, A Prototyping Language for Real-Time Software, IEEE Transactions on Software Engineering, Vol 14. No 10, October, 1988.

[21] R.T. Mittermeir and W. Rossak, W., Reusability, Modern Software Engineering: Frontiers and Current Perspectives, ed., Peter A. Ng and Raymond T. Yeh, Von Nostrand, New York, 1990.

[22] J.D. Naumann, A.M. Jenkins, Prototyping: The New Paradigm for Systems Development, MIS Quarterly, Vol 6, No. 3, September 1982.

[23] J.M. Neighbors, The Draco Approach to Constructing Software from Reusable Components, IEEE Transactions on Software Engineering, vol SE-10, No 5, May 1984, pg 564–574.

[24] R. Prieto-Diaz and P. Freeman, Classifying Software for Reusability, IEEE Software, January 1987.

[25] T.B. Ruegsegger and E. Guerrieri, The Rapid Center Library as a Case Tool, CASEexpo, Washington D.C., Spring 1989.

[26] H.P. Schultz, Software Management Metrics, Technical Report ESD-TR-88-001, Mitre Corporation, Mass, 1988.

[27] T.A. Standish, An Essay on Software Reuse, IEEE Transactions on Software Engineering, Vol SE 10, No. 5, September 1984.

[28] M.E. Swanson, and S.K. Curry, Results of an Asset Engineering Program, Information and Management, 16, 1989.

[29] W. Vitaletti and E. Guerrieri, Domain Analysis within the ISEC RAPID Center, Proceedings of the 8th Annual Conference on Ada Technology, Atlanta, Ga, March, 1990.

[30] P. Wegner, Capital Intensive Software Technology, IEEE Software, July 1984.

[31] L.G. Williams, Overview of the Workshop on Software Reuse, Workshop on Software Reuse, Boulder, Colorado, Oct 1987.

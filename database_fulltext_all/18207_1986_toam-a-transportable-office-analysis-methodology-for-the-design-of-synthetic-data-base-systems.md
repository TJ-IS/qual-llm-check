---
otero_id: 18207
otero_key: "RDUW6YDR"
title: "TOAM: A transportable office analysis methodology for the design of synthetic data base systems"
authors: "Dario Maio; Corrado Costa; Roberto Gallerani"
year: "1986"
journal: "Information & Management"
doi: "10.1016/0378-7206(86)90008-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# TOAM: A Transportable Office Analysis Methodology for the Design of Synthetic Data base Systems

Dario Maio

DEIS, University of Bologna, Viale Risorgimento 2, 40136 Bologna, Italy

and

Corrado Costa and Roberto Gallerani
PERSEO S.p.A., Centergross, Blocco 2A, Gall. B., n. 147, 40050 Funo di Argelato (Bologna), Italy

Recent years have shown increased development of methodological approaches to information system design. One approach to office automation is to attempt to define the information processed in the office and how it moves. This is a complex task and should ideally be supported by PC applications. This paper describes a set of forms and coded descriptions for collecting the data about the office under study. These forms are intended to assist the task of transferring the information to a PC data base (dBASEII). The use of the forms is illustrated by an example from garments industry. The methodology is directed at small to medium-sized industries in which office automation must be integrated with traditional information systems.

Keywords: Office Automation, System Analysis and Design, Methodology, Conceptual Modeling, Database Design, Documentation.

## 1. Introduction

Office information system (OIS) design is now emerging as an important area of research both in the academic and industrial world; the main goals are to define office models, to determine workable

![](/api/attachments/RDUW6YDR/fulltext/images/12dacddfa9a279d204b476f24e4d6e97e5c520739122ddfa5a3b19f335066276.jpg)

Dario Maio is assistant professor at the Computer Science Department, University of Bologna, Italy. He has published in the fields of distributed computing systems, computer performance evaluation, data base design and office information systems. Before joining the Computer Science Department, he received a fellowship from the Italian National Council of Research for the participation to the Air Traffic Control project. He received a degree in electronic engineering from the University of Bologna in 1975.

![](/api/attachments/RDUW6YDR/fulltext/images/7ab973d29076e5b0625e0ef7b3e09646c8fcc44d7a5682832ba4b1f2b9fe538f.jpg)

Corrado Costa is a founding member of the Perseo Co., Bologna, Italy. He is actively involved in consulting and research in office information systems. He was with the Hewlett Packard Company, Milano, Italy, for almost 5 years, with the responsibility for information system design and implementation. He received a degree in electronic engineering from the University of Bologna in 1970.

![](/api/attachments/RDUW6YDR/fulltext/images/f7c7290304a499941caa6e5a6c6f0c615643a63714d1087b397d2e061ed3d3b5.jpg)

Roberto Gallerani received a degree in electronic engineering from the University of Bologna in 1984. His current research interests at Perseo Co., Bologna, Italy are directed toward the areas of office automation, communication networks and decision support systems.

methodologies, and to develop automated tools to provide practical guidance to the designer in making decisions and trade-offs $[1,2,7,8,9,11,12,13]$ . Papers $[4,5]$ provide a review of existing methodologies and tools for OIS conceptual design, stressing their characteristics and original features. Research in conceptual modeling of office environments is now looking at the use of expert systems and knowledge-based natural languages.

However, in spite of the research, potential users are skeptical. Office automation projects disappoint users. Probably methodologies and modeling take a long time and need large investments, before the objectives are close to being reached. Possibly, available commercial office equipment is too specific for individual needs and falls short of resolving semistructured activities. In many organizations, integrating existing data bases with new office tools for decision-making is difficult. Today, the success of a design methodology depends, in large measure, on the ability easily and precisely to describe the most important office tasks that must be performed while allowing the gradual increase in the user participation and contribution.

Recently the Computer Science Department of the University of Bologna participated in the Informatica DATAID Project supported by the Italian National Council of Research. This project involved the development of a complete database design methodology aided by a set of automated tools $[1,6]$ . In particular a physical design tool for relational DBMSs was developed $[3,10]$ ; experience was acquired in methodologies and techniques to be used in conducting cost benefit analyses and evaluating computer effectiveness. This paper discusses the combination of these research contributions with practical experience of the Perseo S.P.A. in developing office automation plans. TOAM, a simple requirement collection methodology, is the fruit of some studies carried out in a medium-sized clothing industry, where the ultimate objective is the development of a data base able to provide a decision support for managers in performing semistructured activities. The user requirements are stored in dBASE II relations; a set of queries is available to the office automation group to facilitate the design process.

## 2. A User Friendly Conceptual Analysis of Office Databases

The methodology presented here is not a general solution to the analysis of office activities in a medium-sized industry. Different organizations will, of course, need different solutions, but we suggest similar approach in all cases where brief analysis of the office activities is required by the users in order to experiment in office automation. For positive short term results it is necessary to involve the managers of the entire organization in the project development, even if the early stage requires gross approximations and tends to lose sight of some important needs.

In the past, many organizations have invested in computer equipment. However, their information systems are not adequate to provide guidance in making good decisions, because the relevant data are stored in too much detail. Often managers operate with a little data manually extracted from computer-generated reports, after running long time-consuming programs which access very large data bases. In this case, managers already familiar with personal – computer office products are frustrated by their forced dependence on EDP personnel and by the absence of rapid consultation services. Similar arguments may be made for those structured activities which require the preparation of documents composed by text, images, graphs and synthetic data. Again commercial products for this purpose require a closed system architecture which provides an insufficient integration with previous implemented information systems on different computers often from different manufactures. Preserving past investments implies a complex design task.

## 2.1. The General Framework of TOAM

The methodological approach proposed here excludes the initial phase in which a policy is defined by top management. The organizational context is identified and an office automation study group is commissioned with the following tasks:

A) Describe the organization in terms of its relevant functions.

B) Identify the office area chosen as the target office.

C) Collect requirements of this office and the offices intimately related to this one utilizing interview forms.

D) Store collected requirements into a data base on a personal computer for subsequent requirement analyses.

E) Obtain a formal description and graphic representation of the information flows and of data, documents, and operational schema.

F) Perform a logical design of a data base for the target office. This represents a kernel for future expansions to other offices.

G) Contact EDP personnel to investigate possible ways of solutions for integrating with current information systems and to forecast other needs.

H) Make a physical design of the hardware and software architectures.

I) Implement a prototype and evaluate its operation.

Note that this process may be varied. It is a method that allows steps to be performed with some degree of parallelism and it may involve iterations. For example, the analysis of the stored requirements during step D may overlap the interview process and may lead to additional meetings with the office personnel in order to remove inaccuracies and inconsistencies. In the following, the description of the steps of logical and physical design is omitted. Details regarding the various data base design phases may be found in the DATAID methodology $[1,6,10]$ .

## 2.2. Collecting office requirements

Steps A and B refer to the initial meetings with the office managers. After describing the entire organization in terms of their basic mission and macro-functions, the analyst should seek to uncover a critical office area to be chosen as the initial target. This office must have all the necessary qualifications to make the study a success and be a first step towards an integrated office system. In particular the following features are required:

\- strong motivation for the office automation;

– existence of a number of connections with other offices in terms of communications and interrelationships;

\- generality of decision-making problems;

\- possibility of arousing interest in other part of the organization.

We now introduce some definitions used in the interview forms of step C.

TASK: the generalization of a function, procedure, activity, meeting or some combination of these.

FUNCTION: a process which receives inputs, produces outputs and cooperates with other processes by synchronization and information interchange. It assumes decisions and creative aspects, rather than merely structured activities.

PROCEDURE: like a function, except that operative aspects predominate.

![](/api/attachments/RDUW6YDR/fulltext/images/6fd2f11694c3a381858f381df422c9cb9b7ac36cd39954d928adc65a2954507c.jpg)  
Fig. 1. Example of a task identifiers tree.

ACTIVITY: a set of structured steps, expressed using sequential pseudo-code based languages, i.e. parallelism is allowed between activities.

MEETING: a special function that represents a time to review and correct conclusions from single offices.

A top-down approach implies, first, task definition and then identification of the functions, procedures, etc. Moreover a function may include procedures and vice versa.

It must be pointed out that the header of each TOAM form (figs. 2–7) is the same; it records:

\- the phase of the project;

\- the name of the project;

\- the form type;

\- the page number,

Because tasks may be viewed as hierarchically ordered, each task T is uniquely determined by the 3-tuple (LN, TSN, LTN) where: LN is the level number to which T belongs; TSN is the task sequence from the root to T; LTN is the task number within its level.

An example is given in Fig. 1. The page number contains the task identifier (LN, TSN, LTN)

![](/api/attachments/RDUW6YDR/fulltext/images/d4c183cb0c4c69935c822dd1c16ef86bdff8175a5a6eb6fdb242bed587d87bc6.jpg)  
Fig. 2. Legenda of the information exchanged between offices.

![](/api/attachments/RDUW6YDR/fulltext/images/257174040202feae44238cf30178b06a54f846050500d21cfd85905d32681cb8.jpg)

and an internal page number IPN. This is very similar to that used in the MAPS methodology [12].

## 2.3. Legenda Forms

During the requirement collection phase, legenda are collected. Fig. 2 gives an example for some of these information types. Other refer to the office department abbreviations, temporal symbols, common abbreviations, etc.

## 2.4. Task Header

Fig. 3 shows an example of the task header form. Task 3022, named PROJECTION PROCESSING and at the third level of the task tree, is performed by the four offices ORG, SAD, MAC and TOM after they receive sales projections from the top management. During the initial interview the only available information is the general idea that PROJECTION PROCESSING is a function and it is made up of subtasks. Other information

COMMENTS:

TASK NAME

![](/api/attachments/RDUW6YDR/fulltext/images/895f650437c428911c8f37c3e006305349624abeb5e9f385199ce0f1a8189077.jpg)

TYPE f

![](/api/attachments/RDUW6YDR/fulltext/images/2059953d524dcbda0f80ad226effa544090b5d5c7979099d17e7f42b3f59c434.jpg)

TIME CONSTRAINTS:

<table><tr><td></td><td>MIN</td><td>MAX</td><td>EXPECTED</td><td>UNIT</td><td>FOR</td></tr><tr><td>DURATION</td><td>5</td><td>7</td><td>5</td><td>m</td><td></td></tr><tr><td>FREQUENCY</td><td>1</td><td>1</td><td>1</td><td>t/s</td><td></td></tr></table>

Fig. 3. Task header form.

refers to the time constraints: duration and frequency (m is month, s is season, t is number of times). At this level of investigation, it is possible to hypothesize the type of the various subtasks. In particular, the analyst discovers that ORG, SAD and MAC each make a projection processing (with time constraints and interactions unknown) and learns that TOM coordinates these subtasks by holding periodic meetings. The top-down approach now suggests an inquiry into the various subtasks, in order to make a complete description of the task. For simplicity, we describe subtask 40221, which is a procedure without parallel activities.

## 2.5. Inputs to the Task

Fig. 4 is an example of the form for inputs to a task. PROJECTION PROCESSING\_ORG is a child of the task 3022 and it belongs to the ORG office. The form provides the following data:

![](/api/attachments/RDUW6YDR/fulltext/images/5f2e2cb43fe8c9052f384271a7257cd3d72941373ed052757361c940799657cd.jpg)

<table><tr><td colspan="4">INPUT</td></tr><tr><td>TYPE_USE</td><td>NAME HOW</td><td>FROM OFFICES</td><td>EMPLOYEE</td></tr><tr><td colspan="4">#1: macroprevision data on the sales for the next season, subdivided into collection, clothes types and market</td></tr><tr><td>DOC_EL</td><td></td><td>TOM</td><td>Smith</td></tr><tr><td colspan="4">#2: presentation terms of each collection of samples</td></tr><tr><td>DOC_EL</td><td></td><td>TOM</td><td>Smith</td></tr><tr><td colspan="4">#3: terms of clothes delivery to the retail shops subdivided into collection and market</td></tr><tr><td>DOC</td><td></td><td>TOM</td><td>Smith</td></tr><tr><td colspan="4">#4: composition of collection of samples and production modalities</td></tr><tr><td>DOC</td><td></td><td>TOM</td><td>Smith</td></tr><tr><td colspan="4">#5: historic data:clothes sold in the previous analogous season, subdivided into delivery, collection and types</td></tr><tr><td>LIS.DOS</td><td>LISxxx.PROGxxx(PR)</td><td>ORG(R)</td><td>JONES</td></tr></table>

Fig. 4. Inputs to the task.

<INPUT>: a short description of the data received; <TYPE>\_<USE>: the kind of input (among those listed in fig. 2) and its value. For example, input #5 is taken from a dossier and input #1 is a document whose content must be processed before entering the task body (with a qualifier EL).

$\langle \mathrm{NAME}\rangle_{-}\langle \mathrm{HOW}\rangle$ : gives the input name, if one exists, and its derivation when the person interviewed knows it. A qualifier may be appended in order to describe the method of production of the data. Input #5 is known within ORG as LISXXX, a listing produced by running the program PROGXXX on the host computer, as summarized in the qualifier PR.

〈FROM OFFICES〉: the offices which provide the input to the task and, if necessary, a qualifier giving the operation performed by the supplying office. (R) qualifier in the input #5 indicates that LISXXX is extracted from a local dossier by the same ORG office.

![](/api/attachments/RDUW6YDR/fulltext/images/542525d51c2ba8dc97a53c00aee18679366ca5c3354900661b762cbefa9bedfc.jpg)

![](/api/attachments/RDUW6YDR/fulltext/images/c14cf652994d8d3f98b6f954f2bb36f5ce0fc014a488bf8b17a8c1a07efc2063.jpg)  
Fig. 5. Outputs from the task.

〈EMPLOYEE〉: gives the name of the personnel supplying the input.

## 2.6. Outputs from the Task

Fig. 5 shows the outputs of task 40221. The syntax is similar to that introduced in the last subsection. For instance, output #1 is a listing plus an office communication, produced by VISICALC facilities on a personal computer and sent to various offices. Furthermore, output #1 is sent to BROWN (office PRD) and to other offices for information purposes (KN qualifier). As a result, ORG inserts (I qualifier) the output #1 on local mass storage on a personal computer. Ambiguities and exceptions in this kind of representation may be resolved only by performing subsequent interviews and more detailed analysis.

![](/api/attachments/RDUW6YDR/fulltext/images/491848134d98a44d42dbdedbace3783f066aeaf2a9226e3be2f3d7e4007458e8.jpg)

```txt
TASK BODY + LOCAL INFORMATION
P1. input handling;
P2. for each collection aggregate the market sale previsions;
P3. on the basis of the historic data (subdivided into delivery) hypothesize distribution of the sale previsions;
P4. operate qualitative evaluation in order to hypothesize the clothes re-enter terms.
```  
Fig. 6. Task body.

## 2.7. Task Body

Fig. 6 describes, together with comments, the PROJECTION PROCESSING\_ORG task body. Obviously, in the case of more complicated tasks, including parallelism between various activities, other types of task description must be used, but not at the preliminary analysis. PETRI nets or specification languages may support this.

## 2.8. Task Resources

Fig. 7 reports the personnel involved in performing the task, the equipment used, and those office services (e.g. secretarial staff, internal EDP center, etc.) which carry out an active role.

## 2.9. Tools for the Requirement Collection and Conceptual Design of Office Databases

During the requirement collection, the analyst should be provided with a set of automated tools:

TASK NAME

![](/api/attachments/RDUW6YDR/fulltext/images/41318e5b067dd668634fd61846e4260452878d5a41186b10360d43f3e68e55db.jpg)  
Fig. 7. Task resources.

a) to produce adequate documentation of the data and to examine its consistency:

b) to transform the heterogeneous description into a homogeneous form in the conceptual model used.

The latter depends on the conceptual schemata used for the design of office data bases. The DATAID methodology assumes an entity relationship model and provides automatic tools to support the designer in expressing static and dynamic aspects [1,6]. Step D is typical of TOAM; it has other aspects than the DATAID methodology (office communications, semistructured activities, document processing, etc.).

TOAM has two advantages. First, a graphic package developed on the HP150 personal computer allows one to produce documentation of the requirements. At present, we believe an “on-line” use of a graphic package during the requirement collection would affect the person interviewed, and would have hardware and software limitations. On the other hand, the analyst is obliged to produce interview results through well-structured forms. All the figures in this paper were obtained by using this graphic package.

![](/api/attachments/RDUW6YDR/fulltext/images/a43fdb7b22ddcb445f22746738852830b0bd1a36c0e2eb18582db309a4d16208.jpg)

![](/api/attachments/RDUW6YDR/fulltext/images/20b4fcb1055bd93c0beeeb5d44fa0b4fc5f54b9504af12ca95f31a484cbc794c.jpg)  
Fig. 8. Document and information flow for the task 40221.

The second advantage is the possibility of storing the requirements in a transportable relational data base. The transfer of the inputs to dBASE II is still manual; moreover, non-automated checking is provided to build a consistent database. The apparent discrepancy between the form structure (hierarchical) and the data base architecture (relational) exists for two reasons: first, the forms must satisfy interview needs; secondly dBASE II offers transportability.

A set of dBASEII programs has been built in order to simplify the requirement analysis. Some of the queries are:

Q1) for a given task find:

\- its children;

\- its ancestors.

Q2) for a given level number, find all the tasks at this level.

Q3) for a given task find:

\- the offices which perform the task,

\- the inputs to the task, indicating the employees which provide them, and the originating tasks.

Q4) for a given task find:

\- the offices which perform the task,

\- the outputs from the task, indicating the employees which receive them, and the destination tasks.

Q5) for a given office, find all its tasks, and for each task solve Q3.

Q6) for a given office, find all its tasks and for each task solve Q4.

These queries provide help in building schema representing task nesting levels, and guidance to the analyst for the construction of functional “spiders” which express the interrelationships between tasks [12]. During the analysis, Q3 and Q4 may not give any destination or source data. This shows what is missing. Other queries provide material on office resource utilization, the use frequency of use of a given piece data, etc.

In conclusion, we illustrate one of the graphic outputs. An automated tool for producing this is being designed. Fig. 8 shows the document and information flow for the task PROJECTION PROCESSING\_ORG together with a short graphic legenda. Names enclosed in the ions are those present in the glossaries and correspond to those in figs. 4 and 5 (not in the same order). The representation of fig. 8 must be extended with a short description of the task body and an exhaustive legenda, then showed to the persons interviewed to verify accuracy of the analysis.

## 3. A Case Study

Recently, we had the opportunity of applying TOAM methodology in a company in the clothing industry. There, a HP3000-based architecture with about 30 terminals is devoted to supporting the usual activities, such as accounting, stockage, production management, etc. Orders collected by the salesmen are sent from portable intelligent terminals to the host computer via a concentrator or MARK3 network service. Some offices use personal computers to perform planning activities; they are supported by typical software packages, such as VISICALC, but this task is not integrated with the database.

We start the project by scheduling conference tutorials on office automation trends, tools, and architecture, and collecting questionnaires filled in by managers and office personnel. After meetings with top management, the following are accomplished:

1) specification of the existing information system, which must be saved and integrated with the new technologies;

2) choice of the target office to act as a prototype with gradual restructuring of its activities;

3) development of a synthetic data base for the target office in such a way that it represents a kernel for future expansions towards other activities;

4) a gradual parallel introduction of personal computers and tools in the other offices must be scheduled in order to cover some semi-structured activities, such as the preparation of documents composed by text, image, graphics, etc.

At present steps A to H of the TOAM general framework have already been completed. We are now starting with the implementation phase (I). The proposed architecture provides for a centralized data base (CSDB), which is shared between various offices. As illustrated in fig. 9 a centralized data base management system will allow interrogations from terminals and HP150 personal computers supporting local data bases (LDB). For these, simple data retrieval and transfer facilities (transparent to the user) are to be designed to integrate data with available products at the workstations. To this end, a set of software tools must be provided to manage this data base hierarchy. At the greatest level of detail, we maintain the old existing files on the host computers in a HP IMAGE database structure. At the intermediate level, we “feed” a shared data base, which records historic data and all information which may be useful to the various office activities. At the office level local DBMSs support various decisional activities and allow local views of CSDB for individual needs. The following design steps must be performed:

![](/api/attachments/RDUW6YDR/fulltext/images/f65e9263713e6a13c3f1b03865495ec654a1873a381398d4a8ce521d3e40f00b.jpg)  
Fig. 9. Proposed architecture.

\- choose a strategy for capturing the data and filtering (DCS) the data;

\- design local host software interfaces (LHI) for CSDB to LDB data communication;

\- choose standards both for LDBMS and CSDBMS in order to facilitate integration and future expansion;

\- design personal computer application interfaces (PCAI) to allow for the use of data in commercial products such as VISICALC, LOTUS or in ad hoc local applications.

As a first experimental prototype, we are evaluating the possibility of implementing the CSDB for the target office on the host computer

Expanding the office data base to the other offices will probably involve the installation of another HP3000 computer connected with the previous one. To this end we are investigating the ADVANCENET and MSNET HP communication facilities in order to allow local data distribution and interchange between the various offices. A parallel project is devoted to satisfying the documentation preparation requirements: we are designing an architecture which utilizes an image acquisition workstation connected to the host computer. Here Hp software is available to integrate text, data, and images and produce office documents on laser printers.

## 4. Conclusions

We have presented a methodology which is primarily addressed to the design of office data bases, it allows for the gradual increase in user participation. We have intentionally avoided giving a detailed description of the various conceptual, logical, and physical design steps, preferring to focus attention on the important question of integrating actual information systems with the emergent office technology. We are conscious of the TOAM boundaries as well as the practical aspects and therefore believe that TOAM, even though it makes gross simplifications in conducting the office requirements analysis, may answer the problem of quickly providing decision support to the office managers in performing semistructured activities.

## References

[1] Albano A. and De Antonellis V., Ed. Computer Aided Data base Design. North Holland, Amsterdam, 1985.

[2] Bailey A., Gerlach J., Mcafee P. and Whinston A., An OIS model for internal accounting control evaluation. ACM Trans. Office Inf. Syst. 1, 1 (Jan. 1983), 25–44.

[3] Bonanno R., Maio D. and Tiberio P. an approximation algorithm for secondary index in relational database physical design. The Computer Journal, vol. 28, 4, (1985).

[4] Bracchi G. and Pernici B. The Design Requirements of Office Systems. ACM Trans. Office Inf. Syst., 2, 2 (April 1984), 151–170.

[5] Barbic F. et al. Modeling and integrating procedures in office information systems design. Information Systems, 10, 2 (1985), 149–168.

[6] Ceri S., Ed. Methodology and Tools for Data Base Design. North Holland, Amsterdam, 1983.

[7] Cook C. Streamlining office procedures- an analysis using the information control net model. In Proc. AFIPS National Computer Conference. (May 1980), 555–565.

[8] Hammer M. and Kunin J.S. Design Principles of an office specification language. In Proc. AFIPS National Computer Conference (May 1980), 541–547.

[9] Lum V., Choy D. and Shu N. OPAS: an office procedure automation system. IBM Syst. J., 21, 3 (1982), 327–350.

[10] Maio D., Sartori C. and Scalas M.R. Architecture of a physical design tool for relational DBMSs, in Albano A. and De Antonellis Ed. Computer Aided Data Base Design, North-Holland, Amsterdam, 1985.

[11] Panko R.R. 38 Offices: analyzing needs in individual offices. ACM Trans. Office Inf. Syst., 2, 3, (July 1984), 226–234.

[12] Santoni M. and Zecchini A. A methodology for the analysis of office work. In Proc. Italian Computing Association annual congress (Pavia, Sept. 1981) 173–180.

[13] Sirbu M., Schoichet S., Kunin J.S., Hammer M.M. and Sutherland J. OAM: an office analysis methodology. Behaviour and Information Technology, 3, 1, (1984), 25–39.

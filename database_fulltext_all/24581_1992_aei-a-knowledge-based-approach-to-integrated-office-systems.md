---
otero_id: 24581
otero_key: "8TR5EK6S"
title: "AEI: A Knowledge-Based Approach to Integrated Office Systems"
authors: "Chandra S. Amaravadi; Olivia R. Liu Sheng; Joey F. George; Jay F. Nunamaker"
year: "1992"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1992.11517951"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# AEI: A Knowledge-Based Approach to Integrated Office Systems

Chandra S. Amaravadi, Olivia R. Liu Sheng, Joey F. George & Jay F. Nunamaker Jr.

To cite this article: Chandra S. Amaravadi, Olivia R. Liu Sheng, Joey F. George & Jay F. Nunamaker Jr. (1992) AEI: A Knowledge-Based Approach to Integrated Office Systems, Journal of Management Information Systems, 9:1, 133-163, DOI: 10.1080/07421222.1992.11517951

To link to this article: http://dx.doi.org/10.1080/07421222.1992.11517951

![](/api/attachments/8TR5EK6S/fulltext/images/e222bae748c56e3123feae6e93835a8cf73460f1b74913db606c9ca059f6798f.jpg)

Published online: 16 Dec 2015.

![](/api/attachments/8TR5EK6S/fulltext/images/706f05776ab7bc8948fa3346946a06ad0bb90ecd4a422fbf8ad1ef890704fa35.jpg)

Submit your article to this journal ↗

![](/api/attachments/8TR5EK6S/fulltext/images/2f0155a65e68a53614de24a1c22cabd4571c655925b437bb371e012a54a3927f.jpg)

View related articles ↗

# AEI: A Knowledge-Based Approach to Integrated Office Systems

CHANDRA S. AMARAVADI, OLIVIA R. LIU SHENG, JOEY F. GEORGE, AND JAY F. NUNAMAKER, JR.

CHANDRA S. AMARAVADI received his doctoral degree in MIS from the University of Arizona in 1989. He is currently an assistant professor at Western Illinois University. His primary research interests are in the issues surrounding the design and development of intelligent office systems, including office analyses, knowledge representation, semantic data models, document and image databases, user interfaces, hypertext, and executive support systems.

OLIVIA R. LIU SHENG received her M.S. and Ph.D. in computers and information systems from the University of Rochester in 1983 and 1986. She has been an Assistant Professor of MIS at the University of Arizona since 1985. She has been the instigator of several research grants from the U.S. Army, NSF, and Toshiba and has published in such journals as Communications of ACM, Journal of Management Information Systems, Performance Evaluation, Information Systems and Operational Research, Data Base, and Journal of Database Administration, as well as in numerous conference proceedings. She served as a chairperson of several conference sessions and presented research results and tutorial lectures. Her current research interests include computer aided systems analysis and design, computer-mediated communication support, distributed group work, and integrated office systems.

JOEY F. GEORGE is an Assistant Professor of MIS at the University of Arizona. He earned his A.B. degree in English from Stanford University in 1979 and his Ph.D. in management at the University of California at Irvine in 1986. His research interests focus on how information systems affect people's jobs. Specific topics he is currently researching include the effects of group decision support system (GDSS) use on the group work process and its outcomes, GDSS use in non-American cultures, the effects of computing on decision authority in organizations, and the effects of extensive computerization in work groups.

JAY F. NUNAMAKER, JR., is head of the Department of MIS and is a Professor of MIS and Computer Science at the University of Arizona. He received a Ph.D. from Case Institute of Technology in systems engineering and operations research. He was an Associate Professor of Computer Science and Industrial Administration at Purdue University. Dr. Nunamaker joined the faculty of the University of Arizona in 1974 to

Acknowledgment: The authors wish to express their thanks to the Army, Major Ted Hengst (formerly Capt. Ted Hengst of AIRMICS), and Division Chief Jim Gant of AIRMICS for their support and cooperation in this project. The authors wish to thank the anonymous reviewers of this paper for their comments and criticisms which led to this improved version. This research was partially funded by the U.S. Army under contract no. DAKF-11-88-C-0021.

develop the MIS program. Author of more than forty papers on group decision support systems, the automation of software construction, performance evaluation of computer systems, and decision support systems for systems analysis and design, he has lectured throughout Europe (including Russia), Asia, and South America. Dr. Nunamaker is chairman of the Association for Computing Machinery (ACM) Curriculum Committee on Information Systems.

ABSTRACT: Although various attempts have been made in the past to introduce office systems and office models, they have been limited in one or several ways: they have not been based on integrated views; no models were developed or the models were artificial; they have been limited in scope; they used restrictive representation schemes; they were not intelligent; they were not user-friendly. Our research attempts to address these issues with: an integrated view of the office; a model tied to the nature of office activity; integration across various office domains; and a knowledge base. Intelligence is supplied from the interface and from the planner, as well as from the domain knowledge. An important component of the domain knowledge is the functional structure which captures activity relationships with a uniform representation scheme. Users can access explanations about functions of the office and can add comments on them. The realization of these concepts in a prototype system is discussed.

KEY WORDS AND PHRASES: integrated office systems, intelligent office systems, knowledge-based office systems, office knowledge representation, office models, office system architectures.

## 1. Introduction

OVER THE LAST DECADE OR SO, researchers have taken several steps in the direction of the automated office. Some have been exploratory while others have been more extensive. It is convenient to discuss these attempts in terms of views, models, specification languages, and systems (see Table 1) as they are an indication of the comprehensiveness of the effort; there is a progression of effort from view to system.

A view is a perspective of the office that leads to the development of a particular type of model. There are a number of well-known views of offices such as forms, data, information, and the like. These have been discussed in $[3, 8, 11, 18]$ . For the benefit of the reader, these are summarized in the appendix. Depending on the view of the office taken, models are developed. These views have directly or indirectly resulted from office studies $[19, 23, 32, 33, 34, 36, 37, 47, 48, 49]$ . An integrated view of the office, if carried through to the step of implementation, will ensure that the system will fulfill needs of all office workers. From Table 1 it is evident that there are no models or systems that meet this requirement.

A model is an abstracted representation of reality. Corresponding to the views, there are several types of models, such as procedural, data, and so on. While there are a number of desirable features of models (such as abstraction and aggregation mechanisms), we consider the scope of model, its applicability, and its intelligibility $[11]$ to be the baseline requirements. Scope refers to the breadth of the model, while applicability refers to the type of office. The model (and submodels, if any) must be capable of representing the general type of office in its entirety. The requirement of intelligibility is an important consideration since users must also participate in the development/evolution process of the system. Researchers have often made various trade-offs in developing systems as a result of which some have skipped this phase altogether (again, see Table 1). For example, no models have been developed for Omega [5, 6] and Cokes [27]. Since there are no attempts originating with integrated views of offices, there are no integrated office models.

Table 1 Dimensions of Research in Office Systems

<table><tr><td>Model/System</td><td>View</td><td>Model</td><td>Architecture Described?</td><td>Specification Language</td><td>System</td></tr><tr><td>Scoops [51]</td><td>Procedures</td><td>APN</td><td>No</td><td>OPSL</td><td>Scoops</td></tr><tr><td>FFM [50]</td><td>Forms, Procedures</td><td>FFM</td><td>No</td><td>TLA</td><td>OFS, MRS</td></tr><tr><td>ODM [22]</td><td>Data</td><td>ODM</td><td>No</td><td>None</td><td>None</td></tr><tr><td>OSL [24]</td><td>Data</td><td>SDM</td><td>No</td><td>OSL</td><td>None</td></tr><tr><td>OfficeTalk-D [16,17]</td><td>Forms, Procedures</td><td>Forms, ICN</td><td>No</td><td>None</td><td>OfficeTalk-D</td></tr><tr><td>Omega [5,6,26]</td><td>Problem Solving</td><td>None</td><td>No</td><td>Omega</td><td>Omega</td></tr><tr><td>Poise [12]</td><td>Procedures, Data</td><td>Poise, ODM</td><td>No</td><td>EDL</td><td>Poise</td></tr><tr><td>SOS [9]</td><td>Data, Activity</td><td>SOS</td><td>No</td><td>None</td><td>None</td></tr><tr><td>OSSAD [11]</td><td>Functions, Roles, Information</td><td>OSSAD</td><td>No</td><td>None</td><td>None</td></tr><tr><td>Offis [28]</td><td>Communications</td><td>None</td><td>No</td><td>Offis</td><td>None</td></tr><tr><td>OSM [2]</td><td>Agents</td><td>OSM</td><td>Yes</td><td>None</td><td>None</td></tr><tr><td>Cokes [27]</td><td>Communications, Organizational</td><td>None</td><td>Yes</td><td>None</td><td>Cokes</td></tr><tr><td>KRS [1,31]</td><td>Documents, Procedures, Organizational</td><td>KRS</td><td>Yes</td><td>KRS</td><td>Office Assistant</td></tr><tr><td>AEI [3]</td><td>Integrated</td><td>AEI</td><td>Yes</td><td>None</td><td>AEI</td></tr></table>

An architecture may be thought of as an implementation philosophy. The architecture must: (1) be based on the model so that it will reflect the nature of the office; (2) have its component functionality clearly defined; (3) have loosely coupled components for software engineering reasons; (4) be knowledge-based since offices are, by definition, knowledge-intensive; (5) have its knowledge clearly partitioned to allow it to be easily modified—declarative representations are popular for this reason; (6) be capable of accommodating different types of office knowledge; and (7) be implementable in various organizational and computational environments. As with models, some researchers have not emphasized this phase of the research.

A specification language can be a language for expressing system specifications (e.g., Offis [28]), a language for expressing knowledge (e.g., KRS [31]), or a special-purpose language for implementation (e.g., OPSL [51]). We consider expressiveness and naturalness of the representation to be key criteria for the specification language [24]. The language must be capable of handling both declarative and procedural knowledge as these are present in the office [6]. Naturalness of the representation facilitates implementation and maintenance. For widespread applicability, the model and architecture must be independent of the implementation language, that is, they must be implementable in a variety of languages. The office system is ultimately the target for all the preceding development effort. The viability of a model or architecture is commonly demonstrated through system implementations. An office system consists of the necessary resources to automate office work. Although a number of requirements can be placed on office systems, at a very minimum, the office system must: (1) have a friendly interface; (2) support office workers to the extent possible [38] (this implies that the system will have various levels of support); (3) be capable of reasoning about office work [20] in terms of gauging which activities have to be performed, in what order, and to troubleshoot if necessary; (4) exploit the existing application structure (again for software engineering considerations); and (5) be evolvable to account for the changing nature of the office [8].

These requirements are summarized in Table 2. We have developed a model-based and knowledge-based office system (which we will refer to as AEI $^{1}$ ) to address these requirements. Before we discuss our architecture further, we will first examine some of the representative efforts more closely.

The remainder of our paper is organized as follows: in section 2 we briefly discuss and evaluate some of the significant office models and knowledge-based office systems. In section 3 we discuss the model on which the architecture is based. In sections 4 and 5 we present the AEI architecture. In sections 6 and 7, we describe by means of a case example of an Army office how the architecture can be applied to an office, and finally in section 8 we discuss the features and limitations of our research and our conclusions.

## 2. Brief Review of the Literature

IN THIS SECTION WE BRIEFLY SURVEY some office models and office systems that are representative of systems in office automation research. Starting with a descriptive model (OSSAD), we proceed to a specification language and problem-solving system (Omega) and then to some intelligent office systems (Poise, Cokes, KRS). A full treatment of the literature is beyond the scope of this paper and the reader is directed to [3, 8, 18] for this purpose.

## 2.1. OSSAD

OSSAD is a descriptive office model developed under the auspices of the Esprit project in Europe [11]. It consists of three types of models: the abstract, the descriptive, and the specification models. The abstract submodel is a description of the information flows (“packets”) among functions and subfunctions, which are further broken down into information flows at the level of activities. The descriptive submodel is comprised of models for roles (work assigned to individuals) and tasks (activities assigned to roles). The specification model is concerned with technical specifications such as those used in software engineering. The OSSAD model is important since it was one of the few models that emphasized interconnection between functions, activities, tasks, and information. The major limitation of OSSAD is that, to our knowledge, it was not extended into an office system. The design details thus remain obscure.

Table 2 Office System Requirements

<table><tr><td>VIEW</td><td>Must be integrated.</td></tr><tr><td>MODEL</td><td>Must represent the entire office. Must be applicable to different types of offices. Must be intelligible. Must be viable.</td></tr><tr><td>ARCHITECTURE</td><td>Must have a well defined functionality. Must have loosely coupled components. Must be knowledge-based. Must have knowledge that is well partitioned. Must have a Knowledge base capable of representing diverse office knowledge. Must be viable.</td></tr><tr><td>SPECIFICATION LANGUAGE</td><td>Must permit representation of procedural and declarative office knowledge. Must be natural to the extent possible.</td></tr><tr><td>SYSTEM</td><td>Must be user-friendly. Must support office workers to the extent possible. Make use of the existing application structure. Must be evolvable.</td></tr></table>

## 2.2. Omega

Omega is a problem-solving system developed by Barber and Hewitt at MIT $[5, 6]$ . It uses the Omega language, which resembles predicate calculus in syntax, for its knowledge representation $[26]$ . In Omega, properties of an office object (for example, a form) are described through what are called “descriptions.” A description remotely resembles a record (or a frame). A description at a specific time instant is referred to as a “viewpoint.” Office work is viewed as the history of information or succession of viewpoints. Descriptions serve to store, transfer, display, accumulate, and modify information. When a user describes a new viewpoint, the system either establishes the consistency of that viewpoint or assists the user in arriving at a new viewpoint that is consistent with existing viewpoints. Problem solving is supported through this viewpoint mechanism. Although an influential system, Omega was restricted to being a generalized problem solver. The researchers did not address the issue of its integration with an office system. Its knowledge representation language is also unable to handle office knowledge in its free form.

## 2.3. Poise

Poise is an office system for intelligent automation of procedures developed by Croft and Lefkowitz [12] at the University of Massachusetts. It consists of: a user interface for interpreting user requests, user actions, and communicating status information; a data model (ODM) for representing objects used by procedures; a procedure library containing the code for executing procedures; and conventional office tools. Procedures in Poise are broken down into goal hierarchies which are used to monitor user actions, while they are on the system. When a user's action is erroneous, it will not fit the pattern in the goal hierarchy and therefore triggers an error message. Thus, intelligence is supplied at the interface level and at the procedure level. Poise was later embellished with a procedure planner for identifying sequences of actions to be taken to perform tasks [13]. Its major weakness is the somewhat awkward representation of procedures (it uses templates) which makes it cumbersome for describing procedures; procedure descriptions are also closely coupled to the data model, increasing challenges for implementation as well as maintenance. Another limitation of Poise lies with its natural language interface, which was table-driven.

## 2.4. Cokes

Cokes [27] is a knowledge-based mail system similar to AIMail [10] and the Information Lens [30] projects. The Cokes knowledge base encompasses frames for declarative knowledge and rules for procedural knowledge. Declarative knowledge includes knowledge of office objects and knowledge of the office structure, while procedural knowledge contains knowledge of communication policies. Declarative knowledge is represented with frames while the procedural knowledge is represented with rules. While this scheme appears valid for the communications domain, its applicability to other domains can be questioned. The richness of the domain [8, 22] requires a more diverse approach to representing office knowledge.

Under the auspices of the Esprit project, an ambitious attempt has been made to

## 2.5. Knowledge Representation System—KRS

develop a universal knowledge representation language (known as KRS) for the office. KRS [29, 31, 46] is a Lisp-based object-oriented representation not unlike KRL [7], comprised of primitives (such as contexts, subjects, inheritance maps, controllers, and collectors) aimed at modeling the diverse and open-ended knowledge of the office. It is capable of accommodating a variety of representation schemes including frames, logic, semantic nets, and the like, but like KRL, it suffers perhaps from the weight of its own features. The extent of interconnections provided in KRS (for example, between subjects, controllers, and collectors) make the underlying model opaque to the end user, if not to the programmer. This is somewhat akin to the problems being faced with hypertext systems today. Unless the interconnections are disciplined somehow, they could lead to problems such as spreading activation.

The Office Assistant is a system based on KRS [1]. The system is based on a model of the organization, procedures, documents, facilities, and time. The architecture of Office Assistant has an operating systems flavor while its interface resembles those systems using the desktop metaphor. The system is user-oriented. This research has been complete as a development effort. As pointed out, the model and specification language lead to an interconnected knowledge base. Also, the Office Assistant can be criticized for its operator-level orientation (see the appendix).

## 2.6. Evaluation

We have reviewed five models/systems above. To do justice to the research attempts, we have presented the models/systems according to their design philosophies. We now present an evaluation along the dimensions introduced in section 1 (see Table 2 again). These are summarized in Table 3. Several observations may be made of these representative models/systems:

1. OSSAD, Omega, and Cokes are incomplete from the system development standpoint. Omega and Cokes lacked models, while OSSAD was not (to our knowledge) developed beyond the model.

2. None of the systems/models was based on an integrated view of the office. For example, OSSAD considers functions, roles, tasks, and information, while Omega is restricted to the domain of problem solving.

3. The models are correspondingly limited in scope. Further, none of the attempts has proposed a theoretical basis for developing office systems.

4. Poise and KRS have representations that may present problems of intelligibility.

5. The functionalities of Poise, Cokes, and KRS have been relatively well defined. The functionalities of Omega and OSSAD are somewhat limited, as discussed in the preceding review.

6. Omega, Poise, Cokes, and KRS are knowledge-based systems. With the exception of KRS, their representation schemes are restrictive.

Table 3 Strengths and Limitations of Representative Systems

<table><tr><td>Dimensions of Evaluation</td><td>OSSAD</td><td>Omega</td><td>POISE</td><td>Cokes</td><td>KRS</td></tr><tr><td>View</td><td colspan="5"></td></tr><tr><td>Integrated</td><td>L</td><td>L</td><td>L</td><td>L</td><td>L</td></tr><tr><td>Model</td><td colspan="5"></td></tr><tr><td>Scope</td><td>N</td><td>NA</td><td>L</td><td>NA</td><td>N</td></tr><tr><td>Applicability</td><td>S</td><td>NA</td><td>N</td><td>NA</td><td>S</td></tr><tr><td>Intelligibility</td><td>S</td><td>NA</td><td>L</td><td>NA</td><td>L</td></tr><tr><td>Architecture</td><td colspan="5"></td></tr><tr><td>Functionality</td><td>NA</td><td>NA</td><td>S</td><td>S</td><td>S</td></tr><tr><td>Software Eng.</td><td>NA</td><td>NA</td><td>L</td><td>S</td><td>L</td></tr><tr><td>Knowledge-based</td><td>NA</td><td>S</td><td>S</td><td>S</td><td>S</td></tr><tr><td>Multi-paradigm</td><td>NA</td><td>L</td><td>L</td><td>L</td><td>S</td></tr><tr><td>Specification Language</td><td colspan="5"></td></tr><tr><td>Declarative &amp; Procedural</td><td>NA</td><td>L</td><td>L</td><td>N</td><td>L</td></tr><tr><td>Natural</td><td>NA</td><td>S</td><td>L</td><td>S</td><td>L</td></tr><tr><td>System</td><td colspan="5"></td></tr><tr><td>Implemented</td><td>NA</td><td>S</td><td>S</td><td>S</td><td>S</td></tr><tr><td>User-friendly</td><td>NA</td><td>S</td><td>S</td><td>N</td><td>S</td></tr><tr><td>Existing env.</td><td>NA</td><td>L</td><td>S</td><td>S</td><td>N</td></tr><tr><td>Evolvability</td><td>NA</td><td>S</td><td>N</td><td>N</td><td>S</td></tr></table>

Note:  
S - Strength  
L - Limitation  
N - Neither  
NA - Not applicable

7. While most of the attempts have resulted in implementations, some of the important issues, such as user-friendliness, implementation in an existing application environment, and evolvability, remain to be addressed.

In general, models and systems are inadequate in one aspect or another. We have made an attempt to develop an office system that addresses what we consider to be the minimal requirements for office systems research with the hope that it can be the starting point for more ambitious development efforts.

Starting with a holistic view of offices, we have developed an integrated model and architecture (which we will refer to as AEI) designed to support office workers in their administration-related activities. The research is integrated from a system development perspective, from an application (task support) perspective, as well as from the implementation (existing programs) perspective. Our research must be viewed as part of the evolution in office systems thinking rather than as a radical departure from tradition.

## 3. A Model of the Office

AN OFFICE MODEL IS A GENERALIZED DESCRIPTION of interactions among entities in the office: the office being defined as a geographical unit of the organization that processes information [18]. At this stage of our research, we restrict ourselves to providing automation support for Type I office tasks [36]. These are clerical and administrative tasks of employees. The model captures the understanding of what occurs in all offices and as such forms the basis of the generalized AEI office architecture. The AEI model is based on the assumption that office work is the result of response to some internal or external stimuli (see figure 1). The nature of these stimuli varies from situation to situation. For instance, a customer could request the status of an order, a subordinate could be asked to review a report, or a deadline could initiate budget preparation. Office workers respond to such stimuli in accordance with the organizational/functional structure of the office; responses could be predetermined as in office procedures or they could require problem solving [5, 6, 47, 48]. Regardless of whether office workers respond mechanically to a situation or intelligently, responses can be viewed as a source of feedback for the action, or they could stimulate additional actions. For example, when a customer orders a product, the order could trigger a sales-invoicing procedure and a shipping procedure.

The AEI model is based on three assumptions. The first assumption made by AEI is that office work is stimulus-driven. A few researchers concur with this view $[16, 33, 51]$ . Its broader roots can be traced to the work of behavioral scientists such as Skinner $[43]$ who viewed human behavior as stimulus-driven. The next major assumption of the model involves the nature of office work, that is, routine versus problem solving. This obviously varies with the type of office. In bureaucratic offices, for example, as much as 90 percent of the work is standardized $[34]$ . Our study of an Army office also revealed that Army personnel do not deviate from Standard Operating Procedures (SOPs) $[3, 44]$ . In general, though, about 43 percent of all office work is formalizable, that is, it could be encoded into procedures $[34]$ . These procedures could involve forms, decisions, communications, information $[19, 49]$ . The remaining 57 percent of office work presumably involves, among other activities, problem solving $[20, 37, 47, 48]$ . This is an area that has often been neglected in the literature. For example, the literature falls short of documenting both the types of stimuli that occur in offices, the cognitive processes involved, and the types of problem solving that occur. $^{2}$ We assume that both types of activities occur in offices. The third assumption of the model deals with allocation of organizational responsibility, that is, the organizational/functional structure. In some types of organizations this allocation is formal while in others it is informal or dynamic. We assume that it is formal, although we see no reason why the corresponding architecture component cannot be upgraded to handle dynamic task allocation.

![](/api/attachments/8TR5EK6S/fulltext/images/c76b130a84f1b67b766f1f023a9739f3e408f2dae887bd5e5de5ccc2533c04b5.jpg)  
Figure 1. The AEI Model

## 4. An Overview of the AEI Architecture

THE INTEGRATED AND KNOWLEDGE-BASED OFFICE ARCHITECTURE developed from the model discussed in the previous section is illustrated in figure 2. The primary components of the architecture are:

A. Interface Module—The interface module handles the dialog between the user and system. It consists primarily of screens, menus, and help messages. It will accommodate requests in natural language as well as those entered through conventional menus. For example, to monitor progress on a project, a manager could enter, "What is the status of the IOIS project?" or type "menu," and select "projects" and "status" from the menu. Because of widespread availability of interface design tools, this module will be omitted from further discussion.

B. Event Handler—The event handler interprets or recognizes stimuli occurring in the office. At present the architecture is geared for stimuli initiated by users. Other types of stimuli, such as changes triggered by database updates, are not considered. When users issue action requests, their intentions are interpreted by the event handler and passed to the procedure planner (see below).

C. Procedure Planner—The procedure planner identifies what system actions will satisfy the user's request by making use of the domain knowledge. It carries this out by interpreting the functional structure, a network of nodes representing functions and procedures in the office.

D. Domain Knowledge—Domain knowledge consists of knowledge common to the office and knowledge about specific application areas. The common office knowledge consists of the organizational and functional structures, while the application knowledge consists of the domain areas: forms, database, information, communications, and decisions.

E. Application Structure—This component contains the knowledge necessary to execute plans prepared by the procedure planner. It consists of procedure libraries, office tools/software, and utilities/macros acting on these tools.

![](/api/attachments/8TR5EK6S/fulltext/images/1e69ac3a5bef55dd387bd1b26be755948ca06ae4f5e90c1bc2e3a9030b134183.jpg)  
Figure 2. The AEI Architecture

F. Exception Handler—If the planner is unable to plan a suitable procedure, the inference engine passes control to the exception handler, which then attempts to gather information relevant to the problem at hand or identifies personnel who can address it.

G. Inference Engine—The inference engine controls interaction among various components of the architecture. It allows users to access the system through the interface module, calls the event handler to understand their request, calls the planner to determine how their request is to be carried out, and then finally initiates execution through the application structure. Since the inference engine is usually supplied with the language used, it will not be discussed further.

Interaction among the components can be described as follows: Users enter their requests in natural language, through the interface module. The inference engine passes the request to the event handler, which processes it and identifies their intention. The next step is to identify the specific office task to be performed along with other associated office tasks. The inference engine invokes the planner. The planner is an algorithm to navigate a goal network to identify the sequence in which tasks have to be performed. The goal network is derived from the functions and procedures of the office. The final step is to execute the plan created by the planner by invoking various combinations of procedures, tools, and utilities, from the application structure.

Integration among the various components is achieved simultaneously from several directions: the interface, the inference engine, the organizational and functional structures, the information domain, as well as the application structure. However, the coupling is loose enough that designs for individual components can be independently changed and additional applications can be readily integrated with the office system. The primary burden of integration is borne by the inference engine through managing component interactions.

## 5. Description of Important Architecture Components

THIS SECTION DESCRIBES THE DESIGN AND FEATURES provided by the more important components of the AEI architecture. As mentioned, the interface module and inference engine are left out of the discussions.

## 5.1. Event Handler

The purpose of the event handler is to interpret office events with respect to its normal activities. Although various types of events occur in offices, including those triggered by customers, supervisors, vendors, and so on, we restrict ourselves to those initiated by users of the system. The event handler processes free-form user requests received from the interface module and identifies their intentions. It does this using the story understanding paradigm $[40, 41, 42]$ , an extension of Conceptual Dependency (CD) theory $[39]$ .

Conceptual Dependency theory was developed in connection with natural language processing. Its basic premise is that there is a conceptual structure underlying sentences $[9, 20]$ , which, once identified, can be used to make inferences regarding goals of the actor (usually a noun). This conceptual structure is constructed from concepts in the sentence and conceptual primitives. For example, in the sentence, “John pushed the chair towards Mary,” the conceptual structure would be “John PTRANSed Chair to Mary,” with John, Chair, and Mary being concepts and PTRANS being a conceptual primitive. This structure could be used to arrive at the conclusion that John wanted Mary to sit on the chair since the object that is being transferred, namely, the chair, is normally used for sitting.

To understand a request, the event handler has to identify concepts in the sentence and generate a conceptualization. A static conceptualization is already present in the functional structure. The function of the event handler is therefore one of finding the node in the functional structure that would satisfy the user's request. To facilitate this task, object action libraries are maintained in the event handler. For example, a Bill of Materials form is typically filled and routed. "Bill of Materials" is the object and allowable actions are "filling" and "routing." Their synonyms are also maintained in the library.

## 5.2. Procedure Planner

The procedure planner generates plans according to user requests processed by the event handler. The functional structure consists of a network of nodes primarily representing functions and procedures in the office. Some of these can be executed by the system while others have to be performed manually. Corresponding to the executable nodes, there are procedure libraries (software libraries). Users may request either a simple task such as “make a note that X is good worker” or a complex task such as “prepare an acquisition package.” In the former case, planning simply consists of checking libraries in the application structure. In the latter case, the planner must determine the proper sequence in which activities contributing to the event should be executed. Since the functional structure already contains relationships among functions and activities, planning is reduced to interpreting the functional structure. The important steps in the planning sequence for AEI including that performed by the event handler are captured in the chart in figure 3.

For an office system to be completely intelligent, the planner must be capable of generating procedures dynamically depending on the situation. However, there are fundamental problems such as subgoal interaction and indeterminism associated with offices $[25]$ that preclude such an approach. The planner algorithm is independent of the office domain because it only navigates the functional network. There is no reference in the planner algorithm to actual functions and procedures within the target office (for example, fill Bill of Materials). The functional structure changes from office to office but because nodes and relationships among them are standardized (e.g., event entity, information entity, information dependency), interpretation of any given structure is always uniform.

## 5.3. Domain Knowledge

Domain knowledge consists of knowledge common to the office and knowledge specific to application areas. The common office knowledge has been grouped into the organizational and functional structures, which are used by other domains/applications within the system. The specialized domains have been grouped into forms, information, communications, and decisions. There are other methods of organizing office knowledge $[5, 10, 12, 27, 29, 31, 46]$ , yet this method is more logical and natural, given the nature of office activities. As pointed out in section 3, the categorization has been developed from office studies $[19, 49]$ .

Forms knowledge consists of form fields, attributes, and routing information $[50]$ . The design of this component is relatively straightforward and readily available in commercial tool kits. Therefore, this component will not be discussed. The other domains are described below.

## 5.3.1. Domain Knowledge—Organizational Structure

The organizational structure is part of the common office knowledge. It is used: (1) to check if an agent's action is permissible according to the organizational task allocation; (2) to provide response to a query such as “Who is in charge of funds?”; (3) to provide knowledge about the personnel organization to other components such as “decisions” and “communications”; and (4) to identify the person to whom an action request is to be directed should the system fail to solve a problem. The design of this component is based on a simplified version of the Office Structure Model [2]. The organizational structure is expressed as a set of predicates (or relations) as follows:

![](/api/attachments/8TR5EK6S/fulltext/images/6bddd895a9e7319f68ca95592a9a0019283d4f252ca8a9f066a9de10f06b2c73.jpg)  
Figure 3. The Planning Sequence

person(name, title)

reports\_to(superior, subordinate)

job\_descr(title, function\_list)

This can easily be made more elaborate, for example by including rules under which each person carries out his or her role (“If the project-leader is absent, the senior-most programmer is authorized to make design decisions . . .”) or rules for allocation (“If many project leaders are qualified to lead a project, select the one whose experience matches the project best . . .”) in case roles are nonunique.

## 5.3.2. Domain Knowledge—Functional Structure

The functional structure component consists of a network of nodes representing relationships between functions, procedures, activities, and information used in the office. This is constructed by analyzing functions and activities performed in the office. The functional structure is used by other components in the architecture such as the inference engine, event handler, and procedure planner as the basis for reasoning about office activity. For example, the types of inferences that can be made from the functional structure are summarized in Table 4.

The design of this component is based on CD theory $[31, 32, 33, 34]$ . As described earlier, the fundamental principle of CD theory is that there is a deep underlying structure called a “conceptualization” in sentences that is independent of syntax. The conceptualization is comprised of relationships among concepts used in the sentence. Understanding a sentence, then, consists of generating these conceptualizations and drawing inferences from them.

Just as there are conceptualizations in a sentence, there are conceptualizations in an office involving agents, office objects, functions, procedures, and information. $^{3}$ These relationships are expressed in the AEI structure using “node types” (entity types) and “relationship types” (link types). This is a departure from CD theory since the office required completely different node types and relationship types. For the general office, we have limited ourselves to two node types and four relationship types, to make the structure user-friendly and to simplify the inferencing. These are illustrated in figure 4 using an example of a small manufacturing company that makes-to-order. The figure also illustrates the applicability of CD theory to the office domain.

The advantage of using CD theory is that general knowledge about office activities is encoded declaratively in a simple but effective structure. While the functional network varies from office to office, the network constructs are invariant across offices. It ensures that the same reasoning mechanism can be used for any office whose

Table 4 Inferences That Can Be Drawn from the Functional Structure

● What functions, procedures, or activities does the office have?

● For a given function, what are the component activities (or events)?

● What are the predecessor and successor activities for an event?

● What information is required for an activity?

● What information is generated by an activity?

● Which activities are completed in parallel?

● What is the purpose of an event (display the description)?

functions are thus encoded. For example, if two entities are connected with a structural dependency, this always means that one of them is a component of the other regardless of the office.

## 5.3.3. Domain Knowledge—Database Knowledge

The database is accessed independently or by other components of the system (for example, the plan execution component) for structured information. Database knowledge is organized into four parts:

1. Knowledge of the relations that exist in the database;

2. Knowledge about the individual attributes that make up each relation;

3. Knowledge required for selecting a tuple in the database; and

4. Knowledge required to perform operations on the database.

The first two types of knowledge are readily available from the system catalog. The implementation of these has also been described in detail in $[4]$ . The third type of knowledge, knowledge required for extracting data, is supplied by the event handler or by the planner making necessary inferences from the domain knowledge. For example, in a request such as “What is the status of the IOIS project?” (for activities completed and to be completed, due dates, etc.), the appropriate query would be:

SELECT activity, duration, status, completion date FROM projects where project = "IOIS".

The details required to build the query are obtained from the event handler and the system catalog. The event handler recognizes “IOIS” as a project and “status” as an action from its object-action library and instantiates the user view, projects(status, activity, duration, . . .) from the system catalog. The fourth type of knowledge involves software routines to perform database operations (such as retrieving records) and is part of the tool knowledge. In the given example, the database procedure for retrieving the required information is invoked from the tool library.

Relationship Type  
![](/api/attachments/8TR5EK6S/fulltext/images/3d75e76a2224d507105680a710344369d9f54530fff0de09d6a9e73d174af0f7.jpg)

## Interpretation

SD = Structural Dependency

The function, estimate costs consists of three activities: estimate labor, estimate materials and estimate overhead.

ID = Information Dependency

The function, estimate materials needs information from the bill of materials.

The function estimate overhead needs Accounting information.

TD = Time Dependency
The function, estimate costs is done after receiving an inquiry.

The function, confirm order can be done after estimating costs

AD = Associative Dependency
The function send invoice is completed at the same time as the goods are shipped.

The function fill bill of materials is executed at the same time as the product is manufactured.

Figure 4. Functional Primitives

The database itself contains records of entities that are relevant to the office such as projects, personnel, contractors, funds, schedules, equipment, and the like.

## 5.3.4. Domain Knowledge—Office Information

This domain contains reports and unstructured information, in contrast to the database domain which carries more structured information. This distinction is not present in the functional structure, which “describes” both types of information with a single node type. For example, the functional structure does not distinguish among data items, records, informal notes, or documents. When the AEI system needs information, it searches the database for structured information or, alternatively, the “information” domain for reports and unstructured information.

Reports and documents are stored in an object-oriented structure similar to the one used in part of the Office Data Model $[12, 22]$ . All office documents are grouped into classes (see figure 5). Documents have some properties that can be described at the class, or subclass, level. Individual objects belonging to the class or subclass can be defined to inherit some or all of these properties. For the “project related” class, the properties shared by all documents are shown to be: author, title, etc.

The primary advantage of this structure is that search can be based on the class/sub-class level or on the level of individual objects. An example of a class/subclass search is: "list all documents relating to the IOIS project." Documents can be managed with a conventional database as well, although the object-oriented approach is more attractive because of its capability for inheritance and ability to retrieve and update objects based on search at the class level.

All types of information are thus integrated with the office system and can be accessed either independently by the user or during execution of some task or activity.

## 5.3.5. Domain Knowledge—Communications

Communications knowledge has been the subject of several research projects $[10, 27, 30]$ . As with other domains, the advantage of including communications here is that it is part of an integrated office system, using the common office knowledge rather than being an island. Our approach does not differ from those in existence.

Communications knowledge concerns message types, communication policies (rules), and any additional routing knowledge. Message types or “templates” are general categories of messages such as meeting announcements, design changes, information about interest areas, and so on. They allow incorporation of intelligence into the system by allowing mail to be processed by rules. When a message is received, it is classified into a type and the rules corresponding to the type are triggered. Rules are derived from communication policies, which are official protocols for sending, routing, and receiving mail messages. The following is an example of a communication policy: “Please inform the project manager of any design changes.” Various actions can be taken on the message, depending on the rules. Routing information is concerned with directions for sending messages to individuals, for example: “send all my mail to Milam Aiken for the next two weeks.”

## 5.3.6. Domain Knowledge—The Decisions Domain

The decisions domain consists of the knowledge or models required for decision making in the office. Until research in this area advances, this is a domain that tends to be application-specific. For AEI, ROMC was used as a general strategy for dealing with the decision domain $[45]$ . The application structure of AEI contains the DSS generators and the DSS tools [45]. To the extent that information required for decision making is contained in the common office knowledge and the database/information domains, the decisions domain is integrated into the architecture.

![](/api/attachments/8TR5EK6S/fulltext/images/72382c8003ee2f1105bf327147de64ad07cc69eb1281d218ee9f11b0d06d2c9f.jpg)  
Figure 5. Document Structure

## 5.4. Application Structure

The application structure [6] consists of the procedural structure and the tool/utility structure. It is important to treat these as a separate domain to achieve tool independence (replacing a spreadsheet software with a newer product), to allow implementation of the system in the context of an existing application structure, to ensure portability to other offices, and finally to control proliferation of EUC programming. After a plan is determined, the inference engine checks to see which of the steps of the plan can be executed by checking against the procedural and tool libraries. Those that cannot be executed are passed on to the exception handler.

The procedural structure consists of a library of precoded software routines embodying knowledge of executing office procedures such as forecasting cash flows or creating invoices. In the past, procedural models $[9, 12]$ have attempted declarative specification of procedures with the idea that these are easier to develop and update. Templates have often been used for this purpose. We feel that such an approach imposes an artificial structure that increases maintenance difficulties because procedures are numerous and ever-changing. Moreover, it is difficult to integrate those with automated procedures already in existence, in conventional languages. Procedures must therefore have clean interfaces (inputs and outputs), must make use of existing tool/utility structure to the extent possible, and must be compatible with the inference engine and interface components.

Office tools are office software such as spreadsheets while macros and utilities are those programs operating on the tools and usually developed in 4GL languages. Tools and utilities serve two purposes within the architecture. First, they can be invoked by procedures within the procedural libraries and, second, they can be accessed independently by the end user.

The principles by which the application structure is designed are illustrated by the high-level procedure for assigning personnel to projects shown below in pseudo Prolog. There are some things to be noted about the example. The procedure “assign\_personnel” makes use of several utilities such as “check\_authorization,” “get\_data,” “update\_db,” which operate on the organizational structure and the database. “Make\_assignment,” is another module called by “Assign\_personnel” which in turn makes a call to an external program and passes the personnel and project information to it.

Procedure Assign Personnel

Assign\_personnel(Username):-

check\_authorization(Username, assign\_personnel),

get\_data(personnel, Researcher\_list, Researcher\_profiles),

get\_data(projects, Project\_list, Project\_profiles),

make\_assignment(Researcher\_list, Researcher\_profiles,

Project\_list, Project\_profiles, Assignment\_list).

update\_db(personnel, Assignment\_list).

Utility Check\_authorization

Check authorization(Name, Activity) :-

person(Name, Title),

job\_descr(Title, Function\_list),

member(Activity, Function\_list).

Such principles will lead to an application structure that can be easily developed, maintained, and reused. For large offices, the productivity benefits resulting from a rational organization of the application structure could be considerable.

## 5.5. Exception Handler

The exception handler handles exceptions to normal office operations. For the Type I office tasks [36] for which this architecture is aimed, these include workers being on leave, information or forms that have been misfiled, orders that are misdirected, and so on. To a certain extent our architecture minimizes these exceptions by facilitating access to domain information. If a worker enters an unusual request into the system (a request not covered by the existing functional structure), the exception handler initiates a search through the organizational structure to see if another worker could handle it. It also searches through the information domain and the functional structure to see if any relevant information could be found regarding the request. Apart from this type of support, even in a Type I office, exceptions have to be handled on a case-by-case basis. Omega [6] was a reasonable attempt in this direction although implementing problem solving on a case-by-case basis in a formal language is hardly practical given the firefighting type of situations that surround exceptions. This is an area that deserves further investigation.

When exceptions become frequent, they can be routinized. To encourage the practice of routinizing exceptions, the exception handler requests workers to store descriptions of the exception associated with the worker's function. When exceptions recur, the historical descriptions are used to convert the exception into a named node in the functional structure, with associated executable procedures in the procedure library.

We discuss the application of the architecture with the help of an office study, which we discuss in the next section.

## 6. An Office Study—AIRMICS

THE ARMY INSTITUTE OF RESEARCH IN MANAGEMENT INFORMATION, COMMUNICATIONS AND COMPUTER SCIENCE—AIRMICS—is an office in Atlanta that conducts and sponsors research in areas of information technology considered to be important by the U.S. Army. The organizational chart of AIRMICS shown in figure 6 summarizes its personnel structure. AIRMICS carries out both internal and external research in order to fulfill its mission of conducting and sponsoring research.

For each project, AIRMICS management appoints a “COR” (Coordinating Officer) who is in charge of initiating and monitoring the project. In connection with initiating a project, a COR must prepare an “acquisition package.” We will focus on the preparation of an acquisition package to illustrate our architecture. The acquisition package consists of:

1. A statement about the uniqueness of the project established by searching a historical database;

2. A technical evaluation of the research value and scope of the project;

3. A Purchase Requisition and Commitment (PR & C) form required for administrative purposes;

4. A Work Unit Summary Form summarizing the work to be done;

5. An approval letter from the director of AIRMICS; and

6. The project proposal that was initially submitted by the contractor.

The acquisition package is prepared by the COR during the initial stages of the project. The uniqueness of the project is first established by searching a historical database (known as DTIC) to ensure that a similar project was not funded in the past by another DOD agency. In order to search the database, the COR consults a directory to find the standardized search terms. He or she then prepares an evaluation of the project based on its potential research value and its viability. This is recorded on a project evaluation form. The next step is to record details of the project, funding, and contractor information on the Purchase Requisition and Commitment form (PR & C form). A Work Unit Summary form capturing details of the work to be done is also filled at this stage. The last step is to obtain approval. This is done along with other potential projects. If the project is approved, an approval letter is prepared and the project is formally initiated.

![](/api/attachments/8TR5EK6S/fulltext/images/4772494447d5bb0542cb79847c1a4c381264cb2b0def98e0ee55ae819804b83c.jpg)  
Figure 6. AIRMICS Organizational Chart

After initiation, the project is monitored for progress through periodic reviews until it is completed. On completion, some termination procedures are carried out and the results are utilized as input for making decisions on acquiring future services and implementing systems within the Army.

From this brief description of AIRMICS, some observations from an OA perspective may be made. First, there are some cognitive tasks such as evaluating projects and some noncognitive tasks such as filling forms. Second, there are predefined procedures and activities for carrying out the routine, noncognitive tasks. Third, many of the noncognitive tasks such as filling forms, searching databases, printing approval letters, and searching online databases are automatable. These could be automated in an “island” fashion as is normal in offices today, or through the integrated and intelligent office system that we have proposed and illustrate in the next section.

## 7. Illustration of the Prototype

A PROTOTYPE SYSTEM BASED ON THE AEI architecture and tailored to the AIRMICS environment was developed primarily in Turbo Prolog, using the Turbo Prolog Tool

Box $^{4}$ for the interface module and the built in database. Since Turbo Prolog uses extended memory only for the database, its 640K limitation for programs required us to implement components of the architecture separately. With the exception of the inference engine, which was supplied with Turbo Prolog, and the exception handler, all components of the architecture were implemented. At present, the exception handler's function is limited to switching the system to menu operation when it cannot understand a particular request.

Prolog was chosen for its desirable features as a specification language $[14]$ . The AIRMICS organizational structure was implemented with a set of predicates as described earlier. The functional structure (part of which is shown in figure 7) was implemented with a semantic net in Prolog. The forms domain was implemented using Vermont Views (a registered trademark of Vermont Creative Software). A decision support system for the task of allocating personnel to projects was also implemented in Vermont Views and Microsoft C (a registered trademark of Microsoft Corporation). The database was implemented with Turbo Prolog's external database. An intelligent mail component processed mail messages in the form of text files using the organizational and functional structures.

Rather than dwell on the numerous implementation details, we will illustrate our architecture with a scenario involving the task of preparing an acquisition package. In the scenario, a new COR for the IOIS project, Captain Ted Hengst is asked to prepare an acquisition package.

After logging in through the main menu of the AEI system, Captain Hengst is presented with a natural language interface. If Captain Hengst did not know what an acquisition package was, he could get information by enquiring “What is an acquisition package?” Each node in the functional structure (not shown in figure 7) has text descriptions attached to it so that information about procedures can be obtained by new personnel. Office personnel can also add their experiences to the descriptions. The COR requests the preparation of an acquisition package or types “Help.” In the former case the request is understood by the event handler and passed on to the planner. In the latter case, the AIRMICS functions are displayed in a menu as shown in figure 8. For illustrative purposes, the planner is demonstrated explicitly in this scenario. In a production system, the planner would be transparent to the user.

The COR selects the function “prepare acquisition package.” The next step is to identify the predecessor events. In an actual system, the planner would automatically check to see if other prerequisite or related tasks were completed, whether any information was required for the requested function, and whether the function has any component events. In the scenario, the COR is presented with a list of dependencies. He selects the option “component events.” The planner navigates through the functional structure and identifies the component events as shown in figure 8.

The system then prompts the COR if he wanted to execute the component events. The COR responds with a “Yes.”

The inference engine then automatically invokes the module “search\_dtic.” The main functions of this module are: (1) creating the project profiles, (2) executing the search, (3) editing the extracted file, and (4) saving the profile. These are shown in the “DTIC Search” main menu in figure 9. The COR first creates a project profile by selecting keywords describing the project. For instance, the IOIS project can be described by the following keywords: (1) Systems Analysis, Office Automation, Forms, DSS, GDSS, (2) Artificial Intelligence, and (3) Information Management. When the COR executes the search on the DTIC database, the profile of the project is matched with profiles in the database and descriptions of any matching projects are extracted in a separate file. The file being scanned is displayed in a separate window and any extracted profiles are displayed in another window.

![](/api/attachments/8TR5EK6S/fulltext/images/17027420067da67c6c57b867733975950530ccf9f610e88597d5ad58892f72d8.jpg)  
Figure 7. AIRMICS Functional Chart (Partial View)

The inference engine then invokes the next subfunction of prepare-acquisition-package, which is “evaluate project.” The COR is now presented with an evaluation form as illustrated in figure 10. The system would automatically fill in certain fields such as proposal number, the date, the project title, his name, department, institution, and so on. The system can make these inferences from the name of the person (Hengst)

![](/api/attachments/8TR5EK6S/fulltext/images/0dd3637ffd0639982387edca537b80a104dcbed412744178b4e97197b5604939.jpg)  
Figure 8. Planner Demonstration

![](/api/attachments/8TR5EK6S/fulltext/images/d8b6fb1c37aa1734cc6e8883ceee59ed51f981092526e711346bf177e44c9fa1.jpg)  
Figure 9. The DTIC Search

who is logged in, and the domain knowledge. The COR then fills in the remaining fields. The inference engine invokes the Purchase Request and Commitment and the Work Unit Summary forms. Processing these forms is similar to the project evaluation form and the same remarks also apply. The final step in preparing the acquisition package is to prepare an approval letter. In the AIRMICS functional structure, the approval letter would be listed as an information dependency for the subfunction, "prep\_appr\_letter." Therefore, if a form letter already exists, the inference engine would invoke the editor with the form letter already loaded. Further, the inference engine is also capable of automatically filling the address fields of the letter, so that the COR's responsibility is reduced to verifying its correctness, printing it and having it signed by the director.

This scenario has illustrated the use of important AEI components such as the: (1) procedure planner, (2) inference engine, (3) functional and organizational structures, (4) DTIC search application, (5) the forms component, and (6) information. Other system functions such as utilities, the ability to add comments to office procedures, the personnel allocation procedure have not been illustrated for brevity.

## 8. Discussion of the Research and Conclusions

STARTING WITH THE LIMITATIONS OF PRIOR RESEARCH and a model of the office, we have developed an office architecture intended to deal with the problems facing many offices today—overabundance of information, confusion regarding responsibilities, software proliferation, and EUC programming. The model that formed the basis for our architecture has been derived by considering the nature of the office. Integration across domains was achieved simultaneously through the interface, the inference engine, the domain knowledge, and the application structure. The domains in the architecture were derived from office studies, ensuring that the architecture will address needs of the general office user. Intelligence is supplied through the event handler as well as through the static functional structure representing basic relationships among activities in the office. The structure is developed from functional primitives. The same primitives are used for different offices, ensuring that the same reasoning mechanism (the planner) can be employed. The event handler, the functional structure, and the planner were adapted from CD theory. The application structure makes use of existing tools and utilities. The inference engine calls the executable nodes in the functional structure and which are present in the application structure. Tools and utilities in the application structure can also be directly invoked by users. Thus, the application structure is linked loosely with activities in the functional structure, ensuring a good design from a software engineering perspective.

![](/api/attachments/8TR5EK6S/fulltext/images/358c8a4e7002755e73a4d483a9fdce84415da8f697aaf6ec0d53fe272fcadc2a.jpg)  
Please enter your comments about the project  
Figure 10. The Project Evaluation Form

Further, each of the components in the architecture (except for the event handler, the planner, and the functional structure which must be upgraded together) can be independently upgraded.

The features of AEI described above lead to an office system that: is integrated across domains; is integrated with the application structure; is reasonably intelligent; can satisfy requirements of Type I offices; and is user-friendly. User-friendliness stems from its natural language interface and also from the fact that users can explore the functional structure (they can ask questions such as, "What is a Bill of Materials?") and add comments to procedures in an organized fashion. Our research is applicable to any Type I office; however, once a system is implemented, only the event handler (not the object-action libraries), the planner, decision models, and the tool structure can be ported intact, subject to hardware/software considerations. This is a strong argument for having models in the first place.

There are, however, certain limitations and design considerations that have been omitted from our architecture. The major limitation is the limited intelligence of the system. The inference engine can make inferences only of the type illustrated in Table 4. Other limitations that remain to be addressed are that it is a single user system, the planner cannot handle multiple interacting subgoals, the exception handler is limited in functionality and finally, the architecture is geared for Type I routine office tasks. This last limitation is dependent on the degree of intelligence that can be supplied by the knowledge base. Office systems with commonsense world knowledge can conceivably take on Type II office tasks. We hope our research is a forerunner for such systems.

## NOTES

1. The model and architecture are referred to as the AEI model and architecture because they originated in an attempt to model office work based on state transitions in a predicate with Agent, Entity (or office object) and Information as arguments [35].

2. Gerson and Star [23] reported on the negotiation process that accompanies the pricing of medical services. They did not provide samples of the disease-rate classification that they refer to in their study or provide details on how the office dealt with the due process.

3. Essentially the deeper meaning of an office model.

4. Both Turbo Prolog and Turbo Prolog Toolbox were registered Trademarks of Borland International at the time of this research.

## REFERENCES

1. Ader, M., and Tueni, M. An office assistant prototype. In Esprit 87, Achievements and Impacts. New York: North Holland 1987, 1205–1225.

2. Aiello, L.; Nardi, D.; and Panti, M.; Modeling the office structure: a first step towards the office expert system. ACM SIGOA Conference, 1984, 25–32.

3. Amaravadi, C. Towards a conceptual model for the office: an integrating approach. Unpublished doctoral dissertation, Tucson, University of Arizona, 1989.

4. Amble, T. Logic and databases. In Logic Programming and Knowledge Engineering. Reading, MA: Addison-Wesley, 1987, 146–166.

5. Barber, G. Embedding knowledge in a workstation. In N. Naffah, ed., Office Information Systems. New York: North Holland, 1982, 342–354.

6. Barber, G., and Hewitt, C. Foundations for office semantics. In N. Naffah, ed., Office Information Systems. New York: North Holland, 1982, 363–382.

7. Bobrow, D., and Winograd, T. An overview of KRL, a knowledge representation language. In R.J. Brachman and H.J. Levesque, eds., Readings in Knowledge Representation. Los Altos, CA: Morgan Kaufman Publishers, 1985, 263.

8. Bracchi, G., and Pernici, B. The design requirements of office systems. ACM Transactions on Office Information Systems, 2, 2, (April 1984), 151–170.

9. Bracchi G., and Pernici, B. SOS: a conceptual model for office information systems. Database (Winter 1984), 11–18.

10. Chang, A. An architecture for electronic messaging in organizations: a distributed problem solving perspective. Ph.D. dissertation, Tucson, University of Arizona, 1987.

11. Conrath, D.W. Office modeling: comments about the present and the future. IEEE Technical Committee on Office Automation Newsletter, 1, 2 (May 1987), 2–10.

12. Croft, B.W., and Lefkowitz, L.S. Task support in an office system. ACM Transactions on Office Information Systems (July 1984), 197–212.

13. Croft, B.W., and Lefkowitz, L.S. Using a planner to support office work. ACM SIGOIS Conference on Office Information Systems, March 1988, 55–77.

14. Dahl, V. Logic programming as a representation of knowledge. Computer (October 1983), 106–111.

15. Date, C.J. An Introduction to Database Systems. Reading, MA: Addison-Wesley, 1986.

16. Ellis, C. A. Information control nets: a mathematical model of office information flow.

Proceedings of the First ACM Conference on Office Information Systems, June 1982.

18. Ellis, C.A., and Nutt, G.J. Office information systems and computer science. ACM Computing Surveys, 12, 1 (March 1980), 3–36.

19. Engel, G.H.; Groppuso, J.; Lowenstein, R.A.; and Traub, W.G. An office communication system. IBM Systems Journal, 18, 3 (1979), 403–431.

20. Fikes, R.E., and Henderson, A.D. On supporting the use of procedures in office work. Proceedings of the AAAI, August 1980, 202–207.

21. Fillmore, C. The case for case. In E. Bach and R. Harms, eds., Universals in Linguistic Theory. New York: Holt, Rinehart, and Winston, 1968, 1–88.

22. Gibbs, S.J. Conceptual modelling and office information systems. In D. Tsichritzis, ed., Office Automation. New York: Springer-Verlag, 1985, 193–225.

23. Gerson, E.M., and Star, S.L. Analyzing due process in the workplace. Third ACM SIGOIS Conference, Providence, Rhode Island, October 6–8, 1986, 70–78.

24. Hammer, M., and Kunin J.S. Design principles of an office specification language. Proceedings of the National Computer Conference, 1980, 541–547.

25. Hewitt, C. Offices are open systems. ACM Transactions on Office Information Systems (July 1986), 271–287.

26. Hewitt, C.; Attardi, G.; and Simi, M. Knowledge embedding in the description system Omega. Proceedings of the AAAI (August 1980), 157–164.

27. Kaye, R.A., and Karam, G. Cooperating knowledge-based assistants for the office. ACM Transactions on Office Information Systems, 5, 1 (October 1987), 297–326.

28. Konsynski, B.R.; Bracker, L.C.; Bracker, W.E. A model for specification of office communications. IEEE Transactions on Communications, COM-30, 1 (January 1982), 27-36.

29. Maes, P. Goals in knowledge-based office systems. In J. Laubsch, ed., 8th German Workshop on Artificial Intelligence, Wingst/Stade. New York: Springer-Verlag, October 8–12, 1984, 20–29.

30. Malone, T.W.; Grant, K.R.; Lai, K.-Y.; Rao, R.; and Rosenblitt, D. Semi-structured messages are surprisingly useful for computer-supported coordination. Proceedings of the Conference on Computer Supported Collaborative Work, Austin, TX, December 1986, 102–115.

31. Marcke, K.V.; Jonckers, V.; and Daelemans, W. Representation aspects of knowledge based office systems. In Esprit 87, Achievements and Impacts. New York: North Holland, 1987, 1226–1238.

32. McLeod, R., and Jones, J.W. A framework for office automation. MIS Quarterly (March 1987), 87–104.

33. Mintzberg, H. The Nature of Managerial Work. Englewood Cliffs, NJ: Prentice-Hall, 1973.

34. Morgenbrod, H.G., and Schwaertzel, H.G. The degree of office automation and its impact on office procedures and employment. Computer Networks (1980), 3–11.

35. Naylor, A.W., and Volz, R.A. Design of integrated manufacturing system control software. IEEE Transactions on Systems, Man, and Cybernetics, 6 (November–December 1987), 881–897.

36. Panko, R.R. Serving managers and professionals. Proceedings of the Office Automation Conference, San Francisco, 1982, 97–103.

37. Poppel, H.L. Who needs the office of the future? Harvard Business Review (November–December 1982), 146–155.

38. Sasso, W.C.; Olson, J.R.; and Merten, A.G. The practice of office analysis: objectives, obstacles, and opportunities. IEEE Technical Committee on Office Automation Newsletter, 1, 2 (May 1987), 11–24.

39. Schank, R.C. Conceptual dependency: a theory of natural language understanding. Cognitive Psychology, 3 (1972), 552–631.

40. Schank, R.C., and Abelson, R.P. Scripts, Plans, Goals and Understanding. Hillsdale, NJ: Lawrence Erlbaum and Associates, 1977.

41. Schank, R.C., and Riesbeck, C.K. Inside Computer Understanding. Hillsdale, NJ: Lawrence Erlbaum and Associates, 1981.

42. Schank, R.C., and Wilensky, R. A goal-directed production system for story understanding. In D.A. Waterman and F. Hayes-Roth, ed., Pattern-directed Inference Systems. New York: Academic Press, 1978, 415–430.

43. Skinner, B.F. Science and Human Behavior. New York: Macmillan, 1953.

44. Software Engineering Research Center. An information systems plan for the Army Institute for Research in Management Information, Communications and Computer Science. Internal Report, Georgia Institute of Technology, Atlanta, June 1988.

45. Sprague, R.H., and Carlson, E.D. Building Effective Decision Support Systems. New York: Prentice-Hall, 1982.

46. Steels, L. Tutorial on the KRS concept system. Technical Report, VUB AI Lab, Pleinlaan, Brussels, 1987.

47. Suchman, L.A. Office procedure as practical action: models of work and system design. ACM Transactions on Office Information Systems, 1, 4 (October 1983).

48. Suchman, L.A., and Wynn, E. Procedures and problems in the office. Office: Technology and People, 2, (1984), 133–154.

49. Thachenkary, C.S., and Conrath, D.W. The office activities of two organizations. In N. Naffah, ed., Office Information Systems. New York: North Holland, 1982, 452–469.

50. Tsichritzis, D. Form management. Communications of the ACM, 25, 7 (July 1982), 453–478.

51. Zisman, M.D. Use of production systems for modeling asynchronous, concurrent processes. In D.A. Waterman and F. Hayes-Roth, eds., Pattern-directed Inference Systems. New York: Academic Press, 1978, 53–68.

## APPENDIX: The Different Views of the Office

A view is a perspective of the office that leads to the development of a particular type of model and ultimately an office system. The several views in the literature are coalesced and described informally below:

Forms: Forms are the physical groupings of data items found in most offices and used as a structured means of official communication. With this view, forms are studied with an emphasis on their data structures, operations, and routings. Models are developed for these aspects with the goal of automating form processing. This is a view exemplified by Office Talk-D system.

Data: This refers to the view that modeling an office consists of modeling the data used in it. The emphasis is on storage and retrieval of data. The data-oriented view has much in common with the database approach in MIS literature. To a limited extent models based on the data-oriented view have also attempted to include those procedures related to changes in the values of the data items. The Office Data Model (ODM) is representative of this view.

Information: In the information view, office information is analyzed with respect to content, flow patterns, storage and retrieval, and so on, and appropriate models are designed. Information models are distinguished from the data models in that they do not discriminate among data types, treating all as text. An item of information, such as “9 percent interest rate,” is treated as text and therefore cannot be directly used in a computation. Very frequently, this view has resulted in document-oriented models.

Procedures: Procedures are predefined sequences of actions for achieving a particular result. Offices have procedures that have to be followed for approving loans, purchasing equipment, hiring new employees, and so on. An analysis based on the procedural view identifies and describes the procedures followed in offices. This is a more general view than the other three views as procedures can involve forms, data, information, or all three. The activity view is related to the procedural view in that activities are part of procedures. Some researchers have viewed operations such as filing, retrieving, mailing, and the like as low-level procedures.

Functions: This is the view that offices and office workers have functions that are a direct consequence of the goals of the office. Functions are descriptions of the work done in the office at the highest level of abstraction. Functions exist in a hierarchy that usually corresponds to the traditional organizational structure. At the lower levels, functions consist of procedures.

Agents: This is the view that office work is executed by the office worker in relationship to the worker's assigned tasks and other office workers. Models based on the agent-oriented perspective are aimed at describing the task assignments of workers and how the assignments change dynamically according to the situation.

Communications: The communications view treats office work as being a result of communications among office workers. Since messages are the unit of communication, models based on this view are focused on managing messages. The Information Lens and the AiMail projects are characteristic of this approach. A recent development in this area has been the introduction of Group Support Systems.

Decisions: This is a view native to the MIS literature rather than the office automation literature. According to the decisions perspective, office activity consists of decision making. Suitable support is provided for the various steps of the decision-making activity.

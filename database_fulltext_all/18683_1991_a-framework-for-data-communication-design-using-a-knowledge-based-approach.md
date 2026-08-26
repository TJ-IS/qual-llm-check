---
otero_id: 18683
otero_key: "F6797M3M"
title: "A framework for data communication design using a knowledge based approach"
authors: "Sven A. Carlsson; Lars Fernebro; Dipak Khakhar"
year: "1991"
journal: "Information & Management"
doi: "10.1016/0378-7206(91)90013-r"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Case study

# A framework for data communication design using a knowledge based approach

Sven A. Carlsson, Lars Fernebro and Dipak Khakhar

Department of Information and Computer Science, University of Lund, S-22362 Lund, Sweden

This article addresses the problems of applying a knowledge based approach to data communication design. A prototype has been developed in order to derive a framework for the conceptual design of such systems. Problems of partitioning and formalizing the design process are discussed. The control of the system and user interface are found to be critical issues.

Keywords: Data communication design, Network design, Knowledge based systems, Expert systems applications, Knowledge acquisition.

![](/api/attachments/F6797M3M/fulltext/images/4582c679b23461560dedf81047ee9c362324dda2f59227d03301ab08fcb81a9f.jpg)

Sven Carlsson is an Assistant Professor at the Department of Information and Computer Science, University of Lund, Sweden. His current research interests include decision support systems, knowledge-based support systems, executive information systems, and strategic information systems. He has been a Visiting scholar at the University of Arizona, Tucson, and a visiting professor at the University of Southern California, Los Angeles. He has published in Journal of Manage-

ment Information Systems, Scandinavian Journal of Information Systems, and international conference proceedings. He is a member of IFIP WG 8.3 on Decision Support Systems and TIMS College on Information Systems.

![](/api/attachments/F6797M3M/fulltext/images/a14bbd6ad177b53505caa3ddb6048277a434ed7a8a454d1fb12e519d4b816bfb.jpg)

Lars Fernebro is an assistant professor at the Department of Information and Computer Science, University of Lund, Sweden. His current research interests include decision support systems, knowledge-based support systems, data communications, and strategic information systems.

## 1. Introduction

Complexity of data communications networks is increasing rapidly with the introduction of new functions and services, increased connectivity, the advent of new technology and components, and demands for interoperability. With the increased importance and criticality of data communication in and between organizations, there is a growing need for a better understanding of the technology. The problems within the data communication area may be classified by applying generic types of problem solving $[10]$ :

\- Diagnosis. From observables, infer its malfunctions in the network, debug these by prescribing remedies, and repair it by executing a plan involving the remedies. The latter requires planning, that is, the design of suitable actions.
- Design by configuring a network subject to given requirements and constraints.

\- Control. This includes interpreting data from sensors in the network, predicting likely consequences of this given situation, and comparing these observations to detect vulnerabilities (monitoring).

![](/api/attachments/F6797M3M/fulltext/images/d8001db99b7b0360bcb243475767b95afd6c42fc5e99d5f8bd9ef5eb4a112d8f.jpg)  
Dipak Khakhar holds B.Tech. (Honours) degree in Metallurgical Engineering and Management from Loughborough University of Technology, England and Ph.D. in Information and Computer Science from Lund University, Sweden. Currently, Dr. Khakhar is head of the department of Information and Computer Science at Lund University. Dr. Khakhar is a board member of The Swedish Computer Society and national representative from Sweden in International

Federation for Information Processing General Assembly (GA) and Committee for Data Communication (IFIP-TC6). Dr. Khakhar is a governor of ICCC (International Council For Computer Communication). Dr. Khakhar is editor of the books, Information Network and Data Communication, I, II & III published by North-Holland.

Designing data communication architectures is becoming increasingly expensive and time-intensive. The complex design process demands the scarce expertise of data communication planners and network architects. Knowledge based systems allow implementation of procedures where emphasis is placed on experience and knowledge about situations and events surrounding them. By articulating and transforming expert knowledge of the network and its operation into suitable representations, the knowledge can be applied to the tasks. This enhances expert scope and effectiveness.

A knowledge based approach can significantly reduce the time and cost needed to develop a data communication architecture and improve the design quality. Once an architecture is designed using a knowledge based system (KBS), changes in assumptions or design philosophy can be tested quickly by changing one or more constraints. Another benefit is the possibility of justifying a selected architecture by performing sensitivity analysis and producing assessment of the current situation.

Some relevant expert systems and KBS have already been developed for networks, for example:

\- Network troubleshooting. Bell Laboratories developed a system for fault diagnosis in telephone nets [22]. COMPASS (GTE Corporation) is an expert system that diagnoses fault messages and prescribes remedies for telephone switch systems [7]. A troubleshooting system for GAN (Global Area Network) is NDS, which applies expert fault diagnosis strategies to recommend appropriate tests to localize faults in a network [23]. NTC is an expert system for troubleshooting in DECnet and Ethernet [20]. KBSKV is an expert system being developed by The Swedish Telecom for fault diagnosis for electromechanical telephone exchanges [19]. ACE (AT&T) provides troubleshooting reports and analyses for telephone cable maintenance [19].

\- Network administration. Nemesys is a network management expert system developed by AT&T for optimizing their long-distance network in high volume traffic [15]. VEX/ATL is an expert system developed by The Swedish Telecom for network route configuration [19].

\- Network design. AT&T developed an expert system for network design. It helps a user to determine a basic topology more rapidly. Thus more time can be spent on doing iterations, looking at alternatives, and tuning the design. BBN has developed an expert assistant tool, called Designet, which helps to design packet switched data networks [15].

It is clear that most expert systems for data communication have been developed for problem types like diagnosis, control, debugging, and planning. The potential benefits of these expert systems are mainly in improving quality of service and saving cost through optimal use of the available resources.

This article presents and discusses experience gained in a project on data communication design using a KBS approach. A structure is presented that identifies the key components of the data communication design process and upon which an expert system implementation can be based. The project presented is a joint venture between The Swedish Telecom and the Department of Information and Computer Science, University of Lund.

A relevant and critical problem for the actual department of The Swedish Telecom is in the design of communication networks for external customers like private and public organizations, ranging in size from small to very large. Design for the department includes both telephone and data communication design, with the latter being the hardest problem of these two.

The current situation for the department is characterized by: (1) a growing demand from customers for services, including data communication; (2) growing competition for The Swedish Telecom due to deregulation of products and services; and, (3) expertise on data communication and especially data communication design being a scarce resource.

The prototype developed to study the data communication design problems has been built through an iterative process that can be categorized into the following five phases: identification, conceptualization, formalization, implementation, and testing [2]. Each is now discussed:

Identification of the problem-domain and subproblems was carried out through discussions between experts and researchers. It included discussion of available resources like computers and software, and expert time constraints. One of the most difficult problems was in identifying and restricting the problem-domain and its subproblems.

Conceptualization of the problem-domain includes decisions on what concepts, relations, etc, are needed to describe data communication design for the chosen subproblem area. A major part of the knowledge acquisition was carried out in this phase. Knowledge was captured using different methods and techniques such as:

\- Design while “thinking aloud” in two different forms; in one, the expert resolved design problems, and in the other the expert solved design problems given by the researchers.

\- Discussion in the research group and with the experts on relevant and critical concepts in the design process.

\- Reading literature on different aspects of data communication design.

Implementation of rules, knowledge, etc., is the process of turning the expert knowledge into formalized knowledge and implementing the formalized knowledge using a knowledge based system shell developed by the research team.

Testing of the prototype; i.e. evaluation of its performance. Knowledge gained in this phase was also used in the conceptualization phase.

## 2. Data communication design

## 2.1. Data communication design problems

For data communication design, the process includes at least the following major phases:

Strategic design, which describes how to design current information flow with respect to the possibilities and limitations of Information Technology (IT). These strategical decisions focus on how to choose a profit maximized information flow in an organization and between organizations The decision includes factors like: how can we use IT; how are investments paid off; how to maintain information channels; and how to link networks to one another. It also includes an understanding of the types of applications and how these can be supported by a new communication infrastructure. These decisions are both business and technically oriented. There is a growing body of articles and books focusing on such problems, opportunities, and obstacles; see for example [3], [4], [11], and [16].

Conceptual/logical design, which defines the design of a specific data communication network in general terms (not product specific). The design includes decisions on how to connect user equipment to different servers so that the requirements are fulfilled. Problems at this level includes how to choose suitable clusters, switching functions, network functions, and conversions due to different protocols, etc. The output of this phase is a logical model of the data communication network.

Physical design or construction, i.e. implementing the conceptual model of the data communication network. To this area belongs problems like choosing specific equipment such as cables, multiplexers, modems, switches, etc. It also includes the problem of how to optimize the network economically.

In reality, design is a complex, iterative, and (in most cases) an evolutionary process. It is a continuous process in an organization. It is unlikely that an organization will plan for a communication network from scratch. In most cases, the organization is interested in modifying an existing environment to enhance facilities for tuning or to reduce cost. The organization may increase flexibility and functionality by replacing old products by new and more effective ones.

Formally, an organization's overall design problem is to maximize profit subject to given constraints. Of the three design phases, our project addresses the two last ones. This means that our design problem is to minimize the cost subject to given data communication requirements and constraints.

## 2.2. Steps in data communication design suggested in literature

Those design phases just discussed are at a general level; the phases must be formalized in detail in order to determine the steps in a design process. In the literature there are very few formal descriptions of the detailed stepwise design of data communication processes. Cynar et al. [5] give the following steps when a human expert designs a network:

User requirements. The user's needs are reviewed for feasibility and consistency.

Traffic requirements. Take the realizable requirements and calculate the traffic required, based upon the number of channels, type of data, data rate, and usage.

Network topology. Interconnect the nodes into the network based on nodal location, traffic, or alternate paths required.

Trunk-line selection. Select the most cost-effective trunking facility between the interconnected nodes. Nodal-equipment selection. Nodal equipment (modems, multiplexers, switches, etc.) is selected based on bandwidth requirements, functional requirements (contention, switching, protocols), special feature requirements (auto fallback, redundant logic, reserve bandwidth), and the designer's knowledge of product availability.

Design presentation. Itemize the services and equipment to be acquired, calculate various costs and generate a network diagram.

Yet another model for designing and setting up a data network is given by Mantelman [15]: (1) clarify the network's purposes; (2) inventory the resources, such as knowledge, contacts, and so on; (3) identify needed resources unavailable locally; (4) select a suitable network structure; (5) assess what kind of network user each person (node) in the network may be expected to be, and (6) decide which networking process will be most effective.

Procedures given by Cynar et al. [5] and Mantelman [15] indicate what data communication design is about. However, to develop a KBS for data communication design requires a more refined description.

## 2.3. Data communication design by human expert

Finding the facts and relevant rules is the most difficult phase in designing an expert system. The reason is that the “human knowledge” that is represented as explicit algorithms is less than 1% of the whole; most of it is of a heuristic nature [18]. Most of the heuristics used by an expert are rules that the expert is unaware of. He has a large number of rules stored and available and is very good at using this knowledge. However, when he has to state them explicitly it becomes difficult.

To enhance our understanding of the data communication design process, a number of problems were posed to network experts in The Swedish Telecom. The problems varied in specification and complexity. For example:

\- Centralized computing. A number of dispersed terminals are to be connected to a central computer.

\- Terminal equipment is to communicate with two computers.

\- A company with an SNA environment has bought another company where a VAX/780 has been used for data processing. These two processing environments are to be integrated.

\- A company has an SNA environment. The host computer is located in the data processing department and the terminals are dispersed in different administrative departments located in two buildings and at different manufacturing plants. The administrative personnel have bought a number of PCs. These are connected in separate LANs. PCs are to be connected to the host computer so that they can also be used as terminals.

The first two problems are very general. They do not mention current devices or how they are connected to the host computers today. The last two problems are, on the other hand, more specific.

Our study of the experts' way of solving the design problems showed that regardless of its complexity, the expert solves it employing a certain strategy. He reasons and argues with his client in order to establish possibilities and constraints that the client may have. The expert has knowledge about a number of products and uses this to design and evaluate different possible solutions. He also takes into account client investment and tries to utilize the products that already exist in the network. Different solutions are presented: first, in a sketchy form, and then, through elaboration, in a more precise and detailed form.

The result of the study of the problem solving process was used in several ways. First, it yielded rules used by the experts in solving design problems. It not only gave the stepwise problem solv-

Table 1
Examples of primitives

ing methods but also guidelines for dividing a complex design problem into a number of subproblems or knowledge areas; it thus provided an architecture for an expert system for data communication design. The vocabulary of the experts during the design process was used as a base for developing a language for data communication design. The inference mechanism of the developed system is also based on the experts' way of solving problems.

## 3. Knowledge based systems for data communication design—a framework

## 3.1. Language for description and manipulation

If a knowledge based system is to be accepted, it must fit the manner an expert or user proceeds with the design process. The system must allow an expert to change rules in the system dynamically and easily, often without any help from a knowledge engineer. In order to facilitate this, a language has been developed for describing and manipulating data networks. Some of the primitives of the language are shown in Table 1. As can be seen from the table, the network manipulating language is divided into two categories. The first contains “instructions” given to the system for defining and manipulating a network; for example, connect a terminal to a server, disconnect a terminal or group of terminals.

The second category of the language consists of primitives for storage and retrieval of different network problems (configurations) and different solutions of a specific problem. Instructions in this category may be used for storing or initiating a stored problem. There are also instructions for piggy-backing a problem; for example, undo(knowledge\_area) or go\_back. To this category belong also instructions associated with the control and behaviour of the system during the design process. For example, a user can follow each step in the design process by using the instruction show(on). Yet another example is the instruction do(knowledge\_area); for activating a certain area and solving only a part of the problem.

<table><tr><td colspan="2">Category 1</td></tr><tr><td>create_object (Name)</td><td>Insert a new object</td></tr><tr><td>create_anonymous_object (Name)</td><td>Insert a new object of unspecified type</td></tr><tr><td>delete_object (Name)</td><td>Delete an object</td></tr><tr><td>add_value (Obj,Att,Val)</td><td>Insert new value to attribute&#x27;s value list</td></tr><tr><td>add_attribute (Obj,Att)</td><td>Insert new attribute</td></tr><tr><td>delete_attribute (Obj,Att)</td><td>Delete an attribute</td></tr><tr><td>delete_value (Obj,Att,Val)</td><td>Delete a value from attribute&#x27;s value list</td></tr><tr><td>Eqpt is Type</td><td>True if Eqpt is an instance of Type</td></tr><tr><td>exists_object (Obj)</td><td>True if object exists</td></tr><tr><td>exists_attribute (Obj,Att)</td><td>True if object has specified attribute</td></tr><tr><td>exists_value (Obj,Att,Val)</td><td>True if object has specified value for attribute</td></tr><tr><td>link(N1,Equipment1 and N2,Equipment2)</td><td>Connect (a number of pieces of) equipment</td></tr><tr><td>linked(Equipment1 and Equipment2)</td><td>True if two pieces of equipment are connected</td></tr><tr><td>different(A,B)</td><td>True if A is not equivalent to B</td></tr><tr><td>is_an_instance (Equipment,Type)</td><td>True if equipment has specified type</td></tr><tr><td>net_compatible (D1,D2)</td><td>True if D1 &amp; D2 can be in a com.network</td></tr><tr><td>disconnect(N,Equipment1 from Equipment2)</td><td>Disconnect two pieces of equipment</td></tr><tr><td>copy(from(Frame1 to Frame2)</td><td>Copying of frames</td></tr><tr><td>get_all_atts (Eqpt)</td><td>Get all attributes for Eqpt</td></tr><tr><td>get_an_att (Eqpt,Att,Value)</td><td>Get Value for attribute Att</td></tr><tr><td colspan="2">Category 2</td></tr><tr><td>do (knowledge_area)</td><td>Execute rules of a knowledge area</td></tr><tr><td>delete (database)</td><td>Clear configuration specification area</td></tr><tr><td>go_back</td><td>Undo rules of previous knowledge area</td></tr><tr><td>load (database)</td><td>Load specification from file</td></tr><tr><td>save (database)</td><td>Save specification to file</td></tr><tr><td>show (on/off)</td><td>Toggle stepwise explanation</td></tr><tr><td>undo (knowledge_area)</td><td>Undo rules of a knowledge area</td></tr></table>

![](/api/attachments/F6797M3M/fulltext/images/ce51f75cfab8ee4af70146175828bc8d96cd3b4aeb7300d7022f36d48f946e29.jpg)  
Fig. 1. Modules and knowledge bases in the prototype.

## 3.2. Modules of a knowledge based system for data communication design

Approaches used by human experts in solving network design problems showed that there are several technically feasible solutions for most problems. An expert chooses one or more feasible solutions and eliminates infeasible solutions. An expert argues for selected solutions in functional and technical as well as economic terms. He compares the solutions. In order to design a system that would fit the way the experts solve design problems and suggest the most suitable solution, the system was decomposed into a number of modules and knowledge bases (see Figure 1).

## User-system interface

We strived for a user-friendly interface with the following properties:

Menu driven interaction control. Besides being easy to use and help the user to recognize and remember possible operations, menus contain information on stored product types.

\- Interruptability. It is possible to interrupt the design procedure at any time. This means that the workspace is saved with the users' requirements and partial solutions, in order to allow the user to continue the procedure on a later occasion.

\- Relevant questions. The system does not ask for data that is irrelevant to the design process nor ask questions that are out of context. To accomplish this, rules should be grouped into modules or knowledge areas that are natural to the user and input should be driven by design rules.

\- Graphics. The system uses graphical representation both in the requirement and the solution stages; that is, requirements can be partly specified using graphics, and results are presented graphically.

The user has a choice concerning the level of interaction with the system, specifically,

\- None, that is, the system simply provide the final configuration; or

\- Eavesdrop, that is, the user is informed at each step of the design process. With the “eavesdrop” capability the user is made aware of the problem flow and sees various intermediate results. In some situations, the user may wish to override the actions taken by the expert system. At any point, the user is able to review and modify any part of the problem status.

## Problem specification module (Problem Specific)

The problem specification module contains functions for: input of a customer's available equipment and connections; input of requirements, new equipment, and preferred type of solution, and input of environmental factors like geographical location of nodes and description of localities.

This module also determines the purpose of a session; the desired amount of user interaction in the problem-solving process, and use guidance in the network design process.

The required input is solution-driven. As in other knowledge based systems, the system asks questions about facts it needs for advancing the design process, i.e. the requested input is “solution-driven”.

## Configuration module (Configure)

The configuration module contains functions for generating new solutions, re-configuration, and test of solutions. The module makes decisions such as: whether a switching function is needed, that is, whether many-to-many interaction is required in the communication system; the need for possible enhancements of links with multiplexors and/or concentrators in order to optimize bandwidth; how to select trunk-lines based on traffic requirements and nodal locations; and the need for programs and equipment for protocol conversion, for example, selection of modems based on trunk-line selection and nodal location.

The module interacts with the system-user for guidance as well as control of the design process. For example, a solution may not exist that satisfies the stated requirements and constraints. This is presented to the user, who must then take appropriate action; for example, change the constraints or terminate the session.

The configuration module establishes an initial configuration, a base solution. This is then evaluated. During the evaluation process the system may suggest alternative solutions. The user may accept, reject, or suggest an alternative. For example, the system may suggest particular switching equipment. The user may accept the suggested equipment, or reject the suggested equipment or suggest another. The user of the system may also accept only part of a suggested solution. For example, the user may accept the proposed switching equipment but alter the number of communication lines in it.

## Cost calculation and pricing

The modules for cost calculation and pricing utilise the product data base to calculate the cost of a solution. These modules use standard calculations and can be implemented in procedural programming languages, modelling languages, or spreadsheet programs.

## Product types and product data bases

The design process selects different types of equipment during the initial phase. Types selected may be switching equipment, multiplexer, modem, and so forth. In this phase, the system is interested only in the functionality of a certain kind of equipment. Properties of different types of equipment are stored in the product-type data base.

In the next phase of the design process, desired properties of the selected product-types are matched with the values for specific products, as stored in the product data base, and appropriate products are chosen.

Data about different types/classes of products and data about specific items of equipment in the data bases are represented using frames. A user-friendly frame editor has been developed. This makes it possible for a user to create, change, and delete frames, attributes, and values in the frames.

## Analysis of alternatives

The function of the module for analyzing alternatives is to give pro and con arguments for various solutions. The module performs sensitivity analysis and produces an assessment of the current solution. If all guidelines and objectives are met, then we have a satisfactory solution. The assessment can also identify some deficiencies in the current solution along with recommendations for changes. The module is also able to detect “overdesigned” solutions as well as those that are “underdesigned”. An overdesigned solution meets all of the user requirements, but is too costly or underutilized.

![](/api/attachments/F6797M3M/fulltext/images/0c43787e248e6f02e03bcca3f6dcfb0caafaedcb45b6bf9ab6219c48b7856329.jpg)  
Fig. 2. The language-tool continuum, as a way to classify the various AI languages and tools (adapted from [8] and [9]).

## 4. Implementation options

## 4.1. Expert system shells vs. programming languages

In the literature on expert systems one often finds claims for using shells, tools, and development environments instead of high-level languages in building expert systems. The use of tools, shells, or environments can speed up the building process and thereby lower the cost of a project. Despite this we have chosen a high-level programming language, Prolog (see Figure 2).

Several factors contributed to the choice of Prolog for development of our expert system. First, available resources; we had a limited budget, which ruled out large expert systems tools. We also wanted to have the possibility of discarding the prototype and choose a new tool. Thus, the chosen tool should be inexpensive. Second, changeability and flexibility; we wanted to have an environment that allowed us to change the structure of knowledge representation and control strategies. Third, intended users of the system were experts in data communication and also persons responsible for customer contacts. As a consequence of their work environment, the system had to be portable to make the distribution of the system to different administrations as smooth as possible. Diffusion and portability of the system was a major goal. Consequently the system should be easy to implement in different local environments and adaptable to the locally used equipment, such as personal computers.

Given the constraints, in terms of money and computer environment, this can be summarized as the distinction between a customized and customizable system. Customizable refers to how well and easily a system can adapt to a specific area or problem-domain and also how easy it is to make changes due to new or changed requirements. By building our system in Prolog we created an environment which was more customized than the shells we evaluated. It should be noted that in general a system developed in Prolog requires more knowledge of the builder and that the development is more time consuming.

We tried to use an inductive expert system shell for knowledge acquisition. It generates rules for the expert system from examples given by the expert. This did not work out well, because the expert did not feel comfortable with the shell. This might be due to the type of problem we are addressing; design is a problem situation characterized by the fact that for most examples there are several feasible solutions, not only one.

## 4.2. Knowledge representation and control strategies

The following knowledge was found to be most critical:

(1) knowledge or facts about different types/ classes of products, that is, knowledge to be stored in the product type and product data bases, and,

(b)  
![](/api/attachments/F6797M3M/fulltext/images/ee7d9c18753d84723958974c4593985704d4da1d4e055d581ebcb5d51184073c.jpg)  
Fig. 3. An example of hierarchy and frame.

<table><tr><td>Name</td><td>Personal Computer</td></tr><tr><td>ISA</td><td>COMPUTER</td></tr><tr><td>Single user</td><td>Yes</td></tr><tr><td>Function</td><td>Ask_user</td></tr><tr><td>Number</td><td>Ask_user</td></tr></table>

(2) expert knowledge on how to solve a problem. These rules cover all phases in the design process, from the first phase, requirement specification, until one or more solutions have been generated.

This knowledge must be represented in the system in a suitable representation that is rich enough to express knowledge of the problem area, can easily be accepted by the expert, and does not substantially slow down performance.

The representational form for facts was chosen to be frames. They are organized in inheritance hierarchies, where a frame lower in the hierarchy inherits properties from frames higher up. Figure 3a shows an example of such a structure, with the root NODE. Children of NODE are COMPUTER and TERMINAL. Further COMPUTER is parent of PC.

NODE, COMPUTER, TERMINAL and PC are all objects represented by frames. Each frame has a unique identifier and a set of possible attributes. Figure 3b illustrates the frame for PC which isa type COMPUTER and has three other attributes. The attribute single\_user has value yes. The attributes function and number have a value ask\_user, which is a procedure used when values of these properties are required by an executing rule. When constructing a frame for an object, the designer can select from a number of default methods similar to ask\_user or specify a completely new method (define a procedure). Considering the structure given in Figure 3a, if an IBM-XT frame of type PC is created, the IBM-XT frame will inherit attributes of PC, that is, inherit single\_user, function, and number.

At the beginning of the project a simple forward chaining inference mechanism was developed; this was considered to be the most suitable control strategy for a design problem of our type. During the development of the prototype we found that expert knowledge on data communication design comprised both structural knowledge (e.g., Which conceptual design configurations are possible? and Which equipment is to be selected in a given situation?) and procedural knowledge (e.g., In which order must design decisions be made?). The procedural knowledge is hard to represent with forward chaining; it results in large condition parts of the rules and can easily lead to inconsistency. Therefore an procedural expert system approach was selected [6].

The knowledge base of the system contains facts about a problem and a set of specialized inference procedures called knowledge areas (KA). A KA consists of an invocation part and a body. The invocation part is an arbitrary logical expression that may include conditions on both currently known facts and currently active goals. It can only be invoked if its expression evaluates to “true”.

The body of a KA can be viewed as a procedure that establishes sequences of subgoals to be achieved (facts to be discovered) and draws conclusions (establish other facts) on the basis of achieving (or not achieving) these subgoals.

The system's main task, at a particular point in time, is to discover all that it can about current goals by executing relevant KAs. To do this, an invocation mechanism is implicitly called by the currently active KA when some currently unknown fact is requested or when some new conclusions are drawn. The mechanism evaluates the invocation part of all instances of the KAs occurring in the knowledge base to decide which ones are “relevant”. These relevant ones are then executed or invoked in turn until either they have all been executed or a definite conclusion has been reached about the current goal.

As an example, the rules for determining whether a switching function is needed constitutes one KA. This will evaluate if terminal equipment is to be connected to more than one server (computer). If this test produces the result “true” another KA for configuring the switching function is activated. This KA will further determine if either a separate switch is capable of doing the job or a computer may be used for this function. In this process one KA will activate a number of others for test of, for instance, the number of channels needed, the traffic requirement through the switching function, etc. Finally, it will activate the KA for relinking involved equipment to the selected switching function.

## 4.3. An example of the user-system interface

Some features of a design session are given in Figure 4. A user specifies his problem using a graphical interface (Figure 4a) by selecting different equipment types from the menu. By “clicking” simple commands like CONNECT, DISCONNECT, MOVE, and DELETE the user can change the configuration. He can also load, save, or print a specification using the function for input/output (I/O). The user may want to specify the chosen equipment in detail. By “clicking” INFO a window pops up on the screen and values of attributes may be entered.

![](/api/attachments/F6797M3M/fulltext/images/4a42634594be208f20af401ecc318a55e6fa990bb34aa367b447c7a4f7e776b7.jpg)  
Fig. 4. Graphical interface. An example with a set of personal computers and terminals required to be linked to two VAX computers.

After a problem has been specified, the user activates the module for configuration. During this phase of a design session, the system asks relevant questions in order to configure the network. A generated solution may be viewed on the screen (Figure 4b). In the example, the system has selected switching equipment (illustrated as a PABX). Since this switch was not in the original specification the system asks the user to specify an appropriate place on the screen (pointing by using a mouse). The system then draws the new configuration.

Under other circumstances, the system may suggest other solutions. For example, if the user has specified that the computers are connected in a computer network, the system may choose one of the computers to function as switching equipment.

## 5. Discussion and further research

## 5.1. Implementation and current status

Our prototype consists of a language for data communication design, an inference mechanism, a knowledge base, a graphical interface, and all the modules described in Figure 1 except for those for pricing, cost calculation, and analysis of alternatives. In the product data base there is only sample equipment. However, The Swedish Telecom is developing a full-scale product data base containing products from various vendors. This data base may be connected to the system.

## 5.2. Implications for further work

In designing and building the prototype, the following problems have been found to be critical with respect to the functionality and usability of the system: the control-strategy (inference-mechanism); the interface to the user; an explanation mechanism; and the types of knowledge represented in the system.

Research examining expert systems' user interface is scarce [1]. More effort is required in developing user interfaces that exploit the potential of expert systems methods and techniques to enhance problem solving processes. There is an extensive literature on interface design [21]. Proposed design guidelines should, to a larger extent, be explored in building a KBS.

The Decision Support Systems literature points out that, to be useful, support systems should be simple, robust, easy to control, adaptive, complete on important issues, easy to communicate with, relevant, etc [13]. The critical question is, of course, what does this mean in a specific application? It is reasonable to assume that there may be a tradeoff between the various characteristics; that is, it is not possible to have the optimum value of all characteristics in a specific application.

In semi-structured tasks like design, both procedural and declarative knowledge have to be represented; that is, knowledge about how a problem is solved as well as which specific solutions are applicable. The inference engine should be able to handle both types of knowledge. The inference engine should also be designed to allow for a user to change strategies or in other ways intervene into the system's process. Similar problems have been discussed by, among others, Georgeff and Bonollo [6], Luconi et al. [14], and Mitchell et al. [17]. Still, this is an area in need of more research.

## 5.3. Expert systems considerations

It is often suggested that a simple problem should be tackled first. However, managing and supporting a data communication environment requires much skill and expertise. If the simplest of the problems were tackled first, there is the danger that the wrong tool would be selected and thus the complexity of the important problems could not be seriously added. It is essential that the problem area be carefully analyzed to ensure that the most appropriate tools are selected. It is too easy to select an oversophisticated tool; this can result in additional expenditure which is not worth the investment.

For development of an expert system, it is important that sufficient expertise be available. The time needed in determining management and expert skills must be scheduled to ensure that the most appropriate knowledge is collected and verified.

Developing a prototype is an appropriate approach to determining what is required. It is a relatively inexpensive way of determining suitability of chosen applications, tools, hardware, and representation techniques.

Although expert systems have considerable functionality and can deliver systems that far outweigh what is possible with conventional systems, there are a number of aspects that must be considered. Expert systems are not easy to develop. It is easy to tackle the wrong problem with the wrong tool. It is essential to review how and where the application of expert systems can deliver the most business and operating benefit.

## Acknowledgement

This research has been supported in part by a grant from The Swedish Telecom, Kalmar. The authors want to thank Ronny Andersson, Leif Carlsson, and Göran Nilsson, at The Swedish Telecom.

## References

[1] Berry, D.C. and D.E. Broadbent. Expert Systems and the Man-Machine Interface. Part Two: The User Interface. Expert Systems, Vol. 4, No. 1, 1987.

[2] Buchanan, B., Bechtal, R., Benett, J., Clancey, W., Kulikowski, C., Mitchell, T., and D.A. Waterman. Constructing an Expert System. In Building Expert Systems. Hayes-Roth, Waterman and Lenat, editors, Addison-Wesley, Reading, MA, 1983.

[3] Cash, J.I. and B.R. Konsynski. IS Redraws Competitive Boundaries. Harvard Business Review. March-April, 1985, pp. 134–142.

[4] Clemons, E.K. and W.F. McFarlan. Telecom: Hook Up or Loose Out. Harvard Business Review. July-August, 1986, pp. 91–97.

[5] Cynar, L., Mueller, D. and A. Paroczai. Computers Design Networks by Imitating the Experts. Data Communications, April, 1986.

[6] Georgeff, M. and U. Bonollo. Procedural Expert Systems. In Proceedings IJCAI-83, Karlsruhe, West Germany, 1983, pp. 151–157.

[7] Goyal, S.K., Prerau, D.S., Lemmon, A.V., Gunderson, A.S. and R.E. Reinke. COMPASS: An Expert System for Telephone Switch Maintenance. Expert Systems. Vol. 2, No. 3, 1985, pp. 112–126.

[8] Harmon, P. and D. King. Expert Systems: Artificial Intelligence in Business. John Wiley & Sons, New York, NY, 1985.

[9] Harmon, P., Maus, R. and W. Morrissey. Expert Systems: Tools and Applications. John Wiley & Sons, New York, NY, 1988.

[10] Hayes-Roth, F., Waterman, D.A. and D.B. Lenat (eds.). Building Expert Systems. Addison-Wesley, Reading, MA, 1983.

[11] Keen, P.G.W. Competing in Time: Using Telecommunications for Competitive Advantage. Revised edition, Ballinger, Cambridge, MA, 1988.

[12] Liebowitz, J. (ed.). Expert Systems Applications to Telecommunications. John Wiley & Sons, New York, NY, 1988.

[13] Little, J. Models and Managers: The Concept of a Decision Calculus. Management Science, Vol. 16, No. 8, 1970.

[14] Luconi, F.L., Malone, T.W. and M.S. Scott Morton. Expert Systems and Expert Support Systems: The Next Challenge for Management. CISR WP#122, Center for Information Systems Research, Sloan School of Management, Massachusetts Institute of Technology, Cambridge, MA, 1985.

[15] Mantelman, L. AI Carves Inroads: Network Design, Testing, and Management. Data Communications, July, 1986.

[16] McFarlan, W.F. Information Technology Changes the Way You Compete. Harvard Business Review, May-June, 1984, pp. 98–103.

[17] Mitchell, T., Steinberg, L. and J. Shulman. A Knowledge-

Based Approach to Design. IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol. 21 PAMI-7, No 5, 1985.

[18] Michie, D. On Machine Intelligence. 2nd edition, Ellis Horwood, Chichester, 1986.

[19] Plotnik, M. Expert Systems Support in Telecommunication. In Information Network and Data Communication, II, Khakhar, D. and V.B. Iversen, editors, North-Holland, Amsterdam, 1988.

[20] Politakis, P. and S.M. Weiss. Developmental Facilities in an Expert System for Network Troubleshooting. In Proceedings of the European Conference on Artificial Intelligence, Italy, September, 1984.

[21] Shneiderman, B. Designing the User Interface. Addison-Wesley, Reading, MA, 1986.

[22] Vcsonder, G.T., Stolfo, S.J., Zielinski, J.E., Miller, F.D. and D.H. Copp. ACE: An Expert System for Telephone Cable Maintenance. Proceedings IJCAI-83, pp. 116–121.

[23] Williams, T.L., Orgren, P.J. and C.L. Smith. Diagnosis of Multiple Faults in a Nationwide Communication Network. Proceedings IJCAI-83, pp 179–181.

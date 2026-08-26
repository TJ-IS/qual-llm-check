---
otero_id: 21407
otero_key: "HXZK5F5A"
title: "SoftCord: an intelligent agent for coordination in software development projects"
authors: "Hardeep Venkataramani Johar"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00075-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# SoftCord: an intelligent agent for coordination in software development projects

Hardeep Venkataramani Johar $^{1,2}$

Computer Information Systems Department, Rider University, 2083 Lawrenceville Road, Lawrenceville, NJ 08648, USA

## Abstract

Over the years, software development has become more complex, and the problems of unreliability, high maintenance costs, and time overruns have greatly increased. A major contributor to this state of crisis in software development is the problem of coordinating activities. Based on a case study of a large software development project, we develop SoftCord, an intelligent agent that helps improve coordination in these projects. SoftCord is an autonomous program that incrementally records problem solving knowledge in a knowledge base (the MS-ATMS), and informs designers of inter-task conflicts when these are detected. Other features of SoftCord include the ability to respond to queries from individual designers, and the ability to set up and support negotiation sessions between designers when conflict resolution is necessary. © 1997 Published by Elsevier Science B.V.

Keywords: Intelligent agents; Software development projects; Coordination support systems; Truth maintenance systems; Artificial intelligence

## 1. Introduction

Software design is a complex collaborative design activity. The complexity in software design arises from two types of uncertainties: (1) uncertainties associated with the incomplete knowledge of the activities of other designers (different modules may be "written by different people, at different times, in different languages" [1]); and (2) uncertainties associated with the lack of complete specification of the problem because of the ill-structured nature of design [2].

Because of these uncertainties, collaborative design problems in general, and software design problems in particular, are characterized by the following coordination and control issues: (1) changes in development groups over time and the subsequent loss of rationale behind design decisions made by designers [3,4]; (2) unstated assumptions made by different designers and the inconsistencies that arise because other designers either do not know about these assumptions or misunderstand them [5]; and (3) frequent changes to design modules and the failure to carry these changes over to other modules because of incomplete knowledge about inter-module dependencies [6].

Software designers usually cope with these control and coordination problems by using repositories such as case tools or object libraries. These tools are useful because they provide easy access to a snapshot of the current state of the artifact being designed, or at least to a repository of objects used in the design. CASE tools, for example, support the design process by providing graphical aids for diagraming the different objects in the design, processing these objects to ensure completeness and consistency, and other useful features such as code generation. Some CASE tools also provide project management and method management features. The objective of a CASE tool is to "build within itself a design database, at a higher level than code statements or physical data element definitions" [[7]: p. xii].

These repository-based approaches capture the history of the project in a series of global snapshots by recording every design decision made. However, they do not capture design process knowledge, the process knowledge used by the designer in arriving at a design decision. Design process knowledge refers to the what, who, and why of decisions made and alternative solutions considered by the designer. This knowledge is critical for examining alternative courses of action when designers and managers need to make a design choice or when they encounter problems and revisit a design decision. Repository-based approaches focus primarily on the outcome of the decision process (the what), rather than on the process by which these decisions were reached. As a result, designers are forced to rely on informal mechanisms such as expert designers $[8,9]$ to fill the gap created by these limitations of design tools. Expert designers serve as informal repositories of design knowledge pointing out potential problems and providing the rationale behind design decisions to help designers make choices and to resolve problems when they occur.

Coordination and control problems adversely affect the design process by (1) increasing the time-to-market [10], (2) causing inconsistencies in the artifact that persist well after the design is completed [11], and (3) resulting in high maintenance costs [7]. As the complexity of the software being designed increases, the effect of these problems is magnified. Developing mechanisms for reducing the number of inconsistencies that arise in software because of coordination problems is an important issue for software engineering research. However, most design tools provide little or no support for the informal processes of coordination and this lack has been identified as a major cause of the software crisis [12].

In this paper, we describe SoftCord, an intelligent agent that helps improve coordination in software development projects. An intelligent agent is a software program that is: autonomous, in that it has some control over its actions and internal state $[13,10]$ ; that is social, in the sense that it communicates with other agents and with humans using an agent-communication language $[1]$ ; and that is cooperative, in that both the agent and the human initiate communication, monitor events, and perform tasks $[14]$ . SoftCord is an intelligent agent that plays a role analogous to the role of the expert designer in software projects. Like the expert designer, SoftCord keeps track of all project knowledge. When a designer makes a design decision, SoftCord checks the knowledge base for potential consistency problems, and if it does find a problem, generates and sends messages to all the designers potentially affected. The design of SoftCord is based on a descriptive model of the software development process that is partly based on a case study conducted at a large development site.

The rest of this paper is organized as follows. In Section 2 we outline a model that describes the software development process and the case study conducted to develop this model. In Section 3 we discuss the structure of SoftCord, an intelligent agent that supports coordination activities, and the multiple solver-assumption based Truth maintenance (MS-ATMS) that underlies it. In Section 4 we present implementation issues and detail the algorithms used in this version of SoftCord. Section 5 sums up the work.

## 2. The software development process

Recent research suggests that the knowledge gathered during the process of software development can provide useful support in the design of large software systems, and some effort has gone into developing systems to record this knowledge (cf. [15] and [5]). However, the focus of these efforts has been more on supporting the storage and retrieval of the rationale behind design decisions, rather than on identifying what aspects of process knowledge are important for coordination, and how this knowledge can be used to support coordination and control activities. In this section, we outline a descriptive process model that helps identify which aspects of process knowledge are useful for coordination and control, and what are the appropriate characteristics of an intelligent agent. The model is based on a case study conducted at a development site.

## 2.1. Case study: procedure

We examined the development process in a large software project undertaken by a "Big 6" consulting firm for a "Fortune 50" communications technology firm. The software being developed was a real estate management system for managing the property owned and leased in North America by the communications technology firm. The primary objective of the new system was to provide the ability to allocate property costs to the various business units that constitute the communications technology firm. The consulting firm developed a client-server system for this purpose where the server records information for accounting programs and the clients are the various functional systems for billing, managing contracts, etc.

The development project involved 80–100 designers over a one year time frame. Designers were divided into four teams: technical, functional, integration, and conversion/migration teams, each with their own responsibilities. Each team was further divided into a number of cells. Each cell contained a cell leader, analyst(s), programmer(s), methods analyst(s), and a representative user. For example, the Functional Team was responsible for function specific deliverables and was divided into six cells, each responsible for deliverables related to one functional part of the application.

The primary sources of data in the case study were two logs maintained by the project team: (1) an issue log that kept track of design questions that had implications across design teams; and (2) a change control log, that recorded all changes that needed to be made to the system (and the number of work days required to make the change). Since design changes are a direct result of the ill-structured nature of the problem, we used the change control log as a starting point, examined the issue log for each change, and conducted follow-up interviews with project personnel to identify the design processes that caused the change. The entire case study was conducted over a period of 6 months that spanned the end of the design phase and the start of the testing phase of the development project.

## 2.2. A descriptive process model

The outcome of the case study is a descriptive process model of the software development process that describes how inconsistencies arise, how these inconsistencies can be traced to assumptions, and how these inconsistencies are resolved (Fig. 1). The model points to two concomitant processes in the design of software.

1. The first process is a decompose/assign-synthesize process [16,4], where the problem is decomposed into subproblems, assigned to designers (either individuals or groups), designers make commitments (i.e. identify solutions), and individual commitments are synthesized to arrive at a solution to the original problem.

2. The second process describes the mechanisms by which individual designers make or change their commitments. Faced with uncertainties about specifications, designers make assumptions about the software artifact. These assumptions guide the selection of alternative solutions, one of which is selected as a commitment. Conflicts occur either when a specification changes, or when dependencies exist between subproblems, and designers make incompatible assumptions. Conflicts are resolved either through negotiation (two or more designers arrive at a mutually satisfactory consistent solution), or through arbitration (a third designer, for example an expert designer [8], suggests or mandates a conflict resolving solution). The negotiation and arbitration processes require that the designers involved have access to the assumptions underlying each commitment, and these processes result in a change in assumptions.

![](/api/attachments/HXZK5F5A/fulltext/images/3e4e213ce02af6f6c45e78a085c31c2da5c63f7f6f418f8f3dd861425ca7351b.jpg)  
Fig. 1. A descriptive model of the software development process.

![](/api/attachments/HXZK5F5A/fulltext/images/4f72d015c15b27d452e4629c5bf0c48cc3d778657474ad1c0d0c6b693411f6c7.jpg)  
Fig. 2. Design decisions and conflicts.

Fig. 2 illustrate how differences in assumptions can result in a conflict. The client-agreement-cell designer collects data about real-estate lease agreements (an agreement is a set of property leases made to one customer). This data is sent to the modules responsible for generating bills for customers (Send-Billing-Data task). Sending aggregate agreement data to the billing module is consistent with the assumption that an agreement is the smallest unit for billing purposes (left side of Fig. 2). When two designers make incompatible assumptions, a conflict occurs. Fig. 2 shows a conflict that occurs because the Generate-Bills task and the Send-Billing-Data tasks make incompatible assumptions. (In the case situation, the two choices were found to be inconsistent during the testing phase when it was discovered that the generated bills appeared to refer to leases, but actually referred to agreements.)

## 2.3. Implications for intelligent agents and coordination

Coordination problems arise primarily because the first process, the decompose/assign/synthesize process splits the overall problem into components that are treated as independent by designers [16,4,5], but these components are not really independent. Conflicts then occur when external specification changes, or the activities of other designers, cause decisions of some designers to become invalid. The implication of this for intelligent agents is that they should minimize the impact of inter-component dependencies, and support designers when conflicts occur and design decisions need to be changed.

It should be noted that in design problems we have no choice but to use the decompose/assign/synthesize approach. This is because of two reasons: first, it is the only practical way of handling the complexity inherent in these problems; and second because different types of expertise are required and individual designers tend to be specialists $[17]$ . Once the problem has been decomposed and assigned to individual designers, each designer needs to treat his or her subproblem as being independent of other subproblems, if the lower level of complexity is to be maintained, and if his or her expertise is to be properly utilized. However, while control over decisions is local to a designer, the artifact being designed must be globally coherent (see $[4]$ for a discussion on local control and global coherence in distributed problem solving).

The impact of these inter-component dependencies and external specification changes is quite serious. Designers are unaware of the existence of some dependencies, and specifications are misunderstood or not properly communicated. We observed that 36% of all design changes were caused by the presence of a dependency between system components, and these changes accounted for 46% of the cost (measured in work days) of all changes. Incorrect assumptions about specifications accounted for 22.22% of the changes and 41.26% of the cost. These occurred because designers were either unaware of a specification, or because they misunderstood a specification. Together, these two causes accounted for 87% of the cost of design changes making coordination problems the most significant cause of design changes (the other causes were: user-requested changes and technically necessary changes).

An intelligent agent must support this local control/global coherence aspect of design. Since designers have heterogeneous skills [18], the ideal agent should allow the designer to work locally on his or her subproblem as if it were the only problem being solved. The agent should come to life when it detects a potential threat to global coherence (either because of a conflict caused by the presence of a dependency, or because some global specification change has occurred), determine which designers need to be know about the threat, informs them about the treat, and help them resolve the conflict or potential conflict.

The agent must also support the conflict resolution processes of negotiation [19] and arbitration [8]. Negotiation processes are used when two or more designers can arrive at a mutually satisfactory solution, whereas arbitration processes are used when negotiation fails, or when negotiation is undesirable. In either case, the outcome of the process is either a change in an assumption or a change in an inference rule used by a designer. The outcome depends on the validity of the assumptions underlying the choices made by designers, and on the relative costs of the different alternatives available to the negotiating and arbitrating agents. The role of the intelligent agent becomes one of helping designers detect and articulate the assumptions underlying their choices (assumption surfacing, cf. [4]), and helping them to evaluate the relative costs of alternative scenarios.

In the next section we describe the architecture of an intelligent agent for coordination—SoftCord.

SoftCord incrementally collects knowledge from the designers relating to the problem being solved, attempts at all times to maintain a consistent set of beliefs about the design of the artifact, detects inconsistencies when they arise, informs designers about these problems, and helps them resolve the inconsistencies detected.

## 3. The structure of Softcord

The structure of SoftCord is illustrated in Fig. 3. Each designer interfaces with SoftCord through some knowledge acquisition tool (such as gIBIS [15]) that minimally interferes with their normal activities. The knowledge acquisition tool passes collected knowledge along to SoftCord. SoftCord is itself divided into two components: a coordinator and a knowledge base. The coordinator collects information from external sources, does some book keeping activities, and incrementally adds all knowledge to its knowledge base. The knowledge base records all knowledge and attempts to ensure that the commitments recorded in it are consistent with each other. When conflicts are detected, SoftCord conveys these to appropriate designers, and responds to requests for further information.

At the heart of SoftCord is the knowledge base. The knowledge base attempts to record all beliefs in a consistent manner, and informs the coordinator of inconsistencies when these are detected. The knowledge base is an extension of assumption-based truth maintenance systems (ATMS), an AI system, and this extended ATMS, the multiple-solver ATMS (MS-ATMS) is described in the next section. Soft-Cord uses the MS-ATMS as a repository for all design knowledge, and as a source for deciding when to initiate action. In Section 3.2, we describe the working of SoftCord including some of the functionalities of the coordinator. The example used to illustrate its working is the same example taken from the case study and described in the previous section. Implementation issues are discussed in Section 4.

![](/api/attachments/HXZK5F5A/fulltext/images/ae694ef8be9a3bfa16d483ac07d9c7a5801ac09a4f1724f7661ebd01691c72cf.jpg)  
Fig. 3. The structure of SoftCord.

## 3.1. SoftCord: MS-ATMS. The knowledge base

Using the descriptive model of the software development process of Section 2, we identify the following types of knowledge that SoftCord needs to maintain:

1. Knowledge about decomposed subproblems.

2. Knowledge about known dependencies between the subproblems. Not all dependencies will be known in advance and SoftCord needs to have a mechanism for detecting dependencies.

3. Knowledge about goals of each subproblem.

4. Knowledge about alternative solutions.

5. Knowledge about the reasoning behind each possible alternative solution.

6. Knowledge about assumptions made by each designer and what assumptions underlie each alternative solution.

7. Knowledge about commitments made by each designer, and the rationale behind the commitment chosen.

Since we need to record knowledge relating to beliefs and the rationale behind beliefs, a truth maintenance systems (TMS) architecture for the memory seemed to be appropriate. A TMS is a system designed to help problem solvers that use assumption-based search techniques to identify solutions. It attempts to reduce the complexity inherent in using search as a solution mechanism by separating problem solver activities from belief maintenance activities (see $[20]$ for a review of the literature on TMS).

One type of TMS, the assumption-based truth maintenance system (ATMS) [21,22] is capable of maintaining multiple consistent states simultaneously by associating a context (a set of assumptions under which a belief is consistent) with each belief. This is a useful feature for SoftCord since inconsistencies may not be resolved immediately but designers may wait for more information to arrive before they attempt a resolution (the other type of TMS, a justification-based TMS [23] automatically resolves inconsistencies).

However, the ATMS does not have all the features necessary for supporting coordination in software development projects, and we extend it to include the following functionalities: (1) the ability to find single consistent solutions; (2) the ability to distinguish data belonging to different designers; and (3) the ability to group alternative solutions to a subproblem and to reason with these alternative solutions. This extended ATMS, the multiple solver assumption-based truth maintenance system (MS-ATMS), serves as the knowledge base component of SoftCord.

## 3.1.1. Basic elements of the MS-ATMS

3.1.1.1. Nodes. Each of knowledge element is stored in the form of a node. A node represents some datum from the real world. The designer provides the datum to the MS-ATMS, which stores it in a node and retrieves it when requested. The assumption Bill-Level(Agreement) is an example of a datum stored in a node. Each datum is recorded in unique node corresponding to the type of knowledge it represents. There are five types of nodes in the MS-ATMS:

1. Assumption nodes: for recording assumptions.

2. Premise nodes: for recording facts.

3. Derived nodes: for recording intermediate conclusions provided by a designer.

4. Objective nodes: that correspond to goals and are used to record alternative solutions for each subproblem.

5. Commitment nodes: that correspond to goals and are used to record choices made by a designer.

When a designer asks the MS-ATMS to record some datum, he/she must also provide the type of knowledge being recorded. Thus if the designer assumes Bill-Level(Agreement), he or she communicates this datum to the MS-ATMS along with the information that the datum is an assumption. The MS-ATMS creates an assumption node and records the datum in that node.

3.1.1.2. Justifications. The datum in the problem domain are not independent. Every piece of data either supports some other piece of knowledge, or is supported by some piece of knowledge. For example, the assumption Bill-Level(Agreement) does not exist in isolation but supports the conclusion Send-Data(Agreement). Support for data arises from domain knowledge provided by the designer. For example, the designer may use a simple rule of the form Bill-Level(?X) ⇒ Send-Data(?X) to indicate that Send-Data(Agreement) follows from Bill-level(Agreement).

All rationale provided to the MS-ATMS are recorded in the form of justifications. Each justification consists of three parts:

1. Consequent: a node corresponding to the deduced datum. In the above example, SendData(Agreement) is the consequent.

2. Antecedents: the set of nodes corresponding to the support for the consequent. In the above example, Bill-Level(Agreement) is the only antecedent.

3. Informant: a detailed explanation for the deduction provided by the designer. For example, the informant for the above justification may be: "Since bills relate to agreements, data about agreements should be sent".

3.1.1.3. Contradictions. Often two or more datum are mutually exclusive because they cannot together provide support for other datum without causing an inconsistency. For example, the two assumptions Bill-Level(Agreement) and Bill-Level(Lease) are mutually exclusive, and cannot together provide support for any other datum.

The MS-ATMS records knowledge of inconsistencies in a special node called a contradiction node. The contradiction node is different from other MS-ATMS nodes in the sense that it has no datum associated with it. The set of mutually exclusive datum are used as a justification of a contradiction node. For example, the designer may indicate a contradiction (or SoftCord may add some contradiction detection rules of its own) using the rule Bill-Level(?X) ∧ Bill-Level(?Y) ∧ (?X ≠ ?Y) ⇒ ⊥, where ⊥ represents a contradiction.

3.1.1.4. Environments and contexts. An environment is defined as a set of assumptions. A node (or rather a datum—we use the terms interchangeably) holds in an environment if it is not inconsistent with respect to that environment (i.e. if no subset of the environment is inconsistent). The set of all nodes that hold in an environment is referred to as a context. For example, if there are two assumptions Bill-Level(Agreement) and Bill-Level(Lease), then there are three possible environments:

1. {Bill-level(Agreement), Bill-Level(Lease)}

2. {Bill-Level(Agreement)}

3. {Bill-Level(Lease)} And Send-Data(Agreement) holds in the environment {Bill-Level(Agreement)} and is in the context of this environment. A premise holds in a special environment, the empty environment, which indicates that the datum associated with the premise is always true.

Environments are useful because assumptions are the only pieces of knowledge which are open to question when making design decisions (we implicitly assume that the designer is making deductions based on valid inference rules. The MS-ATMS is not a domain expert and cannot make judgements about the validity of inference rules). Each node has attached to it a set of minimal environments, and all SoftCord needs to do is to ensure that this set is properly updated, and to examine the assumptions in the set to check for consistency.

3.1.1.5. The structure of a node. We are now in a position to define the structure of a node. A node in an MS-ATMS consists of the following information:

1. Datum: the knowledge element recorded in the node.

2. Justifications: the set of justifications that provide support for the node.

3. Type: the type of the knowledge element being recorded, i.e. whether the datum represents an assumption, an alternative, a commitment, a premise, the contradiction node, or a derived node.

4. Label: the set of minimal environments under which the node holds.

5. Rules: a set of rules which are automatically invoked when information in the node changes (i.e. when a new justification is added). This is useful for resource tracking.

6. Designer: the designer responsible for the subproblem. This is only used for objective and commitment nodes.

7. Resources: resource consumption and resource requirements associated with the datum. These are only used in objective and commitment nodes.

Of these information types, datum, justifications, and type have been explained above. Rules is a special data structure which contains pointers to a set of rules that fire when a new justification is added to the node. While these rules can represent any action that the designer desires, they are primarily useful for making resource computations. For example, when a designer identifies an alternative, the MS-ATMS can query the designer on the resource requirement for the alternative, and on the resources already consumed by that alternative. This information can be recorded in the resources slot, and may be used to provide information on the relative strength of each designer's commitment.

The Label slot is used to record the environments under which the node holds. When the MS-ATMS is informed of a new deduction by a designer, it computes the minimal set of environments under which the node holds for the consequent of the justification. This label is then propagated to all the consequents of the consequent, and so on. A detailed example of this process is described in the next section, and the algorithm for label propagation is described in Section 4.

Fig. 4 illustrates the basic elements of the MS-ATMS. Based on his/her knowledge of the domain, a designer has concluded that the datum Send-Data(Agreement) and Send-Data(Bill) hold (i.e. are consistent with) the assumptions, Bill-Level(Agreement) and Bill-Level(Lease) respectively. The designer indicates this relationship (to SoftCord) by providing justifications for each conclusion. For example, the designer may provide the rule $Bill-Level(?X) \Rightarrow Send-Data(?X)$ to SoftCord as justifications for both conclusions. Fig. 4 shows the assumptions, conclusions and justifications that the designer has provided to SoftCord.

![](/api/attachments/HXZK5F5A/fulltext/images/830545fc5603de97f4aa78522ac8289e2afc64860ef2b415e8134380b5e302ec.jpg)  
Fig. 4. Elements of SoftCord memory.

3.1.1.6. Objective nodes. The goal of a task is semantically different from the solution to a task and should be treated as different within the knowledge base. To see the difference between goals and solutions, consider the goal: determine x, y for $x + y = 7$ . One solution to this is x = 3, y = 4. However, x = 3, y = 4 is also a solution for other possible goals (for example, for the goal: determine x, y for y - x = 1). It therefore makes sense to have a specific node that represent goals. We use objective nodes to represent the goal of a problem, with one objective node for each goal.

Each objective node also records all solutions of the goal. Each solution forms a separate justification for the objective node (therefore each justification in the objective node has exactly one antecedent). The label of the objective node is the union of all the environments in all of its solutions. As a partitioning mechanism, each objective node also contains an identifier for the designer responsible for the subproblem.

The objective node is different from other ATMS nodes in two ways: (1) it contains an identifier for the designer; and (2) the node itself is identifiable as an objective node. This additional information makes it easier for SoftCord to respond to designer queries about possible solutions to the problem. However, for label propagation purposes, the MS-ATMS treats objective nodes in exactly the same way that it treats other ATMS nodes.

3.1.1.7. Commitment nodes. Commitment nodes represent choices made by designers. The primary purpose of a commitment node is to record knowledge about a commitment made by one designer, and to make this accessible to other designers. The commitment node adds semantic knowledge about choices to the MS-ATMS. Along with the standard MS-ATMS data (datum, label, justification), a commitment node contains the node identifier of the selected solution, and an identifier for the designer responsible for the subproblem. Each commitment node has at most one justification. The antecedents of this justification include the solution selected by the designer, and nodes corresponding to any other constraints that the agent may have considered in picking the particular solution.

![](/api/attachments/HXZK5F5A/fulltext/images/78c3a1b09e2d0a109809f2aac62cca2058089906c96e6b186ad70c4d0d4213db.jpg)  
Fig. 5. Commitment and objective nodes.

Fig. 5 illustrates the handling of both objective and commitment nodes. The goal of the subproblem illustrated in the figure is to identify the content of the data to be sent (variables are denoted with a leading "?"). When the problem is decomposed, the designer informs SoftCord of the new goal, and new objective and commitment nodes are set up in the MS-ATMS. These new nodes have no justifications, an empty label, and a designer identifier (client-agreement-cell in this example). When the designer identifies a solution, the command add-solution is passed to the MS-ATMS with two parameters, the identifier for the objective node, and the identifier for the solution node (either of Send-Data(Agreement) or Send-Data(Lease)). The MS-ATMS recomputes the label each time it is informed of a solution.

When the designer makes a choice, the MS-ATMS recomputes labels for all nodes that have this commitment node in a justification (as one of the antecedents). If the MS-ATMS detects an inconsistency, it informs the appropriate designers so that they can revise or negotiate their own choices. In the example, the client-agreement-cell designer has chosen Send-Data(Lease) as the solution, and the label and justification slots in the commitment node reflect this choice. The designer makes a choice using a make-commitment primitive with three parameters, the identifier for the commitment node, the solution choice, and any additional nodes in the justification. Bill-granularity(low) reflects the designer's knowledge of some global constraint.

## 3.2. The working of SoftCord

When SoftCord receives information about the existence of subproblems, it sets up one commitment node for each subproblem. Fig. 6 illustrates two nodes set up for the Send-Data and Generate-Bill tasks along with information about the designer. The labels for these commitment nodes are initially empty because the designers have not made commitments. The arrow from Send-Data(?Content) to Generate-Bill(?Content) indicates that there is a known dependency between the two tasks.

![](/api/attachments/HXZK5F5A/fulltext/images/919183f6b1117d6763d0ade88b985af458da010040d3227eb81c52b437af93af.jpg)  
Fig. 6. SoftCord example: initial state of memory.

![](/api/attachments/HXZK5F5A/fulltext/images/a121f6dba30f75f21411d6fb3fc7caddca36bd1d5c23c0ed9fd1099b93562390.jpg)  
Fig. 7. SoftCord example: one agent has committed.

## 3.2.1. Conflict detection

As designers works on their subproblems, they provide SoftCord with assumptions, intermediate conclusions, and candidate solutions. SoftCord records each item of knowledge in an appropriate node in the MS-ATMS. As each node is added, the MS-ATMS calls the algorithm PROPAGATE to compute the label of the node, and of all nodes that depend on it. If it finds any commitment nodes with an inconsistent environment, it returns a list containing all pairs of inconsistent commitment nodes and inconsistent environments to the coordinator which then sends a message to the designer informing him/her about which assumptions are inconsistent. The designer may choose to resolve the conflict by changing the commitment, or may choose to negotiate with the other designers affected. If the designer chooses to negotiate, SoftCord computes the set of designers affected (the set of designers affected can be computed by constructing a spanning tree rooted at the commitment node in $O(n)$ time, where n is the number of dependencies between commitment nodes), and sends negotiation messages to each agent.

![](/api/attachments/HXZK5F5A/fulltext/images/6215803372bad2af273e0351fdc1cd50dc0732e91bf6cff2d035f118524ad465.jpg)  
Fig. 8. SoftCord. Inconsistent choices.

An example of this process is illustrated in Fig. 7. The Client-Billing-Cell designer has worked on the problem, added two assumption nodes, and two derived nodes, and indicated that Generate-Bill(Agreement) is an acceptable solution to the subproblem (we have omitted objective nodes for brevity). The label of the commitment node indicates the assumptions under which this solution is consistent.

When the designer Client-Agreement-Cell makes a commitment (choosing Send-Data(Lease)), the MS-ATMS recomputes the label of Send-Data(?Content), and propagates the changed label to Generate-Bill(?Content). The outcome is indicated in Fig. 8. The new label of Generate-Bill(?Content) is inconsistent since Bill-Level(Agreement) and Bill-Level(Lease) cannot hold together. At this point SoftCord generates appropriate messages to the designers involved.

Inconsistencies are detected by the MS-ATMS by examining each environment in the label of a node and seeing if that environment is also in the label of the contradiction node. The rules for determining contradictions come from the domain and are provided by designers. In this implementation of Soft-Cord, we used the default rule $x(y_{i}) \wedge x(y_{j}) \wedge y_{i} \neq y_{j} \Rightarrow \bot$ , where $\bot$ represents the contradiction node.

## 3.2.2. Dependency detection

Often, in large projects, domain experts may not know all the dependencies between subproblems. Since knowledge of dependencies is important for conflict detection (label propagation requires that the commitment nodes be connected), SoftCord uses an assumption matching algorithm to detect dependencies. The basic idea behind the algorithm is that two tasks are potentially dependent on each other when they make assumptions about the same object (other domain specific rules for detecting dependencies can also be incorporated into the algorithm). For example, both Generate-Bill(?Content) and SendData(?Content) make an assumption about Bill-Level and are therefore potentially dependent on each other. Algorithm ASSUMPTION-MATCHING is described in Section 4.

## 3.2.3. Conflict resolution: negotiation and arbitration support

When the MS-ATMS detects the inconsistency in Fig. 8, SoftCord informs the designer involved and if necessary sets up a negotiation session between the agents. In general, when a designer is informed that there is a conflict between his/her commitment, and that of some other designer, he/she can do one of three things:

1. Do nothing: i.e. allow the inconsistency to remain hoping that the problem will sort itself out or will be easier to handle in the future. SoftCord keeps a record of the inconsistency in its problem list and allows the inconsistency to remain in the MS-ATMS.

![](/api/attachments/HXZK5F5A/fulltext/images/ca8e3391e1843d0061ebd625d8aaf1ef803a81e20ae20e3cf2bacc9649c5660a.jpg)  
Fig. 9. SoftCord example: state of memory after a consistent solution is found.

```prolog
NOTES:
1. Propagate takes two arguments: the node being changed, and the justification (antecedent part) that is being changed or added.
2. Propagate updates the label of the node and propagates the new label to all consequent nodes through justifications.
3. Propagate returns NULL if no inconsistencies are found. The value of the variable INCONSISTENT is TRUE if at least one inconsistency has been detected.
4. If an inconsistency has been found, then the inconsistent commitment node as well as the inconsistent environment are returned the variable OUTPUT-STACK.
STEP 1: (Compute a new label for N)
    NEW = COMPUTE-LABEL(L_n, ANTECEDENTS). // L_n is the old label.
    If (NEW = L_n) Return // Label has not changed so there is no need to propagate
    Else do one of Steps 2-6 depending on the node type of N

STEP 2: (n is a contradiction node)
    for (each environment E in NEW) do
    MARK-NOGOOD(E) // Add E to the list of nogood environments
    for (each commitment node N' that has E in its label)
    Add N' and E to OUTPUT-STACK
    INCONSISTENT = TRUE
    for (each justification J where N' is an antecedent)
    C = consequent of J
    A' = all antecedents of J excluding N'
    Call Propagate(C,A')
    Label(N) = NEW; Return

STEP 3: (N is an objective node)
    Label(N) = NEW
    Return

STEP 4: (N is a commitment node and it's label is empty)
    Add justification to N // N is the consequent and ANTECEDENTS are the antecedents of the justification
    Add NEW to Label(N)
    for (each justification J where N is an antecedent)
    C = Consequent of J
    A' = all antecedents of J excluding N
    Call Propagate(C,A')
STEP 5: (N is a commitment node and has a non-empty label)
    Construct J' such that // J' will replace the existing justification of N
    Consequent(J') = N
    Antecedents(J') = ANTECEDENTS
    L' = COMPUTE-LABEL(NULL, ANTECEDENTS) // L' will replace the existing label of N
    justification(N) = J' // Since N is a commitment node it will have at most one justification
    Label(N) = L' // and label. These represent the design decision made by the designer's.
    For (Each environment E in Label(N) that is also marked as NOGOOD) do
    add N and E to OUTPUT-STACK
    INCONSISTENT = TRUE
    For (each justification J where N is an antecedent)
    C = Consequent(J)
    A' = all antecedents of J excluding N'
    Call Propagate(C,A')
STEP 6: (All other types of derived nodes)
    Add new justification to N
    Label(N) = NEW
    For (each justification J' where N is an antecedent)
    C = Consequent(J')
    A' = Antecedents(J')
    Call Propagate(C,A')
Fig. 10. Algorithm PROPAGATE (node N, node_list ANTECEDENTS).
```

2. Change the commitment: if the designer chooses to change the commitment, SoftCord sends information about the new commitment to the MS-ATMS which calls its label propagation algorithm and the above process repeats itself. For example, if the Client-Agreement-Cell designer elects to change the commitment to Bill-Level(Agreement), then after the label is computed and propagated, no inconsistencies are detected. Fig. 9 illustrates the status of the MS-ATMS after this event occurs.

3. Negotiate: if the designer can find no other solution, or if the designer feels that the chosen solution is appropriate, he/she may choose to set up a negotiation session. The designer may now query SoftCord to see if there is any solution that is consistent with the current assumption. SoftCord returns one consistent solution if at least one is known to it. For example, if the Client-Agreement-Cell designer queries SoftCord for solutions consistent with the Bill-Level(Lease) (using the get-in-solution command), SoftCord informs him/her that the solution Send-Data(Lease) is consistent. The designer may now request a negotiation session. SoftCord computes the set of designers that need to be involved in the negotiation, sends messages, and allows any designer to ask queries relating to the current state of the knowledge base.

## 4. Implementation

## 4.1. Interface

The interface to the MS-ATMS consists of the following functions:

1. Create-node (datum, node-type): creates a node of type node-type. Returns node identifier.

2. Create-objective (datum, designer): creates an objective node with empty label and empty justifications. Returns node identifier.

3. Create-commitment (datum, designer): creates a commitment node with an empty label. Returns node identifier.

4. Justify-node (consequent, antecedents): adds a justification to a node (consequent). Then runs the label update algorithm to propagate changes (Algorithm PROPAGATE). Returns NULL.

5. Add-solution (objective-node, solution-node): adds solution-node as a justification of objective-node by calling justify-node(objective-node, solution-node). Returns NULL.

6. Make-commitment (commitment-node, solution-node, antecedents): changes the choice in a commitment node. First the current justification and choice are retracted, then the new justification and choice are added, and finally algorithm PROPAGATE is run. Returns NULL if no inconsistent commitment node is found. If an inconsistent commitment node is found, the algorithm terminates and the inconsistent environment is returned along with a list of all intermediate commitment nodes examined during the update process.

7. True-node? (node): returns TRUE if the node label consists of the empty environment.

8. In-node? (node, environment): returns TRUE if the node holds in the environment. A node holds in an environment if some subset of the environment is in the label of the node.

9. Get-in-solution (objective-node, environment): returns the node identifier for the first solution that holds in environment. This is useful when one designer is looking for alternative solutions to another designers task.

10. Get-solutions (objective-node): returns the list of solutions associated with an objective node.

11. Get-commitment (commitment-node): returns the current commitment. Note that it is the task of the problem solver to maintain associations between datum and nodes.

12. Explain-node (node, environment): returns a list of justifications that explain why node holds in environment. Returns NULL if node does not hold in environment.

Additional interface functions are provided so that designers can query data from the various slots in the node. For example:

13. Get-designer (node): returns the value of the designer slot (NULL if there is no designer slot).

4.2. Propagating changes and detecting dependencies

In addition to creating nodes, justifications, environments, and informing the coordinator, the main function of the MS-ATMS is to correctly maintain node labels. Algorithms PROPAGATE and COMPUTE-LABEL described in Fig. 10 and Fig. 11 are the primary engine within the MS-ATMS. PROPAGATE takes two arguments, the node being changed, and the justification that has changed or is being added. The label for the node is updated and the new label is propagated to all consequent nodes through the justifications that contain that node. Algorithm ASSUMPTION-MATCHING (described in Fig. 12) detects dependencies.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
STEP 1: (Compute a new label)
Let $L_k$ be the label of the $i$th antecedent of the $k$th justification
$L = U_i E_i$ such that $E_i \in L_{ik} // L$ is the new label.
STEP 2: Minimize $L$ by removing all environments that are supersets of others in $L$.
</div>

Fig. 11. Algorithm COMPUTE-LABEL ( $L_{n}$ , ANTECEDENTS).

## 4.3. MS-ATMS extensions to the ATMS

The primary extensions that we make to the ATMS are the addition of objective nodes and commitment nodes. These nodes represent goals and commitments respectively, and serve as a mechanism for SoftCord to partition the knowledge base and keep track of the activities of different designers separately. To handle these nodes, the interface of the MS-ATMS extends the ATMS interface with additional interface operations (see Table 1).

The MS-ATMS PROPAGATE algorithm differs from the ATMS PROPAGATE algorithm $[21,24]$ in two ways. First, commitment nodes are not handled in the same way as other derived nodes because of the need to search for inconsistencies and report these to the designer. To deal with this requirement we add Steps 4 and 5 to deal with commitment nodes and modify Step 2 to deal with nogoods. Note that while Step 4 is essentially similar to Step 6 (for derived nodes in general), Step 5 is not. Step 4 is similar to Step 6 because when a commitment node has an empty label, and a designer makes a commitment, the new resultant label cannot contain a no-good environment (since the solution in make-commitment is locally consistent). The commitment may cause a conflict with some other designer's commitment, and that will be tested with the call to PROPAGATE at the end of Step 4. However, when the label is non empty (Step 5), a change in the label of some antecedent node may cause an environment in the commitment node to become inconsistent (i.e. the commitment node is being affected by label propagation rather than being directly manipulated by a designer).

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Let OBJECTIVE = {n$_{j}$, ..., n$_{2}$} be the set of objective nodes
for (each n$_{j}$ ∈ OBJECTIVE)
    Let L$_{j}$ = Label(n$_{j}$)
    for (each n$_{j}$ ∈ OBJECTIVE; j &gt; i)
    Let L$_{j}$ = Label(n$_{j}$)
    for (each e$_{j}$ ∈ L$_{j}$ and e$_{m}$ ∈ L$_{j}$) // This loop
    can be replaced by other domain specific rules
    For (each assumption x(y) ∈ e$_{j}$)
    If x(z) ∈ e$_{m}$ add n, n$_{j}$ to OUTPUT//OUTPUT
    returns the list of dependencies
</div>

Fig. 12. Algorithm ASSUMPTION-MATCHING ().

The second difference between the two versions of the PROPAGATE algorithm is that the MS-ATMS maintains inconsistent environments in the labels of nodes (the ATMS drops inconsistent environments from the labels of all nodes except the contradiction node). This permits the detection of causal implications of inconsistencies, and more important, leaves conflict resolution to designers rather than to the program. The role of an intelligent agent is to detect and inform, not to make decisions in areas where it lacks domain expertise.

ATMS and MS-ATMS differences

<table><tr><td>ATMS Interface</td><td>Additional MS-ATMS Interface</td></tr><tr><td>Create-node (datum, node-type)</td><td>Create-objective (datum, designer)</td></tr><tr><td>Justify-node (consequent, antecedents)</td><td>Create-environment (datum, designer)</td></tr><tr><td>True-node? (node)</td><td>Add-solution (objective-node, node)</td></tr><tr><td>In-node? (node, environment)</td><td>Make-commitment (commitment, solution, antecedents)</td></tr><tr><td>Explain-node (node, environment)</td><td>Get-in-solution (objective-node, environment)</td></tr><tr><td></td><td>Get-solutions (objective-node)</td></tr><tr><td></td><td>Get-commitment (commitment-node)</td></tr></table>

## 4.4. Prototype implementation

We implemented a prototype version of SoftCord in C++ . We represented datum in the form of predicates (a predicate class), and nodes and justifications in the form of objects. Designers communicate with SoftCord using a finite set of commands. For example, the MakeDesigner("Bill") command informs SoftCord that Bill is a designer working on the project. The command MakeTask(Ted, Ann, SendDataGoal, ProjectX, "Send Bill Data") sets up a Send-Data subproblem, with Ted as the designer, Ann as the supervisor (this knowledge is necessary for arbitration purposes), SendDataGoal as the goal (SendDataGoal is a variable representing a predicate), and ProjectX as the project name. Other commands include MakeDependency(Task1, Task2), Assume(Predicate), Conclude(Predicate, justification), Alternative(Task, Designer, Predicate), and Choose(Task, Designer, Predicate, justification).

The Appendix contains a sample output from SoftCord corresponding to the example described in Section 3. In this implementation, all messages to SoftCord are channeled through a single program, and SoftCord sets up the data structures for other programs to use. For example, OUTPUT-STACK in PROPAGATE contains the list of commitment nodes in conflict, and can be used by other programs to compose appropriate messages to the designer. When the designer requests a negotiation session, and SoftCord computes a list of affected designers, SoftCord returns this list in a negotiation-list variable. In the prototype all output is also mirrored on the screen.

## 5. Conclusion

This paper makes two main contributions. First, we develop an intelligent agent for coordination in software development project (SoftCord). Second, we extend ATMS so that it can deal with multiple problem solvers, and with the need to find single consistent solutions. Further research integrating SoftCord with appropriate tools for acquiring problem solving knowledge from designers is necessary.

Computers are becoming central to an increasing range of human decision making activities, and all types of human users interact with computers for a host of everyday activities. Intelligent agents have the potential to play in important role in transforming human computer interaction from direct manipulation to indirect manipulation [14]. With direct manipulation, a user initiates all tasks explicitly, whereas with indirect manipulation, the user and the computer (the autonomous agent) "engage in a cooperative process" where "both initiate communication, monitor events, and perform tasks" [[18]: p.31]. Fundamental to this indirect manipulation nature of an agent is autonomy, and autonomy is the theme that underlies the design of SoftCord. SoftCord serves as a repository of process knowledge, monitors all actions taken by the designer, and initiates action only when necessary, when an actual or potential inconsistency is detected. Intelligent agents in general, and SoftCord in particular attempt to embed technology in the workplace, make it unobtrusive, and interfere minimally (i.e. act only when necessary) with the work of a human decision maker.

An issue that has gone unaddressed in this research is how SoftCord fits into the normal work of a designer. Genesereth and Ketchpel [1] argue that an agent should have a well defined agent-communication language (for both agent-agent communication as well as agent-human communication), and go on to say that this language should be general across many different types of agents. We meet this technical issue half-way by providing a well defined interface to SoftCord (Section 4.1 and Section 4.3), but leave the question of integrating SoftCord with particular knowledge acquisition tools to the implementor. For now, it appears that tools such as gIBIS have been successful in getting managers to articulate process knowledge, and it is technically possible to integrate gIBIS with SoftCord.

The issue of a common agent-human language by which designers indicate process knowledge is also important because of the need to ensure that designers use the same concepts, terms of languages to describe the same issue (for example, it is hard to make a computer program realize that bill-level and level-of-bill is the 2billthing unless this knowledge has been explicitly made available to it). This problem can be partly addressed by linking the knowledge acquisition tool to the data dictionary as a source of project specific vocabulary. The larger issue of developing a common language requires further research on developing an appropriate set of characteristics for software development projects (for example, the bill-level example used in this paper is characterized by the level of aggregation of data). The knowledge acquisition tool could detect this by asking the designer if a data inflow or outflow represents an aggregate or not, whether alternative aggregations are possible, and why the designer chose the particular aggregation. Combined with access to the data dictionary, this would ensure (at a reasonable level) that designers use the same language in coding knowledge elements (see [9] for a discussion on this issue).

The author acknowledges the support of Andersen Consulting and AT&T for access to the case study site, and especially of Roy Loomis and Ron Wolfe of Andersen Consulting for their help. Also, thanks to Vasant Dhar, Edward Stohr, and Alex Tuzhilin, for their comments, suggestions and directions, and to Gita Venkataramani Johar forcomments on early versions of this manuscript. This research is based on a doctoral dissertation completed at the Leonard N. Stern School of Business, New York University. This research was partially supported by a summer research grant from Rider University.

## Appendix A. Sample output from SoftCord

//SETTING UP THE PROJECT
New Project Created
Task: 0 Designer: Ann Supervisor: Ann
Goal: BuildSystem(?B)

//MAKING SUB TASKS
New Task Created.Task: 1 Designer: Ted Supervisor: Ann
Goal: SendData(?X)
Commitment Node 3 created.Goal: SendData(?X)
Objective Node 4 created.Goal: SendData(?X)

//RECORDING DEPENDENCIES
Dependency Created. GenerateBill(?Y)depends on SendData(?X)

//ADDING THE TWO ASSUMPTIONS
Assumption Bill-Level(Agreement) added to data base
Node Id for this assumption is: 7
Assumption Bill-Level(Lease) added to data base
Node Id for this assumption is: 8

//DEFINING THE CONTRADICTORY ENVIRONMENT
//(ASSUMPTION-MATCHING)
Contradiction(Node) holds under the following sets of assumptions:

Assumption Set 1
Bill-Level(Lease)
Bill-Level(Agreement)

//DRAWING CONCLUSIONS
Created new node Id 9 for Send-Data(Agreement)
Send-Data(Agreement) holds under the following sets of assumptions:
Assumption Set 1
Bill-Level(Agreement)
Created new node Id 10 for Send-Data(Lease)
Send-Data(Lease) holds under the following sets of assumptions:
Assumption Set 1
Bill-Level(Lease)

//RECORDING ALTERNATIVE SOLUTIONS
Alternative Send-Data(Agreement) for goal Send-Data(?X) added
This goal can be satisfied under the following sets of assumptions
Assumption Set 1
Bill-Level(Agreement)

Alternative Send-Data(Lease) for goal SendData(?X) added
This goal can be satisfied under the following sets of assumptions
Assumption Set 1
Bill-Level(Agreement)
Assumption Set 2
Bill-Level(Lease)

//DESIGNER ALEX MAKES A COMMITMENT
Choice: Generate-Bill(Agreement)
Inconsistency report follows
No Inconsistencies Detected

//DESIGNER TED MAKES A COMMITMENT
Choice: Send-Data(Lease)
Inconsistency report follows
Message for Designer Alex
The following commitment was found inconsistent:
GOAL: GenerateBill(?Y)
Designer: Alex

CONFLICTING ASSUMPTIONS:
Bill-Level(Lease)
Bill-Level(Agreement)
Set up a negotiation session? (Y/N): Yes

//ALEX REQUESTS A NEGOTIATION SESSION
Message for Designer Ted
The following commitment was found inconsistent:
Designer Alex has requested a negotiation session
GOAL: GenerateBill(?Y)
Designer: Alex

CONFLICTING ASSUMPTIONS:
Bill-Level(Lease)
Bill-Level(Agreement)

Message for Designer Alex
The following commitment was found inconsistent:
Designer Alex has requested a negotiation session
GOAL: GenerateBill(?Y)
Designer: Alex
CONFLICTING ASSUMPTIONS:
Bill-Level(Lease)
Bill-Level(Agreement)

## References

[1] M.R. Genesereth, S.P. Ketchpel, Software Agents, Communications of the ACM, 37 (7) (1994).

[2] H.A. Simon, The Structure of III-Structured Problems, Artificial Intelligence, 4 (1) (1973).

[3] I. Benbasat, J.S. Dhaliwal, A Framework for the Validation of Knowledge Acquisition, Technical Report 88-MIS-006, Faculty of Commerce and Business Administration, University of British Columbia, Vancouver (1988).

[4] L. Gasser, Social Conceptions of Knowledge and Action: DAI Foundations and Open Systems Semantics, Artificial Intelligence 47 (1991) 107–138.

[5] B. Ramesh, Process Knowledge Based Group Support for Systems Development, Ph.D. Dissertation, New York University (October 1991).

[6] C. Pu, G.E. Kaiser, N. Hutchinson, Split Transactions for Open-Ended Activities, in: Proceedings of the 14th International Conference on Very Large Databases, (August 1988) pp. 26–37.

[7] J. Martin, D. McClure, The Problem of Software Maintenance and its Solution, Wiley, 1983.

[8] B. Curtis, H. Krasner, N. Iscoe, A Field Study of the Software Design Process for Large Systems, Communications of the ACM, 31 (11) (1988).

[9] H. Johar, Coordination and Control in Distributed Work: Towards Intelligent Design, Ph.D. Dissertation, New York University, 1994.

[10] P.G.W. Keen, Competing in Time: Using Telecommunications for Competitive Advantage, Ballinger, Cambridge, MA, 1986.

[11] F.P. Brooks, The Mythical Man-Month, in: P. Freeman, A.I. Wasserman (Eds.), Tutorial on Software Design Techniques, IEEE Computer Press, Silver Spring, MD, 1983, pp. 35–42.

[12] R.E. Kraut, L.A. Streeter, Coordination in Software Development, Communications of the ACM, 38 (3) (1995).

[13] C. Castlefranchi, Guarantees for Autonomy in Cognitive Agent Architecture, in: M. Wooldridge, N.R. Jennings (Eds.), Intelligent Agents: Theories, Architectures, and Languages, Springer, Heidelberg, 1995, pp. 56–70.

[14] P. Maes, Agents that Reduce Work and Information Overload, Communications of the ACM, 37 (7) (1994).

[15] E.J. Conklin, K.B. Yakemovic, A Process Oriented Approach to Design Rationale, Human-Computer Interaction, 6 (1991).

[16] C. Gane, Computer-Aided Software Engineering: The Methodologies, the Products, and the Future, Prentice Hall, New Jersey, 1990.

[17] B.G. Silverman, T.M. Mezher, Expert Critics in Engineering Design: Lessons Learned and Research Needs, Artificial Intelligence Magazine, (Spring 1992) 45–62.

[18] E. Edmonds, L. Candy, R. Jones, B. Soufi, Support for Collaborative Design: Agents and Emergence, Communications of the ACM, 37 (7) (1994).

[19] C.W. Hewitt, Open Information Systems Semantics for Distributed Artificial Intelligence. Artificial Intelligence 47 (1991) 79–106.

[20] J.P. Martins, The Truth, the Whole Truth, and Nothing but the Truth, Artificial Intelligence Magazine, 11 (1991) 7–26.

[21] J. DeKleer, An Assumption Based Truth Maintenance System, Artificial Intelligence, 28 (2) (1986).

[22] O. Dressler, An Extended Basic ATMS, in: Proceedings of the 2nd Intl. Workshop on Non Monotonic Reasoning (1988).

[23] J. Doyle, A Truth Maintenance System, Artificial Intelligence 12 (1979) 231–272.

[24] J. DeKleer and K.D. Forbus, Truth Maintenance Systems Tutorial Notes, AAAI Conference Tutorial Series, AAAI, 1991.

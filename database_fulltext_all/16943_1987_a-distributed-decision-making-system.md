---
otero_id: 16943
otero_key: "PHPSBUW3"
title: "A distributed decision-making system"
authors: "A Burns; M.A Rathwell; R.C Thomas"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90071-6"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Distributed Decision-Making System

A. BURNS \*, M.A. RATHWELL \*

and R.C. THOMAS \*\*

\* Postgraduate School of Computing, University of Bradford, Bradford BD7 1DP, UK,

\*\* Department of Computer Science, University of Leeds, Leeds LS2 9JT, UK.

A message based model of a Distributed Decision Making, DDM, System is presented. This model is developed from a survey of the needs of group decision-making processes within organisations and distributed computer applications; a review of this survey is given. DDM extends the DSS concept to one that enables two or more decision making parties to co-operate in using DSS tools. It assumes a framework of organisational decision making which concentrates on the organisation as a political system where communication is important and conflict between groups just as likely as consensus. A brief description of a prototype implementation of the model is given. The use of the prototype has upheld the principles from which DDM was designed.

Alan Burns is a Senior Lecturer in the Postgraduate School of Studies in Computing at the University of Bradford (UK). He received his DPhil from the University of York (UK) in 1978 and has published widely in a number of areas of computer science including: concurrent programming languages, software engineering, human-computer interfaces, and decision support systems. These interests are combined in one of his present research topics – the design of a distributed multi-user decision support environment. He is involved in the provision of DSS tools within real-time systems.

Margaret Rathwell received an MSc in Computer Science from the University of Bradford in 1980, and has recently completed her PhD thesis in distributed decision-making systems. She has worked as an analyst/programmer with the automation support group of an international bank and in local government in the United Kingdom.

Richard Thomas has a BSc in Electronic Engineering, an MSc in Operational Research and an MPhil in Computer Science. He worked for several years on airline reservations systems and then in decision support in the confectionary industry. He is currently a Lecturer at Leeds University where he is working on expert systems and artificial intelligence. He is co-author of a book on computer vision.

## 1. Introduction

One of the growth areas in commercial computing in the last decade has been the development of information systems that support specific decision-making processes. This paper is concerned with understanding the needs for organisational decision support and modelling the resulting distributed (federated) information support system.

Much of the conceptual literature on DSS is concerned with human problem solving and draws on work in cognitive psychology. However, in practice the information systems needed within organisations tend to be built around activities involving planning and co-ordination which require consideration of organisational issues. Support for tasks which involve co-operation and conflict between differentiated organisation units has not been provided in most existing information systems architectures. Moreover much of the early DSS work has tended to ignore the role of communication in the decision-making process. Clearly there is a trend towards interconnecting systems [47] and as Adriav and Ginzberg [3] have commented this dimension should be the focus of future DSS attention.

Keen and Hackathorn [27] have described how many tasks in organisations are interdependent, for example building a divisional marketing plan or the development of a strategic policy. These decision making tasks are hard to give conventional support to as they require ‘organisational support’ for tasks which depend on other organisational units and which involve a sequence of decisions, and ‘group support’ for decision making by a group of individuals engaged in separate but interrelated tasks. Keen and Hackathorn then go on to consider how several people can co-operate around the use of a single DSS. Scher [38] also describes the distribution of a single DSS through an organisation using a conferencing system. The interactive sharing and use of information among a group in a decision-related meeting is similarly facilitated in GDSS (Group Decision Support Systems), a structure advocated by Huber [25].

A different approach is, however, proposed by Thomas and Burns [44] following their analysis of the use of DSSs in a manufacturing company. This new focus is best illustrated by adapting Sprague's connotational view of DSS [40]. The new layer, see fig. 1, is termed 'Distributed Decision Making'. It takes the form of a federation of separate DSSs.

In their book on DSS, Bonczek et al. [8] provide a framework of decision making which stresses the importance of organisational roles, channels of communication and relationships among roles. The relevance of political processes such as bargaining are recognised but they are not seen as a main impetus in decision making. This view is not supported by Kling [28], Ackoff [1,2] or Boneham [10] (and many others). By focusing on conflict as well as communication a DDM system recognises the importance of political/organisational processes within decision making.

The technical support for distributed decision making can be provided through computer-mediated communication systems and networks. Distributed systems and computer networks are important fields of current computer science research and are being increasingly used in organisations. They represent important agents for change. Local area networks, for example, can support a decentralised computing environment where relatively small desktop or microcomputer systems, each dedicated to a small number of users or a small number of tasks, are linked together in an organisational-wide network for information exchange. Distributed applications however have tended to be less well understood than the physical aspects of distribution and networking.

![](/api/attachments/PHPSBUW3/fulltext/images/02e3cbb73ba3bb8e355c14957885c32167f6a1bdfaf4aa7c74a785141b59dbb8.jpg)  
Fig. 1. Focus of DDM.

## 2. Information System Support for Group Planning and Decision Making

The quality of support that could be provided by a DDM system for organisational decision making and planning depends upon an understanding of both group decision-making processes and computer systems building. A number of multi-user applications concerned with resource allocation management and which involve planning, communication, co-operation and co-ordination have been described in the literature. To form the basis for the requirements of a DDM system a survey was made of these group activities [37].

## 2.1. The Group Planning Survey

A common characteristic of many groups involved in organisational decision activities, for example design engineers [31], programmers [12], scientists [24], or managers in a particular operational area [29] is that individuals define their own tasks and information processing needs. Through the use of DSSs, groups allow their decision to be supported by computer systems. Where decisions made by one subunit of an organisation constrain decisions in other parts (such as scheduling activities) or where information is gathered from many parts of the organisation for planning (for example strategic planning) co-operation between groups is required. Negotiation and conflict resolution between different groups may be involved in this process. Communication consists of making tentative decisions and commitments, and a series of interactions with feedback between participants. In this way, decision-making parties may move in stages towards a goal such as the design of a new software system or the formulation of a divisional plan.

## 2.2. Distributed Information Systems

Group planning and decision making makes certain requirements for communication structures in an information system. Cashman and Holt [14] and Dzida [16] note that co-operation between team members in a software engineering environment requires more than a simple electronic mail system. Smith and Davis [39] describe a distributed 'contract net protocol' for problem solving which uses negotiation as a mechanism for task distribution. This is an example of a task sharing system. An alternative approach is to concentrate on result sharing; this is the basis of blackboard systems such as in the original Hearsay-II where programmable knowledge sources are configured into groups and executed [18].

A similar approach is advocated by Tenney and Sandell [42] in their ‘distributed decision making’ method. A distributed control structure links individual elements of the system called domiciles. A domicile is an expert on some subsystem but with no knowledge of the system outside its domain. An example of such a structure can be found in military command and control systems in which distinct agents working towards a military objective can be identified [43].

The extension of electronic mail to computer conferencing has been experimented with by many groups (for example see references [24,38,41]). These systems structure communications amongst a group into topics and keep permanent transcripts of all discussions. Often a centralised computer is used to co-ordinate the compositions and distribute and retrieve text items and messages.

Also special mention must be made of office automation. Here the computer supports the office worker by integrating word-processing, electronic mail and database management. Such integration has proved difficult but there are systems available that provide a single data representation and a uniform set of operations [11,20]. Hewitt's actor model [21] has often been used to model office automation systems (OAS) [7,13]. An OAS may be considered to be comprised of a number of distributed processes (called 'actors') executing concurrently. Activities are frequently event driven with independently executing actors communicating by messages. Zisman [46] considers the use of AI techniques in OAS to manage the workflow in a journal editing process. Agents receive messages and process them in terms of a local rule base to obtain the appropriate action or response.

Another approach is discussed by Ellis [17] in which forms migrate around the OAS and get filled out by staff. The forms themselves contain much of the intelligence in the system.

The analysis reported in this paper was obtained from a research project with the following objectives:

(a) to study group decision-making processes and possible computer support;

(b) to establish the basis for a system to link separate DSSs in an organisation;

(c) to construct a model of the underlying activities of a DDM system, to design and implement a prototype system and gain experience from using it;

(d) to explore some of the applications for which a DDM system is appropriate.

A detailed description of the project is given by Rathwell [36].

## 3. Design of the DDM Model

Following the survey of the requirements for the support of group decision making, and a review of present distributed information systems, the needs of a DDM system were specified. The DDM model is based on a network of nodes, where each node supports some decision making activity. The requirements are summarised as follows:

(a) Support for individual decision makers within a system node.

(b) Communication between nodes, including (but not exclusively so) a form of electronic mail.

(c) Propagation of explanation and conflict resolution support.

(d) Evolutionary development.

(e) Non-hierarchical system topology.

Within each node individuals (and closely working groups) should be provided with ‘classical’ DSS tools. An important feature of these DSSs is that they should be adaptable to the user's way of working.

A common feature of unstructured decision-making processes is the requirement for communication between decision makers. Decisions made in one part of an organisation will constrain decisions to be made in other parts. Communication, co-operation and co-ordination between nodes must be supported. This will often take the form of a DSS's execution interacting with another DSS on a different node.

Our analysis of group activity within organisations indicates that the assumption of the effective existence of agreed organisation-wide objectives is not always (if ever!) valid. Many of the distributed information systems discussed in the last section do assume unity of purpose within the end user population. The lack of this unity must be the reason why many information systems are underutilised or even unused. If common objectives are not assumed, but support is to be given to organisation-wide decision making, then conflict must be explicitly handled. Thomas and Burns [44] pointed out in their case study that taking conflict to a higher level in a hierarchical management structure is often less satisfactory then attempting to explain decisions and reach compromises directly between the parties involved.

The evolutionary development of DSS must be carried over to the entire DDM. Little confidence can be placed on a static DDM being specified and designed in a top-down manner. The interaction between the DSSs must be allowed to grow and be modified as necessary before familiarity with the organisational support is obtained.

An important characteristic pointed to in the group planning applications surveyed [37] is that communication was not organised as a hierarchy. Interactions were amongst equals, such as engineers, software developers, scientists or members of a management team. The DDM model therefore assumes a matrix style organisational structure with communication and cooperation between decision-makers at parallel levels [5,19] (this is independent of the actual formal structure in existence).

## 3.1. DDM Components

A typical DSS can be considered to be composed of operators and data. The interaction between distinct DSSs could therefore be based on either

(a) data sharing, or

(b) operator sharing.

The DDM model described in this paper is based on operator sharing; the reasons for this choice are, briefly:

(i) Many DSSs themselves are constructed as collections of operators, with users combining these components in a flexible way to construct models.

(ii) An important aspect of DDM is the autonomy of each node; data is clearly owned by individual nodes not by some global database. By making data available through operators only the results of program execution are transmitted to other nodes. Data and the structure of the operators themselves are private.

(iii) The DDM structure does not assume a homogeneous system of nodes with a single data representation on all hardware. By sharing only operators data description problems are minimised.

(iv) Finally, by basing the DDM model on operator sharing only, the resulting system is a better march for the logical view of a collection of cooperating but distinct DSSs.

A fuller description of the motivation for basing DDM on operator sharing is given by Rathwell [36].

## 3.1.1. Late binding

For a distributed system based on operator sharing an implementation could be based on static or dynamic binding. Static binding is more efficient for running one-off applications but restricts relocation of data and other system changes. In contrast dynamic binding is performed only when the operators are used. It is more flexible but has a greater run-time overhead.

Because of the ad hoc nature of decision support models it is preferable for DDM system applications to be bound together at execution time. In doing this it will also allow program modules in a variety of languages to be linked together enabling users to be unaware of the particular language or tool being used in an external DSS.

## 4. A Model of a DDM System

In order for practical DDM systems to be constructed it was necessary to first product a definitive description of a DDM system. A simple model was chosen, based (as many office automation system are) on Hewitt's Actor Model [21–23]. Within Hewitt's model a system consists of a collection of communication objects called actors. Each actor has a set of acquaintances that it can communicate with by sending messages. Actors execute asynchronously upon receipt of a message.

The behaviour of the actor when it responds to a message is governed by a script.

The DDM model takes a simple view of the actor system. The objects which form the nodes of a DDM system behave as actors. Thus within the DDM model the basic object is the node. A node may send a message to another node, with which it is acquainted, to request the execution of a DSS operator (called in this model a function). The DDM system therefore consists of a community of nodes and messages between nodes. A user program at a note (which may make use of external functions) is known as an agent. The execution of an external function is called a transaction, the consequence of which may be the transfer of a resource to the calling node.

The structure of a node is shown in fig. 2. A definition of model semantics is as follows, where [] indicates a set of:

node = { [acquaintances], [functions], [agents], [resources], log, script }.

## 4.1. Acquaintances

An acquaintance is a node name:

acquaintances = [node\_names].

In order to execute an external function an agent must know the name of the function and the name of the node that contains that function. An implementation will keep a table that maps between node\_names and whatever physical address is needed to communicate with that node.

During experimentation with a prototype implementation of the system (see section 6) it was found useful to provide one node (called noticeboard) that acted as a name server. Each node that jointed the system would call the function 'register' at noticeboard and would leave its node\_name. The set of acquaintances for the noticeboard therefore contained all nodes in the system. A public function (called aid) of the noticeboard could then be called by any other node to get an up-to-date set of node\_names.

![](/api/attachments/PHPSBUW3/fulltext/images/69f7db01c1e79eff014759e5f7e9275806ba8aab61d94f21003aa4cd52e241bd.jpg)  
Fig. 2. Components of a node.

## 4.2. Functions

A function is in four parts:

$$
\begin{array}{r l} \text { function } & = \left\{\text { description }, [ \text { access\_rights } ], \right. \\ & \quad \text { program\_module }, \text { single\_user } \}. \end{array}
$$

The description will be used to advise human operators on the use of the function and input data formats. Formally it can be expressed as a set of ASCII characters:

description = [characters].

Access-rights is a set of all nodes that can use this function:

access\_rights = [node\_names].

It will usually be a subset of the nodes' acquaintances unless it is assigned to open access (access\_rights = all). At the other extreme a function may be prohibited from external usage (access\_rights = null).

The program\_module (a series of computational events) is the actual code of the function. It could be generated from any programming language that the node supports but must be in a form that will allow the script to execute it automatically.

The fourth element in the definition of a function is 'single-user'; this is a flag that will indicate whether concurrent execution of the program-module is allowed:

single\_user = TRUE | FALSE.

At each node the set of functions must contain two special ones called help and mail (access\_rights = all). A call to help will return the descriptions of all functions that are registered with that node. Mail allows free format text to be sent to any node. The help function is particularly important as it allows users to learn about the DDM system and increase their use of it.

## 4.3. Agents

An agent is a partially ordered set of function calls and computational events. It is partially ordered due to the concurrent nature of many decision support events. Function calls are constructed at the time of the agent's execution; this allows agents to have late binding.

The model of DDM described here does not need to specify the form of the agent language. It must however be constructed so that organisational, and group, decision support activities can be programmed. The primitive structure on which DDM is built is operator sharing between distinct DSSs. An agent will therefore normally contain internal and external function calls plus local data processing.

Within the overall DDM project various forms for an agent language were investigated; these are discussed in the next section.

As agents are themselves program modules then it is possible for an agent (with external calls) to be registered as a function at a node. Thus a function called at a node may itself be an agent that triggers further function calls at other nodes. Indeed a circular path of function calls is possible. Although such a circular path if made up of single-user functions would cause deadlock this error condition is not catered for in the model.

## 4.4. Resources

Resources will usually take the form of computer files. They should not, however, be seen as merely computer stored data. Information held by the human operator also constitutes a node resource. In this case execution of a function will require input from the node user. Resources themselves are encapsulated within the node; only by the execution of an exportable function can resources pass out of a node.

A message which causes a function to be executed that alters the state of any node resource is known as an active message. For example, making an entry in a diary will, if the request is granted, change the node's data. Alternatively a message that leads to a function reading but not changing a resource is known as passive.

The resource that passes between nodes, in the form of a message, need not just be data. It could be a program that is to be executed at the designated node. For example an interactive questionnaire could be sent to a number of nodes; the execution of which will first require input from the node user and will then, automatically generate a reply message. Messages that themselves contain computational events are called, by Waterman, reactive messages [45].

## 4.5. Log

The log is a node resource that keeps track of all transactions (external function calls) both into and out of the node. It is in human readable form and is used, when necessary, for a node user to check on external usage of DDM functions. The log is included in the model both to encourage awareness of the DDM facility and to build confidence in its security (i.e., one can always look at the log to see who exactly has been using the facilities provided).

## 4.6. Script

The script is a definition of how the node should behave, particularly when it receives a message. Its activities are as follows:

(a) If the message is from the user, requesting the execution of an agent, the appropriate language translator is used and external function calls trapped. These calls are transferred into messages and sent to the appropriate node. This action is recorded in the log.

(b) If the message is from another node access\_rights are checked, the program\_module is executed (with whatever data is supplied in the message) and a reply message is constructed. This action is also recorded in the log.

(c) The script also defines the allowable actions on the sets of functions, agents and acquaintances, i.e., it defines how they can be changed.

The reply message which is always constructed for an external call could be null if the function did not generate data; alternatively it can contain error flags indicating either that the function did not exist at that node or that access rights did not contain the calling node's name or that an error occurred during execution.

## 5. Agent Languages

As indicated above the exact form of the agent language is not a concern of the DDM model. Indeed the support of more than one agent language on an implementation would be quite acceptable. Nevertheless the nature of the agent language is of the upmost importance as it provides the user interface to the DDM system.

In principle any DSS language that is based on operators would be extendible. Within this DDM project, however, a language was specially designed to fully exploit the power of the DDM system. The language, which is called AL (an acronym for Agent Language), is described in detail elsewhere [34]; space restrictions do not allow a detailed description here.

The basic action within an agent program is the assignment:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\langle \mathrm{file}\rangle := \langle \mathrm{node\_name}\rangle .\langle \mathrm{function\_name}\rangle \langle \mathrm{file}\rangle .$
</div>

Here a file is constructed by executing a function at a node with data being supplied to the function as another file. Sets of assignments can be executed in sequence or in parallel. For example to display a graph comparing sales and marketing in the first quarter of 1985 in district F the following agent could be used:

```txt
agent
    seq
    par
    data1 := marketing.trends {{district F, 1985, quarter 1}}
    data2 := sales.profit {{[1985, 1, F, price = 20.5]}}
    end par
    screen := graphcomp {datal, data2}
    end seq
end agent
```

The data retrieval from nodes 'sales' and 'marketing' can proceed in parallel; once they have both completed, the local function 'graphcomp' is executed with the results going to 'file' screen. The visual display of the node is considered to be a file called screen (the keyboard is a function called keyboard). The characters within square brackets form file constants.

The agent language provides facilities for loops and conditional statements. It also has an exception handling facility that deals with:

(i) Nodes not in existence.

(ii) Functions not available on specified node.

(iii) Functions failing during execution.

This latter point is an important one. A DDM system cannot assume well engineered components, functions will fail from time to time and the agent language must cater for this.

Another example of an agent program (in AL) is given below. It is based on a program given by Bonczek et al. [9].

```verilog
agent
year : integer
fsale : array of integer
seq
    sale := sales.retrieve {[year v 10]}
    coef := regress {[sale year]}
    for year in 1 .. 10 do
    fsale [year] := forecast {coef + [sale] +
    year}
    screen := plot {fsale + year}
    end do
    screen := display {newdata}
end seq
end agent
```

Sales values for the ten most recent years are retrieved from the sales node. A regression is run on sale against year and a forecast model is run using the coefficients from the regression and plots of predicted sales against future years are generated.

## 6. Implementation of a Prototype DDM System

In order to test the ideas of DDM a prototype implementation was undertaken. This was done under UNIX $^{1}$ on a single VAX $^{2}$ 750 machine. Although the model of DDM is distributed, physical distribution was not attempted in the prototype. Rather each node was associated with a permanently running process. To mirror the model closely, communication between nodes used a message-passing facility. Note that although the model for DDM is message-based this does not necessitate an implementation being message-based.

$^{1}$ Trademark of AT&T.

$^{2}$ Trademark of Digital Equipment Corporation.

A full description of the prototype is given by Rathwell and Burns [35]. The script was coded in C and a translator for AL was constructed using the compiler-compiler tool YACC [26]. Messages took the form of pointers to files with the pointers being passes between nodes using an inter-process communication primitive. A number of DDM related commands were available to the user including ones to register functions and execute agents. The node management software that implemented the script supported concurrency by creating a new child process to deal with each function and agent execution.

Experience with the system indicated that it was useful (i.e., users preferred it) to allow a node to 'disconnect' from the DDM system for periods of time. (For physically distributed systems it would be normal for nodes to be occasionally 'off-line'.) To contend with nodes being temporarily unavailable the name-servier node (the noticeboard) had its facilities extended so that it also acted as a store-and-forward centre for messages destined for off-line nodes. This capability now introduces the possibility of external function calls being delayed for periods of real-time; to deal with this the execution of an agent could be restricted to be within a specified period of time.

## 6.1. Use of Prototype System

The prototype was constructed to gain experience of providing distributed support. It was used in three distinct ways:

(a) To support the activities of a group of research staff in a computer science department.

(b) To implement a computerised decision-making conference using the Nominal Group Technique (NGT) [15].

(c) To implement a rule based scheduling system employing conflict resolution.

Each of these activities will be discussed briefly.

## 6.1.1. Computer-aided research project support

Research projects are large unique efforts which are intended to accomplish a specific objective (or objectives) usually within constraints of time and resources. In a university computing department there are normally a number of such projects with overlapping areas of activity and expertise. The planning and control of a project involves a number of functions (for example see discussion by Archibald [6]) and the co-ordination and consultation between research workers has a critical effect upon the success of a project. However as Allen's [4] study has shown, consultation between researchers is heavily dependent on physical proximity.

To give DDM support each researcher becomes a distinct node on the system. These personnel were already familiar with electronic mail and started to use the DDM prototype to share facilities such as the tools they had developed to access local reference databases. Other activities that use the DDM are

(i) Constructing reports and papers;

(ii) Prototyping distributed software systems;

(iii) Collecting and analysis of experimental results;

(iv) Sharing software tools;

(v) Exchanging information (ideas and problems).

The information exchange leads to the need to support computer conferencing. The basic functions and agents that could be used to construct such a conference were added to the basic set of facilities at each node. The commands introduced were based on Telecenter [32].

Although it was felt that further support for project management and planning was possible and desirable such support did not emerge. This was probably due to the lack of any DSS software within the department that could have introduced such facilities.

## 6.1.2. NGT system design

The nominal group technique [15] is a non-computerised decision-making conference that aims to arrive at a plan of action that has consensus support. Each conference has a theme and proceeds through a number of distinct stages:

(i) idea generation;

(ii) discussion of ideas;

(iii) preliminary vote (ranking) on ideas;

(iv) discussion or preliminary vote; and

(v) final vote and report.

The aim is to produce a list of ideas recommended by the group, based on the conference theme. It is advocated in situations demanding complex decision making where aggregates of individual judgments are needed.

Using a number of functions that had emerged from the introduction of a normal computer conferencing facility a computerised NGT was (relatively easily) constructed. It has a number of advantages over the manual system.

(a) It managed the technical aspects of the process, i.e., bringing all the ideas to all the participants and dealing with the two voting stages.

(b) It enabled the technique to be used without bringing all the relevant staff together for a (typically) day long meeting. The computerised event could take place over a one or two week period.

(c) Most significantly, it enabled the ideas being generated to be anonymous. The personality or position of an individual could no longer affect the amount of support (in the vote) his or her ideas obtained.

## 6.1.3. Resource scheduling

One of the primary requirements of a fully implemented and working DDM system is that it should support conflict resolution. The provision of operator sharing allows such support to be given and various techniques are possible (including NGT discussed above). One approach that was facilitated by the prototype was a resource scheduler that used heuristics to resolve competing requests for the provision of some resource (any organisation resource is applicable here).

The node that manages the resource makes available a function that other nodes call if they wish to make a request. The form of the request is fairly free format and can include any information/evidence the requester wishes to include. To allocate the resource (or resources) the manager runs an expert system that allocates the resource and resolves conflicting requests using a rule-base. If a situation arises that is in some sense new (i.e., there is no rule set that will resolve the conflict) the manager is requested to manually choose between the concerned requests. In doing this he or she is invited to add a new rule (or rules) that encapsulate the decision they have just made. A similar conflict in the future will now be resolved by the rule-base.

The resource allocator (incorporating the expert system) was written in PROLOG as an MSc project [48]. An important property of most expert system is that it can explain how it arrived at its conclusions. If a resource request is unsuccessful the DDM system is used to send a detailed explanation of why this has happened including the rules that were fired. In doing this it is hoped that the conflict that results from a lack of information, or misinformation, will be minimised. Indeed there is no reason why a further DDM function could not be added so that a client can challenge the analysis of the expert system.

## 6.2. Discussion

The model produced enabled links between support systems to be established and the prototype allowed group decision-making activities to be studied. The applications developed in the use of the prototype DDM system showed a number of characteristics:

(1) It was not possible to design these applications as a full system.

(2) Usage of the system was unpredictable.

(3) The system developed showed evolutionary growth

(4) Ownership of the separate support system by their developers was important.

Our analysis of these applications has reinforced our initial view of the requirements of a DDM.

All the needs of the DDM (as specified earlier in section 3) were met in the model and its implementation. However many of the organisational issues that form the basis of the DDM approach were not present within a single university department. Moreover within the department there are not many standard DSS tools in use. There is clearly need for future experimentation with the DDM structure.

The prototype performed well even though efficiently of operation was not a primary requirement of the implementation. Clearly such issues would be important in a production version. To make the system more portable the script has recently been recoded into Ada [30].

## 7. Conclusions

The theoretical base of DDM has combined work in DSSs, distributed computing and organisational decision making. It extends the DSS concept to one that enables two or more decision making parties to co-operate in using DSS tools. It assumes a framework of organisational decision making which concentrates on the organisation as a political system with potential conflict between groups just as likely as consensus. This DDM is built upon the layer of DSS in an organisation and provides a mechanism for separate DSSs to interact, enabling groups, not necessarily linked in a hierarchical manner, to co-operate with one another. Whereas the focus of DSS is on decision making, the focus of DDM is on organisational communication and conflict in decision making.

As Pulkkinen's work has shown [33] there is a clear relationship between the development of structure and process in an organisation and the support of decision-making. Indeed one can stimulate the other. DDM is a flexible system that will support a variety of organisational structures from the hierarchical to the matrix and network systems based on autonomous working groups. The design, implementation and use of a DDM system however, is assumed to have a non-neutral effect upon the decision-making process.

This paper has reviewed the initial analysis from which the DDM model emerged. A more complete analysis is to be found elsewhere $[36,37,44]$ . The model is based on controlled operator sharing. In the classification of DSS architectures given by Sprague and Carlson $[40]$ the DDM federation best fits the bridge structure for a DSS (without data sharing). A prototype has been implemented which incorporates an agent language containing explicit parallelism for programming distributed system functions. The use of the prototype has supported the principles from which DDM was designed. Future implementations are now needed.

## References

[1] R.L. Ackoff, The future of operational research is past, Journal of the Operational Research Society 30, 2 (February 1979) 93–104.

[2] R.L. Ackoff, Resurrecting the Future of Operational Research, Journal of the Operational Research Society 30, 3 (March 1979) 189–199.

[3] G. Adriav and M.J. Ginzberg, DSS Design: A Systemic View of Decision Support, Communications of the ACM 28, 10 (1985) 1045–1052.

[4] T.J. Allen, Communications in R&D organizations, Technology Review (October–November 1967) 31–37.

[5] J.M. Amos and B.R. Sarchet, Management for Engineers, Prentice-Hall (1981).

[6] R.D. Archibald, Managing high technology programs and projects, Wiley (1976).

[7] G. Barber and C. Hewitt, Foundations for Office Semantics, in: N. Naffah, ed., Office Information Systems, INRIA/North-Holland, Amsterdam (1982).

[8] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Foundations of decision support systems, Academic Press, New York 1981.

[9] R.H. Bonczek, N. Ghiaseddin, C.W. Holsapple and A.B. Whinston, The DSS development system, National Computer Conference, U.S.A., 1983, 421–435.

[10] P.E. Boneham, Industrial Democracy and Information Systems, Computer Bulletin 20 (June 1979) 10–11.

[11] G. Bracchi and B. Pernici, SOS: A Conceptual Model for Office Information Systems, Data Base (Winter 1984) 11–18.

[12] F.P. Brooks, The Mythical Man-Month: Essays on Software Engineering, Addison-Wesley, Reading, MA (1975).

[13] K.J. Byrd, S.E. Smith and S.P. Jong, An Actor-Based Programming System, Proceedings of the First SIGOA Conference on Office Information Systems, Philadelphia, PA (June 1982).

[14] P.M. Cashman and A.W. Holt, A Communication-oriented Approach to Structuring the Software Maintenance Environment, ACM Software Engineering Notes 5, 1 (January 1980) 4–17.

[15] A.L. Delbecq, A. Van de Ven and D.H. Gustafson, Group Techniques for Program Planning, Scott, Foresman and Company, Gienview, IL (1975).

[16] W. Dzida, Computer Mediated Messaging for Interactive Purposes, in: R.P. Uhlig, ed., Computer Message Systems, North-Holland, Amsterdam (1981) 79–87.

[17] C. Ellis, An Office Information System Based on Migrating Processes, in: N. Naffah, ed., Office Information Systems, INRIA/North-Holland, Amsterdam (1982).

[18] L.D. Erman, F. Hayes-Roth, V.R. Lesser and D.R. Reddy, The Hearsay-II Speech Understanding System: Integrating Knowledge to Resolve Uncertainty, Computing Surveys 12, 2 (1980) 213–253.

[19] M.J. Gannon, Management: An Organisational Perspective, Little, Brown and Company (1977).

[20] S.J. Gibbs, Office Information Models and the Representation of 'Office Objects', Proceedings of the First SIGOA Conference on Office Information Systems, Philadelphia, PA (June 1982) 21–26.

[21] I. Greif and C. Hewitt, Actor semantics of PLANNER -73, Proceedings of 2nd ACM Symposium on Principles of Programming Languages (1975) 67–77.

[22] C. Hewitt, Viewing Control Structures as Patterns of Passing Messages, Artificial Intelligence 8 (1977) 323–364.

[23] C. Hewitt and H. Baker, Laws for communicating parallel processes, Proceedings of IFIP-77, Toronto (1977) 987–997.

[24] R.S. Hiltz and M. Turoff, The Network Nation, Addison-Wesley, Reading, MA (1978).

[25] G. Huber, Issues in the Design of Group Decision Support Systems, MIS Quarterly 8, 3 (September 1984) 195–204.

[26] S.C. Johnson, Yacc-Yet Another Compiler-Compiler, Computer Science Technical Report No. 32, Bell Laboratories, Murray Hill, NJ (1978).

[27] P.G.W. Keen and R.D. Hackathorn, Decision Support Systems and Personal Computing, Sloan School of Management Working Paper 1088-79, Cambridge, MA (1979).

[28] R. Kling, Social Analyses of Computing: Theoretical Perspectives in Recent Empirical Research, Computing Surveys 12, 1 (March 1980) 61–110.

[29] R. Kupperman, R. Wilcox and H. Smith, Crisis Management: Some Opportunities, Science 187, 4175 (February 1975) 404–410.

[30] B. Napjus, Implementing Distributed Decision-Making Systems, M. Phil Thesis, University of Bradford (1986).

[31] E.J. Neuhold and G. Rabe, Co-operative Use-Development of Interactive Systems, Online 72 Conference Proceedings 1, Brunel University, Uxbridge (September 1972) 165–185.

[32] M.L. Pearson and J.E. Kulp, Creating an Adaptive Computerized Conferencing System on Unix, in: R.P. Uhlig, ed., Computer Message Systems, North-Holland, Amsterdam (1981) 129–143.

[33] K. Pulkkinen, The Premises for Decision Support Systems, B-55, Helsinki School of Economics, Helsinki (1982).

[34] M.A. Rathwell and A. Burns, AL: A Command Language for Distributed Support Systems, Computer Centre Research Report, CCR.48, University of Bradford (1984).

[35] M.A. Rathwell and A. Burns, Distributed Decision Making under UNIX, EUUG Spring Conference, Nijmegen (April, 1984) 22–32.

[36] M.A. Rathwell, Distributed Decision-Making Systems, Ph.D. Thesis, University of Bradford (1985).

[37] M.A. Rathwell and A. Burns, Information Systems Support for Group Planning and Decision-Making Activities, MIS Quarterly 9, 3 (1985) 255–272.

[38] J.M. Scher, Distributed Decision Support Systems for Management and Organizations, DSS-81 Transactions, First International Conference on Decision Support Systems, Atlanta, GA (June, 1981) 130–140.

[39] R.G. Smith and R. Davis, Frameworks for Cooperation in Distributed Problem Solving, IEEE Transactions on Systems, Man and Cybernetics SMC-11, 1 (1981) 61–70.

[40] R.H. Sprague and E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, NJ (1982).

[41] B.I. Strom, Computer Conferencing-Past, Present, and Future, in: N. Naffah, ed., Office Information Systems, INRIA/North-Holland, Amsterdam (1982).

[42] R.R. Tenney and N.R. Sandell, Structures for Distributed Decisionmaking, IEEE Transactions on Systems, Man and Cybernetics SMC-11, 8 (1981) 517–527.

[43] R.R. Tenney, The Role of Distributed Knowledge in Distributed Decisionmaking, Proceedings IEEE International Lage Scale Systems Symposium, Virginia Beach, CA (October, 1982) 487–490.

[44] R.C. Thomas and A. Burns, The Case for Distributed Decision Making Systems, Computer Journal 25, 1 (February, 1982) 147–152.

[45] D.A. Waterman, A Rule-Based Approach to Knowledge Acquisition for Man-Machine Interface Programs, International Journal of Man-machine Studies 10 (1978) 693–711.

[46] M.D. Zisman, Use of Production Systems for Modeling Asynchronous, Concurrent Processes, in: D.A. Waterman and F. Hayes-Roth, eds., Pattern-Directed Inference Systems, Academic Press (1978).

[47] R.W. Zmud, Large-Scale Interconnected Information Systems ..., in: Proc. Large Scale Interconnected Systems, Athens, School of Business Administration, Univ. North Carolina (1983) 139–149.

[48] J. Zuker, An Expert System Scheduler for Resource Allocation, M.Sc. Dissertation, University of Bradford (1984).

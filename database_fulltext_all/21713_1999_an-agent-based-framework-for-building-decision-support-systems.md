---
otero_id: 21713
otero_key: "BC4UEEHG"
title: "An agent-based framework for building decision support systems"
authors: "Tung Bui; Jintae Lee"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00008-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An agent-based framework for building decision support systems

Tung Bui <sup>)</sup>, Jintae Lee <sup>1</sup>

UniÕersity of Hawaii at Manoa, E303, 2404 Maile Way, Honolulu, HI 96822, USA

## Abstract

This paper proposes a framework for building decision support systems using software agent technology to support organizations characterized by physically distributed, enterprise-wide, heterogeneous information systems. Intelligent agents have offered tremendous potential in supporting well-defined tasks such as information filtering, data mining and data conversion. However, the use of intelligent agents to support decisions has not been explored and merits serious consideration. This paper proposes a taxonomy of agent characteristics that can be used to help identify agents to support different types of decision tasks. We advocate a goal-directed, behavior-based architecture for building cooperative decision support using agents. We look at the development of agent-based DSS as being a process of putting together a coordinated workflow of collaborating agents that is able to support a problem-solving process. The methodology is illustrated by a selection of intelligent agents to support Crisis Action Procedures in a large organization. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Decision support systems; System analysis and design; Software agents; Organizational computing

## 1. Introduction

As the networked organization reaches the new frontiers of workplace e.g., flexible organization, Ž electronic commerce , some form of computer-based. organizational intelligence will be required to allow the competitive organization to stay abreast of the fast changing environment—in particular, new forms of business alliances or integration. Organizations are now exploring the use of Internet-based clientserver architecture allowing their large and interdependent functional units to migrate into independent and domain specific platforms, yet capable of interfacing with each other. Recent deployment of the global banking systems and the explosive growth of Web-based electronic commerce are examples of widely publicized success stories. Another more agent-specific example is the Carnot project initiated in 1990 with the attempt to logically unify physically distributed, enterprise-wide, heterogeneous information 28 . Carnot is intended to provide its user with<sup>w</sup> <sup>x</sup> the means to navigate information efficiently and transparently, to update that information consistently and to write applications easily for large, heterogeneous, distributed information systems—systems where resources may even reside on the conventional, closed environments that pervade businesses worldwide 27 .<sup>w</sup> <sup>x</sup>

Early DSS work advocates the development of DSS generators 25 to allow users to quickly de- <sup>w</sup> <sup>x</sup> velop application-specific DSS. DSS applications have been so specific and their deployment is, more often than not, confined to a small number of users. Furthermore, they do not support integration with other Internet-based information resources, and do not benefit from re-use of other DSS components developed elsewhere 1 . Given the Internet infrastructure, DSS now has the potential of being disseminated better 15 . Toward this end and from an<sup>w</sup> <sup>x</sup> organization decision making perspective, we view the DSS of the future as one that support missiondriven and distributed workflow. Furthermore, from a system design and implementation point of view, we view the DSS of the future as one that maximize the re-use of DSS components to deliver relevant, fast and reliable decision support. Finally, we envision a DSS platform in which DSS components are designed and coordinated in such a manner that would best fit the workflow of a business decision by searching for a workgroup that consists of human and non-human workers.

In this paper, we propose the use of software agents as DSS components to build cooperative decision support systems characterized by cooperating agents, either human or non-human actors. The proposed framework expands some of the early work in software agents e.g., Ref. 17 to the context ofŽ <sup>w</sup> <sup>x</sup>. DSS technology. In particular, it is inspired by modeling technologies from von Neumann’s work on self-reproducing automata, distributed artificial intelligence, agent-based modeling to social science <sup>w</sup> <sup>x</sup> 2,5,8 .

The paper is organized as follows. Software agents, as aids to human decision-makers, are described in Section 2. We discuss various characteristics of software agents, suggest its architecture and present a framework for agent coordination and interaction. A development lifecycle for building agent-based DSS is proposed in Section 3. Section 4 illustrates our approach with the design of crisis action procedures.

## 2. Software agents—a DSS perspective

We contend that Internet-based DSS are a special form of Cooperative Information Systems CIS . CISŽ . are characterized by cooperating agents, either human or non-human actors<sup>r</sup>users 6 . Cooperative <sup>w</sup> <sup>x</sup> systems are typically designed to perform complex but more or less pre-determined business tasks or processes. In such systems, the effectiveness of a DSS to support them depends on the interaction capacity of the individual agents operating under rules that place only bounded demands on each agent’s information and computational capacity.

## 2.1. Characteristics of software agents

A software agent, intelligent or not, is a program that performs a specific task on behalf of a user, independently or with little guidance. An intelligent agent performs, reactively and<sup>r</sup>or pro-actively, interactive tasks tailored to a user’s needs without humans or other agents telling it what to do. To accomplish these tasks, it should possess the following general characteristics of 16 : <sup>w</sup> <sup>x</sup>

<sup>Ø</sup> Independence

<sup>Ø</sup> Learning

<sup>Ø</sup> Cooperation

<sup>Ø</sup> Reasoning

<sup>Ø</sup> Intelligence.

Agents are the result of a paradigm shift in developing application software. Software is no longer regarded as a tool. Rather, it is considered as an autonomous assistant to the users—simulating a human relationship, hence the word ‘Personal Assistant’ in the software engineering literature. In other words, the traditional approach to software development is a reactive one in that the computer is programmed to react to the user’s instruction. Instead, the software agent approach is a pro-active one, in that the user specifies what he<sup>r</sup>she wants the computer to accomplish, and the latter performs tasks on behalf of the users. By analogy, a software agent mimics the role of an intelligent, dedicated and competent personal assistant e.g., a secretary of a Ž busy executive, or a medical assistant of an engaged physician . In a network, an agent can be seen as a . program that, once sent across the network, encapsulates the user’s instructions and executes it with little guidance. Creating a new Internet-based agent may involve as simple steps e.g., using Surfbot monitor- Ž ing agent, www.surflogic.com as:.

<sup>Ø</sup> Identify working file location sŽ .

<sup>Ø</sup> Determine desired amount of information volumeŽ and time frame.

<sup>Ø</sup> Select search extent e.g., how many linksŽ .

<sup>Ø</sup> Choose presentation<sup>r</sup>report style.

Agents, such as the Surfbot agent, have been primarily focused to information search and retrieval, and manage information overload. Some others perform repetitive activities and certain specific tasks such as scheduling and interface presentation e.g.,Ž Refs. 21,29 .<sup>w</sup> <sup>x</sup>.

In addition to the role of:

<sup>Ø</sup> Information gatherer

<sup>Ø</sup> Information filter

<sup>Ø</sup> Information learner,

an intelligent software agent should be able to support various phases of the decision making and problem solving process, and serves as a:

<sup>Ø</sup> Problem analyzer

<sup>Ø</sup> Problem solver

<sup>Ø</sup> Implementation agent

<sup>Ø</sup> Monitoring agent

<sup>Ø</sup> Negotiating and conflict resolution agent.

More important and unlike routine tasks that can be automated, decision making involves complex set of tasks that requires integration of supporting agents. To work together, these agents should have behaviors to work in team e.g., Refs. 20,22 with theŽ <sup>w</sup> <sup>x</sup>. ability to:

<sup>Ø</sup> Recall e.g., the extent to which relevant informa-Ž tion is retrieved.

<sup>Ø</sup> Execute tasks with precision e.g., the extent toŽ which gathered information matches decision tasks in the case of information search.

<sup>Ø</sup> Exhibit good citizenship e.g., avoid unnecessaryŽ interaction with other entities<sup>r</sup>agents; report errors.

Later, we will discuss a framework for managing a federation of agents to support decision-making.

## 2.2. A generic software agent architecture

An agent possesses certain skills and knowledge to interact with the user s or other applications Ž . Ž . cooperation, communication, command and control . A generic architecture of a software agent is depicted in Fig. 1.

The user interacts with the agent via the User– Agent Interface or Adapter 14 . This allows the user<sup>w</sup> <sup>x</sup> to retain the current application and add agent capability to the extent required. In other words, the interface role is to pass the agent’s skills and knowledge in the user’s format. The agent uses its embedded procedures Agent’s Processing Engine and re- Ž . lated data Agent’s Repository to perform tasks andŽ . exchange information via a view. A set of views defines the standards of interaction between the user and the agent, and provides the user with a choice of how the information is presented. The electronic mailbox is an example of the view framework 23 .<sup>w</sup> <sup>x</sup>

![](/api/attachments/BC4UEEHG/fulltext/images/fc9aa3daae767bd37c0498cee62cfaf6f1c5ad311508fea5ecd45df320fae6c2.jpg)  
Other software agents/applications  
Fig. 1. A generic software agent architecture.

The repository contains facts and rules allowing agents to reason and learn. It represents the persistent storage of knowledge. Facts are collected from triggering events or sensors short term facts , fromŽ . existing data bases long term facts or derived from Ž . reasoning beliefs . The processing engine also con-Ž . tains the agent’s current understanding of the user and the instructions received from the user.

## 2.3. Characteristics of software agents

Not all software agents are, nor should be, alike. Instead, they should be tailored to problem specifications. In this section, we have identified eight dimensions that could be used to help determine the characteristics of an agent Table 1 .Ž .

Intelligence refers to the skills the user can expect from the agent. An agent could be designed to have rigid based on fixed and simple rules , some reason- Ž .

Table 1  
Spectrum of software agent characteristics

<table><tr><td>Intelligence</td><td>Rigid/automated</td><td>Reasoning</td><td>Planning</td><td>Learning</td></tr><tr><td>Mobility</td><td>Stationary</td><td></td><td></td><td>Mobile</td></tr><tr><td>Lifetime</td><td>Adhoc</td><td>Cloning</td><td></td><td>Persistent</td></tr><tr><td>Interaction</td><td>Agent-to-agent</td><td>Agent-to-application</td><td></td><td>Agent-to-user</td></tr><tr><td>Task Specificity</td><td>Specific</td><td></td><td></td><td>General</td></tr><tr><td>Initiative</td><td>Push</td><td></td><td></td><td>Pull</td></tr><tr><td>Environment</td><td>Stable/secure</td><td></td><td></td><td>Stochastic/insecure</td></tr></table>

ing capability i.e., can make some inferences from Ž user , planning skills able to plan actions indepen- . Ž dent of user input , and learning skills i.e., able to. Ž learn and adapt behavior based on user’s usage patterns . Learning can range from simple counters . of events to past memories with backtracking capability, to associative memories, to predictive models to time series and beyond.

An agent can have various levels of mobility. A stationary agent resides on one or multiple sites. A mobile agent is able to package itself, with all state information, move from one place to another throughout the distributed network that hosts the DSS, install itself on a remote site and begin execution.

Ad hoc agents execute their assigned task s andŽ . end gracefully. Cloning agents can send copies of themselves to other computers. A reason for cloning agents is to make searches and deployment more efficient. Persistent agents do not die after the task is completed. It can live on local or remote processing site e.g., server .Ž .

Agents need guidance from users. Guidance can be as simple as data input or as complex as a complete business application. Agents can interact with other agents, whether of the same type or not. Alternately, an agent can work with other non-agent applications such as databases, web browsers, spreadsheets, etc. Agent interaction can be one of the following types:

<sup>.</sup> Agent acts independently and autonomously of user e.g., fetches updates to users without their Ž request ..

<sup>.</sup> Agent acts independently of user, but takes into consideration user’s request e.g., gathers and Ž filters new data based on user criteria ..

<sup>.</sup> Agent acts independently of user, but understands user’s needs, interacts with other entities such as data, applications, or services on behalf of user Že.g., fetches and filters information from various applications and formats data according to user’s specifications ..

<sup>.</sup> Agent acts independently of user, but understands user’s needs, collaborates and negotiates with other agents e.g., works with other agents to solve a Ž complex decision algorithm ..

<sup>.</sup> Agent acts independently of user, but understands user’s needs, collaborates and negotiates with other agents and user e.g., work with other agentsŽ and interacts with user for input, feedback and decision ..

Agents can be assigned to a generic task or to a task that requires specific knowledge. An agent can be programmed to be competitive i.e., asked to Ž optimize own function possibly at the expense of. other agents or applications. It can also be programmed to behave cooperatively enabling it to collaborate as a team with other agents or applications. Information delivery can be either push i.e., provid-Ž ing information to users when it deems necessary or. pull i.e., at the user’s request .Ž .

Finally, agents can operate in a stable and secure environment characterized by predictable operating conditions or in unstable and insecure platforms necessitating additional skills, knowledge and interface functionalities.

We advocate that the characteristics of an agent has to be tailored to the problem-solving tasks as well as the user’s decision-making style in order to promote trust and confidence between the user and the agents that serve him<sup>r</sup>her.

## 2.4. Coordinating agents’ actiÕities

Normally, complex decision making tasks cannot be done by a single agent. Rather, they are typically achieved through a coordinated effort of many agents with different sets of expertise and assignment. Research in multi-agent systems can be classified into two design paradigms: an autonomy-centered approach vs. distributed problem solving. For a thor-Ž ough survey of these paradigms, see for example, Refs. 2,5,8 .<sup>w</sup> <sup>x</sup> .

The main goal of this section is to describe a coordination theory that can be used to create a coordination characteristic table, which in turn will be used later to determine ideal coordination characteristics among multiple agents for different tasks. Coordination can be regarded as a special case of rules of behavior for the agents to interact with its environment. An example of a single execution rule of an agent is to initiate a processing module say,Ž computing a moving average when all data have . been received.

Since it is not our goal here to endorse a particular coordination theory, we could have chosen any of the existing theories of coordination e.g., Refs.Ž <sup>w</sup> <sup>x</sup> 9,12,13,24,26 . For the sake of concreteness, how-. ever, we choose to describe the coordination theory of Malone and Crowston 18 , with which we are<sup>w</sup> <sup>x</sup> most familiar.

In Ref. 18 , coordination is defined as manage- <sup>w</sup> <sup>x</sup> ment of dependencies among activities. Thus, analyzing coordination requires understanding of two components: the dependency involved and the mechanism used to manage the dependency. The Process Handbook project 19 has identified the types of <sup>w</sup> <sup>x</sup> dependencies and the associated mechanisms, as shown in Table 2. Our approach to defining coordination among agents builds on this work, which is described briefly below.

Dependencies arise from the needs to share resources between activities. Fig. 2 shows three basic kinds: flow, sharing and fit. Flow dependencies arise when one activity uses a resource that is produced by another activity—for example, an agent needs to have authorized access to a database before it can get information from it. Sharing dependencies arise when a resource needs to be shared by multiple activities. For example, a database as a resource has to be shared by multiple agents. Fit dependencies arise when the resources produced by multiple activities have to fit together in some way. For example, different kinds of information gathered by multiple agents have to be integrated to provide an overall view of a problem at hand.

These basic dependencies can be further specialized into more specific types of dependencies. As an example, a task assignment can be seen as a special case of sharing, where the ‘resource’ being shared is the time of people who can do the tasks. Also, a dependency may be decomposed into a set of dependencies. For instance, flow dependencies can be viewed as a combination of three other kinds of constraints: prerequisite constraints an item must beŽ produced before it can be used , accessibility con-. straints an item that is produced must be madeŽ available for use and usability constraints an item. Ž that is produced should be ‘usable’ by the activity that uses it ..

Examples of elementary dependencies between activities and alternative coordination mechanisms for managing them

<table><tr><td>Dependency</td><td>Examples of coordination mechanisms for managing dependency</td></tr><tr><td colspan="2">Flow</td></tr><tr><td>Prerequisite (&#x27;right time&#x27;)</td><td>Make to order vs. make to inventory (&#x27;pull&#x27; vs. &#x27;push&#x27;).Place orders using &#x27;economic order quantity&#x27;, &#x27;Just In Time&#x27;(kanban system), or detailed advanced planning</td></tr><tr><td>Accessibility (&#x27;right place&#x27;)</td><td>Ship by various transportation modes or make at point of use</td></tr><tr><td>Usability (&#x27;right thing&#x27;)</td><td>Use standards or ask individual users (e.g., by having customeragree to purchase and/or by using participatory design)</td></tr><tr><td>Sharing</td><td>‘First come/first serve&#x27;, priority order, budgets, managerialdecision, market-like bidding</td></tr><tr><td>Fit</td><td>Boeing&#x27;s total simulation vs. Microsoft&#x27;s daily build</td></tr></table>

![](/api/attachments/BC4UEEHG/fulltext/images/7f887e73ee2a9dbc840ee102beb9d8eb1eeb69755815385478121436684142b1.jpg)  
Fig. 2. Basic types of dependency taken from Ref. 19 . Ž <sup>w</sup> <sup>x</sup>.

For a given dependency type, we can identify a number of mechanisms, i.e., coordination processes, commonly used to manage it. For example, the prerequisite dependency might be managed by keeping an inventory of the resource or by making it to order when it is needed, while usability may be managed through a product design process. On the other hand, ‘sharing’ dependencies shared resourceŽ constraints can be managed by a variety of coordi-. nation mechanisms such as ‘first come<sup>r</sup>first serve’, priority order, budgets, managerial decision, and market-like bidding. Table 2 shows the dependency types and the mechanisms that can be used to manage them.

## 3. A development lifecycle for building agentbased DSS

Software development methodologies have evolved from the classic waterfall model 3 , to a<sup>w</sup> <sup>x</sup> spiral model 4 , to prototyping and, recently, to<sup>w</sup> <sup>x</sup> scenario-based design 7 . The latter models seem to<sup>w</sup> <sup>x</sup> have worked well for domain-specific, non-heterogeneous platform applications. In a physically distributed environment characterized by non-standard and non-communicating system components, additional considerations to account for components to adapt to each other is crucial for deploying Internetbased applications.

Developing an agent-based DSS requires a new approach. As suggested in Fig. 3, we advocate a two-tier approach to designing an agent-based DSS. The first tier is in essence an assignment model that consists of searching, identifying and selecting the agent s that are most appropriate to accomplish Ž . required tasks first three phases of the lifecycle in Ž Fig. 3 . The second aims at devising coordination.

and collaboration strategy for all the involved agents to work together the last two phases of the lifecycle . Ž .

Each of the phases of the lifecycle is described as follows.

## 3.1. Analyze problem task

This phase consists of performing decision support requirements and devising a detailed breakdown of all decision processes. Processes are sets of partially ordered steps intended to reach a particular goal. Process steps are the most primitive, atomic processes.

## 3.2. Specify agents’ functionality

This step involves iterative search of eligible agents or creation of new agents that satisfy the requirements as determined in the previous steps. Selection criteria include agent’s competence, reliability, and costs. Competence refers to the question how can the agent be built to possess the knowledge to decide when, with what, and how to perform a process step.

## 3.3. Specify agents’ behaÕior

A number of behaviors are specified in this phase. Instructions are prescribed for showing identifications; following exclusion standards<sup>r</sup>protocols; and using Web resources cost-effectively e.g., request Ž global information first, do breath-first search first, use same agent for repetitive tasks to minimize transportation costs, retrieve<sup>r</sup>broadcast information only what is needed at opportune time . Specification. and execution of agent’s problem solving and data management functionalities are tested locally for each of the selected agents. Agent ethics can also be reviewed here. The issues to be considered 11 include:

![](/api/attachments/BC4UEEHG/fulltext/images/6c3d036478cadf424c2ab2d77ac2cbc9ffe1283f5c60b3afe214f1ebbebe0f33.jpg)  
Fig. 3. A development lifecycle for agent-based DSS.

Safety—do not make destruction to the world Tidiness—leave the world as it first found it Thrift—limit the use scarce resource Vigilance—do not execute with unknown consequences.

## 3.4. Coordinating agents in problem solÕing flow

Selected agents are assigned to various tasks, given notification mechanism e.g., agent notifica- Ž tion, self-identification, etc. along with synchroniza-. tion protocols. Execution plan is outlined here for the entire problem solving flow.

## 4. A case study: modeling crisis action procedures

To illustrate the use of the proposed framework, we apply it to the development of an agent-based geographically distributed DSS for crisis action procedures. The goal of a crisis action procedure CAP ,Ž . e.g., as used by joint staffs in the US military, is to contain quickly and effectively crisis situations such as war, terrorism or nuclear accidents. As such, a CAP is a task that can benefit much from an agentbased DSS as it requires swift decision making and accurate information collection from multiple, geographically dispersed sources. The CAP described below is partly based on the description of such a procedure detailed in Ref. 10 .<sup>w</sup> <sup>x</sup>

![](/api/attachments/BC4UEEHG/fulltext/images/7aa6d70d18831c19da5f0d67ca811449e98a9dace4b548164a9aff4614fdda5a.jpg)  
Fig. 4. Decomposition of crisis action procedure phase 1: Identify Potential Problem Situation or Situation Development . Ž .

## 4.1. Analyze problem tasks

The first step in applying the method is to model the process currently in question. Based on experts experience, the topmost level step, CAP, is decomposed into a sequence of required tasks. Designed by experts in the field, Fig. 4 shows the five first-level sub-steps, the first of which is Identify Potential Problem Situation or Situation Development . This Ž . step, Identify Potential Problem Situation, is further decomposed into two steps: Recognize Problem and Submit CINC’s Commanders-in-Chief AssessmentŽ . because the latter two steps constitute what it means to perform the Identify Potential Problem Situation step. For example, Submit CINC’s Assessment has to be done because that step officially marks the conclusion of the step Identify Problem Situation. Similarly, the Recognize Problem step is shown explicitly in the decomposition because one has to be able to recognize a problem in order to identify potential problem situation.

## 4.2. Specify agent functionality

As discussed earlier, Fig. 4 represents a portion of the process model. Each process is represented in the figure by a node. The next step is to determine whether or not a software agent should be developed to implement that process, and if so, the most appropriate profile of that agent. A cost-benefit analysis is performed to justify the use of software agents. If justified, the individual characteristics of these agents are identified to best suit the defined process or tasks, and their coordination requirements with other agents—both human and software—are determined.

Due to limited space, we provide only description of a few agents to illustrate the analyses of the agents’ profile and their coordination characteristics. For example, the Identify the kind of information to monitor process is determined to be too important to be entirely entrusted to a software agent. Nonetheless, the agent can be designed to suggest possible information sources and learn from human decision. The benefit of such an agent is the detection of possible source of information that might have been overlooked whereas the cost is that of implementing a learning agent, which can be done in this case by customizing a little bit of the existing machine learning technique. Another potential cost is that of security what if this pattern gets leaked . Given that theŽ . interaction is user–agent with no intermediary, the security risk is small and even if the information leaks, it would not create any foreseeable problem. Based on this analysis, we decide to create an agent for this task, Identify the kind of information to monitor.

Table 3  
Agent profile for the step, Identify the kind of information to monitor

<table><tr><td>Agent attribute</td><td>Chosen characteristic</td><td>Rationale</td></tr><tr><td>Intelligence</td><td>learning and reasoning</td><td>need to suggest potentially relevant information sources by watching over the user&#x27;s pattern</td></tr><tr><td>Mobility</td><td>mobile</td><td>need to monitor new types of information distributed over the places</td></tr><tr><td>Lifetime</td><td>persistent or clone</td><td>need to constantly monitor for possible information source</td></tr><tr><td>Interaction</td><td>agent-user</td><td>need to suggest the result to the user</td></tr><tr><td>Task-specificity</td><td>domain-specific and general</td><td>need to know the dimensions along which things can be similar (e.g., size, shape, temporality, scale) as well as how things can be relevant to one another. Also needs specific knowledge about a particular type of crisis such as what types of information is likely to be important for different types of crises (e.g., natural disaster, potential war situation)</td></tr><tr><td>Initiative</td><td>push</td><td>need to notify when it finds useful result</td></tr></table>

Table 4  
Agent profile for the step, Decompose the task

<table><tr><td>Agent attribute</td><td>Chosen characteristic</td><td>Rationale</td></tr><tr><td>Intelligence</td><td>reasoning, planning and learning</td><td>need to reason about the best way to break down a task, which typically involves resource planning; need to also learn from experience</td></tr><tr><td>Mobility</td><td>static</td><td>need not itself move around</td></tr><tr><td>Lifetime</td><td>ad hoc</td><td>only needed when the task need to be decomposed, which can be just once in the beginning</td></tr><tr><td>Interaction</td><td>agent-application, agent-user</td><td>the decomposition can be given to the application or to the user if need to be confirmed</td></tr><tr><td>Task-specificity</td><td>domain-specific and general</td><td>needs to have task-specific knowledge to decide on the best decomposition, but also need to have general knowledge about modular organization and coordination issues</td></tr><tr><td>Initiative</td><td>pull</td><td>should be invoked only when needed</td></tr></table>

In order to create a profile for the agent, we examine each of the agent attributes cf. Section 2.3Ž . and determine the most appropriate value for it. Table 3 summarizes such a profile. For example, consider the attribute, Intelligence. The agent should not be rigid if it is to suggest possible sources of critical information because it should be able to infer the relevance of information for the given task. It would need some measure of reasoning and learning capability if it is to learn from the human user. On the basis of survey of the current state of art in learning agent, one may decide that the capability of exemplar-based learning would be most useful while meeting the reliability requirement. With exemplarbased learning, the agent would suggest information similar to the ones that have been previously selected by human user e.g., images of similar type, newsŽ containing similar keywords with the knowledge of. related words, and possibly suggest additional categories when a category is flooded with information. So each characteristic acts as a prompt that forces us to articulate the specific capability that we want and perform the cost<sup>r</sup>benefit analysis of its automation. As to the planning capability, It would not be necessary, though useful, in identifying the relevant information.

We decide that mobility is critical for this task because the agent would have to constantly monitor new types of information distributed over the places and assess their relevance. We also decide that the agent responsible for suggesting possible source of useful information has to be either persistent and<sup>r</sup>or cloning, depending on, among other factors, whether the distributed information sources allow a clone of the agent to be stationed there or not. For now, we leave both of these possibilities open.

As to the interaction attribute, we decided on the agent–user because the job of the agent is to suggest potentially relevant information to monitor. The agent also needs to have both general and specific knowledge in the task-specificity attribute. The agent has to have general knowledge of the dimensions along which things can be similar e.g., size, shape, tempo- Ž rality, scale as well as how things can be relevant to . one another e.g., relation between food shortage andŽ possible riot . It also needs specific knowledge about . a particular type of crisis such as what types of information is likely to be important for different types of crises e.g., natural disaster, potential warŽ situation . This agent would be more useful if it can. push when it finds additional source of information to suggest in contrast to the user having to pull to see if such is the case.

Table 5  
Agent profile for the step, Allocate the task by possibly generating subagents Ž .

<table><tr><td>Agent attribute</td><td>Chosen characteristic</td><td>Rationale</td></tr><tr><td>Intelligence</td><td>reasoning, planning and learning</td><td>need to reason about optimal matches between task and possible subagents, plan about how to pass relevant input that subagents might need and learn from experiences</td></tr><tr><td>Mobility</td><td>static</td><td>can be done in one place</td></tr><tr><td>Lifetime</td><td>ad hoc</td><td>can be done on-need basis so that it does not take up resource unnecessarily</td></tr><tr><td>Interaction</td><td>agent-application</td><td>need to pass the possible allocation to the application so that it can display to the user for confirmation or editing</td></tr><tr><td>Task-specificity</td><td>domain-specific and general</td><td>needs to have the general knowledge about allocation and specific knowledge about matching capabilities with requirements in a given domain</td></tr><tr><td>Initiative</td><td>pull</td><td>should be done on need basis</td></tr></table>

Table 6  
Agent profile for the step, Obtain Subproblem Solutions at the first level Ž .

<table><tr><td>Agent attribute</td><td>Chosen characteristic</td><td>Rationale</td></tr><tr><td>Intelligence</td><td>reasoning, planning and learning</td><td>need to create subagents, now according to the information medium that one has to deal with (e.g., text, image, database)</td></tr><tr><td>Mobility</td><td>mobile</td><td>need to monitor new types of information distributed over the places</td></tr><tr><td>Lifetime</td><td>clone</td><td>need to constantly monitor the information source</td></tr><tr><td>Interaction</td><td>agent-agent</td><td>need to pass back the result to the coordinating agent</td></tr><tr><td>Task-specificity</td><td>domain-specific</td><td>need to look for domain-specific cues</td></tr><tr><td>Initiative</td><td>push</td><td>need to notify when it finds matches</td></tr></table>

The next step is to examine the coordination characteristic or requirement of the agent. In this case and according to the adopted workflow, there is only one agent and the only coordination would be only between the agent and the user although the Ž agent or the user might have to coordinate among its local tasks . The environment and its characteristics. in which the agent will function is also analyzed. The environment is judged to be stable.

We then proceed to the next task, Collect the information according to the priority. This subprocess is actually a complex activity that decomposes into several subprocesses of its own: Decompose the task, Allocate the task, Obtain Subproblem Solution and Collect the results.

Tables 4 and 5 summarize the rationale of identifying the agents’ profile for the Decompose the tasks and Allocate the task processes, respectively. The agent responsible for decomposing a task or suggesting possible decompositions has to consider coordination issues among the subtasks. However, the agent itself need not be coordinated as long as there are no multiple agents sharing this task.

As far as the process Allocate the task is concerned, its coordination is simple because there is no flow dependency among the agents, each of which is simply responsible for the different types of information media. One need not worry about the fit dependency until the process of integrating the returned information is reached. Because of limited resources, however, we do need to manage the Shared Resource dependency in how much each subagent is allowed to spend. One possible mechanism for managing this dependency type is a market-like bidding. We would let the agents estimate the cost of information delivery and then allocate more resource to those agents who promise to deliver most valuable information with least cost. However, we decide that the overhead that would incur might delay the response and not justify the potential benefit. So we simply use the priority to allocate the available resource to the different agents.

Table 7  
Agent profile for the step, Obtain Subproblem Solutions at the second level Ž .

<table><tr><td>Agent attribute</td><td>Chosen characteristic</td><td>Rationale</td></tr><tr><td>Intelligence</td><td>rigid</td><td>collect information that matches certain pattern</td></tr><tr><td>Mobility</td><td>mobile</td><td>still need to traverse over physically distributed information sources though of the same medium and on the same topic</td></tr><tr><td>Lifetime</td><td>clone</td><td>will place a clone in each of the distinct information source if economically feasible</td></tr><tr><td>Interaction</td><td>agent-agent</td><td>need to pass back the result to the coordinating agent</td></tr><tr><td>Task-specificity</td><td>domain-specific</td><td>need to look for domain-specific cues</td></tr><tr><td>Initiative</td><td>push</td><td>need to notify when it finds matches</td></tr></table>

Table 8  
Agent profile for the step, Collect the Results

<table><tr><td>Agent attribute</td><td>Chosen characteristic</td><td>Rationale</td></tr><tr><td>Intelligence</td><td>rigid</td><td>need to merely bring the results together while their integration is left for the next step</td></tr><tr><td>Mobility</td><td>static</td><td>the results arrive whenever ready</td></tr><tr><td>Lifetime</td><td>persistent</td><td>need to be ready anytime to receive the results</td></tr><tr><td>Interaction</td><td>agent-agent</td><td>need to receive results from other agents</td></tr><tr><td>Task-specificity</td><td>general</td><td>need not understand the content of the results at this stage</td></tr><tr><td>Initiative</td><td>push</td><td>the results arrive whenever ready</td></tr></table>

The next task, Obtain Subproblem Solutions, involves actually getting the information on a given topic. However, because the information is spread over heterogeneous information media web, satelliteŽ pictures, audio files, news paper articles , we create. another layer of subagents, now specializing on a given type of information medium. Therefore, this task itself is recursively decomposed into the following subtasks: Decompose Task, Allocate Task, Obtain Subproblem Solution, Collect the Results. Therefore, this decomposition is a recursive application of the decomposition used at a higher level seeŽ Fig. 4 . Thus, we will not repeat this analysis further . except to note that the Obtain Subproblem Solution at this second level will not be recursively decomposed again but it will involve an agent actually looking for specific type of information over a specific information medium. Table 6 below summarizes the agent profile for the Obtain Subproblem Solution at the first level, whereas Table 7 summarizes one for the Obtain Subproblem Solution at the second level.

The coordination characteristics at the first level of the Obtain Subproblem Solution repeat those discussed so far for the Decompose Task, Allocate Task, Obtain Subproblem Solution, Collect the Results processes. And there is little coordination at the second level unless the Obtain Subproblem Solution process is decomposed yet again.

Collect the Results is the last step of the Collect the Information according to Priority process and Table 8 shows its agent profile. Because Obtain Subproblem Solution is recursively performed at two levels, so is the Collect Result process—collecting information of different medium at the second level while collecting information on different topics at the first level. Since the Collect the Result process merely brings the subsolutions into one place and leave the difficult problem of integrating and interpreting them for the next process, Integrate the Results, not much coordination is involved. However, if there is resource shortage, such as out of buffer space, that prevents accepting all the information, then priority will be used to decide to save more important type of information at the expense of deleting information on less important topics.

Table 9  
Coordination characteristics for the step, Identify information to monitor

<table><tr><td>Task</td><td>Coordination</td></tr><tr><td>Identify the Kind of Information to Monitor</td><td>non agent-to-agent coordinationagent-to-user coordination (among local tasks)</td></tr><tr><td>Decompose the Task</td><td>no coordination required</td></tr><tr><td>Allocate the Task</td><td>no fit dependency requiredbidding for low cost</td></tr><tr><td>Obtain Subproblem Solutions</td><td>little coordination</td></tr><tr><td>Collect the Result</td><td>little coordination; but if there is resource shortage (such as out of buffer space),need to manage the fit dependency (e.g., with a priority scheme)</td></tr></table>

We can perform a similar analysis for each of the rest of the processes and identify appropriate agent profiles, but they are not presented in this paper due to the limited space. The coordination characteristics of these agents need to be similarly analyzed. Table 9 shows a summary of such analyses for the processes discussed so far.

the selection of agents when there are more than one agent that meet the requirements; Should we try using or contracting the service of an existing agent or implement our own? In the case of reusing existing agents, which one should we select? Another set of issues has to do with the assessment of the environmental properties—e.g., the likelihood of its stability and security. Unfortunately, these issues would have to be addressed on a case-by-case basis and the current method does not offer much help. Nevertheless, we believe that the method does provide a framework in which such questions can be identified and articulated more easily.

## 5. Conclusion

In this paper, we present an agent-based framework to design decision support systems for distributed organizations. We propose a taxonomy of agent characteristics. The taxonomy can be used to help identify different types of agents to support different types of decision tasks. We also propose a development lifecycle that looks at agent-based DSS as being a design of coordinated agents to optimally support a problem-solving process. In particular, we suggest a two-level development process. The micro-level seeks to identify and specify agents to handle specific decision support tasks, whereas the macro-level seeks to coordinate various agents to optimally support the entire decision-making process. We are currently experimenting with the proposed approach to support military reconnaissancerelated decisions.

To conclude, we would like to enumerate a few caveats in the application of the proposed method. The analysis and design phases in any software development cycle are critical and usually require careful, often tedious, attention to details. The proposed method is no exception. Its main contribution is not in the reduction of careful attention required but in the systematic guidance it provides in the direction of such efforts. There are also many issues other than those discussed in this paper that one would have to face in the application of the method proposed. For example, a set of such issues concerns

## References

<sup>w</sup> <sup>x</sup> 1 H.K. Bhargava, R. Krishnan, R. Mueller, Decision support on demand: emerging electronic markets for decision technologies, Decision Support Systems 1997 .Ž .

<sup>w</sup> <sup>x</sup> 2 S.D. Bird, Towards a taxonomy of multi-agent systems, International Journal of Man–Machine Studies 39 1993Ž . 689–704.

<sup>w</sup> <sup>x</sup> 3 B. Boehm, Software engineering, IEEE Transactions on Computers 25 12 1976 1226–1241.Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 B. Boehm, A spiral model of software development and enhancement, IEEE Computer 21 5 1988 61–72.Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 A. Bond, L. Gasser Eds. , Readings in Distributed ArtificialŽ . Intelligence San Mateo, Morgan Kaufman Publishers, 1988.

<sup>w</sup> <sup>x</sup> 6 C. Bussler, S. Jablonski, Implementing agent coordination for workflow management systems using active database systems, Proceedings of the Fourth International Workshop on Research Issues in Data Engineering, 1994, pp. 53–59.

<sup>w</sup> <sup>x</sup> 7 J.M. Carroll Ed. , Scenario-Based Design in: Envisioning Ž . Work and Technology in System Development, Wiley, New York, 1995.

<sup>w</sup> <sup>x</sup> 8 B. Chaib-draa, R. Mandiau, P. Millot, Distributed artificial intelligence: an annotated bibliography, SIGART Bulletin 3 Ž . Ž . 3 1992 .

<sup>w</sup> <sup>x</sup> 9 E. Durfee, V. Lesser et al., Coherent cooperation among communicating problem solvers, IEEE Transactions on Computers C 36 1987 1275–1291.Ž .

<sup>w</sup> <sup>x</sup> 10 M.R. Edmiston, D.R. Gregg Jr., et al., Decision Support for Reconnaissance Using Intelligence Software Agents, Department of Systems Management, Naval Postgraduate School, Monterey, 1998.

<sup>w</sup> <sup>x</sup> 11 O. Etzioni, D.S. Weld, Intelligent agents on the internet: fact, fiction and forecast, IEEE Expert Intelligent Systems and Their Applications August 1996 .Ž .

<sup>w</sup> <sup>x</sup> 12 L. Gasser, Distribution and coordination of tasks among intelligent agents, Proceedings of the First Scandinavian Conference n Artificial Intelligence, International Organisations Services, Amsterdam, The Netherlands, 1988.

<sup>w</sup> <sup>x</sup> 13 R.V. Guha, D.B. Lenat, Enabling agents to work together, Communications of the ACM 37 7 1994 127–142.Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 IBM, IBM Agent Building Environment Developer’s Toolkit, Level 5, IBM Agent Center of Competence, March 1997, http:<sup>r</sup>www.networking.ibm.com<sup>r</sup>iag<sup>r</sup>iaghom.html.

<sup>w</sup> <sup>x</sup> 15 M. Jeusfeld, T. Bui, Distributed decision support and organization connectivity: a case study, Decision Support Systems 19 3 1997 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 16 R. Kalaoka, A. Whinston, The Frontiers of Electronic Commerce, Addison-Wesley, 1996.

<sup>w</sup> <sup>x</sup> 17 H. Kautz, B. Selman, M. Coan, Bottom-up design of software agents, Communications of the ACM 37 1992 .Ž .

<sup>w</sup> <sup>x</sup> 18 T. Malone, K. Crowston, The interdisciplinary study of coordination, ACM Computing Surveys 26 1994 87–119.Ž .

<sup>w</sup> <sup>x</sup> 19 T.W. Malone, K. Crowston, J. Lee et al., Tools for Inventing Organizations: Toward a Handbook of Organizational Processes, accepted for publication in Management Science Ž .1998 .

<sup>w</sup> <sup>x</sup> 20 T.J. Norman, D. Long, Proposal for goal creation in motivated agents, Proceedings of the 1994 Workshop on Agent Theories, Architectures and Languages 1994 .Ž .

<sup>w</sup> <sup>x</sup> 21 D.E. O’Leary, AI and navigation on the internet and intranet, IEEE Expert Intelligent Systems and Their Applications 11 Ž . Ž .2 1996 8–10.

<sup>w</sup> <sup>x</sup> 22 A. Ortony, G. Clore, A. Collins, The Cognitive of Emotions, Cambridge Univ. Press, 1988.

<sup>w</sup> <sup>x</sup> 23 A. Poggi, HOMAGE: a heterogeneous object-based environment to develop multi-agent systems, Proceedings of the 29th Hawaii International Conference on System Sciences 1996Ž . 282–289.

<sup>w</sup> <sup>x</sup> 24 J.S. Rosenschein, M.R. Genesereth, Communication and cooperation among logic-based agents, Proceedings of Sixth Phoenix Conference on Computers and Communications, Phoenix, AZ, 1987.

<sup>w</sup> <sup>x</sup> 25 R. Sprague Jr., E. Carlson, Building Effective Decision Support Systems, Prentice-Hall, 1982.

<sup>w</sup> <sup>x</sup> 26 T. Winograd, F. Flores, Understanding Computers and Cognition, Norwood, NJ, Ablex, 1986.

<sup>w</sup> <sup>x</sup> 27 D. Woelk, Developing InfoSleuth Agents Using Rosette: An Actor-based Language, Working Paper, Austin, TX, MCC, 1996, http:<sup>rr</sup>www.mcc.com<sup>r</sup>projects<sup>r</sup>infoseulth.

<sup>w</sup> <sup>x</sup> 28 D. Woelk, P. Cannata et al., Using carnot for enterprise information integration, The Second International Conference on Parallel and Distributed Information Systems 1993 133–Ž . 136.

<sup>w</sup> <sup>x</sup> 29 D. Zeng, K. Sycara, Cooperative Intelligent Software Agents, Working Paper, CMU-RI-TR-95-14, Carnegie Mellon University, 1995.

![](/api/attachments/BC4UEEHG/fulltext/images/92cb525b0cf9fadbe6c20c32341d1d0bc97c362cdf19b34ab8c9d1a0d7e9983d.jpg)

Tung Bui is currently professor of Decision Sciences and chair holder of the Matson Navigation Chair of Global Business, University of Hawaii. Bui earned his PhD in information systems from New York University and a doctorate in managerial economics from the University of Fribourg, Switzerland. Bui has done extensive research and consulting in designing and implementing decision support systems for large organizations.

![](/api/attachments/BC4UEEHG/fulltext/images/fc3fe2445bcd5402ee59b9edb8eedb73de76be9d68de6f4aad3e5e84634350f0.jpg)

Jintae Lee is an Assistant Professor in the Department of Decision Sciences at the College of Business Administration, University of Hawaii. His research interest is in knowledge representation and management. His research has so far focused on the representation and organization of process knowledge the Pro- Ž cess Handbook project , the design of . process ontology for sharing the Pro-Ž cess Interchange Format project , and. the representation and use of organizational memory design rationale . His current interest is on the useŽ . of data mining for knowledge management.

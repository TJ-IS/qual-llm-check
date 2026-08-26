---
otero_id: 21405
otero_key: "TJHUUXEN"
title: "A distributed decision support system for strategic planning"
authors: "Suzanne D. Pinson; Jorge Anacleto Louçã; Pavlos Moraitis"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00074-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A distributed decision support system for strategic planning

Suzanne D. Pinson \*, Jorge Anacleto Louçã , Pavlos Moraitis

LAMSADE, Université Paris IX–Dauphine, Place du Maréchal de Lattre de Tassigny, 75775 Paris Cedex 16, France

## Abstract

Recent advances in artificial intelligence, particularly in the field of multi-agent theory, offer great promises in modeling strategic planning processes. In this domain, the ability to introduce distinct cognitive agents which cooperate to solve the problem enables the processing of more complex and ill-structured problems. This paper presents a general framework for building a distributed strategic decision support system (DSDSS) which integrates both advances in distributed decision making and distributed artificial intelligence. It goes on to describe a cooperative and distributed system with two specific features: the users intervene as human agents in the solution formation, and strategic knowledge and domain knowledge are distributed in different agents which communicate through various blackboards and message passing. An example is provided in the field of strategic marketing which illustrates how the system operates. © 1997 Published by Elsevier Science B.V.

Keywords: Strategic planning; Distributed decision support systems; Distributed artificial intelligence; Multi-agent systems; Blackboard systems

## 1. Introduction

In recent years, more and more artificial intelligence techniques have been incorporated into decision support system (DSS) design frameworks in order to include intelligent problem-solving mechanisms and therefore to procure a more powerful decision support and improve the decision-making process $[11,12,17,27,29,37,38]$ .

In addition, the development of distributed artificial intelligence frameworks provides a new methodology to solve complex problems by dividing them into a number of modules which cooperate to solve the problem using their own knowledge, goals, skills and plans. Since strategic planning involves cooperation between several actors in order to propose a global plan of coherent actions, the rapprochement of the domains of DSSs and distributed artificial intelligence may be of mutual interest. Up to now, very few papers and computer systems have addressed the potential intersection, or even the convergence, between these two domains [6,26,30].

Decision-making processes in strategic planning are usually very complex and are frequently partitioned into sub-problems. Very often, this decomposition involves several levels of decision and is by nature hierarchical. Solutions are proposed for each sub-problem, either by experts who work individually or by a group of experts who analyze a problem collectively. They are based on multiple and complex interactions between the actors of the process, and the participation of diverse decision centers in the process of defining a plan of actions. One of the main problems is to find a way to automate the process as much as possible, particularly so as to obtain automatically coherence and coordination among decisions made locally by different actors at different levels.

The problem is compounded by the ill-structured nature of the decision-making process $[24]$ . There is no algorithmic solution. If a solution exists, it is often obtained in stages; the objective of the problem-solving system is not to find an optimal solution but rather to be able to formulate the alternatives among which there may exist a satisfactory solution, called a “satisfying solution” by $[23]$ .

The distributed strategic DSS (DSDSS) presented in this paper is an attempt to address these different problems. We incorporated a distributed intelligence artificial architecture into a strategic DSS. The objective of the system is to support top-level managers in creating strategic scenarios and assessing the feasibility and coherence of a plan of actions. This framework was applied to strategic marketing problems.

This paper is organized as follows. Section 2 gives a brief idea of the domain of strategic decision making as well as a review of previous research. Section 3 explains why distributed artificial intelligence and more specially multi-agent theory is well qualified to represent strategic planning processes. Section 4 highlights the general characteristics of our system and the conflict resolution mechanism that is used. Section 5 describes the architecture of the DSDSS, with a detailed emphasis on interactions between the artificial agents of the system. Finally, in Section 6, an example illustrates how the system operates in the domain of strategic marketing.

## 2. Notions on the domain

## 2.1. Structure and characteristics

Following Greenley's strategic management process model [8,16], there are four major steps for the analysis of the strategic decision-making process (Fig. 1): (1) analyzing the environment, (2) planning direction, (3) planning strategy and (4) implementing strategy. The planning strategy step is related to the generation and evaluation of options in order to select an overall strategy.

Early work in the field of strategic planning $[1,24,34]$ has highlighted some characteristics of the process, such as irregularity, complexity, ill-structured problems, uncertain and imprecise knowledge, and diversified expertise. The adoption of an overall strategy requires an adequate perception over diversified spheres of expertise, such as human resource management, financial management, marketing, R & D and production management. Therefore, it makes sense to consider strategic planning as a distributed decision-making process.

![](/api/attachments/TJHUUXEN/fulltext/images/078024cb5ff369aae6078585e67a42234407330a6da3ff2b7f8ff2f1a2ca52ee.jpg)  
Fig. 1. Strategic management process [8].

According to [36], four groups of individuals are usually involved:

(1) One group is made up of top-level managers, such as division heads and members of the executive committee. They define the strategic orientations of the firm (i.e. international investment, niche concentration, etc.), decompose the main goal into sub-goals and ask the lower levels to solve them. At the end of the strategic process, they decide whether the recommendations are acceptable, need to be modified or should be rejected.

(2) A second group consists of middle-level managers: finance, production, marketing, human resources, etc. Their objective is to deal with sub-goals and to assign them to specialists (or operational managers), while taking into account the internal constraints (financial, technical, managerial, etc.) of the firm.

(3) Another group is composed of low-level managers (line managers, operational managers, etc.) in charge of an operational unit such as a product department or a strategic business unit. Their main goal is to make recommendations and to propose feasible elementary actions based on the available information regarding the sub-goals and environmental constraints.

(4) The fourth group is made up of staff specialists (lawyers, market researchers, R&D managers, etc.) who define all the environmental constraints such as government regulations, historical and current industry information, historical and current information on competitors and customers, political data, demographic data, etc. These constraints are important information because they could prevent or facilitate the successful implementation of recommendations.

## 2.2. Existing tools and systems

A variety of knowledge-based systems have been developed to model strategic planning decisions [3,16,25]. A good review of the literature can be found in [8]. They are mostly DSSs integrating a database, a spreadsheet, financial analysis modeling, forecasting and reporting systems. One of them, [28], has a more sophisticated knowledge representation (i.e. an object-oriented representation), works with qualitative information and causal models, and is able to support organizationally intelligent behavior. Another one, the STRATEX system [5], guides the user through a strategic market planning process, assuming the importance of human-computer cooperation to solve this kind of ill-structured problem. The SMAS system, [22], is a decision support tool that tries to fit knowledge acquisition and modeling to the hierarchical structure of the marketing assessment items. To do so, logic tables were used to elicit weights from experts when there were dependencies between the items being evaluated. The DIEIS (Distributed Intelligent Executive Information System) [6] is an executive information system with the capacities of a multi-expert system. It uses heterogeneous expertise to encompass a variety of problem domains, while distributed information processing allows the sharing of resources to improve the efficiency and effectiveness of the system. Other systems are expert systems for establishing organizational structures [20], but most of these projects have been discontinued due to the high complexity of the tasks and the low involvement of representatives of classical organizational theory. Some other systems are DSSs [2] or group DSSs [7,32,36] which aim at simulating different strategies, either by incorporating probability information specified by the user in decision scenarios or by requiring decision makers to be physically present and to communicate through a computer network.

As stated above, these kinds of systems are mostly DSSs integrating heterogeneous expertise or they are computerized supports allowing decision makers to communicate with each other. They do not encompass any intelligent problem-solving mechanism distributed among autonomous agents. The DSDSS framework proposed in this paper provides such a mechanism. More precisely, the originality of this framework is that it allows integration and coordination of several autonomous agents, automatic task decomposition, task allocation to competent agents and reasoning processes at agent level. It also addresses the problem of coordination and compatibility of actions proposed locally by different agents.

## 3. A multi-agent approach to the strategic planning process

Given the above characteristics and the actors involved, the combination of decision support and distributed artificial intelligence frameworks offers great promises in modeling strategic management applications $[18]$ . The design of DSSs for strategic planning problems should be focused on the creation of an envelope which allows modeling of the actors' behavior and simulation of their interaction. In this domain, the ability to include distinct cognitive agents in a problem-solving process is highly desirable.

Since the strategic planning process needs cooperation between several agents, the framework proposed in this paper stems from different domains: distributed decision making $[31]$ , which proposes different structures of social organization; theory of organizations $[23]$ , which supplies models of communication between decision makers; and distributed artificial intelligence, particularly multi-agent theory $[4]$ , which studies coordination among a collection of autonomous intelligent artificial agents. In order to deal with complexity, multi-agent theory proposes the kind of decomposition found in distributed decision making. A single “super-task” is decomposed into smaller sub-tasks, each of which requires less knowledge. Sub-tasks are allocated among a group of intelligent agents.

As pointed out by [15], “the major problem with designing multi-agent systems is deciding how the task should be decomposed and the control regime to be used and this choice of organization is determined by features of the task”. Relations among agents and role distribution define different types of agent organization. Among the most well-known are (a) contract nets [10], (b) the scientific community metaphor [19] and (c) hierarchical organization [35]. Since the strategic planning process is hierarchical by nature, the multi-agent hierarchical model could be fruitfully adapted to model this process. On each level a decision unit is concerned with a larger portion of the system and its primary task is to coordinate the actions of the subordinate units. This decomposition corresponds also to Simon's hierarchy concept [34] and to the “partial rationality” concept of [9].

In each of the above domains, global coherence of the system is highlighted and studied from different points of view. Coherence of behavior of autonomous agents is conditioned by the satisfaction of feasibility and compatibility conditions. Feasibility refers to the fact that each action proposed at the lower level of the decision-making process must satisfy the economic and environmental constraints. Compatibility refers to the fact that the actions generated for a sub-problem solution have to be compatible with the actions generated for other sub-problems at the same level of decision making. Very often, conflicts arise among contradictory actions. This paper proposes a specific conflict resolution mechanism based on cognitive maps (see Section 4.3) that is incorporated in our DSDSS framework.

## 4. General characteristics of our DSDSS

## 4.1. General overview

In order to provide answers to the preceding problems and taking into account the specific aspects of the domain, we have designed a DSDSS. A first version called ARISTOT, in which the planning process was fully automated, was developed by Moraitis [26] and is described in [30]. Due to the difficulty of obtaining knowledge from managers, we designed an extension of the system where the managers may interact with the system at each level of the hierarchy. This means that the system is more like an assistant where both the users and the system contribute to the development of plans.

The system operates using a global goal, a set of sub-goals called scenarios and a set of actions proposed by the system to achieve these sub-goals under economic constraints. What the system does is:

\- recommend a plan of actions to be performed to achieve the global goal;

\- identify the problems, that is to say, find incompatible actions and give explanations. In this case, it looks for another scenario in its scenario base indexed by global goals and proposes it to the strategic analyst. Either he accepts it and the system starts a new cycle again or he gives another global goal. He may also stop the process (see Fig. 2).

The system is based on the decomposition of the process into several intelligent and coordinated agents working at three levels of decision (strategic, decision-center and specialist levels), a separation between strategic knowledge and domain knowledge, and a two-phase process allowing the conflict mechanism to be applied, as defined in Section 4.3. These main characteristics make it well suited to represent hierarchical distributed decision-making processes.

In contrast with previous approaches, our system allows:

1. a computer representation of a set of agents which cooperate in the problem-solving process, an explicit representation of communication and control between agents, a knowledge-driven allocation of the sub-problems to a set of agents and a knowledge-driven creation of elementary actions;

2. detection of incompatible actions and consequently the possibility for the user to modify the chosen global strategy;

3. the possibility of solving ill-defined problems by using a trial-and-error method and by testing several alternatives in order to find a satisfactory one;

4. the possibility of using incomplete, qualitative knowledge, taking into account each agent's subjective rationality, specific to strategic decision-making problems.

## 4.2. A cooperative approach

Due to their irregular and ill-structured nature, systems for strategic planning problems have to incorporate the users into the problem-solving process (Fig. 2). This approach is based on the paradigm of supporting the planning process rather than automating it. The model has to help the strategic analyst assess the feasibility of a given solution by simulating different strategic planning scenarios. It starts at the top of the hierarchy by asking the strategic analyst to identify his/her global goal. Using its scenario base, it decomposes the global goal into a scenario composed of sub-goals and works down to more immediately achievable goals. The scenario base encompasses the expertise of the strategic analyst and was created during the knowledge acquisition phase. At each level of the hierarchy, managers (middle-level and low-level) may interact with the system to confirm or modify the proposals and the elementary actions proposed by the system (see Section 5.4 for more details).

![](/api/attachments/TJHUUXEN/fulltext/images/e260cc197777d6ab20236928026972bd7802080054f0b5b26edb9eb7839fb1d4.jpg)  
Fig. 2. A cooperative approach to the strategic decision-making process.

A feedback has been designed to allow the strategic analyst to ask for another scenario if the solution is not feasible or satisfactory, and to repeat this until a satisfactory solution is obtained. The planning process is terminated by the strategic analyst, who decides if the proposed plan describes and solves the problem. This approach is called by [23] the principle of a “satisfying solution”. This means that in general a search for a solution in an organization will return an adequate, rather than the best, solution.

## 4.3. The conflict-resolution mechanism

Very often in distributed systems, agent interaction is the result of cooperative behavior. Conflicts might appear as a result of incomplete knowledge or different viewpoints and priorities of agents. For example, in the domain of strategic planning, one agent may have the goal of increasing market share, while another may have the goal of increasing short-term operating profit. In our system, we have chosen a cognitive approach to conflict resolution. It is based on two principles:

1. the March and Simon conflict theory [23] and the “compromise concept” of Simon [33]. This concept means that in a situation where a system aims at the simultaneous achievement of a set of sub-goals, the chosen global solution (the global plan of actions) never allows the total or perfect achievement of the sub-goals;

2. the decision makers' cognitive maps and the use of strength coefficients between actions and sub-goals. When individual conflicts arise during the decision-making phase, the detection of conflicts between actions and the choice of the best action is done using the strength or priority of the proposed actions. The strength coefficient represents the perceived likelihood of enabling the elementary actions to achieve the corresponding sub-goals. The use of strength coefficients by decision makers has been studied by researchers in strategic marketing [13,14]. The objective was to understand and build decision makers' cognitive maps. The studies highlighted the causal relationships between actions and sub-goals, and stated that some actions are positively associated with the corresponding sub-goals, while others are negatively associated. For example, in strategic marketing the action new product discount on saturated channels is positively associated with the sub-goal distribution factors, while it is negatively associated with the price level of a product (cf. the example in Section 6). The strength coefficients are given by the experts during the knowledge acquisition phase and stored in the rule base of each specialist agent.

Given these two principles, the “compromise concept” is represented by our compatibility criterion, defined as follows:

\- If two contradictory elementary actions are proposed for two different sub-goals $j$ and $k$ (for example, increase price of product A to increase profit level and decrease price of product A to increase market share), the action having the greatest strength coefficient will be chosen.

\- If contradictory actions have the same strength for the sub-goals $j$ and $k$ , these sub-goals are said to be incompatible and therefore the scenario is incoherent. In this case, the strategic analyst may ask for another scenario—the system looks for it in its scenario base and starts a new cycle again. This coordination has the form of a trial-and-error method used by human processes in order to solve ill-structured problems.

Furthermore, if an action is proposed twice (for two different sub-goals j and k), the action will appear only once in the final plan of actions.

It should be observed that this conflict-resolution mechanism does not involve negotiation between agents, as is often proposed in multi-agent theory [4]. This stems from the fact that our framework is based on the studies done on decision makers' cognitive maps and on human decision-making processes by [23,33].

In our framework, we have decided to solve conflicts at the strategic level, since the conflicts cannot be solved at the lower levels of the hierarchy (specialist level) for the following two reasons. (1) Since the system is a distributed system and we simulate the behavior of a company, the elementary actions might be proposed by specialist agents at different periods of time and asynchronously. This specific feature allows the agents to be physically distributed and activated in parallel without impeding convergence towards a possible solution. (2) Since the system is a DSS, at any time the user (the strategic analyst) might want to be able to visualize on the screen the optimal solution of each sub-goal in order to understand why certain actions do not appear in the global solution at the end of the problem-solving process.

## 5. A multi-agent architecture for strategic support systems

We propose a two-phase model to represent the distributed decision-making process for strategic planning: (1) the phase of coordination by plans (top-down task decomposition) and (2) the phase of coordination by retroaction (bottom-up integration). This system is supported by a separation between meta-knowledge and domain knowledge and by a hybrid architecture using message passing and blackboard communication that borrows concepts from multi-agent and parallel blackboard systems $[4,21]$ . In distributed problem-solving techniques, blackboard-based models have been seen as one of the best alternatives for matching the complexity and variety of real-time applications. However, these systems do not provide a powerful mechanism to handle the feasibility and compatibility criteria as defined in our framework, thus implying a serious drawback for their application to a wide range of distributed DSSs.

![](/api/attachments/TJHUUXEN/fulltext/images/46fe261eded4a470c4e019bc5199ca571f7b9bc1c4f0eff87d2cf6b9b9a6066a.jpg)  
Fig. 3. Architecture of the system.

The specific features of our system are: (1) direct communication between agents through message passing and indirect communication through shared memories (blackboards); (2) representation, combination and aggregation of hypotheses and actions using the compatibility criteria leading to a global coherent solution; (3) agent activation—agents may be activated in parallel without impeding convergence towards a possible solution. This feature means that there are no conflicts between knowledge sources (KSs). Potential conflicts between actions are solved by the conflict-resolution mechanism (see Section 4.3).

Our multi-agent system consists of three types of elements: the agents, the blackboards and the constraint base (see Fig. 3).

\- Three types of artificial agents—strategic agents (STAs), decision-center agents (DCAs) and specialist agents (SPAs)—cooperate at three different hierarchical levels corresponding to the three levels proposed in our framework.

\- Four types of blackboard are represented to allow communication between agents: the problem blackboard (PBB), the domain blackboard (DOBB), the compatibility blackboard (CBB) and the strategic blackboard (SBB).

\- The constraint base contains the economic and environmental constraints of the domain.

## 5.1. The agents

Three types of artificial agents cooperate in the system: the STAs, the DCAs and the SPAs. They cooperate at three hierarchical levels corresponding to distinct levels of decision responsibility and of activity specialization. At the strategic level, the global goal is divided into several sub-goals to yield a scenario. The DCA level creates proposals to satisfy each sub-goal. Finally, at the most elementary level, SPAs refine these proposals, create elementary actions and test their feasibility. Each agent is implemented as an object which is an instance of one of the three classes of agents. At each level these proposals or elementary actions are proposed to human agents (the corresponding managers) who either accept them or modify them.

![](/api/attachments/TJHUUXEN/fulltext/images/dab15b5bbbfff6478fd6952a711c7560a4dcf5670583968537427be6eba41592.jpg)  
Fig. 4. Agent architecture.

The agent architecture is adapted from the AR-CHON system [39]. An agent is constituted of two elements: the intelligent system and the cooperative layer (Fig. 4).

The intelligent system (IS) is responsible for the useful work of the agents (e.g. generation of elementary actions for SPAs, generation of proposals for DCAs, generation of skeleton plans for the STA). It is composed of the resolution-KS and two local blackboards: the data blackboard (DBB) and the model blackboard (MBB).

The cooperative layer (CL) is responsible for the cooperation with other agents and for the control of the IS tasks. The planning and coordination module is a knowledge source, called planning-KS. It represents the knowledge about other agents of the community (its acquaintances) and the tasks they are able to do. It is also responsible for deciding when and how to cooperate with other agents. The competence module supports the knowledge that the agent has about itself.

In the STA, the IS module is divided into two modules: the resolution-KS allows the agent to decompose the global goal into a set of sub-goals and to propose a skeleton plan to solve the problem, and the compatibility-KS is triggered at the end of the whole process, during the bottom-up coordination phase. It uses the compatibility criteria to test compatibility between elementary actions stored in the CBB. The CL of the STA is responsible for allocating the sub-goals to the DCAs. The planning-KS is triggered at the end of the first IS module task. It looks for DCAs able to achieve the corresponding sub-goal and generates a command (see Section 5.2.2) to be sent to the chosen DCA. This command is stored in the DCA mailbox.

A DCA has two functions. (1) It refines the partial solution, generates proposals in order to achieve the corresponding sub-goal and proposes them to the corresponding middle-level manager. The resolution-KS contains knowledge for proposal creation. It may use the local DBB and MBB to do so. (2) It chooses the appropriate SPA and sends a command to this agent with the proposed location for it to pick it up. A proposal is represented as an object which is an instance of the class proposal. An example of such an object is presented below.

name $=$ proposal-10

sub-goal = Price-Policy

agent-name = price-specialist

hypothesis-name-DOBB = sub-goal - 1

A SPA has the general structure as shown in Fig. 4, except for the planning-KS. The resolution-KS proposes elementary actions corresponding to proposals created by the DCA that have chosen this specialist to participate in a sub-goal solution. Attached to an elementary action is the strength coefficient (SC), which represents the strength of the elementary action for the achievement of the corresponding sub-goal. For example, an elementary action proposed by the agent specialized in price setting is represented by the following object:

name = action - 10

sub-goal = Price-Policy

entity = Product-A

attribute-name = price

attribute-value = 1.000

The values of the attributes “entity”, “attribute-name”, “attribute-value”, “impact” and “SC” are inferred by the SPA using its rule base and are validated by the corresponding low-level manager. The value of “subgoal” comes from the proposal sent by the corresponding DCA. A SPA may be chosen by several DCAs at the same time. The competence module states which task the SPA is able to do. The agent writes proposed elementary actions in the corresponding DOBB (stored by subgoal and entity) and in the CBB (stored by entity and attribute). Its knowledge is represented by rules that are triggered by matching premises against the constraints of the constraint base. Some of the constraint values, such as product cost, may be computed by a mathematical model (stored in the MBB) as a function of the purchase cost and the production cost (stored in the DBB). The structure of a rule of the SPA, price setting, is shown in the following example:

rule: R1

```matlab
if x is a proposal and y a product
    if
    sub-goal (x) = Price-Policy
    and name (y) = Product-A
    and product-cost (y) = high
    and competition (y) = strong
    then
    create an elementary-action z with
    sub-goal (z) = sub-goal (x)
    entity (z) = Product-A
    attribute-name (z) = price
    attribute-value (z) = 1.000
    impact (z) = +
SC (z) = 0.8
```

This says that in order to solve the sub-goal price policy and considering the economic constraints (product cost and competition) on product-A, the price of product-A should be set to \$1000. It also gives the SC of this elementary action. This knowledge is given by the experts during the acquisition phase.

## 5.2. Communication

Communication between agents is carried out by means of three centralized structures called blackboards (the DOBB, the CBB and the SBB) and by decentralized messages sent by the agents to each other and stored in their mailboxes located in the PBB.

## 5.2.1. The blackboards

The PBB contains the problem's initial data which is given interactively by the user. It contains the global goal name, the list of mailboxes of the DCAs and the list of mailboxes of the SPAs. This blackboard allows communication and distribution of decision making among the three levels of decision functions. This data structure is specific and important because it shows at any time of the problem-solving process who is doing what, when and which agents are active. The structure of the distributed decision-making process is available at all times during the problem-solving process.

The DOBB contains feasible elementary actions proposed by the SPAs to achieve a sub-goal. An elementary action is feasible if it satisfies the domain constraints. The set of elementary actions represents a part of the solution to the global problem and a local optimum for the corresponding sub-goal.

The CBB contains the set of feasible elementary actions proposed by all the SPAs. The objective of this structure is to allow the compatibility criteria to be applied to elementary actions in order to detect incompatibility among elementary actions and consequently among sub-goals of the global goal. As a result, a coherent plan of actions is built and stored in the SBB and represents a compromise (in Simon's sense of the word [33]) between feasible elementary actions.

The SBB contains either a plan of elementary actions representing a feasible and coherent solution to the global problem or a set of incompatible actions showing that the scenario is not coherent and that the corresponding sub-goals are incompatible.

## 5.2.2. Direct communication

Message passing between agents has the form of instances of the command class. The structure of a command object is as follows:

```txt
name = <command-name>
from-agent = <sending-agent>
to-agent = <receiving-agent>
work-to-do = <task-name>
```

When an agent at the strategic or decision-center levels sends a request to a lower-level agent, it enters a command in a list of commands. The sending agent also puts the command name into the mailbox of the receiving agent. After having performed the task the receiving agent removes the command from the list. When the list is empty this means that all possible elementary actions have been generated, and the integration phase is activated.

## 5.2.3. The events

Creating or updating a hypothesis in the DOBB or in the CBB creates an event which is stored in the event list. What an event does is (1) sort elementary actions by sub-goal and attribute and store them in the DOBB, and (2) sort elementary actions by entity and attribute and store them in the CBB. The event list contains events which indicate changes in the DOBB and in the CBB. A SPA checks this list before updating the DOBB and the CBB in order to decide the type of action to be performed: create a new hypothesis or update an existing one.

## 5.3. The constraint base

The constraint base contains the economic and environmental constraints of the domain, such as government regulations, historical and current industry information, political data, demographic data, etc. The SPAs match their knowledge against these constraints to generate feasible elementary actions.

## 5.4. How the system operates

The system operates through the following phases.

## 5.4.1. Phase 1: User-computer interaction

The system asks the strategic analyst to define the global goal. The global goal is stored at the strategic level of the PBB.

## 5.4.2. Phase 2: Activation of the strategic agent

(1) The resolution-KS retrieves the global goal name from the strategic level of the PBB and generates a list of sub-goals from its scenario base. This list of sub-goals is proposed to the strategic analyst who may validate or modify it. These sub-goals must be achieved in order to reach the global goal.

(2) The planning-KS looks for the DCAs able to solve the sub-goals, and assigns a sub-goal to the corresponding DCA. The names of the sub-goals are sent by a command to the DCA mailboxes located in the PBB. This command is also stored in the command list.

## 5.4.3. Phase 3: Activation of the DCA

(1) The resolution-KS retrieves the name of the sub-goal from the DCA mailbox located in the PBB. Using its knowledge, it generates proposals. These proposals may be validated or modified by middle-level managers.

(2) The planning-KS allocates proposals to SPAs. It looks for the SPA able to propose an elementary action and passes on the proposal to the selected agent. Proposal names are sent by a command to the mailboxes of the SPAs in the PBB. This command is also stored in the command list. The command sent by the STA is removed from the command list and from the mailbox.

## 5.4.4. Phase 4: Activation of the SPA and the feasibility phase

The resolution-KS of the SPA generates elementary actions and tests their feasibility against the constraints base. Upon acceptance by the corresponding low-level managers, the feasible elementary actions are stored simultaneously in the DOBB and in the CBB. The commands sent by the DCA are removed from the list of commands and from the mailbox.

## 5.4.5. Phase 5: Integration phase

The conflict-resolution mechanism is applied during the integration phase. The STA searches for incompatibilities in the CBB, where all the elementary actions created by SPAs are stored. This mechanism yields two kinds of results:

1. if elementary actions are compatible, the system gives its recommendation as a plan of actions to be performed and stores it in the SBB;

2. if elementary actions are incompatible, the system explains why by giving the corresponding sub-goals and stores them in the SBB.

## 5.4.6. Phase 6: User-computer interaction

In the case of incompatible actions, the STA looks for another scenario in its knowledge base. If one is available for the same goal, it proposes it to the user. Upon the user's approval, it starts a new cycle. This leads to a dynamic reorganization of the agent community. If it does not find an appropriate scenario, it asks the user to cooperate to create a new scenario, to give another global goal or to stop the process (as described in Section 4.2).

## 5.5. Implementation

A prototype has been implemented on a SUN SPARC II workstation to investigate the feasibility of a distributed multi-agent architecture when applied to strategic decision-making problems. It uses the SMECI development environment based on an object-oriented formalism and on LISP. This development environment handles categories (classes of objects), methods associated to categories, and rules that are grouped into tasks. A task is considered as a special object that describes a process. The shell deals with the various tasks according to an agenda which can be controlled and modified dynamically by the user. The graphic library AIDA, included in the SMECI shell, is used to create sophisticated graphic interfaces. This window and icon interface allows the users to simply “point and click” to verify strategies, the distribution of the decision making between agents, actions already proposed by agents, etc. (see Fig. 6, Fig. 7 and Fig. 8 in the next section).

Two types of validation have been undertaken: face validity and predictive power. Face validity is a surface or initial impression of the realism of a system and was checked in the early stages of model building. The system was shown to a group of experts in a French consulting company; they considered the correspondence between the model operation and their perception of the real-life phenomena which the model represents to be good and so accepted face validity. Predictive power was evaluated by testing and comparing the results of the system (strategic plans of actions) against reality. The system was pre-tested using a few case-studies published in the management literature (one of them is given in the following section). The results were compared and found to be identical to those proposed in the literature. Flexibility is another validation criterion. The architecture proposed for our DSDSS approach based on multi-agent theory is very flexible and is able to incorporate new expertise or new points of view without major modifications. It is obvious that more testing and validation are called for. Although the validation of the system is at its early stages, results so far have shown that the DSDSS approach offers potential to assist in a strategic planning process and that research should therefore proceed.

## 6. An experimental scenario

To illustrate the basic concepts of our approach and the general functionality of each element of the system, this section presents the study of a simple academic case which has the advantage of expressing clearly and objectively the most interesting aspects of this architecture.

Developing a marketing strategy involves making decisions about products, distribution, promotion and price in the light of company factors as well as customer, competition and other market factors. Marketing-strategy development defines overall marketing procedures, target markets and the marketing mix of a product, promotion media, distribution channels and price for a company. These strategic decisions are made within the limitations of the market-place and company resources, and within the context of the enterprise-wide strategic goals and plans.

In our example, the global goal of the strategic marketing department is called “enterprise expansion”. In order to achieve the global goal, a scenario called new product marketing strategy has been defined by top marketing executives. It is composed of a set of sub-goals such as product factors, distribution factors, promotion policy and price policy. Sub-goals are stored in the DBB of the STA during the knowledge-acquisition phase. During the reasoning process, these sub-goals are passed on to DCAs and become their local goals (for instance, price policy becomes a local goal for the financial agent). Several elementary actions, defined by the SPAs and validated by lower-level managers, are proposed to achieve these sub-goals, such as product design investment, packaging design investment, research price regulations or transportation company contract. The relations which exist between these three levels of decision are by nature hierarchical and are depicted in Fig. 5. The values “+” and “-” in the figure represent the positive and negative associations between elementary actions and the corresponding sub-goals (see Section 4.3).

![](/api/attachments/TJHUUXEN/fulltext/images/a80b50c9d217e7da17d607373095b69869b231aebebe3f2bf408fa657a4fdf93.jpg)  
Fig. 5. A scenario decomposition.

The marketing strategic planning process is obviously more complex than just specifying a plan of elementary actions. We believe that our approach is, however, a useful starting point for developing a prototype multi-agent system in the marketing-strategy as well as in the corporate-strategy planning area.

Fig. 6, Fig. 7 and Fig. 8, which show screens from the system operation, illustrate human-machine interaction.

In Fig. 6, the upper window, called global goal, shows all possible global goals. The lower window lists the proposed scenarios stored in the knowledge base of the STA.

![](/api/attachments/TJHUUXEN/fulltext/images/14b64985e0079f4b858fd2999bfaf851ac70f23c6e8535b8b01e3d18b93d91b5.jpg)  
Fig. 6. Choosing a global goal and a scenario to be studied.

During the reasoning process, conflicts may arise between elementary actions proposed by SPAs to achieve two different sub-goals. For example, the elementary action new product discount on saturated channels, necessary to achieve the sub-goal distribution factors, and new product high prices segmentation, necessary to achieve the sub-goal price policy, are in conflict. Their effect is to set the price of the new product, but the first one is negatively associated with the first sub-goal, while the second is positively associated with the latter. Using its SCs, the corresponding specialists know that the first action is moderately important for the achievement of the sub-goal distribution factors, while the other one is very important to obtain the required financial performance of price policy. Therefore, the second one will be kept in the global plan of actions. These two elementary actions, as well as the others proposed by each activated specialist, are stored in the DOBB and in the CBB of the system (see Section 5.2.1).

As explained in Section 4.3, the conflict-resolution mechanism is activated by the STA in order to select a set of compatible actions. If the STA is able to solve all merging conflicts, the system provides a coherent solution (Fig. 7 and Fig. 8). Otherwise, it gives incompatible actions as well as the corresponding sub-goals.

The conflict cannot be solved at the level of the specialists because the system is distributed and ac-

![](/api/attachments/TJHUUXEN/fulltext/images/71bedf512636999fa17c9e7ac80de6f463188ea2e09df26c76fcd1e5e35df445.jpg)  
Fig. 7. Outputs of a coherent solution.

![](/api/attachments/TJHUUXEN/fulltext/images/1ecd6c4cc390b2404612bfb3266d14c265839cb39964158da93ec776a017cc68.jpg)  
Fig. 8. The sub-goal level of a coherent solution.

tions may be proposed for each sub-goal by different agents at different intervals of time. It is also important to keep the set of actions proposed to achieve a single sub-goal (it represents the local optimum as defined by Simon [23,34]) in order for the system to give explanations to the user (Fig. 8).

## 7. Conclusions

This paper shows how a structured methodology and framework has been applied for the development of a distributed DSS for strategic decision making which integrates advances in both distributed decision making and distributed artificial intelligence theory. The decomposition of the problem into a number of modules enables the processing of more complex problems by the cooperative effort of intelligent agents using their own knowledge, goals, skills and plans. Three cognitive agents interact in order to satisfy a high-level common goal. During the decision-making process, conflicts might occur as the result of distinct viewpoints. A specific method is proposed for conflict detection and resolution, based on the compromise concept of Simon [33] and on decision makers' cognitive maps. The separation between strategic knowledge and domain knowledge through a multi-blackboard architecture makes the system well suited to represent hierarchical distributed decision-making processes. This has been applied to the problem area of strategic decision making in marketing.

The experience gained from the development effort of our system supports the proposition that multi-agent systems are an appropriate modeling framework for strategic decision making. Several key contributing factors should be highlighted. First, distributed systems are well adapted to modeling task decomposition. The strategic planning process is inherently multidimensional and implies task decomposition. Sub-tasks are allocated to the actors involved in the decision-making process. Second, problems which are essentially ill-structured may be modeled, satisfactorily, by distributed artificial intelligence. Third, multi-agent systems provide an adequate structure to represent multiple and complex interactions between cognitive agents, which are justified by the participation of diverse knowledge sources and decision-centers in the process of defining a global and coherent strategy.

More research has to be done in several directions: (1) adding more knowledge to each agent of the system and fully testing and validating the system, (2) developing the user dialog and interface to allow the users to ask for explanations at any stage of the process, (3) adding more parallelism to the system to improve efficiency, and (4) adding learning capabilities to the cooperative process, using case-based reasoning. When the system detects contradictory actions it could suggest another decomposition, based on its experience and history.

## References

[1] S.J. Armstrong, The Value of Formal Planning for Strategic Decisions: Review of Empirical Research, Strategic Management Journal 3 (1982) 197–211.

[2] A.B. Badiru, P.S. Pulat and M. Kang, DDM: Decision Support System for Hierarchical Dynamic Decision Making, Decision Support System 10 (1993) 1–18.

[3] S.G. Berman and R.F. Kautz, Compete: A Sophisticated Tool that Facilitates Strategic Analysis, Planning Review (July 1990) 35–39.

[4] A.H. Bond and L. Gasser (Eds.), Readings in Distributed Artificial Intelligence (Morgan Kaufmann, 1988).

[5] O.J. Borch and G. Hartvigsen, STRATEX: A Knowledge-Based System for Strategic Market Planning in Small Firms, AICOM 3, No. 1 (1990).

[6] R.T. Chi and E. Turban, Distributed Intelligent Executive Information Systems, Decision Support Systems 14 (1990) 117–130.

[7] C.H. Chung, Lang J.R. and K.N. Shaw, An Approach for Developing Support Systems for Strategic Decision Making in Business, Omega International Journal of Management Science 172 (1989) 135–146.

[8] D.N. Clark, A Literature Analysis of the Use of Management Science Tools in Strategic Planning, Journal of the Operational Research Society 43, No. 9 (1992) 859–870.

[9] R.M. Cyert and J.G. March, A Behavioral Theory of the Firm (Prentice-Hall, 1963).

[10] R. Davis and R.G. Smith, Negotiation as a Metaphor for Distributed Problem Solving, Artificial Intelligence 20, No. 1 (1983) 63–109.

[11] G.1. Doukidis, Decision Support System Concepts in Expert Systems: An Empirical Study, Decision Support Systems 4 (1988) 345–354.

[12] G.I. Doukidis, General Considerations on Knowledge-Based Management Support Systems, In: G.I. Doukidis, F. Land and G. Miller (Eds.), Knowledge-Based Management Support Systems (Ellis Horwood, 1988).

[13] J.S. Falkenberg and K. Gronhaug, Managerial Perceptions of Strategy and Change, European Management Journal 7, No. 2 (1989) 209–217.

[14] J.D. Ford and W.H. Hegarty, Decision Makers Beliefs about the Causes and Effects of Structure: An Exploratory Study, Academy of Management Journal 27, No. 2 (1984) 271–291.

[15] M.S. Fox, An Organizational View of Distributed Systems, IEEE Transactions on Systems, Man and Cybernetics SMC-11, No. 1 (1981).

[16] G.E. Greenley, Strategic Management (Prentice-Hall, 1989).

[17] J.C. Henderson, Finding Synergy Between Decision Support Systems and Expert Systems Research, Decision Sciences 18 (1987) 333–349.

[18] C. Holloway, Strategic Management and Artificial Intelligence, Long Range Planning 16, No. 5 (1983) 89–93.

[19] W.A. Kornfeld and C.E. Hewitt, The Scientific Community Metaphor, IEEE Transactions on Systems, Man and Cybernetics SMC-11, No. 1 (1981) 24–33.

[20] F. Lehner, Expert Systems for Organizational and Managerial Tasks, Information and Management 23 (1992) 31–41.

[21] V.R. Lesser and D.D. Corkill, Distributed Problem Solving, In: S.C. Shapiro (Ed.), Encyclopedia of Artificial Intelligence (Wiley, 1987) 245–251.

[22] M.J. Liberatore and A.C. Stylianou, Using Knowledge-Based Systems for Strategic Market Assessment, Information and Management 27 (1994) 221–232.

[23] J.G. March and H.A. Simon, Organizations (Wiley, 1958).

[24] H. Mintzberg, D. Raisinghani and A. Théorêt, The Structure of "Unstructured" Decision Processes, Administrative Science Quarterly 21 (1976).

[25] R.J. Mockler, Knowledge-Based Systems for Strategic Planning (Prentice-Hall, 1989).

[26] P. Moraitis, Distributed Decision Making and Multi-Agent System, PhD Dissertation, University Paris–Dauphine, (1994) (in French).

[27] D.E. O'Leary and P.R. Watkins (Eds.), Expert Systems in Finance and Accounting (North-Holland, Studies in Management Science and Systems, 1992).

[28] D.B. Paradice, SIMON: An Object-Oriented Information System for Coordinating Strategies and Operations, IEEE Transactions on Systems, Man and Cybernetics 22, No. 3 (1992) 513–525.

[29] S. Pinson, A Multi-Expert Architecture for Credit Risk Assessment: The CREDEX System, In: D.E. O'Leary and P.R. Watkins (Eds.), Expert Systems in Finance and Accounting (North-Holland, Studies in Management Science and Systems, 1992).

[30] S. Pinson and P. Moraitis, An Intelligent Distributed System for Strategic Decisions Making, Group Decision and Negotiation Kluwer Academic, 6, 77–108, 1996.

[31] J. Rasmussen, Modeling Distributed Decision Making, In: J. Rasmussen, B. Brehmer and J. Leplat (Eds.), Distributed Decision Making: Cognitive Models for Cooperative Work (Wiley, 1991).

[32] M.F. Shakun, Airline Buyout: Evolutionary Systems Design and Problem Restructuring in Group Decision and Negotiation, Management Science 37, No. 10 (1991) 1291–1303.

[33] H.A. Simon, Administrative Behavior (MacMillan, 1975).

[34] H.A. Simon, Science of the Artificial (MIT Press, 1969).

[35] R. Steeb, S. Cammarata, F.A. Hayes-Roth, P.W. Thorndyke and R.B. Wesson, Architectures for Distributed Air-Traffic Control, In: A.H. Bond and L. Gasser (Eds.), Readings in Distributed Artificial Intelligence (Morgan Kaufmann, 1988).

[36] R.A. Thietart and M. Bergadaa, STRADIN: A Strategic and Dynamic Inter-personal Decision Making Process, Conference of Strategic Management Society, Amsterdam (1988).

[37] E. Turban, Decision Support Systems and Expert Systems: Managerial Perspectives (MacMillan, 1987).

[38] E. Turban and P.R. Watkins, Integrating Expert Systems and Decision Support Systems, MIS Quarterly 10, No. 2 (1986) 121–136.

[39] T. Wittig (Ed.), ARCHON: An Architecture for Multi-Agent Systems (Ellis Horwood, 1992).

![](/api/attachments/TJHUUXEN/fulltext/images/87dbe244dd7c769d0ae962fa68d87966138b42265cc95813063b39dc348563c4.jpg)

Suzanne D. Pinson is a full professor in the Department of Computer Science at the University of Paris–Dauphine. She is head of the research group in artificial intelligence and decision processes at LAMSADE, a CNRS laboratory. She received a M.S. in computer science and operational research from Northwestern University, Evanston, IL and a M.S. and a Ph.D. in computer science from the University of Paris VI. She was a visiting scholar in artificial intelligence at

UCLA in 1979–1980. Dr. Pinson is the author of a book on cluster analysis and has published numerous papers on data analysis, multi-expert systems and artificial intelligence. She is on the editorial board of several international journals. She is a member of ACM, AAAI, AFIA and AFCET. Dr. Pinson's areas of research concern distributed artificial intelligence, distributed decision making, and multi-agent systems (more precisely, the decision theory approach for coordination in multi-agent systems). Other research interests include frameworks for the development of management and financial distributed decision support systems.

![](/api/attachments/TJHUUXEN/fulltext/images/96834a9b22dd81a1e597509f888cafd97a55981102b16c94b719be323e12214f.jpg)

Jorge Anacleto Louçã is a Ph.D. student in computer science and information systems at the University of Paris-Dauphine and at the Faculty of Sciences, University of Lisbon. He received his diploma degree in business administration from the ISCTE Institute, University of Lisbon, Portugal, and his D.E.A. (Master of Sciences in computer science) from the University of Paris-Dauphine in 1995. His research interests are distributed artificial intelligence,

multi-agent systems, and game theory and its applications to decision support systems.

![](/api/attachments/TJHUUXEN/fulltext/images/9e0023ed06a84102532e054449e4abcaa260e7c1211d76f9d1bc6c89c2f2ad81.jpg)

Pavlos Moraitis is a post-doctoral research fellow at the LAMSADE Laboratory, University of Paris–Dauphine. His research activity is supported by a CNET (National Center for Telecommunications) contract. He received his Diploma degree from the National Technical University of Athens (NTUA) and his Ph.D. degree from the University of Paris–Dauphine in 1994. Dr. Moraitis has held technical and management positions in a software advisory company. His re-

search interests are multi-agent systems, especially the problems of coordination, planning, negotiation and decision making.

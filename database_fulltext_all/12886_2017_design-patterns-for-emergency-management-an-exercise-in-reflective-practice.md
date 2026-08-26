---
otero_id: 12886
otero_key: "TQYTTS98"
title: "Design patterns for emergency management: An exercise in reflective practice"
authors: "Daniela Fogli; Claudio Greppi; Giovanni Guida"
year: "2017"
journal: "Information & Management"
doi: "10.1016/j.im.2017.02.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: Design patterns for emergency management: an exercise in reflective practice

Authors: Daniela Fogli, Claudio Greppi, Giovanni Guida

![](/api/attachments/TQYTTS98/fulltext/images/ec4402adeaa25fc3ad8934f65cab8562d1978af4a7aca676be78ceefe59e5e13.jpg)

PII: S0378-7206(17)30089-7

DOI: http://dx.doi.org/doi:10.1016/j.im.2017.02.002

Reference: INFMAN 2977

To appear in: INFMAN

Received date: 16-11-2015

Revised date: 18-11-2016

Accepted date: 2-2-2017

Please cite this article as: Daniela Fogli, Claudio Greppi, Giovanni Guida, Design patterns for emergency management: an exercise in reflective practice, Information and Management http://dx.doi.org/10.1016/j.im.2017.02.002

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Design patterns for emergency management: an exercise in reflective practice

Daniela Fogli (corresponding author)

Dipartimento di Ingegneria dell’Informazione

Università degli Studi di Brescia

Via Branze 38, 25123 Brescia, Italy

Phone: +39 030 3715666

Email: daniela.fogli@unibs.it

Claudio Greppi

Argonet S.r.l.

Via Pirelli, 29, 20124 Milano, Italy

Phone: +39 02 66823373

Email: c.greppi@argonet.it

Giovanni Guida

Dipartimento di Ingegneria dell’Informazione

Università degli Studi di Brescia

Via Branze 38, 25123 Brescia, Italy

Email: giovanni.guida@unibs.it

## Design patterns for emergency management: an exercise in reflective practice

## Research Highlights

 A reflective practice exercise in the field of emergency management is presented

 The design of knowledge-based decision support systems is discussed

 A collection of design patterns for emergency management is proposed

## Summary

The design of a decision support system (DSS) for emergency management is an important and recurrent task in several application domains. However, despite several approaches and systems are reported in the literature, reusing such experiences is not easy. Starting from the experience gained through three concrete projects carried out by the authors in the last 10 years, in this paper, we suggest an approach based on design patterns, which can be used for the conceptual design of DSSs for emergency management. The validity of the proposed collection of design patterns has been assessed through an evaluation exercise with expert designers.

Keywords: emergency management, decision support, design patterns.

## 1. Introduction

Several literature works offer a wide background analysis of the main traits and challenges of the emergency management task - e.g. [12][27][53][58]. Many proposals address specific aspects such as situation awareness [16][51], information flow [50], and improvisation [35]. Moreover, while most projects focus on crisis management, only minor attention has been paid so far to the management of early warnings and threats (see for instance, [36][41][53]).

In this context, a number of research projects have been focused on the development of computerbased tools—and more specifically, decision support systems (DSS)—for emergency management (e.g., [1][14][18][57]). The design of these tools, however, is often domain-dependent, and rarely general and systematic approaches are proposed. Most works focus on the technical and operative aspects, but do not make explicit the basic principles, the assumptions made, and the adopted design choices, so that the underlying models can hardly be applied in new contexts.

Thus, reusing experience is not easy and, in front of a new emergency management context, DSS designers are often forced to start their work from scratch. To resolve this problem, we propose a practical approach to the conceptual and logical design of a DSS for emergency management, which is also general enough to be effectively used in a large variety of situations. The final goal is to promote design discipline and make the whole design process more effective and efficient. To tackle this challenging goal, we have adopted a reflective practice approach [54][56], inspired by the seminal proposals of [8][47][52]. Our research has been performed per a pathway that includes the following 5 steps:

1. Experience: the background for this research has been offered by three DSS projects in emergency management that we have carried out in the past 10 years;

2. Awareness: we have recognized that the experience with the three DSS projects mentioned above did embody more value than expected; from these projects, it might be possible to distill extensive design knowledge of general validity useful to support the design of DSSs for emergency management in different practical cases;

3. Analysis: focusing on the recurring aspects of the experience done, the conceptual entities that characterize an emergency management problem have been identified that constitute the ontological background of our approach;

4. Generalization: a structured collection of design patterns [2][7][23] has been worked out, which can support the design of DSSs for emergency management in a wide class of situations;

5. Testing: the validity of the proposed approach and design patterns has been tested both in the development of the three projects mentioned above and through a specifically designed evaluation exercise carried out with a sample of selected DSS designers.

This paper reports the main results obtained in this research. The paper is organized as follows. Section 2 presents a summary of the three projects carried out (experience); Section 3 defines the scope of the research including the definition of our concept of emergency, the stakeholders, and the specific focus and goal of our effort (awareness); Section 4 describes the main conceptual elements of our approach to emergency management (analysis); Section 5 presents a collection of design patterns to support the development of DSSs for emergency management in different application contexts (generalization); Section 6 describes the evaluation exercise carried out with six experts in emergency management and DSS design to test the validity of the collection of design patterns (testing); finally,

Section 7 discusses the main advantages of the proposal and outlines some open issues for future work.

## 2. Experience: the three projects

Our experience is based on three concrete projects carried out in 2004–2014. The projects concerned the management of large-scale emergency situations with an impact on people and property. Emergency management includes several complex and interrelated tasks and requires attention by a team of emergency managers, active 24 h a day even for rather long periods of time. Emergency managers generally operate with inadequate information, under pressure, stress, and responsibility overload. In their job, they must promptly respond to the inputs arriving from the emergency field, comply with formal regulations and stated emergency plans, adapt to rapidly changing and sometimes unforeseen situations, and satisfy the requests of the upper management levels and of the involved institutions.

In this context, a DSS is certainly useful to help emergency managers in their activity. The first project was aimed at developing a DSS, called EQ-DSS in the following, for managing the health emergency caused by an earthquake event at the province level. This project was carried out in 2004– 2005 and was focused, as a case study, on the seismic event of Richter magnitude 5.5 occurred in the night of November 24, 2004 in the region around the west coast of Garda lake, near Brescia, a medium-size town in northern Italy [44]. An emergency management team was established to identify the most appropriate response plans, to assure compliance with current regulations, and to allocate the necessary resources. Furthermore, a detailed log of all events occurred, all decisions made, and all actions undertaken was compiled by the emergency managers and subsequently used as a valuable source of information for the identification of conceptual requirements of the DSS. A running DSS prototype has been developed as a client–server application, whose organization corresponds to a typical knowledge-based architecture [9]. Knowledge is specified in a declarative way and can be updated and expanded during the operational life of the system. Beyond proposing the most suitable response plans in front of occurring events, EQ-DSS helps emergency managers allocate available

resources to the actions of the currently active plans to avoid that actions that might be started without the minimal necessary resources [24].

The second experience was focused on the design and development of a DSS for managing a

pandemic flu emergency at the regional level and is referred in the following as HT-DSS. This

experience was conducted in the frame of the project HEALTHREATS—Integrated Decision Support

System for health threats and crises management—supported by an international consortium

including 11 partners from 5 European countries (Italy, Romania, Slovenia, Portugal, and Spain) and

co-funded by the European Commission’s Executive Agency for Health and Consumers during the

years 2007–2010 within the Public Health program [45]. The project produced a fully operationa

DSS prototype [22] structured per a web-based architecture. In particular, by using a knowledge-

based engine, HT-DSS allows deciding, in a structured way, which response plans to adopt and which

actions to undertake in an emergency, and accurately monitoring their execution. At the same time, it

supports collaboration among the different professional roles involved in emergency management and

can prevent different people simultaneously making uncoordinated or even contradictory decisions.

The third project dealt with the design, prototyping, and evaluation of a DSS, referred to in this paper

as TM-DSS, able to assist the personnel in charge of analyzing warnings and managing threats to a

large and complex critical infrastructure. This experience was conducted in the frame of the project

TIDES – Identification of Threats against Critical Infrastructures and Decision Support, supported by

an international consortium including 5 partners from 3 European countries (Italy, France, and Spain)

and co-funded by the European Commission’s Directorate-General Home Affairs, Directorate A:

Internal Security in 2013 and 2014 within the Prevention, Preparedness and Consequence

Management of Terrorism and Other Security-Related Risks program (CIPS 2012) [46].

The project was based on detailed requirements derived from two case studies concerning possible

terrorist attacks to a regasification plant (Cartagena, Spain) and a rail infrastructure (Torino district,

Italy). A complete feasibility study and a proof-of-concept of the TM-DSS were produced, which

demonstrate the main functional and technical features of the system. TM-DSS supports the whole

management process, from the analysis of early warnings that might denote an ongoing terrorist

activity against a critical target, to the identification of a threat and to the management of the intervention plans necessary to prevent that the threat evolves into a critical situation or, at least, to reduce its impact on people and property.

## 3. Awareness: basic concepts and scope of the work

Based on the three experiences and on an extensive analysis of literature works, we started in 2014 a reflective practice process with the goal of identifying a general approach for emergency management applicable in different practical contexts. This process started with an awareness phase, devoted to identify the basic concepts concerning an emergency management context and clarify the scope of the present research.

## 3.1 The concept of emergency and its phases

The concept of emergency does not have a unique definition. Per [53], emergencies can be humancaused, like terrorism or fire, or natural, such as severe weather, earthquakes, or pandemic diseases. Hiltz et al. [27] underline how the terms ―disaster,‖ ―crisis,‖ ―catastrophe,‖ and ―emergency‖ are sometimes used synonymously to denote serious events that have a significant impact on society. Generalizing from these proposals, on the basis of our practical experience, we define an emergency as a sequence of human-caused or natural events that anticipate or characterize a situation that causes a sudden and strong modification in a specific context with a widespread impact on the society—on people, property, and environment—requiring a prompt intervention by all involved stakeholders. Traditionally, an emergency is assumed as comprising four phases [33][39][60], namely mitigation, preparedness, response, and recovery. In this work, we focus only on the response phase, that is on the activities that occur as a response to an emergency, preventing that a threat evolves into a crisis or, at least, to limit the impact of the crisis in case it should actually occur. For the sake of simplicity, in thi paper, we call emergency management as all the activities related to the response phase and emergency managers as the specialists in charge of them. What happens before (mitigation and preparedness) and after (recovery) the response phase is outside the scope of our research. From the experience gained with the three projects illustrated in Section 2, it emerged that the response phase includes several complex and interrelated activities that need to be organized in a

structured way. This can be done by decomposing the response phase into three subphases that, for the sake of clarity, we call steps in the following:

 Warning step. A warning is a weak signal that might denote an abnormal situation anticipating a potential threat, for example, an exchange of information on the web about the preparation of a terrorist attack, a few cases of an infectious disease that might point to a potential pandemic, or the announcement of a demonstration by a social protest group that might indicate the risk of damage to public or private property. Warning management is about the collection and analysis of warning and the assessment of whether they support the identification of a threat. This step concerns the first activities of the response phase, where warnings are collected and analyzed and potential threats are identified.

 Threat step. A threat is an identified critical situation that might evolve into a harmful sequence of events, for example, a confirmed plan for terrorist attack, the warning for an upcoming hurricane, or the evidence of an initial pandemic infection. The threat step follows the warning step in case a threat has been identified. Threat management concerns the implementation of suitable intervention plans to prevent that the threat evolves into a crisis or, at least, to limit the impact of the crisis in case it should actually occur. Emergency is still in an early stage and, maybe, dangerous consequences might be avoided.

 Crisis step. A crisis is a foreseen or unforeseen sequence of events that strongly impact on people, property, and environment, for example, fire onboard a ship, a tsunami, an explosion, or a severe chemical pollution. The crisis step starts if, despite the implemented intervention plans, a threat evolves into a critical event or if an unforeseen critical event occurs. Crisis management require to undertake specific response plans to face the situation occurred, minimize its impact, and restore normality.

In each step, emergency managers are faced with specific tasks as illustrated in Table 1.

Table 1: Tasks carried out by emergency managers in the three steps of the response phase.

#

<table><tr><td>Step</td><td>Tasks</td></tr><tr><td>Warning step</td><td>Collect warnings from available information sourcesInterpret the warnings acquired looking for potential threatsIf a threat is identified, notify it to the involved parties and, in particular, to the unit in charge of threat management</td></tr><tr><td>Threat step</td><td>When a threat notification is received, select the most appropriate intervention plan to face itAssign the selected intervention plan to the operative units in charge of its executionMonitor the execution of the intervention plan and notify the results obtained to the involved parties; in particular, if the threat evolves into a crisis, notify the unit in charge of crisis management</td></tr><tr><td>Crisis step</td><td>When a crisis occurs, select the most appropriate response plan to face itAssign the selected response plan to the operative units in charge of its executionCollect and interpret information from the field about the evolution of the crisis situationMonitor the execution of the response plan and notify the results obtained to the involved parties</td></tr></table>

Finally, note that the above-proposed decomposition of the response phase into three distinct and well-defined steps allows to clearly distinguish between activities that have different goals, are grounded on different knowledge sources, and imply different decision-making problems. Often, the concept of ―response‖ is inherently bound to that of ―crisis‖ and the warning and threat steps do not receive specific consideration; however, the precrisis steps are worth the greatest attention, because in several cases, an effective management of warnings and threats can largely reduce the probability of a crisis or at least limit its impact.

## 3.2 The emergency scenario

An emergency situation, in any of the three steps defined above, involves different stakeholders that can be viewed as organized into layers; in particular, starting from the classifications provided in [50] and [21] in any emergency scenario, we can identify five main layers (Figure 1):

 the causes layer: refers to the human-related or natural events that originate an emergency situation;

 the institutional layer: pertains the institutional bodies in charge of supervising emergency management at local, regional, national, cross-border or worldwide levels;

 the management layer: includes the specialist task force in charge of planning, coordination, and control of the actions necessary to face an emergency;

 the operation layer: refers to the various bodies active on the field of an emergency—lik firefighters, police, civil protection groups, first-aid teams—in charge of implementing the planned actions;

 the population layer: refers to the people directly or indirectly affected by the events that determine the state of emergency.

![](/api/attachments/TQYTTS98/fulltext/images/8e7dc67fe66b32cfa77d87d02efd4ae540a6d67d9711b3c66d772943f7207f8d.jpg)  
Figure 1: The five layers of an emergency scenario.

## 3.3 Focus and goal of the research

In the scenario illustrated above, several research works focus on the causes layer. These are mainly interested in modeling and simulation of the temporal evolution of high-risk situations, such as the work reported in [31] on the estimate of the impacts of the detonation of a nuclear device or the project by [26] devoted to hazard modeling for earthquake preparedness, or the simulation of pandemic scenarios for decision support in health management [32].

Other projects are interested in the institutional layer. For instance, the work reported in [1] addresses the problem of enabling communication and coordination among independent governmental agencies operating in adjoining geographical areas. The work described in [59] investigates information sharing on a global scale among different worldwide organizations, with reference to the case of the SARS outbreak in 2002. Kwon and colleagues [30] analyze the socio-cognitive aspects of interoperability among different organizations in the public safety communication domain. With regard to the operation layer, literature works mainly concentrate on performance evaluation of teams operating in crisis situations (e.g., [5][17]), on training issues (e.g., [49][62]), or on investigating the role of mobile devices in field operations (e.g., [3][29]). Several research works focus also on communication and cooperation that occur at the population layer or between the population layer and the institutional layer based on social media like Facebook or Instagram (see e.g., [14][15][28][34][57]).

In this paper, we focus on the management layer, namely on the complex set of activities and interactions that occur internally to the task force in charge of emergency management. This choice is motivated by two reasons. First, the management task has been the core issue faced in all three projects mentioned in Section 2, from which the present research originates. In fact, this layer plays a fundamental role in effectively dealing with an emergency situation: a correct, timely, and sound management practice is the cornerstone of a successful action. Second, most of the approaches presented in the literature are concerned only with specific issues (e.g., [6][11]) or are applicable only in specific domains (e.g., [20][43]). Accordingly, our goal is to develop a specific conceptual tool for supporting the management layer, which can be applied in a large variety of application domains. In particular, we aim at creating a repository of expert knowledge to guide the design of DSSs that ma help emergency managers in their complex job.

## 4. Analysis: the conceptual elements of emergency management

In this section, we focus on the conceptual elements that characterize our understanding of emergency management according to the experience gained in the three projects discussed in Section 2. These conceptual elements constitute the background for the definition of the design patterns reported in Section 5.

## 4.1 The basic principle: structured collaboration as decision support

The central and easily observable issue in emergency management is coordination and cooperation— in one word collaboration—among the various stakeholders involved. This is a difficult problem that cannot be solved by adopting simple organizational models that, in an emergency situation, often fail to resist to the impact of the events, of stress, and of the strong, sudden needs arising from the field. The need for supporting collaboration in emergency management is underlined in several literature works. For instance, in [53], the authors describe the variety of collaborative efforts occurring in a local community to conduct emergency management planning activities. Turoff et al. [58] assert that systems for emergency management must be conceived as ―collaboration tools for communities of practice.‖ Indeed, collaboration allows exploiting all existing knowledge effectively, improving situation awareness [16][51], supporting information flow and task coordination [13], and correctly sharing responsibilities. On the other hand, the analysis in [60] highlights the trade-off between the need for collaboration to face the complex issues characterizing emergency management and the pressure for the security promised by a clear command chain.

Coherently with these literature studies, in the three projects illustrated in Section 2, collaboration has constantly been the key issue discussed with domain experts during the problem identification phase, and it drove the overall design of EQ-DSS, HT-DSS, and TM-DSS.

Focusing now on the concept of collaboration, it is straightforward to realize that it does not convey a unique meaning and allows for a variety of interpretations. In general, we can identify two paradigms behind the term ―collaboration.‖ The first one, free collaboration, points to a context where the collaboration process is open and unstructured, and its implementation is left to the goals, skills, and initiative of the participants. This is the case, for example, of a social network or a forum, where the collaboration framework allows easy and intuitive interaction, but does not provide any support oriented toward the achievement of particular goals or the execution of specific tasks, nor assigns specific roles to the subjects participating in the collaboration process. Free collaboration is typically domain independent, unstructured, and not goal-oriented. It supports freedom and democracy, but it does not assist in any specific task. The second paradigm, structured collaboration, refers to a form of collaboration that is ruled by specific domain knowledge and supports the participants in the execution of a specific task or the solution of a specific problem, such as, for example, participatory design, group document writing, or workflow management. Structured collaboration assigns specific roles and responsibilities to the participants, exploits domain knowledge to organize their work, and helps them perform the relevant tasks. In other words, it offers a concrete support to the participants for the effective and efficient achievement of a specific goal. Structured collaboration is, therefore, typically domain dependent and goal-oriented.

While free collaboration is certainly appropriate for modeling the interaction occurring at the population layer or between the population layer and the institutional layer, structured collaboration seems definitely necessary to assure the degree of effectiveness and efficiency required at the emergency management layer, which is the specific focus of this research.

The point is now to identify in which specific way structured collaboration might support emergency managers in their job. Behind the various tasks they are in charge of, it is easy to recognize a common issue that characterizes all their activity, namely decision-making. Decision-making is the most challenging and pervading problem of emergency management and the central topic on which collaboration should focus. Moreover, decision-making is especially critical under conditions of uncertainty and complexity [10], which indeed characterize any emergency situation. Therefore, decision support turns out as the ultimate goal of structured collaboration.

## 4.2 The organization of the emergency management layer

Collaboration is a success-critical factor in emergency management, and therefore, it must rely on a structured organization to achieve the effectiveness and efficiency required to face and solve the

many problems that characterize any step of an emergency. This in turn requires the capability to exploit all available knowledge effectively, to comply with regulations and standards, to correctly share responsibilities and tasks, and to rely on a fairly rigid command chain.

Both these remarks call for an explicit and well-defined organization of the emergency management layer. In particular, a hierarchical distributed organization turns out to be necessary. More flexible and open paradigms—certainly effective in more creative contexts—might expose emergency management to a high risk of failure and lead to chaos, which, apparently, is exactly the opposite of what emergency management should strive to achieve.

Accordingly, we assume a two-level hierarchy, including the central management unit on the top and a number of local operative units at the lower level. This organization may shrink into a simpler one in small contexts (e.g., there might be just one local unit or the central and local units might even collapse into a single structure) or expand into a more articulated one in complex situations (e.g., a three- or four-level hierarchy might be necessary).

## 4.3 A knowledge-based approach to emergency management

Emergency management is a complex and multifaceted issue that involves several aspects. In their job, emergency managers have to comply with formal regulations, apply officially stated emergency plans, find solutions to new emerging problems, dynamically adapt to a rapidly changing situation, and promptly respond both to events occurring in the emergency field and to the requests arriving from the upper management at the local, regional, or national level. They often must follow multiple reasoning paths in parallel and supervise a huge set of plans executed by local operative units. Moreover, emergency managers operate in a context that does not allow plain cooperation and relaxed work. Their activity, in all steps of the emergency process, is continuously challenged by stress, caused by task overhead, high responsibility, and time pressure. They must be able to process a large amount of rapidly changing and uncertain information and to carry out alternative reasoning paths with a defeasible logic attitude [13][21].

In this context, it is easy to recognize that the tasks of an emergency manager are typically knowledge intensive and require the best available competence and experience. While past works have

emphasized the role of information sharing [59], collaboration [12][58], and decision support [10], we advocate that the focal point is the capability of providing emergency managers with the right knowledge, in the right moment, and in the right way. In particular, three classes of knowledge can be identified that are crucial to support emergency managers in their job:

 Interpretation knowledge: necessary to assess warnings and identify potential threats, and to analyze the events occurring in the frame of a crisis situation and identify the appropriate actions to undertake;

 Operation knowledge: necessary to define the intervention and response plans that might be carried out in front of a threat or crisis situation;

 Selection knowledge: necessary to identify the best plans and the most appropriate actions to apply in a specific threat or crisis situation.

According to this approach, and considering the three steps that characterize the response phase as discussed in Section 3.1, the overall conceptual architecture of a DSS for emergency management turns out to feature a typical knowledge-based organization [18][25], as shown in Figure 2.

![](/api/attachments/TQYTTS98/fulltext/images/10d88a7bfddeebf3d533530bd7f88dfb595737e04081aa01c87edac28f52e33c.jpg)  
Figure 2: Conceptual organization of a DSS for emergency management.

## 5. Generalization: a design pattern collection for the emergency management problem

To support the conceptual design of a DSS for emergency management, we have adopted design patterns [2][23] as a tool for representing knowledge derived from the experience gained in the three projects discussed in Section 2. In fact, design patterns provide a structured but at the same time intuitive language for effective knowledge coding, sharing, and re-use. As suggested in [23], patterns should be always derived from practical experience, as it is also confirmed in [38], where the authors analyzed three systems they developed in collaboration with the Spain Department of Civil Defense and Protection to derive their design patterns for emergency management systems. Thus, the EQ-DSS, HT-DSS, and TM-DSS projects discussed in Section 2 provided an ideal background for identifying a sound and sufficiently comprehensive collection of patterns for DSS design in the emergency management field.

The process of building design patterns for the emergency management problem has been guided by the following five requirements:

1. each pattern must represent a general solution to a recurrent decision-making problem in the design of a DSS for emergency management;

2. patterns may reference other patterns that can be used to implement their solutions [2][7];

3. references between patterns must have a unique, well-defined semantics, which specifies the role of the referenced patterns in the solution of the referencing one;

4. the pattern collection must cover all main decision-making problems in emergency management;

5. the level of detail of the elementary patterns, that is of the patterns that do not reference any other pattern, must be suitable to support implementation of the specified solution.

Consequently, it is straightforward to observe that a collection of design patterns will result into a network where patterns represent nodes and references the arcs between nodes, as illustrated more formally in Section 5.1.

The construction of design patterns according to the abovementioned requirements has been performed through an iterative process, integrated in the life cycle of EQ-DSS, HT-DSS, and TM-DSS and performed during system design and development. This process includes six steps:

1. generalization from the experience, starting from the specific cases met in the EQ-DSS, HT-DSS, and TM-DSS projects, and identification of recurrent patterns (problems and solutions) according to a decomposition strategy;

2. restructuring of the patterns identified, to support as much as possible the reuse of recurrent patterns through specialization;

3. review and refinement of the patterns identified with the support of emergency management experts and DSS designers;

4. application of the patterns in the ongoing design activity, testing, and refinement;

5. final pattern statement and integration in the network of design patterns under construction;

6. testing and refinement of the network of design patterns thus far constructed with emergency management experts and DSS designers.

These steps were repeated until the network of design patterns became easy to understand and apply (understandability), to adequately cover all main decision-making problems occurring in an emergency situation (completeness), and to effectively and efficiently support the design tasks (usefulness).

Let us stress that the choice of including the identification of design patterns in the life cycle of EQ DSS, HT-DSS, and TM-DSS has allowed us to exploit all the available design experience, avoiding that part of it got lost, as it usually happens, after project conclusion. Moreover, this way design patterns have not only been identified but also immediately applied and tested, thus supporting a more effective and efficient generalization process.

## 5.1 Basic concepts

Intuitively, a design pattern (or only pattern in the following) describes in a structured way a known solution to a recurrent design problem [2]. The patterns relevant to the same application domain can be connected to each other to form a pattern network, that is a finite, directed, acyclic, connected graph [7], where nodes correspond to patterns and arcs represent references to other patterns, such that there exists one and only one node, called the root node (root pattern), with no input arcs.

If there exists an arc from a node (pattern) N1 to a node (pattern) N2, N1 is called a parent node (parent pattern) of N2, and conversely N2 a child node (child pattern) of N1. The root node, therefore, has no parent nodes. All other nodes in the graph have at least one parent node. The nodes without any child node are called leaf nodes (leaf patterns). If a node Q is a child of node P, that is there is a reference from P to Q, then we say that P references Q (or conversely, that Q is referenced by P).

In our proposal, we have identified two possible semantics for a reference, namely decomposition and specialization, thus yielding to two types of references, as defined below:

 d-reference: a pattern X d-references patterns Y1, Y2, … Yn if it can be decomposed into the n subproblems Y1, Y2, … Yn so as the solution of X can be obtained by composing together the solutions of Y1, Y2, … Yn;

 s-reference: a pattern X s-references a pattern Y, if X is a specialization of Y so as the solution of X can be obtained by specializing the solution of Y.

Note that decomposition is a one-to-many relationship between patterns and nonempty sets of patterns, since, in general, a pattern may be decomposed in several alternative ways; however, in the pattern network proposed in this paper, alternative decompositions are not considered. Specialization instead is a many-to-one relationship between patterns, because several patterns may be a specialization of the same pattern.

For nonleaf nodes, d-reference and s-reference are clearly mutually exclusive. For leaf nodes, no reference is allowed because they represent elementary patterns, whose solution does not rely on other patterns.

Going into more details, a pattern is supposed to have a structured internal organization defined according to the following template, derived through a suitable adaptation of templates proposed in the design pattern literature [2][7][19][23]:

 Pattern name: a descriptive name that suggests the goal of the pattern  Application context: the specification of the context where the pattern may be applied; in general, the list of the patterns that reference it

 Problem: the description, in a user-understandable language, of the problem that the pattern is intended to solve

 d-reference: the list of d-referenced patterns (only for nonleaf patterns whose solution is based on decomposition into subproblems)

s-reference: the s-referenced pattern (only for nonleaf patterns whose solution is based on specialization)

 Knowledge base: the knowledge repository necessary to implement the solution (only for knowledge-based patterns)

 Solution: the description of how the current problem can be solved, namely:

o for leaf patterns: the outline of the proposed solution, in terms of elementary actions and control flow;

o for nonleaf patterns whose problem can be solved through decomposition: the specification of how d-referenced patterns should interact to solve the current problem or, in other terms, how the solutions of the d-referenced patterns should be composed to yield the solution of the current problem;

o for nonleaf patterns whose problem can be solved through specialization: the specification of how the referenced pattern should be instantiated to solve the current problem, that is how its variables should be substituted with those of the current problem.

For the sake of simplicity, in the following, we will use the name of a pattern also to identify the problem solved by the pattern or the corresponding node in the pattern network. In addition, eventual empty fields in a pattern specification (namely, d-reference, s-reference, and knowledge base) will simply be omitted. Underlined words denote variable terms appearing in design patterns that are referenced through specialization.

#

## 5.2 Knowledge-based patterns

As discussed in Section 4.3, emergency management is a typically knowledge-intensive task. Accordingly, the definition of the pattern collection proposed Section 5.3 is strongly based on the analysis of domain knowledge. In particular, it is grounded on generic domain knowledge, which i shared by a large class of emergency management contexts and characterizes the way any emergency management problem should be approached. This knowledge is embodied in the design choices behind the definition of our pattern collection; namely, how patterns are defined, how problems are decomposed into subproblems, how patterns interact with each other are the result of a generalization from the three cases presented in Section 2.

However, generic domain knowledge is not enough to develop a concrete DSS for emergency management. Specific domain knowledge that characterizes each individual emergency management situation must be acquired, represented, and stored in the relevant modules defined in the pattern collection to tailor and specialize them to the particular case at hand. Although all modules depend to some extent on specific domain knowledge, some of them are strongly knowledge-based and their implementation requires resorting to specific knowledge representation and knowledge-based reasoning techniques, such as, for example, rule-based or logical reasoning. Specific domain knowledge must be collected through repeated knowledge acquisition sessions performed by professional knowledge engineers with the relevant domain experts [21]. Moreover, like any knowledge-based approach, the design of a knowledge-based module also requires that a basic domain ontology is defined, at least at terminological level, in such a way that knowledge representation can rely on a sound shared background.

## 5.3 The pattern network

A global view of the pattern network that has been developed is shown in Figure 3. Here, arcs that denote d-references are represented by solid arrows, whereas arcs that denote s-references are represented by dotted arrows; e.g., WARNING MANAGEMENT is linked to WARNING COLLECTION, WARNING INTERPRETATION, THREAT GENERATION, and THREAT NOTIFICATION through a d-reference, whereas THREAT NOTIFICATION is linked to

NOTIFICATION through an s-reference. Knowledge-based patterns are represented by rounded rectangles.

![](/api/attachments/TQYTTS98/fulltext/images/6057818b90cb084d0f1c7d93e9389dc6cc833f2c474cf3d7b690e1f833d7e9ed.jpg)  
Figure 3: The pattern network for emergency management (solid arrows denote d-references and dotted arrows denote s-references).

In broad terms, the structure of the pattern network mirrors the conceptual organization of the steps and tasks of an emergency, as illustrated in Table 1. The root node represents the most general case of an emergency management problem that may include one or more of the three subproblems warning management, threat management, and crisis management. Each one of these three problems is then further decomposed at a lower level into finer subproblems; for example, warning management i decomposed into warning collection, warning interpretation, threat generation, and threat notification. Eventually, specialization is applied to exploit the similarities shared by different problems; for example, both warning collection and signal collection are just different instances of information collection. This way, possibly applying decomposition once again if necessary (e.g., plan selection is decomposed into situation-plan matching, plan instantiation, and plan assessment), the leaf nodes are identified and the network is completed.

The whole collection of design patterns is reported in the following six Figures 4–9, according to the depth-first strategy.

![](/api/attachments/TQYTTS98/fulltext/images/6c998a64ce67f0cc7b77c987c9838f41753b4d8ef9ace742e904d75851da5a5e.jpg)

![](/api/attachments/TQYTTS98/fulltext/images/aa926c680b904d82ed5a24a474d225bd14cc3487e55cce1d35d55f79c036e4d1.jpg)

![](/api/attachments/TQYTTS98/fulltext/images/85f72ac69f5e0152ad6316c619be97a5735888605d768696c08a486fa8a8968f.jpg)  
Figure 4: The collection of design patterns – 1.

![](/api/attachments/TQYTTS98/fulltext/images/6aa06b1d595f131a5b7fbbeb1ea84b963fcf60c4f059c1bf05a160fc18aa772e.jpg)  
Figure 5: The collection of design patterns – 2.

## Pattern name: THREAT MANAGEMENT

Application context: EMERGENCY MANAGEMENT (used in isolation or together with WARNING MANAGEMENT)

Problem statement: When a threat is identified, specific actions must be carried out to prevent that it evolves into a crisis or, at least, to mitigate the impact of the crisis in case it should actually occur.

MONITORING, THREAT MANAGEMENT RESULT NOTIFICATION.

Solution: It is assumed that:

each threat deserves a specific intervention;

threats are independent from each other;

several threats can be managed in parallel;

each threat is managed through the application of one intervention plan;

each intervention plan is executed by a local operative unit;

during execution, intervention plans communicate only with the central management unit;

![](/api/attachments/TQYTTS98/fulltext/images/35b28cf6dedafd4182afa693277688bd85b2bc68eb8d2f928d091b390dd5009e.jpg)

an active intervention plan can be stopped if the threat that it is supposed to face is cancelled by a threat update or if an event causes the threat to evolve into a crisis; otherwise, it terminates when the current threat is fixed

A threat management problem can be solved by decomposing it into the four sub-problems mentioned above. As soon as a threat is received from WARNING MANAGEMENT, a new instance of THREAT MANAGEMENT is generated and INTERVENTION PLAN SELECTION is activated. In case no intervention plan appropriate to face the current threat can be identified, INTERVENTION PLAN SELECTION generates a failure that is passed to THREAT MANAGEMENT RESULT NOTIFICATION, and the relevant instance of THREAT MANAGEMENT is stopped. Otherwise, after the most appropriate intervention plan is selected, it is sent to INTERVENTION PLAN ASSIGNMENT that assigns it to the local operative unit in charge of its execution. INTERVENTION PLAN MONITORING carries out all the activities necessary to control the correct an effective execution of an intervention plan. When intermediate or final results of threat management are produced, THREAT MANAGEMENT RESULT NOTIFICATION notifies them to all involved entities

## Pattern name: INTERVENTION PLAN SELECTION

Application context: THREAT MANAGEMENT.

Problem: The most suitable intervention plan to face a threat must be selected from a library of intervention plans according to a set of intervention plan applicability criteria and intervention plan assessment and comparison criteria.

Solution: An intervention plan selection problem can be solved through specialization of PLAN SELECTION, where

the input situation is the current threat;

the plan to be selected is an intervention plan

the library of plans is the available library of intervention plans;

the applicability criteria are the intervention plan applicability criteria;

the assessment and comparison criteria are the intervention plan assessment and comparison criteria.

## Pattern name: PLAN SELECTION

Application context: INTERVENTION PLAN SELECTION and RESPONSE PLAN SELECTION

Problem: Given an input situation, it must be analysed in order to select a plan from a given library of plans according to specified applicability criteria and assessment and comparison criteria

d-reference: SITUATION-PLAN MATCHING, PLAN INSTANTIATION, PLAN ASSESSMENT.

Solution: A plan selection problem can be solved by decomposing it into the three sub-problems mentioned above. The sequential resolution of these sub-problems leads to the identification of a selected plan

## Pattern name: SITUATION-PLAN MATCHING

Application context: PLAN SELECTION.

Problem: Given an input situation, it must be matched against a library of plans in order to identify a subset of candidate plans that can be applied to the current situation according to given applicability criteria.

Knowledge base: Selection knowledge.

Solution: Situation-plan matching includes just one process, namely SPM-1, that carries out all the necessary comparisons between the input situation and the plans in the library, in order to identify the candidate plans

Figure 6: The collection of design patterns – 3.

#

![](/api/attachments/TQYTTS98/fulltext/images/28d89ea386deb68a1d55d0ee79ba4b92ff21b13a9b0d60f66c9be8d479dfa97a.jpg)  
Figure 7: The collection of design patterns – 4.

![](/api/attachments/TQYTTS98/fulltext/images/c234bc1957c733f90749eb0a218652a21bc57505539ecde32763bc4d771268ba.jpg)

![](/api/attachments/TQYTTS98/fulltext/images/1a27f7de1fb8755305d78cd8e72759db223c42587f9bbbbfb31036e0105ab6a1.jpg)  
Figure 8: The collection of design patterns – 5.

![](/api/attachments/TQYTTS98/fulltext/images/e4483b522c777913714d2ef83d8548b7f9d8550577611927008d63795c989c90.jpg)  
Figure 9: The collection of design patterns – 6.

## 6. An empirical evaluation of the pattern network

To conduct the first assessment of the validity of the proposed collection of design patterns, an empirical evaluation exercise was performed with six experts in emergency management and DSS design.

## 6.1 Method

First, the intuitive concept of validity of the proposed collection of design patterns has been better specified through a set of three research questions, namely:

RQ1: Understandability: to what extent is the design knowledge encoded in the collection of design patterns clearly structured, and easy to understand and to apply?

RQ2: Completeness: to what extent is the design knowledge encoded in the collection of design patterns complete, that is, whether it covers the totality of the recurrent problems in the design of a DSS for emergency management?

RQ3: Usefulness: to what extent is the collection of design patterns useful (effective and efficient) for supporting the design of a DSS for emergency management?

To answer these research questions, an evaluation exercise was designed. The exercise consisted of performing a DSS design task using the collection of patterns illustrated in Figures 4–9 and then reporting a critical feedback. To implement this exercise, a survey was organized including three parts: (1) a prequestionnaire to collect information about the professional background of the experts participating in the survey; (2) a core part with the description of the design task to be executed by each participant; and (3) an evaluation questionnaire to be filled in after having completed the task assigned and aimed at gathering experts’ opinion.

Ten experts in DSS design and emergency management were invited to participate in the evaluation exercise, and six of them accepted the invitation. All participants hold an MSc degree in Engineering, and two of them a PhD degree in Computer Science. Three of them are senior with over 20 years of experience, while the others have 2–10 years of professional experience. Five of the six participants rated their expertise in the design of software applications, use of design patterns, design of DSSs and

#

emergency management as ―high‖ or ―very high‖; only one participant declared to have a ―low‖ expertise in emergency management, and a ―medium‖ to ―high‖ expertise in the other topics.

After identification of the experts for the evaluation exercise, each of them was requested to carefully read the design task assigned, concerning the design of a DSS for responding to alerts about a possible terrorist attack to a soccer match. The experts were asked to develop the conceptual design of the whole DSS resorting as far as possible to the collection of design patterns provided (including the explanations provided in Sections 5.1–5.3) and to take note of the design process followed. Finally, they were asked to answer the following nine questions:

1) Is the design pattern network clear and easy to understand? Is the network structure a suitable way to organize the design patterns?

2) Are the individual patterns easy to understand? In particular, are the problems clearly stated and the suggested solutions articulated at the right level of detail?

3) Are any recurrent problems missing in the collection of design patterns?

4) Is any design pattern superfluous or useless?

5) Is representing design knowledge through a collection of patterns an effective way to capture and share the experience and the practical skills of designers?

6) Does the knowledge embedded in the design patterns represent an addition to your persona know how and experience?

7) Did the collection of design patterns prove useful to support the design task you have just faced?

8) Did the design patterns make your work more effective or efficient?

9) Did the design patterns impose undesirable constraints to your work?

The following qualitative scale is proposed to answer the abovementioned questions (a scale with an even number of values has been selected to discourage poorly informative middle-scale judgments):

NNO = definitely no

NO = no, apart from a few exceptions

YES = yes, apart from a few exceptions

YESS = definitely yes

## 6.2 Results

Table 2 summarizes all the answers provided by the six experts to the nine questions listed above. Overall, it shows a very positive assessment by confirming the general validity of the pattern collection.

Table 2: Summary of the answers to the questionnaire.

<table><tr><td>Question</td><td>Expert 1</td><td>Expert 2</td><td>Expert 3</td><td>Expert 4</td><td>Expert 5</td><td>Expert 6</td></tr><tr><td>1</td><td>YESS</td><td>YESS</td><td>YESS</td><td>YESS</td><td>YESS</td><td>YES</td></tr><tr><td>2</td><td>YESS</td><td>YES</td><td>YESS</td><td>YESS</td><td>YESS</td><td>YESS</td></tr><tr><td>3</td><td>YES</td><td>NO</td><td>NO</td><td>NO</td><td>NO</td><td>YES</td></tr><tr><td>4</td><td>NO</td><td>YES</td><td>YES</td><td>NO</td><td>NO</td><td>NO</td></tr><tr><td>5</td><td>YESS</td><td>YESS</td><td>YES</td><td>YESS</td><td>YES</td><td>YES</td></tr><tr><td>6</td><td>NO</td><td>YESS</td><td>YES</td><td>YES</td><td>YESS</td><td>NNO</td></tr><tr><td>7</td><td>YES</td><td>YES</td><td>YES</td><td>YESS</td><td>YESS</td><td>YES</td></tr><tr><td>8</td><td>YESS</td><td>YESS</td><td>YESS</td><td>YESS</td><td>YES</td><td>YESS</td></tr><tr><td>9</td><td>NNO</td><td>NO</td><td>NNO</td><td>NNO</td><td>NO</td><td>NO</td></tr></table>

In more detail:

 RQ1 (questions 1 and 2): all participants considered the network and the individual patterns easy to understand, well structured, and at the right level of detail, thus judging positively the understandability of the collection of design patterns.

 RQ2 (questions 3 and 4): the judgment reported for this research question was more controversial: four experts expressed concerns about missing recurrent problems, and four pointed out the presence of superfluous or useless patterns. Experts’ remarks and the relevant improvements made to the pattern network are reported in Table 3.

 RQ3 (questions 5, 6, 7, 8, and 9): the large majority of experts expressed a very positive judgment about the usefulness of the collection of design patterns as an effective tool for representing and sharing design knowledge and supporting the conceptual design of DSS for emergency management; only two experts assessed the added value of design patterns to their personal know-how and experience as low or inexistent (question 6); however, it is important to note that these experts are those with the highest seniority in the group (22 and 20 years of experience), and this explains their negative answer.

Table 3: Experts’ remarks and relevant improvements to the pattern network.

<table><tr><td>Expert</td><td>Remark</td><td>Improvements to the pattern network</td></tr><tr><td>1</td><td>A pattern to deal with the management of shared resources among different plans is missing.</td><td>This is indeed an important but very specific issue, which is outside the scope of the present work. It might be considered for future research.</td></tr><tr><td>2</td><td>The definition of the patterns INTERVENTION PLAN SELECTION and RESPONSE PLAN SELECTION is similar.</td><td>This is a correct remark, but two different patterns are needed because the input situation determining plan selection (threat or crisis) is different. Therefore, both patterns, which are a specialization of PLAN SELECTION, have been maintained.</td></tr><tr><td>3</td><td>Not all patterns might be useful in all cases.</td><td>This is true for any collection of design patterns. Therefore, this remark has not been considered.</td></tr><tr><td>6</td><td>It is not clear how to manage simultaneously multiple emergencies.</td><td>The definitions of the patterns THREAT MANAGEMENT and CRISIS MANAGEMENT have been clarified, stressing that all threats and events possibly occurring in a given context are considered as fully independent from each other. The case of multiple, nonindependent threats orevents will be considered in future research.</td></tr></table>

In addition to answering the evaluation questionnaire, four of six experts provided some free comments and suggestions for improvement. The most significant experts’ remarks are reported below, together with our comments:

 Expert 2 stressed that the meaning of the reference relations between design patterns was not clear. In fact, the template used in the first version of design patterns submitted to the experts included just a generic ―reference‖ field without a precise definition. On the basis of this observation, we decided to clarify the semantics of the ―reference‖ field by explicitly including in the pattern template two types of references, namely ―d-reference‖ and ―s-reference‖, each one with a well-defined meaning.

 Expert 2 found a bit strange that threat management does not include signal collection and signal interpretation tasks as they occur in crisis management. This is apparently a correct observation, but by ―signal,‖ we explicitly refer either to an additional event that deserves a response through new response plan or to an information message about the ongoing crisis situation. A threat situation, instead, cannot produce further threats because each new threat is dealt with individually through a new instance of the THREAT MANAGEMENT pattern. In the frame of a threat situation, only threat updates (recognized by WARNING MANAGEMENT) can occur or activity messages generated by local operative units can arrive. Therefore, we decided to better explain these aspects in the description of the relevant patterns by keeping, however, unchanged the structure of the pattern network.

 Expert 4 suggested to define a new design pattern INTERPRETATION and redefine WARNING INTERPRETATION and SIGNAL INTERPRETATION as specializations of that pattern. However, this modification would make it difficult to specify the solution of the new pattern, which should be parametric with regard to not only the content of the knowledge base but also its organization, the representation language adopted, and the relevant reasoning algorithm. This would increase the complexity of the pattern network, without any real advantage, and therefore, we decided not to add the new INTERPRETATION pattern but to improve the explanation of knowledge-based patterns in Section 5.2.

 Expert 5 observed that the collection of patterns looks quite complete under the assumption of strong coordination among emergency managers, but further patterns would be necessary to manage the interactions among different institutions during an emergency situation. This is definitely true, but this issue is, however, outside the scope of this research that focuses on the management layer, as underlined in Section 3.3.

 Expert 1 commented that the assumption of independence between the management activities concerning different threat or crisis situations seems too strong and highlighted that the problem of resource management is overlooked. Both are important issues that imply, however, an extended restructuring of the pattern network; they will be dealt with in a future version of the design patterns.

 Expert 2 recommended to include the assessment of threat severity either as a new pattern or in the description of threat generation. Similar to the preceding remark of expert 1, this issue will be dealt with in a future version of the design patterns.

## 7. Discussion and conclusion

The main contribution of the research presented in this paper is the definition of a practical approach to the design of DSSs for emergency management based on a structured collection of design patterns—namely a pattern network—applicable to a variety of concrete application contexts. The design patterns especially focus on the conceptual level of the design task, leaving software engineers free to implement the system according to their own programming practice. The background knowledge on which our approach is based has been derived from practical experiences of DSS development in three concrete domains. It has been properly analyzed, distilled, and generalized to become a domain-independent source, which can be applied to a large variety of emergency situations. Knowledge has been represented in the form of design patterns [2], according to a structured but intuitive representation, to favor communication among the different members of a design team and promote a participatory approach to DSS design [4].

We advocate that the proposed collection of design patterns might constitute a valuable reference knowledge source for both DSS designers and domain experts, making their job more disciplined, effective, and efficient. The validity of our proposal has been supported by the positive results obtained through an empirical evaluation exercise carried out with DSS designers and emergency management experts.

With regard to related works, it is important to mention that a similar pattern-based approach to knowledge representation in the context of emergency management has been proposed in [19], where the authors provide a collection of design patterns for web-based emergency information systems (WEMS). However, the topic of emergency information systems is definitely a different one from DSS design. Moreover, while the patterns proposed in [19] focus on user interaction and interface design, our proposal concentrates on the task of conceptual design and specifically addresses the application logic layer of a system.

The collection of design patterns proposed in this paper, differently from existing approaches proposed in software engineering (e.g., [23]), has been structured according to a finite, directed, acyclic, connected graph. In this way, design patterns can drive the development of a DSS through a top-down problem decomposition strategy, supporting at the same time reuse of known solutions in different contexts through specialization. This approach can be regarded as complementary to that proposed in [42], which is based on meta-modeling techniques.

The paper is compliant with the general definition of emergency proposed in the current literature [27][50], but decomposes the response phase into finer steps—namely warning, threat, and crisis— thus supporting a more detailed understanding of the emergency management task, which constitutes the background for the definition of the design patterns.

Finally, it is important to stress that design patterns have been defined by considering emergency management as a collaboration task [53][58]. In particular, we advocate the need for structured collaboration to ensure the kind of procedural and task-oriented support that proved necessary for emergency management, as suggested in [13][16][50]. This approach goes, therefore, beyond free collaboration, which exploits social media technologies to collect and distribute a wide range of data about an emergency, opening up new opportunities for citizen participation [14][28][34][57], but often causing an information overload. Both from our experience and literature works [12][32], it clearly appears that supporting decision-making is still the most challenging objective in emergency management and the most crucial for success. Therefore, the collection of design patterns proposed in this paper considers decision support as the main function that should be offered in emergency situations to enable structured collaboration. This is in accordance with the analysis of the role of information technology in facilitating collaboration among knowledge workers [47]: like in many other knowledge-intensive organizations, even in emergency management, there is a need for reducing communication overhead to save time for collaborative problem-solving.

The experience discussed in this paper has opened up some important research issues that will be faced in future research:

 extending the proposed collection of design pattern collection with more specific and lower-level patterns specialized to a variety of emergency contexts (e.g., fire, earthquakes, terrorism, pandemic diseases, chemical emergencies, floods, etc.);

 specifying the internal structure of the knowledge bases referenced by design patterns by suggesting a suitable standard representation language and a practical guide for knowledge elicitation;

 introducing the concept of severity of a threat or an event occurring during crisis management that might be useful to support a more clever selection of intervention and response plans (suggested by expert 2 – see Section 6.2);

 considering the complex task of resource management and, more specifically, of resource allocation to the intervention and response plans (suggested by expert 1 – see Section 6.2);

 focusing the problem of multiple, nonindependent threats and crises occurring in the same time frame (suggested by expert 1 – see Section 6.2).

The collection of design patterns presented in this paper will be applied in the near future in new projects that will provide additional hints for validation and refinement. We consider our collection of design patterns only the first step of a long path: extensions or revisions from other researchers based on their own experience are welcome.

## Biographical Notes

## Daniela Fogli

Daniela Fogli received her Master’s degree in Computer Science from the University of Bologna, Italy, in 1994 and PhD in Information Engineering from the University of Brescia, in 1998. Currently, she is an Associate Professor of Computer Science at the Department of Information Engineering, University of Brescia, Italy. From 1998 to 2000, she was a post-doc grant holder at the Joint Research Centre of the European Commission. Since 2000 to April 2015, she has been an Assistant Professor at the University of Brescia. Her research interests are mainly in the field of human-computer interaction and include methods for designing complex interactive systems, meta-design, end-user development, web usability and accessibility, and decision support systems. Recently, she served as a program co-chair of the ACM SIGCHI Italian Chapter International Conference on Computer-Human Interaction (CHItaly 2015) and a short paper co-chair of the ACM International Working Conference on Advanced Visual Interfaces (AVI 2016).

## Claudio Greppi

Claudio Greppi received the Laurea degree in Electronics Engineering from Politecnico di Milano, Italy, in 1995. He worked at Web Models S.r.l. as Senior Analyst; and since 2003, he is CTO at Argonet S.r.l. His interests are in software project management, UML, web services and decision support systems.

## Giovanni Guida

Giovanni Guida received the Laurea degree (Dr.Ing.) in Electronic Engineering (major in Computer Science) from Politecnico di Milano, Italy, in 1975.

Currently, he is a Full Professor of Computer Science at the University of Brescia, Italy. He is a principal investigator of the “Knowledge Engineering and Human-Computer Interaction” research group at the Department of Information Engineering of the University of Brescia.

Previously, he taught at the Politecnico di Milano (1984–1986) and at the University of Udine (1979–1983, 1987–1990), where he founded and directed a research group in the area of artificial intelligence during 10 years (1980–1990). He has been the director of the computing center of the University of Udine (1984–1985, 1989–1990) and of the University of Brescia (1991–1993).

His present research interests include knowledge-based systems, decision support, uncertain reasoning, argumentation theory, human-computer interaction, knowledge engineering methodologies and applications, collaboration and cooperation, and web site design

He is active as an independent consultant in the area of information technology applications and knowledge management. He teaches advanced courses and conducts executive seminars in the field of emerging information technologies.

## References

[1] I. Aedo, P. Díaz, J. M. Carroll, G. Convertino, M. B. Rosson, End-user oriented strategies to facilitate multi-organizational adoption of emergency management information systems, Information Processing and Management 46(1) (2010) 11-21.

[2] C. Alexander, S. Ishikawa, M. Silverstein, M. Jacobson, I. Fiksdahl-King, S. Angel, A Pattern Language: Towns, Buildings, Construction, Oxford University Press, UK, 1977.

[3] L. K. Andresen, E. G. Nilsson. Finding the best devices for emergency responders in Norway – an empirical study, Proceedings of the 11th ISCRAM Conference, University Park, PA, USA, 2014, pp. 110-119.

[4] REMOVED FOR ANONYMITY.

[5] T. Berggren, B. J. E. Johansson, N. Baroutsi, I. Turcotte, S. Tremblay, Assessing team focused behaviors in emergency response teams using the shared priorities measure, Proceedings of the 11th ISCRAM Conference, University Park, PA, USA, 2014, pp. 130-134.

[6] L. Bidoux, J-P. Pignon, F. Bénaben, A model driven system to support optimal collaborative processes design in crisis management, Proceedings of the 11th ISCRAM Conference, University Park, PA, USA, 2014, pp. 245-249.

[7] J. Borchers, A pattern approach to interactive design. John Wiley, Chichester, UK, 2001.

[8] T. Borton, Reach, Touch and Teach, McGraw-Hill, 1970.

[9] F. Burstein, S. A. Carlsson, Decision Support Through Knowledge Management, In: F. Burstein, C. W. Holsapple (Eds.), Handbook on Decision Support Systems 1, Springer, Berlin Heidelberg, Germany, 2008, pp. 103-120

[10] F. Burstein, G. R. Widmeyer, Decision support in an uncertain and complex world, Decision Support Systems 43 (2007) 1647-1649.

[11] A. C. Calderon, J. Hinds, P. Johnson, IntCris: A tool for enhanced communication and collective decision-making during crises, Proceedings of the 11th ISCRAM Conference, University Park, PA, USA, 2014, 205-214.

[12] L. Carver, M. Turoff, Human-Computer Interaction: The human and computer as a team in Emergency Management Information Systems, CACM 50(3) (2007) 33–38.

[13] R. Chen, R. Sharman, H. R. Rao, S. J. Upadhyaya, Coordination in emergency response management. CACM 51(5) (2008) 66-73.

[14] L. M. Collins, J. E. Powell, C. E. Dunford, K. K. Mane, and M. L. B. Martinez, Emergency Information Synthesis and Awareness Using E-SOS, Proceedings of the 5th ISCRAM Conference, Washington, USA, 2008, pp. 618-623.

[15] S. L. Condon, J. R. Robinson, Communication Media Use in Emergency Response Management, Proceedings of the 11th ISCRAM Conference, University Park, PA, USA, 2014, 687-696.

[16] G. Convertino, H. M. Mentis, A. Slavkovic, M. B. Rosson, J. M. Carroll, Supporting Common Ground and Awareness in Emergency Management Planning: A Design Research Project, ACM Transactions on Computer-Human Interaction 18(4) (2011) 22:1-22-34.

[17] A. da Costa Duarte, M. R. da Silva Borges, J. O. Gomes, P. V. R. de Carvalho, ASC Model: a process model for the evaluation of simulated field exercises in the emergency domain, Proceedings of the 10th ISCRAM Conference, Baden-Baden, Germany, 2013, pp. 551-555.

[18] A. De Maio, G. Fenza, M. Gaeta, V. Loia, F. Orciuoli, A knowledge-based framework for emergency DSS, Knowledge-Based Systems 24(8) (2011) 1372-1379.

[19] P. Diaz, P. Acuña, I. Aedo, A. Malizia, A Design Patterns Catalog for Web-Based Emergency Management Systems, In: A. D’Atri et al., Management of the Interconnected World, Springer Verlag Berlin Heidelberg, 2010, pp. 387-394.

[20] J. Dunkel, A. Fernández, R. Ortiz, S. Ossowski, Event-driven architecture for decision support in traffic management systems, Expert Systems with Applications 38(6) (2011) 6530-6539.

[21] REMOVED FOR ANONYMITY.

[22] REMOVED FOR ANONYMITY.

[23] E. Gamma, R. Helm, R. Johnson, J. Vlissides, Design patterns: Elements of re-usable objectoriented software. Addison-Wesley, Reading, MA, USA, 1995.

[24] REMOVED FOR ANONYMITY.

##

[25] G. Guida, C. Tasso, Design and Development of Knowledge-Based Systems: From Life Cycle to Methodology, John Wiley & Sons, Inc., New York, NY, USA, 1995.

[26] J. R. Harrald, T. Jefferson, F. Friedrik, S. Sener, C. Mixted-Freeman, A First Step in Decision Support Tools for Humanitarian Assistance during Catastrophic Disasters: Modeling Hazard Generated Needs, Proceedings of the 4th ISCRAM Conference, Delft, NL, 2007, pp. 51-56.

[27] S. R. Hiltz, P. Diaz, G. Mark, Introduction: Social Media and Collaborative Systems for Crisis Management, ACM Transactions on Computer-Human Interaction 18(4) (2011) 18:1-18:6.

[28] A. Krakovsky, The Role of Social Networks in Crisis Situations: Public Participation and Information Exchange, Proceedings of the 7th ISCRAM Conference, Seattle, USA, 2010.

[29] J. Kuula, V. Auvinen, O. Kauppinen, P. Kettunen, S. Viitanen, T. Korhonen, Smarthpones as an Alerting, Command and Control System for the Preparedness Groups and Civilians: Results of Preliminary Tests with the Finnish Police, Proceedings of the 10th ISCRAM Conference, Baden-Baden, Germany, 2013, pp. 42-51.

[30] G. H. Kwon, T. L. Smith-Jackson, C. W. Bostian, Socio-Cognitive Aspects of Interoperability: Understanding Communication Task Environments among Different Organizations, ACM Transactions on Computer-Human Interaction 18(4) (2011) 20:1-18:21.

[31] T. Jefferson, J. R. Harrald, Estimating the Impacts of Associated with the Detonation of an Improvised Nuclear Device. 2014, Proceedings of the 11th ISCRAM Conference, Universit Park, PA, USA, 2014, pp. 80-84.

[32] J. Jenvald, M. Morin, T. Timpka, H. Eriksson, Simulation as Decision Support in Pandemic Influenza Preparedness and Response, Proceedings of the 4th ISCRAM Conference, Delft, NL, 2007, pp. 295–304.

[33] A. LeDuc , L. Juntunen, E. Stocker, A Guide to Planning Resources on Transportation and Hazards, Natural Hazards Informer 4 (2009). Available at: http://www.nap.edu/read/23008/chapter/1

[34] A. Malizia, A. Bellucci, P. Díaz, I. Aedo, S. Levialdi, eStorys: A visual storyboard system supporting back-channel communication for emergencies, Journal of Visual Languages and Computing 22(2) (2011) 150-169.

[35] D. Mendonça, G. E. G. Beroggi, Decision support for improvisation during emergency response operations, International Journal of Emergency Management 1(1) (2001) 30-38.

[36] U. Meissen, M. Hardt, A. Voisard, Towards a General System Design for Community-Centered Crisis and Emergency Warning Systems, Proceedings of the 11th ISCRAM Conference, University Park, USA, 2014, pp. 155-159.

[37] R. Minciardi, R. Sacile, E. Trasforini, A decision support system for resource intervention in real-time emergency management. International Journal of Emergency Management 4(1) (2007) 59-71.

[38] L. Montells, S. Montero, P. Diaz, I. Aedo, Mining Patterns for Web-based Emergency Management Systems, Proceedings of the 4th ISCRAM Conference, Delft, NL, 2007, pp. 133- 138.

[39] A. H. Mushkatel, L. F. Weschler, Emergency Management and the Intergovernmental System, Public Administration Review 45 (1985) 49-56.

[40] J. Nielsen, Usability Engineering, Academic Press, San Diego, USA, 1993.

[41] A. Ostfeld, E. Salomons, Optimal Layout of Early Warning Detection Stations for Water Distribution Systems Security, J. Water Resour. Plann. Management 130(5) (2004) 377–385.

[42] S. H. Othman, G. Beydoun, Model-driven disaster management. Information & Management, 50(5) 2013 218-228.

[43] K. N. Papamichail, S. French, Design and evaluation of an intelligent decision support system for nuclear emergencies, Decision Support Systems, 41(1) (2005) 84-111.

[44] Project 196320, An integrated decision support system for crisis management, supported by Regione Lombardia, Italy, FSE, Misura D4, November 2004 – December 2005.

[45] Project 2006203, HEALTHREATS - Integrated Decision Support System for health threats and crises management, supported by the European Union, Executive Agency for Health and Consumers, May 2007 – September 2010.

[46] Project HOME/2012/CIPS/AG/4000003773, TIDES - Identification of Threats against Critical Infrastructures and Decision Support, supported by the European Commission’s Directorate-

General Home Affairs, Directorate A: Internal Security, within CIPS 2012 program, May 2013 - October 2014, website: http://www.tides.provincia.novara.it/

[47] P. Pyöriä, Information Technology, Human Relations and Knowledge Work Teams, IEEE Engineering Management Review 35(4) (2007) 87-94.

[48] G. Rolfe, D Freshwater, M. Jasper, Critical reflection in nursing and the helping professions: a user’s guide, Palgrave Macmillan Ltd, 2001.

[49] J. Rudinsky, E. T. Hvannberg, Communication Interface for Virtual Training of Crisis Management, Proceedings of the 10th ISCRAM Conference, Baden-Baden, Germany, 2013, pp. 125-134.

[50] A. Sagun, D. Bouchlaghem, C. J. Anumba, A scenario-based study on information flow and collaboration patterns in disaster management, Disasters 33(2) (2009) 214-238.

[51] C. Sapateiro, P. Antunes, An Emergency Response Model Toward Situational Awareness Improvement, Proceedings of the 6th ISCRAM Conference, Goteborg, Sweden, 2009.

[52] J. M. Scanlon, J W. M. Chernomas, Developing the reflective teacher, Journal of Advanced Nursing 25(6) (1997) 1138–1143.

[53] W. A. Schafer, J. M. Carroll, S. Hayes, S. Abrams, Emergency Management Planning as Collaborative Community Work, Journal of Homeland Security Emergency Management 5(1) (2008) 1-17.

[54] D. Schön, The Reflective Practitioner, How Professionals Think In Action, Basic Books, London, UK, 1983.

[55] S. Shan, L. Wang, L. Li, Y. Chen, An emergency response decision support system framework for application in e-government, Information Technology and Management 13 (2012) 411-427.

[56] G. D. Sherwood, S. L. Horton-Deutsch, Reflective Practice: Transforming Education and Improving Outcomes, Sigma Theta Tau International, 2012.

[57] J. Sutton, L. Palen, I. Shklodvski, Backchannels on the Front Lines: Emergent Uses of Social Media in the 2007 Southern California Wildfires, Proceedings of the 5th ISCRAM Conference, Washington, USA, 2008, pp. 624-632.

[58] M. Turoff, S. R. Hiltz, C. White, L. Plotnick, A. Hendela, X. Yao, The Past as the Future of Emergency Preparedness and Management, International Journal of Information Systems for Crisis Response and Management 1(1) (2009) 12-28.

[59] P. J. van Baalen, P. C. van Fenema, Instantiating global crisis networks: The case of SARS, Decision Support Systems 47 (2009) 277-286.

[60] W. L. Waugh, G. Streib, Collaboration and leadership for effective emergency management, Public Administration Review 66 (2006) 131-140.

[61] E. Wenger, R. McDermott, W. Snyder, Cultivating communities of practice: a guide to managing knowledge, Harvard Business School Press, Boston, USA, 2002.

[62] T. Zarraonandia, V. Banũls, I. Aedo, P. Díaz, M. Turoff, A Scenario-Based Virtual Environment for Supporting Emergency Training, Proceedings of the 11th ISCRAM Conference, University Park, USA, 2014, pp. 80-84.

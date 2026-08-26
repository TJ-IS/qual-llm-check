---
otero_id: 628
otero_key: "B8DR47B7"
title: "Intelligent environment for monitoring Alzheimer patients, agent technology for health care"
authors: "Juan M. Corchado; Javier Bajo; Yanira de Paz; Dante I. Tapia"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.04.008"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Intelligent environment for monitoring Alzheimer patients, agent technology for health care

Juan M. Corchado, Javier Bajo <sup>⁎</sup>, Yanira de Paz, Dante I. Tapia

Departamento Informática y Automática Universidad de Salamanca, Plaza de la Mercaed s/n, 37008, Salamanca, Spain

Received 18 August 2006; received in revised form 9 March 2007; accepted 30 April 2007 Available online 6 May 2007

## Abstract

This paper presents an autonomous intelligent agent developed for monitoring Alzheimer patients' health care in execution time in geriatric residences. The AGALZ (Autonomous aGent for monitoring ALZheimer patients) is an autonomous deliberative casebased planner agent designed to plan the nurses' working time dynamically, to maintain the standard working reports about the nurses' activities, and to guarantee that the patients assigned to the nurses are given the right care. The agent operates in wireless devices and is integrated with complementary agents into a multi-agent system, named ALZ-MAS (ALZheimer Multi-Agent System), capable of interacting with the environment. AGALZ description, its relationship with the complementary agents, and preliminary results of the multi-agent system prototype in a real environment are presented. © 2007 Elsevier B.V. All rights reserved.

Keywords: Multi-agent system; Deliberative agent; Case-based reasoning; RFID; Health care

## 1. Introduction

Agents and multi-agent systems (MAS) have become increasingly relevant for developing distributed and dynamic open systems. The AGALZ (Autonomous aGent for monitoring ALZheimer patients) agent is aimed to improve the efficiency of health care in geriatric residences. This paper describes the AGALZ agent and explains how this deliberative planning agent has been designed and implemented. The AGALZ agent has been integrated within a multi-agent system called ALZ-MAS (ALZheimer Multi-Agent System), developed for facilitating the management and control of geriatric residences. The aim of this paper is to present the AGALZ agent and to demonstrate how its planning mechanism improves the medical assistance in geriatric residences by optimizing the visiting schedules. These agents also facilitate the nurses' and doctors' work by providing updated information about patients and emergencies, as well as historical data.

The applications of agents and multi-agent systems in the health care and clinical management environments are becoming a reality; this fact has been reported for example by Foster et al. [7]. Most agent-based applications are related to the use of this technology in patient monitoring, treatment supervision and data mining. Lanzola et al. [11] present a methodology that facilitates the development of interoperable intelligent software agents for medical applications and propose a generic computational model for implementing them. The model may be specialized in order to support all the different information and knowledge related requirements of a hospital information system. However, they do not contemplate the possibility of using wireless and RFID technology as in this paper, nor have they proposed the use of dynamic planning. Others, such as Jeffrey and Meunier [13] propose the use of virtual machines supporting mobile software agents using the functional programming paradigm. This virtual machine provides the application developer with a rich and robust platform upon which to develop distributed mobile agent applications, specifically when targeting distributed medical information and distributed image processing. This interesting proposal is not viable due to the security reasons that affect mobile agents, and they have not defined an alternative for locating patients or generating planning strategies. There are also agentbased systems that help patients to get the best possible treatment and remind the patient about follow-up tests [14]. They assist the patient in managing continuing ambulatory conditions (chronic problems). They also provide health-related information by allowing the patient to interact with the on-line health care information network. Others such as Decker and Li [6], propose a system to increase hospital efficiency using global planning and scheduling techniques. They propose a multi-agent solution using the generalized partial global planning approach that preserves the existing human organization and authority structures, while providing better system-level performance (increased hospital unit throughput and decreased patient stay time). To do this, they extend the proposed planning method with a coordination mechanism to handle mutually exclusive resource relationships, using resource constraint scheduling. This system does not use dynamic planning, it uses a static task assignment, and it does not work on wireless devices and does not use location information or RFID technology.

The AGALZ agents are integrated within ALZ-MAS multi-agent system which is a dynamic system for the management of different aspects of the geriatric center. This distributed system uses Radio Frequency Identification (RFID) [16] technology for ascertaining patients location in order to maximize their safety or to generate medical staff plans. The development of such multiagent system has been motivated for one of the more distinctive characteristics of geriatric or Alzheimer residences, which is their dynamism, in the sense that the patients change very frequently (new patients arrive and others pass away), while the staff rotation is also relatively high and they normally work in shifts of eight hours. ALZ-MAS provides the personnel of the residence with updated information about the center and the patients, provides the working plan, information about alarms or potential problems and keeps track of their movements and actions within the center. Dynamic problems require the dynamic solutions provided by this technology. From the user's point of view the complexity of the solution has been reduced with the help of friendly user interfaces and a robust and easy to use multi-agent system.

The proposed planning agent AGALZ is a deliberative one and uses a case-based reasoning (CBR) [1] architecture, that allows it to respond to events, to take the initiative according to its goals, to communicate with other agents, to interact with users, and to make use of past experiences to find the best plans to achieve goals. This particular agent uses a special type of CBR systems which we call Case-Based Planning (CBP) system, specially designed for planning construction. AGALZ is also a deliberative agent that works at a high level with the concepts of Believe, Desire, Intention (BDI) [3]. The AGALZ can be called a CBP–BDI agent, and has learning and adaptation capabilities, which facilitates its work in dynamic environment. A CBP–BDI agent is therefore a particular type of CBR–BDI agent [5], which uses case-based reasoning as a reasoning mechanism, which allows it to learn from initial knowledge, to interact autonomously with the environment as well as with users and other agents within the system, and to have a large capacity for adaptation to the needs of its surroundings.

There is an ever growing need to supply constant care and support to the disabled and elderly [15] and the drive to find more effective ways to provide such care has become a major challenge for the scientific community. During the last three decades the number of Europeans over 60 years old has risen by about 50%. Today they represent more than 25% of the population and it is estimated that in 20 years this percentage will rise to one third of the population, meaning 100 millions of citizens [4]. This situation is not exclusive to Europe, since studies in other parts of the world show similar tendencies. In the United States of America, people over 65 years old are the fastest growing segment of the population and it is expected that in 2020 they will represent about 1 of 6 citizens totaling 69 million by 2030 [9]. Furthermore, over 20% of people over 85 years old have a limited capacity for independent living, requiring continuous monitoring and daily care. The Institute of Medicine has studied the role of information technology in improving health care delivery in the US. In [12], the Institute presents a strategy and an action plan to foster innovation and improve the delivery of care. The need to reinvest in the system is underlined and as such six health care aims are defined (to be safe, effective, patient-centered, timely, efficient and equitable) and ten guidelines for the redesign of the system are given focusing on the role of the patient and improvements in knowledge, communication and safety mechanisms. Moreover the Institute proposes a strategy to improve safety in health care based on the study of medical errors [9]. The proposed system presented here has been conceived and developed taking these considerations into account.

The importance of developing new and more reliable ways to provide care and support to the elderly is underlined by this trend [4], and the creation of secure, unobtrusive and adaptable environments for monitoring and optimizing health care will become vital. Some authors [15] consider that tomorrow's health care institutions will be equipped with intelligent systems capable of interacting with humans. Multi-agent systems and architectures based on intelligent devices have recently been explored as supervision systems for medical care for the elderly or Alzheimer patients [7], these intelligent systems aim to support them in all aspects of daily life, predicting potential hazardous situations and delivering physical and cognitive support. Multi-agent systems together with the use of RFID technology offer new possibilities and open new fields such as the ambient intelligence that may facilitate the integration of distributed intelligence software applications in our daily life.

Radio Frequency Identification (RFID) [16] is an automated data-capture technology that can be used to electronically identify, track, and store information about products, items, components or people. It is most frequently used in industrial/manufacturing, transportation, distribution, and warehousing industries, but there are other growth sectors including health care [16]. ALZ-MAS uses microchips mounted on bracelets worn on the patient's wrist or ankle, and sensors installed over protected zones, with an adjustable capture range up to 2 m. The microchips or transponders use a 125 kHz signal help locate the patients, which can be ascertained by consulting the AGALZ agents installed in personnel PDAs.

The following section presents the AGALZ agent and its planning strategy. Section 3 shows the Multiagent system ALZ-MAS in which AGALZ has been incorporated. Section 4 presents the results obtained with the system and the conclusion.

## 2. AGALZ: autonomous health care agent

AGALZ is an autonomous deliberative case-based planner (CBP–BDI) agent developed for integration within a multi-agent system named ALZ-MAS. The goal of this agent is to provide efficient working schedules, in execution time, for geriatric residences staff and therefore to improve the quality of health care and the supervision of patients in geriatric residences. Each of the AGALZ agents is assigned to a nurse or a doctor of a residence, and provides also information about patient locations, historical data and alarms. As the members of the staff are carrying out their duties (following the plan provided by the agent) the initial proposed plan may need to be modified due for example to delays or alarms, in this case the agent is capable of replanning in execution time. The internal structure and capabilities of the AGALZ agents are based on the mental aptitudes of beliefs, desires, and intentions. This high level structure facilitates the incorporation of CBR systems [1] as a deliberative mechanism within BDI agents, facilitating learning and adaptation and providing a greater degree of autonomy than pure BDI architecture [5].

![](/api/attachments/B8DR47B7/fulltext/images/748666e6c7ca1c031c8a17e2dd7e9927a7c4836c4bfde87dd0dd36bb575ed8fd.jpg)  
Fig. 1. AGALZ internal structure.

To introduce a CBR motor into a BDI agent it is necessary to represent the cases used in a CBR system by means of beliefs, desires and intentions, and implement a CBR cycle. A case is a past experience composed of three elements: an initial state or problem description that is represented as a belief; a final state that is represented as a set of goals; and the sequence of actions that makes it possible to evolve from an initial state to a final state. This sequence of actions is represented as intentions or plans. In a planning agent, the reasoning motor generates plans using past experiences and planning strategies, so the concept of Case-Based Planning is obtained [8]. CBP consists of four sequential stages: retrieve stage to recover the most similar past experiences to the current one; reuse stage to combine the retrieved solutions in order to obtain a new optimal solution; revise stage to evaluate the obtained solution; and retain stage to learn from the new experience.

Fig. 1 shows the internal structure of a CPB-BDI agent. Problem description (initial state) and solution (situation when final state is achieved) are represented as beliefs, the final state as a goal (or set of goals), and the sequences of actions as plans. The CBP cycle is implemented through goals and plans. When the goal corresponding to one of the CBP stages is triggered, different plans (algorithms) can be executed concurrently to achieve the goal. Each plan can trigger new sub-goals and, consequently, cause the execution of new plans. AGALZ is an autonomous agent that can survive in dynamic environment because incorporates this planning mechanism. The following subsection presents the planning structure of the AGALZ agent.

## 3. The planning model of the AGALZ agent

A deliberative CBP–BDI agent is specialized in generating plans in execution time and incorporates a case-based planning (CBP) reasoning mechanism. The purpose of the CBR agent is to solve new problems by adapting solutions that have been used to solve similar problems in the past [1], and the CBP–BDI agents are a variation of the CBR–BDI agents, based on the plans generated from each case. The AGALZ agents require dynamic planning systems that allow them to respond to changes in the environment and to provide efficient plans in execution time for optimizing the working rotas. The CBP planner used by the AGALZ agent identifies a plan, for a given nurse, to provide daily nursing care in the residence. It is very important to maintain a map with the location of the different patients at the time of planning or replanning, which is why RFID technology is used to facilitate the location and identification of patients, nurses and doctors.

So as not to overload the mathematical formula without losing generality, this section explains how the most replannable plan is chosen, focussing on one nurse and one patient. Let $E { = } \{ e _ { 0 } { , } { \ldots } { , } e _ { \mathrm { n } } \}$ the set of tasks that the nurse is assigned to.

$$
a _ {j}:\begin{array}{c}E\\e _ {i}\end{array}\stackrel {{\rightarrow}} {{\rightarrow}}\begin{array}{c}E\\a _ {j} (e _ {i}) = e _ {j}\end{array}.\tag{1}
$$

An agent plan is the name given to a sequence of actions (1) that, from a current state $e _ { 0 } ,$ defines the path of states through which the agent passes in order to offer the nurses the optimum path according to each of their characteristics. Below, in Eq. (2), the dynamic relationship between the behaviour of the agent and the changes in medium is modelled. The behaviour of agent A can be represented by its action function $a _ { A } ( t ) \forall t ,$ defined as a correspondence between one moment in time t and the action selected by the agent,

$$
\operatorname{Agent} A = \left\{a _ {\mathrm{A}} (t) \right\} _ {t \in b T \subseteq N}.\tag{2}
$$

From the definition of the action function $a _ { A } ( t )$ it is possible to define a new relationship that collects the idea of an agent's action plan (3),

$$
P _ {A}: \underset {(t, a _ {A} (t))} {T x A} \to \underset {} {A} {P _ {A} (t)}\tag{3}
$$

in the following way,

$$
P _ {A} (t _ {n}) = \sum_ {i = 1} ^ {n} a _ {i A} (t _ {i} - t _ {i - 1}).\tag{4}
$$

Given the dynamic character desired for the planning agent, for a definition of the agent plan, the continuous extension of the previous expression (4) is proposed, in other words (Eq. (5))

$$
P _ {A} (t _ {n}) = \int_ {t _ {0}} ^ {t _ {n}} a _ {A} (t) \mathrm{d} t.\tag{5}
$$

The variation of the agent plan $p _ { A } ( t )$ will be provoked essentially by: The changes that occur in the environment and that force the initial plan to be modified, and the knowledge from the success and failure of the plans that were used in the past, and which are favoured or punished via learning. O indicates the objectives of the agent and $o ^ { , }$ are the results achieved by the plan. R are the total resources and $R ^ { \star }$ are the resources consumed by the agent. The efficiency of the plan (6) is the relationship between the objectives attained and the resources consumed

$$
E _ {\mathrm{ff}} = \frac {\# (O ^ {\prime} \cap O)}{\# R ^ {\prime}}.\tag{6}
$$

Where # means cardinal of a set. The objective is to introduce an architecture for a planning agent that behaves – and selects its actions – by considering the possibility that the changes in the environment block the plans in progress. This CBP–BDI agent searches continually for the plan that can most easily be replanned in the event of interruption (the most replan-able intention). Given an initial point $e _ { 0 } ,$ the term planning problem is used to describe the search for a way of reaching a final point $e _ { i } { \equiv } e ^ { * } { \in } E$ that meets a series of requirements. Given a discrete variable X that can take values of a numerable set represented as

$$
X = \{x _ {i} \} _ {i \in N}.\tag{7}
$$

It is possible to define the associated accumulated variable (8), that can be denoted as $\operatorname { A c } ( X )$ , for a new variable that is constructed by assigning each of the possible values $x _ { i }$ taken by variable X, the total of previous results. If X is discrete, the value i-th of the variable $\operatorname { A c } ( X )$ is defined as

$$
\operatorname{Ac} \left(x _ {i}\right) = \sum_ {j = 1} ^ {i} x _ {j} \quad \forall x _ {i} \in X.\tag{8}
$$

If the variable $X$ is continuous with values in the interval $[ a , b ]$ , it is represented by function $x ( t ) ;$ ; the variable $\operatorname { A c } ( X )$ at a point $x _ { i } \in [ a , b ]$ is defined:

$$
\operatorname{Ac} (x _ {i}) = \int_ {a} ^ {x _ {i}} x (t) \mathrm{d} t \quad \forall x _ {i} \in [ a, b ].\tag{9}
$$

Given a problem E and a plan $p ( t )$ the functions Ob and Rc accumulated from the objectives and costs of the plan (10) can be constructed. For all time points $t _ { i }$ two variables can be associated:

$$
\operatorname{Ob} \left(t _ {i}\right) = \int_ {a} ^ {t _ {a}} O (t) \mathrm{d} t \operatorname{Rc} \left(t _ {i}\right) = \int_ {a} ^ {t _ {i}} R (t) \mathrm{d} t.\tag{10}
$$

This allows us to construct a planning space (or space representing the environment for planning problems) as a vectorial hyper dimensional space where each axis represents the accumulative variable associated with each objective and resource. The planning space, defined in this way, conforms to the following properties:

1. The representations of the plans within the planning space are always monotonously growing functions. Given that Ob(t) and $\operatorname { R c } ( t )$ are functions defined as positive, function $p ( t )$ expressed at these coordinates is constant or growing.

2. In the planning space, the straight lines represent plans of constant efficiency. If the representations of the plans are straight lines, the slope of the function is constant, and coincides with the definition of the efficiency of the plan.

$$
\frac {\mathrm{d}}{\mathrm{d} t} p t = \operatorname{cte} \Longleftrightarrow \lim _ {\Delta \rightarrow 0} \frac {\Delta O (t)}{\Delta R (t)} = \operatorname{cte}.\tag{11}
$$

In an n-dimensional space, the extension of the straight concept line is called a geodesic curve. In this sense the notion of geodesic plans can be introduced, defined as those that maintain efficiency at a constant throughout their development.

The concept of a geodesic plan can be better understood through the idea of a “plan of minimum $r i s k ^ { \ast }$ . Given a problem, the agent must search for the plan that determines a solution with a series of restrictions $F ( O ; R ) { = } 0$ . In the plans base those plans that are initially compatible with the problem faced by the agent, with the requirements imposed on the solution according to the desires, and in the current state [1] are sought. If all the possible plans $\{ p _ { 1 } , . . . , p _ { n } \}$ are represented within the planning space, a subset of states that the agent has already attained in the past will be obtained in order to resolve similar problems.

With the mesh of points obtained (generally irregular) within the planning space and using interpolation techniques, a working hyper plan $h ( x )$ (that encapsulates the information on the set of restrictions from restored experiences, giving place by definition to an hyper plan due to verifies $h ( x _ { j } ) { = } p _ { j } j { = } 1 , . . . , n$ and the planning space is the dimension n) can be obtained, from which geodesic plans can be calculated and with which variation calculation is applied. Suppose, for simplicity's sake, a planning space of dimension 3 with coordinates $\{ O , R _ { 1 } ,$ $R _ { 2 } \}$ . Between the point $e _ { 0 }$ and the objective points $f _ { \mathrm { s } } f \mathrm { = } \{ e _ { 1 }$ $\cdots ^  e _ { m } \}$ and over the interpolation surface $h ( x )$ , the Euler Theorem [8] guarantees that the expression of the geodesic plans will be obtained by resolving the system of equations in Eq. (12):

$$
\left\{ \begin{array}{l} \frac {\partial L}{\partial R _ {1}} - \frac {\mathrm{d}}{\mathrm{d} O} \frac {\partial L}{\partial R _ {1} ^ {\prime}} = 0 \\ \frac {\partial L}{\partial R _ {2}} - \frac {\mathrm{d}}{\mathrm{d} O} \frac {\partial L}{\partial R _ {2} ^ {\prime}} = 0 \end{array} . \right.\tag{12}
$$

Where $R _ { i }$ is the function accumulated $R , ~ O$ is the function of accumulated O and L is the distance function on the hyper plan h(x),

$$
L = \int_ {h} \mathrm{d} l.\tag{13}
$$

In order to obtain all the geodesic plans that, on the surface $h ( x )$ and beginning at $e _ { 0 } ,$ allow us to reach any of the points $e ^ { * } \in f _ { \mathrm { s } } f$ , a condition of the surrounding must be imposed: the initial point will be $e _ { 0 } { = } ( O _ { 0 } { , } R _ { 0 } )$

Using variation techniques expressions for all the geodesic plans that, beginning at $e _ { 0 }$ allow us to attain the desired point are obtained. Once plans have been obtained that will create efficient solutions between the current state and the set of solution states, we will be able to calculate the plan around it (along its trajectory) by a denser distribution of geodesic plans (a greater number of geodesic plans in its environment). The tool that allows us to determine this is called the minimum Jacobi field associated with the solution set. $g _ { 0 } { : } [ 0 , 1 ] \to S$ be a geodesic over a surface S. Let $h { : } [ 0 , 1 ] x [ - \varepsilon , \varepsilon ] \to S$ be a variation of $g _ { 0 }$ so that for each $t \in ( - \varepsilon , \varepsilon )$ , the set $\{ h _ { t } ( s ) \} _ { t \in ( - \varepsilon , \varepsilon ) } : h _ { t } ( s )$ for all $t \in ( - \varepsilon , \varepsilon )$ <sup>ð- ; Þ f ð Þg ð- ; Þ</sup>are geodesic in S and they begin at $g _ { 0 } ( 0 )$ <sup>ð- ; Þ</sup>in other words, they conform to $h _ { t } ( 0 ) { = } g _ { 0 } ( 0 )$ for all $t \in ( - \varepsilon , \varepsilon )$ . In these conditions, taking the variations to a differential limit, the Eq. (14) is obtained:

$$
\begin{array}{c} \lim _ {t \to 0} \{h _ {t} (s) = g _ {0} (s + t) = \lim _ {t \to 0} h (s, t) \} = \frac {\partial g _ {0}}{\partial t} | _ {s, 0} \\ = \frac {\mathrm{d} g _ {0}}{\mathrm{d} s} \equiv J _ {g 0} (s). \end{array}\tag{14}
$$

The term $J _ { g 0 } ( s )$ is given to the Jacobi Field of the geodesic $g _ { 0 }$ for the set $\{ g _ { n } ( x ) \} _ { n \in N } ,$ , and in the same way <sup>fgnðxÞgn N</sup>that the definition has been constructed, it is possible to give a measurement for the distribution of the other geodesics of $\{ g _ { n } ( x ) \} _ { n \in N }$ around $g _ { 0 }$ throughout the trajectory. Given a set of geodesics, some of them are always $g ^ { * }$ that, in their environment, have a greater distribution than other geodesics in a neighbouring environment. This is equivalent to say that it presents a variation in the distribution of geodesics lower than the others and therefore the Jacobi Field associated with $\{ g _ { n } ( x ) \} _ { n \in N }$ reaches its lowest value at $J _ { g ^ { * } }$

<sup>ð Þg</sup>Let's return to the problem of identifying the most replan-able intention, following the recuperation and variation calculation phase, contains a set of geodesic plans $\{ p _ { 1 } , . . . , p _ { n } \}$ . If the $p ^ { * }$ is selected with a minimum Jacobi Field value, it can be guaranteed that in the event of interruption it will have around it a greater number of geodesic plans in order to continue. This suggests that given a problem with certain restrictions $F ( O ; R ) = 0$ , the geodesic plan $p *$ with minimum associated Jacobi field associated with the set $\{ g _ { n } ( x ) \} _ { n \in N }$ is called the most re-<sup>f ð Þg</sup>plan-able solution. The behaviour model G for the CBP– BDI agent is Eq. (15).

$$
G (e _ {0}, p _ {1}, \dots , p _ {n}) = p ^ {*} \Longleftrightarrow \exists_ {n \in} N / J _ {g _ {n}} \equiv J _ {g ^ {*}} = \underset {n \in N} {\operatorname{Min}} J _ {g _ {n}}.\tag{15}
$$

If the plan $p *$ is not interrupted, the agent will reach a desired state $e _ { j } { \equiv } e ^ { { \bf * } } { \in } f _ { \mathrm { s } } f , j { \in } \{ 1 , \dots , m \}$ . In the learning phase, a weighting $w _ { f } ( p )$ <sup>; f ; ; g</sup>is stored. With the updating of weighting $w _ { f } ( p ^ { * } )$ , the planning cycle of the CBP motor is completed.

Let's suppose that the agent has initiated a plan $p ^ { * }$ but at a moment $t > t _ { 0 } ,$ , the plan is interrupted due to a change in the environment. The geodesic planning meets the conditions of the Bellman Principle of Optimality [2], in other words, each on of the plan's parts is partially geodesic between the selected points. This guarantees that $\mathrm { i f } g _ { 0 }$ is geodesic for interrupted $e _ { 0 }$ in $t _ { 1 } ,$ , because $e _ { 0 }$ changes to $e _ { 1 } ,$ , and $g _ { 1 }$ is geodesic to $e _ { 1 }$ that is begun in the state where $g _ { 0 }$ has been interrupted, it follows that: $g { = } g _ { 0 } { + } g _ { 1 }$ is geodesic to $e { = } e _ { 0 } ( t _ { 1 } { - } t _ { 0 } ) { + } e _ { 1 } ( t _ { 2 } { - } t _ { 1 } )$ , the dynamic process follows the CBP cycle recurrently: each time a plan finds itself interrupted; it generates from the state reached so far, the surroundings of the plans from the case base and adjusts them to the new problem. With this it calculates the geodesic plans and selects the one which meets the minimum conditions of the associated Jacobi field.

A minimum global Jacobi field J(t) also meets Bellman's conditions of optimality [2], in other words, a minimum global Jacobi field, must select minimum Jacobi fields “in pieces”.

$$
J _ {\min} (t) = \left\{J _ {\min} \left(t _ {1} - t _ {0}\right), J _ {\min} \left(t _ {2} - t _ {1}\right), \dots , J _ {\min} \left(t _ {n} - t _ {n - 1}\right) \right\}.\tag{16}
$$

If on the one hand, successive Jacobi fields generate one Jacobi field, and on the other hand, minimum Jacobi fields generate a minimum Jacobi field, the MRPI agent that follows a strategy of replanning G(t) as indicated to survive a dynamic environment, it generates a global plan $p ^ { * } ( t )$ that, faced with all possible global plans $\{ p _ { n } ( t ) \} _ { n \in N } ,$ presents a minimum value in its Jacobi field $J _ { g ^ { * } } ( t ) \equiv J _ { p ^ { * } } ( t )$ The AGALZ agent is a CBR–BDI agent that seeks plans in a dynamic environment in execution time.

## 4. ALZ-MAS: a multi-agent environment for the AGALZ agent

The Alzheimer Santísima Trinidad Residence of Salamanca has been interested in improving the services offered to its patients and has collaborated in the development of the technology presented here, providing their know-how and experimenting with the prototype developed. This residence is intended for people over 65 years old, and has the following services and facilities among others: TV room, geriatric bathroom, hairdressing salon, medical service, religious attention, occupational therapy, technical assistance, terrace, garden, laundry service, clothes adjustment, infirmary, reading room, living room, room of visits, cafeteria, social worker, chapel, elevator, customized diet, and multipurpose room.

Fig. 2 shows a diagram of the first floor of the Santísima Trinidad Residence of Salamanca containing the main facility rooms, while all the patients' rooms are located in the second floor. This residence has capacity for 60 patients, an average of 6 nurses, one social worker and 5 more employees with other responsibilities. We selected 30 patients to test the system, so the hardware implemented at the Residence basically consisted of 42 ID door readers (Hitag HT RM401and mobile Work-About Pro RFID), one on each door and elevator, 4 controllers, one at each exit, one in the first floor hall and another in the second floor hall, and 36 bracelets (Sokymat ID Band Unique Q5 with a chip Hitag S 256), one for each patient and the nurses. The ID door readers get the ID number from the bracelets and send the data to the controllers which send a notification to the Manager agent.

![](/api/attachments/B8DR47B7/fulltext/images/2e04fcdd699c159f587090441c375fb8154c1ec2dd8f9bdb9f11700a609c1896.jpg)  
Fig. 2. Sensor positioning in the first floor of the Santísima Trinidad Residence of Salamanca.

The ALZ-MAS multi-agent system is a distributed system of a relatively high dimension, and requires a detailed analysis and design process before its design. We decided to use a combination of Gaia [18] and AUML for the system design, in an attempt to take advantage of both. Through the Gaia analysis, two models are obtained: the role model and the interaction model. Studying the requirements of the problem, five roles have been chosen: the Patient role manages the patient's personal data and behaviour (monitoring, location, daily tasks, and anomalies); the Doctor role treats patients; the Nurse role schedules the nurse's working day obtaining dynamic plans depending on the tasks needed for each assigned patient; the Security role controls the patients' location and manages locks and alarms; and finally, the Manager role manages the medical record database and the doctor–patient and nurse–patient assignment.

As far as an interaction model is concerned, the dependences and relations between roles are described. For the roles involved in the system a number protocols have been considered: request a treatment, inform about monitoring data, inform about care results, request a doctor assignment, request a nurse assignment, inform about assignment, request a patient's daily plan, inform about a patient's daily tasks, request a patient location, inform a nurse about a lock activation, report alarm activation, request doctor situation, doctor reports on his schedule, request a nurse situation, nurse reports situation, patient reports an anomaly, patient reports on personal data and previous medical records. For example, when the nurse wants to know the tasks required for the patient, the Nurse role executes a protocol RequestPatientPlanif through which is able to make a request to the Patient role. The Patient role acts to give a suitable response to the Nurse role and executes the InformPlanif protocol to communicate the planned tasks to the NURSE role.

In the Gaia design process three models are considered: agent model, services model and acquaintance model [18].

To achieve a low level AUML design, with enough details for an implementation to be carried out. The AUML design provides class diagrams for each agent, collaboration or sequence diagrams for each interaction, state and activity diagrams to represent internal states and protocol diagrams to model communicative acts. Some examples of the low level AUML detailed design will be presented in the next section.

The conclusions obtained after the analysis and design process let us conclude that ALZ-MAS is composed of four different types of agent:

Patient agent manages the patient's personal data and behaviour (monitoring, location, daily tasks, and anomalies). Every hour validates the patient location, monitors the patient state and sends a copy of its memory base (patient state, goals and plans) to the manager agent in order to maintain backups. The patient state is instantiated at execution time as a set of beliefs and these beliefs are controlled through goals that must be achieved or maintained. The beliefs that were seen to define a general patient state at the Santísima Trinidad Residence of Salamanca were: weight, temperature, blood pressure, feeding (diet characteristics and next time to eat), oral medication, parenteral medication, posture change, toileting, personal hygiene, and exercise. The beliefs and goals used for every patient depend on the plan (treatment) or plans that the doctors prescribe. The patient agent monitors the patient state by means of the goals. To know if a goal has been achieved or has failed, it is necessary to maintain continuous communication with the rest of the ALZ MAS agents. At least once per day, depending on the corresponding treatment, the patient agent must contact the nurse agent. The patient agent must have periodic communication with the doctor agent. Finally the patient agent must ensure that all the actions indicated in the treatment are taken out.

Manager agent plays two roles the Security role that controls the patients' location and manages locks and alarms; and the Manager role that manages the medical record database and the doctor–patient and nurse–patient assignment. It must provide security for the patients and medical staff and the patients, doctors and nurse assignment must be efficient.

– Doctor AGALZ agent treats patients. The Doctor agent needs to interact with the Patient agent to order a treatment and receive periodic reports, with the Manager agent to consult medical records and assigned patients, and with AGALZ agent to ascertain the patient evolution.

– AGALZ agent schedules also the nurse's working day obtaining dynamic plans depending on the tasks needed for each assigned patient. AGALZ manages nurses' profiles, tasks, available time and resources. The generated plans must guarantee that all the patients assigned to the nurse are given care. The nurse cannot exceed 8 working hours. Every agent generates personalized plans depending on the nurse's profile and working habits.

Manager and Patient agents run in a central computer, but AGALZ agents run on mobile devices, so a robust wireless network has been installed as an extension to the existing wired LAN. With respect to the question of failure recovery, a continuous monitoring of the system is carried out. Every agent saves its memory (personal data) onto a data base. The most sensitive agents are patient agents, so these agents save their state every hour. When an agent fails, another instance can be easily created from the latest backup. The database and server used must have redundancy and failure recovery, so a RAID (Redundant Array of Inexpensive Disks) server is used. In the case of a server failure, an alarm is generated and all the plans and information required for nurses and doctors to carry out their working day are automatically printed. A secure and authenticated access to the patients data is provided. The use of different authorisations for users, logins and passwords, and the encryption of messages using a public key infrastructure and SSL (Secure Socket Layer) have already been implemented. Moreover, the RFID tag only contains the identification number, and not the personal data.

## 5. The AGALZ agents in operation

The objectives of AGALZ agents are: to plan the nurses and doctors working time dynamically, to maintain the standard working reports about their activities, and to guarantee that the patients assigned to the nurses are provided with suitable care. Thus the AGALZ agent schedules the working days obtaining dynamic plans depending on the tasks needed for each assigned patient. As can be seen in Fig. 3, the AGALZ nurse agent has five capabilities and offers three services.

AGALZ implements the reasoning cycle of the CBP system by means of three capabilities: Update, KBase and VCBP (Variational CBP). The Update capability implements the retrieve and retain stages, while the KBase capability implements the reuse stage and the VCBP capability the revise stage, where the nurse opinion is evaluated. The VCBP capability is also in charge of dynamic replanning task. By means of its Give Care capacity, AGALZ supervises each care task and generates the corresponding report. The Consult Nurse Data capability allows AGALZ to execute different queries on stored data.

Given a set of beliefs B compatible with the problem E, it is possible to generate a plan base CBP that contains all the possible plans produced by the combinations of compatible beliefs. The beliefs available for the AGALZ agent are tasks, resources and time.

![](/api/attachments/B8DR47B7/fulltext/images/6d755b3723fc6127c7829360d10eb51e59fe11be3756c1e928380049d775293e.jpg)  
Fig. 3. AGALZ AUML class diagram.

A task is a java object that contains the data of the patient who requested the service, the description of the service and the time limits to carry it out, as can be seen in Table 1. For each task one or more goals are established, in such a way that the whole task is eventually achieved. A goal is also a java object, that identifies what the AGALZ agent wants to achieve (complete a task) and under which conditions (restrictions). For this, a goal can contain parameters and define creation conditions (that allow AGALZ to define the conditions for achieving the goal), context conditions (the conditions that must be fulfilled) or drop conditions. To achieve its objectives each goal triggers plans. A plan is a procedure written in java code. A goal can create new goals (subgoals) to achieve its objectives (for example for the task of rehabilitation AGALZ creates a new goal for each concrete exercise).

The CBP system constructs plans as a sequence of tasks that need to be carried out by a nurse. A description of the problem will be formed by the tasks that the nurse needs to execute, the resources available, and the times assigned for their shift. In the Update stage, the descriptions of similar problems are recovered. In order to do this, the AGALZ agent allows the application of various similar algorithms (cosine, clustering etc.). In this step, those problem descriptions found within a range of similarity close to the original problem description are recovered from the beliefs base. In our case, a tolerance of 20% has been permitted.

Once the most similar problem descriptions have been recovered, the K-Base capability recovers the solutions associated with them. One solution contains all the plans (sequences of tasks) that are carried out in order to achieve the objectives of AGALZ for a problem description (assuming that replanning is possible) in the past, as well as the efficiency of the solution being supplied.

Table 1 Task example

<table><tr><td>Task</td><td>Data</td></tr><tr><td>TaskId</td><td>36</td></tr><tr><td>TaskType</td><td>32</td></tr><tr><td>TaskDescript</td><td>Feeding (lunch)</td></tr><tr><td>TaskPriority</td><td>3</td></tr><tr><td>TaskObjective</td><td>0</td></tr><tr><td>TaskIncidents</td><td>0</td></tr><tr><td>PatientId</td><td>7</td></tr><tr><td>PatientDependence</td><td>2</td></tr><tr><td>MinTime</td><td>12:30</td></tr><tr><td>MaxTime</td><td>15:00</td></tr><tr><td>TaskResources</td><td>Food 1</td></tr></table>

The VCBP capability also combines the recovered solutions, as explained in Section 4, to construct a plan. At this time AGALZ takes control of the processing of the plan (scheduling). The VCBP capability is centered around the objectives and resources needed by each task, as well as on the objectives that the nurse needs to perform and the resources available in order to carry out the global plan. The objectives or global plans that each nurse has are to attend to the patients and not to work for over 8 h. The time available is a problem restriction. This available time will influence the hyper plan of restrictions, specifically, the range of positive values that the z axis takes from this hyper plan. The resources necessary for some of the tasks are food, equipment and rooms. Finally, the VCBP capability takes care of incidents and interruptions that may occur during replanning.

In order to illustrate how the planner works, let's take a significant example. In the first place it is necessary to take into account that each nurse has a different profile according to their qualification and the tasks that they usually carry out. Let $\mathrm { p r } = \mathrm { p r } _ { 1 } , \cdot \cdot \cdot , \mathrm { p r } _ { 1 0 }$ define the stored <sup>¼ ; ;</sup>profiles of the nurses at the residence. It is considered appropriate to manage the profiles of the nurses because there are some nurses who perform tasks with greater skill or who carry out tasks in less time. On the other hand, the AGALZ agent maintains a close relationship with the Manager agent. The Manager agent has as one of its tasks the assignation of nurses to patients and doctors to patients. This assignation is carried out through the CBR reasoning motor of the Manager Agent. When the new assignation of tasks needs to be carried out to the nurses or to the doctors, both past experiences, such as the profile of the nurse or doctor, and the needs of the current situation are retrieved. In this way tasks are allocated to a nurse. These tasks may correspond to the same patient or to a number of patients. Moreover, as mentioned above, the profile of each nurse is taken into account. For example, not all nurses are equally qualified for rehabilitation. If one nurse is more qualified in the area, she will be allocated the patients whose need for rehabilitation is greater, always taking into account that the nurse cannot work more than 8 h, so that the number of patients assigned depends on the time needed to carry out the rehabilitation. The Manager agent takes into account how those patients who receive rehabilitation are improving, the arrival of new patients, holiday rotas etc. As such, the allocation of tasks needs to be set on a daily basis.

Secondly, it is necessary to store within the beliefs base the time that each task takes, described as $t _ { j } = \mathrm { M a x } _ { j , k } \{ t _ { j k } ^ { i } \}$ , where j indicates the type of task, k, the nurse with the most suitable profile to carry it out (since it is only possible to assign on each task type to the nurses who are qualified to carry it out) and $i ,$ the patient that requires the task.

Once the assignation of tasks to a nurse has been completed, the assignation is communicated to the corresponding AGALZ agent. From this moment on, the planning process begins. The AGALZ agent must take into account the time that nurse has available and the time required for each task. Moreover, the resources available and the location of the patients involved are also taken into account. In order to make a plan, the cases with a similar problem are recovered from the beliefs base and solutions (plans) that were used to resolve them are combined.

A large quantity of measurements have be taken in order to standardise the time taken to arrive at a given room, or to take a patient from one room to another (depending on the level of dependence of the patient). These times are included directly in the time assigned for each task.

The location of the patients is a factor which significantly influences the decision as to whether a plan should be interrupted. For example, in the case that a nurse should go to a given room to take dinner to the patient and the patient is actually in a different room, the nurses plan will need to be interrupted. As mentioned above, the location of the patients within the hospital is defined through a reference system in $\Re ^ { 2 }$ . In the location system, it is fundamental that RFID devices are used. These devices make it possible to rapidly assess the possibility or need to replan.

A plan can be interrupted for different reasons. Those which have been taken into account within the residence are: that a resource fails, that a patient suffers some sort of crisis and requires unforeseen attention, that the patient has an unexpected visit or that visits to the patient have gone on over the permitted time allowed and an emergency situation. If the planner finds itself in a situation where the plan is interrupted, it rejects the initial plan and seeks an alternative one. The first thing that needs to change is the task order, attempting to maintain the assignation originally allocated by the Manager agent. The new plan must meet the initial objectives. In the event that this is impossible, the nurses will need to be reassigned. This reassignment will attempt to limit changes to a minimum. For reassignment it is necessary to take into account the tasks that were assigned to the nurses, the development of the plans (which tasks have been carried out and which still need to be done) and the profiles of the nurses (prioritising preparation for the task that cannot be covered). The nurse who is assigned the task should replan in order to include the new task. In the event that the replanning is positive (the tasks that still need to be done and the new task can be carried out) the process is complete. If the replanning is negative, the next nurse down in the ranking will be used.

Lastly, depending on the efficiency of the plan, it will be stored together with its level of efficiency within the beliefs base. In the paragraphs below, we give a specific example in detail.

Let $E ^ { i } = \{ e _ { 0 } ^ { i } , \cdot \cdot \cdot , e _ { h } ^ { i } \}$ the task carried out on patient i, <sup>¼ f ; ; g</sup>put in order of priority. We have the following problem $E = \cup _ { i } E ^ { i } = \left\{ e _ { 0 } , \cdot \cdot \cdot , e _ { n } \right\}$ , that is updated on a daily <sup>¼ [ ¼ f ; ; g</sup>basis, where E denotes the complete set of tasks being carried out and therefore has no superscript.

Selecting a nurse $k \in \{ 1 , \cdots , \ 1 0 \}$ at random (in particular, k = 3), it has been shown that the assignation of tasks according to the profile was:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
- Take patient 2 to the toilet $\equiv e_1^2$; $t_1 = 30$ min.
- Wash patient $2 \equiv e_3^2$; $t_1 = 30$ min.
- Give patient 2 their breakfast $\equiv e_2^2$, $t_2 = 20$ min.
- Give patents 4, 5 and 6 rehabilitation $e_4^5$, $e_5^5$, $ye_5^6$; $t_5 = 90$ min.
- Check weight, blood pressure etc. of patient $6 \equiv e_0^6$; $t_0 = 60$ min.
- Wash patient $5 \equiv \frac{5}{3}$; $t_3 = 30$ min.
- Check weight, blood pressure etc. of patient $5 \equiv e_0^5$; $t_0 = 60$ min.
</div>

Calculation of the tasks assigned verifies that the total time allocated does not go over 8 h. As may be noted, when the tasks are being assigned, the location of the patients is not taken into account (the patients are given the best treatment possible). But the location of the patients is taken into account when the plan is generated (in order to minimise the total time taken to carry out the tasks).

Once the assignation of tasks is complete, each ALGALZ agent carries out a plan for its nurse. They retrieve similar assignations from the beliefs base, and the corresponding plans that were used. A plan is made and supplied to the nurse. The nurse then carries out the plan in sections, in other words, task by task (The current task is shown in the PDA and the nurse has to introduce the result obtained after the task has been accomplished). Each task has a series of objectives which must be reached for the part of the plan to have been completed successfully. In order to carry out each task the nurse must have a number of resources available. For example, the task “Check weight, blood pressure etc.” corresponds to the objective “checking health of patien ${ \bf \vec { \tau } } ^ { > } \equiv { \cal O } _ { 0 } ;$ the tasks “Take patient to the toilet” and “wash patient” corresponds to the objective of appearance and physical well-bein $\mathrm { g } \equiv O _ { 1 , 3 }$ and breakfast, lunch, tea and dinner correspond to the objective, physical recuperation $\equiv O _ { 2 , 4 , 6 , 7 }$ (task 2 indicates breakfast, task 4 indicates lunch, task 6 indicates tea, and 7 indicates dinner). The coding used for resources is similar. It has been decided that the objectives and resources variables should be dichotomic (binary) with a value of 0 to 1 in order to indicate the absence or presence of a resource or objective and to be represented in Fig. 4a. Value 1 indicates that this resource is needed or that this is the objective to be reached, while zero denotes the contrary.

Fig. 4a shows the representation of a space $\Re ^ { 3 }$ for tasks according to the following three coordinates: time, number of objectives achieved, and number of resources used (coordinates taken from similar cases recalled). Specifically, Fig. 4a shows a hyper plan of restrictions and the plan followed for a case retrieved from the beliefs base, considered to be similar. So that Fig. 4a isn't overly large, and in order for the plan to be appreciated at first glance, the time axis has been rescaled (axis z), establishing an isomorphism between the intervals [0.1] and [0.8]:

![](/api/attachments/B8DR47B7/fulltext/images/ebeac2c8b5a08c22a0571f883e02b8ac69d4db7e8793b209a10a59e85b840543.jpg)

![](/api/attachments/B8DR47B7/fulltext/images/3f69216a3d099142c6d718333ed9d3f950db0044ee5a4ca1a8857f2d4f4b78c9.jpg)  
Fig. 4. Hyperplan of restrictions. a) Hyperplan together with the corresponding plan. b) Selection of the most replannable plan.

The isomorphism is as follows:

$$
\begin{array}{l} \lambda : [ 0, 1 ] \to [ 0, 8 ] \\ z \to \lambda (z) = 8 z \end{array}\tag{17}
$$

For other similar retrieved cases, the same procedure is followed. The new plan is made in such a way that the planner proposes the plan in sections, with the greatest density of plans around it (reflected by formulae (15) and (16)). In short, from the tasks that the nurse needs to carry out for one or several patients, the most similar cases (from past experiences) are retrieved from the beliefs base. Below, the hyper plan and the plan carried out are shown. In order to understand the graphical representation, given that the plans are made in sections, we focus on one initial task $e _ { 0 }$ and a final task $e _ { 5 }$ on the same or a different patient. Between the initial and the final task the nurse could carry out other tasks (that involves the same patients as those corresponding to tasks $e _ { 0 }$ and $e _ { 5 }$ or that implicate other patients). The idea that the planner presents is to choose as the optimal solution the plan that has the most plans around it, involving these two fixed tasks on the patient/s assigned, (independently of whether or not it includes other tasks for other patients, if the task is for a patient that hasn't been assigned to the nurse, they are not carried out, but in this way, it also allows the intersection of tasks on other patients):

In this way, as can be seen in Fig. 4b, the plan chosen is the one represented by a discontinuous line since it represents the plan that has most other plans around it and involves other tasks that could be assigned in the case of interruptions. In the example, the plan proposed was:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
- Take patient 2 to the toilet $\equiv e_1^2$; $t_1 = 30$ min.
- Wash patient $2 \equiv e_3^2$; $t_3 = 30$ min.
- Give patient 2 breakfast $\equiv e_2^2$, $t_2 = 20$ min.
- Give rehabilitation to patients 4 and $5 \equiv e_5^4 y e_5^5$; $t_5 = 90$ min.
- Check patient 5's weight, blood pressure etc. $\equiv e_0^5$; $t_0 = 60$ min.
- Wash patient $5 \equiv e_3^5$; $t_3 = 30$ min.
- Give rehabilitation to patient $6 \equiv e_5^6$; $t_5 = 90$ min
- Check patient 6's weight, blood pressure etc. $\equiv e_0^6$; $t_0 = 60$ min.
</div>

During the experiment, patient 5 suffered a crisis and needed to be attended to by the doctor. The nurse chosen was giving rehabilitation to patient 4 at the time. Once they had finished, patient 5 was still being attended by the doctor (ascertained by the location of the patient and the doctor), the time taken to attend to such a crisis is stored in the beliefs base.

The replanning applied took into account the tasks that still needed to be done and the time considered necessary for attending the crisis. In this way the planner proceeded to reorganise and replan the plan as follows:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
- Give rehabilitation to $4 \equiv e_5^4$; $t_5 = 90$ min.
- Give rehabilitation to $6 \equiv e_5^6$; $t_5 = 90$ min.
- Check patient 6's weight, blood pressure etc. $\equiv e_0^6$; $t_0 = 60$ min.
- Check patient 5's weight, blood pressure etc. $\equiv e_0^5$; $t_0 = 60$ min.
- Give rehabilitation to $5 \equiv e_5^5$; $t_5 = 90$ min.
- Wash patient $5 \equiv e_3^5$; $t_3 = 30$ min.
</div>

In the example presented, it has been possible to replan. In the event that it had been impossible to reorganise the tasks that remained, communication would be made with the Manager agent. The Manager agent would need to reassign the tasks according to the level of expertise of the nurses.

The mathematical calculations for obtaining h(x), through Duchon techniques, the set of geodesics $\{ g _ { n } ( x ) \} _ { n \in N }$ through the resolution of the Euler and transversability equations, or for obtaining the Jacobi field, are carried out using the programme ®Mathematica 5.1 and the libraries Jspline+ and Jlink for java.

## 6. Results and conclusions

The ALZ-MAS system, incorporating AGALZ agents, has been tested over the last few months. During the testing period the system usefulness has been evaluated from different points of view. Fig. 5 shows the average number of nurses working simultaneously (each of the 24 h of the day) at the Residence before and after the implantation of the system prototype, with data collected from October 2005 to March 2006. The prototype was adopted on January 15th, 2006. The average number of patients was the same before and after the implementation. To test the system 30 patient agents, 10 AGALZ nurse agents, 2 doctor agents and 1 manager agent were instantiated. In the tests related to the frame of this research we have focused on the AGALZ nurse agents, while the doctor agents do not have planning capabilities incorporated within them as yet. As can be seen in Fig. 5, the dark-blue area represents the average number of nurses required in the residence each hour of a day without the ALZ-MAS. The light-blue area represents the same measure but after the implementation of the ALZ-MAS. As can be seen, the ALZ-MAS helps the nurses to gain time, which can be dedicated to the care of special patients, to learn or to prepare new activities. The time spent on supervision and control tasks has been reduced substantially, as well as the time spent attending false alarms, while the time for direct patient care has been increased.

![](/api/attachments/B8DR47B7/fulltext/images/676ec97c3b982f78c7bea9c280478ab983746f81227e6594273844c1fc714b93.jpg)  
Fig. 5. Number of nurses working simultaneously. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

The tasks executed by nurses were divided in two categories, direct action tasks and indirect action tasks. Direct action tasks are those which require the nurse acting directly on the patient during the whole task (medication, posture change, toileting, feeding, etc.). In the indirect action tasks the nurses do not need to act directly on the patients all the time (reports, monitoring, visits). AGALZ agents can take care of some of these indirect actions, so nurses can dedicate more time to personal patients care. During the first testing period the problem was analysed and data was collected. The average time spent by nurses carrying out their duties with a given patient was obtained, having into account the patient type, its dependency level and the nurse professional level. For the direct action tasks, the following times were obtained for each patient: 35 min cleaning, 18 min feeding, 8 min oral medication, 30 min parenteral medication, 25 min posture change, 8 min toileting, 60 min exercise and 10 min others for patients with a dependence degree of 1; and 45 min cleaning, 28 min feeding, 11 min oral medication, 42 min parenteral medication, 50 min posture change, 30 min toileting, 90 min exercise and 10 min others for patients with a dependence degree of 2. We are especially interested on time spent on indirect tasks; daily times obtained before and after the implementation for each task can be seen on Table 2. Table 2 shows how the implementation of the ALZ-MAS reduces the time spent on indirect task. For example, the average number of minutes spent by a nurse on monitoring patients has been reduced from 167 daily minutes to 105 daily minutes without reducing the care level and the patients safety.

Table 2  
Time (min) spent on indirect tasks

<table><tr><td></td><td>Monitoring</td><td>Reports</td><td>Visits</td><td>Other</td><td>Total</td></tr><tr><td>Before</td><td>167</td><td>48</td><td>73</td><td>82</td><td>370</td></tr><tr><td>After</td><td>105</td><td>40</td><td>45</td><td>60</td><td>250</td></tr></table>

Some authors such as Langer [10] have studied the role of the mindfulness in treating elderly people. During this research project we have been trying to construct a patient-centered social system. Both AGALZ and ALZ-MAS have been designed and developed from the perspective of the patients and the relationship established between the patients and staff. One of the main contributions of this paper is a dynamic planning mechanism which allows replanning in execution time, which in turn improves patient care. The system also facilitates the more flexible assignation of the working shifts at the residence; since the workers have reduced the time spent on routine tasks and can assign this time to extra activities, such as exercising the patients, learning, carrying out leisure activities or just talking with the patients or with their families. Their work is automatically monitored, as well as the patients' activities. The stored information may be analysed with knowledge discovery techniques and may help to improve the quality of life for the patients and the efficiency of the center. The security of the center has also been improved in three ways: the system monitors the patients and guarantees that each one of them is in the right place; secondly, only authorised personnel can gain access to the residence protected areas, and thirdly, the information is stored in a more secure way using redundance and generating continuous backups. The access to information has been protected in order to guarantee confidentiality.

We had certain problems implementing the system, partly because the nurses and workers were not familiar with the use of PDA devices, so some courses were given to introduce them to these technologies and teach them how to use the system interface. After that and with some difficulties with the installation of the wireless access points (with the propagation of the signal) and the collocation of the RFID door readers, the system was running smoothly, with only minor problems.

Table 3  
Efficiency and quality of the CBP engine

<table><tr><td>Strategy</td><td colspan="3">Typical case</td><td colspan="2">Quality</td></tr><tr><td> $Ce_{t}$ </td><td> $n_{c}$ </td><td> $e_{fo}$ </td><td> $e_{ffr}$ </td><td> $e_{ffr}$ </td><td> $Ce_{0.2}$ </td></tr><tr><td>94</td><td>12</td><td>0.47</td><td>0.69</td><td>0.05</td><td>30</td></tr></table>

The CBP–BDI architecture of the AGALZ gents presented in this paper solves one of the problems of BDI (deliberative) architectures, which is the lack of learning capacity. Table 3 shows achieved objectives vs. Possible objectives (efficacy: $e _ { \mathrm { f o } } ) ;$ objectives reached vs. Resources used (efficiency: e ); number of actions or beliefs used (plan stages: $n _ { \mathrm { c } } ) ;$ efficiency of the plan in terms of the number of stages (e ); percentage of cases that reach a solution state vs. the total number (Ce ) and percentage of successful cases that reach values within the top 20% $\displaystyle \left( \mathrm { C e } _ { 0 . 2 } \right)$ . The agent improves its learning as the CBP system comes into play. The number of interruptions for replanning is notable reduced. It also reduces the gap that exists between the formalization and the implementation of BDI agents. The reasoning cycle of the CBR systems helps the agents to solve problems, to adapt to changes in the environment, and to identify new possible solutions. In order to evaluate the learning capacity of the AGALZ agents, the quality of the plans has been measured. The number of interruptions indicates the number of replannings carried out up to the completion of a plan. As previously explained in Section 2, AGALZ executes CBP cycles in order to learn. After the AGALZ agent executes 100 plans it reduces the number of interruptions, at an average of 30%. The average number of interruptions is of 9 times, per day, after ten executed plans, around 8 times after executing 50 plans and around 7 times after executing 100 plans. The results obtained lead us to conclude that AGALZ improves its behaviour with learning, and that the number of interruptions does not decrease by more than 7 per day, on average.

In the future, health care for Alzheimer's patients, the elderly and people with other disabilities will require the use of new technologies that allow medical personnel to carry out their tasks more efficiently. Weick [17] describes the fundamental problems of knowledge transfer and sense making in digital/computer based environments. We have shown the potential of deliberative AGALZ agents in a distributed multi-agent system focused on health care, providing a way to respond to some challenges of health care, related for example to the identification, control and health care planning. In addition, the use of RFID technology on people provides a high level of interaction among users and patients through the system and is fundamental in the construction of the intelligent environment. Furthermore, the use of mobile devices, when used well, can facilitate social interactions and knowledge transfer.

## Acknowledgements

This work has been partially supported by the MCYT TIC2003-07369-C02-02 and the JCYL-2002- 05 project SA104A05. Special thanks to Sokymat by the RFID technology provided and to Telefónica Móviles (Movistar) for the wireless devices donated.

## References

[1] A. Aamodt, E. Plaza, Case-based reasoning: foundational issues, methodological variations, and system approaches, AI Communications 7 (1994) 39–59.

[2] R.E. Bellman, Dynamic Programming, Princeton University Press, Princeton, NJ, 1957.

[3] M.E. Bratman, Intentions, Plans and Practical Reason, Harvard University Press, Cambridge, MA, 1987.

[4] L. Camarinha-Matos, H. Afsarmanesh, Design of a virtual community infrastructure for elderly care, in: L.M. Camarinha-Matos (Ed.), Proceedings of PRO-VE'02, Sesimbra, Portugal, 2002.

[5] J.M. Corchado, R. Laza, Constructing deliberative agents with case-based reasoning technology, International Journal of Intelligent Systems 18 (2003) 1227–1241.

[6] K. Decker, J. Li, Coordinated hospital patient scheduling, in: Y. Demazeau (Ed.), Proceedings of ICMAS98, Paris, France, 1998, pp. 104–111.

[7] D. Foster, C. McGregor, S. El-Masri., A survey of agent-based intelligent decision support systems to support clinical management and research, in: G. Armano, E. Merelli, J. Denzinger, A. Martin, S. Miles, H. Tianfield, R. Unland (Eds.), Proceedings of MAS<sup>⁎</sup>BIOMED'05, Utretch, Netherlands, 2005.

[8] M. Glez-Bedia, J.M. Corchado, A planning strategy based on variational calculus for deliberative agents, Computing and Information Systems Journal 10 (1) (2002) 2–14.

[9] L.T. Kohn, J.M. Corrigan, Donaldson, To Err is Human: Building a Safer Health System, Committee on Quality of Health Care in America Institute of Medicine, National Academy Press, Washington, DC, 1999.

[10] E.J. Langer, Mindfulness, Perseus Books, 1989.

[11] G. Lanzola, L. Gatti, S. Falasconi, M. Stefanelli, A framework for building cooperative software agents in medical applications, Artificial Intelligence in Medicine 16 (3) (1999) 223–249.

[12] T.R. McLean, Crossing the quality of chasm: a new health system for the 1st century, Health Matrix 12 (2002) 239–295.

[13] J.A. Meunier, A virtual machine for a functional mobile agent architecture supporting distributed medical information, in: I.E. E.E Computer Society (Ed.), Proceedings of CBMS '99, Washington, DC, USA, 1999.

[14] S. Miksch, K. Cheng, B. Hayes-Roth, An intelligent assistant for patient health care, Proceedings of Agents'97, ACM Press, New York, 1997, pp. 458–465).

[15] J. Nealon, A. Moreno, Applications of Software Agent Technology in the Health Care domain, Birkhauser, Whitestein series in Software Agent Technologies, 2003.

[16] Sokymat, http://www.sokymat.com2006.

[17] K.E. Weick, Cosmos vs. chaos: sense and nonsense in electronic contexts, in: R.L. Ruggles (Ed.), Knowledge Management Tools, vol. 3, 1985.

[18] M. Wooldridge, N.R. Jennings, D. Kinny, The gaia methodology for agent-oriented analysis and design, Journal of Autonomous Agents and Multi-Agent Systems 3 (3) (2000) 285–312.

Juan M. Corchado (PhD.). Received a PhD. in Computer Science from the University of Salamanca in 1998 and a PhD. in Artificial Intelligence (AI) from the University of Paisley, Glasgow (UK) in 2000. At present he is an Associate Professor, Director of the Intelligent Information System Group (http://bisite.usal.es) and Director of the MSc programs in Computer Science at the University of Salamanca (Spain), previously he was a sub-director of the Computer Science School at the University of Vigo (Spain, 1999–00) and Researcher at the University of Paisley (UK, 1995–98). He has been a research collaborator with the Plymouth Marine Laboratory (UK) since 1993. He has led several Artificial Intelligence research projects sponsored by the Spanish and European public and private institutions and has supervised seven PhD. students. He is the co-author of over 130 books, book chapters, journal papers, technical reports, etc. published by organisations such as Elsevier, IEEE, IEE, ACM, AAAI, Springer Verlag, Morgan Kaufmann, etc., most of these present practical and theoretical achievements of hybrid AI and distributed systems. He has been the President of the organising and scientific committee of several international symposiums.

Javier Bajo (PhD. Student). At present he is an Assistant Professor at the University of Salamanca (Spain). He obtained an Information Technology degree at the University of Valladolid (Spain) in 2001 and an Engineering in Computer Sciences degree at the Pontifical University of Salamanca in 2003. He has been a member of the organising and scientific committee of several international symposiums such as CAEPIA, IDEAL, HAIS, etc. and co-author of papers published in recognized journal, workshops and symposiums.

Dante Tapia (PhD. Student). At present he is a PhD. student at the University of Salamanca (Spain) under the supervision of Dr. Juan M. Corchado. He obtained an Engineering in Computer Sciences degree in 2001 and an MSc in Telematics at the University of Colima (Mexico) in 2004. He has been involved in the development of automated systems in the Faculty of Telematics at the University of Colima and deeply collaborating with the Government of the State, where he obtained a scholarship to complete his academic formation. He has also been a coauthor of papers published in recognized workshops and symposiums.

Yanira de Paz (PhD. Student). At present she holds a scholarship provided by the Spanish Minister of Education to complete a PhD. program at the University of Salamanca (Spain). She obtained a Mathematics degree in 2002 and a Statistic degree in 2003 at the University of Salamanca (Spain). She is an Assistant Professor at the Faculty of Economy at the University of Salamanca and co-author of several mathematical and statistical books. She has also been a lecturer in the Faculty of Mathematics at the Complutense University of Madrid.

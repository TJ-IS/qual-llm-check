---
otero_id: 7820
otero_key: "DH57M7RY"
title: "Conceptual modeling for simulation-based serious gaming"
authors: "Durk-Jouke van der Zee; Bart Holkenborg; Stewart Robinson"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.03.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Conceptual modeling for simulation-based serious gaming

Durk-Jouke van der Zee <sup>a,</sup>⁎, Bart Holkenborg <sup>b</sup>, Stewart Robinson <sup>c</sup>

<sup>a</sup> Faculty of Economics & Business, University of Groningen, P.O. Box 800, 9700 AV, Groningen, The Netherlands

<sup>b</sup> Topicus FINAN, Financial Analysis, Koggelaan 5-D, 8017 JH, Zwolle, The Netherlands

<sup>c</sup> School of Business and Economics, Loughborough University, Loughborough, LE11 3TU 7AL, United Kingdom

## a r t i c l e i n f o

Article history: Received 25 May 2011 Received in revised form 13 December 2011 Accepted 19 March 2012 Available online 29 March 2012

Keywords: Serious gaming Discrete event simulation Conceptual modeling Operations management Education Training

## a b s t r a c t

In recent years many simulation-based serious games have been developed for supporting (future) managers in operations management decision making. They illustrate the high potential of using discrete event simulation for pedagogical purposes. Unfortunately, this potential does not seem to go together with the availability of guidance for the game designer on the use of simulation. In response, we propose a conceptual modeling framework for simulation-based serious gaming It structures the conceptual modeling process by identifving five key modeling activities in de<sup>fi</sup>ning a conceptual model, i.e., a blue print for model coding. Activities aim to explore the learning environment, and capture modeling objectives, and model inputs, outputs and contents. Each activity is further detailed in terms of steps to undertake, good practices, and supportive methods. Use of the framework is illustrated by a case example concerning education of retail managers on inventory control.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Many researchers indicate the high potential of serious games for acquiring decision making skills in operations management, see, for example, Chapman and Martin [10], Ruohomaki [48], Chwif and Barretto [11], Smeds [52], Lainema and Hilmola [32], Lewis and Maylor [34]. Essential strengths of gaming are in the active involvement of trainees, the possibility to experience the topic as a whole, and its suitability to convey system characteristics [7,17,20]. These characteristics give it a decisive advantage over conventional lecturing. Furthermore, factors such as visibility, reproducibility, safety, economy, and system availability make gaming a viable alternative for training-on-the-job [42,48].

In this article we address the design of computer-based serious games for supporting decision making in operations management. Note how we use the adjective “serious” to stress the learning objective underlying the game [15]. For example, serious games are helpful in preparing students for their future role as decision makers on companies' production and logistic systems [32,34]. Also, they may support current operations managers in learning how to make better decisions through experimenting within a safe learning environment [9,25]. Some illustrative examples of serious games concern the design and control of a manufacturing system [5], effective use of enterprise resource planning systems [1], con<sup>fi</sup>guration of emergency departments [27], and operational supply chain management [64].

Discrete event simulation is a natural concept for computer-based modeling of operations systems, due to the ef<sup>fi</sup>ciency of its eventbased time mechanism, and its allowance for uncertainties in operation's timing and outcomes [33]. In recognition of this fact, many simulation software tools are developed offering extensive libraries of tailored building blocks, ef<sup>fi</sup>ciently facilitating systems modeling and visualization. So far, the main use of discrete event simulation concerns logistic analysis of operations systems. However, several authors report successful use of discrete event simulation for gaming purposes, see for example, Belton and Elder [6], Adelsberger et al. [1], Chwif and Barretto [11], Hieber and Hartel [23], Mayer et al. [35], Lainema and Hilmola [32], Van Houten et al. [64], Jain and McLean [27], Battini et al. [5].

Potential and interest for simulation-based serious gaming makes guidance for the game designer in specifying, coding and using simulation models a relevant issue. Here our prime focus is on model speci<sup>fi</sup>- cation or conceptual modeling. Conceptual modeling is meant to establish the intended use of a model and the model elements. A good quality conceptual model suggests a well-informed interpreting of stakeholders' needs and requirements, and project efforts that do not violate restrictions on budget, resources and time [21,45]. Clearly, the qualities of a conceptual model have great impact on the success of simulation work. This implies a real need for guidance for the modeler, in (mastering) his/her creative efforts, as well as sharing them with stakeholders.

Conceptual modeling is well-integrated in game design methodology, see, for example, Greenblat and Duke [21] and Greenblat [20]. However, we found that the current methodology tends to neglect the speci<sup>fi</sup>cs of discrete event simulation. Hence it is up to the designer to identify and exploit the strengths of discrete event simulation, and to cope with its weaknesses. Here discrete event simulation's basic strengths follow from its choice of time concept, the notion of variability in a system's operations, and the availability of tools offering building blocks that map real-world entities in an ef<sup>fi</sup>cient and realistic way. Weaknesses follow from the “analysis perspective” dominating current use of discrete event simulation. Simulation literature and tools tend not to take a pedagogic perspective in model set-up. They have no notion of players or their interaction with the model [32,54,60].

In response to the observed lack of guidance in simulation-based serious game design we propose a conceptual modeling framework. Essentially, it suggests a step-wise approach for specifying the simulation model facilitating the game, and introduces the means to do so. Ideally, both model effectiveness and modeling ef<sup>fi</sup>ciency may bene<sup>fi</sup>t from such a structured approach. Hence the potential of games for supporting decision making in operations management may be increased. The proposed framework results from modi<sup>fi</sup>cations and extensions of the conceptual modeling framework described in Robinson [46]. Changes to the framework re<sup>fl</sup>ect a change of modeling objectives (“learning” instead of “logistical analysis”), and users', i.e., players', needs and requirements. Use of the new framework is related to game design methodology as proposed by Greenblat [20]. Framework application is illustrated by a case study concerning education of retail managers on inventory control.

The remainder of the paper is organised as follows. In Section 2 we introduce the research methodology underlying set-up and use of the new conceptual modeling framework for simulation-based serious gaming. In Section 3, the framework is described in detail. Then the use of the framework is illustrated by a case example (Section 4). Section 5 evaluates contributions made by the framework. Finally, in Section 6, major <sup>fi</sup>ndings are summarized.

## 2. Methodology

In this section we discuss the research methodology underlying set-up of the new conceptual modeling framework for simulationbased serious gaming.

2.1. Focus – design of simulation-based games for operations management decision support

The new framework is meant to facilitate simulation-based serious game design by identifying, structuring and supporting conceptual modeling activities. As a <sup>fi</sup>eld of application we consider operations management. Relevant issues in operations management decision making concern systems design (for example, factory layout, supply chain design etc.) and their planning and control (for example, dispatching, scheduling, capacity planning etc.). The games' serious nature is related to one or more basic pedagogic purposes, such as, to describe, i.e., illustrate or demonstrate an issue, a situation or a process, to demonstrate – a method or a technique, to practice, i.e., training and education, to reflect, i.e. experiment and obtain response, or to prepare, i.e., increase or direct attention towards a speci<sup>fi</sup>c situation [43,65].

Elementary computer simulation support for serious gaming is shown in Fig. 1. It concerns the provision of (i) a simulation model capturing relevant detail and the status of a referent operations system, (ii) a simulation model interface facilitating players' roles as operations managers, by informing them on model status and performance and implementing their decisions (iii) a game interface enabling the operator to intervene in game set-up (initial settings) and progress. The dominant use of simulation in gaming classi<sup>fi</sup>es games as being computerbased, i.e., assuming high computer participant interaction, and high participant control [53].

Our research focus is motivated by our many years of experience in developing simulation models for supporting operations management decision making. In seeking guidance on model set-up we found how simulation literature and tools tend not to take a pedagogic perspective. Hence, as far as serious game characteristics, i.e., its purpose, the notion of players' roles, and players' performance evaluation, are concerned, the modeler has to rely on – the build up of – his experience. We feel how effectiveness of simulation-based games, their ef<sup>fi</sup>cient development, and their use may greatly bene<sup>fi</sup>t from modeler support being tailored towards game use of simulation models. By de<sup>fi</sup>ning a modeling framework we intend to offer such support. Essentially, it is meant to structure, and facilitate model development, by identifying relevant conceptual modeling activities, and clarifying how such activities may be executed making good use of methods, tools and good practices. Note how the concept of a modeling framework is generic, as it allows new insights, tools, and methods to be included.

## 2.2. Game design process – conceptual modeling

The new modeling framework is meant to support the game design process. We describe the game design process according to Greenblat [20], see Table 1. Greenblat's characterization of the game design process builds on earlier joint work with Duke [21]. It serves as a reference model for simulation and gaming – being much cited by simulation game designers, see, for example, Angelides and Paul [3], Crookall and Arai [16], Crookall [13,14], Galvao et al. [19], Smeds [52], Mayer et al. [35], and Battini et al. [5]. Greenblat distinguishes between <sup>fi</sup>ve stages in game design. Stages I–III address game speci<sup>fi</sup>cation in terms of its objectives, model of a chosen referent system and its representation, while stages IV and V concern game construction and preparing for its use. Here we mainly typify stages I-III, as the framework is meant to support these modeling activities. For a more detailed discussion see Greenblat [20].

The initial stage in the process of game design addresses the game subject matter, and characterizes players and game operators. Furthermore, it is meant to clarify the context of its use, such as, for example courses, workshops etc., as well as the resources available for game set-up and use. Stage II concerns model development. The model captures the most critical of the salient elements of a referent system, being either real or imaginary. It does so in terms of actors, system characteristics and linkages, and relevant external factors impacting the system.

In stage III the designer has to determine the representational style for model elements as they have been determined in stage II. A <sup>fi</sup>rst step involves decisions on their detail, being relevant for capturing system behavior, the time frame set for game operation, ordering of game activities, and player interaction. Next the representational form of model elements has to be determined. Greenblat distinguishes between 6 elements of form: scenario, roles, procedures and rules, external factors, visual imagery and symbols, and accounting system. The scenario is meant to inform players about the game environment and the problem they are facing. Each player is typically assigned a role, which implies goals to strive for, and resources to work with. Procedures and rules are meant to guide game operation and player activities. External factors are used to represent game elements in<sup>fl</sup>uencing player options or outcomes of their activities. Visual imagery and symbols like markers, badges, chips etc. facilitate players in getting around in their game environment. Accounting systems concern all quanti<sup>fi</sup>able elements and their linkages.

![](/api/attachments/DH57M7RY/fulltext/images/b75d322b3aded59b257f7552b25f421a47ca9557398955348fe056346357cc77.jpg)  
Fig. 1. Game environment – computer simulation support.

Table 1 Process of game design [22].

<table><tr><td>Stage</td><td>Issues to address</td></tr><tr><td>I Setting objectives and parameters</td><td>Subject matterPurpose (i.e. learning objective) to be servedLikely playersLikely operators (i.e. game leaders)Probable context of useResources (time, money, other) available for development and users</td></tr><tr><td>II Model development</td><td>Identify the major actors for the referent system, including their goals, activities and resources, and the interactions between themIdentify the major referent system characteristics and linkagesIndicate the type of external factors that may effect the referent system</td></tr><tr><td>III Decisions about representation</td><td>Level of abstractionTime frameLinear, radial or interactive structureInteraction among playersLinking model elements to game elements, i.e., scenarios, player roles, procedures and rules, external factors, visual imagery and symbolsDetailing of game elements</td></tr><tr><td>IV Construction and modification</td><td>Choice of materials and computer usePrototypingField tests</td></tr><tr><td>V Preparation for use by others</td><td>Operator&#x27;s manual</td></tr></table>

Stages IV and V address game construction and preparatory tasks for game use. Important activities are building and testing of game prototypes, and writing an operator manual.

2.3. Guidance on conceptual modeling for simulation – modeling frameworks

What assistance is offered in guiding the analyst in specifying a conceptual model for simulation? Our previous work showed how literature suggests the use of three basic approaches: principles of modeling, methods of simpli<sup>fi</sup>cation and modeling frameworks [46]. Principles of modeling refer to the general case of simulation modeling. They stress the bene<sup>fi</sup>ts of aiming for simple models through evolutionary design (incremental modeling). Among others, this may involve the good use of metaphors, analogies, and similarities in model creation [38]. Methods of simpli<sup>fi</sup>cation work the other way around by suggesting a reduction of model scope and/or the level of detail for model elements, starting from their relevance for model accuracy. Gains may, for example, be realized by combining model elements, leaving them out or adapting their attributes. See Innis and Rexstad [26] for an elaborate discussion.

Clearly, the aforementioned principles and methods are helpful in model construction by pointing at possibilities for model pruning. However, they do not guide the analyst in model creation – in terms of what is to be modeled. Modeling frameworks answer this latter need by specifying a procedural approach in detailing a model in terms of its elements, their attributes and their relationships. For example, Shannon [51] distinguishes between four steps in conceptual modeling: speci<sup>fi</sup>- cation of the model's purpose; speci<sup>fi</sup>cation of the model's components; speci<sup>fi</sup>cation of the parameters and variables associated with the components; and speci<sup>fi</sup>cation of the relationships between the components, parameters and variables. Activities suggested by a modeling framework may be supported by guidelines, methods and the notion of good practices. Note how such support may embed principles of modeling and methods of simpli<sup>fi</sup>cation, as discussed above.

So far, several modeling frameworks have been developed, see Robinson [45], Karagoz and Demirors [29], and Van der Zee et al. [63] for overviews. Some frameworks address the general case, i.e., discrete event dynamic systems [4]. However, most frameworks tend to be tailored towards the business or military domain. Some illustrative examples are given by Pace [36,37], Guru and Savory [22], and Kotiadis [31]. Furthermore, differences among frameworks are found concerning their scope. Whereas some frameworks focus on capturing just model contents [4], others consider a wider angle by including an exploration of the problem context, project and modeling objectives, and/or the experimental frame, i.e., model inputs and outputs [31,45].

## 2.4. Towards a conceptual modeling framework for serious gaming

To provide guidance to the game designer in the use of simulation we propose to adapt and extend the modeling framework developed by Robinson [46] for logistical analysis purposes. Alternative frameworks addressing operations systems tend to be scarce [45,63], and primarily focus on capturing just model contents. Essentially, Robinson's framework facilitates the detailling of a conceptual model in a step-wise manner. Respective steps consider an understanding of the problem context, project and modeling objectives, model inputs and outputs, and model content. As such the framework offers good initial coverage of issues to be addressed for game design, compare Table 1 (stages I–III), and Section 2.2. The framework, however, has to be adapted and extended, in order to enable its use for game set-up. Relevant changes relate to the choice of modeling objectives, suggesting the model to be used for learning purposes (instead of logistical analysis), the modeling of players' roles, and the evaluation of players' performance.

## 3. A conceptual modeling framework for simulation-based serious gaming

The new conceptual modeling framework distinguishes between <sup>fi</sup>ve key modeling activities (Section 3.1). Each activity is associated with guidelines, good practices and methods for supporting the game designer in its execution (Section 3.2). Section 3.3 supplements the framework set-up by considering requirements for assessing quality of a conceptual model.

## 3.1. Framework overview – key modeling activities

The framework distinguishes between <sup>fi</sup>ve key modeling activities in developing the conceptual model, aiming to capture (Fig. 2): (i) an understanding of the learning environment, (ii) modeling and general project objectives, (iii) model outputs, (iv) model inputs, and (v) model contents (scope and level of detail).

The <sup>fi</sup>rst and second activity in conceptual modeling largely matches Stage I in the process of game design, compare Table 1. The <sup>fi</sup>rst activity concerns an understanding of the learning environment, i.e., the operations system being studied, decision making issues considered (being open for improvement through learning), prospective players and operators, and the context of use (courses, workshops etc.). An understanding of the learning environment creates the starting point for determining modeling objectives, i.e., what is to be achieved (learned) using the simulation model, and general project objectives addressing project (time) frame and model representation.

![](/api/attachments/DH57M7RY/fulltext/images/7a6bbecdaf5a7822478124586e94cd79c90349d0103ff924b3153321dbb4c457.jpg)  
Fig. 2. A modi<sup>fi</sup>ed framework for conceptual modeling for simulation-based serious gaming (adapted from Robinson [46]).

The bottom three activities are meant to support stages II and III in game design. Relevant model outputs (performance data), indicating players' accomplishments (for the operator), are established as they follow from modeling objectives. Model inputs de<sup>fi</sup>ne the operators' possibilities for altering system con<sup>fi</sup>guration or conditions. Note how unsatisfactory outputs may cause adjustment of model inputs, thereby attempting to (further) tailor the model to players' learning needs. Finally, determining model contents involves decisions on which components to include (model scope) and their detail. Model contents should also clarify how player roles relate to the model.

Relevant extensions of the new framework relative to the original Robinson framework follow from the change of model purpose, i.e., learning instead of logistic analysis, and the notion of player roles, which are to be embedded in the model. Note how respective changes are marked by dashed rectangles in Fig. 2. See Section 5 for a more detailed discussion on this point.

## 3.2. Modeling activities – support for the game designer

Starting from the notion of key-modeling activities we discuss support for the game designer in terms of guidelines, methods, and good practices. Table 2 will be used to guide our discussion.

## 3.2.1. Understanding the learning environment

Serious games originate from a learning environment, i.e., operations management issues open for improvement (subject matter), client interests, the (educational) backgrounds and interests of the prospective players and operators, and the context of use (courses, workshops etc.). Clearly, a game designer's notion and understanding of the learning environment is a prerequisite for developing adequate games.

Greenblat and Duke [21], and Greenblat [20] suggest several techniques and good practices in getting a hold of, and detailing elements of a learning environment. Suggestions, as included in Robinson original framework [46], on the need and support for problem structuring may be added to this. Given this extensive support, and in the interest of space we only shortly typify learning environments, given our choice of domain, and game nature, i.e. being computer-based.

The education of students and the training of company managers, staff and workers characterize two dominant types of learning environments within operations management. Games may help students in developing critical thinking, their abilities to formulate good questions, and creativity in solution <sup>fi</sup>nding. In professional training emphasis is placed on employees' abilities and skills to improve performance [7,12,28,30]. Awareness of learning needs for both categories is relevant, given their direct relationship with pedagogic purposes underlying game set-up (see Section 3.2.2).

## Table 2

A modi<sup>fi</sup>ed conceptual modeling framework for simulation-based serious gaming – detailing activities.

<table><tr><td>Activity</td><td>Details</td></tr><tr><td>1. Understanding the learning environment</td><td>·Understand the subject matter, context of use, and likely players/operators, preferably by interviewing clients and subject matter experts·Explore learning needs, given the environment, i.e., student education or professional training·Decide on the appropriateness of a computer-based game format</td></tr><tr><td>2. Determine objectives– Modeling objectives</td><td>·Identify the game&#x27;s pedagogic purposes·Express modeling objectives in terms of players&#x27; achievements in mastering their decision making skills</td></tr><tr><td>– General project objectives</td><td>·Establish and assess project requirements on resource use·Clarify the nature of the model and its use with respect to:o Visualizationo Player interactiono Responsivenesso Model/component re-use</td></tr><tr><td>3. Identify the model outputs</td><td>·Check modeling objectives for relevant performance measures, indicating player achievements·Establish model outputs helping to identify potential bottlenecks in systems operations and explain player achievements·Determine format for representing responses</td></tr><tr><td>4. Identify the model inputs</td><td>·Select quantitative and qualitative data that can be changed, in order to represent alternative system configurations appealing to (alternative) groups of players·Determine range over which model inputs may be varied</td></tr><tr><td>5. Determine model content: scope and level of detail</td><td>·Determine model scope:o Identify the system boundaryo Identify all components in the real system that lie within the model boundary (include player roles)o Assess whether to include components·Determine model detail (attributes) for all components included·Indentify assumptions and simplifications concerning model scope and detail, and assess their impact on model responses</td></tr></table>

As clari<sup>fi</sup>ed in Section 2.1, we relate the notion of computer-based games to the use of simulation models for representing real-world or <sup>fi</sup>ctitious operations systems. Simulation tools offer large <sup>fl</sup>exibility in their realistic modeling of operations systems in various levels of detail, thereby serving the interests of various player groups. However, such <sup>fl</sup>exibility comes at a price – model set-up may involve signi<sup>fi</sup>cant investments in terms of resources, time and money [33]. This implies a need for considering viability of a “simpler” game format, such as a board game, offering a “physical” rather than a “virtual” environment, or training-on-the-job, by employing the real system (if available).

## 3.2.2. Determine modeling and general project objectives

The exploration of the learning environment, as addressed in the previous section, is meant to set the contours for game and simulation model development. To start game development, this knowledge needs to be linked to the game's pedagogic purpose(s), i.e., what players should have learned after completing the game (compare Section 2.1). For example, the game may be employed to foster students' creativity in solving scheduling issues in job shops, or to train workers on machine operation. In turn, simulation modeling objectives stress the utility of a simulation model within a game context. Here simulation utility is linked to the way it facilitates player learning, given the notion of players' roles relative to some referent system. Note how simulation utility may only partially explain game utility. For example, game operators and/or supportive materials may widen player scope (and learning) by introducing the subject matter, their involvement in game operation, interpretation and communication of players' scores etc.

Modeling objectives can be expressed in terms of players' achievements in mastering their decision making skills. Typically, players' decision making skills are linked to their notion and interpretation of system status, their use of algorithmic support (if any), and their maturity in choosing among decision options – given some criteria for optimization. For example, the simulation model is to facilitate players' learning on improving factory throughput or reducing lead time uncertainty by employing a novel scheduling rule, or – less speci<sup>fi</sup>c – improve their understanding of factory workings. Note how the learning environment may set various degrees of freedom in de-<sup>fi</sup>ning the model. For example, worker training may require a (high <sup>fi</sup>delity) model of an existing system. On the other hand, student education may rely on models of <sup>fi</sup>ctitious – but plausible – systems in fostering students' critical thinking, the formulation of questions, and creativity in solution <sup>fi</sup>nding, see Jones [28], Corsun [12], and Klabbers [30].

General project objectives supplement the modeling objectives by linking simulation model development and use to resource availability, and by detailing the nature of the model. Restrictions on resource use are relevant as they may impact both model contents and representation. For example, to cut expenses in game development, and to meet the project time line, decreasing model detail may seem a viable option. However, such measures need to be tested for the modeling objectives. Simpler models may be acceptable in an educational context, where model precision may be varied to some extent. However, worker training on machine use may require a high <sup>fi</sup>delity model, only allowing for minor simpli<sup>fi</sup>cations. Resource restrictions may not only involve game development, but also its actual use. This does not only refer to those resources instrumental for game set-up, like rooms, computer support, or operators, but also player availability. Typically, players are only available for (very) short periods of time, being subject to their busy schedules and/or tailored curricula.

Effective player-interaction goes together with a good match of the nature of the model to its intended use. Points to consider are:

• Model visualization: how to display model entities and their detail (2D, 3D, schematic, iconic,..)?

• Model interaction (game interface, simulation model interface): how to facilitate players'/ operators' interaction with the model (dragging, pop-ups, menus, error reports, help functions,…)?

• Model responsiveness: what delays (execution times) are acceptable for model's responses to players' decisions?

• Model reuse: how easily can the model accommodate alternative groups of players, with possibly different backgrounds?

Many simulation tools have good facilities for realistic visualization of both operations systems' entities and their dynamics. Apart from icons available from tool libraries, tools may offer the possibility to draw schemes or icons, or to import icons/pictures. It is up to the modeler to decide on model formats, given modeling objectives, and intended model user(s). Points to consider are the way alternative formats contribute to players' insights in system operations, model credibility, and modeling efforts. For example, although many of the current simulation tools allow for 3D animation, many models still rely on 2D displays. This is explained by the fact that in many cases 3D models do not add much to users' insights in system operations. Also, use of 3D models may imply greater efforts for the model developer. However, if physical dimensions of system entities do matter in solution <sup>fi</sup>nding, 3D models may be considered more insightful and trustworthy, and – therefore – worth the modeling effort.

Simulation-based games, as they are studied here, assume high user interaction. Guaranteeing <sup>fl</sup>uent user interaction forces the modeler to think over simple modes for entering player decisions (for example, item dragging, menus, buttons etc.), error reporting, and help functions. Simulation tools may offer such features, but it may take some additional programming to guarantee their appropriate use by players. This follows from the fact that so far their availability and use has been mainly meant to support the modeler in building the model and demonstrating it and its outcomes to the client [60], rather than in the context of game use.

In many cases games are played within a short time frame, being part of, for example, a lecture, or a workshop. On the other hand, players' learning tends to go together with repetitive decision making. These facts, taken together, suggest games' responsiveness to players' decision making being an important issue. Typically, models responses should be in terms of (at most) seconds or minutes, to guarantee both model outputs giving some sound indication of players' learning, and a timely completion of the game.

Game development typically focuses on its repetitive use for multiple or alternative groups of players. This possibility of re-use stresses a well-de<sup>fi</sup>ned model structure, being well-documented, and open to change (at least to some extent). A growing number of simulation tools support re-use by conforming to the concept of object orientation in model coding.

## 3.2.3. Identify the model outputs

Model outputs serve two purposes: (i) to indicate players' achievements relative to the pedagogic purposes set, and (ii) to “explain” players' achievements. In most cases those responses indicating players' achievements can be derived from the modeling objectives, compare Section 3.2.2. The second category of responses seeks to link system operations and player decision making with players' achievements. For example, system throughput (player's achievement) may rely on player's scheduling of a resource for which a high utilization (explanatory output) is reported. An important model feature in this respect may be a “decision trace” for recording the (sequence of) decisions made by a player [60]. A decision trace may be both of relevance for the player in re<sup>fl</sup>ecting on his/her decisions or “undoing” decisions, and the operator in his/her evaluation of player performance. Current simulation tools do not offer standard features for tracing player decision making. However, they may allow for user-de<sup>fi</sup>ned features to address this gap. For a more detailed discussion on best practices for performance measurement, also see Thavikulwat [53], and Salas et al. [50].

After identifying required model outputs, the modeler has to decide on the way they are presented to the users, i.e., players and operators. Some typical formats include numerical data (for example, mean, minimum, maximum, standard deviation) or graphical reports (for example, time series, bar charts, gantt charts). Note how the choice of format should be in line with the general project objectives, see Section 3.2.2.

## 3.2.4. Identify the model inputs

Model inputs are linked to operator inputs, allowing him/her to intervene in game set-up and progress, see Section 2.1, and Fig. 1. Note how game inputs following from players' decision making are addressed in the speci<sup>fi</sup>cation of model contents, see Section 3.2.5.

The choice of model inputs determines the way the model may be tailored to re<sup>fl</sup>ect alternative system con<sup>fi</sup>gurations, initial system status or assumptions on factors external to the system. Alternative system con<sup>fi</sup>gurations may, for example, refer to resource availability, and choice of planning hierarchy and rules. Alternative settings for the system's (initial) status may be used to test players' responses to <sup>fl</sup>uctuations in system work load, and resource availability. Such testing may be part of the players'/operator's evaluation of player decision making, see 3.2.3. External factors concern, for example, customer demand (mix, volume), or supplier delivery performance. Note how model inputs, also referred to as experimental factors, differ from <sup>fi</sup>xed factors, i.e. those elements of the model being pre-con<sup>fi</sup>gured by the modeler.

Choice of model inputs, and the range over which they may be varied, may be decoupled from the actual choice of system con<sup>fi</sup>gurations for a speci<sup>fi</sup>c game session. Restrictions on resources, player interests and availability may force a careful choice and sequencing of just a limited set of game runs (system con<sup>fi</sup>gurations) for a speci<sup>fi</sup>c session. However, (re)use of a game for alternative player groups may make it worthwhile to allow for more <sup>fl</sup>exibility in the choice of model inputs as well as their range. Respective choices should, however, be considered for the (additional) modeling effort required. Note how the above reasoning suggests the existence of a game life cycle, during which potential model inputs currently under the sole of control of the modeler are made accessible for the operator.

In many cases game developers have no hard job in collecting or producing lots of alternative model inputs, with possibly wide ranges. Such inputs should be carefully considered for their contributions to game utility (the “right” game settings), and its feasibility (“not too many games”), compare Section 3.3. A careful choice of inputs is therefore required, starting from the modeling objectives, player availability, resources, and game format. For example, busy managers may force a tailoring of the game to just a few model inputs, whereas student use, does not imply suchlike restrictions. Also a ranking of (combined) inputs (subjects) for their contribution to learning objectives may be necessary to arrive at both an appealing and feasible set of game runs.

## 3.2.5. Determine model content: scope and level of detail

Determining model content entails two activities, i.e., deciding on model scope and its detail. Model scope identi<sup>fi</sup>es model boundaries in terms of components to be included in the model, whereas model detail establishes model depth in terms of components' attributes.

Model scope may be captured according to alternative formats, being characterized by the types of components distinguished. For example, Pidd [39] suggests conceiving simulation models in terms of four types of component: entities, active states, dead states and resources. Many other examples are given by Pooley [41], and Ryan and Heavey [49]. Aforementioned formats, however, do not allow for specifying player roles (decision makers) as they are to be embedded in the simulation model. Typically, they stress <sup>fl</sup>oor operations (physical movements), but do not explicitly recognize decision making activities.

Given the drawbacks of current formats for capturing player interaction, we propose an alternative format for describing model scope, see Van der Zee and Slomp [60]. Component types considered are agents, <sup>fl</sup>ow items and jobs. Especially the notion of agents facilitates a straightforward modeling of player roles. We will only brie<sup>fl</sup>y characterize each component type here. For more details, see Van der Zee and Van der Vorst [61], and Van der Zee [55–57].

Agents represent the infrastructural, non-movable, intelligent elements of an operations system such as workstations, information systems, and managers. Their decision-making capabilities relate to the transformation of goods or data. Within a game context, agents may be linked both to (coded) model components and player roles.

Four types of movable (or <sup>fl</sup>ow) items are distinguished: goods (such as materials, parts, and semi-<sup>fi</sup>nished products), resources (such as workers, tools, and vehicles), data (monitoring data, demand forecasts, etc.), and job de<sup>fi</sup>nitions. Job de<sup>fi</sup>nitions model the <sup>fl</sup>ow of control, i.e., the messages that steer the movement of goods, resources, and data. As such, they initiate and inform agent activities by carrying relevant information related to these activities, such as their input, processing conditions, and the agents to whom the resulting output should be sent. Above we linked agents to both the simulation model and player roles. Hence, job de<sup>fi</sup>nitions may either be embedded in the simulation model or serve as a game input, compare Fig. 1.

In an operations system, agents and <sup>fl</sup>ows are linked by jobs, i.e., business activities. Further, we assume that each such activity relates to a job. Typically, a job links <sup>fl</sup>ow items and agent's resources. Job execution drives model dynamics, marking events by the start and completion of jobs. Note how relating player roles to agents may imply realtime player jobs, i.e., decision making, being decoupled from the activities represented by the model.

To identify those agents, <sup>fl</sup>ow items and jobs to be included in the model a three step approach is proposed: (i) Identify the system boundary, (ii) Identify components within the boundary, and (iii) Assess whether to include/exclude all components identi<sup>fi</sup>ed.

The <sup>fi</sup>rst step assumes an exploration on the edges of the model. Model inputs may be helpful here as they identify components that should be included anyway. Furthermore, model outputs, such as for example, factory lead time or customer delivery times, may hint at what components to include. Typically, model edges are found at decoupling points being marked by logical boundaries (for example stocks, piles of incoming customer orders) and/or organizational boundaries (for example, companies, departments).

The second step concerns identifying components within the referent system's boundaries. This refers especially, but not only, to those components that do matter in linking model inputs, and player decision making to model responses (player achievements). For example, good planning – by the player – of additional machines (model input) may improve system throughput and reduce waiting times. Note how this involves at least two agents (player, machine(s)), three <sup>fl</sup>ow items (goods modeling system throughput, data representing feedback on shop status for the planner, and job de<sup>fi</sup>nitions specifying player's planning decisions), and two jobs (player's planning, machine operation).

The <sup>fi</sup>nal step assesses whether to include or exclude components found for step 2. In principle, justi<sup>fi</sup>cation of either choice should be based on the components relevance for model validity, credibility, utility and feasibility (compare Section 3.3). For example, would removing a component imply a violation of model accuracy (validity)? If not, would it hurt model's credibility, as a “familiar” component may be left out? Also what would be the effects for feasibility (less modeling efforts) or utility (lower model complexity)? Decisions on model scope should be recorded and documented, to facilitate the development process (explicit notion of modeling decisions agreed upon), and game reuse (see Section 3.2.2). A suitable format for doing so may be tables listing components and the justi<sup>fi</sup>cation of their in/exclusion. Tables may be supplemented by diagrams for clarifying component's relationships in terms of some logical (for example, planning hierarchy) or physical ordering (for example, factory layout).

After deciding on the components to include in the model, their detail has to be determined. For example, agents may be detailed for their capacities in storing, and processing speci<sup>fi</sup>c (amounts of)

<sup>fl</sup>ow items, and available resource. Flow items, may be characterized by their arrival pattern, routings, quantity etc. Jobs may be characterized by the nature of the activities involved, following from process logic, and the <sup>fl</sup>ow items and resources serving as inputs. See Robinson [45] for a template suggesting relevant detail for operations systems. Again, just as for model scope, we suggest to record decisions on model detail by means of tables and/or diagrams, characterizing and justifying the detail for each model component.

Both model scope and detail typically go together with simpli<sup>fi</sup>cations and assumptions. Here assumptions follow from uncertainties about the referent system, whereas simpli<sup>fi</sup>cations are meant to make model development and use easier. For policies on making assumptions and simpli<sup>fi</sup>cations see Robinson [45,46]. Depending on the required model accuracy, there may be a need to assess assumptions and simpli-<sup>fi</sup>cations for their effects on system operations, and player achievements. Note how game use in educational settings may allow for rigorous simpli<sup>fi</sup>cations in an attempt to isolate the main effects of the operations manager's decision making on system performance.

## 3.3. Model assessment

In designing a conceptual model it is useful to have a set of requirements in mind [46]. These provide a basis against which to determine whether a conceptual model is appropriate. Our framework involves four requirements for judging the quality of a conceptual model, as follows:

• Validity: “a perception, on behalf of the modeler, that the conceptual model can be developed into a computer model that is suf<sup>fi</sup>ciently accurate for the purpose at hand”.

• Credibility: “a perception, on behalf of the clients, that the conceptual model can be developed into a computer model that is suf<sup>fi</sup>ciently accurate for the purpose at hand”.

• Utility: “a perception, on behalf of the modeler and the clients, that the conceptual model can be developed into a computer model that is useful as an aid to the users' education, given a speci<sup>fi</sup>ed learning context”.

• Feasibility: “a perception, on behalf of the modeler and the clients, that the conceptual model can be developed into a computer model with the time, resource and data available”.

Validity captures the modeler's view on whether the model is suf-<sup>fi</sup>ciently accurate for its purpose, which in this case is pedagogic. Credibility is similar to validity, but is taken from the perspective of the clients rather than the modeler. A model being suf<sup>fi</sup>ciently accurate suggests that all “important” components and relationships are in the model. The perception of whether the important components and relationships are present in the model may vary between the clients and the modeler, and from client to client. It is not unusual, for instance, for clients to desire additional detail in a model, even though the modeler's opinion is that this will have little impact on the model's accuracy.

Given the pedagogic purposes of the simulation the need for accuracy may not be so stringent. Credibility could be interpreted as “realism” or “plausibility”, that is, the extent to which game users perceive the simulation to re<sup>fl</sup>ect the real life situation. Adobor and Daneshfar [2] show how realism may positively in<sup>fl</sup>uence player learning. Depending on the game user's knowledge of the real life situation, this could mean that a relatively low level of accuracy is required, although it must be suf<sup>fi</sup>cient to provide appropriate learning.

For simulation and gaming utility should be linked to the player learning needs and operator requirements. An important moderator of utility may be the “simplicity of model use”. Ease of use would include (a) ease of understanding how to play the game, (b) ease of understanding the results returned, and (c) ease of determining what is needed to improve performance [18]. Adobor and Daneshfar [2] demonstrated that ease of use by the participants positively affected learning in the simulation. Since simulation models for gaming purposes are typically re-used to facilitate different groups of players, re-usability should also be included in considerations about the utility of a conceptual model.

The requirement for model feasibility accounts for whether it is possible to develop the coded model given the skills of the modeler, and the resources and data that are made available. It also takes account of whether the model can be developed within the time frame required for completing the work. If any of these constrains the model development to the point of making it infeasible, then an alternative conceptual model has to be sought.

## 4. Case example – inventory control in retail management

To illustrate the use of the modeling framework we consider a case study on the development of a serious game addressing inventory control for retail management. First we discuss the case background. Next, we consider game development.

## 4.1. Background

A supplier of software for retail management seeks to further exploit its knowledge of business processes in retail. One of the opportunities considered is the design of serious games for educational purposes. Typically, retail managers are educated by training-on-thejob. The use of serious games may present an attractive, alternative way for educating managers in making better founded decisions, and speeding up their learning processes.

As a <sup>fi</sup>rst initiative the company considered the development and use of a serious game for educating managers in fashion retail on yield management [24,58,59]. Sales in fashion retail often tend to follow a seasonal pattern, assuming product demand to be concentrated in a speci<sup>fi</sup>c period, following customers' interests. Typically, product demand diminishes at the end of a season, possibly causing <sup>fi</sup>nancial losses due to unsold stock. Retail managers may in<sup>fl</sup>uence customer demand by in season pricing decisions. In<sup>fl</sup>uencing customer demand in this way is meant to improve shops' pro<sup>fi</sup>ts by increasing turnover (during the season) and reducing unsold stock (at the end of season). Speci<sup>fi</sup>cally, the game concerns the sale of jeans – being considered as an appealing example setting.

## 4.2. Conceptual modeling

In this section we discuss conceptual modeling for the game. Our discussion will be guided by Table 3 that summarizes the conceptual model as the outcome of the modeling activities.

## 4.2.1. Understanding the learning environment

The choice of subject for the game – in season price decisions for fashion retail – follows from interviews of several (senior) retail managers. Players considered are (novice) retail managers. Consultants being employed by the software supplier are meant to act as game operators. The game is supposed to be used in half-day workshops on the chosen subject for various player groups. Possibilities for realistic modeling of retail environments, together with low development cost, motivated the appropriateness of a computer-based game format.

## 4.2.2. Determine modeling and general project objectives

The game is supposed to contribute to retail managers' awareness and insights on the way pricing decisions in<sup>fl</sup>uence customer behavior and shop performance. In turn, the simulation model is meant to facilitate retail managers in showing their skills in making balanced and founded pricing decisions for in-season promotion, see Section 4.1. The key performance indicator is the pro<sup>fi</sup>t margin, as it results from sales, purchase prices and unsold inventory. Starting from the educational purpose of the game, intuitive – simple – models are aimed at, facilitating a clear isolation of main effects of retail managers' decision making.

Table 3  
Retail game – summary of conceptual model.

<table><tr><td>Activity</td><td>Details</td></tr><tr><td>1. Understanding the learning environment</td><td>Clients: retail software supplier (senior consultant)Subject matter experts: senior retail managers, retail software supplierSubject matter: in-season pricing decisions in fashion retail (jeans)Players: (novice) retail managersOperators: retail software supplier (consultants)Context of use: workshop (half a day)Appropriateness of a computer-based game format: confirmed</td></tr><tr><td>2. Determine objectives– Modeling objectives</td><td>Pedagogic purposes: educate retail managers by fostering their awareness and insights on the way in-season pricing decisions influence customer behavior, and – next – shop performance.Modeling objectives: Facilitate players&#x27; in making well-informed and balanced pricing decisions for in-season promotion, resulting in profit margins meeting standards.</td></tr><tr><td>– General project objectives</td><td>Project requirements: (especially) player availability should be consideredModel nature:o Visualization: graphs, bar charts detailing inventory, sales and profit; customer behavior (demand) is captured in equations (not visualized)o Player interaction: simple menus build up of buttons, input boxes and slider bars (operator), slider bars (players)o Responsiveness: on-lineo Model/component re-use: yes</td></tr><tr><td>3. Identify the model outputs</td><td>Performance measures (player achievements): profit marginExplanatory measures: sales figures, inventory status, pricing decisions (decision trace: timing, price setting)Format: Graphs</td></tr><tr><td>4. Identify the model inputs</td><td>Inputs:o Workspace— Season length— Inventory (initial setting, overstocking)— Initial price— Decision frequency: seasonal, weeklyo Cost data— Purchasing costs— Penalty costs (back ordering)— Discounting costs— Costs and proceeds of excess inventoryo Customer demand— Price elasticity— Seasonality (calendar effects, decaying age)— Initial price— Randomness in demand</td></tr><tr><td>5. Determine model content: scope and level of detail</td><td>Scope: seeTable 4, Fig. 4Detail: seeFig. 5</td></tr></table>

General project objectives suggest the availability of the players, i.e., retail managers, to be the most important restriction for game design. Their busy agendas and perceived loss of productivity are among the reasons for this. Retail managers typically make their decisions using a dash board view of shop transactions and their impact on its performance. Visualization should therefore highlight those abstractions of reality in terms of relevant graphs, rather than represent shop <sup>fl</sup>oor detail. Players' interfacing facilities are required to be simple, as generally retail managers are not familiar with simulation tools. Therefore slider bars are chosen as a primary means for enabling player decision making with respect to the model. The aforementioned players' needs together de<sup>fi</sup>ne the format for the simulation model interface, see

Fig. 3. The <sup>fi</sup>gure shows the interface as it has been developed for the game. Furthermore, effects (if any) of player decision making on shop status should be promptly visible to the player. Re-use for educating alternative groups of retail managers is foreseen.

## 4.2.3. Identify the model outputs

Players' achievements are represented in terms of the end of season pro<sup>fi</sup>t margin. Explanatory measurements concerning inventory status, sales <sup>fi</sup>gures, and (earlier) pricing decisions by means of a decision trace, underpin both the player's decision making, and the evaluation of his/her success, also see Fig. 3. Note how the latter evaluation may be used to judge a player's progress and learning.

## 4.2.4. Identify the model inputs

The game is to be rather <sup>fl</sup>exible with respect to the choice of inputs, allowing for alternative groups of players with possibly different (educational) backgrounds, and interests. Our choice of inputs is based on literature research and consultation of domain experts [24]. Actual game use assumes a selection among alternative (categories) of possible inputs and their range for de<sup>fi</sup>ning a (small) number of game runs. Categories of inputs considered follow from the main elements characterizing the decision model being studied, i.e., work space, cost data, and customer demand. Note how work space, as de<sup>fi</sup>ned by the top management, is used for parametrizing retail manager's decision making. For example, it may be used to set frequency of decision making, i.e., weekly or seasonal.

## 4.2.5. Determine model content: scope and level of detail

Model scope is shown in Table 4 and Fig. 4. Table 4 indicates and explains whether system components are being included in the model. It suggests a simple model being composed of two agents (Retail manager and Shop), <sup>fi</sup>ve types of <sup>fl</sup>ow items (Products, Customers, Shop performance, Work space, Pricing decisions), and two types of jobs (Modify product price, Sell products). Several other components are excluded from the model. This follows from the model simplicity aimed at, see Section 4.2.2. Fig. 4 shows the way model components relate.

Model detail is speci<sup>fi</sup>ed by means of object diagrams [8], see Fig. 5. The <sup>fi</sup>gure shows how a player is related to the role of a retail manager, i.e., an intelligent agent. His/her decision jobs are triggered by events, i.e., shop transactions. Decision output is concerned with job de<sup>fi</sup>nitions specifying pricing decisions. Model detail may further be supplemented by tables indicating and explaining choice of system detail. As this logic is rather similar to the representation of model scope, we do not discuss it here.

## 5. Discussion – added value of the modeling framework

## 5.1. Framework set-up: serious gaming vs. logistic analysis

Let us now highlight new elements of the proposed framework, relative to the framework developed by Robinson [46] for logistic analysis purposes. We found little need to adapt the formulation of key modeling activities for the new framework. One subtle change is suggested concerning the <sup>fi</sup>rst activity. The phrase “Understanding the problem situation” is replaced by “Understanding the learning environment”. This is meant to mark the change of model use, i.e., gaming for learning purposes instead of logistic (problem) analysis. Otherwise, the high level activities remain as they were for the original framework.

The main differences between both frameworks concern the detailed implementation of, and support for, the key activities, except for the <sup>fi</sup>rst activity, see above:

• Modeling objectives: Model use is meant to facilitate player learning rather than to provide precise estimates on an operations system's logistic performance. Typically, model accuracy is moderated by the pedagogic purposes underlying the game. Indeed, a simple game may have a greater learning effect than a more complicated game (Section 3.3). Pidd [40] identi<sup>fi</sup>es four modes of model use, with models used for ‘providing insights and debate’ (which could include serious games) requiring the lowest threshold of accuracy. In terms of modeling objectives, the possibility of model re-use for alternative player groups should also be considered.

![](/api/attachments/DH57M7RY/fulltext/images/aafee6a5d91f0aac3f4cc52dddaaf345e39db2ba46b06ffd4bb11281dc6f5f05.jpg)  
Fig. 3. Retail game – simulation model interface.

• General modeling objectives: Users other than analysts set higher demands to insightful model representation, and the simplicity of model interaction. Player availability may be an issue.

• Model outputs: Observations typically cover a short(er) time frame. As re<sup>fl</sup>ection is the real aim of the game, tracing decisions is a prerequisite for player decision analysis.

• Model inputs: Initial system status may be added as a possible input. Mostly, only a limited number of game runs are possible for a session. Consequently, the choice of settings and their sequencing is crucial.

• Model contents: The notion of player roles in model set-up forces an extension of model notation. Apart from the physical processes, their control needs to be (explicitly) speci<sup>fi</sup>ed in terms of intelligent agents (players).

Similar to Robinson's original framework [46] our framework involves four requirements for conceptual model assessment, i.e., validity, credibility, utility, and feasibility. Changes relative to Robinson's work are in their de<sup>fi</sup>nition and interpretation:

• Validity, credibility: Whereas model accuracy in logistics decision making may be of (utmost) importance, demands on model detail may be less stringent on game models – as long as the learning experience is safe-guarded, also see above (modeling objectives).

• Utility: The new de<sup>fi</sup>nition of this requirement acknowledges a change of modeling objective, i.e., “aiding users' education, given a speci<sup>fi</sup>ed learning context”, instead of “aiding decision-making within the speci<sup>fi</sup>ed context”. The notion of player roles is re<sup>fl</sup>ected in the simplicity of model use being an important moderator of utility.

## 5.2. Scope

Essentially, the scope of the framework is determined by initial choices concerning its use, i.e., speci<sup>fi</sup>cation of conceptual models for simulation-based serious games, its <sup>fi</sup>eld of application, i.e., operations management, and class of simulation models being addressed. Conceptual models as they result from framework application are meant to be non-software speci<sup>fi</sup>c speci<sup>fi</sup>cations for the coded simulation model. Given our choice for a small intuitive set of basic model components, we assume mapping the speci<sup>fi</sup>cation of model contents on model code can be done with relative ease.

Table 4 Retail game – model scope.

<table><tr><td>Component</td><td>In/exclude</td><td>Justification</td></tr><tr><td colspan="3">Agents</td></tr><tr><td>Top management</td><td>Excluded</td><td>Game operator&#x27;s role; assumption: no interference during game operation</td></tr><tr><td>Retail manager</td><td>Included</td><td>Player&#x27;s role; key influence on system performance</td></tr><tr><td>Shop</td><td>Included</td><td>Operations system under study; key influence on system performance</td></tr><tr><td>Suppliers</td><td>Excluded</td><td>Assumption: no ordering during season</td></tr><tr><td>Markets</td><td>Excluded</td><td>Simplification: shop coincides with market place</td></tr><tr><td>Competitors</td><td>Excluded</td><td>Simplification: activities of competitors are largely neglected, except for random fluctuations in demand</td></tr><tr><td colspan="3">Flow items</td></tr><tr><td colspan="3">Goods</td></tr><tr><td>Products</td><td>Included</td><td>Represent products being offered; key influence on system performance</td></tr><tr><td>Customers</td><td>Included</td><td>Represent demand; key influence on system performance</td></tr><tr><td colspan="3">Data</td></tr><tr><td>Shop performance</td><td>Included</td><td>Feed back for player and game operator; model outputs</td></tr><tr><td>Supplier agreements</td><td>Excluded</td><td>Assumption: no short term relevance for shop performance</td></tr><tr><td>Replenishment orders</td><td>Excluded</td><td>Simplification: no ordering during season</td></tr><tr><td>Market information</td><td>Excluded</td><td>Simplification: static data, made available at game start</td></tr><tr><td>Competitor analysis</td><td>Excluded</td><td>Simplification: no updates on competitors activities</td></tr><tr><td colspan="3">Job definitions</td></tr><tr><td>Work space</td><td>Included</td><td>Characterizes manager&#x27;s permanent job; Model inputs</td></tr><tr><td>Pricing decisions</td><td>Included</td><td>Key influence on system performance</td></tr><tr><td colspan="3">Jobs</td></tr><tr><td>Modify product price</td><td>Included</td><td>Player&#x27;s main activity; key influence on system performance</td></tr><tr><td>Sell products</td><td>Included</td><td>Key influence on system performance</td></tr></table>

So far, literature on discrete event simulation almost solely facilitates its use for logistic analysis purposes. The new framework supports discrete event simulation use for serious gaming purposes. In turn, the new framework may be considered a basis for further research on uses of simulation similar to gaming. Examples include its use for knowledge elicitation [47] or lean manufacturing engineering [62]. Typically, such applications assume users – other than the analyst – to be actively involved in (visual) model setup and/or use.

Two dominant learning environments may be linked operations management (Section 3.2.1), i.e., education of students and training of company managers, staff and workers. Differences with respect to their interests may be re<sup>fl</sup>ected in modeling objectives (pedagogic purposes), choice of model (being tailored to a speci<sup>fi</sup>c (real) system or not), and game use (given time and resources available).

Our choice of domain implies a rather wide <sup>fi</sup>eld of application for simulation-based games. Therefore, it may be worthwhile to further tailor the framework to address more speci<sup>fi</sup>c <sup>fi</sup>elds, such as, for example, warehousing, inventory management, supply chains, health care, transportations systems, and/or hierarchical levels in operations management decision making, i.e., strategic, tactical or operational decision making. Tailoring of the framework suggests a further detailing of guidelines, good practices and methods, as they are associated with modeling activities. For example, subclasses of agents and <sup>fl</sup>ow items may be de<sup>fi</sup>ned to capture the speci<sup>fi</sup>cs of the <sup>fi</sup>eld. Also the choice of inputs and outputs may rely on pre-de<sup>fi</sup>ned sets of decision issues and performance measures being considered characteristic for the <sup>fi</sup>eld.

![](/api/attachments/DH57M7RY/fulltext/images/5d8fad0be4ab6d8246ca0125454ee3e1de76c726a91580a5b3b0b21e5e21a55b.jpg)  
Fig. 4. Game scope for retail game [25].

![](/api/attachments/DH57M7RY/fulltext/images/d90ccec0efa8f6883e7fd3b5224fca44fe54202ddcce710269d44ef12ff82245.jpg)  
Fig. 5. Retail game – model contents: agents Retail Manager and Shop.

In this article we chose to study the use of discrete event simulation for serious gaming purposes. Depending on the learning objectives also other types of simulation models may qualify as a vehicle for gaming. Discrete event simulation models assume models to be (i) dynamic, i.e., representing a system as it evolves over time, (2) stochastic, i.e., allowing for random input components, and (3) discrete, i.e. linking changes of system status to separate points in time [33]. Other types of models may be classi<sup>fi</sup>ed as either static, deterministic or continuous. For example, players' understanding of procedural logic within an operations management context, such as product routings or scheduling rules, may bene<sup>fi</sup>t from using deterministic models in initial game runs – as players are not “bothered” yet by the uncertainties in a system's operations. Tailoring our framework to alternative classes of simulation models is considered an interesting avenue for future research.

## 5.3. Guidance

Irrespective of its use for logistic analysis purposes or for serious gaming, simulation modeling is often considered more of an art than a science [51,53]. In many cases, both the analyst and the game designer are left on their own in their creative work, thereby relying on their experience. By proposing a modeling framework we aim to structure their work by identifying modeling activities, and suggesting guidelines, good practices and methods relevant for their execution – in an explicit way. In turn, this is meant to help in communicating the (build up of the) conceptual model with stakeholders, allowing them to participate in modeling and to judge its progress.

## 6. Concluding remarks

In this article, we have addressed the guidance for the game designer in developing a simulation-based serious game focusing on operations management decision making. Serious games are helpful for (future) managers in learning how to make better decisions. While literature acknowledges the potential of discrete event simulation as a basis for serious gaming, it offers little support for the game designer in making good use of simulation. In response, we propose a conceptual modeling framework for simulation-based serious gaming.

The new framework focuses on the construction of a conceptual model. It structures the conceptual modeling process by identifying 5 key modeling activities. Activities address an understanding of the learning environment, de<sup>fi</sup>nition of modeling and general project objectives, and determining model inputs, outputs and contents. Each activity is further detailed in terms of steps to undertake, good practices, and supportive methods.

As a starting point for developing the new framework we used an existing framework that was developed for “classic use” of discrete event simulation, i.e., logistic analysis [46]. While the frame set by the key activities largely holds for both uses, relevant changes to the original framework involve their implementation and associated support for the game designer. Essentially, changes re<sup>fl</sup>ect the choice of modeling objective (learning vs. logistic analysis), users (players instead of the analyst), and user interaction with the model (on-line vs. off-line).

Insights obtained in building the new framework may also bene<sup>fi</sup>t future research on alternative soft uses of simulation [44] assuming high user interaction/involvement, like knowledge elicitation [47] or lean manufacturing engineering [62]. Furthermore, a further tailoring of the framework to speci<sup>fi</sup>c <sup>fi</sup>elds within operations management, or other classes of simulation models may prove bene<sup>fi</sup>cial.

## Acknowledgement

The authors like to thank Cees Boon for his project involvement.

## References

[1] H.H. Adelsberger, M.H. Bick, U.F. Kraus, J.M. Pawlowski, A Simulation Game Approach for Ef<sup>fi</sup>cient Education in Enterprise Resource Planning Systems, Proceedings of the 13th European Simulation Multiconference, 1999, pp. 454–460, Warsaw.

[2] H. Adobor, A. Daneshfar, Management simulations: determining their effectiveness, The Journal of Management Development 25 (2) (2006) 151–168.

[3] M.C. Angelides, R.J. Paul, A methodology for speci<sup>fi</sup>c, total enterprise, role-playing, intelligent gaming-simulation environment development, Decision Support Systems 25 (2) (1993) 89–108.

[4] G. Arbez, L. Birta, The ABCmod Conceptual Modelling Framework, in: S. Robinson, R.J. Brooks, K. Kotiadis, D.J. van der Zee (Eds.), Conceptual Modelling for Discrete-Event Simulation, CRC/Taylor & Francis, Boca Raton, 2010, pp. 133–178.

[5] D. Battini, M. Faccio, A. Persona, F. Sgarbossa, Logistic Game™: learning by doing and knowledge-sharing, Production Planning & Control 20 (8) (2009) 724–736.

[6] V. Belton, M.D. Elder, Decision support systems: learning from visual interactive modelling, Decision Support Systems 12 (4–5) (1994) 355–364.

[7] T. Ben-Zvi, The ef<sup>fi</sup>cacy of business simulation games in creating Decision Support Systems: an experimental investigation, Decision Support Systems 49 (1) (2010) 61–69.

[8] G. Booch, Object-oriented Analysis and Design with Applications, Benjamin Cummings, Redwood City, 1994.

[9] F. Borrajo, Y. Bueno, I. De Pablo, B. Santos, F. Fernandez, J. Garcia, I. Sagredo, SIMBA: a simulator for business education and research, Decision Support Systems 48 (3) (2010) 498–506.

[10] G.M. Chapman, J.F. Martin, Computerized business games in engineering education, Computers in Education 25 (1/2) (1995) 67–73.

[11] L. Chwif, M.R.P. Barretto, Simulation models as an aid for the teaching and learning process in operations management, in: S. Chick, P.J. Sánchez, D. Ferrin, D.J. Morrice (Eds.), Proceedings of the 2003 Winter Simulation Conference, IEEE, Piscateway, NJ, 2003, pp. 1994–2000.

[12] D.L. Corsun, We sail the same ship: response to “shuf<sup>fl</sup>ing deck chairs”, Journal of Hospitality and Tourism Education 12 (3) (2000) 10–11.

[13] D. Crookall, A guide to literature on simulation/gaming, in: D. Crookall, K. Arai (Eds.), Simulation and gaming across disciplines and cultures, Sage Publications Thousand Oaks, 1995, pp. 151–171.

[14] D. Crookall, Editorial: thirty years of interdisciplinarity, Simulation & Gaming 31 (1) (2000) 5–21.

[15] D. Crookall, Serious games, debrie<sup>fi</sup>ng, and simulation/gaming as a discipline, Simulation & Gaming 41 (6) (2010) 898–921.

[16] D. Crookall, K. Arai, Simulation and gaming across disciplines and cultures, Sage, Thousand Oaks, CA, 1995.

[17] A.J. Faria, W.J. Wellington, A survey of simulation game users, former-users, and never-users, Simulation & Gaming 35 (2) (2004) 178–207.

[18] A.J. Faria, D. Hutchinson, W.J. Wellington, S. Gold, Developments in business gaming: a review of the past 40 years, Simulation & Gaming 40 (4) (2009) 464–487.

[19] J.R. Galvao, P.G. Martins, M.R. Gomes, Modeling reality with simulation games for a cooperative learning, in: J.A. Joines, R.R. Barton, K. Kang, P.A. Fishwick (Eds.), Proceedings of the 2000 Winter Simulation Conference, IEEE, Piscateway NJ, 2000, pp. 1692–1698.

[20] C.S. Greenblat, Designing Games and Simulations – An Illustrated Handbook, Sage Publications, London, 1988.

[21] C.S. Greenblat, R.D. Duke, Principles and practices of gaming simulation, Sag Publications London. 1981

[22].A. Guru P. Savory A template-based conceptual modeling infrastructure for simulation of physical security systems, in: R.G. Ingalls, M.D. Rossetti, J.S. Smith, B.A. Peters (Eds.), Proceedings of the 2004 Winter Simulation Conference, IEEE, Piscatawav. NL.2004 pp. 866-873

[23] R. Hieber, I. Hartel, Inpacts of SCM order strategies evaluated by simulation-based “Beer Game” approach: the model, concept, and initial experiences, Production Planning & Control 14 (2) (2003) 122–134.

[24] Holkenborg, J.B.M. 2009. The development of a retail simulation game – modelling framework & pilot study. Master thesis, University of Groningen, The Netherlands.

[25] M.R. Hoogeweegen, D.W. Van Liere, P.H.M. Vervest, L.H. Van der Meijden, I. de Lepper, Strategizing for mass customization by playing the business networking game, Decision Support Systems 42 (3) (2006) 1402–1412.

[26] G. Innis, E. Rexstad, Simulation model simpli<sup>fi</sup>cation techniques, Simulation 41 (1) (1983) 7–15.

[27] S. Jain, C.R. McLean, A concept prototype for integrated gaming and simulation for incident management, in: L.F. Perrone, F.P. Wieland, J. Liu, B.G. Lawson, D.M. Nicol, R.M. Fujimoto (Eds.), Proceedings of the 2006 Winter Simulation Conference, IEEE, Piscateway NJ, 2006, pp. 493–500

[28] K. Jones, Simulations: A Handbook for Teachers and Trainers, 3rd ed. Nichols Publishing Company, East Brunswick, NJ, 1995.

[29] N.A. Karagoz, O. Demirors, Conceptual Modelling Notations and Techniques, in: S. Robinson, R.J. Brooks, K. Kotiadis, D.J. van der Zee (Eds.), Conceptual Modelling for Discrete-Event Simulation, CRC/Taylor & Francis, Boca Raton, 2010, pp. 179–210.

[30] J.H.G. Klabbers, The gaming landscape: a taxonomy for classifying games and simulations, Digital Games Research Conference 2003, University of Utrecht, The Netherlands, 2003, pp. 54–67.

[31] K. Kotiadis, Using soft systems methodology to determine the simulation study objectives, Journal of Simulation 1 (3) (2007) 215–222.

[32] T. Lainema, O.P. Hilmola, Learn more, better and faster: computer-based simulation gaming of production and operations, International Journal of Business Performance Management 7 (1) (2005) 34–59.

[33] A. Law, Simulation Modeling & Analysis, McGrawHill, New York, 2007.

[34] M.A. Lewis, H.R. Maylor, Game playing and operations management education, International Journal of Production Economics 105 (2007) 134–149.

[35] I.S. Mayer, W. Bockstael-Blok, E.C. Valentin, A building block approach to simulation: an evaluation using containers adrift, Simulation & Gaming 35 (1) (2004) 29–52.

[36] D.K. Pace, Development and documentation of a simulation conceptual model, Proceedings of the 1999 Fall Simulation Interoperability Workshop, 1999, Avail able via, http://www.sisostds.org/, [accessed March 18, 2011].

[37] D.K. Pace, Simulation conceptual model development, Proceedings of the 2000 Spring Simulation Interoperability Workshop, 2000, Available via, http://www. sisostds.org/, [accessed March 18, 2011].

[38] M. Pidd, Tools for Thinking – Modelling in Management Science, 2nd ed. Wiley, Chichester, 1999.

[39] M. Pidd, Computer Simulation in Management Science, Wiley, Chichester, 2004.

[40] M. Pidd, Why Modelling and Model Use Matter, The Journal of the Operational Research Society 61 (1) (2010) 14–24.

[41] R.J. Pooley, Towards a standard for hierarchical process oriented discrete event diagrams, Transactions of the Society for Computer Simululation 8 (1991) 1–41.

[42] J.R. Raser, Simulation and Society: An Exploration of Scienti<sup>fi</sup>c Gaming, Allyn and Bacon, Boston, 1969.

[43] J.P. Riis, J. Johansen, H. Mikkelsen, Simulation games in production management – An introduction, in: J.O. Riis (Ed.), Simulation games and learning in production management, Chapman & Hall, London, 1995, pp. 3–11.

[44] S. Robinson, Soft with a hard centre: discrete-event simulation in facilitation, The Journal of the Operational Research Society 52 (8) (2001) 905–915.

[45] S. Robinson, Conceptual modelling for simulation Part I: de<sup>fi</sup>nition and requirements The Journal of the Operational Research Society 59 (3) (2008) 278-290

[46] S. Robinson, Conceptual modelling for simulation Part II: a framework for conceptual modelling, The Journal of the Operational Research Society 59 (3) (2008) 291-304.

[47] S. Robinson, A. Alifantis, J.S. Edwards, J. Ladbrook, T. Waller, Knowledge based improvement: simulation and arti<sup>fi</sup>cial intelligence for identifying and improving human decision-making in an operations system, The Journal of the Operational Research Society 56 (8) (2005) 912–921.

[48] V. Ruohomaki, Learning and education with simulation games, in: J.O. Riis (Ed.), Simulation games and learning in production management, Chapman & Hall, London, 1995, pp. 13–25.

[49] J. Ryan, C. Heavey, Process modeling for simulation, Computers in Industry 57 (1) (2006) 437–450.

[50] E. Salas, M.A. Rosen, J.D. Held, J.J. Weissmuller, Performance measurement in simulation-based training: a review and best practices, Simulation & Gaming 40 (3) (2009) 328–376.

[51] R.E. Shannon, Systems Simulation – The Art and Science, Prentice Hall, Englewood Cliffs, 1975.

[52] R. Smeds, Simulation for accelerated learning and development in industrial management – guest editorial, Production Planning & Control 14 (2) (2003) 107–110.

[53] P. Thavikulwat, The architecture of computerized business gaming simulations, Simulation & Gaming 35 (2) (2004) 242–269.

[54] J. Toyli, S.O. Hanse, R. Smeds, Plan for pro<sup>fi</sup>t and achieve pro<sup>fi</sup>t: lessons learnt from a business management simulation, Production Planning & Control 17 (6) (2006) 584–595

[55] D.J. Van der Zee, Modeling decision making and control in manufacturing simulation, International Journal of Production Economics 100 (1) (2006) 155–167.

[56] D.J. Van der Zee, Developing participative simulation models – framing decomposition principles for joint understanding, Journal of Simulation 1 (3) (2007) 187–202.

[57] D.J. Van der Zee, Building insightful simulation models using Petri Nets – a structured approach, Decision Support Systems 51 (1) (2011) 53–64.

[58] D.J. Van der Zee, J.B.M. Holkenborg, Exploring simulation-based serious gaming – Framing the issues, in: M. Gunal, B. Tjahjono, S. Robinson, S. Taylor (Eds.), Proceedings of the Operational Research Society Simulation Workshop 2010 (SW10), OR-Society, Birmingham, 2010, pp. 108–117.

[59] D.J. Van der Zee, J.B.M. Holkenborg, Conceptual Modelling for Simulation-Based Serious Gaming, in: B. Johansson, S. Jain, J. Montoya-Torres, J. Hugan, E. Yücesan (Eds.), Proceedings of the 2010 Winter Simulation Conference, IEEE, Piscataway NJ, 2010, pp. 522–534.

[60] D.J. Van der Zee, J. Slomp, Simulation as tool for gaming and training in operations management – a case study, Journal of Simulation 3 (1) (2009) 17–28.

[61] D.J. Van der Zee, J.G.A.J. Van der Vorst, A modeling framework for supply chain simulation – opportunities for improved decision-making, Decision Sciences 36 (1) (2005) 65–95.

[62] D.J. Van der Zee, A. Pool, J. Wijngaard, Lean engineering for planning systems redesign – staff participation by simulation, in: S.J. Mason, R.R. Hill, L. Moench, O. Rose (Eds.), Proceedings of the 2008 Winter Simulation Conference, IEEE Piscataway, NJ, 2008, pp. 722–730.

[63] D.J. Van der Zee, R.J. Brooks, S. Robinson, K. Kotiadis, Conceptual Modelling: Past, Present and Future, in: S. Robinson, R.J. Brooks, K. Kotiadis, D.J. van der Zee (Eds.), Conceptual Modelling for Discrete-Event Simulation, CRC/Taylor & Francis, Boca Raton, 2010, pp. 473–490.

[64] S.P.A. Van Houten, A. Verbraeck, S. Boyson, T. Corsi, Training for today's supply chains: an introduction to the distributor game, in: M.E. Kuhl, N.M. Steiger, F.B. Armstrong, J.A. Joines (Eds.), Proceedings of the 2005 Winter Simulation Conference, IEEE, Piscateway NJ, 2005, pp. 2338–2345.

[65] M. Van Ments, The effective use of role-play. A handbook for teachers and trainers, Kogan Page, London, 1983.

![](/api/attachments/DH57M7RY/fulltext/images/395e314c9370b2e3b1cd4a704be86aecd688a9c17d7f070cae4009eb11823061.jpg)  
DURK-JOUKE VAN DER ZEE is associate professor of Operations at the Faculty of Economics and Business, University of Groningen, The Netherlands. He teaches in the areas of operations management and industrial engineering. His research interests include simulation methodology and applications, simulation and serious gaming, manufacturing planning and control, and <sup>fl</sup>exible manufacturing systems. Publications of his work can be found in leading journals, like Decision Sciences, Decision Support Systems, International Journal of Production Research, International Journal of Production Economics, Journal of Simulation, IIE Transactions, and Transportation Research B. He is a member of INFORMS-SIM and SCS.

![](/api/attachments/DH57M7RY/fulltext/images/9dce7c383c706cf3fde89cedddf85171799d41147f40b0d901c118a21ebd8e5b.jpg)

BART HOLKENBORG is a systems engineer for Topicus FINAN – Financial Analysis, Zwolle, The Netherlands. He received his MSc in Industrial Engineering & Management at the University of Groningen, The Netherlands. His research interests include simulation of business processes, including serious gaming and software development.

![](/api/attachments/DH57M7RY/fulltext/images/f427ba4bf7771f5114668059630ae5d46d842d9adcf7f6075e6d95ec3da2196c.jpg)

STEWART ROBINSON is Professor of Management Science and Associate Dean for Research at Loughborough University, School of Business and Economics. Previously employed in simulation consultancy, he supported the use of simulation in companies throughout Europe and the rest of the world. He is author/co-author of <sup>fi</sup>ve books on simulation. His research focuses on the practice of simulation model development and use. Key areas of interest are conceptual modeling, model validation, output analysis and alternative simulation methods (discrete-event, system dynamics and agent based). He has recently completed a research project that investigated the use of simulation with lean in healthcare. Professor Robinson is Vice

President of the United Kingdom Operational Research Society.

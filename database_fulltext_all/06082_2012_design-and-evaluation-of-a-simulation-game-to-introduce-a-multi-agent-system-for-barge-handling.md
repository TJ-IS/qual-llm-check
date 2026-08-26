---
otero_id: 6082
otero_key: "WGSRPGVG"
title: "Design and evaluation of a simulation game to introduce a Multi-Agent system for barge handling in a seaport"
authors: "A.M. Douma; J. van Hillegersberg; P.C. Schuur"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.02.013"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Design and evaluation of a simulation game to introduce a Multi-Agent system for barge handling in a seaport

A.M. Douma <sup>a</sup>, J. van Hillegersberg <sup>b</sup>, P.C. Schuur <sup>c,</sup>⁎

<sup>a</sup> Dinalog, Dutch Institute for Advanced Logistics, The Netherlands

<sup>b</sup> Department of Information Systems & Change Management, School of Management and Governance, University of Twente, The Netherlands

<sup>c</sup> Department of Operational Methods for Production and Logistics, School of Management and Governance, University of Twente, The Netherlands

## a r t i c l e i n f o

Article history: Received 21 January 2011 Received in revised form 17 February 2012 Accepted 28 February 2012 Available online 5 March 2012

Keywords: Multi-Agent system Simulation game Barge handling problem Port of Rotterdam

## a b s t r a c t

Multi-Agent systems have been studied extensively, but only a few of these systems are deployed in practice. Essential to get a system implemented is acceptance. In a distributed setting this is challenging, especially when one deals with multiple independent and competing companies. We share our experiences with the use of a real-time multi-player simulation game that we developed to illustrate a Multi-Agent system for the barge handling problem in the Port of Rotterdam. We experienced that the game has many advantages over a more passive approach, such as vocal presentations. We conclude that the game has considerably contributed to the acceptance of the illustrated Multi-Agent system.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Over the last decades, several studies have been performed to the potential of Multi-Agent systems for solving various problems in supply chains. However, until now only a few of these systems are deployed in practice [7]. Clearly, gaining acceptance for a solution is essential to get the system implemented, especially when a lot of independent (and even competing) actors are involved. In this paper we describe our experiences with the use of a simulation game that we developed to gain acceptance of a Multi-Agent system for the barge handling problem.

Over the past few years we have studied the barge handling problem, which is a clear example of an inter-organizational supply chain coordination problem where distributed planning offers a promising solution compared to central coordination. The barge handling problem is the problem how to optimize the alignment of barge and terminal operations in a port. Barge and terminal operators are independent companies and need to align their operations for loading and unloading containers. Barge operators have to decide on the sequence in which a barge visits the terminals and the terminals in turn have to decide on the way they schedule the visiting barges. Each of the actors has its own objectives and behaves opportunistically due to the competitive relations.

Central coordination as solution for the alignment problem seems obvious, but the terminal and barge operators are not willing to accept such a solution. The main two reasons are: i) they want to keep control over their own operations and ii) they are reluctant to share information that could undermine their competitive position [6]. We developed a distributed planning solution by means of a Multi-Agent system [9,10]. This solution meets the two requirements of the actors, namely that they can stay in control of their own operations and that they only need to share limited information.

When designing a distributed planning solution for the barge handling problem, we focused on both acceptance and optimization. We designed the system such that the conditions for participation are acceptable for future system users. Moreover, the system allows the actors to optimize their operations and obtain individual bene<sup>fi</sup>ts. This is important, because if we are able to design a highly ef<sup>fi</sup>cient system, but the system is not acceptable for the actors in practice, then it will never become effective.

However, whether future system users are willing to accept new technology is in particular depending on their perception and expectations of the system [19]. According to the Technology Assessment Model [8,18], the two main factors for users to decide on the acceptance of new technology are i) perceived usefulness and ii) perceived ease of use. Perceived usefulness is de<sup>fi</sup>ned as ‘the degree to which a person believes that using a particular system would enhance his or her job performance’ and perceived ease of use as ‘the degree to which a person believes that using a particular system would be free from effort’ [8].

When designing a solution for the barge handling problem (through a Multi-Agent system) we paid special attention to design choices that could in<sup>fl</sup>uence the acceptance of the users and the extent to which users can optimize their operations. However, when presenting the solution to practitioners we felt that it was hard for them to get a picture of how the system works in practice and whether it provides a solution they are willing to adopt and support. We therefore decided to develop a simulation game to communicate our ideas and to help future system users to get a clear picture of what the solution is about.

Through a simulation game we aim to realize the following four objectives:

1. To communicate our Multi-Agent solution to practitioners in an accessible way to help them to get a clear understanding of the system. We expect that this i) contributes to the acceptance of the solution, ii) supports a focused discussion on design choices and assumptions, and iii) supports a discussion about the conditions for implementation.

2. To use the game as a practical validation of our Multi-Agent system. For instance, how do people interpret and use the information that is provided and what does it mean for the decisions they make?

3. To use the game as a prototype solution for the user interface. For instance, is the presented information useful and is the interface intuitive and clear?

4. To evaluate the way players perceive different interaction protocols and how this affects their performance.

Our experiences reveal that a simulation game is an effective means to contribute to the ‘perceived usefulness’ and ‘perceived ease of use’ of our system by future system users.

The outline of the paper is as follows. Section 2 presents a literature review. In Section 3 we brie<sup>fl</sup>y describe the barge handling problem followed in Section 4 by a description of the game. Section 5 presents our experiences with the simulation game. In Section 6 we re<sup>fl</sup>ect on the extent to which we were able to reach the above four goals. Section 7 gives our overall conclusions.

## 2. Literature review

There is a strong relation between games and simulation. Both provide an environment to support learning or the acquisition of skills [2]. Simulations make it possible to mimic the behavior of a ‘real’ situation under the in<sup>fl</sup>uence of a set of variables that are considered to be important, whereas games stimulate competition between players within a prede<sup>fi</sup>ned set of rules [11,16]. Angelides and Paul [3] state that gaming-simulation is a sequential decision making exercise through which players can experience the consequences of their decisions rapidly in an arti<sup>fi</sup>cial environment containing some characteristics of a real situation. The aim is to enhance a comprehensive understanding of a complex system and to develop learning skills.

Although a wide range of literature has appeared on teaching effectiveness of simulations and experiential exercises, there is hardly any objective evidence to conclude that simulations and experiential exercises indeed result in learning [1,12]. It is unclear whether the perceived learning of players also means actual learning (see for further reading Gosen and Washbush [12]). On the other hand, there are many authors claiming that games do help to increase the understanding of complex situations. Wenzler and Chartier [20] state that the properties of the parts can only be understood in the dynamics of the whole. Games and simulations are a mechanism to show the big picture (Gestalt understanding) in a condensed period of time. Reducing the learning period of people from real time to simulated time, allows for steeper learning curves. Hoogewegen et al. [13] give an example of how games can contribute in understanding dynamic business networks and the effect of different strategies. Barreteau et al. [4] state that games are good at explaining the content of Multi-Agent systems. Especially for the purpose of supporting negotiations, it might be necessary to give the actors insight in the functioning of the system and discuss whether the model's assumptions match their own representation of the system dynamics and whether agents have a correct range of possible actions.

Ryan [16] claims that changing management practices requires learning skills that can be met through games. He states that problems and issues become increasingly interrelated and that, as more people become involved in decision making, priorities become less clear and implementation gets more dif<sup>fi</sup>cult. His experience is that simulation games are extremely useful in developing an appreciation of systems thinking, i.e., viewing the phenomenon under consideration as a consequence of the interaction of the system constituents. Ryan [16] states that simulation games create common experience among participants, which they can refer to when discussing the system concepts (see also [14,20]). Le Bars and Le Grusse [14] describe their experience with a simulation game and a decision support system for (collective) decision making among several actors. They show that this combination improves discussions between stakeholders and facilitates the emergence of acceptable solutions. They mention that acceptability of the solution in this case is more important than the optimal solution. A game-like setting has also been applied in an earlier study of our problem [15], where it is reported that through a game the participants start to realize the seriousness of the problem and the potential bene<sup>fi</sup>ts of an agent based system.

Acceptance of and the intention to use Information Technology have been studied widely in the scienti<sup>fi</sup>c literature. In the previous section we already mentioned the Technology Acceptance Model (TAM), a widely used model stating that the intention of a user to use information technology is determined by two beliefs: perceived usefulness and perceived ease of use [8,19]. Much evidence has been provided that supports the statements made in TAM [18]. With respect to our study this means that perception and expectation of usefulness and ease of use are important determinants for system acceptance, which are to be enhanced by our simulation game.

The brief literature overview shows that games are considered to have potential to increase the understanding of complex systems and support the discussion between stakeholders based on common experiences. Moreover, they can help users to develop their expectations of the system. Although simulation games are a promising tool to exemplify Multi-Agent systems, we only found a few contributions that really did so, namely [4,14,16]. These contributions give support for the statement that simulation games are an appropriate means to improve the understanding of the functioning of a Multi-Agent system, to create a common problem understanding, and support a focused discussion on model choices. They describe experiences in the <sup>fi</sup>eld of policy making, water management, and irrigation systems. Considering the limited number of Multi-Agent systems that are deployed in practice and the complex nature of implementing distributed planning solutions due to the many different actors involved, we are convinced that more research is needed on how to bridge the gap to practice and get Multi-Agent systems implemented.

In this paper we describe our experiences with the use of a simulation game to exemplify a Multi-Agent system in the domain of supply chain management, namely the barge handling problem in the Port of Rotterdam. The problem is considered as most urgent in hinterland container barge navigation by the Port of Rotterdam. The problem is characterized by many different players with con<sup>fl</sup>icting interests in a highly dynamic environment (we introduce the problem in the next section). Through the simulation game we aimed to realize the four goals described in the Introduction of this paper.

## 3. The barge handling problem

The barge handling problem is the problem how to align the operations of barge and terminal operators in a port, such as the Port of Rotterdam. In the Port of Rotterdam, (container) barges are an important means to transport containers between the port and the hinterland. When barges visit the port, they typically visit about eight container terminals to load and unload containers. A sequence of terminal visits is called a rotation. The sequence in which a barge visits these terminals depends on several factors, such as the availability of terminals. Terminals, on the other hand, also have their preferences when to handle a speci<sup>fi</sup>c barge. An alignment of activities is thus required.

Nowadays, barge and terminal operators try to align their operations by making appointments. These appointments are made by telephone, fax, e-mail, and a system called PortBase. Unfortunately, it frequently happens that appointments are not met by either the barge or the terminal operator. Appointments turn out to be unreliable. There are several reasons for this, like the fact that appointments are sometimes not even feasible at the time they are made or the fact that a disruption at one terminal quickly propagates to other terminals and barges. These events often require re-planning of appointments.

In the barge handling problem we deal with speci<sup>fi</sup>c business constraints. Terminals compete with each other and so do barge operators. In the Port of Rotterdam we deal with about 30 container terminals and – on a daily basis – a number of more than 60 barges visiting these terminals. Terminal and barge operators realize that they all can bene<sup>fi</sup>t from adopting IT to enhance their cooperation, but they are reluctant to do so as they fear this may undermine their competitive position. However, the problem is urgent, since it results in signi<sup>fi</sup>cant ef<sup>fi</sup>ciency losses for barge and terminal operators. Also, the Port Authority considers the problem as urgent since it affects the quality of the hinterland connections.

In the past, ideas have been proposed to establish a central trusted party to coordinate the activities of both terminals and barges. However, this has proven to be unacceptable for the stakeholders for two main reasons. First, every actor wants to stay autonomous, i.e., in control of its own operations. Second, every actor is reluctant to share information as it fears that others will use this information to improve their competitive position.

To provide an acceptable solution, we developed a system based on distributed planning (a so-called Multi-Agent system). The system is designed such that conditions for participation are acceptable for all players and still the system enables them to organize their operations ef<sup>fi</sup>ciently. Starting point is that players stay autonomous and share limited information. This is realized by providing an agent for every barge operator and every terminal operator. This agent is a piece of software and is supposed to act in the best interest of the actor it represents. The agents communicate with each other to align their activities. Agents use an interaction protocol for communication. In this protocol (based on so-called service-time pro<sup>fi</sup>les) only limited information is shared, but enough to enable barge and terminal operators to organize their operations ef<sup>fi</sup>ciently. For more information on the interaction protocol, the Multi-Agent system, and extensive simulation results we refer to [9,10].

Clearly, to let the system become effective, it has to be accepted by at least a critical mass of terminal and barge operators. Users need to get a sound understanding of the functioning of the system. In particular, they need to get a clear picture of the extent of autonomy they have in the system to decide on their own operations and the amount of information that is shared. These two aspects relate to the key elements in a Multi-Agent system, namely the agent intelligence and the interaction protocol. The game is designed to allow players to play the role of the barge operator agent and to let them experience different interaction protocols.

## 4. Game description

In this section we give a description of the game. We describe successively the game setting and typology, the role and task of the player, the course of the game, different scenarios, the user interface, the game architecture, and choices to reduce the complexity of the game.

## 4.1. Game setting and typology

The game setting (or scope of the game) is a port with a variable number of terminals. Barges have to visit (a subset of) these terminals to load and unload containers. All barges enter and leave the port via the same waterway. This waterway also determines the start and end point of the game. Players have to take a role in the game. Speci<sup>fi</sup>cally, we focus on a particular stakeholder within the system, namely the barge operator. The game is industry speci<sup>fi</sup>c, namely for the barge handling problem in a port, and is a functional game as we focus on the planning discipline within (terminal and) barge operator companies (see also [2]).

## 4.2. Role and task of the player

In the game the player gets the role of barge operator planner. The terminal operator role is taken care of by the computer. The task of the player is to plan a rotation (sequence of terminal visits) along the terminals in the port that (s)he has to visit. Aim of each player is to minimize the turn-around time of his/her barge in the port, i.e., to plan the terminal visits such that the barge leaves the port as soon as possible. How visits along terminals have to be planned differs per game scenario. We describe the game scenarios in Section 4.4. Since multiple players make decisions simultaneously, they in<sup>fl</sup>uence each other's possibilities to be handled at a terminal.

## 4.3. Course of the game

The course of the game is as follows. All barges start at the entrance of the port. Before the game starts, all players receive a similar assignment, namely a set of terminals that have to be visited. The assignments of players differ but are equal in dif<sup>fi</sup>culty. Players can begin to plan a terminal rotation as soon as the game leader has started the game. From then on, the game proceeds with a constant clock speed and performs a simulation based on the decisions all players make. Players can make and reconsider their decisions until the game ends.

During the game, players can see a map of the port (including all the terminals) on their computer screen (see Fig. 1 and Section 4.5). On this map players can also see the ships of other players sailing. We divide the time horizon in time slots of equal length. Handling of a barge at a terminal takes one time slot. The duration of the handling may not be realistic, for instance when a time slot corresponds with 15 min handling time. However, for the purpose of this game our choice suf<sup>fi</sup>ces. Moreover, it is fair that the handling at each terminal takes an equal amount of time for all players. Whether the players get information about free time slots at the terminal depends on the scenario that is played (see Section 4.4).

Planning a rotation means that players indicate in which sequence they want to visit their terminals and, depending on the scenario played, at what time they want to have their appointments. In Section 4.4 we discuss the different scenarios in detail. As soon as a player has decided on the <sup>fi</sup>rst terminal to visit, his/her barge starts to sail to this terminal. A player can always make up his/her mind and decide that the barge should head to another terminal, as long as the barge has not yet arrived or is not being handled at a terminal.

On arrival at a terminal the barge queues and waits for handling. When the barge has been processed by the terminal, the player gets a noti<sup>fi</sup>cation and the corresponding time slot turns blue (c.f. Fig. 1). After the handling has been completed, the barge immediately heads to the next planned terminal. On arrival at this terminal the barge again enters the queue and waits for handling.

![](/api/attachments/WGSRPGVG/fulltext/images/f1c724339915424ce3774c8fb0009d82526e1f5f561cf794144f790d17794c34.jpg)  
Fig. 1. Screen shot of the user interface.

After all terminals have been visited and the handling at all terminals has been completed, the barge automatically heads back to the entrance of the port which is also the end point of the game. On arrival at the end point, the barge's arrival time is logged and the player has completed his task. The game server sends the player a message on his ranking. The game ends when the game leader stops the game (for instance after there is a winner) or when the time for a game round is over.

## 4.4. Scenarios

In the game we can play four scenarios, which are constructed based on i) the amount of information that is exchanged about the occupation of the terminals and ii) whether players can make appointments with terminals. Let us describe the four scenarios.

Scenario 1 First-come first-served, no waiting information on arrival at a terminal

This is the most basic scenario in which the players make no appointments with terminals and also get no information about the occupation of a terminal. Barges are processed <sup>fi</sup>rst-come <sup>fi</sup>rst-served at a terminal. The player in fact only decides on the sequence in which terminals are visited.

Scenario 2 First-come first-served, with waiting information on arrival at a terminal

In this scenario barges are again processed <sup>fi</sup>rst-come <sup>fi</sup>rst-served, but on arrival in the queue of a terminal they get information on the length of the queue, i.e., the number of time slots a barge has to wait before it will be processed. As soon as the player leaves a terminal (s)he has no insight anymore in the queue length of that terminal. Players can always decide to leave the queue and go to another terminal.

Scenario 3 Appointments, limited information of occupation of the terminal

Players are processed based on appointments with the terminals. To get an appointment with a particular terminal operator, the player has to send a request for a particular time slot to the terminal operator. A terminal operator replies to a barge with ‘yes’ or ‘no’ whether the request has been accepted. If a request is rejected, the player has to send a new proposal until a time slot is accepted. In this way players get fragmentary insight in the occupation of a terminal, which is comparable to practice.

Scenario 4 Appointments, full information of occupation of the terminal The last scenario resembles our solution to the barge handling problem. Players again have to make appointments with terminals. However, this time they get insight in the occupation of the terminal during the day. On screen the player can see which time slots are available. In this way the player has more insight in the waiting time at terminals and has more information to plan a rotation. Note that a time slot that appears to be free at the moment the decision is contemplated, may be occupied at the actual time of request due to decisions of other players. Moreover, the availability of a terminal changes over time through the actions of other players.

Note that scenarios 1 to 3 resemble each to a certain extent the current situation. The current situation is a combination of scenarios 1 to 3, since in practice appointments are made but barges are not always processed according to these appointments. Moreover, barge operators usually have no or limited insight in the length of the queue at terminals. Scenario 4 resembles the solution we propose in [9].

In case a terminal makes an appointment, it applies the following policy:

\- When making an appointment a barge is added to the schedule of the terminal. Barges waiting in the queue, are processed according to this schedule.

\- If a player has made an appointment and arrives late at the terminal, then the appointment is cancelled and a new appointment has to be made. A barge is not processed without an appointment.

\- If a terminal is idle then it looks in the queue whether one of the next planned barges is already waiting. If so, then the <sup>fi</sup>rst planned barge (waiting in the queue) is processed during the idle time slot. If no barge is waiting (or no barge with an appointment) then the terminal leaves the time slot idle.

Requests to the terminal are answered with a random (con<sup>fi</sup>gurable) delay. We do so to prevent that players quickly evaluate many time slots. Moreover, each request constitutes a burden for the terminal operator agent and also in practice the terminal operator might need some time to send a reply. In the game we can play each of the four scenarios separately or in combination, by letting one part of the group play scenario 1 and the other part scenario 2, or one part plays scenario 3 and another part scenario 4.

## 4.5. User interface

The user interface consists of three parts (see Fig. 1). The upper left part is a graphical representation of the game state, depicting the location of all the barges and terminals. The upper right part of the screen presents the performance of the barge. The lower part is reserved to plan a rotation. In this part of the screen a time bar is given for every terminal the player has to visit. This time bar is divided in time slots. The player can select a time slot by clicking on the speci<sup>fi</sup>c time slot. The selected time slots can be communicated with the terminals by clicking the button on the left bottom corner of the screen. As long as the player has not pushed this button, the plan is just a proposal made by the player and not communicated to the game server (and the terminals).

The red vertical line in the lower part of the screen denotes the progress of time and the black vertical line the time before which the player has to complete his/her activities. As soon as the processing of a barge has been completed, the corresponding time slot turns blue. Time slots denied by the terminal turn red and approved time slots turn green. Proposed (and not communicated) time slots are depicted as grey.

In the time bars we can depict waiting pro<sup>fi</sup>les as shown in Fig. 2. This is done only in scenario 4. Waiting pro<sup>fi</sup>les are depicted on a logarithmic scale and show the maximum number of time slots a barge has to wait before it can be processed.

## 4.6. Design choices to reduce complexity

Recall that through the game we aim to illustrate the functioning of a Multi-Agent system for the barge handling problem. In particular, we are interested in how players make their decisions and deal with the information issued by the terminals in each of the scenarios. We simpli<sup>fi</sup>ed the game as much as possible to help players to quickly get an understanding of the basic concepts in the Multi-Agent system and not to bother players with details that could distract them from what we aim to make clear. For similar considerations we refer to [4]. Moreover, Ben-Zvi [5] found that when game complexity increases, perceived usefulness and user satisfaction may start to decrease. Hence a multifaceted game does not guarantee a better outcome. We made the following simpli<sup>fi</sup>cations.

Each player has to plan a rotation for only one barge. The terminal operator role is taken care of by the computer to guarantee a quick and equal response to the players. Recall that we divide the time horizon in time slots of equal length. The game speed is determined by the number of time slots per minute. The handling time for all barges at a terminal takes one time slot. Sailing times are determined based on the shortest (sailable) path between terminals. The sailing speed is equal for all players during the game. All players enter and leave the port via the same entrance and exit point. Terminals have no restricted opening times. We can therefore use a simpli<sup>fi</sup>ed version of service-time pro<sup>fi</sup>les, namely waiting pro<sup>fi</sup>les [9]. When playing scenario 4, we do not add slack to the waiting pro<sup>fi</sup>le as we did in [9]. All terminals in the game have one quay and can process one barge at a time. Different from the reality of the Port of Rotterdam, terminals do not handle sea vessels, but instead we can block time slots for barge handling randomly on initialization of the game.

The following parameters can be con<sup>fi</sup>gured on initialization of the game:

\- Layout of the network

\- Total number of terminals in the port

\- Length of the planning horizon

\- Number of time slots in the planning horizon

\- Number of players

\- Number of terminals the players have to visit

\- Speed of the simulation

\- Sailing speed of the barges

\- Delay in the response of the terminal after a request of the barge

\- Fraction of time slots that are blocked randomly to decrease terminal availability and to increase the game complexity

\- Which scenario is played (scenario 1, 2, 3, or 4, or certain combinations).

The reason why we block time slots randomly on initialization of the game is to realize a realistic utilization degree of the terminals. How the time horizon is divided in time slots is con<sup>fi</sup>gurable, but suppose that we have played the game with about 96 time slots (four time slots per hour in a 24 h time period). If we do not block time slots and we play the game with about ten players, then, per terminal, at most ten time slots during a planning horizon are required for handling. In that case the utilization of the terminals is unrealistically low (in our case about 10%) as well as the game complexity.

At the start of the game we hand out a <sup>fl</sup>ag to each player. When logging-on the game, a player has to select the user-id that corresponds with his/her <sup>fl</sup>ag. The <sup>fl</sup>ags are a nice feature of the game, since they help players to recognize each other's barge. Moreover, the <sup>fl</sup>ags enhance the sense of reality. Last but not least, they cheer up the game room.

## 5. Experiences and evaluation

Over the last three years we have played the game at more than seven occasions with different groups of people, varying from students to practitioners. Among the practitioners were terminal operators, barge operators, consultants, and people from the Port Authority. In this section we describe our experience with the game in two workshops. In workshop 1 we played the game with managing directors of barge operators and in workshop 2 we played the game with barge operator planners. We pick these two workshops, since we played the game in both workshops with part of our target group, namely practitioners that deal with the barge handling problem daily. This gave us the opportunity to evaluate whether the game meets the aims we wanted to achieve (see Section 1). Each of the workshops lasted for about three hours. Unfortunately, in these

Terminal 1

![](/api/attachments/WGSRPGVG/fulltext/images/c0ea999292ad38d0ffe13bc13c1aef82358b444affdb4b457c148c1b545bd1d8.jpg)  
Fig. 2. Example of a waiting pro<sup>fi</sup>le depicted in the time bar of a terminal. The time is depicted on the horizontal axis and the (logarithmic) maximum waiting time on the vertical axis.

two workshops no terminal operator participated. In that stage of the project, playing the game with this part of the target group was already a great step.

## 5.1. Workshop 1

In January 2009 we organized an event to inform managing directors of <sup>fi</sup>ve large barge operators in The Netherlands about the results of our study on the barge handling problem. One of the aims of the workshop was to get support from the barge operators for implementation of our study in practice. Let us describe the setup of the event and our experiences with the game.

## 5.1.1. Setup of the game workshop

The workshop started with an introduction of the barge handling problem and an explanation of how we perceived the problem. We then introduced the concept of a Multi-Agent system and explained the reasons for this approach compared to central coordination. After that we introduced the game by explaining the role of the players, the user interface, and the <sup>fi</sup>rst round. We played three rounds with scenarios 1, 3, and 4, respectively. Players were informed about the number of rounds we played, but we introduced the rounds one after the other. This means that players were not aware of which rounds they were going to play.

After playing all three rounds we had a discussion with the participants on their experiences.

## 5.1.2. Experiences

During the game we observed the following. All players could easily work with the user interface. Players quickly adopted their role as barge operator planner and all players enjoyed playing the game.

During the discussion afterwards we got some striking remarks. One managing director mentioned that, when coming to the workshop, he did not expect to see a solution to the barge handling problem that day. During the introduction of the problem his expectations went down. His expectations decreased even further after playing scenario 1 and 3. But when playing scenario 4 he thought: this is what we need. After the game he was enthusiastic about the solution we developed. This experience was shared by other managing directors. All participants were aware of the fact that the game simpli<sup>fi</sup>ed the current situation, but they considered it as a promising basis for a solution.

Although the participants had dif<sup>fi</sup>culty to understand the role of the agent, they obtained (in a very short period of time) an understanding of the way the system functions, the information that is exchanged and the bene<sup>fi</sup>ts of the Multi-Agent system, being that everyone can make decisions autonomously and without sharing much information.

After the discussion we explained our assumptions and choices, but this did not have as much impact as the game experience. At this meeting the directors declared that they were interested in further research to the implementation of our solution in practice. A few months later we started a feasibility study with these barge operators to investigate whether and how implementation of the system is feasible.

## 5.2. Workshop 2

In April 2010 we organized a workshop for barge operator planners of <sup>fi</sup>ve large barge operators in The Netherlands. The aim of the event was to inform the planners about the solution we developed for the barge handling problem. On this event also two managing directors of barge operators (who participated in the <sup>fi</sup>rst workshop) were present, but they only made observations. The managing directors purposely did not inform their planners about the solution. They wanted their planners to give their own opinion about the solution.

The response of the planners was important for the managing direc tors to decide on their support for implementation of the system. Let us describe the setup of the event and our experiences with the game.

## 5.2.1. Setup of the game workshop

The setup of the workshop was similar to the workshop with the managing directors. We started again with an introduction of the barge handling problem. This took quite some time, since the planners wanted to react, share their experiences, and give their view on the problem. However, they all agreed on the way we described the problem. After that we brie<sup>fl</sup>y introduced the concept of Multi-Agent system and explained the reasons for this approach compared to central coordination. The introduction of the game was similar to the workshop with the managing directors.

After playing all three rounds we had a discussion with the participants on their experiences. In this discussion also the managing di rectors participated.

## 5.2.2. Experiences

The planners indicated at the start of the workshop that they feared that the system would take over their jobs. They were interested but not enthusiastic to hear about our solution. During the game we made the following observations. Several barge operator planners were playing the game as if they had to plan the ships in reality. They made their decisions and started to look what other players did. The simpli<sup>fi</sup>cations we made were not a barrier for them to understand the basic notions of the Multi-Agent system. A few planners needed some help to understand how the interface worked. The planners enjoyed playing the game.

After the game we had some discussions. Planners said they had become enthusiastic about the solution we presented. They had seen many solutions and had low expectations, but after playing the game they spoke about ‘sparks of hope’. Although the system would replace parts of their tasks, they expected that their job could become more interesting as they would have better tools and information to make their planning decisions. Moreover, automating the routine tasks leaves time for more interesting, non-routine tasks that require expert insight of the planners.

What they valued especially was the information on the availability of terminals (scenario 4) and the position of ships in the port. Currently, they lack this information which makes them dependent on information of the barge shippers. Moreover, the lack of information hinders them to optimize the barge rotations. The remaining part of the discussion was about preconditions that have to be met as well as practical aspects that have to be addressed. This discussion was valuable, since participants could give detailed and pointed feedback.

Planners indicated that through the game they had a better understanding of how the system works, the information that is exchanged, and the way they can make their decisions.

## 5.3. General observations

During discussions with managing directors and the barge operator planners we made the following observations. Through the game we got detailed and focused discussions about the Multi-Agent system, assumptions we made, practical issues that have to be addressed, et cetera. Feedback at this level of detail we did not get during sessions in which we only explained the system by means of a presentation. People were able, as we experienced, to quickly understand the concepts behind the Multi-Agent system and the interaction protocol. Through the interaction of the decisions of all the players they could see the dynamics of the system as a whole.

We experienced that people were able to think about applying the system in practice and how it would impact their daily work. Both groups of people also realized that this system would result in a different job content of the planners, less attention to routine tasks that can easily be automated, and an attention shift to the relationship with the terminals and non-routine tasks that require speci<sup>fi</sup>c knowledge and experience of planners.

We were surprised how people changed their attitude towards the system after playing the game. For most of the participants it seemed that experiencing the solution had a much greater impact than through only vocal or written presentations of the solution.

## 5.4. Experiences with developing the game

Developing a real-time multi-player simulation game is technically challenging, due to the many events that take place and that have to be synchronized for all players in the game. Playing the game requires stable network connections, to prevent that a client loses the connection with the server and stops functioning. We experienced that, despite extensive tests, small bugs still popped-up and disturbed the playing of the game. Players experience a (small) bug as very negative, especially when it gives them a disadvantage while playing the game or even forces them to quit the game round.

We consider the risk of failing of the game as a threat. We experienced through all the workshops that failing of the game may be caused by a variety of factors, varying from instable network connections, through unexpected user actions, and (small) bugs. The risk of failing is much higher than when playing a board game. We therefore decided eventually to play the game only at our own network, which was stable and could be tested well. The reason was that players usually have high expectations of playing a game and are not very patient when it does not work. This also determines the image they have of the illustrated system. Developing a bug-free and fool-proof game takes time and requires extensive testing with non-experienced users in order to experience as many combinations of events as possible.

Another challenge is to <sup>fi</sup>nd a balance between complexity and the extent of realism of the simulation. We chose, for instance, to use an abstract picture of a port area to manage the expectations of the users. Users should be aware that the game illustrates the Multi-Agent system at a high level and does not, e.g., consider tides, ship stowage, restricted opening times of terminals, and so on. We experienced that this worked out well.

## 6. Discussion

In Section 1 we described the goals we aimed to reach by means of the simulation game. In this section we re<sup>fl</sup>ect on the extent to which we were able to reach these four goals successively. In our re<sup>fl</sup>ection we combine the experiences of all the workshops we organized.

With respect to our <sup>fi</sup>rst goal we experienced that the game is a useful tool to communicate the functioning of a Multi-Agent system to practitioners. Within a few minutes people get a clear understanding of how the system works and they are able to re<sup>fl</sup>ect on the solution and the choices and assumptions made. Also, playing the game gives food for a focused discussion afterwards. We got more detailed feedback than when we explained our solution using a vocal presentation only. Moreover, people responded with greater enthusiasm after playing the game than after a vocal presentation only. Through the game, players were able to understand the properties of the parts in the dynamics of the whole (see also [20]).

With respect to our second goal we found that the game was especially helpful to see how people make decisions. We were surprised to see how people change their way of decision making depending on the information they have (we re<sup>fl</sup>ect on this when discussing our fourth goal). The game was not useful to validate the simulation results or to prove that one interaction protocol resulted in lower average turn-around times. One reason is that people have to process all the information themselves and do not always make the best decisions possible. Another reason is that we did not play the game often enough with the same players to get statistically signi<sup>fi</sup>cant results.

Our third goal is related to the user interface. We experienced that the players usually have no dif<sup>fi</sup>culty to work with the interface. Both barge operator directors and planners value the fact that an overview of the port was given with all ships sailing, as well as the waiting pro-<sup>fi</sup>le information. This information is important for them to make better planning decisions. In a feasibility study we continued developing the user interface of the barge operator agent based on the game interface [17]. We found that the game is a nice way to prototype the user interface and to create an understanding by practitioners about the way they can use this interface.

The game was also useful to evaluate how players perceived different interaction protocols. When we provide no information about the occupation of terminals, we see that players become passive in the sense that they plan a rotation and hardly ever change it. The reason is that they do not have any information to decide upon. When players can ask a terminal whether a time slot is available (scenario 3), we see that players start to plan and re-plan a rotation. After some time it becomes harder to get a time slot (due to the actions of other players) and players are then more quickly satis<sup>fi</sup>ed with just a feasible rotation. When we provide waiting pro<sup>fi</sup>les (scenario 4) we <sup>fi</sup>nd that players have to process a lot of information. They have more opportunities to optimize their rotation (since they have more information), but it is quite demanding to process this information (although, in the game settings offered, players only have to plan <sup>fi</sup>ve terminals). This is even more so when playing the game under a high time pressure. The fact that actions of others frequently force a player to re-plan, makes this information processing task even more cumbersome. However, in a practical implementation, agents can help to pre-process information and to support (or take over) the decisions of the planners.

Last but not least, although the game was not developed for educational purposes, we experienced that the game was also useful in that respect. It provides students a view on how barge handling activities are organized in the Port of Rotterdam and it helps them to quickly get an understanding of the idea behind and the potential of a distributed planning system.

## 7. Conclusions

We described our experiences with the use of a simulation game to exemplify a Multi-Agent system. We designed a game for a speci<sup>fi</sup>c case, namely the barge handling problem which is the problem to align barge and terminal operations in a port. In the problem we deal with multiple independent players that have to communicate to align their interests. In an earlier study we developed a Multi-Agent system solution for the problem. However, when presenting the solution to practitioners we felt that it was hard for them to get a picture of how the system would work in practice and whether it provides a solution they are willing to adopt and give support for. We therefore decided to develop a simulation game to communicate our ideas.

With the game we tried to achieve four goals, namely i) to communicate our solution to practitioners, ii) to practically validate the Multi-Agent system, iii) to prototype the user interface, and iv) to evaluate the way players perceive different interaction protocols. In the paper we described the design of the game and the choices we made. We concluded with a description of our experiences in two workshops with practitioners and a discussion on the extent to which our goals are realized.

We conclude that a simulation game has many advantages for communicating a Multi-Agent system to practitioners. It helps people to quickly get an understanding of the system and to decide whether they are willing to give support for implementation. The game is also useful as prototyping technique for the user interface and to evaluate the way players perceive the different interaction protocols. To practically validate the performance of the Multi-Agent system, the game is less useful, unless players are trained in playing the game and play the game in multiple rounds to get statistically signi<sup>fi</sup>cant results. This was beyond the scope of our research.

A drawback of real-time multi-player simulation games is that there are many factors that may cause the system to fail, varying from instable network connections, through illegal user actions, to (small) bugs. Players usually have high expectations when playing the game. When the game does not perform well, then they assess this as very negative which impacts the image of the game organizer negatively. They may easily conclude that the game was not well prepared or, even worse, that the exempli<sup>fi</sup>ed system is not worth implementing. Since the game is clearly a communication tool, we therefore expect that extensive testing certainly pays off.

As stated in Section 2, simulation games that exemplify Multi-Agent systems are rarely found in the literature. They con<sup>fi</sup>ne themselves to <sup>fi</sup>elds as policy making, water management and irrigation systems. The contribution of this paper is that it describes a realtime multi-player simulation game which illustrates a Multi-Agent system for a complex logistical system with many different actors with con<sup>fl</sup>icting interests. By letting representatives of these actors play the game, we create mutual understanding on multiple levels. Playing the game with different scenarios, the players learn to appreciate the value of an adequate protocol for information exchange. One of the developments in supply chain management that gains increasing attention (see, e.g., the Dutch national innovation programs in logistics and supply chains) is the alignment (or coordination) of activities and interests of the various members in the supply chain. Part of the coordination in the chain may be done centrally, but it is likely that a large part will be organized through distributed planning. Simulation games as discussed in this paper provide an effective way to communicate distributed planning solutions with supply chain players and to see the merits of such solutions, which may accelerate their acceptance.

We are convinced that without the game we would not have been able to get the support of practitioners to make next steps towards implementation. The game has paved the road to acceptance of the system.

## Acknowledgments

This research has been partly funded by Transumo. Transumo (TRANsition to SUstainable MObility) is a Dutch platform for companies, governments and knowledge institutes that cooperate in the development of knowledge with regard to sustainable mobility.

## References

[1] P. Anderson, H.M. Cannon, D. Malik, P. Thavikulwat, Games as instruments of assessment: a framework for evaluation, Developments in Business Simulation and Experiential Learning 25 (1998) 31-39

[2] M.C. Angelides, R.J. Paul, Developing an intelligent tutoring system for a business simulation game, Simulation Practice and Theory 1 (1993) 109–135.

[3] M.C. Angelides, R.J. Paul, A methodology for speci<sup>fi</sup>c, total enterprise, role-playing, intelligent gaming-simulation environment development, Decision Support Systems 25 (1999) 89–108.

[4] O. Barreteau, F. Bousquet, J.M. Attonaty, Role playing games for opening the black box of multi-agent systems: method and lessons of its application to Senegal

River Valley irrigated systems, Journal of Arti<sup>fi</sup>cial Societies and Social Simulation (2001) 4.

[5] T. Ben-Zvi, The ef<sup>fi</sup>cacy of business simulation games in creating Decision Support Systems: an experimental investigation, Decision Support Systems 49 (2010) 61–69.

[6] Connekt, Eindrapport APPROACH, Delft (in Dutch), Connekt, , 2003.

[7] P. Davidsson, L. Henesey, L. Ramstedt, J. Törnquist, F. Wernstedt, An analysis of agent-based approaches to transport logistics, Transportation Research Part C 13 (2005) 255–271.

[8] F.D. Davis, R.P. Bagozzi, P.R. Warshaw, User acceptance of computer technology: a comparison of two theoretical models, Management Science 35 (1989) 982–1003.

[9] A.M. Douma, J.M.J. Schutten, P.C. Schuur, Waiting pro<sup>fi</sup>les: an ef<sup>fi</sup>cient protocol for enabling distributed planning of container barge rotations along terminals in the Port of Rotterdam, Transportation Research Part C 17 (2009) 133–148.

[10] A.M. Douma, P.C. Schuur, J.M.J. Schutten, Aligning barge and terminal operations using service-time pro<sup>fi</sup>les, Flexible Services and Manufacturing Journal 23 (4) (2011) 385–421.

[11] H. Ellington, E. Addenall, F. Percival, A Handbook of Game Design, Kogan Page, London, 1982.

[12] J. Gosen, J. Washbush, A review of scholarship on assessing experiential learning effectiveness, Simulation Gaming 35 (2004) 270–293.

[13] M.R. Hoogewegen, D. van Liere, P.H.M. Vervest, L. Hagdorn, I. de Lepper, Strategizing for mass customization by playing the business network game, Decision Support Systems 42 (2006) 1402–1412.

[14] M. Le Bars, P. Le Grusse, Use of a decision support system and a simulation game to help collective decision-making in water management, Computers and Electronic in Agriculture 62 (2008) 182–189.

[15] H.M. Moonen, B. van de Rakt, I. Miller, J. van Nunen, J. van Hillegersberg, Agent technology supports inter-organizational planning in the port, in: R.B.M. de Koster, W. Delfmann (Eds.), Managing Supply Chains — Challenges and Opportunities, Copenhagen Business School Press, Copenhagen, 2007.

[16] T. Ryan, The role of simulation gaming in policy-making, Systems Research and Behavioral Science 17 (2000) 359–364.

[17] J. Van Hillegersberg, A.M. Douma, M.E. Iacob, C.P. Katsma, S.M. Eckartz, E.J.A. Folmer, PAT: planning apart together. Een systeem voor afstemming van binnenvaart en terminal activiteiten in de haven van Rotterdam, Feasibility study (in Dutch), University of Twente, , 2009.

[18] V. Venkatesh, H. Bala, Technology acceptance model 3 and a research agenda on interventions Decision Sciences 39 (2008) 273-315

[19] V. Venkatesh, M.G. Morris, G.B. Davis, F.D. Davis, User acceptance of information technology: toward a uni<sup>fi</sup>ed view, MIS Quarterly 27 (2003) 425–478.

[20] I. Wenzler, D. Chartier, Why do we bother with games and simulations: an organizational learning perspective, Simulation and Gaming 30 (1999) 375–384.

Albert M. Douma. Until February 2011, Albert Douma was employed as a researcher at the School of Management and Governance at the University ofTwente, The Netherlands. From this university he received a PhD in Industrial Engineering, and an MSc in Industrial Engineering & Management and in Business Information Technology. His research interests are in the <sup>fi</sup>elds of supply chain management, business information systems, and economics and include Multi-Agent systems, logistics, collaboration in supply chains, production planning, pricing in freight transport, multi-modal networks, simulation, serious gaming, main ports, change management, and simulation. He is currently employed by the Dutch Institute of Advanced Logistics (Dinalog).

Jos van Hillegersberg is a full Professor in the Department of Information Systems and Change Management, School of Management and Governance at the University of Twente. Before joining this University, he was on the faculty of the Rotterdam School of Management at the Erasmus University for 15 years, working on component based software systems, IT management, global outsourcing and agent systems for supply chains. He also worked for several years in business. At AEGON he was component manager for the setup of an Internet Bank. He worked at IBM on arti<sup>fi</sup>cial intelligence and expert systems. He is currently running several projects on improving collaboration in business networks using innovative ICT such as agent technology

Peter C. Schuur is Associate Professor at the School of Management and Governance at the University of Twente, The Netherlands. He received a PhD in Mathematical Physics from the University of Utrecht, The Netherlands. On the theoretical side his research interests are on: packing, covering and cutting problems, as well as the fundamental of simulated annealing. On the applied side his research interests are on (closed loop) supply chain management, including vehicle routing, distributed planning, reverse logistics, layout problems, and warehouse modelling.

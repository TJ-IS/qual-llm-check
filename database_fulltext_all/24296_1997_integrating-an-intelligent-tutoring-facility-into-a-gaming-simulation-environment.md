---
otero_id: 24296
otero_key: "S7F3GH7E"
title: "Integrating an intelligent tutoring facility into a gaming simulation environment"
authors: "Julika Siemer; Marios C Angelides"
year: "1997"
journal: "Journal of Information Technology"
doi: "10.1080/026839697345071"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Journal of Information Technology (1997) 12, 207–222

# Integrating an intelligent tutoring facility into a gaming simulation environment

JULIKA SIEMER AND MARIOS C. ANGELIDES
Information Systems Department, London School of Economics, London WC2A 2AE, UK

Gaming simulations and intelligent tutoring systems are both substantive research and development areas within the field of computer-based education and training which have the potential for mutual enhancement. This paper argues that the pedagogical effectiveness of gaming simulations can be increased through the integration of an intelligent tutoring facility and examines possible roles for such support within a gaming simulation environment. It then commences to present INTUITION, the implementation of the Metal Box Business Simulation game, that illustrates how an intelligent tutoring facility may be integrated within a gaming simulation environment in order to increase its educational value.

## Introduction

Gaming simulation has recently gained considerable popularity as a tool for education and training both in industrial and academic environments (Lardinois, 1989; Schlecher et al., 1992; Angelides and Paul, 1993; Lane, 1995). Gaming simulations promote interest and motivation, present information and principles, put players into situations in which they must articulate positions, ideas, arguments or facts they have previously learned, or train them in skills they will later need. A gaming simulation is a sequential decision-making exercise with the basic function of providing an artificial but realistic environment that enables players to experience the consequences of their decisions through immediate response. Its objective is to enhance a comprehensive understanding of complex systems and to communicate and develop knowledge and skills.

Doukidis and Angelides (1994) classified systems that exhibit learning capabilities into categories of systems that apply different learning approaches such as learning by instructions, learning by analogy, and learning by examples. With gaming simulations, however, the players or trainees learn by performance. Therefore, one problem that often arises with simulation games is the lack of sufficient conceptual ability on the part of the player to manipulate the simulation game in order to gain the best insight into the processes and procedures involved. Intelligent tutoring systems, however, promise to enrich the learning opportunities for players by offering a wider scope for intellectual exploration through individualized player guidance and support within the learning environment. Therefore, to be completely effective as a teaching or learning tool, a gaming simulation should be supported by intelligent tutoring (Angelides and Paul, 1993).

The purpose of this paper is to illustrate how an intelligent tutoring facility can help a gaming simulation environment overcome its major weaknesses. The paper starts with an illustration of why and how an intelligent tutoring facility may support a gaming simulation. In order to illustrate how such an intelligent tutoring facility can be implemented for a gaming simulation, the implementation of INTUITION (Intelligent TUITION) is then presented and examined as a system which has resulted from the integration of an intelligent tutoring facility into a gaming simulation environment to overcome its weaknesses.

## Gaming simulations and intelligent tutoring

Gaming simulation is an important pedagogical tool for accomplishing learning. However, as an educational tool gaming simulations follow the concept of discovery learning and, therefore, do not necessarily support any direct educational aim. Gaming simulations provide the player with the opportunity to develop the skills of hypothesis testing, logic, and inductive and deductive reasoning. However, the player is usually simply put in a position where learning takes place through experimentation with a model allowing them to explore the rules of cause and effect without any helpful and individualized guidance. The original version of the Metal Box Business Simulation game, for example, aims to teach managerial skills to students through experience during game play. However, the game lacks any adaptability to the student since the students are merely provided with a business environment in which they have to direct and organize the game play themselves. As a consequence the students are left to allocate their own rules. Furthermore, unfamiliar management tasks, such as pursuing sensible market research, are often avoided rather than attempted due to lack of student support and encouragement, and feedback about student mistakes is restricted to the reaction of the market and lacks any further remedial explanation or advice. Since the major objective of intelligent tutoring systems is to make the teaching process more adaptable to the individual player, this paper therefore suggests that gaming simulation environments should be supported by an intelligent tutoring facility to be fully effective as a teaching tool.

Intelligent tutoring systems provide helpful guidance and make the teaching process more adaptable to the player by exploring and understanding the individual player and their special needs and interests and by responding to these as a human teacher does (Angelides and Doukidis, 1990; Winkels, 1992). For this purpose, intelligent tutoring systems make use of their domain model, an explicit representation of the domain-specific knowledge and the problem-solving knowledge of the topic which they intend to teach the player. At the same time intelligent tutoring systems are equipped with teaching expertise contained in their tutoring model (Halff, 1988). They have the ability to determine the users' current knowledge state, their missing conceptions and their misconceptions within the teaching domain. They achieve this by collecting feedback from the user during the course of the interaction and by being able to analyse this feedback against a wide range of predefined user behaviours. All of the information about the student is stored in the student model (VanLehn, 1988). This enables the intelligent tutoring system to tailor its instruction according to the needs of the individual student. Most intelligent tutoring systems are also equipped with the ability to help their users clear away any misconceptions and acquire any 'missing conceptions' (for a detailed description of intelligent tutoring systems see Appendix A).

These characteristics of an intelligent tutoring system could therefore be useful in assisting gaming simulation players with their decision making. They could foster the players' learning as well as monitor and provide feedback on their behaviour and performance during game play (Elsom-Cook, 1991).

In order to determine more precisely any possible functions for an intelligent tutoring facility within a gaming simulation environment the following sections discuss the four major operations that are involved in running a simulation game and make suggestions about what an intelligent tutoring facility could offer for each of them in order to improve them.

## The function of an intelligent tutoring facility during game play

The four major standard operations that have to be performed in the context of any game are (1) the preparation for running the game, (2) the introduction to the game, (3) the operation of the game, and (4) the post-game critique (a detailed description of gaming simulations can be found in Appendix B). Each of these operations may involve a range of steps to be performed. The exact number, kind and sequence of the steps involved as part of each operation may vary between different games. However, the following list of steps claims to include all possible steps and suggests how they may be supported by an intelligent tutoring facility (Angelides and Paul, 1993).

## Preparation for running the game

The first operation involves all the activities necessary before the game can commence.

(1) A game has to be selected from a set of available games according to the current teaching aims. An intelligent tutoring facility could decide on the appropriateness of a game on the basis of the teaching goals that are currently set for the players. These teaching goals may be retrieved from the tutoring model. Alternatively, the system may simply examine the context of the student models of the players in order to choose a game or the level of advancement for a particular game.

(2) The game has to be integrated into the overall teaching curriculum. An intelligent tutoring facility could relate the game to the rest of its embedded curriculum by preparing explanations about its reasons for choosing a game, e.g. to satisfy certain pedagogical goals.

(3) The system has to be familiar with the game. An intelligent tutoring facility could ‘possess’ the necessary knowledge about the conditions under which a specific game runs, common errors that appear and difficulties that may arise. This requires access to the rules of the game, its roles, and access to previous records of earlier game runs.

(4) The system has to know the number of players. Providing the exact number of players to an intelligent tutoring facility would enable the system to pre-allocate resources, roles, and responsibility accordingly.

(5) Time schedules for the game have to be set up. An intelligent tutoring facility could set a few time parameters before starting the game, e.g. the duration of runs, time allowed for players to make decisions, time allowed for players to correct decisions, etc. These may depend on a number of parameters, such as the kind of game, the level of advancement of the game, the number of players, their level of advancement, etc.

(6) All teaching materials need to be prepared and handed out. An intelligent tutoring facility could prepare the teaching material and all the support material (e.g. explanations and remedial action) relating to a game making use of records of previous runs of the game. These records should include a score card for every player (thus a student model would be useful). An intelligent tutoring facility could make decisions regarding the distribution of the material to the players, the time of distribution and the chronology of events. The material to be handed out could be incorporated in the scenario (Appendix B). Game manuals could be incorporated into the domain model in such a way that the system can use it to answer specific questions about a game without the players having to browse through pages of electronic text.

(7) Roles have to be assigned to the players. An intelligent tutoring facility could decide what roles should be handed out. This again depends on many factors such as the kind and level of a game, the number and level of players, the time schedules, etc. The decision on who gets what role may be sorted out in many ways: randomly, chosen by the players or chosen by an intelligent tutoring facility according to the student model (e.g. aggressive players become leaders or players who do well in one role should gain experience with a new role, etc.).

(8) Making all these decisions requires a strategy. An intelligent tutoring facility could provide a pre-game strategy or a variety of strategies for making all decisions involved in the seven tasks outlined above.

## Introduction to the game

An intelligent tutoring facility may support the introduction of the players and their preparation for game play.

(1) The reasons for choosing the game have to be explained. An intelligent tutoring facility could state its reasons for choosing a game, i.e. to attain certain pedagogical goals or remedy diagnosed errors.

(2) The purpose, the steps of play, and the rules of the game have to be explained. An intelligent tutoring facility could provide every player with the scenario, the steps of play, and the rules governing each and every step.

(3) Roles (responsibilities, decision-making power and resources) have to be allocated to individual players. If the responsibility for allocating roles lies with an intelligent tutoring facility then the component is responsible for allocating a role to each player on the basis of the student models of the players. An intelligent tutoring facility should clearly state the responsibility of every role, its decision-making power, and the resources available within. A player's role may be allocated to the intelligent tutoring facility itself for a number of reasons: to increase the complexity of the game by simulating non-optimal decisions which then have to be rectified by a real player, to create an ‘ideal’ student model against which student models of the players can be evaluated (assuming that the system is a perfect player), to assume an ordinary player perspective, to collect statistics from the interaction with human players, etc.

(4) The cycle sequence of the game has to be explained. An intelligent tutoring facility could explain the cycle sequence of the game and the chronological sequence of events, i.e. the time parameters that all the players need to be aware of.

(5) Symbology and paraphernalia have to be explained. An intelligent tutoring facility could provide explanations about the symbology employed in the gaming simulation and any paraphernalia which are used to support the gaming simulation environment (Appendix B).

## Operation of the game

The operation of a game may vary between different games and game cycles. In one game the game operator may be constantly involved in a variety of management enterprises. In another the operator may be largely free from such tasks and able to circulate among the players, seeing what is going on and collecting information for use in the post-game discussion-critique. However, all these operating functions may be supported by an intelligent tutoring facility.

(1) The steps of play have to be controlled. An intelligent tutoring facility could use its knowledge about the steps of play of the game under way to control the game flow.

(2) Resources have to be distributed. If an intelligent tutoring facility has access to all the resources that will be distributed before and during the game it may support resource distribution by considering the following parameters: the game cycle stage, resource availability at this stage, the players' roles, and the players' game records (i.e. their student models) with respect to resource handling.

(3) Players have to be monitored and may need assistance: the use of student models. An intelligent tutoring facility could ensure that a certain level of involvement is achieved by the players and that those who have not achieved it yet get more involved. For this purpose an intelligent tutoring facility may reassign a player to a different role that better fits the style of the player. Alternatively, an intelligent tutoring facility may become a partner to the player by assigning a role to itself and thus help the player in making decisions and distributing and reallocating resources until no further need for such a partnership is required. To achieve such a level of performance an intelligent tutoring facility must have access to individual players' student models. A basic player's student model could be the matrix of the game roles played by a player versus the steps of play the player went through. This information could provide a linkage between the player's decisions and actions within the various roles. However, this would only provide overlay information which is not sufficient to explain any errors the player may have acquired. Therefore, an intelligent tutoring facility would not only need to update the student model of each individual player with information about a player's current knowledge status but also with their decision-making strategies, their use of resources, any diagnosed errors (e.g. game concepts), etc. An intelligent tutoring facility may then use this information for a number of reasons: to assess the level of performance of individual players, to assess the level of achievement for the reasons under which it chose the game under way, to help players clear away errors (e.g. incorrect application of rules), to remind players of the correct application of a particular rule, to make decisions about further distribution of resources (e.g. the system may impose a much stricter control on those players who waste or mismanage their resources), to fill any missing concepts (e.g. game concepts), to decide on future roles, etc. The players' student models will be useful for a later chronological analysis of what transpired in the game. An intelligent tutoring facility may introduce pulses (Appendix B) on the basis of the contents of the players' student models.

(4) The time limits have to be controlled. An intelligent tutoring facility could control all the time parameters identified earlier on. To do so, it may refer to the individual players' student models.

(5) Unanticipated consequences have to be dealt with. An intelligent tutoring facility could deal with unanticipated consequences. An intelligent tutoring facility could use a representation of the game model and the equivalent accounting system to reproduce the game conditions under which the unanticipated consequence occurred and compare the outcome of the model with the situation in hand. Should this fail, an intelligent tutoring facility could record the situation for presentation to the game designer who will have to investigate whether there is a real-world parallel for the situation in hand or whether it is a case of game breakdown.

(6) A game progress report has to be created. An intelligent tutoring facility could use indicators from the accounting system to give a progress report about the game at regular intervals (Appendix B). This report could include general statements such as the remaining steps of play, remaining resources, etc. and report on each player's performance by reference to their individual student models. The intelligent tutoring facility should be prepared to respond to inquiries about the individual reports presented to the players by making use of both its domain and student knowledge.

## Post-game critique

There are three distinct phases of the post-play critique.

(1) The final game progress report has to be created. An intelligent tutoring facility could present final game progress reports, a general one regarding the overall conduct of the game play, outcomes, problems, etc. and then individual player reports including feedback. Individual player reports are basically reproduced from the player's student model.

(2) The model presented by the game has to be examined from the perspective of the various roles in a systematic way. This gives everybody a chance to see what happened in the eyes of the other role players. For this purpose an intelligent tutoring facility could present information from the student models to all players about their correct and incorrect decision making, good and bad resource allocation and reallocation, pertinent errors, etc.

(3) The reality which was presented by the game has to be discussed rather than the game itself. This last step suggests getting out of the gaming simulation environment altogether and addressing the actual reality that the game simulated. This involves building a conceptual model of the reality the game depicts and applying it to some real world problem.

In order to illustrate how the integration of an intelligent tutoring facility may be put into practice and how it may increase the educational value of a real application the following section presents INTUITION, a computer-based version of the Metal Box Business Simulation game (Careers Research and Advisory Centre, 1978) which integrates an intelligent tutoring facility. The section will give a brief introduction about the game before it commences to illustrate how its intelligent tutoring facility supports the four standard operations of a game as outlined above.

## INTUITION: integrating an intelligent tutoring facility into a business simulation game

The original version of the Metal Box Business Simulation game was developed to give players an insight into the work of business managers and thereby acquire an understanding of business management. In this game the Metal Box Company is a manufacturer and supplier of central heating boilers and radiators which are sold at prices of between £1600 and £2500.

The player (or group of players) starts business as one of the managers of the Metal Box Company having to solve financial, production or marketing problems. The business must be run efficiently to be able to pay for salaries, materials and services and to cover the costs of the development of new production resources, such as an expansion of the size of the factory. The company has up to four players who take over the following roles.

(1) The production director who has to make decisions on the amount of boilers to produce and has to determine the selling price.

(2) The sales director who makes decisions on any market research or research and development to be undertaken, the number of sales persons to be recruited, and which customers the sales staff should call on.

(3) The financial director who has to master all calculations and is responsible for completing the company's accounts.

(4) The managing director who is in overall charge; he is the final arbiter on all operating decisions.

There are two other companies which are proposing to make and sell similar equipment and therefore are competing in the market. To enable the players to plan, make decisions, and control operations each company uses two documents, the company decision sheet and the company operating statements.

However, a major drawback of the original version of the Metal Box Business Simulation game is its lack of student guidance, support, and individualization. The students are left to allocate their own roles, they impose and control their own time restrictions for all decision processes, they are left without any help for any problems they encounter, and their decision-making processes are not monitored in order to provide them with assistance or encouragement as the need arises. Similarly, feedback about any mistakes that are made is restricted to the reaction of the market and lacks any further remedial action.

INTUITION has been developed as a gaming simulation environment which integrates an intelligent tutoring facility in order to overcome these drawbacks. The remainder of this section describes how the intelligent tutoring facility within INTUITION increases the educational value of the game. For this purpose it illustrates how the intelligent tutoring facility supports each of the four standard operations of a simulation game as discussed above, i.e. the preparation of the game, the introduction to the game, the operation of the game and the post-game critique.

## Preparation for running INTUITION

In order to provide for intelligent tutoring support INTUITION maintains a student model for each player which stores information about the players' knowledge and the errors they have made, the roles they have played in previous games and their experience and success rates with different teaching strategies and remedial actions. This information is used to prepare for game play as follows.

(1) INTUITION is familiar with the common problem players may encounter during game play. INTUITION's student model includes a library of all common errors that may occur during game play. At the same time this error record provides information to the system on how and when to correct these errors if they occur and what rules may have to be recalled in order to eliminate any difficulties.

(2) INTUITION finds out about the number of players. INTUITION inquires about the number of players in order to pre-allocate the market resources accordingly.

(3) INTUITION sets up the time schedules for the game. Before the start of a new game the student models of all of the players who have played the game at an earlier stage are accessed in order to gain information about each player that has been accumulated by the system in any previous games. This information is then used to reassess the advancement level of each player. If a player is new to the game the system creates a student model for this player and the player is assumed to be a novice. A time schedule which allocates time slots to the various decision-making episodes is then created according to the advancement level of the players.

(4) INTUITION sets up the scenario and prepares the supporting teaching materials. Based on the same information INTUITION sets up a suitable scenario and prepares the company decision sheet and the company operating statements.

(5) INTUITION assigns roles to the players. The new game is then set up by allocating the game roles to the players. Since the role of the financial director is most suitable for a beginner INTUITION assures that this role is allocated to one of the players who is new to the game. In addition, INTUITION accesses the student models to determine what roles have been played by the players in previous games. This information is used to ensure that a player is only allocated the role of the production director or the sales director if either they have gained experience in the role of the financial director in a previous game or if the role of the financial director has been allocated to another player.

## Introduction to the game

(1) INTUITION explains the aim, the rules, and the scenario of the game to the players. Once INTUITION has determined the advancement level of all players and has assigned the appropriate roles the system guides the novice player through the rules or, alternatively, leaves the decision of viewing the rules of the game again to the advanced player. At the same time all players are introduced to the game's scenario.

(2) INTUITION introduces all players to their responsibilities and allocates the resources accordingly. INTUITION presents each player with a detailed description of their tasks and responsibilities and the resources available to them.

(3) INTUITION may allocate certain roles to itself. INTUITION accesses the student model to determine what roles have been played by the players in previous games to advocate the concept of learning companionship (Chan and Baskin, 1990). For any role that has previously been played by a real player and is now a simulated role in the new game – a simulated role is a role which is played by the computer system and a gamed role is played by a real player – INTUITION complicates the game by simulating decisions which are strategically incorrect and therefore do not comply with the players' objective during the game play, i.e. the profitable running of the company. The player who has previously played this simulated role is then required to use his/her experience and act as a companion to the system, i.e. he can use his/her experience to influence the decisions of the system. Once the system has made a decision – right or wrong – the experienced companion is required to give his/her approval or an alternative suggestion to this decision which gives the companion the opportunity to detect and correct any 'simulated' incorrect decisions. INTUITION's intelligent tutoring facility compares the player's (the companion's) suggestion against the optimal solution and discusses any suggestions which do not come close enough to this optimal solution with the player. If, however, the player still fails to make the appropriate correction the game continues and the company will have to cope with the consequences.

(4) INTUITION explains the cycle sequence of the game. INTUITION eventually explains the order of decision making and announces the time parameters allocated to the different decisions to be made during the game.

## Operation of the game

Once the preparation of the game and introduction of the players to the roles and rules has been completed, the game commences with the first quarter. In order to support the adaptation and guidance through the game this decision sequence and its linkage is supported by INTUITION's intelligent tutoring facility. Teaching strategies complement the procedures of the accounting system (Appendix B) and help INTUITION to pursue its teaching objectives. Furthermore, the decision sequence and linkage requires INTUITION to use its general gaming simulation knowledge, such as knowledge about the roles, rules, models, and the current market situation. This knowledge has been extended by the additional domain knowledge required for the use of the teaching strategies. Finally, the decision sequence and linkage involves the use of information about the players stored in their student models. INTUITION's intelligent tutoring facility supports the operation of the game as follows.

(1) INTUITION controls the steps of play. An entire quarter within a game can be divided into seven steps of play or micro-cycles which are linked in the order of the sequence of the decisions to be made (Appendix B). INTUITION controls the flow of the game by operating and guiding the student through the micro-cycles below.

(i) Decisions on market research. The sales director is invited to start a quarter by deciding on the kind, if any, of market research to be undertaken. The market research options open to them are on any competitor's expenditure on research and development up to the previous quarter, on an economic forecast over the two quarters ahead and, finally, on the number of products required by any customer in the current quarter.

(ii) Decisions on production. It is then the task of the production director to decide on the size of the factory to be built in the first quarter and on the amount of products to be produced once the construction of the factory has been completed.

(iii) Decisions on sales staff, research and development, and advertising. INTUITION then asks the sales director to decide on the sales staff to be recruited and determine the number and destination of sales staff ready to be sent out to customers. Furthermore, it is at this stage that money may be spent on research and development and advertising.

(iv) Determination of the selling price. The production director is then asked to decide on the selling price and record it on the decision sheet.

(v) Decisions of the competing companies. At this stage INTUITION operates the simulation of all the necessary decisions for two competing companies in the same way as it has been done for the company by its real player(s). The system then proceeds to fill up the control statements of these two competitors.

(vi) Selling the products to the three competing companies. Once the previous micro-cycles have been completed INTUITION organizes the selling of the product. The system inquires about the destination of the sales staff of the companies. If more than one company has sent a sales person to a customer who has a demand for products the deal goes to the company with the lowest selling price (taking account of any notional selling price reductions). The number of products sold by each company is announced separately to each company involved and the details of the sale (i.e. how many products have been sold by a particular sales person) are revealed by including the results in the relevant control statements of the three companies. The sale of a product is a step of play which is executed by INTUITION to process the outcome of the players' decisions and thereby progress the game.

(vii) Entries into the control statements. The quarter concludes with the financial director completing all the control statements based on the outcome of the sale.

(2) INTUITION distributes the resources and controls the market situation. INTUITION distributes resources, such as the starting capital of the company and sets up the current market situation, such as the demand for products, based on the advancement level of the students and their previous decision-making behaviour.

(3) INTUITION monitors all players and provides them with any necessary assistance. INTUITION monitors the decision-making behaviour of each player during game play. All decisions made by players are recorded in the history of interaction of the student model (Appendix A). At the same time INTUITION determines all the correct (or possible) solutions based on all previous events and decisions in the game. These calculated solutions are then used for diagnosis purposes. The players' decisions and solutions are compared against the calculated correct solutions to detect any errors. Once all the possible errors within a particular gamed role have been diagnosed INTUITION provides individualized and efficient assistance and remediation to those players who require it (Siemer and Angelides, 1994). For every error that has been triggered INTUITION determines and adapts dynamically a remedial process according to the individual needs of the player. The specification of such an individualized remedial process is based on factors such as the kind of error to be repaired, the level of advancement (novice or advanced) of the player, the success rate of a particular remedial process applied to that player earlier and the number of occurrences of the same error. Once the remediation has been completed INTUITION takes the player through a consolidation phase in which they have to demonstrate their understanding of the concept involved and then gets the player back into the game in order to correct his/her mistake. Any new decision is examined by repeating the process of diagnosis.

(4) INTUITION controls the time limits. INTUITION regulates the time slots allocated to the various decision-making episodes and reminds the players when they are about to reach the point of time when a decision has to be made.

## Post-game critique

A game may be continued until it comes to one of two natural ‘business’ ends: a company might undercut the remaining companies by sheer growth and drive them into bankruptcy or the game can be stopped when one of the weaker companies has been forced out and the others have established themselves as viable businesses with a steady return on their invested capital.

INTUITION creates the final game process reports. Once the game has come to an end INTUITION analyses the final situation of the game and presents all players with a final game progress report based on the information accumulated in their student models.

## The architecture of INTUITION

In order to illustrate how the intelligent tutoring facility has been integrated into INTUITION's architecture to support the operations described above this section proceeds to specify the configuration of the architecture of INTUITION.

INTUITION has been implemented on an Apple Macintosh using the object-based hypertext package HyperCard 2.1. All the data is incorporated into semi-structured hypercards. The semi-structured kind of card allows the use of labelled fields which can either be filled with default values or may be instantiated with non-default values as these occur. Related hypercards are grouped together in a stack (Nielsen, 1990). All of the stacks and hypercards are linked to other stacks and hypercards to construct the required network that represents the INTUITION game.

The use of hypertext for the development of educational systems has recently become increasingly popular and many systems have been developed using the hypertext approach (Leggett et al., 1990). FLUENT, for example, is a hypertext foreign language tutoring and exploration system (Hamburger and Hashim, 1992). The system teaches Spanish at varying advancement levels. Initially, the tutor gives a command in Spanish which the student has to carry out. This provides the student with comprehension practice and enables the tutor to build up information about the student's learning process.

Apilog is a system which teaches Prolog programming (Bruillard and Weidenfeld, 1990). The hypertext architecture consists of a syntactic analysis module which diagnoses student errors, a Prolog interpreter and a set of examples and goals.

The hypertext system ARRIA teaches the theory of geometrical proofs programming (Bruillard and Weidenfeld, 1990). The system takes the student through a mathematical course in which the student has to solve mathematical problems. ARRIA provides for error diagnosis and correction.

The basic architecture of INTUITION is illustrated in Figure 1. INTUITION represents a fusion of a gaming simulation and intelligent tutoring system which provides for the system's intelligent tutoring facility. This section gives a brief outline of how the three standard components of the intelligent tutoring system have been fused with the gaming simulation before it commences to describe in detail the function of each individual stack that forms part of the overall INTUITION architecture.

INTUITION's gaming simulation knowledge constitutes the basic domain knowledge required to maintain and operate game play. Additional intelligent tutoring system domain knowledge stacks, such as the consolidation, question answering, and example stacks, have been integrated into the gaming simulation knowledge. These additional stacks provide for extra teaching support, such as practice and assistance with problems and presentations of alternative problem solution approaches.

INTUITION's decision sequence and linkage controller has been merged with the tutoring model by incorporating the teaching strategies into INTUITION's accounting system stack. A tutoring strategy planner stack regulates the selection of these strategies.

Eventually, INTUITION incorporates a student model for each player. The student model includes a library of all common errors to support error diagnosis. An overlay model represents the players' current knowledge about the game, the role they play in the current game and the roles they played in previous games, their performance during the different steps of the current and previous games and how well they managed the resources they were allocated by the system. The players' error stack and the player history of remediation stack contain information on all of the errors a player has been found to have made and how these errors have been corrected. Finally, the players' decisions stack constitutes the history of interaction between the system and the players since it records all decisions made by the players. The student model is a useful source of information during game play, because it provides the basis on which the accounting system can make decisions, such as further distribution of resources and role reassignment. In addition, the student model contains the necessary information for error diagnosis and remediation.

![](/api/attachments/S7F3GH7E/fulltext/images/7d42e85bb47558eb716d366a2ba8a8cd989822d43d489a967de243a9aa5cd30c.jpg)  
Figure 1 The architecture of INTUITION

The remainder of this section gives a description of the function and purpose of each individual stack of the INTUITION architecture. INTUITION stores the gaming simulation knowledge with its integrated intelligent tutoring system domain knowledge and the information in the student model on hypercards on gaming simulation knowledge stacks and student model stacks accordingly. The procedures of the accounting system and teaching strategies and the teaching strategy planner are implemented as program scripts which are stored on hypercards on decision sequence and linkage controller stacks.

## Gaming simulation knowledge

INTUITION's gaming simulation knowledge can be divided into static and dynamic knowledge stacks. It includes the additional domain knowledge required for the system's intelligent tutoring facility. The static stacks contain knowledge that has been determined prior to system implementation. The dynamic stacks, on the other hand, contain game knowledge which results from the current market situation during game play and therefore can not be predefined. Altogether, INTUITION contains eight stacks which jointly constitute its gaming simulation knowledge (for a more detailed explanation of the elements of a gaming simulation environment refer to Appendix B): models, rules and roles, consolidation, question answering, examples, simulated competitors' decisions, factual game knowledge, and simulated Metal Box Company decisions.

The models stack supports any calculations or estimates the player may want to perform before making a decision on a particular aspect. The player therefore has access to the models stack at any time and can use it like a calculator. The player can insert values into a model. These values are then analysed by the system (if–then analysis) to obtain an estimate of the result a particular decision might have, e.g. the player may want to analyse all their expenditures in the current quarter in order to obtain an estimate of the total costs per product to support the decision on an appropriate selling price. INTUITION's accounting system uses these models for an evaluation of any decisions made during game play.

The rules and roles stack contain an initial scenario hypercard to introduce the game by stating its aims and principles and a hypercard that contains the steps of play. Furthermore, it contains all the information about the four manager roles (i.,e. the production, sales, financial and managing directors) as four separate hypercards. It includes knowledge about the company decision sheet and the three control statements in four separate blank hypercards that describe the forms that the players will fill in during game play. Finally, the rules stack also includes hypercards about the production, production costs, market, time sequence of production and sales and cash flow, market research, selling the products, product advertising, research and development, and finance. In addition to using its rules and roles hypercards to prepare the player(s) for the game, this stack is used to explain the rules of the game should INTUITION detect a deviation from them, to offer some help in applying them correctly, and to correct any errors which may occur. Similarly, the players are granted direct access to the rules if they feel the need to refer to them during the game.

The consolidation stack supports intelligent tutoring by providing the knowledge and procedures used by the system to lead the players through a process in which they can consolidate newly acquired knowledge.

The question answering stack supports intelligent tutoring by providing question answering screens which are displayed to the player when the system applies question answering as a teaching strategy.

The examples stack supports intelligent tutoring by providing examples which may need to be displayed to the players for teaching purposes during game play.

The factual game knowledge stack contains the factual data that is required to run the game, such as the market demand for the products, the distribution of the market demand on the customers in the current game, and a table with all market demand distributions possible. In addition, the factual game knowledge stack records all the necessary information on the selling prices of all three competitors by accessing the player decisions stack and the simulated competitors' decisions stack during game play. This information is then provided to those players who demand market research information regarding their competitors' selling prices. In the same way and for the same reason the competitors' cumulative expenditures on research and development are combined on a separate hypercard in this stack.

The simulated competitors' decisions stack contains the information about decisions made by the simulated roles of the two competing companies and, similar to the factual game knowledge, is used to run the game. Since this information is determined by the current market situation it is being generated and stored during game play.

The simulated Metal Box Company decisions stack records the data that results from the system simulating all of the actions to be made by the Metal Box Company. This data is based on the current market situation and is consequently generated during game play. In this way an ‘ideal’ student model of all three directors emerges. The data is used to evaluate the decisions of any gamed roles in order to diagnose any errors. Alternatively, if the director role is a gamed role, the data is used as a system-generated input into the game.

## The student model

INTUITION's student model contains five stacks: player decisions, player overlay model, library of errors, players' errors, and player history of remediation.

The player decisions stack records all decisions made by the player during game play. As the players' history of interaction, it constitutes the central stack of the player - system interaction. As the game progresses hypercards are expanded or extra ones are added to this stack and any necessary hypercard links are generated according to the players' decision making.

The player overlay model stack records the emerging knowledge of the player. This knowledge is represented as a subset (overlay) of the domain knowledge and is derived from the decisions recorded in the player decisions stack within the process of diagnosis.

In addition, the player overlay model stack contains lists of all the roles each player has played in any previous games of the current round. When the accounting system decides to remedy an error that occurred with a gamed role, it may refer to the information contained in the player overlay model stack. If a different player has played this role in a previous game, then this player may be asked to support the remedial process by acting as a learning companion to the player who requires remediation.

The library or errors stack which contains all known errors which might occur during interaction has been included in the INTUITION architecture for the purpose of error diagnosis and correction. Each of these possible errors is stored on a separate hypercard in this stack. Each hypercard dynamically defines a remedial process as the error occurs which can then be referred to by the decision sequence and linkage controller to carry out the remedial process.

The players' errors stack contains a separate hypercard for every player (previous or current) that contains all of the errors that the player has been diagnosed to suffer from. Every hypercard includes information regarding the context in which an error has been detected and the number of times it had occurred.

The player history of remediation stack contains all the errors the player has been diagnosed to suffer from and how each and every one has been remediated. For every diagnosed error in the players' error stack, a hypercard is added to the stack of the player concerned. In this way a chronological record of all the remedial tutoring is built up during the course of interaction for each individual player. During game play this stack may be accessed by the human supervisor for information regarding the player's performance and hence support a possible supervisor-led teaching process.

## The decision sequence and linkage controller

The decision sequence and linkage controller includes the accounting system and the teaching strategies which it uses to deal with the players' decisions and to guide the game. It includes knowledge about the game's teaching goals which it will try and help the player to attain during and through game play. Thus, it knows when, where, and how to start, progress, and finish a game. The decision sequence and linkage controller supervises the flow of the game by controlling the steps of play. In addition, when an error is diagnosed for a player, the decision sequence and linkage controller goes into remedial mode for that player. The decision sequence and linkage controller is supported by information which it obtains from the gaming simulation knowledge and the student model. It is implemented as program scripts on the following two stacks: accounting systems and teaching strategies, and tutoring strategy planner.

The accounting system and teaching strategies stack consists of three hypercards which contain program scripts for running and controlling the game. The first hypercard contains program scripts for preparing and starting the game. The process of selling products to the customers is controlled from this hypercard, i.e. it determines which company has sold how many products to which customer. The second hypercard contains the teaching strategies that are used to run and progress the game. The process of generating the entire game is implemented as several separate program scripts. Each program script represents an execution of a simulated role, the diagnosis of an error, the remediation of an error, or the allocation of tasks to a particular player. The order in which these program scripts are executed is determined dynamically as the game progresses.

The tutoring strategy planner stack is accessed when the active involvement of the players themselves, a human collaborate player, or the supervisor is required in the process of determining an adequate and helpful teaching strategy. Accordingly, this stack consists of three types of hypercards which contain lists of possible teaching strategies from which the player, their companion, and the supervisor may choose the one strategy they believe is most suitable and successful for the current teaching process. The hypercards addressing the supervisor include the extra option of gaining access to the student model in order to obtain information about the knowledge state of the player.

## Conclusion

The use of gaming simulation for management education and training purposes is on the increase (Lane, 1995). Gaming simulation can be viewed as a hybrid form that involves the performance of game activities in simulated contexts. In this simulated context the players have goals, have to perform sets of activities, deal with constraints on what can be done, and handle pay-offs

## Integrating an intelligent tutoring facility

(good and bad) as consequences of these actions. The elements in a gaming simulation (roles, goals, activities, constraints, and consequences) are patterned from real life and the linkages between them simulate those elements of the real-world system. In this way gaming simulation can serve as a pre-decision tool to link a more complex model to the real world.

However, a problem with gaming simulations is that the player lacks the sufficient conceptual ability to use the simulation game in such a way that its teaching benefits are optimized. Intelligent tutoring systems, however, promise to enrich the learning opportunities for students by providing individualized student guidance and support within the teaching environment. Therefore, to be completely effective as a teaching or learning tool, a gaming simulation should be equipped with an intelligent tutoring facility (Angelides and Paul, 1993).

To provide for player adaptability, this paper has therefore discussed the manifold possible functions of an intelligent tutoring facility within a gaming simulation environment for each of the four main operations that are generally performed within a game, i.e. the preparation for running the game, the introduction to the game, the operation of the game, and the post-game critique.

This paper has then presented INTUITION as a system which has been implemented by integrating an intelligent tutoring facility within a gaming simulation environment. This integration involved the extension of the gaming simulation environment by intelligent tutoring knowledge, i.e. tutoring knowledge, additional domain knowledge, and student knowledge. The integration of tutoring knowledge and additional domain knowledge enable INTUITION to use teaching strategies which enable the system to follow a clear and attainable educational learning goal for each player, to manage market resources, and to control the decision-making processes accordingly. A student model for each player provides information on the players' current knowledge status, their gamed roles and any errors they have made. It thereby provides the necessary information to guide the game according to each player's performance and competence.

INTUITION offers players the advantages of both simulation gaming and intelligent tutoring combined to best symbiotic effect. The gaming simulation environment promotes learning by experience amongst participants (Lane, 1995) whilst the intelligent tutoring system provides adaptability to the player. INTUITION keeps track of the players' emerging knowledge and any errors occurring in order to provide individual tutoring which is continuously adjusted to each player's knowledge level. INTUITION, therefore, is a prototype system that demonstrates that the pedagogical value of gaming simulation can be increased through the integration of intelligent tutoring support.

## References

Anderson, J.R. (1988) The expert module, in Foundations of Intelligent Tutoring Systems, M.C. Polson and J.J. Richardson (eds) (Lawrence Erlbaum Associates, New York) pp. 21–53.

Angelides, M.C. and Doukidis, G.I. (1990) Is there a place in operational research for intelligent tutoring systems? Journal of the Operational Research Society, 41(6), 491–503. (Reprinted in Artificial Intelligence in Operational Research, G.I. Doukidis and R.J. Paul (eds) (Macmillan, London) 1992, pp. 287–99.

Angelides, M.C. and Paul, R.J. (1993) Developing an intelligent tutoring system for a business simulation game. Simulation Practice and Theory, 1(3), 109–35.

Brown, J.S., Burton, R.R. and De Kleer, J. (1982) Pedagogical, natural language and knowledge engineering techniques in SOPHIE I, II and III, in Intelligent Tutoring Systems D. Sleeman and J.S. Brown (eds) (Academic Press, London, pp. 227–79).

Bruillard, E. and Weidenfeld, G. (1990) Some examples of hypertext's applications, in Designing Hypermedia for Learning, D.H. Jonassen and H. Mandl (eds) (Springer-Verlag, Berlin) pp. 377–86.

Careers Research and Advisory Centre (1978) 'Stelrad Limited', The Metal Box Business Game (Hobsons Press, Cambridge).

Chan, T.W. and Baskin, A.B. (1990) Learning companion systems, In Intelligent Tutoring Systems: At the Crossroads of Artificial Intelligence and Education, C. Frasson and G. Gauthier (eds) (Ablex Publishing Corporation, Norwich) pp. 6–33.

Doukidis, G.I. and Angelides, M.C. (1994) A framework for integrating artificial intelligence and simulation. Artificial Intelligence Review, 8(1), 55–85.

Elsom-Cook, M.T. (1991) Dialogue and teaching styles, in Teaching Knowledge and Intelligent Tutoring, P. Goodyear (ed) (Ablex Publishing Corporation, New Jersey) pp. 61–84.

Greenblatt, C.S. and Duke, R.D. (1981) Principles and Practices of Gaming-simulation (Sage, new York).

Halff, H.M. (1988) Curriculum and instruction in automated tutors, in Foundations of Intelligent Tutoring Systems, M.C. Polson and J.J. Richardson (eds) (Lawrence Erlbaum Associates, New York) pp. 79–108.

Hamburger, H. and Hashim, R. (1992) A foreign language tutoring and learning environment, in Intelligent Tutoring Systems for Foreign Language Learning: The Bridge to International Communication, M.L. Swartz and M. Yazdani (eds) (Springer-Verlag, Berlin) pp. 201–18.

Lane, D.C. (1995) On the resurgence of management simulations and games. Journal of the Operational Research Society, 46(5), 604–25.

Lardinois, C. (1989) Simulation, gaming and training in a competitive, multimodal, multicompany, intercity pas-

senger-transportation environment. Journal of the Operational Research Society, 40(10), 849–61.

Leggett, J.J., Schnase, J.L. and Kacmar, C.J. (1990) Hypertext for learning, in Designing Hypermedia for Learning, D.H. Jonassen and H. Mandl (eds) (Springer-Verlag, Berlin) pp. 27–38.

Nielsen, J. (1990) Hypertext & Hypermedia (Academic Press, London).

Schlecher, T.M., Bessemer, D.W. and Kolosh, K.P. (1992) Computer-based simulation systems and role-playing: an effective combination for fostering conditional knowledge. Journal of Computer-based Instruction, 19(4), 110–14.

Siemer, J. and Angelides, M.C. (1994) Embedding an intelligent tutoring system in a business gaming simulation environment, in Proceedings of the 1994 Winter Simulation Conference, Lake Buena Vista, Florida, Dec. 11–14, 1994, pp. 1399–406.

VanLehn, K. (1988) Student modelling, in Foundation of Intelligent Tutoring Systems, M.C. Polson and J.J. Richardson (eds) (Lawrence Erlbaum Associates, New York) pp. 55–78.

Winkels, R. (1992) Explorations in Intelligent Tutoring and Help (IOS, Amsterdam, The Netherlands).

## Biographical notes

Julika Siemer is a lecturer in the Department of Information Systems at the London School of Economics, a post to which she was appointed in July 1995. She studied computer science at Hildesheim University, Germany, and holds an MSc and PhD in information systems, both from the London School of Economics. She has authored and co-authored several journal and conference papers on intelligent tutoring systems and has developed a full-scale intelligent tutoring system for a business simulation game.

Marios Angelides is a lecturer in information systems at the London School of Economics. He received both his BSc and PhD in computing from the London School of Economics. His major areas of research are multimedia information systems, information superhighways and intelligent tutoring systems. He has published extensively in these areas and he is the author of Multimedia Information Systems (Kluwer Academic Publishers, 1997). He is a member of the Association for Computing Machinery (ACM), the Institute of Electrical and Electronic Engineers (IEEE), Computer Society and the British Computer Society

Address for Correspondence: Julika Siemer, Information Systems Department, London School of Economics, Houghton Street, London WC2A 2AE, UK.

## Appendix A: Intelligent tutoring systems

In order to provide for its intelligence an intelligent tutoring system must pass three tests of intelligence (Anderson, 1988). Firstly, the system must know the subject matter well enough to be able to draw inferences or solve problems in the domain of application. Secondly, it must be able to deduce the student's current understanding of the subject matter and use this individualized knowledge to adapt instruction to the student's needs. Thirdly, the tutor must be able to apply suitable tutoring strategies that reduce the difference between the expert and the student performance. This includes formulating a representation of the subject material and selecting and sequencing concepts from that representation. Therefore, the standard architecture of an intelligent tutoring system includes the following three components: the domain model which represents the subject area to be taught, the tutoring model which contains the teaching strategies which control the presentation of the learning material, and the student model that holds a student's approximation of the domain knowledge (Winkels, 1992).

## The domain model

The first key place for intelligence in an intelligent tutoring system is in the knowledge that system has of its subject domain. There have been three approaches in encoding knowledge into the domain expert which gave rise to the three different types of models for domain experts.

The first approach, which gives rise to the black box model, involves finding a method of reasoning about the domain that does not actually require modification of the knowledge. In other words, the reasoning is implemented using conventional data processing rather than symbolic processing methods. A black box model of a domain expert is one that generates the correct input-output behaviour over a range of tasks in the domain and so can be used as a judge of correctness. However, the internal computations by which it provides this behaviour are either not available or are of no use in delivering instruction. Such a domain expert model can be used in a reactive tutor that tells the students whether they are right or wrong and possibly what the right move would be. A methodology called issue-based tutoring was proposed (Brown et al., 1982), which involves recognizing patterns, i.e. issues, on both the student's and the expert's surface behaviour and generating instruction for those patterns. Nevertheless, this surface-level, issue-based tutoring does not solve the problem of providing explanations about the actual reasoning process, if the intelligent tutoring system does not have access to the internal structure of the domain expert.

## Integrating an intelligent tutoring facility

The second approach, which gives rise to the glass box model of a domain expert, involves reasoning about the domain by applying codified knowledge. A glass box model of a domain expert is the standard knowledge-based systems approach to reasoning with knowledge. These systems are characterized by the great quantity and human-like nature of knowledge that is articulated. Because of its nature, the emerging system should be more amenable to tutoring than a black box model because a major component of this expert system is an articulate, human-like internal representation of the knowledge underlying expertise in the domain. For tutoring systems to be effective, it is not simple enough to understand the knowledge on the domain expert but also the way by which this knowledge is deployed and the humans restrictions levied on it.

The third approach, which gives rise to the cognitive model of a domain expert, involves making the domain expert a simulation of human problem solving in a domain, at some level of abstraction.

## The student model

The component of an intelligent tutoring system that represents the student's current state of knowledge is called the student model. An intelligent tutoring system infers a model of a student's current understanding of the subject matter and uses this individualized model to adapt the instruction to the student's needs.

Inferring a student model is called student diagnosis. The input for diagnosis is garnered through the interaction with the student. The particular kinds of information available to the diagnosis module depend on the overall intelligent tutoring system application. This information could be answers to questions posed by the intelligent tutoring system, moves taken in a game or commands issued to an editor. This information is sometimes complemented by the student's educational history. The output of the diagnostic module, i.e. the product of diagnosis, depends on the use of the student model. Nevertheless, it should reflect the student's current knowledge state. Some of the most common uses for the student model include advancement of the user to the next curriculum topic, offering unsolicited advice when the student needs it, dynamic problem generation and adapting explanations by using concepts that the student understands. All these assume consultation with the student model before any kind of action is taken.

Because students will move gradually from their initial state of knowledge towards mastery, student models must be able to change from representing novices to representing experts. Most intelligent tutoring systems use the same knowledge prepresentation language for both the expert model and the student model. Conceptually, an intelligent tutoring system has one knowledge base to represent the expert and one to represent the student. Nevertheless, the student model is represented as the expert model plus a collection of differences. There are basically two kinds of differences: missing conceptions and misconceptions. A missing conception is an item of knowledge that the expert has and the student does not. Conceptually, the student model is a proper subset of the expert model. Such student models are called overlay models. With overlay models, a student model consists of the expert model plus a list of items that are missing. To model misconceptions an intelligent tutoring system employs a library of predefined misconceptions. The system performs student diagnosis by finding misconceptions from the library that, when added to the overlay model, yield a student model that fits the student's performance.

## The tutoring model

The third key place for intelligence in an intelligent tutoring system is in the principles by which it tutors students and in the methods by which it applies these principles. Automated tutors can use many different instructional techniques, but tutorial interactions, however they are conducted, must exhibit three characteristics.

(1) A tutor must exercise some control over the curriculum, that is the selection and sequencing of material to be presented to the student and some control over instruction, that is the process of the actual presentation of that material to the student.

(2) A tutor must be able to respond to student's questions about the subject matter.

(3) A tutor must be able to determine when students need help in the course of practicing a skill and what sort of help is needed.

The problem of the curriculum can be broken down into two problems: formulating a representation of the material in the domain expert and selecting and sequencing concepts from that representation. In addition, a domain tutor must incorporate some form of propaedeutics, that is knowledge which is needed for enabling learning but not for achieving proficient performance. Curricula in intelligent tutoring systems serve several functions.

(1) A curriculum should divide the material to be learned into manageable units. These units should address at most a small number of instructional goals and should present material that will allow students to master them.

(2) A curriculum should sequence the material in a way that conveys its structure to students.

(3) A curriculum should ensure that the instructional goals presented in each unit are achievable.

(4) Tutors should have mechanisms for evaluating the student reaction to instruction on a moment-to-moment basis and for reformulating the curriculum.

Propaedeutics serve to support performance up to an intermediate level. The underlying assumption is that a skilled performance will be achieved only with practice. As a result, they serve, firstly, to relate theory to practice, secondly, to justify, explain and test possible problem solutions, thirdly, as a stepping-stone to more efficient problem-solving strategies and, fourthly, as strategies for management of the working memory during intermediate stages of learning.

## Appendix B: A framework for business simulation games

According to Greenblat and Duke (1981), a gaming simulation environment either ‘man–machine’ or ‘all-man’, consists of 12 basic elements which are described below.

## Scenario

A scenario is simply a text outlining the plot of the game. It outlines the starting conditions and describes circumstances leading into play. It deals with all aspects, i.e. economic social and political, which are either presented by text or supplemented with diagrams and illustrations. Role descriptions might be considered a part of the scenario, but are normally offered separately. Role descriptions will normally establish initial points of reference and discussion for the players.

## Pulse

A pulse is some event or problem introduced during the course of play to focus the player's attention on a single aspect of the problem. The pulse may be either designer or player induced. It may be predetermined, random or triggered by a certain action in the game. A pulse is an organizational device, used to encourage multilogue (i.e. multiple, simultaneous dialogue) by forcing players to focus on some shared phenomena. One pulse follows another in sequence. In complex games, several are simultaneously initiated. Each represents an aspect of a conceptual map. During play of gaming simulation, these pulses become tangible handles which allow players to grasp the problem in detail and enter into and explore the Gestalt of the total problem situation.

## Cycle sequence

A cycle sequence is divided into the macro-cycle sequence that takes into account preconditions to the game, the introductory cycle, the final cycle and the evaluation process associated with the total exercise and the micro-cycle that takes into account the sequence of things that occur within each cycle, including the initiation, policy, action and evaluation of each cycle.

## Steps of play

Steps of play are the explicit progression of activity in the game. There is a macro-cycle in each game which includes four steps: initiation, policy, action and evaluation. During the initiation, the players read the scenario, take into a cycle any pulses/events/issues that have occurred and consider any new data available to them as a result of the previous cycle. During the action cycle, players make specific decisions according to a given order. During the evaluation phase of the cycle, all play stops and an intellectual discussion ensues, under the direction of the game operator which addresses two questions. What are the results of the cycle just completed? How does this experience relate to the real-world problem? The next step is always recycling, which proves particularly critical because the success of gaming simulation in conveying a problem Gestalt is largely derived from the interactive or cyclical nature of these exercises. Learning takes place through repetition of experience. Steps of play provide the game with basic guidelines of progress. Each sequence denotes another set of instructions, which signals some action(s) to occur. Players move through the game one step at a time. This makes it easier for the player and the operator. The ultimate goal of the steps of play is to increase learning and to enrich the knowledge of the system of the problem being represented.

## Rules

There are a variety of circumstances that might develop in a game, which go beyond the scope of expertise of the game. If these are anticipated, the designer can present rules that govern these cases. These should be made clear to the players at the outset and any changes during play should be posted in a conspicuous way.

## Roles

Roles are characters assigned to players with prescribed patterns of behaviour. They are predicated on known real-world counterparts. The participants may play a role similar to their own ‘real-world’ role, but gener-

## Integrating an intelligent tutoring facility

ally it is better to permit the player to experience the game problem from a position unknown to the person in reality. Roles are always limited in number to those most central to the problem studied. There are basically three kinds of roles that can be included within the game: pseudo, game or simulated. Pseudo roles are invented on the spot to serve some immediate function, e.g. judges and technical experts. When the right situation arises, special participants with unique skills are employed on the spot. Pseudo roles remain neither linked to the basic rule structure, nor are they processed formally through the game's accounting system. Game roles are built into the gaming situation framework and played by real players whose decisions are processed by the game's accounting system. Simulated roles exist in the accounting system but not physically in the game room itself. Often they represent broad classes or categories of people. It is often useful to have simulated roles in the gaming simulation to generate output useful to the game or pseudo roles.

## Models

Models are devices derived from the accounting system to keep track of logical processes. They may be simple or complex. They may be expressed in mathematical terms or illustrated graphically. There are basically three types of models: analogue models which parallel the real-world phenomena and correspond to the real counterparts they represent at least at some level of abstraction, iconic models which give the physical appearance of reality but need not act like reality and heuristic or homologue models.

## Decision sequence and linkage

The sequence of decisions and linkage between players' actions must be understood before the game is built. These represent the typical sequence of decisions that players can make during a normal cycle of play. Often these are developed through the use of a matrix. Across the top of the matrix are all of the game roles and down to the left side are the steps of play. This schematic is intended to answer the question, who is doing what, when and how? It also provides data on information flows and feedback and role-to-role transitions. The matrix depicts the activity and intellectual process of each role during consecutive steps of play. The purpose of this matrix is to assist the game designer in visualizing the sequence of play when the game is finished. The matrix helps to identify role linkages within the game framework, to chart the foreseen reactions of the participants to events during play and to provide an initial analysis of all game, pseudo and simulated role results before play begins. When completed, this matrix gives some early insight into the totality of the game during play. In evaluating the contents of the matrix, the need will arise to adapt or change roles for one of several reasons. Players must be more or less equally loaded so that they are evenly occupied during the presentation. It is also necessary during an analysis of this chart to ensure that decisions are sequenced properly, one behind the other, so that necessary feedback takes place. Finally, the matrix can be used as an aid in explaining to others the sequence of events occurring during a typical game run.

## Accounting system

The accounting system is a set of procedures incorporated directly into the game to deal consistently with player decisions. These decisions, which are outcomes of steps of play, are processed, acted upon and forwarded to some other game component, feeding back either into an indicator, model, role or some combination of the above. An infinite variety of accounting systems exist. Game designers must develop a system suitable to the particular exercise. In the final analysis, the accounting system must be devised to deal in a rigorous and consistent way with all of the information that is manipulated by the gaming elements. Having selected and defined the gaming elements, a procedure for their activation must be devised and implemented as an accounting system in the gaming simulation. The accounting system may be simple or complex and it may manoeuvre players' responses through models, simulations or very simple algorithms. It will always report to the players through various indicators and will be displayed on forms, charts and playing boards. Whenever possible, it is desirable to have the players individually keep the accounting system. This gives them a better understanding of the problem being considered and saves a great deal of work for the operator. Regardless of the format or the combinations employed, the accounting system will inevitably be sequential. This requires very sophisticated judgement by the builders of the exercise to ensure that the sequence of decisions, as represented by the system of accounts, at least integrates into a larger system or Gestalt experience.

## Indicators

Indicators are those aspects of the accounting system that the operator chooses to emphasize for the participants. They report on the game's progress, that is the interaction of players' decisions as filtered through the accounting system and linked to the models.

## Symbology

Symbology is the physical representation of indicators. These are visual aids comprising a set of characteristics about some game phenomenon. Symbology is game specific in that the materials lose meaning outside of the playing arena. They are comprised of spontaneous material such as chips and blocks and are integrated into the game to portray some reality such as the land use or building pattern. Symbology may be any tangible replication incorporated into play to embellish as well as convey meaning. Players are asked to focus their attention on these items to address and manipulate them according to procedures.

## Paraphernalia

Paraphernalia includes everything else required to run the simulation exercise successfully. The material ranges from the decision forms to charts to colour patterns and the game board itself.

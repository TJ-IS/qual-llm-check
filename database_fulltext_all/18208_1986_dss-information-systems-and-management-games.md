---
otero_id: 18208
otero_key: "8PMDA9ZG"
title: "DSS, information systems and management games"
authors: "Rommert J. Casimir"
year: "1986"
journal: "Information & Management"
doi: "10.1016/0378-7206(86)90009-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DSS, Information systems and Management Games \*

Rommert J. Casimir

Dept. of Information Systems, Tilburg University, P.O. Box 90153, 5000 LE Tilburg, the Netherlands.

The concept of a management game can be used to define the notion of Information Systems and Decision Support Systems. A design for such a management game is outlined, and its use for research and education in information systems is discussed.

Keywords: Management Game, Information System, DSS.

![](/api/attachments/8PMDA9ZG/fulltext/images/b5e770d16d312631ce23f3e01c47d4e156263931d9956571e25577149027042a.jpg)  
Computer Science.

Rommert J. Casimir is a lecturer in Information Systems at Tilburg University, the Netherlands. Previously he was a lecturer in Computer Science at Erasmus University, where he also received his M.A. in Business Economics in 1970, and a Systems Programmer with Electrologica. His papers appeared in national journals, including Bedrijfskunde, Informatie, I & I, and MAB. His current interests are in Management Games and their relation to Information Systems and

## 1. Introduction

A Decision Support System (DSS) is usually defined as an information system that supports unstructured or semistructured decisions [1]. Because they often use sophisticated modeling techniques and specialised languages and environments, many authors stress the importance of "DSS generators" and "DSS tools" to the point that the techniques used in the design rather than its purpose are considered the main characteristic. So a DSS may be considered successful even if it was ultimately used for quite other purpose than management support. This has led Huber [12] to make a distinction between "DSS", the products advertised under that name, and "dss" or "decision support systems", the information systems actually used by managers for decision support. In this paper we use the general term for the latter definition, and try to sharpen it by considering the different types of decisions in an organization.

## 2. Decisions and Information Systems

There are two main types of information systems in organizations:

a) Those that define the rights and obligations of the organization or of groups or individuals within it.

b) Systems that provide information of decisions at any level.

The first type provides the bulk of manual and electronic data processing. Examples are accounts receivable and salary systems. DSS texts, e.g. [22], often criticize this type of information system for not providing adequate information for management, thereby neglecting its importance for other purposes. Not all transaction systems belong to this class, because many incorporate decisions at operational levels, e.g. an order entry system may decide how to reorder on low inventory. Management control systems and operational control systems constitute an important subclass of this type.

Information systems of the second type are called management information systems or management accounting systems. This class of informations system includes, but is not equivalent to Decision Support Systems. An information system can serve both ends; in that case it takes on two roles.

## 2.1. Classification of decisions

Two criteria for the classification of decisions are the relative importance of the decision and the time available for it. In our definition the importance of a decision is determined by its importance for the organization, not by its importance for an individual or for the world at large. Usually it can be measured in monetary terms (an important decision involves a large porportion of the resources of an organization), but some decisions are only important because of political or legal consequences.

The notion of the importance of a decision is related to the distinction between structured and unstructured, or programmed and nonprogrammed decisions, as defined in $[20]$ , and first used in the classification of information systems in $[11]$ . Because an organization has limited resources, it can take only a small number of important decisions; so these will never be routine decisions that can be programmed. However, an individual decision may be replicated in a large number of individuals and, as a consequence, a generally accepted rule may be established; such a rule may be called a socially programmed decision. On the other hand, not all unimportant decisions can be programmed. In our view, importance is superior to structuredness as a criterion, as the latter concept has been criticised for its lack of clarity $[23]$ .

The second criterion from [11], the distinction between Operational Control, Management Control and Strategic Planning is not used in our classification, because we focus on decision making at all levels, and not on management tasks; moreover it is not extensively used [21]. However, importance may be defined organizationally: an important decision is a decision that is made (or should be made) by top management.

The length of time available for a decision may be long or short in relation to the time needed to gather and process the information. Time is short if dangers lie ahead or if opportunities may vanish; this occurs when there is a risk of idleness of expensive resources.

For each type of decision the decision maker needs an appropriate type of information system, as in Table 1.

## 2.1.1. Operational decisions

Operational decisions are defined $[2]$ as those normally taken by operating (rather than managerial) personnel. However, this definition cannot be applied where employees regularly combine operating and managerial tasks. In our definition we make no supposition about the decision makers. Because operating decisions have to be made at short notice, they leave no time for consultation with managers. Accordingly, they may have to be made by a computer, by operating personnel following predefined rules, or by a professional. An examples of operational decisions is found in the buying process.

## 2.1.2. Bureaucratic decisions

With bureaucratic decisions, recourse to a higher level is always possible. Examples of bureaucratic decisions are tax assessment and salary review. There is a tendency to use exact rules in bureaucratic decisions because such decisions may be legally challenged as the persons affected by the decision usually have full information.

## 2.1.3. Crisis decisions

Here the decision maker lacks the time to collect and process the necessary information. Society and individuals try to prevent the need for crisis decisions. One very early example is in the replacement of hunting by farming. Profits from a speedy reaction to opportunities is sometimes considered immoral, e.g., in use of inside information. Accordingly, crisis decisions mainly occur after disasters or in international politics.

Table 1  
Decisions and Information Systems

<table><tr><td></td><td>Short</td><td>Long</td></tr><tr><td rowspan="2">Unimportant</td><td>Operational decisions</td><td>Bureaucratic decision</td></tr><tr><td>Operational system</td><td>Bureaucratic system</td></tr><tr><td rowspan="2">Important</td><td>Crisis decision</td><td>Strategic decision</td></tr><tr><td>?</td><td>Decision support system</td></tr></table>

## 2.1.4.Strategic decisions

For strategic decisions, there is ample time to collect and process the necessary information, though the decision maker does not always have perfect information (it may be too expensive). An example is an investment decision.

## 2.1.5. Classification of information Systems

Every type of decision needs an appropriate information system. Information systems for crisis decisions will be omitted from the subsequent discussion, as they have been studied mainly in a military, rather than a business context, e.g. [18]. Table 2 lists the characteristics of the other information systems. Notwithstanding the use of computer science terminology, the concepts are valid for manual as well as automated information systems.

## 2.1.6. Transfer of techniques

The techniques used in one type of information system can be transferred to another. For example, a model that has been developed to support a top banker in million dollar loan decisions certainly is part of a DSS. However, if the same model is used to decide on a large number of loan applications, it is used in a bureaucratic system. Alternatively, if the model is used by bank clerks to instantaneously decide on small loan applications, it is part of an operational system. In this way a DSS may serve as a prototype for a bureaucratic or an operational information system, which explains the similarity of the techniques used in the design of DSS and those used in prototyping. The tendency for DSS to evolve to operational systems is called migration $[17]$ .

## 3. Management Games

## 3.1. Simulation of systems

We can distinguish between operational systems and decision systems that decide what actions the operational system must take. The decision system either reacts to a set of rules or to a more general program. Decisions which are made according to rules are called programmed in the terminology of Simon [20], other decisions are called nonprogrammed. To take decisions in an operational system, information (often called feedback) is needed. We assume that this is supplied by a separate information system, which extracts it from the operational system. Most simulation studies center on the decision system part of systems; they assume that the information system will extract all necessary information from the operational system and pass it to the decision system. A study of the influence of incomplete information on decisions [15], is an exception.

## 3.2. Traditional management games

A management game is a game where two or more players have to make managerial decisions in a simulated world. A popular type is the business game, where the simulated world contains a number of competitive business units. In a business game participants have to take decisions on price, marketing expenses, production and capital expenditure. A description of a large number of such games is given in $[10]$ . The level of abstraction in a management game is far lower than the level of abstraction in game theory. Management games are mainly used in education; many researchers prefer to use interactive simulations, also named simulation games. In those, a single player tries to maximize some results in a simulated world.

A traditional management game is played in a discrete number of rounds or periods, each equivalent to a month, a quarter, or a year. The decisions for a round are taken simultaneously by all players. Consequently players never have complete information on the state of play. When all players have entered their decisions, the results of a round are computed and reported to the players. The time available for decision making by the players normally is much longer than the time needed to compute the results: A ratio of half an hour of decision time to five minutes of computing time is typical. In traditional management games data are collected and processed according to a standard method, except for marketing data, that normally must be bought.

Table 2  
Characteristics of Information Systems

<table><tr><td>Information system</td><td>System Characteristics</td><td>Technical Characteristics</td></tr><tr><td>Operational information system</td><td>Simple algorithms</td><td>Real-time; Reliability</td></tr><tr><td>Bureaucratic information system</td><td>OR (e.g. LP); Statistical techniques</td><td>Batch; Large data sets</td></tr><tr><td>DSS</td><td>Models</td><td>Flexible programs; Data bases</td></tr></table>

## 3.3. Management games and information systems

To apply our classification of decisions to management games, we replace the terms from Table 2 by terms derived from management games, as in Table 3.

From this translation we compose Table 4, which specifies the information systems in a management game. It should be noted that crisis decisions cannot be made in a game played in rounds, because players cannot interfere with the simulated world during a round. A game where players can interfere at any time is a real-time system, and it should organise its output in a way that encourages fast reaction. Experience with arcade games [6] shows that graphical output is preferable for that purpose. Technically, a real-time game may be approximated by shortening the time available for decisions and diminishing the number of decisions required in each round. We should also note that minor, unstructured decisions, which probably occupy the real-life manager during most of his working life, are typically absent from management games. This has no consequence educationally, because students have ample opportunity to practise such decisions elsewhere.

Table 3
Translation of terms

<table><tr><td>Term from Table 1</td><td>Equivalent in Management Game</td></tr><tr><td>Short</td><td>During a round</td></tr><tr><td>Long</td><td>Between rounds</td></tr><tr><td>Unimportant</td><td>Simulated by computer</td></tr><tr><td>Important</td><td>Decided by player</td></tr></table>

Table 4  
Information Systems in a Management Game

<table><tr><td></td><td>During a round</td><td>Between rounds</td></tr><tr><td>By computer</td><td>Operational program</td><td>Preprogrammed decisions</td></tr><tr><td>By player</td><td></td><td>DSS for player</td></tr></table>

## 4. INFOLAB: A new type of management game

## 4.1. Overview

This section describes the design of a management game, (provisionally named INFOLAB, a laboratory for information systems) that can be used as an environment for the development and use of information systems. It was initiated by Kleijnen [16]; a preliminary description was given in [4]. As in a conventional management game, players make management decisions for simulated organizations in a competitive environment. In the prototype the organizations are modeled after industrial companies, but in future the type of organization may be defined by the game administrator.

The main difference between INFOLAB and conventional management games is in the output. Conventional management games produce standard reports, i.e., financial statements and statistical summaries. In INFOLAB, the player has to specify what types of events should be recorded. The output consists of the raw data for those events. The player is free to do no accounting and base his decisions on cash level (which the bank will report free) and market research reports. The player who wants to use other data for decision making will have to build an information system to process the raw data, because the amount of data will be too large for manual handling.

Our design is related to the Minnesota experiments [7] and subsequent research [5,13,14,8]. However, these applied preprogrammed DSS's, using the standard output of a conventional business game as input, to investigate the relation between type of DSS and decision quality, whereas our research centers on information systems design.

In accordance with Table 4 we distinguish two versions:

INFOLAB-1, where the information system will supply data that can be used by players at the end of each round.

INFOLAB-2, where it will also supply data to a decision system built into the game.

So INFOLAB-1 supports Decision Support Systems and bureaucratic information systems as well as control system. INFOLAB-2 also supports operational information systems. In INFOLAB-1 information processing is divided into two distinct phases: data collection and data reduction. The first phase is executed during a round. Specification consists of pinpointing the variables that have to be measured. The second phase is executed between rounds. This part of the information system is defined by user-written programs. For these, any convenient language or program package, including spreadsheets and database systems, may be used. In INFOLAB-2 the data is collected as well as analyzed during a round, to provide inputs to the decision system. To this end, a special language will be designed that allows players to define procedures inside the simulated environment. The design of this language poses a number of problems detailed later. Because of its difficulty, implementation of INFOLAB-2 will not be started until the mechanisms of the game and player attitudes have been studied.

## 4.2. Outline of the game

The gaming model of INFOLAB is derived from MAGEUR, a traditional management game developed for Erasmus University [3]. The main entity is the firm, which is managed by the player. Each firm produces a number of products, which may be chosen from opportunities supplied by research. A product is produced by a product line which employs machines, workers and factory space. Production also entails the use of materials. Firms may switch production factors among different products, discontinue products and introduce new products as they see fit. Sales are made to simulated consumers who choose among competitors on a number of determinants, such as price, quality, and marketing effort. Typically, a firm produces some tens of product batches and effects some hundreds of separate sales transactions for each product. All production and sales results are reported separately; accounting and statistical computation are the task of the participants. However, the game does some operational accounting, e.g., it will compute the cash level as a base for interest charges and it will compute the stock level of materials and finished products to establish production and sales opportunities.

Most of the rules governing the operation of the game will be built into the game program, (e.g., sales are possible only if a product is in stock) but players may be given some scope for the definition of rules, (e.g., a reorder level and an order quantity may be specified).

The game program is divided into two parts: INFOLAB will provide the interface with the participants; INFOMARK computes the results for a round. Supplementary programs BANKER and STOCK will establish the interface with the banker and the stock exchange. The division of the system into separate programs is motivated both by design considerations and by the implementation in an environment with limited program space (currently Turbo Pascal).

Apart from the usual decisions on production, marketing, and finance the participant can define two types of data to be collected: event data and state data. Collection of event data takes place at any occurrence of the stated event; collection of state data (inventory taking) occurs at timing intervals specified by the participant. For any data item collected a price must be paid. Because INFOLAB is a discrete event simulation, the number of different events is finite, so there are a finite number of possible measurements. The set of actual measurements will be defined by the player by explicit choice from a given set. To choose appropriate measurements, the player must thoroughly study the model of the firm: The full range of outputs will be far too expensive.

## 4.3. Decision support

When INFOLAB-1 is used for decision support the participant will get ample time (say a week per round) to study the results of the previous rounds. The choice of a programming tool to investigate this data is left to the participant. However, it will be too large for manual handling. Exploratory research will attempt to establish a relation between tools and models used and subsequent results. INFOLAB is free of prejudice; it allows the use of conventional financial reporting systems as well as Decision Support Systems as a base for managerial decisions. In a later phase we want students in Information Systems to cooperate with students in Marketing, Finance, and Accounting, with the former as information system builders and the latter as users.

## 4.4. Bureaucratic decisions

So far we have assumed that players in IN-FOLAB-1 will only take strategic decisions. However, there is no logical objection to introducing bureaucratic decisions, e.g. by enlarging the number of products, the number of production factors involved in the production of any product, or the number of research proposals that have to be studied before a possibly successful product is found. Bureaucratic decisions, such as pricing decisions for a large number of products may be taken by programs using the data of the latest round. This follows research on robot players in management games [9,15,19].

## 4.5. Control systems

The principal aim of management control systems is to establish whether management instructions have been carried out correctly. The introduction of a management control system into INFOLAB makes sense only if actual operations may differ from the instructions issued by the player and if the player can influence those differences. To this end we plan to introduce daemons into the game. A daemon is a mechanism that changes some specific variable, e.g., a cash daemon reduces the cash level at unpredictable moments. Daemon activity encompasses fraud and other crimes, human errors, machine failures, epidemics, strikes and acts of God. The initial level of deamon activity will be determined by the game administrator, but it may be diminished by a management control system, supported by a pertinent information system. Technically, there is no difference between information system building for decision support and information system building for management controls, as the same tools may be used. However, the user groups are quite different (a typical use of our game for the study of management control system is in EDP audit courses).

## 5. Conclusion

Management games can be used to better define the distinction between different types of information systems and their use in organizations. Consequently, research in the problems of informations systems development in management games will be valuable for a wide range of real-life applications. Future research will center on an environment where students will design an information system and a decision system for a simulated firm. As stated before, the central design problem of this advanced system is the design of a language that may be used to define such systems.

## References

[1] S.L. Alter: Decision support systems: current practices and continuing challenges. Addison-Wesley, Reading Mass., 1980.

[2] R.N. Anthony and J.S Reece: Accounting text and cases. Irwin, Homewood III., 1979.

[3] R.J. Casimir: Mageur, Handleiding ondernemers. (Mageur, Participants manual) Erasmus University, Rotterdam, 1985.

[4] R.J. Casimir: INFOLAB, een laboratorium voor informatiesystemen. (INFOLAB, a laboratory for information systems) Reeks “ter discussie” 85.14 (working paper), Tilburg University, Tilburg 1985.

[5] J.F. Courtney, G. DeSanctis and G.M. Kasper: Continuity in MIS/DSS laboratory research: the case for a common gaming simulator. Decision sciences Vol 14 No 3 (july 1983), pp 419–439.

[6] T.A. DeFanti: The mass impact of videogame technology. in M.C. Yovits (ed.): Advances in Computers. Vol 24, Academic Press, Orlando, 1984.

[7] G.W. Dickson, J.A. Senn and N.L. Chervany: Research in management information systems: the Minnesota experiments. Management science Vol 23 No 9 (may 1977) pp 913–923.

[8] G.W. Dickson, G. DeSanctis and D.J. McBride: Understanding the effectiveness of computer graphics for decision support: a cumulative experimental approach. CACM Vol 29 No 1 (jan 1986), pp 40–47.

[9] D. Dickinson and W.R. Ferrell: Fuzzy set knowledge representation in a system to recommend management decisions. in L.B. Methlie and R.H. Sprague (eds.): Knowledge representation for decision support systems. North Holland, Amsterdam, 1985.

[10] C. Elgood: Handbook of management games (2nd ed.). Gower, Aldershot, 1981.

[11] G.A. Gorry and M.S. Scott Morton: A framework for

management information systems. Sloan management review, Vol 13 No 1 (fall 1971), pp 56–70.

[12] G.P. Huber: Organization science contribution to the design of decision support systems. in G. Fick and R.H. Sprague (eds.): Decision support systems: issues and challenges. Pergamon press, Oxford, 1980.

[13] S.L. Jarvenpaa, G.W. Dickson and G. DeSanctis: Methodological issues in experimental IS research: experiences and recommendations. MIS quarterly Vol 9 No 2 (june 1985).

[14] G.M. Kasper and R.P. Cerveny: A laboratory study of user characteristics and decision-making performance in end-user computing. Information and management 9 (1985) pp 87-96.

[15] J.P.C. Kleijnen: Computers and profits. Addison-Wesley, Reading Mass., 1980.

[16] J.P.C. Kleijnen: De rol van wiskundige modellen en technieken in de bestuurlijke informatica. (The role of mathematical models and techniques in information systems) Informatie 23 Nr 6 (june 1981), pp 387–393

[17] J.H. Moore and M.G. Chang: Meta design consideration in

building DSS. in J.L. Bennett (ed.): Building decision support systems. Addison-Wesley, Reading Mass., 1983.

[18] D.L. Parnas: Software aspects of strategic defense systems. CACM Vol 28 No 12 (dec 1985), pp 1326–1335.

[19] M. Shubik, G. Wolf and S. Lockhart: An artificial player for a business market game. Simulation and games Vol 2 Nr 1 (march 1971), pp 27–43.

[20] H.A. Simon: The new science of management decision (3d ed.). Prentice Hall, Englewood Cliffs N.J., 1977.

[21] C.B. Stabell: Decision support systems: alternative perspectives and schools. in E.R. McLean and H.G. Sol (eds.): Decision support systems: a decade in perspective. North Holland, Amsterdam, 1986.

[22] R.J. Thierauf: Decision support systems for effective planning and control. Prentice Hall, Englewood Cliffs N.J., 1982.

[23] W.J.H. Van Groenendaal: Towards a workable definition of DSS. 8th European conference on operations research. Lisbon, Portugal, sept 1986.

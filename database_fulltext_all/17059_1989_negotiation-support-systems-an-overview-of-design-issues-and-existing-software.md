---
otero_id: 17059
otero_key: "H2DA3F9J"
title: "Negotiation support systems: an overview of design issues and existing software"
authors: "M. Tawfik Jelassi; Abbas Foroughi"
year: "1989"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(89)90005-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Negotiation Support Systems: An Overview of Design Issues and Existing Software

M. Tawfik JELASSI \* and Abbas

FOROUGHI \*\*

\* INSEAD, 77300 Fontainebleau, France. \*\* Indiana University, Bloomington, IN 47405, USA

Negotiation Support Systems (NSS) are a special class of Group Decision Support Systems which emphasize computerized assistance for situations in which there is strong disagreement on factual or value judgments among group members. This paper first discusses negotiation structuring issues that should be taken into account when designing NSS. These issues include behavioral characteristics and cognitive perspectives of negotiators, communication needs of different bargaining settings, determination of each party's real interest(s), generation of options for mutual gain, and data accuracy and consistency. The paper then reviews negotiation theories used as the basis for designing NSS and provides a comprehensive survey of existing software in the area of computer-supported negotiation.

Keywords: Negotiation, Negotiation Structuring, Group Decision Support Systems, Computer-Supported Negotiation, System Analysis and Design, Software Packages.

![](/api/attachments/H2DA3F9J/fulltext/images/77fdde2f88cf227f90b739895c0267764f6601689ffa95850b0b8751e1e4fe3c.jpg)

M. Tawfik Jelassi is Associate Professor of Information Systems at the European Institute of Business Administration (INSEAD). Prior to that, he was on the faculty of the Indiana University School of Business. Dr. Jelassi received a Ph.D. in Computer Applications and Information Systems from New York University, and Diplomas in Computer Science and Business Administration from the Université de Paris-Dauphine and the Université de Tunis. His research interests include Group Decision Support Systems, Computer-Assisted Negotiation, Multiple Criteria Decision Making, and Database Applications. He has recently contributed articles to the European Journal of Operational Research, Journal of Management Information Systems, Decision Support Systems: The International Journal, Information and Management, and the European journal Interfaces. Professor Jelassi also serves as a consultant to business and government in several countries.

## 1. Introduction

Negotiations have often been seen as an “art”, based on “interpersonal skills, the ability to convince and be convinced, the ability to employ a basketful of bargaining ploys, and the wisdom to know when and how to use them” [42, p. 8]. Most successful negotiators have picked up their skills haphazardly and cannot explain the reasons for their success [45]. There is a myriad of literature describing the “art” of negotiating and presenting behavioral guides for developing negotiation skills [49].

An emerging school of thought views negotiation as a “science”. Sperber [45] reported that in the last five years, over 200 articles had been written about experiments covering all aspects of negotiations. He defined negotiation as “the science of accurate observations, realistic assumptions, correct factual analysis, logical inferences, planned behavior and optimal preservation for each moment of a changing bargaining situation” (p. 9). Negotiation skills and abilities are no longer considered a matter of personality or creativity; the negotiation process is seen as having a rational, knowledge-based explanation [29].

Recent advances in computer technology and information systems provide the possibility of assisting group decision making activities in cooperative as well as conflicting settings [25]. Among these advances is the emergence of the Negotiation Support Systems (NSS) concept. These are interactive, computer based tools intended to support negotiating parties (and possibly a human mediator) in reaching an agreement. NSS enable the elimination of communication barriers among negotiating parties, providing techniques for structuring decision analysis and for the systematic direction of the patterns and timing of negotiations. Moreover, they provide communication technologies such as electronic messaging, local-and wide-area networks, and teleconferencing, as well as computer technologies such as multi-user operating systems, public and private-access databases, and facilities for data management and analysis. Decision support software available in NSS include modeling capabilities such as decision trees, risk analysis, forecasting methods and multiattribute functions, as well as structured group methods like Electronic Brainstorming, Nominal Group and Delphi techniques.

![](/api/attachments/H2DA3F9J/fulltext/images/48d1555e4e22d5d92fb7eca806f3dc733ea796314233fcb294147dbabfee8ee4.jpg)

This paper focuses on this emerging managerial support technology called NSS. It is based on the system definition and general capabilities introduced above. Section 2 stresses the differences between soft and hard negotiations. Section 3 discusses design issues drawn from negotiation structuring and investigates the degree to which they have been integrated in available NSS. The discussion also includes an overview of negotiation theories used in existing systems. Section 4 provides a review of some existing negotiation support software. Section 5 concludes the paper with suggestions for future research needed to further improve NSS.

## 2. Soft and Hard Negotiations

Negotiation situations can be seen as lying on a continuum from “hard” to “soft” [11]. “Soft” negotiations are also referred to as “integrative” or “win-win” bargaining [33]. These occur between friendly parties who value their relationship and desire to reach a jointly beneficial agreement. In this type of negotiation, the goals of the parties are not mutually exclusive, and it is possible for both sides to achieve their objectives. For example, a family deciding on what type of car to buy or on where to go on vacation is engaged in soft, integrative negotiation. Soft negotiations are also common in organizational group decision making where there may be opinion differences, but where all parties are united in desiring an optimal solution which is beneficial to all [5].

At the opposite extreme of the negotiation continuum is “hard”, “win-lose”, or “distributive” bargaining [33,11]. Here conflicting parties want to enforce their own positions and are not in a hurry to compromise. “Hard” bargaining is characterized by the fact that (1) the goals of each party are in direct conflict with those of the opposing one; (2) resources are fixed and limited; and (3) each party wants to maximize its share of the resources. Examples of negotiation situations having such characteristics include labor/management disputes, arms control negotiations and peace talks between potentially hostile parties in pursuit of their own interest. It is for this “hard” type of negotiations with its specific features and problems that NSS have been developed. The following section discusses negotiation structuring factors and the degree to which they have been taken into consideration when designing NSS.

## 3. Negotiation-Structuring Factors and Their Relevance to NSS Design

Five factors impact the structuring of a negotiation and are believed to be relevant to NSS design. These factors are mainly derived from Fisher and Ury [11] and they are:

A. Separate the people from the problem;

B. Provide communication between negotiators;

C. Help negotiators identify their real interests;

D. Generate options for mutual gain; and

E. Use objective criteria.

## A. Separate the People from the Problem

Separating the people from the problem helps reduce the negative (and sometimes destructive) impact that personal misperceptions, emotions, and bad communication have on the negotiation process. In this context, it is important to face the problem, not the people. The following sub-sections discuss individual and group characteristics of negotiators, their needs, personal approaches to resolving the conflict, motivational orientation, and semantic disagreements.

1. Individual and Group Characteristics of Negotiators

Recent research has demonstrated the importance of taking into account individual and group characteristics of participants as well as situational variables of group decision making and negotiation $[11,33,46,15]$ . Swap $[46]$ and Gouran $[15]$ identified characteristics which decision makers bring with them to a negotiation situation. Each individual negotiator has distinctive characteristics such as personality, sex, age, race, status, socio-economic background, competence and motivation. Group characteristics include political orientation, leadership, complexity of the task and circumstances, size of the group and history of its members. It is important to include these characteristics in the system design framework in a way that integrates both the technical and the behavioral issues involved [for more details, see $(24)$ ].

Moreover, the diverse nature of conflicting parties increases the likelihood that they will come to the negotiation session not only with different individual/group characteristics and views of the issues at stake but also with varying assumptions and perceptions about the negotiation process itself. For this reason, it is essential to set the stage for the negotiation by establishing rules and obtaining commitment from each party for the resolution of the conflict [2]. The NSS can be used by a mediator to input specific rules agreed to by disputants including such issues as time lines, responses to rule violations, and discussion protocols. These rules can be formatted as a contract and printed for both negotiating sides to sign. As a further step toward creating a positive atmosphere for the negotiation, NSS can support the use of Nominal Group Technique [8] to facilitate the elicitation of common goals and help negotiators focus on the advantages of a negotiated settlement of their differences. The NSS could display the separate inputs on a public screen, and a mediator could then help restate and edit items and display and/or print the advantages agreed upon.

## 2. Negotiators' Needs

Nierenberg [37] contented that Maslow's [35] typology can help describe negotiators' needs and explain the driving forces behind a party's bargaining positions. Maslow's hierarchy recognizes seven levels of needs: physiological needs, safety and security needs, love and belonging needs, esteem needs, needs for self-actualization, needs to know and understand, and aesthetic needs. Nierenberg suggests that a negotiator motivated by security will seek an agreement guaranteeing safety, protection and assurances, while a bargainer motivated by esteem seeks recognition or social prestige. A negotiator with a strong need for achievement will set goals and targets to meet his/her objectives. A party with a high need for affiliation will want to develop and maintain relationships with others and not compromise them. A negotiator with a high need for power will want to control the bargaining situation and can come into high conflict with another negotiator who also has a high need for power.

Moreover, negotiating parties may often have been in dispute for some time before formal negotiating sessions are organized and have not had the opportunity for face-to-face discussion. A formal negotiation should be structured so as to create an atmosphere in which both parties feel free to express their particular needs and concerns. Recognizing the existence of such needs and trying to help conflicting parties formalize them is a desirable feature to have in NSS. Nominal Group Technique [8], with the enforcement of non-interruption rules, can enable each side to express its needs without distraction.

## 3. Negotiators' Individual Approaches to Conflict

Another way of explaining individuals' behavior in negotiating situations is in terms of their approaches toward conflict and negotiation. Five different perspectives that individuals take toward conflict have been identified [33]:

\- Contending or positional bargaining involves a party trying to convince opponents to accept a position favoring his/her own interest, by using persuasion, manipulation and concealment of true position;

\- Accommodating involves trying to help the other party meet its objectives;

\- Compromising means splitting the difference, satisficing but not optimizing;

\- Collaborating involves parties working together to optimize their joint outcome, as in group problem solving; and

\- Avoiding or leaving the negotiating situation when a participant fears conflict, when the issues are not worth bargaining over, or as an attempt to delay negotiations.

The NSS can influence the approach to conflict taken by negotiators by creating an atmosphere that stresses order, rationality, equality and empathy with the other side. For instance, the NSS can help focus on issue resolution by keeping track and posting reminders of session times and deadlines. Also public display helps to focus attention on one issue at-a-time to avoid topic wandering or abstraction and to keep the pace of the discussion going. Consideration of all issues could be ensured by providing time limits for discussion and automatic sequencing through the list of issues. However, in some negotiation settings, it may be important to consider several issues simultaneously [4] since this technique, that Pruitt [40] calls “logrolling”, leads toward more integrative agreements where a higher joint utility could be reached. In such situations, the NSS should display the entire content for discussion.

Often the relationship between negotiating parties is asymmetric in terms of power or influence, and one side may feel intimidated by the other in the course of the negotiation. The NSS can help equalize participation to prevent domination by one side. This could be achieved by setting time limits on verbal discussion and by, for instance, channeling communication as electronic messages.

## 4. Negotiators' Motivational Orientation

Negotiators have been shown to differ also in their motivational orientation. Rubin and Brown's [43] review of research on the role played by motivational orientation identified three general types of orientation: individualistic, cooperative and competitive. A negotiator with an individualistic motivational orientation will only be concerned with maximizing his/her own outcome(s). A negotiator with a cooperative motivational orientation will be willing to work with the other party to seek a solution which maximizes their joint outcome(s). A negotiator with a competitive motivational orientation will want to maximize his/her gain(s) over the opponent, as well as defeat him/her. In reality, there are many intangible motivations which determine the way a bargainer behaves in a negotiating situation. These variations in motivational orientation are mainly due to individual personality, attitudes and predispositions, situational factors such as instructions from a negotiator's constituency or cues given by an opponent about how she/he will behave, and the actual and perceived reward structure for a certain behavior.

“Negotiation Edge” is a software package that was developed to help decision makers identify their personal negotiation styles and strategies. The latter are derived from self assessment of the individual user as well as from assessments of other parties.

Since negotiating sides can be so diverse in terms of personal characteristics, emotional needs, motivation, and approach to conflict, NSS should provide the opportunity for interaction to facilitate negotiators' understanding of, and empathy with, the position of the opposing side. A type of role reversal could be accomplished by displaying the list of issues at stake on each party's private screen and asking each side to assign preference ratings to the issues according to their perception of the other side's values. The two sorted lists could then be displayed on the public screen for discussion.

## 5. Semantic and Syntactic Differences between Negotiators

In many group decision making situations the lack of effective communication can be detrimental to solving the problem at hand. There is often confusion over semantics, and misinterpretation of a term can impede the decision making or negotiation outcome(s). In such situations, techniques such as the PRECISION model [36] can be employed to ensure effective communication among negotiators through the use of a more precise and specific language. This is accomplished through “reframing” techniques and pointers which help individuals redefine and refine imprecise and vague language.

“Linguistics” differences are recognized and addressed in the NSS called MEDIATOR. This system attempts during the prenegotiation phase to resolve these differences in the two parties’ conflicting views of the problem [20]. The technique used in MEDIATOR is called “view integration”; it employs database concepts (such as functional dependencies) to detect semantic and syntactic disagreements among participants [for more details, see (21)].

## B. Communication Between Negotiators

Jarke [19] identified four factors which influence communication between negotiators. These factors are: spatial distance, temporal distance, commonality of goals and control.

1. Spatial distance among individuals has a great impact on the bargaining situation. In establishing a negotiating scenario, participants should keep in mind that more cooperative, integrative-oriented parties are more comfortable in closer proximity. This contrasts with competitive parties which prefer greater physical distances from one another and are more apt to place physical barriers (such as furniture) to separate them from their opponents [33].

DeSanctis and Gallupe [9] identified four types of GDSS environments based on duration of the decision making process and the spatial distance factor. These types are: decision room, local decision network, teleconferencing, and remote decision making (see fig. 1). The four GDSS environments listed above could also be used or adapted for negotiation situations.

(a) The decision room creates an electronic version of a traditional meeting situation. The room is equipped with special GDSS facilities such as a U-shaped table with a microcomputer or a mainframe terminal in front of every participant. Data inputs and private information displays take place at the individual station level. Both face-to-face, verbal interaction and communication via computer messaging are possible. A large video screen is used for displaying to the group summary and analysis of data. The informal interaction and personal contact which occur when negotiators are in one room, as in the NSS NEGO [28], increase the possibility of compromise and conflict resolution.

(b) A local decision network can be established to

![](/api/attachments/H2DA3F9J/fulltext/images/d3947ad7241bdc2a3ed1d3489bb9fb260fc85d7ff12dafbd8972a71f1449c9d0.jpg)  
Fig. 1. Taxonomy of GDSS [from DeSanctis and Gallupe (1985)].

PROBLEM-SOLVING PROCESSES

support group members on an ongoing basis. Each decision maker has a microcomputer or workstation in his own office. Common GDSS software and databases are stored on a central processor. Group participants can communicate with each other and with the central processor through a local-area network. Face-to-face meetings are eliminated, but there is more flexibility since it is not necessary for all participants to be at the same place at the same time.

(c) Teleconferencing provides communication between two or more remote groups by linking decision rooms together through audio and visual facilities.

(d) Remote decision making provides continuous communication between remotely located decision makers meeting on a regular basis.

Because decision-making activities in negotiation settings involve several participants in sometimes scattered locations, its communication needs are very specialized [6]. Heterogeneous information styles must be converted into standard message formats that can be recognized and understood by all parties. Multiple channels for formal as well as informal communications are needed. Structured communication interfaces should facilitate the independent generation of ideas or judgments, assure equal discussion opportunities for all participants, and provide organized feedback to the group. Remote decision settings require unstructured communication interfaces such as on-line and public notepads, electronic mail and bulletin boards and electronic mail to make up for interpersonal communication needs that structured interfaces cannot provide. In addition, remote, distributed systems must provide a high-level communication protocol allowing knowledge sharing and opinion exchange among decision makers.

2. Temporal distance refers to whether decision making is undergone simultaneously or at different points in time. In traditional meetings and teleconferencing, decision makers provide their inputs and come to a decision at a particular point in time. In contrast, electronic mail and bulletin boards as well as computerized conferencing allow decision makers to give their input at different points in time.

![](/api/attachments/H2DA3F9J/fulltext/images/22425d4782cdfd886b2fa612b2f96ef0c4922b12d08b77eecae6a0d479600842.jpg)  
Fig. 2. Modes of GDSS Usage [from Jarke and Jelassi (1986)].

3. Commonality of goals refers to the degree of cooperativeness among negotiators which significantly affects both the required communication needs and the manner in which an agreement is reached. Jarke and Jelassi [21] develop a model for classifying negotiation processes which views the group problem solving process as progressing along two dimensions. These are the problem solving process (problem recognition, design of alternatives, choice of best solution) and group processes (gathering and evaluation of information, knowledge sharing, and negotiation).

According to the model, negotiation processes have the purpose of moving decision makers from the state of recognizing a vaguely defined problem (lower left corner of fig. 2) to a state of making an agreed-upon joint decision (upper right corner of fig. 2). The mode or manner in which a decision is reached depends upon the degree of cooperativeness existing among the decision makers. There are three distinctive modes: pooled, cooperative, and noncooperative.

(a) Pooled mode refers to a situation in which there is a great deal of cooperation, with the group collaborating so much that the individuals almost act as a single decision maker.

(b) Cooperative mode refers to communication among decision makers being organized into various phases between which individual participants make decisions themselves for presentation to the group. In such a situation, decision makers may have difficulty understanding and accepting each other's solutions and may need to negotiate for the final decisions.

(c) Noncooperative NSS mode refers to a situation in which individual decision makers already have their own individual problem representations and preference structures. In this case, negotiations must integrate these often conflicting, incompatible problem representations into a common solution. Such negotiation situations in which competitive parties oppose each other need particular communication channels. Hostile, competitive parties do not want to reveal all of their information, motives and plans to the other side. Each party needs to have access control to private data and problem representations and be supported by negotiation tools. The MEDIATOR NSS first helps each negotiator formulate his/her initial bargaining position through the use of a database view definition mechanism. It then guarantees privacy of the constructed view by providing him/her unique access rights. In addition, each negotiator (or "player") has access to the public data (base data and joint problem representation), and shares semi-public data which is accessible only to a particular player and to the human mediator supported by the system. The negotiating process in MEDIATOR involves the human mediator assisting the players in consensus seeking by exchanging information and compromising where consensus is not possible. The system helps the mediator in supporting compromise by using axiomatic solution concepts and concession making procedures stored in the NSS model base. The mediator can make "what-if" analyses of possible alternatives for the problem solution, use database capabilities to include or exclude sets of alternatives from consideration, employ alternative ranking procedures to redefine criteria sets, or display aggregated utilities of coalitions. In summary, MEDIATOR both protects the privacy of negotiators and helps them directly as well as through a third party in reaching a consensus (see fig 3).

![](/api/attachments/H2DA3F9J/fulltext/images/d4002ffbaa2eb414ceabb7b9cc0d3a77d4a263b56f880acecf9b37d12c8e1ea5.jpg)  
Fig. 3. MEDIATOR Design-Communication through Data Sharing [from Jarke, Jelassi and Shakun (1987)].

4. Control of the negotiation situation can either be in the hands of the group, who makes a democratic decision, or in the hands of a mediator. Three different levels of control can exist in a negotiation situation. First, decision making can be entirely democratic, with the active participation of negotiating parties. Second, decision making can be semi-hierarchical, aided and facilitated by a mediator. Third, the decision making process can be hierarchical, or entirely in the hands of a third party arbitrator [19]. These three levels of control are described in more detail in the following sub-sections.

(a) Democratic, Participative Decision Making. Throughout the negotiation process, the interests of both negotiating sides should be supported and protected to create a truly democratic atmosphere. The NSS should help negotiators in communicating their opinions about the negotiation process through electronic mail and/or teleconferencing. Other matters of concern are whether individual outputs will be public or anonymous, the negotiation support tools to be used, whether there should be a time limit, and if negotiators can modify individual proposals after they have been submitted. Negotiators should be able to evaluate alternatives individually by using a set of interactive multiple criteria decision making methods in the model base. The NSS should also provide structured communication interfaces such as Delphi and Nominal Group Techniques, which facilitate independent generation of ideas and provide mechanisms guaranteeing the rights of all negotiators to equally participate in the discussions.

(b) Semi-hierarchical Decision Making Aided by A Mediator. The NSS MEDIATOR introduced earlier is useful in situations which are complex enough to require support from a third party. In the present version of this system, the role of the human mediator is to support negotiators, but not to decide on the outcome of the negotiations himself. Jarke, Jelassi and Shakun [20] mention that the system could be used in situations where a mediator chooses the solution for the problem at hand, or where the NSS supports the negotiators directly without the intervention of a human mediator.

(c) Third Party Arbitration. The Conflict Analysis Program (CAP) is an example of NSS where an external arbitrator controls the decision making process [12]. The system is interactive and microcomputer based; it supports a third party in his analysis of the conflict situation and his search for the optimal solution. The arbitrator gathers information about the conflict situation and the parties in it and uses this information to create a “realistic” game-theoretic model of the situation. He/she uses the model to eliminate unfeasible outcomes. Next, the arbitrator is supported by CAP in ordering each player’s preferences, then performs a stability analysis to find an equilibrium or outcome which is rational or stable for all players. Here an important degree of responsibility and trust rests upon the arbitrator who performs the tasks listed above without any interaction with, or input from, the parties involved. It could be argued that if an organization chooses to use an arbitrator, it is preferable to have the decision making process supported “scientifically” by NSS rather than done perhaps more haphazardly.

## C. Help Negotiators Identify their Real Interests

In order to plan for a negotiation, each player (or party) should try to anticipate the major events that will occur during the session and be prepared for them [33]. He should first determine his goals, prioritize them in order of importance, and combine them into “packages” of issues for presentation and discussion with the other party. He should also gather information about his opponent, his objectives, his personality, history and negotiating style. This analysis of the opponent is important because negotiations represent interdependent relationships between bargaining parties. The interdependence can be contrient, where the achievement of one person’s goal will prevent the achievement of the other’s. It can also be promotive, where the achievement of one person’s goal helps others achieve their goals as well. The present type of interdependence has a major impact on the evolution of the negotiation process. Because of the complexity of bargaining and the difficulty of reaching the optimal agreement, negotiators often use both decision and negotiation theories to determine their own interests first. Then based on a comparison with the other party’s interests, they strive for the best outcome [33]. Examples of these theories are given below.

1. Multiple Criteria Decision Making. Multiple criteria decision making (MCDM) accounts for numerous and conflicting objectives among different interest groups [16]. Individual decision makers have their own goals, criteria, and attributes separate from the opposing participants. However, they may share some, none or all of these characteristics with each other. Furthermore, criteria are usually conflicting; the improvement of one (or some) of them can be achieved only at the expense of others. The task of the group is to reduce the different individual preferences among criteria to a single collective preference. Once this common interest or preference has been identified, there is a basis for negotiation. Many MCDM methods can be used here; they can be categorized as weighting methods, sequential elimination methods, mathematical programming methods, and spatial proximity methods [for more details, see (34)].

Jelassi [23] traced the evolution of computerized MCDM models from the time when they were “stand-alone” methods to their current status of being interactive and intelligent decision support systems. MCDM methods are very beneficial and suitable for GDSS and NSS because of their integration of multiple views of a problem and their use of both qualitative and quantitative criteria. They are interactive and facilitate easy revisions of individual and group problem representations and opinions. MCDM methods have been used for preference elicitation and aggregation, alternatives generation, and solutions rankings. They are adaptable to both a message-passing and database centered setting, and can be implemented in democratic as well as hierarchical group decision modes. Knowledge sharing and negotiation can be supported by adding database capabilities to multicriteria DSS [22].

2. Game Theory. Game theory is a mathematical technique for the analysis of situations where there is a conflict of interest [48]. For this theory, conflict consists of participants freely selecting various outcomes from a list of alternatives. The different outcomes may put the players against each other, but there may be room for cooperation. Game theory places the essential elements of conflict situations into mathematical models and uses the scientific approach to analyze them. Zero-sum games represent bargaining situations where one party wins and the other loses, such as in “hard”, distributive negotiations. Mixed-motive or non-zero-sum games are more realistic since they represent situations where the interests and outcomes of the parties are both in conflict and congruent, so that one, both, or neither may win.

3. Conflict Analysis. Fraser and Hipel's [13] method considers conflict as a game with individual players having several options. Each negotiator chooses a strategy or a set of options leading to an agreement. He/she has preferences as to the negotiation outcomes. Arranging these outcomes in decreasing order forms a preference vector. According to conflict analysis, an outcome will persist if and only if it is stable for all participants. Therefore, each feasible outcome is analyzed for stability for each player. An outcome is considered stable if it fulfills one of the following three conditions:

(1) The player cannot improve his position unilaterally;

(2) The player can make one or more unilateral improvements for a more preferred outcome, but some or all of the other players can subsequently improve their own position and thereby weaken his; or

(3) The player can make a unilateral improvement for a more preferred outcome, but two or more of the other players can simultaneously improve their individual positions thereby putting him in a less preferred position.

Possible resolutions of the conflict are the equilibria, or outcomes which are stable for all players. Conflict analysis and its extensions can be applied when: (1) players have differing views of the problem; (2) the conflict is unstable over time; or (3) when the analyst has incomplete information. Conflict analysis was used as the basis for developing both the CAP [12] and DECISIONMAKER [13] software systems.

4. Group Decision Theory. Group decision theory (or decision analysis) has evolved from individual decision theory. It prescribes how groups should make decisions in situations which are either risky or riskless (in the sense that the consequences of the decision are uncertain or certain) [10]. This consists of aggregating the individual participants' subjective choices, creating a consensus probability. This reflects the group's evaluation of the likelihood of joint returns. By combining the members' conflicting utilities, the group arrives at a collective utility (or social welfare) function. This function along with the participants' consensus probability are then combined, leading to the selection of the best group outcome. The criterion for choice is the maximization of the group's expected utility. Group decision theory has been used to predict outcomes, in particular in negotiation situations where there is partial information and/or unequal power among the parties involved [10].

5. Generalized Approach for Structuring and Modeling Negotiations. Kersten and Szapiro [29] developed a general approach to structuring and modeling negotiations based on the concept of “pressure” as an alternative to utility theory. This concept is more general than utility and considers internal values and external influences that affect a decision maker. Pressure would explain how a decision maker could make different decisions, not because of a utility change, but due to a difference in time allotted or a gain of new knowledge. This approach considers the effects of pressure in the soft constraints leading to a change in the feasible set and negotiation space and resulting in a compromise. Kersten and Szapiro’s approach builds a model of negotiations assuming known hard and soft constraints. In the case where a compromise is predicted, the shortest path (smallest number of iterations) could be sought. If an ideal compromise is known but does not satisfy the problem constraints, a goal programming model can find the decision which is both feasible and closest to the ideal. Kersten [28] used the above mentioned approach to develop his NSS called NEGO.

6. Evolutionary Systems Design. Traditional analysis techniques such as game theory and MCDM assume that decision makers' preferences or utility functions are stable. Sociology and psychology theorize that values are not stable, but change in negotiation situations. The work of Crawford [7] and others has studied more dynamic aspects such as mutual learning and decision making under uncertainty. Traditional decision analysis techniques are considered too heavily mathematical and oriented to optimal modeling to be useful for real decision problems.

To accommodate dynamic and iterative aspects of decision making, Shakun [44] developed a methodology called Evolutionary Systems Design. EDS visualizes negotiations as a collective process of searching for or designing a mutually acceptable solution. Participants are seen as playing a dynamical difference game in which a coalition of players is formed if it can achieve a set of agreed-upon goals [17]. ESD was designed for use in complex contexts involving multi-player, multicriteria, ill-structured, and dynamic problems. It proves to be a useful methodology in supporting negotiations and provided the base for building the NSS MEDIATOR.

## D. Generate Options for Mutual Gain

There are several techniques which are used to generate alternative solutions. These techniques are:

1. Brainstorming consists of small groups generating many possible solutions and recording them. Emphasis is placed on spontaneity and an uncritical free atmosphere [38].

2. Interactive Brainwriting Pool Technique is brainstorming in which participants write down their ideas instead of stating them [14]. The advantages are that the absence of verbal criticism stimulates creative thinking, dominance of strong personalities is avoided, and all ideas are recorded.

3. Surveys or questionnaires are distributed to large groups of individuals who are asked to list all possible solutions.

4. Nominal group technique first consists of having each negotiator write as many solutions as he can generate [8]. Then, in small groups, these solutions are read aloud, written for public display, and voted on and prioritized by the participants.

The idea generating techniques defined above have shown limitations in their effectiveness for the following reasons. Brainstorming in face-to-face groups suffers from fear of social disapproval, anxiety about oral communication skills, presence of an authority figure, and the tendency to copy responses made by high-status group members [3]. Nominal Group Technique provides initial anonymity but still requires a verbal sharing of ideas. Brainwriting provides partial anonymity by requiring that ideas be written, but complete anonymity is impossible because handwriting can be identified by other members. Local area network communication, microcomputer processing power and graphic information display have enabled the development and use of Electronic Brainstorming. Recent research shows that automated brainstorming, while neutralizing many group effects plaguing the use of brainstorming, provides anonymity and allows participants to freely express their true feelings.

In addition to the above idea generating techniques, another approach helps parties define their underlying needs and develop solution alternatives. Five methods are identified for achieving this type of integrative solution agreement [39]:

1. Expanding the pie is employed when there is a shortage of resources not allowing both parties to satisfy their interests.

2. Nonspecific compensation is used when one party obtains its objectives and compensates the other party for accommodating its interest. The compensator will make offers determining the level of compensation needed to satisfy the other party.

3. Logrolling is applied if there is more than one conflicting issue. The parties compromise so that one party achieves its top priority on the first issue, and the other achieves its top priority on the second. This involves a party's deciding which issues are of high and low priority to it and to its opponent.

4. Cost cutting occurs when one party achieves its objectives and the other party's costs are reduced by going along with the agreement.

5. Bridging is when parties reformulate the problem, disclose information to reveal their interests, and invent options to satisfy both parties' needs.

## E. Use "Objective" Data

Negotiators need assurance of the accuracy and consistency of the data as a basis for their decisions. NSS support facilities (namely the database component and its associated DBMS) can enforce data validity by performing syntactic and semantic checks and pre-defined integrity constraints.

Negotiators are also assisted in obtaining a complete set of decision alternatives from a variety of sources through NSS features. They can access private/public and internal/external data sets, and local databases or remote data sources. Speedy access to information helps negotiators make better decisions without interrupting the negotiation process for long periods of time [24].

## 4. Review of Existing NSS Software

This section reviews the following existing NSS: CAP, DECISIONMAKER, NEGO, DECISION CONFERENCING, MEDIATOR, and RUNE. This review indicates the types of conflicts for which these NSS are useful, the negotiation theories upon which they are based, and the structural aspects as well as specific advantages and limitations of each system.

A. CAP (Conflict Analysis Program) [12] is an interactive, microcomputer-based system which provides support for a third-party arbitrator at the prenegotiation strategy formulation stage. Information from many sources is incorporated into a single model or game representing the conflict situation, in which players have options and preferences. CAP uses metagame analysis methods to formulate and analyze subjective alternative strategies and strategy preferences. Information about the model is stored in CAP and presented to the arbitrator. The latter performs Outcome Removal to eliminate unfeasible agreements (or contracts), Preference Ordering according to the players' outcome preferences, and stability analysis to determine the agreement(s) which have equilibrium or stability for all players.

B. DECISIONMAKER [13] is an enhanced version of CAP useful for modeling and analyzing situations involving strategic negotiations. This NSS (which is written in the C programming language) gives rationale for, and explanations of, stability conditions that occur, and includes the use of sensitivity analysis. DECISIONMAKER forecasts possible compromise resolutions and optimizes decision making, seeking stability for all participating parties. It is an iterative process that involves updating previous models after interpreting the stability of the obtained results. It must be noted here that this NSS does not support face-to-face negotiations. Technical assets of DECISIONMAKER include the capability of handling up to 10 participants, 30 options and 1000 outcomes. The system runs in an MS-DOS operating system environment, supports full screen display and editing and offers complete on-line documentation. Both CAP and DECISION-MAKER have been developed for IBM-compatible microcomputers and are available as software packages.

C. NEGO [28] is a two-stage, interactive process of individual proposal formulation and negotiation leading to compromise based on Kersten and Szapiro's [29] generalized theory of negotiations formulation. This iterative procedure allows decision makers to change their strategies, to form coalitions, and to compromise on the issues at stake. Goals, demands, and alternative objective functions are all analyzed by multi-objective linear programming optimization methods. All participants should remain in the same room, so that they can interact personally with each other. NEGO consists of three programs written in FORTRAN, EXEC 2 and Assembler and runs on an IBM 370/148 under VM/VSP. Linear programming problems are solved by the IBM Mathematical Programming System Extended package, using the Graphical Data Display Manager/Presentation Graphic feature. NEGO is still in the prototype stage and is being applied to management cases.

D. DECISION CONFERENCING [41] is useful for pre-negotiation planning. It provides structure for the disaggregation of complex issues, anticipates the positions of others, creates new alternatives and facilitates negotiators' communication with their constituency [47]. For use in direct negotiations, decision models should be developed separately for the two opposing parties. Then they can work together with the models to derive a mutually preferred solution.

DECISION CONFERENCING combines decision analysis theory with group processing techniques drawn from organizational development [1,41]. Software for decision conferences consists of analytic methods such as decision and influence trees, expected utility models, hierarchical evaluation structures for multiattribute utility analysis, and pareto algorithms for two-party negotiations [31]. A decision conference usually takes place in a conference room furnished with a large-screen video projector, a computer, hand-held terminals for voting or other input by participants, and a control terminal for presenting participant inputs and for accessing other information. Three facilitators assist executive teams in structuring a problem, modeling/refining it, and planning the implementation of its solution, with an emphasis on democratic meeting protocols [41].

<table><tr><td>CAP [Fraser and Hipel (1981)]Types of conflicts useful forBusiness and industry conflicts, labormanagement conflictsStructureInteractive, microcomputer-based, external arbitrator helped in analysis, screen displays from program shown at each step.Negotiation theory based onMeta-game analysisAdvantagesCommercial software package, incorporates information from a variety of sources into single game model, presented in meaningful manner, Stability information automatically calculated.Disadvantages“Impartial” arbitrator solely responsible for creation of model. He removes outcomes on subjective analysis, no input from players after initial input to model.</td><td>DECISIONMAKER[Fraser and Hipel (1986)]Types of conflicts useful forStrategic planning during prenegotiation strategy formulation.Useful also in hypergame situations to model dynamics of a conflict as it evolves over time.StructureIBM PC computers, written in C programming language. Models a conflict, orders scenarios simply, forecasts compromise solution, gives rationale for outcome stability, explains best course of action.Negotiation theory based onMeta-game analysisAdvantagesCommercial software package. Uses full screen display and editing, adaptable for hypergame problems and those requiring state transition approach.DisadvantagesTool for mediator or participant only, no interaction with other participants.</td><td>NEGO [Kersten (1985)]Types of conflicts useful forSupports compromise evaluation in various group decision making problems where there are multiobjectives.Structure2-stage, interactive process of individual proposal formulation and negotiation, Multi-objective linear programming used for optimization.Negotiation theory based onGeneralized theory of negotiationsAdvantages:Close proximity of parties encourages compromise. Multidimensional scaling graphs used to show the negotiation process.DisadvantagesNot useful for solving problems with 2 decision makers with same objective but different criteria as in pure wagebargaining. Still a prototype, no validation.</td><td>DECISION CONFER-ENCING [Quinn et al. (1985)]Types of conflicts useful forSemi- or un-structured problems, used for pre-negotiation planning, also adaptable to direct negotiations.StructureMicro-computer based. Only facilitators use the computer, participants watch analysis of results.Negotiation theory based onModeling techniques of decision analysis and group process techniques of organizational development.AdvantagesStructure for disaggregation of complex issues, anticipates opponent&#x27;s position, creates new alternatives and facilitates communication.DisadvantagesValidation very limited for use with direct negotiations. Not helpful with conflict resolution. Time-consuming, technical problems unresolved.</td><td>MEDIATOR [Jarke et al. (1987)]Types of conflicts useful forMulticriteria, multi-player, Illstructured, dynamic problems. Supports evaluation and selection of alternatives.Can support a mediator who does not decide himself on the solution, support a mediator who does decide the solution, or support players directly without use of a human mediator.StructureData-base centered, Each player has a micro-DSS connected to mainframe, so they share data. Can be used remotely.Negotiation theory based onEvolutionary Systems Design, uses MCDM data analysis techniques.AdvantagesSupports evolution of group problem representation, remote use possible, interaction among players and with mediator.DisadvantagesConceptual model, no validation.</td><td>RUNE [Kersten et al. (1986)]Types of conflicts useful forHelps evaluate negotiating positions and model negotiating strategies during prenegotiation strategy formulation.StructureLearning stage and interaction stage, analysis tools implement the system according to rule-base and meta-rule base.Negotiation theory based onRule based, AIAdvantagesEnables evaluation of consistency of the negotiation goals, models the impact of opponent&#x27;s anticipated decisions on the user&#x27;s future decisions.DisadvantagesPrototype in testing, no validation.</td></tr></table>

E. MEDIATOR [20] is a database-centered, micro-mainframe NSS used to support negotiators and human mediators in solving conflicts. It is applicable during the pre-negotiation stage where players formulate their initial bargaining position. It is also employed in the negotiation stage to help select and evaluate alternatives. MEDIATOR handles subjective (qualitative) and objective (quantitative) data and analyzes decision-maker preferences for possible solutions (agreements). Each negotiating party uses PREFCALC [18,32], a single-user multicriteria DSS, to establish their individual preferences and problem representation, which are transferred then to the common (mainframe) database. The human mediator integrates these individual problem representations using relational query language capabilities to form an initial group joint problem representation. Negotiations are undergone by consensus seeking through exchange of information and compromise. MEDIATOR, which is still in the development stage, is useful for multi-player, multicriteria, ill-structured, dynamic problems.

F. RUNE [30] is a NSS that uses an artificial intelligence approach to help evaluate the players' positions and model negotiating strategies. It views negotiation as being a two-stage process. In the learning stage, participants formulate their first proposals; while in the interaction stage, they exchange proposals and make concessions, reaching either a compromise decision or a deadlock.

RUNE is structured around rule and meta-rule bases (goal modification and response rules). RUNE support facilities include: (1) a set of tools that analyze the goal representation and check for inconsistencies; (2) a goal modifier that updates the content of the rule base; and (3) an inference engine that carries out deductions at the meta-rule level. RUNE enables the user to evaluate the consistency of negotiation goals and to model the impact of the opponent's anticipated decisions or options on the negotiator's future decisions. RUNE is written in the symbolic language PROLOG and currently exists in a prototype version.

G. Summary of NSS Review. This review of computer-assisted negotiation software displays the diversity of structure, purpose and application of these systems. The NSS examples discussed above are based on the evolutionary systems design approach (MEDIATOR), conflict analysis (CAP and DECISIONMAKER), decision analysis (DECISION CONFERENCING), artificial intelligence (RUNE), and the generalized theory of negotiations (NEGO).

DECISIONMAKER, CAP, DECISION CONFERENCING and RUNE are useful for pre-negotiation strategic planning, while MEDIATOR and NEGO are well suited for actual interactive negotiations. The latter two NSS share the advantages of both protecting the rights and privacy of negotiators and helping them to search for a mutually agreeable solution. There are also examples of NSS that support an arbitrator (DECISIONMAKER and CAP), a democratic group decision making environment (DECISION CONFERENCING), or a human mediator in his structuring of the negotiation process and playing a group facilitator role to help achieve an agreement (MEDIATOR).

## 5. Concluding Remarks

This paper has discussed issues involved in the structuring of a negotiation situation. These issues include behavioral characteristics and cognitive perspectives of the negotiators, identification of each party's real interests, the generation of options for mutual gain, and data accuracy and consistency. Also of great importance are the communication needs which vary with each bargaining situation, depending on the spatial and temporal distance among negotiators, the degree of commonality of goals, and the type of decision control. A review of some existing NSS showed that the function of providing computer support for negotiation has been interpreted and implemented in different ways.

Future research work in the field of NSS should be based on data from experiential studies and empirical testing of actual usage of these systems [26,27]. Because of the newness of the negotiation support system concept, little has been written on this subject, and there is a definite need for guidelines, standards, and criteria for building and evaluating NSS. An integrative framework that considers both technical and behavioral aspects of NSS design is needed. It has been the aim of this paper to suggest some important issues which should be included in such a framework for further developing NSS.

## References

[1] Adelman, L. "Real-time Computer Support for Decision Analysis in a Group Setting: Another Class of Decision Support Systems", Interfaces, 14 (2), 1984, 75–83.

[2] Anson, R., Jelassi, M.T., "A Development Framework for Computer-Supported Conflict Resolution". Forthcoming in the European Journal of Operational Research, special issue on Group Decision and Negotiation Support Systems, 1989.

[3] Applegate, L.M., Konsynski, B.R., and Nunamaker, J.F. "A Group Decision Support System for Idea Generation and Issue Analysis in Organizational Planning," Working Paper Series #PL-17, University of Arizona, Tucson, AR., July 1986.

[4] Barclay, S. and Peterson, C. "Multi-Attribute Utility Models for Negotiations". Technical Report 76-1. McLean, VA: Decisions and Design, Inc., March 1976.

[5] Bazerman, M.H. Judgement in Managerial Decision Making, New York, N.Y.: John Wiley and Sons, 1986.

[6] Bui, T.X. and Jarke, M.. “Communications Design for Co-oP: A Group Decision Support System”, ACM Transactions on Office Information Systems, 4 (2), April 1986, 81–103.

[7] Crawford, V.P. "Dynamic Games and Dynamic Contract Theory." Journal of Conflict Resolution, 29 (2), 1985, 195-224.

[8] Delbecq, A.L., Van de Ven, A.H. and Gustafson, D.H. Group Techniques for Programming Planning, Glenview, IL.: Scott-Foresman and Co., 1975.

[9] DeSanctis, G. and Gallupe, B. "Group Decision Support Systems: A New Frontier". Data Base, 16 (1), Winter 1985, 3–10.

[10] Eliashberg, J., LaTour, S.A., Rangaswamy, A. and Stern, L.W. "Assessing the Predictive Accuracy of Two Utility-Based Theories in a Marketing Channel Negotiation Context". Journal of Marketing Research, 23, May 1986, 101–110.

[11] Fisher, R. and Ury, W. Getting to Yes: Negotiating Agreement Without Giving In, Boston, MA.: Houghton Mifflin Co., 1981.

[12] Fraser, N.M. and Hipel, K.W. "Computer Assistance in Labor-Management Negotiations." Interfaces, 11 (2), April 1981, 22–29.

[13] Fraser, N.M. and Hipel, K.W. "Conflict Analysis for Group Decision and Negotiation Support Systems", TIMS/ORSA Joint National Meeting, Miami, FL., October 27–29, 1986.

[14] Geshka, H. "Introduction and Use of Idea-Generating Methods". Research Management, 21 (3), 1978.

[15] Gouran, D.S. Making Decisions in Groups: Choices and Consequences, Glenview, IL.: Scott-Foresman, 1982.

[16] Hwang and Lin. Group Decision Making Under Multiple Criteria, Berlin: Springer-Verlag, 1987.

[17] Jacquet-Lagreze, E. and Shakun, M.F. "Decision Support Systems for Semi-Structured Buying Decisions." European Journal of Operational Research, 16, 1984, 48–58.

[18] Jacquet-Lagreze, E. and Siskos, E. "Assessing a Set of Additive Utility Functions for Multiple Criteria Decision Making". European Journal of Operational Research, 10, 1982, 151–164.

[19] Jarke, M. "Knowledge Sharing and Negotiation Support in Multiperson DSS." Decision Support Systems: The International Journal, 2, 1986, 93–102.

[20] Jarke, M., Jelassi M.T. and Shakun, M.F. "MEDIATOR: Towards a Negotiation Support System", European Journal of Operational Research. 31 (3), September 1987, 314–334.

[21] Jarke, M. and Jelassi, M.T. "View Integration in Negotiation Support Systems", Transactions of the Sixth International Conference on Decision Support Systems, Washington, D.C., April 21–24, 1986, 180–188.

[22] Jelassi, M.T. "An Extended Relational Database for Generalized Multiple Criteria Support Systems." Ph.D. Dissertation, Department of Computer Applications and Information Systems, New York University, 1985.

[23] Jelassi, M.T. "MCDM: From 'Stand-Alone' Methods to Integrated and Intelligent DSS", in Y. Sawaragi, K. Inoue and H. Nakayama, eds., Toward Interactive and Intelligent Decision Support Systems, Berlin: Springer-Verlag, 1987, 80–88.

[24] Jelassi, M.T. and Beauclair, R.A. "An Integrated Framework for Group Decision Support Systems Design", Information and Management. 13 (3), 1987, 143–153.

[25] Jelassi, M.T. and Jones, B.H. "Getting to YES with NSS: How Computers Can Support Negotiations" in R.M. Lee, A.M. McCosh and P. Migliarese (eds.): Organizational Decision Support Systems, Amsterdam: North-Holland, 1988a.

[26] Jelassi, M.T. and Jones, B.H. “Computer-Supported Negotiations: Some Empirical Observations.” Invited Paper to the Joint International Meeting of EURO IX/TIMS XXVIII, Paris, July 6–8, 1988b.

[27] Jones, B.H. and Jelassi, M.T. "Negotiation Support: The Effects of Computer Intervention and Conflict Level on Bargaining Outcome". INSEAD Working Paper Series, N° 89/03, January 1989.

[28] Kersten, G.E. "NEGO - Group Decision Support System". Information and Management, 8, 1985, 237-246.

[29] Kersten, G.D. and Szapiro, T. "Generalized Approach to Modeling Negotiations". European Journal of Operational Research, 26, 1986, 124–142.

[30] Kersten, G.E., Matwin, S., Michalowski, W. and Szpakowicz. "Rule-Based Modelling of Negotiations Strategies", working paper, Karleton University, Ottawa, Ontario, 1986.

[31] Kraemer, K.L. and King, J.L. "Computer-Based systems for Group Decision Support: Status of Use and Problems in Development", Proceedings of the First Conference on

Computer-Supported Cooperative Work, Dec., 3–6, 1986, Austin, Texas.

[32] Lauer, T.W. and Jelassi, M.T. "PREFCALC - A Multi-Criteria Decision Support System: User Tutorial", Institute for Research on the Management of Information Systems, Indiana University, Working Paper #W714. November 1987.

[33] Lewicki, R.J. and Litterer, J.A. Negotiations, Homewood, Il.: Richard D. Irwin, Inc., 1985.

[34] MacCrimmon, K.R. "An Overview of Multiple Objective Decision Making" in J. Cochrane and M. Zelleny (eds.), Multiple Criteria Decision Making, Columbia, S.C.: University of South Carolina Press, 1973.

[35] Maslow, A.H. Motivation and Personality, New York, N.Y.: Harper and Row, 1954.

[36] McMaster, M. and Grinder, J. PRECISION: A New Approach to Communication, Beverly Hills, CA.: Precision Models, 1980.

[37] Nierenberg, G. Fundamentals of Negotiating, New York, N.Y.: Hawthorn Books, 1973.

[38] Osborne, A. Applied Imagination, New York, N.Y.: Charles Scribner and Sons 1953.

[39] Pruitt, D.G. and Lewis, S.A. "Development of Integrative Solutions in Bilateral Negotiations". Journal of Personality and Social Psychology, 31, 1975, 621–633.

[40] Pruitt, D.G. “Achieving Integrative Agreements” in M.H. Bazerman and R.H. Lewicki, eds., Negotiating in Organizations, Beverly Hills, CA: Sage Publications, 1983.

[41] Quinn, R.E., Rohrbough, J. and McGrath. M. "Automated Decision Conferencing: How It Works". Personnel, November, 1985, 49–55.

[42] Raiffa, H. The Art and Science of Negotiation, Cambridge, MA.: Harvard University Press, 1982.

[43] Rubin, J.Z. and Brown, B.R. The Social Psychology of Bargaining and Negotiation, New York, N.Y.: Academic Press, 1975.

[44] Shakun, M.F., Evolutionary Systems Design: Policy Making Under Complexity and Group Decision Support Systems, San Francisco, CA.: Holden Day, 1987.

[45] Sperber, P. Fail-Safe Business Negotiating, Englewood Cliffs, N.J.: Prentice-Hall, 1983.

[46] Swap, W.S. “Destructive Effects of Groups on Individuals” in W.S. Swap et al., (eds.), Group Decision Making, Beverly Hills, CA.: Sage Publications, 1984.

[47] Ulvila, J.W. and Snider, W. "Negotiations of International Oil Tanker Standards: An Application of Multi-Attribute Value Theory", Operations Research, 28 (1), 1980, 81–96.

[48] Von Neuman, J. and Morgenstern, O. Theory of Games and Economic Behavior, Princeton, N.J.: Princeton University Press, 3rd Ed., 1964.

[49] Zartman, W. and Berman, M.R. The Practical Negotiator, New Haven, CT.: Yale University Press, 1982.

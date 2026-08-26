---
otero_id: 16924
otero_key: "N6JC2FHZ"
title: "Knowledge sharing and negotiation support in multiperson decision support systems"
authors: "Matthias Jarke"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90125-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge Sharing and Negotiation Support in Multiperson Decision Support Systems

Matthias JARKE

Graduate School of Business Administration, New York University, 90 Trinity Place, New York, N.Y. 10006, USA \*

A number of DSS for supporting decisions by more than one person have been proposed. These can be categorized by spatial distance (local vs. remote), temporal distance (meeting vs. mailing), commonality of goals (cooperation vs. bargaining), and control (democratic vs. hierarchical). Existing frameworks for model management in single-user DSS seem insufficient for such systems. This paper views multiperson DSS as a loosely coupled system of model and data bases which may be human (the DSS builders and users) or computerized. The system's components have different knowledge bases and may have different interests. Their interaction is characterized by knowledge sharing for uncertainty reduction and cooperative problem-solving, and negotiation for view integration, consensus-seeking, and compromise. Requirements for the different types of multiperson DSS can be formalized as application-level communications protocols. Based on a literature review and recent experience with a number of multiperson DSS prototypes, artificial intelligence-based message-passing protocols are compared with database-centered approaches and model-based techniques, such as multicriteria decision making.

Keywords: Group Decision Support Systems; Negotiation; DSS Design; Knowledge Base Management; Advanced Database Systems

## 1. Introduction

Model building and application are universal features of human and computerized problem solving. A DSS needs models of the problems to be solved, of the data to be used in the problem-solving process, and of the users who are trying to solve the problems. The DSS architecture proposed by Sprague and Carlson [53] captures these three tasks by sub-dividing a DSS into the three components of model manager, data manager, and dialog manager. Traditionally, the DSS has been perceived as a homogeneous single-user system which interacts – at different times – with two kinds of users: the DSS builder (typically a systems analyst with substantial expertise in computers), and the decision maker (typically with very limited computer skills). Current Model Management Systems (MMS) preserve a fairly strict distinction between these user types and provide few facilities for user or systems learning during problem-solving \*.

More importantly, these systems fail to recog-

\* A notable exception are the popular spreadsheet systems which, however, do not offer very sophisticated modelling capabilities.

![](/api/attachments/N6JC2FHZ/fulltext/images/da3f8a840c6f14913041f4e26ced252c09abf914f56cd5d28eb70a6762551e02.jpg)

Matthias Jarke is an Associate Professor of Computer Applications and Information Systems at the Graduate School of Business Administration at New York University. He received diplomas in Computer Science and Business Administration, and a Ph.D. in Economical Sciences from the University of Hamburg, West Germany. In his research, Dr. Jarke investigates the optimal interaction of database management systems with advanced application systems, such as decision support systems and expert systems. Currently, his main interest is in the area of computer support for multiperson problem-solving. His publications include four books and a number of articles on DBMS design and implementation, database user interfaces, decision support systems, expert systems databases, and cost-benefit studies of information systems.

nize that organizational decision-making is rarely a one-person activity [39,6,17,54,15]. On the one hand, multiple decision makers may participate in a decision, in a cooperative group setting or via bargaining-type negotiations among multiple parties. These users may feel a need to communicate and negotiate not only in person but also through their DSS. On the other hand, each decision maker may want to consult multiple models, knowledge bases, and databases. Frequently, these knowledge sources rely on inconsistent assumptions and different perceptions of the problem. Traditional DSS provide little support in such situations.

The apparent need for integrating the ever-increasing number of micro-based DSS [3,43] suggests a radically different approach to model management which takes into account the existence of multiple interacting DSS as well as multiple interacting users. This approach – based on Hewitt's [24,25] concept of Open Systems – perceives a distributed DSS as a collection of loosely coupled problem solvers (human or computerized) which communicate in two different modes: a knowledge acquisition or learning mode, and a problem-solving mode. Fig. 1 presents the main types of interactions for both modes, between systems, between users, and between system and user.

This paper is an attempt to address some of the general model management questions in such a multiperson DSS context. The composition of non-homogeneous mental and computerized models cannot be based on model inputs and outputs alone, as has been suggested in single-user modelling contexts [5,52]. Rather, model composition requires a careful analysis of the assumptions underlying each model. Moreover, human as well as computerized components of the distributed DSS may not always be accessible. Enlisting their communication and cooperation may require an elaborate negotiation process.

![](/api/attachments/N6JC2FHZ/fulltext/images/75f4c39bea6b116fb3ed62373a150b0c05df26a601b65dcdb4c09aa5d5330f3d.jpg)  
(A) KNOWLEDGE ACQUISITION MODE

![](/api/attachments/N6JC2FHZ/fulltext/images/7f9ae5e79d40e6118d6fcc483637d2446afc8c2bc7cdca253bb0afa9d0bfb21c.jpg)  
(B) PROBLEM-SOLVING MODE  
Fig. 1. Multiperson Model Management System (MMS) Usage Modes

In summary, it appears that the design of the communications subcomponent of the distributed MMS is crucial for the success of a multiperson DSS. In the sequel, we shall first examine the communication requirements of such systems in more detail based on a taxonomy of multiperson DSS. Next, we study how three of the major DSS parent areas, databases, artificial intelligence, and operations research have attempted to deal with multiperson systems. Finally, we summarize our conclusions concerning a general communications framework for multiperson DSS.

## 2. A Taxonomy of Multiperson DSS

The communications needs and opportunities of a multiperson DSS are largely dependent on the setting in which the multiperson decision takes place. In this section, we propose four dimensions that may assist in classifying multiperson DSS requirements: spatial distance among the decision makers, temporal distance among the decision-making activities by individual group members, commonality of goals among the decision makers, and type of control over the multiperson decision process. Although there is a continuum of possibilities along each dimension, they will be dichotomized here for simplicity.

Spatial distance. This dimension determines whether full face-to-face communication among decision makers is possible in addition to using the DSS. While this important feature is present in local DSS situations [26], a remote multiperson decision setting must compensate for its lack by providing electronic communications facilities for all aspects of the multiperson decision-making process.

Temporal distance. This dimension determines whether decisions are made by meetings at a particular point in time, or whether decision makers submit their input at different points in time. Examples of the former setting include conventional meetings as well as teleconferencing, whereas the latter may be based on concepts of electronic mail, bulletin boards, and computerized conferencing [58].

Commonality of goals. This dimension distinguishes a situation in which a group wants to solve a common problem cooperatively, from one in which (potentially hostile) parties are bargaining. Research in multiperson DSS has mostly addressed the first problem [13]. Here, the main issues are knowledge sharing among multiple experts, preference aggregation, and negotiation in a friendly setting. Only recently, DSS researchers have tried to exploit the theoretical results obtained by behavioral theory and operations research for bargaining situations.

Control. This dimension distinguishes between situations in which the decision makers reach a decision in a democratic process, and a setting in which there is a human group leader or mediator. In a democratic setting, communication and coordination are achieved directly by the users (through the DSS in remote multiperson DSS). As a consequence of this increased system power, DSS design has to go great lengths towards system fairness – otherwise the system may not be used by those who feel discriminated against. The same is also true if the multiperson DSS supports a human mediator who cannot impose decisions on the parties. On the other hand, if there is a more powerful group leader or compulsory arbitration, the multiperson DSS in final consequence is mostly a DSS for this person, and should be designed accordingly.

The four dimensions are summarized in Fig. 2. With two values for each dimension, there are sixteen types of multiperson decision settings. Each of these can then be mapped on a communications design which is either based on point-to-point communications, or relies on broadcasting of messages. Thus, there are at least 32 types of multiperson DSS; only a few of these have been realized in actual systems. For example, Huber's [26] decision room example explores a cooperative, local, meeting-oriented broadcasting concept with a group facilitator as a (weak) leader. His Delphi example, on the other hand, is distributed both in time and space, and mostly point-to-point. The system CooP described in [8] supports temporally and spatially distributed cooperative decision-making with democratic control and mostly broadcasting messages. A spatially remote cooperative meeting setting on a point-to-point basis is implemented in many computer centers to allow consultants to track errors with remote users on-line. Jarke [30] describes a hierarchically distributed DSS for container management in a spatially and temporally distributed setting with strict hierarchical control and point-to-point communication; here, the multiperson DSS degenerates to an implementation of problem decomposition.

<table><tr><td>SPATIAL DISTANCE</td><td>TEMPORAL DISTANCE</td></tr><tr><td>LOCAL</td><td>MEETING</td></tr><tr><td>REMOTE</td><td>MAILING</td></tr><tr><td></td><td></td></tr><tr><td>COMMONALITY OF GOALS</td><td>CONTROL</td></tr><tr><td>COOPERATION/GROUP</td><td>DEMOCRATIC/SYSTEM</td></tr><tr><td>BARGAINING/NEGOTIATIONS</td><td>COORDINATION</td></tr><tr><td></td><td>HIERARCHICAL/HUMAN</td></tr><tr><td></td><td>COORDINATION</td></tr></table>

Fig. 2. Taxonomy of Multiperson DSS Decision Settings

Space restrictions prevent further elaboration on the different types of multiperson DSS. However, it should have become obvious that there is a rich field for further research. The remainder of this paper investigates application-level communications technologies that can be borrowed from DSS parent disciplines to support multiperson decision-making. We omit a discussion of message-passing at the lower levels of the communications protocol hierarchy [55].

## 3. Data Sharing in DBMS

The idea of data sharing was central to the initial development of mainframe database management systems (DBMS). Shared databases reduce data entry costs and provide centralized management of data integrity. Unfortunately, there are two disadvantages of current DBMS concepts for multiperson DSS.

The first disadvantage stems from the current concept of a database transaction [21] which is geared more towards concurrency control than towards information exchange. The underlying assumption is that each database transaction is an atomic operation on the database with no information about other transactions. Consequently, DBMS use a concept of serializability which states that the effect of the concurrent execution of a set of transactions must be equal to that of any serial execution [4]. This can be a severe disadvantage if the purpose of a user transaction is communication with another user, i.e., the read transaction of the receiver should follow the write transaction of the sender. Further, since transactions are supposedly independent, no mechanisms are provided for them to communicate with each other directly.

Secondly, most current DSS reside on microcomputers. While the need for data management in such DSS has been recognized early on; attempts to integrate microcomputer DSS databases with each other and with centralized mainframe databases are a more recent phenomenon. The commercial solutions are ad-hoc rather than based on any specific theory.

In [33,36,37] we have defined an approach to this problem that integrates data staging, microcomputer database management, multiple criteria model base management, and menu-driven dialogues from a database perspective, and drives their invocation from an abstraction mechanism in the data dictionary. While this model provides a conceptually clean (and largely implemented) solution to accessing shared mainframe databases, it does not address the problem of sharing aggregated problem representations and results.

Moreover, although the data staging mechanism is defined in a way that allows for updates to the extracted database views, the issue of concurrency control for these views is unresolved since DSS transactions may take a long time. It would be unreasonable to expect that the database remains unchanged in between. In [42], a concept is presented that enforces traditional concurrency control for data sharing between working groups but allows explicit communication within a working group. Ries [49] emphasizes the role of integrity constraints in micro-mainframe DBMS because they may prevent unacceptable updates where traditional concurrency control methods fail. Additionally, however, there will also be a need for compensating subtransactions that selectively undo inconsistent changes without rolling back all the work done; this can be achieved through a concept of nested transactions [21].

In summary, existing DSS databases provide little support for true data sharing and information exchange, as required by most multiperson DSS. Among the more recent concepts that may improve this situation are:

(1) federated database architectures [22] that allow limited and controlled exchange of information among workstation databases;

(2) nested transactions that allow selective compensating subtransactions if previous decisions and changes to the database prove inconsistent. Note, that in the distributed DSS context, inconsistency cannot be detected or prevented in advance at acceptable costs;

(3) cooperating transactions that allow point-to-point communication for local coordination among database transactions. We believe that in the distributed DSS context a message sent between user transactions is preferable to attempts to formally analyze the intent of transactions.

(4) data-driven model management that allows the invocation and composition of models based on information stored in the data dictionary, thus attempting to avoid discrepancies among data and model management.

## 4. Knowledge Sharing in KBMS

Both the database and the DSS areas have recognized the need for adding artificial intelligence (AI) capabilities to their systems [35]. Conversely, AI researchers have recognized that their systems require better interfaces to conventional very large databases and mathematical models if they are to succeed in the business world. One emerging concept is the idea of integrated knowledge base management systems (KBMS) [47]. Such a KBMS would include mechanisms for: managing complex data objects; performing inferences using symbolic integrity and deduction rules; accessing large-scale databases for conventional and unformatted (e.g., image) data; and using model libraries containing different kinds of models, such as mathematical, behavioral, or physical. In other words, KBMS are intended to integrate concepts of AI, DBMS, and DSS under a single conceptual umbrella.

The full implementation of such systems is probably a decade away. However, some important aspects that distinguish KBMS from existing knowledge-based systems (expert systems) are being investigated now. Two of these aspects appear important in multiperson DSS design: the distribution of expertise, and the volatile nature of business knowledge.

Similar to multiperson DSS, large-scale KBMS inherit from database systems the property of being developed and used by multiple users, both in a read and in a write mode (Fig. 1). There are two purposes to this simultaneous use: knowledge sharing and negotiation. This has some frequently overlooked consequences for the design of knowledge-based systems and model-based DSS.

The concepts of stable knowledge and model correctness as an idea of truth which underly most existing DSS and expert systems are no longer acceptable. Knowledge bases and correct models do not represent truth but the beliefs of the designers or experts, which in turn are based on their subjective assumptions and goals \*. In a multiperson context, inconsistencies are not just a consequence of design errors which lead to annoying logical contradictions but serve as a fruitful starting point for discussion and compromise.

Carl Hewitt [2,25] was among the first who pointed out the impossibility of a consistent logical theory for multi-actor problem-solving in truly distributed, decentralized decision settings. His open systems approach explores theoretical foundations for systems that initially would not even know where to ask for necessary knowledge but identify new knowledge sources as the need arises. For example, a DSS following this architecture would be alerted to the existence of a particular external model or data base only during decision-making, and then try to establish a mutually understood language and knowledge exchange mechanism with that external source. A few DSS provide such data staging support (cf. Section 3) but require substantial human intervention, e.g., in reformatting the incoming data from previously unknown sources.

Open systems grow, and their components interact, by negotiation with other systems. Davis and Smith [11] propose so-called contract nets that use negotiations for distributed problem solving. Whenever a local problem solver cannot solve a subproblem, it broadcasts a request for proposal, describing the task at hand. Other qualified subsystems will then submit proposals, based on their current status (e.g., workload) and general capabilities. The original problem solver will then negotiate a contract with one of the bidders; among other things, the negotiations will have to make sure that the bidder is really qualified for handling the task.

As an example of extending the contract negotiation approach to DSS, consider the following model management scenario. A microcomputer-based DSS requests the solution of a fairly large linear program. Four other DSS model bases bid on this: a mixed-integer programming package, two linear programming systems, and a network optimizer, each of them providing a cost estimate based on the problem size. The mixed-integer system is excluded because of very high costs. First, negotiations are started with the network package; however, detailed problem analysis during negotiations shows that the problem does not have a network structure. Note, that this involves discussing the assumptions underlying the models, rather than just a simple input/output analysis. Therefore, the negotiations are abandoned. But now the machine where the fastest of the LP packages resides is very busy and submits an increased cost estimate when approached for negotiations. Therefore, the bid by the other LP package is selected and conventions for result delivery are established.

A second shortcoming of existing knowledge-based systems is that their knowledge bases are domain-specific and very stable. Initial knowledge bases can be established a-priori and evolve slowly as the system acquires new knowledge. In business situations as mirrored in DSS, knowledge is often not stable at all; there are examples (e.g., stock selection) where knowledge is only useful if applied immediately, i.e., before becoming known to everybody. Moreover, multiperson DSS will be applied to varying problem contexts where little a-priori knowledge is available. The multiperson DSS model manager should therefore include a machine learning component which rapidly \* Henderson [23] points out the relevance of this observation to the use of DSS by senior executives. Here, we are focusing on its importance for implementing distributed model management.

acquires knowledge, using just a few examples and existing rules [44,60].

Again, the distributed model manager must trace the source of the learned concepts, i.e., the decision maker or models on whose judgments the definition of the concept depends. How does the system get these assumptions? Belief maintenance systems in AI [16] ask the user to justify his decisions, and employ the justifications (rather than an ‘objective’ logical theory) to establish dependencies that trace the consequences of changes in assumptions. In [14], a method is proposed not only to record these justifications during a prototyping process but also to surface more general assumptions underlying them, and to apply those assumptions in analogy-based reasoning [59].

To summarize this section, AI has developed some promising concepts that could serve as a basis for model management in distributed multi-person DSS. However, neither the negotiation nor the assumption surfacing and learning concepts presented here have been fully developed or implemented. In particular, existing concepts do not take into account the support nature of DSS, i.e., the need to interact with multiple users as well as with multiple subsystems.

## 5. MCDM methods as Protocols for Communication and Negotiation

Among the operational research methods, game theory [48] and multiple criteria decision making (MCDM) methods were among the first to consider a multiuser context. Despite the impossibility of defining axiomatically a fair group solution without resorting to dictatorship [1], MCDM methods have a number of advantages for the multiperson DSS context [8]. By their very nature, they integrate multiple views of a problem, using qualitative as well as quantitative criteria. Many of the methods are interactive, allowing for easy revisions of individual or group problem representations and opinions. MCDM methods can be used in a message-passing (point-to-point) as well as in a database-centered (broadcasting) implementation, and they support democratic as well as hierarchical multiperson decision modes. By adding database capabilities to multicriteria-based DSS, both knowledge sharing and negotiation can be supported. Our own implementation efforts have therefore focused on this area first.

A number of multiperson methods have been proposed in the MCDM literature $[2,10,40]$ . Some of these methods – especially if applied in reality – were also combined with other models. Tell $[56]$ employs a Delphi-like method for capturing the preferences of individuals, and factor analysis for limiting the number of criteria. Kirkwood $[41]$ integrates MCDM methods with an analysis of uncertainty about decision outcomes to support multiperson analysis of public sector situations; see $[20]$ for an overview of similar ideas. The present author applied MCDM-based DSS in several multiplayer decision situations using single-user DSS, in order to assess the cost-effectiveness of large-scale public-sector information systems in banking $[34]$ and infection control $[45]$ . However, all of these methods – if computerized at all – were implemented in a single-user, albeit multiplayer, mode.

In the recent past, we have been involved in a number of projects that attempt to design and build multi-user DSS for multiple criteria multiperson decision making. Co-oP [8,7] is a DSS for cooperative group decision making implemented on a network of personal computers. There is one PC for each player and a file server used as a message-switching center (Fig. 3).

Since the decision setting is assumed to be democratic, remote, and cooperative, the Co-oP design offers a wide range of communications facilities with fairly loose communications protocols, ranging from informal electronic mail, to structured group communication tools (NGT, Delphi), to extended MCDM tools for preference aggregation and information exchange. The initial prototype of the system [8] only supported a group version of one particular MCDM method. The full system [7] includes a larger set of models together with a rule-based system for model selection. Some behavioral, process-based tools are also being added.

![](/api/attachments/N6JC2FHZ/fulltext/images/66d68d47c1f5b08fdea01adaf60a587e1b28a496aba55324913691b5593f72fa.jpg)  
Fig. 3. Co-oP Design Combining Individual and Group DSS

If the multiperson decision situation becomes less friendly, there is a need for access control to private data and problem representations, as well as for strong tools for negotiation support. In many cases, the DSS model base will not be able to fully handle negotiation situations. Instead, the collection of human and computerized problem solvers will include a human mediator and a supporting DSS component. The mediator will help the parties (often called players) establish a joint problem representation, and then evolve it – through consensus-seeking and compromise – towards a representation in which there is a mutually acceptable solution.

This concept is being implemented in MEDIATOR, a multicriteria-based micro-mainframe DSS for negotiation support [32]. The system is intended to support negotiation between the marketing and engineering departments of a European car manufacturer [19]. MEDIATOR uses a database-centered approach; that is, communication is achieved through the manipulation of database structures, similar to the blackboard concept in AI [18].

Negotiations proceed in three stages. First, each player establishes an individual representation of the problem at hand, using publicly accessible as well as private databases and DSS tools, to feed an interactive MCDM method [29] that establishes the individual's preference structure. This step is similar in spirit to the idea of the Nominal Group Technique [12] which also requires each player to come up with individual ideas first, before the discussion starts.

In the second phase, called view integration, the human mediator is supported in achieving a joint problem representation in the three steps of: database selection, alternative definition, and criteria definition. Players transfer their individual definitions of data sources, alternatives, criteria, decision matrices, and utility functions to the common database. Each player occupies a private section of that database which can be only accessed by himself and by the mediator (Fig. 4). The mediator will then start the process of integrating these personal problem representations into the group joint problem representation. Relational operations, enhanced by redefinitions of terms, have been shown to support the view integration step effectively [32].

![](/api/attachments/N6JC2FHZ/fulltext/images/629f4c35cd56e6b7de83df06ec3aaed0c4d8fb33d1cc12524ba5b576ddd72e0f.jpg)  
Fig. 4. Mediator Design Communication through Data Sharing

Once this is accomplished, the joint problem representation – in the case of MEDIATOR an enhanced decision matrix – is stored in the publicly accessible area of the common database. From then on, the official negotiations will only work with the joint representation. However, the individual players are free to continue working with their own representation and other decision support tools for personal deliberations.

Upon successful completion of the view integration phase, the third phase, called negotiation, proceeds by consensus seeking through exchange of information and, where consensus is incomplete, by compromise. The negotiation problem is shown – graphically or as relational data in matrix form – in three spaces as a mapping from control space to goal space (and through marginal utility functions) to utility space [51]. Within each of these spaces the negotiation process is characterized by adaptive change that redefines feasible and target sets in seeking a solution.

MEDIATOR allows the human mediator to perform what-if analyses of possible suggestions for problem redefinition. Before, e.g., suggesting that players should lower their utility threshold, the mediator must make certain that this will make additional alternatives available for discussion. Otherwise, the players will feel that they made a concession for nothing and the climate of the negotiation may deteriorate.

In the control space, the relational query language offers the option of including or excluding sets of alternatives from consideration, by restricting the feasibility of certain attribute or criterion values. The human mediator can apply such queries to focus the discussion temporarily on a smaller number of alternatives, or to increase the set of feasible solutions by searching the common database for alternatives the players did not think of originally.

Changes in the goal space involve a redefinition of the criteria set: would dropping a criterion change the ranking? Is the ranking by a particular criterion inconsistent with the overall utility ranking of alternatives? To answer such questions, axiomatic methods and display techniques for relational data are employed, most prominently alternative ranking.

The idea of ranking alternatives is also used to answer what-if questions in the utility space. Since player utilities are simply additional attributes of the decision matrix, they can be used as sorting criteria. For more than two players, it may also make sense to display the aggregated utilities of coalitions. Another representation at the utility level is overlayed marginal utility curves. What-if questions allow the mediator to vary the weight and form of each player's utility curve tentatively, to prevent having the players agree to useless concessions.

In summary, MCDM methods can serve useful purposes as formal tools for preference surfacing, preference aggregation, negotiation, and mediation, both in friendly and in noncooperative decision situations. The close relationship between MCDM decision matrices and relational data representations [28] facilitates a database-centered implementation of such concepts. However, as illustrated by a comparison between the Co-oP and MEDIATOR designs, the decision setting will have a strong influence on the question how exactly to define MCDM-based communication among multiple DSS and multiple users. In [9], we propose an extension to the ISO Open Systems Interface hierarchy that includes components for establishing and enforcing such specialized communications protocols.

## 6. Summary and Conclusion

Multiperson DSS can be viewed as a community of human and computerized problem solvers with different knowledge levels and interests. Model management in such systems requires a strong communications component within the system as well as with the users. Communications design must support two systems capabilities. Knowledge sharing reduces uncertainty and integrates distributed mental and computerized models into coherent solution strategies. Since user coalitions and DSS subsystems may have different interests, problem perceptions, and goals, the communications protocol must also provide negotiation support for problem view integration, consensus-seeking, and compromise. Negotiation support should be offered both from the viewpoint of the individual problem solver and from the viewpoint of the group as a whole (as represented by a common theory or goal, or by a group leader or mediator).

Knowledge sharing and negotiation both require the capability to surface and question assumptions made by model builders. Assumption management in multiperson DSS will facilitate the task of building executive support systems that, according to Henderson [23], are charged with precisely this: the surfacing and questioning of assumptions. Assumption management also helps obviate the traditional notion of model correctness and emphasizes the subjective and volatile nature of modelling: the meaning of a model is not defined globally but determined by what its designer meant!

We have not addressed organizational implementation strategies for multiperson DSS; Keen [38] points out the crucial importance of an efficient communications infrastructure on which multiperson DSS can be piggybacked. We did, however, show that all of the parent areas of DSS research must (and can) contribute to the design of multiperson DSS. DBMS data sharing, AI concepts for knowledge representation, belief maintenance, and negotiation, and OR methods for multicriteria decisions all have to be integrated to support multiperson decisions effectively. Moreover, process-oriented behavioral tools must also be provided in the user interface manager (interpreted here as the subsystem for user-system communication). As Huber and McDaniel [27] point out, such DSS may then in turn influence the design of the organizations that use them. In particular, they may reduce the purported negative influence of single-user DSS on managerial communications [50].

## References

[1] K.J. Arrow, Social Choice and Individual Values, 2nd edn., Wiley, New York (1963).

[2] B. Bereanu, Large group decision making with multiple criteria, in H. Thiriez, S. Zionts (eds.), Multiple Criteria Decision Making, Springer-Verlag, (1976) pp. 87–101.

[3] D. Bernard, Management issues in cooperative computing, ACM Computing Surveys 11, 1 (1979) pp. 3–17.

[4] P.A. Bernstein and N. Goodman, Concurrency control in distributed database systems, ACM Computing Surveys 13 (1981) 2, pp. 185–221.

[5] R.W. Blanning, TQL: a model query language based on the domain relational calculus, Proceedings IEEE Workshop on Languages for Automation, Chicago, (1983) pp. 141–146.

[6] R.H. Bonczek, C.W. Holsapple, A.B. Whinston, Computer-based support for organizational decision making, Decision Sciences 10, (1979) pp. 268–291.

[7] X.T. Bui, Co-oP - A Multicriteria DSS for Cooperative Group Decision Making, Ph.D. Dissertation, Department of Computer Applications and Information Systems, New York University (1985).

[8] X.T. Bui and M. Jarke, A DSS for cooperative multiple criteria group decision making, Proceedings 5th International Conference on Information Systems, Tucson, Az, (1984) pp. 101–113.

[9] X.T. Bui and M. Jarke, Communications requirements for group decision support systems, Proceedings 19th Hawaii International Conference on Systems Sciences, Honolulu (1986) pp. 524–533.

[10] N.C. Dalkey, Group decision analysis, in M. Zeleny (ed.), Multiple Criteria Decision Making Kyoto 1975, Springer-Verlag, (1976) pp. 45–74.

[11] R. Davis and R.G. Smith, Negotiation as a metaphor for distributed problem solving, Artificial Intelligence 20, (1983) pp. 63–109.

[12] A.L. Delbecq, A.H. Van de Ven, and D.H. Gustafson, (1975). Group Techniques for Program Planning: A Guide to Nominal Group and Delphi Processes, Glenview, Il.: Scott, Fossman, and Company (1975).

[13] G. DeSanctis and B. Gallupe, Information Systems support for group decision making, MISRC Working Paper Series MISRC-WP-85-10, University of Minnesota (1985).

[14] V. Dhar and M. Jarke, Learning from prototypes, Proceedings 6th International Conference on Information Systems, Indianapolis (1985) pp. 114–133.

[15] D.R. Dolk, Model management in organizations, presented at ORSA/TIMS Conference, San Francisco (1984).

[16] J. Doyle, A Truth Maintenance System, AI Laboratory Memo 521, Massachusetts Institute of Technology, Cambridge, Mass (1978).

[17] J.J. Elam, J.C. Henderson, and L.W. Miller, Model management systems: an approach to decision support in complex organizations, Proceedings First International Conference on Information Systems (1980).

[18] L.D. Erman and V.R. Lesser, A multi-level organization for problem solving using many diverse, cooperating sources of knowledge, Proceedings Fourth International Joint Conference on Artificial Intelligence, (1975) pp. 483–490.

[19] J.L. Giordano, E. Jacquet-Lagreze and M.F. Shakun, Un SIAD pour la conception de produits nouveaux: aspects multicriteres et multi-acteurs, Note de Recherche, Universite de Paris-Dauphine, Paris (1985).

[20] A.S. Goncalves, Group decision methodology and group decision support systems, DSS-85 Transactions, San Francisco, Ca., (1985) pp. 135–142.

[21] J. Gray, The transaction concept – virtues and limitations, Proceedings 7th Very Large Data Base Conference, Cannes, (1981) pp. 144–154.

[22] D. Heimbigner and D. McLead, A federated architecture for information management, ACM Transactions on Office Information Systems 3, 3 (1985).

[23] J.C. Henderson, A methodology for identifying strategic opportunities for DSS, in Ref. 31 (1986).

[24] C. Hewitt, Viewing control structures as patterns of passing messages, Artificial Intelligence 8, (1976) pp. 323–364.

[25] C. Hewitt, Implications of open systems, in Ref. 31 (1986).

[26] G.P. Huber, Group decision support systems as aids in the use of structured group management techniques, DSS-82 Transactions, San Francisco, (1982) pp. 96–108.

[27] G.P. Huber and R.R. McDaniel, Exploiting information technologies to design more effective organizations in Ref. 31 (1986).

[28] E. Jacquet-Lagreze and M.F. Shakun, Decision support systems for semi-structured buying decisions, European Journal of Operations Research 16, 1, (1984) pp. 48–58.

[29] E. Jacquet-Lagreze and J. Siskos, Assessing a set of additive utility functions for multicriteria decision making: the UTA method, European Journal of Operational Research 10, 2, (1982) pp. 151–164.

[30] M. Jarke, Developing decision support systems: a container management example, Policy Analysis and Information Systems 6, 4, (1982) pp. 351–372.

[31] M. Jarke, ed., Managers, Micros, and Mainframes: Integrating Systems for End Users, London: John Wiley and Sons (1986).

[32] M. Jarke, M.T. Jelassi and M.F. Shakun, MEDIATOR: Towards a negotiation support system, forthcoming in M.F. Shakun, Evolutionary Systems Design: Policy Making under Complexity, San Francisco: Holden Day (1986).

[33] M. Jarke, M.T. Jelassi and E.A. Stohr, A data-driven user interface generator for a generalized multiple criteria decision support system, Proceedings IEEE Workshop on Languages for Automation, New Orleans, (1984) pp. 127–133.

[34] M. Jarke, H. Puller, and P. Thornton, Kosten-Nutzwert-analyse Zweite Automationsphase Deutsche Bundesbank, unpublished report, Frankfurt (1981).

[35] M. Jarke and Y. Vassiliou, Coupling expert systems with database management systems, in W. Reitman (ed.), Artificial Intelligence Applications for Business, Ablex, Norwood, NJ, (1984) pp. 65–85.

[36] M.T. Jelassi, An Extended Relational Database for Generalized Multiple Criteria Decision Support Systems, Ph.D. Dissertation, Department of Computer Applications and Information Systems, New York University, (May 1985).

[37] M.T. Jelassi, M. Jarke and E.A. Stohr, Designing a generalized multiple criteria decision support system, Journal of MIS 1, 4, (1985) pp. 24–43.

[38] P.G.W. Keen, Highways and traffic: building the telecommunications infrastructure, in Ref. 31 (1986).

[39] P.G.W. Keen and M.S. Scott-Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, Mass (1978).

[40] R.L. Keeney and C.W. Kirkwood, Group decision making

using cardinal social welfare functions, Management Science 22, (1975) pp. 430–437.

[41] C.W. Kirkwood, Social decision analysis using multiattribute utility theory, in S. Zionts (ed.), Multiple Criteria Problem Solving, Springer-Verlag, (1977) pp. 335–344.

[42] P. Klahold, G. Schlageter, R. Unland and W. Wilkes, A transaction model supporting complex applications in integrated information systems, Proceedings ACM-SIGMOD International Conference on Management of Data, Austin, Tx., (1985) pp. 388–401.

[43] C. Meador, P.G.W. Keen, and M. Guyote, Personal computers and distributed decision support, Computerworld, (April 1984).

[44] D. Michie, The state of the art in machine learning, in D. Michie (ed.), Introductory Readings in Expert Systems, Gordon and Breach, UK. (1982).

[45] R. Mildner, M. Jarke and H. Ohgke, Infektionshygiene im Krankenhaus, Medizin Mensch Gesellschaft 9, 1, (1984) pp. 38–47.

[46] L.W. Miller and N. Katz, Model management systems to support policy analysis, Decision Sciences Technical Report 82-11-01, Wharton School, University of Pennsylvania (1983).

[47] J. Mylopoulos and M.L. Brodie, eds., On Knowledge Base Management Systems, Springer-Verlag, forthcoming (1986).

[48] J. Owen, Game Theory, 2nd ed., Academic Press, New York (1982).

[49] D.R. Ries, Distributed databases and distributed processing between personal computers and mainframes, in Ref. 31 (1986).

[50] G.L. Sanders, J.F. Courtney, S.L. Loy, The impact of DSS on organizational communications, Information & Management, 7, 2, (1984) pp. 141–148.

[51] M.F. Shakun, Decision support systems for negotiations, forthcoming in M.F. Shakun, Evolutionary Systems Design: Policy Making under Complexity, San Francisco, Ca.: Holden Day (1985).

[52] T.R. Sivasankaran and M. Jarke, Logic-based formula management in an Actuarial Consulting System, forthcoming in Decision Support Systems (1985).

[53] R.H. Sprague and E.D. Carlson, Building Effective Decision Support Systems, Englewood Cliffs, N.J.: Prentice-Hall (1982).

[54] E.A. Stohr, DSS for cooperative decision making, NYU Working Paper Series CRIS #19, GBA 81-27 (CR) (1981).

[55] A. Tanenbaum, Network protocols, ACM Computing Surveys 13, 4, (1981) pp. 453–489.

[56] B. Tell, An approach to solving multi-person multiple-criteria decision-making problems, in S. Zionts (ed.), Multiple Criteria Problem Solving, Springer-Verlag, (1977) pp. 482–493.

[57] H. Thiriez, Multi-person multi-criteria decision-making: a sample approach, in H. Thiriez, S. Zionts (eds.), Multiple Criteria Decision Making, Springer-Verlag, (1976).

[58] M. Turoff and S.R. Hiltz, Computer support for group versus individual decisions, IEEE Transactions on Communications COM-30, 1, (1982) pp. 82–90.

[59] P.H. Winston, Learning and reasoning by analogy, Communications of the ACM 23, 12, (1979) pp. 689–703.

[60] P.H. Winston, Artificial Intelligence, 2nd edn., Addison-Wesley, Reading, Mass (1984).

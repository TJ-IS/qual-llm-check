---
otero_id: 26704
otero_key: "JCVT4D8F"
title: "Modeling Team Processes: Issues and a Specific Example"
authors: "H. Raghav Rao; Abhijit Chaudhury; M. Chakka"
year: "1995"
journal: "Information Systems Research"
doi: "10.1287/isre.6.3.255"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [129.105.215.146] On: 16 September 2016, At: 05:02 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## H4R

## Information Systems Research

![](/api/attachments/JCVT4D8F/fulltext/images/79bf51e1434abbb0bf4c95c9b748d4b4e5ea347cc37f61437a8bc36aa4518966.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Modeling Team Processes: Issues and a Specific Example

H. Raghav Rao, Abhijit Chaudhury, M. Chakka,

## To cite this article:

H. Raghav Rao, Abhijit Chaudhury, M. Chakka, (1995) Modeling Team Processes: Issues and a Specific Example. Information Systems Research 6(3):255-285. http://dx.doi.org/10.1287/isre.6.3.255

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1995 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/JCVT4D8F/fulltext/images/13f1d98f12403ee50ee9182a43d789830649e1ee64c7f720b02e80a3c426a9db.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Modeling Team Processes: Issues and a Specific Example

H. Raghav Rao

325G Jacobs Management Center

SUNY at Buffalo

Abhijit Chaudhury

Buffalo, NY 14160

College of Management

University of Massachusetts

Boston, Massachusetts 02125

with

M. Chakka

325G Jacobs Management Center

SU'NY at Buffalo

Buffalo, NY 14160

This paper develops a perspective to modeling team processes by drawing on concepts from team theory, and the informational processing and organizational paradigms. In such a perspective, humans and their interactions in a team are modeled as objects in a computerized environment. The behavior of the objects are specified in terms of the executable programs. A simulation testbed is described. Various information structures for team decision making in an example financial domain are examined. Questions regarding the relationship between information structure (who (knows) what, when, and how (the information is used)) and team performance are studied for the example. Thus this study can be seen as a step in the translation of behavioral and normative viewpoints of team decision making into a computational framework.

The results indicate that there are complex relationships between information structure and team performance. The conventional wisdom relating improved performance to more information is not always true. The experiments demonstrate several situations of team interaction where more information can lead to dysfunctional effects.

Team Processes—Computational Modeling—Information Structure— Team Performance

## 1. Introduction

eam processes have been studied in diverse literature from various perspectives. In some of these, the team is viewed from an economic angle, in others, the viewpoint is behavioral or sociological. The motivation behind research into these perspectives has been that within the complexities of real-world behavior, there lie some basic universal principles, which can be exploited to build effective team structures.

Team processes and information production, transfer, assimilation and use are inseparably intertwined. To analyze team behavior, besides addressing economic, behavioral and social science issues, it is important to also address the basic principles that underlie the characterization ofinformational aspects: namely, the specifications of the protocols for information exchange, the communications systems, description

1047-7047/95/0603/0255/\$01 25

of the group environment, and informational modeling of team decision making processes that includes modeling the members' cognitive aspects as well. In fact, informational aspects are an inevitable correlate of any team process.

This paper draws on concepts that are distilled from organizational paradigms, and from economic, social choice, and computer science theories. It then uses the concepts to discuss a “computational metaphor" (the modeling of a decision-making system as a computer program) (Doran 1985), that uses recent developments in information technology, primarily from the field of software engineering (Balzer et al. 1990), to model team processes. The ultimate objective of the computational modeling approach in the study of team processes is that it should function as a tool to uncover new insights, and ask new questions that can help researchers perceive problems in group contexts in a fresh light. For example, it should allow one to answer questions about the interrelationships between information structure (who (knows) what, when), and team performance. Following Simon (1990) we argue that computational models, similar to the one described in this paper can provide a bridge between theoretical, and experimental studies. The computational modeling approach is thus a vehicle for translation from the relatively abstract (the sociological and behavioral levels) to the relatively concrete level (that of the computational program).

This paper develops a perspective to modeling team processes by drawing on concepts from team theory, and the informational processing and social choice paradigms. In such a perspective, humans and their interactions in a team are modeled as objects in a computerized environment (Miller et al. 1992). The behavior of the objects are specified in terms of the programs that execute. A simulation testbed is described where computational versions of various team processes can be simulated. The use of the perspective is demonstrated by studying questions about the relationships between information structure (who (knows) what, when, and how (the information is used)), and team performance in the environment of the simulation testbed. The issue of interrelationship is studied in the context of an experimental scenario for team decision-making in a realistic financial domain. Thus this study can be seen as a step in the translation of behavioral and normative viewpoints of team decision making into a computational framework.

This paper is organized as follows: The next section details the motivation behind the paper, and discusses some of the related research. Section 3 identifies various dimensions of the computational perspective, ranging from the normative paradigms of group behavior such as team theory (Marschak and Radner 1972) to the information processing paradigm. Certain concepts from these dimensions are isolated for use in computational modeling of the team process. Section 4 discusses the computational perspective and details strategies for operationalizing theory. It lays out the elements of a high level simulation testbed used to build computational models of the team decision processes. In §§5 and 6, we use the perspective to study the issue of interrelationships between information structure and team performance. We experiment on an example financial resource allocation scenario (adapted from Senft 1987). Questions regarding the circumstances in which differences in information structure lead to dysfunctional effects such as reduced performance and whether increases in information actually lead to improved team performance are investigated. Answers to such questions would have implications on building IT platforms that determine how information is to be dispersed, how and when it is to be presented, in order to support a team. We also discuss the results and show how an understanding of the results can cast light on the relationships between information structures and team performance in the presence of other mediating variables. Finally, §8 concludes the paper.

## 2. Motivation and Related Research

Central to this paper, is the conviction that the relations between research on team informational processes and information technology, specifically artificial intelli gence and distributed computation, should be genuinely symbiotic. Our evolution towards this conviction rests in part on the fact that models in computer science and decision support systems are gaining much from models of group behavior, and organizational behavior. This is reflected in computer science literature in anthropomorphic terminology such as “actors" and “messages" in the work of Hewitt and his colleagues at M.I.T. (1977) and Holland's (1975) work on adaptation in systems. Huber and McDaniel (1986) have drawn on lessons from the various organization design models (rational, political, garbage can, etc.) for designing decision support systems. In fact, the evolution of software systems can be viewed as a special case of the evolution of groups consisting of both human and computer components (Wegner 1984).

In a reverse vein, and in a similar manner to some of the past research cited in subsection 2.1, we feel that the study of team informational processes and structures could gain from the various paradigms of computer science. Through computational modeling of such scenarios, and the incorporation of characteristics of decision makers and their cognitive processes in software, a decision theorist can study the evolutionary behavior of mixed man-machine systems and their interfaces in changing environments. Such studies could then provide the catalyst for major transformations, and can be extended to offer the ability to radically reshape the nature of fundamental business operations (Henderson 1987).

It is important however, to note the following. While anthropomorphism does allow the investigation of interesting parallels, its use has often been criticized because of possible errors of generalization (Krippendorff 1975). As a result theorists have generally avoided homomorphic extensions in favor of less stringent functional extensions (Walsh and Ungson 1991). In this research we follow the latter practice, i.e.. establishing that entities assume similar functions, thus allowing us to study alternate information structures in a team.

The advantages of the computational modeling approach over modeling organizational systems in terms of a normative or behavioral perspective, are several. First, a systematic vocabulary and mechanisms for computationally describing the essential components and characteristics of different team phenomena are provided. This allows development of computerizable specifications of the concepts underlying team informational processes. Second, the implementation of concepts in a running program provides a test of internal coherence and a test of foreseen and unforeseen consequences of a hypothesis. Third, in order to generate and test various hypotheses amidst complex behavioral patterns, it permits a variety of controlled experiments to be easily conducted. Therefore, it can be used to analyze and possibly improve the efficiency of operations in actual team situations. This computational approach to analysis, by providing a means for translating existing theoretical structures into computational programmable systems, would further understanding of the behavior of teams and can be used to facilitate the testing of theoretically plausible models embedded in empirical frameworks (Thagard 1988).

In addition, the computational modeling approach has advantages over modeling techniques based on pure linguistic descriptions as well as those based on mathematical models. For instance, models based on pure linguistic descriptions while flexible. are often logically inconsistent, while mathematical models have consistent structure and general solution techniques, but they suffer from loss of flexibility (Holland and Miller 1991). The computational modeling approach retains much of the flexibility of pure linguistic models while having precision and consistency enforced by the language. The resulting models are “dynamic and they are executable in the sense that the unfolding behavior of the model can be observed step-by-step. This makes it possible to check the plausibility of the behavior implied by the assumptions of the model" (Holland and Miller 1991).

## 2.1. Related Research

Recently, there has been a spurt of interest in the link between research in artificial intelligence, cognitive science, and the automated support of groups. This has resulted in interdisciplinary approaches to understanding how people and machines interact and how computers can be used to study organizational issues (Carlson and Ram 1990, Courtney and Paradice 1990, Prietula and Beauclair 1990, Rao et al. 1990, Weber et al. 1990).

The approaches that focus on team processes, information technology and artificial intelligence, can be categorized into three streams.

1. The traditional stream, where information technology (IT) tools such as artificial intelligence (AI) are applied to solve organizational problems, as seen in the vast literature on expert system applications for individual and group decision support (Rao 1992). Chen and Nunamaker (1989), for example, present an object oriented approach to creating a structured Electronic Brainstorming System, to support collaborative work for generating system specification tools for both organization and information systems modeling.

2. The alternate stream involves studying the nature of the interrelationship between information technology and group behavior. The focus is on the impact of IT on team performance (DeSanctis and Gallupe 1985, 1987).

3. While the focus of the first two streams is on using IT as a tool to support group performance and on studying the impact of IT on group performance, the focus of the third stream is to use IT as a modeling metaphor to describe and analyze group processes. This stream attempts at the unification of the cognitive and technological perspectives. Only recently has interest grown in this area, as is evidenced by the recent research of Blanning (1987), Malone (1987), Malone and Smith (1988), and Crowston et al. (1986). These works involve information technology and AI as paradigms and metaphors for modeling organizations, and also use IT/AI concepts to drive the modeling of organizational phenomena.

Malone (1987) and Malone and Smith (1988), in an analysis of organizational models have shown future trends in the structures of organizational forms of both human organizations and computer systems. Organizational structures that reflect tradeoffs between costs of coordination and the costs of flexibility can be created. These in turn, can be used to respond to dynamic business environments in terms of long term competitive capabilities. Crowston et al. (1986) use concepts from information technology/artificial intelligence to characterize information processing in organizations in terms of message exchange and the processing of messages. They show the utility of the approach in terms of a reduction in the levels of management. In a similar vein McIntyre and Higgins (1989) describe an object-oriented environment where stake holders are incorporated into a model of a team environment and the impact of their positions on decision issues are simulated.

The present paper falls into the third category of research as discussed above. The approach taken in this paper is a step in the operationalization of team processes through the concepts associated with information technology; of embedding behavioral theories or normative theories into computational programs; and a step to appropriate representation of team processes through which intelligent behavior and coordination can be simulated. At the least, it is a starting point for experimenting with basic possibilities and behaviors in different scenarios. With further refinements and extensions this approach could be used (to paraphrase Huber (1984)) by management scientists and computer scientists in working together to develop DSS generators and expert system technology (Henderson 1987) which could create, modify and discard specific DSS according to the needs of decision makers and managers.

## 3. Various Characteristics of the Computational Perspective

The computational approach to modeling allows us to explicitly ımplement an amalgam of powerful concepts available in economic, and social and organizational science for providing explicit concepts for modeling in groups. The range of concepts run from the economics literature (Arrow 1981, Marschak and Radner 1972) to group behavior and behavioral science (Benbasat and Taylor 1982, March and Shapira 1982, DeSanctis 1988, McGrath and Altman 1982, McGrath 1988), organizational theory (Galbraith 1974, Simon 1976) and psvchological literature (Einhorn 1977, Ramaprasad 1987). In this section, we shall distill some of the concepts from the fundamental literature in the area for specific use later in the simulation testbed environment.

This paper focuses on teams of intelligent members or objects, each with varying degrees of autonomy, and each with various choice structures, and internal models of the problem. As such, team processes may vary with the kind of team structure that is represented. There are two important aspects that influence team performance: the decision making aspect and the informational aspect. In order to characterize the decision making aspect, we use team theory as a fundamental building block. The informational aspect is probed primarily through the use of information processing paradigm.

## 3.1. Team Theory Aspects

The seminal work on characterizing teams is by Marschak and Radner (1972) in team theory. Team theory has focused on designing organizations as information processing systems for supporting decision making. Marschak and Radner (1972) define a team to be composed of members whose actions agree with certain rules and guidelines that further the common interest. Individual members have common interests and therefore, in team theory, there is no autonomy among the team members. Each team member can be viewed as having at his/her disposal, a set of information gathering experiments. A sequence of information gathering experiments define a strategy for an individual member. The member has to decide on a certain action or decision which is based on the information gathered. The team problem then, is to choose an information gathering strategy for each team member, a communication pattern followed by the team, and a set of final decisions for each of the members that best serve the welldefined interests of the team. The assignment of information gathering experiments and the communication pattern is known as the information structure, and the choice of decision rules is termed the decision structure. In other words, information structure is defined as who knows what and when. Information structure influences performance of the team (Marschak and Radner 1972).

However, most of the theory of teams has focused on choosing optimal decision structures for given or fixed information structures, rather than on focusing on alternate information structures (Arrow 1985). In addition, it is clear that team performance does not depend only on the information structure. Important mediating variables relate to the circumstances in which the information is being used to decide, and by whom, thus bringing up questions about the decision structure as well as the related environment.

## 3.2. Informational Aspects

The well-known paradigm of organizational and information system theorists, the Information Processing (IP) paradigm (Ungson et al. 1981) views organizations as being composed of units whose main function is to process information by exchang ing messages among themselves. A major component of this approach was developed by Galbraith (1974) to explain why different organizations have different structures. Galbraith pointed out that the main purpose of information processing was to reduce uncertainty. Organizations respond to environmental uncertainty by processing and exchanging information. Thus information requirements determine the structural characteristics and behavior of organizations. Another component of the IP paradigm (Simon 1976, 1981) takes into account the bounded rationality and bounded recall characteristics of humans. Since members of an organization are constrained by these cognitive limits to behavior, their goal is no longer to optimize their decisions. Instead they conduct heuristic searches for satisficing decisions which meet a psychologically determined level of aspiration. Therefore, the assumption of rational behavior is not a behavioral reality.

## 3.3. Autonomy and Cognitive Constraints among Team Members

Much of the traditional literature in the modeling of decision-making in groups and organizations is based on a rational and anticipatory approach (Raiffa 1968). It is assumed that organizations act by estimating the future consequences of alternative actions, forecasting future preferences over their possible consequences, and then choosing the rational outcome. Numerous empirical studies have shown that the decision process in groups is substantially less rational than such an approach suggests (Kay 1974). Alternatives to the rational anticipatory economic model have recently been offered by Lounamaa and March (1987) who focus on incremental and experiential learning by individuals and small groups.

In this paper, we suggest an approach that abstracts from the team theory and information processing paradigms. This paper diverges from the traditional team theory point of view in assuming that in reality it is reasonable to believe that (1) there is autonomy among the individual members of a team, and therefore specific constructs are needed to form a consensus to meet team objectives, (2) team performance over time is limited by the human cognitive constraints of bounded rationality and bounded recall and therefore, in order to deal with the limitations, it is necessary to incorporate intuitively appealing models of individual decision-making that economize on human cognitive resources (Lounamaa and March 1987).

In order to deal with the autonomous members in a team, it is necessary to typify procedures that can be used by teams so that members ultimately meet the team goals. For this, we use the literature in social choice theory on group judgment and consensus formation. The goal of consensus formation, can be attained in various different ways. For instance, one method of goal achievement is through search for a consensus through voting (Moulin 1983, Zahedi 1986) involving appropriate weighting mechanisms for members of the organization (represented by objects). Voting leads to the best possible decision(s) for the team (not necessarily the individual) under certain special conditions. We have to assume that a team decision is to be reached by “combining" the decisions of all its members. If the team operates on democratic principles, each member's decision influences the final outcome (the team decision), in exactly the same way. Then each member receives one vote and has as much influence legally or arithmetically on the final outcome as every other vote. The team decision is then determined by the majority of the voters which should result in the best possible decision for the team (Moulin 1983).

An extension to the one member-one vote principle is to use different weighting schemes to weight team members according to a predefined set of rules so as to emerge with one final choice or decision. Einhorn (1977) conceptualized group judgment as a weighted combination of the judgments of individual members and suggested that one critical issue was the process used by the group to allocate weights to the opinions of different members. Four baseline models were suggested: (a) the random model, (b) the proportional model, (c) the mean or composite model, consisting of the unit weighted composite (where each member is weighted equally) and the unequal weighted composite, and (d) the best member model (where the best member of the group has the largest weight).

In order to handle the cognitive limitations of bounded rationality and bounded recall, we focus on incremental changes in behavior based on feedback as a means of individual decision making. Humans modify their behavior based on their experience and such behavioral modification is less demanding cognitively than most normative models. This concept also has a stronger natural and psychological basis than anticipatory and rational approaches to team decision making. Since decisions are taken over time, it is advisable to incorporate feedback into the team decision-making process (Lounamaa and March 1987, March and Shapira 1982, Simon 1981). There is considerable support in literature for using such models for team decision making (Lindblom 1959, 1965, Cyert and March 1963, Nelson and Winter 1982, Lounamaa and March 1987).

As a first step in the modeling exercise, we look at the team viewpoint and center on designing teams as consisting of interacting decision making members with a common goal. Each member could have different viewpoints with different information structures, and each one could do his/her own inferencing, as long as, ultimately, the objectives of the team are met. Throughout the paper, we take an internal perspective (McGrath 1988) to the team process. In other words, primary attention is on processes internal to the team that is being focused on.

Within such a computational model, it should be possible to vary parameters pertaining to the various team members and simulate different situations through the

Rao · Chaudhury · Chakka  
![](/api/attachments/JCVT4D8F/fulltext/images/fea746b34bbebe15643b79e8879e54b0ea2765b311b9e7597beaaaff83ee3841.jpg)  
e 1. In team theory, relationships between team performance, information structures and individual decision-making are specified.  
e 2 In the computational perspective, team performance is related to information structures in the presence of individual decision-making that is autonomous and cognitively realistic.

FiGURE 1. The Computational Perspective.

synthesis of computational and behavioral viewpoints. The computational model would allow analysts to tackle the problem of design of information structure or of relating such structures to performance as to be able to identify or map how team performance varies with changing information structures. This would allow us to meet the experimental goal of gaining an understanding of the variations in the team performance with variations in plausible information structures (See Figure 1.)

## 4. The Computational Modeling Environment

The computational modeling approach could further understanding of complex human systems. Human experiments in the laboratory setting allow only relatively simple experiments involving a few variables to be carried out. In contrast, the computational approach allows an experimenter to study a myriad of possible strategies that an individual or group may adopt, at relatively low cost, in a step-by-step manner, continually checking for plausibility of behavior exhibited by the model.

There are however, several sometimes key, concepts used in normative and behavioral theories of organizations that do not have a demonstrably clear equivalent in the computational paradigms. Normative theories themselves are based on the underlying assumption of rationality. Rationality is sometimes not humanly feasible, as has been pointed out by Simon (1981). Basing the computational model on normative theories would not allow the emulation of realistic human behavior. Behavioral theories on the other hand, include, for instance, ideas of creativity, and concepts relating to social phenomena such as power, politics, and social cohesion. Such concepts are ambiguous and often there are features that are not understood by anyone well enough to be modelled. As such it may not be possible for the computational model to mimic human processes exactly or in some cases, even approximately. Even so the advantage of using the computational model is that it is easy to relax and test different assumptions and hypotheses. Computational modeling is neither normative (it does not support the concept of the idealistic rational), nor highly descriptive (in that some rich concepts relating to human behavior cannot be mimicked) but it can be used to generate a prescriptive approach to team behavior (Kleinmuntz et al 1988). If a certain model of team behavior performs well in an experiment, it gives us some ground for faith that such behavior will be successful in the real-life situations as well.

## 4.1. A High Level Environment: The Simulation Testbed

To be able to simulate various information structures and their linkage to team performance, it is necessary to build a simulation testbed at the specific level of the members of the team. We need a language or tool to express the information in a conceptual model. For this, we use a hybrid methodology that, for the sake of brevity, we call Grouptalk (after Smalltalk). Grouptalk makes use of the following metaphors: object oriented and rule based systems, and blackboards and message passing semantics (Chandrasekaran 1981, Decker 1987). It is thus that this approach helps to operationalize theory, and incorporate behavioral viewpoints (for instance the axioms of utility theory) into a computational tool. The use of this approach produces a unique experimental environment. The information, knowledge. experience and expectations of each team member can be fully controlled. By perturbing different parameters, multiple variations of team processes can be explored. The approach thus allows an easily manipulated model world in which one can generate and test theoretical hypotheses. Miller et al. (1992) term this as the "natural, long-overdue extension of simulation . . . ‘Beyond what-if" ". (Note. It may be possible to run the same experiments in an assembly language environment: however the advantage of using Grouptalk is that it allows one to describe and build such models in a more natural and rapid fashion, similar to the advantages that 4GL languages have over 3GL languages.)

A computational model must account for:

—Decisions taken at multilevels of a team hierarchy (objects in a team with various attributes).

—Processes and events that occur in the decision making process.

—Data structures and data elements (that implement rules of individual and team behavior).

Of course, because of the complexities of reality it is not possible to map every object in the real world into the computational environment. Therefore, we must, to quote Simon (1990, p. 7), “separate what is essential from what is dispensable in order to capture in our models a simplified picture of reality, which nevertheless will allow us to make inferences that are important to our goals".

This paper uses the object-oriented approach. The value of using the object-oriented approach for computational modeling lies in that it provides a clear correspondence between the objects in the computational model to objects in the real world. Importantly it allows one to easily identify in the model the representation of the concepts used to formulate the propositions one wants to explore, the key issue being visibility and correspondence.

## 4.2. The Object-oriented Paradigm

The object oriented paradigm (Cox 1986, Goldberg 1983) allows the modeling of systems in terms of objects and actions on objects. In addition a number of key concepts make the object-oriented metaphor a powerful tool for modeling team decision making at various levels of abstraction.

TABLE 1  
The Parallel Between Team Characteristics and the Computational Version

<table><tr><td>Team Characteristics</td><td>Computational Version</td></tr><tr><td>1. Human Members</td><td>Objects</td></tr><tr><td>2. Individual Choice Behavior</td><td>Object-Methods</td></tr><tr><td>3. Team Interaction</td><td>Interaction of Messages that invoke methods</td></tr></table>

1. Objects are classified according to their similarities and differences. A class defines the behavior of similar objects by specifying their internal representation, the variables they contain, and the methods available for responding to messages that are sent to them.

2. Encapsulation refers to the characteristic that objects (which are the units of encapsulation) are viewed as black boxes whose behavior is internally defined. The encapsulated object consists of the class description protocol as well as the private data of the particular instance of the class, within a protected boundary (Pinson and Wiener 1988).

3. Objects can communicate with other objects only by sending messages. The information within the object, that implements its behavior is essentially hidden from other objects. This is known as information hiding. An object is known to other objects only through its behavioral characteristics and not through its internal constitution. Thus a user need not understand the internal processing to evoke an appropriate response.

4. The same message can invoke different responses from different objects. Such polymorphic behavior allows the use of entirely different kinds of objects in various ways,

5. A technique whereby new classes (subclasses) are built on top of other classes by specializing the already existing older ones (superclasses) is called inheritance. Classes are created by first inheriting all the variables and behavior defined by a more primitive class and then increasing by specialized variables and behaviors.

6. Methods are the algorithms that determine the details of an object's internal behavior and performance. When a message is sent to an object, a method is evaluated and an object is returned as a result. Protocol definitions of a class always have two parts, class methods and internal methods. Class methods implement messages sent to the class. Instance methods implement messages sent to instances of the class.

Most (though not all) object-oriented systems have the features mentioned above.

## 4.3. The Parallel between Team Characteristics and the Computational Version

The fact that a team can be represented as a number of intelligent objects embedded in a communication network, naturally lends itself to modeling in terms of the object-oriented paradigm (Blanning 1987, Cook et al. 1987, Stefik and Bobrow 1986, Tsichritzis et al. 1987). (See Table 1.)

This paradigm regards program execution as a physical model that can simulate the behavior of either a real or imaginary part of the world. A physical model consists of objects, each object characterized by attributes, knowledge (a set of behavioral rules that take into account the objects local environment), and a sequence of actions. Actions executed by objects essentially reflect transformations or information processes that change the measurable properties of the various phenomena represented by the objects (Agha 1986). These actions can be extended either concurrently with other action sequences or as a part of other action sequences.

4.3.1. Modeling Individual Information Processing and Decision Making In Grouptalk all team members are modeled as objects. Objects have their own private memories and knowledge (or a set of rules). By encapsulating both procedural and declarative information and describing an object in terms of methods and procedures, it is possible for objects to have conflicting viewpoints without compromising the integrity of the system. Each of the objects can be teamed into classes and classes can be arranged into hierarchies with property inheritance. This has an important implication for modeling. Attributes and properties can be shared among individuals in the team while at the same time individual variations can be allowed (Rao 1986). In this context it is pertinent to cite Miller et al. (1992) who mention that the appropriate use of inheritance hierarchies can greatly simplify the specification of a complex situation, producing comprehensible models. The interaction between objects is based on the semantics of message passing. Sharing of information can be realized either through an exchange of messages, or through shared global memory. Objects are also characterized by the type of messages that they respond to. A particular message is responded to by executing a method or a process. Thus an object can be assumed to do all the processing of its internal data and values received as parts of messages using the methods and processes. Thus signals or messages sent by objects can be observed, and inferences about behavior can be drawn.

Representing methods in objects as rule based or logic programs, allows the creation of objects with reasoning capabilities. Such representations (in terms of situation-action rules, or cause-effect rules) allow the incremental development of knowledge bases, as well as allow adaptive activities. They provide explicit constructs for deductive decision making, support inferences, and allow the derivation of new relationships from old ones. In addition, choice structures and voting mechanisms can be modeled in terms of rules in the internal representation of objects.

4.3.2. Modeling Communication Patterns: Blackboard and Message Passing Paradigms. Another precondition for collaborative team decision making is that the members should work in parallel. Thus the need for the computational model to support concurrent and asynchronous actions where actions are executed in parallel. Another need as important as concurrency, is for interaction mechanisms to bring about a meaningful connection between the concurrent processes, and tie the objects into one cohesive system without taking away the autonomy of the objects.

In order to deal with these issues we subscribe to certain critical abstractions: the concepts or organization mind and organizational memory (Sandelands and Stablein 1987, Walsh and Ungson 1991). Organizational memory has been defined as the “stored information from an organization's history that can be brought to bear on present decisions. This information is stored as a consequence of implementing decisions to which they refer, by individual recollections, and through shared interpretations . . . Information can be considered as decisional stimuli and responses that are preserved in particular storage bins and that have behavioral consequences when retrieved" (Walsh and Ungson 1991, pp. 61).

Keeping the concept of organizational memory in mind, two paradigms that are important in the context of the above issues are shared global memory using the blackboard model (Nii 1986) and message passing in terms of the Actor model of concurrent computation (Agha 1986, Hewitt 1977). (Alternate paradigms can also be used as models of different kinds of organizational structures. For example, some real-time conferencing systems (Yavatkar 1990) employ the notion of a “floor" where only a “speaker" that has the floor is allowed to “speak" (or transmit data) at any time. A single token enforces concurrency control over a multipoint connection. Other environments (Sarin and Greif 1985) envisage a session breaking up into smaller discussion teams and thus holding multiple, concurrent conversations. Also some cooperative environments (Stefik et al. 1987) include a notion of a brainstorming session where no concurrency control is needed.)

The blackboard model is an effective cooperation structure' (Filman and Friedman 1984). Blackboard models were conceived to handle parallel and asynchronous message communication which was poorly modeled by the sequential von Neumann model. The blackboard model allows distributed asynchronous interaction between cooperating knowledge sources without central supervision (Pearl 1982). The communication lines are open at all times, each agent may interrogate the message board for revisions made by its neighbors, update its own belief parameters and post new messages on the board that can be seen and read by the neighbor.

The blackboard model is a useful method of integrating knowledge from various sources. Complex problems are partitioned into subtasks which are handled by different knowledge sources or agents. The knowledge is segmented into “agents’ or modules containing related entities, and each agent is provided an inference engine. Note that there is no requirement for the different agents in the knowledge base to use the same representation method, nor for the inference engines to operate in the same way. These different agents use shared memory (the blackboard) to post messages, post partial results, and find information. The blackboard becomes the exclu sive medium of communication between agents. The communication between agents is limited to reading and writing on the blackboard, thus each agent must read/write in a format acceptable to other agents (Engelmore and Morgan 1988) Subsequently a control mechanism or scheduler then controls the integration of information and determines if the current information levels are enough to solve the problem. It examines potential actions in terms of estimated consequences, ranks various actions, and executes the highest ranking action (Nii 1986).

In the Actor model of concurrent computation, interaction among different agents is accomplished through a message passing mechanisms. Agents are like objects in object-oriented languages which exist in parallel with each other. They can accept requests for performing tasks, decompose tasks into subtasks to be performed by other agents, and send requests to other agents. An agent's behavior is a combination of two characteristics: (a) actions that can be taken in response to messages and requests, (b) acquaintances which are known to the agent. Agents in a message passing system do not directly affect each other and can thus retain the object-like characteristic of independent agents. The asynchronous communication of Actors parallels posting letters. One composes a message, drops it in the mail and continues one's activities (Filman and Friedman 1984).

The two techniques (blackboard and message passing) can be further illustrated by analogy with a classroom scenario (Rao et al. 1994). The blackboard method is analogous to a classroom where the students are not encouraged to exchange information among themselves (a free exchange of information could result in chaos) but they are allowed to discuss the problem with the teacher and the medium of discussion is the blackboard. That is if the teacher wants to solve a problem, rather than have a one-to-one communication with one student, the teacher puts the solution on the blackboard so that other students can also have access to the solution. Pure message exchange is effective in a case where a few students are working on a lab project and need to exchange a large amount of information. Here it is much more effective to use a message passing mechanism because of the shorter communication paths involved. Many systems use the combination of the blackboard and message passing mechanisms.

In summary, we use two different paradigms at two levels of computation. Interobject computation uses an object oriented paradigm, which encompasses the blackboard, and message passing models of distributed artificial intelligence. Intraobject computation may be based on a rule based or on a logic programming paradigm. Thus the object-oriented world that we work in contains messages of information that provide behavioral rules (internal representation of objects) and methods for object manipulation

## 5. An Experimental Scenario

The focus of this section is the study of the impact of the information structure on the performance of the team that is being served by that information structure. We define an information structure, “the assignment of signals to agents" (Arrow 1985) in terms of spatial and temporal distribution of information, i.e., who is informed about what and when. We believe that performance of a team is dependent on the information structure that serves it and that effects of alternate structures on performance may be studied through simulation. The focus is on simulating alternate information structures and studying their performance with respect to measures explicitly related to the decision-making task.

While simulation has been used as one of the approaches to studying organizations (Baligh and Burton 1984, L.ounamaa and March 1987) the nagging question has always been that of external validity. On the other hand simulation allows the researchers to control conditions and replicate experiments several times under the same conditions yielding internal and statistical validity. On the other hand the process of abstraction from the real world leads to many kev variables and elements being left out and that creates justifiable doubts about the validity of relationship between the real world and the model simulated. However simplification and abstraction confer their own benefits (Miller et al. 1992, Simon 1990). It is possible to learn the relationship between a limited set of input and output variables and what caused that relationship. By excluding many other factors one can be sure that their presence did not cause the observed output. We believe our assumptions and our experiment are sufficiently realistic to study and gain insight into the relationship between information structure and team performance.

The relationship between information structure and performance is mediated by variables related to the organization structure in which the information structure is embedded. The components that define the organization structure have to be defined

Team Performance = function {Information Structure, Decision Structure, Environment

Rao · Chaudhury · Chakka  
![](/api/attachments/JCVT4D8F/fulltext/images/cf25a5fd1c28cc5cb371245226c7caa931bdeb7b169a3346441a4d4848caa834.jpg)  
Output Variable = Team Performance  
Input Variable = Information Structure  
Mediating Variables = Decision Structure, Environment

FIGURE 2. Model of Team Performance

and established as the environment, within which the primary input parameter of the experiment the information structure, would be varied (Refer to Figure 2) and related to the output parameter which is the team performance.

We paraphrase Baligh and Burton's (1981, 1984) definition of an organization structure in terms of the three elements of Figure 2.

## A. The Decision-Structure

1. The decision-makers in the team.

2. The decision problems that the team is solving; the decisions to be made in each period by each decision-maker.

3. The decision rules and mechanism used by each decision-maker; given the information each member can produce his/her decision (Arrow 1985).

B. Information Structure

1. What information is supplied to what decision maker and who supplies the information (or in the words of Arrow (1985), “. . . The assignment of signals to agents").

## C. The Environment

1. The reward-system under which the decision makers are operating.

2. The degree of turbulence in the environment where the information originates.

In the simulation of organizational situations one could choose an artificially constructed problem and environment (e.g. Lounamaa and March 1987) or a decision problem and an environment that has some features of the real world. In view of our concern with the external validity of our model we have adopted the second approach. The scenario is adapted from Senft (1987) and deals with fund management in a financial institution. This scenario has several advantages in the context of our goals. For example, there is a single dimension of team performance; there is a hierarchy of decision-makers which is a common feature of organizations; the interaction of individuals in the team is built around the issue of “share-a-pie," not an unusual feature in the real world of management of finite resources. The “pie" that we chose is dynamic in the sense that the size of the pie can get bigger if the team does well and may get smaller if the team performs badly.

To put the system in perspective, the system that this paper is concerned with can be classified as a complex adaptive system according to Holland and Miller's (1991) definition. The system is complex in the sense that it “(i) consists of a network of interacting agents; (ii) it exhibits a dynamic aggregate behavior that emerges from the individual activities of the agents, and (iii) its aggregate behavior can be described without a detailed knowledge of the behavior of the individual agents." The agent in the system is adaptive in the sense that “(i) the actions of the agent in its environment can be assigned a value (performance), and (ii) the agent behaves so as to increase this value over time." Finally the environment of each adaptive agent includes the other agents in the system.

## 5.1. The Simulation Model

A. The Decision Structure: The financial institution is organized as a two-level hierarchy, with a coordinator at one level and three money managers on the other, who together as a team constitute the set of decision makers. The coordinator's decision-problem is to allocate resources among the three managers so as to maximize the team return. The managers' decision-problem deals with the choice of investing funds and whether to choose a risky or less risky option. Thus polymorphic behavior crops up in this scenario, since different managers would respond differently to the same message. In our representation the coordinator is helped by a blackboard, to and from which all messages are posted, and read.

In the simulation model the return on investment y is generated by following equation (based on the well-known CAPM model of finance): $k _ { , } = i + ( k _ { m } - i )$ be $\tan _ { j } + u ,$ where $k _ { i } =$ the rate of return for investment j, i = risk free rate of interest, $k _ { m } =$ the rate of return of the market as a whole, and beta, = investment /'s beta value, and u is the error term (Gaussian noise) following a normal distribution with a mean of zero (Schall and Haley 1988, Brigham and Gapenski 1988).

The rate of return on investment j during a given time period depends heavily on what happens to the general market, while a beta coefficient is the most relevant measure of a stock's risk relative to the average stock. The higher the beta, the greater (lower) the expected return if the market return is expected to be higher (lower) than the risk-free rate. In a volatile market where $" k _ { m } \ " { }$ is likely to swing above and below $\ " _ { i } \ " $ over a period of time, a high beta, value would amplify the devıation in return $\because k _ { I } . \ddot { } A$ stock that has a beta greater than 1 is unusually sensitive to market movements; a stock with a beta less than 1 is unusually insensitive to market movements (Brealey and Myers 1991). For the purposes of the simulation we assume that i, the risk free rate is the same as it was in the early 90s, i.e., 8.0 percent (Brealey and Myers 1991, p. 163). $k _ { m }$ is the return on the "market portfolio." It is common to use a surrogate such as the S&P 500 Index or the CRSP Equally weighted index for this market portfolio. We assume that $k _ { m }$ is 15 percent (Jacob and Pettit 1988). This is a justifiable assumption, because the market risk premium, $( k _ { m } - i )$ has averaged 8.4 percent a year over the last $^ { 6 3 }$ years (Brealey and Myers 1991), though the conventional wisdom is that this year $k _ { m }$ is expected to be down to about 10 percent

The risk propensity of the managers (represented by the betas) ranges from high to neutral to low. If the risk propensity is high we assume a representative beta of 1.5, if the risk propensity is neutral, we assume a beta of 1.00 and if the risk propensity is low, we assume a representative beta of 0.5 (Schall and Haley 1988). We choose these representative betas because “most betas are in the range of 0.50 to $1 . 5 0 ^ { \circ }$ (Brigham and Gapenski, 1988 p. 189). The initial condition in all simulation runs assumes that Manager 1 has a high risk propensity, Manager 2 has neutral risk propensity and Manager 3 has low risk propensity. Over a simulation run, managers can change their risk propensities by choosing different average beta values of their investment.

The coordinator has a fund of \$1,000 to begin with in the first period and allocates resources in each period among the money managers in order to maximize return on the fund. The coordinator's decision problem is how to share the fund among the three managers. At the beginning of every period the coordinator allocates the available fund to the three managers. In the first period, the allocation is equal. The initial allocation of resources is based on Einhorn's (1977) unit weighted composite model (i.e., the one member-one vote principle used in the literature of consensus formation), where each of the three money managers are allocated an equal amount of resources. (It is important to note that this is one plausible method of initial allotment of resources. Many other methods exist in resource allocation literature (Radner 1972, Bellman 1961)). This is a very credible allocation rule, especially if we assume that the coordinator has no prior knowledge, or biases about the effectiveness of any of the money managers. This rule corresponds to Laplace's decision rule in decision theory. Laplace's rule is of course valid, when the return functions are assumed to be concave. In the case when better money managers exhibit increasing returns to scale in their investments, it might be better to pick a money manager at random and allocate all of the resources to her.

The three managers invest their allocated budgets in the stock exchange according to their risk propensities. At the end of each period the return is handed back to the coordinator. The coordinator adjusts the share of the managers in the next period proportionally depending on their performance (the one member-one vote principle is now replaced with appropriate weighting mechanisms).

The bases for decision-making mechanisms for the managers and the coordinator are incremental feedback mechanisms based on history. For justification for using such a experiential history based decision-making in our model, readers may refer to Lounamaa and March (1987). The grounds for the mechanism is the fact that individuals and teams of individuals in organizations learn from experience. Current behavior reflects lessons learnt from the past and changes in behavior are essentially incremental modifications of past behavior. A decision maker learns from the consequences of each step before carrying out the next (March and Shapira 1982).

The decision mechanism for the coordinator is: When a manager keeps making good decisions, the advice is incrementally (over a period of time) weighted by the coordinator more than other money managers. This results in the share of good managers being changed favorably as compared to those of poor managers. This is a credible assumption found often in decision making scenarios. (Though some readers may argue here that “the race is not always to the swift", we would like to counter with the oft quoted saying, “The race is not always to the swift, but that is where to look!")

<table><tr><td colspan="3">INFORMATION STRUCTURE</td><td colspan="2">(ENVIRONMENTAL TURBULENCE)</td></tr><tr><td></td><td>Manager Informed</td><td>Coordinator Informed</td><td></td><td></td></tr><tr><td>Structure 1(NI)</td><td>No</td><td>No</td><td>Level A</td><td>0.05</td></tr><tr><td>Structure 2(CI)</td><td>No</td><td>Yes</td><td>Level B</td><td>0.1</td></tr><tr><td rowspan="2">Struct 3 (CIWI)</td><td rowspan="2">No</td><td rowspan="2">Yes with injection</td><td>Level C</td><td>0.2</td></tr><tr><td>Level D</td><td>0.3</td></tr><tr><td>Struct 4 (OMI)</td><td>Yes</td><td>No</td><td>Level E</td><td>0.4</td></tr><tr><td>Struct 5 (BI)</td><td>Yes</td><td>Yes</td><td>Level F</td><td>0.5</td></tr></table>

FIGURE 3. Levels of Variables

The decision mechanism for the individual managers is: Each manager is amenable to change in an incremental manner. A change in a situation may cause a change in the risk taking propensity of the manager. For example, if a manager finds that one of the other managers is doing better in terms of the returns received, the said manager changes his/her risk propensity to copy the more successful one. This kind of phenomena has been well documented in economic literature (Kephart et al. 1990) According to Arthur (1988) “economic agents may be influenced by neighboring agent's choices". The result is a coevolutionary system in which individual agents are simultaneously trying to adapt to one another (Kephart et al. 1990). Recall the old adage, “What is good for the goose is good for the gander!".

B. The Information Structure. The information that is available to the managers is identified by their individual performance and the performance of the other managers. The coordinator can be informed about the performance of the team and the performance of the individual members. With a two-level hierarchy, this allows us to set up four separate information structures (refer to Figure 3);

1) No Information (henceforth denoted by NI) is supplied to the coordinator or the individual managers: This is like a base-line static scenario against which other scenarios can be measured. In this model the managers continue with their initial risk propensity features throughout the simulation run and the coordinator does not deviate from an equal share rule.

2) Only the Coordinator is Informed (CI): In this scenario, the coordinator allocates the budget in the next period based on the ratio of the current period's performance to the last period's performance. If the rate of return of any manager is less than or equal to -1, it implies that the manager has lost all its money and is not allocated any more money. If the rate of return is between 0 and –1. it implies that the manager is losing his capital and he is allocated only 20% of the capital he returns back (note that this is a parameter that can be varied and its effect simulated). The remaining amount is allocated to the other managers (provided their rate of return is positive and more than the risk free rate of return) in proportion to the ratio of their rate of return.

A variant to the above structure that is possible³ is as follows:

3) The Coordinator is Informed and uses (Wuth) Injection of funds (CIWl): This is similar to the above except in the following option. The coordinator keeps 10% of the total fund (\$100) with himself and invests it in a risk-free certificate of deposit for five periods at the risk-free rate of 8%. The coordinator keeps track of the managers' performance over the five periods. Finally at the beginning of the sixth period, the manager injects the kept aside fund into the best performing manager.

The motivation for this alternate scenario is that in order to even out some of the risk, a possible solution is for the coordinator to withhold some resources during the early periods, placing them in a low-risk (or no risk) low-yield investment as a safety buffer, for later investment when the quality of manager's judgments are better known. However, it should be noted that the strategy of creating a buffer has its cost. Even so, it would seem safe to say that the greater the degree of uncertainty, the greater the need for buffers. Alternate scenarios can also be tested: for example, the coordinator can decide that whenever the fund goes bankrupt, the firm should be able to get back its initial vestment (Bordley 1988).

4) Only Managers are Informed but not the Coordinator (OMI): At the end of each period the managers compare their returns with those of the other managers. If the others are doing better, the said manager changes his risk propensity to more closely match that of the manager who is doing the best in the relevant period. The Coordinator however continues allocating the resources equally to each manager. The manager's decision mechanism is thus dynamic but the coordinator follows a static decision mechanism

5) The Managers and the Coordinator are Both Informed (BI): This is a combination of both the Coordinator and the managers using information to decide anew at each period.

C. The Environment. Different managers have various levels of autonomy, and a combination of differing and coincident viewpoints. In addition to the properties that are common to financiers, each manager has certain heuristics and behavioral rules that are implicitly followed, and which distinguishes him/her from the other money managers. For example, a manager may have a high or neutral or low risk propensity. As a result, the investment recommendations would differ from manager to manager. However each manager has to work under general guidelines and policies, for example, a common reward system.

The reward system for the decision-makers can be described as follows: The managers are rewarded according to their individual performance and thereby try to improve their performance using the decision rules and mechanism as described in the previous section. Similarly, the coordinator is motivated to maximize the team return and follows the decision mechanism as described previously

The turbulence (Gaussian noise) is captured by the “u" term of the model which generates the return on individual investment. By adding Gaussian noise with zero mean and standard deviation sigma to each payoff, we are able to model several different effects (i) intentional inclusion of randomness in decision procedure, (ii)

TABLE 2

<table><tr><td colspan="7">Mean Team Performance Values at Each Level</td></tr><tr><td rowspan="2">Information Structure</td><td>Noise Levels</td><td>0.05</td><td>0.10</td><td>0.20</td><td>0.30</td><td>0.40</td></tr><tr><td>No Information Supplied (NI)</td><td>5633.97</td><td>5750.32</td><td>7280.03</td><td>4291.11</td><td>1960.00</td></tr><tr><td>Only Coordinator Informed (CI)</td><td>6711.29</td><td>6272.69</td><td>2512.85</td><td>2243.63</td><td>1278.46</td><td>1171.81</td></tr><tr><td>Only Manager Informed (MI)</td><td>11250.08</td><td>8432.35</td><td>6362.04</td><td>5327.61</td><td>5868.88</td><td>3134.61</td></tr><tr><td>Coord. Informed w/Injection (CIWI)</td><td>7113.49</td><td>5053.52</td><td>6522.92</td><td>1891.19</td><td>2004.52</td><td>1746.61</td></tr><tr><td>Both Informed Mgr &amp; Coord. (BI)</td><td>9693.15</td><td>12983.96</td><td>22389.67</td><td>923.93</td><td>2804.41</td><td>5615.57</td></tr></table>

heterogeneity in payoffs among the population of agents, or (iii) imperfections or uncertainties in the information (Kephart et al. 1990).

## 5.2. Experimental Design and Hypotheses

The example uses the Smalltalk-V environment for simulations. The environment supplies a large number of reusable objects which can be used to model the basic components of the system under study. Simulations are constructed by assembling the appropriate building blocks taken from the library of SMALLTALK objects (Goldberg 1983). The purpose of the simulation exercise is to uncover the relationship between the dependent variable, team performance, and the independent variable, information structures, in the presence of the mediating variable of environment turbulence (Gaussian noise).

Simulations were carried out for five different information structures (as discussed above) at six different levels of noise.

For each information structure and at each level of turbulence, the simulation was carried out for 20 periods. For each of the three managers, the performance was simulated 20 times and then averaged. The output, i.e., team performance, was the aggregate return of the money managers μ. The experiment resulted in a total of 36,000 simulated data points.

We shall test the following main hypothesis at each of the six turbulence levels:

Differences in information structures (j) have no effect on team performance.

H10: $\mu _ { 1 } = \mu _ { 2 } = \mu _ { 3 } = \mu _ { 4 } = \mu _ { 5 } .$

H11: At least one $\mu _ { j }$ is different from the others; $j = 1 , . . . , 5 ( 1 = \mathrm { N I } , 2 = \mathrm { C I } ,$ ${ \bf 3 } = { \bf C I W I } , { \bf 4 } = { \bf O M I } , { \bf 5 } = { \bf B I } )$

If there is evidence that the means differ, then detailed analysis of the factor level is warranted. If the evidence leads to the conclusion that the factor level means $\mu _ { j }$ are equal, the implication is that there is no relation between the factor and the dependant variable (Neter et al. 1985).

If the statistical tests show that the factor level means differ, we shall proceed directly to the estimation of the difference between factor level means. We shall examine how they differ and what the implications of the differences are. Our motivation is to understand the consequences of taking one decision or another in the context of one information structure or another and uncover both foreseen and unforseen consequences. (The mean values of team performance over twenty periods are shown in Table 2).

TABLE 3  
Summary of Anova Procedures for Different Noise Levels

<table><tr><td>Noise Levels</td><td>Mean</td><td>C.V.</td><td>F-value</td><td>Pr &gt; F</td></tr><tr><td>0.05</td><td>8080.39</td><td>33.01</td><td>15.07</td><td>0.0001*</td></tr><tr><td>0.1</td><td>7698 57</td><td>42.35</td><td>19.43</td><td>0.0001*</td></tr><tr><td>0.2</td><td>9013.50</td><td>126.14</td><td>9.18</td><td>0.0001*</td></tr><tr><td>0.3</td><td>2935.49</td><td>80.19</td><td>11 89</td><td>0.0001*</td></tr><tr><td>0.4</td><td>2783.25</td><td>98.04</td><td>8.78</td><td>0.0001*</td></tr><tr><td>0.5</td><td>3216 75</td><td>183.57</td><td>1.94</td><td>0.1098</td></tr></table>

\* Significant values.

## 6. Results Summary

To recapitulate, there are several reasons why this scenario has been chosen. First, the example is adapted from an actual scenario described in Senft (1987). Second, the example involves a two level team, and therefore allows us to model a simple hierarchic structure. Third, the scenario allows us to model four different information and feedback structures: (i) no information as to performance, (ii) and (iii) information is fed back only to one level (either managers or coordinator), (iv) feedback information is supplied to both levels (both manager and coordinator). Fourth, there is a unidimensional measure of team performance, the aggregate return on investment. Fifth, the model allows us to study team performance as a function of different information structures. Sixth, the scenario allows us to model the three characteristics of complexity in the context of organizational behavior and information systems that are set forth by Huber (1984): the numbers of entities in a team, their mutual interdependence and their diversity. The interdependence is modeled by the fact that the team has a single pie to share (the pie is dynamic), and the diversity is modeled through having money managers with different risk propensities

The one way ANOVA procedure was used to test hypotheses 10. At every level of environmental turbulence, except at the 0.5 level, the hypothesis was rejected in favor of the alternate hypothesis. In other words, Hypothesis 10, testing the performance difference among different information structures is rejected at a $\mathbf { \nabla } . p$ level of 0.0001 for the lower turbulence levels while it is not rejected at the highest turbulence level Except at the highest turbulence level, this result establishes the significant effect of information structures on performance (See Table 3). The implication at the high turbulence level is that the unpredictability of the market share is an example of how uncertainties can foment highly volatile dynamics which can confound the results of the simulation.

Consequently, more detailed tests of factor level effects are warranted at the lower turbulence levels (all levels except 0.5). We utilize the Bonferroni Multiple Comparison Method (Neter et al., 1985) to test whether or not the ten factor level means $\pmb { \mu } _ { J }$ and $\mu _ { j ^ { \prime } } ( j = 1 , \ldots , 5$ and  is not equal to j') differ at each of the five levels of environmental turbulence (a total of fifty tests). (See Table 4.)

The results about the team performance are as follows:

1. At the 0.05 noise level: a. The no information (NI) scenario yields a significantly lower performance than the only managers informed (OMI) and the both informed (BI) scenarios.

TABLE 4  
t-Scores U'sing the Bonteronnı Test

<table><tr><td>Noise Levels</td><td>0.05</td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td></tr><tr><td>NI-CI</td><td>-1.27709</td><td>-0.50666</td><td>1.325881</td><td>2.750653*</td><td>0.78981</td></tr><tr><td>NI-OMI</td><td>-6.65749*</td><td>-2.60137*</td><td>0.255318</td><td>-1.39246</td><td>-4.52986*</td></tr><tr><td>NI-CIWI</td><td>-1.75386</td><td>0.675844</td><td>0.210573</td><td>3.224121*</td><td>-0.05158</td></tr><tr><td>NI-BI</td><td>-4.81186*</td><td>-7.01609*</td><td>-4.20239*</td><td>4.523573*</td><td>-0.97855</td></tr><tr><td>CI-OMI</td><td>-5.3804*</td><td>-2.0947*</td><td>-1.07056</td><td>-4 14311*</td><td>-5.31967*</td></tr><tr><td>CI-CIWI</td><td>-0.47677</td><td>1.182507</td><td>-1 11531</td><td>0.473469</td><td>-0.84139</td></tr><tr><td>CI-BI</td><td>-3.53477*</td><td>-6.50942*</td><td>-5 52827*</td><td>1.77292</td><td>-1.76836</td></tr><tr><td>OMI-CIWI</td><td>4 903626*</td><td>3 277209*</td><td>-0.04474</td><td>4.616582*</td><td>4.478276*</td></tr><tr><td>OMI-BI</td><td>1.845625</td><td>4.41472*</td><td>-4.45771*</td><td>5 916034*</td><td>3.551307*</td></tr><tr><td>CIWI-BI</td><td>-3.058*</td><td>-7.69193*</td><td>-4 41296*</td><td>1.299452</td><td>-0.92697</td></tr><tr><td colspan="6">T-CRITICAL = (1 - α/2g; nt - r) = (.975; 100 - 5 = 95) = 1.980</td></tr></table>

\* Significant values.

b. The Both coordinator and manager informed (BI) scenario yields better results than all other scenarios except the only managers informed scenario. where the results are inconclusive. Similarly the only managers being informed scenario performs better than other scenarios except the scenario when both are informed.

c. The coordinator being informed with injection (CIWI) scenario performs worse than when both are informed and when only the managers are informed, though the results with respect to the only coordinator informed scenario (CI) and the no information scenario are inconclusive

2. At the 0.1 noise level: a. The team performance in the no information scenario (NI) is significantly lower than in the only managers informed and both informed (OMI and BI) scenarios.

b. The team performance in the both informed scenario consistently outperforms all other scenarios.

c. The team performance in the OMI scenario outperforms others except BI.

d. The coordinator informed with injection (CIWI) scenario has a worse performance than OMI. BI and is inconclusive w.r.t. CI and NI.

3. At the 0.2 noise level: a. The only significant finding is that the Both Informed scenario outperforms all other scenarios.

4. At the 0.3 noise level: a. Team performance in the No Information (NI) scenario is significantly better than in the CI, CIWI, BI scenarios but is inconclusive w.r.t. OMI.

b. OMI outperforms CIWI, BI, CI but is inconclusive w.r.t. NI.

5. At the 0.4 level of noise· a. The only significant finding is that the team performance in the Only Manager Informed scenario outperforms the Coordinator Informed, Coordinator Informed With Injection, Both Informed and No Information scenarios.

The output of the financial problem solving process is studied for the team in terms of the return on investment of each manager based on the recommendations over a period of time, the change in risk behavior, and the change in the weighting model.

The results show that team performance changes as a result of providing information (a) to the team coordinator and (b) to the team members

Tables 3 and 4 and the attached graphs (see Figure 4) suggest that in team situations, there is no simple relationship between more information to adapt and improved team performance. While it is generally true that some information is better than none, especially at low noise levels, there are cases when the team is well served by the situation of no information to adapt to. In one particular case at higher turbulence (0.3 level) the no information strategy gives a solid positive return on investment while not being subject to violent fluctuations.

Under the conditions seen above, there is no simple linkage between the team members' individual performance and their gains or rewards. Behavioral theorists have (based on operant conditioning theories (Skinner 1974) emphasized that humans and organisms do respond to such feedback. In such conditions, it may be better to have no information or limited information dispersal. Interestingly the example shows that while in nonturbulent environments, the option of both levels having information for adaptation is a good option, this is not true in turbulent environments. In general at lower error variances, the best performance occurs when both the coordinator and the managers are provided information to adapt. However such a strategy deteriorates at higher error variances. At high error rates it is better for the managers to have the information to learn, but not both the managers and the coordinator. A plausible reason is that the learning of each results in actions that counteract the actions of the other. The dysfunctional behavior possibly results from misinterpretation problems associated with either simultaneous change in behavior or a noisy and turbulent environment. Remember the old adage: Too many cooks spoil the broth!

Interestingly, the case when the coordinator withholds some resources during the early periods placing them in a low risk-low yield investment, to be later injected when the quality of the mangers' judgments are better known, turns out to be almost uniformly among the two worst strategies to follow for the team. The other is when the coordinator learns without injection. Two possible explanations can be thought of for this phenomenon: The first possibility is that the fifth period is too early for injection of the buffer fund, i.e., the system has not stabilized by the ifth period. The second possibility is that though the buffer fund may be injected into the portfolio of the best money manager at that time, the said money manager may be at a peak and henceforth be on a downward slide, thus justifying the saying: Do not put all your eggs into one basket!

The reason why both strategies that involve coordinator being provided information for learning are among the worst could be the one observed by Lounamaa and March (1987). The mechanism is too impatient when environmental signals are ambiguous. Slowing the rate of adaptation may be the solution to the problem. (We shall pursue this in greater detail in future research.)

## 7. Discussion

The experiments throw some light on the relationships between information structures and team performance in the presence of other mediating factors. Of course, the experimental results are subject to the specific features of this experiment. The conclusions are generalizable only to the extent that these features are natural. Notwithstanding our concern for the validity of the simplistic model against the complexities of reality we believe that these simulation experiments do carry many critical real-world features such as: individuals modifying behavior due to experience; randomness in the feedback in terms of performance signals; and the necessity of finite resource sharing leading to interactions. In the limited world of the simulations, these experiments display the mutual interplay of the above factors.

Error Rate 0.1  
Error Rate 0.2  
![](/api/attachments/JCVT4D8F/fulltext/images/e69c06e9b87677e767b1630af97306afebf0ae2e2b5ba6efc0a87df281ce2641.jpg)

![](/api/attachments/JCVT4D8F/fulltext/images/01008e478e2f3241f141e52755da823caa9c866186aefbe9fa920b5a6ba14d70.jpg)

![](/api/attachments/JCVT4D8F/fulltext/images/c01f633c84554b419b3d118da2ca3bb54a237f4a3c07fb9e198f240384e5d7d9.jpg)  
FiGURE 4. Aggregate Team Performance.

Rao · Chaudhury • Chakka  
![](/api/attachments/JCVT4D8F/fulltext/images/46cc13fe488900a321fe7eb6b8b954244cc571ef3ea61a114c6229cf8ef049e6.jpg)

![](/api/attachments/JCVT4D8F/fulltext/images/7c3227beaa90cf876d926021c6f97b8503b7c665788b373b63094592a0474034.jpg)

Error Rate 0.5  
![](/api/attachments/JCVT4D8F/fulltext/images/b402b1c88707ac853c629a1a9d011b69c9d3434101dd50ccef0733c064b574ee.jpg)

There are two aspects that are important in terms of the experiment:

(1) The performance of an individual being subject to perturbations outside the model. These perturbations are random factors beyond one's control. In situations where one's performance is subject to random forces that are not in one's control, one may either be too slow to interpret or sometimes too quick to conclude from the data stream. In either case information feedback that is too frequent (for example, both manager and coordinator being informed at high turbulence) or too infrequent (for example, the no information scenario at low noise levels) may lead to ineffective behavior. Thus one is as likely to learn false lessons as the right ones and which may lead ultimately to performance deterioration (Lounamma and March 1987).

(2) Similarly, simultaneous changes in behavior by several members of team can make interpretation of information more problematic. The nature of interaction assumed in the team in this case is based on the sharing of a resource. Better performers get a larger share of the pie. They are compensated for their performance in that they get greater returns from their share of resource (because their performance is better) and they also end with a higher share of the original resource itself. Poorer performance suffers from double jeopardy. Poor performers earn less from their resource and also get a deduction in the share of their pie.

If the experiment had assumed no interaction, that is, total independence among the individuals in the team, then the conclusion would have been very different. We believe that such a case would only have been a trivial instance of team information structure in that the team performance would have been the simple aggregation of the individual performance based on an individual's information structure. In the situation of mutual independence, an individual who follows a bad decision strategy, in presence of randomness, would more often than not receive a feedback that penalizes him/her. The reverse would happen when the individual follows a better strategy.

Over time the individual money manager would improve his/her performance due to the experiential feedback. When the results are averaged it would show more or less a monotonic improvement in performance. Of course, in no situation will the behavior be exactly identical for the two individuals. (The situation is similar to two individuals tossing two fair coins, where it is unlikely that they will have the same numbers of heads or tails.)

Where interaction exists, the situation is very different. Confounding effects due to simultaneous modification of behavior result. If we assume that people do modify their behavior with feedback it raises doubts as to the efficacy of reporting of information when their performances are based on mutual interactions. It is this phenomenon that is being simulated here.

Let us look at two simple situations. Suppose, there are two individual managers who follow either (a) a good strategy; or (b) a bad strategy for decision making. In both situations their initial behavior is identical. In the case of independence while their feedback will not be identical because of the stochastic nature of the experiment and the random perturbations determined by small events outside the model, their individual behavior will improve in an uneven way over time and both behavior patterns will show a certain similarity towards the end. But when we have scenarios involving “share-a-pie" interaction, the situation becomes different. First, because of differential feedback due to randomness, one manager would start getting his/her share increased while the other would experience a decrease (though they are both following the same strategy). The one suffering the decrease would interpret the feedback as a penalty and try to move away from the good strategy that he/she is following. Due to a mistaken interpretation, instead of following the good strategy the manager may end up with a worse one. For the other manager, the reinforcement will be more positive than usual. Due to such misinterpretations the team may perform worse than usual (Arthur 1988).

The situation is similar when both the managers follow the poorer strategies. Again, even though the individuals may use the same strategy, differential experience due to randomness would occur. This differential experience (even though the strategies are same) would lead to one manager having a larger share of the pie and interpreting this as a reward for following a “good” strategy when not. Again, in this case the team may perform poorer than otherwise. The experiments, thus, throw some light on the complex and hidden relationship among information structures and team performance in the presence of other mediating factors.

On the other hand, one strategy may be “inherently better" than the other but has “bad luck" in gaining a better performance early. The eventual outcome may not be of maximum possible benefit; in essence the scenario may lead to possible inefficiencies (Arthur 1988).

A possible implication is that a more refined information structure that is perhaps more expensive, more real-time and extensive in information dispersal need not lead to improved performance in all situations. How the information is interpreted is a crucial element that mediates the relationship between information structure and group performance. This interpretation activity is in turn affected by the nature of the problem, the reward structure, and the nature of decision making. It is important therefore to point out a note of caution: information structure designers may proceed with discretion whenever the problem situation is characterized by random effects and individual decision makers interact closely in terms of their performance and decision making.

## 8. Conclusion

This paper has focused on a computational modeling approach for teams. At the more specific level, a multiparadigm computational model of teams is discussed. Members of teams are modeled as objects. Interobject computation is in terms of the objectoriented paradigm, and intraobject computation is modeled via a rule based or logic based paradigm. Different team decision making strategies can be embedded into the internal representations of team members in terms of rule-based mechanisms.

Huber (1984) lists information acquisition and distribution as one of the three important features of post industrial organizations. Deepening our understanding in this area would have direct relevance as to how well information systems are designed.

The implementation of the financial scenario clearly demonstrates the power of the computational modeling approach to model complex human and team scenarios The simulation has shown how the conventional wisdom that more information is positively linked to performance does not hold universally. The experimental findings obtained in our experiments provide some parallel analogous evidence, at high environmental turbulence levels, for the recent attacks on the conventional wisdom that more expenditure on IT leads to improved performance (Thurow 1991, Katzman 1991). Thurow points out that knowledge of what should not be known is as important of what should be known, in order to capture the promised payoffs of new technologies. Katzman remarks about his personal experience of rarely observing improved decision making with improved information availability (Katzman 1991). Though our simulation has shown that this is true at higher environmental turbulence levels, this is certainly not true at lower turbulence. Such experiments can provide an indication of circumstances where such dysfunctional behavior can be possible. The tentative conclusions that can be drawn are cautionary in nature and can be useful to the designers of information technology platforms, in terms of designing information structures for information distribution, for supporting a team or an organization.

Research in group behavior can be classified into three classes: normative, descriptive, and prescriptive. The normative approach is that of operations research. game theory and team theory. The purpose of the approach is to improve the decisionmaking abilities of a group by providing it with analytical capabilities. The descriptive approach (McGrath 1982, 1988) attempts to describe the group processes, with the objective of enhancing group process design. The third approach is the prescriptive approach: it uses models of group behavior that can be implemented in practice and that can be studied for further refinement and can help improve group performance. Computers with their ever increasing power present us with the possibilities of doing prescriptive research associated with small groups and organizations. In future research, alternate theories will be explored through comparative studies of alternate team decision procedures, and alternate informational structures (who knows what, when and how the information is used). Specifically, we intend to look at questions such as: How does information lag affect decision-making and thereby performance? That is, is it always the case that online information access is superior to periodic reporting? What kind of informational distribution among the coordinator and the manager and frequency of reporting be optimal in (i) stable and deterministic situations, (ii) in stable but noisy conditions, (iii) in evolving but deterministic situations, and (iv) in unstable and noisy conditions?\*

Acknowledgments. The authors are indebted to the three anonymous referees and the AE for their detailed critical comments that have considerably enhanced the lucidity of the paper, and to Professors Burton Swanson and John King for their encouragement. We wish to thank Y. I. Song for his research assistance and also Professor Gail Rein for comments on the paper. This research was supported in part by the National Science Foundation under Grant No. IRI-9011424. The first two authors are in random order to reflect equal contribution.

## References

Agha, G., Actors: Model of Concurrent Computation in Distributed Systems, MIT Press, Cambridge, MA 1986.

Arrow, K., Socıal Choice and Indivıdual Values, Cowles Commission Monograph 12, Wiley, New York 1981.

——, “Informational Structure of the Firm,"AEA Papers and Proceedıngs, 75, 2 (May 1985), 303–307.

Arthur, W. B., “Self-Reinforcing Mechanisms in Economics." in The Economy as an Evolvıng Complex System, P. W. Anderson, K. J. Arrow and D. Pines, Eds, Addison-Weslev, Reading. MA. 1988.

Baligh, H. and R. Burton. “Describing and Designing Organization Structures and Processes," Internatonal Journal of Policy Analysis and Informaton Systems, 5, 4 (1981), 251–266.

- and —, “The Process of Designing Organization Structures and Theır Information Substructures" in S. K. Chang (Ed.), Management and Office Information Systems, Plenum Press, New York 1984,3-25.

Balzer, R., R. Fikes, M. Fox, J. McDermott, and E. Soloway, “AI and Software Engineering: Will the Twain Ever Meet?," Proceedings of the 8th National Conference on Artıficial Intelligence, Vol. 2, AAAI Press, 1990.

Bellman, R. E., Adaptive Control Processes• A Guuded Tour, Princeton Univ. Press, Princeton, NJ, 1961.

Benbasat, I. and R. N. Taylor, “Behavioral Aspects of Information Processing for the Design of Management Information Systems," IEEE Transactions Svstems Man and Cybernetics, SMC, 12, 4 (July/ August 1982).

Blanning, R. W., “Expert Systems as an Organizational Paradigm," Proceedings of the 8th International Conference on Information Systems, 1987.

Bordley, R., “An Additive Group Utılıty for a Fund Manager," Management Science, 34, 7 (July 1988).

Borgida, A., “Features of Languages for the Development of Information Systems at the Conceptual Level," IEEE Software (January 1985)

Brealey R. A. and S. C. Myers, Princıples of Corporate Finance, McGraw Hill, New York, 1991

Brigham E. F and L. C. Gapenskı, Financıal Management· Theory and Practice, The Dryden Press, Chicago, IL, 1988

Carlson, D. A. and S. Ram, "Modelıng Organizations as a Social Network of Distrıbuted Knowledge-Based Systems." Proceedıngs of the 23rd Hawau Internattonal Conference on Systems Sciences, Hawaii, Vol. 4, 1990.

Chandrasekaran, B., “Natural and Socıal System Metaphors for Distributed Problem Solving," IEEE Trans on Systems Man and Cybernetıcs, SMC-Il (January 1981).

Chen, M. and J. F. Nunamaker, “Integration of Organızation and Information Systems Modeling: An Object-Oriented Approach," Proceedıngs of the 22nd HICCS Conference, R. Blanning, and D King Eds., 1989.

Cook, P , C. Ellis, M. Graf, G. Rein, and T. Smith, “Project Nick: Meetings Augmentation and Analysis," ACM Transactions on Office Information Systems, 5, 2 (April 1987)

Copeland, T. E. and J. F. Weston, "Asset Pricing," The New Palgrave, Finance, J. Eatwell, M. Milgate and P. Newman, Eds., MacMillan Press, New York, 1989.

Courtney, J. and D. Paradice, "Intelligent Organızations," Proceedıngs of the 23rd Hawait International Conference on Systems Sctences, Hawaii, 1990.

Cox, B. J., Object Oriented Programming' An Evolutionary Approach, Addison-Wesley, Reading, MA, 1986.

Crowston, K., T. W. Malone, and F. Lin, “Cognitive Science and Organizational Design: A Case Study of Computer Conferencing," Proceedıngs of the Conference on Computers Supported Cooperative Work. Austin, TX, 1986.

Cyert, R. M. and J. G. March, A Behavioral Theory ofthe Firm, Prentice-Hall, Englewood Cliffs, NJ, 1963

Decker, K. S., “Distributed Problem Solving Technıques: A Survey," IEEE Transactions Systems Man and Cybernetics. Vol. SMC-17, 5 (Sept/Oct 1987).

DeSanctis, G., “Small Group Research in Information Systems: Theory and Method," Harvard Colloquuum on Experımental Research in Information Systems, University of British Columbia, Canada, August 1988.

—— and B. R. Gallupe, “Group Decision Support Systems: A New Frontier," Database (Winter 1985)

- and —, “A Foundation for the Study of Group Decision Support Systems," Management Science, 33, 5 (May 1987)

Doran, J., “The Computational Approach to Knowledge, Communication and Structure in Multi-Actor

Systems," Socıal Action and Artıfıcıal Intelligence, N. Gilbert and C. Heath, Eds., Gower Publishing Co, 1985.

Einhorn, H. J., R. M. Hogarth, and E. Klempner, “Quality of Group Judgment," Psychologıcal Bulletın 84 (1977).

Engelmore, R. S. and T. Morgan, Blackboard Systems, Addison-Wesley. Reading, MA, 1988

Filman, R. E. and D. P. Friedman, Coordinated Computing: Tools and Technıques for Distrıbuted Soft ware, McGraw Hill, New York, 1984.

Galbraith, J. R., “Organizational Design: An Information Processing View,"Interfaces, 4. 3 (May 1974).

Goldberg, A., Smalltalk-8O The Interactve Programmıng Envıronment, Addison-Wesley, Readıng, MA, 1983.

Henderson, J. C., “Finding Synergy Between Decision Support Systems and Expert Systems Research," Decision Sctences, 18, 3 (Summer 1987).

Hewitt, C. E., “Viewing Control Structures as Patterns of Passing Messages," Journal of Artificial Intelhgence, 8, 3 (1977).

Holland, J. H., Adaptation in Natural and Artıficıal Systems, Unıv. of Michigan Press, Ann Arbor, MI, 1975.

and J. H. Miller, “Artificial Adaptive Agents in Economic Theory," Amerıcan Economic Review (May 1991).

Huber, G. P., “The Nature and Design of Post-Industrial Organization," Management Science, 30, 8 (1984).

and R. R. McDaniel, “The Decision Making Paradigm of Organization Design," Management Science, 32, 5 (May 1986).

- and ——, “Exploiting Information Technologies to Design More Effective Organizations," Managers, Micros, Maınframes, M. Jarke, Ed., John Wiley, New York, 1986.

Jacob N. L. and R. R. Pettit, Investments, Irwin, Chicago, IL, 1988.

Katzenbach, J. R. and D. K. Smith, “The Discıpline of Teams," Harvard Business Review (March-April 1993), 111–120

Katzman, R., “The Siren Song of New Machines," Computerworld, December 23, 1991.

Kay, N. M., The Innovating Firm, St. Martin's, NY, 1974.

Keen, P. G. W. and M. S. Scott Morton, Decision Support Systems - An Organızational Perspecttve, Addison-Wesley, Reading, MA, 1978.

Kephart, J. O., T. Hogg, and B. A. Huberman, “Collective Behavior of Predıctive Agents," Physıca D 42 (1990), 48–65.

Kleinmuntz, R. A., J. R, Sullivan, L. A. Tomassini, “Audıt Decision Making." Research Opportunities in Auditıng The Second Debate, A. R. Abdel-Khadil and Ira Solomon, Eds , American Association of Accounts, Audit Sector, FL, 1988

Kraemer K. L. and J. L. King, “Computer-based Systems for Cooperative Work and Group Decision Making," ACM Computıng Surveys, 20, 2 (1988).

Krippendorff, K., "Some Prnciples of Information Storage and Retrieval in Society," General Systems 20 (1975), 15–35

Lindblom, C. E., “The Science of Muddhıng Through," Publıc Admınıstration Review, 19 (1959), 79–88.

—, The Intelligence of Democracy, Free Press, NY, 1965.

Little, J. D. C., “Research Opportunities in the Decision and Management Sciences," Management Sct ence, 32, 1 (January 1986).

Lounamaa, P. and J. March, “Adaptive Coordination of a Learning Team," Management Science, 33, 4 (Jan. 1987).

Malone, T. W., “Modeling Coordination in Organizations and Markets," Management Science, 33, 10 (October 1987)

and S A. Smith, “Modeling the Performance of Organizations Structures," Operattons Research, 36, 3 (1988).

March, J. and Z. Shapira, “Behavioral Decision Theory and Organizational Decision Theory," Decısion Makıng An Interdıscıplinary Inquıry, G. R. Ungson and D. N. Braunstein, Eds., Kent Publishing. Boston, MA, 1982

Marschak, J. and R. Radner, Economıc Theory of Teams, Yale Universıty Press, New Haven, CT, 1972.

McGrath, J. E., The Social Psychology of Time, Sage Publications, 1988.

— and I. Altman, “Group Research," Annual Review of Psychology, 33 (1982)

McIntyre, S. C. and L. F. Higgins. “Embedding Stakeholder Analysis in Object-Oriented Organizationa

Modeling," Proceedıngs of the 22nd Hawaiı International Conference on Systems Sciences, R. Blanning and D. Kıng, Eds., 1989.

Miller, D. P., R. J. Firby, P. A. Fishwick, D. W. Franke, and J. Rothenberg, “AI: What Simulationists Really Need to Know," ACM Transactions in Modelıng and Computer Simulation, 2, 4 (October 1992), 269–284.

Moulin, H., The Strategy of Social Choice, North-Holland, New York, 1983.

Nelson, R. R. and S. G. Winter, An Evoluttonary Theory of Economic Change, Harvard University Press, Cambridge, MA. 1982.

Neter, J., W. Wasserman, and M. H. Kutner, Applted Statistıcal Linear Models, Richard Irwin, Homewood, IL, 1985.

Nii, H. P., "Blackboard Systems: The Blackboard Model of Problem Solving and Evolution of Blackboard Architectures," AI Magazine, 7, 2 (1986).

Pearl, J., “Reverend Bayes on Inference Engines: A Distributed Hierarchical Approach," Proceedıngs of AAAI-82, August 18–20, 1982, Pittsburgh, PA, 133–136)

Pinson, L. J. and R. S. Wiener, An Introduction to Object-Oriented Programmıng and Smalltalk, Addıson-Wesley, Readıng, MA. 1988

Prietula, M. J. and R. A. Beauclair, “Artificial Intelligence and Organization Theory: Introduction to Minitrack," Proceedıngs of the 23rd Hawau International Conference on Systems Sciences, Vol. 4, Hawai, 1990.

Radner, R., “Allocation of a Scarce Resource under Uncertainty: An Example of a Team,"C. M. McGuire and R. Radner, Eds., Decision and Organızation (1972).

Raiffa, H., Decision Analysıs, Addıson-Wesley, Reading, MA, 1968.

Ramaprasad, A., “Cognitive Process as a Basıs for MIS and DSS Design," Management Science, 33, 2 (February 1987).

Rao, H., “Intelligent Management Systems: Cooperative Problem Solvers," Proceedings of DSS-86, J. Fedorowicz, Ed., Washington, DC, 1986.

-, R. P. Cerveny, G. L. Sanders, R. Sridhar, and E. J. Garrıty, "Intelligent Control and Resolution of a Network of Learning and Problem Solvıng Processors," Proceedings of the 23rd Hawaii International Conference on Systems Sctences, Hawau, 1990.

-, "Technology Transfer: Makıng Expert Systems Commercially Successful,"IEEE Expert, 7, 2 (April 1992), 5–10.

-, R. Sridhar, and S. Narain, “An Active Intelligent Decision Support System - Architecture and Simulation," Decision Support Systems, 12 (1994).

Sandelands, L E. and R. E. Stablein, "The Concept of the Organization Mind," Research in the Sociology of Organızations, Vol. 5, JAI Press, 1987, 135–161.

Sarin, S. and I. Grief, "Computer-based Real-Time Conferencing Systems,"IEEE Computer, 18, 10 (October 1985). 33–49

Schall, L. D. and C. W. Haley, Introduction to Financial Management, McGraw Hill, NY, 1988.

Senft, D., “Science and Technology Revolutionize Wall Street," The Science of Makıng Money, 1987.

Simon, H. A., The Sciences of the Artificial, MIT Press, Cambridge, MA, 1981.

—, Adminıstrative Behavıor. A Study of Decısion-Makıng Processes in Administrative Organızations, 3rd edition, Free Press, New York, 1976.

-, “Prediction and Prescription in Systems Modeling," Operations Research, 38, 1 (January-February 1990).

Skinner, B. F., About Behavıoraltsm, Knopf, New York, 1974.

Stefik, M., G. Foster, D. G. Bobrow, K. Kahn, S. Lannıng, and L. Suchman, “Beyond the Chalkboard Computer Support for Collaboration and Problem Solving in Meetings," Communications of the ACM, 30, 1 (January 1987), 32–47.

and D. G. Bobrow, “Object Oriented Programming: Themes and Variations," AI Magazine, 6, 4 (Winter 1986).

Thagard, P., The Computational Philosophy of Science, MIT Press, Cambridge, MA, 1988.

Thurow, L. C., Foreword to The Corporation of the 1990s· Information Technologv and Organizational Transformatton. M. Scott Morton. Ed. Oxford University Press, Cambridge, 1991.

Tsichritzıs, D. C., E. Fiume, S. Gibbs, and O. M. Nierstrasz, “KNOs: Knowledge Acquisition, Dissemination, and Manipulation Objects," ACM Transactions on Office Information Systems, 5, 1 (1987)

Ungson, G. R., D. N. Braunstein, and P. D. Hall, "Managerial Information Processing: A Research Review," Admınistratıve Science Quarterly, 26 (March 1981).

Walsh, J. P. and G. R. Ungson, “Organizational Memory," Academv of Management Revıew, 16, 1 (1991), 57-91.

Weber, E. S., Y. I. Liou, M. Chen, and J. F. Nunamaker, "Toward More Intelligent Organizations," Proceedıngs of the 23rd Hawaii International Conference on Systems Sctences Hawaii, 1990

Yavatkar, R., “Communication Support for Collaborative Multimedia Applications," Technical Report 181-91, Department of Computer Science, University of Kentuckv, December 1990

Wegner. P., “Capital Intensive Software Technologies," IEEE Software (July 1984)

Zahedi, F., "Group Consensus Function Estimation When Preferences are Uncertain." Operations Research. 34, 6 (November/December 1986)

---
otero_id: 20835
otero_key: "GDYFJ36K"
title: "Conflict decision training through multi-space co-operation"
authors: "Hai Zhuge"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00064-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Conflict decision training through multi-space co-operation <sup>1</sup>

Hai Zhuge

Laboratory of Computer Science, Institute of Software, Chinese Academy of Sciences, Beijing, People’s Republic of China

Accepted 24 February 2000

## Abstract

Conflict group decision training has three key characteristics: dynamic situation, continuous decision, and cognitive co-operation. Previous models and systems do not entirely reflect these characteristics. This paper proposes a cognitive-based conflict group decision training framework. The conceptual model of the framework reflects the cognitive process and behaviour co-ordination among cognitive space, method space, information space, and resource space in a conflict decision process. The computing model of the framework formalises the conceptual model as an automata-based formalism, which is supported by a cognitive co-operation implementation mechanism and a dynamic conflict situation evaluation approach. A conflict group decision training environment ACTOR implements the framework. Decision makers can be trained in the environment that supports dynamic situation, continuous decision, and cognitive co-operation. An example shows the training process of using the environment. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Agent; Cognitive co-operation; Conflict; Group decision; Training

## 1. Introduction

Conflict group decision is a dynamic and continu ous group decision process under conflict restraint. Its application fields concern commerce competitionŽ in sales market , sports games , state safety strategy. Ž . Ž making , military warfare or training , environmen- . Ž . tal protection pollution and protection , etc. Prob- Ž . lems in these fields are usually semi-structured, and concern complex, uncertain, incorrect, changing, and large amounts of information. Real conflict experimentation in these fields is usually expensive or difficult to carry out e.g., warfare . Hence, conflictŽ . group decision modelling and simulation training are of significance in these fields.

The conflict problem to be discussed consists of two intelligent groups e.g., the blue team and theŽ red team in warfare simulation with limited re- . sources available. The two groups usually have conflict targets tasks . Both of them want to reach theirŽ . targets with the lowest expenditure. The comparison of two groups’ current strengths and degrees of reaching their target reflect the conflict situation. During the conflict period, the two groups make decisions intelligently and continuously i.e., oneŽ group does not need to wait for the opponent’s decision until a terminal condition is satisfied. A. decision affects the evolution of the current situation on which the succeeding decision is based. Conflict decision training concerns the co-operation among the instructor and two conflict groups, the co-operation among the decision makers within each group, and the co-operation between each group and its support system. Thus, conflict group decision training has three characteristics: dynamic situation, continuous decision, and cognitive co-operation.

Related research works have been done in such fields as group decision support systems GDSS ,Ž . dynamic decision, game theory, and conflict analysis. Traditional decision models on GDSS focus on the method of making group decisions e.g., formingŽ a group decision through synthesising group members’ preferences while not paying much attention. to the problems of the environmental change during the decision making period and continue decision making under conflict restraint 2,14 . A continuous<sup>w</sup> <sup>x</sup> decision support system for conflict group decision training applications has been introduced 24 . The<sup>w</sup> <sup>x</sup> model is based on rules and rule-based reasoning. Research on dynamic decision concerns the technique aspect of system construction and the cognitive aspect of some particular applications <sup>w</sup> <sup>x</sup> 6,16,19,22 . The applications of dynamic decision include production control and planning, scheduling, etc 3,4,7,18,20,21 . In these previous systems and<sup>w</sup> <sup>x</sup> models, decisions do not cause any active and intelligent response. Decisions can usually be adjusted to reach a better outcome through properly processing the feedback. Although the feedback from dynamic environment has been regarded as an important factor in making a proper decision, the feedback is still commonly disposed as either a kind of data information or a passive response to a decision 19,24 .<sup>w</sup> <sup>x</sup> However, in conflict applications, the feedback information usually contains a lot of uncertain and incorrect information, which can mislead the succeeding decision making. Thus previous approaches and systems for GDSS and dynamic decision are inadequate for conflict applications.

Standard mathematical models of game theory <sup>w</sup> <sup>x</sup> 1,15 are for multiple step decision in structured, well-defined and small scale conflict applications. Each decision step of one part needs to wait for the decision of another part, and the situation does not change during the response period. These models are inadequate for supporting continuous decisions in conflict environment. Previous research works have also indicated that standard computational techniques for game-theoretic reasoning are inadequate for dealing with realistic games that have large imperfect information 13 .<sup>w</sup> <sup>x</sup>

Conflict analysis approach is a way to forecast the result of conflict through the modelling process and the stability analysis process 10 . The modelling<sup>w</sup> <sup>x</sup> process is to form a set of optional decisions, possible results, and a preference vector. The preference and the stability analysis reflect human common thinking. Unfortunately, the approach does not include human cognitive ability and the restraints in conflict application. Actually, unusual strategies and tricks can be frequently used, and decision making is also restricted by multiple factors such as time stress, cognitive biases, and psychology 14 . The conflict<sup>w</sup> <sup>x</sup> analysis approach is suitable for the application fields that include small optional set of decisions.

Cognitive co-operation plays an important role in the process of conflict group decision. This paper proposes a cognitive-based framework for conflict group decision training through investigating the cognitive process and behaviours in the process of conflict group decision. We conceptually divide the space carrying out conflict into four parts: a cognitive space, a method space, an information space, and a resource space. Conflict group decision and training are conceptually modelled on the basis of a cognitive cycle and the co-ordination among behaviours in these spaces. Then, we formalise the conflict group decision training process as an automata-based formalism, which is supported by the implementation approaches for cognitive co-operation and dynamic conflict situation evaluation. Based on the framework, we describe an agent-based conflict group decision training environment AC-TOR. Agents are employed to simulate the human decision making process at the cognitive level, the system level, and the resource level. An airforce conflict group decision training example is used to demonstrate the training process of using the environment.

The paper proceeds with presenting the conceptual model and the computing model of the proposed framework in Sections 2 and 3, respectively. Section 4 first introduces the training environment ACTOR, then presents the training process and example. Section 5 presents the related work and discussion. Section 6 summarises the work.

## 2. Conceptual model

## 2.1. CognitiÕe cycle for conflict group decision

Cognitive behaviours play an important role in conflict group decision process. In order to make a proper decision, decision makers need to know the current conflict situation. The original feedback from the conflict environment usually contains incomplete, incorrect, and large amount of information. Decision makers would get lost in the large amount of information or be misled by incorrect information. Thus, correct understanding of the feedback information is the key to make a proper decision. Such an understanding is a kind of cognitive processing behaviour with an input flow and an output flow.

If we regard behaviours in a decision process as nodes, and nodes are connected by flows, then conflict group decision process can be described as a cycle called cognitive cycle as shown in Fig. 1.Ž . The directed arcs in the cycle represent the flows with the following types: 1 feedback informationŽ . flow type, which can be further divided into two parts: the crude feedback type and the structured feedback type; 2 cognitive feedback flow type; andŽ . Ž . 3 decision flow type. After making the first decision, the flow type is changed continuously until a terminal condition is satisfied. Nodes in the cycle are behaviours that transform the flows from the input type into the output type. The node ‘‘information collection and processing’’ refers to the behaviours that collect information from the dynamic conflict environment, and transform the flow from the crude feedback type into the structured feedback type. The node ‘‘cognitive processing’’ refers to the behaviours for understanding, analysing and synthesising of the feedback information, and transforming the flow from the structured feedback type into the cognitive feedback flow type. Assistants e.g., staffŽ officers in military application can be employed to. pre-process the large amount of feedback information professionally and provide decision makers with the most useful and necessary information with their understanding. The node ‘‘cognitive co-operation’’ refers to the behaviours that generate a decision by using the cognitive abilities of all the group members. The behaviours of the node transform the flow from the cognitive feedback flow type into the decision flow type. Cognitive co-operation is called cognitive synthesis if the decision group has only one decision maker. The node ‘‘Decision implementation’’ refers to the behaviours for operating resources Ž . e.g., weapon operations in warfare according to the current decision and changing the conflict situation. The behaviours of the node transform the flow from the decision flow type into the crude feedback type.

![](/api/attachments/GDYFJ36K/fulltext/images/64e86bdd6bb81a2155902b0c51b52eb7e254c43a79c0554ac861d42214c76180.jpg)  
Fig. 1. Cognitive cycle for conflict group decision.

The cognitive cycle conceptually describes the conflict decision process for a conflict participating group. The cycle shows that conflict decision making is a process of continuously changing the type of flows. Hence, the enhancement of decision ability can be realised through improving the behaviours of every node of the cycle.

## 2.2. Multi-space behaÕiour co-ordination for conflict group decision

Nodes and arcs of the cognitive cycle constitute a conflict decision space. Behaviours of a node in the cycle concern a part of the space. In order to better analyse the relationship among these behaviours, we separate the conflict decision space into four parts: a cognitive space, a method space, an information space, and a resource space, which are levelled top-down as shown in Fig. 2.

The cognitive space is defined by a cognitive carrier and cognitive behaviours such as cognitive processing and cognitive co-operation. The cognitive space of a decision group is the summarisation of all the member individual cognitive spaces. Methods Žincluding problem-solving models and reasoning methods and method operation behaviours consti-. tute the method space. Information and information operation behaviours constitute the information space. The information operation behaviours include managing information, collecting the feedback information from the resource space, processing information, and supplying useful information to the method space or directly to the cognitive space. Resource Ž . e.g., weapons in warfare and resource operations constitute the resource space. Conflict causes the change of each group’s resources occupation. In some applications e.g., warfare , a group’s resourcesŽ . tend to decrease during conflict if its recovery orŽ reinforcement rate is lower than its loss rate..

![](/api/attachments/GDYFJ36K/fulltext/images/73d5015aec61fc961813798ad20093339ed54843e9e4effa13ad37dcf5684607.jpg)  
Fig. 2. Multi-space behaviours and conflicts.

The high-level behaviours are supported by the low-level behaviours as shown in Fig. 2. Cognitive behaviours at the top level are supported by methods in the method space. The behaviours in the method space are supported by the information operation behaviours. Information in the information space is collected from the resource space at the bottom level. Decisions are generated in the cognitive space, and finally implemented in the resource space.

Conflict exists in all these levels. At the top level, a decision group can use any strategies e.g., decep- Ž tion to reach a target under conflict restraint. Each. group can operate the required methods to support its decision behaviours. At the method space level, different methods support different decision making behaviour. Conflict exists between two groups’ behaviours at the information space level e.g., elec-Ž tronic interference, camouflage, and information deception in warfare . Conflict also exists between two. groups’ behaviours at the resource space level. The amount, function, and efficacy of resources are the important factors in making decisions. For example, the resources of airforce include fighters, pilots, airports, radar, and oil supplies. They constitute the airforce strength conflict. These conflicts are described as the marked two-way arrows in Fig. 2.

A decision making process concerns the coordination among behaviours in these spaces. Such a co-ordination is to arrange the order of related behaviours. We herein suggest a directed diagram to describe the priority order among the related behaviours in a decision process as shown in Fig. 3. A decision group’s behaviours can be divided into six sequential stages, denoted as $< \mathrm { s } _ { 1 } , \ \mathrm { s } _ { 2 } , \ \mathrm { s } _ { 3 } , \ \mathrm { s } _ { 4 } , \ \mathrm { s } _ { 5 }$ ${ \bf s } _ { 6 } >$ . The arrow ‘‘<sup>ª</sup> ’’ represents the priority order between two behaviours. For example, ‘Information processing <sup>ª</sup> Cognitive processing’ means that the information processing should be carried out before the cognitive processing. The two-way arrow ‘‘<sup>¤ª</sup>’’ represents the inter-operation between two behaviours in two different spaces. For example, ‘Cognitive co-operation Method operations means that the cognitive co-operation needs the support of method operations, and the method opera tions need the support of cognitive co-operation.

![](/api/attachments/GDYFJ36K/fulltext/images/20d5da3505467edde98e992f3eb1e587b37e0e5041e69095e634ad31b266d4f2.jpg)  
Fig. 3. Co-ordination among behaviours in conflict group decision process.

## 2.3. Conflict group decision training

Conflict group decision training participants include an instructor and two conflict groups with their supported systems. Each group practices training courses pre-designed by the instructor. Conflict group decision training is to design an inter-operation process to improve the ability of flow processing in a cognitive cycle and to enhance the ability of behaviour co-ordination across multiple spaces through training courses. The instructor can also be regarded as a decision maker or a decision group who makes Ž . decisions for designing training courses, selecting a suitable course from a set of pre-design courses, determining random stage conflict results with the help of models, controlling the training process, and evaluating each group’s decision after the termination of a training process.

Conflict group decision training can be conceptually modelled by three cognitive cycles as shown in Fig. 4. $\mathrm { C M } _ { \mathrm { I } }$ denotes the cognitive mechanism of the instructor. $\mathrm { I F } _ { \mathrm { I } } , \ \mathrm { I F } _ { \mathrm { A } }$ , and $\mathrm { { I F } _ { B } }$ denote the information flow fed back by the instructor, group A and group B, respectively. $\mathrm { C F } _ { \mathrm { I } } , \mathrm { C F } _ { \mathrm { A } } ,$ , and $\mathrm { C F _ { B } }$ denote the cognitive flows generated by the instructor, group A and group B, respectively. $D _ { \mathrm { I } } , ~ D _ { \mathrm { A } }$ , and $D _ { \mathrm { { B } } }$ denote the decision flows made by the instructor, group A and B, respectively. Behaviour nodes of these cognitive cycles change the type of flows. A training process begins with an instructor’s trigger order. The flow moves from one node to another node continuously during the training period. The conflict situation keeps changing, and is transformed from an initial state $\mathrm { ( S t a t e _ { I } ) }$ to a terminal state $\mathrm { ( S t a t e _ { T } ) }$ until a terminal condition is satisfied described in the thickŽ rectangle in Fig. 4 . To reach a definite training . target, the instructor can make decisions to repeatedly conduct the training process with different courses. Each training course transforms two conflict groups’ cognitive abilities including the ability ofŽ cognitive processing and cognitive co-operation. from their initial states into terminal states.

![](/api/attachments/GDYFJ36K/fulltext/images/54fde37aabbc0b7d162b3201020658c59dcfb8be3839190d38ba6600cec2c2e9.jpg)  
Fig. 4. Cognitive cycle model for conflict group decision training.

## 3. Computing model

3.1. An automata formalism for conflict group decision and training

A conflict group decision mechanism CGDMŽ . can be modelled by an automata mechanism whose input is the feedback information flow IF , and Ž . output is the decision flow Ž . D . A decision $\mathrm { \ g r o u p ^ { \prime } s }$ cognitive mechanism CM transforms the informa-Ž . tion flow into the cognitive flow CF , and makesŽ . decisions through cognitive co-operation. A new Ž  conflict situation Sit depends on the current situa-. tion Sit and the new decision. CGDM can be Ž . formally described as follows:

$$
\mathrm{CGDM} _ {k} = \left\langle \mathrm{IF} _ {k}, D _ {k}, \text { Sit }, \mathrm{CM} _ {k}, F _ {k} \right\rangle ,
$$

such that $D _ { k } = { \bf C } { \bf M } _ { k } ( { \bf C } { \bf F } _ { k } , { \bf S } \mathrm { i t } ) , { \bf C } { \bf F } _ { k } = { \bf C } { \bf M } _ { k } ( { \bf I } { \bf F } _ { k } , { \bf S } \mathrm { i t } ) ,$ and $\mathrm { S i t ^ { \prime } } = F _ { k } ( D _ { k } , \mathrm { { \ S i t } } ) . \ k \in \{ \mathrm { I }$ 4 , A, B identifies the three training participants: the instructor, group $\mathbf { A } ,$ and group B. $\mathrm { C M } _ { k }$ is a case-behaviour set, and $F _ { k }$ is a set of state transformation functions. Generally, $\mathrm { C M } _ { k }$ depends on the cognitive behaviours, the evaluation of conflict situation, and conflict restraints. $F _ { k }$ can be determined by rules, models, and human preference under conflict restraints.

A decision training mechanism DTM consists ofŽ . two conflict groups’ decision mechanisms $( \mathrm { C G D M _ { A } }$ and $\mathbf { C G D M _ { B } } )$ and the instructor’s decision making mechanism $( \mathrm { C G D M _ { I } ) }$ . The three participants’ decisions transform the current situation into a new situation. The input flow of the instructor IF con-Ž .

sists of two groups’ decisions and the current situation. DTM can be formally described as follows:

$$
\mathrm{DTM} = \left\langle \mathrm{CGDM} _ {\mathrm{A}}, \mathrm{CGDM} _ {\mathrm{B}}, \mathrm{CGDM} _ {\mathrm{I}} \right\rangle ,
$$

such that $\mathrm { C G D M } _ { k } = < \mathrm { I F } _ { k } , D _ { k } , \mathrm { S i t } , \mathrm { C M } _ { k } , F _ { k } >$ $( k \in \{ \mathrm { I } , ~ \mathrm { A } , ~ \mathrm { B } \} )$ $\mathrm { S i t ^ { \prime } } = F ( ( D _ { \mathrm { I } } , \ D _ { \mathrm { A } } , \ D _ { \mathrm { B } } ) _ { \mathrm { } }$ . , Sit , and $\mathrm { I F _ { I } } = \left( { \cal D } _ { \mathrm { A } } , \ { \cal D } _ { \mathrm { B } } , { \mathrm { S i t } } \right)$

## 3.2. CognitiÕe co-operation

Cognitive co-operation is an important cognitive behaviour of a decision group. A group member has individual beliefs, experiences, and preferences, which support the individual contribution to the final group decision. Cognitive co-operation enables a decision group to establish a common communication language for group decision. For example, a decision maker can know the other member decision makers’ specialisation, and the decision group can unify decision principles and criteria. Discussion is a common form of cognitive co-operation. Blackboard mechanism is usually used as the discussion carrier.

A discussion mechanism with a 3D-blackboard is suggested as shown in Fig. 5. A decision group can be geographically distributed and co-operated work on an intranet. Group members denoted as DM are Ž . weighted in terms of their grades and positions. A discussion organiser can be an agent organises theŽ . discussion with the support of the 3D-blackboard. The 3D-blackboard improves the conventional blackboard in two aspects. Firstly, it can record the historical discussions on old topics. Secondly, it can record the process of forming a decision. The 3D-blackboard has two pointers: ${ \tt p } _ { 1 }$ and ${ \sf p } _ { 2 } . { \sf p } _ { 1 }$ controls the discussion process bottom-up. ${ \tt p } _ { 2 }$ controls a new discussion starting on a new version. Old version discussion can help decision makers to make quick decisions through establishing an analogy between a related old topic and the new topic 23 .<sup>w</sup> <sup>x</sup>

![](/api/attachments/GDYFJ36K/fulltext/images/7a4e1c16ccaa9a798bc91eebe8a1f779c87a4e6f3da5c767d7973b789d9ba6bc.jpg)  
Fig. 5. A discussion mechanism with 3D-blackboard.

![](/api/attachments/GDYFJ36K/fulltext/images/45d53ba095e2031d09136008889aac4c4bcf84da58165261ed3dfbc7e30e8380.jpg)  
Fig. 6. A simulation-based voting mechanism.

A decision is formed through the following four steps:

1. Contribution. Every member decision maker Ž . DM contributes a decision suggestion with reasons, and can feedback the other members’ decision suggestions from the blackboard, then can revise his<sup>r</sup>her own decision if necessary;

2. Classification. All the decision suggestions are classified into several categories;

3. Form a candidate decision. Every member decision maker votes to select a candidate decision;

4. Modification. A final decision is formed through incorporating group members’ opinions into the candidate decision.

Voting is a way to synthesise a final decision from several group members’ decisions. A simulation-based voting mechanism is suggested as shown in Fig. 6. The group cognitive space is constituted by all the decision participants’ cognitive spaces. To make foreseeable decisions, every member decision maker DM can pre-vote first the dashed lines inŽ . Ž Fig. 6 . The feedback simulation mechanism changes. the current situation when the pre-vote decisions input. The feedback simulation is supported by the method space. Through analysing the cognitive feedback, decision makers decide whether their voting need to be adjusted or not before a formal voting. Finally, the candidate decision is formed through the formal voting.

## 3.3. Situation eÕaluation: strength index and psychological line

The current conflict situation is an important factor in forming a decision. Conflict situation mainly concerns two aspects: 1 the comparison between Ž . the degrees of reaching two groups’ targets; and 2Ž . the comparison between two conflict $\mathrm { \ g r o u p s ^ { \prime } }$ strengths. Factors causing the increase or decrease of the strength can be regarded as a kind of strength $\left( \mathrm { e . g . } \right.$ , the occupation of important energy can be regarded as a kind of strength in warfare . We first. assume that $\mathrm { g r o u p } _ { k } { \mathsf { \bar { s } } }$ general strength can be evaluated at any time t in the conflict process by an evaluation function $E ( G _ { k } ( t ) )$ $k \in \{ \mathrm { A }$ 4 , B and $E ( G _ { k } ( t ) ) \geq 0$ . Two conflict groups’ strength can be then clearly compared at any point on the time axis as shown in Fig. 7. The framework suggests a strength index to reflect such a comparison. A strength index is computed in a converse way by two conflict groups.

From the standpoint of group A, the strength index of group A at time t is computed by Index $_ \mathrm { A } ( t )$ $= E ( G _ { \mathrm { A } } ( t ) ) - E ( G _ { \mathrm { B } } ( t ) )$ . Index $_ \mathrm { A } ( t ) > 0$ means that $\mathrm { \ g r o u p _ { A } \vec { \cdot } : }$ s strength is stronger than $\mathrm { \ g r o u p _ { B } \mathrm { ^ { \circ } s } }$ strength at time t. Index $_ \mathrm { A } ( t ) < 0$ means that $\mathrm { \ g r o u p _ { A } \mathrm { ^ { \cdot } s } }$ strength is weaker than $\mathrm { \ g r o u p _ { B } \mathrm { ^ { \circ } s } }$ strength at time t. Index $_ \mathrm { A } ( t )$ $= 0$ means that $\mathrm { \ g r o u p _ { A } \cdot _ { s } }$ strength is equal to $\mathrm { \ g r o u p _ { B } \mathrm { ^ { \circ } s } }$ strength at time t. For group A, $E ( G _ { \mathrm { A } } ( t ) )$ can be computed on the basis of objective information feedback, while the computing of $E ( G _ { \mathrm { B } } ( t ) )$ depends on the cognitive processing of the feedback information about group B.

![](/api/attachments/GDYFJ36K/fulltext/images/d661e896c395dead9f62b256448efd0dc1d7651d50827d06bc141098f38a255d.jpg)  
Fig. 7. Strength index curve and psychological line.

From the standpoint of group B, the strength index of group B at time t is computed by Index ${ \bf \pi } _ { \mathrm { B } } ( t )$ $= E ( G _ { \mathrm { B } } ( t ) ) - E ( G _ { \mathrm { A } } ( t ) )$ . Index $_ \mathrm { B } ( t ) > 0$ means that $\mathrm { \ g r o u p _ { B } \mathrm { ^ { \circ } s } }$ strength is stronger than $\mathrm { \ g r o u p _ { A } \mathrm { ^ { \cdot } s } }$ strength at time t. Index $\mathbf { \Sigma } _ { \mathrm { B } } ( t ) < 0$ means that $\mathrm { \ g r o u p _ { B } \mathrm { ^ { \circ } s } }$ strength is weaker than $\mathrm { \ g r o u p _ { A } \mathrm { ^ { \circ } s } }$ strength at time t. Index ${ \bf \pi } _ { \mathrm { B } } ( t )$ $= 0$ means that $\mathrm { \ g r o u p _ { B } \mathrm { ^ { \circ } s } }$ strength is equal to $\mathrm { \ g r o u p _ { A } \mathrm { ^ { \cdot } s } }$ strength at time t. For group B, $E ( G _ { \mathrm { B } } ( t ) )$ can be computed on the basis of the objective information feedback, while the computing of $E ( G _ { \mathrm { A } } ( t ) )$ depends on the cognitive processing of the feedback information about group A.

The strength evaluation for a group mainly concerns the state of its resource $( r )$ , which is usually a set of complex objects with hierarchical structures. $\mathrm { G r o u p } _ { \mathrm { k } } ^ { \ \cdot } \mathrm { s }$ general strength at time t can be computed by the following function:

$$
\begin{array}{l} E \big (G _ {k} (t) \big) = \sum_ {r _ {\mathrm{i}} (t) \in G _ {k} (t)} w _ {\mathrm{i}} \times E \big (r _ {\mathrm{i}} (t) \big), \\ \text { where } w _ {\mathrm{i}} \in \boldsymbol {W}, \text { and } k \in \{\mathrm{A,B} \}. \end{array}
$$

The assessment of $E ( r _ { \mathrm { i } } ( t ) )$ concerns a domainspecific indicator set and a related weight vector W. W can be determined by using the AHP AnalyticŽ Hierarchy Process approach 17 . When using the. <sup>w</sup> <sup>x</sup> AHP approach, only the resource satisfying the match relationship should be taken into account, for example, the number of fighters should match the number of pilots in the airforce conflict. The comparison between the two groups’ strength change can be reflected by $( E ( G _ { \mathrm { A } } ( t ) ) / E ( G _ { \mathrm { A } } ( 0 ) ) ) / ( E ( G _ { \mathrm { B } } ( t ) ) /$ $E ( G _ { \mathrm { B } } ( 0 ) ) )$

The degree of reaching $\mathrm { g r o u p } _ { k } { \mathsf { \bar { s } } }$ target at time t Ždenoted as $\mathrm { D I T } _ { k } ( t ) , \ k \in \{ \mathrm { A } , \ \mathrm { B } \} )$ can be computed by:

DI $\boldsymbol { \mathrm { T } } _ { k } ( t ) =$ the number of the reached sub-targets at time t<sup>r</sup>total number of sub-targets, which satisfies $\mathrm { D I T } _ { k } ( t ) \in [ 0 , \ 1 ]$ and $\mathrm { D I T } _ { k } ( 0 ) = 0 .$ . If $\mathrm { \ g r o u p _ { A } \mathrm { ^ { \cdot } s } }$ target contradicts $\mathrm { \ g r o u p _ { B } \mathrm { ^ { \circ } s } }$ target, then we have: $\mathrm { D I T } _ { \mathrm { A } } ( t ) +$ $\mathrm { D I T } _ { \mathrm { B } } ( t ) = 1$ . The comparison between the degrees of reaching the two group’s targets can be reflected by $\mathrm { D I T _ { A } } ( t ) / \mathrm { D I T _ { B } } ( t )$

$\mathrm { S i t _ { A / B } } ( t )$ and $\mathrm { S i t _ { B / A } } ( t )$ are used to denote the current situation from the standpoint of groups A and

B, respectively. They can be computed by the following two formulas:

$$
\begin{array}{r l} \operatorname{Sit} _ {\mathrm{A} / \mathrm{B}} (t) & = \big (E \big (G _ {\mathrm{A}} (t) \big) / E \big (G _ {\mathrm{A}} (0) \big) + \operatorname{DIT} _ {\mathrm{A}} (t) \big) \\ & / \big (E \big (G _ {\mathrm{B}} (t) \big) / E \big (G _ {\mathrm{B}} (0) \big) + \operatorname{DIT} _ {\mathrm{B}} (t) \big), \\ & \text { and } \\ \operatorname{Sit} _ {\mathrm{B} / \mathrm{A}} (t) & = \big (E \big (G _ {\mathrm{B}} (t) \big) / E \big (G _ {\mathrm{B}} (0) \big) + \operatorname{DIT} _ {\mathrm{B}} (t) \big) \\ & / \big (E \big (G _ {\mathrm{A}} (t) \big) / E \big (G _ {\mathrm{A}} (0) \big) + \operatorname{DIT} _ {\mathrm{A}} (t) \big). \end{array}
$$

Since $\begin{array} { r } { \mathrm { D I T } _ { k } ( t ) \in [ 0 , 1 ] , \ E ( G _ { k } ( t ) ) / E ( G _ { k } ( 0 ) ) \in [ 0 , 1 ] . } \end{array}$ and $\mathrm { D I T } _ { \mathrm { A } } ( t ) + \mathrm { D I T } _ { \mathrm { B } } ( t ) = 1$ , we have $\mathrm { S i t _ { A / B } } ( t ) .$ $\mathrm { S i t _ { B / A } } ( t ) \in [ 0 , + \infty ] . \ \mathrm { S i t _ { A / B } } ( t ) = 1$ means that the conflict is in a balance situation. $\mathrm { S i t _ { A / B } } ( t ) < 1$ or $\mathrm { S i t _ { B / A } } ( t ) > 1$ means that the current situation is advantageous to group B. $\mathrm { S i t _ { A / B } } ( t ) > 1$ or $\mathrm { S i t _ { B / A } } ( t ) <$ 1 means that the current situation is advantageous to group A.

To reflect the general psychological endurance capacity for each group during conflict, a psychological line is suggested for each group. $\mathrm { P L } _ { \mathrm { A } } ( t )$ and $\mathrm { P L } _ { \mathrm { B } } ( t )$ denote the psychological lines for groups A and B at time t, respectively, as shown in Fig. 7. If index $\mathbf { \rho } _ { \mathrm { A } } ( t )$ is above $\mathrm { P L } _ { \mathrm { A } } ( t )$ Ž i.e., $\mathrm { \ g r o u p _ { A } \mathrm { ^ { \cdot } s } }$ strength is much stronger than $\mathrm { \ g r o u p _ { B } \mathrm { ^ { \circ } s } }$ strength , then group B. is facing a serious situation and enduring a big psychological pressure. For example, such a pressure can cause group B to surrender in warfare. If index $_ \mathrm { \cdot } _ { \mathrm { A } } ( t )$ is below $\mathrm { P L } _ { \mathrm { B } } \left( t \right) \left( \mathrm { i . e . , \ g r o u p _ { A } \mathrm { ^ { \circ } s } } \right.$ strength is much weaker than $\mathrm { \ g r o u p _ { B } \mathrm { ^ { \circ } s } }$ strength , then group A. is facing a serious situation and enduring a big psychological pressure. For example, such a pressure can cause group A to surrender in warfare. $\mathrm { P L } _ { \mathrm { A } } ( t )$ and $\mathrm { P L } _ { \mathrm { B } } ( t )$ can be computed by the following two formulas:

$$
\begin{array}{c} \mathrm{PL} _ {\mathrm{A}} (t) = \alpha \times \big (t / t _ {\mathrm{T}} \big) \times \mathrm{DIT} _ {\mathrm{A}} (t) \times E \big (G _ {\mathrm{A}} (t) \big) \\ / E \big (G _ {\mathrm{A}} (0) \big), \text { and } \\ \mathrm{PL} _ {\mathrm{B}} (t) = \alpha \times \big (t / t _ {\mathrm{T}} \big) \times \mathrm{DIT} _ {\mathrm{B}} (t) \times E \big (G _ {\mathrm{B}} (t) \big) \\ / E \big (G _ {\mathrm{B}} (0) \big), \end{array}
$$

where $t _ { \mathrm { T } }$ denotes the pre-determined or estimatedŽ . conflict period,  is used for keeping $\mathrm { P L } _ { \mathrm { A } } ( t )$ and $\mathrm { P L } _ { \mathrm { B } } ( t )$ within the measure of the index axis.

## 3.4. Restraints and rules

A restraint set of the framework reflects domain characteristics. Restraints concern such factors as the time stress, the beneficial principle, the least cost principle, and the efficacy of resource 11,24 . Group <sup>w</sup> <sup>x</sup> decisions are made under these restraints. A factor is usually determined by a set of sub-factors. All these factors constitute a factor tree, in which leafs are domain-dependent factors. For example, the efficacy of resource is determined by geographical conditions and weather conditions in warfare. The restraint factor set is denoted as $\mathrm { R E S } = \{ \mathrm { F a c t o r } _ { i } \mid i \in$ $\{ 1 , \ldots , n \} \}$ , where Factor <sup>s</sup>ŽFactorName, Type, ValueRange, ValidTimeRange ..

A set of control rules denoted as C-RULES canŽ . be used for assisting the instructor to control the training process. For example, if one of the two conflict groups’ strength decreases to a certain amount $( E ( G _ { k } ( t ) < \alpha )$ that could not support the conflict, then the conflict process should be terminated. If both the two groups’ strengths, then a balance situation is reached. These rules take the form of production rules. For example, the following three rules in C-RULES are used for the termination control of conflict training process.

<sup>Ø</sup> Rule0201: IF $E ( G _ { \mathrm { A } } ( t ) ) \leq \alpha ~ \mathrm { O R } ~ E ( G _ { \mathrm { B } } ( t ) ) \leq \alpha$ THEN Suggest termination; <sub>–</sub>

<sup>Ø</sup> Rule0202: IF $\mathrm { S i t _ { A / B } } ( t ) = 1$ AND $E ( G _ { \mathrm { A } } ( t ) ) \leq \alpha$ AND $E ( G _ { \mathrm { B } } ( t ) ) \leq \alpha$ , THEN Report balance <sub>– –</sub> situation AND Suggest termination;<sub>–</sub>

<sup>Ø</sup> Rule0203: IF A GiveUp OR B GiveUp, THEN <sub>– –</sub> Suggest termination. <sub>–</sub>

New restraints and control rules can be appended to RES and C-RULE, respectively, according to application domain requirement.

## 4. Agent-based conflict decision training environment ACTOR

## 4.1. Architecture

The architecture of a conflict decision training environment ACTOR is described as shown in Fig. 8. It simulates the conflict group decision environment at three levels: the cognitive level, the system level, and the resource level. The cognitive level of a conflict group includes: a human decision group, a cognitive co-operation mechanism e.g., the sug-Ž gested discussion mechanism , and an intelligent. agent group. Each agent has its responsibilities, tasks, and preferences. The structure of an agent consists of a window interface for conversation, a case-based reasoning mechanism, a set of case-action rules, and a task-oriented program. The decision agent group is organised like the human decision group. The human group and the agent group are trained simultaneously. The role of the decision agent group concerns two aspects: 1 to help new participants to get Ž . familiar with the training process through demonstrating the agents’ decision and the training process; and 2 to simulate the group decision training envi-Ž . ronment for a single decision maker, i.e., a human decision maker can be trained in a group decision environment through co-operating with the agents. Multiple training paradigms such as problem-based training, process-based training, and experience accumulation can be used to improve the behaviours of both the human group and the agent group.

![](/api/attachments/GDYFJ36K/fulltext/images/8b912bbe660657667a069dcd7285655e54ea73f87286c39ad001d7866b5a525f.jpg)  
Fig. 8. A conflict decision training environment ACTOR.

The system level facilitates the method space and the information space. The system consists of a group of agents and a decision support base DSB .Ž . The system behaviours are realised through the cooperation among these agents. Agents’ behaviours are supported by the DSB. The scheduling agent is responsible for receiving task information, planning the task, dispatching sub-tasks to the other agents, and managing the DSB. The modelling agent is responsible for model-based decisions. The reasoning agent is responsible for rule-based decisions. The analysis agent is responsible for collecting information from the resource level and providing necessary information to decision makers and the agents at the cognitive level. A new agent can be created through first inheriting from an agent frame and the common rules, then append individual knowledge, preference, and task-oriented program to it.

The DSB consists of an implementation level and a specification level. The implementation level consists of five separated bases: a model base, a rule base, a plan base, and an information base. The model base manages the algorithms for solving mathematical problems in decision process. The rule base manages the rules for reasoning, decision, evaluation, adjustment, and plan selection. Each rule takes the form ‘RuleID: IF conditionŽ .t THEN actionŽ .t <sup>w</sup>WHERE restrictionŽ .t <sup>x</sup>’, for example, Rule0010: IF DIT Ž .t <sup>s</sup>1 THEN A wins WHERE<sub>–</sub> $0 \leq t \leq 1 0$ . Rules in the base are classified into categories in terms of its application classification. The plan base consists of pre-made plan templates for assisting quick decisions in complex situation. Each template is a series of decision steps with parameters. The information base manages the feedback situation information, the temporal results of reasoning, and the temporal results of conflict. DSB can be described at an abstract specification level: DSB<sup>s-</sup>S, T<sup>)</sup>, for any $s \in S , \ s = < f _ { i } \colon \sigma _ { i } \to \tau _ { i } \mid i$ <sup>s</sup> 1, . . . , n <sup>)</sup> , where $\sigma _ { i }$ and $\tau _ { i }$ can be either basictypes or constructed-types.  can be a Cartesian product as $\sigma _ { 1 } \times \ldots \times \sigma _ { n }$ . T is a mapping from S into a type set  4 ModelType, RuleType, DataType , and satisfies the following three rules:

1. IF T sŽ . <sup>s</sup> ModelType, THEN s describes the signature of a model base, WHERE $\sigma _ { i }$ and $\tau _ { i }$ represent the input type and the output type, respectively;

2. IF $T ( s ) = R u l e T y p e$ , THEN s describes a rule base, WHERE f : $\sigma _ { i } \to \tau _ { i }$ represents a rule with the precondition type $\sigma _ { i }$ and the action type $\tau _ { i } ;$

3. IF $T ( s ) = D a t a T y p e ,$ , THEN s describes a data base, WHERE $f _ { i } \colon \sigma _ { i }  \tau _ { i }$ represents the functional dependence relationship, and the data type $\sigma _ { i }$ functionally depends on the data type $\tau _ { i } .$

At the resource level, the conflict environment simulation agent denoted asŽ $\mathbf { S } _ { - } \mathbf { A g e n t } )$ simulates the conflict environment of the application field, and appends the current conflict information to the DSB. The S Agent co-operates with the modelling agent <sub>–</sub> Že.g., for computing the resource damage in a warfare , the reasoning agent, and the analysis agent. during a training process. The S Agent also man- <sub>–</sub> ages the time advancement of the training environment. The adaptability of the training environment ACTOR can be increased by adjusting the function of the S Agent.<sub>–</sub>

## 4.2. Training process and example

The instructor controls the training process by the following four steps:

1. Initialisation. Determine the training purpose, the organisation of each group, the restraint set, and initial conditions including the initial situation,Ž the terminal conditions, and the two groups’ targets ;.

2. Determine stage result. Select the stage conflict result from several optional results in terms of the training purpose and the restraint with the help of the modelling agents;

3. Termination control. Control the termination of the decision training process with the help of control rules;

4. Evaluation. Evaluate each group in terms of their targets and decision records. Each record consists of a situation and the corresponding decision.

## 4.2.1. Example

This example demonstrates the decision training process by a simple airforce conflict training course. The course has the following four assumptions:

1. Initialisation. Two conflict groups, $\mathrm { G _ { A } }$ and $\mathrm { G } _ { \mathrm { B } } .$ have four resources: fighters, oil supplies, airports, and Radar their initial states are shown as Ž the rows satisfying t <sup>s</sup> 0 in Table 1 , which are . distributed on a visual map.

Table 1  
Resource states during a conflict training course period

<table><tr><td>t</td><td>Group</td><td>Fighter</td><td>Radar</td><td>Airport</td><td>Oil</td></tr><tr><td></td><td>A/B</td><td> $w_1$ , num</td><td> $w_2$ , num</td><td> $w_3$ , num</td><td> $w_4$ , ton</td></tr><tr><td rowspan="2">0</td><td>A</td><td>0.30, 30</td><td>0.30, 10</td><td>0.20, 3</td><td>0.20, 400</td></tr><tr><td>B</td><td>0.30, 20</td><td>0.30, 10</td><td>0.20, 2</td><td>0.20, 300</td></tr><tr><td rowspan="2">1</td><td>A</td><td>0.35, 21</td><td>0.20, 10</td><td>0.20, 3</td><td>0.25, 330</td></tr><tr><td>B</td><td>0.35, 10</td><td>0.20, 06</td><td>0.20, 2</td><td>0.25, 250</td></tr><tr><td rowspan="2">2</td><td>A</td><td>0.40, 18</td><td>0.15, 10</td><td>0.15, 3</td><td>0.30, 250</td></tr><tr><td>B</td><td>0.40, 01</td><td>0.15, 03</td><td>0.15, 2</td><td>0.30, 200</td></tr></table>

2. Targets. ‘‘Targe $_ \mathrm { A } \dot { \cdot }$ destroy the strength of $\mathrm { G _ { B } } ^ { \prime }$ and $\ddot { \cdot } \mathrm { { ^ { * } t a r g e t _ { B } } \mathrm { { : } } }$ destroy the strength of $\mathrm { G _ { A } } ^ { \prime }$

3. Additional restraints. The same type of resource has the same function, and the reinforcement rate of every resource is zero during conflict.

4. Terminal condition. The training process terminates if one of the following conditions is satisfied: Fighter number <sub>–</sub> $\leq 1$ <sub>–</sub>, Radar number <sup>s</sup> 0, Airport number<sub>– –</sub><sup>s</sup>0, or Oilamount <sup>F</sup>50.

The following steps show $\mathrm { \ g r o u p _ { A } } ^ { \prime }$ s continue behaviour process during the training period:

Ž . 1 Cognitive co-operation and decision. In terms of the target and the initial situation including theŽ states and distribution of two conflict groups’ resources , the first decision is made: ‘‘to attack. group ’s Radar’’ through the discussion mechanism. <sub>B</sub>

Ž . 2 Planning. With the help of the support system, the plan of the first decision is made: ‘‘20 fighters perform the attack task, 10 fighters are reserves.’’.

Ž . 3 Performance and feedback. This step includes such behaviours as information collection, information processing, and cognitive processing. Information feedback: ‘‘12 of the opponent’s fighters are now invading.’’ Cognitive feedback: ‘‘group ’s aim is to attack $\mathrm { \ g r o u p _ { A } \mathrm { ^ { \circ } s } }$ reserves and airport, the number of invading fighters is superior to the number of group $) _ { \mathrm { A } } \mathbf { \dot { s } }$ reserves.’’

Ž . 4 Cognitive co-operation and plan adjustment. Two possible adjustments are suggested by the support system: a order all the fighters sent out toŽ . return to intercept the invading fighters co-operating with the reserves; and b order some of the fightersŽ . sent out to continue to perform the attack task and some of them to return to intercept the invading fighters co-operating with the reserves. The reasoning agent presents the advantages and disadvantages Ž . factors of the two suggestions. The analysis agent summarises these factors, and presents it to the decision group. Through cognitive co-operation dis-Ž cussion and voting , the suggestion b is selected.. Ž . Thus, the original plan is adjusted to the current plan: ‘‘12 fighters continue to perform the attack task, the other eight fighters return to co-operate with the reserves for intercepting the invading fighters.’’

Ž . 5 Decision performance and feedback. The environment simulation agent generates the possible stage conflict results with the support of the rule base and the model base in DSB. The information feedback is shown as the rows satisfying t <sup>s</sup> 1 in Table 1. The analysis agent evaluates the current situation with the help of the strength index curve and the psychological line.

Ž . 6 Cognitive co-operation, decision and planning. Through cognitive co-operation, decision makers make the second decision: ‘‘order six fighters to attack grou ${ \vec { \mathsf { p } } } _ { \mathrm { B } } { \mathsf { \dot { s } } }$ Radar, and leave 15 fighters as reserves.’’

Ž . 7 Decision performance and feedback. Information feedback: ‘‘six opponent’s fighters are intercepting the fighters sent out to attack $\mathrm { \ g r o u p _ { B } \mathrm { ^ { \circ } s } }$ Radar.’’ Cognitive feedback: ‘‘four of the opponent’s fighters stay at the airport.’’

Ž . 8 Cognitive co-operation and adjustment. Through cognitive co-operation and adjustment, the third decision is made: ‘‘order 10 of the reserves to attack the airport, order two of the reserves to reinforce the fighters attacking the Radar target, and leave other the three as reserves for preventing an opponent’s attack.’’

Ž . 9 Decision performance and feedback. The feedback conflict result information is shown as the rows satisfying t<sup>s</sup>2 in Table 1. The number of the fighters of $\mathrm { G } _ { \mathrm { B } }$ becomes one.

Ž . 10 Termination and cognitive co-operation. The scheduling agent announces the termination of the training in terms of the control rules. The instructor reviews the conflict process, evaluates two group’s decisions at each step, and scores the general training result.

A new training process can be triggered after adjusting the initial assumption.

## 5. Related works and discussion

As human intelligent behaviour, decision making has the characteristics of subjective and quantitative, task-oriented, pattern-based, and non-linear internal process. The impact of the time stress on decision making performance of the command and control team is investigated 14 . A specification language<sup>w</sup> <sup>x</sup> for cognitive modelling is proposed 8 . The concepts<sup>w</sup> <sup>x</sup> of cognitive space and cognitive skills like reasoning, abstraction, and analogy are discussed 23 .

The issue of time constraint on multi-agent systems is investigated for resource allocation in command, control and communication systems 11 . For <sup>w</sup> <sup>x</sup> multi-agent co-operation, Kraus 12 points out that <sup>w</sup> <sup>x</sup> combining AI techniques with such methods as game theory, operational research, physics, and philosophy is beneficial for negotiation and co-operation in multi-agent environments. The semantics for modelling agent as a decision maker with beliefs, preferences, and decision strategies are investigated, where agent is regarded as a state machine with a set of possible local states, a set of possible actions, and a program 5 . A language KQML for multi-agents <sup>w</sup> <sup>x</sup> communication is suggested 9 .<sup>w</sup> <sup>x</sup>

The stock index reflects both the current and historical states of stock market. All the participants of a stock market can be dynamically divided into two conflict groups: a selling group and a buying group. The total amount and the price of buying or Ž selling a share form the strength of buying or. Ž selling . The index dynamically reflects the strength. comparison between the two conflict groups. If the selling group’s strength is stronger than the buying group’s strength, the index will be down. If the selling group’s strength is weaker than the buying group’s strength, the index will be up. Psychological factor plays an important role in forming selling and buying decisions. Similar to the index of the stock market, the strength index used in the presented framework dynamically reflects the strength comparison between two conflict groups. Decision makers can make decisions in terms of the change of the strength index curve and the dynamic relationship between the curve and the psychological line.

The effectiveness of the suggested discussion mechanism depends on the co-operation between the decision group and the support mechanism. The suggested architecture of the discussion mechanism is suitable for multiple kinds of group decision applications. New cognitive co-operation models can be incorporated into the proposed framework.

The architecture of the training environment AC-TOR can be used in a wide variety of conflict applications. First, the levelled architecture can isolate the domain-specific variables. Second, the behaviours of ACTOR are performed by the agents at three levels. Since each agent performs an independent task, the modification of an agent does not affect the other agents. Third, the S Agent at the<sub>–</sub> resource level simulates the conflict environment of the application domain. The other levels only concern the content of the DSB they do not directly Ž access the resource level simulation . The change of. the resource level does not affect the other levels. Fourth, domain-specific rules and models can be easily appended to the DSB for new applications.

## 6. Summary

This paper has investigated the behaviours and the process of conflict group decision, presented a cognitive-based framework for conflict group decision training, and described the implementation of a conflict group decision training environment ACTOR. The main contribution of this work concerns three aspects. First, we establish a new conflict group decision training model reflecting human cognitive behaviour and process. Decisions are made through cognitive co-operation and behaviours co-ordination among the cognitive space, the method space, the information space, and the resource space. Second, we propose a dynamic conflict situation evaluation approach based on the strength index and the psychological line. Decision makers can be intuitively informed about the dynamic conflict situation, which provides the basis for making proper decisions. Third, we propose a levelled and agent-based conflict group decision training environment that implements the proposed framework. Decision makers can be trained with the environment that supports dynamic situation, continue decision, and cognitive co-operation.

The proposed framework can be applied to those fields that can be generalised as a conflict decision problem. It also provides a new architecture for designing application decision support systems in line with human cognitive characteristics.

## Acknowledgements

The author thanks the anonymous referees for their helpful comments on the earlier version of this paper.

## References

<sup>w</sup> <sup>x</sup> 1 G.M. Adelson-Velsky, V.L. Arlazarov, M.V. Donskoy, Algorithms for Games, Springer, New York, 1988.

<sup>w</sup> <sup>x</sup> 2 K.A. Arrow, Social Choice and Individual Value, 2nd edn., Wiley, New York, 1963.

<sup>w</sup> <sup>x</sup> 3 A.B. Badiru, P.S. Pulat, M. Kang, DDM: decision support system for hierarchical dynamic decision making, Decision Support Systems 10 1993 1–18.Ž .

<sup>w</sup> <sup>x</sup> 4 G. Biswas, M. Oliff, A. Sen, An expert decision support system for production control, Decision Support Systems 4 Ž .1988 235–248.

<sup>w</sup> <sup>x</sup> 5 R.I. Brafman, M. Tennenholtz, Modelling agents as qualitative decision makers, Artificial Intelligence 94 1997 217–Ž . 268.

<sup>w</sup> <sup>x</sup> 6 T. Bui, C. Loebbecke, Supporting cognitive feedback using system dynamics: a demand model of the global system of mobilef telecommunication, Decision Support Systems 17 Ž .1996 83–98.

<sup>w</sup> <sup>x</sup> 7 A. Collinot, C.L. Pape, Adapting the behaviour of a job-shop scheduling system, Decision Support Systems 7 1991 341– Ž . 353.

<sup>w</sup> <sup>x</sup> 8 R. Cooper, J. Fox, J. Farringdon, T. Shallice, A systematic methodology for cognitive modelling, Artificial Intelligence 85 1996 3–44.Ž .

<sup>w</sup> <sup>x</sup> 9 T. Finin et al., KQML as an agent communication language, in: Proceedings of the Third International Conference on Information and Knowledge Management CIKM’94 , 1994,Ž . http:<sup>rr</sup>www.cs.umbc.edu.

<sup>w</sup> <sup>x</sup> 10 N.M. Fraser, K.W. Hipel, Conflict Analysis: Model and Resolution, Elsevier, New York, 1984.

<sup>w</sup> <sup>x</sup> 11 S. Kraus, J. Wilkenfeld, G. Zlotkin, Multiagent negotiation under time constraints, Artificial Intelligence 75 1995 297–Ž . 345.

<sup>w</sup> <sup>x</sup> 12 S. Kraus, Negotiation and cooperation in multi-agent environments, Artificial Intelligence 94 1997 79–97.Ž .

<sup>w</sup> <sup>x</sup> 13 D. Koller, A. Pfeffer, Representations and solutions for game-theoretic problems, Artificial Intelligence 94 1997 Ž . 167–215.

<sup>w</sup> <sup>x</sup> 14 P. Lehner et al., Cognitive biases and time stress in team

decision making, IEEE Trans. Syst., Man, Cybern. 27 5Ž . Ž . 1997 698–703, September.

<sup>w</sup> <sup>x</sup> 15 R.B. Myerson, Game Theory: Analysis of Conflict, Harvard University Press, 1991.

<sup>w</sup> <sup>x</sup> 16 S. Piramuthu, N. Raman, M.J. Shaw, Integration of simulation modelling and inductive learning in an adaptive decision support system, Decision Support Systems 9 1993 127–142.Ž .

<sup>w</sup> <sup>x</sup> 17 T.L. Saaty, The Analysis Hierarchy Process, McGraw-Hill, New York, 1980.

<sup>w</sup> <sup>x</sup> 18 K. Sengupta, T.K. Abdel-Hamid, Alternative conceptions of feedback in dynamic decision environments: an experimenta investigation, Management Science 39 4 1993 411–428,Ž . Ž . April.

<sup>w</sup> <sup>x</sup> 19 K. Sengupta, D. Te’eni, Cognitive feedback in GDSS: improving control and convergence, MIS Quarterly 1993 87–Ž . 109, March.

<sup>w</sup> <sup>x</sup> 20 J.D. Sterman, Modelling managerial behaviour: misperceptions of feedback in a dynamic decision making experiment, Management Science 35 3 1989 321–339, March.Ž . Ž .

<sup>w</sup> <sup>x</sup> 21 H. Tsubone, H. Matsuura, K. Kimura, Decision support system for production planning-concept and prototype, Decision Support Systems 13 1995 207–215.Ž .

<sup>w</sup> <sup>x</sup> 22 R. Vetschera, Integrating database and preference evaluations in group decision support: a feedback-oriented approach, Decision Support Systems 7 1991 67–77. Ž .

<sup>w</sup> <sup>x</sup> 23 H. Zhuge et al., Abstraction and analogy in cognitive space: a software process model, Information and Software Technology 39 7 1997 463–468.Ž . Ž .

<sup>w</sup> <sup>x</sup> 24 H. Zhuge, Conflict group decision training: model and system, Knowledge-Based Systems 11 3–4 1998 191–196.Ž . Ž .

![](/api/attachments/GDYFJ36K/fulltext/images/bdef8a1c58c7bff8517479ce605f46a1604ea0a24b3d956b9ce6bc10572f3441.jpg)

Hai Zhuge received the Ph.D. in Computer Science from Zhejiang University, China, in 1992. He was a post-doctoral research fellow 1992–1994 and an as-Ž . sociate research professor at the Institute of Software, Chinese Academy of Sciences. He is now the senior visiting fellow of two institutes in China and the principle investigator of two national grants. His current research interests include problem-oriented model base systems, cognitive-based software process

model, analogical reasoning, agent-based simulation, timed workflow model, and inter-operation model for group decision. His publications mainly appear in Decision Support Systems, Knowledge-based Systems, Information and Software Technology, Journal of Systems and Software, and Chinese Journal of AdÕanced Software Research.

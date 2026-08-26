---
otero_id: 19896
otero_key: "6SWKC3HR"
title: "An interface between natural language and abstract argumentation frameworks for real-time debate analysis"
authors: "Benjamin Delhomme; Franck Taillandier; Irène Abi-Zeid; Rallou Thomopoulos; Cédric Baudrit; Laurent Mora"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113694"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An interface between natural language and abstract argumentation frameworks for real-time debate analysis

![](/api/attachments/6SWKC3HR/fulltext/images/db0a9c9e3d476bbc29fe4fcf533e9d9c12133a1f65dc92dae41d89752fc9a32a.jpg)

Benjamin Delhomme <sup>a,\*</sup>, Franck Taillandier <sup>b</sup>, Ir\`ene Abi-Zeid <sup>c</sup>, Rallou Thomopoulos C´edric Baudrit <sup>e</sup>, Laurent Mora

<sup>a</sup> Universit´e de Bordeaux, I2M, UMR 5295, 33400 Talence, France

<sup>b</sup> INRAE, Aix-Marseille Universit´e, UMR RECOVER, 13182 Aix-en-Provence, France

<sup>c</sup> Universit´e Laval, Department of Operations and Decision Systems, Qu´ebec G1V 0A6, Canada

<sup>d</sup> INRAE, Universit´e de Montpellier, CIRAD, Institut Agro, UMR IATE / INRIA GraphIK, 34060 Montpellier, France

<sup>e</sup> INRAE, Universit´e de Bordeaux, I2M, USC 1368, 33400 Talence, France

## A R T I C L E I N F O

Keywords: Argumentation framework Conflict resolution Real-time debate modeling Participatory debate Computational argumentation tool

## A B S T R A C T

Participatory approaches are increasingly being used to plan policies, usually involving stakeholders with con flicting interests, visions and objectives. Participants are often passionate about their cause, especially in sen sitive contexts such as their health or the environment for example. Whether involved in, or observing a debate, more often than not, it is hard to follow its progress; positions are unclear and arguments are unstructured often resulting in circular discussions. This is true both for participants in an ongoing debate hoping to reach a consensus as well as for those who. a posteriori, wish to understand what was discussed and how. However, at the current time, there are to our knowledge no tools to support real-time debates by allowing participants to visualize arguments and identifying opposing points of view in order to resolve conflicts. In order to fill this gap, we developed a model based on Dung’s argumentation framework that we implemented in a tool called AIPA, along with a web-application to facilitate user interaction. AIPA allows one to formalize and visualize, in real time, the arguments of the participants, to conduct inferences in order to identify acceptable arguments and to highlight conflicting ones. Furthermore, AIPA can be used a posteriori to summarize a debate in an easy to follow argument representation. The main contribution of AIPA is its ability to structure the debate by making the arguments chain traceable and transparent, in real-time and a posteriori, and this, with users with no expertise in argumentation. In this paper, we present AIPA along with two applications to illustrate its workings and benefits.

## 1. Introduction

Policy planners are faced with an increasingly complex contexts with sometimes strong resistance from citizens [12]. As a consequence, the last two decades have seen the emergence of participatory or concerted approaches to support public projects planning involving stakeholders with different perspectives and value systems [26]. Furthermore, many methods aiming at collecting the opinions of different stakeholders on planning projects have emerged, including the use of registers (elec tronic or not), web-forums, social networks, etc. However, the use of these tools raises several concerns: the discussions are not structured and the information can be difficult to find and to understand. This can lead to redundant arguments and to the inability to achieve a global overview of the debate: Which arguments are supported, who are the supporters and the opponents, where are the contradictions or the agreements, and in a real-time debate, if and how can a dead-end discussion be opened again etc. In a posteriori contexts, in order to summarize a debate and extract the main information, organizers of participatory processes often produce a synthesis report, analyzing the elements collected. However, this report normally arrives after the opinion gathering phase, which does not allow the participants to build their argumentation as a func tion of what has been said. Furthermore, the synthesis produced is generally focused on one part of the argumentation, namely that in favor of the decision made or the selected project, ignoring other possibilities, and ultimately translating only a small part of the debates. Therefore, it would be beneficial to have a tool/method capable of (1) supporting participants (regardless of their degree of expertise in argumentation) in real-time and (2) provide a posteriori a clear representation of the debate. Through a traceable and transparent debate, such a tool can help in building one’s own arguments and understanding those of others.

![](/api/attachments/6SWKC3HR/fulltext/images/41501328f1bb138b5594701d98577450bcf81117150d0d3776dfaa0d67610db7.jpg)  
Fig. 1. Attack graph.

In order to answer the need for traceability and structure both durint a debate and a posteriori, we propose to use argument analysis, an approach that has emerged in support of participatory decision-making [1]. We focus in particular on computational argumentation, which has been applied for different purposes, ranging from argument represen tation - graphical [18] and structural [25] - to the identification of a “winning argument” [19]. Among the various developments of compu tational argumentation, Dung’s abstract argumentation framework (AAF) [14] is particularly interesting since it has several characteristics that can be applied to debate support and analysis. However, an AAF remains a theoretical and conceptual approach; it does not provide a structured nor a semantic definition of arguments, focusing on the relation between arguments (attack relation) rather then on the internal structure or the meaning of an argument. This limits its applicability to a debate in a real context, where the different actors must understand the semantic of an argument. To overcome the AAF limitation, we devel oped a new argumentation model called ADM (Argued Discussion Model) and implemented it in a software tool called AIPA (Argumen tation Interface for Participatory Approach), in turn implemented in WebAIPA, a web application for a concurrent use by non-expert users. AIPA, which relies on AAF engines, is meant to support real-time debates for non-expert users by: (1) proposing an arguments semantic and (2) visualizing the arguments network and the debate’s status. AIPA allows one to formalize and visualize, in real-time, the arguments of the par ticipants, to conduct inferences in order to identify acceptable argu ments and to highlight conflicting ones. Furthermore, AIPA can be used a posteriori to summarize a debate in an easy to follow argument rep resentation. This is a novel and original contribution to the body of literature on computational argumentation and fills a need for debate support in practice.

The remainder of this paper is organized as follows: Section 2 pre sents the AAF and related literature on argumentation for collective decision-making; Section 3 presents our argued discussion model which is implemented in AIPA, presented in Section 4. Section 5 presents the implementation and a discussion of AIPA. We present two applications in Section 6 while Section 7 contains the conclusion.

2. Related literature on abstract argumentation in collaborative or participatory decision-making

## 2.1. Abstract argumentation frameworks

The abstract argumentation framework (AAF), developed by Dung [14], is based on the principle that an argument is considered acceptable as long as no other argument attacks it or if attacked, the attacked argument is defended by other arguments. Dung defines an AAF as an oriented graph where nodes are arguments and edges are attacks be tween arguments (Fig. 1). The term “argument” should not be misun derstood with the common interpretation of an argument as “a set of Statements composed of a conclusion and at least one premise, linked together by a logical link” [10]. In AAF, an argument is an abstract notion which has no semantic meaning; it can represent data, a pro posal... The notion of attack has also no direct semantic meaning; it is also an abstract concept. Based on these principles, Dung [14] provide the following definitions.

## 2.1.1. Definitions

We present below basic definitions of an AAF in order to facilitate the understanding of AIPA related concepts. Readers unfamiliar with AAF are referred to Dung [14].

Definition 1. An argumentation framework is a pair $A F { = } { < } A , R >$ with:

• A, a set of arguments,

• R, the binary relation on A such as for an argument a attacking $a _ { j } , ( a _ { i } ,$ $a _ { j } ) \in R .$

Definition 2. A set of arguments $S \subseteq A$ is said conflict-free iff ∀a , $a _ { j } \in S ,$ the arguments do not attack each other: (a , a ) ∕∈ R.

Definition 3. An argument $a _ { i } \in A$ is acceptable with respect to a set ${ \mathcal { S } } \subseteq A$ iff ∀a ∈ A, if a attacks a then a is attacked by S. Being attacked by a set S means being attacked by an argument in S.

Definition 4. A set of arguments ${ \mathcal { S } } \subseteq A$ is admissible if and only if S is conflict-free and each argument in S is acceptable with respect to S. The empty set is always admissible.

## 2.1.2. Extensions

An extension is a set of arguments that share common properties. It is built according to rules called semantics. Many types of extensions were defined by Dung [14].

Definition 5. A set $S \subseteq A$ is a preferred extension if and only if S is admissible and maximal (for set inclusion).

Definition 6. A set ${ \mathcal { S } } \subseteq A$ is a stable extension if and only if S is ad missible and ∀a ∈S, $\forall a _ { j } \in S , ( a _ { i } , a _ { j } ) \in R .$

Lemma 1. A stable extension is therefore an admissible set that attacks all the arguments that do not belong to it. It means that a stable extension is a preferred extension but the reciprocal is false.

Definition 7. A set $S \subseteq A$ is a complete extension if S is admissible and each acceptable argument with respect to S belongs to S.

Lemma 2. A preferred extension is complete.

Definition 8. A set ${ \mathcal { S } } \subseteq A$ is a grounded extension if it is the smallest (for set inclusion) complete extension. A grounded extension is unique.

Based on these definitions, two inference rules can be used in order to identify accepted arguments: credulous and skeptical. In a credulous inference, an argument is accepted if it belongs to at least one preferred extension. In a skeptical one, an argument is accepted if it belongs to the grounded extension.

## 2.2. Using an abstract argumentation framework in collective decisions

While there is a significant literature dealing with abstract argu mentation for decision-making, very few papers have focused on participatory aspects, collective decision making or debate. Most of the works related to abstract argumentation can be classified into four cat egories: (i) new argumentation frameworks based on the AAF, (ii) theoretical/conceptual analysis of an AAF and its properties, (iii) algo rithm and implementation and (iv) application to a problem. Papers in the first category are dedicated to providing new methodological development regarding argumentation frameworks, as for instance, using imprecise probability [22] or Attack-Incomplete Argumentation Frameworks [6]. The second category gathers theoretical work aiming at demonstrating properties of AAFs, such as the study of the theoretical relationship between formal concept analysis and abstract argumenta tion [3]. The third category corresponds to work aiming at improving abstract argumentation inferences, such as Cerutti et al. [11] or Niu et al. [23]. Finally, in the last category, many papers describe how to instantiate AAF approaches to real world decision context. For instance, Pazienza et al. [24] use abstract argumentation to predict financial an alysts’ recommendations in earnings conference calls, Santini and Yautsiukhin [27] to support the administration of security in computer networks.

Although very relevant since they provide methodological and/or operational contributions to make AAFs more efficient, none of these papers address the issues of concern to us in this paper. There is none theles some literature related to abstract argumentation and participa tory approaches, debate analysis, or collective decisions (6 papers). Two of these papers provide new methodological development regarding argumentation frameworks (first category). The first one proposes a practical argumentation semantics [21]. It allows to integrate, in addi tion to Dung’s theoretical argument (what to believe), practical argu ments (what to do). The authors provide new extensions considering these two types of argument. The distinction between these two types of argument is interesting to analyze decisions. However, it is mainly a methodological contribution, hardly usable in the context of a real-time debate in participatory decision-making. Its second methodological contribution is to combine AAFs with Issue-Based Information System (IBIS) argument models to support debates on design alternatives [5]. The model is implemented in a visualization tool dedicated to a pool of experts discussing different choices of design alternatives. This method uses a quantitative evaluation for argument and different rules and functions are provided to compute the score of each argument (level of acceptability). It is an interesting approach to support discussions be tween a pool of experts (mainly engineers) whose emphasis is on the assessment of alternatives. The notion of an argument’s score can be debated: Who gives the score? What is the meaning of an intermediate score in terms of argument validity? Furthermore, the tool is not intended for real-time debates with many participants; Issues such as computation time and distributed interface are not discussed. However, this paper contains some interesting elements for our work, namely a structured model of argument coupled with an AAF and a graphical interface to visualize the argumentation structure.

In the second category (theoretical contribution), Booth et al. [9] discuss the computational complexity of AAFs combined with labelling. This provides a better understanding of the notion of computational complexity for AAFs. In the third category, Alfano et al. [2] deals with algorithm or implementation. The authors provide an algorithm to compute the grounded semantics extension based on an updating approach. It is an incremental algorithm, useful in dynamic contexts where argumentation frameworks are continuously updated to consider new information and also interesting for real-time computation of extensions.

Doumbouya et al. [13] is at the intersection of the second and third categories. It provides a method to compute accepted arguments based on the properties of AAFs. The principle is to combine mathematical properties (e.g. symmetry, asymmetry, strong connectivity and irre flexivity) of AAF graphs to compute extensions. As the previous paper, it proposes an interesting strategy to accelerate inference computations, which is useful in a real-time, but not sufficient to fill the gap identified above.

Finally, Karanikolas et al. [20] has the most applied objective and proposes a procedure to support collective decision making for appli cations in agriculture. The authors combine Computational Social Choice (CSC) and AAFs in order to reach the best decision regarding issues in agricultural engineering; the approach was implemented in a tool called Ecobiocap. The principle is allow participants to express their preferences regarding alternatives. CSC is used in order to aggregate these preferences and rank alternatives. The use of argumentation consists of discussing the top alternatives and preferences. However, the paper focuses on the CSC part of the model, and the use of Argumen tation is just mentioned and not detailed. Furthermore, it is not intended for real-time debates, it is not centered on discussions but uses a voting system and it does not provide a visualization of the results.

The literature surveyed above constitutes the theoretical background for our research and has provided us with insights that shaped our approach: (i) a specific model of argument must be defined in order to give a meaning to this notion for all participants, (ii) inferences provided by AAFs can give interesting information to make decisions or/and to understand the issues of the debate, (iii) specific rules/inferences must be developed in order to use the model of argument with the AAF, and (iv) the tool should be able to perform calculations in real-time during the discussions and (v) the tool should be able to provide a simple and clear visualization of the argumentation structure. These five elements are at the core of our novel argument model, called Argued Discussion Model (ADM). We call AIPA the combination of ADM with rules using AAF inferences, and WebAIPA its implemntation as a web application (WebAIPA). We present ADM, AIPA and WebAIPA below.

## 3. Argued discussion model

The use of argument structures in a context of a debate in partici patory approaches is quite complex. Indeed, the different stakeholders have limited knowledge of theoretical argumentation and it has been shown that conflict resolution cannot be solved with complex argument structures due to the human argumentation process [28]. Moreover, since the objective is to focus on real-time debates, to argue and identify the type of argument at the same time would drastically increase the complexity for non-experts. Therefore, we propose the Argued Discus sion Model (ADM), a simpler model that shares the ideas of support and defeat relations from a bipolar framework [4], and implements the argument concept in a way usable in a real context of live debate.

Definition 9. An argument is an abstract concept referring to a proposition - a declarative sentence that can be either true or false. It is either a Conclusion or a Statement (which is also an abstract concept).

Remark 1. The word “argument” has a wide range of definitions and can lead to confusion. In the ADM, an argument is an extension of the AAF argument, meaning an ADM argument can be used in the AAF.

Definition 10. An Argued Discussion Model (ADM) is a pair $A D = \left. A _ { \mathrm { { i } } } \right.$ $T \rangle$ with:

• $\mathbf { A } ,$ a set of arguments with:

$C ,$ a set of Conclusions such as $C \subseteq A ,$

$s ,$ a set of Statements such as $s \subset A$ with $S \cup C = A$ and $S \cap C = \emptyset$ with:

$S _ { f } ,$ a set of StatementFor where ${ \mathit { S f } } \subseteq { \mathit { S } } ,$

$S _ { a } ,$ a set of StatementAgainst where $S _ { a } \subseteq S ,$

$S _ { a } \cup S _ { f } = S$ and $S _ { a } \cap S _ { f } = \emptyset ,$

• T, the binary relation $T \subseteq S \times A$ such as for a Statement s targeting (or being about) $a _ { i } ,$ we have $( s _ { i } , a _ { i } ) \in$ T with the following properties: – T is irreflexive such as $\forall s _ { i } \in S , ( s _ { i } , s _ { i } ) \not \in T$ - meaning no argument can target itself,

– T is asymmetric such as $\forall s _ { i } \in S$ and $\forall a _ { i } \in A , { \mathrm { i f } } \left( s _ { i } , a _ { i } \right) \in T ,$ then $( a _ { i } ,$ $s _ { i } ) \notin T$ - no argument can be targeted by an argument it targets, – T is functional such as $\forall s _ { i } \in S$ and ∀ $a _ { i } , a _ { j } \in A , \operatorname { i f } \left( s _ { i } , a _ { i } \right) \in T$ and $( s _ { i } ,$ $a _ { j } ) \in T ,$ then $a _ { i } = a _ { j }$ - which means a Statement is targeting at most one Argument,

![](/api/attachments/6SWKC3HR/fulltext/images/3d0a23d0e5a40557d392106fdc07767afce0c0e20b012f75cf3074c57a35600c.jpg)  
Fig. 2. Partial representation of the ADM.

– T is not injective such as ∀ ${ \bf \chi } _ { s _ { i } , s _ { j } } ^ { \prime } \in S$ and $\mid a _ { i } \in A , \mathrm { i f } \left( s _ { i } , a _ { i } \right) \in T$ and $( s _ { k } , a _ { i } ) \in T ,$ then $s _ { i } \neq s _ { k } - \mathbf { a n }$ argument can be targeted by more than one Statement,

– T is not surjective such as $\forall a _ { i } \in A , \exists s _ { i } \in S$ such that $( s _ { i } ,$ a ) ∕∈ T - an argument doesn’t have to be targeted,

$T _ { f _ { 5 } }$ is the binary relation $T _ { f } \subseteq S _ { f } \times A _ { : }$ , subset of T such as $T _ { f } \subseteqq T$ with $T _ { f }$ being transitive such as ∀ s<sub>fi</sub>, s<sub>fj</sub>, $s _ { f k } \in S _ { f } ,$ if (s<sub>fi</sub>, s<sub>fj</sub>) ∈ T<sub>f</sub> and $( s _ { f j } , s _ { f k } ) \in$ $T _ { f _ { 5 } }$ then $( s _ { f i } , s _ { f k } ) \in T _ { f }$ - meaning if one makes a StatementFor $( S _ { f 1 } )$ toward a StatementFor $( S _ { f 2 } )$ that is already targeting a StatementFor $( S _ { f 3 } )$ then $s _ { f 1 }$ approves also $S _ { f 3 } ,$

$T _ { a } ,$ the binary relation $T _ { a } \subseteq S _ { a } \times A ;$ , subset of T such as $T _ { f } \subseteq T$ with $T _ { f }$ being not transitive such as $\forall s _ { a i } , s _ { a j } , s _ { a k } \in S _ { a } , { \mathrm { i f ~ } } ( s _ { a i } , s _ { a j } ) \in T _ { f }$ and $( s _ { a j } ,$ $s _ { a k } ) \in T _ { f } ,$ then (s<sub>ai</sub>, $s _ { a k } ) \notin T _ { f } ,$ meaning if one makes a State mentAgainst $( S _ { a 1 } )$ toward a StatementAgainst $( S _ { a 2 } )$ that is already targeting a StatementAgainst $( S _ { a 3 } )$ then $S _ { a 1 }$ doesn’t reject $ { S } _ { a 3 }$

Example 1. Throughout this example, we assume a public consulta tion about increasing fuel tax of a group of citizens. Let $A _ { i }$ be an instance of Argument concept, an argument (though non-implementable) put forward is $A _ { 1 }$ - “Increasing taxes reduces fuel consumption and therefore pollution” or $A _ { 2 }$ - “Increasing taxes penalizes the poorest citizens”.

Definition 11. A Conclusion is a particular proposition pertaining to a given decision, i.e., resolving a question. It can be an alternative, a goal or a choice and it is always a final step in the discussion.

Example 2. (Example 1 - continued) A Conclusion is $C _ { 1 }$ - “Fuel tax should be increased". Another is $C _ { 2 }$ -“Fuel taxes should be decreased”.

Definition 12. All Conclusions are mutually exclusive. As a result (disjointness), there should not be any logical disjunction $\ " \mathrm { o r } ^ { \mathrm { , * } }$ in a Conclusion to avoid inconsistency.

Example 3. (Example 2 - continued) The two ConclusionsC and $C _ { 2 }$ are disjoint.

Definition 13. There is always a “Negation” Conclusion:

• Let $C _ { N e g }$ be a Negation Conclusion and $C _ { i }$ be a Conclusion,

$C _ { N e g } = \neg ( C _ { 1 } \lor C _ { 2 } \lor \dots \lor C _ { n } ) .$

Example 4. (Example 3 - continued) Following this list of Conclusions:

$C _ { 1 }$ - “Fuel tax should be increased”,

• $C _ { 2 }$ - “Fuel tax should be decreased”.

The Negation Conclusion would be $C _ { N e g }$ - “Gas taxes should not be increased nor decreased”.

Lemma 3. Since there is always a “Negation” Conclusion, there are al ways at least two Conclusions - $C _ { N e g }$ and $C _ { i } .$

Remark 2. With the exception of the two Conclusions required (Lemma 3), any number of Statement or Conclusion can be added at any time in any order.

Example 5. (Example 4 - continued) As the first Conclusion $C _ { 1 } \cdot \mathrm { ^ { 6 * } F }$ uel tax should be increased” was expressed, there is automatically a $C _ { N e g } \cdot$ “Not (Gas taxes should be increased)” - or written differently - “Gas taxes should not be increased” where $C _ { N e g } = \lnot C _ { 1 } .$

Definition 14. A Statement is an abstract concept referring to an assertion or a denial. It is declined into StatementFor (assertion) or StatementAgainst (denial). A StatementFor should be understood as “I agree with this argument because...” and inversely for a StatementAgainst.

Lemma 4. Since a Statement is in agreement or disagreement with an argument (a Conclusion or another Statement), it cannot exist without being linked to the “about” relation shown as the binary relation T in theDefinition 10, thus explaining the functional property.

Remark 3. Since the Conclusions are, by definition, mutually exclu sive (Definition 12), a Conclusion is therefore different from a State ment. The goal of mutual exclusion is to ensure the identification of a Conclusion that satisfies every participant or to encourage participants to reach a consensus in the absence of a common Conclusion.

Lemma 5. Since $s \subset A$ and $C \subseteq A$ ( Definition 10), only Conclusion ele ments can exist without being linked to other arguments.

Example 6. (Example 2 - continued) A citizen adds a StatementFor $S f _ { 1 }$ - “Increasing taxes reduces fuel consumption and therefore pollution” about $C _ { 1 }$ - “Fuel taxes should be increased” but someone disagrees with him/her and adds a StatementAgainst Sa - “This can only be true if credible and accessible alternatives to petrol cars are proposed, which is not the case today” about $S f _ { 1 }$

The ADM is partially represented in Fig. 2. The top concept can be either a Conclusion $( \mathrm { i } . \mathrm { e } . ,$ , debate issue) or Statement $( \mathrm { i . e . , }$ pros or cons assertions regarding an argument). Statement is always about a Conclusion or another Statement divided into StatementFor and

StatementAgainst. In a debate, there is always a Negation Conclusion that is the complement of all the other Conclusions. Since every concept is based on an Argument, we can integrate this model in AAF engines by converting the “about” relation into attacks in order to obtain AAF ex tensions (notably sets of preferred and grounded extensions).

## 4. Analyzing debate in real-time with AIPA

## 4.1. General principles

As discussed above, we designed a tool called AIPA that combines the ADM (argument model) with inferences developed by Dung in order to support participatory approaches in real-time for non-expert users. In AIPA, only the ADM graph is stored, every time an Argument (Statement or Conclusion) is added or removed, a corresponding AAF graph is generated according to a chosen “translation” into a graph of attacks (Section 4.2). The resulting AAF graph is recomputed every time a change occurs in the ADM graph, a Statement or a Conclusion can be made out of sequence, without order or time constraint. AIPA provides, in real-time debates, the following elements:

1. A trace - if wanted - of the debate,

2. The debate’s current status: “Conclusion accepted”, “Conflictual Conclusions” and “All Conclusions rejected”,

3. Statement which is in/out of favor for every Conclusion,

4. Statements accountable for the current debate status.

## 4.1.1. Traceability

A trace corresponds to the graph itself and its recording. AIPA re cords the different arguments, who makes them and when. Due to the ADM definition, a StatementFor or StatementAgainst is always posterior to its target (Conclusion or Statement). Thus, the resulting graph takes the form of a tree, facilitating its understanding by the participants and other stakeholders outside of the debate. Furthermore, the information regarding the three first elements can easily be represented on thi graph.

## 4.1.2. Debate status

AIPA, by combining ADM with AAF inferences, provides relevant compatibility (GNU/Linux & Windows) and development ease. They all have been interfaced with AIPA in order to switch seamlessly according to our needs. Three were found via the International Competition on Computational Models of Argumentation (ICCMA’17) [16]: Argmat-dvisat, Argmat-sat and ConArg. The last one being DungOMatic [29]. The computed extensions are then combined with our model (ADM) in order to provide an assessment of the debate in real-time. This assessment is done through grounded and preferred extensions from which we establish three graphs status.

Definition 15. The rules determining the graph status are defined as follows:

• Accepted: If only one Conclusion is included in the grounded extension,

• Conflictual: If there is no Conclusion in the grounded extension and if more than one Conclusion are included in the preferred extensions,

• Rejected: If there are no Conclusion in grounded extension and no Conclusions in the preferred extensions.

## 4.1.3. InFavor function

Since the binary relation between only StatementFor is transitive and the one between only StatementAgainst is not (Definition 10), we use as shown in the Algorithm 1 the negation of the binary operator XOR (exclusive or) in order to determine whether the selected Statement contributes positively to a given Conclusion or negatively. A Conclusion is reached (or not which means not in favor of) by iteration through a function “getTarget()” that returns only one Argument (Statement or Conclusion) aimed by a Statement (parameter of the function). The nature of an argument (StatementFor, StatementAgainst of Conclusion) is ascertained by a boolean function called “isInstanceOf()”. This func tion is displayed as “isInstanceOf(Argument, StatementFor/State mentAgainst/Conclusion)” and returns true if the argument is the specified concept.

Algorithm 1. inFavor(s,c) - determine if a Statement s is in favor of a Conclusion c.

```matlab
Data: A Statement s, a Conclusion c
Result: Return a Boolean, if True then the Statement s is in favor of the Conclusion c
Boolean res = isInstanceOf(s, StatementFor);
Statement temp = s;
while NOT(isInstanceOf(getTarget(temp), Conclusion)) do
    temp = getTarget(temp);
    res = NOT(res XOR (isInstanceOf(temp,StatementFor)));
end
if getTarget(temp) != c then
    res = NOT(res);
end
return res;
Algorithm 1: Algorithm to determines if a Statement is in favor of a Conclusion
```

information to the stakeholders during the debate in real-time (pro cessed in seconds). To address the real-time characteristic, we use en gines developed for extensions computing, from which we chose four depending on their availability, efficiency for a given semantic, platform

4.1.4. Results explanation

AIPA aims at providing an explanation of the results (i.e., the status of a Conclusion). By explanation, we mean highlighting the Statements that are behind the graph status result. To this end, a translation from our model has to be done in order to obtain a Dung graph for deter mining the debate status (Section 4.2), then explaining the debate status (Section 4.3).

![](/api/attachments/6SWKC3HR/fulltext/images/6cddbdd33d2e913126f88e0aadd036c9c791a20b09d1b9fd435e2ee3087bdaf9.jpg)  
Fig. 3. Model translated to Dung’s Framework.

## 4.2. Translation rules

The connection between Dung’s extensions and the model is done by translating (or converting) our argument model to an AAF graph, thus the “interface” in AIPA. Although one could choose to change any translation regarding the meaning he/she would expect from the debate (and the model used), the restrictions imposed by the model led to fixed translation of several concepts.

Remark 4. Since we convert an ADM graph to an AAF graph, we emphasize the fact that an edge in an ADM graph is always mentioned as “about”, “target” or “aim”, whereas the word “attack” refers to an edge in an AAF graph.

## 4.2.1. Conclusion translation

Definition 12 imposes mutual exclusivity between Conclusions. Thi is ensured by making each Conclusion attack each other Conclusion, thus allowing either one Conclusion or none to emerge from the grounded extension (Fig. 3). Fig. 3a provides an instance of debate with 3 Conclusions including the Negation Conclusion $C _ { n e g }$ and 1 State mentAgainst. Fig. 3b presents the resulting Dung’s graph using the Conclusion translation.

Remark 5. For better readability, StatementFor and StatementAgainst are distinguished by the format of every arrow. A StatementFor $s _ { f 1 }$ about a Conclusion $C _ { 1 }$ would be shown as a node containing $s _ { 1 }$ with a dashed arrow going toward the node $C _ { 1 }$ and StatementAgainst $S _ { a 1 }$ would be represented using simple arrow (Fig. 4a for both case).

![](/api/attachments/6SWKC3HR/fulltext/images/f4f5ccf58ba05ec0c3eec38c6bd6c5a95c525874808fa4b4dd7340adf57d5c9f.jpg)

Due to the Conclusion exclusivity definition (Definition 3), a distinction is made between Statement that targets Conclusion and Statement that targets other Statement.

## 4.2.2. StatementAgainst translation

As stated in Definition 14, a StatementAgainst is a denial of another argument, therefore, StatementAgainst is directly translated into an argument with an attack on the target of the StatementAgainst. Because a StatementAgainst is always about only one argument (Conclusion or Statement), A StatementAgainst generates only one argument and one attack in the Dung’s graph (Fig. 3).

## 4.2.3. StatementFor translation

Given that the AAF considers only attack and not support relation, one would ask the meaning of a StatementFor: Is the StatementFor a support that should strengthen another argument? Should the State mentFor be the exact opposite of an attack? Can we be in favor of something without being against its contrary? There are several valid answers to these questions. In order to consider these different possi bilities, AIPA provides two different translations for StatementFor, called Support and Optimistic translation. The person in charge of the debate (more probably the facilitator) will choose his/her preferred one according to his/her needs. These translations are heavily linked to the meaning we give to different situations in the debate. They are detailed below.

## 4.2.4. Support translation

This translation focuses on being as neutral as possible, i.e., every conflict needs to be solved in order to get a joint accepted Conclusion and Arguments are equals in importance. If the purpose is to find a common goal in a very “objective” manner where every argument matters, this translation should be used. As said before (Section 4.2.1), this translation has two cases, one where a StatementFor is about Conclusion and the other when a StatementFor is about another State ment. In both cases, every StatementFor attacks every StatementAgainst of the same level (they target the same argument) and converserly. The other translations work as follows:

![](/api/attachments/6SWKC3HR/fulltext/images/edd1c4aedd5ca395913482632f1710b99834dc14d92fdb45138d687ac69e56d5.jpg)  
(b) Dung support translation of figure 4a resulting in a Conflictual status $\bigl ( C _ { 1 } ^ { \prime } \& C _ { n e g } \bigr )$  
Fig. 4. Model 2 translated to Dung’s Framework with the support translation.

![](/api/attachments/6SWKC3HR/fulltext/images/6cbadea0c93bed3714b3b39635dce5526c5888cfe5f023e171ba3601c67fc249.jpg)  
Fig. 5. Model 2 translated to Dung’s Framework with the optimistic translation.

• StatementFor about Conclusion

– A StatementFor attacks every Conclusion that it doesn’t target (or it isn’t about).

• StatementFor about Statement

– If a StatementFor S target a Statement S, then S attacks every arguments attacked by S (thus support translation).

– If a StatementFor S<sub>f</sub> target a Statement S, then every argument that attack S also attack S .

Fig. 4a provides an instance of debate with 2 Conclusions and 4 Statements. Fig. 4b presents the resulting Dung’s graph using the sup port translation. The computation of the grounded extension (GE) and the preferred extensions (PE) via Dung’s engine results in:

$$
\begin{array}{l} \bullet G E = \emptyset \\ \bullet P E = \{\{S _ {4}, C _ {1}, S _ {2} \}, \{C _ {n e g}, S _ {3}, S _ {1} \} \} \end{array}
$$

Thus, in this example, neither of the Conclusion is accepted. Ac cording to Definition 15, they are conflictual. In this case, the debate should continue in order to provide more arguments to solve the conflict.

Remark 6. The reader may notice that cycles of attacks appear in Fig. 4b, these cycles are one of the reasons there are multiple preferred extensions in the AAF (Bench-Capon [7]).

## 4.2.5. Optimistic translation

Acknowledging the need to find a consensual solution without resolving every conflict, we propose another translation, called opti mistic translation, where only arguments which are not in conflict are taken into account. Two cases have to be distinguished as in support translation for the StatementFor as follows:

![](/api/attachments/6SWKC3HR/fulltext/images/d87f998122810188a30cced0953d1f291e475b871b76600640a225abaf0a7774.jpg)  
Fig. 6. Excerpt of WebAipa graph view.

• StatementFor about Conclusion

– A StatementFor attacks every Conclusion that it doesn’t target.

– StatementFor about Statement

– A StatementFor is attacked by every StatementAgainst sibling (Statement which shares the same target).

– A StatementFor attacks every opposite sibling of its target, mean ing a StatementFor that target a StatementAgainst will attack in AAF graph every StatementFor of the same level.

Fig. 5a shows the same graph used in the previous translation. We applied however the optimistic translation (Fig. 5b) resulting in different sets for the grounded extension (GE) and the preferred exten sions (PE):

$$
\begin{array}{l} \bullet G E = \{S _ {4}, C _ {1}, S _ {2} \} \\ \bullet P E = \{\{S _ {4}, C _ {1}, S _ {2} \} \} \end{array}
$$

Following Definition 15, Conclusion $C _ { 1 } ,$ belonging to the $\mathbf { G E } ,$ is accepted with the optimistic translation. This small example provides the difference between the two translations. Whereas the first trans lation led to conflicting Conclusions, this second translation resolves the debate by giving $C _ { 1 }$ as accepted. Thus the choice of a translation will depend on the objective: if the emphasis is on the debate and one wants the debate to really lead to a consensual solution, the support translation will be preferred; if, however, it is necessary to settle the debate and reach a Conclusion, the optimistic translation will be preferred.

## 4.3. Providing indications regarding the graph status

Since there are two specific translations for a StatementFor (support and optimistic) and three debate status available (accepted, conflictual and rejected), there is a maximum of eight achievable outcomes to explain. However, in our case, only the accepted debate status differs for the explanations according to the chosen translation.

Definition 16. In a support translation, a Statement explains an accepted Conclusion if it’s included in the grounded extension and if it’s in favor of the accepted Conclusion (Algorithm 1).

Definition 17. In an optimistic translation, a Statement explains an accepted Conclusion if it’s included in the grounded extension and it matches one of the following rules:

• The Statement is a StatementFor

• The Statement is a StatementAgainst and matches one of the following rules:

– the Statement has no siblings (other Statement aiming at the same target)

– the Statement is targeted by at least one StatementFor

– all siblings of the Statement are StatementAgainst or follow all of the following rules:

\* the sibling of the Statement is at least targeted by one Statement

\* the sibling of the Statement is only targeted by a StatementFor

Example 7. Fig. 5 led to the result $C _ { 1 }$ as an accepted Conclusion with $S _ { 4 }$ (SF) and $S _ { 2 } \ ( S { \mathrm A } )$ included in the grounded extension $\begin{array} { r } { ( G E = \{ S _ { 4 } , C _ { 1 } , } \end{array}$ S }). Since only $s _ { 2 }$ is compliant with the Definition 17, S is the reason behind $C _ { 1 }$ being the accepted Conclusion.

Since there are at least two conflictual Conclusions, we provide ex planations (Definition 18) according to the selected conflictual Conclusion.

Definition 18. In support and optimistic translations, a Statement explains a conflictual Conclusion if it’s in favor of this Conclusion and it’s included in the union of every preferred extension that contains a Conclusion.

Example 8. Fig. 4 shows a conflictual result with two preferred ex tensions: $\{ S _ { 4 } , C _ { 1 } , S _ { 2 } \}$ and $\{ C _ { n e g } , S _ { 3 } , S _ { 1 } \}$ . Having Conclusion in both ex tensions means every Statement included in either one will explain the conflict when combined with the inFavor function. In this exemple, $C _ { 1 }$ has a conflictual status because $s _ { 2 }$ and $S _ { 4 }$ exists and CNeg shares the same status due to $s _ { 1 }$ and $S _ { 3 } .$

Definition 19. In a support and optimistic translation, a Statement explains a rejected Conclusion if it’s in favor of this Conclusion and it’s included in the union of every preferred extension that does not contain a Conclusion.

## 5. Implementation

ADM and AIPA were implemented in a web application tool called WebAIPA, which displays, in real-time, any changes in the debate graph. Fig. 6 shows the ADM graph of the AipaForum debate. Arrows repre senting a StatementAgainst are colored in red and StatementFor are colored in blue. Conclusion and Statements nodes have their own colors depending on the AAF extensions results. Green Statement is a State ment that contributes to an accepted Conclusion. Grey Statements means that they are conflicting, and white Statements do not contribute to the current status of the graph. By hovering over a Conclusion, Statements in favor of the Conclusion will be highlighted by a blue circle while Statements not in favor will be highlighted by a red circle. Finally, the user can change the translation used (support or optimistic) and see the new status of the graph. (Definition 15).

WebAipa is interfaced with a custom-made forum (AipaForum) through a REST-like API (web services for interoperability between systems) to WebAIPA with the aim of providing the current state of the debate and a graph representation of the forum. Both representations have their arguments connected to one another in order to keep track of the debate and to be able to go from a representation to another. Par ticipants had access to the forum where they had to formulate their arguments and to WebAIPA, allowing them to see the induced argu mentation structure. Each time an argument is added or removed, AIPA provides new information on the argument acceptability thanks to AAF inferences. The replies are indented so every Statement are below the other Statement or Conclusion they target. As soon as a new reply is made, the corresponding Statement is also created in WebAipa.

The forum, WebAIPA and AIPA engine worked in real-time allowing users to move from one to the other without loss of information, i.e., as soon as an argument was formulated, it was represented in the argument graph. This allowed participants to add their arguments in the forum (a classical format and well mastered by the participants) and to see the influence of their arguments on the acceptability of the Conclusions as well as to understand the argumentation structure.

## 6. Applications

In order to illustrate the applicability of our tools we present two case-studies. The first is in the context of a debate regarding the choice among four urban development projects. This exercise using fictitious projects aims at showing how our tools can be used in real-time in a debate framework. The second application is within a participatory process for a real urban development projec, namely the choice of a where to build a new route for a tramway. In this case, AIPA was used a posteriori to formalize the arguments and analyze the debates that took place on an online forum during the participatory process.

## 6.1. Application 1: real-time debate

In order to illustrate the functioning of AIPA and its potential ben efits in real-time, we applied it to a debate related to an urban planning project around Bordeaux University. The participants in the debate were asked to discuss and choose between four fictitious projects for the development of this area:

• Naturalia (C ): a solution that gives priority to the natural environ ment and respect for fauna and flora,

• Cyber Campus (C ): a solution based on new technologies and link to industry,

• Mobility (C<sub>3</sub>): a solution highlighting the problems of travel and mobility, facilitating access for all on campus,

• Agora (C ): a solution that places human relations at the centre and proposes arrangements to facilitate exchanges and proximity.

Eight members of the University participated in the debate using AIPAForum; they had different profiles (age, gender...) and functions (student, professor, researcher, technician...) representing a wide range of opinions. Participants interacted individually with the system by adding Statements without restrictions on the number of arguments. The first author presented the projects to the participants along with an explanation of what Statements represent and how to use the forum. Although it is generally possible to add at any time a new Conclusion, e. g. a new project (which could eventually induce a compromise), we chose to deactivate this capability since we wanted the participants to reach a consensus with the help of AIPA, Statements however could be added anytime about an another Statement or a Conclusion.

The participants expressed 44 arguments. The number of arguments per participant ranged from 3 to 8, distributed as follows: Naturalia (14), Cyber campus (12), Mobility (10) and Agora (8). A debriefing followed the debate. In the application case, WebAIPA was combined with AIPAForum in order to evaluate the accessibility and the potential of AIPA. Globally, the participants appreciated the support of the argu mentation structure and the information given by inference in a forum type platform. However, the combination of the forum with AIPA, albeit usable by non-specialists, has limitations. Some participants expressed their accordance with a Statement without an explicit argument by a simple “I agree”/“I disagree”. Such expressions cannot currently be used as arguments in AIPA since they are incomplete. They do not provide a rationale for the agreement/disagreement. An alternative would be to integrate, in AIPA, a framework such as the weighted-based framework [15] by adding a preference concept in the model (like/dislike). Other relevant argumentation frameworks are the attitude-computing approach inspired by social psychology as implemented in Thomopou los et al. [31] or the social choice oriented approach [8]. Furthermore, some participants, had difficulty expressing their arguments. For example, some Against Statements did not target the right argument for their purpose. Another issue is the argument itself, since normally in a debate, people rarely describe to their position in one argument as formalized in AIPA (Statement). They often nuance a general assertion or denial, e.g. “It’s a good thing to have pedestrian areas, but at the same time it’s not convenient for parking.” This natural human behavior, observed on the forum, cannot be directly translated into an argument in AIPA. In fact, AIPA expects simple arguments that express a single idea. This limitation does not mean than it is not possible to express complex arguments, rather that an argument composed of several ideas must be broken down into several arguments. If we consider the previous example, the argument “It’s a good thing to have pedestrian areas, but at the same time it's not convenient for parking." has to be broken down into two AIPA arguments: “It’s a good thing to have pedestrian areas” and “It is not convenient for parking." Finally. the WebAipa interface was also found to be perfectible regarding explanations about conflicts. On a positive note, participants felt that the tool helped to refocus the debates by highlighting the important arguments, i.e., those that carried the debate forward. This made it possible to focus on these arguments without trying to add elements against arguments that were already discarded.

## 6.2. Application 2: participatory approach

In order to illustrate the second anticipated benefit of AIPA, namely summarizing, a posteriori, debates for transparency purposes, we applied it to a real case in urban and transportation planning.<sup>1</sup> Bordeaux Metropole planned to extend the tram track in order to connect new cities in the metropolis, and notably Saint-M´edard-en-Jalles which will be the new terminus of the line. Four routes were proposed by the urban planning team. The choice between these routes was the subject of a participatory process in which citizens were asked to give their opinions on these routes. The participatory process regarding this tram track extension lasted three years (2017–2019) and through many meetings with the participation of hundreds of citizens. The participatory approach also used a web forum for the online collection of citizens opinions on the various routes submitted for discussion. 435 people participated in the exchanges on this forum through 676 messages.

In order to represent the discussions on the forum, we conducted an exhaustive content analysis of the 676 messages, and formalized them as input arguments through WebAIPA. The analysis of these messages al lows us to note several limitations of the way the forum was used, making the debate and the positions of the participants difficult to un derstand. Indeed, we can observe that: 1) some messages do not propose any arguments, nor do they express any opinion, 2) some messages are very long, composing a complex argumentation set that is difficult to apprehend directly, 3) many arguments are proposed several times (strong redundancy), 4) there is a lack of interaction between the mes sages, often not allowing for constructed exchanges.

The formalization of the arguments was done manually by extracting them from the different messages. This led to 173 different arguments in WebAIPA. Several lessons can be learned from this application. First, even with 173 arguments, results were obtained instantaneously. Therefore, our tool is adapted to a real debate context in which a high number of arguments are expressed. Second, the graph structure of AIPA highlights the links between arguments which facilitates the identifi cation of conflicts and oppositions. For example. AIPA provided the set of pro and con arguments for each route, making it easy to identify the arguments for and against each proposal. Finally, AIPA provided the status of each Conclusion (tram route) as well as the arguments that explains this status. As a matter of fact, in this appplication, the four routes are in conflict, i.e., none of them are accepted. In fact, each route has a set of arguments for it and against it with two of routes facing very strong opposition. No consensus was possible and the Bordeaux Metro pole finally decided in 2019 to abandon these routes and to opt for a bus system rather than a tramway.

In this application, AIPA could not support the construction of a consensus since it was used a posteriori, however its use has allowed to structure and clearly represent the debate for maximum transparency thereby facilitating the understanding of what was said and how. The main limitation of this application is the need for a manual argument extraction phase. This however, could have been overcome if the par ticipants had used AIPAForum directly, which was not possible since it was not available in 2017. Another alternative worth exploring to reduce the burden of manual argument extraction is the use of argument mining to create AIPA compatible arguments.

## 7. Conclusion

In response to an identified need for tools to support debates in realtime and in a posteriori analyses, we developed and implemented a model based on AAF, along with a web-application to facilitate user interaction. AIPA allows one to formalize and visualize the arguments of the participants, to conduct inferences in order to identify acceptable arguments and to highlight conflicting ones. As illustrated, it is partic ularly relevant for debates in participatory contexts. It acts as an inter face between arguments in natural language and abstract arguments. While AAFs provide inferences, our tool provides a meaning.

AIPA allows to structure in a simple way the arguments in the debate, to define the acceptable arguments, to give information on pro/cons arguments, on conflicting situations and on key arguments. It provides a tree-like representation of the argument structure easy to follow to all participants in a debate, regardless of their argumentation talents. Its main benefits are two-fold: to help participants in a debate to structure their arguments and to understand those of the others, and to under stand, a posteriori, how a debate was conducted.

Even if AIPA can help reach consensus by highlighting deadlocks in the discussion, once opinions are polarized, it might very difficult to reach a common ground. Nonetheless, this was not our aim behind developing AIPA and it was not our pretention to provide a tool that guarantees resolution of all conflicts. Our primary objective is to allow for a better structuring of the debates, to facilitate their understanding and follow-up. We believe that this can contribute to rich exchanges between the participants, and ultimately to decisions quality.

Our contribution in this paper is two-fold: (1) at the methodological level by developing a model for argument representation that completes AAFs and (2) at the technical level by designing and developing an easy to use web-based tool meant to help non-expert users in debates to structure their opinions (participants) as well as to understand, a pos teriori debates (observants). Although AIPA is operational and can be used in numerous contexts of participating debates, many further en hancements can be envisaged. At an application level, it would be interesting to conduct an experiment where we compare how a debate is conducted with and without AIPA in order to measure its added benefit. At a methodological level, different argument translations could be used concurrently, each translation referring to a different argument concept such as in Toulmin's advanced argument model. Furthermore. the combination of argument mining with AIPA could be explored.

In terms of decision support, AIPA can be used to help structure a multicriteria decision aiding (MCDA) process. It can support the model structuring phase, during workshops where actors engage jointly in identifying alternatives, constructing criteria, evaluating alternatives and discussing and challenging the aggregated results obtained with decision analytic methods. This can increase the acceptance of the final decision by all parties since the arguments would be easy to follow and the rationale behind the decisions related to the choice of criteria or to the evaluations of the alternatives more transparent. In fact, this type of use was illustrated in Taillandier et al. [30] in the context of the choice of an urban development project. As argued in Introne and Iandoli [17], Arguments Based Systems, can be useful in decision-support contexts where decision makers are encouraged to rigorously express their rationale.

Finally, we believe that the integration of argumentation based tools such as AIPA within decision support systems, especially those based on black-box optimization procedures, can seriously enhance the accept ability of results by providing explanations regarding the solutions retained. This future avenue of research is worth pursuing for the cross fertilisation of both domains.

## References

[1] Jussi Airaksinen, Eerika Albrecht, Arguments and their effects - a case study on drafting the legislation on the environmental impacts of peat extraction in finland J. Clean. Prod. 226 (2019) 1004–1012.

[2] G. Alfano, S. Greco, F. Parisi, An incremental algorithm for computing the grounded extension of dynamic abstract argumentation frameworks, Group Decis. Negot. 28 (5) (2019) 935–960.

[3] L. Amgoud, H. Prade, A formal concept view of abstract argumentation, in: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificia Intelligence and Lecture Notes in Bioinformatics), 2013, 7958 LNAI:1-12.

[4] L. Amgoud, C. Cayrol, M.C. Lagasquie-Schiex, P. Livet, On bipolarity in argumentation frameworks, Int. J. Intell. Syst. 23 (10) (2008 October) 1062–1093.

[5] P. Baroni, M. Romano, F. Toni, M. Aurisicchio, G. Bertanza, Automatic evaluation of design alternatives with quantitative argumentation, Argum. Comput. 6 (1) (2015) 24–49

[6] D. Baumeister, D. Neugebauer, J. Rothe, Verification in attack-incomplete argumentation frameworks, Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics) 9346 (2015) 341–358

[7] T.J.M. Bench-Capon, Dilemmas and paradoxes: cycles in argumentation frameworks, J. Log. Comput. 26 (4) (2016) 1055–1064.

[8] Pierre Bisquert, Madalina Croitoru, Christos Kaklamanis, Nikos Karanikolas, A decision-making approach where argumentation added value tackles social choice deficiencies, Prog. AI 8 (2) (2019) 229–239.

[9] Richard Booth, Martin Caminada, Paul E. Dunne, Mikolaj Podlaszewski, Iyad Rahwan, Complexity properties of critical sets of arguments, in: S. Parsons, N. Oren, C. Reed, F. Cerutti (Eds.), Computational Models of Argument, vol. 266 of Frontiers in Artificial Intelligence and Applications, Scottish Informat & Comp Sci Alliance, 2014, pp. 173–184.

[10] P. Breton, G. Gauthier, Histoire des th´eories de l’argumentation, La D´ecouverte Paris, 2000, p. 120.

[11] Federico Cerutti, Massimiliano Giacomin, Mauro Vallati, How we designed winning algorithms for abstract argumentation and which insight we attained, Artif. Intell. 276 (2019) 1–40.

[12] Cecilia Claeys, Arlette Herat, Carole Barthelemy, Valerie Deldreve, The calanques national park, between environmental effort and urban effort, Articulo - J. Urban Res. 16 (2017).

[13] Mamadou Bilo Doumbouva. Bernard Kamsu-Foguem. Hugues Kenfack Argumentation and graph properties, Inf. Process. Manag. 52 (2) (2016) 319–325.

[14] Phan Minh Dung, On the acceptability of arguments and its fundamental role in nonmonotonic reasoning and logic programming, in: In IJCAI, vol. 93, 1995, pp. 852–857.

[15] Paul E. Dunne, Anthony Hunter, Peter McBurney, Simon parsons, and michael wooldridge. weighted argument systems: basic definitions, algorithms, and complexity results, Artif. Intell. 175 (2) (2011 Feb) 457–486.

[16] Sarah A. Gaggl, Thomas Linsbichler, Marco Maratea, Stefan Woltran, Design and results of the second international competition on computational models o argumentation, Artif. Intell. 279 (2020 Feb) 103193.

[17] Joshua Introne, Luca Iandoli, Improving decision-making performance through argumentation: an argument-based decision support system to compute with evidence. Decis. Support Syst. 64 (2014 August) 79–89.

[18] Areti Karamanou, Nikolaos Loutas, Konstantinos Tarabanis, Argvis: structuring political deliberations using innovative visualisation technologies, in: Proceedings of the Third IFIP WG 8.5 International Conference on Electronic Participation, ePart’11, Springer-Verlag, 2011, pp. 87–98.

[19] Amin Karamlou, Kristijonas Cyras, Francesca Toni, Deciding the winner of a debate using bipolar argumentation, in: AAMAS. 2019.

[20] N. Karanikolas, P. Bisquert, P. Buche, C. Kaklamanis, R. Thomopoulos, A decision support tool for agricultural applications based on computational social choice and argumentation, Int. J. Agric. Environ. Inf. Syst. 9 (3) (2018) 54–73.

[21] Hiroyuki Kido, Katsumi Nitta, Practical argumentation semantics for sociall efficient defeasible consequence., in: AAMAS. 2011.

[22] M. Morveli-Espinoza, J.C. Nieves, C.A. Tacla. An imprecise probability approach for abstract argumentation based on credal sets in: Lecture Notes in Compute Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics). 2019. 11726 LNAI:39-49.

[23] D. Niu, L. Liu, S. Lü, New stochastic local search approaches for computing preferred extensions of abstract argumentation, AI Commun. 31 (4) (2018) 369–382.

[24] A. Pazienza, D. Grossi, F. Grasso, R. Palmieri, M. Zito, S. Ferilli, An abstrac argumentation approach for the prediction of analysts’ recommendations following earnings conference calls, Intelligenza Artificiale 13 (2) (2020) 173–188.

[25] Chris Reed, Katarzyna Budzynska, Rory Duthie, Mathilde Janier, Barbara Konat, John Lawrence, Alison Pease, Mark Snaith, The argument web: an online ecosystem of tools, systems and services for argumentation, Philos. Technol. 30 (2)

[26] Nipada Ruankaew, Christophe Le Page, Pongchai Dumrongrojwatthana, C´ecile Barnaud, Nantana Gajaseni, Annemarie van Paassen, Guy Tr´ebuil, Companion modelling for integrated renewable resource management: a new collaborative approach to create common values for sustainable development. Int

[27] F. Santini, A. Yautsiukhin, Quantitative analysis of network security with abstract argumentation, in: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics). 2016. 9481: 30-46.

[28] A.A. Sillince John. Masoud H. Saeedi. Computer-mediated communication: problems and potentials of argumentation support systems. Decis, Support Syst. 26 (4) (1999 October) 287–306.

[29] M. Snaith, J. Devereux, J. Lawrence, C. Reed, Pipelining argumentation technologies, Front. Artif. Intell. Appl. 216 (2010) 447–453.

[30] Franck Taillandier, Benjamin Delhomme, Rallou Thomopoulos, C´edric Baudrit, Ir\`ene Abi-Zeid, Designing an argumentative decision-aiding method for urban planning., in: Proceedings of 7\`eme Colloque du r´eseau OPDE - Des Outils pour D´ecider Ensemble, 2017 October.

[31] Rallou Thomopoulos, Julien Cufi, Maxime Le Breton, A generic software to support collective decision in food chains and in multi-stakeholder situations. in: FoodSim 2020 - 11th Biennial FOODSIM Conference, Proceedings of FoodSim, Ghent, Belgium. September 2020. 2020

Benjamin Delhomme is a PhD student in civil engineering at the Univer- sity of Bordeaux. After being graduated in civil engineering from the University of Bordeaux, he obtained a master’s degree in computer science from the Univer- sity of Grenoble-Alpes. Specialized in knowledge representation, he participated in the European project MICA (Mineral In telligence Capacity Analysis). He is currently working on the development of a decision support tool combining multicriteria methods and argumentation systems within the rehabilitation of building stocks.

Franck Taillandier is a researcher (HDR) at INRAE Aix-en-Provence. For 8 years, he was assistant professor at the University of Bordeaux in civil engineering. He works on complex system modeling, decision-support and risk management applied to civil engineering, including urbanism, architecture, real property and project management.He authored more than 90 articles and has been involved in several projects regarding urban planning, infrastructure man- agement, risk management, building energy and material eco-design. He has coordinated project work packages and supervised several PhDs.

Irene \` Abi-Zeid is a full professor specialized in multicriteria decision aid- ing at Laval University, Ouébec, Canada, She obtained a B.Sc, and a M.Sc, in Mathematics from Ottawa University and a Ph.D. in applied statistics and risk analysis from Université du Ouébec and the ENGREF (France). Her current research activities are conducted along two major axes

Search planning for search and rescue operations and Multicriteria Decision Aiding with applica- tions in transportation, urban planning, social deprivation, and water quality. She has published in international conferences and journals and has conducted numerous funded research projects in the area of decision sciences for industry and governments at the provincial and federal levels. She has developed MCDA- ULaval, an open source software implementing many ELECTRE multicriteria methods. Her software is widely used for research and teaching purposes in Canada and Europe and is freely available.

Rallou Thomopoulos is a senior researcher (HDR) at INRAE Montpel- lier in knowledge representation and decision aiding. She defended her PhD thesis in computer science in 2003. She has been a researcher in knowledge representation at the INRA National Research Institute since 2004 an and as- sociate researcher in the LIRMM Computer Sci ence Laboratory at Montpellier since 2006. She works on the integration of ontology and data-representation formalisms, the expression of gradual information and viewpoints in ontologies, and, more specifically, in the framework of the conceptual graph model.

Cedric \` Baudrit is a researcher for the French National Research Institute for Agriculture, Food and Environment (INRAE), in knowledge representation and reasoning. He is interested in the development of mathematical tools ca- pable of (1) integrating frag mented heterogeneous knowledge stemming from different sources; (2) taking into ac count stochastic and epistemic uncertainty in order to model global complex system. In 2005, he received the Ph.D. degree in computer science from Universit´e Paul Sabatier, in Toulouse (France). In 2002, he holds a master in Applied Mathematics and Computer Science from the University of Orl´eans, France.

Laurent Mora is assistant professor at the University of Bordeaux in Civil Engineering since 2006. He is the head of the civil engineering department of the IUT of Bordeaux. He works on modeling and simulation of building energy performance, decision-support, IA and uncertainty modeling. He is the author of more than 80 articles and coordinated or participated into several national and international research proiects

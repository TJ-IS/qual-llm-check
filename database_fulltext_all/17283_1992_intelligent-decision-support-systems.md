---
otero_id: 17283
otero_key: "XHS7HGGQ"
title: "Intelligent decision support systems"
authors: "Hans W. Gottinger; Peter Weimann"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90053-r"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Intelligent decision support systems

Hans W. Gottinger

Institute of Management Science, University of Maastricht, Maastricht, Netherlands and Fraunhofer Institute for Technological Forecasting, Euskrichen, Germany

Peter Weimann

Industrieanlagen-Betriebsgesellschaft, D-8012 Ottobrunn, Germany

This paper explores the basic ingredients of intelligent decision support systems in partial contrast to approaches followed by expert systems. Rule based expert systems for decision support have been successful for well structured, well understood decision situations of a taxonomic classification type. But, in general, A.I. has growing influence in software

![](/api/attachments/XHS7HGGQ/fulltext/images/17ed5f094e1e1c42700362703b2b8b2150684c4b82202702c8e4dab2154838d5.jpg)

Hans W. Gottinger received a diploma in Economics from the University of Munich (1966), PhD Math. Statist., University of Munich, 1969, Habil. Oper. Research, Technical University of Munich, 1976. He held positions as visiting professor at the University of California, Berkeley (1972–1974), the University of California, Los Angeles (1976), and the University of Virginia, Charlottesville (1985–1987). He has been Professor of Management Science, University of Maastricht. The

Netherlands since 1985 and Director, Fraunhofer Institute of Technological Forecasting, Euskirchen/Bonn, Germany since 1987. Since 1990 he has been on leave of absence as a Visiting Professor to Nuffield College and the Oxford Institute for Energy Studies, Oxford, UK.

![](/api/attachments/XHS7HGGQ/fulltext/images/fa258fce49af3b783bee0ffa9eaebbb2644fe2fe6fae35c3cd62de6c2523fa48.jpg)

Peter Weimann received his Master of Computer Science from the University of Dortmund. Currently working for the IABG he has been involved in the research and development of expert systems throughout his career and is at present involved in expert database systems, intelligent decision support systems, and object oriented technology. Peter Weimann has written and contributed in several publications and papers. He is official expert and person of contact for

AI/Expert Systems in his company.

Correspondence to: Hans W. Gottinger, Institute of Management Science, University of Maastricht, P.O. Box 591, NL 6200 Maastricht, Netherlands.

engineering for ill-structured application areas by supporting an incremental development process with new programming techniques and architectures. As uncertainty is prevalent, information costly and payoff relevant, and the preferred solution depends on the specific beliefs and preferences of an individual or group decision maker. The resolution methods of decision theory embodied in first-order predicate logic, form a natural basis for computerized intelligent decision support. A unified characterization of knowledge and inference for logical, probabilistic, and decision-theoretic reasoning is developed for intelligent decision support over a wide spectrum of decision situations.

Keywords: Intelligent decision support, Expert systems, Influence diagrams, Decision theory, Knowledge engineering

## 1. Introduction

In the past few years there has been substantial attention devoted to the use of artificial intelligence (AI) methods and architectures, most commonly rule based expert systems, as tools for decision support. An inherent focus of expert system development is the adequate modeling of human problem solving capabilities. In its sequel we observe the construction of several methods of representation like production rules, semantic networks, frames and scripts as well as inference mechanisms such as logic reasoning, non-monotonic reasoning and default reasoning, e.g., in facing problems like inconsistency and knowledge gaps. From the software engineering point of view, systems analysis can be done on a higher level of abstraction (closer to the domain expert) and involving the entire engineering cycle (Patrick 1986).

Especially rule based techniques have proven to be very attractive for a variety of problems, particularly those which have fairly well structured (though possibly large) problem spaces, which can be solved through the use of heuristic methods or rules of thumb, and are currently solved by human experts. In these domains the reasoning and explanation capabilities offered by rule based expert systems are very effective. A rule-based approach tends to break down when applied to more difficult problems or problems that require a normative, prescriptive structure for decision and inference purposes, in particular, relating to the following situations:

(1) there is substantial uncertainty on various levels of decision-making;

(2) the preferred solution is sensitive to the specific preferences and desires of one or several decision makers;

(3) problems of rationality and behavioral coherence are intrinsic concerns of decision systems;

(4) problems of resource-boundedness for the user can be dealt with more adequately (Hansson and Mayer, 1988).

In established fields such as operations research and management science we have been developing methods for allocating resources under various conditions of time, uncertainty and rationality constraints. Central to these methods is the existence of an objective or utility function, as an indicator of the desirability of various outcomes. We will draw on this body of knowledge, especially elements related to the normative use of individual and group decision theory to approach difficult decision problems.

On the other hand, an evolutionary approach to system development is a major advantage of a production system or rule based program architecture and of expert system techniques in general. That is, once general decisions have been made regarding the basic control procedures and the organization of the rule base, the knowledge base can be incrementally improved by adding, modifying or deleting individual production rules. The advantage of rule-based program architecture combined with new programming paradigms, such as object-oriented programming and logic programming, facilitates advanced prototyping. In this light we develop methods for reasoning about the structure of probabilistic and decision theoretic models in a rule-based manner based on domain knowledge.

Summarizing, our attempt is to integrate conventional AI, logic-based approaches to problem solving with techniques for probabilistic analysis and decision making under uncertainty from operations research and management science to develop methods for improving the quality of decision making.

In this view, an intelligent decision support system (IDSS) is an interactive tool for decision making for well-structured (or well-structurable) decision and planning situations that uses expert system techniques as well as specific decision models to make it a model-based expert system (integration of information systems and decision models for decision support). The decision model imposes a normative profile on the IDSS serving for problem structuring and knowledge representation.

## 2. Computer-aided decision making

Advances in artificial intelligence, coupled with analytic techniques developed in the fields of systems analysis and operations research, can provide a means of significantly improving the quality of decision making by individuals and organizations. Traditional approaches to computer assisted decision making include decision support systems (DSS). The typical DSS provides means to sort, select, and transform information in the data base. Another recent development has been the use of artificial intelligent techniques, most commonly rule-based expert systems, as tools for decision support.

The efficacy of a rule based approach to decision support depends on the nature of the problem being solved. The classification-recommendation approach to decision making has significant limitations for particular types of domains. There are several incompatible taxonomies for the categorization of expert system problem areas. The most common scheme (Clancey, 1986) divides expert systems application areas into analysis problems (e.g. debugging, diagnosis and interpretation) and synthesis problems (e.g., configuration, planning and scheduling). Some problems cannot be classified that way because they comprise subtasks with many independent or semi-dependent sources of knowledge, interacting to find a common solution. The best example for such class of problems is speech recognition, but also in decision support we have problem areas such as planning/scheduling in military command and control. In those areas the expert systems approach supports the incremental improvement of the heuristic problem-solving process by adequate modeling of a rule—or frame—based representation embedded in an appropriate architecture, e.g., the blackboard architecture (Nii, 1986). Especially for the analysis problems, the heuristic classification based on a recommendation approach to decision making has significant limitations for particular domains.

Perhaps the biggest drawback of the expert systems approach is that most implementations do not have a general representation for the preferences or beliefs of the decision maker. This lack of a high level map to describe what the decision maker desires and believes has several ramifications. Another problem is that traditional AI systems are not well equipped to handle small differences in outcomes on a variety of attributes which may affect decision making. For example, most planning systems are based on developing a plan which can be proven to achieve a specific goal. The plan is either successful or unsuccessful (i.e., it can be proven constructively that there exists a successful plan or not), but most planning algorithms cannot evaluate trade-offs among factors such as the speed of achieving a goal versus cost and safety considerations. This contrasts with real decision situations, where alternative possible plans meet a variety of objectives to various degrees. In specific application areas combining analysis and synthesis problems (e.g., command and control) it might be advantageous to merge expert system techniques with decision procedures. In the planning and scheduling task for air traffic control or for the planning task of military operations for example we set up utility functions for the resource allocation process while we devise production rules and specific inference engines based on temporal reasoning (Allen, 1984) for scheduling activities. Finally, most significant decisions involve an element of uncertainty: That is, the decision maker lacks information about some aspects of his problem. Rule-based systems operate deterministically in their own reasoning, however, they can be engineered to be effective in a particular uncertain domain (the best example is the Mycin approach with uncertainty factors). In relatively well understood, static domains, one can design systems to look for the most likely cause of a fault before those that are less likely, and then recommend the repair strategy most likely to be effective. Therefore explicit treatment is not always necessary for a system which has to deal with uncertainty. However, in many cases uncertainty is encountered at a deeper level. Uncertainty arises because the situation is new or has not been previously considered.

Representations of uncertainty must be based on the information and beliefs of a particular decision maker, and cannot be delegated to an expert. Finally, if there is an interaction between uncertainty, an individual's attitude toward risk, and the preferred course of action, then explicit consideration of uncertainty is needed.

## 3. Integration of decision theory

We start out from recent efforts to design computer systems for decision support based on decision theory (Holtzman, 1985; Shachter, 1986). More general systems can be established by starting from group decision theory (team theory) for distributed decision making (Gottinger, 1989).

The basic result of the axioms of decision theory is the existence of a value function for scoring alternative sets of outcomes under certainty and a utility function for scoring uncertain outcome bundles. If the decision maker accepts the axioms (say, Savage's axioms, Savage, 1954; Gottinger, 1980) in the sense that he would like his decision making to be consistent with these axioms, then the decision maker should choose that course of action which maximizes expected utility. The importance of these axioms is that encoding decision procedures based on these axioms provide a basis for recommendations by an intelligent decision aid under uncertainty. They provide an explicit set of norms by which the system will behave. Other authors have argued why an individual should accept the decision axioms for decision making (Savage, 1954; Holtzman, 1987). The acceptance of these axioms is implicit in the philosophy and design of decision methods described here. The use of value and utility functions as criteria for decision making has several advantages. If the function is continuous with respect to outcomes, then it is able to handle small differences in outcomes in a consistent manner. This allows the computerized aid to handle an essentially infinite number of possible outcomes, not just those prespecified, foreseen, and categorized by the system's designers.

In addition, an approach to decision making based on decision theory has a mechanism, at least in principle, for handling completely new decision situations. The theory ensures the existence of a value and utility function. If the current expression of the preferences in the system does not incorporate the attributes of a new decision situation, the system can resort to the construction of a higher level or more general preference structure. By following these principles we are able to use the richness of modern decision theory and their axiomatic foundation (Fishburn, 1988). We could even encode ethical principles into decision theory (Harsanyi, 1976) and therefore enrich rational decision making in more than one dimension.

If the preference structure can be generated with sufficient generally, then the decision system can attempt to encode attributes of the new situation in terms of the general function, and use the new expression as a basis for decision making in the new situation. The task of developing robust preference models by incorporating deep and fundamental trade-offs is a difficult one. Development and elicitation of utility functions which reflect trade-offs regarding life and death issues as well as other dissimilar attributes is complex (Keeney and Raiffa, 1976). For the foreseeable future, assessment of utility functions for decision aids will necessarily be domain dependent. In fact, the applicability of decision aids such as those envisioned here will, in all likelihood, be limited by the ability to assess an appropriate representation of preferences. Domains in which there is a well developed empirical and theoretical basis for development of utility functions (e.g. financial and engineering decision making and some areas in medicine) are most promising.

Thus the decision axioms, along with the fundamentals of first order logic, provide a normative basis for reasoning about decisions. It is in this light that both logical and probabilistic inference will be utilized in an intelligent decision system.

So far we have distinguished between the problem solving capabilities of rule-based expert systems on the one hand, model-based decision recommendations using decision theory on the other. The choice of an appropriate technique or set of techniques for a given decision situation depends on many factors relevant to a particular decision. These include:

(1) complexity of the situation;

(2) availability of alternatives;

(3) uncertainty with respect to the outcomes and relationships in the decision domain;

(4) strength of preferences with respect to alternative outcomes;

(5) magnitude of gain or loss possible in the decision;

(6) requirements of procedural rationality and strength of heuristics available.

It seems reasonable to make all these characteristics an intrinsic part of a modelling process for an intelligent DSS design (Jarke and Radermacher, 1988). Modelling processes of this sort could possibly be more abstractly dealt with by structural modeling (Geoffrion, 1989) which establishes general principles for handling model-based resource allocation and decision processes.

## 4. Decision model based representation

For decision making, a model consists of the following elements: (1) alternatives; (2) state descriptions; (3) relationships; and (4) preferences. There can be no decision without alternatives, the set of distinct resource allocations from which the decision maker can choose. Each alternative must be clearly defined. State descriptions are essentially collections of concepts with which the decision is framed. It includes the decision alternatives and the outcomes which are related to the choices. The state description forms the means of characterizing the choice and outcome involved in the decision. The state description is also intertwined with expression of relationships. Relationships are simply the mappings of belief in some elements of the state description to others. The relations could be represented as logic relations, if—then rules, mathematical equations, or conditional probability distributions. The final component of a decision model is preferences. These are the decision maker's rankings in terms of desirability for various possible outcomes. They include not only his rankings in terms of the various outcomes which may occur in a decision situation, but also his attitude toward risky outcomes and preferences for outcomes which may occur at various times. They also embody information identifying those factors in a decision situation that are of concern, whether a factor indicates a desirable or undesirable outcome, and how to make tradeoffs among alternative collections of outcomes.

## 5. Influence diagrams

## 5.1. Basic structure

As a computationally convenient way for a decision model based representation we deal with influence diagrams. We define the structure of influence diagrams (that in a superficial way resemble network flow representation, Ford and Fulkerson, 1962).

In other words, influence diagrams are network depictions of decision situations (Smith, 1988). Until recently, their primary use has been in the professional practice of decision analysis as a means of eliciting and communicating the structure of decision problems. Each node in the diagram represents a variable or decision alternative; links between nodes connote some type of influence. Decision makers and experts in a given domain can view a graphical display of the diagram, and readily apprehend the overall structure and nature of dependencies depicted in the graph. Recently, there has been additional attention devoted to influence diagrams based on their uses in providing a complete mathematical description of a decision problem and as representations for computation. In addition to representing the general structure of a decision model, information characterizing the nature and content of particular links is attached to the diagram (Howard and Matheson, 1981). The diagram then presents a precise and complete specification of a decision maker's preferences, probability assessments, decision alternatives, and states of information. In addition the diagrammatic representations can be directly manipulated to generate decision theoretic recommendations and to perform probabilistic inference. The formalism of belief networks (Pearl, 1988) are identical graphical constructs which express probabilistic dependencies (no preferences or decisions). At this point, already, it is worthy to point out that inference and decision procedures using influence diagrams appear to be NP-hard (Cooper, 1987). Therefore, for some complex, multiply connected networks, it may be necessary to use approximation algorithms. Approximation algorithms produce an inexact bounded solution, but guarantee that the exact solution is within those bounds. Following the notation of Shachter (1986) we define the syntax and semantics of influence diagrams.

![](/api/attachments/XHS7HGGQ/fulltext/images/735fe981a27f9f682df28c968360ef261a3fa3b86c36d3ae1adbfca549d16596.jpg)  
Fig. 1.

Definition 1. An influence diagram is an acyclic directed graph $G = (N, A)$ consisting of a set, N, of nodes and a set, A, of arcs.

The set of nodes, N, is partitioned into subsets V, C, and D. There is one value node in V, representing the objective of the decision maker. Nodes in C, the chance nodes, represent uncertain outcomes. Nodes in D, the decision nodes, represent the choices or alternatives facing the decision maker.

A simple diagram appears in fig. 1. By convention, the value node is drawn as a diamond, chance nodes are drawn as circles, and decision nodes are drawn as rectangles.

V is the value node, the proposition which embodies the objective to be maximized in solving the decision problem. C1 and C2 represent uncertainties and D represents the decision. The semantics of arcs in the graph depend on the type of the destination node. Arcs into value or chance nodes denote probabilistic dependence. These arcs will be referred to as probabilistic links. Arcs terminating in decisions indicate the state of information at the time a decision is made.

Thus, C1 is an uncertainty which is probabilistically influenced (conditioned) by C2 and the decision. The ultimate outcome V, depends on the decision D and C2.

Definition 2. Each node's label is a restricted proposition, a proposition of the form ( $p t_{1}t_{2}\ldots t_{n}$ ) where each $t_{i}$ is either an object constant or alternative set.

We now define a set $\Omega(i)$ and a mapping $\pi_{i}$ for each node.

Definition 3. The set $\Omega(i)$ is the outcome set for the proposition represented by node i. It is a set of mutually exclusive and collectively exhaustive outcomes for the proposition.

Definition 4. The predecessors of a node i are the set of nodes j with arcs from j to i.

Definition 5. The successors of a node i are the set of nodes j such that there is an arc from i to j.

The mapping $\pi_{i}$ depends on node type. The domain of each mapping is the cross product of the outcome sets of the predecessors of node i. Let the cross product of predecessors of i be CP(i) where

$$
\begin{array}{r l} \mathrm{CP} (i) = & \left\{\Omega (i _ {1}) \times \Omega (i _ {2}) \dots \times \Omega (i _ {n}) \mid \right. \\ & \text { nodes } i _ {1}, \ldots , i _ {n} \in \text { predecessors } \\ & \text { of   node } i \}. \end{array}
$$

The range of each mapping $\pi_{i}$ depends on the type of node i.

## 5.2. Transformations

An influence diagram is said to be a decision network if: (1) it has at least one node; and (2) if there is a directed path which contains all the decision nodes (Pearl, 1988; Howard and Matheson, 1981). The second condition implies that there is a time ordering to the decision, consistent with the use of an influence diagram to represent the decision problem for an individual. Furthermore, arcs may be added to the diagram so that the choices made for any decision are known at the time any subsequent decision is made. These are no-forgetting arcs, in that they imply the decision maker remembers all of his previous selections for decisions, and has not forgotten anything that was known at the time of a previous decision.

The language of influence diagrams is a clear and computable representation for a wide range of complex and uncertain decision situations. The structure of dependencies (an lack thereof) is explicit in the linkages of the graph, as are the states of information available at each state in a sequence of decisions. The power of the representation lies, in large part, in the ability to manipulate the diagram to either express an alternative expansion of a joint probability distribution underlying a particular model, or to generate decision recommendations. The basic transformations of the diagram required to perform these operations are node removal and arc reversal.

These operations will be illustrated and defined with respect to a generic set of node labels: i and j are chance nodes, v is the value node. The labels p1, p2, and p3 will in general represent groups of predecessors of i, j, or v as indicated by the figures. In the interest of simplifying the descriptions of the operations, they will be treated as individual nodes. More detailed descriptions of these operations appear in Shachter (1986), Smith (1988).

Removal of a stochastic chance node i, which is a predecessor of a value node v, is performed by taking conditional expectation. (See fig. 2.) The new expected value function for v is calculated as follows

![](/api/attachments/XHS7HGGQ/fulltext/images/d55be93b2d533970d78d412904212441143116d2c0097fa139f881c7738b11dd.jpg)  
Fig. 2.

![](/api/attachments/XHS7HGGQ/fulltext/images/73fda74c246a586d0b05c4b6fb159a4fd3da29ab913aeda6bdb6a762bef0676b.jpg)  
Fig. 3.

$$
\begin{array}{l} \pi_ {\text {new}, v} (\omega_ {p 1}, \omega_ {p 2}, \omega_ {p 3}) \\ = \sum_ {\omega_ {i} \in \Omega (i)} \pi_ {\text {old}, v} (\omega_ {p 1}, \omega_ {p 2}, \omega_ {p 3}) \\ \times \pi_ {i} (\omega_ {i} | \omega_ {p 1}, \omega_ {p 2}). \end{array}
$$

The value nodes new predecessors are $p1$ , $p2$ , and $p3$ .

Removal of a deterministic chance node, i, which is a predecessor to the value node, v, is performed by substitution. The picture of this process is the same as the previous case. The new expected value function for v is

$$
\begin{array}{l} \pi_ {\text {new}, v} (\omega_ {p 1}, \omega_ {p 2}, \omega_ {p 3}) \\ = \pi_ {\text {old}, v} \big (\pi_ {i} (\omega_ {p 1}, \omega_ {p 2}), \omega_ {p 2}, \omega_ {p 3} \big). \end{array}
$$

Removal of a stochastic chance node, i, which is a predecessor to another chance node, j, is also performed by taking conditional expectation. (See fig. 3). The new distribution for successor node j is calculated as

$$
\begin{array}{l} \pi_ {\text {new}, j} (\omega_ {p 1}, \omega_ {p 2}, \omega_ {p 3}) \\ = \sum_ {\omega_ {i} \in \Omega (i)} \pi_ {\text {old}, j} (\omega_ {j} | \omega_ {i}, \omega_ {p 2}, \omega_ {p 3}) \\ \times \pi_ {i} (\omega_ {i} | \omega_ {p 1}, \omega_ {p 2}). \end{array}
$$

The new predecessors of j are the predecessors of j other than i, that is, p1, p2 and p3.

Removal of a decision node, i, predecessor to the value node v is performed by maximizing expected utility. The decision node can only be removed when all of its predecessors are also predecessors of the value node; that is, the choice is based on the expectations for the value, given what is known. (See fig. 4). After removal the new expected value function for v is

$$
\pi_ {\text { new }, i} \left(\omega_ {p 2}\right) = \max _ {\omega_ {i} \in \Omega (i)} \left[ \pi_ {\text { old }, i} \left(\omega_ {i}, \omega_ {p 2}\right) \right].
$$

The new predecessors of v are the predecessors of i which are also predecessors of v, p2 as illustrated here. Note that there may be some informational predecessors of i, e.g. p1, which were not predecessors of v before the removal. The values of these variables are irrelevant to the decision, since the expectation for the value is independent of their values. The optimal policy for the decision i is

$$
\pi_ {i} = \underset {\omega_ {i} \in \Omega (i)} {\arg \max} \left[ \pi_ {\text { old }, v} (\omega_ {i}, \omega_ {p 2}) \right]
$$

This is the calculated $\pi_{i}$ for decision nodes. We will refer to this calculated mapping as the decision function for i, $\pi_{d,i}(\omega_{p2})$ . (See 6.3., Informational Influences.)

![](/api/attachments/XHS7HGGQ/fulltext/images/2058be87bf5d9e01b84afdaf3301ae20385936d5cf50fb9e1227d6f329c8e8d6.jpg)

Fig. 5.  
![](/api/attachments/XHS7HGGQ/fulltext/images/299b9766600f9cd1ef24cc317db232d4d1595125657679d26f42bec18f1856e9.jpg)

Reversal of a probabilistic link between chance nodes is an application of Bayes' rule. Reversing a link from node i to node j can be performed as long as there is not other path from i to j (this is necessary to prevent the reversal from creating a cycle). In reversing, the new conditional probability description for i and j are calculated as

$$
\begin{array}{l} \pi_ {\text {new}, j} \big (\omega_ {j} | \omega_ {p 1}, \omega_ {p 2}, \omega_ {p 3} \big) \\ = \sum_ {\omega_ {i} \in \Omega (i)} \pi_ {\text {old}, i} \big (\omega_ {j} | \omega_ {i}, \omega_ {p 2}, \omega_ {p 3} \big) \\ \times \pi_ {\text {old}, i} \big (\omega | \omega_ {p 1}, \omega_ {p 2} \big), \\ \pi_ {\text {new}, j} \big (\omega_ {i} | \omega_ {j}, \omega_ {p 1}, \omega_ {p 2}, \omega_ {p 3} \big) \\ = p _ {\text {old}, j} \big (\omega_ {j} | \omega_ {i}, \omega_ {p 2}, \omega_ {p 3} \big) \\ \times \pi_ {\text {old}, i} \big (\omega_ {i} | \omega_ {p 1}, \omega_ {p 2} \big) \\ / \pi_ {\text {new}, j} \big (\omega_ {j} | \omega_ {p 1}, \omega_ {p 2}, \omega_ {p 3} \big). \end{array}
$$

The operations of reversal and removal allow a well formed influence diagram to be transformed into another equivalent diagram. The original and the transformed diagrams are equivalent in two senses. First, the underlying joint probability distribution and state of information associated with each is identical, since the diagram expresses alternative ways of expanding a joint distribution into a set of conditional and prior distributions (Howard and Matheson, 1981). Second, the expectation for the value in the diagram and the sequence of recommended actions from decision node removal are invariant over these transformations (Shachter 1986; Holtzman, 1987). In the next section, we focus on applying a sequence of these manipulations to obtain these recommendations.

## 5.3. Solution procedures

On the basis of these manipulations, there exist algorithms to evaluate any well-formed influence diagram (Shachter, 1986). For purposes of probabilistic inference, we need two separate algorithms. In one version, which applies to well-formed diagrams, evaluation consists of reducing the diagram to a single value node with no predecessors, the value of which is the expected value of the decision problem assuming the optimal policy is followed. In the course of removing decisions, the optimal policy, i.e. the set of decision functions $\pi_{d,i}$ associated with each decision is generated. In the other algorithm, the objective is to determine the probability distribution for a variable, as opposed to its expected value. Both versions of the algorithm are described below.

## Procedure EXPECTED VALUE (diagram)

1 Verify that the diagram has no cycles.

2. Add no-forgetting arcs between decision nodes as necessary.

3. WHILE the value node has predecessors

3.1 IF there exists a deterministic chance node predecessor whose only successor is the value node, THEN Remove the deterministic chance node into the value node

ELSE

3.2. IF there exists a stochastic chance node predecessor whose only successor is the value node, THEN Remove the stochastic chance node into the value node

ELSE

3.3. IF there exists a decision node predecessor and all the predecessors of the value node are predecessors of the decision node, THEN Remove the decision node into the value node

## ELSE

## 3.4. BEGIN

3.4.1. Find a stochastic predecessor X to the value node that has no decision successors.

3.4.2. For each successor $S_x$ of $X$ such that there is no directed path from $X$ to $S_x$ . Reverse Arc from $X$ to $S_x$

3.4.3. Remove stochastic predecessor X

## 4. END

At the conclusion of the EXPECTED VALUE procedure, the value node has no predecessors, and its single value is the expected value of the value node. Optimal decision functions are generated in the course of removing the decision nodes. The algorithm to solve for a probability discription (or lottery) for a node is as follows

## Procedure PROBABILITY-DISTRIBUTION (diagram)

1. Verify that the diagram has no cycles.

2. IF the value node is deterministic, THEN convert to a probabilistic chance node with unit probability on deterministic values.

3. WHILE the value node has predecessors

3.1. IF there exists a deterministic chance node predecessor whose only successor is the value node, THEN Remove the deterministic chance node into the value node ELSE

3.2. IF there exists a stochastic chance node predecessor whose only successor is the value node, THEN Remove the stochastic chance node into the value node

## ELSE

3.3. IF there exists a decision node predecessor and all the predecessors of the value node are predecessors of the decision node, THEN Remove the decision node from the list of predecessor

## ELSE

## 3.4. BEGIN

3.4.1. Find a stochastic predecessor X to the value node that has no decision successors.

3.4.2. For each successor $S_{x}$ of $X$ such that there is no directed path from $X$ to $S_{x}$ . Reverse Arc from $X$ to $S_{x}$

3.4.3. Remove stochastic predecessor X

## 4. END

The termination of this procedure is a probabilistic chance node with probabilities over the alternative possible outcomes of the original value node. Note that if decision predecessors are encountered in the algorithm, the distribution will be conditioned on the possible choice of the decision variables. The procedure does not remove decision nodes or generate decision functions.

## 6. Decision logic and inference

The concepts developed above are now used to define a class of formulas (sentences) for decision domains. These formulas will be referred to as well-formed influences. A decision domain will be described in terms of a set of these well-formed influences.

Definition 6. If A is a proposition and B is a conjunction of propositions $B_{i}$ of the form $B_{1}B_{2}\ldots B_{n}$ , then the expressions $A|_{p}B \equiv \pi_{p}(A|B)$ , $A|_{i}B$ and AB are well-formed influences.

A well-formed influence is an analog to a Horn clause in conventional logic programming. We have extended the Horn clause expression to incorporate statements about conditional probability distributions and to express information availability for decision making. A Horn clause in logic programming is a disjunction of propositions, in which all propositions but one are negated. A Horn clause has the following form $Av \neg B_{1}v \neg B_{2}v \ldots v \neg B_{n}$ ,

or by De Morgan's Law $Av \neg (B_1 B_2 \ldots B_n)$

more familiar form as a rule $A(B_{1}B_{2}\ldots B_{n})$ which is read IF $B_{1}$ and $B_{2}$ etc. are true then A is true. Also by definition, all variables in a Horn clause are universally instantiated; that is, the sentence is true for any term that is substituted for a variable appearing in the formula.

The choice of Horn clauses as a basis for influences is made for three basic reasons. First, there is a well understood, complete set of procedures for Horn clause logical inference. Inference is complete in that any Horn clause that is logically implied by another set of clauses is provable from that set using these procedures (Gallier, 1986). The inference procedures developed for Horn clauses will be the starting point for the probabilistic and decision theoretic techniques which are developed later in this section.

Secondly, first-order logic and Horn clause logic have proved to be an extremely expressive and useful language in a wide variety of situations. Expressing knowledge in Horn clauses is the basis for the logic programming language PROLOG, and forms the underpinnings for many derivative rule-based inference systems (Kowalski, 1979). First order logic is also the basis for several approaches to deductive databases and therefore supports the implementation process.

Finally, there is a natural parallel between the structure of a Horn clause and that of a conditional probability distribution, allowing a straightforward extension from logical rules to probabilistic rules. The Horn clause relates the truth of a proposition $(A)$ to a conjunction of preconditions $(B_{1}B_{2}\ldots B_{n})$ while a conditional probability distribution relates a probability distribution to a state of information—also expressed as conjunction of events. The representation of influences based on Horn clauses therefore rests on three pillars—computability, expressibility, and extensibility.

The proposition A (a single proposition) is referred to as the consequent of the influence and the conjunction B as the antecedent of the influence. We now describe in more detail the interpretation of each element of a well-formed influence (Breese and Tse, 1987).

## 6.1. Logic influences

A logical influence is an implication formula of the form $A \leftarrow B$ .

This expression is a logical conditional, i.e., an IF-THEN rule. A logical influence with an empty antecedent is the assertion of a fact, i.e. a fact which is unconditionally true.

We can interpret logical statements in terms of zero-one probabilities. The correspondence between a logic statement of the form $A \leftarrow B$ and a conditional probability function $\pi(A \mid B)$ can be developed.

## 6.2. Probabilistic influences

A probabilistic influence, incorporating a probabilistic connector, $|_{p}$ , and a probability distribution is of the form

$$
A \mid_ {\mathrm{p}} B \equiv \pi_ {\mathrm{p}} \left(\omega_ {A} \mid \omega_ {B}\right).
$$

This sentence is the probabilistic analog to a deterministic logical influence. The left-hand side of the influence expresses the fact that the probability distribution over the alternative outcomes of A may be dependent on the outcome of B. The right hand side of the influence, $\pi_{\mathrm{p}}(\omega_{A}|\omega_{B})$ , provides the numerical values of the distribution. It can be interpreted as providing the probability distribution over the outcomes of A for a given outcomes of B.

Just as logical influences express a means of asserting facts with certainty given other facts, a probabilistic influence expresses a measure of belief in a proposition given other facts. Suppose one desires to express the uncertainty of tomorrow's weather. Furthermore, we wish to condition the probability assessment for tomorrow's weather given the values of today's weather and a forecast of the weather of tomorrow. This can be expresses as follows

$$
\left(\text { WEATHER } x \text { TOMORROW }\right) | _ {\mathrm{p}}
$$

$$
(\text { WEATHER } y \text { TODAY })
$$

$$
(\text { FORECAST } z \text {   TODAY })
$$

$$
\equiv \pi_ {\mathrm{p}} (\omega (\text { WEATHER } x \text { TOMORROW }) | \omega
$$

$$
(\text { WEATHER } y \text { TODAY })
$$

$$
(\text { FORECAST } z \text {   TODAY })
$$

where $x, y, z \in \{fair, cloudy, rainy\}$ (the alternative set) and the w are members of the alternative outcomes for each proposition.

A probabilistic influence with an empty antecedent is the assertion of a prior (unconditional) probability distribution. For example

$$
\begin{array}{l l} \forall y (\text { WEATHER } x y) | _ {\mathrm{p}} \\ \equiv \pi_ {\mathrm{p}} (\omega (\text { WEATHER } x y)) = \\ \omega & \mathrm{p} (\omega) \\ (\text { WEATHER FAIR } y) & 0. 3 \\ (\text { WEATHER CLOUDY } y) & 0. 2 \\ (\text { WEATHER RAINY } y) & 0. 5 \end{array}
$$

Notice that in this example y is universally quantified—this is an assertion that for any value for y, the given probability distribution holds.

## 6.3. Informational influences

An informal influence uses the informational connector $\big|_{i}$ to express information availability $A\big|_{i}B$ .

This sentence denotes an informational influence and is only relevant in the context of decision making. The statement conveys two important pieces of information. The first is that A (a restricted proposition) is a proposition that is under the decision maker's control. The outcome of A from the set $\Omega(A)$ is not stochastic, but rather is selected by the decision maker. Thus as opposed to being the direct consequence of other outcomes (as in logic influences) or uncertain but conditionally dependent on other outcomes (as in probabilistic influences), its outcome is chosen from the set of alternative outcomes by the decision maker. Second, the propositions in B are known at the time the decision about A is made. Since the propositions may in general be probabilistic, this statement asserts that any uncertainties about their outcomes (within $\Omega(B)$ ) will be resolved by the time a commitment on A is made.

Suppose the decision is the choice among alternatives for a rocket launch. The informational influence

$$
\forall t ((\text { MISSION - CONTROL } z t) | _ {i}
$$

(WEATHER y t))

says that the launch decision for any time t is made knowing that day's weather.

An informational influence is purely descriptive. In no way it indicates what should be done in light of some other objectives. It differs from the other two types of influence in that they have some direct interpretation in terms of inference—knowing the antecedent of a logical or probabilistic influence tells something about the consequent, regardless of other information. Informational influences have inferential consequences only in the context of evaluating a situation for an optimal sequence of decisions. That is, only within the broader context of a decision model can one make a prescription regarding what choice should be made.

A function $\pi_{d,A}(\omega_{B})$ is generated corresponding to an informational influence as a result of an optimization over the decision alternatives in terms of the decision model. In general, it will be a deterministic function mapping elements of $\Omega(B)$ —what is known—to the elements of $\Omega(A)$ —what can be done.

## 6.4. Decision language

Recall the elements that are necessary to represent a decision domain: Alternatives, state descriptions, and preferences. We will summarize by indicating how each element of a decision description can be expressed with respect to the constructs generated above.

First, recall that propositions form the basic unit of representation for a decision domain. There are three levels of knowledge regarding a proposition expressible in the language. First, it is possible to express a fact for a proposition, that is, a set of values for the variables (as in a fact substitution) in the proposition that are asserted to be true with certainty. Second, the values of the variables in a proposition may be restricted to some set. Thus, the outcomes for that proposition are restricted to a collectively exhaustive, mutually exclusive set, termed the alternative outcomes. Finally, a probability distribution can be used to associate each possible outcome with a probability. We have also shown how probability distributions and outcome sets are expressed for conjunctions of propositions.

Alternatives, the decision maker's options, are expressed in the set of outcomes for a proposition which is the consequent of an informational influence. The fact that a proposition has alternative outcomes and is the consequent of an informational influence defines it as a decision proposition. State descriptions consist of the set of facts and probabilities expressed within or deducible from a domain description. Relationships between states are expressed by the various types of influences available in the language; the logic, probabilistic, and informational influences expressed for the domain. Preferences are handled by identification of a particular proposition whose outcome incorporate the decision maker's objectives. A real valued variable in the proposition is identified as the objective, i.e. the value to be maximized or minimized. A logical influence is defined which is capable of computing this value as a function of other propositions in the domain.

## 6.5. Example: A decision process

This section presents a simple example, using the decision language to describe a specific subproblem in a decision domain. Consider a security trader dealing in a single instrument, perhaps a particular Treasury security issue or foreign currency. The dealer's task is to trade continually in the instrument in order to make a profit. The trader's decisions are what quantity of the security to buy or sell at each instant of the trading day. The fundamental strategy is to buy low, sell high, which is considerably easier to write down than to execute. The dealer's primary uncertainty is what the price of the security will be in the future. Changes in the price are dynamic and dependent on the price in previous periods as well as some other economic conditions or market factors. The trader wishes to maximize his expected profit at some terminal time (Cohen et al., 1982).

The following basic decision alternatives represent the trader's decision to buy, sell, or do nothing (hold) in each trading period. The set of propositions for this situation is shown below along with an interpretation for each. Alternative values for restricted variables are shown in brackets { }. These propositions constitute the means of expressing state descriptions for this domain: (PROFIT profit time)

Trader's net profit. This is the cumulative total of all the trader's gains and losses in terms of profits since trading was initiated.

(POSITION value time)

Trader's net holding of the security. This is the cumulative total of all the trader's sales and purchases in terms of units of the security.

(TRADE{BUY SELL HOLD} time)

Trader's decision alternatives.

(PRICE{90 91 92} time)

Range of security prices. This is a restriction on the assumed range of prices that the instruments can adopt.

(FUTURES-EXPIRE time)

Futures contract expiration. Futures are contracts for the delivery of a given security at a future data. Standard security future contracts expire on a predetermined data (e.g. the 3rd Friday in March, June, September, etc.). This proposition is true if “time” occurs on a date when futures contracts mature.

(FUTURES-VOLUME{HEAVY MODERATE} time)

Indicator of activity level for futures markets. The level of activity in futures affects the levels of activity and prices in the “cash” market (i.e. for current delivery) that is considered in this example.

(GURU{BULLISH BEARISH} time)

Forecast by a market prognosticator or analyst. This represents the information of some outside expert. The “guru” is “bullish” if he believes prices are likely to rise, and is “bearish” if prices are thought to fall.

We now describe the set of relationships which characterize this domain.

The trader's profit and position are simply accounting relations, expressed as deterministic influences. We assume an initial position of zero units of the security, an initial profit of zero dollars, and a single trade quantity of 100 units. The facts (PROFIT 0.0 0) $\leftarrow$ and (POSITION 0.0 0) $\leftarrow$ indicate the trader starts with no holdings and no profit.

The net position of the trader is the difference between total sales and total purchases by the trader and depends on the trade made in the current period and net holdings in the previous period.

(POSITION new-position time)

← (-time 1 last-time) ∧

(POSITION old-position last-time) ∧

(TRADE BUY time) ∧

(+old-position 100 new-position)

```txt
(POSITION new-position time)
← (-time 1 last-time) ∧
(POSITION old-position last-time) ∧
(TRADE SELL time) ∧
(-old-position 100 new-position)
(POSITION new-position time)
← (-time 1 last-time) ∧
(POSITION old-position last-time) ∧
(TRADE HOLD time)
```

The profit level at any time is composed of the profit the trader has accumulated so far, plus an adjustment for the amount of the security the trader is holding (net position). If we identify maximizing profit as the objective of the trader, then his preferences among various outcomes (for PRICE, PROFIT, and POSITION) in terms of other propositions are expressed by the logic influence

(PROFIT new-profit time)

← (-time 1 last-time) ∧

(PROFIT old-profit last time) ∧

(PRICE old-price last time) ∧

(PRICE price time) ∧

(POSITION old-position last time) ∧

(-price old-price change-in-price) ∧

(\*old-position change-in-price change-in-value) ∧

(+old-profit change-in-value new-profit)

The PRICE proposition is the uncertain proposition in this example. The conditional probability distribution for PRICE is expressed by a series of probabilistic influences. A simple influence is

(PRICE new-price time) $|_{p}$

(-time 1 last-time) ∧

(PRICE old-price last-time)

$= \pi_{\mathrm{p}}(\omega (\mathrm{PRICEnew - price time})|\omega$

(FUTURE-ACTIVITY level time)).

This influence expresses a simple stochastic update of price given the previous period's price. If futures contracts for the security expire in a particular period, then the price is independent of the old price and is expressed by a different distribution

(PRICE new-price time) $|_{p}$

(FUTURES-EXPIRE time) ∧

(FUTURES-ACTIVITY level time)

$= \pi_{\mathrm{p}}(\omega (\text {PRICE new - price time})|\omega$

(FUTURES-ACTIVITY level time)).

Note that since (FUTURES-EXPIRE time) is not restricted, the conditional probability distribution $\pi_{p}$ will not have separate entries for alternative outcomes of (FUTURES-EXPIRE time), therefore the distribution can be written solely in terms of the alternative outcomes for (FUTURES-ACTIVITY level time). The term (FUTURES-EXPIRE time) is a condition that must be true for the conditional probability distribution $\pi_{p}()$ to be applicable. Note that the representation allows the expression of several conditional distributions simultaneously, and allows for the expression of conditions redarding which of the alternatives is appropriate by interweaving of deterministic information (e.g. FUTURES-EXPIRE) and uncertain outcomes (e.g. PRICE).

The trader also has information available from the market analyst (the GURU) regarding his view of the market is being bullish or bearish. The guru therefore provides the trader with a indicator of overall market trends. The trader's opinion of this expert is expressed in the following influence

(GURU assessment time) $|_{p}$

(+time 1 next-time) ∧ (PRICE price time) ∧ (PRICE next-price next-time)

$= \pi_{\mathrm{p}}(\omega (\mathrm{GURU assessment time})|\omega$

(PRICE price time) ∧

(PRICE next-price next time)).

This influence expresses the trader's probability distribution with respect to the guru's forecast for each possible set of prices for the current and subsequent period (i.e. the alternative outcomes of (PRICE price time) ∧ (PRICE next-price next-time)).

The final component indicates the decision in this domain and the information available. The influence states that at time 2 the trader knows the price and guru assessment.

(TRADE action 2) $|_{i}$ (GURU assessment 2) $\wedge$ (PRICE price 2)

For all periods, the trader knows the price when making a trade.

(TRADE action time) $|_{i}$ (PRICE price time).

These other facts and priors define the state of knowledge base at a given time. For example (PRICE price 0) $|_{p} \equiv \pi_p(\omega(PRICE\ price\ 0))$ (FUTURES-ACTIVITY level time) $|_{p} \equiv \pi_p(\omega(FUTURE-ACTIVITY\ level\ time))$ (FUTURES-EXPIRE 2) $\leftarrow$ .

The first two statements express prior probability distribution for prices at time zero, and futures activity for any period respectively. The last is a fact expressing that futures expire in period 2. The statements above, plus the values making up the probability distributions $\pi_{p}()$ constitute the representation of this domain. The statements in this example are listed in the Appendix.

## 7. Summary and conclusions

The techniques presented here are grounded on the premise that for effective intelligent decision support, the representation of a decision situation in a computer must reflect the alternatives, beliefs, and preferences of the user of the system. Therefore, the approach developed here focuses on the development of representations and techniques which construct a probabilistic or decision-theoretic model for a particular user, query, and state of information, and support the exploration of alternative representations and models for various phenomena by the user.

Central to the development of powerful computer-based decision aids is a means of expressing information and relationships important to describing a particular decision domain. We sketched a language based on first-order logic for the description of states, alternatives, beliefs and preferences associated with a decision domain and decision maker. The language includes constructs for explicitly enumerating the alternative possible outcomes for uncertain propositions, probability distributions over these outcomes, the choices facing the decision maker, and his preferences regarding alternative outcomes of differing likelihood. The concept of a logic rule has been generalized to provide for the expression of conditional probabilities (i.e. the probability of a proposition over its alternative outcomes given some conjunctions of propositions is true) and of information availability at the time of decision.

The current system relies on influence diagrams as a formalism for representing decision problems, and the algorithm developed by Shachter to solve for the optimal sequence of decisions. These techniques, while general, are inefficient for some problems, especially those which exhibit special structure that can be exploited in generating a solution. For example, recognition of separability of the value function in a Markov decision problem allows one to solve stochastic optimization problems using dynamic programming techniques. In addition, recent work on computational procedures for evaluating influence diagram (Chavez and Cooper, 1988) can also make the process more efficient in view of complexity bounds given by NP-hardness issues. In particular, KNET is a successful example of an IDSS that integrates decision networks and traditional expert systems. Other formal representations of decision problems, for example linear or non-linear program, may be appropriate in some domains. Of particular interest are multi-person control or decision problems such as team theory or special organizational representations of command and control problems (Levis, 1984; Marschak and Radner, 1972) that are decision theoretic generalizations of the basic structure of decision theory (Savage, 1954).

The final basic area for future research is the incorporation of the ideas and concepts developed in this paper into artificial intelligence theories for autonomous rational agents. Currently, work in this area attempts to develop theories for belief, belief modification, goals, and action using classical logic and its extensions as a formalism (Georgeff, 1986; Rosenschein, 1985). Basing a theory of rationality on single person decision theory has several advantages:

(1) It provides an axiomatic basis for action;

(2) it insures the existence of a utility function providing a mapping from uncertain outcomes and decisions to preferences;

(3) it incorporates well grounded techniques for developing optimal strategies, handling uncertainty and risk preference, and calculation of the value of perfect and imperfect information;

(4) there exist well-tested methods and techniques application of decision-theoretic ideas to real world problems based on the professional practice of decision analysis and other system sciences (Holtzman and Breese, 1986; Howard and Matheson, 1984).

Such a theory should be flexible enough to allow for bounded rationality concerns (Simon, 1978; Gottinger, 1982). We should note that all decision making support by a computer aid reflects limited rationality to some degree. Even the most sophisticated DSS conceivable is limited in that it is based on a model, which by definition is an abstraction of reality and therefore contains inaccuracies due to cognitive limitations. The perfect or complete IDSS is an unattainable ideal.

## References

J.F. Allen, Towards a General Theory of Action and Time, Artificial Intelligence, Vol. 33, No. 2, (1984).

J. Breese and E. Tse, Integrating Logical and Probabilistic Reasoning for Decision Making, AAAI, Third Workshop on Uncertainty in AI, Seattle, pp. 355–362 (1987).

R.M. Chavez and G.F. Cooper, KNET: Integrating Hypermedia and Bayesian Modeling, AAAI, Fourth Workshop on Uncertainty in AI, Minneapolis, pp. 49–54 (1988).

W.J. Clancey, Heuristic Classification, Artificial Intelligence 27, pp. 289–310 (1985).

J.B. Cohen, E. Zinbarg, and A. Zeigel, Investment Analysis and Portfolio Management, (Irwin, Homewood, IL, 1982).

G.F. Cooper, Probabilistic Inference Using Belief Networks is NP-hard, Report KSL-87-27, Medical Computer Science Group, Stanford Univ., Stanford, Ca. (1987).

P.C. Fishburn, Nonlinear Preference and Utility Theory, (The Johns Hopkins Univ. Press, Baltimore, MD, 1988).

L.R. Ford and D.R. Fulkerson, Network Flows, Princeton Univ. Press (Princeton, N.J. 1962).

A.M. Geoffrion, The Formal Aspects of Structural Modelling, Operations Research 37 (1), pp. 30–51 (1989).

M. Georgeff, The Representation of Events in Multiagent Domains, AAAI-86: Proceedings of the Fifth National Conference on Artificial Intelligence, Philadelphia, P.A., pp. 70–75 (1986).

H.W. Gottinger, Elements of Statistical Analysis, (DeGruyter, Berlin, 1980).

H.W. Gottinger, Computational Costs and Bounded Rationality, In Stegmüller, W. and W. Spohn, eds., Philosophy of Economics, Springer (1982).

H.W. Gottinger, Decision Making in Large Systems, International Conf. on Organizations and Information Systems, Bled, Yugoslavia (1989).

O. Hannson and A. Mayer, The Optimality of Satisficing Solutions, AAAI, Fourth Workshop on Uncertainty in AI, Minneapolis, pp. 148–157 (1988).

J. Harsanyi, Essays on Ethics, Social Behavior and Scientific Explanation (Reidel, Dordrecht, 1976).

S. Holtzman, Intelligent Decision Systems, Addison-Wesley, (Reading, 1987).

S. Holtzman and J.S. Breese, Exact Reasoning about Uncertainty: On the Design of Expert Systems for Decision

Support, In Kanal and Lemmer, eds., Uncertainty in Artificial Intelligence, pp. 339–346 (Amsterdam, North Holland, 1986).

R.A. Howard and J.E. Matheson, Influence Diagrams, 1981, In Howard, R.A. and J.E. Matheson, eds., The Principles and Applications of Decision Analysis, SDG Publications, Strategic Decisions Group (Menlo Park, California, 1984).

M. Jarke and F.J. Radermacher, The AI Potential of Model Management and its Central Role in Decision Support, Decision Support Systems, 4 (4) (1988).

R.L. Keeney and H. Raiffa, Decisions with Multiple Objectives: Preferences and Value Tradeoffs, (Wiley, New York, 1976).

A.H. Levis, A Mathematical Theory of Command and Control Structures, Lab. for Information and Decision Systems, M.I.T., LIDS-FR-1393, Cambridge, Mass. (Aug. 1984).

J. Marschak and R. Radner, Economic Theory of Teams, (Yale Univ. Press, New Haven, Conn., 1972).

H.P. Nii, Blackboard Systems: The Blackboard Model of Problem Solving and the Evolution of Blackboard Architectures, AI Magazine 7 (2) pp. 38–53 (1986).

D. Patrick, Artificial Intelligence, Applications in the Future of Software Engineering (Ellis Horwood, Chichester, 1986).

J. Pearl, Probabilistic Systems in Artificial Intelligence, (Morgan Kaufmann, Los Altos, Ca., 1988).

J.S. Rosenschein and M.R. Genesereth, Deals among Rational Agents, Proc. Ninth Intern. Joint Conf. A.I., Los Angeles, pp. 91–99 (1985).

L.J. Savage, The Foundations of Statistics, (Wiley, New York, 1954).

H.A. Simon, How to decide what to do, Bell Jour. of Economics 8 (1978).

J.Q. Smith, Decision Analysis: A Bayesian Approach, (Chapman and Hall, London 1988).

R.D. Shachter, Evaluating Influence Diagrams, Operations Research, 34 (1986)

## Appendix A

Influences for trading example:

(TRADE{BUY SHELL HOLD} time) ←

(A1)

(PRICE{90 91 92} time) ← (A2)

(FUTURES-VOLUME

{HEAVY MODERATE} time) ← (A3)

(GURU{BULLISH BEARISH} time) ← (A4)

(PROFIT 0.0 0) $\leftarrow$ (A5)

(POSITION 0.0 0) ← (A6)

(POSITION new-position time)

← (-time 1 last-time) ∧
(POSITION old-position last-time) ∧ (A7)
(TRADE BUY time) ∧
(+old-position 100 new-position)

(POSITION new-position time)
← (-time 1 last-time) ∧
(POSITION old-position last-time) ∧ (A8)
(TRADE SELL time) ∧
(-old-position 100 new-position)
(POSITION old-position time)
← (-time 1 last-time) ∧
(POSITION old-position last-time) ∧ (A9)
(TRADE HOLD time)
(PROFIT new-profit time)
← (-time 1 last-time) ∧
(PROFIT old-profit last-time) ∧
(PRICE old-price last-time) ∧
(PRICE price time) ∧
(POSITION old-position last-time) ∧ (A10)
(-price old-price change-in-price) ∧
(\*old-position change-in-price change-in-value) ∧
(+old-profit change-in-value new-profit)
(PRICE new-price time) |p
(FUTURES-EXPIRE time) ∧
(FUTURES-ACTIVITY level time) (A11)
= πp(ω(PRICE new-price time) | ω
(FUTURES-ACTIVITY level time)) (A12)

(PRICE new-price time) | $_{p}$ (FUTURES-EXPIRE time) ∧
(FUTURES-ACTIVITY level time)
= π $_{p}$ (ω(PRICE new-price time) | ω
(FUTURES-ACTIVITY level time))
(GURU assessment time) | $_{p}$ (+time 1 next-time) ∧
(PRICE price time) ∧
(PRICE next-price next-time) (A13)
= π $_{p}$ (ω(GURU assessment time) | ω
(PRICE price time) ∧
(PRICE next-price next time))
(TRADE action 2) | $_{i}$ (GURU assessment 2) ∧
(PRICE price 2) (A14)
(TRADE action time) | $_{i}$ (PRICE price time)
(A15)
(PRICE price 0) | $_{p}$ ≡ π $_{p}$ (ω(PRICE price 0))
(A16)
(FUTURES-ACTIVITY level time) | $_{p}$ ≡ π $_{p}$ (ω(FUTURE-ACTIVITY level time))
(A17)
(FUTURES-EXPIRE 2) ← (A18)

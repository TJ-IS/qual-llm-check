---
otero_id: 10976
otero_key: "5KUX5WEG"
title: "Decision maps: A framework for multi-criteria decision support under severe uncertainty"
authors: "T. Comes; M. Hiete; N. Wijngaards; F. Schultmann"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.05.008"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision maps: A framework for multi-criteria decision support under severe uncertainty

T. Comes <sup>a,</sup>⁎, M. Hiete <sup>a</sup>, N. Wijngaards <sup>b</sup>, F. Schultmann

<sup>a</sup> Institute for Industrial Production (IIP), Karlsruhe Institute of Technology (KIT), Hertzstr. 16, D-76187 Karlsruhe, Germany <sup>b</sup> Thales Research & Technology Netherlands/d-cis Lab, PO Box 90, NL-2600 AB, Delft, The Netherlands

## a r t i c l e i n f o

Article history: Received 8 April 2010 Received in revised form 6 May 2011 Accepted 23 May 2011 Available online 12 June 2011

Keywords: Multi-Criteria Decision Analysis Scenario-based decision support Severe uncertainty Causal Maps

## a b s t r a c t

In complex strategic decision-making situations the need for well-structured support arises. To evaluate decision alternatives, information about the situation and its development must be determined, managed and processed by the best available experts. For various types of information different reasoning principles have been developed: deterministic, probabilistic, fuzzy and techniques for reasoning under ignorance (i.e., the likelihood of an event cannot be quanti<sup>fi</sup>ed). We propose a new approach based on Decision Maps supporting decision makers under fundamental uncertainty by generating descriptions of different possible situation developments (scenarios) in a distributed manner. The scenarios are evaluated using Multi-Criteria Decision Analysis techniques.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

In complex strategic decision-making situations often decisions among a <sup>fi</sup>nite set of feasible alternatives respecting multiple con<sup>fl</sup>icting objectives must be made [3]. Multi-Criteria Decision Analysis (MCDA) supports decision makers in these situations [77], as it allows for a transparent evaluation of alternatives. Yet, the use of MCDA can be problematic when uncertainties are signi<sup>fi</sup>cant [22]. Uncertainties, however, play an important role in most strategic decision-making situations, as information is often imprecise, uncertain or lacking [50]. Decision-making is particularly challenging when severe uncertainties forestalling to judge and quantify the likelihood of relevant events persist [4]. To describe and operationalise a lack of knowledge, this paper adopts the terminology introduced by Knight [41], which is still commonly used in today's decision theory (e.g., [14,50,57]). The terms risk, uncertainty and ignorance have the following precise meanings:

• In decisions under risk the decision makers know the probability of the possible outcomes.

• In decisions under ignorance these probabilities are either unknown or non-existent.

• Uncertainty is used as a broad term referring to both risk and ignorance. In this thesis, the latter de<sup>fi</sup>nition is used.

Scenarios offer a possibility to deal with severe uncertainties as they explore fundamentally different descriptions of a situation and its possible developments [65]. Being plausible, consistent and coherent [64], scenarios appeal to decision makers and help in overcoming cognitive biases such as overcon<sup>fi</sup>dence or misjudgement of likelihoods [79]. To construct scenarios describing a large and complex decision problem, knowledge and expertise from various domains have to be brought together [50,68].

In this paper a new approach for decision support under heterogeneous types of uncertainty in distributed settings is presented. Decision Maps, a new framework facilitating scenario construction and assessment with MCDA techniques combine Directed Acyclic Graphs (DAGs) used to manage information distribution and processing, and MCDA evaluation structures.

Although there are approaches exploiting DAGs for multi-criteria decision support (such as Bayesian Networks [76] and Causal Maps [46,48]) or more general graphs with feedback loops (Fuzzy Cognitive Maps [73,80] or System Dynamics [7,62]), until now there is to our best knowledge no approach exploiting these structures for distributed scenario construction. (For a more detailed discussion on the combination of network structures and MCDA see Section 2.3.) Furthermore, each of these approaches makes use of one and only one paradigm for reasoning under uncertainty. Decision Maps allow for handling multiple of these paradigms at a time according to the information and expertise available. Lastly, although recently a small number of approaches evaluating scenarios with respect to multiple goals have been developed [19,31,33,46], none of these systematically integrates scenario construction and evaluation of alternatives. In our framework, Multi-Attribute Value Theory (MAVT) provides a rationale for constructing decision-relevant scenarios. In this manner, the problem structuring techniques of MAVT are used as a means to structure and manage information processing. This enables reducing information overload of the experts involved in the scenario construction process and the decision makers, to whom the <sup>fi</sup>nal results are presented.

In this paper we focus on the (technical) framework for using Decision Maps to support Scenario-Based Multi-Criteria Decision Analysis. Speci<sup>fi</sup>cally, the topics of heterogeneous information as well as the construction of scenarios that ful<sup>fi</sup>l general requirements enhancing their acceptance (namely, plausibility, coherence and consistency) are addressed, as the scenarios form the foundation for the decision analysis. Furthermore, the management of the number of scenarios under consideration is discussed, as the control of the potential combinatorial explosion is a requirement for practical operationalisation [58]. Scenario management processes that are currently available are often not properly supported by available techniques and tools [1]. Both topics are described using lightweight formalisations. Our approach is illustrated by a small cut-out of a larger case-study under investigation. In this paper, we presume that, for the decision problem at hand the alternatives to choose among, a hierarchical structure of objectives and the preferences with respect to each of the objectives can all be elicited from the responsible decision makers. These assumptions ensure the applicability of MAVT approaches. Additionally, it is assumed that experts establishing the consequences of the application of an alternative are available, ensuring the con<sup>fi</sup>guration of information processing work <sup>fl</sup>ows [53].

The remainder of this paper is structured as follows: the next section discusses MCDA (focusing on Multi-Attribute Decision Making techniques), scenario-based decision support and problem structuring techniques for representing interdependencies between different variables in<sup>fl</sup>uencing the decision. Subsequently, our novel Decision Map approach is introduced, and it is shown how decision makers are supported throughout all phases of the decision making process. Section 3 describes the problem structuring phase, i.e., the con<sup>fi</sup>guration of Decision Maps in distributed settings ensuring ef<sup>fi</sup>cient handling of information. Additionally, it is shown that Decision Maps facilitate combining several principles of reasoning under uncertainty. Section 4 treats the assessment of consequences. First, the Decision Map approach is exploited to construct relevant scenarios and a new method for keeping the number of scenarios manageable is introduced. Second, it is shown how the generated scenarios facilitate the evaluation of alternatives by using the MCDA part of the Decision Map. Particularly, we highlight methods to take the robustness of an alternative and the risk aversion of the decision makers into account. Section 5 illustrates the Decision Map approach by means of an emergency management example. The <sup>fi</sup>nal Section 6 discusses the approach presented, introduces future research directions and draws conclusions.

## 2. Strategic decision making under uncertainty

This section discusses the most relevant decision support techniques frequently applied to facilitate strategic decision making in complex situations: Multi-Attribute Decision Making, scenario-based decision support and problem structuring techniques for strategic decision making under uncertainty.

## 2.1. Multi-Attribute Decision Making

MCDA is a technique to compare a set of alternatives with respect to multiple objectives. To this end, abstract higher-level goals are expressed in terms of a number of more precise criteria [18,69]. When the decision consists of selecting one out of a <sup>fi</sup>nite set of feasible alternatives $A { = } \{ a _ { 1 } , { \ldots } , a _ { k } \}$ , techniques from Multi-Attribute Decision Making (MADM) can be applied [3]. Multi-Attribute Value Theory (MAVT) is targeted at decision making under certainty, where each alternative leads invariably to a speci<sup>fi</sup>c result. Conversely, Multi-Attribute Utility Theory (MAUT) is suitable for decision making under risk, where each alternative leads to a speci<sup>fi</sup>c probability distribution of the result.

In both MAVT and MAUT, the decision process starts by structuring the problem as an attribute tree hierarchically ordering the decision makers' aims at different abstraction levels, cf. Fig. 1. The tree shows how the overall goal is divided into criteria (possibly sub-criteria etc.), until the level of attributes is reached. It is generally assumed that each criterion can be operationalised by a set of measurable attributes allowing for assessing the consequences arising from the implementation of any particular alternative [69]. In the next step preferential information is elicited [76]. The relative importance of criteria in both MAVT and MAUT is captured in weights w<sup>l</sup> for each criterion j at each abstraction level l. (More precisely, the weights indicate the relative importance of changing the level of performance on the respective objectives from their worst to their best levels [58].)

To compare attributes that are measured on different scales in MAVT, the attribute scores $x _ { a j }$ (determined for each alternative a with respect to each attribute j) are normalised to values $\nu _ { a j } = \nu _ { j } ( x _ { a j } )$ (see Fig. 1). The value functions $\nu _ { j } { : } R \to [ 0 , 1 ]$ expresses how important it is to attain a performance that is close to the optimal possible one. The last step in MAVT is the weighted aggregation of performances to the total performance $t _ { a }$ taking into account the weights w<sup>l</sup> at each abstraction level l. In this manner, a ranking of alternatives is achieved.

MAUT addresses the problem of uncertain information using probabilistic techniques. The consequence vector for an alternative $a _ { i }$ contains the scores of attributes $j = 1 , . . . , n \colon x _ { a _ { i } } = ( x _ { a _ { i } 1 } , . . . x _ { a _ { i } n } ) .$ . In $\mathrm { M A U T } , x _ { a _ { i } }$ is considered a function of uncertain random factors with known density function $f ( x _ { a _ { i } } )$ . The expected utility of an alternative is $E ( u ( x _ { a _ { i } } ) ) = \int _ { R ^ { n } } u ( x _ { a _ { i } } ) f ( x _ { a _ { i } } )$ , where ${ \boldsymbol { u } } ( { \boldsymbol { x } } _ { a _ { i } } )$ is a utility function re<sup>fl</sup>ecting the decision makers' risk preferences [39]. It can be problematic to model the uncertainties on the attributes in this manner: <sup>fi</sup>rst, the use of probabilistic methods can hamper the acceptance, as it may lead to counter-intuitive results [38]. Second, constrictive independence assumptions on the attributes [3] need to be ful<sup>fi</sup>lled. Third, the elicitation of utility functions and the deduction of adequate distributions can be problematic, particularly if not only aleatory but also epistemic uncertainties prevail [3,11,35]. Lastly, when the decisions to be made concern rare events with low probability and important consequences, the use of expected values as a basis for the decision is contestable [44,79].

Another approach allowing for considering uncertainties is sensitivity analysis [61]. Sensitivity analyses varying the input parameters used for an initial result are usually applied ex post. Generally, these are targeted at testing robustness rather than exploring fundamentally different developments of a situation. Whilst standard sensitivity analyses vary only one parameter, there are approaches analysing the effects of simultaneous variations of multiple parameters using sampling techniques (e.g., Monte-Carlo methods [9]).

![](/api/attachments/5KUX5WEG/fulltext/images/a2f32d1f07730abd204046ba7f6ed7beaaff80b6ef5c3f0962ecc77900879e02.jpg)  
Fig. 1. Attribute tree: measurable attributes in gradient boxes, criteria and overall goa in white boxes. Dependence of attributes on the alternatives (represented as diamonds) is shown by dashed lines.

Although these methods have linear complexity, simulations become computationally expensive when the models themselves become increasingly complex [50], which is problematic when time is limited. Lastly, like most probabilistic methods the running of Monte-Carlo simulations is data-intensive. Consequently, these simulations usually cannot produce results unless a considerable body of empirical information has been collected, or unless the analyst is willing to make several assumptions in the place of such empirical information [24].

## 2.2. Scenario-based decision support

Scenarios are purposeful stories about a situation and how it could unfold over time in its contextual environment containing all elements relevant for a decision [79]. In this way, using scenarios enables taking into account not merely local perturbations but also profound changes of the system under scrutiny. Furthermore, scenarios help in overcoming cognitive biases such as overcon<sup>fi</sup>dence and facilitate the integration of fundamental risks with large impact but low likelihood into the decision making process [65]. Additionally, scenarios offer the possibility to consider and discuss several possible situation developments and facilitate con<sup>fl</sup>ict management between diverging preferences and value judgements by helping <sup>fi</sup>nding common ground for future action [75].

Whilst there are different approaches to constructing and using scenarios, we focus on systematic aspects of scenario planning and analysis [75], adopting the concept of “scenario” as used in combinatorial scenarios [50] and Formative Scenario Analysis [66], where a scenario describes the state of a system and its development by means of a set of impact variables.

Important requirements for a scenario's acceptance are [64,79]:

• Plausibility: the scenario does not go beyond the realm of possibility,

• Coherence: causal links explaining why a scenario arises are made explicit (particularly important in case a scenario seems to be unlikely),

• Consistency: the scenario is unambiguous (particularly, there are no con<sup>fl</sup>icts between the states of any sets of variables within one scenario).

Scenarios have been recommended as a tool to complement decision analysis as they are designed to challenge decision makers' perceptions of the future [78]. Recently few approaches evaluating scenarios with respect to multiple goals have been developed [19,33,46,59]. Yet, none of them systematically integrates scenario construction and evaluation of alternatives.

## 2.3. Problem structuring for strategic decision making under uncertainty

A number of problem structuring techniques representing explicitly relations between impact variables (termed “variables” in the following) have been developed. A common feature of these techniques is the representation of the problem as a network, depicting variables as nodes and the relations between them as arcs. Each of the techniques that are brie<sup>fl</sup>y discussed in this section relies on one unique principle for reasoning under uncertainty.

First, consider the nature of the interdependence relations: two events $x _ { i } = A$ and $x _ { j } = B$ are statistically related if the probability of their joint occurrence P(A∩B) does not equal the product of their individual probabilities P(A) P(B), [63]. Thus, if A is statistically related to B, then B is equally related to A. Therefore, statistical relations are symmetric. Contrarily, in decision making it is important to display cause–effect relations, as the decision makers need to know the impact of manipulating certain factors (by implementing an alternative) [43]. That is why displaying the relations between causes and effects as a network of directed arcs helps decision makers in evaluating alternatives [23].

Bayesian Networks describe interactions between variables in terms of (conditional) probability distributions [54]. The underlying probability judgements can only be made precisely if accurate data and models are available. When decisions on large and complex problems need to be made, however, there is usually not one selfcontained model covering the necessary domain knowledge for all eventualities [21], and the quality of the available data is heterogeneous [56]. Additionally, in strategic decision making the time is rather long until the impact of a decision can be observed, and the complex interdependencies between all relevant factors make it dif<sup>fi</sup>cult to attribute a consequence clearly to a decision made. Thus, the aforementioned conditions for accurate probability judgements are violated. Last, there are the problems of cognitive biases in the elicitation of probabilities (e.g., overcon<sup>fi</sup>dence in the quality of judgements, [26]) as well as in the understanding and interpretation of the possibly counter-intuitive results [5,72].

Cognitive or Causal Maps are discursive problem structuring techniques representing variables in a network of causes and effects. These techniques are suitable in situations, when the dependencies of variables can only be valued qualitatively, e.g., by labels indicating the direction of in<sup>fl</sup>uence (usually, + or −). If more information about the type and strength of in<sup>fl</sup>uence is available, a <sup>fi</sup>ner graduation of labels can be chosen. Alternatively, fuzzy membership functions can be used to model the relations leading to Fuzzy Causal Maps[55]. The in<sup>fl</sup>uence of the variables on each other (particularly, on a set of goal variables) can, for Causal Maps, be modelled by causal inference mechanisms [49], de<sup>fi</sup>ning partial and total effects on and of the variable on a path through the network. To calculate the partial and total effects, different operators have been discussed in [47]. For Fuzzy Causal Maps whose structure includes feedback loops, temporal aspects play a crucial role: given a set of initial values for each node within the Map (captured a state vector sv(0)), the development of the system's state is assessed by combining an incidence matrix W (weighted with the causal links' strengths) with a fuzzy transformation F. The system's state at a time t+ 1 is then derived from its state at t by setting $s v ( t + 1 ) = F ( s v ( t ) \cdot W ) \ [ 4 2 , 5 5 , 8 0 ]$

For each type of network, the respective inference mechanisms (be it conditional distributions for Bayesian Networks, in<sup>fl</sup>uence weights and causal inference operators for Causal Maps or weights and fuzzy transformations for Fuzzy Causal Maps) need to be de<sup>fi</sup>ned a priori requiring extensive discussion and time [12,34,40]. As a consequence, they are mainly applied in strategic decision making [48,67]. Whilst time-consuming discursive approaches elicit experts' knowledge each time a problem needs to be solved, automated expert systems standardise the results elicited in a knowledge-base [32,71]. By excluding human experts from the problem-solving process, autonomous expert systems provide results much faster than discursive techniques. However, these systems require a comprehensive knowledge-base covering all aspects of the tasks being performed [21]. This is infeasible in complex problems in a changing environment, as there will always be some relevant aspects that newly appear and/or have not (yet) been included [25].

Bayesian Networks, Causal and Fuzzy Causal Maps allow for modelling uncertainty by a single reasoning principle. In large and complex problems, however, information of diverse types typically coexists [20,56]. For some information, suf<sup>fi</sup>ciently rich statistics or accurate expert judgements may be available allowing for the deduction of conditional probability distributions and thus, the construction of Bayesian Networks. For other variables there may be vague and imprecise speci<sup>fi</sup>cations, which can be represented by fuzzy sets. Yet in other cases, information may be sparser or even lacking.

The Decision Map approach presented in this paper facilitates distributed reasoning. Therefore, it allows for partitioning the overall decision problem into a set of sub-problems. For each sub-problem, the reasoning principles applied can be chosen by the responsible experts according to the information (and time for further assessments) available, cf. Section 3.2 for a more detailed description on how Decision Maps can be used to handle heterogeneous types of information.

## 3. Problem structuring using Decision Maps

This section describes how the decision problem can be structured using Decision Maps broadening the basis of the decision support system by merging the Multi-Attribute Decision Making (MADM) attribute tree with a Directed Acyclic Graph (DAG) describing the problem on behalf of different interlinked relevant variables. A variable is deemed relevant when it can have a measurable impact on at least one attribute. DAGs are particularly suitable to represent cause– effect-chains [28]. Therefore, we refer to DAGs (representing the experts' knowledge about the interdependence of variables) as Causal Maps following, e.g., [28,29,46]. Although we adopt the term Causal Map, we do not impose causal inference mechanisms or aggregation as used by Montibeller and Belton [47,49]. Whilst sometimes, causal models are referred to as mental models of the decision makers and experts involved [10] or as a means to calculate the impact of an alternative on a set of attributes [47,49], our approach uses Causal Maps as a means to structure the flow of information, proceeding from causes to effects.

## 3.1. The configuration of Decision Maps

Each Decision Map consists of two parts: a Causal Map (CM) and an attribute tree (AT). The CM allows for ef<sup>fi</sup>ciently processing information relevant for the decision at hand. The AT enables an assessment of the CM's results respecting multiple goals and the decision makers' preferences.

If the CM can be elicited directly from decision makers (i.e., when there is enough time to bring all involved actors together), this step can be integrated into the MCDA problem structuring phase (for a detailed discussion of the elicitation of CMs from expert groups see, e.g., [3,23].) If restrictions defy discursive approaches, we propose following a distributed procedure. Distributed approaches are particularly useful when a large and complex problem can be segmented into sub-problems, each of which can be solved by specialised experts (human or automated systems) working exclusively on their limited sub-problem [8]. Directed acyclic graphs, such as CMs, are suitable for representing such distributed problem-solving frameworks, as they allow for representing each expert's knowledge locally [51].

To con<sup>fi</sup>gure the CM a distributed approach based on the resolution of task dependencies is used. The experts' (reasoning) capabilities are elicited a priori in terms of tasks or service(s) they can perform, information they can provide thereby and information each service requires. This re<sup>fl</sup>ects that an expert's output may rely on input he cannot determine autonomously. The system connects experts via software agents that are an interface between the expert (human or automated) and the service-based discovery architecture [53]. We make the assumption that experts refer implicitly (in the case of humans) or explicitly (in the case of automated systems) to a local causal model that allows them providing their service, their reasoning processes are represented as local CMs.

The expert actually providing information about the state of a certain variable is identi<sup>fi</sup>ed in a negotiation process ensuring that the best expertise available within a limited time is used [53]. These experts are connected via software agents. To handle trade-offs between quality of output (in terms of accuracy and level of aggregation) and time required to perform a service, the experts are allowed to qualify the need for the information in qualitative terms (e.g., imperative, interesting). This helps to identify information that must be taken into account even when time is critical.

The con<sup>fi</sup>guration of the global CM starts by identifying experts capable of determining the attributes' states. Referring to their local CMs, these experts specify the information their service depends on. Fig. 2 shows an example. Successively, the experts are connected in a CM by connecting all local CMs [17]. On the whole, the CM integrates expert knowledge and automated systems into a distributed information processing framework that allows for determining the attributes' values.

After the problem structuring phase, the Decision Map is attained, cf. Fig. 3. The connection between both parts of the Decision Map is made via the attributes, which are part of both the CM and the $\mathsf { A T } .$

The CM displaying cause–effect chains is presumed to be chronologically ordered: let i and j be two nodes. If i→j, then the state $x _ { i }$ of i in<sup>fl</sup>uences the state $x _ { j } \ 0 { \mathrm { f } } \ j .$ This implies that x at time t in<sup>fl</sup>uences $x _ { j } \ \mathrm { a t } \ t + \Delta ,$ where $\varDelta > 0 .$ . The temporal structure of the CM allows for the elimination of loops [51]. This is important if the scenarios constructed stretch far into the future and feedback between the variables has to be taken into account. For the AT, the linear structure is ensured by the hierarchical order of the tree showing the operationalisation of higher level goals by means of lower level criteria. Choosing the time steps appropriately, the structure of the entire Decision Map can therefore always be represented as a DAG. This structure facilitates distributed or local computation of (intermediate) results. This is particularly important for those parts of the Decision Map that are solved by automated systems or are solved using standardised inference mechanisms (e.g., Bayesian Networks being sub-graphs of the Decision Map).

## 3.2. Principles of reasoning under uncertainty in the Decision Map

The next step is the analysis of the information available and a description of the appropriate principles for handling uncertainty. We distinguish four types according to the level of (un-)certainty: deterministic, probabilistic, fuzzy and limiting. Accordingly, we distinguish the following node classes depending on the principles used to determine the state $x _ { j }$ of a node j given the states of all direct predecessor nodes $i \in \tilde { \Psi } ( j ) $

• Deterministic $( D ) \colon x _ { j }$ can be determined uniquely, with possibly small (local) perturbations.

• Probabilistic or Bayesian $( B ) \colon { \mathsf { a } }$ (conditional) probability distribution for $x _ { j }$ can be derived.

• Fuzzy (F): information on $x _ { j }$ is vague and imprecise, but can be captured using fuzzy methods.

• Limiting $( L ) \colon x _ { j }$ is limited to ${ \ddot { I } } _ { j } \subset I _ { j } ,$ where $I _ { j }$ is the image set of j.

Each of the nodes in the CM is assigned uniquely to one of the classes B, D, F or L. For deterministic nodes one unique state is derived. For all other nodes a set of possible states arises. Although for each node in B, F or L the support (roughly speaking, the set of possible values) can be continuous or crisp, it is useful to distinguish these sets, as the underlying paradigms of reasoning differ considerably: probabilistic methods are suitable for aleatory uncertainties; the underlying information may rely on measurements and observations or be based on expert judgements [52]. Fuzzy nodes allow taking into account uncertainties that arise from the imprecision and vagueness of linguistic descriptions [55]. Nodes for which the likelihood of possible states cannot be quanti<sup>fi</sup>ed can be found in L. That means, if there is ignorance about the likelihood of a node j's state, no arbitrary assumptions are made. Particularly, we do not assume that the variable's possible states are equally likely (i.e., uniformly distributed). Note that we do not propose jumbling the principles and underlying paradigms. The distributed approach applied here divides the problem into sub-problems that are handled independently or consecutively. This facilitates the application of different principles for dealing with uncertainty as well as the <sup>fl</sup>exible adaptation of the reasoning methods to the information at hand and the time available.

![](/api/attachments/5KUX5WEG/fulltext/images/0b6ffef04383c308ecca9cbe1c798a9c8bc69900320e525e37a9dae0de33f7e9.jpg)  
Fig. 2. Con<sup>fi</sup>guration of the CM based on local CMs, example for attribute 2. Information provided by the experts is labelled with bold capital letters, information necessary for them in italic letters. Connections within a local CM (continuous arcs) represent causal relations. Connections between the local CMs (dashed arcs) represent the <sup>fl</sup>ow of information.

Whilst the nodes are mapped to the aforementioned classes, the processing of information is not standardised: each expert is free to choose the algorithms, heuristics, and best practises that <sup>fi</sup>t best. This allows for <sup>fl</sup>exible reaction to the problem at hand, which is of great importance in dynamic and hardly predictable situations.

## 4. Distributed scenario construction

In this section, a novel approach for constructing scenarios in a distributed manner taking into account bounded availability of experts is presented. This approach makes use of straightforward set and graph theory allowing for capturing precisely interdependency relations and thus to analyse the plausibility, coherence and consistency of scenarios. Furthermore, this approach serves as a means to manage the number of scenarios arising (see Section 4.2).

## 4.1. Scenario construction

The Decision Map con<sup>fi</sup>gured for each alternative $a _ { i } \in A = \{ a _ { 1 } , . . . , a _ { k } \}$ as described in the previous section is now used to construct a set of scenarios $S ( a _ { i } )$ assessing the consequences of implementing $a _ { i \cdot }$ (The structure of the CM can change for the evaluation of different alternatives, as the alternatives may in<sup>fl</sup>uence different aspects of the environment. Yet, as the work <sup>fl</sup>ows are determined dynamically, each CM is complete in itself.)

For each $a _ { i } \in A$ the CM-part of the Decision Map is initialised by determining the states of the independent nodes. A node j is independent from all other nodes, when the set of its predecessors $\Psi _ { j } = \emptyset$ (cf. black nodes in Fig. 4). For all independent nodes $j ^ { i n d }$ , the responsible experts determine autonomously one or more states $x _ { j } ^ { i n \bar { d } }$ depending on the quality and accessibility of information as well as on the time available.

After the initialisation, scenarios are developed iteratively: let $S _ { \Psi ( j ) } ^ { \eta }$ be a partial scenario consisting of instantiations of all nodes in $\psi ( \bar { j } ) , \mathrm { e . g . , } \ S _ { \psi ( j ) } ^ { \eta } = \{ i _ { 1 } = x _ { 1 } ^ { \eta } , . . . , i _ { n } = x _ { n } ^ { \eta } \} \ \mathrm { f o r } \ | \psi ( j ) | = n w _ { . }$ with $\eta { \in } \{ 1 , . . . , N \}$ where N is the number of partial scenarios. Let $\tilde { \Psi } ( j )$ be the set of direct predecessors of j. Graphically there is an arc from i to j for all $i \in \tilde { \Psi }$ (see Fig. 4). The expert responsible for determining j is provided $S _ { \tilde { \Psi } ( j ) } ^ { \boldsymbol { \eta } } = \cup _ { i _ { k } \in \tilde { \Psi } ( j ) } \left\{ i _ { k } = x _ { k } ^ { \boldsymbol { \eta } } \right\}$

Given $S _ { \tilde { \Psi } ( j ) } ^ { \eta }$ , the responsible expert determines the possible states of j: $x _ { j } ^ { \eta , 1 } , \ldots , x _ { j } ^ { \eta , \lambda _ { j } }$ <sup>j</sup>, cf. Fig. 5. The new partial scenario $S _ { j } ^ { \eta , \mu }$ arises by merging $S _ { \Psi ( j ) } ^ { \eta }$ with the possible states of $j \colon \ S _ { j } ^ { \eta , \mu } { = } \cup _ { i _ { l } \in \psi ( j ) } \{ i _ { l } =$ $x _ { l } ^ { \eta } \} \cup \{ i _ { j } = x _ { j } ^ { \eta , \mu } \}$ , where $\mu { \in } \{ 1 , { \ldots } , \lambda _ { j } \}$ . Thus, uncertainty is re<sup>fl</sup>ected in a multiplicity of states, and each of the previous instantiations of the CM splits in a number of partial scenarios.

The scenario construction is completed when each variable in the CM was assessed and is assigned at least one state. The set of scenarios Σ can be understood as a way of expressing uncertainty in a set of relevant states for each variable, where each scenario contains a concerted set of states.

This scenario construction approach ensures that all information necessary to determine a variable's state is provided to the responsible expert, as all direct dependencies are taken into account. The risk of information overload is reduced by avoiding redundant or irrelevant information that was not judged necessary by the expert. Regarding the requirements for scenario acceptance, coherence is ensured as interdependencies are represented in the Decision Map. Consistency is ensured as values from different scenarios are not mixed. The scenario construction method guarantees that values within a scenario are kept consistent as far as possible given the information and expertise available. First, all direct interdependencies are explicitly considered. Second, indirect interdependencies are integrated by conditioning each node's state on the state of its (direct) predecessors. Finally, the plausibility of the scenarios depends on the experts available given time constraints and on the credibility of their judgements. Advanced negotiation protocols ensure that the best available expertise is identi<sup>fi</sup>ed ensuring that the scenarios' plausibility is as good as possible.

![](/api/attachments/5KUX5WEG/fulltext/images/2280e5912b834544bbf74c2a75247548547df68748e802f64d9ad91f0f31634a.jpg)  
Fig. 3. An exemplary Decision Map. Left side: CM, direct causal relations are represented as arcs, variables are depicted as ovals, decision variables (alternatives) as diamonds, independent nodes in black. Right side: attribute tree, attributes and criteria are depicted in boxes, hierarchical dependencies as light lines.

![](/api/attachments/5KUX5WEG/fulltext/images/476f2edabc2449c17f791515ee2d75239d8b7ca5a9837a278996b8edcf3a8490.jpg)  
Fig. 4. Structure of the <sup>fl</sup>ow of information, example for variable 5.

## 4.2. Controlling the number of scenarios

The use of scenarios varies widely because of a lack of a generally accepted principle for scenario management [1]. Whilst the few existing approaches to scenario management focus on the evaluation of (complete) scenarios after their construction [1,2,36, e.g.,], this paper presents an approach that allows for local scenario management. This approach uses the capabilities of the (local) experts to de<sup>fi</sup>ne the number of scenarios to be passed on.

In case a variable j is deterministic, $x _ { j }$ is unique and the (partial) scenario $S _ { j } ^ { \eta , \mu } { = } S _ { j } ^ { \eta , 1 } { = } S _ { \psi ( j ) } ^ { \eta } \cup \chi _ { j }$ follows immediately. For uncertain variables $j \in B \cup F \cup L = : U , \texttt { a }$ set of possible values $X _ { j }$ arises. To avoid combinatorial explosion along with information overload or high workload, the number of states that are passed on must be controlled. To this end, for each uncertain node j a subset $\{ x _ { j } ^ { 1 } , . . . , x _ { j } ^ { \lambda _ { j } } \} { \subset } X _ { j }$ of values that are judged the most relevant is selected as a basis continuing scenario construction.

The choice of the maximum number of states to be passed on, $\lambda _ { j } ,$ is a compromise between uncertainty and ambiguity. To determine $\lambda _ { j } ,$ we propose a distributed procedure asking each expert determining one of j's direct successors $\kappa \in \tilde { \Theta } ( j )$ to indicate the number of states of j he can process within a given time $t , \lambda _ { j } ^ { \kappa } { = } \lambda _ { j } ^ { \kappa } ( t )$ . To facilitate this process, each expert should consider the total number of partial scenarios, he needs to consider: if for a node $\begin{array} { r } { \kappa \in \tilde { \Theta } ( j ) \colon \left| \left\{ j \in \tilde { \Psi } ( \kappa ) \cap U \right\} \right| = \ : u _ { \kappa } > 1 } \end{array}$ , then an upper bound for the number of partial scenarios to be processed in κ is $n _ { \kappa } = \prod _ { l = 1 } ^ { u } \lambda _ { j _ { l } }$

![](/api/attachments/5KUX5WEG/fulltext/images/6656dd4da312d9ac83910f3c0fe8b7c5d813c6b7acfea4f6a97a81f8b6e628db.jpg)  
Fig. 5. Example of scenario construction. Interdependencies represented as continuous arcs, <sup>fl</sup>ows of information as dashed arcs. Results for variables 3 and ${ \boldsymbol { 7 } } \in { \tilde { \Psi } } ( 6 )$ are combined to partial scenario $S _ { \tilde { \Psi } } ( 6 ) ( = S _ { \Psi } ( 6 ) )$ , each of which is used to determine a state for var. 6

A naïve way to determine $\lambda _ { j }$ from $n _ { \kappa }$ is choosing equal values, i.e., $\lambda _ { j } = \lfloor b _ { \kappa } / u _ { \kappa } \rfloor ,$ , where $b _ { \kappa } \mathrm { i } s$ the maximum number of scenarios that can be processed given the time constraints to be respected. As this approach does not re<sup>fl</sup>ect the importance of considering a multiplicity of scenarios for a variable $j ,$ ideally, each expert should take into account the impact that a change of the state of a node $j \in \tilde { \Psi } ( \kappa ) \cap U$ will have on his output. If the state of κ is sensitive to changes in $j , \lambda _ { j }$ should be larger than in case of robust results, as in the <sup>fi</sup>rst case small perturbations in j result in signi<sup>fi</sup>cant changes in $\kappa .$ Possibly, the experts can also specify directions of sensitivity $( \mathrm { e . g . }$ , sensitive to increase, but robust for decrease). For automated systems, this assessment can be done via sensitivity analyses. Human experts can also use qualitative assessments based on their experience (e.g., “robust” or “sensitive”). Finally, $\begin{array} { r } { \mathbb { \Lambda } _ { j } = \operatorname* { m i n } _ { \mathbb { \kappa } \in \tilde { \Theta } ( j ) } \left\{ \mathbb { \Lambda } _ { j } ^ { \kappa } \right\} } \end{array}$

If for a node j the number of possible states $\left| X _ { j } \right| > \lambda _ { j } ,$ a mechanism for selecting the most relevant states must be implemented. This mechanism should ensure that the set of partial scenarios $\cup _ { \eta , \mu } S _ { j } ^ { \eta , \mu }$ covers a broad variety of possible developments and contains the most likely ones. $\lambda _ { j }$ is an upper limit, and each expert is free to provide $\tilde { \Lambda } _ { j } < \Lambda _ { j }$ assessments, if he/she feels that these re<sup>fl</sup>ect suf<sup>fi</sup>ciently the variety of possible developments. Still, it is useful to develop some general guidelines that can be implemented easily for the involved automated systems. These guidelines ensure the consistency of the selection and can be adapted to the decision makers' requirements (e.g., the minimum required likelihood of each piece of information). The selection of the most relevant states follows a procedure that varies with the principle for reasoning under uncertainty. For all cases discussed below assume that $\lambda _ { j } \ge 3$

If $j { \in } B , \ x _ { j } ^ { 1 , . . . , \Lambda _ { j } }$ is determined using quantiles $x _ { j } ^ { \alpha _ { l } }$ and $x _ { j } ^ { \beta _ { m } }$ that correspond to the α - and $\beta _ { m }$ -quantiles. The probability that a scenario generates a score that is lower than $x _ { j } ^ { a _ { l } } \left( l = 1 , . . . , L \right)$ (higher than $x _ { i } ^ { \beta _ { m } }$ $( m { = } 1 , . . . , M ,$ where $L + { \cal { M } } { < } { \lambda _ { j } } ) )$ is smaller or equal than α $( 1 - \beta _ { m } )$ The choice of α and $\beta _ { m } -$ particularly for the extreme states $x _ { j } ^ { 1 }$ and $x _ { j } ^ { \lambda _ { j } } -$ depends on the minimum acceptable likelihood: as it is advised not to restrict too much the possible scenarios by likelihood considerations [65], $\alpha _ { 1 }$ and $\beta _ { M }$ should be chosen such that they are as close to 0 resp. 1 as acceptable for the decision makers. In addition, the $\lambda _ { j } - ( L + M )$ most probable state(s) are selected, e.g., for $\lambda _ { j } - ( L +$ $M ) = 1$ one selects $x _ { j } ^ { m a x } = a r g m a x p _ { j } ( x )$ , where $p _ { j } ( x )$ is the (conditional) probability distribution for node j, see Fig. 6. If x<sup>max</sup> is not unique, the state closest to the mean is selected.

$\operatorname { I f } j \in F ,$ a similar approach making use of the underlying fuzzy membership function $\mu _ { j }$ characterising the state $x _ { j }$ is implemented. The decision makers de<sup>fi</sup>ne a threshold of minimal acceptable membership $\gamma _ { j } ^ { m i n }$ . Analogue to the probabilistic case, the extreme states $x _ { j } ^ { \alpha _ { 1 } }$ and $x _ { I } ^ { \beta _ { M } }$ can be derived as $x _ { j } ^ { \alpha _ { 1 } } { = } i n f \{ x : \mu ( x ) \geq \gamma _ { j } ^ { m i n } \}$ and $x _ { j } ^ { \beta _ { M } } { = } s u { \bar { p } } \{ x { : } \mu ( x ) { \bar { \geq } } \gamma _ { j } ^ { m i n } \}$ . For exploring a broader set of states, further thresholds $\gamma _ { \alpha _ { 1 } } , \dots , \gamma \alpha _ { L }$ and $\gamma _ { \beta _ { 1 } } , . . . , \gamma \beta _ { M }$ (where $M + L { < } \lambda _ { j } )$ can be used. Additionally, the mean of the scores with maximum membership is used. $\mathrm { I f } \lambda _ { j } - ( M + L ) > 1$ , further states with $\mu ( x _ { j } ) = 1$ can be passed on.

![](/api/attachments/5KUX5WEG/fulltext/images/f3c41bf69663d65a03a2190bac4a6fbc6af027f33b472e4df9dbb86a6267ba88.jpg)  
Fig. 6. Exemplary selection of states for a standard Gaussian variable j, with $\lambda _ { j } = 3$ and quantiles $\alpha { = } 1 - \beta { = } 0 . 0 2 5$ Thus $x _ { j } ^ { \alpha } { = } - 1 . 9 6 , x _ { j } ^ { m a x } { = } 0$ and $x _ { j } ^ { \beta } { = } 1 . 9 6$

$\mathrm { F o r } j \in L ,$ , the extreme scores (i.e. inf(I ) and sup(I )) as well the score closest to the median can be selected. Alternatively, if the experts providing the state(s) of j are human, they can be asked to select the score which seems most likely to them. If $\lambda _ { j } { > } 3$ further scores with equal distances to the extreme and medium scores can be chosen.

Using these scores determined and presented as described above, new (plausible and consistent) partial scenarios $S _ { j } ^ { \eta , 1 , \dots , \eta , \lambda _ { j } }$ are generated respecting the processing capacity of each expert and constraints in time. Successively, a set of scenarios $S ( a _ { i } )$ for each alternative $a _ { i } \in A$ is created.

## 4.3. Evaluation of decision alternatives

To evaluate the alternatives the attribute tree (AT) part of the Decision Map is used. In the simplest case all nodes are deterministic and just one scenario $S ( a _ { i } )$ and one corresponding set of attribute scores for each alternative $a _ { i } \in A$ is derived. Hence, standard MAVT can be applied [3]. If there are uncertain nodes, however, a set of scenarios $\Sigma ( a _ { i } )$ is created $\forall a _ { i } \in A .$ . The complete set of created scenarios is denoted $\Sigma = \cup _ { i = 1 } ^ { k } \Sigma ( a _ { i } )$ . Each scenario $S { \in } \Sigma$ is evaluated using the AT and the elicited preferences, resulting in a performance $p ( S ) [ 3 ]$

As the maximum number of scenarios manageable for (human) decision makers is considered seven [45], in all cases with more than seven scenarios the need for reducing the number of presented scenarios arises. This can be achieved either by selection or aggregation of scenario results.

When presenting individual scenarios to the decision makers, we propose an approach for scenario selection founded on the evaluation of results: for each set $\Sigma ( a _ { i } )$ , the scenarios with the worst, the best and the performance closest to the median $( S ( a _ { i } ) ^ { w } , \ S ( a _ { i } ) ^ { b } { \mathrm { a n d } } \ S ( a _ { i } ) ^ { m } ,$ respectively) are presented to the decision makers in detail. Thus, the decision makers' preferences are taken into account explicitly.

This approach does neither refer to an intuitive de<sup>fi</sup>nition of pessimistic or optimistic cases (as often done in scenario planning [64]) nor require measuring the dissimilarity or distance between scenarios by the difference in the states of the variables as in formative scenario analysis [66]. It allows for making the spread of evaluations according to the decision makers' preferences as well as the worst-case performance for each alternative easily visible. In this manner, our approach supports decision makers in choosing an alternative whose total performance (or performance in selected criteria) does not fall below a certain threshold τ for all scenarios for which the minimum likelihood requirements of all states are kept (cf. Section 4.2). τ re<sup>fl</sup>ects the minimal required performance. To determine the threshold (or aspiration level) τ, different methods have been suggested (e.g., benchmarking [30], iterative approaches [13]). Thus, the Decision Map approach facilitates robust decision making, in the sense that it supports making a decision that performs on average suf<sup>fi</sup>ciently well for a set of scenarios [4,58], or that guarantees that a minimum performance is reached for all scenarios [74].

To base the decision not only on re<sup>fl</sup>ections about individual scenarios, but on the totality of scenarios created, the presentation of individual scenarios is complemented by a further MAVT step aggregating the results. To this purpose, weights $w _ { j } ( S _ { j } ( a _ { i } ) )$ ) re<sup>fl</sup>ecting the relative importance of each scenario $S _ { j } ( a _ { i } ) \in \Sigma ( a _ { i } )$ are elicited. For the meaning and interpretation of scenario importance weights see [22,70]. To determine the weights, e.g., the deviation of the total performance or the performance in some criteria in $S _ { j } ( a _ { i } )$ from prede<sup>fi</sup>ned goals for these performances can be used [15]. Note that the weights elicited in this manner represent the importance of considering a scenario regardless of its likelihood. The weights are normalised such that $\sum j { \overset { m _ { a i } } { = } } 1 w _ { j } = 1$ , where $m _ { a _ { i } } = \left| \Sigma ( a _ { i } ) \right|$ . Then, for each alternative $a _ { i } ,$ the performances of all scenarios $p ( S _ { j } ( a _ { i } ) )$ are aggregated by $\begin{array} { r } { p ( a _ { i } ) = \sum _ { j = 1 } ^ { m _ { a i } } w _ { j } p ( S _ { j } ( a _ { i } ) ) } \end{array}$

The aggregation of results can help in avoiding assigning importance exclusively to scenarios that are easy to imagine (bias of imaginability) or similar to cases which were already experienced by the decision makers (bias of representativeness) [72]. Furthermore, the discussion and consensus building about the scenario weights makes the underlying preferences and value judgements explicit. Thereby, biases like the certainty effect (a sharp discrepancy between the weights that are attached to sure gains and to highly probable gains in the evaluation of prospects) and loss aversion (the emphasis of potential losses and disadvantages compared to gains and advantages) [37] can be exposed and taken into account.

## 5. Emergency management example

This section illustrates the Decision Map approach by means of an example from the <sup>fi</sup>eld of strategic emergency management. In this domain common characteristics include [6,27,79]:

• a <sup>fi</sup>nite set of feasible alternatives to choose from,

• multiple goals, which are often con<sup>fl</sup>icting, • multiple, often locally dispersed decision makers, experts and stakeholders involved, each of which has different knowledge, skills, competences and preferences,

• information of heterogeneous type, quality and uncertainty,

• constrained time for the decision-making and bounded availability of experts and decision makers, but no real-time or ad-hoc decision making,

• the need for transparency, comprehensibility and documentation, to enhance acceptance and compliance.

In strategic emergency management the need for distributed, timely, coherent and effective decision support as offered by the Decision Map approach arises. The example described below is deliberately kept small to allow for a clear exploration of our approach by highlighting its main features. It has been extracted from an ample use case that has been investigated with decision makers from emergency management authorities.

## 5.1. Situation description

A freight train is derailed causing the leakage of chlorine from a ruptured tank waggon. A responder unit specialised in dealing with hazardous material covers the rupture, thereby temporarily stabilising the situation. The chlorine must be transferred to a transportation tank to resolve the situation permanently. This transfer is fraught with the risk of a further leakage threatening the population in the downwind area. A decision on the preventive measure to be applied must be made: evacuation of downwind areas or sheltering in house.

## 5.2. The configuration of the Decision Map

To structure the decision problem an AT has been elicited from potentially involved decision makers. This tree includes the criteria Health, Effort and Impact on Society, which are broken down into 39 attributes. To illustrate our approach, we focus on health topics and show how the scores for the attribute Number of ill in hospital exposed are derived.

First the (best) expert available and able to provide information about the number of ill in hospitals exposed is identi<sup>fi</sup>ed. This expert indicates that he needs information on the alternative implemented. As it is assumed that Evacuation takes place before a potential plume reaches the hospital, for Evacuation the CM con<sup>fi</sup>guration is <sup>fi</sup>nished (cf. Table 1, left side). In this example, the structure of the CM depends on the alternatives implemented, as for alternative Sheltering further information on the hospitals (potentially) exposed is needed (represented in Table 1, left side, as a further link). Here, exposure is understood as exceeding of a threshold concentration. Continuing this process iteratively, the CM expands until all independent nodes (represented as black ovals) are reached.

Matrix showing CMs for determining Number of ill in hospital exposed for Evacuation and Sheltering. Left side: con<sup>fi</sup>guration, arcs represent connection of expertise. Right side: resulting CM, arcs represent <sup>fl</sup>ow of information during scenario construction phase.  
![](/api/attachments/5KUX5WEG/fulltext/images/a9e9f53bf2f7e8ffebce97c119843b06ffad53bab467bc0086e46f8f93476611.jpg)

## 5.3. Scenario construction

After the CM con<sup>fi</sup>guration, scenarios can be constructed by processing information following the links established. First, the scores for the independent nodes are determined by the experts. For the evaluation of Evacuation it is assumed that the hospital will be evacuated completely before the chlorine transfer starts. Therefore, the Number of ill in hospital exposed is set to 0. For Sheltering a number of scenarios arise: the <sup>fi</sup>rst source of uncertainty is uncertainty about the success of the transfer as expressed by the local expert. The variable Success of transfer is a binary ∈L, generating two different sets of scenarios. If Success of transfer is 1 (i.e., no chlorine is released), there is no hospital exposed and the Number of ill in hospital exposed is again set to 0.

For the scenarios assuming that chlorine is set free, the full CM needs to be considered. The expert determining the Amount of chemical in vessel states that there is still a considerable amount of the chemical in the tank, which has a volume of $1 0 0 \mathrm { m } ^ { 3 } .$ . Apparently, this node belongs to F. Here, the amount of chlorine left is modelled as a trapezoidal fuzzy number, cf. Fig. 7. As the expert estimating the source term for chlorine release, which is the only successor of the node Amount of chemical in vessel, speci<sup>fi</sup>ed that he can process up to three possible values for the amount of chlorine, and as the threshold γ of minimum required membership was set to 0.8, the states passed on are $x _ { j } ^ { 1 } = 6 2 \mathrm { m } ^ { 3 } , x _ { j } ^ { 2 } = 7 2 . 5 \mathrm { m } ^ { 3 } \mathrm { a n d } x _ { j } ^ { 3 } = 8 2 \mathrm { m } ^ { 3 }$ (see Fig. 7). Similarly, one proceeds to assess the potential leak sizes. Assume that two possible leak sizes are passed on to the expert estimating the source term, who needs to consider each of the six possible combinations of amount of chlorine and leak size.

![](/api/attachments/5KUX5WEG/fulltext/images/cca8f9f7fdcebcd7f3f9258240de75df14d1450efb2604ba56c91f3e0d90e36f.jpg)  
Fig. 7. Fuzzy membership function modelling “considerable amount of chemical left in the tank” as a trapezoidal fuzzy number.

For the weather conditions, particularly for the wind direction, probabilistic techniques can be applied [60]. Three possible meteorological conditions are passed on. Then, the six source terms estimated as well as the three meteorological conditions are then used by a (deterministic) atmospheric dispersion model to predict the according (18) plume shapes

The number of states passed on does not necessarily increase by following the CM, as only decision-relevant information is processed. Whilst the number of plume shapes may be large, here, only one hospital is situated in the vicinity of the incident. That is why the number of possible states for Hospitals exposed is only two.

## 5.4. Evaluation of decision alternatives

When the CM is fully assessed for all alternatives with respect to each attribute, an evaluation of each scenario is performed. Then, scenario weights re<sup>fl</sup>ecting the importance of each scenario are elicited. In this example, equal weights for the scenarios of each decision alternative were used. This results in a higher total performance for Sheltering (0.66 vs. 0.59 for Evacuation). In addition to these results, the decision makers are provided with stacked bar charts showing the performance of the worst, medium and best scenarios for both decision alternatives (see Fig. 8). This chart facilitates the assessment of robustness, as it shows that the worst scenario for alternative evacuation results in a much better performance than the worst-case scenario for sheltering. A sensitivity analysis, where the scenario weights are varied, provides further support for the decision makers [16].

## 6. Discussion and conclusion

We described a framework for decision support respecting multiple goals in complex situations susceptible to severe uncertainty, where the decision consists in choosing one out of a small set of feasible alternatives. Multi-Attribute Value Theory (MAVT) provides the underlying evaluation principles to facilitate the consideration of trade-offs and the decision makers' preferences. To consider uncertainties in a transparent and easily understandable way, descriptions of different possible future developments of the situation (i.e., scenarios) are used. The integration of Causal Maps (CM) and ATs to Decision Maps enables distributed scenario construction taking into account the uncertainties that arise during the determination of attribute scores.

![](/api/attachments/5KUX5WEG/fulltext/images/bcc4b4d031a8e1148526dbc7fd4531e8eb8123bd18aa09e81658c4cb3b6a186d.jpg)  
Fig. 8. Evaluation of Evacuation, Sheltering and Do Nothing (DN) alternatives. Results for worst, medium and best evaluated scenarios.

Contrarily to other approaches for evaluating scenarios with MCDA techniques [19,33,46,59], our approach systematically integrates scenario construction and evaluation of alternatives. In this way, MAVT is used as a rationale for processing and <sup>fi</sup>ltering information during the scenario construction phase. Additionally, the distributed approach enables using different techniques for reasoning under uncertainty that <sup>fi</sup>t best the actual situation and the information available. Thus, the decision map does not require any standardisation of reasoning principles (as, e.g., needed for the construction of Bayesian Networks, Causal Maps or Fuzzy Cognitive Maps) but can be adapted <sup>fl</sup>exibly to the problem at hand.

## 6.1. Distributed scenario construction

The Decision Map approach for scenario construction can be positioned in between discursive scenario-based decision support, which require face-to-face meetings [65,66], and expert systems, which solve decision problems autonomously by using a model of the domain [21]. Our approach is particularly suitable for large and complex decision problems where expertise from several domains has to be brought together, but time and availability of experts is bounded. Additionally, our approach supports decision makers in varying environments, or when it is necessary to consider rare events. In these cases, the use of automated systems, which require a vast continuously updated knowledge base covering all eventualities [21], is problematic.

To ensure that the information processed is relevant, it is necessary that the experts are able to specify the type of service they can provide (including information on the type and format of output) as well as the type of information necessary to provide this service. Whilst for automated systems, this tantamounts just to the declaration of input and output, for human experts it is necessary to ensure that they comply to these speci<sup>fi</sup>cations.

The basis for decision making in our approach is a set of scenarios for each alternative. Requirements for the scenarios' acceptance are their plausibility, coherence, and consistency, which have to be ensured by the experts. Assuming that the experts are able to specify their services in terms of input and output variables (represented as local CM), each scenario arising is coherent, as the global CM explicitly represents interdependencies. Concerning the plausibility, our approach assumes that each expert provides information to the best of his knowledge given potential constraints regarding the information and time available. By keeping track of the expertise used within the scenario construction (i.e., logging who provided the information on each node), it is possible to qualify the plausibility of the scenarios by the expertise used. For the consistency similar considerations hold: <sup>fi</sup>rst, we assume that each expert is capable of specifying the factors that have an impact on his assessment. Second, we presume that the output of an expert <sup>fi</sup>ts to the input he used. In this manner, both plausibility and consistency depend on the experts contributing to the system.

## 6.2. Timeframe

Concerning the issue of time, all steps within the Decision Map approach need to be considered. The problem structuring phase encompasses the elicitation of the AT and the con<sup>fi</sup>guration of the CM. If the situation at hand allows for some degree of standardisation of its evaluation (e.g., when the goals of the decision makers remain essentially unaffected for a certain class of decision problems), it is possible to use AT templates (that can be re<sup>fi</sup>ned if necessary). Additionally, if the situation at hand follows certain patterns and the input and output each expert potentially contributing to the scenario construction provides can be de<sup>fi</sup>ned a priori, the con<sup>fi</sup>guration of the CM can be accelerated. Contrarily, if the decision problem is unique or if there is disagreement on the evaluation principles and preferences within the attribute tree and discussion is required to build a consensus, more time needs to be reserved for the problem structuring phase as well as for a potential analysis of results.

The maximum number of scenarios constructed depends on the number of nodes in the CM and on the number of scores for each node. If the CM has n nodes, and each node is assigned at most $\lambda _ { j }$ scores, an upper bound for the magnitude of the set of created scenarios Σ is $\prod _ { j = 1 } ^ { n } \lambda _ { j } .$ It is each expert's responsibility to de<sup>fi</sup>ne the number of pieces of information for each of the input variables he uses that he can handle within a given time. This approach allows for allocating a time $\tau _ { j }$ to each expert functioning as a node j in the CM. By weighing each arc (j,k) from j to one of its successors $k \in \Theta ( j )$ , an upper bound for the time of scenario construction for each alternative corresponds to the length of the longest path $\begin{array} { r } { P ^ { * } \colon l ( P ^ { * } ) = \sum { } _ { ( j , k ) \in P ^ { * } } \tau _ { j } , } \end{array}$ . There might be trade-offs between the amount of different types of information an expert can process and the accuracy of the information he determines and passes on. This concerns both the information regarding different aspects of the situation (represented by different nodes in the CM) and the level of granularity of this information (ranging from very speci<sup>fi</sup>c information to general trends). The Decision Map approach reveals these trade-offs and can help analysing which pieces of information are the most relevant and must be taken into account even when time is critical. Other pieces of information (or information on a higher level of detail) might only be processed if time is abundant.

Finally, the results should not be understood as an imperative prescription, but rather as a support and guidance for the decision makers. Thus, the analysis and interpretation of the results requires some additional time (particularly, when our approach is applied in an iterative manner allowing for integration of feedback and re<sup>fi</sup>nements).

## 6.3. Directions for future research

The Decision Map approach is the basis for a further exploration of distributed decision support under severe uncertainty. Elicitation techniques and interfaces to support each expert's assessment need to be further developed. This concerns particularly the meta-information (e.g., the number of input an expert can process within a given time, the sensitivity of his results to change in input).

Another issue concerns possible changes in the information: the information underlying a scenario may change quantitatively (e.g., predicted results change) or qualitatively. In the <sup>fi</sup>rst case the principles of reasoning under uncertainty are not affected, whilst the latter case corresponds to situations, where new or better information allows for a more accurate description of the likelihood of a piece of information (e.g., when previously uncertain information becomes known, or when lacking information becomes available). In both cases a decision must be made if a new piece of information is important enough to justify a scenario update requiring effort from experts providing information of all successor nodes in the CM.

Finally, the results must be presented in a transparent and easily understandable way so that users and stakeholders will accept the recommendations found. To this end, both visualisation techniques and the generation of natural language reports containing information on the scenario itself as well as meta-information about the experts contributing to a scenario or the information about the likelihood are investigated.

## 6.4. Conclusion

The Decision Map approach supports decision makers facing large and complex problems under uncertainty. Our framework is particularly useful when the type and quality of information is heterogeneous, as it allows for the simultaneous handling of several principles for reasoning under uncertainty. As the approach presented is a generic framework supporting strategic decision making it can be applied in various domains, e.g., environmental management, policy assessment or risk management.

The Decision Map integrating a CM and an AT facilitates distributed scenario construction involving human experts and automated reasoning systems. Uncertainty about the state of a variable will be expressed as a number of possible states that propagate through the Decision Map as (partial) scenarios: whenever an expert is uncertain about a variable's state, this uncertainty results in multi-furcation of (partial) scenarios.

The distributed approach for scenario construction facilitates dealing with heterogeneous types and qualities of information, as it allows for the <sup>fl</sup>exible use of reasoning principles (e.g., probabilistic or fuzzy techniques). It becomes possible to evade the risk of losing information, which happens when the reasoning paradigm chosen has little requirements, but also offers little information, (e.g., intervals or qualitative statements) or misjudgements and biases (e.g., when using Bayesian techniques without having suf<sup>fi</sup>cient statistical information).

The use of the Decision Map facilitates robust decision making, as it integrates the decision makers' preferences and allows for basing scenario selection on a systematic evaluation, rather than on the users' intuition or on an abstract notion of “distance” within the CM. To come to an overall ranking of alternatives taking into account all created scenarios, an additional MAVT step is performed. Deeper insights into the decision situation can be gained than those provided by standard methods that base the evaluation on a best guess or the most likely development.

## Acknowledgement

This research is funded by the EC FP7-ICT project DIADEM, ref. no: 224318, www.ist-diadem.eu. The authors wish to thank their DIADEM partners, particularly the Danish Emergency Management Agency, for the comments on the example and the role and use of scenarios and MCDA for decision making.

## References

[1] D.M. Ahmed, D. Sundaram, S. Piramuthu, Knowledge-based scenario management — process and support, Decision Support Systems 49 (2010) 507–520.

[2] T.A. Alspaugh, A.I. Antón, Scenario support for effective requirements, Information and Software Technology 50 (2008) 198–220.

[3] V. Belton, T. Stewart, Multiple Criteria Decision Analysis, An Integrated Approach, Kluwer Academic Publishers, Boston, 2002.

[4] Y. Ben-Haim, Robust rationality and decisions under severe uncertainty, Journal of the Franklin Institute 337 (2000) 171–199.

[5] Y. Ben-Haim, Uncertainty, probability and information-gaps, Reliability Engineering and System Safety 85 (2004) 249–266.

[6] V. Bertsch, Uncertainty Handling in Multi Attribute Decision Support for Industrial Risk Management, Ph.D. thesis, Universität Karlsruhe (TH), Karlsruhe, 2008.

[7] J.P. Brans, C. Macharis, P.L. Kunsch, A. Chevalier, M. Schwaninger, Combining multicriteria decision aid and system dynamics for the control of socio-economic processes. An iterative real-time procedure, European Journal of Operational Research 109 (1998) 428–441.

[8] T. Bui, J. Lee, An agent-based framework for building decision support systems, Decision Support Systems 25 (1999) 225–237.

[9] J. Butler, J. Jia, J. Dyer, Simulation techniques for the sensitivity analysis of multicriteria decision models, European Journal of Operational Research 103 (1997) 531–546.

[10] J.C. Butler, J.S. Dyer, J. Jia, Using attributes to predict objectives in preference models, Decision Analysis 3 (2006) 100–116.

[11] B. Chaib-draa, Causal maps: theory, implementation, and practical applications in multiagent environments, IEEE Transactions on Knowledge and Data Engineering 14 (2002) 1201–1217.

[12] T.J. Chermack, Improving decision-making with scenario planning, Futures 36 (2004) 295–309.

[13] J.R. Cho, H.S. Jeong, W.S. Yoo, Multi-objective optimization of tire carcass contours using a systematic aspiration-level adjustment procedure, Computational Mechanics 29 (2002) 498–509.

[14] R. Clemen, T. Reilly, Making Hard Decisions with DecisionTools, Duxbury, Paci<sup>fi</sup>c Grove, CA, 1999.

[15] T. Comes, M. Hiete, E. Schultmann. A decision support system for multi-criteria decision problems under severe uncertainty in longer-term emergency management, in: C.H. Antunes, D. Ríos Insua (Eds.), Proceedings of the 25th Mini EURO Conference on Uncertainty and Robustness in Planning and Decision Making (2010), Coimbra.

[16] T. Comes, M. Hiete, N. Wijngaards, M. Kempen, Integrating Scenario-Based Reasoning into Multi-Criteria Decision Analysis, in: J. Landgren, S. Jul (Eds.), Proceedings of the 6th International Conference on Information Systems for Crisis Response and Management (2009), Gothenburg.

[17] T. Comes, C. Conrado, M. Hiete, M. Kamermans, G. Pavlin, N. Wijngaards, An intelligent decision support system for decision making under uncertainty in distributed reasoning frameworks, in: S. French, B. Tomaszewski, C. Zobel (Eds.), Proceedings of the 7th International Conference on Information Systems for Crisis Response and Management (2010), Seattle

[18] J.P. Davis, J.W. Hall, A software-supported process for assembling evidence and handling uncertainty in decision-making, Decision Support Systems 35 (2003) 415-433

[19] D. Diakoulaki, F. Karangelis, Multi-criteria decision analysis and cost-bene<sup>fi</sup>t analysis of alternative scenarios for the power generation sector in Greece, Renewable and Sustainable Energy Reviews 11 (2007) 716–727.

[20] M. Dohnal, Ignorance and uncertainty in reliability reasoning, Microelectronics and Reliability 32 (1992) 85–121.

[21] J. Dugdale, A cooperative problem-solver for investment management, International Journal of Information Management 16 (1996) 133–147.

[22] I. Durbach, T. Stewart, Integrating scenario planning and goal programming, Journal of Multi-Criteria Decision Analysis 12 (2003) 261–271.

[23] C. Eden, Analyzing cognitive maps to help structure issues or problems, European Journal of Operational Research 159 (2004) 673–686.

[24] S. Ferson, What Monte Carlo methods cannot do, Human and Ecological Risk Assessment: An International Journal 2 (1996) 990–1007

[25] G. Fischer, A.C. Lemke, T. Mastaglio, A.I. Morch, The role of critiquing in cooperative problem solving, ACM Transactions on Information Systems 9 (1991) 123–151.

[26] B. Fischhoff, Hindsight is not equal to foresight: the effect of outcome knowledge on judgment under uncertainty. Journal of Experimental Psychology, Human Perception and Performance 1 (1975) 288-299.

[27] S. French, T. Bedford, E. Atherton, Supporting ALARP decision making by cost bene<sup>fi</sup>t analysis and multiattribute utility theory, Journal of Risk Research 8 (2005) 207–223.

[28] D. Galles, J. Pearl, Axioms of causal relevance, Arti<sup>fi</sup>cial Intelligence 97 (1997) 9-43 Relevance.

[29] C. Goodier, S. Austin, R. Soetanto, A. Dainty, Causal mapping and scenario building with multiple organisations, Futures 42 (2010) 219–229.

[30] M.A. Goodrich, W.C. Stirling, E.R. Boer, Satis<sup>fi</sup>cing revisited, Minds and Machines 10 (2000) 79–109.

[31] P. Goodwin, G. Wright, Enhancing strategy evaluation in scenario planning: a role for decision analysis, Journal of Management Studies 38 (2001) 1–16.

[32] H.W. Gottinger, P. Weimann, Intelligent decision support systems, Decision Support Systems 8 (1992) 317–332.

[33] R. Hites, Y. De Smet, N. Risse, M. Salazar-Neumann, P. Vincke, About the applicability of MCDA to some robustness problems, European Journal of Operational Research 174 (2006) 322–332.

[34] S. Howick, C. Eden, F. Ackermann, T. Williams, Building con<sup>fi</sup>dence in models for multiple audiences: The modelling cascade, European Journal of Operational Research 186 (2008) 1068–1083.

[35] J. Jakeman, M. Eldred, D. Xiu, Numerical approach for quanti<sup>fi</sup>cation of epistemic uncertainty, Journal of Computational Physics 229 (2010) 4648–4663.

[36] M. Jarke, X.T. Bui, J.M. Carroll, Scenario management: an interdisciplinary approach, Requirements Engineering 3 (1998) 155–173.

[37] D. Kahneman, D. Lovallo, Timid choices and bold forecasts: a cognitive perspective on risk taking, Management Science 39 (1993) 17–31.

[38] D. Kahneman, A. Tversky, Variants of uncertainty, Cognition 11 (1982) 143–157.

[39] R.L. Keeney, H. Raiffa, Decisions with Multiple Objectives, John Wiley & Sons, New York, 1976.

[40] M.S. Khan, S.W. Khor, A framework for fuzzy rule-based cognitive maps, in: C. Zhang, H.W. Guesgen, W.K. Yeap (Eds.), PRICAI 2004: Trends in Arti<sup>fi</sup>cial Intelligence, volume 3157 of Lecture Notes in Computer Science, Springer, Berlin Heidelberg, 2004, pp. 454–463.

[41] F.H. Knight, Risk, Uncertainty, and Pro<sup>fi</sup>t, Houghton Mif<sup>fl</sup>in Co., Boston, 1921.

[42] B. Kosko, Fuzzy cognitive maps, International Journal of Man-Machine Studies 24 (1986) 65–75.

[43] T. Krynski, J. Tenenbaum, The role of causality in judgment under uncertainty, Journal of Experimental Psychology. General 136 (2007) 430–450.

[44] J.G. March, Z. Shapira, Managerial perspectives on risk and risk taking Management Science 33 (1987) 1404–1418.

[45] G.A. Miller, The magical number seven, plus or minus two: some limits on our capacity for processing information, Psychological Review 63 (1956) 81–97.

[46] G. Montibeller, V. Belton, Causal maps and the evaluation of decision options—a review, Journal of the Operational Research Society 57 (2006) 779–791.

[47] G. Montibeller, V. Belton, Qualitative operators for reasoning maps: evaluating multi-criteria options with networks of reasons, European Journal of Operational Research 195 (2009) 829–840.

[48] G. Montibeller, A. Franco, Multi-criteria decision analysis for strategic decision making, in: P.M. Pardalos, D.W. Hearn, C. Zopounidis, P.M. Pardalos (Eds.), Handbook of Multicriteria Analysis, Volume 103 of Applied Optimization, Springer, Berlin Heidelberg, 2010, pp. 25–48.

[49] G. Montibeller, V. Belton, F. Ackermann, L. Ensslin, Reasoning maps for decision aid: an integrated approach for problem-structuring and multi-criteria evaluation, Journal of the Operational Research Society 59 (2008) 575–589.

[50] M.G. Morgan, M. Henrion, Uncertainty: A Guide to Dealing with Uncertainty in Quantitative Risk and Policy Analysis, Cambridge University Press, Cambridge, 1990.

[51] S. Nadkarni, P.P. Shenoy, A Bayesian network approach to making inferences in causal maps, European Journal of Operational Research 128 (2001) 479–498.

[52] E. Nikolaidis, S. Chen, H. Cudney, R.T. Haftka, R. Rosca, Comparison of probability and possibility for design against catastrophic failure under uncertainty, Journal of Mechanical Design 126 (2004) 386–394.

[53] G. Pavlin, N. Wijngaards, K. Nieuwenhuis, Towards a single information space for environmental management through self-con<sup>fi</sup>guration of distributed information processing systems, in: J. Hřebíček, J. Hradec, E. Pelikán, O. Mírovský, W. Pillmann, I. Holoubek, T. Bandholtz (Eds.), Proceedings of the European conference TOWARDS eENVIRONMENT. Opportunities of SEIS and SISE: Integrating Environmental Knowledge in Europe (20o9) Masaryk University Brno Czech Republic, pp. 94–103.

[54] J. Pearl, Causality: Models, Reasoning, and Inference, Cambridge University Press, Cambridge. 2009.

[55] A. Peña, H. Sossa, A. Gutiérrez, Causal knowledge and reasoning by cognitive maps: Pursuing a holistic approach, Expert Systems with Applications 35 (2008) 2–18.

[56] S. Pender, Managing incomplete knowledge: why risk management is not suf<sup>fi</sup>cient, International Journal of Project Management 19 (2001) 79–87.

[57] M. Peterson, An Introduction to Decision Theory, Cambridge Introductions to Philosophy, Cambridge University Press, Cambridge, 2009.

[58] H. Raiffa, Preferences for multi-attributed alternatives, Journal of Multi-Criteria Decision Analysis 14 (2006) 115-157.

[59] C. Ram, G. Montibeller, A. Morton, Extending the use of scenario planning and MCDA for the evaluation of strategic options, Journal of the Operational Research Society 62 (2011) 817–829.

[60] W. Raskob, F. Gering, V. Bertsch, Approaches to visualisation of uncertainties to decision makers in an operational Decision Support System, in: Proceedings of the 6th International Conference on Information Systems for Crisis Response and Management (2009), Gothenburg.

[61] D. Ríos-Insua, S. French, A framework for sensitivity analysis in discrete multi-objective decision-making, European Journal of Operational Research 54 (1991) 176–190.

[62] S.P. Santos, V. Belton, S. Howick, Adding value to performance measurement by using system dynamics and multicriteria analysis, International Journal of Operations & Production Management 22 (2002) 1246–1272.

[63] K.M. Sayre, Statistical models of causal relations, Philosophy of Science 44 (1977) 203-214

[64] S.P. Schnaars, How to develop and use scenarios, Long Range Planning 20 (1987) 105–114.

[65] P.J.H. Schoemaker, Multiple scenario development: its conceptual and behavioral foundation, Strategic Management Journal 14 (1993) 193–213.

[66] R.W. Scholz, O. Tietje (Eds.), Embedded Case Study Methods. Integrating Quantitative and Qualitative Knowledge, Sage Publications, Thousand Oaks, 2002.

[67] C.R. Schwenk, Strategic decision making, Journal of Management 21 (1995) 471–493.

[68] M.J. Shaw, M.S. Fox, Distributed arti<sup>fi</sup>cial intelligence for group decision support: integration of problem solving, coordination, and learning, Decision Support Systems 9 (1993) 349–367.

[69] T.J. Stewart, A critical survey on the status of multiple criteria decision making theory and practice, Omega 20 (1992) 569–586.

[70] T.J. Stewart, Dealing with uncertainties in MCDA, International Series in Operations Research & Management Science, vol. 78, Springer, 2005, pp. 445–470.

[71] M. Stumptner, An overview of knowledge-based con<sup>fi</sup>guration, AI Communications.10 (1997).111-125

[72] A. Tversky, D. Kahneman, Judgment under uncertainty: heuristics and biases, Science 185 (1974) 1124–1131.

[73] G.H. Tzeng, W.H. Chen, R. Yu, M.L. Shih, Fuzzy decision maps: a generalization of the dematel methods, Soft Computing - A Fusion of Foundations, Methodologies and Applications 14 (2010) 1141–1150.

[74] P. Vincke, Robust solutions and methods in decision-aid, Journal of Multi-Criteria Decision Analysis 8 (1999) 181–187.

[75] A. Volkery, T. Ribeiro, Scenario planning in public policy: understanding use, impacts and the role of institutional context factors, Technological Forecasting and Social Change 76 (2009) 1198–1207.

[76] D. von Winterfeldt, W. Edwards, Decision Analysis and Behavioral Research, Cambridge University Press, Cambridge, 1986.

[77] W. Watthayu, Y. Peng, A Bayesian network based framework for multi-criteria decision making, in: Proceedings of the 17th International Conference on Multiple Criteria Decision Analysis (2004), Whistler, British Columbia CA.

[78] G. Wright, P. Goodwin, Future-focussed thinking: combining scenario planning with decision analysis, Journal of Multi-Criteria Decision Analysis 8 (1999) 311–321.

[79] G. Wright, P. Goodwin, Decision making and planning under low levels of predictability: enhancing the scenario method, International Journal of Forecasting 25 (2009) 813–825.

[80] R. Yu, G.H. Tzeng, A soft computing method for multi-criteria decision making with dependence and feedback, Applied Mathematics and Computation 180 (2006) 63–75.

Tina Comes studied Mathematics, Literature and Philosophy at the Universität Trier, Germany, Université Lille I, France and the Friedrich-Alexander Universität Erlangen— Nürnberg, Germany. She holds a diploma in Mathematics from the Friedrich-Alexander Universität Erlangen—Nürnberg. At present, she works as a researcher in the interdisciplinary research unit on ‘Technique Assessment and Risk Management’ at the Institute for Industrial Production (IIP) at the Karlsruhe Institute of Technology (KIT). Her major research areas are risk management, multi-criteria decision analysis scenario analysis and intelligent distributed reasoning systems.

Dr. Michael Hiete holds a diploma and PhD in Geoecology, both from the Technical University Carolo-Wilhelmina at Braunschweig, Germany. He is an Assistant Professor and the head of the interdisciplinary research team on Technique Assessment and Risk Management' at the IIP at the Karlsruhe Institute of Technology (KIT). Germany. His major research areas include the techno-economic assessment of emission abatement options, the modelling and analysis of critical infrastructure, risk management and multi-criteria decision analysis.

Dr. Niek Wijngaards, received his PhD in 1999 on the topic of self-modifying agent systems using a re-design process. Since 1998 he worked at the University of Canada as a Postdoctoral-Fellow and at the VUA, where he was an assistant professor from 2000 to 2004 at the Intelligent Interactive Distributed Systems group. Since October 2004 he works for Thales Research & Technology Netherlands as senior researcher and program manager. He is fully employed at D-CIS Lab. Wijngaards is involved in research on actor–agent teams as well as their practical applications at e.g. the Dutch Police organisation and the Dutch Railroads.

Prof. Dr. Frank Schultmann is Professor at the Karlsruhe Institute of Technology (KIT) and Director of the Institute for Industrial Production (IIP) and the French-German Institute for Environmental Research (DFIU). In addition, he is Adjunct Professor at the University of Adelaide, Australia. He studied Business Engineering at the Universität Karlsruhe (TH) and received a Ph.D. in Economics from the Faculty of Economics and Business Engineering of the Universität Karlsruhe (TH). Previous to his present positions he was Professor at the Department of Computer Science at the University of Koblenz-Landau and holder of the Chair of Business Administration, Construction Management and Economics at the University of Siegen.

---
otero_id: 21539
otero_key: "QUNWSQ9M"
title: "Using goals to design and verify rule bases"
authors: "P.G. Chander; R. Shinghal; T. Radhakrishnan"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00046-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using goals to design and verify rule bases

P.G. Chander <sup>)</sup>, R. Shinghal <sup>1</sup>, T. Radhakrishnan <sup>2</sup>

Department of Computer Science, Concordia UniÕersity, Montreal, Canada H3G 1M8

## Abstract

The design of rule-based systems is often plagued by errors and anomalies. The verification and validation V and VŽ . processes to detect errors and anomalies in a rule base are complex. Methods that are general enough for comprehensive anomaly detection suffer from heavy computation. Special methods for V and V that have reduced computational needs lack in their scope and applicability. Most of the existing verification tools perform their checking based on the syntax of rule base encoding often ignoring useful meta knowledge of the domain. In this paper, we propose a way to abstract domain knowledge using goals. At the design level, goals are realized in a rule base using one of several design schemes, where a design scheme is a goal-to-hypothesis mapping satisfying certain constraints. At the implementation level, goals are inferred using partially ordered rule sequences called paths. Verification of a rule base can be performed by identifying certain rule aberrations, that can be indicative of the rule base anomalies circularity, ambivalence, redundancy, and deficiency. A case study is presented to highlight that the goal-based approach is useful for preventing rule subsumption a form of redundancy Ž . and for enhancing the run time performance of a rule base.Ž . q 1997 Elsevier Science B.V.

Keywords: Rule-based system; Design schemes; CARD anomalies; Verification and validation

## 1. Introduction and motivation

Conceptually, the design and development of a rule-based system is a combination of comprehension, mapping, and encoding of the knowledge from a domain expert into a set of rules 1 . The compre- <sup>w</sup> <sup>x</sup> hension also called knowledge acquisition is re-Ž . quired in order to acquire the problem solving knowledge from the domain expert. The mapping is a formalization of this knowledge into a task domain identifying the set of tasks associated with problem solving. The rule-base development encodes the task domain representation of the acquired knowledge into a set of rules. Comprehension, mapping, and encoding are done by a knowledge engineer.

The design of rule bases, however, is often plagued by anomalies abbreviated in the literature as CARD <sup>w</sup> <sup>x</sup> 2,3 : Circularity, Ambivalence, Redundancy, and Deficiency. Verification of rule bases entails detecting the CARD anomalies.

Definition 1 Ž . CARD Anomalies A rule base that contains a rule and<sup>r</sup>or an atom such that removing the rule or removing a part of the rule does not affect the functioning of the system, is said to exhibit redundancy. A rule base is ambivalent if it violates domain constraints. Deficiency is the inability of a system to provide an adequate response for a permissible combination of initial evidence. A rule base is circular whenever a set of rules can repeatedly cause one another to fire in an interminable loop.

It is not practical to detect these anomalies manually in large rule bases; procedures to automate their detection are required. Such detection procedures are collectively referred to as rule base verification procedures 2,3 .<sup>w</sup> <sup>x</sup>

## 1.1. Related research

Early works on verification used simple pairwise rule comparisons, see for instance Refs. 4,5 . How-<sup>w</sup> <sup>x</sup> ever, procedures that do not take into account the inference chains in a rule base can miss detecting some anomalies as pointed out by Ginsberg 6 . It <sup>w</sup> <sup>x</sup> has also been observed that additional evaluation perspectives can be obtained if the V and V processes take into account meta knowledge of the domain 7,8 : for example, the extended structure<sup>w</sup> <sup>x</sup> checker in EVA uses the notion of atom synonyms to detect redundant rules, but does not take into account the inference chains in the rule base. For a comprehensive anomaly detection, inference chains need to be considered 9 . But verification, taking <sup>w</sup> <sup>x</sup> into account the inference chains in a rule base, however, has an exponential complexity in the worst case 6,10 . Limiting himself to propositional, not<sup>w</sup> <sup>x</sup> predicate, logic Ginsberg 6 computed labels—the initial evidence required to infer for each final hypothesis to check for redundancy and inconsistency. The COVER verification tool takes into account the linear inference chains in a rule base for anomaly detection, but does not make use of meta knowledge of the domain 2 . <sup>w</sup> <sup>x</sup>

In summary, an effective verification or, moreŽ generally, evaluation procedure for rule-based sys- . tems can be judged using the following three criteria: 1. the extent meta knowledge of a domain is utilized for additional perspectives on anomaly detection;

2. accounting for rule interactions hence, inference Ž chains to improve the scope of anomaly detec-. tion rather than limiting its scope to individual or Ž pairwise rules; and .

3. provisions to control the computation required for computing the transitive closure of rule inferences.

In this paper, we are motivated towards developing a design frame work integrating evaluation for rule-based systems. More specifically, we are interested in the following issues in the development and analysis of rule-based systems:

Ž .a how do we map a design choice to a given implementation?

Ž . b how do we ensure that the implementation, and its associated design restriction if any , representsŽ . part of the acquired knowledge?

Ž .c how does the methodology support restructuring of existing systems say to improve its perfor-Ž mance ?.

Ž . d how do we effectively evaluate the developed rule base conforming to the above criteria?

Though we have developed several evaluation procedures for rule-based systems, in order to conserve the size of this paper, we restrict ourselves to verification. For additional details, we refer the reader to Refs. 11–16 .<sup>w</sup> <sup>x</sup>

The paper is organized as follows. In Section 2, we describe how goal specification can be used to abstract the knowledge of a domain. Goals not only serve to abstract a large body of knowledge, but also set a reference for later verification and validation. Once goals are conceived, the task of realizing them in a rule base entails some restrictions: this results in several design schemes for rule-based systems. Section 2 also explicates how goals are inferred in a rule base using a notion of a rule base path or, simply,Ž path . Section 3 describes a case study of knowledge. restructuring using goal specification 15 . Thus, goal <sup>w</sup> <sup>x</sup> specification is useful not only for development, but for reverse engineering as well. In Section 4, we describe how rule bases developed adhering to our model can be verified for the CARD anomalies by providing our verification perspectives using pathsŽ . and goals. Goal specification can be used to control the computation required for path extraction from a rule base, but those details are described elsewhere to conserve the size of this paper 11 . <sup>w</sup> <sup>x</sup>

## 2. Abstracting domain knowledge by goals

The knowledge acquisition process advocated by us is based on capturing the problem solving in a domain in the form of ‘goal to goal’ progressions as viewed in traditional AI research 17 . In order to <sup>w</sup> <sup>x</sup> solve a problem, a system will transit through a set of states. It is unrealistic to enumerate every possible state that is traversed by the system without some sort of abstraction over the state space. A domain expert solving problems in the domain knows of the typical mile posts that are accomplished as part of solving problems in the domain; thus, they can be specified. Such states are called goals. In addition, the domain expert also specifies constraints associated with the domain called inviolables; an inviolable is a conjunction of hypotheses such that all of them should not be true at the same time. An example of an inviolable is MALE Ž . x <sup>n</sup> PREGNANT Ž . x ; it is obvious that no goal or part of a goal should contain an inviolable. Goals also serve as meta knowledge of the domain, and are useful for later verification and validation 18,14–16 .<sup>w</sup> <sup>x</sup>

![](/api/attachments/QUNWSQ9M/fulltext/images/7226f73d0bd25a76474bad23e6c3679c97fc523378b024d718ae19e527a09fa9.jpg)  
Fig. 1. At the functional requirements stage of the system, the acquired knowledge is mapped to identify goals, and inviolables. Note, the goals at this stage only abstract the acquired knowledge. The decision of how to represent and realize each goal in the system would be a design decision.

The process of identifying and mapping the acquired knowledge into goals is not a mechanical process 19 . Often, the extent to which a domain<sup>w</sup> <sup>x</sup> expert communicates the knowledge clearly and unambiguously, the skill of the knowledge engineer, and the rigor of the knowledge acquisition process play a major role. This process is similar to the way problem concepts are identified and mapped to operators and states in SOAR 17 . To illustrate, we show <sup>w</sup> <sup>x</sup> an example from Ref. 20 , identifying goals and <sup>w</sup> <sup>x</sup> inviolables see Fig. 1 .Ž .

Every goal, when translated into a first order logic formula, consists of a conjunction of hypotheses, where each hypothesis is represented as a logic atom Ž . a predicate with its arguments . To illustrate, Fig. 2 shows the translation of some of the goals identified in Fig. 1 into a conjunction of atoms denoting hypotheses. The atoms present in goals are called goal atoms; the other atoms are non-goal atoms, they being needed for rule encoding. While solving problems, two kinds of goals are inferred: goals that facilitate inferring a solution, and the goals that represent the solutions to problems in the domain. The former are called intermediate goals and the latter final goals. Typically, the intermediate goals are those that are achieved in order to infer a final goal, and a final goal is part of some solution.

<table><tr><td>Goal Identified</td><td>Represented concept</td><td>Goal Translation</td></tr><tr><td>Biliary Cirrhosis</td><td>A diagnosis representing biliary cirrhosis.</td><td>P-BILL-CIRR(x, sex, case-hist)</td></tr><tr><td>Multiple liver cysts</td><td>An intermediate diagnosis indicating cysts in liver.</td><td>CYSTS(x, sex, tchnq, hist)</td></tr><tr><td>Abdominal Pain</td><td>A symptom associated with polycystic disease.</td><td>PART(x, sex, desc) ∧ SYMPTOM(s-desc)</td></tr></table>

Fig. 2. Translating some of the goals identified in Fig. 1 into a conjunction of first order logic atoms.

Definition 2 Ž . Intermediate and Final Goals Goals that are inferred in order to facilitate reaching a solution are called intermediate goals. The goals that are used for indicating domain solutions are called final goals.

In our model, problem solving in a domain is viewed as a succession of goal inferences until a set of final goals are inferred. This progression can be conceptually portrayed by means of an AND<sup>r</sup>OR graph called the goal graph of the domain, or, simply, the goal graph. Fig. 3 shows a goal graph for the example medical domain used in Fig. 1 20 . Each<sup>w</sup> <sup>x</sup> node in the goal graph corresponds to a goal, where the unshaded nodes denote goals that are not solutions, and the shaded nodes denote solutions. A connector in this graph is from a set of goals $G =$ $\{ g _ { i _ { 1 } } , g _ { i _ { 2 } } , \ldots , g _ { i _ { n } } \}$ to a goal $g ,$ where $g \not \in G .$ . A circular mark in the connector near $g$ indicates that goal $g$ is inferable from goal $g _ { i _ { 1 } }$ and goal $g _ { i _ { 2 } }$ and . . . goal $g _ { i _ { n } }$ . A connector thus indicates the conceptual encoding required to infer a given goal g from a set G of goals. The different connectors to a goal depict the different alternatives for inferring that goal. Permissible initial evidence are said to be level-0 goals; other inferred goals are at higher levels, the first digit of the subscript indicating the level of a goal.

![](/api/attachments/QUNWSQ9M/fulltext/images/7540aaf3b7ad1d87ad13cfa90eb27a5ea6f3f192c975bf861645b5ae548d60a8.jpg)  
Fig. 3. A sample goal graph from a medical domain to diagnose Ž liver and biliary disorders to abstract important states associated . with problem solving.

In the implementation of a rule base, domain knowledge is encoded using a set of if . . . then . . . rules 17 . Problem solving at this level takes place <sup>w</sup> <sup>x</sup> by rule firings to infer hypotheses representing the various domain knowledge concepts 17,21 . The<sup>w</sup> <sup>x</sup> syntax of the rules to encode the acquired knowledge partitions hypotheses inferred in the rule base into two types: intermediate and final. An intermediate hypothesis is one that occurs in the consequent of at least one rule and in the antecedent of at least one rule. A final hypothesis is one that occurs in the consequent of at least one rule, but never in the antecedent of a rule.

A design issue arises in mapping the intermediate and final goals in a goal specification to the intermediate and final hypotheses in a rule base. This mapping is necessary because it explicates the link between the semantic representation of the acquired knowledge using goals to its actual syntactic real-Ž . ization using hypotheses . A design scheme for a Ž . rule base is a realizable restriction imposed in mapping goals to hypotheses for satisfaction of a set of domain dependent and independent criteria.

Definition 3 Ž . Design Scheme A design scheme D is an ordered pair of partial mappings $< \mu _ { 1 } , ~ \mu _ { 2 } >$ such that:

$$
\begin{array}{l} \mu_ {1}: \mathcal {F} \mapsto \mathrm{H} _ {\mathrm{i}} \cup \mathrm{H} _ {\mathrm{f}} \\ \mu_ {2}: \mathcal {I} \mapsto \mathrm{H} _ {\mathrm{i}} \cup \mathrm{H} _ {\mathrm{f}} \end{array}
$$

where $\mathcal { F }$ is the set of final goals, $\mathcal { I }$ is the set of intermediate goals, $\mathrm { H } _ { \mathrm { i } }$ is the set of intermediate hypotheses, and $\mathrm { H } _ { \mathrm { f } }$ is the set of final hypotheses. The mapping is partial because not all hypotheses need be goal constituents.

An analysis of the mapping restrictions provide, however, different design schemes for structuring rule bases. This is described next.

## 2.1. Designing rule base structures to realize goals

There are theoretical and pragmatic aspects that need to be considered in designing rule-based systems. A single design scheme may not be suitable for all domains; thus, we need a design schemata. A design schemata requires the following: 1 a prag-Ž . matic component describing the qualitative aspects of the design schemes contained, and 2 a theoreti-Ž . cal component that outlines the relationship between the design schemes to facilitate choosing a design scheme. More specifically, the pragmatic component dictates the choice between design schemes depending upon the relative importance given to development, evaluation, and maintenance. The theoretical component allows for further compromises between development and maintenance by formalizing the properties of design schemes, and its use. However, the mapping restriction that is imposed at the design phase between goals and hypotheses is not unique. This can be stated as follows:

Issue: Let $\mathbf { f } = \mathbf { A } _ { 1 } \wedge \mathbf { A } _ { 2 } \wedge , \ldots$ be a final goal and $\mathbf { i } = \mathbf { A } _ { 1 } ^ { \prime } \wedge \mathbf { A } _ { 2 } ^ { \prime } \wedge , . .$ . be an intermediate goal specified, where the A’s are hypotheses. The question arises: What properties should $\mathbf { A } _ { 1 } , \mathbf { A } _ { 2 } , \ldots$ . and ${ \bf A } _ { 1 } ^ { \prime }$ $\mathrm { A } _ { 2 } ^ { \prime } , \ldots$ . satisfy in the rule base?

The possible choices for the constituent hypotheses of final and intermediate goals are summarized in Fig. 4. We will use the notation <sup>-</sup> Fn, Im <sup>)</sup> to denote a design scheme, in analyzing the relationships between the 25 possible design schemes from Fig. 4.

While all the choices in Fig. 4 are realizable restrictions resulting in various design schemes, some of them can be counter intuitive. Consider for example restriction I1 for intermediate goals that requires them to be composed of only final hypotheses. In this case, the intermediate goals cannot help infer any final goals because final hypotheses cannot be causal to other final hypotheses. A similar observation is applicable to restriction F4 for final goals. Thus, owing to counter intuitive semantics of the specification, we recommend avoiding all design schemes with either of these mapping restrictions. Further, restriction I5, where intermediate goal composition is unconstrained, is discouraged because specification of intermediate goals can be uncontrolled, and such ad hoc specification may not reflect the intent of the domain expert. We, however, allow restriction F5 for ease in solution specification to facilitate functional, structural and<sup>r</sup>or empirical validation 22,18,23,11 , but care should be exercised in<sup>w</sup> <sup>x</sup> specifying solutions when using this restriction. In general, the choice of which mapping to choose for a given goal realization entails several factors. We give below two important criteria that play a major role in making this choice. For additional details, refer to Chander et al. 15 .<sup>w</sup> <sup>x</sup>

<sup>Ø</sup> The extent of analysis and synthesis components in a domain influences the type of the hypothesis constituent in goals, and hence is a factor in determining a goal-to-hypothesis mapping.

<sup>Ø</sup> For large rule bases, the mapping should also facilitate ease in refining a given goal specification because such refinements are quite often needed to control the computation required for path extraction and for subsequent evaluation 11,12 .<sup>w</sup> <sup>x</sup>

Unfortunately, there is no procedure to choose a design scheme from the set of schemes for a domain. In other words, for an arbitrary domain and development criteria, there is no known step-by-step method by which we can choose a design scheme from a set of design schemes. Often, the skill and experience of the knowledge engineer, size of the proposed system, the extent of analysis and synthesis components in problem solving used in the domain, domain constraints expressed though domain dependent criteria, and long term objectives such as the extent ofŽ maintenance expected expressed through domain . independent criteria dictate whether to reject or select a design scheme from its characteristics 24–26 .<sup>w</sup> <sup>x</sup> As an example consider a domain dependent criteria where states accepted as solutions can also lead to Ž . perhaps more refined solutions. For this domain, design schemes with choice F1 for final goals is not the right choice because solution causality cannot be captured by this choice for final goals. On the other hand, if one cannot infer additionally from domain solutions, or if the solutions are mutually exclusive then design schemes with choice F1 are perhaps more appropriate. Appendix A gives an example of choosing a design scheme for a particular domain.

<table><tr><td>Hypotheses in a final goal f(F1) All are final hypotheses.(F2) At least one hypothesis is final.(F3) At least one hypothesis is intermediate.(F4) All are intermediate hypotheses.(F5) No constraints.</td><td>Hypotheses in an intermediate goal i(I1) All are final hypotheses.(I2) At least one hypothesis is final.(I3) At least one hypothesis is intermediate.(I4) All are intermediate hypotheses.(I5) No constraints.</td></tr></table>

Fig. 4. The choices for constituent hypotheses in a final goal f and an intermediate goal i, provided neither f nor i contains an inviolable.

An examination of the relationship between the various design schemes shows that some scheme mappings are more general than others. This allows us to identify a relationship called inheritance between the design schemes. Inheritance between the design schemes is important because it allows for compromises in development vs. maintenance and also influences certain system qualities understanda-Ž bility, maintainability, etc. , and thus plays a role in. design scheme selection. The details, however, are beyond the scope of this paper and the reader is referred to Refs. 27,28 .<sup>w</sup> <sup>x</sup>

Goal specification and the various design schemes are not constrained for only development. Goal specification can be usefully utilized for reverse engineering as well. We describe in Section 3 a case study for optimization of rule bases.

## 2.2. Modeling goal inference in problem solÕing

In our model, problem solving is viewed as the inference of a succession of goals until a set of final goals are inferred. In general, a set of rule firings are required before a goal can be inferred because goals are conjunctions of hypotheses. Thus, to abstract problem solving that takes place at the rule base level in terms of the goals specified for the domain, we must explicate the relationship between a set of rules in the rule base inferring a goal.

A rule base constructed based on a given goal specification and a design scheme implements the problem solving by rule sequences that progress from goal s to goal from the given goal specifica-Ž . tion. Every such rule sequence $\varPhi$ in the rule base is said to have realized a connector in the goal graph; thus, there may be more than one rule sequence to realize a given connector. These rule sequences are called rule base paths or, simply, paths , the termŽ . used in order to be consistent with the structuralŽ . validation terminology 29,8 . If a rule<sup>w</sup> <sup>x</sup> $\boldsymbol { \mathrm { r } } _ { j }$ occurs immediately after rule $\mathbf { r } _ { i }$ in such a sequence $\Phi _ { \pmb { \imath } }$ , then a non-goal atom in the consequent of $\mathbf { r } _ { i }$ unifies with an atom in the antecedent of $\mathbf { r } _ { j } .$ Rule $\boldsymbol { \mathrm { r } } _ { j }$ in the rule sequence $\varPhi$ is said to be accessible from rule $\mathbf { r } _ { i } { \dot { , } }$ goal atoms inferred within the sequence $\varPhi$ contribute only to the goal being inferred. A path, thus, localizes the rule interactions hence, the inference chainsŽ . that occur in a goal-to-goal progression. In addition, the partial ordering captures inference chains that are not only linear, but those that are partially ordered as well.

Just as a goal graph can be used to pictorially depict the relationship between the goals, details of goal realization at the rule base structural level can also portrayed by a graph. Such a graph depicting paths in a rule base is called the rule graph. A rule graph is a labeled directed graph. Each node in a rule graph corresponds to a rule. The atoms inferred by firing a rule $\mathbf { r } _ { i }$ are shown by labeling the directed arcs from $\mathbf { r } _ { i }$ as $A _ { i } ^ { 1 } , \ A ^ { i 2 } , \ldots$ . An arc labeled $A _ { i } ^ { n }$ from $\mathbf { r } _ { i }$ to $\boldsymbol { \mathrm { r } } _ { j }$ indicates that the atom $A _ { i } ^ { n }$ in the consequent of $\mathbf { r } _ { i }$ unifies with an atom in the antecedent of $\mathbf { r } _ { j } .$ Goal atoms inferred by rules in a path are shown by directed arcs incident on the right vertical bar representing goal g. An example rule graph of a path is shown in Fig. 5.

![](/api/attachments/QUNWSQ9M/fulltext/images/fd95c3c651c9b9d739dcdcd0442a5b58176a8ff61d5e770cbef08395296a9201.jpg)  
Fig. 5. A rule graph representation of a path. The rule sequence infers goal $g$ once goal $g ^ { \prime }$ is inferred.

<table><tr><td>Goal Graph</td><td>Rule Graph</td></tr><tr><td>The sequence in which goals are inferred.</td><td>The sequence in which rules are fired.</td></tr><tr><td>An AND-OR graph.</td><td>A labeled directed graph.</td></tr><tr><td>Nodes represent goals, some of which are solutions.</td><td>Rectangular nodes represent rules.Vertical bars represent goals.</td></tr><tr><td>Connectors represent paths that portray order of inferring the goals.</td><td>Directed edges represent atoms inferred in rule firings.</td></tr></table>

Fig. 6. A comparison of the rule and goal graphs.

Goal graphs and rule graphs are compared in Fig. 6.

Formally, every path is a poset, denoted by $< \sigma$ $\succ >$ , where  is the set of rules in the path, and <sup>%</sup> is a partial ordering relation between the rules of the path defined as follows:

$\forall \mathbf { r } _ { i } , \mathbf { r } _ { j } \in \sigma ) \mathbf { r } _ { i } \succ \mathbf { r } _ { j }  \mathbf { r } _ { j }$ is accessible from $\mathbf { r } _ { i }$

A path can also be represented by specifying the partial ordering relation <sup>%</sup> between the rules in the path. Thus, the path of Fig. 5 can be represented as $\mathbf { \Sigma } \succ = \{ < \mathbf { R } _ { 1 } , \ \mathbf { R } _ { 2 } > \ , \ \mathbf { \Sigma } < \mathbf { R } _ { 1 } , \ \mathbf { R } _ { 3 } > \ , \ < \mathbf { R } _ { 2 } , \ \mathbf { R } _ { 4 } > \ , \ \mathbf { \Sigma } <$ $\mathbb { R } _ { 3 } , \mathbb { R } _ { 4 } > \}$

The extent to which a given rule base realizes the acquired knowledge of goal inference is reflected by the paths in the rule base; they are collectively said to portray the structure of the rule base.

Definition 4 Ž . Rule Base Structure The structure of a rule base or, simply structure is defined asŽ . ² <sub>G</sub>, , <sub>D</sub>: where <sub>G</sub> is the goal specification of the domain, II is a set of rule base paths, and $\mathcal { D } = \langle \mu _ { 1 } , \mu _ { 2 } \rangle$ is the adhered design scheme, such that:

$$
\left(\forall \Phi \in \Pi\right) (\exists G, g) (G \subset \mathscr {G}) (g \in \mathscr {G}) G \wedge \Phi \vdash g\tag{1}
$$

$$
(\forall g \in \mathcal {G}) \mathrm{H} \supseteq \left\{ \begin{array}{l} \mu_ {1} (g) \text {   if   } g \text {   is   a   final   goal } \\ \mu_ {2} (g) \text {   if   } g \text {   is   an   intermediate   goal } \end{array} \right.\tag{2}
$$

where H is the set of all hypotheses in the rule base.

The second condition in the above definition simply asserts that goals are inferred using rule base hypotheses only. Thus, if any external actions are to be modeled as part of a goal inference, it should still be represented using a hypothesis in the rule base; the action can take place following the inference of this hypothesis. During system evaluation, this can ensure that a given rule fires correctly by examining the inferred goal. This is particularly useful, when simulating external actions that could take placeŽ during field operation as part of a rule can be costly,. or cannot be done during development. As an example, consider a life support system that monitors patient breathing, and turns on additional oxygen when oxygen intake falls below a threshold. In the system implementation, a rule should fire when the oxygen intake falls below a threshold, and turn on the appropriate oxygen equipment. In our model, this action should be represented using an hypothesis in the rule consequent in addition to executing the appropriate action. During system development, the rule firing can then be mapped to a path which can be inspected to check if the rule fires under the correct conditions. Note, the development site may or may not have the associated control equipment in this case owing to its cost.

The extraction of paths from a rule base using a given goal specification is a non-trivial problem because procedures that extract inference chains from a rule base have an exponential complexity in the worst case 6,29 . However, goal specification can be<sup>w</sup> <sup>x</sup> used to control the computation required to because it can be refined to cut down the number of rule dependencies to be enumerated during path extraction 11 . We have developed a tool called Path<sup>w</sup> <sup>x</sup> Hunter to extract the paths in a rule base from a given goal specification. Path Hunter has been used successfully to extract the paths from a large rulebased system containing 435 rules 11 . The extrac-<sup>w</sup> <sup>x</sup> tion of paths and the goal graph realized in the rule Ž base is termed structure extraction, and it influences. a variety of evaluation processes for rule-based systems 14,8,6,29,15,18 . To model the problem solv-<sup>w</sup> <sup>x</sup> ing that occurs due to rule firings, one must extract the goal graph realized in a rule base. A goal graph extraction process from a rule base should enumerate all the connector chains from permissible initial evidence to a final goal. This progression can be easily captured because every path in the rule base represents a connector. Thus, we only need to enumerate path sequences required from a given initial evidence until a final goal is inferred 14 . Such a sequence of<sup>w</sup> <sup>x</sup> paths is called a route.

Definition 5 Ž . Relevant and Irrelevant Routes A route is a sequence of one or more paths. A route from a level-0 goal to a solution is called a relevant route; any other route from a level-n goal to a goal $g ^ { \prime } ,$ , where $n \geq 1$ or $g ^ { \prime }$ is not a solution, is called an irrelevant route.

Irrelevant routes indicate that some intermediate goals are not useful for inferring final goals, and<sup>r</sup>or some final goals are not reachable 14 . Such routes<sup>w</sup> <sup>x</sup> and goals in the goal graph are thus not useful for problem solving and can indicate redundancy and<sup>r</sup>or deficiency in the rule base 15 .<sup>w</sup> <sup>x</sup>

## 3. Goal supported restructuring: a case study

Goal specification can be used for rule base restructuring to improve rule base performance, and is also useful for preventing some coding errors. A common problem when encoding rules or ruleŽ groups whose consequent action depends upon the. Ž . specificity of the input conditions is rule subsumption a form of rule redundancy : for example, ruleŽ . R: A™C subsumes rule R : A<sup>n</sup>B™D 30 . More<sup>w</sup> <sup>x</sup> generally, rule $\mathbf { r } _ { i }$ is said to subsume rule $\mathbf { r } _ { j } ,$ whenever the antecedent of $\mathbf { r } _ { i }$ is more general than the antecedent of $\mathbf { r } _ { j } .$ Rule subsumption in a rule base is undesirable because it can produce unexpected results during problem solving 30 . It can also in-<sup>w</sup> <sup>x</sup> crease the amount of work an inference engine has to do when checking for rule activations because it causes more number of rules to be activated for a given set of input conditions 16 . In addition, a<sup>w</sup> <sup>x</sup> direct encoding of the domain knowledge without structuring it can lead to more work on the part of the inference engine because the number of combinations it should enumerate for determining which rules are ready to fire can be quite large 21,16 . A<sup>w</sup> <sup>x</sup> systematic identification of goals and encoding them as rule group discriminators during rule base development, however, can be used to prevent rule subsumption and performance degradation by limiting Ž the number of combinations to be searched by an inference engine for rule activations . The following . case study, that restructures an existing rule base using goals, illustrates the above aspects. Goal specification was applied successfully for optimizing the rule base of an expert system designed to perform library search 16 . The system functions as follows:<sup>w</sup> <sup>x</sup> it is given a set of input search fields associated with a document such as title, author, subject . . . , up to a total of 13 fields. Typically, a subset of these is entered by the user. The system then checks for the location of the document using a data base system, and having obtained the location eventually retrieves the document. The first prototype version uses aŽ . sample library data base at a central site. This prototype was developed under CLIPS 21 consisting of<sup>w</sup> <sup>x</sup> 205 rules.

```lisp
(defrule five-fields-data-not-match
  (declare (salience 91))
    ?addr1 <- (phase read ?type1 $?data1)
    ?addr2 <- (phase read ?type2&~?type1 $?data2)
    ?addr3 <- (phase read ?type3&~?type1&~?type2 $?data3)
    ?addr4 <- (phase read ?type4&~?type1&~?type2&~?type3 $?data4)
    ?addr5 <- (phase read ?type5&~?type1&~?type2&~?type3&~?type4 $?data5)
    (not (phase read ?type&~?type1&~?type2&~?type3&~?type4&~?type5$?));
    (not (match-field $?))
=>
  (retract ?addr1 ?addr2 ?addr3 ?addr4 ?addr5)
  (assert (error-mess Data do not match.))
)
```  
Fig. 7. An example rule from the library reference expert system.

In this application, however, the knowledge obtained from the human reference librarians the do-Ž main experts was translated to handle the various. input fields while searching for a relevant document. One such rule is shown in Fig. 7. This rule is activated when the user enters five input search fields, but they do not match any of the existing document descriptions.

When a direct translation is done as shown in Fig. 7 to check whether each input field is different from the other using the ‘&’ and ‘<sup>;</sup> ’ operators of CLIPS, it resulted in rule subsumption and an enormous computational overhead. The reason is as follows. In the system, rules that handle i-fields entered subsume the rules that handle the case Ž . i <sup>q</sup> 1 -fields entered, whereas the handling of i input fields and i<sup>q</sup>1 input fields are supposed to be exclusive. This subsumption arises because there are no discriminators coded into the rules to distinguish more focussed search specifications from general search specifications. As a result, a huge amount of pattern matching takes place, and a large number of rules are activated all the time though they do not fire when theŽ . number of input fields is close to 13. Note, the use of salience a form of rule priority assignment in CLIPSŽ . to force sequentiality so that i <sup>q</sup> 1 input fields get priority over rules that handle i input fields does not always work.

```asm
(defrule test-rule ;; A typical rule simplified from its original form
    (phase ?x)
    (phase ?y&~?x)
    (phase ?z&~?y&~?x)
=> 
    (printout t ?x ?y ?z) ; a sample action
)

CLIPS> (matches testrule)
Matches for Pattern 1
f-1
f-2
f-3
Matches for Pattern 2
f-1
f-2
f-3
Matches for Pattern 3
f-1
f-2
f-3
Partial matches for CEs 1 - 2 +----+
f-3,f-2 | Activations |
f-3,f-1 | f-3,f-2,f-1 |
f-1,f-3 | f-3,f-1,f-2 |
f-2,f-3 | f-1,f-3,f-2 |
f-2,f-1 | f-2,f-3,f-1 |
f-1,f-2 | f-1,f-2,f-3 |
Partial matches for CEs 1 - 3 | f-2,f-1,f-3 |
f-3,f-2,f-1 +----+
f-3,f-1,f-2
f-1,f-3,f-2
f-2,f-3,f-1
f-1,f-2,f-3
f-2,f-1,f-3
```  
Fig. 8. Run time analysis of a typical simplified rule in the rule base of the library reference expert system.Ž .

![](/api/attachments/QUNWSQ9M/fulltext/images/e0d0bbdb2d0a6581e0ed65ccdee65614d9822248c6c3a36408b4dc13fd1144af.jpg)  
Fig. 9. Restructuring the sample rule shown in Fig. 8.

When translating the rule in Fig. 7 and others internally, and during pattern matching the inference engine will have to do an enormous amount of error checking in trying to satisfy the antecedent constraints. Combined with the subsumption that is existing between the rules, the number of pattern combinations required to check which rules are enabled would be of factorial complexity with respect to the input fields because all possible permutations of the input fields have to be considered by the inference engine while instantiating the antecedent variables. This is illustrated in Fig. 8 that portrays the structure of a typical rule in the rule base and its run-time behavior. In fact, the system does even run when the number of input fields is more than six.

In Fig. 8, it is assumed that the initial facts in the working memory are phase author , Ž . Ž f-2: phase title , and . Ž . f-3: phase subject . The specific values associated with the fields are not shown for simplicity. The abbreviation CE n–m refers to a combination of facts that partially satisfy the antecedent.Ž . The activations refer to the number of times the rule can fire. Note that the number of activations of the rule is $6 \left( { \it { \Delta } } = 3 ! \right)$ . In addition, this rule subsumes every rule group that handles more than three input fields,Ž . thus increasing the pattern matching computation.

![](/api/attachments/QUNWSQ9M/fulltext/images/b8462a04a69217763231972d6f12cbf4ac1ca113d5f4fea95bea3d6e453b0d29.jpg)  
Fig. 10. The restructured rule based on additional level-0 goals.

An analysis of encoding of knowledge in rules such as the one in Fig. 7 indicates incorrect and inadequate design of atoms to reflect the captured knowledge. We need to identify predicates and goals Ž . level-0 in this case to reflect the extent of input handling. In addition, we also need to make use of the fact that rules that handle i-fields should be treated exclusively from rules handling a different number of input fields. Thus, we need two level-0 goals: FIELD-INPUT Ž . n that says how many field are input, and FIELDS $( x , y , \dots )$ that records the fields that actually input. For example, if the fields author, title and subject are entered, then these atoms are respectively, FIELD-INPUT 3 and FIELDSŽ . Ž . author, title, subject , and must be asserted as initial facts before the system is to run. The atom FIELD-INPUT Ž .i groups and discriminates rules handling i input fields from rules that handle j input fields, where $i \neq j .$ The arguments of the predicate FIELDS structures the antecedent of the rules so that the variables have only one unique instantiation for a given set of input fields no permutation is neces-Ž sary . The effect of such restructuring applied to the. sample rule in Fig. 8 is shown in Fig. 9a, and its execution trace for the same input augmented by the Ž atom FIELDS author, title, subject is shown inŽ .. Fig. 9b.

With the added level-0 goals, the rule shown in Fig. 7 is restructured as shown in Fig. 10.

![](/api/attachments/QUNWSQ9M/fulltext/images/65fbb2f4a57460a4a93e0bfe88ab9535dfa22380c55639fba42744dcc3cb1d55.jpg)  
After goal based restructuring.  
Fig. 11. The effect of goal based restructuring in the library reference expert system. Individual, autonomous rule groups are formed consistent with the way problems would be handled in the domain.

These modifications cut down the subsumption between rules and the inference engine computation required to check for rule activations as there are no more elaborate error checks forced as part of pattern matching. This enabled the system to handle the full thirteen field input. In addition, the goals also modularized the system by helping to group rules handling i input fields to be treated independently of rules handling field number different from i, making the analysis of the rule base easier because each group is typically not more than seven to eight rules. The effect of the goal based restructuring is shown in Fig. 11.

## 4. Detecting CARD anomalies using goals and paths

Rule base verification entails the detection of CARD anomalies in a rule base. Redundancy is the result of unwanted, or excess rules and atoms; deficiency refers to missing knowledge; ambivalence exists whenever an inviolable becomes true; and circularity exists due to circular rule enablements causing potentially infinite loops, but, more importantly, indicates the presence of circular and hence, Ž possibly inaccurate reasoning in the system. .

In our approach, the detection of CARD anomalies requires the identification of certain rule situations that can be indicative of these anomalies. They are called rule aberrations because they indicate an abnormality in the system 15 . <sup>w</sup> <sup>x</sup>

Definition 6 Ž . Rule Aberration The anomaly set <sub>A</sub> of a rule base is the set of anomalies that can be present in a rule base typically the CARD anoma- Ž lies . A rule aberration in a rule base consists of a set. of paths that portray the manifestation of one or more elements from the anomaly set <sub>A</sub>. If , a set of paths in a rule base, is an aberration, then we can state that:

$$
\pi \vDash a \subseteq \mathcal {A}.
$$

Goal specification, paths, and the extracted goal graph allow for a comprehensive detection of the CARD anomalies in a rule base at any stage during its construction: detect paths that adhere to one or more rule aberrations. We give below a list of ten aberrations, and provide comments about the possible anomalies these aberrations could indicate. We, however, do not claim that the list is exhaustive. Studying the various aberrations provides a different perspective on anomaly detection in rule bases. Moreover, by basing our study on rule sequences pertinent to problem solving rather than individual rules, we capture the rule interactions as well. Prior to the application of the aberration specifications below, it is assumed that the relevant and irrelevant routes from the goal graph see definition 5 haveŽ . been extracted from the rule base 14 . For convenience, an informal description of such a procedure appears in Fig. 12.

```txt
Obtaining all relevant routes, and irrelevant routes culminating on a final goal.
1. Select a final goal f.
2. Starting from f, build recursively the goal graph containing all the goals from which f can be inferred.
Obtaining irrelevant routes that terminate on intermediate goals.
1. Start from every intermediate goal i that has not appeared in any of the routes after steps 1 and 2 of the above procedure are applied to all the final goals.
2. For such intermediate goals i build recursively the goal graph containing all the goals from which i can be inferred to obtain irrelevant routes that culminate on the intermediate goal i.
```  
Fig. 12. Determination of relevant and irrelevant routes in a goal graph.

The identification of specific rules and atoms that may be causal to an anomaly in the rule base is called flagging. Our procedures flag rules to make the knowledge engineer aware of them; on further examination, the knowledge engineer may leave a flagged rule unchanged, edit the flagged rule, or may add other rules to the rule base so that the flagged rule is no longer causal to the anomaly. Below, we describe a list of aberrations for redundancy 29 .<sup>w</sup> <sup>x</sup> Note, these aberrations can be caused due to deficiency in the system as well. An example system is presented in Appendix B to illustrate the manifestation of these aberrations.

Aberration 1 ŽRedundancy detection using route irrelevancy. Motivation: A rule that does not con-. tribute to problem solving is redundant.

begin

For all rules r do

if all routes in which r appears are irrelevant or empty, then flag r as potentially redundant;

end

A rule that does not appear in any path is not useful for inferring any goal, and hence redundant. More generally, if a rule appears only in irrelevant routes, then it does not contribute to solving any problem in the domain because an irrelevant route either does not begin from initial evidence, or does not end in a solution. Hence, such a rule that appears only in irrelevant routes could be redundant. Similarly, a rule does not contribute to problem solving if it does not appear in any route.

Aberration 2 Ž . Detection of redundant rule chains. Motivation: Rule chains that infer common goals<sup>r</sup>atoms are indicative of redundant work in the system.

A rule chain as used in the literature 31 is a<sup>w</sup> <sup>x</sup> linear sequence of rules. Aberration 2 is used to detect redundant rule chains.

begin<sup>r</sup> <sup>)</sup> For redundancy of rule chains; See Nguyen 31 ; we also enable detection of redun-<sup>w</sup> <sup>x</sup> dant rules <sup>)r</sup>

1. Flag paths appearing only in irrelevant routes as redundant.

2. For any two paths $\varPhi _ { 1 }$ and $\varPhi _ { 2 }$ ,

Ž .i if the goals required for $\varPhi _ { 1 }$ subsume the goals required for $\varPhi _ { 2 }$ , and the goal inferred by $\varPhi _ { 1 }$ subsumes the goal inferred by $\varPhi _ { 2 }$ , then flag $\varPhi _ { 1 }$ and $\varPhi _ { 2 }$

$\big / ^ { * }$ For efficiency, we may consider only relevant routes $^ * /$

3. For any two paths $\varPhi _ { 1 }$ and $\varPhi _ { 2 }$ where each appears in at least one relevant route

Ž .i if goals required for $\varPhi _ { 1 }$ is subsumed by the goal s required forŽ . $\varPhi _ { 2 }$ , and

Ž . ii if goal inferred by $\varPhi _ { 2 }$ subsumes goal inferred by $\boldsymbol { \varPhi } _ { 1 } .$ , then flag $\varPhi _ { 1 }$ and $\varPhi _ { 2 }$ ;

$\big / ^ { * }$ For example, if goal atoms inferred by $\varPhi _ { 2 }$ is a subset of the goal atoms inferred by $\varPhi _ { 1 }$ , then flag rules in $\varPhi _ { 2 }$ not appearing in any other path. <sup>)</sup>r

end.

The method in Nguyen 31 will flag the above<sup>w</sup> <sup>x</sup> rule chains, but their approach to the extraction of rule chains may not be practical for large rule bases. We, however, efficiently extract paths using our path hunter tool 11 . Note, because of the partially or-<sup>w</sup> <sup>x</sup> dered nature of paths, we flag not only rule chains that are linear, but those that are partially ordered as well.

Aberration 3 Ž . Detection of redundant atoms. Motivation: Multiply inferred atoms in a path may be redundant.

The intuition behind aberration 3 for detecting redundant atoms is that whenever atoms are inferred by a rule r, if some other rule s always fire to inferŽ . these additionally, then these atoms in the consequent of r are possibly redundant.

begin<sup>r</sup> <sup>)</sup> Based on goal redundancy $^ * /$

1. For all paths $\Phi ,$ if more than one rule infers the set of goal atoms for goal g inferred by do

Ž .i Let $X \colon =$ set of goal atoms that are multiply inferred.

Ž . ii if any subset Y of X is multiply inferred in all paths in which these goal atoms, are inferred, flag this subset of goal atoms.

Ž . iii if a toe rule r in  has goal atoms only from the set Y in ii above, flag rule r.Ž .

$\big / ^ { * }$ a complementary step to step 1; applied to non-goal atoms; <sup>r</sup>

2. For all paths $\Phi ,$ let X be the set of dangling non-goal atoms

Ž . Ž . i if non-goal atoms in a subset of X are dangling in every path they appear, flag this Ž . sub set of non-goal atoms.

Ž . ii For all rules $\mathbf { r } _ { 1 }$ that infer some dangling nongoal atoms in a subset of Ž . X above, and some other consumed non-goal atoms, if some other rule s infer the consumed non-goal atoms in ev-Ž . ery path where $\mathbf { r } _ { 1 }$ appears, flag $\mathbf { r } _ { 1 }$ end.

Two types of non-goal atoms can be identified in a path: ‘dangling’ and ‘consumed’. A dangling nongoal atom in a path is an atom in the consequent of a rule, but does not unify with an atom in the an-Ž tecedent of any other rule in the path see atom ${ \bf A } _ { 3 } ^ { 1 }$ in Fig. 5 . A consumed non-goal atom is one that is . in the consequent of a rule in a path that unifies with an atom in the antecedent of some rule in the path Ž see atom ${ \bf A } _ { 1 } ^ { 1 }$ in Fig. 5 . In this aberration, if atom . $\mathsf { A } _ { 1 } ^ { 3 }$ is dangling in every path it appears, then it is flagged. In addition, step 1 iii of this aberrationŽ . flags redundant toe rules rules that infer only goalŽ atoms in a path whenever their consequent is in- . ferred by other rules in every path they appear.

Aberration 4 Ž . Subsumed rules. Motivation: Use the meta knowledge of goals to identify rules that are functionally equivalent to each other.

The traditional methods flag duplicate rules and rules of the form a™b and a $\wedge \mathrm { ~ c ~ } \to \mathrm { ~ b ~ }$ , where the latter is subsumed by the former. Using paths, however, a more general form of detection is possible. Let ${ \bf r } _ { 1 } \colon { \bf A } _ { 1 } \ \wedge \ { \bf A } _ { 3 } $ H and $\mathbf { r } _ { 2 } \colon \mathbf { A } _ { 1 } \ \wedge \ \mathbf { A } _ { 2 }  \mathbf { H } ^ { \prime }$ be any two rules such that $\mathbf { A } _ { 3 }$ is a goal atom, the remaining atoms are non-goal, and the H’s represent hypotheses which can be a conjunction of atoms. Further, let H subsume $\mathrm { H } ^ { \prime }$ . Then, the rule pair ${ < \bf { r } _ { 1 } }$ $\mathbf { r } _ { 2 } >$ is flagged redundant if the following conditions hold: i if every path in whichŽ . $\mathbf { r } _ { 1 }$ appears has at least one rule that infers $\mathbf { A } _ { 2 }$ in other words, wheneverŽ $\mathbf { r } _ { 1 }$ fires, $\mathbf { r } _ { 2 }$ can also fire then perhaps. $\mathbf { r } _ { 1 } ,$ or $\mathbf { r } _ { 2 }$ is redundant; ii wheneverŽ . $\mathbf { r } _ { 2 }$ occurs in a path from G to $g$ and $\mathbf { A } _ { 3 }$ is contained in G Žin other words, $\mathbf { r } _ { 1 }$ can also be used to traverse between any $G$ to g whenever $\mathbf { r } _ { 2 }$ can do so , then perhaps. $\mathbf { r } _ { 1 }$ , or $\mathbf { r } _ { 2 }$ is redundant.

We flag both the rules because the consequent of rules $\mathbf { r } _ { 1 }$ and $\mathbf { r } _ { 2 }$ should be examined before concluding redundancy. For example, 1 if H is BIRDŽ . $( x )$ and $\mathrm { H ^ { \prime } }$ is BIRD Tweety , and condition i aboveŽ . Ž . holds then $\mathbf { r } _ { 2 }$ is redundant; and 2 if H is BIRDŽ . $( x )$ and $\mathrm { H ^ { \prime } }$ is BIRD Ž . Ž . x <sup>n</sup> SINGS x , and condition Ž .ii above holds then $\mathbf { r } _ { 1 }$ is redundant.

begin

Let $\mathbf { r } _ { 1 }$ and $\mathbf { r } _ { 2 }$ be any two rules in the rule base.

1. Flag $< \mathbf { r } _ { 1 } , \mathbf { r } _ { 2 } >$

$\mathbf { \Omega } / \mathbf { \Omega } ^ { * } \mathbf { \Omega } \mathbf { r } _ { 1 }$ can traverse between any goal—goal whenever $\mathbf { r } _ { 2 }$ can $^ * /$

Ž .i if the goal atoms in the antecedent of $\mathbf { r } _ { 1 }$ are contained in the goals required for every path where $\mathbf { r } _ { 2 }$ appears, and

Ž . ii Every non-goal atom in the antecedent of $\mathbf { r } _ { 1 }$ not present in the antecedent of $\mathbf { r } _ { 2 }$ is supplied by some rule in every path in which $\mathbf { r } _ { 2 }$ appears, and Ž . iii One of the rule consequents subsumes another.

2. Flag $< { \bf r } _ { 1 } , { \bf r } _ { 2 } > , / ^ { * }$ vice versa $^ * /$

Ž .i if goal atoms in the antecedent of $\mathbf { r } _ { 2 }$ are contained in he set of goals required for every path that contains $\mathbf { r } _ { 1 }$ , and

Ž . ii Every non-goal atom in the antecedent of $\mathbf { r } _ { 2 }$ not present in the antecedent of $\mathbf { r } _ { 1 }$ is supplied by some rule in every path in which $\mathbf { r } _ { 1 }$ appears, and Ž . iii One of the rule consequents subsumes another.

end

This aberration is a general form for detecting rule subsumption: whenever a rule can replace another rule in all goal-to-goal progressions the latter participates, then these rule pairs are flagged. This aberration can also detect syntactic subsumption between rules because rule r: a™b can appear in every path where rule $\mathbf { r } { ' } :$ ${ \textrm { a } } \wedge { \textrm { c } } \to$ b can appear. The detection of subsumed rules is important because of performance implications see our case study in SectionŽ 3 , and from the observation that rule subsumption . can interfere with certain ‘greedy’ inference strategies producing unexpected results 30

Aberration 5 Ž . Detecting useless inferences. Motivation: Redundant atoms in a rule consequent serve no useful purpose.

begin

1. Let X:<sup>s</sup>rules flagged redundant in any of the above aberrations 1–4, consider the atoms in the antecedent of the rules in X.

2. If some of these atoms never appear in the antecedent of rules not in X then flag these atoms. 3. If a rule r infers any of the atoms flagged in step 2, then flag r. <sup>r</sup> <sup>)</sup> useless inference <sup>)r</sup> end

Inferring an atom used only in the antecedent of flagged rules is possibly redundant. This aberration enables detection of redundant atoms by inspecting the antecedent of the rules flagged already by any of Ž the above aberrations . If an atom A in the an-. tecedent of one of these rules never appears in the antecedent of rules that are not flagged, then this atom is redundant. Note, this type of flagging would require examination of some rules that have not been flagged, but use these atoms in their consequent.

Aberration 6 ŽDetecting redundant consumed atoms. Motivation: Redundant atoms in rule an-. tecedents can cause rule unreachability.

Atoms in the antecedent of a rule r inferred only by flagged rules are redundant. The rule r can become unreachable if all the flagged rules are deleted from the rule base. This type of flagging would require examination of some rules that have not been flagged, but use these atoms in their antecedent. This is complementary to aberration 5.

begin

1. Let X:<sup>s</sup>rules flagged redundant in any of the above aberrations 1–4, consider the atoms in the consequent of the rules in X.

2. If some of these atoms never appear in the consequent of rules not in X, then flag these atoms.

3. If a rule r uses any of the atoms flagged in step 2, then flag r. <sup>r</sup> <sup>)</sup> potential unreachability <sup>r</sup> end

For example, consider a rule r: a™b flagged by Ž . one or more of the aberrations 1–4. Let r : b™c be a rule that is not flagged by the aberrations. Then aberration 6 flags this rule r because if the knowledge engineer deletes rule r then rule r becomes Ž . potentially unreachable: that is, it could never fire. Thus, caution is advised in deleting flagged rules.

The following aberrations characterize ambivalence in the system 16 . <sup>w</sup> <sup>x</sup>

Aberration 7 Ž .Ambivalence in a Path. Motivation: Goal inference should not violate a domain constraint.

## begin

1. Intra-path The conjunction of non-goal atomsŽ . in a path should not be subsumed by an inviolable. This also applies to the conjunction of all the atoms in a path.

2. Goal ambivalence No goal should be sub-Ž . sumed by an inviolable. This can indicate inaccuracies in knowledge acquisition.

3. The set of goals required by a path should not contain or be subsumed by an inviolable.

end.

Aberration 7 is based on a path and a goal it infers. Clearly, in trying to infer a goal, the non-goal atoms in a path should not violate a constraint. For example, MALE Ž . Ž . x <sup>n</sup> FEMALE x , should not be inferred in a path even though it may infer something useful. Condition 2 prohibits incorrect goal specification. Condition 3 enables no path should start at the cost of violating a constraint.

Aberration 8 Ž . Ambivalence over Inference Chains. Motivation: Solutions should not be inferred from permissible initial evidence at the cost of violating a domain constraint.

## begin

1. The conjunction of non-goal atoms in a relevant route should not be subsumed by an inviolable. This means as part of problem solving at least one constraint is violated.

2. The conjunction of goal atoms in a relevant route should not be subsumed by an inviolable. This means as part of problem solving at least one constraint is violated.

<sup>r</sup> <sup>)</sup> Also check for constraint violation for all atoms inferred in the route <sup>)r</sup>

end.

Aberration 8 considers transitivity of inferences Ž . an inference used for other inferences to check for ambivalence. This can occur under two scenarios. In the first scenario, while goals are not inviolables themselves, some of the goal atoms can be part of inviolables. In problem solving therefore the system can be ambivalent whenever this set of atoms are collectively inferred over a sequence of paths. In general, a system is potentially ambivalent, whenever a set of goals subsume an inviolable. The ambivalence is potential because, this is problematic iff we have path sŽ .<sup>r</sup>routes that involve this set of goals. In the second scenario, we ensure no atoms involved in a relevant route violate a constraint: this ensures that this complete sequence of paths from initial evidence to final goals is free of ambivalence. More specifically, we may check if a set of non-goal or goal atoms or their combination violates a constraint in order to focus the fix in the rule base or goal specification or both. Note, checking that every path is free from ambivalence cf. aberration 7 doesŽ . not ensure that a route is free from ambivalence.

Aberration 9 ŽImpact of Impermissible Initial Evidence. Motivation: A rule base should not infer any . meaningful result from an impermissible combination of initial evidence.

## begin

1. As part of route determination check if an impermissible set of initial evidence is obtained at level-0.

2. Reverse of 1 For every set of impermissibleŽ . initial evidence, check if paths and routes can be enumerated. Flag all these paths. end.

Conditions 1 and 2 check for all routes that can be caused by an impermissible evidence combination: this is serious because, if at least one of these routes is relevant, then an inviolable is treated as a valid input by the system. This reflects on inaccuracy and negative adequacy of the system solving problemsŽ that are not intended to be solved . Note, condition 2. requires a modification to the algorithm for route enumeration described in Ref. 14 . There is only one <sup>w</sup> <sup>x</sup> aberration for circularity.

Aberration 10 Ž . Path Circularity. Motivation: Goal inference should not entail circular reasoning.

begin

1. A sequence of paths $( \boldsymbol { \phi } _ { 1 } , \ldots , \boldsymbol { \phi } _ { n } )$ where goal inferred by a path $\Phi _ { i - 1 } ~ 1 < i \leq n$ is used as part of the start state of path $\textstyle \phi _ { i } ,$ , such that the goal inferred by $\Phi _ { n }$ is contained in the start state of $\boldsymbol { \varPhi } _ { 1 } .$

The start state of a path is the set of goals required by a path before the rules in the path can fire. Since paths are partially ordered, the above detection of circularity can flag more than one circular dependency between the rules in the system. In addition, during path extraction, the tool Path Hunter <sup>w</sup> <sup>x</sup> 11 also flags rules whenever it detects a circular accessibility relationship between the rules in the rule base.

![](/api/attachments/QUNWSQ9M/fulltext/images/50c696ddcc3a876f0abad24745c26a787ba0bdf1336d34d1356226b5810d6447.jpg)  
Fig. 13. An example description of the occupation of the various persons in a university domain.

<table><tr><td>Knowledge Acquired Via Interviews</td></tr><tr><td>“All undergraduates hold unique green bordered ID cards.”</td></tr><tr><td>“Most undergraduates here hold a GPA that is higher than national average.”</td></tr><tr><td>“Though they are hard working, generally no financial aid is available.”</td></tr><tr><td>“A hard working student is likely to take honors courses.”</td></tr><tr><td>“All undergraduates are considered as regular academic students who are enrolled using a registration process.”</td></tr><tr><td>“Good grades in junior college is required for admission into university.”</td></tr><tr><td>“Only regular academic students can enroll during registration.”</td></tr><tr><td>“All registered undergraduates are young.”</td></tr><tr><td>“Undergraduate students do not receive financial aid; however, students with good record and good grades in junior college can expect bursaries on a competitive basis making their life comfortable.”</td></tr><tr><td>“Only undergraduates can register for honors courses and those in the dean’s list (with high GPA, above 3.5) and taking honors courses can pass with distinction; such high GPA requires hard work from the undergraduates.”</td></tr><tr><td>“University graduates with distinction have a good career in industry and a comfortable life.”</td></tr></table>

Fig. 14. Typical knowledge elicited from a domain expert about a university environment. Interviews are the most common ways of eliciting knowledge from the domain. These are later translated into a set of goals associated with the domain by the knowledge engineer in collaboration with the domain expert forming the goal specification for the domain.

Currently, we are in the process of writing a verification tool based on the algorithms developed for detecting rule aberrations. In general, these algorithms require that the paths be pre-processed into a set of indices before aberrations can be spotted. The typical indices are the rule index list of paths, and Ž routes in which a rule appears , and fact index list . Ž of paths and routes in which the fact appears . As an. example, an algorithm to detect aberration 6 appears below. It, however, requires only the current set of flagged rules and atoms. We have assumed the existence of a function Antecedent r to return a list of Ž . atoms in the antecedent of rule r. Most of the algorithms to detect aberrations are simple except a few such as the one to detect aberration 4.

Procedure aberration 6; <sup>r</sup>) detect aberration 6 )r

Input: Paths, FlaggedR, FlaggedA.

begin

<table><tr><td>The Goal Specification.</td></tr><tr><td>REGISTERED(x) ∧ GREENBORDRID(x)</td></tr><tr><td>GREENBORDRID(x) ∧ HARDWORKING(x)</td></tr><tr><td>REGISTERED(x) ∧ DEANSLIST(x)</td></tr><tr><td>ACADEMIC(x)</td></tr><tr><td>GOODCAREER(x)</td></tr><tr><td>BURSARY(x)</td></tr><tr><td>COMFLIFE(x)*</td></tr><tr><td>ACADEMIC(x) ∧ YOUNG(x)*</td></tr><tr><td>GOODGRADES(x,y) ∧ GT(x,Gpa, 3.5)*</td></tr></table>

Fig. 15. The goal specification of the university domain from its description in Fig. 14. An asterisk on a goal indicates that it is a final goal.

Atoms denoting initial evidence

$$
g _ {0 1} = \text { REGISTERED } (\mathrm{x})
$$

are as follows:

$$
g _ {0 2} = \text { GREENBORDRID } (\mathrm{x})
$$

$$
g _ {0 3} = \text { HARDWORKING(x)   and }
$$

$$
g _ {0 4} = \mathrm{DEANSLIST(x)}
$$

Let FlaggedR:<sup>s</sup> current set of flagged rules; Let FlaggedA:<sup>s</sup> current set of flagged atoms; For all x such that x <sup>g</sup> FlaggedA do If 'r f FlaggedR <sup>n</sup> x <sup>g</sup> Antecedent r thenŽ . Flag rule $\mathrm { ~ r ~ } / \mathrm { ~ } ^ { * }$ r can become potentially unreachable <sup>)r</sup> end.

## 5. Summary and conclusion

The design and development of rule-based systems often cause anomalies in the rule base. We presented a frame work that can facilitate a variety of software engineering processes in a rule-based system life-cycle to deal with such anomalies. The frame work is based on abstracting the acquired knowledge in terms of goals goal specification , and Ž . representing knowledge in terms of rule sequences inferring goals paths with the design stage provid- Ž . ing a goal-to-hypothesis mapping design scheme Ž . appropriate for the domain. We also described how goals and paths can be a useful tool both for detecting the CARD anomalies in a rule base, and for knowledge restructuring to optimize rule bases usingŽ a case study ..

The design restrictions imposed between goals and the hypotheses realizing them in the rule base results in several design schemes. The inheritance relationship between the different design schemes allows varying amounts of freedom with which knowledge can be encoded. It also provides compromises between development and maintenance, and under certain conditions, inheritance can be used to perform an automated transformation of a rule base in one scheme into another 28 . Thus, one can <sup>w</sup> <sup>x</sup> choose a scheme ‘better’ suited for development, but transform it into another before field delivery. The analysis of this inheritance relationship and related issues are not discussed as they are beyond the scope of this paper.

Finally, an implemented rule base must be subjected to various evaluation procedures to compare its actual behavior with the expected behavior. We provided our perspectives on rule base verification based upon paths and goals. More specifically, we described detecting the CARD anomalies in a rule base by specifying rule situations called rule aberra-

$$
\begin{array}{r c l} G R A D (x) & \wedge & U G R A D (x) \\ N O F I N A I D (x) & \wedge & B U R S A R Y (x) \end{array}
$$

Fig. 16. The inviolables of the university domain. It is assumed that a registered student cannot be both undergraduate and graduate. In addition, if a person receives a bursary, he<sup>r</sup>she cannot be categorized as not receiving any financial aid.

tions. The computation required for path extraction Ž . hence, for evaluation can be controlled by an appropriate choice of a design scheme and prudent goal refinements if needed . We are currently in theŽ . process of writing a verification tool that implements the aberration specifications described in this paper. We have also developed tools to extract paths from a given rule base as well as to measure path coverage <sup>w</sup> <sup>x</sup> 11,12 , and intend to augment this tool suite with the above path-based verifier. This tool suite is expected to provide reliable support to system developers.

## Appendix A. Illustrating design scheme selection

Consider constructing a rule base to identify a person’s occupation in a university environment. The domain description appears in Fig. 13 and a typical analysis for a knowledge engineer to prune, or choose design schemes is described below.

```txt
R1 : REGISTERED(x) ∧ GREENBORDRID(x) →
ENROLLED(x) ∧ NOFINAID(x)
R2 : ENROLLED(x) → ACADEMIC(x) ∧ STUDENT(x)
R3 : GREENBORDRID(x) ∧ NOFINAID(x) → UGRAD(x)
R4 : STUDENT(x) ∧ UGRAD(x) → ACADEMIC(x)
R5 : GREENBORDRID(x) → NOTGRAD(x)
R6 : REGISTERED(x) ∧ NOTGRAD(x) →
STUDENT(x) ∧ ACADEMIC(x) ∧ YOUNG(x) ∧ UGRAD(x)
R7 : DEANSLIST(x) →
HIGHGPA(x) ∧ HONSCOURSES(x)
R8 : REGISTERED(x) ∧ HONSCOURSES(x) → UGRAD(x)
R9 : UGRAD(x) ∧ DEANSLIST(x) →
GOODGRADES(x, Juniorcollege) ∧ COMPLETED(x, JuniorCollege)
R10 : HIGHGPA(x) ∧ REGISTERED(x) → GT(x, Gpa, 3.5)
R11 : HARDWORKING(x) → HONSCOURSES(x)
R12 : GREENBORDRID(x) → HIGHGPA(x)
R13 : HIGHGPA(x) ∧ HONSCOURSES(x) →
UGRAD(x) ∧ DISTINCTION(x)
R14 : UGRAD(x) ∧ DISTINCTION(x) → GOODCAREER(x)
R15 : GOODRECORD(x, Juniorcollege) ∧ COMPLETED(x, Juniorcollege)
→ GOODCAREER(x) ∧ BURSARY(x)
R16 : GOODCAREER(x) → COMFLIFE(x)
R17 : BURSARY(x) → COMFLIFE(x)
```  
Fig. 17. The rule base encoding the knowledge describing the university domain.

The design schemes based on choice I1 or I5 for intermediate goals are ruled out according to the recommendation in Section 2.1. In addition, for the above description choice I2 for intermediate goals that forces every intermediate goals to have at least one final hypothesis is not convenient for encoding.

The $< \mathrm { F } 1 , ~ \mathrm { B } >$ , and <sup>-</sup>F1, I4<sup>)</sup> schemes can accommodate the goal specification in Fig. 13, but can have difficulty inaccommodating goals specified later as the rule base develops incrementally. For example, adding new goals REGULAR\_STUDENT, IR-

![](/api/attachments/QUNWSQ9M/fulltext/images/14d343af16c584e93fe322d75b2ee305631011e373890cd94c283973800374f8.jpg)

![](/api/attachments/QUNWSQ9M/fulltext/images/22f3a9c07ec4287f673d082bac280ca0cf72e60072e23c0c900a6ce2b48aa1fe.jpg)

![](/api/attachments/QUNWSQ9M/fulltext/images/e61f77679ad7b0fa1f3a54bfc235e34d6dd4a0564eaa4e24839bbc4ae0df8b5c.jpg)

![](/api/attachments/QUNWSQ9M/fulltext/images/a5a56b6e132dc6dc9d6007e1c69ce58e77b2b39dc59e69d1a26e3c280a16f260.jpg)

![](/api/attachments/QUNWSQ9M/fulltext/images/ee0dcb4233f0f496ecc03cf3d5b1ed835280ad818869e313cd44229e169d0415.jpg)  
Fig. 18. Paths extracted from the rule base of Fig. 17. To avoid cluttering, not all of the inferred atoms in a path are shown.

![](/api/attachments/QUNWSQ9M/fulltext/images/bae9c0fe4d6c28e48caae9224e0ec355f4aa670ed7bbaac7b6f3724a16aa7558.jpg)  
Fig. 19. The goal graph for the rule base shown in Fig. 17.

REGULAR\_STUDENT, but emphasizing their relation to GRAD, UGRAD, while still retaining them as solutions, can be cumbersome owing to the restriction F1 that requires all final goals should contain only final hypothesis. Note, changing a final goal to an intermediate goal can require significant rule base modification in these schemes. The <sup>-</sup>F2, I3<sup>)</sup> scheme can accommodate the goal specification with ease. But, of course, care should be taken while maintaining causal<sup>r</sup>temporal relations between final goals. For instance, consider the domain constraint involving DEAN and ASSOCDEAN: we simply cannot realize final goal ASSOCDEAN as an intermediate hypothesis and use it to infer DEAN owing to restriction F2. A similar argument applies to the <sup>-</sup>F2, I4<sup>)</sup> scheme. However, a reversal of goal types is better accommodated in the <sup>-</sup>F2, I3<sup>)</sup> scheme owing to its flexibility.

Realizing the solutions as they are specified while maintaining their relationships is easier in schemes with choice F3 for final goals that require every solution to have at least one intermediate hypothesis. However, some of the final goals in this scheme can be counter intuitive, if they are realized as only intermediate hypotheses hence, less understandable .Ž .

A similar observation applies to schemes with choice F5 for final goals that impose no constraints in final goal realization. In addition, care should be exercised if such a scheme is chosen because the rule base can become obscure and error prone due to incremental modifications.

A knowledge engineer may thus prefer to choose either the <sup>-</sup>F2, I3<sup>)</sup> scheme, or the <sup>-</sup>F2, I4<sup>)</sup> scheme for this domain.

## Appendix B. An example to illustrate rule aberrations

We present a small system to describe a university environment to illustrate the manifestation of the various aberrations. The body of knowledge acquired by interviews for this domain is shown in Fig. 14; the goal specification of the domain is shown in Fig. 15; and the inviolables in Fig. 16. Note, permissible combinations of initial evidence which representŽ conjunction of atoms representing initial evidence that a domain expert would use to start problem solving should also be specified. In order to show.

<table><tr><td>Flagged Rules/Atoms</td><td>Route(s)</td><td>Aberration(s)</td></tr><tr><td>R1, R2, R3</td><td> $\Phi 1$ </td><td rowspan="3">Aberration 1</td></tr><tr><td>R17</td><td> $\Phi 6$ </td></tr><tr><td>R15</td><td>none</td></tr><tr><td>Paths  $\Phi 1$  and  $\Phi 2$ </td><td>NA</td><td>Aberration 2</td></tr><tr><td>COMPLETED(x, Juniorcollege)</td><td>NA</td><td>Aberration 3</td></tr><tr><td>R4, ACADEMIC(x)</td><td></td><td></td></tr><tr><td>R8, R13</td><td>NA</td><td>Aberration 4</td></tr><tr><td>UGRAD(x), HONSCOURSES(x),...</td><td>NA</td><td>Aberrations 5 and 6</td></tr></table>

Fig. 20. Summarizing the results of redundancy<sup>r</sup>deficiency aberrations for the example rule base of Fig. 17.

![](/api/attachments/QUNWSQ9M/fulltext/images/72e4c082a01e09bec155cbdd374b0dabb151f8885bc9fc9567dc0270da3ed33f.jpg)  
Fig. 21. The path where rule R15 appears. The path is ambivalent as it infers the inviolable BURSARY <sup>n</sup> NOFINAID.

the effect of each initial evidence on problem solving, we show each atom that is an initial evidence as a level-0 goal. Thus, permissible combinations of initial evidence would be represented as AND edges from level-0 goals in the goal graph.

Suppose design scheme <sup>-</sup>F1, I3<sup>)</sup> is chosen for this domain, a rule base to encode the goal progression knowledge is shown in Fig. 17.

The paths of the rule base are shown in Fig. 18 and the goal graph in Fig. 19. For this rule base and the given goal specification, the intermediate goals $g _ { 1 2 }$ and $g _ { 1 4 }$ are irrelevant.

A summary of the application of aberration specifications 1–6 is shown in Fig. 20. For example, rule R15 was flagged by aberration 1 because it does not appear in any path. The actual cause, however, is due to deficiency as will be apparent later. Similarly, atom COMPLETEDŽ . x, Juniorcollege in the consequent of rule R9 was flagged using aberration 3. Note, however, that this atom is used in the antecedent of rule R15 that was flagged also redundant : thus, Ž . detection methods based on simple unification may not detect this atom as redundant 32 .<sup>w</sup> <sup>x</sup>

Inspection of the rules and atoms flagged by the above aberrations should also reveal a design scheme violation. Of course, whenever rules or atoms are flagged by aberration procedures, refining the goal specification and editing the rule base may remove the anomalies. For example, the subsumption problem between R8 and R13 can be corrected by modifying the permissible combination of initial evidence HARDWORKING Ž . Ž . x <sup>n</sup> GREENBORDRID x to HARD-WORKING Ž . Ž .x <sup>n</sup> GREENBORDRID x <sup>n</sup> GOODRECORD Ž . x, y , and the antecedent of rule R13 to contain the atom GOODRECORD Ž . x, Courses . However, modifications to fix a detected anomaly can also introduce additional anomalies. For illustration, consider the following modification to the rule base in Fig. 17 to ensure that rule R15 appears in a path.

As rule R15 was flagged redundant by aberration R-1, a knowledge engineer trying to fix this redundancy can include GOODRECORD Ž . x, Juniorcollege as initial evidence. However, this still would not make R15 appear in a path. It is required to remove GOODCAREER Ž . x in the consequent of rule R15. In addition, the conjunction REGISTERED Ž . x <sup>n</sup> GOODRECORD Ž . x, y must also be added as a permissible combination of initial evidence. To accommodate the status of a registered person with good grades in junior college, assume that the following new rule is added:

```txt
R1 : REGISTERED(x) ∧ GREENBORDRID(x) →
ENROLLED(x) ∧ NOFINAID(x)
R2 : ENROLLED(x) → STUDENT(x)
R3 : GREENBORDRID(x) ∧ NOFINAID(x) → UGRAD(x)
R4 : STUDENT(x) ∧ UGRAD(x) → ACADEMIC(x) ∧ YOUNG(x)
R5 : DELETED
R6 : DELETED
R7 : DEANSLIST(x) → HIGHGPA(x) ∧ HONSCOURSES(x)
R8 : REGISTERED(x) ∧ HONSCOURSES(x) → UGRAD(x)
R9 : UGRAD(x) ∧ DEANSLIST(x) →
GOODGRADES(x, Juniorcollege)
R10 : HIGHGPA(x) ∧ REGISTERED(x) → GT(x, Gpa, 3.5)
R11 : HARDWORKING(x) ∧ GREENBORDRID(x) →
HIGHGPA(x) ∧ HONSCOURSES(x)
R12 : Merged with rule R11 above
R13 : HIGHGPA(x) ∧ HONSCOURSES(x)
∧GOODRECORD(x, Courses) → DISTINCTION(x)
R14 : DISTINCTION(x) → GOODCAREER(x, Industry)
R15 : GOODRECORD(x, Juniorcollege) ∧
COMPLETED(x, Juniorcollege) → BURSARY(x)
R16 : GOODCAREER(x, Industry) → COMFLIFE(x)
R17 : BURSARY(x) → COMFLIFE(x)
R18 : GOODRECORD(x, Juniorcollege) ∧ REGISTERED(x) →
COMPLETED(x, Juniorcollege)
```  
Fig. 22. The modified rule base based upon the evaluation results of the rule base shown in Fig. 17.

$$
\text { R18:REGISTERED(x) } \land \text { GOODRECORD(x,Juniorcollege)}
$$

$$
\rightarrow \text {   COMPLETED } (x, \text { Juniorcollege }) \land \text {   NOFINAID } (x)
$$

to encode the knowledge describing a person just registered after completing junior college, who does not receive any financial aid. This adds a new path which is shown in Fig. 21.

However, the modification to remove the redundancy of rule R15 has now resulted in another anomaly in the rule base. The path in Fig. 21 infers an inviolable: BURSARY <sup>n</sup> NOFINAID; thus, the system is now ambivalent. An inspection of the rule base shows that, in this case, atom NOFINAID Ž . x is not required in the consequent of rule R18, because rule R1 makes that inference for a general registered undergraduate student. The impact of a rule modification can immediately be assessed by thus checking the paths affected for aberrations, if any.

![](/api/attachments/QUNWSQ9M/fulltext/images/bac158fe80f6b8e75e92caf8651a39c4de30e162b332b06fcb95b674ceb00078.jpg)

![](/api/attachments/QUNWSQ9M/fulltext/images/de6e54a541323faffd630ff667b771cf8bd8e1fda59b5f5be659efe8a2cf9fb9.jpg)

![](/api/attachments/QUNWSQ9M/fulltext/images/7f87fdd5da7e32e12237c7b13e3f7ea787b9b412508896ad9148252ee6473a49.jpg)

![](/api/attachments/QUNWSQ9M/fulltext/images/52385cd173d31ec81002751a5cc2c2201b3cedc516e204ef7ac45aa9d003fe6a.jpg)

![](/api/attachments/QUNWSQ9M/fulltext/images/032836ee96768b2fbda39d489fe7458cfd9c14e52012f7ba6c3a789a5ea814b0.jpg)  
Fig. 23. Paths of the rule base shown in Fig. 22 which is the rule base modified to fix the errors, anomalies and scheme violations detected after evaluation of the rule base shown in Fig. 17.

![](/api/attachments/QUNWSQ9M/fulltext/images/08f4e83fa6b5852cf700729d928995806e04f8c5f19fb246ab8b95c755de6c57.jpg)  
Fig. 24. The goal graph for the rule base shown in Fig. 22.

The final version of the rule base after making the required modifications to fix the detected anomalies is shown in Fig. 22.

Once all the detected anomalies are fixed, and the system behavior is judged to be acceptable by a knowledge engineer, the system is tested for the satisfaction of the user acceptability criteria 33,34 . Often, the user acceptability criteria can impose further constraints on the user interface required, on the response times, on the system adequacy, etc. Let us assume that our user acceptability criteria involves that the system should be optimal and adequate in its domain 14 : that is, it should utilize all the interme-<sup>w</sup> <sup>x</sup> diate goals specified for problem solving and produce a solution for every permissible combination of initial evidence.

The final set of paths and the goal graph for the system are shown in Figs. 23 and 24. There are no more unwanted rules or atoms. All the rules in the rule base come into play for problem solving and the system is optimal and adequate for the given goal specification. As there are no irrelevant final goals, the system satisfies the user acceptability criteria.

## References

<sup>w</sup> <sup>x</sup> 1 G.R. Yost, Acquiring knowledge in SOAR, IEEE Expert 8 Ž . Ž .3 1993 26–34.

<sup>w</sup> <sup>x</sup> 2 A.D. Preece, R. Shinghal, A. Batarekh, Principles and prac-

tice in verifying rule-based systems, Knowledge Eng. Rev. 7 Ž . Ž . 2 1992 115–141.

<sup>w</sup> <sup>x</sup> 3 R.M. O’Keefe, D.E. O’Leary, Expert system verification and validation: a survey and tutorial, Artificial Intelligence Rev. 7 1 1993 3–42. Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 T.A. Nguyen, W.A. Perkins, T.J. Laffey, D. Pecora, Checking an expert systems knowledge base for consistency, completeness, in: Proceedings of the 9th International Joint Conference on Artificial Intelligence IJCAI 85 , Vol. 1, Boston,Ž . MA, 1985, pp. 278–375.

<sup>w</sup> <sup>x</sup> 5 B.J. Cragun, H.J. Steudel, A decision-table-based processor for checking completeness and consistency in rule-based expert systems, Int. J. Man–Machine Stud. 26 5 1987Ž . Ž . 633–648.

<sup>w</sup> <sup>x</sup> 6 Allen Ginsberg, Knowledge-base reduction: a new approach to checking knowledge bases for inconsistency and redundancy, in: Proceedings of the 7th National Conference on Artificial Intelligence AAAI 88 , Vol. 2, St. Paul, MN,Ž . August 1988, pp. 585–589.

<sup>w</sup> <sup>x</sup> 7 Robert T. Plant, The meta knowledge level: a methodology for validation, in: Proceedings of the AAAI Workshop on Validation and Verification of Knowledge-Based Systems, Washington, DC, July 1993, pp. 94–108.

<sup>w</sup> <sup>x</sup> 8 C.L. Chang, J.B. Combs, R.A. Stachowitz, A report on the expert systems validation associate EVA , Expert Syst. Appl. Ž . 1 3 1990 217–230.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 A.D. Preece, R. Shinghal, A. Batarekh, Verifying expert systems: a logical framework and a practical tool, Expert Syst. Appl. 3 2Ž . Ž .<sup>r</sup>3 1992 421–436.

<sup>w</sup> <sup>x</sup> 10 Marie-Christine Rousset, On the consistency of knowledge bases: the COVADIS system, Computational Intelligence, 4 Ž . 2 : 166–170, May 1988; Also in ECAI 88, Proc. European Conference on AI, Munich, August 1–5, 1988, pp. 79–84.

<sup>w</sup> <sup>x</sup> 11 C. Grossner, A. Preece, P. Gokulchander, T. Radhakrishnan, C.Y. Suen, Exploring the structure of rule based systems, in: Proceedings of the 11th National Conference on Artificial Intelligence AAAI 93 , Washington, DC, 1993, pp. 704–709. Ž .

<sup>w</sup> <sup>x</sup> 12 A. Preece, C. Grossner, P. Gokulchander, T. Radhakrishnan, Structural validation of expert systems: experience using a formal model, in: Notes of the Workshop on Validation and Verification of Knowledge-Based Systems, 11th Nationa Conference on Artificial Intelligence, Washington, DC, July 1993, pp. 19–26.

<sup>w</sup> <sup>x</sup> 13 A. Preece, P. Gokulchander, C. Grossner, T. Radhakrishnan, Modeling rule base structure for expert system quality assurance, in: Notes of the Workshop on Validation of Knowledge-Based Systems, 13th International Joint Conference on Artificial Intelligence, Savoic, France, August 1993, pp. 37– 50.

<sup>w</sup> <sup>x</sup> 14 P. Gokul Chander, R. Shinghal, T. Radhakrishnan, Static determination of dynamic functional attributes in rule-based systems, in: Proceedings of the 1994 International Conference on Systems Research, Informatics and Cybernetics, AI Symposium ICSRIC 94 , Baden Baden, Germany, August Ž . 1994, pp. 79–84.

<sup>w</sup> <sup>x</sup> 15 P. Gokul Chander, T. Radhakrishnan, R. Shinghal, Using paths to detect redundancy in rule bases, in: Proceedings of the 11th IEEE Conference on Artificial Intelligence Applications, IEEE CAIA ’95, Los Angeles, CA, February 1995, pp. 133–139.

<sup>w</sup> <sup>x</sup> 16 P.G. Chander, R. Shinghal, T. Radhakrishnan, Goal supported knowledge base restructuring for verification of rule bases, in: Notes of the Workshop on Verification and Validation of Knowledge-Based Systems, 14th InternationalJoint Conference on Artificial Intelligence, Montreal, Canada, August 1995, pp. 15–21.

<sup>w</sup> <sup>x</sup> 17 Rajjan Shinghal, Formal Concepts in Artificial Intelligence, Chapman & Hall, London, UK, co-published in U.S. with Van Nostrand–Reinhold, New York, 1992.

<sup>w</sup> <sup>x</sup> 18 A. Preece, C. Grossner, P. Gokulchander, T. Radhakrishnan, Structural validation of expert systems: experience using a formal model, in: Jay Liebowitz Ed. , Second WorldŽ . Congress on Expert Systems, Estoril, Portugal, January 1994, pp. 323–330.

<sup>w</sup> <sup>x</sup> 19 Gregg R. Yost, Allen Newell, A problem space approach to expert system specification, in: Proceedings of the International Joint Conference on Artificial Intelligence, IJCAI ‘89, San Mateo, CA, 1989, pp. 621–627.

<sup>w</sup> <sup>x</sup> 20 P. Lucas, Refinement of the HEPAR expert system: tools and techniques, Artificial Intelligence Med. 6 2 1994 175–188.Ž . Ž .

<sup>w</sup> <sup>x</sup> 21 J. Giarratano, G. Riley, Expert Systems: Principles and Programming, 2nd edn., PWS Publ., Boston, MA, 1993.

<sup>w</sup> <sup>x</sup> 22 A. Batarekh, A.D. Preece, A. Bennett, P. Grogono, Specifying an expert system, Expert Syst. Appl. 2 4 1991 285–Ž . Ž . 303.

<sup>w</sup> <sup>x</sup> 23 N. Zlatareva, A.D. Preece, State of the art in automated validation of knowledge-based systems, Expert Syst. Appl. 7 Ž . Ž . 2 1994 151–167.

<sup>w</sup> <sup>x</sup> 24 J. Debenham, Expert systems designed for maintenance, Expert Syst. Appl. 5 3 1992 233–244.Ž . Ž .

<sup>w</sup> <sup>x</sup> 25 Steven A. Wells, The VIVA method: a life-cycle independent approach to KBS validation, in: Proceedings of the AAAI Workshop on Validation and Verification of Knowledge-Based Systems, Washington, DC, July 1993, pp. 109– 113.

<sup>w</sup> <sup>x</sup> 26 J.A. Long, I.M. Neale, Using paper models in validation, verification and testing, Int. J. Expert Syst. 6 3 1993 Ž . Ž . 357–382.

<sup>w</sup> <sup>x</sup> 27 P.G. Chander, T. Radhakrishnan, R. Shinghal, Design schemes for rule-based systems, International Journal of Expert Systems: Research and Applications, November 1996, In press.

<sup>w</sup> <sup>x</sup> 28 Prabhakar Gokul Chander, On the design and evaluation of rule-based systems, PhD thesis, Department of Computer Science, Concordia University, Montreal, May 1996.

<sup>w</sup> <sup>x</sup> 29 J.D. Kiper, Structural testing of rule-based expert systems, ACM Trans. Software Eng. Meth. 1 2 1992 168–187.Ž . Ž .

<sup>w</sup> <sup>x</sup> 30 Daniel E. O’Leary, Inference engine greediness and subsumption of conditions in rule-based systems, in: Notes of the Workshop on Verification and Validation of Knowledge-Based Systems, Fourteenth International Joint Conference on Artificial Intelligence, Montreal, Canada, August 1995, pp. 42–48.

<sup>w</sup> <sup>x</sup> 31 T.A. Nguyen, Verifying consistency of production systems, in: Proceedings of the 3rd Conference on Artificial Intelligence Applications, Washington, DC, Spring 1987, pp. 4–8.

<sup>w</sup> <sup>x</sup> 32 F. Polat, H.A. Guvenir, UVT: a unification-based tool for knowledge base verification, IEEE Expert 8 3 1993 69–75.Ž . Ž .

<sup>w</sup> <sup>x</sup> 33 A.D. Preece, Towards a methodology for evaluating expert systems, Expert Syst. 7 4 1990 215–223.Ž . Ž .

<sup>w</sup> <sup>x</sup> 34 Carlo Ghezzi, Mehdi Jazayeri, Dino Mandrioli, Fundamentals of Software Engineering, Prentice-Hall, New York, 1991.

![](/api/attachments/QUNWSQ9M/fulltext/images/b7289813169db5b73e22f48a6cedbbb17801c86bfe803c0e2dfcea34f791a987.jpg)

Dr. P.G. Chander is a post doctoral fellow in the department of Computer Science at Concordia University. He completed his Bachelor’s degree in Electrical and Electronics Engineering at Regional Engineering College Tiruchirappalli, his Master’s degree in Computer Engineering at Boston University, and his Doctoral degree in Computer Science at Concordia University. His research interests include Artificial Intelligence, Distributed Systems, Multi-media

Databases, and Design of Distributed Multi-media Applications.

![](/api/attachments/QUNWSQ9M/fulltext/images/97b4dde60f59e8ffc250bc1bae13c1349a3d516b3cc14e7a18fca5952ecbdc53.jpg)

Dr. R. Shinghal is a professor of computer science in Concordia University, Montreal. He is the author of Forma Concepts in Artificial Intelligence, 666 pp., published in the UK by Chapman and Hall, co-published in the U.S. with Van Nostrand.

![](/api/attachments/QUNWSQ9M/fulltext/images/d6a5b5bb254f7a0dfd06d5dd96609f36d014fe4ebe4885a96a0e14fa3a543256.jpg)  
Dr. T. Radhakrishnan obtained his M.Tech and PhD from Indian Institute of Technology, Kanpur, India. He has been working at Concordia University since 1975. His areas of research and teaching interests are in Cooperating Intelligent Agents, User Interfaces, and the Design of Reliable Knowledge Base Systems. He is also interested in Social Aspects of Computing and Information Technology particularly for the benefit of people in Developing countries.

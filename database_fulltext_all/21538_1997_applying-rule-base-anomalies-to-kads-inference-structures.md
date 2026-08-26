---
otero_id: 21538
otero_key: "UYR6SCW9"
title: "Applying rule-base anomalies to KADS inference structures"
authors: "Frank van Harmelen"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00045-6"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Applying rule-base anomalies to KADS inference structures

Frank van Harmelen

AI Group, Department of Mathematics and CS, Vrije UniÕersiteit Amsterdam, Amsterdam, The Netherlands

## Abstract

The literature on validation and verification of knowledge-based systems contains a catalogue of anomalies for knowledge-based systems, such as redundant, contradictory or deficient knowledge. Detecting such anomalies is a method for verifying knowledge-based systems. Unfortunately, the traditional formulation of the anomalies in the literature is very specific to a rule-based knowledge representation, which greatly restricts their applicability. In this paper, we show how the traditional anomalies can be reinterpreted in terms of conceptual models in particular KADS inference structures . For thisŽ . purpose, we present a formalisation of KADS inference structures which enables us to apply the traditional rule-base anomalies to these inference structures. This greatly improves the usefulness of the anomalies, since they can now be applied to a much wider class of knowledge-based systems. Besides this reformulation and wider applicability of the traditional anomalies, further contributions of this paper are a novel formalisation of KADS inference structures and a number of improvements to the existing formalisation of the traditional anomalies. q 1997 Elsevier Science B.V.

Keywords: Validation; Verification; Knowledge-based systems; Anomalies; Inference structures

## 1. Introduction

Traditional anomalies for knowledge-based systems KBSs concern properties such as redundant, Ž . contradictory or deficient knowledge. Detecting anomalies is a method for verifying KBSs. Ideally anomaly detection must be done using the conceptual model of a KBS, and not its implementation. This is required to keep anomaly detection free from details about the particular procedural properties of the inference engine for the knowledge-base. However, traditionally, anomalies are formulated in terms of a rule-based knowledge-representation formalism. This has made the formulation of the anomalies specific to a particular representation language.

In this paper, we show how the traditional rulebased anomalies can be reinterpreted in terms of conceptual models.

In the literature on validation and verification of KBSs, many researchers have devised, categorised and extended definitions for structural anomalies of rule-based systems. We have taken a specific formulation of anomalies for rule-bases from Ref. 1<sup>w</sup> <sup>x</sup> Ž . henceforth, Pr & Sh for short as the basis for our work, but that paper in turn builds upon previous work by a variety of researchers, including Refs. <sup>w</sup> <sup>x</sup> 2–5 . These papers define a wide class of anomalies, but we focus on those in Ref. 1 , which are an <sup>w</sup> <sup>x</sup> important and representative set of anomalies.

We will show how to reinterpret these anomalies in terms of the conceptual models as proposed by the KADS method of KBS construction. KADS 6 is a<sup>w</sup> <sup>x</sup> well-known method of constructing conceptual models for KBSs, which has found widespread acceptance both in industry and in academia.

The traditional anomalies are most relevant for a specific part of KADS conceptual models, called inference structures. These inference structures are declarative and implementation-independent descriptions of the problem-solving competence of a KBS. In order to apply Pr & Sh’s formalisation of the traditional anomalies to these inference structures, we require a formalisation of these inference structures. However, existing formalisations see Ref. 7 for anŽ <sup>w</sup> <sup>x</sup> overview are too far removed from Pr&Sh’s defini-. tions. We will use a recent formalisation from Ref. <sup>w</sup> <sup>x</sup> 8 , which allows a direct interpretation of the traditional anomalies in terms of KADS inference structures. This greatly improves the usefulness of the anomalies, since they can now be applied to a wide class of knowledge-based systems, instead of only to rule-based systems.

Furthermore, anomalies were traditionally defined for a rule-based formalism Žsuch as first-order logic in Ref. 1 , rather than for a particular rule-based<sup>w</sup> <sup>x</sup>. representation language e.g., OPS5 or Prolog . ThisŽ . was done in order to re-use verification methods. Typically, the approach taken has been to translate implemented systems written in concrete languages to the formalism on which the anomalies were defined. In abstracting the implemented systems, information is lost, which is one of the reasons why anomalies are not necessarily faults. This approach may seem ‘backwards’, but it arose because until recently, the only concrete description of the KBS was the implementation itself.

In the above light, the contributions of this paper are: i that the formalism upon which the anomalies Ž . are defined is at a higher level of abstraction, namely that of the conceptual model which exists before design choices are made for example the choice toŽ use rules ; ii that verification no longer depends on. Ž . the ‘backwards’ creation of a verifiable abstraction of the implemented system, but instead proceeds in the ‘forwards’ direction: the conceptual model is created, verified ‘accurately’, and only then, implemented.

The structure of this paper is as follows. In Section 2, we summarise the anomalies as formalised by Pr&Sh, and introduce a number of improvements to Pr&Sh’s definitions. Section 3 describes KADS inference structures and introduces Aben’s formalisation of them. Section 4 uses this formalisation to interpret the anomalies for inference structures, and Section 5 concludes. Appendix A discusses and motivates in more detail the alterations we have made to the original definitions of Pr & Sh.

Notation: In what follows, we will use lower-case letters from the middle of the alphabet for literals, lower-case letters from the end of the alphabet for first order variables, lower-case Greek letters for variable substitutions, and calligraphic letters for sets of formula, literals or terms.

## 2. Summary of the work by Preece and Shinghal

In this section, we discuss the main definitions of Ref. 1 . We will not simply summarise these defini- <sup>w</sup> <sup>x</sup> tions, but also introduce improvements. Comments on our changes to Pr&Sh’s original definitions have been relegated to notes at the end of this paper. Although our versions of Pr&Sh’s definitions often differ significantly from the original ones, they are all in the spirit of Ref. 1 .<sup>w</sup> <sup>x</sup>

We first introduce the terminology and notation used in Ref. 1 : 1 a rule <sup>w</sup> <sup>x</sup> Ž . $R _ { i }$ is formula of the form $l _ { 1 } \wedge . . . \wedge l _ { n }  m$ where each $l _ { i }$ and m are first order literals; 2 for each ruleŽ . $R _ { i } = l _ { 1 } \wedge . . . \wedge l _ { n } \to$ m, we write antec $\mathbf { \xi } _ { R } ) = \{ l _ { 1 } , \ldots , l _ { n } \}$ and conseq RŽ . $= m$ . We will sometimes abuse notation and interpret the set antec RŽ . Ž . as a conjunction; 3 a rule set $\mathcal { R }$ is a set of rules; 4 the goal-literalsŽ . $\mathcal { G }$ is the set of all ground literals that could possibly be output from the rule set; 5 the input-literalsŽ . $\mathcal { I }$ is the set of all ground literals that constitute all possible inputs to the rule set. Since we are dealing with first-order formula, the sets $\mathcal { G }$ and $\mathcal { I }$ can in general be infinite; 6 a semantic constraint is a set ofŽ . literals $\{ l _ { 1 } , \ldots , l _ { n } \}$ such that their conjunction $l _ { 1 }$ $\wedge \ . \ . \wedge l _ { n }$ is regarded as a semantic inconsistency Že.g., the set male xŽ . Ž . , pregnant x 4.. Semantic constraints form a way of introducing an extended notion of semantic inconsistency among rules even when they are logically consistent. We write $\mathcal { C }$ for the set of all semantic constraints for a rule set; and Ž . 7 an environment is a subset of $\mathcal { I }$ that does not imply any semantic constraint. We write $\varepsilon$ for the Ž . possibly infinite set of all such environments. Formally, for all $e \in { \varepsilon }$ and all $c \in { \mathcal { C } }$

There are nine anomalies that Ref. 1 defines.<sup>w</sup> <sup>x</sup>

<sup>w</sup> <sup>x</sup> A1 Unsatisfiable rule: a rule R is unsatisfiable iff there is no way of deducing R’s antecedent from any legal input:

$$
\neg \left(\exists e \in \mathscr {E}, \exists \sigma : R \cup e \vdash \sigma \circ a n t e c (R)\right)
$$

Žwe write $\sigma \circ \phi$ for the application of substitution to formula and $\sigma _ { 1 } \sigma _ { 2 } \circ \phi$ for the simultaneous application of multiple substitutions ..

<sup>w</sup> <sup>x</sup> A2 Unusable rule: a rule R is unusable iff the consequent of R subsumes neither a goal literal nor any antecedent literal in the rule set:

$$
\begin{array}{l} \forall \sigma : (\sigma \circ c o n s e q (R) \notin G \land \\ \neg \exists R ^ {\prime} \in \mathcal {R} \setminus \{R \}: \sigma \circ c o n s e q (R) \in a n t e c (R ^ {\prime})  . \end{array}
$$

<sup>w</sup> <sup>x</sup> A3 Subsumed rule: a rule R is subsumed iff there exists a more general rule:

$$
\exists R ^ {\prime} \in S C R \setminus \{R \}, \exists \sigma : R ^ {\prime} \rightarrow \sigma \circ R.
$$

<sup>w</sup> <sup>x</sup> A4 Redundant rule: a rule R is redundant in rule set <sub>R</sub> iff R is not essential for the computation of any goal literal from any environment:

$$
\forall e \in \mathcal {E}, \forall g \in \mathcal {G}:
$$

if SCR<sup>j</sup>e<sup>&</sup>g then ${ \mathcal { R } } \setminus \{ R \} \cup e \vdash g$

Anomalies A1 – A3 are special cases of A4 .<sup>w</sup> <sup>x w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup>

<sup>w</sup> <sup>x</sup>  A5 Inconsistent rule pair: rules R and R are an inconsistent pair iff R and R are both applicable and derive a semantic constraint:

'e <sup>g</sup> <sub>E</sub> , ' , ' :

$$
\begin{array}{l} \mathcal {R} \cup e + \sigma \circ c o n s e q (R) \wedge \\ \mathcal {R} \cup e + \sigma^ {\prime} \circ c o n s e q (R ^ {\prime}) \wedge \\ \big \{\sigma \circ c o n s e q (R), \sigma^ {\prime} \circ c o n s e q (R ^ {\prime}) \big \} \in C. \end{array}
$$

<sup>w</sup> <sup>x</sup> A6 Inconsistent rule set: a rule set <sub>R</sub> is inconsistent iff from some legal input it is possible to derive a semantic constraint from <sub>R</sub>:

$$
\exists e \in \mathscr {E}, \exists c \in C: \mathscr {R} \cup e \vdash c.
$$

Anomaly A5 is a special case of A6 .<sup>w x</sup> <sup>w x</sup>

<sup>w</sup> <sup>x</sup> A7 Circular rule set: a rule set <sub>R</sub> is circular iff antec RŽ . cannot be derived from any environment, except by adding R’s consequent:

$$
\exists R \in \mathscr {R}: \forall e \in \mathscr {E}: \mathscr {R} \cup e \vdash a n t e c (R) \wedge
$$

$$
\exists e \in \mathscr {E}: \mathscr {R} \cup e \cup \operatorname{conseq} (R) \vdash \operatorname{antec} (R).
$$

<sup>w</sup> <sup>x</sup> A8 Unused input: an input literal $i \in \mathcal { I }$ is unused iff any result that can be computed from an environment can also be computed from that environment minus i:

$$
\forall e \in \mathscr {E} \forall g \in \mathscr {G}: \text { if } \mathscr {R} \cup e \vdash g \text { then } \mathscr {R} \cup e \setminus \{i \} \vdash g.
$$

<sup>w</sup> <sup>x</sup> A9 Incomplete rule set: a rule set $\mathcal { R }$ is incomplete iff there exists some output that cannot be computed from any environment:

$$
\exists g \in \mathcal {G}: \forall e \in \mathcal {E R} \cup e \vdash g,
$$

## 3. KADS inference structures

In this section, we describe KADS inference structures, both informally and formally. The informal description is by now well known in the literature see Ref. 9 . Our particular formalisation ofŽ <sup>w</sup> <sup>x</sup>. KADS inference structures is new, and is based on the notions from Ref. 8 , although we have simpli-<sup>w</sup> <sup>x</sup> fied the formal treatment.

## 3.1. Informal description

KADS inference structures are used to model iŽ . what the legal inferences are that can be made by a system; ii the role that domain knowledge plays in Ž . these inference steps; and iii the dependencies be-Ž . tween these inference steps. An inference structure is a collection of inference steps and knowledge roles. See Fig. 1 for a simple example. Each inference step is a relation between its input knowledge roles and output knowledge roles. Each knowledge role is a collection of domain knowledge that, by being input or output of a particular inference step, plays a particular role in the inference process. Dependencies between inference steps are modelled by sharing knowledge roles among inference steps: the output of one inference step can be the input for another inference step.

Notice that a KADS inference structure is indeed at the abstraction level of a conceptual model: it describes inference steps and knowledge roles without committing us to a particular data-structure to represent the knowledge roles, or to a particular algorithm to implement the inference steps. Furthermore, an inference structure is indeed declarative and not procedural, as required in Section 1: it expresses data-dependencies among inference steps but does not specify control flow. For example, in Fig. 1, many different control regimes can still be imposed: first select all maximal elements or all minimal elements, or selecting one maximal and minimal element alternatively, etc. Such control flows are not specified in the inference structure, leaving them fully declarative.

![](/api/attachments/UYR6SCW9/fulltext/images/1133873b965f3040fc8d7b3c5a6b7cf0df51a4d01e42aafed7a443310a4998e6.jpg)  
Fig. 1. A KADS inference structure for computing the distance between two sets. Inference steps are ovals, knowledge roles are boxes, arrows indicate data dependency. In a , inference steps max and min construct from their input knowledge rolesŽ . $s e t _ { 1 }$ and $s e t _ { 2 }$ the pairs of minima or maxima respectively. The inference step diff subsequently computes the difference between the elements of such a pair to produce a measure of the distance between the two input sets.

It is exactly this set of properties which makes KADS inference structures so useful for validation and verification. They define the functionality of a KBS, but do so independently of particular datastructures and control choices. This means that any properties we will proof of the inference structures will also be independent of such choices. This allows validation and verification to be done in an earlier stage of KBS development, before choices are made concerning such implementation details. Any results obtained for the conceptual model will remain valid for different designs that we might choose in a later stage. It will be convenient to use both a graph-theoretical and a logical formalisation.

## 3.2. Graph-theoretical formalisation

An inference structure is a directed graph where the nodes are inference steps or knowledge roles, and where any edge connects either an inference step to a knowledge role or vice versa. All sources and sinks of such a graph must be knowledge roles.

## 3.3. Logical formalisation

The formalisation given here is compatible with the formalisation of inference structures in our speci-Ž .<sup>2</sup> fication language ML 10 , but the precise details<sup>w</sup> <sup>x</sup> of the relation are beyond the scope of this paper. After this work was completed, we learned that it resembles the formalisation of data-flow diagrams, as given in Ref. 11 . Although the spirit of that <sup>w</sup> <sup>x</sup> formalisation is very similar to ours, many of the technical details are significantly different.

## 3.4. Knowledge role

Each knowledge role is a unique first-order variable of a unique type. It may seem strange that knowledge roles which contain domain knowledgeŽ . are formalised by first order variables i.e., ranging Ž over terms and not by sentences. By formalising an. inference structure as a meta-theory of the domain-Žknowledge as done in $( \mathrm { M L } ) ^ { 2 } )$ , we can still model domain knowledge as first-order sentences while viewing knowledge roles as variables over terms. Again, we refer to Ref. 10 for the technical details<sup>w</sup> <sup>x</sup> of this solution.

## 3.5. Inference step

An inference step is a predicate with, as arguments, the variables corresponding to the connecting roles. The predicate characterises the input<sup>r</sup>output relation of the inference step.

Example: the inference step diff from Fig. 1 is formalised as predicate diff yŽ . < pairs, z<measure , defined by:

$$
\forall y:: p a i r s, z:: m e a s u r e: d i f f (y; z) \leftrightarrow
$$

$$
\exists y _ {1}, y _ {2}: y = \left(y _ {1}, y _ {2}\right) \land z = y _ {1} - y _ {2}.\tag{1}
$$

The notation y< pairs indicates that variable y is of type pairs. We use the ; notation to separate input arguments from output arguments, but this notation has no formal relevance.

## 3.6. Confluent knowledge role

A knowledge role is confluent $i f f$ it is an output role of more than one inference step.

## 3.7. Confluence-free inference structure

An inference structure which is free from confluent knowledge roles is formalised by the conjunction of its inference steps. If a knowledge role r connects two inference steps sayŽ $p _ { 1 }$ and $p _ { 2 } )$ , then $p _ { 1 }$ and $p _ { 2 }$ use the same variable for the argument of type r.

Example: the inference structure from figure Fig. 1b is formalised as:

$$
\begin{array}{l} \langle x _ {1}:: s e t _ {1}, x _ {2}:: s e t _ {2}, y:: p a i r s, z:: m e a s u r e \rangle \\ \min (x _ {1}, x _ {2}; y) \wedge d i f f (y, z). \end{array}
$$

Notice that all occurrences of the variables in this formula are free. The $\langle \dots \rangle$ notation is only an informal annotation to indicate the typing of these free variables.

## 3.8. Terminal roles

A knowledge role is a terminal role $i f f$ it is not the input role of any inference step.

## 3.9. Initial roles

A knowledge role is an initial role $i f f$ it is not the output role of any inference step.

## 3.10. Fully connected inference structure

An inference structure I is fully connected iff there is a sequence of connected steps and roles between any two roles if we ignore the direction of the edges.

## 3.11. Confluence-free sub-structure

J is a confluence-free substructure of inference structure I iff J is a fully connected subgraph of I that includes all terminal roles of I and where no role is the output of more than one inference step. Confluence-free substructures of I can be obtained by ‘tracing back’ from the terminal roles of I, and choosing one alternative when there is a choice of preceding inference steps.

Example: Fig. 1b,c are exactly the confluence-free sub-structures of Fig. 1a.

## 3.12. Formalisation of an inference structure

An inference structure I is formalised as the disjunction of its confluence-free sub-structures.

Example: the inference structure I from Fig. 1b is formalised as: p

$$
\begin{array}{l} \langle x _ {1} \because s e t _ {1}, x _ {2} \because s e t _ {2}, y \because p a i r s, z \because m e a s u r e \rangle \\ \big (\min (x _ {1}, x _ {2}; y) \wedge d i f f (y; z) \big) \vee \\ \big (\max (x _ {1}, x _ {2}; y) \wedge d i f f (y; z) \big). \end{array}
$$

Prefix: the prefix of an inference $p$ in an inference structure I is the largest fully-connected subgraph J of I of which the terminal roles are all the input roles of $p .$

Example: the following formula is the prefix of diff in Fig. 1a:

prefix diff Ž . <sup>'</sup>

$$
\langle x _ {1} \because s e t _ {1}, x _ {2} \because s e t _ {2}, y \because p a i r s, z \because m e a s u r e \rangle
$$

$$
\min \left(x _ {1}, x _ {2}; y\right) \vee \max \left(x _ {1}, x _ {2}; y\right).
$$

## 3.13. Assignment to a knowledge role

An assignment of a value Õal<type to a knowledge role Õar<type is a substitution $\sigma = \{ v a r / v a l \}$ where Õal is a ground term i.e., not containing Ž variables . We will also speak of an assignment for. m u ltip le k n o w led g e ro les w h en $\sigma =$ $\{ ( v a r _ { 1 } / v a l _ { 1 } ) , \ldots , ( v a r _ { n } / v a l _ { n } ) \}$

## 3.14. Satisfying an inference structure

Let be an assignment for all the knowledge roles occurring in an inference structure I, and let DEF be the definition of all inference steps occurring in I Ž Ž . in the same way that Eq. 1 is the definition for $d i f f )$ , then $\sigma$ satisfies I iff $\mathrm { D E F } \models \sigma \circ I .$ This definition allows I to consist of a single inference step, in which case we will speak of the satisfaction of the inference step. We will often implicitly assume the definition of all the inference steps in DEF, and will not keep including DEF in our formulae. Because of this, and to improve the readability, instead of $\mathrm { D E F } \models \sigma \circ I$ we will write $\operatorname { S A T } ( \sigma , \ I )$ When writing SATŽ . , I , is assumed to be a ground substitution, as mentioned before. Furthermore, must be an assignment for all knowledge roles in I. The intuition behind $\operatorname { S A T } ( \sigma , I )$ is that is an assignment to knowledge roles in I corresponding to a legal execution of I.

Example: if DEF is definition Eq. 1 for Ž . $d i f f$ plus the obvious definitions for max and min, then the following assignments $\sigma _ { 1 }$ and $\sigma _ { 2 }$ satisfy the inference structure from Fig. 1 as formalised in 3 :Ž .

$$
\begin{array}{l} \sigma_ {1} = \big \{\big (x _ {1} / \{1, 2, 3 \} \big), \big (x _ {2} \{4, 6, 8 \} \big), \big (y / (1, 4) \big), \big (z / 3 \big) \big) \\ \sigma_ {2} = \big \{\big (x _ {1} / \{1, 2, 3 \} \big), \big (x _ {2} \{4, 6, 8 \} \big), \big (y / (3, 8) \big), \big (z / 5 \big) \big) \end{array}
$$

Notice that $\sigma _ { 1 }$ and $\sigma _ { 2 }$ assign the same values to the input roles of I, but contain different assignments for the output roles. This reflects the non-determinacy of the inference structure $I ,$ as revealed by the fact that it has multiple confluence-free sub-structures.

## 4. Anomalies for inference structures

In this section, we will use the formalisation of KADS inference structures from Section 3 to apply Pr & Sh’s definition of rule-based anomalies to inference structures. As explained in Section 1, this will provide us with a formulation of anomalies in terms of a proper conceptual model, instead of the implementation specific language of production rules.

The intuition behind our reformulation is to view an inference step as the analogue of a rule, and a rule set as an entire inference structure. Antecedent and consequent of a rule then correspond to the input and output types of an inference step, and input- and goal-literals become all possible values for the initial and terminal roles of an inference structure. This analogy can be made precise by the following rules: Ž . Ž . 1 for an inference structure I, inputs I is the set of types corresponding to all initial roles of $I ,$ and outputs IŽ . is the set of types corresponding to all terminal roles of I. Additionally, we will write intern IŽ . for the set of all types that are neither initial nor terminal roles. We will write $\sigma \sqsubset i n p u t s ( I )$ if $\sigma$ is a substitution for a set of variables of exactly the types in inputs IŽ . Ž . , and similarly for outputs I and intern IŽ . Ž . ; 2 the goal set $\mathcal { G }$ is the set of all possible assignments to terminal roles. For example, if an inference structure has two terminal roles, $r _ { 1 }$ and $r _ { 2 } ,$ then $\mathcal { G }$ will have the form $\mathcal { G } = \{ r _ { 1 } / v a l _ { 1 1 } ,$ $r _ { 1 } / v a l _ { 1 2 } , . . . , r _ { 2 } / v a l _ { 2 1 } , r _ { 2 } / v a l _ { 2 2 } , . . . \} ; ( 3 )$ the input set $\mathcal { I }$ is the set of all possible assignments to initial roles. $\mathbf { A } \mathbf { s }$ before, $\mathcal { G }$ and $\mathcal { I }$ will in general be infinite; 4 the definitions of semantic constraint andŽ . the constraint set $\mathcal { C }$ are as before and; 5 an envi-Ž . ronment is a subset of $\mathcal { I }$ that assigns a value to each initial knowledge role in such a way that no semantic constraint is implied. As before, we write $\mathcal { E }$ for the possibly infinite set of all such environ- Ž . ments. Formally: $\varepsilon \subseteq \mathcal { I }$ and $\varepsilon \stackrel { } { \mathop { : } } i n p u t s ( I )$ and $\forall \varepsilon \circ c$ for all $\varepsilon \in { \mathcal { E } }$ and all $c \in { \mathcal { C } }$

Comparing this list with the one in Section 2 shows that a shift has taken place from predicates to terms in the formalisation: in Ref. 1<sup>w</sup> <sup>x</sup> $\mathcal { G }$ and $\mathcal { I }$ Žand consequently $\mathcal { E } )$ were sets of ground literals and are now sets of ground term-substitutions. Similarly, antec RŽ . Ž . and conseq R were sets of literals while inputs IŽ . Ž . and outputs I are sets of term-types. This is the result of no longer taking a sentence a rule asŽ . the primitive element, but rather a predicate in- Ž ference step . This shift will be noticeable in the. reformulation of Pr&Sh’s anomalies to which we turn now. The important point to notice in the new formulation of the anomalies below is the close correspondence with the formulation of the anomalies in Section 2, both formally and informally.

<sup>w</sup> <sup>)</sup> A1 Unsatisfiable inference step: an inference<sup>x</sup> step p is unsatisfiable iff there is no way of satisfying p from any legal input:

$$
\neg \big (\exists \varepsilon \in \mathscr {E}, \exists \sigma : \mathrm{SAT} \big (\varepsilon \sigma , p r e f i x (p) \wedge p \big) \big),
$$

i.e., there exists no input environment e which can be completed with another substitution $\sigma$ to form a satisfying assignment for p and its prefix.

<sup>w</sup> <sup>)</sup> A2 Unusuable inference step: an inference step <sup>x</sup> $p$ is unusable $i f f$ no output value of $p$ contributes to either the goal-set or to satisfying another inference $p ^ { \prime } \colon$

$$
\begin{array}{l l} \forall \sigma , \forall \omega \sqsubset o u t p u t s (p): \\ \text {if SAT(  \sigma\omega,p)} \\ \text {then \omega\cap SCG = 0 and} \\ \neg (\exists p ^ {\prime} \in I \setminus \{p \}, \exists \sigma^ {\prime}: & \text {SAT(  \sigma^{\prime} \omega,p^{\prime})\wedge} \\ & \neg S A T (\sigma^ {\prime}, p ^ {\prime})), \end{array}
$$

i.e., for all possible satisfying assignments  of $p ,$ the output roles never contribute to the goal set $\mathcal { G } _ { : }$ , and they also never form an essential part of any satisfying assignment $\sigma { ' } \omega$ for another inference step $p ^ { \prime }$

An example of this is the following: if in the inference structure $( p _ { 1 } ( x _ { 1 } ; y ) \lor p _ { 2 } ( x _ { 2 } ; y ) ) \land q ( y ; z )$ the inference $q$ never holds for any value of y derived by $p _ { 2 }$ , then $p _ { 2 }$ is unusable.

<sup>w</sup> <sup>)</sup> A3 Subsumed inference step: an inference step <sup>x</sup> $p$ is subsumed $i f f$ there exists another inference which, for any input<sup>r</sup>output relation of $p ,$ specifies at least the same output from at most the same input:

$$
\begin{array}{l} \exists p ^ {\prime} \in I \setminus \{p \}: \\ \forall \sigma \sqsubset i n p u t s (p), \forall \omega \sqsubset o u t p u t s (p) \\ \text { if } S A T (\sigma \omega , p) \\ \text { then } \exists \sigma^ {\prime} \sqsubset i n p u t s (p ^ {\prime}), \exists \omega^ {\prime} \sqsubset o u t p u t s (p ^ {\prime}): \\ S A T (\sigma^ {\prime} \omega^ {\prime}, p ^ {\prime}) \wedge \sigma^ {\prime} \subseteq \sigma \wedge \omega \subseteq \omega^ {\prime}. \end{array}
$$

An example is the following: in the inference structure $p ( \boldsymbol { x } _ { 1 } , \boldsymbol { x } _ { 2 } ; \boldsymbol { y } ) \vee p ^ { \prime } ( \boldsymbol { x } _ { 1 } ; \boldsymbol { y } )$ , if for any value of $x _ { 1 } ,$ $p ^ { \prime }$ computes the same value for y as p does, irrespective of the value of $x _ { 2 }$ Žin other words: $p ( x _ { 1 } ,$ $x _ { 2 } ; y ) \land p ^ { \prime } ( x _ { 1 } ; y ^ { \prime } )  y = y ^ { \prime } )$ , then $p$ is subsumed by $p ^ { \prime } .$

<sup>w</sup> <sup>)</sup> A4 Redundant inference step: an inference step<sup>x</sup> $p$ is redundant in inference structure $I ~ i f f ~ p$ is not essential for the derivation of any output assignment from any environment:

$$
\begin{array}{l} \forall \varepsilon \in \mathcal {E}, \forall \omega \sqsubset o u t p u t (I): \\ \text { if } \exists \sigma \sqsubset i n t e r n (I): \mathrm{SAT} (\varepsilon \sigma \omega , I) \\ \text { then } \exists \sigma^ {\prime} i n t e r n (I): \mathrm{SAT} (\varepsilon \sigma^ {\prime} \omega , I \setminus \{p \}), \end{array}
$$

i.e., whenever some value for I ’s output roles is computed from some input environment  Žvia an additional assignment $\sigma$ for I ’s internal roles , then. the same output values can be computed from the same input values via an inference structure that does not contain $p .$ Notice that, as before, ${ [ \mathrm { A } 1 ^ { \ast } ] } _ { - }$ $[ \mathbf { A } \boldsymbol { 3 } ^ { * } ]$ are special cases of $[ \mathrm { A } 4 ^ { \ast } ]$

<sup>w</sup> <sup>)</sup> A5 Inconsistent inference steps: we do not <sup>x</sup> treat this case separately, since it is a rather uninteresting special case of $[ \mathsf { A } 6 ^ { \ast } ]$

<sup>w</sup> <sup>)</sup> A6 Inconsistent inference structure: an infer-<sup>x</sup> ence structure I is inconsistent iff from some legal input it is possible to derive a role assignment that satisfies I and which also satisfies a semantic constraint:

$$
\exists \varepsilon \in \mathscr {E}, \exists \sigma , \exists c \in S C C: \mathrm{SAT} (\varepsilon \sigma , I) \wedge \mathrm{SAT} (\varepsilon \sigma , c).
$$

$[ \mathrm { A } 7 ^ { \ast } ]$ Circular inference structure: we have not succeeded in finding a suitable definition of circularity of an inference structure.

$[ \mathrm { A } 8 ^ { \ast } ]$ Unused input value: an input value $( v a r / i )$ $\in \mathcal { I }$ is unused $i f f$ any result that can be computed from an environment  can also be computed from that environment minus $( v a r / i ) \colon$

$$
\begin{array}{l} \forall \varepsilon \in \mathcal {E}, \forall \omega \sqsubset o u t p u t (I), \forall \sigma \sqsubset i n t e r n (I) \colon \\ \text { if } \operatorname{SAT} (\varepsilon \sigma \omega , I) \text { then } \operatorname{SAT} (\varepsilon \sigma \omega \setminus \{v a r / i \}, I), \end{array}
$$

i.e., for any input environment and for any output assignment that can be computed from via some internal assignment  , the same  can be computed from the same without using $( v a r / i )$

As an example, in the inference structure mentioned under $[ \mathrm { A } 3 ^ { \ast } ]$ all values for $x _ { 2 }$ would be unused.

<sup>w</sup> <sup>)</sup> A9 Incomplete inference structure: an infer-<sup>x</sup> ence structure I is incomplete iff there is a terminal role value which cannot be derived from any environment.

$$
\exists (v a r / g) \in S C G: \forall \varepsilon \in \mathscr {E}, \forall \sigma :
$$

$$
\text { if } \mathrm{SAT} (\varepsilon \sigma , I) \text { then } (v a r / g) \notin \sigma ,
$$

i.e., no possible way of satisfying I from some input environment e contains $( v a r / g )$

## 5. Conclusion

In this paper, we have presented i a number ofŽ . improvements to the formalisation of rule-based anomalies by Pr & Sh, ii a formalisation of KADSŽ . inference structures, and iii an interpretation of theŽ . traditional anomalies in terms of these implementation independent structures. This greatly improves the usefulness and applicability of the anomalies as a method of KBS verification. It also opens up the possibility to analyse other properties of inference structures as part of KBS verification, such as determinedness, consistency and coherence, as defined in Ref. 8 .<sup>w</sup> <sup>x</sup>

Some technical problems remain to be solved for our formalisation: the current formalisation can only deal with circular inference structures in a trivial way, which does not correspond to their actual use in practice, namely to model non-monotonic reasoning processes. It remains to be seen if the current formalisation can be extended to deal with these cases.

As Pr & Sh state, anomalies are not errors, they are only indications of possible errors. As a result, anomaly detection is only half the work. After an anomaly has been detected in an application, we need to know which errors are responsible for that anomaly, and how these errors can be repaired. Further study of error-classes for inference structures is required before this problem can solved satisfactorily.

As with any formal method, the proof of the pudding is in the eating. At first sight, it might appear that our formulation of the anomalies is not directly applicable: many of the anomalies state properties about infinite sets such as input- or goalliterals. However, the same objection could be raised against Pr&Sh’s original anomalies. Nevertheless, Ref. 1 reports a number of case studies that have established both the feasibility and the usefulness of the anomalies on a number of realistic KBS applications. This gives us sufficient confidence that this will also be the case for our reformulation of the anomalies for KADS models.

The next step in this work must no doubt be to apply these anomalies to realistic KADS models, and to subject our definitions to similar empirical tests as reported by Pr&Sh. To achieve this end, it will certainly be necessary to build software that automatically checks inference structures for the anomalies that we have defined in this paper.

## Acknowledgements

We are grateful to two anonymous referees, whose comments have helped to improve this paper.

## Appendix A. Comments on the work by Preece and Shinghal

In this section we describe and motivate the alterations we have made in Section 2 to the definitions from Ref. 1 .<sup>w</sup> <sup>x</sup>

<sup>w</sup> <sup>x</sup> A1 Unsatisfiable rule: Pr & Sh’s original definition is:

$$
\begin{array}{l} \exists l \in a n t e c (R) \colon \\ \neg (\exists \sigma : \sigma \circ l \in S C I \lor \\ \exists R ^ {\prime} \in S C R \setminus \{R \}: \exists \sigma : \sigma \circ l \in c o n s e q (R ^ {\prime}) \big). \end{array}
$$

Because of the existential quantification over a single antecedent literal l, this definition disregards the case when two antecedent literals are both satisfiable, but not under the same substitution. Consider the rule $l _ { 1 } ( 1 , y ) \land l _ { 2 } ( x , 2 )  m ( x , y )$ with $\mathcal { E } = \{ ( 1 , 1 )$ Ž . 2,2 . Pr & Sh’s definition does not capture this rule4 as unsatisfiable, although it will never fire from either of the given environments. Besides being simpler, our definition does not suffer from this problem. On the other hand, the original definition has the advantage of being more easily computable by automatic checkers.

<sup>w</sup> <sup>x</sup> A2 Unusable rule: our formulation is equivalent to the one by Pr&Sh.

<sup>w</sup> <sup>x</sup> A3 Subsumed rule: Pr&Sh’s definition for a subsumed rule is:

$$
\exists R ^ {\prime} \exists \sigma : R \rightarrow \sigma \circ R ^ {\prime}.
$$

We believe this to be an error. Consider $R = a  b$ and $R ^ { \prime } = a \wedge a ^ { \prime } \to b$ . Then $R \to R ^ { \prime }$ but it would seem to us that R is subsumed, rather than R.

<sup>w</sup> <sup>x</sup> A4 Redundant rule: Pr&Sh’s definition for redundancy of R is:

$$
\forall e \in \mathscr {E}: \{h | S C R \cup e \vdash h \} = \{h | S C R \setminus \{R \} \cup e \vdash h \}.
$$

Our definition differs from this in two aspects: first, if we regard this equality as a mutual inclusion of the left- and right-hand side, then the inclusion $\supseteq$ of this equality is trivial by monotonicity of Ž $\vdash ) ,$ so we omit it from our definition. Secondly, we restrict the inclusion to literals from $\mathcal { G }$ instead of using any literal h. After all, rules are also redundant if they only contribute to irrelevant literals. Therefore, our definition makes all rules redundant which do not contribute directly or indirectly to the computationŽ . of goal literals, which is not the case in Pr & Sh’s definition.

<sup>w</sup> <sup>x</sup> A5 Inconsistent rule pair: besides our definition, Pr&Sh also demand that $a n t e c ( R )  a n t e c ( R ^ { \prime } )$ Presumably, this is to ensure that R and $R ^ { \prime }$ are applicable in the same cases. In our definition, we explicitly demand that both R and $R ^ { \prime }$ are applicable from the same environment, rather than relying on Ž . Ž  the special case of antec R ™antec R .. Pr&Sh call this anomaly ‘ambivalent rule pair’, but we prefer the term ‘inconsistent’, since the rules R and $R ^ { \prime }$ imply a semantic constraint which is interpreted as a semantic inconsistency. Again, as with A3 , the<sup>w</sup> <sup>x</sup> original version has the advantage of being more easily computable by automatic checkers.

<sup>w</sup> <sup>x</sup> A6 Inconsistent rule set: our definition is equivalent to the one by Pr&Sh.

<sup>w</sup> <sup>x</sup> A7 Circular rule set: Pr & Sh’s original definition is:

$$
\begin{array}{c} \exists R \in S C R, \exists e \in \mathscr {E}: S C R \cup e   \forall   a n t e c (  R) \wedge \\ S C R \cup e \cup c o n s e q (  R) \vdash a n t e c (  R) \end{array}
$$

This already makes R circular if its antecedent cannot be derived from some environment e except by adding $R ^ { * } s$ consequent to e. Our definition is stronger, and demands that R is only circular if its antecedent cannot be derived from any environment, although it can be derived from some environment by adding $R ^ { * } s$ consequent.

<sup>w</sup> <sup>x</sup> A8 Unused input: Pr & Sh’s original definition for an unused input i demanded that:

$$
i \notin S C G \land \neg (\exists R \in S C R, \exists \sigma : i \in \sigma \bigcirc a n t e c (R))
$$

which says that i is never used, either as a final result, or for triggering a rule. This definition suffers from the problem that i may be used by a rule that, when using i, does not contribute to computing any element of ${ \mathcal { G } } ,$ even though the rule does contribute to elements of $\mathcal { G }$ from other environments, and therefore does not qualify as an unusable rule. This would mean that i goes unnoticed as an unused input. The alternative definition that we proposed does not suffer from this problem.

<sup>w</sup> <sup>x</sup> A9 Incomplete rule set: Pr&Sh’s definition of an incomplete rule set was:

$$
\exists e \in \mathscr {E}: \forall g \in S C G: S C R \cup e \forall g,
$$

Ži.e., there exists an environment from which $\mathcal { R }$ will not produce any output at all . This definition, which . has the reverse quantifier scheme from the one we propose, says more about the environment $e$ than it does about the rule set ${ \mathcal { R } } \colon$ the fact that $R \cup e \forall g$ for any g may be due to an erroneous environment e.g., Ž $e = \emptyset )$ which was not prevented by sufficiently strong semantic constraints. By universally quantifying over $\mathcal { E }$ , our definition avoids this problem.

## References

<sup>w</sup> <sup>x</sup> 1 A. Preece, R. Shinghal, Foundation and application of knowledge base verification, Int. J. Intelligent Syst. 9 1940 Ž . 683–701.

<sup>w</sup> <sup>x</sup> 2 M. Suwa, A. Scott, E. Shortliffe, An approach to verifying completeness and consistency in a rule-based expert system, AI Magazine 3 4 1982 16–21.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 T.A. Nguyen, W.A. Perkins, T.J. Laffey, Checking an expert systems knowledge base for consistency and completeness, IJCAI-85, 1985, pp. 375–378.

<sup>w</sup> <sup>x</sup> 4 A. Ginsberg, Knowledge-base reduction: a new approach to checking knowledge bases for inconsistency and redundancy, Proceedings of the 7th National Conference on Artificia Intelligence AAAI’88, 1988, pp. 585–589.

<sup>w</sup> <sup>x</sup> 5 C. Chang, J. Combs, R. Stachowitz, A report on the expert systems validation associate eva , Expert Syst. Appl. 1 3Ž . Ž . Ž .1990 217–230.

<sup>w</sup> <sup>x</sup> 6 B.J. Wielinga, A.Th. Schreiber, J.A. Breuker, Modelling expertise, In: A.Th. Schreiber, B.J. Wielinga, J.A. Breuker Ž . Eds. , KADS: A Principled Approach to Knowledge-based System Development, Academic Press, London, 1993, pp. 21–46.

<sup>w</sup> <sup>x</sup> 7 D. Fensel, F. van Harmelen, A comparison of languages which operationalise and formalise KADS models of expertise, Knowledge Eng. Rev. 9 1994 105–146.Ž .

<sup>w</sup> <sup>x</sup> 8 M. Aben, Formal methods in knowledge engineering, PhD thesis, University of Amsterdam, Faculty of Psychology, ISBN 90-5470-028-9, February 1995.

<sup>w</sup> <sup>x</sup> 9 A.Th. Schreiber, The KADS approach to knowledge engineering, Knowledge Acquisition 4 1 1992 1–4, EditorialŽ . Ž . special issue.

<sup>w</sup> <sup>x</sup> Ž .<sup>2</sup> 10 F. van Harmelen, J.R. Balder, ML : a formal language for KADS models of expertise, Knowledge Acquisition, 4 1Ž . 1992. Special issue: the KADS approach to knowledge engineering, reprinted in KADS: a principled approach to knowledge-based system development, In: A.Th. Schreiber, et al. Ž . Eds. , 1993.

<sup>w</sup> <sup>x</sup> 11 P.G. Larsen, N. Plat, H. Toetenel, A formal semantics of data-flow diagrams, Formal Aspects of Computing 3 1993 Ž . 1–21.

![](/api/attachments/UYR6SCW9/fulltext/images/d440fe41a254cd92b1f6fe039544c86113df01ddc3f0506614691c9850ca70ef.jpg)

Frank van Harmelen 1960 studiedŽ . mathematics and computer science in Amsterdam. In 1989, he was awarded a PhD from the Department of AI in Edinburgh for his research on meta-level reasoning. While in Edinburgh, he worked with Dr. Peter Jackson on Socrates, a logic-based toolkit for expert systems, and with Prof. Alan Bundy on proof planning for inductive theorem proving. After his PhD research, he moved back to Amsterdam where he worked from

1990 to 1995 in the SWI Department under Prof. Wielinga. He was involved in the REFLECT project on the use of reflection in expert systems, and in the KADS project, where he contributed to Ž .<sup>2</sup> the development of the ML language for formally specifying Knowledge-Based Systems. In 1995 he accepted a lectureship at the Vrije Universiteit Amsterdam, where he is a member of the AI research group. His current interests include formal specification languages for knowledge-based systems, meta-reasoning and reflection, and the use of meta-reasoning in diagnosis. He is author of a book on meta-level inference, editor of a book on knowledge-based systems, and has published over 30 research papers.

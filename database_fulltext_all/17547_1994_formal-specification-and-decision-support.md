---
otero_id: 17547
otero_key: "4CQR3PVE"
title: "Formal specification and decision support"
authors: "Paul J. Krause; Patrick J. Byers; Saki Hajnal"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90003-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Formal specification and decision support

Paul J. Krause $^{a,*}$ , Patrick J. Byers $^{b}$ , Saki Hajnal $^{a}$

$^{a}$ Imperial Cancer Research Fund, Lincoln's Inn Fields, London WC2A 3PX, UK

$^{b}$ Department of Mathematics and Computing Science, Surrey University, Guildford, Surrey, UK

To gain widespread acceptance, decision support systems must be built to the highest possible standards. We believe techniques of formal specification and refinement have a valuable role to play in the development of certain components of decision support systems. We present a tutorial study of the use of formal specification focused on a system for maintaining deductive extensions of a knowledge base. The system is specified using an object-oriented variant of the specification language Z. The relationship of the formal specification with existing theoretical work in AI is discussed together with its refinement into a demonstrably correct implementation.

Keywords: DSS development; Formal specification; Software engineering; KBS validation

![](/api/attachments/4CQR3PVE/fulltext/images/2c9a2976667ad166369245480ac329175c34dd7eebabcb56c4405d15257ae947.jpg)

Paul Krause received a degree in mathematics and physics, and a Ph.D. in physics from Exeter University. After seven further years working in low temperature metrology he moved to research in computing science, first at Surrey University and latterly at the Imperial Cancer Research Fund. His research interests include formal specification and development of software, logical models of reasoning and reasoning under uncertainty.

![](/api/attachments/4CQR3PVE/fulltext/images/2fd41d6aeba3af81a72ef2e5631388268dad8721166153c1c3845ee1e04b37cb.jpg)

Patrick Byers gained an MA in mathematics from Cambridge University and obtained a PhD in mathematical logic from the University of Surrey in 1990, studying the model theory of computer programs. Since then he has worked for Smith System Engineering in a variety of areas related to information system modelling and formal specification. Dr. Byers is now working as a consultant and is a director of Information Systems Research Limited. Dr. Byers' interests centre on the formal specification of system behaviour, covering safety critical, real-time and learning systems. He has worked in collaboration with the Imperial Cancer Research Fund on the formalisation of decision procedures since 1989.

Correspondence to: P.J. Krause, Imperial Cancer Research Fund, Lincoln's Inn Fields, London WC2A 3PX, UK.

## 1. Introduction

Computer based support is beginning to show a great deal of potential in medical decision making. However, if such systems are to be relied upon to any extent, then their builders are under a moral, as well as possibly a legal $[12]$ , obligation to use the best practice currently available in their development. Work at the Imperial Cancer Research Fund has been directed at the development of a number of experimental computer-based assistants for medical decision making [e.g. 4]. However, we also have a program of work aimed at addressing how far formal specification techniques in software engineering may, and should, be adapted to meet the needs of developers of such systems $[7,8]$ . We believe that formal techniques can and should be used more widely in system development and, to that end, we present here a tutorial study of the use of one particular specification language which we are using.

To focus the discussion, we will concentrate on one specific component of the complete system. This is a process which maintains the deductive extension of a selected set of facts and inference rules. The extension will be revised as facts (case data) are asserted into, or retracted from, the database. We will use this example to illustrate three aspects of the formal development of software; the elicitation of requirements, the writing of a formal model which satisfies those requirements and the refinement of that specification towards an implementation.

![](/api/attachments/4CQR3PVE/fulltext/images/4bd916ac4f3228f81ee5aef008c8cb6a81267d067501e8fe7849716ea73535b6.jpg)  
Saki Hajnal is a Higher Executive Officer in the Advanced Computation Laboratory of the Imperial Cancer Research Fund. She received her BA in Mathematics and Genetics from the University of Cambridge in 1982. Her research interests include applications of AI and logic-based computing techniques in biology and medicine, particularly the scope for decision support in the interpretation of biomedical images.

$$
\Gamma (\pi_ {1}, \dots , \pi_ {\mathrm{k}})
$$

<table><tr><td>X</td><td>Component Declarations</td></tr><tr><td>Y</td><td>Invariant Predicates</td></tr><tr><td>Z</td><td>Initialisation Predicates</td></tr></table>

Schema 1

The final version of the specification is more complex than the version which will be presented here. However, the aim of this paper is to provide a discussion of the benefits which may be gained from the use of formal methods, rather than concentrate on the technicalities of one completed specification (the full version of the specification may be found in [6]). Perhaps the most important benefits are that:

\- The discipline of writing a formal specification helps in eliciting and clarifying our exact requirements for the intended system.

\- The statement of the required properties in a formal language enables a rigorous appraisal of the intended system, in terms of current theoretical work, to be effected.

\- In implementing the specification by using a process of stepwise refinement, we may be confident that the final program will indeed behave as we have specified.

## 2. Object-oriented process specification

Behavioural Object-Oriented Process Specification, or Schuman–Pitt notation $[16,17]$ , is a variant of the specification language Z $[19,20]$ . As the name suggests, the most obvious difference between the Schuman–Pitt notation and Z is in the former's commitment to the "object-oriented" paradigm for structuring and decomposing complex systems. This notation provides a framework for formally specifying and reasoning about the behaviour of user-defined "classes" of abstract objects. As with Z, data types are specified using simple set-theoretic constructs, with constraints on their values specified using first-order predicate calculus. A simple syntactic structure using "schemas" provides a framework for the specification. A "state-schema" is used to introduce a specific class of abstract objects. Contained within this schema is a characterisation of the internal state for each instance of the class (state components together with state invariants), together with the conditions which must hold in any initial state. A state schema has the generic form shown in Schema 1.

The header of a state schema provides an identifier for the class in question (Γ), as well as naming any formal parameters for that class $(\pi_{1},\ldots,\pi_{k})$ .

The associated “event-schemas” specify the operations which may be carried out on instances of the corresponding classes. The event schema headers include the identifier for the class with which the event is associated ( $\Gamma$ ), together with the name of the operation ( $\phi_{i}$ ) and the names of any input ( $\alpha_{i}$ ) and/or output parameters ( $\rho_{i}$ ) figuring in its signature. Contained within the event schema are the type declarations for the parameters, and statements of the preconditions and postconditions which must be satisfied by the state before and after the event respectively (Schema 2).

Primed variable names in the post-conditions refer to state components after the application of the event. The state invariant introduced in the state schema must continue to be satisfied after any operation on an instance of the associated class is carried out. Consequently, a succinct statement of the explicit changes made by the operation is all that is necessary. A significant departure from Z or VDM is the use of a special rule of historical inference in the Schuman–Pitt notation, whereby only the minimal effect (change of state) need be specified for each event associated with a given class. That is, any elements of the program state which are not explicitly referred to in the event specification are assumed to remain unchanged by the event. This “rest-unchanged" semantics has particularly important implications for the specification of concurrent systems, although this is not a major concern for the present work. It does, however, make for a more succinct specification than that obtained using either Z or VDM.

<table><tr><td colspan="2"> $\Gamma.\phi_{i}(\alpha_{1},\ldots,\alpha_{k}\rightarrow\rho_{1},\ldots,\rho_{n})$ </td></tr><tr><td>P</td><td>Parameter Declarations</td></tr><tr><td>Q</td><td>Precondition Predicates</td></tr><tr><td>R</td><td>Postcondition Predicates</td></tr></table>

Schema 2

## 3. Required properties of a "viable" extension

The extension management system forms a component of a number of programs which are under development in this department for the simulation of expert decision making. The general requirement is that given a theory, as identified in some decision making context, the required program should generate all the consequences of this theory. As more evidence becomes available, this “closure” of the theory will be updated. Early implementations of this update mechanism used Prolog’s negation as failure, thus allowing the update mechanism to have a non-monotonic character. However, it is not necessarily the case that Prolog’s negation as failure has all the properties one might require for non-monotonic reasoning [e.g. 9].

Firstly no changes should be made to the maintained extension unless there is some justification for so doing. Consider, for example, the following rule:

$$
\mathrm{a} \wedge \neg \mathrm{b} \Rightarrow \mathrm{d}.
$$

If fact “a” is asserted into a database containing the above rule, with no information available as to the truth or falsehood of “b”, the following are minimal models: {a,b}, {a,d}. What is actually intended is that only those facts are added to the database which have a justification; in this case, the set {a,d} (we may give “user” as a justification).

Consider now the pair of rules:

$$
\mathrm{a} \wedge \neg \mathrm{b} \Rightarrow \mathrm{c},\tag{i}
$$

$$
\mathrm{c} \wedge \neg \mathrm{d} \Rightarrow \mathrm{b}.\tag{ii}
$$

The user asserts “a”. “c” is concluded using rule (i), then “b” concluded using rule (ii). However, the simultaneous conclusion of “b” and “c” is invalid in this context; we need to ensure that each fact has a currently valid justification.

We next consider self supporting circular reasoning. In a complex rule set, it may not be possible, or may not be considered desirable, to eliminate the possibility of such an occurrence. The difficulty is that once triggered, the mutual supports may continue to justify conclusions even after the triggering fact has been withdrawn. An example of such a rule set is:

$$
\mathrm{c} \Rightarrow \mathrm{d},
$$

$$
\mathrm{d} \Rightarrow \mathrm{e},\tag{iii}
$$

$$
\mathrm{e} \Rightarrow \mathrm{d},\tag{iv}
$$

(v)

Again, initially the facts “c”, “d” and “e” are not present in the database. The user then asserts “c”. “d” and “e” are then both concluded, “d” having support {c,e} and “e” having one justification {d}. The user now retracts “c”. If support is based naively on the presence of justifications, we have an implementation in which only the justification {c} for “d” is withdrawn, but justification {e} remains. So “d” remains in the database. A further constraint must be placed on the set of justifications; the justification set should be well-founded. That is, any conclusion must be derivable in an ordered sequence of inference steps from the asserted facts.

A final insight into the behaviour of the EMS may be gained from the pair of rules:

$$
\mathrm{d} \wedge \neg \mathrm{a} \Rightarrow \mathrm{b},
$$

$$
\mathrm{d} \wedge \neg \mathrm{b} \Rightarrow \mathrm{a}.\tag{vi}
$$

(vii)

We have two possible models on asserting “d”; viz. {d,b} and {d,a}. Suppose we had:

$$
\begin{array}{l} \text { has   -   child(A,C) } \land \neg \text { adopted(C) } \Rightarrow \text { fertile(A) } \\ \text { has   -   child(A,C) } \land \neg \text { fertile(A) } \Rightarrow \text { adopted(C) } \end{array}
$$

Suppose alexandra has a child carla. As the system is intended, there should be no way it can give a preference for adopted(carla) or fertile (alexandra); there are two alternative scenarios. That is to say, with these rules there is one possible world in which adopted(carla) is true, and one in which fertile(alexandra) is true, but neither is true in all possible worlds. Using symbols from modal logic, we may conclude adopted(carla) and fertile(alexandra), i.e. both states are possible. Were, for example, adopted(carla) true in all possible worlds (through some other constraint), then conclude adopted (carla) – it is necessary that adopted(carla).

In summary, we require in the specification statements to the effect that:

1. Justifications for all consequences added to the database must be currently valid.

DB

```txt
Facts : set(DATA)
RuleSet : set(GROUND_RULE)
PossibleC : set(DATA)
NecessaryC : set(DATA)

PossibleC = {φ:DATA |∃S ⊆ DATA · viable(Facts,S,RuleSet) ∧ φ ∈ S}
NecessaryC = {φ:DATA |∀S ⊆ DATA · viable(Facts,S,RuleSet) ⇒ φ ∈ S}

Facts' = ∅
```

## Schema 3

2. All chains of justifications generated by application of the rule set should be grounded in user asserted facts.

3. Account must be taken of possible indeterminacy in the applicability of rules in the rule set. In order to fulfil these requirements, we have produced the following formal specification.

## 4. Formal specification of the database extension management system

This is a specification of a database extended by the deductive closure of the rule set contained in that database. We will only consider the propositional case; a first order version of the specification is documented in [6]. We wish to maintain information about all possible extensions generated by the rule set, grounded in the facts in the database. Facts are positive ground literals, and conclusions are also positive literals. Each rule is specified as a triple: (positive antecedents, negative antecedents, consequent). A rule is satisfiable if all of the positive antecedents, and none of the negative antecedents, are present in the database.

We first define a class DB with four components; Facts, RuleSet, PossibleC and NecessaryC. The user may assert facts into, or retract facts from the set Facts. The RuleSet is as discussed above. Initially the set of Facts is empty. The last two state components contain information on the deductive closure of the rule set. PossibleC contains all those items of data for which there exists at least one viable extension of the fact set containing that item. NecessaryC contains those items of data which are contained in all viable extensions of the fact set.

```txt
viable(Facts, Consequences, RuleSet) ≡
(∃J: seq set(DATA) ·
    head J = Facts
    ∧ last J = Consequences
    ∧ ∀i < #J · ∃C:DATA ·
    J(i + 1) = J(i) ∪ {C}
    ∧ ∃(P,N,C) ∈ RuleSet ·
    P ⊆ J(i)
    ∧ N ∩ Consequences = ∅)
∧
(∀ (P,N,C) ∈ RuleSet ·
    P ⊆ Consequences
    ∧ N ∩ Consequences = ∅
    ⇒ C ∈ Consequences)
```

Schema 4

The term “viable” needs a precise definition. An extension is viable if it contains all the user asserted facts and all, and only, consequences of those facts which may be derived by a finite sequence of rule applications. The formal definition of a viable extension given in Schemas 3 and 4 captures the notions of well-foundedness and validity of the supports for the consequence set (the appendix contains a glossary of the Z notation used here). The following types are used:

Given Types: DATA (Positive ground literals)
Derived Types: GROUND – RULE:

set(DATA), set(DATA), DATA)

The first condition for a consequence set to be viable ensures that all consequences are grounded in the set Facts. A consequent is only added to the conclusion set if it could be derived from the fact set in a finite sequence of inferences, and if the derivation will not be invalidated by the later addition of further consequences to the database.

The second condition ensures that any consequence which could legitimately be added to the consequence set is added.

These are the only data which are added to the consequence set in deriving it from the set Facts.

The event-schemas 5 and 6 specify the operations which may be carried out on instances of the class DB. As mentioned already, a succinct statement of the explicit changes made by an operation is all that is necessary. Assert and retract are simple to specify in this notation. For example, in the case of asserting an item of data into the database, we only need specify that the data item of interest, $\phi$ , is present in the set Facts' after the operation (there are no preconditions, other than that the element $\phi$ to be asserted must be of type DATA).

Retract just removes an item of data from the fact set. The datum is not necessarily removed from the database. It may be present in either PossibleC or NecessaryC if it is derivable from the remaining facts.

The “rest-unchanged” semantics ensures that all other elements that were present in the set Facts before either operation are present in the set Facts’ after the operation. The state invariant ensures that the sets PossibleC and NecessaryC are updated accordingly.

Having now captured the notions of “possible” and “necessary” in terms of viable extensions, we

DB.assert(φ)

<table><tr><td>φ:DATA</td></tr><tr><td>φ ∈ Facts&#x27;</td></tr><tr><td>Schema 5DB.retract(φ)</td></tr><tr><td>φ:DATA</td></tr><tr><td>φ∉ Facts&#x27;</td></tr></table>

Schema 6

can specify two query operations. The first succeeds if the specified element is a member of all possible extensions of the fact set (Schema 7).

The second succeeds if the specified element is a member of at least one of the possible extensions (Schema 8).

## 5. Proof obligations

In many engineering disciplines it is common for a model to be constructed as part of the process of specifying and designing a system. This enables predictions to be made about the properties of the end product, and a full analysis of its behaviour under extreme conditions to be carried out, before construction is initiated. The model may be a physical scale model or it may be a mathematical model. Both permit the design to be evaluated in terms of some known underlying theory. Formal specification languages are intended to enable software engineers to produce a mathematical model of the software they wish to build before committing to coding it. As well as providing an unambiguous statement of the program's intended behaviour, the formal specification may be subject to mathematical proofs and formal analysis of its properties. In addition, once the formal specification has been finalised, a process of “stepwise refinement” may be used for generating software which correctly implements the specification $[23]$ .

DB.nq(φ)

φ:DATA

$\varphi \in$ NecessaryC

Schema 7

DB.pq(φ)

<table><tr><td>φ:DATA</td></tr><tr><td>φ ∈ PossibleC</td></tr></table>

Schema 8

A demonstration of the fulfillment of the static proof obligations for the Extension Management System is given in [6]. These are the minimum set of proofs which need to be undertaken in the validation of a formal specification. A complete statement of the requirements can be found in [17], and the fulfillment of these obligations is in fact very straightforward for this particular specification [6].

The next step is to consider the dynamic behaviour of the complete system as specified. A significant benefit accruing from a commitment to the object-oriented paradigm in the specification language we have been using is that it becomes plausible to speak about the behaviour of individual instances of a given class; that is, to consider how the state of such objects may evolve from initialisation over time. A full discussion of these aspects does, unfortunately, become quite technical. It is, for example, necessary to augment the event schemas with predicates embodying an explicit statement of the “rest-unchanged” semantics before an analysis of the behaviour can be undertaken. For a description of the nature of these predicates and the sort of proofs of behaviour that may be undertaken see $[17]$ . The point to emphasise here is that the behaviour of the specified system can be subject to mathematical analysis.

The state invariants of the class DB ensure that after an event has occurred to an instance of this class, the state components PossibleC and NecessaryC will be updated appropriately, in order that these state invariants remain valid. PossibleC and NecessaryC are ancillary components of the class DB and do not constrain the applicability or otherwise of any of the events associated with DB. Hence the static proof obligations tell us nothing about whether or not the properties of viable are reasonable in any sense. We have presented some examples of the way in which rules should be treated, but to gain confidence that our intuition is reasonable we have compared our method with some already existing definitions of how extensions should be built from a theory. We discuss one such comparison in the next section.

## 6. Characterisation of "viable" extensions in terms of default logic

The applicability of a rule used in generating a “viable” extension may be dependent on the absence of information. As a consequence, as new information becomes available, although some new rules may be triggered, the applicability of previously valid rules may be blocked. This non-monotonic character is captured by a number of non-standard logics $[18]$ which seem to model belief revision quite effectively $[11]$ .

One such non-standard logic is Reiter's Default Logic [15]. In Reiter's logic, a first order theory W is augmented by a set D of default rules of the form $[\alpha: \beta_{1}, \ldots, \beta_{n}/\gamma]$ , where $\alpha, \beta_{1}, \ldots, \beta_{n}, \gamma$ are formulae in the given language L. This rule may be read: "If the prerequisite $\alpha$ is true, so long as it is consistent to believe $\beta_{1}, \ldots, \beta_{n}$ , one may conclude $\gamma$ ". In order to relate the intuition behind our construction of "viable" extensions to existing work, it is of interest to note that we may translate the set of facts and the rule set (theory T) into an equivalent default theory $\Delta = (\mathrm{D}, \mathrm{W})$ as follows.

Our rules are of the form:

$$
\mathrm{P} _ {1} \wedge \dots \wedge \mathrm{P} _ {\mathrm{m}} \wedge \neg \mathrm{N} _ {1} \wedge \dots \wedge \mathrm{N} _ {\mathrm{n}} \Rightarrow \mathrm{C}.
$$

Denote W as the set of positive clauses (the set of facts unioned with those rules for which n = 0). D is the set of defaults obtained as follows.

For every clause $P_{1} \wedge \ldots \wedge P_{m} \wedge \neg N_{1} \wedge \ldots \wedge \neg N_{n} \Rightarrow C$ s.t. n > 0, include in D the default rule: $\left[(P_{1} \wedge \ldots \wedge P_{m}): \neg N_{1}, \ldots, \neg N_{n}/C\right]$ .

Then a “viable” extension of the theory T is equivalent to an extension of the default theory $\Delta$ . The proof of this assertion is quite straightforward and we do not include it here.

The same translation scheme is used by Bidoit and Froidevaux to associate a (prioritised) default theory with, in their case, a stratified logic program P. In their case, the restriction to a stratified logic program ensures that the associated default theory has exactly one extension $[1,14]$ .

Our preference is to consider the possibility of alternative scenarios.

## 7. A prolog implementation of the construction of "viable" extensions

In its most general form, the specification will be very hard to implement efficiently. In this section, we will present an equivalent specification which can at least be used as the basis for a Prolog “animation”.

The original definition of viable is non-constructive; the viable extension itself is used to check the validity of each rule application (N ∩ Consequences = ∅). Rather than generate possible extensions and test if they are viable, it would be preferable to constrain the successive rule applications used in the sequence 'J' so that they can be used to construct a viable extension without it already existing. The original definition of a "viable" extension can be modified by including an additional sequence R which stores the negative antecedents of rules as they are applied. When a rule is used to construct a successor set in the sequence J, we now say that its negative antecedents should not already be known, and should not become known. The negative antecedents are accumulated in a set in the sequence R, and no rule will subsequently be applied which will alter the status of the negative antecedents of a previously applied rule (C∉R(i + 1)). This is expressed in the predicate "viable2" which is equivalent to "viable" (the proof of this is relatively straightforward, and can be found in [6]), and is defined in Schemas 9 and 10.

It is very straightforward to produce a Prolog programme which is a correct implementation of this definition $[6]$ . However, this is still not an ideal solution. The term ‘non-constructive’ was applied to the original definition of viable because the defining sequence J required the presence of an ‘oracle’; reference was made to the resulting extension in each step in the sequence. The defining sequence of this equivalent definition does not require the presence of an oracle. The construction of each successive member of the defining sequence only refers to the results of the previous constructions. However, it is not a proper constructive definition because once the sequence is complete a check must be made to see if the resulting set of propositions is indeed an extension of the theory. Some constructions may fail this test. Consequently, this test is an ‘almost constructive’ definition because we do not know whether or not the result of the construction is indeed an extension until after it has been constructed.

In practical terms, this means that the prolog implementation may have to backtrack after constructing an extension, and try a different sequence of rule applications before it succeeds in building an extension which passes the final test:

$$
(\neg \exists (\mathrm{P}, \mathrm{N}, \mathrm{C}) \in \text { RuleSet }
$$

·deducible(Consequences,P,N,C)).

In fact unless we make some further restrictions on the sets of rules we wish to consider, this

```txt
viable2(Facts, Consequences, RuleSet) ≡
(∃J: seq set(DATA) ·
∃R: seq set(DATA) ·
    head J = Facts
    ∧ last J = Consequences
    ∧ head R = ∅
    ∧ ∀i < #J · ∃C:DATA ·
    J(i + 1) = J(i) ∪ {C}
    ∧ deducible(J(i), P, N, C)
    ∧ R(i + 1) = R(i) ∪ N
    ∧ C∉R(i + 1))
∧
(¬∃(P, N, C) ∈ RuleSet · deducible(Consequences, P, N, C))
```

```txt
deducible(K,P,N,C) ≡
(P,N,C) ∈ RuleSet
∧ P ⊆ K
∧ C∉ K
∧ N ∩ K = ∅.
```

## Schema 10

would appear to be the best that can be done. This definition can be generalised to produce an almost constructive definition of a default extension (as defined by Reiter), and it has been shown [13] that of all the currently known definitions, this one produces the fewest number of pre-extensions ('false tries').

## 8. Discussion

We have presented an abstract specification of a database extension management system. There is no requirement that the extension(s) be explicitly maintained in order to satisfy the specification. The specification may be refined into a deductive database (the semantics of the first order version being equivalent to the stable model semantics $[5]$ of general logic programs $[22]$ ), or equally into a truth maintenance system (with default logic based semantics).

The next stage is to refine the specification into an implementation. We have demonstrated a first stage in the generation of a prototype implementation. This generated (almost by accident) a result which was of interest to the default logic community. However, the main point to be made here is that a formal statement of an aspect of the complete system enabled us to link in our requirements with a body of existing theoretical work (see, for example, [14]). This could then be used to inform the further refinement of the specification.

The concentration on the inference engine rather than the knowledge base itself has been quite deliberate. There is an expanding body of work on the validation, verification and test of knowledge based systems $[10]$ . But for this work to be of value, one must be able to rely on the integrity of the underlying inference engine. Without this assurance, it would not be possible to be confident that any errors detected in the test cycle were actually a reflection on the integrity of the rule set, rather than that of the inference engine. However, we do also believe that more formal approaches to specification are applicable to many aspects of knowledge-based system development [8]. Indeed, this belief is also reflected in current developments in the KADS methodology for KBS construction [21].

Clearly, formal studies can be taken to an almost arbitrary depth. We have tried to demonstrate that a clear logical statement of the problem provides a minimal level which can then be linked in, if necessary, with deeper analyses where available. We seriously believe that formal approaches do have a valuable contribution to make to the development of knowledge-based decision support system development, and hope that this paper may go some way to encourage their wider application.

## Acknowledgments

P. Krause is supported under SERC project number 1822. We gratefully acknowledge colleagues involved in ESPRIT Basic Research Action 3085 for many helpful discussions, and also John Fox for helpful comments on an earlier draft.

## Appendix: glossary.

We assume the reader is familiar with the usual logical connectives $(\wedge, \vee, \neg, \Rightarrow)$ , and the set theoretic constructs $(\cup, \cap, \subseteq, \in)$ . Some additional notation is used in the specifications which follows that of the $Z$ language. [20] includes a complete glossary of the $Z$ notation; the following are informal definitions of the additional constructs used here.

S: set(T) $\hat{=}$ S is a set of elements of type T.

S: seq(T) $\triangleq$ S is a sequence of elements of type T.

head S $\triangleq$ the first element in the sequence S.

last S $\triangleq$ the last element in the sequence S.

S(i) $\hat{=}$ the 'i'th element of the sequence S, where i = 1, ... #S.

#S ≡ the number of elements in the sequence S.

$\varnothing$ $\hat{=}$ the empty set.

## References

[1] N. Bidoit and C. Froidevaux, Minimalism Subsumes Default Logic and Circumscription in Stratified Logic Programming, in: Proceedings of Logic in Computer Science (LICS-87), 89–97, (IEEE, New York, 1987).

[2] D.W. Etherington, Reasoning with Incomplete Information (Pitman, 1988).

[3] J. Fox, D.A. Clark, A.J. Glowinski, M.J. O'Neil, Using predicate logic to integrate qualitative reasoning and classical decision theory, IEEE Trans. on Systems Man. and Cybernetics, 20, no. 2, 347–357 (1990).

[4] J. Fox, A.J. Glowinski, C. Gordon, S. Hajnal, M.J. O'Neil, Logic engineering for knowledge engineering: Design and implementation of the Oxford System of Medicine, Artificial Intelligence in Medicine, 2, no. 6, 323–339 (1990).

[5] M. Gelfond and V. Lifschitz, The stable model semantics for logic programming, in: Proc. 1988 Conference and Symposium on Logic Programming, Seattle Washington, 1070–1080 (1988).

[6] P.J. Krause, P.J. Byers, S.J. Hajnal and J. Cozens, The Formal Specification of a Database Extension Management System, Biomedical Computing Unit Report TR 116, Imperial Cancer Research Fund (1990).

[7] P.J. Krause, J. Fox, M. O'Neil and A.J. Glowinski, Can We Formally Specify a Medical Decision Support System?, IEEE Expert, 8, no. 3, 56–61 (1993).

[8] P.J. Krause and A.J. Glowinski, Formal Specifications and Medical Decision Support Systems, Applied Artificial Intelligence, 7, 237–256 (1993).

[9] P.J. Krause and D.A. Clark, Representing Uncertain Knowledge; an AI Perspective, (Intellect Books, Oxford, 1993).

[10] J. Liebowitz, Ed., Special Issue: Verification and Validation of Knowledge Based Systems, Expert Systems with Applications, 1(3) (1990).

[11] D. Makinson and P. Gardenfors, Relations between the

logic of theory change and nonmonotonic logic, in: A. Fuhrman and M. Morreau, Eds, Proceedings of the Konstanz workshop on belief revision (Springer-Verlag, 1990).

[12] V. Mital and L. Johnson, Structuring financial expert systems to defend against negligence, in: T.R. Addis and R.M. Muir, Eds, Research and Development in Expert Systems VII, 171–182 (Cambridge University Press, 1990).

[13] Y. Moinard, Unifying various approaches to default logic, in: Proceedings of IPMU '92, Palma de Mallorca, Spain. 61–64 (1992).

[14] T.C. Przymusinski, Non-monotonic reasoning versus logic programming: a new perspective, in: D. Partridge and Y. Wilks, Eds, The foundations of artificial intelligence: A sourcebook, 47–71 (Cambridge University Press, 1990).

[15] R. Reiter, A Logic for Default Reasoning, Artificial Intelligence 13, 81–132 (1980).

[16] S.A. Schuman and D.H. Pitt, Object-Oriented Subsystem Specification, in: Meertens, Ed., Program Specification and Transformation, 313–342 (North-Holland, 1987).

[17] S.A. Schuman, D.H. Pitt and P.J. Byers, Object-Oriented Process Specification, Computing Science Technical Report, University of Surrey (1989).

[18] P. Smets, E.H. Mamdani, D. Dubois H. Prade, Eds., Non-Standard Logics for Automated Reasoning (Academic Press, 1988).

[19] J.M. Spivey, Understanding Z: a Specification Language and its Formal Semantics (Cambridge University Press, 1988).

[20] J.M. Spivey, The Z Notation. A Reference Manual (Prentice Hall International, 1988).

[21] F. van Harmelen and J. Balder, (ML) $^{2}$ : A formal language for KADS models of expertise, Knowledge Acquisition 4, 127–161 (1992).

[22] M. Wallace, ECRC, Personal Communication (1990).

[23] J.B. Wordsworth, Specification and refinement using Z and the guarded command language: a compendium, Technical Report, IBM United Kingdom Laboratories (1988).

---
otero_id: 17024
otero_key: "X3JYXE5P"
title: "A logic model for electronic contracting"
authors: "Ronald M. Lee"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90096-6"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Logic Model for Electronic Contracting $^{1}$

Ronald M. LEE

Management Science and Information Systems, CBA 5.202, Graduate School of Business, University of Texas, Austin, TX 78712, USA

Contracting is an essential aspect of doing business. Electronic contracting uses telecommunications and artificial intelligence to improve contracting processes by streamlining red tape, enforcing legal correctness. To do this, the underlying conceptual structures of contracts and contracting must be carefully understood. A logic model is presented that emphasizes temporal, deontic and performative aspects of contracting.

Keywords: Logic Modeling, Contracts, Temporal Logic, Deontic Logic, Electronic Contracting.

![](/api/attachments/X3JYXE5P/fulltext/images/d00063be911b50a62ac48e9fd982468b2b01b1583b022cc49dd0e6ad6f612d38.jpg)

Ronald M. Lee is presently of the Information Systems Group in the Management Science and Information Systems Department at the University of Texas. Previously, he was a member of the faculty at Washington University, St. Louis, a research scholar at the International Institute of Applied Systems Analysis (IIASA) in Vienna, Austria and visiting professor at the New University of Lisbon, Portugal. He has a doctorate in Decision Sciences from the Wharton School, University of Pennsylvania. Research interests focus on logic modeling methods and their application to macro-level administrative systems, including electronic markets, electronic contracting networks, and bureaucratic systems.

## 1. Introduction: Electronic Contracting

Contracting is one of the most fundamental concepts of Western economics. Essentially, a contract is a generalization of the notion of direct exchange that provides for cross-temporal transactions, allowing one party to offer goods or services at one time in exchange for other goods or services at another time. $^{2}$ In doing so, an enormous gain in flexibility is achieved. In contrast to a direct exchange market, for instance a farmers market, contracting parties are able to negotiate arrangements that are far more complex and specialized to the particular needs of the parties involved [Williamson (1975, 1979)].

On the other hand, contracting is constrained by the communications technology it uses. Today, despite the availability of instantaneous and worldwide electronic communications (phone, telex, electronic mail), contracts are still recorded mostly in the medium of paper documents. A principal reason for this is to provide evidence for the terms and conditions of the original agreement. Electronic records can often be altered without leaving a trace. The hard copy evidence of paper – carefully typed, signed and notarized to make it easy to distinguish the original version – is still preferred.

Another key characteristic of contract communications is the language used. For a contract to be effective in governing the obligatory actions of the parties, it is desirable that the expression of contract terms be clear and unambiguous. Unfortunately, there is no guarantee that what one party intended by a certain phrase is what the other party understood by it. For this reason, much of the terminology used in contracting is given specific interpretation by the law.

Closely related to the language of contracting are the procedures for communicating. It is very important when something is in fact, said. For instance, one party may make numerous drafts of a contractual offer, without committing to any of them. These might even be discussed with the other party. However, it is only when the offer is delivered in a certain (conventional) way, does it become binding. Similarly, only if the acceptance of the other party is conveyed in a given fashion that it actually creates a contract. Like the language for contracting, these conventions for 'saying' may be misunderstood by the parties. Furthermore, the conventions may vary depending on the type of exchange involved. Again it is the responsibility of the law to interpret and disambiguate these procedures.

Whereas precision of language and careful specification of procedures help to reduce the potential confusion and disagreement in contracting, they also add greatly to the overhead. An apparently straight forward arrangement, may become lengthy and complex to work out in all its contingencies and details. This adds not only to the cost, but also the time involved for contracting. For this reason, certain types of contracts have been standardized and streamlined to make them more efficient to negotiate. Examples are commodities contracts, used by organized exchanges such as the Chicago Board of Trade. Also helping to reduce contracting overhead, the Uniform Commercial Code (UCC) provides default provisions and standardized interpretations for common terms for contracts involving sales of goods within the U.S.

In this paper, we consider how contracting processes might be further improved through computer support. Clearly, telecommunications and database management could be – and are – put to use to speed communications and facilitate storage and retrieval. Our focus is however on the language and formal procedures of contracting, and how the technology might be employed for the further standardization of certain classes of contracts in order to further reduce the transactions costs and time of contracting. We refer to this as ‘electronic contracting’. The strategy is based on an analogy between legal standardization (such as the UCC) and logical formalization. Both are concerned with prescribing precise interpretations to certain types of statements. In law, however, this is done within the framework of natural language, whereas in logic specialized symbolism is introduced. Our point is that through the mediation of the computer, these two approaches can be effectively integrated.

## 2. Motivation for a Logic Model of Contracts

Currently, contracts may be represented electronically in one of two ways – as records in a database, or as a text file. The database approach provides powerful search and retrieval mechanisms, but is limiting it its expressiveness. By contrast, text files, prepared using word processing, can be arbitrarily expressive, but offer no means for retrieval or inferencing. The approach proposed here is a third alternative: to express contract terms and conditions using a formal language. $^{3}$

By a formal language, we means a language having an explicit set of primitive vocabulary, plus explicit grammar rules for combining this vocabulary to form more complex expressions, as well as explicit inferencing mechanisms for reasoning about these expressions. A familiar example of formal languages are programming languages, where the expressions are imperative statements to the computer. Other examples are logical languages, e.g., predicate calculus, where the expressions are declarative expressions about some subject area. In other formal languages, the grammar may be graphical, e.g., semantic nets and Petri nets.

The kind of formal language we have in mind for specifying contracts is one based on predicate logic. In essence it is more like a complex data structure than a computer language; that is, while it is interpretable computationally, it does not contain commands for the computer. Rather, it specifies the obligations of the parties to the contract. Unlike data structures, which are used primarily for retrieval purposes, this logical representation will also support inferencing about contracts. For instance, it can be used to determine if a contract is incomplete or if it has contradictory conditions. It can be used in a 'what if' mode to evaluate its effects under hypothetical circumstances, and it can be linked to a database of actual events to track the actual progression of obligations.

This strategy offers both expressiveness and inferential capabilities. The cost, however, is a substantial increase in notational complexity. The predicate logic needed to cover this domain is at least as complicated as a conventional programming language, and users – lawyers, contractors – would need to have comparable training in order to use it effectively. However, unlike programming languages, which refer to (otherwise unfamiliar) machine operations, the domain of reference in contracting is well known to its users, i.e., contract terms and conditions. This fact can be used to help minimize the obscurity of the notation and reduce the training overhead.

This has to do with the nature of the relationship between natural and formal languages. We often associate this with differences in syntax. The axiomatic expressions of predicate logic, for instance, often look much different than their natural language readings. On the other hand, this is mainly a convenience of abbreviation. For example, the predicate logic expression ‘D(J, G)& P(S, M) → C(T)’ is syntactically equivalent to ‘if Jones delivers goods and Smith pays money then contract terminated’. The second expression looks like natural language but is actually as formal and computable as the first. The more fundamental difference between natural and formal languages is the way they are controlled. In a formal language, the basic vocabulary has a fixed interpretation, while the formation of expressions and the inferences drawn from them are controlled by explicit, mechanical rules. In natural language, by contrast, the interpretation of terms, the grammar, and the reasoning conventions are implicit. Often these may be understood differently by the parties involved, leading to misunderstandings and disagreements. In contracting, such misunderstandings can be very costly, necessitating prolonged arbitration or litigation to resolve them. For this reason legal language, so-call ‘legalese’, makes a considerable effort to avoid ambiguities, and to elucidate terms and conditions as clearly and completely as possible.

The logical notation proposed here shares these same objectives, but carries the process of formalization further to the point where the language can be interpreted computationally. There is however no need to burden the user unnecessarily with formal syntax. An external syntax, consisting of a restricted form of legal English, is provided, that parses into the logical form. A definite clause grammar is used for this purpose.

Our criteria for a logical representation of contracting are based on the notion of a contract as a device for specifying and securing cross-temporal transactions. In its temporal aspects, a contract is much like a plan in that it specifies a (possibly contingent) series of activities, some of which are to be performed sequentially, others which may be performed concurrently. An example is a construction contract, where the sequence of activities to be performed by the contractor is specified. Contracts differ from plans in that (promises between) multiple agents are involved, i.e., the contracting paries. $^{4}$ Thus the performance of one party's activity, e.g., a payment, may be contingent on the other party's completion of another activity, e.g., some stage of the construction.

The analogy of contracts to plans is useful in that various planning tools may be applied to the modeling of contracts. A PERT diagram, for instance, is effective for capturing the relative timing of activities arranged sequentially and concurrently. A decision tree is useful for modeling contingency or choice between activities. A Petri net combines the features of PERT and decision trees in representing sequence/concurrency and choice in a common formalism.

Logic, however, may seem less well suited for these applications in that it is normally used for modeling static relationships. However, various non-standard logics have been developed for modeling dynamic environments. For instance, tense logics, used to describe the temporal aspects of natural language verb tenses, were discussed in Kimbrough and Lee (1987) in this issue. Here, we make use of a different kind of logic, a 'logic of change', to capture the sequencing of contracting activities. The value of a logic representation for this purpose is that it can more effectively integrate other features of interest in contracting. However, the visual clarity of graphical techniques is also valuable. For this reason, we make use of a Petri net notation, which is then translated into a logical form.

In addition to the relative timing of activities, contracts also make reference to absolute times in the form of deadlines. For these purposes, a temporal logic that provides operators for associating activities with specific points in time is incorporated.

Normally, the main purpose of planning is to provide adequate lead time for interdependent activities while minimizing the overall duration of the project. With contracts, by contrast, the main goal is to guarantee performance. Contracts therefore have an additional aspect not found in plans, namely, obligation. Within the logic literature, obligation, along with the related concepts of permission and prohibition, have been studied as another form of non-standard logic known as deontic logic. This provides another important component in the modeling of contracts.

In addition to the logical specification of contracts themselves, electronic contracting also needs to include the procedures by which contracts are made. Again, these procedures involve temporal relationships analogous to plans. However, the actions performed in negotiating a contract are mainly linguistic – as opposed to physical – actions. For instance, one party may make a formal offer, which the other party accepts. While these actions may include the transfer of physical paper documents, their primary effect is linguistic. Indeed, it is this aspect that makes electronic contracting feasible. However, these types of linguistic actions are more than data transfers. The act of communicating in these cases is in itself meaningful, e.g., resulting in the commencement of an obligation. That is to say, contracting involves communications that are not only informative, but also performative. $^{5}$ Various classes of performative communications have been studied within linguistics and philosophy. Whereas the usual goal in this work is to model the changes in social relationships occurring in a wide range of human discourse, the types of performatives used in contracting are much more restricted.

In the discussion to follow, each of these logics pertaining to the specification of contracts and contracting processes is examined in more detail. However, a fully integrated axiomatization of these different logics is beyond our scope at present. Rather, we take on the more modest goal of integrating these aspects in a logic programming formulation that demonstrates their relevance and usefulness for electronic contracting in the form of an operating prototype. This may be regarded as a special purpose axiomatization, which could eventually lead to a more general theory.

## 3. Temporal Aspects: Relative Time

Contracts specify one or more actions to be performed by the contracting parties. In some contracts, a sequence of actions is stipulated, for example, periodic payments on a lease. In other cases, concurrent actions are involved, such as in construction contracts. In still others, certain actions may be contingent on the occurrence of a natural event, for instance fire insurance, or contingent on the performance of the other party, as in option contracts. The promissory aspect of contracts is yet another form of contingency, for instance the penalties incurred when a deadline is not met. These temporal relationships are key to a logic of contracts, to deduce who is to do what, when (and what happens if they do not).

## 3.1. Petri Net Notation

A convenient way to model this variety of temporal relationships is to use Petri nets diagrams. $^{6}$ A Petri Net is a graph representation having two types of nodes. So-called ‘place’ nodes indicate states or sub-states of the system, and are drawn as circles. The other type is ‘transition’ nodes, drawn as a vertical bar. A Petri Net is a directed graph having these two node types in alternation. The interpretation is that the various activities in the system are modeled as places (sub-states). Transition nodes mark the transition from one set of activities to another. $^{7}$ A simple contract where $X$ does $A$ and iY does $B$ is modeled as shown in fig. 1.

![](/api/attachments/X3JYXE5P/fulltext/images/b6e107135cfb53892d0e613dc46c26af70c2fbc60fad9a19a2f4e1c0679493f4.jpg)  
Fig. 1. Example Contract in Petri Net Notation.

The events and actions of the contract are specified as attributes of transitions. In the example, control goes from 'start' to transition 1, which initiates two parallel activities, S1 and S2. Transition 2 fires when the action X: A is accomplished, and goes to a wait state, S3. Similarly, transition 3 fires when the action Y: B is accomplished, and goes to wait state S4. When the two actions have both been achieved, transition 4 fires and the 'finish' state is reached.

## 3.2. A Logic of Change

Conventional proposition or predicate logic is usually applied to model static situations. However, various extended forms have been proposed to capture dynamic aspects. One of these is the 'logic of change' of von Wright (1965). We use this as a basic for modeling relative time relationships in logic. The basic device in von Wright's approach is a new logical connective, T, which he describes as a kind of asymmetrical conjunction $^{8}$

## p T q

is read $p$ 'and next' $q$ , where $p$ and $q$ are propositions. The connective $T$ is 'forward looking', that is, p T q indicates that q is the state to follow the present state, p. Thus

$$
(p \mathrm{T} q) \rightarrow p
$$

is a theorem (p. 297). Von Wright generalizes this to consider a system whose basic features are characterized by a finite set of elementary propositions, $p1, \ldots, pn$ . An elementary literal is an elementary proposition or its negation. A state of the system is then a conjunction of elementary literals, resulting in $2n$ state descriptions, denoted as $s1, \ldots, s2n$ . A scenario might then be characterized as a sequence of state descriptions connected by T, e.g.

## s1 T s2 T s3 T...

Next consider that a transition from one state to the next might be indeterminate, e.g.

$$
\mathbf {T} (s j \vee s k)
$$

Note that this is effectively an exclusive disjunction, since the conjunct of two different state descriptions would yield a contradiction (i.e., at least one proposition in one is a negation of that in the other). In this fashion, von Wright's T calculus may be used to give a logical representation for a state-transition diagram. These are usually depicted graphically, for instance, as shown in fig. 2. Fig. 2 is expressed in the T calculus as s1 T ((s2 T s4) ∨ (s3 T (s4 ∨ a5))).

A state-transition diagram models transitions from one complete system state to another. Branching in the diagram represents a choice between target states. A Petri net is a generalization that in addition represents concurrency. In this case, the concept of a state is relaxed so that it no longer includes the full set of elementary propositions or their negations, but rather only a subset. We refer to this revised notion as a 'substrate'. Thus a substate is also a conjunct of elementary literals. Note however that it is now plausible for two substates to occur simultaneously. This has the effect of re-introducing conjunction in the T expressions.

![](/api/attachments/X3JYXE5P/fulltext/images/b90292c6efd7822491179e8a1a2a3c1ce9fda5b95bdaa20283275a250e5eacbf.jpg)  
Fig. 2. Example State-Transition Diagram.

A logical interpretation for Petri nets can now be stated:

\- place nodes in the PN correspond to substates in the T calculus,

\- transition nodes in the PN correspond to uses of the T connective in the T calculus,

\- arcs branching out of a place node correspond to disjunction in the T calculus,

\- arcs branching out of a transition node correspond to conjunction in the T calculus.

## 3.3. Logic Programming Formulation

Logic programming implements a restrict form of first order predicate logic, i.e., Horn clauses of the form

$$
\psi 0: - \psi 1, \psi 2, \dots , \psi n, \quad n \geqslant 1,
$$

where each $\psi i$ is a first order predicate, ‘:-’ is left implication (“if”), and commas are conjunction. The reading is ‘to prove $\psi 0$ it is sufficient to prove $\psi 1$ and $\psi 2$ and...and $\psi n$ . Variables are implicitly quantified universally on the left. Variables are written beginning with uppercase, whereas constants are in lower case, are numerals, or are special symbols (punctuation marks, etc).

Since the logical connectives are fixed in this clausal form, we are not at liberty to add new connectives as von Wright proposes. Logic programming does however provide great flexibility in the types of individuals that can be described. In particular, these can be ‘structures’ containing embedded parameters. We utilize this to represent the notion of a substate discussed above. Each substate is represented in the form

$$
\mathbf {s} (\mathbf {N}, \mathbf {T}),
$$

where N = substate name, T = time when substate is completed.

As a plan for a future sequence of events, the parameter T will normally be an unbound variable. In the implementation, it is used to track the history of an actual or hypothetical scenario.

A conjunction of substates will be represented as a list of the form

$$
[ \mathrm{A} 1, \dots , \mathrm{Am} ].
$$

This can be used to define more complex substates or to provide a complete state description. In using this representation, we make the assumption that each substate description is mutually exclusive in the set of elementary propositions it contains. Thus a conjunct of substates will never define a contradictory state of affairs.

Corresponding to von Wright's T connective, we introduce the predicate, 'trans':

$$
\operatorname{trans} ([ \mathrm{A1}, \dots , \mathrm{Am} ], [ \mathrm{B1}, \dots , \mathrm{Bn} ], \text { Event }).
$$

This indicates a transition from the substate A1,...,Am, the precondition of the transition, to the substate, B1,...,Bn, the postcondition. There will be one such ‘trans’ assertion for each transition node in the Petri net. Not present in von Wright’s formulation, we add an additional parameter, ‘Event’. This is an event or action taken by one of the contracting parties that causes the transition to another substate in the contract. (In Petri net terminology, the enabling condition for the transition to ‘fire’.) The earlier Petri net graph, where party X is to do action A concurrently with party Y’s doing action B is specified by the following ‘trans’ assertions:

$$
\operatorname{trans} ([ \mathrm{s} (\text { start }, \mathrm{T0}) ], [ \mathrm{s} (1, \mathrm{T1}), \mathrm{s} (2, \mathrm{T2}) ], \text { true }),
$$

$$
\operatorname{trans} ([ \mathrm{s} (1, \mathrm{T} 1) ], [ \mathrm{s} (3, \mathrm{T} 3) ], \mathrm{X}: \mathrm{A}),
$$

$$
\operatorname{trans} ([ \mathrm{s} (2, \mathrm{T} 2) ], [ \mathrm{s} (4, \mathrm{T} 4) ], \mathrm{Y}: \mathrm{B}),
$$

$\operatorname{trans}(\mathbf{s}(3, \mathbf{T}3), \mathbf{s}(4, \mathbf{T}4)], [\mathbf{s}(\text{finish}, \mathbf{T}5)], \text{true})$ .

State names may be descriptive, e.g. 'start', 'finish', or else arbitrary integers, e.g., 1, 2. Also, if a transition is automatic, having no conditions, the predicate 'true' is used.

The processing of a Petri net using these 'trans' assertions is not unlike that for discrete event simulations. An overall system state list is maintained as a list of substates. When a transition is enabled, the input substates (preconditions) are removed from the state list, and the output substates (postconditions) are added to it. A basic algorithm is as follows:

bump(L0, LL):-

trans(SL0, SL1, Conds),

remove(SL0, L0, L1),

call(Conds),

append(SL1, L1, L2),

bump(L2, LL).

bump(L, L).

Here, L0 is the starting state list for the Petri net, and LL is the final state list. The purpose of each call of the 'bump' predicate is to evaluate a single transition. It first finds a 'trans' assertion and attempts to remove its precondition substate list (SL0) from the current system state list (L0), giving list L1. It then tests if the enabling condition (event) for this transition is true ('call'). If this succeeds, the output substate list for the transition is appended to the system state list, and 'bump' is invoked again recursively. If a particular 'trans' assertion fails in the remove (failure of preconditions) or fails in the evaluation of the enabling event, the system backtracks to try another 'trans' assertion. If no 'trans' assertions succeeds, control falls through to the boundary condition, and the input system state list becomes the final state list.

## 4. Temporal Aspects: Absolute Time

## 4.1. The RU Calculus

Petri nets, and correspondingly, the T calculus, are useful for describing relative relationships in time, that is whether one activity is to follow another, is concurrent with it, or whether certain activities are chosen in lieu of others. However, another aspect needed for modeling contracts is how actions of the various parties are fixed in an absolute time framework, e.g., the meeting of a deadline. For this, some additional logical constructs are needed.

An approach to this is the temporal logic system of Rescher and Urquhart (1971), which we will call the RU calculus. This is based on the use of a temporal operator, $R_{t}\phi$ , read that $\phi$ is ‘realized’ at time, t. Here $\phi$ is presumed to be a formula in conventional first order logic with identity. Basic axioms for their system are as follows ( $t, t', t''$ are time points):

$$
\mathrm{RU1.} R _ {t} (\sim \phi) \leftrightarrow \sim R _ {t} \phi .
$$

Comment: the R operator is interchangeable with negation.

$$
\mathbf {R U 2 .} R _ {i} (\phi \& \psi) \leftrightarrow R _ {i} \phi \& R _ {i} \psi .
$$

Comment: the R operator distributes across conjunction. Note that axioms RU1 and RU2 taken together provide that the R operator is distributable over all the propositional connectives.

$$
\mathrm{RU3.} R _ {t ^ {\prime}} (\forall t \phi) \leftrightarrow \forall t R _ {t ^ {\prime}} \phi .
$$

Comment: the R operator is interchangeable with universal quantification (providing t and $t'$ are distinct). The basic system is extended by adding an ordering relation on times, denoted $Utt'$ indicating that time t precedes time $t'$ . This is a total ordering, hence irreflexive, asymmetric, transitive and complete. This permits a mapping, f, to the real number line, such that a notion of temporal addition, $\oplus$ , can be defined in terms of arithmetic addition, i.e.

$$
f (t \oplus t ^ {\prime}) = f (t) + f (t ^ {\prime}).
$$

This notion of temporal addition forms a commutative group, hence commutative and associative, with identity and inverse.

## 4.2. Re-interpretation of RU for Contracting

The advantage of the RU calculus is that it provides absolute time references. However, as presented, it is too mathematical for business applications. A basic difficulty is that it regards time as constituting a ratio scale, having a natural zero or origin point. This permits the view of time values both in terms of absolute position on the time line as well as measures of interval length along that line. This is not true of ordinary discourse about time in business. Rather than a real number line, the (Gregorian) calendar is the usual reference framework. In this, though the birth of Christ might be considered as a zero point, it is not a real origin, as presumed in a ratio scale. Rather, it is like the zero on the Centigrade or Fahrenheit scales for temperature. Just as these do not represent zero temperature, nor does the year 0 A.D. represent zero time. Calendar time is thus an interval scale rather than a ratio scale. Furthermore, the calendar has been broken up into other intervals, months and years, with the result that the language for absolute time position is somewhat different than the language for interval duration. $^{9}$ We now consider how the RU calculus might be adapted for these considerations. To begin, we note that the business view of time does not disagree with the underlying ontology of RU; time is still conceptualized as a dense linear ordering of points. The difference is more in the units of reference. In business, this is most commonly a calendar date, which we will adopt as a basic unit. To distinguish days (and other time intervals) from time points, we use the notation d, d', d'', etc. In order to refer to time intervals of greater length, we use the notation

## $\mathbf{SPAN}(d, d')$

indicating the time span from the beginning of date d to the end of date $d'$ . We next need to indicate how basic temporal assertions are to be expressed. For this, we introduce two additional temporal operators: $Rd_{d}\phi$ , that $\phi$ is ‘realized during’ the time interval d; and $RT_{d}\phi$ , that $\phi$ is ‘realized throughout’ time interval $\phi$ . The definitions are as follows:

$$
R D _ {d} \phi \leftrightarrow \exists (t \in d) \& R _ {t} \phi .
$$

Reading: $\phi$ is realized during interval d if and only if for some time point t in d, $\phi$ is realized at t.

$$
R T _ {d} \phi \leftrightarrow \forall t (t \in d) \rightarrow R _ {t} \phi .
$$

Reading: $\phi$ is realized throughout interval d if and only if for every time point t in d, $\phi$ is realized at t.

We also need corresponding notions for temporal ordering and temporal addition. Though a temporal ordering would be simple if the only time units were calendar dates, this becomes overly cumbersome when longer and possibly overlapping time intervals are included. Rather, we consider various time points as the end points of time intervals, given by the functions:

$$
\operatorname{BEG} (d) = \text {   beginning   point   of   interval   } d,
$$

END(d) = ending point of interval d.

Since these refer to time points, the ordering predicate, $Utt'$ , applies here as well. For this, however, we use the more suggestive notation

$$
t. <  . t ^ {\prime}
$$

to indicate that time point t precedes time point $t'$ . More difficult is the notion of temporal addition. As noted earlier, we cannot simply add calendar dates (or even time points) since the calendar has no essential origin point, and hence is an interval rather than a ratio scale. We therefore need to redefine the RU notation of temporal addition. For simplicity, we consider only one type of interval measure, an integer multiple of days, ignoring other units such as months and years. The notation is as follows:

## $d\oplus nD.$

where D is a functional constant indicating a one day interval, n is an integer or an integer expression. Intuitively, this refers to the date n days hence from date, d.

## 4.3. Logic Programming Formulation

We now adapt the preceding discussion to a logic programming notation, and indicate its role in the broader model for electronic contracting. (Recall that in logic programming notation, the logic convention is reversed so that variables are in upper case and constants are lower case.)

As discussed above, the granularity of time reference used here is at the level of calendar days. The notation is DD-MMM-19YY where DD = integer (1–31), MMM = three letter abbreviation for month (jan, ..., dec). 19YY = integer year. For instance, 27-jun-1987 is June 27, 1987. (The '-' is a Prolog operator, the same as used in arithmetic expressions. In this context it is not evaluated however.)

The notation for temporal precedence is the following:

D0. = .D1, date D0 equals date D1,

D0. < .D1, date D0 precedes date D1,

D0. <= .D1, date D0 precedes or equals date D1,

D0. > .D1 date D0 follows date D1,

D0. $> = .\mathbf{D}1$ , date D0 follows or equals date D1,

D0. <> .D1, date D0 does not equal date D1.

The logic programming notation for the RD and RT operators is as follows:

rd(D): A,

$\mathbf{rt}(\mathbf{D})\colon \mathbf{A},$

indicating that even A was ‘realized during’ or ‘realized throughout’ date D, respectively. The time interval, D, need not be restricted to single dates. Longer time intervals may be specified using the construct

span(D0, D1)

which refers to the interval from the beginning of date D0 to the end of date D1.

Often, especially to stipulate deadlines, it is convenient to indicate that an event is to be 'realized before' the end of a given date. For this we use the abbreviated form

rb(D): A

instead of

rd(span(\_, D)): A.

Here the underscore indicates an unbound variable. Thus, rb(D): A is true if event A occurs within the time span beginning arbitrarily, and ending on date D.

Temporal arithmetic is included in a limited fashion. Time intervals may also be indicated using the notation

$\mathbf{D} + \mathbf{D}\mathbf{D},$

where S is a specific date and DD is of the form 1 day

K days

(these are postfix Prolog operators). For instance, rb(D + 30 days): A

indicates that event A occurs on or before the date

30 days hence from date D. In the contracting model, expressions formed using the 'rd', 'rt' and 'rb' operators are used to specify the enabling conditions of transitions ('trans' assertions). In doing this, an agency specification is added to indicate the party responsible for a given action. This has the form

X: rt(D): A = party X realizes event
A throughout period D,

X: rd(A): A = party X realizes event
A during period D,

X: rb(D): A = party X realizes event
A before the end of period D.

Example: Jones agrees to kennel Smith's dog, Fido, over the sumer, from June 1 through August 31, 1988. In return, Smith will pay jones \$100 by June 15. The Petri net structure is the same as in the earlier example, where X is Jones, A is kenneling Fido, Y is Smith, and B is the \$100 payment. The 'trans' assertions are

trans([S0], [S3], jones :

rt(span(1-jun-1988, 31-aug-1988)):

kennel(fido).

trans([S2], [S4], smith:

rb(15-jun-1988): pay(jones, \$100).

## 4.4. Facts, Deadlines, and Temporal Negation

Most of the time references in contracts have to do with deadlines, i.e., the time by which some event or action is to occur. Deadlines are tested by comparison to actual occurrences or facts. Facts are distinguished by the notation

fact(A),

where A = an event or action.

In reasoning about contracts, one is particularly concerned about when deadlines are met or not met. This involves a special form of negation we call ‘temporal negation’, denoted by the symbol, ‘\~’. For instance,

\~rb(D):A

indicates that deadline D has not been met.

Normally, in logic programming, negation is by failure, i.e., 'not P' is true if P cannot be proven. Temporal negation is a somewhat narrower concept. The absence of relevant facts is not by itself sufficient to show that a deadline has failed. If the deadline date has not yet been reached, the stipulated event or action may yet occur. Thus, the current time must also be considered. Indicating the current time as the predicate, 'time(T)', the temporal negation of an event to be realized before deadline D is defined as follows:

$$
\sim \operatorname{rb} (\mathbf {D}): \mathbf {A}: - \text { time } (\mathbf {T}),
$$

$$
\text { not   } \operatorname{fact} (\operatorname{rd} (D): A), T. >. D.
$$

$$
\operatorname{fact} (\operatorname{rd} (\mathbf {D 0}): \mathbf {A}), \mathrm{T}. >. \mathbf {D 0}, \mathbf {D 0}. >. \mathbf {D}.
$$

The first rule says that the deadline fails if there are no facts that A has occurred, and the current time is later than the deadline. The second rule says that the deadline also fails if action A occurred, but after the deadline date, and the current time is after the deadline. Analogous rules apply for actions and other forms of deadlines.

## 5. Deontic Aspects

## 5.1. Deontic Logic

Whereas temporal aspects are important in contracting, they are of course not the whole story. Another important feature is that the various actions do not simply occur, but rather they are obligatory. The nature of obligation has been studied in logic under the heading cf 'deontic logics', usually regarded as an applied form of modal logic. The first of these was proposed by von Wright (1968). As a basic concept, he introduced the operator

$O\phi,$

read that $\phi$ is obligatory. Based on this, a notion of permission can be defined as its logical dual

$$
P \phi \leftrightarrow \sim O \sim \phi .
$$

That is, to be permitted to $\phi$ is not to be obliged not to do it. A related concept of prohibition was defined as

$$
F \phi \leftrightarrow O \sim \phi .
$$

That is, $\phi$ is forbidden if it is obligatory not to do $\phi$ . Whereas variations of deontic logic continue to be proposed and debated, there is general agreement on the following ‘standard system’ of axioms [Folesdal and Hilpinen (1981)]

$$
\mathrm{D1.} O \phi \rightarrow \sim O \sim \phi .
$$

Reading: If $\phi$ is obligatory, then it is not forbidden.

$$
\mathrm{D2.} O (\phi \& \psi) \leftrightarrow O \phi \& O \psi .
$$

Reading: $\phi$ and $\psi$ are together obligatory if and only if they are obligatory separately.

$$
\mathbf {D 3 .} O (\phi \vee \sim \phi).
$$

Reading: It is obligatory to either do or not do $\phi$ . These axioms can be re-stated in terms of permission as follows:

$$
\mathbf {D 1} ^ {\prime}. P \phi \vee P \sim \phi .
$$

Reading: either A or not A is permitted.

$$
\mathrm{D} 2 ^ {\prime}. P (\phi \vee \psi) \leftrightarrow P \phi \vee F \psi .
$$

Reading: $\phi$ or $\psi$ is permitted if and only if either one of them is permitted.

$$
\mathrm{D} 3 ^ {\prime}. \sim P (\phi \& \sim \phi).
$$

Reading: It is not permitted to both do and not do $\phi$ .

Axioms D3 (or D3') seems the least intuitive for it suggests that every deontic system is complete over the set of possible actions. This is needed for technical reasons; to block certain anomalous inferences.

## 5.2. Deontic Reasoning for Contracts

We next consider how deontic logic can be applied to the case of contracting. Our approach is based on a suggestion by Anderson (1967) relating deontic logic to (alethic) modal logic using the definition

$$
O \phi \leftrightarrow \square (\sim \phi \rightarrow S),
$$

where S is a propositional constant indicating the sanction occurring from the violation of one's duties. In the case of contracts, such sections are sometimes stated explicitly within the contract as, e.g., penalty clauses or collateral. When sanctions for nonperformance are not stated, they may be determined through a court suit or other form of arbitration. However, for contracts, the notion of logical necessity for such sanctions is unrealistic. These contingencies do not necessarily apply for all possible worlds. Rather, it is sufficient to assert them only for the actual circumstances (world) of the contract. Thus, in our interpretation, we drop the necessity operator and adopt the equivalence $O\phi \leftrightarrow (\sim \phi \rightarrow S)$ .

The deontic axioms for contracting (DC) can then be stated as follows:

$$
\mathbf {D C 1 .} O \phi \rightarrow \sim (\phi \rightarrow S).
$$

Reading: the obligation to do $\phi$ implies that no sanctions occur for not doing $\phi$ .

$$
\begin{array}{r l}\text {DC2.}&O (\phi \&\psi)\\&\leftrightarrow (\sim \phi \rightarrow S) \&(\sim \psi \rightarrow S).\end{array}
$$

Reading: $\phi$ and $\psi$ are obligatory if and only if not doing $\phi$ implies sanctions and not doing $\psi$ implies sanctions.

$$
\mathbf {D C 3 .} (\phi \&\sim \phi) \rightarrow S.
$$

Reading: doing and not doing $\phi$ implies sanctions (analogue to D3, included for technical reasons).

## 5.3. Logic Programming Formulation

As discussed above, the representation of obligation (and other deontic concepts) in the electronic contracting model is based on an interpretation of contingent actions leading to sanctions. Replacing the former propositional constants, S, for sanction, we use the notation:

## default(X)

indicating the state where party X has defaulted on the contract. An action is obligatory, therefore is one that results in a state of 'default' if it is not done. In the Petri net notation, this is illustrated in fig. 3. That is, if X does action A, a transition is made from state S0 to state S1. If X does not A (e.g., by a certain deadline), the contract goes to a state where X is in default. The 'trans' assertions for this example are the following:

trans([S0], [S1], X: A).

trans([S0], [default(X)], \~X:A).

## 6. Performative Aspects

The discussion so far has focused on the logic underlying a contract text itself. We now consider the logical structure of actions by which a contract is formed, i.e., the negotiation of contracts. As noted earlier, a contract is in effect an exchange of obligations between parties. In practice, however, few contracts are formed as two simultaneous promising actions. Rather, the process is normally sequentialized by one party making an offer of a given set of contract terms, which the other party later accepts. Alternatively, the other party may reject the offer, or make a counter-offer. Offers or counter-offers may also be revoked by the offering party. This process can be described in the Petri net notation as shown in fig. 4.

![](/api/attachments/X3JYXE5P/fulltext/images/50062c67e33e9b913e0222edb84bc5002409d81177ae6d76de84fa2ac93285c9.jpg)  
Fig. 3. Example Petri Net with Temporal Negation.

The process begins at the null state, S0. If party X makes an offer to Y for contract C, the process moves to S1, from which several contingent actions can occur. If X revokes the offer or if Y rejects it, the process returns to S0, the null state. If Y accepts the offer, then state S2 is reached where the contract becomes executory. If Y makes a counter-offer, the process returns to state S1, with an offer for a new contract, C', and with the roles of X and Y reversed. Other negotiation processes may have variations from this model. For instance, in normal retail transactions, one usually does not make counter-offers. In real estate transactions, an offer is usually accompanied by an earnest money payment. In load applications, the bank's acceptance of a loan may have conditions based on the verification of the applicant's salary, credit history, etc.

Several points are noteworthy. The contracts, which is a contingent sequence of actions, representable as Petri net, is itself the result of a contingent sequence of actions, also representable as a Petri net. However, whereas the terms of a contract typically refer to various types of physical actions, e.g., delivery of goods, the negotiation process consists of actions that are linguistic. We refer to such linguistic actions as performatives. $^{10}$ A performative statement differs from one that is merely informative in that the event of making the statement is itself meaningful, and causes a change in state. A commonly used example is marriage ceremonies. For instance, a statement, 'John and Alice are married.' may be either true or false, but does not by its utterance give rise to any change in state. However, a statement, 'I now pronounce you husband and wife.' spoken by the proper religious authority under certain circumstances does in fact create the state of marriage. $^{11}$ . Performatives do not however have to be spoken. For example, a written signature is a common performative for the acceptance of a contract. Performatives do not even have to be in words. For instance, at an art auction, the raising of one's hand may be a legally binding performative, creating a purchase obligation. Similarly, on a commodities exchange, certain hand signals are performative offers to buy or sell at a given price.

![](/api/attachments/X3JYXE5P/fulltext/images/930651eb2e99a61db2fcbdea92235299a12495f39dc85d50d6ccc25ac76dabe7.jpg)  
Fig. 4. Petri Net for Contract Negotiation.

What counts as a performative is determined by some contextual set of rules or conventions. For example, signatures are performative within the rules and conventions of contract law. Hand signals are performative within the rules and con-vections of an auction or a stock or commodities exchange. In these latter cases, the rules and con-ventions are typically set forth in an umbrella membership agreement that is enforceable within the broader scope of contract law. The notion of electronic contracting would operate on this same principle.

## 7. Implementation

## 7.1. Definition Operator

Certain types of contractual forms appear in a wide variety of situations. Rather than having to re-specify these in detail each time, a definition facility is provided. To do this, we introduce a definition operator

## C::=DEF,

where C is a name for the contract form, followed by a parenthetical list of arguments. DEF is a list of primitive ‘trans’ assertions, or references to other contract forms. For instance, consider a contract of the form where X does A, followed by Y doing B, as shown in fig. 5. This might be defined as the contract structure, ‘two-step’:

two-step(X:A,Y:B)::=

$\operatorname{trans}([s(1, T1)], [s(2, T2)], X:A)$ ,

$$
\operatorname{trans} ([ \mathrm{s} (1, \mathrm{T} 1) ], [ \mathrm{s} (\text { default } (\mathrm{X}), \mathrm{T}) ], \sim \mathrm{X}: \mathrm{A}),
$$

$$
\operatorname{trans} ([ \mathrm{s} (2, \mathrm{T} 2) ], [ \mathrm{s} (3, \mathrm{T} 3) ], \mathrm{Y}: \mathrm{B}),
$$

$$
\operatorname{trans} ([ \mathrm{s} (2, \mathrm{T} 2) ], [ \mathrm{s} (\text { default } (\mathrm{X}), \mathrm{T}) ], \sim \mathrm{Y}: \mathrm{B}).
$$

This definition can now be used to generate a specific contract between parties, by supplying arguments for the variable parameters. For instance,

![](/api/attachments/X3JYXE5P/fulltext/images/fb6134bdbe1a82bf39f2a997264fa2d3703c624bb0b7e7dfccc57bc687687516.jpg)  
Fig. 5. A Contract Structure.

two-step(jones: rd(10-jun-88): pay(smith, \$100),

smith: rw(10 days): deliver(jones, widget))

indicates a contract where Jones is to pay Smith \$100 by 10 June 1988, and Smith, in turn, is to deliver a widget to Jones within 10 days of Jones payment.

By exploiting the flexible variable binding facilities provided by logic programming, other contractual forms can be defined through the use of variable structures. For instance, a contract structure, 'pre-pay' may be defined as an application of variables to 'two-step', where X pays some amount, \$P, after which Y delivers item Z.

pre-pay(X, Y, \$P, Z, X, XX)::=

two-step(X:rb(D):pay(X,\$P),

$\mathbf{Y}:\mathbf{rb}(\mathbf{D} + \mathbf{DD}):\mathbf{deliver}(\mathbf{X},\mathbf{Z}))$

Another contract structure, 'post-pay', might defined, where Y makes the delivery first, followed by X's payment:

post-pay(X, Y, \$P, Z, D, DD)::=

two-step(X:rb(D):deliver(Y,Z),

Y: rb(D + DD): pay(X, \$P).

A further refinement might be the contract structure, ‘post-pay-30’, specifying payment within 30 days:

post-pay-30(X, Y, \$P, Z, D)::=

post-pay(X, Y, \$P, Z, D, 30-days).

## 7.2. Contract Subroutines

In addition to the ability to define more detailed contractual forms through the application of variables, one contract form may reference another in subroutine fashion. An example of this is the contract structure for simple obligations. This is defined as the contract structure ‘obligtrans’ as follows:

obligtrans([S0], [S1], X:A)::=

trans([S0], [S1], X: A),

$\operatorname{trans}([S0], [s(default(X), T)], \sim X:A)$ .

Since contract structures may be used multiple times in a single contract, states in the contract are left as variables. Once such definitions have been made, they can be used in a similar fashion to 'trans' assertions in defining other contracts. For example, an alternative definition for 'two-step' might have been the following:

two-step(X:A,Y:B)::=

obligtrans([s(1, T1)], [s(2, T2)], X:A),

obligtrans([s(2, T2)], [s(3, T3)], Y: B).

## 7.3. Other Subroutine Examples

Example subroutine: contingent obligation. This type of structure arises in contracts where an obligation is dependent on the occurrence of some other event. Examples are various types of insurance and options. The Petri net diagram is as shown in fig. 6. Farty X's obligation to do B is contingent upon A occurring. Thus, if A occurs, X must do B or else default. However, if A does not occur, X's obligation is by-passed. This is the effect of the following subroutine definition:

condtrans(A, X : B, [S0, S1, S2])::=

trans([S0], [S1], A),

$\operatorname{trans}([S0], [S2], \sim A)$ ,

trans([S1], [S2], X : B),

$\operatorname{trans}([S1], [s(default(X), TD)], \sim X: B)$ .

Example subroutine iterated payments. Another common contracting structure is an iterated payment, e.g., as in installment loans, leases, etc. The Petri net diagram for an iterated payment is shown in fig. 7. This definition differs from others in that it also includes arithmetic operations and tests. Party X is obligated to do action A for Q iterations. Variable K is the counter. Thus, the sequence begins by setting K to 0. This is recorded in the state name, 'count(K)'. If K is greater than K, the process ends. Otherwise, it looks for the action, X:A, where K is incremented, and the process repeats. If X:A does not occur, then X defaults. (Note: normally, the variable K will also be embedded in the action predicate A, to distinguish one action from another.) This is captured in the following predicate:

![](/api/attachments/X3JYXE5P/fulltext/images/a3deb8055e59d2a008ed2a50899cefb774089834cd958128d211d05a92f06437.jpg)  
Fig. 6. Petri Net for Contingent Obligation.

![](/api/attachments/X3JYXE5P/fulltext/images/55dd30ab9040797e08993ac924985a7852ad60cc253d3e49524d10648f26b903.jpg)  
Fig. 7. Petri Net for Iterated Payments.

itertrans(X:A,K,Q,[S0,S1])::=

$$
\operatorname{trans} ([ \mathrm{S0} ], [ \mathrm{s} (\operatorname{count} (1, \mathrm{Q}), _ {-}) ], \text {true}),
$$

$$
\operatorname{trans} \left(\left[ s (\operatorname{count} (K, Q), _ {-}) \right], [ S 1 ], K Q\right),
$$

$$
\operatorname{trans} \bigl (\bigl [ s (\operatorname{cou} (K, Q), \_ \bigr) \bigr ],
$$

$$
\begin{array}{r l} & {\left[ s \big (\operatorname{count} (K K, Q), _ {-}) \right], (X: A, K K \text {is} K + 1) \big),} \\ & {\operatorname{trans} \big ([ s (\operatorname{count} (K, Q), _ {-}) ], [ s (\operatorname{default} (X), _ {-}) ] \big ],} \\ & {\sim X: A).} \end{array}
$$

## 8. Natural Language Interface

In the Prolog prototype, a natural language parser was developed to convert an English-like 'legalese' into the internal logic notation. This parser can also be used in the reverse, to paraphrase responses back into English. $^{12}$

Contracts are defined using the following general form:

contract $\langle name\rangle$ defined $\langle definition\rangle$ ,

where

$\langle \mathrm{name}\rangle =$ name for contract type,

<definition>

= expressions according to grammatical rules.

In addition, ‘scenarios’ indicating a hypothetical sequence of actual events can be defined, using the form

scenario $\langle name\rangle$ defined $\langle definition\rangle$ .

Once a contract and various scenarios have been defined, an exercise of the contract can be tested using the command

at $\langle$ time $\rangle$ whatif scenario $\langle$ name $\rangle$ ,

where

$\langle \mathrm{time}\rangle =$ hypothetical current date,

$\langle \mathrm{name}\rangle =$ scenario name.

Variations on this are

at $\langle$ time $\rangle$ whatif nothing.

at $\langle$ time $\rangle$ whatif same.

The parameter ‘nothing’ indicates an empty scenario; ‘same’ refers to the previously defined scenario.

Following is a simple example of a contract definition. The name of the contract is 'x1':

contract x1 defined:

Jones agrees to pay \$500 to Smith by May 3, 1987. Following that,

Smith agrees to deliver a washing machine to Jones within 10 days.

From this, the natural language parser produces the following logic representation (underscores followed by integers are internally generated variable names):

$\operatorname{trans}\bigl([s(\text{start}, 1-\text{jan-0})], [s(1, -93)], \text{true}\bigr)$

$\operatorname{trans}\left(\left[\mathrm{s}(1, -83)\right], \left[\mathrm{s}(2, -89)\right]\right)$

Jones: rb(3-may-1987): pay(Smith, \$500))

$\operatorname{trans}\bigl (\left[\mathrm{s}(1, - 83)\right],\left[\mathrm{s}(\operatorname{default}(\operatorname{Jones}), - 90)\right]$

\~ Jones: rb(3-may-1987): pay(Smith, \$500))

$\operatorname{trans}\left(\left[\mathrm{s}(2, -83)\right], \left[\mathrm{s}(3, -89)\right], \text{true}\right)$

$\operatorname{trans}\left(\left[\mathrm{s}(3, -83)\right], \left[\mathrm{s}(4, -89)\right], \text{true}\right)$

$\operatorname{trans}\left(\left[\mathrm{s}(4, -83)\right], \left[\mathrm{s}(5, -89)\right]\right)$ ,

Smith: rw(10days): deliver(Jones, washer))

$\operatorname{trans}\left(\left[\left(s(4, -83)\right], \left[s(\text{default}(\text{Smith}), -90)\right]\right), \right.$

\~ Smith: rw(10days): deliver(Jones, washer)) trans([s(5, \_83)], [s(finish, \_89)], true).

We now illustrate how a contract can be ‘executed’ by asking it various types of hypothetical ‘what if’ questions. To begin, we consider the case where no actions have been taken by either party. We ask the status of the contract as of May 1, 1987:

?- at 1-may-1987 whatif nothing.

Actions pending:
Jones is to pay \$500 to Smith by May 3, 1987.

Suppose the present time is now May 4 and nothing has happened. An execution of this scenario is the following:

?- at 5-may-1987 whatif nothing.

Party Jones defaults at May 4, 1987 because Jones failed to pay \$500 to Smith by May 3, 1987.

The following example presents a scenario, called 'a':

?-list scenario a.

a defined
Jones pays \$500 to Smith on April 24, 1987.

An execution of this scenario is as follows:

?- at 30-may-1987 whatif scenario a.

Party Smith defaults at May 5, 1987 because Smith failed to deliver a washing machine to Jones within 10 days.

Following is another scenario, 'b':

?-list scenario b.

scenario b defined
Jones pays \$500 to Smith on April 24, 1987.
Smith delivers a washing machine to Jones on April 30, 1987.

An execution of this scenario is as follows:

?- at 30-may-1987 whatif scenario b.

Contract completed on April 30, 1987.

Boiler plate contracts, with embedded variables, can also be defined. For example,

contract x2 defined:

Party X agrees to pay amount A to party Y by date D.

Following that,

Party Y agrees to deliver a washing machine to party X within 10 days.

These variables, by the way, are not Prolog variables (though corresponding Prolog variables are created internally). Variables here are strongly typed, e.g., by such prefixes as 'party', 'quantify', 'date', 'item', 'amount', 'interval', and so on. Variable names are otherwise arbitrary, and can be in either upper or lower case. An application of a boiler-plate contract to an actual situation is illustrated by the following example:

contract x3 defined:
contract x2 where
party X is Adam,
party Y is Baker,
amount A is \$100,
date D is April 15, 1989.

A paraphrase of the contract will now show the variables in the original boiler-plate text replaced by these new values (paraphrase in English):

Adam agrees to pay \$100 to Baker by April 15, 1989.

Following that,

Baker agrees to deliver a washing machine to Adam within 10 days.

## 9. Concluding Remarks

With the rapid growth of large-scale telecommunications networks, much of the necessary technology for electronic contracting applications is becoming available. Furthermore, numerous projects in logic programming technology (e.g., at MCC, ICOT, ESPRIT) promise large-scale processing capacity and database integration within the near future, key features for the inferential aspects of our proposal.

Anticipating such developments, a rich variety of theoretically interesting issues arise. Basic is the fundamental nature of business communications. Traditional systems analysis approaches emphasize the management of data, i.e., symbolic records of facts. However, the transmission of factual information is only one part of business communications. Another important part is performative communications, which change legal commitments of the organization. The signing of a contract is a prime example of this. Other examples include the issuing of a purchase order, sending an invoice, conveyance of a software license, conveyance of stocks or bonds, etc. Indeed, when conducted electronically, the payment of money is also in this category. The various kinds of business performatives and their associated socio-legal effects is a central problem area for further research.

## Appendix: Notational Summary

The following BNF syntax summarizes the formal notation for contracts (terms and conditions), for scenarios, and for negotiation procedures. The symbols ‘→’ and ‘|’ are for syntactic definition and alternation, respectively. Terms within angle brackets are non-terminals, all others are terminals.

$\langle \text{contract} \rangle \rightarrow \langle \text{trans assertion} \rangle | \langle \text{trans assertion} \rangle$ $\langle \text{contract} \rangle$

$\langle \mathrm{scenario}\rangle \rightarrow \langle \mathrm{fact}\rangle |\langle \mathrm{fact}\rangle \langle \mathrm{scenario}\rangle$ <negotiation procedure> → <performative trans assertion> |
<performative trans assertion> <negotiation procedure>

$\langle \mathrm{fact}\rangle \rightarrow \mathrm{fact}(\langle \mathrm{event}\rangle)$ . | fact( $\langle$ action $\rangle$ ).

$\langle$ trans assertion $\rangle \rightarrow$ trans([<substrate list>], [<sub-state list>], <acts>).

$\langle$ substate list $\rangle \rightarrow \langle$ substate $\rangle |\langle$ substate $\rangle \langle$ substate list $\rangle$

$\langle \mathrm{substate}\rangle \rightarrow \mathrm{s}(\langle \mathrm{state name}\rangle ,\langle \mathrm{date}\rangle )$

$\langle$ state name $\rangle \rightarrow \langle$ integer $\rangle |\langle$ integer $\rangle |\langle$ atom $\rangle |$ $\langle$ default $\rangle |\langle$ count $\rangle$

$\langle \mathrm{default}\rangle \rightarrow \mathrm{default}(\langle \mathrm{party}\rangle)$

$\langle \mathrm{count}\rangle \rightarrow \mathrm{count}(\langle \mathrm{numval}\rangle ,\langle \mathrm{var}\rangle)$

$\langle \mathrm{party}\rangle \rightarrow \langle \mathrm{atom}\rangle$

$\langle \mathrm{numval}\rangle \rightarrow \langle \mathrm{var}\rangle |\langle \mathrm{integer}\rangle$

$\langle\text{performative trans assertion}\rangle\rightarrow\text{trans}([\langle\text{substate list}\rangle],[\langle\text{substate list}\rangle],\langle\text{performative action}\rangle).$

```xml
<acts> → <action or event> | <action or event>, 
<acts>
<action or event> → <action> | <event> | true |
    <arith>
<action> → <agent> | <event> | ~ <action>
<event> → <r operator> | <event verb>
<event verb> → pay(<recipient>, $<integer>) |
    deliver(<recipient>, <object>) |
    (etc.)
<performative action> → <agent> | <r operator>: <performative verb> | true
<performative verb> → offer(<recipient>, <contract id>) |
    offer(<recipient>, <contract id>) |
    revoke(<contract id>) |
    reject(<contract id>) |
    accept(<contract id>) |
    counter(<recipient>, <contract id>)
    <object> → <atom> | <collective object>
    <collective object> → <atom> | <integer>
    <agent> → <party>
    <recipient> → <party>
    <party> → <atom>
    <r operator> → rd(<span>) | rt(<span>) | rb(<date>)
    <span> → <date> | span(<date>, <date>)
    <date> → <day> - <mo> - <yr>
    <day> → 1 | ... | 31
    <mo> → jan | feb | ... | dec
    <digit> → 0 | 1 | ... | 9
    <integer> → <digit> | <digit> <integer>
    <interval> → 1 day | <integer> days
    <uc> → A | ... | Z
    <lc> → a | ... | z
    <string> → <uc> | <lc> | <digit> | <string> <string>
    <atom> → <lc> <string> | ' <string>'
    <var> → <uc> <string>
    <contract id> → <atom> | <atom>(<arglist>)
    <arglist> → <arg> | <arg>, <arglist>
    <arg> → <var> | <action>
    <contract definition> → <contract id>::=<contract>
    <numexp> →
    <numval> | <numexp> <numop> <numexp>
    <numop> → + |-| * |/
    <arith> → <var> is<numexp>
```

## References

Anderson, A.R., The Formal Analysis of Normative Systems, in: N. Rescher, ed., The Logic of Decision and Action (University of Pittsburgh Press, 1967) 147–213.

Andersson, J.S., How to Define ‘Performative’ (University of Uppsala, Sweden, 1975)

Austin, J.L., How to DO Things with Words (Harvard University Press, Cambridge, MA, 1962).

Clocksin, W.F. and C.S. Mellish, Programming in Prolog (Springer-Verlag, 1981).

Davis, R.E., Logic Programming and Prolog: A Tutorial, IEEE Software, September, 53–62.

Flores, F. and J. Ludlow, Doing and Speaking in the Office, Decision Support Systems: Issues and Challenges (Pergamon Press, 1980).

Folesdal, D. and R. Hilpinen, Deontic Logic: An Introduction, in: R. Hilpinen, ed., Deontic Logic: Introductory and Systematic Readings (Reidel, Dordrecht, 1981).

Hilpinen, R., ed., Deontic Logic: Introductory and Systematic Readings (Reidel, Dordrecht, 1981).

Hilpinen, R., ed., New Studies in Deontic Logic (Reidel, Dordrecht, 1981).

Kimbrough, S., R. Lee and D. Ness, Performative, Informative and Emotive Systems: The First Piece of the PIE. Proceedings of the Conference on Information Systems (1984) 141–148.

Kimbrough, S., and R. Lee, On Illocutionary Logic as a Telecommunications Language, Proceedings of the International Conference on Information Systems, San Diego (Dec., 1986) 15–25.

Kimbrough, S., and R. Lee, Logic Modeling as a Tool for Management Science, Decision Support Systems 4, no. 1.

Lee, R., International Contracting – A Formal Language Approach, Hawaii International Conference on System Sciences, Kona, Hawaii (1988).

Lee, R., H. Coelho and J.C. Cotta, Temporal Inferencing on Administrative Databases, Information Systems 10, no. 2 (1985) 197–206.

Lee, R. and L. Miller, Logic Programming for Planning and Simulation, Decision Support Systems 2, no. 1 (1986) 15–25.

Lee, R. and G. Widmeyer, Shopping in the Electronic Marketplace, Journal of Management Information Systems 2, no. 4 (1986) 21–35.

Lyytinen, K.J., Theories of Language and Information Systems: An Appraisal of Alternative Language Views for Information Systems, International Conference on Information Systems (1984).

Malone, T., Electronic Markets and Electronic Hierarchies, CACM (1987).

McCarthy, J., The Common Business Communication Language in: A. Endres and J. Reetz, eds., Textverarbeitung und Buerosysteme (Oldenbourg Verlag, 1982).

Peterson, J.L., Petri Net Theory and the Modeling of Systems (Prentice-Hall, 1981).

Rescher, N. and A. Urquhart, Temporal Logic (Springer-Verlag, 1971).

Searle, J., Speech Acts: An Essay in the Philosophy of Language (Cambridge University Press, London, 1969).

Searle, J. and D. Vanderveken, Foundations of Illocutionary Logic (Cambridge University Press, London, 1985).

Tiersma, P.M., The Language of Offer and Acceptance: Speech Acts and the Question of Intent, California Law Review 74, no. 189 (1986) 189–232.

von Wright, G.H., And Next, Acta Philosophica Fennica, Fasc XVIII (North-Holland, Amsterdam, 1965).

von Wright, G.H., The Logic of Action – A Sketch in: N. Rescher, ed., The Logic of Decision and Action (University of Pittsburgh Press, 1967) 121–136.

von Wright, G.H., An Essay in Deontic Logic and the General Theory of Action, Acta Philosophica Fennica, Fasc. XXI (North-Holland, Amsterdam, 1968).

Williamson, O., Markets and Hierarchies: Analysis and Anti-Trust Implications (The Free Press, 1975).

Williamson, O., Transaction-Cost Economics: The Governance of Contractual Relations, Journal of Law and Economics (1979).

Winograd, T. and F. Flores, Understanding Computers and Cognition: A New Foundation for Design (Ablex Publishing, 1986).

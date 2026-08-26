---
otero_id: 17031
otero_key: "F834ZTAE"
title: "Logic modeling with partially ordered preferences"
authors: "George R. Widmeyer"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90099-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Logic Modeling with Partially Ordered Preferences

George R. WIDMEYER

Department of Decision Systems, University of Southern California, Los Angeles, CA 90089-1421, USA

Logic modeling is the use of formal logic as a modeling tool for problems of interest to management science. Based on a review of the logic of preference literature this paper presents five axioms for reasoning about a decision maker's preferences. A semantics of situations is adopted for the symbols used. Both logical deduction and a modification of dynamic programming are proposed for the problem of selecting preferred states of affairs over time. Finally, a sketch of an implementation in Prolog is presented.

Keywords: Logic, Preference, Prolog.

![](/api/attachments/F834ZTAE/fulltext/images/315485f8f822668a85343d2bbeabc9da4dae94d52daab1aef78d84e74fe3a328.jpg)

George R. Widmeyer is Assistant Professor of Decision Systems in the School of Business Administration of the University of Southern California. He received a Bachelor of Engineering Science in 1973, a M.S. in Operations Research in 1975, and a Ph.D. in Information Systems in 1986, all from the University of Texas at Austin. He also has eight years of full-time industry experience as an analyst and manager of data processing. His research interest include the use of logic

in decision support systems and the phenomenon of shopping in the electronic marketplace.

## 1. Introduction

Logic modeling is the use of formal logic as a modeling tool for problems of interest to management science [Kimbrough and Lee (1987)]. One characteristic of important decisions is that they generally are large and have many interactions that must be taken into consideration. Therefore, it is necessary to suitably delimit the problem domain.

The importance of defining the problem is well recognized. This leads to a necessarily limited description of the problem domain. Savage uses the term ‘small worlds’ to refer to the concept in statistics of a satisfactorily isolated decision situation [Savage (1954, section 5.5)]. Reiter adopts the term ‘closed world’ to describe the assumption in artificial intelligence applications that all the information about the problem is present in a database [Reiter (1978)]. Other terms can also be used, but the basic concept is to define the domain of discourse.

After the problem domain has been defined it is generally possible to reasoning about the problem. Consistency and completeness of the description and logical entailment is one type of reasoning that can be done but in most cases it is desirable to extend this to reasoning about preferences defined on the problem domain. A preference relation can be defined on the domain of discourse, which can be denoted as $(X, P)$ where X is a set and P is a relation defined on the set. The characteristics of the relation P are relative to the set X [Roberts (1979)].

This paper has descriptions of 'states of affairs' as the set $X$ . The relation $P$ is a set of preference relations defined on $X$ . The problem to be solved is to find a preferred sequence of states of affairs. The algorithm that is used is dynamic programming [Bellman (1957)] but modified for partially ordered preferences. This means that an algebraic function cannot be used for aggregating the returns from each stage of the problem.

Certain assumptions about the preference relation P are required for an algebraic function such

$$
u (x _ {1}, x _ {2}) = k _ {1} u _ {1} (x _ {1}) + k _ {2} u _ {2} (x _ {2}),\tag{as}
$$

where there are two factors, $x_{1}$ and $x_{2}$ , the value of which can be additively decomposed. Four cases can be defined in terms of ordinal versus cardinal data. These are

<table><tr><td rowspan="2"> $u_{i}$ </td><td colspan="2"> $k_{i}$ </td></tr><tr><td>ordinal</td><td>cardinal</td></tr><tr><td>ordinal</td><td>1</td><td>X</td></tr><tr><td>cardinal</td><td>2</td><td>3</td></tr></table>

The value function given above is representative of case 3 where the individual value functions, $u_{i}$ , are cardinal and the coefficients, $k_{i}$ , are numeric rates of substitution between the factors [Keeney and Raiffa (1976)]. When the coefficients are not known as in case 2 but only their ranking then it is possible to compute nondominated alternatives [Kirkwood and Sarin (1985)]. Finally, in case 1 only the ranking of alternatives along each attribute and the ranking of attributes is known. It is this case that is considered in this paper.

This paper proposes a method for finding a sequence of states of affairs for the case when preference is only partially ordered, the situation of case 1 above. The algorithm is a modification of classical dynamic programming. The next section presents the assumptions necessary for the algorithm. Section 3 discusses preference elicitation when preference is a partial order. Section 4 presents the algorithm and some suggestions for its use. The final section is some conclusions and recommended extensions.

## 2. Preference as a Partial Order

This section presents the assumption that can be incorporated into a decision support system (DSS) for reasoning with preferences. First the syntax and semantics of situations is presented. This is followed by the five axioms that are needed. Then the transistivity and independence assumptions are discussed.

A binary relation P on X can have certain properties. These are defined as:

(P1) reflexivity: $xPx$ , for all $x$ in $X$ ,

(P2) irreflexivity: $\sim xPx$ , for all $x$ in $X$ ,

(P3) symmetry: $xPy \dashrightarrow yPx$ , for all $x, y$ in $X$ , (P4) asymmetry: $xPy \dashrightarrow \sim yPx$ , for all $x, y$ in $X$ , (P5) transitivity: $xPy \& yPz \dashrightarrow xPz$ , for all $x, y, z$ in $X$ ,

(P6) negative transitivity: $\sim xPy\& \sim yPz \dashrightarrow \sim xPz$ , for all $x, y, z$ in $X$ ; or equivalently: $xPz \dashrightarrow xPy \vee yPz$ , for all $x, y, z$ in $X$ ,

(P7) completeness: $x \neq y \to xPy \vee yPx$ , for all $x, y$ in $X$ .

We use the term (strict) partial order to mean a relational system $(X, P)$ that is irreflexive and transitive. A (strict) weak order is asymmetric and negatively transitive. A (strict) linear order is irreflexive, transitive and complete.

## 2.1. Syntax and Semantics

We adopt Barwise and Perry's (1983) semantics for the elements of the set X. Their syntax is modified for our purpose.

Let $A$ be a set of entities, indexed from 1 to $N$ , the elements of $A$ are $a_1, \ldots, a_N$ . Let $R$ be a set of relations and $L$ a set of spatio-temporal locations. Then, we can define the following:

$$
\begin{array}{l l} \text {constituent sequence} & c s:: r (a _ {1}, \ldots , a _ {M}), \\ & M <   = N, \\ \text {State of affairs} & s o a:: (1, c s), \\ \text {course of events} & c o e:: \{s o a \}, \\ a _ {i} \text {in} A, r \text {in} R, 1 \text {in} L. \end{array}
$$

Preferences are expressed for states of affairs. This is based on Von Wright's (1972) concept of preference. We don't really prefer an apple to an orange. We prefer the state of affairs of enjoying the taste of an apple to the state of affairs of enjoying the taste of an orange.

A course of events is a set of states of affairs (SOAs). For example, in the context of a dinner menu the following three constituent sequences could be defined:

$cs_{1}::$ having a beef entree,

$cs_{2}::$ having a chicken entree,

$cs_{3}::$ having white wine.

Then saying that beef is preferred to chicken would be

$$
(1, c s _ {1}) P (1, c s _ {2}),
$$

and that beef and white wine is preferred to chicken and white wine would be

$$
\left[ \left(1, c s _ {1}\right), \left(1, c s _ {3}\right) \right] P \left[ \left(1, c s _ {2}\right), \left(1, c s _ {3}\right) \right].
$$

where we use list notation to collect elements of a set into courses of events.

The logic of preference literature [Chisholm and Sosa (1966), Rescher (1967), Von Wright (1963,1972)] develop rules of inference with the purpose of defining 'good' and 'bad'. They do it using logic notation and the semantic notion of 'possible worlds' (state description in the sense of Carnap). This literature uses the logical connective symbol '&' for the conjunction of SOAs and for truth functional statements about preferred combinations of SOAs. This is because SOAs are considered 'proposition-like' by Von Wright. This is consistent with Barwise and Perry where their SOAs explicitly carry a truth value since their syntax has soa::(1, cs, v) where v is either 0 or 1. We drop the third argument by assuming that all SOAs are true and allowing logical negation of an SOA.

## 2.2. Axioms

Let x, y and z stand for SOAs in X (i.e., x is a particular instance of the tuple $(1, cs)$ ). Then the following five axioms are needed:

(A1) Asymmetry: $xPy \dashrightarrow yPx$ , for all $x, y$ in $X$ , (A2) Transitivity: $xPy \& yPz \dashrightarrow xPz$ , for all $x, y, z$ in $X$ ,

(A3) Monotonicity: For all $x, y, z$ in $X$ , $xPy \leftrightarrow [x, z]P[y, z] \leftrightarrow [z, x]P[z, y]$ , (A4) Finiteness: $X$ is a finite set,

(A5) Zorn's lemma.

The fifth axiom, Zorn's lemma, can be stated as: if P is a strict partial order on a set X and if each linearly ordered subset of X has a maximal element then X has a maximal element [Fishburn (1972)]. It is an axiom of set theory and it has been shown to be equivalent to the axioms of choice (Suppes (1972)]. Finiteness of the SOAs (assumed in axiom A4) is sufficient for each subset to have a maximal element.

Before continuing, we should comment on what is not being assumed. First the preference relation P on the SOAs is not assumed to be complete, where completeness is defined as

$$
(x) (y) (x \neq y \rightarrow x P y \vee y P x).
$$

This means that the decision maker can say that x is preferred to y, y is preferred to x, he is indifferent ent between $x$ and $y$ , or that he is unsure.

A second axiom that we are not assuming is negative transitivity [Chipman (1960)], which can be stated as

$$
(x) (y) (z) (\sim x P y \& \sim y P z \dashrightarrow \sim x P z),
$$

or equivalently,

$$
(x) (y) (z) (x P z \dashrightarrow x P y \vee y P x).
$$

It can be proved that transitivity and completeness imply negative transitivity. If negative transitivity was substituted for transitivity in axiom A2 for the relation P on X would be a weak order and the following theorem could be proved.

Theorem 1. If $P$ on $X$ is a weak order and $X$ is countable, then there is a real-valued function, $u$ , on $X$ such that $xPy \leftrightarrow u(x) > u(y)$ .

This theorem is proved by Fishburn (1970, Theorem 2.2) and by Roberts (1979, Theorem 3.1) and by several others.

If completeness or negative transitivity were required then the decision maker could not answer 'don't know' when preference information is elicited. The impact of this is discussed in the next section.

## 2.3. Transitivity

The preference relation, P, is transitive and irreflexive and hence defines a strict partial order on the set of SOAs. The relation of unsure can be defined as

$$
\begin{array}{l} x U y \leftrightarrow \sim (x P y) \& \sim (y P x), \quad \text { or   as } \\ x U y \leftrightarrow \sim (x P y \vee y P x). \end{array}
$$

This says that your are unsure as to whether x is preferred to y or y is preferred to x if and only if it is not true that either xPy or yPx.

A very important feature of U is that it is not transitive (i.e., it is not true that $xUy \& yUz \dashrightarrow xUz$ ). If P on a set of SOAs is a strict partial order than xUy, yUz and xPz is allowed. This is because U is not an equivalence relation (i.e., reflexive, symmetric and transitive). We can define a new relation, E, that is transitive when P is a strict partial order [Fishburn (1970)]

$$
(x) (y) \left(x E y \leftrightarrow (z) \left(x U z \leftrightarrow y U z\right)\right),
$$

where $xUy \leftrightarrow \sim (xPy) \& \sim (yPx)$ .

Using this definition, the following theorem can be proved.

Theorem 2. If P on X is a strict partial order and X is couniable, then there is a real-valued function, u, on X such that

$$
\begin{array}{l} x P y \dashrightarrow u (x) > u (y), \\ x E y \dashrightarrow u (x) = u (y). \end{array}
$$

A proof of this theorem is given by Fishburn (1970, Theorem 2.5; 1985, Theorem 1.4). It requires the use of Szpilrajn's extension theorem, which says that every partially ordered set can be embedded in a linearly order set, that is proved using Zorn's lemma (our axiom A5).

It is important to recognize that the implication for the partially ordered case is one-way. Therefore, even though a real-valued function, u, exists and it can be used to compare alternatives x and y numerically, it cannot be inferred that x is preferred to y just because $u(x) > u(y)$ . This is because the implication of Theorem 2 is one-way.

The impact of the lack of completeness is that the unsure relation is not transitive. Other numeric representations have been studied, such as semi-orders and interval orders [Fishburn (1985)] but this paper uses logic since both of these are subsets of partial orders. The importance of the lack of completeness of the preference relation for DSS design is that the numeric representation of Theorem 1 cannot be used for reasoning about a preferred sequence of states of affairs.

In summary, the characteristics of the three relations, P, I and E defined in this section are: P is irreflexive and transitive (and hence asymmetric); U is reflexive and symmetric; and E is reflexive, symmetric and transitive. The next section discusses the type of independence condition that is needed.

## 2.4. Monotonicity

All axiomizations of preference use an independence condition. Marschak and Radner (1972) have several such as their independence condition 1:

Conditional preferences in one state of affairs are independent of consequences in other states of affairs.

Savage (1954) states a 'sure-thing' principle:

Partition a course of events into independent states of affairs. If $xPy$ given all SOAs then $xPy$ , which can be stated as $(x)(y)(z)[[x, z]P[y, z] \dashrightarrow xPy)$ .

Von Wright (1963) argues for an axiom of ‘unconditional preference’ that he states as

$$
\begin{array}{r} (x) (y) (x P y \leftrightarrow (z) ((x \& z) P (y \& z) \\ \& (x \& \sim z) P (y \& \sim z))), \end{array}
$$

with the side condition that z is not a truth function of any other states. This blocks the substitution of $\sim x$ or $\sim y$ for z that would produce the contradiction $x\&\sim x$ or $y\&\sim y$ .

Von Wright (1963) asks if this is a reasonable assumption. First, it is a universal generalization and would require checking all possible combinations of states x and z versus y and z. What if the number of states of affairs is very large? The second problem is that this principle seems to require elementary SOAs which are not a function of other SOAs. Von Wright (1963, p. 13) asks ‘but is not this assumption of ‘simples’ or of ‘logical atomism’ bad metaphysics?’

Von Wright answers these two questions by stipulating that the unconditional preferences are to be taken ‘relative to a given set of descriptions of generic states of affairs’, which he calls a ‘Universe of Discourse’. This then solves both problems since the rule only has to be checked for the finite set of SOAs and the Universe of Discourse contains all possible combinations of SOAs.

We would given Von Wright's axiom as

$$
\begin{array}{c} (x) (y) \big (x P y \leftrightarrow (z) ([ x, z ] P [ y, z ] \\ \& [ x, \sim z ] P [ y, \sim z ]) \big). \end{array}
$$

This is similar to our axiom A3, monotonicity, which can be stated as

$$
(x) (y) (z) \left(x P y \leftrightarrow [ x, z ] P [ y, z ]\right),
$$

where preference for SOAs such as x and y imply a preference for course of events such as $[x, z]$ and $[y, z]$ .

The monotonicity axiom from the standpoint of management science is generally regarded as reasonable, relatively mild or draws no comment at all [e.g., Krantz et al. (1971), Roberts (1979), Mitten (1974), Villarreal and Karwan (1981)]. Monotonicity necessitates that we partition the SOAs into independent SOAs. This means that there cannot be synergy between the SOAs. Consider the following example. $^{1}$

Define four states as

p::I live for 1 month more and die,

q::I live for 80 years more, then die,

r:: I live in excruciating pain,

s:: I live comfortably and have a fulfilling existence.

Now, $[q, s]P[p, s]$ but $[p, r]P[q, r]$ . This can happen. How do we account for this contradiction as a result of our assumptions? The answer lies in the fact that $p$ is not unconditionally preferred to $q$ , i.e., $pPq$ is not true. If it was true then monotonicity would imply $[p, s]P[q, s]$ in addition to $[p, r]P[q, r]$ . What is true is that $sPr$ since $[p, s]P[p, r]$ and $[q, s]P[q, r]$ . Even $[p, s]P[q, r]$ and $[q, s]P[p, r]$ could be considered true and these are not impacted by the monotonicity assumption applied to either $pPq$ or $sPr$ . Therefore, monotonicity is a limitation and its impact needs future work.

A final point concerns the monotonicity of grouping SOAs into sets forming COEs and monotonicity of the logical connective. The assumption on the formation of COEs means that $[x, \sim x, y]$ ,

would be allowed but in standard logic

$$
p \& \sim p \& q \neq q.
$$

In fact, $p \& \sim p$ is a contradiction and implies all possible conclusions. Such statements as $p \& \sim p$ must be handled by non-monotonic logic (see articles by Belzer and Loewer, Kimbrough and Adams, and Nute in this issue). For our purposes, we assume the rules of standard logic and do not allow inferencing from the premise $p \& \sim p$ . Therefore, we must restrict the substitution instances for $z$ to not being truth functionally dependent on $x$ or $y$ as Von Wright (1963) does. Barwise and Perry (1983) achieve the same restriction by building into their theory the 'Principle of Noncontradiction', which says that any actual COE cannot have the same SOA as being both true and false.

## 2.5. Summary

This section has presented the assumptions to be incorporated into our logic model for reasoning with preferences. It was based on a semantics for situations and a review of the logic of preference literature. It specifically discussed the meaning and implication of transitivity and monotonicity. The five axioms are minimal assumptions and are not sufficient for a numeric representation of preference.

## 3. Preference Elicitation

When the preference relation P on a set X is only assumed to be a partial order then a real-valued function u on X cannot be used to reason about preference as discussed in section 2.2. Therefore, the standard weak order preference elicitation approaches [e.g., Keeney and Raiffa (1976)] are not applicable. This section presents an interactive elicitation for partially ordered preferences.

## 3.1. User Responses

The assumption of a partial order means that a decision maker can given four responses to a question about whether he prefers alternative $a$ to alternative $b$ . He can say, 'Yes', 'No', 'Indifferent' or 'Unsure'. Each of these responses results in different database assertion in our DSS. We define two predicates in the logic programming language Prolog. The first better $(a, b)$ represents the fact that the decision maker says that $a$ is judged to be better than $b$ . The second equal $(a, b)$ represents the fact that the decision maker judges them to be equally desirable.

If the decision maker responds Yes to a question about alternative $a$ versus alternative $b$ then the fact better $(a, b)$ is asserted. Correspondingly, if the decision maker answers No to the question then better $(b, a)$ is asserted. Now if the decision maker is indifferent between $a$ and $b$ , then we take this to mean that $a$ is equivalent to $b$ and make a database assertion of the form equal $(a, b)$ . Finally, if the decision maker says that he is unsure then not better $(a, b)$ and not better $(b, a)$ are both true and nothing is asserted into the database.

There are two primitive predicates, better and equal, that are used to store preference information. As discussed in section 2.2 both are transitive. Our assumption of only a partial order means that the following series of responses by the decision maker are possible concerning three alternatives a, b and c:

(1) He can't say whether $a$ or $b$ is better.

(2) He can't say whether $b$ or $c$ is better.

(3) But he feels that $a$ is better than $c$ .

As a result of these three responses the single assertion of better(a, c) is entered into the database. If we had assumed a strict weak order then we would have asserted equal(a, b), equal(b, c) and deduced equal(a, c) and not ask the third question. If we had the third response we would have to point out that there is a contradiction and request further study.

## 3.2. Elicitation Program

A simple interactive elicitation program in Prolog can be written based on programs in Chapter 19 of Sterling and Shapiro (1986). It has questioning and explanation capability characteristic of an expert system but it is not an optimal partially ordered preference elicitation method.

First some rules can be defined using axioms A1 and A2. These use the predicate better(X, Y) as the decision maker's subjective judgement that SOA X is preferred to SOA Y. The four rules are

prefer(X, Y) :- better(X, Y).

/\* database fact \*/,

$\operatorname{prefer}(X, Y):-\operatorname{better}(X, Z)$ ,

prefer(Z, Y). / \* transitivity \*/,

$\operatorname{prefer}(X, Y): -\operatorname{better}(Y, X),!,$

fail. / \* asymmetry \*/,

prefer(X, X): - !, fail. / \* irreflexivity \*/

The reason that the ‘cut-fail’ (i.e., ‘!, fail’) is used in defining asymmetry and irreflexivity is that we lack completeness. Therefore, we cannot use ‘not’ since ‘not(better(Y, X))’ fails not only when there is a database fact to the effect of ‘better(Y, X)’ (i.e., a piece of positive information) but it also fails when there is no information.

If there is not information in the database then the following code requests preference information and asserts the necessary database facts. It is placed after the rules.

$\operatorname{prefer}(X, Y): -\operatorname{ask}(X, Y, \operatorname{Answer})$ ,

respond(X, Y, Answer), nl.

ask(X, Y, Answer): - write('Is'), write(X),

write('preferred to'), write(Y), write('?'),

read(Answer).

respond(X, Y, yes): - asserta(better(X, Y)).

respond(X, Y, no): - asserta(better(Y, X)).

respond(X, Y, indifferent)

:- asserta(equal(X, Y)).

respond(X, Y, unsure).

The fourth response ‘unsure’ is used for the ‘Don’t Know’ case.

The user can stop at any time and the system can reason with whatever information has been elicited. This approach can be used in finding preferred courses of action by allowing interactive elicitation about preferences for SOAs while building courses of events. This can be done aided by the use of dynamic programming presented in the next section.

## 4. Situation Finding

The procedure that is proposed for finding a preferred sequence of states of affairs is dynamic programming. The first subsection modifies the classical dynamic programming backward chaining algorithm for partially ordered preference. After that the approach is demonstrated with some Prolog code.

## 4.1. Preferred Courses of Events

The principle of optimality states

An optimal policy has the property that, whatever the initial state and initial policy, the remaining policy must constitute an optimal policy with regard to the state that results from the use of the initial policy [Bellman (1957, p. 83)].

Various authors have used dynamic programming in their solution procedures. Bellman (1957), Mitten (1964) and Nemhauser (1966) provide the basic idea. Mitten (1974) presents an approach that uses ordinal preference information and Villarreal and Karwan (1981) develop a branch and bound technique. The procedure offered here is in the spirit of Mitten (1974) but drops the requirement for completeness and adds Zorn's lemma, which is equivalent to the axiom of choice. We present our procedure for finding the Pareto optimal COEs in the following theorem.

Theorem 3. Assume that the relational system $(X, t^{\prime})$ satisfies asymmetry, transitivity, monotonicity, finiteness and Zorn's lemma. Then any COE constructed by the following recursive procedure is optimal. Take $COE_0 = [ ]$ and for $t - 1, \ldots, n$ let $COE_t^* = \max[SOA_t, COE_{t-1}^*]$ over all $SOA_t$ such that $[SOA_t, COE_{t-1}^*]$ is feasible.

Remember that $\left[SOA_{t}, COE_{t-1}^{*}\right]$ represents a set with the state of affairs $SOA_{t}$ and the optimal course of events $COE_{t-1}^{*}$ .

Proof. For $t = 1$ , $COE_{t}^{*} = \max[SOA_{t}]$ which exists and is optimal by Zorn's lemma. The proof proceeds by induction. Assume $COE_{t-1}^{*}$ exists and is optimal. Then $COE_{t-1}^{*}PCOE_{t-1}$ for all $COE_{t-1} \neq COE_{t-1}^{*}$ and so by monotonicity $[SOA_{t}, COE_{t-1}^{*}]P[SOA_{t}, COE_{t-1}]$ for all $COE_{t-1} \neq COE_{t-1}^{*}$ . Now, the construction required by the theorem has $COE_{t}^{*} = \max[SOA_{t}, COE_{t-1}^{*}]$ and so $COE_{t}^{*}$ is optimal. Further, $COE_{t}^{*}$ exists because $COE_{t-1}^{*}$ was assumed to exist and $SOA_{t}$ exists. Therefore, $COE_{t}^{*}$ exists and is optimal.

## 4.2. Prolog Implementation

This subsection sketches an implementation of the ideas presented in the logic programming language Prolog. This logic modeling approach uses both logical deduction and the principle of optimality. Krishnan et al. (1987) provide a detailed discussion on dynamic programming and Prolog.

The basic dynamic programming code is (DP1) bestcoe(0, [ ]).

(DP2) bestcoe(T, COE-STAR): - findall(POTENTIAL-COE-STAR, potential-coe-star(T, POTENTIAL-COE-STAR), S), choice-set(S, COE-STAR).

(DP3) pctential-coe-star(T, [SOA | PARTIAL-COE-STAR]) :-soa(T, SOA), T-MINUS-1 is T-1, bestcoe(T-MINUS-1, PARTIAL-COE-STAR)

Where the predicate $soa(T, SOA)$ is a database of facts about the states of affairs over time. The predicate bestcoe(T, COE-STAR) gives the best course of events at time T as COE-STAR. The findall predicate is a built-in procedure for generating a list of potential COEs that are then checked for being in the preferred set. A reading of these three clause is: DP1 – the best course of events at time 0 is nothing, the null list; DP2 – the best course of events at time T is COE-STAR and is produced by finding all potential courses of events, storing them in a list S and then choosing among these to find the subset COE-STAR; DP3 – potential optimal courses of events at time T are found by inserting states of affairs at time T at the head of a list of optimal courses of events for T - 1.

The preferred set is found by defining a predicate that finds a ‘choice set’ [Fishburn (1972)]

$C(S) = \{x: x \text{ in } S \text{ and } yPx \text{ for no } y \text{ in } S\}$ .

This predicate is

(DP4) choicset(S, COE-STAR): - findall(X, choice(X, S), COE-STAR).

(DP5) choice(X, S): - member(X, S), not((member(Y, S), choose(Y, X))).

where the member predicate tests whether X is a member of the list S and choose is defined as

(DP6) choose([HY | \_], [HX | \_])

:- prefer(HY, HX).

(DP7) choose([HY|[TY]], [HX|[TX]])
:- choose(TY, TX).

These predicates use the list notation because in Prolog it is necessary to store sets, such as the choice set, as a list.

Consider the following example. Say that there are three time periods and three possible constituent sequences at each period. Assume that a is better than b is better than c, d is better than e is better than f, and only that h is better than i. Then the Prolog code given would find [a] the best course of events at time 1, [d, a] the best COE for 2 time periods, and both [h, d, a] and [i, d, a] for the best COE for 3 time periods.

## 5. Conclusion

Preference theory in philosophy has been driven by trying to define ‘the good’ or at least ‘the better’. The only noncontroversial axioms that arise from this literature are those of asymmetry and transitivity, which are the characteristics of a partial order. Management science assumes a complete ordering in the form of the axioms for a partial order plus completeness. Then the problem is mapped to the real numbers and a cardinal value function is used for reasoning aout a preferred course of events.

The logic modeling approach presented in this paper does not assume completeness. Therefore, a linear additive value function does not exist and the approaches of multicriteria decision making cannot be used. Only the axioms can be used for reasoning based on the rules of logical deduction. This paper adopts a semantics for the primitives based on a theory of situations. The symbols in the logic modeling approach have a rich semantics and can be directly used for reasoning.

This reasoning can be more than logical deduction. Section 4 of this paper shows that the operations research technique of dynamic programming can be adapted to the case where the return function is not cardinal but just the concatenation of stagewise returns if these returns satisfy certain limited assumptions. The resulting solution is Pareto optimal. This is followed by a sketch of a possible implementation.

Certainly, if a decision maker satisfies the conditions necessary for the use of a cardinal value function then that is the more powerful approach. But where the decision maker is just exploring his preferences and is even still trying to define the problem then logic modeling is a useful method. The approach presented in this paper has relaxed the assumption of completeness. A possible extension is to modify the monotonicity axiom to allow explicit interaction effects to be present between SOAs in a set. This might be based on the fact that Von Wright does not allow SOAs to be truth-functionally dependent on each other in a particular course of events but Barwise and Perry only require that the union of SOAs satisfy their principle on noncontradiction.

## References

[1] Barwise, Jon and John Perry, Situations and Attitudes (MIT Press, Cambridge, MA, 1983).

[2] Bellman, R.E., Dynamic Programming (Princeton University Press, Princeton, New Jersey, 1957).

[3] Chipman, J.S., The Foundations of Utility, Econometrica 28 (1960) 193–224.

[4] Chisholm, R.M. and E. Sosa, On the Logic of 'Intrinsically Better', American Philosophical Quarterly 3 (1966) 244–249.

[5] Clocksin, W.F. and C.S. Mellish, Programming in Prolog (Springer-Verlag, New York, 1984).

[6] Fishburn, P.C., Utility Theory for Decision Making (Wiley, New York, 1970).

[7] Fishburn, P.C., Mathematics of Decision Theory (Mouton, Paris, 1972).

[8] Fishburn, P.C., Interval Orders and Interval Graphs (Reidel, Dordrecht, 1985).

[9] Keeney, R.H. and H. Raiffa, Decisions with Multiple Objectives (Wiley, New York, 1976).

[10] Kimbrough, S.O. and R.M. Lee, Logic Modeling: A Tool for Management Science, Proceedings of the Twentieth Hawaii International Conference on System Sciences 3, edited by R.R. Grams and R.H. Sprague, Jr. (1987) 424–434.

[11] Kirkwood, C.W. and R.K. Sarin, Ranking with Partial Information: A Method and an Application, Operations Research 33 (1985) 38–48.

[12] Krantz, D.H., R.D. Luce, P. Suppes and A. Tversky, Foundations of Measurement 1 (Academic Press, New York, 1971).

[13] Krishnan, R., R.M. Lee and G.R. Widmeyer, Portfolio Problems in Prolog, Proceedings of the Twentieth Hawaii International Conference on System Sciences, edited by E.A. Stohr et al., Western Periodicals, North Hollywood, CA (1987) 404–411.

[14] Marschak, J. and R. Radier, Economic Theory of Teams (Yale University press, New Haven, 1972).

[15] Mitten, L.G., Composition Principles for Synthesis of Optimal Multistage Process, Operations Research 12 (1964) 610–619.

[16] Mitten, L.G., Preference Order Dynamic Programming, Management Science 21 (1974) 43–46.

[17] Nemhauser, G.L. Introduction to Dynamic Programming (Wiley, New York, 1966).

[18] Reiter, R., On Closed World Data Bases, in: Logic and Data Bases, edited by H. Gallaire and J. Minker (Plenum Press, New York, 1978) 55–76.

[19] Rescher, N., Semantic Foundations for the Logic of Preference, in: The Logic of Decision and Action, edited by N. Rescher (University of Pittsburgh Press, 1967) 37–79.

[20] Roberts, F.S. Measurement Theory with Applications to Decisionmaking, Utility and the Social Sciences (Addison-Wesley, Reading, MA, 1979).

[21] Savage, L.J., The Foundations of Statistics (Wiley, New York, 1954).

[22] Sterling, L. and E. Shapiro, The Art of Prolog (MIT Press, Cambridge, 1986).

[23] Suppes, P., Axiomatic Set Theory (Dover Publications, New York, 1972).

[24] Villarreal, B. and M.H. Karwan, An Interactive Dynamic, Programming Approach to Multicriteria Discrete Programming, Journal of Mathematical Analysis Applications 81 (1981) 525–544.

[25] Von Wright, G.H., The Logic of Preference (Edinburgh University Press, 1963).

[26] Von Wright, G.H., The Logic of Preference Reconsidered, Theory and Decision 3 (1972) 140–169.

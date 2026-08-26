---
otero_id: 17120
otero_key: "HAJHZAR6"
title: "Reasoning with preferences and values"
authors: "George R. Widmeyer"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90007-e"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Reasoning with Preferences and Values

George R. WIDMEYER

Decision Systems Department, School of Business Administration, University of Southern California, Los Angeles, CA 90089-1421, USA

This paper is concerned with supporting practical thinking. This involves reasoning with a decision maker's preferential and ethical orderings of the different courses of action that could be pursued. We reject the use of a numeric utility function and argue for a logic programming approach for decision support. The basic properties of a logic model for reasoning with preferences and ethical values is defined. The paper then considers the problem of trading-off conflicting preferences and values. We propose a principle of cooperating preferences and values after a review of several other approaches.

Keywords: Logic Modeling; Preference.

![](/api/attachments/HAJHZAR6/fulltext/images/7cd0e3e063d2e20a385e5f563687cb022912030977f9290dddc7a6a60635b5a7.jpg)

George R. Wildmeyer is Assistant Professor of Decision Systems in the School of Business Administration of the University of Southern California. He received a Bachelor of Engineering Science in 1973, a M.S. in Operations Research in 1975, and a Ph.D. in Information Systems in 1986, all from the University of Texas at Austin. He also has eight years of full-time industry experience as an analyst and manager of data processing. His research interest include the use of logic in decision support systems and the phenomenon of shopping in the electronic marketplace.

## 1. Introduction

The concept of a decision support system (DSS) is changing from an emphasis on ‘improving the effectiveness of managerial decision making in semi-structured tasks’ to ‘improving creativity and learning for decisions that really matter’ [Keen (1986, p. 286)]. This paper presents an approach for supporting the decision maker’s reasoning about his actions and values. It address one of the research questions posed by Elam et al. [stated in Keen (1986)] in their vision of DSS. The issue is the formulation and solution of ‘wicked’ problems that require reasoning with values, ethics and aesthetics.

This is related to a problem given by March (1978), which he calls the ‘optimal sin problem’. The problem is how to tradeoff, over time, strict morality and experimentation with the possibility of having different ethics. The goal is to maintain some consistency between ethics and actions. Hence, we propose a system that allows a person to iteratively modify his actions, preferences or values in order to maintain consistency. The system is based on relational set theory and implemented in Prolog [Clocksin and Mellish (1984)].

This paper is concerned with supporting practical thinking. This involves reasoning with a decision maker's axiological evaluations (i.e., preferential ordering) and deontological evaluations (i.e., moral or normative ordering) of different courses of action that could be pursued [Von Wright (1962) and Korner (1976)]. We define a preference relation, denoted by P, to represent a comparison of alternatives based on the decision maker's subjective view of 'better than'. We define a value relation, denoted by V, to represent a comparison of alternatives based on the decision maker's subjective view of 'ethically preferred'. Therefore, aPb could be read as: 'I prefer a to b', and aVb could read as: 'a is more in accord with the norms of society than b'. Both types of evaluations can be used in a decision support system for identifying a preferred course of actions.

A second way of thinking of this is provided by the context of organizational decision making. If we adopt the view of rational decision making then we can regard human choice as a process of drawing conclusions from premises [Simon (1976, p. xii)]. Our premises are of two types: values premises that are provided by the organization and society, and personal preference premises, which are those of the individual manager. This is different than Simon (1976) since he would consider these two types of premises to be 'value premises' and to these he would add 'factual premises' (see his chapter III). Hence, we separate Simon's value premises into two components: organizational and personal. We assume that the organization does not completely control the individual and hence the personal premises which the decision maker holds may conflict with those supplied by the organization. We are trying to provide decision support that identifies and resolves this possible conflict.

The next section provides some background in relational systems and argues for a logic programming approach for decision support. Then we discuss preference theory from both a behavioral and a normative viewpoint. This is followed by the basic properties of a logic model for preference. The next section is a proposed syntax and rules of inference for the logic model. Section 6 offers an approach to trading off preferences and values over time. The final section gives conclusions.

## 2. Relational Systems

A relational system is a finite sequence of the form $\langle A, R_{1}, \ldots, R_{n} \rangle$ where A is a nonempty set of elements and the $R_{t}$ are relations on A [Tarski (1954)]. In our system, the elements of A are the actions that the decision maker can perform over time. The relations, $R_{t}$ , are revealed preferences for actions and are defined as the intersection of subjective preference, $P_{t}$ , and subjective values, $V_{t}$ , therefore

$$
a R _ {i} b \Leftrightarrow a P _ {i} b \& a V _ {i} b.
$$

This is read as: the decision maker reveals that he prefers $a$ to $b$ if and only if he truly prefers $a$ to $b$ and he values $a$ over $b$ . The relations of $P_t$ and $V_t$ could also be thought of as a pragmatic and an ideological component, respectively, for a person's desired behavior. We use the subscript $t$ to indicate that these relationships are time-dependent and hence can change.

Throughout this paper, we adopt the convention of representing the domain of possible actions as the set A with specific members a, b and c. The variables x, y and z stand for general members of the set A and when used in formulae are assumed to be universally quantified.

We can make a distinction between a numerical relational system (NRS) and an empirical relational system (ERS). A NRS is a relational system $\langle A, R_{1}, \ldots, R_{n} \rangle$ whose domain A is a set of real numbers and the $R_{i}$ are generally taken to be the common relations obtaining between numbers such as addition and greater than. On the other hand, an ERS has as its domain a set of identifiable entities [Suppes and Zinnes (1963)]. Scott and Suppes (1958) explain that an ERS is set of empirical data:

...we are mainly considering qualitative empirical data. Intuitively, we may think of each particular relation $R_{i}$ (an $m_{i}$ -ary relation, say) as representing a complete set of 'yes' and 'no' answers to a question asked of every $m_{i}$ -termed sequences of objects in $A$ . (p. 114)

The following figure repeats this distinction in the context of building a DSS.

<table><tr><td>Real World</td><td>abstraction</td><td>Empirical Relational System</td><td>measurement</td><td>Numerical Relational System</td></tr><tr><td></td><td></td><td>|</td><td></td><td>|</td></tr><tr><td></td><td></td><td>|</td><td></td><td>|</td></tr><tr><td></td><td></td><td>DSS $_L$ </td><td></td><td>DSS $_N$ </td></tr></table>

The process of abstraction involves representing objects and relationships of the 'real world' as a relational system. Then the measurement process maps these set-theoretic entities and relations into the real number system. Measurement theory is the study of quantifying empirical relational systems through the construction of scales from the empirical relational system to a numerical relational system [Krantz et al. (1971) and Roberts (1979)]. The result is that inferencing in the numerical relational system using numbers and mathematical operations implies knowledge about the real world.

Assume that information about the real world is represented in the empirical relational system using first-order logic. Statements about the ERS express the knowledge that an alternative, say a, is preferred to another alternative, say b. This can be represented in the logic-based decision support system $\left(\mathrm{DSS}_{\mathrm{L}}\right)$ directly as the fact ‘aRb’. In order to represent this in the numeric based system $\left(\mathrm{DSS}_{\mathrm{N}}\right)$ it is necessary to develop a scale (e.g., a function f) such that:

$$
x R y \Leftrightarrow f (x) > f (y).
$$

One of the necessary and sufficient conditions for the existence of such a function f is completeness of the relation R, as suggested by the complete set of 'yes' or 'no' answers of Scott and Suppes. By completeness we mean that for x not equal to y either xRy or yRx is true.

In our proposed system we drop the Scott and Suppes requirement for completeness. A numeric based system using the cardinal function f of above is possible if and only if the relation R is complete (this is discussed in section 3.2). Hence, we cannot traverse the measurement link to a numeric representation with a cardinal evaluation function. We could use an ordinal function - a ordering that only tells whether an action x is better than an action y - it does not indicate the strength of the relation R. Since an ordinal evaluation is also amenable to a logic programming implementation, we choose to do so. A second reason for choosing logic programming is that we take a logical, deductive point of view.

## 3. Preference

This section reports on behavioral and normative decision theory. The purpose is to argue that completeness is not generally a characteristic of preference information. Behavioral decision theory tries to explain how decisions are actually made whereas normative decision theory gives a view of how decision should be made.

## 3.1. Behavioral Preference

Two modes of preference elicitation can be identified. The first is termed 'dimensional' and means that the decision maker specifies information by performing comparisons along each dimension (e.g., the P and V) of a problem. The alternate mode for specifying preference information is termed 'holistic' and represents a single statement or evaluation (e.g., the R) of preference amongst two alternatives. Russo and Dosher (1983), Svenson (1979) and Wallsten (1980) give evidence toward showing that people prefer dimensional over holistic information processing. Johnson and Payne (1985) report on the tradeoffs between the accuracy and effort of the different strategies that people use.

A reason for using dimensional strategies is that decision makers are better at providing judgments along dimensions rather than providing aggregate evaluations. Dawes (1979), Dawes and Corrigan (1974) and Einhorn and Hogarth (1975) argue that individuals are good at single dimensional evaluations but poor at aggregating such judgments even when the single evaluations are correct. Therefore, heuristics that allow a decision maker to specify preferences along attributes are better than requiring holistic judgments. The problem is how to aggregate these individual preferences.

We show in section 4 that even if there is a complete set of dimensional evaluations there may not be a complete holistic ordering. Therefore, dimensional elicitation can lead to the completeness assumption being violated.

## 3.2. Normative Preference

Assume that there is a set of alternatives, A, and several relations defined on them, $R_{i}$ . The goal of measurement theory is to define the necessary and sufficient conditions for a numeric representation to capture the relationships expressed by the $R_{i}$ , i.e., for a homomorphism to exist. These numeric functions can then be used in a DSS for reasoning about a decision maker's preferences. The necessary and sufficient conditions of the existence for the homomorphism are very important because they express assumed constraints on the characteristics of the empirical system.

Von Neumann and Morgenstern (1947) presented the earliest axiom system for utility theory. They assume that preference is (1) complete, (2) transitive, and (3) continuous. The first two assumptions imply that preference is a weak order. Completeness means that one of the following three conditions must be true for two alternatives, $a$ and $b$ :

(1) $a$ is a preferred to $b$ ;

(2) $b$ is preferred to $a$ ;

or (3) the decision maker is indifferent between $a$ and $b$ .

Although they use this condition in their derivation they state some reservations,

It is conceivable – and may even in a way be more realistic – to allow for cases where the individual is neither able to state which of two alternatives he prefers nor that they are equally desirable. (page 19)

Given the three conditions, they prove that there is a utility function that preserves preference and can be used for inferencing in the form:

$$
x P y \Leftrightarrow u (x) > u (y),
$$

where 'xPy' is read as 'x is preferred to y'.

Other writers have argued against the completeness assumption [e.g., Aumann (1962), Luce (1956) and Halldin (1986)] but the basic problem is that when completeness is dropped then a numeric utility function cannot be used. Fishburn (1970) shows that when preference is only a partial order (i.e., irreflexive and transitive but not complete) that the implication of the representation is one-way:

$$
x P y \Rightarrow u (x) > u (y)
$$

which means that the utility function does not always provide conclusive help in determining the preferred alternative.

We do not assume completeness and therefore cannot use an utility function for reasoning about a decision maker's preferences. As a result all that we can do is use the axioms and rules of inference in our DSS. This is done after we establish the basic properties of the logic model of preferences and values.

## 4. Basic Properties of the Logic Model

This section presents two lemmas and a theorem concerning the intersection of relations. They state conditions on the holistic relationship between alternatives based on the properties of the dimensional relations. Krantz et al. (1971) give similar lemmas but they start with the holistic properties and derive the dimensional properties. The impact of the lemmas is summarized in a theorem. The theorem is grounded in the theory of partial orders given in Dushnik and Miller (1941) and Baker et al. (1970).

Define a relation R as the intersection of n primitive relations R Then, we have

$$
x R y = _ {\mathrm{df}} x R _ {1} y \& x R _ {2} y \& \dots \& x R _ {n} y.
$$

With this definition the following lemma can be proved.

Lemma 1. If the $R_{i}$ are {reflexive, irreflexive, symmetric, asymmetric, acyclic, transitive} then $R$ is correspondingly.

The proof of Lemma 1 is direct and therefore only the irreflexive, acyclic and transitive cases are given:

Proof. If the $R_{i}$ are irreflexive then $\sim xR_{i}x$ and it is true that $(\sim xR_{1}x \vee \sim xR_{2}x \vee \ldots \vee \sim xR_{n}x)$ and then $\sim (xR_{1}x \& xR_{2}x \& \ldots \& xR_{n}x)$ , which is $\sim (xRx)$ by definition of $R$ . Therefore, $R$ is irreflexive. If the $R_{i}$ are acyclic (i.e., transitive closure is irreflexive) then $x_{0}R_{i}x_{1} \& x_{1}R_{i}x_{2} \& \ldots \& x_{k-1}R_{i}x_{k} \Rightarrow \sim (x_{k}R_{i}x_{0})$ . Assume the premise of the definition and then $\sim (x_{k}R_{i}x_{0})$ for all $i$ and therefore it is true that $(\sim x_{k}R_{1}x_{0} \vee \ldots \vee \sim x_{k}R_{n}x_{0})$ and then $\sim (x_{k}R_{1}x_{0} \& \ldots \& x_{k}R_{n}x_{0})$ , which is $\sim (x_{k}Rx_{0})$ by definition of $R$ . Therefore, $R$ is acyclic. If the $R_{i}$ are transitive then $xR_{i}y \& yR_{i}z \Rightarrow xR_{i}z$ . Assume the premise of the definition and then $(xR_{1}y \& \ldots \& xR_{n}y) \& (yR_{1}z \& \ldots \& yR_{n}z) \Rightarrow (xR_{1}z \& \ldots \& xR_{n}z)$ , which is $xRy \& yRz \Rightarrow xRz$ by definition of $R$ . Therefore, $R$ is transitive.

Lemma 2. If the $R_{i}$ are {negatively transitive, complete} it is not necessarily true that $R$ is correspondingly.

The proof of Lemma 2 is more difficult since it involves something that is not necessarily true or false. The case of completeness is given since transitivity and completeness together imply negative transitivity and as we have seen in Lemma 1 transitivity is preserved under intersection.

Proof. The case for n=2 is given. Assume $R_{1}$ and $R_{2}$ are complete. The proof proceeds by showing that this is insufficient for R to be complete in all cases. If R is complete then $xRy \vee yRx$ by definition of completeness, then $(xR_{1}y \& xR_{2}y) \vee (yR_{1}x \& yR_{2}x)$ by the definition of R. Then applying distribution twice and rearranging we have,

$$
\begin{array}{l} (x R _ {1} y \vee y R _ {1} x) \& (x R _ {2} y \vee y R _ {2} x) \& \\ (x R _ {2} y \vee y R _ {1} x) \& (x R _ {1} y \vee y R _ {2} x). \end{array}
$$

Note that the first two conjuncts express the completeness of $R_{1}$ and $R_{2}$ and that there are two more conjuncts. The completeness of R requires the completeness of $R_{1}$ and $R_{2}$ and additional relationships. Therefore, the completeness of $R_{1}$ and $R_{2}$ are insufficient for the completeness of R.

As an example of this consider two strict weak orders (i.e., asymmetric and negatively transitive, which is implied by being irreflexive, transitive and complete but not vice-versa). Let

$$
\begin{array}{l} R _ {1} = \{(a, b), (b, c), (a, c) \}, \\ R _ {2} = \{(b, a), (b, c), (a, c) \}. \end{array}
$$

Then the intersection $R$ is $\{(b, c), (a, c)\}$ . $R$ is still irreflexive, transitive (trivially) but it is not complete. In fact it is still negatively transitive [it is a 2-dimensional weak order after Dushnik and Miller (1941)] but if there is a third relation $R_3 = \{(b, a), (b, c), (c, a)\}$ then the intersection of $R_1$ and $R_3$ is just $\{(b, c)\}$ which is not negatively transitive or complete.

The impact of Lemma 2 is that completeness is not necessarily preserved by the intersection of the relations $R_{i}$ defined on a set A. Based on our discussion in section 3, we can see that even if we have sufficient conditions for utility functions along each dimension we do not necessarily have a utility function that represents the holistic preferences of the decision maker. Conditions for the existence for the holistic value function are given by Keeney and Raiffa (1976) or Dyer and Sarin (1979). We summarize the impact of two previous lemmas.

Theorem 1. The intersection of $n$ ( $n > 1$ ) strict {total, weak or partial} orders is a strict partial order.

Proof. A strict partial order is irreflexive and transitive and since by lemma 1 these are preserved by intersection the result is a strict partial order. A strict weak order is asymmetric and negatively transitive, which implies irreflexivity and transitivity, and are implied by irreflexivity, transitivity and completeness. Since completeness is not preserved as shown in Lemma 2, the result is a strict partial order. Finally, a strict total order is irreflexive, transitive and complete and since completeness is not preserved by intersection the result is a strict partial order.

## 5. Logic Modeling

Logic modeling is the use of formal logic as a modeling tool for problems of interest to management science [Kimbrough and Lee (1988)]. This section presents the axioms and rules of inference for reasoning about values.

## 5.1.Axioms

A set of basic axioms can be derived from the work of Montgomery and Svenson [Montgomery and Svenson (1976) Svenson (1979) and Montgomery (1983)]. These authors do not specifically state the following axioms but they are clearly based on their work:

Axiom 1. Subjective representation of the choice alternative is described by a set of criteria.

Axiom 2. A decision maker expresses evaluations for alternatives along each criteria.

For our case, we assume that there are two criteria, preferences and values, at each period in time. This leads to two primitive predicates, prefer $(t, a, b)$ and value $(t, a, b)$ , which can be read as 'at time t, a is preferred to b' and 'at time t, the value of a is greater than b'.

Axiom 3. In order to reason about alternatives the decision maker applies one or more decision rules, all of which satisfy transitivity.

These axioms result in the use of dominance as an inferencing mechanism. The problem is that there are few practical decision situations where a single dominant alternative exists. The best that can usually be done is to identify the non-dominated alternatives and then choose from this reduced list. Since the number of nondominated alternatives may be large, this is not a trivial task. Several authors have proposed heuristics for reducing the nondominated set. An interesting approach is suggested by Montgomery (1983) in which he provides a series of operators that restructure the problem until a dominant alternative emerges. The use of these operators is a formalization of such rules as dimensional reduction and majority of confirming dimensions [Russo and Dosher (1983)], maximizing the number of dimensions with greater attractiveness [Svenson (1979)], and bounding the problem space [Walker (1986)].

## 5.2. Rules of Inference

The main rule of inference is given below stating Axiom 3 in both logic notation and in Prolog. Some additional predicates are given in order to demonstrate some of the reasoning about preferences and values.

A decision rule that satisfies Axiom 3 is our rule expressing the fact that actions must be in accords with the intersection of a decision maker's preferences and values:

$$
x R _ {t} y \Leftrightarrow x P _ {t} y \& x V _ {t} y.
$$

The necessary part of this biconditional can be expressed in Prolog as:

choose(T, X, Y): -

$\operatorname{prefer}(T, X, Y)$ , $\operatorname{value}(T, X, Y)$ .

We assume that ‘prefer’ and ‘value’ are both irreflexive and transitive and therefore by Lemma 1 ‘choose’ is irreflexive and transitive. This can be expressed as:

choose(T, X, X): - !, fail.

choose(T, X, Y) : -

choose(T, X, Z), choose(T, Z, Y).

It can be shown that irreflexivity and transitivity implies asymmetry. Therefore, it is instructive to see if a goal such as 'choose(T, a, b)' could ever succeed if it has already been determined that 'choose(T, b, a)' is true. It is also necessary to make sure that the goal 'not(choose(T, a, b))' does succeed. Both cases do act as required but the rule order is necessary for the code to behave as intended.

Overlapping time intervals for the decision maker's preferences and values can be handled with the following code.

$$
\operatorname{choose} (T, X, Y): -
$$

$$
\operatorname{prefer} (T 1, T 2, X, Y), T > = T 1, T <   = T 2,
$$

$$
\text { value } (T 3, T 4, X, Y), T > = T 3, T <   = T 4.
$$

This says that if there are preferences and values that bracket the time T in which preferences and values favor X over Y then X is chosen over Y. The four place predicates ‘prefer’ and ‘value’ are appropriately defined from the three place predicates of the same name.

Another set of rules are included for the ‘prefer’ and ‘value’ predicates since they are also irreflexive and transitive. These are necessary because we want the implication to be in both directions. That is, preferences and values imply the choice of certain actions and the choice of particular actions imply certain preferences and values. In this way the decision maker is forced to iterate between specification of actions, preferences and values until they are consistent.

As an example of how this type of reasoning is used, consider three alternatives - a, b, and c - and let the relation P and V be:

$$
\begin{array}{l} P = \{(a, b), (b, c), (a, c) \}, \\ V = \{(b, a), (b, c), (a, c) \}. \end{array}
$$

The intersection R is $\{(b, c), (a, c)\}$ , as discussed in section 4.1. From this we see that both a and b are revealed to be better than c, but we do not know the relationship between them. We can either elicit more information about a and b or we can suggest that either course of action a or b can be pursued. If the decision maker really wants to pursue course of action c, then he must change both his preferences and his values.

## 6. Tradeoffs over Time

The major issue that we have identified is how should a person change his preferences and values to be in accord with his actions. Should the decision maker change his preferences or his values? Which is more important? This section explores two possible answers. The first is a linear additive utility function over time approach. The second is based on game theory. It then gives an example of reasoning about the case of aPb and bVa.

## 6.1. Utility Function over Time

Conjoint measurement provides necessary and sufficient conditions for the existence of a linear additive utility function that can represent out $R_{t}$ relation. The two major assumptions are that $\langle A, R \rangle$ is a strict weak order and that it satisfy independence. Independence means that the evaluations of alternatives at a particular time t using the decision maker's references and values are independent of the evaluations at other times not equal to t. If we could assume these [and some other given in Krantz et al. (1971) or Roberts (1979)] then at each time period t we could assess a utility function such that:

$$
\begin{array}{r l} a R _ {t} b & \Leftrightarrow r _ {t} (a) = p _ {t} (a) + v _ {t} (a) > r _ {t} (b) \\ & = p _ {t} (b) + v _ {t} (b), \end{array}
$$

where $p_{t}$ and $v_{t}$ are component preference and values utility functions.

Given these functions at each time t we could build a discounted utility function:

$$
\begin{array}{r l} r (a) & = r _ {1} (a) + (1 + i) ^ {- 1} r _ {2} (a) \\ & \quad + (1 + i) ^ {- 2} r _ {3} (a) + \dots \end{array}
$$

The problem with this is that we would have to assume that $\langle A, R_1, R_2, \ldots \rangle$ is a strict weak order and satisfies independence. But we cannot do this. The theorem of section 4 says that the relations $R_t$ on $A$ are a strict partial order. Second, we want to allow the decision maker's preferences and values in one time period to impact his preferences and values in subsequent periods and hence we cannot satisfy the independence assumption either.

Harvey (1986) relaxes some of the assumptions of the discounted utility model. He then develops a discount function that decreases arithmetically rather than geometrically and has variable rather than constant discount rates. But he still has to assume a weak order and independence conditions.

Widmeyer (1988) provides a method based on dynamic programming that would allow the $R_{t}$ relations on A to be a strict partial order. But he also must assume these relations to be independent of each other in order for the recursive procedure to work. Therefore, we need a method that explicitly recognizes the dependences of future preferences and values on past actions and hence on past preferences and values.

## 6.2. Evolving Cooperation

We think of the preference relation $P_{t}$ and the value relation $V_{t}$ as being represented by two persons in a nonzero sum game. Obviously, if $aP_{t}b$ , $aV_{t}b$ and $aR_{t}b$ are all true then there is no conflict and really no reason for using a decision support system. The decision maker just does what he prefers and society sanctions. The interesting case is when there is conflict.

Assume that $aR_{t}b$ is true but the $bP_{t}a$ and $bV_{t}a$ . This means that the decision maker's preferences and values must change in order to be consistent with his actions. Consider the following payoff matrix where each 'player', $P_{t}$ and $V_{t}$ , can either change or hold to there current evaluations.

$$
\begin{array}{c c c} & V _ {t} \\ P _ {\text {hold}} ^ {\text {change}} & \text {change} & \text {hold} \\ & (G, G) & (W, B) \\ & (B, W) & (P, P) \end{array}
$$

The entries in this matrix satisfy:

$$
B (e s t) > G (o o d) > P (o o r) > W (o r s t),
$$

and $G > \frac{1}{2}(\mathbf{B} + \mathbf{W})$ . For example, the entry $(B, W)$ is interpreted as that it is the Best for $P_{t}$ to hold and the Worst for $V_{t}$ to change if that is the joint strategy chosen.

The form of the game matrix given is an example of the classical Prisoner's Dilemma game. We can think of having to play this game at each time period. Axelrod (1984) shows that a very robust strategy for this kind of game, called the iterated Prisoner's Dilemma, is 'Tit for Tat'. This strategy says that you start by changing and thereafter do what the other player did on the previous move.

Translating this strategy to our situation of preferences and values it says that the decision maker should consider immediately changing his preferences and values if there is a conflict. If he changes one but not the other in a particular time period then in the next period he should either change the second or return the one he changed back. After some period of time the decision maker will relent from holding his individual non-cooperating preferences and values, for which he gets $(P, P)$ , and changes each and gets $(G, G)$ . Hence, the idea of evolving cooperation.

For each pair of actions he can decide whether his preferences and values are in alignment with his revealed evaluation of these actions. If they are then he can move on to the next pair. If not then he can go through a sequence of games considering whether he will change his internal axiological or deontological evaluations. He has to eventually get everything into alignment and the Tit for Tat strategy is one possible decision rule that could be incorporated into a decision support system for reasoning with preferences and values.

## 6.3. Conflicting Preference and Values

A more interesting situation is when the person holds $aP_{t}b$ and $bV_{t}a$ . Then what does he do? Does he trade this off to result in $aR_{t}b$ or $bR_{t}a$ ? We explore this by considering the completeness of R.

If we drop the time index t, then the logical relationship on R is: $xRy \Leftrightarrow xPy \& xVy$ . We can state the completeness of R as: $xRy \vee yRx$ . If this is stated in terms of P and V then we have:

$$
(x P y \vee y P x) \& (x V y \& y V x) \&
$$

$$
(x P y \vee y V x) \& (y P x \vee x V y),
$$

similar to the statement of the completeness of $R$ given in the proof of Lemma 2. Label the four conjunctive terms 1, 2, 3 and 4. Now there are four cases:

I. $xPy, xVy$ .

II. yPx, yVx.

III. $xPy, yVx$ .

IV. $yPx, xVy$ .

All four terms are true for cases I and II. Term 4 is false in case III and term 3 is false in case IV. When P = V as in cases I and II then the intersection of P and V equals P, equals V, equals R and the choice is clear. When $P \neq V$ then R is not completely specified, as in cases III and IV.

Now reintroduce the time subscript. Based on the discussion in section 6.2, we adopt the following principle.

Principle of Cooperating Preferences and Values: We cannot have $xP_{t}y$ if there does not exist an $s$ such $xV_{s}y$ , $s \geq t$ .

Consider this principle in an organizational context. If the decision maker holds a preference for action a over b at time t, which is in the conflict with the organizational values, then he must be able to make the argument that the organizational values will change at some time s in the future. If the decision maker cannot make such an argument then his preferences and values, in relation to actions a and b, remain in conflict. The extent of decision support is determined by the help that the decision maker receives in making such an argument.

## 7. Conclusion

We have presented some rules of inference that can be incorporated into a DSS for reasoning with values. The goal of the system is to allow exploration and learning by the decision maker by forcing consistency between actions taken and the decision maker's subjective preferences and values. The system is based in a review of the behavioral and normative literature and proceeds from an axiomatic and set-theoretic standpoint. Finally, it is an example of logic modeling as an approach to supporting decision making.

Possible extensions of this research that are being pursued involve the development of a modal logic of preference and argument based reasoning for decision support. It is felt that decision support consists of a proper argument favoring a particular course of action. An important part of that argument involves reasoning with preferences and values.

We have tried to address the research issue of providing decision support for problems that require reasoning with values and ethics. The principle of cooperating preferences and values is based in the idea that it is not a question of immorality to hold preferences that conflict with current ethical values. Rather it is only illogical to hold those preferences if the argument cannot be made that such ethical values will change in the future. We realize that ethics is a sensitive issue but we feel that this is all the more reason why we should try to provide decision support in solving such problems.

## Acknowledgment

I would like to thank Steve Kimbrough and the anonymous referees for their helpful suggestions.

## References

Aumann, R.J., Utility Theory without the Completeness Axiom, Econometrica 30 (1962) 445–462.

Aumann, R.J. Utility Theory without the Completeness Axiom: A Correction, Econometrica 32 (1964) 210–212.

Axelrod, R., The Evolution of Cooperation (Basic Books, New York, 1984).

Baker, K.A., P.C. Fishburn and F.S. Roberts, Partial Orders of Dimension 2, Interval Orders, and Interval Graphs, Paper P-4367 (The RAND Corporation, Santa Monica, CA, 1970).

Clocksin, W.F. and C.S. Mellish, Programming in Prolog (Springer-Verlag, New York, 1984).

Dawes, R.M., The Robust Beauty of Improper linear Models, American Psychologist 34 (1979) 571–582.

Dawes, R.M. and B. Corrigan, Linear Models in Decision Making, Psychological Bulletin 81 (1974) 95–106.

Dushnik, B. and E.W. Miller, Partially Ordered Sets, American Journal of Math 63 (1941) 600–610.

Dyer, J.S. and R.K. Sarin, Measurable Multiattribute Value Functions, Operations Research 27 (1979) 810–822.

Einhorn, H.J. and R.M. Hogarth, Unit Weighting Schemes for Decision Making, Organizational Behavior of Human Performance 13 (1975) 171–192.

Fishburn, P.C., Utility Theory for Decision Making, (John Wiley & Sons, New York, 1970).

Halldin, C., Preference and the Cost of Preferential Choice, Theory and Decision 21 (1986) 35–63.

Harvey, C.M., Value Functions for Infinite-Period Planning, Management Science 32 (1986) 1123–1139.

Johnson, E.J. and J.W. Payne, Effort and Accuracy in Choice, Management Science 31 (1985) 395–414.

Keen, P.G.W., Decision Support Systems: The Next Decade, in: Decision Support Systems: A Decade in Perspective E. McLean and H.G. Sol, eds. (North-Holland, New York 1986) 221–237.

Keeney, R.L., Siting Energy Facilities (Academic Press, New York, 1980).

Keeney, R.L. and H. Raiffa, Decisions with Multiple Objectives (John Wiley & Sons, New York, 1976).

Kimbrough, S.O. and R.M. Lee, Logic Modeling: A Tool for Management Science, Decision Support Systems 4 (1988).

Korner, Stephan, Experience and Conduct: A Philosophical Enquiry into Practical Thinking (Cambridge University Press, New York, 1976).

Krantz, D.H., R.D. Luce, P. Suppes and A. Tversky, Foundations of Measurement, Vol. 1 (Academic Press, New York, 1971).

Luce, R.D., Semiorders and a Theory of Utility Discrimination, Econometrica 24 (1956) 178–191.

March, J.G., Bounded Rationality, Ambiguity, and the Engineering of Choice, The Bell Journal of Economics 9 (1978) 587–608.

Montgomery, H., Decision Rules and the Search for a Dominance Structure: Towards a Process Model of Decision Making, in: Analysing and Aiding Decision Processes, P. Humphreys, O. Svenson and A. Vari, eds. (North-Holland, Amsterdam, 1983) 343–369.

Montgomery, H. and O. Svenson, On Decision Rule and Information Processing Strategies for Choice Among Multiattributed Alternatives, Scandinavian Journal of Psychology 17 (1976) 283–291.

Roberts, F.S., Measurement Theory with Applications to Decisionmaking, Utility and the Social Sciences (Addison-Wesley, Reading, MA, 1979).

Russo, J.E. and B.A. Dosher, Strategies for Multiattribute Binary Choice, Journal of Experimental Psychology: Learning, Memory, and Cognition 9 (1983) 676–696.

Scott, D. and P. Suppes, Foundational Aspects of Theories of Measurement, Journal of Symbolic Logic 23 (1958) 113–128.

Simon, H., Administrative Behavior, 3rd edition (Free Press, 1976).

Suppes, P. and J.L. Zinnes, Basic Measurement Theory, in: Handbook of Mathematical Psychology, Vol. 1, R.D. Luce, R.R. Bush and E. Galanter, eds. (John Wiley and Sons, New York, 1963) 1–76.

Svenson, O., Process Description of Decision Making, Organizational Behavior and Human Performance 23 (1979) 86–112.

Tarski, A., Contributions to the Theory of Models, Idagationes Mathematicae 16 (1954) 572–588; 17 (1955) 56–64.

Von Neumann, J. and O. Morgenstern, Theory of Games and Economic Behavior, 2nd edition, (Princeton University Press, Princeton, NJ, 1947).

Von Wright, G.H., The Logic of Preference, (Edinburgh University Press, 1963).

Walker, The Use of Screening in Policy Analysis, Management Science 32 (1986) 389–402.

Wallsten, T.S., Processes and Models to Describe Choice and Inference Behavior, in: Cognitive Processes in Choice and Decision Behavior, T.S. Wallsten, ed. (Lawrence Erlbaum Associates, Hillsdale, NJ, 1980) 215–237.

Widmeyer, G.R., Logic Modelling with Partially Ordered Preferences, Decision Support Systems 4 (1988) 87–95.

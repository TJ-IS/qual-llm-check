---
otero_id: 10896
otero_key: "G89EW5VE"
title: "Modelling uncertain positive and negative reasons in decision aiding"
authors: "Meltem Öztürk; Alexis Tsoukiàs"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.06.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Modelling uncertain positive and negative reasons in decision aiding

Meltem Öztürk <sup>⁎</sup>, Alexis Tsoukiàs

LAMSADE- CNRS, Université Paris Dauphine, 75775, Paris Cedex 16, France

Accepted 9 June 2006

Available online 27 July 2006

## Abstract

The use of positive and negative reasons in inference and decision aiding is a recurrent issue of investigation as far as the type of formal language to use within a DSS is concerned. A language enabling to explicitly take into account such reasons is Belnap's logic and the four valued logics derived from it. In this paper, we explore the interpretation of a continuous extension of a four valued logic as a necessity degree (in possibility theory). It turns out that, in order to take full advantage of the four values, we have to consider “sub-normalised” necessity measures. Under such a hypothesis four valued logics become the natural logical frame for such an approach.

© 2006 Elsevier B.V. All rights reserved.

Keywords: Uncertainty; Four valued logic; Possibility theory; Preference modelling; Decision making

## 1. Introduction

The design and implementation of Decision Support Systems requires, besides appropriate computer interfaces, the use of formal languages in which the information about decision problems and preferences of the decision makers and of the users have to be coded. A language regularly used (some times implicitly) for such a purpose is classic logic. For instance preference statements of the type “x is better than y” become binary predicates to apply in a universe of discourse represented by the set of potential actions a decision maker could undertake. Classic logic is sufficiently powerful to allow elegant and concise representations besides fitting the mathematical dimension of most of the decision and evaluation models used within Decision Support Systems [see Refs. 6,10].

On the other hand classic logic is not always suitable to formalise real life problem situations since it is unable to handle incomplete and/or inconsistent information. In decision aiding such situations are regular and indeed classic logic has often been criticised as a language used for decision support models formulation [see 16,17,27,32,39]. Both in decision theory and in logic, a recurrent idea is to separate positive and negative reasons supporting a decision and/or a logical inference [for some early contributions the reader can see 7,8,15,29,30]. Under such a perspective we study the possibility to extend a four valued logic [see 37] in situations where it is possible to make continuous valuations on the presence of truth.

The best known formal language explicitly designed to take into account positive and negative reasons for inference purposes is Belnap's four valued logic. The four values $( t , f , k , u )$ introduced by Belnap have a clear epistemic nature. Given a proposition $\alpha ,$ four situations are possible:

— true (t): there is evidence that α holds (presence of positive reasons) and there is no evidence that α does not hold (absence of negative reasons);

— false (f): there is no evidence that α holds (absence of positive reasons) and there is evidence that α does not hold (presence of negative reasons);

— contradictory (k): there is evidence that α holds (presence of positive reasons) and there is evidence that α does not hold (presence of negative reasons);

unknown (u): there is no evidence that α holds (absence of positive reasons) and there is no evidence that α does not hold (absence of negative reasons).

However, the sources of uncertainty are not limited to pure unknown and/or contradictory situations. The evidence “for” or “against” a certain sentence might not be necessarily of a crisp nature. In this case, we can consider continuous valuation of “positive” and “negative reasons” [see 38]. This continuous extension may help us to deal with uncertainty due to doubts about the validity of the knowledge; imprecision due to the vagueness of the natural language terms; incompleteness due to the absence of information; apparent inconsistency due to contradictory statements. Such situations are all the more relevant in decision aiding and preference modelling.

Indeed Belnap's logic has already been studied and extended [in Refs. 14,36,39] as a language for preference modelling purposes (the DDT logic). Such a (first order) language allows to take explicitly into account crisp positive and negative reasons for which a preference statement of the type “x is better than $y '$ holds, thus allowing the construction of more flexible preference structures [see Ref. 40]. In this paper, besides presenting the DDT logic [37] we study the continuous extension of Belnap's logic suggested in Ref. [28]. Of course Belnap's logic is not the only way to consider paraconsistency [see Refs. 12,31]. However, it has the simplest semantics allowing to create easily extensions for several different purposes. The reader can see other types of extensions in the work of Arieli [see Ref. 2–5].

The aim of the paper is to verify whether it is possible to associate to the DDT logic an uncertainty distribution, possibly of the possibility/necessity type and if so, under which conditions. Section 2, introduces the basic concepts of the four valued logic and its continuous extension through the concept of positive and negative membership. Two examples of their use in decision aiding are also present in this section. In Section 3, we try to establish a first relation between four valued logic and possibility theory. Some related problems are discussed. In Section 4, we suggest the use of “subnormalised” necessity distributions and we show why four valued logic can be considered a language to which we associate such a type of uncertainty distributions.

## 2. Four valued logic and its continuous extension

## 2.1. Syntax

Belnap's original proposition [see Refs. 7,8] aimed to capture situations where hesitation in establishing the truth of a sentence could be associated either to ignorance (poor information) or to contradiction (excess of information). In order to distinguish these two types of uncertainty, he suggested the use of four values forming a bi-lattice (see Fig. 1). Intuitively, the four values are partially ordered on the basis of two relations: “more truth” relation and “more information” relation. It is easy to remark that u and k are incomparable on the first dimension of the bi-lattice while t and f are incomparable on the second one. It has been shown that such a bi-lattice is the smallest nontrivial interlaced bilattice [see Refs. 21,24].

DDT logic [for details see Ref. 37] extended Belnap's logic in a first order language endowed with a weak negation (≁). DDT is a Boolean algebra. This logic allows a distinction between the strong negation (¬) and the complementation (∼) (see Table 1). It is easy to check that ∼ α ≡ ¬ ≁ ¬ ≁ α. One can remark that strong negation swaps positive and negative reasons, complementation reverses the existence of negative and positive reasons while weak negation reverses only the existence of negative reasons.

![](/api/attachments/G89EW5VE/fulltext/images/a320deed52d0cb7ce090e1bab75f4b0827e3c0aa572728e80497ba5e60006ceb.jpg)  
Fig. 1. The bi-lattice suggested by Belnap.

Table 1  
The truth tables of the negations and the complement

<table><tr><td> $\alpha$ </td><td> $\neg\alpha$ </td><td> $\neg\alpha$ </td><td> $\neg\alpha$ </td></tr><tr><td> $t$ </td><td> $k$ </td><td> $f$ </td><td> $f$ </td></tr><tr><td> $k$ </td><td> $t$ </td><td> $k$ </td><td> $u$ </td></tr><tr><td> $u$ </td><td> $f$ </td><td> $u$ </td><td> $k$ </td></tr><tr><td> $f$ </td><td> $u$ </td><td> $t$ </td><td> $t$ </td></tr></table>

The truth values of some basic binary operators are introduced in Table 2 where the conjunction (resp. disjunction) is constructed as the lower bound (resp. upper bound) of the truth dimension.

One can remark that the implication is defined as follows:

$$
\alpha \rightarrow \beta \equiv \sim \alpha \vee \beta
$$

This is a strong implication of the type used in classic logic. The purpose of such an operator is to be a representation of inclusion. However, other weaker implications can be defined within this language.

Besides ordinary four valued sentences, in DDT it is possible to formulate bivalued sentences such as:

• $\Delta \alpha$ (there is presence of truth in α);

$\Delta \neg \alpha$ (there is presence of truth in ¬α);

• $T \alpha$ (α is true);

• Kα (α is contradictory);

• $U \alpha$ (α is unknown);

• Fα (α is false);

through the following formulas:

$$
\begin{array}{l} \text {- - } \Delta \alpha \equiv (\alpha \land \lnot \sim \alpha) \lor (\lnot \alpha \land \lnot \lnot \alpha) \\ \text {- - } T \alpha \equiv \alpha \land \lnot \sim \alpha \\ \text { It   is   easy   to   see   that: } \\ \text {- - } \Delta \alpha \equiv T (\alpha) \lor K (\alpha) \\ \text {- - } T \alpha \equiv \Delta \alpha \land \lnot \Delta \lnot \alpha . \end{array}
$$

Example 2.1. Why the above is a relevant language in decision aiding problems? Let us take the example of a Parliament which is preparing to vote for a new proposal ((r)) concerning an ethical issue. Members of the Parliament (MPs) can vote “for” or “against” this proposal or can “not vote”.

Table 2  
The truth of tables conjunction, disjunction and implication

<table><tr><td> $\wedge$ </td><td>t</td><td>k</td><td>u</td><td>f</td><td> $\vee$ </td><td>t</td><td>k</td><td>u</td><td>f</td><td> $\rightarrow$ </td><td>t</td><td>k</td><td>u</td><td>f</td></tr><tr><td>t</td><td>t</td><td>k</td><td>u</td><td>f</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>k</td><td>u</td><td>f</td></tr><tr><td>k</td><td>k</td><td>k</td><td>f</td><td>f</td><td>k</td><td>t</td><td>k</td><td>t</td><td>k</td><td>k</td><td>t</td><td>t</td><td>u</td><td>u</td></tr><tr><td>u</td><td>u</td><td>f</td><td>u</td><td>f</td><td>u</td><td>t</td><td>t</td><td>u</td><td>u</td><td>u</td><td>t</td><td>k</td><td>t</td><td>k</td></tr><tr><td>f</td><td>f</td><td>f</td><td>f</td><td>f</td><td>f</td><td>t</td><td>k</td><td>u</td><td>f</td><td>f</td><td>t</td><td>t</td><td>t</td><td>t</td></tr></table>

Table 3  
The truth table of example 1

<table><tr><td>Case</td><td> $V(\alpha)$ </td><td> $V(\neg\alpha)$ </td><td> $\Delta\alpha$ </td><td> $\Delta\neg\alpha$ </td><td>Value</td></tr><tr><td>1</td><td>75</td><td>20</td><td>1</td><td>0</td><td>True</td></tr><tr><td>2</td><td>48</td><td>40</td><td>0</td><td>1</td><td>False</td></tr><tr><td>3</td><td>60</td><td>40</td><td>1</td><td>1</td><td>Contradictory</td></tr><tr><td>4</td><td>41</td><td>25</td><td>0</td><td>0</td><td>unknown</td></tr></table>

Suppose that the Parliament has the following rule for adopting laws concerning ethics: a “strong” majority has to vote “for” (more than 51%) and no more than 1/3 can vote “against” (the last one is used in order to defend minorities).

This kind of voting can be captured by the four valued logic as in the following:

$$
\Delta \alpha = 1 \quad \text { iff } \quad \frac {V (\alpha)}{N} \geq 0. 5 1
$$

$$
\Delta \neg \alpha = 1 \quad \text { iff } \quad \frac {V (\neg \alpha)}{N} \geq 0. 3 3
$$

where N: number of MPs (let's suppose the parliament having 100 Mps) V(α): number of MPs voting for α, V (¬α): number of MPs voting against α.

Four different cases are presented in Table 3. In the first two cases there is no hesitation since in the first one the bill is clearly accepted, while in the second it is clearly rejected. In the third case, the majority of MPs are for the acceptance of the proposal but at the same time the number of MPs against (r) is remarkable too; the proposition will not be accepted, but it is clear that we are facing a conflict, a contradictory case. Finally, in the fourth case, the votes for and against (r) are insufficient to make a decision which is expressed here with the unknown value. From a decision aiding point of view, it is clear that the recommendation of an analyst towards a decision maker facing any of the above situations will be different. In the third case it is necessary to work towards the opposants (perhaps negotiating in order to meet some of their claims), while in the fourth case it is necessary to convince the “non voters” (perhaps strengthening the contents of the law). The reader can see further literature on similar voting schemes in Ref. [19].

Until this point we gave a brief presentation of DDT in terms of a propositional language. However, what we really need is a first order language (which DDT indeed is). We therefore need to go more in details with the relevant semantics for this purpose.

## 2.2. Semantics

The introduced logic deals with uncertainty. A set A may be defined, but the membership of an object a to the set may not be certain either because the information is not sufficient or because the information is contradictory.

In order to distinguish these two principal sources of uncertainty, the knowledge about the “membership” of a to A and the “non-membership” of a to A are evaluated independently since they are not necessarily complementary. From this point of view, from a given knowledge, we have two possible entailments, one positive, about membership and one negative, about non-membership. Therefore, any predicate is defined by two sets, its positive and its negative extension in the universe of discourse. Since the negative extension does not necessarily correspond to the complement of the positive extension of the predicate we can expect that the two extensions possibly overlap (due to the independent evaluation) and that there exist parts of the universe of discourse that do not belong to either of the two extensions. The four truth values capture these situations. More formally: Consider a first order language L. A similarity type $\rho$ is a finite set of predicate constants $R ,$ where each R has a finite arity $n _ { R } \leq \omega$ . Every alphabet uniquely determines a class of formulas. Relative to a given similarity type $\rho , R ( x _ { 1 } , . . . ,$ $x _ { m } )$ is an atomic formula iff $x _ { 1 } , . . . , x _ { m }$ are individual variables, $R \in \rho ,$ and $n _ { R } { = } m$ . In this paper, formulas are denoted by the letters α, $\beta , \gamma , \cdots ,$ , possibly subscripted.

A structure or model M for similarity type $\rho$ consists of a non-empty domain |M| and, for each predicate symbol $R \in \rho ,$ an ordered pair $R ^ { M } { = } \langle R ^ { M + } , R ^ { M - } \rangle$ of sets (not necessarily a partition) of $n _ { R } { \mathrm { - t u p l e s } }$ from $| M | .$ . In fact, an individual can be in the two sets or in neither of them. A variable assignment is a mapping from the set of variables to objects in the domain of the model. Capital letters from the beginning of the alphabet are used to represent variable assignments.

Example 2.2. Consider a language about preference statements using binary predicates (the preference relations) and a universe of discourse being the Cartesian product of a set A of candidates with itself. Traditionally when we write $p ( x , y )$ we read “x is preferred to y” and the semantics associated to this sentence is constructed taking pairs of candidates (instances of x and $y ,$ let's say a and $b )$ and checking whether it is indeed the case tha $^ { 6 6 } a$ is preferred to $b ^ { \dag }$ . All instances, for which it is the case, define the set of models of $p ( x , y )$ . Automatically the complement of this set with respect to the universe of discourse is the set of models of $\therefore p ( x , y )$ . The negation of a sentence coincides with its complement.

Let's use the DDT language in the above example. There might be pairs of instances of x and y (let's say a and b) for which we have information that “a is preferred to $b ^ { \dag }$ . There might also be other instances of x and y (let's say c and $d )$ for which we have information that $^ { 6 6 } c$ is not preferred to $d ^ { \ast }$ . The set of all $^ { ( a , b ) }$ will define the set of models of $\dot { p } ( x , y )$ , while the set of all $( c , d )$ will define the set of models of not $p ( x , y )$ . If we accept (that due to our imperfect knowledge) these two sets do not form a partition of the universe of discourse, then it is easy to note that there will be in the universe of discourse pairs for which we have both positive and negative information and pairs for which we have none.If we call the set of models of $\dot { p } ( x , y )$ its positive extension, denoting it as $P +$ and the set of models of not $p ( x , y )$ its negative extension, denoting it as $P - ,$ in the case of classic logic it is sufficient to know one of the above to completely know also the other (since one is the complement of the other). In the case of the DDT logic (and other four valued logics) we need to explicitly know both of them. In other terms the semantics of a sentence have to be defined through two sets (the positive and negative extension in the universe of discourse).

The truth definition for DDT is defined via two semantic relations, $\models _ { t }$ (true entailment) and $\models _ { f }$ (false entailment), by simultaneous recursion as in the following definition (due to the structure introduced, the case of “not true entailment” $\nvDash _ { t }$ does not coincide with the false entailment and the case of “not false entailment” $\nvDash _ { f }$ does not coincide with the true entailment). Each formula is univocally defined through its model which is however, a couple of sets, the “positive” and “negative” extensions of the formula.

Definition 2.1. Let $M$ be a model structure and A a variable assignment.

$$
- M \vDash_ {t} R (x _ {1}, \dots , x _ {n}) [ A ] \text {   iff   } \langle A (x _ {1}), \dots , A (x _ {n}) \rangle \in R ^ {M +}.
$$

$$
- M \vDash_ {f} R (x _ {1}, \dots , x _ {n}) [ A ] \text {   iff   } \langle A (x _ {1}), \dots , A (x _ {n}) \rangle \in R ^ {M -}.
$$

$$
- M \nexists_ {t} R (x _ {1}, \dots , x _ {n}) [ A ] \text {   iff   } \langle A (x _ {1}), \dots , A (x _ {n}) \rangle \in | M | R ^ {M +}.
$$

$$
M \neq_ {f} R (x _ {1}, \dots , x _ {n}) [ A ] \text {   iff   } \langle A (x _ {1}), \dots , A (x _ {n}) \rangle \in | M | R ^ {M -}.
$$

$$
- M \vDash_ {t} \neg \alpha [ A ] \text {   iff   } M \vDash_ {f} \alpha [ A ].
$$

$$
- M \vDash_ {f} \neg \alpha [ A ] \text {   iff   } M \vDash_ {t} \alpha [ A ].
$$

$$
- M \not \equiv_ {t} \neg \alpha [ A ] \text {   iff   } M \not \equiv_ {f} \alpha [ A ].
$$

$$
- M \not \models_ {f} \neg \alpha [ A ] \text {   iff   } M \not \models_ {t} \alpha [ A ].
$$

$$
- M \vDash_ {t} \sim \alpha [ A ] \text {   iff   } M \vDash_ {t} \alpha [ A ].
$$

$$
- M \vDash_ {f} \sim \alpha [ A ] \text {   iff   } M \not = _ {f} \alpha [ A ].
$$

$$
- M \not \equiv_ {t} \sim \alpha [ A ] \text {   iff   } M \not \equiv_ {t} \alpha [ A ].
$$

$$
- M \nVdash_ {f} \sim \alpha [ A ] \text {   iff   } M \vDash_ {f} \alpha [ A ].
$$

$- \ M \models _ { t } \forall x \alpha [ A ] \ \operatorname { i f f } \ M \models _ { t } \alpha [ A ^ { \prime } ]$ for all $A ^ { \prime }$ differing with A at most at x.

– M⊭ ∀ xα[A] iff M⊭ α[A′] for all $A ^ { \prime }$ differing with A at most at x.

– M⊨<sub>f</sub> ∀ xα[A] iff M⊨<sub>t</sub> α[A′] for an $A ^ { \prime }$ differing with A at most at x.

– M⊭<sub>f</sub> ∀ xα[A] iff M⊭<sub>t</sub> α[A′] for an $A ^ { \prime }$ differing with A at most at x.

It is now possible to introduce an evaluation function v(α) mapping $\mathcal { L }$ in to the set of truth values $\{ t , k , u , f \}$ as follows:

$$
- v (\alpha) = t \text {   iff   } M \vDash_ {t} \alpha [ A ] \text {   and   } M \nVdash_ {f} \alpha [ A ]
$$

$$
- v (\alpha) = k \text {   iff   } M \vDash_ {t} \alpha [ A ] \text {   and   } M \vDash_ {f} \alpha [ A ]
$$

$$
- v (\alpha) = u \text {   iff   } M \nVdash_ {t} \alpha [ A ] \text {   and   } M \nVdash_ {f} \alpha [ A ]
$$

$$
- v (\alpha) = f \text {   iff   } M \not \equiv_ {t} \alpha [ A ] \text {   and   } M \vDash_ {f} \alpha [ A ]
$$

Given any two subsets of formula α and $\beta ,$ we can now extend Definition 2.1 as follows:

$\alpha \mathsf { \Pi } { = } _ { t } \beta$ iff, for all variable assignments, $\mathrm { i f } M { \models } _ { t } \alpha [ { \bf A } ]$ then ${ M } | = { _ { t } } \beta [ \mathrm { A } ]$

$\alpha \mathsf { \Pi } \simeq _ { f } \beta$ iff, exists a variable assignment for which, $M { \models } _ { f } \beta { \lbrack \mathrm { A } ] } \ \mathrm { a n d } \ M { \ v \ L } \not = { \boldsymbol { \alpha } } { \ v { D } } { \ v { \alpha } } { \ v { \alpha } } { \ v { \alpha } } { \mathrm { I A } } ]$

$\alpha \sharp _ { t } \beta$ iff, exists a variable assignment for which, $M { \models } _ { t } \alpha { [ \boldsymbol { \mathrm { A } } ] } \ \mathrm { a n d } \ M { \ v \Leftarrow } _ { t } \beta { \ v \lbrack } \boldsymbol { \mathrm { A } } ]$

$\alpha \sharp _ { f } \beta$ iff, for all variable assignments, $\mathrm { i f } M { \models } _ { f } \beta { \ v { \left[ A \right] } }$ then $M { \ = } _ { f } \alpha [ \mathrm { A } ]$

We get:

Proposition 2.1. Given a non empty domain jMj and two sets of formula α and β

$$
\alpha \vDash_ {t} \beta i f f A ^ {M +} \subseteq B ^ {M +}
$$

$$
\alpha \vDash_ {f} \beta i f f B ^ {M -} \notin A ^ {M -}
$$

α⊭ β iff A<sup>M+</sup> ⊈ B<sup>M+</sup>

α⊭<sub>f</sub> β iff B<sup>M−</sup> ⊆A<sup>M−</sup>

Proof. Straightforward applying Definition 2.1.

Finally we can introduce the concept of strong consequence:

Definition 2.2. (Strong consequence.)

A formula α is true in a model M iff $M \mathbf { \bar { = } } _ { t } \alpha [ A ]$ and $M \not = \alpha [ A ]$ for all variable assignments A and we write $M \models \alpha \ [ A ]$ . A formula α is satisfiable iff α is true in a model Mfor some M. A set of formulas Γ is said to has as strong consequence or to strongly entail a formula α (written $\Gamma { \models { \alpha } } )$ when for all models Mand variable assignments A, if $M \models \beta _ { i } [ A ]$ , for all $\beta _ { i } \in I ,$ , then $M \models \alpha [ A ]$

Translating the above in set notation we get the following: consider a set A and a predicate S of finite arity n. Such a universe is partitioned into four subsets:

$$
S ^ {t} = S ^ {+} \cap \sim S ^ {-} S ^ {k} = S ^ {+} \cap S ^ {-}\tag{1}
$$

$$
S ^ {u} = \sim S ^ {+} \cap \sim S ^ {-} S ^ {f} = \sim S ^ {+} \cap S ^ {-}\tag{2}
$$

where $\sim S ^ { + } ( \sim S ^ { - } )$ is the complement of $S ^ { + } ( S ^ { - } )$ and ${ \boldsymbol { S } } ^ { t } ,$ $S ^ { k } , \ S ^ { u } , \ S ^ { f } ,$ represent the true, the contradictory, the unknown and the false extensions of the predicate S within the universe $A ^ { n }$ . Hence $\left( \neg S \right) ^ { + } , \left( \neg S \right) ^ { - } , \left( \sim S \right) ^ { + }$ and $\left( \sim S \right) ^ { - }$ are defined as follows:

$$
(\neg S) ^ {+} = S ^ {-} \quad (\neg S) ^ {-} = (S ^ {+})
$$

$$
(\sim S) ^ {+} = \sim (S ^ {+}) \quad (\sim S) ^ {-} = \sim (S ^ {-})
$$

Obviously the following hold:

$$
S ^ {t} \cup S ^ {k} = S ^ {+} S ^ {f} \cup S ^ {k} = S ^ {-}\tag{3}
$$

$$
S ^ {t} \cup S ^ {u} = \sim S ^ {-} S ^ {f} \cup S ^ {u} = \sim S ^ {+}\tag{4}
$$

$$
S ^ {t} = (\neg S) ^ {f} = (\sim S) ^ {f}
$$

$$
S ^ {k} = (\neg S) ^ {k} = (\sim S) ^ {u}
$$

$$
S ^ {u} = (\neg S) ^ {u} = (\sim S) ^ {k}
$$

$$
S ^ {f} = (\neg S) ^ {t} = (\sim S) ^ {t}
$$

$$
S ^ {t} \cup S ^ {k} \cup S ^ {u} \cup S ^ {f} = A ^ {n}
$$

$$
S ^ {t} \cap S ^ {k} = S ^ {t} \cap S ^ {u} = 0
$$

$$
S ^ {t} \cap S ^ {f} = S ^ {f} \cap S ^ {k} = S ^ {f} \cap S ^ {u} = S ^ {k} \cap S ^ {u} = 0
$$

## 2.3. Continuous extension

For the continuous extension of the previously introduced four valued logic, $S ^ { + }$ and $S ^ { - }$ can be considered as fuzzy subsets and two membership functions can be introduced (for a fixed domain M):

$$
\mu_ {S ^ {+}}: M \rightarrow [ 0, 1 ] \quad \mu_ {S ^ {-}}: M \rightarrow [ 0, 1 ]
$$

Such functions can be considered for instance as degrees representing to what extent we believe in $S ( x )$ and in non $S ( x )$ respectively (X representing a universe of discourse). Such an interpretation can be represented by the following notation:

$$
\mu_ {S ^ {+}} (\alpha) = B (\alpha) \quad \mu_ {S ^ {-}} (\alpha) = B (\neg \alpha)
$$

We then have to define the fuzzy subsets $S ^ { t } , S ^ { k } , S ^ { u } , S ^ { f } .$ The membership functions of such subsets can be respectively denoted by:

$$
\mu_ {S ^ {t}} (\alpha) = t (\alpha) \quad \mu_ {S ^ {k}} (\alpha) = k (\alpha)
$$

$$
\mu_ {S ^ {u}} (\alpha) = u (\alpha) \mu_ {S ^ {f}} (\alpha) = f (\alpha)
$$

## 2.3.1. Basic operators on B( )

We have to make explicit the intersection, the union and the complementation to fuzzy subsets of X in order to establish relations between the positive and negative reasons (B(α), B(¬α)) and the four fuzzy membership functions. To define these operators, we introduce a De Morgan triple (N,T,V) where N is a strict negation on [0,1], T a continuous t-norm and V is a continuous conorm such that $V ( x , y ) { = } N ( T ( N ( x ) { , } N ( y ) ) )$ . Fuzzyfing Eqs. (1), (2) and (3) we obtain:

$$
B (\alpha) = V (t (\alpha), k (\alpha)) \quad B (\neg \alpha) = V (N (t (\alpha)), k (\alpha))
$$

$$
\begin{array}{l} t (\alpha) = T (B (\alpha), N (B (\neg \alpha))) \\ u (\alpha) = T (N (B (\alpha)), N (B (\neg \alpha))) \end{array}
$$

$$
\begin{array}{c} k (\alpha) = T (B (\alpha), B (\neg \alpha)) \qquad f (\alpha) \\ = T (N (B (\alpha)), B (\neg \alpha)) \end{array}
$$

As a consequence we should get:

$$
\forall \alpha , B (\alpha) = V (T (B (\alpha), N (B (\neg \alpha))), T (B (\alpha), B (\neg \alpha)))
$$

Supposing that B(α) = x and $B ( \lnot \alpha ) { = } y _ { \ l }$ , the last equation can be written as follows:

$$
\forall x, y \in [ 0, 1 ], x = V (T (x, N (y)), T (x, y))
$$

Unfortunately, there is generally no De Morgan triple satisfying such an equation (see Ref. [1]). Thus, we have to investigate partial solutions relaxing some constraints of the problem. The idea is to use different t-norms for different quantities [see also Ref. 22]. Following [28] the four truth values can be defined through B(α) and B (¬α) as follows:

$$
t (\alpha) = T _ {1} (B (\alpha), N (B (\neg \alpha)))\tag{5}
$$

$$
k (\alpha) = T _ {2} (B (\alpha), (B (\neg \alpha)))\tag{6}
$$

$$
u (\alpha) = T _ {3} (N (B (\alpha)), N (B (\neg \alpha)))\tag{7}
$$

$$
f (\alpha) = T _ {4} (N (B (\alpha)), (B (\neg \alpha)))\tag{8}
$$

where $B ( \alpha ) + N ( B ( \alpha ) ) = 1$ and $T _ { 1 } , ~ T _ { 2 } , ~ T _ { 3 } , ~ T _ { 4 }$ are continuous t-norms. The following step is to decide which t-norms will be used for $T _ { 1 } , T _ { 2 } , T _ { 3 } , T _ { 4 }$ . For this purpose, we propose a number of conditions:

• the definition of fuzzy partition must be fulfilled:

$$
\forall \alpha , t (\alpha) + k (\alpha) + u (\alpha) + f (\alpha) = 1\tag{9}
$$

• the fuzzyfication of the definitions of strong and weak negation and complementation presented in Table 1 must be satisfied:

$$
t (\alpha) = f (\neg \alpha) = f (\sim \alpha) = k (\not \sim \alpha)\tag{10}
$$

$$
k (\alpha) = k (\neg \alpha) = u (\sim \alpha) = t (\not \sim \alpha)\tag{11}
$$

$$
u (\alpha) = u (\neg \alpha) = k (\sim \alpha) = f (\not \sim \alpha)\tag{12}
$$

$$
f (\alpha) = t (\neg \alpha) = t (\sim \alpha) = u (\not \sim \alpha)\tag{13}
$$

• the fuzzyfication of Eqs. (3) and (4) which represent relations betweenpositive and negative reasons and four values must be satisfied:

$$
B (\alpha) = V (t (\alpha), k (\alpha))\tag{14}
$$

$$
B (\neg \alpha) = V (f (\alpha), k (\alpha))\tag{15}
$$

• the contradictory and unknown cases must be exclusive:

$$
\forall \alpha , \min \{u (\alpha), k (\alpha) \} = 0.\tag{16}
$$

Proposition 2.2. $\langle T _ { I } , \ T _ { 2 } , \ T _ { 3 } , \ T _ { 4 } , \ T , \ V , \ N \rangle$ is solution of Eqs. (9)–(16) if and only if the following conditions hold:

$$
N = L N _ {\varphi} \quad T _ {2} = T _ {3} = L T _ {\phi}
$$

$$
V = L V _ {\phi} \quad T _ {1} = T _ {4} = \min
$$

where $( L N _ { \phi } , L T _ { \phi } , L V _ { \phi } )$ is the Lukasiewicz triple [see Ref. 33].

Proof. See Appendix A. Similar proofs can be also seen in Refs. [13,41,42].

For the sake of simplicity we only interpret here the case where $\phi \ ( x ) = x ; \forall x \in [ 0 , 1 ]$ . We thus get

Corollary 2.1.

$$
t (\alpha) = \min (B (\alpha), 1 - B (\neg \alpha))\tag{17}
$$

$$
k (\alpha) = \max (B (\alpha) + B (\neg \alpha) - 1, 0)\tag{18}
$$

$$
u (\alpha) = \max (1 - B (\alpha) - B (\neg \alpha), 0)\tag{19}
$$

$$
f (\alpha) = \min (1 - B (\alpha), B (\neg \alpha))\tag{20}
$$

Proof. Straightforward from Eqs. (10)–(13) and Proposition 2.2.

Corollary 2.2.

$$
B (\alpha) = t (\alpha) + k (\alpha)\tag{21}
$$

$$
B (\neg \alpha) = f (\alpha) + k (\alpha)\tag{22}
$$

Proof. Applying Proposition 2.2 on Eq. (14) we get:B $( \alpha ) { = } \operatorname* { m i n } ( t ( \alpha ) { + } k ( \alpha ) , 1 )$ . Since $t ( \alpha ) + k ( \alpha ) + u ( \alpha ) + f ( \alpha ) = 1$ we have that $t ( \alpha ) + k ( \alpha ) \leq 1$ .Therefore $B ( \alpha ) { = } t ( \alpha ) { + } k ( \alpha )$ Similarly $B ( \neg \alpha ) { = } f ( \alpha ) + k ( \alpha )$

We can now define some basic operators like negation, complementation, conjunction, disjunction, implication and equivalence.

For this purpose we represent each formula α by $\left. \alpha , \ ( B ( \alpha ) , B ( \lnot \alpha ) ) \right.$ 〉 where $( B ( \alpha ) , \ B ( \neg \alpha ) )$ is an ordered pair.

In order to define negations and complementation, we make use of their interpretation in crisp case (see Subsection 2.1) and we obtain:

$$
\langle \neg \alpha , (B (\neg \alpha), B (\alpha)) \rangle\tag{23}
$$

$$
\langle \prec \alpha , (B (\alpha), 1 - B (\neg \alpha)) \rangle\tag{24}
$$

$$
\langle \sim \alpha , (1 - B (\alpha), 1 - B (\neg \alpha)) \rangle\tag{25}
$$

The conjunction (resp. the disjunction) corresponds —as in crisp case—to the lower bound (resp. the upper bound) of $\propto$ and $\beta .$

$$
\langle \alpha \wedge \beta , (T _ {1} (B (\alpha), B (\beta)), V _ {1} (B (\neg \alpha), B (\neg \beta))) \rangle\tag{26}
$$

$$
\langle \alpha \vee \beta , (V _ {2} (B (\alpha), B (\beta)), T _ {2} (B (\neg \alpha), B (\neg \beta))) \rangle\tag{27}
$$

where T =min, V =max, i=1, 2.

Remark 2.1. We presented here definitions of operators in terms of belief degrees $( B ( \alpha ) , B ( \neg \alpha ) )$ . The same definitions are given in terms of four values in Ref. [28]. Let's remark that Eqs. (14), (15) make the passage from the one to the other easy and provide equivalent definitions. In order to give an example, we show how to compute $k ( \alpha \lor \beta )$ ):

$$
k (\alpha \wedge \beta) = \max (B (\alpha \wedge \beta) + B (\neg (\alpha \wedge \beta)) - 1, 0)
$$

$$
\begin{array}{c} k (\alpha \wedge \beta) = \max [ \min (B (\alpha), B (\beta)) \\ + \max (B (\neg \alpha), B (\neg \beta)) - 1, 0 ] \end{array}
$$

$$
\begin{array}{c} k (\alpha \wedge \beta) = \max [ \min (B (\alpha), B (\beta)) \\ - \min (1 - B (\neg \alpha), 1 - B (\neg \beta)), 0 ] \end{array}
$$

$$
\begin{array}{c} k (\alpha \wedge \beta) = \max [ \min (B (\alpha), B (\beta)) \\ - \min (1 - B (\neg \alpha), 1 - B (\neg \beta)), 0 ] \end{array}
$$

$$
\begin{array}{l} k (\alpha \wedge \beta) = \max [ \min (t (\alpha) + k (\alpha), t (\beta) \\ \qquad + k (\beta)) - \min (t (\alpha) + u (\alpha), t (\beta) + u (\beta)), 0 ] \end{array}
$$

As far as implication is concerned a simple “fuzzyfication” of the definition of this operator in the DDT logic is not sufficient. Remind that in DDT $\alpha { \longrightarrow } \beta { \equiv } \sim \alpha \wedge \beta .$ Although DDT is based on a Boolean algebra its continuous extension is not. DDT is established on a four elements set partially ordered through the bi-lattice introduced in Section 2.1. Its continuous extension is established on a continuous space of infinite values and therefore cannot be a Boolean algebra. Therefore not all operators can be compositional. Since for the purpose of this paper a detailed treatment of implication is not necessary, we are not going to analyse further this issue.

We conclude this part by a generalisation of inference. One can define modus ponens as in the following:

$$
\begin{array}{c}\langle \alpha (B (\alpha), B (\neg \alpha)) \rangle\\\frac {\langle \alpha \rightarrow \beta , (B (\alpha \rightarrow \beta) , B (\neg (\alpha \rightarrow \beta))) \rangle}{\langle \beta , (B (\beta) , B (\neg \beta)) \rangle}\\\text { where } B (\beta) = \min (B (\alpha), B (\alpha \rightarrow \beta)); B (\neg \beta) = \max (B (\neg \alpha),\\B (\neg (\alpha \rightarrow \beta))).\end{array}
$$

The interested reader can find more details about operators in Ref. [28].

How can the continuous extension of the four valued logic be useful in decision aiding situations? The following example shows why distinguishing between continuous positive and negative reasons can be interesting in decision aiding. Typically it will allow to provide the client of the decision aiding process with more operational recommendations.

Example 2.3. We choose again as an example the case of a Parliament which is preparing to vote for a new proposal (α) concerning an ethical issue. Members of the Parliament (MPs) can vote “for” or “against” this proposal or can “not vote” but this time we are going to value the positive and negative reasons within the [0,1] interval. Since a majority is needed, positive reasons become strictly positive when at least 50% of the MPs vote “for” and become sure (equal to 1) when at least 80% vote “for”. Negative reasons are used especially in order to defend minority, that is why they become strictly positive when at least 15% vote “against” and become sure (equal to 1) when at least 35% vote “against”. The model is shown in Fig. 2.

Table 4  
![](/api/attachments/G89EW5VE/fulltext/images/c09ac470076e2e9d61edbd0454188949b694a058b26613784b4e593831051412.jpg)  
Fig. 2. B(α) and B(¬α) for Example 2.

In Table 4 we show the simulation of a number of votes on a set of issues. How can the decomposition in positive and negative reasons help a decision maker?

First of all it is easy to observe that (with that precise decision rule) negative reasons grow faster than positive ones.

After a deep analysis of Table 4 we can make the following comments: Cases 1 to 3 show that convincing two non voters to vote $\mathrm { ^ { 6 6 } f o r ^ { 5 9 } }$ will not improve acceptability (t(a)), while convincing two opponents to not vote will do. Cases 4 and 5 show how acceptability and opposition will change due to opinion shifts from “for” to “against” when there are no “non voters”. Cases 6 to 10 show the appearance of hesitation due to ignorance or conflict. The analysis of the positive and negative reasons helps in showing to a decision maker in what direction he should concentrate his efforts in order to pursue his policy.

The truth table for example 2

<table><tr><td>Case</td><td> $V(a)$ </td><td> $V(\neg a)$ </td><td> $B(a)$ </td><td> $B(\neg a)$ </td><td> $t(a)$ </td><td> $k(a)$ </td><td> $u(a)$ </td><td> $f(a)$ </td></tr><tr><td>1</td><td>75</td><td>20</td><td>0.83</td><td>0.25</td><td>0.75</td><td>0.08</td><td>0</td><td>0.17</td></tr><tr><td>2</td><td>75</td><td>18</td><td>0.83</td><td>0.15</td><td>0.83</td><td>0</td><td>0.02</td><td>0.15</td></tr><tr><td>3</td><td>77</td><td>20</td><td>0.9</td><td>0.25</td><td>0.75</td><td>0.15</td><td>0</td><td>0.1</td></tr><tr><td>4</td><td>82</td><td>18</td><td>1</td><td>0.15</td><td>0.85</td><td>0.15</td><td>0</td><td>0</td></tr><tr><td>5</td><td>78</td><td>22</td><td>0.93</td><td>0.35</td><td>0.65</td><td>0.28</td><td>0</td><td>0.07</td></tr><tr><td>6</td><td>58</td><td>26</td><td>0.26</td><td>0.55</td><td>0.26</td><td>0</td><td>0.19</td><td>0.55</td></tr><tr><td>7</td><td>58</td><td>17</td><td>0.26</td><td>0.1</td><td>0.26</td><td>0</td><td>0.64</td><td>0.1</td></tr><tr><td>8</td><td>58</td><td>35</td><td>0.26</td><td>1</td><td>0</td><td>0.26</td><td>0</td><td>0.74</td></tr><tr><td>9</td><td>68</td><td>26</td><td>0.6</td><td>0.55</td><td>0.45</td><td>0.15</td><td>0</td><td>0.4</td></tr><tr><td>10</td><td>68</td><td>17</td><td>0.6</td><td>0.1</td><td>0.6</td><td>0</td><td>0.3</td><td>0.1</td></tr></table>

## 2.3.2. Other approaches about B( )

The idea of having two separate measures for beliefs and disbeliefs is not new. Ref. [34] talks about confidence and diffidence measures as two separable components of a belief function. However, in his approach these components are commensurable (thus computable through a generalised Dempster rule). This is not the case of $B ( \alpha )$ and $B ( \neg \alpha )$ which do not need such an assumption. Ref. [18] introduce the concept of guaranteed possibility as a further uncertainty measure, different with respect to the usual possibility measures. These two distributions can be seen as upper and lower approximations of a not well known possibility distribution. They do not represent though independent positive and negative reasons concerning the belief to a sentence. Nearest to our approach can be considered the Transferable Belief Model [see Ref. 35] which allows measures of contradiction.

On the other hand our continuous extension of a four valued logic is not the unique approach followed in the literature. Ref. [23] have also presented a different extension within the context of preference modelling. The major difference between these two approaches is the fact that Fortemps and Slowi´nski's one does not provide a fuzzy partition of the universe of discourse.

In their approach, positive an negative reasons are presented by two independent necessity degrees, $\mathcal { N } _ { T }$ and $\mathcal { N } _ { F }$ which they call degrees of truthfulness and falsity respectively. Using our notation $\left. \alpha , ( \mathcal { N } _ { T } ( \alpha ) , \mathcal { N } _ { F } ( \alpha ) ) \right.$ , we can mention that $\mathcal { N } _ { T } ( \mathrm { r e s p . } \mathcal { N } _ { F } )$ corresponds to our fuzzy membership function $\mu _ { S + } ( \mathrm { r e s p . ~ } \mu _ { S - } )$

Their interpretation of negations, complementation, conjunction and disjunction is very similar to ours:

$$
\langle \neg \alpha , (\mathcal {N} _ {F} (\alpha), \mathcal {N} _ {T} (\alpha)) \rangle
$$

$$
\langle \prec \alpha , (\mathcal {N} _ {T} (\alpha), 1 - \mathcal {N} _ {F} (\alpha)) \rangle
$$

$$
\langle \sim \alpha , (1 - \mathcal {N} _ {T} (\alpha), 1 - \mathcal {N} _ {F} (\alpha)) \rangle
$$

$$
\langle \alpha \wedge \beta , (\min (\mathcal {N} _ {T} (\alpha), \mathcal {N} _ {T} (\beta)), \max (\mathcal {N} _ {F} (\alpha), \mathcal {N} _ {F} (\beta)) \rangle
$$

$$
\langle \alpha \vee \beta , (\max (\mathcal {N} _ {T} (\alpha), \mathcal {N} _ {T} (\beta)), \min (\mathcal {N} _ {F} (\alpha), \mathcal {N} _ {F} (\beta))) \rangle
$$

They define four values in an ordinal way:

$$
t (\alpha) = \min (\mathcal {N} _ {T} (\alpha), 1 - \mathcal {N} _ {F} (\alpha))\tag{28}
$$

$$
k (\alpha) = \min (\mathcal {N} _ {T} (\alpha), \mathcal {N} _ {F} (\alpha))\tag{29}
$$

$$
u (\alpha) = \min (1 - \mathcal {N} _ {T} (\alpha), 1 - \mathcal {N} _ {F} (\alpha))\tag{30}
$$

$$
f (\alpha) = \min (1 - \mathcal {N} _ {T} (\alpha), \mathcal {N} _ {F} (\alpha))\tag{31}
$$

The use of purely ordinal definition for the four values has some advantages, especially in the case when only ordinal data are needed, but presents some drawbacks. Some of the properties that we think interesting for decision aiding purposes are not satisfied:

• the four values defined as in Eqs. (28)–(31) do not provide a fuzzy partition of the domain:

$$
\exists \alpha , t (\alpha) + k (\alpha) + u (\alpha) + f (\alpha) \neq 1
$$

• contradictory and unknown cases are not exclusive:

$$
\exists \alpha , k (\alpha) > 0 \text { and } u (\alpha) > 0
$$

Supposing that unknown case represents a lack of information and contradictory case an excess of information, it is difficult to interpret a case where the unknown and contradictory values are both different from zero.

• it is not possible to rebuild the value of $N _ { T }$ or $N _ { F }$ from four values, for example:

$$
\begin{array}{l} \mathcal {N} _ {T} (\alpha) \neq t (\alpha) + k (\alpha) \\ \mathcal {N} _ {F} (\alpha) \neq f (\alpha) + k (\alpha) \end{array} .
$$

## 2.3.3. Nature of B( )

What do B(α) (and B(¬α)) intuitively represent? First of all they can be seen as membership functions. Since for any sentence α we consider that there exist two extensions, the positive and the negative one, we can imagine that to any such sentence it is possible to associate two fuzzy sets, one representing its membership to the positive examples and the other representing its membership to the negative examples.

We can see these two membership functions as the fuzzy counterpart of the $\Delta ( \alpha )$ (respectively $\Delta ( \neg \alpha ) )$ in DDT logic. These formulas represent the presence of truth in sentence α (respectively :α). In other terms these formulas can be considered as the positive (negative) reasons for which α holds.

To some extend B(α) and B(¬α) try to “measure” how strong are such positive and negative reasons. Intuitively B(α) − 0 should be interpreted as “there are no positive reasons at all”, while $B ( \lnot \alpha ) - 1$ should be understood as “negative reasons are the strongest possible”. The reasons, for which the strength of positive and negative reasons can be continuous, are twofold:

— either because of the quality of the available information (reliability of our information sources, quantity of information, presence and dimension of measurement errors, etc.);

— or because of the use of ill-defined concepts (through linguistic variables) such as “young”, “heavy”, etc. [the reader can see more in this issue in Ref. 17].

A general approach could be to consider them as capacities. One can define a capacity on a set Ω as follows [11,25]:

Definition 2.3. (Capacity)

Suppose that υ: $2 ^ { \bar { \Omega } } {  } \bar { \mathbb { R } } ^ { + }$ is a set function, then υ is a capacity if and only if the following conditions are satisfied $( A , B \subseteq \varOmega )$

1. υ(0) = 0 (boundary condition), and

2. if A ⊆ B then υ(A) ≤ υ(B) (monotonicity condition)

In addition, if υ(Ω) = 1 then the capacity is normalised.

Let us remark that probabilities are normalised capacities with additive conjunction. If B(α) is seen as the probability $P ( \alpha )$ , we will have $B ( \alpha ) + B ( \lnot \alpha ) = P ( \alpha ) +$ $P ( \neg \alpha ) { = } 1$ and therefore:

$$
t (\alpha) = P (\alpha) \quad k (\alpha) = 0
$$

$$
u (\alpha) = 0 \qquad f (\alpha) = 1 - P (\alpha)
$$

It is easy to note that interpreting B(α) as a probability, although possible in principle, contradicts the hypothesis that positive and negative reasons are not complementary and commensurable. Therefore normally it should not be the case that we can write something like $B ( \alpha ) + B ( \lnot \alpha ) = 1$ . An alternative could be to consider B(α) as a necessity measure, since this type of capacity does not impose complementarity with the negation.

## 3. (α) as a standard necessity

In this section we first briefly recall some definitions of possibility theory which will be useful for the rest of the paper (the reader can see more details in Ref. [16]). Possibility measures are expected to provide an ordinal representation of uncertainty as follows:

## Definition 3.1. Possibility measure

Given a set of events Ω, a possibility measure Π is a function defined on the power set $2 ^ { \mathcal { Q } } , \mathsf { \bar { ( } } \Pi : 2 ^ { \mathcal { Q } } \mathrm {  } [ 0 , 1 ] )$ such that:

$$
\begin{array}{l} 1. \Pi (0) = 0, \Pi (\varOmega) = 1 \\ 2. A \subseteq B \in 2 ^ {\varOmega} \to \Pi (A) \leq \Pi (B) \\ 3. \forall A, B \in 2 ^ {\varOmega}, \Pi (A \cap B) = \max (\Pi (A), \Pi (B)) \end{array}
$$

The dual of the possibility measure, denoted necessity measure is defined as N(a) = 1 − Π(¬a).

## Definition 3.2. Necessity measure

Given a set of events Ω, a necessity measure Nis a function defined on the power set $2 ^ { \mathcal { Q } } , \mathring { ( N : 2 ^ { \mathcal { Q } } \longrightarrow [ 0 , 1 ] ) }$ such that:

$$
\begin{array}{l} 1. N (0) = 0, N (\Omega) = 1, \\ 2. A \subseteq B \in 2 ^ {\Omega} \to N (A) \leq N (B) \\ 3. \forall A, B \in 2 ^ {\Omega}, N (A \cap B) = \min (N (A), N (B)) \end{array}
$$

Let's remark that the disjunction of the necessity measure and the conjunction of the possibility measure are not compositional:

$$
\begin{array}{c} N (\alpha \lor \beta) \geq \max (N (\alpha), N (\beta)) \\ \Pi (\alpha \land \beta) \leq \min (\Pi (\alpha), \Pi (\beta)) \end{array}\tag{32}
$$

As a result, we obtain the following properties:

$$
\Pi (\alpha) \geq N (\alpha) \max (\Pi (\alpha), \Pi (\neg \alpha)) = 1\tag{33}
$$

$$
\begin{array}{l l} \text {   If   } & N (\alpha) \neq 0, \qquad \text {   then   } \qquad \Pi (\alpha) = 1 \\ \text {   If   } & \Pi (\alpha) \neq 1, \qquad \text {   then   } \qquad N (\alpha) = 0 \end{array}\tag{34}
$$

By definition we can consider a possibility measure as the upper bound of the uncertainty associated to an event (or a sentence), the one carrying the less specific information. Dually the necessity measure will represent the lower bound: how sure we are about an event (or a sentence). Clearly three extreme situations are possible:

$$
\begin{array}{l} \text {- - } N (\alpha) = 1; N (\neg \alpha) = 0,   \alpha \text { is the case;} \\ \text {- - } N (\alpha) = 0; N (\neg \alpha) = 1,   \neg \alpha \text { is the case;} \\ \text {- - } N (\alpha) = 0; N (\neg \alpha) = 0, \text { nothing is sure and everything } \\ \text { is possible. } \end{array}
$$

A first attempt to interpret the continuous valuation of “presence of truth in $\alpha ^ { \ast }$ and “presence of truth in $\neg { \alpha } ^ { \mathfrak { n } }$ could be to consider them as necessity measures. Coming back to our notation, we consider $B ( \alpha )$ , as a standard necessity; as a consequence we have:

$$
\begin{array}{c} B (\alpha) = N (\alpha) = 1 - \Pi (\neg \alpha), \\ B (\neg \alpha) = N (\neg \alpha) = 1 - \Pi (\alpha) \end{array}
$$

Hence, we obtain the following definitions:

$$
t (\alpha) = \min (N (\alpha), \Pi (\alpha))\tag{35}
$$

$$
k (\alpha) = \max (N (\alpha) - \Pi (\alpha), 0)\tag{36}
$$

$$
u (\alpha) = \max (\Pi (\alpha) - N (\alpha), 0)\tag{37}
$$

$$
f (\alpha) = \min (\Pi (\neg \alpha), N (\neg \alpha))\tag{38}
$$

However, since Π(α) > N(α) we can reformulate the Eqs. (35)–(38):

$$
\begin{array}{l} t (\alpha) = N (\alpha) \\ k (\alpha) = 0 \\ u (\alpha) = \Pi (\alpha) - N (\alpha) \\ f (\alpha) = N (\neg \alpha) = 1 - \Pi (\alpha) \end{array}
$$

We first observe that interpreting B(α) as a standard necessity measure leads to k(α) = 0. This is not surprising given the semantics of necessity. Let us study separately the two situations, N(α) > 0 and N (α) = 0:

<table><tr><td>When  $N(\alpha) > 0$ , we get:</td><td>When  $N(\alpha) = 0$ , we get:</td></tr><tr><td> $t(\alpha) = N(\alpha)$ </td><td> $t(\alpha) = k(\alpha) = 0$ </td></tr><tr><td> $k(\alpha) = f(\alpha) = 0$ </td><td> $u(\alpha) = \Pi(\alpha)$ </td></tr><tr><td> $u(\alpha) = \Pi(\neg \alpha)$ </td><td> $f(\alpha) = N(\neg \alpha)$ </td></tr></table>

In other terms it appears that, while the necessity measure represents the “trueness” of a sentence (or, exclusively, of its negation), the possibility measure represents the “unknownness” of the same sentence.

There are two different ways to define the usual logical operators. In order to present them we give an example. We consider here the case of conjunction for which there exist two different ways of definition. Each way is denoted by index $i , i { = } 1 , 2$ . Unfortunately the results in the two cases are different:

• The first one consists in using directly the definition of conjunction of our continuous extension given in Eq. (26):

$$
\begin{array}{l} \langle \alpha \wedge_ {1} \beta , (\min (B (\alpha), B (\beta)), \max (B (\neg \alpha), B (\neg \beta))) \rangle \\ \qquad = \langle \alpha \wedge_ {1} \beta , (\min (N (\alpha), N (\beta)), \max (N (\neg \alpha), \\ N (\neg \beta))) \rangle = \langle \alpha \wedge_ {1} \beta , (\min (N (\alpha), N (\beta)), \max (1 - \Pi (\alpha), \\ 1 - \Pi (\beta))) \rangle = \langle \alpha \wedge_ {1} \beta , (\min (N (\alpha), N (\beta)), \\ 1 - \min (\Pi (\alpha), \Pi (\beta))) \rangle \end{array}
$$

• The second one consists in using the definition of conjunction and disjunction of possibility theory presented in Definition 3.2 and in Eq. (32):

$$
\begin{array}{l} \langle \alpha \wedge_ {2} \beta , (B (\alpha \wedge \beta), B (\neg (\alpha \wedge \beta))) \rangle \\ = \langle \alpha \wedge_ {2} \beta , (N (\alpha \wedge \beta), N (\neg (\alpha \wedge \beta))) \rangle \\ = \langle \alpha \wedge_ {2} \beta , (N (\alpha \wedge \beta), 1 - \Pi (\alpha \wedge \beta)) \rangle \\ = \langle \alpha \wedge_ {2} \beta , (\min (N (\alpha), N (\beta))), 1 - \Pi (\alpha \wedge \beta)) \rangle \end{array}
$$

It is easy to check that these two definitions are not equivalent. Negative reasons of the second definition are greater than the first one's. $\Pi ( \alpha \lor \beta ) { \leq } \operatorname* { m i n } ( \Pi ( \alpha )$ 4 Π(β)).

Similar results may be obtained for other operators like disjunction, implication and equivalence. Although this approach is consistent with possibility theory, it has some weak points:

presence of truth and “trueness” are practically equivalent;

— there is no way to consider contradictory statements;

— there are several compositional problems.

## 4. (α) as a sub-normalised necessity measure

An important feature of four valued logics is the separation of negation from complementation. Possibility theory does not make any difference between these two operators since it has been conceived as an uncertainty measure to be associated to classic logic. In this section, we suggest the idea of associating an uncertainty measure to a formalism such as DDT and study the consequences. In order to do that we recall the use of the “weak negation” ≁ (to be read as “perhaps”) of DDT logic (see Subsection 2.1). We remind that such a weak negation is conceived so that the complement of a sentence $" \alpha > $ can be established as $5 6  x  x 0 ^ {  }$ Finally we remind that for each sentence α we have the distribution $\langle \alpha , B ( \alpha ) , B ( \neg \alpha ) \rangle$ 〉.

We denote the dual measure of B as H $( H ( \alpha ) = 1 - B$ $( \neg \alpha ) )$ so that for each sentence α we have the new distribution $\langle \alpha , H ( \alpha ) , H ( \neg \alpha ) \rangle$ 〉. From Eq. (9) and recalling that $B ( \neg \alpha ) { = } f ( \alpha ) + k ( \alpha )$ we get that:

$$
H (\alpha) = t (\alpha) + u (\alpha)
$$

Proposition 4.1. Consider two dual uncertainty distributions on a set Ω: B(x) and H(x), applied on the language DDT, such that Eqs. (9)–(16) are satisfied. Then $\forall x \in \mathcal { Q } B ( x ) = H ( \neg \sim x )$

Proof. Recall that $\scriptstyle H ( \alpha ) = t ( \alpha ) + u ( \alpha )$

From Eqs. (10)–(13) and the definitions of the DDT logic we have:

$$
\begin{array}{l} - t (\alpha) = f (\sim \alpha) = f (\neg \not \sim \neg \not \sim \alpha) = t (\not \sim \neg \not \sim \alpha) = t (\neg \sim \alpha); \\ - u (\alpha) = k (\sim \alpha) = k (\neg \not \sim \neg \not \sim \alpha) = k (\not \sim \neg \not \sim \alpha) = k (\neg \sim \alpha); \end{array}
$$

Therefore, H(α) = t(¬ ∼ α) + k(¬ ∼ α).

In other terms the dual measure of B is equal to the measure of the negation of the complement. It is easy to extend the result of Proposition 4.1 to all formula as results in Table 5.

Table 5 shows that the introduction of the weak negation reduces the dual measures of the type necessity/possibility to a single one. Indeed we just need to know one of the uncertainty measures of a sentence and of its negation in order to know all about the uncertainty associated to this sentence. Let us remark that in standard possibility theory, there is only an ordinal relation between necessity and possibility $( \forall \alpha , \pi ( \alpha ) \ge N ( \alpha ) )$ which does not permit to rebuild one in terms of the other one.

Further on, let us consider the first column of Table 5. If we consider that only one uncertainty distribution is defined (say B) there is no reason to claim that $B ( \lnot \sim \alpha ) =$ $B ( \not \sim \neg \not \sim \alpha ) { > } B ( \alpha )$ (the uncertainty associated to the complement of the negation of a sentence is not necessarily larger than the uncertainty associated to the sentence itself; they should be unrelated). However, since $B ( { \not \sim } \neg { \not \sim } \alpha ) { = } H ( \alpha )$ , if the relation $H ( \alpha ) { > } B ( \alpha )$ does not hold we are practically relaxing the normalisation principle of uncertainty measures used in the possibility theory $( I I ( \alpha ) \not \gg N ( \alpha ) )$ . Approaches which make use of such relaxation of possibility measures exist in the literature and in such cases the necessity degree is generally called sub-normalised in order to differentiate them for classical possibility measures which are normalised in the interval [0,1]. [9]. What we see is that, while it is difficult to justify such distributions in a pure possibility theory frame, the use of the DDT logic allows to give a logical justification for their existence.

Equivalence between B and H

<table><tr><td> $B(\alpha)$ </td><td> $=B(\neg\alpha)$ </td><td> $=H(\neg\neg\neg\alpha)$ </td><td> $=H(\neg\neg\alpha)$ </td></tr><tr><td> $B(\neg\alpha)$ </td><td> $=B(\neg\neg\alpha)$ </td><td> $=H(\neg\neg\neg\neg\alpha)$ </td><td> $=H(\neg\alpha)$ </td></tr><tr><td> $B(\neg\neg\neg\neg\alpha)$ </td><td> $=B(\neg\neg\neg\alpha)$ </td><td> $=H(\neg\alpha)$ </td><td> $=H(\neg\neg\alpha)$ </td></tr><tr><td> $B(\neg\neg\neg\alpha)$ </td><td> $=B(\neg\neg\alpha)$ </td><td> $=H(\alpha)$ </td><td> $=H(\neg\neg\neg\alpha)$ </td></tr></table>

Moreover, the use of this sub-normalised uncertainty distribution has as a consequence that:

$$
\begin{array}{l} B (\alpha \lor \beta) = B (\sim (\sim \alpha \land \sim \beta)) = 1 - B (\sim \alpha \land \sim \beta) \\ \qquad = 1 - \min (B (\sim \alpha), B (\sim \beta)) \\ \qquad = \max (1 - B (\sim \alpha), 1 - B (\sim \beta)) \\ \qquad = \max (B (\alpha), B (\beta)). \end{array}
$$

This does not solve all compositional problems of the language, but allows a wider field of interesting computational results.

Last, but not least, recall once more that in our language we associate to each sentence α the distribution: $\langle \alpha , B ( \alpha ) , B ( \lnot \alpha ) \rangle$ . We can interpret $B ( \alpha )$ and $B ( \neg \alpha )$ as two functions on the power set of a set of events Ω. We establish the following definition.

Definition 4.1. A DDT distribution on the set of events Ω is a couple of functions $f _ { 1 } : 2 ^ { \varOmega } \mapsto [ 0 , 1 ] , f _ { 2 } : 2 ^ { \varOmega } \mapsto [ 0 , 1 ]$ such that:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
—  $\forall A\subseteq\Omega$  we have  $\langle A,f_{1}(A),f_{2}(A)\rangle$ ;
—  $f_{1}(0)=f_{2}(0)=0;$ 
—  $f_{1}(\Omega)=f_{2}(\Omega)=1;$ 
—  $A\subseteq B\Rightarrow f_{1}(A)\leq f_{1}(B);$ 
—  $C\subseteq D\Rightarrow f_{2}(C)\leq f_{2}(D);$ 
— for  $A\cap B$  we have  $\langle A\cap B,\min(f_{1}(A),f_{1}(B)),\max(f_{2}(A),f_{2}(B))\rangle$ ;
— for  $A\cup B$  we have  $\langle A\cup B,\max(f_{1}(A),f_{1}(B)),\min(f_{2}(A),f_{2}(B))\rangle$ .
</div>

It has already been noted that uncertainty measures can be seen as capacity measures. The use of a double instead of a single function allows to consider the possibility to compare this type of distribution with the case of two capacity measures. Such measures, defining two independent, monotone capacities have recently been introduced in the literature by [26] and are called bi-capacities:

## Definition 4.2. (Bi-capacity)

Let us denote $P ( J ) = \{ ( C , D ) : C \subseteq J , D \subseteq J , C \cap D = 0 \}$ then $\upsilon : P ( J ) \longrightarrow [ 0 , 1 ] \times [ 0 , 1 ]$ is a bi-capacity function if it satisfies the following conditions:

1. $\upsilon ( 0 , 0 ) { = } 0 ,$ , and

2. if $C \supseteq E$ and $D \subseteq F$ then $v ( C , D ) \geq v ( E , F )$

This definition suggests that two subsets of J have an empty intersection which is not always the case with positive and negative reasons. For this reason, we make use of a more recent definition given by Ref. [20] where the exclusivity condition on the sets C and $D$ is not necessary. They called such measures generalised bicapacities:

## Definition 4.3. (Generalised bi-capacity)

Let us denote $P ^ { * } \left( J \right) = \left\{ \left( C , D \right) : C \subseteq J , D \subseteq J \right\}$ , then υ : $P ( J ) \longrightarrow [ 0 , 1 ] \times [ 0 , 1 ]$ is a generalised bi-capacity function if it satisfies the following conditions

1. $v ^ { * } ( C , 0 ) { = } ( c , 0 )$ , and $\upsilon \left( 0 , D \right) = \left( 0 , d \right)$ , with $c , d \in [ 0 , 1 ]$

$$
v ^ {*} (J, 0) = (1, 0)
$$

$$
v (0, J) = (0, 1)
$$

3. Suppose that $v ^ { * } \ ( C , D ) { = } ( c , d )$ and υ⁎ $( E , \ F ) { = } ( e { , } f )$ with $c , d , e , f { \in } [ 0 , 1 ]$ , if $C \supseteq E$ and $D \subseteq F$ then, $c \geq e$ and $d { \le } f$

Given $( C , D ) \subseteq P ^ { * } ( J )$ with $v ^ { * } ( C , D ) = ( c , d )$ , they define two new relations $\upsilon ^ { * ^ { + } }$ and $\upsilon \ast ^ { - } \colon \upsilon ^ { \ast ^ { + } } ( c , d ) = c$ and $v ^ { \ast } ^ { - } ( c , d ) { = } d .$

Proposition 4.2. A DDT uncertainty distribution is a generalised bi-capacity measure.

Proof. Let's consider $P ^ { * } ( J ) = \{ ( C , D ) : C \subseteq J , D \subseteq J \}$ and $v ^ { * ^ { + } } ( c , d ) { = } B ( \alpha ) { = } f _ { 1 } ( \alpha )$ and $v ^ { * } { } ^ { - } ( c , d ) = B ( \lnot = \infty ) = f _ { 2 } ( \alpha )$ , then $v ^ { * } \left( C , D \right) { = } ( f _ { 1 } ( \alpha ) , f _ { 2 } ( \alpha ) )$ . We have

1. $v ^ { * } \left( C , 0 \right) { = } \left( c , 0 \right)$ , and $v ^ { * } \left( 0 , D \right) = \left( 0 , d \right)$ , with $c , d \in [ 0 , 1 ] .$ from Definition 4.3.

2. $v ^ { * } \left( J , 0 \right) { = } ( 1 , 0 )$ , and $v ^ { * } \left( 0 , J \right) { = } ( 0 , 1 )$ , from Definition 4.3.

3. Suppose that $v ^ { * } \ ( C , D ) { = } ( f _ { 1 } ( \alpha ) , f _ { 2 } ( \alpha ) )$ and $v ^ { * } \left( E , F \right) =$ $( f _ { 1 } ( \beta ) , f _ { 2 } ( \beta ) )$ , if $C \supseteq E$ and $D \subseteq F$ then, from definition $4 . 3 , f _ { 1 } ( \alpha ) { \geq } f _ { 1 } ( \beta )$ and $f _ { 2 } ( \alpha ) \leq f _ { 2 } ( \beta )$

## 5. Conclusion

In this paper we discuss two distinct tools used to deal with uncertainty: four valued logics and uncertainty distributions; both extensively used in decision aiding, the first one in order to take into account positive and negative reasons in formulating a recommendation, the second one in order to take into account the poor or contradictory information present in the decision aiding process.

We first show how it is possible to extend a four valued logic using continuous valuations of positive and negative reasons. We then interpret such continuous valuations as standard necessity measures. On the one hand we obtain a result consistent with possibility theory, but on the other hand we lose some of the expressive power of the four valued logic, mainly the possibility to distinguish contradictory statements from unknown ones. We then show that by interpreting such valuations as sub-normalised necessity measures, we are able to fully exploit the expressivity of the four valued language, but at the price of losing the possibility to use two independent dual measures of uncertainty.

## Acknowledgements

A large part of this paper was prepared while the first author was visiting DIMACS, Rutgers University, within an exchange program funded by the NSF-CNRS, the support of which is gratefully acknowledged. It has been finished while the second author was visiting the SMG, Universit´e Libre de Bruxelles under an IRSIA scholarship which is also gratefully acknowledged. The authors would like to thank the three anonymous referees for their valuable comments which allowed to improve the paper.

## Appendix A

Proof of Proposition 2.2. Before giving the proof of the proposition, we remind in the following thedefinition of a Lukasiewicz triple:

$$
L N _ {\phi} (x) = \phi^ {- 1} (1 - \phi (x))
$$

$$
L T _ {\phi} (x, y) = \phi^ {- 1} (\max (\phi (x) + \phi (y) - 1, 0))
$$

$$
L V _ {\phi} (x, y) = \phi^ {- 1} (\min (\phi (x) + \phi (y), 1))
$$

where ϕ is an automorphism of [0,1].

The proof will be done in two steps:

i. First of all, we will suppose that

$$
N = L N _ {\phi}, T _ {2} = T _ {3} = L T _ {\phi}
$$

$$
V = L V _ {\phi} T _ {1} = T _ {4} = \min
$$

and try to prove that Eqs. (9)–(16) are satisfied.

Let's begin with the definitions of four fuzzy values:

$$
t (\alpha) = \min (B (\alpha), 1 - B (\neg \alpha))\tag{39}
$$

$$
k (\alpha) = \phi^ {- 1} \max (\phi (B (\alpha)) + \phi (B (\neg \alpha)) - 1, 0)\tag{40}
$$

$$
u (\alpha) = \phi^ {- 1} \max (1 - \phi (B (\alpha)) - \phi (B (\neg \alpha)), 0)\tag{41}
$$

$$
f (\alpha) = \min (1 - B (\alpha), B (\neg \alpha))\tag{42}
$$

in this case,

if $\phi ( B ( \alpha ) ) + \phi ( B ( - \alpha ) ) \geq 0$ thus,

$$
\phi (B (\alpha)) \geq 1 - \phi (B (\neg \alpha)),
$$

or ϕ is an automorphism of [0,1], then

$$
B (\alpha) \geq 1 - B (\neg \alpha),
$$

$$
B (\neg \alpha) \geq 1 - B (\alpha)
$$

as a conclusion

$$
k (\alpha) = \phi^ {- 1} (\phi (B (\alpha)) + \phi (B (\neg \alpha)) - 1) \text {   and   we   get }
$$

$$
t (\alpha) = 1 - B (\neg \alpha), k (\alpha) = B (\alpha) + B (\neg \alpha) - 1, u (\alpha) = 0, f (\alpha)
$$

It is easy to check that Eqs. (9)–(16) are satisfied.

if $\phi ( B ( \alpha ) ) + \phi ( B ( \lnot \alpha ) ) \le 0 ,$ , then $\phi ( B ( \alpha ) ) \leq 1 - \phi ( B$ (¬α)),

thus $B ( \alpha ) { \leq } 1 { - } B ( \lnot \alpha ) .$ , and $B ( \lnot \alpha ) \leq 1 - B ( \alpha ) .$

as a conclusion

$u ( \alpha ) { = } { \phi } ^ { - 1 } ( 1 { - } ( \phi ( B ( \alpha ) ) { + } \phi ( B ( \neg \alpha ) ) ) )$ and we get

$$
t (\alpha) = B (\alpha), u (\alpha) = 1 - (B (\alpha) + B (\neg \alpha)), k (\alpha) = 0, f (\alpha) = B
$$

It is easy to check that Eqs. (9)–(16) are satisfied. As a consequence, if $N { = } L N \phi , T _ { 2 } { = } T _ { 3 } { = } L T \phi V { = } L V \phi$ $T _ { 1 } { = } T _ { 4 } { = } \mathrm { m i n }$ then Eqs. (9)–(16) are satisfied.

ii. Let's analyse now the other direction of the equivalence:

Suppose that Eqs. (5)–(16) are satisfied, then

$$
\text { i.   } N = L N \phi \text {: because   } B (\alpha) + N (B (\alpha)) = 1
$$

$$
B (\alpha) + N (B (\alpha)) = 1, \text {   then   } V (t (\alpha), k (\alpha)) + V (f (\alpha), u (\alpha))
$$

$$
V (t (\alpha), 0) + V (f (\alpha), u (\alpha)) = 1
$$

$$
t (\alpha) + V (f (\alpha), u (\alpha)) = 1 (t \text {-co - norm property}),
$$

$$
V (f (\alpha), u (\alpha)) = f (\alpha) + u (\alpha) \tag {Eq.(9)}
$$

iii. $T _ { 1 } \mathrm { = } T _ { 4 } \mathrm { = m i n \mathrm { : } \ f r o m \ E q s . \ ( 5 \mathrm { - } 8 ) }$ and (14), (15), we

get:

$$
t (\alpha) = T _ {1} (V (t (\alpha), k (\alpha)), V (t (\alpha), u (\alpha)))
$$

$$
k (\alpha) = T _ {2} (V (t (\alpha), k (\alpha)), V (f (\alpha), k (\alpha)))
$$

$$
u (\alpha) = T _ {3} (V (f (\alpha), u (\alpha)), V (t (\alpha), u (\alpha)))
$$

$$
f (\alpha) = T _ {4} (V (f (\alpha), u (\alpha)), V (f (\alpha), k (\alpha)))
$$

$$
\text { if   } k (\alpha) = 0 \text {   then }
$$

$$
t (\alpha) = T _ {1} (t (\alpha), V (t (\alpha), u (\alpha)))
$$

$$
V \left(t (\alpha), u (\alpha)\right) \geq t (\alpha), \text { then }
$$

$$
T _ {1} \text {   is   the   upper   bound   of   } t \text {-norms,   ie.   } T _ {1} = \min
$$

$$
f (\alpha) = T _ {4} (V (f (\alpha), u (\alpha)), f (\alpha))
$$

$$
V (f (\alpha), u (\alpha)) \geq f (\alpha), \text { then }
$$

$T _ { 4 }$ is the upper bound of t-norms, i.e. $T _ { 4 } { = } _ { \operatorname* { m i n } }$

$$
\mathrm{iv.} T _ {2} = T _ {3} = L T \phi
$$

$$
\text { if   } k (\alpha) = 0 \text {   then }
$$

$$
u (\alpha) = T _ {3} (N (V (t (\alpha), k (\alpha))), N (V (f (\alpha), k (\alpha))))
$$

$$
u (\alpha) = T _ {3} (N (V (t (\alpha), 0)), N (V (f (\alpha), 0)))
$$

$$
u (\alpha) = T _ {3} (N (t (\alpha)), N (f (\alpha)))
$$

$$
u (\alpha) = T _ {3} (1 - t (\alpha), 1 - f (\alpha)), \text {   and   } u (\alpha) = 1 - t (\alpha) - f (\alpha)
$$

thus,

$$
T _ {3} (1 - t (\alpha), 1 - f (\alpha)) = 1 - t (\alpha) - f (\alpha),
$$

then, $T _ { 3 }$ is continuous, Archimedean and has a zero divisor, i.e. it is nilpotent.

An element $x \in [ 0 , 1 ]$ is called a zero divisor of a $t -$ norm T if and only if $( \exists y \in [ 0 , 1 ] T ( x , y ) = 0 )$ . A t-norm without zero divisors is called positive.

A continuous t-norm Tis Archimedean if and only if $\forall x \in [ 0 , 1 ] T ( x , x ) < x .$

Let's prove that $T _ { 3 }$ is Archimedean:

Suppose that $T _ { 3 }$ is not Archimedean, then

∀α, t(α) = f(α), T<sub>3</sub>(1 − t(α), 1 − f(α)) = 1 − t(α), or

$$
T _ {3} (1 - t (\alpha), 1 - f (\alpha)) = u (\alpha) = 1 - t (\alpha) - f (\alpha),
$$

as a conclusion, $T _ { 3 }$ is Archimedean.

Let's prove that $T _ { 3 }$ has a zero divisor:

Suppose that $T _ { 3 }$ does not have a zero divisor, then $\forall x , y \in [ 0 , 1 ] T ( x , y ) \neq 0 ,$ or

there exist cases where $t ( \alpha ) { \neq } 1 , f ( \alpha ) { \neq } 1 , u ( \alpha ) { \neq } 0 ,$ . thus

$$
\exists \alpha ; t (\alpha), f (\alpha) \in [ 0, 1 ] T _ {3} (1 - t (\alpha), 1 - f (\alpha)) = 0),
$$

as a conclusion, $T _ { 3 }$ has a zero divisor

Moreover, it is known that a nilpotent t-norm is $\phi -$ transform of the Lukasiewicz t-norm, as a conclusion $T _ { 3 } { = } L T _ { \phi }$

The proof of $T _ { 2 } { = } L T _ { \phi }$ is similar to the last one where the condition $k ( \alpha ) { = } 0 \mathrm { i s }$ replaced by u(α) = 0.

## References

[1] C. Alsina, On a family of connectives for fuzzy sets, Fuzzy Sets and Systems 16 (1985) 231–235.

[2] O. Arieli, Paraconsistent reasoning and preferential entailments by signed quantified Boolean formulae, ACM Transactions on Computational Logic 5 (2005) 1–29.

[3] O. Arieli, A. Avron, The value of the four values, Artificial Intelligence 102 (1998) 97–141.

[4] O. Arieli, A. Avron, Bilattices and paraconsistency, in: D. Batens, C. Mortensen, G. Priest (Eds.), Frontiers of Paraconsistent Logic, Studies in Computational Logic, vol. 8, Research Studies Press, Baldock, 2000, pp. 11–27.

[5] O. Arieli, C. Cornelis, G. Deschrijver, E. Kerre, Billatice-bases squares and triangles, Proceedings of ECSQARU 2005, LNAI 3571, Springer Verlag, Berlin, 2005, pp. 563–575.

[6] J.-P. Barthelemy, R. Bisdorff, G. Coppin, Human centered processes and decision support systems, European Journal of Operational Research 136 (2002) 233–252.

[7] N.D. Belnap, How a computer should think, Proceedings of the Oxford International Symposium on Contemporary Aspects of Philosophy, Oxford, England, 1976, pp. 30–56.

[8] N.D. Belnap, A useful four-valued logic, in: G. Epstein, J. Dunn (Eds.), Modern uses of multiple valued logics, D. Reidel, Dordrecht, 1977, pp. 8–37.

[9] S. Benferhat, D. Dubois, H. Prade, Towards a possibilistic logic handling of preferences, Applied Intelligence 14 (2001) 303–317.

[10] D. Bouyssou, T. Marchant, M. Pirlot, P. Perny, A. Tsoukiàs, Ph. Vincke, Evaluation and Decision Models: A Critical Perspective, Kluwer Academic, Dordrecht, 2000.

[11] G. Choquet, Theory of capacities, Annales de l'Institut Fourier 5 (1953) 131–295.

[12] N.C.A. da Costa, Theory of inconsistent formal systems, Notre Dame Journal of Formal Logic 15 (1974) 497–510.

[13] B. De Baets, E. Kerre, B. Van De Walle, Fuzzy preference structures and their characterization, Journal of Fuzzy Mathematics 3 (1995) 373.

[14] P. Doherty, D. Driankov, A. Tsoukiàs, Partial logics and partial preferences, Proceedings of the CEMIT 92 International Conference, Tokyo, 1992, pp. 525–528.

[15] D. Dubarle. Essai sur la généralisation naturelle de la logique usuelle. Mathématique, Informatique, Sciences Humaines, No 107:17–73, 1989. 1963 manuscript, published posthumously.

[16] D. Dubois, H. Prade, Possibility Theory, Plenum Press, New-York, 1988.

[17] D. Dubois, H. Prade, Possibility theory, probability theory and multiple valued logics: a clarification, Annals of Mathematics and Artificial Intelligence 32 (2001) 35–66.

[18] D. Dubois, H. Prade, Ph. Smets, Not impossible vs. guaranteed possible in fusion and revision, in: S. Benferhat, Ph. Besnard (Eds.), Proceedings of ECSQARU-01, 2001, pp. 522–531.

[19] D.S. Felsenthal, M. Machover, Ternary voting games, International Journal of Game Theory 26 (1997) 335–351.

[20] J. Figueira and S. Greco. Dealing with interactivity between bipolar multiple criteria preferences in outranking methods. Private communication, 2004.

[21] M.C. Fitting, Bilattices and the semantics of logic programming, Journal of Logic Programming 11 (1991) 91–116.

[22] J. Fodor, M. Roubens, Fuzzy Preference Modelling and Multicriteria Decision Support, Kluwer Academic Publishers, 1994.

[23] Ph. Fortemps, R. Slowiński, A graded quadrivalent logic for ordinal preference modelling: Loyola-like approach, Fuzzy Optimization and Decision Making 1 (2002) 93–111.

[24] M.L. Ginsberg, Multivalued logics: a uniform approach to reasoning in artificial intelligence, Computational Intelligence 4 (1988) 265–316.

[25] M. Grabisch, Ch. Labreuche, Fuzzy measures and integrals in MCDA, in: J. Figueira, S. Greco, M. Ehrgott (Eds.), Multiple Criteria Decision Analysis: State of the Art Surveys, Springer Verlag, Boston, 2005, pp. 563–608.

[26] M. Grabisch, Ch. Labreuche, Bi-capacities for decision making on bipolar scales, Proceedings of the EUROFUSE 02 Workshop on Information Systems, 2002, pp. 185–190.

[27] P. Perny, M. Roubens, Fuzzy preference modelling, in: R. Slowinski (Ed.), Fuzzy Sets in Decision Analysis, Operations Research and Statistics, Kluwer Academic, Dordrecht, 1998, pp. 3–30.

[28] P. Perny, A. Tsoukiàs, On the continuous extension of a four valued logic for preference modelling, Proceedings of the IPMU 1998 Conference, Paris, 1998, pp. 302–309.

[29] P.T. Raju, The principle of four-cornered negation in Indian philosophy, Review of Metaphysics 7 (1954) 694–713.

[30] N. Rescher, Introduction to Value Theory, Prentice Hall, Englewood Cliffs, 1969.

[31] N. Rescher, R. Brandom, The Logic of Inconsistency, Blackwell, Oxford, 1980.

[32] B. Roy, Main sources of inaccurate determination, uncertainty and imprecision, Mathematical and Computer Modelling 12 (10 11) (1989) 1245–1254.

[33] B. Schweizer, A. Sklar, Probabilistic Metric Spaces, Elsevier Science, New York, 1983.

[34] Ph. Smets, The canonical decomposition of a weighted belief, Proceedings of IJCAI-95, 1995, pp. 1896–1901.

[35] Ph. Smets, R. Kennes, The transferable belief model, Artificial Intelligence (1994) 191–234.

[36] A. Tsoukiàs, A qualitative approach to face uncertainty in decision models, Decision Support Systems 12 (1994) 287–296.

[37] A. Tsoukiàs, A first-order, four valued, weakly paraconsistent logic and its relation to rough sets semantics, Foundations of Computing and Decision Sciences 12 (2002) 85–108.

[38] A. Tsoukiàs, P. Perny, Ph. Vincke, From concordance/discordance to the modelling of positive and negative reasons in decision aiding, in: D. Bouyssou, E. Jacquet-Lagr\`eze, P. Perny, R. Slowinski, D. Vanderpooten, Ph. Vincke (Eds.), Aiding Decisions with Multiple Criteria: Essays in Honour of Bernard Roy, Kluwer Academic, Dordrecht, 2002, pp. 147–174.

[39] A. Tsoukiàs, Ph. Vincke, A new axiomatic foundation of partial comparability, Theory and Decision 39 (1995) 79–114.

[40] A. Tsoukiàs, Ph. Vincke, Extended preference structures in MCDA, in: J. Climaco (Ed.), Multicriteria Analysis, Springer Verlag, Berlin, 1997, pp. 37–50.

[41] B. Van DeWalle, B. De Baets, E. Kerre, Recent advances in fuzzy preference modelling, Intelligent Systems and Soft Computing for Nuclear Science and Industry (1996) 98–104.

[42] B. Van DeWalle, B. De Baets, E. Kerre, Characterizable fuzzy preference structures, Annals of Operations Research 80 (1998) 105–136.

![](/api/attachments/G89EW5VE/fulltext/images/510ad00c036ce23b473d884cf5ba9fd4301e5892aa2188993755520a63cd6082.jpg)  
Meltem Öztürk is a research and teaching assistant at LAMSADE, Universtié Paris Dauphine, where she recently defended her PhD in computer science. She holds a degree in industrial engineering from Galatasaray University, Istanbul and a Master degree in Management Science from Universit´e Paris Dauphine. Her research interests include decision theory, preference modelling and artificial intelligence. Personal web page: http://www.lamsade.dauphine.fr/∼ozturk.

![](/api/attachments/G89EW5VE/fulltext/images/99b5967e8112461c2905bba507b9bc970b1aaf22cde018428fe19a0e4e952cb9.jpg)

Alexis Tsoukiàs is a CNRS research director at LAMSADE, Université Paris Dauphine. He holds a PhD in Computer Science and Systems Engineering from Politecnico di Torino (Italy) where he also graduated engineering studies. His research interests include subjects such as: multiple criteria decision making, non-conventional preference modelling, applied non classical logics, ordinal mathematical programming, artificial intelligence and decision theory. He is the co-

author of two books and more than 70 journal articles and book contributions. He has been vice-president of ROADEF (the French Operational Research society) and he is now President of EURO (the European association of Operational Research societies). Besides teaching to several post-graduate classes he occasionally practices decision support. He has been invited to several Universities world wide. Personal web page: http://www.lamsade.dauphine.fr/∼tsoukias.

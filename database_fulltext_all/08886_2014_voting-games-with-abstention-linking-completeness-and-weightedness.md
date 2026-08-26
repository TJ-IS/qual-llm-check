---
otero_id: 8886
otero_key: "82WXZ4Q2"
title: "Voting games with abstention: Linking completeness and weightedness"
authors: "Josep Freixas; Bertrand Tchantcho; Narcisse Tedjeugang"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.08.015"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Voting games with abstention: Linking completeness and weightedness<sup>☆</sup>

Josep Freixas <sup>a,</sup>⁎, Bertrand Tchantcho <sup>b,c</sup>, Narcisse Tedjeugang d

<sup>a</sup> “Departament de Matemàtica Aplicada 3 i Escola Politècnica Superior d'Enginyeria de Manresa (Universitat Politècnica de Catalunya)”, Spain

<sup>b</sup> University of Yaounde I, MASS laboratory, Cameroon

<sup>c</sup> University of Cergy Pontoise, THEMA Laboratory, France

<sup>d</sup> University of Yaounde I, Cameroon

## a r t i c l e i n f o

Article history: Received 23 February 2012 Received in revised form 15 July 2013 Accepted 31 August 2013 Available online 9 September 2013

MSC: 91A12 90B50 91A35 05C65 94C10

## a b s t r a c t

Weighted games for several levels of approval in input and output were introduced in [9]. An extension of the desirability relation for simple games, called the in<sup>fl</sup>uence relation, was introduced for games with several levels of approval in input in [24] (see also [18]). However, there are weighted games not being complete for the in<sup>fl</sup>uence relation, something different to what occurs for simple games. In this paper we introduce several extensions of the desirability relation for simple games and from the completeness of them it follows the consistent link with weighted games, which solves the existing gap. Moreover, we prove that the in<sup>fl</sup>uence relation is consistent with a known subclass of weighted games: strongly weighted games.

© 2013 Elsevier B.V. All rights reserved

Keywords: Decision making process Voting systems in democratic organizations Multiple levels of approval Weightedness and completeness Desirability relations

## 1. Introduction

Voting systems in democratic institutions, as those in international economic organizations or federal voting bodies, have in common that voters must make decisions involving a choice between multiple alternatives instead of the most usual assumption which assumes that voters are only allowed to vote for “yes” or “no”. The speci<sup>fi</sup>c or de<sup>fi</sup>nable decision context consists of “either breaking the status quo or not”. The target system describes each situation in which partitions of voters are able to pass a new law or change the status quo. Making decisions in democratic organizations is regarded as a DSS and an investigation of the DSS literature reveals that research has mainly focused on the effects of design, implementation and use on decision outcomes (see e.g., [3,11]).

The generalization of simple voting games to multiple levels arose out of the observation that, while many real voting systems allow voters to abstain (or be absent), simple games, by their nature, cannot take this possibility into account; those who do not vote “yes” are presumed to vote “no”. Some works that took more than two input alternatives into consideration are: [5,19,1,12,14,16,17].

The voting structures, we primarily consider in this paper, are particular cases of (j, k) voting systems introduced in [9]. These structures assume that levels of approval in both, input and output, are ordered. The paper is con<sup>fi</sup>ned to the case k = 2 and is focused for j = 3 ordered levels of input approval, although the results obtained in this paper extend for any arbitrary greater value of j. When absent voters are taken into account with a quorum (like in [4] or in [25]) the levels of input approval are not ordered and therefore, the results in this paper do not extend to that context. Some (3, 2) voting systems are weighted (3, 2) systems which admit a representation by means of vector weights and a threshold for the system, and therefore their representations as weighted systems are useful to separate the two possible collective outcomes. A purpose of this paper is to link the completeness of some desirability relations that determine the importance of voters in the system, with weighted systems with several ordered levels of approval for the input.

A necessary but not suf<sup>fi</sup>cient condition for a simple game to be representable as a weighted game is to be complete, i.e., all players are pairwise comparable by the desirability relation, which is a pre-ordering on the set of voters and therefore a re<sup>fl</sup>exive and transitive relation. Consequently, an easy and practical way to identify some non-weighted simple games is to check that they are not complete.

The notion of weighted game for (j,k) simple games is supported by a powerful combinatorial argument, grade–trade robustness for partitions. Even the issue of ascertaining whether an anonymous (j,2) game is weighted is a dif<sup>fi</sup>cult issue [10,26]. When we are restricted to simple games, i.e $j = k = 2$ , weighted (j,k) games are simply weighted simple games and grade–trade robustness for partitions (see [9]) is trade-robustness for coalitions (see [21] and [23]).

In this paper, we will look at the extension of the desirability relation for simple games [13] to the ternary voting game (or more generally for (3, 2) games) given in [24], wherein such an extension was denominated in<sup>fl</sup>uence relation. In [24], it is proved that the in<sup>fl</sup>uence relation fails to be transitive and cycles for players are possible. We observe that one may easily <sup>fi</sup>nd weighted (3, 2) games which are not complete for the in-<sup>fl</sup>uence relation, so that the completeness of the game for the in<sup>fl</sup>uence relation is not a necessary condition for a (3, 2) game to be weighted. To solve this gap we consider three separate new relations, each of them weaker than the in<sup>fl</sup>uence relation. Then the desired notion of completeness is derived by demanding the completeness of each one of these three new relations. This notion is weaker than the completeness for the in<sup>fl</sup>uence relation, but it is enough to become a necessary condition for the (3, 2) game to be weighted. Moreover, we will prove that the completeness derived by the in<sup>fl</sup>uence relation becomes a necessary condition for a (3, 2) game to be strongly weighted, a subclass of weighted games already considered in [9].

An additional issue is also considered in this paper. It concerns the associated notions of swap-robustness for each of the three new relations introduced in the paper. These characterizations extend the known characterization of complete simple games by swap-robustness given in [22] and [20].

The paper is organized as follows. The technical background as well as an example is introduced in what remains of this section. In Section 2 we introduce several notions of desirability for (3, 2) games and consider their completeness, their restrictions and extensions to simple games and the hierarchies they induce. In Section 3 we consistently link weighted (3, 2) games with an appropriate class of complete (3, 2) games, and strongly weighted (3, 2) games with complete (3, 2) games with respect to the in<sup>fl</sup>uence relation. In Section 4 different $( 3 ,$ 2) swap robustness properties, which restriction for the case of simple games constitutes a characterization of complete games, are established for the derived notions of completeness for (3,2) games. Conclusion ends the paper.

## 1.1. The class of (3, 2) simple games

The material on this section is essentially taken from Freixas and Zwicker [9], where (j,k) simple games are introduced, for the particular choices: j = 3 and $k = 2 .$ Before the main notions are introduced we need some preliminary de<sup>fi</sup>nitions. An ordered tripartition of the <sup>fi</sup>nite set N is a sequence ${ \boldsymbol { S } } = ( S _ { 1 } , S _ { 2 } , S _ { 3 } )$ of mutually disjoint sets whose union is N. Any S is allowed to be empty, and we think of $S _ { i }$ as the set of those voters of N who vote approval level i for the issue at hand (where approval level 1 is the highest level of approval, 2 is the intermediate level and 3 the lowest level). The most relevant situation that happens in voting is when $S _ { 1 }$ corresponds to the set of “yes” voters, $S _ { 2 }$ to the set of abstainers and $S _ { 3 }$ to the set of “no” voters. Thus, an ordered tripartition is the analog of a coalition for a standard simple game. Let $3 ^ { N }$ denote the set of all ordered tripartitions of N. For $\bar { S } , T \in 3 ^ { N }$ , we write S $\subseteq ^ { 3 }$ T to mean that either S = T or S may be transformed into T by shifting 1 or more voters to higher levels of approval. This is the same as saying $S _ { 1 } \subseteq T _ { 1 }$ and $S _ { 1 } \cup S _ { 2 } \subseteq T _ { 1 } \cup T _ { 2 } ;$ we write $S \subset ^ { 3 } T$ if $S \subseteq ^ { 3 } T$ and $S \ne T .$ The $\subseteq ^ { 3 }$ order de<sup>fi</sup>ned on $3 ^ { N }$ has minimum: the tripartition $\mathcal { N }$ such that $\mathcal { N } _ { 3 } = N$ , and maximum: the tripartition such that $\mathcal { M } _ { 1 } = N ; \mathrm { i . e . }$ , for every tripartition $S , { \mathcal { N } } \subseteq ^ { 3 } S \subseteq { ^ { 3 } }$ holds.

De<sup>fi</sup>nition 1.1. A (3, 2) simple game $G = ( N , V )$ (henceforth (3, 2) game) consists of a <sup>fi</sup>nite set N of voters together with a value function

$V : 3 ^ { N } \to \{ 0 , 1 \}$ , which satis<sup>fi</sup>es $V ( \mathcal { N } ) = 0 , V ( \mathcal { M } ) = 1$ , and is monotonic: <sup>ðN</sup>for all ordered tripartitions S and T, $\operatorname { i f } S \subset ^ { 3 } 1$ <sup>Þ ¼M</sup>T then $V ( S ) \leq V ( T )$

$\mathsf { A } \left( 3 , 2 \right)$ game is also de<sup>fi</sup>ned by the set of winning tripartitions $W =$ $\{ S \in 3 ^ { N } : { \bar { V ( S ) } } = 1 \}$ that satis<sup>fi</sup>es $\mathcal { N } \notin \boldsymbol { W } , \mathcal { M } \in \boldsymbol { W }$ , and the monotonicity requirement: $\mathrm { i f } S \subset ^ { 3 } T$ and $S \in W$ <sup>N</sup>then $T \in W .$

Standard notions for coalitions in simple games naturally extend for tripartitions in (3,2) games: S is a losing tripartition whenever $V ( S ) = 0$ let L denote the set of losing tripartitions; S is a minimal winning tripartition provided that S is winning and for all $T \in 3 ^ { N }$ such that $T \stackrel { - 3 } { \subset } S ,$ , T is losing, let $W ^ { m }$ denote the set of minimal winning tripartitions; S is a maximal losing tripartition provided that S is losing and for all $T \in 3 ^ { N }$ such that $S \subset { } ^ { 3 } T ,$ T is winning, let $L ^ { M }$ denote the set of maximal losing tripartitions. It is clear that W and L form a bipartition of $3 ^ { N } ,$ , and that each of the sets: $W , L , W ^ { m }$ , and $L ^ { M }$ uniquely determines the (3, 2) game.

De<sup>fi</sup>nition 1.2. Let $\mathsf { G } = ( \mathsf { N } , \mathsf { V } )$ be a (3, 2) game. A representation of G as a weighted (3, 2) game consists of a vector $w = ( w _ { 1 } , w _ { 2 } , w _ { 3 } )$ where w : $N {  } \mathbb { R }$ for each i together with a real number quota q such that for every tripartition $\mathsf { S } , \mathsf { V } ( \mathsf { S } ) = 1$ if and only if $w ( S ) \geq q ,$ where w(S) denotes

$$
\sum_ {i = 1} ^ {3} \sum_ {p \in S _ {i}} w _ {i} (p) \text {   and   } w _ {1} (p) \geq w _ {2} (p) \geq w _ {3} (p) \text {   for   each   } p \in N.
$$

We say that ${ \sf G } = ( { \sf N } , { \sf V } )$ is a weighted (3, 2) game if it has such a representation.

As was observed in [9], each “yes” voter contributes the weight $w _ { 1 } ( p )$ to the total weight H; each abstainer contributes $w _ { 2 } ( p )$ to H, and each “no" voter contributes $w _ { 3 } ( p )$ to $H ,$ with the issue passing exactly if H meets or exceeds some preset quota q. That is, before any voting takes place each voter is pre-assigned three weights with $w _ { 1 } ( p ) \geq w _ { 2 } ( p ) \geq w _ { 3 } ( p )$ for each voter $p ,$ but will make no assumptions about the signs of $w _ { 1 } ( p )$ $w _ { 2 } ( p )$ or $w _ { 3 } ( p )$ . As occurs for simple games where two weights represent super<sup>fl</sup>uous information, three weights represent super<sup>fl</sup>uous information. If we renormalize by subtracting $w _ { 2 } ( p )$ from each of the weights $w _ { 1 } ( p ) , ~ w _ { 2 } ( p )$ and $w _ { 3 } ( p )$ then the new triple of weights $w ^ { + } ( p ) =$ $w _ { 1 } ( p ) - w _ { 2 } ( p ) , 0$ , and $w ^ { - } ( p ) = w _ { 3 } ( p ) - w _ { 2 } ( p )$ describes the same voting system, and satis<sup>fi</sup>es $w ^ { + } ( p ) \geq 0 \geq w ^ { - } ( p )$

A stronger condition of a weighted (3, 2) game introduced in [9] is the following.

De<sup>fi</sup>nition 1.3. A strongly weighted (3, 2) game is a weighted (3, 2) game that admits a representation such that for every pair of voters p and $\Gamma ,$ either

$$
w ^ {+} (p) \geq w ^ {+} (r) \text { and } - w ^ {-} (p) \geq - w ^ {-} (r)
$$

or

$$
w ^ {+} (p) \leq w ^ {+} (r) \text { and } - w ^ {-} (p) \leq - w ^ {-} (r).
$$

Example 1.4. Consider the (3, 2) game with a set of voters $N = \{ a , b , c \} ;$

$$
W ^ {m} = \{(a, b, c), (b, c, a), (c, a, b) \}.
$$

From the set of minimal winning tripartitions one may easily generate the set of winning tripartitions, the set of losing tripartitions and the set of maximal losing tripartitions, which is:

$$
L ^ {M} = \{(a, c, b), (b, a, c), (c, b, a), (\emptyset , a b c, \emptyset) \}.
$$

One may check that it is not weighted since the weight of the three minimal winning tripartitions are:

$$
w ^ {+} (a) + w ^ {-} (c), w ^ {+} (b) + w ^ {-} (a) \text {   and   } w ^ {+} (c) + w ^ {-} (b)
$$

respectively, and the weight of the maximal losing tripartitions are:

$$
w ^ {+} (a) + w ^ {-} (b), w ^ {+} (b) + w ^ {-} (c), w ^ {+} (c) + w ^ {-} (a) \text { and } 0
$$

respectively. If the game was weighted the system of the twelve inequalities obtained by pairing the weights of minimal winning and maximal losing tripartitions would be consistent. However, three of these inequalities (<sup>fi</sup>rst–<sup>fi</sup>rst, second–second and third–third) lead to a contradiction

$$
w ^ {-} (c) > w ^ {-} (b), w ^ {-} (a) > w ^ {-} (c), w ^ {-} (b) > w ^ {-} (a)
$$

hence the game is not weighted.

## 2. Several relations on the set of voters for (3, 2) games

We start the original contents of the paper by introducing three separate relations on N for (3, 2) games that constitute the main tool for linking weightedness and completeness.

De<sup>fi</sup>nition 2.1. Let (N, V) be a (3, 2) game.

(i) D<sup>+</sup>-desirability. $\mathsf { L e t } S = ( S _ { 1 } , S _ { 2 } , S _ { 3 } )$ be a tripartition, p and r be two arbitrary abstainers.

$$
p \gtrsim_ {D ^ {+}} r \Longleftrightarrow V (S _ {1} \cup p, S _ {2} \backslash p, S _ {3}) \geq V (S _ {1} \cup r, S _ {2} \backslash r, S _ {3})
$$

(ii) D<sup>−</sup>-desirability. $\mathsf { L e t } S = ( S _ { 1 } , S _ { 2 } , S _ { 3 } )$ be a tripartition, p and r be two arbitrary “no” voters.

$$
p \succsim_ {D ^ {-}} r \Longleftrightarrow V (S _ {1}, S _ {2} \cup p, S _ {3} \backslash p) \geq V (S _ {1}, S _ {2} \cup r, S _ {3} \backslash r)
$$

(iii) D<sup>±</sup>-desirability. Let ${ \boldsymbol { S } } = ( S _ { 1 } , S _ { 2 } , S _ { 3 } )$ be a tripartition, p and r be two arbitrary “no” voters.

$$
p \gtrsim_ {D ^ {\pm}} r \Longleftrightarrow V (S _ {1} \cup p, S _ {2}, S _ {3} \backslash p) \geq V (S _ {1} \cup r, S _ {2}, S _ {3} \backslash r)
$$

Of course, $V ( S _ { 1 } \cup p , S _ { 2 } \mid p , S _ { 3 } ) \geq V ( S _ { 1 } \cup r , S _ { 2 } \mid r , S _ { 3 } )$ is equivalent to assert that $( S _ { 1 } \cup r , S _ { 2 } \cup r , S _ { 3 } ) \in W$ implies that $( S _ { 1 } \cup p , S _ { 2 } \ \backslash \ p , S _ { 3 } ) \in W ,$ and similarly for the two next inequalities in De<sup>fi</sup>nition $2 . 1$

A player p is at least as $D ^ { + }$ -desirable as r if whenever r can transform a losing tripartition in which both are abstainers into a winning tripartition by shifting his support from abstention to full support, player p can achieve the same, ceteris paribus. Similar interpretations can be given for the D<sup>−</sup> and $D ^ { \pm }$ desirability relations.

De<sup>fi</sup>nition 2.2 (Tchantcho et. al. [24]). Let G = (N,V) be a (3, 2) simple game, p and r are two voters. Voter p is said to be at least as in<sup>fl</sup>uential as $\mathrm { \Delta } \mathrm { r } ,$ denoted $p \succeq r ,$ if for all $( S _ { 1 } , S _ { 2 } , S _ { 3 } ) \in 3 ^ { N }$ it yields:

$$
V (S _ {1} \cup p, S _ {2} \backslash p, S _ {3}) \geq V (S _ {1} \cup r, S _ {2} \backslash r, S _ {3}) \text {if} p, r \in S _ {2},
$$

$$
V (S _ {1}, S _ {2} \cup p, S _ {3} \backslash p) \geq V (S _ {1}, S _ {2} \cup r, S _ {3} \backslash r) \text { if } p, r \in S _ {3},
$$

and

$$
V (S _ {1} \cup p, S _ {2}, S _ {3} \backslash p) \geq V (S _ {1} \cup r, S _ {2}, S _ {3} \backslash r) \text { if } p, r \in S _ {3}.
$$

The I-in<sup>fl</sup>uence relation, which is re<sup>fl</sup>exive but nontransitive, is a stronger condition of each of the three separate relations given in De<sup>fi</sup>nition 2.1. Indeed, if p and r are two arbitrary voters then:

$$
p \succ_ {I} r \Rightarrow p \succeq_ {D ^ {+}} r, p \succeq_ {D ^ {-}} r, p \succeq_ {D ^ {\pm}} r
$$

and at least one of the three relations is strict. Moreover,

$$
p \approx_ {I} r \Longleftrightarrow p \approx_ {D ^ {+}} r, p \approx_ {D ^ {-}} r, p \approx_ {D ^ {\pm}} r
$$

Now we introduce the induced notion of completeness for the three separate relations considered in De<sup>fi</sup>nition 2.1 and two additional ones. We recall that the notion of completeness for the in<sup>fl</sup>uence relation (from now on I-completeness) was given in [24].

## De<sup>fi</sup>nition 2.3.

(i) A (3, 2) game is $D ^ { + }$ -complete if either $p { \succeq } _ { D ^ { + } } r$ or $r { \stackrel {  } { \sim } } _ { D ^ { + } } p$ for all pair p, r of voters.

(ii) A (3, 2) game is $D ^ { - }$ -complete if either pc − r or rc − p for all pair p, r of voters.

(iii) A (3, 2) game is D<sup>±</sup>-complete if either $p { \stackrel {  } { \sim } } _ { D ^ { \pm } } r$ or $r { \stackrel {  } { \sim } } _ { D ^ { \pm } } p$ for all pair p,r of voters.

(iv) $\mathsf { A } \left( 3 , 2 \right)$ game is complete if it is $D ^ { + }$ -complete, $D ^ { - }$ -complete, and $D ^ { \pm } .$ -complete.

(v) A (3, 2) game is hierarchically complete or H-complete if it is complete and the total rankings induced by $\succsim _ { D ^ { + } } , \succsim _ { D }$ −, and $D ^ { \pm }$ coincide.

For the game in Example 1.4 we have:

$$
\begin{array}{l l l l} D ^ {+}: & a \succ b, & c \succ a, & b \succ c, \\ D ^ {-}: & a \succ b, & c \succ a, & b \succ c, \\ D ^ {\pm}: & b \succ a, & a \succ c, & c \succ b. \end{array}
$$

The three relations $\succsim _ { D ^ { + } } , \succ _ { D }$ − and $\succeq _ { D ^ { \pm } }$ F are complete and therefore the game is complete, but not I-complete since none of these three relations is transitive.

The following result establishes some links between the different types of completeness. We say that two relations on $N , \succsim _ { 1 }$ and $\succsim _ { 2 } ,$ are never opposite i $\mathrm { f } p \succ _ { 1 }$ r and $\cdot \succ _ { 2 } p$ is impossible for any pair p, r of voters.

## Theorem 2.4.

(i) If (N,W) is H-complete, then $\succeq _ { H } \succeq _ { D ^ { + } } , \succeq _ { D ^ { - } } , \succeq _ { D ^ { \pm } }$ are transitive, coin cide with $\succsim _ { I } ,$ and (N,W) is I-complete.

(ii) If (N,W) is I-complete, then $\succsim$ is transitive, and $\succeq _ { I } , \succeq _ { D ^ { + } } , \succeq _ { D ^ { - } } , \succeq _ { D ^ { \pm } }$ are never opposite relations, and (N,W) is complete

## Proof.

(i) (N,W) being hierarchically complete implies that $\succsim _ { D ^ { + } } , \succsim _ { D }$ − and $\succsim _ { D ^ { \pm } }$ are complete and coincide.

Let p and r be two players. $p \succ _ { I }$ r is equivalent to $p { \succeq } _ { D ^ { + } } r , p { \succeq } _ { D ^ { - } } r$ and $p { \stackrel {  } { \sim } } _ { D ^ { \pm } } r ,$ and at least one of the three relations is strict; $p \approx r$ is equivalent to: $p { \approx } _ { D ^ { + } } r , ~ p { \approx } _ { D ^ { - } } r$ and $p { \approx } _ { D ^ { \pm } } r ;$ and since $\succsim _ { D ^ { + } } , \succsim _ { D ^ { - } }$ , and $\succsim _ { D ^ { \pm } }$ coincide, it is then obvious that: $\mathbf { \nabla } \cdot \mathbf { p } \succ _ { I }$ r implies $p \succ _ { D ^ { + } } r , p \succ _ { D }$ −r and $p \succ _ { D ^ { \pm } } r ,$ and

$p \approx _ { I }$ r implies $p { \approx } _ { D ^ { + } } r , p { \approx } _ { D ^ { - } } r$ and $p { \approx } _ { D ^ { \pm } } r .$

Thus $\succeq _ { I } , \succeq _ { D ^ { + } } , \succeq _ { D ^ { - } } \mathrm { a n d } \succeq _ { D ^ { \pm } }$ coincide; and $\succsim$ is complete since (N,W) is complete.

With respect to transitivity: I-completeness implies I transitivity (it was proved in [24]) and I-transitivity implies that $\succsim _ { D ^ { + } } , \succsim _ { D ^ { - } }$ and $\succsim _ { D ^ { \pm } }$ are transitive, since these relations coincide with $\succsim _ { I } .$

(ii) We remark again that I-completeness implies I-transitivity. Moreover, it is obvious that I-completeness implies that $\succeq _ { D ^ { + } }$ $\succsim _ { D ^ { - } }$ − , and $\succsim _ { D ^ { \pm } }$ are complete (see the de<sup>fi</sup>nition of ${ \succsim } _ { I } )$ , and therefore $( N , W )$ is complete. Let p and r be two players:

$p \succ _ { I }$ r implies $p { \gtrsim } _ { D ^ { + } } r , p { \gtrsim } _ { D }$ − r, and $p { \succsim } _ { D ^ { \pm } } r ,$ and

$p \approx _ { I }$ r implies $p { \approx } _ { D ^ { + } } r , p { \approx } _ { D ^ { - } } r ,$ and $p { \approx } _ { D ^ { \pm } } r .$

Hence, $\succeq _ { I } , \succeq _ { D ^ { + } } , \succeq _ { D ^ { - } }$ − and $\succsim _ { D ^ { \pm } }$ are never opposite relations. □

The transitivity of the in<sup>fl</sup>uence relation when the game is I-complete allows to talk about I-hierarchy of the (3, 2) game, i.e., the speci<sup>fi</sup>c total ranking for voters derived from the I-relation. Similarly we may consider the H-hierarchy for the game derived from the H-relation. A study on Ihierarchies for (3, 2) games can be found in [15].

## 3. Weighted and complete (3, 2) games: coherency

For simple games it is well-known that if a voter has a greater weight than another then the former voter is at least as desirable, as a coalitional partner, than the other. When three levels are introduced in the input this matter becomes more complex, however a “good” definition for desirability should be coherent with that of weightedness.

It is well known that for n N 5 there are simple games which are complete but not weighted. However, for $n > 2$ there exist (3, 2) games which are complete but not weighted, see e.g., Example 1.4. Next Proposition shows that for n = 2 all (3, 2) games are (strongly) weighted (Table 1).

It is also well known that for n N 3 there are simple games which are not complete. Thus, any example of a simple game non-being complete provides an example of a (3, 2) game non-being complete, where abstaining is tantamount to voting “no.” As for $n = 4$ there are three non-isomorphic simple games which are not complete, we conclude that for n N 3 (with the addition of null voters if necessary) there exist (3, 2) games which are not complete. However, next Proposition also shows that for n = 3 all (3, 2) games are complete.

Proposition 3.1. Every (3, 2) game with n = 2 is strongly weighted and every (3, 2) game with n = 3 is complete.

## Proof.

• Every (3, 2) game with $n = 2$ is complete, and moreover strongly weighted: see Table 1.

• Every (3, 2) game with n = 3 is complete.

Assume that (N,W) is a (3, 2) game such that $N = \{ a , b , c \} _ { \ast }$ Proof that (N,W) is D<sup>+</sup>-complete:

(⁎) Assume that the tripartition $( a , b , c )$ is winning, then the tripartitions (a,bc,∅) and (ac,b,∅) are winning as well. Hence, a $\succeq _ { D ^ { + } } b .$

(⁎⁎) Assume that the tripartition (a,bc,∅) is winning, then the tripartition (ac,b, ) is also winning. If $( a , b , c ) \notin W$ and $( b , a , c ) \in W ,$ then $( b , a c , \mathcal { D } ) \in W$ and $( b c , a , \emptyset ) \in W ,$ hence $b { \succsim } _ { D ^ { + } } a .$ If $( a , b , c ) \notin W$ and $( b , a , c ) \notin W ,$ then as $( a , b c , \emptyset ) \in W$ and $( a c , b , \emptyset ) \in W , a { \gtrsim } _ { D ^ { + } } b .$ If it reduces to (∗) and it reduces \*) and

If $( a , b , c ) \in W ,$ $a { \succsim } _ { D ^ { + } } b$ :

(⁎⁎⁎) Assume that $( a c , b , \emptyset ) \in W .$

If (a,bc,∅) ∈ W, it is (\*\*). If $( a , b c , \emptyset ) \not \in W$ and $( b , a c , \emptyset ) \in W ,$ it is (\*\*) with b playing the role of a. If (a,bc,∅) ∉ W and $( b , a c , \emptyset ) \not \in W ,$ then $( a c , b , \emptyset ) \in W ; ( a , b ,$ c) ∉ W and $( b , a , c ) \notin W ,$ , that is $a { \succsim } _ { D ^ { + } } b$

If the tripartitions (a,b,c), (a,bc,∅) and (ac,b,∅) are all not winning, then it is obvious that $b { \succeq } _ { D ^ { - } }$ a. Hence, $a { \succsim } _ { D ^ { \dagger } }$ b or $b { \succsim } _ { D ^ { + } } a$ : It is then easy to prove that $a { \succsim } _ { D ^ { + } }$ c or $c { \succsim } _ { D ^ { \dagger } }$ a and that $b { \stackrel {  } { \sim } } _ { D ^ { + } } c _ { 0 \Gamma } c { \stackrel {  } { \sim } } _ { D ^ { + } } b .$ Therefore, (N,W) is $D ^ { + } { \mathrm { - c o m p l e t e . } }$

The proofs that (N,W) is D<sup>−</sup>-complete and $D ^ { \pm } \mathrm { - c o m p l e t e }$ are analogous. □

Table 1  
List of (3, 2) games with n = 2 up to isomorphism.

<table><tr><td></td><td> $W^{n}$ </td><td>q</td><td>w(1)</td><td>w(2)</td><td>Hierarchy</td></tr><tr><td>1</td><td> $(12, \emptyset, \emptyset)$ </td><td>2</td><td> $(1, 0, 0)$ </td><td> $(1, 0, 0)$ </td><td> $1 \approx_{I} 2$ </td></tr><tr><td>2</td><td> $(1, 2, \emptyset)$ </td><td>1</td><td> $(1, 0, -1)$ </td><td> $(0, 0, -1)$ </td><td> $1 \succ_{I} 2$ </td></tr><tr><td>3</td><td> $(1, 2, \emptyset)$  and  $(2, 1, \emptyset)$ </td><td>1</td><td> $(1, 0, -1)$ </td><td> $(1, 0, -1)$ </td><td> $1 \approx_{I} 2$ </td></tr><tr><td>4</td><td> $(1, 2, \emptyset)$  and  $(2, \emptyset, 1)$ </td><td>1</td><td> $(1, 0, 0)$ </td><td> $(1, 0, -1)$ </td><td> $2 \succ_{I} 1$ </td></tr><tr><td>5</td><td> $(1, \emptyset, 2)$ </td><td>1</td><td> $(1, 0, 0)$ </td><td> $(0, 0, 0)$ </td><td> $1 \succ_{I} 2$ </td></tr><tr><td>6</td><td> $(1, \emptyset, 2)$  and  $(2, \emptyset, 1)$ </td><td>1</td><td> $(2, 0, -1)$ </td><td> $(2, 0, -1)$ </td><td> $1 \approx_{I} 2$ </td></tr><tr><td>7</td><td> $(1, \emptyset, 2)$  and  $(\emptyset, 12, \emptyset)$ </td><td>0</td><td> $(1, 0, -1)$ </td><td> $(0, 0, -1)$ </td><td> $1 \succ_{I} 2$ </td></tr><tr><td>8</td><td> $(1, \emptyset, 2)$  and  $(\emptyset, 2, 1)$ </td><td>0</td><td> $(1, 0, 0)$ </td><td> $(0, 0, -1)$ </td><td> $1 \approx_{I} 2$ </td></tr><tr><td>9</td><td> $(\emptyset, 12, \emptyset)$ </td><td>0</td><td> $(0, 0, -1)$ </td><td> $(0, 0, -1)$ </td><td> $1 \approx_{I} 2$ </td></tr><tr><td>10</td><td> $(\emptyset, 1, 2)$ </td><td>0</td><td> $(0, 0, -1)$ </td><td> $(0, 0, 0)$ </td><td> $1 \succ_{I} 2$ </td></tr><tr><td>11</td><td> $(\emptyset, 1, 2)$  and  $(\emptyset, 2, 1)$ </td><td>-1</td><td> $(0, 0, -1)$ </td><td> $(0, 0, -1)$ </td><td> $1 \approx_{I} 2$ </td></tr><tr><td>12</td><td> $(1, \emptyset, 2), (2, \emptyset, 1)$  and  $(\emptyset, 12, \emptyset)$ </td><td>0</td><td> $(1, 0, -1)$ </td><td> $(1, 0, -1)$ </td><td> $1 \approx_{I} 2$ </td></tr></table>

## 3.1. Weightedness implies completeness

The next result shows that “carrying” more weight implies being more desirable in the suitable level of approval. That's a useful result in order to connect weights and desirability relations and, further, to connect weightedness and completeness. Moreover, the next result is the main justi<sup>fi</sup>cation of the consideration of the three separate desirability orderings in De<sup>fi</sup>nition 2.1.

Theorem 3.2. Given two arbitrary players p and r in a weighted (3, 2) game, for any weighted representation of it, we have:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
(i)  $w^{+}(p) \geq w^{+}(r)$  implies  $p \gtrsim_{D^{+}} r$ ,
(ii)  $-w^{-}(p) \geq -w^{-}(r)$  implies  $p \gtrsim_{D^{-}} r$ , and
(iii)  $w^{+}(p) - w^{-}(p) \geq w^{+}(r) - w^{-}(r)$  implies  $p \gtrsim_{D^{\pm}} r$ .
</div>

## Proof.

(i) Assume that $w ^ { + } ( p ) \geq w ^ { + } ( r ) . \mathtt { A s } :$ V $\prime ( S _ { 1 } \cup p , S _ { 2 } \setminus p , S _ { 3 } ) = w ( S _ { 1 } , S _ { 2 } , S _ { 3 } ) + w ^ { + } ( p )$ and w( $S _ { 1 } \cup r , S _ { 2 } \mid r , S _ { 3 } ) = w ( S _ { 1 } , S _ { 2 } , S _ { 3 } ) + w ^ { + } ( r )$ it yields: $w ( S _ { 1 } \cup p , S _ { 2 } \cup p , S _ { 3 } ) \geq w ( S _ { 1 } \cup r , S _ { 2 } \cup r , S _ { 3 } ) ,$ , and therefore: $V ( S _ { 1 } \cup p , S _ { 2 } \cup p , S _ { 3 } ) \geq V ( S _ { 1 } \cup r , S _ { 2 } \cup r , S _ { 3 } )$ . Hence, $p { \succsim } _ { D ^ { + } } r .$ (ii) Assume $\mathrm { t h a t } - w ^ { + } ( p ) \geq - w ^ { + } ( r ) . \mathrm { A s } .$ V $\nu ( S _ { 1 } , S _ { 2 } \cup p , S _ { 3 } \cup p ) = w ( S _ { 1 } , S _ { 2 } , S _ { 3 } ) - w ^ { - } ( p$ ) and $w ( S _ { 1 } , S _ { 2 } \cup r , S _ { 3 } \cup r ) = w ( S _ { 1 } , S _ { 2 } , S _ { 3 } ) - w ^ { - }$ <sup>−</sup>(r), it yields: $w ( S _ { 1 } , S _ { 2 } \cup p , S _ { 3 } \setminus p ) \ge w ( S _ { 1 } , S _ { 2 } \cup r , S _ { 3 } \setminus r )$ and therefore: $V ( S _ { 1 } , S _ { 2 } \cup p , S _ { 3 } \setminus p ) \geq V ( S _ { 1 } , S _ { 2 } \cup r , S _ { 3 } \setminus r )$ . Hence, $p { \succeq } _ { D ^ { - } } r .$ (iii) Assume that $w ^ { + } ( p ) - w ^ { - } ( p ) \geq w ^ { + } ( r ) - w ^ { - } ( r )$ . As: $w ( S _ { 1 } \cup p ,$ $S _ { 2 } , S _ { 3 } \setminus p ) = w ( S _ { 1 } , S _ { 2 } , S _ { 3 } ) + ( w ^ { + } ( p ) - w ^ { - } ( p ) )$ and $w ( S _ { 1 } \cup r , S _ { 2 } ,$ $S _ { 3 } \setminus r ) w ( S _ { 1 } , S _ { 2 } , S _ { 3 } ) + ( w ^ { + } ( r ) - w ^ { - } ( r ) )$ it yields: $w ( S _ { 1 } \cup p ,$ S , $S _ { 3 } \mid p ) \geq w ( S _ { 1 } \cup r , S _ { 2 } , S _ { 3 } \mid r )$ and therefore: $V ( S _ { 1 } \cup p , S _ { 2 } ,$ $S _ { 3 } \mid p ) \geq V ( S _ { 1 } \cup r , S _ { 2 } , S _ { 3 } \mid r )$ . Hence, $p { \stackrel {  } { \sim } } _ { D ^ { \pm } } r . \boxed { \begin{array} { r l } \end{array} }$

Some important corollaries are derived from the previous result

Corollary 3.3. Every weighted (3, 2) game is a complete (3, 2) game for which the three relations $\succsim _ { D ^ { + } } , \succsim _ { D ^ { - } }$ and $\succeq _ { D ^ { \pm } }$ are transitive.

Proof. It follows from Theorem 3.2 since for every two arbitrary players either $w ^ { + } ( p ) \geq w ^ { + } ( r )$ or $w ^ { + } ( p ) \leq w ^ { + } ( r )$ . Hence, either p $\stackrel { \textstyle \sum _ { D ^ { + } } } { \sim } r \ : 0 \mathrm { r } \ : r \stackrel { \textstyle \sum _ { D ^ { + } } } { \sim } p ;$ and the same occurs for relations $\succsim m ^ { - }$ and $\succeq _ { D ^ { \pm } }$ Moreover, i $\mathrm { f } p , r , s \in N$ with $w ^ { + } ( p ) \geq w ^ { + } ( r ) \geq w ^ { + } ( s )$ , then $p { \stackrel {  } { \sim } } _ { D ^ { + } } r , r$ $\succeq _ { D ^ { \dagger } }$ s and also $p { \succsim } _ { D ^ { + } } s$ . Similar reasonings apply to $\succsim _ { D }$ − and $\succeq _ { D ^ { \pm } }$ respectively. □

Corollary 3.4. A strongly weighted (3, 2) game is an I-complete (3, 2) game.

Proof. It follows from Theorem 3.2 since strongly weightedness for the game implies that for any two arbitrary voters p and r either $[ p / \approx _ { D ^ { + } } r , p$ c − r and $p { \succeq } _ { D ^ { \pm } } r ]$ or $[ r { \stackrel {  } { \sim } } _ { D }$ p, rc − p and $r { \succeq } _ { D ^ { \pm } } p ]$ which implies p c<sub>I</sub> r or $r \succsim _ { I } p ,$ , and therefore I-completeness for the game. □

The following three items summarize the most important results of this section:

(i) Completeness and transitivity of the three separate relations considered is a necessary but not suf<sup>fi</sup>cient condition for a (3, 2) game to be weighted.

(ii) Strongly weighted (3, 2) games are weighted (3, 2) games being I-complete. I-completeness, which implies transitivity for $\succsim _ { I }$ is a necessary but not suf<sup>fi</sup>cient condition for a (3, 2) game to be strongly weighted.

(iii) There exist (3, 2) games which are weighted but not I-complete.

Note that (i) is the desired property, linking weightedness and completeness, for (3, 2) games that we were looking for and which is the analogous for simple games for which weighted games are complete; (ii) tells us that I-completeness, which is a stronger condition than completeness, is a necessary condition for a (3, 2) game to be strongly weighted, whereas (iii) points out the existence of weighted (3, 2) games non-being I-complete.

## Remark 3.5.

$$
w ^ {+} (p) \geq w ^ {+} (r)
$$

$$
- w ^ {-} (p) \geq - w ^ {-} (r)
$$

$$
p \gtrsim_ {D ^ {+}} r
$$

$$
p \gtrsim_ {D}
$$

$$
p \gtrsim_ {D ^ {\pm}} r,
$$

$$
p \gtrsim_ {D ^ {\pm}} r
$$

(ii) $w ^ { + } ( p ) > w ^ { + } ( r )$ imply $p { \succsim } _ { D ^ { + } } r ,$ but not necessarily implies $p \succ _ { D ^ { + } } r .$ Analogously, $- \ : w ^ { - } ( p ) > - \ : w ^ { - } ( r ) \ :$ implies $p { \succsim } _ { D ^ { - } } r ,$ but not necessarily implies $p \succ _ { D ^ { - } } r .$ Analogously, $w ^ { + } ( p ) - w ^ { - } ( p ) > w ^ { + } ( r ) -$ $w ^ { - } ( r )$ implies $p { \stackrel {  } { \sim } } _ { D ^ { \pm } } r ,$ , but not necessarily implies $p \succ _ { D ^ { \pm } } r .$

## 4. Swap robustness

The purpose of this section is to provide necessary and suf<sup>fi</sup>cient conditions for a (3, 2) game to be complete in terms of swaps among tripartitions. To this purpose we previously need to give necessary and suf<sup>fi</sup>cient conditions in terms of swaps among tripartitions for the completeness of the game for each of three relations: $\succeq _ { D ^ { + } } , \succeq _ { D ^ { - } } , \succeq _ { D ^ { \pm } }$

## De<sup>fi</sup>nition 4.1.

(i) A (3, 2) game is swap<sup>+</sup>-robust if for all $S , T \in W , p \in S _ { 1 } \cap T _ { 2 }$ and $r \in S _ { 2 } \cap T _ { 1 }$ either $( ( S _ { 1 } \lor p ) \cup r , ( S _ { 2 } \lor r ) \cup p , S _ { 3 } )$ wins or $( ( T _ { 1 } \lor r ) \cup p , ( T _ { 2 } \lor p ) \cup r , T _ { 3 } )$ wins.

(ii) $\mathsf { A } ( 3 , 2 )$ game is swap<sup>−</sup>-robust if for all $S , T \in W , p \in S _ { 2 } \cap T _ { 3 }$ and $r \in S _ { 3 } \cap T _ { 2 }$ either $( ( S _ { 1 } , ( S _ { 2 } \lor p ) \cup r , ( S _ { 3 } \lor r ) \cup p )$ wins or ((T , $( T _ { 2 } \setminus r ) \cup p , ( T _ { 3 } \setminus p ) \cup r )$ wins.

(iii) $\mathsf { A } \left( 3 , 2 \right)$ game is swap<sup>±</sup>-robust if for all $S , T \in W , p \in S _ { 1 } \cap T _ { 3 }$ and $r \in S _ { 3 } \cap T _ { 1 }$ either $( ( S _ { 1 } \lor p ) \cup r , S _ { 2 } , ( S _ { 3 } \lor r ) \cup p )$ wins or $( ( T _ { 1 } \setminus r ) \cup p , T _ { 2 } , ( T _ { 3 } \setminus p ) \cup r )$ wins.

(iv) A (3, 2) game is swap-robust if and only if it is swap<sup>+</sup>-robust, swap<sup>−</sup>-robust and swap<sup>±</sup>-robust.

A given (3, 2) game (N,W) is swap<sup>+</sup>-robust means that for any two winning tripartitions S and T, two players p and r such that p is a yesvoter in S while being an abstainer in T, r is an abstainer in S while being a yes-voter in T, the permutation of p and r between S and T yields two tripartitions for which at least one is still winning.

Mutatis mutandis the same reading for swap<sup>−</sup>-robustness and $\mathsf { s w a p } ^ { \pm } \mathrm { - r o b u s t . }$

## Proposition 4.2.

(i) A (3, 2) game is $D ^ { + }$ -complete if and only if it is swap<sup>+</sup>-robust.

(ii) A (3, 2) game is D<sup>−</sup>-complete if and only if it is swap<sup>−</sup>-robust.

(iii) A (3, 2) game is $D ^ { \pm }$ -complete if and only if it is $s w a p ^ { \pm }$ -robust. (iv) A (3, 2) game is complete if and only if it is swap-robust.

## Proof.

(i) (⇒) Assume that (N,V) is $D ^ { + }$ -complete. Let p and r be two arbitrary abstainers. As V is $D ^ { + }$ -complete either $p { \gtrsim } _ { D ^ { + } } r \ { 0 } \Gamma r { \gtrsim } _ { D ^ { + } } p . \ A s -$ sume w.l.o.g. $r { \stackrel {  } { \sim } } _ { D ^ { + } } p$ , and consider two arbitrary winning tripartitions S and T with $p \in S _ { 1 } \cap T _ { 2 }$ and $r \in S _ { 2 } \cap T _ { 1 } ,$ , then $( ( S _ { 1 } \lor p ) \cup r , ( S _ { 2 } \lor r ) \cup p , S _ { 3 } )$ wins since $r { \succeq } _ { D ^ { + } } p . ~ ( \Leftarrow )$ Assume that V is swap<sup>+</sup> robustness, w.l.o.g. assume that $S , T$ (with $p \in S _ { 1 } \cap T _ { 2 }$ and $r \in S _ { 2 } \cap T _ { 1 } )$ and $( ( S _ { 1 } \lor p ) \cup r , ( S _ { 2 } \lor r ) \cup p , S _ { 3 } )$ are winning tripartitions. Let $B = ( B _ { 1 } , B _ { 2 } , B _ { 3 } ) = ( S _ { 1 } \setminus p , S _ { 2 } \cup p ,$ $S _ { 3 } ) _ { \mathrm { { t } } }$ , then $p , \ r \in B _ { 2 }$ and $1 = V ( B _ { 1 } \cup r , B _ { 2 } \lor r , B _ { 3 } ) \geq V ( B _ { 1 } \cup p$ $B _ { 2 } \setminus { \mathfrak { p } } , B _ { 3 } )$ which implies $r _ { D ^ { + } } p .$

(ii) Mutatis mutandis the same.

(iii) Mutatis mutandis the same.

(iv) It follows from the three previous items. □

Note that Tchantcho et al. [24] gave a similar characterization for I-completeness in terms of swaps among tripartitions (called here Iswap robustness). Of course, I-swap robustness implies swap robustness, while the converse is not true.

## 5. Conclusion

Unlike the desirability relation de<sup>fi</sup>ned for (3, 2) games for which every weighted game is complete, there exist weighted (3, 2) games that are not complete under the in<sup>fl</sup>uence relation (I-in<sup>fl</sup>uence) introduced and studied by Tchantcho et al. [24]. Indeed, this relation is very strong. We consider as in [18] the three separate relations that compose the in<sup>fl</sup>uence relation de<sup>fi</sup>ned in [24]. The completeness of each of these relations is a necessary condition for a (3, 2) game to be weighted. Moreover, the completeness of the I-in<sup>fl</sup>uence relation is a necessary condition for a (3, 2) game to be a strongly weighted (3, 2) game.

One major concern of the paper [24] is to link the I-in<sup>fl</sup>uence relation to the extension of Shapley-Shubik, Banzhaf, and the two Coleman preorderings introduced in [6–8] respectively. One future of this work is to proceed to such comparisons. Another work concerns the study of different power indices for games with a priori unions in the context of games with abstention, as is mainly done in [2] for simple games.

Finally, it is worth noting that although this paper deals with (3, 2) games, all the results obtained in Sections 2, 3 and 4 can be easily extended to (j,2) games.

## Acknowledgments

The authors are grateful to the three referees of this paper for their interesting comments that contributed to improve the original submitted version.

## References

[1] J. Abdou, H. Keiding, Effectivity functions in social choice, Kluwer Academic Publishers, 1991.

[2] J.M. Alonso-Meijide, F. Carreras, M.G. Fiestras-Janeiro, G. Owen, A comparative axiomatic characterization of the Banzhaf–Owen coalitional value, Decision Support Systems 43 (2007).701-712

[3] P. Bharati, A. Chaudhury, An empirical investigation of decision-making satisfaction in web-based Decision Support Systems, Decision Support Systems 37 (2004) 187–197.

[4] P.P. Côrte-Real, P.T. Pereira, The voter who wasn't there: referenda, representation and abstention, Social Choice and Welfare 22 (2004) 349–369.

[5] P.C. Fishburn, The theory of social choice, Princeton University Press, Princeton, 1973.

[6] J. Freixas, Banzhaf measures for games with several levels of approval in the input and output, Annals of Operations Research 137 (2005) 45–66.

[7] J. Freixas, The Shapley–Shubik power index for games with several levels of approval in the input and output, Decision Support Systems 39 (2005) 185–195.

[8] J. Freixas, Probabilistic power indices for voting rules with abstention, Mathematical Social Sciences 64 (2012) 89–99

[9] J. Freixas, W.S. Zwicker, Weighted voting, abstention, and multiple levels of approval, Social Choice and Welfare 21 (2003) 399–431.

[10] J. Freixas, W.S. Zwicker, Anonymous yes–no voting with abstention and multiple levels of approval Games and Economic Behavior 69 (2009) 428–444

[11] E.J. Garrity, B. Glassberg, Y.J. Kim, G.L. Sanders, S.K. Shin, An experimental investigation of web-based information systems success in the context of electronic commerce, Decision Support Systems 39 (2005) 483–503.

[12] J. Greenberg, The theory of social situations: an alternative game—theoretic approach, Cambridge University Press, 1991.

[13] J.R. Isbell, A class of simple games, Duke Mathematics Journal 25 (1958) 423–439.

[14] H. Moulin, Axioms of cooperative decision making, Cambridge University Press, 1988.

[15] C. Parker, The in<sup>fl</sup>uence relation for ternary voting games, Games and Economic Behavior 75 (2012) 867–881.

[16] B. Peleg, Game theoretic analysis of voting in committees, Cambridge University Press. 2008.

[17] B. Peleg, H. Peters, Strategic social choice: stable representations of constitutions, Springer, 2010.

[18] R. Pongou, B. Tchantcho, L. Diffo Lambo, Political in<sup>fl</sup>uence in multi-choice institutions: cyclicity, anonymity, and transitivity, Theory and Decision 70 (2011) 157–178.

[19] A. Rubinstein, Stability of decision systems under majority rule, Journal of Economic Theory 23 (1980) 150–159.

[20] A.D. Taylor, A. Pacelli, Mathematics and Politics, 2nd ed. Springer Verlag, New York, USA. 2008.

[21] A.D. Taylor, W.S. Zwicker, A characterization of weighted voting, Proceedings of the American Mathematical Society 115 (1992) 1089–1094.

[22] A.D. Taylor, W.S. Zwicker, Weighted voting, multicameral representation, and power, Games and Economic Behavior 5 (1993) 170–181.

[23] A.D. Taylor, W.S. Zwicker, Simple games: desirability relations, trading, and pseudoweightings, Princeton University Press, New Jersey, USA, 1999.

[24] B. Tchantcho, L. Diffo Lambo, R. Pongou, B. Mbama Engoulou, Voters' power in voting games with abstention: in<sup>fl</sup>uence relation and ordinal equivalence of power theories, Games and Economic Behavior 64 (2008) 335–350.

[25] P.V. Uleri, On referendum voting in Italy: YES, NO, or non-vote? How Italian parties learned to control referendums, European Journal of Political Research 41 (2002) 863–883.

[26] W.S. Zwicker, Anonymous voting rules with abstention: weighted voting, in: S.J. Brams, W.V. Gehrlein, F.S. Roberts (Eds.), The Mathematics of Preference, Choice, and Order: Essays in Honor of Peter C. Fishburn, Springer, Heidelberg, 2009, pp. 239–258.

Josep Freixas received the Ph.D in Mathematics from the Technical University of Catalonia, in 1994. He works in the Department of Applied Mathematics 3 and in the High Engineering School of Manresa. He was a visiting professor in the Bergamo University (Italy) in 1996 and in the Union College of Schenectady in New York (USA) in 2000. His research interests include Decision and Game Theory, Reliability and Computer Sciences. He has pub lished papers on these topics and gave several invited lectures in different universities. He was an advisor of several Ph.D students. He is currently leading a research project on Game Theory and Decision-Making.

Bertrand Tchantcho received the Ph.D in Mathematics from the University of Yaounde I in Cameroon in 2004. He is a permanent associate professor at the Advanced Teachers' Training College, and one of the faculties of the University of Yaounde I. His research interests include Game Theory and Social Choice Theory. He is a member of the Applied Mathematics to Social Sciences of the University of Yaounde I and associate researcher at the THEMA laboratory of the University of Cergy-Pontoise in France. He was a visiting professor in many countries including USA, France and Benin.

Narcisse Tedjeugang is currently a Ph.D student in Applied Mathematics to Social Sciences in the University of Yaounde I.

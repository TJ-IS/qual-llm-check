---
otero_id: 15974
otero_key: "45JYK22K"
title: "The Shapley–Shubik power index for games with several levels of approval in the input and output"
authors: "Josep Freixas"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.10.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Shapley–Shubik power index for games with several levels of approval in the input and output

Josep Freixas

Department of Applied Mathematics III, Polytechnic School of Manresa, Polytechnic University of Catalonia Av. Bases de Manresa 61-73, Manresa 08240, Barcelona, Spain

Available online 1 December 2003

## Abstract

Voting systems with several levels of approval in the input and output are considered in this paper. That means games with n 2 players, j 2 ordered qualitative alternatives in the input level and k 2 possible ordered quantitative alternatives in the output. We introduce the Shapley –Shubik power index notion when passing from ordinary simple games or ternary voting games with abstention to this wider class of voting systems. The pivotal role of players is analysed by means of several examples and an axiomatization in the spirit of Shapley and Dubey is given for the proposed power index. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

JEL classification: C71; D71

Keywords: ( j, k) simple games; Several levels of approval; Abstention; Shapley– Shubik index; AMS, 91A12; 91A40; 91A80; 91C15

## 1. Introduction, summary and background

The use of game theory to study the distribution of power in voting systems can be traced back to the invention of simple games by Von Neumann and Morgenstern [19] in their 1944 classic, Theory of Games and Economic Behavior. The definition of simple games covers most of the familiar examples of constitutional political machinery, among them weighted voting, direct majority rule, relative majority rule, bicameral or multicameral legislatures, veto situations, etc.

Several approaches yield indices which can be interpreted directly in terms of the a priori ability of the players to affect the outcome. The two most conspicuous representatives of this line of research are the Shapley –Shubik power index [8,17,18] and the Banzhaf–Coleman power index [2,7]. A wide collection of studies providing different axiomatizations and other power indices notions has been developed since then by several scientists.

In practice when considering voting systems it is observed that abstention plays a key role in many of the real voting systems that have been modelled by these games (such as the United Nations Security Council, or the United States federal system), yet simple games, by their very nature, cannot take the possibility of abstention into account; those who do not vote ‘yes’ are presumed to vote ‘no’. Indeed, Felsenthal and Machover ([11], p. 22) have remarked on the extent to which some authors ‘misreport the rules as though abstention were not a distinct option and offer the hypothesis that ‘the misreporting is due to what philosophers of science have called theoryladen or theory-biased observation—a common occurrence, akin to optical illusion, whereby an observer’s perception is unconsciously distorted so as to fit a preconception’ ([11], p. 280, as well as [10,12]).

One factor that may have hindered the study of games with multiple levels of approval is the absence of a completely satisfactory definition of weighted voting in this context. Indeed, for ( j, k) simple games introduced by Freixas and Zwicker [14], a natural weighted notion is proposed and a combinatorial characterization is given in terms of ‘grade trade robustness’ for weighted ( j, k) games within the class of all ( j, k) simple games. The framework models voting systems which meet the following conditions: (a) several levels of approval are permitted in the input, say j, (b) several levels of approval are permitted in the output, say k, and (c) those levels are qualitatively ordered.

Here we intend to provide an a priori Shapley – Shubik (S–S) power index for ( j, k) simple games. In these games, each individual voter expresses one of j possible levels of input support, and the output consists of one of k possible levels of collective support. Standard simple games are (2, 2) simple games, (3, 2) simple games allow each voter a middle option, which may be interpreted as ‘I abstain.’ In a seminal work by Felsenthal and Machover ([11], pp. 291 – 293) it is proposed a Shapley –Shubik power index notion for ternary voting systems (our (3, 2) simple games with abstention). Here we will extend their approach to ( j, k) simple games, a topic being its derivation from axioms closely related to Dubey and Shapley’s axiomatization [9] for simple games.

Revising the literature on the several attempts to generalize simple games we find that the most relevant examples of ( j, k) simple games are those were abstention plays a key role. Several real voting systems have been modelled by these games, such as the United Nations Security Council, or the United States federal system. An important and isolated earlier work on abstention can be found in Fishburn ([13], pp. 53 –55). Fishburn’s context can be viewed as a special case of our ( j, k) simple games (in which $j = 3 = k ,$ , the game is constant-sum, and the intermediate output level of approval is only achieved when the vote is tied exactly). More recently, several works by Felsenthal and Machover [10 – 12] have been devoted to the study of voting systems with abstention, and outline the rudiments of a theory of a priori voting power with abstention. Their ‘ternary voting rules’ correspond to our (3, 2) simple games with the three input alternatives: ‘yes,’ ‘abstention’ and ‘no.’ In the alternative model proposed by Braham and Steffen [6], abstention does not really figure expressing an intermediate degree of support between ‘yes’ and ‘no.’

Classical cooperative games have given rise to several generalizations, related to our model, but distinguished in part by the fact that the output of a cooperative game is a cardinal value rather than a discrete level in a finite ordering. Bolger [3–5] deals with the so-called games with n players and r alternatives, in which the r possible inputs are not ordered; each input alternative j attracts its own coalition of supporting voters, and each such coalition is assigned an output cardinal value (so that the total output is an r-tuple of cardinal values). In particular he develops a Shapley value for such class. More recently, Magan˜a [16], and Amer et al. [1] introduce the closely related r-games and define the Shapley –Shubik index for this type of games. Hsiao and Raghavan [15] consider multi-choice games and defined a Shapley value for that class considering that different actions carry different weights. In their context the inputs are ordered (each agent has an ‘effort level’), and the output is a single cardinal value. However, their notion of monotonicity ([15], Definition 2 p. 243) differs from ours.

Let us briefly outline the contents of this paper. Section 2 deals with notation, definitions, the formal description of the class of ( j, k) simple games and several examples. Section 3 defines the S –S power index for ( j, k) simple games and relates it to an explanatory probability model; the pivotal role of player is also developed. Taking as reference the examples introduced in Section 2, Sections 4 and 5, illustrates how to calculate the S–S power index for the ( j, 2) and ( j, k) cases, respectively. Finally, Appendix A shows how to derive the S –S power index from a set of axioms for the ( j, 2) case. As Felsenthal and Machover points out in their book: ‘The theory of voting power in ternary voting systems is in its infancy, and much remains to be discovered’. This paper tries to be a small insight in this research line.

## 2. The class of ( j, k) simple games

The material on this section is essentially taken from Freixas and Zwicker [14]. Before the main notions are introduced we need some preliminary definitions. An ordered j-partition of the finite set $N$ is a sequence $\scriptstyle A = \left( _ { 1 } A , \dotsc , A \right)$ of mutually disjoint sets whose union is N. Any $_ { i } A$ is allowed to be empty, and we think of $_ i A$ as the set of those voters of N who vote approval level i for the issue at hand (where approval level 1 is the highest level of approval, 2 is the next highest, etc.), $\mid { } _ { i } A \mid$ means de cardinality of $_ { i } A .$ . Thus, an ordered j-partition is the analogue of a coalition for a standard simple game. Let <sup>j</sup>N denote the set of all ordered j-partitions of N. For $X , \ Y \in ^ { j } N ,$ , we write $X ^ { j } \subseteq Y$ to mean that either $X { = } Y$ or X may be transformed into $Y$ by shifting 1 or more voters to higher levels of approval. This is the same as saying $_ { i } X \uparrow \subseteq Y \uparrow$ for each $i = 1 , 2 , . . . , j ;$ where ${ } _ { i } X \uparrow$ denotes ${ } _ { 1 } X \cup { } _ { 2 } X \cup { } . . . \cup { } _ { i } X$ for each $i = 1 , 2 , . . . , j ;$ we write $X ^ { j } \subset Y { \mathrm { i f } } X ^ { j } \subseteq Y$ and $X \neq ~ Y .$ The $^ j \subseteq$ order defined on $^ j N$ has minimum: the j-partition $\mathcal { N }$ such that ${ \mathrm { \Omega } } _ { j } \mathcal { N } = N ,$ and maximum: the $j -$ partition M such that $\mathsf { 1 } \mathcal { M } = N ;$ i.e. for every $j -$ partition A we have $\mathcal { N } ^ { j } \subseteq \boldsymbol { A } ^ { j } \subseteq \mathcal { M }$

Definition 2.1. A $( j , k )$ hypergraph $G = ( N , V )$ consists of a finite set N together with a value function V: $^ j N \longrightarrow \{ \nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { k } \}$ ; here $\{ \nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { k } \}$ is the value set of $G ,$ whose members are any k objects equipped with a strict linear ordering $\nu _ { 1 } { > } \nu _ { 2 } { > } . . { > } \nu _ { k }$

For ordered j-partitions X and Y we write $X { < _ { V } Y }$ to mean $V ( X ) < V ( Y )$ and $X { \le _ { V } Y }$ to mean $V ( X ) \leq V ( Y )$

Definition 2.2. A ( j, k) simple game is a $( j , \ k )$ hypergraph such that $V ( \mathcal { N } ) < V ( \mathcal { M } )$ and is monotonic: for all ordered j-partitions X and Y, if $X ^ { j } \subseteq Y$ then $X { \le _ { V } } Y .$

An ordinary simple game may be identified with a (2, 2) simple game for which the value set is $\{ w i n .$ lose} with win>lose, and a simple game with ties corresponds to a $( 2 , 3 )$ game with value set {win, tie, lose} and win >tie >lose. From Definition 2.2 it follows that a value function V might not necessarily be exhaustive. If this property fails for some V we will specify by $\{ \nu _ { i _ { 1 } } , ~ \nu _ { i _ { 2 } } , . . . , ~ \nu _ { i _ { r } } \}$ the images set of V contained in $\{ \nu _ { i _ { 1 } } , \nu _ { i _ { 2 } } , . . . , \nu _ { k } \}$ with $\nu _ { 1 } \geq \nu _ { i _ { 1 } } > \nu _ { i _ { 2 } } > . ~ . ~ . >$ $\nu _ { i _ { r } } \ge \nu _ { k }$

For some specific integers $j \geq 2$ and $k \geq 2$ the symbol $C ^ { j , k } ( N )$ will denote the set of all $( j , k )$ simple games on N. To every $( j , k )$ simple game we may consider a real numeric evaluation a: $\{ \nu _ { 1 } , . . . . , \nu _ { k } \} \to \mathbb { R } ^ { k } .$ for each element in the value set $\{ \nu _ { 1 } , . . . . , \nu _ { k } \}$ , it is assigned $\alpha ( \nu _ { i } ) { = } \alpha _ { i }$ conserving the order, i.e. $\mathsf { \alpha } _ { i } { > } \mathsf { \alpha } _ { i } + 1$ for each $1 \leq i \leq k - 1$ . We agree to normalize every numeric evaluation in the lowest level assigning $\boldsymbol { \alpha } _ { k } = 0$ . The uniform numeric evaluation is defined as the map ${ \mathfrak { x } } = \mu$ such that $\mu _ { i } = k - i , 1 \leq i \leq k .$

Definition 2.3. For every (N, V) and a real numeric evaluation a the associated $( j , k )$ simple game is (N, a j V) or, briefly, $( N , ^ { \alpha } V )$

What we are really doing in considering this new game is assigning a quantitative numeric output set instead of a qualitative ordered output set.

Notice that an ordinary simple game is a (2, 2) simple game with the uniform numeric evaluation. For some numeric evaluation a and some concrete integers $j \geq 2$ and $k \geq 2$ the symbol ${ } ^ { \alpha } C ^ { j , k } ( N )$ will denote the set of all $( j , k )$ simple games on N with numeric evaluation a. If the number of approval levels in the output is $k = 2$ then 1 is always assigned to $\cdot _ { \mathrm { W i n } } \cdot$ and 0 to $\mathbf { \bar { \rho } } _ { \mathrm { l o s e } } ,$ (in such case the game will be denoted by V instead of ${ } ^ { \mu } { V } { ) } { ; }$ otherwise, if $k { > } 2$ , the numeric evaluation $\alpha ,$ may be interpreted as a numeric measure of each element in the value set $\{ \nu _ { 1 } , . . . . , \nu _ { k } \}$ : if a $j -$ partition reaches $\nu _ { i }$ and after some changes in the players’ vote preferences converts into another $j -$ partition that reaches $\nu _ { m }$ with $\nu _ { m } { > } \nu _ { i } ,$ the collective utility award of this modification is measured as $\mathfrak { X } _ { m } - \mathfrak { X } _ { i }$ . For different situations, different numeric values arise. Associated with the numeric evaluation a we introduce the vector of consecutive level differences $d { = } ( d _ { 1 } , . . . . , d _ { k - 1 } )$ defined as: $d _ { i } = \alpha _ { i } - \alpha _ { i + 1 } ,$ $1 \leq i \leq k - 1$ . This vector completely determines a because we are assuming $\boldsymbol { \alpha } _ { k } = 0$ . Notice that the vector of consecutive level differences associated to the uniform numeric evaluation, $\mu ,$ is $d _ { i } = 1 , 1 \le i \le k - 1$

In a ( j, 2) simple game the notions of winning and minimal winning coalitions can be extended: $X$ is a winning j-partition whenever $V ( X ) = \nu _ { 1 } ,$ X is a minimal winning j-partition whenever X is winning and Y is a losing j-partition if $Y ^ { j } { \subset } X .$ These definitions can easily be extended to $( j , k )$ games, an X j-partition such that $V ( X ) = \nu _ { i }$ is i-winning for $i = 1 , . . . , k - 1 ;$ an X j-partition such that $V ( X ) = \nu _ { i }$ is i-minimal for $i = 1 , \ldots , k { - } 1 ;$ ; whenever $V ( Y < \nu _ { i }$ if $Y ^ { j } \subseteq X .$ We conclude the main definition of this section recalling what is meant by a weighted $( j , k )$ simple game.

Definition 2.4. Let $G = ( N , V )$ be a $( j , k )$ simple game. A representation of $G$ as a weighted $( j , k )$ simple game consists of a sequence $w { = } ( w _ { 1 } , . . . . w _ { \mathrm { j } } )$ of $j$ weight functions, where w<sub>i</sub>: $N \longrightarrow$ R for each i, together with $k - 1$ real number quotas $q _ { 1 } \geq q _ { 2 } \geq . . . \geq q _ { k - 1 }$ such that for every j-partition X and every r with $1 \leq r \leq k .$ $V ( X ) = \nu _ { r }$ if and only if $q _ { r - 1 } > w ( X ) \geq q _ { r } ,$ , where w(X) denotes

$$
\Sigma \{\Sigma \{w _ {i} (x): x \in_ {i} X \}: 1 \leq i \leq j \}
$$

and we think of $q _ { 0 }$ and $q _ { k }$ as having nominal values of $+ \infty$ and $- \infty$ , respectively. We say that $G { = } ( N ,$ $\boldsymbol { V } )$ is a weighted $( j , k )$ simple game if it has such a representation.

In what follows, we describe some examples that will be useful to illustrate the used terminology of this section and to calculate, in Sections 4 and 5, the S–S power index we will be introduced in Section 3. All the examples are weighted and it is left to the reader given a representation of them using weights and quotas in the sense of Definition 2.4.

Example 2.5. Consider the example 8.3.7 given by Felshental and Machover ([12], p. 288). Let (N, V) be the ternary voting rule $( j = 3$ and $k = 2 ;$ in our context, and the three alternatives are to vote $\cdot _ { \mathrm { y e s , \vec { \mathbf { \tau } } } } ,$ ‘abstention’ or ‘no’) with assembly $N { = } \{ 1 , 2 , 3 \}$ , where a bill is passed if player 1 votes for it and at least one of the other two does not oppose it. This game has two minimal winning three-partitions (we omit brackets): $A { = } ( 1 , 2 , 3 )$ and $B { = } ( 1 , 3 , 2 )$

Example 2.6. A resolution is carried in the Security Council if at least nine members support it and no permanent member is explicitly opposed, our formal description of the UNSC as a (3, 2) game is as follows: let $P { = } \{ 1 , 2 , 3 , 4 , 5 \}$ and $R { = } \{ 6 , 7 , . . . . , 1 5 \}$ be, respectively, the set of permanent members and nonpermanent members, and

$$
\begin{array}{l} V (A) = V (_ {1} A, _ {2} A, _ {3} A) \\ = \left\{ \begin{array}{l l} \text { win } & \text { if   } | _ {1} A | \geq 9 \text {   and   } _ {3} A \cap P = \emptyset \\ \text { lose } & \text { otherwise } \end{array} \right. \end{array}
$$

Here, we think of $_ { 1 } A$ as the set of voters of N who vote ${ \mathrm { \Sigma ^ { 6 } y e s } } , { \mathrm { \Sigma } } _ { 2 } A$ as the set of those voters of N who abstain, and $_ { 3 } A$ as the set of those voters of N who vote $\cdot _ { \mathrm { n 0 . } }$

Example 2.7. Let (N, V) be the quaternary voting rule $( j = 4$ and k = 2 in our context) with $n = 4$ players, namely 1, 2, 3 and 4. Each voter may express strong support, marginal support, weak opposition, or strong opposition to a certain proposed motion. The bill will pass only under one of the following scenarios:

1. Player 1 expresses strong support, player 2 shows at least marginal support, and furthermore player 3 is not strongly opposed.

2. Player 1 expresses strong support, player 3 shows at least marginal support, and furthermore player 2 is not strongly opposed.

That game has two minimal winning four-partitions (we omit brackets): $A = ( 1 , 2 , 3 , 4 )$ and $B { = } ( 1 , 3 , 2 , 4 )$

Example 2.8. The board of directors of a business company is considering to renew an important amount of personal computers. They will take a decision among the three following possibilities:

1. to buy $\alpha _ { 1 }$ new computers,

2. to buy only $\alpha _ { 2 }$ new computers $( x _ { 1 } > x _ { 2 } )$

3. not to buy, at the present moment, any new computer.

The final decision is taken according to the votes of the president = 1 and the vice-president = 2 of the company. Each one of them votes for carrying out a ‘high investment’ in new computers, a ‘partial investment’ or for ‘postponing’ the final decision. Of course, these three options show an induced order: high investment> partial investment> postponement. The final decision is taken according to the following scenarios:

1. It will be bought $\alpha _ { 1 }$ new computers if the president is in favour of doing a ‘high investment’ and the vicepresident does not vote for the ‘postponement’.

2. It will be bought $\alpha _ { 2 }$ new computers if either the president is in favour of doing a ‘high investment’ and the vice-president votes for ‘postponement,’ or the president votes for ‘partial investment’ and the vice-president votes for ‘high investment’.

Example 2.9. (Example taken from Freixas and Zwicker [14].) The last step in obtaining the engineering degree at the Polytechnic School of Manresa is an evaluation of each student’s final project. The grading system for this evaluation is similar to those in use at other schools in the Polytechnic University of Catalonia. The academic committee is formed by three professors who evaluate students. Each professor evaluates a different aspect: one assesses the theoretical contents, another the laboratory training, and the last considers the exercises and developments written by the student. Each student is then assigned a single, final mark compounded from the separate marks proposed by the three professors. The possible final marks that a student can get are: excellent $( \nu _ { 1 } )$ , notable or creditable $( \nu _ { 2 } )$ , pass $( \nu _ { 3 } )$ , and fail $( \nu _ { 4 } )$ . The possible marks that a professor may assign are: right (right votes are clustered in $_ { 1 } M )$ , regular (regular votes are clustered in $_ { 2 } A )$ and wrong (wrong votes are clustered in $_ { 3 } A )$ and the rule that determines final marks is given by the following (3, 4) game:

(b)

$$
\begin{array}{l} V (_ {1} A, _ {2} A, _ {3} A) \\ = \left\{ \begin{array}{l l} \text { excellent } & \text { if   } \operatorname{pra} \in_ {1} A, | _ {1} A | \geq 2, _ {3} A = \emptyset \\ \text { notable } & \text { if   } _ {3} A = \emptyset \text { and } (_ {1} A = \{\operatorname{pra} \} \text { or } _ {2} A = \{\operatorname{pra} \}) \\ \text { pass } & \text { if   } | _ {1} A | = 1, | _ {2} A | = 2, \operatorname{pra} \in_ {2} A; o r | _ {1} A | = 2, _ {2} A = \emptyset , \text { th } \in_ {1} A \\ \text { fail } & \text { otherwise } \end{array} \right. \end{array}\tag{c}
$$

wherein ‘th’ and ‘pra’ refer, respectively, to the theory professor and the practical professor. In Freixas and Zwicker [14], a weighted representation is given for this game (renormalizing at the middle level):

$$
(w _ {1} (\mathrm{th}), w _ {2} (\mathrm{th}), w _ {3} (\mathrm{th})) = (1, 0, - 3)
$$

$$
\left(w _ {1} (\text { pro }), w _ {2} (\text { pro }), w _ {3} (\text { pro })\right) = (1, 0, - 2)
$$

$$
(w _ {1} (\text { pra }), w _ {2} (\text { pra }), w _ {3} (\text { pra })) = (2, 0, - 1)
$$

and quotas:

$$
q _ {1} = 3, q _ {2} = 2, q _ {3} = 1.
$$

Understanding that a student obtains the $\nu _ { k }$ mark if the total weight assigned by the three evaluators is at least $q _ { k } .$ For instance, suppose further that Susan’s grade are as follows: a good mark by the theory professor (th) and by the professor evaluating the work’s practical application (pra) but a fail mark by the professor evaluating calculus, exercises and further developments (pro). Susan’s final weight is then: $1 + 2 - 2 = 1 = q _ { 3 }$ , so her final examination grade is ‘pass.’ Below we will calculate the index proposed in this paper under the three following assumptions:

(a) the uniform numeric evaluation, i.e. considering $( d _ { 1 } , \ d _ { 2 } , \ d _ { 3 } ) { = } ( 1 , \ 1 , \ 1 )$ R

$$
(d _ {1}, d _ {2}, d _ {3}) = (3, 1, 1)
$$

$$
(d _ {1}, d _ {2}, d _ {3}) = (1, 1, 3).
$$

In the second case, the differences vector is assigned great importance to students that reach the highest mark, so the index proposed should be able to improve (with respect to assumption (a)) the index of those evaluators that have more influence in order a student obtains the ‘excellent’ mark. In the third case, we have the opposite situation, the differences vector is assigned great importance to students that obtain the ‘pass mark, so the index proposed should be able to improve (with respect to assumption (a)) the index of those evaluators that have more influence in the ‘pass’ mark. As we shall see, the index proposed will provide a numeric measure sensitive to each of these different scenarios.

## 3. The Shapley –Shubik index for ( j, k) simple games

In this section, we outline a probabilistic proposal for the Shapley–Shubik notion for voting systems with several levels of approval. The nomenclature is the same as that used by Felsenthal and Machover [11] in their book. We understand our approach as a small complementary step to their incipient work.

Definition 3.1. Let N be a finite set. By a queue of N we mean a bijection from N to the set $I _ { n } { = } \{ 1 , 2 , . . . , n \}$ where (as usual) $n = \left| N \right|$

The queue space $\mathcal { Q } _ { N }$ is the probability space consisting of the set of all queues of N, with each queue assigned probability 1/n!.

When there is no risk of confusion, we omit the subscript $^ \circ N ^ { \prime }$ and write simply $\because \mathbb { A }$ particular queue of Q will be denoted by $Q .$

Definition 3.2. Let $N$ be a finite set, with $| N | = n$ The j-space $\mathcal { I } _ { N }$ is the probability space consisting of the set $^ j N$ of all j-partitions of $N ,$ with each j-partition assigned the same probability: $1 / j ^ { n }$

When there is no risk of confusion, we omit the subscript $^ \circ N ^ { \prime }$ in $\mathcal { I } _ { N }$ and write simply ${ ^ { \circ } \mathcal { I } } . { ^ { \circ } } \mathrm { A }$ particular j-partition of J will be denoted by J.

$\mathcal { I } _ { N }$ has the following interpretation: divisions of the board are generated by n equiprobable trials. In other words, each member of the board votes ‘the highest possibility,’ ‘the second highest possibility, $\cdot \cdot , \cdot ,$ ‘the lowest possibility’ with equal probability of $1 / j ;$ and members act independently of each other.

Definition 3.3. Let N be a finite set. By a roll call of N we mean and ordered pair $R = \langle Q , J \rangle$ , where $\boldsymbol { Q }$ is a queue of N and J is a j-partition of N. In this connection, we denote Q and $J ,$ respectively by $\cdot _ { \mathrm { q R } } ,$ and ${ \mathrm {  ~ \ j R ~ } } )$ and we refer to them, respectively, as the queue and j-partition of R. The j-roll call space $\mathcal { Q } _ { N } \times \mathcal { T } _ { N }$ is the probability space consisting of the set of all roll calls of N, with each roll call assigned the same probability: $1 / ( n ! j ^ { n } )$ , where (as usual) $n = \left| N \right|$

Remark 3.4. It is helpful to visualize a roll call R of N as the membership of N queuing up in a random order (this is the first component, $q R ) ;$ and at the same time each member $p { \in } N$ votes at random ‘the highest possibility,’ ‘the second highest possibility,’. . ., ‘the lowest possibility’ with equal probability of $1 / j$

Definition 3.5. If V is a ( j, k) simple game with assembly N and $R = \langle q R , j R \rangle$ is a j-roll call of N then the V -i-pivot of R for $i = 1 , . . . , k { - } 1$ ; denoted by ‘i-$\mathrm { p i v } ( R , { \cal N } )$ is uniquely defined either:

(i) the voter whose vote in R clinches the outcome of jR under, at least the output level $\nu _ { i } ,$ or

(ii) the voter whose vote in R clinches the outcome of $j R$ under, at most the output level $\nu _ { i + 1 }$

In other words, the i-piv(R; V) is earliest voter in $q R$ which satisfies one of the two following excluding conditions:

(i) independently as all subsequent voters act the outcome will be $\nu _ { h }$ with $\nu _ { h } \ge \nu _ { i } ,$ , or

(ii) no matter how all subsequent voters were to change their votes, the final outcome would be no greater than $\nu _ { i + 1 }$

To illustrate these definitions consider the following example.

Example 3.6. Let V be a (3, 5) weighted game with five voters, such that there is a main player, namely 1, whose weights are:

$$
(w _ {\text { yes }} (1), w _ {\text { abstain }} (1), w _ {\text { no }} (1)) = (3, 0, - 1)
$$

for the remaining players, $p ^ { \neq }$ 1:

$$
(w _ {\mathrm{yes}} (p), w _ {\mathrm{abstain}} (p), w _ {\mathrm{no}} (p)) = (1, 0, - 1)
$$

and, quotas

$$
(q _ {1}, q _ {2}, q _ {3}, q _ {4}) = (7, 5, 4, 2)
$$

Consider the roll call R with queue $q R { = } \{ 2 , 4 , 1 , 3 ,$ $5 \}$ and $j R$ the tripartition of N: ({1, 4}, {2, 3}, {5}), that is, players 1 and 4 vote ‘yes,’ players 2 and 3 ‘abstain’ and, player 5 votes ‘no.’ For such roll call R:

(a) Player 2 is 1-pivot because

$$
v _ {2} = V (\{1, 3, 4, 5 \}, \{2 \}, \emptyset) <   v _ {1}
$$

or equivalently, the total weight of j-partition $( \{ 1 , ~ 3 , ~ 4 , ~ 5 \} , ~ \{ 2 \} , ~ \emptyset )$ is $w _ { \mathrm { y e s } } ( 1 ) + w _ { \mathrm { y e s } } ( 3 ) +$ $w _ { \mathrm { y e s } } ( 4 ) + w _ { \mathrm { y e s } } ( 5 ) + w _ { \mathrm { a b s t a i n } } ( 2 ) = 6 < 7 .$

(b) Player 1 is 4-pivot because

$$
v _ {4} = V (\{1, 4 \}, \{2 \}, \{3, 5 \}) > v _ {5}.
$$

(c) Player 5 is 3-pivot because

$$
v _ {4} = V (\{1, 4 \}, \{2, 3 \}, \{5 \}) <   v _ {3}
$$

and also 2-pivot because

$$
v _ {4} = V (\{1, 4 \}, \{2, 3 \}, \{5 \}) <   v _ {2}.
$$

j-partitions weight assuming the two extreme cases for available possibilities to vote for all the subsequent voters

<table><tr><td></td><td>Condition (i)</td><td>Condition (ii)</td></tr><tr><td>Player 2</td><td> $w(\emptyset, \{2\}, \{1, 3, 4, 5\}) = -4$ </td><td> $w(\{1, 3, 4, 5\}, \{2\}, \emptyset) = 6$ </td></tr><tr><td>Player 4</td><td> $w(\{4\}, \{2\}, \{1, 3, 5\}) = -2$ </td><td> $w(\{1, 3, 4, 5\}, \{2\}, \emptyset) = 6$ </td></tr><tr><td>Player 1</td><td> $w(\{1, 4\}, \{2\}, \{3, 5\}) = 2$ </td><td> $w(\{1, 4, 5\}, \{2, 3\}, \emptyset) = 5$ </td></tr><tr><td>Player 3</td><td> $w(\{1, 4\}, \{2, 3\}, \{5\}) = 3$ </td><td> $w(\{1, 4, 5\}, \{2, 3\}, \emptyset) = 5$ </td></tr><tr><td>Player 5</td><td> $w(\{1, 4\}, \{2, 3\}, \{5\}) = 3$ </td><td> $w(\{1, 4\}, \{2, 3\}, \{5\}) = 3$ </td></tr></table>

Easily from the previous Table 1 we derive Table 2. From Table 2, it follows that: player 2 is 1-pivot, player 5 is 2-pivot and also 3-pivot, and finally player 1 is 4-pivot. Neither player 4 nor player 3 are i-pivot for $i = 1 , 2 , 3 , 4 .$

Of course from Definition 3.5 if V is a $( j , k )$ simple game, for any roll call R and for any step level $i = 1 , \ldots . , k { - } 1$ , there is a unique player in N such that is i-pivot. We can now introduce the S –S power index for a ( j, k) simple game.

Definition 3.7. The Shapley–Shubik power index for a $( j , k )$ simple game with numeric evaluation a for player p is:

$$
\begin{array}{c} \Phi_ {p} [ ^ {\alpha} V ] = \frac {1}{n ! j ^ {n} (\alpha_ {1})} \sum_ {i = 1} ^ {k - 1} (\alpha_ {i} - \alpha_ {i + 1}) | \{R \in Q _ {N} \\ \times J _ {N}: i - \operatorname{piv} (R; V) = p \} |. \end{array}
$$

For instance, if we consider ( j, k) simple games with the uniform numeric evaluation $\mu$ the latter Definition 3.7 reduces to:

$$
\begin{array}{c} \Phi_ {p} [ ^ {\mu} V ] = \frac {1}{n ! j ^ {n} (k - 1)} \sum_ {i = 1} ^ {k - 1} | \{R \in Q _ {N} \\ \times J _ {N}: i - \operatorname{piv} (R; V) = p \} |. \end{array}
$$

In particular for ( j, 2) simple games we may identify ‘1-pivot’ with ‘pivot’ and Definition 3.7 reduces to:

$$
\Phi_ {p} [ V ] = \frac {1}{n ! j ^ {n}} \mid \left\{R \in Q _ {N} \times J _ {N}: \operatorname{piv} (R; V) = p \right\} |.
$$

When considering (3, 2) simple games with abstention the Definition 3.7 coincides with that proposed by Felshental and Machover [11] in p. 292:

$$
\Phi_ {p} [ V ] = \frac {1}{n ! 3 ^ {n}} \mid \left\{R \in Q _ {N} \times J _ {N}: \operatorname{piv} (R; V) = p \right\} |.
$$

Finally, for standard simple games ((2, 2) simple games in our context) Definition 3.7 reduces to:

$$
\Phi_ {p} [ V ] = \frac {1}{n ! 2 ^ {n}} \mid \left\{R \in Q _ {N} \times J _ {N}: \operatorname{piv} (R; V) = p \right\} |.
$$

## Remark 3.8. For ( j, 2) simple games

$$
\Phi_ {p} [ V ] = P (p \text {   is   the   } V - \text { pivot }),
$$

where P is the (discrete and uniform) probability distribution in the roll call space $\mathcal { Q } _ { N } \times \mathcal { T } _ { N } .$ This was already suggested by Felsenthal and Machover for ternary voting games with abstention. When we extend such probabilistic interpretation to $( j , \ k )$ simple games we need to introduce $\phi _ { p } ^ { i } [ V ]$ as the probability that player p becomes i-critical, i.e.,

$$
\Phi_ {p ^ {i}} [ V ] = P (p \text {   is   the   } V - i \text {-pivot }).
$$

Under this probabilistic scheme Definition 3.7 is equivalent to

$$
\Phi_ {p} [ ^ {\alpha} V ] = \sum_ {i = 1} ^ {k - 1} \frac {\alpha_ {i} - \alpha_ {i + 1}}{\alpha_ {1}} \Phi_ {p ^ {i}} [ V ].
$$

j-partitions value function assuming the two extreme cases for available possibilities to vote for all the subsequent voters

<table><tr><td></td><td>Condition (i)</td><td>Condition (ii)</td></tr><tr><td>Player 2</td><td> $V(\emptyset, \{2\}, \{1, 3, 4, 5\}) = v_5$ </td><td> $V(\{1, 3, 4, 5\}, \{2\}, \emptyset) = v_2$ </td></tr><tr><td>Player 4</td><td> $V(\{4\}, \{2\}, \{1, 3, 5\}) = v_5$ </td><td> $V(\{1, 3, 4, 5\}, \{2\}, \emptyset) = v_2$ </td></tr><tr><td>Player 1</td><td> $V(\{1, 4\}, \{2\}, \{3, 5\}) = v_4$ </td><td> $V(\{1, 4, 5\}, \{2, 3\}, \emptyset) = v_2$ </td></tr><tr><td>Player 3</td><td> $V(\{1, 4\}, \{2, 3\}, \{5\}) = v_4$ </td><td> $V(\{1, 4, 5\}, \{2, 3\}, \emptyset) = v_2$ </td></tr><tr><td>Player 5</td><td> $V(\{1, 4\}, \{2, 3\}, \{5\}) = v_4$ </td><td> $V(\{1, 4\}, \{2, 3\}, \{5\}) = v_4$ </td></tr></table>

Remark 3.9. For each level of approval $l { = } 1 , { \ldots } { \ldots } j$ if we define

$$
c _ {l, i} [ V ] = | \{R \in Q \times J: i \text {-pivot} (R; V) \in_ {l} J \} |
$$

for every step value function $i = 1 , \ldots . , k - 1$ , it holds

$$
\sum_ {l = 1} ^ {j} c _ {l, i} [ V ] = n! j ^ {n}.
$$

In particular, if k = 2 the latter equality reduces to

$$
\sum_ {l = 1} ^ {j} c _ {l} [ V ] = n! j ^ {n}.
$$

## 4. The calculus of the Shapley –Shubik index for ( j, 2) simple games

Taking as a reference the examples introduced in Section 2 we calculate and outline the idea behind to be a pivotal player. As we shall show this idea is a natural extension than that proposed by Shapley and Shubik.

The calculations for the two first examples were already made by Felsenthal and Machover. To be precise, they show that $\varPhi _ { 1 } = 2 2 / 2 7$ and $\varPhi _ { 2 } = \varPhi _ { 3 } = 5 /$ 54 for Example 2.5 and point out that there is no a simple game with three voters can yield such values of U (because they are not multiples of 1/6). For the UNSC (Example 2.6) they find the following values of U: 0.1636 and 0.0182 for a permanent member and for an ordinary member, respectively.

Consider now the Example 2.7 in which player 4 plays a ‘dummy’ role and players 2 and 3 a symmetric role. As we shall see Axioms 1 and 3 of Theorem 5.1 will respectively guarantee that $\varPhi _ { 4 } = 0$ and $\varPhi _ { 2 } = \varPhi _ { 3 }$ Hence, we may only consider roll calls of three players (without considering player 4) and computing only $\varPhi _ { 1 }$ we will do so using the probability interpretation given in Remark 3.8 for the S –S power index. Voter 1 is pivotal in the following events.

(1) Player 1 votes first and does not vote alternative $_ { 1 } A .$ . The probability of this event is 1/4.

(2) Player 1 votes second, the first did not vote alternative $_ { 4 } A$ and 1 does not vote alternative $_ { 1 } A \colon$ This has probability 3/16.

(3) Player 1 votes third, the first voter voted alternative $_ { 1 } A$ or alternative $_ { 2 } A$ and the second voter did not vote alternative $_ { 4 } A .$ . The probability of this is 1/8.

(4) Player 1 votes third, the first voter voted alternative $_ { 3 } A$ and the second voter voted alternative $_ { 1 } A$ or alternative $_ { 2 } A .$ This has probability 1/24.

Thus $\varPhi _ { 1 } = 2 9 / 4 8 ;$ hence $\varPhi _ { 2 } = \varPhi _ { 3 } = 1 9 / 9 6$ and, of course $\varPhi _ { 4 } = 0$ . Notice that:

(i) There is no a simple game with four voters can yield values of $\varPhi$ (because they are not integer multiples of 1/24).

(ii) The results for this game are not equal than those obtained in Example 2.5 because of the different number of input alternatives. As 22/ 27>29/48 the S–S index intuitively seems more egalitarian when the number of input alternatives increase.

## 5. The calculus of the Shapley –Shubik index for ( j, k) simple games

If $k { > } 2 ,$ , it appears k - 1 kinds of pivotal players. Consider now the Example 2.8 wherein the output set has three values and thus two step levels, and consequently, two type of pivotal players. To calculate the S –S power index we can write out the 2! orderings of the voters for each j-partition and in each ordering underline the 1-pivotal voter and overline the 2- pivotal one (Table 3).

Counting pivots gives $\varPhi _ { 1 ^ { 1 } } [ V ] { = } P ( 1$ is the V - 1- pivot) = 12/18 and $\phi _ { 1 ^ { 2 } } [ \ / ] { = } P ( 1$ is the $V - 2 { \cdot } \mathrm { p i v } 0 \mathrm { t } ) = 1 4 /$ 18. Hence

$$
\Phi_ {1} [ V ] = \frac {\alpha_ {1} - \alpha_ {2}}{\alpha_ {1}} \frac {1 2}{1 8} + \frac {\alpha_ {2} - \alpha_ {3}}{\alpha_ {1}} \frac {1 4}{1 8}.
$$

Analogously for the second player, $\varPhi _ { 2 ^ { 1 } } [ V ] { = } P ( 2$ is the $V - 1 { \cdot } \mathrm { p i v } 0  t ) = 6 / 1 8$ and $\Phi _ { 2 ^ { 2 } } [ M ] { = } P ( 2$ is the $V - 2 \cdot$ pivot) = 4/18. Hence

$$
\Phi_ {2} [ V ] = \frac {\alpha_ {1} - \alpha_ {2}}{\alpha_ {1}} \frac {6}{1 8} + \frac {\alpha_ {2} - \alpha_ {3}}{\alpha_ {1}} \frac {4}{1 8}.
$$

Table 3  
All the roll calls for Example 2.8

<table><tr><td>j-partition</td><td>Value function</td><td>Orderings</td></tr><tr><td> $(\{1,2\}, \emptyset, \emptyset)$ </td><td> $v_1$ </td><td> $\overline{1}\overline{2} \ 2\overline{\overline{1}}$ </td></tr><tr><td> $(\{1\}, \{2\}, \emptyset)$ </td><td> $v_1$ </td><td> $\overline{1}\overline{2} \ 2\overline{\overline{1}}$ </td></tr><tr><td> $(\{1\}, \emptyset, \{2\})$ </td><td> $v_2$ </td><td> $\underline{1}\overline{2} \ \overline{2}\underline{1}$ </td></tr><tr><td> $(\{2\}, \{1\}, \emptyset)$ </td><td> $v_2$ </td><td> $\overline{1}\underline{2} \ 2\overline{1}$ </td></tr><tr><td> $(\{2\}, \emptyset, \{1\})$ </td><td> $v_3$ </td><td> $\overline{1}2 \ \underline{2}\overline{1}$ </td></tr><tr><td> $(\emptyset, \{1,2\}, \emptyset)$ </td><td> $v_3$ </td><td> $\overline{1}\overline{2} \ 2\overline{1}$ </td></tr><tr><td> $(\emptyset, \{1\}, \{2\})$ </td><td> $v_3$ </td><td> $\overline{1}\underline{2} \ \overline{2}\underline{1}$ </td></tr><tr><td> $(\emptyset, \{2\}, \{1\})$ </td><td> $v_3$ </td><td> $\overline{1}2 \ 2\overline{1}$ </td></tr><tr><td> $(\emptyset, \emptyset, \{1,2\})$ </td><td> $v_3$ </td><td> $\overline{1}2 \ \overline{2}\underline{1}$ </td></tr></table>

For instance, if we assign more importance (for example the double) to the rate ${ \bf \tilde { v } } _ { 1 } / { \bf { v } } _ { 2 } \}$ than to the rate ${ } ^ { \circ } \mathrm { v } _ { 2 } / \mathrm { v } _ { 3 } { } ^ { \circ } \ ( ( d _ { 1 } , \ d _ { 2 } ) { = } ( 2 , \ 1 )$ or, $( \alpha _ { 1 } , \ \alpha _ { 2 } , \ \alpha _ { 3 } ) { = } ( 3 , \ 1 , \ 0 ) )$ we obtain 19/27 and 8/27 for voters 1 and 2, respectively.

Finally, for Example 2.9 if we proceed to count the V -i-pivots for each step level $i = 1 , 2 , 3$ , and for each player th, pra and pro we obtain:

$$
\begin{array}{l l l} \Phi_ {\mathrm{th} ^ {1}} = \frac {4 2}{1 6 2}, & \Phi_ {\mathrm{th} ^ {2}} = \frac {5 4}{1 6 2}, & \Phi_ {\mathrm{th} ^ {3}} = \frac {9 0}{1 6 2}, \\ \Phi_ {\mathrm{pra} ^ {1}} = \frac {7 8}{1 6 2}, & \Phi_ {\mathrm{pra} ^ {2}} = \frac {6 0}{1 6 2}, & \Phi_ {\mathrm{pra} ^ {3}} = \frac {3 6}{1 6 2}, \\ \Phi_ {\mathrm{pro} ^ {1}} = \frac {4 2}{1 6 2}, & \Phi_ {\mathrm{pro} ^ {2}} = \frac {4 8}{1 6 2}, & \Phi_ {\mathrm{pro} ^ {3}} = \frac {3 6}{1 6 2}. \end{array}
$$

(a) Thus the S –S index under the uniform numeric evaluation is:

$$
\Phi_ {\mathrm{th}} = \frac {3 1}{8 1}, \Phi_ {\mathrm{pra}} = \frac {2 9}{8 1}, \Phi_ {\mathrm{pro}} = \frac {2 1}{8 1}.
$$

(b) Assuming now that we assign high importance to the highest mark $( ( d _ { 1 } , d _ { 2 } , d _ { 3 } ) { = } ( 3 , 1 , 1 )$ or $( x _ { 1 } , x _ { 2 }$ $\alpha _ { 3 } , \ \alpha _ { 4 } ) = ( 5 , \ 2 , \ 1 , \ 0 ) )$ . The S–S power index is now:

$$
\Phi_ {\mathrm{th}} = \frac {2 7}{8 1}, \Phi_ {\mathrm{pra}} = \frac {3 3}{8 1}, \Phi_ {\mathrm{pro}} = \frac {2 1}{8 1}.
$$

Thus, the practical professor has a great influence in order for a student to reach the highest mark. As this is reflected by these indices in comparison with the obtained ones under assumption (a). So the S –S power index is sensitive under changes in the numeric evaluation assigned to the game.

(c) Assuming now that we assign high importance to the lowest level $( ( d _ { 1 } , d _ { 2 } , d _ { 3 } ) { = } ( 1 , 1 , 3 )$ or, $( x _ { 1 } , x _ { 2 } ,$ $\alpha _ { 3 } , \alpha _ { 4 } ) { = } ( 5 , 4 , 3 , 0 )$ . The S–S power index is:

$$
\Phi_ {\mathrm{th}} = \frac {6 1}{1 3 5}, \Phi_ {\mathrm{pra}} = \frac {4 1}{1 3 5}, \Phi_ {\mathrm{pro}} = \frac {3 3}{1 3 5}.
$$

Under this assumption, it is showed that the theory professor is the most decisive in order for a student to reach the pass mark.

## Acknowledgements

Research partially supported by Grant BFM 2000- 0968 of the Science and Technology Spanish Ministry.

## Appendix A. An axiomatization for the Shapley –Shubik index of ( j, 2) simple games

In this appendix, we are concerned in extending to $( j , 2 )$ simple games the axiomatization done by Dubey and Shapley for standard simple games. We axiomatize a $ { ^ \circ }  { \mathrm { r a w } } ^ { \prime }  { \mathrm { S } }  { - }  { \mathrm { S } }$ index, $\phi ,$ which after normalized by $n ! j ^ { n }$ gives rise to U.

For any game $V { \in } C ^ { j , 2 } ( N )$ , if p is a permutation of N we define pV by

$$
\begin{array}{c} (\pi V) (A) = (\pi V) (_ {1} A, \ldots , _ {j} A) \\ = V (\pi^ {- 1} (_ {1} A), \ldots , \pi^ {- 1} (_ {j} A)). \end{array}
$$

For ( j, 2) simple games with an arbitrary numeric evaluation V, $W { \in } \mathrm { C } ^ { j , 2 } ( N )$ , we define the operations V \_W and V^W by

$$
\begin{array}{l} (V \lor W) (A) = \max \{V (A), W (A) \}, \\ (V \land W) (A) = \min \{V (A), W (A) \}. \end{array}
$$

It is clear that $\mathrm { C } ^ { j , 2 } ( { \cal N } )$ is closed under the operations $\pi , \vee ,$ and ^. For each player $p { \in } N ,$ , we need to consider j copies of it, the index set $N _ { l }$ for every $1 \leq l \leq j ,$ contains the l copies for elements in $N ,$ so the index $p _ { l }$ will mean the l-copy of $\mathrm { ~ } p \in N .$ The idea that follows under considering these copies is due to the goal of introducing a power index notion, $\phi _ { p _ { l } } [ V ]$ will mean a power index for player $p$ when he/she takes action $\cdot \boldsymbol { l } ^ { \flat }$

$1 \leq l \leq j$ in game V. Since we do assume that all actions in the input level are equally powerful we are interested in the sum $\begin{array} { r } { \Phi _ { p } [ V ] = \sum _ { l = 1 } ^ { j } \mathbf { \bar { \Phi } } \Phi _ { p _ { l } } [ V ] } \end{array}$

A player $p$ is called dummy if $p { \in } _ { j } J$ for every minimal winning j-partition $J ,$ intuitively a dummy player can never help an arbitrary losing j-partition to win or can never damage an arbitrary winning $j -$ partition to lose. Finally, recall that for each level of approval $l = 1 , . . . , j ,$ it was previously defined as

$$
c _ {l} [ V ] = | \{R \in Q \times J: \operatorname{pivot} (R; V) \in_ {l} J \} |
$$

and it holds $\textstyle \sum _ { l = 1 } ^ { j } c _ { l } [ V ] = n ! j ^ { n }$

Theorem 5.1. Let (N, V) be a ( j, 2) simple game then, there is a unique function

$$
\phi : \cup_ {l = 1} ^ {j} N _ {l} \to \mathbb {R} ^ {n j}
$$

whose restriction on N, /: $N \longrightarrow \mathbb { R } ^ { n }$ defined as

$$
\phi_ {p} = \sum_ {l = 1} ^ {j} \phi_ {p _ {l}}
$$

satisfies the following four axioms:

(S1) If p is a dummy in V, then $\phi _ { p _ { l } } / V ] = 0$ for each $I \leq l \leq j .$

(S2) $\Sigma _ { p \in N } \phi _ { p _ { l } } I V J = c _ { l } [ V ]$ for each $I \leq l \leq j .$

(S3) For any permutation p of N, $\phi _ { \pi ( p ) _ { l } } [ \pi V ] = \phi _ { p _ { l } } \ : [ V ]$ for each $I \leq l \leq j .$

(S4) For any $V { \in } C ^ { j , 2 } ( N )$ and $W { \in } C ^ { j , 2 } ( N ) , \ \phi / V { \vee } W ] +$ $\phi [ V \wedge W ] = \phi [ V ] + \phi [ W ] .$

Proof. For any j-partition A such that $A \neq N ,$ define the unanimity game $V _ { A }$ by

$$
V _ {A} (J) = \left\{ \begin{array}{l l} 0 & \text { if } J \not \supseteq^ {j} A \\ 1 & \text { if } J \supseteq^ {j} A \end{array} \right.
$$

Every $p { \in } _ { j } A$ is a dummy in $V _ { A } ,$ , therefore, by $\mathrm { S 1 } _ { : }$ $\phi _ { p _ { \mathnormal { \vert } } } [ V _ { A } ] = 0$ for such $p$ and each $1 \leq l \leq j$ (and thus $\phi _ { p } [ V _ { A } ] = 0 )$ . If p is the permutation that interchanges $p$ and $q ,$ , for any $p { \in } _ { l } A$ and $q { \in } _ { l } A$ for some $1 \leq l \leq j$ , and leaves the other players fixed, then p $\cdot V _ { A } { = } V _ { A }$ and thus, by S3,

$$
\phi_ {p l} [ V _ {A} ] = \phi_ {q l} [ V _ {A} ].
$$

Therefore, $\phi [ V _ { A } ]$ is uniquely determined, if $\phi$ exists, and for each $1 \leq l \leq j$ is given by

$$
\phi_ {p _ {l}} [ V _ {A} ] = \left\{ \begin{array}{l l} 0 & \text { if } p \in_ {j} A \\ \frac {c _ {l} ^ {i} [ V _ {A} ]}{| _ {i} A |} & \text { if } p \in_ {i} A, i \neq j \end{array} \right.
$$

using S2, where

$$
c _ {l} ^ {i} \left[ V _ {A} \right] = | \{R \in Q \times J: \operatorname{pivot} (R; V) \in_ {l} J \cap_ {i} A \} |.
$$

Notice that for unanimity games $c _ { l } [ V _ { A } ]$ coincides with $\textstyle \sum _ { i = 1 } ^ { j - 1 } c _ { l } ^ { i } [ V _ { A } ]$ :. Every game $V { \in } \mathrm { C } ^ { j , 2 } ( N )$ has a finite number of minimal winning j-partitions, $J _ { 1 } , . . . J _ { m }$ , and they completely determine $V ,$ since $V ( B ) = 1$ if and only if $B \supseteq ^ { j } J _ { h }$ for at least one $h = 1 , . . . , m$ . Now if $V { \in } \mathrm { C } ^ { j , 2 } ( N )$ is not of the form $V _ { J } ,$ then $m { > } 1$ , so $V$ can be written as $V { = } V ^ { \prime } \backslash V ^ { \prime \prime } ,$ where $V ^ { \prime }$ Vand $V ^ { \prime \prime }$ are games with fewer winning j-partitions than V. Of course, the game $V ^ { \prime } \wedge V ^ { \prime \prime }$ has even fewer winning j-partitions. So we can perform an induction on the number of winning j-partitions, using S4:

$$
\phi [ V ] = \phi [ V ^ {\prime} \vee V ^ {\prime \prime} ] = \phi [ V ^ {\prime} ] + \phi [ V ^ {\prime \prime} ] - \phi [ V ^ {\prime} \wedge V ^ {\prime \prime} ],
$$

and it follows that $\phi [ V ]$ is uniquely determined. We must still prove existence. The foregoing proof of uniqueness has implicit in it a recursive construction of $\phi$ that establishes existence; however, it is simpler to check directly that the function $\phi$ as already defined

$$
\phi_ {p _ {l}} [ V ] = | \{R \in Q _ {N} \times J _ {N}: \operatorname{piv} (R; V) = p, p \in_ {l} J \} |
$$

satisfies S1–S4. In fact, S1–S3 are obvious, while S4 follows from showing that /[V] can be extended to a linear function $\mathrm { C } ^ { j , 2 } ( { \bar { N } } )$ . Since

$$
[ V \vee W ] + [ V \wedge W ] \equiv V + W,
$$

S4 is now obvious.

## References

[1] R. Amer, F. Carreras, A. Magan˜ a, Extension of values to games with multiple alternatives, Annals of Operation Research 84 (1998) 63–78.

[2] J.F. Banzhaf, Weighted voting doesn’t work: a mathematical analysis, Rutgers Law Review 19 (1965) 317– 343.

[3] E.M. Bolger, Power indices for multicandidate voting games, International Journal of Game Theory 14 (1986) 175– 186.

[4] E.M. Bolger, A value for games with n players and r alternatives, International Journal of Game Theory 22 (1993) 319–334.

[5] E.M. Bolger, A consistent value for games with n players and r alternatives, International Journal of Game Theory 29 (1993) 93 – 99.

[6] M. Braham, F. Steffen, Voting power in games with abstentions, in: M.J. Holler, et al. (Eds.), Power and Fairness, Jahrbuch fu¨r Neue Politische Ekonomie, vol. 20, Mohr-Siebeck, Tu¨bingen, 2003, pp. 333– 348.

[7] J.S. Coleman, Control of collectivities and the power of a collectivity to act, in: B. Lieberman (Ed.), Social Choice, Gordon and Breach, New York, 1971, pp. 269– 300.

[8] P. Dubey, On the uniqueness of the Shapley value, International Journal of Game Theory 4 (1975) 131 – 139.

[9] P. Dubey, Ll.S. Shapley, Mathematical properties of the Banzhaf index, Mathematics of Operations Research 4 (1979) 99– 131.

[10] D.S. Felsenthal, M. Machover, Ternary voting games, International Journal of Game Theory 26 (1997) 335 – 351.

[11] D.S. Felsenthal, M. Machover, The Measurement of Voting Power: Theory and Practice, Problems and Paradoxes, Edward Elgar Publishing, Cheltenham, 1998.

[12] D.S. Felsenthal, M. Machover, Models and reality: the curious case of the absent abstention, in: J.M. Holler, G. Owen (Eds.), Power Indices and Coalition Formation, Kluwer Academic Publishers, Dordrecht, 2001, pp. 297– 310.

[13] P.C. Fishburn, The Theory of Social Choice, Princeton University Press, Princeton, NJ, 1973.

[14] J. Freixas, W.S. Zwicker, Weighted voting, abstention, and

multiple levels of approval, Social Choice and Welfare 21 (2003) 399–431.

[15] C.R. Hsiao, T.E.S. Raghavan, Shapley value for multichoice cooperative games I, Games and Economic Behavior 5 (1993) 240– 256.

[16] A. Magan˜a, Formaci<sup>´</sup>on de coaliciones en los juegos cooperativos y juegos con m´ ultiples alternativas, PhD Thesis, Mathematics Department of UPC, Spain (1996).

[17] Ll.S. Shapley, A value for n-person games, in: A.W. Tucker, H.W. Kuhn (Eds.), Contributions to the Theory of Games, vol. II, Princeton University Press, Princeton, NJ, 1953, pp. 307– 317.

[18] Ll.S. Shapley, M. Shubik, A method for evaluating the distribution of power in a committee system, American Political Science Review 48 (1954) 787– 792.

[19] J. Von Neumann, O. Morgenstern, Theory of Games and Economic Behavior, Princeton University Press, Princeton, NJ, 1944.

![](/api/attachments/45JYK22K/fulltext/images/da6c76063f77fd788d46e3f4bf107fcdde63e28084a8d2246b531b0c2547e4a2.jpg)  
Josep Freixas works in the Mathematics Department III of the Polytechnic University of Catalonia. The main topics of his research are: Game and Decision Theory, Boolean Algebra and Reliability. He has published 14 papers, some of them coauthored by one of the following professors: F. Carreras, M.A. Puente, G. Gambarelli and W.S. Zwicker. He’s 41 years old.

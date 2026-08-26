---
otero_id: 7192
otero_key: "FW66SG34"
title: "A new power index based on minimal winning coalitions without any surplus"
authors: "José María Alonso-Meijide; Josep Freixas"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.01.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A new power index based on minimal winning coalitions without any surplus

José María Alonso-Meijide <sup>a</sup>, Josep Freixas <sup>b,</sup>⁎

<sup>a</sup> Department of Statistics and Operations Research and Science Faculty (Lugo Campus), University of Santiago de Compostela, Spain

<sup>b</sup> Department of Applied Mathematics III and High Engineering School (Manresa Campus), Technical University of Catalonia, Spain

## a r t i c l e i n f o

Article history: Received 29 December 2009 Accepted 16 January 2010 Available online 21 January 2010

Keywords: Decision making process Voting systems in democratic organizations Relative power indices Desirability relation Shift power index

## a b s t r a c t

In this paper we propose a new power index useful for the evaluation of each member in a committee, or democratic institution, and the degree of in<sup>fl</sup>uence over the voting decision making system. The proposed solution is based on the observation that democratic organizations not only tend to form coalitions which can by themselves guarantee the control of the organization, but that they also do it in an extremely ef<sup>fi</sup>cient way that avoids the inclusion of powerful members if they can be replaced by weaker ones, The mathematical foundation of the new measure is based on two different axiomatizations. A comparison with other well-known measures is also done.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

International economic organizations (such as the International Monetary Fund or the World Bank), federal voting bodies (such as the European Union Council of Ministers or the Presidential Electoral College of the United States) have governance systems designed to give different amounts of in<sup>fl</sup>uence over decision making to different members of the organization.

All these organizations, and many other democratic institutions, can be seen as DSS and have in common that voters must make decisions involving a choice between alternatives; here we assume them to have binary alternatives, based on individual estimates. The speci<sup>fi</sup>c or de<sup>fi</sup>nable decision context consists of ‘either breaking the status quo or not.’ The target system describes each situation in which coalitions are able to pass a new law or change the status quo. Making decisions in democratic organizations is regarded as a DSS. In this paper we are primarily concerned with determining the amount of in<sup>fl</sup>uence that different players in voting systems of democratic organizations have.

In many cases, the decision rule of these organizations can be modeled with a weighted game or, more generally, with a simple game. A simple game is a pair formed by the set of players and the set of winning coalitions. A winning coalition is formed by a set of players that can enforce the result of a vote.

Different power measures are proposed to quantify the amount of in<sup>fl</sup>uence that different players in a simple game have. A power index is an n-vector whose elements measure the respective ability of each player to determine the outcome of a simple game. Among them, we can cite the Banzhaf index [3], the Shapley–Shubik index [18], the Johnston index [14], the Deegan–Packel index [5], or the Public Good Index [10].

For the last two indices, a particular family of winning coalitions plays a decisive role: the set of minimal winning coalitions. The minimality condition says that if players want to maximize power, then surplus players must not be taken into account.

A strong condition is given for weighted voting games by The Size Principle [16], which implies that a coalition will be formed if and only if its weight is the minimum among the weights of the minimal winning coalition. A coalition that satis<sup>fi</sup>es The Size Principle is a minimal winning coalition but, the converse is not necessarily true. In this paper, we take this analysis one step further and consider an intermediate type of coalitions, namely, shift minimal winning coalitions. Using these coalitions, we de<sup>fi</sup>ne a new power index and, in this sense, the proposed power index can be seen as a combination of previously developed indices. Besides, we provide two axiomatic characterizations of this index using old and new properties.

Stability lies at the core of the power index we are introducing. Indeed, if a ‘shift minimal winning coalition’ is formed to pass a decision, all voters in it do not have propensity to disrupt the coalition; no voter in it can be replaced by a weaker voter because, in this case, it could be no longer maintain the status of winning coalition. Thus, nobody in the coalition can claim a higher payoff. The power index we propose re<sup>fl</sup>ects a very frequent behavior in democratic organizations. That is to say, the winning coalition that is <sup>fi</sup>nally formed is not only able to pass the issue at hand, but it is also shift minimal. There are no surplus voters in it and nobody in the coalition can be replaced by a weaker voter without altering the winning status of the coalition.

The paper is organized as follows. In the rest of this section we introduce some formal de<sup>fi</sup>nitions and recall some related power indices. The Shift power index is introduced in Section 2 and it is compared with the Banzhaf and Public Good indices. Section 3 contains the mathematical foundations that support the proposed power index; two axiomatizations for it are proposed. Finally, some concluding remarks are provided.

In the sequel, $N = \{ 1 , 2 , . . . , n \}$ will denote a <sup>fi</sup>xed, but otherwise arbitrary <sup>fi</sup>nite set of players. Any subset $S \subseteq N$ is a coalition.

De<sup>fi</sup>nition 1.1. A simple game consists of a set of players N and a set of winning coalitions, , which is a collection of subsets of N with the following properties:

1. ∅∉ ,

<sup>W</sup>2. N∈ ,

3. if S∈ and ${ \mathsf { S C T } } ,$ then T∈ (monotonicity).

Thus a simple game is a pair N; formed by a <sup>fi</sup>nite set N and a subset of $2 ^ { N }$ <sup>ð WÞ</sup>with the three requirements in De<sup>fi</sup>nition 1.1. A minimal winning coalition, S, is a winning coalition which does not contain any other winning coalition as a proper subset. The set of minimal winning coalitions is denoted by $\mathcal { W } ^ { m } , \mathsf { A }$ non-winning coalition is a <sup>W</sup>losing coalition. A player is null if it does not belong to any minimal winning coalition. Let D denote the set of null players. A simple game is interpreted as a formalization of a voting situation where N is the set of voters. A winning coalition then has the power to enforce a decision that has been unanimously adopted by its members.

Monotonicity allows for a certain ef<sup>fi</sup>ciency in describing $( N , \mathcal { W } ) \colon$ we need to list only the minimal winning coalitions. The entire collection of winning coalitions can now be obtained by closure with the operation of adding new elements to the minimal winning coalitions. Hence $( N , \mathcal { W } ^ { m } )$ is enough information to describe the game.

Loosely speaking, a power index is a function g which assigns to a simple game N; a vector $g ( N , \mathcal { W } ) { \in } \mathbb { R } ^ { n }$ where each component $g _ { i } ( N , \mathcal { W } )$ <sup>ð WÞ ð WÞ</sup>is a measure for the ith player in the simple game $( N , \mathcal { W } )$ according to g. As N does not change in the rest of the paper, we will write g instead of g N; hereafter.

<sup>ðWÞ ð WÞ</sup>The Banzhaf index [3] examines any winning coalition, no matter what order it might have been formed in, and considers any voter to derive power from being pivotal in it. In order to translate this into a formal de<sup>fi</sup>nition, consider a simple game $( N , \mathcal { W } )$

A swing for a player i N is a coalition $S \subseteq N$ such that $i \in S , S \in \mathcal { W }$ and $S \backslash \{ i \} \not \in { \mathcal { W } } .$ We denote by $\boldsymbol \eta _ { i } ( \mathcal { W } )$ <sup></sup>the number of swings for player $i \in N .$

De<sup>fi</sup>nition 1.2. Let $\boldsymbol \eta _ { i } ( \mathcal { W } )$ express the number of swings of player i. <sup>ðWÞ</sup>Then the Banzhaf Relative Index assigns to each player $i \in N$ the real number:

$$
\beta_ {i} (\mathcal {W}) = \frac {\eta_ {i} (\mathcal {W})}{\sum_ {j = 1} ^ {n} \eta_ {j} (\mathcal {W})} \text {   so   that   } \sum_ {i = 1} ^ {n} \beta_ {i} (\mathcal {W}) = 1.
$$

Instead, Holler [10] considers the numbers $c _ { i } ( \mathcal { W } ) = | \{ S \in \mathcal { W } ^ { m } : i \in S \} |$ for each i∈N and proposes an alternative relative power index.

De<sup>fi</sup>nition 1.3. Let $c _ { i } ( \mathcal { W } )$ express the decisiveness of player i, i.e. the <sup>ðWÞ</sup>number of coalitions S such that $S { \in } w ^ { m }$ and $i \in S$ in the simple game $( N , \mathcal { W } )$ <sup>W</sup>. Then the Public Good Index for $i \in N$ is the real number:

$$
h _ {i} (\mathcal {W}) = \frac {c _ {i} (\mathcal {W})}{\sum_ {j = 1} ^ {n} c _ {j} (\mathcal {W})} \text {   so   that   } \sum_ {i = 1} ^ {n} h _ {i} (\mathcal {W}) = 1.
$$

Holler [11] points out:

‘Although we take only minimal winning coalitions into account for the calculation of the Public Good Index we do not claim that no other coalitions will be formed. It is only assumed that these coalitions do not matter and thus should not be taken into consideration when it comes to measuring power.

The denominator of these two relative power indices depends not only on n, but on the whole or $\boldsymbol { \mathcal { W } } ^ { m }$ . It turns out that this makes <sup>W W</sup>the relative power indices rather dif<sup>fi</sup>cult to handle mathematically.

A different concept was proposed by Riker [16] for the more restrictive set of weighted voting games.

De<sup>fi</sup>nition 1.4. $( N , \mathcal { W } )$ is called a weighted voting game (brie<sup>fl</sup>y, weighted game) if there exist natural integers $w _ { 1 } , . . . , w _ { n }$ such that every coalition $S , S { \in } { \mathcal { W } }$ if and only if the sum of the $w _ { i } ^ { \prime } s , i { \in } S$ , is at least equal to some preset quota q.

The number $w _ { i }$ is interpreted as the number of votes that the player i owns, and q is the least total number of votes necessary to pass a decision. Such representation for N; is indicated by [q; $w _ { 1 } , . . . , w _ { n } ]$ and w(S) stands for $\sum { } _ { i \in S } w _ { i } .$ . For n≥4 there are simple games which are not weighted.

Riker [16] claimed that ‘parties seek to increase votes only up to the size of a minimum coalition.’ This follows from the well-known ‘Size Principle’ (Riker, [17] p. 32) which implies that, given a multimember voting body or weighted game $[ q ; w _ { 1 } , . . . , w _ { n } ]$ a coalition $S _ { 0 }$ will be formed provided that $w ( S _ { 0 } ) = B$ where $B = \operatorname* { m i n } _ { c \sim \operatorname* { m } { ( S ) } }$ . The <sup>S∈</sup>W <sup>ð Þ</sup>underlying idea of this solution is that payoffs for any winning coalition are identical. If the coalition payoff is split between the members of the winning coalition according to their respective voting weights, each member's share will be maximized through the minimizing of the coalition of membe $\mathbf { \partial } \cdot ( s ) ^ { \prime }$ voting weight(s). Hence, for a weighted body [50;40,35,25] the minimal winning coalition $S _ { 0 } =$ {2, 3} with minimum coalitional winning weight $w ( S _ { 0 } ) = 6 0$ will be formed, although {1, 2} and {1, 3} are also minimal winning coalitions.

It is important to note that the coalitions in the set $\{ S \subseteq N : w ( S ) = B \}$ can include null voters, so the appropriate set to search the coalitions that ful<sup>fi</sup>ll Riker's principle is $\{ S \subseteq N : w ( S ) = B , S \cap D = \emptyset \}$ which is a subset of the set of minimal winning coalitions.

In this paper we propose a new power measure for simple games. It contains elements of both the Public Good Index and Riker's principle; thus, to a certain extent, it can be seen as an intermingled solution. The fundamental idea is the notion of desirability which we recall and develop in the next section.

## 2. The Shift power index

De<sup>fi</sup>nition 2.1. Let N; be a simple game, i and j be two voters. <sup>ð WÞ</sup>Players i and j are said to be equally desirable, denoted by i j if: for any coalition S such that i∉S and $j \not \in S , S \cup \{ i \} \in \mathcal { W } \Longleftrightarrow S \cup \{ j \} \in \mathcal { W } .$

De<sup>fi</sup>nition 2.2. (Isbell, [13]) Let N; be a simple game, i and j <sup>ð WÞ</sup>be two voters. Player i is said to be (strictly) more desirable than j, denoted by $i { \succ } j$ if the following two conditions are ful<sup>fi</sup>lled:

1. For every coalition S such that i∉S and $j \not \in S , S \cup \{ j \} \in \mathcal { W } \Rightarrow S \cup \{ i \} \in \mathcal { W } .$

2. There exists a coalition T such that i T and $\scriptstyle j \neq T , T \cup \{ i \} \in { \mathcal { W } }$ <sup>W</sup>and $T \cup \{ j \} \not \in \mathcal { W } .$

The desirability relation denoted by ≿ is de<sup>fi</sup>ned in N as follows: i≿j $\mathrm { i f } i { \succ } j \ o \Gamma i { \sim } j$ and we say that i is at least as desirable as j (as a coalitional partner). It is not dif<sup>fi</sup>cult to see that the desirability relation (≿) is a preordering.

De<sup>fi</sup>nition 2.3. A simple game $( N , \mathcal { W } )$ is complete or linear if the <sup>ð WÞ</sup>desirability relation is a complete preordering.

In particular, every weighted game is also a complete game, since $w _ { i } \ge w _ { j }$ implies i ≿ j.

The proposed index is to a certain extent similar to the Public Good and the Deegan and Packel indices. Our index has two features in common with these two indices: it does not take into account overwhelming winning coalitions, and it fails to be monotonic, i.e., more weight can lead to less power (see [12] and [6] on references of monotonicity failures for the Public Good and the Deegan–Packel indices respectively).

If S is an arbitrary losing coalition in a simple game N; , and i and j are two external voters with $i { \succ } j ,$ then S joining to i offers more chances to convert S into a winning coalition than S joining to j. Precisely, if S is a losing coalition and S∪ {j} wins, then $S \cup \{ i \}$ also wins. Thus, if we regard all losing coalitions as a whole, we can assert that i is globally better positioned than j to be chosen as a coalitional partner.

Nevertheless, consider now only those losing coalitions S in N; containing neither i nor j and that convert $S \cup \{ j \}$ into a winning coalition. Voters in all of these coalitions S prefer joining to j than to i because the joining of j is enough for them to win, but j is less powerful than i. Indeed, some crucial players for $S \cup \{ j \}$ can lose that status in S∪{i}. This approach lays down the foundations of the power index we propose which is close to Riker's idea, but not the same. Roughly speaking the proposed power index in this paper is based on the following principle:

• every voter wishes to form part of a minimal winning coalition, and • to share membership with others who cannot be one-to-one substituted by weaker players (according to the desirability relation) and still leaving winning the coalition.

The previous discussion considers only losing coalitions. If we regard winning coalitions, an analysis on stability or satisfaction of players can also be done. Assume <sup>fi</sup>rst that S is a winning coalition but non-minimal. Then some voters in S might feel unhappy because they think that they could get a better payoff by excluding some members; thus, in this sense, a winning but not minimal coalition is not stable. Hence, the candidates for stable coalitions are the minimal winning coalitions. This approach comes closer to the Public Good Index, but we see our analysis to complete the end. In fact, if S is a minimal winning coalition $i \in S , j \notin S ,$ but i≻j and $( S | \{ i \} ) \cup \{ i \}$ still wins, then all members in S\{i} would prefer j to i as a coalitional partner. Thus, they collectively will encourage j (maybe by offering her a good payoff) to join S \ {i}.

All these considerations lead us to take a look at the notion of the shift minimal winning coalition which is at the core of our proposed power index. See [19] for references and history on the mathematical use of the shift ordering.

In practice, this notion means an index that, for each player, will take into account the number of shift minimal winning coalitions which that player belongs to, independently of the size of such coalitions.

De<sup>fi</sup>nition 2.4. Let N; be a simple game and ≿ be its desirability <sup>ð</sup>ordering. A coalition $S { \in } w ^ { m }$ is shift minimal if for every i∈S and j ∉S such that i ≻ j it holds $( S \backslash \{ i \} ) \cup \{ j \} \notin \mathcal { W } .$

From now on, the set of shift minimal winning coalitions will be denoted by <sup>s</sup>.

In [4] a classi<sup>fi</sup>cation theorem for complete simple games is established; it allows the enumeration of all these games up to isomorphism by listing the possible values of certain invariants. The classi<sup>fi</sup>cation was done in an ef<sup>fi</sup>cient way by considering δ-minimal winning models which are collections of shift minimal coalitions. That is, the information needed to describe a complete simple game is minimized.

If N; is a complete game, we may think of the linearly ordered <sup>ð WÞ</sup>set of ≿-equally desirable classes as being lined up from the most in<sup>fl</sup>uential on the left to the least in<sup>fl</sup>uential on the right. Thus if i≻j coalition $( S \backslash \{ j \} ) \cup \{ i \}$ is obtained by ‘shifting a one to the left. Precisely, a shift minimal winning coalition is a coalition S that is minimal, among minimal winning coalitions, in the ≿-ordering.

If N; is not necessarily a complete simple game one may also consider the desirability relation and keep the shift minimal winning coalitions of N; . The remaining minimal winning coalitions are obtained from the shift minimal coalitions by replacing weaker (i.e. strictly less desirable) voters for stronger ones.

Example 2.5. A simple game $( N , { \mathcal { W } } )$ is homogeneous if it admits a weighted representation $[ q ; w _ { 1 } , . . . , w _ { n } ]$ such that $\sum _ { i \mathop { = } \vec { \mathbf { c } } } w _ { i } = q$ for all $S { \in } w ^ { m }$ . In a homogeneous game all voters in any minimal winning coalition are crucial; thus, $\mathcal { W } ^ { m } = \mathcal { W } ^ { s }$ . An example of a homogeneous real-world voting system is the United Nations Security Council modeled as a simple game, i.e. without taking into consideration the possibility of abstention. See e.g. [9] for a treatment of this example taking into account abstention, and [8] and [7] for the computation of the Shapley–Shubik and Banzhaf measures respectively.

Example 2.6. Consider the weighted game [5;4,3,1,1,1], whose minimal winning coalitions are

$$
\mathcal {W} ^ {m} = \{\{1, 2 \}, \{1, 3 \}, \{1, 4 \}, \{1, 5 \}, \{2, 3, 4 \}, \{2, 3, 5 \}, \{2, 4, 5 \} \}.
$$

The game is complete because is weighted. The complete desirability relation is $1 { > } 2 { > } 3 { \sim } 4 { \sim } 5 .$ Coalition {1, 2} is a minimal winning one, but is not shift minimal since $2 \mathord { > } j \mathrm { \ f o r \ } j = 3 , 4 , 5$ and coalitions of the form {1, j} still win. It is not dif<sup>fi</sup>cult to check that the remaining minimal winning coalitions are also shift minimal. Thus,

$$
\mathcal {W} ^ {s} = \{\{1, 3 \}, \{1, 4 \}, \{1, 5 \}, \{2, 3, 4 \}, \{2, 3, 5 \}, \{2, 4, 5 \} \}.
$$

Example 2.7. Consider the simple game of <sup>fi</sup>ve voters de<sup>fi</sup>ned by its set of minimal winning coalitions

$$
\mathcal {W} ^ {m} = \{\{1, 2, 3 \}, \{1, 2, 4 \}, \{1, 2, 5 \}, \{1, 3, 4 \}, \{3, 4, 5 \} \}.
$$

The pairwise comparisons by the desirability preordering determine the following relations

$$
1 \succ 5, 1 \succ 2, 3 \sim 4, 3 \succ 5, 4 \succ 5
$$

so the game is not complete. One may easily check that coalitions {1, 2, 5} and {3, 4, 5} are shift minimal winning coalitions, however {1, 2, 3}, {1, 2, 4}, {1, 3, 4} are not. Thus,

$$
\mathcal {W} ^ {s} = \{\{1, 2, 5 \}, \{3, 4, 5 \} \}.
$$

The lists of shift minimal winning coalitions in the two previous examples reveal that if voters act sel<sup>fi</sup>shly looking for the formation of a coalition with partners who are as weak as possible, then under the desirability relation the weaker voters tend to be the most crucial voters at the expense of the stronger ones. The following relative power measure intends to capture this idea.

De<sup>fi</sup>nition 2.8. Let $s _ { i } ( \mathcal { W } )$ express the number of coalitions S such that $S { \in } { \mathcal { W } } ^ { s }$ and $i \in S$ <sup>ðWÞ</sup>in the simple game N; . Then the Shift power index <sup>W</sup>for i is the real number:

$$
f _ {i} (\mathcal {W}) = \frac {s _ {i} (\mathcal {W})}{\sum_ {j = 1} ^ {n} s _ {j} (\mathcal {W})} \text {   so   that   } \sum_ {i = 1} ^ {n} f _ {i} (\mathcal {W}) = 1.
$$

We point out that although we take only shift minimal winning coalitions into account for the calculation of the Shift power index, we do not claim that no other coalitions will be formed. It is only assumed that these coalitions are not preferred for at least one of their voters, and thus they should not be taken into consideration when it comes to measuring power.

For homogeneous games, Example 2.5, the Public Good Index and the Shift power index coincide. The Shift power index for Example 2.6 is:

$$
(f _ {1}, f _ {2}, f _ {3}, f _ {4}, f _ {5}) = \left(\frac {3}{1 5}, \frac {3}{1 5}, \frac {3}{1 5}, \frac {3}{1 5}, \frac {3}{1 5}\right).
$$

One might be surprised to observe that all voters receive the same payoff. This apparent paradoxical situation, which is a bit more drastic than the Public Good Index can be explained by observing that if coalition {1, 2} is formed, then voter 2 has no incentive to convince another voter to be shifted by voter 1. Since the new coalition would lose, voter 2 feels happy in coalition {1, 2}. But voter 1, in coalition {1, 2}, prefers any other voter as a partner because a coalition of the form {1, j} where j=3, 4, 5 wins, and voters 3, 4 and 5 are strategically weaker than 2 according to the desirability relation. Hence, coalition {1, 2} is not ‘stable’ for at least one voter and thus it should not be taken into account to calculate power.

This latter observation constitutes the main difference between our power index and the Public Good Index which assigns

$$
(h _ {1}, h _ {2}, h _ {3}, h _ {4}, h _ {5}) = \left(\frac {4}{1 7}, \frac {4}{1 7}, \frac {3}{1 7}, \frac {3}{1 7}, \frac {3}{1 7}\right).
$$

The Shift power index for Example 2.7 is:

$$
(f _ {1}, f _ {2}, f _ {3}, f _ {4}, f _ {5}) = \left(\frac {1}{6}, \frac {1}{6}, \frac {1}{6}, \frac {1}{6}, \frac {2}{6}\right).
$$

Although voter 5 is strictly less desirable than voters 1, 3 and 4, she has more power because everyone wishes to have her as a partner in the coalition to be formed. Instead, the Public Good Index assigns:

$$
(h _ {1}, h _ {2}, h _ {3}, h _ {4}, h _ {5}) = \left(\frac {4}{1 5}, \frac {3}{1 5}, \frac {3}{1 5}, \frac {3}{1 5}, \frac {2}{1 5}\right).
$$

Remark 2.9. From the previous de<sup>fi</sup>nitions it is clear that for all simple games N; yields

$$
\mathcal {W} ^ {s} \subseteq \mathcal {W} ^ {m} \subseteq \mathcal {W} ^ {S}\tag{1}
$$

where $\mathcal { W } ^ { S } = \{ T \in \mathcal { W } : T \backslash \{ j \} \quad$ ∉ foratleastaplayerj∈T . Moreover if <sup>W f</sup>A is a subset of $2 ^ { N } , i \in N$ <sup>f g</sup>and $A _ { i }$ stands for the set $\{ T { \in } A : T \backslash \{ i \} { \notin } A \}$ then from Eq. (1) it directly follows

$$
\mathcal {W} _ {i} ^ {s} \subseteq \mathcal {W} _ {i} ^ {m} \subseteq \mathcal {W} _ {i} ^ {s}.\tag{2}
$$

In order to compute some power indices we need to identify for all $i \in N$ the sets:

1. <sup>s</sup> for the Shift power index,

2. $\mathcal { W } _ { i } ^ { m }$ for the Public Good or the Deegan–Packel power indices,

3. ${ \mathcal W } _ { i } ^ { \dot { S } }$ for the Banzhaf, Johnston or Shapley–Shubik power indices.

Hence, from the inclusions in Eq. (2) it can be deduced that the Shift power index is, among these six power indices, the one that involves the minimum amount of information.

## 3. Two axiomatizations for the Shift power index

Before stating the axioms it is convenient to de<sup>fi</sup>ne a game as a function rather than as a set of coalitions.

A cooperative game v (in N, omitted hereafter) is a simple game if $( \mathsf { a } ) \ v ( S ) = 0$ or 1 for all S, (b) is monotonic, i.e. $\nu ( S ) { \leq } \nu ( T )$ whenever $S \subset T ,$ and $( \mathsf { c } ) \nu ( N ) = 1$ . Either the family of winning coalitions $\mathcal { W } = \mathcal { W } ( \boldsymbol { \nu } ) = \{ S \subseteq N : \nu ( S ) = 1 \}$ or the subfamily of minimal winning coalitions $\mathcal { W } ^ { m } = \mathcal { W } ^ { m } ( \nu ) = \{ S \in \mathcal { W } : T \subset S \Rightarrow T \notin \mathcal { W } \}$ with the inclusion <sup>W W ð Þ f W Wg</sup>determines the game. The subfamily of shift minimal winning coalitions $\mathscr { W } ^ { s } = \mathscr { W } ^ { s } ( \boldsymbol { \nu } ) = \{ S \in \mathscr { W } ^ { m } : ( S \backslash \{ i \} ) \cup \{ j \} \notin \mathscr { W } \mathrm { ~ i f ~ } i \succ j , i \in S , j \notin S \}$ de-<sup>W W ð Þ f W ð f gÞ f g W g</sup>termines the game if the preordering induced by the desirability relation on N is known.

To state the <sup>fi</sup>rst three axioms we need the following standard de<sup>fi</sup>nition. $\operatorname { I f } \pi : N \to N$ is a permutation of the player set N and v is a simple game over $N ,$ then πv is the simple game de<sup>fi</sup>ned by $( \pi \nu ) ( S ) =$ $\nu ( \pi S ) , \forall S \subseteq N .$

The <sup>fi</sup>rst three common axioms for a power index $g$ can now be stated.

(A1) i is a null for v implies $g _ { i } ( \nu ) = 0$

$$
\sum_ {i = 1} ^ {n} g _ {i} (v) = 1.\tag{A2}
$$

(A3) π : $N \to N$ a permutation implies $g _ { i } ( \pi v ) = g _ { j } ( \nu )$ where $i = \pi j .$

To state the fourth axiom we need to extend the equi-desirability and desirability relations to coalitions as was done in [4]. To this end, let $S \perp T$ mean that $\tau _ { i j } ( S ) = T$ for some $i { \sim } j$ and $\pi = \tau _ { i j }$ denotes the transposition of players i and j. This is a binary relation on $2 ^ { N }$ , and we de<sup>fi</sup>ne the coalition equi-desirability≈as the equivalence relation generated by ⊥, i.e.

$S \approx T$ if and only if $S \bot R _ { 1 } . . . \bot R _ { h } = T$ for some h:

Analogously, we consider the relation given by

T⊣ S if and only if $S = \emptyset \ : 0 \Gamma \tau _ { i j } ( S ) \subseteq T$ for some j∈Sand i≿j;

and de<sup>fi</sup>ne the coalition dominance $\succapprox$ as the preorder generated by $\dashv ,$ i.e.

$T { \succap } S$ if and only i ${ \mathrm { ' } } T \substack {  R _ { 1 } . . . .  R _ { h } = S \mathrm { f o r } s 0 \mathrm { m e } h } .$

Relations ≈ and $\succapprox$ are, respectively, extensions o $\Gamma \sim \mathrm { a n d } \gtrsim \mathrm { t o } 2 ^ { N } ,$ , in the sense that, for example, i≿j if and only if $\lbrace i \rbrace \succapprox \lbrace j \rbrace$ . Moreover, ≈ is the equivalence relation associated with $\succapprox$ . Whenever we write $S { \succap _ { \approx { v _ { i } } } } T$ we mean that coalition S dominates coalition T for game v .

Let $\mathcal { W } ^ { s } ( \nu )$ be the set of shift minimal winning coalitions of game v <sup>W ð Þ</sup>and de<sup>fi</sup>ne the sum $\nu _ { 1 } \circ \nu _ { 2 } \circ \dots \circ \nu _ { m }$ of the simple games $\nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { m }$ as follows:

$$
v _ {1} \circ v _ {2} \circ \dots \circ v _ {m} (S) = \left\{ \begin{array}{l l} 1, & \text { if } \quad S \gtrsim_ {v _ {1}} T _ {1} \in \mathcal {W} ^ {s} (v _ {1})   \text { or } \\ & S \gtrsim_ {v _ {2}} T _ {2} \in \mathcal {W} ^ {s} (v _ {2})   \text { or } \\ & \dots \\ & S \gtrsim_ {v _ {m}} T _ {m} \in \mathcal {W} ^ {s} (v _ {m}) \\ 0, & \text { otherwise. } \end{array} \right.
$$

Note that $\mathscr { W } ^ { s } ( \nu _ { 1 } \circ \nu _ { 2 } \circ . . . \circ \nu _ { m } ) \subseteq \bigcup _ { i = 1 } ^ { m } \mathscr { W } ^ { s } ( \nu _ { i } ) .$

We further de<sup>fi</sup>ne $\nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { m }$ shift mergeable if $\mathcal { W } ^ { s } ( \nu _ { 1 } ) , \mathcal { W } ^ { s } ( \nu _ { 2 } ) , \ldots$ $\mathcal { W } ^ { s } ( v _ { m } )$ is a partition of $\mathcal { W } ^ { s } ( \nu _ { 1 } \circ \nu _ { 2 } \circ . . . \circ \nu _ { m } )$

<sup>ð Þ W</sup>This condition says that $\nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { m }$ <sup>Þ</sup>have no pairwise overlaps in the sense that no shift minimal winning coalition in $\nu _ { i }$ can be winning in v and no shift minimal winning coalition in v can be winning in v . Note, however, that a coalition can simultaneously be a minimal winning coalition in several games $\nu _ { j } .$

It follows that if $\nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { m }$ are shift mergeable then

$$
s _ {i} (v _ {1} \circ v _ {2} \circ \dots \circ v _ {m}) = \sum_ {j = 1} ^ {m} s _ {i} (v _ {j})
$$

where $s _ { i } ( \nu )$ is the number of shift minimal winning coalitions containing i.

Finally, let $\begin{array} { r } { s ( \nu ) = \sum _ { i = 1 } ^ { n } s _ { i } ( \nu ) } \end{array}$ . The fourth axiom can now be stated.

(A4) $\nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { m }$ shift mergeable ⇒

$$
g _ {i} (v _ {1} \circ v _ {2} \circ \dots \circ v _ {m}) = \frac {\sum_ {j = 1} ^ {m} s (v _ {j}) g _ {i} (v _ {j})}{\sum_ {j = 1} ^ {m} s (v _ {j})}.\tag{3}
$$

Thus, A4 states that the power of the sum $\nu _ { 1 } \circ \nu _ { 2 } \circ \dots \circ \nu _ { m }$ (being $\nu _ { 1 } ,$ $\nu _ { 2 } , . . . , \nu _ { m }$ shift mergeable games) is a weighted mean of power of the component games $\nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { m } .$ . The weight of a component game $\nu _ { j }$ is the proportion between the sum for every player i∈N of the number of shift minimal winning coalitions containing i, and the sum of the previous numbers for every component game. A similar property, called critical mergeability, is used in [15] to characterize the Johnston power index.

To state the <sup>fi</sup>fth axiom, for u≤v we mean $u ( S ) \leq v ( S )$ for all S N. We say that u is dense in v if $u \leq \nu$ <sup></sup>and the shift minimal winning coalitions for u and for v coincide. The <sup>fi</sup>fth axiom can now be stated.

(A5) If u is dense in $\nu \Rightarrow g _ { i } ( u ) = g _ { i } ( \nu )$

Theorem 3.1. A power index g satisfying A1, A2, A3, A4 and A5 is the Shift power index.

Proof. Existence. It is immediate that, the Shift power index, f de<sup>fi</sup>ned on the domain of simple games by $f _ { i } ( \nu ) { = } s _ { i } ( \nu ) / s ( \nu )$ satisfies A1-A3 and A5. For A4 we have

$$
\begin{array}{l} f _ {i} (v _ {1} \circ v _ {2} \circ \dots \circ v _ {m}) = \frac {s _ {i} (v _ {1} \circ v _ {2} \circ \dots \circ v _ {m})}{s (v _ {1} \circ v _ {2} \circ \dots \circ v _ {m})} \\ = \frac {\sum_ {j = 1} ^ {m} s _ {i} (v _ {j})}{\sum_ {j = 1} ^ {m} s (v _ {j})} (\text { because   of   shift   mergeability }) \\ = \frac {\sum_ {j = 1} ^ {m} s (v _ {j}) f _ {i} (v _ {j})}{\sum_ {j = 1} ^ {m} s (v _ {j})}. \end{array}
$$

Uniqueness. Conversely, let g be an index satisfying A1 through A5 in the domain of simple games. If v has a single shift minimal winning coalition, call it $S _ { v } ,$ then it follows from A1 to A3 that

$$
g _ {i} (v) = \left\{ \begin{array}{l l} 1 / | S _ {v} |, & \text { if   } i \in S _ {v}; \\ 0, & \text { otherwise }. \end{array} \right.\tag{4}
$$

Now consider any simple game v with shift minimal winning coalitions enumerated as $S _ { 1 } , S _ { 2 } , . . . , S _ { m }$ . We can then consider $\nu _ { 1 } \circ \nu _ { 2 } \circ \dots \circ \nu _ { m }$ where each v has a simple shift minimal winning coalition S in game v. Thus $\nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { m }$ are shift mergeable because $\mathcal { W } ^ { s } ( \nu _ { 1 } ) , \mathbf { \bar { \nu } } ^ { \mathrm { w } } ( \nu _ { 2 } )$ $\mathcal { W } ^ { s } ( v _ { m } )$ is a partition of $\mathcal { W } ^ { s } ( \nu _ { 1 } \circ \nu _ { 2 } \circ . . . \circ \nu _ { m } )$ <sup>W ð Þ W ð Þ</sup>. Then, by A4 and Eq. (4), it follows that

$$
s (v _ {j}) g _ {i} (v _ {j}) = \left\{ \begin{array}{l l} 1, & \text { if   } i \in S _ {j}; \\ 0, & \text { otherwise }. \end{array} \right.
$$

Hence, we obtain

$$
g_{i}(u) = \sum_{\substack{S_{j}\\ i\in S_{j}}}1 / s(u) = s_{i}(u) / s(u)
$$

wherein $u = \nu _ { 1 } \circ \nu _ { 2 } \circ \dots \circ \nu _ { m }$ and because u is dense in v, A5 implies $g _ { i } ( \nu ) =$ $S _ { i } ( \nu ) / s ( \nu ) , \mathrm { i . e . } g _ { i } ( \nu ) { = } f _ { i } ( \nu )$ □

Remark 3.2. (Independence of the axiomatic system) The axiom system A1–A5 is independent. Indeed:

(i) The power index g, given $\mathsf { b y } g _ { i } ( \nu ) = \frac { 1 } { n } \operatorname { f o r } \mathrm { a l l } i \in N ,$ , and for all v, satis<sup>fi</sup>es A2–A5 but not A1.

(ii) The power index g, given by $g _ { i } ( \nu ) = 0$ for all i ∈ N, and for all v, satis<sup>fi</sup>es $\mathsf { A } 1 , \mathsf { A } 3 { - } \mathsf { A } 5$ but not A2.

(iii) The power index g, de<sup>fi</sup>ned for all i∈N and for all v given by

$$
g _ {i} (v) = \frac {m _ {i} \cdot s _ {i} (v)}{\sum_ {j = 1} ^ {n} m _ {j} \cdot s _ {j} (v)},
$$

where $( m _ { 1 , } m _ { 2 } , . . . , m _ { n } )$ is a system of positive weights such that $\sum _ { i = 1 } ^ { n } m _ { i } = \dot { 1 }$ with $m _ { i } \neq m _ { j }$ if $i \neq j ,$ satis<sup>fi</sup>es A1–A2, A4–A5 but not A3.

(iv) The power index g, given by $g _ { i } ( \nu ) = \frac { 1 } { | \mathcal { W } ^ { s } ( \nu ) | } \sum _ { S \in \mathcal { W } _ { i } ^ { s } ( \nu ) } \frac { 1 } { | S | }$ for al $i \in N ,$ and for all v, where $\mathcal { W } _ { i } ^ { s } ( \nu ) = \{ S \in \mathcal { W } ^ { s } ( \nu ) : i \in S \}$ <sup>ð Þ</sup>satis<sup>fi</sup>es $\mathsf { A } 1 { - } \mathsf { A } 3$ A5 but not A4.

(v) The power index given by

$$
g _ {i} (v) = \left\{ \begin{array}{l l} f _ {i} (v), & \text { if   } v = v _ {1} \circ v _ {2} \circ \ldots \circ v _ {m} \\ & \text { being   } v _ {1}, v _ {2}, \ldots , v _ {m} \text {   shift   mergeable; } \\ h _ {i} (v), & \text { otherwise. } \end{array} \right.
$$

for all i∈N, and for all v, satis<sup>fi</sup>es A1–A4 but not A5.

We propose a second axiomatic characterization for the Shift power index. To this purpose we will use a property of monotonicity which can simultaneously replace shift mergeability and density in Theorem 3.1. This property of monotonicity compares the behavior of the same player in two different games with the same set of voters. There are some previous works wherein similar monotonicity properties have been used. Indeed, in [20] a characterization of the Shapley value is given using a property of strong monotonicity instead of additivity. In [15] a new characterization of the Deegan–Packel index is provided, using a similar property to strong monotonicity instead of mergeability. It is the property of minimal monotonicity. In the formulation of this property, a relation between two simple games v and w given in terms of the cardinality of the sets of minimal winning coalitions is taken into account. In a second paper, [2] a characterization of the Public Good Index is provided with a similar property.

We now state the last axiom.

(A6) A power index g satis<sup>fi</sup>es the property of shift minimal monotonicity if for any pair of simple games v and w de<sup>fi</sup>ned in N,

$$
g _ {i} (w) \cdot s (w) \geq g _ {i} (v) \cdot s (v),
$$

for all players $i \in N$ such that $\mathcal { W } _ { i } ^ { s } ( w ) \supseteq \mathcal { W } _ { i } ^ { s } ( \nu )$

<sup>W ð Þ  W ð Þ</sup>Thus A6 states that if the set of shift minimal winning coalitions containing a player i in game v is a subset of the set of shift minimal winning coalitions containing this player in game w, then the power of player i in game w is not less than power of player i in game v (we must normalize this power by the number of shift minimal winning coalitions in games v and w).

Note that shift minimal monotonicity implies

$$
g _ {i} (w) \cdot s (w) = g _ {i} (v) \cdot s (v),\tag{5}
$$

for any two simple games v and w, and for all i∈N such that $\mathcal { W } _ { i } ^ { s } ( \nu ) =$ $\mathcal { W } _ { i } ^ { s } ( w )$

In the next result, we propose a new characterization for the Shift power index where axioms A4–A5 are replaced by A6.

Theorem 3.3. A power index g satisfying A1, A2, A3 and A6 is the Shift power index.

Proof. Existence. To prove that the Shift power index satis<sup>fi</sup>es the property of shift minimal monotonicity, consider two simple games v and w and a player $i \in N$ such that $\mathcal { W } _ { i } ^ { s } ( \nu ) \subseteq \mathcal { W } _ { i } ^ { s } ( w )$ . Then

$$
f _ {i} (v) = \frac {s _ {i} (v)}{s (v)},
$$

and,

$$
\begin{array}{l} f _ {i} (w) = \frac {s _ {i} (w)}{s (w)} \\ \qquad = \frac {| \mathcal {W} _ {i} ^ {s} (w) |}{s (w)} \\ \qquad = \frac {| \mathcal {W} _ {i} ^ {s} (v) | + | \mathcal {W} _ {i} ^ {s} (w) \setminus \mathcal {W} _ {i} ^ {s} (v) |}{s (w)} \\ \qquad = \frac {s _ {i} (v) + | \mathcal {W} _ {i} ^ {s} (w) \setminus \mathcal {W} _ {i} ^ {s} (v) |}{s (w)}. \end{array}
$$

Then

$$
\begin{array}{r l} f _ {i} (w) \cdot s (w) & = s _ {i} (v) + | \mathcal {W} _ {i} ^ {s} (w) \setminus \mathcal {W} _ {i} ^ {s} (v) | \\ & \geq s _ {i} (v) \\ & = f _ {i} (v) \cdot s (v) \end{array}
$$

Uniqueness. We can prove the uniqueness by induction on the number of shift minimal winning coalitions. If the game has a unique shift minimal winning coalition, then $\nu = u _ { S }$ for a coalition $S \subseteq N .$ If a power index g satis<sup>fi</sup>es the properties of ef<sup>fi</sup>ciency, symmetry, and null player, then

$$
g _ {i} (v) = \left\{ \begin{array}{l l} \frac {1}{| S |} & \text { if } i \in S \\ 0 & \text { if } i \notin S. \end{array} \right.
$$

Then, the solution is unique. Assume uniqueness whenever the number of shift minimal winning coalitions of a game is less than m and let v be a simple game with m shift minimal winning coalitions. Suppose $\mathcal { W } ^ { s } ( \nu ) = \{ S _ { 1 } , S _ { 2 } , . . . , S _ { m } \}$

Let $R { = } S _ { 1 } \cap S _ { 2 } \cap { \ldots } \cap S _ { m }$ and suppose that i∉R. We de<sup>fi</sup>ne the simple game v′ associated to voter i where $\mathcal { W } _ { i } ^ { s } ( v ^ { \prime } ) = \{ S { \in } \mathcal { W } ^ { s } ( \nu ) : i { \in } S \}$ and $\mathcal { W } _ { i } ^ { s } ( v ^ { \prime } ) = \mathcal { W } _ { i } ^ { m } ( v ^ { \prime } )$

<sup>W W</sup>Taking into account that $\mathcal { W } _ { i } ^ { s } ( \nu ) = \mathcal { W } _ { i } ^ { s } ( v ^ { ' } )$ , by the property of shift <sup>W</sup>minimal monotonicity, it holds

$$
g _ {i} (v) \cdot s (v) = g _ {i} (\boldsymbol {v} ^ {\prime}) \cdot s (\boldsymbol {v} ^ {\prime}).
$$

So by induction $g _ { i } ( \nu )$ is unique when i∉R.

Thus, the <sup>fi</sup>nal step is to demonstrate the uniqueness when $i { \in } R { = } S _ { 1 } \cap S _ { 2 } \cap { \ldots } \cap S _ { m } .$ By symmetry, $g _ { i } ( \nu )$ is a constant c for all members of R. Since the solution is ef<sup>fi</sup>cient and it is unique for all i not in R, it follows that c must be unique.

## Remark 3.4.

(i) The arguments used in the proof of the previous result (uniqueness) are very similar to those used in [2] to characterize the Public Good Index. The main difference resides in the fact that in [1] the induction is on the cardinality of the set of minimal winning coalitions in the game.

(ii) As a Referee has pointed out, in the previous result we can substitute (A6) by the weaker property Eq. (5). The same happens with the strong monotonicity property used in [1] to characterize the Shapley value, that can be substituted by the weaker axiom of marginal contributions. We maintain (A6) because we consider it more intuitive than Eq. (5).

Remark 3.5. (Independence of the second axiomatic system) The axiom system A1–A3 and A6 is independent. Indeed:

(i) Given a simple game v with null voters, so that D≠∅ and $| D | = d { > } 0 ,$ let P be the set of voters $\{ i \in N \colon s _ { i } ( \nu ) \geq s _ { j } ( \nu ) f o t$ r all $j \in N \}$ and $| P | = p .$ By the definition of simple game ${ \cal P } \ne { \cal D } .$ Then the power index g defined as:

$$
g _ {i} (v) = \left\{ \begin{array}{l l} f _ {i} (v) + \frac {\epsilon}{d \cdot s (v)}, & \text { if } i \in D; \\ f _ {i} (v) - \frac {\epsilon}{p \cdot s (v)}, & \text { if } i \in P; \\ f _ {i} (v), & \text { otherwise }. \end{array} \right.
$$

where -N 0 is very close to zero, for all i∈N, and for all v , satisfies A2, A3 and A6, but not A1.

(ii) The power index g, given by $g _ { i } ( \nu ) = 0$ for all $i \in N ,$ and for all v, satisfies $\mathsf { A } 1 , \mathsf { A } 3 , \mathsf { A } 6$ but not A2.

(iii) Given a simple game v, let $| D | = d$ so that $0 \leq d \leq n - 1 ,$ , let $\epsilon _ { i } f o r$ $i { = } 1 , { \ldots } , n { - } d$ be different real numbers close to zero, $\sum _ { i = 1 } ^ { n - d } \epsilon _ { i } = 0 ,$ and with the remaining $2 ^ { n - d } - 1$ partial sums all different. It is clear that the election of these real numbers is always possible. Then the power index g defined as:

$$
g _ {i} (v) = \left\{ \begin{array}{l l} f _ {i} (v), & \text { if   } i \in D; \\ f _ {i} (v) + \frac {\epsilon_ {i}}{s (v)}, & \text { otherwise }. \end{array} \right.
$$

for all $i \in N ,$ and for all v, satisfies A1, A2 and A6, but not A3 (iv) The power index g, given by $g _ { i } ( \nu ) = h _ { i } ( \nu )$ i.e. the Public Good Index, satisfies A1–A3 but not A6

Remark 3.6. A referee has proposed us a modification of the Shift power index. The principle in designing this new index is similar to that used in order to define the Shift power index. The main difference resides in the fact that, with the idea proposed by the referee, those minimal winning coalitions in which a player can be substituted by a weaker player or (and here is the difference) by a set of weaker players should not be considered when we measure power. Taking into account this idea, a new power index could be defined. This index is an independent solution of the Shift power index, in the sense, that we can find examples in where a coalition is considered to compute the Shift power index but not for this new index, and vice versa. As the Shift power index, this new index uses less information than the Public Good Index, but does not satisfy the Riker's Principle. For example, if we consider the game [10;5,5,3,3,3], there is a unique coalition {1,2} that satisfies the Riker's Principle, but this coalition would not be considered by the index proposed by the Referee. In any case, it is our opinion that the new principle and the underlying index proposed by the referee are interesting and deserve to be studied.

## 4. Conclusion

The paper presents (Section 2) a new power index, namely, the Shift power index. The proposed power index is a relative one and it derives from the Banzhaf index and the Public Good Index, since it is based on the number of a particular type of coalitions that a player belongs to. For the Shift power index, the relevant number is the cardinality of the set of shift minimal winning coalitions, that is, the minimal winning coalitions in which it is not possible to replace any player for a weaker one and still maintain the condition of winning coalition.

Besides, in Section 3, we provide two characterizations for the Shift power index and the corresponding Remarks in which we prove that all the properties used in the characterizations are needed.

We think that this paper opens future lines of research. It could be interesting to study procedures to compute the Shift power index. These methods could be based on tools such as multilinear extensions and on generating functions. Another line could be the study of extensions of the Shift power index de<sup>fi</sup>ned for more complex models. In [1], different power indices for games with a priori unions are studied and compared. In a similar way, it is possible to de<sup>fi</sup>ne a modi<sup>fi</sup>cation of the Shift power index when a system of unions is considered. A different possibility could be to consider situations in which the communication among the players is not complete and it is restricted by an undirected graph de<sup>fi</sup>ned on the set of players. And, of course, we can compare the results given by different power indices suggested in the literature in order to assess the a priori distribution of power in a voting body and the results obtained with the Shift power index. Finally, it would be interesting to <sup>fi</sup>nd different real contexts in which the Shift power index would be an appropriate index to measure power.

## Acknowledgements

The authors wish to thank the Editor Andrew Whinston for his supervision task of the reviewing process, three anonymous Referees for carefully reading an earlier version of this work and pointing out useful comments that have allowed us to improve the presentation of the paper, and also to JoDee Anderson for her linguistic support.

The research of Jose Maria Alonso-Meijide was partially funded by Grants INCITE09-207-064-PR from the Xunta de Galicia and ECO2008- 03484-C02-02/ECON from the Spanish Science and Innovation Ministry and the European Regional Development Fund.

The research of Josep Freixas was partially funded by Grants SGR 2009-1029 of Generalitat de Catalunya and MTM 2009-08037 from the Spanish Science and Innovation Ministry.

## References

[1] J.M. Alonso-Meijide, F. Carreras, M.G. Fiestras-Janeiro, G. Owen, A comparative axiomatic characterization of the Banzhaf-Owen coalitional value, Decision Support Systems 43 (2007) 701–712.

[2] J.M. Alonso-Meijide, B. Casas-Méndez, M.J. Holler, S. Lorenzo-Freire, Computing power indices: multilinear extensions and new characterizations, European Journal of Operational Research 188 (2008) 540–554

[3] J.F. Banzhaf, Weighted voting doesn't work: a mathematical analysis, Rutgers Law Review 19 (1965) 317–343.

[4] F. Carreras, J. Freixas, Complete simple games, Mathematical Social Sciences 32 (1996) 139–155.

[5] J. Deegan, E.W. Packel, A new index of power for simple n-person games International Journal of Game Theory 7 (1978) 113–123.

[6] D.S. Felsenthal, M. Machover, Postulates and paradoxes of relative voting power— a critical reappraisal, Theory and Decision 38 (1995) 195–229.

[7] J. Freixas, Banzhaf measures for games with several levels of approval in the input and output, Annals of Operations Research 137 (2005) 45–66.

[8] J. Freixas, The Shapley–Shubik power index for games with several levels of approval in the input and output, Decision Support Systems 39 (2005) 185–195.

[9] J. Freixas, W.S. Zwicker, Weighted voting, abstention, and multiple levels of approval, Social Choice and Welfare 21 (2003) 399–431.

[10] M.J. Holler, Forming coalitions and measuring voting power, Political Studies 30 (1982) 262–271.

[11] M.J. Holler, Two stories, one power index, Journal of Theoretical Politics 10 (1998) 179–190.

[12] M.J. Holler, R. Ono, F. Steffen, Constrained monotonicity and the measurement of power, Theory and Decision 50 (2001) 385–397.

[13] J.R. Isbell, A class of simple games, Duke Mathematics Journal 25 (1958) 423–439.

[14] R.J. Johnston, On the measurement of power: some reactions to Laver, Environment and Planning A 10 (1978) 907–914.

[15] S. Lorenzo-Freire, J.M. Alonso-Meijide, B. Casas-Méndez, M.G. Fiestras-Janeiro, Characterizations of the Deegan–Packel and Johnston power indices, European Journal of Operational Research 177 (2007) 431–444.

[16] W.H. Riker, The Theory of Political Coalitions, Yale University Press, New Haven, USA, 1982.

[17] W.H. Riker, Theory of political coalitions, Journal Studies 30 (1982) 262–271.

[18] L.S. Shapley, M. Shubik, A method for evaluating the distribution of power in a committee system, American Political Science Review 48 (1954) 787–792.

[19] A.D. Taylor, W.S. Zwicker, Simple Games: Desirability Relations, Trading, and Pseudoweightings, Princeton University Press, New Jersey, USA, 1999.

[20] H.P. Young, Monotonic solutions of cooperative games, International Journal of Game Theory 14 (1985) 65–72.

![](/api/attachments/FW66SG34/fulltext/images/907d66da55efed386a77993d48f1974769680b0c100cbc29d68c360611db1b11.jpg)  
José M<sup>a</sup>. Alonso-Meijide received his B. S. Degree and Ph. D. in Mathematics from the University of Santiago de Compostela (Spain). He is a professor at Department of Statistics and Operations Research of the University of Santiago de Compostela since 1997. His research is focused in Game Theory and applications in the <sup>fi</sup>elds of politics and economics. He is author of several papers in international journals, (Annals of Operations Research, Naval Research Logistics, European Journal of Operations Research, etc.). He belongs to various research associations (GTS, SEIO, RSME, SGAPEIO).

![](/api/attachments/FW66SG34/fulltext/images/55cdd3a54a397ff04fd262b8de0a9a6dd7d6430a98bda43054ea73ae8b6d9e9c.jpg)

Josep Freixas received the PhD in Mathematics from the Technical University of Catalonia, in 1994. He works in the Department of Applied Mathematics 3. He was visiting professor in the Bergamo University (Italy) in 1996 and in the Union College of Schenectady in New York (USA) in 2000. His research interests include Decision and game theory, reliability and statistics, and computer sciences. He has published many papers on these topics.

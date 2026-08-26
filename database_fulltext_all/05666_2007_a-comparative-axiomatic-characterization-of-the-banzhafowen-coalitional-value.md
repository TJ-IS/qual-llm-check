---
otero_id: 5666
otero_key: "BZFSPX5F"
title: "A comparative axiomatic characterization of the Banzhaf–Owen coalitional value"
authors: "J.M. Alonso-Meijide; F. Carreras; M.G. Fiestras-Janeiro; G. Owen"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.11.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A comparative axiomatic characterization of the Banzhaf–Owen coalitional value

J.M. Alonso-Meijide <sup>a,⁎</sup>, F. Carreras <sup>b</sup>, M.G. Fiestras-Janeiro <sup>c</sup>, G. Owen

<sup>a</sup> Department of Statistics and Operations Research and Faculty of Sciences of Lugo, University of Santiago de Compostela, Spain <sup>b</sup> Department of Applied Mathematics II and School of Industrial and Aeronautic Engineering of Terrassa, Technical University of Catalonia, Spain

<sup>c</sup> Department of Statistics and Operations Research and Faculty of Economics, University of Vigo, Spain <sup>d</sup> Department of Mathematics, Naval Postgraduate School of Monterey, California, United States

Received 16 May 2006; received in revised form 30 October 2006; accepted 12 November 2006 Available online 4 January 2007

## Abstract

A compact axiomatic characterization of the modified Banzhaf value for games with a coalition structure (Banzhaf–Owen value, for short) is provided. The axiomatic system used here can be compared with parallel axiomatizations of other coalitional values such as the Owen value or the Alonso–Fiestras value, thus giving arguments to defend the use of one of them that will depend on the context where they are to be applied. © 2006 Elsevier B.V. All rights reserved.

JEL classification: C71 Keywords: Cooperative game; Banzhaf value; Coalition structure; Coalitional value

## 1. Introduction

The assessment of the strategic position of each player in any game is a main objective of cooperative game theory, as it can be applied to e.g. sharing costs or profits in economic problems or measuring the power of each agent in a collective decision-making system. The Shapley value φ is the best known concept in this respect, and its axiomatic presentation (Shapley [41], also in Roth [40]) introduced a new, elegant style in game theory and opened a fruitful research line (see Winter [48], and Monderer and Samet [29]).

The first attempt to provide a power measure is, probably, the work produced by Luther Martin in the

1780’s, shown in Riker [39]. (The reader may find an interesting history and discussion of power indices in Felsenthal and Machover [20].) As a sort of reaction to the application of φ to simple games as a power index, suggested by Shapley and Shubik [42], and following a more classical procedure, Banzhaf [12] introduced a different index of power (essentially equivalent to those proposed by Penrose [38] and Coleman [17]) that gave rise to a Banzhaf value β on all cooperative games first defined by Owen [32]. Many axiomatic characterizations of one, the other or both values may be found in the literature (see, e.g., Owen [34], Dubey and Shapley [19], Young [49], Lehrer [27], Straffin [43], Amer and Carreras [7], Nowak [30] or Laruelle and Valenciano [25]). A most interesting one was given by Feltkamp [21], who gave parallel characterizations of the Shapley and Banzhaf values that enhance the similarities and differences between them. Indeed, only one property distinguishes these values: efficiency for the Shapley value versus total power for the Banzhaf value.

Forming coalitions is a most natural behavior in cooperative games, and the evaluation of the consequences that derive from this action is also of great interest to game theorists. Games with a coalition structure were first considered by Aumann and Drèze [11], who extended the Shapley value to this new framework in such a manner that the game really splits into subgames played by the unions isolatedly from each other, and every player receives the payoff allocated to him by the Shapley value in the subgame he is playing within his union. A second approach was used by Owen [33] (also in Owen [36]), when introducing and axiomatically characterizing his coalitional value $\varPhi$ (Owen value). In this case, the unions play a quotient game among themselves, and each one receives a payoff which, in turn, is shared among its players in an internal game. Both payoffs, in the quotient game for unions and within each union for its players, are given by the Shapley value. In addition to the initial one, many other axiomatic characterizations of $\varPhi$ can be found in the literature (Hart and Kurz [24], Winter [47], Amer and Carreras [8,9], Vázquez et al. [44], Hamiache [23] or Albizuri [2] among others).

By applying a similar procedure to the Banzhaf value, Owen [35] obtained a second coalitional value, the modified Banzhaf value Ψ for games with a coalition structure or Banzhaf–Owen value. Here, the payoffs at both levels, that of the unions in the quotient game and that of the players within each union, are given by the Banzhaf value. In this case, no axiomatization was initially provided. A first axiomatic characterization was reached by Albizuri [1], but only on the restricted domain of (monotonic) simple games. Amer et al. [10] were the first to establish a characterization of Ψ on the full domain of all cooperative games. However, as they said in Remark 3.3(b) under a suggestion of a referee of their article, their characterization is far from giving rise to an almost common axiomatization of both $\varPhi$ and $\psi$ similar to Feltkamp's one for $\varphi$ and $\beta .$ (For a wide generalization of Owen's procedure to coalitional semivalues, which encompasses the four coalitional values that will be considered here, the interested reader is referred to Albizuri and Zarzuelo [3]. For a way of extending to games with coalition structure the notion of sharing function, please see van den Brink and van der Laan [13].)

Our aim here is to provide a new axiomatic characterization for the Banzhaf–Owen value $\psi$ that is able to be compared with some of the existing ones for $\varPhi$ and, specifically, with the characterization reached by Vázquez et al. [44]. We will also discuss several series of axioms found in the literature and other values closely related to the Banzhaf–Owen value. Moreover, we will express our detailed opinion on the relevance of axiomatizations and the convenience of considering them with an open mind. We briefly quote from Section 4.3:

“Then, why axiomatic systems? There are some reasons for this interest of game theorists in getting them. First, for a mathematically elegant and pleasant spirit. Second, because a set of basic (and assumed independent and hence minimal) properties is a most convenient and economic tool to decide on the use of the value. Finally, such a set allows a researcher to compare a given value with others and select the most suitable one for the problem he or she is facing each time.”

The organization of the paper is as follows. In Section 2, a minimum of preliminaries is provided. In Section 3 we give the axiomatic characterization of the Banzhaf–Owen value. Section 4 is devoted to comparing it with parallel axiomatizations of $\varPhi ,$ of Alonso and Fiestras' symmetric coalitional Banzhaf value π (Alonso-Meijide and Fiestras-Janeiro [6]) and even of a sort of “counterpart” value $\mu$ introduced by Amer et al. [10] (both to be defined below in due time) and to discussing by the way our results. Section 5 summarizes our conclusions.

## 2. Preliminaries

Although the reader is assumed to be generally familiar with cooperative game theory, we recall here some basic notions.

## 2.1. Games and values

A finite transferable utility cooperative game (from now on, simply a game) is a pair $( N , \nu )$ defined by a finite set of players $N ,$ usually $N = \{ 1 , 2 , . . . , n \}$ , and a function $\nu : 2 ^ { N } { \longrightarrow } R .$ , that assigns to each coalition $S \subseteq N$ a real number v(S) and satisfies $\nu ( \emptyset ) { = } 0$ . Given a finite set $N$ and a coalition $S \subseteq N ,$ , we denote by $( N , \delta _ { S } )$ the Dirac game of coalition S (Feltkamp [21]), given by $\delta _ { S } ( T ) = 1$ if $T { = } S$ and $\delta _ { S } ( T ) = 0$ , otherwise. In the sequel, $\mathcal { G } _ { N }$ will denote the family of all games on a given $N$ and <sup>G</sup> the family of all games.

A player $i \in N$ is a dummy in game $( N , \nu ) \operatorname { i f } \nu ( S \cup \{ i \} ) { = } \nu$ $( S ) + \nu ( \{ i \} )$ for all $S \subseteq N \backslash \{ i \}$ , that ${ \mathrm { i } } \mathbf { s } ,$ if all his marginal contributions equal $\nu ( \{ i \} )$ . Two players $i , j { \in } N$ are symmetric in game $( N , \nu )$ if $\nu ( S \cup \{ i \} ) { = } \nu ( S \cup \{ j \} )$ for all $S \subseteq N \backslash \{ i , j \}$ , i.e., if their marginal contributions to each coalition coincide.

By a value we will mean a map f that assigns to every game $( N , \nu ) { \in } \mathcal { G }$ a vector $f ( N , \nu ) { \stackrel { - } { \in { \cal R } ^ { N } } }$ with components $f _ { i } ( N , \nu )$ <sup>ð Þ</sup>for all $i \in N .$

Definition 2.1. (Owen [32]) The Banzhaf value $\beta$ is the value defined by

$$
\beta_ {i} (N, v) = \frac {1}{2 ^ {n - 1}} \sum_ {S \subseteq N \setminus \{i \}} [ v (S \cup \{i \}) - v (S) ]\tag{1}
$$

for any $i { \in } N$ and any $( N , \nu ) { \in } { \mathcal { G } } .$

## 2.2. Games with a coalition structure

Let us consider a finite set, say, $N = \{ 1 , 2 , . . . , n \}$ . We will denote by $P ( N )$ the set of all partitions of N. Each $P { \in } P ( N )$ , of the form $P = \{ P _ { 1 } , P _ { 2 } , . . . , P _ { m } \}$ , is called a coalition structure or system of unions on N. The socalled trivial coalition structures are $P ^ { n } = \{ \{ 1 \} , \{ 2 \} $ $\{ n \} \}$ , where each union is a singleton, and $P ^ { N } = \{ N \}$ where the grand coalition forms. Given $i \in N , P ( i )$ will denote the subfamily of coalition structures $P { \in } P ( N )$ such that $\{ i \} \in P .$ If $i \in P _ { k } \in P , \ P _ { - i }$ will denote the partition obtained from P when player i leaves union $P _ { k }$ and becomes isolated, i.e.,

$$
P _ {- i} = \left\{P _ {h} \in P: h \neq k \right\} \cup \left\{P _ {k} \setminus \{i \}, \{i \} \right\}.
$$

A cooperative game with a coalition structure is a triple $( N , \nu , P )$ where $( N , \nu ) { \in } \mathcal { G }$ and $P { \in } P ( N )$ . The set of <sup>ð Þ G</sup>all cooperative games with a coalition structure will be denoted by $\mathcal { G } ^ { c s }$ , and by $\mathcal { G } _ { N } ^ { c s }$ the subset where N is the player set.

If $( N , \nu , P ) { \in } \mathcal { G } ^ { c s }$ and $P = \{ P _ { 1 } , P _ { 2 } , . . . , P _ { m } \}$ , the quotient game $( M , \nu ^ { P } )$ is the cooperative game played by the unions, or, rather, by the set $M = \{ 1 , 2 , . . . , m \}$ of their representatives, as follows:

$$
v ^ {P} (R) = v \big (\underset {r \in R} {\cup} P _ {r} \big) \quad \text { for   all } R \subseteq M.\tag{2}
$$

Notice that $( M , \ \nu ^ { P } )$ is nothing but $( N , \ \nu )$ whenever $P { = } P ^ { n }$ . A not completely trivial case is the following.

Example 2.2. Let $( N , \nu ) { \in } \mathcal { G }$ be given and $i , j \in N$ be distinct players. Let $P ^ { i , j }$ be the coalition structure of N where just i and j form a union while the remaining players stay all isolated. In this case, we can slightly alter the notations, take ij as a new player representing both i and j and each other player k as representing himself, thus considering $N ^ { i , j } = \{ i j , 1 , 2 , . . . , \hat { i } , . . . , \hat { j } , . . . , n \}$ (where ˆi and ˆj mean that i and j have been removed) as quotient player set and, as quotient game, the game $\nu ^ { i , j }$ defined by

$$
\begin{array}{l} v ^ {i, j} (S) = v (S) \quad \text { and } \\ v ^ {i, j} (S \cup \{i j \}) = v (S \cup \{i, j \}) \quad \text { for   any   } S \subseteq N \setminus \{i, j \}. \end{array}
$$

As we see, this game, considered by Lehrer [27] and Nowak [30] in their axiomatizations of the Banzhaf value and called “reduced game” or “amalgamation of i and $j ^ { \ast } ,$ , is nothing but the simplest non-trivial example of a quotient game. Its generalization to the case where, instead of $\{ i , j \}$ , some coalition $S \subseteq N$ with $| S | \ge 2$ forms is straightforward.

By a coalitional value we will mean a map g that assigns to every game with a coalition structure $( N , \nu , P )$ a vector $g ( N , \dot { \nu } , \bar { P } ) { \in } R ^ { N }$ with components $g _ { i } ( N , \nu , P )$ for each $i \in N .$

Definition 2.3. (Owen [35]) The Banzhaf–Owen value Ψ is the coalitional value defined by

$$
\begin{array}{l} \Psi_ {i} (N, v, P) = \sum_ {R \subseteq M \setminus \{k \}} \sum_ {T \subseteq P _ {k} \setminus \{i \}} \frac {1}{2 ^ {m - 1}} \frac {1}{2 ^ {p _ {k} - 1}} \\ \qquad \times [ v (Q \cup T \cup \{i \}) - v (Q \cup T) ] \end{array}\tag{3}
$$

for all $i \in N$ and all $( N , \nu , P ) { \in } \mathcal { G } ^ { c s }$ , where $P _ { k } { \in } P$ is the union such that $i \in P _ { k } , \mathrm { m } { = } | M | , p _ { k } { = } | P _ { k } |$ and $Q = \cup _ { r \in R } P _ { r }$

Definition 2.4. Given a value f on , a coalitional value $g$ on $\mathcal { G } ^ { c s }$ is a coalitional f-value if

$$
g (N, v, P ^ {n}) = f (N, v) \quad \text { for   all } \quad (N, v) \in \mathcal {G}.\tag{4}
$$

## 3. An axiomatic approach

We shall consider the following properties for a coalitional value g on $\mathcal { G } ^ { c s }$

A1. (2-Efficiency) For all $( N , \nu ) { \in } { \mathcal { G } } ,$ , and any pair of distinct players $i , j \in N ,$

$$
g _ {i} (N, v, P ^ {n}) + g _ {j} (N, v, P ^ {n}) = g _ {i j} (N ^ {i, j}, v ^ {i, j}, P ^ {n - 1}).
$$

A2. (Dummy player) If $i \in N$ is a dummy in $( N , \nu )$ then $g _ { i } ( N , \nu , P ^ { n } ) { = } \nu ( \{ i \} )$

A3. (Symmetry) If $i , j { \in } N$ are symmetric players in $( N , \nu )$ then $g _ { i } ( N , \nu , P ^ { n } ) { = } g _ { j } ( N , \nu , P ^ { n } )$

A4. (Equal marginal contributions) If (N, v) and $( N , w )$ are games with a common player set $N ,$ and some player $i \in N$ satisfies $\nu ( S \cup \{ i \} ) - \nu ( S ) { = } w ( S \cup \{ i \} ) - w ( S )$ for all $S \subseteq N \{ i \}$ , then $g _ { i } ( N , \nu , P ^ { n } ) { = } g _ { i } ( N , \nu , { } m , P ^ { n } )$

A5. (Neutrality under individual desertion) If $( N , \nu , P ) { \in } \mathcal { G } ^ { c s } , P _ { k } { \in } P$ and $i , j { \in } P _ { k }$ are distinct players, <sup>ð</sup>then

$$
g _ {i} (N, v, P) = g _ {i} (N, v, P _ {- j}).
$$

A6. (1-Quotient game property) If $( N , \nu , P ) { \in } { \mathcal { G } } ^ { c s }$ and $P \in P ( i )$ for some $i \in N ,$ , then

$$
g _ {i} (N, v, P) = g _ {k} (M, v ^ {P}, P ^ {m}),
$$

where $P _ { k } { = } \{ i \}$

Axioms A2 and A3 (also called equal treatment property) are standard in the literature. Axiom A1 was introduced by Lehrer [27] in a slightly different form (as an inequality), although it was soon discovered (see, $\mathrm { e . g . }$ , Carreras and Magaña [14]) that equality holds, as reported also by Nowak [30], while A4 was introduced by Young [49]. We refer to these sources, and also to Haller [22] and Malawski [28], for discussions about the meaning and scope of these properties. The discussion on axioms A5 and A6 will be done in the next section.

We will first establish a close relationship between the coalitional values satisfying A1–A4 and the Banzhaf value. More precisely:

Proposition 3.1. A coalitional value g satisfies A1–A4 if, and only if, it is a coalitional Banzhaf value, i.e.

$$
\begin{array}{l} g _ {i} (N, v, P ^ {n}) = \beta_ {i} (N, v) \quad \text { for   all } i \in N \quad \text { and   all } \\ (N, v) \in \mathcal {G}. \end{array}\tag{5}
$$

Proof. The proof follows the same guidelines as Nowak's [30] (non-trivial) proof. The only difference between Nowak's statement and ours is that he is talking about values, whereas we are referring to coalitional values, although the connection is given by the appearance of the trivial coalition structure $P ^ { n }$ in our axiom set $_ \mathrm { A } 1 { - } \mathrm { A } 4$ □

Remark 3.2. The interest of this first result lies in the existence of an analogous result for the Shapley value, obtained by Young [49] and also cited by Nowak [30] (the difference will be explained in the next section). This is a sort of starting point for our aim to “put in parallel” the Owen value Φ (as a coalitional Shapley value) and the Banzhaf–Owen value $\psi \left( \mathrm { a } \right)$ coalitional Banzhaf value in the above sense).

Now, we are ready to state and prove our main result.

Theorem 3.3. (Existence and uniqueness) A coalitional value g satisfies A1–A6 if, and only if, it is the Banzhaf– Owen coalitional value Ψ. In other words, Ψ is the unique coalitional Banzhaf value that satisfies A5 and A6.

Proof. (a) (Existence) 1. The Banzhaf–Owen coalitional value Ψ satisfies A1–A4. According to Proposition 3.1, it suffices to check Eq. (5). Let $( N , \nu ) { \in } \mathcal { G }$ and $i \in N .$ . As we will deal with $P { = } P ^ { n }$ <sup>ð Þ</sup>, we have $M { = } N ,$ $P _ { k } { = } \{ i \}$ so that $k { = } i$ and $p _ { k } { = } 1$ $T { = } 0$ and $Q { = } R$ when applying formula (3). Thus

$$
\begin{array}{l} \Psi_ {i} (N, v, P) = \sum_ {R \subseteq M \setminus \{k \}} \sum_ {T \subseteq P _ {k} \setminus \{i \}} \frac {1}{2 ^ {m - 1}} \frac {1}{2 ^ {p _ {k} - 1}} \\ \qquad \times [ v (Q \cup T \cup \{i \}) - v (Q \cup T) ] \end{array}
$$

reduces to

$$
\begin{array}{c} \Psi_ {i} (N, v, P ^ {n}) = \sum_ {R \subseteq N \setminus \{i \}} \frac {1}{2 ^ {n - 1}} [ v (R \cup \{i \}) - v (R) ] \\ = \beta_ {i} (N, v). \end{array}
$$

2. The Banzhaf–Owen value Ψ satisfies $\mathrm { A } 5 ,$ the property of neutrality under individual desertion. Let $( N , \nu , P ) { \in } \mathcal { G } ^ { c s } , P _ { k } { \in } P$ and $i , j \in P _ { k }$ be distinct players. <sup>ð</sup>Let

$$
P _ {- j} = \left\{P _ {1} ^ {\prime}, P _ {2} ^ {\prime}, \dots , P _ {m + 1} ^ {\prime} \right\},
$$

where $P _ { h } ^ { \prime } { = } P _ { h }$ for every $h { \in } M \backslash \{ k \} , \ P _ { k } ^ { \prime } { = } P _ { k } \backslash \{ j \}$ and $P _ { m + 1 } ^ { \prime } = \{ j \}$ , and let $M ^ { \prime = } ( 1 , 2 , \dots , m , m + 1 \}$ . Then, $m ^ { \prime } { = } m + 1$ and $p _ { k } ^ { \prime } { = } p _ { k } { - } 1$ so that

$$
\begin{array}{l} \Psi_ {i} (N, v, P _ {- j}) = \sum_ {R \subseteq M ^ {\prime} \setminus \{k \}} \sum_ {T \subseteq P _ {k} ^ {\prime} \setminus \{i \}} \frac {1}{2 ^ {m ^ {\prime} - 1}} \frac {1}{2 ^ {p _ {k} ^ {\prime} - 1}} \\ \qquad \times [ v (Q \cup T \cup \{i \}) - v (Q \cup T) ] \end{array}
$$

reduces, by separating the cases $m + 1 \in R$ and $\mathbf { m } { + } 1 \not \in R$ and grouping terms again, to

$$
\begin{array}{l} \Psi_ {i} (N, v, P _ {- j}) = \sum_ {R \subseteq M \setminus \{k \}} \sum_ {T \subseteq P _ {k} \setminus \{i \}} \frac {1}{2 ^ {m - 1}} \frac {1}{2 ^ {p _ {k} - 1}} \\ \qquad \times [ v (Q \cup T \cup \{i \}) - v (Q \cup T) ] \\ \qquad = \Psi_ {i} (N, v, P). \end{array}
$$

3. The Banzhaf–Owen value Ψ satisfies A6, the 1- quotient game property. Let $( N , \nu , P ) { \in } \mathcal { G } ^ { c s }$ be such that $P \in P ( i )$ , and let $P _ { k } { = } \{ i \}$ <sup>ð</sup>. Then $p _ { k } { = } 1$ <sup>G</sup>, so that $T { = } 0$ and therefore

$$
\begin{array}{l} \Psi_ {i} (N, v, P) = \sum_ {R \subseteq M \setminus \{k \}} \sum_ {T \subseteq P _ {k} \setminus \{i \}} \frac {1}{2 ^ {m - 1}} \frac {1}{2 ^ {p _ {k} - 1}} \\ \qquad \times [ v (Q \cup T \cup \{i \}) - v (Q \cup T) ] \end{array}
$$

reduces to

$$
\begin{array}{l} \Psi_ {i} (N, v, P) = \sum_ {R \subseteq M \setminus \{k \}} \frac {1}{2 ^ {m - 1}} [ v (Q \cup \{i \}) - v (Q) ] \\ = \sum_ {R \subseteq M \setminus \{k \}} \frac {1}{2 ^ {m - 1}} [ v ^ {P} (R \cup \{k \}) - v ^ {P} (R) ] \\ = \beta_ {k} (M, v ^ {P}) = \Psi_ {i} (M, v ^ {P}, P ^ {m}). \end{array}
$$

(b) (Uniqueness) Let us assume for the moment that two coalitional Banzhaf values $g ^ { 1 }$ and $g ^ { 2 }$ satisfy neutrality under individual desertion (A5) and the 1- quotient game (A6). Then we can find a game $( N , \nu )$ and a coalition structure P on N with the maximum number of unions such that $g ^ { 1 } ( N , \nu , P ) \not = g ^ { 2 } \ ( N , \nu , P )$ , i.e., $g _ { i } ^ { 1 }$ $( N , \nu , P ) \neq g _ { i } ^ { 2 } ( N , \nu , P )$ for some $i \in N .$

As $g ^ { 1 }$ and $g ^ { 2 }$ are coalitional Banzhaf values, it follows that $m { < } n ,$ . Let us take $P _ { k } { \in } P$ such that $i \in { \cal P } _ { k } .$ Two possible cases arise:

$\dot { } | P _ { k } | = 1$ . Then, $P _ { k } { = } \{ \mathrm { i } \}$ . By A6 we have

$$
\begin{array}{l} g _ {i} ^ {1} (N, v, p) = g _ {k} ^ {1} (M, v ^ {P}, P ^ {m}) \quad \text { and } \\ g _ {i} ^ {2} (N, v, P) = g _ {k} ^ {2} (M, v ^ {P}, P ^ {m}). \end{array}
$$

Since $g ^ { 1 }$ and $g ^ { 2 }$ are coalitional Banzhaf values

$$
g _ {k} ^ {1} (M, v ^ {P}, P ^ {m}) = \beta_ {k} (M, v ^ {P}) = g _ {k} ^ {2} (M, v ^ {P}, P ^ {m}).
$$

Therefore, $g _ { i } ^ { 1 } ( N , \nu , P ) { = } g _ { i } ^ { 2 } \ ( N , \nu , P )$ , a contradiction. $\mathbf { \nabla } \cdot | P _ { k } | > 1$ . Then, there is some $j \in P _ { k }$ such that $j \neq i .$ By A5,

$$
\begin{array}{l} g _ {i} ^ {1} (N, v, P) = g _ {i} ^ {1} (N, v, P _ {- j}) \text { and } \\ g _ {i} ^ {2} (N, v, P) = g _ {i} ^ {2} (N, v, P _ {- j}). \end{array}
$$

By the maximality of partition P it follows that

$$
g _ {i} ^ {1} (N, v, P _ {- j}) = g _ {i} ^ {2} (N, v, P _ {- j}),
$$

and this leads to $g _ { i } ^ { 1 } ( N , \nu , P ) { = } g _ { i } ^ { 2 } ( N , \nu , P )$ , a contradiction again.

Remark 3.4. (Independence of the axiomatic system) The axiom system A1–A6 is independent. Indeed:

(i) The coalitional value g defined, with the same notation as in case of Ψ for Eq. (3) and adding $t { = } | T |$ and $r { = } | R |$ , as

$$
g_{i}(N,v,P) = \sum_{\substack{R\subseteq M\setminus \{k\} \\ T\subseteq P_{k}\setminus \{i\}}}\frac{(r + t)!(m + p_{k} - r - t - 2)!}{(m + p_{k} - 1)!}\\ \times [v(Q\cup T\cup \{i\}) - v(Q\cup T)],
$$

satisfies A2–A6, but not A1.

(ii) The coalitional value g given by $g \ ( N , \nu , P ) = 0$ for all $( N , \nu , P ) \in \mathcal { G } ^ { c s }$ satisfies A1 and $_ { \mathrm { A } 3 - \mathrm { A } 6 }$ , but not A2.

(iii) Let i and j be two distinct and fixed players. Let $g$ be the coalitional value defined as follows:

• If N = {i, j} and P = {N},

$$
g _ {i} (N, v, P) = \frac {3}{4} [ v (N) - v (\{j \}) ] + \frac {1}{4} v (\{i \}) \text {   and   }
$$

$$
g _ {j} (N, v, P) = \frac {1}{4} [ v (N) - v (\{i \}) ] + \frac {3}{4} v (\{j \}).
$$

• Otherwise, for every $( N , \nu , P ) { \in } \mathcal { G } ^ { c s } \setminus \{ ( \{ i , j \} , \nu , \{ N \} ) \}$

$g _ { k } ( N , \nu , P ) = \varPsi _ { k } ( N , \nu , P )$ ; for every $k { \in } N .$

Then g satisfies A1–A2 and $_ { \mathrm { A 4 - A 6 } }$ , but not A3.

(iv) The coalitional value g defined as

$$
g _ {i} (N, v, P) = \left\{ \begin{array}{l l} \Psi_ {i} (N, v, P) & \text { if } (N, v, P) \not \in \mathcal {C} \\ 0 & \text { if } (N, v, P) \in \mathcal {C}, \end{array} \right.
$$

where $\mathcal { C } = \{ ( N , \nu , P ) { \in } \mathcal { G } ^ { c s } : \nu = a _ { S } \delta _ { S }$ ; for some $S { \subsetneq } N$ $\textstyle { a _ { S } } \in R  \}$ <sup>C ¼ fð</sup>, satisfies $_ \mathrm { A l - A } 3$ and ${ \mathrm { A } } 5 { \mathrm { - } } { \mathrm { A } } 6 .$ , but not A4.

(v) The symmetric coalitional Banzhaf value π, introduced by Alonso-Meijide and Fiestras-Janeiro [6] and defined, with the same notation as in the case of $\psi$ for Eq. (3) and adding $t { = } | T |$ , by

$$
\begin{array}{l} \pi_ {i} (N, v, P) = \sum_ {R \subseteq M \setminus \{k \}} \sum_ {T \subseteq P _ {k} \setminus \{i \}} \frac {1}{2 ^ {m - 1}} \frac {t ! (p _ {k} - t - 1) !}{p _ {k} !} \\ \qquad \times [ v (Q \cup T \cup \{i \}) - v (Q \cup T) ], \end{array}
$$

satisfies A1–A4 and A6, but not A5 (for details, see Alonso-Meijide and Fiestras-Janeiro [6]). This coalitional value will be considered in detail in the next section.

(vi) The coalitional value g given by $g ~ ( N , \nu , P ) =$ $\beta ( N , \nu )$ for all $( N , \nu , P ) { \in } { \mathcal { G } } ^ { c s }$ satisfies A1–A5, but not $_ { \mathrm { A } 6 }$

## 4. Discussion

This section is devoted to the analysis and criticism of the results obtained in Section 3.

## 4.1. On the axioms

Some comments are in order concerning the properties we have used as axioms. First, it bears mention that properties A1–A4 might be replaced with any other system of axioms that characterizes the Banzhaf value by adding the mention of the trivial coalition structure as we did before. In particular, A1 is equivalent, in the presence of $_ { \mathrm { A } 2 - \mathrm { A } 4 }$ , to the so-called total power property (with regard to $P ^ { n } { } _ { ; }$ , of course), which states

$$
\begin{array}{l} \sum_ {i \in N} g _ {i} (N, v, P ^ {n}) = \frac {1}{2 ^ {m - 1}} \sum_ {S \subseteq N} \sum_ {i \notin S} [ v (S \cup \{i \}) - v (S) ] \\ \text { for   all } (N, v) \in \mathcal {G} \end{array}
$$

and can be traced back (omitting $P ^ { n } )$ at least to Owen [34] and Dubey and Shapley [19]. Moreover, note that no use has been made of additivity nor of strong monotonicity (Young [49]) in our system, although it should be noticed that A4 is what Young calls independence, a property weaker than strong monotonicity. Not only φ and β, but all semivalues (see Weber [45], Dubey et al. [18] or Weber [46] for this notion) satisfy A2–A4 (always omitting $P ^ { n } )$ and an ad hoc modification of the total power property for each one of them.

A5 (neutrality under individual desertion) describes the invariance of the allocations given by a coalitional value to the players of any union in front of the existence of self-isolating players in that union. This property is stronger than the “balanced contributions property” that will be considered below.

Finally, A6 (1-quotient game property) states that, using the coalitional value in the original game with a coalition structure, any isolated player gets the same payoff as the union he forms if we use the same coalitional value in the quotient game with the trivial singleton structure. This property is weaker than the “quotient game property” that will be described below.

## 4.2. Other properties, other values

Let us now consider, for purposes of comparison, a new series of properties for a coalitional value that have been used as axioms in the literature. We recall that $P _ { k } ,$ $P _ { h } \in P$ are symmetric unions in $( N , \nu , P )$ if k and h are symmetric players in the quotient game $( M , \nu ^ { P } )$

B1. (Efficiency) For all $( N , \nu ) { \in } \mathcal { G }$

$$
\sum_ {i \in N} g _ {i} (N, v, P ^ {n}) = v (N).
$$

B5. (Balanced contributions within unions) For all $( N , \nu , P ) { \in } { \mathcal { G } } ^ { c s }$ and all $i , j { \in } P _ { k } { \in } P$

$$
g _ {i} (N, v, P) - g _ {i} (N, v, P _ {- j}) = g _ {j} (N, v, P) - g _ {j} (N, v, P _ {- i}).
$$

B6. (Quotient game property) For all $( N , \nu , P ) { \in } \mathcal { G } ^ { c s }$ and all $P _ { k } { \in } P$

$$
\sum_ {i \in P _ {k}} g _ {i} (N, v, P) = g _ {k} (M, v ^ {P}, P _ {m}).
$$

B7. (Symmetry in the quotient game) If $P _ { k }$ and $P _ { h }$ are symmetric unions in $( N , \nu , P )$ , then

$$
\sum_ {i \in P _ {k}} g _ {i} (N, v, P) = \sum_ {j \in P _ {h}} g _ {j} (N, v, P).
$$

As was said in Section 4.1, A5 is stronger than B5, whereas A6 is weaker than B6. Both relations are clear.

Now, we list in Table 1 all the properties A1–A6 and B1, B5 and B6, specifying which of them are satisfied by each one of the four coalitional values we are considering in this paper, namely, the Banzhaf–Owen value Ψ, the symmetric coalitional Banzhaf value or Alonso-Fiestras value for short π (which follows Owen's [33,35] two-step procedure but applies the Banzhaf value in the quotient game and the Shapley value within unions), the classical Owen value Φ, and a “counterpart” μ of π introduced as a counterexample by Amer et al. [10] (which uses the Shapley and Banzhaf values in reverse order). Note therefore that these four values cover all the variations of Owen's scheme using the Shapley and Banzhaf values.

An OK (resp., empty) entry in the four final columns means that the corresponding coalitional value satisfies (resp., fails to satisfy) the corresponding property. The proof of the positive (OK) entries and suitable counterexamples in case of failure can be easily found in the literature concerning these four values already mentioned here. It is worthy of mention that property A1, 2-efficiency, is specific of Ψ. The total power property for this value differs from the corresponding one for π (see Alonso-Meijide and Fiestras-Janeiro [6], although they share a common spirit.

Table 1 Properties and coalitional values

<table><tr><td>Symbol</td><td>Property</td><td> $\Psi$ </td><td> $\pi$ </td><td> $\Phi$ </td><td> $\mu$ </td></tr><tr><td>A1</td><td>2-Efficiency/total power</td><td>OK</td><td>OK</td><td></td><td></td></tr><tr><td>B1</td><td>Efficiency</td><td></td><td></td><td>OK</td><td>OK</td></tr><tr><td>A2</td><td>Dummy player</td><td>OK</td><td>OK</td><td>OK</td><td>OK</td></tr><tr><td>A3</td><td>Symmetry</td><td>OK</td><td>OK</td><td>OK</td><td>OK</td></tr><tr><td>A4</td><td>Equal marginal contributions</td><td>OK</td><td>OK</td><td>OK</td><td>OK</td></tr><tr><td>A5</td><td>Neutrality under individual desertion</td><td>OK</td><td></td><td></td><td></td></tr><tr><td>B5</td><td>Balanced contributions within unions</td><td>OK</td><td>OK</td><td>OK</td><td>OK</td></tr><tr><td>A6</td><td>1-Quotient game</td><td>OK</td><td>OK</td><td>OK</td><td>OK</td></tr><tr><td>B6</td><td>Quotient game</td><td></td><td>OK</td><td>OK</td><td></td></tr><tr><td>B7</td><td>Symmetry in the quotient game</td><td></td><td>OK</td><td>OK</td><td></td></tr><tr><td>MLE</td><td>Computation by multilinear extensions</td><td>OK</td><td>OK</td><td>OK</td><td>OK</td></tr></table>

The last row–not essential to our discussion, but nice enough to be included here–refers to the possibility of computing a value by using, as in the well known cases of the Shapley value (Owen [31]) and the Banzhaf value (Owen [32]), the multilinear extension of the game where it is applied. The references are Owen and Winter [37] for Φ, Carreras and Magaña [14] (see also Carreras and Magaña [15]) for Ψ, and Alonso-Meijide et al. [4] for π and μ. The multilinear extension, introduced by Owen [31], becomes therefore a very interesting tool, for both theory and practice, in the framewrk of coalitional values.

For a moment, we will disregard value μ and focus on the remaining values Φ, Ψ and π. The important point is that we have, then, parallel (i.e., very close) axiomatic characterizations of these coalitional values. We state them.

Theorem 4.1. (Vázquez et al. [44]) A coalitional value satisfies B1, A2–A4 and B5 and B6 if, and only if, it is the Owen value Φ.

Theorem 4.2. (Theorem 3.3 in this paper) A coalitional value satisfies A1–A6 if, and only if, it is the Banzhaf– Owen value Ψ.

Theorem 4.3. (Alonso-Meijide and Fiestras-Janeiro [6]) A coalitional value satisfies A1–A4, B5 and B6 if, and only if, it is the symmetric coalitional Banxhaf value π.

As is seen, the only basic difference between Φ and π lies in the fact that the former is a coalitional φ-value whereas the latter is a coalitional β-value. Instead, the differences between Φ and Ψ arise in axioms A1/B1, A5/B5 and A6/B6, the latter two pairs being linked by an implication relationship, while the differences between π and Ψ are limited to A5/B5 and A6/B6. We feel that this is a complete generalization of Feltkamp's [21] axiomatic characterizations of φ and β. It also enhances the role of π as an “intermediate” value between Φ and Ψ, and we wish to mention here that Theorem 4.3 extends in a natural way to all symmetric coalitional binomial semivalues $\pi ^ { p }$ for $p \in \mathsf { \Gamma } [ 0 ]$ , 1] (introduced by Carreras and Puente [16]), as is shown in Alonso-Meijide et al. [5].

It has not been an easy task to make changes on B5 and B6 in order to get, respectively, really simple and sharp axioms A5 and A6, those that mark the essential differences between Φ and Ψ. It has been necessary to “split hairs” accurately.

Which is the reason to have included the symmetric coalitional Banzhaf value π in our considerations? Well, Alonso-Meijide and Fiestras-Janeiro [6] realized that Ψ fails to satisfy two in principle interesting properties of Φ, namely B6 (quotient game property) and B7 (symmetry in the quotient game). Then they suggested to modify Owen’s two-step allocation scheme (common to Φ and Ψ ) and use β for sharing in the quotient game and φ to sharing within unions. This gave rise to π, that satisfies B6 and B7 but differs from the Owen value Φ in satisfying A1 instead of B1. In Section 4.3, we will look again at the meaning of π.

Now, we would like to refer to the work by Amer et al. [10]. Their first axiomatic characterization of the Banzhaf–Owen value on the domain of all cooperative games was reached by considering six properties that, for our purposes, do not need to be stated in detail:

C1. Additivity.

C2. Dummy player property.

C3. Symmetry within unions.

C4. Many null players.

C5. Delegation neutrality.

C6. Delegation transfer.

Properties C1–C3 are standard in the literature. C4 is perhaps the most striking one. C5 and C6 refer to the socalled “delegation game”, close to Lehrer's [27] “reduced game” but avoiding the use of different player sets. In order to show–partially–the independence of this axiom system, it is introduced in Remark 2.1(b) the “fourth value” μ (a mixed coalitional value that can be now viewed as a “counterpart” of π), since it satisfies all properties but C4 (see Remark 3.3(a) in Amer et al. [10]), thus proving that this “rare” property does not follow from the remaining ones. The problem with this axiomatic characterization is that it is far from any of the existing ones for the Owen value Φ, as the authors recognize in their Remark 3.3(b) following a suggestion of a referee of their article, because Φ satisfies all but property C6 but it is hard to imagine which property–if any–would be able to replace C6 and complete a hypothetical parallel axiomatization of Φ.

In our opinion, the relative “failure”, only in this sense, of the work by Amer et al. [10] enforces still more our result (Theorem 3.3).

Finally, let us deal with value μ. We first introduce two more properties for a coalitional value $g \colon$

D1. (Many-quotient game property) If $( N , \nu , P ) { \in } { \mathcal { G } } ^ { c s }$ and $P _ { k } { \in } P$ is such that $p _ { k } { = } | P _ { k } | { > } 1$ then

$$
\sum_ {i \in P _ {k}} g _ {i} (N, v, P) = g _ {k} (M, v ^ {P}, P ^ {m}).
$$

D2. (2-Efficiency within unions) For all $( N , \nu , P ) { \in } { \mathcal { G } } ^ { c s }$ any $P _ { k } { \in } P$ <sup>ð</sup>and any pair of distinct players $i , j \in P _ { k } ,$

$$
g _ {i} (N, v, P) + g _ {j} (N, v, P) = g _ {i j} (N ^ {i, j}, v ^ {i, j}, P ^ {i j}),
$$

where $P ^ { i j }$ is the partition that arises from P by simply collapsing i and j in a single player $i j .$

Notice that property D1 and property A6 are complementary particular cases of property B6. Furthermore, it is not difficult to see that D2 coincides with C6 (the delegation transfer property introduced by Amer et al. [10]): the only difference is, roughly speaking, that, in the original delegation transfer property, the delegating player becomes a null player, whereas this player disappears in D2.

Thus, B6\A6 and C6 are consistent notations for D1 and D2, respectively, so that we will use them in the sequel.

Then, we have a fourth result concerning μ and using C6 (Theorem 4.4), whose proof is omitted since it is similar to that of Theorem 3.3, and a new and interesting comparative table referred to the four values (Table 2) where the splitting of B6 into A6 and B6\A6 matters.

Table 2  
New properties and coalitional values

<table><tr><td>Symbol</td><td>Property</td><td> $\Psi$ </td><td> $\pi$ </td><td> $\Phi$ </td><td> $\mu$ </td></tr><tr><td>A1</td><td>2-Efficiency/total power</td><td>OK</td><td>OK</td><td></td><td></td></tr><tr><td>B1</td><td>Efficiency</td><td></td><td></td><td>OK</td><td>OK</td></tr><tr><td>A2</td><td>Dummy player</td><td>OK</td><td>OK</td><td>OK</td><td>OK</td></tr><tr><td>A3</td><td>Symmetry</td><td>OK</td><td>OK</td><td>OK</td><td>OK</td></tr><tr><td>A4</td><td>Equal marginal contributions</td><td>OK</td><td>OK</td><td>OK</td><td>OK</td></tr><tr><td>B5</td><td>Balanced contributions within unions</td><td>OK</td><td>OK</td><td>OK</td><td>OK</td></tr><tr><td>A6</td><td>1-Quotient game</td><td>OK</td><td>OK</td><td>OK</td><td>OK</td></tr><tr><td>B6\A6</td><td>Many-quotient game</td><td></td><td>OK</td><td>OK</td><td></td></tr><tr><td>C6</td><td>2-Efficiency within unions/delegation transfer</td><td>OK</td><td></td><td></td><td>OK</td></tr></table>

Theorem 4.4. A coalitional value satisfies B1, A2–A4, B5, A6 and C6 if, and only if, it is the counterpart value $\mu .$

Remark 4.5. Even a final axiomatic characterization of $\psi$ can be stated, once we have considered C6. In effect: a coalitional value satisfies A1–A4, B5, A6, and C6 if, and only if, it is the Banzhaf–Owen value Ψ. The proof is analogous to that of 3.3.

## 4.3. On the philosophy behind axiomatics

To close this section, we would like to make some comments about what is behind this “logical game” of axiomatizations.

For any value, understood as a solution concept for cooperative conflicts, it is always interesting, in both theory and practice, to have an explicit formula and even an alternative computation procedure. This is the case of the four coalitional values mentioned here, Φ, $\psi ,$ π and $\mu ,$ all of which are obtained by combining the weighting coefficients of $\varphi$ and $\beta$ in similar formulas and also by applying the multilinear extension technique.

Also a list of properties of the value, as long as possible, is always desirable. Then, why axiomatic systems? There are some reasons for this interest of game theorists in getting them. First, for a mathematically elegant and pleasant spirit. Second, because a set of basic (and assumed independent and hence minimal) properties is a most convenient and economic tool to decide on the use of the value. Finally, such a set allows a researcher to compare a given value with others and select the most suitable one for the problem he or she is facing each time.

Why are parallel axiomatic characterizations especially interesting? Because they favor ease when comparing different options to be chosen as the preferred value. (Of course, there may also be other criteria to decide which is the most suited value/index to describe the considered situation: the behavioral model, the belonging or less to the core, the monotonicity– according to various definitions–and so on.)

Then, we feel that one should strongly avoid being dogmatic at this point. Probably, there is no value able to cover all situations. For example, there is no unanimous criterion to choose among using either the Shapley value φ or the Banzhaf value $\beta$ as power index in all cases. We contend that pure and applied game theorists should be flexible at most in this respect. On the one hand, in both theory and practice, one has often to handle additional information not stored in either the characteristic function v of the game or the coalition structure when evaluating this couple. On the other hand, only a few properties found in the literature can really be considered absolutely compelling, i.e., almost no axiom is compelling in vacuo, but only inserted in the framework of a given, specific cooperative conflict. Even those that appear as the best placed in this sense might well be conditioned by the characteristics of the problem where we pretend to use the value they define. The conclusion is that all of us should look at axioms with an open mind and without a priori value judgements. The history of science is full of examples of theoretical models that only after a certain period of time have been proven to be useful in practice. Let us briefly illustrate these considerations by means of some simple instances.

Example 4.6. (a) Assume that N is a set of workers in a given production area and P reflects the classification of them into the firms they are working for. Assume, besides, that g is a coalitional value that allocates to each worker his salary and to each firm its (net) income (say, per year in both cases). In this context, axiom B5 (balanced contributions within unions) is too weak since here it seems more suitable to assume the stronger hypothesis that the salary of a worker will not change if a partner leaves the firm, and this is precisely axiom A5 (neutrality under individual desertion). Furthermore, axiom B6 (quotient game property) is no compelling either because the sum of the salaries of the workers of a firm needs not coincide with the net income of the firm. This seems too strong. However, if a worker creates and holds his own firm alone, it is very reasonable that his salary coincides with the net income of his firm, and this is precisely the weaker axiom A6 (1-quotient game property). Thus, we have in mind the Banzhaf–Owen value Ψ.

(b) Now, assume that political parties are the agents in a parliamentary context and the coalition structures reflect the coalition formation. Assume, moreover, that g is a coalitional value that measures, in some sense, the “power” of both parties and coalitions. In this case, A5 (neutrality under individual desertion) might not be a reasonable property, but not necessarily should it be automatically replaced with B5 (balanced contributions within unions): maybe the effect on a party of the desertion of a coalition partner is not the same as the effect when the roles are interchanged. Also B6 (quotient game property) may be not completely convincing, since the power concept at the coalition level might well be different from power at the party level, and hence the sum of the power indices of the colligated parties might differ from the power of their union in the quotient game—at least, it is not completely clear why they should coincide. Instead, it seems much more reasonable that this coincidence holds in the case of a party that remains isolated, and this is property A6 (1-quotient game).

(c) Still in the parliamentary framework, one can consider that parties in the original game, and unions in the quotient game, fight for something called “power”. However, once each union gets its fraction of power in the quotient game, it is often convenient to share this index among its members efficiently. For example, and especially, whenever the coalition is winning and gives rise to a coalition government, that coalition will need to share cabinet and parliamentary positions such as presidencies and ministries and budgets management among its members. Even if one prefers the Banzhaf value as power index, he/she will apply it in the quotient game, but will necessarily prefer the efficient Shapley value when sharing within the union. In other words, he/she will prefer the symmetric coalitional Banzhaf value π, because of the failure of Ψ as to B6 and B7.

These examples show the relativity of the term “compelling” and hence the convenience of looking at axioms and axiomatic characterizations with no constraints and to appreciate those axiomatizations that permit a comparison between different (coalitional, in this case) values. We hope that the reader will hold this view and agree, therefore, with our opinion so far expressed.

Remark 4.7. Finally, we would like to point out an additional criterion that supports the use of the Banzhaf–Owen value Ψ as power index and comes from a rather different, not axiomatic approach: the probabilistic one. We are referring to a nice paper by Laruelle and Valenciano [26] where three meanings of Ψ are provided in the voting context. By interpreting power as the ability–say, probability–to become decisive in a voting process, the authors state three interpretations of this coalitional value: (a) as a modified Banzhaf index of the given voting rule; (b) as the Banzhaf index of a modified voting rule; and (c) as an (extended) Banzhaf index of an (extended notion of) voting rule. Two conclusions of this article deserve also being mentioned: (1) the Banzhaf–Owen values of different agents can be compared only in case of players of the same union, a condition to be taken into account in the applications of this power index; (2) similar interpretations of other coalitional values in the voting context are problematic; in other words, the arguments given for Ψ do not adapt convincingly to them.

Unfortunately, the authors leave to the reader the verification of this but give no hint.

## 5. Conclusions

We have provided (Section 3) a new axiomatic characterization of the modified Banzhaf value for games with a coalition structure (Owen [35]) on the full domain of all cooperative games. It is the second axiomatization of this value that is published, the first one having been given by Amer et al. [10], but the basic difference is that ours can be compared with parallel characterizations of the classical Owen coalitional value (Owen [33]), the symmetric coalitional Banzhaf value (Alonso-Meijide et al. [6]), and a counterpart of the latter also found in Amer et al. [10]. Note that these four values cover all ways of combining the use of the Shapley and Banzhaf values, in the quotient game and within the unions. We have also shown the logical independence of our axiomatic system.

Next (Sections 4, 4.1 and 4.2) we have discussed our axioms, relating and/or comparing them with other properties that have previously appeared in the literature on coalitional values, and putting in parallel different sets of axioms to cope with the relevance of each one of the four values and the essential differences between them (Tables 1 and 2 and Theorems 4.1–4.4). In particular, Theorem 4.4 provides the first axiomatic characterization of the “counterpart” value, and even an additional characterization of the modified Banzhaf value for games with a coalition structure is given in Remark 4.5. It seems also worthwhile to mention that all four values can be computed by means of the multilinear extension (last row of Table 1).

Finally, we have developed (Sections 4 and 4.3) some reflections on the meaning of the axiomatizations and enhanced the convenience to have such descriptions of a given value and, moreover, when possible, parallel axiomatizations, which should be useful to both theorists and practitioners in order to choose, in each situation they face, the best solution concept. We have also expressed our criticism against too dogmatic views when deciding on whether or not a given axiom is “compelling”.

## Acknowledgements

The authors wish to thank interesting suggestions and comments made by Professor I. García-Jurado and an anonymous referee.

Financial support from Xunta de Galicia (Grant PGIDT03PXI20701PN), Generalitat de Catalunya (Grant SGR 2005-00651) and the Science and Technology Spanish Ministry and the European Regional Development Fund (Grants BEC 2002-04102-C02-02, SEJ 2005-07637-C02-02 and BFM 2003-01314, the latter of which sponsored Owen's visits to Terrassa in April 2005 and June 2006 and Alonso-Meijide's visit to Terrassa in March–April 2006) is gratefully acknowledged.

## References

[1] M.J. Albizuri, An axiomatization of the modified Banzhaf– Coleman index, International Journal of Game Theory 30 (2001) 167–176.

[2] M.J. Albizuri, Axiomatizations of Owen value without efficiency, Discussion Paper 25, Department of Applied Economics IV, Basque Country University, Spain, 2002.

[3] M.J. Albizuri, J.M. Zarzuelo, On coalitional semivalues, Games and Economic Behavior 49 (2004) 221–243.

[4] J.M. Alonso-Meijide, F. Carreras, M.G. Fiestras-Janeiro, The multilinear extension and the symmetric coalition Banzhaf value, Theory and Decision 59 (2005) 111–126.

[5] J.M. Alonso-Meijide, F. Carreras, M.A. Puente, Axiomatic characterizations of the symmetric coalitional binomial semivalues, Working Paper MA2-IR-05-00001, Department of Applied Mathematics II, Technical University of Catalonia, Spain, 2005.

[6] J.M. Alonso-Meijide, M.G. Fiestras-Janeiro, Modification of the Banzhaf value for games with a coalition structure, Annals of Operation Research 109 (2002) 213–227.

[7] R. Amer, F. Carreras, Games and cooperation indices, International Journal of Game Theory 24 (1995) 239–258.

[8] R. Amer, F. Carreras, Cooperation indices and coalition value, TOP 3 (1995) 117–135.

[9] R. Amer, F. Carreras, Power, cooperation indices and coalition structures, in: M.J. Holler, G. Owen (Eds.), Power Indices and Coalition Formation, Kluwer, 2001, pp. 153–173.

[10] R. Amer, F. Carreras, J.M. Gimenez, The modified Banzhaf value for games with a coalition structure: an axiomatic characterization, Mathematical Social Sciences 43 (2002) 45–54.

[11] R.J. Aumann, J. Drèze, Cooperative games with coalition structures, International Journal of Game Theory 3 (1974) 217–237.

[12] J.F. Banzhaf, Weighted voting doesn't work: a mathematical analysis, Rutgers Law Review 19 (1965) 317–343.

[13] R. van den Brink, G. van der Laan, A class of consistent share functions for games in coalition structure, Games and Economic Behavior 51 (2005) 193–212.

[14] F. Carreras, A. Magaña, The multilinear extension and the modified Banzhaf–Coleman index, Mathematical Social Sciences 28 (1994) 215–222.

[15] F. Carreras, A. Magaña, The multilinear extension of the quotient game, Games and Economic Behavior 18 (1997) 22–31.

[16] F. Carreras, M.A. Puente, A parametric family of mixed coalitional values, in: A. Seeger (Ed.), Recent Advances in Optimization, Lecture Notes in Economics and Mathematical Systems, Springer-Verlag, 2006, pp. 323–339.

[17] J.S. Coleman, Control of collectivities and the power of a collectivity to act, in: B. Lieberman (Ed.), Social Choice, Gordon and Breach, 1971, pp. 269–300.

[18] P. Dubey, A. Neyman, R.J. Weber, Value theory without efficiency, Mathematics of Operations Research 6 (1981) 122–128.

[19] P. Dubey, L.S. Shapley, Mathematical properties of the Banzhaf power index, Mathematics of Operations Research 4 (1979) 99–131.

[20] D.S. Felsenthal, M. Machover, Voting power measurement: a story of misreinvention, Social Choice and Welfare 25 (2005) 485–506.

[21] V. Feltkamp, Alternative axiomatic characterizations of the Shapley and Banzhaf values, International Journal of Game Theory 24 (1995) 179–186.

[22] H. Haller, Collusion properties of values, International Journal of Game Theory 23 (1994) 261–281.

[23] G. Hamiache, A new axiomatization of the Owen value for games with coalition structures, Mathematical Social Sciences 37 (1999) 281–305.

[24] S. Hart, M. Kurz, Endogeneous formation of coalitions, Econometrica 51 (1983) 1047–1064.

[25] A. Laruelle, F. Valenciano, Shapley-Shubik and Banzhaf indices revisited, Mathematics of Operations Research 26 (2001) 89–104.

[26] A. Laruelle, F. Valenciano, On the meaning of the Owen– Banzhaf coalitional value in voting situations, Theory and Decision 56 (2004) 113–123.

[27] E. Lehrer, An axiomatization of the Banzhaf value, International Journal of Game Theory 17 (1988) 89–99.

[28] M. Malawski, Equal treatment, symmetry and Banzhaf value axiomatizations, International Journal of Game Theory 31 (2002) 47–67.

[29] D. Monderer, D. Samet, Variations on the Shapley Value, in: R. Aumann, S. Hart (Eds.), Handbook of Game Theory with Economic Applications, Elsevier, 2002, pp. 2055–2076.

[30] A.S. Nowak, On an axiomatization of the Banzhaf value without the additivity axiom, International Journal of Game Theory 26 (1997) 137–141.

[31] G. Owen, Multilinear extensions of games, Management Science 18 (1972) 64–79.

[32] G. Owen, Modification of the Banzhaf-Coleman index for games with a priori unions, in: M.J. Holler (Ed.), Power, Voting and Voting Power, 1982, pp. 232–238.

[33] G. Owen, Values of games with a priori unions, in: R. Henn, O. Moeschlin (Eds.), Mathematical Economics and Game Theory, Springer, 1977, pp. 76–88.

[34] G. Owen, Characterization of the Banzhaf–Coleman index, SIAM Journal on Applied Mathematics 35 (1978) 315–327.

[35] G. Owen, Power, voting and voting power, in: M.J. Holler (Ed.), Modification of the Banzhaf–Coleman Index for Games with a Priori Unions, 1982, pp. 232–238.

[36] G. Owen, Game Theory, 3d. edition. Academic Press Inc., 1995.

[37] G. Owen, E. Winter, Multilinear extensions and the coalitional value, Games and Economic Behavior 4 (1992) 582–587.

[38] L.S. Penrose, The elementary statistics of majority voting, Journal of the Royal Statistical Society 109 (1946) 53–57.

[39] W.H. Riker, The first power index, Social Choice and Welfare 3 (1986) 293–295.

[40] A.E. Roth (Ed.), The Shapley Value: Essays in Honor of Lloyd S. Shapley, Cambridge University Press, 1988.

[41] L.S. Shapley, A value for n-person games, in: H.W. Kuhn, A.W. Tucker (Eds.), Contributions to the Theory of Games II, Princeton University Press, 1953, pp. 307–317.

[42] L.S. Shapley, M. Shubik, A method for evaluating the distribution of power in a committee system, American Political Science Review 48 (1954) 787–792.

[43] P.D. Straffin, The Shapley-Shubik and Banzhaf power indices, in: A.E. Roth (Ed.), The Shapley Value: Essays in Honor of Lloyd S. Shapley, Cambridge University Press, 1988, pp. 71–81.

[44] M. Vázquez, A. van den Nouweland, I. García-Jurado, Owen's coalitional value and aircraft landing fees, Mathematical Social Sciences 34 (1997) 273–286.

[45] R.J. Weber, Subjectivity in the valuation of games, in: O. Moeschlin, D. Pallaschke (Eds.), Game Theory and Related Topics, North-Holland, 1979, pp. 129–136.

[46] R.J. Weber, Probabilistic values for games, in: A.E. Roth (Ed.), The Shapley Value: Essays in Honor of Lloyd S. Shapley, Cambridge University Press, 1988, pp. 101–119.

[47] E. Winter, The consistency and potential for values with coalition structure, Games and Economic Behavior 4 (1992) 132–144.

[48] E. Winter, The Shapley value, in: R. Aumann, S. Hart (Eds.), Handbook of Game Theory with Economic Applications, Elsevier, 2002, pp. 2025–2054.

[49] H.P. Young, Monotonic solutions of cooperative games, International Journal of Game Theory 14 (1985) 65–72.

José María Alonso-Meijide was born in 1970 in Lalín, Spain. He received his B.S. Degree and Ph.D. in Mathematics from the University of Santiago de Compostela (Spain). He is Professor at the Department of Statistics and Operations Research of the University of Santiago de Compostela since 1997.

His research is focused on game theory and applications in the fields of politics and economics. He is the author of several papers in international journals (Annals of Operations Research, Naval Research Logistics, European Journal of Operations Research, etc.). He belongs to various research associations (GTS, SEIO, RSME, SGAPEIO).

Francesc Carreras was born in 1949 in Terrassa, Spain. He received his B.S. Degree in Mathematics from the University of Barcelona and his Ph.D. in Mathematics from the Universitat Autònoma de Barcelona. At present, he is a full professor of the Technical University of Catalonia (UPC), at the Department of Applied Mathematics II and the Industrial and Aeronautical Engineering School of Terrassa. He is the author of books on linear algebra and game theory. His research concerns game theory and related fields. He has been awarded the Operations Research Prize of the Spanish Defense Ministry in 1992 and 1995. He is leading the UPC Game Theory Research Group and the three-year Research Project “Models and Methods of Game Theory for Social and Technological Sciences”, supported by the Science and Technology Spanish Ministry and the European Regional Development Fund. He is an invited lecturer in different universities and presentations in national and international conferences and meetings. He has papers published in different journals and contributed chapters to several volumes.

María Gloria Fiestras-Janeiro was born in 1962 in Forcarei, Spain. She received her B.S. Degree and Ph.D. in Mathematics from the University of Santiago de Compostela (Spain). She is Assistant Professor of the Department of Statistics and Operations Research of the University of Vigo (Spain). Her research interests are in the field of game theory. She is the author of several papers in international journals (Annals of Operations Research, Journal of Optimization Theory and Applications, Mathematical Social Sciences, etc.). She belongs to various research associations (GTS, SEIO).

Guillermo Owen was born in 1938 in Bogota, Colombia. He obtained a B.S. Degree in Mathematics from Fordham University in 1958, and a Ph.D., also in Mathematics, from Princeton University in 1962. He has taught mathematics at Fordham University (1961–69), Rice University (1969–77) and the University of the Andes (1978–82). He is currently the Distinguished Professor of Mathematics at the Naval Postgraduate School, where he has taught since 1982.

Professor Owen has served as the associate editor of Management Science, the International Journal of Game Theory, Games and Economic Behavior, and the International Game Theory Review. He is a frequent contributor to these and other journals. Professor Owen is a member of the Royal Society of Arts and Sciences of Cataluña, of the Academy of Exact Sciences of Colombia, and of the Third World Academy of Sciences.

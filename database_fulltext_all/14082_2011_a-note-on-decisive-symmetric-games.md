---
otero_id: 14082
otero_key: "VJCRCF58"
title: "A note on decisive symmetric games"
authors: "Francesc Carreras; Josep Freixas; María Albina Puente"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.10.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A note on decisive symmetric games<sup>☆</sup>

Francesc Carreras <sup>a</sup>, Josep Freixas <sup>b</sup>, María Albina Puente <sup>b,</sup>⁎

<sup>a</sup> Department of Applied Mathematics II and Industrial and Aeronautical Engineering School of Terrassa, Universitat Politècnica de Catalunya, Spain <sup>b</sup> Department of Applied Mathematics III and Engineering School of Manresa, Universitat Politècnica de Catalunya, Spain

## a r t i c l e i n f o

Article history: Received 11 March 2009 Received in revised form 7 September 2010 Accepted 7 October 2010 Available online 27 January 2011

Keywords: Simple game Decisive symmetric game α-decisiveness

## a b s t r a c t

Binary voting systems, usually represented by simple games, constitute a main DSS topic. A crucial feature of such a system is the easiness with which a proposal can be collectively accepted, which is measured by the “decisiveness index” of the corresponding game. We study here several functions related to the decisiveness of any simple game. The analysis, including the asymptotic behavior as the number n of players increases, is restricted to decisive symmetric games and their compositions, and it is assumed that all players have a common probability p to vote for the proposal. We show that, for n large enough, a small variation, either positive or negative, in p when p=1/2 takes the decisiveness to quickly approach, respectively, 1 or 0. Moreover, we analyze the speed of the decisiveness convergence.

© 2011 Elsevier B.V. All rights reserved

## 1. Introduction

An investigation of the DSS literature reveals that research has mainly focused on the effects of design, implementation and use on decision outcomes (see e.g. [2,3,15]). In addition, it is well known that game theory has been applied to different kinds of problems concerning DSS. For instance, several studies have been conducted with concepts such as supply chain formation and supply chain coalitions (see e.g. [17,18]). Moreover, the multiple mechanisms to take decisions by voting existing in political organizations can be seen as DSS since voters must make decisions involving a choice between alternatives. Here we will assume that there are just two alternatives: either breaking the status quo or not, and this is the speci<sup>fi</sup>c decision context. We will additionally suppose that all voters play an equivalent role in the voting system at hand and that the system is “decisive”, i.e., there is no structural bias towards either breaking or not breaking the status quo.

Simple games constitute an interesting class of cooperative games. Not only as a test bed for cooperative concepts but also for the variety of their interpretations (often far from game theory). In particular, they are frequently applied to describe and analyze collective decision-making mechanisms ruled by voting.

In order to establish concepts, let us assume that a single proposal P, such as a bill or an amendment, is pitted against the status quo Q.

Each agent (player) has only two options: voting for P or voting against it and hence for maintaining the status quo. The rules must state the groups of agents (coalitions) which can pass the proposal when voting for it (such a collection of winning coalitions de<sup>fi</sup>nes a simple game in the set of agents), so that abstention is in fact allowed, but it counts for Q. Usually, each agent controls a number of votes (weight) and the proposal receives approval if, and only if, the total weight of the group of agents that vote for it meets or exceeds a given threshold (quota): we then speak of a weighted majority game. (For weighted and non-weighted simple voting rules taking abstention into account as a very third alternative, see e.g. [8–10,13,6] or, especially, [14], where symmetric games, which may be weighted and decisive, with abstention or other alternatives, are considered; for power measures to quantify the amount of in<sup>fl</sup>uence that different players have in a simple game (see e.g. [1] and/or [21]).

Parliamentary bodies provide conspicuous examples. If voting discipline within parties holds, then the agents are the parties, and each one controls the votes of all its representatives. Otherwise, each parliamentarian is an agent with one vote (symmetric or k-out-of-n game). The US Senate can be viewed in this way due to the political freedom to act that each senator enjoys. Other examples where the agents are, actually, individuals are popular juries or the Constitutional Court. As a sample of more complicated structures, the US Congress is a tricameral system (compound simple game), where the components are the President (1 member), the House of Representatives (435 members) and the Senate (101 members) and a simple majority is required in each component to pass a motion.<sup>1</sup>

In the literature, and following [22], it is said that a mechanism is “decisive” whenever, for each couple of complementary groups of agents, one and only one of them is able to pass a motion.<sup>2</sup> All components of the US Congress as well as many national and regional parliaments and town councils in more or less democratic countries are decisive in this sense since the number n of agents is odd and the threshold is $\textstyle k = { \frac { n + 1 } { 2 } }$ (the so-called straight majority). In fact, a more precise and general notion of “decisiveness” exists that will be reviewed below. Let us <sup>fi</sup>rst consider a motivating example.

Example 1.1. (Adapted from [5]) A nine-member jury has to decide whether the accused is guilty of a crime. The procedure is such that at least <sup>fi</sup>ve members must cast a non-guilty verdict for the man to be acquitted. Let us assume that the rule is legally modi<sup>fi</sup>ed in such a way that only four members are needed for a non-guilty verdict. The defendant's possibilities of freedom have of course increased but… to what extent? The answer will depend on the view held by each jury member. The details will be given in Example 3.2.

Based on a neutral probabilistic voting model for a proposal P against a given status quo Q, a structural decisiveness index, equivalent to Coleman's [7] “power of a collectivity to act”, was introduced in [5]. It applies to any simple game and measures the formal, abstract “agility” of the voting procedures represented by the game.

This index was generalized in [4] as follows. Additional information is taken into account by means of an assessment vector $\alpha { = } ( \alpha _ { 1 } , \alpha _ { 2 } ,$ $\alpha _ { n } ) \in [ 0 , 1 ] ^ { n }$ , where n is the number of players. It is assumed to provide an independent probability $\alpha _ { i }$ of each player i to vote for the proposal (and hence a probability $1 - \alpha _ { i }$ to vote against or abstain). This gives rise to a α-decisiveness index, which yields the probability of the proposal to be socially accepted under these conditions. Alternatively, the α-decisiveness index may be viewed as the probability of a random coalition to win when each player i has a probability α to belong.

Once more in order to establish concepts, one might conventionally assume that the status quo is always of a conservative nature whereas the proposals are progressive.<sup>3</sup> In that case an assessment value α would be considered conservative if $0 { \le } { \alpha } _ { i } { < } 1 / 2$ , neutral if $\alpha _ { i } = 1 / 2 ,$ , and progressive if $1 / 2 < \alpha _ { i } \leq 1$

In this paper we will restrict the analysis to decisive symmetric games (i.e. k-out-of-n games with n odd and $\begin{array} { r } { k = \frac { n + 1 } { 2 } ) } \end{array}$ and assume that all players have a common inclination to vote for the proposal (that is, $\alpha _ { i } = p$ for some $p \in [ 0 , 1 ]$ and all i). Although these are strong restrictions, it seems obvious that this is a necessary first step (cf. Section 6 for a further research program). Moreover, due to the continuity of the functions involved, the results might well be extended to cases where the equality does not hold but $\alpha _ { 1 } , \alpha _ { 2 } , . . . ,$ $\alpha _ { n }$ are close enough to each other (see also suggestion B in Section 6).

We will study the variation of the decisiveness of the game under two main hypotheses: (i) the players' common inclination $p { > } 1 / 2$ to vote for a proposal slightly increases; (ii) the number of involved players increases. We will also compare the decisiveness of the game with the common assessment p. The analysis done in this paper is relevant to decision making situations in which the status quo may be altered by a new proposal that is submitted to the collective decision. The knowledge of both n and p allows us to estimate the exact probability of the proposal to be passed and thus estimating what could <sup>fi</sup>nally happen. Our study has signi<sup>fi</sup>cance for statistical, forecast and marketing purposes. If someone is interested in in<sup>fl</sup>uencing the outcome then the knowledge of the decisiveness could help him to decide whether to implement actions with the purpose of increasing or decreasing the value of p to affect the collective decision in the desired sense.

Example 1.2. Let us assume that a mid-company wishes to change the current incentive scheme for workers. Each worker has to choose between two different possibilities: either adopting the new one (option 1) or keeping the current one (option 2). The option which receives more votes will be adopted and abstention is counted for option 2. The owners of the company, who are not indifferent to the two options, wish to in<sup>fl</sup>uence the opinion of the workers before they vote. With this purpose, the owners will present the issue at stake from a viewpoint favorable at most to the company's interests, option 1.

Of course, many more similar examples can be found where an in<sup>fl</sup>uencing leader asks the members of his organization to take a decision on some subject directly concerning the organization as such. A conspicuous example is a government that wishes to call a referendum on a topic of national interest like e.g. the possibility of joining (or leaving) an international alliance or organization, a unilateral declaration of independence in the case of a region with a strong nationalism, or any other question of this kind. In this case it is well known the strong in<sup>fl</sup>uence that mass media (press, TV, radio, internet…) can exert on the public opinion in topics far from the daily life, but also the capability of any government, in general, to press some of these media to presenting the issue at stake from a viewpoint favorable at most to the government's interests.

The voters' assessment on the proposal, as well as the variation of this assessment with the time, can be determined by means of opinion polls made by specialized data treatment enterprises with a great deal of experience in this <sup>fi</sup>eld. Also a forecast about abstention can be obtained this way.

Therefore, by assuming that the arithmetic mean of this predisposition is measured by a parameter $p \in [ 0 , 1 ]$ , understood as the probability that a typical voter votes for option 1 in the voting procedure, the successive opinion polls will provide the evolution of p along the time before the voting and especially after each company's action to promote its preferred option.

Our results guarantee that, with this information in hand, the company will know when, how much, and which way, efforts should be addressed to modify the value of p by means of new interventions in<sup>fl</sup>uencing the audience.

More precisely, let us assume that the predictable number of voting workers (we assume that this number is odd) $\mathrm { i } s n = 1 , 0 0 1$ , option 1 will be achieved only if at least 50% of active voters vote for, and that in a given moment the predisposition mean is e.g. $\scriptstyle p = 0 . 4 9 1 5$ or $\begin{array} { r } { p = 0 . 5 0 2 0 . } \end{array}$ Then, our model applies with $k = 5 0 1$ . Our results will give, e.g., the value of p that gives rise to a decisiveness of, say, 0.6, a “security level” in order to be almost sure that option 1 will pass. Which would be this security level for different values of n? (For details see Example 4.4).

The organization of the paper is as follows. After a short Section 2 on preliminaries where we recall several basic notions, in Section 3 we introduce three functions: decisiveness, aggregate (difference) and enlargement (difference). They are analyzed in Section 4: Theorem 4.1 establishes some mathematical properties of these functions, and their asymptotic behavior is described in Theorem 4.2. In Section 5 we extend some results to games that are compositions of decisive symmetric games. The conclusions are stated in Section 6. The proofs are outlined in the Appendix.

## 2. Preliminaries

A (monotonic) simple game is a pair (N, W) where $N = \{ 1 , 2 , . . . , n \}$ denotes a <sup>fi</sup>nite set of players and W is a collection of coalitions (subsets of N) that satis<sup>fi</sup>es the following properties: $( \mathrm { i } ) \ 0 \not \in W ; ( \mathrm { i i } )$ if $S { \in } W$ and $S { \subset } T { \subseteq } N$ then $T \in W$ (monotonicity). A coalition S is winning if $S { \in } W ,$ and losing otherwise. A simple game (N, W) is called decisive whenever $S \in W \operatorname { i f } ,$ and only if, N\S∉W for each $S \subseteq N .$

A simple game $( N , W )$ is a weighted majority game if a quota qN0 and weights $w _ { 1 } , w _ { 2 } , . . . , w _ { n } { \geq } 0$ exist such that $S { \in } W$ if, and only if, $\sum { } _ { i \in S } w _ { i } \geq q .$ . We then write $( N , W ) \equiv [ q ; w _ { 1 } , w _ { 2 } , . . . , w _ { n } ]$ and call to this a representation of (N, W).

In particular, $( N , W )$ is a symmetric or k-out-of-n game<sup>4</sup> if it admits a representation of the form

$$
(N, W) \equiv [ k; \overbrace {1 , \dots , 1} ^ {n} ]
$$

for an integer k such that $1 \leq k \leq n$ . It readily follows that a symmetric game $( N , W )$ is decisive if, and only if, n is odd and $\begin{array} { r } { k = \frac { n + \mathrm { ~ i ~ } } { 2 } . } \end{array}$ . Hence a decisive symmetric game is completely determined by the quota $k ,$ so that later on we will merely refer to k, since $n = 2 k - 1$

Let (N, W) be a simple game and $\alpha { = } ( \alpha _ { 1 } , \alpha _ { 2 } , . . . , \alpha _ { n } ) { \in } [ 0 , 1 ] ^ { n }$ be an assessment vector. The α-decisiveness of (N, W) was de<sup>fi</sup>ned in [4] as

$$
\delta (N, W, \alpha) = \sum_ {S \in W} \prod_ {i \in S} \alpha_ {i} \prod_ {j \in N \setminus S} \Bigl (1 - \alpha_ {j} \Bigr).\tag{1}
$$

Using the multilinear extension ([20], [19]) of game (N, W), given by

$$
f (x _ {1}, x _ {2}, \dots , x _ {n}) = \sum_ {S \in W} \prod_ {i \in S} x _ {i} \prod_ {j \in N \setminus S} \left(1 - x _ {j}\right),
$$

it follows that $\delta ( N , \ W , \ \alpha ) { = } f ( \alpha _ { 1 } , \ \alpha _ { 2 } , \ . . . , \ \alpha _ { n } )$ for all (N, W) and all $\alpha \in [ 0 , 1 ] ^ { n }$ . (Several boundaries for the multilinear extension, and hence for the α-decisiveness, are proposed in [11]).

By setting $\alpha { = } ( 1 / 2 , 1 / 2 , . . . , 1 / 2 )$ we get the structural decisiveness<sup>5</sup>, de<sup>fi</sup>ned in[5] as

$$
\delta (N, W) = \frac {| W |}{2 ^ {n}}.
$$

## 3. Decisiveness and related functions

We will study a particular case where (N, W) is symmetric and $\alpha { = } ( p , p , . . . , p )$ for some $p \in [ 0 , 1 ]$ . We will then consider the α- n decisiveness of a symmetric game $( N , W ) { \equiv } [ k ; \overbrace { 1 , . . . , 1 } ]$ , simply called <sup>ð Þ ½</sup>decisiveness in the sequel and given, using Eq. (1), by

$$
f _ {n, k} (p) = \sum_ {i = k} ^ {n} \binom {n} {i} p ^ {i} (1 - p) ^ {n - i} \quad \text { for   all } \quad p \in [ 0, 1 ].\tag{2}
$$

It is not dif<sup>fi</sup>cult to see that the decisiveness of a symmetric game is improved when the number of players increases from n $\tan { n + 1 }$ while the quota k does not vary. However, when passing from a k-out-of-n game to $\texttt { a } ( k + 1 ) - \mathtt { o u t - o f - } ( n + 1 )$ game, that is, when increasing simultaneously the number n of players and the quota k, the opposite result is obtained, as is shown in the next statement. For completeness, it also includes the case where the quota increases from k to $k + 1$ and the number n of players remains unchanged.

Lemma 3.1. Let $( N , W ) { \equiv } [ k ; \overbrace { 1 , . . . , 1 } ^ { n } ]$ be a symmetric game with decisiveness $f _ { n , \ k } ( p )$ <sup>ð Þ ½</sup>. Then, for all $p { \in } [ 0 , 1 ] .$

$$
(a) f _ {n + 1, k} (p) - f _ {n, k} (p) = \binom {n} {k - 1} p ^ {k} (1 - p) ^ {n - k + 1}.\tag{b}
$$

$$
f _ {n, k + 1} (p) - f _ {n, k} (p) = - \binom {n} {k} p ^ {k} (1 - p) ^ {n - k} (\text { for } k <   n).
$$

$$
(c) f _ {n + 1, k + 1} (p) - f _ {n, k} (p) = - \binom {n} {k} p ^ {k} (1 - p) ^ {n - k + 1}.
$$

Example 3.2. (Example 1.1 revisited) Three simple cases will be considered here, as a sample for many other additional options. We will apply Lemma $3 . 1 ( \mathsf { b } )$

(i) If the jury members are not inclined toward any particular verdict, that is, if a probability of $1 / 2$ to vote for acquittance is attached to each, then the defendant's probability of getting freedom changes from 0.5000 to 0.7461 when the decision rule demands four non-guilty votes only: an increase of almost 50%. These values correspond to the structural decisiveness.

(ii) If the jury members are inclined toward a guilty verdict and a common probability of, say, 0.4 to choose acquittance is attached to each, then the probability of getting freedom changes from 0.2666 to 0.5174: an increase of 94%.

(iii) If the jury members are clearly inclined toward acquittance and a common probability of 0.8 to cast a non-guilty verdict is attached to each, then the probability of getting freedom changes from 0.9804 to 0.9969: about 1.68% more.

The values obtained in (ii) and (iii) correspond to other particular cases of the general α-decisiveness. Although for any probability $p \in ( 0 , 1 )$ the probability of getting freedom increases when reducing the quota from 5 to 4, the absolute and relative differences are quite different from one case to another.

The differences obtained in Lemma 3.1 do not show a uniform sign. From now on we con<sup>fi</sup>ne our analysis to decisive symmetric games, and begin by raising the following question: does a decisive symmetric game with “many” players show always more (or always less) decisiveness than another with “few” players? Intuitively, one might feel that a game with many players should possess less decisiveness than another with few players, because it seems more dif<sup>fi</sup>cult to get an agreement (to form a winning coalition) in the former case than in the latter.

However by using structural decisiveness (for which $p { = } 1 / 2 )$ this intuitive assumption is proven wrong, since it yields 1/2 for all decisive games. In Lemma 3.3 we state the variation of the decisiveness of a decisive symmetric game when passing from 2k−1 to 2k+1 players and show that its sign depends on p. Notice that, according to Eq. (2), the decisiveness of a k-out-of-(2k−1) game is given by

$$
f _ {2 k - 1, k} (p) = \sum_ {i = k} ^ {2 k - 1} \binom {2 k - 1} {i} p ^ {i} (1 - p) ^ {2 k - 1 - i} \quad \text {   for   all   } \quad p \in [ 0, 1 ].
$$

Lemma 3.3. If $\left[ k ; 1 , \ 1 , \ . . . , \ 1 \right]$ and $\left[ k + 1 ; 1 , ~ 1 , ~ . . . , ~ 1 \right]$ are decisive symmetric games with $2 k - 1$ and $2 k + 1$ players, respectively, then

$$
f _ {2 k + 1, k + 1} (p) - f _ {2 k - 1, k} (p) = \binom {2 k - 1} {k} p ^ {k} (1 - p) ^ {k} (2 p - 1) \qquad \text {   for   all   } \quad p \in [ 0, 1 ].
$$

Therefore it is clear that the decisiveness of the game with more players is greater if, and only if, $1 / 2 { < } p { < } 1$ . In other words, the decisiveness of decisive symmetric games is an increasing function of the number of players if $p { \in } ( 1 / 2 , 1 )$ , and a decreasing function if $p \in ( 0 , 1 / 2 )$

In the sequel we will denote the decisiveness function $f _ { 2 k - 1 , k } ( p )$ simply as $f _ { 2 k - 1 } ( p )$ . Two more functions that will be analyzed are introduced below. The former compares the decisiveness of the game (a sort of “aggregate assessment”) with the assessment value p common to all players. The latter describes the variation of decisiveness when the quota increases by one unit and, correspondingly, the number of players is enlarged by two units.

De<sup>fi</sup>nition 3.4. The aggregate (difference) function is given by

$$
G _ {2 k - 1} (p) = f _ {2 k - 1} (p) - p \quad \text {   for   all   } \quad p \in [ 0, 1 ].
$$

De<sup>fi</sup>nition 3.5. The enlargement (difference) function is given by

$$
\Delta_ {2 k - 1} (p) = f _ {2 k + 1} (p) - f _ {2 k - 1} (p) \quad \text {   for   all   } \quad p \in [ 0, 1 ].
$$

Notice that, according to Lemma 3.3,

$$
\Delta_ {2 k - 1} (p) = \binom {2 k - 1} {k} p ^ {k} (1 - p) ^ {k} (2 p - 1) \quad \text { for   all } \quad p \in [ 0, 1 ].
$$

## 4. Main results

4.1. Behavior of the decisiveness, aggregate and enlargement functions

We state here the basic properties of the decisiveness function $f _ { 2 k - 1 } ( p )$ , the aggregate function $G _ { 2 k - 1 } ( p )$ , and the enlargement function $\Delta _ { 2 k - 1 } ( p )$ ).

Theorem 4.1. Let k≥2.

Part A. The decisiveness function $f _ { 2 k - 1 } ( p )$ satisfies the following properties (see Fig. 1):

(A1) f<sub>2k 1</sub>(1 − p) = 1 − f<sub>2k 1</sub>(p) for all p ∈ [0,1].

(A2) $f _ { 2 k - 1 } ( p )$ is an increasing function on [0,1].

(A3) $f _ { 2 k - 1 } ( p )$ is convex on the interval [0,1/2] and concave on [1/2,1], so that its only inflection point is at $p = 1 / 2$ and its unique fixed points are $p { = } 0 , 1 / 2 , 1$

Part B. The aggregate function $G _ { 2 k - 1 } ( p )$ satisfies the following properties (see Fig. 2):

(B1) $G _ { 2 k - 1 } ( 1 - p ) = - G _ { 2 k - 1 } ( p ) f o r a l l p \in [ 0 , 1 ] .$

(B2) The only roots of ${ \bf \dot { G } } _ { 2 k - 1 } ( p )$ are $\begin{array} { r } { p = 0 , 1 / 2 , } \end{array}$ 1.

(B3) Let p and p $b e 1 / 2 { \pm } \sqrt { 1 { - } 4 \beta } / 2$ , respectively, where $\beta = \left\lceil k \binom { 2 k - 1 } { k } \right\rceil ^ { \frac { 1 } { 1 - 1 } }$ . Then $G _ { 2 k - 1 } ( p )$ is an increasing function on [p<sub>m</sub>, p<sub>M</sub>] and a decreasing function on each of the portions [0, $p _ { m } ]$ and [p<sub>M</sub>, 1], and attains over [0,1] its unique absolute maximum at point $p = p _ { M }$ and its unique absolute minimum at point $\begin{array} { r } { p = p _ { m } . } \end{array}$

(B4) $G _ { 2 k - 1 } ( p )$ is convex on [0,1/2] and concave on [1/2,1], with a unique inflection point at $p { = } 1 / 2 .$

![](/api/attachments/VJCRCF58/fulltext/images/93887f2ceb710a09cd465670befae50a9e00920a8210fa70076619af27134032.jpg)  
Fig. 1. The graph of $f _ { 2 k - 1 } ( p ) .$

Part C. The enlargement function $\Delta _ { 2 k - 1 } ( p )$ satisfies the following properties (see Fig. 3):

(C1) $\Delta _ { 2 k - 1 } ( 1 - p ) = - \Delta _ { 2 k - 1 } ( p )$ for all $p \in [ 0 , 1 ]$

(C2) The only roots o $\stackrel { \triangledown } { { \cal { f } } } \Delta _ { 2 k - 1 } ( p ) \ a r e \ p = 0 , 1 / 2 , 1 .$

(C3) Let $p _ { M } ^ { \prime }$ and $p _ { m } ^ { \prime }$ be $1 / 2 { \pm } 1 / 2 \sqrt { 2 k + 1 }$ , respectively. Then $\Delta _ { 2 k - 1 }$ (p) is an increasing function on [p′ , p′ ] and a decreasing function on each of the portions $[ 0 , p _ { m } ^ { \prime } ]$ and [p′ , 1], and attains over [0,1] its unique absolute maximum at point $p = p _ { M } ^ { \prime }$ and its unique absolute minimum at point $p = p _ { m } ^ { \prime }$

(C4) Let $p _ { 2 }$ and $p _ { 1 }$ be $1 / 2 \pm { \sqrt { 3 } } / 2 { \sqrt { 2 k + 1 } } ,$ , respectively. Then $\Delta _ { 2 k - 1 }$ (p) is convex on each of the portions $[ p _ { 1 } , 1 / 2 ]$ and $[ p _ { 2 } , 1 ]$ and concave on each of the portions $\left[ 0 , \ p _ { 1 } \right]$ and $[ 1 / 2 , p _ { 2 } ]$ , and its inflection points are at $\begin{array} { r } { p = p _ { 1 } , 1 / 2 , p _ { 2 } . } \end{array}$

Finally, at $\cdot p = 1 / 2$ there is a symmetry center for the graphs of $f _ { 2 k }$ 1 $( p ) , G _ { 2 k - 1 } ( p )$ and $\Delta _ { 2 k - 1 } ( p )$ .

4.2. Asymptotic behavior

Now we study the asymptotic behavior of the decisiveness and aggregate functions. As will be seen, the sequences of continuous functions considered here admit pointwise limit. However, a singularity at $p { = } 1 / 2$ prevents uniform convergence. It follows that games with high decisiveness arise when the players' common assessment p is above 1/2.

Theorem 4.2. (i) Let $F ( p )$ be the pointwise limit of the sequence $\{ f _ { 2 k - 1 }$ $( p ) \} _ { k \in N }$ Then (see Fig. 4)

$$
F (p) = \left\{ \begin{array}{l l} 0 & \text {   if   } p <   1 / 2, \\ 1 / 2 & \text {   if   } p = 1 / 2, \\ 1 & \text {   if   } p > 1 / 2. \end{array} \right.
$$

![](/api/attachments/VJCRCF58/fulltext/images/cb21ce4340a76ee0c6a1f96f9ab0ef5bea354b6c96c196acc0467ff1a71258da.jpg)  
Fig. 2. The graph of $G _ { 2 k - 1 } ( p ) .$

![](/api/attachments/VJCRCF58/fulltext/images/93db3d647218b8acc8126794998ea65049709576cf8275ecc4b8a3233d037818.jpg)  
Fig. 3. The graph of $\varDelta _ { 2 k }$ <sub>− 1</sub>(p).

(ii) Let g(p) be the pointwise limit of the sequence $\{ G _ { 2 k - 1 } ( p ) \} _ { k \in N } .$ Then (see Fig. 5)

$$
g (p) = \left\{ \begin{array}{l l} - p & \text {if} \quad p <   1 / 2, \\ 0 & \text {if} \quad p = 1 / 2, \\ 1 - p & \text {if} \quad p > 1 / 2. \end{array} \right.
$$

Remark 4.3. If we de<sup>fi</sup>ne $\delta ( p )$ as the pointwise limit of the sequence $\{ \Delta _ { 2 k - 1 } ( p ) \} _ { k \in N }$ then by Theorem $4 . 2 ( \mathrm { i } )$ it follows that $\delta \equiv 0 .$ . This explains why we did not mention this third limit function at the beginning of this subsection.

## 4.3. Some comments

From Theorem 4.1 and Theorem 4.2 some conclusions can be derived. Part A of Theorem 4.1 states that $f _ { 2 k - 1 } ( p )$ is an increasing function and, as $p { = } 1 / 2$ is the unique in<sup>fl</sup>ection point, $f _ { 2 k - 1 } ( p ) - { \mathrm { t h e } }$ slope of the curve – attains its maximum value at $p { = } 1 / 2 .$ . Thus, if initially $p { = } 1 / 2$ is assumed but for some reason this players' assessment is slightly increased, then the game decisiveness passes from $1 / 2$ to a considerably higher level (see Table 1).

Furthermore, part (i) of Theorem 4.2 indicates that if the common assessment p is improved from 1/2 then the game decisiveness tends to 1 whenever the number of players increases. Notice that

$$
\lim _ {k \to + \infty} f _ {2 k - 1} ^ {\prime} (1 / 2) = \lim _ {k \to + \infty} k \binom {2 k - 1} {k} \left(\frac {1}{4}\right) ^ {k - 1} = + \infty ,
$$

$$
f _ {2 k - 1} (p) \text {   at   } p = 1 / 2
$$

$$
\mathrm{to} + \infty .
$$

i.e. the slope of f (p) at p=1/2 tends to +∞. From the variation o ${ \bf \dot { G } } _ { 2 k - 1 } ( p )$ and the fact that $G _ { 2 k - 1 } ( 0 ) = G _ { 2 k }$ −1 $( 1 / 2 ) = G _ { 2 k - 1 } ( 1 ) = 0 ,$ , Part B of Theorem 4.1 states that the decisiveness of the game is greater than the players' assessment $\mathrm { i f } 1 / 2 { < } p { < } 1$ and lower if $0 { < } p { < } 1 / 2$ (see Table 2).The most appreciable difference between game decisiveness and the players' assessment is attained at $p _ { M } .$ Moreover, as

$$
\lim _ {k \to \infty} \left[ k \binom {2 k - 1} {k} \right] ^ {\frac {1}{1 - k}} = 1 / 4,
$$

![](/api/attachments/VJCRCF58/fulltext/images/14752c87d28d153e2087bd4579dc020d0b6f3d4e9cacb8388e9f49ad29fb8967.jpg)  
Fig. 4. The graph of F(p).

![](/api/attachments/VJCRCF58/fulltext/images/d5702355e5c588ba64b3f41556a5647f885bd5704962457f435709f0c3a9a78d.jpg)  
Fig. 5. The graph of g(p).

$p _ { M }$ tends to $1 / 2$ when k is large and, according to part (i) of Theorem 4.2 $f _ { 2 k - 1 } ( { p } _ { M } )$ tends to 1 and the aggregate function at this point tends to $1 / 2$ (see Table 3 for values of k and $p _ { M } )$

Finally, Part C of Theorem 4.1 says that, when the number of players increases, the game decisiveness increases ${ \mathrm { i f } } ,$ and only if, $p { > } 1 / 2$ Moreover, when k tends to in<sup>fi</sup>nity $p ^ { \prime } u$ tends to 1/2 and, according to part (i) of Theorem 4.2, the decisiveness of the game at this point tends to 1 (see values in Table 4).

Theorem 4.2 gives an asymptotic result useful to easily estimate the decisiveness or aggregate functions whenever the estimated value of p is known. However, in practice the value of k is <sup>fi</sup>xed and known, whereas p needs to be estimated and vary as a function of the time before the election takes place. The anticipation of the allowable result in the election is in some circumstances very valuable: to this end one may construct tables analogous to our Tables 1, 2, 3 and 4 in order to make precise predictions on the decisiveness and the aggregate function as a function of the estimated value $p .$ This information constitutes the knowledge basis of the DSS in order to forecast what could happen in the election. It is clear that, prior to the election, either parties or collectives supporting each decision will act to improve the value of p in the desired sense.

To sum up, in order to get a high level of decisiveness in a large decisive symmetric game it is extremely important that the players assessment remains above $1 / 2 .$

Behavior of $f _ { 2 k - 1 } ( p )$ for p close to 1/2 and different values of k.

<table><tr><td>k</td><td> $f_{2k-1}(0.55)$ </td><td> $f_{2k-1}(0.6)$ </td></tr><tr><td>2</td><td>0.5748</td><td>0.6480</td></tr><tr><td>3</td><td>0.5931</td><td>0.6826</td></tr><tr><td>10</td><td>0.6710</td><td>0.8139</td></tr><tr><td>20</td><td>0.7357</td><td>0.8979</td></tr><tr><td>40</td><td>0.8143</td><td>0.9642</td></tr><tr><td>100</td><td>0.9216</td><td>0.9978</td></tr></table>

Behavior $\ O \cot f _ { 2 k - 1 } ( p )$ and $G _ { 2 k - 1 } ( p )$ for $k = 1 0$ and different values of p

<table><tr><td>p</td><td> $f_{2k-1}(p)$ </td><td> $G_{2k-1}(p)$ </td></tr><tr><td>0.3</td><td>0.0326</td><td>-0.2674</td></tr><tr><td>0.4</td><td>0.1861</td><td>-0.2139</td></tr><tr><td>0.5</td><td>0.5000</td><td>0.0000</td></tr><tr><td>0.6</td><td>0.8139</td><td>0.2139</td></tr><tr><td>0.7</td><td>0.9674</td><td>0.2674</td></tr></table>

Maximum values of $G _ { 2 k - 1 } ( p )$ and corresponding value of decisiveness.

<table><tr><td>k</td><td> $p_M$ </td><td> $f_{2k-1}(p_M)$ </td><td> $G_{2k-1}(p_M)$ </td></tr><tr><td>2</td><td>0.7887</td><td>0.8849</td><td>0.0962</td></tr><tr><td>3</td><td>0.7597</td><td>0.9063</td><td>0.1467</td></tr><tr><td>4</td><td>0.7396</td><td>0.9194</td><td>0.1798</td></tr><tr><td>5</td><td>0.7245</td><td>0.9284</td><td>0.2039</td></tr><tr><td>20</td><td>0.6426</td><td>0.9664</td><td>0.3239</td></tr><tr><td>50</td><td>0.6018</td><td>0.9799</td><td>0.3781</td></tr><tr><td>60</td><td>0.5950</td><td>0.9819</td><td>0.3870</td></tr></table>

Example 4.4. (Example 1.2 revisited) In the next table we compute a “security level” to pass option 1, i.e. the value of p such that $f _ { 2 k - 1 } ( p ) =$ 0.6 for different values of k. Thus, we can compare the different results obtained by companies of different sizes, e.g. between 101 and 1001 workers. We observe that for $n { = } 1 , 0 0 1$ workers a value of p of 0.50427 is enough to almost “guarantee” that option 1 will be adopted, while for $n { = } 1 0 1$ a considerable greater value of p is needed (0.51257). It is also relevant to note (see Table 5.) that as soon as k increases the critical value of p decreases very slowly.

For government referendums or similar situations in multinational companies (with much more than 1, 000 workers) this “security level” will be greater than 0, 5 but extremely close to it, so that a reliable prediction greater than 0, 5 will guarantee the result of the voting in the desired direction.

## 5. Composition of decisive symmetric games

Here we present an extension of the preceding results to the case where a game is made up of several decisive symmetric games. We <sup>fi</sup>rst state formally the procedure to obtain a composition of m $( \geq 2 )$ symmetric component games by using a symmetric quotient game. This composition is a particular case of the compound simple game notion introduced in [23].

De<sup>fi</sup>nition 5.1. Let (N, W) be a game that admits a partition $\{ N _ { 1 } , N _ { 2 } ,$ $\ldots , N _ { m } \}$ of N and let $M = \{ 1 , 2 , . . . , m \}$ and $n _ { j } = | N _ { j } |$ for each j∈M. Assume that integer numbers k, $k _ { 1 } , k _ { 2 } , . . . , k _ { m } { \geq } 1$ exist, with $k \leq m$ and $k _ { j } \leq n _ { j }$ for each $j \in M ,$ in such a way that

$$
W = \{S \subseteq N: | I _ {S} | \geq k \},
$$

where $I _ { S } = \{ j \in M : | S \cap N _ { j } | \geq k _ { j } \}$ for each $S \subseteq N .$ We will say that (N, W) is a k-out-of-m compound game. This is the result of linking, by means of the k-out-of-m game in $M ,$ the $k _ { j } -$ out-of-n component games de<sup>fi</sup>ned in each N<sub>j</sub>.

Table 4 Maximum values of $\Delta _ { 2 k - 1 } ( p )$ and corresponding values of decisiveness.

<table><tr><td>k</td><td> $p_M'$ </td><td> $f_{2k-1}(p_M')$ </td><td> $f_{2k+1}(p_M')$ </td><td> $\Delta_{2k-1}(p_M')$ </td></tr><tr><td>2</td><td>0.7236</td><td>0.8130</td><td>0.8667</td><td>0.0537</td></tr><tr><td>3</td><td>0.6890</td><td>0.8220</td><td>0.8592</td><td>0.0372</td></tr><tr><td>4</td><td>0.6666</td><td>0.8267</td><td>0.8551</td><td>0.0284</td></tr><tr><td>5</td><td>0.6507</td><td>0.8295</td><td>0.8526</td><td>0.0231</td></tr><tr><td>6</td><td>0.6387</td><td>0.8315</td><td>0.8509</td><td>0.0194</td></tr><tr><td>20</td><td>0.5781</td><td>0.8383</td><td>0.8443</td><td>0.0060</td></tr><tr><td>50</td><td>0.5493</td><td>0.8402</td><td>0.8425</td><td>0.0023</td></tr><tr><td>100</td><td>0.5327</td><td>0.8407</td><td>0.8419</td><td>0.0012</td></tr></table>

Value of p when $f _ { 2 k - 1 } ( p ) = 0 . 6$ for different values of k.

<table><tr><td>k</td><td>p</td></tr><tr><td>51</td><td>0.51257</td></tr><tr><td>101</td><td>0.50892</td></tr><tr><td>201</td><td>0.50632</td></tr><tr><td>301</td><td>0.50516</td></tr><tr><td>401</td><td>0.50447</td></tr><tr><td>501</td><td>0.50427</td></tr></table>

Fig. 6 illustrates this de<sup>fi</sup>nition with a numerical example. Five decisive $k _ { j } – 0 \mathsf { u t } – 0 \mathsf { f } – n _ { j }$ games are combined by means of a 3-out-of-5 quotient game, giving rise to a compound game with n=19 players. E.g., coalition S consisting of starred players is a winning coalition in this game because the columns where it yields winning coalitions (component games 1, 3 and 5) form a winning coalition in the quotient game.

It is easy to see that the decisiveness of a compound game (N, W) is given by

$$
f _ {n _ {1}, k _ {1}; \dots ; n _ {m}, k _ {m}} ^ {k - o u t - o f - m} (p) = \sum_ {R \subseteq M: | R | \geq k} \prod_ {j \in R} f _ {n _ {j}, k _ {j}} (p) \prod_ {j \in M \setminus R} \left[ 1 - f _ {n _ {j}, k _ {j}} (p) \right].
$$

Remark 5.2. (i) If, moreover, all component games are decisive then, according to the notation used in Section 4, the decisiveness of $( N , W )$ is given by

$$
f _ {2 k _ {1} - 1, \dots , 2 k _ {m} - 1} ^ {k - o u t - o f - m} (p) = \sum_ {R \subseteq M: | R | \geq k} \prod_ {j \in R} f _ {2 k _ {j} - 1} (p) \prod_ {j \in M \backslash R} \left[ 1 - f _ {2 k _ {j} - 1} (p) \right].
$$

(ii) The decisiveness of such a compound game (N, W) can be calculated in terms of the decisiveness of games studied in Section 4. (iii) If $k = m$ then

$$
W = \left\{S \subseteq N: | S \cap N _ {j} | \geq k _ {j} \text {   for   all   } j = 1, 2,..., m \right\}
$$

and we say that (N, W) is a composition via unanimity of m decisive 2k −1

symmetric games $[ k _ { j } ; \overbrace { 1 , . . . , 1 } ]$ (see [12]). In this case, the decisiveness is given by

$$
f _ {2 k _ {1} - 1, \ldots , 2 k _ {m} - 1} ^ {m - u n a n i m i t y} (p) = \prod_ {j = 1} ^ {m} f _ {2 k _ {j} - 1} (p).
$$

(iv) If k = 1 then

$$
W = \left\{S \subseteq N: | S \cap N _ {j} | \geq k _ {j} \text {   for   some   } j \right\}
$$

and we say that (N, W) is a composition via individualism of m decisive 2k −1

symmetric games $\lbrack k _ { j } ; \overbrace { 1 , . . . , 1 } ] \mathrm { ; }$ : it is the dual $\mathtt { g a m e } ^ { 6 }$ of the compound game obtained in $( \mathrm { i i i } ) ( s e e [ 1 2 ] )$ . In this case, the decisiveness is given by

$$
f _ {2 k _ {1} - 1, \dots , 2 k _ {m} - 1} ^ {m - i n d i v i d u a l i s m} (p) = 1 - \prod_ {j = 1} ^ {m} \left[ 1 - f _ {2 k _ {j} - 1} (p) \right].
$$

Let us <sup>fi</sup>nally assume that the m decisive symmetric games have the same number of players, i.e. $k _ { j } = k \mathrm { f o r } j = 1 , . . . , m$ . Tables 5 and 6 give the decisiveness of the compound game via unanimity and individualism, respectively, for $p { = } 0 . 5 5$ and different values of k and m.

Remark 5.3. (i) Similarly as we did in Section $^ { 4 , }$ we may consider the sequence

$$
\left\{f _ {2 k _ {1} - 1, \dots , 2 k _ {m} - 1} ^ {k - o u t - o f - m} (p) \right\} _ {(k _ {1}, \dots , k _ {m}) \in \mathbb {N} ^ {m}}
$$

![](/api/attachments/VJCRCF58/fulltext/images/608f7231224826a736891449ce5c63428b5c8a26bd48a7d0bdd85badb18cb154.jpg)  
Fig. 6. A compound game.

and its pointwise limit $F ^ { k - o u t - o f - m } ( p )$ when all k tend to in<sup>fi</sup>nity. By applying Theorem 4.2(i) we obtain

$$
F ^ {k - o u t - o f - m} (p) = \left\{ \begin{array}{l l} 0 & \text { if } \quad p <   1 / 2, \\ 2 ^ {- m} \sum_ {r = k} ^ {m} \binom {m} {r} & \text { if } \quad p = 1 / 2, \\ 1 & \text { if } \quad p > 1 / 2. \end{array} \right.
$$

Notice that if $m = 2 k - 1$ , that is, if the quotient game is decisive, it follows that $f _ { 2 k _ { 1 } - 1 , ~ . . . , 2 k m - 1 } ^ { k - o u t - o f - ( 2 k - 1 ) } ( 1 / 2 ) { = } 1 / 2$ and we obtain

$$
F ^ {k - o u t - o f - (2 k - 1)} (p) = \left\{ \begin{array}{l l} 0 & \text { if } \quad p <   1 / 2, \\ 1 / 2 & \text { if } \quad p = 1 / 2, \\ 1 & \text { if } \quad p > 1 / 2. \end{array} \right.
$$

(ii) In particular, if we consider the sequences

$$
\begin{array}{l l} \left\{f _ {2 k _ {1} - 1, \ldots , 2 k _ {m} - 1} ^ {m - u n a n i m i t y} (p) \right\} _ {(k _ {1}, \ldots , k _ {m}) \in \mathbb {N} ^ {m}} & \text { and } \\ \left\{f _ {2 k _ {1} - 1, \ldots , 2 k _ {m} - 1} ^ {m - i n d i v i d u a l i s m} (p) \right\} _ {(k _ {1}, \ldots , k _ {m}) \in \mathbb {N} ^ {m}} \end{array}
$$

their pointwise limits are given by

$$
F ^ {m - u n a n i m i t y} (p) = \left\{ \begin{array}{l l} 0 & \text { if } \quad p <   1 / 2, \\ (1 / 2) ^ {m} & \text { if } \quad p = 1 / 2, \\ 1 & \text { if } \quad p > 1 / 2, \end{array} \right.
$$

and

$$
F ^ {m - i n d i v i d u a l i s m} (p) = \left\{ \begin{array}{l l} 0 & \text { if } \quad p <   1 / 2, \\ 1 - (1 / 2) ^ {m} & \text { if } \quad p = 1 / 2, \\ 1 & \text { if } \quad p > 1 / 2. \end{array} \right.
$$

Taking into account the expressions of these preceding limit functions, we can deduce that the asymptotic properties stated in Section 4 for symmetric decisive games also hold for the models studied in this section. As a consequence of this asymptotic behavior it follows that, for the four kinds of models analyzed in the paper, games with a high decisiveness arise whenever the players' common assessment p remains above 1/2. On the contrary, if this common assessment fails to reach a level greater than 1/2 then game decisiveness will be greatly damaged. However, in practice, as we have shown in Section 4, the value of p is not known and it needs to be estimated. In this situation we can also construct tables in order to forecast what could happen in an electoral process.

Behavior of f<sub>2k − 1, …,</sub> <sub>2k − 1</sub><sup>m</sup> <sup>− unanimity</sup> (0.55) for different values of k and m.

<table><tr><td>k</td><td> $f_{2k-1}(0.55)$ </td><td> $f_{2k-1}^{2-unanimity},\ldots,2k-1(0.55)$ </td><td> $f_{2k-1}^{4-unanimity},\ldots,2k-1(0.55)$ </td></tr><tr><td>2</td><td>0.5748</td><td>0.3303</td><td>0.1091</td></tr><tr><td>3</td><td>0.5931</td><td>0.3517</td><td>0.1238</td></tr><tr><td>10</td><td>0.6710</td><td>0.4503</td><td>0.2028</td></tr><tr><td>20</td><td>0.7357</td><td>0.5413</td><td>0.2930</td></tr><tr><td>40</td><td>0.8143</td><td>0.6631</td><td>0.4397</td></tr><tr><td>100</td><td>0.9216</td><td>0.8493</td><td>0.7214</td></tr></table>

We conclude this section by comparing the decisiveness of a decisive symmetric game $f _ { 2 k - 1 } ( p )$ with the decisivenes $; f _ { 2 k _ { 1 } - 1 , 2 k 2 - 1 , . . . , 2 k m - 1 } ^ { r - o u t - o f - ( 2 r - 1 ) } ( p )$ (where $m { = } 2 r { - } 1 )$ , of a $r – 0 \mathrm { u t } – 0 \mathrm { f } – ( 2 r - 1 )$ compound game where all component games are also decisive, provided that the overall number of votes is the same in both games, that is, $\begin{array} { r } { \sum _ { i = 1 } ^ { m } ( 2 k _ { i } - 1 ) = 2 k - 1 } \end{array}$

Example 5.4. (i) Let us consider the 3-out-of-5 compound game introduced at the beginning of this section. We will compare its decisiveness $f _ { 5 , 5 , 3 , 5 , 1 } ^ { 3 - o u t - v f - 5 } ( p )$ with the decisiveness $f _ { 1 9 } ( \boldsymbol { p } )$ of the 10-out-of-19 decisive symmetric game. Notice that both games have 19 players, but in the <sup>fi</sup>rst the players are not all symmetric. We obtain

$$
f _ {1 9} (p) - f _ {5, 5, 3, 5, 1} ^ {3 - o u t - o f - 5} (p) = p ^ {6} (1 - p) ^ {6} h (p) (2 p - 1)
$$

where

$$
\begin{array}{c} h (p) = - 2 3 0 1 4 p ^ {6} + 6 9 0 4 2 p ^ {5} - 6 3 9 0 3 p ^ {4} + 1 2 7 3 6 p ^ {3} \\ + 4 3 1 4 p ^ {2} + 8 2 5 p + 9 0 \end{array}
$$

is a positive function in [0,1]. Then

$$
f _ {1 9} (p) - f _ {5, 5, 3, 5, 1} ^ {3 - o u t - o f - 5} (p) > 0 \quad \text { if } \quad 1 / 2 <   p <   1
$$

and

$$
f _ {1 9} (p) - f _ {5, 5, 3, 5, 1} ^ {3 - o u t - o f - 5} (p) <   0 \quad \text { if } \quad 0 <   p <   1 / 2.
$$

From this result we observe that a slight bias in favor of breaking the status quo $( p \approx 1 / 2$ but $p { > } 1 / 2 )$ has a stronger effect for the weighted majority game than for the compound game, while the effect is the contrary if a slight bias against breaking the status quo $( p \approx 1 / 2$ but $p { < } 1 / 2 )$ exists.

As the next two items show, this is not an isolated case where this property holds.

(ii) We compare now the decisiveness of a 5-out-of-9 game and a 2- out-of-3 compound game where the three component games are also 2-out-of-3 games.

It is not dif<sup>fi</sup>cult to verify that

$$
f _ {9} (p) - f _ {3, 3, 3} ^ {2 - o u t - o f - 3} (p) = 2 7 p ^ {4} (1 - p) ^ {4} (2 p - 1),
$$

so that

$$
f _ {9} (p) - f _ {3, 3, 3} ^ {2 - o u t - o f - 3} (p) > 0 \text {   if   } 1 / 2 <   p <   1
$$

and

$$
f _ {9} (p) - f _ {3, 3, 3} ^ {2 - o u t - o f - 3} (p) <   0 \quad \text { if } \quad 0 <   p <   1 / 2.
$$

The same property as in (i) arises.

(iii) Finally, we compare the decisiveness of a 8-out-of-15 game and a 3-out-of-5 compound game where the <sup>fi</sup>ve component games are 2- out-of-3 games. Here

$$
f _ {1 5} (p) - f _ {3, 3, 3, 3, 3} ^ {3 - o u t - o f - 5} (p) = 2 7 0 p ^ {6} (1 - p) ^ {6} \left(- 6 p ^ {2} + 6 p + 1\right) (2 p - 1),
$$

so that

$$
f _ {1 5} (p) - f _ {3, 3, 3, 3, 3} ^ {3 - o u t - o f - 5} (p) > 0 \quad \text { if } \quad 1 / 2 <   p <   1
$$

and

$$
f _ {1 5} (p) - f _ {3, 3, 3, 3, 3} ^ {3 - o u t - o f - 5} (p) <   0 \quad \text { if } \quad 0 <   p <   1 / 2.
$$

The property arises again.These three instances suggest the following conjecture, which would be interesting to verify.

Conjecture. If the decisiveness $f _ { 2 k - 1 } ( p )$ is compared with $f _ { 2 k _ { 1 } } ^ { r - { \bf \bar { o } } u t } - { \bf \Sigma } _ { 2 k 2 } ^ { o f - ( 2 \bar { r } - 1 ) } { \bf \Sigma } _ { \cdots } ^ { } { \bf \Sigma } _ { 2 k m - 1 } ^ { } \left( p \right)$ , where $m = 2 r - 1$ and $\begin{array} { r l r } {  { \sum _ { i = 1 } ^ { m } ( 2 k _ { i } - 1 ) = } } \end{array}$ $2 k - 1 ,$ , we contend that

$$
f _ {2 k - 1} (p) - f _ {2 k _ {1} - 1, 2 k _ {2} - 1, \dots , 2 k _ {m} - 1} ^ {r - o u t - o f - (2 r - 1)} (p) = \overline {{h}} (p) (2 p - 1),
$$

where $\overline { { h } } ( p )$ stands for a positive polynomial function on (0, 1), symmetric with respect to point $p { = } 1 / 2$ and attaining its unique absolute maximum on [0,1] at point $1 / 2 .$

From this, we could deduce that

$$
f _ {2 k - 1} (p) - f _ {2 k _ {1} - 1, 2 k _ {2} - 1, \dots , 2 k _ {m} - 1} ^ {r - o u t - o f - (2 r - 1)} (p) > 0 \quad \text { if } \quad 1 / 2 <   p <   1
$$

and

$$
f _ {2 k - 1} (p) - f _ {2 k _ {1} - 1, 2 k _ {2} - 1, \dots , 2 k _ {m} - 1} ^ {r - o u t - o f - (2 r - 1)} (p) <   0 \quad \text { if } \quad 0 <   p <   1 / 2.
$$

## 6. Conclusions

In this paper we have studied decisive symmetric games and extended our results partially to their compositions by means of a quotient k-out-of-m game not necessarily decisive. We have shown that, when the common assessment of the players is greater than 1/2, the game decisiveness increases quickly, and also that it tends to 1 when the number of players increases, thus emphasizing the interest of keeping the player assessment at this higher level. Several additional considerations should also be pointed out.

(a) If the players' assessments differ, high game decisiveness still arises when maintaining above 1/2 the lowest individual assessment. This follows from the results obtained in the paper since the α-decisiveness $f ( \alpha _ { 1 } , \alpha _ { 2 } , . . . , \alpha _ { n } )$ is a monotonic function with respect to each variable.

(b) The main results obtained here are asymptotic, generating interest in the convergence speed. Tables 1, 5 and 6 illustrate some particular cases for several values of k and $p { = } 0 . 5 5$ . For instance, the basic model, given by $f _ { 2 k - 1 } ( p )$ , requires at least 199 players to achieve a level of decisiveness above 0.92, but if $p { = } 0 . 6$ instead of $p { = } 0 . 5 5$ then the enlargement is substantial (see Table 1). By considering a composition of a few games via unanimity, the convergence to 1 becomes slower (see Table 6). However, when considering a composition of a few games via individualism, the convergence to 1 becomes quicker (see Table 7).

(c) In general, given an arbitrary sequence of decisive games, it is not true that its asymptotic behavior is the same as function F(p) obtained in Theorem 4.1. For instance, for each integer n≥1 one may consider a game (N, W) with n players in which the winning coalitions are those that contain a particular player i, so that all games are dictatorships of player i. These games are decisive and their decisiveness is given by $f _ { n } ( p ) = p$ for all $n \in  { \mathbb { N } } ,$ where p is the players' common assessment, but it is clear that its pointwise limit is $F ( p ) = p$

<table><tr><td>k</td><td> $f_{2k-1}(0.55)$ </td><td> $f_{2k-1,\dots,2k-1}^{2-individualism}(0.55)$ </td><td> $f_{2k-1,\dots,2k-1}^{4-individualism}(0.55)$ </td></tr><tr><td>2</td><td>0.5748</td><td>0.8192</td><td>0.9673</td></tr><tr><td>3</td><td>0.5931</td><td>0.8344</td><td>0.9726</td></tr><tr><td>10</td><td>0.6710</td><td>0.8918</td><td>0.9883</td></tr><tr><td>20</td><td>0.7357</td><td>0.9301</td><td>0.9951</td></tr><tr><td>40</td><td>0.8143</td><td>0.9655</td><td>0.9988</td></tr><tr><td>100</td><td>0.9216</td><td>0.9936</td><td>0.9999</td></tr></table>

Further research should be focused on suggestions A and B below. However, considering more general classes of games and/or more general assessment vectors would most probably result in a loss of quality with respect to the regular results found here.

A. Symmetric but not necessarily decisive simple games could be considered. Both cases $k { < } \frac { n + 1 } { 2 }$ and $\textstyle k > { \frac { n + 1 } { 2 } }$ deserve interest. Also general weighted majority games and even general simple games could be analyzed.

B. It would be interesting to work with assessment vectors whose components were de<sup>fi</sup>ned by two parameters $p \neq q$ such that $0 { \le } q { \le } 1 / 2 { \le } p { \le } 1$ . Or even by three parameters $p , q , r$ such that $0 { \le } q { < } r { = } 1 / 2 { < } p { \le } 1$ . Finally, an attempt could be made to deal with assessment vectors $\alpha { = } ( \alpha _ { 1 } , \alpha _ { 2 } , . . . , \alpha _ { n } )$ free from any restriction.

## Acknowledgements

The authors wish to thank three anonymous referees for their helpful comments.

## Appendix. Proofs

Lemma 3.1. Using Eq. (2), (b) is trivial and (a) and (c) are straightforward consequences of the relationship $\binom { n + 1 } { k } =$ $\textstyle { \binom { n } { k } } + \left( { \begin{array} { c } { n } \\ { k - 1 } \end{array} } \right)$ for all $n , k { \in } N$ such that $1 \leq k \leq n$ □

Lemma 3.3. The result follows by applying Lemma 3.1 to the decomposition

$$
\begin{array}{l} f _ {2 k + 1, k + 1} (p) - f _ {2 k - 1, k} (p) = \left[ f _ {2 k + 1, k + 1} (p) - f _ {2 k, k} (p) \right] \\ \qquad + \left[ f _ {2 k, k} (p) - f _ {2 k, k + 1} (p) \right] \\ \qquad + \left[ f _ {2 k, k + 1} (p) - f _ {2 k - 1, k} (p) \right]. \end{array}
$$

Theorem 4.1. Part A. Let $g ( p ) { = } f _ { 2 k - 1 } ( p ) { + } f _ { 2 k - 1 } ( 1 - p )$ . Then $g ( 0 ) =$ 1. Moreover, as

$$
f _ {2 k - 1} ^ {\prime} (p) = k \binom {2 k - 1} {k} p ^ {k - 1} (1 - p) ^ {k - 1},
$$

it follows that $g ^ { \prime } ( p ) = 0$ for all $p \in [ 0 , 1 ]$ . Thus, g(p) is constant and its value is 1. This proves (A1).

$A s f _ { 2 k - 1 } ^ { \prime } ( p ) { > } 0$ whenever $0 < p < 1$ , it follows tha $\cdot f _ { 2 k - 1 } ( p )$ increases on [0,1]. This proves (A2).

Finally, (A3) easily follows, for kN2, from the expression of the second derivative

$$
f _ {2 k - 1} ^ {\prime \prime} (p) = k (k - 1) \binom {2 k - 1} {k} p ^ {k - 2} (1 - p) ^ {k - 2} (1 - 2 p).
$$

Indeed, we then have $f _ { 2 k - 1 } ^ { \prime \prime } ( p ) { > } 0 \mathrm { i f } 0 { < } p { < } 1 / 2 , f _ { 2 k - 1 } ^ { \prime \prime } ( p ) { < } 0$ if $1 / 2 { < } p { < } 1$ , and hence $f _ { 2 k - 1 } ^ { \prime \prime } ( p ) = 0$ just for $p { = } 0 , 1 / 2 , 1$ , which implies that the unique <sup>fi</sup>xed points of $f _ { 2 k - 1 } ( p )$ are also $p { = } 0 , 1 / 2 , 1 . \operatorname { F o r } k { = } 2 ,$ $f _ { 2 k - 1 } ^ { \prime \prime } ( p )$ vanishes only at $p { = } 1 / 2$ , but the <sup>fi</sup>xed points directly follow from $f _ { 2 k - 1 } ( p ) = p .$

Part B. Statements (B1) and (B2) respectively follow from (A1) and (A2). As to (B3), <sup>fi</sup>rst we have

$$
G _ {2 k - 1} ^ {\prime} (p) = k \binom {2 k - 1} {k} p ^ {k - 1} (1 - p) ^ {k - 1} - 1.
$$

Setting $\beta = p ( 1 - p )$ , equation $G _ { 2 k - 1 } ^ { \prime } ( p ) = 0$ gives $\beta = \bigg [ k \binom { 2 k - 1 } { k } \bigg ] ^ { \frac { 1 } { 1 - k } }$ The roots of $p ^ { 2 } - p + \beta = 0$ are therefore $1 / 2 \pm \sqrt { 1 - 4 \beta } / 2$ (and are denoted as $p _ { M }$ and $p _ { m } ,$ respectively). Using Bolzano's theorem we check that these roots must belong to the interval $( 0 , 1 ) ^ { }$ , given that $G _ { 2 k - 1 } ^ { \prime } ( p )$ is a continuous function with

$$
G _ {2 k - 1} ^ {\prime} (0) <   0, \quad G _ {2 k - 1} ^ {\prime} (1) <   0 \quad \text { and } \quad G _ {2 k - 1} ^ {\prime} (1 / 2) > 0.
$$

The two former inequalities are clear. For the third, we have to check that $\begin{array} { r } { G ^ { \prime } ( 1 / 2 ) = k \binom { 2 k - 1 } { k } \frac { 1 } { 4 ^ { k - 1 } } - 1 } \end{array}$ is positive. If we set $\begin{array} { r } { r _ { k } = \frac { ( 2 k - 1 ) ! } { [ ( k - 1 ) ! ] ^ { 2 } } } \end{array}$ , the relation $r _ { k } { > } 4 ^ { k - 1 }$ is easily derived by induction, as $r _ { 2 } { > } 4$ <sup>½ð</sup>and $\begin{array} { r } { r _ { k + 1 } = \frac { 2 ( 2 k + 1 ) } { k } r _ { k } > 4 ^ { k } } \end{array}$ follows from the induction assumption $r _ { k } { > } 4 ^ { k - }$

In addition, the sign of $G _ { 2 k - 1 } ^ { \prime } ( p )$ establishes the intervals where $G _ { 2 k - 1 } ( p )$ increases or decreases and, jointly with $G _ { 2 k - 1 } ( 0 ) = 0 =$ $G _ { 2 k - 1 } ( 1 )$ , con<sup>fi</sup>rms that the unique absolute maximum and minimum of $G _ { 2 k - 1 } ( p )$ on [0,1] are attained at points $p _ { M }$ and $p _ { m } ,$ respectively. Finally, (B4) follows from (A3) since

$$
G _ {2 k - 1} ^ {^ {\prime \prime}} (p) = f _ {2 k - 1} ^ {^ {\prime \prime}} (p) = k (k - 1) \binom {2 k - 1} {k} p ^ {k - 2} (1 - p) ^ {k - 2} (1 - 2 p).
$$

Part C. Statement (C1) is straightforward to verify. For (C2), it is clear that $p { = } 0 , 1 / 2 ,$ , 1 are roots of $\Delta _ { 2 k - 1 } ( p )$ . Uniqueness follows from the piecewise monotonicity of $\Delta _ { 2 k - 1 } ( p )$ , stated in (C3).

For (C3), from

$$
\Delta_ {2 k - 1} ^ {\prime} (p) = - \binom {2 k - 1} {k} p ^ {k - 1} (1 - p) ^ {k - 1} \Big [ (4 k + 2) p ^ {2} - (4 k + 2) p + k \Big ]
$$

it follows that the only roots of $\Delta { ' } _ { 2 k - 1 } ( p ) = 0$ in the interval (0, 1) are $1 / 2 { \pm } 1 / 2 \sqrt { 2 k + 1 }$ (denoted as $p ^ { \prime } u$ and ${ p ^ { \prime } } _ { m } ,$ respectively). The remains of this proof follow the same guidelines as those of (B3). Finally, for (C4) we get

$$
\begin{array}{l} \Delta_ {2 k - 1} ^ {"} (p) = - \binom {2 k - 1} {k} p ^ {k - 2} (1 - p) ^ {k - 2} \\ \qquad \times \Big [ - \Big (8 k ^ {2} + 4 k \Big) p ^ {3} + \Big (1 2 k ^ {2} + 6 k \Big) p ^ {2} - 6 k ^ {2} p + k ^ {2} - k \Big ] \\ = \binom {2 k - 1} {k} p ^ {k - 2} (1 - p) ^ {k - 2} (2 p - 1) \\ \qquad \times \Big [ \Big (4 k ^ {2} + 2 k \Big) p ^ {2} - \Big (4 k ^ {2} + 2 k \Big) p + k ^ {2} - k \Big ]. \end{array}
$$

The roots of $\Delta _ { 2 k - 1 } ^ { \prime \prime } ( p ) { = } 0$ in (0, 1) are 1/2 and $1 / 2 { \pm } \sqrt { 3 } / 2 \sqrt { 2 k + 1 }$ (denoted as $p _ { 2 }$ and $p _ { 1 } ,$ respectively). The remains of this proof are analogous to those of (B4).

The fact that there is a symmetry center for all graphs at $p { = } 1 / 2$ derives from (A1), (B1) and (C1). □

Theorem 4.2. Part (i) let $p { < } 1 / 2 .$ Then, taking into account that

$$
p ^ {k} (1 - p) ^ {k - 1} > p ^ {k + 1} (1 - p) ^ {k - 2} > \dots > p ^ {2 k - 1}
$$

and

$$
\sum_ {i = k} ^ {2 k - 1} \binom {2 k - 1} {i} = \frac {1}{2} \sum_ {i = 0} ^ {2 k - 1} \binom {2 k - 1} {i} = 4 ^ {k - 1},
$$

we obtain

$$
\begin{array}{l} 0 \leq f _ {2 k - 1} (p) = \sum_ {i = k} ^ {2 k - 1} \binom {2 k - 1} {i} p ^ {i} (1 - p) ^ {2 k - 1 - i} \\ \quad \leq p ^ {k} (1 - p) ^ {k - 1} \sum_ {i = k} ^ {2 k - 1} \binom {2 k - 1} {i} = p ^ {k} (1 - p) ^ {k - 1} 4 ^ {k - 1}. \end{array}
$$

The sequence on the right tends to 0 because $p ( 1 - p ) { < } 1 / 4$ for $p { < } 1 / 2$ , so that $F ( p ) = 0$ whenever pb1/2. As 1/2 is a <sup>fi</sup>xed point for each $f _ { 2 k - 1 } \ ( { \mathsf { s e e } } \ ( { \mathsf { A } } 2 )$ in Theorem 4.1), $F ( 1 / 2 ) = 1 / 2$ . Finally, if $p { > } 1 / 2$ then $F ( p ) = 1$ because of the symmetry property (A1) for each $f _ { 2 k - 1 }$ with k≥2 (Theorem 4.1).

Part (ii) follows from applying Part (i) to the aggregate function. □

Theorem 4.2. Alternative Proof. Function $f _ { 2 k - 1 } ( p ) = 1 - P r o b ( X { < } k )$ where X is a binomial random variable with $n = 2 k - 1$ trials and probability of success equal to p. We may apply the Chernoff bound to get

$$
\operatorname{Prob} (X <   k) <   \exp \left(- 2 \frac {(n p - k) ^ {2}}{n}\right) \quad \text { whenever } \quad k \leq n p.
$$

Taking $p { > } 1 / 2 ,$ , we get that $P r o b ( X { < } k )$ tends to 0 when k goes to ∞ and hence $F ( p ) = 1 . \mathrm { I f } p { < } 1 / 2$ then $F ( p ) = 0$ because of the symmetry property (A1) for each $f _ { 2 k - 1 }$ with $k \geq 2 .$ . Finally, as 1/2 is a <sup>fi</sup>xed point for each $f _ { 2 k - 1 }$ (see (A2) in Theorem 4.1), $F ( 1 / 2 ) = 1 / 2$ □

## References

[1] J.M. Alonso-Meijide, J. Freixas, A new power index based on minimal winning coalitions without any surplus, Decision Support Systems 49 (2010) 70–76

[2] G. Ariav, M.J. Ginzberg, DSS design: a systemic view of decision support, Communications of the ACM 28 (1985) 1045–1052.

[3] P. Bharati, A. Chaudhury, An empirical investigation of decision-making satisfaction in web-based Decision Support Systems, Decision Support Systems 37 (2004) 187–197.

[4] F. Carreras, α-Decisiveness in simple games, Theory and Decision 56 (2004) 77–91.

[5] F. Carreras, A decisiveness index for simple games, European Journal of Operational Research 163 (2005) 370–387.

[6] F. Carreras, A. Magaña, The Shapley–Shubik index for simple games with multiple alternatives, Annals of Operations Research 158 (2008) 81–97.

[7] J.S. Coleman, Control of collectivities and the power of a collectivity to act, in: B. Lieberman (Ed.), Social Choice, Gordon and Breach, New York, 1971, pp. 269–300.

[8] D.S. Felsenthal, M. Machover, Ternary voting games, International Journal of Game Theory 26 (1997) 335–351.

[9] D.S. Felsenthal, M. Machover, Models and reality: the curious case of the absent abstention, in: M.J. Holler, G. Owen (Eds.), Power Indices and Coalition Formation, Kluwer Academic Publishers, Dordrecht, 2001, pp. 87–103.

[10] J. Freixas, The Shapley–Shubik index for games with several levels of approval in the input and output Decision Support Systems 39 (2005) 269–282

[11] J. Freixas, Bounds for the Owen multilinear extension, Journal of Applied Probability 44 (2007) 852–864

[12] J. Freixas, M.A. Puente, A note about games—composition dimension, Discrete Applied Mathematics 113 (2001) 265-273

[13] J. Freixas, W.S. Zwicker, Weighted voting, abstention and multiple levels of approval, Social Choice and Welfare 21 (2003) 399–431.

[14] J. Freixas, W.S. Zwicker, Anonymous yes–no voting with abstention and multiple levels of approval, Games and Economic Behavior 69 (2009) 428–444.

[15] E.J. Garrity, B. Glassberg, Y.J. Kim, G.L. Sanders, S.K. Shin, An experimental investigation of web-based information systems success in the context of electronic commerce, Decision Support Systems 39 (2005) 483–503.

[16] J.R. Isbell, A class of simple games, Duke Mathematics Journal 25 (1958) 423–439.

[17] T. Moyaux, B. Chaid-draa, S. D'Amours, Multi-agent simulation of collaborative strategies in a supply chain, International Conference on Autonomous Agents, Proceedings of the Third International Joint Conference on Autonomous Agents and Multiagent Systems, vol. 1, 2004, pp. 52–59.

[18] M. Nagarajan, G. Sosic, Game-theoretic analysis of cooperation among supply chain agents: review and extensions, European Journal of Operational Research 187 (2008) 719–745.

[19] G. Owen, Game Theory, 3rd. ed, Academic Press, 1995.

[20] G. Owen, Multilinear extensions of games, Management Science 18 (1972) 64–79.

[21] L.S. Shapley, M. Shubik, A method for evaluating the distribution of power in a committee system, American Political Science Review 48 (1962) 787–792.

[22] L.S. Shapley, Simple games: an outline of the descriptive theory, Behavioral Science 7 (1962) 59–66.

[23] L.S. Shapley, Compound Simple Games I: Solutions of Sums and Products, The RAND Corporation, Santa Monica, 19628 RM–3192.

Francesc Carreras was born in 1949 in Terrassa, Spain. He received his B. S. Degree in Mathematics from the University of Barcelona and his Ph.D. in Mathematics from the Universitat Autònoma de Barcelona. At the present, full professor of the Universitat Politècnica de Catalunya (UPC), at the Department of Applied Mathematics II and the Industrial and Aeronautical Engineering School of Terrassa. He is author of books on linear algebra and game theory. His research concerns game theory and related <sup>fi</sup>elds. He has been awarded the Operations Research Prize of the Spanish Defense Ministry in 1992 and 1995. He is leading the UPC Game Theory Research Group and the three-year Research Project “Cooperative Games and Con<sup>fl</sup>icts of Interest. Theory and Practice”, supported by the Education and Science Spanish Ministry and the European Regional Development Fund. Invited lectures at different universities and presentations in national and international conferences and meetings. Papers published in different journals and contributed chapters to several volumes.

Josep Freixas received the PhD in Mathematics from the Technical University of Catalonia, in 1994. He works in the Department of Applied Mathematics 3 and in the High Engineering School of Manresa. He was visiting professor in the Bergamo University (Italy) in 1996 and in the Union College of Schenectady in New York (USA) in 2000. His research interests include Decision and Game Theory, Reliability and Computer Sciences. He has published many papers on these topics. Invited lectures in different universities. Supervisor of several Ph. D. Thesis. Leading several research projects on Game Theory and Decision-Making. External member of the "Barcelona Graduate School of Economics" who partially supported this work.

María Albina Puente was born in 1962 in Ribadeo, Spain. She received the PhD in Mathematics from the Technical University of Catalonia, in 2000 She works in the Department of Applied Mathematics 3 and in High Engineering School of Manresa. His research interests include Decision and Game Theory, Reliability and Computer Sciences. He has published some papers on these topics.

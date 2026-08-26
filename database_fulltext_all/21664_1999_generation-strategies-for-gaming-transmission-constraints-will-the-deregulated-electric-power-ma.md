---
otero_id: 21664
otero_key: "NYF2FASV"
title: "Generation strategies for gaming transmission constraints: will the deregulated electric power market be an oligopoly?"
authors: "Ziad Younes; Marija Ilic"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00075-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Generation strategies for gaming transmission constraints: will the deregulated electric power market be an oligopoly?

Ziad Younes <sup>a</sup>, Marija Ilic <sup>b,)</sup>

<sup>a</sup> Technology and Policy Program, Massachusetts Institute of Technology, Economie Industrielle, UniÕersite de Paris IX, Paris, France ´ <sup>b</sup> Department of Electrical Engineering and Computer Science, Massachusetts Institute of Technology, Room 10-059, Cambridge, MA 02139 USA

## Abstract

Constrained transmission lines are known to be able to economically isolate submarkets from the competition of players located elsewhere on the network. This paper examines the type of oligopolistic competition that is likely to take place in these submarkets. It shows, using simple models, how static or intertemporal Nash equilibria can rise in a framework of price or supply function competitions, found to be more realistic than Cournot models in the particular case of short-term competition in the electric power market. This paper shows also how transmission constraints can play a direct role in the outcome of the oligopolistic competition and encourage strategic behavior by the generators. Transmission lines that would not be constrained if the players did not know of their thermal limits may be strategically driven to operate at these limits in order to maximize the profits of the players who have market power, leaving the others to cope with the consequences of such behavior. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Transmission constraints; Market power; Electric power systems; Games

## 1. Introduction

The nodal pricing proposal advocated in Ref. 5 has been frequently criticized because it ignores the<sup>w</sup> <sup>x</sup> potential market power that the market participants can have in such a framework. Singh et al. 10 show how,<sup>w</sup> <sup>x</sup> with location-dependent nodal spot pricing and transmission constraints, a non-discriminating auction mechanism creates opportunities for strategic behavior. Nevertheless, the problem of market power lies beyond the auction mechanism or the features of the nodal pricing model. More generally, in any market structure in which the generators determine their bids, those generators in areas constrained by weak transmission lines should see their market power boosted because they are isolated, by the constraints, from the competition of other generators. As shown in Ref. 13 , locational market power will exist because of loop flow and transmission <sup>w</sup> <sup>x</sup> constraints that produce geographically and temporally localized relevant markets. One single constrained line in a meshed 24-bus system was shown to be sufficient to create a relevant submarket of three buses while this submarket was still linked to the rest of the network by four unconstrained lines. Moreover, as shown by the experience of deregulation in the British electric power market 12 , global market power can also exist,<sup>w</sup> <sup>x</sup> transmission constraints set aside, because of the relative size of competitors. Therefore, one should not assume, a priori, that the market is perfect, but rather acknowledge the potential existence of market power in any form of proposed deregulation and try to limit this power. To do this, we will have to replace our traditional assumptions of a perfect market with more realistic oligopolistic models.

The objective of this paper is to present some of the potential conceptual consequences of abandoning these perfect market assumptions. Section 2 reviews the basics of oligopolistic competition and static or intertemporal Nash equilibria; readers familiar with these concepts may want to skip it. In Section 3, we discuss the choice of the oligopolistic model best suited for electric power systems. In Section 4, we expose some of the consequences of oligopolistic competition prior to accounting for transmission constraints; we discuss the potential emergence of tacit collusion and determine conditions under which this behavior is not sustainable. In Section 5, we introduce transmission constraints in the simple three-bus power system models and show how they can induce new types of strategic behavior.

## 2. Oligopolistic competition: generalities

In a dynamic game with discrete stages, a number of players are making a strategic decision at each stage. The combined decisions of all players determine, through a middleman or in a decentralized market setting, the quantities of goods exchanged between the players as well as the prices at which they are exchanged, and, therefore, the profits of the players for the stage.

Let n be the number of players, k the stage index, $x _ { i }$ the strategic variable whose value player i chooses in the set $E _ { i } , ~ x _ { i } ( k )$ the strategic decision of player i at stage $k ; \ \pi _ { i }$ the one-stage profit function of player i, $\pi _ { i } ( x _ { 1 } ( k ) , \ldots , x _ { n } ( k ) )$ is its profit at period $k , ~ r$ the discount rate between two consecutive stages, X the vector $[ x _ { 1 } , \ldots , x _ { n } ] _ { }$ , and $X _ { - i }$ the vector $\left[ { { x _ { 1 } } , \ldots , { x _ { i - 1 } } , { x _ { i + 1 } } , \ldots , { x _ { n } } } \right]$

## 2.1. One-stage competition

In a one-stage competition framework, player i assumes that all other players are taking fixed decisions $X _ { \scriptscriptstyle { 0 _ { - i } } }$ . He will give to his own decision variable $x _ { i }$ the value $x _ { \mathbf { o } _ { i } }$ that maximizes his profit:

$$
\pi_ {i} \left(x _ {\mathrm{o} _ {i}}, X _ {\mathrm{o} _ {- i}}\right) = \max _ {\alpha L E i} \pi_ {i} \left(\alpha , X _ {\mathrm{o} _ {- i}}\right).\tag{1}
$$

Or, when $x _ { i }$ takes real values and $\pi _ { i }$ is differentiable:

$$
\frac {f \pi_ {i}}{f x _ {i}} \left(x _ {\mathrm{o} _ {i}}, X _ {\mathrm{o} _ {- i}}\right) = 0.\tag{2}
$$

When $\pi _ { i }$ has continuous second derivatives, the implicit function theorem 9 ensures locally the existence of a <sup>w</sup> <sup>x</sup> reaction function $R _ { i }$ , whose partial derivatives exist and are continuous, so that:

$$
\frac {f \pi_ {i} \big (R _ {i} (\boldsymbol {X} _ {- i}) , \boldsymbol {X} _ {- i} \big)}{f x _ {i}} = 0,\tag{3}
$$

where:

$$
R _ {i} \big (\textbf {X} _ {- i} \big) = x _ {i}\tag{4}
$$

gives the optimal choice of player i for $X _ { . i }$ fixed.

Definition 1: We say that X ) is a static Nash equilibrium if:

$$
\forall i, \frac {f \pi_ {i} (\boldsymbol {X} *)}{f x _ {i}} = 0.\tag{5}
$$

At a static Nash equilibrium, every strategic variable $x _ { i } *$ is the optimal choice of player i for $X _ { . i }$ ) fixed. X ) is also an intersection point of all reaction functions:

$$
\forall i, x _ {i} * = R _ {i} \left(X _ {- i} *\right).\tag{6}
$$

In an oligopolistic situation with only one stage, the static Nash equilibrium is likely to be obtained if all players can observe the decisions of all other players and change their own decisions in real time. If the bids are revealed only after the market clears, attaining this equilibrium is unlikely and depends on the information that every player has since he will make his decision as a function of what he expects the other decisions to be.

## 2.2. Dynamic process and stability of static Nash equilibria

In a dynamic framework, at every stage, the players learn more about the decisions of the others and the strategic variables may converge to the static Nash equilibrium even if the bids are not revealed before the market clears at any given stage. Assuming that a player knows the bets of other players in the preÕious stage, not knowing what they will be at the current stage, the simplest strategy would be for him to assume that the bets are staying as they were in the previous period and to maximize his profit accordingly. In this case:

$$
\forall i, \forall k, x _ {i} (k + 1) = R _ {i} \left(X _ {- i} (k)\right).\tag{7}
$$

This set of equations describes dynamically how the bets at the current stage depend on the bets at the previous stage. It is clear that if the process defined in Eq. 7 converges, its limit is a static Nash equilibrium. TheŽ . stability of this equilibrium is an important question. Studying the stability of an equilibrium requires determining whether the system can converge to this equilibrium independently of the initial conditions generalŽ stability , and . Ž . <sup>r</sup>or whether it can return to it after a small perturbation local stability .

When X ) is a static-Nash equilibrium:

$$
\forall i, x _ {i} (k + 1) - x _ {i} * = R _ {i} \left(X _ {- i} (k)\right) - R _ {i} \left(X _ {- i} *\right),\tag{8}
$$

$$
\forall i, \forall k, x _ {i} (k + 1) = x _ {i} * + \sum_ {j \neq i} \left(\frac {\partial R _ {i}}{\partial x _ {j}} (\boldsymbol {X} _ {- i} *)\right) \left(x _ {j} (k) - x _ {j} *\right) + O \left| \left| \boldsymbol {X} _ {- i} (k) - \boldsymbol {X} _ {- i} * \right| \right| ^ {2}.\tag{9}
$$

From Eq. 3 , we get: Ž .

$$
\forall i, _ {j? i} \left(\frac {f ^ {2} \pi_ {i}}{f x _ {i} x _ {j}} \mathrm{d} x _ {j}\right) + \frac {f ^ {2} \pi_ {i}}{f x i ^ {2}} _ {j? i} \frac {f R _ {i}}{f x _ {j}} \mathrm{d} x _ {j} = 0.\tag{10}
$$

When $( f ^ { 2 } \pi ) / ( f x i ^ { 2 i } )$ Ž . is different from 0 for all i, Eq. 9 can be rewritten as:

$$
\forall i, \forall k, (x _ {i} (k + 1) - x _ {i} ^ {*}) = \underset {i? i} {\overset {f \pi_ {i}} {-}} \frac {\overline {{f x _ {i} x _ {j}}}}{\overline {{f ^ {2} \pi_ {i}}} ^ {(x _ {- i} *)}} \underset {f x _ {i} ^ {2}} {\overset {\vee} {\rightleftarrows}} (x _ {j} (k) - x _ {j} ^ {*}) + O \big \| X _ {- i} (k) - X _ {- i} * \big \| ^ {2}\tag{11}
$$

Linearizing Eq. 11 gives: Ž .

$$
\big (\boldsymbol {X} (k) - \boldsymbol {X} * \big) = \mathbf {A} ^ {k} \big (\boldsymbol {X} _ {0} - \boldsymbol {X} * \big),\tag{12}
$$

where the elements of matrix A are,

$$
a _ {i j} = \begin{array}{c} - f ^ {2} \pi_ {i} \\ - \overline {{f x _ {i} x _ {j}}} \\ \overline {{f ^ {2} \pi_ {i}}} \\ \overline {{f x i ^ {2}}} \end{array} , \quad i? j \quad \text {and} a _ {i j} = 0, i = j\tag{13}
$$

Theorem: The stability of the linearized system, and, therefore, the local stability of the static Nash equilibrium, is ensured when the eigenÕalues of matrix A are less than 1 in module. Furthermore, when Eq. 11 is linear, ( ) the same condition implies general stability.

This theorem is an immediate application of Ref. 1 .<sup>w</sup> <sup>x</sup>

## 2.3. Intertemporal Nash strategies

Nash static equilibrium, although useful for analyzing many situations, has a major weakness in multistage games since it does not recognize that the decision of a player at one stage might affect the decisions of other players at further stages and that this player might take his decision accordingly. In order to recognize this interdependence in multistage games, we can define Nash equilibria in terms of strategies rather then in terms of strategic variables, where a strategy chosen by a player determines his decision at a stage as a function of what the other players did at past stages of the game.

We say that the function $S _ { i }$ is the inter-temporal strategy of player i when the decision of player i at the stage k is given by:

$$
x _ {i} (k) = S _ {i} (k, X (0), \dots X (k - 1)).\tag{14}
$$

If $S = [ S _ { 1 } , \ldots S _ { n } ]$ is the set of strategies of all players, their strategic decisions at every stage will be defined recursively by the strategies S and the vector X at stage k will be $X ( k , S )$

Definition 2: We say that $S * = [ S _ { I } * , \ldots , S _ { n } * J$ is an inter-temporal Nash equilibrium if eÕery strategy $S _ { i } *$ maximizes the discounted sum of the profits of player i giÕen the other strategies $S _ { - i } * =$ $\left. l S _ { I } \ast , S _ { i - I } \ast , S _ { i + I } \ast , \dots , S _ { n } \ast I \right.$ as fixed. Or:

$$
\forall i, \frac {_ {k} \pi_ {i} (X (k , S *))}{(1 + r) ^ {k}} = \max _ {S _ {i}} \frac {_ {k} \pi_ {i} (X (k , S _ {i} , S * _ {- i}))}{(l + r) ^ {k}}.\tag{15}
$$

When X ) is a static Nash equilibrium, staying at X ) at every period strategiesŽ S) where $X ( k , S * ) = X * )$ is also an inter-temporal Nash equilibrium. However, it might not be the unique or even a Pareto-optimal <sup>1</sup> inter-temporal Nash equilibrium.

## 2.4. Cournot competition, Bertrand competition and perfect markets

A Bertrand competition is an oligopolistic framework where the strategic variables $( x _ { i } ) _ { i \leq n }$ are the prices $\left( P _ { i } \right) _ { i \leq n }$ of the goods produced by the players, a static Nash equilibrium is then called a Bertrand–Nash equilibrium. In a Cournot competition, the strategic variables $\left( x _ { i } \right) _ { i \leq n }$ are the quantities ${ { \left( { q } _ { i } \right)}  } _ { i \le n }$ of goods produced by the players, and an equilibrium would be a Cournot–Nash equilibrium. A perfect market is an extreme case of Cournot competition where the number of players is infinite and the price of the market p is an exogenous constant rather than a function of the quantities. In a perfect market, equality 5 shows how everyŽ . player will produce the quantity that equalizes its marginal cost with the market price.

## 3. Choosing the strategic variables

The type of oligopolistic model that is adapted to study an oligopolistic market for electric power depends on the future structure of this market. In a centralized market, where a power exchange PX takes the bids of theŽ . generators and loads and determines the physical dispatch, the type of competition is exogenous and depends on the bidding procedure. When the generators are bidding prices and the PX determines the quantities, the short-term competition will be a Bertrand competition. When the generators are to bid their production levels as a function of the prices they receive, the short term equilibrium prices will then be given by the ‘supply function equilibrium’ developed in Ref. 6 and applied to the British power market in Ref. 4 . The equilibrium price<sup>w x</sup> <sup>w x</sup> will be higher than those yielded by a Bertrand competition and lower than those given by a Cournot competition in the unlikely case where the generators are only bidding quantities.

In a decentralized market where the transactions are settled in bilateral and multilateral markets, the type of short-term competition is endogenous and probably not unique. <sup>2</sup> One of the classic oligopolistic models is the Cournot model where the firms compete by choosing the quantity they want to put on the market and an independent auctioneer sets the price that clears the market. Well-adapted to the study of long-term competition and barriers for entry, Cournot competition models are useful in scenarios where the firms first commit themselves to a production capacity and compete next by choosing prices in a second period since the competition by prices in the second period yields the same results given by a one-phase game where the strategic variable chosen by the firm is their output 7 . Therefore, the Cournot competition model might be adapted to examine generation competition in a long-term strategic interaction framework where the generators have to choose their generation capacity a la Cournot before competing a la Bertrand every day. \` \`

Nevertheless, besides some specific cases the oil market in certain periods of its history, for example ,Ž . competition by quantities is fairly unrealistic to analyze short-term competition. This is especially true in decentralized multilateral and bilateral electric power markets where firms rarely bid only for quantities and where there is no central auctioneer to set the price. One could argue in favor of using Cournot competition to determine what happens on a daily basis since it is supposed to give the expected output of a Bertrand competition in the second period. Nevertheless, this reasoning makes two very strong and unrealistic assumptions: 1 the demand characteristics should be the same in the ‘second period’ as those expected when theŽ . capacity choices were made first period ; 2 the demand should also be fairly stable in the very short term, andŽ . Ž . very close to its average, to enable the long-term expected outcome the outcome of the Cournot competition toŽ . be used to interpret what happens on an hourly basis. Furthermore, when transmission lines are constrained <sup>3</sup> and generators are competing for their use, it is unrealistic to consider that when taking its strategic decisions, a generator will not expect his competitors to react immediately to any change in his own output. For all these reasons, this model seems unable to give valuable insights on short-term hourly, daily competition in theŽ . generation market.

An alternative is the classical Bertrand oligopolistic competition model where the strategic variables are the prices that each competing firm chooses to maximize its profit, considering as fixed the prices of its competitors. Under this model, the equilibrium price will be the marginal cost of production when the products are undifferentiated, the firms can serve all the demand they face at a constant marginal price, and the players play once. This result, combined with the observation that the prices on the British electric power market are above marginal prices, has sometimes been used to reject this competition model in favor of a Cournot competition 8 . Nevertheless, Edgeworth 3 has shown that, if no single firm can serve all the demand, the <sup>w x</sup> <sup>w x</sup> output of a Bertrand competition with production capacity constraints is no longer competitive and the equilibrium price can exceed the marginal cost. As reported by Ref. 11 , this result is valid in the more general<sup>w</sup> <sup>x</sup> context of price competition between firms with increasing marginal costs. The price competition model can give interesting results if used in the context of generation capacity constraints and increasing marginal costs, but these results must be interpreted carefully, since in this model every player assumes that the price decisions of his competitors are weakly linked to his own decision.

The supply function model, where generators bid functions linking the price to their output, can also constitute a credible alternative and a good compromise between Cournot and Bertrand competition in a highly decentralized market, where the prices of the transactions are not public and large transactions are likely to be made at different prices than smaller ones. Therefore, in a decentralized market, we are likely to observe a combination of Bertrand competition and supply function competition in different geographically and temporally localized sub-markets.

However, none of the models we discussed takes into consideration the repeated nature of the interactions between the players. When this interaction is periodic, and especially in a centralized scheme where the prices are public, inter-temporal Nash strategies in which tacit collusion could be enforced by retaliation threats is a credible alternative that must be investigated. An example is given in Section 4.2.

## 4. Market power in small networks

## 4.1. An example of supply curÕe equilibrium: existence and stability of static Nash equilibrium

To illustrate static Nash equilibrium and its dynamic stability, we consider the case of an inelastic load L with a demand $q _ { L }$ buying power from two generators G1 and G2 with quadratic cost functions:

$$
C _ {i} = b _ {i} q _ {i} + a _ {i} q _ {i} ^ {2}, \qquad i = 1, 2,\tag{16}
$$

where $q _ { i }$ is the output of generator i.The two generators are a duopoly and are assumed to compete by providing linear <sup>4</sup> supply functions:

$$
P _ {i} = x _ {i} \frac {f C _ {i}}{f q _ {i}}, \qquad i = 1, 2 \mathrm{or},\tag{17}
$$

$$
P _ {i} = x _ {i} \big (b _ {i} + 2 a _ {i} q _ {i} \big), \qquad i = 1, 2\tag{18}
$$

where $x _ { i }$ is a strategic variable set by player i. Without transmission constraints, the market clears at a unique equilibrium price p so that:

$$
q _ {L} = q _ {1} + q _ {2}.\tag{19}
$$

Equalities 16 to 19 yield: Ž . Ž .

$$
q _ {i} = \frac {1}{2} \frac {- x _ {i} b _ {i} + x _ {j} b _ {j} + 2 q _ {L} x _ {j} a _ {j}}{a _ {i} x _ {i} + a _ {j} x _ {j}}, \quad i \neq j.\tag{20}
$$

Knowing the quantity functions, and, therefore, the price as a function of the strategic variables, it is easy to calculate $\pi ( x _ { 1 } , x _ { 2 } ) .$ , the profits of the generators as a function of their strategic variables.

For the purposes of simulations, we have used the software Maple V to derive the reactions functions R1 and R2, the unique static Nash equilibrium $\left[ x _ { 1 } * , x _ { 2 } * \right]$ , and the module $\mathbf { ( { \mathrm { d e t } } A ) ^ { 1 / 2 } }$ of the eigenvalues of matrix A as defined in Section 2. <sup>5</sup>

$$
R _ {i} = \left(\frac {2 q _ {L} a _ {j} ^ {2} + a _ {j} b _ {j}}{2 a _ {i} a _ {j} q _ {L} + b _ {j} a _ {i} + 2 a _ {j} b _ {i}}\right) x j + \left(\frac {2 a _ {j} a _ {i} q _ {L} + a _ {j} b _ {i} + b _ {j} a _ {i}}{2 a _ {i} a _ {j} q _ {l} + b _ {j} a _ {i} + a _ {j} b _ {i}}\right), \qquad i \neq j,\tag{21}
$$

$$
x _ {i} * = \frac {1}{2} \frac {2 q _ {L} a _ {j} ^ {2} + 2 a _ {j} q _ {L} + a _ {i} b _ {i} + b _ {j} a _ {i} + 2 a _ {j} b _ {i}}{b _ {j} a _ {i} + a _ {j} b _ {i}}, \quad i \neq j,\tag{22}
$$

$$
\left(\det \mathbf {A}\right) ^ {1 / 2} = \left(\frac {\left(2 a _ {1} a _ {2} q _ {L} + a _ {2} b _ {1}\right) \left(2 a _ {1} a _ {2} q _ {L} + a _ {1} b _ {2}\right)}{\left(2 b _ {2} a _ {1} + \left(2 a _ {1} a _ {2} q _ {L} + a _ {2} b _ {1}\right)\right) \left(\left(2 a _ {1} a _ {2} q _ {L} + a _ {1} b _ {2}\right) + 2 b _ {2} a _ {2}\right)}\right) ^ {1 / 2}.\tag{23}
$$

This last term is smaller than 1 if the coefficients $a _ { 1 } , a _ { 2 } , b _ { 1 } , b _ { 2 }$ are strictly positive.

We can conclude that a unique Nash equilibrium exists for this type of competition and that this equilibrium is always stable if the coefficients of the quadratic cost functions are positive.

## 4.2. Bertrand competition with n symmetric players: static and intertemporal Nash equilibria

We are considering here a simple model similar to that of Ref. 2 where<sup>w</sup> <sup>x</sup> n generators, with constant marginal costs c and individual production capacities k, are facing a demand $q = a - p _ { ; }$ , where $p$ is the price and a is a coefficient larger than c. <sup>6</sup> The generators are competing by prices in an infinitely repeated game. In Ž . <sup>7</sup> a one-stage game, the equilibrium would be a Bertrand–Nash equilibrium BNE of pure or mixed strategies. In the repeated game, $S *$ is a set of strategies $[ S _ { 1 } * , \ldots , S _ { n } * ]$ for players 1 to $n$ that consist of betting the monopoly price as long as all other players do the same, and sticking to the Nash bet of the single stage game after observing any deviation. If S) is an inter-temporal Nash equilibrium as defined in Section 2, we say that the players can tacitly collude at the monopoly price. At every stage of the repeated game, if generator i thinks that the other generators are playing the strategies $S _ { j } *$ , he will have to choose between colluding by bidding the monopoly price and sharing the demand with the others, defecting by bidding a price that is slightly under the monopoly price and producing at full capacity, or playing the one-stage Bertrand Nash strategy if he is expecting other generators to do the same. When the profits from defecting in one period are smaller than the discounted future profits that a generator will lose by defecting, he will choose to collude if no one has defected until now but he will bet the BNE bets if anyone has defected because he knows that his competitors will follow their strategies $S _ { j } *$ , and do the same. Therefore, in this case, the strategy $S _ { i } *$ is his optimal strategy and $S *$ is a Nash inter-temporal equilibrium that satisfies Eq. 15 . WhenŽ . r is the annual discount rate, T the period between two interactions, C the profit from colluding, D the profit from defection and B the profits at the BNE, tacit collusion is an inter-temporal Nash equilibrium if:

![](/api/attachments/NYF2FASV/fulltext/images/4d18f2fb053ad66d15ab2e4d54e624b08bebc76bbe63a5d25c9b961fd01b659e.jpg)

$$
D (n, k) - C (n, k) \leq \frac {C (n , k) - B (n , k)}{e ^ {r T} I}.\tag{24}
$$

It is clear from Eq. 30 that the periodŽ . T between two interactions will determine whether the strategies S) are Nash strategies and whether we are likely to observe tacit collusion at the monopoly price. It is shown in Ref. <sup>w</sup> <sup>x</sup> 13 that tacit collusion is not sustainable for any values of k and n if T satisfies:

$$
T? \frac {\ln (2)}{r}.\tag{25}
$$

In other words, for any number of generators of any size facing any linear demand and for a discount rate of 10%, contracts for delivery of electric power during 7 years or more should always help hinder collusive behavior. <sup>8</sup> On the other hand, spot markets, where the period between two interactions is very small, are likely to encourage collusion; this issue is discussed in Ref. 13 .<sup>w</sup> <sup>x</sup>

## 5. Strategic behavior due to transmission constraints

We have seen in Section 4 some examples where a reduced number of players interacting in a small market can raise the price above the competitive levels and therefore reduce the social welfare. Transmission constraints isolate a reduced number of players in small markets and produce the type of imperfections described previously. However, they can also have a more direct role in creating imperfections in the market for electric power by giving gaming opportunities to some of the players. The goal of this section is to give a sense of the type of strategic behavior that could take place, through a series of very simple simulations of three-bus power systems.

First, to develop an intuitive sense of what could happen, we return to the example described in Section 4.1. The three lines of this network have the same impedance and the line joining the two generators has a thermal constraint of $d / 4$ , where d is the inelastic demand of load L Ž .Fig. 1 . Because of the constraint, the generator G1 can decide to raise its price via raisingŽ $x _ { 1 } )$ and its profits as much as it wants, since the constraint is protecting a minimal output $q _ { 1 }$ of at least $d / 8 .$ . Generator G2 could do the same. The mere existence of a transmission constraint transforms a duopoly that would have respected this constraint at its equilibrium in a quasi-monopoly. We will now consider the case where the load is elastic and examine the results given by different topologies and transmission network constraints. As in Section 4, the cost functions and the supply functions of the two generators are the following:

![](/api/attachments/NYF2FASV/fulltext/images/143fe4fba2e0b2287e23eb8fb292c790335e2adebe5742fe237a2f4d563abe36.jpg)  
Fig. 2.

$$
\begin{array}{l} C _ {i} = b _ {i} q _ {i} + a _ {i} q _ {i} ^ {2}, \qquad i = 1, 2, \\ p _ {i} = x _ {i} \frac {f C _ {i}}{f q _ {i}}, \qquad i = 1, 2, \end{array}\tag{26}
$$

27 Ž .

The load is elastic and has a utility function:

$$
U = b _ {L} \left(q _ {1} + q _ {2}\right) - a _ {L} \left(q _ {1} + q _ {2}\right) ^ {2}.\tag{28}
$$

The load is assumed to be an aggregation of smaller loads without market power. Its demand function will therefore be:

$$
P _ {L} = b _ {L} - 2 a _ {L} \left(q _ {1} + q _ {2}\right).\tag{29}
$$

In a market without network externalities, the unique market price that makes supply match demand maximizes the apparent social welfare, total utility of the consumers minus the apparent total cost ofŽ . production: $U - x _ { 1 } C _ { 1 } - x _ { 2 } C _ { 2 } \mathrm { o r } ^ { q _ { 1 } + q _ { 2 } } { } _ { 0 } P _ { L } ( q ) \mathrm { d } q - { } ^ { q _ { 1 } } { } _ { 0 } P _ { 1 } ( q ) \mathrm { d } q - { } ^ { q _ { 2 } } { } _ { 0 } P _ { 2 } ( q ) \mathrm { d } q .$ The presence of transmission constraints may not allow such a unique price to exist and the maximum welfare is attained for different prices at different nodes through a coordinating PX that takes the supply function bids of the generators and determines the optimal outputs, or through an appropriate set of trading rules which would make the system attain this optimal scheme through decentralized transactions. The way the outputs are determined is irrelevant to the simulation as long as the outputs and prices are the same. Moreover, whether the lines to be constrained and the outputs of the generators are set by a coordinating power exchange PX organism or indirectly reachedŽ . through an appropriate set of rules for decentralized bilateral or multilateral trading, it is the choice $o f x _ { 1 }$ and $x _ { 2 }$ by the generators that will effectiÕely determine which lines are constrained as well as the optimal outputs $q _ { 1 } ( x _ { 1 } , x _ { 2 } )$ and $q _ { 2 } ( x _ { 1 } , x _ { 2 } )$ . Knowing these functions, the generators deduce their profits as a function of $x _ { 1 }$ and $x _ { 2 }$ . as well as their reaction functions. More specifically, depending on what constraints are active, the analytical formulation of the output functions $q _ { 1 }$ and $q _ { 2 }$ could change. The players will calculate primary reaction functions associated with every type of constrained or unconstrained dispatch. Every player will then build his global reaction function by comparing the profits yielded by his primary reaction functions. These global reaction functions will reflect when a player will choose to constrain the network and when he chooses to leave it unconstrained.

![](/api/attachments/NYF2FASV/fulltext/images/a2f78d13020d8d3231f12837659416cc71a66aebd12f9b265422129ef055bef9.jpg)  
Fig. 3.

![](/api/attachments/NYF2FASV/fulltext/images/9d2953fe15bc904aed929fb0fd018063e13b0dfcb8fe221558069f0d652a4362.jpg)  
Fig. 4.

## 5.1. Topology 1: no loop flows

The line linking G1 and the load has a thermal constraint T Ž . Fig. 2 and therefore,

$$
q _ {1} + q _ {2} \leq T.\tag{30}
$$

In all the simulations, the gray line separates the area where the bids $( x _ { 1 } , x _ { 2 } )$ will lead the line to be operating at its thermal limit constrained area from the area where it would be operating below this limit unconstrainedŽ . Ž area . The solid lines are the reaction functions. R1 and R2 and the dotted lines are the reaction functions as they would have been if the line had no thermal constraint.

![](/api/attachments/NYF2FASV/fulltext/images/dbdd3c70883b0441b7bedc8a87dc0f311c37b3175847254bc656c7defbd603b1.jpg)  
Fig. 5.

![](/api/attachments/NYF2FASV/fulltext/images/eac54eafb95958d7b53729713c071f6c5ddede286be064642e5e8a78d39e7d86.jpg)  
Fig. 6.

When the constraint is relatively low Fig. 3 , the Nash equilibrium is the same as would be obtained withoutŽ . constraints. When the constraint is tightened Fig. 4 , the Nash equilibrium is obtained in the constrained areaŽ . and for higher prices because the generators, having market power, can exploit the constraint more effectively than a price-taker load.

The last case, shown in Fig. 5, is an intermediate case where the unconstrained equilibrium would lie in the constrained area but the prices are not high enough to allow for a constrained equilibrium. We observe a peculiar situation where a continuum of Nash equilibria seems to be sustainable on the boundary separating the constrained from the unconstrained area.

## 5.2. Topology 2: introduction of loop flow

We add in this example an unconstrained line between G2 and the load, giving to G2 a competitive advantage on G1 because of loop flows Fig. 6 . Ž .

To respect the constraint we must have:

$$
\alpha_ {1} q _ {1} + \alpha_ {2} q _ {2} \leq T\tag{31}
$$

with

$$
0 <   \alpha_ {2} <   \alpha_ {1} <   1,\tag{32}
$$

where and $\beta$ reflect the physical characteristics of the network.

In the first simulation Fig. 7 , the first generator had more power to affect the state of the system,Ž . constrained or unconstrained, than G2 because of loop flow. In this example, because the transmission constraint is not very tight, the unconstrained equilibrium is sustainable.

![](/api/attachments/NYF2FASV/fulltext/images/613cb4c17560c0a7073cfd707e37a6a574a1b126727d56b6a391e966ab1dbe9b.jpg)  
Fig. 7.

![](/api/attachments/NYF2FASV/fulltext/images/163683c8c8a526a870e5badd6ece75cc321bf364fbe7adf702724df91dc091d9.jpg)

![](/api/attachments/NYF2FASV/fulltext/images/6e5f8f38ed027c74716ab2b00da9db02ce24fbb456f47756c4b023a6db891406.jpg)  
Fig. 9.

A higher constraint on the network Fig. 8 moves the Nash equilibrium on the boundary separating theŽ . constrained from the unconstrained areas. When we raise the inelasticity of the load $^ { 9 } \left( \mathrm { F i g . 9 } \right)$ , we observe how R2 becomes discontinuous and no longer intersects R1, preventing a static Nash equilibrium from existing. This discontinuity is due to the fact that generator G2, because it has a better strategic location, will prefer not to follow the first generators when the bids of the latter are too low, but rather concentrate on raising the price and the profits from the market share that the constraint is protecting for him. It is mostly notable that in this example, an unconstrained equilibrium exists in the unconstrained area and that it would be a feasible Nash equilibrium if the players did not know of the existence of the constraints. However, because G2 knows that the constraint is protecting a portion of his market share, he will deviate from this equilibrium and try to raise its profit further.

![](/api/attachments/NYF2FASV/fulltext/images/cdd0c37493cd86a62a81a61f3c81f4096648e0e0b8cd19410e44962ee27dcb58.jpg)  
Fig. 10.

## 5.3. Topology 3: two-way constraints

In this example, it is the line linking the two generators that has a thermal limit T imposing two constraints on the system:

$$
\begin{array}{l} \alpha q _ {1} - \beta q _ {2} \leq T, \\ \beta q _ {2} - \alpha q _ {1} \leq T \end{array}\tag{33}
$$

Ž . 34

with

$$
0 <   \beta <   1, 0 <   \alpha <   1,\tag{35}
$$

where and $\beta$ reflect the physical characteristics of the network Fig. 10 .Ž .

When the line linking the two generators is weak, it can be constrained in its two directions, which creates two constrained areas: ‘Constrained area 1’ where Eq. 33 is an equality and ‘Constrained areaŽ . $_ { 2 } \cdot$ where Eq. Ž . Ž . 34 is an equality Fig. 11 .

The generators now have new opportunities for strategic bidding: in the last example, only one generator had a market share protected by loop flow and constraints. Here, both do; and that is why we observe discontinuities in both reaction functions in Fig. 11. Nevertheless, the constraint is not very restrictive in this example and the reaction curves intersect in the unconstrained area at the unconstrained Nash equilibrium.

However, with a tighter transmission constraint, as in Fig. 12, or a more inelastic load, as in Fig. 13, the reaction functions may no longer intersect, even if, once again, the unconstrained equilibrium where the marketŽ would settle if the generators did not know the existence of the constraint lies in the feasible unconstrained. area.

![](/api/attachments/NYF2FASV/fulltext/images/3465ccf02425f23f16d8d9955b6d4db952e97e74778ae8530064345a4aa69da2.jpg)  
Fig. 11.

![](/api/attachments/NYF2FASV/fulltext/images/21108ef2eea7b4f2f169cc69870ad8f25f729d5335bb61a706ea53eb78936fbd.jpg)  
Fig. 12.

Interpreting what would happen in reality when the reaction functions do not intersect and where there is no static Nash equilibrium is not easy. A first basic interpretation might be that every generator will react myopically to the bids of his competitors, observing these bids, reacting accordingly to its reaction function, and leading the market to an unstable situation. In this case, the examples developed above seem to indicate that the bids will always remain above the bids of the unconstrained Nash equilibrium, independent of the physical feasibility of this equilibrium. This is due to the fact that in the cases where the reaction functions did not intersect, at least one of them lies completely above the bet of the unconstrained equilibrium, the other having either the same property or being monotonic.

A more sophisticated interpretation is that the generators will play mixed strategies, i.e., that their bets will follow a random process maximizing their expected profits, and also leading to instability. Nevertheless, myopic instability or mixed strategy equilibria may not be sustainable in the long term in a repeated game where continuous interactions and maybe the fear that a high instability will lead the regulator to investigate andŽ change the rules could make a more sophisticated inter-temporal Nash equilibria sustainable. In all these. scenarios, the load seems to be worse off because the generators have more market power and more opportunities for strategic bidding, which are created by thermal limits on some of the transmission lines.

![](/api/attachments/NYF2FASV/fulltext/images/1f73adfe6152f8735b530a34cfeeb53241c91b72d4beb0f28e1ba7aa48400368.jpg)  
Fig. 13.

## 6. Conclusions

Transmission constraints and loop flow create a double threat to the emergence of a competitive electricity market. When these constraints are too tight, they separate sub-markets from the rest of the network and raise the locational market power of generators located there, even if these markets are still linked by other unconstrained lines to the rest of the network 13 . The reduction in the number of players in interaction leads to<sup>w</sup> <sup>x</sup> higher prices as usually recognized, and sometimes to tacit collusion due to repeated periodic interactions as seen in Section 4. But transmission lines can also lead to inefficient behavior even they are not supposed to be constrained in a competitive framework. A transmission line that may have a reasonable capacity to allow normal operations of the network could become a source of inefficiencies and higher market prices if the generators realize that they can make profits by strategically constraining it. A fairly inelastic load on a network with comfortable transmission capacities, or a more elastic load and low transmission capacities, may give the generators the opportunity to strategically constrain the network in order to exploit their protected market share with very high bids. The load elasticity, which is known to affect the prices at the unconstrained equilibrium and to raise the market power of the players, is found to also be capable of affecting their ability to strategically constrain the network, create potential instabilities, and raise the average prices. If the regulators fail to make the loads more elastic through the appropriate price signals, the network might have to be largely overbuilt, with all the economic and environmental problems that this might cause. Future research should focus on whether a policy for expanding the grid, that gives appropriate incentives to overbuild a line when market power is used before the expansion, would constitute a credible threat against strategic bidding and excessive abuse of market power. Such a strategy could paradoxically save the network from being overbuilt 13 . Quantitative analysis must also be conducted to determine the significance of a problem that we have only shown to be conceptually possible. More complex networks must be used, with realistic data and nonlinear supply functions.

## Acknowledgements

The authors greatly appreciate the financial support given by the MIT Consortium for Transmission Provision and Pricing that has made this research possible. Discussions with Professor John Tsitsiklis at MIT, Professor Francisco Galiana at McGill University and Dr. Richard Green at Cambridge University were important as the authors plowed through this new terrain.

## References

<sup>w</sup> <sup>x</sup> 1 M. Aoki, Optimal Control and System Theory in Dynamic Economic Analysis, North-Holland, 1976, p. 123.

<sup>w</sup> <sup>x</sup> 2 W. Brock, J. Schneikman, Price setting supergames with capacity constraints, Review of Economic Studies 11 1895 371–382.Ž .

<sup>w</sup> <sup>x</sup> 3 F. Edgeworth, La Teoria Pura del Monopolio, Giornale degli Economisti 40 1897 13-3 in: F. Edgeworth Ed. , The Pure Theory ofŽ . Ž Ž . Monopoly, Papers Relating to Political Economy, Vol. 1, Macmillan, London, 1925 ..

<sup>w</sup> <sup>x</sup> 4 R. Green, D. Newberry, Competition in the British electric spot market, Journal of Political Economy 100 1992 929–953.Ž .

<sup>w</sup> <sup>x</sup> 5 W. Hogan, Contract networks for electric power transmission, Journal of Regulatory Economics 4 1992 211–242. Ž .

<sup>w</sup> <sup>x</sup> 6 P.D. Klemperer, M.A. Meyer, Supply function equilibria in oligopoly under uncertainty, Econometrica 57 1989 1243–1277. Ž .

<sup>w</sup> <sup>x</sup> 7 D. Kreps, J. Schneikman, Quantity pre-commitment and Bertrand competition yield Cournot outcomes, Bell Journal of Economics 14 Ž .1983 326–337.

<sup>w</sup> <sup>x</sup> 8 S. Oren, Economic inefficiency of passive transmission rights in congested electricity systems with competitive, The Energy Journal 18 Ž . Ž . 1 1997 63–83.

<sup>w</sup> <sup>x</sup> 9 E. Ramis, Cl. Deschamps, J. Odoux, Cours de Mathematiques Speciales, Masson, Paris, 1988.´ ´

<sup>w</sup> <sup>x</sup> 10 H. Singh, S. Hao, A. Papalexopoulos, Power Auctions and Network Constraints, IEEE, 1997, pp. 608–614.

<sup>w</sup> <sup>x</sup> 11 J. Tirole, The Theory of Industrial Organization, The MIT Press, 1988.

<sup>w</sup> <sup>x</sup> 12 C.D. Wolfram, Measuring Duopoly Power in the British Electricity Market, MIT Department of Economics, WP, November 1995. <sup>w</sup> <sup>x</sup> 13 Z. Younes, M. Ilic, Transmission System Constraints in Non-Perfect Electricity Market, Proc. of 18th Annual North American Conference USAEE<sup>r</sup>IAEE, 1997, pp. 256–265.

Marija Ilic is a Senior Research Scientist in the Department of Electrical Engineering and Computer Science at the Massachusetts Institute of Technology, where she teaches several graduate courses in electric power systems and heads research in the same area. She has twenty years of experience in teaching and research in this area. Prior to coming to MIT in 1987, she was an Assistant Professor at Cornell University, and tenured Associated Professor at the University of Illinois at Urbana-Champaign. Her main interest is in the system aspects of operations, planning and economics of electric power systems.

Ziad Younes is a Lebanese engineer and economist. He has graduated from the Ecole Polytechnique in Paris, and has a Master in Technology and Policy from the Massachusetts Institute of Technology. He has a D.E.A. in Industrial Organization from the University of Paris IX and is currently a PhD student there. Ziad’s interest is mainly focused on how to deal with market imperfections in a deregulated electric power industry.

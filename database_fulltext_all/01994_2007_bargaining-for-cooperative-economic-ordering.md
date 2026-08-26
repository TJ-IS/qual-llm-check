---
otero_id: 1994
otero_key: "SVDE2C8B"
title: "Bargaining for cooperative economic ordering"
authors: "Stefan Minner"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.05.016"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Bargaining for cooperative economic ordering

Stefan Minner<sup>\*</sup>

University of Mannheim, Business School, Schloss, 68131 Mannheim, Germany

Available online 7 July 2005

## Abstract

This paper analyzes horizontal cooperations between organizations that have the opportunity to jointly replenish material requirements. Two mechanisms are investigated, the search for short-term cooperations (e.g., via electronic markets) and longterm cooperations. The operations management context used in this paper is the economic order quantity model. Collaboration is analyzed by using bargaining concepts from non-cooperative and cooperative game theory. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Cooperative sourcing; Economic order quantities; Game theory

## 1. Introduction

Collaboration with suppliers and customers offers the potential to realize substantial cost reduction and service improvement benefits. This represents one area in supply chain management, which is the design and control of relations with supplier and customers with regard to information and material flows [34]. Decentralized decisions in a supply chain create a potential of self-interest and conflict. A recent direction in quantitative supply chain research investigates channel coordination, i.e., the design of contracts between individual decision-makers (e.g., a buyer and a seller) in the chain such that the difference between the outcome of a centralized solution made by a single decision-maker for the entire chain and decentralized decisions is avoided as much as possible [2,6,7,14,15]. Game theory is the main instrument to analyze the interaction between the individual decision-maker’s problems; see [4] for a recent review on non-cooperative and cooperative concepts.

The aforementioned research investigates vertical relations in supply chains, whereas this paper considers a horizontal problem associated with the organization and optimization of supply. Many papers analyze the horizontal aspect of market competition, e.g., [1,3,18]. The horizontal aspect in this paper is that several independent organizations have requirements for the same part to manufacture their main product. They are situated at the same level in the value chain. Cooperation between these organizations offers cost savings by having a larger (joint) sourcing quantity, which increases their negotiation power towards suppliers, their ability to make use of favorable quantity discounts and to achieve economies of scale, or a coordinated organization of supply might reduce their overall transaction costs [5]. One central issue for the analysis of such sourcing cooperations is (as for vertical supply chain cooperations) the measurement of potential benefits of cooperation (e.g., the cost that a single purchasing operation with the combined volume would be able to achieve) and how to allocate these benefits among the parties involved. A different aspect of horizontal cooperations in inventory and replenishment is the exchange of inventories in emergency situations by transshipments [29].

In order to investigate the initiation of horizontal collaboration, we use bargaining models, which represent game situations between the decision-makers (players) involved (for an overview on negotiation analysis, see [27]). The players have a common interest to cooperate, i.e., there are positive benefits of joint supply operations, but there exist conflicting interests about how to cooperate, i.e., how to allocate the benefits of cooperation. Bargaining concepts model the process of reaching an agreement (or not) in order to unlock the benefits of cooperative supply.

The procurement situation under consideration in this paper is the traditional economic order quantity model. There exist benefits from having a larger requirements volume (economies of scale), i.e., this enables shorter cycle times and lot sizes increase with the square root of the number of aggregated units (for the case of identical items) [16]. One instrument to seek for sourcing cooperation is the internet, i.e., B2B electronic marketplaces where organizations can actively seek partners for purchasing requirements or (passively) accept offers being made by others. The outcome for a player heavily depends on the design of these markets, especially the design of the underlying bargaining rules. This is similar to the design of (vertical) procurement auctions, which also uses concepts from game theory to analyze the underlying decision problems and their interaction (e.g., see [8]). Often, the change of the rules of the game (or selecting the market place that offers the most favorable rules for the respective firm) offers higher benefits than playing a given game in the best possible way [22]. Another issue, besides actively or passively seeking cooperations, is the question whether to seek on spot (internet) markets with many potential partners and exploiting the benefits of competition between others or whether higher benefits can be achieved from creating longterm purchasing cooperations with a selected partner [13,26]. Models which address the purchasing problem with special purchasing opportunities are discussed, e.g., in [19,30]. For a strategic discussion of the difference between group purchasing and cooperative sourcing as well as for a literature review, see [9]. In the following, we will discuss different settings for the bargaining process to develop sourcing agreements in order to provide some (initial) decision support.

The paper is organized as follows. In Section 2, we summarize the assumptions of the economic order quantity model based on a net-present-value analysis (e.g., [33] for a recent discussion), which is the basis for the later analysis as it represents the status quo for the decision-makers before cooperation, respective their outcome when not reaching an agreement how to cooperate. In Section 3, we analyze a bargaining solution with one active player who makes an offer to a second player. The impact of having several potential partners (i.e., the size of an electronic market for cooperations) and the impact of information asymmetry are discussed. In addition, an equilibrium type of model without pre-assigned roles for releasing or receiving offers is analyzed. In Section 4, we investigate bargaining for long-term cooperation. The main difference between short-term and long-term cooperative sourcing is that replenishment processes, especially the timing and sizes of orders, can be better synchronized and therefore higher benefits be achieved from the latter alternative. In detail, we analyze a Nash bargaining solution. Thereafter, we compare the two types of cooperation and determine a critical market size, which represents the level of indifference between the two alternatives. The paper concludes with a summary of the main strategic implications of the analysis and points outs several lines for future research.

## 2. Model assumptions

Each decision-maker in the following models operates in an environment that can be described by the economic order quantity (EOQ) model. Unless stated otherwise, we assume that all decision-makers are identical with respect to demand rates and cost structure. A continuous demand of rate d has to be satisfied; backorders are not permitted. An order of size Q is placed with an external supplier at time instants $t = k T , k = 0 , 1 , 2 , . . .$ . and $Q { = } d T$ whenever inventory reaches the level zero. The respective lead time is assumed to be zero, i.e., an order instantaneously increases the inventory level by the ordered amount. In order to value the current and an infinite number of future decisions, we use a net-present-value (NPV) instead of an average cost approach. In a net-presentvalue, discounted cash-flow-oriented framework each order is associated with two kinds of payments, a setup cost A (payment being independent of the order size $\mathcal { Q } , \mathrm { e . g . }$ , a fixed transportation charge) and a variable purchasing price c per unit. With each order, the total payment is $A + c Q$ . Using a continuous interest rate of $r ,$ the net-present-value of the infinite stream of payments is

$$
\begin{array}{l} \text { NPV } = (A + c Q) + (A + c Q) \mathrm{e} ^ {- r T} + \ldots \\ \qquad + (A + c Q) \mathrm{e} ^ {- r k T} + \ldots \\ \qquad = (A + c Q) \sum_ {k = 0} ^ {\infty} \mathrm{e} ^ {- r k T} = \frac {A + c Q}{1 - \mathrm{e} ^ {- r Q / d}}. \end{array}\tag{1}
$$

This present value formulation excludes out-ofpocket inventory holding costs. However, the extension is straightforward. The optimal order quantity is obtained from

$$
\begin{array}{l} \frac {\mathrm{dNPV}}{\mathrm{d} Q} = \frac {c (1 - \mathrm{e} ^ {- r Q / d}) - (A + c Q) \frac {r}{d} \mathrm{e} ^ {- r Q / d}}{(1 - \mathrm{e} ^ {- r Q / d}) ^ {2}} = 0 \\ \Leftrightarrow \mathrm{e} ^ {r Q ^ {*} / d} - 1 = \frac {r (A + c Q ^ {*})}{d c}. \end{array}\tag{2}
$$

Condition (2) has a single positive solution for $Q ^ { * }$ because for $Q = 0$ the left hand side equals 0 and the right hand side equals $r A / ( d c ) { > } 0$ . Further, the left hand side increases with slope $( r / d ) \mathrm { e } ^ { r Q / d } \geq r / d$ and the right hand side with $r / d .$ . The second order condition yields

$$
\begin{array}{c} \frac {\mathrm{d} ^ {2} \mathrm{NPV}}{\mathrm{d} Q ^ {2}} = \frac {- 2 c \frac {r}{d} \mathrm{e} ^ {- r Q / d}}{(1 - \mathrm{e} ^ {- r Q / d}) ^ {2}} + \frac {r}{d} (A + c Q) \mathrm{e} ^ {- r Q / d} \\ \times \frac {\frac {r}{d} (1 + \mathrm{e} ^ {- r Q / d})}{(1 - \mathrm{e} ^ {- r Q / d}) ^ {3}}. \end{array}\tag{3}
$$

For the solution $Q ^ { * }$ that satisfies (2), we need

$$
\begin{array}{l} - 2 c \Big (1 - \mathrm{e} ^ {- r Q / d} \Big) + (A + c Q) \frac {r}{d} \Big (1 + \mathrm{e} ^ {- r Q / d} \Big) \geq 0 \\ \Leftrightarrow - 2 c \Big (1 - \mathrm{e} ^ {- r Q / d} \Big) \geq - c \Big (\mathrm{e} ^ {r Q / d} - 1 \Big) \\ \times \Big (1 + \mathrm{e} ^ {- r Q / d} \Big) \Leftrightarrow \Big (1 - \mathrm{e} ^ {- r Q / d} \Big) \Big (1 + \mathrm{e} ^ {- r Q / d} \Big) \\ \geq 2 \Big (1 - \mathrm{e} ^ {- r Q / d} \Big) \mathrm{e} ^ {- r Q / d} \end{array}
$$

to ensure a minimum which is satisfied since $\mathrm { e } ^ { - r Q / d }$ $\leq 1$ for all positive values of $\mathcal { Q } .$ . Note that the solution to Eq. (2) can only be obtained numerically. In order to find a closed form expression, it is common practice in inventory research to use a second order Taylor approximation for the exponential function $( \mathrm { e } ^ { x } \approx$ $1 + x + x ^ { 2 } / 2 )$ , and this yields the well-known square root formula for the economic order quantity (e.g., see [31]). The rationale behind this approximation is the degree of accuracy for the incorporation of interest rate effects, e.g., a first order approximation would imply an interest factor $1 + r T ,$ a second order approximation $1 + r T + 0 . 5 r ^ { 2 } T ^ { 2 }$ The accuracy of such approximations increases if the product of interest rate r and inventory cycle $T { = } Q / d$ becomes sufficiently small, that is, with small interest rates and/or large order frequencies.

$$
Q ^ {*} \approx \sqrt {\frac {2 A d}{r c}}.\tag{4}
$$

The traditional average cost analysis yields a reasonable approximation of the net-present-value approach if the holding cost rate is set equal to $r c .$ The exact cost present value for the optimal ordering decision using (2) is

$$
\mathrm{NPV} ^ {*} = \frac {A + c Q ^ {*}}{1 - \mathrm{e} ^ {- r Q ^ {*} / d}} = \frac {c d}{r} \mathrm{e} ^ {r Q ^ {*} / d} = A + c Q ^ {*} + \frac {c d}{r}.\tag{5}
$$

Because the demand stream has to be satisfied by assumption, the cost for procuring items just-in-time to satisfy demands (equal to $c d / r )$ are not relevant to the ordering decisions, i.e., the total relevant costs are only $A + c Q ^ { * }$ . This analysis is used as a building block in the following sections.

## 3. One-time cooperation

Assume that several decision-makers have the opportunity to cooperate by placing joint orders instead of individually purchasing their requirements.

## 3.1. Stackelberg game

As a first step, let us consider a cooperation with two decision-makers, in the following named players 1 and 2 at an arbitrary point in time. Player 1 has zero inventory and therefore needs to place a replenishment order. Player 1 makes an offer for a joint replenishment to player 2. The offer consists of proposing a share of the fixed replenishment cost $\scriptstyle A = A _ { 1 } + A _ { 2 }$ where $A _ { i }$ is player i’s share. If player 2 accepts the offer, a joint order is placed with an exogeneous supplier and both players receive their desired quantity. If the offer is rejected, player 1 places an individual order. For simplicity of presentation, we do not explicitly model the physical process of delivery and material allocation.

The information that is available to both players for their decision-making is the cost structure, which is further assumed to be identical (similar business); however, the demand rate and the inventory level of the other decision-maker is unknown. If all decisionmakers replenish according to the same EOQ model, the information player 1 has about the inventory level y of player 2 is uniformly distributed on the interval [0, Q\*]. Both players assume that this is a one-time cooperation, that is, after a potential cooperation they will return to their individual EOQ replenishment pattern.

This decision problem can be formulated as a Stackelberg game with asymmetric information. Player 1 who actively seeks a cooperation by making an offer to cooperate acts as a leader (who has the power to make the proposal and can anticipate the other player’s reaction) and player 2 is a follower who only has the choice to accept or reject the proposal. In the following two subsections, we describe the respective decision problems. Note that the leader could improve his performance by making use of the revelation principle, i.e., by offering a menu of different contracts (for different inventory levels) to the follower such that the follower will reveal information about the inventory level.

## 3.1.1. The follower’s decision problem

Player 2 who receives the offer to place a joint order faces two decisions: (1) whether to accept or reject the offer and (2) if accepting, how many units to order. If the offer to place a single joint order is rejected and the current inventory level is $y \in [ 0 , Q ] ,$ future replenishments of size Q will take place at times $t { = } y / d { + } k T$ with k = 0, 1, 2, . . . and $T { = } Q / d .$ The net-present-value of the associated stream of payments is

$$
\begin{array}{l} \mathrm{NPV} _ {2} ^ {\mathrm{no}} = (A + c Q) \mathrm{e} ^ {- r y / d} + (A + c Q) \mathrm{e} ^ {- r (y / d + T)} \\ \qquad + \ldots + (A + c Q) \mathrm{e} ^ {- r (y / d + k T)} + \ldots \\ \qquad = (A + c Q) \mathrm{e} ^ {- r y / d} \sum_ {k = 0} ^ {\infty} \mathrm{e} ^ {- r k Q / d} \\ \qquad = \mathrm{e} ^ {- r y / d} \frac {A + c Q}{1 - \mathrm{e} ^ {- r Q / d}}. \end{array}\tag{6}
$$

Since this is the same NPV as in the standard model shown in Section 2 (multiplied by a constant factor $\mathrm { e } ^ { - r y / d } )$ , the optimal decision is, not surprisingly, to order the economic order quantity after y has been used and the inventory level is zero.

When accepting the offer, the question is how many units to order with this single joint replenishment. A replenishment of size $\tilde { \varrho }$ takes place at time t = 0 and future orders of size Q at $\scriptstyle t = ( y + \tilde { Q } + k Q ) / d ,$ $k = 0 , 1 , 2 , . . .$

The net-present-value of accepting the offer to cooperate is

$$
\mathrm{NPV} _ {2} ^ {\mathrm{co}} = A _ {2} + c \tilde {Q} + \mathrm{e} ^ {- r (y + \tilde {Q}) / d} \frac {A + c Q}{1 - \mathrm{e} ^ {- r Q / d}}.\tag{7}
$$

The optimality conditions are

$$
\begin{array}{l} \frac {\partial \mathrm{NPV} _ {2} ^ {\mathrm{co}}}{\partial Q} \\ = \mathrm{e} ^ {- r (y + \tilde {Q}) / d} \cdot \frac {c (1 - \mathrm{e} ^ {- r Q / d}) - \frac {r}{d} (A + c Q) \mathrm{e} ^ {- r Q / d}}{(1 - \mathrm{e} ^ {- r Q / d}) ^ {2}} \\ = 0, \end{array} \tag {8}
$$

$$
\frac {\partial \mathrm{NPV} _ {2} ^ {\mathrm{co}}}{\partial \tilde {Q}} = c - \frac {r}{d} \cdot \mathrm{e} ^ {- r (y + \tilde {Q}) / d} \frac {A + c Q}{1 - \mathrm{e} ^ {- r Q / d}} = 0.\tag{9}
$$

After rearranging terms from both conditions, we find

$$
\frac {d c}{r} \mathrm{e} ^ {r Q / d} = \frac {A + c Q}{1 - \mathrm{e} ^ {- r Q / d}},\tag{10}
$$

$$
\frac {d c}{r} \mathrm{e} ^ {r (\tilde {Q} + y) / d} = \frac {A + c Q}{1 - \mathrm{e} ^ {- r Q / d}}.\tag{11}
$$

Exploiting the equality of both right hand sides, we find that ${ \tilde { Q } } ^ { * } { = } Q ^ { * } { - } y$ . Thus, the second player uses the cooperative replenishment quantity to order up to the maximum (EOQ) inventory level. Since condition (10) is the same as (2) in Section 2, the standard economic order quantity $Q ^ { * }$ for future orders still applies. The decision for player 2 whether to cooperate or not depends on the comparison of the netpresent-values $\mathrm { N P V } _ { 2 } ^ { \mathrm { c o } }$ of accepting and $\mathrm { N P V } _ { 2 } ^ { \mathrm { n o } }$ of rejecting the offer. Cooperation provides a smaller cost present value if

$$
\begin{array}{l} A _ {2} + c \tilde {Q} + \mathrm{e} ^ {- r (y + \tilde {Q}) / d} \frac {A + c Q}{1 - \mathrm{e} ^ {- r Q / d}} <   \mathrm{e} ^ {- r y / d} \frac {A + c Q}{1 - \mathrm{e} ^ {- r Q / d}} \\ \Leftrightarrow A _ {2} + c \tilde {Q} <   \frac {A + c Q}{1 - \mathrm{e} ^ {- r Q / d}} \mathrm{e} ^ {- r y / d} \left(1 - \mathrm{e} ^ {- r \tilde {Q} / d}\right) \end{array} \tag {12}
$$

Inserting from (11), we find that cooperation is beneficial if

$$
\frac {(A _ {2} + c \tilde {Q}) r}{d c} <   e ^ {r \tilde {Q} / d} - 1.\tag{13}
$$

Note that an equality in (13) would provide condition (2) of determining the optimal order quantity for a setup cost of size $A _ { 2 }$ . Using the second order Taylor approximation in (13), we find that cooperation is preferred if

$$
\tilde {Q} ^ {*} = Q ^ {*} - y > \sqrt {\frac {2 d A _ {2}}{r c}} = \sqrt {\frac {A _ {2}}{A}} Q ^ {*} =: Q _ {2} ^ {*}.\tag{14}
$$

Cooperation is beneficial if the quantity that is required to fill the gap ${ \tilde { Q } } ^ { * } { = } Q ^ { * } { - } y$ between the current inventory level y and the EOQ is larger than the optimal ordering quantity given that $A _ { 2 }$ would be the regular setup cost for each replenishment. Summarizing, the decision rule for player 2 as a function of the sharing offer $A _ { 2 }$ is: If $y { \le } Q ^ { * } { - } Q _ { 2 } ^ { * }$ , accept the offer, otherwise reject it.

## 3.1.2. The leader’s decision problem

The decision problem for player 1 is to set $A _ { 2 }$ such that its own cost present value is minimized.

For the same reason as analyzed for player 2, player 1 will not adjust its order quantity for the single joint replenishment because of the assumption that it is a one-time cooperation. If there are repeated opportunities, then there is an incentive for a reduced order quantity in order to exploit cooperation benefits more frequently. Further, player 1 has no gain in information from delaying an offer and, therefore, it is optimal to place an offer for cooperation whenever the inventory level is equal to zero. For the decision upon the sharing offer, the optimal reaction of player 2 is incorporated. The cost function for player 1 in case player 2 accepts the offer $( y \le Q ^ { * } - Q ^ { * } )$ is

$$
\begin{array}{r l} \mathrm{NPV} _ {1} ^ {\mathrm{co}} & = A - A _ {2} + c Q + \mathrm{e} ^ {- r Q / d} \frac {A + c Q}{1 - \mathrm{e} ^ {- r Q / d}} \\ & = \mathrm{NPV} - A _ {2} \end{array}\tag{15}
$$

whereas if the offer is rejected $( y > Q ^ { * } - Q _ { 2 } ^ { * } )$ the cost present value is $\mathrm { { N P V } _ { 1 } ^ { n o } = N P V . }$ If the leader had perfect information about the follower’s inventory level, he would propose a share where player 2 is indifferent (or just little in favor of accepting) between accepting or rejecting. However, player 1 has incomplete information about the demand rate and the inventory level of player 2 and therefore has to use a prior distribution on demand rate and the inventory level, which we assume is uniform on [0, Q\*]. Let $f ( Q )$ be the prior distribution that player 1 has about player 2’s order size. The expected present value $\mathrm { E N P V } ( A _ { 2 } )$ of making an offer $A _ { 2 }$ is obtained from weighting the cost of cooperation with the probability that the inventory level of player 2 is less than or equal to the critical level and the cost of no cooperation with the probability that the inventory level is above the critical level.

$$
\begin{array}{r l} P (y \leq Q ^ {*} - Q _ {2} ^ {*}) & = \int_ {0} ^ {\infty} f (Q ^ {*}) \int_ {0} ^ {Q ^ {*} - Q _ {2} ^ {*}} \frac {1}{Q ^ {*}} \mathrm{d} s \mathrm{d} Q ^ {*} \\ & = \int_ {0} ^ {\infty} f (Q ^ {*}) \left(1 - \sqrt {\frac {A _ {2}}{A}}\right) \mathrm{d} Q ^ {*} \\ & = 1 - \sqrt {\frac {A _ {2}}{A}}. \end{array}\tag{16}
$$

Then the expected present value is

$$
\operatorname{ENPV} \left(A _ {2}\right) = \operatorname{NPV} - A _ {2} \left(1 - \sqrt {\frac {A _ {2}}{A}}\right).\tag{17}
$$

Because (17) is convex in $A _ { 2 } ,$ the optimal present value minimizing offer $A _ { 2 }$ follows from

$$
\frac {\mathrm{dENPV} \left(A _ {2}\right)}{\mathrm{d} A _ {2}} = - 1 + \sqrt {\frac {A _ {2}}{A}} + \frac {1}{2} \sqrt {\frac {A _ {2}}{A}} = 0 \Leftrightarrow A _ {2} ^ {*} = \frac {4}{9} A.\tag{18}
$$

As a result, the player that makes the offer to cooperate has to keep 5/9 of the setup cost and will pass on 4/9 to his counterpart. The asymmetric allocation is due to the need to compensate player 2 for ordering sooner than necessary.

Instead of using Taylor-series approximation, the exact cost sharing offer can be determined, however, only numerically. The offer $A _ { 2 } ^ { * }$ that maximizes the transfer payments $A _ { 2 } \cdot p ( A _ { 2 } )$ with $p ( A _ { 2 } ) { = } 1 { - } Q _ { 2 } { \ast } / Q ^ { \ast }$ is given by

$$
A _ {2} ^ {*} = c (Q ^ {*} - Q _ {2} ^ {*} (A _ {2} ^ {*})) \left(\mathrm{e} ^ {r Q _ {2} ^ {*} (A _ {2} ^ {*}) / d} - 1\right)\tag{19}
$$

where $\mathrm { d } Q _ { 2 } ( A _ { 2 } ) / \mathrm { d } A _ { 2 }$ is obtained from (13) by implicit differentiation and $Q ^ { * }$ can be obtained from (2) and $\boldsymbol { Q } _ { 2 } ^ { * }$ from an equality in (13).

In the following, we test the quality of our approximation using a standard data set of $\scriptstyle A = 5 0 0 , c = 1 0 0 ,$ $d = 1 0 0 , \ r = 0 . 1$ , the parameters A, c and d being varied. In a first set, the demand rate d was varied from $d = 1$ to $d = 1 0 0 0$ , which implies ordering from nine times annual demand to ordering three times a year. The maximum error occurred for d = 1 and was 3.4% (A\*=214.86 instead of $A _ { 2 } { = } 2 2 2 . 2 2 )$ . For a demand rate of $d = 1 0$ with an order quantity of three annual demands, the error already reduces to 1.1%. The cost share converges to $4 A / 9$ for increasing demand rates. A similar behavior was observed when varying c from c =1 to c = 1000. The setup cost A was varied from A=10 to A=5000. For small values, the exact offer is slightly larger than the approximate values (for $A = 1 0 , A _ { 2 } ^ { * } = 4 . 4 7 , 4 A / 9 = 4 . 4 4 )$ ; for larger values, the exact offer is smaller with a maximum observed error for $\scriptstyle A = 5 0 0 0$ with $A _ { 2 } ^ { * } { = } 2 1 9 7 . 0 4$ instead of $4 A / 9 = 2 2 2 2 . 2 2$

## 3.1.3. Benefits and renegotiation incentives

Under the optimal allocation of A, player 2 will accept the optimal offer if $y \le Q ^ { * } - Q _ { 2 } ^ { * } = Q ^ { * } / 3$ , i.e., if its inventory level is not larger than a third of the maximum inventory level. Therefore, in 2/3 of all cases, an offer will be rejected and both players realize zero benefits. In 1/3 of all cases, when player 2 accepts the offer, player 1 realizes a benefit of $\Delta _ { 1 } { = } 4 A / 9$ . The benefit of player 2 depends on its inventory level y and is given by

$$
\begin{array}{l} \Delta_ {2} = \mathrm{e} ^ {- r y / d} \frac {A + c Q ^ {*}}{1 - \mathrm{e} ^ {- r Q ^ {*} / d}} \\ \quad - \left(A _ {2} ^ {*} + c \tilde {Q} + \mathrm{e} ^ {- r (y + \tilde {Q}) / d} \frac {A + c Q ^ {*}}{1 - \mathrm{e} ^ {- r Q ^ {*} / d}}\right) \\ = \frac {d c}{r} \left(\mathrm{e} ^ {r \tilde {Q} / d} - 1\right) - \left(A _ {2} ^ {*} + c \tilde {Q}\right) \approx \frac {r c}{2 d} (Q ^ {*} - y) ^ {2} \\ \quad - A _ {2} ^ {*} \end{array} \tag {20}\tag{20}
$$

using (11) and second order Taylor-series approximation for the exponential function.

For $y = 0 ,$ , this yields the maximum benefit $\Delta _ { 2 } { = } A - A _ { 2 } ^ { * } { = } 5 A / 9$ and, for ${ y = } Q ^ { * } / 3$ , this reduces to the minimum benefit $\Delta _ { 2 } = 0 .$ . In general, without having any specific knowledge about y (other than assuming that it is uniform on [0, $Q ^ { * } ] )$ , player 1 will realize an a-priori expected benefit of $E ( \Delta _ { 1 } ) { = } 4 A / 2 7$ , whereas the expected benefit of a follower, not knowing if or when an offer will take place is

$$
E \left(\Delta_ {2}\right) = \frac {1}{Q ^ {*}} \int_ {0} ^ {Q ^ {*} / 3} \frac {r c}{2 d} (Q ^ {*} - y) ^ {2} - A _ {2} ^ {*} d y = \frac {7}{8 1} A,\tag{21}
$$

i.e., about a half of the expected benefit obtained for the leader. As a result, though getting the smaller share of the setup cost, the follower in general is in an unfavorable position by having too much inventory when receiving an offer to cooperate. This suggests the need of other schemes of cooperation that better synchronize inventory levels and therefore opportunities to cooperate. One might also interpret this result as the penalty of not actively seeking for cooperations and just acting as a follower to proposed offers.

If player 1 would know the inventory level of player 2, the cost sharing offer would be chosen such that player 2 would just accept it, i.e.,

$$
Q _ {2} ^ {*} = Q ^ {*} - y \Leftrightarrow A _ {2} = A + y ^ {2} \frac {r c}{2 d} - 2 y \sqrt {\frac {r c A}{2 d}}.\tag{22}
$$

For $y = 0 ,$ , we find $A _ { 2 } { = } A$ and, for ${ \boldsymbol { y } } = { \boldsymbol { Q } } ^ { * }$ , we have $A _ { 2 } { = } 0$ . For ${ y = } Q ^ { * } / 3$ , we know that player 2 is indifferent between accepting and rejecting the offer and (22) yields $A _ { 2 } { = } 4 A / 9$ . Whenever the inventory level of player 2 is below a third of its maximum level, there is no incentive to renegotiate and the uncertainty about the inventory level is in favor of player 2. In case of a higher inventory level, both players would be better off if they can renegotiate about the share. However, if player 2 announces the true inventory level, player 1 will achieve all benefits (by just making an offer when player 2 is indifferent). One could extend the above analysis by player 1 making a second offer after player 2 rejected the initial offer (now having the better information that the inventory level is uniform on $[ Q ^ { * } / 3 , Q ^ { * } ]$ . But with several rounds of negotiation, player 1 would have to reduce his cost sharing offer (in order to account for too high inventory levels for the second player). Player 2, knowing this, would therefore wait until the last round. Therefore, player 1 will only make a single offer (or several identical offers).

## 3.2. Transaction costs

Now, let us assume that the search and implementation of cooperations is associated with further transaction costs. There might be two general categories of transaction costs, a cost for implementing a cooperation after an agreement has been reached and a cost for seeking for a cooperation, regardless of whether an agreement is reached or not.

First, let us consider the case that a replenishment cooperation is associated with a fixed cost of T being independent of quantity, $\mathrm { e . g . }$ , for the transportation of materials that are delivered to one partner and need to be allocated and distributed. Here, the question arises, how these costs are shared besides sharing the fixed cost of $A .$ Therefore, the offer $A _ { 2 }$ is the total transfer payment. We distinguish two extreme settings where either the leader or the follower is responsible for carrying out the allocation.

If the lead player carries the cost of materials allocation of jointly replenished goods, the analysis for the follower remains whereas the expected present value for the leader in (17) becomes

$$
\operatorname{ENPV} \left(A _ {2}\right) = \operatorname{NPV} - \left(A _ {2} - T\right) \left(1 - \sqrt {\frac {A _ {2}}{A}}\right).\tag{23}
$$

The resulting optimal cost sharing offer is

$$
A _ {2} ^ {*} = \frac {T}{3} + \frac {2}{9} A + \frac {2}{9} A \sqrt {1 + \frac {3 T}{A}}.\tag{24}
$$

Note that $A _ { 2 } ^ { * }$ includes a share on both, fixed ordering and transaction costs. In case that the transaction cost $T$ is significantly smaller than A, i.e., $3 T / A \approx 0$ , we find that $\begin{array} { r } { A _ { 2 } ^ { * } \approx T / 3 + 4 A / 9 , \mathrm { i . e . , } } \end{array}$ in addition to the setup cost share of $4 A / 9 _ { ; }$ , the follower has to carry a third of the transportation costs. However, a positive benefit for the lead player is only present if 2T / $3 + 5 A / 9 { \le } A ,$ , i.e., $T { \le } 2 A / 3$

Now, let us assume that the follower has to take care of the material allocation. Then the desired orderup-to-level for the extra replenishment becomes

$$
Q _ {2} = \sqrt {\frac {2 d (A _ {2} + T)}{r c}} = \sqrt {\frac {A _ {2} + T}{A}} Q ^ {*} =: Q _ {2} ^ {*}\tag{25}
$$

and the probability that an offer $A _ { 2 }$ is accepted becomes

$$
P (y \leq Q ^ {*} - Q _ {2} ^ {*}) = 1 - \sqrt {\frac {A _ {2} + T}{A}}.\tag{26}
$$

Under this condition, the expected cost present value for the leader is

$$
\operatorname{ENPV} \left(A _ {2}\right) = \operatorname{NPV} - A _ {2} \left(1 - \sqrt {\frac {A _ {2} + T}{A}}\right).\tag{27}
$$

The optimal cost sharing offer becomes

$$
A _ {2} ^ {*} = \frac {2}{9} A - \frac {2}{3} T + \frac {2}{9} A \sqrt {1 + \frac {3 T}{A}}.\tag{28}
$$

If the transportation cost is significantly smaller than the setup cost, $\mathrm { i . e . , ~ } 3 T / A \approx 0$ , the cost sharing offer has to be reduced by two thirds of the transportation cost. In this case, profitability for the leader requires $4 A / 9 - 2 T / 3 \geq 0$ , i.e., $T { \le } 2 A / 3$

## 3.3. Multiple potential partners

Assume that player 1 operates on a spot market with n potential partners for a joint order. The offer will be announced to all participants. We analyze two kinds of cooperations: (i) the cooperation is implemented with the first partner to accept the offer (if any) or (ii) cooperate with as many partners as accept the offer.

The present value $\mathrm { N P V } _ { 1 } ^ { \mathrm { c o } }$ is realized if the inventory level of at least one other player is less or equal to the critical level. The value $\mathrm { N P V } _ { 1 } ^ { \mathrm { n o } }$ only applies in the case that all players have more than the critical number of $Q ^ { * } - Q _ { 2 } ^ { * }$ units available. The probability for this event, assuming that all inventory levels are uniform between zero and $Q ^ { * }$ and are independent, is

$$
\begin{array}{l} P (y _ {1} > Q ^ {*} - Q _ {2} ^ {*}, y _ {2} > Q ^ {*} - Q _ {2} ^ {*}, \dots , y _ {n} > Q ^ {*} - Q _ {2} ^ {*}) \\ = \left(\frac {Q _ {2} ^ {*}}{Q ^ {*}}\right) ^ {n} = \left(\sqrt {\frac {A _ {2}}{A}}\right) ^ {n}. \end{array}\tag{29}
$$

Then the expected cost when making an offer of $A _ { 2 }$ to all market participants becomes

$$
\begin{array}{l} \mathrm{ENPV} (A _ {2}) = \left[ 1 - \left(\sqrt {A _ {2} / A}\right) ^ {n} \right] \mathrm{NPV} _ {1} ^ {\mathrm{co}} \\ \qquad + \left(\sqrt {A _ {2} / A}\right) ^ {n} \mathrm{NPV} _ {1} ^ {\mathrm{no}} \\ \qquad = \mathrm{NPV} - A _ {2} \left(1 - \left(\sqrt {\frac {A _ {2}}{A}}\right) ^ {n}\right). \end{array}\tag{30}
$$

Setting the first derivative equal to zero yields

$$
\begin{array}{r l} \frac {\mathrm{dENPV} (A _ {2})}{\mathrm{d} A _ {2}} & = - 1 + \left(\sqrt {\frac {A _ {2}}{A}}\right) ^ {n} + \frac {n}{2} \left(\sqrt {\frac {A _ {2}}{A}}\right) ^ {n} = 0 \\ & \Leftrightarrow A _ {2} = \left(\frac {2}{n + 2}\right) ^ {\frac {2}{n}} A. \end{array} \tag {31}
$$

For a single potential partner, we find a share of $A _ { 2 } { = } 4 A / 9 , n { = } 2$ yields an equal share of the setup cost, whereas for n tending to infinity, i.e., the player is almost certain to find a partner for cooperation, he will pass on the entire setup cost.

The expected benefit of player 1 from seeking for cooperations is

$$
E \left(\Delta_ {1}\right) = \mathrm{NPV} - \mathrm{ENPV} \left(A _ {2} ^ {*}\right) = \frac {n}{n + 2} \left(\frac {2}{n + 2}\right) ^ {\frac {2}{n}} A.\tag{32}
$$

A shortcoming of this modeling is that we assume a passive behavior of the other market participants. They could improve their performance by incorporating the fact that they do not have to accept any offer but instead can wait for a better offer from another player or even place an offer themselves. This situation is analyzed in the following section.

In case that the cooperation can be carried out with several partners simultaneously, higher benefits can be achieved since as many agents as join the cooperation transfer a share $A _ { 2 } .$ . If k partners join, the cost for the lead player becomes $\mathrm { N P V } ( k ) { = } \mathrm { N P V } - k A _ { 2 }$ . The probability that k players join, i.e., k players have an inventory level less than or equal to $Q ^ { * } - Q _ { 2 } ^ { * }$ and, assuming that all these levels are independent, results from a binomial distribution with market size n and probability $\begin{array} { r } { p = 1 - \sqrt { \frac { A _ { 2 } } { A } } . } \end{array}$ Then

$$
\begin{array}{l} \mathrm{ENPV} (A _ {2}) = \sum_ {k = 0} ^ {n} \binom {n} {k} \left(1 - \sqrt {\frac {A _ {2}}{A}}\right) ^ {k} \left(\sqrt {\frac {A _ {2}}{A}}\right) ^ {n - k} \times \mathrm{NPV} (k) \\ = \mathrm{NPV} - A _ {2} n \left(1 - \sqrt {\frac {A _ {2}}{A}}\right). \end{array} \tag {33}
$$

the optimal cost share remains $A _ { 2 } ^ { * } { = } 4 A / 9$ and the expected a priori benefit $E ( \Delta _ { 1 } ) { = } \mathrm { N P V } - \mathrm { E N P V } ( A _ { 2 } ) { = }$ $n ( 4 / 2 7 ) A$

## 3.4. Repeated opportunities

In the basic model, there are pre-assigned hierarchies, i.e., a leader that proposes a cooperation and a follower that only has the options to accept or reject the offer. If there exist no pre-assigned roles and there is the opportunity of repeated future cooperation agreements, a more general equilibrium type of model is required, which is analyzed in the following.

When an offer for a joint replenishment is received, the two existing options are not just to accept or to reject, but have to take into account the own opportunity to make a cost sharing proposal in the future. Assume that there is an equilibrium cost sharing offer $A _ { 2 } ^ { * } ,$ an equilibrium probability $p ( A _ { 2 } ^ { * } )$ that an equilibrium offer is accepted, an equilibrium cost present value $\mathrm { N P V } _ { E }$ and an equilibrium order quantity $Q _ { E } .$ In the situation that the inventory level is equal to zero and one aims to find a cooperation partner, the expected present value of an equilibrium offer consists of the expected direct payments and the future stream of equilibrium payments.

$$
\mathrm{NPV} _ {E} = A + c Q _ {E} - A _ {2} p (A _ {2}) + \mathrm{e} ^ {- r Q _ {E} / d} \mathrm{NPV} _ {E}.\tag{34}
$$

This expression includes a restrictive assumption about future incoming offers for cooperation, that is, we assume that there is a potential for future cooperation but we do not actively plan for incoming offers. As a consequence, the next planned event after a replenishment is the time where the inventory level reaches zero. Solving (34) for $\mathrm { N P V } _ { E }$ yields

$$
\mathrm{NPV} _ {E} = \frac {A + c Q _ {E} - A _ {2} p (A _ {2})}{1 - \mathrm{e} ^ {- r Q _ {E} / d}}\tag{35}
$$

which is similar to NPV in (1) except that an adjusted setup cost of $\tilde { A } { = } A - p ( A _ { 2 } ) A _ { 2 }$ is used. The optimal order quantity now takes into account that there exist potential future cooperations and therefore having an incentive to order more frequently to increase these benefits.

When rejecting the proposed offer and assuming that there will be no other offer before having to order again, the present value is

$$
\mathrm{NPV} _ {\mathrm{re}} = \mathrm{e} ^ {- r y / d} \mathrm{NPV} _ {E}.\tag{36}
$$

Given that the offer is accepted and assuming that there will be no cooperation offer before the next replenishment is required, the optimal order quantity is determined from

$$
\mathrm{NPV} _ {\mathrm{co}} = \min _ {\tilde {Q}} \left\{A _ {2} + c \tilde {Q} + \mathrm{e} ^ {- r (y + \tilde {Q}) / d} \mathrm{NPV} _ {E} \right\}\tag{37}
$$

and the optimal order quantity is $\scriptstyle \tilde { Q } = Q _ { E } - y$ (the proof is the same outlined for the one-time cooperation). It is optimal to use the cooperation to fill the gap between the current inventory level y and the equilibrium order-up-to-level $Q _ { E } .$ . Comparing the present values (36) and (37) of the two options, accepting is preferred over rejection if

$$
\begin{array}{l} A _ {2} + c \tilde {\mathcal {Q}} + \mathrm{e} ^ {- r (y + \tilde {\mathcal {Q}}) / d} \mathrm{NPV} _ {E} \leq e ^ {- r y / d} \mathrm{NPV} _ {E} \\ \Leftrightarrow \frac {r (A _ {2} + c \tilde {\mathcal {Q}})}{d c} \leq \mathrm{e} ^ {r \tilde {\mathcal {Q}} / d} - 1. \end{array}\tag{38}
$$

This implies that cooperation is beneficial whenever $\tilde { \mathcal { Q } } = \mathcal { Q } _ { E } - y \ge \mathrm { E O Q } ( A _ { 2 } )$ , that is if $y { \le } Q _ { E } { - } \mathrm { E O Q }$ $\left( A _ { 2 } \right)$ . Even in case the inventory level approaches zero, there is no incentive to wait for the own offering opportunity.

Using the above result and again making the assumption that the inventory level of the follower is uniform between zero and $\varrho _ { E } ,$ the probability that an offer $A _ { 2 }$ is accepted, that is, that the inventory level is lower than the difference between the equilibrium order quantity and the economic order quantity for a setup cost of size $A _ { 2 }$ is

$$
\begin{array}{c} p (A _ {2}) = 1 - \sqrt {\frac {A _ {2}}{A - p (A _ {2}) A _ {2}}} \Leftrightarrow (1 - p (A _ {2})) ^ {2} \\ \times \left(\frac {A}{A _ {2}} - p (A _ {2})\right) = 1. \end{array}\tag{39}
$$

In order to find the equilibrium acceptance proba bility, we would have to solve a cubic equation.

The cost present value minimizing offer $A _ { 2 }$ (equivalently, the transfer price maximizing offer) is determined from

$$
\min _ {A _ {2}} \{- A _ {2} p (A _ {2}) \} \Rightarrow \frac {\mathrm{dNPV}}{\mathrm{d} A _ {2}} = - p (A _ {2}) - A _ {2} \frac {\mathrm{d} p (A _ {2})}{\mathrm{d} A _ {2}} = 0.\tag{40}
$$

The derivative $\mathrm { d } p ( A _ { 2 } ) { = } \mathrm { d } A _ { 2 }$ can be obtained from the cubic Eq. (39) by implicit differentiation and is given by

$$
\frac {\mathrm{d} p \left(A _ {2}\right)}{\mathrm{d} A _ {2}} = \frac {- (1 - p \left(A _ {2}\right)) \frac {A}{A _ {2} ^ {2}}}{2 \left(\frac {A}{A _ {2}} - p \left(A _ {2}\right)\right) + 1 - p \left(A _ {2}\right)} <   0.\tag{41}
$$

Inserting into (40), we need to solve

$$
\begin{array}{l} (1 - p (A _ {2})) \left(\frac {A}{A _ {2}} - p (A _ {2})\right) \\ = 2 p (A _ {2}) \left(\frac {A}{A _ {2}} - p (A _ {2})\right) \Leftrightarrow p (A _ {2}) = \frac {1}{3}. \end{array}\tag{42}
$$

Inserting into (39) and solving for $A _ { 2 }$ yields

$$
A _ {2} ^ {*} = \frac {1 2}{3 1} A, Q _ {E} = \sqrt {\frac {2 d \frac {2 7}{3 1} A}{r c}}.\tag{43}
$$

An optimal offer is to propose a cost sharing where more than two third of the fixed ordering cost is retained with the proposer. The acceptance probability is again one third. The expected benefit at each ordering instant is $E ( \Delta ) { = } 4 A / 3 1$ and less than in the single opportunity case (4A / 27). However, it is achieved more frequently when ordering the equilibrium quantity $Q _ { E } .$ The present value of benefits becomes $E ( \Delta ) / ( 1 - \mathrm { e } ^ { - r Q _ { E } / \bar { d } } )$ . For the setting with multiple potential partners, the equilibrium probability is determined from

$$
\begin{array}{l} p (A _ {2}) = 1 - \left(\sqrt {\frac {A _ {2}}{A - p (A _ {2}) A _ {2}}}\right) ^ {n} \Leftrightarrow (1 - p (A _ {2})) ^ {\frac {2}{n}} \\ \times \left(\frac {A}{A _ {2}} - p (A _ {2})\right) = 1. \end{array} \tag {6}\tag{44}
$$

Then the optimal offer $A _ { 2 } ^ { * }$ and the associated probability of cooperation $p ( A _ { 2 } ^ { * } )$ are

$$
p \left(A _ {2}\right) = \frac {n}{n + 2}, A _ {2} ^ {*} = \frac {(n + 2) 4 ^ {\frac {1}{n}}}{(n + 2) ^ {\frac {n + 2}{n}} + n 4 ^ {\frac {1}{n}}} A.\tag{45}
$$

Both, the probability of finding a cooperation partner and the share $A _ { 2 }$ are increasing with n and so is the expected benefit $p ( A _ { 2 } ) A _ { 2 }$ achieved for each ordering instant.

## 3.5. Experimental results

One limitation of game theory models is that they assume rational behavior of all decision-makers. One example is that a follower will accept any positive offer over getting nothing even if the leader retains almost all the benefits. Therefore, empirically observable behavior of decision-makers often deviates from theory. In experimental economics [11], such games are played with individuals, and their real decision behavior is investigated. In our context, a follower might only accept an offer if his current situation is improved by at least a threshold value.

For the presented replenishment cooperation problem, an experiment was conducted with 156 undergraduate students of a core operations management course after teaching the basics of order quantity models. Though undergraduate students might not be a reliable source for business decision-making, the results serve as a basic indication how humans decide in the illustrated cooperation problem. The used data were A= 500, r =0.1, c =100 and $d { = } 1 0 0$ , which yield an EOQ of 100 units. The students were asked about two types of decisions, (i) accepting a given cost sharing offer with a given current inventory level y (and how many units to order) and, after addressing these questions, (ii) proposing an own offer to a follower how to share the setup cost of $A = 5 0 0$ . The students were given the following 9 scenarios $( y , A _ { 2 } )$ of inventory level y and offer A : 1: (0,375), 2: (0,250), 3: (0,125), 4: (30,300), 5: (30,200), 6: (30,100), 7: (60,225), 8: (60,175), 9: (60,125).

Fig. 1 shows the percentage that a specific order quantity was proposed in each scenario. Note that a zero order quantity implies rejecting the offer. The theoretically optimal decision is to order 100 in the first three scenarios, to reject the offer, i.e., order zero in the fourth scenario, to order 70 in scenarios 5 and 6, and to reject the offer in the last three scenarios.

Fig. 2 shows the proposed offers in part (ii) of the experiment in terms of the proposer’s share $\ v { A } _ { 1 } = \ v { A } - \ v { A } _ { 2 }$ . We observe that there exist two prominent numbers, $A _ { 1 } = 2 5 0$ and $ { \boldsymbol { A } } _ { 1 } = 3 0 0$ . The average proposal is 265.08, which is close to the theoretically optimal proposal of $A _ { 1 } ^ { * } { = } 2 7 2 . 2 2$

![](/api/attachments/SVDE2C8B/fulltext/images/ae0454e389b5eda827509aab44bcf59e72c36ccf48d73b8511931e2bdd991b3a.jpg)  
Fig. 1. Experimental results—follower decision.

![](/api/attachments/SVDE2C8B/fulltext/images/13aaac097bf4a80cfaf9d4123ded6030e71c0331d079947b3ffa81a71da281ab.jpg)  
Fig. 2. Experimental results—leader decision.

## 4. Long-term cooperation

In contrast to one-time cooperations, long-term cooperative sourcing with a partner organization offers the additional benefit (besides sharing ordering costs) of synchronizing replenishment operations and using the optimal resupply strategy of a virtually centralized organization. In the following, we analyze the centrally optimal ordering decision and present the Nash bargaining solution from cooperative game theory as a concept to allocate the benefits from centralized ordering. In the following, let $d _ { i }$ denote player i’s demand rate. We will analyze the case of $n = 2$ not necessarily identical players.

## 4.1. Centrally optimal ordering policy

Jointly ordering $d _ { 1 } + d _ { 2 }$ units results in an order quantity $\boldsymbol { \mathcal { Q } } ^ { \mathrm { c o } }$ and a cost present value $\mathrm { N P V } ^ { \mathrm { c o } }$ given by

$$
\begin{array}{l} Q ^ {\mathrm{co}} = \sqrt {\frac {2 A (d _ {1} + d _ {2})}{r c}} \text { and } \\ \mathrm{NPV} ^ {\mathrm{co}} = \frac {A + c Q ^ {\mathrm{co}}}{1 - \mathrm{e} ^ {- r Q ^ {\mathrm{co}} / (d _ {1} + d _ {2})}}. \end{array}\tag{46}
$$

Note that the new optimal joint ordering involves a different timing of replenishments. Orders are placed more frequently and both ordering and inventory holding costs are reduced. The joint order $\boldsymbol { Q } ^ { \mathrm { c o } }$ will be allocated according to the demand rates, $\begin{array} { r } { \tilde { \boldsymbol { Q } } _ { i } = \frac { d _ { i } } { d _ { 1 } + d _ { 2 } } \boldsymbol { Q } _ { \mathrm { ~ \tiny ~  ~ } } ^ { \mathrm { c o } } } \end{array}$ . The (identical) cycle time for both players is $\begin{array} { r } { \tilde { T } = Q _ { i } ^ { \mathrm { c o } } / d _ { i } = \sqrt { \frac { 2 A } { r c ( d _ { 1 } + d _ { 2 } ) } } . } \end{array}$ For identical players, this leads to the well-known square root law when consolidation of inventories and replenishments is implemented, ${ \tilde { Q } } = Q ^ { \mathrm { c o } } / { \sqrt { 2 } }$ . The total benefit is

$$
\begin{array}{l} E (\Delta) = \mathrm{NPV} _ {1} + \mathrm{NPV} _ {2} - \mathrm{NPV} ^ {\mathrm{co}} \\ \approx \sqrt {\frac {A c}{2 r}} \Big (\sqrt {d _ {1}} + \sqrt {d _ {2}} - \sqrt {d _ {1} + d _ {2}} \Big), \end{array}\tag{47}
$$

where the approximation is obtained using $\mathrm { e } ^ { x } \approx 1 + x .$

In a hierarchical setting with a leader to propose a (long-term) share and a follower who regards this as a take-it or leave-it offer, the optimal sharing offer would be $\begin{array} { r } { A _ { 2 } = \sqrt { \frac { d _ { 2 } } { d _ { 1 } + d _ { 2 } } } A , } \end{array}$ which gives all benefits to the leader. However, the stability of such a solution for a long-term cooperation where one of the partners achieves zero benefits is questionable since the discriminated decision-maker will immediately quit the cooperation when receiving any better offer, e.g., onetime cooperation on a spot market.

## 4.2. Nash bargaining solution

The Nash solution is a concept from cooperative game theory [23,24] that follows from several axioms of rational decision-making. The bargaining process is not modeled explicitly. One important component within this framework is the utility function for each decision-maker, i.e., how certain outcomes of the bargaining process are evaluated. Because of the (random) outcome of the negotiation, the decisionmaker’s attitude towards risk plays an important role for bargaining. Assume that one player is more riskaverse than the other. As a consequence, the more risk-averse player is willing to agree on a lower share of the benefits (because of the risk of not reaching an agreement) than a risk neutral player would. Maximizing expected cost benefits from cooperation as done in the previous sections implies linear utility functions and therefore risk neutral decision-makers, which we will retain in the following.

The objective function to obtain the Nash bargaining solution is to maximize the product of the player’s benefits from cooperation. Each individual benefit is the difference between the player’s disagreement point (when not reaching an agreement and therefore placing individual orders) and the cost NPV under the negotiated cooperation pay-off. Because the following analysis is straightforward for non-identical players (with respect to their demand rates), we will illustrate this extended problem version. The disagreement point for both players, i.e., the cost present value they obtain if no agreement is reached, is

$$
\mathrm{NPV} _ {i} = \frac {A + c Q _ {i}}{1 - \mathrm{e} ^ {- r Q _ {i} / d _ {i}}}.\tag{48}
$$

When both players cooperate with a proposed allocation $\scriptstyle A = A _ { 1 } + A _ { 2 }$ for the setup cost, the resulting present values are

$$
C _ {i} = \frac {A _ {i} + c \tilde {Q} _ {i}}{1 - \mathrm{e} ^ {- r \tilde {T}}}.\tag{49}
$$

The objective is to find a sharing agreement $\scriptstyle A = A _ { 1 } + A _ { 2 }$ such that the Nash product NP is maximized, i.e.,

$$
\max _ {A _ {i}} \mathrm{NP} = (\mathrm{NPV} _ {1} - C _ {1}) (\mathrm{NPV} _ {2} - C _ {2})\tag{50}
$$

$$
\text { s.t. } \quad C _ {i} \leq \text { NPV } _ {i} \quad i = 1, 2.\tag{51}
$$

As shown by Nash, the solution of this optimization problem is the only one that satisfies the following axioms: (i) invariance to equivalent utility representations (i.e., preferences and not the chosen utility function matter), (ii) individual rationality $\begin{array} { r } { ( \mathrm { i } . \mathrm { e } . , \ C _ { i } \leq \mathrm { N P V } _ { i } ) } \end{array}$ , (iii) Pareto efficiency (i.e., the entire achievable benefit is allocated which implies that whenever there is a positive benefit from cooperation that an agreement is reached), (iv) symmetry and (v) independence of irrelevant alternatives. For a more detailed discussion of these axioms and respective proofs, see [20,21].

The necessary optimality condition with respect to the cost sharing offer $A _ { 1 }$ is

$$
\begin{array}{r l} \frac {\mathrm{dNP}}{\mathrm{d} A _ {1}} & = \frac {1}{1 - \mathrm{e} ^ {- r \tilde {T}}} \left[ (\mathrm{NPV} _ {1} - C _ {1}) - (\mathrm{NPV} _ {2} - C _ {2}) \right] = 0 \\ & \Leftrightarrow A - 2 A _ {1} + c \big (\tilde {Q} _ {2} - \tilde {Q} _ {1} \big) \\ & = \Big (1 - \mathrm{e} ^ {- r \tilde {T}} \Big) (\mathrm{NPV} _ {2} - \mathrm{NPV} _ {1}) \\ A _ {1} ^ {*} & = \frac {A + c \big (\tilde {Q} _ {2} - \tilde {Q} _ {1} \big) + \Big (1 - \mathrm{e} ^ {- r \tilde {T}} \Big) (\mathrm{NPV} _ {1} - \mathrm{NPV} _ {2})}{2}. \end{array}\tag{52}
$$

The interpretation of optimality condition (52) is that both players in the cooperation will achieve equal benefits, i.e., total cost savings from the sourcing cooperation are equally shared (the so-called split the difference rule whenever both players have equal bargaining power). As a consequence, the player with a higher demand rate and therefore larger supply volume will have to carry a larger portion of the setup cost from each replenishment. Using the approximation $( 1 - \mathrm { e } ^ { - r \tilde { T } } ) / ( \bar { 1 } - \mathrm { e } ^ { - r T _ { i } } ) { \approx } \tilde { T } / T _ { i } = \bar { \sqrt { d _ { i } } } / \bar { \sqrt { d _ { 1 } + d _ { 2 } } }$ , the optimal sharing offer reduces to

$$
A _ {1} ^ {*} = \left(1 - \frac {\sqrt {d _ {2}} - \sqrt {d _ {1}}}{\sqrt {d _ {1} + d _ {2}}}\right) \frac {A}{2}\tag{53}
$$

which only depends on the setup cost and the demand rated of the players. The player with the larger demand rate carries the larger portion of the setup cost. The respective benefits are 50% of (47) for each player.

In contrast to the Nash bargaining solution, Rubinstein [28] explicitly models the interaction of offers and counter offers by the two players. The game theoretic concept to solve this sequential game is the subgame perfect equilibrium (see, e.g., [10]). Then, the decision problem for the player that receives an offer to terminate individual replenishments and to reach a cooperative sourcing agreement is to compare the cost present values of accepting the offer or rejecting it and being able to make an offer at the beginning of the next cycle. For the time between opportunities to offer approaching zero, the Rubinstein solution yields the same outcome as the Nash solution (e.g., see [20]).

## 4.3. Cost allocation

Under general conditions the Nash bargaining solution yields a different outcome than simple-cost based-allocation rules. In the following, we use a simple example to illustrate these differences. The cost parameters are $A = 5 0 0 , \mathrm { ~ } c = 1 0 0$ and $r { = } 0 . 1$ . The demand rate of player 1 is $d _ { 1 } = 1 0 0$ , whereas the demand rate of the second player is varied from $d _ { 2 } = 1 0$ to $d _ { 2 } = 2 0 0$ . In the following, we consider allocations of overhead costs because the present value of the continuous stream of just-in-time procurement–which is equal to $c d _ { i } / r { \mathrm { - a r e } }$ direct costs that can be allocated exactly.

The exact Nash bargaining allocation is obtained from (52), the approximation using (53). A first method is to allocate the setup costs only by a volume (demand rate)-based allocation $\begin{array} { r } { A _ { i } = \frac { \dot { d } _ { i } } { d _ { 1 } + d _ { 2 } } \dot { } } \end{array}$ or a transaction-based $\begin{array} { r } { A _ { i } = \frac { d _ { i } / Q _ { i } } { d _ { 1 } / Q _ { 1 } + d _ { 2 } / Q _ { 2 } } A } \end{array}$ <sup>1 2</sup> allocation. Fig. 3 shows the resulting allocations for player 1. In case the two players have identical demand rates, all methods yield the same allocation of setup costs. If player 2 has a smaller demand rate than player 1, all allocations provide a larger cost share than the bargaining solution for player 1. Therefore, the synergy potential provided by the larger party is not sufficiently incorporated by the simple allocation methods. The best quality compared to the exact solution is achieved when setup costs are allocated according to the number of setups before cooperation.

![](/api/attachments/SVDE2C8B/fulltext/images/4c6e839ea11410a831a9285fa0dcb923f851a6eafce6ace5727008625052005c.jpg)  
Fig. 4. Allocation of total relevant cost.

A second method is based on the allocation of total relevant costs. In addition to setup costs, inventory holdings costs, i.e., the interest on having to make payments in advance due to batching, have to be taken into account. Fig. 4 shows the allocation of total benefits among the two players when total relevant costs are allocated according to the bargaining solution, a volume-based allocation, a transaction or a cost (before cooperation)-based allocation. We can observe an underestimation of the synergy potential provided by the larger player for the volume-based and an overestimation for the transaction-based method.

## 4.4. Comparison of one-time and long-term cooperation

An important question is whether to engage in spot markets for initiating cooperative orders or to seek for long-term cooperative sourcing relationships. We use the equal share provided by the Nash solution as a benchmark for the benefits of long-term cooperative sourcing. In order to compare these benefits to the ones obtained by a player who seeks short-term order agreements on a market, let us assume that the expected benefit associated with a single cooperation (32) will be achieved for all future replenishments. Then the benefit

![](/api/attachments/SVDE2C8B/fulltext/images/d263c7f6ce493dd5bda59c069da505eeb20c3e86bf8ac38fa7d6550c2e402849.jpg)  
Fig. 3. Allocation of setup cost.

$$
\mathrm{NPV} _ {\Delta} = \frac {\frac {n}{n + 2} \left(\frac {2}{n + 2}\right) ^ {2 / n} A}{1 - \mathrm{e} ^ {- r Q / d}}\tag{54}
$$

has to be compared to the equal share of (47) as the outcome of the Nash bargaining solution and a critical size of potential partners can be obtained, which, in general, depends on all parameters of the problem. Using $1 - \bar { \mathrm { e } } ^ { - r Q / d } \approx r Q / \bar { d } .$ , which is reasonable for sufficiently small interest rates and inventory cycles, the comparison of benefits only depends on the number of potential partners and the lead player prefers the market alternative over the long-term cooperation if

$$
\frac {n}{n + 2} \left(\frac {2}{n + 2}\right) ^ {2 / n} > 1 - \frac {1}{\sqrt {2}}.\tag{55}
$$

The smallest market size n for which this condition is satisfied is $n ^ { * } { = } 3$ , i.e., there have to be at least 3 other potential partners accepting cooperation offers on a market in order to be able to achieve more benefits than in a long-term cooperative sourcing agreement with a single partner. For the setting where multiple partners can join the cooperation, the short-term alternative is preferred if

$$
\frac {4 n}{2 7} > 1 - \frac {1}{\sqrt {2}}.\tag{56}
$$

The smallest number n for which this condition is satisfied is $n ^ { * } = 2$ . When repeated opportunities for cooperation exist and there is no pre-assigned hierarchy, the present value of benefits changes to $p ( A _ { 2 } ) A _ { 2 } /$ $( 1 - \mathrm { e } ^ { - r \hat { Q } _ { E } / d } )$ using (45). When using the first order approximation, again the comparison only depends on the number of partners and $n ^ { * } { = } 4$

## 5. Conclusions

The paper presents different bargaining solutions for cooperative replenishment of items in the context of the economic order quantity model. The results highlight that the benefits that can be achieved for decentralized decision-makers from cooperation depend on the rules of the bargaining game. A first finding is that actively seeking for cooperations provides higher benefits than passively accepting offers, i.e., there are first mover advantages. A second finding is that acting on a spot market for initiating cooperations compared to building a long-term cooperation with a single partner is only beneficial if there exists a critical number of potential partners.

The initial findings in this paper offer several lines of extension. So far the transaction cost for seeking and carrying out cooperations have not been modeled explicitly. These are costs of transportation for distributing the jointly purchased units and fees for participating in electronic markets for initiating cooperations and the respective efforts for monitoring these markets. Another issue is the bargaining over sourcing cost components other than the fixed cost, i.e., if quantity discounts can be achieved from cooperations and how to allocate these benefits. Additionally, bargaining might be extended to simultaneously bargaining with cooperation partners and suppliers, i.e., combining horizontal and vertical aspects in supply chain management. The modeling of a market (see [25,32] for industrial organization literature on market microstructure) might also be extended in several ways, e.g., several active and passive players or players acting in both ways, making and accepting offers. Then, the additional question arises what the optimal policy for acting on a market is.

The models considered in this paper assume that only two organizations bargain over a cooperation at a time. If cooperations with multiple (n <sup>N</sup> 2) players are formed, the explicit modeling of the bargaining process becomes more complex, one reason being that there are many more alternatives how to organize offers and counter offers etc. The approach used in cooperative game theory [12,21] is to move away from the noncooperative foundation of the bargaining process but instead study coalitions and formulate requirements for their stability and to find concepts for the allocation of benefits (e.g., the core, Shapley value, Nucleolus, etc.). One such approach with respect to the EOQ ordering of groups can be found in [17].

Moving away from the EOQ context, another fruitful aspect are cooperations for sharing risk, i.e., cooperative safety stocks or sharing resources like warehouses, manufacturing capacity, or maintenance equipment.

## References

[1] R. Anupindi, Y. Bassok, E. Zemel, A general framework for the study of decentralized distribution systems, Manufacturing and Service Operations Management 3 (4) (2001 (Fall)) 349 – 368.

[2] G.P. Cachon, Supply chain coordination with contracts, in: A.G. de Kok, S.C. Graves (Eds.), Supply Chain Management: Design, Coordination and Operation, Handbooks in Operations Research and Management Science, vol. 11, Elsevier, Amsterdam, 2003, pp. 229 – 339.

[3] G. Cachon, P. Harker, Competition and outsourcing with scale economies, Management Science 48 (10 (October)) (2002) 1314– 1333.

[4] G. Cachon, S. Netessine, Game theory in supply chain analysis, in: D. Simchi-Levi, S.D. Wu, Z.-J. Shen (Eds.), Handbook of Quantitative Supply Chain Analysis, Kluwer, Boston, 2004, pp. 13– 65.

[5] M. Carney, The incentive structures of co-operative retail buying groups, Economic and Industrial Democracy 13 (1992) 207–231.

[6] C. Corbett, Stochastic inventory systems in a supply chain with asymmetric information: cycle stocks, safety stocks, and consignment stock, Operations Research 49 (4) (2001 (July– August)) 487– 500.

[7] C.J. Corbett, C.S. Tang, Designing supply contracts: contract type and information asymmetry, in: S. Tayur, R. Ganeshan, M. Magazine (Eds.), Quantitative Models for Supply Chain Management, Kluwer, Boston, 1999, pp. 269– 297.

[8] W.J. Elmaghraby, Supply contract competition and sourcing policies, Manufacturing and Service Operations Management 2 (4) (2000 (Fall)) 350– 371.

[9] M. Essig, M. Cooperative Sourcing, Lang, Frankfurt/Main, 1999.

[10] D. Fudenberg, J. Tirole, Game Theory, MIT Press, Cambridge, 1991.

[11] J.H. Kagel, A.E. Roth (Eds.), The Handbook of Experimental Economics, Princeton University Press, Princeton, 1995.

[12] J.P. Kahan, A. Rapoport, Theories of Coalition Formation, Erlbaum, Hillsdale, 1984.

[13] P.R. Kleindorfer, D.J. Wu, Integrating long- and short-term contracting via business-to-business exchanges for capital-intensive goods, Management Science 49 (11) (2003 (November)) 1597– 1615.

[14] R. Kohli, H. Park, A cooperative game theory model of quantity discounts, Management Science 35 (6) (1989) 693– 707.

[15] H.L. Lee, S. Whang, Decentralized multi-echelon supply chains: incentives and information, Management Science 45 (5) (1999 (May)) 633– 640.

[16] D.H. Maister, Centralization of inventories and the square root law, International Journal of Physical Distribution and Material Management 6 (3) (1976) 124– 134.

[17] A. Meca, J. Timmer, I. Garcia-Jurado, P. Borm, Inventory games, European Journal of Operational Research 156 (1) (2004 (July)) 127– 139.

[18] K.J. Min, C.-K. Chen, A competitive inventory model with options to reduce setup and inventory holding costs, Computers and Operations Research 22 (5) (1995 (May)) 503 – 514.

[19] K. Moinzadeh, Replenishment and stocking policies for inventory systems with random deal offerings, Management Science 43 (3) (1997 (March)) 334 – 342.

[20] A. Muthoo, Bargaining Theory with Applications, Cambridge University Press, Cambridge, 1999.

[21] R.B. Myerson, Game Theory: Analysis of Conflict, Harvard University Press, Cambridge, 1991.

[22] B. Nalebuff, A. Brandenburger, Co-opetition, Doubleday, New York, 1996.

[23] J. Nash, The bargaining problem, Econometrica 18 (1950) 155– 162.

[24] J. Nash, Two-person cooperative games, Econometrica 21 (1953) 128– 140.

[25] M. O’Hara, Market Microstructure Theory, Blackwell, Oxford, 1995.

[26] B. Peleg, H.L. Lee, W.H. Hausman, Short-term E-procurement strategies versus long-term contracts, Production and Operations Management 11 (4) (2002 (Winter)) 458– 479.

[27] H. Raiffa, J. Richardson, D. Metcalfe, Negotiation Analysis: The Science and Art of Collaborative Decision Making, Harvard University Press, Cambridge, 2002.

[28] A. Rubinstein, Perfect equilibrium in a bargaining model, Econometrica 50 (1) (1982) 97– 109.

[29] N. Rudi, S. Kapur, D. Pyke, A two-location inventory model with transshipment and local decision making, Management Science 47 (12) (2001) 1668– 1680.

[30] E.A. Silver, D.J. Robb, M.R. Rahnama, Random opportunities for reduced cost replenishments, IIE Transactions 25 (2) (1993 (March)) 111– 120.

[31] E.A. Silver, D.F. Pyke, R. Peterson, Inventory Management and Production Planning and Scheduling, 3rd ed., Wiley, Chichester, 1998.

[32] D.F. Spulber, Market Microstructure, Cambridge University Press, Cambridge, 1999.

[33] D. Sun, M. Queyranne, Production and inventory model using net present value, Operations Research 50 (3) (2002 (May–June)) 528–537.

[34] D.J. Thomas, P.M. Griffin, Coordinated supply chain management, European Journal of Operational Research 94 (1) (1996 (October)) 1 – 15.

![](/api/attachments/SVDE2C8B/fulltext/images/c686f172edc2096a864331d862e2c72d1ba4edc9ef0955ed7e651103adcb851d.jpg)  
Stefan Minner is Professor of Business Administration and Logistics at the University of Mannheim. He received his MBA degree from the University of Bielefeld and his PhD from the University of Magdeburg. His major research interests and publications are in the area of collaboration in logistics, reverse logistics and safety stock planning.

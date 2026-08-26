---
otero_id: 13510
otero_key: "BUS7XJ4B"
title: "On the Optimality of Fixed-up-to Tariff for Telecommunications Service"
authors: "Yasushi Masuda; Seungjin Whang"
year: "2006"
journal: "Information Systems Research"
doi: "10.1287/isre.1060.0097"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [128.122.253.228] On: 28 July 2015, At: 19:37 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR

![](/api/attachments/BUS7XJ4B/fulltext/images/57597f063dac5fe2dfa0134958f9bee373935381530079b92d3ba2fb52d62ee1.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# On the Optimality of Fixed-up-to Tariff for Telecommunications Service

Yasushi Masuda, Seungjin Whang,

## To cite this article:

Yasushi Masuda, Seungjin Whang, (2006) On the Optimality of Fixed-up-to Tariff for Telecommunications Service. Information Systems Research 17(3):247-253. http://dx.doi.org/10.1287/isre.1060.0097

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2006, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/BUS7XJ4B/fulltext/images/8a425bf5c1540eecbc944a3455b27a858f9028dd020741bb98fb5680bbd0644f.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# On the Optimality of Fixed-up-to Tariff for Telecommunications Service

Yasushi Masuda

Faculty of Science and Technology, Keio University, Yokohama 223-8622, Japan, masuda@ae.keio.ac.jp

Seungjin Whang

Graduate School of Business, Stanford University, 518 Memorial Way, Stanford, California 94305-5015, whang\_jin@gsb.stanford.edu

tariff is the total charge payable by a customer for services provided. We study the design of tariffs for a telecommunications service provider. We develop an economic model that captures the negative externalities of the network and the diversity of customers. The tariff is designed so that it reflects the expected response of different customers and the system congestion it would induce. We study a simple tariff structure in wide use by mobile phone carriers—a menu of “fixed-up-to (FUT)” plans like “fixed access fee \$35 up to 300 minutes, and \$0.40 per minute beyond the limit.” We derive the optimal menu of FUT plans and show that such a simple FUT menu structure delivers as good performance to the monopolistic carrier as any nonlinear pricing schedule.

Key words: tariff design; queuing delays; nonlinear pricing; menu of plans

History: Sumit Sarkar, Senior Editor; Terence Hendershott, Associate Editor. This paper was received on January 5, 2005, and was with the authors 6 <sup>1</sup> months for 2 revisions.

## 1. Introduction

A tariff indicates the total charge payable by a customer for services provided (Wilson 1993). Examples of tariff are a fixed monthly fee, uniform pricing, multipart pricing, and nonlinear pricing on total call time or the number of packets exchanged. In this paper, we study the design of tariffs for a telecommunications service provider (or simply carrier). We develop a model that captures two aspects of telecommunications service. First, the service quality deteriorates as the usage level increases. Second, customers may differ in valuing the service, so they may react differently to a given tariff. The monopolistic carrier in our model should consider these aspects and design the tariff to maximize the profit.

The standard approach to tariff design is nonlinear pricing. Diverse customers have different demand functions, so they react differently facing different marginal and fixed costs of nonlinear pricing. With nonlinear pricing, the carrier has large degrees of freedom in choosing pricing parameters that can be used to induce the right level of subscription, usage, and the system performance. See Nonlinear Pricing by

Robert Wilson (1993) that offers an invaluable set of methodologies and insights to tariff design in the electric power industry. In the queueing context, see Rao and Peterson (1998) who demonstrate that a special form of nonlinear tariff (i.e., two-part tariff) exists to induce optimal output rates and priority assignment for a service facility.

Despite its optimality, however, few instances of sophisticated nonlinear pricing are observed in practice. Rather, we find very simple tariffs in wide use. For example, most U.S. mobile phone carriers offer a fixed-up-to (FUT) plan such as “fixed access fee \$35 up to 300 minutes, and \$0.40 per minute beyond the limit” (Verizon Wireless). In addition, they offer a menu of such FUT plans. That is, if an FUT plan is represented by (fixed fee, free call time allowance, overlimit rate), the menu looks like {(\$35, 300, \$0.40), (\$75, 900, \$0.35), (\$200, 3,000, \$0.20)}. This simple tariff structure may have the benefit of simple billing (i.e., computation, estimation, and interpretation), but perhaps at some sacrifice of the carrier’s profit. That is, the FUT plans may be a simple approximation to some complicated nonlinear convex pricing. Contrarily, however, this paper demonstrates that the simple FUT menu structure is an optimal tariff structure in its own way and, in fact, as good as any other nonlinear pricing, to the monopolistic carrier.

The main idea of the result starts with the insights of Walter Oi (1971) on two-part pricing in Disneyland Park. Oi (1971) notes that one way of extracting all the consumer surplus at Disneyland Park is to charge the marginal cost per ride, plus a fixed entrance fee that is equal to the consumer surplus. This scheme leaves no efficiency loss (or deadweight loss), and all potential surplus accrues to the carrier. Two-part pricing can be extended to nonlinear pricing when the service provider faces heterogeneous customers varying in their benefits (see Wilson 1993). Nonlinear tariffs may be offered in a menu of options from which customers choose depending on their service valuation. A menu of FUT plans is one such example.

Under a menu of FUT plans, the time allowance can serve as an admissions control. By adjusting the time allowance, the carrier can control the congestion level. The coupling of an allowance with a fixed fee can provide the desired trade-off that helps induce self-selection in tariff design. By asking subscribers to select from a menu of competing plans, the carrier can induce them to reveal their type, and based on the information, price discriminate them. In fact, a welldesigned multiplan FUT tariff turns out as good as any nonlinear pricing.

There exists a rich literature on the economics of queueing systems, where pricing plays a critical role. Because free access policy leads to overcongestion (Naor 1969), various pricing systems have been studied as a way to control admissions and quality of service. Interested readers are referred to Hassin and Haviv (2003) for an extensive treatment of the topic. Most relevant to the present work are Mendelson (1985) and Rao and Peterson (1998). From the former, we borrow the basic model that provides the trade-off between delays and consumer benefits in a queueing system. The latter is a rare piece of work that studies nonlinear tariffs in a queueing system.

In this paper, we focus on the design of an optimal multiplan FUT tariff and its optimality. In $\ S 2 ,$ we develop the basic setting of the model. In §3, we derive the optimal menu of FUT plans. We note that the multiplan tariff is not always optimal. Depending on the composition of the consumer population, a single-plan tariff could be better than any multiplan tariff. Section 4 constitutes the core of this paper, where we consider nonlinear pricing, compare it with the FUT menu, and demonstrate that the FUT menu is not dominated by any menu of nonlinear tariffs. The last section provides qualitative discussions on the tariff issue, along with concluding remarks and future research directions.

## 2. The Model

Consider a service provider, or a carrier, that sells network access service to a large number of small customers. Customers<sup>1</sup> are nonhomogeneous. Each customer belongs to one of I types that differ in the level of benefit they derive from using the system. For the sake of simple analysis, we assume that there are two types $( \mathrm { i . e . , } I = 2 )$ indexed by $i = 1 , 2 .$ In each type, a continuous set of nonatomic (or measure-zero) customers exist. All customers are symmetric within the same type. Each customer has a Poisson stream of jobs (calls or packets) she may submit to the network. The intensity of usage is expressed in terms of the usage rate or job submission rate . The benefit of a high usage rate is captured by the benefit (or gross value) function $V _ { i } ( \lambda )$ for each type-i customer, with its marginal valuation function $v _ { i } ( \lambda )$ and $V _ { i } ( 0 ) = 0 .$ The population measure of type-i potential customers is denoted by $f _ { i }$ for $i \in \mathcal { I } : = \{ 1 , 2 \}$ with $f : = f _ { 1 } + f _ { 2 }$ and $r : = f _ { 2 } / f$

The marginal valuation function is strictly downward sloping $( \mathrm { i } . \mathrm { e } . , v _ { i } ^ { \prime } ( x ) < 0$ for each $i \in \mathcal { I } )$ over $x \ge 0 .$ In addition, we assume that ${ v } _ { i } ( \cdot )$ strictly increases in $i \in \mathcal { I }$ for each value of the argument; that is, $v _ { 2 } ( x ) > v _ { 1 } ( x )$ for every $x \ge 0 .$ . It means that customers are ordered by the demand intensity; i.e., customers of high-type extract higher marginal benefit at every usage rate. It also implies that the benefit functions $V _ { i } ( \cdot )$ of different types never intersect except at zero. This single-crossing assumption is admittedly strong, but standard in the mechanism design literature, because it significantly simplifies the notation and analysis (Fudenberg and Tirole 1993). Because of different valuations, customers of different types use the network at different rates.

Let $\begin{array} { r } { \Lambda = \sum _ { i = 1 } ^ { 2 } \ f _ { i } \lambda _ { i } } \end{array}$ denote the total usage rates by subscribers. Note that a single customer’s increase in the job rate alone imposes no externalities to other jobs, because each customer has measure zero. We assume the capacity of the communications network is fixed. As more jobs are handled by the fixed capacity, the system performance deteriorates. The deterioration (e.g., busy signals, delays in delivery, and call drops) is summarized by the average waiting time function $W ( \Lambda )$ that is convex increasing and twice differentiable: i.e., $W ^ { \prime } ( \Lambda ) > 0$ and $W ^ { \prime \prime } ( \Lambda ) > 0 . \ c W ( \Lambda )$ is the average cost of congestion in terms of dollars. The fixed cost associated with the carrier’s fixed capacity is denoted by K.

## 3. The Menu of FUT Plans for a Profit-Maximizing Carrier

We consider a monopolistic carrier that sets the tariff to maximize his profit. The monopolist’s options are divided into two classes: two-plan tariffs and singleplan tariffs. We investigate each option.

The setting is modeled as a game that proceeds as follows. Each customer’s type i and the population distribution $f _ { i }$ are exogenously determined. The carrier, that knows $V _ { i } ( \cdot )$ and $f _ { i } ,$ but not the individual customer’s type, offers a menu of FUT plans. Given the menu, customers decide whether to subscribe or not, which plan to choose, and at what rate $\lambda _ { i } .$ Then, usage rates by individuals add up to the aggregate usage rate $\Lambda ,$ which determines the mean waiting time $W ( \Lambda )$

With the revelation principle, the carrier can maximize his profit by assuming that every type-i subscriber selects $( \pi _ { i } , \lambda _ { i } , p _ { i } )$ under the incentive compatibility constraints, where $\pi _ { i } , \lambda _ { i } .$ , and $p _ { i }$ are the fixed fee, the allowed usage rate, and the overlimit rate, respectively, for type-i subscribers. Let $P _ { i } ( \lambda _ { i } ^ { \circ } ) = \pi _ { i }$ + $p _ { i } ( \lambda _ { i } ^ { \circ } - \lambda _ { i } ) ^ { + }$ , where $( x ) ^ { + } = \operatorname* { m a x } \{ 0 , x \}$

Under the given menu of FUT plans, the (subgameperfect Nash) equilibrium $\{ \lambda _ { i } ^ { \circ } , \Lambda ^ { \circ } , \mathcal { I } ^ { \circ } \}$ satisfies the following:

(1) Individual Demand Relationship and Self-Selection. A type-i subscriber will choose the i-th plan and the usage rate $\lambda _ { i } ^ { \circ }$ at which her marginal value is equal to the marginal cost. The cost consists of two parts: (1) cash payment to the carrier and (2) the opportunity cost of waiting time incurred. Hence, with respect to a given $\Lambda ^ { \circ } , \lambda _ { i } ^ { \circ }$ satisfies

$$
V _ {i} \left(\lambda_ {i} ^ {\circ}\right) - P _ {i} \left(\lambda_ {i} ^ {\circ}\right) - c \lambda_ {i} ^ {\circ} W \left(\Lambda^ {\circ}\right) \geq V _ {i} (\lambda) - P _ {j} (\lambda) - c \lambda W \left(\Lambda^ {\circ}\right),
$$

$$
\forall \lambda > 0, i, j = 1, 2.\tag{1}
$$

(2) Subscriber Set. A subset ${ \mathcal { F } } ^ { \circ } \subset { \mathcal { F } }$ of customer types will subscribe to the carrier’s system. The subscription decision is based on whether the total cost of subscription and usage does not exceed the total value of the system at the equilibrium usage rate. Thus the subscriber set ${ \mathcal { F } } ^ { \circ }$ denotes the market penetration; that is,

$$
\mathscr {I} ^ {\circ} = \{i \mid V _ {i} (\lambda_ {i}) \geq c \lambda_ {i} W (\Lambda^ {\circ}) + P (\lambda_ {i}), \text {   for   some   } \lambda_ {i} \}.\tag{2}
$$

(3) Usage Rate to Carriers. Individual usage rates $\lambda _ { i } ^ { \circ }$ add up to the aggregate usage rate $\Lambda ^ { \circ }$

$$
\sum_ {i \in \mathcal {I} ^ {\circ}} \lambda_ {i} ^ {\circ} f _ {i} = \Lambda^ {\circ}\tag{3}
$$

The problem of choosing the tariff can be formulated as

$$
\max _ {(\pi_ {1}, \lambda_ {1}, p _ {1}), (\pi_ {2}, \lambda_ {2}, p _ {2}), \lambda_ {1} ^ {\circ}, \lambda_ {2} ^ {\circ}, \Lambda^ {\circ}, \mathscr {I} ^ {\circ}} f _ {1} P _ {1} (\lambda_ {1} ^ {\circ}) + f _ {2} P _ {2} (\lambda_ {2} ^ {\circ}) - K\tag{P0):}
$$

subject to (1), (2), and (3).

Throughout this paper, we assume that each subscriber will use the full amount of allowed usage rates and that no subscriber will use more than the limit. This is without loss of generality. To see this, suppose $( \pi _ { i } , \lambda _ { i } , p _ { i } )$ is offered to a type-i subscriber. If the carrier finds it optimal to induce a subscriber to use $\lambda _ { i } ^ { \circ } > \lambda _ { i } ,$ then the carrier can replace the current plan $( \pi _ { i } , \lambda _ { i } , p _ { i } )$ with a new one $( \pi _ { i } ^ { \prime } , \lambda _ { i } ^ { \circ } , p _ { i } ^ { \prime } )$ , while keeping the same level of revenue.<sup>2</sup>

<sup>2</sup> Consider a new plan $( \pi _ { i } ^ { \prime } , \lambda _ { i } ^ { \circ } , p _ { i } ^ { \prime } )$ with $\pi _ { i } ^ { \prime } = \pi _ { i } + p _ { i } ( \lambda _ { i } ^ { \circ } - \lambda _ { i } )$ and $p _ { i } ^ { \prime } \gg 0$ . Under the new plan, the subscriber maximizes her utility at $\lambda _ { i } ^ { \circ }$ . Because the subscriber’s utility is unchanged under the new plan, she has no incentive to switch plans. Note that the new plan is more expensive than the old plan—with one exception at $\lambda _ { i } ^ { \circ } ,$ , where the two plans charge the same amount $\pi _ { i } ^ { \prime } .$ Thus, a subscriber of the other type does not switch plans. We conclude that the new menu with the i-th plan replaced by $( \pi _ { i } ^ { \prime } , \lambda _ { i } ^ { \circ } , p _ { i } ^ { \prime } )$ is also optimal. On the contrary, if $\lambda _ { i } ^ { \circ } < \lambda _ { i }$ at optimality, we use a similar argument—the carrier can make a new plan $( \pi _ { i } , \lambda _ { i } ^ { \circ } , p _ { i } )$ for type-i subscribers while keeping the optimality. Hence, each subscriber will use the allowed rate—no more and no less.

Under this assumption, (1) can be written as

$$
V _ {i} \left(\lambda_ {i}\right) - \pi_ {i} - c \lambda_ {i} W (\Lambda) \geq V _ {i} \left(\lambda_ {j}\right) - \pi_ {j} - c \lambda_ {j} W (\Lambda), \quad i \neq j.
$$

The participation set ${ \mathcal { F } } ^ { \circ }$ at optimality is not given a priori, but must be endogenously determined as a result of the tariff design. It may be a two-plan tariff or may be single-plan tariffs. In what follows, we examine each case.

We first consider the case of two-plan FUT tariffs. The problem P 0 is restated as follows:

$$
(P 1) \colon \max _ {\pi_ {1}, \pi_ {2}, \lambda_ {1}, \lambda_ {2}, \Lambda} \left[ \sum_ {i = 1} ^ {2} f _ {i} \pi_ {i} - K \right]
$$

subject to

$$
V _ {1} \left(\lambda_ {1}\right) - \pi_ {1} - c \lambda_ {1} W (\Lambda) \geq V _ {1} \left(\lambda_ {2}\right) - \pi_ {2} - c \lambda_ {2} W (\Lambda)\tag{4}
$$

$$
V _ {2} (\lambda_ {2}) - \pi_ {2} - c \lambda_ {2} W (\Lambda) \geq V _ {2} (\lambda_ {1}) - \pi_ {1} - c \lambda_ {1} W (\Lambda)\tag{5}
$$

$$
\Lambda = f _ {1} \lambda_ {1} + f _ {2} \lambda_ {2}\tag{6}
$$

$$
V _ {i} (\lambda_ {i}) - \pi_ {i} - c \lambda_ {i} W (\Lambda) \geq 0, i = 1, 2.\tag{7i}
$$

Using the standard technique in the mechanism design literature, we obtain the following theorem.

Theorem 1. The optimal menu $\mathcal { M } ^ { \circ }$ of FUT plans is given by $\{ ( \pi _ { 1 } ^ { \circ } , \lambda _ { 1 } ^ { \circ } , p _ { 1 } ^ { \circ } ) , ( \pi _ { 2 } ^ { \circ } , \lambda _ { 2 } ^ { \circ } , p _ { 2 } ^ { \circ } ) \}$ , where (assuming an interior solution)

(a) $( \lambda _ { 1 } ^ { \circ } , \lambda _ { 2 } ^ { \circ } )$ satisfies

$$
v _ {2} (\lambda_ {2} ^ {\circ}) - c W (\Lambda^ {\circ}) - c \Lambda^ {\circ} W ^ {\prime} (\Lambda^ {\circ}) = 0\tag{8}
$$

$$
f v _ {1} (\lambda_ {1} ^ {\circ}) - f _ {2} v _ {2} (\lambda_ {1} ^ {\circ}) - f _ {1} c W (\Lambda^ {\circ}) - c f _ {1} \Lambda^ {\circ} W ^ {\prime} (\Lambda^ {\circ}) = 0\tag{9}
$$

$$
\Lambda^ {\circ} = f _ {1} \lambda_ {1} ^ {\circ} + f _ {2} \lambda_ {2} ^ {\circ}.\tag{10}
$$

(b) $( \pi _ { 1 } ^ { \circ } , \pi _ { 2 } ^ { \circ } )$ satisfies

$$
\pi_ {1} ^ {\circ} = V _ {1} (\lambda_ {1} ^ {\circ}) - c \lambda_ {1} ^ {\circ} W (\Lambda^ {\circ})\tag{11}
$$

$$
\pi_ {2} ^ {\circ} = V _ {2} \left(\lambda_ {2} ^ {\circ}\right) - V _ {2} \left(\lambda_ {1} ^ {\circ}\right) + \pi_ {1} ^ {\circ} - c \left(\lambda_ {2} ^ {\circ} - \lambda_ {1} ^ {\circ}\right) W \left(\Lambda^ {\circ}\right).\tag{12}
$$

(c) $p _ { i } ^ { \circ }$ is a constant, satisfying $p _ { i } ^ { \circ } \geq v _ { i } ( \lambda _ { i } ^ { \circ } ) - c W ( \Lambda ^ { \circ } )$ $f o r i = 1 , 2 .$

See the appendix for all proofs. We note here that Theorem 1 depends heavily on the single-crossing properties of valuation functions $V _ { i } .$ Note from (11), that the monopolist extracts all the surplus from lowtype subscribers. One sees from (12) that a high-type subscriber is indifferent between the two FUT plans.

Also, (12) with (11) implies that a high type retains an information rent.

Note also that the overlimit rates $p _ { i }$ do not play a critical role so far as they are large enough, because the usage rates beyond the allowance will never be reached in equilibrium by subscribers. Thus, overlimit charges can be viewed as a penalty to ensure subscribers use at the recommended rates. Indeed, in practice, the overlimit rates are three or four times the average rates of the allowance price (Verizon Wireless).

Corollary 1. The net profit to the carrier <sup>s</sup>, the average revenue per user (ARPU) A<sup>s</sup>, the net value of the system <sup>t</sup>, and the subscriber’s surplus <sup>c</sup> of type i are, respectively, given by

$$
\Pi^ {s} = f g _ {1} (\lambda_ {1} ^ {\circ}, \Lambda) - f _ {2} g _ {2} (\lambda_ {1} ^ {\circ}, \Lambda) + f _ {2} g _ {2} (\lambda_ {2} ^ {\circ}, \Lambda) - K,
$$

$$
A ^ {s} = g _ {1} (\lambda_ {1} ^ {\circ}, \Lambda) - r g _ {2} (\lambda_ {1} ^ {\circ}, \Lambda) + r g _ {2} (\lambda_ {2} ^ {\circ}, \Lambda)
$$

$$
\Pi^ {t} = \sum_ {i = 1} ^ {2} [ f _ {i} g _ {i} (\lambda_ {i} ^ {\circ}, \Lambda) ] - K,
$$

$$
\begin{array}{c} \Pi_ {1} ^ {c} = 0, \\ \Pi_ {2} ^ {c} = V _ {2} (\lambda_ {1} ^ {\circ}) - V _ {1} (\lambda_ {1} ^ {\circ}), \end{array}
$$

where $g _ { i } ( x , \Lambda ) : = V _ { i } ( x ) - c x W ( \Lambda ) , f o r \ i = 1 , 2 .$

The menu approach where the monopolist attempts to attract both types of customers is not always the optimal strategy. ${ \mathrm { I f } } ,$ for example, the number of lowtype customers is relatively small compared with that of high type $( \mathrm { i . e . , ~ } f _ { 2 } / f  1 )$ , the monopolist would rather ignore low-type customers and offer a single FUT plan targeted only at high-type customers. It may produce a superior outcome to the carrier, because in the menu approach, the monopolist cannot extract all consumer surplus from high type, while he can under a single FUT plan. We now turn to singleplan FUT tariffs.

Consider first an optimal single-plan FUT tariff $( \pi , \lambda , p )$ attracting both types of customers (often called a pooling plan). The corresponding optimization problem is equivalent to P1 with one more constraint $( \pi _ { 1 } , p _ { 1 } ) = ( \pi _ { 2 } , p _ { 2 } )$ . It is thus clear that a singleplan FUT tariff for both types cannot outperform its more general menu approach P1. In fact, it can be shown that the pooling plan never emerges as an optimal solution to P 1.

Next, suppose that the monopolist wants to design a single-plan tariff to attract one type. He has two choices depending on which type of customers to attract: (1) type 1 only and (2) type 2 only. A singleplan FUT tariff that appeals only to low types is not possible. If the plan is attractive to low types, then it is also attractive to high types. Thus, this class of tariffs becomes equivalent to the pooling plans that we earlier determined to be inferior. In contrast to the previous case, a single-plan FUT tariff that attracts only high types is possible.

It can be proved that there exists a cutoff point $r _ { 0 } \in ( 0 , 1 ] ,$ such that it is optimal for the carrier to use the optimal multiplan FUT tariff for $r \leq r _ { 0 } ,$ and to use the optimal, high-only single-plan FUT tariff for $r \geq r _ { 0 } ,$ where $r : = f _ { 2 } / f$ . Thus the monopolist may use either high-only single plans or a menu of FUT plans, depending on the relative size of the high-type market.

## 4. Nonlinear Pricing

Note that a FUT plan $( \pi _ { i } , \lambda _ { i } , p _ { i } )$ is a special case of nonlinear pricing with $h _ { i } ( \lambda ) = \pi _ { i } + p _ { i } ( \lambda - \lambda _ { i } ) ^ { + }$ +. Thus, optimal FUT plans cannot outperform optimal nonlinear pricing. Then, one might ask, What is the potential profit loss by restricting the search to FUT plans? As it turns out, a menu of general nonlinear pricing does not give any higher profit to the monopolistic carrier, and the optimal FUT menu is equally good. To show this, we formulate the search for an optimal menu  of nonlinear pricing as follows. For the moment, suppose that the menu is designed to attract both types of customers and consists of two nonlinear schedules. Then, $\mathcal { N } : = \{ h _ { i } ( \lambda _ { i } ) , i = 1 , 2 \}$ solves

$$
(P 2): \quad \max _ {h _ {i} (\cdot), \lambda_ {i}, \Lambda} \sum_ {i = 1} ^ {2} h _ {i} (\lambda_ {i}) f _ {i} - K
$$

subject to

$$
\lambda_ {i} = \arg \max _ {\lambda_ {i} ^ {\prime}} V _ {i} (\lambda_ {i} ^ {\prime}) - h _ {i} (\lambda_ {i} ^ {\prime}) - c \lambda_ {i} ^ {\prime} W (\Lambda),
$$

$$
i = 1, 2,\tag{13i}
$$

$$
\begin{array}{l} V _ {1} (\lambda_ {1}) - h _ {1} (\lambda_ {1}) - c \lambda_ {1} W (\Lambda) \\ \qquad \geq \max _ {\lambda_ {1} ^ {\prime}} [ V _ {1} (\lambda_ {1} ^ {\prime}) - h _ {2} (\lambda_ {1} ^ {\prime}) - c \lambda_ {1} ^ {\prime} W (\Lambda) ], \end{array}\tag{14}
$$

$$
V _ {2} (\lambda_ {2}) - h _ {2} (\lambda_ {2}) - c \lambda_ {2} W (\Lambda)
$$

$$
\geq \max _ {\lambda_ {2} ^ {\prime}} [ V _ {2} (\lambda_ {2} ^ {\prime}) - h _ {1} (\lambda_ {2} ^ {\prime}) - c \lambda_ {2} ^ {\prime} W (\Lambda) ],\tag{15}
$$

$$
V _ {i} (\lambda_ {i}) - h _ {i} (\lambda_ {i}) - c \lambda_ {i} W (\Lambda) \geq 0, i = 1, 2,
$$

$$
\Lambda = f _ {1} \lambda_ {1} + f _ {2} \lambda_ {2}.\tag{16i}
$$

(17)

A similar argument to §3 leads to the characterization of the optimal menu of nonlinear tariffs analogous to Theorem 1. Then, we find that an optimal solution to P2 can be implemented by a multiplan FUT tariff with the same usage rates and payments, and high enough overlimit charges as reported in the following theorem.

Theorem 2. An optimal multiplan FUT tariff is not dominated by nonlinear pricing.

This result—the key result of this paper—shows that the multiplan FUT tariff structure is not only simple in implementation, but also optimal in generating profit to the carrier. No other form of nonlinear pricing can outperform FUT plans. The underlying intuition is rather simple as follows. The effect of optimal nonlinear tariffs is essentially to offer a menu of two options, each specifying the allowed usage rate and the total payment, that satisfy both self-selection and participation constraints (i.e., (14) and 16i, respectively). These two options correspond to the kinks of the FUT plans in the space of (time, fee). Thus the FUT tariffs enforce the same equilibrium outcome (as the optimal nonlinear tariff) by heavily penalizing overlimit usage. Further, because the FUT is a special case of nonlinear tariff, the same options would satisfy the constraints. The same argument holds for single-plan tariffs. Note from this argument, that the theorem holds regardless of the single-crossing property, and that it holds for any number of types.

## 5. Conclusion

This paper studies the design of a tariff for the telecommunications service. We have developed an economic model to capture the negative externalities of the network, while allowing subscribers to choose the optimal usage rate based on the tariff. We study a simple tariff structure in wide use by wireless phone carriers that offers a menu of FUT plans. We derive the optimal menu of FUT plans and show that such a simple FUT menu structure delivers as good a performance as any other nonlinear pricing to the monopolistic carrier.

The model has a number of strong assumptions that need relaxation. First of all, the model assumes that the subscriber has no uncertainty in demand and has a fixed downward sloping demand curve. In practice, each subscriber faces uneven demand that fluctuates over time. This means that the subscriber may knowingly or unknowingly go beyond the allowance range, thus paying the overlimit charge, but the present model treats it as a nonequilibrium event. Suppose, by contrast, that the subscriber does not know the demand function at the time of choosing the plan. The subscriber would take the expectation of her demand and make the join/plan decisions. In this process, the subscriber faces a newsvendor type of trade-off between overage (when signing up for a high-allowance plan) and underage (for a low-allowance plan). Now, the overlimit charge p<sub>i</sub> becomes an important decision variable to the carrier, unlike the deterministic case where it was immaterial so far as it is large enough (Theorem 1(c)). The exact determination of p requires further analysis, but is of secondary interest to this work with its focus on the structure of the optimal tariff.

Second, we have assumed only two types of customers, but there may be more in reality. This extension is rather straightforward. A standard textbook or earlier economics work (in the agency or mechanism design literature, for example) has a rich set of tools to handle the problem of differentiating more than two types. In particular, the single-crossing assumption is unlikely to hold. If it fails, it may be necessary to offer less than N plans for N different customer types. A useful technique is available for bunching types (see Mussa and Rosen 1978 and Moorthy 1984). However, the main result (Theorem 2) will hold in general.

Third, this paper has assumed that all types have the same delay cost c. What if customers have different delay costs like in data communications (e.g., instant messaging versus music download)? The carrier may assign different priorities to different types through a menu of nonlinear tariffs, as was studied by Mendelson and Whang (1990) and Rao and Peterson (1998). One way to incorporate priority charges to FUT plans is charging different rates against the call time allowance, depending on the priority selected. Our conjecture is that the menu of FUT plans would be, again, as efficient as any nonlinear tariff but needs further investigation.

Fourth, Theorem 1 and other following results assume an interior solution. If the problem has a corner solution, then one type of customer is not worth serving because of their low valuation of the service. In this case, the carrier may prefer to offer a single-plan FUT tariff. Theorem 2 will continue to hold in this case.

Last, we have only considered a monopolistic carrier. In practice, multiple carriers compete in multiple dimensions like price structure, price level, and market segment. We hope that more research, theoretical and empirical, will follow to enrich our understanding of competitive tariffs in telecommunications markets. For example, it would be interesting to see if the market can sustain a mixed equilibrium, where one carrier offers a menu and another offers a high-only single plan. For example, a wireless carrier MetroPCS offers a single plan of unlimited local and longdistance calls at a fixed price, while other carriers offer a menu of FUT plans.

## Acknowledgments

The authors would like to thank the associate editor and the referees for offering valuable input on earlier drafts. In particular, their insightful comments were instrumental in refining the discussions concerning Theorem 2. The second author gratefully acknowledges the partial financial support from Global Supply Chain Forum at Stanford University.

## Appendix. Proofs

To solve P1, we start with the following two useful lemmas. Their proofs are standard in the mechanism design literature, so we omit them here. They are also available on request from the authors.

Lemma 1. Any feasible $( \lambda _ { 1 } , \lambda _ { 2 } )$ in (P1) satisfies $\lambda _ { 2 } > \lambda _ { 1 }$

Lemma 2.

(a) Constraints 7i and (5) imply 7i. That is, the monopolist should design the tariff only to ensure that low-type customers sign up. Then, high-type customers would automatically sign up.

(b) At optimality, constraint (5) holds in equality. High-type customers would be made to choose the high-usage plan feeling indifferent between high-usage and low-usage plans.

(c) Constraint (5) with equality implies (4). That is, the monopolist should be concerned that high-type customers do not move down to plan 1 (or the low-usage plan), but not that lowtype customers do not move up to the high-usage plan.

(d) At optimality, constraint 7i holds in equality. Low-type customers get zero net value, while high-type customers have some positive net value.

It should be noted that the single-crossing property plays a crucial role in Lemmas 1 and 2, hence in Theorem 1 as well.

Proof of Theorem 1. Using the lemmas, one can simplify P 1 as follows:

$$
(P A 1): \quad \max _ {\pi_ {1}, \pi_ {2}, \lambda_ {1}, \lambda_ {2}, \Lambda} \sum_ {i = 1} ^ {2} f _ {i} \pi_ {i} - K
$$

subject to

$$
V _ {2} (\lambda_ {2}) - \pi_ {2} - c \lambda_ {2} W (\Lambda) = V _ {2} (\lambda_ {1}) - \pi_ {1} - c \lambda_ {1} W (\Lambda)\tag{A.1}
$$

$$
\Lambda = f _ {1} \lambda_ {1} + f _ {2} \lambda_ {2}\tag{A.2}
$$

$$
V _ {1} (\lambda_ {1}) - \pi_ {1} - c \lambda_ {1} W (\Lambda) = 0.\tag{A.3}
$$

By applying the equalities (A.1) and (A.3) to the objective, one can further simplify PA1 and obtain $( \lambda _ { 1 } ^ { \circ } , \lambda _ { 2 } ^ { \circ } )$ by solving

$$
(P A 2): \quad \max _ {\lambda_ {1}, \lambda_ {2}, \Lambda} [ f g _ {1} (\lambda_ {1}, \Lambda) - f _ {2} g _ {2} (\lambda_ {1}, \Lambda) + f _ {2} g _ {2} (\lambda_ {2}, \Lambda) ]
$$

subject to

$$
\Lambda = f _ {1} \lambda_ {1} + f _ {2} \lambda_ {2},
$$

where $g _ { i } ( x , \Lambda ) : = V _ { i } ( x ) - c x W ( \Lambda )$ , for $i = 1 , 2 $ . This directly leads to the theorem. <sup></sup>

Proof of Theorem 2. After some standard analysis (similar to Lemma $^ { 2 ) , }$ we reduce the constraint set to the following four conditions: 13i, (15) in equality, 16i in equality, and (17). Let the optimal usage rates be denoted by $\lambda _ { i } ^ { n }$ . Given  , we can create a menu - of FUT plans affiliated with $\mathcal { N }$ as follows: $\mathscr { M } : = \{ ( \pi _ { 1 } ^ { m } , \lambda _ { 1 } ^ { n } , p _ { 1 } ^ { m } ) , ( \pi _ { 2 } ^ { m } , \lambda _ { 2 } ^ { n } , p _ { 2 } ^ { m } ) \}$ , where $\lambda _ { i } ^ { n }$ solves $( P 2 ) , \pi _ { i } ^ { m } : = h _ { i } ( \lambda _ { i } ^ { n } )$ , and $p _ { i } ^ { m }$ are some constants large enough. Then, the theorem can be shown as follows. Plug in $\lambda _ { i } = \lambda _ { i } ^ { n }$ and $h _ { i } ( \lambda _ { i } ^ { n } ) = \pi _ { i } ^ { m }$ in (14). Then, (17) and 16i imply (4), (6), and $( 7 i )$ if we instantiate the right-hand side of (14) and (15) with $\lambda _ { 1 } ^ { \prime } = \lambda _ { 2 } ^ { n }$ and $\lambda _ { 2 } ^ { \prime } = \lambda _ { 1 } ^ { n }$ . Because the feasible set of 16i and (17) is a subset of (4), (6), and 7i, - is feasible for the affiliated ${ \mathcal { N } } ,$ and an optimum in P1 is not dominated by an optimum in P 2. Hence follows the result. The result can be easily extended to the single-plan case: there always exists a single FUT plan that achieves the same performance as any nonlinear pricing schedule.

## References

Fudenberg, D., J. Tirole. 1993. Game Theory. The Massachusetts Institute of Technology Press, Cambridge, MA.

Hassin, R., M. Haviv. 2003. To Queue or Not to Queue: Equilibrium in Queueing Systems. Kluwer Academic Publishers, Dordrecht, The Netherlands.

Mendelson, H. 1985. Pricing computer services: Queueing effects. Comm. ACM 28 312–321.

Mendelson, H., S. Whang. 1990. Optimal incentive-compatible pri ority pricing for the M/M/1 queue. Oper. Res. 38 870–883.

Moorthy, S. 1984. Market segmentation, self-selection, and product line design. Marketing Sci. 31 288–307.

Mussa, M., S. Rosen. 1978. Monopoly and product quality. J. Econom. Theory 18 301–317.

Naor, P. 1969. On the regulation of queue size by levying tolls. Econometrica 37 15–24.

Oi, W. Y. 1971. A Disneyland dilemma: Two-part tariffs for a Mickey Mouse monopoly. Quart. J. Economics 86 77–90.

Rao, S., E. R. Peterson. 1998. Optimal pricing of priority services. Oper. Res. 46(1) 46–56.

Verizon Wireless. http://www.verizonwireless.com/.

Wilson, R. 1993. Nonlinear Pricing. Oxford University Press, Oxford, UK.

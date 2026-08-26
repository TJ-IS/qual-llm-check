---
otero_id: 26644
otero_key: "D8MZKWCJ"
title: "Free-Access Policy for Internal Networks"
authors: "P. S. Giridharan; Haim Mendelson"
year: "1994"
journal: "Information Systems Research"
doi: "10.1287/isre.5.1.1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [129.105.215.146] On: 09 July 2018, At: 11:21 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/D8MZKWCJ/fulltext/images/4f049a3013ff1a89fcc04a75ff692be589868bfd948639ed0e28a62b9e9a60d2.jpg)

## Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Free-Access Policy for Internal Networks

P. S. Giridharan, Haim Mendelson,

To cite this article: P. S. Giridharan, Haim Mendelson, (1994) Free-Access Policy for Internal Networks. Information Systems Research 5(1):1-22. https://doi.org/10.1287/isre.5.1.1

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1994 INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Free-access Policy for Internal Networks

P. S. Giridharan

Graduate School of Industrial Administration

Carnegie Mellon University

Pittsburgh, Pennsylvania 15213

Haim Mendelson

Graduate School of Business

Stanford University

Stanford, Californıa 94305-5015

This paper evaluates the free-access policy as a control mechanism for internal networks. We derive the optimal message pricing scheme, compare it to the free-access policy, and study the associated net-value loss. We derive uniform upper bounds on this value loss, and apply our results to the polar implementations of ethernet and token ring networks. The results show that the free-access policy is often attractive.

Pricing—Computer networks--Free-access

## 1. Introduction

The past few years have witnessed an increasing role for data communications. A , recent survey of U.S. corporations (Roeckl 1989) indicates that 59% have private networks, and data communications expenses as a percentage of total data-processing spending has grown almost fourfold between the early seventies and 1987 (Mendelson 1993). The growing use of data communications networks in organizations raises a host of issues pertaining to their management and control, the objective being to make their operation consistent with overall organizational goals. This paper addresses the desirability of implementing a pricing scheme to control the use of such networks.

Diverse incentives arise in data communications due to externalities which may be positive or negative. In general, positive externalities exist when the actions of a decision maker (acting in his or her own self-interest) create beneficial side-effects for others. In telecommunications, positive externalities arise when a message creates value to the system as a whole—in particular to the receiver—in addition to its value to the sender. Negative externalities generally arise when the self-interest driven actions of an individual impose costs on others. In data communications, each message increases the delay of other messages in the network. By adding to the message load, the user generating the message inflicts costs on other users, resulting in negative externalities. The effect of both externalities is a divergence between the costs and benefits as perceived by individual users and those pertaining to the organization as a whole.

Transfer prices can play a useful role in controlling externalities. They can create incentives that induce members—while acting in their own best interests—-to behave so that they jointly maximize the overall net value of the organization (Mendelson 1985, 1993; Mendelson and Whang 1990; Dewan and Mendelson 1990). However, the implementation of a transfer-pricing scheme may be costly, and organizations often do not charge for the use of internal networks (McWilliams 1987). A free-ac cess policy, whereby the members are not charged for generating messages, avoids these costs, but on the other hand the resulting usage pattern may not be optimal Thus, there is a tradeoff between the costs of implementing a pricing scheme and the value loss due to suboptimal behavior under the free-access policy. This tradeoff is the main subject of this paper.

We quantify the net-value loss due to the free-access policy, study its determinants, and derive conditions under which the free-access policy is an attractive policy choice; and those under which it is not. We derive both the exact net-value loss and uniform upper bounds on its magnitude. The bounds are powerful as they pertain to any set of downward-sloping marginal value functions.

There is a vast literature on positive externalities in interorganizational communications networks, particularly with respect to determining their optimal size. Examples include Artle and Averous (1973), Gravelle (1972), Littlechild (1970, 1975), Oren et al. (1982), Rohlfs (1974), and Squire (1973).

Negative externalities have traditionally received some attention——if indirect—in the area of performance evaluation, where the message delay as a function of network parameters is quantified (see, e.g., Hammond et al. (1986), Stallings (1984)). More broadly, the queueing theory literature includes a number of contributions in the area of queue control to achieve desirable objectives. Naor (1969) was the first to study differences between “social" and “individual" optimization in the context of the M/M/1 queueing system. Balachandran (1972) considers payments to purchase priorities and discusses possible divergence between social and individual optimization. Yechiali (1971, 1972) and Mendelson and Yechiali (1981) extend Naor's (1969) results to more general queueing situations. Adiri and Yechiali (1974) and Alperstein (1988) consider the case of multiple priority classes. Balachandran and Schaefer (1979, 1980) (hereafter, B&S) consider the issue of class dominance when there are multiple classes. B&S (1979) show that for public optimality, one user class will dominate the usage of the facility. B&S (1980) show that with an upper limit on utilization, public optimality calls for diversification, but the objective function is not well behaved. Their methodology and results are discussed in §2 and applied to our setting in §§4 and 5. Radhakrishnan (1991) compares the performance of cost application (job pricing) mechanisms with group incentive mechanisms (i.e., incentive schemes based on overall performance measures) in the presence of negative externalities, hidden information, and hidden action. Studying the impact of delay costs on optimal capacity and its utilization, Mendelson (1985) has shown how negative externalities affect the management and control of computer systems. Mendelson and Whang (1990) and Dewan and Mendelson (1990) generalize his results to the cases of multiple-user classes and nonlinear delay cost functions. These results, however, do not incorporate a divergence between the organization and the individual users either in terms of the value experienced or in the opportunity costs of time. In this paper, we study the control problem for an internal network with a general externality structure, focussing on a comparison of the “optimal" pricing policy to a free-access policy.

We present our model in §2. We derive the optimal per-message pricing scheme in §3. We analyze the free-access policy in §4. We present our results on the magnitude of the net-value loss and discuss extensions to our results in §5. Our concluding remarks are in §6.

## 2. The Model

We consider members of an organization who are interconnected through a data communications network. The members generate messages that have value both to the senders and to the organization. Whenever a member (considering her own interests) sends messages to another member over the network, the rest of the system in general, and the receiver in particular, may also benefit from the message. On the other hand, there is also a deleterious effect on the system due to increased congestion and delays. Thus, we can distinguish between two types of externalities, according to their source: value externalities that arise because of differences between the perceived value of the message to the sender and its value to the organization, and congestion externalities that result from the contention over network resources.

In general, value externalities represent the additional value of messages which is not perceived by their senders. The decision to initiate a message is made from the sender's perspective, which may not capture the full value of the message. Since the senders consider only the benefits accruing to them while initiating messages, the rest of the value forms a positive externality. While value externalities are often positive, they may also be negative, depending on whether the value of the message to the organization is higher or lower than the value perceived by the sender.

As a simple example of positive value externalities, consider a sales representative who has just received a list of product defects from a customer and communicates it to the quality control department. The sales representative's objective in sending the communication may be to “make the customer happy," and she may consider only this benefit when sending the message. On the other hand, the quality control department also values information that can be used to improve the product sold to other customers as well. Over and above the value perceived by the sales representative and the quality control department, the organization may potentially derive yet more benefits, such as increased quality-consciousness, which are not directly perceptible, but which ultimately add value to the organization. Thus, the message has value that is perceived by the sales representative and the quality control department as well as a residual value seen by the organization as a whole. While all three components add value to the organization, the sales representative may reckon only with her benefits, and the rest of the value is a positive externality accruing to the organization (of course, this depends on the incentive schemes employed by the organization).

Negative value externalities can arise when the message benefits the sender directly, say in the form of a perquisite, but its effect on the organization is deleterious. As a concrete example, a message from a project member to another may consist of the following components: some personal correspondence, some information relevant to the project, and some unauthorized classified information. The first part benefits the member but has no value impact on the organization and thus does not have any value externality.' The second part adds value to the organization, and usually at least some of it will be perceived by the sender. The value that does not accrue to the sender constitutes a value externality (whether it is positive or negative depends on the relative values accruing to the organization and to the sender). The third part may add value to the sender but is harmful to the organization, thereby constituting a negative externality.

In a communications network, congestion externalities arise because the capacity of the communications channel is limited. As a member sends messages through the network, she increases the congestion and hence the delay faced by all other messages. This problem becomes acute as the message rate increases. Its impact depends on the opportunity cost of time, i.e., the value loss due to a unit-time delay in the transfer of a message.

As described above, data communications networks are characterized by both positive and negative externalities. The organization aims to induce its members to generate messages so that the net-value of the message flow is maximized. We study a network supporting N types of messages, 1, $2 , \ldots , N$ . We denote by $\lambda _ { \iota }$ the expected rate of type-i messages. We allow for stochastic variation in the message lengths, assuming that they are independent and identically distributed (i.i.d). The gross value of type-i messages to their senders when their arrival rate is $\lambda _ { \iota }$ is given by the senders' value function $S _ { \iota } ( \lambda _ { \iota } )$ . The gross value of type-i messages to the organization is given by $V , ( \lambda , )$ (all values and costs are per unit time). For all $i ,$ the functions $S _ { \imath } ( \cdot )$ and $\mathcal { V } _ { t } ( \cdot )$ are assumed to be nondecreasing, weakly concave, and twice differentiable.

The network is modeled as a queueing system with an aggregate capacity (= average number of messages it can support per unit time) of μ (cf. Kleinrock (1975)). We denote by $\begin{array} { r } { \lambda , \lambda = \sum _ { \ i } \lambda _ { \iota } } \end{array}$ , the system-wide message rate. Without loss of generality, we let $\mu = 1$ , implying that λ is also the capacity utilization of the channel. Because network resources are limited, each message experiences a delay. The expected time a message spends in the system is $W ( \lambda )$ , the expected number of messages in the system is $L ( \lambda )$

We next consider the opportunity cost of time. Just as the sender may perceive only part of the value of a message, she may take into account only a fraction of the delay cost. For example, the overall delay cost may be split between the sender and the receiver. To illustrate, consider the sales representative discussed earlier. Each day's delay in rectifying the defects may inflict a cost on the sales representative (e.g., in the form of lost commissions) because of lost business with that particular customer. This is the opportunity cost reckoned by the sales representative. However from the organization's point of view, the delay cost may actually be larger. For example, if the product is sold to several customers, there is a potential loss with respect to each customer due to each day's delay in rectifying the defects.

To reflect this reality, we generalize the delay-cost structure to allow the opportunity costs of time for the senders of type-i messages, denoted by $b _ { s , \iota }$ , to be different from the organizational opportunity cost of time, ${ b . } ^ { 2 }$ We denote by $\alpha _ { \iota }$ the fraction of the system-wide (organizational) delay cost that is perceived by the senders of type-i messages, i.e.. $\alpha _ { \iota } = b _ { s , \iota } / b$ . We assume $\alpha _ { \iota } \geq 0 \colon$ ; in the interpretations of our results, we discuss the plausible case $\alpha _ { \iota } \leq 1 ( \mathrm { i } . \mathrm { e } . , \mathrm { } \mathbf { a }$ fraction of the delay cost is perceived by the senders), although this assumption is not required for the analysis. Thus, the delay cost perceived by the senders of type-t messages per unit time is $\alpha _ { \iota } \cdot b$

The overall externality structure is summarized by the function

$$
k _ {i} (\lambda_ {i}) = \frac {S _ {i} ^ {\prime} (\lambda_ {i})}{\alpha_ {i} V _ {i} ^ {\prime} (\lambda_ {i})},
$$

which we call the index of self-interest. It is the ratio of the fractions of system-wide marginal value and marginal delay cost accruing to the senders of type-i messages

Under our model, the expected system-wide delay cost is given by $b \cdot L ( \lambda )$ . We assume that $L ^ { \prime } ( \lambda )$ —and hence the expected system-wide marginal delay cost function, $b \cdot L ^ { \prime } ( \lambda ) { \mathrm { - } } { \mathrm { i } } s$ an increasing function of the capacity utilization λ. This reflects the fact that the expected number of messages in the system typically increases at an increasing rate as its utilization increases. Similarly, we assume that $W ( \lambda )$ is an increasing function of ${ \lambda . ^ { 3 } \ \mathbf { W } \mathrm { e } }$ further assume that the system gets saturated as λ approaches unity. These standard assumptions are satisfied by virtually all existing performance models of communication networks, which typically also assume Poisson arrivals (see Hammond and OReilly (1986) for several examples). In particular they are satisfied by the specific structures studied in §5.

As part of our analysis, we take advantage of the analysis in B&S (1979, 1980). where the marginal value curve in each class is flat (i.e., all jobs within a class have the same value). B&S (1979) show that both private and social optimization lead to “class dominance" phenomena whereby only users from a dominant class (or classes) will use the system, and that the dominant classes may be different under the optimal and free-access regimes. The discrete modelling approach taken by B&S inspired the result of Theorem 2, and an extension of their class-dominance result helps establish the general result of Theorem 4. To facilitate comparisons with B&S (1979), we use the terms “type" and “class" interchangeably.

## 3. Optimal Pricing Policy

In this section we derive the optimal pricing policy in the presence of both value and congestion externalities, different message types, and allowing for differences between the organizational delay cost and the delay costs perceived by the senders. The organization's net-value maximization problem is

$$
\max _ {\lambda_ {1}, \lambda_ {2}, \dots , \lambda_ {N}} \left\{\sum_ {i = 1} ^ {N} V _ {i} (\lambda_ {i}) - b \cdot L (\lambda) \right\},\tag{1}
$$

where $\begin{array} { r } { \lambda = \sum _ { i = 1 } ^ { N } \lambda _ { \iota } } \end{array}$ . When all the marginal value curves are flat, there will be class dominance, if there is no upper limit on utilization (Balachandran and Schaefer 1979), and diversification if there is an upper limit on utilization (Balachandran and Schaefer 1980). In the case of general downward-sloping marginal value curves, the first-order condition for type-i messages is $V _ { , } ^ { \prime } ( \lambda _ { } ^ { * } ) = - b \cdot L ^ { \prime } ( \lambda ^ { * } )$ 4

Mendelson (1985) has shown that when only congestion externalities are present pricing can be used to induce the desired arrival rate by charging users the negative externality term. In the current setting, intuition suggests that members should be “penalized" for any negative externalities they impose on others but also “rewarded" for any positive externalities they confer. Thus, for each message generated, the originator should be charged a monetary price equal to minus the sum of the value (positive or negative) and congestion (always negative) externalities that result from the marginal message (at the optimum). When each member takes this price (as well as her own value function and delay cost) into account, the resultant arrival rates are optimal for the system as a whole. The following theorem formalizes this notion.

THEOREM 1. The optimal price $p _ { \iota } ^ { * }$ for type-i messages is given $b \nu$

$$
p _ {i} ^ {*} = (1 - \alpha_ {i}) \cdot b \cdot W (\lambda^ {*}) + b \cdot \lambda^ {*} \cdot W ^ {\prime} (\lambda^ {*}) - [ V _ {i} ^ {\prime} (\lambda_ {i} ^ {*}) - S _ {i} ^ {\prime} (\lambda_ {i} ^ {*}) ].\tag{2}
$$

PRooF. The senders of type-t messages will increase the message rate $\lambda _ { \iota }$ to the point where $S _ { \iota } ^ { \prime } ( \lambda , )$ is equal to the overall cost they perceive for their marginal message. This overall cost is the sum of the delay cost they bear and the monetary price they pay per message. We wish to induce the arrival rate ${ \boldsymbol { \lambda } } _ { \iota } ^ { * }$ satisfying the first-order optimality condition $V _ { \prime } ^ { \prime } ( \lambda _ { \iota } ^ { * } ) = \boldsymbol { b } \cdot \boldsymbol { L } ^ { \prime } ( \lambda ^ { * } )$ . Using Little's Law $( L = \lambda \cdot W )$ and its derivative $( L ^ { \prime } = W + \lambda \cdot W ^ { \prime } )$ , we obtain at the optimum

$$
\begin{array}{r l} S _ {i} ^ {\prime} (\lambda_ {i} ^ {*}) & = S _ {i} ^ {\prime} (\lambda_ {i} ^ {*}) + b \cdot L ^ {\prime} (\lambda^ {*}) - V _ {i} ^ {\prime} (\lambda_ {i} ^ {*}) = b \cdot L ^ {\prime} (\lambda^ {*}) - [ V _ {i} ^ {\prime} (\lambda_ {i} ^ {*}) - S _ {i} ^ {\prime} (\lambda_ {i} ^ {*}) ] \\ & = b \cdot W (\lambda^ {*}) + b \cdot \lambda^ {*} \cdot W ^ {\prime} (\lambda^ {*}) - [ V _ {i} ^ {\prime} (\lambda_ {i} ^ {*}) - S _ {i} ^ {\prime} (\lambda_ {i} ^ {*}) ] \\ & = \alpha_ {i} \cdot b \cdot W (\lambda^ {*}) + (1 - \alpha_ {i}) \cdot b \cdot W (\lambda^ {*}) \\ & + b \cdot \lambda^ {*} \cdot W ^ {\prime} (\lambda^ {*}) - [ V _ {i} ^ {\prime} (\lambda_ {i} ^ {*}) - S _ {i} ^ {\prime} (\lambda_ {i} ^ {*}) ]. \end{array}\tag{3}
$$

The first term on the right-hand side of Equation (3) is the delay cost incurred by the originator of the message, which is already taken into account in her decisions. Hence, the monetary price to be charged is given by (2). Q.E.D.

The first term on the right-hand side of Equation (2) represents the portion of the delay cost of the marginal message which is not borne by the sender. The second term is the marginal delay cost imposed on others due to the increase in the queueing delay for other messages (see Mendelson (1985)). The sum of the first two terms thus represents the negative externality of the marginal message. The third (bracketed) term is the difference between the organizational marginal value of type-i messages and the senders' perceived marginal value, and represents the positive externality of the marginal type-i message. Hence, the price to be charged is equal to the difference between the negative and positive externalities created by the marginal type-i message. Figure 1 depicts the pricing scheme of Theorem 1 graphically.

The implementation of the pricing policy recommended by Theorem 1 is not costless. The main problem is an information problem: the solution requires the knowledge of functions that are extremely difficult to determine in practice. First, we need information on the performance functions, L and W, as well as the organization's opportunity cost of time, b. Then, we need to know, for each message type, the value of the messages to the system, the value of the messages to the senders, and the opportunity cost of time for a message of that type. Clearly, it is difficult to determine all the relevant parameters.

The optimal price to be charged for sending messages may actually be negative. This may happen when the positive externalities are relatively high or when the negative externalities are relatively low. The first situation may, for example, occur in a case where engineers work on different parts of a design and communicate through a network to exchange images. The latter may occur when the opportunity cost of time b, is low, or when the communications delays are themselves low (e.g., due to an ample capacity). In these cases, the members have to be actually paid for generating the messages. Clearly, there are practical problems associated with this, such as incen-

![](/api/attachments/D8MZKWCJ/fulltext/images/4557fda8710f4b42d993384820b84b1e6c1248262d46b6d454054b6a7d555018.jpg)  
FIGURE 1. Opumal Pricing

$V ^ { \prime } : \mathbf { \mathfrak { s } }$ the overall marginal value function, obtained as the horizontal summation of the N type-t marginal value functions $V _ { \prime } ^ { \prime }$

$\mathbf { \boldsymbol { J } } ^ { \prime \prime } { } _ { 1 } ^ { \prime }$ is the marginal value curve for type-1 messages.

$S _ { \mathrm { ~ 1 ~ } } ^ { \prime }$ is the senders' marginal value curve for type-1 messages.

b • Èis the expected overall delay cost for the marginal message. $\alpha _ { 1 } \cdot b \cdot H ^ { \prime }$ is the fraction of the expected delay cost for the marginal type-1 message that is perceived by the senders. $b \cdot L ^ { \prime }$ is the overall expected marginal delay cost function.

The optimal arrival rates. ${ \lambda } _ { \iota } ^ { * } .$ , are obtained by equating the marginal value functions $V ^ { \prime } ( \lambda , )$ to the marginal delay cost function, $b \cdot L ^ { \prime } ( \lambda )$ . The arrival rate ${ \boldsymbol { \lambda } } _ { 1 } ^ { * }$ for type-1 messages is induced by pricing type-1 messages as follows

$O C _ { \mathrm { i } }$ (or ${ \boldsymbol { \alpha } } _ { 1 } \cdot { \boldsymbol { b } } \cdot { \boldsymbol { W } } ^ { \prime }$ ) is the privately-perceived delay cost, which is borne by the senders of type-1 messages and hence need not be included in the price

$C _ { 1 } C _ { 2 }$ is equal to $\mathrm { ~ ( ~ 1 ~ - ~ } \alpha _ { 1 } \mathrm { ) } \cdot b \cdot W$ , which is the fraction of the delay cost of the marginal message which is not borne by its sender and hence needs to be charged

$C _ { 2 } C _ { 4 }$ is the congestion externality (Mendelson 1985) inflicted on others, which is not perceived by the sender and hence needs to be charged

$C _ { 3 } C _ { 4 }$ is the value externality for type-1 messages, $\{ { \mathbb { V } } _ { 1 } ^ { \prime } ( \lambda _ { 1 } ^ { * } ) - S _ { 1 } ^ { \prime } ( \lambda _ { 1 } ^ { * } ) \}$ , which is positıve in this example. The value externality needs to be subtracted from the optimal price in order to induce the senders of type-1 messages, who perceive a marginal value of $S _ { \textbf { i } } ^ { \prime } ( \lambda _ { 1 } ^ { * } )$ , to take into account the full marginal value of their messages to the organization, which is $V ^ { \prime } ( \lambda _ { 1 } ^ { * } )$ . The optimal price is $p _ { 1 } ^ { * } = C _ { 1 } - C _ { 1 } ^ { * }$

tives to create “junk" messages. At the frivolous extreme, it may induce a member to pay those willing to generate useless messages on his or her behalf.

Another facet of the information problem is the incentive-compatibility issue discussed (for the case of pure congestion externalities) by Mendelson and Whang (1990) and Radhakrishnan (1991): since the optimal pricing scheme discriminates between the different message types, users have an incentive to classify their messages as belonging to the more desirable classes. When the administrator cannot tell what class any given message belongs to, this makes pricing difficult to implement. In particular, message types with large positive externalities may call for heavy price discounts and (as discussed above) their senders may in fact have to be paid in order to induce the optimal message rates. No doubt, users will be tempted to classify their messages into these types, resulting in substantial administration problems.

Finally, there is an accounting overhead involved when a pricing mechanism is used. This includes keeping track of the messages sent from every member to every other member, billing the members and making the collections. Thus, while pricing can be used to solve the externality problems in intraorganizational networks, it is not costless and is not always implementable. In the absence of pricing, the above problems are avoided—but users may use the network suboptimally. This calls for balancing the losses due to the free-access policy against the costs of pricing, especially in light of the fact that the positive and negative externalities may have a mutually-balancing effect on the optimal price to be charged. Hence, a free-access policy may well be attractive, depending on the associated (net) value loss. This loss is assessed in the next section.

## 4. Free-access Policy

In the previous section, we showed how pricing can be used to align the incentives of individual members with the objective of the organization. We then discussed the costs and difficulties of implementing an optimal pricing scheme. A free-access policy whereby the members are not charged for generating messages allows the organization to avoid these costs as well as the need to determine the various system parameters. On the other hand, there is no guarantee that the resulting message rate will be the optimal one for the organization. The tradeoff is then between the costs of implementing a pricing scheme and the value loss due to suboptimal behavior in its absence.

In what follows, we study the net-value loss due to a free-access policy compared to the optimal pricing policy. We consider an organization that uses the free-access policy and evaluate by how much it can increase the net-value of the network by optimally pricing network services. This enables us to determine under what conditions free-access is an attractive policy option. We use the following notational conventions: The superscript \* denotes the value of a variable taken at the optimal solution, and the subscript $F$ denotes its value under the free-access policy, e.g., ${ \lambda } _ { \iota } ^ { * }$ and $\lambda _ { \iota , F }$ denote the optimal arrival rate and the free-access arrival rate, respectively, for type-i messages. Recall that $k _ { \iota } ( \lambda _ { \iota } )$ denotes the index of self-interest for senders of type-i messages as a function of the message rate. In particular, we denote by $k _ { \iota }$ (without the argument) the index of self-interest at the free-access message rate of type-i messages.

Under the free-access policy, the arrival rates, $\lambda _ { \iota , F } ,$ will be the results of the senders cost-benefit analysis. The benefit of the marginal type-i message is $S _ { \imath } ^ { \prime } ( \lambda _ { \imath } )$ , which is downward-sloping. On the cost side, since there are no monetary costs under the free-access policy, the expected cost of the marginal type-i message is its expected delay cost, $b _ { s , \iota } \cdot W ( \lambda )$ , which is upward-sloping. When the marginal value curves are all horizontal, there will be a class dominance as shown in B&S (1979). In the case of general downward-sloping demand curves, the first-order condition for the arrival rate of type-i messages under the free-access policy is

$$
S _ {t} ^ {\prime} \left(\lambda_ {t, F}\right) = b _ {s, t} \cdot W \left(\lambda_ {F}\right).\tag{4}
$$

Using the definitions of $k _ { \iota }$ , Equation (4) reads

$$
V _ {1} ^ {\prime} (\lambda_ {1, F}) = b \cdot \frac {W (\lambda_ {F})}{k _ {t}},\tag{5}
$$

where $k _ { t }$ are evaluated at the free-access arrival rates, $\lambda _ { t , F } .$

The object of study here is $\Delta N V ,$ , the net-value loss because of the free-access policy compared to the optimal pricing policy. We distinguish between three types of marginal value curves (within each class i): a flat marginal value curve, corresponding to a fixed marginal value $V _ { \iota } ^ { \prime }$ for all $\lambda _ { \iota }$ ; a stepwise marginal value curve with marginal value $V _ { \prime } ^ { \prime }$ for $\lambda _ { t } \le a _ { t } ^ { m }$ and zero thereafter $( a _ { \iota } ^ { m }$ is the maximum arrival rate for class i); and a general nonincreasing marginal value curve. In Theorem 2, we find the exact expected net-value loss for the case of stepwise marginal value curves, where the optimal solution satisfies the class dominance condition of B&S (1979). This result is useful since an arbitrary downward-sloping marginal value function can be approximated, to any desired precision, by a sequence of stepwise curves. In Theorem 3, we consider the general case and derive the maximum expected net-value loss. As it turns out, the results for the different cases are related since the maximum expected net-value loss is attained for flat marginal value curves.

## 4.1. Stepwise or Flat Marginal Value Curves

Consider the case where the marginal value curves are either stepwise or flat. We can assume without loss of generality that the marginal values satisfy $V _ { 1 } ^ { \prime } \geq V _ { 2 } ^ { \prime } \geq          \cdots$ $\ge V _ { N } ^ { \prime } . \ \mathbf { B y } \left( 5 \right)$ , we must have $k _ { 1 } \le k _ { 2 } \le \cdots \le k _ { \scriptscriptstyle { \Lambda } }$ . Hence, the expected net-value under the free-access policy, $N V _ { F } ,$ , is given by

$$
N V _ {F} = \sum_ {i = 1} ^ {N} \lambda_ {i, F} \cdot V _ {i} ^ {\prime} (\lambda_ {i, F}) - b \cdot L (\lambda_ {F}).\tag{6}
$$

Using Equation (5), we get

$$
\begin{array}{r l} N V _ {F} & = \sum_ {i = 1} ^ {N} \lambda_ {i, F} \cdot b \cdot \frac {W (\lambda_ {F})}{k _ {i}} - b \cdot L (\lambda_ {F}) \\ & = \sum_ {i = 1} ^ {N} \lambda_ {i, F} \cdot b \cdot \frac {W (\lambda_ {F})}{k _ {i}} - b \cdot \lambda_ {F} \cdot W (\lambda_ {F}), \end{array}
$$

where the last equality follows from Little's Law. Factoring b and $W ( \lambda _ { F } )$ out, we obtain the expected net value under the free-access policy

$$
N V _ {F} = b \cdot W (\lambda_ {F}) \cdot \left[ \sum_ {i = 1} ^ {N} \frac {\lambda_ {i , F}}{k _ {i}} - \lambda_ {F} \right].\tag{7}
$$

Next consider the optimal net value. We examine first the case of a single class (N $= 1 )$ with a flat marginal value $V _ { 1 } ^ { \prime }$ . Let $\lambda _ { M } ^ { * }$ denote the optimal system-wide arrival rate. Then, ${ \lambda } _ { M } ^ { * }$ must satisfy the first-order condition $V _  \mathrm { ~ \scriptsize ~ \} } ^ { \prime \prime } = b \cdot L ^ { \prime } ( \lambda _ { M } ^ { * } )$ . Note that if $\boldsymbol { \mathbf { \mathit { J } } ^ { \prime \prime } } _ { 1 }$ $\leq b \cdot L ^ { \prime } ( 0 )$ , then the optimal arrival rate is zero. Since $V _ { 1 } ^ { \prime } = b \cdot W ( \lambda _ { F } ) / k _ { 1 }$ , we get

$$
L ^ {\prime} \left(\lambda_ {M} ^ {*}\right) = \max \left\{\frac {W \left(\lambda_ {F}\right)}{k _ {1}}, L ^ {\prime} (0) \right\}.
$$

If the optimal arrival rate ${ \lambda } _ { M } ^ { * }$ is zero, then the optimal net-value is also zero. $\operatorname { I f } \lambda _ { M } ^ { * }$ is not zero, then the optimal expected net-value to the system is given by

$$
N V ^ {*} = V _ {1} \left(\lambda_ {M} ^ {*}\right) - b \cdot L \left(\lambda_ {M} ^ {*}\right) = \lambda_ {M} ^ {*} \cdot V _ {1} ^ {\prime} - b \cdot L \left(\lambda_ {M} ^ {*}\right),\tag{8}
$$

since $V _ { \mathrm { ~ 1 ~ } } ^ { \prime }$ is constant. Further since $V _ { \mathrm { ~ 1 ~ } } ^ { \prime } = b \cdot L ^ { \prime } ( \lambda _ { M } ^ { * } )$ , we get from Little's Law

$$
N V ^ {*} = b \cdot \lambda_ {M} ^ {*} \cdot L ^ {\prime} (\lambda_ {M} ^ {*}) - b \cdot L (\lambda_ {M} ^ {*}) = b \cdot \lambda_ {M} ^ {*} \cdot L ^ {\prime} (\lambda_ {M} ^ {*}) - b \cdot \lambda_ {M} ^ {*} \cdot W (\lambda_ {M} ^ {*}).\tag{9}
$$

Using the derivative of Little's Law $( L ^ { \prime } = \lambda \cdot W ^ { \prime } + W ^ { \prime } )$ and rearranging terms, we get

$$
N V ^ {*} = b \cdot \lambda_ {M} ^ {* 2} \cdot W ^ {\prime} (\lambda_ {M} ^ {*}).\tag{10}
$$

Note that (10) holds also in the case where ${ \lambda } _ { M } ^ { * } = 0$ . Comparing (7) and (10), the expected net-value loss is given by

$$
b \cdot \lambda_ {M} ^ {* 2} \cdot W ^ {\prime} (\lambda_ {M} ^ {*}) + b \cdot W (\lambda_ {F}) \cdot \left[ \lambda_ {F} - \sum_ {i = 1} ^ {N} \frac {\lambda_ {i , F}}{k _ {i}} \right].
$$

This result is directly generalizable to the stepwise multiple-class case:

TíEOREM 2. If the marginal value curve of each class i is stepwise with level $V _ { \iota } ^ { \prime }$ and maximum arrival rate $a _ { i } ^ { m }$ , then the expected net-value loss due to the free-access policv is given by

$$
\Delta N V = b \cdot \lambda_ {M} ^ {* 2} \cdot W ^ {\prime \prime} (\lambda_ {M} ^ {*}) + b \cdot W (\lambda_ {F}) \cdot \sum_ {i = 1} ^ {c} a _ {i} ^ {m} \cdot \left(\frac {1}{k _ {i}} - \frac {1}{k _ {c + 1}}\right) + b \cdot W (\lambda_ {F}) \cdot \left[ \lambda_ {F} - \sum_ {i = 1} ^ {N} \frac {\lambda_ {I F}}{k _ {i}} \right].
$$

The proof is in the working paper version and is available upon request.

## 4.2. Net-value Loss—General Case

Finally, we evaluate the net-value loss in the general case. Recall that we consider an organization that follows the free-access policy and assess by how much it could increase its net-value through optimal pricing. This assessment by itself is subject to information problems; in particular, the organization is assumed not to know its exact value function. One variable that is observable is the system's capacity utilization under the current free-access policy. To evaluate the current system, we calculate an upper bound on the expected net-value loss from the free-access policy. This upper bound provides a basis for deciding on whether to implement a pricing policy and for evaluating the existing free-access system.

Theorem 3 provides the maximum expected net-value loss as a function of the free-access capacity utilization, parameterized by the indices of self-interest, the maximum being taken over all possible downward-sloping system-wide and senders' marginal value functions for each message type. Thus, Theorem 3 is quite powerful, as it provides bounds that can be used without knowledge of the exact value functions.

THEOREM 3. For any general set of value functions, (i) the maximum expected net-value loss occurs when $V _ { \iota } ^ { \prime } ( \lambda _ { \iota } )$ are flat at $b \cdot ( W ( \lambda _ { F } ) / k _ { t } )$ for all i and $\lambda _ { \iota }$ , and (ii) the maximum expected net-value loss is given by

$$
\Delta N V _ {\max} = b \cdot \lambda_ {M} ^ {* 2} \cdot W ^ {\prime} (\lambda_ {M} ^ {*}) + b \cdot W (\lambda_ {F}) \cdot \left[ \lambda_ {F} - \sum_ {i = 1} ^ {N} \frac {\lambda_ {i F}}{k _ {i}} \right],\tag{11}
$$

where ${ \lambda } _ { M } ^ { * }$ is defined implicitly by

$$
L ^ {\prime} \left(\lambda_ {M} ^ {*}\right) = \max _ {i} \left\{\frac {W \left(\lambda_ {F}\right)}{k _ {i}}, L ^ {\prime} (0) \right\}.
$$

PRooF. First consider the case where all the marginal value curves are flat at their respective free-access levels, i.e.,

$$
V _ {i} ^ {\prime} \left(\lambda_ {i}\right) = V _ {i} ^ {\prime} \left(\lambda_ {i, F}\right) = b \cdot \frac {W \left(\lambda_ {F}\right)}{k _ {i}} \quad \text { for   all } i \text { and } \lambda_ {i}.
$$

Let ${ \lambda } _ { \mathrm { f l a t } } ^ { \ast }$ be the corresponding vector of (net-value maximizing) optimal arrival rates Let ${ \boldsymbol { \lambda } } _ { \Omega \mathbf { a } \mathbf { t } } ^ { * }$ be the optimal total arrival rate. Hence, the optimal expected net-value is

$$
\sum_ {i = 1} ^ {N} \lambda_ {i, \text { flat }} ^ {*} \cdot V _ {i} ^ {\prime} (\lambda_ {i, I}) - b \cdot L (\lambda_ {\text { flat }} ^ {*})
$$

and the free-access expected net-value is

$$
N V _ {F} = \sum_ {i = 1} ^ {N} \lambda_ {i, F} \cdot V _ {i} ^ {\prime} (\lambda_ {i, F}) - b \cdot L (\lambda_ {F}).
$$

Thus, in this case, the expected net-value loss, denoted by $\Delta N V _ { \operatorname* { m a x } }$ , is given by

$$
\Delta N V _ {\max} = \sum_ {i = 1} ^ {N} \left[ \lambda_ {i, \text { flat }} ^ {*} - \lambda_ {i, F} \right] \cdot V _ {i} ^ {\prime} (\lambda_ {i, F}) - b \cdot L (\lambda_ {\text { flat }} ^ {*}) + b \cdot L (\lambda_ {F}).
$$

By optimality of ${ \lambda } _ { \mathrm { f l a t } } ^ { \ast } ,$ , we have, for any $\lambda \neq \lambda _ { \mathrm { { f l a t } } } ^ { \ast }$

$$
\sum_ {i = 1} ^ {N} \lambda_ {i, \text { flat }} ^ {*} \cdot V _ {i} ^ {\prime} (\lambda_ {i, F}) - b \cdot L (\lambda_ {\text { flat }} ^ {*}) \geq \sum_ {i = 1} ^ {N} \lambda_ {i} \cdot V _ {i} ^ {\prime} (\lambda_ {i, F}) - b \cdot L (\lambda),
$$

and hence

$$
\begin{array}{l} \Delta N V _ {\max} = \sum_ {t = 1} ^ {N} [ \lambda_ {t, \text { flat }} ^ {*} - \lambda_ {t, F} ] \cdot V _ {t} ^ {\prime} (\lambda_ {t, F}) - b \cdot L (\lambda_ {\text { flat }} ^ {*}) + b \cdot L (\lambda_ {F}) \\ \geq \sum_ {t = 1} ^ {N} [ \lambda_ {t} - \lambda_ {t, F} ] \cdot V _ {t} ^ {\prime} (\lambda_ {t, F}) - b \cdot L (\lambda) + b \cdot L (\lambda_ {F}). \end{array}\tag{12}
$$

Next, consider an arbitrary set of downward-sloping curves. Let $\lambda ^ { * }$ be the corresponding vector of optimal arrival rates. The expected net-value loss, $\Delta N V$ , is given by

$$
\begin{array}{r l} \Delta N V & = \sum_ {i = 1} ^ {N} \left\{V _ {i} (\lambda_ {i} ^ {*}) - V _ {i} (\lambda_ {i, F}) \right\} - b \cdot L (\lambda^ {*}) + b \cdot L (\lambda_ {F}) \\ & = \sum_ {i = 1} ^ {N} \left\{\int_ {0} ^ {\lambda_ {i} ^ {*}} V _ {i} ^ {\prime} (\lambda_ {i}) d \lambda_ {i} - \int_ {0} ^ {\lambda_ {i, F}} V _ {i} ^ {\prime} (\lambda_ {i}) d \lambda_ {i} \right\} - b \cdot L (\lambda^ {*}) + b \cdot L (\lambda_ {F}) \\ & = \sum_ {i = 1} ^ {N} \int_ {\lambda_ {i, F}} ^ {\lambda_ {i} ^ {*}} V _ {i} ^ {\prime} (\lambda_ {i}) d \lambda_ {i} - b \cdot L (\lambda^ {*}) + b \cdot L (\lambda_ {F}). \end{array}
$$

Since $V _ { \iota } ^ { \prime }$ is downward-sloping, we have

$$
\int_ {\lambda_ {l, F}} ^ {\lambda_ {l} ^ {*}} V _ {l} ^ {\prime} (\lambda_ {l}) d \lambda_ {l} \leq \int_ {\lambda_ {l, F}} ^ {\lambda_ {l} ^ {*}} V _ {l} ^ {\prime} (\lambda_ {l, F}) d \lambda_ {l}.
$$

(Note that this inequality holds irrespective of the ordering between $\lambda _ { \iota , F }$ and ${ \lambda } _ { \iota } ^ { * } . )$ Substituting this in the above equality, we have

$$
\Delta N V \leq \sum_ {t = 1} ^ {N} \left[ \lambda_ {t} ^ {*} - \lambda_ {t, F} \right] \cdot V _ {t} ^ {\prime} (\lambda_ {t, F}) - b \cdot L (\lambda^ {*}) + b \cdot L (\lambda_ {F}).\tag{13}
$$

From Equations (12) and (13), we get the desired result: the maxımum expected net-value loss occurs when the marginal value curves for the organization are flat at their respective free-access levels. Equation (11) follows from (7) and (10). Q.E.D.

Consider the case where all message classes $i = 1 , \ldots , N$ have the same index of self-interest k (at their free-access arrival rates). We get from Theorem 3 and Little's Law:

$$
\text { COROLLARY   1. } \quad \Delta N V _ {\max} = b \cdot \lambda_ {M} ^ {* 2} \cdot W ^ {\prime} (\lambda_ {M} ^ {*}) + b \cdot L (\lambda_ {F}) \cdot [ 1 - (1 / k) ].
$$

Again looking at Theorem $^ { 3 , }$ since $\lambda _ { \iota F } / k _ { \iota }$ is nonnegative for all i, we get that $\Delta N V _ { \mathrm { m a x } }$ is bounded by $b \cdot \lambda _ { M } ^ { * 2 } \cdot W ^ { \prime } ( \lambda _ { M } ^ { * } ) + b \cdot W ( \lambda _ { F } ) \cdot \lambda _ { F }$ . Using Little's Law, we get

$$
\text { COROLLARY   2. } \quad \Delta N V _ {\max} \text {   is   bounded   by   } b \cdot \lambda_ {M} ^ {* 2} \cdot W ^ {\prime} (\lambda_ {M} ^ {*}) + b \cdot L (\lambda_ {F}).
$$

Corollary 1 pertains to the case where classes have homogeneous indices of self-interest, whereas Corollary 2 allows for heterogeneous indices across the message classes. In addition to the free-access capacity utilizations, the only parameter needed to compute the bound in Corollary 2 is $k _ { \operatorname* { m i n } } = \operatorname* { m i n } _ { \iota } k _ { \iota }$ . This result is useful because the class with the minimal index of self-interest has the maximum system-wide marginal value, given by $b \cdot W ( \lambda _ { F } ) / k _ { t }$ . One implication is that in computing the bound, the organization only has to consider that class which has the highest marginal value to the organization, not worrying about those classes of messages that create no value to the organization. In other words, the bound in Corollary 2 allows for heterogeneity of the classes and subsumes “junk" messages also. Also, in the same corollary, the second term can be interpreted as the net-value when there is no value at all to the organization due to free-access, but there is a cost, $b \cdot L ( \lambda _ { F } )$

## 5. Examples, Numerical Results and Extensions

In this section we analyze the implications of our general results and discuss further extensions. We evaluate in detail two extremes of network performance. For each, we consider first a specific case of a known (logarithmic) value function and then—the general case of unknown value functions.

The analysis requires further specification of the network performance functions $L ( \lambda )$ and $W ( \lambda )$ . These depend on the multiple-access scheme employed by the network. We first briefly describe this concept and then pursue the analysis.

## 5.1. Network Performance and Multiple-access Schemes

The network delay performance is a function of the multiple-access scheme used. At one extreme is the “ideal deterministic" case. This is a commonly-used simple model for token-ring networks. At the other extreme of performance is the pure ALOHA-type random-access scheme, where each node is free to broadcast whenever it has messages. This simple model is used in performance evaluation of ethernet networks. While our results apply to a system with general performance characteristics, our numerical analyses apply to these two extreme and widely-used cases of delay performance which are commonly used in the literature (cf. Hammond and O'Reilly (1986)) and in practice.

The expression for W(when the capacity of the channel is normalized to unity) for the deterministic scheme is (see, e.g., Hammond and O'Reilly (1986))

$$
W (\lambda) = \frac {1}{2} + \frac {1}{2 (1 - \lambda)},\tag{14}
$$

with $L ( \lambda ) = \lambda \cdot W ( \lambda )$ . Here, the arrival of messages at each node is taken to be Poisson; the messages are assumed to have constant lengths; and the propagation time is negligible. Note that a constant message length has been specified in the assumptions so that the ideal central control behaves as an $M / D / 1$ queue. (In what follows, we contrast the results to the case of random message lengths.) It is easy to verify that these performance functions satisfy our assumptions.

Random-access schemes are characterized by collisions that increase with the number of messages. The analysis of these schemes distinguishes between the throughput of the network, i.e., the fraction of time it is transmitting useful messages, and it total capacity utilization (including failed messages). For the case of pure ALOHA with capacity normalized to unity, the throughput λ is given by (Hammond and O'Reilly 1986)

$$
\lambda = \rho \cdot e ^ {- 2 \rho},\tag{15}
$$

where $\pmb { \rho }$ is the total observed capacity utilization, including retransmissions. It can be easily shown that λ is a quasiconvex function of ${ \bf { \dot { \rho } } } _ { \bf { \dot { \rho } } }$ and it reaches a maximum value of $1 / 2$ e corresponding to $\rho = 0 . 5$ . Furthermore, we cannot have a stable operation when $\rho$ is more than 0.5. Hence, our analysis will consider observed capacity utilizations $\pmb { \rho }$ of up to 0.5 (or equivalently, throughput rates up to $1 / 2 e )$ for the random-access scheme.

Although we are ultimately interested in the throughput λ, the performance functions of the random access scheme are traditionally, and conveniently, expressed in terms of the total capacity utilization $\rho .$ Furthermore. the capacity utilization is the variable that can actually be observed by network administrators. Hence, we will present our results in terms of $\rho ,$ the observed variable. The expected delay function W is given by⁵

$$
W (\rho) = e ^ {2 \rho},\tag{16}
$$

and $L$ is given by Little's Law. It is again easy to verify that these performance functions satisfy our assumptions.

We are now ready to examine the net-value loss under the two schemes. In Subsection 5.2, we study an example with known-value functions. When these functions are unknown, we can use Theorem 3 and its corollaries to evaluate the maximum expected net-value loss, where the maximum is taken over all possible downward-sloping marginal value functions. The results, presented in Subsection 5.3, provide robust upper bounds on the actual loss that can be anticipated in practice.

## 5.2. Example: Known-value Functions

Consider an organization facing the known-value function $V ( \lambda ) = A \cdot \ln ( 1 + \lambda )$ where A is a constant. The value function is thus homogeneous with marginal value $A / ( 1 + \lambda )$ . Since the value function is known, the optimal expected capacity utilization, and hence the expected net-value loss due to the free-access policy, can be computed exactly. Throughout, we evaluate the expected net-value loss as a fraction of $^ { b , }$ the organizational opportunity cost of time for a single message. Thus, a netvalue loss of unity means that the implementation of the free-access policy results in a loss per unit of time which is equal to the cost of delaying a single message by one unit of time.

Figure 2 depicts the net-value loss as a function of the free-access capacity utilization for the deterministic case, with index of self-interest $k = 0 . 7$ . When the free-access capacity utilization $\lambda _ { F }$ is very low, the optimal capacity utilization is above the free-access one, typically resulting in a small but positive loss; and when it is high, the optimal capacity utilization is lower than the free-access one, again resulting in a loss. The greater the divergence between the free-access and the optimal capacity utilizations, the greater the net-value loss. Since practical values of capacity utilization range between single-digit percentages and perhaps 40%–50%, we find that the netvalue loss is substantially below one for most of the relevant range. In other words, the net-value loss per unit time is rather negligible. It becomes significant, creating a rationale for pricing, at high levels of capacity utilization (above 80%). Figure 3 depicts the corresponding results for the random-access scheme; the behavior is similar.

![](/api/attachments/D8MZKWCJ/fulltext/images/6a70e08e0ddcb43daa92a9f9f9d641412c4b2f4f33fed5fd164e0219c432fe4a.jpg)  
FiGURE 2. Net-value loss for the logarithmic value function $V ( \lambda ) = A \cdot \ln ( 1 + \lambda )$ as a function of the observed free-access capacity utilization. k = 0.7: access scheme—deterministic

The net-value loss depends not only on the capacity utilization, but also on the index of self-interest k. Figure 4 shows the net-value loss as a function of k under the deterministic scheme for three alternative levels of the free-access capacity utilization $\lambda _ { F } \colon 0 . 2 , 0 . 5 ,$ and 0.7. The net-value loss is a quasi-convex function of k with a minimum value of zero (this is, in fact, a general property of the solution). The point where the net-value loss is zero corresponds to the case where the free-access capacity utilization exactly matches the optimal one. When the index of self-interest is very low, the optimal capacity utilization is more than the free-access one and users have to be paid to generate messages; and when k is high, the optimal capacity utilization is less than the free-access one and users have to be charged for optimality. The greater the divergence between the optimal and the free-access capacity utilizations, the greater the net-value loss. The same pattern is obtained for the random-access case in Figure 5.

The patterns derived for the polar models of token-ring and ethernet are representative of general patterns of behavior although the actual numbers will often depend on specific implementations. For example, organizations sometimes use networks of different kinds connected to a backbone. A performance analysis can be performed for any specific network structure under consideration, resulting in the performance functions $W ( \lambda )$ and $L ( \lambda )$ . These functions summarize the relevant aspects of network performance, and once derived they can be substituted for the general functions in §4 as done here.

![](/api/attachments/D8MZKWCJ/fulltext/images/d94ba1c215265cda8625f05bd910163e7843eea9113700c8cbe7148f1a22e79a.jpg)  
FiGURE 3. Net-value loss for the logarithmic value function $V ^ { \prime } ( \lambda ) = . 4 \cdot \ln ( 1 + \lambda )$ as a function of the observed free-access capacity utilization. $k = 0 . 7 ;$ access scheme—random-access, Note that under the random-access scheme, the relevant domain for the observed capacity utilization is [0, 0.5)

## 5.3. General Case: Unknown-value Functions

In general, the value functions are not known. The results of §4 can then be used to derive the maximum net-value loss for both access schemes. For each case, we first derive the maximum expected net-value loss assuming that all message types have the same index of self-interest (at the free-access capacity utilization). $k _ { \iota } = k$ . From Corollary 1, the maximum expected net-value loss in this case is given by

$$
\frac {b}{2} \cdot \frac {\lambda_ {M} ^ {* 2}}{(1 - \lambda_ {M} ^ {*}) ^ {2}} + \frac {b}{2} \cdot \lambda_ {F} \cdot \frac {(k - 1)}{k} \cdot \frac {(2 - \lambda_ {F})}{(1 - \lambda_ {F})}
$$

for the deterministic scheme, where

$$
\begin{array}{r l} \lambda_ {M} ^ {*} = & \max \left\{1 - \sqrt {\frac {k \cdot (1 - \lambda_ {F})}{\lambda_ {F} \cdot (k - 1) + (2 - k)}}, 0 \right\} \quad \text { and } \\ & b \cdot \frac {\rho_ {M} ^ {*} \cdot e ^ {2 \cdot (\rho_ {F} - \rho_ {M} ^ {*})} - \rho_ {F}}{k} + b \cdot \rho_ {F} - \rho_ {M} ^ {*} \end{array}
$$

for the random-access scheme, where

$$
\frac {e ^ {2 \rho_ {M} ^ {*}}}{1 - 2 \cdot \rho_ {M} ^ {*}} = \max \left\{\frac {e ^ {2 \rho_ {F}}}{k}, 1 \right\}.
$$

The maximum expected net-value loss is presented in Table 1 for both schemes. As before, we measure the net-value loss in units of the opportunity cost of time, b. Again, since the random access scheme becomes unstable above a capacity utilization of0.5, its maximum net-value loss was computed for free-access capacity utilizations between 0 and 0.4. Most of the entries in Table 1 are less than unity, i.e., the maximum expected net-value loss is only a fraction of the delay cost of a single message; the actual loss is likely to be even smaller. Each row of Table 1 shows the loss as a function of k for a given value of the observed free-access capacity utilization, and the behavior of the bounds is similar to that found for the example in Subsection 5.1: the loss first decreases sharply with k and then starts increasing. Each column shows the dependence on the capacity utilization. The loss is low unless k is very low or the capacity utilization is very high.

![](/api/attachments/D8MZKWCJ/fulltext/images/5e47d82fcca14293f231ffef10bb88f8c5e70ed2d388a235b7636c9f0c20924a.jpg)  
FiGURE 4. Net-value loss for the logarithmic value function as a function of the index of self-interest k; the three curves correspond to three levels of observed free-access capacity utilization: 0.2, 0.5, and 0.7; and the access scheme is deterministic.

![](/api/attachments/D8MZKWCJ/fulltext/images/a42a8e696f36b7a360753d69650f02144bfb3ef1376778d2464bfa41b751ff0a.jpg)  
FiGURE 5 Net-value loss for the logarithmic value function as a function of the index of self-interest k; the observed free-access capacity utilization is 0.2 and the access scheme is random-access.

TABLE 1  
Maxımum Expected Net-value Loss (in Units of b) as a Function of the Observed Capacıty Utilization and k

<table><tr><td colspan="9">Multiple-access Scheme: Deterministic</td></tr><tr><td> $\lambda_F$ </td><td>k</td><td>0.2</td><td>0.25</td><td>0.5</td><td>1</td><td>2</td><td>4</td><td>5</td></tr><tr><td>0</td><td></td><td>2</td><td>1.354248</td><td>0.267949</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0.1</td><td></td><td>1.764349</td><td>1.177104</td><td>0.210500</td><td>0.001463</td><td>0.052777</td><td>0.079166</td><td>0.084444</td></tr><tr><td>0.2</td><td></td><td>1.523437</td><td>0.996572</td><td>0.154171</td><td>0.006966</td><td>0.112500</td><td>0.168750</td><td>0.180000</td></tr><tr><td>0.3</td><td></td><td>1.276193</td><td>0.812288</td><td>0.100324</td><td>0.019057</td><td>0.182142</td><td>0.273214</td><td>0.291428</td></tr><tr><td>0.4</td><td></td><td>1.021448</td><td>0.624206</td><td>0.051667</td><td>0.042338</td><td>0.266666</td><td>0.400000</td><td>0.426666</td></tr><tr><td>0.5</td><td></td><td>0.758342</td><td>0.433375</td><td>0.013932</td><td>0.085786</td><td>0.375000</td><td>0.562500</td><td>0.600000</td></tr><tr><td>0.6</td><td></td><td>0.487980</td><td>0.244448</td><td>0.000510</td><td>0.168861</td><td>0.525000</td><td>0.787500</td><td>0.840000</td></tr><tr><td>0.7</td><td></td><td>0.220606</td><td>0.075214</td><td>0.047792</td><td>0.340924</td><td>0.761543</td><td>1.137500</td><td>1.213333</td></tr><tr><td>0.8</td><td></td><td>0.014835</td><td>0.004168</td><td>0.283375</td><td>0.763932</td><td>1.285786</td><td>1.800000</td><td>1.920000</td></tr><tr><td>0.9</td><td></td><td>0.351530</td><td>0.592561</td><td>1.467424</td><td>2.337722</td><td>3.103679</td><td>3.764624</td><td>3.964554</td></tr><tr><td colspan="9">Multiple-access Scheme: Random-access</td></tr><tr><td> $\rho_F$ </td><td>k</td><td>0.2</td><td>0.25</td><td>0.5</td><td>1</td><td>2</td><td>4</td><td>5</td></tr><tr><td>0</td><td></td><td>0.523847</td><td>0.359756</td><td>0.072383</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0.1</td><td></td><td>0.311938</td><td>0.204738</td><td>0.027521</td><td>0.005262</td><td>0.050000</td><td>0.075000</td><td>0.080000</td></tr><tr><td>0.2</td><td></td><td>0.147083</td><td>0.087932</td><td>0.003237</td><td>0.022199</td><td>0.100000</td><td>0.150000</td><td>0.160000</td></tr><tr><td>0.3</td><td></td><td>0.039097</td><td>0.017168</td><td>0.003435</td><td>0.052805</td><td>0.150000</td><td>0.225000</td><td>0.240000</td></tr><tr><td>0.4</td><td></td><td>0</td><td>0.002032</td><td>0.032880</td><td>0.099491</td><td>0.201466</td><td>0.300000</td><td>0.320000</td></tr></table>

We next relax the condition of homogeneity and let the messages be heterogeneous in terms of their index of self-interest. In this case, we can use Corollary 2 to get an upper bound on the net-value loss in terms of $k _ { \mathrm { m n } }$ . This bound obtains when no value arises at all to the organization under free-access; i.e., under free-access the members generate only $\ " \mathrm { j u n k } \ "$ messages (from the organization's point of view).

By Theorem 3 and its Corollary 2, for a given $k _ { \mathrm { m n } } .$ , as $\lambda _ { F }$ increases, ${ \lambda } _ { M } ^ { * }$ increases and hence the upper bound on $\Delta N V _ { \mathrm { m a x } }$ (as given by Corollary 2) increases. Similarly, for a given $\lambda _ { F }$ , as the $k _ { \mathrm { m n } }$ increases, $\lambda _ { M } ^ { * }$ decreases and hence the bound decreases. Thus, we expect the bounds to be the worst for high values of capacity utilization and low indices of self-interest. We numerically evaluated these bounds and observed the following results: Under the deterministic scheme, when the observed capacity utilization is up to 0.5 and the index of self-interest is unity or greater, the upper bound on the expected net-value loss is a fraction of the opportunity cost of one message; when $k = 0 . 5$ , the bound is less than h when $\lambda _ { F } \le 0 . 3$ ; however when k and $\lambda _ { t }$ are not in this range, the bound increases beyond unity. For the random access case, we found that the bound is less than unity for $k \geq 0 . 5$ and $\rho _ { F } \leq 0 . 4$ . When $\rho _ { F } \gtrsim 0 . 3$ and $k \le 0 . 2 5$ , the bound is greater than unity.

Recall that the deterministic access scheme corresponds to an M/ D/1 system. To examine the robustness of our results, we also studied the M/ M/ 1 system, where the message lengths are drawn from an exponential distribution. We found that the maximum net-value loss was close to that of the $M / D / 1$ scheme given in Table 1, tending to be lower when k is less than 0.5 and tending to be higher when k is more than 0.5. For example, when $k = 0 . 2$ , the maximum net-value loss for $M / M / 1$ is lower as long as $\lambda _ { F } \le 0 . 8$ . Similarly, when $k = 5$ , the maximum net-value loss is higher for $M / M / 1$ . For example, when $\lambda _ { F } = 0 . 5$ , the maximum expected net-value loss is 0.6 for $M / D / 1$ and 0.8 for $M / M / 1$

The foregoing analyses suggest that organizations should consider abandoning the free-access policy either when the network utilization is high (say 60% or 70% in the deterministic case or above 30% in the random-access case) or when the index of self-interest is low (about 0.25 or less). For example, suppose a message retains its value to the organization even if it is communicated with a delay of a month, but the organizational incentives are such that if it is communicated with a delay of more than a week, the sender stands to gain nothing. Then, the free-access policy may lead to a significant loss.

Summarizing, we have shown when the free-access policy is attractive and when it may have to be reevaluated (and possibly abandoned). The power of these results is due to their independence of the particular value functions. As we demonstrate below, similar results apply under more general assumptions.

## 5.4. Extensions

We next show that our results directly extend to the following more general cases:

(i) the organizational opportunity cost of time varies across message types; and

(ii) the service-time distributions are different across message types, and the arrival pattern is Poisson,

Both extensions (i) and (ii) apply the class-dominance approach of B&S (1979). First consider (i). Denote by $b _ { \iota }$ the organizational opportunity cost of a type-i message, $L _ { \imath }$ the expected number of type-i messages in the system, $\alpha _ { \iota } = b _ { s , \iota } / b _ { \iota }$ , and as before, $k _ { \iota } ( \lambda _ { \iota } ) = S _ { \iota } ^ { \prime } ( \lambda _ { \iota } ) / \alpha _ { i } V _ { \iota } ^ { \prime } ( \lambda _ { \iota } )$ . Since message lengths are drawn from a common distribution, L and W are still functions of the total arrival rate λ (rather than the specific composition of the arrival-rate vector $\lambda )$ . From Little's Law, we have $L _ { \imath }$ $= \lambda _ { \iota } \cdot W = \lambda _ { \iota } / \lambda \cdot L$ . Hence, $L _ { \iota }$ is a function of both $\lambda _ { \iota }$ and λ. Now, the organization's net-value maximizing problem is

$$
\max _ {\lambda_ {1}, \lambda_ {2}, \dots , \lambda_ {N}} \sum_ {t = 1} ^ {N} \left\{V _ {t} (\lambda_ {t}) - b _ {t} \cdot L _ {t} (\lambda) \right\}.
$$

The first-order condition for type-i messages is

$$
V _ {i} ^ {\prime} (\lambda_ {i} ^ {*}) = \sum_ {j = 1} ^ {N} b _ {j} \cdot \frac {\partial L _ {j}}{\partial \lambda_ {i}} (\lambda_ {i} ^ {*}, \lambda^ {*}).
$$

It can be shown, in an exactly analogous manner to Theorem 1, that the optimal price for type-i messages, $p _ { i } ^ { * }$ , is given by

$$
p _ {t} ^ {*} = (1 - \alpha_ {t}) \cdot b _ {t} \cdot W (\lambda^ {*}) + \sum_ {j = 1} ^ {N} b _ {j} \cdot \lambda_ {j} ^ {*} \cdot W ^ {\prime} (\lambda^ {*}) - [ V _ {t} ^ {\prime} (\lambda_ {t} ^ {*}) - S _ {t} ^ {\prime} (\lambda_ {t} ^ {*}) ].
$$

Under the free-access policy, the message rates will be given by $S _ { \iota } ^ { \prime } ( \lambda _ { \iota , F } )$ $= b _ { s , \iota } \cdot W ( \lambda _ { F } )$ . In exactly an analogous manner to Equation (5), we can show that $V _ { \iota } ^ { \prime } ( \lambda _ { \iota , F } ) = b _ { \iota } \cdot W ( \lambda _ { F } ) / k _ { \iota }$

To derive the expected net-value loss, first consider the case of flat marginal value curves, as in B&S (1979). B&S (1979) derive their class-dominance results under Poisson arrivals and heterogeneous service time distributions. We first show in

Lemma 1 that a similar result holds under the general arrival pattern and homogeneous service time distribution studied here.

LEmmA 1. Assume that each class i has a flat marginal value curve at $V _ { \iota } ^ { \prime }$ . Then, for a general arrival pattern, there will be a single class admitted at optimality.

PRooF. Without loss of generality, consider two classes. Let λ be a given total arrival rate, and let $\lambda _ { 1 }$ and $( \lambda \ : - \ : \lambda _ { ! } )$ be the arrival rates for the two classes. The net-value to the organization, NV, is given by

$$
\begin{array}{r l} N V & = \lambda_ {1} \cdot V _ {1} ^ {\prime} + (\lambda - \lambda_ {1}) \cdot V _ {2} ^ {\prime} - b _ {1} \cdot L _ {1} (\lambda_ {1}, \lambda) - b _ {2} \cdot L _ {2} (\lambda - \lambda_ {1}, \lambda) \\ & = \lambda_ {1} \cdot V _ {1} ^ {\prime} + (\lambda - \lambda_ {1}) \cdot V _ {2} ^ {\prime} - b _ {1} \cdot \lambda_ {1} \cdot W (\lambda) - b _ {2} \cdot (\lambda - \lambda_ {1}) \cdot W (\lambda). \end{array}
$$

Hence, we get

$$
\partial N V / \partial \lambda_ {1} = V _ {1} ^ {\prime} - V _ {2} ^ {\prime} - b _ {1} \cdot W (\lambda) + b _ {2} \cdot W ^ {\prime} (\lambda).
$$

The RHS is a constant for a given λ. Hence, depending on whether the RHS is positive or negative, $\lambda _ { t }$ would be set at λ or 0 for optimality.6 In particular, this result holds when λ is the optimal arrival rate, λ\*. Q.E.D.

We can now show that an adaptation of Equation (l1) will indeed give the expected net-value loss. To see this, invoke Lemma 1 and let $i ^ { * }$ be the optimal class. Now, defining ${ \lambda } _ { M } ^ { * }$ implicitly by $V _ { \iota ^ { * } } ^ { \prime } = b _ { \iota ^ { * } } \cdot L ^ { \prime } ( \lambda _ { M } ^ { * } )$ , we can show, in exactly an analogous manner to (10), that $N V ^ { * } = b _ { \iota } \bullet \cdot \lambda _ { M } ^ { * 2 } \cdot W ^ { \prime } ( \lambda _ { M } ^ { * } )$ . Straightforward manipulation gives the expected free-access net-value as

$$
N V _ {F} = W \left(\lambda_ {F}\right) \cdot \sum_ {i = 1} ^ {N} b _ {i} \cdot \lambda_ {i, F} \cdot \left[ \frac {1}{k _ {i}} - 1 \right].
$$

From the expected optimal and free-access net-values, the expected net-value loss is

$$
\Delta N V = b _ {i *} \cdot \lambda_ {M} ^ {* 2} \cdot W ^ {\prime} (\lambda_ {M} ^ {*}) + W (\lambda_ {F}) \cdot \sum_ {i = 1} ^ {N} b _ {i} \cdot \lambda_ {i, F} \cdot \left[ 1 - \frac {1}{k _ {i}} \right].\tag{17}
$$

Thus, the expected net-value loss is given by an adaptation of Equation (1 1) obtained by using type $i ^ { * }$ (instead of type 1) for optimality and by using the respective delay costs for the various classes (instead of b).

We have thus far considered the case of flat marginal value curves. Next consider the case of general nonincreasing marginal value curves. We show that the expected net-value loss is maximized when the marginal value curves are flat at their freeaccess levels. Thus, (17) also gives the maximum expected net-value loss in the general case.

THEoREM 4. For general value functions and heterogeneous orgunizational opportunity costs across message types, (i) the maximum expected net-value loss occurs when $V _ { \iota } ^ { \prime \prime } ( \lambda _ { \iota } )$ are flat at $b _ { \iota } \cdot W ( \lambda _ { F } ) / k _ { \iota }$ for all i and $\lambda _ { \iota }$ , and (ii) the maximum expected net-value loss is given by (17)

The proof is similar to that of Theorem 3, with $\textstyle \sum _ { i = 1 } ^ { N } b _ { i } \cdot L _ { i }$ replacing $b \cdot L$ A useful way to compare (11) and (17) is to rewrite them respectively as

$$
b \cdot \lambda_ {M} ^ {* 2} \cdot W ^ {\prime \prime} (\lambda_ {M} ^ {*}) + b \cdot \sum_ {i = 1} ^ {N} L _ {i, F} \cdot \left[ 1 - \frac {1}{k _ {i}} \right] \quad \text { and }
$$

$$
b _ {i *} \cdot \lambda_ {M} ^ {* 2} \cdot W ^ {\prime} (\lambda_ {M} ^ {*}) + b _ {i *} \cdot \sum_ {i = 1} ^ {N} L _ {i, F} \cdot \left[ 1 - \frac {1}{k _ {i}} \right] \cdot \frac {b _ {i}}{b _ {i *}},
$$

where $\scriptstyle L _ { \imath , F }$ - represents the expected number of messages of type-i under free-access. Thus, if we replace, for all $i , [ 1 - 1 / k , ] \mathrm { b y } \{ 1 - 1 / k , \} \cdot b _ { t } / b _ { t }$ •(or equivalently, replace $k _ { t }$ by $1 / ( 1 - [ 1 - 1 / k _ { \iota } ] \cdot b _ { \iota } / b _ { \iota ^ { * } } ) )$ and b by $b _ { \iota ^ { * } }$ , we can use (11) to represent the expected net-value loss, which can then be conveniently expressed in units of $b _ { t } ,$

The analogs of Corollaries 1 and 2 also follow. Specifically, similar to Corollary l for a common k for all classes, we have

$$
\Delta N V _ {\max} = b _ {t ^ {*}} \cdot \lambda_ {M} ^ {* 2} \cdot W ^ {\prime \prime} (\lambda_ {M} ^ {*}) + b _ {t ^ {*}} \cdot L (\lambda_ {F}) \cdot \left[ 1 - \frac {1}{k} \right] \cdot \sum_ {i = 1} ^ {N} \frac {\lambda_ {i}}{\lambda} \cdot \frac {b _ {i}}{b _ {t ^ {*}}}.
$$

Similar to Corollary 2, we have the result that $\Delta N V _ { \mathrm { m a x } }$ is bounded by

$$
b _ {t ^ {*}} \cdot \lambda_ {M} ^ {* 2} \cdot W ^ {\prime} (\lambda_ {M} ^ {*}) + \sum_ {i = 1} ^ {N} b _ {i} \cdot L _ {i} (\lambda_ {i, F}, \lambda_ {F}).
$$

Thus, our results extend to the case of heterogeneous organizational opportunity costs in a straightforward manner.

It is now easy to see that our result can be extended to the case of heterogeneous service-time distributions, but with Poisson arrivals. The analysis will be exactly similar to the foregoing one, with the class dominance result in B&S (1979) replacing Lemma 1.

An interesting future extension would be to the case of a general arrival pattern, heterogeneous delay costs, and heterogeneous service-time distributions.

## 6. Concluding Remarks

In this paper, we evaluate the free-access policy as a control mechanism for internal communications networks. To do this, we first derive the pricing policy that it theoretically optimal (i.e., the pricing policy that will maximize the network's expected net-value to the organization). We discuss the practical problems associated with the actual implementation of such a pricing policy.

We next use the optimal control structure derived above as the baseline case to evaluate the free-access policy. Specifically, we ask the question, “How deviant is the free-access policy from the optimal policy (in terms of expected net-value to the organization $) ? ^ { , , }$ We derive the loss in net-value that the organization can expect in opting for a free-access policy relative to an optimal control structure. We derive general upper bounds on this loss for the case where the value functions are not known.

The expression for the maximum expected net-value loss is a function of the performance characteristics of the network (e.g., delay in the delivery of messages, number of messages in the system at any given time, etc.). These performance characteristics are in turn determined by the multiple-access scheme that is employed by the network. From the wide spectrum of possible implementations, we chose two schemes that represent extremes of network performance: the “Pure ALOHA" and “Ideal Centralized Control," that also represent simple models of the two widely-used network types of ethernet and token ring. We show the conditions under which the maximum net-value loss that the organization can expect from a free-access policy is a fraction of the opportunity cost of one message.

In these situations, considering that

(a) getting the data needed to determine the optimal pricing policy is difficult;

(b) there are costs involved in setting up and operating a pricing policy;

(c) there are no such costs in a free-access policy;

(d) our results provide the maximum net-value loss that the organization can expect under a free-access policy (whereas the actual net-value loss could be lower): and

(e) the results are independent of the particular value functions,

a free-access policy is an attractive control structure for internal networks. We also identify conditions under which the maximum expected net-value loss is relatively high and hence pricing should be considered.

In our analysis, we initially consider different opportunity costs of time for the senders of different types of messages and a constant organizational opportunity cost of time. Here, we do not place any restrictions on the arrival patterns. We then extend the results to the case where the organizational opportunity costs of time are different for different message types. We show that our results can be adapted in a straightforward manner to the case of heterogeneous organizational opportunity costs of time, as well as to the case of heterogeneous organizational opportunity costs of time and heterogeneous service-time distributions, if the arrivals have a Poisson distribution.

Other possible extensions could be to the case of general arrival patterns with heterogeneous service-time distributions, and to the case of nonlinear delay costs. One can also look at the peak-load problem and investigate when an organization could benefit from a pricing policy for the peak period and a free-access policy for the nonpeak period. Finally, one can also compare other control structures, such as the profit-center control structure with the optimal pricing and free-access control structures.\*

Acknowledgements. Partial financial support by the Xerox Research Chair at the Graduate School of Industrial Administration and the Information Networking Institute at Carnegie Mellon University, and by the Computer Industry Project of the Sloan Foundation at Stanford University is gratefully acknowledged. The authors acknowledge helpful comments and suggestions by anonymous reviewers.

\* Rajiv Banker, Associate Editor. This paper was received on October 30, 1991, and has been with the authors 11 months for l revision.

## References

Adirı, I. and U. Yechiali, "Optimal Priority-purchasing and Price Decısions in Non-monopoly and Monopoly Queues," Operations Research, 22, 3 (1974), 1051–1066

Alperstein, H., “Optimal Pricing Policy for the Service Facılities Offerıng a Set of Priority Prices," Management Science, 34, 5 (May 1988), 666–671.

Artle, R. and C. Averous, “The Telephone System as a Public Good: Static and Dynamic Aspects," Bell Journal of Economıcs and Management Science, 4, 1 (Spring 1973), 89–100

Balachandran, K. R., “Purchasing Priorities in Queues." Management Scrence, 18, 5. Part I (Jan. 1972), 316-326.

and M. E. Schaefer, “Class Dominance Characterıstics of a Service Facılity," Econometrica, 47, 2 (March 1979), 515–519.

Information on Congestion," European Journal of Operattonal Research, 4, 3 (March 1980), 195–202.

---
otero_id: 414
otero_key: "36RV3NBC"
title: "Optimal mediated auctions with endogenous participation"
authors: "Ying-Ju Chen"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Optimal mediated auctions with endogenous participation

Ying-Ju Chen ⁎

University of California, 4121 Etcheverry Hall, Berkeley, CA 94720, United State

a r t i c l e i n f o

Article history: Received 29 December 2011 Received in revised form 20 October 2012 Accepted 4 December 2012 Available online 13 December 2012

Keywords: Internet auctions Electronic marketplace Endogenous participation Mechanism design

## a b s t r a c t

The majority of academic papers on the Internet auction design do not distinguish between the auctioneer and the object owner, whereas nowadays leading Internet auction websites operate primarily as mediators that provide the platforms with no physical possessions of the auction objects. The role separation between the auctioneer and the object owner (seller) creates both incentive misalignment and information asymmetry issues. In this paper, we acknowledge this role separation and study the optimal (revenue-maximizing) auction mechanism from the mediator's perspective, taking into account the costly participation from both the sellers and the buyers.

We show that the mechanism induces participation from low-valuation sellers and high-valuation buyers. Compared with the conventional seller-optimal auction, the seller in the mediator-optimal mechanism keeps the object more frequently ex post because the mediator intentionally compensates the seller for withholding the object. This exacerbated ex post allocative inef<sup>fi</sup>ciency also gives rise to too little ex ante participation for both the seller and the buyers. We propose a simple two-stage mechanism for implementation that is reminiscent of some widely observed Internet auctions. Our qualitative results are robust against model variations such as heterogeneous participation costs, multiple units, and multiple sellers

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Due to the explosive growth that online auctions have exhibited during the last decade, nowadays millions of people purchase commodities from Internet auction sites, such as eBay, Yahoo!, and Amazon. Formally speaking, an auction is a trading mechanism that involves two sides: the seller who owns the object, and the buyers who intend to purchase the object. Traditionally, the seller is the auctioneer who designs the auction rules regarding how the object is awarded among the interested buyers, and what payments are made based on the revealed information. The vast auction literature has provided a clear answer to this auction design problem. Stemming from Myerson [27], it has now been a <sup>fi</sup>xture that the “seller-optimal” auction mechanism can be implemented by any standard auction (<sup>fi</sup>rst-price, second-price, Dutch, or English) with an appropriate reserve price. Nevertheless, in the Internet era, the auction mechanism is designed by a third-party auction website such as eBay, Yahoo!, and Amazon which do not necessarily own the objects. These giant commercial institutions serve as independent mediators that induce both sides of traders (sellers and buyers) to the exchange environments. Consequently, the current practice of Internet auctions creates a novel role separation between the object owner (seller hereafter) and the auctioneer (mediator hereafter) who designs the mechanism, i.e., the auction rules.

The role separation raises some new challenges for the Internet auction design that are less pronounced in the traditional auctions. First, in line with the assumption that the seller does not observe the buyers' private valuations, here the mediator may have no access to the seller's own valuation of retaining the object as well. This asymmetric information problem is the central premise of the auction literature, as auctions are designed speci<sup>fi</sup>cally to elicit the feedbacks/ inputs from the buyers when the seller does not know what is the right price to sell; see [14,21,27]. Viewed in this way, it seems natural that the mediator, as the auctioneer, may also face information asymmetry vis-a-vis the seller. Consequently, the mediator faces two distinct sources of information asymmetry, and the auction mechanism has to be designed as an optimal response to these informational disadvantages.

Second, the mediator now needs to induce the appropriate traders from both sides to participate in order to facilitate pro<sup>fi</sup>table transactions. Despite the effort towards the reduction of transaction costs, participating in the Internet auctions remains costly and timeconsuming. For example, it requires the seller to subscribe in the system, provide relevant information for the identity check, hold the object for a while before the bidding process ends. All the above create additional hassle for the seller, who may otherwise sell the object immediately through other channels or simply withhold the object. From the buyers' side, they may have to learn the auction rules, purchase bid documents, and stay connected during (at least the last stage of) the bidding process. This costly participation issue has been widely documented in various papers and has been recognized as one of the most crucial concerns in the modern auction design, see [5,12,13,19,25,29] for more elaborations.<sup>1</sup> There may also be some intangible costs for either the seller or the buyers, as they have to think ex ante the cost and bene<sup>fi</sup>t of participating in the Internet auction versus selling/purchasing elsewhere immediately [31]. An important task for the mediator is therefore to overcome the disincentives of the sellers and the buyers and engage them in this exchange environment.

The discrepancy between the academic literature and the practical Internet auction design gives rise to the following research questions. What is the optimal (revenue-maximizing) auction mechanism from the mediator's perspective? How do the buyers bid in this mediatoroptimal mechanism, and how do the seller and the buyers determine whether to participate? Is it possible for the mediator to implement the optimal mechanism in a simple way? How does the two-sided information asymmetry affect the ex post allocation and the ex ante participation decisions of the sellers and the buyers?

We attempt to provide a uni<sup>fi</sup>ed, easily extendable framework to address all the above issues. In pursuit of this goal, we construct a stylized model with a monopolistic mediator, a seller, and a number of potential buyers (bidders). Each buyer desires one unit of product and, upon receiving it, obtains a valuation that is privately known. The seller is endowed with a single object and intends to sell to the buyers for pro<sup>fi</sup>t, and she must sell through the mediator. This creates the distinction between the object owner (seller) and the auctioneer (mediator); furthermore, the mediator has no access to the seller's private valuation of keeping the object. We assume that the seller, as well as the buyers, must incur participation costs upon entering the platform operated by the mediator. Confronted with the seller and the buyers' costly participation and two sources of asymmetric information, the mediator's goal is to design a mechanism that maximizes his expected payoff.

Based on the above model characteristics, we show that the participation decisions of both the seller and the buyers exhibit the cutoff structures: while a buyer participates in the mechanism only if her valuation for the object is suf<sup>fi</sup>ciently high, the seller is willing to put up her object for sale when her valuation is low. This result is admittedly intuitive; nonetheless, it provides the theoretical building block for us to characterize the equilibrium behaviors and derive additional insights that we lay out below. In terms of implementation, we propose a simple two-stage mechanism in which the mediator <sup>fi</sup>rst speci<sup>fi</sup>es the upfront listing fee and reserve fee (paid while setting the reserve price) to the seller; afterwards, the mediator completely delegates the auction design to the seller and compensates the seller for withholding the object upon participation. Accordingly, the seller can conduct any standard auction (<sup>fi</sup>rst-price, second-price, English, or Dutch) and will choose an appropriate reserve price. This seems to coincide with the current “proxy selling” practice of the electronic marketplace, as eBay does not charge the winners and allows the seller to decide the auction format.

We can also compare the equilibrium outcomes in the conventional seller-optimal auction and our mediator-optimal mechanism. Our analysis reveals that compared with the seller-optimal auction, the seller keeps the object more frequently ex post in the mediator-optimal mechanism. The ex post inefficiency is exacerbated when the mediator serves as the auctioneer, because now the seller's mis-incentive to withhold the object is ampli<sup>fi</sup>ed due to the two-sided private information. Moreover, the mediator-optimal mechanism induces too little ex ante participation for both the seller and the buyers. The rationale of this ex ante reluctance arises from the ex post inef<sup>fi</sup>cient allocation. Anticipating this, each buyer is less likely to receive the object upon participation; therefore, fewer buyers will be engaged in the bidding ex ante. The buyers' reaction also has an adverse effect on the seller's participation decision: because the seller expects to attract fewer buyers to bid for the object, she is more cautious while determining to put up the object for sale. Collectively, we observe that the mediator's involvement in fact reduces the possibility of successful transactions, and results in a larger degree of inef<sup>fi</sup>ciency both ex ante and ex post.

We further extend our results to incorporate the possibilities of heterogeneous participation costs, multiple units, and multiple sellers. We show that the cutoff structures for the participation decisions are not prone to these modi<sup>fi</sup>cations, and the valuation in<sup>fl</sup>ation from the sellers' side leads to the more pronounced ex post inef<sup>fi</sup>ciency compared to their seller-optimal counterpart. When a seller with a higher valuation incurs a higher participation cost, she is less likely to participate when their participation costs are higher or more heterogeneous. Nevertheless, the buyers' participation is not altered by this modi<sup>fi</sup>cation, and the ex post allocation rule again relies on the virtual surplus comparisons across the buyers and the seller. When the seller is endowed with multiple units, the participation decisions from both sides become more sophisticated; nevertheless, the allocation rule remains simple as it resembles the result from the classical multi-unit auction.

We organize the rest of this paper as follows. Section 2 reviews some relevant literature. In Section 3, we lay out the basic model with a single seller who intends to sell one product. Section 4 derives the optimal mechanism from the mediator's perspective. In Section 5, we investigate some extended scenarios with heterogeneous participation costs, multiple units, and multiple sellers. Section 6 provides some concluding remarks. All the proofs are relegated to the Appendix A.

## 2. Literature review

Our paper belongs to a long-standing literature on auction theory, which has been applied extensively in the context of Internet auctions. For example, Cai et al. [3], Caldentey and Vulcano [4], Liu and Chen [17], and Hidvegi et al. [10] study the regular auctions for physical goods or services, Chen et al. [6], Feng et al. [8], and Liu et al. [18] examine the design of keywords/search auctions, and Ghosh et al. [9], Mahdian et al. [20], and McAfee et al. [23] investigate the display advertising auctions. As aforementioned, the majority of papers on the Internet auctions do not distinguish between the auctioneer and the object owner, whereas we acknowledge the practical situation that it is the mediator rather than the seller that conducts the auction design. Our problem can also be regarded as an extension of Myerson [27] and Maskin and Riley [21] to this electronic marketplace. In an in<sup>fl</sup>uential paper, Myerson and Satterthwaite [28] consider the mechanism design with two sides of economic agents. We extend Myerson and Satterthwaite [28] by incorporating the endogenous participation decisions from both sellers and buyers, and demonstrate the intricate interplay between the ex ante participation and ex post allocation.

There are a few papers that consider the role of mediator in the auction design, including Ashlagi et al. [1] and Matros and Zapechelnyuk [22]. In the context of position auctions, Ashlagi et al. [1] characterize a suf<sup>fi</sup>cient condition under which the equilibrium outcomes of their proposed mediated auction coincide with the Vickrey–Clarke–Groves (VCG) mechanism. Matros and Zapechelnyuk [22] elaborate on the seller's commitment issue and show that when the seller is allowed to re-auction the object repeatedly, it is optimal for the mediator to abandon the listing fee. None of the aforementioned papers considers the participation decisions from both sides, which are the central topic we address in this paper. Additionally, the multi-unit case and the scenario with seller competition have no counterparts in their papers.

The impact of buyers' opportunity or participation costs has also been investigated in a number of papers. Engelbrecht-Wiggans [7], Levin and Smith [16], McAfee and McMillan [24], and Tan [30] consider the scenarios in which the bidders must decide whether to enter the auctions before observing their valuations. This ex ante entry case eliminates the heterogeneity among bidders regarding the participation decisions. Celik and Yilankaya [5], Lu [19], Menezes and Monteiro [25], and Stegeman [29] consider the case when the bidders learn their valuations before making the entry decisions. Our sequence of events follows the latter research stream. We contribute to this research stream by introducing the seller's participation as well as the discrepancy between the auctioneer (the mediator) and the object owner (the seller).

## 3. Model

We consider a stylized model with a monopolistic mediator, a seller, and a number of potential buyers (bidders).

## 3.1. Buyers

Each buyer, indexed by $i { = } 1 , . . . , N ,$ desires one unit of product, and, upon receiving it, obtains valuation $\nu _ { i \cdot }$ The valuation $\nu _ { i }$ is identically and independently drawn from a common distribution function $F _ { B }$ with the corresponding density function $f _ { B } \ 0 \mathrm { n } \ \left[ \underline { { \nu } } , \bar { \nu } \right]$ . The valuation <sup></sup>v is privately observed by buyer i but is unknown to either the mediator, the seller, or any other buyer. Since the valuations {v }'s are i.i.d. draws from a common distribution, the buyers are ex ante symmetric (identical). The seller is endowed with a single object and intends to sell to the buyers for pro<sup>fi</sup>t. All parties considered in this model are risk-neutral, i.e., they are expected payoff maximizers. Initially, we assume that only one seller is present; in Section $5 ,$ we investigate the alternative setting in which multiple sellers may co-exist.

## 3.2. Role separation

We introduce two departures from the classical auction literature. First, the seller must sell through the mediator, which creates the distinction between the object owner (seller) and the auctioneer (mediator). As we separate these two roles, it is conceivable that the mediator may have no access to the seller's private valuation of keeping the object. Thus, unlike the classical integrated auction (where the object owner and the auctioneer are the same person), the mediator now faces two sources of private information from both the seller and the buyers. For ease of exposition, we use player 0 to denote the seller, and player i to represent buyer i whenever convenient. We use $\nu _ { 0 }$ to denote the seller's valuation that is unobservable by either the mediator or the buyers (where the subscript 0 indicates the seller's index). From the mediator's perspective, $\boldsymbol { v } _ { 0 }$ follows a distribution $F _ { S }$ with $f _ { S }$ being its density and $\left[ \underline { { \boldsymbol { v } } } _ { 0 } , \bar { \boldsymbol { v } } _ { 0 } \right]$ being its support. We call $\boldsymbol { v _ { 0 } }$ and {v }'s the “types” of the <sup></sup>seller and the buyers as they are only privately observable. To facilitate our analysis, we impose the following regularity conditions.

Assumption 1. 1) $F _ { B } ( \nu )$ has an increasing failure rate $( \mathrm { I F R } ) , \mathrm { i } . \mathbf { e } . , H ( \nu ) \equiv$ $\frac { 1 - F _ { B } ( \nu ) } { f _ { B } ( \nu ) }$ is decreasing in $\boldsymbol { v } ;$ and 2) $h ( \nu _ { 0 } ) \equiv _ { f _ { S } ( \nu _ { 0 } ) } ^ { F _ { S } ( \nu _ { 0 } ) }$ is increasing in $\nu _ { 0 } .$

These monotonicity conditions are adopted to exclude the possibility of bunching $( \mathrm { i . e . } ,$ multiple types of sellers and/or buyers take the same indistinguishable actions in equilibrium), see [15]. The <sup>fi</sup>rst assumption is also known as the monotone hazard rate (MHR) property. The second assumption follows the same line, and is also commonly adopted in the agency literature in which the sellers/suppliers are endowed with private information. The bounds $\underline { { \nu } } _ { 0 } , \bar { \nu } _ { 0 } , \underline { { \nu } } ,$ andv are necessarily positive, and $\bar { \boldsymbol { v } } _ { 0 }$ <sup> </sup>and v can be either <sup>fi</sup>nite or in<sup>fi</sup>nite.

As the second departure from the classical auction literature, we assume that the seller as well as the buyers must incur participation costs upon entering the platform operated by the mediator. We use $c _ { B } 2 0$ to denote the (common) participation cost of the buyers, and $c _ { S } { \geq } 0$ to denote the seller's if she intends to sell her object through the mediator.

## 3.3. Mediator's objective

Confronted with the seller's and the buyers' costly participation and two sources of asymmetric information, the mediator's goal is to design a mechanism that maximizes his expected payoff. We invoke the revelation principle to con<sup>fi</sup>ne our search within the family of direct revelation mechanisms. In these direct revelation mechanisms, the mediator simply requests the seller and the buyers to report their private information and selects the allocations and payments accordingly. We normalize the reservation utility for the buyers to zero regardless of their willingness to pay. In Section 4, we comment on how the optimal mechanism may be implemented by some existing practical auction schemes.

## 3.4. Mechanism

In the presence of costly participation, the mechanism should specify the probabilities of participating in the auction, the allocation of the object, and the corresponding payments. For ease of notation let $\mathbf { v } \equiv ( \nu _ { 0 } , . . . , \nu _ { N } ) \equiv ( \nu _ { i } , . . . , \mathbf { v } _ { - i } )$ represent the type vector, where $\mathbf { v } _ { - i } { \equiv }$ $( \nu _ { 0 } , . . . , \nu _ { i - 1 , } \nu _ { i + 1 } , . . . , \nu _ { N } )$ is the type pro<sup>fi</sup>le of other players excluding player i. We use $\rho _ { 0 } ( \nu )$ and $\{ \rho _ { i } ( \nu ) \} ^ { \prime } s$ to represent the participation probabilities of the seller and the buyers, respectively. Upon the seller's participation, let $Q _ { 0 } ( { \mathsf { v } } )$ denote the probability that the seller keeps the object, and $\{ Q _ { i } ( \pmb { v } ) \} ^ { \prime } s$ denote the probabilities that the object is awarded to one of the buyers. Accordingly, $P _ { 0 } ( { \bf { v } } )$ and $\{ P _ { i } ( \pmb { v } ) \}$ 's refer to the (expected) payments the mediator collects from the seller and the buyers. In the presence of costly participation, $\{ P _ { i } ( \pmb { v } ) \} _ { s } ^ { \prime }$ and $\{ Q _ { i } ( \pmb { v } ) \} ^ { \prime } s$ are not suf<sup>fi</sup>cient for describing the mechanism. The seller may eventually retain the object $( Q _ { 0 } ( \mathbf { v } ) = 1 )$ but have incurred the participation cost. Likewise, each buyer may pay $c _ { B }$ upon participation but end up without getting the object. The separation of participation and allocation stages allows us to account for this subtle difference.

These probabilistic terms and allocations are adopted in compliance with the auction theory; as we will see in the sequel, at optimality they turn out to be deterministic. Notably, the participation decisions are at the discretion of the buyers (and the seller). However, they can be regarded as part of the mechanism design, because they in<sup>fl</sup>uence the ultimate allocation of the object. This is similar to how the bids and allocations are induced in the standard auction literature. The auctioneer sets up the mechanism, and the bidders (in our context the buyers and the seller) are induced to choose whether to participate, how much to pay, and whether to obtain the object (ex post).

## 3.5. Timing

The sequence of events proceeds as follows. 1) At the beginning of the game, the mediator announces the mechanism $\{ \rho _ { i } ( { \bf v } ) , Q _ { i } ( { \bf v } ) , P _ { i } ( { \bf v } ) \}$ 2) The seller and the buyers privately observe their own types {v }'s and determine their reporting strategies, where the reports $\{ \hat { \boldsymbol { v } } _ { i } \} ^ { \prime } \boldsymbol { s }$ need not coincide with their true types. 3) Based on the reports $\{ \hat { \nu } _ { i } \} ^ { \prime } s ,$ the seller and the buyers pay to the mediator $\{ P _ { i } ( \hat { \nu } _ { i } ) \} ^ { \prime } s ,$ , partic-<sup>f g</sup>ipate in the auction according to $\{ \rho _ { i } ( \hat { \mathbf { v } } ) \} ^ { \prime } \mathbf { s } ,$ , where $\hat { \mathbf { v } } \equiv ( \hat { \nu } _ { 0 } , . . . , \hat { \nu } _ { N } )$ ; if the <sup>f g</sup>seller participates, the object is awarded to buyer i with probability $Q _ { i } ( { \hat { \mathbf { v } } } ) ,$ , and is withheld by the seller with probability $Q _ { 0 } ( \hat { \mathbf { v } } )$ . For ease <sup>ð Þ ð Þ</sup>of illustration, we summarize the notation in Table 1. In the next section, we characterize the optimal mechanism from the mediator's perspective.

## 4. Mediator-optimal mechanism

In this section, we characterize the mechanism that maximizes the mediator's expected payoff. To this end, we shall start with the seller's and the buyers' reporting strategies. In the direct revelation mechanism, it is without loss of generality to focus on the equilibrium in which the seller and each buyer report truthfully. However, we need to ensure that no pro<sup>fi</sup>table deviation may arise.

## 4.1. Payoffs

Suppose that the seller's true type is $\boldsymbol { v } _ { 0 }$ but she reports it as ${ \hat { v } } _ { 0 } . A s \cdot$ suming that all the buyers report truthfully, the seller's expected payoff based on this reporting strategy is

$$
U _ {0} (v _ {0}; \hat {v} _ {0}) \equiv \mathbb {E} _ {\mathbf {v} - 0} \{\rho_ {0} (\hat {v} _ {0}, \mathbf {v} _ {- 0}) [ v _ {0} Q _ {0} (\hat {v} _ {0}, \mathbf {v} _ {- 0}) - P _ {0} (\hat {v} _ {0}, \mathbf {v} _ {- 0}) - c _ {S} ] + [ 1 - \rho_ {0} (\hat {v} _ {0}, \mathbf {v} _ {- 0}) ] v _ {0} \},\tag{1}
$$

where the misreport $\hat { \boldsymbol { v } } _ { 0 }$ affects the probability of participation $\rho _ { 0 } ( \hat { \nu } _ { 0 } , { \bf v } _ { - 0 } ) ,$ , the allocation $Q _ { 0 } ( \hat { \nu } _ { 0 } , { \bf v } _ { - 0 } )$ , and the payment $P _ { 0 } ( \hat { \nu } _ { 0 } , { \bf v } _ { - 0 } )$ The expectation is taken over all possible type realizations of the buyers $( { \bf { v } } _ { - 0 } )$ . From Eq. (1), if the seller opts not to participate (with probability $1 - \rho _ { 0 } ( \hat { \nu } _ { 0 } , { \bf v } _ { - 0 } ) )$ , he retains the object and obtains the payoff v .

Likewise, if a type-v<sub>i</sub> buyer i unilaterally reports to be type- $- { \hat { V } } _ { i } ,$ her expected payoff is

$$
U _ {0} (v _ {0}; \hat {v} _ {0}) \equiv \mathbb {E} _ {\mathbf {v} _ {- i}} \{\rho_ {i} (\hat {v} _ {i}, \mathbf {v} _ {- i}) [ \hat {v} _ {i} Q i (\hat {v} _ {i}, \mathbf {v} _ {- i}) - P _ {i} (\hat {v} _ {i}, \mathbf {v} _ {- i}) - c _ {B} ] \}.
$$

Thus, as long as a buyer participates in the mechanism $( \rho _ { i } ( \hat { \nu } _ { i } ,$ $\mathbf { v } _ { - i } ) { \neq } 0 )$ , she must pay the participation cost $c _ { B } .$ <sup>ð</sup>On the other hand, <sup>Þ</sup>when $\rho _ { i } ( \hat { \nu } _ { i } , { \bf v } _ { - i } ) = 0 ,$ the buyer never obtains any utility from the object $( U _ { i } ( \nu _ { i } ; \hat { \nu } _ { i } ) = 0 )$ . Therefore, if a buyer chooses not to participate (by <sup>ð Þ ¼</sup>reporting a valuation $\hat { \nu } _ { i }$ that leads to $\rho _ { i } ( \hat { \nu } _ { i } , { \bf v } _ { - i } ) = 0 )$ , her “bid” will be discarded by the auctioneer.

## 4.2. Incentive constraints

In equilibrium, truth-telling must be induced, i.e., each player is weakly better off reporting her true type, thereby leading to the following incentive compatibility (IC) constraints:

$$
U _ {i} (v _ {i}; v _ {i}) \geq U _ {i} (v _ {i}; \hat {v} _ {i}), \forall v _ {i}, \hat {v} _ {i}, \forall i.\tag{IC}
$$

Moreover, the mechanism must guarantee that upon reporting their types, each player receives at least her reservation utility. For the seller, this implies that the following individual rationality (IR) constraint must hold:

Table 1 Summary of notation.

<table><tr><td>Notation</td><td>Descriptions</td></tr><tr><td> $N$ </td><td>Number of buyers</td></tr><tr><td> $v_i$ </td><td>Valuation of buyer  $i$ </td></tr><tr><td> $F_B, f_B$ </td><td>Prior distributions of  $v_i$ ;  $H(v) \equiv \frac{1 - F_B(v)}{f_B(v)}$ </td></tr><tr><td> $v_0$ </td><td>Seller&#x27;s valuation</td></tr><tr><td> $F_S, f_S$ </td><td>Prior distributions of  $v_0$ ;  $h(v_0) \equiv \frac{F_c(v_0)}{f_S(v_0)}$ </td></tr><tr><td> $c_B$ </td><td>Buyers&#x27; participation cost</td></tr><tr><td> $c_S$ </td><td>Seller&#x27;s participation cost</td></tr><tr><td> $\mathbf{v}$ </td><td>Valuation profile;  $\mathbf{v} \equiv (v_0, ..., v_N) \equiv (v_i, ..., \mathbf{v}_{-i})$ </td></tr><tr><td> $\rho_i(\mathbf{v})$ </td><td>Participation probability</td></tr><tr><td> $Q_0(\mathbf{v})$ </td><td>The probability that the seller keeps the object</td></tr><tr><td> $Q_i(\mathbf{v})$ </td><td>The probability that buyer  $i$  is awarded the object</td></tr><tr><td> $P_i(\mathbf{v})$ </td><td>(Expected) payment</td></tr><tr><td> $\hat{v}_i$ </td><td>Report by player  $i$ </td></tr><tr><td> $\Pi$ </td><td>Mediator&#x27;s profit</td></tr></table>

$$
U _ {0} (v _ {0}; v _ {0}) \geq v _ {0}, \forall v _ {0},\tag{IR - S}
$$

where the left-hand side $U _ { 0 } ( \nu _ { 0 } ; \nu _ { 0 } )$ corresponds to the seller's expected payoff within the mechanism (that is, her expected payoff derived from the mechanism), and the right-hand side $\boldsymbol { v } _ { 0 }$ indicates the seller's valuation if she keeps the object. This constraint ensures that the seller, upon participation, willingly gives away the object because she is compensated more than simply consuming the object. Notably, since the participation decision is part of the mechanism, conceptually the seller is allowed to enter the mechanism and then choose the non-participation $( \rho _ { 0 } = 0 )$ ). In this case, the seller's payoff from the mechanism is zero rather than her reservation utility $\nu _ { 0 } .$ Likewise, the following (IR) constraints for the buyers are satis<sup>fi</sup>ed:

$$
U _ {i} (v _ {i}; v _ {i}) \geq 0, \forall v _ {i}, \forall i = 1, \dots , N.\tag{IR - B}
$$

## 4.3. Feasibility

Finally, since the mediator can award the buyers only when the seller participates, we have the following feasibility (F) constraint:

$$
\sum_ {i = 0, \dots , N} \rho_ {i} (\mathbf {v}) Q _ {i} (\mathbf {v}) \leq \rho_ {0} (\mathbf {v}), \forall \mathbf {v},\tag{F}
$$

where the right-hand side is the probability that the seller participates, and the left-hand side is the aggregate probability that the object is awarded to one of the players. The right-hand side of (F) indicates that when the seller does not participate $( \rho _ { 0 } ( \mathbf { v } ) = 0 )$ , the mediator cannot award any object to the buyers. At the other extreme, if the seller participates, at most one buyer (among those participating ones) can win the object. As we include $\rho _ { 0 } ( \mathbf { v } ) Q _ { 0 } ( \mathbf { v } )$ in the left-hand side, we allow the seller to withhold the object even if she participates in the auction.

Note also that the constraint (F) has been a relaxation because we only require it to hold in expectation; nevertheless, the actual feasibility constraint should apply to every instance. This is in line with the classical auction literature as this relaxation does not lead to any discrepancy, and it is easy to verify that the optimal allocation (to be characterized later) satis<sup>fi</sup>es the detailed feasibility constraints. In addition, it is inconsequential if we replace the inequality of (F) by an equality, because at optimality this feasibility constraint is always binding (see the Appendix A for details).

## 4.4. Mediator's problem

Let us now return to the mediator's problem. The mediator's goal is to <sup>fi</sup>nd a set of parameters $\{ \rho _ { i } , Q _ { i } , P _ { i } \}$ that solves the following optimization problem:

$$
\begin{array}{l} (\mathbf {P}) \varPi = \max _ {\rho_ {i} \geq 0, Q _ {i} \geq 0, P _ {i}} \mathbb {E} _ {\mathbf {v}} \sum_ {i = 0, \ldots , N} \rho_ {i} (\mathbf {v}) P _ {i} (\mathbf {v}) \\ \text { s.t. } (\mathrm{IR} - \mathrm{S}), (\mathrm{IR} - \mathrm{B}), (\mathrm{IC}), \text { and } (\mathrm{F}), \end{array}
$$

where $\rho _ { i } ( \pmb { v } ) P _ { i } ( \pmb { v } )$ corresponds to the expected payment collected from player i.

De<sup>fi</sup>ne $J _ { 0 } ( \nu _ { 0 } ) \equiv \nu _ { 0 } + h ( \nu _ { 0 } )$ and $J _ { i } ( \nu _ { i } ) \equiv \nu _ { i } - H ( \nu _ { i } ) \equiv J ( \nu _ { i } )$ for $i = 1 , . . . , N .$ Additionally, we de<sup>fi</sup>ne $G ( \cdot )$ as the distribution function of maximum valuation $\nu _ { M } \equiv m a x _ { i = 1 , . . }$ v ; it can be easily veri<sup>fi</sup>ed that $G ( v _ { M } ) =$ $F _ { B } ^ { N } ( \nu _ { M } )$ for all $\boldsymbol { \nu } _ { M } \in [ \underline { { \boldsymbol { \nu } } } , \bar { \boldsymbol { \nu } } ]$ . Furthermore, de<sup>fi</sup>ne ϕ(v) as the unique function that satis<sup>fi</sup>es $\bar { J } _ { 0 } ( \phi ( \nu ) ) = J ( \nu )$ , i.e.,

$$
\phi (v) + \frac {F _ {S} (\phi (v))}{f _ {S} (\phi (v))} = v - \frac {1 - F _ {B} (v)}{f _ {B} (v)}.
$$

Likewise, de<sup>fi</sup>ne $\psi ( v _ { 0 } )$ as the unique function that satis<sup>fi</sup>es $J ( \psi ( \nu _ { 0 } ) ) = J _ { 0 } ( \nu _ { 0 } )$ , i.e.,

$$
v _ {0} + \frac {F _ {S} (v _ {0})}{f _ {S} (v _ {0})} = \psi (v _ {0}) - \frac {1 - F _ {B} (\psi (v _ {0}))}{f _ {B} (\psi (v _ {0}))}.
$$

The existence of these functions is guaranteed by Assumption 1. In the next proposition, we characterize the revenue maximizing mechanism from the mediator's perspective.

Proposition 1. In the mediator-optimal mechanism:

• The seller with valuation below v<sup>∗</sup> participates, where the cutoff v<sup>∗</sup> is the unique solution to

$$
c _ {S} = \int_ {\psi (v _ {0} ^ {*})} ^ {\overline {{v}}} [ J (v _ {M}) - J _ {0} (v _ {0} ^ {*}) ] N f _ {B} (v _ {M}) F _ {B} ^ {N - 1} (v _ {M}) d v _ {M}.\tag{2}
$$

• Accordingly, the buyers with valuations above $\boldsymbol { v } _ { \ast }$ participate in the auction, where the cutoff v is the unique solution $t o ^ { 2 }$

$$
c _ {B} = F _ {B} ^ {N - 1} (v _ {*}) \int_ {\underline {{V}} _ {0}} ^ {\phi (v _ {*})} [ J (v _ {*}) - J _ {0} (v _ {0}) ] d F _ {0} (v _ {0}).\tag{3}
$$

• Upon the seller's participation, the object is awarded to player i if and only $i f J _ { i } ( \nu _ { i } ) = \mathrm { m a x } _ { j = 0 , \dots , N } \{ J _ { j } ( \nu _ { j } ) \}$ ; ties are broken arbitrarily.

Proposition 1 shows that although we allow for probabilistic participations and allocations, at optimality they turn out to be deterministic. This is reminiscent of the linear programming relaxation approach of integer programs, as the optimal solution turns out to satisfy the (ignored) integer constraints. According to Proposition 1, the participation decisions of both the seller and the buyers exhibit the cutoff structures: while a buyer participates in the mechanism only if her valuation for the object is suf<sup>fi</sup>ciently high, the seller is willing to put up her object for sale when her valuation is low. Given that the buyers incur participation costs, it is conceivable that they are willing to do so only when they like the object a lot. On the other hand, as the seller can always keep her object and stay out of the transactions, the mediator can successfully induce her to agree to sell it only when the seller's private valuation is low.

In terms of the payment rule, there are various ways to implement the optimal allocation and participation decisions, since the bidders are only concerned about their expected payments (by taking expectations over all possible scenarios). For example, all standard auction mechanisms (<sup>fi</sup>rst-price, second-price, Dutch, and English) with reserve prices lead to exactly the same allocation and therefore can all be employed as the payment rule. Accordingly, since the mechanism has to maintain the buyers' individual rationality, a participation subsidy is required to compensate their participation costs. Notably, since in equilibrium the participation decisions are binary $( \rho _ { i } ( \hat { \nu } _ { i } , { \bf v } _ { - i } ) = 0$ or 1), conceptually we can think of it as if the buyers report (or bid) only when they have decided to participate. In this sense, the direct revelation mechanism only requires each bidder to reveal her true type upon participation.<sup>3</sup>

Proposition 1 also allows us to compare the equilibrium outcomes in the conventional seller-optimal auction and our mediator-optimal mechanism. Our <sup>fi</sup>rst observation is that it is more likely that the seller withholds the object ex post.

Corollary 1. Compared with the seller-optimal auction, the seller keeps the object more frequently upon her participation.

To understand this result, recall from the auction literature that $J ( v _ { i } )$ can be regarded as the “virtual surplus” from a type-v bidder. In the conventional seller-optimal auction, it turns out tha $J ( v _ { i } )$ is also the revenue that the auctioneer can extract from the bidder in the presence of information asymmetry. Thus, the seller should allocate the object to the bidder that has the highest virtual surplus, given that the highest virtual surplus exceeds the seller's own valuation $\nu _ { 0 } .$ . In the mediatoroptimal mechanism, however, the seller withholds the object based on her in<sup>fl</sup>ated valuation $J _ { 0 } ( \nu _ { 0 } ) \equiv \nu _ { 0 } + h ( \nu _ { 0 } ) > \nu _ { 0 } ;$ this immediately implies that she withholds the object too often compared to what she would do in the seller-optimal auction.

The primary reason for this discrepancy is that when the mediator acts as the auctioneer, he faces one additional source of information asymmetry because he does not observe directly the seller's valuation. Thus, from the seller's perspective, she attempts to exaggerate her private valuation in exchange of a lower payment. This over-quoting behavior of the seller's outside option necessarily leads to a valuation in<sup>fl</sup>ation as the mediator intends to induce the seller's participation in the mechanism. This valuation in<sup>fl</sup>ation subsequently alters the seller's incentive in the auction stage, and she therefore is more reluctant to give away her own object to the buyers. This valuation in<sup>fl</sup>ation further indicates that the ex post inef<sup>fi</sup>ciency is exacerbated when the mediator serves as the auctioneer, because now the seller's mis-incentive to withhold the object is ampli<sup>fi</sup>ed due to the two-sided private information. Incidentally, the number of potential buyers does not factor into the allocation rule; in this sense, this simple ranking system is portable across various practical situations.

Having discussed the ex post allocations, we now return to the ex ante stage and examine the participation decisions of the seller and the buyers. We <sup>fi</sup>nd that both sides are less willing to participate in the mediator-optimal mechanism.

Corollary 2. Compared with the seller-optimal auction, the mediatoroptimal mechanism induces too little participation for both the seller and the buyers.

The rationale of this ex ante reluctance arises from the ex post inef-<sup>fi</sup>cient allocation. From Corollary 1, the seller has a (further) distorted incentive to withhold the object. Anticipating this, each buyer is less likely to receive the object upon participation and therefore fewer buyers will be engaged in the bidding ex ante. The buyers' reaction also has an adverse effect on the seller's participation decision. Because the seller expects to attract fewer buyers to bid for the object, the competition among the buyers becomes less intense, which subsequently gives rise to a lower expected revenue for the seller. Consequently, the seller is more cautious while determining to put up the object for sale. Collectively, we observe that the mediator's involvement in fact reduces the possibility of successful transactions, and results in a larger degree of inef<sup>fi</sup>ciency both ex ante and ex post.

Finally, let us articulate how the mediator-optimal mechanism can be implemented. Recollect that the direct revelation mechanism is by construction a single-shot scheme as the mediator requests the seller and the buyers report simultaneously. However, we <sup>fi</sup>nd that this optimal mechanism can be implemented via the following two-stage mechanism in a natural way.

Proposition 2. To implement the mediator-optimal mechanism, the mediator can compensate the seller for withholding the object upon participation and delegate the auction design and the corresponding reserve price to the seller. Accordingly, the seller can conduct any standard auction (first-price, second-price, English, or Dutch) and will choose an appropriate reserve price that implements the mediator-optimal mechanism.

As demonstrated in Corollary 1, the mediator should encourage the seller to withhold the object; thus, it is conceivable that he should compensate the seller if she decides to keep the object ex post. As an example, suppose that a second-price auction is adopted. The reserve price shall be set at the level $\psi ( v _ { 0 } )$ so as to facilitate the optimal allocation rule; the optimal reserve prices under other auction formats can be derived similarly. A rather interesting result is that, even though the mediator faces two sources of information asymmetry and serves as the market maker, he can simply request the seller to pay an upfront listing fee upon participation and an associated reserve fee for setting the reserve price; afterwards, he can completely delegate the auction design to the seller and allow her to choose arbitrarily the auction format. This seems to coincide with the current practice of the electronic marketplace, as eBay does not charge the buyers and allows the seller to decide the auction format.

Having discussed the ex post allocation, the ex ante participation decisions, and the implementation of the mediator-optimal mechanism, we in the next section examine some variants and see how robust our results are and whether these modi<sup>fi</sup>cations give rise to additional managerial insights.

## 5. Extensions

In this section, we investigate some variants of our basic model characteristics.

## 5.1. Seller's type-dependent participation cost

When the participation cost is a measure of the time value that the seller spends in registering and preparation, it is possible that a seller with a higher valuation may also value her time more. To incorporate this effect, we amend our basic model with the type-dependent participation cost $c _ { S } ( \nu _ { 0 } )$ , which is assumed to be nonnegative $( c _ { S } ( \nu _ { 0 } ) 2 0 )$ and increasing $( c _ { s } ^ { \prime } ( \nu _ { 0 } ) { \geq } 0 )$ ). This monotonicity is justi<sup>fi</sup>ed as the seller that attaches a higher valuation to her own object is typically wealthier and therefore has a higher opportunity cost. This interpretation of heterogeneous valuations dates back to at least the classical market segmentation paper [26]. With the seller's type-dependent participation cost, we can now derive the alternative mediator-optimal mechanism as summarized in the following proposition.

Proposition 3. Suppose that the seller's participation cost is typedependent. In the mediator-optimal mechanism:

• The seller with valuation below v<sup>t</sup> participates, where the cutoff v<sup>t</sup> is the unique solution to

$$
\begin{array}{l} c _ {S} \Big (v _ {0} ^ {t} \Big) + c _ {S} ^ {\prime} \Big (v _ {0} ^ {t} \Big) h \Big (v _ {0} ^ {t} \Big) \\ = \int_ {\psi \big (v _ {0} ^ {t} \big)} ^ {\bar {v}} \Big [ J (v _ {M}) - J _ {0} \Big (v _ {0} ^ {t} \Big) \Big ] N f _ {B} (v _ {M}) F _ {B} ^ {N - 1} (v _ {M}) d v _ {M}. \end{array}\tag{4}
$$

• Accordingly, the buyers with valuations above v participate in the auction, where the cutoff v is defined via Eq. (3) in Proposition 1.

• Upon the seller's participation, the object is awarded to player i if and only $i f J _ { i } ( \nu _ { i } ) = m a x _ { j = 0 , . . . , N } \{ J _ { j } ( \nu _ { j } ) \}$ ; ties are broken arbitrarily.

Proposition 3 shows that when the seller's participation cost depends on her private valuation, her participation decision will re<sup>fl</sup>ect this dependence as shown in Eq. (4). Nevertheless, the buyers' participation is not altered by this modi<sup>fi</sup>cation, and the ex post allocation rule again relies on the virtual surplus comparisons across the buyers and the seller. Conceptually, one can imagine that the mediator <sup>fi</sup>rst lays out the upfront payment (listing fee) and the reserve fee for the seller that are tailored to endogenize the seller's type-dependent participation cost; afterwards, as the seller is delegated the right to design the auction, he intends to adopt the same allocation rule because the ex ante participation cost and payments are sunk. This separation result provides a handy guideline for the mediator while designing appropriate mechanisms to account for the seller's sophisticated participation concerns.

We can further derive some empirical implications based on this extended setting. To this end, let us employ a speci<sup>fi</sup>c functional form of the seller's type-dependent participation cost as $c _ { S } ( \nu _ { 0 } ) = c _ { S a } + c _ { S b } \nu _ { 0 } ,$ where $c _ { S a }$ corresponds to the base participation cost that every type of seller must incur, and $c _ { S b }$ measures how sensitive the intangible time value is with regard to the seller's true valuation. The higher $c _ { S b }$ is, the more heterogeneous different types of sellers are in terms of participation costs. The following corollary shows that the seller is less likely to participate when their participation costs are higher or more heterogeneous, because in either case it is more costly for the mediator to induce the seller to participate and at the same time incentivize her to reveal her true valuation.

Corollary 3. With the seller's type-dependent participation cost $c _ { S } ( \nu _ { 0 } ) = c _ { S a } + c _ { S b } \nu _ { 0 } ,$ a higher $c _ { S a } \operatorname { o r } c _ { S b }$ leads to a lower cutoff $\nu _ { 0 } ^ { t } .$ However, the buyers' participation is not affected.

## 5.2. Multiple units

Next, let us consider the alternative setting when the seller has multiple identical products to sell. In this case, we assume that the seller is endowed with K units of products, and attaches the same valuation $\boldsymbol { v } _ { 0 }$ to each product. Thus, $\boldsymbol { v } _ { 0 }$ is best interpreted as the pro<sup>fi</sup>t margin that the seller obtains if she sells these products in a different channel rather than via the mediated auction. It is possible to extend our analysis to the case with nonlinear valuation by using the endogenous shadow price approach as in Huang and Sundararajan [11]; nevertheless, the notation will be cumbersome and we leave this aside to avoid distraction. We keep all other model characteristics as in Section 3.

In such a scenario, the mechanism again speci<sup>fi</sup>es the probabilities of participating in the auction and the corresponding payments; nevertheless, the allocation becomes more complicated as we now have to decide how to allocate multiple objects upon the seller's participation. We again use $\rho _ { 0 } ( \mathbf { v } )$ and $\rho _ { i } ( \mathbf { v } ) ^ { \prime }$ s to represent the participation probabilities, and $P _ { 0 } ( \mathbf { v } )$ and $\{ \{ P _ { i } ( { \bf v } ) \} \} ^ { \prime } s$ refer to the (expected) payments. Upon the seller's participation, $Q _ { i } ( \pmb { \nu } )$ denotes the probability that buyer i obtains an object, and $Q _ { 0 } ( \mathbf { v } ) { \equiv } K - \sum _ { i = 1 , . . . , N } Q _ { i } ( \pmb { v } )$ therefore corresponds to the expected number of objects the seller keeps after the bidding stage. Given this alternative interpretation of $Q _ { 0 } ( \mathbf { v } )$ the sequence of events and the mediator's optimization problem formulation remain the same, except that now the seller's individual rationality constraint becomes:

$$
U _ {0} (v _ {0}; v _ {0}) \geq K v _ {0}, \forall v _ {0},\tag{IR - S'}
$$

where

$$
U _ {0} (v _ {0}; \hat {v} _ {0}) \equiv \mathbb {E} _ {\mathbf {v} _ {- 0}} \left\{\rho_ {0} (\hat {v} _ {0}, \mathbf {v} _ {- 0}) [ v _ {0} Q _ {0} (\hat {v} _ {0}, \mathbf {v} _ {- 0}) - P _ {0} (\hat {v} _ {0}, \mathbf {v} _ {- 0}) - c _ {S} ] + [ 1 - \rho_ {0} (\hat {v} _ {0}, \mathbf {v} _ {- 0}) ] K v _ {0} \right\}.
$$

We omit the detailed formulation and proceed to characterize the optimal mechanism. The results are summarized in the following proposition. For ease of notation, we de<sup>fi</sup>ne the order statistics $V _ { 1 } \equiv \mathrm { m a x } _ { i = 1 , \dots , N } V _ { i }$ as the highest valuation among the buyers, $V _ { 2 } \equiv$ $m a x _ { i = 1 , \dots , N } \{ \nu _ { i } | \nu _ { i } < V _ { 1 } \}$ as the second highest valuation, and so on for $V _ { i } , i { = } 3 , . . . , N$ . Additionally, let $G _ { i } ( V _ { i } )$ denote the distribution function of the i-th order statistics among {v }'s, and $\{ g _ { i } ( V _ { i } ) \}$ 's represent their corresponding density functions. These distribution functions all have closed-form expressions, e.g., $G _ { 1 } ( V _ { 1 } ) = F _ { B } ^ { N } ( V _ { 1 } )$ and $G _ { N } ( V _ { N } ) =$ $1 - [ 1 - F _ { B } ( V _ { N } ) ] ^ { N } .$ We further define $d G ^ { K } ( { \bf v } ) \equiv d G _ { 1 } ( V _ { 1 } ) \times \cdots \times d G _ { K } ( V _ { K } )$ and $d G ^ { K - 1 } ( \mathbf { v } ) \equiv d G _ { 1 } ( V _ { 1 } ) \times \cdots \times d G _ { K - 1 } ( V _ { K - 1 } )$

Proposition 4. In the mediator-optimal mechanism:

• There exist two cutoffs v<sup>K</sup> and $\nu _ { * } ^ { K }$ such that the seller with valuation below v<sup>K</sup> participates and the buyers with valuations above v<sup>K</sup> participate.

• Upon the seller's participation, a buyer i is awarded an object $i f J ( v _ { i } ) \ge$ $J _ { 0 } ( v _ { 0 } )$ and is among the K highest values of $\{ J _ { l } ( v _ { l } ) \} \colon$ s; ties are broken arbitrarily.

The above proposition shows that when the seller is endowed with multiple units, the participation decisions from both sides become more sophisticated; nevertheless, the allocation rule remains simple as it resembles the result from the classical multi-unit auction. As in Section $^ { 4 , }$ the mediator intentionally distorts the seller's incentive to withhold the objects more often; consequently, the seller decides whether to award the buyers based on her own virtual valuation $J _ { 0 } ( \nu _ { 0 } )$ rather than her true valuation. This valuation in<sup>fl</sup>ation again leads to the more pronounced ex post inef<sup>fi</sup>ciency compared to the seller-optimal multi-unit auction.

In terms of participation decisions, Proposition 4 suggests a two-step calculation procedure. First, the mediator can calculate the buyers' participation cutoff $v _ { * } ^ { K }$ (speci<sup>fi</sup>ed in the Appendix $\mathsf { A } ) ;$ ; second, the mediator can then use this v<sup>K</sup> to recursively obtain the participation cutoff $\boldsymbol { v } _ { 0 } ^ { K }$ for the seller. In the following, we give a simple example for which the cutoff levels can be easily computed. When $N { = } K { = } 2$ , the derivations in the Appendix A lead to the following simple expressions:

$$
\begin{array}{l} c _ {S} = \int_ {\psi (v _ {0} ^ {*})} ^ {\overline {{v}}} \int_ {v _ {*}} ^ {V _ {1}} [ J (V _ {1}) - J _ {0} (v _ {0} ^ {*}) ] d G ^ {2} (\mathbf {v}) \\ \qquad + \int_ {\psi (v _ {0} ^ {*})} ^ {\overline {{v}}} \int_ {\psi (v _ {0} ^ {*})} ^ {V _ {1}} [ J (V _ {1}) + J (V _ {2}) - 2 J _ {0} (v _ {0} ^ {*}) ] d G ^ {2} (\mathbf {v}), \\ 2 c _ {B} f _ {B} (v _ {*}) = g _ {2} (v _ {*}) \int_ {v _ {*}} ^ {\overline {{v}}} \left[ \begin{array}{c} \int_ {\underline {{V}} _ {0}} ^ {\phi (v _ {*})} [ J (V _ {1}) + J (v _ {*}) - 2 J _ {0} (v _ {0}) ] d F _ {0} (v _ {0}) \\ + \int_ {\phi (v _ {*})} ^ {\phi (V _ {1})} [ J (V _ {1}) - J _ {0} (v _ {0}) ] d F _ {0} (v _ {0}) \end{array} \right] d G ^ {K - 1} (\mathbf {v}). \end{array}
$$

The detailed derivations are omitted.

## 5.3. Multiple sellers

Let us now examine the situation in which multiple sellers may intend to sell homogeneous products to the buyers.

## 5.3.1. Model setting

In this case, even though the products are identical, different sellers may attach different valuations that are privately observable to themselves. To this end, we assume that there are I sellers (and N buyers) and modify our notation for ease of illustration. In this extended setting, the sellers' valuations are i.i.d. random draws from the common distribution $F _ { S } ,$ and the buyers' valuations are i.i.d. random draws from the common distribution $F _ { B } .$ Let $f _ { S }$ and $f _ { B }$ represent their corresponding density functions, and s;s  and v; v  are their supports, respectively.

As there are multiple sellers, it is no longer convenient to use a single label 0 to represent them. We index the sellers by $j = 1 , . . . , I$ and the buyers by $i = 1 , . . . , N .$ We use $s _ { j }$ to denote the valuation realization of seller j, and $\nu _ { i }$ to denote the valuation realization of buyer i. We maintain the regularity conditions in Assumption 1. We assume that each player (either a seller or a buyer) demands at most one unit of product; additional units generate no extra utilities for any player if she has one already.

Confronted with multiple sellers and buyers, the mechanism should specify the probabilities of participating in the auction, the allocation of the object, and the corresponding payments. With some abuse of notation, we let $\pmb { \mathsf { s } } \equiv ( s _ { 1 } , \ldots , s _ { I } )$ and $\mathbf { v } \equiv ( \nu _ { 1 } , . . . , \nu _ { N } )$ represent the type vectors of the sellers and the buyers; moreover, we de<sup>fi</sup>ne $\pmb { \mathscr { s } } _ { - j } \equiv \left( \mathscr { s } _ { 1 } , ~ . . . , \mathscr { s } _ { j - 1 } , \mathscr { S } _ { j + 1 } , ~ . . . , \mathscr { S } _ { I } , \mathscr { V } _ { 1 } , ~ . . . , \mathscr { V } _ { N } \right)$ as the type pro<sup>fi</sup>le of other players except seller j, and $\mathbf { v } _ { - i } \equiv ( s _ { 1 } , . . . , s _ { I } , \allowbreak \nu _ { 1 } , . . . , \allowbreak \nu _ { i - 1 } , \allowbreak \nu _ { i + 1 } , . . . , \allowbreak \nu _ { N } )$ is the type pro<sup>fi</sup>le of other players excluding buyer i. Thus, $( \pmb { \mathscr { s } } , \pmb { v } ) \equiv ( s _ { j } , \pmb { \mathscr { s } } _ { - j } ) \equiv$ $\left( \boldsymbol { v } _ { i } , \mathbf { v } _ { - i } \right)$

We use $\{ \rho _ { j } ^ { S } ( \pmb { \mathscr { s } } , \pmb { v } ) \} ^ { \prime } \ d \mathbf { s }$ and $\{ \rho _ { i } ^ { B } ( \pmb { \mathscr { s } } , \pmb { v } ) \} ^ { \prime } \ d \mathbf { s }$ to represent the participation probabilities of the sellers and the buyers, respectively. If at least one seller participates, we let $Q _ { j } ^ { S } ( \pmb { \mathscr { s } } , \pmb { \nu } )$ denote the probability that sell-$\operatorname { e r } j$ keeps one object (which is certainly her own object as all the objects are homogeneous); likewise, we use $Q _ { i } ^ { B } ( \pmb { s } , \pmb { v } )$ to denote the probability that buyer i is awarded an object. Accordingly, $\{ P _ { j } ^ { S } ( \pmb { \mathscr { s } } , \pmb { \nu } ) \} ^ { \prime } \pmb { S }$ and $\{ P _ { i } ^ { B } ( \pmb { \mathscr { s } } , \pmb { \nu } ) \}$ 's refer to the (expected) payments the mediator collects from the sellers and the buyers. Given the above mechanism, the sequence of events is almost the same except that now multiple sellers move simultaneously. Next, we characterize the optimal mechanism from the mediator's perspective.

## 5.3.2. Problem formulation

In order to characterize the mediator-optimal mechanism, we again start with the seller's and the buyers' reporting strategies. Suppose that seller j's true type is $s _ { j }$ but she reports it as ${ \hat { s } } _ { j } .$ Assuming that all other players report truthfully, this seller's expected payoff based on this reporting strategy is

$$
U _ {j} ^ {S} \left(s _ {j}; \hat {s} _ {j}\right) \equiv \mathbb {E} _ {\mathbf {s} _ {- j}} \left\{\rho_ {j} ^ {S} \left(\hat {s} _ {j}, \mathbf {s} _ {- j}\right) \left[ s _ {j} Q _ {j} ^ {S} \left(\hat {s} _ {j}, \mathbf {s} _ {- j}\right) - P _ {j} ^ {S} \left(\hat {s} _ {j}, \mathbf {s} _ {- j}\right) - c _ {S} \right] + \left[ 1 - \rho_ {j} ^ {S} \left(\hat {s} _ {j}, \mathbf {s} _ {- j}\right) \right] s _ {j} \right\},
$$

where the misreport affects the probability of participation $\rho _ { 0 } \big ( \hat { s } _ { j } , \pmb { \mathscr { s } } _ { - j } \big )$ the allocation $Q _ { j } ^ { S } \left( \hat { s } _ { j } , \pmb { \mathscr { s } } _ { - j } \right)$ , and the payment $P _ { j } ^ { S } \left( \hat { s } _ { j } , \pmb { \mathscr { s } } _ { - j } \right)$ . Likewise, if a type- v buyer i unilaterally reports to be type- $\cdot \hat { \boldsymbol { v } } _ { i } ,$ , her expected payoff is

$$
U _ {i} ^ {B} (v _ {i}; \hat {v} _ {i}) \equiv \mathbb {E} _ {\mathbf {v} _ {- i}} \left\{\rho_ {i} ^ {B} (\hat {v} _ {i}, \mathbf {v} _ {- i}) \left[ v _ {i} Q _ {i} (\hat {v} _ {i}, \mathbf {v} _ {- i}) - P _ {i} ^ {B} (\hat {v} _ {i}, \mathbf {v} _ {- i}) - c _ {B} \right] \right\}.
$$

We can then write down the following incentive compatibility constraints:

$$
U _ {j} ^ {S} \left(s _ {j}; s _ {j}\right) \geq U _ {j} ^ {S} \left(s _ {j}; \hat {s} _ {j}\right), \forall s _ {j}, \hat {s} _ {j}, \forall j,\tag{IC - S}
$$

$$
U _ {i} ^ {B} (v _ {i}; v _ {i}) \geq U _ {i} ^ {B} (v _ {i}; \hat {v} _ {i}), \forall v _ {i}, \hat {v} _ {i}, \forall i.\tag{IC - B}
$$

Likewise, the individual rationality (IR) constraints become:

$$
U _ {j} ^ {S} \left(s _ {j}; s _ {j}\right) \geq s _ {j}, \forall s _ {j}, \forall j, \text { and } U _ {i} ^ {B} (v _ {i}; v _ {i}) \geq 0, \forall v _ {i}, \forall i.\tag{IR}
$$

With multiple sellers, we have the following feasibility (F) constraint:

$$
\sum_ {j = 1, \dots , I} \rho_ {j} ^ {S} (\mathbf {s}, \mathbf {v}) Q _ {j} ^ {S} (\mathbf {s}, \mathbf {v}) + \sum_ {i = 0, \dots , N} \rho_ {i} ^ {B} (\mathbf {s}, \mathbf {v}) Q _ {i} ^ {B} (\mathbf {s}, \mathbf {v}) \leq \sum_ {j = 1, \dots , I} \rho_ {j} ^ {S} (\mathbf {s}, \mathbf {v}), \forall \mathbf {s}, \mathbf {v},\tag{\( (F') \}
$$

where the right-hand side is the expected number of objects from the participating sellers, and the left-hand side is the expected number of objects awarded during the auction.

Let us now return to the mediator's problem. The mediator's goal is to <sup>fi</sup>nd a set of parameters $\{ \rho _ { j } ^ { S } , Q _ { j } ^ { S } , P _ { j } ^ { S } , \rho _ { i } ^ { B } , Q _ { i } ^ { B } , P _ { i } ^ { B } \}$ that solves the following optimization problem:

$$
(\mathbf {P 2}) \Pi = \max _ {\rho_ {j} ^ {S}, \rho_ {i} ^ {B} \geq 0, Q _ {j} ^ {S}, Q _ {i} ^ {B} \geq 0, P _ {j} ^ {S}, P _ {i} ^ {B}} \mathbb {E} _ {\mathbf {s}, \mathbf {v}} \left[ \sum_ {i = 1, \dots , I} \rho_ {j} ^ {S} (\mathbf {s}, \mathbf {v}) P _ {j} ^ {S} (\mathbf {s}, \mathbf {v}) + \sum_ {i = 1, \dots , N} \rho_ {i} ^ {B} (\mathbf {s}, \mathbf {v}) P _ {i} ^ {B} (\mathbf {s}, \mathbf {v}) \right]
$$

$$
\begin{array}{l} \text { s.t. } (\mathrm{IR}), (\mathrm{IC} - \mathrm{S}), (\mathrm{IC} - \mathrm{B}), \text { and } (\mathrm{F} ^ {\prime}). \end{array}
$$

In the next proposition, we provide a characterization of the opti mal allocation. De<sup>fi</sup>ne ${ \cal J } _ { \cal S } ( s _ { j } ) \equiv s _ { j } + h ( s _ { j } )$ and $J _ { B } ( \nu _ { i } ) \equiv \nu _ { i } - H ( \nu _ { i } )$

Proposition 5. With multiple sellers, in the mediator-optimal mecha nism: there exist two cutoffs $s ^ { * }$ and v such that a seller participates if and only $i f$ her valuation is below $s ^ { * } ,$ and a buyer participates $i f$ and only $i f$ her valuation is above $\boldsymbol { v } _ { \ast \ast }$ Upon the participation of m sellers, the object is awarded to buyer i if and only $i f J _ { B } ( \nu _ { i } )$ is among the m highest values of $\{ J _ { S } ( s _ { j } ) \} ^ { \prime } s$ and $\{ J _ { B } ( \nu _ { l } ) \} ^ { \prime } s ,$ ; ties are broken arbitrarily.

Proposition 5 shows that the cutoff structures from both sides are not prone to the seller competition: each buyer decides to bid if her valuation regarding the object is suf<sup>fi</sup>ciently high, and each seller participates if she attaches a low valuation to her own object. Furthermore, the allocation of the objects for sale again depends on the virtual surpluses that the participating sellers and buyers generate. Thus, allocative inef<sup>fi</sup>ciency arises ex post, and it is conceivable that ex ante participation decisions will also be distorted for both the sellers and the buyers. We omit the detailed characterization of the cutoff levels for conciseness.

## 6. Conclusions

In this paper, we attempt to provide a uni<sup>fi</sup>ed, easily extendable framework to investigate the mediator-optimal mechanism in the electronic marketplace, taking into account the two sources of information asymmetry and the costly participation from both sides. We prove the cutoff structures of the participation decisions of both the seller and the buyers, and compare the equilibrium outcomes in the conventional seller-optimal auction and our mediator-optimal mechanism. Our analysis reveals that the seller keeps the object more frequently ex post, and the mediator-optimal mechanism induces too little ex ante participation. Collectively, we observe that the mediator's involvement in fact reduces the possibility of successful transactions, and results in a larger degree of inef<sup>fi</sup>ciency both ex ante and ex post. We further extend our results to incorporate the possibilities of heterogeneous participation costs, multiple units, and multiple sellers, and <sup>fi</sup>nd that our qualitative results are not prone to these modi<sup>fi</sup>cations.

Incidentally, although in this paper we focus on the regular auction in which the seller is endowed with an object for sale, our results can be converted to the situation in which the buyer conducts a reverse auction in search of an appropriate supplier. In such a procurement auction context, the mediator in this case may be the middleman such as Li and Fung. Following the procedure laid out above, we can verify that the ex post allocative inef<sup>fi</sup>ciency again arises in the mediated auction compared to the conventional “buyer-optimal” auction; additionally, this ex post inef<sup>fi</sup>ciency leads to ex ante inef<sup>fi</sup>- cient participation from both sides.

Our analysis may be extended in a couple of ways. For example, in our basic setting the mediator possesses his monopoly power while setting up the platform. Nevertheless, in reality eBay faces competition from Yahoo! and other Internet auction websites. In such a scenario, it would be intriguing to see how these mediators determine their fee policies and mechanisms, and how the competition between mediators affects the participation decisions of the sellers and buyers. As another possible extension, the sellers may have heterogeneous products for sale; accordingly, the mediator has to induce the seller to disclose the true valuations she has on different products, and decides whether to conduct a single grand auction to sell (some of) those products or conduct several separate auctions for these products. This remains a research priority.

## Acknowledgments

I thank Andrew Whinston (Editor) and the reviewers for the valuable comments that signi<sup>fi</sup>cantly improved the paper. I have also bene<sup>fi</sup>ted from the discussions with Itai Ashlagi, Jianqing Chen, Jane Feng, Ke-Wei Huang, Dimitri Kostamis, Ling-Chieh Kung, De Liu, and Zhixi Wan. All the remaining errors are my own.

## Appendix A. Proofs

Proof of Proposition 1. The proof procedure follows the standard literature of mechanism design. We <sup>fi</sup>rst replace the incentive compatibility constraints by a set of weaker constraints. This gives rise to a relaxed problem of (P). We then characterize the optimal solution to the relaxed problem via <sup>fi</sup>rst-order conditions. Afterwards, we show that the candidate solution exhibits the cutoff structure indicated in the proposition and is also feasible to problem (P); thus, it attains the maximum value and is indeed optimal. Finally, we characterize the optimal cutoff levels.

Let us <sup>fi</sup>rst rewrite the incentive compatibility constraints. We start with the buyers' incentive problems and de<sup>fi</sup>ne $\mathcal { U } _ { i } ( \nu _ { i } ) \equiv \mathcal { U } _ { i } ( \nu _ { i } ; \nu _ { i } )$ . From (IC), we obtain that

$$
\mathcal {U} _ {i} (v _ {i}) \equiv \max _ {\hat {v} _ {i}} \mathbb {E} _ {\mathbf {v} _ {- i}} \{\rho_ {i} (\hat {v} _ {i}, \mathbf {v} _ {- i}) [ v _ {i} Q _ {i} (\hat {v} _ {i}, \mathbf {v} _ {- i}) - P _ {i} (\hat {v} _ {i}, \mathbf {v} _ {- i}) - c _ {B} ] \}.
$$

The envelope theorem thus implies that

$$
\frac {d}{d v _ {i}} \mathcal {U} _ {i} (v _ {i}) = \frac {\partial}{\partial v _ {i}} \mathcal {U} _ {i} (v _ {i}; \hat {v} _ {i}) \Big | _ {\hat {V} _ {i}} = v _ {i} = \mathbb {E} _ {\mathbf {v} _ {- i}} \{\rho_ {i} (\mathbf {v}) Q _ {i} (\mathbf {v}) \}.
$$

Note that the above term is always non-negative. Thus, the integral form is (from Fundamental Theorem of Calculus):

$$
\mathcal {U} _ {i} (v _ {i}) = \mathcal {U} _ {i} (v) + \int_ {\underline {{v}}} ^ {v i} \mathbb {E} _ {\mathbf {v} _ {- i}} \{\rho_ {i} (u, \mathbf {v} _ {- i}) Q _ {i} (u, \mathbf {v} _ {- i}) \} d u.
$$

Now we switch to the seller's incentive compatibility constraint. In this case, we de<sup>fi</sup>ne $\mathcal { U } _ { 0 } ( \nu _ { 0 } ; \hat { \nu } _ { 0 } ) \equiv \mathcal { U } _ { 0 } ( \nu _ { 0 } ; \hat { \nu } _ { 0 } ) - \nu _ { 0 }$ and $U _ { 0 } ( \nu _ { 0 } ) \equiv U _ { 0 } ( \nu _ { 0 } ; \nu _ { 0 } )$ . Thus,

$$
\mathcal {U} _ {0} (v _ {0}) \equiv \max _ {\hat {v} _ {0}} \mathbb {E} _ {\mathbf {v} _ {- 0}} \{\rho_ {0} (\hat {v} _ {0}, \mathbf {v} _ {- 0}) [ v _ {0} Q _ {0} (\hat {v} _ {0}, \mathbf {v} _ {- 0}) - P _ {0} (\hat {v} _ {0}, \mathbf {v} _ {- 0}) - c _ {S} ] + [ 1 - \rho_ {0} (\hat {v} _ {0}, \mathbf {v} _ {- 0}) ] v _ {0} \} - v _ {0},
$$

and according to the envelope theorem we obtain that:

$$
\frac {d}{d v _ {0}} \mathcal {U} _ {0} (v _ {0}) = \frac {\partial}{\partial v _ {0}} u _ {0} (v _ {0}; \hat {v} _ {0}) | _ {\hat {v} _ {0} = v _ {0}} = - 1 - \mathbb {E} _ {v - 0} \{\rho_ {0} (v) [ 1 - Q _ {0} (v) ] \} \leq 0,
$$

$$
\Rightarrow \mathcal {U} _ {0} (v _ {0}) = \mathcal {U} _ {0} (\bar {v} _ {0}) + \int_ {v _ {0}} ^ {\bar {v} _ {0}} [ 1 + \{\rho_ {0} (u, v _ {- 0}) [ 1 - Q _ {0} (u, v _ {- 0}) ] \} ] d u,
$$

where the integral form follows from the negativity of $d \mathcal { U } _ { 0 } ( \nu _ { 0 } ) / d \nu _ { 0 } .$

2) The candidate solution and its verification:

From the above derivations, the aggregate expected payments can be expressed as

$$
\begin{array}{l} \Pi = \mathbb {E} _ {\mathbf {v}} \sum_ {i = 0, \dots , N} \rho_ {i} (v) P _ {i} (v) \\ = \mathbb {E} _ {\mathbf {v}} \left\{ \begin{array}{c} \rho_ {0} (v) v _ {0} Q _ {0} (v) - \rho_ {0} (v) c _ {S} - \rho_ {0} (v) v _ {0} - \mathcal {U} _ {0} (\bar {v} _ {0}) - \int_ {v _ {0}} ^ {\bar {v}} 0 \Big [ 1 + \mathbb {E} _ {\mathbf {v} _ {- 0}} \{\rho (u, v _ {- 0}) [ 1 - Q _ {0} (u, v _ {- 0}) ] \} \Big ] d u \\ + \sum_ {i = 1, \dots , N} \Big [ \rho_ {i} (v) v _ {i} Q _ {i} (v) - \rho_ {i} (v) c _ {B} - U _ {i} (v) - \int_ {\underline {{v}}} ^ {v i} \mathbb {E} _ {\mathbf {v} _ {- i}} \{\rho_ {i} (u, v _ {- 1}) Q _ {i} (u, v _ {- 1}) \} d u ] \end{array} \right\}. \end{array}
$$

As the mediator's objective Π is decreasing in ${ \cal U } _ { 0 } ( \bar { \nu } _ { 0 } )$ and $\{ \mathcal { U } _ { i } ( \underline { { \nu } } ) \} ^ { \prime } \mathbf { s } ,$ at optimality ${ \mathcal { U } } _ { 0 } ( { \bar { \nu } } _ { 0 } )$ and $\{ \mathscr { U } _ { i } ( \underline { { \nu } } ) \} ^ { \prime } s$ should be zero. Additionally, we can <sup>U ð Þ</sup>apply integration by parts and rewrite Π as follows:

$$
\Pi = \mathbb {E} _ {\mathbf {v}} \Bigg \{ \begin{array}{c} - (v _ {0} + h (v _ {0})) \rho_ {0} (\mathbf {v}) [ 1 - Q _ {0} (\mathbf {v}) ] - \rho_ {0} (\mathbf {v}) c _ {S} - h (v _ {0}) \\ + \sum_ {i = 1, \dots , N} [ \rho_ {i} (\mathbf {v}) Q _ {i} (\mathbf {v}) (v _ {i} - H (v _ {i})) - \rho_ {i} (\mathbf {v}) c _ {B} ] \end{array} \Bigg \}
$$

$$
= \mathbb {E} _ {\mathbf {v}} \left\{ \begin{array}{c} - (v _ {0} + h (v _ {0})) \rho_ {0} (\mathbf {v}) [ 1 - Q _ {0} (\mathbf {v}) ] + \sum_ {i = 1, \ldots , N} [ \rho_ {i} (\mathbf {v}) Q _ {i} (\mathbf {v}) (v _ {i} - H (v _ {i})) ] \\ - \rho_ {0} (\mathbf {v}) c _ {S} - \sum_ {i = 1, \ldots , N} \rho_ {i} (\mathbf {v}) c _ {B} - h (v _ {0}) \end{array} \right\},
$$

where we recall that $\begin{array} { r } { h ( \nu _ { 0 } ) \equiv \frac { F _ { S } ( \nu _ { 0 } ) } { f _ { S } ( \nu _ { 0 } ) } } \end{array}$ and $\begin{array} { r } { H ( \nu ) \equiv \frac { 1 - F _ { B } ( \nu ) } { f _ { B } ( \nu ) } } \end{array}$ . Note that $J _ { 0 } ( \nu _ { 0 } ) \equiv \nu _ { 0 } + h ( \nu _ { 0 } )$ and $J _ { i } ( \nu _ { i } ) \equiv \nu _ { i } - H ( \nu _ { i } )$ . The above expression can be rewritten as

$$
\Pi = \mathbb {E} _ {\mathbf {v}} \Bigg \{\sum_ {i = 0, \dots , N} J _ {i} (v _ {i}) \rho_ {i} (v) Q _ {i} (v) - \rho_ {0} (v) [ c _ {S} + J _ {0} (v _ {0}) ] - \sum_ {i = 1, \dots , N} \rho_ {i} (\mathbf {v}) c _ {B} - h (v _ {0}) \Bigg \}.\tag{5}
$$

Recollect the feasibility constraint: $\sum _ { i = 0 , . . . , N } \rho _ { i } ( \mathbf { v } ) Q _ { i } ( \mathbf { v } ) { \leq } \rho _ { 0 } ( \mathbf { v } )$ , v. Given the expression in $\operatorname { E q . } \left( 5 \right)$ , we can then pointwise maximize over the joint terms $\{ \rho _ { i } ( { \bf v } ) Q _ { i } ( { \bf v } ) \} ^ { \prime } { \bf s } \colon$

$$
\rho_ {i} (\mathbf {v}) Q _ {i} (\mathbf {v}) = \left\{ \begin{array}{c c} \rho_ {0} (\mathbf {v}), & \text { if } J _ {i} (v _ {i}) = \max _ {j = 0, \ldots , N} \left\{J _ {j} \Big (v _ {j} \Big) \right\}, \\ 0, & \text { otherwise }. \end{array} \right.
$$

Ties are broken arbitrarily. Accordingly, the mediator's expected payoff becomes:

$$
\Pi = \mathbb {E} _ {\mathbf {v}} \left\{\rho_ {0} (\mathbf {v}) \max _ {i = 0, \dots , N} \left\{J _ {i} (v _ {i}) \right\} - \rho_ {0} (\mathbf {v}) \left[ c _ {S} + J _ {0} (v _ {0}) \right] - \sum_ {i = 1, \dots , N} \rho_ {i} (\mathbf {v}) c _ {B} - h (v _ {0}) \right\}.
$$

Note that Assumption 1 implies that $J _ { i } ( \nu _ { i } )$ is increasing in $\nu _ { i }$ for all i. Thus, at optimality it is without loss of generality to consider only the equilibrium with the cutoff structure: every buyer i participates if and only if her valuation exceeds a cutoff v . That is ${ \bf \nabla } . \rho _ { i } ( { \bf v } ) = 1 \{ { \nu } _ { i } \ge { \nu } _ { * } \}$ for all i. Given this, we can then expand the integral form of Π and rewrite it as

$$
\Pi = \mathbb {E} _ {\mathbf {v}} \bigg \{\rho_ {0} (\mathbf {v}) \underset {i = 0, \dots , N} {\max} \{J _ {i} (v _ {i}) \} - \rho_ {0} (\mathbf {v}) [ c _ {S} + J _ {0} (v _ {0}) ] - h (v _ {0}) \bigg \} - N c _ {B} [ 1 - F _ {B} (v _ {*}) ],
$$

and the <sup>fi</sup>rst term is active only when the $\mathrm { t y p e } { \cdot } v _ { 0 }$ seller is not excluded by the mechanism. The coef<sup>fi</sup>cient of $\rho _ { 0 } ( \mathbf { v } )$ in the integrand is $\mathrm { m a x } ( J _ { 0 } ( \nu _ { 0 } ) , \mathrm { m a x } _ { i = 1 , \dots , N } \{ J _ { i } ( \nu _ { i } ) \} ) - c _ { S } - J _ { 0 } ( \nu _ { 0 } )$ , which is decreasing in $\nu _ { 0 } .$ Consequently, the mediator should exclude the seller from above, i.e., there exists a cutoff level $\check { v _ { 0 } }$ such that the seller participates in the mechanism if and only if $\nu _ { 0 } \leq \nu _ { 0 } ^ { * } .$ It is also worth mentioning that the above allocation rule necessarily implies that $\rho _ { i } ( \mathbf { v } ) Q _ { i } ( \mathbf { v } )$ is increasing in v and therefore the global incentive compatibility constraints are satis<sup>fi</sup>ed. The individual rationality constraints hold trivially as ${ \mathcal { U } } _ { 0 } ( { \bar { \nu } } _ { 0 } )$ and $\{ \mathcal { U } _ { i } ( \underline { { \nu } } ) \} \colon$ are 0 and all other types obtain a weakly higher expected payoff than these cutoff types do

3) Optimal cutoffs:

Let us now pin down the optimal cutoffs $\boldsymbol { \nu } _ { 0 } ^ { * }$ and $\nu _ { * }$ . To this end, we <sup>fi</sup>rst recall the notation $\nu _ { M } \mathbf { \equiv } \mathrm { m a x } _ { i = 1 , \dots , N } V _ { i }$ and the corresponding distri bution function $G ( \nu _ { M } ) = F _ { B } ^ { N } ( \nu _ { M } ) .$ As Assumption 1 guarantees the monotone hazard rates, for any given instance $\{ \nu _ { i } , i = 0 , . . . , N \}$ , we have that $m a x _ { i = 0 , \ldots , N } \{ J _ { i } ( \nu _ { i } ) \} = m a x \{ J _ { 0 } ( \nu _ { 0 } ) , J ( \nu _ { M } ) \}$ . With this change of expressions, we can rewrite the mediator's expected payoff as follows:

$$
\Pi = \int_ {V _ {0}} ^ {v _ {0} ^ {*}} \int_ {v _ {*}} ^ {\overline {{v}}} [ \max \{J _ {0} (v _ {0}), J (v _ {M}) \} - J _ {0} (v _ {0}) ] d G (v _ {M}) d F _ {0} (v _ {0}) - \mathbb {E} h (v _ {0}) - c _ {S} F _ {S} (v _ {0} ^ {*}) - N c _ {B} [ 1 - F _ {B} (v _ {*}).\tag{6}
$$

$$
\Pi = \int_ {V _ {0}} ^ {v _ {0} ^ {*}} \int_ {\psi (v _ {0})} ^ {\overline {{v}}} [ J (v _ {M}) - J _ {0} (v _ {0}) ] d G (v _ {M}) d F _ {0} (v _ {0}) - c _ {S} F _ {S} \big (v _ {0} ^ {*} \big) - \mathbb {E} h (v _ {0}) - N c _ {B} [ 1 - F _ {B} (v _ {*}) ].
$$

The above equation can be rearranged as we recall the de<sup>fi</sup>nition of $\psi ( \nu _ { 0 } )$ . Speci<sup>fi</sup>cally, ma $\ B = \{  { V _ { 0 } } (  { V _ { 0 } } ) , J (  { V _ { M } } ) \} = J (  { V _ { M } } )$ if and only if $\nu _ { M } { \geq } \psi ( \nu _ { 0 } ) . { \mathrm { C o n - } }$ sequently,

Differentiating the above equation with respect to $\nu _ { 0 } ^ { * } ,$ we obtain the following <sup>fi</sup>rst-order condition:

$$
c _ {S} = \int_ {\psi (v _ {0} ^ {*})} ^ {\overline {{v}}} [ J (v _ {M}) - J _ {0} (v _ {0} ^ {*}) ] d G (v _ {M}) = \int_ {\psi (v _ {0} ^ {*})} ^ {\overline {{v}}} [ J (v _ {M}) - J _ {0} (v _ {0} ^ {*}) ] N f _ {B} (v _ {M}) F _ {B} ^ {N - 1} (v _ {M}) d v _ {M},
$$

where in the last equality we apply the de<sup>fi</sup>nition of $G ( v _ { M } )$

Likewise, we can also rewrite the mediator's function and characterize the optimal cutoff $\boldsymbol { v } _ { \ast \ast }$ . Speci<sup>fi</sup>cally, rearranging Eq. (6) and

$$
\begin{array}{l} \Pi = \int_ {v _ {*}} ^ {\overline {{v}}} \int_ {V _ {0}} ^ {v _ {0} ^ {*}} [ \max \{J _ {0} (v _ {0}), J (v _ {M}) \} - J _ {0} (v _ {0}) ] d F _ {0} (v _ {0}) d G (v _ {M}) - c _ {S} F _ {S} \big (v _ {0} ^ {*} \big) - \mathbb {E} h (v _ {0}) - N c _ {B} [ 1 - F _ {B} (v _ {*}) ] \\ = \int_ {v _ {*}} ^ {\overline {{v}}} \int_ {V _ {0}} ^ {\phi (v _ {M})} [ J (v _ {M}) - J _ {0} (v _ {0}) ] d F _ {0} (v _ {0}) d G (v _ {M}) - c _ {S} F _ {S} \big (v _ {0} ^ {*} \big) - \mathbb {E} h (v _ {0}) - N c _ {B} [ 1 - F _ {B} (v _ {*}) ], \end{array}
$$

where we have used the fact that ma $\scriptstyle \{ J _ { 0 } ( \nu _ { 0 } ) , J ( \nu _ { M } ) \} = J ( \nu _ { M } )$ if and only if $\nu _ { 0 } \le \phi (  { \boldsymbol { \nu } } _ { M } )$ Differentiating the above equation with respect to $\nu _ { * }$ we obtain the following <sup>fi</sup>rst-order condition:

$$
\begin{array}{c} N c _ {B} f _ {B} (v _ {*}) = \int_ {\underline {{V}} _ {0}} ^ {\phi (v _ {*})} [ J (v _ {*}) J _ {0} (v _ {0}) ] d F _ {0} (v _ {0}) N f _ {B} (v _ {*}) F _ {B} ^ {N - 1} (v _ {*}), \\ \iff c _ {B} = F _ {B} ^ {N - 1} (v _ {*}) \int_ {\underline {{V}} _ {0}} ^ {\phi (v _ {*})} [ J (v _ {*}) - J _ {0} (v _ {0}) ] d F _ {0} (v _ {0}). \end{array}
$$

This completes the proof. □

Proof of Corollary 1. This follows directly from the fact that $J _ { 0 } ( \nu _ { 0 } ) \equiv \nu _ { 0 } + h ( \nu _ { 0 } ) > \nu _ { 0 } ,$ , for all $\nu _ { 0 } ,$ as in the seller-optimal auction the seller determines whether to withhold the object based on $\nu _ { 0 } . \quad \boxed { }$

Proof of Corollary 2. Let us start with the buyers' side. It can be veri<sup>fi</sup>ed that in the seller-optimal auction, each buyer participates in the auction if and only if her valuation exhibits the cutoff $ { \boldsymbol \nu } _ { * } ^ { s }$ that is the unique solution to:

$$
c _ {B} = F _ {B} ^ {N - 1} \left(v _ {*} ^ {s}\right) \int_ {\underline {{v}} _ {0}} ^ {\phi \left(v _ {*} ^ {s}\right)} \left[ J \left(v _ {*} ^ {s}\right) - v _ {0} \right] d F _ {0} (v _ {0}).\tag{7}
$$

Note that the right-hand side is strictly increasing in v<sup>s</sup>. Compared with Eq. (3), we <sup>fi</sup>nd that if we plug in the cutoff $\nu _ { \ast } ,$ the right-hand side of $\operatorname { E q . } \left( 7 \right)$ would be

$$
F _ {B} ^ {N - 1} (v _ {*}) \int_ {\underline {{V}} _ {0}} ^ {\phi (v _ {*})} [ J (v _ {*}) - J _ {0} (v _ {0}) ] d F _ {0} (v _ {0}) <   F _ {B} ^ {N - 1} (v _ {*}) \int_ {\underline {{V}} _ {0}} ^ {\phi (v _ {*})} [ J (v _ {*}) - v _ {0} ] d F _ {0} (v _ {0}).
$$

Thus, v is higher than $ { \boldsymbol { v } } _ { * } ^ { s }$

Now we switch to the seller's side. In the seller-optimal auction, the participation cutoff $ { \boldsymbol { v } } _ { 0 } ^ { s }$ should be determined by

$$
c _ {S} = \int_ {\psi (v _ {0} ^ {s})} ^ {\overline {{v}}} [ v _ {M} ] N f _ {B} (v _ {M}) F _ {B} ^ {N - 1} (v _ {M}) d v _ {M}.
$$

A similar argument shows that the solution to Eq. (2), v<sup>∗</sup>, should be lower than $ { \boldsymbol { v } } _ { 0 } ^ { s }$ because the right-hand side in the above equation is decreasing in $\nu _ { 0 } ^ { s } . \sqsupset$

Proof of Proposition 2. Observe that from the proof of Proposition 1, there is a notion of revenue equivalence in the following sense. For any given pair of mechanisms that induce the same ex ante participation decisions and ex post allocations, the mediator obtains the same expected payoff. Consequently, all we need to do is to <sup>fi</sup>nd a two-stage mechanism that induces the same participation and allocation rules. In this case, we can simply set the entry fee $T _ { B }$ and the induced reserve price r such that

$$
(v _ {*} - r) F _ {B} ^ {N - 1} (v _ {*}) = c _ {B} + T _ {B},\tag{8}
$$

where $\boldsymbol { v } _ { \ast }$ is the cutoff level that follows from Eq. (3) and $T _ { B }$ is the common entry subsidy that does not depend on the buyers' reports/bids. Note that the left-hand side of $\operatorname { E q . } \left( 8 \right)$ is the expected payoff of a buyer with valuation $\boldsymbol { v } _ { \ast }$ in equilibrium after participating in the auction. To see this, observe that this particular buyer wins if and only if all other N−1 buyers do not participate as their valuations are lower than $\nu _ { * } ;$ this happens with probability $F _ { B } ^ { N - 1 } ( v _ { * } )$ , Furthermore, when she wins, she pays the reserve price r, whereas when she loses she receives a null pavoff ex post, Col lectively, the right-hand side constitutes her expected payoff. Eq. (8) therefore guarantees that this particular buyer is intent to participate, and it is easy to verify that all types above this cutoff will also participate.

Accordingly, we can determine the fees that the mediator charges for the seller. To this end, we shall write down the seller's expected payoff based on the reserve price and the allocation rule. We in the sequel focus on the English auction, which in this case gives rise to the dominant strategy equilibrium for the buyers by revealing their true valuations. Note that this is also the same as the classical second-price sealed-bid auction as in our context they are strategically equivalent. Given that each buyer bids her true valuation in the English auction, we shall set the reserve price at $\psi ( v _ { 0 } )$ such that the object is kept in the seller's hands ex post if and only if the maximum virtual surplus from the buyers (among $\{ J ( v _ { i } ) \} ^ { \prime } s )$ is less than $J _ { 0 } ( \nu _ { 0 } )$

The corresponding seller's expected payoff is then

$$
\left[ v _ {0} ^ {*} + R \big (v _ {0} ^ {*} \big) \right] F _ {B} ^ {N} (\psi (v _ {0})) + N \psi (v _ {0}) [ 1 - F _ {B} (\psi (v _ {0})) ] F _ {B} ^ {N - 1} (\psi (v _ {0})) + \int_ {\psi (v _ {0})} ^ {\overline {{v}}} v [ 1 - F _ {B} (v) ] d F _ {B} ^ {N - 1} (v).\tag{9}
$$

In Eq. (9), the <sup>fi</sup>rst term $\nu _ { 0 } F _ { B } ^ { N } ( \psi ( \nu _ { 0 } ) )$ corresponds to the case in which no buyer participates with probability $F _ { B } ^ { N } ( \psi ( \nu _ { 0 } ) )$ and the seller with holds the object and obtains the valuation $\nu _ { 0 }$ along with the compensation $R ( v _ { 0 } ^ { * } ) .$ . In the second term $N [ 1 - F _ { B } ( \psi ( \nu _ { 0 } ) ) ] F _ { B } ^ { N - 1 } ( \psi ( \nu _ { 0 } ) )$ indicates the probability that exactly one buyer participates and pays the reserve price to the seller; consequently, the seller's net payoff is $\psi ( \nu _ { 0 } )$ . The integral term represents the situation in which more than one buyer participate and the seller collects the second-highest bid. The seller with cutoff val uation v<sup>∗</sup> participates in the mechanism if the following condition holds:

$$
\begin{array}{l} \left[ v _ {0} ^ {*} + R (v _ {0} ^ {*}) \right] F _ {B} ^ {N} (\psi (v _ {0} ^ {*})) + N \psi (v _ {0} ^ {*}) \left[ 1 - F _ {B} (\psi (v _ {0} ^ {*})) \right] F _ {B} ^ {N - 1} (\psi (v _ {0} ^ {*})) \\ \qquad + \int_ {\psi (v _ {0} ^ {*})} ^ {\overline {{v}}} v [ 1 - F _ {B} (v) ] d F _ {B} ^ {N - 1} (v) = c _ {S} + T _ {S} (v _ {0} ^ {*}). \end{array}\tag{10}
$$

Note that in order to induce the seller to choose the appropriate reserve price (which subsequently affects the ex post allocation of the $\mathsf { o b j e c t } )$ , it is essential that the mediator compensates the seller for withholding the object. In other words, $R ( \nu _ { 0 } ^ { * } ) = h ( \nu _ { 0 } ^ { * } ) \equiv \frac { F _ { S } ( \nu _ { 0 } ^ { * } ) } { f _ { S } ( \nu _ { 0 } ^ { * } ) }$ such that the seller makes the reserve price as if her valuation is $\nu _ { 0 } ^ { * } + R ( \nu _ { 0 } ^ { * } ) { = } J _ { 0 } ( \nu _ { 0 } ^ { * } )$ . Given this, the entry fee/subsidy $T _ { S } ( v _ { 0 } ^ { * } )$ in Eq. (10) guarantees that the seller with cutoff valuation v<sup>∗</sup> is willing to participate

Following a similar argument, we can construct the compensation $R ( \nu _ { 0 } ) = h ( \nu _ { 0 } )$ for all $\nu _ { 0 } \leq \nu _ { 0 } ^ { * }$ to induce the appropriate reserve price and design the corresponding entry fee $T _ { S } ( \nu _ { 0 } )$ to ensure incentive compatibility. As this is rather straightforward, we omit the details. For all other standard auctions, we can use similar constructions to induce the same ex ante participation decisions and ex post allocations. Further more, if the mediator is intent to delegate to the seller the reserve price decision, he should compensate the seller in such a way that the per ceived valuation becomes $J _ { 0 } ( \nu _ { 0 } )$ . □

Proof of Proposition 3. As the proof procedure is similar to that for Proposition 1, we only highlight the differences in the following.

In deriving the relaxed problem, apparently the buyers' incentive compatibility constraints are unaltered and therefore we obtain the following integral form:

$$
U _ {i} (v _ {i}) = U _ {i} (v) + \int_ {\underline {{v}}} ^ {v i} \mathbb {E} _ {\mathbf {v} _ {- i}} \left\{\rho_ {i} (u, \mathbf {v} _ {- i}) Q _ {i} (u, \mathbf {v} _ {- i}) \right\} d u,
$$

where we de<sup>fi</sup>ne $U _ { i } ( \nu _ { i } ) \equiv U _ { i } ( \nu _ { i } ; \nu _ { i } )$ . Nevertheless, the seller's incentive compatibility constraint changes. Speci<sup>fi</sup>cally, if we de<sup>fi</sup>ne $\mathcal { U } _ { 0 } ( \nu _ { 0 } ; \hat { \nu } _ { 0 } ) \equiv$ $U _ { 0 } ( \nu _ { 0 } ; \hat { \nu } _ { 0 } ) - \nu _ { 0 }$ and $\mathcal { U } _ { 0 } ( \nu _ { 0 } ) \equiv \mathcal { U } _ { 0 } ( \nu _ { 0 } ; \nu _ { 0 } )$ , the envelope theorem gives rise to the following equations:

$$
\begin{array}{l} \frac {d}{d v _ {0}} \mathcal {U} _ {0} (v _ {0}) = \frac {\partial}{\partial v _ {0}} \mathcal {U} _ {0} (v _ {0}; \hat {v} _ {0}) | _ {\hat {V} _ {0} = v _ {0}} = - 1 - \rho_ {0} (\mathbf {v}) c _ {S} ^ {\prime} (v _ {0}) - \mathbb {E} _ {\mathbf {v} _ {- 0}} \{\rho_ {0} (\mathbf {v}) [ 1 - Q _ {0} (\mathbf {v}) ] \} \leq 0, \\ \Rightarrow \mathcal {U} _ {0} (v _ {0}) = \mathcal {U} _ {0} (\bar {v} _ {0}) + \int_ {\overline {{v _ {0}}}} ^ {\overline {{v _ {0}}}} \Big [ 1 + \rho_ {0} (u, \mathbf {v} _ {- 0}) c _ {S} ^ {\prime} (u) + \mathbb {E} _ {\mathbf {v} _ {- 0}} \{\rho_ {0} (u, \mathbf {v} _ {- 0}) [ 1 - Q _ {0} (u, \mathbf {v} _ {- 0}) ] \} \Big ] d u. \end{array}
$$

Accordingly, the aggregate expected payments can be expressed as

$$
\Pi = \mathbb {E} _ {\mathbf {v}} \left\{ \begin{array}{c} - \rho_ {0} (\mathbf {v}) v _ {0} [ 1 - Q _ {0} (\mathbf {v}) ] - \rho_ {0} (\mathbf {v}) c _ {S} (v _ {0}) - \mathcal {U} _ {0} (\bar {v} _ {0}) \\ - \int_ {v _ {0}} ^ {\overline {{v}} _ {0}} \Big [ 1 + \rho_ {0} (u, \mathbf {v} _ {- 0}) c _ {S} ^ {\prime} (u) + \mathbb {E} _ {\mathbf {v} _ {- 0}} \{\rho_ {0} (u, \mathbf {v} _ {- 0}) [ 1 - Q _ {0} (u, \mathbf {v} _ {- 0}) ] \} \Big ] d u \\ + \sum_ {i = 1, \ldots , N} \big [ \rho_ {i} (\mathbf {v}) v _ {i} Q _ {i} (\mathbf {v}) - \rho_ {i} (\mathbf {v}) c _ {B} - U _ {i} (v) - \int_ {v} ^ {v i} \mathbb {E} _ {\mathbf {v} _ {- i}} \{\rho_ {i} (u, \mathbf {v} _ {- i}) Q _ {i} (u, \mathbf {v} _ {- i}) \} d u \big ] \end{array} \right\}.
$$

As the mediator's objective Π is decreasing in ${ \mathcal { U } } _ { 0 } ( { \bar { \nu } } _ { 0 } )$ and $\{ U _ { i } ( \boldsymbol { y } ) \} ^ { \prime } \boldsymbol { s } ,$ , at optimality ${ \mathcal { U } } _ { 0 } ( { \bar { \nu } } _ { 0 } )$ and $\{ \mathcal { U } _ { i } ( \boldsymbol { x } ) \}$ 's should be zero. Additionally, we can <sup>U</sup>apply integration by parts and rewrite Π as follows:

$$
\begin{array}{l} \Pi = \mathbb {E} _ {\mathbf {v}} \Bigg \{ \begin{array}{c} - (v _ {0} + h (v _ {0})) \rho_ {0} (\mathbf {v}) [ 1 - Q _ {0} (\mathbf {v}) ] + \sum_ {i = 1, \ldots , N} [ \rho_ {i} (\mathbf {v}) Q _ {i} (\mathbf {v}) (v _ {i} - H (v _ {i})) ] \\ - \sum_ {i = 1, \ldots , N} \rho_ {i} (\mathbf {v}) c _ {B} - \rho_ {0} (\mathbf {v}) [ c _ {S} (v _ {0}) + h (v _ {0}) c _ {S} ^ {\prime} (v _ {0}) ] - h (v _ {0}) \end{array} \Bigg \} \\ = \mathbb {E} _ {\mathbf {v}} \Bigg \{\sum_ {i = 0, \ldots , N} J _ {i} (v _ {i}) \rho_ {i} (\mathbf {v}) Q _ {i} (\mathbf {v}) - \rho_ {0} (\mathbf {v}) [ c _ {S} (v _ {0}) + c _ {S} ^ {\prime} (v _ {0}) h (v _ {0}) + J _ {0} (v _ {0}) ] - h (v _ {0}) - \sum_ {i = 1, \ldots , N} \rho_ {i} (\mathbf {v}) c _ {B} \Bigg \}, \end{array}
$$

where we recall the de<sup>fi</sup>nitions of $h ( \nu _ { 0 } ) , H ( \nu ) , J _ { 0 } ( \nu _ { 0 } ) \equiv \nu _ { 0 } + h ( \nu _ { 0 } )$ , and $J _ { i } ( \nu _ { i } ) \equiv \nu _ { i } - H ( \nu _ { i } )$ . From here we observe that the pointwise maximization solution is unaltered:

$$
\rho_ {i} (\mathbf {v}) Q _ {i} (\mathbf {v}) = \left\{ \begin{array}{c c} \rho_ {0} (\mathbf {v}), & \text { if } J _ {i} (v _ {i}) = \max _ {j = 0, \ldots , N} \bigl \{J _ {j} \Bigl (v _ {j} \Bigr) \bigr \}, \\ 0, & \text { otherwise }. \end{array} \right.
$$

Ties are broken arbitrarily. Accordingly, the mediator's expected payoff becomes:

$$
\Pi = \mathbb {E} _ {\mathbf {v}} \Bigg \{\rho_ {0} (\mathbf {v}) \max _ {i = 0, \dots , N} \{J _ {i} (v _ {i}) \} - \rho_ {0} (\mathbf {v}) [ c _ {S} (v _ {0}) + c _ {S} ^ {\prime} (v _ {0}) h (v _ {0}) + J _ {0} (v _ {0}) ] - \sum_ {i = 1, \dots , N} \rho_ {i} (\mathbf {v}) c _ {B} - h (v _ {0}) \Bigg \}.
$$

This immediately leads us to the cutoff structure identi<sup>fi</sup>ed in Proposition 1.

We can then follow exactly the same procedure to characterize the optimal cutoff levels v<sup>∗</sup> and v . To this end, we recall the notation $\nu _ { M } \equiv \mathrm { m a x } _ { i = 1 , \dots , N } \nu _ { i } , \ G ( \nu _ { M } ) = F _ { B } ^ { N } ( \nu _ { M } )$ , and $\mathtt { m a x } _ { i = 0 , \dots , N } \{ J _ { i } ( \nu _ { i } ) \} = \operatorname* { m a x } \{ J _ { 0 } ( \nu _ { 0 } ) , J ( \nu _ { M } ) \}$ . With this change of expressions, we can rewrite the mediator's expected payoff as follows:

$$
\begin{array}{l} \Pi = \int_ {\underline {{V}} _ {0}} ^ {v _ {0} ^ {*}} \int_ {v _ {*}} ^ {\overline {{v}}} [ \max \{J _ {0} (v _ {0}), J (v _ {M}) \} - J _ {0} (v _ {0}) ] d G (v _ {M}) d F _ {0} (v _ {0}) \\ \qquad - \int_ {\underline {{V}} _ {0}} ^ {v _ {0} ^ {*}} [ c _ {S} (v _ {0}) + c _ {S} ^ {\prime} (v _ {0}) h (v _ {0}) ] d F _ {0} (v _ {0}) - \mathbb {E} h (v _ {0}) - N c _ {B} [ 1 - F _ {B} (v _ {*}) ]. \end{array}
$$

As max $\{ J _ { 0 } ( \nu _ { 0 } ) , J ( \nu _ { M } ) \} = J ( \nu _ { M } )$ if and only if $\nu _ { M } 2 \psi ( \nu _ { 0 } )$ , we can rewrite the above equation as

$$
\begin{array}{l} \Pi = \int_ {\underline {{v}} _ {0}} ^ {v _ {0} ^ {*}} \int_ {\psi (v _ {0}) ^ {v}} [ J (v _ {M}) - J _ {0} (v _ {0}) ] d G (v _ {M}) d F _ {0} (v _ {0}) \\ \qquad - \int_ {\underline {{v}} _ {0}} ^ {v _ {0} ^ {*}} [ c _ {S} (v _ {0}) + c _ {S} ^ {\prime} (v _ {0}) h (v _ {0}) ] d F _ {0} (v _ {0}) - \mathbb {E} h (v _ {0}) - N c _ {B} [ 1 - F _ {B} (v _ {*}) ]. \end{array}
$$

<sup></sup>Differentiating the above equation with respect to v<sup>∗</sup>, we obtain the following <sup>fi</sup>rst-order condition:

$$
c _ {S} \left(v _ {0} ^ {*}\right) + c _ {S} ^ {\prime} \left(v _ {0} ^ {*}\right) h \left(v _ {0} ^ {*}\right) = \int_ {\psi \left(v _ {0} ^ {*}\right)} ^ {\overline {{v}}} \left[ J \left(v _ {M}\right) - J _ {0} \left(v _ {0} ^ {*}\right) \right] N f _ {B} \left(v _ {M}\right) F _ {B} ^ {N - 1} \left(v _ {M}\right) d v _ {M}.
$$

Likewise, we can also rewrite the mediator's function and characterize the optimal cutoff v by rewriting Π as follows:

$$
\Pi = \int_ {v _ {*}} ^ {\overline {{v}}} \int_ {\underline {{v}} _ {0}} ^ {\phi (v _ {M})} [ J (v _ {M}) - J _ {0} (v _ {0}) ] d F _ {0} (v _ {0}) d G (v _ {M}) - \int_ {\underline {{v}} _ {0}} ^ {v _ {0} ^ {*}} \Big [ c _ {S} (v _ {0}) + c _ {S} ^ {'} (v _ {0}) h (v _ {0}) \Big ] d F _ {0} (v _ {0}) - N c _ {B} [ 1 - F _ {B} (v _ {*}) ].
$$

This leads to the same <sup>fi</sup>rst-order condition with respect to $\nu _ { * } \colon$

$$
c _ {B} = F _ {B} ^ {N - 1} (v _ {*}) \int_ {\underline {{V}} _ {0}} ^ {\phi (v _ {*})} [ J (v _ {*}) - J _ {0} (v _ {0}) ] d F _ {0} (v _ {0}).
$$

□

Proof of Corollary 3. This follows immediately from Eq. (4), as the right-hand side of is decreasing in $\nu _ { 0 } ^ { t } , \square$

Proof of Proposition 4. As the proof procedure is similar to that for Proposition 1, we only highlight the differences in the following.

In deriving the relaxed problem, apparently the buyers' incentive compatibility constraints are unaltered and therefore we obtain the following integral form:

$$
U _ {i} (v _ {i}) = U _ {i} (\nu) + \int_ {\underline {{\nu}}} ^ {\nu i} \mathbb {E} _ {\mathbf {v} _ {- i}} \{\rho_ {i} (u, \mathbf {v} _ {- i}) Q _ {i} (u, \mathbf {v} _ {- i}) \} d u,
$$

where we de<sup>fi</sup>ne $U _ { i } ( \nu _ { i } ) \equiv U _ { i } ( \nu _ { i } ; \nu _ { i } )$ . Nevertheless, the seller's incentive compatibility constraint changes. Speci<sup>fi</sup>cally, if we de<sup>fi</sup>ne $\mathcal { U } _ { 0 } ( \nu _ { 0 } ; \hat { \nu } _ { 0 } ) \equiv$ $U _ { 0 } ( \nu _ { 0 } ; \hat { \nu } _ { 0 } ) – K \nu _ { 0 }$ and $\mathcal { U } _ { 0 } ( \nu _ { 0 } ) \equiv \mathcal { U } _ { 0 } ( \nu _ { 0 } ; \nu _ { 0 } )$ , the envelope theorem gives rise to the following equations:

$$
\mathcal {U} _ {0} (v _ {0}) = \mathcal {U} _ {0} (\bar {v} _ {0}) + \int_ {v _ {0}} ^ {\overline {{V}} _ {0}} \left[ K + \mathbb {E} _ {\mathbf {v} _ {- 0}} \{\rho_ {0} (u, \mathbf {v} _ {- 0}) [ K - Q _ {0} (u, \mathbf {v} _ {- 0}) ] \} \right] d u.
$$

Accordingly, the aggregate expected payments can be expressed as

$$
\Pi = \mathbb {E} _ {\mathbf {v}} \left\{ \begin{array}{c} - \rho_ {0} (\mathbf {v}) v _ {0} [ K - Q _ {0} (\mathbf {v}) ] - \rho_ {0} (\mathbf {v}) c _ {S} - \mathcal {U} _ {0} (\bar {v} _ {0}) - \int_ {v _ {0}} ^ {\overline {{V}} _ {0}} \Big [ K + \mathbb {E} _ {\mathbf {v} _ {- 0}} \{\rho_ {0} (u, \mathbf {v} _ {- 0}) [ K - Q _ {0} (u, \mathbf {v} _ {- 0}) ] \} \Big ] d u \\ + \sum_ {i = 1, \ldots , N} \Big [ \rho_ {i} (\mathbf {v}) v _ {i} Q _ {i} (\mathbf {v}) - \rho_ {i} (\mathbf {v}) c _ {B} - U _ {i} (\underline {{v}}) - \int_ {\underline {{v}}} ^ {\underline {{v}} _ {i}} \mathbb {E} _ {\mathbf {v} _ {- i}} \{\rho_ {i} (u, \mathbf {v} _ {- i}) Q _ {i} (u, \mathbf {v} _ {- i}) \} d u \Big ] \end{array} \right\}.
$$

As the mediator's objective Π is decreasing in $\mathcal { U } ( \bar { \boldsymbol { v } } _ { 0 } )$ and $\{ U _ { i } ( \boldsymbol { y } ) \} ^ { \prime } \boldsymbol { s } ,$ at optimality ${ \mathcal { U } } _ { 0 } ( { \bar { \nu } } _ { 0 } )$ and $\{ U _ { i } ( \boldsymbol { x } ) \} ;$ s should be zero. Additionally, we can <sup>U</sup>apply integration by parts and rewrite Π as follows:

$$
\Pi = \mathbb {E} _ {\mathbf {v}} \Bigg \{\sum_ {i = 0, \dots , N} J _ {i} (v _ {i}) \rho_ {i} (\mathbf {v}) Q _ {i} (\mathbf {v}) - \rho_ {0} (\mathbf {v}) [ c _ {S} + K J _ {0} (v _ {0}) ] - K h (v _ {0}) - \sum_ {i = 1, \dots , N} \rho_ {i} (\mathbf {v}) c _ {B} \Bigg \}.
$$

From here we observe that the pointwise maximization solution is unaltered:

$$
\rho_ {i} (\mathbf {v}) Q _ {i} (\mathbf {v}) = \left\{ \begin{array}{c c} \rho_ {0} (\mathbf {v}), & \text { if } J _ {i} (v _ {i}) \text { isamongthe } K \text { highestvaluesof } \{J _ {l} (v _ {l}) \} ^ {\prime} \text { s }, \\ 0, & \text { otherwise }. \end{array} \right.
$$

Ties are broken arbitrarily. This immediately leads us to the cutoff structure identi<sup>fi</sup>ed in Proposition 1.

We can then follow exactly the same procedure to characterize the optimal cutoff levels v<sub>0</sub><sup>∗</sup> and $\nu _ { * } .$ . To this end, we recall the order statistic $V _ { 1 } \equiv \mathrm { m a x } _ { i = 1 , \dots , N } \nu _ { i } , V _ { 2 } \equiv \mathrm { m a x } _ { i = 1 , \dots , N } \{ \nu _ { i } | \nu _ { i } < V _ { 1 } \}$ as the second highest valuation, and so on for $V _ { i } , i { = } 3 , . . . , N .$ . With this change of expressions, we can rewrite the mediator's expected payoff as follows:

$$
\begin{array}{l} \Pi = \int_ {v _ {0}} ^ {v _ {0} ^ {*}} \left\{ \begin{array}{c} \int_ {\psi (v _ {0})} ^ {\overline {{v}}} \int_ {v _ {*}} ^ {\psi (v _ {0})} \int_ {v _ {*} ^ {*}} ^ {V _ {2}} \dots \int_ {v _ {*} ^ {*}} ^ {V _ {K - 1}} [ J (V _ {1}) - J _ {0} (v _ {0}) ] d G ^ {K} (\mathbf {v}) \\ + \int_ {\psi (v _ {0})} ^ {\overline {{v}}} \int_ {\psi (v _ {0})} ^ {V _ {1}} \int_ {v _ {*}} ^ {\psi (v _ {0})} \int_ {v _ {*} ^ {*}} ^ {V _ {2}} \dots \int_ {v _ {*} ^ {*}} ^ {V _ {K - 1}} [ J (V _ {1}) + J (V _ {2}) - 2 J _ {0} (v _ {0}) ] d G ^ {K} (\mathbf {v}) \\ + \dots \\ + \int_ {\psi (v _ {0})} ^ {\overline {{v}}} \dots \int_ {\psi (v _ {0})} ^ {V _ {n - 1}} \int_ {v _ {*}} ^ {\psi (v _ {0})} \int_ {v _ {*} ^ {*}} ^ {V _ {n}} \dots \int_ {v _ {*} ^ {*}} ^ {V _ {K - 1}} \left[ \sum_ {i = 1, \ldots , n} J (V _ {i}) - n J _ {0} (v _ {0}) \right] d G ^ {K} (\mathbf {v}) \\ + \dots \\ + \int_ {\psi (v _ {0})} ^ {\overline {{v}}} \dots \int_ {\psi (v _ {0})} ^ {V _ {K - 1}} \left[ \sum_ {i = 1, \ldots , K} J (V _ {i}) - K J _ {0} (v _ {0}) \right] d G ^ {K} (\mathbf {v}) \\ \end{array} \right\} d F _ {0} (v _ {0}) \\ - c _ {S} F _ {S} (v _ {0} ^ {*}) - K \mathbb {E} h (v _ {0}) - N c _ {B} [ 1 - F _ {B} (v _ {*}) ], \end{array}
$$

where in the <sup>fi</sup>rst integral we specify the detailed allocations for different instances. As an example, in the integral $\int _ { \psi ( \nu _ { 0 } ) } ^ { \overline { { \nu } } } \int _ { \nu _ { * } } ^ { \psi ( \nu _ { 0 } ) } \int _ { \nu _ { * } } ^ { V _ { 2 } } \dots$ $\int _ { \boldsymbol { \nu } _ { * } } ^ { V _ { K - 1 } } [ J ( V _ { 1 } ) - J _ { 0 } ( \boldsymbol { \nu } _ { 0 } ) ] d G ^ { K } ( \mathbf { v } )$ , only the maximum valuation among the buyers exceeds $\psi ( \nu _ { 0 } )$ whereas the second order statistics $V _ { 2 }$ is below $\psi ( v _ { 0 } )$ . Consequently, exactly one object is awarded to the buyer with the maximum valuation. In the second integral, the highest two valuations exceed $\psi ( v _ { 0 } )$ , and likewise for all other cases. Apparently, the order statistics after $K + 1$ do not matter because they never factor into the integrands.

Differentiating the above equation with respect to v<sub>0</sub><sup>∗</sup>, we obtain the following <sup>fi</sup>rst-order condition:

$$
\begin{array}{l} c _ {S} = \int_ {\psi (v _ {0} ^ {*})} ^ {\overline {{v}}} \int_ {v _ {*}} ^ {\psi (v _ {0} ^ {*})} \int_ {v _ {*} ^ {*}} ^ {V _ {2}} \ldots \int_ {v _ {*}} ^ {V _ {K - 1}} \left[ J (V _ {1}) - J _ {0} (v _ {0} ^ {*}) \right] d G ^ {K} (\mathbf {v}) + \int_ {\psi (v _ {0} ^ {*})} ^ {\overline {{v}}} \int_ {\psi (v _ {0} ^ {*})} ^ {V _ {1}} \int_ {v _ {*}} ^ {\psi (v _ {0} ^ {*})} \int_ {v _ {*} ^ {*}} ^ {V _ {2}} \ldots \int_ {v _ {*}} ^ {V _ {K - 1}} \left[ J (V _ {1}) + J (V _ {2}) - 2 J _ {0} (v _ {0} ^ {*}) \right] d G ^ {K} (\mathbf {v}) + \ldots \\ \qquad + \int_ {\psi (v _ {0} ^ {*})} ^ {\overline {{v}}} \ldots \int_ {\psi (v _ {0} ^ {*})} ^ {V _ {K - 1}} \left[ \sum_ {i = 1, \ldots , K} J (V _ {i}) - K J _ {0} (v _ {0} ^ {*}) \right] d G ^ {K} (\mathbf {v}). \end{array}\tag{11}
$$

Likewise, we can also rewrite the mediator's function and characterize the optimal cutoff $\nu _ { * } .$ . Speci<sup>fi</sup>cally, we can rewrite Π as

$$
\begin{array}{l} \Pi = \int_ {v _ {*}} ^ {\overline {{v}}} \int_ {v _ {*}} ^ {V _ {1}} \dots \int_ {v _ {*}} ^ {V _ {K - 1}} \left[ \begin{array}{c} \int_ {v _ {0}} ^ {\phi (V _ {K})} \left[ \sum_ {i = 1, \ldots , K} J (V _ {i}) - K J _ {0} (v _ {0}) \right] d F _ {0} (v _ {0}) \\ + \int_ {\phi (V _ {K})} ^ {\phi (V _ {K - 1})} \left[ \sum_ {i = 1, \ldots , K - 1} J (V _ {i}) - (K - 1) J _ {0} (v _ {0}) \right] d F _ {0} (v _ {0}) \\ + \dots \\ + \int_ {\phi (V _ {2})} ^ {\phi (V _ {1})} [ J (V _ {1}) - J _ {0} (v _ {0}) ] d F _ {0} (v _ {0}) \end{array} \right] d G ^ {K} (\mathbf {v}) \\ - c _ {S} F _ {S} (v _ {0} ^ {*}) - K \mathbb {E} h (v _ {0}) - N c _ {B} [ 1 - F _ {B} (v _ {*}) ]. \end{array}
$$

Differentiating the above equation with respect to $\boldsymbol { v } _ { \ast }$ we obtain the following <sup>fi</sup>rst-order condition:

$$
N c _ {B} f _ {B} (v _ {*}) = g _ {K} (v _ {*}) \int_ {v _ {*}} ^ {\overline {{v}}} \int_ {v _ {*}} ^ {V _ {1}} \dots \int_ {v _ {*}} ^ {V _ {K - 2}} \left[ \begin{array}{c} \int_ {v _ {0}} ^ {\phi (v _ {*})} \left[ \sum_ {i = 1, \dots , K - 1} J (V _ {i}) + J (v _ {*}) - K J _ {0} (v _ {0}) \right] d F _ {0} (v _ {0}) \\ + \int_ {\phi (v _ {*})} ^ {\phi (V _ {K - 1})} \left[ \sum_ {i = 1, \dots , K - 1} J (V _ {i}) - (K - 1) J _ {0} (v _ {0}) \right] d F _ {0} (v _ {0}) \\ + \dots \left(F ^ {'} 1 2\right) \\ + \int_ {\phi (V _ {2})} ^ {\phi (V _ {1})} [ J (V _ {1}) - J _ {0} (v _ {0}) ] d F _ {0} (v _ {0}) \end{array} \right] d G ^ {K - 1} (\mathbf {v}),\tag{12}
$$

where we recall that $g _ { K }$ is the density function of the K-th order statistic $V _ { K } .$ The optimal cutoff levels are then jointly determined by solving Eq. (11) and (12). □

Proof of Proposition 5. As the proof procedure is similar to that for Proposition 1, we only highlight the differences in the following. The buyers' incentive compatibility constraints are unaltered and therefore we obtain the following integral form:

$$
U _ {i} ^ {B} (v _ {i}) = U _ {i} ^ {B} (\nu) + \int_ {\underline {{v}}} ^ {v i} \mathbb {E} _ {\mathbf {v} _ {- i}} \Bigl \{\rho_ {i} ^ {B} (u, \mathbf {v} _ {- i}) Q _ {i} ^ {B} (u, \mathbf {v} _ {- i}) \Bigr \} d u.
$$

Regarding the sellers' incentive compatibility constraints, let us de<sup>fi</sup>ne $\mathcal { U } _ { j } ^ { S } \big ( s _ { j } ; \hat { s } _ { j } \big ) \equiv U _ { j } ^ { S } \big ( s _ { j } ; \hat { s } _ { j } \big ) - s _ { j }$ and $\mathcal { U } _ { j } ^ { S } ( s _ { j } ) \equiv \mathcal { U } _ { j } ^ { S } ( s _ { j } ; s _ { j } )$ . Thus, the envelope theorem implies that:

$$
\mathcal {U} _ {j} ^ {S} (s _ {j}) = \mathcal {U} _ {j} ^ {S} (\bar {s}) + \int_ {s _ {j} ^ {- s}} \left[ 1 + \mathbb {E} _ {\mathbf {s} _ {- j}} \left\{\rho_ {j} ^ {S} (u, \mathbf {s} _ {- j}) [ 1 - Q _ {j} ^ {S} (u, \mathbf {s} _ {- j}) ] \right\} \right] d u.
$$

Accordingly, the aggregate expected payments can be expressed as

$$
\Pi = \mathbb {E} _ {\mathbf {s}, \mathbf {v}} \left\{ \begin{array}{c} \sum_ {j} \left[ \begin{array}{c} - \rho_ {j} ^ {S} (\mathbf {s}, \mathbf {v}) s _ {j} \Big [ 1 - Q _ {j} ^ {S} (\mathbf {s}, \mathbf {v}) \Big ] - \rho_ {j} ^ {S} (\mathbf {s}, \mathbf {v}) c _ {S} - \mathcal {U} _ {j} ^ {S} (\overline {{s}}) \\ - \int_ {s _ {j} ^ {s}} \Big [ 1 + \mathbb {E} _ {\mathbf {s} _ {- j}} \Big \{\rho_ {j} ^ {S} (u, \mathbf {s} _ {- j}) \Big [ 1 - Q _ {j} ^ {S} (u, \mathbf {s} _ {- j}) \Big ] \Big \} \Big ] d u \end{array} \right] \\ + \sum_ {i} \Big [ \rho_ {i} ^ {B} (\mathbf {s}, \mathbf {v}) v _ {i} Q _ {i} ^ {B} (\mathbf {s}, \mathbf {v}) - \rho_ {i} ^ {B} (\mathbf {s}, \mathbf {v}) c _ {B} - U _ {i} ^ {B} (\underline {{v}}) - \int_ {v} ^ {v _ {i}} \mathbb {E} _ {\mathbf {v} _ {- i}} \Big \{\rho_ {i} ^ {B} (u, \mathbf {v} _ {- i}) Q _ {i} ^ {B} (u, \mathbf {v} _ {- i}) \Big \} d u \Big ] \end{array} \right\},
$$

which implies that at optimality $\{ \mathcal { U } _ { j } ^ { S } ( \bar { s } ) \} ^ { \prime } s$ and $\left\{ U _ { i } ^ { B } ( \underline { { \nu } } ) \right\} \ Y \mathsf { s }$ should be zero. Applying integration by parts, we can rewrite Π as follows:

$$
\Pi = \mathbb {E} _ {\mathbf {s}, \mathbf {v}} \left\{ \begin{array}{c} - \sum_ {j = 1, \ldots , M} \Big (s _ {j} + h \Big (s _ {j} \Big) \Big) \rho_ {j} ^ {S} (\mathbf {s}, \mathbf {v}) \Big [ 1 - Q _ {j} ^ {S} (\mathbf {s}, \mathbf {v}) \Big ] + \sum_ {i = 1, \ldots , N} \Big [ \rho_ {i} ^ {B} (\mathbf {s}, \mathbf {v}) Q _ {i} ^ {B} (\mathbf {s}, \mathbf {v}) (v _ {i} - H (v _ {i})) \Big ] \\ - \sum_ {j = 1, \ldots , M} \rho_ {j} ^ {S} (\mathbf {s}, \mathbf {v}) c _ {S} - \sum_ {i = 1, \ldots , N} \rho_ {i} ^ {B} (\mathbf {s}, \mathbf {v}) c _ {B} - \sum_ {j = 1, \ldots , M} h \Big (s _ {j} \Big) \end{array} \right\}.
$$

Recalling that ${ \cal J } _ { S } ( s _ { j } ) \equiv s _ { j } + h ( s _ { j } )$ and $J _ { B } ( \nu _ { i } ) \equiv \nu _ { i } - H ( \nu _ { i } )$ , the above expression can be rewritten as

$$
\Pi = \mathbb {E} _ {\mathbf {s}, \mathbf {v}} \left\{ \begin{array}{c} \sum_ {j = 1, \ldots , M} J _ {S} (s _ {j}) \rho_ {j} ^ {S} (\mathbf {s}, \mathbf {v}) Q _ {j} ^ {S} (\mathbf {s}, \mathbf {v}) + \sum_ {i = 1, \ldots , N} J _ {B} (v _ {i}) \rho_ {i} ^ {B} (\mathbf {s}, \mathbf {v}) Q _ {i} ^ {B} (\mathbf {s}, \mathbf {v}) \\ - \sum_ {j = 1, \ldots , M} \rho_ {j} ^ {S} (\mathbf {s}, \mathbf {v}) [ c _ {S} + J _ {S} (s _ {j}) ] - \sum_ {i = 1, \ldots , N} \rho_ {i} ^ {B} (\mathbf {s}, \mathbf {v}) c _ {B} - \sum_ {j = 1, \ldots , M} (s _ {j} + h (s _ {j})) \end{array} \right\}.
$$

The above expression thus gives rise to a clear pecking order in terms of $\{ J _ { S } ( s _ { j } ) \} ^ { \prime } s$ and $\{ J _ { B } ( \nu _ { i } ) \} \mathrm { s }$ . Furthermore, from the monotonicity of $\{ J _ { S } ( s _ { j } ) \} _ { S }$ and $\{ J _ { B } ( \nu _ { i } ) \} \mathrm { s }$ ensured by Assumption 1, we observe that the cutoff structure is preserved in equilibrium when there are multiple sellers. Speci<sup>fi</sup>cally, we can then specify two cutoffs s<sup>∗</sup> and v such that a seller participates if and only if her valuation is below s<sup>∗</sup>, and a buyer participates if and only if her valuation is above $\nu _ { * } .$ , Given the above participation strategies and the allocation rules. the global incentive compatibility constraints are satis<sup>fi</sup>ed automatically as they preserve monotonicity. We can also pin down the optimal cutoffs $s ^ { * }$ and v via straightforward derivations. Nevertheless, the algebra is tedious. □

## References

[1] I. Ashlagi, D. Monderer, M. Tennenholtz, Mediators in position auctions, Games and Economic Behavior 67 (1) (2009) 2–21.

[2] P. Bajari, A. Hortacsu, Winner's curse, reserve prices and endogenous entry: empirical insights from eBay, The RAND Journal of Economics 34 (2) (2003) 329-355

[3] G. Cai, Y.-J. Chen, X. Gong, Design of online auctions: proxy versus non-proxy settings, Decision Support Systems 52 (2) (2012) 384–394.

[4] R. Caldentey, G. Vulcano, Online auction and list price revenue management, Management Science 53 (5) (2007) 795–813.

[5] G. Celik, O. Yilankaya, Optimal auctions with simultaneous and costly participation, The B. E. Journal of Theoretical Economics 9 (1) (2009).

[6] J. Chen, J. Feng, A. Whinston, Keyword auctions, unit-price contracts, and the role of commitment, Production and Operations Management 19 (3) (2010) 305–321.

[7] R. Engelbrecht-Wiggans, On optimal reservation prices in auctions, Management Science 33 (6) (1987) 763–770.

[8] J. Feng, Z. Shen, R. Zhan, Ranked items auctions and online advertisement, Production and Operations Management 16 (4) (2007) 510–522.

[9] A. Ghosh, P. McAfee, K. Papineni, Vassilvitskii, Bidding for representative allocations for display advertising, in: Proceedings of the 4th international Workshop on Internet and Network Economics, WINE, 2009.

[10] Z. Hidvegi, W. Wang, A.B. Whinston, Buy-price English auction, Journal of Economic Theory 129 (1) (2006) 31–56.

[11] K.-W. Huang, A. Sundararajan, Pricing digital goods: discontinuous costs and shared infrastructure, Information Systems Research 22 (4) (2011) 721–738.

[12] P. Klemperer, What really matters in auction design, The Journal of Economic Perspectives 16 (1) (2002) 169–189

[13] P. Klemperer, Auctions: Theory and Practice, Princeton University Press, USA, 2004.

[14] V. Krishna, Auction Theory, Academic Press: Elsevier Science, 2002.

[15] J. Laffont, D. Martimort, The Theory of Incentives: The Principal–Agent Model, Princeton University Press, USA, 2002.

[16] D. Levin, J. Smith, Equilibrium in auctions with entry, The American Economic Review 84 (3) (1994) 585–599.

[17] D. Liu, J. Chen, Designing online auctions with past performance information, Decision Support Systems 42 (3) (2006) 1307–1320.

[18] D. Liu, J. Chen, A. Whinston, Ex ante information and the design of keyword auctions, Information Systems Research 21 (1) (2010) 133–153.

[19] J. Lu, Auction design with opportunity cost, Economic Theory 38 (1) (2009) 73–103.

[20] M. Mahdian, H. Nazerzadeh, A. Saberi, Allocating online advertisement space with unreliable estimates, in: Proceedings of the 8th ACM conference on Electronic commerce. ACM.2007 pp. 294-301.

[21] E. Maskin, J. Riley, Optimal multi-unit auctions, in: Frank Hahn (Ed.), The Economics of Missing Markets, Information, and Games, Oxford University Press, Oxford 1989 pp. 312-335

[22] A. Matros, A. Zapechelnyuk, Optimal fees in internet auctions, Review of Economic Design 12 (3) (2008) 155–163.

[23] R. McAfee, J. McMillan, Auctions with entry, Economics Letters 23 (4) (1987) 343–347.

[24] P. McAfee, K. Papineni, S. Vassilvitskii, Maximally representative allocations for guaranteed delivery advertising campaigns, in: Working paper, Yahoo! Research, 2010.

[25] F. Menezes, P. Monteiro, Auctions with endogenous participation, Review of Economic Design 5 (1) (2000) 71–89.

[26] M. Mussa, S. Rosen, Monopoly and product quality, Journal of Economic Theory 18 (2) (1978) 301–317.

[27] R. Myerson, Optimal auction design, Mathematics of Operations Research 6 (1) (1981) 58–73.

[28] R. Myerson, M. Satterthwaite, Ef<sup>fi</sup>cient mechanisms for bilateral trading, Journal of Economic Theory 29 (2) (1983) 265–281.

[29] M. Stegeman, Participation costs and ef<sup>fi</sup>cient auctions, Journal of Economic Theory 71 (1) (1996) 228–259.

[30] G. Tan, Entry and R & D in procurement contracting, Journal of Economic Theory 58 (1) (1992) 41–60

[31] J. Tirole, Cognition and incomplete contracts, The American Economic Review 99 (1) (2009) 265–294.

Ying-Ju Chen joined the Department of Industrial Engineering and Operations Research at UC Berkeley in July 2007 after completing his PhD in Operations Management in the IOMS Department, Leonard N. Stern School of Business, New York University. He also holds master's and bachelor's degrees of Electrical Engineering from National Taiwan University. He is a recipient of NYU teaching excellence award, Second place of INFORMS Junior Faculty Interest Group (JFIG) paper competition, the Harold MacDowell Award from Stern School, Meritorious Service Awards from Management Science and Manufacturing & Service Operations Management, and other awards and fellowships during his academic journey. His current research interests lie in operations-marketing interface, auctions, supply chain management, and competitive strategies. His work has appeared in several leading conferences and journals in the <sup>fi</sup>elds of accounting, economics, information systems, marketing, and operations research.

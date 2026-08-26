---
otero_id: 12740
otero_key: "YQ77YSQF"
title: "Bidding behaviors for a keyword auction in a sealed-bid environment"
authors: "Y. Kamijo"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.07.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Y. Kamijo

Kochi University of Technology, Department of Management, 185 Miyanokuchi, Tosayamada-Cho, Kami-Shi, Kochi 782-8502, Japan

## a r t i c l e i n f o

Article history: Received 23 March 2012 Received in revised form 27 May 2013 Accepted 8 July 2013 Available online 17 July 2013

JEL classification: C72 C91 D44

Keywords: Internet advertisements Keyword auction Sealed-bid environment Dynamic game of incomplete information

## a b s t r a c t

A keyword auction is conducted by Internet search engines to sell advertising slots listed on the search results page. Although much of the literature assumes the dynamic bidding strategy that utilizes the current bids of other advertisers, such information is, in practice, not available for participants in the auction. This paper explores the bidding behavior of advertisers in a sealed-bid environment, where each bidder does not know the current bids of others. This study considers secure bidding with a trial bid (SBT) as the bid adjustment process used by the advertisers, which is functional in a sealed-bid environment. It is shown that the SBT bid adjustment process converges to some equilibrium point in a one-shot game irrespective of the initial bid pro<sup>fi</sup>le. Simulation results verify that a sealed-bid environment would be bene<sup>fi</sup>cial to search engines.

© 2013 The Author. Published by Elsevier B.V. All rights reserved.

## 1. Introduction

Internet advertisements called sponsored links, which are shown along with search results for a keyword or combination of keywords, are sold through keyword auctions. Each time a user enters a search term into a search engine such as Google, Yahoo! or Bing, an auction is run, and advertisement positions and advertisement fees are determined based on the auction result. Over a million keyword auctions are conducted each day all over the world, and Internet advertisements from keyword auctions are a principal source of revenue for search engines.

The generalized second-price (GSP) auction and the auction mechanisms based on it are most widely used for selling advertisements on Internet search engines. In the GSP, based on the bids submitted by advertisers, ad slots are allocated according to the descending order of the bids, that is, the top position is allocated to the bidder with the highest bid, the second-ranked position is allocated to the bidder with the second-highest bid, and so on. Every time a search engine user clicks the advertisement, the advertiser pays the bidding price of the advertiser one position lower. Thus, this is a second-price auction for selling multiple objects with a one-dimensional strategy space.

Since the payment of each advertiser does not depend on his bid, but on the bid submitted by the advertiser one position lower than his, the GSP auction is similar to the Vickrey auction selling one object [25]. In fact, when there is only one ad slot, the GSP auction is equivalent to the Vickrey auction and thus, it has the following property: submitting the true expected revenue from the sponsored link is a dominant strategy for each advertiser.

However, when there are multiple ad slots, the GSP auction does not retain the truth-telling property [9]. This indicates that advertisers participating in the GSP auction have no option but to undertake the complicated task of choosing their bids.

Edelman and Ostrovsky [8] reported that bids observed in GSP auctions <sup>fl</sup>uctuate widely, and proposed that this could be caused by the bidders' strategic behavior.

In this paper, I explore bidding behavior for a hypothetical keyword auction. As explained in the previous paragraph, the bids submitted by advertisers vary over a given period. This suggests that we should pay attention to the dynamic aspect of bidding behavior. After describing the bidding behavior of the advertisers in a keyword auction, I examine whether a stable bid pro<sup>fi</sup>le exists for the bidding behavior. In the event that it is stable, I investigate the property that the stable bid pro<sup>fi</sup>le possesses. I also explore how long it takes to realize the stable bid pro<sup>fi</sup>le.

My analysis considers a simpli<sup>fi</sup>ed model of keyword auctions.<sup>1</sup> I assume that the click-through rates (CTRs) of ad slots are common knowledge. In each period, an advertiser can change his bid according to the result of the keyword auction played in a previous period. The information available to the advertiser is limited to his revenue, his payment to a search engine, and the manner in which ad slots were assigned to advertisers in a previous period. The advertiser does not know the actual bids of the other advertisers. This means that advertisers cannot follow the greedy bidding strategy, where in each period, they update their bids to provide the best response to others' bids. Since a keyword auction, in practice, is a sealed-bid second-price auction, advertisers update their bids according to the limited information.

Since 2002, both Google and Yahoo!, the two leading search engines, have used the GSP auction mechanism.<sup>2</sup>

An important difference between the auctions conducted by Yahoo! and Google was that Google employed a sealed-bid auction, while Yahoo!'s auction was an open-bid auction. In Yahoo!'s keyword auction, the current bids of advertisers were publicly provided through the software (the View Bid Tool). However, this service was discontinued in 2007 when Yahoo! switched its allocation rule to mirror Google's quality-based bidding. Thus, currently, keyword auctions managed by the two leading search engines are sealed-bid auctions.<sup>3</sup> Moreover, search engines generally restrict the bidding information available to the automated bidding software and require a review of any automated bidding code [14].

Even though the current keyword auctions are sealed-bid auctions, most studies concerning the bidding strategy for a dynamic auction assume an open-bid environment. Cary et al. [5,6] considered a type of greedy bidding strategy. Since the payment is calculated by a secondpricing rule, there can be multiple best-response bids even though the best ad slot is uniquely determined. In their analysis, among the bestresponse bids, the bidder was assumed to choose one bid so as to balance two objectives: to push the prices paid by the other advertisers higher and to limit the risk that a change in other advertisers' bids could result in the bidder paying a higher price than expected. Thus, this bidding strategy is called balanced bidding. Bu et al. [4] analyzed the same bidding behavior.<sup>4</sup> In addition to the greedy bidding strategy, other bidding strategies such as antisocial bidding have also been analyzed in the literature [3,20,28].

In this paper, a bid adjustment process in a sealed-bid environment is analyzed. While the existing literature provides a good perspective on how bidders change and adjust their bids in a dynamic auction, the analysis of bidding behavior based on a more realistic setting is also encouraged. Even though a sealed-bid environment may be temporary because of the bidders' actual experience in a dynamic auction, the question of how bidders adjust their bids and how bidders learn of other bids is answered only by considering the sealed-bid environment.

First, I consider a conservative bidding strategy called secure bidding. The idea of secure bidding was derived partly from balanced bidding, which was proposed by Cary et al. [5] for the open-bid environment. The bidder who follows secure bidding adjusts his bid, given his revenue, his payment, and his ad slot, and never searches for information about the bids of other advertisers. I show that there exist multiple stable bid pro<sup>fi</sup>les against secure bidding (or the <sup>fi</sup>xed point of bidding behavior according to secure bidding) and that some of them are not an envy-free equilibrium [9,23], a Nash equilibrium, or ef-<sup>fi</sup>cient. This implies that to achieve equilibrium, the searching behavior for other bids should be incorporated.

Next, I consider the bidding behavior based on secure bidding that entails a trial bid in a short period as a partial exploration of the competitor's bid in one higher ad slot. I show that the <sup>fi</sup>xed point of secure bidding with a trial bid (SBT) exists uniquely. Moreover, at the <sup>fi</sup>xed point, the ad slots are ef<sup>fi</sup>ciently assigned to advertisers, the bid pro<sup>fi</sup>le is an envy-free equilibrium, and the revenue of a search engine is the same as that in the truth-telling equilibrium in the Vickrey-Clarke-Groves (VCG) mechanism [25,7,17].

I also examine whether advertisers' bids converge to the stable bid pro<sup>fi</sup>le if they update their bids repeatedly according to SBT. I consider an asynchronous model of bid adjustment, where in each period, one bidder is randomly selected and this bidder changes his bid according to SBT. I show that in the resulting Markov process, convergence occurs with probability one in the sealed-bid repeated keyword auction. This is similar to the observation in an open-bid environment reported by Bu et al. [4] and Cary et al. [5].

I also consider greedy bidding in a sealed-bid environment. Since the bids of others are not revealed to the bidder, he has to search for their bids on his own or through an automated bidding agent. A bidder <sup>fi</sup>nds others' bids randomly, and from among these, he calculates the best ad slots to acquire and submits a secure bid for the ad slot. I show that imperfect greedy bidding converges with probability one to the same <sup>fi</sup>xed point as that in SBT.

Finally, I compare the bidding behavior in a sealed-bid environment with that in an open-bid environment using a computer simulation. I compare the convergence time, search engines' revenues, and advertisers' utilities in the SBT bid adjustment process and the bid adjustment process in the literature. The simulation results suggest that in the sealed-bid environment, the convergence time becomes longer and the average revenue of search engines becomes higher compared to the open bid environments. Thus, the sealed-bid environment can be bene<sup>fi</sup>cial to a search engine. However, advertisers can improve payoffs by switching their bidding behavior from SBT to the greedy bidding strategy even though the search for other advertisers' bids is imperfect.

## 2. A keyword auction

## 2.1. The environment

There are $N , N \geq 2 ,$ advertisers (bidders) participating in a keyword auction. Each advertiser i has an expected revenue v per ad click, called a value, and it is assumed that $\nu _ { 1 } > \nu _ { 2 } > . . . > \nu _ { N } .$ There are K ad slots with CTR $\alpha _ { 1 } \equiv \alpha _ { 2 } \\\equiv \ldots \\\cong \alpha _ { K } ,$ where α is the estimated probability of being clicked, or the estimated number of clicks in a given period for an advertiser in the k-th ad slot. We also set $\alpha _ { k } = 0$ for all $k > K$ and assume $N \geq K . ^ { 5 }$

## 2.2. The generalized second-price auction

Each advertiser submits a bid in the auction. Let b be an advertiser i's bid. I denote the bid pro<sup>fi</sup>le of N advertisers by $\mathbf { b } = ( b _ { 1 } , . . . , b _ { N } )$

In the GSP auction, advertisers are allocated ad slots in descending order of their bids $b _ { 1 } , b _ { 2 } , . . . , b _ { N } .$ Let d(k) denote the bidder who submits the k-th highest bid among b. In the GSP auction, bidder d(k) acquires ad slot k.

The advertiser obtaining the k-th ad slot pays the bid of the advertiser obtaining the next ad slot lower down (i.e., the k + 1-th ad slot) for each click.

Hence, the payment is $\alpha _ { k } b _ { d ( k + 1 ) } .$

To complete the de<sup>fi</sup>nition of the payments, I assume that $b _ { d ( k ) } = 0$ if k N N. Accordingly, when $K = N ,$ the payment of d(K) is assumed to be zero, and for $k > K ,$ bidder d(k) pays $\alpha _ { k } b _ { d ( k + 1 ) } = 0$ (as per the definition of α ).

## 2.3. An envy-free equilibrium

A bid pro<sup>fi</sup>le b (and the corresponding allocation d(.)) is an envyfree equilibrium if the following conditions are satis<sup>fi</sup>ed:

$$
\text {   for   any   } k = 1, 2,..., K, \quad \alpha_ {k} \left(v _ {d (k)} - b _ {d (k + 1)}\right) \geq \alpha_ {k + 1} \left(v _ {d (k)} - b _ {d (k + 2)}\right);\tag{1}
$$

$$
\text { for   any } k = 2, 3,..., K + 1, \quad \alpha_ {k} \left(v _ {d (k)} - b _ {d (k + 1)}\right) \geq \alpha_ {k - 1} \left(v _ {d (k)} - b _ {d (k)}\right); \tag {2}
$$

$$
\text {(if} N > K) \text { for any} k = K + 1,..., N, \quad b _ {d (k)} = v _ {d (k)}.\tag{3}
$$

These conditions require that no bidder is better off by exchanging his position with that of the bidder immediately above (Inequality (2)) or that immediately below (Inequality (1)).

Edelman, Ostrovsky, and Schwarz [9] and Varian [23] showed several properties of an envy-free equilibrium. First, an envy-free equilibrium is a re<sup>fi</sup>nement of the Nash equilibrium. Second, the allocation of ad slots in an envy-free equilibrium is efficient, that is, the bidder with the k-th highest value obtains ad slot k. Third, the set of envy-free equilibria constitutes the lattice, and the set of the utility pro<sup>fi</sup>le in envy-free equilibria also forms the lattice. Fourth, the greatest and the least elements in the lattice are the seller's revenue-maximizing and revenue-minimizing bid pro<sup>fi</sup>les, respectively. Moreover, the explicit formulae of these two bid pro<sup>fi</sup>les are known. The revenue-minimizing bid pro<sup>fi</sup>le b<sup>∗</sup> is obtained as follows:

$$
b _ {k} ^ {*} = \frac {1}{\alpha_ {k - 1}} \sum_ {\ell = k} ^ {K + 1} (\alpha_ {\ell - \ell} - \alpha_ {\ell}) v _ {\ell}\tag{4}
$$

for any $k = 2 , 3 , . . . , K$ and any $b _ { 1 } ^ { * }$ with $b _ { 1 } ^ { * } > b _ { 2 } ^ { * } .$ . The revenuemaximizing bid pro<sup>fi</sup>le $\mathbf { b } ^ { * * }$ is obtained as follows:

$$
b _ {k} ^ {* *} = \frac {1}{\alpha_ {k - 1}} \sum_ {\ell = k} ^ {K + 1} (\alpha_ {\ell - 1} - \alpha_ {\ell}) v _ {\ell - 1}
$$

for any $k = 2 , 3 , . . . , K$ and any b<sup>∗∗</sup> with $b _ { 1 } ^ { * * } > b _ { 2 } ^ { * * }$ . From the de<sup>fi</sup>nition of the envy-free equilibrium, $b _ { k } ^ { * } = b _ { k } ^ { * * } = \nu _ { k }$ for any $k > K ,$

The envy-free equilibrium is used to theoretically or empirically analyze a keyword auction market.<sup>6</sup> Using this concept, Edelman and Schwarz [10] investigated the effect of setting a reserve price on the revenue of the search engine, and showed that the GSP auction with a reserve price is an optimal mechanism. Varian [24] estimated the bene<sup>fi</sup>t to advertisers from Internet advertising in search engines and concluded that the bene<sup>fi</sup>t tends to be two and three times advertising expenditures. Fukuda et al. [13] checked the prediction from envy-free equilibrium on the GSP auction and its alternative using a laboratory experiment. However, there is no existing study that theoretically supports the equilibrium concept for a keyword auction in a sealed-bid environment. This paper is the <sup>fi</sup>rst to investigate this.

## 3. Bidding behavior in the sealed-bid environment

## 3.1. Secure bidding

Let us consider how the advertiser who currently possesses ad slot k adjusts his bid in the next period. An important assumption is that he does not know the bids of any of the other bidders except for advertiser $d ( k + 1 )$ , which can be guessed from his payment. This environment, which appears to closely resemble a real keyword auction, is called the sealed-bid environment. An environment where each bidder knows the current bids of other bidders is called an open-bid environment. Most of the literature has analyzed bid adjustment in an open-bid environment. In this paper, I explore bid adjustment in a sealed-bid environment.

I <sup>fi</sup>rst consider the following conservative bid adjustment of advertisers. The idea is that advertiser i, who currently occupies ad slot k, gradually or sharply increases his bid so as to acquire ad slot $k - 1$ as long as at least the current payoff is guaranteed after obtaining the higher ad slot. Thus, the new bid $b _ { i } ^ { ' }$ has to satisfy the following condition:

$$
\alpha_ {k} \left(v _ {i} - b _ {d (k + 1)}\right) \leq \alpha_ {k - 1} \left(v _ {i} - b _ {i} ^ {\prime}\right).
$$

The left-hand side of the above inequality is the current payoff of advertiser i, and the right-hand side is i's worst payoff after obtaining ad slot k-1 with new bid $b _ { i } ^ { ' }$ . The right-hand side is also interpreted as the payoff of i when i gradually increases his bid and obtains the higher slot at $b _ { i \cdot } ^ { ' }$ Therefore, the bid adjustment of the conservative advertiser is to choose the maximum bid satisfying the condition and this maximum is easily calculated as follows:

$$
b _ {i} ^ {S} \left(k, b _ {d (k + 1)}\right) = \left(1 - r _ {k}\right) v _ {i} + r _ {k} b _ {d (k + 1)},
$$

where $\begin{array} { r } { r _ { k } = \frac { \alpha _ { k } } { \alpha _ { k - 1 } } } \end{array}$ and $r _ { 1 }$ is assumed to be a for some $a < 1 . { } ^ { 7 }$ This bidding is <sup>¼</sup>called secure bidding (SB). I set $r _ { k } = 0$ for all $k > K ,$ meaning that the SB of the advertiser i who does not obtain any ad slot is $b _ { i } ^ { S } ( k , b _ { d ( k + 1 ) } ) = \nu _ { i } .$

There are two remarks on SB. First, it depends only on the identity of the bidder (or the value of the bidder), his current position, and his current payment. Thus, bid adjustment via SB is possible in the sealed-bid environment. Second, this can be interpreted as the weakly dominant strategy conditional on the bidder trying to acquire one higher slot $k - 1$ . Consider a situation where advertiser i changes his bid so as to acquire one higher ad slot $k - 1$ , and ignore (for the moment) advertisers other than i and $d ( k - 1 )$ and slots other than k and $k - 1$ . Let $b _ { d ( k \mathrm { ~ - ~ } 1 ) }$ be the current bid of bidder $d ( k - 1 )$ . Then, $\mathrm { ~ f ~ } b _ { d ( k - 1 ) } \lesseqqgtr b _ { i } ^ { S } ( k _ { * }$ $b _ { d ( k + 1 ) } )$ , any new bid b<sup>′</sup> of bidder i satisfying $b _ { i } ^ { ' } { > } b _ { d ( k - 1 ) }$ is his best response to $b _ { d ( k \mathrm { ~ - ~ } 1 ) } .$ Further, $\mathrm { i f } \ b _ { d ( k - 1 ) } \geq b _ { i } ^ { \varsigma } ( k , b _ { d ( k + 1 ) } ) ,$ <sup>Þ</sup>, any new bid $b _ { \ i } ^ { ' }$ satisfying $b _ { i } ^ { ' } { < } b _ { d ( k - 1 ) }$ becomes his best response to $b _ { d ( k \mathrm { ~ - ~ } 1 ) } .$ Combining <sup>ð Þ</sup>these two observations, $b _ { i } ^ { S } ( k , b _ { d ( k + 1 ) } )$ is always the best response to the bid of the advertiser in ad slot $k - 1$

## 3.2. Limitations of the secure bidding adjustment

A bid pro<sup>fi</sup>le b (and the corresponding allocation $d ( . ) )$ is consistent with SB if for any $k = 1 , 2 , . . . , N , b _ { d ( k ) } = b _ { d ( k ) } ^ { S } ( k , b _ { d ( k + 1 ) } ) . ^ 8$ Since the SB of advertiser i depends only on v , the ad slot acquired by him, and the bid of the advertiser in the one-lower ad slot, we can calculate the bid pro<sup>fi</sup>le consistent with SB given the predetermined allocation $d ( . )$ Therefore, assuming $d ( . )$ is predetermined, calculate the bid pro<sup>fi</sup>le b as follows:

$$
\begin{array}{l} \bullet k > K, b _ {d (k)} = v _ {d (k)}; \\ \bullet \text { repeatedly   apply } b _ {d (k)} = b _ {d (k)} ^ {S} (k, b _ {d (k + 1)}) \text { from } k = K \text { to } k = 1. \end{array}
$$

$\mathrm { I f } b _ { d ( 1 ) } \geq b _ { d ( 2 ) } \geq . . . \geq b _ { d ( N ) }$ holds for the resulting bid pro<sup>fi</sup>le, then this is consistent with SB.

Consistency with SB implies that the bid pro<sup>fi</sup>le is a <sup>fi</sup>xed point of the bid adjustment process in which each advertiser changes his bid via SB in every period. The following proposition indicates that in the <sup>fi</sup>xed point, the advertisers with the top K highest values obtain the ad slots.

Proposition 1. Assume b is consistent with SB. Then, {d(1), d(2),..., $d ( K ) \} = \{ 1 , 2 , . . . , K \} \ /$

The proof of this proposition (and those of others) is obtained from the appendix on this journal's web page.

The intuition of this proposition is as follows. Since the secure bidding of an advertiser is always less than or equal to its value and the equality holds when i does not have an ad slot, the secure bidding of i, $i \leqq K ,$ , when i does not have any ad slot, is always greater the secure bidding $\mathrm { o f } j , j > K .$ . Therefore, if b is consistent with SB, an advertiser $j , j > K ,$ never possesses an ad slot.

Proposition 1 does not mean that ad slots are ef<sup>fi</sup>ciently allocated to advertisers in the <sup>fi</sup>xed point of bid adjustment via SB.

Proposition 2. Consistency with SB does not imply that b is an envy-free equilibrium or a Nash equilibrium, or that b is efficient.

Inef<sup>fi</sup>ciency of the consistent bid pro<sup>fi</sup>le occurs when two advertisers, say i and j with $\nu _ { i } > \nu _ { j } ,$ retain twisted ad slots (e.g., i obtains slot 2 and j obtains slot 1) and the secure bidding of i is smaller than $\nu _ { j } .$ In such a case, the bid pro<sup>fi</sup>le is consistent with SB but j may improve its payoff by reducing its bid in order to obtain ad slot 2.

Proposition 2 indicates that the <sup>fi</sup>xed point of the bid adjustment via SB is not an envy-free equilibrium. This result contradicts previous literature that used the envy-free equilibrium as an analytical tool because it might not be achieved in the sealed-bid environment even though the adjustment process is long enough. In the next section, in which I incorporate a temporal increase in a bid in order to search for the bids of other advertisers, I propose a new bid adjustment process and show that the unique <sup>fi</sup>xed point of the process is an envy-free equilibrium.

## 4. Secure bidding with a trial bid

## 4.1. A trial bid

Even though the bids of others are unknown, each advertiser can obtain some information on the bids of others through the list of advertisements shown on the search results page. Therefore, a partial search for the bids of others is possible in the following manner. First, a bidder increases, as a trial, his bid in order to check whether he acquires a higher ad slot with the new bid. If he does not obtain the higher ad slot, it means that the prices of these slots are too expensive for him, and thus, he changes the bid back to the previous value. On the other hand, if the increased bid gives him a higher ad slot, he will retain the increased bid. Therefore, the purpose of the trial bid is a partial exploration of the bids of the advertisers in the higher ad slots, conducted in a very short period that does not affect the payoff.

I consider the following kinds of trial bids. The trial bid of the advertiser who currently occupies ad slot k is the bid that he would submit if he currently has ad slot $k - 1$ . Here, I consider secure bidding as the basis of the bidding behavior. Therefore, the trial bid of d(k) in ad slot k is

$$
b _ {d (k)} ^ {T} := b _ {d (k)} ^ {S} \left(k - 1, b _ {d (k)}\right),
$$

where $b _ { d ( k ) }$ is the current bid of d(k).

The reasoning for the trial bid de<sup>fi</sup>ned above is as follows. As con-<sup>fi</sup>rmed in the previous section, secure bidding may induce an inef<sup>fi</sup>cient allocation of ad slots as a <sup>fi</sup>xed state. From the standpoint of a bidder (say i), this means that the bidder (say j) who currently occupies the slot above i could be inappropriate in a sense that $j ^ { \prime } s$ value is less than i's one, that is, $v _ { j } < v _ { i }$ holds. So it is natural for i to increase his bid to the level that he would choose if he were currently in $j ^ { \prime } s$ position in order to check whether j is appropriate to occupy the slot; if j is inappropriate $( \mathrm { i } . \mathrm { e } . , \nu _ { j } < \nu _ { i } )$ , i's trial bid can beat j's secure bid, and otherwise, j can preserve his current position against i's challenge. Thus, a trial bid can correct the twisted neighboring bidders (d(k) and $d ( k + 1 )$ with $\nu _ { d ( k ) } < \nu _ { d ( k + 1 ) } )$ to an ef<sup>fi</sup>cient manner. In the next subsection, I show that the <sup>fi</sup>xed point of the bid adjustment based on secure bidding combined with a trial bid is always ef<sup>fi</sup>cient and an envy-free equilibrium.

## 4.2. The fixed point of secure bidding with a trial bid

For an advertiser, secure bidding with trial bid (SBT) is a bid adjustment as follows. Let b be a current bid pro<sup>fi</sup>le and i be an advertiser obtaining ad slot k.

• If i's payoff is negative or $\mathrm { i f } \ k > K ,$ he submits $\nu _ { i }$ and retains it.

• If i's payoff is non-negative and $k \leq K ,$ he <sup>fi</sup>rst submits a trial bid $b _ { d ( k ) } ^ { S } ( k - 1 , b _ { d ( k ) } )$ . Then, if he acquires the higher ad slot, he retains the trial bid. Otherwise, he changes the trial bid to the secure bid $b _ { d ( k ) } ^ { S } ( k , b _ { d ( k + 1 ) } )$ and retains the latter.

One merit of SBT is that the <sup>fi</sup>xed point of the bid adjustment via SBT exists uniquely and is an envy-free equilibrium.

Proposition 3. The bid profile b<sup>∗</sup> defined in Eq. (4) is a unique fixed point of SBT.

As explained in the paragraph immediately following Proposition 2, a bid pro<sup>fi</sup>le consistent with SB becomes inef<sup>fi</sup>cient when two advertisers, say i and j with $\nu _ { i } > \nu _ { j } ,$ retain the twisted ad slots and the secure bidding of i is smaller than $\nu _ { j } .$ . If an advertiser uses only secure bidding, i never beats the bid of j whose value is less than i's value. However, if i uses a trial bid to check whether j's position is adequate or not, i <sup>fi</sup>nds that i itself is more adequate to the higher ad slot and thus beats the bid of j. Thus, the twisted relation disappears. This reasoning implies that the <sup>fi</sup>xed point of SBT should be ef<sup>fi</sup>cient. The ef<sup>fi</sup>ciency of a bid pro-<sup>fi</sup>le together with consistency with SB uniquely determined the bid pro<sup>fi</sup>le.

This proposition means that the <sup>fi</sup>xed point of SBT is an envy-free equilibrium. Moreover, this is the revenue-minimizing (or bidderoptimal) equilibrium among all envy-free equilibria. One important remark is that b<sup>∗</sup> is a <sup>fi</sup>xed point of the bidding behavior analyzed by Cary et al. [5] and Bu et al. [4] for the open-bid environment. Therefore, combining our results with those of the literature indicates that the stable bid pro<sup>fi</sup>le in an open-bid environment should be a unique stable bid pro<sup>fi</sup>le in a sealed-bid environment.

## 4.3. A typical bidding pattern in SBT

The literature on empirical bidding behavior in a keyword auction reports that the bidding war and the cease-<sup>fi</sup>re, that is, the phenomenon where two or more bidders alternately and gradually raise their bids and suddenly drop them when their bids exceed some critical value is frequently observed. Theoretical research has shown that this can be the result of equilibrium bidding behavior [26,27,1]. Although these observations and theoretical results are based on the open-bid environment, the bidding behavior based on SBT shows that this phenomenon can occur even in a sealed-bid environment.

Fig. 1 plots the transition of bids via SBT across 20 periods where there are three advertisers and two ad slots. The values of advertisers 1, 2 and 3 are 100, 95 and 10, respectively, and the CTRs of ad slots 1 and 2 are 100 and 50, respectively. The initial bid pro<sup>fi</sup>le is (20, 45, 10) and advertisers 1 and 2 alternately change their bids via SBT. From this, the bidding war is observed in the <sup>fi</sup>rst half of the entire period (until about period 10). Advertiser 2, who has the second-highest value, drops his bid since his trial bid never exceeds the bid of advertiser 1 for this period. After $b _ { 2 }$ is dropped, advertiser 1 follows suit and drops his bid to a certain level, after which there is no further bid adjustment.

![](/api/attachments/YQ77YSQF/fulltext/images/12ea8b7ed7f0e766c192853bb7003a51f7e6c86be2240e69c991dd85a5b5242c.jpg)  
Fig. 1. Bidding war and cease-<sup>fi</sup>re when bidders use SBT (three bidders and two ad slots)

The bid pro<sup>fi</sup>le in the last half of the entire period is the <sup>fi</sup>xed point b<sup>∗</sup>. This indicates that bid adjustment via SBT can reach the <sup>fi</sup>xed point in a <sup>fi</sup>nite time. This point is analyzed in the next section, and it will be shown that convergence to b<sup>∗</sup> is guaranteed with probability one.

## 5. Convergence of SBT

In this section, I explore whether convergence is attained in a repeatedly played keyword auction. I consider a situation where in each period, one advertiser is randomly selected and changes his bid according to SBT. We call this bid adjustment process asynchronous SBT dynamics. The point of concern is whether this process converges to the <sup>fi</sup>xed point of the bid adjustment via SBT, that is, b<sup>∗</sup>. In asynchronous SBT dynamics, from any initial bid pro<sup>fi</sup>le $\mathbf { b } ^ { 0 } ,$ , the probability distribution over the set of all bid pro<sup>fi</sup>les in the next period is uniquely determined. Thus, this constitutes a Markov chain over the state space $\Omega ,$ where Ω is the set of all bid pro<sup>fi</sup>les. Generally, the limit distribution of the Markov chain depends on the initial state. However, the following theorem indicates that from any initial bid pro<sup>fi</sup>le, the asynchronous SBT dynamics converges to b<sup>∗</sup>.

Theorem 1. For any bid profile $\mathbf { b } ^ { 0 } ,$ there is a finite sequence of bid profiles starting from $ { \mathbf { b } } ^ { 0 }$ and ending with b<sup>∗</sup> such that in each period, one bidder changes his bid via SBT and the number of bid adjustments is less than or equal to $3 N ( N + 1 ) / 2$

This theorem means that for any bid pro<sup>fi</sup>le, there exists a small probability greater than $\eta > 0$ that b<sup>∗</sup> is realized. This guarantees that the convergence to b<sup>∗</sup> occurs almost surely from any initial bid pro<sup>fi</sup>le. Thus, the following proposition holds.

Proposition 4. For any bid profile $\mathbf { b } ^ { 0 } ,$ the convergence to $\boldsymbol { \mathrm { b } } ^ { * }$ occurs with probability one in the asynchronous SBT dynamics.

In the literature, a slightly different type of asynchronous model is also considered. The difference is that instead of choosing one bidder at random in each period, one order of N bidders is chosen at random in each “round” and the bidders change their bids sequentially in this order. This type of dynamics is more restrictive but much seemingly fairer than one considered in the above because in the dynamics, a bidder generally has a chance to adjust his bid after another bidder adjusts a bid. As shown in the following proposition, under some condition, the convergence to b<sup>∗</sup> is guaranteed when a bidder follows the SBT even though the asynchronous model is the one considered in this paragraph.

Proposition 5. Assume $N = K$ and $r _ { 1 } \cong r _ { 2 } \cong . . . \\\\cong r _ { K }$ hold. For any bid profile $\mathbf { b } ^ { 0 } ,$ the convergence to $\mathbf { b } ^ { * }$ occurs with probability one in the asynchronous dynamics where in each round, the order of N bidders is randomly selected and the N bidders sequentially adjust their bids via SBT.

## 6. Greedy bidding in a sealed-bid environment

The idea of SBT is such that there is a short period for a partial exploration of the bids of others. In this section, I explore this idea further and assume that a bidder can <sup>fi</sup>nd, partly and randomly, the bids of others before adjusting his bid. If such a search for others' bids is executed perfectly, the situation becomes an open-bid environment, and thus, each bidder can follow a greedy bidding strategy, where in each period, advertisers update their bids according to the best response to the others' bids. I <sup>fi</sup>rst explain the greedy bidding strategy considered by Bu et al. [4] and Cary et al. [5,6].

For any bid pro<sup>fi</sup>le b and for any advertiser i, let b be the bid pro<sup>fi</sup>le except for i's bid. Assume that at b, i obtains ad slot $k \leq K .$ Then, given the other bids, the price of ad slot ‘ paid by advertiser i per click is $p _ { \ell } ^ { i } =$ $b _ { d ( \ell ) }$ for‘bkand $p _ { \ell } ^ { i } = b _ { d ( \ell + 1 ) }$ <sup>¼</sup>for‘ k. The asymmetry of prices between the <sup>ð Þ ð Þþ</sup>higher and lower ad slots comes from the fact that in order to obtain the higher ad slot $\ell ,$ i must beat the bid of advertiser $d ( \ell )$ , who currently oc-<sup>ð Þ</sup>cupies ad slot ‘. However, it is suf<sup>fi</sup>cient for i to beat the bid of $b ( \ell + 1 )$ who currently occupies ad slot $\ell + 1$ <sup>ð</sup>to obtain the lower ad slot ‘.

The best response of i against b <sub>i</sub> is to choose a bid to obtain ad slot $\ell ^ { * }$ in

$$
\arg \max _ {\ell \in \{1, \dots , K + 1 \}} \alpha_ {\ell} (v _ {i} - p _ {\ell}).
$$

If there are multiple best-response ad slots, we assume that the advertiser chooses the highest ad slot among them (i.e., smallest $\ell ) .$ If the prices of any ad slots are greater than $\nu _ { i } ,$ i's best-response ad slot is $K + 1$ .Even though the best-response ad slot $\ell ^ { * }$ is determined, there are many best-response bids against b $^ { - i \dagger }$ that is, any bid in the interval $( p _ { \ell } , p _ { \ell - 1 } )$ is the best response to $\mathbf { b } _ { - i }$ . To choose one from them, we assume that the advertiser uses secure bidding for ad slot $\ell ^ { * }$ . Thus, his bid is $b _ { i } ^ { S } \left( \ell , p _ { \ell } ^ { i } \right)$

The greedy bidding strategy mentioned above is summarized as follows. Let b be a current bid pro<sup>fi</sup>le and i be an advertiser obtaining ad slot k. The secure greedy bidding (SGB) is the following bid adjustment:

• Let ‘<sup>∗</sup> be the smallest element in arg max $\ell { \in } \{ 1 , { \ldots } , K { + } 1 \} { \alpha } _ { \ell } ( { \nu } _ { i } { - } { p } _ { \ell } )$

• I $\mathrm { : } \ell ^ { \ast } \le K , \mathrm { : }$ i submits $b _ { i } ^ { S } ( \ell ^ { * } , p _ { \ell ^ { * } } ^ { i } )$

• $\textstyle \mathbf { f } \ \ell ^ { * } = K + 1 ,$ , i submits $\nu _ { i \cdot }$

Cary et al. ([5,6] and Bu et al. [4] separately analyzed SGB and showed that the unique <sup>fi</sup>xed point of the SGB is b<sup>∗</sup>. Moreover, they also show that for any bid pro<sup>fi</sup>le $\mathbf { b } ^ { 0 } ,$ , there exists a <sup>fi</sup>nite sequence of bid pro<sup>fi</sup>les starting from $ { \mathbf { b } } ^ { 0 }$ and ending with b<sup>∗</sup> such that in each period, one bidder changes its bid via SGB.

Asynchronous SGB dynamics presents a situation where, in each period, one advertiser is randomly selected, and he changes his bid according to SGB. The following proposition holds.

Proposition 6. For any bid profile $\mathbf { b } ^ { 0 } ,$ the convergence to b<sup>∗</sup> occurs with probability one in asynchronous SGB dynamics [5,4].

Next, we consider a SGB adjustment model with a search for other bids. Let q be the probability that an advertiser $i = d ( k )$ <sup>fi</sup>nds the price of each ad slot in a search period. As a result of the search, the advertiser knows the price of ad slots in B, which is a subset of $\left\{ 1 , . . . , K , \right.$ $K + 1 \}$ . B must be non-empty because $k + 1 \in B$ and $K + 1 \in B$ always hold. Advertiser i chooses secure bidding to acquire the ad slot in arg $\mathrm { m a x } _ { \ell \in B } \alpha _ { \ell } ( \nu _ { i } - p _ { \ell } )$ in the next period.

<sup>ð Þ</sup>Let b be a current bid pro<sup>fi</sup>le and i be an advertiser obtaining ad slot k. The secure partial greedy bidding (SPGB) is as shown in the following bid adjustment.

• Let B be the set of ad slots the prices of which are detected in a search period, where the price of each slot is detected independently with probability q.

• Let ‘<sup>∗</sup> be the smallest element in arg max $\varrho { \bf { \mathrm { } } } B ^ { \alpha _ { \ell } } ( \nu _ { i } { - } p _ { \ell } )$

• I $: \ell ^ { * } \leq K$ , then i submits $b _ { i } ^ { S } ( \ell ^ { * } , p _ { \ell ^ { * } } ^ { i } )$

• If $\dot { \ell } ^ { * } = K + 1$ , then i submits $\nu _ { i \cdot }$

If $q = 1 ,$ , this is identical to asynchronous SGB dynamics. Even though B is determined by $( K - 1 )$ ) independent random trials, there always exists some positive probability $( \dot { = } q ^ { K - 1 } )$ such that $B = \{ 1 , . . . , K ,$ $K + 1 \}$ . This means that the bidders choose the same bid as in SGB with positive probability. Coupled with the fact that there exists a <sup>fi</sup>nite sequence of bid pro<sup>fi</sup>les starting from any initial bid pro<sup>fi</sup>le and ending with b<sup>∗</sup> such that in each period one bidder changes his bid via SGB, the following proposition can be induced.

Proposition 7. For any bid profile $\mathbf { b } ^ { 0 } ,$ the convergence to $\boldsymbol { \mathrm { b } } ^ { * }$ occurs with probability one in asynchronous SPGB dynamics.

## 7. Comparison among SBT, SGB, and SPGB

We now have three different bid adjustment strategies: (1) SGB for the open-bid environment and (2) SBT and (3) SPGB for the sealed-bid environment. A prominent feature common to these three is that they have the same <sup>fi</sup>xed point (b<sup>∗</sup>) of bid adjustment dynamics. Thus, to obtain further insight, we need to investigate how these three are different before arriving at the <sup>fi</sup>xed point. Since convergence to the <sup>fi</sup>xed point is guaranteed by Propositions 4, 5, and $6 ,$ a comparison among the three can be a fair method to evaluate to what extent the sealed-bid environment is bene<sup>fi</sup>cial or harmful to advertisers and the search engine relative to the open-bid environment.

To see how these three bid adjustments are different, I run a computer simulation. In the simulation, the number of slots equals the number of advertisers, and the CTR is chosen as the geometrically decreasing sequence by $\alpha _ { k } = \delta ^ { k - 1 }$ for all k given some $\delta \in ( 0 , 1 )$ . For each parameter selection on the discount rate (δ), the number of advertisers (N), and the detection probability to others' bids (q), I take 200 instances, where, in each instance, the values of advertisers are chosen from a normal distribution with $\mu = 5 0 0$ and $s . d . = 2 0 0$ following Cary et al. [5].

## 7.1. Convergence speed of SGB, SPGB and SBT

Fig. 2 plots the average time before the convergence of SBT, SPGB (with detection probabilities 0.75, 0.59, 0.10), and SGB as a function of δ, where δ is calibrated from 0.50 to 0.95 in steps of 0.05, <sup>fi</sup>xing $N = 1 0 .$ First, this indicates that in all <sup>fi</sup>ve bidding strategies, the time before convergences increases as the values of CTRs become denser, that is, as δ approaches 1. This is because when the values of CTRs across ad slots are dense, advertisers' bids also tend to become dense, implying that bid adjustment to the <sup>fi</sup>xed point is more dif<sup>fi</sup>cult. A similar observation is also found in Cary et al. [5] using a different bidding strategy. Second, even though the greedy bidding is imperfect in a sealed-bid environment, SPGB with middle or high detection probability shows a similar convergence speed to that of SGB. On the other hand, SPGB with low probability and SBT converge at a lower rate compared to SGB, and this becomes clearer as δ approaches 1.

The second observation still holds even when we change the number of advertisers. Fig. 3 plots the average time before the convergence of SBT, SPGB (with detection probabilities 0.75, 0.50, 0.10), and SGB, as a function of N. I <sup>fi</sup>x $\delta = 0 . 7$ because this value has proven to be well-<sup>fi</sup>tted in practical data [12]. Here, the average time of convergence is divided by N in order to eliminate the direct effect of the increase in N, given that as only one advertiser changes his bid, the increase in N necessarily increases the time before convergence. Fig. 3 indicates that in all cases, the time before convergence increases non-linearly as a function of N; this interpretation is consistent with Theorem 1, at least for SBT.

![](/api/attachments/YQ77YSQF/fulltext/images/8e745509b53ed7874145bc52909746dc1ba390c493d4f7f161bd79cfb0f60f70.jpg)  
Fig. 2. Average time of convergence of SBT, SPGB, and SGB as a function of δ $( N = 1 0 ) .$

![](/api/attachments/YQ77YSQF/fulltext/images/bebbd68b7dc0e144a1ab266cdc1a3b8990b33c204b4ccce6832c011ae70f74d2.jpg)  
Fig. 3. Average time of convergence of SBT, SPGB, and SGB as a function of N $( \delta = 0 . 7 )$

In the simulation results displayed above, I choose only three detection probabilities. Thus, it is unclear when the convergence speed of SPGB becomes largely different from that of SGB. Fig. 4 plots the average time before the convergence of SPGB as a function of detection probability q, where q is calibrated from 1 to 0.05 in steps of 0.05, <sup>fi</sup>xing $N = 1 0 ,$ 20, 30 and $\delta = 0 . 7$ . This indicates that there is a kink near $q = 0 . 1 5$ . For the interval greater than this kink, the average time of convergence is moderately elevated as q decreases. However, it rises steeply in the interval less than the kink. This is quite surprising and can be a positive result since even though in the sealed-bid environment, the convergence speed is not so different from that in the open-bid environment (if advertisers follow the greedy bidding strategy).

## 7.2. Payoff and revenue comparison in open- and sealed-bid environments

Even though convergence to equilibrium is guaranteed, the average payoffs for advertisers and the average revenue of a search engine before the convergence are of concern to both parties, because the changes in parameters such as CTRs, values, and the number of advertisers, entail a change in equilibrium bids, and such changes in parameters occur frequently in practice.

Fig. 5 plots the average payoff of advertisers and the revenue of a search engine before convergence to equilibrium in open-bid and sealed-bid environments. First, this indicates that when we compare SGB and SPGB, an advertiser's payoff in SPGB is smaller than that in SGB, and this decreases as the detection probability decreases. For a search engine, the relationship is completely reversed. That is, the search engine's revenue in SPGB is larger than that in SGB, and this increases as the detection probability decreases. Comparing SGB and SBT, the same relationships hold for both the payoffs and the revenue.

![](/api/attachments/YQ77YSQF/fulltext/images/812ce61d7b61b352b6861ac165f8fe8b5677b6e08acc40e7e14c36b0cbde86fb.jpg)  
Fig. 4. Average time of convergence of SBT, SPGB, and SGB as a function of q $( \delta = 0 . 7 ) .$

![](/api/attachments/YQ77YSQF/fulltext/images/eead6ffe71f8ab61c2f259a010d54ace9f7441d268b3c1b7279af128ebe87f81.jpg)  
Fig. 5. Average payoffs for advertisers and revenue of a search engine before convergence relative to equilibrium payoffs and revenue, respectively $( N = 1 0 , \delta = 0 . 7 )$

From this, the sealed-bid environment may be bene<sup>fi</sup>cial to the search engines and disadvantageous to advertisers, at least in the time before equilibrium has been attained.

Second, comparing SPGB and SBT (the two bidding strategies for a sealed-bid environment), an advertiser's payoff in SPGB is considerably larger than that in SBT, and the inverse relation holds for the search engines. In addition, while the payoffs of advertisers in SPGB before the convergence are greater than the equilibrium payoffs, those in SBT are not. In contrast, the revenue in SBT till the convergence is greater than the equilibrium revenue, but that is not the case in SPGB. This seems to be consistent with the bidding war that can occur before the convergence (see subsection 4.3).

This analysis suggests that advertisers should use SPGB rather than SBT. Moreover, the effort expended to detect the bids of others rewards the advertisers. For the time before convergence, search engines can exploit advertisers in a sealed-bid environment.

## 8. Conclusion

In this paper, I explored the types of bidding behavior in a sealed-bid keyword auction. I <sup>fi</sup>rst showed that secure bidding (where the bidder does not search for information on the bids of other advertisers) has several limitations. Then, I considered secure bidding with minimal exploration through a trial bid (SBT) and showed that the <sup>fi</sup>xed point of SBT is uniquely determined and that the dynamic bid adjustment according to SBT converges to the <sup>fi</sup>xed point with probability one.

An imperfect version of the greedy bidding strategy (SPGB) was also investigated and the convergence result still holds for SPGB.

A computer simulation showed that a search engine can bene<sup>fi</sup>t from a sealed-bid environment. Advertisers can improve their payoffs by switching from SBT to SPGB. One reason is that the search for a bene<sup>fi</sup>cial lower ad slot may decrease bids, and thus, reduce the price of ad slots until the <sup>fi</sup>xed point is realized. A similar observation is reported from Cary et al. [29] who compared the greedy bidding among all ad slots and one where a bidder searches only the lower ad slots. They <sup>fi</sup>nd that the latter is more pro<sup>fi</sup>table to advertisers than the former. However, the switch from SBT to SPGB will be costly to advertisers because detecting others' bids is more dif<sup>fi</sup>cult than checking the allocation. In addition, it seems that an automated bidding agent that searches for others' bids is prohibited by a search engine; as of March 2012, no Internet advertising agency provides such a service.<sup>9</sup>

I conclude by discussing other reasons for a search engine to use a sealed-bid auction. First, a sealed-bid environment prevents advertisers from antisocial or spiteful bidding, whereby an advertiser bids slightly lower than the bid of the advertiser in the targeted position. Liang and Qi [20] and Zhou and Lukose [28] suggested that antisocial bidding was observed in the data from Yahoo! when it used an open-bid environment and theoretically proved that antisocial bidding leads to instability of bids in a dynamic auction. In other words, combined with our theoretical <sup>fi</sup>nding, this indicates that a sealed-bid environment may validate using an envy-free equilibrium to analyze the market of keyword auctions. Second, under a sealed-bid environment, advertisers tend to engage in a competition in differentiation by, for example, improving the quality of advertisements or <sup>fi</sup>nding more attractive keywords rather than competing in bidding. This implies that advertisers can avoid price competition that is not bene<sup>fi</sup>cial in the long run. In addition, competition in differentiation by advertisers can also bene<sup>fi</sup>t a search engine because it creates a marketplace for online advertisements. Thus, if advertisers compete only in the bidding for some given keyword, the advertisers and a search engine are in a zero-sum situation where the surplus generated from the keyword is constant and the problem is how to divide the surplus between advertisers and a search engine. In contrast, a competition in differentiation can lead to a win–win relationship between them.

## Acknowledgments

I thank Makoto Yokoo, Yukihiko Funaki, and the participants at the 2010 Japanese Economic Association Autumn Meeting and the 2011 Autumn Meeting of the Operations Research Society of Japan for their helpful comments. I am also grateful for the associate editor and two anonymous referees for their useful comments and suggestions. This work has been <sup>fi</sup>nancially supported by the JSPS Grant-in-Aid for Young Scientists (B) 21730162 and 23730194, and by the Seimeikai foundation.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at http://dx. doi.org/10.1016/j.dss.2013.07.003.

## References

[1] K. Asdemir, A dynamic model of bidding patterns in sponsored search auctions, Information Technology and Management 12 (2010) 1-16

[2] S. Athey, G. Ellison, Position auctions with consumer search, forthcoming in, The Quarterly Journal of Economics 126 (3) (2011) 1213–1270.

[3] F. Brandt, G. Weiss, Antisocial agents and Vickrey auctions, Intelligent Agents VIII, LNCS 2333 (2002) 335-347

[4] T.-M. Bu, X. Deng, Q. Qi, Dynamic of strategic manipulation in ad-words auction, Workshop on Sponsored Search Auctions, in Conjunction With the 16th International World Wide Web Conference, Canada (May 11, 2007), 2007.

[5] M. Cary, A. Das, B. Edelman, I. Giotis, K. Heimerl, R. Karlin, C. Mathieu, M. Schwarz, Greedy bidding strategies for keyword auctions, Proceedings of the 8th ACM Conference on Electronic Commerce, 2007, pp. 262–271.

[6] M. Cary, A. Das, B. Edelman, I. Giotis, K. Heimerl, R. Karlin, C. Mathieu, M. Schwarz, On best-response bidding in GSP auctions. NBER Working Paper Series, 2008, p. 13778

[7] E.H. Clarke, Multipart pricing of public goods, Public Choice 11 (1971) 17–33.

[8] B. Edelman, M. Ostrovsky, Strategic bidder behavior in sponsored search auctions, Decision Support Systems 43 (2007) 192-198.

[9] B. Edelman, M. Ostrovsky, M. Schwarz, Internet advertising and the generalized second price auction: selling billions of dollars worth of keywords, American Economic Review 97 (2007) 242–259.

[10] B. Edelman, M. Schwarz, Optimal auction design in a multi-unit environment: the case of sponsored search auctions forthcoming in American Economic Review Papers and Proceedings 100 (2010) 597–602.

[11] J. Feng, Optimal mechanism for selling a set of commonly ranked objects, Marketing Science 27 (2008) 501–512.

[12] J. Feng, H.K. Bhargava, D.M. Pennock, Implementing sponsored search in web search engines, INFORMS Journal on Computing 19 (2007) 137–148.

[13] E. Fukuda, Y. Kamijo, A. Takeuchi, M. Masui, Y. Funaki, Theoretical and experimental investigations of performances of the keyword auction mechanisms, forthcoming in, RAND Journal of Economics (2013).

[14] B. Jansen, T. Mullen, Sponsored search: an overview of the concept, history, and technology, International Journal of Electronic Business 6 (2008) 114–131.

[15] Z. Katona, M. Sarvary, The race for sponsored links: bidding patterns for search advertising, mimeo (2008).

[16] B. Kitts, B. LeBlanc, Optimal bidding on keyword auctions, Electronic Markets 14 (2004) 186–201.

[17] T. Groves, Incentives in teams, Econometrica 41 (1973) 617–631.

[18] J. Li, D. Liu, S. Liu, Optimal keyword auctions for optimal user experiences, Decision Support Systems, 2013 (forthcoming).

[19] L. Li, D. Zeng, H. Zhao, Pure-strategy Nash equilibria of GSP keyword auction, Journal of the Association for Information Systems 13 (2012) 57–87.

[20] L. Liang, Q. Qi, Cooperative or vindictive: bidding strategies in sponsored search auction, WINE, 2007, pp. 167–178.

[21] D. Liu, J. Chen, Designing online auctions with past performance information, Decision Support Systems 42 (2006) 1307–1320.

[22] D. Liu, J. Chen, A. Whinston, Ex ante information and the design of keyword auctions, Information Systems Research 21 (2010) 133–153.

[23] H.R. Varian, Position auctions, International Journal of Industrial Organization 25 (2007) 1163–1178.

[24] H.R. Varian, Online ad auction, AER Papers and Proceedings, 2009

[25] W. Vickrey, Counterspeculation, auctions, and competitive sealed tenders, Journal of Finance 16 (1961) 8–27.

[26] X. Zhang, J. Feng, Price cycles in online advertising auctions, Twenty-Sixth International Conference on Information System, 2005.

[27] X. Zhang, J. Feng, Cyclical bid adjustments in search-engine advertising, Management Science 57 (2011) 1703–1719.

[28] Y. Zhou, R. Lukose, Vindictive bidding in keyword auctions, Proceedings of the Ninth International Conference on Electronic Commerce, 2007.

[29] M. Cary, A. Das, B. Edelman, I. Giotis, K. Heimerl, A. Karlin, S. Kominers, C. Mathieu, M. Schwarz, Convergence of position auctions under myopic best-response dynam ics, ACM Transactions on Economics and Computation (2013), (forthcoming).

![](/api/attachments/YQ77YSQF/fulltext/images/b4d2aa43364ca5283a6f1131f21bf340748cc89e479437c09308a2299ff608f7.jpg)  
Yoshio Kamijo is an associate Professor of the School of Management at the Kochi University of Technology (KUT), Japan. He received his Ph.D. degree in Economics from the Graduate School of Economics, Waseda University. His research interests include game theory, mathematical economics, industrial organization and experimental economics. His research has appeared in International Journal of Game Theory, Mathematical Social Sciences, Journal of Mathematical Economics, Rand Journal of Economics, Regional Science and Urban Economics, European Journal of Operational Research, Journal of Socio-Economics and others.

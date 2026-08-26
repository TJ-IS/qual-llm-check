---
otero_id: 1558
otero_key: "PUYV7N2F"
title: "Designing Hybrid Mechanisms to Overcome Congestion in Sequential Dutch Auctions"
authors: "Yixin Lu; Alok Gupta; Wolfgang Ketter; Eric van Heck"
year: "2022"
journal: "MIS Quarterly"
doi: "10.25300/misq/2022/16472"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DESIGNING HYBRID MECHANISMS TO OVERCOMECONGESTION IN SEQUENTIAL DUTCH AUCTIONS<sup>1</sup>

Yixin Lu School of Business, George Washington University, Washington, DC, U.S.A {yixinlu@gwu.edu}

Alok Gupta Carlson School of Management, University of Minnesota, Minneapolis, MN, U.S.A. {alok@umn.edu}

Wolfgang Ketter

Faculty of Management, Economics, and Social Sciences, University of Cologne, Cologne, GERMANY, and Rotterdam School of Management, Erasmus University, Rotterdam, THE NETHERLANDS {ketter@wiso.uni-koeln.de}

Eric van Heck Rotterdam School of Management, Erasmus University, Rotterdam, THE NETHERLANDS {evanheck@rsm.nl}

A common problem in many mature markets is how to deal with congestion—a situation in which transaction requests from market participants cannot be accommodated in an expedited manner. This paper examines the congestion problem in sequential Dutch auction markets. Transactions in these markets typically involve perishable goods, making market clearing speed crucial. Traditionally, sequential Dutch auctions have been implemented with fast-paced auction clocks that process equally attractive bids in the order they arrive and only award the first bidder as the winner of each round, which can lead to serious congestion in case of a demand surge. We propose a hybrid mechanism that capitalizes on the discrete nature of the auction clock and batches together the highest bids, allowing multiple transactions at the same price in each round. To evaluate the performance of the hybrid mechanism, we first develop a game-theoretic model comparing the hybrid mechanism to the traditional sequential Dutch auction mechanism. Our model predicts that the hybrid mechanism will achieve higher operational efficiency without compromising allocative efficiency. We then complement the theoretical analysis by evaluating the hybrid mechanism through a quasi-natural field experiment. The empirical analysis of the field data shows that the hybrid mechanism can significantly speed up the market clearing process and increase price stability without affecting the expected revenue. Our findings shed new light on the design and operation of multi-unit auctions.

Keywords: Mechanism design, market congestion, discrete bids, quasi-natural field experiment, hybrid mechanism, sequential Dutch auctions, analytical model, game theory, digital transformation

## Introduction

“Every new market has to attract enough participants and then help those participants cope with the resulting congestion.” (Alvin E. Roth, “The Art of Designing Markets,” 2007, p. 8)

The digital transformation has created unprecedented opportunities for businesses to design, implement, and profit from markets (Bichler et al. 2010). Some famous examples include e-commerce sites such as eBay and Amazon (Bajari and Hortaçsu 2004), ad exchanges powered by Google and Microsoft (Varian 2009), and online labor markets such as Freelancer (Hong et al. 2015). While the durability and success of a market require thorough examination of various idiosyncratic issues, a common problem faced by many mature markets is how to deal with congestion—a situation in which transaction requests from market participants cannot be accommodated in an expedited manner. Regardless of the sources, congestion can lead to significant market failures (Roth 2015).

In this paper, we focus on the congestion problem in sequential Dutch auction markets. Transactions in these markets typically involve trades of perishable goods such as fish, flowers, or tobacco (Graham 1998; Klemperer 1999; Lu et al. 2016). Traditionally, sequential Dutch auctions are implemented using fast-paced clocks. The clock is initially set at a high price level that points to the 12 o’clock position. Once an auction starts, the clock ticks down counterclockwise to predetermined points that correspond to different price levels. A bidder (buyer) can place a bid by pressing a button to stop the clock at the current price. If multiple bidders place bids at the same price, the bidding requests will be processed in the order they arrive<sup>2</sup> and only the first (earliest) bidder is awarded the goods. If the winning bidder does not purchase the entire bundle of goods being auctioned, the clock restarts at a high price position and the process is repeated. Note that in this case, congestion arises from the failure to accommodate bidding requests for the same goods at the same time; although capacity may exist (i.e., the winner’s demand is less than the total available amount), the temporal demand experiences a delay because it can only be fulfilled in later rounds. Due to the perishable nature of the goods, such congestion can be very costly for both buyers and sellers; if it is left unaddressed, buyers and sellers will leave and seek alternative ways to trade.

Given the discrete nature of the auction clock (and thus the predetermined price levels), the congestion in sequential rounds could be intuitively mitigated by batching together all the bids at a given price level. That is, all the bids arriving between the time of the first bid and the time the clock ticks down to the next price level would be honored at the same price; if the temporal demand exceeds the supply, the auctioned goods would be randomly allocated among the winning bidders. Such a modified mechanism could be viewed as a hybrid of the traditional sequential Dutch auction and the uniform-price auction.

At the outset, the hybrid mechanism could speed up the marketclearing process by enabling multiple transactions in each round. However, bidders may adopt different bidding strategies in response to the mechanism change, which, in turn, would affect the winning prices and sellers’ revenue. On the one hand, the multi-winner feature may lead to stronger bid-shading. On the other hand, the observation that multiple competitors have purchased in the current round could be perceived as a signal of increased intensity of competition (Häubl and Popkowski Leszczyc 2019) and thus may lead to more aggressive bidding in subsequent rounds.

Our main research question is: How does the hybrid mechanism impact bidding dynamics and outcomes? To address this question, we first develop a game-theoretical model to characterize the strategic interactions under the traditional sequential Dutch auction mechanism and the hybrid mechanism, respectively. Our theoretical analysis shows that the hybrid mechanism achieves higher operational efficiency without compromising allocative efficiency. Since the gametheoretical model relies on strong assumptions about bidders’ underlying demand, information structure, and bidding behavior, which may not hold in real-world markets, we further evaluate the performance of the hybrid mechanism through a large-scale quasi-natural field experiment (Shadish et al. 2002). The empirical analysis of the field data shows that the hybrid mechanism can significantly speed up the market clearing process without affecting the expected revenue. In particular, we observed that the average number of rounds taken to complete an auction dropped by approximately 18% under the hybrid mechanism. We also found that the hybrid mechanism can significantly increase price stability, which is in the interest of both sellers and buyers in a wholesale market.

Our paper makes important contributions to both the theory and practice of market design. To start with, our study is among the first to examine the potential of a hybrid mechanism in mitigating congestion in multi-unit sequential auctions. In this regard, we contribute to the growing body of information systems research that studies novel design choices in complex markets (Bichler et al. 2010). Next, we extend the literature on optimal mechanism design by incorporating operational efficiency as a key performance metric. While prior research has demonstrated that an auction’s duration or overall rate of progression should be viewed as a valuable resource in market design (Katok and Kwasnica 2008), most of the existing studies assume the auction speed as given or exogeneous. By contrast, we endogenize the operational efficiency in studying alternative design choices. Finally, despite the growing interest in hybrid mechanisms (Dutra and Menezes 2002), there is limited understanding of the design and implementation of these mechanisms in real-world markets. In the current research, we adopt a multi-method approach where we combine analytical modeling and rich field data to evaluate the performance of the proposed hybrid mechanism. Therefore, our findings provide useful insights for practitioners.

The rest of the paper proceeds as follows. We first review prior works on auction design. Following that, we present the gametheoretical model and derive theoretical predictions about the performance of the hybrid mechanism. We then test these predictions using data collected from a large-scale quasi-natural field experiment. Finally, we discuss the implications of our findings and outline the directions for future research.

## Literature Review

Auctions have long been used to facilitate trades of products and services. One of the central questions in auction design concerns the choice of the selling mechanism. Different selling mechanisms vary in their allocation and pricing rules, transparency (i.e., the extent to which mechanisms disclose information to market participants), and transaction cost. The general consensus is that the optimal choice is be based on the nature of the goods or services being auctioned, the prospective supply and demand relationship, and the market environment (Einav et al. 2018; Hong et al. 2015; Hortaçsu and McAdams 2010; Wei and Lin 2017). Below, we discuss prior studies that are closely related to our current research.

## Single-Unit vs. Multi-Unit Auctions

Since the publication of Vickrey’s (1961) seminal work, researchers have made extensive progress in understanding the revenue implications of different selling mechanisms. For single-unit auctions, one of the most celebrated results is the revenue equivalence theorem, which states that the standard types of auctions — English, Dutch, first-price sealed-bid, and second-price sealed-bid—generate the same expected revenue under the assumption that bidders hold independent private values of the object for sale and are risk-neutral toward winning (Vickrey 1961; Myerson 1981). When bidders’ information about the object is affiliated,<sup>3</sup> Milgrom and Weber (1982) have shown that mechanisms that release more information lead to higher expected prices; accordingly, English auctions would generate more revenue than secondprice sealed-bid auctions, which in turn would generate more revenue than first-price sealed-bid auctions. Apart from the information structure, different auction mechanisms also vary in their dynamic properties. For example, Katok and Kwasnica (2008) have shown that bidders are willing to trade monetary cost for time saved, suggesting that the speed of an auction is an important design parameter.

Compared with single-unit sales, the optimal design problem in multi-unit auctions is much more complex, as such auctions involve a set of additional economic issues that affect the bidding process (Ausubel et al. 2014; Bapna et al. 2003a; Goes et al. 2012; Lu et al. 2016). For multi-unit simultaneous auctions, a long-debated issue is the choice between two different pricing rules (Hortaçsu and McAdams 2010): the uniform-price rule, where all the winning bidders pay the same price, and the discriminatory-price rule, where each bidder pays what was bid for the unit(s) won. The common wisdom is that uniform-price auctions and discriminatory-price auctions can be viewed as multi-unit generalizations of second- and first-price auctions, respectively. Therefore, these multi-unit variants inherit the efficiency ranking described in Milgrom and Weber (1982). However, researchers have shown, both empirically and analytically, that the truth-telling attributes or the efficiency property of second-price auctions do not carry over to uniform-price auctions, due to differential bid shading across different units. In other words, bidders are incentivized to shade their bids differently across units (Ausubel et al. 2014; List and Lucking-Reiley 2000). When it comes to multi-unit sequential auctions, McAfee and Vincent (1993) have shown that even in very simple settings, the equilibrium in multiunit sequential auctions could involve mixed strategies, and characterizing these strategies is a formidable task. Further, as bidders are competing for the same goods with each other repeatedly, they could learn from signals about their competitors and market conditions and adapt their bidding strategies accordingly (Jeitschko 1998; Zeithammer 2007). These findings reinforce the importance of adaptation and customization of pricing rules in multi-unit auctions.

## Continuous vs. Discrete Bids

To date, most of the theoretical work on auction design assumes that bids are continuous (Krishna 2009). However, in many real-world auctions, bids are restricted to a finite set of discrete values. For example, online auction sites such as eBay and Amazon often impose a minimum bid increment to speed up the process. In discrete bid auctions, full efficiency is generally unachievable (Rothkopf and Harstad 1994a): since there may be more than one bidder who submits the same bid, the allocation relies on either a priori ranking or randomization; there is no guarantee that the auctioned good(s) will be assigned to the bidder with the highest valuation.

Among the few studies that have examined auctions with discrete bids, researchers are primarily interested in the optimization of the bid increment (Bapna et al. 2003b; Li and

Kuo 2013; Rothkopf and Harstad 1994a). The most closely related paper to ours is Bapna et al. (2003b), where the authors provide both analytical and empirical evidence of the importance of the bid increment on bidding strategies and propose a heuristic decision rule to set the bid increment. The main difference between Bapna et al. (2003b) and our work is that the former adopts a decision-theoretic perspective to study bidding behaviors, whereas we first adopt a gametheoretic perspective to derive the symmetric, pure-strategy Bayesian Nash equilibrium under the traditional sequential Dutch auction mechanism and the hybrid mechanism, and then test the theoretical predictions from the equilibrium analysis through a large-scale quasi-natural field experiment.

## Hybrid Mechanisms

The proliferation of internet-based markets has fueled the development of hybrid mechanisms that combine commonly used selling mechanisms and shed new light on optimal selling mechanisms. For example, eBay has introduced the buy-it-now (BIN) feature into its auctions, which allows buyers to purchase the item(s) under auction at a predetermined, fixed price set by the seller. At first glance, it is puzzling why sellers would adopt such a hybrid mechanism given that the BIN option caps the maximum sales price and thus lower the profitability. However, researchers have found that when bidding incurs high transaction costs, the BIN auction could increase both sellers’ profits and buyers’ surplus (Mathews 2004).

Another notable example is the buy-it-now or take-a-chance (BINTAC) mechanism proposed by Celis et al. (2014) in the display advertising market. In a BINTAC auction, if there is only one bidder choosing the BIN option, that bidder will receive the auctioned item at the predetermined price. If more than one bidder chooses the BIN option, a second-price auction will be held, and the buy-it-now price will be used as the reserve price. If no bidder is interested in the BIN option, one of the top bidders will be randomly selected to receive the auctioned item. BINTAC ensures that the item for sale can be allocated, regardless of bidders’ value distribution, while incentivizing high-valuation bidders to choose the buy-it-now option rather than wait and take their chances in the bidding process.

Our paper shares the same spirit of the growing literature that examines the performance of hybrid mechanisms in complex real-world environments. A key difference between our paper and prior studies is that we are not only interested in the expected revenue generated from the sales, but also the operational efficiency (i.e., how fast a mechanism can allocate the goods for sale). Because time is a valuable resource for both sellers and buyers, it is important to examine whether a mechanism can achieve a high market clearing speed.

## Theoretical Model

Consider N (?? > 2) bidders competing for two identical items. Bidders are assumed to be risk-neutral and have single-unit demand (i.e., a bidder exits the auction upon winning one unit). Each Bidder ?? draws a private value $v _ { i } ( i = 1 , \dots N )$ independently from a commonly known, continuous distribution $\mathcal { F }$ on [0,1] and chooses a bid from the set $B = \{ b _ { 1 } , b _ { 2 } , \dots b _ { M } \}$ , where $b _ { j } = ( j - 1 ) / M , j = 1 , 2 , . .$ , ??. The bid increment $1 / M$ is constant and can be as small as one cent in real-world auctions. A bidding strategy $\beta$ is a function from [0,1] to set ??.

Below we first characterize the equilibrium strategies under the sequential Dutch auction mechanism and the hybrid mechanism, respectively. We then compare the performance of the two mechanisms in equilibrium.

## Equilibrium Analysis

## The Sequential Dutch Auction Mechanism

In the traditional sequential Dutch auction, in each round of the auction, the bidder with the highest bid receives the item and pays a price equal to the placed bid. If two or more bidders submit the same highest bid, a random tie-breaking rule is adopted.<sup>4</sup>

We are interested in sequentially rational equilibria<sup>5</sup> and consider symmetric bidding strategies given by:

$$
\beta^ {I} (v _ {i}) = \left\{ \begin{array}{l l} b _ {k}, i f v _ {i} \in (t _ {k - 1} ^ {I}, t _ {k} ^ {I} ] k \geq 2 \\ b _ {1}, i f v _ {i} \leq t _ {1} ^ {I} \end{array} \right.\tag{1}
$$

$$
\beta^ {I I} (v _ {i}) = \left\{ \begin{array}{l l} b _ {l}, i f v _ {i} \in (t _ {l - 1} ^ {I I}, t _ {l} ^ {I I} ], l \geq 2 \\ b _ {1}, i f v _ {i} \leq t _ {1} ^ {I I} \end{array} \right.\tag{2}
$$

Here, $\beta ^ { I }$ and $\beta ^ { I I }$ denote the bidding strategy in the first round and second round, respectively. $t _ { k } ^ { I }$ and $t _ { k } ^ { I I }$ are series of critical points that partition the value space, and $0 = t _ { 0 } ^ { I } <$ $t _ { 1 } ^ { I } < \cdots \dot { t } _ { k } ^ { I } < \cdots < t _ { r } ^ { I } = 1 , 0 = t _ { 0 } ^ { I I } < t _ { 1 } ^ { I I } \dot { < } \cdots t _ { l } ^ { I I } < \cdots < t _ { s } ^ { I I } =$

1, and $1 \leq r , s \leq M$ . Given the assumptions above, we can prove that Equations $( 1 ) \ - \ ( 2 )$ constitute a symmetric Bayesian Nash equilibrium.

Proposition 1. Given a sequential Dutch auction that sells two identical items to bidders with single-unit demand, if each bidder draws a private value independently from a commonly known, continuous distribution ℱ on [0,1] and chooses a bid from the set $B = \{ b _ { 1 } , b _ { 2 } , \dots b _ { M } \}$ where $b _ { j } = ( j - 1 ) / M , j = I ,$ $2 , \ \dots , \ M _ { \mathrm { ~ } }$ , there exist two series, $\{ t _ { k } ^ { I } , k \geq 1 \}$ and $\{ t _ { l } ^ { I I } , l \ge 1 \}$ such that the bidding strategies defined by Equations $( l ) - ( 2 )$ constitute a symmetric Bayesian Nash equilibrium.

The proof of Proposition 1 makes use of backward induction. The detailed proofs of all the propositions in this paper are given in the Appendix. It is worth noting that, while the bid levels $b _ { 1 } , b _ { 2 } , \dots b _ { M }$ are equally distributed with a constant increment of $1 / M$ , neither $t _ { k } ^ { I }$ nor $t _ { l } ^ { I I }$ is necessarily equally distributed in the value space.

## The Hybrid Mechanism

As explained earlier, the hybrid mechanism combines the characteristics of the traditional sequential Dutch auction and the uniform price auction. Specifically, if only one bidder submits the highest bid in the first round, the hybrid mechanism proceeds exactly as the traditional sequential Dutch auction. However, if two or more bidders submit the same highest bid in the first round, the two items under auction are randomly assigned to two bidders with the highest bid and the auction ends. Again, we consider symmetric bidding strategies:

$$
\hat {\beta} ^ {I} (v _ {i}) = \left\{ \begin{array}{l l} b _ {k}, i f v _ {i} \in (\hat {t} _ {k - 1} ^ {I}, \hat {t} _ {k} ^ {I} ] k \geq 2 \\ b _ {1}, i f v _ {i} \leq \hat {t} _ {1} ^ {I} \end{array} \right.\tag{3}
$$

$$
\hat {\beta} ^ {I I} (v _ {i}) = \left\{ \begin{array}{l l} b _ {l}, i f v _ {i} \in (\hat {t} _ {l - 1} ^ {I I}, \hat {t} _ {l} ^ {I I} ], l \geq 2 \\ b _ {1}, i f v _ {i} \leq \hat {t} _ {1} ^ {I I} \end{array} \right.\tag{4}
$$

where $\hat { \beta } ^ { I }$ and $\hat { \beta } ^ { I I }$ correspond to the bidding strategy in the first round and second round, respectively, and $\hat { t } _ { k } ^ { I }$ and $\bar { \hat { t } } _ { k } ^ { I I }$ are series of critical points that partition the value space, $0 \stackrel { \because } { = } \hat { t } _ { 0 } ^ { I } < \hat { t } _ { 1 } ^ { I } <$ $\cdots \hat { t } _ { k } ^ { I } < \cdots \stackrel { \cdot } { < } \hat { t } _ { \hat { r } } ^ { I } = 1 , \stackrel { \cdot } { 0 } = \hat { t } _ { 0 } ^ { I I } < \hat { t } _ { 1 } ^ { I I } < \cdots \hat { t } _ { l } ^ { I I } < \cdots < \hat { t } _ { \hat { s } } ^ { I I } \stackrel { \cdot } { = } 1$ , and $1 \leq \hat { r } , \hat { s } \leq M$ . Similar to the sequential Dutch auction, we have the following proposition:

Proposition 2. Suppose two identical units are sold via the hybrid mechanism described above. If all the bidders have single-unit demand and they draw private values independently from a commonly known, continuous distribution ℱ on [0,1] and choose bids from the set $B =$ $\{ b _ { 1 } , b _ { 2 } , \dots b _ { M } \}$ where $b _ { j } = ( j - 1 ) / M , j = I , 2 , \ldots , M ,$ , there exist two series, $\{ \hat { t } _ { k } ^ { I } , k \geq 1 \}$ and $\{ \hat { t } _ { l } ^ { I I } , l \ge 1 \}$ , such that the bidding strategies defined by Equations (3) - (4) constitute a symmetric Bayesian Nash equilibrium.

The proof is analogous to the proof of Proposition 1, although the characterization of the strategic interaction in the first round is slightly more complicated, as the hybrid mechanism allows multiple winners.

Figure 1 illustrates the equilibrium bidding functions under the two mechanisms when ℱ is the uniform distribution, ?? ∈ {5,10}, and $N = 3$ . We can see that the bidding functions that correspond to the first and the second round are quite different under both mechanisms, i.e., $t _ { k } ^ { I } \neq t _ { l } ^ { I I }$ and $\hat { t } _ { k } ^ { I } \neq \hat { t } _ { l } ^ { I I }$ . In particular, low-value bidders tend to shade their bids more in the second round than in the first round, whereas high-value bidders tend to act in the opposite way (i.e., shade more in the first round than in the second round). Such a differential bidshading pattern is consistent across the two mechanisms.

## Comparison of Performance in Equilibrium

## Allocative Efficiency

Allocative efficiency—the degree to which items end up in the hands of the bidders who value them the most—is an important performance indicator of a selling mechanism. Following prior auction literature (Ausubel et al. 2014; Krishna 2009), we define allocative efficiency as the total surplus realized by trading parties (i.e., buyers and sellers) divided by the maximum surplus that could have been achieved. Formally, given an allocation scheme $\boldsymbol { x } = ( x _ { 1 } , \dots x _ { i } , \dots x _ { N } )$ , where $x _ { 1 } \in \{ 0 , 1 \}$ denotes whether Bidder ?? receives the item, the allocative efficiency, denoted by ??, is given by $\alpha = \textstyle \sum _ { i } x _ { i } v _ { i } / \operatorname* { m a x } _ { i } \{ v _ { i } \}$ Given the symmetric equilibrium strategies defined in Equations $( 1 ) ~ \textrm { - } ( 2 )$ and Equations $\textcircled { 3 } \textrm { - } \textcircled { 4 }$ , the following proposition describes the relative performance of the two mechanisms in terms of allocative efficiency.

Proposition 3. Consider an auction that sells two identical items to $N \left( N > 2 \right)$ bidders. Suppose all the bidders have single-unit demand; they draw private values independently from a commonly known, continuous distribution $\mathcal { F }$ on [0,1], and choose bids from the set $B = \{ b _ { 1 } , b _ { 2 } , \dots b _ { M } \}$ where $b _ { j } =$ $( j - 1 ) / M , j = I , 2 , \ldots , M .$ . Let ?? and ??̂ denote the average allocative efficiency under the traditional sequential Dutch auction mechanism and the hybrid mechanism, respectively. When the number of bid levels goes to infinity (i.e., bid increment goes to zero), the two mechanisms yield the same allocative efficiency, i.e., $\operatorname* { l i m } _ { M  \infty } ( \hat { \alpha } - \alpha ) = 0 \mathrm { . }$

![](/api/attachments/PUYV7N2F/fulltext/images/5ccfafb7903e97e7cb754bbc3ee7e7cf600fafd73775abdcf8c8ae2b1c5abde5.jpg)  
(a) Traditional Mechanism (M = 5)

![](/api/attachments/PUYV7N2F/fulltext/images/87c8b195b61be79e83603e03cde2b133abcb7daeaf8dc7a46dff442ec313457c.jpg)  
(c) Hybrid Mechanism (M = 5)

![](/api/attachments/PUYV7N2F/fulltext/images/b74d36637ba9a45d97fd5e9a483157793140c6e910e3c9781122777538566493.jpg)  
(b) Traditional Mechanism (M = 10)

![](/api/attachments/PUYV7N2F/fulltext/images/deb05532686a4a28549968a031c07dfbcbde07584ca71f6af0069dd4f61e7570.jpg)  
(d) Hybrid Mechanism (M = 10)

When ℱ is the uniform distribution, we plot the allocative efficiency under the two mechanisms in Figure 2. We can see that the variations of allocative efficiency under the two mechanisms closely resemble each other: as the number of bid levels increases (i.e., bid increment decreases), the allocative efficiency improves steadily; however, for any given finite bid level, as the number of bidders increases, the allocative efficiency will decrease.

It is worth noting that while the allocative efficiency of the hybrid mechanism is very close to that of the traditional mechanism in equilibrium for any large ?? (i.e., the bid increment is sufficiently small), the revenue ranking between the two mechanisms is ambiguous. Even in a simple threebidder, uniform distribution setting such as the one shown in Figure 1, depending on the realizations of the top two bidders’ values, the expected revenue under the hybrid mechanism could be either higher or lower than the traditional mechanism. Furthermore, due to the analytical intractability of the series that characterize the equilibrium bidding functions, i.e., {??<sup>??</sup> , ?? ≥ 1}, {??<sup>????</sup>, ?? ≥ 1}, {??̂<sup>??</sup> , ?? ≥ 1}, and {??̂<sup>????</sup>, ?? ≥ 1}, we cannot derive asymptotic properties of the expected revenues under the two mechanisms. Therefore, we leave the revenue comparison to the empirical analysis.

## Operational Efficiency

Drawing upon the study of Lu et al. (2019a), we use the number of rounds taken to complete the sale to measure the operational efficiency of a mechanism. Note that under the traditional sequential Dutch auction, it always takes two rounds to complete the sale. Under the hybrid mechanism, the number of rounds taken to finish the auction varies depending on the realization of bidders’ private values. However, we can prove that, on average, the number of rounds decreases when switching from the traditional mechanism to the hybrid mechanism.

Proposition 4. Given the same value distribution and bidders’ information structure described in Propositions 1- 3, the hybrid mechanism outperforms the traditional sequential Dutch auction in operational efficiency for any finite bid space (i.e., ?? < ∞).

To illustrate Proposition 4, consider auctions with three bidders whose private values are drawn independently from the uniform distribution defined on [0,1], i.e., ℱ\~Uniform[0,1] and ??=3. We plot the average number of rounds taken to complete the auction under the hybrid mechanism. The number of bid levels ?? takes the value from the set of {5, 10, 25, … 50}. For each value of ??, we generate 1,000 auctions and calculate the average number of rounds taken to complete these auctions. We then repeat this procedure 1,000 times, allowing us to obtain 1,000 values of the average and characterize its distribution for each value of ??. Figure 3 depicts the results of this process as a series of boxplots.

We can see that: (1) when the bid space is sparse (e.g., ?? = 5 or 10), the hybrid mechanism outperforms the traditional mechanism considerably in operational efficiency; (2) when the number of bid levels increases, the average number of rounds needed to finish the sale under the hybrid mechanism also increases but remains lower than two, suggesting that the hybrid mechanism yields a higher operational efficiency than the traditional mechanism.

## Empirical Analysis

Our theoretical analysis in the previous section suggests that, compared with the traditional sequential Dutch auction mechanism, the hybrid mechanism can achieve higher operational efficiency without compromising allocative efficiency. However, it is worth noting that some of the assumptions underlying the theoretical model are untenable in real-world markets. Specifically, bidders participating in sequential multi-unit auctions often have multi-unit demand rather than single-unit demand (Goes et al. 2012; Lu et al. 2016), and their private values may be drawn from different distributions (Hortaçsu and McAdams 2010). Also, bidders are likely to adopt simple heuristics that deviate from the equilibrium strategy (Lu et al. 2019). To account for these real-world complications, we conducted a large-scale quasinatural field experiment in the Dutch Flower Auctions (DFA) to further evaluate the hybrid mechanism.

## The Dutch Flower Auctions

DFA account for more than half of the global floriculture trade. They facilitate trades of over 30,000 species of flowers and plants, generating an annual turnover of €4.6 billion.<sup>6</sup> The high economic stakes involved in these transactions make it important to carefully evaluate the revenue and efficiency implications of alternative mechanisms. DFA use a traditional sequential Dutch auction mechanism, which is implemented with a fast-running clock displayed on a projection screen.<sup>7</sup>

![](/api/attachments/PUYV7N2F/fulltext/images/f8611802a3d97fa0849986d7a849741a66f483d240893469f8802ae89bb2ccce.jpg)  
(a) Traditional Mechanism

![](/api/attachments/PUYV7N2F/fulltext/images/3f4ff6a8d6895f086b84a9c5615c013996908d83a4f8184169460b85ad0b5a99.jpg)  
(b) Hybrid Mechanism  
Figure 2. Comparison of Allocative Efficiency (??\~ [??, ??])

![](/api/attachments/PUYV7N2F/fulltext/images/5e46305d67eb92551a116cf63701f067ae6c8d59f081bcc13be4fcbb20c1ec72.jpg)  
Figure 3. Operational Efficiency under Hybrid Mechanism (??\~ [??, ??]; ??=3)

![](/api/attachments/PUYV7N2F/fulltext/images/341f4e1e08dfeb6a45bdc51d5af7f1be7311d5234d17bed7e44ba0eb6ef09717.jpg)  
Figure 4. A Set of Four Dutch Flower Auctions (Source: Royal FloraHolland)

Figure 4 shows four auction clocks running simultaneously in an auction hall. Besides the current asking price, which is discrete and indicated by the red dot on the clock screen, each clock screen also displays information about the grower (supplier), the product (e.g., the category, the quality, the maturity level, and the bundling conditions), the current available units, the price per tick (i.e., the bid increment), and the minimum purchase units.

Traditionally, bidders had to come to the auction halls to participate in the auctions on weekdays from 6:30 AM to 10:30 AM. With the introduction of the remote bidding system, bidders can purchase all the auctioned products online from their own workstations anywhere in the world. Over the past decade, the digital transformation of the floriculture industry has greatly increased the efficiency of the market processes in DFA. However, it also creates new challenges. For example, the reduction of transaction cost makes it much easier for producers of horticultural goods to bypass the auction market—which often suffers from congestion especially during peak days (e.g., Valentine’s Day, Mother’s Day)—and sell directly to wholesalers, retailers, and even end customers, which could significantly reduce revenue. Furthermore, the mechanism (i.e., the sequential Dutch auction mechanism) that facilitates the trading process has barely evolved to accommodate the emerging needs from both the supply and demand sides, and there is a growing concern about its viability in the midst of radical changes in the business environment.<sup>8</sup> Consistent with the initiatives taken by the market maker of DFA to reinvent the auction process, our current research explores the potential of an alternative mechanism that aims to mitigate the congestion problem pertinent to the traditional sequential Dutch auction mechanism.

## Experimental Design

We conducted a large-scale quasi-natural field experiment in early 2016. The hybrid mechanism was implemented on three clocks that auctioned potted plants at a major auction site (i.e., treatment site) and the transaction data were collected from January 21 to February 11, 2016. The experiment manipulation is illustrated in Figure 5.

![](/api/attachments/PUYV7N2F/fulltext/images/8ac683419535a95884beb26b42c08219ac94d9fcabe99688469d92fc5f2a4427.jpg)  
Figure 5. Illustration of the Experiment Manipulation

![](/api/attachments/PUYV7N2F/fulltext/images/0513454de75d73bc013827da63b6150f702392a64b0c254ef2e5e3079a45a074.jpg)  
Figure 6. Overview of the Experiment Design

When there is only one bidder that submits the highest bid, the hybrid mechanism works exactly the same as the traditional sequential Dutch auction mechanism. However, when there are multiple bidders that submit the highest bid, the hybrid mechanism awards multiple winners: in our case, both Bidder A and Bidder B would fulfill their demand in the current round of the auction,<sup>9</sup> as opposed to the situation under the traditional mechanism where only Bidder A would be the winner.

To quantify the impact of the mechanism change on sellers’ revenue and market processes, we also obtained (1) transaction data from the treatment site between December 17, 2015 and January 7, 2016, which was prior to the mechanism change,<sup>10</sup> and (2) transaction data from a nearby auction site (i.e., the control site), where the same types of products were sold via the traditional sequential Dutch auction mechanism during the entire pre-experiment and experiment period. Figure 6 summarizes our experimental design. Compared with a simple before-after experimental design that restricts attention to the treatment site, the incorporation of transaction data from a control site allows us to rule out potential confounding factors associated with systematic changes in supply or demand during the experiment period (Shadish et al. 2002).

Before moving to the econometric analysis of the experimental data, we briefly discuss the choice of the treatment and the control sites. Currently, the market maker of DFA, Royal FloraHolland, operates four auction sites throughout the country. The treatment site and the control site are among the largest in terms of the number of bidders served and the average number of daily transactions. Apart from their geolocations, the two sites share several commonalities. First, both sites have adopted the digital auctioning system where the physical auction clocks are replaced by projection screens. Second, the product assortments at the two sites are quite similar. In fact, many of the large growers offer their products for sale at both sites. Third, both sites provide excellent facilities for both suppliers and customers to ensure efficient transportation and delivery of products. It is worth noting that while bidders can freely choose to buy from any of the auction sites, most bidders tend to buy from the site closest to their distribution centers to ensure logistics efficiency; many large wholesalers even own commercial properties such as office buildings around the chosen site.<sup>11</sup> Such location dependence disincentivizes bidders to switch between the treatment site and control site during the experiment period and alleviates concerns about a potential selection bias.

## Data and Descriptive Analysis

As explained earlier, we collected transaction data from auctions of potted plants at the treatment site and control sites during the pre-experiment and experiment period. In addition to purchase price and quantity, each transaction consists of the following information: (1) transaction ID and timestamp (date and time); (2) product specification, which includes product category, main characteristics, and quality information; (3) supply-side information (e.g., the available quantity of the product prior to the transaction, the minimum purchase quantity, grower information, and packaging specifications); (4) clock configuration information (e.g., price per tick); (5) logistics information; (6) buyer’s information, which includes the buyer’s name, identity, and the bidding channel (i.e., whether the buyer was bidding on-site or remotely).

Table 1 and Table 2 provide stylized examples of transactions under the traditional sequential Dutch auction mechanism and the hybrid mechanism, respectively. Due to space limits, we did not include all the attributes in a transaction log. The first thing to note from these tables is that each transaction takes only a few seconds under both mechanisms, although the hybrid mechanism pushes the limit even further by including additional purchase opportunities in each round. Furthermore, for a given bundle of homogeneous products (i.e., Product ID: 14016; Grower ID: 282660), the winning price can vary significantly across different transactions.

After combining all the transactions during the pre-experiment and experiment period from both sites, we had a total of 170,094 transactions from 48,648 auctions, with 81,958 transactions (20,197 auctions) from the treatment site and 88,136 transactions (28,451 auctions) from the control site. To control for unobservable heterogeneity from the supply side, we matched the product categories across the two sites and excluded products with a transaction volume of less than 0.5% of the total transaction. After the matching, we were left with a total of 160,822 transactions from 46,216 auctions, of which 77,133 transactions (19,126 auctions) were from the treatment site and 83,689 transactions (27,090 auctions) were from the control site.

Prior to formal analysis, we present some model-free evidence about the impact of the mechanism change on auction-level outcomes. Table 3 and Table 4 provide the summary statistics of the auction-level outcome variables from the treatment site and the control site, respectively. For the treatment site, we can see that from the pre-experiment to the experiment period: (1) the weighted average price increased, whereas the price range and standard deviation of price decreased; (2) the number of rounds taken to complete an auction decreased; (3) the average purchase quantity increased, whereas the standard deviation of purchase quantity did not vary much. For the control site, we observe that: (1) the weighted average price, price range, and standard deviation of price showed similar (yet less salient) trends as those from the treatment site from the pre-experiment to the experiment period; (2) the number of rounds taken to complete an auction did not vary much; (3) both the average purchase quantity and the standard deviation of purchase quantity decreased.

Among the six auction-level outcome variables presented in Tables 3 and 4, we are most interested in the weighted average price and the number of rounds, as they serve as good measures of seller’s revenue and operational efficiency, respectively. Therefore, we also plotted their distributions. According to Figure 7, the price distributions are quite similar throughout the two time periods at both sites, while the distribution of the number of rounds shifts to the left and becomes narrower from the pre-experiment to the experiment period at the treatment site.

Taken together, these observations suggest that the mechanism change had a positive impact in terms of operational efficiency. However, since these model-free results do not account for any potential confounding factors from the supply and demand sides (for example, suppliers’ reputation or buyers’ channel adoption and usage), they could be biased or misleading.

Table 1. A Stylized Transaction Log under the Traditional Mechanism

<table><tr><td>Transaction time</td><td>Product ID</td><td>Grower ID</td><td>Available quantity</td><td>Minimum purchase quantity</td><td>Bidder ID</td><td>Purchase quantity</td><td>Price (euro)</td><td>Online</td></tr><tr><td>7:06:41</td><td>14016</td><td>282660</td><td>18</td><td>1</td><td>501</td><td>2</td><td>27.00</td><td>Yes</td></tr><tr><td>7:06:43</td><td>14016</td><td>282660</td><td>16</td><td>1</td><td>332</td><td>5</td><td>23.00</td><td>Yes</td></tr><tr><td>7:06:44</td><td>14016</td><td>282660</td><td>11</td><td>3</td><td>945</td><td>7</td><td>21.00</td><td>No</td></tr><tr><td>7:06:46</td><td>14016</td><td>282660</td><td>4</td><td>4</td><td>202</td><td>4</td><td>22.00</td><td>Yes</td></tr></table>

Table 2. A Stylized Transaction Log under the Hybrid Mechanism

<table><tr><td>Transaction time</td><td>Product ID</td><td>Grower ID</td><td>Available quantity</td><td>Minimum purchase quantity</td><td>Bidder ID</td><td>Purchase quantity</td><td>Price</td><td>Online</td></tr><tr><td>7:23:39</td><td>14016</td><td>282660</td><td>20</td><td>1</td><td>1847</td><td>6</td><td>26.00</td><td>No</td></tr><tr><td>7:23:39</td><td>14016</td><td>282660</td><td>14</td><td>1</td><td>1880</td><td>4</td><td>26.00</td><td>Yes</td></tr><tr><td>7:23:39</td><td>14016</td><td>282660</td><td>10</td><td>1</td><td>1792</td><td>5</td><td>26.00</td><td>Yes</td></tr><tr><td>7:23:41</td><td>14016</td><td>282660</td><td>5</td><td>4</td><td>1811</td><td>5</td><td>24.00</td><td>Yes</td></tr></table>

Table 3. Auction-Level Summary Statistics from the Treatment Site

<table><tr><td colspan="2">Variables</td><td>Mean</td><td>Median</td><td>S.D.</td><td>Min.</td><td>Max.</td></tr><tr><td rowspan="2">Weighted average price</td><td>Pre-exp.</td><td>20.4</td><td>14.0</td><td>19.8</td><td>0.6</td><td>198.4</td></tr><tr><td>Exp.</td><td>23.3</td><td>15.8</td><td>23.9</td><td>0.7</td><td>470.0</td></tr><tr><td rowspan="2">Price range</td><td>Pre-exp.</td><td>3.6</td><td>2.0</td><td>7.5</td><td>0.1</td><td>420.0</td></tr><tr><td>Exp.</td><td>2.4</td><td>1.2</td><td>3.7</td><td>0.1</td><td>78.0</td></tr><tr><td rowspan="2">S.D. of price</td><td>Pre-exp.</td><td>1.6</td><td>0.8</td><td>2.8</td><td>0.03</td><td>124.9</td></tr><tr><td>Exp.</td><td>1.1</td><td>0.6</td><td>1.8</td><td>0.02</td><td>45.3</td></tr><tr><td rowspan="2">Number of rounds</td><td>Pre-exp.</td><td>4.0</td><td>4.0</td><td>2.6</td><td>1.0</td><td>26.0</td></tr><tr><td>Exp.</td><td>3.5</td><td>3.0</td><td>2.0</td><td>1.0</td><td>16.0</td></tr><tr><td rowspan="2">Average purchase quantity</td><td>Pre-exp.</td><td>12.9</td><td>8.0</td><td>15.5</td><td>1.0</td><td>192.0</td></tr><tr><td>Exp.</td><td>13.6</td><td>8.0</td><td>15.7</td><td>1.0</td><td>168.0</td></tr><tr><td rowspan="2">S.D. of purchase quantity</td><td>Pre-exp.</td><td>6.3</td><td>4.0</td><td>6.6</td><td>0.4</td><td>89.1</td></tr><tr><td>Exp.</td><td>6.4</td><td>4.0</td><td>7.3</td><td>0.4</td><td>94.0</td></tr></table>

Table 4. Auction-Level Summary Statistics from the Control Site

<table><tr><td colspan="2">Variables</td><td>Mean</td><td>Median</td><td>S.D.</td><td>Min.</td><td>Max.</td></tr><tr><td rowspan="2">Weighted average price</td><td>Pre-exp.</td><td>21.9</td><td>16.0</td><td>24.1</td><td>0.7</td><td>436.2</td></tr><tr><td>Exp.</td><td>22.5</td><td>16.4</td><td>24.4</td><td>0.9</td><td>1116.7</td></tr><tr><td rowspan="2">Price range</td><td>Pre-exp.</td><td>2.9</td><td>1.5</td><td>4.9</td><td>0.1</td><td>90.0</td></tr><tr><td>Exp.</td><td>2.4</td><td>1.2</td><td>3.7</td><td>0.1</td><td>78.0</td></tr><tr><td rowspan="2">S.D. of price</td><td>Pre-exp.</td><td>1.4</td><td>0.7</td><td>2.5</td><td>0.03</td><td>53.2</td></tr><tr><td>Exp.</td><td>1.1</td><td>0.6</td><td>1.8</td><td>0.02</td><td>45.3</td></tr><tr><td rowspan="2">Number of Rounds</td><td>Pre-exp.</td><td>3.0</td><td>3.0</td><td>1.9</td><td>1.0</td><td>17.0</td></tr><tr><td>Exp.</td><td>3.1</td><td>3.0</td><td>1.9</td><td>1.0</td><td>16.0</td></tr><tr><td rowspan="2">average purchase quantity</td><td>Pre-exp.</td><td>16.4</td><td>11.0</td><td>17.4</td><td>1.0</td><td>283.0</td></tr><tr><td>Exp.</td><td>13.6</td><td>8.0</td><td>15.7</td><td>1.0</td><td>168.0</td></tr><tr><td rowspan="2">S.D. of purchase quantity</td><td>Pre-exp.</td><td>7.0</td><td>4.5</td><td>7.9</td><td>0.4</td><td>190.9</td></tr><tr><td>Exp.</td><td>6.4</td><td>4.0</td><td>7.3</td><td>0.4</td><td>94.0</td></tr></table>

![](/api/attachments/PUYV7N2F/fulltext/images/fd5ba028edfa71a306d722aaad34a105d411a88ed2f552275c1a75281a2768fb.jpg)  
(a) Weighted Average Price  
Figure 7. Distributions of Auction-Level Outcome Variables

![](/api/attachments/PUYV7N2F/fulltext/images/2919f80dd248dd4c619f5e79c05967c5b10a7ba8d32271ad6b0c98275f19b27b.jpg)  
(b) Number of Rounds

## Identification Strategy

To quantify the effect of the mechanism change on market processes and outcomes, we adopted a difference-indifferences (DID) strategy (Angrist and Pischke, 2008). DID estimators have been widely used to make causal inferences with observational data collected from natural experiments (Card and Krueger 1994; Huang et al. 2017) or quasi-natural experiments (Lu et al. 2019) where the experiment treatment (e.g., policy change) cannot be randomly assigned. In our case, given the institutional setup of DFA, it is not possible to randomly assign the treatment to either auctions or bidders.

We used individual auctions as the unit of analysis and focused on two key performance indicators, the weighted average of the winning price in each round and the number of rounds taken to complete an auction. The former is used to measure revenue performance, whereas the latter is used to measure operational efficiency. To reduce the skewness of the distributions (see Figure 7), we took the natural logtransformations of these two variables. Our model specifications are as follows:

$$
\begin{array}{c} \ln \left(\text { WeightedAvgPrice } _ {i, t}\right) = \\ \beta_ {0} + \beta_ {1} \text { Treatment } _ {i} \times \text { Post } _ {t} + \beta_ {2} \text { Treatment } _ {i} + \theta_ {t} + \gamma \mathbf {X} _ {i, t} + \epsilon_ {i, t} \end{array} \tag {5}
$$

$$
\begin{array}{c} \ln (\text { NumberOfRounds } _ {i, t}) = \\ \beta_ {0} + \beta_ {1} \text { Treatment } _ {i} \times \text { Post } _ {t} + \beta_ {2} \text { Treatment } _ {i} + \theta_ {t} + \gamma \mathbf {X} _ {i, t} + \epsilon_ {i, t} \end{array} \tag {6}\tag{6}
$$

In Equations (5) - (6), ?? indexes auctions, and t indexes the transaction time (week) in the study period. ?????????????????? is a dummy variable that equals 1 if the auction was at the treatment site and 0 if it was at the control site. $P o s t _ { t }$ is a dummy variable that equals 1 if the auction was conducted during the experiment period and 0 otherwise. The week-fixed effects $\theta _ { t }$ were included as non-parametric controls for the temporal variations that are common at both the treatment site and control site. $\mathbf { X } _ { i , t }$ is a vector of control variables, including the product characteristics ProductCode, PotSize, MinimumPlantHeight, and MinimumNumberPlants. ProductCode describes the product category, PotSize specifies the size (diameter) of the pot that the plant comes in, MinimumPlantHeight specifies the smallest plant in a bundle up for auction (also referred to as a “lot”), and MinimumNumberPlants describes the minimum number of plants per pot of the products offered in a lot. To account for supply-side heterogeneity, we also included LotSize (i.e., the total available units in a lot), Packaging (i.e., how the potted plants are packaged), and a series of grower dummies. Finally, since market demand varies across different days of a week (e.g., market demand is typically higher on Fridays than on Thursdays because end customers typically purchase more floriculture products on weekends), we also controlled for the day of the week on which the auction occurred.

Our coefficient of interest is $\beta _ { 1 }$ . It captures the effect of the mechanism change on the treatment site. Specifically, a positive value of the coefficient in Equation (5) would indicate that the hybrid mechanism at the treatment site generates higher revenue, as compared to the control site where the traditional mechanism was used. Similarly, a negative value of $\beta _ { 1 }$ in Equation (6) would suggest that the hybrid mechanism reduces the total number of rounds taken to complete an auction and thereby leads to a higher market clearing speed.

## Estimation Results

## Main Findings

Table 5 summarizes the estimation results using the model specifications in Equations (5) - (6). For the revenue measure, i.e., ln(????????ℎ??????????????????????), the coefficient for the interaction term Treatment × Post is statistically insignificant, indicating that the mechanism change had no significant effect on the revenue. However, we note that the estimated coefficient for the dummy variable ?????????????????? is significant. Specifically, the weighted average price at the treatment site was 6% lower than that of the control site. This suggests that there exist systematic differences in price levels between the treatment site and control site. Compared with our observations from Table 3, these findings reinforce the notion that model-free evidence could be misleading. As for the control variables, we observe that both LotSize and PotSize had a negative impact on the weighted average price, whereas MinimumPlantHeight had a positive impact on the weighted average price.

For the efficiency measure, i.e., ln(????????????????????????????), we observe that the coefficient corresponding to the treatment effect is negative (-0.177) and statistically significant (p-value < 0.001), indicating that the mechanism change significantly reduced the number of rounds taken to conclude an auction and thereby increased the operational efficiency. Note that an improvement in operational efficiency not only benefits the buyers but also the sellers (growers) in the market. For buyers, it reduces their monitoring cost and allows them to quickly proceed to the next auction that offers similar products if their demand is not fulfilled in the current auction. For sellers, the increased speed of individual auctions can translate into a reduction in lead times and a faster turnaround for perishable products to reach their destinations. It also opens space in the daily schedule to auction more products.

## The Parallel Trend Assumption

A key assumption underlying the validity of the DID identification is the parallel trend assumption, that is, the differences in revenue and efficiency between the treatment and control site would remain constant over time in the absence of the mechanism change (Angrist and Pischke 2008). To examine the pre-experiment trends at the two sites, we used a relativetime model (Card and Krueger 1994; Greenwood and Wattal 2017). In particular, we used the last week of the pre-experiment period, denoted by $P r e _ { ( - 1 ) }$ , as the baseline (i.e., January 4-7, 2016), and created additional indicator variables that correspond to the first, second, and third week in the preexperiment period (i.e., $P r e _ { ( - 4 ) } , P r e _ { ( - 3 ) }$ , and $P r e _ { ( - 2 ) } )$ and the three weeks in the experiment period $( \mathrm { i . e . , } P o s t _ { ( 0 ) } , P o s t _ { ( + 1 ) }$ , and $P o s t _ { ( + 2 ) } )$ . We then reestimated the DID models specified in Equations (5) - (6) by replacing the dummy variable ???????? with these relative time indicator variables. Table 6 reports the estimation results.

For both outcome variables, ln(????????ℎ??????????????????????) and ln(????????????????????????????), the coefficients corresponding to the pre-treatment trends are statistically insignificant, suggesting that the parallel trend assumption is not violated. In addition, the results from Table 6 suggest the mechanism change did not affect the revenue, as none of the coefficients that capture the treatment effects on the outcome variable ln(????????ℎ??????????????????????) are significant. By contrast, the estimated coefficients corresponding to the treatment effects on ln(????????????????????????????) are all negative (−0.123, −0.237, and −0.162) and significant (p-value < 0.001), indicating that the number of rounds taken to finish an auction decreased significantly after the mechanism change.

## Robustness Checks

We performed various other tests to assess the robustness of the observed treatment effects. To start with, since not all bidders participated in the auctions throughout the study period—some bidders only participated in auctions during the pre-experiment period, whereas others only bid during the experiment period. As a result, the observed treatment effects on revenue and efficiency may be due to the changes in the bidder population during the pre-experiment and experiment periods. Specifically, if the bidder population exposed to the treatment varied during the three-week experiment period, the observed improvement in operational efficiency may be attributable to the novelty effect (Robey 1979).

Table 5. Effect of Mechanism Change on Revenue and Operational Efficiency

<table><tr><td>Variables</td><td>ln(WeightedAvgPrice)</td><td>ln(NumberOfRounds)</td></tr><tr><td>Treatment × Post</td><td>0.002(0.007)</td><td>-0.177 ***(0.010)</td></tr><tr><td>Treatment</td><td>-0.060 ***(0.005)</td><td>0.190 ***(0.007)</td></tr><tr><td>LotSize</td><td>-0.002 ***(0.0001)</td><td>0.010 ***(0.0001)</td></tr><tr><td>PotSize</td><td>-0.0008 ***(0.00003)</td><td>-0.0003 ***(0.00004)</td></tr><tr><td>MinimumPlantHeight</td><td>0.005 ***(0.0001)</td><td>-0.001 ***(0.0001)</td></tr><tr><td>MinimumNumberPlants</td><td>0.00005 *(0.00002)</td><td>0.00005(0.00003)</td></tr><tr><td>Packaging</td><td>-0.029 ***(0.0004)</td><td>0.0004(0.0005)</td></tr><tr><td>Weekday-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Grower-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>ProductCode-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Week-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>46,216</td><td>46,216</td></tr><tr><td>Adjusted R-squared</td><td>0.857</td><td>0.428</td></tr></table>

Note: Robust standard errors in parentheses. \*\*\*?? < 0.001, $^ { \overline { { { \star \star } _ { p } < 0 . 0 1 , } } }$ \*?? < 0.05

<table><tr><td>Variables</td><td>ln(WeightedAvgPrice)</td><td>ln(NumberOfRounds)</td></tr><tr><td>Treatment × Pre(-4)</td><td>-0.003(0.015)</td><td>0.022(0.020)</td></tr><tr><td>Treatment × Pre(-3)</td><td>0.007(0.013)</td><td>-0.005(0.017)</td></tr><tr><td>Treatment × Pre(-2)</td><td>0.008(0.014)</td><td>-0.030(0.018)</td></tr><tr><td>Treatment × Post(0)</td><td>-0.006(0.013)</td><td>-0.123 ***(0.018)</td></tr><tr><td>Treatment × Post(+1)</td><td>0.002(0.012)</td><td>-0.237 ***(0.016)</td></tr><tr><td>Treatment × Post(+2)</td><td>0.008(0.013)</td><td>-0.162***(0.017)</td></tr><tr><td>Treatment</td><td>-0.063 ***(0.009)</td><td>0.194 ***(0.012)</td></tr><tr><td>Pre(-4)</td><td>-0.061***(0.011)</td><td>-0.012(0.015)</td></tr><tr><td>Pre(-3)</td><td>-0.231 ***(0.009)</td><td>-0.103 ***(0.011)</td></tr><tr><td>Pre(-2)</td><td>-0.073 ***(0.009)</td><td>-0.012(0.012)</td></tr><tr><td>Post(0)</td><td>-0.067***(0.009)</td><td>-0.033 **(0.012)</td></tr><tr><td>Post(+1)</td><td>0.105 ***(0.008)</td><td>0.003(0.011)</td></tr><tr><td>Post(+2)</td><td>0.018 *(0.008)</td><td>-0.038 ***(0.011)</td></tr><tr><td>LotSize</td><td>-0.002 ***(0.0001)</td><td>0.010 ***(0.0001)</td></tr><tr><td>PotSize</td><td>-0.0007 ***(0.00003)</td><td>-0.0003 ***(0.00004)</td></tr><tr><td>MinimumPlantHeight</td><td>0.005 ***(0.0001)</td><td>-0.001 ***(0.0001)</td></tr><tr><td>MinimumNumberPlants</td><td>0.00005 *(0.00002)</td><td>0.00005(0.00003)</td></tr><tr><td>Packaging</td><td>-0.029 ***(0.0004)</td><td>0.0004(0.0005)</td></tr><tr><td>Weekday-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Grower-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>ProductCode-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>46,216</td><td>46,216</td></tr><tr><td>Adjusted R-squared</td><td>0.856</td><td>0.429</td></tr></table>

Note: Robust standard errors in parentheses. \*\*\*?? < 0.001, \*\*?? < 0.01, \*?? < 0.05

Furthermore, since bidders in these auctions are typically representing their firms, their willingness to pay is associated with the profits they could make should they win, or the severity of the consequences should they lose. As such, the efficiency gain may result from risk aversion—that is, bidders exposed to the mechanism change happened to be more risk averse than those competing under the traditional mechanism.

To test for these alternative explanations to our main findings presented earlier, we created a subsample that only included the transactions from active bidders that participated during the entire study period. We then estimated the DID models specified in Equations (5) - (6), and two augmented models that included a bidder-fixed effect. If the observed treatment effects were primarily driven by the change in the bidder population, we would observe significant changes in the estimates for the interaction terms. Table 7 summarizes the estimation results. Overall, the estimates from the subsample of active bidders are largely consistent with our main findings from Table 5. Thus, we can rule out the alternative explanations discussed above.

Next, given the large price dispersion of products sold through the auctions (see Table 3 and Table 4), we would like to know whether the observed effect of the mechanism change varies across products within different price ranges. We sorted different products based on their average prices and created two subsamples, one consisting of the top 30% of products, and the other consisting of the bottom 30%. The former consisted of 14,899 transactions, whereas the latter consisted of 12,815 transactions. We reestimated the models specified in Equations (5) - (6) using the two subsamples, respectively. The results are reported in Table 8.

According to Table 8, the mechanism change has opposite revenue effects on high-end and low-end products: the weighted average price increased by 3.4% for low-end products but decreased by 1.7% for high-end products. For the efficiency measure, i.e., ln(????????????????????????????), the estimates in Table 8 indicate that while the mechanism change significantly reduced the number of rounds taken to conclude an auction for both high-end and low-end products, the effect size is greater for high-end products than for low-end products.

Another concern is that although we have accounted for much of the unobserved heterogeneity through the controls and fixed effects in the model specifications in Equations (5) - (6), the auctions from the control site may nevertheless not serve as perfect counterfactuals for those from the treated site. To address this concern, we used coarsened exact matching (Iacus et al. 2012) to further limit the ex ante differences between the transactions from the treatment and control sites. Specifically, we first matched the transactions on product and lot characteristics. We then replicated the DID estimation using the matched sample. Table 9 provides the estimation results. We can see that the mechanism change had an insignificant effect on the revenue but a strong and significant effect on the operational efficiency. Overall, the results are largely consistent with those from Table 5.

Finally, we conducted a falsification test to rule out the possibility that the observed treatment effect on operational efficiency was due to spurious correlation. To do so, we randomly assigned an auction to the experiment period and reestimated the model specified in Equations (5) - (6). Since the dummy variable ???????? no longer reflects the actual treatment assignment, we refer to such random assignment as a “placebo” treatment. We repeated the estimation procedure with the “placebo” treatment 1,000 times. Table 10 shows the mean and standard deviation of the coefficient (??<sup>′</sup>) capturing the “placebo” effect on revenue and efficiency. The estimated coefficients associated with the “placebo” treatment are not significantly different from zero, suggesting that our main findings presented in Table 5 were not driven by pure coincidence. Specifically, while it is quite likely that we would observe a similar coefficient in Table 10 to the coefficient in Table 5 purely by chance for the revenue measure,<sup>12</sup> the probability of obtaining a similar coefficient to the one in Table 5 for the efficiency measure purely by chance is extremely low (p-value < 0.001).

Table 7. Revenue and Efficiency Effects on the Subsample of Active Bidders

<table><tr><td rowspan="2">Variables</td><td colspan="2">In(WeightedAvgPrice)</td><td colspan="2">In(NumberOfRounds)</td></tr><tr><td>Base</td><td>Augmented</td><td>Base</td><td>Augmented</td></tr><tr><td>Treatment × Post</td><td>0.004(0.008)</td><td>0.004(0.008)</td><td>-0.161 ***(0.010)</td><td>-0.140 ***(0.009)</td></tr><tr><td>Treatment</td><td>-0.058 ***(0.005)</td><td>-0.059 ***(0.014)</td><td>0.171 ***(0.007)</td><td>0.197 ***(0.018)</td></tr><tr><td>LotSize</td><td>-0.002 ***(0.0001)</td><td>-0.002 ***(0.0001)</td><td>0.010 ***(0.0001)</td><td>0.009 ***(0.0001)</td></tr><tr><td>PotSize</td><td>-0.0008 ***(0.00003)</td><td>-0.0008 ***(0.00003)</td><td>-0.0002 ***(0.00004)</td><td>-0.0003 ***(0.00004)</td></tr><tr><td>MinimumPlantHeight</td><td>0.005 ***(0.0001)</td><td>0.005 ***(0.0001)</td><td>-0.001 ***(0.0001)</td><td>-0.001 ***(0.0001)</td></tr><tr><td>MinimumNumberPlants</td><td>0.00005 *(0.00002)</td><td>0.00005 *(0.00002)</td><td>0.00006(0.00003)</td><td>0.0001 ***(0.00003)</td></tr><tr><td>Packaging</td><td>-0.028 ***(0.0004)</td><td>-0.027 ***(0.0004)</td><td>0.00003(0.00005)</td><td>-0.00001(0.00005)</td></tr><tr><td>Weekday-fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Grower-fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>ProductCode -fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Week-fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Bidder-fixed effect</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Observations</td><td>44,925</td><td>44,925</td><td>44,925</td><td>44,925</td></tr><tr><td>Adjusted R-squared</td><td>0.856</td><td>0.863</td><td>0.424</td><td>0.525</td></tr></table>

Note: Columns denoted by Base show the estimation results corresponding to the model specifications in Equations (5) - (6), whereas Columns denoted by Augmented show the results under the augmented models (including bidder fixed effect). Robust standard errors in parentheses. \*\*\*?? < 0.001, \*\*?? < 0.01, \*?? < 0.05

Table 8. Revenue and Efficiency Effects on High- and Low-end Products

<table><tr><td rowspan="2">Variables</td><td colspan="2">ln(WeightedAvgPrice)</td><td colspan="2">ln(NumberOfRounds)</td></tr><tr><td>High-end</td><td>Low-end</td><td>High-end</td><td>Low-end</td></tr><tr><td>Treatment × Post</td><td>-0.017*(0.007)</td><td>0.034***(0.010)</td><td>-0.206***(0.017)</td><td>-0.118***(0.018)</td></tr><tr><td>Treatment</td><td>-0.007(0.005)</td><td>-0.061***(0.007)</td><td>0.212***(0.013)</td><td>0.144***(0.013)</td></tr><tr><td>LotSize</td><td>-0.001***(0.0001)</td><td>-0.001***(0.0001)</td><td>0.011***(0.0003)</td><td>0.008***(0.0002)</td></tr><tr><td>PotSize</td><td>0.006***(0.0004)</td><td>0.0001***(0.00003)</td><td>-0.003***(0.0009)</td><td>-0.0002***(0.00005)</td></tr><tr><td>MinimumPlantHeight</td><td>0.004***(0.0001)</td><td>-0.0008***(0.0001)</td><td>-0.003***(0.0003)</td><td>-0.0002(0.0002)</td></tr><tr><td>MinimumNumberPlants</td><td>0.0002***(0.00004)</td><td>0.0007***(0.00004)</td><td>0.0003**(0.0001)</td><td>-0.0002**(0.00008)</td></tr><tr><td>Packaging</td><td>-0.053***(0.001)</td><td>-0.009***(0.0003)</td><td>0.001(0.003)</td><td>0.002***(0.0006)</td></tr><tr><td>Weekday-fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Grower-fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>ProductCode-fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Week-fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>14,899</td><td>12,815</td><td>14,899</td><td>12,815</td></tr><tr><td>Adjusted R-squared</td><td>0.701</td><td>0.624</td><td>0.374</td><td>0.456</td></tr></table>

Note: Robust standard errors in parentheses. \*\*\*?? < 0.001, \*\*?? < 0.01, \*?? < 0.05

<table><tr><td colspan="3">Table 9. Effect of Mechanism Change on the Matched Sample</td></tr><tr><td>Variables</td><td> $\ln(WeightedAvgPrice)$ </td><td> $\ln(NumberOfRounds)$ </td></tr><tr><td>Treatment × Post</td><td>0.001(0.008)</td><td>-0.181 ***(0.014)</td></tr><tr><td>Treatment</td><td>-0.041 ***(0.005)</td><td>0.199 ***(0.010)</td></tr><tr><td>LotSize</td><td>-0.003 ***(0.0002)</td><td>0.013***(0.0004)</td></tr><tr><td>PotSize</td><td>0.00005(0.00004)</td><td>-0.0004 ***(0.0001)</td></tr><tr><td>MinimumPlantHeight</td><td>0.010 ***(0.0003)</td><td>-0.002 ***(0.001)</td></tr><tr><td>MinimumNumberPlants</td><td>-0.0002 *(0.00003)</td><td>-0.0002***(0.0001)</td></tr><tr><td>Packaging</td><td>-0.079 ***(0.001)</td><td>-0.006***(0.001)</td></tr><tr><td>Weekday-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Grower-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>ProductCode-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Week-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>20,136</td><td>20,136</td></tr><tr><td>Adjusted R-squared</td><td>0.926</td><td>0.379</td></tr></table>

Note: Robust standard errors in parentheses. \*\*\*?? < 0.001, \*\*?? < 0.01, \*?? < 0.05

<table><tr><td colspan="3">Table 10. Results of Falsification Test</td></tr><tr><td></td><td>ln(WeightedAvgPrice)</td><td>ln(NumberOfRounds)</td></tr><tr><td>Mean of  $\beta_1'$ </td><td>0.0002</td><td>0.000098</td></tr><tr><td>S.D. of  $\beta_1'$ </td><td>0.006</td><td>0.0082</td></tr><tr><td> $\beta_1$ </td><td>0.002</td><td>-0.177</td></tr><tr><td>Z-score</td><td>0.77</td><td>560.03</td></tr><tr><td>p-value</td><td>0.44</td><td>&lt;0.001</td></tr></table>

Note: $\beta _ { 1 } ^ { \prime }$ denotes the estimated coefficient associated with the “placebo” treatment; $\beta _ { 1 }$ denotes the original estimate associated with the actual treatment.

<table><tr><td colspan="3">Table 11. Treatment Effect on Price Dispersion</td></tr><tr><td>Variables</td><td>ln(PriceRange)</td><td>ln(S.D.ofPrice)</td></tr><tr><td>Treatment × Post</td><td>-0.270 ***(0.019)</td><td>-0.205 ***(0.042)</td></tr><tr><td>Treatment</td><td>0.178 ***(0.014)</td><td>0.123 ***(0.031)</td></tr><tr><td>LotSize</td><td>0.002 ***(0.0003)</td><td>-0.001 *(0.0006)</td></tr><tr><td>PotSize</td><td>-0.0009 ***(0.00007)</td><td>-0.001 ***(0.0002)</td></tr><tr><td>MinimumPlantHeight</td><td>0.006 ***(0.0003)</td><td>0.007 ***(0.0007)</td></tr><tr><td>MinimumNumberPlants</td><td>-0.00006(0.00006)</td><td>-0.000050.0001</td></tr><tr><td>Packaging</td><td>-0.021 ***(0.001)</td><td>-0.023 ***(0.002)</td></tr><tr><td>Weekday-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Grower-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>ProductCode-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Week-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>46,216</td><td>46,216</td></tr><tr><td>Adjusted R-squared</td><td>0.523</td><td>0.235</td></tr></table>

Note: Robust standard errors in parentheses. \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05

## Additional Analyses

In addition to the analyses that focus on the two key market performance indicators (i.e., revenue and efficiency), we conducted secondary analyses to compare bidding dynamics in sequential rounds before and after the mechanism change. We first examined the effect of the mechanism change on the level of price dispersion. We considered two outcome variables, the price range, which is measured as the difference between the highest and lowest winning price in an auction, and the standard deviation of winning prices in an auction, and estimated the following DID models:

$$
\begin{array}{c} \ln \left(P r i c e R a n g e _ {i, t}\right) = \\ \beta_ {0} + \beta_ {1} T r e a t m e n t _ {i} \times P o s t _ {t} + \beta_ {2} T r e a t m e n t _ {i} + \theta_ {t} + \gamma \mathbf {X} _ {i, t} + \epsilon_ {i, t} \end{array} \tag {7}
$$

$$
\begin{array}{c} \ln \left(S t d. d e v. o f P r i c e _ {i, t}\right) = \\ \beta_ {0} + \beta_ {1} T r e a t m e n t _ {i} \times P o s t _ {t} + \beta_ {2} T r e a t m e n t _ {i} + \theta_ {t} + \gamma \mathbf {X} _ {i, t} + \epsilon_ {i, t} \end{array} \tag {8}\tag{8}
$$

Table 11 summarizes the estimation results. We can see that both the range and the standard deviation of prices decreased significantly under the treatment, indicating that the hybrid mechanism increases the auction-level price stability.

To explore the potential drivers of the increased price stability, we draw upon prior literature on declining price trends in sequential auctions (Lu et al. 2016; Lu et al. 2019; McAfee and Vincent 1993; van den Berg et al. 2001) to examine whether the mechanism change has any impact on the price trend in sequential rounds. Following van den Berg et al. (2001), we used the difference of log prices in consecutive rounds as the dependent variable, which allows for (1) the control of potential confounding factors that influence the length of an auction and the price simultaneously, and (2) the control of the observed or unobserved heterogeneity across different auctions. We also included the rank of a transaction and the available units prior to the transaction for control. The complete model is specified as follows:

$$
\begin{array}{r l} & {\ln \left(\frac {P r i c e _ {i , k , t}}{P r i c e _ {i , k - 1 , t}}\right) = \beta_ {0} + \beta_ {1} T r e a t m e n t _ {i} \times P o s t _ {t} + \beta_ {2} T r e a t m e n t _ {i} + \theta_ {t}} \\ & {+ \mu_ {1} T r e a t m e n t _ {i} \big (A v a i l a b l e _ {i, k - 1} - 2 \big) + \mu_ {2} T r e a t m e n t _ {i} \big (R a n k _ {i, k} - 2 \big)} \\ & {\quad + \mu_ {3} P o s t _ {t} \big (A v a i l a b l e _ {i, k - 1} - 2 \big) + \mu_ {4} P o s t _ {t} \big (R a n k _ {i, k} - 2 \big)} \\ & {\quad + \mu_ {5} \big (A v a i l a b l e _ {i, k - 1} - 2 \big) + \mu_ {6} \big (R a n k _ {i, k} - 2 \big) + \epsilon_ {i, k, t},} \end{array}\tag{9}
$$

where ?? indexes the auction, ?? indexes the rank within an auction, and ?? indexes the time period (week). $A v a i l a b l e _ { i , k - 1 }$ denotes the available units prior to the (?? − 1)th transaction in auction ??, and $R a n k _ { i , k }$ denotes the rank of a transaction in auction ??. It is worth noting that we used two-unit auctions and auctions that were completed after two rounds as the reference points, thus Equation (9) is not well defined for single-unit or single-round auctions. Nevertheless, these auctions are not of interest to the characterization of the effect on price trends in sequential rounds. The estimation results are provided in Table 12.

The first thing to note from Table 12 is that the estimated coefficient of the intercept is negative and statistically significant, which confirms the declining price trend reported in prior studies (Lu et al. 2016; Lu et al. 2019; van den Berg et al. 2001). Next, the coefficient of the interaction term (i.e., ?????????????????? × ????????) is positive and significant, suggesting that the mechanism change can mitigate the price declining trend. Further, the estimates of ????????, ???????? × ????????, and ?????????????????? × ???????? indicate that the price declining trend tends to flatten in later rounds, and the magnitude of the flattening effect varies over time and across both sites.

At the outset, the main findings from Tables 11 and 12 are largely consistent with Häubl and Popkowski Leszczyc (2019) where the authors find that greater speed of competitor reaction increases the perceived competition intensity, which results in a higher willingness to pay. In our case, observing multiple winners (competitors) in previous rounds increases the perceived intensity of dynamic competition, which in turn discourages bid shading in subsequent rounds and leads to increased price stability. It is worth noting that a more stable price path is in the interest of both buyers (bidders) and growers (sellers), and it benefits the market as a whole in the long term because increased price stability leads to less regret for buyers and encourages their entry in the auctions, which in turn creates more selling opportunities for sellers.

Since bidders have to make decisions on both price and quantity, we also examined the effect of the mechanism change on bidders’ purchase quantity. To do so, we replaced the dependent variables in Equations (7) - (8) by the logtransformation of the average and standard deviation of purchase quantities in an auction. The estimation results are summarized in Table 13.

Here, we make two interesting observations. First, bidders average purchase quantity per transaction increased by approximately 6% under the hybrid mechanism. Second, the variation of purchase quantity at the auction level decreased by more than 8%. Taken together, these findings suggest that the increase in the perceived competitive intensity not only mitigates the potential bid shading in sequential rounds (see results from Table 12), but also stimulates bidders’ temporal demand (i.e., making the products more desirable).

<table><tr><td colspan="2">Table 12. Treatment Effect on Price Trend in Sequential Rounds</td></tr><tr><td>Variable</td><td> $\ln\left(\frac{PriceCurrentRound}{PricePreviousRound}\right)$ </td></tr><tr><td>Intercept</td><td>-0.046 ***(0.0012)</td></tr><tr><td>Treatment × Post</td><td>0.0059 ***(0.0013)</td></tr><tr><td>Treatment</td><td>0.0026(0.0013)</td></tr><tr><td>Treatment × Available</td><td>0.0000081(0.000022)</td></tr><tr><td>Treatment × Rank</td><td>-0.0016 ***(0.00036)</td></tr><tr><td>Post × Available</td><td>-0.000076 ***(0.000022)</td></tr><tr><td>Post × Rank</td><td>-0.0022 ***(0.00035)</td></tr><tr><td>Available</td><td>0.000038 *(0.000017)</td></tr><tr><td>Rank</td><td>0.0042 ***(0.00033)</td></tr><tr><td>Week-fixed effect</td><td>Yes</td></tr><tr><td>Observations</td><td>109,650</td></tr><tr><td>Adjusted R-squared</td><td>0.010</td></tr></table>

Note: Robust standard errors in parentheses. \*\*\*?? < 0.001, ${ } ^ { \star \star } p < 0 . 0 1 ,$ ${ } ^ { \star } p < 0 . 0 5$

<table><tr><td colspan="3">Table 13: Treatment Effect on Purchase Quantity</td></tr><tr><td>Variables</td><td>ln(AvgPurchaseQuant)</td><td>ln(S. D. ofPurchaseQuant)</td></tr><tr><td>Treatment × Post</td><td>0.057 ***(0.010)</td><td>-0.085 ***(0.015)</td></tr><tr><td>Treatment</td><td>-0.217***(0.007)</td><td>-0.059 ***(0.011)</td></tr><tr><td>LotSize</td><td>0.007 ***(0.0001)</td><td>0.012 ***(0.0002)</td></tr><tr><td>PotSize</td><td>0.0004 ***(0.00004)</td><td>0.0004 ***(0.00006)</td></tr><tr><td>MinimumPlantHeight</td><td>-0.001 ***(0.0001)</td><td>-0.003 ***(0.0003)</td></tr><tr><td>MinimumNumberPlants</td><td>-0.0001 **(0.00003)</td><td>-0.0001 **(0.00004)</td></tr><tr><td>Packaging</td><td>-0.004 ***(0.0005)</td><td>-0.001(0.0008)</td></tr><tr><td>Weekday-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Grower-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>ProductCode-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Week-fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>46,216</td><td>46,216</td></tr><tr><td>Adjusted R-squared</td><td>0.555</td><td>0.406</td></tr></table>

Note: Robust standard errors in parentheses. \*\*\*?? < 0.001, \*\*?? < 0.01, \*?? < 0.05

Table 14. Purchase Quantity Effect on High- and Low-End Products

<table><tr><td rowspan="2">Variables</td><td colspan="2"> $\ln(AvgPurchaseQuant)$ </td><td colspan="2"> $\ln(S. D. ofPurchaseQuant)$ </td></tr><tr><td>High-end</td><td>Low-end</td><td>High-end</td><td>Low-end</td></tr><tr><td>Treatment × Post</td><td>0.078 ***(0.017)</td><td>-0.0015(0.019)</td><td>-0.083 **(0.027)</td><td>-0.109 ***(0.029)</td></tr><tr><td>Treatment</td><td>-0.257 ***(0.013)</td><td>-0.166 ***(0.014)</td><td>-0.085 ***(0.020)</td><td>-0.066 **(0.021)</td></tr><tr><td>LotSize</td><td>0.0109 ***(0.003)</td><td>0.006 ***(0.0002)</td><td>0.0159 ***(0.0005)</td><td>0.0096 ***(0.0003)</td></tr><tr><td>PotSize</td><td>0.001(0.001)</td><td>0.0003 ***(0.00006)</td><td>0.001(0.001)</td><td>0.0002 **(0.00008)</td></tr><tr><td>MinimumPlantHeight</td><td>0.0003(0.0003)</td><td>-0.0007 **(0.0002)</td><td>-0.0009(0.00007)</td><td>-0.0015 **(0.0005)</td></tr><tr><td>MinimumNumberPlants</td><td>-0.0006 ***(0.0001)</td><td>0.0002 **(0.00008)</td><td>-0.0003 *(0.0001)</td><td>0.00008(0.00012)</td></tr><tr><td>Packaging</td><td>-0.019 **(0.002)</td><td>-0.0017 **(0.0006)</td><td>-0.019 **(0.005)</td><td>-0.004(0.003)</td></tr><tr><td>Weekday-fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Grower-fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>ProductCode-fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Week-fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>14,899</td><td>12,815</td><td>14,899</td><td>12,815</td></tr><tr><td>Adjusted R-squared</td><td>0.436</td><td>0.550</td><td>0.309</td><td>0.291</td></tr></table>

Note: Robust standard errors in parentheses. \*\*\*?? < 0.001, \*\*?? < 0.01, \*?? < 0.05

Finally, we examined whether the observed effects on purchase quantity varied across products within different price ranges. As before, we sorted different products based on their average prices and created two subsamples, one consisting of the top 30% of products, and the other consisting of the bottom 30%. We then reestimated the model.

According to Table 14, the decrease in the variation of purchase quantity remains significant across the two product categories. However, the increase in average purchase quantity is restricted to high-end products, suggesting that the increase in the perceived competitive intensity under the hybrid mechanism could stimulate demand for high-end products but not for low-end products. This finding also indicates that for high-end products, the observed improvement in operational efficiency (i.e., reduction in the average number of rounds taken to complete an auction) was not only due to the successful accommodation of temporal demand but also resulted from the increase in purchase quantity at the transaction level. Note that for any given lot of products, an increased purchase quantity per transaction means less post-auction handling of the lot (e.g., sorting and packing for delivery), which in turn leads to considerable time and cost savings.

## Discussion

We began this research by questioning whether a hybrid mechanism that allows for multiple winners in each round of a traditional multi-unit sequential Dutch auction could address the congestion problem arising from time-critical trading environments. Using analytical modeling and a large-scale quasi-natural field experiment, we demonstrate that the hybrid mechanism can significantly improve market performance in terms of operational efficiency and price stability.

## Contributions

Our paper makes important contributions to the interdisciplinary field of market design. First, we extend prior research around different design choices for complex markets by proposing a hybrid mechanism that combines the characteristics of the traditional sequential Dutch auction mechanism and a uniform-price mechanism. While information systems researchers have made extensive progress in understanding dynamic interactions in online auctions, most of the existing studies have restricted attention to the economic and behavioral implications of standard auction formats. To the best of our knowledge, this is the first study that explores the potential of hybrid mechanisms in addressing critical challenges faced by many well-established online and multi-channel markets. As such, our paper responds to the call for more research that identifies and evaluates novel mechanism designs (Bichler et al. 2010).

Second, given that the traditional sequential Dutch auction price discriminates (Katok and Roth 2004), i.e., winners do not pay the same price, our study sheds new lights on the longterm debate around the choice between discriminatory and uniform-price auctions by evaluating the performance of a hybrid of them. Unlike most of the existing studies that assume continuous bidding space, we consider a more realistic setting, where bidders choose their bids from a series of prespecified discrete values and show, theoretically and empirically, how bidders behave in various circumstances.

Third, our research adds to the literature on information disclosure in complex markets. With the ongoing digital transformation, market designers have more flexibility in customizing the information disclosed to different market participants (Adomavicius et al. 2013; Granados and Gupta, 2013). However, given the complex interplay of different strategic and informational factors in real-world markets, information strategy decisions often involve trade-offs between conflicting interests. Fortunately, in our case, by disclosing real-time information about competitors’ temporal demand and increasing the perceived intensity of competition, the hybrid mechanism not only increases the market clearing speed but also price stability, both of which benefit all market participants.

## Implications

Our research provides valuable insights to practitioners involved in market design and operation. Over the past decades, the integration of multiple channels enabled by information technology has accelerated the growth of many markets. However, given the increasing number of participants, congestion has become a serious issue, which, if left unaddressed, would discourage entry and eventually lead to market failure (Roth 2015).

Combining analytical modeling with fine-grained analysis of field data, we show that the proposed hybrid mechanism can effectively mitigate the congestion problem resulting from the delay in fulfilling temporal demand. Such improvement in operational efficiency benefits both buyers and sellers in timecritical markets. In the case of DFA, for example, high operational efficiency not only reduces lead time and allows products to be delivered more quickly but also opens space within the daily auction schedule to accommodate more products for sale, which encourages market entry and participation, thereby increasing the total revenue generated from trades. By incorporating the richness and complexity of the real-world operating environment, we provide actionable insights into how to design and evaluate hybrid mechanisms.

It is worth noting that while the current study has primarily focused on markets that employ sequential Dutch auctions, our proposed hybrid mechanism, after necessary adaptation and modification, would have broad applications in other time-critical markets. For example, many grocery stores have started to adopt dynamic discounting systems to reduce food waste.<sup>13</sup> Our findings have useful implications for designing optimal pricing strategies. In addition, since variations of sequential Dutch auctions have been used for clearance sales (Katok and Roth, 2004), our hybrid mechanism could be adapted to improve the efficiency of transactions in these contexts as well.

## Limitations and Future Work

The current study has several limitations. To start with, both our theoretical and empirical analyses focus on competitive bidding in the auction market and thus do not take into account competition in the downstream retail markets, which might impact bidders’ strategies. Investigating the impact of the hybrid mechanism on strategic interactions in interconnected business networks would be a promising direction for future work.

Second, we have not accounted for the potential impact of the mechanism change on bidders’ participation decisions at the market level. However, given the business-to-business (B2B) nature of the market we are studying, bidders’ participation is primarily order driven (i.e., bidders participate in the auctions to fulfill their customers’ orders) and thus less susceptible to mechanism changes. Nevertheless, recent research has shown that multi-winner awarding rules in online procurement auctions can significantly encourage participation (Wang et al. 2019). Future research could examine the direct impact of the hybrid mechanism on bidder entry at the market level.

Third, our empirical analyses suggest that increased informedness among bidders about market states (i.e., competitors’ temporal demand) has an overall positive impact on price stability in B2B markets. However, many online auctions are in business-to-consumer (B2C) or consumer-toconsumer (C2C) markets. Therefore, our findings may not be directly applicable, and this calls for further examination.

## Acknowledgments

The authors would like to thank senior editor Bin Gu, associate editor Xianjun Geng, and the three anonymous reviewers for their valuable comments and suggestions throughout the review process. The remaining errors are the authors’ own. This research would not have been possible without the collaboration of Royal FloraHolland in the Artificial Intelligence in the Floriculture Chain (iFlow) project (2015-2020), sponsored by Topsector Horticulture and Starting Materials, one of the nine top sectors of the Netherlands.

## References

Adomavicius, G., Curley, S.P., Gupta, A., and Sanyal, P. 2013. “Impact of Information Feedback in Continuous Combinatorial Auctions: An Experimental Study of Economic Performance,” MIS Quarterly (37:1), pp. 55-76.

Angrist, J.D., and J. Pischke. 2008. Mostly Harmless Econometrics: An Empiricist’s Companion, Princeton University Press.

Athey, S. 2001. “Single Crossing Properties and the Existence of Pure Strategy Equilibria in Games of Incomplete Information,” Econometrica, (69:4), pp. 861-889.

Ausubel, L.M., Cramton, P., Pycia, M., Rostek, M., and Weretka, M. 2014. “Demand Reduction and Inefficiency in Multi-unit Auctions,” Review of Economic Studies (81:4), pp. 1366-1400.

Bajari, P., and Hortaçsu, A. 2004. “Economic Insights from Internet Auctions.” Journal of Economic Literature (42:2), pp. 457-486.

Bapna, R., Goes, P., and Gupta, A. 2003a. “Replicating Online Yankee Auctions to Analyze Auctioneers’ and Bidders’ Strategies,” Information Systems Research (14:3), pp. 244-268.

Bapna, R., Goes, P., and Gupta, A. 2003b. “Analysis and Design of Business-to-Consumer Online Auctions,” Management Science (49:1), pp. 85-101.

Bichler, M., Gupta, A., and Ketter, W. 2010. “Designing Smart Markets,” Information Systems Research (21:4), pp. 688-699.

Card, D., and Krueger, A. B. 1994. “Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania,” American Economic Review (84:4), pp. 772-793.

Celis, L. E., Lewis, G., Mobius, M., and Nazerzadeh, H. 2014. “Buy-it-now or Take-a-chance: Price Discrimination through Randomized Auctions,” Management Science (60:12), pp. 2927-2948.

Dutra, J. C., and Menezes, F.M., 2002. “Hybrid Auctions,” Economics Letters (77:3), pp. 301-307.

Einav, L., Farronato, C., Levin, J., and Sundaresan, N., 2018. “Auctions versus Posted Prices in Online Markets,” Journal of Political Economy (126:1), pp. 178-215.

Goes, P., Karuga, G., and Tripathi, A. 2012. “Bidding Behavior Evolution in Sequential Auctions: Characterization and Analysis,” MIS Quarterly (36:4), pp. 1021-1042.

Graham, I. 1998. “The Emergence of Linked Fish Markets in Europe,” Electronic Markets (8:2), pp. 29-32.

Granados, N., and Gupta, A. 2013. “Transparency Strategy: Competing with Information in a Digital World,” MIS Quarterly (37:2), pp. 637-641.

Greenwood, B. N., and Wattal, S. 2017. “Show Me the Way to Go Home: An Empirical Investigation of Ride-Sharing and Alcohol Related Motor Vehicle Fatalities,” MIS Quarterly (41:1), pp. 163-187.

Häubl, G., and Popkowski Leszczyc, P. T. 2019. “Bidding Frenzy: Speed of Competitor Reaction and Willingness to Pay in Auctions,” Journal of Consumer Research (45:6), pp. 1294- 1314.

Hong, Y., Wang, C., and Pavlou, P.A. 2015. “Comparing Open and Sealed Bid Auctions: Evidence from Online Labor Markets,” Information Systems Research (27:1), pp. 49-69.

Hortaçsu, A., and McAdams, D. 2010. “Mechanism Choice and Strategic Bidding in Divisible Good Auctions: An Empirical Analysis of the Turkish Treasury Auction Market,” Journal of Political Economy (118:5), pp. 833-865.

Huang, N., Hong, Y., and Burtch, G. 2017. “Social Network Integration and User Content Generation: Evidence from Natural Experiments,” MIS Quarterly (41:4), pp. 1035-1058.

Iacus, S.M., King, G., and Porro, G. 2012. “Causal Inference without Balance Checking: Coarsened Exact Matching,” Political Analysis (20:1), pp. 1-24.

Jeitschko, T.D. 1998. “Learning in Sequential Auctions.” Southern Economic Journal (65:1), pp. 98-112.

Katok, E., and Kwasnica, A. M. 2008. “Time is Money: The Effect of Clock Speed on Seller’s Revenue in Dutch Auctions,” Experimental Economics (11:4), pp. 344-357.

Katok, E., and A.E. Roth. 2004. “Auctions of Homogeneous Goods with Increasing Returns: Experimental Comparison of Alternative “Dutch” Auctions,” Management Science (50:8), pp. 1044-1063.

Klemperer, P. 1999. “Auction Theory: A Guide to the Literature,” Journal of Economic Surveys (13:3) pp. 227-286.

Krishna, V. 2009. Auction Theory, Academic Press.

Li, Z., and Kuo, C.C. 2013. “Design of Discrete Dutch Auctions with an Uncertain Number of Bidders,” Annals of Operations Research (211:1), pp. 255-272.

List, J.A., and Lucking-Reiley, D. 2000. “Demand Reduction in Multi-Unit Auctions: Evidence from a Sports Card Field Experiment,” American Economic Review (90:4), pp. 961-972.

Lu, Y., Gupta, A., Ketter, W., and van Heck, E. 2016. “Exploring Bidder Heterogeneity in Multichannel Sequential B2B Auctions,” MIS Quarterly (40:3), pp. 645-662.

Lu, Y., Gupta, A., Ketter, W., and van Heck, E. 2019. “Information Transparency in Business-to-Business Auction Markets: The Role of Winner Identity Disclosure,” Management Science (65:9), pp. 4261-4279.

Mathews, T. 2004. “The Impact of Discounting on An Auction with a Buyout Option: A Theoretical Analysis Motivated by eBay’s Buy-it-now Feature,” Journal of Economics (81:1), pp. 25-52.

McAfee, R. P., and Vincent, D. 1993. “The Declining Price Anomaly,” Journal of Economic Theory (60:1), pp. 191-212.

Milgrom, P., and Weber, R. J. 1982. “The Value of Information in a Sealed-Bid Auction,” Journal of Mathematical Economics (10:1), pp. 105-114.

Myerson, R.B. 1981. “Optimal Auction Design,” Mathematics of

Operations Research (6:1), pp. 58-73.

Robey, D. 1979. “User Attitudes and Management Information System Use,” Academy of Management Journal (22:3), pp. 527-538.

Roth, A.E. 2007. “The Art of Designing Markets,” Harvard Business Review (85:10), pp. 118-126.

Roth, A.E. 2015. Who Gets What—and Why: The New Economics of Matchmaking and Market Design, Houghton Mifflin Harcourt.

Rothkopf, M., and Harstad, R. 1994a. “On the Role of Discrete Bid Levels in Oral Auctions,” European Journal of Operational Research, (74:3), pp. 572-581.

Rothkopf, M., and Harstad, R. 1994b. “Modeling Competitive Bidding: A Critical Essay,” Management Science (40:3), pp. 364-384.

Shadish, W. R., Cook, T. D., and Campbell, D. T. 2002. Experimental and Quasi-experimental Designs for Generalized Causal Inference. Houghton Mifflin Company.

Varian, H.R. 2009. “Online Ad Auctions,” American Economic Review, (99:2), pp. 430-434.

Van den Berg, G. J., Van Ours, J. C., and Pradhan, M. P. 2001. “The Declining Price Anomaly in Dutch Dutch Rose Auctions,” American Economic Review (91:4), pp. 1055-1062.

Vickrey, W. 1961. “Counter Speculation, Auctions, and Competitive Sealed Tenders,” The Journal of Finance (16:1), pp. 8-37.

Wang, Q., Feng, J., Jiang, X., and Xie, J. 2019. “Multiple-Winner Award Rules in Online Procurement Auctions,” Production and Operations Management, (28:10), pp. 2533-2551.

Wei, Z., and Lin, M. 2017. “Market Mechanisms in Online Peerto-Peer Lending,” Management Science (63:12): pp. 4236- 4257.

Zeithammer, R. 2007. “Strategic Bid-Shading and Sequential Auctioning with Learning from Past Prices,” Management Science (53:9), pp. 1510-1519.

## About the Authors

Yixin Lu is an assistant professor of information systems at the George Washington University School of Business (GWSB). Yixin’s research focuses on the strategic use of information and its impact on decision-making. She applies interdisciplinary approaches combining econometrics, game theory, controlled lab experiment, large-scale randomized experiment, and machine learning techniques to identify and quantify the impact of technological advancement on individuals, organizations, and society. Her research has been published in top journals such as Information Systems Research, Management Science, and MIS Quarterly. She has received the Dean’s Emerging Scholar Award and Outstanding ISTM Faculty Award at GWSB. She has also been awarded the AIS Impact Award (2020), the AIS Early Career Award (2021), and the INFORMS ISS Design Science Award (2021). She currently serves as associate editor at Information Systems Research.

Alok Gupta is the senior associate dean for faculty, research and administration at the Carlson School of Management, the University of Minnesota. He is the Curtis L. Carlson Schoolwide Chair in Information Management and the former chair of the Information and Decision Sciences Department. He was awarded the prestigious NSF CAREER Award for his research on dynamic pricing mechanisms on the internet in 2001. He has won numerous awards including the AIS Impact Award in 2020, and ISS Design Science Award three times in 2011, 2012 and 2021. He was named an INFORMS Information Systems Society Distinguished Fellow in 2014 and the Fellow of AIS in 2016. In 2021, he received the INFORMS ISS Practical Impact Award and INFORMS ISS President’s Service award. He is also a recipient of the AIS LEO award—the association’s highest recognition. He has served in editorial positions at most major IS journals, including senior editor at Information Systems Research, Journal of Management Information Systems, and associate editor at Management Science. Since 2017, he has served as the editor-in-chief of Information Systems Research.

Wolfgang Ketter is the chaired professor of Information Systems for Sustainable Society in the Faculty of Management, Economics, and Social Sciences at the University of Cologne, Germany, where research he leads focuses on how digital transformation can create a faster and more stable transition to sustainable energy and mobility. Additionally, he is the coordinator of the Key Research Initiative “Sustainable Smart Energy and Mobility” at the University of Cologne. This initiative explores the interdependent transition to sustainable energy and mobility from an interdisciplinary perspective, ranging from artificial intelligence to economics to social behavior. He is also the chaired professor of next generation information systems in the Department of Technology and Operations Management, and the director of the Erasmus Centre for Future Energy Business at the Rotterdam School of Management, Erasmus University. He has served as associate editor at Information Systems Research and MIS Quarterly. Since 2017 he has served as an advisor to the German government on energy and mobility policy, and since 2018 he has been a fellow of the World Economic Forum Global Future Council on Mobility. He won the prestigious AIS Impact Award (2020), the INFORMS Wagner Prize Finalists Award (2020), the INFORMS ISS Design Science Award (2012 and 2021), and the Information Systems Research Best Paper Award for 2020.

Eric van Heck is the chaired professor of Information Management and Markets at the Rotterdam School of Management, Erasmus University. He is a fellow of the Erasmus Research Institute of Management and a member of the Erasmus Center for Data Analytics. His research focuses on auction markets, business analytics, circular and digital business design, and digital work. In 2020, he received the AIS Sandra Slaughter Service Award, the AIS Technology Challenge Award, and the AIS Impact Award, and, in 2021, the INFORMS ISS Design Science Award. His flower research was a source of inspiration for his latest book for a general audience: Technology Meets Flowers. Unlocking the Circular and Digital Economy (Springer, 2021).

## Appendix

## Mathematical Proofs

## Proof of Proposition 1

Following prior studies in game-theoretical analysis of sequential auctions, we focus on sequentially rational equilibria, i.e., following any outcome of the first round, the strategies in the second round constitute an equilibrium (Krishna 2009). We begin with the second round where $N - 1$ bidders are competing for the (remaining) one item under auction. Suppose all other bidders, except for Bidder ??, follow the equilibrium strategy $\beta ^ { I I }$ defined in Equation (2). If Bidder ?? bids $b _ { 1 }$ in the second round and wins (i.e., none of her competitors bid more than $b _ { 1 } )$ , it implies that the values of all the $N - 2$ bidders are no more than $t _ { 1 } ^ { I I }$ . Using order statistics, Bidder ??’s expected payoff is given by

$$
\varOmega^ {I I} (b _ {1}, v _ {i}) = \frac {1}{N - 1} \mathcal {F} (t _ {1} ^ {I I}) ^ {N - 2} (v _ {i} - b _ {1}),
$$

where $v _ { i } \in \left( t _ { l - 1 } ^ { I I } , t _ { l } ^ { I I } \right]$ . If Bidder ?? bids $b _ { l } , l \ge 2$ , her expected payoff is given by

$$
\begin{array}{l} \Omega^ {I I} (b _ {l}, v _ {i}) = \sum_ {j = 0} ^ {N - 2} \frac {1}{j + 1} \cdot \binom {N - 2} {j} \Big (\mathcal {F} \big (t _ {l} ^ {I I} \big) - \mathcal {F} \big (t _ {l - 1} ^ {I I} \big) \Big) ^ {j} \mathcal {F} \big (t _ {l - 1} ^ {I I} \big) ^ {N - 2 - j} (v _ {i} - b _ {l}) \\ = \frac {\sum_ {j = 0} ^ {N - 2} \binom {N - 1} {j + 1} \Big (\mathcal {F} \big (t _ {l} ^ {I I} \big) - \mathcal {F} \big (t _ {l - 1} ^ {I I} \big) \Big) ^ {j + 1} \mathcal {F} \big (t _ {l - 1} ^ {I I} \big) ^ {N - 2 - j}}{(N - 1) (\mathcal {F} (t _ {l} ^ {I I}) - \mathcal {F} (t _ {l - 1} ^ {I I}))} (v _ {i} - b _ {l}) \\ = \frac {\mathcal {F} \big (t _ {l} ^ {I I} \big) ^ {N - 1} - \mathcal {F} \big (t _ {l - 1} ^ {I I} \big) ^ {N - 1}}{(N - 1) \left(\mathcal {F} (t _ {l} ^ {I I}) - \mathcal {F} (t _ {l - 1} ^ {I I})\right)} (v _ {i} - b _ {l}). \end{array}
$$

Here we consider all the possible scenarios where Bidder ?? wins with a bid $b _ { l }$ . Specifically, if ?? other bidders $( j \geq 0 )$ also bid $b _ { l } .$ , the probability of which is $\left( \mathcal { F } ( t _ { l } ^ { I I } ) - \mathcal { F } \big ( t _ { l - 1 } ^ { I I } \big ) \right) ^ { j }$ , and the rest $( N - 2 - j )$ bidders bid less than $b _ { l } ,$ the probability of which is $\mathcal { F } \big ( t _ { l - 1 } ^ { I I } \big ) ^ { N - 2 - j }$ , according to the random tie-breaking rule, Bidder ??’s winning probability $\mathrm { i s } { \frac { 1 } { j + 1 } } .$

Define $\begin{array} { r } { \varphi _ { l } = \frac { 1 } { N - 1 } ( \mathcal { F } \big ( t _ { l } ^ { I I } \big ) ^ { N - 1 } - \mathcal { F } \big ( t _ { l - 1 } ^ { I I } \big ) ^ { N - 1 } ) / \Big ( \mathcal { F } \big ( t _ { l } ^ { I I } \big ) - \mathcal { F } \big ( t _ { l - 1 } ^ { I I } \big ) \Big ) } \end{array}$ , we have $\varOmega ^ { I I } ( b _ { l } , v _ { i } ) = \varphi _ { l } ( v _ { i } - b _ { l } )$ . By definition, if $b _ { l }$ is an equilibrium bid, it must be a better, or at least no worse, choice than $b _ { l - 1 }$ and $b _ { l + 1 }$ . Because Bidder ?? prefers $b _ { l }$ to $b _ { l - 1 } .$ , we have

$$
\Omega^ {I I} (b _ {l}, v _ {i}) \geq \Omega^ {I I} (b _ {l - 1}, v _ {i}).
$$

Similarly, because Bidder ?? prefers $b _ { l } \mathrm { t o } \ b _ { l + 1 } .$ , we have

$$
\Omega^ {I I} (b _ {l}, v _ {i}) \geq \Omega^ {I I} (b _ {l + 1}, v _ {i}).
$$

Since $t _ { 0 } ^ { I I } = 0 .$ , we have $\begin{array} { r } { \varphi _ { 1 } = \frac { 1 } { N - 1 } \mathcal { F } ( t _ { 1 } ^ { I I } ) ^ { N - 2 } } \end{array}$ and $\mathcal { F } ( t _ { 0 } ^ { I I } ) = 0$ . The above inequalities can be rewritten as

$$
\varphi_ {l} (v _ {i} - b _ {l}) \geq \varphi_ {l - 1} (v _ {i} - b _ {l - 1}),
$$

$$
\varphi_ {l} (v _ {i} - b _ {l}) \geq \varphi_ {l + 1} (v _ {i} - b _ {l + 1}).
$$

Define $\delta { = } 1 / M$ . Replacing $b _ { l }$ with $b _ { l - 1 } + ~ \delta ,$ and $b _ { l + 1 }$ <sub>1</sub> with $b _ { l } + \delta ,$ , we have<sup>14</sup>:

$$
v _ {i} \geq b _ {l - 1} + \frac {\varphi_ {l}}{\varphi_ {l} - \varphi_ {l - 1}} \delta ,
$$

$$
v _ {i} \leq b _ {l} + \frac {\varphi_ {l + 1}}{\varphi_ {l + 1} - \varphi_ {l}} \delta .
$$

Since the above inequalities should hold for any $l \geq 1$ , comparing them with Equation (2), we can obtain

$$
t _ {l} ^ {I I} = b _ {l} + \frac {\varphi_ {l + 1}}{\varphi_ {l + 1} - \varphi_ {l}} \delta , l \geq 1.
$$

The decision problem faced by bidders in the first round is more complicated. Again, let us take the perspective of Bidder ?? with value $v _ { i }$ and assume that all other bidders are following the equilibrium strategy $\beta ^ { I }$ defined in Equation (1). Further, suppose that all bidders, including Bidder ??, follow $\beta ^ { I I }$ in the second round, regardless of what happens in the first round. The expected payoff of Bidder ?? when placing a bid $b _ { k }$ is

$$
\Omega^ {I} (b _ {k}, v _ {i}) = \operatorname * {P r} (\text { wins   in   the   1st   round } | b _ {k}) (v _ {i} - b _ {k}) + \operatorname * {P r} (\text { wins   in   the   2nd   round } | v _ {i}) \big (v _ {i} - \beta^ {I I} (v _ {i}) \big).
$$

Given $v _ { i } \in \left( t _ { k - 1 } ^ { I } , t _ { k } ^ { I } \right]$ and $v _ { i } \in \left( t _ { l - 1 } ^ { I I } , t _ { l } ^ { I I } \right]$ , following similar derivations as above, we have

$$
\begin{array}{l} \operatorname * {P r} (\text {wins in the 1st round } | b _ {k}) = \sum_ {j = 0} ^ {N - 1} \frac {1}{j + 1} \cdot \binom {N - 1} {j} \left(\mathcal {F} (t _ {k} ^ {I}) - \mathcal {F} (t _ {k - 1} ^ {I})\right) ^ {j} \mathcal {F} (t _ {k - 1} ^ {I}) ^ {N - 1 - j} \\ = \frac {1}{N (\mathcal {F} (t _ {k} ^ {I}) - \mathcal {F} (t _ {k - 1} ^ {I}))} \sum_ {j = 0} ^ {N - 1} \binom {N} {j + 1} (\mathcal {F} (t _ {k} ^ {I}) - \mathcal {F} (t _ {k - 1} ^ {I})) ^ {j + 1} \mathcal {F} (t _ {k - 1} ^ {I}) ^ {N - 1 - j} \\ = \frac {\mathcal {F} (t _ {k} ^ {I}) ^ {N} - \mathcal {F} (t _ {k - 1} ^ {I}) ^ {N}}{N (\mathcal {F} (t _ {k} ^ {I}) - \mathcal {F} (t _ {k - 1} ^ {I}))}, \end{array}
$$

$$
\operatorname * {P r} (\mathrm{winsinthe2ndround} | v _ {i}) = \left(1 - \frac {\mathcal {F} (t _ {k} ^ {I}) ^ {N} - \mathcal {F} (t _ {k - 1} ^ {I}) ^ {N}}{N (\mathcal {F} (t _ {k} ^ {I}) - \mathcal {F} (t _ {k - 1} ^ {I}))}\right) \cdot \frac {\mathcal {F} (t _ {l} ^ {I I}) ^ {N - 1} - \mathcal {F} (t _ {l - 1} ^ {I I}) ^ {N - 1}}{(N - 1) (\mathcal {F} (t _ {l} ^ {I I}) - \mathcal {F} (t _ {l - 1} ^ {I I}))}.
$$

Therefore, we have

$$
\Omega^ {I} (b _ {k}, v _ {i}) = (v _ {i} - b _ {k}) \cdot \frac {\mathcal {F} (t _ {k} ^ {I}) ^ {N} - \mathcal {F} (t _ {k - 1} ^ {I}) ^ {N}}{N (\mathcal {F} (t _ {k} ^ {I}) - \mathcal {F} (t _ {k - 1} ^ {I}))} + \left[ \left(1 - \frac {\mathcal {F} (t _ {k} ^ {I}) ^ {N} - \mathcal {F} (t _ {k - 1} ^ {I}) ^ {N}}{N (\mathcal {F} (t _ {k} ^ {I}) - \mathcal {F} (t _ {k - 1} ^ {I}))}\right) \cdot \frac {\mathcal {F} (t _ {l} ^ {I I}) ^ {N - 1} - \mathcal {F} (t _ {l - 1} ^ {I I}) ^ {N - 1}}{(N - 1) (\mathcal {F} (t _ {l} ^ {I I}) - \mathcal {F} (t _ {l - 1} ^ {I I}))} \right] (v _ {i} - \beta^ {I I} (v _ {i})).
$$

Define

$$
\tau_ {k} = \frac {\mathcal {F} (t _ {k} ^ {I}) ^ {N} - \mathcal {F} (t _ {k - 1} ^ {I}) ^ {N}}{N (\mathcal {F} (t _ {k} ^ {I}) - \mathcal {F} (t _ {k - 1} ^ {I}))},
$$

$$
\omega_ {k} = (1 - \frac {\mathcal {F} \big (t _ {k} ^ {I} \big) ^ {N} - \mathcal {F} \big (t _ {k - 1} ^ {I} \big) ^ {N}}{N \left(\mathcal {F} (t _ {k} ^ {I}) - \mathcal {F} (t _ {k - 1} ^ {I})\right)} \cdot \big (v _ {i} - \beta^ {I I} (v _ {i}) \big).
$$

The payoff equation can be rewritten as

$$
\Omega^ {I} (b _ {k}, v _ {i}) = (v _ {i} - b _ {k}) \cdot \tau_ {k} + \omega_ {k} \varphi_ {l}.
$$

By definition, if $b _ { k }$ is an equilibrium bid in the first round, $b _ { k }$ must be a better, or at least not worse, choice than $b _ { k - 1 }$ and $b _ { k + 1 }$ . Thus we have

$$
\Omega^ {I} (b _ {k}, v _ {i}) \geq \Omega^ {I} (b _ {k - 1}, v _ {i}),
$$

$$
\Omega^ {I} (b _ {k}, v _ {i}) \geq \Omega^ {I} (b _ {k + 1}, v _ {i}).
$$

By plugging in the payoff equation $\varOmega ^ { I } ( b _ { k } , v _ { i } ) = ( v _ { i } - b _ { k } ) \cdot \tau _ { k } + \omega _ { k } \varphi _ { l }$ , we can obtain

$$
\tau_ {k} (v _ {i} - b _ {k}) + \omega_ {k} \varphi_ {l} \geq \tau_ {k - 1} (v _ {i} - b _ {k - 1}) + \omega_ {k - 1} \varphi_ {l},
$$

$$
\tau_ {k} (v _ {i} - b _ {k}) + \omega_ {k} \varphi_ {l} \geq \tau_ {k + 1} (v _ {i} - b _ {k + 1}) + \omega_ {k + 1} \varphi_ {l}.
$$

Replacing $b _ { k }$ with $b _ { k - 1 } + \delta ,$ and $b _ { k + 1 }$ with $b _ { k } + \delta ,$ and following Lemma 1, the inequalities above can be rewritten as

$$
v _ {i} \geq b _ {k - 1} + \frac {\tau_ {k} \delta - (\omega_ {k} - \omega_ {k - 1}) \varphi_ {l}}{\tau_ {k} - \tau_ {k - 1}},
$$

$$
v _ {i} \leq b _ {k} + \frac {\tau_ {k + 1} \delta - (\omega_ {k + 1} - \omega_ {k}) \varphi_ {l}}{\tau_ {k + 1} - \tau_ {k}}.
$$

Since the above inequalities should hold for any $k \geq 1$ , comparing them with Equation (1), we can obtain

$$
t _ {k} ^ {I} = b _ {k} + \frac {\tau_ {k + 1} \delta - (\omega_ {k + 1} - \omega_ {k}) \varphi_ {l}}{\tau_ {k + 1} - \tau_ {k}}. \mathrm{■}
$$

Lemma 1: Given a continuous distribution ℱ on [0,1], an integer $N \ ( N > 2 )$ , and a series $\{ t _ { k } ^ { I } \}$ that partition the interval $[ 0 , 1 ] , i . e . , 0 =$ $t _ { 0 } ^ { I } < t _ { 1 } ^ { I } < \cdots t _ { k } ^ { I } < \cdots < t _ { r } ^ { I } = 1$ . For any ?? $( 2 \leq k \leq r )$ , we have $\tau _ { k } - \tau _ { k - 1 } > 0$ , where $\begin{array} { r } { \tau _ { k } = \frac { \mathcal { F } \left( t _ { k } ^ { I } \right) ^ { N } - \mathcal { F } \left( t _ { k - 1 } ^ { I } \right) ^ { N } } { N \left( \mathcal { F } \left( t _ { k } ^ { I } \right) - \mathcal { F } \left( t _ { k - 1 } ^ { I } \right) \right) } } \end{array}$

Proof:

For any ?? $( 2 \leq k \leq r )$ , we have

$$
\begin{array}{l} \tau_ {k} - \tau_ {k - 1} = \frac {1}{N} \sum_ {j = 0} ^ {N - 1} \mathcal {F} (t _ {k} ^ {I}) ^ {j} \mathcal {F} (t _ {k - 1} ^ {I}) ^ {N - 1 - j} - \frac {1}{N} \sum_ {j = 0} ^ {N - 1} \mathcal {F} (t _ {k - 1} ^ {I}) ^ {j} \mathcal {F} (t _ {k - 2} ^ {I}) ^ {N - 1 - j} \\ = \frac {1}{N} \sum_ {j = 0} ^ {N - 1} \mathcal {F} (t _ {k - 1}) ^ {N - 1 - j} [ \mathcal {F} (t _ {k} ^ {I}) ^ {j} - \mathcal {F} (t _ {k - 2} ^ {I}) ^ {j} ] > 0. \quad \blacksquare \end{array}
$$

## Proof of Proposition 2

Analogous to the proof of Proposition 1, we begin with the second round, where the ?? − 1 bidders are competing for the remaining one item. Note that in this case, the decision problem faced by the bidders under the hybrid mechanism is exactly the same as the one under the traditional sequential Dutch auction. Thus, we have $\hat { \beta } ^ { I I } = \beta ^ { I I }$ , and $\hat { t } _ { l } ^ { I I } = t _ { l } ^ { I I }$ for any $l \geq 1$

Now let us consider the bidding competition in the first round. Again, we take the perspective of Bidder ?? with the private value of $v _ { i } \left( v _ { i } \in \right.$ $\left( \hat { t } _ { k - 1 } ^ { I } , \hat { t } _ { k } ^ { I } \right] )$ . Her expected payoff by placing a bid $b _ { k }$ is given by

$$
\Omega^ {I} (b _ {k}, v _ {i}) = \operatorname * {P r} (\text { wins   in   the   1st   round } | b _ {k}) (v _ {i} - b _ {k}) + \operatorname * {P r} (\text { wins   in   the   2nd   round } | v _ {i}) \big (v _ {i} - \beta^ {I I} (v _ {i}) \big).
$$

There are two possible scenarios under which Bidder ?? wins in the first round:

(1) All the other ?? − 1 bidders bid less than $b _ { k } ,$ , where we have

$$
\operatorname * {P r} (\text { wins   in   the   1st   round   (Scenario   1) } | b _ {k}) = \mathcal {F} \left(\hat {t} _ {k - 1} ^ {I}\right) ^ {N - 1};
$$

(2) ?? other bidders $( j \geq 1 )$ bid $b _ { k } .$ , the probability of which is $\left( \mathcal { F } ( \hat { t } _ { k } ^ { I } ) - \mathcal { F } ( \hat { t } _ { k - 1 } ^ { I } ) \right) ^ { j }$ , whereas the rest of the bidders bid less than $b _ { k } ,$ , the probability of which is $\mathcal { F } \big ( \hat { t } _ { k - 1 } ^ { I } \big ) ^ { N - 1 - j }$ . Bidder $i \ ' \mathbf { s }$ winning probability is $\frac { 2 } { j + 1 }$ under the random tie-breaking rule. Therefore,

$$
\Pr (\text {wins in the 1st round (Scenario 2)} | b _ {k}) = \sum_ {j = 1} ^ {N - 1} \frac {2}{j + 1} \cdot \binom {N - 1} {j} \left(\mathcal {F} \bigl (\hat {t} _ {k} ^ {I} \bigr) - \mathcal {F} \bigl (\hat {t} _ {k - 1} ^ {I} \bigr)\right) ^ {j} \mathcal {F} \bigl (\hat {t} _ {k - 1} ^ {I} \bigr) ^ {N - 1 - j}.
$$

Combining the two scenarios, we can obtain

$$
\begin{array}{l} \operatorname * {P r} (\text {wins in the 1st round} | b _ {k}) = \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big) ^ {N - 1} + \sum_ {j = 1} ^ {N - 1} \frac {2}{j + 1} \cdot \binom {N - 1} {j} \Big (\mathcal {F} \big (\hat {t} _ {k} ^ {I} \big) - \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big) \Big) ^ {j} \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big) ^ {N - 1 - j} \\ = - \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big) ^ {N - 1} + \frac {2}{N} \frac {\mathcal {F} \big (\hat {t} _ {k} ^ {I} \big) ^ {N} - \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big) ^ {N}}{\mathcal {F} (\hat {t} _ {k} ^ {I}) - \mathcal {F} (\hat {t} _ {k - 1} ^ {I})}. \end{array}
$$

If Bidder ?? loses in the first round but the auction proceeds to the second round, there must be one and only one bidder who bids higher than the rest of the $N - 1$ bidders, including Bidder ?? who bids $b _ { k }$ . This is because if there are multiple highest bids, under the hybrid mechanism, both items will be sold in the first round and the auction ends. Given $v _ { i } \in \left( \hat { t } _ { k - 1 } ^ { I } , \hat { t } _ { k } ^ { I } \right]$ and $\bar { v } _ { i } \in \left( t _ { l - 1 } ^ { I I } , t _ { l } ^ { I I } \right]$ , we can visualize the possible scenarios faced by Bidder ??.

As shown in Figure A1, the value of the winning bidder in the first round must be higher than $\hat { t } _ { k } ^ { I } .$ . Among the rest of the $N - 2$ bidders, those with a private value of more than $t _ { l - 1 } ^ { I I }$ will affect Bidder ??’s winning probability in the second round. In addition, it is noteworthy that for any Bidder $j ( j \neq i )$ , as long as $v _ { j } \leq t _ { l } ^ { I I }$ , Bidder j may tie with Bidder ?? in the second round even if $v _ { j } \in \left( \widehat { t } _ { k } ^ { I } , \widehat { t } _ { k + 1 } ^ { I } \right]$ . This is due to the fact that the two series $\{ \hat { t } _ { k } ^ { I } , k \geq 1 \}$ and $\{ t _ { l } ^ { I I } , l \ge 1 \}$ are different partitions of the value space.

![](/api/attachments/PUYV7N2F/fulltext/images/bcc09188d936e1cce405b226a5dfc39ec88052cee9d4f1ce9a106e510cb98b33.jpg)

Figure A1. Illustration of Bidder ??’s Second-Round Winning Scenario

Following the above analysis, we first consider the case when the value of the winning bidder in the first round, denoted by $v _ { w } ^ { I }$ , falls into the interval $\left( \widehat { t } _ { k } ^ { I } , \widehat { t } _ { k + 1 } ^ { I } \right]$ . Bidder $i \ ' \mathbf { s }$ winning probability in the second round is given by:

Pr(wins in the 2nd round |??<sub>??</sub>, ??<sub>??</sub><sup>??</sup> ∈ (??̂<sub>??</sub><sup>??</sup> , ??̂<sub>??+1</sub><sup>??</sup> ])

$$
\begin{array}{l} \text {d round} \left| v _ {i}, v _ {w} ^ {I} \in \left(\hat {t} _ {k} ^ {I}, \hat {t} _ {k + 1} ^ {I} \right]\right) \\ = (N - 1) (\mathcal {F} \big (\hat {t} _ {k + 1} ^ {I} \big) - \mathcal {F} \big (\hat {t} _ {k} ^ {I} \big)) \mathcal {F} (\hat {t} _ {k} ^ {I}) ^ {N - 2} \cdot \sum_ {j = 0} ^ {N - 2} \frac {1}{j + 1} \cdot \binom {N - 2} {j} \Big (\mathcal {F} \big (t _ {l} ^ {I I} \big) - \mathcal {F} \big (t _ {l - 1} ^ {I I} \big) \Big) ^ {j} \mathcal {F} \big (t _ {l - 1} ^ {I I} \big) ^ {N - 2 - j} \\ = \Big (\mathcal {F} \big (\hat {t} _ {k + 1} ^ {I} \big) - \mathcal {F} \big (\hat {t} _ {k} ^ {I} \big) \Big) \mathcal {F} \big (\hat {t} _ {k} ^ {I} \big) ^ {N - 2} \cdot \frac {\mathcal {F} \big (t _ {l} ^ {I I} \big) ^ {N - 1} - \mathcal {F} \big (t _ {l - 1} ^ {I I} \big) ^ {N - 1}}{\mathcal {F} (t _ {l} ^ {I I}) - \mathcal {F} (t _ {l - 1} ^ {I I})}. \end{array}
$$

Similarly, when $v _ { w } ^ { I }$ falls into the interval $( \hat { t } _ { k + 1 } ^ { I } , \hat { t } _ { k + 2 } ^ { I } ] ,$ , we have

Pr(wins in the 2nd round $\left| v _ { i } , v _ { w } ^ { I } \in \left( \hat { t } _ { k } ^ { I } , \hat { t } _ { k + 1 } ^ { I } \right] \right)$

$$
= \left(\mathcal {F} \big (\hat {t} _ {k + 2} ^ {I} \big) - \mathcal {F} \big (\hat {t} _ {k + 1} ^ {I} \big)\right) \mathcal {F} \big (\hat {t} _ {k + 1} ^ {I} \big) ^ {N - 2} \cdot \frac {\mathcal {F} \big (t _ {l} ^ {I I} \big) ^ {N - 1} - \mathcal {F} \big (t _ {l - 1} ^ {I I} \big) ^ {N - 1}}{\mathcal {F} (t _ {l} ^ {I I}) - \mathcal {F} (t _ {l - 1} ^ {I I})}.
$$

Aggregating all the possible cases regarding $v _ { w } ^ { I } .$ we can obtain

Pr(wins in the 2nd round

$$
| v _ {i}) = \sum_ {j = k} ^ {\hat {r} - 1} (\mathcal {F} \big (\hat {t} _ {j + 1} ^ {I} \big) - \mathcal {F} \big (\hat {t} _ {j} ^ {I} \big)) \mathcal {F} \big (\hat {t} _ {j} ^ {I} \big) ^ {N - 2} \cdot \frac {\mathcal {F} \big (t _ {l} ^ {I I} \big) ^ {N - 1} - \mathcal {F} \big (t _ {l - 1} ^ {I I} \big) ^ {N - 1}}{\mathcal {F} (t _ {l} ^ {I I}) - \mathcal {F} (t _ {l - 1} ^ {I I})}
$$

Thus Bidder ??’s expected payoff in the first round is given by

$$
\Omega^ {I} (b _ {k}, v _ {i}) = (v _ {i} - b _ {k}) \cdot \left[ - \mathcal {F} (\hat {t} _ {k - 1} ^ {I}) ^ {N - 1} + \frac {2}{N} \frac {\mathcal {F} (\hat {t} _ {k} ^ {I}) ^ {N} - \mathcal {F} (\hat {t} _ {k - 1} ^ {I}) ^ {N}}{\mathcal {F} (\hat {t} _ {k} ^ {I}) - \mathcal {F} (\hat {t} _ {k - 1} ^ {I})} \right]
$$

$$
+ \left(v _ {i} - \beta^ {I I} (v _ {i})\right) \cdot \sum_ {j = k} ^ {\hat {r} - 1} \Big (\mathcal {F} \big (\hat {t} _ {j + 1} ^ {I} \big) - \mathcal {F} \big (\hat {t} _ {j} ^ {I} \big) \Big) \mathcal {F} \big (\hat {t} _ {j} ^ {I} \big) ^ {N - 2} \cdot \frac {\mathcal {F} \big (t _ {l} ^ {I I} \big) ^ {N - 1} - \mathcal {F} \big (t _ {l - 1} ^ {I I} \big) ^ {N - 1}}{\mathcal {F} (\hat {t} _ {l} ^ {I I}) - \mathcal {F} (t _ {l - 1} ^ {I I})}.
$$

Define

$$
\hat {\tau} _ {k} = - \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big) ^ {N - 1} + \frac {2}{N} \frac {\mathcal {F} \big (\hat {t} _ {k} ^ {I} \big) ^ {N} - \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big) ^ {N}}{\mathcal {F} (\hat {t} _ {k} ^ {I}) - \mathcal {F} (\hat {t} _ {k - 1} ^ {I})},
$$

$$
\widehat {\omega} _ {k} = \left(v _ {i} - \beta^ {I I} (v _ {i})\right) \cdot \sum_ {j = k} ^ {\hat {r} - 1} \left(\mathcal {F} \big (\hat {t} _ {j + 1} ^ {I} \big) - \mathcal {F} \big (\hat {t} _ {j} ^ {I} \big)\right) \mathcal {F} \big (\hat {t} _ {j} ^ {I} \big) ^ {N - 2}
$$

$$
\hat {\varphi} _ {l} = (N - 1) \varphi_ {l}.
$$

We can rewrite the expected payoff as

$$
\Omega^ {I} (b _ {k}, v _ {i}) = (v _ {i} - b _ {k}) \cdot \hat {\tau} _ {k} + \widehat {\omega} _ {k} \hat {\varphi} _ {l}.
$$

Similar as before, using the definition of equilibrium, we can obtain the following inequalities with respect to Bidder ??’s expected payoff:

$$
\Omega^ {I} (b _ {k}, v _ {i}) \geq \Omega^ {I} (b _ {k - 1}, v _ {i}),
$$

$$
\Omega^ {I} (b _ {k}, v _ {i}) \geq \Omega^ {I} (b _ {k + 1}, v _ {i}).
$$

Plugging in $\Omega ^ { I } ( b _ { k } , v _ { i } ) = ( v _ { i } - b _ { k } ) \cdot \hat { \tau } _ { k } + \widehat { \omega } _ { k } \widehat { \varphi } _ { l }$ , we have

$$
\hat {\tau} _ {k} (v _ {i} - b _ {k}) + \widehat {\omega} _ {k} \hat {\varphi} _ {l} \geq \hat {\tau} _ {k - 1} (v _ {i} - b _ {k - 1}) + \widehat {\omega} _ {k - 1} \hat {\varphi} _ {l},
$$

$$
\hat {\tau} _ {k} (v _ {i} - b _ {k}) + \widehat {\omega} _ {k} \widehat {\varphi} _ {l} \geq \hat {\tau} _ {k + 1} (v _ {i} - b _ {k + 1}) + \widehat {\omega} _ {k + 1} \widehat {\varphi} _ {l}.
$$

Replacing $b _ { k }$ with $b _ { k - 1 } + ~ \delta ,$ and $b _ { k + 1 }$ with $b _ { k } + \delta$ , following Lemma 2, the above inequalities can be rewritten as

$$
v _ {i} \geq b _ {k - 1} + \frac {\hat {\tau} _ {k} \delta - (\widehat {\omega} _ {k} - \widehat {\omega} _ {k - 1}) \hat {\varphi} _ {l}}{\hat {\tau} _ {k} - \hat {\tau} _ {k - 1}},
$$

$$
v _ {i} \leq b _ {k} + \frac {\hat {\tau} _ {k + 1} \delta - (\widehat {\omega} _ {k + 1} - \widehat {\omega} _ {k}) \hat {\varphi} _ {l}}{\hat {\tau} _ {k + 1} - \hat {\tau} _ {k}}.
$$

Since the above inequalities should hold for any $k \geq 1 .$ , comparing them with Equation (3), we can obtain

$$
\hat {t} _ {k} ^ {I} = b _ {k} + \frac {\hat {\tau} _ {k + 1} \delta - (\widehat {\omega} _ {k + 1} - \widehat {\omega} _ {k}) \hat {\varphi} _ {l}}{\hat {\tau} _ {k + 1} - \hat {\tau} _ {k}}. \mathrm{■}
$$

Lemma 2: Given a continuous distribution ℱ on [0,1], an integer $N \ ( N > 2 )$ , and a series $\it { \Omega } / \hat { t } _ { k } ^ { I } \it { \Omega } / \Omega$ that partition the interval [0,1], i.e., $0 =$ $\hat { t } _ { 0 } ^ { I } < \hat { t } _ { 1 } ^ { I } < \dots \hat { t } _ { k } ^ { I } < \dots < \hat { t } _ { \hat { r } } ^ { I } = 1$ . For any ?? $( 2 \leq k \leq \hat { r } )$ , we have $\hat { \tau } _ { k } - \hat { \tau } _ { k - 1 } > 0 ,$ , where $\begin{array} { r } { \hat { \tau } _ { k } = - \mathcal { F } \big ( \hat { t } _ { k - 1 } ^ { I } \big ) ^ { N - 1 } + \frac { 2 } { N } \frac { \mathcal { F } \big ( \hat { t } _ { k } ^ { I } \big ) ^ { N } - \mathcal { F } \big ( \hat { t } _ { k - 1 } ^ { I } \big ) ^ { N } } { \mathcal { F } \big ( \hat { t } _ { k } ^ { I } \big ) - \mathcal { F } \big ( \hat { t } _ { k - 1 } ^ { I } \big ) } } \end{array}$

Proof:

For any ?? $( 2 \leq k \leq r )$ , we have

$$
\begin{array}{r l} & {\hat {t} _ {k} - \hat {t} _ {k - 1} = \frac {1}{N} \Bigg [ 2 \sum_ {j = 0} ^ {N - 1} \mathcal {F} \big (\hat {t} _ {k} ^ {I} \big) ^ {j} \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big) ^ {N - 1 - j} - N \cdot \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big) ^ {N - 1}} \\ & {- 2 \sum_ {j = 0} ^ {N - 1} \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big) ^ {j} \mathcal {F} \big (\hat {t} _ {k - 2} ^ {I} \big) ^ {N - 1 - j} + N \cdot \mathcal {F} \big (\hat {t} _ {k - 2} ^ {I} \big) ^ {N - 1} \Bigg ]} \\ & {= \frac {1}{N} [ 2 \sum_ {j = 0} ^ {N - 1} \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big) ^ {j} (\mathcal {F} \big (\hat {t} _ {k} ^ {I} \big) ^ {N - 1 - j} - \mathcal {F} \big (\hat {t} _ {k - 2} ^ {I} \big) ^ {N - 1 - j})} \\ & {- N \cdot \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big) ^ {N - 1} + N \cdot \mathcal {F} \big (\hat {t} _ {k - 2} ^ {I} \big) ^ {N - 1} ]} \\ & {\geq \frac {2}{N} \sum_ {j = 0} ^ {N - 1} [ \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big) ^ {j} (\mathcal {F} \big (\hat {t} _ {k} ^ {I} \big) ^ {N - 1 - j} - \mathcal {F} \big (\hat {t} _ {k - 2} ^ {I} \big) ^ {N - 1 - i j} - \frac {1}{2} \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big) ^ {N - 1 - i j} + \frac {1}{2} \mathcal {F} \big (\hat {t} _ {k - 2} ^ {I} \big) ^ {N - 1 - i j}) ]} \\ & {\quad = \frac {2}{N} \sum_ {j = 0} ^ {N - 1} [ \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big) ^ {j} (\mathcal {F} \big (\hat {t} _ {k} ^ {I} \big) ^ {N - 1 - i j} - \frac {1}{2} \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big) ^ {N - 1 - i j} - \frac {1}{2} \mathcal {F} \big (\hat {t} _ {k - 2} ^ {I} \big) ^ {N - 1 - i j}) ] > 0.} \end{array}
$$

## Proof of Proposition 3

We first consider the allocative efficiency (??) under the traditional sequential Dutch auction, where only one item is sold in each round. Assume ?? bidders $( j \geq 1 )$ bid the same highest price. Following the random tie-breaking rule, $\alpha = 1 / j$ . Therefore, in the first round, we can obtain

$$
E (\alpha^ {I}) = \sum_ {k = 1} ^ {r} \sum_ {j = 1} ^ {N} \frac {1}{j} \cdot {\binom {N} {j}} (\mathcal {F} (t _ {k} ^ {I}) - \mathcal {F} (t _ {k - 1} ^ {I})) ^ {j} \mathcal {F} (t _ {k - 1} ^ {I}) ^ {N - j}
$$

$$
= \sum_ {j = 1} ^ {N} \frac {1}{j} \cdot \sum_ {k = 1} ^ {r} {\binom {N} {j}} \left(\mathcal {F} \big (t _ {k} ^ {I} \big) - \mathcal {F} \big (t _ {k - 1} ^ {I} \big)\right) ^ {j} \mathcal {F} \big (t _ {k - 1} ^ {I} \big) ^ {N - j}.
$$

Define $\begin{array} { r } { \rho ^ { I } ( j , N ) = \sum _ { k = 1 } ^ { r } \binom { N } { j } ( \mathcal { F } \big ( t _ { k } ^ { I } \big ) - \mathcal { F } \big ( t _ { k - 1 } ^ { I } \big ) ) ^ { j } \mathcal { F } \big ( t _ { k - 1 } ^ { I } \big ) ^ { N - j } } \end{array}$ , we can rewrite the above equation as follows:

$$
E (\alpha^ {I}) = \sum_ {j = 1} ^ {N} \frac {1}{j} \cdot \rho^ {I} (j, N).
$$

Since ∑ ??<sup>??</sup>(??, ??)<sup>??</sup><sub>??=1</sub> = ∑ ∑ (<sup>??</sup><sub>??</sub> ) (ℱ(??<sub>??</sub><sup>??</sup> ) − ℱ(??<sub>??−1</sub><sup>??</sup> ))<sup>??</sup> ℱ(??<sub>??−1</sub><sup>??</sup> )<sup>??−??</sup> <sup>??</sup><sub>??=1</sub><sup>??</sup><sub>??=1</sub>

$$
= \sum_ {k = 1} ^ {r} \sum_ {j = 1} ^ {N} {\binom {N} {j}} \left(\mathcal {F} \big (t _ {k} ^ {I} \big) - \mathcal {F} \big (t _ {k - 1} ^ {I} \big)\right) ^ {j} \mathcal {F} \big (t _ {k - 1} ^ {I} \big) ^ {N - j}
$$

$$
= \sum_ {k = 1} ^ {r} (\mathcal {F} (t _ {k} ^ {I}) ^ {N} - \mathcal {F} (t _ {k - 1} ^ {I}) ^ {N}) = \mathcal {F} (t _ {r} ^ {I}) ^ {N} - \mathcal {F} (t _ {0} ^ {I}) ^ {N} = 1,
$$

We have $E ( \alpha ^ { I } ) < 1$ for $N > 2$

Similarly, we can derive the expected allocative efficiency in the second round as follows:

$$
E (\alpha^ {I I}) = \sum_ {l = 1} ^ {s} \sum_ {j = 1} ^ {N - 1} \frac {1}{j} \cdot \binom {N - 1} {j} (\mathcal {F} (t _ {l} ^ {I I}) - \mathcal {F} (t _ {l - 1} ^ {I I})) ^ {j} \mathcal {F} (t _ {l - 1} ^ {I I}) ^ {N - 1 - j}
$$

$$
= \sum_ {j = 1} ^ {N - 1} \frac {1}{j} \cdot \rho^ {I I} (j, N - 1),
$$

where $\begin{array} { r } { { \boldsymbol \rho } ^ { I I } ( j , N - 1 ) = \sum _ { l = 1 } ^ { s } \binom { N - 1 } { j } ( \mathcal { F } \big ( t _ { l } ^ { I I } \big ) - \mathcal { F } \big ( t _ { l - 1 } ^ { I I } \big ) ) ^ { j } \mathcal { F } \big ( t _ { l - 1 } ^ { I I } \big ) ^ { N - 1 - j } , \mathrm { a n d } E ( \alpha ^ { I I } ) < 1 . } \end{array}$

Therefore, the average allocative efficiency under the traditional sequential Dutch auction for two identical items is given by:

$$
\alpha = \frac {1}{2} \Big (E (\alpha^ {I}) + E (\alpha^ {I I}) \Big) = \frac {1}{2} \sum_ {j = 1} ^ {N} \frac {1}{j} \cdot \rho^ {I} (j, N) + \frac {1}{2} \sum_ {j = 1} ^ {N - 1} \frac {1}{j} \cdot \rho^ {I I} (j, N - 1).
$$

Next, let us consider the allocative efficiency under the hybrid mechanism. Note that when more than one bidder places the highest bid, the two identical items will be sold out in one round. Suppose $j \left( j \geq 2 \right)$ bidders place the highest bid, following the random tie-breaking rule, $\hat { \alpha } = 2 / j$ . Thus, we can obtain

$$
E (\hat {\alpha} | \text { auction   ends   in   the   1st   round }) = \sum_ {k = 1} ^ {\hat {r}} \sum_ {j = 2} ^ {N} \frac {2}{j} \cdot \binom {N} {j} \left(\mathcal {F} \big (\hat {t} _ {k} ^ {l} \big) - \mathcal {F} \big (\hat {t} _ {k - 1} ^ {l} \big)\right) ^ {j} \mathcal {F} \big (\hat {t} _ {k - 1} ^ {l} \big) ^ {N - j}.
$$

Define $\begin{array} { r } { \hat { \rho } ^ { I } ( j , N ) { = } \sum _ { k = 1 } ^ { { \hat { r } } } \binom { N } { j } ( \mathcal { F } \big ( \hat { t } _ { k } ^ { I } \big ) - \mathcal { F } \big ( \hat { t } _ { k - 1 } ^ { I } \big ) ) ^ { j } \mathcal { F } \big ( \hat { t } _ { k - 1 } ^ { I } \big ) ^ { N - j } } \end{array}$ . We can rewrite the above question as

$$
E (\hat {\alpha} | \text { auction   ends   in   the   1st   round }) = \sum_ {j = 2} ^ {N} \frac {2}{j} \cdot \hat {\rho} ^ {I} (j, N).
$$

When there is only one highest bidder in the first round, the probability of which is given by

$$
\hat {\rho} ^ {I} (1, N) = \sum_ {k = 1} ^ {r} \binom {N} {1} \left(\mathcal {F} \big (\hat {t} _ {k} ^ {I} \big) - \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big)\right) \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big) ^ {N - 1},
$$

the auction will move to the second round, and the expected allocative efficiency can be derived in a same way as in the second round of a traditional sequential Dutch auction:

$$
E (\hat {\alpha} ^ {I I}) = \sum_ {j = 1} ^ {N - 1} \frac {1}{j} \cdot \rho^ {I I} (j, N - 1).
$$

Combining the cases discussed above, we can obtain

$$
\hat {\alpha} = \frac {1}{2} \hat {\rho} ^ {I} (1, N) \cdot \left[ 1 + \sum_ {j = 1} ^ {N - 1} \frac {1}{j} \cdot \rho^ {I I} (j, N - 1) \right] + \sum_ {j = 2} ^ {N} \frac {2}{j} \cdot \hat {\rho} ^ {I} (j, N).
$$

The difference between the two mechanisms, in terms of allocative efficiency, is given by

$$
\begin{array}{l} \hat {\alpha} - \alpha = \frac {1}{2} \hat {\rho} ^ {I} (1, N) \cdot \left[ 1 + \sum_ {j = 1} ^ {N - 1} \frac {1}{j} \cdot \rho^ {I I} (j, N - 1) \right] + \sum_ {j = 2} ^ {N} \frac {2}{j} \cdot \hat {\rho} ^ {I} (j, N) \\ \qquad = \frac {1}{2} \hat {\rho} ^ {I} (1, N) + \sum_ {j = 2} ^ {N} \frac {2}{j} \cdot \hat {\rho} ^ {I} (j, N) - \frac {1}{2} \sum_ {j = 1} ^ {N} \frac {1}{j} \cdot \rho^ {I} (j, N) \\ \qquad - \frac {1}{2} \big (1 - \hat {\rho} ^ {I} (1, N) \big) \sum_ {j = 1} ^ {N - 1} \frac {1}{j} \cdot \rho^ {I I} (j, N - 1) \\ \qquad = \frac {3}{2} \sum_ {j = 2} ^ {N} \frac {1}{j} \cdot \hat {\rho} ^ {I} (j, N) - \frac {1}{2} \big (1 - \hat {\rho} ^ {I} (1, N) \big) \sum_ {j = 1} ^ {N - 1} \frac {1}{j} \cdot \rho^ {I I} (j, N - 1) \\ \qquad + \frac {1}{2} \sum_ {j = 1} ^ {N} \frac {1}{j} \cdot (\hat {\rho} ^ {I} (j, N) - \rho^ {I} (j, N)). \end{array}
$$

By definition, $\begin{array} { r } { \hat { \rho } ^ { I } ( 1 , N ) = \sum _ { k = 1 } ^ { r } \binom { N } { 1 } \left( \mathcal { F } \big ( \hat { t } _ { k } ^ { I } \big ) - \mathcal { F } \big ( \hat { t } _ { k - 1 } ^ { I } \big ) \right) \mathcal { F } \big ( \hat { t } _ { k - 1 } ^ { I } \big ) ^ { N - 1 } } \end{array}$ . When $M  \infty$ , i.e., the bid increment $\delta \to 0$ , we have $\hat { t } _ { k } ^ { I } - \hat { t } _ { k - 1 } ^ { I } $ $^ { 0 , }$ and $\mathcal { F } \big ( \hat { t } _ { k } ^ { I } \big ) - \mathcal { F } \big ( \hat { t } _ { k - 1 } ^ { I } \big )  0$ . Define

$$
\begin{array}{r l} & {\Psi = \underset {\hat {t} _ {k} ^ {I} - \hat {t} _ {k - 1} ^ {I} \to 0} {\lim} \sum_ {k = 1} ^ {r} \binom {N} {1} \left(\mathcal {F} \big (\hat {t} _ {k} ^ {I} \big) - \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big)\right) \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big) ^ {N - 1}} \\ & {\qquad = N \int_ {0} ^ {1} \mathcal {F} \big (\hat {t} _ {k} ^ {I} \big) ^ {N - 1} d \mathcal {F} \big (\hat {t} _ {k} ^ {I} \big).} \end{array}
$$

Using Riemann-Stieltjes integral (integration by parts), we can rewrite the above equation as

$$
\begin{array}{r l} & {\Psi = N \left[ \mathcal {F} \big (\hat {t} _ {k} ^ {I} \big) ^ {N - 1} \mathcal {F} \big (\hat {t} _ {k} ^ {I} \big) | _ {0} ^ {1} - \int_ {0} ^ {1} \mathcal {F} \big (\hat {t} _ {k} ^ {I} \big) (N - 1) \mathcal {F} \big (\hat {t} _ {k} ^ {I} \big) ^ {N - 2} d \mathcal {F} \big (\hat {t} _ {k} ^ {I} \big) \right]} \\ & {\qquad = N (\mathcal {F} (1) ^ {N} - \mathcal {F} (0) ^ {N}) - (N - 1) \Psi .} \end{array}
$$

Since $\mathcal { F } ( 1 ) ^ { N } - \mathcal { F } ( 0 ) ^ { N } = 1$ , we have Ψ=1, i.e., $\operatorname* { l i m } _ { M \to \infty } \widehat { \rho } ^ { I } ( 1 , N ) = 1$ . Using a similar approach, we can prove that for any $j \geq 2$ lim $\hat { \rho } ^ { I } ( j , N ) = 0$ ??→∞

Finally, following the derivations of Proposition 1 and Proposition2, we can establish that lim $\hat { t } _ { k } ^ { I } = \operatorname* { l i m } _ { M \to \infty } t _ { k } ^ { I } \left( k \geq 1 \right)$ . Thus, $\operatorname * { l i m } _ { M  \infty } ( \hat { \rho } ^ { I } ( j , N ) -$ ??→∞ $\rho ^ { I } ( j , N ) ) = 0$ . Combining the above results, we can obtain $\operatorname* { l i m } _ { M \to \infty } \hat { \alpha } - \alpha = 0$ . ∎

## Proof of Proposition 4

Let ?? denote the number of rounds taken to finish the auction under the hybrid mechanism. As discussed above, the probability that there is only one highest bidder in the first round (thus the auction takes two rounds to complete) is given by

$$
\hat {\rho} ^ {I} (1, N) = \sum_ {k = 1} ^ {r} \binom {N} {1} \left(\mathcal {F} \big (\hat {t} _ {k} ^ {I} \big) - \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big)\right) \mathcal {F} \big (\hat {t} _ {k - 1} ^ {I} \big) ^ {N - 1}.
$$

Combining the two possible scenarios (i.e., the auction ends in two rounds or one round):

$$
E (\lambda) = 2 \hat {\rho} ^ {I} (1, N) + \left(1 - \hat {\rho} ^ {I} (1, N)\right) = 1 + \hat {\rho} ^ {I} (1, N).
$$

Following the derivations of Proposition 3, for any finite $M , \hat { \rho } ^ { I } ( 1 , N ) < 1 . \mathrm { T h u s } , E ( \lambda ) < 2 .$ ∎

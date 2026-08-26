---
otero_id: 27670
otero_key: "Z6R68WC4"
title: "The Impact of Buy-Now Features in Pay-per-Bid Auctions"
authors: "Jochen Reiner; Martin Natter; Bernd Skiera"
year: "2014"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222310204"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/Z6R68WC4/fulltext/images/2f020cc2a5fe17a29e290ce74f85e30dbca3e9314b186beb7ed294ae336bc3a8.jpg)

![](/api/attachments/Z6R68WC4/fulltext/images/6344ac12a5287e5607e07f2e3be9a04a054244a3c3656560b361680d5fbeb330.jpg)

Click for updates

# Journal of Management Information Systems

Publication details, including instructions for authors and subscription information: http://www.tandfonline.com/loi/mmis20

# The Impact of Buy-Now Features in Payper-Bid Auctions

Jochen Reiner <sup>a</sup> , Martin Natter <sup>b</sup> & Bernd Skiera

<sup>a</sup> Faculty of Business and Economics, Goethe University Frankfurt, Germany

<sup>b</sup> Hans-Strothoff Chair of Retailing, Goethe University Frankfurt <sup>c</sup> Faculty of Business and Economics, Goethe University Frankfurt Published online: 07 Dec 2014.

To cite this article: Jochen Reiner , Martin Natter & Bernd Skiera (2014) The Impact of Buy-Now Features in Pay-per-Bid Auctions, Journal of Management Information Systems, 31:2, 77-104

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222310204

## PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the “Content”) contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and use can be found at http://www.tandfonline.com/page/termsand-conditions

# The Impact of Buy-Now Features in Pay-per-Bid Auctions

Jo chen Reinr , Mar tin Na tter , and Bernd Skiera

Jochen Reiner is a postdoctoral researcher in retailing at the Faculty of Business and Economics, Goethe University Frankfurt, Germany. His research focuses on innovative pricing and promotion mechanisms, retailing, online reviews, and pricing. His research has been published in the Journal of International Marketing.

Mar tin Natter is the Hans-Strothoff Chair of Retailing at Goethe University Frankfurt. He holds a Ph.D. from Vienna University of Economics and Business Administration and an M.S. in MIS from the University of Vienna. He is interested in retailing, pricing, and positioning. Dr. Natter is director of Goethe’s Incubator. His research has appeared in leading journals, such as Marketing Science, Management Science, and Journal of Marketing.

Ber nd Skier a is a Chaired Professor of Electronic Commerce at the Faculty of Business and Economics, Goethe University Frankfurt, and a member of the board of the E-Finance Lab. Before his academic career, he was a software developer for SAP. His research areas are online marketing, customer management, and pricing. His work has been published in, among others, Journal of Marketing, Journal of Marketing Research, Management Science, Marketing Science, Journal of Management Information Systems, International Journal of Electronic Commerce, Journal of Product Innovation Management, Journal of Service Research, and European Journal of Operational Research.

Abs tr act: Pay-per-bid auctions require all bidders to pay for every bid. However, paying bidding fees without receiving the auction item in return often causes high dissatisfaction among losers, resulting in heated discussions and high churn rates. To reduce these negative reactions, pay-per-bid auctioneers created the Buy-Now feature, which allows losers to put all or part of the bidding fees that they paid during an auction toward buying the auction item. Using unique data, including individual customer bidding histories and cost data from more than 6,800 pay-per-bid auctions, we find that, overall, the Buy-Now feature leads to more aggressive bidding behavior, attracts more bidders, increases loyalty, and results in a higher profit per auction. However, for voucher auctions that represent common value auctions, the Buy-Now feature causes a decrease in the number of bidders and the profit per auction, although we find an increase in the average number of bids per bidder. We also show theoretically that a bidder can pursue a risk-free bidding strategy. However, we find empirically that bidders rarely use this strategy.

Key wor ds and phr as es : Buy-Now feature, Buy-Now prices, electronic auctions, online marketing, online retailing, pay-per-bid auctions, penny auctions.

Pay-per -b id auctions (e.g., [1, 12, 13, 19, 21, 28]) are a fast-paced type of online auction that represent a new online trend [22]. Pay-per-bid auctions (also known as “penny auctions”) differ from well-known auctions such as eBay (e.g., [3, 10]) in several ways: Bidders pay a fee for every bid that they place, a bid can only change the price by a constant amount (i.e., a fixed increment), auctions have soft-close endings (i.e., every bid delays the end of the auction), and the auctioneer is usually also the seller of the product.

For example, an ascending pay-per-bid auction typically begins at <sup>€</sup>0.00. The product’s price increases by a fixed increment (e.g., <sup>€</sup>0.01) for every bid placed. A bidder pays a fee of <sup>€</sup>0.50 for every bid and each bid extends the auction by a specific time, usually up to 20 seconds. The auction ends when no new bid is placed within this time frame. The bidder who placed the final bid wins the auction and has the option of buying the product at the price of the final bid (i.e., the final price), which is usually much lower than the current retail price (CRP).

Currently, pay-per-bid auctions represent a multimillion-dollar industry that attracts a large number of bidders. For example, the Web monitoring company Compete (www.compete.com) reported that QuiBids (www.quibids.com), the most visited U.S. pay-per-bid auction site, had an average of 8 million unique monthly visitors to their U.S. site between April 2012 and April 2013. However, the market for pay-per-bid auctions has been highly competitive in recent years, with the rise and fall of many auctioneers. The most striking characteristic of pay-per-bid auctions is their use of bidding fees, which means that unsuccessful bidders leave auctions empty-handed after paying for their bids. Unsurprisingly, pay-per-bid auctions have sparked heated discussions in prominent newspapers (e.g., [28]), blogs (e.g., www.sitejabber.com/ websites/penny-auction/), and consumer protection agencies. Most of these discussions have reached negative conclusions. To reduce these negative reactions, many pay-per-bid auctioneers have introduced a Buy-Now feature (BNF). In the context of pay-per-bid auctions, the BNF allows a bidder, at any time in an auction, to use all or part (e.g., 50 percent) of the value of the bids placed during the auction toward buying the auction item. For example, assuming that a bidder can use 100 percent of the value of his or her bids and has already submitted 200 bids at a fee of <sup>€</sup>0.50 each for a product that is sold at a Buy-Now price (BNP) of <sup>€</sup>250, the bidder can subtract the <sup>€</sup>100 that he or she paid in bidding fees from the BNP to purchase the item for only an additional <sup>€</sup>150.

The actual amount of bids that can be put toward buying an auctioned item varies across pay-per-bid auctioneers. Although most auctioneers impute the full amount (100 percent) of placed bids, some limit the percentage of imputable bids (e.g., 75 percent, 50 percent, or 25 percent), which indicates that a consensus has yet to be reached on the optimal design of the BNF across auctioneers.

The aim of this study is to analyze theoretically and empirically the effect of the BNF on auctioneers’ profit per auction and bidder behavior. In our theoretical model, we investigate the differences in profit per auction among auctions with and without the BNF. Furthermore, we examine whether the BNF provides a benefit for the bidders. In our empirical study, we first investigate the effect of the BNF on the average number of bids per bidder, the number of bidders, and the profit per auction compared to those of auctions without the BNF. Then, we differentiate between product (private value) and voucher (common value) auctions. Finally, we investigate BNF usage, learning patterns, and the effects of the BNF on customer loyalty.

Our empirical analysis is based on the complete transaction and bidding data of a European provider of pay-per-bid auctions, and shows that product auctions with the BNF attract more bidders and increase their loyalty; the resulting higher average number of bids leads to higher prices. Together, these behavioral changes increase the profit per auction of the auctioneer. For voucher auctions we find a higher usage of the BNF, more aggressive bidding behavior, and a negative effect of BNF on the number of bidders and profit per auction.

We show that offering a BNF in which 100 percent of bids can be put toward purchasing an item in a pay-per-bid auction provides bidders with a “risk-free” strategy. Still, we empirically find that bidders rarely employ this strategy; hence, auctioneers benefit from the BNF because their bidders do not overuse the risk-free strategy. Regarding the bidders who actually use the BNF, we find that 14.85 percent of the analyzed bidders exhibit a significant learning effect over the course of their BNF usage experiences. Furthermore, we find that the deviation from the optimal number of bids decreases for bidders who won a higher number of auctions and who used the BNF more intensively. Interestingly, an increase in bidder experience does not lead to a smaller deviation.

Review of Related Literature

## Comparison of Pay-per-Bid Auctions and All-Pay Auctions

Pay-per -b id auctions s har e char acter is tics with all-pay auctions because both auctions require losers to pay (see, e.g., [4]). In pay-per-bid auctions, bidders have to pay for each bid, whereas in all-pay auctions, bidders have to pay for the bids that they submit. In both auctions, the winner is the bidder with the highest bid [14, p. 29]. All-pay auctions are typically used to model research and development (R&D) races (e.g., [9]), lobbying (e.g., [4]), or charity (e.g., [23]). Noussair and Silver [18] showed that all-pay auctions yield higher expected revenues than winner-pay auctions. Previous literature has also compared pay-per-bid auctions to wars of attrition (see, e.g., [6]) or Shubik’s dollar auctions [24], which are special types of all-pay auctions.

However, pay-per-bid auctions have several characteristics that distinguish them from the three aforementioned auction types in important ways: (1) none of these formats allow the actual winner to pay less than the losers [12]; (2) in pay-per-bid auctions, the main costs are, on average, the sum of the rather small bidding fees per bid; (3) bidders are not required to place a bid in every round to remain in the auction [15]; and (4) if a bid is placed, the price increases by a (relatively small) fixed amount.

## Review of the Literature on Pay-per-Bid Auctions

In recent years, several research papers have theoretically and empirically discussed various aspects of pay-per-bid auctions. Augenblick [1] analyzes the behaviors of bidders and auctioneers in pay-per-bid auctions by developing a theoretical model and analyzing large empirical data sets. Augenblick [1] finds that bidding behavior can be explained by a naive sunk cost fallacy. He shows that auctioneers face a high volatility of revenues (above and below the CRP) but generate positive profits overall. Bidders also learn to realize higher consumer surpluses, but at a slow rate, thus maintaining the profits of the auctioneers.

Platt et al. [19] develop a parsimonious model of rational bidders to predict particular distributions of ending prices in pay-per-bid auctions. The authors show that, with risk-neutral bidders, expected auction revenues are near the bidders’ valuation of the auction item but that some categories (namely, video game paraphernalia) show significantly higher revenues. Platt et al. [19] show that the incorporation of mild risk-loving preferences of bidders helps to explain the higher revenues in these categories.

Byres et al.’s [7] study builds on Platt et al.’s [19] model and analyzes information asymmetries (e.g., asymmetries in the perceived number of bidders and their valuations) in pay-per-bid auctions. Byres et al. find that even small asymmetries across bidders can increase auction duration and disproportionally skew the distribution of auctioneers’ profits.

Caldara [8] presents the first experimental study on pay-per-bid auctions, and shows that large profits of pay-per-bid auctions occur because of bidders’ mistakes and inexperience. A higher number of bidders in an auction leads to significantly higher auction revenues and overbidding.

Hinosaar [12] presents a game theoretical analysis of pay-per-bid auctions that generates stylized facts for pay-per-bid auctions and compares them to empirical data. He finds that high variance in outcomes is a general property of pay-per-bid auctions.

Kim et al. [13] compare ascending and descending pay-per-bid auctions. Their theoretical model comparison suggests revenue equivalence between different price increments in descending and ascending auctions. Kim et al. empirically find that the variance of the revenue per auction is higher in ascending auctions than in descending auctions. However, in contrast to their prediction (revenue equivalence), they find significant differences in revenues per auction. They explain these differences by factors such as the number of bidders and the type of the product category (whether hedonic or utilitarian).

Mittal [17] explores the possibility of describing bidding behavior using a unique Nash equilibrium. Assuming that bidders act symmetrically, the author is able to describe how bidders randomize overbidding and waiting in a particular round based on their expected utilities. The results are many Nash equilibria for pay-per-bid auctions, making the analysis cumbersome.

Wang and Xu [30] emphasize the importance of learning and strategic sophistication in a game and show that bidders’ behavior is better understood through a behavioral game theory approach than through equilibrium analyses that assume experienced and rational bidders.

## Review of the Literature on Buy-Now Feature in Auctions

A major problem in translating findings related to the BNF in pay-per-bid auctions is that most studies have focused on eBay auctions, which are English auctions (see, e.g., [5, 20]). The concepts behind English and pay-per-bid auctions are very different. In a pay-per-bid auction, the BNF represents an opportunity to reduce the price that the buyer has to pay after he or she has finished the auction. In contrast, in English auctions, the buyer needs to use the BNF before or during the auction. Thus, a user of the BNF in an English auction saves the effort (e.g., time) of participating in an auction but usually pays a BNP that is higher than the average final price of the English auction.

However, some findings regarding this feature’s impact on bidding behavior might be transferable. For example, Hidvégi et al. [11] provide evidence that the BNF attracts risk-averse bidders and Mathews [16] shows that the BNF attracts time-constrained bidders who would not otherwise participate. Furthermore, Standifird et al. [26] find that the BNF does not change the bidding behavior of eBay customers. In Standifird et al.’s field experiment, customers preferred the entertainment of the auctions to the BNP even when the BNP was set below the prevailing market price.

In terms of pay-per-bid auctions, there are four available studies that address the BNF. Byres et al. [7] examine the BNF and conclude that it transforms a bidder into a shill bidder, assuming that only one bidder uses the BNF and all others bidders bid as usual. Furthermore, they conclude that, when multiple bidders consider taking advantage of the BNF (i.e., use it as a safeguard), the auction becomes a variant of a game of chicken.

Wang and Xu [30] address the BNF in their analysis of bidding behavior and observe that the maximum number of bids that exceed the CRP decrease after the introduction of the BNF. The authors find mixed results for the profit implications of the BNF.

Lam [15] distinguishes between gift card auctions (common value auctions) and non–gift card auctions (private value auctions). He finds that gift card auctions with a BNF last longer and that non–gift card auctions end earlier than their counterparts without a BNF. Based on his analysis, he concludes that the BNF appears to increase bidding aggressiveness, particularly in the early rounds of the auction. In his study, Lam [15] shows that overall bidding increases when a BNF is present and that it leads to longer-lasting auctions and higher revenues for the auctioneer. Stix [27] also discusses the effect of the BNF in pay-per-bid auctions, and outlines that offering the BNF increases bidder retention.

The review of the literature shows that four studies have addressed the BNF in pay-per-bid auctions. However, all four of the above-mentioned studies—Byres et al. [7], Lam [15], Stix [27], and Wang and Xu [30]—are limited by the fact that their authors had no access to information on the actual usage of the BNF. Our data set contains all of the necessary information regarding the BNF, such as how many bids a bidder placed in a specific auction before he or she used (or did not use) the BNF, and product costs for the auctioneer, which allows us to calculate real profits per auction. Our individual bidding data enable us to evaluate bidding behavior and the resulting consumer surplus.

## Theoretical Framework

## Auctioneer Profit per Auction

The pr ofit $\pi _ { _ i }$ that an auctioneer makes in auction i of the set of all auctions I can be decomposed into three parts. The first part is the product margin received from the auction winner, which is generated by the selling of the product (called “product profit”), $\pi _ { i } ^ { p r o d u c t }$ <sup>t</sup>, and is given by the auction ending price $p _ { i } ^ { f u a l }$ minus the product cost $c _ { i } { \mathrm { : } }$

$$
\pi_ {i} ^ {\text { product }} = p _ {i} ^ {\text { final }} - c _ {i} \quad (i \in I).\tag{1}
$$

The second part is the profit that is generated by bidding fees (called “bidding profit”), $\pi _ { _ i } ^ { b i d d i n g }$ , which is the number of bids $n _ { _ i }$ times the fee per bid $b _ { _ i \cdot } ^ { \cdot }$

$$
\pi_ {i} ^ {\text { bidding }} = n _ {i} \cdot b _ {i} \quad (i \in I).\tag{2}
$$

The third part is the profit that is generated by offering a BNF (called “Buy-Now profit”), $\pi _ { i } ^ { b u y n o w }$ , which is given by

$$
\pi_ {i} ^ {\text { buynow }} = \left(B N P _ {i} - c _ {i}\right) \cdot \frac {n _ {i} \cdot b _ {i} \cdot \alpha_ {i} \cdot \gamma_ {i}}{\delta_ {i} \cdot B N P _ {i}} - n _ {i} \cdot b _ {i} \cdot \alpha_ {i} \cdot \gamma_ {i} \quad (i \in I).\tag{3}
$$

Rearranging Equation (3) yields

$$
\pi_ {i} ^ {\text { buynow }} = \left[ \frac {(1 - \delta_ {i}) \cdot B N P _ {i} - c _ {i}}{\delta_ {i} \cdot B N P _ {i}} \right] \cdot n _ {i} \cdot b _ {i} \cdot \alpha_ {i} \cdot \gamma_ {i} \quad (i \in I).\tag{4}
$$

The Buy-Now price $( B N P _ { i }$ ; frequently the CRP) in auction i is usually larger than the product cost $c _ { \scriptscriptstyle i } \delta _ { \scriptscriptstyle i }$ indicates the share of the BNP for which bidding fees are imputed. For example, if a bidder has placed bids worth $\yen 70$ on a product that has a BNP of <sup>€</sup>100, then $\delta _ { \mathrm { { i } } } = 7 0$ percent. $\mathbf { \alpha } _ { \mathrm { ~ \it ~ \ / ~ d ~ } }$ represents the share of bids that each bidder is permitted to apply toward the BNF in auction $i . \Upsilon _ { i }$ denotes the share of bids from all bidders that use the BNF. We distinguish between $\mathbf { \alpha } _ { \mathfrak { i } }$ and $\gamma _ { i }$ because the provider of the auction determines $\alpha _ { _ i } ( \mathrm { e . g . , } \alpha _ { _ i } = 1 0 0$ percent), whereas the bidders determine $\gamma _ { i } ,$ that is, they decide whether to use the BNF. For example, $\gamma _ { i } = 3 0$ percent means that 30 percent of all bids placed during auction i have been imputed to the BNF.

The first term on the right-hand side of Equation (3), $( B N P _ { i } - c _ { i } )$ , reflects the Buy-Now margin of the product that is sold via the BNF. The second term, $n _ { i } \cdot b _ { { \scriptscriptstyle i } } \cdot \mathbf { \alpha } \cdot \boldsymbol { \gamma } _ { { \scriptscriptstyle i } } / \delta _ { { \scriptscriptstyle i } } \cdot B N P _ { { \scriptscriptstyle i } { \mathrm { : } } }$ indicates the number of products that are sold via the BNF. To determine the number of products, we divide the sum of the bidding fees $n _ { _ i } \cdot b _ { _ i } \cdot \mathbf { \vec { x } } _ { i } \cdot \boldsymbol { \gamma } _ { i }$ that bidders put toward the BNF by the average sum of the bidding fees at which bidders cash in the BNF $( { \boldsymbol { \delta } } _ { \cdot } \cdot { \boldsymbol { B } } { \boldsymbol { N } } P _ { \cdot } )$ . The third term, $n _ { _ i } \cdot b _ { _ i } \cdot \mathbf { \vec { x } } _ { i } \cdot \boldsymbol { \gamma } _ { i }$ , indicates the sum of the bidding fees that bidders put toward the BNF. This sum of bidding fees has to be subtracted from the bidding profit.

The final price $p _ { i } ^ { f n a l }$ is the sum of the starting price $s _ { i }$ and the product of the increment $d _ { i }$ and the number of bids $n _ { _ i }$ in auction $i \colon$

$$
p _ {i} ^ {\text { final }} = s _ {i} + n _ {i} \cdot d _ {i} (i \in I).\tag{5}
$$

The profit in auctions without a BNF $( \pi _ { i } ^ { n o B N } )$ consists of the product and bidding profits (Equations (1) and (2)). Substituting Equation (5) into the sum of Equations (1) and (2) yields the profit in auctions without a BNF:

$$
\pi_ {i} ^ {n o B N} = \pi_ {i} ^ {p r o d u c t} + \pi_ {i} ^ {b i d d i n g} = s _ {i} + n _ {i} \cdot (d _ {i} + b _ {i}) - c _ {i} \quad (i \in I).\tag{6}
$$

In contrast, the profit in auctions with the BNF $( \pi _ { i } ^ { B N } )$ consists of the sum of the product, bidding, and Buy-Now profits (Equations (1), (2) and (4)):

$$
\pi_ {i} ^ {B N} = \pi_ {i} ^ {\text { product }} + \pi_ {i} ^ {\text { bidding }} + \pi_ {i} ^ {\text { buynow }}
$$

$$
= s _ {i} + n _ {i} \cdot \left(d _ {i} + b _ {i}\right) - c _ {i} + \left[ \frac {\left(1 - \delta_ {i}\right) \cdot B N P _ {i} - c _ {i}}{\delta_ {i} \cdot B N P _ {i}} \right] \cdot n _ {i} \cdot b _ {i} \cdot \alpha_ {i} \cdot \gamma_ {i} \quad (i \in I).\tag{7}
$$

If the BNF does not affect bidding behavior $( \mathrm { i . e . }$ , the number of bids), the difference in profits (∆π ) between an auction i with and without the BNF is given by subtracting Equation (6) from Equation (7):

$$
\Delta \pi_ {i} = \pi_ {i} ^ {B N} - \pi_ {i} ^ {n o B N} = \left[ \frac {\left(1 - \delta_ {i}\right) \cdot B N P _ {i} - c _ {i}}{\delta_ {i} \cdot B N P _ {i}} \right] \cdot n _ {i} \cdot b _ {i} \cdot \alpha_ {i} \cdot \gamma_ {i} (i \in I).\tag{8}
$$

Because all parameters are positive, the difference in profit remains positive if

$$
\left(1 - \delta_ {i}\right) \cdot B N P _ {i} > c _ {i} \quad (i \in I).\tag{9}
$$

Inequality (9) shows that the BNF only has a positive impact on profit when bidders cash in the BNF with a sum of bidding fees that is smaller, on average, than the Buy-Now margin. For example, a product with a CRP of <sup>€</sup>100 and a cost of <sup>€</sup>70 results in a Buy-Now margin of <sup>€</sup>30. If the bidders use the BNF with an average sum of bidding fees greater than <sup>€</sup>30 $( \mathrm { i } . \mathrm { e } . , \delta _ { _ i } > 0 . 3 )$ , the auctioneer loses money by offering the BNF.

The worst case for the auctioneer is that bidders always cash in the BNF with a sum of bidding fees that is equal to the $B N P _ { i }$ such that $\ S _ { \ O _ { i } } = 1$ . The auctioneer then always realizes a loss unless the product costs are zero (see inequality (9)).

Equation (7) shows that, all else being equal, the profit $\pi _ { i } ^ { B N }$ increases with (1) a decrease in product cost $c _ { i } ; ( 2 )$ a decrease in $\delta _ { \mathrm { { } } i } ,$ the share of the BNP for which bidding fees are imputed; (3) an increase in $B N P _ { i } ; ( 4 )$ an increase in the number of bids, $n _ { { } _ { i } } ;$ and (5) an increase in the bidding fee, $b _ { _ i }$ . The effects of $\mathbf { \alpha } _ { \mathrm { ~ i ~ } } ^ { \mathbf { { \alpha } } }$ (the share of bids that each bidder is permitted to apply toward the BNF) and $\gamma _ { i }$ (the share of bids from all bidders that use the BNF) depend on $\ S _ { _ i }$ , the share of the BNP for which bidding fees are imputed. If $\ S _ { _ i }$ is low, so that $( 1 - \delta _ { i } ) \cdot B N P _ { _ i } > c _ { i } ,$ the profit $\pi _ { i } ^ { B N }$ increases with an increase in ${ \bf \alpha } _ { i }$ and $\gamma _ { i } .$ . The opposite effect occurs if $\ S _ { _ i }$ is high, so that $( 1 - \delta _ { i } ) \cdot B N P _ { _ i } { < } c _ { i }$

In the following, we account for the possibility that the number of bids $n _ { _ i }$ may differ between auctions with and without the BNF. Such differences may occur, for example, because of an increase in the average number of bids per bidder or an increase in the number of bidders (see, e.g., [15]). The difference in the number of bids between an auction i with and without the BNF is represented by $\Delta n _ { i }$

Extending Equation (7) to include the difference in the number of bids, $\Delta n _ { _ i } { = } n _ { _ i } ^ { { B N } } { - } n _ { _ i } ^ { { n o } B N }$ , yields

$$
\begin{array}{c} \pi_ {i} ^ {B N ^ {\prime}} = s _ {i} + (n _ {i} + \Delta n _ {i}) \cdot (d _ {i} + b _ {i}) - c _ {i} + \left[ \frac {(1 - \delta_ {i}) \cdot B N P _ {i} - c _ {i}}{\delta_ {i} \cdot B N P _ {i}} \right] \\ \cdot (n _ {i} + \Delta n _ {i}) \cdot b _ {i} \cdot \alpha_ {i} \cdot \gamma_ {i} \quad (i \in I). \end{array}\tag{10}
$$

The difference in profit $( \Delta \pi _ { i } ^ { \prime } )$ between auction i with and without the BNF (Equations (6) and (10)) equals

$$
\begin{array}{l} \Delta \pi_ {i} ^ {\prime} = \pi_ {i} ^ {B N ^ {\prime}} - \pi_ {i} ^ {n o B N ^ {\prime}} = \frac {\alpha_ {i} \cdot b _ {i} \cdot \gamma_ {i} \cdot (\Delta n _ {i} + n _ {i}) \cdot (c _ {i} - (1 - \delta_ {i}) \cdot B N P _ {i})}{\delta_ {i} \cdot B N P _ {i}} - \Delta n _ {i} (b _ {i} + d _ {i}) \\ = \Delta n _ {i} (b _ {i} + d _ {i}) + \left[ \frac {(1 - \delta_ {i}) \cdot B N P _ {i} - c _ {i}}{\delta_ {i} \cdot B N P _ {i}} \right] \cdot \alpha_ {i} \cdot b _ {i} \cdot \gamma_ {i} \cdot (\Delta n _ {i} + n _ {i}) (i \in I). \end{array}\tag{11}
$$

The first term $\Delta n _ { _ i } ( b _ { _ i } + d _ { _ i } )$ represents the change in (1) the product profit, that is, the final price, which is the product of $\Delta n _ { i }$ and the increment $d _ { i { : } i }$ , and (2) the bidding profit, which is the product of $\Delta n _ { _ i }$ and the bidding fee $b _ { _ i }$ . The second and third terms describe the Buy-Now profit that results from the difference in the number of bids $\Delta n _ { _ i }$ . This result indicates that the Buy-Now margin $( ( 1 - \delta _ { i } ) \cdot B N P _ { i } - c _ { i } )$ increases or decreases with $\Delta n _ { _ i }$ . Thus, comparable to Equation (9), the size of the Buy-Now profit depends on whether bidders cash in the BNF with an average sum of bidding fees that is smaller than the Buy-Now margin.

## Bidding Behavior

We now investigate the impact of the BNF on the behavior of bidders who maximize consumer surplus. When no BNF is available, the consumer surplus $C S _ { i , j , r } ^ { n o B N }$ for bidder j for placing an additional bid r at a price $p _ { i , r }$ in auction i is given by

$$
C S _ {i, j, r} ^ {n o B N} = \left(W T P _ {i, j} - p _ {i, r}\right) \cdot \operatorname * {P r} \left(p _ {i, r} = p _ {i} ^ {\text { final }}\right) - b _ {i} \quad (i \in I, j \in J, r \in R).\tag{12}
$$

The consumer surplus $C S _ { i , j , r } ^ { n o B N }$ for bid r consists of bidder j’s individual willingness to pay for the product in auction i minus the current price of the product $( \boldsymbol { p } _ { i , r } )$ times the probability that the price $p _ { i , r }$ will win the auction $( \mathrm { P r } ( p _ { i , r } = p _ { i } ^ { f n a l } ) )$ . Finally, the bidding fee $( b _ { _ i } )$ for the additional bid has to be subtracted.

We assume a bidder-specific willingness to pay that allows for individual evaluations of the product in auction i. As a consequence, the bidder-specific willingness to pay also allows for different bidding strategies, as found by Bapna et al. [2]. In the case where a BNF is available, Equation (12) needs to be extended by the option value $( O V _ { i , j , r } )$ of the BNF. The BNF represents an option for the bidders because each bidder can, but does need not to, use it. Consequently, its value cannot be negative. The option value for bidder j in auction i at bid r who has already submitted $n _ { i , j , r }$ bids equals

$$
O V _ {i, j, r} = \max \left\{W T P _ {i, j} - B N P _ {i} + n _ {i, j, r} \cdot b _ {i} \cdot \alpha_ {i}; 0 \right\} \quad (i \in I, j \in J, r \in R).\tag{13}
$$

Adding the option value to the consumer surplus of auctions without the BNF, that is, Equation (12), yields

$$
\begin{array}{c} C S _ {i, j, r} ^ {B N} = \left(W T P _ {i, j} - p _ {i, r}\right) \cdot \operatorname * {P r} \left(p _ {i, r} = p _ {i} ^ {\text { final }}\right) - b _ {i} \\ + \max \left\{W T P _ {i, j} - B N P _ {i} + n _ {i, j, r} \cdot b _ {i} \cdot \alpha_ {i}; 0 \right\} \quad (i \in I,   j \in J,   r \in R). \end{array}\tag{14}
$$

The term $W T P _ { _ { i , j } } - B N P _ { _ i } + { n _ { _ { i , j , r } } } \cdot { b _ { _ i } } \cdot { \bf { \sigma } } _ { \alpha _ { _ i } }$ represents the value of the BNF in auction i for bidder j. The value of the BNF option consists of the bidder-specific willingness to pay $( W T P _ { i , j } )$ , from which the Buy-Now price of auction $i ( B N P _ { i } )$ has to be subtracted and the sum of the bidding fees that bidders put toward $( \mathsf { \alpha } \mathsf { \alpha } _ { i } = { \mathrm { s h a r e } }$ of permitted bids) the BNF.

A positive option value for the BNF occurs if $W T P _ { _ { i , j } } - B N P _ { _ i } + n _ { _ { i , j , r } } \cdot b _ { _ i } \cdot \alpha _ { _ i } > 0$ , that is, if bidder j makes at least the following number of bids:

$$
n _ {i, j, r} ^ {\text { lower }} \geq \frac {B N P _ {i} - W T P _ {i , j}}{b _ {i} \cdot \alpha_ {i}} \quad (i \in I, j \in J, r \in R, b _ {i} \cdot \alpha_ {i} > 0).\tag{15}
$$

Because the option is only valuable for the bidder after reaching this number of bids, it can be considered the lower threshold. The bidder can buy the product in auction i via the BNF only at the $B N P _ { i } .$ Therefore, the maximum number of bids is limited by the following inequality:

$$
n _ {i, j, r} \cdot b _ {i} \cdot \alpha_ {i} \leq B N P _ {i} (i \in I, j \in J, r \in R).\tag{16}
$$

The bidder additionally has to consider the actual price $p _ { i , r }$ in the auction, which the bidder has to pay if he or she wins the auction with bid r. However, the price $p _ { i , r }$ is usually small compared to the $B N P _ { i }$ . Thus, the upper threshold for the bidder’s number of bids is

$$
n _ {i, j, r} ^ {\text {upper}} = \frac {B N P _ {i} - p _ {i , r}}{b _ {i} \cdot \alpha_ {i}} \quad (i \in I, j \in J, r \in R, b _ {i} \cdot \alpha_ {i} > 0).\tag{17}
$$

It is interesting to analyze the situation of a bidder who has submitted more bids than $n _ { { } _ { i , j , r } } \geq n _ { { } _ { i , j , r } } ^ { { } _ { l o w e r } }$ but fewer bids than $n _ { i , j , r } \leq n _ { i , j , r } ^ { \ u p p e r }$ . In this case, the bidder can either cash in his or her option value or submit another bid.

Thus, the bidder’s change in consumer surplus from submitting another bid is

$$
\begin{array}{l} C S _ {i, j, r + 1} ^ {B N} - O V _ {i, j, r} = \Big [ \Big (W T P _ {i, j} - p _ {i, r + 1} \Big) \cdot \operatorname * {P r} \Big (p _ {i, r} = p _ {i} ^ {\text { final }} \Big) - b _ {i} + W T P _ {i, j} - B N P _ {i} \\ \qquad + \Big (n _ {i, j, r} + 1 \Big) \cdot b _ {i} \cdot \alpha_ {i} \Big ] - \Big [ W T P _ {i, j} - B N P _ {i} + n _ {i, j, r} \cdot b _ {i} \cdot \alpha_ {i} \Big ] \\ \qquad = \Big (W T P _ {i, j} - p _ {i, r + 1} \Big) \cdot \operatorname * {P r} \Big (p _ {i, r} = p _ {i} ^ {\text { final }} \Big) - b _ {i} \cdot \big (1 - \alpha_ {i} \big) \\ \left(i \in I,   j \in J,   r \in R,   \frac {B N P _ {i} - W T P _ {i , j}}{b _ {i} \cdot \alpha_ {i}} \leq n _ {i, j, r} \leq \frac {B N P _ {i} - p _ {i , r}}{b _ {i} \cdot \alpha_ {i}},   b _ {i} \cdot \alpha_ {i} > 0\right). \end{array}\tag{18}
$$

Thus, as long as $\mathsf { q } _ { \cdot _ { i } } < 1$ , the difference in consumer surplus can be positive or negative. However, if $\alpha _ { _ i } = 1$ , Equation (18) reduces to

$$
\begin{array}{c} C S _ {i, j, r + 1} ^ {B N, \alpha = 1} - O V _ {i, j, r} ^ {\alpha = 1} = \left(W T P _ {i, j} - p _ {i, r + 1}\right) \cdot \operatorname * {P r} \left(p _ {i, r} = p _ {i} ^ {\text { final }}\right) \geq 0 \\ \left(i \in I,   j \in J,   r \in R,   \frac {B N P _ {i} - W T P _ {i , j}}{b _ {i}} \leq n _ {i, j, r} \leq \frac {B N P _ {i} - p _ {i , r}}{b _ {i}}, b _ {i} > 0\right). \end{array}\tag{19}
$$

This solution is remarkable because a bidder can simply increase his or her consumer surplus by submitting more bids after the option value becomes positive (i.e., after the number of bids reaches the lower threshold). Thus, a bidder cannot lose money by bidding more (up to the upper number of bids defined in Equation (17)), whereas other bidders whose option values are still negative can lose money, depending on each bidder’s individual willingness to pay.

Thus, when $\mathsf { \alpha } _ { \mathrm { \alpha } _ { i } } = 1 0 0$ percent, bidders who have placed a number of bids higher than their individual lower thresholds but lower than the upper threshold can follow a risk-free bidding strategy by continuing to place bids until they either win the auction or stop bidding and cash in their option value. Thus, the risk-free bidding strategy supports the expectation that the BNF reduces extreme losses. However, if two or more bidders simultaneously follow the risk-free bidding strategy, they will outbid one another until they reach their upper thresholds. As soon as the bidders use the BNF, they will leave the auction without a gain because their sum of bidding fees equals the BNP . A consequence of the risk-free bidding strategy might be that the BNF leads to higher final prices that would be less attractive to the winners of the auction.

Although we do not formally link the theoretical framework for bidding behavior with that of the auctioneers’ profit per auction, the two views help us in formulating propositions regarding the design of these auctions that impact bidding behavior and, ultimately, the profit per auction. Setting the share of bids that each bidder is permitted to apply toward the BNF at 100 percent, that is, ${ \bf Q } _ { i } = 1$ , leads to a risk-free bidding strategy that provides a strong incentive to increase the number of bids, which will also increase the share of the BNP for which bidding fees are imputed, $\ S _ { _ i }$ . The latter increase is particularly dangerous for the auctioneer because it might lead to a situation, that is, $( 1 - \delta _ { i } ) \cdot B N P _ { _ i } { < } c _ { i } ,$ , in which the auctioneer realizes a loss.

## Propositions

Bas ed on our theor etical analys es of auctioneer pr ofit per auction and bidder behavior and the related literature, we develop propositions that we test in our empirical analysis.

## Auctioneer Profit per Auction

The BNF prevents bidders from incurring high losses. As a consequence, the BNF might attract additional bidders. Therefore, we propose the following:

Proposition 1: Auctions with a BNF attract more bidders than auctions without a BNF.

Furthermore, the limited losses and the identified risk-free bidding strategy should increase the number of bids per bidder:

Proposition 2: Auctions with a BNF have a higher average number of bids placed per bidder.

As a consequence of a higher average number of bids per bidder and an increased number of bidders (see Propositions 1 and 2), we expect that more bids will be placed in auctions with a BNF and that the final prices that winners pay will rise [8, 15]. Equations (9) and (11) show that, as long as $( 1 - \delta _ { i } ) \cdot B N P _ { _ i } > c _ { i } ,$ a higher number of bids placed in auctions leads to a positive Buy-Now profit and thus to a higher profit per auction with the BNF:

Proposition 3a: Auctions with a BNF result in final prices that are higher than those in auctions without a BNF.

Proposition 3b: Auctions with a BNF result in profits per auction that are higher than those in auctions without a BNF.

Pay-per-bid auctions can be divided into voucher auctions (which represent common value auctions) and product auctions (which represent private value auctions). Products, such as computers, video games, or cell phones, are valued individually, whereas vouchers, such as bid packages, gift cards, gold bars, or cash, have identical values for all bidders. In line with Lam [15] and Stix [27], we argue that bidders evaluate these two auction types differently. The auctioned vouchers represent a pure monetary value that is defined; in this case, even small gains are a clear benefit. In contrast, in the product auctions, bidders might have different valuations, thus the benefits are less obvious.

We assume that the willingness to pay for vouchers is close or equal to the BNP. We therefore expect a higher average number of bids to be placed in voucher auctions. With respect to the number of bidders, we anticipate to observe a higher number of bidders in voucher auctions than in product auctions. Our reasoning is that voucher auctions have a higher average value for the bidders (WTP is closer to BNP). Due to the more visible benefits in voucher auctions, we expect that more bidders in these auctions will employ the BNF such that $( 1 - \delta _ { i } ) \cdot B N P _ { _ i } > c _ { i }$ does not hold and the Buy-Now profit becomes negative (cf. [30]). Accordingly, we state the following propositions:

Proposition 4a: The BNF results in a higher average number of bids per bidder in voucher (common value) auctions than in product (private value) auctions.

Proposition 4b: The BNF results in a higher number of bidders in voucher auctions than in product auctions.

Proposition 4c: The BNF results in higher final prices in voucher auctions than in product auctions.

Proposition 4d: The BNF results in a lower profit per auction in voucher auctions than in product auctions.

From the auctioneer’s perspective, it is interesting to know which products to select for an auction with a BNF. Equation (9) indicates that products with higher margins are more likely to realize a positive Buy-Now profit (see Equation (7)). Thus, we expect that products with higher margins will realize higher profits in auctions with a BNF than products with lower product margins:

Proposition 5: The BNF yields a higher profit with increasing product margins.

## Bidding Behavior

With respect to BNF usage, Equations (15) and (17) present the lower and upper thresholds of the risk-free strategy. Bidders should be aware of the upper threshold and the favorability of the BNF because the additional amount of money that they have to pay when using the BNF is displayed on the screen. Consequently, we assume that bidders will especially use the BNF when they have already paid a substantial amount for bids in an auction:

Proposition 6: A higher number of bids that are already placed by one bidder in an auction increases the bidder’s likelihood of using the BNF.

A willingness to pay that is closer to the BNP in voucher auctions leads to a faster increase in the option value (see Equation (13)). As a consequence, using the BNF becomes more attractive for bidders because they can apply their paid sum of bidding fees toward buying the auctioned item instead of leaving the auction empty-handed and with a loss. Thus, we expect that bidders will use the BNF more often in voucher auctions:

Proposition 7: The BNF is used more often in voucher (common value) auctions than in product (private value) auctions.

If an auctioneer allows bidders to apply all of the value of the bids placed during the auction toward buying the auction item (i.e., a =1), bidders can follow a risk-free bidding strategy after their option value becomes positive. However, we expect that it will take some time [1] for the bidder to identify the risk-free bidding strategy:

Proposition 8: Bidders learn to use the risk-free bidding strategy over time.

The BNF offers the possibility of reducing extreme losses. Because these extreme losses have caused high churn, we expect that the introduction of a BNF will increase the loyalty of the bidders who use it. However, because winning an auction is usually more attractive than purchasing a product via the BNF, we hypothesize that winning an auction has a stronger positive impact on loyalty than the use of the BNF. We also expect that bidders who win auctions and avoid losses by using the BNF will exhibit the highest loyalty:

Proposition 9a: Bidders who have already used the BNF but never won an auction are more loyal than bidders who have never used the BNF and never won an auction.

Proposition 9b: Bidders who have already won auctions but never used the BNF are more loyal than bidders who have never won an auction but used the BNF.

Proposition 9c: Bidders who have already won auctions and used the BNF are more loyal than bidders who have already won auctions but never used the BNF.

## Data and Descriptive Analysis

Our em pir ical analys es ar e b as ed on com plete tr ans action and bidding data from a European pay-per-bid auctioneer. Our data set contains information on 6,812 auctions in 12 categories auctioned at three increments and covers 6.244 million bids placed by 83,867 unique bidders between August 2009 and May 2010. The data are unique in several ways. First, the 6,812 auctions offer both auction types—with and without the BNF—over the entire period of study. Second, the data set contains the costs of the auctioned items; hence, we can use precise cost information to calculate profits. In total, we analyzed 5,587 auctions (82.02 percent) that offered the BNF and 1,225 (17.98 percent) auctions that did not. In our data set, all of the auctions that offered the BNF allowed for the imputation of all bids placed during the auction (i.e., ${ \bf Q } _ { i } = 1 0 0$ percent). Across all categories, we observe an average of 70.59 bidders per auction, with a maximum of 1,185 bidders and a minimum of two bidders per auction. With respect to the number of bids placed, we find a mean value of 9.36 (minimum = 1.00, maximum = 99.40) for the average number of bids.

On average, final prices correspond to 7.08 percent of the CRPs, indicating that the winners of these auctions saved, on average, 92.92 percent. Nevertheless, the average profit for the auctioneer is <sup>€</sup>233.20 per auction. However, this profit per auction varies substantially (standard deviation of <sup>€</sup>722.18) such that 36.83 percent of all auctions yield a loss. We find an average value of <sup>€</sup>203.15 for the CRPs of the auctioned items, with a standard deviation of <sup>€</sup>245.42, which shows that the values of products differ substantially (minimum = <sup>€</sup>12.97; maximum = <sup>€</sup>1,363.90). An interesting aspect of our data is the cost information. We find that costs are, on average, 84.44 percent of the CRP, which equals the BNP. Thus, the average margin of the auctioned products equals 15.56 percent.

With respect to BNF use (see Table 1), we observe that, in auctions where the BNF is offered, an average of 1.26 products (= units) are sold via this feature per auction. However, the voucher category is an exception; an average of 6.67 vouchers is sold via the BNF per auction. The higher BNF usage in the voucher category provides support for Proposition 7 $( p < 0 . 0 1 )$ .

We find that only three of the other product categories (notebooks, cell phones, and navigation) exhibit a mean BNF use per auction greater than one. Thus, in most (i.e., eight) categories, on average, less than one bidder uses the BNF per auction. For example, in the fun category, less than 50 percent of the auctions exhibit BNF usage. In terms of the price increment, we observe that 4,798 auctions feature a 1-cent increment (84.16 percent with BNF), 1,366 auctions use a 2-cent increment (71.96 percent with BNF), and 648 auctions use a 5-cent increment (87.35 percent with BNF). Thus, the number of auctions decreases with an increase in the increment.

Table 1. Overview of Bidder’s Usage of Buy-Now Feature per Auction

<table><tr><td>Category</td><td>Average number of times BNF was used per auction</td><td>Average number of products sold via BNF</td><td>Number of auctions (BNF in percent)</td></tr><tr><td>Vouchers</td><td>6.674</td><td>2,910</td><td>1,272(34.3)</td></tr><tr><td>Cell phones</td><td>1.101</td><td>545</td><td>558(88.7)</td></tr><tr><td>Notebooks</td><td>1.055</td><td>326</td><td>413(74.8)</td></tr><tr><td>Navigation</td><td>1.051</td><td>184</td><td>177(98.9)</td></tr><tr><td>Video games</td><td>0.887</td><td>986</td><td>1,179(94.3)</td></tr><tr><td>Audio</td><td>0.760</td><td>349</td><td>465(98.7)</td></tr><tr><td>Camcorders</td><td>0.700</td><td>250</td><td>380(93.9)</td></tr><tr><td>Computers</td><td>0.674</td><td>289</td><td>435(98.6)</td></tr><tr><td>Lifestyle</td><td>0.628</td><td>270</td><td>479(89.8)</td></tr><tr><td>Home and garden</td><td>0.566</td><td>286</td><td>517(97.7)</td></tr><tr><td>Video</td><td>0.538</td><td>397</td><td>777(95.0)</td></tr><tr><td>Fun</td><td>0.493</td><td>70</td><td>160(88.8)</td></tr><tr><td>Mean/sum</td><td>1.261</td><td>6,862</td><td>6,812(82.02)</td></tr><tr><td colspan="4">Note: BNF = Buy-Now feature. N = 6,812.</td></tr></table>

## Empirical Analysis

## Auctioneer Profit per Auction

To as es Pr opos itions 1–3, we employ linear regressions to capture the effect of the BNF on the auctioneer profit per auction $( \pi _ { i } )$ , the number of bidders $( n b _ { _ i } )$ , and the average number of bids per bidder in auction $i ( a b _ { \cdot } )$ . The product of $n b _ { _ i }$ and $a b _ { _ i }$ determines the number of bids $n _ { _ i }$ per auction $( \boldsymbol { n } _ { \scriptscriptstyle i } = \boldsymbol { n } \boldsymbol { b } _ { \scriptscriptstyle i } \cdot \boldsymbol { a } \boldsymbol { b } _ { \scriptscriptstyle i } )$ and, consequently, the final price $( p _ { i } ^ { f n a l } = n _ { i } \cdot d _ { i } )$ . Equations (20)–(22) present our model:

$$
a b _ {i} = \eta_ {0} + \eta_ {1} \cdot B N F _ {i} ^ {\text { yes }} + \eta_ {2} \cdot \ln (C R P _ {i}) + \sum_ {g = 1} ^ {1 1} \eta_ {2 + g} \cdot \text { Category } _ {i} + \sum_ {u = 1} ^ {2} \eta_ {1 3 + u} \cdot \text { inc } _ {i}\tag{20}
$$

$$
+ \sum_ {b = 1} ^ {6} \eta_ {1 5 + b} \cdot \text { Weekday } _ {i} + \sum_ {m = 1} ^ {9} \eta_ {2 1 + m} \cdot \text { Month } _ {i} + \sum_ {v = 1} ^ {2 3} \eta_ {3 0 + v} \cdot \text { Hour } _ {i} + \eta_ {5 4} \cdot \text { Payday } _ {i} + \varepsilon_ {i}
$$

$$
n b _ {i} = \beta_ {0} + \beta_ {1} \cdot B N F _ {i} ^ {\text { yes }} + \beta_ {2} \cdot \ln (C R P _ {i}) + \sum_ {w = 1} ^ {1 1} \beta_ {2 + w} \cdot C a t e g o r y _ {i} + \sum_ {e = 1} ^ {2} \beta_ {1 3 + e} \cdot i n c _ {i}
$$

$$
+ \sum_ {z = 1} ^ {6} \beta_ {1 5 + z} \cdot \text { Weekday } _ {i} + \sum_ {t = 1} ^ {9} \beta_ {2 1 + t} \cdot \text { Month } _ {i} + \sum_ {p = 1} ^ {2 3} \beta_ {3 0 + p} \cdot \text { Hour } _ {i} + \beta_ {5 4} \cdot \text { Payday } _ {i} + \zeta_ {i}\tag{21}
$$

$$
\pi_ {i} = \mu_ {0} + \mu_ {1} \cdot B N F _ {i} ^ {\text { yes }} + \mu_ {2} \cdot \ln (C R P _ {i}) + \sum_ {k = 1} ^ {1 1} \mu_ {2 + k} \cdot C a t e g o r y _ {i} + \sum_ {s = 1} ^ {2} \mu_ {1 3 + s} \cdot i n c _ {i}\tag{22}
$$

$$
+ \sum_ {g = 1} ^ {6} \mu_ {1 5 + g} \cdot \text { Weekday } _ {i} + \sum_ {f = 1} ^ {9} \mu_ {2 1 + f} \cdot \text { Month } _ {i} + \sum_ {a = 1} ^ {2 3} \mu_ {3 0 + a} \cdot \text { Hour } _ {i} + \mu_ {5 4} \cdot \text { Payday } _ {i} + \varsigma_ {i}.
$$

We model the effect of the availability of the BNF $( B N F _ { i } ^ { y e s } = 1 )$ on the average number of bids per bidder in auction $i ( a b _ { \cdot } )$ in Equation (20), on the number of bidders $( n b _ { _ i } )$ in Equation (21), and on the auctioneer profit per auction $( \pi _ { i } )$ in Equation (22). In all three equations, we control for the logarithm current retail price $( \ln ( C R P _ { i } ) )$ to account for differences in the values of the auctioned items. The different product category effects are captured via 11 category dummies $( C a t e g o r y _ { i } )$ and two increment dummies $( i n c _ { i } )$ control for the effects of different increments among the auctions (see, e.g., [13]). We additionally employed $6 + 9 + 2 3 = 3 8$ binary variables to control for time effects; namely, the day of the week $( W e e k d a y _ { i } )$ , the month $( M o n t h _ { _ i } )$ , and the time of day (i.e., the hour the auction started $[ H o u r _ { i } ] )$ . We also control for payday effects $( \mathrm { i . e . }$ , the first three days of a month $[ P a y d a y _ { i } ] )$ , which may influence bidders budgets. The error terms of the equations are represented by $\varepsilon _ { _ i } , \zeta _ { _ i }$ , and $\mathsf { S } _ { i } .$ .

Table 2 depicts the results. We focus on the main variables of interest in Table $2 ;$ we do not report the parameters of the time effects. Table 2 shows that offering the BNF has a strong, significant, and positive effect on the average number of bids and the number of bidders per auction. The effect of the BNF on the number of bidders shows that bidders value the BNF and prefer auctions that offer this feature. Furthermore, the parameters of Equation (22) show that the BNF significantly increases the profit per auction. Offering the BNF increases the profit per auction by <sup>€</sup>81.46 (column 4, Table 2), supporting Proposition 3b. The results from Equations (20) and (21) further support Proposition 1, which states that the BNF attracts more bidders (+10.97; column 3, Table 2), and Proposition 2, which states that the BNF increases the average number of bids per bidder (+4.55; column 2, Table 2).

Bidders are ultimately interested in obtaining an attractive deal when they participate in pay-per-bid auctions. However, with respect to Proposition 3a, we find that offering the BNF results in a significant price increase of <sup>€</sup>0.79 (+10.97 bidder times +4.55 additional bids per bidder multiplied by 1.58 cents, that is, the weighted average increment in price).

Table 2. Impact of Buy-Now Feature on Average Number of Bids, Number of Bidders, and Profit per Auction in Product (Private Value) and Voucher (Common Value) Auctions

<table><tr><td>All categories</td><td>Average number of bids $(ab_i)$ </td><td>Number of bidders $(nb_i)$ </td><td>Profit per auction $(\pi_i)$ </td></tr><tr><td>Intercept</td><td>-11.991***(1.180)</td><td>-163.723***(13.267)</td><td>-855.116***(108.347)</td></tr><tr><td>Buy-Now offered (= 1, binary)</td><td>4.553***(0.377)</td><td>10.973***(4.232)</td><td>81.457**(34.561)</td></tr><tr><td>In Current retail price</td><td>3.736***(0.135)</td><td>50.439***(1.517)</td><td>229.767***(12.386)</td></tr><tr><td>Category: Audio (= 1, binary) $^a$ </td><td>0.402(0.529)</td><td>-34.997***(5.945)</td><td>-151.691***(48.548)</td></tr><tr><td>Category: Cell phones (= 1, binary)</td><td>0.353(0.472)</td><td>42.655***(5.305)</td><td>352.651***(43.325)</td></tr><tr><td>Category: Video (= 1, binary)</td><td>0.539(0.493)</td><td>-8.165(5.538)</td><td>-37.900(45.225)</td></tr><tr><td>Category: Navigation (= 1, binary)</td><td>1.035(0.666)</td><td>-47.849***(7.486)</td><td>-268.910***(61.132)</td></tr><tr><td>Category: Video games (= 1, binary)</td><td>0.874*(0.454)</td><td>-22.544***(5.108)</td><td>-81.847**(41.715)</td></tr><tr><td>Category: Camcorders (= 1, binary)</td><td>1.121**(0.529)</td><td>-45.04***(5.941)</td><td>-206.361***(48.517)</td></tr><tr><td>Category: Computers (= 1, binary)</td><td>0.300(0.536)</td><td>-37.851***(6.020)</td><td>-189.209***(49.159)</td></tr><tr><td>Category: Home and garden (= 1, binary)</td><td>0.465(0.515)</td><td>-51.064***(5.784)</td><td>-247.698***(47.234)</td></tr><tr><td>Category: Fun (= 1, binary)</td><td>0.052(0.716)</td><td>-29.986***(8.045)</td><td>-121.612*(65.698)</td></tr><tr><td>Category: Lifestyle (= 1, binary)</td><td>1.763***(0.525)</td><td>-48.201***(5.898)</td><td>-225.929***(48.166)</td></tr><tr><td>Category: Voucher (= 1, binary)</td><td>6.077***(0.553)</td><td>26.474***(6.217)</td><td>165.009***(50.772)</td></tr><tr><td>Increment: 2 cents (= 1, binary) $^b$ </td><td>0.473(0.288)</td><td>5.643*(3.241)</td><td>31.361(26.464)</td></tr><tr><td>Increment: 5 cents (= 1, binary)</td><td>0.443(0.412)</td><td>18.617***(4.628)</td><td>127.359***(37.796)</td></tr><tr><td>Weekdays (binary)</td><td>Yes $^c$ </td><td>Yes</td><td>Yes</td></tr><tr><td>Month (binary)</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Daytime (Hours) (binary)</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Start of month (Pay Day) (binary)</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $R^2$ (adj. $R^2$ )</td><td>0.233(0.227)</td><td>0.414(0.409)</td><td>0.207(0.201)</td></tr><tr><td>F-value (p-value)</td><td>37.99(p&lt;0.01)</td><td>88.25(p&lt;0.01)</td><td>32.64(p&lt;0.01)</td></tr></table>

Notes: N = 6,812. <sup>a</sup> Reference category = Notebook. <sup>b</sup> Reference category = 1-cent increment. <sup>c</sup> Yes indicates that our model controls for these variables. Standard errors are in parentheses. $^ { * } p < 0 . 1 ;$ \*\* p < 0.05; \*\*\* p < 0.01.

In Proposition 4, we argue that voucher auctions are different from product auctions. To compare these two auction types, we separately estimate Equations (20)–(22) for voucher and product auctions. In comparing the results of product auctions (Table 3) with those of voucher auctions (Table 4), we find that the BNF increases the average number of bids in voucher auctions by more than twice the increase for product auctions. This finding provides support for Proposition 4a and confirms the finding of Lam [15]. Furthermore, we find that the BNF discourages bidders from participating in voucher auctions (–17.44 bidders), which is in strong contrast to the results for the product auctions, in which we find that the BNF attracts +14.19 additional bidders. Proposition 4b is therefore not supported.

With respect to profit per auction, we observe a negative effect of the BNF for voucher auctions, supporting Proposition 4d. In voucher auctions, the profit per auction decreases by an average of –<sup>€</sup>94.00 when the BNF is offered. The negative impact on profit is explained by bidders who use a high sum of bidding fees to cash in the BNF (see Equation (9)) and a rather suboptimal use of the BNF in the product auctions. Furthermore, this finding indicates the high level of risk faced by the auctioneer when offering voucher auctions with a BNF because bidders use it frequently (see Table 1).

We conduct a matching analysis to test for potential endogeneity problems that might occur through a systematic scheduling of auctions with BNFs on particular days of the week or times of day and the selection of products in auctions with BNF. We employ a direct matching approach for the matching analysis, in which we match the auctions for vouchers and products separately as we do for the regression analyses. For the matching, we use the BNF (offered: yes versus no) as a treatment variable and use the product ID, the increments, the days of the week, and the starting hour of each auction categorized in three groups (morning [1:00 a.m .–8:00 a.m .], afternoon [9:00 a.m .–4:00 p.m .], and night [5:00 p.m .–12 p.m .]) as the independent variables. The matching analysis confirms our findings from the regression analyses, as it outlines significantly $( p < 0 . 0 1 )$ ) lower mean profits for voucher auctions with a BNF and a significantly larger mean profit for product auctions with a BNF.

To test Proposition 4c, we run an additional regression analysis that includes only auctions with a BNF. We use the final price (in euros) of the auctions as the dependent variable and a binary variable for the voucher category and the logarithm (ln) of the CRP as independent variables. We find a positive difference $( p < 0 . 0 1 )$ ) between the average final prices in the voucher auctions and in the product auctions with a BNF. This result supports Proposition 4c, which states that the BNF results in final prices that are higher in voucher auctions than in product auctions.

In Proposition 5, we expect the BNF to have a positive effect on profits as product margins increase. We test this proposition through a regression analysis. We use the profit per auction as the dependent variable and the product margin relative to the CRP, the logarithm of the CRP, a binary variable for the BNF, a binary variable indicating voucher auctions, and an interaction term for the BNF and the product margin as independent variables. We find a positive interaction effect $( p < 0 . 0 1 )$ for the BNF and the margin, which supports Proposition 5. Thus, the BNF has an increasingly positive effect on profits as product margins increase. This finding implies that auctioneers should offer products with high margins in auctions with a BNF.

Table 3. Impact of Buy-Now Feature on Average Number of Bids, Number of Bidders, and Profit in Product (Common Value) Auctions

<table><tr><td>Product auctions</td><td>Average number of bids (ab_i)</td><td>Number of bidders (nb_i)</td><td>Profit per auction (π_i)</td></tr><tr><td>Intercept</td><td>-10.225***</td><td>-208.14***</td><td>-1,045.51***</td></tr><tr><td></td><td>(1.319)</td><td>(15.473)</td><td>(128.538)</td></tr><tr><td>Buy-Now offered (= 1, binary)</td><td>4.128***</td><td>14.186**</td><td>119.974**</td></tr><tr><td></td><td>(0.583)</td><td>(6.843)</td><td>(56.85)</td></tr><tr><td>In Current retail price</td><td>3.532***</td><td>56.965***</td><td>255.442***</td></tr><tr><td></td><td>(0.154)</td><td>(1.801)</td><td>(14.96)</td></tr><tr><td>Category: Audio (= 1, binary)a</td><td>0.262</td><td>-26.697***</td><td>-121.881**</td></tr><tr><td></td><td>(0.557)</td><td>(6.528)</td><td>(54.232)</td></tr><tr><td>Category: Cell phones (= 1, binary)</td><td>0.483</td><td>42.568***</td><td>351.048***</td></tr><tr><td></td><td>(0.488)</td><td>(5.726)</td><td>(47.570)</td></tr><tr><td>Category: Video (= 1, binary)</td><td>0.429</td><td>-0.132</td><td>-8.969</td></tr><tr><td></td><td>(0.516)</td><td>(6.047)</td><td>(50.232)</td></tr><tr><td>Category: Navigation (= 1, binary)</td><td>1.055</td><td>-41.305***</td><td>-245.993***</td></tr><tr><td></td><td>(0.691)</td><td>(8.106)</td><td>(67.340)</td></tr><tr><td>Category: Video games (= 1, binary)</td><td>0.814*</td><td>-14.930***</td><td>-57.329</td></tr><tr><td></td><td>(0.477)</td><td>(5.595)</td><td>(46.475)</td></tr><tr><td>Category: Camcorders (= 1, binary)</td><td>1.152**</td><td>-40.836***</td><td>-189.860***</td></tr><tr><td></td><td>(0.548)</td><td>(6.430)</td><td>(53.419)</td></tr><tr><td>Category: Computers (= 1, binary)</td><td>0.230</td><td>-31.105***</td><td>-171.281***</td></tr><tr><td></td><td>(0.561)</td><td>(6.577)</td><td>(54.639)</td></tr><tr><td>Category: Home and garden (= 1, binary)</td><td>0.517</td><td>-45.213***</td><td>-236.649***</td></tr><tr><td></td><td>(0.540)</td><td>(6.340)</td><td>(52.665)</td></tr><tr><td>Category: Fun (= 1, binary)</td><td>-0.077</td><td>-22.058**</td><td>-95.250</td></tr><tr><td></td><td>(0.745)</td><td>(8.740)</td><td>(72.604)</td></tr><tr><td>Category: Lifestyle (= 1, binary)</td><td>1.832***</td><td>-42.537***</td><td>-211.854***</td></tr><tr><td></td><td>(0.550)</td><td>(6.455)</td><td>(53.622)</td></tr><tr><td>Increment: 2 cents (= 1, binary)b</td><td>-0.015</td><td>13.572***</td><td>80.121**</td></tr><tr><td></td><td>(0.335)</td><td>(3.926)</td><td>(32.617)</td></tr><tr><td>Increment: 5 cents (= 1, binary)</td><td>0.209</td><td>28.599***</td><td>170.022***</td></tr><tr><td></td><td>(0.457)</td><td>(5.357)</td><td>(44.505)</td></tr><tr><td>Weekdays (binary)</td><td>Yesc</td><td>Yes</td><td>Yes</td></tr><tr><td>Month (binary)</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Daytime (Hours) (binary)</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Start of month (Pay Day) (binary)</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>R2(adj. R2)</td><td>0.219</td><td>0.431</td><td>0.212</td></tr><tr><td></td><td>(0.212)</td><td>(0.425)</td><td>(0.204)</td></tr><tr><td>F-value (p-value)</td><td>29.08</td><td>78.25</td><td>27.83</td></tr><tr><td></td><td>(p&lt;0.01)</td><td>(p&lt;0.01)</td><td>(p&lt;0.01)</td></tr></table>

Notes: N = 5,540. <sup>a</sup> Reference category = Notebook. <sup>b</sup> Reference category = 1-cent increment. <sup>c</sup> Yes indicates that our model controls for these variables. Standard errors are in parentheses. $^ { * } p < 0 . 1 ;$ \*\* $p < 0 . 0 5 ; ^ { \ast \ast \ast } p < 0 . 0 1 .$

Table 4. Impact of Buy-Now Feature on Average Number of Bids, Number of Bidders, and Profit in (Private Value) Voucher Auctions

<table><tr><td>Voucher auctions</td><td>Average number of bids (ab $_i$ )</td><td>Number of bidders (nb $_i$ )</td><td>Profit per auction ( $\pi_i$ )</td></tr><tr><td>Intercept</td><td>-10.256***(3.669)</td><td>-0.865(23.612)</td><td>-192.370(149.095)</td></tr><tr><td>Buy-Now offered (= 1, binary)</td><td>8.252***(0.712)</td><td>-17.443***(4.583)</td><td>-93.999***(28.938)</td></tr><tr><td>In Current retail price</td><td>4.826***(0.334)</td><td>11.312***(2.149)</td><td>86.409***(13.573)</td></tr><tr><td>Increment: 2 cents (= 1, binary) $^a$ </td><td>0.255(0.672)</td><td>-3.525(4.327)</td><td>-45.101*(27.322)</td></tr><tr><td>Increment: 5 cents (= 1, binary)</td><td>1.279(1.450)</td><td>-13.283(9.334)</td><td>-51.499(58.937)</td></tr><tr><td>Weekdays (binary)</td><td>Yes $^b$ </td><td>Yes</td><td>Yes</td></tr><tr><td>Month (binary)</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Daytime (Hours) (binary)</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Start of month (Pay Day) (binary)</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>R $^2$ (adj. R $^2$ )</td><td>0.366(0.345)</td><td>0.239(0.213)</td><td>0.185(0.158)</td></tr><tr><td>F-value (p-value)</td><td>17.32(p&lt;0.01)</td><td>9.40(p&lt;0.01)</td><td>6.83(p&lt;0.01)</td></tr></table>

Notes: N = 1,272. <sup>a</sup> Reference category = 1-cent increment. <sup>b</sup> Yes indicates that our model controls for these variables. Standard errors are in parentheses. \* p < 0.1; \*\* p < 0.05; \*\*\* $p < 0 . 0 1$

## Bidding Behavior

The main advantage of the BNF for bidders is that they can use it to avoid extreme losses; in other words, they can use their bids to buy the product at the BNP. We test this claim by comparing the behavior of losing bidders in auctions with and without a BNF. We compare the top 1 percent of losers in auctions with and without a BNF. We find that the top 1 percent of losers in auctions without the BNF lose, on average, –<sup>€</sup>126.81 per auction, whereas the top 1 percent of losers in auctions with the BNF lose significantly $( p < 0 . 0 1 )$ less: on average, –<sup>€</sup>106.82.

To gain some initial insight into BNF usage, we compare the sum of bidding fees relative to the BNP for the BNF users (Figure 1). The large spike at 100 percent corresponds to bidders who cashed in their sum of bidding fees when the value of their placed bids equaled the BNP. However, the ratio of the sum of bidding fees to the

![](/api/attachments/Z6R68WC4/fulltext/images/753d81ec05cd62caaf14f95e013a2fad1e1c8da06d70a5ced4aafd033c246d10.jpg)  
Sum of Bidding Fees as Percentage of Buy-Now Price  
Figure 1. Distribution of Sum of Bidding Fees per Auction Across Users of Buy-Now Feature  
Note: Mean = 62.47 percent; Minimum = 0.05 percent; Maximum = 179.00 percent.

BNP is much less than 100 percent for a large number of BNF usages (62.47 percent of the BNP on average). Thus, the majority of bidders did not bid until their sum of bidding fees equaled the BNP and missed the opportunity to win the auction. However, Figure 1 also shows 72 bidders who indicate that they place more bids than the risk-free strategy recommends; these bidders clearly missed the upper threshold to stop bidding. Thus, not all bidders are using the BNF optimally.

Figure 2 displays the likelihood that a bidder will use the BNF given his sum of bidding fees relative to the BNP of the auctioned item. Figure 2 clearly indicates that the number of bidders who do not use the BNF substantially decreases with an increasing number of bids. We confirm this observation through a logistic regression that shows a positive and significant $( p < 0 . 0 1 )$ relationship between the sum of bidding fees relative to the BNP and BNF usage (yes versus no). We therefore provide support for Proposition 6.

To summarize, we find that few bidders who use the BNF follow the proposed risk-free bidding strategy. For a more detailed description of bidder heterogeneity, we followed the approach of Bapna et al. [2], who clustered bidders with respect to their bidding characteristics (average number of bids per auction, auction entry and exit). We find that the cluster of bidders that places the most bids also exhibits the highest likelihood of using the BNF, which is in line with the pattern displayed in Figure 2.

Figure 1 already indicates that bidders do not take full advantage of the risk-free bidding strategy. An interesting question, which we address in Proposition 8, is whether bidders actually learn to use the BNF, that is, learn to apply the risk-free bidding strategy. To answer this question, we utilize two different approaches. In the vein of Spann and Tellis [25], we investigate whether bidding behavior exhibits a typical learning pattern. For the BNF, a typical learning behavior would show that the bidder minimizes the absolute deviation between the optimal number of bids (i.e., the upper threshold $( B N P _ { _ i } - p _ { _ i , r } / ( b _ { _ i } \cdot \mathbf { \alpha } \alpha _ { _ i } ) )$ and the number of bids placed when using the BNF over time. We use the absolute deviation because our data show that bidders occasionally overbid in the presence of a BNF (i.e., their sum of bidding fees exceeds the BNP), which also represents a deviation from the optimal number of bids. If learning exists, then we will find a decrease in the bidder’s absolute deviation from the optimal number of bids.

![](/api/attachments/Z6R68WC4/fulltext/images/59be1eb112128c0d40e77645388da4cdd1fb3a066f4589cc64e493e8d80af93a.jpg)  
Sum of Bidding Fees as Percentage of the Buy-Now Price  
Figure 2. Likelihood of Buy-Now Feature Usage as a Function of the Sum of Bidding Fees

We analyze whether the empirically observed BNF usage sequences match the assumed learning pattern by estimating each bidder’s BNF usage patterns. We consider the bidders who have used the BNF at least six times. This selection assures the robustness of the regression, which includes two parameters, and that we have sufficient observations to identify the learning process, which is assumed to occur rather slowly [1]. To capture the bidding pattern, we fit the following linear regressions to each bidder’s BNF usage sequence:

$$
\left| d e v i a t i o n _ {j, k} \right| = \omega_ {0, k} + \omega_ {1, k} \cdot \frac {1}{\ln \left(n s e q _ {j , k} ^ {B N F} + 1\right)} + \xi_ {j, k} \quad (j \in J, k \in K).\tag{23}
$$

where |deviation $\mathbf { \Phi } _ { j , k } |$ is the absolute deviation from the optimal number of bids (i.e., the upper threshold) of bidder j and BNF usage $k ; n s e q _ { j , k } ^ { B N F }$ is the cumulative number of

BNFs used by bidder j when using the BNF for the kth time (e.g., two for the second time the BNF is used); ${ \mathfrak { O } } _ { 0 , k }$ and ${ \mathfrak { O } } _ { 1 , k }$ are the parameters that capture the inverse logarithmic shape of Equation (23); and $\xi _ { \boldsymbol { k } , j }$ is the error term. We conclude that a learning pattern exists when ${ \bf \omega } _ { \omega _ { 1 , k } } > 0$ at the 5 percent level; that is, when the absolute deviation from the optimal BNF usage significantly decreases with the cumulative experience of BNF usage. We conclude that bidders who do not exhibit this type of learning pattern do not learn over time (either because they already use the BNF optimally and cannot improve or because they do not learn with experience). We find that, out of the 303 analyzed bidders who used the BNF more than six times within the observation period, only 45 bidders (14.85 percent) can be characterized by the learning pattern and thus exhibit learning behavior.

This analysis shows that a relatively small group of bidders learns to better use the BNF over time. However, the analysis is unable to explain the deviation from the upper threshold. We therefore conduct a second analysis that aims to explain the deviation from the upper threshold. We conduct an exponential regression analysis that is pooled over all BNF usages. As the dependent variable, we use the absolute deviation of bids compared to the optimal number of bids (i.e., the upper threshold $( B N P _ { _ i } { - } p _ { _ i , r } / ( b _ { _ i } { \cdot } \alpha _ { _ i } ) ) )$ each time a bidder uses the BNF. As an independent variable, we use the logarithm of the cumulative number of auctions in which each bidder participates as a measure of experience (e.g., [29]). We also include the logarithm of the cumulative number of BNF usages to control for BNF experience and the logarithm of the cumulative number of auctions won. Both variables are comparable to experience and success measures. Furthermore, we include the logarithm of the average active time per bid, which represents the ratio of the placed bids and the time a bidder was active in the auction (i.e., monitored the auction). We define active time as the time span between the bidder’s first and last bid. The purpose of this variable is to control for the monitoring costs a bidder faces when participating in the auction. These monitoring costs might explain deviations from the optimal number of bids. We further control for product categories, the number of bidders in the auction, the logarithm of the CRP, and the number of BNF users in the auction.<sup>1</sup>

Table 5 presents the results of the exponential regression and shows that the deviation significantly decreases with greater BNF experience and with a higher number of previously won auctions. The significant effect of BNF usage confirms our finding that some bidders learn to use the BNF. The significant effect of the auctions won might relate to the fact that a bidder who wins auctions is more involved in the auction mechanisms. However, we find a positive effect of experience in pay-per-bid auctions. We further find that the CRP has a positive effect on the deviation. The reason for this result might be that it takes a greater effort to bid up to the upper threshold when the product has a high value. We also find that, in auctions where the BNF is used many times, the deviation from optimal usage decreases. Here, the reason might be that, if several bidders bid more aggressively (see Tables 3–4) against one another, the bidders push each other faster in the direction of the upper threshold. We observe a decrease in the deviation when a higher number of bidders participate in the auctions. Finally, we find that a higher average active time per bid is positively related to a greater deviation from optimal bidding behavior. This result may indicate that bidders account for the opportunity costs arising from monitoring or participating in pay-per-bid auctions.

Table 5. Determinants of Deviation from Optimal Bidding Behavior

<table><tr><td rowspan="2"></td><td colspan="2">Absolute deviation from upper threshold</td></tr><tr><td>Parameter</td><td>Standard error</td></tr><tr><td>Intercept</td><td>-1.624***</td><td>0.213</td></tr><tr><td>In Number of auctions participated</td><td>0.031***</td><td>0.007</td></tr><tr><td>In Number of auctions won</td><td>-0.051***</td><td>0.005</td></tr><tr><td>In Number of BNFs used</td><td>-0.070***</td><td>0.005</td></tr><tr><td>Total number of BNFs used in auctions</td><td>-0.029***</td><td>0.004</td></tr><tr><td>Total number of bidders in auction</td><td>-0.001***</td><td>0.000</td></tr><tr><td>In Current retail price</td><td>1.067***</td><td>0.035</td></tr><tr><td>In Average active time per bid</td><td>0.065***</td><td>0.011</td></tr><tr><td>Category: Audio (= 1, binary)a</td><td>-0.148</td><td>0.125</td></tr><tr><td>Category: Cell phones (= 1, binary)</td><td>-0.018</td><td>0.110</td></tr><tr><td>Category: Video (= 1, binary)</td><td>-0.077</td><td>0.125</td></tr><tr><td>Category: Navigation (= 1, binary)</td><td>-0.184</td><td>0.147</td></tr><tr><td>Category: Video games (= 1, binary)</td><td>-0.136</td><td>0.106</td></tr><tr><td>Category: Camcorders (= 1, binary)</td><td>-0.216</td><td>0.133</td></tr><tr><td>Category: Computers (= 1, binary)</td><td>-0.223</td><td>0.140</td></tr><tr><td>Category: Home and Garden (= 1, binary)</td><td>0.024</td><td>0.134</td></tr><tr><td>Category: Fun (= 1, binary)</td><td>0.149</td><td>0.232</td></tr><tr><td>Category: Lifestyle (= 1, binary)</td><td>-0.302**</td><td>0.136</td></tr><tr><td>Category: Voucher (= 1, binary)</td><td>0.056</td><td>0.124</td></tr><tr><td>Increment: 2 cents (= 1, binary)b</td><td>-0.081</td><td>0.071</td></tr><tr><td>Increment: 5 cents (= 1, binary)</td><td>-0.088</td><td>0.133</td></tr><tr><td>R2 (adj. R2)</td><td>0.435(0.433)</td><td></td></tr><tr><td>F-value (p-value)</td><td>252.7(p &lt; 0.01)</td><td></td></tr></table>

Notes: N = 6,592. <sup>a</sup> Reference category = Notebook. <sup>b</sup> Reference category = 1-cent increment. \* p < 0.1; \*\* p < 0.05; \*\*\* p < 0.01.

The result from our first bidder-learning analysis partially provides support for Proposition 8, as we find that 14.85 percent of the investigated bidders learn to use the BNF better over time. The second analysis shows that bidders who have won auctions and used the BNF present a lower deviation. We further find that experience (i.e., the number of auctions participated in) does not decrease the absolute deviation. Thus, experience itself does not seem to provide a learning effect. However, the results indicate a learning effect for the usage of the BNF. One reason for this result might be the pronounced feedback from the auctioneer when using the BNF. When using the BNF, the auctioneer communicates to the bidder the actual amount he or she has to pay (on top), which might increase the awareness of the option value.

We additionally analyze whether sophisticated bidders may avoid auctions with BNFs, which could explain the low number of bidders that learn. We operationalize sophisticated bidders as the top 500 bidders who realized the highest consumer surplus across all auctions and participated in at least 10 auctions. We find that the sophisticated bidders prefer auctions with a BNF $( p < 0 . 0 1 )$ compared to the remaining bidders.

We next investigate whether the BNF increases the loyalty of bidders (Proposition 9). To assess the loyalty of bidders in pay-per-bid auctions, we classify bidders into four distinct groups. These four groups are determined by whether a bidder has won at least one auction (yes versus no) and whether he or she has used the BNF at least once (yes versus no). The first group, the “Winner only” group, includes bidders who have won at least one auction but have never used the BNF. The second group, the “Winner and Buy-Now” group, includes the bidders who have won at least one auction and have used the BNF at least once. The third group, the “Loser” group, consists of the bidders who have never won an auction and have never used the BNF. The fourth group, the “BNF only” group, contains bidders who have used the BNF (at least once) but have never won an auction.

According to Proposition 9, we expect BNF usage to have a positive impact on bidder loyalty, making it higher than the loyalty of bidders who do not use this feature (Proposi tion 9a). However, because winning the auction is usually more attractive than purchasing a product with the BNF, we expect to find high loyalty among the bidders who actually win auctions (Proposition 9b). We propose that the highest loyalty can be observed among the bidders who have won auctions and used the BNF (Proposition 9c).

To quantify the effect of the BNF on loyalty, we estimate a Cox regression model. We use all bidders who participated in their first auction during weeks 1–30 of our data set. Thus, we have no left censoring in our data. We then define the eight weeks after the first auction as the observation period for each bidder. In the next step, we right censor all of the bidders who showed an active lifetime greater than 56 days (i.e., eight weeks). To estimate the model, we then use the number of days that a bidder was active as the dependent variable and control for being a member of one of the four groups (the loser group is the reference category).

The results (Table 6) show that all of the groups have a lower churn rate than the reference group (“Loser”) and that the loyalty of the three groups is significantly different. The “BNF only” group exhibits a 35.6 percent higher probability of expanding their active lifetime by an additional day than does the reference group. This finding provides support for Proposition 9a. The “Winner only” group has a 60.2 percent higher probability of remaining active than the “Loser” group and a higher probability of remaining active than the “BNF only” group. Thus, Proposition 9b is supported. Finally, the “Winner and Buy-Now” group exhibits the highest probability (71.3 percent) of remaining active, providing support for Proposition 9c. Thus, our results clearly demonstrate the positive effect of the BNF on loyalty. This analysis underscores the high churn rate that the providers of pay-per-bid auctions typically face (compare [30]) and the relevance of new, loyalty increasing features.

<sub>of</sub> <sub>Cox</sub> <sub>Regression</sub> M<sup>odel</sup> <sup>with</sup> <sup>Impact</sup> <sup>of</sup> <sup>Bidder</sup> <sup>Characteri</sup>

<table><tr><td rowspan="2"></td><td rowspan="2">Parameter(standard error)</td><td rowspan="2">Exp(parameter)</td><td colspan="2">Confidence interval</td><td rowspan="2">Increase in probability ofremaining active the next day</td></tr><tr><td>Lower 0.95</td><td>Upper 0.95</td></tr><tr><td>BNF only</td><td>-0.440***(0.027)</td><td>0.644</td><td>0.611</td><td>0.679</td><td>35.6</td></tr><tr><td>Winner only</td><td>-0.920***(0.033)</td><td>0.398</td><td>0.373</td><td>0.425</td><td>60.2</td></tr><tr><td>Winner and Buy-Now</td><td>-1.247***(0.043)</td><td>0.287</td><td>0.264</td><td>0.313</td><td>71.3</td></tr><tr><td colspan="6">Notes: N = 71,862 observations; number of events = 64,129. Reference group is the “Loser” group. The “Loser” group includes bidders who have never used the BNF nor won an auction. * p &lt; 0.1; ** p &lt; 0.05; *** p &lt; 0.01.</td></tr></table>

## Summary and Conclusion

Bidders in pay-per -b id auctions ar e often tem pted by attractive deals but face the risk of extreme losses. Such losses often cause negative word of mouth on the Internet and high churn rates that place the long-term feasibility of this business model into question. In response to these negative effects, pay-per-bid auctioneers have introduced the BNF, which permits bidders to recuperate their losses by applying their bidding fees toward buying the auctioned item at the BNP, which is usually the CRP. In our paper, we theoretically and empirically investigate the effects that the BNF has on profit and bidding behavior.

Based on unique data for 6,812 pay-per-bid auctions that include information about actual costs, we find that the BNF leads to an increase in the average number of bids per bidder and causes higher final prices. Thus, bidders who do not use the BNF are worse off in auctions where this feature is offered and should avoid them. For bidders, our findings show that the BNF results in less attractive deals for winners and less extreme losses for losers. In line with our propositions, the results for product (private value) and voucher (common value) auctions differ. In product auctions, we find that the BNF leads to an increase in the number of bidders and the profit (+<sup>€</sup>120 per auction), whereas in voucher auctions, the BNF causes a decrease in the number of bidders and profit (–<sup>€</sup>94 per auction).

Thus, increased BNF usage can easily decrease the profit per auction. We further find that the BNF yields higher profits for products with higher margins. Overall, an auctioneer benefits from the fact that the BNF has a relatively low usage frequency, increases the number of bids placed, and partially attracts more bidders, which results in higher final prices. It seems that many bidders participate in auctions to obtain an attractive deal with only a few bids. The BNF fulfills its intended purpose, which is to help bidders avoid extreme losses. We show that the maximum losses of participants per auction in auctions without the BNF are significantly higher than those in auctions with the BNF. Our analysis of individual bidding records shows that the likelihood of a bidder using the BNF substantially increases with an increasing number of previously placed bids, and this effect is even greater in voucher auctions. We further investigate whether bidders learn to use the BNF over the course of their participation in payper-bid auctions. We find that only a few (14.85 percent) of the bidders present a BNF usage pattern that demonstrates learning. In a consecutive analysis, we explore the drivers of bidders’ absolute deviations from the optimal number of bids (i.e., the upper threshold). We find that bidders who have won auctions and used the BNF exhibit a lower deviation. We further find that experience does not decrease the absolute deviation. Thus, experience itself does not seem to provide a learning effect.

Because pay-per-bid auctions tend to suffer from high churn rates, the BNF could be a promising tool to limit churn. Using a Cox regression model, we demonstrate that the BNF substantially increases bidder loyalty. We argue that winning an auction is usually more attractive than buying an auction item via the BNF and therefore analyze different groups of participants. We find that the group of participants who lost in all auctions without using the BNF (“Loser” group) exhibits the highest churn rate and that the group of bidders who used the BNF (“BNF only”) increased their probability of remaining active for another day by 35.6 percent. As we proposed, winning auctions is even more effective and increases the probability of the “Winner only” group remaining active by 60.2 percent compared to the “Loser” group. We observe the highest loyalty for the “Winner and Buy-Now” group, who have won auctions and used the BNF (+71.3 percent). Thus, the BNF can positively influence churn rates.

An implication for pay-per-bid auctioneers is that the BNF could help to lower negative word of mouth about pay-per-bid auctions by reducing the likelihood of extreme losses for bidders. The BNF is useful because it increases loyalty among its users, attracts more bidders, and generates higher profits overall. However, these benefits result only from bidders’ nonoptimal use of the BNF, and the increased use of the risk-free bidding strategy (if $\alpha _ { _ i } = 1 0 0$ percent) could jeopardize the feature’s benefits. The use of the BNF for voucher auctions is not recommended because more bidders in these auctions use the BNF and therefore cause a decrease in profit.

For the bidder, the BNF provides a risk-free option to participate in auctions depending on his or her evaluation of the auctioned item. However, as soon as more than one bidder uses this strategy, the expected return decreases substantially. This low return may explain the relatively low usage of the BNF. We further find that some bidders learn to use the BNF more effectively and that the learning is driven by successful auction participation (i.e., either winning an auction or using the BNF).

Acknowledgments: The authors thank the two anonymous reviewers and guest editor Ravi Bapna for providing very valuable comments on earlier drafts of this paper.

## Note

1. For robustness, we also conducted this analysis with additional control variables, namely, the day of the week and the start time of the auction. However, the inclusion of these variables did not change the overall result.

## Refer ences

1. Augenblick, N. Consumer and producer behavior in the market for penny auctions: A theoretical and empirical analysis. University of California, Berkeley, April 2012.

2. Bapna, R.; Goes, P.; and Gupta, A. User heterogeneity and its impact on electronic auction market design: An empirical exploration. MIS Quarterly, 25, 4 (2004), 21–43.

3. Bapna, R.; Jank, W.; and Shmueli, G. Consumer surplus in online auctions. Information Systems Research, 19, 4 (2008), 400–416.

4. Baye, M.; Kovenock, D.; and de Vries, C. The all-pay auction with complete information. Economic Theory, 8, 2 (1996), 291–305.

5. Budish, E.B., and Takeyama, L.N. Buy prices in online auctions: Irrationality on the Internet? Economic Letters, 72, 3 (2001), 325–333.

6. Bulow, J., and Klemperer, P. The generalized war of attrition. American Economic Review, 89, 1 (1999), 175–189.

7. Byres, J.W.; Mitzenmacher, M.; and Zervas, G. Information asymmetries in pay-per-bid auctions: How Swoopo makes bank. Cornell University, Ithaca, NY, January 5, 2010 (available at http://arxiv.org/abs/1001.0592/).

8. Caldara, M. Bidding behavior in pay-to-bid auctions: An experimental study. University of California, Irvine, March 26, 2012 (available at www.chapman.edu/research-and-institutions/ economic-science-institute/\_files/BrownBag/michaelcaldera2012.pdf).

9. Dasgupta, P. The theory of technological competition. In J.E. Stiglitz and G.F. Mathewson (eds.), New Developments in the Analysis of Market Structure. London: Macmillan, 1986, pp. 519–547.

10. Easley, R.F.; Wood, C.A.; and Sharad, B. Bidding patterns, experience, and avoiding the winner’s curse in online auctions. Journal of Management Information Systems, 27, 3 (Winter 2010–11), 241–268.

11. Hidvégi, Z.; Wang, W.; and Whinston, A.B. Buy-price English auction. Journal of Economic Theory, 129, 1 (2006), 31–56.

12. Hinnosaar, T. Penny auctions are unpredictable. Northwestern University, Evanston, IL, 2010.

13. Kim, J.Y.; Brünner, T.; Skiera, B.; and Natter, M. An analysis of pay-per-bid auctions. International Journal of Research in Marketing, 31, 4 (2014), forthcoming.

14. Krishna, V. Auction Theory, 2d ed. Amsterdam: Elsevier, 2010.

15. Lam, T. Pay-per-bid auctions with an exit option: An experimental and empirical investigation. Working paper, University of New South Wales, 2011.

16. Mathews, T. The impact of discounting on an auction with a buyout option: A theoretical analysis motivated by eBay’s buy-it-now feature. Journal of Economics, 81, 1 (2004), 25–52.

17. Mittal, S. Equilibrium analysis of generalized penny auctions. Harvard University, Cambridge, 2010.

18. Noussair, C., and Silver, J. Behavior in all-pay auctions with incomplete information. Games and Economic Behavior, 55, 1 (2006), 147–206.

19. Platt, B.C.; Price, J.; and Tappen, H. The role of risk preferences in pay-to-bid auctions. Management Science, 59, 9 (2013), 2117–2134.

20. Popkowski Leszczyc, P.T.L.; Qiu, C.; and He, Y. Empirical testing of the reference-price effect of buy-now prices in Internet auctions. Journal of Retailing, 85, 2 (2009), 211–221.

21. Reiner, J.; Natter, M.; and Skiera, B. Exciting commerce. In J.E. Wieringa, P.C. Verhoef,

and J.C. H oekstra (eds.), Liber Amicorum in Honor of Peter S.H. Leeflang. Groningen, 2011, pp. 339–349.

22. Reiner, J.; Brünner, T.; Natter, M.; and Skiera, B. Using cumulative prospect theory to explain why bidders participate in pay-per-bid auctions. Working paper, Goethe University Frankfurt, 2013.

23. Schram, A.J.H.C., and Onderstal, S. Bidding to give: An experimental compression of auctions for charity. International Economic Review, 50, 2 (2009), 431–457.

24. Shubik M. Dollar auction game—Paradox in noncooperative behavior and escalation. Journal of Conflict Resolution, 15, 1 (1971), 109–111.

25. Spann, M., and Tellis, G. J. Does the Internet promote better consumer decision? The case of name-your-own-price auctions. Journal of Marketing, 70, 1 (2006), 65–78.

26. Standifird, S.S.; Roelofs, M.R.; and Durham, Y. The impact of eBay’s buy-it-now function on bidder behavior. International Journal of Electronic Commerce, 9, 2 (2004), 167–176.

27. Stix, E. An empirical study of online penny auctions. Brown University, Providence, RI, May 3, 2012 (available at www.cs.brown.edu/research/pubs/theses/ugrad/2012/estix.pdf).

28. Thaler, R.H. Paying a price for the thrill of the hunt. New York Times, November 14, 2009 (available at www.nytimes.com/2009/11/15/business/economy/15view.html).

29. Wang, X., and Hu, Y. The effect of experience on Internet auction bidding dynamics. Marketing Letters, 20, 3 (2009), 245–261.

30. Wang, Z., and Xu, M. Learning and strategic sophistication in games: Evidence from penny auctions on the Internet. Northeastern University, Boston, February 2012 (available at www.economics.neu.edu/zwang/Penny%20auction.02.2012.pdf).

---
otero_id: 21721
otero_key: "6X6R3NFU"
title: "Multiple-issue auction and market algorithms for the world wide web"
authors: "Jeffrey Teich; Hannele Wallenius; Jyrki Wallenius"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00016-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Multiple-issue auction and market algorithms for the world wide web

Jeffrey Teich <sup>a,)</sup>, Hannele Wallenius <sup>b,1</sup>, Jyrki Wallenius <sup>c,2</sup>

<sup>a</sup> Department of Management, New Mexico State UniÕersity, Las Cruces, NM 88003, USA 8 <sup>b</sup> Department of Industrial Engineering and Management, Helsinki UniÕersity of Technology, 02150 Espoo, Finland c International Center, Helsinki School of Economics, POB 1210, 00101 Helsinki, Finland

Accepted 11 February 1999

## Abstract

The Internet is quickly changing the way business-to-consumer and business-to-business commerce is conducted in the world. The Electronic Revolution has also spawned a trend of price wars and, in some instances, chaos, because of the zero-sum nature of the electronic channel. The technology has created an opportunity to get beyond the lose–lose nature of single issue price wars by determining sellers’ and buyers’ preferences across multiple issues and encouraging negotiations, thereby creating possible joint gains for all parties. We develop simple multiple-issue algorithms and heuristics that could be used in electronic auctions and electronic markets, to match businesses to businesses and consumers based on dovetailing underlying interests and preferences. We provide arguments that such dovetailed matches should help stabilize markets and make them more efficient. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Auctions; Electronic markets; Decision support; Negotiation modeling; World wide web; Intelligent agents

## 1. Introduction

In order to put our study into perspective, we present a market framework adapted from the work of Guttman and Maes 20 Fig. 1 . The market<sup>w</sup> <sup>x</sup> Ž . framework consists of one or many buyers and one or many sellers. One buyer and one seller, assuming the current tendency towards non-fixed prices, defines a traditional negotiation. The negotiation may take place face-to-face or electronically. One seller and many buyers defines an auction which may be live or on-line. Many sellers and one buyer defines a reverse auction, an example being a government auction. Many sellers and many buyers defines a market or a double auction, which may be live or electronic. Live and electronic versions of stock exchanges exist. Guttman and Maes 20 also differ-<sup>w</sup> <sup>x</sup> entiate between traditional classified ad markets and traditional stock markets, the difference being that in traditional stock markets, there is a centralized multilateral exchange compared to classified ad markets, where trading is ad hoc and bilateral. Centralized multilateral exchange markets may become classified ad markets and vice versa due to revolutionary changes made possible through the Internet and the expansion of the world wide web for electronic commerce. An example of a previously classified ad market, which is becoming an exchange market, is the US home mortgage market. Traditional retail markets may offer an opposite example. Such markets are becoming more one-to-one, exhibiting features similar to classified ad markets e.g., Egghead Ž and Dell Computer . Some traditional markets and. auctions offer the possibility of trading both electronically or live. Even the traditional large stock exchanges are moving in the direction of partially electronic markets.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">BUYERS</td></tr><tr><td>ONE</td><td>MANY</td></tr><tr><td rowspan="2">SELLERS</td><td>ONE</td><td>NEGOTIATION</td><td>AUCTION</td></tr><tr><td>MANY</td><td>REVERSE AUCTION</td><td>MARKETS</td></tr></table>

Fig. 1. Market framework.

Most existing live and electronic auctions and markets mainly focus on a single issue, namely price of the merchandise or stock 20 . There exists exten-<sup>w</sup> <sup>x</sup> sive literature demonstrating the detrimental effects of single issue, distributive zero-sum negotiations.Ž . Price wars are a concrete example, leading to a volatile market 1,8,21,25 . Exclusive focus on price<sup>w</sup> <sup>x</sup> will also do a disservice to buyers and sellers alike by hiding important value attributes from consideration. Following Guttman and Maes 19 , an explicit consideration of such multiple value attributes holds the promise of converting distributive negotiations into integrative negotiations. See also the work of Kersten and Szpakowicz 27 .<sup>w</sup> <sup>x</sup>

In this paper, we develop simple, heuristic algorithms for multiple-issue electronic markets and auctions, to match businesses with businesses and consumers based on dovetailing buyers’ and sellers underlying interests and preferences. We argue that such dovetailed matches should help stabilize markets and make them more efficient. To the best of our knowledge, there is very little literature on multiple-issue markets and auctions whether electronic or live. See, for example, the works of Bodendorf et al. <sup>w x</sup> <sup>w</sup> <sup>x</sup> 7 , Kagel and Roth 23 pp. 416–421 and Rein- Ž . heimer and Bodendorf 47 . When discussing auc- <sup>w</sup> <sup>x</sup> tions, we focus on auctioning a single good having multiple negotiable attributes<sup>r</sup>issues or multiple quantities of homogeneous goods, such as stocks. When discussing markets, we focus on the case of multiple diametrically opposed issues, as well as the case where quantity is a negotiable issue. A web site that runs the algorithms acts as the exchange mechanism.

The organization of the rest of the paper is as follows. In Section 2, we review the relevant literature. In Section 3, we discuss some theory of multiple-issue markets and auctions; in Section 4, auction algorithms and in Section 5, market algorithms. Section 6 concludes the paper.

## 2. Literature overview

We classify the literature into Electronic Negotiation Models, Automated Agents, Auctions and Markets. The literature is vast and draws upon Economics, Finance, Information Sciences, Marketing and Negotiation Science, among others. We focus on the recent electronic applications of auctions and markets and also provide some representative web site URLs. In many instances, the developments have been so rapid that the academic journals are lagging behind and many of the applications and publications can only be found in the WWW.

Different aspects of Electronic Commerce have been relatively well documented, although the research in the area is very active 5,6,9,13,31,44 .<sup>w</sup> <sup>x</sup> FastParts 71 and GE’s TPN 73 provide good<sup>w x</sup> <sup>w x</sup> examples of business-to-business Electronic Commerce web sites. See the reference list for URLs. The dramatic expansion and ease of Electronic Commerce will make electronic markets and auctions common. Obviously, it is not unimportant how such electronic markets and auctions are conducted. For interesting discussions see, the works of Fan et al. <sup>w x</sup> <sup>w x</sup> 15 and Klein 29 .

## 2.1. Electronic negotiation models

Computer-aided negotiation support models have been developed to provide analytical aid to negotiators, both as individuals and groups see, e.g., Refs.Ž <sup>w</sup> <sup>x</sup> 58,59 . Research in the area of negotiation model- . ing has been quite active within the last two decades. For a review of the literature, see the works of Teich et al. 57,60 . Kersten’s site 77 is representative of<sup>w</sup> <sup>x</sup> <sup>w x</sup> the current state of the art in electronic negotiations. Kersten’s site 77 is among the first web-based<sup>w</sup> <sup>x</sup> negotiation support sites and includes the possibility for asynchronous negotiations 26 . Segev’s site 81<sup>w x</sup> <sup>w x</sup> provides an extensive list of references and links.

## 2.2. Automated agents

In recent years, Artificial Intelligence researchers have created several software agents that aid in web browsing, searching, shopping, negotiating and other internet related tasks see, e.g., Refs. 4,12,28,40,43,Ž <sup>w</sup> 53,70 . The web portal Excite’s Jango 75 devel- <sup>x</sup>. <sup>w</sup> <sup>x</sup> Ž oped by Doorenbos et al. , a shopping agent, is . probably the biggest commercial success thus far of agent technology. This agent, and others, however, concentrate on finding the lowest price among merchants offering a specific product or service, as discussed in the introduction. MIT Media Lab’s forthcoming site T@T 82 promises to be an excep- <sup>w</sup> <sup>x</sup> tion, offering agent technology and Distributed Constraint Satisfaction Problem protocols to aid the multiple-issue<sup>r</sup>attribute choice problem 41 . Their<sup>w</sup> <sup>x</sup> earlier generation Kasbah 76 site offered automated<sup>w</sup> <sup>x</sup> negotiation utilizing different negotiation strategies over a single issue, price. The first generation shopping agents are already being used in some of the auction sites e.g., Refs. 66,69 .Ž <sup>w</sup> <sup>x</sup>.

## 2.3. Auctions

The most common types of auctions are the open English auction ascending price , the open DutchŽ . auction descending price , the closed Sealed bidŽ . auctions first or second price, the latter also known Ž as Vickery auction . Other more complicated auc- . tions are the Double auction multiple buyers andŽ sellers , Multi-unit auctions, such as the open En- . glish clock auction, the Combinatorial auction, which permits bids on groups of assets, and the Reverse or Procurement auction. Some of these auctions may be conducted as closed or as open auctions, simultaneous or sequential. There is extensive literature which discusses and tests these auctions using multiple performance measures, including revenue equivalence, the extent of price discrimination, and the efficiency of auctions 3,11,14,16,17,22,23,33–Ž<sup>w</sup> 38,50–52,56,62 ; Roth’s site 79 includes links to<sup>x</sup> <sup>w x</sup> literature . The auctions listed above are single-issue . Ž . price auctions, with the exceptions of Multi-unit auctions price and quantity and Combinatorial auc-Ž . tions groupings of assets .Ž .

Web-based electronic auctions have recently become very popular. For a review, see the works of Wellman and Wurman 64 and Wurman et al. 65 .<sup>w x</sup> <sup>w x</sup> As discussed by Schwartz 54 , hundreds of different<sup>w</sup> <sup>x</sup> types of electronic auctions exist. Design features include whether or not sellers specify reservation prices, whether there is automatic bidding for exam-Ž ple, Refs. 66,69,76 , whether bidders rate each<sup>w</sup> <sup>x</sup>. other via blacklists, when the auctions close and rules regarding the closing, the type of merchandise Ž . Ž new, used and the quantities offered one or multiple , whether we have a regular or reverse. <sup>r</sup>procurement auction see Refs. 72,80 . Priceline is a typeŽ <sup>w</sup> <sup>x</sup>. of reverse auction for unused capacity on airlines— being extended for automobiles and home mortgages, where bidders with a credit card commit-Ž ment ‘name their price’ 63 .. <sup>w</sup> <sup>x</sup>

## 2.4. Markets

Our market framework differentiates between auctions and markets. Yet, in practice, there is an overlapping area, specifically referred to in the auction literature as double auctions. Such double auctions serve many buyers and sellers. In fact, the continuous double auction is probably the oldest practised type of market exchange of goods and stocks, where buyers and sellers post their bids<sup>r</sup>asks continuously and transactions occur when they overlap, resulting in price discrimination throughout the trading day. A popular competing market is known as the Call market a.k.a. single price auction , where the auc-Ž . tioneer<sup>r</sup>marketer balances the supply and the demand and determines a single price at which all goods are exchanged at that uniform price during the trading day. Matching is an important aspect to some markets, especially the more complicated ones <sup>w</sup> <sup>x</sup> 18,24,39,49 .

Dissatisfaction with the high costs of using intermediaries when trading on organized exchanges has contributed to the development of electronic markets, either web-based or non-web-based. These costs include direct costs in terms of commissions paid to brokers and indirect costs, such as market impact, where high volume trades result in higher<sup>r</sup>lower trading prices. In particular, large institutional investors are highly motivated to avoid the indirect costs of market impact. See, for example, the works of Angel et al. 2 , Lupien and Rickard 32 and<sup>w x</sup> <sup>w</sup> <sup>x</sup> Schwartz 55 . This has led to the development of<sup>w</sup> <sup>x</sup> what are known as electronic fourth markets, such as Instinet and POSIT Portfolio System for Institu-Ž tional Trading , and the more recent web-based elec-. tronic markets. As examples of web-based electronic markets, see the Arizona Stock Exchange 67 a call <sup>w</sup> <sup>x</sup> Ž market , band-X 68 a classified ad market for the . <sup>w</sup> <sup>x</sup> Ž exchange of bandwidth , FastParts 71 a market for. <sup>w</sup> <sup>x</sup> Ž electronic components and GE’s TPN 73 a market. <sup>w</sup> <sup>x</sup> Ž for components ..

## 2.4.1. Case of OptiMark

Similar to Instinet and POSIT, OptiMark is an electronic stock exchange market, developed for institutional block traders. Even though the market is not web-based OptiMark is cooperating with bothŽ the Pacific Exchange and NASDAQ, set to begin early<sup>r</sup>later in 1999, respectively , we will discuss it. more in-depth because it is the only multiple-issue Ž . 2 market we are aware that exists. Those two issues are price of stock and quantity traded. Again, the motivation is to reduce the market impact of large institutional trades by encouraging traders to state preferences anonymously across ranges of priceŽ . and size, and matching buyers and sellers. Such large traders may be willing to accept a higher or lower price than the current market price for large volumes of trades. See the work of Lupien and Rickard 32<sup>w</sup> <sup>x</sup> and OptiMark’s site 78 ; IBM 74 provides the<sup>w x</sup> <sup>w x</sup> patent at their site. See also the work of Clemons and Weber 10 . In economic terms, they try to eliminate <sup>w</sup> <sup>x</sup> the shifts of demand or supply curves when new buyers<sup>r</sup>sellers enter or exit the market. OptiMark’s success in eliminating the market impact, stabilizing markets and reducing price volatility will be tested in actual use.

![](/api/attachments/6X6R3NFU/fulltext/images/6f51fececa8c193798e9e6435566bbeed8833dec9f546787a85eac094defd361.jpg)  
Fig. 2. OptiMark: buyer’s satisfaction density profile. Source: www.optimark.com.

![](/api/attachments/6X6R3NFU/fulltext/images/d31d784c98f82ffe63c6390fd7f4dc86d1f82d6f9660cdca064e5bb09105e511.jpg)  
Fig. 3. OptiMark aggregation stage. Source: www.optimark.com.

We have reproduced three figures from Opti-Mark’s web site and explain their electronic market system based on those. See Figs. 2–4. In Fig. 2, one buyer’s satisfaction density profile based on theŽ buyer’s underlying value function is exhibited..

Lupien and Rickard 32 use the following nota- <sup>w</sup> <sup>x</sup> tion. There are M buyers and N sellers. The size<sup>r</sup>price combinations are assigned—using contours of satisfaction—a value ranging from 0 to 1; a value of 0 indicates unwillingness to trade at that price<sup>r</sup>size combination; a value of 1 indicates the highest level of satisfaction. Only discrete levels of type 0.1, 0.2, 0.3, etc. are allowed, higher values indicating higher levels of preference for that price<sup>r</sup> size trade. However, the satisfaction values at prices between adjacent specified contours at each sizeŽ . are interpolated as floating point values. Every trader is required to indicate his<sup>r</sup>her satisfaction profiles for each stock he<sup>r</sup>she wants to trade, using the 0 to 1 scale. The actual detail and accuracy will, however, vary from trader to trader. The satisfaction density profiles are defined as $B _ { i } ( p , s )$ for buyer i and $S _ { k } ( p , s )$ for seller k where $p$ is price and s is quantity of stock.

![](/api/attachments/6X6R3NFU/fulltext/images/efe5d29e2d3f2dbcd075ef7ed733c077364809d81437c491b38d6bdafa794d5c.jpg)  
Fig. 4. OptiMark cross-products in stage 2. Source: www. optimark.com.

OptiMark then matches buyers and sellers based on a two-stage system. Fig. 3 explains the aggregation procedure, which is the first stage. Starting with the size<sup>r</sup>price cells containing a value $\cdot _ { 1 } \cdot$ for bothŽ buyer and seller , the algorithm attempts to match . traders by combining<sup>r</sup>aggregating smaller-quantity traders to larger-quantity traders at a single price. In the second stage, in Fig. 4, for remaining buyer–seller combinations, a ‘mutual satisfaction density profile value’ is calculated by multiplying the individual satisfaction density profiles. They define the mutual satisfaction density profile between the ith buyer and the kth seller to be

$$
\begin{array}{l} J _ {i k} (p, s) = B _ {i} (p, s) S _ {k} (p, s), \\ i = 1, \ldots , M; k = 1, \ldots , N. \end{array}
$$

The matching is based on the ranked list of MN cross-products for all price<sup>r</sup>size cells, the maximum of which is basically a Nash Bargaining Solution. OptiMark is planning to match buyers and sellers every 90 s. In case of ties, five rules exist to break them. <sup>3</sup>

## 3. Multiple-issue markets and auctions: some theory

## 3.1. Quantity is not an issue

Fig. 5a presents contract curves for a two-issue market<sup>r</sup>auction example, where there exists one seller and three potential buyers. When dealing with multiple issues in auctions and markets, in a diametrically opposed issue space, some matches of buyers and sellers make more sense than others because of dovetailing underlying values. If we map the contract curves from Fig. 5a to the utility space, we obtain Fig. 5b. The result is the three Pareto frontiers from which no joint gains are possible for that individual buyer<sup>r</sup>seller pair. The Anti-Pareto frontier is defined as the lower bound of the feasible region in the utility space. One such frontier for buyer1<sup>r</sup>seller, from which no joint losses are possible, is represented in the figure. Of course, Anti-Pareto frontiers exist for the other buyer<sup>r</sup>seller combinations as well, but are not depicted in the figure. Assuming all individual ‘value points’ derived from the buyers and seller’s value functions were known, as would be the case in experimental settings computer simu-Ž lations or human experiments , we could make the. following argument. From the seller’s point of view, it would make sense to match him<sup>r</sup>her with buyer 2 for lower levels of Issue 1 and Issue 2 and with buyer 3 for higher levels of Issue 1 and Issue 2. This is what we call the ‘Super Pareto Frontier’ consisting of the most northeasterly segments of the combined contract curves. In reality, we would not know the value points and we need algorithms to match buyers and sellers based on underlying dovetailed interests. Even without the value points, and considering the problem of interpersonal comparison of utilities, the inward or outward bulging shape of the utility curves could facilitate the identification of good matches and the concession making process in the issue space. The reason being that for outward bulging utility curves, a large concession in issue space may result in a small decrement of utility. For inward bulging utility curves, the opposite is true see Ref.Ž <sup>w</sup> <sup>x</sup> 42 . We are not advocating the automatic matching . of Seller with Buyers on the Super Pareto frontier. We expect the seller to be individually rational and

(a)  
![](/api/attachments/6X6R3NFU/fulltext/images/f315cb2788a543f5d2c2ec36c6ea2b6a76ff25c57a1142ad4aade297d6a0786a.jpg)

(b)  
![](/api/attachments/6X6R3NFU/fulltext/images/6e0bfb3030172b6ba2acc8cd27da66af987487eaf3b8ce7575f20ab2a37abeea.jpg)  
Fig. 5. a Contract curves for multiple-issue market: one seller and three potential buyers in a diametrically opposed issue space. b Super Ž . Ž . Pareto frontier in utility space for a .Ž .

negotiate with the buyer with whom he<sup>r</sup>she can receive the highest utility, and that could be buyer 1 in Fig. 5b and, hence, a Super Pareto solution would not be attained. Therefore, the concept of ‘good matches’ and ‘dovetailing interests’ may not always be useful in real situations because it depends on the trader’s BATNAs Best Alternative To a NegotiatedŽ Agreement and power, among others..

![](/api/attachments/6X6R3NFU/fulltext/images/68b7b0d6c1d87630bf0a4739b86e5969863f68cb2500c95a50975f6aec57cf41.jpg)  
Fig. 6. Contract curves for groups of sellers and buyers.

## 3.2. Quantity is an issue

In a multiple-issue market, when quantity is an issue, value is a function of both quantity and price, among others. The value functions of groups of sellers and buyers result in indifference curves in the multiple-issue space. These can then be viewed as a type of Edgeworth Box forming a contract curve at the tangency points of the indifference curves. This concept is demonstrated in a two-issue price Ž <sup>r</sup>quantity example in Fig. 6. A single point on the contract. curve will be implicitly ‘negotiated’ by market participants. Exactly where this negotiated point is on the curve is indeterminate, but will be converged upon at least with an efficient market mechanismŽ .

by market forces. In a seller’s market, a point in the upper right-hand-side of the curve will be converged upon, in a buyer’s market, a point in the lower right. In a simulated market with defined value functions, a researcher could determine whether the resulting trade agreement lies on this contract curve whichŽ would be Pareto Optimal or off it..

## 4. Multiple-issue auction algorithms

## 4.1. Quantity is not an issue

Fig. 7 illustrates the Leap Frog Method where bidders determine the path of bids. This is a natural extension of a typical single issue English auction where bidders shout out their bids. Each bid must be an improvement over the previous bid in at least one of the issues and no worse in any of the issues. We cannot advocate this method because the path is somewhat arbitrarily determined and it does not consider the preference of the auction maker at all.

![](/api/attachments/6X6R3NFU/fulltext/images/b525a532544a1f7d1dc082143972a49b0b305d47b204a37904e341e198ebd100.jpg)  
Fig. 7. Leap Frog Method: bidders determine path.

In Fig. 8, we describe an Auction Maker Controlled Bid Mechanism, which could be used in either a regular auction single seller or a reverseŽ . auction single buyer . In Fig. 8, we represent a Ž . preference path for a seller in a situation where the seller and the buyers are diametrically opposed in a two-issue space. The preference path is determined as follows: the seller rank orders his<sup>r</sup>her most important jumps from his<sup>r</sup>her nadir worst point forŽ . issues that are ‘discretized’. By discretized issues we mean continuous issues that have been given a set of discrete levels. If an issue already has a set of discrete levels, we could use those. The ranking process continues until all levels of each issue have an associated rank. The ranks determine the preference path for the seller and the path then in which the bidders would follow. If desired, the auction maker could provide the auctioneer or computerŽ . with a reservation level below which a bid is not accepted. We anticipate that this method will be preferred by the sellers, and the result will be more efficient than the result with the Leap Frog Method.

## 4.2. Quantity is an issue

We propose a discriminative auction for the multi-unit case in a computerized web environment. The advantage to the seller is that revenue should be maximized although this needs to be verified . TheŽ . advantage to the buyer is that the bid required to enter the ‘action’ is posted while keeping the actual bids sealed. We think that bidders will appreciate the additional information. By allowing some degree of price discrimination, but less than in a typical discriminative auction, the ‘winner’s curse’ effect can be reduced, thus encouraging active bidding.

We next introduce some terminology and notation. An actiÕe bid is one, which would be accepted at that price and quantity, if the auction were to close at that point in time. An inactiÕe bid is one that has expired because it was outbid. A semi-actiÕe bid is one in which the bidder will only receive a partial quantity if the auction closed at that point in time. Our algorithm assumes that bidders will accept partial quantities, if their bid is semi-active. In the work of Teich et al. 61 , we explore other variations of<sup>w</sup> <sup>x</sup> the algorithm which, among others, relax this assumption. $\boldsymbol { S } _ { i } = ( \boldsymbol { p } _ { i } , \boldsymbol { q } _ { i } ) ,$ , is the bid of bidder i, where $p _ { i } = \mathrm { p e r }$ unit price for bidder i, and $q _ { i } = \mathrm { q u a n t i t y }$ desired by bidder $i , ( i = 1 , \ldots , n ) ;$ ; n<sup>s</sup>number of bidders; D <sup>s</sup> number of units for sale; t <sup>s</sup> iteration counter; sp <sup>s</sup> suggested price at iteration t.

![](/api/attachments/6X6R3NFU/fulltext/images/7fe740f1d77deab054a5792a7ef71e99fb138a27731ee778d68b51b536b7fafe.jpg)  
Fig. 8. Auction market specified path.

An outline of our multiple unit discriminative auction algorithm is as follows.

Step 1. Auction owner specifies quantity for sale D, reservation prices, the closing time of the auction and the minimum increment in bids epsilon . Ž .

Step 2. Bidder i enters auction by specifying a desired quantity $q _ { i } ,$

Step 3. Bidders request a price. The suggested price, $\operatorname { s p } _ { t } ,$ is either at the reservation level if supply has not yet depleted, or at the previous level, or is calculated an epsilon amount above the previous price. The determination is based on whether total demand at that price can be met by the supply. If so, the price remains the same as previously; if not, it is increased by an epsilon amount.

Step 4. Bidders submit their bid $S _ { i }$ either at the level suggested by the algorithm, or above that level, or they drop out. Bids below the suggested level are not accepted.

Step 5. Bidders whose status changes are informed and requested to make a decision. Return to Step 2. Repeat until auction closes.

The revenue, increasing at every iteration, is calculated as follows.

Total Revenue $\textstyle = \sum _ { i = j + 1 } ^ { \mathtt { n } } p _ { i } q _ { i } + q _ { j \mathrm { r } } p _ { j } ,$ , where j refers to the semi-active bidder; $j + 1 , \dotsc , n$ are the active bidders. The residual quantity for semi-active bidder j is:

$$
q _ {j \mathrm{r}} = D - \sum_ {i = j + 1} ^ {n} q _ {i} \text {   iff   } \sum_ {i = j + 1} ^ {n} q _ {i} + q _ {j} > D, \text {   otherwise },
$$

$$
q _ {j \mathrm{r}} = 0.
$$

In the above formula, note that j refers to a semi-active bidder if such a bidder exists andŽ . $j +$ $1 , \ldots , n$ to the active bidders. Hence, if the demand by active bidders and the new semi-active bidder Ž . j exceeds D, by definition, the semi-active bidder receives a fraction, but not all he<sup>r</sup>she wants. If the demand of the active bidders and the new bidder does not exceed D, there is no semi-active bidder.

![](/api/attachments/6X6R3NFU/fulltext/images/fc252f004b704e5c79a517ae357478de31b0eec7e2938adabe36490eec746bf8.jpg)  
Fig. 9. Price<sup>r</sup>quantity auction example.

As an example, assume a seller has 100 units of a homogenous good to auction, with a reservation price of US\$1 per unit, and epsilon is 5%. At time 1, bidder 1 enters the auction, specifies a quantity of 50 and requests a price from the auction mechanism. Since there are no other bids, the reservation price is suggested to the bidder. He makes his bid 1, 50 andŽ . it becomes active in status. At time 2, bidder 2 enters, specifies a quantity of 40 and requests a price. Again, the reservation price of US\$1 is suggested, because the supply has not yet been depleted. Bidder 2 makes his bid 1, 40 and it becomes activeŽ . in status. At time 3, bidder 3 enters the auction, and specifies a quantity of 30. At this point, the supply is depleted and a new price must be calculated. The auction mechanism calculates a price an epsilon percentage 5% above the latest price, and a price ofŽ . US\$1.05 is suggested to the bidder. He<sup>r</sup>she then makes the bid 1.05, 30 . Bidder 2 then is outbid andŽ . thus becomes semi-active with a quantity of 20 units, because he<sup>r</sup>she was the last one to bid at the price of US\$1. Bidder 1 remains active. At time 4, bidder 2 has three options. He<sup>r</sup>she can withdraw from the auction completely, stay semi-active in status, or re-bid. Assume he<sup>r</sup>she decides to re-bid at the same quantity of 40 units, and requests a price. The price US\$1.05 is suggested by the mechanism because at that price the quantities of bidders 2 and 3 would be met by the supply. Bidder 2 then makes his<sup>r</sup>her bid Ž . 1.05, 40 . Bidder 3 remains active in status and bidder 1 becomes semi-active with a quantity of 30 units. At time 5, bidder 1 has, again, three options, i.e., withdraw, remain semi-active or re-bid. Assume he<sup>r</sup>she decides to re-bid and requests a price. The mechanism then returns a price of US\$1.1025 because at US\$1.05 the demand is greater than the supply. Therefore, the new price must be calculated at 5% above the most recent price suggested of Ž US\$1.05 . If bidder 1 makes this bid 1.1025, 50 ,. Ž . he<sup>r</sup>she will become active in status, bidder 3 will remain active, and bidder 2 will become semi-active with a quantity of 20. The process repeats until the auction closes. See Fig. 9 for status and positions at the close and the following table for the sequence of the bids.

<table><tr><td>Time</td><td>Bidder/bid#</td><td>q</td><td>p</td></tr><tr><td>1</td><td>1/1</td><td>50</td><td>1</td></tr><tr><td>2</td><td>2/1</td><td>40</td><td>1</td></tr><tr><td>3</td><td>3/1</td><td>30</td><td>1.05</td></tr><tr><td>4</td><td>2/2</td><td>40</td><td>1.05</td></tr><tr><td>5</td><td>1/2</td><td>50</td><td>1.1025</td></tr></table>

Table 1  
OptiMark cross product scores

<table><tr><td rowspan="13">Buyer profile</td><td>1.00</td><td>0.00</td><td>0.10</td><td>0.20</td><td>0.30</td><td>0.40</td><td>0.50</td><td>0.60</td><td>0.70</td><td>0.80</td><td>0.90</td><td>1.00</td></tr><tr><td>0.90</td><td>0.00</td><td>0.09</td><td>0.18</td><td>0.27</td><td>0.36</td><td>0.45</td><td>0.54</td><td>0.63</td><td>0.72</td><td>0.81</td><td>0.90</td></tr><tr><td>0.80</td><td>0.00</td><td>0.08</td><td>0.16</td><td>0.24</td><td>0.32</td><td>0.40</td><td>0.48</td><td>0.56</td><td>0.64</td><td>0.72</td><td>0.80</td></tr><tr><td>0.70</td><td>0.00</td><td>0.07</td><td>0.14</td><td>0.21</td><td>0.28</td><td>0.35</td><td>0.42</td><td>0.49</td><td>0.56</td><td>0.63</td><td>0.70</td></tr><tr><td>0.60</td><td>0.00</td><td>0.06</td><td>0.12</td><td>0.18</td><td>0.24</td><td>0.30</td><td>0.36</td><td>0.42</td><td>0.48</td><td>0.54</td><td>0.60</td></tr><tr><td>0.50</td><td>0.00</td><td>0.05</td><td>0.10</td><td>0.15</td><td>0.20</td><td>0.25</td><td>0.30</td><td>0.35</td><td>0.40</td><td>0.45</td><td>0.50</td></tr><tr><td>0.40</td><td>0.00</td><td>0.04</td><td>0.08</td><td>0.12</td><td>0.16</td><td>0.20</td><td>0.24</td><td>0.28</td><td>0.32</td><td>0.36</td><td>0.40</td></tr><tr><td>0.30</td><td>0.00</td><td>0.03</td><td>0.06</td><td>0.09</td><td>0.12</td><td>0.15</td><td>0.18</td><td>0.21</td><td>0.24</td><td>0.27</td><td>0.30</td></tr><tr><td>0.20</td><td>0.00</td><td>0.02</td><td>0.04</td><td>0.06</td><td>0.08</td><td>0.10</td><td>0.12</td><td>0.14</td><td>0.16</td><td>0.18</td><td>0.20</td></tr><tr><td>0.10</td><td>0.00</td><td>0.01</td><td>0.02</td><td>0.03</td><td>0.04</td><td>0.05</td><td>0.06</td><td>0.07</td><td>0.08</td><td>0.09</td><td>0.10</td></tr><tr><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td></td><td>0.00</td><td>0.10</td><td>0.20</td><td>0.30</td><td>0.40</td><td>0.50</td><td>0.60</td><td>0.70</td><td>0.80</td><td>0.90</td><td>1.00</td></tr><tr><td></td><td colspan="11">Seller profile</td></tr></table>

Prior to the auction, the seller has the right to set a reservation price. This reservation price could refer to the total minimum revenue generated from the auction, or he<sup>r</sup>she could use multiple reservation prices for different quantities. For example, he<sup>r</sup>she could specify that for quantities between 1 and 10 units the reservation price is, say, US\$100 per unit, and for quantities above 10, the reservation price per unit is US\$90.

In our algorithm, the price discrimination is reduced to an epsilon difference if the bidders accept the suggested bid. If, however, they bid above the suggested bid, then, the price discrimination level could be higher. Why would a bidder be willing to pay above the suggested price level? This could happen if the bidder wants to decrease the probability of being outbid. If an automatic bidding mechanism is used, then the bidder could specify the top price to bid at his quantity, and the mechanism would automatically re-bid on his<sup>r</sup>her behalf up to that point. Beyond that point, he<sup>r</sup>she could specify a reduced quantity up to another level, and so on.

Table 2  
Modified 0-4 point scheme: cross products

<table><tr><td rowspan="7">Buyer profile</td><td>4</td><td>0</td><td>4</td><td>8</td><td>12</td><td>16</td></tr><tr><td>3</td><td>0</td><td>3</td><td>6</td><td>9</td><td>12</td></tr><tr><td>2</td><td>0</td><td>2</td><td>4</td><td>6</td><td>8</td></tr><tr><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td colspan="6">Seller profile</td></tr></table>

Key: 4 best of threes, 3 happy with trade, 2 best of ones, 1 willing to trade, 0 not willing to trade.

## 5. Multiple-issue market algorithms

OptiMark’s two-issue market algorithm is novel and is gaining momentum among practitioners. Opti-Mark’s training institute has taught over 2000 traders to use their forthcoming system. It does have several appealing features: anonymity, possible elimination of market impact, preference elicitation over two issues and the aggregation of small trades matched with larger quantities. However, we have some criticisms towards the algorithm, which we wish to discuss. We also provide some suggestions for improving the preference elicitation and the matching.

## 5.1. Quantity is an issue

Table 3  
Modified 0-2 point scheme: cross products

<table><tr><td rowspan="5">Buyer profile</td><td>2</td><td>0</td><td>2</td><td>4</td></tr><tr><td>1</td><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td></td><td>0</td><td>1</td><td>2</td></tr><tr><td></td><td colspan="2">Seller profile</td><td></td></tr></table>

Key: 2 Best, 1 will trade, 0 no trade.

OptiMark allows price discrimination, that is, trading same stocks at the same time at different prices. OptiMark accepts price discrimination, because it allows greater quantities to be traded—a feature OptiMark and, apparently their customers, see desirable. Even though the level of price discrim-

(b)  
(a)  
![](/api/attachments/6X6R3NFU/fulltext/images/870ca0fe093d8e57a48d320252519ada9a407dc2f225ba6350d1a4e91252d16b.jpg)

![](/api/attachments/6X6R3NFU/fulltext/images/7ddc689171c37d9d8d4860a611c155528c1db7cc56752f75f0b97234f4f899a5.jpg)  
Fig. 10. a Seller’s prefrence profile in 2–1–0 method example. b Buyer’s preference profile in 2–1–0 method example. c Ž . Ž . Ž . Cross-products of buyer<sup>r</sup>seller profiles from Fig. 10a and b: line crosses region of ‘1s’. d Cross-products of buyer Ž . <sup>r</sup>seller profiles: line does not cross region of ‘1s’.

(c)  
![](/api/attachments/6X6R3NFU/fulltext/images/8aad9cceba1082929d4a4cf7f7f14195efc2e7af7dcf418ce7cf53c000088f1e.jpg)

(d)  
![](/api/attachments/6X6R3NFU/fulltext/images/07acad8179ae92559ba3b6b3fec15c1a3a7de3e6927b471a1b04fb2648c61098.jpg)

ination will not go unreported, <sup>4</sup> a trader would have to work to find it out. The level of price discrimination could be larger with OptiMark contrasted with traditional stock exchange trading. ‘Winners curse may be avoided because traders may not know they have been ‘cursed’.

We are critical of the 0, 0.1, 0.2, . . . , 0.9, 1 preference elicitation scale. OptiMark explains that a 0 means unwillingness to trade and a 1 means total satisfaction with the trade. Scores in-between differentiate between levels of preference. This seems to be too complicated to be done every 90 s, even though OptiMark counters that traders can input preference scores as quick<sup>r</sup>dirty as they desire and yet still obtain desirable trades. OptiMark seems to agree, since they have plans to increase the degree of automation of the preference elicitation process in the future 48 . We question why anyone would be<sup>w</sup> <sup>x</sup> willing to furnish preference scores between 0 and 1 with their system and are concerned that traders do not specify a unique ‘feasible’ single best ‘1’ cell. Furthermore, some traders may be more skillful than others in strategically manipulating scores to gain advantage arbitrage? over other traders. ObviouslyŽ . values<sup>r</sup>preference scores cannot be compared across people. As discussed below, our suggestion is to use a cruder scale.

Even if traders shared the same preference scale and accurately portrayed it, ranking the cells based on the product of preference scores, is arbitrary. See Table 1, where we have reproduced the possible OptiMark cross-products. For example, the product of 0.6 and 0.6 is the same as 0.4 and 0.9. Nash and OptiMark treat the cells as equally good. Subjectively, we would argue that 0.6 times 0.6 would be a better match assuming that 0.6 means the same forŽ both traders . Similarly, OptiMark’s matching algo-. rithm would prefer 0.5 times 1 to 0.7 times 0.7. Again, we would argue that the latter would be a better match. For a criticism of the use of the Nash bargaining solution in negotiation literature, see the work of Raiffa 45 .<sup>w</sup> <sup>x</sup>

In Tables 2 and 3, we have calculated cross-products associated with two simple preference elicitation schemes. Table 2 is based on a 0–4 scheme and Table 3 on an even simpler 0–2 scheme. In the 0–4 scheme a trader will only specify a single ‘4’ value, as well as at most a single ‘2’ value. Likewise, in the 0–2 scheme a trader would specify only a single ‘2 value. In practice, for the ‘single best cell’ concept to work, we should specify certain realistic ranges, from which the trader picks the best. The 0–4 and the 0–2 scales are quick and dirty and fairly easy to specify. In both of these scales, the maximum of the minimum scores is the same as the maximum of the cross-products, which is untrue in the original Opti-Mark scheme, as demonstrated above. Raiffa 46<sup>w</sup> <sup>x</sup> argues that the max–min rule may be more fair than the max cross-product rule. This perceived benefit comes with the additional cost of an increased number of ties, which must be resolved one way or another.

In both the 0–4 scheme and the 0–2 scheme, there are two phases in the matching process.

Phase 1: Find the cross-products the same as inŽ OptiMark and match the ranked list. .

Phase 2: There will be ties, especially on the ‘one’ cross-products. We describe below three possible tie breaker rules. Our description is specifically tailored for the 0–2 scheme see, for example, Fig. Ž 10a and b , however, with slight modification they . could also be applied to the 0–4 scheme.

Idea A B tie breaker: Count the number of tiesŽ . for each pair. Start matching based on the LARGEST Ž . Ž . SMALLEST number of ties 1s most likely . For each matching pair, draw a line between the 2s mostŽ preferred points . Mark the tied region see Fig. . Ž 10c . If the line passes through the marked region,. select the cell where the midpoint of the line segment passing through the marked region is located. If the line does not pass through the marked region, then select the cell that is closest to the overall midpoint of the line connecting the two best cells Ž . see Fig. 10d .

Idea C: Force the matches which simply maximize quantity of shares traded. The true maximum quantity would be computationally difficult to calculate with a large number of tied traders a combina- Ž torial<sup>r</sup>maximum flow network problem . Therefore,. we suggest a greedy heuristic approach to approximate this maximum quantity. For all tied traders, first calculate the maximum quantity for each paired buyer<sup>r</sup>seller combination. Match the buyer<sup>r</sup>seller whose quantity is highest in case of no unique price, Ž split the difference in price , delete that pair and. repeat until all feasible pairs have been matched.

Which of these ideas performs best awaits further testing and analysis as well as thorough comparison to the operation of OptiMark’s original algorithm.

## 5.2. Quantity is not an issue

In Fig. 11, we present the preference paths for three buyers and one seller who are diametrically opposed in a two-issue space see also Ref. 30 . AsŽ  . explained in Section 2.3, the preference paths are determined by having each party rank order the most important jumps from their nadir worst point for Ž . issues that are ‘discretized’. The ranks determine the preference path for each trader. The traders could specify their reservation levels on their preference path if desired. We match sellers and buyers based

Buyer's Preferred Poin

![](/api/attachments/6X6R3NFU/fulltext/images/00b71ab09ba805c3d4912c51b0935e53bc9f807cd9592e4e9d7c0828b9021241.jpg)  
Fig. 11. Preference paths for four parties in Fig. 5a example.

on their ‘closeness’ of the path and suggest they negotiate with that party. If they have specified their reservation level on that path, we can check if there is an overlap and a possible agreement zone. If a match occurs, we inform the two parties and they close the deal.

A word of explanation regarding the definition of closeness and why closeness is desirable is in order. If a buyer’s and seller’s preference paths overlap completely, this implies that there is complete dovetailing interests. In other words, what one party desires most, the other party desires least. On the other extreme, if preference paths are completely divergent, then there is no dovetailing interests, meaning both parties desire the same things. Geometrically, a simple measure of closeness of two preference paths is the area between the paths. In higher dimensions, this concept is more difficult to operationalize. Instead, we recommend that we base the measure of closeness on the distance between the coordinates of the points on the paths.

In case the participating sellers and buyers agree, we could automate the matching based on minimum distance and overlapping reservation levels and select a settlement point. One settlement option could be the midpoint of the overlapping reservation levels. If the sellers and buyers do not agree to automate, we would simply notify the participants of a close match and allow them to negotiate.

The closer the paths, the better the match. Of course, if reservation levels are specified and overlap, then an agreement zone exists. Even if a good match exists, reservation levels may not overlap. The reverse is also possible, in other words, bad matches may have overlapping reservation levels.

## 6. Concluding discussion

We have presented and discussed several multiple-issue auction and market algorithms. Much literature exists that discusses auctions and markets. However, very few mention multiple-issue auctions and markets and few algorithms and procedures exist for such situations. To compare and contrast such algorithms in an experimental setting, a number of performance measures could be utilized. They mostly relate to the quantity or value of goods traded, and stability and efficiency of trades. Quantity and value of goods traded is self explanatory. One common measure of the efficiency of markets is the percentage of the maximum possible gains from trade which is realized by the allocation process. It is computed as the sum total of consumer surplus and producer surplus divided by total possible sum. A traditional measure of stability is the Nash Equilibrium. Pareto Optimality of realized trades is of particular interest in multiple-issue markets because of the potential of logrolling and generating joint gains.

Our future work includes experimentation with human subjects and computer simulation of various algorithms and their impact on markets and auctions under controlled experimental settings. We are in the process of implementing several of the algorithms to the web environment. The aim is to improve the performance of auctions and markets by matching consumers and producers based on their underlying preferences and dovetailing interests. Such matching will reduce the likelihood of damaging price wars and increase the satisfaction of the traders.

## Acknowledgements

We wish to express our thanks to Professor Gregory Kersten, University of Carleton, for useful suggestions regarding literature on electronic markets and auctions. We also express our thanks to Dr. John T. Rickard, OptiMark Technologies, and Mr. Alexander Zaitsev, Moscow State University, for very useful comments.

## References

<sup>w</sup> <sup>x</sup> 1 G. Anders, The big Internet challenge, Wall Street Journal Ž . July 23, 1998 .

<sup>w</sup> <sup>x</sup> 2 J.J. Angel, G.I. Gastineau, C.J. Weber, Reducing the market impact of large stock trades, Journal of Portfolio Management Fall 1997 69–76.Ž .

<sup>w</sup> <sup>x</sup> 3 O. Ashenfelter, How auctions work for wine and art, Journal of Economic Perspectives 3 1989 23–36.Ž .

<sup>w</sup> <sup>x</sup> 4 M. Barbuceanu, M.S. Fox, Integrating communicative action, conversations and decision theory to coordinate agents, Proceedings of the First International Conference on Autonomous Agents, Agents 97, Marina Del Rey, ACM, 1997.

<sup>w</sup> <sup>x</sup> 5 A. Barua, S. Ravindran, A.B. Whinston, Efficient selection of suppliers over the internet, Journal of Management Information Systems 13 1997 117–127.Ž .

<sup>w</sup> <sup>x</sup> 6 J.B. Baty, R.M. Lee, InterShop: enhancing the vendor<sup>r</sup>

customer dialectic in electronic shopping, Journal of Management Information Systems 11 1995 9–19. Ž .

<sup>w</sup> <sup>x</sup> 7 F. Bodendorf, T. Bui, S. Reinheimer, A software-agent-based DSS for supporting an electronic air cargo market, Proceedings of the International Society of Decision Support Systems ISDSS’97 , Lausanne, Schweiz, 1997, pp. 181–194.Ž .

<sup>w</sup> <sup>x</sup> 8 K. Burdett, M.G. Coles, Steady state price distributions in a noisy search equilibrium, Journal of Economic Theory 72 Ž . 1997 1–32.

<sup>w</sup> <sup>x</sup> 9 S.Y. Choi, D.O. Stahl, A.B. Whinston, The Economics of Electronic Commerce, Macmillan, New York, 1997.

<sup>w</sup> <sup>x</sup> 10 E. Clemons, B. Weber, Restructuring institutional block trading: an overview of the OptiMark system, Journal of Management Information Systems 15 1998 41–60.Ž .

<sup>w</sup> <sup>x</sup> 11 J.C. Cox, V.L. Smith, J.M. Walker, Theory and behavior of multiple unit discriminative auctions, The Journal of Finance 34 1984 983–1010.Ž .

<sup>w</sup> <sup>x</sup> 12 R.B. Doorenbos, O. Etzioni, D.S. Weld, A scalable comparison-shopping agent for the world-wide web, Proceedings of the First International Conference on Autonomous Agents, Agents 97, Marina Del Rey, ACM, 1997.

<sup>w</sup> <sup>x</sup> 13 G. Elofson, W.N. Robinson, Creating a custom mass-production channel on the internet, Communications of the ACM 41 Ž .1998 56–62.

<sup>w</sup> <sup>x</sup> 14 R. Engelbrecht-Wiggans, Revenue equivalence in multi-object auctions, Economics Letters 26 1988 15–19. Ž .

<sup>w</sup> <sup>x</sup> 15 M. Fan, J. Stallaert, A. Whinston, Creating electronic markets, Dr. Dobb’s Journal, Issue 11, November 1998.

<sup>w</sup> <sup>x</sup> 16 R.A. Feldman, R. Mehra, Auctions: theory and applications, International Monetary Fund Staff Papers 40 1993 485–504.Ž .

<sup>w</sup> <sup>x</sup> 17 R.A. Feldman, R. Mehra, Auctions: a sampling of techniques, Finance and Development September Issue 1993b Ž . Ž . 32–35.

<sup>w</sup> <sup>x</sup> 18 L.N. Foner, Yenta: a multi-agent, referral-based matchmaking system, Proceedings of the First International Conference on Autonomous Agents, Agents 97, Marina Del Rey, ACM, 1997.

<sup>w</sup> <sup>x</sup> 19 R.H. Guttman, P. Maes, Agent-mediated Integrative Negotiation for Retail Electronic Commerce, MIT Media Lab Paper, 1998a.

<sup>w</sup> <sup>x</sup> 20 R.H. Guttman, P. Maes, Cooperative vs. Competitive Multiagent Negotiations in Retail Electronic Commerce, MIT Media Lab Paper, Forthcoming in Proceedings of the Second International Workshop on Cooperative Information Agents, Paris, July 1998. <sup>5</sup>

<sup>w</sup> <sup>x</sup>21 R.H. Guttman, R.H. Moukas, P. Maes, Agent-Mediated Electronic Commerce: A Survey, MIT Media Lab Paper, Forthcoming in Knowledge Engineering Review, June 1998. <sup>5</sup>

<sup>w</sup> <sup>x</sup> 22 D.B. Hausch, Multi-object auctions: sequential vs. simultaneous sales, Management Science 32 1986 1599–1610.Ž .

<sup>w</sup> <sup>x</sup> 23 J. Kagel, A. Roth Eds. , Handbook of Experimental Eco- Ž . nomics, Princeton Univ. Press, Princeton, NJ, 1995.

<sup>w</sup> <sup>x</sup> 24 M. Kallio, S. Salo, Competitive Equilibrium Applied to a

Commodity Exchange for Timber Trade, Helsinki School of Economics Working Paper, Department of Economics, 1993.

<sup>w</sup> <sup>x</sup> 25 J.O. Kephart, J.E. Hanson, J. Sairamesh, Price-War Dynamics in a Free-Market Economy of Software Agents, IBM Thomas J. Watson Research Center Working Paper, 1998.

<sup>w</sup> <sup>x</sup> 26 G. Kersten, S.J. Noronha, Negotiation Via the World Wide Web: A Cross-Cultural Study of Decision Making, IIASA Interim Report IR 97-052, 1997. <sup>6</sup>

<sup>w</sup> <sup>x</sup> 27 G. Kersten, S. Szpakowicz, Modelling Business Negotiations for Electronic Commerce, IIASA Interim Report IR 98-015, 1998. <sup>6</sup>

<sup>w</sup> <sup>x</sup> 28 L.-P. Khoo, S.B. Tor, S.S.G. Lee, The potential of intelligent software agents in the world wide web in automating part procurement, International Journal of Purchasing and Materials Management 34 1998 46–52.Ž .

<sup>w</sup> <sup>x</sup> 29 S. Klein, EM-electronic auctions, EM-Electronic Markets 7 Ž . Ž .4 1997 .

<sup>w</sup> <sup>x</sup> 30 P. Korhonen, N. Oretskin, J. Teich, J. Wallenius, The impact of a biased starting position in a single negotiation text type mediation, Group Decision and Negotiation 4 1995 357–Ž . 374.

<sup>w</sup> <sup>x</sup> 31 H.G. Lee, T.H. Clark, Market process reengineering through electronic market systems: opportunities and challenges, Journal of MIS 13 1997 113–136.Ž .

<sup>w</sup> <sup>x</sup> 32 W.A. Lupien, J.T. Rickard, Crossing Network Utilizing Optimal Mutual Satisfaction Density Profile, United States Patent a5689652, 1997.

<sup>w</sup> <sup>x</sup> 33 R.P. McAfee, J. McMillan, Auctions and bidding, Journal of Economic Literature 25 1987 699–738.Ž .

<sup>w</sup> <sup>x</sup> 34 R.P. McAfee, J. McMillan, Competition and game theory, Journal of Marketing Research 33 1996 263–267.Ž .

<sup>w</sup> <sup>x</sup> 35 K.A. McCabe, S. Rassenti, V.L. Smith, Auction institutional design: theory and behavior of simultaneous multiple-unit generalizations of the dutch and english auctions, The American Economic Review 80 1990 1276–1283.Ž .

<sup>w</sup> <sup>x</sup> 36 K.A. McCabe, S. Rassenti, V.L. Smith, Smart computer-assisted markets, Science 254 1991 534–538.Ž .

<sup>w</sup> <sup>x</sup> 37 K.A. McCabe, S. Rassenti, V.L. Smith, Testing Vickrey’s and other simultaneous multiple unit versions of the English auction, Research in Experimental Economics 4 1991 45–Ž . 79.

<sup>w</sup> <sup>x</sup> 38 P. Milgrom, Auctions and bidding: a primer, Journal of Economic Perspectives 3 1989 3–22.Ž .

<sup>w</sup> <sup>x</sup> 39 S. Mongell, A.E. Roth, Sorority rush as a two-sided matching mechanism, American Economic Review 81 1991 441–Ž . 464.

<sup>w</sup> <sup>x</sup>40 A. Moukas, G. Zacharia, Evolving a multi-agent information filtering solution in Amalthaea, Proceedings of the First International Conference on Autonomous Agents, Agents 97, Marina Del Rey, ACM, 1997.

<sup>w</sup> <sup>x</sup> 41 A. Moukas, R. Guttman, P. Maes, Agent-mediated Electronic Commerce: An MIT Media Laboratory Perspective, MIT

Media Lab Paper, Proceedings of the First International Conference on Electronic Commerce ICEC 98 , Seoul, Ko- Ž . rea, April 1998. <sup>5</sup>

<sup>w</sup> <sup>x</sup> 42 J. Mumpower, The judgment policies of negotiators and the structure of negotiation problems, Management Science 37 Ž . 1991 1304–1324.

<sup>w</sup> <sup>x</sup> 43 J.R. Oliver, A machine-learning approach to automated negotiation and prospects for electronic commerce, Journal of Management Information Systems 13 1997 83–112.Ž .

<sup>w</sup> <sup>x</sup> 44 R.A. Peterson, S. Balasubrmanian, B.J. Bronnenberg, Exploring the implications of the Internet for consumer marketing, Journal of the Academy of Marketing Science 25 1997Ž . 329–346.

<sup>w</sup> <sup>x</sup> 45 H. Raiffa, The Art and Science of Negotiation, Harvard Univ. Press, Cambridge, MA, 1982.

<sup>w</sup> <sup>x</sup> 46 H. Raiffa, Lectures on Negotiation Analysis, Program on Negotiation Books, Cambridge, MA, 1996.

<sup>w</sup> <sup>x</sup> 47 S. Reinheimer, F. Bodendorf, Price finding mechanisms in an electronic air cargo market, Proceedings of the 5th European Conference on Information Systems ECIS’97 , Cork, Ire-Ž . land, 1997.

<sup>w</sup> <sup>x</sup> 48 J.T. Rickard, N.G. Torre, Theory of optimal transaction implementation, Presented at the 32nd Asilomar Conference on Signals, Systems and Computers, November 1–4, 1998.

<sup>w</sup> <sup>x</sup> 49 A.E. Roth, M.A. Oliveira Doyomsyot, Two-sided Matching: A Study in Game-Theoretic Modeling and Analysis, Cambridge Univ. Press, Cambridge, UK, 1990.

<sup>w</sup> <sup>x</sup> 50 M.H. Rothkopf, E. Dougherty, M. Rose, Comment on multiobject auctions: sequential vs. simultaneous sales, Management Science 32 1986 1611–1612.Ž .

<sup>w</sup> <sup>x</sup> 51 M.H. Rothkopf, R.M. Harstad, Modeling competitive bidding, Management Science 40 1994 364–384. Ž .

<sup>w</sup> <sup>x</sup> 52 M.H. Rothkopf, A. Pekec, R.M. Harstad, Computationally Manageable Combinatorial Auctions, DIMACS Technical Report 95-09, Forthcoming in Management Science, 1995.

<sup>w</sup> <sup>x</sup> 53 T. Sandholm, V. Lesser, Issues in Automated Negotiation and Electronic Commerce: Extending the Contract Net Framework, University of Massachusetts at Amherst, Computer Science Department Working Paper, 1995.

<sup>w</sup> <sup>x</sup> 54 E.I. Schwartz, At On-line auctions, good and raw deals, New York Times March 5th Issue 1998 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 55 R.A. Schwartz, Reshaping the equity markets: a guide for the 1990s, Harper Business 1991 .Ž .

<sup>w</sup> <sup>x</sup> 56 V.L. Smith, Papers in Experimental Economics, Cambridge Univ. Press, New York, 1991.

<sup>w</sup> <sup>x</sup>57 J.E. Teich, H. Wallenius, J. Wallenius, Advances in negotiation science, Transactions on Operational Research 6 1994Ž . 55–94.

<sup>w</sup> <sup>x</sup> 58 J.E. Teich, H. Wallenius, M. Kuula, S. Zionts, A decision support approach for negotiation with an application to agricultural income policy negotiations, European Journal of Operational Research 81 1995 76–87.Ž .

<sup>w</sup> <sup>x</sup> 59 J.E. Teich, H. Wallenius, J. Wallenius, S. Zionts, Identifying pareto-optimal settlements for two-party resource allocation negotiations, European Journal of Operational Research 93 Ž .1996 536–549.

<sup>w</sup> <sup>x</sup> 60 J.E. Teich, H. Wallenius, J. Wallenius, World-Wide-Web

Technology in Support of Negotiation and Communication, Journal of Technology Management 17 1999 223–229.Ž .

61 J.E. Teich, H. Wallenius, J. Wallenius, A. Zaitsev, A Multiple Unit Auction Algorithm: Some Theory and a Web Implementation, Forthcoming in EM-Electronic Markets, the International Journal of Electronic Commerce and Business Media.

<sup>w</sup> <sup>x</sup> 62 R. Tenorio, Revenue equivalence and bidding behavior in a multi-unit auction market: an empirical analysis, The Review of Economics and Statistics May, 1993 302–314.Ž .

<sup>w</sup> <sup>x</sup> 63 J.S. Walker, B. Schneier, J.A. Jorasch, Method and apparatus for a cryptographically assisted commercial network system designed to facilitate buyer-driven conditional purchase offers, US Patent Number 5794207, 1996.

<sup>w</sup> <sup>x</sup>64 M.P. Wellman, P.R. Wurman, Real Time Issues for Internet Auctions, First IEEE Workshop on Dependable and Real-Time E-Commerce Systems DARE-98 , Denver, USA, JuneŽ . 1998.

<sup>w</sup> <sup>x</sup>65 P.R. Wurman, W.W. Walsh, M.P. Wellman, Flexible double auctions for electronic commerce: theory and implementation, University of Michigan, Artificial Intelligence Laboratory, forthcoming in Decision Support Systems, 1998.

<sup>w</sup> <sup>x</sup> 66 AuctionBot: http:<sup>rr</sup>auction.eecs.umich.edu<sup>r</sup>

<sup>w</sup> <sup>x</sup> 67 Arizona Stock Exchange: www.azx.com

<sup>w</sup> <sup>x</sup> 68 Band-X: www.band-X.com

<sup>w</sup> <sup>x</sup> 69 Bid4it: www.bid4it.com

<sup>w</sup> <sup>x</sup> 70 BotSpot: botspot.com

<sup>w</sup> <sup>x</sup> 71 FastParts: www.fastparts.com

<sup>w</sup> <sup>x</sup> 72 Freemarkets: www.freemarkets.com

<sup>w</sup> <sup>x</sup> 73 GE’s TPN: www.geic.tpn.com

<sup>w</sup> <sup>x</sup> 74 IBM Patent site: http:<sup>rr</sup>www.patents.ibm.com<sup>r</sup>

<sup>w</sup> <sup>x</sup> 75 Jango: www.jango.com

<sup>w</sup> <sup>x</sup> 76 Kasbah: kasbah.media.mit.edu

<sup>w</sup> <sup>x</sup> 77 Kersten’s site: http:<sup>rr</sup>interneg.carleton.ca<sup>r</sup>

<sup>w</sup> <sup>x</sup> 78 OptiMark: www.optimark.com and www.hipermarkets.com

<sup>w</sup> <sup>x</sup> 79 Roth’s site: http:<sup>rr</sup>www.pitt.edu<sup>r ;</sup> alroth<sup>r</sup>alroth.htmla vshort

<sup>w</sup> <sup>x</sup> 80 Priceline: www.priceline.com

<sup>w</sup> <sup>x</sup> 81 Segev’s site: http:<sup>rr</sup>haas.berkeley.edu<sup>r ;</sup> citm<sup>r</sup>nego<sup>r</sup> nego-frames.html

<sup>w</sup> <sup>x</sup> 82 T@T: http:<sup>rr</sup>ecommerce.media.mit.edu<sup>r</sup>tete-a-tete<sup>r</sup>index. html

Dr. Jeffrey Teich is an Associate Professor at the New Mexico State University. His research interests and publications are in the areas of negotiation modeling and decision support. In addition, he has served as Visiting Professor at the Helsinki School of Economics teaching in its international programs.

Dr. Hannele Wallenius is a Senior Lecturer at the Department of Industrial Management, the Helsinki University of Technology. Her research interests and publications are in the areas of public sector operations research and negotiation modeling.

Dr. Jyrki Wallenius is Professor of Management and Director of the International Center at the Helsinki School of Economics. He is also the Director of the Interactive Telecommunications Program at the Helsinki School of Economics, an intensive training program in cutting edge telecommunications technologies, applications and multimedia. Dr. Wallenius academic interests and published research lie in the areas of decision making and negotiation modeling.

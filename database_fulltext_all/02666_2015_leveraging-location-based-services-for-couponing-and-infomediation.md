---
otero_id: 2666
otero_key: "7ABADYGC"
title: "Leveraging location-based services for couponing and infomediation"
authors: "Xiao Zou; Ke-Wei Huang"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.05.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Leveraging location-based services for couponing and infomediation

Xiao Zou ⁎, Ke-Wei Huang

National University of Singapore, Singapore

a r t i c l e i n f o

Available online xxxx

Keywords: Location-based services Price dispersion Infomediary Coupons Economic analysis Informedness

## a b s t r a c t

Following the explosive growth of smartphone and mobile broadband networks, location-based services (LBS) have become an essential component of mobile commerce. LBS applications can assist consumers in acquiring personalized information on the spot, inducing them to make purchase decisions at nearby shops. Motivated by its unique features, we study how LBS, as a couponing channel and an infomediary, may change the way people use information for purchase decision-making. We propose a model that combines price dispersion with horizontal differentiation to investigate the impact of LBS on retail competition. Previous research on the Internet infomediary has shown that the optimal LBS adoption pattern involves one retailer choosing to join the infomediary in equilibrium. However, our results show that the optimal LBS adoption strategy is for neither or both retailers to adopt, depending on the size of the uninformed segments and reach of services. The location identi cation feature of LBS would allow the retailers to price more aggressively in order to build greater demand at the initial stage; however, this will limit the equilibrium profit level in the subsequent pricing stages. We compare the results for both an Internet infomediary and a LBS infomediary and discuss the implications of our findings for retailers' pricing, promotion and technology adoption strategies for LBS.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

As a result of the explosive growth and penetration of smartphones and tablets in recent years, more and more business activities have shifted from e-commerce on desktop computers to mobile commerce on mobile computing devices. For mobile devices, location-based services (LBS) play a significant role. LBS is broadly defined as any application, service, or campaign that incorporates the use of the geographic location of the user to deliver a service or a marketing message [15]. LBS is unique in utilizing the location information of users in real time. Thus, a large number of novel services do not have a counterpart in the traditional e-commerce world. Consumer and advertiser expenditures on LBS are expected to approach US\$ 10 billion by 2016 [21]. More and more large retail businesses, such as Starbucks, American Express, and Wal-Mart, have already actively leveraged the features of LBS to drive store traffic, increase brand awareness and interact with consumers.

This study focuses on two key features of LBS: as a new coupon delivery channel, and as a new infomediary for price and product comparison. First, although retailers have been offering paper coupons for many years, mobile platforms provide retailers with new opportunities to offer personalized coupons to potential buyers at significantly lower costs. According to market research, 47% of mobile consumers want retailers to send coupons to their mobile devices when they are in or near a store [13]. The most successful service provider to date is Foursquare, which had more than 40 million users worldwide in 2014. Users of Foursquare can earn badges as well as coupons via check-in when they visit restaurants or local stores a number of times. Following the success of Foursquare, many entertainment and novel coupon apps have emerged. For example, using CheckPoints, shoppers can use their phone's camera to scan the barcodes of certain products at participating retailers to earn prizes without being required to buy anything [24]. CheckPoints' retail partners are banking on the fact that most users will end up buying the product being scanned. Similarly, ShopKick has partnered with Target, Macy's, Simon malls and other leading retailers to provide indoor LBS couponing services. ShopKick has installed sensors in store ceilings to track users' activities in a store. Users can collect points simply by roaming around in the retail stores. As a result, the number of store walk-ins has increased 60%, and customers with ShopKick buy twice as often as non-Shopkick users [22]. According to Nielsen [1], the majority of smartphone (63%) and tablet (53%) owners search and scan to achieve savings in store aisles. These savings continue at the checkout lane, where smartphone shoppers are more likely to use their devices for mobile coupons (34%) and for making payments (23%).

The second feature of LBS is that they act as infomediaries. LBS have changed the way consumers gather price and product information. As nearly 40% of smartphone owners use their phones for in-store price comparisons, making it the top mobile shopping-related activity [14]. During the holiday season in 2011, for example, 19% of US consumers used their phone to compare products or prices in store. This success resulted from the fact that app developers brilliantly utilized various features to make search and price comparison easier than their e-commerce counterparts. With a smartphone, users can compare prices using the following input methods: type in a product name; scan a barcode or QR code on a product; speak a product's name into an app; take a picture of a product; or simply point the device's camera at the product, in the case of augmented reality apps that automatically display the product information on-screen in their devices. For example, Amazon's Price Check app provides almost all of these input methods for price comparison; Google's Shopper app can show users all the places an item is available online as well as in nearby physical stores; and Consumer Reports' Mobile Shopper app provides users not only price comparisons but also expert ratings, reviews and buying advice.

These unique features motivated us to study how the adoption of LBS apps may affect retailers' pricing strategies, profitability and market competition. On the one hand, LBS couponing apps may attract more traffic to the retailers' stores. On the other hand, price comparison apps and LBS couponing may lead to price wars among retailers in the same neighborhood, resulting in lower profit margins. It is not selfevident that the increases in sales volume will outweigh the decreases in profit margin. A game-theoretic model can help us to establish the retailers' equilibrium strategies for pricing, LBS adoption, and equilibrium profits.

In this study, we build a model that integrates the two most popular pricing models in the literature: the Hotelling pricing model for the analysis of location differentiation, and the “model of sales” for analyzing couponing strategy. We will model a retail market with two distant shopping malls, each of which has two retailers, at the two ends of a Hotelling line. On the line, there are three groups of consumers distinguished by their information heterogeneity. This assumption is the same as one that is used by Varian [23] in his “Model of Sales”. Among the three groups of consumers, two consumer segments are uninformed and only aware of the prices that one store has set. The remaining segment consists of informed, smart shoppers who know the prices of both retailers. We consider a game in which the retailers first decide whether to adopt LBS. LBS allows them to provide discount prices to consumers, and the consumers can use LBS to compare the prices of participating retailers; as a result, LBS in our model plays the role of both a new coupon delivery channel and a price comparison engine. In Stage 2, consumers will decide which mall to visit, based on the retailers' expected prices. Last, once consumers reach the mall, a proportion of them with LBS will receive additional discounted prices from participating retailers. Consumers will make final purchase decisions based on the lowest price offered to them. Our model assumes that consumers make their shopping mall choice and store choices separately, based on several strategic pricing-related variables of the retailers.

We analyze the model by considering three separate cases for the retailers' LBS adoption decisions. In each case, we solve the game by backward induction and derive the equilibrium prices for each retailer. In particular, the third stage of the store pricing game supports results similar to those seen in the existing literature on price dispersion [7,23,16]. We treat LBS as a type of price referral infomediary. In Stage 2, we incorporate the posted prices and distance between two malls into the model to capture the critical feature of LBS, the location. We then derive the optimal LBS adoption strategy based on the retailers' equilibrium profits in each of the three cases. We find that, first, the equilibrium adoption strategy of LBS is that neither retailer joins the LBS or that both retailers join the LBS, depending on the size of uninformed segment of consumers and the reach of LBS. The equilibrium for the Internet infomediary, in contrast, is that only one retailer will choose to adopt the infomediary. Essentially, the location feature of LBS is likely to intensify the price competition because retailers need to price more aggressively to compete for consumers in various segments. This will limit the profit in the subsequent pricing stage. This negative competitive effect overwhelms the positive effect due to price discrimination and the additional demand resulting from adopting LBS.

The rest of the paper is organized as follows. Section 2 reviews the related literature from economics, marketing and information systems. Section 3 introduces the model set-up. Section 4 presents the analysis of the solution and discusses the results. Section 5 concludes the paper.

## 2. Literature review

Our study is related to three streams of research. First, this study relates to the economics literature on price dispersion [20,23,5]. In these models, only a subset of consumers, called informed consumers or smart shoppers, are assumed to have access to a complete list of product prices and therefore to be able to identify the product with the lowest price. For instance, Varian [23] shows that firms tend to charge either very high prices or randomly offer different levels of discounts in a mixed strategy equilibrium. In this way, price dispersion is a price discrimination device between uninformed and informed consumers in the homogeneous goods market. The heterogeneity between these two types of consumers is also known as “informational differentiation”. In other words, firms have the options of serving only uninformed customers at a very high price or serving both informed and uninformed customers at a lower price. The seminal finding is that the equilibrium pricing strategy among competing retailers is a mixed strategy pricing equilibrium in which the retailers may randomly choose discounted prices to compete for the informed customers.

Second, by extending the solution concept of Varian [23], several marketing studies have investigated various marketing issues such as consumer loyalty, sales and promotion strategy [11,16], and referral infomediary [7]. The focal variables in these studies include the size of the loyal consumer segment [11,16], the magnitude of consumer loyalty [11,17], and the depth [18] and frequency of the promotion [18,16]. In contrast to the economic literature, these marketing studies focus more on modeling the demand-side properties as the explanations of price dispersion. Consistent with this stream of literature on price infomediary, our study models promotional price competition using the similar setup, because one role of mobile LBS promotion, similar to that of the Internet infomediary, is essentially a channel to enable consumers to become more informed about the price information from nearby retailers. One difference in our context is that consumers have access to the in-store price since they are physically in the store and, therefore, the mobile channel price must be lower than the in-store price. In contrast, e-commerce retailers can set different prices on different websites, and the customers may not be aware that they are buying at a higher price at a price comparison site. Moreover, unlike most marketing studies, we focus on information differentiation instead of brand differentiation to model the price dispersion under LBS.

Lastly, several related studies in the information systems literature have investigated the impact of the Internet referral infomediary in the context of e-commerce and e-business. For instance, Bakos [3] models the role of buyer search costs and examines the impact of electronic marketplaces on consumers' price discovery behavior. In the supply-chain setting, a study by Ghose et al. [8] finds that referral services play a critical role in enabling retailers to discriminate across consumers with different valuations. Moreover, Weber and Zheng [25] analyze the firms' bidding strategies in an intermediated search market, given consumers' equilibrium search behavior. Xu et al. [26] study online search strategy and equilibrium oligopolistic pricing. Bandyopadhyay et al. [4] have derived the mix-strategy pricing equilibrium for sellers in the context of online exchanges. Finally, Iyer and Pazgal [10] have examined the impact of Internet shopping agent on market competition and pricing. Our model is in line with these studies. To the best of our knowledge, none of the existing studies have adopted a similar type of model to investigate the impacts of LBS price promotion.

Our study can be considered as an extension of Chen et al. [7], who analyze the effect of the Internet referral infomediary on retail markets. Specifically, we extend Chen et al. [7] to model the mobile infomediary

Please cite this article as: X. Zou, K.-W. Huang, Leveraging location-based services for couponing and infomediation, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.05.007

![](/api/attachments/7ABADYGC/fulltext/images/12d5d93d18e7c7e61bdfedb9ef883fd8792add4cf62d9f5c11fa708e08a2561d.jpg)  
Fig. 1. The setting of the location market.

and couponing strategy in the last stage, when consumers have already arrived at the malls. We have extended their model by adding a secondstage Hotelling pricing game to investigate the impact of adopting LBS on the third-stage pricing and couponing strategies. More importantly, our study compares our results of the LBS infomediary with existing results on the Internet infomediary. By this comparison, we highlight the unique impacts of the LBS infomediary, relative to the e-commerce infomediary.

## 3. Model setup

We begin with the discussion of a market with duopoly retailers in two shopping malls. Next, associated assumptions on consumers are discussed. Last, we discuss the unique setup of LBS and its impact on the competition between retailers.

## 3.1. Retailers

There are two shopping malls (or shopping districts) L and R at the ends of a Hotelling line with the length normalized to 1 without loss of generality. In each mall, there are two retailer stores; our model can be generalized to a finite number of stores as in the standard “model of sales” [23]. As shown in Fig. 1, L and $L _ { 2 }$ are located in Mall L while $R _ { 1 }$ and $R _ { 2 }$ are located in Mall R. This shopping mall setup is the first main departure point from the existing literature in two ways. First, incorporating the mall location allows us to model the distinctive feature of LBS: LBS provides product or price information only in one specific shopping district. Second, it allows us to incorporate the posted price strategy of retail stores, which has been under-explored in similar models. To model retail stores, we simply need to maximize the sum of profits of $L _ { 1 }$ and $R _ { 1 } .$ . For ease of exploration, we assume that each store maximizes its store profit. In this study, we assume $L _ { 1 }$ and $R _ { 1 }$ belong to Retailer 1 and $L _ { 2 }$ and $R _ { 2 }$ belong to Retailer 2. Retail stores are risk neutral and they maximize their expected profits. For ease of exposition, the variable cost of production and fixed cost are also assumed to be zero. Our results can be generalized to a constant variable cost setup and incorporating fixed costs does not affect pricing and competition at all, as in most existing pricing studies.

## 3.2. The sequence of the game

The game in this study consists of three stages. In Stage 1, retailers decide whether to adopt LBS. Thus there are three possibilities: 1) both retailers adopt LBS; 2) only one retailer adopts LBS and 3) neither retailer adopts LBS.

In Stage 2, retail stores decide the original retail price $p ^ { c } ,$ , which will be called the posted price throughout this paper. Based on $p ^ { c }$ and the traveling cost in the Hotelling model, consumers then decide which mall to visit. This posted price can be understood as “usual price” or “regular price” and is a common practice in the retail industry. Due to price dispersion, retail stores seldom sell goods at this posted price, which serves as an upper bound on the actual level of price dispersion [9]; instead it is primarily used as a signal to attract customers to visit the shopping malls. Previous studies such as Chen and Iyer [6] have also explored the effect of similar posted price mechanisms in the context of consumer addressability, in which firms simultaneously choose posted prices and then choose pricing strategies that are contingent on the previously chosen posted prices to their addressable consumer segments. Thus, a low posted price may attract more consumers to the mall initially, but it would limit the equilibrium price and profit level in the subsequent stage. The consumer may conjecture that retail stores may offer a lower price (than posted price) following a probability distribution in-store or via LBS.

In Stage 3, each retailer has to make one or two pricing decisions, depending on whether or not they adopted LBS in Stage 1. For retailers who did not adopt LBS, only one in-store promotional price will be offered to all consumer segments. Conversely, retailers who adopted can offer one additional LBS promotional price only to consumers who own smartphones equipped with the focal LBS app. In other words, the retailer with LBS can set two prices, one in-store price and one LBS price, with price dispersion. The objective of the retail store is to maximize expected profit by setting three prices (i.e., posted price, in-store promotional price and LBS promotional price) and one LBS adoption strategy. We assume that both types of discounted prices are lower than the original price, which is consistent with the marketing practice. Consumers will choose the lowest price among the options offered to them to purchase the product. Please refer to Fig. 2 for a brief timeline of this game. Details of the utility function specification of consumers will be elaborated in the next section.

## 3.3. Consumers

The market consists of a unit mass of consumers on the Hotelling line. Consumers have identical valuation for visiting the mall and an

![](/api/attachments/7ABADYGC/fulltext/images/04a3f53b693d40aabdf76d33edbc5e09109c65b721983cdb34949842456b9d8a.jpg)  
Fig. 2. Consumer segmentation: one retailer adopts.

Please cite this article as: X. Zou, K.-W. Huang, Leveraging location-based services for couponing and infomediation, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.05.007

identical reservation price for buying the good. The identical valuation for the mall is assumed to be v. Moreover, without loss of generality, the reservation price for purchasing the good is normalized to be 1 for simplicity. The travel cost parameter in the Hotelling model is denoted by t.

Consistent with the price dispersion literature, consumers are assumed to be heterogeneous in terms of information about prices. Therefore, consumers are divided into three segments, as in the standard literature. A proportion $\beta$ of consumers have access to the price information of both retailers and will buy from the store that offers the lowest price. We call these smart shoppers “informed consumers” throughout this paper. There are two other groups of shoppers who only know and buy from one retailer. We assume that $\alpha _ { i }$ consumers are “uninformed consumers” who only buy from Retailer i $( i = 1 , 2 )$ These consumers do not know that the focal product is also available at the other retailer or do not have sufficient price information about the other retailer; hence, they will buy from the retailer about which they are informed but not from the competing retailer. This setting implies $\alpha _ { 1 } + \alpha _ { 2 } + \beta = 1$ . To simplify the following analysis, we also assume that $\alpha = \alpha _ { 1 } = \alpha _ { 2 }$ and focus on the symmetric equilibrium. This symmetric setting approach has been widely adopted by many price dispersion studies [7]. Asymmetric price dispersion models lead to qualitatively similar equilibrium solutions with much more complicated algebra.

As explained in Section 3.2, consumers have two decisions to make. First, they decide which shopping mall to visit. The choice of mall depends on two factors: the distance between the consumer and two shopping malls, and the expected original prices of the retailers within the same shopping mall. Informed and uninformed consumers will have different expected original prices. Since uninformed consumers only buy from one retailer (e.g., Retailer 1), they only compare the posted prices of $L _ { 1 }$ and $R _ { 1 } .$ . On the other hand, informed consumers would form their expectation based on the average posted prices of the two retail stores because of symmetry.

Formally, let the consumer surplus of visiting Mall j be $U _ { j } ,$ and we have

$$
U _ {j} = \left\{ \begin{array}{l} v - t x - p _ {i j} ^ {c}, \qquad \text { for   } \alpha_ {i} \text {   segment }; \\ v - t x - \frac {p _ {1 j} ^ {c} + p _ {2 j} ^ {c}}{2}, \text {   for   } \beta \text {   segment }, \end{array} \right.\tag{1}
$$

where i = 1, 2 and j = L, R. The reservation utility v for the malls is assumed to be large enough that every consumer will go to one of the two malls and the market is fully covered. As in all pricing models, consumers go to the shopping mall that gives them the higher surplus. Note that only informed consumers (β segment) make this decision based on average posted prices, while uninformed consumers (e.g., α and $\alpha _ { 2 }$ segments) will not consider average posted prices. The posted price is a key strategic pricing variable in the mall choice stage, as a low posted price may attract more consumers to the mall but it would limit the equilibrium price and profit level in Stage 3.

Once they have reached the chosen shopping mall, the second decision that consumers need to make is which retail store to visit to make their purchase. At this stage, the uninformed consumers only buy from the store about which they are informed. For example, $L _ { 1 }$ consumers will only buy from the Store $L _ { 1 } ;$ whereas the $\beta$ consumers will buy from the store that offers the lower price. Let the utility of buying from Store i in Mall j be $u _ { i j } ,$ we have

$$
u _ {i j} = \left\{ \begin{array}{l l} 1 - p _ {i j}, & \text { for   } \alpha_ {i} \text {   segment }; \\ 1 - m i n \big (p _ {1 j}, p _ {2 j} \big), & \text { for   } \beta \text {   segment }, \end{array} \right.\tag{2}
$$

where $i = 1 , 2 \mathrm { a n d } j = L , F$ . In our setting, consumers make these two decisions separately in Stages 2 and 3. Specifically, we argue that the reservation utility v for going to the mall is different from the reservation utility for purchasing the final good, which is 1 in our setup. This assumption is consistent with consumer behavior in practice, as consumers typically go to mall for more than one purpose; v N 1 because consumers also get additional benefits from other activities such as window shopping, dining, and other events in the mall. When consumers adopted LBS apps, they will receive an additional promotional price via the mobile LBS channel, which is discussed in the next section.

## 3.4. The impact of LBS

For the reach of the LBS infomediary, we follow the setup by Chen et al. [7]. We assume that there is a fraction $k ( 0 < k < 1 )$ of consumers who adopted LBS, which is exogenously given and is identical across all consumer segments. Consumers who use LBS will get additional price quotes from the retailers who adopt LBS. A consumer with price information obtained through both LBS and the retail store will choose the lowest price to make the final purchase. In other words, the introduction of LBS essentially creates another channel through which consumers may receive an additional promotional quote and also learn the complete price information from all retailers who have joined the LBS infomediary. In this way, LBS significantly alters the consumer segmentation in the market with information differentiation, as shown in Figs. 3 and 4 in the next section.

## 4. Analysis

The model is analyzed and solved by backward induction as in all other applied game theoretic models. We first analyze pricing equilibrium in Stage 3, which is similar to the standard price dispersion games of either Chen et al. [7] or Varian [23], depending on the number of retailers who adopt LBS in a specific case. Then we consider Stage 2's posted pricing game, which is similar to a Hotelling pricing model. Finally, we derive the optimal LBS adoption strategy in Stage 1 by comparing the equilibrium profits derived in the three subgames (i.e., three cases) of LBS adoption strategies.

## 4.1. Within-mall price competition game in Stage 3

In Stage 3, retailers can set in-store prices and LBS prices (if adopted) to maximize profit, and consumers choose one retail store to make the final purchase. In the analysis below, we discuss the equilibrium pricing and profit under three possible LBS adoption cases.

## 4.1.1. Case 1: neither retailer adopts LBS

When neither retailer adopts LBS, this subgame is a standard price dispersion game as in Varian [23]. The only difference is that the price cap in this price dispersion model is determined by the posted price set in Stage 2 of our model. In Stage 3, the consumers have already arrived at the shopping malls. Since the two malls are symmetric, we only need to solve the pricing game in Mall L. Let us define $D _ { L }$ as the total number of consumers who go to Mall L. Among $D _ { L } ,$ there are

<table><tr><td colspan="2"></td><td>KLBS users</td></tr><tr><td> $\alpha_{1}$  (Uninformed Customers of  $R_{1}$ )</td><td> $\alpha_{1}(1-k)$ </td><td> $\alpha_{1}k$ </td></tr><tr><td> $\beta$  (Informed Customers)</td><td> $\beta(1-k)$ </td><td> $\beta k$ </td></tr><tr><td> $\alpha_{2}$  (Uninformed Customers of  $R_{2}$ )</td><td> $\alpha_{2}(1-k)$ </td><td> $\alpha_{2}k$ </td></tr></table>

Fig. 3. Sequence of the game.

Please cite this article as: X. Zou, K.-W. Huang, Leveraging location-based services for couponing and infomediation, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.05.007

![](/api/attachments/7ABADYGC/fulltext/images/e669f371452776bf98d98fdd750f6dce74e5bdb018776d7d6d9acf28da01c943.jpg)  
Fig. 4. Consumer segmentation with LBS

three types of consumers: two uninformed groups and one informed group. Denote those consumers in Mall L (originally from two uninformed segments $\alpha _ { 1 }$ and $\alpha _ { 2 } )$ as $D _ { L 1 }$ and $D _ { L 2 } ,$ , respectively. Please bear in mind that these uninformed consumers would only buy from $L _ { 1 }$ and $L _ { 2 }$ respectively. By symmetry, we have ${ \cal D } _ { L 1 } = { \cal D } _ { L 2 } = \alpha { \cal D } _ { L }$ . Similarly, we denote the informed consumers in segment $\beta$ in Mall L as $\beta D _ { L }$ . So, $D _ { L } = 2 \alpha D _ { L } + \beta D _ { L }$ These informed consumers will buy from the retail store that offers the lower price. Retailer i in Mall L will choose price $p _ { i }$ to maximize the following profit function, given the price $p _ { j }$ from the competitor.

$$
\begin{array}{l} \pi_ {i} (p _ {i}, p _ {j}) = \underbrace {\alpha D _ {L} \times p _ {i}} _ {\text { Profit   from   Uninformed   Consumers }} \\ + \underbrace {\operatorname{prob} [ p _ {j} > p _ {i} ] \beta D _ {L p _ {i}} + \operatorname{prob} [ p _ {j} = p _ {i} ] \frac {\beta D _ {L}}{2} p _ {i}} _ {\text { Profit   from   Informed   Consumers }} \end{array}\tag{3}
$$

where $i \neq j , i \mathrm { a n d } j = L _ { 1 } , L _ { 2 } .$

Following the standard solution procedure from the price dispersion literature [23,16], we know that there is no pure-strategy Nash equilibrium. Instead, both retailers adopt mixed-strategy pricing in equilibrium. In addition, let $F _ { i } ( p )$ be the cumulative distribution function (CDF) of price and let π be the equilibrium profit for Store i, and we have the following lemma.

Lemma 1. If neither retailer adopts LBS, given the demand in Mall $D _ { L }$ and the price cap p<sub>i</sub><sup>c</sup>, the profit and the equilibrium distribution function of price are

$$
\begin{array}{l} \pi_ {i} = \alpha D _ {L} \times p _ {i} ^ {c}; \\ F _ {i} (p) = 1 - \frac {\alpha (p _ {i} ^ {c} - p)}{\beta p}, w h e r e \frac {\alpha p _ {i} ^ {c}}{\alpha + \beta} <   p <   p _ {i} ^ {c}. \end{array}\tag{4}
$$

This result is standard; similar results can be found in Narasimhan [16] and Varian [23]. One important property of the results is that the retailer's equilibrium profit only depends on the size of the uninformed segment $( \alpha D _ { L } )$ and the posted price (p<sup>c</sup>). We will use these two properties as the building blocks to derive the solution for more complicated problems in Stage 1 and Stage 2.

## 4.1.2. Case 2: both retailers adopt LBS

When both retailers adopt LBS, a proportion of the consumers (defined as the ratio k) can receive two additional LBS discounted prices on their smartphone. We now have a total of six types or segments of consumers as illustrated in Fig. 3. First, among the consumers who use LBS, we have a segment of $\beta \times k \times D _ { L }$ informed consumers who know both in-store prices and also receive two more LBS prices. These consumers can make their purchase at the lowest price among four available prices. As the LBS price is always lower than the store price, the final transaction price of these consumers will be one of the two LBS prices. Second, segments of $2 \times \alpha \times k \times D _ { L }$ consumers will also receive two LBS prices from both stores as well as also one in-store price from the store about which they were originally informed. Since the LBS prices are lower than in-store prices, consumers in this segment become perfectly informed of the price information of the two stores and will also purchase at the lower price of the two available LBS prices. In other words, this $2 \times \alpha \times k \times D _ { L }$ consumer segment would become informed consumers because of LBS. Lastly, the remaining $( 1 - k ) \times D _ { L }$ consumers who do not adopt LBS will behave the same way as in Case 1. Fig. 3 visually depicts the impact of k on consumer segmentation.

As shown in Fig. $3 , k \times D _ { L }$ consumers receive discounted prices via LBS, which leads to Bertrand price competition within the $k \times D _ { L }$ segment. Therefore, the original price competition essentially will be for a smaller market with $( 1 - k ) \times D _ { L }$ consumers who do not use LBS. The solution in this case is similar to that in Case 1; the difference lies only in the proportion of each consumer segment. As a result, we have the following lemma.

Lemma 2. If both retailers adopt LBS, given $D _ { L }$ and p<sup>c</sup>, the equilibrium profit and the distribution function of price are

$$
\begin{array}{l} \pi_ {i} = (1 - k) \times \alpha D _ {L} \times p _ {i} ^ {c}; \\ F _ {i} (p) = 1 - \frac {\alpha (p _ {i} ^ {c} - p)}{\beta p}, w h e r e \frac {\alpha p _ {i} ^ {c}}{\alpha + \beta} <   p <   p _ {i} ^ {c}. \end{array}\tag{5}
$$

Comparing the profit in Eqs. (4) and (5), we see that the profit of each store has decreased from ${ \cal D } _ { L } \mathrm { t o } ( 1 - k ) \times { \cal D } _ { L } ,$ which shows that the profit is strictly lower in the case in which both retailers use LBS, due to the reduced information differentiation. Recall that we are analyzing two retailers who carry one homogeneous product. Originally in the price dispersion models, two retailers are differentiated by the product information available to consumers in the sense that some consumers only shop at one retailer because they do not know the same product is also available at a nearby competing retailer. With LBS apps, consumers become well-informed and the differentiation among retailers disappear. The aggravated price war ignited by LBS may cannibalize the existing profit, leading to an effectively shrunk market size to $( 1 - k ) \cdot D _ { L }$ . Please also bear in mind that although LBS leads to a price war in Stage 3, it may attract more consumers to this mall in Stage 2, creating an intriguing trade-off in this model.

## 4.1.3. Case 3: only one retailer adopts LBS

The most complicated yet unique subgame in our model is the one that occurs when only one retailer adopts LBS. Without loss of generality, let Retailer 1 be the store with LBS whereas Retailer 2 does not adopt LBS in this section. Again, we analyze the pricing problem in Mall L. Let the in-store price of Retailer 1 be $p _ { L 1 }$ and the LBS price be $p _ { L 1 } ^ { L B S }$ . Similar to the previous two cases, in the three consumer segments without LBS, the equilibrium pricing strategy is mixed-strategy pricing as in Case 1.

Let $D _ { L 1 } , D _ { L 2 }$ and $D _ { L }$ be the demand for Store $L _ { 1 } , L _ { 2 }$ and Mall L. Based on the findings in Chen et al. [7], we can show that the prices offered via LBS channel will be lower than in-store prices (Chen et al., 2002, Proposition 1). As shown in Fig. 4, for $\alpha _ { 1 }$ consumers who are informed of $L _ { 1 } , k \times D _ { L 1 }$ (Area D) now will get a lower price through LBS, while $k \times D _ { L 2 }$ of segment $\alpha _ { 2 }$ (Area F) who are informed about $L _ { 2 }$ will become the new informed consumers because they now know $p _ { L 1 } ^ { L B S }$ and $p _ { L 2 } .$ In this model, Chen et al. [7] show that Retailer 1 adopts mixed pricing strategies in both in-store (Areas A, B & C) and LBS channels (Areas $D , E \& F )$ whereas Retailer 2 adopts mixed pricing strategies in only one retail channel (Chen et al., 2002, Propositions 1 and 2). Following Chen et al. [7], in equilibrium, the range of the price of retail store $L _ { 1 }$ would be $p _ { L 1 } \in ( p _ { L 1 } ^ { m } , p _ { L 1 } ^ { c } )$ and the range of the LBS price from $L _ { 1 }$ is $p _ { L 1 } ^ { L B S } \in ( p _ { L 1 } ^ { b } , p _ { L 1 } ^ { m } )$ , where $\begin{array} { r } { p _ { L 1 } ^ { m } = \frac { \alpha ( 1 - \alpha ) } { ( 1 - \alpha ) ^ { 2 } - ( 1 - 2 \alpha ) k } p _ { L 1 } ^ { c } } \end{array}$ and $p _ { L 1 } ^ { b } = \left( 1 - k \right)$ p<sup>m</sup> . We follow their setup by assuming $k < 1 - \alpha s ($ o that $p _ { L 1 } ^ { m } < p _ { L 1 } ^ { c }$ . For L (without LBS), the range of the price is $p _ { L 2 } \in ( p _ { L 2 } ^ { b } , p _ { L 2 } ^ { c } )$ , where $p _ { L 2 } ^ { b } =$ $\begin{array} { r } { \frac { ( 1 - k ) \alpha ( 1 - \alpha ) } { ( 1 - \alpha ) ^ { 2 } - ( 1 - 2 \alpha ) k } p _ { L 2 } ^ { c } . } \end{array}$ . In other words, $L _ { 1 } ,$ who uses LBS, charges two different prices in two price intervals for the two channels respectively; whereas, $L _ { 2 }$ who does not use LBS only charges regular store prices. Let $F _ { L 1 } ( p )$ $F _ { L 1 } ^ { L B S } ( p )$ , and $F _ { L _ { 2 } } ( p )$ be the cumulative distribution functions (CDF) of prices. The equilibrium pricing and profit are summarized in the following lemma.

Lemma 3. If only one retailer adopts LBS, given $D _ { L 1 } , D _ { L 2 } , D _ { L }$ and price cap $p _ { i } ^ { c } ,$ the equilibrium price distribution functions and profit are

$$
\pi_ {L 1} = (1 - k) \times D _ {L 1} \times p _ {L 1} ^ {c} + k \times p _ {L 1} ^ {b} \times D _ {L};\tag{6}
$$

$$
F _ {L 1} (p) = \frac {1 - \alpha}{1 - 2 \alpha} \left(1 - \frac {p _ {L 1} ^ {m}}{p}\right), w h e r e p _ {L 1} ^ {m} <   p <   p _ {L 1} ^ {c};
$$

$$
F _ {L 1} ^ {L B S} (p) = \frac {1}{k} \left(1 - \frac {p _ {L 1} ^ {b}}{p}\right), \quad \text { where } p _ {L 1} ^ {b} <   p <   p _ {L 1} ^ {m}.
$$

The equilibrium pricing and profit for Store $L _ { 2 }$ are

$$
\begin{array}{l} \pi_ {L 2} = (D _ {L} - D _ {L 1}) \times p _ {L 2} ^ {b}; \\ F _ {L 2} (p) = \left\{ \begin{array}{l l} 1 - \frac {\alpha (p _ {L 2} ^ {c} - p)}{\beta p}, & \text {   for   } p _ {L 2} ^ {m} <   p <   p _ {L 2} ^ {c}, \\ \frac {1}{1 - \alpha} \bigg (1 - \frac {p _ {L 2} ^ {b}}{p} \bigg), & \text {   for   } p _ {L 2} ^ {b} <   p <   p _ {L 2} ^ {m}, \end{array} \right. \end{array}\tag{7}
$$

$$
\begin{array}{l} \text { where } p _ {L 1} ^ {m} = \frac {\alpha (1 - \alpha)}{(1 - \alpha) ^ {2} - (1 - 2 \alpha) k} p _ {L 1} ^ {c}, p _ {L 1} ^ {b} = (1 - k \dot {}) p _ {L 1} ^ {m}, \text { and } p _ {L 2} ^ {m} = \frac {\alpha (1 - \alpha)}{(1 - \alpha) ^ {2} - (1 - 2 \alpha) k} \\ p _ {L 2} ^ {c}, p _ {L 2} ^ {b} = (1 - k) p _ {L 2} ^ {m}. \end{array}
$$

In the equilibrium mixed-strategy of pricing, there are two intervals of randomized pricing for each retailer. For Retailer 1, in-store price is randomized at a higher range to target the consumers who do not have LBS, whereas the LBS price is randomized at a lower range to target the consumers with LBS. Retailer 2 will optimally react by offering one randomized price accordingly. The profit function in Lemma 3 reveals simple yet intuitive insights on profitability. Specifically, for $\pi _ { L 1 } ,$ , the first term represents the profit from the regular store channel. When the store price is charged at $p _ { L 1 } ^ { c }$ , the demand that Retailer 1 get will be Area A with the size $( 1 - k ) \times D _ { L 1 }$ . Similarly, the second term represents the profit from the LBS channel; that is, Retailer 1 can get all demand from the LBS channel (Areas D, E & F) by charging the lowest possible price $p _ { L 1 } ^ { b }$ . On the other hand, Retailer 2 can get all demand, except for Retailer 1's uninformed segment (Area A) by charging the lowest price in the price range.

From Retailer 1's perspective, the trade-off of offering extra discounts via LBS includes the following effects. First, the LBS channel allows Retailer 1 to poach the other retailer's uninformed consumers (Area F in Fig. 4, which cannot be reached without LBS). A similar effect has been discussed in the paper by Chen et al. [7]. In other words, LBS can serve as a targeted advertising channel to poach the competitor's uninformed customers. The second (negative) effect is that the lowered LBS price may cannibalize the profit from Retailer 1's “loyal” customers in Area D in Fig. 4. The last effect is that the LBS price may intensify the price war between two retailers. In equilibrium, Retailer 2 may react with more aggressive pricing because consumers are better informed in the LBS market.

## 4.2. Between-mall pricing game in Stage 2

Let us now consider the effect of posted prices and shopping mall locations. In Stage 2, both retailers announce the posted price through another channel or medium (e.g., newspaper, catalog, website etc.). The posted prices are common knowledge to all consumers. The introduction of posted prices has two strategic effects. First, consumers decide which mall to visit based on the posted prices. Second, the posted price is also the price cap for the pricing dispersion game in Stage 3. The first one affects retailers' profit positively as it increases the demand, whereas the second effect adversely affects retailers' profit because the price cap inhibits retailers' flexibility in offering discounts in Stage 3. The objective of retailers is to set an intermediate and optimal posted price to maximize the store profits in Stage 2. For instance, a low posted price may attract more consumers to the mall, but it would limit the equilibrium price and profit level in Stage 3. The consumer may conjecture that stores may offer a lower price (than the posted price) following a probability distribution (e.g., CDF in Lemma 1, 2 & 3) in store or via LBS. Once the consumer enters the shopping mall in Stage 3, the consumer can know the actual prices offered, including the in-store promotion price and LBS promotion price (for LBS users).

Again, we analyze Mall L due to the symmetric setting. Based on the surplus for going to one specific mall defined in Eq. (1), we can derive the demand function of Mall L in the three consumers segments. Specif ically, denote $D _ { L 1 } , D _ { L 2 }$ and $D _ { L \beta }$ as the sizes of uninformed consumers for $\alpha _ { 1 } , \alpha _ { 2 }$ segments and β informed consumers, respectively. Similar to the demand function in standard Hotelling models, it follows that

$$
\begin{array}{l l} D _ {L 1} = \frac {\alpha}{2} + \frac {p _ {R 1} ^ {c} - p _ {L 1} ^ {c}}{2 t} & \text { in } \alpha_ {1} \text { segment. } \\ D _ {L 2} = \frac {\alpha}{2} + \frac {p _ {R 2} ^ {c} - p _ {L 2} ^ {c}}{2 t} & \text { in } \alpha_ {2} \text { segment. } \\ D _ {L \beta} = \frac {\beta}{2} + \frac {p _ {R 1} ^ {c} - p _ {L 1} ^ {c} + p _ {R 2} ^ {c} - p _ {L 2} ^ {c}}{4 t} & \text { in } \beta \text { segment. } \end{array}\tag{8}
$$

As a result, $D _ { L }$ is a function of the posted price from all stores and is denoted by

$$
D _ {L} \left(p _ {L 1} ^ {c}, p _ {L 2} ^ {c}, p _ {R 1} ^ {c}, p _ {R 2} ^ {c}\right) = D _ {L 1} + D _ {L 2} + D _ {L \beta} = \frac {1}{2} + \frac {3 \left(p _ {R 1} ^ {c} - p _ {L 1} ^ {c} + p _ {R 2} ^ {c} - p _ {L 2} ^ {c}\right)}{4 t}.\tag{9}
$$

Similar to Stage 3's subgames, we will examine three possible cases given the LBS adoption strategy of retailers in the first stage.

## 4.2.1. Case 1: neither retailer adopts LBS

Based on Lemma 1, we have derived the profit function which only depends on the total demand $D _ { L }$ and the price cap.

$$
\begin{array}{l} \pi_ {i} = \alpha D _ {L} \times p _ {i} ^ {c}, \\ \pi_ {j} = \alpha (1 - D _ {L}) \times p _ {j} ^ {c}, \end{array}
$$

where $i = L _ { 1 } , L _ { 2 } { \mathrm { a n d } } j = R _ { 1 } , R _ { 2 } .$

The stores' maximization problem is then specified as

$$
\max _ {p _ {i} ^ {c}} \pi_ {i},
$$

where $i = L _ { 1 } , L _ { 2 } , R _ { 1 } , R _ { 2 } .$

By substituting Eq. (9) into the above profit functions and taking the first-order derivative, we have a system of equations for four retail stores. As all stores are symmetric we summarize the results in the following proposition.

## Proposition 4. Equilibrium for neither adopts

If neither retailer adopts LBS, the equilibrium posted price and profit are

$$
\begin{array}{l} p _ {i} ^ {c} = \frac {2}{3} t, \\ \pi_ {i} = \frac {t \alpha}{3}, \end{array}\tag{10}
$$

where $i = L _ { 1 } , L _ { 2 }$ and $R _ { 1 } , R _ { 2 } .$

As shown in the results above, the equilibrium posted price and profit depend on the size of the uninformed segment α and the location parameter t. It is straightforward that the critical feature of LBS, the location, plays a significant role in determining the equilibrium price and profit.

As t increases, the profit of the retailer increases; this means that the more the shopping malls are differentiated or distant, the more profit each retailer will get. This is consistent with the conventional wisdom of models on location competition. Meanwhile, in order to make the posted price mechanism behave in order, $p _ { i } ^ { c }$ must be less than or equal to 1, which is the reservation prices of consumers. In other words, t needs to be relatively small. This finding explains why many LBS as infomediary mobile applications are only widely used in urban areas where shopping malls are not significantly distant from each other.

## 4.2.2. Case 2: both retailers adopt LBS

In this case, we still assume that the proportion of consumers who have adopted LBS is k. Following Lemma 2, we have

$$
\begin{array}{l} \pi_ {i} = (1 - k) \times \alpha D _ {L} \times p _ {i} ^ {c}, \\ \pi_ {j} = (1 - k) \alpha (1 - D _ {L}) \times p _ {j} ^ {c}, \end{array}
$$

where $i = L _ { 1 } ,$ , L<sub>2</sub> and $j = R _ { 1 } , R _ { 2 }$ . By the similar procedure in Case 1, essentially we solve Case 1 with a smaller market size with $( 1 - k )$ of the market size in Case 1. The equilibrium posted prices and profit are reported in the following proposition.

## Proposition 5. Equilibrium for both adopt

If both retailers adopt LBS, the equilibrium posted price and profit are

$$
\begin{array}{l} p _ {i} ^ {c} = \frac {2}{3} t, \\ \pi_ {i} = \frac {t \alpha}{3} (1 - k), \end{array}\tag{11}
$$

where $i = L _ { 1 } , L _ { 2 }$ and $R _ { 1 } , R _ { 2 } .$

Basically the posted prices are not affected, and the profit becomes strictly lower than that in Case 1. Intuitively, the introduction of LBS would decrease the profit because it intensifies price competition by reducing the differentiation between the two retailers.

## 4.2.3. Only one retailer adopts LBS

When only one retailer adopts the LBS, the solution becomes fairly complicated because of the asymmetric setting. Without loss of generality, we assume only $L _ { 1 }$ adopted LBS and $L _ { 2 }$ did not. Similar to Cases 1 and 2, substituting Eqs. (8) and (9) into the profit functions Eqs. (6) and (7), we then solve for the equilibrium pricing and profit. Results are summarized as follows.

## Proposition 6. Equilibrium for one adopts

If only Retailer 1 adopts LBS, the equilibrium posted price and profit are as follow:

$$
\begin{array}{l} p _ {i} ^ {c} = \frac {2 t \alpha \left[ (1 - \alpha) ^ {2} + k \alpha \right]}{k (3 \alpha - 1) (2 - \alpha) + 2 (1 - \alpha) ^ {2}}, \\ \pi_ {i} = \frac {t \alpha^ {2} (1 - k) \left((1 - \alpha) ^ {2} + k \alpha\right) ^ {2}}{\left[ k (3 \alpha - 1) (2 - \alpha) + 2 (1 - \alpha) ^ {2} \right] \left[ (1 - \alpha) ^ {2} - (1 - 2 \alpha) k \right]}, \end{array}\tag{12}
$$

where $i = L _ { 1 } , R _ { 1 }$

For Retailer 2 who does not adopt LBS,

$$
\begin{array}{l} p _ {j} ^ {c} = \frac {2}{3} t (1 - \alpha), \\ \pi_ {j} = \frac {\alpha t (1 - \alpha) ^ {3} (1 - k)}{3 \left[ (1 - \alpha) ^ {2} - (1 - 2 \alpha) k \right]}, \end{array}\tag{13}
$$

where $j = L _ { 2 } , R _ { 2 } .$

## 4.3. LBS adoption game in the first stage

By comparing equilibrium profits derived previously in the three possible cases, we have the following proposition for the LBS adoption strategy. Details of the proof are presented in the Appendix.

## Proposition 7. Equilibrium adoption strategy

Among all three possible adoption scenarios, the equilibrium LBS adoption strategy is summarized as follows:

1. If α $\geq { \frac { 1 } { 3 } } ,$ there are two pure strategy Nash equilibria for “Both retailers adopt” and “Neither retailer adopts”, and there is a mixed strategy between the two.

2. $\begin{array} { r } { I f \alpha < \frac { 1 } { 3 } , } \end{array}$ , the equilibrium depends on the value of k,

(a) $I f k \leq { \frac { \alpha ( 1 - \alpha ) ^ { 2 } } { ( 1 - 2 \alpha ) } }$ , there are two pure strategy Nash equilibria for “Both retailers adopt” and “Neither retailer adopts”, and there is a mixed strategy between the two.

(b) $I f \ k > \frac { \alpha ( 1 - \alpha ) ^ { 2 } } { ( 1 - 2 \alpha ) }$ , there is one pure strategy Nash equilibrium for “Neither retailer adopts”.

Overall, the above proposition reveals that the optimal LBS adoption behaves like a classic coordination problem, in which both retailers either join or do not join together. The specific optimal LBS strategy depends on the values of size of uninformed segment α and reach of LBS k. Intuitively, increasing α has a positive impact on the retailer's profit due to the increase in informational differentiation, because it implies that more consumers are uninformed and only visit one retailer, whereas increasing the reach of LBS k negatively affects the retailer's profit because it implies that more consumers become well-informed by adopting LBS and the LBS price is lower than the in-store prices. As shown in Proposition 7-1, when the informational differentiation α is large, the potential additional demand (a function of α) that can be poached from the competitor's original uninformed segment could be relatively large, which is the main benefit of adopting LBS. Therefore, “Both retailers adopt” could be a viable equilibrium strategy for both retailers, even if it is suboptimal compared to the case without LBS because of the competition effect. Moreover, when the informational differentiation α is relatively small, as long as the reach of LBS k is relatively small (Proposition 7-2a), the positive benefit from adopting LBS could offset the negative effect due to intensified price competition from the LBS channel. Thus the two retailers could still join LBS together. However, when the informational differentiation α is small and LBS reach k is high (Proposition 7-2b), the unique pure LBS strategy is “Neither retailer adopts” because the negative effect of LBS is larger than the benefit from LBS adoption.

For simplicity, we have assumed that the reach of LBS k is the same for uninformed and informed consumers. In practice, however, we would expect the informed consumers to have a much higher LBS adoption rate than the uninformed consumers. Now, let the reach of LBS for the uninformed consumer segment be k and the reach for the informed consumer segments be $k ,$ where k<sup>'</sup> N k. A graphical illustration of such a case is shown in Fig. 4, where a small proportion of Area B is not in Area E. We are interested in how a different k<sup>'</sup> may affect the results of the model.

First, it is straightforward to see that the profit of Case 1 (without LBS) remains unchanged (Proposition 4). Second, the profit for Case 2 (both LBS) also remains unchanged, because the profit is based on the size of the segment of uninformed consumers who are not using LBS, the proportion of which is still k in this setting. Lastly, for the most complicated case, Case 3, considering the profit in Proposition $6 ,$ generally we can show that the profit for Retailer 1 is an increasing function of k, whereas Retailer 2's profit is decreasing in $k . ^ { 1 }$ Intuitively, when k<sup>'</sup> increases, the value of LBS increases and Retailer 1 is better off with higher profit by extracting more demand and profit from the LBS channel, whereas Retailer 2 is worse off. If we consider the change in the payoff matrix that is illustrated in the proof of Proposition 7 in the Appendix, with k<sup>'</sup>, Profit A and B remain unchanged, and C increases while D decreases. Ultimately, as $k ^ { ' }$ increases, we would have $C > B$ and $A > D ,$ , and the equilibrium adoption would be $( A , A ) \ ( \mathrm { i . e . }$ , “Both retailers adopt”).

Generally, we show that consideration of two different values of k for informed and uninformed consumers does not significantly affect the results of equilibrium adoption, in which coordination of adoption could be optimal for both retailers. Essentially, increasing k<sup>'</sup> transfers part of the segment of informed consumers from the regular store channel (Area B) to the LBS channel (Area E) in Fig. 4, which increases the value of the LBS channel and creates a different adoption pattern dynamic.

## 4.4. Traditional infomediary vs. LBS infomediary

Consider a special case of our model to benchmark our results and highlight the unique adoption pattern. If we omit the second stage of the game, in which retailers decide posted prices to maximize their profits, we are able to re-examine the equilibrium profits and LBS strategy of the Internet infomediary by omitting the location of shopping malls. In this study, we call this Internet infomediary the “traditional infomediary” because it has prevailed with the growth of ecommerce in the past two decades. This Internet infomediary has brought benefit to consumers by reducing search cost, because consumers can use this service to research price information from retailers. Specifically, Chen et al. [7] have studied the problem by looking at the Internet referral infomediary and its impact on retail competition. We extend their study [7] by incorporating the “shopping mall” concept and the location dimension to capture the distinctive feature of LBS. In this section, we solve this special case of the traditional infomediary in our setting and compare the results with the LBS infomediary.

In this section, there is no posted price setting stage. In other words, consumers would only consider travel cost when deciding which mall to visit.<sup>2</sup> As a result, half of the consumers in each segment visit one mall. In this setting, exactly $\begin{array} { r } { \alpha + \frac { \beta } { 2 } } \end{array}$ consumers visit each mall. In one particular mall, there are<sup>α</sup> segment of uninformed consumers for $L _ { 1 }$ and $L _ { 2 } ,$ respectively and another $\frac { \beta } { 2 }$ segment of informed consumers who shop at both retailers. Hence, we have $\begin{array} { r } { D _ { L 1 } = D _ { L 2 } = \frac { \alpha } { 2 } , D _ { L \beta } = \frac { \beta } { 2 } \mathrm { { a n d } } D _ { L } = \frac { 1 } { 2 } } \end{array}$ . Note that all these values are now exogenous since we omit posted price competition. Further, the price cap for store prices will be the reservation price, which is 1 in the model. Based on the above lemmas and propositions, the equilibrium pricing is summarized in Table 1.

The result is generally consistent with Chen et al. [7]. Comparing the profits in three adoption cases, we find that the case in which only one retailer adopts the Internet infomediary yields the highest profit for both retailers. Using a similar approach, we can easily verify that the equilibrium adoption pattern is that only one retailer will join the Internet infomediary.

We can then compare the equilibrium profit of the two types of infomediary for all three adoption cases as shown in Table 2. First, it is straightforward to observe that “Neither adopts” always dominates “Both adopt” in both types of infomediary. More importantly, the dynamic of the LBS adoption decision has also changed dramatically. In particular, “Only one retailer adopts LBS” is the optimal LBS adoption strategy for the Internet infomediary, while this is not the case for the LBS infomediary. We observe a clear coordination game between retailers' adoption, and an asymmetric adoption case is never optimal.

Equilibrium solution of traditional Internet infomediary.

<table><tr><td>Case</td><td>Equilibrium profit</td><td>Equilibrium price distribution</td></tr><tr><td>Neither adopts</td><td> $\pi_{i} = \frac{\alpha}{2}$ </td><td> $F_{i} = 1 - \frac{\alpha(1-p)}{\beta p}, \frac{\alpha}{\alpha+\beta < p < 1}$ </td></tr><tr><td>Both adopt</td><td> $\pi_{i} = (1-k)\frac{\alpha}{2}$ </td><td> $F_{i} = 1 - \frac{\alpha(1-p)}{\beta p}, \frac{\alpha}{\alpha+\beta < p < 1}$ </td></tr><tr><td rowspan="2">Only 1 adopts</td><td> $\pi_{L1} = (1-k)\frac{\alpha}{2}\frac{(1-\alpha)^{2}+k\alpha}{(1-\alpha)^{2}-(1-2\alpha)k}$ </td><td> $F_{L1} = \frac{1-\alpha}{1-2\alpha}\left(1-\frac{p^{m}}{p}\right), F_{L1}^{LBS} = \frac{1}{k}\left(1-\frac{p^{b}}{p}\right)$ </td></tr><tr><td> $\pi_{L2} = (1-k)\frac{\alpha}{2}\frac{(1-\alpha)^{2}}{(1-\alpha)^{2}-(1-2\alpha)k}$ </td><td> $F_{L2} = \begin{cases} 1 - \frac{\alpha(1-p)}{\beta p}, & forp^{m} < p < p^{c} \\ \frac{1}{1-\alpha}\left(1-\frac{p^{b}}{p}\right), & forp^{b} < p < p^{m} \end{cases}$ where  $p^{m} = \frac{\alpha(1-\alpha)}{(1-\alpha)^{2}-(1-2\alpha)k}, p^{b} = (1-k) \dot{p}^{m}$ </td></tr></table>

The reason for this finding is that in the setting of the Internet infomediary, the retailer who does not use the infomediary (Retailer 2) gains a higher profit than they may obtain by joining the infomediary in the case of asymmetric adoption. In the asymmetric case of the LBS adoption game, the retailer who does not use LBS may end up with very low profit, compared to what they may obtain by joining LBS. As a consequence, that retailer may also adopt LBS because of the competition from Retailer 1, even both retailers end up with lower profits than if both of them do not adopt LBS. Moreover, from the perspective of platform pricing [19,2,12], unlike the Internet infomediary where a seller could pay a fee for platform enrollment, platform pricing may not be a viable business model in the case of the LBS infomediary.

## 5. Conclusion

In this study, we present a model on location-based service, synthesizing the price dispersion model with the Hotelling location model, and investigate the impact of LBS on retailers' pricing, profits and LBS adoption strategy. Specifically, we solve the game using backward induction in three adoption cases and derive the equilibrium profit and pricing accordingly. We analyze the equilibrium LBS adoption strategy by comparing profits in all adoption cases. Our results are used to compare against the benchmarking case of the Internet infomediary from the literature. The results show that the optimal adoption strategy in the Internet infomediary is asymmetric (i.e., only one retailer adopts the infomediary). In contrast, in the LBS adoption game, the equilibrium is similar to that of a coordination game.

## 5.1. Implications for research and practice

Our analysis provides several implications for research. First, this study addresses how LBS essentially changes the consumer segmentation. On the one hand, LBS as an additional coupon delivery channel increases retailers' ability to engage in price discrimination and attract more store traffic. On the other hand, the infomediary feature of LBS introduces intensified price competition among retailers in the same neighborhood. The interaction of the two effects reveals a unique dynamic in terms of adoption strategies, as compared to the prevailing Internet infomediary. Second, the derived equilibrium profit and pricing depend on the level of information differentiation, travel cost parameters, and the reach of the LBS. More importantly, the equilibrium adoption pattern depends on the relationships between the size of the uninformed segment and the adoption rate. Third, our analysis highlights the strategic importance of posted prices and location competition when considering shopping mall concepts.

Comparison of traditional infomediary and LBS infomediary

<table><tr><td>Case</td><td>Internet infomediary</td><td>LBS infomediary</td></tr><tr><td>Neither adopts</td><td> $\pi_{i} = \frac{\alpha}{2}$ </td><td> $\pi_{i} = \frac{t\alpha}{3}$ </td></tr><tr><td>Both adopt</td><td> $\pi_{i} = (1-k)\frac{\alpha}{2}$ </td><td> $\pi_{i} = \frac{t\alpha}{3}(1-k)$ </td></tr><tr><td rowspan="2">Only 1 adopts</td><td> $\pi_{1} = (1-k)\frac{\alpha}{2}\frac{(1-\alpha)^{2}+k\alpha}{(1-\alpha)^{2}-(1-2\alpha)k}$ </td><td> $\pi_{1} = \frac{t\alpha^{2}(1-k)\left((1-\alpha)^{2}+k\alpha\right)^{2}}{\left[k(3\alpha-1)(2-\alpha)+2(1-\alpha)^{2}\right]\left[(1-\alpha)^{2}-(1-2\alpha)k\right]}$ </td></tr><tr><td> $\pi_{2} = (1-k)\frac{\alpha}{2}\frac{(1-\alpha)^{2}}{(1-\alpha)^{2}-(1-2\alpha)k}$ </td><td> $\pi_{2} = \frac{\alpha t(1-\alpha)^{3}(1-k)}{3\left[(1-\alpha)^{2}-(1-2\alpha)k\right]}$ </td></tr></table>

The analytical results provide several implications for retailers in terms of pricing/promotion and LBS adoption strategies. First, our results can help retailers to design optimal promotional pricing strategies when LBS is adopted by themselves and/or their competitors, especially within the same shopping region. The retailer could make use of the model to understand the key strategic impact of pricing variables for pricing decisions. For example, retailers should alleviate the posted price competition by setting a higher posted price, as a low posted price may not increase overall profits because of local competition from the other retailers in the same mall. Second, our analysis provides key implications regarding LBS adoption strategy for retailers, based on the current competitive environment of stores' brand awareness and the adoption rate of LBS. For example, a prevalent adoption of LBS is only optimal when there is a small proportion of informed shoppers who know both retailers' prices or when the reach of LBS is very small. A small LBS adoption could occur in the early stage of the adoption life cycle. In practice, we see that the LBS apps could be more popular and widely adopted by fashion retailers or restaurants, as these are cases in which consumers are more locked-in to each brand due to strong consumer tastes and loyalty. Finally, because of distinct optimal adoption strategies in LBS (compared to the Internet), retailers should not apply the conventional wisdom to follow the competitors' adoption strategy of new technologies, such as LBS. Instead, retailers could assess the pay-off of different adoption scenarios based on the market conditions described above. Under certain conditions, retailers should collude not to adopt LBS to gain higher profits, because LBS triggers price war. Obviously, consumers gain the most from LBS because LBS provides them with one more channel through which to receive discounted prices as well as a new infomediary to compare prices from more retailers.

## 5.2. Limitation and future research

Several assumptions of our study can be generalized in future works. First, we assume that the reach of LBS in this model is exogenous, which could be relaxed to reflect real business scenarios. In the real world for many other applications with the feature of a two-sided advertising platform, the adoption of this new platform by retailers should be endogenized. Although we provide simple intuition when the reach of LBS is not identical across segments, researchers could rigorously model the reach of the infomediary as an endogenous variable in consumers' utility specification to generate more insights. Second, we have omitted the possible coordination strategy between retailers stores for ease of exploration. In particular, this model considers the profit maximization decision of each individual store but not the retailer for model tractability. It may be interesting to investigate an asymmetric setting in which one large retailer competes with two individual small retailers. In such a setting, we could analyze whether the large retailer may gain more than the small stores by adopting LBS. Lastly, this study can be extended by considering vertically differentiated malls. It could be interesting to examine whether the retailers located in high-end or ordinary malls have stronger incentives to adopt LBS technologies.

## Acknowledgment

The authors thank the editor, the anonymous reviewers, Dan Ma, Robert Kaufman, Byungjoon Yoo, Khim Yong Goh, Tuan Quang Phan, Jianqing Chen, the conference participants at the International Conference on Electronic Commerce 2012 for their valuable comments and suggestions. This research is partially supported by the Singapore Ministry of Education, Project Grants R-253-000-103-112.

## Appendix A. Notation and definition

Table A.3 Notation and definition.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $L_1, L_2, R_1, R_2$ </td><td>Individual retail store</td></tr><tr><td> $p_i^c$ </td><td>Posted price of store i</td></tr><tr><td> $p_i$ </td><td>In-store price of Store i</td></tr><tr><td> $p_i^{LBS}$ </td><td>LBS price of Store i</td></tr><tr><td>k</td><td>Reach of LBS</td></tr><tr><td> $D_i$ </td><td>Demand of Store i</td></tr><tr><td> $\pi_i$ </td><td>Profit if Store i</td></tr><tr><td> $\alpha, \beta$ </td><td>Size of uninformed/informed segments</td></tr><tr><td> $F_i(p), F_i^{LBS}(p)$ </td><td>CDF of in-store and LBS prices</td></tr></table>

## Appendix B. Proofs of Lemmas and Propositions

Proof of Lemma 1. In this sub-game, similar to the proofs of Propositions 2–5 in [16], we have that in this mixed-strategy equilibrium: 1) the price support for store price is continuous, and 2) neither form can have a probability mass point below 1 in its support. Since $D _ { L }$ and $p _ { i } ^ { c }$ are given in Stage 2, we directly apply the results from [16] or [23] and get the results accordingly. ■

Proof of Lemma 2. In this subgame, firms are essentially in Bertrand competition for the $\boldsymbol { k } \cdot \boldsymbol { D } _ { L }$ consumers who use LBS infomediary. As a result, the equilibrium price and profit would be 0 for this consumer segment. For the rest of the $( 1 - k ) \cdot D _ { L }$ consumers, $( 1 - k ) \times \alpha D _ { L }$ would buy from $L _ { 1 } \thinspace 0 \Gamma L _ { 2 } ,$ , and $( 1 - k ) \cdot D _ { L \beta }$ consumers would buy from the retailer offering lower price. Thus the competition is equivalent to Lemma 1 with a shrunk market. As a result, $1 - \frac { \alpha \big ( p _ { i } ^ { c } - p \big ) } { \beta p }$ and $( 1 ~ -$ $k ) \times \alpha D _ { L } \times p _ { i } ^ { c }$ are equilibrium price distribution and profit. ■

Proof of Lemma 3. The derivation follows directly from [7]. First, the price support for Retailer 1 (with LBS) and Retailer 2 is continuous with $( p _ { L 1 } ^ { b } , p _ { L 1 } ^ { m } ) \cup ( p _ { L 1 } ^ { m } , p _ { L 1 } ^ { c } )$ and $( p _ { L 2 } ^ { b } , p _ { L 2 } ^ { m } ) \cup ( p _ { L 2 } ^ { m } , p _ { L 2 } ^ { c } )$ respectively. Second, Retailer 1's profit is the sum of two expected profits from two price intervals in two channels; whereas Retailer 2's profit is resulted from two mixed-strategy pricing in a single channel. In our model, we have

$$
\begin{array}{c} \pi_ {L _ {1}} = (1 - k) D _ {L 1} p _ {L 1} + (1 - k) D _ {L \beta} (1 - F _ {L 2} (p _ {L 1})) p _ {L 1} \\ \qquad + k D _ {L 1} p _ {L 1} ^ {L B S} + k \big (D _ {L 2} + D _ {L \beta} \big) \big (1 - F _ {L 2} \big (p _ {L 1} ^ {L B S} \big) \big) p _ {L 1} ^ {L B S} \\ \pi_ {L 2} = (1 - k) D _ {L 2} p _ {L 2} + (1 - k) D _ {L \beta} (1 - F _ {L 1} (p _ {L 2})) p _ {L 2} \\ \qquad + k \big (D _ {L 2} + D _ {L \beta} \big) \Big (1 - F _ {L 1} ^ {L B S} (p _ {L 2}) \Big) p _ {L 2}. \end{array}
$$

Following Propositions 1 and 2 of [7] with the given $D _ { L \alpha } , D _ { L \beta }$ and $p _ { i } ^ { c } ,$ we can derive the equilibrium profit and price distribution. ■

Proof of Proposition 4. By substituting Eq. (9) into Eq. (4) in Lemma 1, we have

$$
\pi_ {L 1} = \alpha \left[ \frac {1}{2} + \frac {3 \left(p _ {R 1} ^ {c} - p _ {L 1} ^ {c} + p _ {R 2} ^ {c} - p _ {L 2} ^ {c}\right)}{4 t} \right] p _ {L 1} ^ {c}
$$

$$
\pi_ {R 1} = \left[ 1 - \left(\frac {1}{2} + \frac {3 \left(p _ {R 1} ^ {c} - p _ {L 1} ^ {c} + p _ {R 2} ^ {c} - \bar {p} _ {L 2} ^ {c}\right)}{4 t}\right) \right] p _ {R 1} ^ {c}
$$

$$
\pi_ {L 2} = \alpha \left[ \frac {1}{2} + \frac {3 \left(p _ {R 1} ^ {c} - p _ {L 1} ^ {c} + p _ {R 2} ^ {c} - p _ {L 2} ^ {c}\right)}{4 t} \right] p _ {L 2} ^ {c}
$$

$$
\pi_ {R 2} = \left[ 1 - \left(\frac {1}{2} + \frac {3 (p _ {R 1} ^ {c} - p _ {L 1} ^ {c} + p _ {R 2} ^ {c} - p _ {L 2} ^ {c})}{4 t}\right) \right] p _ {R 2} ^ {c}.
$$

Please cite this article as: X. Zou, K.-W. Huang, Leveraging location-based services for couponing and infomediation, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.05.007

Take First-Order-Condition and solve for four posted prices

$$
\begin{array}{l} p _ {i} ^ {c} = \frac {2}{3} t, \\ \pi_ {i} = \frac {t \alpha}{3}. \end{array}
$$

By symmetric setting, all stores should get the same price and profit. ■

Proof of Proposition 5. Substitute Eq. (9) into Eq. (5) in Lemma 2. Following the same procedures used in the proof of Proposition 4, by symmetric setting, all stores should get the same price and profit. ■

Proof of Proposition 6. Substitute Eq. (9) into Eqs. (6) and (7) in Lemma 3. Following the same procedures used in the proof of Propositions 4 and 5, by symmetric setting, all stores should get the same price and profit. ■

Proof of Proposition 7. We draw a simple payoff matrix as follows. A, B, C, and D denote the profit in Propositions 4, 5, and 6.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Retailer 2</td></tr><tr><td>Adopt</td><td>Not adopt</td></tr><tr><td rowspan="2">Retailer 1</td><td>Adopt</td><td>A, A</td><td>C, D</td></tr><tr><td>Not adopt</td><td>D, C</td><td>B, B</td></tr></table>

To identify the Nash Equilibrium, we need to compare B and C, then A and D.

First, we show that C is less then B,

$$
\begin{array}{l} C - B = \frac {t \alpha^ {2} (1 - k) \left((1 - \alpha) ^ {2} + k \alpha\right) ^ {2}}{\binom {k (3 \alpha - 1) (2 - \alpha)} {+ 2 (1 - \alpha) ^ {2}} \left[ (1 - \alpha) ^ {2} - (1 - 2 \alpha) k \right]} - \frac {t \alpha}{3} \\ = \frac {\frac {1}{3} t \alpha * \binom {(\alpha - 2) (2 \alpha - 1) (- 3 \alpha + 3 \alpha^ {2} + 1) k ^ {2}} {+ (1 4 \alpha - 1 5 \alpha^ {2} + 3 \alpha^ {3} - 4) (\alpha - 1) ^ {2} k}}{+ (3 \alpha^ {3}) k ^ {3} + (2 - 3 \alpha) (\alpha - 1) ^ {4})}{- \binom {k (3 \alpha - 1) (2 - \alpha)} {+ 2 (1 - \alpha) ^ {2}} \left[ (1 - \alpha) ^ {2} - (1 - 2 \alpha) k \right]}. \end{array}
$$

The sign of the expression depends on the numerator.

Since we know that $k < 1 \mathrm { ~ - ~ } \alpha ,$ , we determine the sign of the numerator as follows:

$$
\begin{array}{l} 3 \alpha^ {3} k ^ {3} + (\alpha - 2) (2 \alpha - 1) (- 3 \alpha + 3 \alpha^ {2} + 1) k ^ {2} \\ \qquad + (1 4 \alpha - 1 5 \alpha^ {2} + 3 \alpha^ {3} - 4) (\alpha - 1) ^ {2} k \\ \qquad + (2 - 3 \alpha) (1 - \alpha) ^ {4} \\ > 3 \alpha^ {3} k ^ {3} + (\alpha - 2) (2 \alpha - 1) (- 3 \alpha + 3 \alpha^ {2} + 1) k ^ {2} \\ \qquad + (1 4 \alpha - 1 5 \alpha^ {2} + 3 \alpha^ {3} - 4) (\alpha - 1) ^ {2} k \\ \quad + (2 - 3 \alpha) k (1 - \alpha) ^ {3} \\ = k \binom {3 \alpha^ {3} k ^ {2} + (6 \alpha^ {4} - 2 1 \alpha^ {3} + 2 3 \alpha^ {2} - 1 1 \alpha + 2) k} {+ (9 \alpha - 1 2 \alpha^ {2} + 3 \alpha^ {3} - 2) (1 - \alpha) ^ {2}} \\ > k (3 \alpha^ {3} k ^ {2} + (6 \alpha^ {4} - 2 1 \alpha^ {3} + 2 3 \alpha^ {2} - 1 1 \alpha + 2) k \\ \qquad + (9 \alpha - 1 2 \alpha^ {2} + 3 \alpha^ {3} - 2) (1 - \alpha) k) \\ = k ^ {2} \alpha^ {2} (2 - (1 - k) 3 \alpha + 3 \alpha^ {2} - 3 \alpha) \\ > k ^ {2} \alpha^ {2} (2 - 3 \alpha^ {2} + 3 \alpha^ {2} - 3 \alpha) \\ = k ^ {2} \alpha^ {2} (2 - 3 \alpha) \\ > 0. \end{array}
$$

$$
\text {   As   a   result,   } \frac {t \alpha^ {2} (1 - k) ((1 - \alpha) ^ {2} + k \alpha) ^ {2}}{(k (3 \alpha - 1) (2 - \alpha) + 2 (1 - \alpha) ^ {2}) ((1 - \alpha) ^ {2} - (1 - 2 \alpha) k)} - \frac {t \alpha}{3} <   0.
$$

Second, we compare A and D.

$$
\begin{array}{l} D - A = \frac {1}{3} \alpha t (1 - \alpha) ^ {3} \frac {1 - k}{[ (1 - \alpha) ^ {2} - (1 - 2 \alpha) k ]} - \frac {t \alpha}{3} (1 - k) \\ = \frac {1}{3} t \alpha (1 - k) \frac {(1 - 2 \alpha) k - \alpha (1 - \alpha) ^ {2}}{(1 - \alpha) ^ {2} - (1 - 2 \alpha) k}. \end{array}
$$

The sign depends on $~ ( 1 ~ - ~ 2 \alpha ) k ~ - ~ \alpha ( 1 ~ - ~ \alpha ) ^ { 2 }$ . If $k > \frac { \alpha ( 1 - \alpha ) ^ { 2 } } { ( 1 - 2 \alpha ) }$ $( 1 - 2 \alpha ) k - \alpha ( 1 - \alpha ) ^ { 2 } > 0$ and there is one pure strategy Nash equilib rium is “Neither adopts”, otherwise there are two pure-strategy Nash equilibria for “Both adopt” and “Neither adopts”, and a mixed strategy between the two.

However, we also assume that $k < 1 \mathrm { ~ - ~ } \alpha ;$ therefore $1 - \alpha =$ $\begin{array} { r } { \frac { \alpha ( 1 - \alpha ) ^ { 2 } } { ( 1 - 2 \alpha ) } \Rightarrow \alpha = \frac { 1 } { 3 } . } \end{array}$ Thus the equilibrium is summarized as:

1. If α ≥ $\begin{array} { r } { \frac { 1 } { 3 } , k < 1 - \alpha \le \frac { \alpha ( 1 - \alpha ) ^ { 2 } } { ( 1 - 2 \alpha ) } , } \end{array}$ , there are two pure strategy Nash equilibria (A,A) and (B,B), and a mixed strategy between the two.

2. If $\begin{array} { r } { \alpha < \frac { 1 } { 3 } , \frac { \alpha ( 1 - \alpha ) ^ { 2 } } { ( 1 - 2 \alpha ) } < 1 - \alpha . } \end{array}$

(a) If $k < \frac { \alpha ( 1 - \alpha ) ^ { 2 } } { ( 1 - 2 \alpha ) }$ , there are two pure strategy Nash equilibria (A,A) and (B,B), and a mixed strategy between the two.

(b) $\begin{array} { r } { \operatorname { I f } \frac { \alpha ( 1 - \alpha ) ^ { 2 } } { ( 1 - 2 \alpha ) } < k < 1 - \alpha , } \end{array}$ , there is one pure strategy Nash equilibrium (B,B). ■

## References

[1] A.C. Nielson, A Mobile Shopper's Journey: From the Couch to the Store (and Back Again), AC Nielson, 12 August 2013. Available at: http://www.nielsen.com/us/en newswire/2013/a-mobile-shoppers-journey–from-t he-couch-to-the-store–andback.html [Last accessed: 27 November 2013] (2013).

[2] M. Armstrong, Competition in two-sided markets, The RAND Journal of Economics 37 (3) (2006) 668–691.

[3] J.Y. Bakos, Reducing buyer search costs: implications for electronic marketplaces, Management Science 43 (12) (1997) 1676–1692.

[4] S. Bandyopadhyay, J.M. Barron, A.R. Chaturvedi, Competition among sellers in online exchanges, Information Systems Research 16 (1) (2005) 47–60.

[5] M.R. Baye, J. Morgan, Information gatekeepers on the internet and the competitiveness of homogeneous product markets, American Economic Review 91 (3) (2001) 454–474.

[6] Y. Chen, G. Iyer, Research note consumer addressability and customized pricing, Marketing Science 21 (2) (2002) 197–208.

[7] Y. Chen, G. Iyer, V. Padmanabhan, Referral infomediaries, Marketing Science 21 (4) (2002) 412-434

[8] A. Ghose, T. Mukhopadhyay, U. Rajan, The impact of internet referral services on a supply chain, Information Systems Research 18 (3) (2007) 300–319.

[9] A. Ghose, Y. Yao, Using transaction prices to re-examine price dispersion in electronic markets, Information Systems Research 22 (2) (2011) 269–288.

[10] G. Iyer, A. Pazgal, Internet shopping agents: virtual co-location and competition Marketing Science 22 (1) (2003) 85–106.

[11] B. Jing, Z. Wen, Finitely loyal customers, switchers, and equilibrium price promotion, Journal of Economics and Management Strategy 17 (3) (2008) 683–707.

[12] M. Lin, R. Wu, W. Zhou, Platform pricing with endogenous network effects, 2015. Available at SSRN 2426033.

[13] Loyalty 360, Customers want online shopping options, Loyalty 360, 3 June 2013. Available: http://loyalty360.org/resources/article/customers-want-onlineshopping-optio ns [Last accessed: 27 November 2013] (2013).

[14] MarketWatch, 5 top price-compare apps, MarketWatch, 23 March 2012. Available: http://www.marketwatch.com/story/5-of-the-best-price-comparison-apps-1332470 811226 [Last accessed: 27 November 2013] (2012).

[15] Mobile Marketing Association, Mobile Location Based Services Marketing Whitepaper, Tech. Rep, Mobile Marketing Association, 2011.

[16] C. Narasimhan, Competitive promotional strategies, Journal of Business 61 (4) (1988) 427-449

[17] J.S. Raju, V. Srinivasan, R. Lal, The effects of brand loyalty on competitive price promotional strategies, Management Science 36 (3) (1990) 276-304

[18] R.C. Rao, Pricing and promotions in asymmetric duopolies, Marketing Science 10 (2) (1991) 131-144

[19] J.-C. Rochet, J. Tirole, Platform competition in two-sided markets, Journal of the European Economic Association 1 (4) (2003) 990–1029.

[20] S. Salop, J. Stiglitz, Bargains and ripoffs: a model of monopolistically competitive price dispersion, The Review of Economic Studies 44 (3) (1977) 493–510.

[21] Strategy Analytics, The 10 Billion Rule: Location, Location, Location, Tech. rep, Strategy Analytics, 2011

[22] USA TODAY, Shopkick 3.0 rewards home shoppers: get ‘kicks’ with picks before hitting stores USA TODAY 25 October 2012, ILast accessed: 27 November 2013] (2012).

Please cite this article as: X. Zou, K.-W. Huang, Leveraging location-based services for couponing and infomediation, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.05.007

[23] H.R. Varian, A model of sales, The American Economic Review 70 (4) (1980) 651–659.

[24] Washington Post, Put down those coupon clippers, The Washington Post, 20 February 2011. [Last accessed: 27 November 2013] (2011).

[25] T.A. Weber, Z.E. Zheng, A model of search intermediaries and paid referrals Information Systems Research 18 (4) (2007) 414–436.

[26] L. Xu, J. Chen, A. Whinston, Oligopolistic pricing with online search, Journal of Management Information Systems 27 (3) (2010) 111–142.

![](/api/attachments/7ABADYGC/fulltext/images/56ea3102fc93f1f800105047b6616b20da33f6f848b8134bf5a9c8ad2e6db3b3.jpg)  
Xiao Zou received his Ph.D. degree in Information Systems from the School of Computing at the National University of Singapore. He is currently working as a Data Scientist in Singapore Telecommunications Limited. His research interests include economics of IT, business analytics, mobile commerce and IT service management. His work has ap peared in the leading Information Systems conferences including International Conference on Information Systems, International Conference on Electronic Commence, and Pacific Asia Conference on Information Systems.

![](/api/attachments/7ABADYGC/fulltext/images/f9bc18246c680926890d6c28897e5bbdb39b5d44620382a8b9afb82cd76204ae.jpg)

Ke-Wei Huang is an Assistant Professor at the Department of Information Systems, at the School of Computing, National University of Singapore. He got his Ph.D. degree in Information Systems from Stern School of Business at New York University. His field of specialization and research is the economics of information systems, pricing information goods, e-commerce personalization strategies, and text mining applications in finance. His works have been published in Information Systems Research, Strategic Management Journal, Production and Operations Management, Quantitative Marketing and Economics, Journal of Economics & Management Strategy, IEEE Transactions on Engineering Management, and ACM Transactions on MIS.

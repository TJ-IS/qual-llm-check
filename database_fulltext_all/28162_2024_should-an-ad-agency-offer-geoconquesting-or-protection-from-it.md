---
otero_id: 28162
otero_key: "2UASBH9S"
title: "Should an Ad Agency Offer Geoconquesting or Protection from It?"
authors: "Manmohan Aseri; Amit Mehra; Vijay Mookerjee; Hong Xu"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.0648"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Should an Ad Agency Offer Geoconquesting or Protection from It?

Manmohan Aseri,<sup>a,</sup>\* Amit Mehra,<sup>b</sup> Vijay Mookerjee,<sup>b</sup> Hong Xu<sup>c</sup>

<sup>a</sup> University of Pittsburgh, Pittsburgh, Pennsylvania 15260; <sup>b</sup> The University of Texas at Dallas, Richardson, Texas 75080; <sup>c</sup> Hong Kong University of Science and Technology (HKUST), Clear Water Bay, Hong Kong

\*Corresponding author

Contact: maseri@katz.pitt.edu, https://orcid.org/0000-0001-6943-2432 (MA); amit.mehra@utdallas.edu, https://orcid.org/0000-0002-3822-9543 (AM); vijaym@utdallas.edu, https://orcid.org/0000-0001-5583-3585 (VM); hxu@ust.hk, https://orcid.org/0000-0001-8561-0163 (HX)

Received: December 22, 202 Revised: June 1, 2022; April 4, 2023 Accepted: May 31, 2023 Published Online in Articles in Advance: July 6, 2023

https://doi.org/10.1287/isre.2021.0648

Copyright: © 2023 INFORMS

Abstract. The recent years have witnessed a tremendous increase in Internet advertising, especially location-based advertising on mobile devices. At the same time, search-driven and display advertising on more traditional media such as personal computers continues to be strong. This study examines the interaction between top-of-funnel advertising (e.g., search or display advertising) and bottom-of-funnel advertising (e.g., using a mobile application on a smart phone). We are particularly interested in the phenomenon of geoconquesting: the bottom-of-funnel advertising efforts of a firm to poach (or lure away) customers that have come to a competing firm’s physical store as a result of top-of-funnel advertising efforts by the firm. Geoconquesting efforts by a competing firm should reduce a focal firm’s incentive to invest in top-of-funnel efforts. Thus, a key challenge for an agent like Google that provides both top-of-funnel and bottom-of-funnel advertising services is to balance the inherent conflict between the two to maximize the total revenue collected from the two forms of advertising. We develop a game-theoretic model for this phenomenon. The model is from the perspective of an advertising agent that wishes to maximize the revenue earned from both kinds of advertising services, under the absence or the presence of an outside option that can be used by advertisers to obtain geoconquesting services. A key result is that sometimes the agent benefits from not offering geoconquesting, but instead promises, after collecting a fee, to protect the advertisers from poaching on each other’s search traffic. Interestingly, such a protection service becomes more lucrative for the agent when a cheaper outside option fo geoconquesting is available to the advertisers.

History: Juan Feng, Senior Editor; Zhengrui Jiang, Associate Editor.

Funding: H. Xu acknowledges the financial support from the Hong Kong Research Grants Council [Project 16504022].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.0648.

Keywords: geoconquesting • marketing funnel • digital advertising

Protection Money: Money that criminals take from people in exchange for agreeing not to hurt them or damage their property. Cambridge Dictionary

## 1. Introduction

Digital advertising has gained tremendous growth during the last decade. One unique feature of digital advertising is that it offers the possibility of targeting consumers effectively based on a wide range of factors. An example of targeting is to show search ads of a firm to those consumers who use product-specific keywords and display interest in a product sold by the firm. Another example of targeting is to show display ads of a firm on a website whose content matches with the nature of the product sold by the firm. Thus, a retailer of sports goods can show their ad on the sports pages of a newspaper website. Because consumers who visit the website are interested in that type of content, they are likely to be interested in such targeted ads as well. The targeting capabilities of digital advertising described previously are primarily used to identify consumer segments who are interested in the products sold by these firms. The purpose of advertising to these consumers is to reach consumers at the top of the purchase funnel and to raise their awareness about the firm and their products.

In recent years, capabilities to target consumers based on their location are also becoming popular. Consumer location is typically tracked using their mobile phones and such consumers can be shown ads appropriate to the location. On mobile media, location is a powerful signal of intent. Consumers’ proximity to a business’s location is an indicator of their shopping intention at the business. Such signal carried by consumers’ location is particularly important to brick-and-mortar businesses using digital advertising to convert online consumers to shop at their offline businesses. The purpose of such location-based advertising is to influence consumers at the bottom of the purchase funnel and to convert consumers to purchases.

## 1.1. Geoconquesting

One interesting approach to location-based targeting is called geoconquesting, where an advertiser targets consumers who are in a location in close proximity of their competitor’s physical sales outlet. This kind of targeting is usually combined with a discount to lure the consumers away from the competitor to the advertiser’s store. For example, Burger King used a geoconquesting strategy against McDonald’s to gain market share.<sup>1</sup> Similarly, Dunkin’ Donuts also used geoconquesting to attract additional traffic from its competitors.<sup>2</sup> Geoconquesting is very different from other marketing activities such as targeting or personalization. Using geoconquesting, firms focus only on attracting (or conquesting) the traffic of the competitor. This is very different from other marketing activities such as targeting or personalization, because in such activities, the focus of firms is on their own (or neutral) traffic, and the goal is to convert that traffic into sales. Geoconquesting is a modern method of poaching potential customers from competitors, which is made possible by innovations in information technology (IT) and real-time advertising.

Apart from this, geoconquesting is closely related to the concept of geo-fencing, with some subtle differences. If a firm tries to attract consumers in a particular geographic (virtual) fence, then it is geo-fencing. However, if the firm creates such a fence strategically around its competitor’s geographic location, then it is geoconquesting. Thus, geoconquesting is achieved by using geo-fencing in a particular way.

Previous studies have shown the effectiveness of geoconquesting on consumers’ purchase decisions. For example, Chen et al. (2017) study the consequences of mobile geo targeting in a competitive setting. Similarly, Andrews et al. (2016) examine the effects of physica crowdedness on consumer responses to mobile ads and find that mobile ads can be a welcome relief in a crowded subway environment.

In this study, we examine the interaction between targeted advertising of two kinds: (1) top-of-funnel advertising at a search engine or content website, where the purpose of advertising is to induce awareness and topof-mind recall for a firm, and (2) bottom-of-funnel advertising, specifically geoconquesting, that targets users at a physical location, near a sales outlet of the competitor to attract customers could be close to making a purchase. We consider the situation of a big digital agency like Google that offers both the traditional forms of advertising and location-based geoconquesting. Targeting users through geoconquesting may have a substantial impact on the strategy space of both the firms and the advertising agency. The availability of geoconquesting as an additional advertising channel may lock the firms in intense competition, thus reducing their profits and inducing them to lower their advertising spending. In this case, clearly, the agent would not want to offer the geoconquesting service. In contrast, the advertising agency may be able to improve its profits because firms may increase their overall advertising spending by investing in both top-of-funnel and bottomof-funnel advertising. In such a case, the agency would have the incentive to offer a geoconquesting service. In this situation, if the firms’ profits reduce, the agency may be able to further improve its profits by offering insurance to the firms to protect them from geoconquesting for a fee. The firms may be willing to pay this fee because avoiding loss of traffic to the competing firms through geoconquesting may improve their profits.

Thus, the advertising agency has a complex strategy space to consider. It can either not offer geoconquesting services, offer geoconquesting services when it can make additional profits, or introduce geoconquesting services and simultaneously offer protection from geo conquesting for a fee. It is unclear which of these three strategies will provide the highest profit for the agency because it depends on how intense the competition between firms becomes due to geoconquesting and how much price are firms willing to pay to get protection. Finally, the presence of other agencies that can offer geoconquesting is expected to change the market equilibrium because even when the focal agency does not offer geoconquesting, the other agencies would offer it. To the best of our knowledge, the interactions between top-of-funnel advertising and bottom-of-funnel geoconquesting from the perspectives of both the advertisers and the advertising agency has not been examined. Our study bridges this gap and contributes to the literature by enhancing our knowledge about the impacts of technology on advertising and consumer behaviors. We formu late a game-theoretic model to analyze the competition between two advertisers and initially consider the digital agency as a principal who anticipates the decisions of the advertisers to make decisions about its service offerings. We then extend this model to include the possibility that the advertisers have an outside option to use the services of other competing digital agencies that are smaller and hence they only offer only location-based advertising.

## 1.2. Main Insights

Our results reveal that the firms always invest in geoquesting, although such an investment reduces profits for both firms. In the meantime, the investment by the firms in geoconquesting may reduce their investment in top-of-funnel advertising. The reason is that geoconquesting lowers the effectiveness of top-of-funnel advertising: A customer acquired through top-of-funnel advertising may be lured away by the competing firm, thus reducing the value of top-of-funnel advertising. Therefore, offering geoconquesting represents a tradeoff for the advertising agency because, although its earnings increase from geoconquesting services, firms spend less on top-of-funnel advertising.

We find that because of this tradeoff, geoconquesting services may not be offered by a monopolist agency. We further find that even when the agency can improve its profits by offering geoconquesting, it may be able to improve its profits even further by offering protection to the firms from geoconquesting. The firms are willing to pay for this protection because geoconquesting is detrimental to their profits. We then extend our analysis to consider a situation where geoconquesting services are also available through small competing agencies that specialize in location-based targeting. In such a scenario, the firms can invest in top-of-funnel advertising through the focal agency and use the services of one of the smaller agencies to do geoconquesting. Because of this outside option, implementing protection from geoconquesting is harder for the focal agency because it must buy out sufficient impressions from the market to prevent the smaller agencies from offering geoconquesting. We find that even in such circumstances, the foca agency will be able to offer geoconquesting. Finally, we find that the presence of smaller geoconquesting service providers (representing competition for the focal agency) may improve the focal agency’s profit compared with the case when the agency was a monopoly provider of geoconquesting services. This can happen because the smaller agencies may charge a smaller fee for geoconquesting, thus inducing the firms to invest even more in geoconquesting, which, in turn, reduces their profits compared with the scenario when only the focal agency offers geoconquesting. Because the firms’ profits reduce even more in this case, they are willing to pay a higher protection fee and this effect may enable the focal agency to improve its profits. The provision of protection service is a theoretical idea proposed in our paper. It is not yet being practiced in the industry. Advertising agents can offer the protection service to safeguard advertising firms from the possibility of geoconquesting. Also, as our results suggest, it will not only protect the advertising firms but can also increase the advertising agent’s profit.

## 1.3. Organization of the Paper

The rest of the paper is organized as follows. In Section 2, we present a brief review of the literature on digital advertising. In Section 3, we present our model, main notation and the sequence of events in the game. In Section 4, we introduce geoconquesting and analyze it under a monopoly setting and in the presence of an outside option. Under each of these settings, we solve problems of firms and the focal agent and derive their equilibrium strategies. In Section 5, we analyze the protection service offered by the focal agent. Again, similar to the analysis of geoconquesting, we analyze the protection service both under a monopoly setting and in the presence of an outside option. In Section 6, we examine how the focal agent’s strategy of offering geoconquesting changes, when the geoconquesting can be offered by a third party or outside option. In Section $^ { 7 , }$ we extend the model to perform several robustness checks. Finally, in Section 8, we conclude with summarizing our main results and recommendations.

## 2. Literature

Digital advertising has spawned the availability of different modes of advertising. A significant body of research has studied the features of different advertising modes like search advertising (Ghose and Yang 2009, Agarwal et al. 2011, Abhishek and Hosanagar 2013, Ghose et al. 2014, Abhishek et al. 2015), display advertising (Ghose and Todri 2015, Mookerjee et al. 2017, Kumar et al. 2020), and the interplay between different advertising modes like and organic and search advertising (Yang and Ghose 2010). The research on attribution modeling shows that these modes of advertising differ in their ability to target customers at different stages of their purchase process. For example, Abhishek et al. (2015) find that display ads affect the consumers when they are at an early stage of their purchase funnel, whereas search ads play a role in converting customers throughout the purchase funnel.

With the advance of targeting technologies, it has now become possible to reach customers in a particular location. For example, Ghose et al. (2019) find that consumers who are on commuting locations are more likely to redeem mobile coupons than noncommuting consumers. Fang et al. (2014) find that the extent of discounts needed to be provided to entice consumers depends not only on their location but also on the time gap between the event and the instant when the coupon is offered.

The capability to target customers based on their location is very useful to advertisers as they can send messages to customers who are in the vicinity of the store of a competing firm. Such customers are likely to be lower funnel customers because their location shows that they are highly interested in the product or service and are ready to con vert. They may have decided to buy from the competi tor, but the advertiser can poach these customers by offering them a discount. This approach to providing location-based coupons is called geoconquesting. Fong et al. (2015) specifically analyze geoconquesting and show that this strategy becomes more effective as higher discounts are offered to consumers. Kuksov et al. (2017) show that in-store poaching through competitor advertising may benefit both firms when the firm whose customers are poached gets compensated for showing its competitors’ ads. Mehra et al. (2012) analyze poaching in the context of software upgrades and show that the competing firms are better off when switching costs between their products are lower. Fudenberg and Tirole (2000) establish that the extent of poaching depends upon the nature of contract between the firm and consumers.

The ability to target consumers at different stages of the purchase funnel raises the challenge of determining the right advertising mix that would result in optimal performance for an advertising firm. Investing in a topof-funnel advertising mode like display advertising increases awareness about the firm while investing in a lower-funnel mode like geoconquesting secures ready to convert customers through poaching for the firm. Sayedi et al. (2014) consider a similar situation where firms consider their investment decisions in traditional advertising (e.g., TV or print) for awareness and sponsored search advertising on the brand keywords of the competing firms for poaching. They find that when firms are asymmetric in terms of their advertising budget, firms with a low budget use more poaching, inducing firms with high budgets to shift budget allocation to traditional advertising. Such a shift may hurt the revenues of the search engine that enables poaching. Hence, it is in the interest of the search engine to limit the ability to poach. Our paper differs from Sayedi et al. (2014) in two ways. One, we consider that the same agency provides advertising for both awareness and poaching. Therefore, this agency does not care about shifting the budget allocation between different advertising modes. Rather, it cares only for the total amount spent by firms on advertising. This assumption captures the context where advertising for awareness can be done through digital display advertising and does not depend on traditional advertising modes like TV. Second, we consider the situation when the agency can offer firms immunity (protection) against poaching for a price. If such immunity changes the nature of competition between firms so that their profits increase, they may be willing to invest in buying such an immunity. Furthermore, they may be willing to invest more in buying the immunity than they invest in advertising. If this is the case, the agency also benefits from offering such an immunity.

To summarize, our paper is closely related to the research on how different modes of advertising affect each other. To the best of our knowledge, the interaction between the top-of-funnel advertising approaches (display and search advertising) and bottom-of-funnel advertising (location-based geoconquesting) has not been studied before. Our study is a first step to plug this gap in the literature.

## 3. Model Setup

We consider two offline firms selling substitute products to a customer mass of one. We assume that these firms are price takers and therefore charge equal prices. We normalize the prices of both firms’ products to one. An online advertising agent provides two types of advertising services to the firms: top-of-funnel advertising and geoconquesting.

## 3.1. Top-of-Funnel Advertising

Top-of-funnel advertising targets customers in their early stage of the purchase funnel and assists customers with awareness or product discovery. Examples of topof-funnel advertising include keyword advertising or display advertising. Firm $i , i \in \{ 1 , 2 \}$ , spends an amount $a _ { i }$ per customer for top of the funnel advertising. The effectiveness of firm $i ^ { \prime } \mathrm { s }$ advertising spend depends on the advertising spend by the other firm $j , j \in \{ \bar { 1 , 2 } \} , \ j \neq i .$ Larger spending by firm j reduces the market acquired by firm i. We capture this idea by modeling that firm i acquires $\begin{array} { r } { L _ { i } = \frac { a _ { i } ^ { \star } } { a _ { 1 } + a _ { 2 } } } \end{array}$ fraction of the market out of the total consumer mass of one. The advertising agent charges a fee of $\mu _ { t }$ per unit amount spent by the firms (we assume $0 \leq \mu _ { t } \leq 1 )$ ). Thus, it collects $a _ { i } \mu _ { t }$ from firm i. Consequently, firm i spends a total amount $( 1 + \mu _ { t } ) a _ { i }$ for topof-funnel advertising.<sup>3</sup> We assume that the market for top-of-funnel advertising is competitive, implying that the fee $\mu _ { t }$ is not chosen by the advertising agent but rather is an exogenously given rate that depends on the type of product or the industry of the advertising firm.

In addition to the customers who get attracted to a firm through top of the funnel advertising, there may be other customers who are unaffected by such advertising. These are the aware consumers who prefer one firm over the other. We assume that for each advertising firm there are d customers of this kind (same for both firms). Therefore, a total traffic of $L _ { i } + d$ is created for firm i.

Figure 1 illustrates how the traffic received by firms is affected by their top-of-funnel advertising spend $a _ { i } .$ . The big funnel-like triangle represents the marketing funnel. Firm i receives $L _ { i }$ fraction of top-of-funnel traffic, which is proportional to its advertising spend $a _ { i } .$ Apart from this top-offunnel traffic, firm i also receives a direct traffic of $d ,$ which brings the total bottom-of-funnel traffic received by firm i to $L _ { i } + d .$ . Next, we describe a setting where the agent offers both top-of-funnel and geoconquesting to the firms.

## 3.2. Top-of-Funnel Advertising with Geoconquesting

Geoconquesting allows firms to target customers who are near the bottom of the purchase funnel. Specifically, when a customer is in close proximity to firm i’s physical store, firm j targets this customer’s mobile device with a discount offer to make the customer switch to visit firm $j ^ { \prime } \mathrm { s }$ store. The geoconquesting advertisement can take the form of a banner ad or a pushed notification to a thirdparty mobile application opened by the customer.

To acquire customers through geoconquesting, firm i specifies the level of spend, $s _ { i } > 0$ per customer, to the agent to be spent on geoconquesting. Firm i’s geocon questing efforts will affect all customers that are near firm $j ^ { \prime } \mathbf { s }$ store and not just those that are visiting in response to firm $j ^ { \prime } \mathbf { s }$ top-of-funnel advertising. Therefore, based on the spend of $s _ { i } ,$ firm i invests $( L _ { j } + d ) s _ { i }$ in geoconquesting. In addition, to spend this budget on behalf of the firm, the agency charges a markup fee of $\mu _ { g }$ for each unit of spending, resulting in a total spend of $( L _ { j } + d ) s _ { i } ( 1 + \mu _ { g } )$ by the firm on geoconquesting.

Because of the spending on geoconquesting, firm i is able to attract some customers from firm $j .$ . We assume that the number of customers attracted by firm i is $( L _ { j } + d ) r _ { i } { \sqrt { s _ { i } } } ,$ where $s _ { i }$ is the geoconquesting spending of firm i and $r _ { i }$ is the rebate or discount offered by firm i. This formulation ensures that the geoconquested segment increases with the size of segment available for geoconquesting, the amount of rebate offered, and the amount spent for geoconquesting. To simplify expressions, we perform variable transformation by replacing s by $g _ { i } ^ { 2 }$ . Thus, firm i geoconquests $( L _ { j } + d ) g _ { i } r _ { i }$ consumers from firm j.

Figure 1. (Color online) Each Firm Receives $L _ { i }$ Fraction of Top-of-Funnel Traffic  
![](/api/attachments/2UASBH9S/fulltext/images/4916f9af0864a7059c95e4386547d706eae91ca3509c9044d0648e707bf250c2.jpg)  
Notes. This traffic is proportional to their advertising spend a . Apart from this top-of-funnel traffic $L _ { i } ,$ each firm also receive a direct traffic of d Thus, the total bottom-of-funnel traffic received by each firm is $L _ { i } { \dot { + } } d .$

Figure 2 illustrates the split of total traffic between both firms in the presence of geoconquesting. Geoconquesting enables each firm to poach the bottom-offunnel traffic received by the other firm. As the figure shows, firm 1 geoconquests (or poaches) $g _ { 1 } r _ { 1 }$ fraction of firm $2 ^ { \prime } \mathrm { s }$ bottom-of-funnel traffic $( L _ { 2 } + d )$ . Similarly, firm 2 also geoconquests $g _ { 2 } r _ { 2 }$ fraction of firm 1’s bottom-offunnel traffic $( L _ { 1 } + d )$ . This geoconquesting by both firms is represented by the cross arrows in the bottom of Figure 2. The remaining fraction of the bottom-offunnel traffic, that is, $( 1 - g _ { 2 } r _ { 2 } )$ and $( 1 - g _ { 1 } r _ { 1 } )$ , stays with the respective firms. Thus, the total number of customers received by firm 1 is

$$
(L _ {1} + d) (1 - g _ {2} r _ {2}) + (L _ {2} + d) g _ {1} r _ {1}.
$$

Similarly, the total number of customers for firm 2 is

$$
(L _ {2} + d) (1 - g _ {1} r _ {1}) + (L _ {1} + d) g _ {2} r _ {2}.
$$

In the basic model, we assume the agent is the only provider of geoconquesting services. We later relax this assumption and assume that there are some third parties or an outside option that also provides geoconquesting service. We analyze this setup because several small agencies like Cidewalk exist that provide location-based targeting services. However, such small agencies may not provide the services for advertising for awareness. The reason is that advertising for awareness is more complicated as doing it effectively requires a combination of online display advertising on websites, online video advertising on sites like YouTube, and investments on TV and print media. Therefore, only a few big agencies provide these kind of services.

## 3.3. Notation

Table 1 represents the main notation used in this paper. It is worth mentioning that $\pi _ { u } ( v ; w )$ represents the profit of player u under strategy v, when outside option is $w ,$ where $u \in \{ 1 , 2 , g \} , v \in \{ N G , G , P \}$ , and $w \in \{ o , \overline { { o } } \}$ }. Here, i and j represent two advertising firms, g represents the agent, NG represents that agent chooses not to offer geo conquesting and G represents agent’s choice of offering geoconquesting. Similarly, o represents the presence of an outside option and o represents its absence. Thus, $\pi _ { g } ( G ; \overline { { o } } )$ is the profit of the agent (g), when it offers geoconquesting (G) under no outside option (o).

## 3.4. Sequence of Events

Figure 3 depicts the sequence of events. First, the agent decides whether to offer geoconquesting or not. If the agent decides not to offer geoconquesting, then both

Figure 2. (Color online) Geoconquesting Enables Each Firm to Poach the Bottom-of-Funnel Traffic Received by the Other Firm  
![](/api/attachments/2UASBH9S/fulltext/images/2f9190b4fc4b3be4b35495dfce1b42ba72f96b3aeeafd3fad70cc8cdfcfc0e68.jpg)  
Notes. Firm 1 geoconquests (or poaches) $g _ { 1 } r _ { 1 }$ fraction of firm 2’s bottom-of-funnel traffic $( L _ { 2 } + d )$ . Similarly, firm 2 also geoconquests $g _ { 2 } r _ { 2 }$ fraction of firm 1’s bottom-of-funnel traffic $( L _ { 1 } + { \breve { d } } )$ . This geoconquesting by both firms is represented by cross arrows in the bottom. The remaining frac tion of the bottom-of-funnel traffic, i.e.. $( 1 - g _ { 2 } r _ { 2 } )$ and $( 1 \bar { - } g _ { 1 } r _ { 1 } ) .$ , stays with the firms respectively

firms only need to decide their top-of-funnel advertising spend $a _ { i } .$ On the other hand, if the agent decides to offer geoconquesting, it also chooses the geoconquesting fee $\mu _ { g } .$ . In this case, the firms also need to choose their geoconquesting spend $g _ { i }$ and rebate $r _ { i } , $ along with their top-offunnel advertising spend $a _ { i } .$ .

Table 1. Main Notation for Our Analysis

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $d$ </td><td>Direct traffic at bottom-of-funnel.</td></tr><tr><td> $i$ </td><td>Indexes for firms,  $i \in \{1, 2\}$ .</td></tr><tr><td> $g$ </td><td>Index used for the agent.</td></tr><tr><td> $a_{i}$ </td><td>Top-of-funnel (TOF) advertising spend of firm  $i$ ,  $i \in \{1, 2\}$ .</td></tr><tr><td> $L_{i}$ </td><td>Fraction of top-of-funnel market share acquired by firm  $i$ .</td></tr><tr><td> $\mu_{t}$ </td><td>Top-of-funnel fee (in terms of commission),  $0 \leq \mu_{t} \leq 1$ </td></tr><tr><td> $g_{i}$ </td><td>Advertising spend on geoconquesting by firm  $i$ .</td></tr><tr><td> $\mu_{g}$ </td><td>Geoconquesting fee charged by the agent,  $0 \leq \mu_{g} \leq 1$ .</td></tr><tr><td> $r_{i}$ </td><td>Rebate or discount offered by firm  $i$  for geoconquesting.</td></tr><tr><td> $\mu_{o}$ </td><td>Market price of geoconquesting (in terms of commission),  $0 \leq \mu_{o} \leq 1$ .</td></tr><tr><td> $G$ </td><td>Geo conquesting is offered by the agent</td></tr><tr><td> $NG$ </td><td>No geo conquesting (only TOF advertising) is offered by the agent.</td></tr><tr><td> $P$ </td><td>Protection is offered by the agent.</td></tr><tr><td> $o$ </td><td>Outside option is present.</td></tr><tr><td> $\overline{o}$ </td><td>Outside option is not present.</td></tr><tr><td> $f_{o}$ </td><td>Protection fee paid by the firm, under an outside option.</td></tr><tr><td> $f_{\overline{o}}$ </td><td>Protection fee paid by the firm, under no outside option.</td></tr><tr><td> $\pi_{u}(v;w)$ </td><td>Equilibrium profit of player  $u$  under strategy  $v$ , when outside option is  $w$ , where  $u \in \{1, 2, g\}$ ,  $v \in \{G, NG, P\}$ , and  $w \in \{o, \overline{o}\}$ .</td></tr></table>

Figure 3. Sequence of Events  
![](/api/attachments/2UASBH9S/fulltext/images/ae280d766ba522a2a85094acdc77a87763fdfaf0b0f80477b49eabc2c22af3f7.jpg)  
Notes. First the agent decides whether to offer geoconquesting or not. If the agent decides not of offer geoconquesting, then both the firms only need to decide their top-of-funnel advertising spend $a _ { i \cdot }$ On the other hand, if the agent decides to offer geoconquesting, then the firms also need to choose their geoconquesting spend $g _ { i }$ and rebate $r _ { i } ,$ along with the top-of-funnel advertising spend a .

In the next section, we now proceed to analyzing the equilibrium strategies of firms and the focal agent.

## 4. Geoconquesting

In this section, we analyze the focal agent’s decision of whether to offer geoconquesting or not. First, we analyze this problem in a monopoly setting, in which the focal agent is the only one who can possibly offer geoconquesting. Then, we examine how this decision of the focal agent changes when there is an outside option, which also provides geoconquesting.

## 4.1. Geoconquesting with Monopoly Agent

We first consider the monopoly setting. To analyze this, we solve the problem of the focal agent and firms in a backward induction manner. That is, we first solve the problem of firms and derive their optimal decisions under no geoconquesting (NG) and geoconquesting (G).

4.1.1. Firms’ Problems Under No Geoconquesting. We now proceed to analyze the problems faced by advertising firms. First, we solve firms’ problems when geoconquesting is not offered. The profit of the firms can be written as follows:

$$
\begin{array}{r} \pi_ {1} = (L _ {1} + d) - (1 + \mu_ {t}) a _ {1}, \\ \pi_ {2} = (L _ {2} + d) - (1 + \mu_ {t}) a _ {2}. \end{array}
$$

The objective of firm i is to maximize profit by choosing $a _ { i } .$ After solving, we obtain the following result.

Lemma 1. When geoconquesting is not offered by the agent, the firms’ top-of-funnel advertising spendings are

$$
a _ {1} = a _ {2} = \frac {1}{4 \mu_ {t} + 4}.
$$

The corresponding profits for firms are

$$
\pi_ {1} = \pi_ {2} = d + \frac {1}{4}.
$$

We now proceed to solve the problems of firms under geoconquesting.

4.1.2. Firms’ Problems Under Geoconquesting. We now solve the problem of firms when both top-of-funnel and geoconquesting are offered. The profit of firms can now be written as follows:

$$
\begin{array}{r l} & {\pi_ {1} = (L _ {1} + d) (1 - g _ {2} r _ {2}) + (L _ {2} + d) g _ {1} r _ {1} (1 - r _ {1})} \\ & {\qquad - (1 + \mu_ {t}) a _ {1} - (1 + \mu_ {g}) (L _ {2} + d) g _ {1} ^ {2},} \\ & {\pi_ {2} = (L _ {2} + d) (1 - g _ {1} r _ {1}) + (L _ {1} + d) g _ {2} r _ {2} (1 - r _ {2})} \\ & {\qquad - (1 + \mu_ {t}) a _ {2} - (1 + \mu_ {g}) (L _ {1} + d) g _ {2} ^ {2}.} \end{array}
$$

The objective of firm i is to maximize profit by choosing $a _ { i } , g _ { i }$ , and r<sub>i</sub>. After solving the model, we have the following result.

Lemma 2. When geoconquesting is offered, at fee $\mu _ { g \prime }$ the optimal values of a<sub>i</sub>, $g _ { i } ,$ , r<sub>i</sub> are

$$
a _ {1} = a _ {2} = \frac {6 4 \mu_ {g} + 5 9}{2 5 6 (\mu_ {t} + 1) (\mu_ {g} + 1)};
$$

$$
g _ {1} = g _ {2} = \frac {1}{8 (1 + \mu_ {g})};
$$

$$
r _ {1} = r _ {2} = \frac {1}{2}.
$$

The corresponding profits for firms are

$$
\pi_ {1} = \pi_ {2} = \frac {4 d (6 4 \mu_ {g} + 6 1) + 6 4 \mu_ {g} + 6 3}{2 5 6 (\mu_ {g} + 1)}.
$$

Comparing profits and the top-of-funnel advertising spends of firms under geoconquesting and no geocon questing (i.e., comparing the values of $\pi _ { i }$ and $a _ { i }$ with and without geoconquesting), we get the following result.

Proposition 1. Geoconquesting has the following effect on advertising firms.

(i) Geoconquesting leads to lower spend on top-of funnel advertising. That is, both firms choose lower $a _ { 1 }$ and $a _ { 2 }$ under geoconquesting compared with their values under no-geoconquesting.

(ii) Advertising firms face the prisoner’s dilemma in the presence of geoconquesting. In particular, both firms’ receive lower profit compared with their profit under no-geoconquesting.

The first result highlights the tradeoff faced by the advertising firms and the agent. The possibility of poaching customers at the bottom-of-funnel through geoconequesting reduces firms’ incentive to attract traffic through top-of-funnel advertising. This shift in advertsing spend in turn results in the agent’s tradeoff of revenue between top-of-funnel and geoconquesting. When offering geoconquesting, the agent receives additional revenue from this service but also faces reduced revenue from their topof-funnel service. This tradeoff has important implications when considering the agent’s strategy.

The second part of the previous proposition highlights that geoconquesting results in a prisoner’s dilemma; that is, the advertising firms are always worse off under geo conquesting. This is reminiscent of previous findings in literature where improvement in coupon targeting abilities of firms in a competitive setting resulted in a prison er’s dilemma (Shaffer and Zhang 1995). The reason for these results is that improvement in the ability to target consumers resulted in intensified price competition leading to a loss in profits. Despite the loss in profits, firms still invest in targeting services because even if they do not, the competing firm will do so, leaving the focal firm at a severe disadvantage and even lower profits.

We next examine the effect of geoconquesting prices on the advertising firms’ strategies. In Lemma 2, taking the derivative of $a _ { 1 } , \ \pi _ { 1 }$ with respect to $\mu _ { g } ,$ we get

$$
\begin{array}{l} \frac {d a _ {1}}{d \mu_ {g}} = \frac {5}{2 5 6 (\mu_ {g} + 1) ^ {2} (\mu_ {t} + 1)}, \\ \frac {d \pi_ {1}}{d \mu_ {g}} = \frac {1 2 a + 1}{2 5 6 (\mu_ {g} + 1) ^ {2}}. \end{array}
$$

Also, from $\begin{array} { r } { g _ { 1 } = g _ { 2 } = \frac { 1 } { 8 ( 1 + \mu _ { g } ) } } \end{array}$ in lemma 2, it is easy to see tha $g _ { 1 }$ and $g _ { 2 }$ are decreasing in $\mu _ { g } .$ Thus, we have the following result.

Proposition 2. When the geoconquesting price $( \mu _ { g } )$ increases, firms increase their top-of-funnel advertising spendings (a ), decrease their geoconquesting spendings (g ), and make higher profits.

The intuition of the previous result is as follows. As the price of geoconquesting increases, firms reduce their geoconquesting spending, and instead, rely more on their top-of-funnel advertising to attract customers to their stores. The counterintuitive part of the previous result is that the profit of advertising firms is higher when they have to pay a higher fee for geoconquesting $( \mu _ { g } )$ . This happens because a higher geoconquesting fee disincentivizes both advertising firms to do geoconquesting, which mitigates the problem of prisoner’s dilemma. On the other hand, when geoconquesting becomes more affordable $( \mu _ { g }$ is low), firms increase their geoconquesting spendings, and an increasing portion of the top-of-funnel customers are poached away by the competitor. In other words, top-of-funnel advertising becomes less effective when firms geoconquest, and hence, firms have less incentive to advertise near the top of the funnel. Thus, when the geoconquesting fee is lower, the overall profit of firms decreases because their overall traffic decreases and the geoconquesting spending increases.

We now proceed to the agent’s problem to analyze if the agent has an incentive to offer geoconquesting.

4.1.3. Agent’s Problem. The agent chooses the markup fee for geoconquesting, $\mu _ { g } ,$ to maximize profit from both advertising and geoconquesting. The objective function for the agent is as follows:

$$
\pi_ {g} = \mu_ {g} (L _ {2} + d) g _ {1} ^ {2} + \mu_ {g} (L _ {1} + d) g _ {2} ^ {2} + \mu_ {t} a _ {1} + \mu_ {t} a _ {2}.\tag{1}
$$

When $2 - 3 \mu _ { t } + 4 d ( 1 + \mu _ { t } ) < 0$ , the first derivative of $\pi _ { g }$ over $\mu _ { g }$ is strictly positive, meaning that the agent sets the price for geoconquesting to infinity, or in other words, the geoconquesting does not occur in equilibrium. In the opposite case, that is, when $2 - 3 \mu _ { t } + 4 \bar { d } ( 1 + \mu _ { t } ) > 0$ , the agent sets an optimal price $\mu _ { g } ^ { * }$

We formally state the agent’s equilibrium strategy in the following result. The equilibrium values of all variables are indicated by a \* superscript. Define $\hat { \mu } _ { g } =$ $\frac { 2 + 7 \mu _ { t } + 4 d ( 1 + \mu _ { t } ) } { 2 - 3 \mu _ { t } + 4 d ( 1 + \mu _ { t } ) } .$

Lemma 3. The equilibrium strategies of firms and the agent are characterized as follows:

(i) When $2 - 3 \mu _ { t } + 4 d ( 1 + \mu _ { t } ) < 0 ,$ , geoconquesting is not offered by the agent in equilibrium. The firms’ equilibrium investments for top-of-funnel advertising are characterized by $\begin{array} { r } { a _ { 1 } ^ { * } = a _ { 2 } ^ { * } = \frac { 1 } { 4 ( 1 + \mu _ { t } ) } } \end{array}$

<sup>t</sup>(ii) Otherwise, geoconquesting is offered by the agent in equilibrium. The agent sets price $\mu _ { g } ^ { * } = \hat { \mu } _ { g }$

Firms’ equilibrium strategies are as follows:

$$
a _ {1} ^ {*} = a _ {2} ^ {*} = \frac {4 9 2 d (1 + \mu_ {t}) + 2 4 6 + 2 7 1 \mu_ {t}}{1 0 2 4 (1 + 2 d) (1 + \mu_ {t}) ^ {2}};\tag{2}
$$

$$
g _ {1} ^ {*} = g _ {2} ^ {*} = \frac {2 - 3 \mu_ {t} + 4 d (1 + \mu_ {t})}{3 2 (1 + 2 d) (1 + \mu_ {t})};\tag{3}
$$

$$
r _ {1} ^ {*} = r _ {2} ^ {*} = \frac {1}{2}.\tag{4}
$$

Substituting the equilibrium values of the variables from the first part of the previous result in the profit functions, we derive the optimal profit for firms and the agent. Thus, the profit of the firms under no geoconquesting is

$$
\pi_ {i} ^ {*} (N G; \overline {{o}}) = \frac {1}{4} + d, \forall i \in \{1, 2 \}.
$$

The profit of the agent under no geoconquesting is

(5)

$$
\pi_ {g} ^ {*} (N G; \overline {{o}}) = \frac {\mu_ {t}}{2 (1 + \mu_ {t})}.\tag{6}
$$

Similarly, substituting the equilibrium values of the variables from part (ii) of Lemma 3 in the profit func tions, we derive the optimal profit for firms and the agent. The profit of the firms when geoconquesting is offered is

$$
\pi_ {i} ^ {*} (G; \overline {{o}}) = \frac {1}{4} + d - \frac {(1 + 1 2 d) (2 - 3 \mu_ {t} + 4 d (1 + \mu_ {t}))}{1 0 2 4 (1 + 2 d) (1 + \mu_ {t})}, \forall i \in \{1, 2 \}.\tag{7}
$$

The profit of the agent when geoconquesting is offered is

$$
\begin{array}{c} 4 + 1 6 d ^ {2} (1 + \mu_ {t}) ^ {2} + 8 d (1 + \mu_ {t}) (2 + 1 2 5 \mu_ {t}) \\ \pi_ {g} ^ {*} (G; \overline {{o}}) = \frac {+ \mu_ {t} (9 \mu_ {t} + 5 1 2 (1 + \mu_ {t}) - 1 2))}{1 0 2 4 (1 + 2 d) (1 + \mu_ {t}) ^ {2}}. \end{array}\tag{8}
$$

Next, we proceed to analyze how the service fee charged by the agent for geoconquesting services $( \mu _ { g } ^ { * } )$ depends on the top-of-funnel price, $\mu _ { t } ,$ , and the extent of the exogenous traffic available for geoconquesting (d). The marginal value of the investment in geoconquesting increases with the total traffic available for geoconquesting. This traffic has an exogenous segment that is unaffected by top-of-funnel advertising. In addition, it has an endogenous segment that depends on the firms investment in top-of-funnel advertising, which, in turn, depends on the advertising fee $\left( \mu _ { t } \right)$ for top-of-funnel advertising.

We know that $\mu _ { g } ^ { * } = \hat { \mu } _ { g } ,$ where $\begin{array} { r } { \hat { \mu } _ { g } = \frac { 2 + 7 \mu _ { t } + 4 d ( 1 + \mu _ { t } ) } { 2 - 3 \mu _ { t } + 4 d ( 1 + \mu _ { t } ) } . } \end{array}$ . Taking the derivative of $\hat { \mu } _ { g }$ with respect to $\mu _ { t } ,$ we obtain

$$
\frac {\partial \hat {\mu} _ {g}}{\partial \mu_ {t}} = \frac {4 0 d + 2 0}{[ 4 d (\mu_ {t} + 1) - 3 \mu_ {t} + 2 ] ^ {2}},
$$

which is clearly positive. Because $\begin{array} { r } { \frac { \partial \hat { \mu } _ { g } } { \partial \mu _ { t } } > 0 , } \end{array}$ the fee for geoconquesting set by the agent, that is, $\mu _ { g } ^ { * } = \hat { \mu } _ { g } ,$ , increases with the top-of-funnel fee $\mu _ { t } .$ . Thus, we note that as the price for top-of-funnel advertising increases, the agent sets a higher fee for geoconquesting. We formally note this result as a proposition.

Proposition 3. The agent sets a higher fee for geoconquesting $( \mu _ { g } ^ { * } ) _ { \mathrm { - } }$ , as the price for top-of-funnel advertising $( \mu _ { t } )$ increases.

The intuition behind the previous result is that as the fee for top-of-funnel advertising increases, the firms reduce their investment in that mode, leading to a reduction in the traffic generated through advertising. This traffic reduction makes geoconquesting less attractive for the firms because they are able to poach fewer customers with the same investment. Hence, it may appear that the agent should reduce its fee for geoconquesting to increase the incentive for the firms to invest in geoconquesting. However, we see an opposite behavior. This counterintuitive behavior appears because the agent chooses the geoconquesting fee to strike a balance between the profit from top-of-funnel and the profit from geoconquesting. Although a lower $\mu _ { g }$ increases firms’ incentives to invest in geoconquesting, it reduces firms’ incentives to invest in top-of-funnel advertising, as the customer traffic created through investment in top-of-funnel advertising can be poached by their competitors at a lower cost. Therefore, reducing $\mu _ { g }$ has an investment increasing effect for geoconquesting and an investment reducing effect for top-of-funnel advertising. The optimal value of $\mu _ { g }$ shows that the latter effect dominates and so the agent increases its geoconquesting fee to stimulate a higher top-of-funnel advertising investment by firms.

From the expressions of $\mu _ { g } ^ { * } ,$ , we obtain

$$
\frac {\partial \mu_ {g} ^ {*}}{\partial d} = - \frac {4 0 \mu_ {t} (1 + \mu_ {t})}{(2 - 3 \mu_ {t} + 4 d (1 + \mu_ {t})) ^ {2}}.
$$

It is clear that $\frac { \partial \mu _ { g } ^ { * } } { \partial d } \leq 0$ . As the direct traffic d increases, the agent sets a lower price for geoconquesting. We formally note this result as a proposition.

Proposition 4. The agent sets a lower fee for geoconquesting $( i . e . , \mu _ { g } ^ { * }$ decreases), as the direct traffic d increases.

Intuitively, as d increases, both firms have a larger number of customers near their stores. This creates an incentive for firms to increase their investment in geoconquesting. The agent can further stimulate the firms to invest in geoconquesting by reducing its geoconquesting fee. As described earlier, such a reduction would also create an incentive for the firms to reduce their top-of-funnel investments. However, in this case, the increase in investment from geoconquesting dominates the reduction in investment for top-of-funnel advertising, and so the agent responds to an increase in d by lowering its geoconquesting fee.

Taking the derivative of $\pi _ { i } ^ { * } ( G ; \overline { { o } } )$ with respect to $\mu _ { t } ,$ we get $\begin{array} { r } { \frac { \partial \pi _ { i } ^ { * } ( G ; \overline { { o } } ) } { \partial \mu _ { t } } = \frac { 5 ( 1 2 d + 1 ) } { 1 0 2 4 ( 2 d + 1 ) ( \mu _ { t } + 1 ) ^ { 2 } } } \end{array}$ : It is easy to see that $\frac { \partial \pi _ { i } ^ { * } ( G ; \overline { { o } } ) } { \partial \mu _ { t } } > 0$ . This means that the profit of advertising firms increases with the top-of-funnel fee $\mu _ { t } .$ . This is counterintuitive because firms are earning higher profits despite paying a higher top-of-funnel fee. We formally note this result here.

## Theorem 1. When geoconquesting is offered,

(i) The profits of advertising firms increase with an increase in the top-of-funnel fee $\mu _ { t }$ and the direct traffic d.

(ii) The profit of the agent decreases with an increase in the top-of-funnel fee $\mu _ { t }$ and the direct traffic d.

The intuition behind the first result is related to the result in Proposition $3 . \mathrm { A s } \mu _ { t }$ increases, the agent increases $\mu _ { g }$ (as given by Proposition 3). The increase in $\mu _ { g }$ reduces the extent of geoconquesting, which benefits the advertising firms and increases their profits. In the meantime, for the agent, a smaller direct traffic d indicates smaller market for geoconquesting. In addition, as Proposition 4 suggests, the agent will lower the geoconquesting price in response to a lower d. Although lower geoconquesting price has the positive effect of increasing the firms’ geoconquesting intensity, this is dominated by the reduction of market and reduction of profit margin, and overall lead to the profit for the agent to reduce with the amount of direct traffic d.

In this section, we saw that both the firms are worse off when the focal agent offers geoconquesting. In this situation, the focal agent can offer not to provide geoconquesting service, at some price. In the next section, we analyze such an offer, referred to as protection service, by the focal agent.

## 5. Protection from Geoconquesting

In this section, we analyze a proposal in which the agent offers to provide protection from geoconquesting. Because both firms suffer profit loss when they conduct geoconquesting, they may be willing to pay to avoid geoconquesting. Will the agent have the incentive to protect the firms from geoconquesting? The agent’s profit when it provides protection from geoconquesting consists of two components: the profit from providing top of funnel advertising services to the firms and the fee collected from the protection service. The provision of geoconquesting services reduces the benefit of the top of funnel advertising and so reduces the firms’ investment in that type of advertising. By providing protection from geoconquesting, the agent may be able to stimulate more investment by the firms in top of funnel advertising. In addition, from Section 4, we know that the profit of the firms decreases when they use geoconquesting. When the agency offers protection by withdrawing the provision of geoconquesting services to the firm’s competitor, the profits of the firms increase. Therefore, the firms will be willing to pay for the protection services. Both of these reasons indicate that such a service may increase the overall profit for the agent. The downside of offering such a service is that the agency forgoes the profits from geoconquesting services. If the net benefit to the agent is higher than the loss from not offering geoconquesting, it will have an incentive to provide such a service.

The incentive of the agent to offer a protection service may depend upon competition from other agencies that provide an alternative way for the firms to conduct geoconquesting. If other agencies (the outside option for the firms) offer geoconquesting, and the focal agent also offers geoconquesting, then the focal agent must consider the availability of the outside option for the firms. If the agent offers protection in this scenario, then the firms’ incentive to subscribe to the geoconquesting service depends upon the outside option of conducting geoconquesting.

## 5.1. Protection with Monopoly Agent

In this section, we analyze the strategies of firms and a monopolist focal agent offering protection. Specifically, we analyze whether the focal agent will provide protection services when it is the only one that offers geoconquesting services. We also analyze how the agent should be pricing this protection service, when it chooses to offer it. We denote $f _ { \overline { { o } } }$ as the fee or price that firms pay for the protection service.

5.1.1. Sequence of Events under Protection. Figure 4 depicts the sequence of events under protection service. When the agent offers the protection service, the sequence of events changes compared with that without the protection service (see Figure 3). Most importantly, we see that the option of offering protection becomes feasible only when the agent would have offered geoconquesting if offering protection was not a choice $( \mathrm { i . e . , G }$ is better than NG). This is because otherwise the threat of geoconquesting will not be credible, meaning there is nothing to protect from. The interpretation of other events in the sequence are similar to that in Figure 3.

We assume the agent determines $f _ { \overline { { o } } }$ to extract firms’ maximum willingness-to-pay for the protection service. When firms choose protection, it is equivalent to them choosing zero geoconquesting spending, and their payoff in this case is equal to that in the case of no geoconquesting, that is, $\bar { \pi } _ { i } ^ { * } ( N G ; \overline { { o } } )$ . The difference between firms’ payoff with and without geoconquesting is the maximum they are willing to pay for the protection service, that is,

$$
f _ {\overline {{o}}} = \pi_ {i} ^ {*} (N G; \overline {{o}}) - \pi_ {i} ^ {*} (G; \overline {{o}}),\tag{9}
$$

where $\pi _ { i } ^ { * } ( N G ; \overline { { o } } )$ is the profit of the firm under no geoconquesting and $\pi _ { i } ^ { * } ( G ; \bar { \overline { { o } } } )$ is the profit of the firms when geoconquesting is offered. Substituting the values of $\bar { \pi } _ { i } ^ { * } ( N G ; \bar { \overline { { o } } } )$ and $\bar { \pi } _ { i } ^ { * } ( G ; \overline { { o } } )$ from (5) and (7), we have

$$
f _ {\overline {{o}}} ^ {*} = \frac {(1 + 1 2 d) (2 - 3 \mu_ {t} + 4 d (1 + \mu_ {t}))}{1 0 2 4 (1 + 2 d) (1 + \mu_ {t})}.\tag{10}
$$

Figure 4. Sequence of Events with Protection  
![](/api/attachments/2UASBH9S/fulltext/images/290e75794d3ebcf71f9268c4267bf624b0828eebd61ed6e7d4fb65635b031bfa.jpg)  
Notes. The option of offering protection becomes feasible only when the agent would have offered geoconquesting if offering protection was not a choice (i.e., G is better than NG). This is because otherwise the threat of geoconquesting will not be credible, meaning there is nothing to protect from.

Firms cannot be worse off under protection. Therefore, the firms are always willing to pay a positive amount for the protection services. When a firm subscribes to the protection service, then the agent does not offer the geoconquesting services to the competing firm. Let the protection service offered by the agent is represented by $P .$ In an equilibrium where both the firms buy the protection services, the agent’s profit is given by the following expression:

$$
\pi_ {g} (P; \overline {{o}}) = \pi_ {g} (N G; \overline {{o}}) + 2 f _ {\overline {{o}}} ^ {*}.\tag{11}
$$

The second term comprises of the protection fee paid by both the firms to the agent. Substituting the value of $\pi _ { g } ( N G ; \overline { { o } } )$ from (6) and the value o $\mathrm { ; } f _ { \overline { { o } } }$ from (10), we have

$$
\pi_ {g} ^ {*} (P; \overline {{o}}) = \frac {4 d [ 1 2 d (\mu_ {t} + 1) + 1 2 0 \mu_ {t} + 7 ] + 2 5 3 \mu_ {t} + 2}{5 1 2 (2 d + 1) (\mu_ {t} + 1)}.\tag{12}
$$

Taking derivative with respect to $\mu _ { t } ,$ we have

$$
\frac {d \pi_ {g} ^ {*} (P ; \overline {{o}})}{d \mu_ {t}} = \frac {4 5 2 d + 2 5 1}{5 1 2 (2 d + 1) (\mu_ {t} + 1) ^ {2}}.
$$

We see that the profit of the agent from protection services increases with the top-of-funnel fee $\mu _ { t } .$ . The reason is that as $\mu _ { t }$ increases, the agent earns a higher revenue from top-of-funnel advertising.

Next, we compare the agent’s profit with and without protection and state the conditions under which the agent offers protection in the following result, that ${ \mathrm { i } } { \mathrm { s } } ,$ when $\pi _ { g } ^ { * } ( P ; \overline { { o } } ) > \pi _ { g } ^ { * } ( G ; \overline { { o } } )$

Theorem 2. Offering protection instead of geoconquesting leads to a higher profit for the agent.

Intuitively, the protection service protects firms from poaching due to geoconquesting. Thus, such protection is valid only when in the absence of protection poaching via geoconquesting will happen (otherwise, there is nothing to protect from). In other words, the threat of geoconquesting should be credible for protection to become a valid option. Thus, when offering geoconquesting is the optimal choice between offering it or not, protection becomes the valid and optimal choice. However, when geoconquesting is not better than no-geoconquesting, protection is not a valid option, because the threat of geoconquesting is not credible. Thus, no geoconquesting continues to be the optimal choice.

As the extent of traffic generated at a firm’s store increases, the incentive of the competing firm to poach this traffic through geoconquesting also increases. With an increase of investment in geoconquesting, the profits of the firms reduce. Thus, clearly, as the extent of traffic increases, the benefit of avoiding geoconquesting for the firms increases. Hence, the firms are willing to pay a higher fee for protection services. From the point of view of the agent, however, the tradeoff is between getting a higher protection fee and losing a higher amount of revenue from geoconquesting. When the firms invest in geoconquesting, the agent’s revenue is only from the service fee of enabling such investments. However, when the firms’ invest in getting protection, the entire increase in the firms’ revenue can be extracted by the monopolist agent. Therefore, with increasing traffic, the firms are more willing to pay for protection services, and the agent is also more willing to offer these services. This explains the underlying logic behind the result in Theorem 2. We also see that

$$
\frac {d f _ {\overline {{o}}} ^ {*}}{d \mu_ {t}} = - \frac {5 (1 2 d + 1)}{1 0 2 4 (2 d + 1) (\mu_ {t} + 1) ^ {2}}.
$$

Formally, we have the following result.

Proposition 5. The protection price $( f _ { \overline { { o } } } ^ { * } )$ ) decreases with the top-of-funnel fee $\mu _ { t }$ .

The intuition of the previous result is that as the fee for top-of-funnel advertising $\left( \mu _ { t } \right)$ increases, the firm attracts less traffic for geoconquesting (because it is expensive to attract traffic). Thus, the need of protection decreases, which leads to a lower price of protection $( f _ { \overline { { o } } } ^ { * } )$ . We now proceed to analyze this protection service when there are also some third-party providers (outside option) that provide geoconquesting service, other than the focal agent.

In the next section, we introduce an outside-option for providing geoconquesting services and analyze its impact on equilibrium strategies of firms and the focal agent.

## 6. Geoconquesting in the Presence of an Outside Option

In this section, we examine how the focal agent’s strategy of offering geoconquesting changes, when the geoconquesting can be offered by a third party or outside option. We consider the situation where several third party agents specializing in geoconquesting exist. These agents provide an outside option to the firms who seek geoconquesting services. We wish to analyze whether firms choose the same agent for both advertising and geoconquesting services or will they delegate the geoconquesting service to the third-party agents? Answers to these questions have practical implications for exist ing dominant agents in the top-of-funnel advertising market, such as Google, because these insights will show whether such focal agencies will be competitive when they expand to offer geoconquesting services at the bottom-of-funnel.

We assume that the third party agents offer geoconquesting services at a price $\mu _ { o } .$ . Furthermore, we also assume that the third-party agents target a different market than our focal agent, and hence $\mu _ { o }$ is exogenous in our analysis. For example, third-party agencies like

Cidewalk<sup>4</sup> make it very simple to set up geoconquesting but do not provide the whole gamut of services like a full-service agency such as Google where firms can do top-of-funnel advertising and geoconquesting. Therefore, the market served by these third-party agencies is composed of small mom-and-pop businesses who do not invest in top of funnel advertising and have a very limited expertise in setting up their advertising campaigns. The presence of such third party agents, however, creates an alternative way to do geoconquesting for bigger advertisers who invest in both types of advertising. Hence, we model the presence of such agencies as an outside option for such big advertisers.

## 6.1. Firms’ Problems

Given the prices $\mu _ { g }$ and $\mu _ { o } ,$ the advertising firms decide whether to use the services of the focal agent or one of the third-party agents for geoconquesting services. We assume that the firms always choose the agent that offers the minimum price. Thus, firms choose the foca agent if $\mu _ { g } \leq \mu _ { o } ;$ otherwise, they choose the outside option. Given this strategy of advertising firms, we now proceed to analyze the problem of the focal agent.

6.1.1. Agent’s Problem. The focal agent’s strategy in this scenario can be described as follows:

$$
\mu_ {g} ^ {*} = \left\{ \begin{array}{l} \hat {\mu} _ {g}, \quad \text { if } \mu_ {o} > \hat {\mu} _ {g} \\ \mu_ {o} - \epsilon , \text { otherwise. } \end{array} \right.\tag{13}
$$

The previous result highlights that when the price offered by the third-party agents is higher than the optimal $\hat { \mu } _ { g } ,$ , the focal agent simply stays with its optimal price and both firms choose the focal agent for geoconquesting services because its fee is lower than the thirdparty agents. When the price of the third-party agents is lower than the optimal $\hat { \mu } _ { g } ,$ then, to acquire the firms, the focal agent needs to undercut the third-party agent’s price slightly to $\mu _ { o } - \epsilon .$ . The focal agent will always choose to reduce its price below the optimal price because the alternative is to lose the geoconquesting revenue from both firms with no possible upside on the top-of-funnel advertising because firms will do geoconquesting through the third-party firms. Thus, because of competition from the third-party agent, the focal agent may be forced to offer lower geoconquesting prices. It is sufficient for the focal agent to undercut the outside option by a infinitesimally small amount. Thus, we assume that $\epsilon = 0$ for rest of the analysis. We also see that when $\mu _ { o } > \hat { \mu } _ { g } ,$ , the presence of an outside option does not affect the geoconquesting fee offered by the focal agent, that is, when $\mu _ { o } > \hat { \mu } _ { g } , \mu _ { g } ^ { * } = \hat { \mu } _ { g }$ . Thus, for the rest of the analysis, we assume that $\mu _ { o } \leq \hat { \mu } _ { g }$ to make the outside option effective.

The left figure in Figure 5 pictorially illustrates the parametric regions when geoconquesting is offered by the focal agent, in the absence of an outside option. We see that in this figure the focal agent sometimes does not offer geoconquesting, because it reduces the incentives of firms to invest in top-of-funnel advertising; thus, by not offering geoconquesting, the agent can earn more profit from the top-of-funnel. However, when an outside option is present, by not offering geoconquesting, the agent cannot influence the incentive of firms to invest in top-of-funnel, because firms will use the outside option for geoconquesting if the agent does not offer it. Thus, not offering geoconquesting will only lead to a loss of revenue from geoconquesting, without increasing the top-of-funnel revenue. Therefore, the focal agent always offers geoconquesting in this situation. The right figure in Figure 5 pictorially depicts this and shows that the focal agent always offers geoconquesting, in the presence of an outside option.

Figure 5. (Color online) Comparison of Change in Strategies for Offering Geoconquesting Before and After the Outside Option  
![](/api/attachments/2UASBH9S/fulltext/images/0bd22bdb1e406d2332f5213507071db47a0c6a0a70892849281bf229403d10c2.jpg)

In the next section, we examine whether the focal agent continues to offer protection when firms have an outside option to buy geoconquesting services.

## 6.2. Protection in the Presence of an Outside Option

We now extend the analysis to examine the effect of an outside option on the strategies of firms and the focal agent. In the presence of an outside option for geoconquesting, the advertising firms cannot avoid geoconquesting, even if the focal agent does not offer it. Thus, they are willing to pay extra for protection. Nevertheless, the firms will choose protection only if it leads to a higher net profit after subtracting the protection price.

We now analyze how the focal agent changes its strategy of offering protection service and how it prices this service. Let $f _ { o }$ represents the protection fee charged by the agent when an outside option is present.

6.2.1. Sequence of Events with Outside Option. Figure 6 depicts the sequence of events in the presence of an outside option. Compared with the sequence of events in Figure 4, we note two significant differences in this case:

i. The option of offering protection service is always available. This is in contrast to the case without outside option, when the option of offering protection was available only when geoconquesting (G) is better than no geoconquesting (NG). This is because, in the presence of an outside option, the threat of geoconquesting is always credible. If the agent does not offer geoconquesting, even then third parties are offering it.

ii. Outside option forces the agent to offer geoconquesting at $\mu _ { o } ,$ which increases the extent of geoconquesting (because $\mu _ { o } \leq \hat { \mu } _ { g } )$

If the focal agent offers protection, the price for such a service is set as the difference between firms’ payoff with and without protection; that is, the protection price is

Figure 6. Sequence of Events with Outside Option  
![](/api/attachments/2UASBH9S/fulltext/images/62468daeba0e4ef76f37b83ffca0f393acf2e07f9121488e461e0e3859c6c5bb.jpg)  
Notes. (i) The option of offering protection service is always available. This is because, in the presence of an outside option, the threat of geoconquesting is always credible. (ii) Outside option forces the agent to offer geoconquesting at $\mu _ { o } ,$ which increases the extent of geoconquesting (because $\begin{array} { r } { \bar { \mu } _ { o } \leq \hat { \mu } _ { g } ) . } \end{array}$

$$
f _ {o} = \pi_ {i} ^ {*} (N G; o) - \pi_ {i} ^ {*} (G; o).\tag{14}
$$

When the agent offers protection, it ensures that the firm does not suffer from geoconquesting, and the firm’s profit is same as that in the absence of geoconquesting (even in the presence of an outside option). Thus, the profit of the firm without geoconquesting does not change with the entry of an outside option. Thus, $\pi _ { i } ^ { * } ( N G ; o )$ stays same as that in (5). Therefore,

$$
\pi_ {i} ^ {*} (N G; o) = \frac {1}{4} + d, \forall i \in \{1, 2 \}.\tag{15}
$$

Conversely, the profit of the firm under geoconquesting now changes with the entry of an outside option (because the optimal value of $\mu _ { g } ^ { * }$ changes). Substituting the value of $\mu _ { g } ^ { * }$ in (1), we have

$$
\pi_ {i} ^ {*} (G; o) = \frac {4 d (6 4 \mu_ {o} + 6 1) + 6 4 \mu_ {o} + 6 3}{2 5 6 (\mu_ {o} + 1)}.\tag{16}
$$

Substituting the values of $\pi _ { i } ( N G ; o )$ and $\pi _ { i } ( G ; o )$ from (15) and (16), respectively, in (14), we get

$$
f _ {o} ^ {*} = \frac {1 2 d + 1}{2 5 6 (\mu_ {o} + 1)}.\tag{17}
$$

Interestingly, the protection price does not depend on the top-of-funnel fee $\mu _ { t } .$ . This is in direct contrast with the result in Proposition $5 ,$ in which the protection price (in the absence of outside option) decreases with $\mu _ { t } .$ The reason is that the protection price depends on the level of threat given by the agent to firms (in terms of the loss of revenue due to geoconquesting) to make firms buy the protection service. In the absence of an outside option, this level of threat is totally controlled by the agent (by controlling the geoconquesting fee $\mu _ { g } )$ . In the absence of an outside option, this threat level decreases with an increase in top-of-funnel fee $\mu _ { t } ,$ because firms do not attract enough traffic from top-of-funnel for geoconquesting, which consequently leads to a decrease in the protection price that the agent can charge. However, with the entry of a competitive outside option things change: The focal agent can no longer control the level of threat because the threat level is decided by the outside option.

We also see that in $( 1 7 ) , f _ { o }$ increases with a decrease in $\mu _ { o } ,$ when $\mu _ { o } \leq \hat { \mu } _ { g } .$ . In other words, as the outside option becomes more competitive (a decrease in $\mu _ { o } ) _ { . }$ , the protection fee increases because of the increased level of threat. We now proceed with obtaining the profit of the agent, when it offers protection service, in the presence of an outside option.

The profit of the agent can be written as

$$
\pi_ {g} (P; o) = \pi_ {g} (N G; o) + 2 f _ {o}.\tag{18}
$$

Substituting the value of $\mathrm { \dot { \rho } }$ from (17), we get

$$
\pi_ {g} ^ {*} (P; o) = \frac {1 2 d + 1}{1 2 8 (\mu_ {o} + 1)} + \frac {\mu_ {t}}{2 \mu_ {t} + 2}.\tag{19}
$$

![](/api/attachments/2UASBH9S/fulltext/images/75d3d7005be6f1a939f21284bf18a2be69c4aa3ef98ab86e622c40560bd1f20a.jpg)  
Figure 7. (Color online) Comparison of Change in Strategies for Offering Protection Before and After the Outside Option

Taking the derivative of $\pi _ { g } ^ { * } ( P ; \overline { { o } } )$ with respect to $\mu _ { o } ,$ we get

$$
\frac {d \pi_ {g} ^ {*} (P ; \overline {{o}})}{d \mu_ {o}} = - \frac {1 2 d + 1}{1 2 8 (\mu_ {o} + 1) ^ {2}}.\tag{20}
$$

Interestingly, the profit from offering protection decreases with $\mu _ { o } .$ In other words, a more competitive outside option leads to a higher profit from offering protection.

The reason is that a lower value of $\mu _ { o }$ makes geoconquesting cheap and therefore increases the need of protection. We now proceed to analyze the impact of an outside option on the agent’s profit.

## 6.3. Impact of Outside Options on Agent

Thus far, we analyzed the impact of the strength of outside option on the profitability of offering the protection service. We now analyze the overall impact of the outside option on the profit of the agent. From Theorem 2, we know that offering protection is a superior choice compared with offering geoconquesting. Thus, the agent will always offer protection instead of geoconquesting. Also, whenever not offering geoconquesting is better than offering it, protection cannot be offered (because it is not a credible threat). The left figure in Figure 7 depicts the strategies of the agent before (or in the absence of) outside option. Comparing this left subfigure with the left figure in Figure 5, we see that protection is optimal in the region where geoconquesting was optimal. The right figure of Figure 7 depicts that in the presence of an outside option, protection will always be offered. This happens because the outside option will always offer geoconquesting, even if the agent chooses not to offer geoconquesting. Thus, offering protection is always feasible and turns out to be the optimal choice always.

There is a small difference between the protection offered before and after the outside option: In the absence of the outside option, the agent can offer protection from a potential geoconquesting level corresponding to $\mu _ { g } ^ { * } =$ $\hat { \mu } _ { g } .$ . However, in the presence of an outside option, the agent can offer protection from a potential geoconquesting level corresponding to $\boldsymbol { \mu } _ { g } ^ { * } = \boldsymbol { \mu } _ { o }$ . Because $\mu _ { o } \leq \hat { \mu } _ { g } ,$ the level of potential geoconquesting in the presence of an outside option is much higher. Thus, the threat of geocon questing and the need of protection from it are also higher in the presence of an outside option.

To compare the profit of the agent before and after the outside option, we need the following two comparisons: (i) $\pi _ { g } ^ { * } ( \bar { P } ; o ) \geq \pi _ { g } ^ { * } ( N G ; \overline { { o } } )$ and (ii) $\pi _ { g } ^ { * } ( { \tilde { P } } ; o ) \geq \pi _ { g } ^ { * } ( { \tilde { P } } ; { \overline { { o } } } )$ We find that both these conditions are true in all para metric regions. Thus, we have the following result.

Theorem 3. The agent continues to offer protection in the presence of an outside option. Moreover, the profit of th agent increases due to the presence of an outside option.

The intuition of the previous result is as follows:

1. $\pi _ { g } ^ { * } ( P ; o ) \geq \pi _ { g } ^ { * } ( N G ; \overline { { o } } )$ : The intuition behind this result is that the presence of an outside option makes the threat of geoconquesting credible. Specifically, in the absence of an outside option, when it is not optimal for the agent to offer geoconquesting, the agent cannot even consider offering protection, because such an offer of protection from geoconquesting will not be credible (because offering geoconquesting is not optimal). However, the entry of an outside option makes the threat of geoconquesting credible, leading to protection becoming a feasible option.

2. $\pi _ { g } ^ { * } ( P ; o ) \geq \pi _ { g } ^ { * } ( P ; \overline { { o } } )$ : The intuition is that a more competitive outside option $( \mu _ { o } \leq \hat { \mu } _ { g } )$ allows the agent to charge a higher protection price, and, therefore, enables it to earn a higher profit.

In Theorem 3, we established that an outside option increases the profit of the agent. Now we analyze how this increase in profit is affected by the level of competition and other parameters. Let $\Delta \pi _ { o }$ represent the increase in profit of the agent due to the entry of an outside option. Then, we have

$$
\frac {d \Delta \pi_ {o}}{d \mu_ {o}} = - \frac {1 2 d + 1}{1 2 8 (\mu_ {o} + 1) ^ {2}}.\tag{21}
$$

From the previous equation, we see that the increase in the agent’s profit decreases with $\mu _ { o } .$ It means that a more competitive outside option (low $\mu _ { o } )$ leads to a higher increase in the profit of the agent.

Proposition 6. The increase in the agent’s profit due to the entry of an outside option is higher when the outside option is very attractive $( \mu _ { o }$ is low).

The intuition of the previous result is tied to the fact that a more competitive outside option (low $\mu _ { o } )$ increases the need of protection from geoconquesting, thus making the protection service more profitable.

In the next section, we test the robustness of our results by extending the model to include additional features.

## 7. Extensions

We now test the robustness of our main results by extending our model to incorporate some additional features. Specifically, add the following features: (i) protection with opportunity cost, (ii) privacy-sensitive consumers and unequal effect of geoconquesting on direct and top-of-funnel traffic, and (iii) both advertising firms charge different prices for their products. Apart from these additional features, we also analyze the impact of no geoconquesting, geoconquesting, and protection on social welfare.

## 7.1. Protection with Opportunity Cost

Offering protection instead of geoconquesting can be considered a lost opportunity to earn revenue from geoconquesting. To ensure that the third-party agents (or the outside option) cannot offer geoconquesting services when the focal agent offers protection, the focal agent must ensure that advertising opportunities with geolocation information in the geographical areas relevant to the clients of the focal agency should not become available. In the absence of this geolocation information, it would not be possible for the third party agents to offer geoconquesting services to the clients served by the focal agent. The focal agent owns the advertising exchange where any agent can purchase ad impressions. Therefore, the focal agent can strip off the geolocation information from ad impression opportunities that may be relevant to its own clients, thus enforcing protection. However, the ad impression opportunities are less valuable once they are stripped off their geolocation information and hence the focal agent suffers a loss in revenues from such ad-impression opportunities.

Based on this discussion, we write the profit expression of the focal agent as follows:

$$
\begin{array}{r} \pi_ {g} (P; o) = \pi_ {g} (N G; o) + 2 f _ {o} - e (L _ {2} + d) (g _ {1}) ^ {2} \\ - e (L _ {1} + d) (g _ {2}) ^ {2}. \end{array}\tag{22}
$$

In the previous expression, the parameter e helps capture the net cost to the focal agency in providing geoconquesting services. We assume that $\bar { 0 } \leq e \leq 1$ , which implies that stripping off the geolocation information makes these ad impressions less valuable in the market. As e increases, the loss of revenue due to lack of geolocation information is higher. $\mathrm { A t } \ e = 1$ , the impressions lose all the value. Comparing the profit of the agent with and without an outside option, we get the following result. Define $\hat { e } = \operatorname* { m i n } \{ \hat { e } _ { N G } , \ \hat { e } _ { P } \}$ , where $\begin{array} { r } { \hat { e } _ { P } = \frac { - ( 1 2 d + 1 ) ( \mu _ { o } ^ { - } + 1 ) ( 4 d ( \mu _ { o } - 1 ) ( \mu _ { t } + 1 ) + \mu _ { o } ( 2 - 3 \mu _ { t } ) - 7 \mu _ { t } - 2 ) } { 8 ( 2 d + 1 ) ^ { 2 } ( \mu _ { t } + 1 ) } } \end{array}$ and $\hat { e } _ { N G } =$ $\textstyle { \frac { 1 2 d \mu _ { o } + 1 2 d + \mu _ { o } + 1 } { 4 d + 2 } } .$

Proposition 7. The entry of an outside option increases the profit of the agent, when the opportunity cost (e) is low, that $i s , e \le \hat { e }$

The previous result establishes that the entry of an outside option continues to benefit the agent as long as the opportunity cost e is low, that i $\mathrm { s } , e \leq \hat { e } . \mathrm { A l s o } .$ , we have $\hat { e } = \hat { e } _ { N G }$ when the agent does not offer geoconquesting in the absence of an outside option. Similarly, $\hat { e } = \hat { e } _ { P }$ when the agent offers protection in the absence of an outside option.

Figure 8 pictorially depicts how the profit-enhancing region for the agent shrinks as the opportunity cost (e) increases. In particular, when both top-of-funnel fee (µ ) and direct traffic (d) are low, the outside option no longer enhances the profit of the agent. The reason behind this is that the profit from protection service has two components: (i) the profit from top-of-funnel advertising and (ii) profit from protection at bottom-of-funnel. When the top-of-funnel fee $\mu _ { t }$ is low, the agent’s profit from top-of-funnel advertising is low. Similarly, when the direct traffic d is low, the agent is unable to charge a high enough protection price. Thus, the profit from bottom-of-funnel protection is also low.

Interestingly, we see that even when the opportunity cost is at its maximum $( \mathrm { i . e . , } e = 1 )$ , we have some parametric region where the outside option increases the agent’s profit. This is because the absence of geoconquesting has several indirect benefits for the agent. First, it incentivizes the advertising firms to invest more in top-of-funnel advertising. Second, it allows the agent to extract additional surplus from the advertising firms. These indirect benefits of not offering geoconquesting may exceed the direct benefit of offering geoconquesting (i.e., revenue from it).

Figure 8. (Color online) As the Opportunity Cost (e) Increases, the Region, Where the Outside Option Leads to Higher Profits, Shrinks  
![](/api/attachments/2UASBH9S/fulltext/images/551594538639b751da84a6087d31f42e9fc250230e708372383082d3bf3d8155.jpg)

![](/api/attachments/2UASBH9S/fulltext/images/6548e767a5e7a1897f00d4376def74ec2622756c3c28c386b7f27e4e934bdf4e.jpg)

![](/api/attachments/2UASBH9S/fulltext/images/f74477e437289d99a92d0508a15f1c393948618e9dd5c514b4ea6429021f59c3.jpg)

## 7.2. Privacy Sensitive Consumers and Unequa Effect of Geoconquesting on Direct and Top-of-Funnel Traffic

Some consumers are privacy sensitive, and therefore, they might turn off location tracking on their mobile devices. These privacy sensitive consumers are not available for geoconquesting. We now extend our model of Section 4 and assume that a $\beta$ fraction of consumers turn off location tracking on their mobiles and are unavailable for geoconquesting. Apart from this, in our model, we did not distinguish between the direct traffic and the topof-funnel traffic, in terms of the effectiveness of geoconquesting. Specifically, we assumed that geoconquesting equally affects both direct and top-of-funnel traffic. However, the direct traffic might be inherently different from top-of-funnel traffic. This traffic might be more loyal to the firm, or these customers might be located physically closer to the store. Thus, we now consider a situation in which geoconquesting is less effective on the direct customers. We model this by assuming that only α fraction of direct consumers are affected by geoconquesting. Thus, the profits of the firms can now be written as follows:

$$
\begin{array}{r} \pi_ {1} = \beta [ (L _ {1} + \alpha d) (1 - g _ {2} r _ {2}) + (1 - \alpha) d + (L _ {2} + \alpha d) \\ g _ {1} r _ {1} (1 - r _ {1}) - (1 + \mu_ {g}) (L _ {2} + d) g _ {1} ^ {2} ] - (1 + \mu_ {t}) a _ {1}, \\ \pi_ {2} = \beta [ (L _ {2} + \alpha d) (1 - g _ {1} r _ {1}) + (1 - \alpha) d + (L _ {1} + \alpha d) \\ g _ {2} r _ {2} (1 - r _ {2}) - (1 + \mu_ {g}) (L _ {1} + d) g _ {2} ^ {2} ] - (1 + \mu_ {t}) a _ {2}. \end{array}
$$

In the expression of $\pi _ { 1 } ,$ only $\beta$ fraction of consumers is available for geoconquesting. Thus, the traffic via geoconquesting and its cost are multiplied by $\beta .$ Because the cost of top-of-funnel advertising is unaffected by this, this cost $( \mathrm { i . e . , } ( 1 + \mu _ { t } ) a _ { 1 } )$ is not multiplied by β. Similarly, the first term inside bracket in $\pi _ { 1 }$ indicates that only $L _ { 1 } + \alpha d$ traffic is available for geoconquesting by firm 2, because geoconquesting works only on the α fraction of consumers. Thus, $( 1 - \alpha ) d$ traffic (the second term) remains unaffected by geoconquesting of firm 2. Although only an α fraction of direct traffic gets affected by geoconquesting, the firms exert geoconquesting effort on the entire direct traffic d (only α fraction responds). Thus, the cost paid by firm 1 for geoconquesting remains the same as that in the base model of Section 4, that is, $( 1 + \mu _ { g } ) ( L _ { 2 } + d ) g _ { 1 } ^ { 2 } ,$ , which is the last term inside bracket in the expression of $\pi _ { 1 }$

7.2.1. Firms’ Problem Under Geoconquesting. Solving for $\begin{array} { r } { \frac { \partial \pi _ { 1 } } { \partial a _ { 1 } } = \frac { \partial \pi _ { 1 } } { \partial g _ { 1 } } = \frac { \partial \pi _ { 1 } } { \partial r _ { 1 } } = 0 } \end{array}$ , we get

$$
a _ {1} ^ {*} =
$$

$$
\frac {\beta [ 4 d (d (\alpha - 6) \alpha + 6 4 d (\mu_ {g} + 1) - 2 \alpha + 6 4 \mu_ {g} + 6 1) + 6 4 \mu_ {g} + 5 9 ]}{2 5 6 (2 d + 1) ^ {2} (\mu_ {g} + 1) (\mu_ {t} + 1)},\tag{23}
$$

$$
g _ {1} ^ {*} = \frac {2 d \alpha + 1}{1 6 d \mu_ {g} + 1 6 d + 8 \mu_ {g} + 8},\tag{24}
$$

$$
r _ {1} ^ {*} = \frac {1}{2}.\tag{25}
$$

The proof of the negative semidefinite-ness of Hessian matrix of $\pi _ { 1 }$ is in the online appendix (in the proof of Proposition 8).

Let $\pi _ { i } ^ { * } ( G ; \overline { { o } } )$ represent the profit of the firm i under geoconquesting, then we have

$$
\begin{array}{c} \pi_ {i} ^ {*} (G; \overline {{o}}) = \beta \left(d + \frac {1}{4}\right) - \frac {(2 d \alpha + 1) (2 d (1 2 d + 7) \alpha + 1) \beta}{2 5 6 (2 d + 1) ^ {2} (\mu_ {g} + 1)}, \\ i \in 1, 2. \end{array} \tag {2}\tag{26}
$$

7.2.2. Firms’ Problem Under No Geoconquesting. When geoconquesting is not offered, the strategies of adveritising firms stay the same as that in Lemma 3. Thus, in

this case,

$$
a _ {i} ^ {*} = \frac {\beta}{4 (1 + \mu_ {t})}, i \in 1, 2.
$$

Let $\pi _ { i } ^ { * } ( N G ; \overline { { o } } )$ represent the profit of the firm i under no geonconquesting, then we have

$$
\pi_ {i} ^ {*} (N G; \overline {{o}}) = \beta \left(d + \frac {1}{4}\right), i \in 1, 2.\tag{27}
$$

Comparing the profits of firm 1 with and without geoconquesting, that is, comparing (26) and (27), it is easy to see that

$$
\pi_ {i} ^ {*} (G; \overline {{o}}) \leq \pi_ {i} ^ {*} (N G; \overline {{o}}).\tag{28}
$$

7.2.3. Agent’s Problem. The profit function of the agent remains as that in Section 4:

$$
\pi_ {g} = \beta \mu_ {g} (L _ {2} + d) g _ {1} ^ {2} + \beta \mu_ {g} (L _ {1} + d) g _ {2} ^ {2} + \mu_ {t} a _ {1} + \mu_ {t} a _ {2}.\tag{29}
$$

When geoconquesting is not offered, the profit of the agent can be obtained by substituting $\begin{array} { r } { a _ { 1 } = a _ { 2 } = \frac { \beta } { 4 ( 1 + \mu _ { t } ) } . } \end{array}$ Thus, we get

$$
\pi_ {g} ^ {*} (N G; \overline {{o}}) = \frac {\beta \mu_ {t}}{2 \mu_ {t} + 2}.\tag{30}
$$

Similarly, when geoconquesting is offered, we get the profit of the agent by substituting the optimal strategies of firms under geoconquesting, that is, $a _ { i } ^ { * } , \ g _ { i } ^ { * }$ and $r _ { i } ^ { * } .$ Thus, we have

$$
\pi_ {g} ^ {*} (G; \overline {{o}}) = \frac {\beta [ U _ {1} + 2 (2 d + 1) \mu_ {g} (2 d \alpha + 1) ^ {2} ]}{1 2 8 (2 d + 1) ^ {2} (\mu_ {g} + 1) ^ {2}},\tag{31}
$$

where $\begin{array} { r } { U _ { 1 } = \frac { ( \mu _ { g } + 1 ) \mu _ { t } ( 4 d ( d ( \alpha - 6 ) \alpha + 6 4 d ( \mu _ { g } + 1 ) - 2 \alpha + 6 4 \mu _ { g } + 6 1 ) + 6 4 \mu _ { g } + 5 9 ) } { \mu \ + 1 } . } \end{array}$ <sup>t</sup>When the agent offers geoconquesting, the first-order µt⁺ condition of $\pi _ { g } ^ { * } ( G ; \overline { { o } } )$ with respect to $\mu _ { g }$ leads to the following solution:

$$
\mu_ {g} ^ {*} = \frac {2 d \mu_ {t} (4 d \alpha + \alpha + 8) + 4 d (2 d \alpha + \alpha + 1) + 7 \mu_ {t} + 2}{2 a (\alpha (4 d (\mu_ {t} + 1) + 3 \mu_ {t} + 2) - 4 \mu_ {t} + 2) - 3 \mu_ {t} + 2}.\tag{32}
$$

The proof of concavity of $\pi _ { g } ^ { * } ( G ; \overline { { o } } )$ is in the online appendix. We also need $\mu _ { g } ^ { * } > 0 $ , which is true when the denominator of $\mu _ { g } ^ { * }$ is positive. Thus, we need

$$
2 a (\alpha (4 d (\mu_ {t} + 1) + 3 \mu_ {t} + 2) - 4 \mu_ {t} + 2) - 3 \mu_ {t} + 2 > 0.
$$

Under this condition, it is easy to establish that $\pi _ { g } ^ { * } ( G ) \geq$ $\pi _ { g } ^ { * } ( N G )$ .

7.2.4. Protection Fee. From (28), we know that $\pi _ { i } ^ { * } ( G ; \overline { { o } } )$ $\leq \pi _ { i } ^ { * } ( N G ; \overline { { o } } )$ . Thus, the agent can charge a protection fee of

$$
f _ {\overline {{o}}} = \pi_ {i} ^ {*} (N G; \overline {{o}}) - \pi_ {i} ^ {*} (G; \overline {{o}}).
$$

Substituting the values of $\pi _ { i } ^ { * } ( N G ; \overline { { o } } )$ and $\pi _ { i } ^ { * } ( G ; \overline { { o } } )$ from (30) and (31), respectively, we get

$$
f _ {\overline {{o}}} = \frac {(2 d (1 2 d + 7) \alpha + 1) \beta (2 d (\alpha (4 d (\mu_ {t} + 1) + 3 \mu_ {t} + 2) - 4 \mu_ {t} + 2) - 3 \mu_ {t} + 2)}{1 0 2 4 (2 d + 1) ^ {3} (\mu_ {t} + 1)}.
$$

The profit of the agent by offering protection is

$$
\pi_ {g} (P; \overline {{o}}) = \pi_ {g} (N G; \overline {{o}}) + 2 f _ {\overline {{o}}}.\tag{33}
$$

Substituting the values of $\pi _ { g } ( N G ; \overline { { o } } )$ and f<sub>o</sub>, we get

$$
\pi_ {g} (P; \overline {{o}}) = \frac {\beta \mu_ {t} U _ {2} + 2 (2 d + 1) \beta (2 d \alpha + 1) (2 d (1 2 d + 7) \alpha + 1)}{5 1 2 (2 d + 1) ^ {3} (\mu_ {t} + 1)},
$$

where $U _ { 2 } = 4 d ( d ( ( 4 d + 3 ) ( 1 2 d + 7 ) \alpha ^ { 2 } - 4 8 d \alpha - 4 4 \alpha + 5 1 2 d$ $+ 7 6 8 ) - 9 \alpha + 3 8 2 ) + 2 5 3 .$

7.2.5. Testing Robustness of Theorem 2. Next, we check whether the result in Theorem 2 continues to hold in this extension, when the direct traffic is less responsive to the geoconquesting. That is, we want to show that offering protection instead of geoconquesting leads to a higher profit for the agent. Thus, we need to show that $\pi _ { g } ( P ; \overline { { o } } ) \geq \pi _ { g } ( G ; \overline { { o } } )$ . Define $\begin{array} { r } { \hat { \alpha } = \frac { 1 } { 6 + 1 0 a } . } \end{array}$ Using the expressions of $\pi _ { g } ^ { * } ( P ; \overline { { o } } )$ and $\pi _ { g } ^ { * } ( G ; \overline { { o } } )$ , it is easy to establish that $\pi _ { g } ( P ; \overline { { o } } ) \geq \pi _ { g } ^ { \circ } ( G ; \overline { { o } } )$ ) when $\alpha \geq { \hat { \alpha } }$ . This proves that offering protection instead of geoconquesting leads to a higher profit.

We now solve the problem of the agent under a situation when a third party, that is, an outside option, also offers the geoconquesting service.

7.2.6. Testing Robustness of Theorem 3. We now check whether the result in Theorem 3 holds in this exten sion. That is, we want to show that the agent continues to offer protection in the presence of an outside option. Moreover, the profit of the agent increases due to the presence of an outside option. In the presence of an out side option, the agent is forced to offer geoconquesting at $\mu _ { g } = \mu _ { o }$ . Thus, the protection fee charged by the agent is

$$
f _ {o} = \frac {(2 d \alpha + 1) (2 d (1 2 d + 7) \alpha + 1) \beta}{2 5 6 (2 d + 1) ^ {2} (\mu_ {o} + 1)}.
$$

The profit of the agent in this case is

$$
\pi_ {g} ^ {*} (P; o) = \frac {\beta (2 d \alpha + 1) (2 d (1 2 d + 7) \alpha + 1)}{1 2 8 (2 d + 1) ^ {2} (\mu_ {o} + 1)} + \frac {\beta \mu_ {t}}{2 \mu_ {t} + 2}.\tag{34}
$$

To compare the profit of the agent before and after the outside option, we need the following two comparisons: $( \mathrm { i } ) \ \pi _ { g } ^ { * } ( P ; o ) \geq \pi _ { g } ^ { * } ( N G ; \overline { { o } } )$ and $\mathrm { i i } ) \ \pi _ { g } ^ { * } ( P ; o ) \geq \pi _ { g } ^ { * } ( \bar { P } ; \overline { { o } } )$ Thus, we obtain

$$
\begin{array}{c} \pi_ {g} ^ {*} (P; o) - \pi_ {g} ^ {*} (N G; \overline {{o}}) = \frac {(2 d \alpha + 1) (2 d (1 2 d + 7) \alpha + 1) \beta}{1 2 8 (2 d + 1) ^ {2} (\mu_ {o} + 1)}, \\ (2 d (1 2 d + 7) \alpha + 1) \beta (U _ {3} \\ \pi_ {g} ^ {*} (P; o) - \pi_ {g} ^ {*} (P; \overline {{o}}) = \frac {+ 2 (2 d + 1) (1 - \mu_ {o}) (2 d \alpha + 1))}{5 1 2 (2 d + 1) ^ {3} (\mu_ {o} + 1) (\mu_ {t} + 1)}, \end{array}
$$

where $U _ { 3 } = \mu _ { t } ( 2 d \mu _ { o } ( ( 4 d + 3 ) \alpha - 4 ) - 2 d ( 4 d \alpha + \alpha + 8 ) - 3 \mu _ { o } - 7 ) .$ It is easy to see that above qualities are positive. Thus, (i) $\pi _ { g } ^ { * } ( P ; o ) \bar { \geq } \pi _ { g } ^ { * } ( N G ; \overline { { o } } )$ and (ii) $\pi _ { g } ^ { * } ( P ; o ) \geq \bar { \pi _ { g } ^ { * } } ( P ; \overline { { o } } )$

We now summarize the analysis in this extension in the following proposition.

Proposition 8. When $\alpha > { \hat { \alpha } } ,$ we have the following results: i. Offering protection instead of geoconquesting leads to a higher profit for the agent.

ii. The agent continues to offer protection in the presence $o f$ an outside option. Moreover, the profit of the agent increases due to the presence of an outside option

The previous proposition shows that as long as a sufficient fraction of direct traffic is affected by geoconquesting, our main results continue to hold. In the next section, we conclude and summarize the main findings of our paper.

## 7.3. Different Product Prices by Advertising Firms

In our model thus far, we assumed that both advertising firms are identical. We now relax this assumption and allow Firm 1 and Firm 2 to charge different prices for their products. We assume that Firm 1 and 2 charge prices $p _ { 1 }$ and $p _ { 2 }$ , respectively. Without loss of generality, we assume that $p _ { 1 } > p _ { 2 }$ . In this situation, the profits of firms can be written as follows:

$$
\begin{array}{c} \pi_ {1} = p _ {1} (L _ {1} + d) (1 - g _ {2} r _ {2}) + p _ {1} (L _ {2} + d) g _ {1} r _ {1} (1 - r _ {1}) \\ \qquad - (1 + \mu_ {t}) a _ {1} - (1 + \mu_ {g}) (L _ {2} + d) g _ {1} ^ {2}, \\ \pi_ {2} = p _ {2} (L _ {2} + d) (1 - g _ {1} r _ {1}) + p _ {2} (L _ {1} + d) g _ {2} r _ {2} (1 - r _ {2}) \\ \qquad - (1 + \mu_ {t}) a _ {2} - (1 + \mu_ {g}) (L _ {1} + d) g _ {2} ^ {2}. \end{array}
$$

Taking the derivative of $\pi _ { 1 }$ with respect to $a _ { 1 } , g _ { 1 } , r _ { 1 }$ and $\pi _ { 2 }$ with respect to $a _ { 2 } , g _ { 2 } , r _ { 2 } ,$ we get

$$
\begin{array}{r l r} & & {- a _ {1} ^ {2} (\mu_ {t} + 1) - 2 a _ {1} a _ {2} (\mu_ {t} + 1) + a _ {2} (- a _ {2} (\mu_ {t} + 1)} \\ & & {\frac {d \pi_ {1}}{d a _ {1}} = \frac {+ (r _ {1} - 1) r _ {1} g _ {1} p _ {1} - r _ {2} g _ {2} p _ {1} + g _ {1} ^ {2} (\mu_ {g} + 1) + p _ {1})}{(a _ {1} + a _ {2}) ^ {2}},} \\ & & {- a _ {2} ^ {2} (\mu_ {t} + 1) - 2 a _ {1} a _ {2} (\mu_ {t} + 1) + a _ {1} (- a _ {1} (\mu_ {t} + 1)} \\ & & {\frac {d \pi_ {2}}{d a _ {2}} = \frac {+ (r _ {2} - 1) r _ {2} g _ {2} p _ {2} - r _ {1} g _ {1} p _ {2} + g _ {2} ^ {2} (\mu_ {g} + 1) + p _ {2})}{(a _ {1} + a _ {2}) ^ {2}},} \\ & & {\frac {d \pi_ {1}}{d g _ {1}} = - \frac {(d (a _ {1} + a _ {2}) + a _ {2}) ((r _ {1} - 1) r _ {1} p _ {1} + 2 g _ {1} (\mu_ {g} + 1))}{a _ {1} + a _ {2}},} \\ & & {\frac {d \pi_ {2}}{d g _ {2}} = - \frac {(d (a _ {1} + a _ {2}) + a _ {1}) ((r _ {2} - 1) r _ {2} p _ {2} + 2 g _ {2} (\mu_ {g} + 1))}{a _ {1} + a _ {2}},} \\ & & {\frac {d \pi_ {1}}{d r _ {1}} = - \frac {(2 r _ {1} - 1) g _ {1} p _ {1} (d (a _ {1} + a _ {2}) + a _ {2})}{a _ {1} + a _ {2}},} \\ & & {\frac {d \pi_ {2}}{d r _ {2}} = - \frac {(2 r _ {2} - 1) g _ {2} p _ {2} (d (a _ {1} + a _ {2}) + a _ {1})}{a _ {1} + a _ {2}}.} \end{array}
$$

Solving for $\begin{array} { r } { \frac { d \pi _ { 1 } } { d r _ { 1 } } = 0 \mathrm { a n d } \frac { d \pi _ { 2 } } { d r _ { 2 } } = 0 . } \end{array}$ , it is easy to see that $\begin{array} { r } { r _ { 1 } ^ { * } = \frac { 1 } { 2 } } \end{array}$ and $\begin{array} { r } { r _ { 2 } ^ { * } = \frac { 1 } { 2 } . } \end{array}$ . Substituting $\begin{array} { r } { r _ { 1 } = \frac { 1 } { 2 } } \end{array}$ in $\frac { d \pi _ { 1 } } { d g _ { 1 } }$ and solving for $\begin{array} { r } { \frac { d \pi _ { 1 } } { d g _ { 1 } } = 0 , } \end{array}$ , leads to $\begin{array} { r } { g _ { 1 } ^ { * } = \frac { p _ { 1 } } { 8 ( \mu _ { g } + 1 ) } } \end{array}$ : Similarly, solving $\begin{array} { r } { \frac { d \pi _ { 2 } } { d g _ { 2 } } = 0 } \end{array}$ leads to $\begin{array} { r } { g _ { 2 } ^ { * } = \frac { p _ { 2 } } { 8 ( \mu _ { g } + 1 ) } } \end{array}$ : Substituting $\begin{array} { r } { r _ { 1 } ^ { * } = \frac { 1 } { 2 } , r _ { 2 } ^ { * } = \frac { 1 } { 2 } , g _ { 1 } ^ { * } = } \end{array}$ $\frac { p _ { 1 } } { 8 ( \mu _ { g } + 1 ) } ,$ and $\begin{array} { r } { g _ { 2 } ^ { * } = \frac { p _ { 2 } } { 8 ( \mu _ { g } + 1 ) } } \end{array}$ in the expressions of $\textstyle { \frac { d \pi _ { 1 } } { d a _ { 1 } } }$ and $\textstyle { \frac { d \pi _ { 2 } } { d a _ { 2 } } } ,$ we can simultaneously solve for $\begin{array} { r } { \frac { d \pi _ { 1 } } { d a _ { 1 } } = 0 } \end{array}$ and $\begin{array} { r } { \frac { d \pi _ { 2 } } { d a _ { 2 } } = 0 . } \end{array}$ which leads to

$$
\begin{array}{l} a _ {1} ^ {*} = \frac {W _ {2} W _ {1} ^ {2}}{(\mu_ {t} + 1) (W _ {2} ^ {2} + 2 W _ {2} W _ {1} + W _ {1} ^ {2})}, \\ a _ {2} ^ {*} = \frac {W _ {2} ^ {2} W _ {1}}{(\mu_ {t} + 1) (W _ {2} ^ {2} + 2 W _ {2} W _ {1} + W _ {1} ^ {2})}, \end{array}
$$

where $\begin{array} { r } { W _ { 1 } = - \frac { p _ { 1 } ^ { 2 } } { 3 2 ( \mu _ { g } + 1 ) } + \frac { p _ { 1 } ^ { 2 } } { 6 4 ( \mu _ { g } + 1 ) } - \frac { p _ { 1 } p _ { 2 } } { 1 6 ( \mu _ { g } + 1 ) } + p _ { 1 } , \ W _ { 2 } = - \frac { p _ { 1 } p _ { 2 } } { 1 6 ( \mu _ { g } + 1 ) } } \end{array}$ $\begin{array} { r } { - \frac { p _ { 2 } ^ { 2 } } { 3 2 ( \mu _ { g } + 1 ) } + \frac { p _ { 2 } ^ { 2 } } { 6 4 ( \mu _ { g } + 1 ) } + p _ { 2 } . } \end{array}$

The proof of negative semidefiniteness of the Hessian matrix is in the online appendix (please see the proof of Lemma 4). We formally note the result here.

Lemma 4. When firm 1 and 2 set prices $p _ { 1 }$ and $p _ { 2 }$ and the agent is offering geoconquesting, firm 1’s optimal decisions are $\begin{array} { r } { a _ { 1 } ^ { * } = \frac { W _ { 2 } W _ { 1 } ^ { 2 } } { ( \mu _ { t } { + } 1 ) ( W _ { 2 } ^ { 2 } { + } 2 W _ { 2 } W _ { 1 } { + } W _ { 1 } ^ { 2 } ) } , ~ g _ { 1 } ^ { * } = \frac { p _ { 1 } } { 8 ( \mu _ { g } { + } 1 ) } , } \end{array}$ and $\begin{array} { r } { r _ { 1 } = \frac { 1 } { 2 } . } \end{array}$ . Similarly, firm $2 ^ { \prime } s$ optimal decisions are $a _ { 2 } ^ { * } =$ $\begin{array} { r } { \frac { W _ { 2 } ^ { 2 } W _ { 1 } } { ( \mu _ { t } + 1 ) ( W _ { 2 } ^ { 2 } + 2 W _ { 2 } W _ { 1 } + W _ { 1 } ^ { 2 } ) } , ~ g _ { 2 } ^ { * } = \frac { p _ { 2 } } { 8 ( \mu _ { g } + 1 ) } , ~ r _ { 2 } ^ { * } = \frac { 1 } { 2 } . } \end{array}$

We now solve the problem when the agent does not offer geoconquesting. When the agent is not offering geoconquesting, we have $g _ { 1 } = g _ { 2 } = r _ { 1 } = r _ { 2 } = 0$ . Using these in the previous first-order conditions, we get $a _ { 1 } ^ { * } =$ $\frac { p _ { 2 } p _ { 1 } ^ { 2 } } { ( \mu _ { t } + 1 ) ( p _ { 2 } ^ { 2 } + 2 p _ { 2 } p _ { 1 } + p _ { 1 } ^ { 2 } ) } ,$ , and $\begin{array} { r } { a _ { 2 } ^ { * } = \frac { p _ { 2 } ^ { 2 } p _ { 1 } } { ( \mu _ { t } + 1 ) ( p _ { 2 } ^ { 2 } + 2 p _ { 2 } p _ { 1 } + p _ { 1 } ^ { 2 } ) } . } \end{array}$ . We formally describe the result here.

Lemma 5. When firm 1 and firm 2 set prices $p _ { 1 }$ and $p _ { 2 }$ and the agent is not offering geoconquesting, their optimal decisions are $\begin{array} { r } { a _ { 1 } ^ { * } = \frac { p _ { 2 } p _ { 1 } ^ { 2 } } { ( \mu _ { t } + 1 ) ( p _ { 2 } ^ { 2 } + 2 p _ { 2 } p _ { 1 } + p _ { 1 } ^ { 2 } ) } a n d a _ { 2 } ^ { * } = \frac { p _ { 2 } ^ { 2 } p _ { 1 } } { ( \mu _ { t } + 1 ) ( p _ { 2 } ^ { 2 } + 2 p _ { 2 } p _ { 1 } + p _ { 1 } ^ { 2 } ) } . } \end{array}$

Comparing the expressions of $g _ { 1 } ^ { * }$ and $g _ { 2 } ^ { * }$ in Lemma $^ { 4 , }$ it is easy to see that $g _ { 1 } ^ { * } \geq g _ { 2 } ^ { * }$ , because $p _ { 1 } > p _ { 2 }$ . Similarly, com paring the optimal values of $a _ { 1 } ^ { * }$ and $a _ { 2 } ^ { * }$ in Lemma $^ { 4 , }$ it is easy to establish that $a _ { 1 } ^ { * } \geq a _ { 2 } ^ { * }$ . Also, comparing the values of $\dot { a _ { 1 } ^ { * } }$ and $a _ { 2 } ^ { * }$ from Lemma 5 (when the agent does not offer geoconquesting), we can easily establish that $a _ { 1 } ^ { * } \geq a _ { 2 } ^ { * }$ . We formally note this in the following proposition.

Proposition 9. When firm 1 and 2 set prices $p _ { 1 }$ and $p _ { 2 }$ such that $p _ { 1 } \geq p _ { 2 } .$ , the firms top-of-funnel and geoconquesting spendings are also asymmetric and satisfy the following:

• When the agent offers geoconquesting, the advertisers with higher product price $p _ { 1 }$ also invest more in both $t o p { - } O f { - }$ funnel and geoconquesting, that is, $g _ { 1 } ^ { * } \geq g _ { 2 } ^ { * }$ , and $a _ { 1 } ^ { * } \geq a _ { 2 } ^ { * }$

• When the agent does not offer geoconquesting, $a _ { 1 } ^ { * } \geq a _ { 2 } ^ { * }$

Intuitively, because $p _ { 1 } > p _ { 2 }$ , firm 1 is in a stronger position and can spend more on top-of-funnel and geoconquesting.

7.3.1. Agent’s Problem. Using the firms’ optimal decisions, we can write the profit function of the agent as

follows:

$$
\begin{array}{c} \pi_ {g} = \mu_ {g} (L _ {2} + d) g _ {1} ^ {2} + \mu_ {g} (L _ {1} + d) g _ {2} ^ {2} + \mu_ {t} a _ {1} + \mu_ {t} a _ {2}, \\ = \frac {\mu_ {t} W _ {2} (W _ {1} + W _ {2})}{W _ {1} (\mu_ {t} + 1) \left(\frac {(W _ {1} + W _ {2}) ^ {2}}{W _ {1} ^ {2}}\right)} \\ + \frac {\mu_ {g} (p _ {2} ^ {2} (a + L 1) + p _ {1} ^ {2} (a + L 2))}{6 4 (\mu_ {g} + 1) ^ {2}}. \end{array}
$$

Because $W _ { 1 }$ and $W _ { 2 }$ also depend on $\mu _ { g } ,$ the previous expression is highly nonlinear in $\mu _ { g } .$ Thus, we numerically solve for the optimal value of $\mu _ { g }$ and verify the results in Theorem 2 and 3. Theorem 2 proves that the agent’s profit is higher under protection service compared with offering geoconquesting. Figure 9 numerically shows the robustness of this result and plots the profits of the agent when it provides protection service and geoconquesting. It is clear that the profit of agent is higher when it provides protection service.

Similarly, Theorem 3 proves that the presence of an outside option benefits the agent. Figure 10 numerically checks the robustness of this result. We can see that as the outside option becomes worse $( \mathrm { i } . \mathrm { e } . , \mu _ { o }$ increases), the profit of the agent decreases. In other words, as the outside option becomes better $( \mathrm { i } . \mathrm { e } . , \mu _ { o }$ decreases), the profit of the agent increases.

In the next section, we analyze the impact of nogeoconquesting, geoconquesting, and protection on social welfare.

## 7.4. Social Welfare Analysis

We now analyze how different strategies adopted by the agent affect the social surplus. The total social welfare is the sum of profits earned by the platform and the advertisers. Let SocialSurplus $( P ; { \overline { { o } } } )$ , SocialSurplus $\left( G ; \overline { { o } } \right)$ and SocialSurplus $( N G ; \overline { { o } } )$ represent the total social surplus when the agent is offering, respectively, protection, geoconquesting, and no geoconquesting (under no outside option). Similarly, let SocialSurplus $( P ; o )$ , Social Surplus $\left( \mathrm { G } ; \mathrm { o } \right)$ , and SocialSurplus $( N G ; \bar { o } )$ represent the total social surplus when the agent is offering, respectively, protection, geoconquesting, and no geoconquesting (under outside option). Thus, we have

Figure 9. (Color online) Agent’s Profit Under Protection Is Higher Than That Under Geoconquesting  
![](/api/attachments/2UASBH9S/fulltext/images/bab422995abf4885e5bba87db6b43e7bde3d8840bdfa27780e91d841270492ad.jpg)

Figure 10. (Color online) As the Outside Option Becomes Worse $( \mathrm { i } . \mathrm { e } . , \mu _ { o }$ Increases), the Profit of the Agent Decreases  
![](/api/attachments/2UASBH9S/fulltext/images/a738064db438ca3c9a1b86e77f1d3e5c17baf80abd89b7b145c10709d6dbcf7b.jpg)  
Note. In other words, as the outside option becomes better $( \mathrm { i . e . , ~ } \mu _ { o }$ decreases), the profit of the agent increases.

SocialSurplus $( N G ; \overline { { o } } ) = \pi _ { g } ^ { * } ( N G ; \overline { { o } } ) + 2 \times \pi _ { i } ^ { * } ( N G ; \overline { { o } } ) ,$

SocialSurplus $( G ; \overline { { o } } ) = \pi _ { g } ^ { * } ( \mathcal { \bar { G } } ; \overline { { o } } ) + 2 \times \pi _ { i } ^ { * } ( G ; \overline { { o } } ) ,$

SocialSurplus $( P ; \overline { { o } } ) = \pi _ { g } ^ { * } ( P ; \overline { { o } } ) + 2 \times \pi _ { i } ^ { * } ( P ; \overline { { o } } )$

Substituting the values of profit expressions, we get

$$
\begin{array}{c} \text {SocialSurplus(NG;} \overline {{o}}) = 2 d - \frac {1}{2 (\mu_ {t} + 1)} + 1, \\ 4 0 1 6 d ^ {2} (\mu_ {t} + 1) ^ {2} + 8 d (5 1 7 \mu_ {t} + 3 7 9) \\ \text {SocialSurplus(G;} \overline {{o}}) = \frac {(\mu_ {t} + 1) + \mu_ {t} (1 0 3 9 \mu_ {t} + 1 5 2 6) + 5 1 2}{1 0 2 4 (2 d + 1) (\mu_ {t} + 1) ^ {2}}, \\ \text {SocialSurplus(P;} \overline {{o}}) = \frac {4 d (1 2 d (\mu_ {t} + 1) + 1 2 0 \mu_ {t} + 7) + 2 5 3 \mu_ {t} + 2}{5 1 2 (2 d + 1) (\mu_ {t} + 1)}. \end{array}
$$

Similarly, we can obtain social welfare under an outside option. Thus, we have

$$
\text { SocialSurplus } (N G; o) = \pi_ {g} ^ {*} (N G; o) + 2 \times \pi_ {i} ^ {*} (N G; o),
$$

$$
\text { SocialSurplus } (G; o) = \pi_ {g} ^ {*} (G; o) + 2 \times \pi_ {i} ^ {*} (G; o),
$$

$$
\mathrm{SocialSurplus} (P; o) = \pi_ {g} ^ {*} (P; o) + 2 \times \pi_ {i} ^ {*} (P; o).
$$

Substituting the values of profit expression, we get

$$
\begin{array}{l} \text {SocialSurplus(NG;o) = 2d- \frac {1}{2(\mu_ {t} + 1)} + 1}, \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \text {SocialSurplus(G;o) = \frac {+4dV3 + 495\mu_ {t} +\mu_ {o} V4 + 254}{512(2d + 1)(\mu_ {o} + 1) ^ {2} (\mu_ {t} + 1)},} \\ \text {SocialSurplus(P;o) = \frac {12d + 1}{128(\mu_ {o} + 1)} +\frac {\mu_ {t}}{2\mu_ {t} + 2}}, \end{array}
$$

where $V _ { 3 } = \mu _ { o } ( 1 3 \mu _ { o } ( 4 0 \mu _ { t } + 2 9 ) + 1 0 3 8 \mu _ { t } + 7 6 2 ) + 5 1 0 \mu _ { t } +$ 377, $V _ { 4 } = \mu _ { o } ( 5 1 5 \mu _ { t } + 2 5 4 ) + 1 0 1 8 \mu _ { t } + 5 1 6 .$

Comparing the expressions of total social surplus, we obtain the following result.

Proposition 10. The social surplus is lowest under protection service and highest under no geoconquesting. That is, SocialSurplus(P; o) ≤ SocialSurplus(G; o) ≤ SocialSurplus (NG; o). This is true under an outside option too, that is, $S o c i a l S u r p l u s ( P ; o ) \leq S o c i a l S u r p l u s ( G ; o ) \leq S o c i a l S u r p l u s$ (NG; o).

The previous result highlights the fact that, although protection makes the agent better off, this benefit comes at the expense of the advertisers. Conversely, although no geoconquesting is best with respect to the social surplus, the agent does not have an incentive to not offer geoconquesting. Another important result we obtain is as follows.

Proposition 11. The social surplus under the protection services increases with an outside option. That is, Social $S u r p l u s ( P ; o ) \ge S o c i a l S u r p l u s ( P ; \overline { { o } } )$

The previous result further highlights the fact that the presence of an outside option makes protection inevitable and benefits the agent. We now proceed to extend our model to include an opportunity cost, incurred by the agent for providing the protection service.

## 8. Conclusion and Discussion

In this study, we examine an advertising agency’s incentive in offering geoconquesting service under a set of scenarios accounting for competition among advertising firms, competition among advertising agencies, as well as the possibility of protecting firms from geoconquesting. We find that geoconquesting can improve the profit of the focal ad agency but reduce profits of the advertising firms. However, the advertising firms choose to adopt geoconquesting because a classic prisoner’s dilemma exists. In the presence of specialized third parties offering geoconquesting at a lower price, the focal agent needs to match their price. This price matching exacerbates the prisoner’s dilemma and decreases the profit of advertising firms further.

Because the focal ad agency loses out its geoconquesting business to the specialist agency, it has an incentive to regain its lost business through some other approach. Because both advertising firms suffer a profit loss when they conduct geoconquesting, the focal ad agency may offer protection to the advertising firms from geoconquesting. This agent can implement the protection through hiding the location data in an ad-impression before selling it on the ad exchange.

We analyze whether the focal ad agency offers such a protection service to compete with the specialist ad agency. Furthermore, we also analyze whether the incentives of the agent to offer protection exist even when it is a monopoly and whether these incentives change with competition. Interestingly, we find that the presence of an outside option increases the profit of the focal agent, because the need of protection from geoconquesting becomes more severe.

An interesting top-of-funnel variant of poaching a competitor’s customers is when an advertising firm buys search keywords of its competitor. For example, if Adidas buys keywords like “Nike.” Although buying competitor’s keywords appears to be a top-of-funnel version of poaching customers, it is very different from the concept of geoconquesting where poaching occurs at the bottom of the consumer purchase funnel. Although the presence of geoconquesting disincentivizes firms to invest in top-of-funnel advertising, buying a competitor’s keywords is unlikely to disincentivize firms from investing downstream in geoconquesting.

Our findings carry practical implications for advertising agencies on whether to offer geoconquesting services and how to compete with large agencies that also offer top-of-funnel services. More broadly, our study sheds insights on firms’ advertising strategies for adopting multiple channels to reach out to their prospective customers. One of the limitations of this work is that consumers are assumed to be nonstrategic. If advertising firms start giving heavy discounts to poach consumers from their competitors, then these consumers might strategically locate themselves close to the competitor to receive discounts.

## Acknowledgments

The authors are listed in alphabetical order.

## Endnotes

<sup>1</sup> See https://www.adweek.com/brand-marketing/what-marketerscan-learn-from-burger-kings-geo-conquesting-strategy-against-mcdonalds/.

<sup>2</sup> See https://dealerscope.com/2021/03/geo-conquesting-mobilemarketing-on-your-competitors-turf/.

<sup>3</sup> This cost is motivated by Google’s pricing: https://support. google.com/adsense/answer/180195?hl=en.

<sup>4</sup> See https:www.cidewalk.comtour.html.

## References

Abhishek V, Hosanagar K (2013) Optimal bidding in multi-item multislot sponsored search auctions. Oper. Res. 61(4):855–873.

Abhishek V, Hosanagar K, Fader PS (2015) Aggregation bias in sponsored search data: The curse and the cure. Marketing Sci. 34(1):59–77.

Agarwal A, Hosanagar K, Smith MD (2011) Location, location, location: An analysis of profitability of position in online advertis ing markets. J. Marketing Res. 48(6):1057–1073.

Andrews M, Luo X, Fang Z, Ghose A (2016) Mobile ad effectiveness: Hyper-contextual targeting with crowdedness. Marketing Sci. 35(2):218–233.

Chen Y, Li X, Sun M (2017) Competitive mobile geo targeting. Marketing Sci. 36(5):666–682.

Fang Z, Luo X, Andrews M, Phang CW (2014) Mobile discounts: A matter of distance and time. Harvard Bus. Rev. https://hbr.org 2014/05/mobile-discounts-a-matter-of-distance-and-time.

Fong NM, Fang Z, Luo X (2015) Geo-conquesting: Competitive locational targeting of mobile promotions. J. Marketing Res. 52(5): 726–735.

Fudenberg D, Tirole J (2000) Customer poaching and brand switch ing. RAND J. Econom. 31(4):634–657.

Ghose A, Todri V (2015) Toward a digital attribution model: Mea suring the impact of display advertising on online consumer behavior. Preprint, submitted November 10, https://dx.doi.org/ 10.2139/ssrn.2672090.

Ghose A, Yang S (2009) An empirical analysis of search engine advertising: Sponsored search in electronic markets. Management Sci. 55(10):1605–1622.

Ghose A, Ipeirotis PG, Li B (2014) Examining the impact of ranking on consumer behavior and search engine revenue. Management Sci. 60(7):1632–1654.

Ghose A, Kwon HE, Lee D, Oh W (2019) Seizing the commuting moment: Contextual targeting based on mobile transportation apps. Inform. Systems Res. 30(1):154–174.

Kuksov D, Prasad A, Zia M (2017) In-store advertising by competi tors. Marketing Sci. 36(3):402–425.

Kumar S, Tan Y, Wei L (2020) When to play your advertisement? Optimal insertion policy of behavioral advertisement. Inform. Systems Res. 31(2):589–606.

Mehra A, Bala R, Sankaranarayanan R (2012) Competitive behaviorbased price discrimination for software upgrades. Inform. Systems Res. 23(1):60–74.

Mookerjee R, Kumar S, Mookerjee VS (2017) Optimizing performancebased internet advertisement campaigns. Oper. Res. 65(1): 38–54.

Sayedi A, Jerath K, Srinivasan K (2014) Competitive poaching in sponsored search advertising and its strategic impact on tradi tional advertising. Marketing Sci. 33(4):586–608

Shaffer G, Zhang ZJ (1995) Competitive coupon targeting. Marketing Sci. 14(4):395–416.

Yang S, Ghose A (2010) Analyzing the relationship between organic and sponsored search advertising: Positive, negative, or zero interdependence? Marketing Sci. 29(4):602–623.

C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pera</sub>ti<sub>ons</sub> R<sub>esearc</sub>h & th<sub>e</sub> M<sub>anagemen</sub>t S<sub>c</sub>i<sub>ences an</sub>d it<sub>s con</sub>t<sub>en</sub>t <sub>may no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or</sub> <sub>ema</sub>il<sub>e</sub>d t<sub>o</sub> <sub>mu</sub>lti<sub>p</sub>l<sub>e</sub> <sub>s</sub>it<sub>es</sub> <sub>or</sub> <sub>pos</sub>t<sub>e</sub>d t<sub>o</sub> <sub>a</sub> li<sub>s</sub>t<sub>serv</sub> <sub>w</sub>ith<sub>ou</sub>t th<sub>e</sub> <sub>copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup> <sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use.</sub>

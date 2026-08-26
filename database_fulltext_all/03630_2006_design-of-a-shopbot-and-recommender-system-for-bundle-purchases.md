---
otero_id: 3630
otero_key: "S685MJ3B"
title: "Design of a shopbot and recommender system for bundle purchases"
authors: "Robert Garfinkel; Ram Gopal; Arvind Tripathi; Fang Yin"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.05.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Design of a shopbot and recommender system for bundle purchases

Robert Garfinkel <sup>a,1</sup>, Ram Gopal <sup>a,2</sup>, Arvind Tripathi <sup>b,3</sup>, Fang Yin <sup>a,⁎</sup>

<sup>a</sup> School of Business, University of Connecticut, Storrs, CT 066269-1041, USA University of Washington Business School, Seattle, WA 98195-3200, USA

Received 29 June 2005; received in revised form 10 May 2006; accepted 14 May 2006 Available online 3 July 2006

## Abstract

The increasing proliferation of online shopping and purchasing has naturally led to a growth in the popularity of comparisonshopping search engines, popularly known as “shopbots”. We extend the one-product-at-a-time search approach used in current shopbot implementations to consider purchasing plans for a bundle of items. Our approach leverages bundle-based pricing and promotional deals frequently offered by online merchants to extract substantial savings. Interestingly, our approach can also identify “freebies” that consumers can obtain at no extra cost. We also develop a model to extend the capability of the current recommendation algorithms that are mainly based on collaborative filtering and item-to-item similarity techniques, to incorporate product price and savings as an additional important factor in making recommendations to shoppers. We develop a practica algorithm that can be employed when the number of items is large or when the real-time nature of shopbot applications dictates quick response rates to consumer queries. A detailed experimental analysis with real-world data from major retailers suggests that the proposed models can provide significant savings for bundle purchasing consumers, and frequently identify freebies for consumers. Together the results underscore the potential benefits that can accrue by incorporating our models into current shopbot systems.

© 2006 Elsevier B.V. All rights reserved.

Keywords: Shopbot; Bundle pricing; Recommender system; Integer programming

## 1. Introduction

The Internet has dramatically reduced buyer search costs by providing easy information retrieval [13]. On the other hand researchers have found significant price variation on the Internet even for identical commodities such as books and CDs, to name a few [3,4]. This variation and the large number of vendors have made it difficult for a user to find the best price for an item or items. In response, a number of comparison-shopping search engines, widely known as “shopbots”, have become popular (e.g., mySimon.com, Froogle.com, and PriceGrabber.com). At these websites a shopper can enter the product name and specification, and the shopbot will search a large number of vendors and return the prices offered by retailers, as well as other information such as shipping cost and availability. Since the first shopbot, BargainFinder, launched in 1995, a large number of shopbots have emerged and are increasingly being used by online shoppers. Shopbots are claimed to be able to collect, process, and present product related information at little cost, and therefore greatly affect the efficiency and behavior of markets [16].

Most current shopbots are geared towards oneproduct-at-a-time search. We refer to a “product” as something that can be purchased separately from any other item (see Section 2.1). Thus, using these shopbots, a shopper who wants to find the best price for a group (bundle) of products would have to initiate a search for each individual item and then combine the results on her own. A few shopbots do allow a shopper to compare shopping for multiple items as a whole by displaying the total purchasing price of these items from a single vendor and/or from multiple vendors (e.g., PriceGrabber.com's “Shopping List” feature, BooksPrice.com's multiple book price comparison). However, none of these shopbots can incorporate the variety of bundling and pricing alternatives that are frequently offered by online retailers [19].

To illustrate the disadvantage of using one-productat-a-time shopbots to purchase a bundle, consider Fig.

![](/api/attachments/S685MJ3B/fulltext/images/110dc2aa08d218678cfb2f90ec6717db6009f31010f6c7854c5a1cb2ca9cc3f2.jpg)  
Fig. 1. Comparison between shopbot results and bundle promotion.

1. The lowest individual prices obtained from the shopbot MySimon.com for Apple iPod (\$244), and the software packages McAfee VirusScan 8.0 (\$32), Roxio Easy CD and DVD Creator (\$43.44), and Quicken 2004 Basic (\$26.31) are listed. Best Buy, on the other hand, offers a bundle promotion where a consumer who purchases Apple iPod for \$249.99 would then qualify to purchase any three software packages for a total of \$49.98. While the offer by Best Buy is not the cheapest for any individual product, it is a cheaper option for a consumer interested in purchasing Apple iPod, along with two or more of the listed software packages. In this situation, the shopbot fails to provide the best possible purchase plan for the consumers.

The use of bundle pricing and promotions has been a common marketing practice for a long time. Recently, They have been used extensively and more frequently in online retailing to boost sales since the menu cost of a digital storefront is much lower than that of its bricks-and-mortar counterpart. Another reason for increased use of bundle pricing and promotions could be that retailers are trying to avoid direct price competition pressure caused by shopbots. Further, online shoppers are increasingly purchasing multiple items in a single order because of factors such as the convenience of online shopping, site search, non-linear shipping costs, and recommendations of related products from various recommendation systems [5]. Therefore, it would be desirable to design a shopbot that is able to take advantage of promotions based on bundle pricing and promotions. Such a bundle shopbot would benefit consumers who desire to purchase multiple items by providing optimal purchase plans. It would also benefit merchants who offer bundle pricing and promotions to increase their market exposure.

The focus of our work is on the development of models for shopbots that leverage bundle pricing and promotional deals offered by online merchants to extract price savings. It is intended to operate in the presence of the demand for multiple items by a user. Recent academic work has addressed issues surrounding the impact of shopbots on consumer behavior and retailer pricing strategies [8,16], and operational design improvements to enhance a consumer's overall utility with the shopbots [11].

To the best of our knowledge, this is the first research incorporating bundle pricing and promotion into shopbot design. The main contribution of this research is to extend the capability of the current shopbots to take advantage of the plethora of bundle pricing and promotions so that shopbots can provide shoppers more effective and value-added services. This research also extends the capability of the current recommendation algorithms that are mainly based on collaborative filtering and item-to-item similarity techniques, to incorporate product price and savings as an additional important factor in making recommendations to shoppers. We also provide an empirical demonstration of the significant savings that could result from our extension to the current shopbots.

The rest of the paper is organized as follows. Section 2 presents a general classification of bundles, as well as a model for purchasing the desired products at minimum cost in the presence of bundle pricing and promotions. An efficient algorithm for solution of that model is also given. A recommender system based on the model of Section 2 is the subject of Section 3. Computational results using real data are given in Section 4 and indicate that substantial savings can result from use of the models and algorithms of Sections 2 and 3. Conclusions and future research directions are highlighted in Section 5.

## 2. Bundle purchasing models

In this section, we first discuss various types of bundle pricing and promotion practices that are commonly used by the retail industry. We then formally develop a general bundle purchasing model that leverages the bundle pricing and promotions to deliver optimal purchasing plans for the customers. Since a real shopbot needs to be able to respond to requests of a large number of shoppers in a timely way, we present a practical algorithm to solve the general bundle purchasing problem quickly and with excellent performance.

## 2.1. General classifications of bundles

There is considerable literature on the benefits of bundling to the sellers. Beginning with the work of Stigler [18] on how bundling can increase seller profits, this stream of research has dealt with the seller's bundling decision problem. Work in this stream has focused on construction and pricing of bundles to maximize profit (see [19] for a comprehensive review).

Adam and Yellen [1] classified three modes of bundling structures, namely pure bundling, mixed bundling, and component selling (pure unbundling). In pure bundling, individual items are not offered. Mixed

![](/api/attachments/S685MJ3B/fulltext/images/cc2df9f7278e435bb166bb42b12a0371e05cb3a328156b45bad0af48f4b5704b.jpg)  
Fig. 2. Bundle example — tie-in.

bundling is a combination of pure bundling and component selling. On the other hand pure bundling is not a concept of interest from the buyer's point of view since one can simply consider “components” to be minimal sets of goods that can be purchased individually.

![](/api/attachments/S685MJ3B/fulltext/images/5ebd972dbefa6425f7783a455ec8c76c10c12559171fbbdcf75e7343a62e0aa7.jpg)  
Fig. 3. Bundle example — add-on.

The various general bundling strategies that have been implemented by retailers [15] are listed below:

Deterministic bundling: Exactly one set of predetermined items is included in the bundle.

Non deterministic bundling: This includes, for instance, the following:

Tie-in bundling: The buyer is required to buy one major product (e.g., digital camera or mp3 player) to qualify for discounted prices on other products $\mathrm { ( e . g . }$ three software products for \$48). Usually there are comprehensive lists of both the major and tied-in products (see Fig. 2 for an illustration).

Add-on bundling: The buyer is required to buy one product (e.g., wireless router) to get a free product (e.g., wireless card). This is illustrated in Fig. 3.

Cross promotion: The buyer is required to purchase one product to qualify for a discount on another product. However, the buyer has the option of not purchasing the additional product.

Total value discount: If the total amount of an order is above a certain threshold, the order gets an extra discount (e.g., 10% or \$15 off any order above \$100) (see Fig. 4).

We incorporate all the above varieties of bundle pricing and promotion practices in the following model.

## 2.2. The general model

Consider a buyer with demand for one of each of a set of items $S _ { 0 } .$ A set of bundles $B : = \{ B _ { 1 } , B _ { 2 } , . . . \}$ is offered by the retailers, where each bundle in B contains at least one element of $S _ { 0 } .$ Included in B are the $\left| S _ { 0 } \right|$ degenerate bundles {i} for all $i \in S _ { 0 } .$ . Each item i has an original (unbundled) cost given by $c _ { i } { > } 0$ . The unbundled cost $\textstyle c ( T ) : = \sum _ { i \in T } c _ { i }$ of a set T of items represents the <sup>ð Þ</sup>benchmark for price savings. Also let $S _ { j }$ be the set of items in $B _ { j } ,$ and the set of all items in B is denoted by $S { : = } \cup _ { j \in B } \bar { S _ { j } }$ . The cost of $B _ { j }$ is $f _ { j } { > } 0$ , so that $f _ { j } { = } c _ { i }$ if $S _ { j } { = }$ <sup>[</sup>{i}. Let $B ( i )$ be the set of bundles that contain item i. Then the problem (CB) of choosing the cheapest set of bundles that satisfies the demand for $S _ { 0 } ,$ , can be modeled as the following set covering problem:

$$
\min \sum_ {j \in B} f _ {j} x _ {j}\tag{1}
$$

s.t.

$$
\sum_ {j \in B (i)} x _ {j} \geq 1, i \in S _ {0}\tag{2}
$$

$$
x _ {j} \text { binary }, j \in B\tag{3}
$$

Note that constraint (2) allows the buyer to receive additional goods beyond the desired set $S _ { 0 } .$ If $B ^ { * }$ is an optimal set of bundles from CB, denote by $\textstyle S ^ { * } \mathrel { \mathop : } = \bigcup _ { i \in B ^ { * } }$ $S _ { j }$ <sup>[</sup>the corresponding optimal set of goods. Then, if $B ^ { * }$ is purchased, the buyer may receive the set $F ^ { * }$ of additional goods (“freebies”) beyond single units of the elements of $S _ { 0 }$ . That is, $F ^ { * }$ contains at least one unit of every element of $S ^ { * } \backslash S _ { 0 } ,$ as well as possible extra units of elements of $S _ { 0 } .$ . In Section 4 we show that our shopbot design frequently identifies freebies for shoppers, which results in further savings. This feature is not available in any current shopbots and can provide additional value and a richer shopping experience for shoppers.

![](/api/attachments/S685MJ3B/fulltext/images/e748e7d830d968f8b8b39aa31ced0b99a29f81b7ecbb9dda8c476f96c815e4ee.jpg)  
Fig. 4. Bundle example — value discount.

Given the bundle set B, along with the vector of bundle prices, the problem of choosing an optimal subset of B is set covering, which is shown to be NP-Hard (e.g. [7]). There are also other features of the current problem that make it computationally difficult. Interested readers can refer to Appendix A for a detailed discussion.

## 2.3. A GRAB algorithm

For consumer purchases that involve only a few items, an optimal solution of CB can easily be found by generic integer programming or specialized set covering algorithms. However, if we want to use the same model to help organizations decide on an optimal purchase plan for a large number of items, even specialized algorithms might take a long time to reach optimality. On the other hand, even if the number of items is small as in the case for individual consumers, the huge number of simultaneous requests that could be received by the shopbots can still pose a challenge. For example, pricegrabber.com, a popular shopbot, claims to provide price comparison services to 18 million active shoppers. Even if only a small portion of these shoppers send in bundle search requests at any point of time, it would take at least quite a few seconds to solve for optimality for all the requests. Usability research shows that delay of more than 10 s results in loss of user attention [12]. So waiting time even in seconds could lead to user attrition. Therefore, a practical algorithm that can solve the problem quickly will be useful if the number of items to be purchased is large and/or there are potential benefits from shaving off valuable seconds in responding to a large number of shopper requests. Therefore, we present the algorithm, which we name “Greedy Addition of Bundles” (GRAB).

Let t index the iterations; $M ^ { t }$ be the items in $S _ { 0 }$ not yet purchased at iteration $t ; N ^ { t }$ be the bundles of B that have not been chosen at iteration t. The GRAB algorithm is formally presented below.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm GRAB
Initialization Step:
    Set  $M^{1}=S_{0}$ ,  $N^{1}=B$ , and t=1.
Bundle Addition Step:
Select a Bundle
 $j^{t}\in N^{t}$  to  $\min\left\{f_{j}/\sum_{i\in S_{j}\cap M^{t}}c_{i}\right\}$ .
Iteration Step:
Set  $N^{t+1}=N^{t}\backslash\{j^{t}\}$ ,  $M^{t+1}=M^{t}\backslash\{S_{j}^{t}\}$ , and t=t+1.
If  $M^{t}\neq\phi$  go to Bundle Addition Step.
Bundle Generation Step:
The solution is  $x_{j}=1$  for  $j\notin N^{t+1}$  and  $x_{j}=0$  otherwise.
</div>

Note that at each step the algorithm chooses a bundle that includes at least one desired item not purchased at previous steps. The chosen bundle has the lowest ratio of cost to the individual costs of these desired items in the bundle. This algorithm is a variation of that of Fisher and Wolsey [6]. GRAB takes advantage of the fact that there are prices for each of the individual items, a condition that is not true in general set covering problems. Our computational experiments with real-world data suggest that the timesavings of GRAB are on the order of 90% compared to generic integer programming packages such as CPLEX. In terms of objective function value, the performance of GRAB is consistent and is approximately 1% greater than that of an optimal algorithm.

## 3. Recommender system

The general bundle purchasing model described in the previous section can also be utilized to extend the capabilities of current recommendation systems. Recommendation has become an important tool for target marketing in the online world. Given the huge number of items available and vast amount of information that can be easily collected from online shoppers, almost every major online retailer employs recommendation systems to help shoppers identify interesting items, thereby boosting sales and enhancing the shopping experience. There are numerous recommendation algorithms that have been adopted, including traditional collaborative filtering, cluster models, search-based methods, and item-to-item collaborative filtering, among others [9]. These algorithms commonly use the shopper's purchasing activity data as well as browsing history, rating data, and demographic data to infer the shopper's preferences and give recommendations based on the similarity and/or relatedness amongst shoppers and/or items.

However, none of the current recommendation algorithms consider possible savings that can be obtained from bundle pricing and promotions in making recommendations to consumers [2]. Consider a situation where a shopper wants to buy a digital camera. Current recommendation systems may recommend one or more photo printers to accompany the camera, based on the similarity among shoppers and/or items. However, if there is a bundle promotion involving this camera and a certain model of printer, current recommendation algorithms are not capable of identifying this specific printer as the top pick, which could then generate the highest utility option for the shopper.

Here we use the general model CB of the previous section to develop a model for recommending products that the consumer can obtain at discounts if combined with the original bundle of items. Note that this is in addition to any freebies identified when solving the original problem CB. Recall from Section 2.2 that $S ^ { * } { : } { = } \cup _ { j \in B ^ { * } } S _ { j }$ . Then, one-at-a-time, for all $i ^ { \prime } \in S \backslash S ^ { * }$ solve the following set covering problem, which we denote by RS:

$$
\min \sum_ {j \in B} f _ {j} x _ {j}\tag{4}
$$

s.t.

$$
\sum_ {j \in B (i)} x _ {j} \geq 1, i \in \{i ^ {\prime} \} \cup S ^ {*}\tag{5}
$$

$$
x _ {j} \text { binary }, j \in B\tag{6}
$$

with optimal objective value $z ( i ^ { \prime } )$ . Then product recommendation can be displayed in non increasing order of extra savings $c _ { i ^ { \prime } } - z ( i ^ { \prime } )$ or alternatively of $\underline { { c _ { i } {  } { z } ( i ) } }$ . The same GRAB algorithm can be used to solve ${ \mathrm { R S } } ^ { c _ { i ^ { \prime } } }$

Note that our model assumes a given set of items $S \backslash S ^ { * }$ to consider for recommendation. This set of items could come from the current recommendation algorithms. Then, based on the possible savings from bundle pricing and promotions, these items are sorted in order of non-decreasing amount of savings and presented in that order. We believe the incorporation of bundle pricing and promotion information into recommendation algorithms will greatly enhance the possibility that shopper purchase the recommended items and benefit both shoppers and merchants.

## 4. Experimental verification

To ascertain the potential practical benefits from deploying our models, we conducted an experimental verification using real-world data on computer-related products. Recent reports indicate that this product category, which includes software, wireless gadgets, printers, memories, and digital cameras is one of the most commonly purchased categories online [14]. When selecting retailers from whom to collect data, we tried to avoid the brand effect that might complicate our experimental results. The literature has shown that the reputation of a seller, especially in the online world, does have a significant impact on the price of a product and the behavior of shoppers [17]. Therefore, to limit any confounding retailer brand effects that may influence a shopper, we carefully selected the set of retailers for consideration as follows. We initially started with Best Buy, and then identified its main competitors in the category of computer products. This information was derived from Hoovers (www.hoovers.com), which provides in-depth information on $4 0 { , } 0 0 0$ of the world's top business entities as well as comprehensive industry and market information. This process led to the selection of the following 14 retailers: Best Buy; Circuit City, Buy.com, CDW.com, Staples, Kmart, Wal-Mart, OfficeMax, Office Depot, Sears, Gateway, Radio Shack, CompUSA, and Amazon.com. We only included these 14 well-established national retail chains or online retailers so that the reputation of sellers is identical across different bundle solutions. This way we can show clearly that the savings are really from purchasing in bundles instead of possibly purchasing from a cheap, but perhaps non brand-name seller. If we were to include more sellers, it will surely not reduce the total savings, but these savings could be compromised by the lack of reputation of certain sellers.

We then monitored these retailers for a period of 10 days in early 2004, and captured their bundle-based pricing and promotional offers for computer-related products. During these 10 days, we identified various formats of bundle offers including: special discounts/ rebates on bundled software; free memory cards with purchase of digital cameras; and any three software products for a fixed price with the purchase of a given set of products. From these we generated a total of 194 bundles involving 36 products. These products naturally fell into seven groups and are listed in Table 1, along with the lowest price for each product among these 14

Table 1 List of products

<table><tr><td>Group</td><td>Product</td><td>Lowest price</td></tr><tr><td rowspan="5">Camera</td><td>Photosmart 635 2.1 megapixel digital still camera</td><td>$149.99</td></tr><tr><td>Canon powershot A80 digital still camera (4.0 megapixel)</td><td>$349.94</td></tr><tr><td>Olympus 5.0-Megapixel 3× Optical/4× Digital Zoom Digital Camera Brand/Model: OLM C5000ZOOM</td><td>$329.94</td></tr><tr><td>Sony Cyber-shot® 5.0-Megapixel 4× Optical/4× Digital Zoom Digital Camera Brand/Model: SON DSCV1</td><td>$459.94</td></tr><tr><td>Kodak 5.0-Megapixel 3× Optical/3.3× Digital Zoom Digital Camera Brand/Model: EKC DX4530</td><td>$269.99</td></tr><tr><td rowspan="2">Memory</td><td>Lexar 128 MB compact flash card</td><td>$44.74</td></tr><tr><td>SanDisk 128MB Secure DigitalTM Memory Card Brand/Model: SDK SDSDB128781</td><td>$54.99</td></tr><tr><td rowspan="3">Printer</td><td>PhotoSmart 7350 Color photo printer (inkjet printer)</td><td>$89.98</td></tr><tr><td>Black inkjet cartridge (Mfr: Epson) T007201</td><td>$18.93</td></tr><tr><td>Color inkjet cartridge (Mfr: Epson) T009201</td><td>$18.80</td></tr><tr><td rowspan="8">Software — picture-editing</td><td>Adobe® Photoshop® Elements 2.0</td><td>$58.62</td></tr><tr><td>Adobe Photoshop Album 2.0</td><td>$39.22</td></tr><tr><td>DVD_PictureShow_2/Photo_Explorer_8_-_Windows_</td><td>$49.99</td></tr><tr><td>PhotoImpact_8_-_Windows_</td><td>$55.00</td></tr><tr><td>VideoStudio_7_-_Windows_</td><td>$86.99</td></tr><tr><td>Pinnacle_Studio_Version_8_-_Digital_Imaging_-_Windows_</td><td>$57.95</td></tr><tr><td>Flip_Album_Suite_BE4.2_-_Windows_</td><td>$49.95</td></tr><tr><td>Pinnacle_Studio_Version_7_-_Windows_</td><td>$49.99</td></tr><tr><td rowspan="9">Software — utility</td><td>Norton Antivirus 2004 Professional edition</td><td>$57.94</td></tr><tr><td>Norton Antispam 2004</td><td>$24.12</td></tr><tr><td>McAfee Internet Security Suite 6.0</td><td>$39.99</td></tr><tr><td>Tax cut deluxe 2003</td><td>$24.95</td></tr><tr><td>McAfee SpamKiller V5.0</td><td>$24.96</td></tr><tr><td>McAfee Personal Firewall plus 5.0</td><td>$15.86</td></tr><tr><td>Norton Systemworks 2004</td><td>$59.72</td></tr><tr><td>Norton Personal Firewall 2004</td><td>$44.82</td></tr><tr><td>McAfee_VirusScan_2004_Ver._8.0_-_Windows_</td><td>$30.00</td></tr><tr><td rowspan="3">WirelessCard</td><td>Netgear WG511 802.11g 54 Mbps Wireless PC Card</td><td>$38.20</td></tr><tr><td>D-Link AirPlus Xtreme G DWL G650</td><td>$43.99</td></tr><tr><td>Belkin 802.11b Wireless Notebook Adapter Brand/Model: BLK F5D6020</td><td>$29.99</td></tr><tr><td rowspan="4">WirelessRouter</td><td>Netgear WGR614 v2 802.11g Wireless 4-port Router</td><td>$67.98</td></tr><tr><td>D-Link AirPlus Xtreme G DI-624</td><td>$55.18</td></tr><tr><td>Belkin 802.11b Wireless Broadband Router with 4-Port Switch Brand/Model: BLK F5D62314</td><td>$34.99</td></tr><tr><td>Belkin 802.11g Wireless Broadband Router with 4-Port Switch Brand/Model: BLK F5D72304</td><td>$49.99</td></tr></table>

retailers in the monitoring period. Table 2 lists summary statistics on the individual items and the bundles. We evaluated the bundle shopping models by varying the size of the bundle from 2 to 20. For each bundle size, we randomly generated the products in the bundle by randomly drawing from the seven product groups without replacement. The reason for drawing by group is that, realistically, a shopper is less likely to buy products in the same category, for example, two digital cameras, in one order than to buy products from different categories, for example, a digital camera and a photo printer. One thousand bundles for each bundle size were generated, resulting in a total of 19,000 simulation runs.

Table 2 Summary of the sample

<table><tr><td>Items</td><td></td><td>Bundles</td><td></td></tr><tr><td>Mean</td><td>$84.64</td><td>Mean</td><td>$376.80</td></tr><tr><td>Max</td><td>$459.94</td><td>Max</td><td>$549.97</td></tr><tr><td>Min</td><td>$5.86</td><td>Min</td><td>$0.01</td></tr><tr><td>S.D.</td><td>$105.05</td><td>S.D.</td><td>$142.19</td></tr><tr><td>n</td><td>36</td><td>n</td><td>194</td></tr></table>

For each bundle we solved the problem using both CPLEX and our algorithm and compared the resulting savings using the sum of the individually-cheapest prices of items in the bundle as a benchmark. Fig. 5 highlights the cumulative percentage savings over the

![](/api/attachments/S685MJ3B/fulltext/images/e0c1cb88f78e9a184346f23e232eadca082d995ea6658cda3ccd2a47566ee0da.jpg)  
Fig. 5. Distribution of savings.

benchmark using the GRAB algorithm. Positive savings were observed in over 85% of the cases. The median savings rate was 10%, and in nearly 10% of the cases the percentage savings were over 20%. Table 3 lists the performance of CPLEX and the GRAB algorithm for various bundle sizes. As expected, the savings increase as the number of items in the bundle increases. The GRAB algorithm performs extremely well. Both the optimal and GRAB algorithms were able to frequently identify freebies, with more freebies identified for larger bundles. Utilizing the lowest individual price of the freebies as the baseline, the net savings with the freebies included are 4% to 10% higher than without the freebies. Interestingly, the GRAB algorithm, in a number of instances, was able to identify higher-valued freebies than the optimal algorithm.

Results from the evaluation of the recommender system are shown in Table 4. These results were derived from the optimal algorithm and reflect the product recommendation that results in the largest savings. In general, the buyer need only spend less than 5% of the original total cost to purchase the recommended item.

Performance analysis results

<table><tr><td rowspan="2">Number of items needed</td><td rowspan="2">Avg benchmark cost of needed items</td><td colspan="6">Optimal</td><td colspan="6">GRAB algorithm</td></tr><tr><td>Avg cost</td><td>Avg saving (%)</td><td>S.D. (%)</td><td>Avg # of extra items</td><td>Avg value of extra items</td><td>% of benchmark cost</td><td>Avg cost</td><td>Avg saving (%)</td><td>S.D. (%)</td><td>Avg # of extra items</td><td>Avg value of extra items</td><td>% of benchmark cost</td></tr><tr><td>2</td><td>$166.47</td><td>$158.51</td><td>6.8</td><td>16.5</td><td>0.3</td><td>$13.38</td><td>10.9</td><td>$158.51</td><td>6.8</td><td>16.5</td><td>0.3</td><td>$13.38</td><td>10.9</td></tr><tr><td>3</td><td>$257.41</td><td>$246.04</td><td>5.9</td><td>11.8</td><td>0.4</td><td>$17.26</td><td>9.5</td><td>$246.04</td><td>5.9</td><td>11.8</td><td>0.4</td><td>$17.26</td><td>9.5</td></tr><tr><td>4</td><td>$323.21</td><td>$306.18</td><td>6.3</td><td>9.6</td><td>0.5</td><td>$24.73</td><td>10</td><td>$306.23</td><td>6.2</td><td>9.6</td><td>0.5</td><td>$24.85</td><td>10.1</td></tr><tr><td>5</td><td>$414.57</td><td>$390.26</td><td>6.5</td><td>8.3</td><td>0.6</td><td>$31.35</td><td>9.3</td><td>$390.41</td><td>6.5</td><td>8.3</td><td>0.7</td><td>$31.58</td><td>9.4</td></tr><tr><td>6</td><td>$497.73</td><td>$466.50</td><td>6.7</td><td>7.1</td><td>0.7</td><td>$32.03</td><td>7.7</td><td>$466.68</td><td>6.6</td><td>7.1</td><td>0.7</td><td>$32.34</td><td>7.8</td></tr><tr><td>7</td><td>$588.50</td><td>$545.42</td><td>7.7</td><td>7</td><td>0.8</td><td>$37.52</td><td>7.3</td><td>$545.75</td><td>7.6</td><td>7</td><td>0.8</td><td>$38.00</td><td>7.4</td></tr><tr><td>8</td><td>$666.88</td><td>$611.69</td><td>8.8</td><td>7.1</td><td>1.0</td><td>$42.05</td><td>7</td><td>$612.28</td><td>8.7</td><td>7.1</td><td>1.0</td><td>$42.63</td><td>7.1</td></tr><tr><td>9</td><td>$757.90</td><td>$695.09</td><td>8.8</td><td>6.8</td><td>1.1</td><td>$47.00</td><td>6.8</td><td>$695.70</td><td>8.7</td><td>6.8</td><td>1.1</td><td>$47.87</td><td>6.9</td></tr><tr><td>10</td><td>$844.94</td><td>$772.20</td><td>9</td><td>6.1</td><td>1.1</td><td>$46.30</td><td>5.9</td><td>$773.05</td><td>8.9</td><td>6.1</td><td>1.1</td><td>$47.24</td><td>6</td></tr><tr><td>11</td><td>$912.59</td><td>$826.50</td><td>9.9</td><td>5.9</td><td>1.3</td><td>$51.82</td><td>6</td><td>$827.44</td><td>9.8</td><td>5.9</td><td>1.3</td><td>$53.19</td><td>6.2</td></tr><tr><td>12</td><td>$1000.71</td><td>$900.85</td><td>10.3</td><td>5.5</td><td>1.3</td><td>$54.82</td><td>5.7</td><td>$902.26</td><td>10.2</td><td>5.6</td><td>1.4</td><td>$56.71</td><td>5.9</td></tr><tr><td>13</td><td>$1087.77</td><td>$974.91</td><td>10.7</td><td>5.2</td><td>1.4</td><td>$58.10</td><td>5.5</td><td>$976.53</td><td>10.5</td><td>5.2</td><td>1.5</td><td>$60.17</td><td>5.7</td></tr><tr><td>14</td><td>$1168.34</td><td>$1042.02</td><td>11.1</td><td>4.9</td><td>1.5</td><td>$58.58</td><td>5.1</td><td>$1043.92</td><td>10.9</td><td>4.9</td><td>1.6</td><td>$61.38</td><td>5.3</td></tr><tr><td>15</td><td>$1248.80</td><td>$1104.26</td><td>11.9</td><td>4.9</td><td>1.5</td><td>$58.76</td><td>4.8</td><td>$1106.82</td><td>11.7</td><td>4.8</td><td>1.6</td><td>$62.39</td><td>5.1</td></tr><tr><td>16</td><td>$1351.52</td><td>$1192.22</td><td>12.1</td><td>4.8</td><td>1.5</td><td>$59.90</td><td>4.5</td><td>$1195.06</td><td>11.9</td><td>4.7</td><td>1.6</td><td>$63.43</td><td>4.8</td></tr><tr><td>17</td><td>$1441.32</td><td>$1262.71</td><td>12.7</td><td>4.7</td><td>1.6</td><td>$63.62</td><td>4.5</td><td>$1266.77</td><td>12.4</td><td>4.6</td><td>1.7</td><td>$67.01</td><td>4.7</td></tr><tr><td>18</td><td>$1535.85</td><td>$1341.38</td><td>12.9</td><td>4.4</td><td>1.6</td><td>$63.85</td><td>4.2</td><td>$1345.72</td><td>12.6</td><td>4.2</td><td>1.8</td><td>$67.74</td><td>4.5</td></tr><tr><td>19</td><td>$1613.24</td><td>$1402.93</td><td>13.3</td><td>4.3</td><td>1.7</td><td>$68.56</td><td>4.3</td><td>$1409.23</td><td>12.8</td><td>4.1</td><td>1.9</td><td>$72.97</td><td>4.6</td></tr><tr><td>20</td><td>$1711.97</td><td>$1478.32</td><td>13.8</td><td>4.1</td><td>1.7</td><td>$69.20</td><td>4.1</td><td>$1486.10</td><td>13.4</td><td>3.8</td><td>1.9</td><td>$73.52</td><td>4.3</td></tr></table>

Table 4  
Recommendation analysis results

<table><tr><td>No. of items needed</td><td>Benchmark cost of needed itemsa</td><td>Extra cost to buy recommended itema</td><td>Extra cost % of original costa</td><td>Benchmark value of recommended itema</td><td>% saving of benchmark valuea</td></tr><tr><td>2</td><td>$164.41</td><td>$6.05</td><td>4.2</td><td>$68.86</td><td>95.9</td></tr><tr><td>3</td><td>$255.94</td><td>$7.71</td><td>3.6</td><td>$71.34</td><td>94.7</td></tr><tr><td>4</td><td>$331.80</td><td>$10.15</td><td>3.6</td><td>$75.65</td><td>93.1</td></tr><tr><td>5</td><td>$421.17</td><td>$12.86</td><td>3.5</td><td>$80.57</td><td>91.3</td></tr><tr><td>6</td><td>$505.77</td><td>$14.99</td><td>3.0</td><td>$83.94</td><td>89.9</td></tr><tr><td>7</td><td>$583.44</td><td>$15.77</td><td>2.5</td><td>$85.44</td><td>89.3</td></tr><tr><td>8</td><td>$664.67</td><td>$20.15</td><td>3.0</td><td>$92.47</td><td>86.5</td></tr><tr><td>9</td><td>$750.58</td><td>$19.62</td><td>2.7</td><td>$91.58</td><td>86.8</td></tr><tr><td>10</td><td>$840.99</td><td>$22.49</td><td>2.9</td><td>$95.82</td><td>85.3</td></tr><tr><td>11</td><td>$929.82</td><td>$28.52</td><td>3.4</td><td>$104.34</td><td>82.1</td></tr><tr><td>12</td><td>$1005.48</td><td>$28.90</td><td>3.1</td><td>$104.74</td><td>81.2</td></tr><tr><td>13</td><td>$1085.41</td><td>$27.81</td><td>2.8</td><td>$102.85</td><td>82.2</td></tr><tr><td>14</td><td>$1180.28</td><td>$34.94</td><td>3.2</td><td>$111.28</td><td>78.8</td></tr><tr><td>15</td><td>$1260.15</td><td>$34.44</td><td>3.1</td><td>$109.83</td><td>79.4</td></tr><tr><td>16</td><td>$1350.48</td><td>$34.69</td><td>3.0</td><td>$107.57</td><td>78.8</td></tr><tr><td>17</td><td>$1441.52</td><td>$35.21</td><td>2.8</td><td>$106.55</td><td>79.2</td></tr><tr><td>18</td><td>$1527.57</td><td>$36.63</td><td>2.8</td><td>$106.06</td><td>78.0</td></tr><tr><td>19</td><td>$1614.40</td><td>$38.52</td><td>2.7</td><td>$105.22</td><td>78.1</td></tr><tr><td>20</td><td>$1706.26</td><td>$40.24</td><td>2.7</td><td>$105.68</td><td>77.5</td></tr></table>

<sup>a</sup> All are means over sample of 1000.

The potential savings from purchasing the recommended product are extremely large (in excess of 75%). These savings are the highest for smaller sized bundles, which underscores the viability of the proposed recommender system for consumer-oriented shopbots where a consumer's original shopping list may be comprised of only one or a few items.

## 5. Concluding remarks

We have provided a model for computing an optimal purchase plan to procure a bundle of items from competing sellers who offer bundle pricing and promotions. We have also developed a recommender system that suggests additions to the original bundle. Detailed analysis of the models with real-world data on computer-related products from major retailers reveals significant savings for bundle purchases, frequent opportunities to obtain freebies, and additional substantial savings that can result from the recommender system. These findings point to the viability of the proposed models for implementation consideration in current shopbot systems.

Since we are not trying to do an extensive empirical test of the effect of bundle purchasing on the saving for consumers, we only collected a small number of bundle promotions during a short period of 10 days for this paper. Savings resulting from our small experimentation should not be used as a general indicator of the true savings that could be realized by consumers in the real shopbot environment. In addition, before the current bundle searching algorithm can be implemented in the real world it must be further refined. It will require not only the refinements of the algorithm to generate the bundle set B given all formats of bundle promotions, but also the joint efforts between shopbots and retailers with respect to how bundle promotion information should be presented, updated, and made available for shopbots. In general a shopbot needs a large amount of information on various types of bundle promotions in order to be able to make recommendations to shoppers. Currently this information is not available in a way that enables automatic retrieval through current web-crawling technology, nor is it provided by any retailers through direct data feed. In our experimental analysis, the data was collected through a manual process of visiting and extensively browsing retailer websites daily. However, there are secondary sources through which the bundle promotion information could be collected, integrated, and presented in a manner facilitating automatic retrieval. One example of such a secondary source is online deal forums such as www.fatwallet.com and www.dealcoupon.com. These forums possess a large amount of information on retailer promotions and pricing posted by their members. Some forums process the raw input from their members and present it in organized and searchable formats. Bundle purchase shopbots could potentially procure relevant data from such forums as the basis for optimization and recommendation. In addition, if an appropriate mechanism can be developed to provide incentives for retailers to directly feed the deal information into the shopbots, as some retailers are currently doing with traditional shopbots, the issue of data availability can be satisfactorily resolved.

Our work can be extended in a number of ways. Our finding that the savings increase with the number of items in the bundle suggests potential benefits from aggregating various consumer purchase plans. Consideration of retailer reputation and substitutable products is also worthy of further study. Finally, while mechanisms to automate retrieval of individual item prices from a retailer exist and are in use by current shopbots, no such mechanisms exist to automate the procurement of bundle prices and promotions. While the wide variety of bundling and bundle promotion strategies used by online retailers pose significant challenges, this can contribute immensely to the popularity and usage of shopbots.

## Appendix A. Complexity analysis

Given the bundle set B, along with the vector of bundle prices, the problem of choosing an optimal subset of B is set covering, which is shown (e.g., [7]) to be NP-Hard. Of course the complexity of CB is a function of the size of the problem in terms of the number of constraints and variables. The former is determined by the cardinality of $S _ { 0 } ,$ , i.e. the number of items specified by the user. The latter can be bounded by $2 ^ { | S _ { 0 } | } - 1$ , since if two bundles contain identical elements of $S _ { 0 } ,$ the shopbot will simply choose the cheaper of the two.

## A.1. Complexity from value discounts

Consider a seller who offers a total value discount of α if the buyer spends more than a floor g. That is, the price of a set T of items is

$$
\left\{ \begin{array}{c} c (T), \text {   if   } c (T) \leq g \\ (1 - \alpha) c (T), \text {   otherwise } \end{array} \right.
$$

As before let S denote the set of all items offered by the seller and let $T _ { 0 } { : = } S \cap S _ { 0 }$ be those items in the bundle desired by the buyer. Any items purchased in $S \backslash T _ { 0 }$ have no intrinsic value except for the possible discount. If c $( T _ { 0 } ) \geq g$ the buyer will purchase only the items in $T _ { 0 } ,$ so assume that $c ( T _ { 0 } ) { < } g$ . Then let $X \subseteq S \backslash T _ { 0 }$ be the additional items purchased. To get the discount it must be true that $c ( X ) { \geq } g - c ( T _ { 0 } )$ . It is also easy to see that X must satisfy αc $( T _ { 0 } ) { \geq } ( 1 - \alpha ) c ( X )$ or else the discount does not outweigh the additional cost of X. Then the resulting problem is

$$
\min \sum c _ {i} y _ {i}\tag{7}
$$

s.t.

$$
\sum_ {i \in S \setminus T _ {0}} c _ {i} y _ {i} \geq g - c (T _ {0})\tag{8}
$$

$$
\sum_ {i \in S \setminus T _ {0}} c _ {i} y _ {i} \leq \frac {\alpha}{1 - \alpha} c (T _ {0})\tag{9}
$$

$$
y _ {i} \geq 0 \text {   and   integer,   } i \in S \setminus T _ {0}\tag{10}
$$

But even as α → 1, so that the constraint (9) becomes inoperative, the remaining problem is a minimization variation of the standard Integer Knapsack Problem, with the special property that the cost coefficients and the constraint coefficients are the same. That special case is known to be NP-Hard (see e.g. [10]).

In practice, the hard problem of finding the optimal price for a certain bundle under value discount can be solved satisfactorily by using a “filler” good to make up the gap between the current total price c(T)and the floor $g . \mathrm { ~ \ r ~ { ~ A ~ } ~ } ^ { \ast } \mathrm { f i l l e r } ^ { \ast }$ good is an item that is priced at a sufficiently low amount, such as a book mark at 25 cents, and can be used to increase the total price to barely exceed the floor g. There are numerous online bargain forums where information of such filler goods is posted for most major online merchants. These filler goods can also be programmatically retrieved by constructing customized query for the individual merchant.

## A.2. Complexity from generating the bundle set

Determination of the bundle set B to be used in solving CB, and also for the recommender system, is clearly an important issue. In general terms it follows that as the set B is expanded the solutions to CB will improve. Yet, there are two downsides to making |B| large. In general CB becomes more difficult to solve as $| B |$ increases and, in addition, there is the cost of searching the Web to find additional promotions. Finally, the size and structure of B will also be determined by the particular bundle promotions as indicated in Section 2.1. For non-deterministic bundling there may be multiple elements of B for a given promotion and set $S _ { 0 } .$ . The shopbot may simply choose to add only one element to B in these circumstances but, as shown above, choosing the cheapest such element, for at least one type of promotion, is itself an NP-Hard problem. Thus it may be useful to develop heuristic rules for the generation of B.

## References

[1] W.J. Adams, J.L. Yellen, Commodity bundling and the burden of monopoly, Quarterly Journal of Economics 90 (3) (1976) 475–498.

[2] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions, IEEE Transactions on Knowledge and Data Engineering 17 (6) (2005) 734–749.

[3] J. Bailey, Electronic Commerce: Prices and Consumer Issues for Three Products: Books, Compact Discs, and Software. 1998, Organisation for Economic Co-Operation and Development.

[4] E. Brynjolfsson, M.D. Smith, Frictionless commerce? A comparison of internet and conventional retailers, Management Science 46 (4) (2000) 563–585.

[5] DoubleClick, E-Commerce Site Trend Report Q3 2004. 2004.

[6] M.L. Fisher, L.A. Wolsey, On the greedy heuristic for covering and packing problems, SIAM Journal on Algebraic and Discrete Methods (1982) 584–591.

[7] M.R. Garey, D.S. Johnson, Computers and Interactability, Freeman, 1979.

[8] J.O. Kephart, A.R. Greenwald, Shopbot economics, Autonomous Agents and Multi-Agent Systems 5 (2002) 255–287.

[9] G. Linden, B. Smith, J. York, Amazon.com recommendations: item-to-item collaborative filtering, IEEE Internet Computing 7 (1) (2003) 76–80.

[10] S. Martello, P. Toth, Knapsack Problems: Algorithms and Computer Implementations, John Wiley & Sons, New York, 1990.

[11] A.L. Montgomery, et al., Designing a better shopbot, Management Science 50 (2) (2004) 189–206.

[12] J. Nielsen, Designing Web Usability, New Riders Publishing, Indianapolis, IN, 2000.

[13] P. Pereira, Do lower search costs reduce prices and price dispersion? Information Economics and Policy 17 (1) (2005) 61–72.

[14] Shop.org, Online Sales Skyrocket as Profitability Jumps, According to Shop.org/Forrester Research Study. 2004, Shop. org.

[15] H. Simon, G. Wuebker, Bundling—a powerful method to better exploit profit potential, in: G. Wuebker (Ed.), Optimal Bundling: Marketing Strategies for Improving Economic Performance, Springer-Verlag, Berlin, 1999, pp. 7–28.

[16] M.D. Smith, The impact of shopbots on electronic markets, Journal of the Academy of Marketing Science 30 (4) (2002) 442–450.

[17] M.D. Smith, E. Brynjolfsson, Consumer decision making at an internet shopbot: brand still matters, The Journal of Industrial Economics 49 (4) (2001) 541–558.

[18] G.J. Stigler, United States vs. Loew's Inc.: a note on block booking, Supreme Court Review (1963) 152–157.

[19] S. Stremersch, G.J. Tellis, Strategic bundling of products and prices: a new synthesis for marketing, Journal of Marketing 66 (1) (2002) 55–72.

![](/api/attachments/S685MJ3B/fulltext/images/8e1ffa7d999a6ae5664684bbfe16eca859b87d7de5883efa69384f7b7b074b6f.jpg)

Dr. Robert Garfinkel is a professor in the Operations and Information Management Department of the School of Business at the University of Connecticut. His work on a variety of problems in operations research, mainly involving combinatorial optimization, has appeared in such journals as: Operations Research; Management Science; Informs Journal on Computing; Decision Support Systems, and Mathematical Programming. His current research has focused heavily on

the problem of optimally balancing valid security concerns against the desire to provide users of a database with valuable information. Other ongoing research streams include: improving efficiency in hospital settings; design of markets for grid computing; construction of recommender systems for shopbots; optimization problems in microfluidic systems; and optimization in vehicle routing. He is also coauthor of the book Integer Programming with George Nemhauser.

![](/api/attachments/S685MJ3B/fulltext/images/88fb23ff5fb336a05fb3e0ffdf0982abc95ae46d9d95a13257749feeb9347e20.jpg)

Dr. Ram D. Gopal is currently the GE Endowed Professor of Business and an Ackerman Research Scholar. His current research interests are in the areas of data security, privacy and valuation, database management, intellectual property rights and economics of software and music piracy, online market design and performance evaluation, economics of online advertising, technology integration, and business impacts of technology. His research has appeared in

Management Science, Operations Research, INFORMS Journal on Computing, Information Systems Research, Journal of Business, Journal of Law and Economics, Communications of the ACM, IEEE Transactions on Knowledge and Data Engineering, Journal of Management Information Systems, Decision Support Systems, and other journals and conference proceedings. He currently serves as the Ph.D. director for the department and is on the editorial board of Information Systems Research, Journal of Database Management, Information Systems Frontiers, and Journal of Management Sciences.

![](/api/attachments/S685MJ3B/fulltext/images/14c19d9655eed5a1c0917abe80c5875d494622b29765b2087e9c952c3040c395.jpg)

Arvind K Tripathi is an Assistant Professor at the Management Science Department, University of Washington Business School, Seattle. He holds a Ph.D. from the University of Connecticut. His research interests are in online advertising marketing, open source software development, and electronic markets. His research has been published or forthcoming in marketing and information systems journals such as Journal of Retailing, Decision Support Systems, Communications of the ACM and IEEE Transactions on

Knowledge and Data Engineering. He serves on the editorial board of Journal of Database Management.

![](/api/attachments/S685MJ3B/fulltext/images/7a7ac1ca590c51bb00f176f29ca843bb76dc3d518bf97713d88f80e88a131b31.jpg)

Dr. Fang Yin is an Assistant Professor in the Operations and Information Management Department of the School of Business at the University of Connecticut. His research interests are in business value of IT investment, online sales promotion, shopbots design, and online recommender systems. He has published in MIS Quarterly, Journal of Retailing, Sloan Management Review, and several other journals. He holds a Ph.D. from the University of Texas at Austin.

---
otero_id: 6720
otero_key: "MVQAG232"
title: "An Economic Analysis of Customer Co-design"
authors: "Amit Basu; Sreekumar Bhaskaran"
year: "2018"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0729"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [35.176.47.6] On: 07 April 2018, At: 13:53 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## HR ms Research

## Information Systems Research

![](/api/attachments/MVQAG232/fulltext/images/a39e5d4fe300ef0dcc27e6b06103e954d51a4906287ea8ba6586a1147fa9a5b9.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## An Economic Analysis of Customer Co-design

Amit Basu, Sreekumar Bhaskaran

To cite this article:

Amit Basu, Sreekumar Bhaskaran (2018) An Economic Analysis of Customer Co-design. Information Systems Research

Published online in Articles in Advance 06 Apr 2018

https://doi.org/10.1287/isre.2017.0729

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2018, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# An Economic Analysis of Customer Co-design

Amit Basu,<sup>a</sup> Sreekumar Bhaskaran<sup>a</sup>

<sup>a</sup> Cox School of Business, Southern Methodist University, Dallas, Texas 75275

Contact: abasu@smu.edu, http://orcid.org/0000-0003-3171-2695 (AB); sbhaskar@cox.smu.edu, http://orcid.org/0000-0001-6069-1972 (SB)

Received: July 27, 2015 Revised: April 27, 2016; October 17, 2016; January 18, 2017 Accepted: April 2, 2017 Published Online in Articles in Advance: April 6, 2018

https://doi.org/10.1287/isre.2017.0729

Copyright: © 2018 INFORMS

Abstract. A key barrier to companies successfully engaging customers in the design of new products is customers fearing that they will be forced to pay much more for the custom products they help design. This fear is justified by the fact that once the customer has invested significant time and efort in co-designing a product, the firm can extract the entire consumer surplus through higher prices. At the same time, the firm allowing its customers to co-design products would be unlikely to commit to a price up front before knowing the complete design of the custom product, since it would then face a significant risk of losing money. In this paper, we develop analytical models for this problem, and show how a firm can motivate its customers to engage in co-design. We also show how ofering co-design can impact the firm’s product (line) strategies and the quality of its products, including motivating the firm to increase the quality of its standard product, sometimes even beyond the eficient quality level. The efect of market and firm characteristics on the value of engaging customers in the co-design process is also examined. In addition, we analyze the efects of (a) information asymmetry about the firm’s co-design capability, and (b) competition, on the firm’s decisions regarding codesign. These results provide valuable insights for managers considering investment in technology to support customer co-design.

History: Anindya Ghose, Senior Editor; Giri Kumar Tayi, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2017.0729.

Keywords: co-design • product lines • customization • information asymmetry • competition

## 1. Introduction

Customers play a largely reactive role in the traditional approach to new product development. Although the firm can use various market research mechanisms to understand the customers’ preferences, the ultimate design of the product is determined by the firm itself. This approach works well for mass-produced products, or “standard products.” However, interest in ofering customized products has increased, thanks to advances in production and information technologies that allow firms to cost-efectively incorporate the particular needs and preferences of customers in product design (Baldwin and von Hippel 2011). Such trends have been observed in industries ranging from automobiles, where most major manufacturers ofer a wide variety of customizable features in their products, to newspapers and magazines, where the digitization of products has led to highly personalized electronic versions of what used to be very standardized physical products.

Product customization can be achieved in various ways. One way that is well established and has been in use for millennia, is the “job shop” or “bespoke” approach, in which customers design the product they need, and the manufacturer builds the custom product to the specifications provided by the customer. This approach works well for complex products such as heavy industrial machinery and commercial construction, which are typically manufactured at relatively low scale, as well as for custom components outsourced by Original Equipment Manufacturers (OEMs), which could be at large scale. In this approach, the customer has to assemble all of the necessary design resources and expertise needed to design and specify the product in terms that can be communicated to the manufacturer.

A second approach is “mass customization,” which has gained a lot of attention over the past decade. By leveraging the rapid and cost-efective reconfiguration capabilities of production technologies such as flexible manufacturing systems (for physical products) and active online content management systems (for digital products), variants of product designs can be produced in a cost-efective manner even at a relatively high scale. In this approach, the manufacturing firm has to invest in the relevant production technologies, and possibly also in customer-facing resources that enable customers to specify their design choices, usually from a palette of preset options. A key aspect of this approach is that the customization process takes relatively little efort from the customer, since it is typically a process of selection from finite and small sets of choices. What diferentiates this approach from the job-shop approach is the ability of the manufacturer to operate at scale, even though the number of units produced for each configuration is very small.

A third approach in which the customer plays a more active role in the design of the product is the “co-design” approach, which forms the basis of this research. In this mode, the manufacturer provides a significant set of design resources to the customer, who then has the opportunity to work with these resources to help design a customized product (Thomke and von Hippel 2002, Thallmaier 2014). The starting point for this co-design process may range from a baseline template to essentially a blank page, where the customer works with designers at the firm through a possibly iterative process to develop the design.<sup>1</sup>

The three approaches impose progressively increasing capabilities on the firm, with mass customization requiring flexible manufacturing technology, while codesign requires not just that but also design and testing tools easily accessible to customers interested in participating in co-design. While co-design is not exclusive to the online setting, the ability to provide software tools for design and testing online is a significant factor in making support of co-design a practical option for the firm. In fact, such software applications are a distinct class of information systems for the firm. However, as shown in this paper, while the technical challenges of hosting such applications on the firm’s website may not be great and the firm may be able to implement them at a relatively low cost in many situations, the decision to ofer co-design software applications to customers involves some significant strategic and economic considerations beyond just the implementation costs and technical feasibility.

In developing our approach, we assume two key features about the co-design process: (1) the nature of the customer’s co-design efort may be more creative, complex, and extensive than in traditional featureselection-based customization;<sup>2</sup> and (2) the firm allowing its customers to co-design products may not commit to a price up front before knowing the complete design of the custom product, if there is significant uncertainty about the potential cost of producing the co-designed product (Thallmaier 2014).<sup>3</sup> The first assumption is important, in that the customer facing the option of engaging in co-design may not choose this option unless they feel that they will realize positive benefits from the efort. The second assumption is also important because it impacts the aforementioned customer decision regarding engagement in co-design. We will discuss both these assumptions in Appendix A.

Clearly, co-design could overcome the inherent information asymmetry that exists between manufacturers and customers in that customers know what they want, but traditionally have no efective way to let the manufacturer know that, while the manufacturer knows customer needs and preferences only at the aggregate level, and therefore has to design products that are acceptable, even though likely not ideal, for a suficient number of customers. Furthermore, modern information technology in the form of web-based software and tools for product design enables manufacturers to provide co-design capabilities that make it relatively easy for customers to engage in the design and customization process. Combined with the advances in manufacturing technologies for mass customization, co-design potentially could lead to more (fully) satisfied customers, as well as other benefits such as a reduction in inventory of unsold standard products.

An early example of this approach is the online company emachineshop.com, which ofers both of-theshelf and custom products. The company ofers a significant set of online product design and configuration tools, including sophisticated computer-aided design software, for customers to co-design and upload specifications for machined components. As another example, Ford Motor Company ofers customers of its commercial truck division an online resource called Commercial Truck Tools (CTT). Using this software, customers can custom design the truck they would like to buy, including a variety of sizes, heights, storage capacities, fixtures, storage systems, etc. Once the design is completed, it is submitted online, and Ford responds with a price quote for the configuration. Note that this is diferent from the “build your own” tools ofered by most automobile manufacturers, which are limited to choices among preset and prepriced options. Furthermore, in both examples, the firms do not commit to a price until the final design of the custom product is completed by the customer.

A likely reason for the lack of adoption of co-design is that there is a fundamental tension between the firm ofering co-design and the customer taking up the ofer to engage in co-design. The firm’s reluctance to precommit to a price is driven by the fear that the customer may design a product that is overly expensive to produce. On the other hand, the customer is unlikely to engage in co-design if they are unsure of the price they would have to pay for the final customized product after they have expended significant efort in the co-design process.

Thus, the key issue addressed in this paper is how a manufacturer capable of cost-efectively producing customized products can ofer customers the opportunity to co-design the products they want, in a way that motivates the customer to invest the necessary efort even when there is no ex ante price commitment from the firm. Using a relatively simple and stylized economic model, we (1) examine the conditions under which ofering co-design is a viable strategy for a firm; (2) demonstrate that inclusion of the co-design option for (some) elements of a product line can motivate desirable changes to the quality of even standard products ofered by the firm; and (3) analyze the impact of information asymmetry about the firm’s co-design capability and competition on the firms co-design support strategies.

The paper is organized in five sections. We start by discussing some relevant streams of past research in the next section. Then we analyze the first two claims above in various scenarios. In Section 4, we examine the efects of (a) information asymmetry about the firm’s co-design capability, and (b) the efect of the standard product being ofered by a competing firm. Finally in Section 5, we discuss the implication of our results and directions for further research.

## 2. Relevant Literature

A number of diferent streams of research reported in the literature relate to the work reported in this paper. These are discussed in turn in this section.

## 2.1. Customization and Mass Customization

A number of researchers have examined the feasibility of product customization relative to traditional product standardization geared toward mass production. The choice between customization and standardization in mass production contexts has been examined at least as far back as the 1980s (Davis 1987). The question of how to produce mass customized products has also been discussed in the literature (Anderson 2004, Zipkin 2001). With regard to the decision to customize, Dewan et al. (2003) use a circular market-based model (Salop 1979) to show that a firm that ofers customization can deter potential new entrants by increasing its range of customization. In Syam et al. (2005) and Syam and Kumar (2006), the customization strategies of competing firms are examined to show that in equilibrium, the firms are likely to adopt similar customization choices. Mendelson and Parlaktuk (2008) consider the competitive position of a firm as a factor in its choice of whether to adopt customization, and if so, what level of customization it should choose. They show that mass customization is not an efective competitive strategy for a firm that has an inferior cost or quality position. However, if firms are suficiently diferentiated to begin with, Xia and Rajagopalan (2009) show that product variety could mitigate price pressures and help firms command higher premiums.

It is also important that the customers are capable of handling the customization task; if not, a standardized product might be more profitable for a firm (Gu and Tayi 2015). As shown by Choudhary et al. (2005) and Ghose and Huang (2009), higher premiums can also be obtained through personalized pricing, which might result in higher quality levels and greater consumer welfare. Another problem in the context of customization is the challenge of understanding customer needs, and the implication of these needs in terms of the quality and/or price of customized products. Terwiesch and Loch (2004) show how progressive prototyping, particularly iterative collaborative prototyping involving both the firm and the customer, can be used to address this problem. They study the question of how many prototypes should be built, and how they, as well as the resulting customized products, should be priced.

## 2.2. Product Lines

Another stream of relevant literature examines the role and efective use of product lines. Mussa and Rosen (1978) and Moorthy (1984) show that when customers are allowed to self-select products in a product line diferentiated on quality and price, the quality of the low-preference segment is lower than the optimal level. Sometimes it might even be optimal for the firm to cripple the low-end product even if such crippling is expensive (Deneckere and McAfee 1996, Desai 2001).

One way to mitigate this cannibalization efect would be through intertemporal price discrimination in which the lower quality product is ofered only after the launch of the high-quality version (Moorthy and Png 1992). In addition, when products have multiple attributes, the subsumption efects of pure quality diferentiation can be moderated by diferentiation along additional vertical dimensions (Krishnan and Zhu 2006). Balachander and Srinivasan (1994) consider information asymmetry regarding a firm’s product quality and its impact on market entry by potential competitors. They show that an incumbent firm can signal its dominant position to potential entrants by raising quality across its product line.

These issues have also been considered in the software versioning literature, which examines the use of multiple versions of digital products such as software. Various researchers have studied versioning as a form of second-degree price discrimination. For example, Raghunathan (2000) and Bhargava and Choudhary (2001, 2008) examine when versioning is optimal and the optimal number of versions sold by a software maker.

## 2.3. Customer Co-creation

In addition to the more established notions of customization and even mass customization, there is an emerging literature on the engagement of customers in the product design process. Wind and Rangaswamy (2001) use the term “customerization” to describe active customer engagement though resources such as the Internet. Dewan et al. (2003) also recognize the possible active involvement of customers in the product design process, as well as the firm’s role in facilitating such engagement by ofering a certain level of customization capabilities. The notion of co-creation is studied in Syam and Pazgal (2013), in the context of multiple customers, and examines the efect of externalities among diferent customers as well as between the firm and customers to determine when and to what extent co-creation is beneficial. An important factor that they consider is the efect of the firm’s pricing approach on customers’ incentives to engage in cocreation. Bhattacharya et al. (2014) study the role of contractual mechanisms to motivate customer engagement when a firm uses third-party customer support centers. Customer involvement in the design process has also been studied in the context of deliberation when the customer evaluates multiple options in a product line (Villas-Boas 2009, Guo and Zhang 2012, Xiong and Chen 2013). As illustrated in these papers, the customers’ deliberation cost to evaluate multiple product options can afect a firm’s product line strategy. Similar efects are achieved through seller induced learning mechanisms such as product demonstrations and trials (Xiong and Chen 2014). Although these different streams of literature provide insights into the customization strategies adopted by firms, the focus of these papers is primarily on the firm’s customization eforts, rather than the customer’s efort.

Recently, a number of studies have examined how firms can ofer significant facilities that enable customers to co-design products that meet their unique and personalized preferences (Tseng and Piller 2011, Thallmaier 2014, Seybold 2006). While these illustrate the growing significance of co-design as a viable approach to collaborative new product development, they do not completely address the question of how customers could be motivated to participate in the codesign process. Our paper extends this literature by introducing the customers’ co-design efort as a significant consideration in the firm’s decision to ofer the option of customization, and by examining the efects of this option on the product line decisions of the firm.

## 3. Model

We consider a market consisting of two types of customers: high-end customers who are willing to pay a premium to obtain a product that meets their specific needs, and low-end customers who are less discerning and less demanding, and have a relatively low utility from the product. We denote these segments by H and L with H representing the high-end and L representing the low-end segment. Each customer in the H segment values a product of quality q at $v _ { H } q$ while the same product is valued by a customer in the L segment at $v _ { L } q$ . Based on the definition of the two segments, $v _ { H } > v _ { L } > 0$ . The total number of customers in the market is $N = n _ { H } + n _ { L } ;$ of these customers, $n _ { H }$ are of type H and the remaining $n _ { L }$ customers are of type L. We use the parameter α to represent the fraction of high-end customers, i.e., $\alpha = n _ { H } / ( n _ { H } + n _ { L } )$ . Without loss of generality, we normalize the value of N to 1.

The firm can choose to ofer either a single product or a line of distinct products for each customer segment. Let the quality of the product made available to each segment be $q _ { i } .$ We assume that the marginal cost of production incurred by the firm is convex in the level of quality of the product. Specifically, we assume that the marginal cost of production for a product of quality q is $c q ^ { 2 }$

## 3.1. No Co-design

We want to examine how the firm’s decision to ofer a product line, as well as the qualities of the product(s) it chooses to ofer, afects its customers’ decision on how much efort to invest in co-designing the firm’s product(s). We start, however, by considering a simple case in which there is no opportunity for customers to engage in co-design. Note that this case has already been analyzed in the literature, but for completeness we present the main results in this setting.

Case 1: Single Product. The profits and product quality levels ofered by the firm depend on whether the firm ofers a product line or a single product to its customers. When the firm ofers a single product, it can be targeted such that only high-end customers purchase it or such that both the high- and low-end segments purchase it. For the case in which the product is ofered only to the high-end segment, let the profits of the firm from targeting only the high-end segment be $\pi _ { 1 H } ,$ where the subscript 1 is used to refer to the case. These profits then can be represented as

$$
\pi_ {1 H} = \alpha (v _ {H} q - c q ^ {2}).
$$

This expression takes into consideration the fact that the firm extracts the entire surplus from the customer. The quality that maximizes the firm’s profits and the corresponding profits are

$$
q _ {1 H} ^ {*} = \frac {v _ {H}}{2 c}; \quad \pi_ {1 H} ^ {*} = \frac {\alpha v _ {H} ^ {2}}{4 c}.\tag{1}
$$

If the firm wants to cover both segments with its product, it has to ensure that the price is not greater than the willingness to pay of the low-end segment, so that the low-end customers participate in the market. However, the firm can still price such that the entire surplus from the low-end segment is extracted. Thus its profit function, when both the high- and low-end segments purchase the product, can be stated as

$$
\pi_ {1 L} = v _ {L} q - c q ^ {2}.
$$

The corresponding optimal product quality and profits of the firm, respectively, are

$$
q _ {1 L} ^ {*} = \frac {v _ {L}}{2 c}; \quad \pi_ {1 L} ^ {*} = \frac {v _ {L} ^ {2}}{4 c}.\tag{2}
$$

Case 2: Product Line. We now focus our attention on the case in which the firm ofers a product line consisting of a Premium (high-end) product and a Standard (low-end) product. Let $p _ { P }$ and $p _ { S }$ be the prices for premium and standard products, respectively. Since it is in the best interests of the firm to ensure that the high-end segment purchases the premium product, the prices should be such that the high-end customer receives a greater surplus by purchasing the premium product than by purchasing the standard product. So if the quality levels of the premium and standard product are $q _ { P }$ and $q _ { S } ,$ , respectively, the prices of these products will be

$$
\begin{array}{r l} & p _ {2 S} = v _ {L} q _ {S}, \\ & p _ {2 P} = v _ {H} q _ {P} - v _ {H} q _ {S} + v _ {L} q _ {S} \\ & \qquad = v _ {H} q _ {P} - (v _ {H} - v _ {L}) q _ {S}. \end{array}
$$

Once again, the firm extracts the entire surplus from the low-end segment. Thus the profit function of the firm as a function of $q _ { P }$ and ${ q } _ { S } ,$ which are the quality of the premium and standard products, respectively, can be stated as

$$
\pi_ {2} = \alpha (v _ {H} (q _ {P} - q _ {S}) + v _ {L} q _ {S} - c q _ {P} ^ {2}) + (1 - \alpha) (v _ {L} q _ {S} - c q _ {S} ^ {2}).
$$

Therefore the optimal quality levels for the two products in this scenario will be

$$
q _ {2 P} ^ {*} = \frac {v _ {H}}{2 c},\tag{3}
$$

$$
q _ {2 S} ^ {*} = \frac {v _ {L} - \alpha v _ {H}}{2 c (1 - \alpha)}.\tag{4}
$$

Furthermore, the profits of the firm are given by

$$
\pi_ {2} ^ {*} = \frac {\alpha v _ {H} ^ {2} - 2 \alpha v _ {H} v _ {L} + v _ {L} ^ {2}}{4 c (1 - \alpha)}.\tag{5}
$$

Proposition 1. If the firm does not ofer a co-design option, we have the following:

1. There exists a threshold on the willingness to pay of the high-end segment, $\bar { v } _ { H } ,$ above which the firm ofers a single product that is targeted exclusively to the high end. Below this threshold, the firm ofers a product line.

2. $\bar { v } _ { H }$ is decreasing in α and increasing in $v _ { L }$ .

Proof. All proofs are provided in the online appendix.

This is illustrated in Figure 1. The decision of the firm to either ofer a product line or single product, quite predictably, depends on the willingness to pay of the high-end segment. A product line approach enables the firm to obtain greater market coverage, which however comes with the threat of cannibalization. The presence of the standard product constrains the firm’s ability to charge more for the premium product. As a result, for a suficiently high willingness to pay for the high-end customers, it is in the best interests of the firm to eliminate cannibalization by ofering only the premium product, and focusing only on the high-end market segment. Consistent with intuition, an increase in the proportion of high-end customers <sup>(</sup>α<sup>)</sup> or a decrease in the willingness to pay of low-end customers $\left( v _ { L } \right)$ increases the attractiveness of the single product strategy.

Figure 1. (Color online) Efect of Customer Valuation of Product Quality  
![](/api/attachments/MVQAG232/fulltext/images/901082621710b760f7377cb914b2f2d3844a2fcba54b3557fc452ab31784308c.jpg)

When the firm indeed ofers a product line, it crimps the quality of the standard product to make it an unattractive choice for the high-end segment. So while the high-end segment receives eficient quality (used to denote the quality level a firm would ofer a customer segment if it were the only one targeted, unconstrained by cannibalization from other segments; Krishnan and Zhu (2006), the low-end segment is ofered a product whose quality is strictly below the eficient level.<sup>4</sup>

## 3.2. Co-design

We now consider the scenario in which the firm ofers its customers the opportunity to co-design the product along with the firm. By engaging in co-design, the customer is able to develop a product that uniquely suits her requirements; consequently, the customer will be willing to pay more for such a product.

We capture this efect as follows: In the absence of the co-design option, the willingness of each customer segment i to pay for a given level of product quality is $v _ { i } .$ However, if the customer engages in co-design, the willingness to pay increases by a factor θ; thus the willingness to pay of the customer in segment i becomes $( 1 + \theta ) v _ { i }$ . Note that we model co-design as changing the subjective value of the customized product to the participating customer rather than the objective quality of the product to all customers. As stated by Abbott, vertical diferentiation of quality occurs when “the ‘superior’ of any two qualities is considered preferable by virtually all buyers,” while horizontal diferentiation in quality occurs when “diferent people will rank dissimilar qualities in diferent order” (Abbott 1953, p. 828). We recognize that the result of customer codesign may in some cases also increase the general quality of the product as well, but our assumption is that the intention of the customer is to improve the subjective value of the product for themselves, rather than to improve its general quality. This subjective change in the value of a product caused by co-design is consistent with Abbott’s view of horizontal diferentiation, which is why we model the efect of co-design as a change in the specific customer’s willingness to pay.

This increase in willingness to pay for a co-designed product depends on the co-design efort committed by the customer as well as the firm’s co-design capability— which represents the set of co-design support features and facilities ofered by the firm to facilitate the customer’s co-design eforts. Such facilitation of co-design through the provision of design tools is illustrated in the examples cited earlier of Ford trucks and emachineshop.com, and is also discussed in Seybold (2006), Thallmaier (2014), and Tseng and Piller (2011). It is reasonable to assume that θ is increasing in both customer efort as well as firm capability, and for analytical tractability we assume the specific functional form $\theta =$ $\phi \times \gamma .$ , where $\phi$ is the firm’s co-design capability and γ is the co-design efort of the customer. We also assume that the cost incurred by the customer engaging in a co-design efort γ is convex of the form $\kappa \gamma ^ { 2 }$

Our assumption that co-design efort increases the customer’s willingness to pay for the product implies that the customer is able to tailor the product more closely to her preferences. This approach allows us to gain the same insights as a more complex model such as one that assumes customer preferences distributed along a Hotelling line. Furthermore, our model is also general enough to accommodate contexts where an increased willingness to co-design products is motivated by the pride associated with the “I designed it myself” efect (Thomke and von Hippel 2002, Franke et al. 2010).

The sequence of decision making is as follows: The firm decides whether to engage the customers in codesign, and determines the quality of the products it would like to make available to the customers. The customer then decides how much efort to put into the co-design process, and this determines the willingness to pay for the products that they choose to buy. Finally, after the co-design process is completed, the firm announces the price(s) for the product(s) and the customer decides which of the products she would like to purchase from the firm.

This assumption of deferred price commitment is reasonable because it is unrealistic to expect the firm to set a price for a product before it knows the product’s final form and features and therefore its production cost. To further demonstrate the validity of this assumption, in Appendix A we examine the question of when the price should be set, if the production cost of the co-designed product is uncertain. Even in this more complex model, we are able to show that the firm is indeed often better of by setting the product’s price after the co-design process is complete.

Case 3: Single Product. First, consider a scenario where the firm ofers a single product of quality q and in addition, allows the customer the option of customizing it through co-design. When the customer of segment $i \in [ H , \breve { L ] }$ purchases the co-designed product, the utility she receives would increase from $v _ { i } q$ to $( 1 + \theta ) v _ { i } q$ . Since the firm has to defer its pricing decision for the co-designed product until after the customer has incurred the cost $\kappa \gamma ^ { 2 }$ to co-design the product, it can extract (almost) all of the surplus from the customer. The customer, anticipating this opportunistic behavior of the firm, will therefore choose not to engage in co-design. It follows that the profits that the firm is able to generate for this scenario would be identical to those in Case 1.

We formally state this result in the following proposition.

Proposition 2. Co-design is infeasible in the single product scenario.

Case 4: Product Line. Now we consider the scenario in which the firm, in addition to the premium product, also ofers a standard product. $\mathrm { A s }$ in Case 2, let the quality of the premium product be $q _ { P }$ and that of the standard product be $q _ { S } .$ The efect of the co-design process is to increase the customer’s willingness to pay for the product they purchase.

A key premise in our approach is that the efect of co-design is to increase the customer’s willingness to pay for quality, rather than increasing the quality itself. The rationale for this is that as the customer engages in the co-design efort, not only do they tailor the design to their needs, but they also gain a greater appreciation for the benefits. Thus, even at the same level of product quality, their willingness to pay is enhanced by the factor θ. Thus, when a customer of type $i \in [ H , \check { L } ]$ participates in the co-design process, her willingness to pay for either product increases to $( 1 + \theta ) v _ { i }$ . As a result, the utility that she would obtain from the product $j \in [ P , S ]$ can be written as

$$
u _ {i j} = (1 + \theta) v _ {i} q _ {j}.\tag{6}
$$

When the firm ofers the product line, it would like the customers to self-select such that the high-end customer chooses the premium product while the lowend customer purchases the standard product. This can be ensured if the price of the standard product is no greater than the utility that the low-end customer obtains from it (participation constraint), while the price of the premium product is such that the highend segment obtains a greater utility from purchasing it instead of the standard product (incentive compatibility constraint).

Lemma 1. The low-end customer will not engage in $c o \mathrm { - }$ design in the product line scenario.

As in the single product case, when the firm prices the products optimally, it will have an incentive to extract out the entire surplus from the low-end customers. This perverse incentive of the firm causes the low-end customer to not engage in co-design. The implication of this lemma is that the price of the standard product will be as follows:

$$
p _ {4 S} = u _ {S} = v _ {L} q _ {S}.
$$

If the high-end segment engages in co-design, the incentive compatibility constraint implies that the price of the premium product will be

$$
\begin{array}{r l} & p _ {4 P} = u _ {H P} - (u _ {H S} - p _ {4 S}) \\ & \quad = (1 + \theta) v _ {H} q _ {P} - ((1 + \theta) v _ {H} q _ {S} - v _ {L} q _ {S}) \\ & \quad = (1 + \theta) v _ {H} (q _ {P} - q _ {S}) + v _ {L} q _ {S}. \end{array}
$$

The entire utility of the high-end segment $( ( 1 + \theta ) v _ { H } q _ { P } )$ is not extracted by the firm through this pricing decision; hence, the high-end segment will always find it to be valuable to engage in co-design. The extent of this engagement is reflected in the customer’s co-design efort.

Note that, as reflected in Equation (6), we assume that the customer’s willingness to pay for both the premium and standard products increases as a result of their co-design efort. The rationale for this is that when the customer invests in co-design efort, it also refines their appreciation of and, therefore, willingness to pay for the standard product. Thus co-design enables a potential customer the opportunity to “learn by doing.” This learning then translates into a better appreciation of the utility of the diferent features of the standard product and would not have been possible without co-design efort. In the context of the Ford trucks example described earlier, if a customer puts in efort to design a customized version, she also gains a better understanding of how to use the standard version of the truck. Consequently, the co-design efort results in some residual value even if she ends up buying the standard product. Note that, if this assumption does not hold, then the presence of a standard product is insuficient to motivate co-design.

The net surplus of the customer for a given level of efort γ is the diference between the utility she derives from the product and the price she has to pay for it. The customer will choose an efort level that will maximize the net surplus she is able to obtain from the transaction while taking into consideration the cost of efort $\kappa \gamma ^ { 2 }$ . Let $\lambda ( \gamma )$ be the net surplus of the high-end customer; it follows that

$$
\begin{array}{r l} & {\lambda (\gamma) = u _ {H P} - p _ {4 P} - \kappa \gamma^ {2}} \\ & {\quad = (1 + \phi \gamma) v _ {H} q _ {P} - p _ {4 P} - \kappa \gamma^ {2}} \\ & {\quad = q _ {S} ((1 + \phi \gamma) v _ {H} - v _ {L}) - \kappa \gamma^ {2}.} \end{array}\tag{7}
$$

Proposition 3. The optimal co-design efort of the high-end customer is given by

$$
\gamma^ {*} = \frac {q _ {S} v _ {H} \phi}{2 \kappa}.\tag{8}
$$

In addition, $\gamma ^ { * }$ is increasing in $v _ { H } , q _ { S }$ , and $\phi .$ .

Unlike in Case 3 where the firm ofers only a single product, the customer now finds it to be worthwhile to engage in co-design when both a premium and a standard product are ofered. In efect, the standard product serves as a fallback option for the customer in case the firm chooses to gouge the customer by overpricing the co-designed premium product. As a result, the optimal efort of the customer is increasing in ${ q } _ { S } ,$ which is the quality of the standard product. As $q _ { S }$ increases, so does the value of the fallback option from the standard product, as a result of which the customer is motivated to commit more efort on co-design. Consistent with intuition, this efort is also increasing $v _ { H } ,$ which is the willingness of the customer to pay for quality, as well as $\phi ,$ which is the firm’s co-design capability. This result is consistent with Dewan et al. (2003), who show that ofering a standard product in addition to customized products can improve market coverage and lead to higher profits. However, they do not consider the customer’s efort in the customization process, and thus the role of the standard product in their context is diferent.

Having determined the optimal co-design efort of the customer, we now turn our attention to the firm’s decision with respect to the quality level of the standard and premium products. The firm’s profit function when it ofers both products and customers self-select as above can be represented as

$$
\pi_ {4} = \alpha (p _ {4 P} - c q _ {P} ^ {2}) + (1 - \alpha) (p _ {4 S} - c q _ {S} ^ {2}).
$$

Substituting the optimal efort and the corresponding prices for both products into the above profit function, we obtain that

$$
\begin{array}{l} \pi_ {4} (q _ {P}, q _ {S}) = q _ {S} (v _ {L} - c q _ {S}) \\ \qquad - \frac {\alpha (q _ {P} - q _ {S}) (2 c \kappa (q _ {P} + q _ {S}) - v _ {H} (2 \kappa + q _ {S} v _ {H} \phi^ {2}))}{2 \kappa}. \end{array}
$$

The optimal quality levels for both products can be determined by diferentiating the profits with respect to (w.r.t.) $q _ { P }$ and $q _ { S }$ and these are as below

$$
q _ {4 P} ^ {*} (\phi) = \frac {2 \kappa v _ {H} (v _ {H} \phi^ {2} (\alpha v _ {H} + v _ {L}) + 4 (1 - \alpha) c \kappa)}{1 6 (1 - \alpha) c ^ {2} \kappa^ {2} + 8 \alpha c \kappa v _ {H} ^ {2} \phi^ {2} - \alpha v _ {H} ^ {4} \phi^ {4}},\tag{9}
$$

$$
q _ {4 S} ^ {*} (\phi) = \frac {2 \kappa (\alpha v _ {H} ^ {3} \phi^ {2} + 4 c \kappa v _ {L} - 4 \alpha c \kappa v _ {H})}{1 6 (1 - \alpha) c ^ {2} \kappa^ {2} + 8 \alpha c \kappa v _ {H} ^ {2} \phi^ {2} - \alpha v _ {H} ^ {4} \phi^ {4}}.\tag{10}
$$

Having determined the optimal quality level for the premium and standard products, we now examine how these quality levels are afected by changes in market and product characteristics.

Proposition 4 (Efect of Customer Valuation). 1. $q _ { 4 P } ^ { * }$ is increasing in $v _ { H }$ and $v _ { L } .$

2. $q _ { 4 S } ^ { * }$ is increasing in $v _ { L }$ . By contrast, $q _ { 4 S } ^ { * }$ is nonmonotonic in $v _ { H } ;$ in addition, $q _ { 4 S } ^ { * }$ is decreasing in $v _ { H }$ when $v _ { H }$ is low and increasing in $v _ { H }$ when $v _ { H }$ is $h i g h .$

This proposition is illustrated in Figure 2. It implies that the optimal quality of the premium product is increasing in both the valuation of the high- and lowend customer segments. A higher valuation of both of these segments serves two objectives: an increase in the marginal return from higher product quality as well as a decrease in the level of cannibalization from the low-end segment. First, because the high-end customer segment is willing to spend more on quality, it becomes worthwhile for the firm to ofer better quality for the premium product. Second, the higher valuation of the low-end customers $\left( v _ { L } \right)$ increases the price that a firm can charge for the standard product, which in turn mitigates the efect of cannibalization from that product. This same increase in low-end customer valuations similarly increases the optimal product quality of the standard product as well.

Figure 2. (Color online) Efect of Customer Valuation of Product Quality  
![](/api/attachments/MVQAG232/fulltext/images/73533f18fc2c778780cc932225f3515c1f75f536eb749142ab100b3ee6fa08ac.jpg)

By contrast, the efect of higher $v _ { H }$ on the optimal quality of the standard product is less straightforward. Depending on whether the valuation of the high-end customer segment is high or low, a further increase in their valuation can increase or decrease the optimal quality of the standard product, because of two opposing efects. On one hand, an increase in $v _ { H }$ increases the value of the high-end segment for the firm; as $v _ { H }$ increases, the firm seeks to consolidate this value by crimping the quality of the standard product, which helps to reduce the efect of cannibalization. As a result, as $v _ { H }$ increases, the firm is tempted to reduce the quality of the standard product (Mussa and Rosen 1978, Moorthy 1984). However, in the presence of the codesign option, the firm also needs to consider the efect of the quality of the standard product on the customer’s incentive to participate in the co-design process. As detailed in Proposition 3, the optimal efort of the customer is increasing in the quality of the standard product. The value of this higher efort is also greater when the willingness to pay of the high-end segment is higher. Because of this, above a suficiently high value of $v _ { H } .$ , a further increase in $v _ { H }$ calls for a higher quality standard product. Indeed, this result illustrates the tension between the need to mitigate cannibalization in conjunction with the imperative to incentivize the customers to participate in the co-design process.

In the above analysis, we have assumed that when the co-design option is ofered, the utility derived by a high-end customer from the standard product of quality $q _ { S }$ is $( 1 + \theta ) v _ { H } q _ { S }$ . This is based on the reasonable assumption that when a customer puts in efort to customize a product, she gains a better understanding of the product line that leads to a greater appreciation for the standard product as well. Again, considering the

![](/api/attachments/MVQAG232/fulltext/images/1b42885c2d141fa7187536a340f20f08df2c45ba20d0a2904e185d4b54e9320d.jpg)  
- = 0.3; c = 1; v = 1; k = 4

Ford truck example, a customer trying to customize a truck may, at the end of the process, better appreciate the features of the standard configuration of the truck as well, thereby gaining more utility from $\mathrm { i t . } ^ { 5 }$ However, this increased willingness to pay for the standard product in itself is not the reason why the optimal quality for the standard product is higher in the presence of the codesign option. If that were so, we would expect to see a similar efect when $v _ { H } ,$ , the high-end customer’s valuation for the standard product is higher, even without co-design. However, this is not true. The optimal quality of the standard (low-end) product in the traditional product line literature is $( v _ { L } - \alpha v _ { H } ) / ( 2 c ( 1 - \alpha ) )$ <sup>)</sup>. So any increase in $v _ { H }$ results in a lower optimal quality for the standard product, which reduces cannibalization.

Proposition 5 (Efect of α). The optimal quality $q _ { 4 j } ^ { * }$ is increasing in α only if κ is below a threshold. $q _ { 4 j } ^ { * }$ is decreasing in α otherwise.

This is illustrated in Figures 3 and 4. It characterizes the efect of α, which represents the relative size of the high-end segment of the market, on the optimal quality of both products. Interestingly, we find that its efect depends on the co-design cost of the customer, $\mathrm { i . e . , }$ whether it is high or low. When this cost is low (low κ), the firm should optimally increase the quality of both products when there is an increase in the size of the high-end segment. By contrast, when the customer’s co-design cost is high (high κ), an increase in α pushes the optimal qualities in the opposite direction.

To understand these results, it is useful to examine the efect of an increase in α on the relative significance of the high- and low-end customer segments. As α increases, the firm’s decisions are increasingly focused on the value that can be derived from the highend segment. An increase in the quality of the standard product has two diametrically opposing efects. On one hand, a higher standard product quality serves to increase the high-end customer’s incentive to engage in co-design and invest in greater co-design efort. At the same time, this higher standard product quality can also intensify the cannibalization of the premium product by the standard product.

Figure 3. (Color online) Efect of α on Optimal Co-designed Product Quality  
![](/api/attachments/MVQAG232/fulltext/images/0e1a8650e733f0b8ec67491d3c4813ccddd78abe1fbf1a3da121f55dd9374dcf.jpg)

The relative strength of these two efects determine the firm’s optimal response to an increase in α. When κ is suficiently low, the marginal return from a co-design efort of the customer is much higher. As a result, the firm finds it to be more profitable to increase the quality of the standard product and incentivize the customer to commit a higher level of efort on co-design. This higher co-design efort also increases the value from the premium product and hence the quality of the premium product as well. On the other hand, when κ is suficiently high, the return from customers’ efort into co-design is too low to overcome the efect of cannibalization. As a result, an increase in α pushes the firm to reduce the quality of the standard product as a means to reduce cannibalization. The lower standard product quality now allows the firm to charge more for the premium product. However, since the customer’s efort is also lower in this scenario, the quality of the premium product also sufers. Thus, as α increases, the optimal quality of both premium and standard products go down.

Proposition 6. The efect of co-design capability φ: $q _ { 4 j } ^ { * }$ is increasing in φ.

The implication of this proposition is relatively easy to see, and the efect of the firm’s co-design capability on the optimal quality levels of both products is consistent with intuition. Higher co-design capability supported by a firm encourages a greater level of co-design efort from the customers, which in turn translates to a higher quality for both products.

![](/api/attachments/MVQAG232/fulltext/images/b27408fd67e75ffbd617e0a4e69b969303357f881d28aa807952b91d666496d7.jpg)

Figure 4. (Color online) Efect of α on Optimal Standard Product Quality  
![](/api/attachments/MVQAG232/fulltext/images/c1018ae1e6e36e10f0c80f63dd219bf19326ec5af95a3dc8e346ffa5ebf5a147.jpg)

Proposition 7 (Efect of Co-design on Product Quality). 1. $q _ { 4 j } ^ { * } \geq q _ { 2 j } ^ { * } ,$ i.e., the firm ofers higher standard and premium quality products when customers have the option of co-design.

2. There exists a threshold on φ above which $q _ { 4 S } ^ { * } > q _ { 1 L } ^ { * } ,$ i.e., low-end customers obtain a quality that is even greater than the eficient quality for that segment.

We find that when the firm ofers the co-design option to customers, the optimal quality of both products is higher. The option to co-design allows a customer to fine-tune the premium product to her particular needs and increases her valuation for that product. This in turn increases the marginal value that the firm can derive from its quality investments for the premium product and thus increases the optimal quality of the premium product.

In addition to the direct efect on the premium product quality, the option of co-design also indirectly afects the quality of the standard product. A higher quality of the standard product can encourage customers to invest more efort into the co-design process; this efect increases the optimal quality of the standard product. Indeed, this efect can be so strong that the firm might even ofer a standard product whose quality can be higher than the eficient quality. However, for this to be the case, we find that the firm’s codesign capability needs to be suficiently high. In this region, the high marginal return from customers’ codesign efort mitigates the cannibalization threat from the standard product. As a result, the firm finds it optimal to raise the standard product quality to a level that is even beyond the eficient quality, as illustrated in Figure 5.

![](/api/attachments/MVQAG232/fulltext/images/9554d3e6389e5b7d306884624a14470b2ccba054a739a1708d41cfc1a55f732a.jpg)

This result is particularly interesting because it runs counter to the conventional wisdom from the product line literature. As described in Moorthy (1984), Moorthy and Png (1992), and Mussa and Rosen (1978), when a firm ofers a product line, it seeks to mitigate the potential cannibalization efect by reducing the quality of the low-end ofering. The lower quality discourages the high-end segment from settling for this option. By contrast, when a firm ofers codesign options to its customers, the same motivation to increase the profitability of the high-end segment encourages the firm to increase the quality of the lowend ofering (standard product). Thus, the cannibalization efect is superseded by the benefit derived through customer co-design.

Figure 5. Efect of Co-design on Standard Product Quality  
![](/api/attachments/MVQAG232/fulltext/images/18fc1e6c5eefd7dd65c935f52821e009c07ca8d541a9119b0a4c5310da244ad9.jpg)

It is also useful to compare our results with Dewan et al. (2003), who show that a monopolist manufacturer might find it optimal to ofer both standard and customized products as a means to enable higher but eficient market coverage. They also show that the firm might find it optimal to ofer a level of customization far greater than what the customers themselves might prefer. By contrast, in our paper, the level of co-design is decided by the customer herself and her incentives therein are influenced by the firm’s co-design capability as well as its product line choices. Moreover, the customers are strictly better of both because they get a better quality product and because their greater efort leads to a higher willingness to pay for quality.

While, like Dewan et al. (2003), we have assumed a monopolistic firm, it is also useful to consider whether our results would change if the standard product is ofered by a competitor. Even in this setting, as shown later in Section 4.2, an increase in the quality of the standard product will have a positive impact on a firm’s ability to motivate co-design efort from the customer. An interesting implication of this result is that investing in information technology to support customer co-design can help a firm even when a competitor that ofers a standard product increases the quality of that product.

## Optimal Strategy of the Firm

As we showed earlier, to motivate co-design, the firm has to ofer a product line. This is because without a product line, the ability of the firm to extract all of the surplus from the customer after she puts in the codesign efort, discourages her to even engage in this process. However, although a product line allows a firm to engage the customer, the resulting cannibalization still constrains the firm’s pricing power. One option for the firm in this situation would be to ofer just a single product that is targeted only toward the high-end segment as in Case 1. While this option lacks the involvement from the customers through codesign, it also does not sufer from the cannibalization efect in a product line. In the following proposition, we determine when the firm would find it optimal to ofer a product line and furthermore, when to engage the customer in the co-design process.

Proposition 8 (Optimal Co-design Strategy). 1. There exists a threshold on κ above which single product strategy dominates co-designed product line. This threshold is decreasing in α.

2. The range of parameters for which a product line is optimal increases when the firm ofers customers the option of co-design.

The first part of the proposition underscores the critical role played by the customer’s co-design cost <sup>(</sup>κ<sup>)</sup> in the firm’s decision to ofer a product line. When this cost is suficiently low, co-design encouraged through the ofering of product lines becomes a viable strategy for the firm. However, if this cost is too high, a single product strategy becomes the preferred option. Essentially, the presence of the low-end standard option helps motivate the customer to participate in the codesign process and its value increases as the customer’s co-design cost decreases. This efect is further moderated by the size of the high-end segment. As the proportion of high-end customers increases, the single product option becomes preferable at lower levels of co-design cost. The firm in this situation is balancing the need to encourage its customers to participate in codesign with its desire to manage cannibalization. When α becomes larger, a single product helps the firm eliminate cannibalization and derive higher profits from the larger high-end segment.

The second part of the proposition illustrates an important efect of co-design in a firm’s product strategy. The presence of co-design option increases the range of parameters for which a firm should ofer a product line to its customers. Figure 6 shows that the co-design option motivates the firm to ofer a product line in the intermediate region in which it would otherwise have ofered only a single product targeted at the high-end segment. Thus, the possibility of co-design encourages the firm to ofer broader coverage of the market. In addition, the value of this higher coverage is greater when the customer’s cost to co-design is lower.

Figure 6. (Color online) Optimal Co-design Strategy  
![](/api/attachments/MVQAG232/fulltext/images/17fe5c10e23bbf583d03c2b534161bf343bdf532e4d2720240021ce541db0cd2.jpg)

## 4. Information Asymmetry and Competition

In developing the models in Section 3, we have made a number of assumptions. In this section, we extend our analysis to examine how our models and results would be afected by relaxing a couple of key assumptions. We start by considering the possibility of information asymmetry between the firm and customers about the firm’s co-design capability. We then consider the situation where the standard product is not ofered by the firm itself, but by a competing firm.

## 4.1. Informational Asymmetry About a Firm’s Co-design Capability.

We have so far assumed that customers know the codesign capability (henceforth referred to as capability) of the firm. In reality, until the customer invests significant efort into the co-design process, they may not be aware of the true level of a firm’s capability. At the same time, the firm may also be unable to reliably communicate its capability level to customers since every firm might find it to be beneficial to claim that it ofers high co-design capabilities.

In this section, we explicitly account for this possibility that customers are not able to reliably distinguish between a high and low-capability firm. We model this by assuming that the firm can be one of two types: an h type firm that has a high co-design capability $\phi _ { h }$ or an l type firm with a low co-design capability $\phi _ { l }$ where $\phi _ { h } > \phi _ { l } > 0$ . The customer does not know with certainty which type of firm she is interacting with (high capability or low capability) and knows only the probability associated with the diferent types. In particular, she knows that the firm is of h type with probability ω (and correspondingly, of type l with probability $1 - \omega )$ . We define $\bar { \phi } = \omega \bar { \phi _ { h } } + ( 1 - \bar { \omega } ) \phi _ { l }$ , as the expected value of the firm’s capability.

We start by examining the “full-information” scenario in which the customer is able to identify the type of the firm with which she is dealing. In this scenario, when the customer knows that she is dealing with a high- (low-) capability firm, she would invest in a high (low) level of efort that is consistent with the analysis in Section 3 (Equation (8)), which will be

$$
\gamma_ {F} (\phi_ {i}; q _ {S}) = \frac {q _ {S} v _ {H} \phi_ {i}}{2 \kappa}.\tag{11}
$$

The firm, anticipating this response from the customer would also choose to ofer quality levels in accordance with its capability level, as determined earlier (and repeated below for ease of exposition)

$$
q _ {F P} ^ {*} (\phi_ {i}) = \frac {2 \kappa v _ {H} (v _ {H} \phi_ {i} ^ {2} (\alpha v _ {H} + v _ {L}) + 4 (1 - \alpha) c \kappa)}{1 6 (1 - \alpha) c ^ {2} \kappa^ {2} + 8 \alpha c \kappa v _ {H} ^ {2} \phi_ {i} ^ {2} - \alpha v _ {H i} ^ {4} \phi^ {4}},\tag{12}
$$

$$
q _ {F S} ^ {*} (\phi_ {i}) = \frac {2 \kappa (\alpha v _ {H} ^ {3} \phi_ {i} ^ {2} + 4 c \kappa v _ {L} - 4 \alpha c \kappa v _ {H})}{1 6 (1 - \alpha) c ^ {2} \kappa^ {2} + 8 \alpha c \kappa v _ {H} ^ {2} \phi_ {i} ^ {2} - \alpha v _ {H} ^ {4} \phi_ {i} ^ {4}},\tag{13}
$$

where $i \in [ h , l ]$ . The corresponding optimal co-design efort of the high-end customer for these quality levels is then $\gamma _ { F } ^ { * } ( \phi _ { i } ) \bar { = } \gamma _ { F } ( \phi _ { i } ; q _ { F S } ^ { * } ( \phi _ { i } ) )$

Now, consider a setting in which the customer is not certain about the firm’s capability. This would occur if, in equilibrium, the low-capability firm finds it optimal to present itself to the customer as a high-capability firm, by mimicking the high-capability firm’s strategy $( { \mathrm { i . e . } }$ , ofer the same quality levels as a high-capability firm), and furthermore, if the high-capability firm also finds it to be too expensive to ofer quality levels that will diferentiate itself from the low-type firm. In the absence of any information that resolves this uncertainty, the decision of the customer with respect to the efort on co-design depends on the expected surplus that she obtains through the co-design process. As shown in Proposition 3, the optimal co-design efort is increasing in the firm’s capability. Given the uncertainty about the firm’s capability under information asymmetry, the customer will be hesitant to invest much efort in the co-design process because of the fear that it might be dealing with a low-capability firm. We refer to this scenario as the pooling equilibrium. Note that this situation is similar to the lemons’ market problem (Akerlof 1970), in that the customer will be unwilling to invest co-design efort beyond that appropriate for an “average” capability firm.

This leads to the natural question of whether a high-capability firm can reliably signal its type to a customer in a way that would not be mimicked by a low-capability firm. This resolution of information asymmetry will then encourage the customer to put in a high level of efort into the co-design process when dealing with the high-capability firm. We refer to this scenario as the separating equilibrium.

Let $\pi _ { d l 2 } \left( \pi _ { d l 1 } \right)$ be the profits of the low-capability firm when it does (not) mimic the quality levels of the highcapability firm. In addition, let $q _ { d h i } ^ { * }$ (where $i \in \{ P , S \} )$ be the optimal quality levels ofered by the high-capability firm when the low-capability firm does not mimic. The expressions for these terms and the associated equilibria are discussed in detail in Appendix B. The analysis of the equilibria allows us to characterize conditions under which the high-capability firm will be able to signal its capability levels, as illustrated in the following proposition.

Proposition 9. Let us suppose that $\pi _ { d l 2 } ( q _ { P } ^ { * } ( \phi _ { h } ) , q _ { S } ^ { * } ( \phi _ { h } ) ) >$ $\pi _ { d l 1 } ( q _ { P } ^ { * } ( \phi _ { l } ) , q _ { S } ^ { * } ( \phi _ { l } ) )$ . Then there will be a separating equilibrium in which the optimal product quality levels of both firms will be as follows:

$$
\begin{array}{r l} & 1. q _ {d h P} ^ {*} > q _ {P} ^ {*} (\phi_ {h}) \mathrm{and} q _ {d h S} ^ {*} > q _ {S} ^ {*} (\phi_ {h}); \\ & 2. q _ {d l P} ^ {*} = q _ {P} ^ {*} (\phi_ {l}) \mathrm{and} q _ {d l S} ^ {*} = q _ {S} ^ {*} (\phi_ {l}). \end{array}
$$

Proposition 9 characterizes the optimal product quality for both products under a separating equilibrium in which a high-capability firm is able to signal its type to customers. In this equilibrium, we find that the high-capability firm ofers quality levels that are higher than what it would have ofered under a full information scenario. If the quality levels set by the firm were at the optimal levels for a high-capability firm in the full information scenario, the customer would not be confident that she was dealing with a high-capability firm, since it would also be worthwhile for a low-capability firm to ofer these levels to mimic a high-capability firm. By ofering quality levels that are even higher, the high-type firm makes it prohibitively expensive for the low-type firm to masquerade as a high-type firm. Although the low-capability firm would be able to induce a higher level of efort from the customer by mimicking, the customer would realize the true lower capability level of the firm after putting in efort on codesign, and would then be unwilling to pay as high a premium as she would to a true high-capability firm. Thus, in efect, under the conditions stated in Proposition 9, the high-capability firm will be able to overcome the information asymmetry challenge and reliably signal its type to customers.

An implication of this result is that the presence of information asymmetry, the quality of standard products ofered to customers will be higher even more often than under full information conditions; furthermore, this quality level may sometimes be even higher than the eficient quality. Thus, in some sense, the role of product lines in motivating co-design and higher quality products becomes even more significant under information asymmetry.

Figure 7 illustrates how some parameters afect the type of decision spaces under information asymmetry. When the cost of quality <sup>(</sup>c<sup>)</sup> and the probability of the firm being a high-capability type <sup>(</sup>ω<sup>)</sup> are low, it is optimal for each type of firm to set quality levels consistent with the full-information scenario, thus enabling the customer to recognize the firm’s capability level. As c and ω increase, it becomes worthwhile for a low-capability firm to mimic the quality levels of a high-capability firm. This is the scenario of Proposition 9, and as shown above, the high-capability firm can resolve the customer’s uncertainty by raising its quality levels even higher. Finally, when c and ω increase still further, the cost of signaling becomes so prohibitive that a pooling equilibrium becomes the preferred outcome.

Figure 7. (Color online) Equilibria Under Informational Asymmetry  
![](/api/attachments/MVQAG232/fulltext/images/e82ae60551806d53230aa86557d5c7d8877f3d058c7160e8826ad09ae23e5bdb.jpg)

It is also interesting to note that under the conditions of Proposition 9, the optimal co-design efort of the customer is also afected, as illustrated in the following corollary.

Corollary 1. The optimal efort of the customer could be higher in the information asymmetry scenario, $i . e . , \gamma _ { d h } ( \phi _ { h } ;$ $q _ { d h S } ^ { ^ { - } } ) \geq \gamma _ { F } ( \phi _ { h } ; q _ { F S } ^ { * } ( \phi _ { h } ) )$ , when $\pi _ { d l 2 } ( q _ { P } ^ { * } ( \phi _ { h } ) , q _ { S } ^ { * } ( \phi _ { h } ) ) \ >$ $\pi _ { d l 1 } ( q _ { P } ^ { * } ( \phi _ { l } ) , q _ { S } ^ { * } ( \phi _ { l } ) )$

Because the firm has an incentive to signal its type with higher quality levels, the marginal value of the efort from a customer increases, thereby increasing her optimal efort and resulting in a more valuable custom product for that customer. An interesting and counterintuitive implication of this result is that the optimal efort of the customer when there is information asymmetry may be even higher than in the full information scenario. From a practical standpoint, this is important because it ofers the firm two viable strategies for dealing with information asymmetry regarding its codesign capability: First, investing in technology (e.g., authentication mechanisms) or resources (e.g., advertising) to reduce the information asymmetry; or second, adjusting its product quality levels and product line design to signal its co-design capability. Since the latter has the added benefit of encouraging greater customer efort, it might indeed be a better option.

## 4.2. Competition

We have so far assumed a monopolistic situation where both the standard product and the co-designed product were ofered by the same firm. To examine whether our results hold in the presence of competition, we now consider a setting in which there are two firms, A and $B ,$ with each firm ofering a distinct product. Thus, as before, we have two customer segments, with each segment being ofered two products to choose from. Without loss of generality, we assume that firm A is preferred by the high-end segment and ofers a product with the co-design option, while firm B is preferred by the low-end segment and ofers a standard product. The price, quality, and marginal cost of production of each firm’s products are $p _ { i } , q _ { i } ,$ and $c _ { i } q _ { i } ^ { 2 } ,$ respectively, where $i \in [ A , B ] . ^ { 6 }$

We model the competition between the firms as follows: when the high-end segment buys a co-designed product from A, the net surplus she receives is $u _ { H A } - p _ { A } ,$ where $u _ { H A }$ is the utility obtained by the high-end segment from the co-designed product. If, however, she purchases the standard product from firm $B ,$ the utility she receives is $\psi u _ { H B } - p _ { B } ,$ where $\psi$ is the intensity of competition between the two firms.<sup>7</sup> It follows that the high-end segment will purchase from firm A only if $u _ { A } - p _ { A } \geq \psi u _ { B } - p _ { B }$ . Similarly, the low-end segment will purchase from firm B only if $u _ { L B } - p _ { B } \geq \psi u _ { L A } - p _ { A } .$ In addition, the prices should also be such that $u _ { H A } -$ $p _ { { A } } \geq 0$ and $u _ { L B } - p _ { B } \geq 0$

The sequence of decision making is as follows: The firms first determine the quality of their products. The high-end customer then decides how much efort to put into the co-design process, and this determines their willingness to pay for the products that they choose to buy. Finally, after the co-design process is complete, the firms announce the price(s) for the product(s) and the customer decides which of the products she would like to purchase from the firms.

Proposition 10. The optimal co-design efort of the highend customer is given by

$$
\gamma^ {*} = \frac {q _ {B} v _ {H} \phi \psi}{2 \kappa}.\tag{14}
$$

In addition, $\gamma ^ { * }$ is increasing in $q _ { B }$ and $\psi .$

The above proposition shows that a higher quality product from a competitor can encourage the highend customers to put in more co-design efort. Furthermore, this level of efort is also influenced by the level of competition between the two firms. When a firm faces greater competition (higher ψ), it has to respond by lowering its prices. Interestingly, when the firm ofers co-design, the higher surplus because of this greater competition motivates increased co-design efort from the high-end customers.

Proposition 11. (a) $q _ { A } ^ { * }$ is increasing in $\psi .$

(b) There exist conditions under which the profits of firm A are increasing in ψ when it ofers a co-design option.

The first part of this proposition indicates that as competition intensifies, the firm ofering co-design can benefit by increasing its product quality. In other words, even in this competitive situation, the efect of the co-design option is to lead to a higher optimal product quality.

The second part of the proposition points to the interesting possibility that higher competitive intensity can actually be beneficial for the firm ofering codesign. The reasoning behind this is as follows: more intense competition (higher ψ) causes the firm to lower its prices. Normally, these lower prices lead to lower profits. However, when the firm ofers co-design, the higher surplus perceived by the high-end customer can motivate greater co-design efort, which in turn increases the customer’s willingness to pay and thus higher margins and profits for the firm. In other words, an investment in technology to support co-design can lead to higher profits in the presence of competition.

We have used a relatively simple competitive setting in this section to test the robustness of our approach. Consideration of other, more complex competitive environments might lead to additional insights regarding the value of co-design under competition. Although the key insights from our models about the role of the standard product and the impact on product quality may hold in such settings as well, such models present interesting areas for future research.

## 5. Discussion and Conclusion

Although there is a significant body of research on the consideration of individual customer preferences in product design, mostly in the context of customization and mass customization, a tacit assumption common in this literature is that the primary cost of any customization efort is borne by the manufacturer of the product. In this paper, we examine the issue of co-design, which involves the investment of a significant amount of efort by customers in their contribution to the product design process. In other words, we have modeled the co-design process as defined by both the co-design capability supported by the manufacturer and made available to the customer, as well as the co-design efort invested by the customer engaging in co-design.

We start with the premise that the customer may not choose the option of co-design if she believes that the firm will set the price of the custom product (higher) to extract the entire consumer surplus.<sup>8</sup> We examine the problem of overcoming this resistance on the customer’s part to engage in co-design. We show that the customer is unlikely to engage in a potentially expensive co-design efort unless she also has the option of buying a standard product that does not involve codesign, even though the standard product may provide lower value to the customer, and even when the standard product is ofered by another firm. In other words, a necessary but not suficient condition for codesign to be feasible is that the customer can choose between standard and customizable products. This is evidenced in both of the specific industry examples we cited earlier, since Ford and emachineshop.com ofer standard versions of their products in addition to the co-design option. It is also interesting to note that as more companies begin to ofer co-design capabilities at various levels (BMW, Gap, Longchamp, Muji, North Face, Yamaha, etc.; Ogawa and Piller 2006), in all cases, the firms ofer standard products as well.

Furthermore, we show that when a firm ofers a product line including both standard products as well as customizable products that could generate higher utility to the customer through co-design, it may be profitable for the firm to actually ofer higher quality standard products than it might otherwise. This is an interesting result, which counteracts the “conventional wisdom” in the product line literature about the cannibalization efect that might motivate the firm to lower the quality of its low-end products when ofering a product line.

We also address the question of the firm’s optimal strategy when it has the option of supporting codesign. We show that depending on the composition of the market, in terms of the distribution of high-end versus low-end customers, as well as the cost faced by customers in engaging in co-design, the firm’s optimal strategy can range from ofering only high-quality standard products to high-end customers to ofering a product line of standard products at diferent levels of quality, to ofering a product line that includes codesigned products as well as standard products. An interesting result in this context is that the range of conditions under which a product line is preferable to a single product strategy increases when the firm includes the option of co-design in its choice set.

Clearly, to motivate customers to participate in codesign, the firm has to ofer appropriate resources and tools for this purpose. However, the customer may not understand the quality and efectiveness of these resources at the outset of the co-design process. Therefore, we also examine the very real problem of information asymmetry that arises when customers considering the option of engaging in co-design are unsure of the co-design capability of the firm ofering that option. We show that a firm interested in leveraging co-design and therefore providing a high level of co-design capability can signal this higher capability to the interested customer by raising the quality of its products relative to the full information situation in which the customer knows the firm’s co-design capability before investing any efort. In efect, in the presence of this information asymmetry, we show that the firm may find it profitable to raise the quality of not only its customizable products but also that of its standard products, in some cases even beyond its eficient quality level.

The interplay of the product line planning decision and the co-design capability planning decision that we show through our analysis can be valuable in the product planning process. As we mentioned in Section 1, firms that want to pursue co-design as a feature of their product oferings cannot simply adopt a “field of dreams” approach (based on the notion “build it and they will come”). Rather, it is important to view the co-design capability decision as a part of their product portfolio planning.

While we believe that our model provides useful insights, it is still a first step in understanding the economics of co-design. There are a number of refinements and extensions that would be worth exploring in future research. One possible extension is to consider the firm’s cost of providing co-design capabilities. Note that, while these costs may be quite high in some contexts, particularly in traditional brick-and-mortar businesses, the use of information technologies such as the Internet and a variety of computer-aided software tools that are increasingly becoming more user-friendly, can make these costs more manageable. Finally, it would be useful to empirically study the relationship between market composition, with respect to the distribution of high- and low-end customers, and the use of diferent product strategies by firms.

## Acknowledgments

The authors would like to thank the editors and reviewers for their constructive feedback, as well as the attendees of the 2014 TEIS Workshop.

## Appendix A. Cost Uncertainty and Price Commitment

We now relax the assumption that the firm knows the level of co-design efort exerted by the customer. In addition, we explicitly consider the possibility that the firm incurs an additional cost to incorporate customer co-design into the product. We assume that this cost is convex in the level of efort by the customer.

We model the uncertainty in efort as follows: when the customer incurs a cost of $\dot { \kappa } \gamma ^ { 2 } .$ , she is able to improve the willingness to pay by a factor $\gamma + \epsilon$ where  is a random variable with the following distribution:

$$
\epsilon = \left\{ \begin{array}{l l} \epsilon_ {H} = \frac {\Delta \rho}{1 - \rho} & \mathrm{w.p.} 1 - \rho , \\ \epsilon_ {L} = - \Delta & \mathrm{w.p.} \rho . \end{array} \right.
$$

Note that  has a mean of 0 and a variance of $( \rho / ( 1 - \rho ) ) \Delta ^ { 2 }$ Thus, this distribution allows us to manipulate the variance of customer co-design efort without afecting its mean. The firm’s cost of incorporating this efort into the product is $f ( \gamma + \epsilon ) ^ { 2 }$

## Case 1: No Price Commitment

The price of the premium product will depend on the customer’s efort as well as the realization of $\epsilon .$ Thus, when the customer puts in efort $\gamma ,$ the price of both products will be

$$
\begin{array}{c} {p _ {N P} (\gamma , \epsilon) = (1 + \phi (\gamma + \epsilon)) v _ {H} (q _ {P} - q _ {S}) + v _ {L} q _ {S},} \\ {p _ {N S} = v _ {L} q _ {S}.} \end{array}
$$

The optimal efort of the customer for both realizations of $\epsilon$ would be

$$
\gamma^ {*} = \frac {q _ {S} v _ {H} \phi}{2 \kappa}.
$$

However, when the firm decides what quality levels to ofer for the premium and standard products, it does not know the realization of  and hence will be uncertain about the prices that it will obtain for its products. The profits of the firm as a function of  and quality levels are

$$
\pi_ {N} (q _ {P}, q _ {S}, \epsilon) = \alpha (p _ {N P} (\gamma^ {*}, \epsilon) - c q _ {P} ^ {2}) + (1 - \alpha) (p _ {N S} - c q _ {S} ^ {2}).
$$

Substituting $\gamma ^ { * }$ and taking expectations over $\epsilon ,$ we have that the profits of the firm are

$$
\begin{array}{r l} & {\pi_ {E N} (q _ {P}, q _ {S}) = \frac {1}{4 (1 - \rho) \kappa^ {2}} (\alpha (1 - \rho) (q _ {S} v _ {H} ^ {2} \phi^ {2} (2 \kappa (q _ {P} - q _ {S}) - f q _ {S})} \\ & {\qquad + 4 \kappa^ {2} (q _ {P} - q _ {S}) (v _ {H} - c (q _ {P} + q _ {S}))) - 4 \alpha \rho \Delta^ {2} f \kappa^ {2}} \\ & {\qquad + 4 (1 - \rho) \kappa^ {2} q _ {S} (v _ {L} - c q _ {S}))} \end{array}
$$

Diferentiating the profit function w.r.t. $q _ { P }$ and $q _ { S }$ gives us the optimal quality levels, which are

$$
\begin{array}{r} q _ {N P} ^ {*} = \frac {2 v _ {H} (v _ {H} \phi^ {2} (\alpha v _ {H} (f + \kappa) + \kappa v _ {L}) + 4 (1 - \alpha) c \kappa^ {2})}{1 6 (1 - \alpha) c ^ {2} \kappa^ {2} + 4 \alpha c v _ {H} ^ {2} \phi^ {2} (f + 2 \kappa) - \alpha v _ {H} ^ {4} \phi^ {4}}, \\ q _ {N S} ^ {*} = \frac {2 \kappa (\alpha v _ {H} ^ {3} \phi^ {2} + 4 c \kappa v _ {L} - 4 \alpha c \kappa v _ {H})}{1 6 (1 - \alpha) c ^ {2} \kappa^ {2} + 4 \alpha c v _ {H} ^ {2} \phi^ {2} (f + 2 \kappa) - \alpha v _ {H} ^ {4} \phi^ {4}}. \end{array}
$$

Substituting these optimal quality levels in the profit function gives us the profits of the firm under this scenario as

$$
\begin{array}{r l} & {\pi_ {N P} ^ {*} = \frac {4 c \kappa^ {2} (\alpha v _ {H} (v _ {H} - 2 v _ {L}) + v _ {L} ^ {2}) + \alpha v _ {H} ^ {3} \phi^ {2} (\alpha f v _ {H} + 2 \kappa v _ {L})}{1 6 (1 - \alpha) c ^ {2} \kappa^ {2} + 4 \alpha c v _ {H} ^ {2} \phi^ {2} (f + 2 \kappa) + \alpha v _ {H} ^ {4} \phi^ {4}}} \\ & {\qquad + \frac {\alpha \rho \Delta^ {2} f}{1 - \rho}.} \end{array}
$$

## Case 2: Price Commitment

We now turn to the case in which the firm commits to a price when it ofers a single product that can be co-designed.<sup>9</sup> In this case, the firm first decides both the optimal quality for the product and makes a credible commitment to the price at which the co-designed product would be sold. The customer then incurs the efort to co-design the product. Finally, she purchases the product at the precommitted price.

The surplus of the customer when the firm commits to a price p as a function of  is

$$
\lambda (\gamma , p, \epsilon) = q _ {C P} v _ {H} (1 + \phi (\gamma + \epsilon)) - \kappa \gamma^ {2} - p _ {C}.
$$

The optimal efort of the customer is now given by

$$
\gamma^ {*} = \max \left[ 0, \frac {q _ {C P} v _ {H} \bar {\phi}}{2 \kappa} \right].
$$

Thus, the customer will put in a positive efort if $\lambda ( \gamma ^ { * } , p , \epsilon )$ $> 0 ;$ if not, she does not engage in co-design, i.e., $\gamma ^ { * } = 0$

In the absence of any uncertainty, the firm will be able to set a price that induces co-design efort and extracts all of the surplus of the customer. However, under uncertainty, this might not be possible since the firm has to commit to the price before it knows the realization of .

Given our model that  can take two values, there are two possibilities with respect to the price: the firm can set a high price $( p _ { H } )$ that will induce efort only when $\epsilon = \epsilon _ { H } ,$ , or it can set a low price $( p _ { L } )$ that will induce efort under both scenarios $( \epsilon = \epsilon _ { H } \wedge \epsilon _ { L } )$ . The expressions for these prices will be

$$
\begin{array}{l} {p _ {H} = \frac {q _ {C P} v _ {H} ((1 - \rho) q _ {C P} v _ {H} \phi^ {2} + 4 \kappa (1 - \rho (1 - \Delta \phi)))}{4 (1 - \rho) \kappa},} \\ {p _ {L} = \frac {q _ {C P} v _ {H} (4 \kappa (1 - \Delta \phi) + q _ {C P} v _ {H} \phi^ {2})}{4 \kappa}.} \end{array}
$$

The profits of the firm when the price is $p _ { H }$ will be

$$
\pi_ {C H} = \alpha ((1 - \rho) (p _ {H} - f (\gamma^ {*} + \epsilon_ {H}) ^ {2}) + \rho v _ {H} q _ {C P} - c q _ {C P} ^ {2}).
$$

The optimal quality under this scenario will be

$$
q _ {C P H} ^ {*} = \frac {2 \kappa v _ {H} (\rho \Delta \phi (\kappa - f) + \kappa)}{4 c \kappa^ {2} - (1 - \rho) v _ {H} ^ {2} \phi^ {2} (\kappa - f)}.
$$

Substituting the optimal quality back into the profit function gives us the profits of the firm under this scenario as

$$
\begin{array}{r l} & {\pi_ {C H} ^ {*} = (\alpha \kappa (\kappa ((1 - \rho) (\rho \Delta v _ {H} \phi + v _ {H}) ^ {2} - 4 \rho^ {2} c \Delta^ {2} f)} \\ & {\qquad - (1 - \rho) \rho \Delta f v _ {H} ^ {2} \phi (\rho \Delta \phi + 2)))} \\ & {\qquad \cdot ((1 - \rho) (4 c \kappa^ {2} - (1 - \rho) v _ {H} ^ {2} \phi^ {2} (\kappa - f))) ^ {- 1}.} \end{array}
$$

The profits of the firm when the price is $p _ { L }$ will be

$$
\pi_ {C L} = (p _ {L} - (1 - \rho) f (\gamma^ {*} + \epsilon_ {H}) ^ {2} - \rho f (\gamma^ {*} + \epsilon_ {L}) ^ {2} - c q _ {C P} ^ {2}).
$$

Figure A.1. (Color online) Efect of Cost and Efort Uncertainty  
![](/api/attachments/MVQAG232/fulltext/images/f17e2d433eea0540ed027e0c4bda369175416d876d7289f0df81a9a71036c8da.jpg)

The optimal quality under this scenario will be

$$
q _ {C P L} ^ {*} = \frac {2 \kappa^ {2} v _ {H} (1 - \Delta \phi)}{4 c \kappa^ {2} - v _ {H} ^ {2} \phi^ {2} (\kappa - f)}.
$$

Substituting the optimal quality back into the profit function gives us the profits of the firm under this scenario as

$$
\begin{array}{r l} & {\pi_ {C L} ^ {*} = (\rho (\kappa^ {2} (4 \rho c \Delta^ {2} f + (\rho - 1) v _ {H} ^ {2} (\Delta \phi - 1) ^ {2})} \\ & {\qquad + \rho \Delta^ {2} f ^ {2} v _ {H} ^ {2} \phi^ {2} - \rho \Delta^ {2} f \kappa v _ {H} ^ {2} \phi^ {2}))} \\ & {\qquad \cdot ((1 - \rho) (4 c \kappa^ {2} - v _ {H} ^ {2} \phi^ {2} (\kappa - f))) ^ {- 1}.} \end{array}
$$

Comparing $\pi _ { N P } ^ { * } , \pi _ { C H } ^ { * } .$ , and $\pi _ { C L } ^ { * }$ , as shown in Figure ${ \mathrm { A . 1 } } _ { }$ , shows that deferring the pricing decision is optimal when the uncertainty associated with co-design efort is suficiently high.

Note that the case in which there is no uncertainty about the production costs of co-designed products arises when $\Delta = 0 .$ . As Figure A.1 shows, even in this case, there are conditions (high f ) under which deferring price commitment until after co-design is optimal for the firm.

## Appendix B. Analysis of Equilibria Under Information Asymmetry About the Firm’s Co-design Capability

## Pooling Equilibrium

First consider the case in which the high-capability firm is not able to reliably signal its capability. Since the customer is not able to distinguish between the two firm types, her decision on how much to invest in the co-design process will take into consideration the expected surplus she will obtain through her eforts. This surplus can be represented as

$$
\begin{array}{c} \lambda_ {E} (\gamma) = \omega (q _ {S} ((1 + \phi_ {h} \gamma) v _ {H} - v _ {L})) + (1 - \omega) q _ {S} ((1 + \phi_ {l} \gamma) v _ {H} - v _ {L}) \\ - \kappa \gamma^ {2}. \end{array} \tag {B.1}
$$

The optimal co-design efort of the customer in this scenario will be

$$
\underline {{\gamma}} (\bar {\phi}; q _ {s}) = \frac {q _ {s} v _ {H} \bar {\phi}}{2 \kappa}.\tag{B.2}
$$

To figure out the quality levels that the firm might choose to ofer, we need to determine the profits that the firm might be able to obtain, when it anticipates this efort from a customer. These profits, would in turn, depend on the capability level of the firm. If the firm is of high capability, its profits will be<sup>10</sup>

$$
\pi_ {m h} (q _ {P}, q _ {S}, p _ {P}, p _ {S}) = \alpha (p _ {P} (\phi_ {h}, \underline {{\gamma}}) - c q _ {P} ^ {2}) + (1 - \alpha) (p _ {S} - c q _ {S} ^ {2}). \tag {B.3}\tag{B.3}
$$

The above expression takes into account the fact that the customer would be benefiting from her opportunity of having worked with a high-capability firm; hence, the price she is willing to pay for the co-designed product would be higher (because of the higher return for her efort). Substituting the prices and quality levels into the profit function, we have that

$$
\pi_ {m h} = \frac {2 \kappa q _ {S} (v _ {L} - c q _ {S}) - \alpha (q _ {P} - q _ {S}) (2 c \kappa (q _ {P} + q _ {S}) - v _ {H} (2 \kappa + q _ {S} v _ {H} \bar {\phi}))}{2 \kappa}.\tag{B.4}
$$

Diferentiating the above profit function with respect to q<sub>P</sub> and $q _ { S }$ gives us the optimal quality levels that the high-type firm would like to ofer

$$
\begin{array}{r} q _ {m h P} ^ {*} = \frac {2 \kappa v _ {H} (v _ {H} \phi_ {h} \bar {\phi} (\alpha v _ {H} + v _ {L}) + 4 (1 - \alpha) c \kappa)}{1 6 (1 - \alpha) c ^ {2} \kappa^ {2} + 8 \alpha c \kappa v _ {H} ^ {2} \phi_ {h} \bar {\phi} - \alpha v _ {H} ^ {4} \phi_ {h} ^ {2} \bar {\phi} ^ {2}}, \\ q _ {m h S} ^ {*} = \frac {2 \kappa (\alpha v _ {H} (4 c \kappa - v _ {H} ^ {2} \phi_ {h} \bar {\phi}) - 4 c \kappa v _ {L})}{1 6 (1 - \alpha) c ^ {2} \kappa^ {2} + 8 \alpha c \kappa v _ {H} ^ {2} \phi_ {h} \bar {\phi} - \alpha v _ {H} ^ {4} \phi_ {h} ^ {2} \bar {\phi} ^ {2}}. \end{array}\tag{B.5}
$$

(B.6)

Note that, the above analysis assumes that the highcapability firm is not able to diferentiate itself from the lowcapability firm. As mentioned earlier, for this to be an equilibrium, it should be optimal for the low-capability firm to mimic the high-capability firm’s quality levels. This will lead to a situation in which the customer will not be able to distinguish between the two firms and hence she will determine her optimal efort based on the expected value of the firm’s capability level. Thus, it follows that the optimal quality level of the low-capability firm would be

$$
\begin{array}{r} q _ {m l P} ^ {*} = q _ {m h P} ^ {*}, \\ q _ {m l S} ^ {*} = q _ {m h S} ^ {*}. \end{array}
$$

Substituting the optimal quality levels into the profit function gives us the optimal profits of the firm as a function of the capability as well as the customers’ beliefs about the capability.

## Separating Equilibrium

Now consider the scenario in which the firm can signal its type through its product quality levels. In such a scenario, the customer will be able to make an informed decision on the level of efort that she should invest in co-design. Let $q _ { d h j }$ be the quality levels ofered by the high-capability firm and $q _ { d l j }$ be that of the low-capability firm where $j \in [ P , S ]$

Given the diferent quality levels, when the customer decides how much efort to invest in co-design, she takes into account both the implied capability level of the firm as well as the quality of the standard product it ofers. As detailed in Proposition $^ { 3 , }$ her optimal efort would then be

$$
\gamma_ {d j} (\phi_ {j}; q _ {d j S}) = \frac {q _ {d j S} v _ {H} \phi_ {j}}{2 \kappa},\tag{B.7}
$$

where $j \in [ h , l ]$ indicates the capability of the firm as inferred from the quality level.

Now consider the decision of a firm whose capability is low. Under the assumption that the quality levels of the lowcapability firm are diferent from that of the high-capability firm, its profits as a function of prices and quality can be characterized as

$$
\begin{array}{r} \pi_ {d l 1} (q _ {d l P}, q _ {d l S}, p _ {P}, p _ {S}) = \alpha (p _ {P} (\phi_ {l}, \gamma_ {l}) - c q _ {d l P} ^ {2}) \\ + (1 - \alpha) (p _ {S} - c q _ {d l S} ^ {2}). \end{array}\tag{B.8}
$$

If, however, the low-capability firm mimics the quality levels chosen by the high-capability firm, its profits will be

$$
\begin{array}{r} \pi_ {d l 2} (q _ {d h P}, q _ {d h S}, p _ {P}, p _ {S}) = \alpha (p _ {P} (\phi_ {l}, \underline {{\gamma}}) - c q _ {d h P} ^ {2}) \\ + (1 - \alpha) (p _ {S} - c q _ {d h S} ^ {2}). \end{array}\tag{B.9}
$$

For the high-capability firm to be able to credibly signal its type, it has to ensure that the low-capability firm finds it optimal to not mimic its quality levels. Hence the only feasible quality levels for the high-capability firm would be those levels that ensure that $\pi _ { d l 2 } < \pi _ { d l 1 }$

## Endnotes

<sup>1</sup> A related but diferent approach is open innovation (Tita 2016), in which firms (e.g., Threadless.com and FirstBuild) engage external participants in product development using mechanisms such as contests.

<sup>2</sup> “Customer Co-Design describes a process that allows customers to express their product requirements and carry out product realization processes by mapping the requirements into the physical domain of the product” (Tseng and Piller 2011, p. 8).

<sup>3</sup> In fact, “. . . customers who self-configure their own products tend to spend 20–30 percent more than customers who purchase of-theshelf solutions” (Seybold 2006, p. 272).

<sup>4</sup> In our formulation, $q _ { 1 H } ^ { * }$ (Equation (1)) and $q _ { 1 L } ^ { * }$ (Equation (2)) are the eficient quality levels for the high- and low-end segments, respectively.

<sup>5</sup> However, this increase in willingness to pay for the standard product may not be the same as for the co-designed product. So a more precise approach would be to moderate this efect by a discount factor $\delta < 1 ,$ so that the utility from the standard product, after the customer engages in co-design, will be $( 1 + \theta \delta ) v _ { H } q _ { S }$ . However, since this does not afect the key results of the paper, we have not included such a discount factor.

<sup>6</sup> Given that there are only two customer segments, there is no need to consider multiple products being ofered by each firm, since such a strategy will never be optimal in equilibrium. One could, of course, consider a more general model of competition with more than two segments, but the results of such a model would be hard to compare with our model in Section 3.

<sup>7</sup> We assume that $\psi$ is low enough to ensure that firm A does not cover the entire market.

<sup>8</sup> It is interesting that even in limited co-design involving selecting a subset of features, as in custom textbooks, firms price the custom product significantly higher than the corresponding fraction of the standard/full product’s price.

<sup>9</sup> We recognize that price commitment is a possibility even when the firm ofers a product line. However, since the primary purpose of this analysis is to show that even under price commitment, a single product might not be optimal, we restrict our comparison between price commitment with single product and no price commitment.

<sup>10</sup> The first subscript m refers to the fact that the resulting equilibrium will be a pooling equilibrium where the low-capability firm mimics the high-capability firms product quality levels, and d refers to a separating equilibrium where high- and low-capability firms ofer diferent quality levels.

## References

Abbott L (1953) Vertical equilibrium under pure quality competition. Amer. Econom. Rev. 43(5):826–845.

Akerlof GA (1970) The market for lemons: Quality uncertainty and the market mechanism. Quart. J. Econom. 84(3):488–500.

Anderson DM (2004) Build-to-Order and Mass Customization: The Ultimate Supply Chain Management and Lean Manufacturing Strategy for Low-Cost On-Demand Production Without Forecasts or Inventory (CIM Press, Cambria, CA).

Balachander S, Srinivasan K (1994) Selection of product line qualities and prices to signal competitive advantage. Management Sci. 40(7):824–841.

Baldwin C, von Hippel E (2011) Modeling a paradigm shift: From producer innovation to user and open collaborative innovation. Organ. Sci. 22(6):1399–1417.

Bhargava HK, Choudhary V (2001) Information goods and vertical diferentiation. J. Management Inform. Systems 18(2):89–106.

Bhargava HK, Choudhary V (2008) Research note: When is versioning optimal for information goods? Management Sci. 54(5): 1029–1035.

Bhattacharya S, Gupta A, Hasĳa S (2014) Joint product improvement by client and customer support center: The role of gain-share contracts in coordination. Inform. Systems Res. 25(1):137–151.

Choudhary V, Ghose A, Mukhopadhyay T, Rajan U (2005) Personalized pricing and quality diferentiation. Management Sci. 51(7):1120–1130.

Davis SM (1987) Future Perfect (Addison-Wesley, Reading, MA).

Deneckere RJ, McAfee RP (1996) Damaged goods. J. Econom. Management Strategy 5(2):149–174.

Desai PS (2001) Quality segmentation in spatial markets: When does cannibalization afect product line design? Marketing Sci. 20(3):265–283.

Dewan R, Jing B, Seidmann A (2003) Product customization and price competition on the Internet. Management Sci. 49(8): 1055–1070.

Franke N, Schreier M, Kaiser U (2010) The “designed it myself” efect in mass customization. Management Sci. 56(1):125–140.

Ghose A, Huang K-W (2009) Personalized pricing and quality customization. J. Econom. Management Strategy 18(4):1095–1135.

Gu Z(J), Tayi GK (2015) Investigating firm strategies on ofering consumer-customizable products. Inform. Systems Res. 26(2): 456–468.

Guo L, Zhang J (2012) Consumer deliberation and product line design. Marketing Sci. 31(6):995–1007.

Krishnan V, Zhu W (2006) Designing a family of developmentintensive products. Management Sci. 52(6):813–825.

Mendelson H, Parlaktuk AK (2008) Competitive customization. Manufacturing Service Oper. Management 10(3):377–390.

Moorthy KS (1984) Market segmentation, self-selection, and product line design. Marketing Sci. 3(4):288–307.

Moorthy SR, Png IPL (1992) Market segmentation, cannibalization, and the timing of product introductions. Management Sci. 38(3):345–359.

Mussa M, Rosen S (1978) Monopoly and product quality. J. Econom. Theory 18(2):301–317.

Ogawa S, Piller FT (2006) Reducing the risks of new product development. MIT Sloan Management Rev. 47(2):65–71.

Raghunathan S (2000) Software editions: An application of segmentation theory to the packaged software market. J. Management Inform. Systems 17(1):87–113.

Salop S (1979) Monopolistic competition with outside goods. Bell J. Econom. 10(9):141–156.

Seybold PB (2006) Outside Innovation: How Your Customers Will Co-Design Your Company’s Future (HarperCollins, New York).

Syam NB, Kumar N (2006) On customized goods, standard goods, and competition. Marketing Sci. 25(5):525–537.

Syam NB, Pazgal A (2013) Co-creation with production externalities. Marketing Sci. 32(5):805–820.

Syam NB, Ruan R, Hess JD (2005) Customized products: A competitive analysis. Marketing Sci. 24(4):569–584.

Terwiesch C, Loch CH (2004) Collaborative prototyping and the pricing of custom-designed products. Management Sci. 50(2): 145–158.

Thallmaier SR (2014) Customer Co-Design: A Study in the Mass Customization Industry (Springer Gabler, Wiesbaden, Germany).

Thomke S, von Hippel E (2002) Customers as innovators: A new way to create value. Harvard Bus. Rev. 80(4):74–81.

Tita B (2016) A new approach to new products. Wall Street Journal (September 19). https://www.wsj.com/articles/a-new -approach-to-new-products-1474250821.

Tseng MM, Piller F (2011) The Customer Centric Enterprise: Advances in Mass Customization and Personalization (Springer, Berlin Heidelberg).

Villas-Boas JM (2009) Product variety and endogenous pricing with evaluation costs. Management Sci. 55(8):1338–1346.

Wind J, Rangaswamy A (2001) Customerization: The next revolution in mass customization. J. Interactive Marketing 15(1):13–32.

Xia N, Rajagopalan S (2009) Standard vs. custom products: Variety, lead time, and price competition. Marketing Sci. 28(5):887–900.

Xiong H, Chen Y-J (2013) Product line design with deliberation costs: A two-stage process. Decision Anal. 10(3):225–244.

Xiong H, Chen Y-J (2014) Product line design with seller-induced learning. Management Sci. 60(3):784–795.

Zipkin PH (2001) The limits of mass customization. MIT Sloan Management Rev. 42(3):81–88.

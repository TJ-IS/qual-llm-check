---
otero_id: 28356
otero_key: "DBT6WQND"
title: "Strategic Implications of Online Retail Platforms’ Membership-Based Free Shipping Programs"
authors: "Geng Sun; Huseyin Cavusoglu; Srinivasan Raghunathan"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.0208"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Strategic Implications of Online Retail Platforms’ Membership-Based Free Shipping Programs

Geng Sun,<sup>a</sup> Huseyin Cavusoglu,<sup>b</sup> Srinivasan Raghunathan<sup>b,</sup>\*

<sup>a</sup> Robert C. Vackar College of Business & Entrepreneurship, University of Texas Rio Grande Valley, Edinburg, Texas 78539; <sup>b</sup> Naveen Jinda School of Management, University of Texas at Dallas, Richardson, Texas 75080

Contact: geng.sun@utrgv.edu, https://orcid.org/0000-0001-5162-5412 (GS); huseyin@utdallas.edu, https://orcid.org/0000-0002-7982-3602 (HC); sraghu@utdallas.edu, https://orcid.org/0000-0002-2782-3520 (SR)

Received: March 28, 2022 Revised: November 2, 2022; March 1, 2023 Accepted: April 26, 2023 Published Online in Articles in Advance: July 11, 2023

https://doi.org/10.1287/isre.2022.0208

Copyright: © 2023 INFORMS

Abstract. Product shipping is an indispensable but costly operation in online retailing. Although several initiatives are underway to reduce the shipping cost, an important innovation is the membership-based free shipping (MFS) program, in which a retail platform that allows third-party sellers to sell their products for a commission bears the shipping costs for purchases made by members who have paid an up-front fee. We identify several strategic impacts of MFS programs that are the key drivers to their success from the platform’s or other stakeholders’ perspectives. For example, we find that the membership fee collected by the platform does not cover its shipping cost, which suggests the MFS program benefit members and hurts the platform if the program is evaluated based on direct operational considerations only. However, we also show that the MFS program actually benefits the platform and hurts consumers when the shipping cost is less than a threshold. Moreover, the platform’s benefit from the MFS program follows an inverted U shape with respect to the shipping cost, suggesting that the program enjoys the greatest benefit for products with a moderate shipping cost. Even though the MFS program enhances the overall consumer demand and consumption, it could hurt society because the MFS program stimulates demand from consumers who have a low consumption utility relative to the shipping cost. Our results demonstrate that the MFS program is not just a shipping cost-transfer mechanism; rather, it is a strategic initiative by online retail platforms to exploit the need for prod uct shipping to their advantage.

History: Ram Gopal, Senior Editor; Yuliang Yao, Associate Editor. Supplemental Material: The online supplement is available at https://doi.org/10.1287/isre.2022.0208.

Keywords: online retailing • free shipping • membership • MFS

## 1. Introduction

Online retail platforms (hereafter, platforms) in which third-party sellers sell their products offer consumers enormous benefits, such as large product selection and convenience. At the same time, online retailing suffers from challenges, which are not salient in its brick-andmortar counterpart. One such challenge is shipping physical products to consumers. Shipping is an indispensable but costly operation in online retailing because of the geographical separation between buyers and sellers. Industry experts often cite the shipping cost as the Achilles’ heel of e-commerce that hinders its growth (Rossi 2015). Recognizing the importance of shipping in online consumers’ purchase decisions, platforms have been investing heavily in distribution networks including last-mile logistics to improve the efficiency of shipping operations for products sold in those platforms (Greene 2020, Moran 2022). Moreover, some platforms have introduced a membership-based free shipping (MFS) program that actively seeks to address the consumers’ shipping cost burden. Examples of MFS programs include Amazon Prime, ShopRunner, Walmart.com’s now-defunct ShippingPass, and Walmart.com’s recently introduced Walmart+. A common key element of these programs is that once a consumer becomes a member of the program by paying an up-front membership or subscription fee, the platform ships products for free to the member whenever she makes a purchase during the membership period. Essentially, unlike the cost-reduction efforts of the platforms, MFS programs transfer the shipping cost burden from consumers to the retailer or the platform, albeit for a fee. The popularity of MFS programs is evident from the membership size of these programs; the Amazon Prime program has over 200 million members around the world (Dean 2022), and the Walmart+ program has reached 32 million U.S. subscribers within the first year of its launch (Repko 2021).

Despite the popularity of MFS programs, industry ex perts are divided in their opinions about the effectiveness of these programs to increase platforms’ profits (Tuttle

2011, Rubin 2015, Byrnesarchive 2016, Levy 2016). Some experts claim that the revenue from membership fees of MFS programs plays a pivotal role in helping platforms deliver profits (Rubin 2015, Streitfeld 2015, Levy 2016). On the contrary, other experts claim that unlimited free shipping can be a very costly burden for the platforms, hurting their bottom lines (Burke 2015, Sheffield 2015, Rubin 2016). For instance, Amazon’s shipping and fulfillment costs accounted for 32% of their revenue in 2021 (Al 2022). The value of MFS programs to consumers is also keenly debated. Because consumers pay an up-front fee to join these programs, figuring out if the membership is worth the fee is another issue for which there is no consensus among experts (Broida 2016, Consumer Reports 2016, Nolan 2016). Furthermore, whether MFS programs improve the overall welfare of stakeholders in the system, such as platform, sellers, and consumers, remains an unexplored question, although it has been reported that the free shipping programs exacerbate broader societal costs, such as carbon footage, packaging waste, and driver safety (Bird 2018, Nguyen 2018, Callahan 2019).

In spite of the significant attention given to MFS programs in the popular press and their more than decadelong existence, there is limited academic research on this topic (e.g., Fang et al. 2021). The academic research has focused on questions such as when should a retailer (rather than a platform in which third-party sellers sell their products) offer the MFS program, what should the membership fee be, and what is the optimal membership base. However, the impacts of these programs go beyond shipping as they have subtle implications for various parties involved with these programs, such as the platform, the third-party sellers that sell via the platform, and consumers who buy at the platform. Assessing the benefits of MFS programs without accounting for their strategic impacts could lead to flawed conclusions and an incomplete understanding of these programs. In this paper, we aim to articulate the strategic effects of a platform’s MFS program on different stakeholders and the role of shipping cost using a game-theoretical model. In particular, in our context, the product pricing and MFSrelated decisions are made by different parties: the former by third-party sellers and the latter by the platform.

We consider a dominant online platform where independent third-party sellers sell their products to consumers using an agency pricing model (i.e., sellers pay a percentage of the sale price as a commission to the platform). In return, the platform provides various valueadded services to sellers, such as online storefronts, product review systems, and recommendation systems. Such a business model is ubiquitous in online retailing and is used by platforms such as Amazon, Walmart.com, and Shop Runner. For instance, Amazon sells a majority of its products and more than 90% of products in several product categories using the agency pricing model (Jiang et al. 2011). The Walmart marketplace, which enjoyed a 60% increase in thirdparty sellers in 2021, also relies on the agency pricing model (Young 2022). In the absence of the MFS program, consumers pay not only the product price but also, the shipping cost. If the platform implements the MFS program, then the platform pays the shipping cost for program members. We develop a model of this context with two sellers, each selling a single product, and assess the implications of the MFS program for the stakeholders by comparing the equilibrium outcomes in the presence of the MFS program with those in its absence.

The key findings and implications of our study are the following.

i. The membership fee collected by the platform does not cover the cost it incurs in shipping products purchased by members during the membership period. Thus, solely from the perspective of shipping, the MFS program hurts the platform and benefits the members.

ii. Despite the platform’s shipping-related loss, the MFS program still benefits the platform when the shipping cost is less than a threshold value. However, a reduction in the shipping cost does not necessarily increase the platform’s benefit from the MFS program. The platform benefits the most from the MFS program when the shipping cost is moderate (i.e., neither too low nor too high).

iii. The MFS program hurts consumers overall. The MFS program hurts not only nonmembers but also, members. Both nonmembers and members are hurt by the higher product price consumers pay under the MFS program compared with when there is no MFS program. Moreover, the membership fee, which extracts the surplus difference between when a consumer joins the program and when she does not, offsets the ship ping cost-related savings members enjoy.

iv. Even though the MFS program increases the overall demand and the platform finds the program to be profitable, it is not necessarily social welfare enhancing. The MFS program stimulates extra demand from members who have a low utility for the products. Society’s gain from this extra demand could fall short of the shipping cost required to satisfy this demand under the MFS program, thus hurting social welfare. Therefore, even when the other societal costs associated with extra demand are ignored, the MFS program could still hurt society based on consumption benefits and shipping costs alone.

These findings are new to the literature. The findings suggest that the MFS program is a strategic vehicle for the platform to benefit at the consumers’ expense and sometimes, also at society’s expense. The results show that the MFS program is not a simple shipping cost-transfer mechanism; they demonstrate that it is a strategic initiative by online retail platforms to exploit shipping activity, which is indispensable in online retailing. We demonstrate that our findings are driven by several subtle effects regarding how sellers and consumers respond to the MFS program.

Hence, judging the MFS program purely as a cost-transfer mechanism between the platform and the consumers can lead to misleading and incorrect conclusions. Finally, the implications of MFS programs for online retail platforms can be quite different from those of physical stores, and the differences could be attributed to the role of shipping, which is more significant in online retailing than physical retailing.

## 2. Related Literature

Our work and its contributions are primarily related to the literature on online retailing, where product shipping is an essential activity (de Koster 2002, Lummus and Vokurka 2002). The bulk of the research on this topic focuses on improving efficiency by reducing inventory, delivery, and logistics costs, but we focus on free shipping. Two recent studies have examined free shipping in the online retailing context. Wen and Lin (2017) study the impact of the MFS program when one of two competing retailers adopts the program. They show that the MFS program benefits both retailers by softening the price competition between them. Fang et al. (2021) consider an e-tailer’s decision on whether to add MFS to its paid shipping/contingent free shipping menu. They focus on a setting where a consumer could buy an auxiliary product to take advantage of free shipping but also suffers a disutility from the auxiliary product. Consumers are heterogeneous in the disutility dimension and in shopping frequency. They identify the conditions under which different shipping policies are optimal. In contrast to the aforementioned studies, we examine a single dominant platform that is used by third-party sellers to sell their products for a commis sion using an agency model, which is a prominent business model in online marketplaces. Therefore, although the MFS program decision is made by the platform, the product pricing decisions are made by the third-party sellers in our model. Because the sellers’ interests may not be perfectly aligned with that of the platform, whether the product pricing decision and the MFS program decision are made by the same party could make a difference in understanding the strategic implications of MFS. Another key difference between our study and the other two studies is that we consider a setup in which the purchase frequencies of consumers are not only heterogeneous but also, endogenous. This difference is especially critical in light of our finding, which is consistent with reality: that the MFS program indeed affects the purchase frequency of members.<sup>1</sup> Moreover, we articulate the role of shipping cost on the value of the MFS program and provide insights into which types of products are appropriate for inclusion in the MFS program. Finally, unlike Fang et al. (2021), in which a sell er’s shipping policy is viewed as a price-discriminating device for consumer segmentation, the platform in our model uses the membership fee on the consumer side and commission on the seller side to realize value from the MFS program. Consequently, although some of the effects of the MFS program identified in this paper and Fang et al. (2021) appear to be similar, those effects are driven by different factors in the two papers.

This paper is also related to the rich body of work that has examined strategic consumer behavior in retailing contexts where a consumer makes current decisions by rationally anticipating future seller behavior and its impact on the consumer. Such contexts include dynamic pricing (Su 2007, Aviv and Pazgal 2008), capacity rationing (Liu and Van Ryzin 2008), product rollovers (Liang et al. 2014), supply chain contracting (Su and Zhang 2008), opaque selling (Jerath et al. 2010), quick response (Cachon and Swinney 2009), and posterior price matching (Lai et al. 2010). However, our context differs from the extant literature in one key aspect. The existing litera ture typically considers scenarios where retailers have control of the product, inventory, and pricing decisions. In contrast, in our context, although the platform makes decisions (e.g., membership fee) regarding the MFS program, the third-party sellers choose the product prices. We find that this unique feature plays a significant role in strategic consumers’ decision to become members of the MFS program because consumers would expect to purchase more when they are members and purchase less when they are not relative to when the MFS pro gram is not present.

Finally, even though the MFS programs are a recent phenomenon, they share a few characteristics with loyalty programs that are popular among brick-andmortar retailers and in the airline industry and have been extensively studied. Since the seminal works of Farrell (1990) and Klemperer (1987), researchers have examined the impacts of loyalty programs on brand loyalty, repeat-purchase patterns, and customer reten tion (Dowling and Uncles 1997, Sharp and Sharp 1997, Uncles et al. 2003, Yi and Jeon 2003, Lewis 2004, Ashley et al. 2016). These studies show that loyalty programs can lock in customers, increase switching cost, increase customer loyalty, and soften competition between firms. Our work differs from this stream of research along several dimensions. First, although a loyalty program is an ex post reward mechanism, the MFS is a front-end subscription-based program that promises future savings. Second, loyalty programs generally offer free membership, but MFS programs do not. Therefore, although the participation decisions of consumers are not necessarily strategic for loyalty programs, consumers have to assess the expected future benefits of the MFS program in relation to the membership fee they have to pay before making the joining decision. Finally, the question of whether the consumer remains loyal to the platform or switches to another platform does not arise in our context. Thus, our results are not driven by how MFS affects competition between platforms.

## 3. Model

We consider a dominant online platform R that allows third-party sellers to sell their products on the platform for a commission equal to α fraction of the sale price.<sup>2</sup> There is a mass of consumers, normalized to one, who use the platform. A consumer visits R to shop for a product that could possibly satisfy her need whenever a consumption need arises. We consider a time period that consists of N discrete shopping instances. For example, the time period could be a year, and each day in the year could be a shopping instance such that the time period has 365 shopping instances. A consumer may not have a consumption need in every shopping instance. Furthermore, even when she faces a consumption need, the intensity of the need and her product preference can differ across shopping instances. A consumer has two options when she visits the platform: either (i) buy the product that offers the maximum positive surplus or (ii) do not buy any product. The consumer will choose the second option if no product offers a positive surplus to her. There is a cost associated with shipping the product to the consumer if she buys it. A consumer buys a maximum of one unit of one product in a shopping instance. The fixed and marginal production costs are assumed to be zero for all products. We normalize N to one in the theoretical analysis for expositional clarity.

## 3.1. Consumer Utility and Consumer Segments

Consumers are heterogeneous in their shopping $f r e -$ quency in the sense that some consumers face consumption needs and visit the platform more frequently than others during the time period we consider. For instance, the head of a household who has more family members is likely to shop more often than one who has fewer family members in his household. The shopping frequency defines the consumer type in our model. We assume that the σ fraction of the consumers includes infrequent shoppers, and the probability that a consumption need arises for an infrequent shopper in a shopping instance is $\gamma _ { l } .$ The rest, (1 � σ) fraction, of the consumers are frequent shoppers with the corresponding probability of having a consumption need at a shopping instance being $\gamma _ { h } ,$ where $\gamma _ { l } < \gamma _ { h }$ . We define ${ \mathcal { Z } } ( \sigma ,$ $\gamma _ { l } , \gamma _ { h } ) \triangleq \sigma \gamma _ { l } + ( 1 - \sigma ) \gamma _ { h } ( \mathcal { Z } _ { \cdot }$ , hereafter), which denotes the likelihood that a consumer (of unknown type) would visit the platform at any shopping instance. The consumer utility for a product at a shopping instance depends on her base valuation, which represents the value she derives from an ideal product that meets her need perfectly and the misfit cost if the product does not meet her need perfectly at that instance. A consumer’s base valuation and misfit cost can vary across shopping instances. We assume a consumer’s base valuation at a shopping instance, conditional on her having a consumption need, is low, $v _ { l } ,$ with probability θ and high, $v _ { h } ,$ with probability $( 1 - \theta )$ , where $v _ { l } < v _ { h }$ . We can consider the base valuation as capturing the intensity of the consumption need. For example, the need could be an essential one in one shopping instance but a nonessential one (i.e., a want/desire) in another instance for the same consumer. In the case of essential needs, the consumer would likely have a high valuation and buy a product to satisfy the need. On the other hand, in case of a nonessential need, she is more likely to have a low valuation and may purchase a product only if she finds a product that is sufficiently close to her preference. In other words, we assume that the market is fully covered when the base valuation is $v _ { h } ,$ and it is partially covered when the base valuation is $v _ { l } .$

To model consumer preference or misfit cost, we assume, for simplicity, that the platform offers two products that are imperfect substitutes from two different sellers. We denote the two products as A and B. For notational brevity, we refer to the respective sellers as A and B as well. We use a typical horizontal product differentiation model for the misfit cost. In particular, we assume that products A and B are located at positions 0 and 1 of a unit line, respectively. A consumer’s location at a shopping instance is equally likely to be at any point along the line. The distance between a consumer and a product at a shopping instance measures the degree of misfit of the product to the consumer at that instance. Notice that when the degree of misfit between a consumer and product A is $\lambda , \lambda \in [ 0 , 1 ]$ , the degree of misfit between the consumer and product B is $( 1 - \lambda )$ ). The misfit cost is the degree of misfit times a unit misfit cost t. Note that neither the base valuation $( v _ { l }$ and $v _ { h } )$ nor the degree of misfit (λ) are idiosyncratic types of consumers; on the other hand, the shopping frequency is.

The cost to ship the product to the consumer at any shopping instance during the period is $s ,$ regardless of who pays for it. This is reasonable in a context where the shipping is done by an independent logistics provider. We examine this context in order to focus on the strategic impacts related to who pays for shipping. We consider two scenarios that differ with respect to who bears the shipping cost. In the scenario in which the platform does not offer the MFS program, consumers incur the shipping cost. In the scenario in which the platform offers the MFS program, the platform bears the shipping cost of members, but nonmembers bear the shipping cost themselves. Thus, conditional on a consumer having a consumption need, if she has a base valuation $v ,$ $v \in \{ v _ { h } , v _ { l } \}$ , is located at $\lambda ,$ , and bears the shipping cost, then her net utility from products A and B is as follows:

$$
\begin{array}{l} {U _ {A} = v - p _ {A} - \lambda t - s,} \\ {U _ {B} = v - p _ {B} - (1 - \lambda) t - s.} \end{array}
$$

Here, $p _ { A }$ and $p _ { B } ,$ respectively, denote the prices of A and B. Clearly, if the platform bears the shipping cost for the consumer, then the shipping cost term will not be part of the net utility expressions.

A consumer knows whether she has a consumption need at a particular shopping instance, and if there is a need, she also knows her base valuation and her location on the Hotelling line before making the purchase decision at that shopping instance. Therefore, the expected demands (purchase frequencies hereafter) for a frequent shopper and an infrequent shopper, respectively, are given by $D _ { h } = ( 1 - \sigma ) \gamma _ { h } ( \theta ( ( 2 v _ { l } - p _ { A } - p _ { B } -$ $2 s ) / t ) + 1 - \theta )$ and $D _ { l } = \sigma \gamma _ { l } ( \theta ( ( 2 v _ { l } - p _ { A } - p _ { B } - 2 s ) / t ) +$ 1 � θ) if the consumer incurs the shipping cost.<sup>3</sup> The purchase frequency for a consumer type when the platform incurs the shipping cost for the consumer can be obtained by setting $s = 0$ in the expressions.

Neither the platform nor the sellers know the type of an individual consumer, whether a consumer has a need at a specific instance, her base valuation, or the consumer’s location. However, the sellers and the platform know the distributions of consumers’ shopping frequency, base valuation, and location.

## 3.2. Timing of the Game

The sequence of events is as follows. In stage 1, the platform announces a (per-member) membership fee M at the beginning of the period and commits to bearing the member’s shipping costs during the period. In stage $^ { 2 , }$ consumers decide whether to participate in the MFS program, also at the beginning of the period. In stage 3, sellers choose their prices simultaneously.<sup>4</sup> In stage 4, consumers who face a consumption need visit the platform and make their purchase decisions, and all parties realize their payoffs. In the case where the platform does not offer the MFS program, stage 1 and stage 2 are irrelevant, and the game starts from stage 3.

All players are risk neutral. Table 1 in the online supplement summarizes the main notation used in the paper. We use subscript $i , i \in \{ A , B \}$ , to denote sellers/ products and superscript $j , j \in \{ b , m \}$ , to denote the program scenarios—no MFS (b) and MFS (m). We make the following technical assumptions in our analysis:

$$
\begin{array}{l} s + \frac {t (1 - \theta) + \frac {2 s \theta (1 - \sigma) \gamma_ {h}}{\mathcal {Z}}}{1 + \theta} <   v _ {l} \\ <   \frac {t (3 + \theta) (1 - \sigma) \gamma_ {h} + [ t (3 + \theta) - 4 s \theta ] \sigma \gamma_ {l}}{2 (1 + \theta) \mathcal {Z}}. \\ v _ {h} > \frac {2 s (1 + \theta) + t (3 + \theta) + 4 \theta \left(v _ {l} + \frac {s (1 - \sigma) \gamma_ {h}}{\mathcal {Z}}\right)}{2 (1 + 3 \theta)}. \end{array}
$$

The first assumption ensures that if a consumer has a low valuation in a shopping instance, then she would buy a product if she has a low misfit cost to at least one of the two products and not buy either product otherwise. The second assumption ensures that if a consumer has a high valuation in a shopping instance, she would buy one of the two products.

## 3.3. No MFS (Benchmark Scenario)

In this section, we derive the subgame perfect equilibrium for the scenario without the MFS program.<sup>5</sup> If a consumer has a consumption need, has a base valuation $v _ { h } ,$ and is located at λ at the shopping instance, she will buy product A if $U _ { A } > U _ { B }$ and will buy product B otherwise. We can verify that she will buy product A if $\lambda <$ $( t - p _ { A } ^ { b } + p _ { B } ^ { b } ) / 2 t$ and product B otherwise. On the other hand, if the same consumer has a base valuation $v _ { l } ,$ then she will buy product A if $\lambda < ( v _ { l } - p _ { A } ^ { b } - s ) / t$ , buy product B if $\lambda > 1 - ( v _ { l } - p _ { B } ^ { b } - s ) / t .$ , and will not buy any product otherwise.

In stage 3, at the beginning of the shopping instance, sellers choose prices to maximize their expected profits given as follows:

$$
\begin{array}{l} \underset {p _ {A} ^ {b}} {\arg \max} \pi_ {A} ^ {b} \\ = \mathcal {Z} \bigg [ \theta \frac {v _ {l} - p _ {A} ^ {b} - s}{t} + (1 - \theta) \frac {t - p _ {A} ^ {b} + p _ {B} ^ {b}}{2 t} \bigg ] p _ {A} ^ {b} (1 - \alpha), \end{array}\tag{1}
$$

$$
\begin{array}{l} \underset {p _ {B} ^ {b}} {\arg \max} \pi_ {B} ^ {b} \\ = \mathcal {Z} \bigg [ \theta \frac {v _ {l} - p _ {B} ^ {b} - s}{t} + (1 - \theta) \frac {t - p _ {B} ^ {b} + p _ {A} ^ {b}}{2 t} \bigg ] p _ {B} ^ {b} (1 - \alpha). \end{array}\tag{2}
$$

Seller A computes his expected demand as the product of the likelihood of the consumers visiting the platform $\mathcal { Z }$ and the expected demand from the visiting consumers $[ \theta ( v _ { l } - p _ { A } ^ { b } - s ) / t + ( 1 - \theta ) ( t - p _ { A } ^ { b } + p _ { B } ^ { b } ) / 2 t ] .$ , as in Equation (1). Analogously, seller B computes his expected demand as in Equation (2).

Solving the first-order conditions for the sellers’ maximization problems, we obtain the optimal retail prices.

Lemma 1. In the absence of the MFS program, in equilib rium, the retail prices $p _ { A } ^ { b * }$ and $p _ { B } ^ { b * }$ , purchase frequency of frequent shoppers $\mathsf { D } _ { h } ^ { b * }$ , and purchase frequency of infrequent shoppers $\dot { D } _ { l } ^ { b * }$ are as follows:

$$
\begin{array}{l} p _ {A} ^ {b *} = \frac {2 \theta (v _ {l} - s) + t (1 - \theta)}{1 + 3 \theta}, \\ p _ {B} ^ {b *} = \frac {2 \theta (v _ {l} - s) + t (1 - \theta)}{1 + 3 \theta}, \\ D _ {h} ^ {b *} = \frac {(1 + \theta) [ 2 \theta (v _ {l} - s) + t (1 - \theta) ] (1 - \sigma) \gamma_ {h}}{t (1 + 3 \theta)}, \\ D _ {l} ^ {b *} = \frac {(1 + \theta) [ 2 \theta (v _ {l} - s) + t (1 - \theta) ] \sigma \gamma_ {l}}{t (1 + 3 \theta)}. \end{array}
$$

Proof. All proofs are in the online supplement unless indicated otherwise. w

Using Lemma 1, we compute the equilibrium platform profit $\pi _ { R } ^ { b * }$ , consumer surplus $C S ^ { b * }$ , and social welfare $\bar { S W } ^ { b * }$ in the no MFS scenario, where we define the social welfare as the summation of sellers’ profits, platform profit, and consumer surplus. We provide the expressions for these in the online supplement. We confirm that an increase in shipping cost s reduces the equilibrium prices because the sellers will expect a smaller demand when the shipping cost is higher. The purchase frequency of each type also decreases in s even though sellers set a lower price because the reduction in price does not offset the increase in the shipping cost. Consequently, both the sellers’ profits and the platform’s profits decrease in s.

## 4. Analysis of the MFS Program

We derive the subgame perfect equilibrium for the scenario with the MFS program and then compare the equilibria with and without the MFS program to identify the impact of the MFS program. If the platform implements the MFS program, it can induce one of two possible equilibria. (i) Only frequent shoppers become members, or (ii) both frequent shoppers and infrequent shoppers become members.<sup>6</sup> Furthermore, the case where only infrequent shoppers become members cannot be an equilibrium because if an infrequent shopper finds it profitable to become a member, so will a frequent shopper because a frequent shopper would expect to save more in shipping costs by joining the MFS program than an infrequent shopper. In this paper, we focus on the equilibrium in which only frequent shoppers join the MFS program as this scenario is more likely in practice than the one in which all consumers join the MFS program. We performed the analysis for the equilibrium where both frequent and infrequent shoppers join the program and found the insights presented in this paper to hold in that equilibrium as well.<sup>7</sup>

In stage 4 of the game under the MFS program, a member’s purchase decision can vary from that of a nonmember because a member does not bear the shipping cost, whereas a nonmember does. A nonmember’s purchase decision rule remains the same as that under the benchmark scenario. On the other hand, if the consumer is a member, she will buy product A if $\lambda <$ $( t - p _ { A } ^ { m } + p _ { B } ^ { m } ) / 2 t$ and product B otherwise if her base valuation is $v _ { h } ;$ if the base valuation is $v _ { l } ,$ then she will then buy product A if $\lambda < ( v _ { l } - p _ { A } ^ { m } ) / t .$ , buy product B if $\lambda > 1 - ( v _ { l } - p _ { B } ^ { m } ) / t .$ , and will not buy any product otherwise.

In stage 3, the expected seller profits depend on the size and the composition of the membership base. We can show that in the equilibrium, all frequent shoppers would choose to join the MFS program, and hence, the sellers’ pricing problems in equilibrium are formulated

as

$$
\begin{array}{l} \underset {p _ {A} ^ {m}} {\arg \max} \pi_ {A} ^ {m} = \left[ \sigma \gamma_ {l} \bigg (\theta \frac {v _ {l} - p _ {A} ^ {m} - s}{t} + (1 - \theta) \frac {t - p _ {A} ^ {m} + p _ {B} ^ {m}}{2 t} \bigg) \right. \\ + (1 - \sigma) \gamma_ {h} \bigg (\theta \frac {v _ {l} - p _ {A} ^ {m}}{t} + (1 - \theta) \frac {t - p _ {A} ^ {m} + p _ {B} ^ {m}}{2 t} \bigg) \bigg ] p _ {A} ^ {m} (1 - \alpha), \\ \underset {p _ {B} ^ {m}} {\arg \max} \pi_ {B} ^ {m} = \left[ \sigma \gamma_ {l} \bigg (\theta \frac {v _ {l} - p _ {B} ^ {m} - s}{t} + (1 - \theta) \frac {t - p _ {B} ^ {m} + p _ {A} ^ {m}}{2 t} \bigg) \right. \\ + (1 - \sigma) \gamma_ {h} \bigg (\theta \frac {v _ {l} - p _ {B} ^ {m}}{t} + (1 - \theta) \frac {t - p _ {B} ^ {m} + p _ {A} ^ {m}}{2 t} \bigg) \bigg ] p _ {B} ^ {m} (1 - \alpha). \end{array}
$$

In stage 2, a consumer will join the program only if her expected (purchase-related) surplus gain by joining the MFS program compared with not joining is not less than the membership fee, $M ^ { m }$ . The expected surplus gain would depend on the consumer’s belief about how many consumers would join the program. Moreover, for the equilibrium to sustain, the platform’s belief about the size of the membership base when it sets the membership fee should be consistent with the consumers’ belief as well. We show in the online supplement that the only sustainable belief in the equilibrium is all frequent shoppers join the MFS program. Therefore, for a frequent shopper, the expected surplus with the membership is given by

$$
\begin{array}{l} \gamma_ {h} \left[ \int_ {0} ^ {\frac {v _ {l} - p _ {A} ^ {m}}{t}} \theta (v _ {l} - p _ {A} ^ {m} - \lambda t) d \lambda + \int_ {0} ^ {\frac {t - p _ {A} ^ {m} + p _ {B} ^ {m}}{2 t}} (1 - \theta) (v _ {h} - p _ {A} ^ {m} - \lambda t) d \lambda \right. \\ \left. + \int_ {0} ^ {\frac {v _ {l} - p _ {B} ^ {m}}{t}} \theta (v _ {l} - p _ {B} ^ {m} - \lambda t) d \lambda + \int_ {0} ^ {\frac {t - p _ {B} ^ {m} + p _ {A} ^ {m}}{2 t}} (1 - \theta) (v _ {h} - p _ {B} ^ {m} - \lambda t) d \lambda \right]. \end{array}
$$

The expected surplus for a frequent shopper without the membership is given by

$$
\begin{array}{c} \gamma_ {h} \left[ \int_ {0} ^ {\frac {v _ {l} - p _ {A} ^ {m} - s}{t}} \theta (v _ {l} - p _ {A} ^ {m} - \lambda t - s) d \lambda + \int_ {0} ^ {\frac {t - p _ {A} ^ {m} + p _ {B} ^ {m}}{2 t}} (1 - \theta) \right. \\ \left. (v _ {h} - p _ {A} ^ {m} - \lambda t - s) d \lambda \right. \\ + \left. \int_ {0} ^ {\frac {v _ {l} - p _ {B} ^ {m} - s}{t}} \theta (v _ {l} - p _ {B} ^ {m} - \lambda t - s) d \lambda + \int_ {0} ^ {\frac {t - p _ {B} ^ {m} + p _ {A} ^ {m}}{2 t}} (1 - \theta) \right. \\ \left. (v _ {h} - p _ {B} ^ {m} - \lambda t - s) d \lambda \right]. \end{array}
$$

We can compute the expected surplus for an infrequent shopper with and without the membership by replacing $\gamma _ { h }$ with $\gamma _ { l }$ in the expressions.

For a frequent shopper, the expected surplus gain by joining the MFS program as compared with not joining is the difference between the two terms. Then, in stage 1, the platform would set the membership fee to an amount that is slightly less than the frequent shopper’s surplus gain; any fee less than this amount only reduces the platform’s profit, and any fee higher than this amount implies that the frequent shoppers would find it undesirable to join the program. When the platform sets the membership fee $M ^ { m }$ to be slightly less than her surplus gain, a frequent shopper that is deciding whether to join the MFS program will find that joining is better than not joining. Furthermore, we can show that an infrequent shopper’s surplus gain from joining the MFS program is less than the membership fee. Thus, an individual frequent shopper’s decision would be to join the program, and an individual infrequent shopper’s decision would be to not join the program.

Lemma 2. If the platform implements the MFS program, in equilibrium, the membership fee $M ^ { m * }$ , retail prices $p _ { A } ^ { m * }$ and $p _ { B } ^ { m * }$ , purchase frequency of frequent shoppers $D _ { h } ^ { m * }$ , and $p u r -$ chase frequency of infrequent shoppers $\dot { D _ { l } ^ { m * } }$ are as follows:

$$
\begin{array}{r l} & M ^ {m *} = \frac {s [ (1 - \sigma) (2 \theta (1 + \theta) v _ {l} + t - s \theta - (t + 3 s) \theta^ {2}) \gamma_ {h}}{+ \sigma ((1 - \theta) (t + t \theta - s \theta) + 2 \theta (1 + \theta) v _ {l}) \gamma_ {l} ] \gamma_ {h}}, \\ & p _ {A} ^ {m *} = \frac {(t (1 - \theta) + 2 \theta v _ {l}) (1 - \sigma) \gamma_ {h} + (t (1 - \theta)}{(1 + 3 \theta) \mathcal {Z}}, \\ & p _ {B} ^ {m *} = \frac {(t (1 - \theta) + 2 \theta v _ {l}) (1 - \sigma) \gamma_ {h} + (t (1 - \theta)}{(1 + 3 \theta) \mathcal {Z}}, \\ & D _ {h} ^ {m *} = \frac {[ (1 + \theta) (2 v _ {l} \theta + t (1 - \theta)) (1 - \sigma) \gamma_ {h} + (t (1 - \theta^ {2})}{+ 2 \theta (v _ {l} + v _ {l} \theta + 2 s \theta)) \sigma \gamma_ {l} ] (1 - \sigma) \gamma_ {h}}{t (1 + 3 \theta) \mathcal {Z}}, \\ & D _ {l} ^ {m *} = \frac {[ (t (1 - \theta^ {2}) + 2 \theta (v _ {l} (1 + \theta) - s - 3 s \theta)) (1 - \sigma) \gamma_ {h}}{+ (1 + \theta) (2 \theta (v _ {l} - s) + t (1 - \theta)) \sigma \gamma_ {l} ] \sigma \gamma_ {l}}. \end{array}
$$

Using Lemma 2, we compute the equilibrium platform profit $\pi _ { R } ^ { m * }$ , consumer surplus $C S ^ { m * }$ , and social welfare $S W ^ { m * }$ . These are provided in the online supplement. We show that the equilibrium prices decrease in the shipping cost $s ,$ as in the benchmark scenario. It is intuitive that the nonmembers’ $( \mathrm { i . e . } ,$ , infrequent shoppers’) purchase frequency decreases in $s ,$ as in the benchmark scenario. On the other hand, in contrast to the benchmark case, the members’ (i.e., frequent shoppers’) purchase frequency increases in s under the MFS program. The reason is that an increase in the shipping cost leads to a decrease in prices. However, the price decrease does not offset the increase in the shipping cost for the infrequent shoppers, and therefore, the infrequent shopper segment’s demand decreases in the shipping cost. In contrast, frequent shoppers do not have to pay for shipping; hence, their demand increases in the shipping cost.

Proposition 1. If the platform implements the MFS program, in equilibrium, the platform’s revenue from the mem bership fee is less than the shipping cost it incurs.

Proposition 1 shows that the platform subsidizes the shipping cost of its members by charging a membership fee that is less than the shipping cost it would incur for purchases made by the member. This result confirms the assumption made by Fang et al. (2021) that only consumers with a total shipping cost greater than the membership fee join the MFS program. Proposition 1 is consistent with data from Amazon’s Prime program, which are shown in Figure 1. The figure shows Amazon’s revenue from Prime memberships during the years 2006–2016 (Amazon introduced the Prime program in 2005). We note that the revenues shown in the figure include only the portion of the membership fee that is attributed to the free shipping benefit because the Prime program includes benefits other than free shipping as well. The figure also shows the shipping costs incurred by Amazon to serve the members. We make the following observations from this figure. (i) The shipping cost is higher than the revenue every year, and (ii) the gap between revenue and shipping cost, which represents the shipping cost subsidy to members, has been steadily increasing from \$317 million in 2006 to \$7.19 billion in 2016. We note that the number of Prime members also increased during this period, and the subsidy grew along with it.

Proposition 1 provides theoretical support to the argument that the online retail platforms are hurt by the MFS programs when the program is evaluated solely based on membership revenue and shipping costs. However, the following result demonstrates that this conclusion may be unwarranted.

Proposition 2. If the platform implements the MFS program, the platform’s equilibrium profit is higher compared with the no MFS benchmark if and only $i f s < s ^ { m * }$ , where

$$
\begin{array}{r} s ^ {m *} = \frac {4 \alpha (1 + \theta) [ t (1 - \theta) + 2 \theta v _ {l} ] \mathcal {Z}}{[ 1 + (6 + 4 \alpha) \theta + (9 + 4 \alpha) \theta^ {2} ] (1 - \sigma) \gamma_ {h}}. \\ + [ 1 + (6 + 8 \alpha) \theta + (9 + 8 \alpha) \theta^ {2} ] \sigma \gamma_ {l} \end{array}
$$

Proposition 2 shows that the platform would be hurt by the MFS program only when the shipping cost is high. Clearly, the platform’s shipping subsidy to members, demonstrated by Proposition $^ { 1 , }$ would be prohibitively high if the shipping cost is high. It is worth pointing out that Amazon excludes high shipping cost items, such as bulky items, from its Prime program.<sup>8</sup> However, when the shipping cost is not high, despite the shipping subsidy, the platform benefits from the MFS program. We identify two strategic impacts of the MFS program that contribute to the higher platform profit with the MFS program compared with the benchmark scenario when s is not high.

Figure 1. (Color online) Shipping Subsidy of Amazon  
![](/api/attachments/DBT6WQND/fulltext/images/16a2caaf22f96b9988c413fd18086e29a3abc26356e4988d834bd6d7afc9f6df.jpg)  
Source. https://www.statista.com/chart/6527/amazon-shipping-costs/.

## 4.1. Impact on Price

By comparing equilibrium prices, we find that the retail prices are higher when the platform implements the MFS program than when it does not. Sellers recognize that members incur a smaller purchase cost compared with when there is no MFS program because they do not incur the shipping cost. Consequently, sellers increase their prices and extract some of the members’ savings in the shipping cost when the platform implements the MFS program. Fang et al. (2021) also find a similar result in the context of the e-tailer that makes both MFS-related and product pricing decisions. In our context, the result is noteworthy because the popular press reports note that Amazon encouraged third-party sellers to inflate their prices after it introduced the Prime program (GeekWire 2014). We denote this impact of the MFS program on the prices as the price-increasing effect. The price-increasing effect of the MFS program can be quantified as

$$
\Delta p _ {i} ^ {*} = p _ {i} ^ {m *} - p _ {i} ^ {b *} = \frac {2 s \theta (1 - \sigma) \gamma_ {h}}{(1 + 3 \theta) \mathcal {Z}} > 0.
$$

## 4.2. Impact on Demand

By comparing equilibrium demands, we find that the purchase frequency of members of the MFS program is higher compared with when there is no MFS program. On the other hand, we find that the purchase frequency of nonmembers is lower. The nonmembers purchase less because of the price-increasing effect discussed previously. The members purchase more despite the price-increasing effect because the shipping cost savings offset the price increase. Although the impacts on the two groups—members and nonmembers—are in opposite directions, we find that the net impact of the MFS program on the overall purchase frequency is positive. We denote this impact of the MFS program on the overall purchase frequency of consumers as the demand enhancement effect. We quantify the demand effects as follows:

$$
\begin{array}{r l} & {\Delta D _ {h} ^ {*} = D _ {h} ^ {m *} - D _ {h} ^ {b *}} \\ & {\qquad = \frac {2 s \theta (1 - \sigma) \gamma_ {h} ((1 + \theta) (1 - \sigma) \gamma_ {h} + (1 + 3 \theta) \sigma \gamma_ {l})}{t (1 + 3 \theta) \mathcal {Z}} > 0,} \\ & {\Delta D _ {l} ^ {*} = D _ {l} ^ {m *} - D _ {l} ^ {b *} = - \frac {4 s \theta^ {2} (1 - \sigma) \sigma \gamma_ {l} \gamma_ {h}}{t (1 + 3 \theta) \mathcal {Z}} <   0,} \\ & {\Delta D ^ {*} = \Delta D _ {h} ^ {m *} + \Delta D _ {l} ^ {m *} = \frac {2 s \theta (1 + \theta) (1 - \sigma) \gamma_ {h}}{t (1 + 3 \theta)} > 0.} \end{array}
$$

The demand effect we have identified is new to the literature and is consistent with practice as well. It has

① MFS Profitable ②MFS Unprofitable ③&4Infeasible Regions

been reported that an Amazon Prime member spends an average of \$1,400 a year on Amazon, whereas a nonmember spends only $\$ 600.$ Even though the higher shopping frequency of a member compared with a nonmember could partly explain this difference in spending, Proposition 2 shows that the differential impacts of the MFS program on members and nonmembers could be a key contributor to it as well.

The explained effects of the MFS program are positive for the platform; however, the platform is not always better off with the MFS program because of the shipping subsidy, as shown in Proposition 1. To further explain Proposition $^ { 2 , }$ we decompose the platform profit under the MFS program into three components: commission revenue received from the sellers (CR), membership fee paid by subscribing consumers (MF), and absorbed shipping cost (SC). Clearly, CR is higher if the platform implements the MFS program than if it does not because the price-increasing effect and the demand enhancement effect of the MFS program improve the overall commission revenue. Thus, in light of Proposition 1, whether the platform benefits from the MFS program depends on whether the increase in the commission revenue, $C R ^ { m * } - \pi _ { R } ^ { b * }$ , compensates for the shipping cost subsidy to members, $S C ^ { \widehat { m } * } - M F ^ { m * }$ . When the shipping cost is smaller than $s ^ { m * }$ given in Proposition 2, the subsidy is smaller than the increase in the commission revenue, and the platform benefits from the MFS program. However, when the shipping cost is above s<sup>m∗</sup>, the platform is hurt by the MFS program.

Proposition 2 reveals the role of the shipping cost in the MFS program’s profitability to the platform. We are unable to theoretically analyze the roles of other key model parameters on the MFS program profitability.

Therefore, we resort to numerical illustrations to provide additional insights. In particular, we highlight the roles of θ and σ. Because the parameter θ denotes the probability that a consumer has a low base valuation in a shopping instance, the impact of θ on the platform’s MFS program profitability shows how the product types that are included for free shipping (i.e., essential products that have a higher likelihood of a high valuation versus discretionary products that have a higher likelihood of a low valuation) in the MFS program affect its profitability for the platform. On the other hand, the parameter σ denotes the probability that a consumer is an infrequent shopper. Thus, the impact of σ on the platform’s MFS program profitability shows how the market type in which the MFS program is deployed (i.e., markets with predominantly heavy online shoppers versus those where there are predominantly light online shoppers) affects its profitability for the platform. Figure 2 illustrates these impacts. We find that a smaller θ is more likely to favor the outcome in which the platform benefits from the MFS program, suggesting that the MFS program is more likely to be profitable for essential products. Moreover, we find that a smaller σ could more likely favor the outcome in which the platform benefits from the MFS program, especially when θ is moderate, suggesting that the MFS program is more likely to be profitable in markets characterized by heavy online shopping. By comparing panels (a) and (b) in Figure 2, we also find that the region in which the MFS program is profitable to the platform shrinks as the shipping cost increases, which is consistent with Proposition 2.

To gain additional insights about the impact of the MFS program on the platform, we quantify the value of the MFS program to the platform as $\Delta \pi _ { R } ^ { * } = \pi _ { R } ^ { m * } - \pi _ { R } ^ { b * }$ The following result shows how the value of the MFS program to a platform is affected by the shipping cost.

Figure 2. (Color online) Profitability of MFS  
![](/api/attachments/DBT6WQND/fulltext/images/9ace0f3cdc7cf714d42224f28552d18104ee6a96b9bf95d11d72c494b66cb6f5.jpg)  
Notes. α � 0:15, t � 2, v � 2, γ � 0:5, γ � 0:2. (a) s � 0.4. (b) s � 0.55

(b)  
![](/api/attachments/DBT6WQND/fulltext/images/b554e0e380fc68e8bb3b5a2aa95b92bf2cbed523e18820a6fd13ac65d747abed.jpg)

Proposition 3. The value of the MFS program to the platform $\Delta \pi _ { R } ^ { * }$ increases in s when $s < s ^ { m * } / \dot { 2 }$ and decreases in s when $s > s ^ { m * } / 2$

Proposition 3 shows that the value of the MFS program to the platform follows an inverted U shape with respect to s and that the value is highest when the shipping cost is equal to $s ^ { m * } / 2$ . The dynamics of the three components of platform profit—CR, MF, and SC—with respect to the shipping cost s determine how the value of the MFS program is affected by s. The following derivatives explain these dynamics:

$$
\begin{array}{r l r} & & {\frac {\partial (C R ^ {*} - \pi_ {R} ^ {b *})}{\partial s} = - \frac {8 \theta^ {2} (1 + \theta) (1 - \sigma) \gamma_ {h} (2 \sigma \gamma_ {l} + (1 - \sigma) \gamma_ {h})}{t (1 + 3 \theta) ^ {2} \mathcal {Z}}} \\ & & {\times s + \frac {4 \theta (1 + \theta) (1 - \sigma) (t (1 - \theta) + 2 \theta v _ {l}) \gamma_ {h}}{t (1 + 3 \theta) ^ {2}},} \\ & & {\frac {\partial (S C ^ {*} - M F ^ {*})}{\partial s} = \frac {\theta (1 - \sigma) \gamma_ {h}}{t} \times s.} \end{array}
$$

We observe that the shipping subsidy offered by the platform to members is increasing in s in a convex fashion $( \mathrm { i . e . , ~ } \partial ( S C ^ { * } - M F ^ { * } ) / \partial s$ is positive and increasing in s). The convexity arises because an increase in the shipping cost increases the demand from members (recall the discussion following Lemma 2). Therefore, an increase in the shipping cost not only increases the subsidy each time a member makes a purchase but also increases the purchase frequency of members. On the other hand, the benefit from the program in the form of an increase in the commission revenue is increasing in s in a concave fashion (i.e., $\partial ( C R ^ { * } - \pi _ { R } ^ { b * } ) / \partial s$ is positive and decreasing in s). The quadratic nature of the platform’s value from the MFS program implies that the value is highest when $s = s ^ { m * } \bar { / } 2$ . We can also verify that the value is zero when $s = 0 ,$ . The primary implication of Proposition 3 is that the platform finds the MFS program to be most attractive at moderate values of the shipping cost. Thus, the MFS program is likely to be most valuable in the context of online marketplaces selling physical goods where the shipping cost plays a role and it is neither excessive nor inconsequential. More importantly, even though we do not consider any cost to implement the MFS program, if there is an implementation cost, the platform will implement the MFS program only when the shipping cost is neither too high nor too low.

Proposition 4. If the platform implements the MFS program, the equilibrium consumer surplus is less than that in the no MFS benchmark.

Proposition 4 reveals that consumers as a whole are worse off when the platform implements the MFS program than when it does not. The nonmembers are worse off with the MFS program because of the priceincreasing effect; nonmembers not only pay higher prices but also, consume less when the platform implements the MFS program than when it does not. The reduction in nonmembers’ surplus has implications for members as well as the platform. For members, it seems that they should be better off when the platform implements the MFS program than when it does not because the members choose between two options— joining and not joining the MFS program—that gives them a higher expected surplus. However, we find that even members are actually worse off under the MFS program compared with the benchmark. The explanation for this finding is the following.

Consider a frequent shopper deciding whether to join the program. Because of the adverse effect of the pro gram on nonmembers, she will expect to suffer a loss in surplus if she does not join the program. On the other hand, by joining the program, she will expect a positive purchase-related surplus gain. The expected surplus gain when she joins the program as opposed to the sur plus loss when she does not provides her an incentive to join the program. Recognizing this incentive, the platform charges a membership fee that is just less than the difference in surplus between joining and not joining, which is equal to the surplus gain from joining plus the surplus loss from not joining. That ${ \mathrm { i } } \mathbf { s } ,$ the platform extracts more than just the savings a consumer would enjoy by joining the program compared with when no one joins the program; it also extracts an additional amount equal to the loss in surplus if she does not join the program. Consequently, even the members end up being hurt by the MFS program compared with the benchmark. Essentially, the platform exploits the differ ential impacts of the MFS program on the two consumer types and forces frequent shoppers to choose between two options—joining and not joining—both of which hurt them compared with when there is no MFS pro gram but joining hurts them less. In this regard, MFS can also be considered as a strategy that allows the sellers to more efficiently extract surplus from each consumer segment, mitigating the well-known cannibalization problem (Clemons and Weber 1994, Riggins 2004).

We note that when the platform implements the MFS program, between the two options—joining the MFS program and not joining the MFS program—joining the MFS program is the best response for a frequent shopper in the equilibrium. Meanwhile, Proposition 4 shows that members become worse off. Hence, even though every single frequent shopper acts in her best interest and becomes a member, collectively all of them are hurt by the MFS program. Thus, consumer participation in the MFS program is effectively a prisoner’s dilemma for consumers.

Proposition 5. If the platform implements the MFS program, the equilibrium social welfare is higher than that in the no MFS benchmark if and only ${ i f s < \overline { { s } } ^ { m } }$ , where

$$
\overline {{s}} ^ {m} = \frac {2 (1 + \theta) (t (1 - \theta) + 2 \theta v _ {l}) \mathcal {Z}}{(1 + \theta) (1 + 5 \theta) (1 - \sigma) \gamma_ {h} + (1 + \theta (1 0 + 1 3 \theta)) \sigma \gamma_ {l}}.
$$

As shown in Proposition 5, the impact of the MFS program on social welfare can be positive or negative, similar to that on the platform profit. The possible negative impact of MFS on social welfare is somewhat surprising given that the MFS program enhances the overall demand, which enhances the consumption utility. The reason for the possible adverse impact of the MFS program on social welfare lies in the nature of additional demand generated by the MFS program. We note that social welfare is affected by the (purchasing) consumers’ gross utility (i.e., valuation minus the misfit cost, excluding product prices that simply transfer wealth from one party to another within the society) and the cost of satisfying the demand from these consumers. The only cost in satisfying the demand in our context relates to shipping. The MFS program increases the total gross utility of consumers driven solely by the additional demand generated by the MFS program. However, if the shipping cost is higher than the threshold given in Proposition 5, then the cost required to satisfy this demand offsets the additional utility it generates.

Consider the marginal consumers who are indifferent between buying and not buying when there is no MFS program. These consumers have a low valuation of the product. They are farther away from the product they are indifferent between buying and not buying and hence, have a higher misfit cost compared with other low-valuation buyers who buy. Essentially, these marginal consumers have a low gross utility for the products. If they have to bear the shipping cost, as in the no MFS case, they do not find it profitable to buy either product. On the contrary, under the MFS program, if these consumers are members, they do not incur the shipping cost, and they will buy the product that is closer to them. In fact, even some members who are farther than these marginal consumers could end up buying a product under the MFS program, but they would not buy any product in the absence of the MFS program. These consumers are those who constitute the demand enhancement effect among members. These consumers generate very low additional utility because of their low valuation and high misfit costs. However, the flip side is that the same shipping cost is required to fulfill their demand as that from consumers who have high valuation and low misfit cost. The MFS program removes the shipping cost from the consideration of members when they make the purchase decisions, but society still incurs this cost. When the shipping cost is high, the MFS program stimulates demand from lowvaluation members even when their misfit cost is high at the expense of the platform and society, which incur the shipping cost. This could lead to a smaller social welfare when the platform implements the MFS program than when it does not.

We checked the robustness of our findings related to the impact of the MFS program by analyzing several model extensions and generalizations. We present these analyses in the online supplement. In particular, we considered scenarios where (i) the platform offers contingent-free shipping on top of MFS, (ii) sellers set a shipping fee for consumers, (ii) the MFS program offers additional benefits (purchase related and nonpurchase related) on top of free shipping, (iii) the sellers are asymmetric, and (iv) the platform incurs a lower shipping cost compared with individual sellers on the platform. The analyses reveal that although the MFS program can have an additional impact under these scenarios, those identified in this section remain intact.

## 5. Managerial Implications and Conclusion

As one of the first studies on the membership-based free shipping programs by online retail platforms, this paper offers nontrivial theoretical insights into these programs and provides valuable implications for practicing managers. On the theoretical side, our study shows why MFS can be a viable solution to the product shipping issue salient in online retailing and a strategy to enhance online retail platforms’ profit. Viewing MFS programs as a cost-transfer mechanism not only dilutes the impact of these programs but also, leads to incorrect conclusions about their value to various stakeholders.

On the practical side, our findings prescribe how online retail platforms should make decisions when offering MFS programs. In particular, platform managers have to pay special attention to not so obvious strategic influences of MFS programs to benefit from these programs. First, platforms should not view membership fee as the main source of revenue to drive profit from these programs. The main reason is that MFS programs are generally implemented by platforms where third-party sellers make product pricing decisions. Thus, it is not possible for the platform to keep the product margin low enough and rely mainly on the membership fee for profit. On the contrary, platforms should be will ing to subsidize their members by setting a membership fee that does not fully reap the cost of free shipping. Otherwise, a myopic view that focuses solely on the platform’s shipping subsidy may lead to program failure, even though the program can actually be profitable if properly implemented.

Second, although an MFS program is generally profitable when the shipping cost is low, an online retail platform does not necessarily gain more from MFS programs if the shipping cost goes down; the shipping cost has a nonmonotonic effect on the platform’s profit from the MFS program. In fact, the platform benefits the most when the shipping cost is neither too low nor too high. Therefore, if the platform has the opportunity to lower the shipping cost, through initiatives such as forming alliances with logistics providers or investing in in-house delivery, the benefits of such initiatives should be carefully evaluated as these efforts may lower the incentives for consumers to join the MFS program in the first place.

Third, our numerical analysis suggests that the platform is likely to profit from the MFS program when it includes essential products and in markets with a large fraction of frequent online consumers. Thus, the platform can reap maximum benefit from the MFS program when it judiciously chooses the product assortment strategy for the MFS program and introduces the program in carefully selected markets, tailored to the specific market with possibly different membership fees.

Finally, although MFS programs enable more consumption, the additional demand may not always be welfare enhancing. This is true even though we did not explicitly model any societal costs other than the shipping cost. To alleviate the potential adverse influences on a platform’s reputation and promote a socially responsible image, platform managers should make efforts on initiatives that mitigate or compensate for MFS’s negative societal impacts. For instance, Amazon’s pledge to reduce its carbon footprint to zero by 2040 (Shieber 2019) with the help of electric delivery trucks could be an effort in the right direction to make the MFS program acceptable to other stakeholders.

Our study can be extended in several directions. First, we assume the platform has no competitors in the marketplace. This assumption, although limiting, does not conflict with reality in a significant way as evidenced by Amazon’s monopolistic power in the online retailing business (Dayen 2019). Yet, examining a model with platform competition would provide additional insights into how the MFS program affects the nature and intensity of competition between platforms. Second, we assume that the sellers do not resort to price discrimination with the help of this program, even though the platform would have the ability to distinguish members from nonmembers. Finally, the presence of multiple shipping options with different delivery times suggests that a comparative study of numerous shipping options found on different platforms may be a valuable extension of our research.

## Endnotes

<sup>1</sup> Although Fang et al. (2021) consider an extension in their online supplement in which member consumers purchase more frequently after becoming a member, the increase in the purchase frequency (i.e., the demand-enhancing effect of the MFS program) is exogenously specified.

<sup>2</sup> Endogenizing the commission rate does not change our results and insights. The derivation of the model is available from the author upon request.

<sup>3</sup> The purchase frequency is different from the shopping frequency as consumers may not purchase a product in some shopping instance even if they shop. In addition, although the shopping frequency is exogenous, the purchase frequency is endogenous.

<sup>4</sup> Prices of online retailers are generally less rigid (Bergen et al. 2005). Hence, the pricing decisions occur after the MFS participation decisions.

<sup>5</sup> We use the scenario where the consumer pays the full cost of shipping whenever she buys as the benchmark so that we can tease out the impacts of the MFS program that transfers the full shipping cost of members to the platform.

<sup>6</sup> There can potentially be another equilibrium in which neither frequent nor infrequent consumers (i.e., no consumer) become members. The outcomes of this equilibrium are identical to those in the no MFS (benchmark) scenario, which we analyze in Section 3.3. We assume that the platform would not implement the MFS program that would induce an equilibrium with outcomes that are identical to those in the no MFS scenario.

<sup>7</sup> Detailed analysis is available upon request from the authors.

<sup>8</sup> Amazon either does not offer free shipping or does not promise the delivery schedule offered under the Prime program for these products (https://www.fool.com/the-ascent/personal-finance/articles/the average-amazon-prime-member-spends-this-much-per-year/).

<sup>9</sup> See https://www.cirpllc.com/blog/2018/9/25/amazon-primemembership-growth-slows.

## References

Ali A (2022) Visualizing Amazon’s rising shipping costs. Accessed June 23, 2023, https://www.visualcapitalist.com/visualizingamazons-rising-shipping-costs/.

Ashley C, Gillespie EA, Noble SM (2016) The effect of loyalty program fees on program perceptions and engagement. J. Bus. Res. 69(2):964–973.

Aviv Y, Pazgal A (2008) Optimal pricing of seasonal products in the presence of forward-looking consumers. Manufacturing Service Oper. Management 10(3):339–359.

Bergen ME, Kauffman RJ, Lee D (2005) Beyond the hype of frictionless markets: Evidence of heterogeneity in price rigidity on the internet. J. Management Inform. Systems 22(2):57–89.

Bird J (2018) What a waste: Online retail’s big packaging problem. Accessed June 23, 2023, https://www.forbes.com/sites/ jonbird1/2018/07/29/what-a-waste-online-retails-big-packagingproblem/#714fa278371d.

Broida R (2016) Amazon Prime: Still a good deal at \$99? Accessed June 23, 2023, https://www.cnet.com/news/amazon-primestill-a-good-deal-at-99/.

Burke K (2015) Is free shipping killing Amazon’s profit? Accessed June 23, 2023, http://www.marketwatch.com/story/is-freeshipping-killing-amazons-profit-2015-07-14.

Byrnesarchive N (2016) How Amazon loses on Prime and still wins Accessed June 23, 2023, https://www.technologyreview.com/ s/601889/how-amazon-loses-on-prime-and-still-wins/.

Cachon GP, Swinney R (2009) Purchasing, pricing, and quick response in the presence of strategic consumers. Management Sci. 55(3): 497–511.

Callahan P (2019) Amazon pushes fast shipping but avoids responsibility for the human cost. New York Times (September 5), https:// www.nytimes.com/2019/09/05/us/amazon-delivery-driversaccidents.html.

Clemons EK, Weber BW (1994) Segmentation, differentiation, and flexi ble pricing: Experiences with information technology and segment tailored strategies. J. Management Inform. Systems 11(2):9–36.

Consumer Reports (2016) Amazon Prime membership is worth the cost. Accessed June 23, 2023, http://www.consumerreports. org/holiday-shopping/amazon-prime-membership-is-worth-thecost/.

Dayen D (2019) Is Amazon violating U.S. antitrust laws? This law student thinks he has evidence. Accessed June 23, 2023, https:// inthesetimes.com/article/21850/is-amazon-using-predatorypricing-in-violation-of-antitrust-laws-monopoly.

Dean B (2022) Amazon Prime user and revenue statistics. Accessed June 23, 2023, https://backlinko.com/amazon-prime-users.

de Koster RBM (2002) The logistics behind the enter click. Klose A, Speranza MG, Van Wassenhove LN, eds. Quantitative Approaches to Distribution Logistics and Supply Chain Management, Lecture Notes in Economics and Mathematical Systems, vol. 519 (Springer, Ber lin), 131–148.

Dowling GR, Uncles M (1997) Do customer loyalty programs really work? MIT Sloan Management Rev. 38(4):71.

Fang Z, Ho Y-C, Tan X, Tan Y (2021) Show me the money: The economic impact of membership-based free shipping programs on e-tailers. Inform. Systems Res. 32(4):1115–1127.

Farrell J (1990) Competition with lock-in. de Fontenay, Shugard, Sibley, eds. Telecommunications Demand Modeling: An Integrated View (North-Holland, Netherlands), 353–362.

GeekWire (2014) Lawsuit alleges Amazon Prime third-party prices are inflated to cover shipping. Accessed June 23, 2023, http://www. geekwire.com/2014/lawsuit-alleges-amazon-prime-third-partyprices-inflated-cover-shipping/.

Greene J (2020) Amazon’s big holiday shopping advantage: An in-house shipping network swollen by pandemic-fueled growth. Washington Post (November 27), https://www.washingtonpost.com/techno logy/2020/11/27/amazon-shipping-competitive-threat/.

Jerath K, Netessine S, Veeraraghavan SK (2010) Revenue management with strategic customers: Last-minute selling and opaque selling. Management Sci. 56(3):430–448.

Jiang B, Jerath K, Srinivasan K (2011) Firm strategies in the “mid tail” of platform-based retailing. Marketing Sci. 30(5):757–775.

Klemperer P (1987) Markets with consumer switching costs. Quart. J. Econom. 102(2):375–394.

Lai G, Debo LG, Sycara K (2010) Buy now and match later: Impact of posterior price matching on profit with strategic consumers. Manufacturing Service Oper. Management 12(1):33–55.

Levy A (2016) How Prime makes Amazon profitable. Accessed June 23, 2023, https://www.fool.com/investing/general/2016/03/25 how-prime-makes-amazon-profitable.aspx.

Lewis M (2004) The influence of loyalty programs and short-term promotions on customer retention. J. Marketing Res. 41(3):281–292.

Liang C, C¸akanyıldırım M, Sethi SP (2014) Analysis of product rollover strategies in the presence of strategic customers. Management Sci. 60(4):1033–1056.

Liu Q, Van Ryzin GJ (2008) Strategic capacity rationing to induce early purchases. Management Sci. 54(6):1115–1131.

Lummus RR, Vokurka RJ (2002) Making the right e-fulfillment deci sion. Prod. Inventory Management J. 43(1/2):50–55.

Moran CD (2022) Walmart to bring in-home delivery to 30M US house holds this year. Accessed June 23, 2023, https://www.grocerydive.

com/news/walmart-to-bring-in-home-delivery-to-30m-ushouseholds-this-year/616687/.

Nguyen N (2018) The hidden environmental cost of Amazon Prime’s free, fast shipping. Accessed June 23, 2023, https://www.buzzfeed news.com/article/nicolenguyen/environmental-impact-of-amaz on-prime.

Nolan C (2016) Amazon Prime membership: Is it worth the \$99 annual fee? Accessed June 23, 2023, https://www.thestreet. com/story/13215530/1/amazon-prime-membership-is-it-worth the-99-annual-fee.html.

Repko M (2021) Walmart+ is gaining momentum, hits 32 million members, Deutsche Bank estimates. Accessed June 23, 2023, https:// www.cnbc.com/2021/09/14/walmart-hits-32-million-membersdeutsche-bank-estimates.html.

Riggins FJ (2004) A multi-channel model of separating equilibrium in the face of the digital divide. J. Management Inform. Systems 21(2):161–179.

Rossi B (2015) Shipping is the ‘Achilles heel’ of online retailers Accessed June 23, 2023, http://www.information-age.com shipping-achilles-heel-online-retailers-123458893/.

Rubin BF (2015) Amazon surprise! Prime members help deliver a profit. Accessed June 23, 2023, https://www.cnet.com/news/ amazon-pulls-off-surprise-profit-thanks-to-prime/.

Rubin BF (2016) Your impulse buys are costing Amazon a fortune. Accessed June 23, 2023, https://www.cnet.com/news/yourimpulse-buys-are-costing-amazon-a-fortune/.

Sharp B, Sharp A (1997) Loyalty programs and their impact on repeat-purchase loyalty patterns. Internat. J. Res. Marketing 14(5): 473–486.

Sheffield H (2015) Amazon Prime: Why unlimited shipping is too good to be true. Accessed June 23, 2023, http://www.independent. co.uk/news/business/news/amazon-prime-why-unlimited shipping-is-too-good-to-be-true-a6715036.html.

Shieber J (2019) Amazon’s ‘climate pledge’ commits to net zero carbon emissions by 2040 and 100% renewables by 2030. Accessed June 23, 2023, https://techcrunch.com/2019/09/19/amazons climate-pledge-commits-to-net-zero-carbon-emissions-by-2040- and-100-renewables-by-2030/.

Streitfeld D (2015) Amazon reports a profit, citing Prime as the key New York Times (January 30), https://www.nytimes.com/2015/ 01/30/technology/amazon-earnings-profit-prime.html?\_r=0.

Su X (2007) Intertemporal pricing with strategic customer behavior. Management Sci. 53(5):726–741.

Su X, Zhang F (2008) Strategic customer behavior, commitment, and supply chain performance. Management Sci. 54(10):1759–1773.

Tuttle B (2011) Amazon Prime loses \$11 annually per member … and it’s a huge success. Accessed June 23, 2023, https://business. time.com/2011/11/14/amazon-prime-loses-11-annually-permember-and-its-a-huge-success/.

Uncles MD, Dowling GR, Hammond K (2003) Customer loyalty and customer loyalty programs. J. Consumer Marketing 20(4): 294–316.

Wen Z, Lin L (2017) Membership free shipping programs: Effect on competition and optimality of member fees. Proc. 50th Hawaii Internat. Conf. System Sci. https://scholarspace.manoa.hawaii edu/items/9a3f8960-0680-4925-8a45-076bef89d527.

Yi Y, Jeon H (2003) Effects of loyalty programs on value perception, program loyalty, and brand loyalty. J. Acad. Marketing Sci. 31(3):229–240.

Young J (2022) Walmart marketplace’s push to grow third-party seller base. Accessed June 23, 2023, https://www.digitalcommerce360. com/2022/09/13/in-focus-walmart-marketplaces-push-to-grow third-party-seller-base/.

C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pera</sub>ti<sub>ons</sub> R<sub>esearc</sub>h & th<sub>e</sub> M<sub>anagemen</sub>t S<sub>c</sub>i<sub>ences an</sub>d it<sub>s con</sub>t<sub>en</sub>t <sub>may no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or</sub> <sub>ema</sub>il<sub>e</sub>d t<sub>o</sub> <sub>mu</sub>lti<sub>p</sub>l<sub>e</sub> <sub>s</sub>it<sub>es</sub> <sub>or</sub> <sub>pos</sub>t<sub>e</sub>d t<sub>o</sub> <sub>a</sub> li<sub>s</sub>t<sub>serv</sub> <sub>w</sub>ith<sub>ou</sub>t th<sub>e</sub> <sub>copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup> <sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use.</sub>

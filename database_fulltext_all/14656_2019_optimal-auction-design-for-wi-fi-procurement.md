---
otero_id: 14656
otero_key: "FVH3GTG7"
title: "Optimal Auction Design for Wi-Fi Procurement"
authors: "Liangfei Qiu; Huaxia Rui; Andrew Whinston"
year: "2019"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0742"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.209.6.61] On: 13 February 2019, At: 22:45 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/FVH3GTG7/fulltext/images/f6ec1067185e0ff4cea4e204a282017dd5218216d69f18e0991a93067bd1f532.jpg)  
Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Optimal Auction Design for Wi-Fi Procurement

Liangfei Qiu, Huaxia Rui, Andrew Whinston

To cite this article: Liangfei Qiu, Huaxia Rui, Andrew Whinston (2019) Optimal Auction Design for Wi-Fi Procurement. Information Systems Research

Published online in Articles in Advance 01 Feb 2019

https://doi.org/10.1287/isre.2017.0742

Full terms and conditions of use: https://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2019, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Optimal Auction Design for Wi-Fi Procurement

Liangfei Qiu,<sup>a</sup> Huaxia Rui,<sup>b</sup> Andrew Whinston<sup>c</sup>

<sup>a</sup> Warrington College of Business, University of Florida, Gainesville, Florida 32611; <sup>b</sup> Simon Business School, University of Rochester, Rochester, New York 14627; <sup>c</sup> McCombs School of Business, University of Texas at Austin, Austin, Texas 78712 Contact: liangfeiqiu@ufl.edu, http://orcid.org/0000-0002-8771-9389 (LQ); huaxia.rui@simon.rochester.edu (HR); abw@uts.cc.utexas.edu (AW)

Received: June 3, 2015 Revised: November 6, 2016; March 2, 2017 Accepted: June 21, 2017 Published Online in Articles in Advance: February 1, 2019

https://doi.org/10.1287/isre.2017.0742

Copyright: © 2019 INFORMS

Abstract. The unprecedented growth of cellular trafic driven by the use of smartphones for web surfing, video streaming, and cloud-based services poses bandwidth challenges for cellular service providers. To manage the increasing data trafic, cellular service providers are experimenting with the use of third-party Wi-Fi hot spots to augment their cellular capacity. We develop an analytical framework to study the optimal procurement auction for Wi-Fi capacity. Such an auction design is complicated by the fact that Wi-Fi networks have much more limited spatial coverage compared with the cellular network. Neither a global auction that includes all Wi-Fi hot spots nor multiple local auctions that include only hot spots in each local Wi-Fi region is optimal. We find that the optimal mechanism is an integration of one global auction that includes hot spots from an endogeneously determined set of Wi-Fi regions and many separate local auctions that are only held in the rest of the Wi-Fi regions. To implement the optimal mechanism, we also provide an eficient algorithm whose computation complexity is of the order of the number of Wi-Fi regions. Our work contributes to the literature by designing the optimal mechanism for a unique type of IT procurement auction problem that is a tight integration of economics and computational technology.

History: Il-Horn Hann, Senior Editor; Subodha Kumar, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2017.0742.

Keywords: Wi-Fi of-loading • procurement auction • mechanism design

## 1. Introduction

The increasing popularity of smartphones has triggered an explosive growth of mobile data trafic driven by web surfing, video streaming, online gaming, and many other digital goods industries (Tan et al. 2016, Tan and Carrillo 2017). According to Cisco Visual Networking Index Global Mobile Data Forecast Update (2016– 2021), global mobile data trafic grew 63% in 2016 and reached 7.2 exabytes per month at the end of 2016, up from 4.4 exabytes per month at the end of 2015 (Cisco 2017). Moreover, mobile data trafic is expected to grow at a compound annual growth rate of 47% from 2016 to 2021, reaching 49.0 exabytes per month by 2021. The huge amount of mobile data trafic poses a challenge to the network infrastructure: Cellular networks are overloaded and congested during peak hours because of insuficient capacity, which leads to poor user experience and churn.

Researchers have proposed several solutions from both technical and economic aspects: (1) increasing the number of cellular towers or deploying the cellsplitting technology; (2) upgrading the network to fourth-generation (4G) networks such as Long Term Evaluation, High Speed Packet Access, and WiMax; (3) expanding capacity by acquiring the spectrum of other networks, such as the attempted purchase of

T-Mobile USA by AT&T; (4) adopting smart data pricing mechanisms (e.g., usage- and app-based pricing plans) to constrain the heaviest mobile data users, instead of using flat-rate pricing plans with unlimited data (Sen et al. 2012); and (5) of-loading data trafic to Wi-Fi networks (Bulut and Szymanski 2012).

Although all these solutions help alleviate the problem, each has its disadvantages. The first two solutions require large investments, and getting government approval for building new cell towers can take years. From an economic perspective, it is extremely expensive to increase the number of cellular base stations.<sup>1</sup> As a result, all cellular networks augment the first two solutions with other approaches to expand capacity. The third solution sufers from regulatory constraints. Cramton et al. (2007) show that an important market failure arises in spectrum auctions with dominant incumbents. They suggest that the Federal Communications Commission (FCC) should place limits on how much spectrum AT&T and Verizon are allowed to purchase.<sup>2</sup> Although the average net benefits realized under congestion-based pricing tend to be higher than the average net benefits realized under flatrate pricing (Gupta et al. 2011), usage-based plans may also backfire by alienating smartphone users, who are likely the customer segment with the highest revenue growth potential.

Because of these technical, economic, and regulatory constraints, the fifth solution—using Wi-Fi hot spots for mobile data trafic of-loading—seems to be one of the most promising approaches in augmenting solutions (1) and (2). A straightforward approach is for the cellular service providers to build and manage their own hot spots. In fact, we have seen some pilot projects for self-managed hot spots (Aĳaz et al. 2013). Even though the option of service providers directly managing hot spots is often available, it is still expensive (Iosifidis et al. 2015) and may not be cost-efective. For example, Paul et al. (2011) found that 28% of subscribers generate trafic only in a single hour during peak hours in a day. Clearly, building and managing hot spots just for that peak hour is not eficient. Of-loading trafic to third party hot spots overcomes the obstacle of managing a hot spot and ensures the high availability of Wi-Fi resources. This strategy could potentially be a win–win solution: The cellular service provider saves the cost of building more cellular base stations or hot spots just for the peak trafic demands. The Wi-Fi hot spots profit from sharing their otherwise wasted spare capacity. Indeed, such practice of sharing unused capacity is gaining traction in the industry (e.g., Airbnb, Uber) thanks to the advancement in technology, and the study of such sharing economy is also on the rise (Weber 2014).

We follow this paradigm of the sharing economy and focus on of-loading mobile trafic to third-party Wi-Fi hot spots owned by entities such as local restaurants, bookstores, and hotels. Cellular service providers have shown great interest in such an approach. In 2012, for example, KDDI Corporation, a principal telecommunication provider in Japan, had already cooperated with about 100,000 commercial Wi-Fi hot spots (Aĳaz et al. 2013). However, of-loading data trafic to third-party Wi-Fi hot spots is not purely a technology strategy to augment the existing cellular network. Considering the economic incentives of third-party Wi-Fi hot spots, Wi-Fi of-loading is also a practical mechanism design problem. Therefore, efectively leveraging third-party Wi-Fi capacity requires the combination of both information technology and economic theory, which is in the spirit of designing smart markets (Bichler et al. 2010). Because Wi-Fi capacity is a type of product with quite standardized characteristics, competitive bidding should be a better way to select the lowest cost bidder than negotiations.<sup>3</sup>

In this study, we aim to model and solve the optimal procurement auction of third-party Wi-Fi capacity. Because Wi-Fi networks usually have more limited range than cellular resources, the range of a cellular tower should be partitioned into several Wi-Fi regions. The cellular capacity can serve data trafic in any Wi-Fi region, whereas Wi-Fi networks can serve only local trafic. However, the procurement auction design is not equivalent to running one local auction in each Wi-Fi region because of the presence of the cellular resource. Buying more resources from one local Wi-Fi hot spot frees up more cellular capacity to serve demand in other Wi-Fi regions, thereby creating interregion competition. On the other hand, the procurement auction design is not equivalent to one global auction either, where hot spots in all Wi-Fi regions participate in one auction. This is because implementing a global auction may not always be feasible: Wi-Fi capacity in one region cannot be transferred to other regions. The inflexibility of Wi-Fi capacity causes difficulty for implementing a completely global auction when regions with heavy mobile trafic have insuficient Wi-Fi capacity and those with light mobile trafic have excessive Wi-Fi capacity.

We find that the optimal mechanism is equivalent to an integration of one global auction that includes hot spots from an endogeneously determined set of Wi-Fi regions and one local auction on each of the rest of the Wi-Fi regions. This integration of global and local auctions is both theoretically interesting and practically important. It is the consequence of two unique features of procuring Wi-Fi capacity for mobile trafic of-loading: (1) the coupling of local auctions because of the existence of the more flexible cellular capacity and (2) heterogeneity in terms of both the demand for mobile bandwidth and the supply of Wi-Fi capacity in diferent Wi-Fi regions. To implement the optimal mechanism, we also provide an eficient algorithm whose computational complexity is of the order of the number of Wi-Fi regions.

The insights from this paper apply more generally to a class of procurement auction problems. The key issue in the procurement of Wi-Fi capacity is to design the optimal auction mechanism in the presence of product flexibility and information asymmetry between suppliers (i.e., Wi-Fi hot spots) and the downstream firm (i.e., the cellular service provider). This procurement problem in the wireless industry is an example of a general setting where (1) the downstream firm owns product-flexible in-house capacity that can be used for multiple products; (2) the product-flexible capacity is limited, and the firm needs to procure products from multiple upstream suppliers; and (3) each supplier is specialized and can produce only one product. Given the limitation of product-flexible capacity (in-house capacity) and the information asymmetry between the downstream firm and the suppliers, the downstream firm needs to solve the complex problem of designing an optimal procurement auction. This procurement scenario is common when companies are investing in product-flexible capacity that entails the ability to produce multiple products with the same capacity and the ability to reallocate capacity between products (Goyal and Netessine 2011). Many manufacturing and service companies use flexible capacity to hedge against uncertainty in future demand (Fine and Freund 1990, Van Mieghem 1998).<sup>4</sup>

Note that we have abstracted away the capacity problem of broadband. Our key argument is that broadband technology is fundamentally diferent from cellular technology in terms of capacity constraints. First, broadband technology has advanced faster than cellular technology in past decades, and, currently, increasing broadband capacity is much cheaper than increasing cellular capacity. Unlike fiber optics in the case of broadband capacity, cellular capacity is inherently and technically constrained by radio spectrum capacity. Second, even if significant advances in cellular technologies take place in the near future, the cellular service providers will still need to worry about the traffic because of various regulatory constraints. We elaborate on these diferences between broadband technology and cellular technology in Online Appendix C.

## 2. Literature Review

The technology aspect and implementation of this study are clearly related to the vast literature in computer science on mobile data of-loading (Balasubramanian et al. 2010, Iosifidis et al. 2015, Dong et al. 2014). We refer interested readers to Aĳaz et al. (2013) for an overview of the technical and business perspectives of mobile data of-loading and to Kang et al. (2014) for a discussion on mobile data of-loading through third-party Wi-Fi hot spots. The theoretical aspect of the present study is mostly related to two streams of literature, optimal auction design and supply chain management, which we will review in more detail.

In many procurement situations, the buyer cares about other attributes in addition to price when evaluating the submitted bids. Dasgupta and Spulber (1990) extended the standard fixed quantity auction and studied a quantity auction that allows the quantity of goods purchased to be endogenously determined by the submitted bids. In a multiattribute scoring auction, suppliers submit multidimensional bids, and the contract is awarded to the supplier who submitted the bid with the highest score according to a scoring rule. Che (1993) developed a scoring procurement auction in which suppliers bid on two dimensions of the good. This scoring auction allows only sole sourcing. However, of-loading data trafic to multiple Wi-Fi hot spots is naturally done in our procurement setting. Duenyas et al. (2013) showed that a simple version of the open-descending auction can implement the optimal procurement mechanism for a newsvendor problem. The model in this study difers from such auctions because of the unique challenge in our application setting.

Much of the literature on supply chain management has focused on scenarios where adding productflexible capacity is beneficial (Goyal and Netessine 2011). Janakiraman et al. (2018) considered a firm that produces multiple products each period, using a shared resource with limited capacity, in a periodically reviewed stochastic inventory model. A natural question is, with limitations on product-flexible capacity, how should a downstream firm design its procurement auction mechanism? In the present study, we introduce an auction design problem with asymmetric information in the presence of product-flexible capacity. The downstream firm procures capacity from the suppliers to optimally combine with its in-house capacity to produce diferent products. In this process, the downstream firm makes the following decisions: how to allocate its product-flexible capacity to produce diferent products, how much quantity should be procured from each supplier, and what the corresponding payment scheme for each supplier should be. Our theoretical analysis provides insights to these questions in the context of the telecommunication industry and complements the existing literature on product line designs when the product-flexible capacity is limited. Netessine et al. (2002) analytically characterized the critical efects of increasing demand correlation between products on the flexible capacity decisions. We also find that the demand correlation as well as the level of in-house product-flexible capacity plays a crucial role in the optimal design of the procurement mechanism. When the demand is highly positively correlated or when the inhouse product-flexible capacity is suficiently large, the optimal procurement mechanism simplifies to a global auction including all upstream suppliers, but in general, it is equivalent to an integration of one global auction and multiple local auctions.

## 3. Model

## 3.1. Model Setup

A cellular network provides service to its customers, who demand bandwidth. We think of the packets requested by the consumers as being serviced in a queuing system. The expected waiting time a typical customer experiences can be written as $W ( \mu )$ , where $\mu$ is the service capacity. Clearly, $W ( \mu )$ should be decreasing in $\mu$ and be bounded below. We further make the technical assumption that $W ( \mu )$ is twice diferentiable and is strictly convex in $\mu$

$$
\frac {d W}{d \mu} <   0, \quad \frac {d ^ {2} W}{d \mu^ {2}} > 0.
$$

This is a mild technical assumption that is satisfied, for example, by an $M / M / c$ queue.<sup>5</sup> In the special case of an $M { \dot { / } } M / 1 { \dot { \bf \Omega } }$ queue, as is assumed in Cheng et al. (2011), $W ( \mu )$ is simply $W ( \mu ) = 1 / ( \mu - \lambda )$ , where λ is the customer demand rate.

Given the expected waiting time, the cellular service provider incurs a cost of $\chi ( W ) .$ , which is a strictly increasing function of W. To capture the rapidly rising cost of service degradation due to customers’ increased expected waiting times (e.g., dissatisfied customers, or churn), we assume that the function $\chi ( \cdot )$ is convex. As a special case, Cachon and Feldman (2011) assumed the waiting cost is a linear function of W. For convenience, we refer to the composition of $\chi ( \cdot )$ and $W ( \cdot )$ as $\omega ( \mu ) \equiv \chi ( W ( \mu ) )$ <sup>)</sup>. It is straightforward to show that $\omega ( \mu )$ is strictly decreasing and strictly convex in $\mu . ^ { 6 }$

Given the unprecedented growth rate of mobile data demand and the high cost associated with congestion, the cellular network is interested in procuring spare resources from third-party Wi-Fi hot spots. Although both can be used to meet the user demand, cellular resources and Wi-Fi resources have diferent spatial coverages. In suburban areas, a typical cellular base station covers one to two miles (2–3 km), and in dense urban areas, it may cover one-fourth to one-half of a mile (400–800 m). A typical Wi-Fi network has a range of 120 feet (32 m) indoors and 300 feet (95 m) outdoors.<sup>7</sup> To model this unique feature of bandwidth supply, we partition a cell sector into several Wi-Fi regions so that Wi-Fi hot spots within the same region are relatively close together. In particular, we assume the cell sector can be divided into M Wi-Fi regions.<sup>8</sup> Cellular resources can serve trafic in any region m, whereas Wi-Fi hot spots in region m can serve only local traffic. A unique challenge in the procurement auction is that the longer-range cellular resource introduces coupling between the shorter-range Wi-Fi hot spots. The procurement problem in one Wi-Fi region is not independent of the procurement problem in another region, because purchasing more Wi-Fi capacity from a local Wi-Fi hot spot in one region frees up more cellular capacity that can be used to serve the demand in another region.

Serving mobile demand for the cellular network provider incurs cost to a hot spot, which difers among hot spots. We assume the cost function for hot spot i to provide capacity Q to the cellular network is

$$
C (Q, \theta_ {i}) \equiv \int_ {0} ^ {Q} c (q, \theta_ {i}) d q, i = 1, 2, \ldots , N,
$$

where $c ( q , \theta _ { i } ) \geq 0$ is the marginal cost function for hot spot $i ,$ and $\theta _ { i }$ reflects each hot spot’s private information about the cost of bandwidth provision, which differs among diferent hot spots. In reality, the private information $\theta _ { i }$ can be interpreted as each hot spot’s sensitivity to its Wi-Fi congestion rate. For example, some hot spots, like cofee shops, might be more sensitive to their Wi-Fi congestion because some customers go there primarily for their Wi-Fi services, while other hot spots, like restaurants, might be less sensitive.

We assume $c _ { q } ( q , \theta _ { i } ) \geq 0$ to capture the fact that the marginal cost of providing capacity for each hot spot increases as more capacity is provided to the cellular network. Following previous literature (Dasgupta and Spulber 1990), we also assume that the marginal cost is increasing and convex in the cost parameter, $c _ { \theta } \geq 0 , c _ { \theta \theta } \geq 0 .$ , and that $c _ { q \theta } \geq 0$ . Hot spots’ cost parameters are independently and identically distributed with a continuously diferentiable cumulative distribution function $F ( \cdot )$ defined on $[ \underline { { \theta } } , \bar { \theta } ] ,$ , which is common <sup>¯</sup>knowledge. We further assume $H ( \theta ) \equiv F ( \theta ) / F ^ { \prime } ( \theta )$ is an increasing function of θ, which is satisfied by common distribution functions such as the uniform distribution.

To model potential revenue sharing between a hot spot and its Internet service provider (ISP), we assume that a hot spot gets a proportion $( \tilde { \alpha } \in ( 0 , 1 ) )$ of the payment from the cellular service provider for providing Wi-Fi capacity. The other proportion 1 <sup>−</sup> α˜ goes to the ISP. We define $\alpha = \tilde { \alpha } ^ { - 1 }$ for notational convenience. Finally, let $\theta ^ { * }$ be the threshold cost parameter chosen by the cellular service provider so that any hot spot with $\theta > \theta ^ { * }$ will not participate in the procurement auction.

To determine the optimal auction mechanism, we first need to derive the value of procuring Wi-Fi capacity. Let $y _ { m }$ be the amount of Wi-Fi capacity the cellular service provider purchased from hot spots in region $m ,$ and let $\begin{array} { r } { \boldsymbol { y } = \sum _ { m = 1 } ^ { \hat { M } } \boldsymbol { y } _ { m } } \end{array}$ be the total Wi-Fi capacity purchased in all regions. Because congestion costs in different regions naturally involve diferent customers at any given time, a cost function that is separable across regions captures such cost structure. This is also consistent with the tradition in economics of using additive utilitarian social welfare function, which is also widely used in the information systems literature. In particular, we model the congestion cost of each region, $\omega _ { m } ,$ as a region-specific function of $y _ { m } + \mu _ { m } ,$ for $m =$ $1 , \ldots , M$ . For example, diferent regions might have different customer demand rates, and the cellular service provider might also place diferent weights in diferent regions. The total congestion cost is then $\begin{array} { r } { \sum _ { m = 1 } ^ { M } \omega _ { m } ( \mu _ { m } + } \end{array}$ $y _ { m } )$ , where $\mu _ { m }$ is the amount of cellular capacity allocated to region $m ,$ , and the congestion cost minimization problem can be written as

$$
\begin{array}{l} J (y _ {1}, \ldots , y _ {M}) = \min _ {\mu_ {1}, \ldots , \mu_ {M}} \sum_ {m = 1} ^ {M} \omega_ {m} (\mu_ {m} + y _ {m}) \\ \text {s.t.} \quad \sum_ {m = 1} ^ {M} \mu_ {m} \leq \mu , \\ \mu_ {m} \geq 0, \text {for} m = 1, 2, \ldots , M. \end{array}\tag{1}
$$

The cellular service provider purchases Wi-Fi capacity $y _ { 1 } , \dots , y _ { M }$ for the M regions from hot spots in these regions to supplement its cellular capacity.<sup>9</sup> The objective is to minimize the total cost, including those for congestion $J ( y _ { 1 } , \dots , y _ { M } )$ and for procurement, which include both the actual costs of hot spots providing

Wi-Fi resources and the information rent due to information asymmetry. The cellular service provider follows a two-step decision procedure: In the first step, it purchases Wi-Fi capacity from hot spots in diferent regions. In the second step, the cellular service provider allocates cellular resources across regions.

## 3.2. Global Auction

In this section, we assume the nonnegativity constraints on $\mu _ { m }$ are not binding and call the resulting auction mechanism a global auction. We will see later that this is an important building block of the actual optimal mechanism.

Proposition 1. Under a global auction, the optimal cellular resource allocation is given by

$$
\mu_ {m} ^ {*} = \phi_ {m} (\Psi (y + \mu)) - y _ {m},
$$

where $\phi _ { m } ( \cdot )$ is the inverse of $\omega _ { m } ^ { \prime } ( \cdot )$ , and $\Psi ( \cdot )$ is the inverse of $\begin{array} { r } { \Phi ( \cdot ) \equiv \sum _ { m = 1 } ^ { M } \phi _ { m } ( \cdot ) } \end{array}$ . The optimal congestion cost is

$$
J (y) \equiv \sum_ {m = 1} ^ {M} \omega_ {m} (\phi_ {m} (\Psi (y + \mu))).
$$

Moreover, J<sup>(</sup>y<sup>)</sup> is decreasing and convex.

Proof. The first-order condition implies that there exists a Lagrange multiplier for the cellular capacity constraint $\nu > 0$ such that

$$
\omega_ {m} ^ {\prime} (y _ {m} + \mu_ {m}) + \nu = 0, \quad \forall m = 1, 2, \ldots , M.
$$

Hence,

$$
\mu_ {m} ^ {*} = \phi_ {m} (- \nu) - y _ {m},
$$

where $\phi _ { m }$ is guaranteed to exist because of the strict convexity of $\omega _ { m } ( \cdot )$ . The cellular capacity constraint is binding at the optimal solution, which implies

$$
\begin{array}{c} \mu = \sum_ {m = 1} ^ {M} \mu_ {m} ^ {*} = \sum_ {m = 1} ^ {M} (\phi_ {m} (- \nu) - y _ {m}) \\ = \sum_ {m = 1} ^ {M} \phi_ {m} (- \nu) - y = \Phi (- \nu) - y. \end{array}
$$

Because $\omega _ { m } ( \cdot )$ is strictly convex and $\phi _ { m } ( \omega _ { m } ^ { \prime } ( x ) ) = x ,$ we see that $\phi _ { m }$ is monotone increasing

$$
\phi_ {m} ^ {\prime} (\omega_ {m} ^ {\prime} (x)) = \frac {1}{\omega_ {m} ^ {\prime \prime} (x)} > 0.
$$

Hence, $\Phi ( x )$ is also monotone increasing

$$
\Phi^ {\prime} (x) = \sum_ {m = 1} ^ {M} \phi_ {m} ^ {\prime} (x) > 0,
$$

which guarantees the existence of the inverse of $\Phi ( \cdot ) _ { - }$ which is denoted by $\Psi ( \cdot )$

Therefore, $\nu = - \Psi ( y + \mu ) .$ , and the claim follows. Because $J ( y _ { 1 } , \dots , y _ { M } )$ is a function of $y _ { 1 } , \dots , y _ { M }$ only through their sum, $y ,$ with a slight abuse of notation, we write it simply as $J ( y )$ when none of the nonnegativity constraints is binding.

Now, we show that $J ( y )$ is decreasing and convex in y. Denote $z = y + \mu$ so that $\Phi ( - \nu ) = z$ and $\Psi ( z ) = - \nu$ Because $\dot { \Psi } ( \Phi ( x ) ) = x .$ , we have

$$
\Psi^ {\prime} (z) = \frac {1}{\Phi^ {\prime} (- \nu)} = \left(\sum_ {m = 1} ^ {M} \phi_ {m} ^ {\prime} (- \nu)\right) ^ {- 1}.
$$

The first and second derivatives of $J ( y )$ are

$$
\begin{array}{r l} & J ^ {\prime} (y) = \sum_ {m = 1} ^ {M} \omega_ {m} ^ {\prime} (\phi_ {m} (\Psi (z))) \phi_ {m} ^ {\prime} (\Psi (z)) \Psi^ {\prime} (z) \\ & \qquad = \Psi (z) \frac {1}{\sum_ {m = 1} ^ {M} \phi_ {m} ^ {\prime} (- \nu)} \sum_ {m = 1} ^ {M} \phi_ {m} ^ {\prime} (- \nu) \\ & \qquad = \Psi (z) = - \nu <   0, \\ & J ^ {\prime \prime} (y) = \Psi^ {\prime} (z) = \left(\sum_ {m = 1} ^ {M} \phi_ {m} ^ {\prime} (- \nu)\right) ^ {- 1} > 0. \end{array}
$$

Therefore, J<sup>(</sup>y<sup>)</sup> is decreasing and convex in y. <sup></sup>

For this optimal allocation to be feasible, we need $\mu _ { m } ^ { * } \geq 0 , \mathrm { o r } $ , equivalently,

$$
\mu \geq \Phi (\omega_ {m} ^ {\prime} (y _ {m})) - y, \quad \forall m = 1, \ldots , M.\tag{2}
$$

As we stated at the beginning of this section, we assume the nonnegativity constraints of $\mu _ { m }$ are nonbinding, and hence the inequality (2) is always satisfied.

Intuitively, when condition (2) is satisfied, the Wi-Fi resource in one region is a perfect substitute of the Wi-Fi resource in another region, from the perspective of the cellular service provider. Given our solution for the second-stage problem, the first-stage problem is a direct revelation game in which hot spots truthfully report their types in the Bayesian Nash equilibrium. We adopt the notational convention of writing $\theta _ { - i } = ( \theta _ { 1 } , \ldots , \bar { \theta } _ { i - 1 } , \theta _ { i + 1 } , \ldots , \theta _ { N } )$ . The procurement auction can be implemented via a direct revelation mechanism where

• the cellular service provider announces a payment-bandwidth schedule $P _ { i } = P ( \theta _ { i } , \theta _ { - i } )$ and a bandwidth allocation schedule $q _ { i } = Q ( \theta _ { i } , \theta _ { - i } ) ;$

• hot spot i truthfully reports the private cost parameter ${ \bar { \theta _ { i } } } ,$ given $P ( \theta _ { i } , \dot { \theta _ { - i } } )$ and $Q ( \theta _ { i } , \theta _ { - i } ) ;$ ; and

• hot spot i provides bandwidth $q _ { i } = Q ( \theta _ { i } , \theta _ { - i } )$ to the cellular service provider and its revenue is $\tilde { \alpha } P ( \theta _ { i } , \theta _ { - i } )$

By selling its spare bandwidth, a hot spot is essentially delivering a certain quantity of requested data for the cellular service provider. Hence, we simply refer to $Q ( \theta _ { i } , \theta _ { - i } )$ as the quantity schedule from now on. To implement the scheme, the cellular service provider can periodically run the procurement auction to obtain

Wi-Fi capacity from each region and determine the optimal allocation of cellular capacity across regions. Alternatively, the service provider can rerun the auction whenever the demand rates or the rate distribution across Wi-Fi regions changes significantly. As long as the realized demand rates are consistent with the demand rates used to compute the optimal auction rule, the operation is optimal. From the individual customer’s perspective, she may not even know how her requested data is delivered (cellular tower or Wi-Fi hot spot). It is not technologically dificult to automatically select the $\mathrm { \Delta } ^ { \prime \prime } \mathrm { b e s t { \prime \prime } }$ (from the cellular service provider’s financial perspective) source of capacity for the customer data request, which may not necessarily be the geographically closest hot spot. Current technology already can seamlessly switch between cellular towers and Wi-Fi hot spots, although the criteria of switching are often purely technological.

In the case of a global auction, the expected gain from procuring a total of y Wi-Fi capacity is $J ( 0 ) - { \bar { J } } ( y )$ which is increasing and concave in $y .$

To describe the optimal global auction mechanism, we first define $\underline { { \nu } } _ { i }$ as

$$
\underline {{\nu}} _ {i} \equiv \alpha c (0, \theta_ {i}) + \alpha c _ {\theta} (0, \theta_ {i}) H (\theta_ {i}), \quad \forall i = 1, \ldots , N,
$$

and impose the following technical condition:

$$
- \Psi (\mu) > \min \{\underline {{\nu}} _ {1}, \underline {{\nu}} _ {2}, \dots , \underline {{\nu}} _ {N} \}.
$$

Note that the function $- \Psi ( q )$ can be interpreted as the marginal value of Wi-Fi capacity when the total acquired Wi-Fi capacity is $q .$ Hence, this condition ensures that the marginal benefit of procuring an infinitesimal amount of Wi-Fi capacity is larger than the least (virtual) marginal cost of the hot spot providing Wi-Fi capacity. Without this condition, a Wi-Fi procurement auction is never optimal and should not be considered by the cellular service provider at all.

The following proposition characterizes the optimal global auction mechanism for the cellular service provider and is an application of Dasgupta and Spulber (1990).

Proposition 2 (Dasgupta and Spulber 1990). In the optimal direct revelation mechanism, all hot spots truthfully announce their cost parameters θ. The optimal procurement quantity schedule $q _ { i } ^ { * } = Q ^ { * } ( \theta _ { i } , \theta _ { - i } ) , f o r i = 1 , 2 , \ldots , N ,$ , is determined by

$$
- \Psi \bigg (\mu + \sum_ {j = 1} ^ {N} q _ {j} ^ {*} \bigg) = \alpha c (q _ {i} ^ {*}, \theta_ {i}) + \alpha c _ {\theta} (q _ {i} ^ {*}, \theta_ {i}) H (\theta_ {i}).
$$

The optimal payment schedule $P _ { i } = P ^ { * } ( \theta _ { i } , \theta _ { - i } ) , f o r i = 1$ $2 , \ldots , N$ is given by

$$
P _ {i} = \alpha \left(C (q _ {i} ^ {*}, \theta_ {i}) + \int_ {\theta_ {i}} ^ {\theta^ {*}} C _ {\theta} (Q ^ {*} (\theta , \theta_ {- i}), \theta) d \theta\right).
$$

The cellular service provider’s expected gain from the procurement auction is

$$
J (0) - \mathbb {E} \left[ J \left(\sum_ {i = 1} ^ {N} q _ {i} ^ {*}\right) + \alpha \sum_ {i = 1} ^ {N} C \left(q _ {i} ^ {*}, \theta_ {i}\right) + \alpha \sum_ {i = 1} ^ {N} C _ {\theta} \left(q _ {i} ^ {*}, \theta_ {i}\right) H \left(\theta_ {i}\right) \right].
$$

The intuition of the above proposition is that the $\mathrm { ^ { \prime \prime } v i r t u a l ^ { \prime \prime } }$ marginal costs must be equalized across all hot spots in all regions at the optimum, which determines the optimal quantity functions $Q _ { i } ( \vec { \theta } ) , i = 1 , \ldots , N$ Because $c _ { \theta } \geq 0 , c _ { \theta \theta } > 0 ,$ , and $H ( \theta )$ is increasing in $\theta ,$ it is easy to verify that $( 1 ) q _ { i } ^ { * }$ is decreasing in $\theta _ { i } ,$ that $\left( 2 \right) q _ { j } ^ { * }$ is increasing in $\theta _ { i }$ for $j \neq i ,$ , and that $( 3 ) \textstyle \sum _ { j = 1 } ^ { N } q _ { j } ^ { * }$ is decreasing in $\theta _ { i }$

In the direct revelation game, hot spot i reports its true cost parameter $\theta _ { i }$ . The capacity it needs to provide is $q _ { i } = Q ^ { \bar { * } } ( \theta _ { i } , \theta _ { - i } ) .$ , and its payment is $P _ { i } = P ^ { * } \hat { ( \theta _ { i } , \theta _ { - i } ) }$ This optimal mechanism is a global auction including all hot spots from diferent regions. Note that launching separate local auctions within each region is not optimal because running multiple local auctions essentially reduces competition among hot spots, which could be exploited by flexibly allocating cellular resources among regions. In equilibrium, the virtual marginal costs $c \bar { ( } q _ { i } , \bar { \theta } _ { i } ) + c _ { \theta } ( q _ { i } , \bar { \theta } _ { i } ) H ( \theta _ { i } )$ are equalized across hot spots in diferent regions, and the marginal benefit of procuring Wi-Fi capacity is also equalized across regions. The global auction efectively creates perfect interregion competition among hot spots, which is particularly important when intraregion competition is limited in some regions (e.g., regions with few hot spots).

Based on Propositions 1 and 2, we design the following procedure to calculate the optimal global auction.

• Invite each of the n hot spots to report its cost parameter θ. Denote the submitted cost parameters as $\mathbf { \hat { \{ } }  \theta _ { 1 } , \theta _ { 2 } , \dots , \theta _ { N } \}$

• Define the map q $q \colon \Theta ^ { N } \to \mathbb { R } ^ { N }$ through the following steps:

—Given $\nu \geq 0$ and for each $i = 1 , 2 , \dots , N$ , define $g _ { i } ( \nu )$ as

$$
g _ {i} (\nu) = \left\{ \begin{array}{l l} 0 & \text {if} \nu \leq \underline {{\nu}} _ {i} = \alpha c (0, \theta_ {i}) + \alpha c _ {\theta} (0, \theta_ {i}) H (\theta_ {i}), \\ \infty & \text {if} \nu \geq \bar {\nu} _ {i} \equiv \lim _ {x \to \infty} [ \alpha c (x, \theta_ {i}) + \alpha c _ {\theta} (x, \theta_ {i}) H (\theta_ {i}) ], \\ x ^ {*} & \text {if} \underline {{\nu}} _ {i} <   \nu <   \bar {\nu} _ {i}, \end{array} \right.
$$

where $x ^ { * }$ is the solution to the equation

$$
\alpha c (x, \theta_ {i}) + \alpha c _ {\theta} (x, \theta_ {i}) H (\theta_ {i}) = \nu
$$

in the interval $( 0 , \infty )$ . Because the left-hand side of the equation is increasing in x and $\nu \in ( \underline { { \nu } } _ { i } , \bar { \nu } _ { i } ) , x ^ { * }$ uniquely exists. Given a value of $\nu \in \left( \underline { { \nu } } _ { i } , \bar { \nu } _ { i } \right)$ , we can easily solve for $x ^ { * }$ <sup>¯</sup>using bisection in an appropriately constructed interval $[ 0 , \bar { q } _ { i } ]$ . It is also easy to see that the nonnegative function $g _ { i } ( \nu )$ is (weakly) increasing in ν.

—Let $q ^ { * }$ be the unique solution to the following equation:

$$
\sum_ {i = 1} ^ {N} g _ {i} (- \Psi (\mu + q)) = q.
$$

The uniqueness follows directly from the monotonicity of $\dot { \sum _ { i = 1 } ^ { N } } g _ { i } ( - \Psi ( \mu + q ) ) - q .$ . To see the existence of $q ^ { * }$ , note that by our technical assumption, we have $\begin{array} { r } { \sum _ { i = 1 } ^ { N ^ { \prime } } g _ { i } ( - \Psi ( \mu ) ) > \overline { { 0 } } } \end{array}$ . Let $\begin{array} { r } { \bar { q } \equiv \sum _ { i = 1 } ^ { N } g _ { i } ( - \Psi ( \boldsymbol { \dot { \mu } } ) ) > 0 . } \end{array}$ . Because $\begin{array} { r } { \sum _ { i = 1 } ^ { N } g _ { i } ( - \Psi ( \mu + q ) ) } \end{array}$ is (weakly) decreasing in q, we have

$$
\sum_ {i = 1} ^ {N} g _ {i} (- \Psi (\mu + \bar {q})) \leq \sum_ {i = 1} ^ {N} g _ {i} (- \Psi (\mu)) = \bar {q}.
$$

By continuity, $q ^ { * }$ exists, and we can easily solve for $q ^ { * }$ using bisection in the interval $( 0 , \bar { q } )$

—Denote by $\vec { q } \equiv ( q _ { 1 } , q _ { 2 } , \dots , q _ { N } ) \equiv ( g _ { 1 } ( - \Psi ( \mu + q ^ { * } ) )$ $g _ { 2 } ( - \Psi ( \mu + q ^ { * } ) ) , \ldots , g _ { N } ( - \Psi ( \mu + q ^ { * } ) ) )$ . Clearly, we have $\Sigma _ { i } q _ { i } = q ^ { * }$ . By the definition of $g _ { i } ( \nu )$ , for any i such that $q _ { i } \equiv g _ { i } ( - \Psi ( \dot { \mu } + q ^ { * } ) ) > 0 .$ , we have

$$
\alpha c (q _ {i}, \theta_ {i}) + \alpha c _ {\theta} (q _ {i}, \theta_ {i}) H (\theta_ {i}) = - \Psi (\mu + q ^ {*}).
$$

In other words, the optimality condition of Proposition 2 is satisfied.

• Define payment plan $P _ { i }$ as

$$
\begin{array}{r l} & P _ {i} \equiv P _ {i} (\theta_ {1}, \ldots , \theta_ {N}) \\ & \qquad \equiv \alpha C (q _ {i}, \theta_ {i}) + \alpha \int_ {\theta_ {i}} ^ {\theta^ {*}} C _ {\theta} (q _ {i} (\theta , \theta_ {- i}), \theta) d \theta . \end{array}
$$

• Hot spot i will provide capacity $q _ { i }$ and receive payment $\bar { P _ { i } }$

• The expected gain of the cellular service provider is

$$
J (0) - \mathbb {E} \bigg [ J (q ^ {*}) + \alpha \sum_ {i = 1} ^ {N} C (q _ {i}, \theta_ {i}) + \alpha \sum_ {i = 1} ^ {N} C _ {\theta} (q _ {i}, \theta_ {i}) H (\theta_ {i}) \bigg ].
$$

Figure 1. (Color online) Illustration of the Feasibility Condition  
![](/api/attachments/FVH3GTG7/fulltext/images/3e8bf89cbdc5db8fbd97471d437643a59c94189fcde4222f9eeb4127e6b1b191.jpg)

3.3. Integrating Global and Local Auctions, $M = 2$ Thus far, we have assumed that $\mu _ { m } ^ { * } \geq 0$ for all m. We call this the feasibility condition and it can be written as

$$
\begin{array}{r} \mu \geq \Phi \bigg (\omega_ {m} ^ {\prime} \bigg (\sum_ {i \in E _ {m}} Q ^ {*} (\theta_ {i}, \theta_ {- i}) \bigg) \bigg) - \sum_ {i = 1} ^ {N} Q ^ {*} (\theta_ {i}, \theta_ {- i}), \\ \forall m = 1, \ldots , M, \end{array}
$$

where $E _ { m }$ is the set of participating hot spots in region m. Under the feasibility condition, the cellular capacity $\mu$ is suficiently large for all regions under all realizations of hot spot supply $( { \mathrm { i . e . , } } \theta _ { 1 } , \ldots , \theta _ { N } )$ . Clearly, this is a very restrictive assumption when the cellular capacity is only moderate. In a realistic environment, the feasibility condition will most likely hold for some realizations of cost parameters $( \theta _ { i } , \theta _ { - i } )$ but not for others.

In this section, we relax the assumption that $\mu _ { m } \geq 0$ is nonbinding when $M = 2$ . Once we fully solve the optimal procurement auction design problem with $M = 2 ,$ we will solve the most general case with $M > 2$ in Section 3.4.

To further illustrate the feasibility condition, we depict two examples in Figure 1 based on a simulation.<sup>10</sup> We assume that there are two Wi-Fi regions $( M = 2 )$ and that each region has four hot spots $( N = 8 )$ The congestion cost functions for the cellular service provider and Wi-Fi hot spots are $\omega _ { m } ( \mu _ { m } + y _ { m } ) = 1 / ( \mu _ { m } +$ $y _ { m } - \lambda _ { m } )$ and $\begin{array} { r } { C ( q , \theta _ { i } ) = \hat { ( \frac { 1 } { 2 } + \theta _ { i } ) } q ^ { \overset { . } { 2 } } } \end{array}$ , where the private cost parameters for hot spots, $( \theta _ { 1 } , \ldots , \theta _ { 8 } )$ , are independently drawn from a uniform distribution $U [ 0 , \bar { 1 } ]$ . In Figure 1, the x-axis corresponds to the demand rate in region 1, and the y-axis corresponds to the demand rate in region 2.

• A blue <sup>×</sup> indicates that the feasibility condition is always satisfied;

![](/api/attachments/FVH3GTG7/fulltext/images/c4cc26be3abd05cc41f56cecb5f6f48273df96e4de338b07a9caa4247a1bc3fe.jpg)  
Notes. The cellular capacity, $\mu ,$ is set to be 0.4 in the left panel and 0.2 in the right panel. The feasibility condition is more likely to be violated when the demands are unbalanced or when $\mu$ is small.

• A black star indicates that the feasibility condition is always violated;

• A red dot indicates that the feasibility condition is violated for some realizations of cost parameters $( \theta _ { i } , \theta _ { - i } )$ but not for others.

When the feasibility condition is always satisfied (the blue <sup>×</sup>), even though a hot spot in region 1 cannot directly serve customers in region 2, by serving customers in region 1, it efectively frees up some cellular capacity, which can then be used to serve customers in region 2. Thus, a single global auction to obtain bandwidth from all hot spots should outperform multiple local auctions because of increased competition among hot spots. As a result, the optimal procurement mechanism should be the global auction discussed thus far. When the feasibility condition is always violated (the black stars), all cellular resources should be allocated to the region experiencing a surge in demand due to the insuficient amount of cellular capacity. In this case, running two local auctions is optimal.

We focus on the nontrivial scenario (i.e., the red dots) where the feasibility condition is violated for some realizations of cost parameters but not for others. In this more general scenario, the value of procuring $\left( y _ { 1 } , \ldots , y _ { M } \right)$ Wi-Fi capacity from the M regions depends not only on the total procured Wi-Fi capacity y but also on its distribution across regions. Correspondingly, we denote the value of procuring $\left( y _ { 1 } , \ldots , y _ { M } \right)$ Wi-Fi capacity as $J ( 0 ) \mathrm { ~ - ~ } J ( y _ { 1 } , \ldots , y _ { M } ) .$ where $J ( y _ { 1 } , \dots , y _ { M } )$ is the minimized congestion cost defined in (1). Given $\left( y _ { 1 } , \ldots , y _ { M } \right) .$ , let $\hat { \mu } _ { m }$ be the optimal amount of cellular capacity allocated to region $m ,$ ignoring all of the nonnegativity constraints on $\mu _ { i } \ ( \mathrm { i . e . } ,$ in the global auction). From Proposition 1, we know that $\hat { \mu } _ { m } = \phi _ { m } ( \Psi ( y + \mu ) ) - y _ { m } .$

Intuitively, the optimal auction should be designed so that $\mu _ { m }$ coincides with $\hat { \mu } _ { m }$ whenever $\hat { \mu } _ { m }$ is nonnegative under some realization of $( \theta _ { 1 } , \ldots , \theta _ { N } )$ . On the other hand, whenever $\hat { \mu } _ { m }$ is negative under other realizations of $( \theta _ { 1 } , \ldots , \theta _ { N } )$ , the optimal quantity schedule should be able to adjust the procurement to take into account the corner solution in the second-stage optimization problem (1). In other words, the optimal quantity schedule is likely a nonsmooth function of $( \theta _ { 1 } , \ldots , \theta _ { N } )$ with many segments. However, as long as the quantity schedule is nonincreasing in hot spot type, we can find a truth-telling mechanism to implement it. Fortunately, as we will show in the proof of our next result, the proposed optimal quantity schedule is continuous everywhere, which essentially upgrades local monotonicity into global monotonicity.

The following proposition gives the optimal quantity schedule and payment function.

Proposition 3. The optimal quantity $q _ { i } ^ { * * } = Q _ { i } ^ { * * } ( \theta _ { i } , \theta _ { - i } )$ is determined by

$$
- \Psi \left(\mu + \sum_ {j = 1} ^ {N} q _ {j} ^ {* *}\right) = \alpha c (q _ {i} ^ {* *}, \theta_ {i}) + \alpha c _ {\theta} (q _ {i} ^ {* *}, \theta_ {i}) H (\theta_ {i}),\tag{3}
$$

if the resulting $\hat { \mu } _ { 1 }$ and $\hat { \mu } _ { 2 }$ are both nonnegative, and is determined by

$$
\begin{array}{c} - \omega_ {m} ^ {\prime} \left(\mu \mathbf {1} _ {\hat {\mu} _ {m} > 0} + \sum_ {j \in E _ {m}} q _ {j} ^ {* *}\right) = \alpha c (q _ {i} ^ {* *}, \theta_ {i}) + \alpha c _ {\theta} (q _ {i} ^ {* *}, \theta_ {i}) H (\theta_ {i}), \\ \forall i \in E _ {m}, m = 1, 2, \end{array} \tag {4}
$$

otherwise, where $\mathbf { 1 } _ { \hat { \mu } _ { m } > 0 }$ is the indicator function for $\hat { \mu } _ { m } > 0 .$ The optimal payment schedule $P _ { i } ^ { * * } ( \theta _ { i } , \theta _ { - i } ) ,$ , for $i = 1 , 2 $ $\cdots , n$ , is given by

$$
P _ {i} ^ {* *} (\theta_ {i}, \theta_ {- i}) = \alpha \left(C (q _ {i} ^ {* *}, \theta_ {i}) + \int_ {\theta_ {i}} ^ {\theta^ {*}} C _ {\theta} (Q _ {i} ^ {* *} (\theta , \theta_ {- i}), \theta) d \theta\right).\tag{5}
$$

Proof. The revelation principle implies that we need to focus only on direct mechanisms. Hence, we only need to find the quantity schedule $Q ( \theta _ { i } , \theta _ { - i } )$ that maximizes the service provider’s gain from the procurement auction, taking into account the information rent required for truth telling.

Our proof has three steps. First, given a quantity schedule, we establish the corresponding payment rule that is necessary for incentive compatibility. Second, we optimally choose the quantity schedule. Third, we verify that the proposed quantity schedule is nonincreasing, which ensures that the payment rule is not only necessary but also suficient<sup>11</sup> for incentive compatibility.

Step 1. The expected profit of hot spot provider i with cost parameter θ reporting parameter $\theta ^ { \prime }$ is

$$
\pi (\theta^ {\prime}, \theta) = \mathbb {E} _ {- i} [ \tilde {\alpha} P (\theta^ {\prime}, \theta_ {- i}) - C (Q (\theta^ {\prime}, \theta_ {- i}), \theta) ].
$$

The incentive compatibility implies that $\pi ( \theta , \theta ) \ : -$ $\pi ( \theta , \theta ^ { \prime } ) \geq \pi ( \theta , \theta ) - \pi ( \theta ^ { \prime } , \theta ^ { \prime } ) \geq \pi ( \theta ^ { \prime } , \theta ) - \pi ( \theta ^ { \prime } , \theta ^ { \prime } )$ , or, equivalently,

$$
\begin{array}{l} \mathbb {E} _ {- i} [ C (Q (\theta , \theta_ {- i}), \theta^ {\prime}) - C (Q (\theta , \theta_ {- i}), \theta) ] \\ \qquad \geq \pi (\theta , \theta) - \pi (\theta^ {\prime}, \theta^ {\prime}) \\ \qquad \geq \mathbb {E} _ {- i} [ C (Q (\theta^ {\prime}, \theta_ {- i}), \theta^ {\prime}) - C (Q (\theta^ {\prime}, \theta_ {- i}), \theta) ]. \end{array}
$$

Let $\pi ( \theta ) \equiv \pi ( \theta , \theta )$ . Dividing both sides by $\theta - \theta ^ { \prime }$ and taking limits as $\theta ^ { \prime } \to \theta _ { \ast }$ , we have

$$
\frac {d \pi (\theta)}{d \theta} = - \mathbb {E} _ {- i} [ C _ {\theta} (Q (\theta , \theta_ {- i}), \theta) ].
$$

Integrating both sides from $\theta _ { i }$ to $\theta ^ { * }$ , and using the fact that $\pi ( \bar { \theta ^ { * } } ) = 0 .$ , we have

$$
\begin{array}{l} \pi (\theta_ {i}) = \int_ {\theta_ {i}} ^ {\theta^ {*}} \mathbb {E} _ {- i} [ C _ {\theta} (Q (\theta , \theta_ {- i}), \theta) ] d \theta \\ = \mathbb {E} _ {- i} \left[ \int_ {\theta_ {i}} ^ {\theta^ {*}} C _ {\theta} (Q (\theta , \theta_ {- i}), \theta) d \theta \right]. \end{array}
$$

Hence, the expected payment a hot spot provider with cost parameter $\theta _ { i }$ will receive must satisfy

$$
\begin{array}{l} \mathbb {E} _ {- i} [ \tilde {\alpha} P (\theta_ {i}, \theta_ {- i}) ] \\ = \mathbb {E} _ {- i} \left[ C (Q (\theta_ {i}, \theta_ {- i}), \theta_ {i}) + \int_ {\theta_ {i}} ^ {\theta^ {*}} C _ {\theta} (Q (\theta , \theta_ {- i}), \theta) d \theta \right], \end{array}
$$

and the claim on $P _ { i } ^ { * * } ( \theta _ { i } , \theta _ { - i } )$ follows.

Step 2. We now prove the optimal quantity schedule. From the buyer’s perspective, the expected payment to any hot spot provider is

$$
\begin{array}{r l} & {\mathbb {E} _ {i} [ \mathbb {E} _ {- i} [ P (\theta_ {i}, \theta_ {- i}) ] ]} \\ & {\quad = \alpha \mathbb {E} [ C (Q (\theta_ {i}, \theta_ {- i}), \theta_ {i}) ]} \\ & {\qquad + \alpha \int_ {\underline {{\theta}}} ^ {\theta^ {*}} \left(\int_ {\theta_ {i}} ^ {\theta^ {*}} \mathbb {E} _ {- i} [ C _ {\theta} (Q (\theta , \theta_ {- i}), \theta) ] d \theta\right) d F (\theta_ {i})} \\ & {\quad = \alpha \mathbb {E} [ C (Q (\theta_ {i}, \theta_ {- i}), \theta_ {i}) ]} \\ & {\qquad + \alpha \bigg [ F (\theta_ {i}) \int_ {\theta_ {i}} ^ {\theta^ {*}} \mathbb {E} _ {- i} [ C _ {\theta} (Q (\theta , \theta_ {- i}), \theta) ] d \theta \bigg ] \bigg | _ {\underline {{\theta}}} ^ {\theta^ {*}}} \\ & {\qquad + \alpha \int_ {\underline {{\theta}}} ^ {\theta^ {*}} F (\theta_ {i}) \mathbb {E} _ {- i} [ C _ {\theta} (Q (\theta_ {i}, \theta_ {- i}), \theta_ {i}) ] d \theta_ {i}} \\ & {\quad = \alpha \mathbb {E} [ C (Q (\theta_ {i}, \theta_ {- i}), \theta_ {i}) ]} \\ & {\qquad + \alpha \int_ {\underline {{\theta}}} ^ {\theta^ {*}} \mathbb {E} _ {- i} [ F (\theta_ {i}) C _ {\theta} (Q (\theta_ {i}, \theta_ {- i}), \theta_ {i}) ] d \theta_ {i}} \\ & {\quad = \alpha \mathbb {E} [ C (Q (\theta_ {i}, \theta_ {- i}), \theta_ {i}) ]} \\ & {\qquad + \alpha \mathbb {E} _ {- i} \left[ \int_ {\underline {{\theta}}} ^ {\theta^ {*}} C _ {\theta} (Q (\theta_ {i}, \theta_ {- i}), \theta_ {i}) H (\theta) d F (\theta_ {i}) \right]} \\ & {\quad = \alpha \mathbb {E} [ C (Q (\theta_ {i}, \theta_ {- i}), \theta_ {i}) + C _ {\theta} (Q (\theta_ {i}, \theta_ {- i}), \theta_ {i}) H (\theta_ {i}) ].} \end{array}
$$

Let $q _ { i } \equiv Q ( \theta _ { i } , \theta _ { - i } )$ . The cellular service provider’s total expected cost minimization problem can now be written as the following optimization problem:

$$
\begin{array}{l}\underset { \begin{array}{c}q_{i},i = 1,\ldots ,N\\ \mu_{m},m = 1,\ldots ,M \end{array} }{\min}\Pi = \mathbb{E}\bigg[\sum_{m = 1}^{M}\omega_{m}(\mu_{m} + y_{m})\\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad +\alpha \sum_{i = 1}^{N}C(q_{i},\theta_{i}) + \alpha \sum_{i = 1}^{N}C_{\theta}(q_{i},\theta_{i})H(\theta_{i})\bigg]\\ \text{s.t.}\sum_{m = 1}^{M}\mu_{m}\leq \mu ,\\ \qquad \qquad \qquad \mu_{m}\geq 0,\quad \forall m = 1,2,\ldots ,M,\\ \qquad \qquad \qquad y_{m} = \sum_{i\in E_{m}}q_{i},\forall m = 1,2,\ldots ,M, \end{array}
$$

where the expectation $\mathbb { E } [ \cdot ]$ is taken over $\theta _ { 1 } , \theta _ { 2 } , \ldots , \theta _ { N }$ and the optimization is taken over $N + M$ functions of $\theta _ { 1 } , \theta _ { 2 } , \ldots , \theta _ { N } \colon q _ { i } ( \vec { \theta } )$ and $\mu _ { m } ( { \vec { \theta } } ) , \forall i = 1 , \ldots , N , m =$ $1 , \ldots , M$

The degenerated structure of this variational calculus problem allows us to solve the problem through pointwise optimization over the space of Θ. Based on this observation, we further simplify the problem by dividing the space of Θ into two areas

$$
\begin{array}{l} \Theta_ {1} \equiv \{(\theta_ {1}, \theta_ {2}, \ldots , \theta_ {N}) | \hat {\mu} _ {1} \geq 0, \hat {\mu} _ {2} \geq 0 \}, \\ \Theta_ {2} \equiv \{(\theta_ {1}, \theta_ {2}, \ldots , \theta_ {N}) | \hat {\mu} _ {1} <   0 \text {or} \hat {\mu} _ {2} <   0 \}. \end{array}
$$

If $\begin{array} { r } { \vec { \theta } \in \Theta _ { 1 } , } \end{array}$ the nonnegativity conditions of $\mu _ { m }$ are not binding. Hence, the optimization problem is equivalent to the one studied in Proposition 1. Therefore, the quantity schedule from Proposition 1 is optimal when $ { \vec { \theta } } \in \Theta _ { \tau }$

If $\dot { \theta } \in \Theta _ { 2 } ,$ , then one of the nonnegativity constraints must be binding at the optimum. Without loss of generality, assume $( \breve { \mu } _ { 1 } ^ { * } , \mu _ { 2 } ^ { * } ) = ( \breve { \mu } , 0 )$ at the optimal. The pointwise optimization problem can be simplified as

$$
\begin{array}{r l} \min _ {q _ {1}, \ldots , q _ {N}} & \Pi = \omega_ {1} (\mu + y _ {1}) + \omega_ {2} (y _ {1}) + \alpha \sum_ {i = 1} ^ {N} C (q _ {i}, \theta_ {i}) \\ & \quad + \alpha \sum_ {i = 1} ^ {N} C _ {\theta} (q _ {i}, \theta_ {i}) H (\theta_ {i}), \\ & = \bigg (\omega_ {1} (\mu + y _ {1}) + \alpha \sum_ {i \in E _ {1}} C (q _ {i}, \theta_ {i}) \\ & \quad + \alpha \sum_ {i \in E _ {1}} C _ {\theta} (q _ {i}, \theta_ {i}) H (\theta_ {i}) \bigg) \\ & \quad + \bigg (\omega_ {1} (y _ {2}) + \alpha \sum_ {i \in E _ {2}} C (q _ {i}, \theta_ {i}) \\ & \quad + \alpha \sum_ {i \in E _ {2}} C _ {\theta} (q _ {i}, \theta_ {i}) H (\theta_ {i}) \bigg) \\ & \text {s.t.} y _ {m} = \sum_ {i \in E _ {m}} q _ {i}, \quad \forall m = 1, 2, \end{array}
$$

which is the same as that of designing two separate local auctions. Therefore, with $\theta \in \Theta _ { 2 }$ , the optimal mechanism is equivalent to holding two separate local auctions, with all cellular resources allocated to one of the regions.

Step 3. Finally, to ensure that the payment schedule is not only necessary but also suficient for incentive compatibility, we need to verify that Ɛ− $_ i [ Q _ { i } ^ { * * } ( \theta _ { i } , \theta _ { - i } ) ]$ is nonincreasing in $\theta _ { i }$ . It sufices to show that $q _ { i } ^ { * * } = Q _ { i } ^ { * * } ( \theta _ { i } , \theta _ { - i } )$ is decreasing in $\theta _ { i }$ given any $\theta _ { - i }$ . Note that by our assumptions on hot spot cost structure and $\boldsymbol { H } ( { \dot { \boldsymbol { \theta } } } ) , \boldsymbol { q } _ { i } ^ { * * }$ is decreasing within the region of $\theta _ { i } ,$ where either the global auction is optimal or the local auction is optimal. The only possible violation of the monotonicity property is when the value of $\theta _ { i }$ crosses some threshold below (above) which local (global) is optimal or vice versa. Clearly, if $q _ { i } ^ { * * }$ is continuous at such thresholds, local monotonicity implies global monotonicity.<sup>12</sup>

To establish continuity, we first denote the region to which hot spot i belongs as region 1 and note that the global auction is chosen if and only if $\hat { \mu } _ { 1 } =$ $\phi _ { 1 } ( \Psi ( y + \mu ) ) - y _ { 1 } > 0$ and $\hat { \mu } _ { 1 } < \mu ,$ or, equivalently, $- \omega _ { 1 } ^ { \prime } ( y _ { 1 } ) > - \Psi ( y + \mu )$ and $- \omega _ { 1 } ^ { \prime } ( y _ { 1 } + \mu ) < - \Psi ( y + \mu )$ Define the threshold $\tilde { \theta } _ { i }$ as the value of $\theta _ { i }$ such that $- \omega _ { 1 } ^ { \prime } ( y _ { 1 } ) = - \Psi ( y + \mu ) \equiv$ m˜ and the threshold $\hat { \theta } _ { i }$ as the value of $\theta _ { i }$ such that $- \omega _ { 1 } ^ { \prime } ( y _ { 1 } + \mu ) = - \Psi ( y + \mu ) \equiv \hat { m }$ Clearly, $\tilde { \theta } _ { i } \neq \hat { \theta } _ { i }$ because of the strict convexity of $\omega _ { 1 } ( \cdot )$ Denote the solution to the following equation by $\tilde { q } _ { i } \mathrm { : }$

$$
\tilde {m} = \alpha c (q _ {i} ^ {* *}, \theta_ {i}) + \alpha c _ {\theta} (q _ {i} ^ {* *}, \theta_ {i}) H (\theta_ {i}).
$$

Denote the solution to the following equation by $\hat { q } _ { i } \mathrm { . }$ :

$$
\hat {m} = \alpha c (q _ {i} ^ {* *}, \theta_ {i}) + \alpha c _ {\theta} (q _ {i} ^ {* *}, \theta_ {i}) H (\theta_ {i}).
$$

Let $\epsilon > 0$ be small enough. Then, for any $\theta \in ( \tilde { \theta } _ { i } - \epsilon$ $\tilde { { \boldsymbol { \theta } } } _ { i } + { \boldsymbol { \epsilon } } ) , q _ { i } ^ { * * }$ is either the solution to the equation

$$
- \Psi (\mu + y) = \alpha c (q _ {i} ^ {* *}, \theta_ {i}) + \alpha c _ {\theta} (q _ {i} ^ {* *}, \theta_ {i}) H (\theta_ {i}),\tag{6}
$$

or the solution to the equation

$$
- \omega_ {1} ^ {\prime} (y _ {1}) = \alpha c (q _ {i} ^ {* *}, \theta_ {i}) + \alpha c _ {\theta} (q _ {i} ^ {* *}, \theta_ {i}) H (\theta_ {i}).\tag{7}
$$

Because the left-hand sides of both Equations (6) and (7) equal m˜ at $\theta _ { i } = \tilde { \theta } _ { i }$ and the right-hand sides of both equations are the same continuous function of $\theta _ { i } ,$ we have $\begin{array} { r } { \operatorname* { l i m } _ { \theta _ { i } \to \tilde { \theta } _ { i } - } q _ { i } ^ { * * } = \operatorname* { l i m } _ { \theta _ { i } \to \tilde { \theta } _ { i } + } q _ { i } ^ { * * } = \tilde { q } _ { i } } \end{array}$ . Hence, $q _ { i } ^ { * * }$ is continuous at $\tilde { \theta } _ { i }$ . Similarly, we can show that $q _ { i } ^ { * * }$ is also continuous at $\hat { \theta } _ { i }$ . Therefore, $\cdot \ q _ { i } ^ { * * }$ is everywhere continuous and is thus decreasing in its range. <sup></sup>

Note that the above auction mechanism has a nice economic interpretation as the integration of a global auction and local auctions. Whenever the feasibility condition is satisfied, the mechanism is equivalent to the optimal mechanism described in Proposition $^ { 1 , }$ which is essentially a global auction that includes all hot spots from both regions. Whenever the feasibility condition is violated, the optimal mechanism is to allocate all cellular capacity to one region and to organize one local auction for each region. This integration of global and local auctions in the optimal procurement auction is the consequence of two unique features of procuring Wi-Fi capacity for mobile trafic of-loading: (1) the coupling of the local auction because of the existence of the more flexible cellular capacity and (2) the heterogeneity of demand for mobile bandwidth and supply of Wi-Fi capacity in diferent regions.

However, there is only one auction, and the choice between running a global auction and running two local auctions is endogeneously determined by the auctioneer based on the realization of $( \theta _ { 1 } , \dots , \bar { \theta } _ { N } )$ . From the perspective of a hot spot, ex ante, it does not know whether it will participate in a global auction or a local auction. It does not need to know. What matters to a hot spot is only the payment and quantity schedule designed by the auctioneer. Based on these schedules and its expectation of the types of all other hot spots, it is optimal for the hot spot to truthfully report its type by our mechanism design.

3.4. Integrating Global and Local Auctions, $M > 2$ With more than two regions, the basic idea of integrating multiple local auctions and one global auction remains the same, although the optimal grouping of Wi-Fi regions becomes more complicated. We denote by $R _ { g }$ the set of regions where cellular capacity will be allocated $( \mathrm { i . e . , }$ regions that participate in a global auction) and denote by $R _ { l }$ the set of regions where cellular capacity will not be allocated (i.e., regions that participate in local auctions). The optimal auction involves one local auction for each region in $R _ { l }$ where no cellular resource will be allocated and one global auction for all regions in $R _ { g }$ where all cellular resources will be allocated.

The key is to optimally divide the set of regions into $R _ { g }$ and $R _ { l }$ . Intuitively, whether a region—say region m—should be in $R _ { l }$ or $R _ { g }$ depends on whether the nonnegativity constraint $\mu _ { m } ^ { \mathrm { ~ \ j ~ } } \ge 0$ will be binding or not if it participates in the global auction. Yet we can evaluate whether $\mu _ { m } \geq 0$ only after we construct $R _ { g }$ and $R _ { l } .$ Because the number of ways of dividing regions into $R _ { g }$ and $R _ { l }$ increases exponentially with the number of regions, a brute-force approach of checking each possible division is practically infeasible. Hence, we must find a division algorithm whose complexity is polynomial in the number of regions. To achieve this goal, we first note in the following proposition that $R _ { g }$ should be as large as possible to achieve optimality.

Proposition 4. Given $M \geq 2$ and $( \theta _ { 1 } , \dots , \theta _ { N } )$ , suppose there are two diferent schemes of dividing the regions into global and local auctions, both of which lead to a feasible allocation of cellular capacity: $I f \left( R _ { g } , R _ { l } \right)$ and $( \tilde { R } _ { g } ^ { \prime } , \tilde { R } _ { l } )$ where $\tilde { R } _ { g } \subset R _ { g }$ , then the optimal gain corresponding to the auction design with $( R _ { g } , \dot { R _ { l } } )$ is larger than the optimal gain corresponding to the auction design with $( \tilde { R } _ { g } , \tilde { R } _ { l } )$ .

Proof. We write down the optimal auction design problem with $( R _ { g } , R _ { l } )$ as

$$
\begin{array}{rl}\min_{\substack{q_{i},i = 1,\ldots ,n\\ \mu_{m},m = 1,\ldots ,M}} & \Pi = \sum_{m = 1}^{M}\omega_{m}(\mu_{m} + y_{m}) + \alpha \sum_{i = 1}^{N}C(q_{i},\theta_{i})\\ & \qquad +\alpha \sum_{i = 1}^{N}C_{\theta}(q_{i},\theta_{i})H(\theta_{i})\\ \text{s.t.} & \sum_{m\in R_{g}}\mu_{m}\leq \mu , \end{array}
$$

$$
\begin{array}{r l} & {\mu_ {m} \geq 0, \quad \forall m \in R _ {g},} \\ & {\mu_ {m} = 0, \quad \forall m \in R _ {l},} \\ & {y _ {m} = \sum_ {i \in E _ {m}} q _ {i}, \quad \forall m = 1, 2, \ldots , M.} \end{array}
$$

Because ${ \tilde { R } } _ { g } \subset R _ { g } ,$ the optimal auction design problem with $( \tilde { R } _ { g } , \mathring { R } _ { l } )$ is the same as the above problem except with the additional constraints that $\begin{array} { r } { \mu _ { m } = 0 , } \end{array}$ , <sup>∀</sup> m ∈ $\hat { R _ { g } } \backslash \tilde { R } _ { g } .$ . Clearly, the minimized total cost corresponding to $( R _ { g } ^ { \cup } , R _ { l } )$ should be smaller than the minimized total cost corresponding to $( \tilde { R } _ { g } , \tilde { R } _ { l } )$ . □

Given that we need to find the largest possible $R _ { \mathfrak { o } }$ to achieve optimality, we should clearly start with all of the regions—that is, $R _ { g } = \{ 1 , \ldots , M \}$ . If doing this leads to an infeasible allocation of cellular capacity, we will have to shrink $R _ { g }$ in some way. Intuitively, we should exclude those regions with $\boldsymbol { \mu } _ { m } ^ { * } < 0$ from $R _ { g }$ to restore feasibility, which would naturally give rise to a sequential procedure of constructing $R _ { g }$ and $R _ { l }$ . However, the main concern with the sequential procedure is whether “exclusion” should be irreversible. In other words, if a region is excluded from $R _ { g } ,$ , would it be beneficial to put it back into $R _ { g }$ at some later step in this sequential procedure? Our next result shows that the answer is no. The key insight is that if a region is in $R _ { l }$ at some stage, then it will be in $R _ { l }$ in later stages had it remained in $R _ { g } ,$ , which justifies the irreversible shrinking of $R _ { g }$ and guarantees the algorithm complexity of the order of O<sup>(</sup>M<sup>)</sup>.

To describe the procedure, we first introduce the notations for the k subproblem. Let $\begin{array} { r } { Y _ { k } = \sum _ { m \in R _ { g } ^ { k } } y _ { m , k } , } \end{array}$ where $\begin{array} { r } { y _ { m , k } = \sum _ { i \in E _ { m } } q _ { i , k } , } \end{array}$ and $q _ { i , k }$ is determined by the following equation:

$$
\begin{array}{c} - \Psi (Y _ {k} + \mu) = \alpha c (q _ {i, k}, \theta_ {i}) + \alpha c _ {\theta} (q _ {i, k}, \theta_ {i}) H (\theta_ {i}), \\ \forall   i \in \bigcup_ {m \in R _ {g} ^ {k}} E _ {m}. \end{array}
$$

Let $\mu _ { m , k } ^ { * } = \phi _ { m } ( \Psi ( Y _ { k } + \mu ) ) - y _ { m , k } , R _ { + } ^ { k } \equiv \{ m \in R _ { g } ^ { k } | \mu _ { m , k } ^ { * } \geq 0 \} .$ and $R _ { - } ^ { k } \equiv \{ m \in R _ { g } ^ { k } | \mu _ { m , k } ^ { * } < 0 \}$

Proposition 5. Given $M \geq 2$ and $( \theta _ { 1 } , \dots , \theta _ { N } )$ , the optimal quantity schedule $q _ { i } ^ { * * }$ is given by

$$
\begin{array}{c} - \Psi \bigg (\mu + \sum_ {j \in E _ {m}, m \in R _ {g}} q _ {j} ^ {* *} \bigg) = \alpha c (q _ {i} ^ {* *}, \theta_ {i}) + \alpha c _ {\theta} (q _ {i} ^ {* *}, \theta_ {i}) H (\theta_ {i}), \\ \forall   i \in E _ {m},   m \in R _ {g}, \\ - \omega_ {m} ^ {\prime} \bigg (\sum_ {j \in E _ {m}} q _ {j} ^ {* *} \bigg) = \alpha c (q _ {i} ^ {* *}, \theta_ {i}) + \alpha c _ {\theta} (q _ {i} ^ {* *}, \theta_ {i}) H (\theta_ {i}), \\ \forall   i \in E _ {m},   m \in R _ {l}, \end{array}
$$

where $R _ { g }$ and $R _ { l }$ are constructed through the following iterative procedure:

• Step $0 . \ L e t \ k = M , R _ { \sigma } ^ { M } = \{ 1 , 2 , \ldots , M \}$ , and $R _ { \iota } ^ { M } = \varnothing$

• Step 1. $I f R _ { - } ^ { k } = \emptyset ,$ , let $R _ { g } = R _ { g } ^ { k }$ and $R _ { l } = R _ { l } ^ { k }$ . Stop the procedure.

• Step 2. If $R _ { - } ^ { k } \neq \emptyset ,$ , let $R _ { g } ^ { k - 1 } = R _ { + } ^ { k }$ and $R _ { l } ^ { k - 1 } = R _ { l } ^ { k } \cup R _ { - } ^ { k }$ Decrease k by 1 and repeat Step 1.

The optimal payment schedule $P _ { i } ^ { * * }$ , for $i = 1 , 2 , . . . n$ , is given by

$$
P _ {i} ^ {* *} = \alpha \left(C (q _ {i} ^ {* *}, \theta_ {i}) + \int_ {\theta_ {i}} ^ {\theta^ {*}} C _ {\theta} (q _ {i} ^ {* *}, \theta) d \theta\right).\tag{8}
$$

Proof. From the proof of Proposition $^ { 3 , }$ we know that the optimal mechanism is an integration of one global auction and at most $M - 1$ local auctions. With $\bar { M } > 2 ,$ the key is to determine the optimal division of regions into $\dot { R _ { g } }$ and $R _ { l }$

The first part of this proposition is a straightforward generalization of Proposition 3 and the proof is omitted. The second part ofers an eficient algorithm for constructing the optimal $R _ { g }$ and $R _ { l }$ with the complexity of O<sup>(</sup>M<sup>)</sup>.

The key to proving the efectiveness of this algorithm is showing that if a region is in $R _ { l }$ at some stage, then it will always be in $R _ { l }$ in later stages. Therefore, at each stage, we should shrink $R _ { g } ^ { k }$ by moving all of those regions in $R _ { - } ^ { k }$ to $R _ { l } ^ { k - 1 }$ and none of those regions in $R _ { + } ^ { k }$ to $\mathsf { R } _ { l } ^ { k - 1 }$ . In this way, we keep $R _ { g }$ as large as possible $( \mathrm { i . e . , }$ by not moving those regions in $R _ { + } ^ { k } )$ while attempting to restore feasibility (i.e., by moving those regions in R<sup>k</sup> to $R _ { l } )$

Mathematically, we need to show that, given $t \in R _ { - } ^ { k }$ and $s \neq t ,$ , if we let $R _ { g } ^ { k - 1 } = R _ { g } ^ { k } \backslash \{ s \}$ , then $t \in R _ { - } ^ { k - 1 }$ . Note δ that s could be in either $R _ { + } ^ { k }$ $R _ { - } ^ { k }$

Consider the k subproblem. The Wi-Fi capacity procurement $q _ { i , k } = Q ^ { * } ( \bar { \theta _ { i } } , \bar { \theta } _ { - i } )$ , is determined by

$$
\begin{array}{c} - \Psi (\mu + Y _ {k}) = \alpha c (q _ {i, k}, \theta_ {i}) + \alpha c _ {\theta} (q _ {i, k}, \theta_ {i}) H (\theta_ {i}), \\ \forall   i \in \bigcup_ {m \in R _ {g} ^ {k}} E _ {m}, \end{array}\tag{9}
$$

where $\begin{array} { r } { Y _ { k } = \sum _ { i \in \cup _ { m \in R _ { \alpha } ^ { k } } E _ { m } } q _ { i , k } . } \end{array}$

In the <sup>(</sup>k <sup>−</sup> 1<sup>)</sup> subproblem, $q _ { i , k - 1 } ,$ is determined by the following equation:

$$
\begin{array}{c} - \Psi (\mu + Y _ {k - 1}) = \alpha c (q _ {i, k - 1}, \theta_ {i}) + \alpha c _ {\theta} (q _ {i, k - 1}, \theta_ {i}) H (\theta_ {i}), \\ \forall   i \in \bigcup_ {m \in R _ {g} ^ {k - 1}} E _ {m}, \quad ( \end{array}\tag{10}
$$

where $\begin{array} { r } { Y _ { k - 1 } = \sum _ { i \in \cup _ { m \in R ^ { k - 1 } } E _ { m } } q _ { i , k - 1 } , } \end{array}$

We first show that g $Y _ { k - 1 } \le Y _ { k }$ by contradiction. Suppose $Y _ { k - 1 } > Y _ { k } ;$ the $\mathfrak { l } , - \Psi ( \mu + Y _ { k } ) > - \Psi ( \mu + Y _ { k - 1 } )$ because $\mathbf { \bar { \Psi } } ( \cdot ) ^ { \prime } > 0$ . Hence, the right-hand side of Equation (9) is greater than the right-hand side of Equation (10) for all $i \in \cup _ { m \in R _ { g } ^ { k - 1 } } E _ { m }$ . Yet $\alpha c ( q , \theta _ { i } ) + \alpha c _ { \theta } ( \bar { q , { \theta _ { i } } } ) H ( \theta _ { i } )$ is increasing in $q .$ Therefore, we must have $q _ { i , k } > q _ { i , k - 1 } ,$ $\forall i \in \cup _ { m \in R _ { \sigma } ^ { k - 1 } } E _ { m } ,$ which implies

$$
\begin{array}{l} Y _ {k} = \sum_ {i \in E _ {s}} q _ {i, k} + \sum_ {i \in \bigcup_ {m \in R _ {g} ^ {k - 1}} E _ {m}} q _ {i, k} \geq \sum_ {i \in \bigcup_ {m \in R _ {g} ^ {k - 1}} E _ {m}} q _ {i, k} \\ > \sum_ {i \in \bigcup_ {m \in R _ {g} ^ {k - 1}} E _ {m}} q _ {i, k - 1} = Y _ {k - 1}, \end{array}
$$

a contradiction. Because $Y _ { k - 1 } \leq Y _ { k }$ , we immediately see that $q _ { i , k } \leq q _ { i , k - 1 } ,$ for all $i \in \cup _ { m \in R _ { g } ^ { k - 1 } } E _ { m } ,$ , which implies $y _ { m , k } \leq y _ { m , k - 1 } .$ , for all m <sup>∈</sup> $R _ { g } ^ { k - 1 }$

Second, we show that $\bar { \mu } _ { m , k - 1 } ^ { * } \leq \mu _ { m , k } ^ { * } ,$ , for all $m \in R _ { g } ^ { k - 1 }$ To see this, note that

$$
\begin{array}{l} \mu_ {m, k - 1} ^ {*} \\ \qquad = \phi_ {m} (\Psi (Y _ {k - 1} + \mu)) - y _ {m, k - 1} \leq \phi_ {m} (\Psi (Y _ {k} + \mu)) - y _ {m, k - 1} \\ \qquad \leq \phi_ {m} (\Psi (Y _ {k} + \mu)) - y _ {m, k} = \mu_ {m, k} ^ {*}, \end{array}
$$

where the first inequality is because $\phi _ { m } ^ { \prime } > 0 , \Psi ^ { \prime } > 0$ , and $Y _ { k - 1 } \le Y _ { k }$ , and the second inequality is because $y _ { m , k } \leq$ $y _ { m , k - 1 } .$

Therefore, we have $\mu _ { t , k - 1 } ^ { * } \leq \mu _ { t , k } ^ { * } < 0 ,$ , or, equivalently, $t \in R _ { - } ^ { k - 1 }$ . 

## 4. Concluding Remarks

In the present study, we designed an optimal auction mechanism for Wi-Fi procurement so that cellular service providers can of-load mobile data. The integration of both cellular and Wi-Fi resources significantly improves mobile bandwidth availability. A unique challenge in this procurement auction is that the longer-range cellular resource introduces coupling among the shorter-range Wi-Fi hot spots. We solved for the optimal auction mechanism and showed that the optimal auction can be interpreted as an endogeneously determined combination of a global auction and many local auctions.

The actual auctions and of-loading to Wi-Fi would need to be integrated with the policy management infrastructure, which supplies some of the key variables in the auction valuation: (1) the currently ofered data trafic, (2) the capacity of each cell tower, and (3) the structure of the congestion cost. The proposed procurement auction integrates all relevant information into the supply chain through wireless networks. Our procurement mechanism extends beyond the limits of service providers’ cellular resources to interconnect multiple hot spots in diferent regions. Conventional data of-loading is based on the access network discovery and selection function (ANDSF)<sup>13</sup> that processes static Wi-Fi of-load policies. Recently, the intelligent mobile solution company Tekelec Inc. developed its Mobile Policy Gateway (MPG) to implement complex Wi-Fi of-load policies. The Tekelec MPG enables support for our smart data of-loading based on the auction approach.

Our procurement auction design problem can be regarded as a subproblem of a capacity expansion project for a cellular service provider. Given a cellular sector, the cellular service provider can compare the option of using Wi-Fi capacity procurement with building a new cell tower. By comparing the net gain of each option $( \mathrm { i . e . , }$ the diference between the reduced congestion cost and the cost of capacity expansion, whether through Wi-Fi procurement or building a tower), the service provider can select the one that yields the higher net gain. In our model, the benefit of using Wi-Fi capacity procurement is the expected reduction of congestion cost, which is given by $\mathbb { \bar { E } } [ J ( 0 , \dots , 0 ) - J ( y _ { 1 } ^ { * } , \dots , y _ { M } ^ { * } ) ] .$ where $\boldsymbol { y } _ { m } ^ { * }$ is the optimal amount of Wi-Fi capacity procured in region $m ,$ and $J ( y _ { 1 } ^ { * } , \ldots , y _ { M } ^ { * } )$ is the corresponding congestion cost defined in Equation (1). The total payment to Wi-Fi hot spots and the Internet service provider is $\mathbb { E } [ \sum _ { i = 1 } ^ { N } P _ { i } ^ { * * } ( \theta _ { i } , \overleftarrow { \theta } _ { - i } ) ]$ . Therefore, the net gain from Wi-Fi procurement is $\mathbb { E } [ J ( 0 , \dots , 0 ) - J ( y _ { 1 } ^ { * } , \dots , y _ { M } ^ { * } ) -$ $\begin{array} { r l } { ~ } & { { } \sum _ { i = 1 } ^ { N } P _ { i } ^ { * * } ( \theta _ { i } , \mathbf { \dot { \theta } } _ { - i } ) \big ] } \end{array}$ . To determine the optimal amount of cellular capacity, we assume that the cost of increasing the cellular capacity from $\mu$ to $\mu + \mu _ { 0 }$ is $V ( \mu _ { 0 } )$ , where $V ( \cdot )$ is most likely discontinuous at 0 because of the fixed cost of building a new cell tower. The minimized total cost from increasing cellular capacity is the optimized objective of the following problem:

$$
K(\mu_{0}) = \min_{\mu_{0}\geq 0}\Bigg(V(\mu_{0}) + \min_{\substack{\mu_{1},\ldots ,\mu_{m}\in \mathbb{R}^{+}\\ \sum_{i}\mu_{i}\leq \mu +\mu_{0}}}\sum_{m = 1}^{M}\omega_{m}(\mu_{m})\Bigg).
$$

Let $\mu _ { 0 } ^ { * }$ be the optimal $\mu _ { 0 }$ to the above problem. Then, the cellular service provider prefers (1) to add $\mu _ { 0 } ^ { * }$ cellular capacity if $K ( \mu _ { 0 } ^ { * } )$ < min $\{ J ( 0 , \ldots , 0 ) , \mathbb { E } [ J ( y _ { 1 } ^ { * } , \ldots , y _ { M } ^ { * } )$ + $\begin{array} { r l } & { \sum _ { i = 1 } ^ { N } \bar { P } _ { i } ^ { * * } ( \theta _ { i } , \theta _ { - i } ) ] \dag ; ( 2 ) } \end{array}$ to procure bandwidth from Wi-Fi hot spots if $\begin{array} { r } { \mathsf { E } [ J ( y _ { 1 } ^ { \ast } , \dots , y _ { M } ^ { \ast } ) + \sum _ { i = 1 } ^ { N } P _ { i } ^ { \ast \ast } ( \theta _ { i } , \theta _ { - i } ) ] < } \end{array}$ min $\{ J ( 0 , \ldots , 0 ) , K ( \mu _ { 0 } ^ { * } ) \} ;$ ; and (3) to seek no additional capacity otherwise.

The model in the present study can also be useful for certain supply chain problems. Consider a firm that produces multiple products using a shared resource (in-house capacity) that is common to products 1 and 2. Because of capacity limitations, the firm also needs to procure the products from diferent suppliers. Supplier 1 produces only product 1; suppliers 2–4 produce only product 2. Because the in-house capacity is a shared resource that can be used for all products, it is suboptimal to decompose this supply chain problem into two independent procurement problems. Our theoretical model provides an auction framework for the downstream firm to optimally integrate the upstream capacity with its own product-flexible capacity.

We recognize several limitations in the present research. First, only one cellular service provider is considered in our procurement auction. One direction for future research is to extend our model to a setting with multiple cellular service providers. Second, we assumed the marginal cost function of all hot spots can be approximated using a one-parameter function family. This is a simplifying assumption. It could be interesting to explore how multiple dimensions of hot spot heterogeneity interact with the optimal auction design. Finally, our study focused on the supply-side reaction to congestion by assuming exogenous demand rates to improve analytical tractability. As a future research direction, it is important to study the demand-side reaction by estimating consumer response to congestion using empirical data.

## Acknowledgments

The authors thank the senior editor, associate editor, and three anonymous reviewers for their detailed and constructive comments. The authors thank Xianjun Geng, Dale Stahl, Maxwell Stinchcombe, and Thomas Wiseman for useful comments. The authors also thank seminar participants at the University of Florida, George Washington University, Beĳing University, the 2013 International Conference on Information Systems, the 48th Hawaii International Conference on System Sciences, the 26th Annual POMS Conference, and the 2017 China Summer Workshop on Information Management for useful discussions. The authors are grateful to Chee Ching, Yu Jin, and Wen-Ling Hsu from AT&T for valuable inputs from the industry perspective. The authors are solely responsible for any existing errors.

## Endnotes

<sup>1</sup> According to Balachandran et al. (2008), although cell-splitting provides capacity benefits, it could be quite expensive and economically infeasible since in addition to the base station hardware/deployment cost, each of the new bases needs to be provided with backhaul connectivity via either wireline access or microwave links.

<sup>2</sup> This concern is also reflected in the action taken by the FCC to block the recent merger between AT&T and T-Mobile USA.

<sup>3</sup> See, for example, the work of Bajari et al. (2009), who considered several determinants that may influence the choice of auctions versus negotiations. For complex projects, auctions may stifle communication between the buyer and the contractor. Clearly, Wi-Fi capacity satisfies the standard assumption of well-defined products in the auction literature.

<sup>4</sup> In the automotive industry, the plants of most of the automobile companies are much more flexible than before: Ford’s Rouge plant can manufacture nine diferent products (Goyal and Netessine 2011).

<sup>5</sup> For the proof, please refer to Lemma 1 in Online Appendix A.

<sup>6</sup> The proof is as follows: $\omega ^ { \prime } ( \mu ) = \chi ^ { \prime } ( W ) \cdot W ^ { \prime } ( \mu ) < 0 , \omega ^ { \prime \prime } ( \mu ) =$ $\chi ^ { \prime \prime } ( W ) \bar { ( } W ^ { \prime } ( \mu ) ) ^ { 2 } + \chi ^ { \prime } ( W ) W ^ { \prime \prime } ( \mu ) > 0 .$

<sup>7</sup> See Wikipedia, s.v. “Wi-Fi,” http://en.wikipedia.org/wiki/Wifi, and s.v. “Cell site,” http://en.wikipedia.org/wiki/Cell\_site (accessed July 20, 2018).

<sup>8</sup> For example, one can generate regions by clustering the Wi-Fi hot spots using a k-means method. For simplicity, we assume that cellular capacity can be reallocated seamlessly from one Wi-Fi region to another. In practice, some cellular capacity can be redirected (e.g., core processing for the base station), and some capacity cannot be redirected (e.g., radio capacity for directional antennas—these cover only a certain direction and angular range).

<sup>9</sup> Note that our problem can be regarded as a subproblem of a capacity expansion project for a cellular service provider. Given a cellular sector, the cellular service provider can compare the option of (i) procuring Wi-Fi capacity, or (ii) building a new cell tower, or (iii) not to seek any capacity expansion. By evaluating and comparing the overall benefits (i.e., the diference between the reduced congestion cost and the cost of capacity expansion, whether through Wi-Fi procurement or building a cell tower), the service provider can select the best action. We discuss this more formally in Section 4. Intuitively, Wi-Fi procurement will be preferred in situations where (i) the existing tower capacity is not terribly insuficient given the customer demand or (ii) there are plenty of inexpensive Wi-Fi hot spots in the regions. On the other hand, in regions where the demand or the growth of demand is enormous and the existing cellular capacity is very insuficient, building a new cell tower might be more costefective than procuring Wi-Fi capacity from hot spots.

<sup>10</sup> For more details on the simulation, please refer to Online Appendix B.

<sup>11</sup> For the proof, see Dasgupta and Spulber (1990, p. 14).

<sup>12</sup> In Lemma 2 in Online Appendix A, we prove a stronger result that a continuous and locally decreasing function is globally decreasing, which is suficient for the case of any M <sup>≥</sup> 2.

<sup>13</sup> The purpose of the ANDSF is to assist user equipment to discover and select non-3rd Generation Partnership Project (3GPP) networks such as Wi-Fi and WiMax.

## References

Aĳaz A, Aghvami H, Amani M (2013) A survey on mobile data ofloading: Technical and business perspectives. IEEE Wireless Comm. 20(2):104–112.

Bajari P, McMillan R, Tadelis S (2009) Auctions versus negotiations in procurement: An empirical analysis. J. Law, Econom., Organ. 25(2):372–399.

Balachandran K, Kang J, Karakayali K, Singh J (2008) Capacity benefits of relays with in-band backhauling in cellular networks. Gong K, Letaief KB, Niu Z, eds. Proc. IEEE Internat. Conf. Comm. (IEEE, Piscataway, NJ), 3736–3742.

Balasubramanian A, Mahajan R, Venkataramani A (2010) Augmenting mobile 3g using WiFi. Banerjee S, ed. Proc. 8th Internat. Conf. Mobile Systems, Appl., Services (ACM, New York), 209–222.

Bichler M, Gupta A, Ketter W (2010) Designing smart markets. Inform. Systems Res. 21(4):688–699.

Bulut E, Szymanski B (2012) WiFi access point deployment for eficient mobile data ofloading. Akan ÖB, Ekici E, eds. Proc. First ACM Internat. Workshop on Practical Issues Appl. Next Generation Wireless Networks (ACM, New York), 45–50.

Cachon G, Feldman P (2011) Pricing services subject to congestion: Charge per-use fees or sell subscriptions? Manufacturing Service Oper. Management 13(2):244–260.

Che Y (1993) Design competition through multidimensional auctions. RAND J. Econom. 24(4):668–680.

Cheng HK, Bandyopadhyay S, Guo H (2011) The debate on net neutrality: A policy perspective. Inform. Systems Res. 22(1):60–82.

Cisco (2017) Cisco visual networking index: Global mobile data trafic forecast update, 2016–2021. Accessed July 27, 2017, https://www.cisco.com/c/en/us/solutions/collateral/service -provider/visual-networking-index-vni/mobile-white-paper -c11-520862.pdf.

Cramton P, Skrzypacz A, Wilson R (2007) The 700 MHz spectrum auction: An opportunity to protect competition in a consolidating industry. Working paper, University of Maryland, College Park.

Dasgupta S, Spulber D (1990) Managing procurement auctions. Inform. Econom. Policy 4(1):5–29.

Dong W, Rallapalli S, Jana R, Qiu L, Ramakrishnan KK, Razoumov L, Zhang Y, Cho TW (2014) ideal: Incentivized dynamic cellular ofloading via auctions. IEEE/ACM Trans. Networking 22(4): 1271–1284.

Duenyas I, Hu B, Beil DR (2013) Simple auctions for supply contracts. Management Sci. 59(10):2332–2342.

Fine CH, Freund RM (1990) Optimal investment in product-flexible manufacturing capacity. Management Sci. 36(4):449–466.

Goyal M, Netessine S (2011) Volume flexibility, product flexibility, or both: The role of demand correlation and product substitution. Manufacturing Service Oper. Management 13(2):180–193.

Gupta A, Jukic B, Stahl D, Whinston A (2011) An analysis of incentives for network infrastructure investment under diferent pricing strategies. Inform. Systems Res. 22(2):215–232.

Iosifidis G, Gao L, Huang J, Tassiulas L (2015) A double auction mechanism for mobile data-ofloading markets. IEEE/ACM Trans. Networking 23(5):1634–1647.

Janakiraman G, Nagarajan M, Veeraraghavan S (2018) Simple policies for managing flexible capacity. Manufacturing Service Oper. Management 20(2):333–346.

Kang X, Chia YK, Sun S, Chong HF (2014) Mobile data ofloading through a third-party WiFi access point: An operator’s perspective. IEEE Trans. Wireless Comm. 13(10):5340–5351.

Netessine S, Dobson G, Shumsky R (2002) Flexible service capacity: Optimal investment and the impact of demand correlation. Oper. Res. 50(2):375–388.

Paul U, Subramanian A, Buddhikot M, Das S (2011) Understanding trafic dynamics in cellular data networks. Ni L, Zhang W, eds. Proc. IEEE INFOCOM (IEEE, Piscataway, NJ), 882–890.

Sen S, Joe-Wong C, Ha S, Chiang M (2012) Incentivizing time-shifting of data: A survey of time-dependent pricing for Internet access. IEEE Comm. Magazine 50(11):91–99.

Tan Y, Carrillo JE (2017) Strategic analysis of the agency model for digital goods. Production Oper. Management 26(4):724–741.

Tan Y, Carrillo JE, Cheng HK (2016) The agency model for digital goods. Decision Sci. 47(4):628–660.

Van Mieghem J (1998) Investment strategies for flexible resources. Management Sci. 44(8):1071–1078.

Weber T (2014) Intermediation in a sharing economy: Insurance, moral hazard, and rent extraction. J. Management Inform. Systems 31(3):35–71.

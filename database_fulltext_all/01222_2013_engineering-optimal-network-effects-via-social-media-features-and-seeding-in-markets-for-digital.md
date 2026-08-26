---
otero_id: 1222
otero_key: "G3RW422Q"
title: "Engineering Optimal Network Effects via Social Media Features and Seeding in Markets for Digital Goods and Services"
authors: "Yifan Dou; Marius F. Niculescu; D. J. Wu"
year: "2013"
journal: "Information Systems Research"
doi: "10.1287/isre.1120.0463"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Engineering Optimal Network Effects via Social Media Features and Seeding in Markets for Digital Goods and Services

Yifan Dou

School of Economics and Management, Beihang University, Beijing 100191, China, dou@buaa.edu.cn

Marius F. Niculescu, D. J. Wu

Scheller College of Business, Georgia Institute of Technology, Atlanta, Georgia 30308, {marius.niculescu@scheller.gatech.edu, dj.wu@scheller.gatech.edu}

irms nowadays are increasingly proactive in trying to strategically capitalize on consumer networks and social interactions. In this paper, we complement an emerging body of research on the engineering of wordof-mouth effects by exploring a different angle through which firms can strategically exploit the value-generation potential of the user network. Namely, we consider how software firms should optimize the strength of network effects at utility level by adjusting the level of embedded social media features in tandem with the right market seeding and pricing strategies in the presence of seeding disutility. We explore two opposing seeding cost models where seeding-induced disutility can be either positively or negatively correlated with customer type. We consider both complete and incomplete information scenarios for the firm. Under complete information, we uncover a complementarity relationship between seeding and building social media features that holds for both disutility models. When the cost of any of these actions increases, rather than compensating by a stronger action on the other dimension to restore the overall level of network effects, the firm will actually scale back on the other initiative as well. Under incomplete information, this complementarity holds when seeding disutility is negatively correlated with customer type but may not always hold in the other disutility model, potentially leading to fundamentally different optimal strategies. We also discuss how our insights apply to asymmetric networks.

Key words: social commerce and social media; network effects; social interaction; seeding; adoption process; digital goods and services

History: David Godes, Senior Editor; Zsolt Katona, Associate Editor. This paper was received on January 15, 2012, and was with the authors 4 months for 2 revisions. Published online in Articles in Advance December 20, 2012.

## 1. Introduction

For many categories of products, it has been widely known in the industry and documented in a rich research literature that the existing network of users can impact in many ways the adoption process. First, it may induce word-of-mouth (WOM) effects, leading to faster or more efficient propagation of information about the product, helping consumers in the valuation learning process. Second, increased adoption within certain social groups, even in the absence of informative interpersonal communication, may lead to herding behavior, i.e., imitation effects, especially when the intended market exhibits homophilic tendencies. Third, if the product is susceptible to network effects at individual utility level, a larger network may boost the value of the product to each user and, implicitly, increase the willingness-to-pay (WTP) of potential adopters.

The rapid expansion of the Internet user base (with over 2.26 billion individuals connected according to Internet World Stats 2012) and the relatively recent advent of social media tools provided firms with unprecedented abilities to reach and capitalize on the network of users. Many businesses with an online storefront (e.g., Amazon, Apple App Store, Beach Camera, Best Buy, Newegg, Target, etc.) introduced features and channels to allow users to rate products. Similarly, many practices and businesses (from car dealers to medical doctors) are now rated online by customers. Two-sided platform providers (e.g., Airbnb, eBay, eLance) introduced feedback mechanisms through which participants can build reputation. Many providers of content creation and productivity software (e.g., Adobe, Google Docs, Microsoft Word, wikis) introduced collaboration tools that made these products or services more appealing to various users. Along the same lines, several cloud storage services (e.g., Dropbox, Mozy) allow users to share documents. Some companies also support online forums through which customers can interact with each other and start discussion threads about product-related topics (e.g., Dell, Amazon Web Services). Moreover, the value of social and professional networks (e.g., Facebook, LinkedIn, Salesforce Chatter); massive multiplayer online games (e.g., Blizzard’s World of Warcraft); video, voice, and text chatting tools (e.g., Google Talk, Skype, Yahoo Messenger); or blogging and microblogging tools (e.g., Twitter) is predicated on social interactions. Many other examples can be mentioned where social media features have facilitated growth in value or acceleration of information dissemination in association with products by enhancing the potential benefit of user interactions.

Most of the literature capturing the influence of consumer networks on the product adoption traditionally considers the manifestation, strength, and impact of such effects outside the influence reach of the firm (e.g., Bass 1969, Robinson and Lakhani 1975, Kalish 1983). In other words, although social interactions do occur and have been shown to influence consumer behavior, very few studies actually explored how the firms should manage and strategically influence these interactions (Godes et al. 2005). Recent studies began opening this path, focussing primarily on firms’ strategies and opportunities to engineer WOM effects. Biyalogorsky et al. (2001) study how consumer referral actions should be incentivized. Dellarocas (2006) inspects how strategic manipulation of online forums can shift the information value of online reviews for customers. Chen and Xie (2008) explore the firm’s benefit from establishing an online community where consumers can post reviews. Forman et al. (2008) empirically show that the prevalence of reviewer disclosure of identity information can be associated with an increase in consumer trust in the reviews, with impact on subsequent online product sales. Thus, firms might benefit from strategically creating online review platforms and incentive mechanisms that encourage reviewers to share more information. Godes and Mayzlin (2009) empirically study how firms should strategically recruit customers for WOM campaigns based on loyalty considerations to drive sales. Aral and Walker (2011) highlight the effectiveness of viral product features in generating social contagion. Aral et al. (2011) analyze the performance of seeding and referral incentive programs as two popular methods to engineer social contagion.

We extend this literature by considering how a monopolistic firm can strategically engineer the strength of network effects at utility level via social media. On this dimension, we focus on deriving the optimal level of social media functionality that increases the value of social interactions to each user. Such functionality includes features and environments that facilitate communication between users (e.g., chat capabilities, virtual reality environments where avatars can interact, screen sharing), collaboration on and cocreation of content (e.g., wikis, content editing, and tagging), peer endorsement or referral (e.g., on professional networks such as LinkedIn), building of reputation, etc. In a different context, Bakos and Katsamakas (2008) explore how an intermediary would optimally engineer the strength of cross-side network effects when designing a twosided Internet platform. In contrast, we consider a vendor that endogenizes the strength of direct (sameside) network effects experienced by the buyers in parallel with seeding the market, when there are synergies between the two actions, as will be further discussed in the paper.

Our study focuses on paid digital goods and services where the value is mostly induced by the network. Some examples include (but are not restricted to) massive multiplayer online games (e.g., World of Warcraft), social dating sites (e.g., eHarmony, Match.com), professional social networks (Salesforce’s Chatter Plus), and specialized online forums with paid memberships (e.g., Angie’s List, Naturescapes.net). We point out that our results go beyond digital goods and services, and apply to other products and services (e.g., voice communication services) where marginal costs are negligible and the bulk of value is derived from the network. When network effects strongly dominate stand-alone benefits from the product (i.e., benefits in the absence of the network), firms may find it profitable to spark adoption by giving away some consumption for free. In this paper, we focus on seeding strategies, whereby the firms give the products with full functionality and perpetual license to a few customers to boost the WTP of other customers and catalyze adoption (Lehmann and Esteban-Bravo 2006, Jiang and Sarkar 2009, Galeotti and Goyal 2009). Alternative strategies that are also employed in the industry to spark adoption involve freemium approaches (limited-time free trials or free versions with stripped-down functionality— Niculescu and Wu 2012).

In addition to potential demand cannibalization and boost in network effects, in the context of paid products, seeding may induce a separate effect on the paying customers. If some customers are charged for the product, then seeding implies price discrimination in the market: seeded customers pay less (zero) compared to unseeded individuals who end up buying the product. If seeding is extensive and paying customers observe it, then they might consider the price scheme unfair. Extant empirical studies illustrate that price discrimination could potentially lower customers’ WTP. Oliver and Shor (2003) show evidence of strong negative effects on fairness perception, satisfaction, and purchase completion among online shoppers that are prompted to enter a coupon code toward the conclusion of the checkout process for such customers that did not receive a code in advance. Novemsky and Schweitzer (2004) explore the role of internal social comparisons (between buyer and seller) and external social comparisons (between buyer and buyer) in negotiator satisfaction. They find that buyer’s satisfaction will be increased if other buyers have a smaller surplus. Xia et al. (2004) provide a literature review and conceptual framework to understand the fairness of pricing. When price comparisons are perceived as unfavorable for similar transactions, they predict that customers will have an adverse response to the seller’s strategy, which may involve negative emotions (such as anger or outrage), negative WOM, and reduced demand. According to Hinz et al. (2011), when price discrimination is observed, it is often the case that customers feel unhappy about the unfair pricing. Also, it is not uncommon in the industry for adopters to question pricing practices of the firms and exert pressure on them. For example, Amazon offered a public apology and refunds to over 6,000 customers in response to public backlash over a series of price tests through which different online shoppers were quoted different prices for various DVDs (?). In another example, after introducing the first generation iPhone in June 2007, within just three months Apple dropped the price by \$200 for the entire market. Faced with a flood of complaints from early adopters, Apple decided to refund each of them \$100 in the form of store credit (Wingfield 2007).

Building on prior literature and industry observations, in the context of digital goods and services with an associated price tag, we formalize the negative effects of seeding associated with price discrimination via a disutility incurred by paying customers. In our model, the more customers are seeded, the greater is the backlash and valuation downgrading from paying customers who question the fairness of the pricing scheme. To capture various potential market scenarios, we consider two contrasting seeding disutility models. Under the first seeding disutility model, SDU<sup>+</sup>, for each customer, the seeding-induced disutility is positively correlated with her type. Thus, the highest-type customers are experiencing the highest seeding-induced disutility. Under the second model, SDU<sup>−</sup>, every customer experiences a seeding disutility that is negatively correlated to her type. In this case, high-type customers do not experience much disutility because of seeding. Various examples justifying each setup are included in §2.

In this paper we explore the trade-off between benefits and costs associated with seeding and building social media features into the digital product. On one hand seeding boosts WTP of potential customers because it leads to larger user networks. On the other hand, seeding induces disutility for paying customers and, contingent on seed allocation, can cannibalize demand. Similarly, building social media features that boost the strength of network effects at the utility level (i.e., by allowing more value extraction from social interactions) would lead to increased WTP for the customers but involves building efforts. Taking these trade-offs into consideration, we seek to find out what are the optimal seeding, pricing, and social media strategies for the firm.

Depending on firm access to market information, we explore two scenarios: complete information on firm side (the firm knows enough about the customers such that it can perform targeted seeding) and incomplete information (the firm does not know much about the customers other than the consumer distribution and, thus, cannot resort to targeted seeding). First, under complete information, for each of the disutility models, we solve completely the market equilibrium, discuss market coverage, and investigate the interaction effects between seeding and building social media features. Under both disutility scenarios, we find that if the marginal cost/penalty associated with one of these initiatives increases, the firm will scale back (or sometimes leave unchanged) its efforts on the other dimension as well. This is interesting because, at the utility level, an upward change in each of these two dimensions would increase the impact of the network effects. However, if the investment required to build more social media features in the product is higher, while the firm scales back on such features, it will not try to compensate by seeding more. Similarly, if the seeding disutility rate is higher, while the firm scales back on seeding, it does not try to boost the strength of network effects.

Under incomplete information, while the firm decides strategically on the seeding volume, we assume the seeds end up being spread uniformly in the market. Under disutility model SDU<sup>−</sup>, complementarity between seeding and building social media features continues to hold. However, under SDU<sup>+</sup>, some new patterns emerge. When the seeding penalty is small, it may be actually possible for both levels of seeding and social media features to be increasing in the seeding penalty. When seeding penalty is intermediate, the two actions act as substitutes to each other with respect to changes in penalty rate. When the seeding penalty increases, the firm reduces seeding and builds at the same time stronger network effects. Once seeding disutility is large, we encounter the same complementarity effects as in all the other settings. Also, for small social media building costs, the actions act as substitutes to each other with respect to changes in social media costs. If it is more expensive to build social media features but not too expensive, the firm increases the seeding ratio and decreases the level of social media features. However, once the social media cost becomes large enough, the outcome reverts to the previously uncovered complementarity in actions.

We also explore how our frameworks and results extend to asymmetric networks where connections between users are active only in one direction. We show that some of the previous insights continue to remain robust, and we also inspect various seeding patterns induced by the network structure.

Our paper has important practical implications. First, in the industry, firms recognize the value of network effects and put a lot of effort into harnessing them. This paper and the framework and results within provide a host of practical and actionable insights into how to optimally use in tandem two levers (seeding and building social media features) aimed at boosting network effects taking into account how they can jointly impact the market outcome. In particular, in addition to development cost considerations, firms should also consider the magnitude and form of seeding disutility when deciding the optimal social media strategy. For example, as discussed above, higher seeding disutility may incentivize firms to scale back on the level of social media features embedded in their products. In parallel, we also suggest pricing strategies that effectively jumpstart and sustain adoption. Our analysis further indicates that barriers to entry are higher for firms in environments characterized by $S D U ^ { + }$ seeding disutility model. Another practical implication of our results is toward measuring the value of information. Unprecedented amounts of consumer data are collected in the market and many players are now engaging in big data analytics. Firms can choose to invest internally in such capabilities or procure such information from an increasing number of third-party providers who specialize in collecting, analyzing, and selling market information. By deriving the optimal strategies and profits under complete and incomplete information, this paper takes an important step toward measuring how much value firms should place on identifying customer characteristics. We further discuss the value of information in the conclusion.

The rest of the paper is structured as follows. In §2, we introduce our general modeling framework. In $\ S 3 ,$ we present the analysis of the complete information case. In §4, we extend our discussion to incomplete information settings. In §5, we extend our analysis to asymmetric networks and provide further discussions on robustness of our key findings. We conclude in §6. All proofs of our results can be found in the appendix.

## 2. General Model

Consider a software market with a monopolistic firm and a heterogeneous and stationary pool of potential customers with mass normalized to 1 and types  distributed uniformly in the interval 601 17. For simplicity, in the main part of the paper we focus on a symmetric, fully connected consumer network and assume the software exhibits heterogeneous network effects. We relax the symmetry assumption in §5. Thus, if the current installed base has size , then a customer of type  will get a direct benefit b from the software, where b captures the strength of network effects. Apart from the network-generated value, we assume the product carries negligible stand-alone value. Our model is consistent with setups in Dhebar and Oren (1985, 1986).

To boost paying customers’ product valuation, the software firm seeds a fraction  of the market. While the seeding process in itself jumpstarts adoption, it also generates disutility at the individual level for paying customers as discussed in the Introduction. For each paying customer , we model this disutility as a function $\Delta ( \alpha , \theta )$ that is nonnegative, convex and increasing in $\alpha ,$ and captures heterogeneity of this effect as experienced by each customer. The nonlinear dependence on the size of the seeded pool captures the fact that disutility is very limited for small seeded pools but rapidly increases as more customers are seeded.

In this paper, we consider a setup where customers progressively join the network toward a market equilibrium. Seeding occurs immediately before the product is released for sale. Customers do not know the overall type distribution in the market and act in a myopic fashion, making their adoption decision based on the perceived utility from the product computed using the current observed installed base. In general, in the software industry (and others), there are many cases where firms make public the information regarding installed base or such information is estimated and reported with regularity by market research firms.<sup>1</sup> Consistent with such observations, we assume in our model that customers have access to this information. If at a given moment the installed base is of size  (including seeded customers), then a paying customer of type  would momentarily perceive the utility from buying the product as

$$
u (\theta \mid \alpha , b, p, \delta) = b \delta \theta - \Delta (\alpha , \theta) - p.\tag{1}
$$

A customer of type  adopts as soon as she perceives $u ( \theta | \cdot ) \geq 0$ . This setup is consistent with Rohlfs (1974) and Dhebar and Oren (1985), among others.

The firm is proactive in managing the strength of network effects via choosing the right amount of social media features that boost the value of social interactions to each user. As such, we assume that the firm will incur a convex cost $c b ^ { 2 }$ to induce network effects at marginal strength $b ,$ with $c > 0 .$ . If we denote by $N ( \alpha , b , p )$ the mass of paying customers<sup>2</sup> at the conclusion of the adoption process (in equilibrium), then the firm’s optimization problem becomes

$$
\max _ {\alpha \in (0, 1), b > 0, p > 0} \pi (\alpha , b, p) = p N (\alpha , b, p) - c b ^ {2}.\tag{2}
$$

We consider all development efforts with the exception of the building of social media features sunk. This reflects a realistic scenario where the firm is reevaluating its strategy closer to market release when more accurate information is available.<sup>3</sup> Moreover, as we are focusing on digital goods and services, the reproduction costs are assumed negligible.

Although, as discussed in the Introduction, it has been documented that price discrimination can lead to a decrease in WTP because of perceived unfairness, there is very little research connecting this disutility to consumer characteristics. Related literature offers various insights as to how various customer groups react to negative firm actions (e.g., price increases or service failures). For example, under conditions of high price inequality, consumers that shop with higher frequency perceive price increases as less fair compared to customers that shop with lower frequency (Huppertz et al. 1978). A different study by Martin et al. (2009) takes a somewhat opposite stance by showing that loyal customers do not necessarily perceive major price increases less fair than nonloyal customers (and, in the case of small price increases, actually the opposite might occur). The same study proposes that, under conditions of a price increase, post customer loyalty is greater for previously loyal customers than nonloyal customers. Such findings are also consistent with Hess et al. (2003), whereby it is argued that more loyal customers invest in maintaining the relationship with the vendor and, thus, are more forgiving toward minor negative actions compared to nonloyal customers. However, some customers may come to expect certain relational benefits in exchange for their loyalty. For example, customer service quality expectations may be positively correlated to the longevity of the customer-firm relationship duration (Heilman et al. 2000).

Thus, the above literature suggests that disutility from firm’s actions may be different for distinct customer groups. However, in the absence of a clear consensus regarding how seeding-induced disutility is related to customer type (or WTP), for completeness of the analysis we choose to explore two opposing models to account for various market peculiarities. The seeding disutility functions under the two models are parameterized as follows:

$$
\text { model   } S D U ^ {+} \colon \Delta (\alpha , \theta) = s \alpha^ {2} \theta ,
$$

$$
\text { model   } S D U ^ {-}: \Delta (\alpha , \theta) = s \alpha^ {2} (1 - \theta),
$$

where $s \geq 0$ . Under model $S D U ^ { + }$ , for each customer, the seeding-induced disutility is positively correlated with her type. Thus, the highest-type customers are experiencing the highest seeding-induced disutility. Under model SDU<sup>−</sup>, every customer experiences a seeding disutility that is negatively correlated to her type. In this case, high-type customers do not experience much disutility because of seeding.

If adoption starts, then, at any subsequent moment, the instantaneous utility is increasing in type under both $S D U ^ { + }$ and $S D U ^ { - \frac { 7 } { 4 } }$ Consequently, our model is consistent with the extant literature on vertical differentiation in the sense that if a customer adopts, all higher-type customers must adopt as well. As such, customer type is positively correlated with instantaneous consumer WTP. If there are different types that perceive at a given time nonnegative utility from the product and they have not adopted yet, for simplicity we assume the higher-type moves first. In that sense, we assume that type (hence, utility) is positively correlated with the urgency to use the product for whatever mission-critical needs that customer has.

## 3. Complete Information

We first consider the case where the firm has complete information about customer types and, thus, can perform seeding targeted toward specific individual types. For example, such scenarios may correspond to markets where consumers leave a considerable and relevant informational footprint after (online) activities, which is made available to the vendor. Such information may be collected perhaps in association with the consumption of a related product/service offered by the same vendor or by a partner of the vendor. In other cases, users have to satisfy certain conditions to qualify for the free offer, and they must reveal this information to the provider prior to receiving the product. For example, through its Dreamspark global initiative, Microsoft is making developer grade software available for free to students in many countries around the world (Microsoft 2008). To qualify, students have to prove their affiliation with an academic institution (which, in the United States, can be done by providing a .edu email address). In another example, in 2009, in a \$15 million initiative, Autodesk seeded 100 early-stage clean tech companies with free software bundles each worth approximately \$150,000 (Autodesk 2009). In these examples, Microsoft and Autodesk managed to target a particular segment of the market with their free offer.

3.1. Optimal Strategy Under Model SDU<sup>+</sup> We start by exploring necessary conditions for optimality:

Lemma 1. <sub>Under</sub> $S D U ^ { + }$ and complete information, if the firm stays in the market $( i . e .$ , it can make profit) then its optimal strategy $\{ \alpha ^ { * } , b ^ { * } , p ^ { * } \}$ and optimal seed allocation must satisfy the following:

(i) b<sup>∗</sup><sup>∗</sup> $\begin{array} { r } { \alpha ^ { \ast } - s \alpha ^ { \ast 2 } \geq p ^ { \ast } ; } \end{array}$

(ii) all customers with types $\theta \in [ 0 , \alpha ^ { * } )$ are seeded;

(iii) all customers with types $\theta \in [ \alpha ^ { * } , 1 ]$ purchase the product.

Part (i) of Lemma 1 states that seeding cannot be effective at sparking adoption unless it is coupled with strong enough network effects. In other words, the optimal strategy has to be chosen in such a way that at least the highest-type customers want to adopt at the very beginning. Parts (ii) and (iii) basically capture the fact that, under optimal seed allocation, there is no segment of the market left without a product. Although it seems more or less intuitive that seeds should go to the low-type customers to prevent sales cannibalization, what is interesting is that, under the optimal strategy, if any unseeded customer purchases the product, then all unseeded customers purchase the product. Seeding more induces two opposing effects at the instantaneous utility level: it increases the network benefits and it also increases the seeding disutility. Nevertheless, the firm will choose to manipulate the three controls (seeding, level of social media features, and pricing) in such a way as to seed right up to the lowest-type paying customers. Paid adoption occurs in decreasing order of types for customers with type $\theta \in \left[ \alpha , 1 \right]$ . The following result characterizes the optimal strategy of the firm.

Proposition 1. <sub>Under</sub> $S D U ^ { + }$ and complete information, $i f c s \geq 1 / 4 ,$ , then the firm exits the market. Otherwise, $i f c s < 1 / 4 ,$ , then the firm enters the market and its optimal strategy $\{ \alpha ^ { * } , b ^ { * } , p ^ { * } \}$ is given by

$$
\alpha^ {*} = \frac {3 (1 - 2 c s) - \sqrt {1 - 4 c s + 3 6 c ^ {2} s ^ {2}}}{4} \leq \frac {1}{2},
$$

$$
b ^ {*} = \frac {\alpha^ {*} (1 - \alpha^ {*})}{2 c}, p ^ {*} = b ^ {*} \alpha^ {*} - s \alpha^ {* 2}.
$$

As it turns out, the individual rationality (IR) constraint at adoption time is binding for the highest type. Thus, under an optimal strategy, the firm will choose a price such that seeding just jumpstarts adoption and this minimal push is enough for the adoption to gain momentum and not stall until every unseeded consumer purchases the product.

We emphasize that this equilibrium strategy is not dependant on adoption sequence. Suppose customers exhibit various degrees of inertia in reacting to market changes (such as installed base growth), but they all eventually react to such changes. First, for any given seeding ratio, pricing such that IR constraint is binding for the highest-type customers represents the highest price the firm can charge such that adoption can start (once the highest-type customers decide to make a move). Once adoption starts, if it evolves in decreasing order of types, it can be shown that IR constraint at adoption time will not be binding for any of the other paying customers except for the highest-type paying customers. Even if adoption does not occur in decreasing sequence of types, as long as it does not stall, we reach the same full market coverage and, thus, an identical optimal strategy. Otherwise, if at any moment adoption stalls momentarily (perhaps because of some higher-type customers being slow in reacting to market evolution compared to lower type customers), it will pick up eventually as there will always be some unseeded type for whom adoption yields nonnegative utility. As such, full market coverage is reached again. In such cases, pricing lower such that IR constraint is not binding for the highest type is suboptimal. Thus, the strategy derived in Proposition 1 remains optimal even under different adoption sequences.

Next, we focus our attention on the interaction between building more social media features to increase the strength of network effects and seeding the market. Technically each of these actions on the firm’s behalf is aimed at boosting WTP but they both come at a cost. So a natural question arises: are these actions complementary or in substitution of each other? In other words, if the cost/penalty associated with being more proactive on one of these two dimensions increases, would the firm increase or decrease its activity on the other dimension? The following result addresses this question:

Proposition 2. <sub>Under</sub> $S D U ^ { + }$ and complete information, when the firm stays in the market $( c s < 1 / 4 )$ , seeding and embedding more social media features are complementary actions. If any of the costs associated with these actions 4s or c5 increases, the firm scales back on both dimensions $( i . e . , \ \partial \alpha ^ { * } / \partial s \le 0 , \ \partial \alpha ^ { * } / \partial c \le 0 , \ \partial b ^ { * } / \partial s \le 0 , \ \partial b ^ { * } / \partial c \le 0 )$

The fact that the firm scales back on a particular action if the associated cost/penalty with that respective action increases $( \mathrm { i . e . , ~ } \ \hat { \partial \alpha } ^ { * } / \partial s \ \overset { \cdot } { \leq } 0 , \ \partial b ^ { * } / \partial c \leq \hat { 0 } )$ is to be expected. However, the interesting results in Proposition 2 characterize the interaction between the two actions. At first glance, one might expect that as the cost of boosting the strength of network effects via more sophisticated social media features increases, the firm might turn to the other lever it has access to, seeding, in order to increase WTP (and vice versa). However, seeding is valuable to the firm as long as it does not cannibalize too much demand and does not induce paying customers to downgrade their valuation of the product too much. When it is more costly to generate strong marginal network effects via social media, the firm reduces its investment along that dimension. In turn, if it were to compensate such an action by a boost in seeding, to reach the same overall level of network effects the firm would have to seed more customers. Thus, for similar network effects, the firm would actually see both an increase in seeding penalty and, because of full market coverage, a decrease in the number of paying customers. As it turns out, these two effects dominate the benefits from the boost in overall network benefits from seeding, and, consequently, the firm prefers to downsize the seeding pool as well.

A similar argument goes in the other direction. If the seeding-induced downgrading of WTP of paying customers is more intense, then the firm first scales back on seeding. Again, at first glance, it might seem like a good idea in such a case to simultaneously boost the strength of network effects so that the firm does not have to rely on seeding that much. Nevertheless, once operating at optimal network effect strength levels, it is costly to further upgrade $b ,$ and this cost is not recovered by the benefit of an upward shift in WTP because of stronger network effects.

When seeding does not induce any disutility for the paying customers $( s = 0 ) .$ , then $\alpha ^ { * } \doteq 1 / 2 , \ b ^ { * } \doteq 1 / ( 8 c )$ and $p ^ { * } = 1 / ( 1 6 c )$ . In such cases, the optimal seeding ratio and, implicitly, the ratio of paying customers are independent from the strength of network effects embedded in the product. If the cost of adding social media features is increasing, the firm settles for a lower strength of network effects and, at the same time, charges customers less such that IR constraint remains binding for the highest type while the seeding ratio is kept unaltered.

As seen from Proposition 1, the upper bound for $\alpha ^ { * }$ is $1 / 2$ . Thus, under the optimal strategy, the software firm prefers an outcome where the majority of customers are paying customers whose WTP is influenced by a well-balanced combination of seeding and social media features that boost network effects.

Last, we mention that the results in this section can be extended to more general type distribution functions and utility structures. This discussion has been included in Appendix B.

## 3.2. Optimal Strategy Under Model SDU<sup>−</sup>

In this section, we explore a setting where customer type is negatively correlated with seeding-induced disutility. As argued in $\ S 2 ,$ , in some instances, more loyal customers may perceive less disutility because of seeding procedures compared to less loyal customers. It may be the case that more loyal customers also have higher WTP. Customers with higher WTP may be big clients such as corporations who developed a relationship with the vendor over time and for whom switching costs would be too high. Such clients might be less likely to fret much over some other customers receiving the product for free. At the other end of the type spectrum, customers who do not derive much value from the product and might operate on a tight budget might be more upset if others got it for free. The following lemma characterizes the market segmentation under the vendor’s optimal strategy.

<sup>Lemma</sup> <sup>2.</sup> Under SDU<sup>−</sup> and complete information, if the firm stays in the market $( i . e . ,$ it can make profit) then its optimal strategy $\{ \alpha ^ { * } , b ^ { * } , p ^ { * } \}$ and optimal seed allocation must satisfy the following:

(i) $b ^ { * } \alpha ^ { * } \geq p ^ { * } ;$

(ii) there exists a marginal type $\theta _ { m } > \alpha ^ { * }$ such that all customers with type $\theta \in \left[ \theta _ { m } , 1 \right]$ purchase the product, no customers of type $\theta < \theta _ { m }$ purchase the product, and all seeds come from the interval $[ 0 , \theta _ { m } )$ (though they may not need to be grouped at the very low end).

Condition (i) illustrates the fact that adoption has to start with the highest-type customers. Condition (ii) states that, similar to the $S D U ^ { + }$ case, paid adoption occurs among the top-tier customers. Nevertheless, unlike in the case of SDU<sup>+</sup>, full market coverage may not be optimal. We will revisit this point later. Firm’s optimal strategy is presented below.

<sup>Proposition</sup> <sup>3.</sup> Under SDU<sup>−</sup> and complete information, the firm always enters the market. Let $\theta _ { m } ^ { * }$ be the lowest type among paying customers under optimality. Then firm’s optimal strategy is as follows:

Region 1: $0 \leq c s \leq 1 / 8$ . Then

$$
\alpha^ {*} = \frac {1}{2}, \quad b ^ {*} = \frac {1}{8 c}, \quad \theta_ {m} ^ {*} = \frac {1}{2};
$$

Region 2: $1 / 8 < c s < ( 3 1 - 7 \sqrt { 1 7 } ) / 1 6$ . Then

$$
\alpha^ {*} = 3 \theta_ {m} ^ {*} - 1, b ^ {*} = \frac {(1 - \theta_ {m} ^ {*}) \theta_ {m} ^ {* 2}}{c}, \theta_ {m} ^ {*} = \tilde {x},
$$

where x˜ is defined as the unique real solution to the equation $c s ( 2 - 6 x ) + x ^ { 3 } = 0$ over the interval $[ - 1 +$ ${ \sqrt { 1 + 8 c s } } , { \sqrt { 2 c s } } | ;$

$$
R e g i o n 3: (3 1 - 7 \sqrt {1 7}) / 1 6 \leq c s. T h e n
$$

$$
\alpha^ {*} = 3 \theta_ {m} ^ {*} - 1,
$$

$$
\begin{array}{c} b ^ {*} = \frac {1 - 2 4 c s - 3 6 c ^ {2} s ^ {2} + (1 + 6 c s) \sqrt {1 + 3 6 c s + 3 6 c ^ {2} s ^ {2}}}{1 6 c}, \\ \theta_ {m} ^ {*} = \frac {- b ^ {*} + 3 s + \sqrt {b ^ {*} (b ^ {*} + 3 s)}}{9 s}. \end{array}
$$

Under all regions, $p ^ { * } = b ^ { * } ( 1 - \theta _ { m } ^ { * } + \alpha ^ { * } ) \theta _ { m } ^ { * } - s { \alpha ^ { * } } ^ { 2 } ( 1 - \theta _ { m } ^ { * } )$

One immediate difference from $S D U ^ { + }$ is that, under $S D U ^ { - }$ , the firm will always prefer to enter the market. That is because the highest-type customers experience very small seeding disutility and thus their WTP is more or less dictated by network-generated value. If c is very high, low b can induce positive WTP at top tier, which, coupled with low (but not too low) prices would induce revenues that would dominate associated social media costs.

Another difference from $S D U ^ { + }$ is that, under $S D U ^ { - }$ the IR constraint at adoption time is binding for the marginal-type paying customers rather than the highest paying customers. Thus, at the very beginning, many customers may be willing to adopt solely based on the network value generated by the seeds. One of the reasons leading to this outcome is the fact that seeding disutility is low for top-tier customers under model SDU<sup>−</sup>.

One interesting aspect of the optimal strategy under SDU<sup>−</sup> is that, when seeding penalties and costs associated with social media features are relatively low $( c s \leq 1 / 8 ) _ { \cdot }$ , then the firm responds to the disutility solely through adjusting the price downward by the biggest seeding disutility a paying customer can experience (i.e., the one experienced by the lowest paying type $\theta _ { m } )$ . Its seeding and social media engineering strategies do not change under small fluctuations in seeding penalty. Also, in such regions, seeding is not influenced by changes in the cost of adding more social media features. However, in markets characterized by higher costs $( c s > 1 / 8 )$ , the optimal seeding and social media engineering strategies will depend on both s and c. As it turns out, differently from $S D U ^ { + }$ , under $S D U ^ { - }$ , full market coverage does not always hold. The following corollary to Proposition 3 captures this:

<sup>Corollary</sup> <sup>1.</sup> Under SDU<sup>−</sup> and complete information, full market coverage $( \alpha ^ { * } = \theta _ { m } ^ { * } )$ is attained only when $c s \leq 1 / 8$ . When $c s > 1 / 8$ , then $\alpha ^ { \ast } < \theta _ { m } ^ { \ast } ,$ and there are always customers that are not purchasing the product and are not seeded.

When the costs associated with seeding and/or building more social media features into the product are relatively high, it is not optimal to seed more or lower the price to a level where all unseeded customers adopt. Unseeded customers of low type actually have high disutility from seeding so their WTP would be rather low. The firm is better off keeping the price higher and extracting more consumer surplus from the high tier. Seeding the aforementioned unseeded customers would also generate a decrease in WTP for customers in the mid-type range (where there is significant seeding disutility) that would shrink or completely eliminate any benefits from the increased WTP at the high end (where there is little seeding disutility).

In regions 2 and $^ { 3 , }$ as $\alpha ^ { * } < \theta _ { m } ^ { * }$ and $\alpha ^ { * } = 3 \theta _ { m } ^ { * } - 1$ , it follows immediately that $\alpha ^ { * } < 1 / 2$ . Thus, again, it is never optimal to seed more than half of the market.

In spite of the differences in both model and optimal strategy, we find that the complementarity result between seeding and building social media features for model $S D U ^ { + }$ (Proposition 2) extends to $S D U ^ { - }$

<sup>Proposition</sup> <sup>4.</sup> Under SDU<sup>−</sup> and complete information, optimal seeding ratio $\alpha ^ { * }$ and optimal strength of network effects $b ^ { * }$ are both nonincreasing in c and s.

For region 1, b<sup>∗</sup> is independent of s and $\alpha ^ { * }$ is independent of both c and s. Strict monotonicity is experienced in regions 2 and 3. As discussed above, under $S D U ^ { - }$ , under optimality, IR constraint is binding for the lowest paying type because highest types have negligible seeding disutility. If adding more social media features becomes costlier, the firm will reduce its investment in social media and thus, decrease the marginal network-generated value of the product. This, in turn, would lower WTP for all customers. If the firm would respond by increasing seeding to boost network effects, actually the WTP of the low end of the paying group would decrease a lot and that dictates price. Thus, the firm would see either a smaller paying segment or would have to charge a lower price, and those actions would lead to a lower profit. As a result, it is better for the firm to decrease seeding as well. Alternatively, if s increases, the low end gets affected most. To compensate for that decrease, the firm would have to invest a lot in social media features. Granted that at the top tier this increases WTP for the customers, however, in regions 2 and 3, where c was also relatively high, associated social media costs would increase steeply for such a process and wipe out other benefits. Therefore, the firm finds it more profitable to actually decrease social media features and manipulate demand more through price.

## 4. Incomplete Information

When the firm has incomplete market information, i.e., it knows the type distribution but not the exact type of each customer, it may not be able to target individual customers by type. In this scenario, when a firm attempts to seed the market, one of the inherent downsides is the potential to cannibalize some of the demand from high-type customers because the firm cannot ensure that the seeds go to the lowest end (Niculescu and Wu 2012). For example, in the app markets for iOS and Android devices, it is not uncommon for some of the developers to offer their apps for free for a limited period of time to boost adoption in the market. In such cases, any customer who comes across the app during this limited time window can download it for free. We consider the case where the firm decides strategically on the seeding volume but the seeds end up being spread uniformly in the market. We again explore both models $S D \bar { U } ^ { + }$ and $S D U ^ { - }$ for a complete picture of how the firm adjusts seeding and the level of social media features in products in response to fluctuations in costs depending on market specifics.

Before we discuss each model, we would like to point out some other differences between uniform seeding and seeding under complete information. Under complete information, we saw in §3 that full market coverage always occurs under $S D U ^ { + }$ and it may occur also for SDU<sup>−</sup> contingent on small costs. However, under uniform seeding, full market coverage never occurs, regardless of the seeding disutility model. This is because for any positive price, there will always be unseeded customers with low types for whom benefits fall below that price. Moreover, for both seeding disutility models, the IR constraint at the adoption time is binding for the lowest-type paying customers. This is not the case under complete information for SDU<sup>+</sup>.

## 4.1. Uniform Seeding Under Model SDU<sup>+</sup> In this case, firm’s optimal solution is as follows:

Proposition 5. <sub>Under</sub> $S D U ^ { + }$ and uniform seeding, when the firm decides to enter the market, its optimal strategy $\{ \alpha ^ { * } , b ^ { * } , p ^ { * } \}$ is given by

$$
\begin{array}{r} \alpha^ {*} = z (b ^ {*}) \in \left[ 0, \frac {2 (5 - 2 \sqrt {2})}{1 7} \right], \\ b ^ {*} = \underset {b \geq 0} {\arg \max} \bigg \{b (1 - 2 z (b)) z (b) - \frac {s ^ {2} z (b) ^ {4}}{b} \\ - s z (b) ^ {2} (1 - 3 z (b)) - c b ^ {2} \bigg \}, \end{array}
$$

$$
p ^ {*} = \alpha^ {*} (b ^ {*} - s \alpha^ {*}),
$$

where $z ( b )$ is defined as the unique solution to the equation $b ^ { 2 } ( 1 - \dot { 4 } z ) - 4 \dot { s } ^ { 2 } z ^ { 3 } + b s z ( - 2 + 9 z ) = 0$ over the interval $[ 0 , ( 2 ( 5 - 2 \sqrt { 2 } ) ) / 1 7 ]$ . The marginal paying type is $\theta _ { m } ^ { * } =$ $( \alpha ^ { * } ( b ^ { * } - s \alpha ^ { * } ) ) / ( b ^ { * } ( 1 - \alpha ^ { * } ) )$ . Also, b<sup>∗</sup> exists and is unique. Moreover, there exists a bound $\xi \le 1 / 4$ such that when $c s > \xi$ then the firm does not enter the market.

First, we observe that the upper bound on seeding has decreased dramatically $( ( \hat { 2 } ( \bar { 5 } - 2 \sqrt { 2 } ) ) / 1 7 \approx 0 . 2 5 5 5 )$ compared to the complete information case $( 1 / 2 )$ The fact that uniform seeding effectively reduces the available market at the high end deters the firms from pursuing overly aggressive seeding campaigns. Revisiting the app market example, this observation is consistent with the practice to limit the free promotion to a short window to avoid excessive seeding. Moreover, profit under complete information seeding dominates profit under uniform seeding. Thus, when the firm would not enter the market under the former case, it will also not do so under the latter. When $s = 0 ,$ the optimal strategy is given by $\alpha ^ { * } = 1 / 4 , b ^ { * } = 1 / ( 1 6 c )$ and $p ^ { * } = 1 / ( 6 4 c )$ .

Given the complexity of the solution, we perform a numerical sensitivity analysis on the optimal seeding ratio $\alpha ^ { * }$ and level of social media features $b ^ { * }$ with respect to their associated costs. This analysis yields very interesting and, in certain regions, different results, compared to the ones under complete information. We capture these results in Figure 1, where panels $( \mathsf { a } ) \mathsf { - } ( \mathsf { c } )$ illustrate how $\alpha ^ { * }$ and $b ^ { * }$ change with respect to s, and panels (d)–(f) explore sensitivity with respect to c. We see that the complementarity results now hold only when costs are sufficiently large (cs high enough). In such a case, similar insights compared to the ones in §3.1 apply and we omit this discussion for brevity. When c is small, we can see that it is optimal to build a high level of social media features in the product, but such a practice would not be optimal for high c. Thus, similar to the complete information case and quite intuitive in nature, $b ^ { * }$ will tend to decrease in c.

However, this is where similarities stop. First, under small cs we notice that $\alpha ^ { * }$ is increasing in both c and s. Moreover, $b ^ { * }$ tends to also increase in s when s is small. To get a better understanding of the sensitivity with respect to s, we illustrate in Figure 2 several properties of the equilibrium outcome corresponding to panel (a) in Figure 1. Note that under complete information we have full market coverage and an increase in $\alpha ^ { * }$ would always result in a shrinking of the size of the paying group. When new seeds are given away, all of them are actually cannibalizing paying customers. However, as it turns out, under uniform seeding, because we do not have full market coverage (because of unseeded low types not adopting), new seeds only cannibalize a fraction of the paying customers as they get distributed uniformly. Thus, the firm can actually increase at the same time both the seeding ratio $\alpha ^ { * }$ and the size of the paying group $( 1 - \alpha ^ { * } ) ( 1 - \theta _ { m } ^ { * } )$ , as can be seen from panels (a) and (d) of Figure 2. Given that increasing seeding involves more seeds to the high types as well, the high-type paying group shrinks. However, the firm responds by lowering price and expanding adoption toward the lower end of the market, as can be seen from panels (b) and (c). When s is small, increasing seeding comes at a low penalty and thus, it results mostly in increased WTP. Additional increase in b also further adds to the increase in WTP. In such a case, the newly added revenue from the low end of the market (because of lower price and higher WTP, both of which induce more customers to join) may actually cut the double losses at the high end (because of fewer unseeded customers and lower price).

Figure 1 Optimal <sup>∗</sup> and b<sup>∗</sup> Under Uniform Seeding and Seeding Disutility Model SDU<sup>+</sup>  
![](/api/attachments/G3RW422Q/fulltext/images/03c8ec937d44c88790b3fe61283fd27182a80dd2dbfce39f7c0bb31a4647b53b.jpg)  
Notes. The yy -plots have $b ^ { * }$ on the left-hand y -axis and $\alpha ^ { * }$ on the right-hand y -axis. Panels (a)–(c) consider sensitivity with respect to s, whereas panels (d)–(e) consider sensitivity with respect to c.

As s increases, for intermediate ranges we see that the firm will switch toward using social media engineering as a substitute for seeding. Once s is not too small, the benefits from extra seeding vanish as the WTP cannot be boosted that high without substantial investments in boosting b because of the increasing disutility. This effect, together with the reduced pool of paying high-type customers, make increasing the seeding ratio suboptimal. In such a region, in parallel with a decrease in $\alpha ^ { * }$ we see an increase in b<sup>∗</sup>. The firm finds it optimal to continue to expand the market into lower types by decreasing price, thus absorbing the increase in the seeding disutility. At the same time, the decrease in $\alpha ^ { * }$ also expands the group of high-type paying customers. When the seeding disutility is not too high, the firm will still keep $\alpha ^ { * }$ at relatively high levels, adjusting upward $b ^ { * }$ in parallel with the decrease in $\alpha ^ { * }$ to reverse a decrease in network value. In this case, maintaining $b ^ { * }$ at high levels is also worth it given that increase in WTP of high types. Nevertheless, once s becomes too high, it is too costly for the firm to use this approach because it would be necessary to invest a lot in $b ^ { * }$ to maintain WTP at high levels. Thus, in such regions, the firm will resort to decreasing all three controls $\{ \alpha ^ { * } , b ^ { * } , p ^ { * } \}$

Figure 2 Details of Equilibrium When c = 003 Under Uniform Seeding and Model SDU<sup>+</sup>  
![](/api/attachments/G3RW422Q/fulltext/images/cb481dcb3a60c96e61865ace628e09440d6815d121d6c44ad9d700122728eeb4.jpg)

![](/api/attachments/G3RW422Q/fulltext/images/0da11b33e985f01da47ab952bd45e9eb7cdb153a6a3f65ff04d6e9cce538fef4.jpg)

![](/api/attachments/G3RW422Q/fulltext/images/582b6daeb5492864be3adcc2800b08a4d866581bae9ba49138e0fdb98596e393.jpg)

![](/api/attachments/G3RW422Q/fulltext/images/e136caf164e5d3c08456965bf288a26233c64dd6013b98af929c7d8281ec107c.jpg)

For $c ,$ we see in panels (d)–(f) of Figure 1 that under small values, seeding ratio is increasing in $c ,$ which, again, indicates that seeding and social media engineering are substitutes to each other in generating profit. An increase in c will induce a decrease in the level of social media features embedded in the product. Similar evolutions of $p ^ { * } , \theta _ { m } ^ { * } ,$ , and $( 1 - \alpha ^ { * } ) ( 1 - \theta _ { m } ^ { * } )$ with respect to $c$ are observed as in the case of changes in s (plots are omitted for brevity). For small ranges of $c ,$ even if $b ^ { * }$ decreases, it remains moderate in value, providing the potential for a substantial network value if installed base is robust. Small upward adjustments in seeding ratio might be profitable as they help retain network value and allow the firm to profitably expand in the lower type segment of the market by lowering the price. However, the boost in seeding is taken advantage of exactly through network effects and, thus, once c gets really high, the firm would not find it optimal to further invest in $b ^ { * }$ which, in turn, would expose customers to a potentially high seeding disutility without high benefits from the network. To compensate for this, the firm will reduce the seeding ratio, thus increasing the number of paying customers among the higher types and also reducing the disutility at all levels. The associated price decrease also allows the firm to strategically extend the group of paying customers toward more of the lower-type customers.

## 4.2. Uniform Seeding Under Model SDU

Under uniform seeding and model SDU<sup>−</sup>, firm’s optimal strategy is as follows:

<sup>Proposition</sup> <sup>6.</sup> Under SDU<sup>−</sup> and uniform seeding, the firm always enters the market and its optimal strategy $\{ \alpha ^ { * } , b ^ { * } , p ^ { * } \}$ is given by

$$
\alpha^ {*} = \left\{ \begin{array}{l l} \frac {- 2 b ^ {*} + \sqrt {4 b ^ {* 2} + 3 b ^ {*} s}}{3 s} \in \left[ 0, \frac {5 - \sqrt {5}}{1 0} \right], & s > 0 \\ \frac {1}{4}, & s = 0 \end{array} \right.
$$

$$
\begin{array}{c} {b ^ {*} = \frac {1 - 1 2 c s - 9 c ^ {2} s ^ {2} + (1 + 3 c s) \sqrt {1 + 1 8 c s + 9 c ^ {2} s ^ {2}}}{3 2 c},} \\ {p ^ {*} = \frac {2 b ^ {*} + b ^ {*} \alpha^ {*} - 6 s \alpha^ {* 2}}{9}.} \end{array}
$$

The marginal paying type is $\theta _ { m } ^ { * } = 1 / 3$

Under SDU<sup>−</sup> and uniform seeding, the marginal paying type is always the same $( \theta _ { m } ^ { * } = 1 / 3 )$ , in contrast with most of the cases previously studied, with the exception of the low-cost region 1 under SDU<sup>−</sup> and complete information. Even compared to the latter, there is one important difference, namely, that in the current case, while $\theta _ { m } ^ { * }$ is constant, the firm adjusts all its controls $\alpha ^ { * } , b ^ { * } , p ^ { * }$ in response to fluctuations in $c$ and s. Moreover, when $s > 0$ , as $\alpha ^ { * }$ can be rewritten as $\alpha ^ { * } = ( 1 / 3 ) ( ( - 2 b ^ { * } ) / { s } + \sqrt { ( b ^ { * } / s ) ( b ^ { * } / { s } + 3 ) } )$ , given that $b ^ { * } / s$ is a function of $c s ,$ it follows that $\alpha ^ { * }$ is a function of $c s ,$ and opposite-direction cost fluctuations that leave cs unchanged also leave the seeding ratio unchanged. Moreover, we note that, compared to the full information case, the upper bound on the seeding ratio also decreases significantly from $1 / 2$ to $( 5 - \sqrt { 5 } ) / 1 0 \approx 0 . 2 7 6 4$ . Similar to the discussion in §4.1, given that seeding strategies reduce the top-tier paying group under uniform seeding, the firms will not engage in overly subsidizing adoption.

We next explore the sensitivity of $\alpha ^ { * }$ and $b ^ { * }$ with respect to costs. An increase in s would result in a decrease in WTP pronounced more significantly at lower type levels. As such, unlike under $S D U ^ { + }$ , the firm does not see it beneficial to expand into the lower market by inducing lower $\theta _ { m } ^ { * }$ and more paid adoption. In turn, it shifts toward increasing the paying group toward the top tier by lowering $\alpha ^ { * } .$ . In tandem, it also lowers $b ^ { * }$ as there is less pressure to induce strong network effects to compensate for seeding disutility and this allows the firm to ease down on costs of building a high level of social media features into the product. On the other hand, when c increases, given convexity of social media costs, insights remain robust behind $\bar { b } ^ { * }$ being decreasing. Once the networkinduced value decreases for all types, if the firm would try to compensate with an increase in seeding, it will induce a higher disutility and reduce the number of paying customers at the top tier. The firm would then have to operate at suboptimal price levels to sustain a robust adoption. As such, the firm also prefers to reduce the seeding ratio, preventing a strong drop in WTP and, at the same time, increasing the size of the paying group. Thus, the complementarity results uncovered under full information continue to hold. The above insights are formalized in the next result.

Proposition 7. <sub>Under</sub> $S D U ^ { - }$ and uniform seeding, optimal seeding ratio $\alpha ^ { * }$ and optimal strength of network effects $b ^ { * }$ are both nonincreasing in c and s.

Unlike in the case of complete information, the two seeding disutility models may lead to optimal strategies that are different not only in specific value but in more fundamental ways. As such, when there is seeding disutility in the market, it is very important for firms to account for its proper form when detailed consumer information is lacking. Returning to the iOS example at the beginning of $\ S 4 ,$ app developers can use such insights to better time the length of the promotional campaigns $( \mathrm { i . e . , }$ , control the size of the seeded pool of customers) contingent on market characteristics.

## 5. Extension: Asymmetric Networks

In this section, we present an illustration of how our results can be extended to asymmetric networks. Among others, network asymmetry may be induced by lack of full connectivity (e.g., Zubcsek and Sarvary 2011) and/or by single-direction links (e.g., Lehmann and Esteban-Bravo 2006). As such, there are a vast number of possible asymmetric network scenarios. We will explore one case that pertains to the latter category.

Suppose the market has two disjoint consumer segments: low-value segment L $( \theta \ \in [ 0 , r ] )$ and highvalue segment H $( \overrightharpoon { \theta } \in ( r , 1 ] )$ . Suppose the network is fully connected but asymmetric in nature. Within each segment, all links are bidirectional. Across segments, links are unidirectional, going from highvalue segment to low-value segment, but not vice versa. In a sense, the high-value and low-value segments correspond to the innovators and imitators in Lehmann and Esteban-Bravo (2006). We assume that the network-induced value for each customer is given by the volume of incoming links. For each segment, the seeding ratio is always upper bounded by the size of the segment.

In this extension, we focus on SDU<sup>+</sup> seeding disutility model.<sup>5</sup> We further assume that seeding disutility is only manifesting within the high valuation segment (and only with respect to seeds in that segment), whereas in the low-value segment it is negligible $( s _ { L } = 0 , ~ s _ { H } = s > 0 )$ ). Of course, this is just one example of how seeding disutility can manifest in the market. We consider the case of full information. Although the market is segmented, we still assume that the seller only approaches it with a unique price. Seller’s optimization problem consists of how to choose $p ^ { * } , b ^ { * }$ , and seeding levels $\{ \alpha _ { L } ^ { * } , \alpha _ { H } ^ { * } \}$ corresponding to each segment.

It is straightforward to establish the following properties in equilibrium under optimal strategy. First, all seeds should go to the lowest end in each segment. Second, both segments will be fully covered. Let us focus on the high-end segment first. If the segment H is not completely seeded (that might be an option), and price is low enough such that paid adoption can start in that segment, given that segment H can be treated in isolation (it is not influenced by segment L), similar to our previous results it turns out that adoption goes all the way until the high segment is covered without stalling. It is irrelevant if at some point along the process adoption also started at the low level. Note that if there is any paid adoption in segment H, the highest-type customers must always be willing to adopt from the start. It cannot be optimal for some customers to be left without seeds in the high-end segment and the price be set above the WTP of the highest type. This is because lowsegment adoption cannot increase WTP at the high end (because of unidirectional links) and thus, those unseeded customers in segment H will never buy. However, seeding them would increase WTP in the low-end segment even further (because segment L does not exhibit seeding disutility). As such, in optimality, either the entire segment H is seeded or all unseeded customers purchase the product.

Next, in terms of equilibrium, we point out that it is irrelevant whether paid adoption starts in segment L before being complete in segment H . If it starts after, basically the WTP of the first adopters in segment L will be higher. Nevertheless, if it starts before, if at any point there is any stalling in segment L, adoption will pick up again once adoption from above picks up. As such, any equilibrium outcome where paid adoption in the low segment is starting before paid adoption is complete in the high segment can be replicated under a strategy where the low-segment market is opened after high-segment market is fully covered. If it is optimal to set the price very high such that there is no adoption in the low-value segment, then it is irrelevant whether customers are seeded in that segment or not because of asymmetry. As such, for simplicity, we can assume in these settings full seeding of the low-value segment. However, if it is optimal to have paid adoption in the low-end segment as well, then, once adoption starts, it can again be shown that it will not stall until everyone is covered (because of the concavity of the instantaneous WTP, via a similar argument as in the case of symmetric networks).

Under optimality, it can be easily shown that when r is close to one, it is optimal to seed the entire high-end segment, and when r is close to zero, it is optimal to price in such a way that there will be no paid adoption anyways in the low-end segment. When r is in an intermediate range, it is optimal to seed a fraction of each segment and have paid adoption in each segment as well.

We focus the remaining part of our discussion on the interesting regions for $r , c ,$ and s, where it is optimal to have paid adoption in both segments. Figures 3 and 4 illustrate sensitivity of $\alpha _ { L } ^ { * } , \alpha _ { H } ^ { * } , \alpha _ { L } ^ { * } + \alpha _ { H } ^ { * } ,$ and $b ^ { * }$ with respect to cost parameters s and c. In the plots, parameter r is chosen at 004 and we consider $c , s \in$ 60011 0047, ranges that ensure optimality of paid adoption in both segments.

First, as it can be seen from panels (a)–(c) in Figure 3, aggregate seeding ratio $\alpha ^ { * } = \alpha _ { L } ^ { * } + \alpha _ { H } ^ { * }$ is decreasing in s. Thus, we uncover a similar pattern as in

Figure 3 Sensitivity of Optimal Strategies with Respect to s Under Asymmetric Network Structure and Seeding Disutility Model ${ \pmb s o v } ^ { + }$ When $r = 0 . 4$

![](/api/attachments/G3RW422Q/fulltext/images/49438ca6d28644a5f09f1c408f141f20f611f1bbc10c24dc5b3a5bbbc0d7f45f.jpg)  
(d) $c = 0 . 1$

![](/api/attachments/G3RW422Q/fulltext/images/b4ab0f29e49cb9fc0d88bc426c3616e2b2abd060064532f8a3e75d82f2a83df9.jpg)  
(e) $c = 0 . 2$

(c) c = 0.4  
![](/api/attachments/G3RW422Q/fulltext/images/75f17fe4a9c5858e5b58cc48bc91a5d2f21e5b15e7fd7c3c42cf81f9ab3651d9.jpg)  
(f) $c = 0 . 4$

![](/api/attachments/G3RW422Q/fulltext/images/b23572b498567f3971a6d57b5fb17584a74fc41b17364b25397ab6e6924b9287.jpg)  
(g) $c = 0 . 1$

![](/api/attachments/G3RW422Q/fulltext/images/09bb15e68f046dfa018c29cc68d32e94c0d26880682bf32b0a62eb4e13c75199.jpg)

![](/api/attachments/G3RW422Q/fulltext/images/333e3ccd8e02d366e9f32136d782c723c4f3464fc13eb9475721b24389f6ec28.jpg)

![](/api/attachments/G3RW422Q/fulltext/images/c586ec88fd416c46729b497b58662ad3005fa275088373b43f2122b34fe34e13.jpg)

(h) $c = 0 . 2$  
![](/api/attachments/G3RW422Q/fulltext/images/0be08e1d85004ae9527edd9ee351bf0c11515609d5f55a51e1bfe8507a8186ed.jpg)

![](/api/attachments/G3RW422Q/fulltext/images/47e3766f07fbe2ff583606e563eaa3c569a0b5f7068d6a0029fecffe36132f9d.jpg)  
the case of the symmetric network. For low ranges of $s ,$ if s increases, the seeding disutility in segment H increases but there is no impact on segment L. All else equal, the decrease in WTP in segment H puts downward pressure on price. This impacts not only revenue from high-end segment but also that from low-end segment. To prevent too much revenue loss, the firm will react first by releasing some of the pressure on price in the high-end by boosting b<sup>∗</sup>. When c is low, as in panels (d) and (g) or (e) and (h), the firm will embed a relatively higher level of social media features in the product. As $b ^ { * }$ is pushed even higher, while $s$ is still small, it may be beneficial to increase $\alpha _ { H } ^ { * }$ in response to an increase in s because in both segments seeding is taken advantage of via network effects. In the low-end segment, the boost in $b ^ { * }$ eliminates some of the need for a high level of seeding and, thus, the firm can actually decrease $\alpha _ { L } ^ { * }$ without affecting too much the WTP of consumers in that segment. For high $c ,$ as in panels (f) and (i), in small ranges of $s ,$ given that it is too expensive to operate at high levels of $b ^ { * }$ , the boost in $\mathbf { \widehat { \boldsymbol { b } } ^ { * } }$ allows the firm to reduce its reliance on seeding in the low-end segment. It will also result to the same practice in the

high-end segment for different reasons. Because $b ^ { * }$ is small, for small $s ,$ as s increases the small boost in $b ^ { * }$ cannot compensate for the increase in seeding disutility. As such, we see in panels (e) and (f) that $\alpha _ { H } ^ { * }$ is decreasing in s. This reasoning applies pretty much in all cases once s gets large enough because seeding disutility simply grows too big and the firm will curb seeding in the high-end segment, because it cannot boost $\Breve { b ^ { * } }$ too much because of the associated convex costs. When c is high, this is also accompanied by an expected decrease in $b ^ { * }$ , as can be seen in panel (i) of Figure 3.

Figure 4 captures sensitivity with respect to $c .$ Again, from panels (a)–(c) we see that aggregate seeding ratio is decreasing in c. At the same time, convexity of social media costs induces $b ^ { * }$ to decrease in c. Thus, insights from the symmetric network case carry through. As c increases, $\bar { b } ^ { * }$ decreases, and, as a result, in both segments, the network value of the product decreases. When $c$ is low and $s$ is not too high, to avoid pressure on price, the firm might try to boost $\alpha _ { H } ^ { * }$ . This can be seen in panels (d) and (e). However, once seeding disutility is too high, this is not optimal anymore, as can be seen in panel (h). Once c is

Figure 4 Sensitivity of Optimal Strategies with Respect to c Under Asymmetric Network Structure and Seeding Disutility Model ${ \pmb s o v } ^ { + }$ When $r = 0 . 4$  
![](/api/attachments/G3RW422Q/fulltext/images/b4ef0daacae159c1dd5acbd0f2f35c11788a1ef09165a5cdebf38037215b25f0.jpg)

![](/api/attachments/G3RW422Q/fulltext/images/65dea25fe1bd42f81598dec8e6006b46a6b232f2050e024a95251b74e68d44f9.jpg)

![](/api/attachments/G3RW422Q/fulltext/images/e10b7579d753863cc51a9ca250baaea67d94a40b54f747278f6913061b5f69c0.jpg)

(d) s = 0.1  
![](/api/attachments/G3RW422Q/fulltext/images/2d38deeac832fc73694cd0713563c8d046973172b8470d55ea98cf2f8d140f96.jpg)

(e) s = 0.2  
![](/api/attachments/G3RW422Q/fulltext/images/f2f980e19557b7cc372b2ca166115e5134872e00c3878192890ff26706e3cb00.jpg)

(f) s = 0.4  
![](/api/attachments/G3RW422Q/fulltext/images/cccce4a1c6695a453e452eda5ec2bd7e6e8d071ee1a7bbb2d07ed234f812cdef.jpg)

(g) s = 0.1  
![](/api/attachments/G3RW422Q/fulltext/images/507da886147fe03358bd276ea72070612a79a2eb36239855cd4f89dcb91402b1.jpg)

(h) s = 0.2  
![](/api/attachments/G3RW422Q/fulltext/images/69522667649ac5b5398393da3e1ba3d456d259e8f38b23f13871e318515779d9.jpg)

![](/api/attachments/G3RW422Q/fulltext/images/388d8b26d772d2e970565246a6c9a5df43a7dba72244bc73881341053f3e15a8.jpg)  
too high, $b ^ { * }$ is pushed too low and seeding penalty would be too high if the firm would try to push seeding further. As such, it will decrease $\alpha _ { H } ^ { * }$ . Looking at the low-end segment, as the firm makes adjustments in the high-end segment to prevent too much pressure on price, it will expand its sales in the low-end segment by reducing seeding ratio, thus having more paying customers.

## 6. Conclusion

Firms nowadays are increasingly proactive in trying to strategically capitalize on consumer networks and social interactions. In this paper, we complement an emerging body of research on the engineering of WOM effects by exploring a different angle through which firms can strategically exploit the value-generation potential of the user network. Namely, we consider how software firms should optimize the strength of network effects at the utility level in tandem with the right seeding and pricing strategies in the presence of seeding disutilities. To the best of our knowledge, our study is one of the first explorations of this research path. Our results have important managerial implications for practitioners in the industry who are trying to capitalize on network effects in a more effective way. Moreover, the applicability of our results is augmented by the fact that we consider two potential seeding disutility scenarios, thus covering multiple plausible consumer reactions in the market.

Under complete information when the firm can target individual customer types, after deriving the optimal firm strategy and the associated market structure, we uncover counterintuitive complementarities between seeding and the building of social media features in the presence of disutility associated with seeding. Although both initiatives contribute to a direct increase in WTP of consumers, each of them comes at a cost. The inherent trade-offs induce the firm to scale back on any of these initiatives if the cost associated with the other increases. Thus, markets with high seeding disutility because of price discrimination are also exhibiting low network effects embedded in the products. Alternatively, markets for products where significant investment in social media features is necessary to make an impact on the network value also experience low levels of market seeding. We further show that our results are robust to both seeding disutility models.

Under incomplete information, although complementarity between seeding and building social media features continues to hold for $S D U ^ { - }$ everywhere, under disutility model $S D U ^ { + }$ we uncover a host of new insights. In particular, a more peculiar complementarity can occur as well, where, for small seeding penalties, it may be optimal for both seeding ratio and level of social media features to be increasing in the seeding penalty. Moreover, for intermediate seeding penalties or low costs we uncover the potential for the two actions to act as substitutes. Thus, different disutility models may actually lead to very different optimal strategies under incomplete information. This highlights the importance of not overlooking the form of the seeding disutility in various markets, especially in the absence of consumer information.

In an extension, we also explore how our framework and insights can be extended to certain classes of asymmetric networks. At a high level, some of the previous results remain robust, while new insights also emerge. Moreover, we explore how the firm jointly approaches the seeding process for different segments in the market by allocating seeds in each segment. For example, when both costs are high and the market is almost evenly split between the high and the low segments, complementarity between seeding and building social media features continues to hold. On the other hand, when seeding penalty is low, this complementarity relationship breaks as the firm may find it optimal to adjust overall seeding ratio and social media features in opposite directions in response to an increase in seeding penalty.

As expected, the value of information computed by taking the difference (or percent difference) between profits under complete and incomplete information is decreasing in both c and s. We only briefly mention here this point because it is intuitive. As it is becoming increasingly costly to induce high WTP, firms are less willing to pay high premiums for low returns on additional information.

Although our paper is among the first to address in an analytical setting the interaction between social media and seeding strategies, it does have its own limitations that present various interesting opportunities for future research. First, we assumed customers have limited information about the market structure (type distribution) and act myopically. In that sense, our study adds to the rich literature that assumes a more or less pronounced form of bounded rationality on the demand side. In future studies, this assumption can be relaxed toward an analysis of markets in the presence of strategic customers. We expect many of our insights to carry through. Second, one could look into extending our modeling framework to explore the implications of competition on how firms would jointly adjust seeding and social media features. Third, alternative forms of network effects (e.g., additive) can be considered in association with products that also carry an intrinsic value that is independent of the user network. Fourth, as an alternative to seeding, firms can consider freemium strategies to jump-start adoption. Fifth, it would be interesting to dive even deeper into exploring asymmetric networks, going beyond our illustration in §5. Although we focused mostly on the existence and direction of links between users, an interesting setting to consider would be one where links also have weights. As such, firms might focus seeding strategies toward opinion leaders. Also, it would be interesting to explore firm’s strategies in asymmetric networks where some of the users might consider a product to be a “status good,” deriving additional utility from being associated with the respective brand image (Kuksov 2007, Kuksov and Xie 2012). Sixth, for simplicity and, in some cases, analytical tractability, we assumed a reasonable sequence of adoption whereby higher types move first in cases when multiple customers who did not adopt yet would derive positive utility at a given moment. As discussed in the paper, the adoption sequence does not influence the results in §§3.1 and 5. However, it would be insightful to relax this assumption and explore how it affects optimal seeding and social media strategies under SDU<sup>−</sup>. Last but not least, it would be a very informative exercise to empirically test our model predictions.

## Acknowledgments

The authors thank the senior editor, associate editor, and the two anonymous reviewers for their constructive feedback on the manuscript. The authors also extend their gratitude to Terrence August, Hemant Bhargava, Rachel Chen, Vidyanand Choudhary, Debabrata Dey, Vijay Mookerjee, Barrie Nault, Yong Tan, Yong-Pin Zhou, Feng Zhu; the participants at the Information Systems Research Special Issue Workshop on Social Media and Business Transformation, University of Maryland, June 2–3, 2012; and the participants at the Theory in Economics of Information Systems Workshop, Laguna Beach, June 9–10, 2012, for their insightful comments. The authors acknowledge the financial support from the NET Institute (http://www.NETinst.org) [Summer Research Grant #11-07] and the Center for International Business Education and Research at Georgia Institute of Technology. Yifan Dou also acknowledges partial financial support from the National Natural Science Foundation of China (NSFC) [Grants 70890082 and 71232007] and from Tsinghua University Initiative Scientific Research Program [Grant 20101081741].

## Appendix A. Proofs

Proof of Lemma 1. <sub>(i)</sub> <sub>If</sub> $b ^ { * } \alpha ^ { * } - s \alpha ^ { * 2 } < p ^ { * } ,$ then paid adoption cannot start regardless of how seeds are assigned. Immediately after seeding, there is a mass of consumers of size  in the market. Given that we assume customers are myopic, even the highest-type customers $( \theta = 1 )$ cannot perceive a positive momentary utility at that stage. Thus, no unseeded customers is willing to be the first to pay for the software.

(ii, iii) We prove (ii) and (iii) simultaneously. Note that if the firm chooses to enter the market $( \mathrm { i . e . , }$ it can make profit), then $\alpha ^ { * } > 0$ and $b ^ { * } > 0 .$ . Via simple interchange arguments, it can be easily shown that the lowest-type paying customers must have type greater or equal to the highesttype seeded customers. Basically all that we have to show is that there are no unseeded customers that are left without a product.

Let $\theta _ { s }$ be the highest type among seeded customers and $\underline { { \theta } } _ { p }$ be the lowest type among paying customers. Then $0 \leq$ $\dot { \alpha ^ { * } } \leq \bar { \theta } _ { s } \leq \underline { { \theta } } _ { p } \leq 1$ . It is trivial to see that the highest-type customers (with $\theta = 1 )$ will be purchasing customers under any optimal seeding policy and seeds allocation.

Consider the function

$$
h (\theta) \triangleq [ b ^ {*} (1 - \theta + \alpha^ {*}) - s \alpha^ {* 2} ] \theta - p ^ {*}.
$$

Then h is concave in . If all customers with types above  adopt, then $h ( \theta )$ would represent the perceived utility for type  at the moment this type is considering adoption. Because consumers of type $\theta = 1$ are adopters, it must be the case that $h ( 1 ) \geq 0$ . Moreover, the following holds:

$$
(b ^ {*} - s \alpha^ {* 2}) \alpha^ {*} = b ^ {*} \alpha^ {*} - s \alpha^ {* 3} \geq b ^ {*} \alpha^ {*} - s \alpha^ {* 2}.
$$

Consequently,

$$
h (\alpha^ {*}) \geq h (1) \geq 0.
$$

Because h is concave in $\theta ,$ thus, $h ( \theta ) \geq 0$ for all $\theta \in [ \alpha ^ { * } , 1 ]$ Because $\bar { \theta } _ { s } \geq \alpha ^ { * }$ , then it immediately follows that adoption cannot stall before $\bar { \theta } _ { s }$ adopts. Consequently, we have $\bar { \theta } _ { s } ^ { - } = \underline { { \theta } } _ { \nu }$ and all customers above $\bar { \theta } _ { s }$ adopt.

The only thing left to prove is that $\bar { \theta } _ { s } = \alpha ^ { * } .$ , i.e., there are no unseeded customers below $\bar { \theta } _ { s } .$ . We prove this argument by contradiction. Suppose that under an optimal seeding allocation and optimal parameter values, $\bar { \theta } _ { s } > \alpha ^ { * }$ . Then, by seeding in interval $[ 0 , \bar { \alpha ^ { * } } )$ , the customers in the interval $[ \bar { \alpha } ^ { * } , \bar { \theta } _ { s } )$ will also adopt given that $h ( \theta ) \geq 0$ for $\theta \geq \alpha ^ { * }$ , and thus profit will increase. Contradiction. Such a seeding allocation cannot be optimal. Thus, $\bar { \theta } _ { s } = \alpha ^ { * }$ . Customers in the interval $[ 0 , \alpha ^ { * } )$ are seeded and all other customers end up buying the product. <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>1.</sup> According to Lemma 1, the firm will only consider scenarios where $b \alpha - s \alpha ^ { 2 } \geq p$ . Then, customers with types $\theta \in [ 0 , \alpha )$ are seeded and customers with types $\theta \in [ \stackrel { \cdot } { \alpha } , \stackrel { \cdot } { 1 } ]$ are purchasing the product. For each paying customer $\theta ,$ at purchase time the installed base is $\delta ( \theta , \alpha ) = 1 - \theta + \alpha$ because, in addition to all seeded customers, all customers with higher types would have already purchased the product and no customer with lower types is moving ahead of current type. Therefore, the utility of the customer of type  at purchase time is

$$
u (\theta \mid \alpha , b, p, \delta (\theta , \alpha)) = [ b (1 - \theta + \alpha) - s \alpha^ {2} ] \theta - p.\tag{A1}
$$

The utility function is concave in . Thus, for adoption to start and not to stall, it is necessary and sufficient that the utilities of the first paying customer and last paying customer are nonnegative:

$$
\begin{array}{r l} & u (\theta = 1 \mid \alpha , b, p, \delta (1, \alpha)) = (b \alpha - s \alpha^ {2}) - p \geq 0, \\ & u (\theta = \alpha \mid \alpha , b, p, \delta (\alpha , \alpha)) = (b - s \alpha^ {2}) \alpha - p \geq 0. \end{array}
$$

Given that $\alpha \in [ 0 , 1 ]$ we have b $- s \alpha ^ { 2 } \le b \alpha - s \alpha ^ { 3 }$ . Because the firm is profit maximizing, the IR constraint will be binding for the highest type and thus

$$
p ^ {*} (\alpha , b) = b \alpha - s \alpha^ {2}.\tag{A2}
$$

Consequently

$$
\pi (\alpha , b) = (b \alpha - s \alpha^ {2}) (1 - \alpha) - c b ^ {2}.
$$

${ \boldsymbol { \pi } } ( \alpha , b )$ is quadratic and concave in b. Note that for the constraint $b \alpha - s \alpha ^ { 2 } \geq p$ to hold, it is necessary that $b \geq s \alpha$ . Solving this constrained optimization problem, it immediately follows that

$$
b ^ {*} (\alpha) = \max \left\{s \alpha , \frac {\alpha (1 - \alpha)}{2 c} \right\}.
$$

Note that

$$
s \alpha \geq \frac {\alpha (1 - \alpha)}{2 c} \Leftrightarrow \alpha \geq 1 - 2 c s.
$$

Then

$$
\pi (\alpha) = \left\{ \begin{array}{l l} \frac {1}{4 c} \times \alpha^ {2} (1 - \alpha) (1 - 4 c s - \alpha) & \text { if } \alpha <   1 - 2 c s, \\ - c b ^ {2} & \text { otherwise. } \end{array} \right.
$$

Thus, if $\alpha \geq 1 - 2 c s$ the firm cannot make any profit and would exit the market. Therefore, to make a profit, the firm would choose $\alpha < 1 - 2 c s .$ . In this case, note that $\tau ( \alpha ) = 0$ has four roots $\alpha _ { 1 } = \alpha _ { 2 } = 0 , \ \alpha _ { 3 } = 1$ , and $\alpha _ { 4 } = 1 - 4 c s$ . We distinguish two cases:

(i) $1 / 4 \leq c s .$ Then $\begin{array} { r } { \alpha _ { 4 } \leq \alpha _ { 1 } = \alpha _ { 2 } = 0 < \alpha _ { 3 } . } \end{array}$ . Then $\pi ( \alpha )$ is decreasing on $( - \infty , \alpha _ { 4 } ] ,$ decreasing and then increasing on $[ \alpha _ { 4 } , 0 ] .$ , bouncing off at zero because that is a double root, decreasing and then increasing on $[ 0 , 1 ] ,$ , and increasing on $[ 1 , \infty )$ . Given that the firm considers $\alpha \in [ 0 , 1 - 2 c s )$ consequently we must have $\alpha ^ { * } = 0 ,$ . The optimal price and optimal network effects are zero and the firm exits the market because it cannot make any profit.

(ii) $1 / 4 > c s .$ In this case, $\alpha _ { 1 } = \alpha _ { 2 } = 0 < \alpha _ { 4 } = 1 - 4 c s <$ $\alpha _ { 3 } = 1$ . Then $\pi ( \alpha )$ is decreasing on $( - \infty , 0 ]$ , bouncing off at zero because that is a double root, increasing and then decreasing on $[ 0 , 1 - 4 c s ] ,$ decreasing and increasing on $[ 1 -$ 4cs1 17, and increasing on 611 5. Therefore, $\alpha ^ { * }$ is the unique root of the first order condition (FOC) that falls in the interval $( 0 , 1 - 4 c s )$ . That root is not zero (which is one of the roots of the FOC). Computing the FOC, we get

$$
\frac {\partial \pi}{\partial \alpha} = \frac {\alpha}{2 c} \times [ 1 - 4 c s - \alpha (3 - 6 c s) + 2 \alpha^ {2} ].
$$

The FOC gives optimal seeding ratio

$$
\alpha^ {*} = \frac {3 (1 - 2 c s)}{4} - \frac {\sqrt {1 - 4 c s + 3 6 c ^ {2} s ^ {2}}}{4}.
$$

It is trivial to verify that $\alpha ^ { * } \leq 1 / 2 . \quad \bigsqcup$

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>2.</sup> Follows directly from computing the derivatives of the optimal quantities $\alpha ^ { * }$ and $b ^ { * }$ derived in Proposition 1 with respect to c and s. <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Lemma</sup> <sup>2.</sup> (i) At the very beginning, right after the seeding process and before any paid adoption has occurred, a customer of type  perceives an instantaneous utility $u ( \theta \mid \cdot ) = ( b \alpha \theta - \dot { s \alpha ^ { 2 } } ( 1 - \hat { \theta } ) ) - p = ( b \alpha + s \alpha ^ { 2 } ) \theta -$ $s \alpha ^ { 2 } - p .$ Thus, at the very beginning (and actually also at every moment afterward), the instantaneous utility is increasing in type. Therefore, at least the highest-type customers must want to adopt. Thus, we need $u ( 1 \mid \cdot ) \geq 0 ,$ , or b $\geq p .$

(ii) Given that at any moment utility will be increasing in type (disutility is the same once seeding has occurred and the network benefits increase more for the higher types), it can be easily observed (via an interchange argument) that seeding should not be at the high end. No seeded customer should have a higher type than a paying customer. Moreover, given monotonicity of utility in type at any given time, everyone with type above the marginal type should adopt as well. <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>3.</sup> We present here a sketch of the proof. Some portions are omitted for brevity but available from the authors upon request. First, for the firm to make any profit, it is necessary to charge a positive price. That means that the highest-type adopters $( \theta \bar { = } 1 )$ must have positive benefit from the product before any paid adoption occurs. Because b $> { \bar { 0 } } ,$ highest-type adopters always have a positive WTP for the product. For a paying customer of type $\theta ,$ at the moment of purchase (after all the higher types have already adopted and before any other lower type adopts), her perceived utility is

$$
u (\theta \mid \cdot) = [ b (1 - \theta + \alpha) \theta - s \alpha^ {2} (1 - \theta) ] - p.
$$

The utility function is concave in . Given that $u ( 0 \mid \cdot ) =$ $- s \alpha ^ { 2 } - p \dot { \leq } 0 ,$ , adoption stops at a certain marginal type $\theta _ { m } ,$ where $\mathop { u } ( \theta _ { m } \mid \cdot ) \stackrel { \cdot } { = } 0 \leq u ( \stackrel { \cdot } { 1 } \mid \cdot ) .$ , or, equivalently, $\theta _ { m } \leq \alpha +$ $( s \alpha ^ { 2 } ) / b$ . Optimal price is given by $p ^ { * } = b ( 1 - \theta _ { m } + \alpha ) \theta _ { m } -$ s $^ 2 ( 1 - \theta _ { m } )$ . Also, $\theta _ { m } \geq \alpha$ . Then the profit is given by

$$
\begin{array}{l} \pi (\theta_ {m}, \alpha , b) \\ \qquad = p (1 - \theta_ {m}) - c b ^ {2} \\ \qquad = [ b (1 - \theta_ {m} + \alpha) \theta_ {m} - s \alpha^ {2} (1 - \theta_ {m}) ] (1 - \theta_ {m}) - c b ^ {2}. \end{array}\tag{A3}
$$

We consider two different cases: $( \mathrm { i } ) \ s = 0$ and $( \operatorname { i i } ) s > 0 .$

(i) s = 0. In this case, the optimal strategy under $S D U ^ { - }$ is identical to the optimal strategy under $S \bar { D } U ^ { + }$ , which has been derived in Proposition 1.

(ii) $s > 0 .$ In this case, profit function in (A3) is quadratic in . We optimize first in  under the constraint $0 \leq \alpha \leq$ ${ \theta _ { m } } \leq \operatorname* { m i n } \{ \bar { \alpha } + ( s \alpha ^ { 2 } ) / b , 1 \}$ . Moreover, we verify within each region that the profit is positive. Note that the profit function is concave in . Solving unconstrained $\mathsf { \bar { \partial } } \pi / \partial \alpha = 0 ,$ we obtain root $\alpha = ( b \theta _ { m } ) / ( 2 s ( \bar { 1 - \theta _ { m } } ) )$ . Moreover, given that $\alpha \ge 0 ,$ , it can be shown that $\alpha + ( s \alpha ^ { 2 } ) / b \geq \theta _ { m }$ is equivalent to $\alpha \ge ( - b + \sqrt { b ( b + 4 s \theta _ { m } ) } ) / ( 2 s )$ . Thus, we have

$$
\alpha^ {*} = \max \left\{\frac {- b + \sqrt {b (b + 4 s \theta_ {m})}}{2 s}, \min \left\{\theta_ {m}, \frac {b \theta_ {m}}{2 s (1 - \theta_ {m})} \right\} \right\}.
$$

After considering and comparing all the feasible cases (analysis omitted for brevity but available from the authors), it can be shown that the optimal solution is the following:

Region 1: $0 < c s \leq \bar { 1 / 8 }$ . In this case $\alpha ^ { * } = \theta _ { m } ^ { * } = 1 / 2 , \ \mathbf  \bar { \} } b ^ { * } = $ $1 / ( 8 c ) , \stackrel { \cdot } { \pi } ^ { \ast } = ( 1 - 4 c s ) / ( 6 4 c )$

Region 2: $1 / 8 < c s < ( 3 1 - 7 \sqrt { 1 7 } ) / 1 6 .$ In this case, $\alpha ^ { * } =$ $( b ^ { * } \theta _ { m } ^ { * } ) / \bar { ( } 2 s ( 1 - \theta _ { m } ^ { * } ) ) .$ , <sup>∗</sup> is the unique real solution to the equation $c s ( 2 - 6 \theta _ { m } ) ^ { - } + \theta _ { m } ^ { 3 } = 0$ over the interval $[ - 1 +$ $\dot { \sqrt { 1 + 8 c s } } , \sqrt { 2 c s } ] , \ \boldsymbol { b } ^ { * } = ( 2 s ( \boldsymbol { 1 } ^ { * } - \boldsymbol { \theta } _ { m } ^ { * } ) ^ { 2 } \boldsymbol { \theta } _ { m } ^ { * } ) / ( 4 c s - \boldsymbol { \theta } _ { m } ^ { * \ 2 } ) ,$ and $\pi ^ { * } =$ $( s ( 1 - \theta _ { m } ^ { * } ) ^ { 4 } { { \theta } _ { m } ^ { * } } ^ { 2 } ) \bar { / } ( 4 c s - { { \theta } _ { m } ^ { * } } ^ { 2 } )$ . Replacing $c s = \theta _ { m } ^ { * } { } ^ { 3 } / ( 6 \theta _ { m } ^ { * } - 2 ) ,$ it can be shown that $\alpha ^ { * } = 3 \theta _ { m } ^ { * } - 1 , b ^ { * } = ( ( 1 - \theta _ { m } ^ { * } ) { \theta _ { m } ^ { * } } ^ { 2 } ) / c ,$ and $\pi ^ { * } = s ( 1 - \theta _ { m } ^ { * } ) ^ { 3 } ( 3 \theta _ { m } ^ { * } - 1 ) .$

$R e g i o n \ 3 : ( 3 1 - 7 \sqrt { 1 7 } ) / 1 6 \leq c s .$ Then

$$
\alpha^ {*} = \frac {- b ^ {*} + \sqrt {b ^ {*} (b ^ {*} + 4 s \theta_ {m} ^ {*})}}{2 s}, \quad \theta_ {m} ^ {*} = \frac {- b ^ {*} + 3 s + \sqrt {b ^ {*} (b ^ {*} + 3 s)}}{9 s},
$$

and $b ^ { * } = \frac { 1 - 2 4 c s - 3 6 c ^ { 2 } s ^ { 2 } + ( 1 + 6 c s ) \sqrt { 1 + 3 6 c s + 3 6 c ^ { 2 } s ^ { 2 } } } { 1 6 c } ,$

$$
\text { and } \quad \pi^ {*} = b ^ {*} (- b ^ {*} c + \alpha^ {*} - \alpha^ {*} \theta_ {m} ^ {*}).
$$

Replacing $\theta _ { m } ^ { * }$ into $\alpha ^ { * }$ and $\pi ^ { * } ,$ we obtain

$$
\begin{array}{c} \alpha^ {*} = \frac {- b ^ {*} + \sqrt {b ^ {*} (b ^ {*} + 3 s)}}{3 s} \text {and} \\ \pi^ {*} = \frac {b ^ {*} (6 s \alpha^ {*} - \alpha^ {*} \sqrt {b ^ {*} (b ^ {*} + 3 s)} - 9 c s b ^ {*} + b ^ {*} \alpha^ {*})}{9 s}. \end{array}
$$

Then, we see that $- b ^ { * } \sqrt { b ^ { * } ( b ^ { * } + 3 s ) } = 3 \alpha ^ { * } s .$ Replacing in $\theta _ { m } ^ { * } ,$ we obtain $\theta _ { m } ^ { * } = ( 1 + \alpha ^ { * } ) / 3 , \mathrm { o r } \ \alpha ^ { * } = 3 \theta _ { m } ^ { * } - 1$

It can be shown that the optimal profit is positive in all regions. <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Corollary</sup> <sup>1.</sup> Follows immediately from the proof of Proposition 3. <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>4.</sup> As Proposition 3 states, the optimal strategy is characterized over three distinct regions for the value of cs. We explore each region separately

Region 1: $0 \leq c s \leq 1 / 8 .$ This case is straightforward. Results hold in weak form with respect to changes in s and only b responds to changes in c.

Region $\bar { 2 } : ~ 1 / 8 < c s < ( \bar { 3 } 1 - 7 \sqrt { 1 7 } ) / 1 6 ,$ . Note first that the optimal values $\alpha ^ { * }$ and $b ^ { * }$ depend on ${ \theta } _ { m } ^ { * }$ . Thus, we need to first understand the monotonicity of $\theta _ { m } ^ { * }$ with respect to c and s; $\theta _ { m } ^ { * }$ is defined in implicit form as the unique solution to equation $c s ( 2 - 6 \theta _ { m } ) \dot { + } \theta _ { m } ^ { 3 } = 0$ over the interval $[ - 1 +$ $\sqrt { 1 + 8 c s } , \sqrt { 2 c s } ]$ . Let us denote $\rho = c s$ and define function $\tau ( \theta _ { m } , \rho ) \triangleq \rho ( 2 - 6 \theta _ { m } ) + \theta _ { m } ^ { 3 }$ . Then $\theta _ { m } ^ { * } ( \rho )$ is the unique function such that $\tau ( \theta _ { m } ^ { * } ( \rho ) , \rho ) = 0$ for every $\rho \in ( 1 / 8 , ( 3 1 - 7 \sqrt { 1 7 } ) / 1 6 )$ Therefore, over this interval,

$$
\frac {\partial \theta_ {m} ^ {*} (\rho)}{\partial \rho} = - \frac {\partial \tau / \partial \rho}{\partial \tau / \partial \theta_ {m}} = - \frac {2 - 6 \theta_ {m} ^ {*}}{3 (\theta_ {m} ^ {* 2} - 2 \rho)}.
$$

As discussed in the proof of Proposition $^ { 3 , }$ in region $2 , \theta _ { m } ^ { * } <$ ${ \sqrt { 2 \rho } } .$ Moreover, $\theta _ { m } ^ { * } > 1 / 3$ . Thus, clearly, $\partial \theta _ { m } ^ { * } ( \rho ) / \partial \rho < 0 .$ . Consequently, since $\rho = c s , \theta _ { m } ^ { * }$ is decreasing in both c and s.

Because $\alpha ^ { * } = 3 \theta _ { m } ^ { * } \mathrm { ~ - ~ } 1 ,$ , it immediately follows that $\partial \alpha ^ { * } / \partial s < 0$ and $\partial \alpha ^ { * } / \partial c < 0 .$

Next, we consider the derivatives of $b ^ { * }$ with respect to $c$ and s:

$$
\begin{array}{c} \frac {\partial b ^ {*}}{\partial c} = \frac {\theta_ {m} ^ {*} [ c (2 - 3 \theta_ {m} ^ {*}) (\partial \theta_ {m} ^ {*} / \partial c) - (1 - \theta_ {m} ^ {*}) \theta_ {m} ^ {*} ]}{c ^ {2}} \quad \text { and } \\ \frac {\partial b ^ {*}}{\partial s} = \frac {\theta_ {m} ^ {*} (2 - 3 \theta_ {m} ^ {*})}{c} \times \frac {\partial \theta_ {m} ^ {*}}{\partial s}. \end{array}
$$

It can be easily seen that $\theta _ { m } ^ { * } < 1 / 2$ . Given that $2 - 3 \theta _ { m } ^ { * } >$ $0 , \ \partial \theta _ { m } ^ { * } / \partial s < 0 , \ \bar { \partial } \theta _ { m } ^ { * } / \partial c < 0 ,$ then it immediately follows that $\partial b ^ { * } / \partial s < 0$ and ¡b $\mathit { \Omega } / \partial c < 0$

Region 3: $( 3 1 - 7 \sqrt { 1 7 } ) / 1 6 \leq c s$ . Because we have the formula for $b ^ { * }$ only in terms of c and $s ,$ it can be easily verified that $\partial b ^ { * } / \partial s < 0$ and $\partial b ^ { * } / \partial c < 0$

From the proof of Proposition 3, in region 3, we know that $\alpha ^ { * } = ( - \bar { b } ^ { * } + \sqrt { b ^ { * } ( b ^ { * } + 3 s ) } ) / ( 3 s )$ . It immediately follows that

$$
\frac {\partial \alpha^ {*}}{\partial c} = \frac {(\sqrt {b ^ {*} + 3 s} - \sqrt {b ^ {*}}) ^ {2}}{6 s \sqrt {b ^ {*} (b ^ {*} + 3 s)}} \times \frac {\partial b ^ {*}}{\partial c} \quad \text { and }
$$

$$
\frac {\partial \alpha^ {*}}{\partial s} = \frac {- (\sqrt {b ^ {*} + 3 s} - \sqrt {b ^ {*}}) ^ {2} (b ^ {*} - s (\partial b ^ {*} / \partial s))}{6 s ^ {2} \sqrt {b ^ {*} (b ^ {*} + 3 s)}}.
$$

It can be easily seen that $\partial \alpha ^ { * } / \partial c < 0 .$ . Furthermore, note that $b ^ { * } = { \dot { s } } \gamma ( c s )$ , where $\gamma ( x ) \triangleq ( 1 - 2 4 x - 3 6 x ^ { 2 } +$ $( 1 ~ + ~ 6 x ) \sqrt { 1 + 3 6 x + 3 6 x ^ { 2 } } ) / ( 1 6 x )$ . It can be shown that $\gamma ( \boldsymbol { x } )$ is decreasing when $x \geq ( 3 1 - 7 { \sqrt { 1 7 } } ) / 1 6$ . Then $b ^ { * } -$ $s ( \partial b ^ { * } / \partial s ) = - c s ^ { 2 } \gamma ^ { \prime } ( c s ) > 0$ . Then, it immediately follows that $\partial \alpha ^ { * } / \partial s < 0 . \quad \bigsqcup$

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>5.</sup> Note that the profit in this model cannot exceed the profit under full information, where the seeds are allocated optimally. Since, according to Proposition 1, under full information the firm does not enter the market when $c s > 1 / 4 _ { , }$ , this holds true as well in the uniform seeding case. Thus, there exists $\xi \leq 1 / 4 ,$ such that, when $c s > \xi$ then the firm chooses not to enter the market.

First, for the firm to make any profit, it is necessary to charge a positive price. That means that the highest-type adopters $\bar { ( \theta = 1 ) }$ ) must have positive benefit from the product before any paid adoption occurs. Thus, it is necessary to have $b \geq s \alpha$ . For any (paying or nonpaying) individual with type , there are  seeded customers with type smaller than . Therefore, when a paying customer of type  decides to purchase the product, at the moment of purchase (after all the higher types already adopted and before any other lower type adopts) her perceived utility is

$$
u (\theta \mid \cdot) = [ b (1 - \theta + \alpha \theta) - s \alpha^ {2} ] \theta - p.
$$

The utility function is concave in . Given that $u ( 0 \mid \cdot ) =$ $- p \leq 0 ,$ adoption stops at a certain marginal type $\theta _ { m } ,$ where $u ( \theta _ { m } \ { \textrm { \cdot } } ) \ { \textrm { \cdot } } ) = 0 \ { \textrm { \leq } } \ u ( 1 \ | \ \ \cdot )$ , or, equivalently, $\theta _ { m } \ \leq$ $( \alpha ( b - s \alpha ) ) / ( b ( 1 - \alpha ) ) . ^ { 6 }$ Then, it follows that $p = [ b ( 1 - \theta _ { m } +$ $\alpha \theta _ { m } ) - s \alpha ^ { 2 } ] \theta _ { m } ,$ and the profit is given by

$$
\begin{array}{l} \pi (\theta_ {m}, \alpha , b) \\ \qquad = p (1 - \alpha) (1 - \theta_ {m}) - c b ^ {2} \\ \qquad = [ b (1 - \theta_ {m} + \alpha \theta_ {m}) - s \alpha^ {2} ] \theta_ {m} (1 - \alpha) (1 - \theta_ {m}) - c b ^ {2}. \end{array}\tag{A4}
$$

We optimize first in $\theta _ { m }$ under constraint $\theta _ { m } \ \leq$ min $\mathbb { \cdot } \{ ( \bar { \alpha ( b - s \alpha ) } ) / ( b ( 1 - \alpha ) ) , 1 \}$ . Note that the profit is cubic in $\theta _ { m }$ with a positive coefficient for $\theta _ { m } ^ { 3 }$ . Solving for $\partial \pi / \partial \theta _ { m } = 0 ,$ , we obtain the following two local extremes:

$$
\begin{array}{l} \theta_ {m, 1} = \frac {2 b - b \alpha - s \alpha^ {2} - \sqrt {b ^ {2} - b ^ {2} \alpha + b ^ {2} \alpha^ {2} - b s \alpha^ {2} - b s \alpha^ {3} + s ^ {2} \alpha^ {4}}}{3 b (1 - \alpha)}, \\ \theta_ {m, 2} = \frac {2 b - b \alpha - s \alpha^ {2} + \sqrt {b ^ {2} - b ^ {2} \alpha + b ^ {2} \alpha^ {2} - b s \alpha^ {2} - b s \alpha^ {3} + s ^ {2} \alpha^ {4}}}{3 b (1 - \alpha)}. \end{array}
$$

It can be shown that $0 \leq \theta _ { m , 1 } \leq 1 \leq \theta _ { m , 2 }$ . Thus, the profit is increasing in $\theta _ { m }$ over $[ 0 , \theta _ { m , 1 } ]$ and decreasing over $[ \bar { \theta } _ { m , 1 } , 1 ]$ Thus

$$
\theta_ {m} ^ {*} = \min \left\{\theta_ {m, 1}, \frac {\alpha (b - s \alpha)}{b (1 - \alpha)} \right\}.\tag{A5}
$$

We will split the analysis into 10 cases, based on when $\theta _ { m , 1 } < ( \geq ) \bar { ( } \alpha ( b - s \alpha ) ) / ( \bar { b } ( 1 - \alpha ) )$

C $\mathit { a s e 1 . 1 / 2 < \alpha < 1 \mathrm { a n d } b \geq ( s \alpha ^ { 2 } ) / ( 2 \alpha - 1 ) }$

$C a s e ~ 2 . ~ ( 5 + { \sqrt { 5 } } ) / 1 0 ~ < ~ \alpha ~ < ~ 1 ~ \mathrm { a n d } ~ ( - 3 s \alpha ^ { 2 } ~ + ~ 5 s \alpha ^ { 3 } ~ -$ $\sqrt { 5 } s \alpha ^ { 2 } ( 1 - \alpha ) ) / ( 2 ( 1 - 5 \alpha + 5 \alpha ^ { 2 } ) ) \leq b < ( s \alpha ^ { 2 } ) / ( 2 \alpha - 1 ) .$

$\mathit { C a s e 3 . } ~ ( 5 + \sqrt { 5 } ) / 1 0 < \alpha < 1$ and $s \alpha \leq b < ( - 3 s \alpha ^ { 2 } + 5 s \alpha ^ { 3 } -$ $\sqrt { 5 } s \alpha ^ { 2 } ( 1 - \alpha ) ) / ( 2 ( 1 - 5 \alpha + 5 \alpha ^ { 2 } ) ) .$

Case 4.  = 45 + 55/10 and $( ( 3 + { \sqrt { 5 } } ) s ) / ( 5 ( { \sqrt { 5 } } - 1 ) ) \leq b <$ $( s \alpha ^ { 2 } ) / ( 2 \alpha - 1 )$

$C a s e 5 . \alpha = ( 5 + \sqrt { 5 } ) / 1 0$ and $s \alpha \leq b < ( ( 3 + \sqrt { 5 } ) s ) /$ $( 5 ( { \sqrt { 5 } } - 1 ) ) .$

$$
6. 1 / 2 <   \alpha <   (5 + \sqrt {5}) / 1 0
$$

$$
(- 3 s \alpha^ {2} + 5 s \alpha^ {3} -
$$

$$
\sqrt {5} s \alpha^ {2} (1 - \alpha)) / (2 (1 - 5 \alpha + 5 \alpha^ {2})) \leq b <   (s \alpha^ {2}) / (2 \alpha - 1)
$$

$\mathit { C a s e 7 . 1 / 2 < \alpha < ( 5 + \sqrt { 5 } ) / 1 0 }$ and s $\leq b < ( - 3 s \alpha ^ { 2 } +$ $5 s \alpha ^ { 3 } - \sqrt { 5 } s \alpha ^ { 2 } ( 1 - \alpha ) ) / ( 2 ( 1 - 5 \alpha + 5 \alpha ^ { 2 } ) ) .$

Case 8. $( 5 - \sqrt { 5 } ) / 1 0 < \alpha \leq 1 / 2$ and $( - 3 s \alpha ^ { 2 } + 5 s \alpha ^ { 3 } -$ $\sqrt { 5 } s \alpha ^ { 2 } ( 1 - \alpha ) ) / ( 2 ( 1 - 5 \alpha + 5 \alpha ^ { 2 } ) ) \leq b .$

$C a s e 9 . ( 5 - \sqrt { 5 } ) / 1 0 < \alpha \leq 1 / 2$ and s $\leq b < ( - 3 s \alpha ^ { 2 } +$ $5 s \alpha ^ { 3 } - \sqrt { 5 } s \alpha ^ { 2 } ( 1 - \alpha ) ) / ( 2 ( 1 - 5 \alpha + 5 \alpha ^ { 2 } ) )$

$$
0 <   \alpha \leq (5 - \sqrt {5}) / 1 0.
$$

For Cases $1 , ~ 2 , ~ 4 , ~ 7 ,$ and 9, we have $\theta _ { m } ^ { * } = \theta _ { m , 1 } <$ $( \alpha ( b - s \alpha ) ) / ( b ( 1 - \alpha ) )$ . For all the other Cases $( 3 , 5 , 6 , 8 , 1 0 ) ,$ we have $\theta _ { m } ^ { * } = ( \alpha ( b - s \alpha ) ) / ( b ( 1 - \alpha ) ) \le \theta _ { m , 1 }$ . Replacing ${ \boldsymbol { \theta } } _ { m } ^ { * }$ in (A4), we obtain an expression for profit in terms of b and . It can be shown that when $\alpha > ( 5 - { \sqrt { 5 } } ) / 1 0 .$ , i.e., in cases 1–9, for any given feasible $b ,$ profit is decreasing in . Thus, none of these cases is possible under optimality. Consequently, under optimality, the firm will choose  and b such that case 10 occurs. Thus, under optimality

$$
\theta_ {m} ^ {*} = \frac {\alpha^ {*} (b ^ {*} - s \alpha^ {*})}{b ^ {*} (1 - \alpha^ {*})}, \quad 0 <   \alpha^ {*} \leq \frac {5 - \sqrt {5}}{1 0}, \quad b ^ {*} \geq s \alpha^ {*}.\tag{A6}
$$

Replacing $\theta _ { m } ^ { * }$ in (A4), we obtain

$$
\pi (\alpha , b) = b (1 - 2 \alpha) \alpha - \frac {s ^ {2} \alpha^ {4}}{b} - s \alpha^ {2} (1 - 3 \alpha) - c b ^ {2}.\tag{A7}
$$

It can be shown that when $\alpha \ : < \ : ( 5 - \sqrt { 5 } ) / 1 0 ,$ , then $\partial ^ { 2 } \pi ( \alpha , b ) / \partial \alpha ^ { 2 } \leq 0$ for any feasible $b ,$ i.e., profit is concave in the seeding ratio. Also, $\partial \pi ( \alpha , b ) / \partial \alpha | _ { \alpha = 0 } > 0 ,$ $\partial \pi ( \alpha , b ) / \partial \alpha | _ { \alpha = ( 5 - \sqrt { 5 } ) / 1 0 } < 0$ . Moreover, when $b < s ,$ it can also be shown that $\partial \pi ( \alpha , b ) / \partial \alpha | _ { \alpha = b / s } < 0$ . Thus, the optimal seeding ratio is interior, unique, and satisfies FOC. Furthermore, $\alpha ^ { * } ( b ) < b / s$ for any $b ,$ so the only constraint on b that we imposed will be satisfied. For any $b ,$ the seeding ratio is given in implicit form as the unique solution to $\partial \pi ( \alpha , b ) / \partial \alpha = 0$ over the interval $[ 0 , ( 5 - { \sqrt { 5 } } ) / 1 0 )$ . Simplifying FOC, for any $b , \alpha ^ { * } ( b )$ satisfies

$$
b ^ {2} [ 1 - 4 \alpha^ {*} (b) ] - 4 s ^ {2} \alpha^ {*} (b) ^ {3} + b s \alpha^ {*} (b) [ - 2 + 9 \alpha^ {*} (b) ] = 0
$$

$$
\alpha^ {*} (b) <   \frac {5 - \sqrt {5}}{1 0}.\tag{A8}
$$

For any general value $\alpha \in ( ( 2 ( 5 - 2 { \sqrt { 2 } } ) ) / 1 7 , ( 5 - { \sqrt { 5 } } ) / 1 0 ) .$ we have $\smile \ l { b } ^ { 2 } ( 1 - 4 \alpha ) \ l - 4 s ^ { 2 } \alpha ^ { 3 } + b s \alpha ( - 2 + 9 \alpha ) \ l < 0$ for any $b \geq 0 , s \geq 0 $ . Thus, it must be the case that $\alpha ^ { * } ( b )$ ∈ $[ 0 , ( 2 ( 5 - 2 \sqrt { 2 } ) ) / 1 7 ]$

In regions where the firm enters the market, we need to prove existence and uniqueness of $b ^ { * }$ maximizing $\pi ( \hat { \alpha ^ { * } } ( b ) , b )$ in (A7).

First, when $s = 0 ,$ it immediately follows that the unique solution is $b ^ { * } = 1 / ( 1 6 c )$

For the remaining part of the proof we focus on the case when $s > 0 .$ . Using (A8) to simplify (A7), we obtain

$$
\pi (b) = \frac {b ^ {2} (3 - 1 6 c s) + 6 b (- 2 b + s) \alpha^ {*} (b) + (1 1 b - 8 s) s \alpha^ {*} (b) ^ {2}}{1 6 s}.\tag{A9}
$$

From $( \mathsf { A } 8 )$ we have li $\begin{array} { r } { \Omega _ { b \to 0 } \alpha ^ { * } ( b ) = 0 ; } \end{array}$ hence from (A9) we have lim $\mathfrak { r } _ { b  0 } \pi ( b ) = 0$ . Moreover, when $b = 0 ,$ the firm cannot make profit as no consumer will buy the product for a positive price. As such $\pi ( 0 ) = 0 .$ . It can be shown that $\begin{array} { r } { \operatorname* { l i m } _ { b \to \infty } \alpha ^ { * } ( b ) = 1 / 4 } \end{array}$ . From Equation $( \mathrm { A } 7 ) ,$ , we see that, in this $\mathrm { c a s e , } \ - c b ^ { 2 }$ will be the dominant term as b gets large. Hence, li $\mathfrak { n } _ { b \to \infty } \pi ( b ) = - \infty$ . It follows immediately that for large b, the profit will be decreasing in b. Given that $\alpha ^ { * } ( b ) \in \ \bar { [ 0 , ( 2 ( 5 - 2 \sqrt { 2 } ) ) / 1 7 ] }$ , there exists $\bar { b } > 0$ such that $\pi ( b ) < 0$ for all $b > \bar { b } , \pi ( 0 ) = 0 .$ , and $\pi ( b )$ is continuously differentiable on compact $[ 0 , { \bar { b } } ] ,$ , the existence of a maximum is guaranteed for 4b5 over $[ 0 , \infty )$

We next move to prove uniqueness of $b ^ { * }$ in cases where $s > 0$ and the firm chooses to enter the market, i.e., in cases when $\pi ( b ^ { * } ) > 0$ . Since $\pi ( 0 ) = 0 , b ^ { * }$ must be interior and satisfy FOC of $( \mathrm { A } 9 ) , \mathrm { i . e . , } \partial \pi ( b ) / \partial b | _ { b = b ^ { \ast } } = 0$

We will prove below that FOC of (A9) can have a unique solution when $\alpha ^ { * } ( b ) \in ( 0 , ( 2 ( 5 - 2 \sqrt { 2 } ) ) / 1 7 ] , \alpha ^ { * } ( b )$ satisfies (A8), and $b > 0 .$ . We can skip case $\alpha ^ { * } = 0$ because in that case the firm will set $b ^ { * } = 0$ because it cannot make any profit. Differentiating (A8) with respect to b and using the implicit function theorem, we obtain

$$
\frac {d \alpha^ {*} (b)}{d b} = \frac {2 b (1 - 4 \alpha^ {*}) + s \alpha^ {*} (9 \alpha^ {*} - 2)}{2 [ b (2 b + s) - 9 b s \alpha^ {*} + 6 s ^ {2} \alpha^ {* 2} ]}.\tag{A10}
$$

It can be easily shown that $b ( 2 b + s ) - 9 b s \alpha + 6 s ^ { 2 } \alpha ^ { 2 } > 0$ for any $b > 0 , \ s > 0 , \ 0 \leq \alpha \leq ( 2 ( 5 - 2 \sqrt { 2 } ) ) / 1 7$ . Thus, the derivative in (A10) is properly defined. Taking total derivatives in Equation (A9) with respect to b, we obtain d $\cdot / d b = \partial \pi / \partial b +$ ¡ $/ \partial \alpha ^ { * } \times d \alpha ^ { * } / d b$ . Inserting (A10), we obtain

$$
\begin{array}{c} \frac {d \pi}{d b} = (- 3 2 b ^ {3} c + s ^ {2} \alpha^ {* 2} [ 8 + 3 \alpha^ {*} (1 1 \alpha^ {*} - 6) ] \\ \qquad + 2 b ^ {2} [ 3 + 8 c s (9 \alpha^ {*} - 1) + 2 \alpha^ {*} (1 2 \alpha^ {*} - 7) ] \\ \qquad - b s \alpha^ {*} [ 8 + \alpha^ {*} (7 2 \alpha^ {*} + 9 6 c s - 3 1) ]) \\ \qquad \cdot (8 [ b (2 b + s) - 9 b s \alpha^ {*} + 6 s ^ {2} \alpha^ {* 2} ]) ^ {- 1}. \end{array}\tag{A11}
$$

As discussed above, the denominator is always positive. Thus, for FOC to be satisfied, the numerator must be zero. We discuss two cases:

(i) $\alpha ^ { * } = 1 / 4 .$ Then, from (A8) it follows that $b ^ { * } = s .$ Replacing b<sup>∗</sup> in (A11), we have $d \pi / d b = 0$ if and only if $c s = 3 3 / 5 1 2 $

(ii) $\alpha ^ { * } \in ( 0 , 1 / 4 ) \cup ( 1 / 4 , ( 2 ( 5 - 2 \sqrt { 2 } ) ) / 1 7 ]$ . Then, from (A8) we have

$$
b ^ {2} = \frac {4 s ^ {2} \alpha^ {* 3} + b s \alpha^ {*} (2 - 9 \alpha^ {*})}{1 - 4 \alpha^ {*}}.\tag{A12}
$$

Repeatedly using (A12) to reduce the degree of $b ,$ we can transform the numerator in the left-hand side of $( \mathsf { A } 1 1 )$ into a linear equation in b. It follows that a maximizing b value must satisfy

$$
\begin{array}{l} b = (s \alpha^ {*} (- 8 + 5 8 \alpha^ {*} + 6 4 c s \alpha^ {*} - 9 7 \alpha^ {* 2} - 5 7 6 c s \alpha^ {* 2} - 8 8 \alpha^ {* 3} \\ \quad + 1, 1 5 2 c s \alpha^ {* 3} + 2 4 0 \alpha^ {* 4})) \\ \cdot (4 - 3 2 c s - 6 3 \alpha^ {*} + 3 3 6 c s \alpha^ {*} + 3 4 0 \alpha^ {* 2} - 1, 2 3 2 c s \alpha^ {* 2} \\ \quad - 7 5 2 \alpha^ {* 3} + 1, 5 6 8 c s \alpha^ {* 3} + 5 7 6 \alpha^ {* 4}) ^ {- 1}. \end{array} \tag {A1}\tag{A13}
$$

A profit-maximizing pair $( \alpha ( b ^ { * } ) , b ^ { * } )$ must satisfy both (A8) and (A13). Inserting (A13) into (A8), we obtain

$$
\mu_ {1} (\alpha^ {*}) \times \mu_ {2} (\alpha^ {*}) \times \mu_ {3} (\alpha^ {*}) = 0,\tag{A14}
$$

where

$$
\begin{array}{l} \mu_ {1} (\alpha) \triangleq - (8 s ^ {2} (1 - 4 \alpha) ^ {2} (1 - \alpha) \alpha^ {2}) \\ \quad \cdot ([ 1 6 c s (7 \alpha - 2) (1 + 7 \alpha (2 \alpha - 1)) \\ \quad + (4 \alpha - 1) (- 4 + \alpha (4 7 + 8 \alpha (1 8 \alpha - 1 9))) ] ^ {2}) ^ {- 1}, \\ \mu_ {2} (\alpha) \triangleq 4 + 3 4 \alpha^ {2} - 2 3 \alpha , \\ \mu_ {3} (\alpha) \triangleq 2 5 6 c ^ {2} s ^ {2} \alpha^ {2} - 2 c s (9 \alpha - 2) (4 + \alpha^ {2} - 8 \alpha) \\ \quad - (\alpha - 1) (4 \alpha - 1) (4 + 3 \alpha (6 \alpha - 5)). \end{array}
$$

It can be immediately seen that $\mu _ { 1 } ( \alpha ) < 0$ and $\mu _ { 2 } ( \alpha ) > 0$ for all $\alpha \in ( 0 , 1 / 4 ) \cup ( 1 / 4 , ( 2 ( 5 - 2 \sqrt { 2 } ) ) / 1 7 ]$ . Thus, (A14) can hold if and only if $\mu _ { 3 } ( \alpha ^ { * } ) = 0$ . Thus, for b to be unique, it is necessary and sufficient for $\mu _ { 3 } ( \alpha )$ to have a unique solution over $( 0 , 1 / 4 ) \cup ( 1 / 4 , ( 2 ( 5 - 2 \sqrt { 2 } ) ) / 1 7 ]$ when $c s < 1 / 4$ . It can be shown that $d \mu _ { 3 } ( \alpha ) / d \alpha > 0$ on $( 0 , ( 2 ( 5 -$ $2 \sqrt { 2 } ) ) / 1 7 ]$ when $c s < 1 / 4$ . Moreover, $\mu _ { 3 } ( 0 ) = - 4 + 1 6 c s < 0$ and $\mu _ { 3 } ( ( 2 ( 5 - 2 \sqrt { 2 } ) ) / 1 7 ) = ( ( 1 , 0 2 4 ( 3 3 - 2 0 \sqrt { 2 } ) ) / 2 8 9 ) ( c s - c$ $( 2 1 { \sqrt { 2 } } - 1 0 ) / 5 4 4 ) ^ { 2 } \geq 0 .$ Thus, $\mu _ { 3 } ( \alpha ) = 0$ has a unique solution in the desired region. Moreover, given that $\mu _ { 3 } ( 1 / 4 ) =$ $( 1 / 3 2 ) ( - 3 3 + 5 1 2 c s )$ , we see that a unique optimal solution under case (ii) always exists when $c s \neq 3 3 / 5 1 2$ . When $c s =$ $3 3 / 5 1 2 ,$ no solution exists under case (ii) but a unique solution exists under case (i). <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>6.</sup> Note that in this model, for any $b > 0$ and $\alpha > 0 ,$ because b $> 0 ,$ the firm can get the adoption started under a positive price because the highest-type customers have no seeding-induced disutility. The firm will never choose $\alpha = 0 \ \mathrm { o r } \ b = 0$ . For any (paying or nonpaying) individual with type , there is a mass of size  of seeded customers with types smaller than . Therefore, when a paying customer of type  decides to purchase the product, at the moment of purchase (after all the higher types already adopted and before any other lower type adopts) her perceived utility is

$$
u (\theta \mid \cdot) = [ b (1 - \theta + \alpha \theta) \theta - s \alpha^ {2} (1 - \theta) ] - p.
$$

The utility function is concave in . Given that $u ( 0 \mid \cdot ) =$ $- s \alpha ^ { 2 } - p \overset { . } { \mathop { \leq } } 0 .$ , adoption stops at a certain marginal type $\theta _ { m } ,$ where $u ( \theta _ { m } \mid \cdot ) \stackrel { - } { = } 0 \leq \bar { u } ( 1 | \cdot )$ , or, equivalently, $\theta _ { m } \ \leq$ $( \alpha ( b + s \alpha ) ) / ( b ( 1 - \alpha ) ) . ^ { 7 }$ Then, it follows that the optimal price is $p = b ( 1 - \theta _ { m } + \alpha \theta _ { m } ) \theta _ { m } - s \alpha ^ { 2 } ( 1 - \theta _ { m } )$ , and the profit is given by

$$
\begin{array}{c} \pi (\theta_ {m}, \alpha , b) = p (1 - \alpha) (1 - \theta_ {m}) - c b ^ {2} \\ = [ b (1 - \theta_ {m} + \alpha \theta_ {m}) \theta_ {m} - s \alpha^ {2} (1 - \theta_ {m}) ] \\ \cdot (1 - \alpha) (1 - \theta_ {m}) - c b ^ {2}. \end{array}\tag{A15}
$$

We optimize first in $\theta _ { m }$ under constraint $\theta _ { m } \leq \operatorname* { m i n } \{ ( \alpha ( b +$ $s \alpha ) ) / ( \bar { ( } b ( 1 - \alpha ) ) , 1 \}$ . Note that the profit is cubic in $\theta _ { m }$ with a positive coefficient for $\theta _ { m } ^ { 3 }$ . Solving for $\partial \pi / \partial \theta _ { m } = 0 ,$ , we obtain the following two local extremes:

$$
\begin{array}{l} \theta_ {m, 1} = \frac {2 b - b \alpha + s \alpha^ {2} - \sqrt {b ^ {2} - b ^ {2} \alpha + b ^ {2} \alpha^ {2} - 2 b s \alpha^ {2} + 4 b s \alpha^ {3} + s ^ {2} \alpha^ {4}}}{3 b (1 - \alpha)}, \\ \theta_ {m, 2} = \frac {2 b - b \alpha + s \alpha^ {2} + \sqrt {b ^ {2} - b ^ {2} \alpha + b ^ {2} \alpha^ {2} - 2 b s \alpha^ {2} + 4 b s \alpha^ {3} + s ^ {2} \alpha^ {4}}}{3 b (1 - \alpha)}. \end{array}
$$

It can be shown that $0 \leq \theta _ { m , 1 } \leq 1 \leq \theta _ { m , 2 }$ . Therefore, the profit is increasing in $\theta _ { m }$ over $[ 0 , \theta _ { m , 1 } ]$ and decreasing over $\left[ \theta _ { m , 1 } , 1 \right]$ . Thus

$$
\theta_ {m} ^ {*} = \min \left\{\theta_ {m, 1}, \frac {\alpha (b + s \alpha)}{b (1 - \alpha)} \right\}.\tag{A16}
$$

We will split the analysis into five cases, based on when $\theta _ { m , 1 } \leq ( \geq ) \bar { ( } \alpha ( b + s \alpha ) ) / ( \bar { b } ( 1 - \alpha ) )$ .

Case 1. 1/2 ≤ .

Case 2. 0 <  < 1/2 and $b \leq ( s \alpha ^ { 2 } ) / ( 1 - 2 \alpha )$

Case 3. $( 5 - \sqrt { 5 } ) / 1 0 \leq \alpha < 1 / 2$ and $( s \alpha ^ { 2 } ) / ( 1 - 2 \alpha ) < b .$

Case 4. $0 < \alpha < ( 5 - \sqrt { 5 } ) / 1 0$ and $( s \alpha ^ { 2 } ) / ( 1 - 2 \alpha ) < b \leq$ $( s \alpha ^ { 2 } ( 1 - 2 \alpha + \sqrt { \alpha ( 1 - \alpha ) } ) ) / ( 1 - 5 \alpha + 5 \alpha ^ { 2 } ) .$

$\mathit { C a s e 5 . 0 } ~ < ~ \alpha ~ < ~ ( 5 ~ - ~ \sqrt { 5 } ) / 1 0$ and $( s \alpha ^ { 2 } ( 1 ~ - ~ 2 \alpha ~ + ~$ $\sqrt { \alpha ( 1 - \alpha ) } ) ) / ( 1 - 5 \alpha + 5 \alpha ^ { 2 } ) < b .$

For Cases 1–4, we have $\theta _ { m } ^ { * } \ = \ \theta _ { m , 1 } \ \leq \ ( \alpha ( b \ + \ s \alpha ) ) /$ $( b ( 1 ~ - ~ \alpha ) )$ . For Case $5 ,$ we have $\theta _ { m } ^ { * } = ( \alpha ( b + s \alpha ) ) /$ $\left( b ( 1 - \alpha ) \right) \le \theta _ { m , 1 }$ . Replacing ${ \boldsymbol { \theta } } _ { m } ^ { * }$ in (A4), we obtain an expression for profit in terms of b and . It can be shown that in all Cases 1–4, for any given feasible $b ,$ profit is decreasing in . Thus, none of these cases is possible under optimality. Case $\alpha = ( 5 - { \sqrt { 5 } } ) / 1 0$ can be easily ruled out as well (to make sure that the optimal solution is not at the boundary of Case 3). Consequently, under optimality, the firm will choose  and b such that Case 5 occurs. Thus, under optimality,

$$
\begin{array}{c} \theta_ {m} ^ {*} = \frac {\alpha^ {*} (b ^ {*} + s \alpha^ {*})}{b ^ {*} (1 - \alpha^ {*})}, 0 <   \alpha^ {*} <   \frac {5 - \sqrt {5}}{1 0}, \\ b ^ {*} > \frac {s \alpha^ {* 2} (1 - 2 \alpha^ {*} + \sqrt {\alpha^ {*} (1 - \alpha^ {*})})}{1 - 5 \alpha^ {*} + 5 \alpha^ {* 2}}. \end{array}\tag{A17}
$$

Replacing $\theta _ { m } ^ { * }$ in (A15), we obtain

$$
\pi (\alpha , b) = b (1 - 2 \alpha) \alpha - s \alpha^ {3} - c b ^ {2}.\tag{A18}
$$

We consider two cases: $( \mathrm { i } ) \ s = 0$ and $( \mathrm { i i } ) \ s > 0$

(i) s = 0. In this case, the optimal strategy under SDU<sup>−</sup> with uniform seeding is identical to the optimal strategy under SDU<sup>+</sup>, which has been derived in Proposition 5.

(ii) $s > 0 .$ . In this case, from A18, for any $b ,$ we see that profit is cubic in  with negative coefficient for the degree 3 term. The solutions to $\pi ( \alpha , b ) / \partial \alpha = 0$ are

$$
\alpha_ {1} = \frac {- 2 b - \sqrt {4 b ^ {2} + 3 b s}}{3 s} <   0 <   \alpha_ {2} = \frac {- 2 b + \sqrt {4 b ^ {2} + 3 b s}}{3 s} <   \frac {5 - \sqrt {5}}{1 0}.
$$

It immediately follows that

$$
\alpha^ {*} (b) = \frac {- 2 b + \sqrt {4 b ^ {2} + 3 b s}}{3 s}.\tag{A19}
$$

It can be verified that

$$
\frac {s \alpha^ {*} (b) ^ {2} [ 1 - 2 \alpha^ {*} (b) + \sqrt {\alpha^ {*} (b) (1 - \alpha^ {*} (b))} ]}{1 - 5 \alpha^ {*} (b) + 5 \alpha^ {*} (b) ^ {2}} <   b
$$

for any $b > 0 .$ Thus, the constraint in Case 5 holds for any b once the firm seeds a fraction $\alpha ^ { * } ( b )$ of the market. Then, inserting $\alpha ^ { * } ( b )$ into (A18), we obtain

$$
\pi (b) = \frac {b [ (8 b + 6 s) \sqrt {b (4 b + 3 s)} - 1 6 b ^ {2} - 9 b s (2 + 3 c s) ]}{2 7 s ^ {2}}.\tag{A20}
$$

Then, it can be shown that $\partial \pi ( b ) / \partial b = 0$ has three roots

$$
\begin{array}{c} b _ {1} = \frac {1 - 1 2 c s - 9 c ^ {2} s ^ {2} - (1 + 3 c s) \sqrt {1 + 1 8 c s + 9 c ^ {2} s ^ {2}}}{3 2 c} <   b _ {2} = 0 \\ <   b _ {3} = \frac {1 - 1 2 c s - 9 c ^ {2} s ^ {2} + (1 + 3 c s) \sqrt {1 + 1 8 c s + 9 c ^ {2} s ^ {2}}}{3 2 c}, \end{array}
$$

and $\partial \pi ( b ) / \partial b < 0$ on $( b _ { 1 } , 0 ) \cup ( b _ { 3 } , \infty )$ and $\partial \pi ( b ) / \partial b > 0$ on $( - \infty , b _ { 1 } ) \cup ( 0 , b _ { 3 } )$ . Consequently,

$$
b ^ {*} = b _ {3} = \frac {1 - 1 2 c s - 9 c ^ {2} s ^ {2} + (1 + 3 c s) \sqrt {1 + 1 8 c s + 9 c ^ {2} s ^ {2}}}{3 2 c}.\tag{A21}
$$

Then, it immediately follows that $\theta _ { m } ^ { * } = 1 / 3 .$ . Plugging in all the optimal parameters in the profit function, it can be shown that the optimal profit is positive for any $s > 0$ and $c > 0 . \ \bigsqcup$

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>7.</sup> Follows directly from computing the derivatives of the equilibrium $\alpha ^ { * }$ and $b ^ { * }$ derived in Proposition 6 with respect to c and s. <sup></sup>

## Appendix B. Generalization of Model SDU<sup>+</sup> Under Complete Information

The analysis of firm’s strategies under seeding disutility model $S \bar { D } U ^ { + }$ and full information (on the seller side) can be extended to general consumer utility structures and type distributions as detailed in the next two subsections.

## B.1. General Utility Structures

In this section we explore a more general form of the utility function, where the link between customer types and WTP is moderated by a function w that is twice differentiable, with ${ \partial w / \partial \theta } > 0 , \ w ( 0 ) = 0 ,$ , and $w ( 1 ) = 1$ . Thus, if at the current moment the installed base has size , the utility perceived momentarily by a paying customer of type  is

$$
u (\theta \mid \alpha , b, p, \delta) = (b \delta - s \alpha^ {2}) w (\theta) - p.\tag{B1}
$$

The following result captures firm’s optimal strategies when $w ( \theta )$ is concave.

Proposition B1. <sub>Under</sub> $S D U ^ { + }$ and complete information, when w is concave, then the optimal strategy is the same as in Proposition 1.

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>B1.</sup> When w is concave, it can be shown that Lemma 1 still applies. Because the proof of this statement follows similar steps as the proof of Lemma 1, we omit it for brevity. Proof is available from the authors upon request. If the firm stays in the market, every customer ends up with the product and seeds go to the lowest valuation customers. Nevertheless, unlike in Lemma 1, depending on the properties of moderating function w, IR constraint does not need to be always binding for the highest-type customers at adoption time. Similar to the argument in the proof of Proposition 1, for any paying customer of type , at the moment of adoption the installed base is $\delta ( \theta , \alpha ) =$ $1 - \theta + \alpha$ . Thus, for any paying customer of type $\theta \in \left[ \alpha , 1 \right]$ the utility at the adoption moment is given by

$$
u (\theta \mid \alpha , b, p, \delta (\theta , \alpha)) = [ b (1 - \theta + \alpha) - s \alpha^ {2} ] w (\theta) - p.\tag{B2}
$$

Because w is concave, given the boundary conditions $w ( 0 ) = 0$ and $w ( 1 ) = 1$ , then it immediately follows that $w ( \theta ) \geq \theta$ for all $\theta \in \left[ 0 , 1 \right]$ . Then,

$$
\begin{array}{c} \frac {\partial u (\theta \mid \alpha , b , p , \delta (\theta , \alpha))}{\partial \theta} = - b w (\theta) + [ b (1 - \theta + \alpha) - s \alpha^ {2} ] \frac {\partial w (\theta)}{\partial \theta}, \\ \frac {\partial^ {2} u (\theta \mid \alpha , b , p , \delta (\theta , \alpha))}{\partial \theta^ {2}} = - 2 b \frac {\partial w (\theta)}{\partial \theta} \\ \qquad + [ b (1 - \theta + \alpha) - s \alpha^ {2} ] \frac {\partial^ {2} w (\theta)}{\partial \theta^ {2}} \leq 0. \end{array}
$$

Thus, perceived utility at adoption time $u ( \theta | \alpha , b , p , \delta ( \theta , \alpha ) )$ is concave in . Thus, for adoption to start and not stall at all, it is necessary and sufficient that the IR constraints hold for the extreme adopting types $\theta = 1$ and $\theta = \alpha$ . These IR constraints are

$$
\begin{array}{c} {u (\theta = 1 \mid \alpha , b, p, \delta (1, \alpha)) = (b \alpha - s \alpha^ {2}) - p \geq 0,} \\ {u (\theta = \alpha \mid \alpha , b, p, \delta (\alpha , \alpha)) = (b - s \alpha^ {2}) w (\alpha) - p \geq 0.} \end{array}
$$

Because $v ( \theta ) \geq \theta$ for all $\theta \in \left[ 0 , 1 \right]$ and $\alpha \in [ 0 , 1 ] ,$ , then it follows that $( b - s \alpha ^ { 2 } ) w ( \alpha ) \geq ( b - s \alpha ^ { 2 } ) \alpha \geq b \alpha - s \alpha ^ { 2 }$ . Because the firm is profit maximizing, the IR constraint will be binding for the highest type. We retrieve exactly the same solution as in Proposition 1. <sup></sup>

In Proposition B1, Lemma 1 continues to apply: seeds go to the lowest end of the valuation spectrum $( \mathrm { i . e . , } \breve { \theta } \in [ 0 , \alpha ^ { \ast } ) )$ and all other customers purchase the product. Proposition B1 extends our findings under the baseline model where the utility function was linear in type to more general nonlinear cases. Proposition B1 shows that under a concave moderating function w, the optimal strategy is the same as in the baseline case. Thus, the complementarity interaction between seeding and increasing the strength of network effects via social media features characterized in Proposition 2 extends to this setting as well, and the same insights apply. Similar to the analysis in §3.1, IR constraint at adoption time will be binding for the highest-type customers. Also, the majority of customers will be paying customers $( \alpha ^ { * } \leq 1 / 2 )$

## B.2. General Distribution Functions

So far we have assumed that customers are uniformly distributed. In this section we relax this assumption and consider a general customer type cumulative distribution function (cdf) F that is continuous, strictly increasing, and twice differentiable, with boundary conditions $F ( 0 ) = { \bar { 0 } }$ and $F ( 1 ) = 1 \ ( \mathrm { i . e . }$ , no atom mass concentrated at any customer types). Similar to the baseline case in §3.1, we consider $w ( \theta ) = \theta$

Although, for the very general case the optimal solution is not tractable in closed form, we are able to derive firm’s strategy for certain distribution classes as illustrated in the following result:

<sup>Proposition</sup> <sup>B2.</sup> Suppose F satisfies the following two constraints for all $\theta \in [ 0 , 1 ] \colon ( 1 ) 2 F ^ { \prime } ( \theta ) + \theta F ^ { \prime \prime } ( \theta ) \geq 0 ,$ and (2) $F ( \theta ) \overset { \cdot } { \leq } \theta$ . Then the optimal strategy $\{ \alpha ^ { * } , b ^ { * } , p ^ { * } \}$ is the same as in Proposition 1, with customers with types $\displaystyle \dot { \theta } \in [ 0 , F ^ { - 1 } ( \alpha ^ { * } ) )$ being seeded and all other customers purchasing the product.

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>B2.</sup> Again, under the very specific conditions in this proposition, results similar to the ones in Lemma 1 hold in the sense that when the firm chooses to stay in the market, it will choose a strategy such that all customers get the product (all seeds go to the lowest end of the type distribution and all other customers end up purchasing the product). Proof is omitted for brevity but available from the authors upon request. Because  denotes the seeding ratio, then under optimal strategy customers in the interval $[ 0 , \theta _ { \alpha } )$ are seeded where $F ( \theta _ { \alpha } ) \stackrel { = } { = } \alpha$

If a fraction  of the market is seeded, then seeds go to types $[ 0 , \theta _ { \alpha } )$ with $F ( \theta _ { \alpha } ) = \alpha$ . For a paying customer of type $\bar { \theta } \bar { \in } [ \theta _ { \alpha } , 1 ] ,$ , at adoption time there exists an installed base of mass $\delta ( \theta , \alpha ) = 1 - F ( \theta ) + \alpha$ . Thus, the perceived utility at adoption time is given by

$$
u (\theta \mid \alpha , b, p, \delta (\theta , \alpha)) = [ b (1 - F (\theta) + \alpha) - s \alpha^ {2} ] \theta - p.\tag{B3}
$$

Then, using the first constraint on F , we obtain

$$
\begin{array}{c} \frac {\partial u (\theta \mid \alpha , b , p , \delta (\theta , \alpha))}{\partial \theta} = - b F ^ {\prime} (\theta) \theta + [ b (1 - F (\theta) + \alpha) - s \alpha^ {2} ], \\ \frac {\partial^ {2} u (\theta \mid \alpha , b , p , \delta (\theta , \alpha))}{\partial \theta^ {2}} = - b [ 2 F ^ {\prime} (\theta) + \theta F ^ {\prime \prime} (\theta) ] \leq 0. \end{array}
$$

Thus, perceived utility at adoption time is concave in consumer type and, consequently, in order for paid adoption to start and not stall, it is necessary and sufficient that the IR constraint holds for the extreme paying customer types $\theta = 1$ and $\begin{array} { r } { \theta = \theta _ { \alpha } \mathrm { : } } \end{array}$

$$
\begin{array}{c} u (\theta = 1 \mid \alpha , b, p, \delta (1, \alpha)) = (b \alpha - s \alpha^ {2}) - p \geq 0, \\ u (\theta = \theta_ {\alpha} \mid \alpha , b, p, \delta (\theta_ {\alpha}, \alpha)) = (b - s \alpha^ {2}) \theta_ {\alpha} - p \geq 0. \end{array}
$$

Using the second constraint on F , we have $\alpha = F ( \theta _ { \alpha } ) \leq$ $\theta _ { \alpha } \leq 1$ . Then, $b \alpha - s \alpha ^ { 2 } \leq b \theta _ { \alpha } - s \alpha ^ { 2 } \leq b \alpha - s \alpha ^ { 2 } \theta _ { \alpha }$ . Consequently, when the firm maximizes profit, the IR constraint at adoption time must be binding for the highest type $\theta = 1$ . The rest of the proof is identical to the proof of Proposition 1. <sup></sup>

In general, convex cdf functions F satisfy the required criteria. Such functions describe markets where there are more high-type customers. Thus, once a few low-type customers are seeded, paid adoption can sustain momentum at the high valuation level given the distribution skewness. Also distribution functions that are sublinear, increasing, and not extremely concave on any type interval satisfy the criteria. For all such distributions, the complementarity results in Proposition 2 continue to hold as well.

## References

Aral S, Walker D (2011) Creating social contagion through viral product design: A randomized trial of peer influence in networks. Management Sci. 57(9):1623–1639.

Aral S, Muchnik L, Sundararajan A (2011) Engineering social contagions: Optimal network seeding and incentive strategies. Working paper, New York University.

Autodesk (2009) Autodesk debuts clean tech partner program. Press Release (July 21), http://www.investor.autodesk.com/ phoenix.zhtml?c=117861&p=irol-newsArticle&ID=1309750 &highlight=.

Bakos Y, Katsamakas E (2008) Design and ownership of two-sided networks: Implications for Internet platforms. J. Management Inform. Systems 25(2):171–202.

Bass MF (1969) A new product growth model for consumer durables. Management Sci. 15(5):215–227.

Biyalogorsky E, Gerstner E, Libai B (2001) Customer referral management: Optimal reward programs. Marketing Sci. 20(1):82–95.

Chen Y, Xie J (2008) Online consumer review: Word-of-mouth as a new element of marketing communication mix. Management Sci. 54(3):477–491.

Dellarocas C (2006) Strategic manipulation of Internet opinion forums: Implications for consumers and firms. Management Sci. 52(10):1577–1593.

Dhebar A, Oren SS (1985) Optimal dynamic pricing for expanding networks. Marketing Sci. 4(4):336–351.

Dhebar A, Oren SS (1986) Dynamic nonlinear pricing in networks with interdependent demand. Oper. Res. 34(3):384–394.

Forman C, Ghose A, Wiesenfeld B (2008) Examining the relationship between reviews and sales: The role of reviewer identity disclosure in electronic markets. Inform. Systems Res. 19(3):291–313.

Galeotti A, Goyal S (2009) Influencing the influencers: A theory of strategic diffusion. RAND J. Econom. 40(3):509–532.

Godes D, Mayzlin D (2009) Firm-created word-of-mouth communication: Evidence from a field test. Marketing Sci. 28(4): 721–739.

Godes D, Mayzlin D, Chen Y, Das S, Dellarocas C, Pfeiffer B, Libai B, Sen S, Shi M, Verlegh P (2005) The firm’s management of social interactions. Marketing Lett. 16(3):415–428.

Heilman CM, Bownamn D, Wright GP (2000) The evolution of brand preferences and choice behaviors of consumers new to a market. J. Marketing Res. 37(2):139–155.

Hess RL, Ganesan S, Klein MN (2003) Service failure and recovery: The impact of relationship factors on customer satisfaction. J. Acad. Marketing Sci. 31(2):127–145.

Hinz O, Hann IH, Spann M (2011) Price discrimination in e-commerce? An examination of dynamic pricing in nameyour-own-price markets. MIS Quart. 35(1):81–98.

Huppertz JW, Arenson SJ, Evans HR (1978) An application of equitiy theory to buyer-seller exchabge situations. J. Marketing Res. 15(2):250–260.

Internet World Stats (2012) World Internet usage and population statistics. Accessed September 2012, http://www .internetworldstats.com/stats.htm (as of 09/2012).

Jiang Z, Sarkar S (2009) Speed matters: The role of free software offer in software diffusion. J. Management Inform. Systems 26(3):207–239.

Kalish S (1983) Monopolist pricing with dynamic demand and production cost. Marketing Sci. 2(2):135–159.

Kuksov D (2007) Brand value in social interaction. Management Sci. 53(10):1634–1644.

Kuksov D, Xie Y (2012) Competition in a status goods market. J. Marketing Res. 49(5):609–623.

Lehmann DR, Esteban-Bravo M (2006) When giving some away makes sense to jump-start the diffusion process. Marketing Lett. 17(4):243–254.

Martin WC, Ponder N, Lueg JE (2009) Price fairness perceptions and customer loyalty in a retail context. J. Bus. Res. 62(6):588–593.

Microsoft (2008) Microsoft gives students access to technical software at no charge to inspire success and make a difference. Press Release (February 18), http://www.microsoft.com/en -us/news/press/2008/feb08/02-18GSDPR.aspx.

Niculescu MF, Whang S (2012) Codiffusion of wireless voice and data services: An empirical analysis of the Japanese mobile telecommunications market. Inform. Systems Res. 23(1):260–279.

Niculescu MF, Wu DJ (2012) Economics of free under perpetual licensing: Implications for the software industry. Working paper, Georgia Institute of Technology. http://ssrn.com/ abstract=1853603.

Novemsky N, Schweitzer ME (2004) What makes negotiators happy? The differential effects of internal and external social comparisons on negotiator satisfaction. Organ. Behav. Human Decision Processes 95(2):186–197.

Oliver RL, Shor M (2003) Digital redemption of coupons: Satisfying and dissatisfying effects of promotion codes. J. Product and Brand Management 12(2):121–134.

Robinson B, Lakhani C (1975) Dynamic price models for newproduct planning. Management Sci. 21(10):1113–1122.

Rohlfs J (1974) A theory of interdependent demand for a communications service. Bell J. Econ. Management Sci. 5(1):16–37.

Weiss TR (2000) Amazon apologizes for price-testing program that angered customers. Computerworld (September 28), http:// www.computerworld.com/s/article/51392/Amazon\_apologizes \_for\_price\_testing\_program\_that\_angered\_customers.

Wingfield N (2007) Steve Jobs offers rare apology, credit for iPhone. WSJ Online (September 7), http://online.wsj.com/article/ SB118910651781519626.html.

Xia L, Monroe KB, Cox JL (2004) The price is unfair! A conceptual framework of price fairness perceptions. J. Marketing 68(4):1–15.

Zubcsek PP, Sarvary M (2011) Advertising to a social network. Quant. Marketing Econ. 9(1):71–107.

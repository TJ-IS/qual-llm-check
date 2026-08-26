---
otero_id: 1156
otero_key: "E4W6EZYE"
title: "Pricing in C2C Sharing Platforms"
authors: "Steffen Zimmermann; Peter Angerer; Daniel Provin; Barrie R. Nault"
year: "2018"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00505"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
ISSN 1536-9323

# Pricing in C2C Sharing Platforms

Steffen Zimmermann<sup>1</sup>, Peter Angerer<sup>2</sup>, Daniel Provin<sup>3</sup>, Barrie R. Nault<sup>4</sup>

<sup>1</sup>University of Innsbruck, Austria, steffen.zimmermann@uibk.ac.at <sup>2</sup>University of Innsbruck, Austria, peter.angerer@uibk.ac.at <sup>3</sup>University of Innsbruck, Austria, daniel.provin@uibk.ac.at <sup>4</sup>University of Calgary, Canada, nault@ucalgary.ca

## Abstract

Sharing platforms such as zilok.com enable sharing of durable goods among consumers, and seek to maximize profits by charging transaction-based platform fees. We develop a model in which consumers who have heterogeneous needs concerning the use of a durable good decide whether to purchase and share (i.e., be a lender) or borrow (i.e., be a borrower), and a monopoly sharing platform determines the platform fees. We find, first, that consumers with greater need to use a durable good purchase and share, and that consumers with lesser need borrow. Second, sharing platforms maximize profits only if the supply of a durable good matches demand—that is, the market must clear in order for platform fees to be profit maximizing. Third, the market-clearing condition requires lender and borrower fees are classic strategic complements. Fourth, to maintain the market-clearing condition, sharing platforms have to increase their lender fee or decrease their borrower fee in response to increases in the sharing price, increases in usage capacity, and decreases in the purchase price of a durable good, and vice versa. These findings indicate that commonly applied one-sided pricing models in sharing platforms can be improved.

Keywords: Sharing Economy, Sharing Platforms, Durable Goods, Consumer Behavior, Platform Pricing Behavior.

Kenny Cheng was the accepting senior editor. This research article was submitted on April 30, 2016 and went through one revision.

## 1 Introduction

Consumers own a substantial amount of underutilized durable goods. For instance, in the U.S., consumers own approximately 50 million power drills, which are used on average only six to thirteen minutes until they are replaced (Botsman & Rogers, 2010). Granting other consumers access to the unused capacity of durable goods represents the underlying idea in the emerging consumer-to-consumer (C2C) sharing economy. The sharing economy is expected to grow to \$335 billion by 2025 (PwC, 2015). This rise is mainly driven by consumers who increasingly favor paying for temporary access to durable goods instead of buying and owning them (Dervojeda et al., 2013) and by C2C sharing platforms such as zilok.com, which enable the distribution of excess capacity of underutilized durable goods by giving consumers the opportunity to share them.

The C2C sharing market is characterized by four classes of participants (cf., Dervojeda et al., 2013). First are producers or retailers that sell (durable) goods to consumers and charge a purchase price. Next, lenders are consumers that purchase goods and grant other consumers temporary access to this good by charging a sharing price. On the other hand, borrowers are consumers that do not purchase, but aim to get temporary access to a durable good by paying a sharing price. Finally, sharing platforms are accessibilitybased systems that provide mediating services enabling sharing transactions between lenders and borrowers and can charge platform fees to both groups. Figure 1 illustrates the participants and their interplay in the C2C sharing market.

In the context of a C2C sharing market, we consider the commercial sharing of durable goods such as a power drill which is enabled by a C2C sharing platform such as Zilok.com. In our model lenders and borrowers maximize utility, the sharing platform maximizes profit, and we take the purchase price of the good from the producer or retailer as given. To make our analysis concrete, we use the example of sharing a power drill through a sharing platform such as Zilok.com as a running example throughout.

![](/api/attachments/E4W6EZYE/fulltext/images/014a803f20fe02fcdd2ae9a568fc32b4742fe2517b6455231fd8fecc9ba5481f.jpg)  
Figure 1. C2C Sharing Market

The objective of C2C sharing platforms is to enable sharing transactions and maximizing profits by charging a transaction-based platform fee to lenders and/or a transaction-based platform fee to borrowers. It is not sufficient to simply set optimal platform fees once. Rather, sharing platforms have to be aware of changes in external factors (i.e., factors that sharing platforms are not accountable for). Such external factors include the purchase price, which is set by producers or retailers, the sharing price, which is set by the lender, and the usage capacity (capacity hereafter) of a durable good, which can be influenced by the lender through repairing or replacing worn parts representing investments in capacity. Changes in these external factors may influence supply and demand and require consequent responses in the platform fees.

Our analysis and running example refer only to the C2C sharing part of zilok.com. There are other forms of sharing that our analysis does not cover. We do not consider altruistic sharing, commodity exchange, and gift-giving among family members and friends (Belk, 2010). Our focus is separate from the sharing of perishable goods such as food (e.g., provided by olioex.com), intangible goods such as services (e.g., transportation provided by uber.com), and digital goods such as music (e.g., provided by spotify.com). In addition, our focus is separate from luxury goods because consumers are typically not willing to share expensive and valuable goods. We also do not consider business-to-consumer (B2C) sharing enabled by B2C sharing platforms such as car2go.com.

Accordingly, we address the following research question: What is the optimal pricing behavior of C2C sharing platforms to maximize profits in response to changes in external factors?

To answer our research question, we develop a twostage model. In the first stage, a monopoly sharing platform maximizes profits by setting prices in a twosided market structure (cf., Armstrong, 2006; Rochet & Tirole, 2006; Rysman, 2009). In the second stage, we analyze the behavior of consumers that di<sub>ff</sub>er in their need to use a durable good, whereby consumers decide whether to purchase and share (i.e., be a lender) or borrow (i.e., be a borrower) to maximize their net utility (cf., Becker, 1976). In using this two-stage formulation, we are in line with Knote and Blohm (2016), who identified the understanding of multisided principles and pricing models of sharing platforms as the most important knowledge gaps in understanding the sharing economy. An innovation embedded in our formulation is that consumers decide which side of the market they are on as part of our model. This is a departure from most of the two-sided market literature, in which the participants on the two sides are predetermined.

Our analysis yields a series of results. We find, first, that consumers with a greater need to use a durable good purchase and share, and consumers with a lesser need to use borrow that good. Second, sharing platforms maximize profits only if the supply of a durable good matches demand—that is, the market must clear in order for platform fees to be profitmaximizing. Third, the market-clearing condition requires that lender and borrower fees are classic strategic complements. Fourth, to maintain the marketclearing condition, sharing platforms have to increase their lender fee or decrease their borrower fee in response to increases in the sharing price, increases in capacity, and decreases in the purchase price of a durable good, and vice versa. These findings indicate that commonly applied one-sided pricing models of sharing platforms can be improved.

We structure our work as follows: We begin by discussing the related literature to position our research question. Next, we define our notation and explain our assumptions. Subsequently, we solve our two-stage model in reverse order by first analyzing consumer behavior and then analyzing optimal pricing behavior by a monopoly sharing platform. Finally, we conclude by presenting managerial implications and discussing implications for future research.

## 2 Related Literature

We structure this section according to our analysis sequence by first discussing articles that investigate consumer behavior in the sharing economy and then discussing articles that analyze sharing platform behavior. Of course, there are articles that address other aspects of the sharing economy, such as the consequences of the sharing economy on traditional firms (e.g., Cusumano, 2015; Malhotra & Van Alstyne, 2014; Zervas, Proserpio, & Byers, 2014). We do not cover this literature as it is unrelated to our model and contribution.

## 2.1 Consumer Behavior

Belk (2007) argues that sharing can foster communities, save resources, and create synergies for consumers. Furthermore, in describing cost savings as the main motive, the article draws a comparison to companies that increasingly outsource operations in order to lower costs, and argues that, for similar reasons, consumers will increasingly share their owned goods to reduce their total costs of ownership. Botsman and Rogers (2010) also argue that bedsides the advantage to consumers of saving money, sharing lowers environmental damage and encourages the development of better products. Phipps et al. (2013) introduce a conceptual framework based on social cognitive theory, and argue that besides saving money, consumers receive further benefits from the sharing economy, such as community building of like-minded people and the emergence of sustainable spaces to meet. Sundararajan (2016) depicts a broad and visionary picture of the sharing economy as “crowdbased capitalism,” making the point that sharing will lead to higher utilization of product capacity and that the complex microstructure of the sharing economy requires a set of models. Moehlmann (2015) studies data from airbnb.com and finds that the likelihood of choosing a sharing option is predominantly determined by users’ self-benefit and cost savings, whereas environmental considerations are negligible. Bearing in mind the different motives that drive consumers to participate in the sharing economy, we focus on cost savings since this is the most widely agreed upon reason for participating in the C2C sharing market.

Matzner, Chasin, and Todenhoefer (2015) present an empirical study based on the theory of planned behavior in which they represent lenders and borrowers as part of the same consumer group and acknowledge that consumers can independently decide how they participate in the C2C sharing market. We follow this view of consumers in our model whereby consumers choose whether to lend or borrow endogenously. Chen (2009) empirically studies the needs and perceived values of art consumers and finds that art collectors and exhibit visitors differ in their need to consume art leading to different consumer groups namely, ownership for the art collector and access for the exhibit visitor. Accordingly, we consider consumers who di er in their need to use a durable good, and our model confirms Chen’s (2009) finding that consumers with greater need aim to own rather than simply access a durable good.

Lamberton and Rose (2012) draw from three di<sub>ff</sub>erent studies and empirically find that the rational consumer utility model is applicable to commercial sharing. Thus, we use rational consumer behavior to inform our model. Fraiberger and Sundararajan (2015) build a theoretical model for peer-to-peer sharing of durable goods in which consumers are also allowed to trade their durable goods through secondary markets. They calibrate their model with data from the U.S. automobile industry and transaction data of the car sharing platform getaround.com. The results show a decrease in ownership but increase in utilization and consumer welfare due to the availability of a sharing market: below-median-income consumers have a significantly higher improvement in welfare and also provide a majority of the sharing supply. Mueller (2014) theorizes about the behavior of consumers participating in the C2C sharing market and considers consumers that are heterogeneous in the value gained from using a durable good. We adopt this model setup as our starting point, and analyze the implications of consumer behavior on platform pricing behavior.

## 2.2 Platform Behavior

Einav, Farronanto, and Levin (2016) find that successful platforms need to set the sharing price to balance demand and supply. They argue that auctions may be suitable because they allow prices to respond to market conditions, but also that consumers tend to be less interested in auctions now than they were fifteen years ago. As a result, Einav et al. (2016) call for simpler pricing mechanisms that make use of available information that can e<sub>l</sub>ectively substitute for auctions. Moreover, on most sharing platforms, the sharing price is set by the lender rather than the platform. In contrast to Einav et al. (2016), we analyze and find pricing mechanisms for platform fees instead of the sharing price to balance supply and demand for maximizing profit. Weber (2014) analyzes how a sharing platform can eliminate moral hazard between lenders and borrowers. In the collaborative housing market, where heterogeneous borrowers and vertically di<sub>ff</sub>erentiated lenders (in terms of housing quality) can use airbnb.com as a sharing platform to increase matching probability, the sharing platform o<sub>ff</sub>ers a form of insurance that requires borrowers to make a deposit and gives lenders the ability to file claims if damage occurs. Weber (2014) assumes that the sharing platform, in turn, charges symmetric platform fees to lenders and borrowers for the mediating services, and finds that if all participants are risk neutral, then the sharing platform can cover all lenders’ claims while providing incentives to borrowers to behave as lenders would if they were using their own space.

The literature discussed above is summarized in Table 1 according to content and method.

<table><tr><td colspan="3">Table 1. Related Literature</td></tr><tr><td>ContentMethod</td><td>Consumer behavior</td><td>Platform behavior</td></tr><tr><td>Descriptive/conceptual</td><td>Belk (2007)Botsman &amp; Rogers (2010)Phipps et al. (2013)Sundararajan (2016)</td><td>Einav et al. (2016)</td></tr><tr><td>Empirical</td><td>Moehlmann (2015)Matzner et al. (2015)Chen (2009)Lamberton &amp; Rose (2012)</td><td></td></tr><tr><td>Theoretical</td><td>Fraiberger &amp; Sundararajan (2015) Mueller (2014)</td><td>Weber (2014)</td></tr></table>

Our literature review on the sharing economy found that consumer behavior is investigated more extensively than platform behavior—only Weber (2014) theoretically analyzes platform behavior as we do in the context of a C2C sharing market. In contrast to that work, our formulation presumes potentially asymmetric platform fees, which allows us to operationalize the concept of subsidizing one side over the other, which is common in the two-sided platforms literature (cf., Caillaud & Jullien, 2003; Eisenmann, Parker, & Van Alstyne, 2006; Rysman, 2009). Moreover, we focus on the directional changes in platform pricing as a response to changing external factors, such as changes in the durable good’s purchase price and capacity. Our model further applies to C2C sharing platforms for durable goods in general and abstracts from a specific platform or product. We further abstract from specific utility functions, using a reduced-form utility function for lenders and borrowers, allowing us to develop more general results. In doing so, we show how sharing platforms can dynamically maximize profits by adapting their platform fees based on changes in external factors.

The structure of our model is related to that of Brock and Evans (1985) in which individual entrepreneurs make production decisions and a policy maker decides on a tax schedule to maximize welfare. Our model is also related to studies by Nault (1996) and Levi and Nault (2004) in which firms decide whether to convert to a new technology and a policy maker offers di<sub>ff</sub>erent tax regimes that impact firms’ choices of whether to convert. The essential differences in our model are that we have consumers that decide on whether to purchase and share, or borrow a durable good, rather than firms that decide between technologies. Moreover, we consider a sharing platform that decides on platform fees to maximize profits instead of a policy maker that decides on tax schedules. Finally, and most importantly, we consider a two-sided market, where di<sub>ff</sub>ering platform fees can be charged to lenders and to borrowers.

Two-sided markets are usually characterized by strong network externalities, which in a winner-take-all setting often result in a monopoly platform (cf., Eisenmann et al., 2006; Rysman, 2009). Accordingly, we treat the sharing platform as a monopoly in our model, and abstract from the conditions that may have led to the platform being a monopoly. A monopoly setting is reasonable because two-sided platforms do not face diminishing returns when growing beyond a certain point as lenders usually benefit from a large number of borrowers and vice versa. This leads to winner-take-all market consolidations featuring a single platform that serves almost the entire market. Such market consolidations have taken place in other twosided markets such as online social networking with Facebook, online auctions with eBay, and web search with Google being the dominant platforms (Eisenmann et al., 2006).

Nevertheless, the challenge for two-sided platforms to be successful is to get both sides of the market (in our case, borrowers and lenders) on board (Rochet & Tirole, 2006). This can be achieved by platform pricing behavior that accounts for externalities on both sides. Pricing in two-sided markets includes the opportunity of (relative) subsidizing one side over the other (cf., Armstrong, 2006; Caillaud & Jullien, 2003; Eisenmann et al., 2006; Rysman, 2009). Such pricing strategies can compensate di erent price elasticities (Rysman, 2009) and di<sub>ff</sub>erent numbers of participants on both sides (Eisenmann et al., 2006), consequently impacting overall transaction volume and platform profits (Lee & Wu 2009). In our model, we allow for asymmetric pricing as well as di<sub>ff</sub>erent price elasticities for supply and demand of a durable good.

## 3 Notation and Assumptions

Our assumptions pertain to a number of di erent factors relating to consumer heterogeneity, consumer utility, and platform fees.

We consider consumers that participate in the C2C sharing market. For these consumers, it is economically worthwhile to either purchase and share or borrow a durable good. We exclude consumers that are willing neither to purchase nor to borrow a durable good or who prefer outside options such as face-toface sharing between friends and family members or other alternatives. Our first assumption concerns those consumers that participate in the C2C sharing market.

## Assumption 1: Consumer heterogeneity: Consumers di<sub>ff</sub>er in their need to use a durable good.

Consistent with Alba et al. (1997), we assume that consumers are heterogeneous in their need to use a durable good and denote consumers as <sub>??</sub> , which is normalized in the interval [0,1]. Thus, $f ( \theta ) > 0 \forall \theta \in$ $[ 0 , 1 ] , F ( 0 ) = 0$ and $F ( 1 ) = 1 ~ . ~ \theta$ represents an increasing need to use a durable good, such that consumers with $\theta = 0$ are those with the lowest need, and consumers with $\theta = 1$ are those with the greatest need. <sub>??</sub> is taken to be uniformly distributed over its range. This incurs little loss of generality as <sub>??</sub> can be scaled as needed.

In our running example of sharing a power drill, a consumer with a greater need to use a power drill (high <sub>??</sub>) could be an individual that enjoys artisanal work at home (handy-person hereafter). A consumer with less need to use a power drill (low <sub>??)</sub> could be an individual that dislikes doing artisanal work at home (non-handy-person hereafter).

The amount of time consumers aim to use a durable good is denoted by $x \in [ 0 , { \bar { x } } ]$ with the subscript L for the own usage time of lenders and with the subscript B for the demand usage time of borrowers. The amount of time a lender aims to share a durable good is called supplied usage time and is denoted by $y \in [ 0 , \bar { x } ]$ . As borrowers would typically maximize the usage of a durable good in the available time, the amount of time a lender actually shares a durable good (i.e., shared usage time) is equal to the actual usage time of the durable good by borrowers. Otherwise, borrowers would just be paying for the availability of the durable good without using it. <sub>??</sub> and <sub>??</sub> are bounded from below, because using a durable good for a negative time is infeasible; they are bounded from above by the durable good’s usage capacity <sub>??</sub>̅. For example, a power drill typically fails after a specific number of operating hours. The durable good considered for sharing in our model is homogeneous (not vertically di erentiated) and represents the best economic choice with a minimum price/performance ratio $( p _ { P } / \bar { x } )$ out of different products of a product type such as power drills. This means that a consumer would decide whether to purchase and share or borrow the power drill with the best ratio between purchase price and capacity.

The monetary utility of a consumer depends on the need to use a durable good, <sub>??</sub>, and the usage time <sub>??</sub> (i.e., own usage time, $x _ { L }$ , for lenders or demanded usage time, $x _ { B } ,$ for borrowers). We denote this utility by a reduced-form utility function $U ( \theta , x )$ , which is bounded from below $U ( \theta , 0 ) = 0$ We take a consumer’s utility as increasing in the need to use a durable good, and increasing and concave in the usage time to its capacity <sub>??</sub>̅. The latter represents the standard assumption of decreasing marginal utility.

Assumption 2: Consumer utility:

$$
\frac {\partial U (\theta , x)}{\partial \theta} > 0, \frac {\partial U (\theta , x)}{\partial x} > 0, a n d \frac {\partial^ {2} U (\theta , x)}{\partial x ^ {2}} <   0.
$$

For example, the utility gained from using a power drill is higher for a handy-person as compared to a nonhandy-person. Moreover, the utility from using a power drill increases in the usage time while the marginal utility from using the power drill decreases because a consumer typically drills the more important holes before the less important ones and the drill wears out through usage.

Given the nature of the consumer’s utility function, there is a relationship between the usage time and the consumer’s need to use a durable good. This crosse ect is fundamental to the results in that a consumer’s marginal utility is increases with the need to use a durable good.

Assumption 3: Cross-e<sub>ff</sub>ect:

$$
\frac {\partial^ {2} U (\theta , x)}{\partial x \partial \theta} > 0.
$$

For our example, this means that a handy-person experiences a higher marginal utility from using a power drill than a non-handy-person.

Consumers in the C2C sharing market can either purchase and share, or borrow a durable good. Lenders purchase a durable good for a purchase price, $p _ { P } \in R ^ { + }$ and charge borrowers a sharing price per unit of shared usage time, $p _ { S } \in R ^ { + }$

The mediating services to connect lenders and borrowers are provided by a monopoly sharing platform (e.g., Eisenmann et al., 2006; Rysman, 2009). The monopoly platform is limited to intermediation: it does not compete with traditional firms outside the domain of sharing such as is the case with airbnb.com that competes with the hotel industry. As stated earlier, we consider consumers for whom participating in the C2C sharing market is economically worthwhile, and for these consumers there is no alternative C2C sharing platform on which they could share a durable good.

## Assumption 4: Platform fees: The monopoly sharing platform sets nonnegative transaction-based platform fees to lenders and borrowers.

To maximize profits, the sharing platform sets a transaction-based lender fee, $s _ { L } \in [ 0 , p _ { S } ]$ , and a transaction-based borrower fee, $s _ { B } \in [ 0 , p _ { P } ]$ (cf., Armstrong, 2006). The lender fee is limited by $p _ { S }$ because with a lender fee greater than the sharing price, no lender would have an incentive to share a durable good. The borrower fee is limited by $p _ { P }$ because with a borrower fee greater than the purchase price, all borrowers would purchase the durable good. These weakly positive transaction-based fees allow for subsidizing one group over the other to compensate di<sub>ff</sub>erent numbers of lenders and borrowers and di erent price elasticities (cf., Caillaud & Jullien, 2003; Eisenmann et al., 2006; Rysman, 2009). We do not allow for negative fees (i.e., subsidizing lenders and/or borrowers for making sharing transactions via the sharing platform) because the sharing platform must cover fixed costs $C \in R ^ { + }$ for providing the mediating services and we do not observe any sharing platform operating in the sharing market that currently charges negative fees. This indicates that sharing platforms have to generate revenue from charging positive platform fees, $s _ { L } + s _ { B } \in R ^ { + }$ , in order to be profitable.

In practice, sharing platforms charge a percent-ofvalue lender fee and/or a percent-of-value borrower fee, which represent a percentage rate of the total sharing price $( p _ { S } * \operatorname* { m i n } \{ y , x _ { B } \}$ in our model). Hence, in such implemented pricing models, platform fees increase in the sharing price and in the shared usage time. In contrast, as our basic pricing model, we intentionally use unit transaction fees, which only increase in the shared usage time. We do this in order to examine whether commonly applied percent-ofvalue platform fees are profit maximizing or whether they can be replaced by a better pricing model.

## 4 Model Set-Up

We set up our C2C sharing market model as a twostage model. In the first stage, the monopoly sharing platform sets transaction-based platform fees to borrowers and lenders. In the second stage, consumers maximize their net utility by deciding to be a lender or a borrower based on their individual needs and the resulting expected own or demanded usage time of a durable good. In our two-stage model, we work backwards and examine consumer behavior first and platform pricing second.

## 4.1 Consumer Behavior

## 4.1.1 Borrowers

For a borrower, the net utility $\phi _ { B }$ includes the sharing price paid to the lender and the borrower fee paid to the sharing platform:

$$
\phi_ {B} = U (\theta , x _ {B}) - p _ {S} * x _ {B} - s _ {B} * x _ {B} > 0,\tag{1}
$$

where we subscript the borrower-specific variables with . We take $U ( \theta , x _ { B } > 0 )$ is sufficiently large to make (1) positive for all borrowers. Otherwise, borrowers would not borrow and consequently not participate in the C2C sharing market. For borrowers, the first-order condition by choice of demanded usage time is

$$
\begin{array}{r} \frac {\partial \phi_ {B}}{\partial x _ {B}} = \frac {\partial U (\theta , x _ {B})}{\partial x _ {B}} - p _ {S} - s _ {B} = 0 \\ = \omega (\theta , x _ {B}, p _ {S}, s _ {B}), \end{array}\tag{2}
$$

where $\omega ( \theta , x _ { B } , p _ { S } , s _ { B } )$ implicitly defines the optimal value function $x _ { B } ( \theta , p _ { S } , s _ { B } )$ Lemma 1 describes the behavior of $x _ { B } ( \theta , p _ { S } , s _ { B } )$

Lemma 1: For borrowers, the demanded usage time is increasing in their need to use a durable good and is decreasing in the sharing price and the borrower fee.

Proof: From Assumption 3, we have

$$
\frac {\partial \omega (\theta , x _ {B} , p _ {S} , s _ {B})}{\partial \theta} = \frac {\partial^ {2} U (\theta , x _ {B})}{\partial x _ {B} \partial \theta} > 0.
$$

The sign of the second-order condition follows directly from Assumption 2 and is

$$
\frac {\partial \omega (\theta , x _ {B} , p _ {S} , s _ {B})}{\partial x _ {B}} = \frac {\partial^ {2} U (\theta , x _ {B})}{\partial x _ {B} ^ {2}} <   0.
$$

Directly from the implicit function rule, we have

$$
\begin{array}{r} \frac {\partial x _ {B}}{\partial \theta} = - \frac {\partial \omega (\theta , x _ {B} , p _ {S} , s _ {B}) / \partial \theta}{\partial \omega (\theta , x _ {B} , p _ {S} , s _ {B}) / \partial x _ {B}} \\ = - \frac {\partial^ {2} U (\theta , x _ {B}) / \partial x _ {B} \partial \theta}{\partial^ {2} U (\theta , x _ {B}) / \partial x _ {B} ^ {2}} > 0, \end{array}
$$

$$
\begin{array}{r} \frac {\partial x _ {B}}{\partial p _ {S}} = - \frac {\partial \omega (\theta , x _ {B} , p _ {S} , s _ {B}) / \partial p _ {S}}{\partial \omega (\theta , x _ {B} , p _ {S} , s _ {B}) / \partial x _ {B}} \\ = - \frac {- 1}{\partial^ {2} U (\theta , x _ {B}) / \partial x _ {B} ^ {2}} <   0, \end{array}
$$

$$
\begin{array}{r} \frac {\partial x _ {B}}{\partial s _ {B}} = - \frac {\partial \omega (\theta , x _ {B} , p _ {S} , s _ {B}) / \partial s _ {B}}{\partial \omega (\theta , x _ {B} , p _ {S} , s _ {B}) / \partial x _ {B}} \\ = - \frac {- 1}{\partial^ {2} U (\theta , x _ {B}) / \partial x _ {B} ^ {2}} <   0. \end{array}
$$

Q.E.D.

In our running example Lemma 1 implies that a handyperson (high <sub>??</sub>) that borrows a power drill aims to use the drill for a longer time compared to a borrower that dislikes artisanal work (low <sub>??</sub> ). Moreover, borrowers increase their demanded usage time with a decreasing sharing price and a decreasing borrower fee they have to pay when borrowing a power drill.

The effects on $x _ { B }$ in the proof of Lemma 1 represent the borrowers’ individual elasticities of demand for sharing a durable good. We refer to these elasticities later.

## 4.1.2 Lenders

For a lender, the net utility $\phi _ { L }$ includes the sharing price received from the borrower, the lender fee paid to the sharing platform, and the purchase price paid to own the durable good:

$$
\begin{array}{c} \phi_ {L} = U (\theta , x _ {L}) + p _ {S} * y - s _ {L} * y - p _ {P} > 0, \\ s. t. x _ {L} + y \leq \overline {{x}}, \end{array}\tag{3}
$$

where we subscript the lender-specific variables with . We take $U ( \theta , x _ { L } > 0 )$ to be sufficiently large so that, together with $p _ { S } * y , ( 3 )$ is positive for all lenders. Otherwise, lenders would not purchase and share a durable good, and consequently would not participate in the C2C sharing market. In order to maximize the net utility subject to the inequality constraint by choice of the two independent variables $x _ { L }$ and $y ,$ we apply the Karush-Kuhn-Tucker (KKT) theorem (cf., Boyd & Vandenberghe, 2004). The Lagrange function and its first-order conditions are

$$
\begin{array}{r} L = U (\theta , x _ {L}) + p _ {S} * y - s _ {L} * y - p _ {P} \\ - \lambda_ {1} [ x _ {L} + y - \bar {x} ], \end{array}
$$

$$
\frac {\partial L}{\partial x _ {L}} = \frac {\partial U (\theta , x _ {L})}{\partial x _ {L}} - \lambda_ {1},\tag{4}
$$

$$
\frac {\partial L}{\partial y} = p _ {S} - s _ {L} - \lambda_ {1},\tag{5}
$$

and we have the associated KKT conditions

$$
\begin{array}{c} {(i) \frac {\partial L}{\partial x _ {L}} = 0, (i i) \frac {\partial L}{\partial y} = 0,} \\ {(i i i) x _ {L} + y \leq \bar {x}; \lambda_ {1} \geq 0; \lambda_ {1} [ x _ {L} + y - \bar {x} ] = 0.} \end{array}
$$

Lemma 2 describes the extent by which the capacity of a durable good is exploited by lenders.

Lemma 2: Lenders fully exploit the usage capacity of a durable good to maximize their net utility.

Proof: To find a solution we consider whether the constraint in (3) is binding. Suppose $x _ { L } + y < \bar { x } .$ . From KKT condition (iii) it follows that $\lambda _ { 1 } = 0$ and from Assumption 2 it follows that $\partial L / \partial x _ { L } > 0$ Consequently, KKT condition (i) is violated. Now suppose $x _ { L } + y = \bar { x }$ . From KKT condition (iii) it follows that $\lambda _ { 1 } > 0$ <sub>.</sub> Consequently, KKT condition (i) and (ii) can be fulfilled and this case represents a valid solution. Q.E.D.

In our running example Lemma 2 means that lenders of a power drill maximize their net utility if they either use or share their power drill to its capacity (or until the power drill breaks).

Setting (4) and (5) to zero, rearranging (5) and inserting into (4) we have

$$
\begin{array}{r} \frac {\partial U (\theta , x _ {L})}{\partial x _ {L}} - [ p _ {S} - s _ {L} ] = 0 \\ = \psi (\theta , x _ {L}, p _ {S}, s _ {L}), \end{array}\tag{6}
$$

where $\psi ( \boldsymbol { \theta } , x _ { L } , p _ { S } , s _ { L } )$ implicitly defines the optimal value function $x _ { L } ( \theta , p _ { S } , s _ { L } )$ . Lemma 3 describes the behavior of $x _ { L } ( \theta , p _ { S } , s _ { L } )$

Lemma 3: For lenders, the own usage time is increasing in their need to use a durable good, decreasing in the sharing price, and increasing in the lender fee.

Proof: From Assumption 2 we have

$$
\frac {\partial \psi (\theta , x _ {L} , p _ {S} , s _ {L})}{\partial x _ {L}} = \frac {\partial^ {2} U (\theta , x _ {L})}{\partial x _ {L} ^ {2}} <   0.
$$

From Assumption 3 we have

$$
\frac {\partial \psi (\theta , x _ {L} , p _ {S} , s _ {L})}{\partial \theta} = \frac {\partial^ {2} U (\theta , x _ {L})}{\partial x _ {L} \partial \theta} > 0.
$$

Directly from the implicit function rule, we have

$$
\begin{array}{r l} & {\frac {\partial x _ {L}}{\partial \theta} = - \frac {\partial \psi (\theta , x _ {L} , p _ {S} , s _ {L}) / \partial \theta}{\partial \psi (\theta , x _ {L} , p _ {S} , s _ {L}) / \partial x _ {L}}} \\ & {\qquad \qquad \qquad \qquad \qquad = - \frac {\partial^ {2} U (\theta , x _ {L}) / \partial x _ {L} \partial \theta}{\partial^ {2} U (\theta , x _ {L}) / \partial x _ {L} ^ {2}} > 0,} \\ & {\frac {\partial x _ {L}}{\partial p _ {S}} = - \frac {\partial \psi (\theta , x _ {L} , p _ {S} , s _ {L}) / \partial p _ {S}}{\partial \psi (\theta , x _ {L} , p _ {S} , s _ {L}) / \partial x _ {L}} = - \frac {- 1}{\partial^ {2} U (\theta , x _ {L}) / \partial x _ {L} ^ {2}}} \\ & {\qquad \qquad \qquad <   0,} \\ & {\frac {\partial x _ {L}}{\partial s _ {L}} = - \frac {\partial \psi (\theta , x _ {L} , p _ {S} , s _ {L}) / \partial s _ {L}}{\partial \psi (\theta , x _ {L} , p _ {S} , s _ {L}) / \partial x _ {L}} = - \frac {1}{\partial^ {2} U (\theta , x _ {L}) / \partial x _ {L} ^ {2}}} \\ & {\qquad \qquad \qquad > 0.} \end{array}
$$

Q.E.D.

In our running example Lemma 3 implies that a handyperson (high <sub>??</sub>) that purchases and shares a power drill, uses the drill for a longer time than a non-handy-person (low <sub>??</sub>). Moreover, lenders increase their own usage time of the power drill with a lower sharing price they receive from the borrowers and with a greater lender fee.

In order to determine the optimal supplied usage time, we use Lemma 2 and (6) to get

$$
\begin{array}{r l} & {\bar {x} = x _ {L} (\theta , p _ {S}, s _ {L}) + y} \\ & {\qquad \Rightarrow \bar {x} - \frac {\partial U (\theta , x _ {L})}{\partial x _ {L}}} \\ & {\qquad + [ p _ {S} - s _ {L} ] - y = 0} \\ & {\qquad = \delta (\theta , \bar {x}, y, p _ {S}, s _ {L}),} \end{array}\tag{7}
$$

where $\delta ( \theta , \bar { x } , y , p _ { S } , s _ { L } )$ implicitly defines the optimal value function $y ( \theta , \bar { x } , p _ { S } , s _ { L } )$ . Lemma 4 describes the behavior of $y ( \theta , \bar { x } , p _ { S } , s _ { L } )$

Lemma 4: For lenders, the supplied usage time is decreasing in their need to use a durable good, is decreasing with the lender fee, is increasing with the sharing price, and is increasing with capacity.

Proof: From Assumption 3 we have

$$
\frac {\partial \delta (\theta , \bar {x} , y , p _ {S} , s _ {L})}{\partial \theta} = - \frac {\partial^ {2} U (\theta , x _ {L})}{\partial x _ {L} \partial \theta} <   0.
$$

Directly from the implicit function rule, we have

$$
\begin{array}{r l r} & & {\frac {\partial y}{\partial \theta} = - \frac {\partial \delta (\theta , \bar {x} , y , p _ {S} , s _ {L}) / \partial \theta}{\partial \delta (\theta , \bar {x} , y , p _ {S} , s _ {L}) / \partial y}} \\ & & {= - \frac {- \partial^ {2} U (\theta , x _ {L}) / \partial x _ {L} \partial \theta}{- 1} <   0,} \\ & & {\frac {\partial y}{\partial \bar {x}} = - \frac {\partial \delta (\theta , \bar {x} , y , p _ {S} , s _ {L}) / \partial \bar {x}}{\partial \delta (\theta , \bar {x} , y , p _ {S} , s _ {L}) / \partial y} = - \frac {1}{- 1} > 0,} \\ & & {\frac {\partial y}{\partial p _ {S}} = - \frac {\partial \delta (\theta , \bar {x} , y , p _ {S} , s _ {L}) / \partial p _ {S}}{\partial \delta (\theta , \bar {x} , y , p _ {S} , s _ {L}) / \partial y} = - \frac {1}{- 1} > 0,} \\ & & {\frac {\partial y}{\partial s _ {L}} = - \frac {\partial \delta (\theta , \bar {x} , y , p _ {S} , s _ {L}) / \partial s _ {L}}{\partial \delta (\theta , \bar {x} , y , p _ {S} , s _ {L}) / \partial y} = - \frac {- 1}{- 1} <   0.} \end{array}
$$

Q.E.D.

In our running example, Lemma 4 implies that a nonhandy-person (low <sub>??</sub>) aims to share their own power drill for a longer time than a handy-person (high <sub>??</sub>). Moreover, lenders increase their supplied usage time with higher power drill capacity, with a higher sharing price they receive from borrowers, and with a lower lender fee paid to the sharing platform.

The e<sub>ff</sub>ects on <sub>??</sub> in the proof of Lemma 4 represent the lenders’ individual elasticities of supply for sharing a durable good. We refer to these elasticities later.

## 4.1.3 Indifferent consumer

Consumers maximize their net utility by deciding whether to purchase and share or borrow a durable good. That is,

$$
\begin{array}{r l} & {\max \{U (\theta , x _ {L} (\theta , p _ {S}, s _ {L})) + p _ {S} * y (\theta , \bar {x}, p _ {S}, s _ {L}) -} \\ & {\qquad s _ {L} * y (\theta , \bar {x}, p _ {S}, s _ {L}) - p _ {P},} \\ & {\qquad U (\theta , x _ {B} (\theta , p _ {S}, s _ {B})) - p _ {S} * x _ {B} (\theta , p _ {S}, s _ {B}) -} \\ & {\qquad s _ {B} * x _ {B} (\theta , p _ {S}, s _ {B}) \}.} \end{array}
$$

We use Lemma 2 to substitute $y \big ( \tilde { \theta } , \bar { x } , p _ { S } , s _ { L } \big )$ with $\bar { x } -$ $x _ { L } \big ( \widetilde { \theta } , p _ { S } , s _ { L } \big )$ and identify the consumer that is indifferent between purchasing and sharing, and borrowing, ${ \widetilde { \theta } } ,$ by

$$
\begin{array}{r l r} & & U (\widetilde {\theta}, x _ {L} (\widetilde {\theta}, p _ {S}, s _ {L})) + p _ {S} \\ & & * [ \bar {x} - x _ {L} (\widetilde {\theta}, p _ {S}, s _ {L}) ] \\ & & - s _ {L} * [ \bar {x} - x _ {L} (\widetilde {\theta}, p _ {S}, s _ {L}) ] - p _ {P} \\ & & - U (\widetilde {\theta}, x _ {B} (\widetilde {\theta}, p _ {S}, s _ {B})) + p _ {S} * x _ {B} (\widetilde {\theta}, p _ {S}, s _ {B}) + \\ & & s _ {B} * x _ {B} (\widetilde {\theta}, p _ {S}, s _ {B}) = 0 \\ & & = \Lambda (\widetilde {\theta}, p _ {S}, s _ {L}, \bar {x}, p _ {P}, s _ {B}), \end{array}\tag{8}
$$

where $\varLambda \bigl ( \widetilde { \theta } , p _ { S } , s _ { L } , \bar { x } , p _ { P } , s _ { B } \bigr )$ implicitly defines the indifferent consumer $\widetilde { \theta ( } p _ { S } , s _ { L } , \bar { x } , p _ { P } , s _ { B } )$ . We use <sub>(∙)</sub> for $( p _ { S } , s _ { L } , \bar { x } , p _ { P } , s _ { B } )$ in the following arguments to simplify and shorten our notation.

Our first theorem defines the separation of consumers into those that borrow and those that purchase and share.

Theorem 1: Consumers with a greater need purchase and share (i.e., are lenders), and consumers with a lesser need borrow (i.e., are borrowers).

Proof: By totally differentiating (8), we get

$$
\begin{array}{r l} & {\frac {\partial \varLambda}{\partial \widetilde {\theta}} = \frac {\partial U (\widetilde {\theta} , x _ {L} (\widetilde {\theta} , p _ {S} , s _ {L}))}{\partial \widetilde {\theta}} +} \\ & {\qquad \frac {\partial U (\widetilde {\theta} , x _ {L} (\widetilde {\theta} , p _ {S} , s _ {L}))}{\partial x _ {L}} * \frac {\partial x _ {L} (\widetilde {\theta} , p _ {S} , s _ {L})}{\partial \widetilde {\theta}}} \\ & {\qquad - p _ {S} * \frac {\partial x _ {L} (\widetilde {\theta} , p _ {S} , s _ {L})}{\partial \widetilde {\theta}} + s _ {L} * \frac {\partial x _ {L} (\widetilde {\theta} , p _ {S} , s _ {L})}{\partial \widetilde {\theta}}} \\ & {\qquad - \frac {\partial U (\widetilde {\theta} , x _ {B} (\widetilde {\theta} , p _ {S} , s _ {B}))}{\partial \widetilde {\theta}}} \\ & {\qquad - \frac {\partial U (\widetilde {\theta} , x _ {B} (\widetilde {\theta} , p _ {S} , s _ {B}))}{\partial x _ {B}} * \frac {\partial x _ {B} (\widetilde {\theta} , p _ {S} , s _ {B})}{\partial \widetilde {\theta}}} \\ & {\qquad + p _ {S} * \frac {\partial x _ {B} (\widetilde {\theta} , p _ {S} , s _ {B})}{\partial \widetilde {\theta}} + s _ {B} * \frac {\partial x _ {B} (\widetilde {\theta} , p _ {S} , s _ {B})}{\partial \widetilde {\theta}}.} \end{array}
$$

Rearranging and cancelling terms and using the optimality conditions defined in (2) and (6), we have

$$
\begin{array}{c} \frac {\partial \varLambda}{\partial \widetilde {\theta}} = \frac {\partial U (\widetilde {\theta} , x _ {L} (\widetilde {\theta} , p _ {S} , s _ {L}))}{\partial \widetilde {\theta}} \\ - \frac {\partial U (\widetilde {\theta} , x _ {B} (\widetilde {\theta} , p _ {S} , s _ {B}))}{\partial \widetilde {\theta}}. \end{array}\tag{9}
$$

From Assumption 2, it follows that both terms on the right hand side of (9) are positive. For $s _ { L } = s _ { B } = 0$ , the first term equals the second term and consequently (9) equals zero. We excluded this case from our analysis directly after Assumption 4 because the platform would not cover its fixed cost. Starting from $s _ { L } = s _ { B } =$ <sub>0</sub> and using Lemma 1 and Lemma 3, a marginal increase of $s _ { B }$ results in a marginal decrease of $x _ { B } ( \widetilde { \theta } , p _ { S } , s _ { B } )$ and a marginal increase of $s _ { L }$ results in a marginal increase of $x _ { L } \big ( \widetilde { \theta } , p _ { S } , s _ { L } \big )$ . The resulting difference $x _ { L } \big ( \widetilde { \theta } , p _ { S } , s _ { L } \big ) - x _ { B } ( \widetilde { \theta } , p _ { S } , s _ { B } )$ is positive. Treating this difference as small, $x _ { L } ( \widetilde { \theta } , p _ { S } , s _ { L } ) -$ $x _ { B } ( \widetilde { \theta } , p _ { S } , s _ { B } )$ represents a marginal increase in <sub>??</sub> . Thus, (9) represents the change in the marginal utility with an increasing need to use of the indi erent consumer which can be rewritten as $\partial A / \partial \tilde { \theta } =$ $\partial ^ { 2 } U ( \tilde { \theta } , x ) / \partial x \partial \tilde { \theta }$ . This term is positive from Assumption 3. Q.E.D.

In our running example, Theorem 1 implies that consumers with a lesser need to use a power drill borrow and consumers with a greater need purchase and share the power drill.

Lemma 5 determines the e<sub>ff</sub>ects of the purchase price, the platform fees, the sharing price, and capacity on the indifferent consumer.

Lemma 5: The proportion of borrowers increases in the purchase price, decreases in the borrower fee, increases in the lender fee, decreases in the sharing price, and decreases in capacity.

Proof: Using Lemma 2 and totally di<sub>ff</sub>erentiating (8) with respect to $p _ { P } , s _ { B } , s _ { L } , p _ { S }$ , and <sub>??</sub>̅, cancelling terms, using the optimality conditions of (2) and (6), and using the implicit function rule, we have

$$
\begin{array}{c} \frac {\partial \tilde {\theta} (\cdot)}{\partial p _ {P}} = - \frac {\partial \Lambda / \partial p _ {P}}{\partial \Lambda / \partial \tilde {\theta}} = - \frac {- 1}{\partial \Lambda / \partial \tilde {\theta}} > 0, \\ \frac {\partial \tilde {\theta} (\cdot)}{\partial s _ {B}} = - \frac {\partial \Lambda / \partial s _ {B}}{\partial \Lambda / \partial \tilde {\theta}} = - \frac {x _ {B} (\widetilde {\theta} , p _ {S} , s _ {B})}{\partial \Lambda / \partial \tilde {\theta}} <   0, \\ \frac {\partial \tilde {\theta} (\cdot)}{\partial s _ {L}} = - \frac {\partial \Lambda / \partial s _ {L}}{\partial \Lambda / \partial \tilde {\theta}} = - \frac {- \bar {x} + x _ {L} (\widetilde {\theta} , p _ {S} , s _ {L})}{\partial \Lambda / \partial \tilde {\theta}} > 0, \\ \frac {\partial \tilde {\theta} (\cdot)}{\partial p _ {S}} = - \frac {\partial \Lambda / \partial p _ {S}}{\partial \Lambda / \partial \tilde {\theta}} \\ = - \frac {\bar {x} - x _ {L} (\widetilde {\theta} , p _ {S} , s _ {L}) + x _ {B} (\widetilde {\theta} , p _ {S} , s _ {B})}{\partial \Lambda / \partial \tilde {\theta}} <   0, \\ \frac {\partial \tilde {\theta} (\cdot)}{\partial \bar {x}} = - \frac {\partial \Lambda / \partial \bar {x}}{\partial \Lambda / \partial \tilde {\theta}} = - \frac {p _ {S} - s _ {L}}{\partial \Lambda / \partial \tilde {\theta}} <   0. \end{array}
$$

From Theorem 1, the denominators of the five equations above are positive. Consequently, the first equation is positive and the second equation is negative. From the domain of $x \in [ 0 , { \bar { x } } ]$ , it follows that the third equation is positive and the fourth equation is negative. From the domain of $s _ { L } \in [ 0 , p _ { S } ]$ , it follows that the fifth equation is negative. Q.E.D.

Lemma 5 explains how external factors influence the number of lenders and borrowers of a durable good (cf., first, fourth, and fifth equation in the proof of

Lemma 5), and how the sharing platform can influence the number of lenders and borrowers by adapting its platform fees (cf., second and third equation in the proof of Lemma 5).

## 4.2 Platform Pricing Behavior

As stated earlier, the monopoly sharing platform sets a borrower fee $s _ { B }$ and a lender fee $s _ { L }$ , to be paid to the sharing platform for each transaction between borrowers and lenders. The aggregate shared usage time represents the minimum of aggregate demand of all borrowers and aggregate supply of all lenders.

Using Theorem 1, aggregate demand is represented by

$$
X (\theta , p _ {S}, p _ {P}, s _ {B}, s _ {L}, \bar {x}) = \int_ {0} ^ {\widetilde {\theta} (\cdot)} x _ {B} (\theta , p _ {S}, s _ {B}) d \theta ,
$$

and aggregate supply is represented by

$$
Y (\theta , p _ {S}, p _ {P}, s _ {B}, s _ {L}, \bar {x}) = \int_ {\widetilde {\theta} (\cdot)} ^ {1} y (\theta , p _ {S}, s _ {L}, \bar {x}) d \theta .
$$

The sharing platform also faces fixed costs, $\mathrm { C } ,$ for setting up the platform. Consequently, the profit function of the sharing platform is

$$
\begin{array}{r} \pi = \min \{X (\theta , p _ {S}, p _ {P}, s _ {B}, s _ {L}, \bar {x}), \\ Y (\theta , p _ {S}, p _ {P}, s _ {B}, s _ {L}, \bar {x}) \} [ s _ {B} + s _ {L} ] - C \end{array}
$$

Based on this profit function we can state the profit maximization problem for two cases.

Case 1: For the case in which aggregate supply is greater than or equal to aggregate demand, the profit maximization problem is given by

$$
\max _ {s _ {B}, s _ {L}} \pi = \max _ {s _ {B}, s _ {L}} \{X (\theta , p _ {S}, p _ {P}, s _ {B}, s _ {L}, \bar {x}) * [ s _ {B} + s _ {L} ] - C \},\tag{10}
$$

$$
\mathrm{s.t.} X (\theta , p _ {S}, p _ {P}, s _ {B}, s _ {L}, \bar {x}) \leq Y (\theta , p _ {S}, p _ {P}, s _ {B}, s _ {L}, \bar {x}).
$$

In order to maximize the sharing platform’s profit by choice of the platform fees $s _ { B }$ and $s _ { L }$ , we again use the theorem KKT theorem. The Lagrange function and its first-order conditions are

$$
\begin{array}{r l} & L _ {x} = \int_ {0} ^ {\widetilde {\theta} (\cdot)} x _ {B} (\theta , p _ {S}, s _ {B}) d \theta * [ s _ {B} + s _ {L} ] - \\ & \qquad \lambda_ {1} \left[ \int_ {0} ^ {\widetilde {\theta} (\cdot)} x _ {B} (\theta , p _ {S}, s _ {B}) d \theta - \int_ {\widetilde {\theta} (\cdot)} ^ {1} y (\theta , p _ {S}, s _ {L}, \bar {x}) d \theta \right] \\ & \qquad - C, \end{array}
$$

$$
\begin{array}{r} \frac {\partial L _ {x}}{\partial s _ {B}} = \int_ {0} ^ {\widetilde {\theta} (\cdot)} x _ {B} (\theta , p _ {S}, s _ {B}) d \theta + \\ [ s _ {B} + s _ {L} ] \end{array}
$$

$$
* \left[ \int_ {0} ^ {\widetilde {\theta} (\cdot)} \frac {\partial x _ {B} (\theta , p _ {S} , s _ {B})}{\partial s _ {B}} d \theta + x _ {B} (\widetilde {\theta}, p _ {S}, s _ {B}) * \frac {\partial \widetilde {\theta} (\cdot)}{\partial s _ {B}} \right]
$$

$$
\begin{array}{r l} & {- \lambda_ {1} \Bigg [ \int_ {0} ^ {\widetilde {\theta} (\cdot)} \frac {\partial x _ {B} (\theta , p _ {S} , s _ {B})}{\partial s _ {B}} d \theta} \\ & {\qquad + y (\widetilde {\theta}, p _ {S}, s _ {L}, \bar {x}) * \frac {\partial \widetilde {\theta} (\cdot)}{\partial s _ {B}}} \\ & {\qquad + x _ {B} (\widetilde {\theta}, p _ {S}, s _ {B}) * \frac {\partial \widetilde {\theta} (\cdot)}{\partial s _ {B}} \Bigg ],} \end{array}\tag{11}
$$

$$
\begin{array}{r} \frac {\partial L _ {x}}{\partial s _ {L}} = \int_ {0} ^ {\widetilde {\theta} (\cdot)} x _ {B} (\theta , p _ {S}, s _ {B}) d \theta + [ s _ {B} + s _ {L} ] \\ * x _ {B} (\widetilde {\theta}, p _ {S}, s _ {B}) * \frac {\partial \widetilde {\theta} (\cdot)}{\partial s _ {L}} \end{array}
$$

$$
\begin{array}{r l} & {- \lambda_ {1} \Bigg [ - \int_ {\widetilde {\theta} (\cdot)} ^ {1} \frac {\partial y (\theta , p _ {S} , s _ {L} , \bar {x})}{\partial s _ {L}} d \theta} \\ & {\qquad + y (\widetilde {\theta}, p _ {S}, s _ {L}, \bar {x}) * \frac {\partial \widetilde {\theta} (\cdot)}{\partial s _ {L}}} \\ & {\qquad + x _ {B} (\widetilde {\theta}, p _ {S}, s _ {B}) * \frac {\partial \widetilde {\theta} (\cdot)}{\partial s _ {L}} \Bigg ],} \end{array}\tag{12}
$$

and we have the KKT conditions

$$
(i) \frac {\partial L _ {x}}{\partial s _ {B}} = 0, (i i) \frac {\partial L _ {x}}{\partial s _ {L}} = 0,
$$

$$
\begin{array}{r l} (i i i) & X (\theta , p _ {S}, p _ {P}, s _ {B}, s _ {L}, \bar {x}) \\ & \leq Y (\theta , p _ {S}, p _ {P}, s _ {B}, s _ {L}, \bar {x}); \lambda_ {1} \geq 0; \\ & \quad \lambda_ {1} [ X (\theta , p _ {S}, p _ {P}, s _ {B}, s _ {L}, \bar {x}) \\ & \qquad - Y (\theta , p _ {S}, p _ {P}, s _ {B}, s _ {L}, \bar {x}) ] \\ & \qquad = 0. \end{array}
$$

Lemma 6. In Case 1, a monopoly sharing platform only maximizes profits by setting the platform fees in a way that aggregate demand equals aggregate supply.

Proof: To find a solution we consider if the constraint in (10) is binding. Suppose $X ( \theta , p _ { S } , p _ { P } , s _ { B } , s _ { L } , \bar { x } ) <$ $Y ( \theta , p _ { S } , p _ { P } , s _ { B } , s _ { L } , \bar { x } ) \mathrm { ; }$ <sub>:</sub> From KKT condition (iii) follows $\lambda _ { 1 } = 0$ . From Lemma 5 follows that (12) is positive. Consequently, we have $\partial L _ { x } / \partial s _ { L } > 0$ and KKT condition (ii) is violated.

Now suppose ??(??, ?? , ?? , ?? , ?? , ??̅) = $Y ( \theta , p _ { S } , p _ { P } , s _ { B } , s _ { L } , \bar { x } )$ : From KKT condition (iii) it follows $\lambda _ { 1 } > 0$ . Consequently, KKT condition (i) and (ii) can be fulfilled and this case represents a valid solution. Q.E.D.

Case 2: For the case in which aggregate supply is lower than or equal to aggregate demand, the profit maximization problem is given by

$$
\begin{array}{r} \max _ {s _ {B}, s _ {L}} \pi = \max _ {s _ {B}, s _ {L}} \{Y (\theta , p _ {S}, p _ {P}, s _ {B}, s _ {L}, \bar {x}) \\ * [ s _ {B} + s _ {L} ] - C \}, \end{array}\tag{13}
$$

$$
\mathrm{s.t.} Y (\theta , p _ {S}, p _ {P}, s _ {B}, s _ {L}, \bar {x}) \leq X (\theta , p _ {S}, p _ {P}, s _ {B}, s _ {L}, \bar {x}).
$$

As in Case 1, we use the KKT theorem. The Lagrange function and its first-order conditions are

$$
\begin{array}{r l} L _ {y} = \int_ {\widetilde {\theta} (\cdot)} ^ {1} y \big (\theta , p _ {S}, s _ {L}, \bar {x} \big) d \theta * [ s _ {B} + s _ {L} ] & \\ - \lambda_ {1} \Bigg [ \int_ {\widetilde {\theta} (\cdot)} ^ {1} y \big (\theta , p _ {S}, s _ {L}, \bar {x} \big) d \theta & \\ - \int_ {0} ^ {\widetilde {\theta} (\cdot)} x _ {B} (\theta , p _ {S}, s _ {B}) d \theta \Bigg ] - C, \end{array}
$$

$$
\begin{array}{r l} & {\frac {\partial L _ {y}}{\partial s _ {B}} = \int_ {\widetilde {\theta} (\cdot)} ^ {1} y \big (\theta , p _ {S}, s _ {L}, \bar {x} \big) d \theta -} \\ & {\qquad [ s _ {B} + s _ {L} ] * y \big (\widetilde {\theta}, p _ {S}, s _ {L}, \bar {x} \big) * \frac {\partial \widetilde {\theta} (\cdot)}{\partial s _ {B}}} \\ & {- \lambda_ {1} \Bigg [ - \int_ {0} ^ {\widetilde {\theta} (\cdot)} \frac {\partial x _ {B} \big (\theta , p _ {S} , s _ {B ,} \big)}{\partial s _ {B}} d \theta} \\ & {\qquad - y \big (\widetilde {\theta}, p _ {S}, s _ {L}, \bar {x} \big) * \frac {\partial \widetilde {\theta} (\cdot)}{\partial s _ {B}}} \\ & {\qquad - x _ {B} \big (\widetilde {\theta}, p _ {S}, s _ {B} \big) * \frac {\partial \widetilde {\theta} (\cdot)}{\partial s _ {B}} \Bigg ],} \end{array}\tag{14}
$$

$$
\begin{array}{c} \frac {\partial L _ {y}}{\partial s _ {L}} = \int_ {\widetilde {\theta} (\cdot)} ^ {1} y (\theta , p _ {S}, s _ {L}, \bar {x}) d \theta + \\ [ s _ {B} + s _ {L} ] * \\ \left[ \int_ {\widetilde {\theta} (\cdot)} ^ {1} \frac {\partial y (\theta , p _ {S} , s _ {L} , \bar {x})}{\partial s _ {L}} d \theta - y (\widetilde {\theta}, p _ {S}, s _ {L}, \bar {x}) * \frac {\partial \widetilde {\theta} (\cdot)}{\partial s _ {L}} \right] \end{array}
$$

$$
\begin{array}{r l} & {- \lambda_ {1} \left[ \int_ {\tilde {\theta} (\cdot)} ^ {1} \frac {\partial y (\theta , p _ {S} , s _ {L} , \bar {x})}{\partial s _ {L}} d \theta \right.} \\ & {\qquad \left. - y (\tilde {\theta}, p _ {S}, s _ {L}, \bar {x}) * \frac {\partial \tilde {\theta} (\cdot)}{\partial s _ {L}} \right.} \\ & {\qquad \left. - x _ {B} (\tilde {\theta}, p _ {S}, s _ {B}) * \frac {\partial \tilde {\theta} (\cdot)}{\partial s _ {L}} \right],} \end{array}\tag{15}
$$

and we have the KKT conditions

$$
(i) \frac {\partial L _ {y}}{\partial s _ {B}} = 0, (i i) \frac {\partial L _ {y}}{\partial s _ {L}} = 0,
$$

$$
\begin{array}{c} (i i i) Y (\theta , p _ {S}, p _ {P}, s _ {B}, s _ {L}, \bar {x}) \leq X (\theta , p _ {S}, p _ {P}, s _ {B}, s _ {L}, \bar {x}); \lambda_ {1} \\ \geq 0; \end{array}
$$

$$
\begin{array}{c} \lambda_ {1} [ Y (\theta , p _ {S}, p _ {P}, s _ {B}, s _ {L}, \bar {x}) - X (\theta , p _ {S}, p _ {P}, s _ {B}, s _ {L}, \bar {x}) ] \\ = 0. \end{array}
$$

Lemma 7: In Case $^ { 2 , }$ a monopoly sharing platform only maximizes profits by setting the platform fees in a way that aggregate demand equals aggregate supply.

Proof: To find a solution we consider if the constraint in (13) is binding. Suppose $Y ( \theta , p _ { S } , p _ { P } , s _ { B } , s _ { L } , \bar { x } ) <$ $X ( \theta , p _ { S } , p _ { P } , s _ { B } , s _ { L } , \bar { x } )$ : From KKT condition (iii) it follows $\lambda _ { 1 } = 0$ . From Lemma 5 it follows that (14) is positive. Consequently, we have $\partial L _ { y } / \partial s _ { B } > 0$ and KKT condition (i) is violated.

Now suppose $Y ( \theta , p _ { S } , p _ { P } , s _ { B } , s _ { L } , \bar { x } ) =$ $X ( \theta , p _ { S } , p _ { P } , s _ { B } , s _ { L } , \bar { x } )$ : From KKT condition (iii) it follows $\lambda _ { 1 } > 0$ . Consequently, KKT condition (i) and (ii) can be fulfilled and this case represents a valid solution. Q.E.D.

Combining Lemma 6 and Lemma 7, we find that a sharing platform has to set the platform fees in a way that the market clears, in other words, to maximize profits platform fees have to be set so that aggregate demand equals aggregate supply. We identify the platform fees that result in such a market by the market-clearing condition

$$
\begin{array}{r l} & {\int_ {\widetilde {\theta} (\cdot)} ^ {1} y \big (\theta , p _ {S}, s _ {L}, \bar {x} \big) d \theta} \\ & {- \int_ {0} ^ {\widetilde {\theta} (\cdot)} x _ {B} (\theta , p _ {S}, s _ {B}) d \theta} \\ & {= 0 = \epsilon (p _ {S}, s _ {B}, s _ {L}, p _ {P}, \bar {x}),} \end{array}\tag{16}
$$

where $\epsilon ( p _ { S } , s _ { B } , s _ { L } , p _ { P } , \bar { x } )$ implicitly defines the lender fee $s _ { L } ( p _ { S } , s _ { B } , p _ { P } , \bar { x } )$ and the borrower fee $s _ { B } ( p _ { S } , s _ { L } , p _ { P } , \bar { x } )$ Based on this market-clearing condition, Lemma 8 explains how aggregate demand and supply simultaneously change as a result of changes in the external factors, and the platform fees.

Lemma 8: Aggregate demand increases and aggregate supply decreases in the lender fee and purchase price. Aggregate supply increases and aggregate demand decreases in the borrower fee, the sharing price, and capacity.

Proof: Totally differentiating (16) with respect to ?? , ?? , ?? ?? <sup>,</sup> <sup>and</sup> ??�<sup>,</sup> <sup>we</sup> <sup>have</sup>

$$
\begin{array}{r l} & {\frac {\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x})}{\partial p _ {S}} =} \\ & {- \int_ {0} ^ {\tilde {\theta} (\cdot)} \frac {\partial x _ {B} (\theta , p _ {S} , s _ {B})}{\partial p _ {S}} d \theta + \int_ {\tilde {\theta} (\cdot)} ^ {1} \frac {\partial y (\theta , p _ {S} , s _ {L} , \bar {x})}{\partial p _ {S}} d \theta} \\ & {- y (\tilde {\theta}, p _ {S}, s _ {L}, \bar {x}) * \frac {\partial \tilde {\theta} (\cdot)}{\partial p _ {S}} - x _ {B} (\tilde {\theta}, p _ {S}, s _ {B}) * \frac {\partial \tilde {\theta} (\cdot)}{\partial p _ {S}} > 0,} \\ & {\frac {\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x})}{\partial s _ {B}} =} \end{array}
$$

$$
\begin{array}{r l} & {- \int_ {0} ^ {\widetilde {\theta} (\cdot)} \frac {\partial x _ {B} (\theta , p _ {S} , s _ {B})}{\partial s _ {B}} d \theta - y (\widetilde {\theta}, p _ {S}, s _ {L,}, \bar {x}) * \frac {\partial \widetilde {\theta} (\cdot)}{\partial s _ {B}}} \\ & {- x _ {B} (\widetilde {\theta}, p _ {S}, s _ {B}) * \frac {\partial \widetilde {\theta} (\cdot)}{\partial s _ {B}} > 0,} \\ & {\frac {\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x})}{\partial s _ {L}} =} \\ & {\int_ {\widetilde {\theta} (\cdot)} ^ {1} \frac {\partial y (\theta , p _ {S} , s _ {L} , \bar {x})}{\partial s _ {L}} d \theta - y (\widetilde {\theta}, p _ {S}, s _ {L,}, \bar {x}) * \frac {\partial \widetilde {\theta} (\cdot)}{\partial s _ {L}}} \\ & {- x _ {B} (\widetilde {\theta}, p _ {S}, s _ {B}) * \frac {\partial \widetilde {\theta} (\cdot)}{\partial s _ {L}} <   0,} \\ & {\frac {\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x})}{\partial p _ {P}} =} \\ & {- y (\widetilde {\theta}, p _ {S}, s _ {L,}, \bar {x}) * \frac {\partial \widetilde {\theta} (\cdot)}{\partial p _ {P}} - x _ {B} (\widetilde {\theta}, p _ {S}, s _ {B}) * \frac {\partial \widetilde {\theta} (\cdot)}{\partial p _ {P}} <   0,} \\ & {\frac {\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x})}{\partial \bar {x}} =} \\ & {\int_ {\widetilde {\theta} (\cdot)} ^ {1} \frac {\partial y (\theta , p _ {S} , s _ {L} , \bar {x})}{\partial \bar {x}} d \theta - y (\widetilde {\theta}, p _ {S}, s _ {L,}, \bar {x}) * \frac {\partial \widetilde {\theta} (\cdot)}{\partial \bar {x}}} \\ & {- x _ {B} (\widetilde {\theta}, p _ {S}, s _ {B}) * \frac {\partial \widetilde {\theta} (\cdot)}{\partial \bar {x}} > 0.} \end{array}
$$

From the borrowers’ individual elasticities of demand explained in Lemma 1, the lenders’ individual elasticities of supply explained in Lemma 4, and the changes in the number of lenders and borrowers explained in Lemma 5 we get the signs of the five equations above. Q.E.D.

The first equation represents the e<sub>ff</sub>ect of the sharing price on aggregate demand and supply. A marginal increase of the sharing price decreases the demand of borrowers and increases the supply of lenders. These e<sub>ff</sub>ects are represented by the first two terms. Moreover, the supply increases and the demand decreases from a shift of the indi<sub>ff</sub>erent consumer. This e<sub>ff</sub>ect is represented by the last two terms. Overall, a marginal increase of the sharing price leads to a greater aggregate supply than demand.

The second equation represents the e<sub>ff</sub>ect of the borrower fee on aggregated demand and supply. A marginal increase of the borrower fee decreases the demand of all borrowers represented by the first term and has no e<sub>ff</sub>ect on the supply of lenders. Moreover, the supply increases and the demand decreases from a shift of the indi<sub>ff</sub>erent consumer. This e<sub>ff</sub>ect is represented by the last two terms. Overall, a marginal increase of the borrower fee leads to a greater aggregate supply than demand.

The third equation represents the e<sub>ff</sub>ect of the lender fee on aggregated demand and supply. A marginal increase of the lender fee decreases the supply of lenders represented by the first term and has no e<sub>ff</sub>ect on the demand of borrowers. Moreover, the supply decreases and the demand increases from a shift of the indi<sub>ff</sub>erent consumer. This e<sub>ff</sub>ect is represented by the last two terms. Overall, a marginal increase of the lender fee leads to a greater aggregate demand than supply.

The fourth equation represents the e<sub>ff</sub>ect of the purchase price on aggregated demand and supply. The only e<sub>ff</sub>ect from a marginal increase of the purchase price is a shift of the indi<sub>ff</sub>erent consumer resulting in an increasing aggregate demand and a decreasing aggregate supply.

The last equation represents the e<sub>ff</sub>ect of capacity on aggregated demand and supply. A marginal increase in capacity increases the supply of all lenders represented by the first term and has no e ect on the demand of all borrowers. Moreover, the supply increases and the demand decreases from a shift of the indi<sub>ff</sub>erent consumer. This e<sub>ff</sub>ect is represented by the last two terms. Overall, a marginal increase in capacity leads to a greater aggregate supply than demand.

Consequently, isolated changes in the external factors and the platform fees result in a violation of the market-clearing condition described in (16). To maintain the market-clearing condition, the sharing platform has to adapt its platform fees in response to the e<sub>ff</sub>ects explained in Lemma 8. Theorem 2 defines the comparative statics of the platform fees as a result of changes in the external factors and of changes in the complement platform fee:

Theorem 2. The lender fee is increasing with the sharing price, is increasing with the borrower fee, is increasing with capacity, and is decreasing with the purchase price. The borrower fee is increasing with the purchase price, is increasing with the lender fee, is decreasing with the sharing price, and is decreasing with capacity.

Proof: From Lemma 8 and the implicit function rule, we get the e<sub>ff</sub>ects on $s _ { L }$ by

$$
\frac {\partial s _ {L}}{\partial p _ {S}} = - \frac {\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x}) / \partial p _ {S}}{\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x}) / \partial s _ {L}} > 0,
$$

$$
\frac {\partial s _ {L}}{\partial s _ {B}} = - \frac {\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x}) / \partial s _ {B}}{\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x}) / \partial s _ {L}} > 0,
$$

$$
\frac {\partial s _ {L}}{\partial p _ {P}} = - \frac {\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x}) / \partial p _ {P}}{\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x}) / \partial s _ {L}} <   0,
$$

$$
\frac {\partial s _ {L}}{\partial \bar {x}} = - \frac {\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x}) / \partial \bar {x}}{\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x}) / \partial s _ {L}} > 0,
$$

and the effects on $s _ { B }$ by

$$
\frac {\partial s _ {B}}{\partial p _ {S}} = - \frac {\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x}) / \partial p _ {S}}{\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x}) / \partial s _ {B}} <   0,
$$

$$
\frac {\partial s _ {B}}{\partial s _ {L}} = - \frac {\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x}) / \partial s _ {L}}{\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x}) / \partial s _ {B}} > 0,
$$

$$
\frac {\partial s _ {B}}{\partial p _ {P}} = - \frac {\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x}) / \partial p _ {P}}{\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x}) / \partial s _ {B}} > 0,
$$

$$
\frac {\partial s _ {B}}{\partial \bar {x}} = - \frac {\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x}) / \partial \bar {x}}{\partial \epsilon (p _ {S} , s _ {B} , s _ {L} , p _ {P} , \bar {x}) / \partial s _ {B}} <   0.
$$

Q.E.D.

The comparative statics of the lender and borrower fees to each other are positive, indicating that these fees are strategic complements. This is because a reduction in one requires a reduction in the other in order to maintain the market-clearing condition, and vice versa. For given external factors, the comparative statics of the lender and borrower fees can be used to change their absolute level. This is required if platform profits can be increased through changing the absolute level of the platform fees. The profit maximizing level of the platform fees depends on the relative magnitudes of the platform fee elasticities of demand explained in Lemma 1, the platform fee elasticities of supply explained in Lemma 4, and the e<sub>ff</sub>ects of changing platform fees on the number of lenders and borrowers explained in Lemma 5.

Moreover, the comparative statics show that in order to remain profit maximizing and maintain the marketclearing condition, a monopoly sharing platform must adapt its platform fees in response to changes in purchase price, sharing price, and capacity of a durable good as follows: the lender fee has to be increased or the borrower fee has to be decreased with an increasing sharing price, an increasing capacity, and a decreasing purchase price of a durable good and, vice versa. Whether to adapt the lender fee or the borrower fee depends on the relative magnitude of the external factor elasticities of demand explained in Lemma 1, the external factor elasticities of supply explained in Lemma 4, and the e<sub>ff</sub>ects of changing external factors on the number of lenders and borrowers explained in Lemma 5.

## 5 Conclusion and Discussion

Rifkin (2000) predicted in the year 2000 that “ownership is steadily being replaced by access.” A couple of years later several sharing platforms such as zilok.com emerged. These sharing platforms aim to maximize profits and need to understand how to optimally price lenders and borrowers in response to changes in external factors, such as the sharing price, purchase price, and capacity of a good.

We find that sharing platforms maximize profits only if the supplied usage time of a durable good provided by lenders through a sharing platform matches the demanded usage time requested by borrowers—that is, the market must clear for platform fees to be profit maximizing. We further find that the market-clearing condition requires lender and borrower fees are classic strategic complements, and we show how sharing platforms have to adapt their platform fees in response to a changing sharing price, purchase price, and durability.

Most pricing models of existing sharing platforms have not implemented pricing models in which platform fees dynamically change for the same durable good in response to external factors. Although in a di<sub>ff</sub>erent setting, an exception is uber.com, which dynamically adapts the sharing price in response to changing demand and supply in the sharing of transportation services. The major di<sub>ff</sub>erence between uber.com and the sharing platforms for durable goods that we study—aside from features of the setting (i.e., on uber.com participation in market sides is predetermined, capacity is flexible, etc.)—is that uber.com not only decides on the platform fees but also on the sharing price.

Sharing platforms for durable goods can only set the platform fees (i.e., the lender determines the sharing price). The vast majority of sharing platforms such as aszilok.com only charge a percent-of-value lender fee, representing a percentage rate of the total sharing price, and do not charge borrowers. Our model results indicate that such a percent-of-value lender fee may be a valid pricing model for lenders as long as the sharing platform is able to clear the market by using this mechanism. However, if the demand for sharing a durable good is higher than supply, then even with a very low lender fee, raising a borrower fee can become necessary to fulfill the market-clearing condition and to maximize profits. In our model, we found that such a borrower fee must be reduced if the sharing price increases in order to maintain the market-clearing condition. Subsequently, a percent-of-value borrower fee (e.g. charged by airbnb.com) cannot continuously maximize profits. These findings indicate that commonly applied one-sided pricing models of sharing platforms can be improved.

Because not all factors that influence platform fees can be continuously observed, sharing platforms may implement the relationships defined in our Lemmas and Theorems as rule-based pricing mechanisms (cf., Bădică, Bădită, & Ganzha, 2006). In this way, sharing platforms can ensure that the platform fees are adapted in an automated way in response to changes of, for example, the sharing or purchase price of a durable good, and may dynamically maximize their profits.

Although there are benefits from analyzing platform pricing in a general analytical model— specifically the wide range to which the results apply—there are still some limitations that represent starting points for future research.

Nonnegative platform fees: In our model we assume nonnegative platform fees $( s _ { L } \in [ 0 , p _ { S } ] ; s _ { B } \in$ $[ 0 , p _ { P } ] ; s _ { L } + s _ { B } \in R ^ { + } )$ <sub>.</sub> We made this assumption because sustainable business models of sharing platforms require positive fees to cover fixed costs and we do not observe negative fees charged by operating sharing platforms in practice. However, especially for new start-ups, it may be the case that supply for sharing a durable good is zero or very low while demand is very high. In this case, to encourage supply on the sharing platform, it may be profit maximizing (at least in the short run) to subsidize lenders by a negative fee. To analyze if and how our findings change in the case of negative platform fees would likely require a di usion model and is a task for future research.

Nonlinear platform fees: We implicitly assume the transaction-based platform fees linearly increase in the shared usage time of a durable good. However, there are pricing models in which the marginal platform fees decrease in the shared usage time (e.g., zilok.com charges a lender fee which decreases from 9% to 5% in the shared usage time of a durable good). To analyze the e<sub>ff</sub>ects of di<sub>ff</sub>erent nonlinear pricing models, our model would have to be extended by reduced-form functions for the platform fees.

Fixed platform fees: If the platform fees take the form of a membership (or fixed) fee that can differ between the membership fee charged to borrows and lenders, the difference in these fees would be an argument to the function which defines the consumer that is indifferent between borrowing and lending. Consequently, the di<sub>ff</sub>erence in membership fees could be used by the sharing platform as a means with which to control the number of borrowers and lenders. The membership fees could also be used to make additional profit from consumers if the consumer need for the durable good were sufficiently large.

Externalities: Sharing durable goods can have positive externalities (e.g., lowering environmental damage, fostering communities), and negative externalities (e.g., downturn in demand for buying durable goods, decreasing revenues for traditional firms). A possible extension of our model would be the incorporation of such externalities and the analysis of their impact on our findings.

Welfare and policy: A further direction for future research is to extend our model to include welfare analysis. This is of special interest, since existing literature has not yet reached a consensus on the impact of the sharing economy on producer surplus. For instance, Zervas et al. (2014) empirically found that airbnb.com successfully competes with established firms in the hospitality industry, leading to decreasing hotel revenues. In contrast, Jiang and Tian (2015) highlight that consumers have higher reservation prices for durable goods because they anticipate additional revenues from sharing. Consequently, manufacturers of durable goods may benefit from sharing, as they can charge higher purchase prices. Moreover, the impact of the sharing economy on overall welfare, including consumer surplus, producer surplus, and di<sub>ff</sub>erent externalities is unclear. There is also a lack of policy frameworks for regulating the new sharing economy (Dervojeda et al., 2013). Against this backdrop, another interesting direction for further research would be analyzing di<sub>ff</sub>erent policy measures for the C2C sharing market and their impact on social welfare.

B2C business models: Beside the C2C sharing business model analyzed in this research, B2C sharing is another business model that is commonly applied in the sharing economy. In our current C2C model, consumers decide to purchase and share (i.e., be a lender) or borrow (i.e., be a borrower) a homogeneous durable good based on the utilities they expect from the two options. In contrast, in a B2C model, lenders and borrowers are mutually exclusive groups—lenders are firms that maximize profits, while borrowers are consumers who maximize utility. As this represents a substantially di<sub>ff</sub>erent model setup, in future research we aim to analyze whether our findings also hold in a B2C sharing model.

## References

Alba, J., Weitz, B., Janiszewski, C., Lutz, R., Sawyer, A., Wood, S., & Lynch, J. (1997). Interactive home shopping: Consumer, retailer, and manufacturer incentives to participate in electronic marketplaces. Journal of Marketing, 61(3), 38-53.

Armstrong, M. (2006). Competition in two-sided markets. The RAND Journal of Economics, 37(3), 668-691.

Becker, G. S. (1976). The economic approach to human behavior. Chicago, IL: The University Press of Chicago.

Belk, R. (2007). Why not share rather than own? The ANNALS of the American Academy of Political and Social Science, 611, 126-140.

Belk, R. (2010). Sharing. Journal of Consumer Research, 36(5), 715-734.

Botsman, R., & Rogers, R. (2010). What’s mine is yours: The rise of collaborative consumption. New York, NY: HarperCollins.

Boyd, S., & Vandenberghe, L. (2004). Convex optimization. New York, NY: Cambridge University Press.

Brock, W. A., & Evans, D. S. (1985). The economics of regulatory tiering. The RAND Journal of Economics, 16(3), 398-409.

Bădică, C., Bădită, A., & Ganzha, M. (2006). Implementing rule-based mechanisms for agentbased price negotiations. In Proceedings of the 2006 ACM Symposium on Applied Computing. ACM.

Caillaud, B., & Jullien, B. (2003). Chicken & egg: Competition among intermediation service providers. The RAND Journal of Economics, 34(2), 309-328.

Chen, Y. (2009). Possession and access: Consumer desires and value perceptions regarding contemporary art collection and exhibit visits. Journal of Consumer Research, 35(6), 925-940.

Cusumano, M. A. (2014). How traditional firms must compete in the sharing economy. Communications of the ACM, 58(1), 32-34.

Dervojeda, K., Verzijil, D., Nagtegaal, F., Lengton, M. , Rouwmaat, E., Monfardini, E., & Frideres L. (2013). The sharing economy: Accessibility based business models for peer-to-peer markets. Retrieved from http://ec.europa.eu/DocsRoom/documents/13413/ attachments/2/translations/en/renditions/native.

Einav, L., Farronato, C., & Levin, J. (2016). Peer-to-peer markets. Annual Review of Economics, 8, 615-635.

Eisenmann, T., Parker G., & Van Alstyne, M. W. (2006). Strategies for two-sided markets. Harvard Business Review, 84(10), 92-101.

Fraiberger, S., & Sundararajan A. (2015). Peer-to-peer rental markets in the sharing economy. Social Science Research Network. Retrieved from https://papers.ssrn.com/sol3/papers.cfm?abstract id=2574337

Jiang, B., & Tian, L. (2015). Collaborative consumption: Strategic and economic implications of product sharing (Working paper). Washington University, St. Louis, MO.

Knote, R., & Blohm, I. (2016). Deconstructing the sharing economy: On the relevance for IS research. In Proceedings of the Multikonferenz Wirtschaftsinformatik (pp. 46-54). Illmenau, Germany.

Lamberton, C. P., & Rose, R. L. (2012). When is ours better than mine? A framework for understanding and altering participation in commercial sharing systems. Journal of Marketing, 76(4), 109-125.

Lee, R. S., & Wu, T. (2009). Subsidizing creativity through network design: Zero-pricing and net neutrality. The Journal of Economic Perspectives, 23(3), 61- 76.

Levi, M. D., & Nault, B. R. (2004). Converting technology to mitigate environmental damage. Management Science, 50(8), 1015-1030.

Malhotra, A., & Van Alstyne, M., (2014). The dark side of the sharing economy and how to lighten it. Communications of the ACM, 57(11), 24-27.

Matzner, M., Chasin F., & Todenhoefer L., (2015). To share or not to share: Towards understanding the antecedents of participation in it enabled sharing services. In Proceedings of the European Conference on Information Systems. AIS.

Moehlmann, M. (2015). Collaborative consumption: determinants of satisfaction and the likelihood of using a sharing option again. Journal of Consumer Behavior, 14(3), 193-207.

Mueller, M. P. (2014). An economic analysis of online sharing systems’ implications on social welfare. Proceedings of the European Conference on Information Systems. AIS.

Nault, B. R. (1996). Equivalence of taxes and subsidies in the control of production externalities. Management Science, 42(3), 307-320.

Phipps, M., Ozanne, L. K., Luchs, M. G., Subrahmanyan, S., Kapitan, S., Catlin, J. R., Gau, R., Naylor, R. W., Rose, R. L., & Simpson, B. (2013). Understanding the inherent complexity of sustainable

consumption: A social cognitive framework. Journal of Business Research, 66(8), 1227-1234.

PwC (2015). The sharing economy: Sizing the revenue opportunity. Retrieved from http://www.pwc.co.uk/issues/megatrends/collision s/sharingeconomy/the-sharing economy-sizingthe-revenue-opportunity.html

Rifkin, J. (2000). The age of access: The new culture of hypercapitalism where all of life is a paid-for experience. New York, NY: Putnam.

Rochet, J. C., & Tirole, J. (2006). Two-sided markets: a progress report. The RAND Journal of Economics, 37(3), 645-667.

Rysman, M. (2009). The economics of two-sided markets. The Journal of Economic Perspectives, 23(3), 125- 143.

Sundararajan, A. (2016). The sharing economy. Cambridge, MA: Massachusetts Institute of Technology Press.

Weber, T. A. (2014). Intermediation in a sharing economy: Insurance, moral hazard, and rentextraction. Journal of Management Information Systems, 31(3), 35-71.

Zervas, G., Proserpio, D., & Byers, J. (2014). The rise of the sharing economy: Estimating the impact of airbnb on the hotel industry (Working paper) Boston University, Boston, MA

## About the Authors

Steffen Zimmermann is a full professor in the Department of Information Systems, Production and Logistics Management at the University of Innsbruck, Austria. He received his doctorate degree from the University of Augsburg, Germany. His main research interests include economics of IS, online consumer reviews, platform and blockchain business. He has published several articles in international research journals, including Business & Information Systems Engineering, Decision Support Systems, Information Systems Research, and Service Science. He has also presented his research at IS leading conferences, such as the International Conference on Information Systems and the Conference on Information Systems and Technology.

Peter Angerer is a PhD candidate in the Department of Information Systems, Production and Logistics Management at the University of Innsbruck, Austria. His main research topic is the sharing economy which is also the focus of his PhD thesis. In particular, theorizing the economic effects of sharing platforms on the participants of the sharing ecosystem and the behavioral implications of the design of sharing platforms on its users are the two main areas of interest. His research has appeared in several proceedings of major IS conferences, including International Conference for Information Systems (ICIS), European Conference on Information Science (ECIS) and Hawaii International Conference on System Sciences (HICSS).

Daniel Provin is a PhD candidate in the Department of Information Systems, Production and Logistics Management at the University of Innsbruck, Austria and is an IT professional for manufacturing execution systems. His research interests focus on the sharing economy, blockchain technologies, and the internet of things. Theorizing the economic effects of sharing platforms on the participants of the sharing ecosystem and the behavioral implications of the design of sharing platforms on its users are the two main areas of academic interest. The application of blockchain technologies and Internet of Things are part of his professional R&D activities. His research has appeared in proceedings of major IS conferences, including International Conference for Information Systems (ICIS) and Hawaii International Conference on System Sciences (HICSS).

Barrie R. Nault is Distinguished Research Professor and Director of the Informatics Research Centre at the University of Calgary. He was previously on faculty at The Ohio State University, the University of California, and the University of Alberta. He received his PhD from the University of British Columbia. Dr. Nault was an IS Department Editor for Management Science, and is a Distinguished Fellow of the INFORMS Information Systems Society. His research includes IT productivity; ownership, incentives, membership and investment in networks, virtual organizations and supply chains; public safety networks; net neutrality; IT and transaction costs; and environmental incentives for new technology conversion. Dr. Nault has published research articles in Information Systems Research; IEEE Transactions on Engineering Management; Management Information Systems Quarterly; Management Science; Production and Operations Management; Strategic Management Journal; Marketing Science; Journal of Money, Credit and Banking; Journal of Monetary Economics; Organization Science, among others. He has also written reports for the National Research Council, and has held grants from the NSF in the U.S. as well as NSERC and SSHRC in Canada.

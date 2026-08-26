---
otero_id: 2020
otero_key: "75XS85J9"
title: "Does It Pay to Shroud In-App Purchase Prices?"
authors: "Jeffrey D. Shulman; Xianjun Geng"
year: "2019"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0835"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [141.216.78.40] On: 31 August 2019, At: 09:25 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/75XS85J9/fulltext/images/a81968f4388f3e67d81b9cae2898e5b52651c6a6d81d6a301b209f5768efe8ab.jpg)

## Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Does It Pay to Shroud In-App Purchase Prices?

Jeffrey D. Shulman, Xianjun Geng

To cite this article:

Jeffrey D. Shulman, Xianjun Geng (2019) Does It Pay to Shroud In-App Purchase Prices?. Information Systems Research

Published online in Articles in Advance 29 Aug 2019

https://doi.org/10.1287/isre.2019.0835

## Full terms and conditions of use: https://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2019, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Does It Pay to Shroud In-App Purchase Prices?

Jeffrey D. Shulman,<sup>a</sup> Xianjun Geng<sup>b</sup>

<sup>a</sup> Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195; <sup>b</sup> A. B. Freeman School of Business, Tulane University, New Orleans, Louisiana 70118

Contact: jshulman@uw.edu, https://orcid.org/0000-0001-5288-3421 (JDS); geng@tulane.edu, http://orcid.org/0000-0002-9915-7096 (XG)

Received: Revised: October 25, 2017; Au<sub>Accepted:</sub> Published Online in Articles in Advance: August 29, 2019

https://doi.org/10.1287/isre.2019.083

Copyright:

Abstract. Application (app) developers commonly sell their apps at relatively low prices and subsequently earn substantial revenue from in-app purchases. Although some con sumers may do their research about in-app prices before deciding whether to buy the app, others only discover the in-app prices later in the purchase process. This paper presents an analytical model to examine the profit and welfare implications of hidden prices of the in-app purchases. This paper has three main contributions. First, it finds a profit-improvement effect of hidden prices under circumstances for which prior literature finds profit irrelevance. In this regard, the model identifies a new mechanism driving the profit-improvement result. Second, it finds when app developers can be made better off by platforms disclosing in-app purchase prices. Third, it shows how platform decisions intended to improve pricing transparency may actually diminish consumer welfare. We also consider a model variation whereby app developers can shroud in-app prices. The findings have implications for app developers considering hidden in-app purchases, as well as platforms such as Google, Apple, and Amazon, which can restrict this practice.

History: Alessandro Acquisti, Senior Editor; De Liu, Associate Editor. Funding: X. Geng received financial support from the National Science Foundation of China [Grants 71628205 and 71872144].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2019.0835.

Keywords: game theory • in-app purchase • shrouded prices • pricing

## 1. Introduction

In 2009, Apple introduced in-application purchases (in-app purchases).<sup>1</sup> Nowadays, it is a common practice for developers on mobile platforms to first offer their apps at a low price to consumers and subsequently charge consumers more for optional functionalities or content through in-app purchases. For example, as of October 2017, the mobile game Minecraft: Pocket Edition was listed for \$6.99 in both the Apple App Store and Google Play, and a popular fitness app, 7-Minute Workout Challenge, was listed for \$2.99.<sup>2</sup> These prices are listed prominently at the point of purchase but only tell a part of the full story. In-app content such as “skin packs” for Minecraft users and additional workout packs for 7-Minute Workout Challenge users require additional payment.

Interestingly, platforms such as the Apple App Store and Google Play demonstrate a level of control regarding how readily available to make information about the in-app purchase prices. As can be seen in Online Appendix A, Google Play requires more scrolling to find in-app purchase prices than the Apple App Store (iOS 9). Moreover, the Apple App Store increased the amount of scrolling necessary to find in-app purchase prices in the subsequently released iOS 11 (Online Appendix A). Previous research shows that consumers are heterogeneous in their propensity to scroll to lower screens in online shopping (e.g., Brynjolfsson et al. 2004). As a consequence, a platform’s decision as to where to disclose in-app purchase content can determine how many consumers ultimately find this information before purchase. We refer to the burying of in-app purchase prices as shrouding.

In this research, we examine the equilibrium pricing decisions by competing app developers and the platform shrouding decision.<sup>3</sup> This is an increasingly important economy. For instance, app purchases accounted for \$29 billion in revenue, and in-app purchases accounted for \$37 billion in revenue. Both measures represent significant growth over 2011, when revenues from app purchases and in-app purchases were \$7 billion and \$700 million, respectively.<sup>4</sup> The market for mobile apps is also characterized by intense competition. The Apple App Store and Google Play as of 2018 boost 2 million and 3.9 million apps, respectively, and popular genres, such as fitness apps, contain hundreds of competing apps.<sup>5</sup> In this paper, we develop a game theory model to address the following research questions:

1. Do app developers benefit from platform shrouding of in-app purchase prices?

2. Does having more consumers uninformed about the prices of in-app purchases always lead to higher firm and platform profits? Relatedly, what should be a mobile platform’s optimal disclosure policy regarding in-app purchases?

3. Does more transparency regarding the prices of in-app purchases always lead to higher consumer welfare?

To address these research questions, we develop a model of competition between two horizontally differentiated app developers in serving rational consumers. We allow for the app platform to set the degree of shrouding and consider consumer heterogeneity in the propensity to become informed about the in-app purchase prices. When consumers are uninformed about in-app purchase prices, they form rational expectations about the unobserved prices. Consideration of rational consumers is consistent with prior research in information systems (IS), marketing, and economics (e.g., Lal and Matutes 1994, Acquisti and Varian 2005, Dou et al. 2017) and produces novel results when jointly considered with consumer heterogeneity in the propensity to become informed of in-app purchase prices given the platform’s shrouding decision.

In addressing the research questions, our model identifies a new economic mechanism that generates new findings with regard to the relationship between shrouding of in-app purchase prices and firm profitability. Previous literature has looked at why competing firms may each shroud prices, but a common result is that equilibrium industry profitability is unaffected by shrouding (Lal and Matutes 1994, Verboven 1999, Gabaix and Laibson 2006). The “Chicago-school argument,” as Ellison (2005, p. 586) referred to it, is that any gain from unadvertised prices will be competed away via lower advertised prices, even if individual firms may choose not to advertise some prices. The practical implication of prior research is that, with few exceptions, app developers would not benefit from price shrouding on a platform. We show, however, that platform shrouding may boost profits for the app developers and the platform.

The known exceptions in which industry profits may increase as a result of price shrouding are Shulman and Geng (2013) and Ellison (2005). Shulman and Geng (2013) require competition between vertically differentiated firms for shrouding to increase industry profits. The Ellison (2005) result requires that consumers who are willing to pay the shrouded prices are significantly more sensitive to interfirm differences in posted prices. Ellison (2005, p. 587) acknowledges, “there are markets where willingness to pay for addons and sensitivity to interfirm price differences are better modeled as independent,” markets to which his analysis does not apply. From a practical standpoint, our research examines whether the conditions of either Shulman and Geng (2013) or Ellison (2005) must be satisfied to recommend price shrouding by a platform aiming to boost industry profits. Moreover, prior research considers the industry profitability of shrouding versus a standard pricing game, leaving the question of the optimal degree of shrouding unanswered.

In addressing the first research question, this paper identifies a new competition-softening effect by which shrouding in-app purchase prices can increase equilibrium profitability in cases not identified in the literature. Specifically, this research shows that consumers who do not observe the in-app purchase prices will rationally expect them to be negatively correlated with the observed base prices. Consequently, a firm’s price cut on the app price is less effective in attracting consumers, which softens competition and boosts firm profitability. This finding suggests that platforms can benefit from price shrouding in situations not predicted by the prior literature. Moreover, app developers may earn greater profit on a platform that shrouds the in-app purchase prices.

Addressing the second research question produces new insights. Previous models either consider all consumers as informed or uninformed about unadvertised prices (e.g., Lal and Matutes 1994, Ellison 2005), find no effect of the number of uninformed consumers on equilibriuim profitability (e.g., Gabaix and Laibson 2006), or do not study the issue (Shulman and Geng 2013). Our research finds that having more consumers uninformed about in-app purchase prices before making their firm choice is not always beneficial to app developers or platforms.<sup>6</sup> Our counterintuitive result arises because the competition-softening effect mentioned earlier holds only if the proportion of uninformed consumers is not too large. We find a nonmonotonic effect of shrouding on app developer and platform profitability. As a consequence, a move toward greater, but not complete, transparency in inapp purchase prices benefits app developers. The research further shows that a mobile platform should adopt a disclosure policy regarding in-app purchase prices that is neither too transparent nor too obscure.

In addressing the third research question, the research demonstrates that initiatives to keep consumers better informed of in-app purchase prices may not be in the consumers’ best interest. In fact, consumers may be worse off when in-app purchase prices are transparent to a greater number of consumers. This contrasts with conventional wisdom. The Office of Fair Trading in the United Kingdom calls for price information to be provided “clearly, accurately and prominently up-front, before the consumer . . . agrees to make a purchase.”<sup>7</sup> The European Commission has actively engaged with leading mobile platforms on how to provide “clearer explanations about the costs involved in apps.”<sup>8</sup> Studying the coexistence of informed and uninformed rational consumers is managerially relevant because even when firms shroud in-app purchase prices, a subset of consumers, but not all, will scroll to obtain this information. An implication of the model findings is that consumers may be disadvantaged by recent changes to platform disclosure policies that make it such that some, but not all, consumers find the in-app purchase price information.

The rest of the paper sequentially discusses relevant literature, describes the model, and presents the results and concluding remarks.

## 2. Literature

A growing literature studies the antecedents and implications of shrouded add-on prices (where in-app purchases are one example of add-ons) in competitive markets (e.g., Ellison 2005, Gabaix and Laibson 2006). Because our research uniquely examines the endogenous platform choice of the degree of shrouding, we focus our review of this literature on how prior work answers the following two questions: whether add-on pricing benefits competing firms in equilibrium and whether such benefit, if it exists, increases in the number of uninformed consumers (i.e., consumers who do not observe in-app purchase prices when they make app purchases). Although prior literature has explained why a firm may choose to shroud its prices (e.g., Lal and Matutes 1994, Verboven 1999, Gabaix and Laibson 2006), a common result of these models that is robust to most model variations is the profit-irrelevance result: equilibrium firm profits earned on hidden add-on prices are competed away owing to equivalently diminished profits earned on base prices. Note that even though each firm chooses to shroud prices because a unilateral deviation is unprofitable, the net result from competing firms shrouding prices is that any profit from the shrouded price is competed away on the posted price. This profit-irrelevance result collides with the belief in the popular press that firms benefit from shrouding prices (e.g., Sullivan 2007, p. 4). Furthermore, this profit-irrelevance result is also at odds with some recent empirical findings: Chetty et al. (2009) and Ellison and Ellison (2009) provide evidence that withholding information about add-on prices can benefit firms; Brown et al. (2010) find that when add-on prices are hidden, firm profits increase in these fees.

Two recent papers seek to explain when the profitirrelevance result can be overturned. Ellison (2005) finds that add-on pricing improves firm profitability only if there is a significant and negative correlation between consumer price sensitivity and add-on valuation, which creates an adverse selection problem that softens price competition. Shulman and Geng (2013) demonstrate that vertical differentiation between sellers in both the quality of the add-on and the quality of the base product, when coupled with consumer-bounded rationality, can lead competing firms to profit from add-on pricing. Our research does not impose a correlation between consumer price sensitivity and add-on valuation, or quality asymmetry, or bounded rationality. Therefore, we find new conditions under which unadvertised prices can boost profitability. We also uniquely identify the optimal degree of shrouding by the platform rather than consider a discrete comparison of profit with shrouding with profit without shrouding. Figure 1 summarizes the state of the add-on pricing literature with regard to predicting the profitability of shrouded add-on prices.

Figure 1. (Color online) Add-On Pricing Literature’s Models and Findings About Equilibrium Profit Effect of Shrouding  
![](/api/attachments/75XS85J9/fulltext/images/c84acdf77d416b137eed23ecc39b089729008ecf617a57af6f5784a439fbb584.jpg)

Only one prior paper, Gabaix and Laibson (2006), touches on the question of whether a larger number of uninformed consumers will benefit competing firms more. Other papers in this literature either assume that the number of uninformed consumers is a constant (Lal and Matutes 1994, Verboven 1999, Ellison 2005) or consider a varying number of uninformed consumers yet are mute on its profit implications (Shulman and Geng 2013). Gabaix and Laibson (2006) find that individual competing firms will choose to shroud but that the net result is an equilibrium profit equivalent to the profit obtained with all prices advertised. In their model, firm profits are not affected by the number of uninformed consumers. To our knowledge, our paper is the first to show how the number of uninformed consumers has a nonmonotonic effect on equilibrium profits of competing firms. This finding allows for a richer understanding of the optimal degree of platform shrouding.

This research also adds to the IS literature on digital goods pricing (e.g., Gupta et al. 1997, Dewan et al. 2003, Sundararajan 2004, Choudhary 2009). In particular, our paper is related to the research stream on versioning of digital goods because the combined app and in-app content can be considered a more valuable “product” than just the app alone. Dewan et al. (2003) show that versioning of digital goods may benefit a firm in both monopoly and duopoly settings. Bhargava and Choudhary (2008) consider monopolistic versioning of digital goods and offer a general condition on when versioning is optimal. Although we can view an app without in-app purchases and with in-app purchases as two different versions of the app, the research differs from the prior work in that we focus on information shrouding.

This research is also related to the literature on freemium pricing (e.g., Cheng et al. 2014, Niculescu and Wu 2014). Cheng et al. (2014) compare featurelimited, time-locked and their hybrid versions of freemium. They find that the hybrid version dominates the other two. Niculescu and Wu (2014) compare featurelimited and uniform seeding versions of freemium. They find that the optimal choice depends on factors including prior bias, cross-module synergy, word-ofmouth effect, and the number of game periods. Quality learning is a core dynamic of the freemium literature—the free stage offers consumers a chance to better learn the quality of the full product. Our paper does not depend on this learning effect. Furthermore, the focus of our paper is the strategic implications of information shrouding regarding in-app purchase prices.

This research has several notable distinctions from the bundling literature (see, e.g., Nalebuff 2004, Ghosh and Balachander 2007, Chao and Derdenger 2013) First, the consumer’s in-app purchase decision requires prior purchase of the app. Second, we allow for in-app purchase prices to be unobserved by some consumers, whereas prices in the bundling literature are common knowledge. These two features create the recipe for a novel mechanism driving the profitability of in-app purchase pricing that is absent in the bundling literature. This also allows for consideration of how the presence of consumers who are uninformed about in-app purchase prices affects consumer welfare and profitability.

## 3. The Model

We consider a linear city model similar to the ones in Ellison (2005) and Shulman and Geng (2013). Two app developer firms, 1 and 2, engage in horizontal competition on a linear city with unit measure. Firm 1 (2) occupies location 0 (1). Each firm offers an app and has content available for in-app purchase. Each firm ${ } _ { j , \ l }$ $j = 1 , 2 ,$ , chooses its app price $p _ { j b }$ and its in-app purchase price $p _ { j a }$ . Although apps commonly have multiple in-app purchase options and prices, we treat $p _ { j a }$ as a summary measure of a segment’s in-app purchase payments in the interest of parsimony. Firms pay an exogenous proportion of revenue γ to the app platform but otherwise have zero marginal costs.

In the main model, the app platform chooses the degree to which consumers have access to information about in-app prices. For example, the Apple App Store and Google Play differ in their disclosure policies that affect the ease of access to in-app purchase information (see screenshots in Online Appendix A). Before the app firms choose their prices, the platform chooses its in-app purchase disclosure policy. We summarize this policy with the degree of difficulty in finding the in-app purchase price captured by $\beta .$ The platform sets $\beta$ to maximize combined revenue from the app firms. In an extension, we assume that the platform sets minimum disclosure requirements but that the app developers can choose the degree of shrouding up to the cap.

On the consumer side, we allow for three types of consumer heterogeneity. The first source of heterogeneity is derived from the observation that some consumers value the functionalities or contents available for in-app purchases, whereas others do not. We refer to the former (latter) as app-only (in-app) consumers. For example, most users of gaming apps do not purchase any in-app content.<sup>9</sup> In the interest of parsimony, we assume that the heterogeneity is discrete.<sup>10</sup> We normalize consumer population to 1 and assume there are 1 α app-only consumers, where $0 < \alpha < 1$ . Although we acknowledge that in some cases the value for the in-app purchases is driven by differences in the marginal utility of income (as is required for the profit-improvement result in Ellison 2005), the valuation of in-app purchase options also depends on personal relevancy, availability of alternatives, and the consumption situation, which may not always map onto the marginal utility of income.

The second source of consumer heterogeneity is driven by the common observation that consumers are heterogeneous in their search for and attentiveness to information. For instance, Brynjolfsson et al. (2004) find that consumers are heterogeneous in their propensity to scroll to lower screens on an internet shopbot. Early work on eye pattern movements [see Rayner (1998) for a review] shows that individuals vary widely in their eye-movement patterns, and more recently, Van der Lans et al. (2008) found that individuals differ in the effectiveness of individuals visual search strategies. We model this heterogeneity by parsimoniously assuming that consumer’s willingness to scroll to find in-app purchase information $\phi$ is uniformly distributed between 0 and 1 across all consumers.<sup>11</sup> Given the platform’s choice of $\beta ,$ consumers will choose to locate the in-app purchase price information if and only $\operatorname { i f } \phi > \beta .$ . We refer to consumers who ultimately observe in-app purchase price information as informed consumers. Given the uniform distribution of $\phi ,$ there will be $( 1 - \beta )$ informed consumers. We refer to the $\beta$ proportion of consumers who ultimately do not observe in-app purchase price information as uninformed consumers. The more challenging the app platform makes it to find in-app pricing on its platform, the more uninformed consumers there will be.

Note in a model of rational consumers that “there is no room in the scheme for unanticipated consequences” (Simon 1955, p. 103). Thus, our model of uninformed consumers applies equivalently to situations in which the uninformed consumers are not even informed that the in-app items carry a separate charge as well as when the uninformed consumers are informed that there is an in-app price but are not informed of its value. The equivalence comes from the fact that rationality requires that uninformed consumers form accurate expectations of in-app purchase prices in equilibrium.

The third consumer source of heterogeneity is driven by the observation that consumers have horizontal preferences between app firms. Within each consumer segment, consumers are also differentiated by a stylized taste parameter θ that is uniformly distributed on 0, 1 and represents a consumer’s location on the linear city. Consumer i at location $\theta _ { i }$ suffers a fit cost of $t \theta _ { i } ( t ( 1 - \theta _ { i } ) )$ if she purchases from firm 1 (2).

We solve for the subgame perfect Nash equilibrium in which the expectations of uninformed consumers are confirmed to be rational. Let $\hat { p } _ { j a } ( p _ { 1 b } , p _ { 2 b } )$ denote uninformed consumers’ expectation of firm $j ^ { \prime } \mathbf { s }$ in-app purchase price on observing both firms’ app prices, $\bar { j } = 1 , 2$ . All consumers have unit demand of the app with reservation value $v _ { b }$ , and in-app consumers have unit demand of the in-app purchase item with reservation value $v _ { a }$ . Consistent with Ellison (2005), Gabaix and Laibson (2006), and Shulman and Geng (2013), we assume that $v _ { b }$ is large enough for full market coverage to avoid having key findings obscured by technical discussions of the magnitude of $v _ { b } .$ .

Our definition of uninformed consumers and inapp content purchasing merits further discussion. Alternatively, consumers may be informed about inapp purchase prices but uninformed about how often they will be incurred. Provided that consumers form rational expectations about the combined value of in-app content, such a world is equivalent to our formulation.<sup>12</sup>

We assume that $t > v _ { a } / 2 ;$ ; that is, the level of horizontal differentiation is sufficiently large relative to the value of the in-app purchase item. This assumption rules out the possibility that a firm abandons all informed consumers in pursuit of a maximum margin on the in-app purchase of uninformed consumers. Table 1 provides a list of notations used in this model.

Our timeline, depicted in Figure 2, assumes that the platform leads in its choice of in-app purchase price disclosure policy. Subsequently, app firms simultaneously choose app prices and then simultaneously choose in-app purchase prices. Given the heterogeneity in consumer propensity to scroll for in-app purchase prices, some consumers observe only app prices, and other consumers observe both prices. On the basis of the observed information, consumers choose which app to buy. After purchase, all consumers observe in-app purchase prices from the purchased app and then choose whether to make the in-app purchase. Technically, a consumer can buy the rival app after observing the in-app purchase price, but it is straightforward to show that such behavior is not optimal. The sequential choice of advertised app prices and in-app purchase prices is consistent with convention established in the add-on pricing literature (e.g., Lal and Matutes 1994, Ellison 2005) and thus allows for isolation of the factors driving our unique results. Moreover, the unique results are subsequently shown to hold in an alternative timeline involving simultaneous price setting.

Table 1. Parameters and Decision Variables

<table><tr><td>Symbol</td><td>Definition</td></tr><tr><td> $\gamma$ </td><td>Platform&#x27;s share of revenue</td></tr><tr><td> $\beta$ </td><td>Platform&#x27;s shrouding level</td></tr><tr><td> $\phi$ </td><td>Consumer willingness to scroll to find in-app purchase information</td></tr><tr><td> $p_{jb}$ </td><td>App price from firm  $j$ </td></tr><tr><td> $p_{ja}$ </td><td>In-app purchase price from firm  $j$ </td></tr><tr><td> $v_b$ </td><td>Consumer reservation value of the app</td></tr><tr><td> $v_a$ </td><td>Consumer reservation value of the in-app purchase item</td></tr><tr><td> $t$ </td><td>Transportation cost for consumers</td></tr><tr><td> $\theta_i$ </td><td>Consumer  $i$ &#x27;s taste parameter</td></tr><tr><td> $\alpha$ </td><td>Proportion of in-app consumers</td></tr></table>

Figure 2. (Color online) Timeline of the Game  
![](/api/attachments/75XS85J9/fulltext/images/d85b6f0d76240d8ff337acfd6b7b183c172e6a3dd4ca55f8702e6ef366c4d8de.jpg)

As shown in Figure 2, we assume that uninformed consumers have to purchase the app before observing the in-app purchase prices. This fits the scenario in which a consumer discovers the prices of desired functionality or contents of the in-app purchase items as they are viewed within the app. We further assume that once a consumer has purchased the app from a firm, she is stuck with this firm in that she can only pick between making the in-app purchase from the same firm or not to purchase it.

## 4. Results

We first derive outcomes for any given stage 0 platform choice of $\beta .$ We subsequently identify the equilibrium $\beta ^ { * }$ . Using backward induction, we first characterize consumer choices in stages 3 and 4 conditional on observed app prices and uninformed consumer expectations. We then discuss rational beliefs of uninformed consumers in stage 3 and firm in-app prices in stage 2. Finally, we discuss equilibrium app pricing, firm profits, and consumer surplus.

The behaviors of each of the three consumer segments must first be analyzed: 1 α app-only consumers, $\alpha ( 1 - \beta )$ informed consumers, and $\alpha \beta$ uninformed consumers. The last two segments together are referred to as in-app consumers. In stage 4 and conditional on stage 3 purchase of the app, in-app consumers make an in-app purchase from the same firm if the price is no more than $v _ { a }$ . In the derivation of demand equations, we consider only $p _ { j a } \leq v _ { a } ,$ which will prove to be optimal in equilibrium.

In stage $^ { 3 , }$ informed consumers observe in-app prices $p _ { 1 a }$ and $p _ { 2 a }$ before making their app purchase decisions. The location of the marginal informed consumer that is indifferent between the two firms $\theta _ { I }$ satisfies $v _ { b } + v _ { a } - t \theta _ { I } - p _ { 1 b } - p _ { 1 a } = v _ { b } + \ v _ { a } - t ( 1 - \theta _ { I } ) - p _ { 2 b } - \ p _ { 2 a } .$

Therefore, $\theta _ { I } = 1 / 2 + ( p _ { 2 b } + p _ { 2 a } - p _ { 1 b } - p _ { 1 a } ) / ( 2 t )$ . Uninformed consumers do not observe in-app prices before making the decision regarding which app to buy; instead, they form rational expectations of these in-app purchases $\hat { p } _ { 1 a } ( p _ { 1 b } , p _ { 2 b } )$ and $\hat { p } _ { 2 a } ( p _ { 1 b } , p _ { 2 b } )$ . Accordingly, the marginal uninformed consumer is located at $\theta _ { U } = 1 / 2 + ( p _ { 2 b } + \hat { p } _ { 2 a } ( p _ { 1 b } , p _ { 2 b } ) - p _ { 1 b } - \hat { p } _ { 1 a } ( p _ { 1 b } , p _ { 2 b } ) ) /$ 2t . Last, the marginal app-only consumer is located at $\theta _ { A } = 1 / 2 \overset { \cdot } { + } ( p _ { 2 b } - \bar { p } _ { 1 b } ) / ( 2 t )$ . Therefore, the total number of in-app consumers and app-only consumers that go to firm j are, respectively,

$$
\begin{array}{c} \# I n A p p _ {j} = \alpha \bigg [ (1 - \beta) \bigg (\frac {1}{2} + \eta (j) \frac {p _ {2 b} + p _ {2 a} - p _ {1 b} - p _ {1 a}}{2 t} \bigg) \\ \qquad + \beta \bigg (\frac {1}{2} + \eta (j) p _ {2 b} + \hat {p} _ {2 a} (p _ {1 b}, p _ {2 b}) \\ \qquad - p _ {1 b} - \hat {p} _ {1 a} (p _ {1 b}, p _ {2 b}) \bigg / (2 t) \bigg) \bigg ], \\ \# A p p O n l y _ {j} = (1 - \alpha) \bigg (\frac {1}{2} + \eta (j) \frac {p _ {2 b} - p _ {1 b}}{2 t} \bigg), \end{array}
$$

where $\eta ( j ) = 1 \ : \mathrm { i f } \ : j = 1$ , and $\eta ( j ) = - 1 \mathrm { i f } j = 2$ . Demands for each firm’s app $D _ { j b }$ and in-app purchases $D _ { j a }$ are then $D _ { j b } = \# A p \bar { p O } n l y _ { j } + \# I n A p p _ { j }$ and $D _ { j a } = \# I \dot { n } A p p _ { j }$ Therefore, for any given app prices and in-app prices, firm profits are

$$
\pi_ {j} = (1 - \gamma) (p _ {j b} D _ {j b} + p _ {j a} D _ {j a}),\tag{1}
$$

for $j = 1 , 2$ . We next analyze firm in-app purchase pricing, which will affect consumers’ rational beliefs

## 4.1. Rational Beliefs

Given any app prices $p _ { 1 b }$ and $p _ { 2 b } ,$ , we solve for the inapp purchase prices of firms $\left( p _ { 1 a } ^ { * } , p _ { 2 a } ^ { * } , \hat { p } _ { 1 a } , \hat { p } _ { 2 a } | p _ { 1 b } , p _ { 2 b } \right)$ such that

• Firms optimize in-app purchase prices given uninformed consumer beliefs; that is,

$$
\begin{array}{r} p _ {j a} ^ {*} = \underset {p _ {j a}} {\arg \max} \pi_ {j} (p _ {j a}, p _ {- j a} ^ {*}, \hat {p} _ {1 a}, \hat {p} _ {2 a} | p _ {1 b}, p _ {2 b}), \\ \text {for} j = 1, 2; \text {and} \end{array}\tag{2}
$$

• Firms anticipate that the stage 3 beliefs of uninformed consumers will be consistent with the equilibrium firm strategy; that is,

$$
\hat {p} _ {j a} = p _ {j a} ^ {*}, \quad \mathrm{forany} (p _ {1 b}, p _ {2 b}) \mathrm{and} j = 1, 2.\tag{3}
$$

To avoid repetition in describing actions, payoffs, and beliefs regarding each firm, we let <sub>−</sub>j indicate a firm other than firm j. We only need to consider beliefs of uninformed consumers because the belief of app-only consumers is not relevant to their actions, and informed consumers will directly observe in-app purchase prices before making app purchase decisions. Solutions to (2) for $j = 1$ , 2 can be derived by using (1) and solving the first-order conditions. The following lemma describes the rational beliefs.

Lemma 1. Given ${ p } _ { 1 b } ,$ p<sub>2b</sub>, $\hat { p } _ { 1 a } ( p _ { 1 b } , p _ { 2 b } )$ , and $\hat { p } _ { 2 a } ( p _ { 1 b } , p _ { 2 b } )$ assume that $\omega _ { j } \leq \omega _ { - j } . ^ { 1 3 }$ Optimal in-app purchase prices are

$$
(p _ {j a} ^ {*}, p _ {- j a} ^ {*}) = \left\{ \begin{array}{l l} (\omega_ {j}, \omega_ {- j}) & \text {if} \omega_ {- j} <   v _ {a}, \\ (\mu_ {j}, v _ {a}) & \text {if} \mu_ {j} <   v _ {a} \leq \omega_ {- j}, \\ (v _ {a}, v _ {a}) & \text {if} \mu_ {j} \geq v _ {a}, \end{array} \right.
$$

where $\begin{array} { r } { \omega _ { j } \triangleq \frac { t } { 1 - \beta } - p _ { j b } + \frac { \beta } { 3 ( 1 - \beta ) } \left( p _ { - j b } + \hat { p } _ { - j a } ( p _ { 1 b } , p _ { 2 b } ) - p _ { j b } - \right. } \end{array}$ $\hat { p } _ { j a } ( p _ { 1 b } , p _ { 2 b } ) )$ and

$$
\begin{array}{r l} \mu_ {j} \triangleq & - p _ {j b} + \frac {1}{2} \bigg [ (p _ {- j b} + v _ {a}) + \frac {t}{1 - \beta} \\ & + \frac {\beta}{1 - \beta} \big (p _ {- j b} + \hat {p} _ {- j a} (p _ {1 b}, p _ {2 b}) - p _ {j b} - \hat {p} _ {j a} (p _ {1 b}, p _ {2 b}) \big) \bigg ]. \end{array}\tag{4}
$$

All proofs are in the online appendix. Lemma 1 states what the optimal in-app purchase prices are for any belief system. However, rational beliefs call for a particular set of beliefs in which the expected prices match the realized prices. Equating the optimal price with the expected price using (3) and (4), we can then solve for the rational belief for uninformed consumers given any app prices $p _ { 1 b }$ and $p _ { 2 b }$

Proposition 1. Given $p _ { 1 b } ,$ p , assume that $p _ { j b } \ge p _ { - j b }$ . The unique rational expectations of in-app purchase prices for uninformed consumers are the following:

$$
\mathrm{i.} (\hat {p} _ {j a}, \hat {p} _ {- j a}) = \left(\frac {t}{1 - \beta} - p _ {j b}, \frac {t}{1 - \beta} - p _ {- j b}\right) i f p _ {- j b} > \frac {t}{1 - \beta} - v _ {a}.
$$

ii. $\begin{array} { r } { ( \hat { p } _ { j a } , \hat { p } _ { - j a } ) = \left( \frac { t + p _ { - j b } + v _ { a } } { 2 - \beta } - p _ { j b } , v _ { a } \right) \ i f \ p _ { - j b } \leq \frac { t } { 1 - \beta } - v _ { a } } \end{array}$ and $p _ { j b } > \frac { t + \dot { p } _ { - j b } - \dot { v _ { a } } ( 1 - \beta ) } { 2 - \beta } .$

$$
\text { iii. } (\hat {p} _ {j a}, \hat {p} _ {- j a}) = (v _ {a}, v _ {a}) \text {   if   } p _ {j b} \leq \frac {t + p _ {- j b} - v _ {a} (1 - \beta)}{2 - \beta}.
$$

The result in part (iii) of Proposition 1 is consistent with prior works, including Lal and Matutes (1994), Verboven (1999), Ellison(2005),andGabaix and Laibson (2006). When both firms charge low enough app prices, uninformed (but rational) consumers expect firm j to charge the maximum in-app purchase prices $( \mathrm { i . e . , }$ the consumer’s reservation value on its in-app content), and consumers take this into account in their purchase decisions.

Part (i) of Proposition 1, in contrast, contributes a new insight to the literature: when both firms’ app prices are higher than $t / ( 1 - \beta ) - v _ { a } ,$ , instead of expecting a maximal possible in-app purchase price, uninformed consumers rationally expect firm $j ^ { \prime } \mathbf { s }$ in-app purchase price to be an inner solution that linearly decreases in its app price. This negative correlation between the observed app price and the in-app purchase price subsequently softens the competition between the app firms: a firm’s price cut on the app price is now less effective in attracting uninformed consumers than that without in-app purchase because the uninformed consumer expects a lesser cut on the total price (i.e., app price plus in-app purchase price) she pays.

Notice that the possible existence of enough informed consumers is instrumental to this new finding: for any given $p _ { j b } , p _ { j b } > t / ( 1 - \beta ) - v _ { a }$ will not hold if $\beta$ is close enough to 1. Therefore, our assumption that consumers are heterogeneous in their willingness to scroll to find information, resulting in both informed and uninformed consumers coexisting, plays a pivotal role in driving this new finding. Although Gabaix and Laibson (2006) also have a mix of informed and uninformed consumers, all consumers who are informed of the unadvertised price will choose to substitute away from purchasing it. Our finding is driven by the fact that some uninformed consumers will still choose to purchase the in-app content.

The intuition is best seen (although not limited to) when the vast majority of in-app consumers is informed $( \mathrm { i . e . , } \beta$ is very close to 0). In this case, and if we assume that ma $\times \{ \omega _ { j } , \omega _ { - j } \} < v _ { a }$ is true, which indeed holds for any given stage 1 app prices and any consumer belief as long as $\beta$ is small enough, firm j chooses in-app purchase price $p _ { j a } ^ { * } = \omega _ { j }$ . Therefore,

$$
\begin{array}{r} \frac {\partial p _ {j a} ^ {*}}{\partial p _ {j b}} = - 1 + \frac {1}{3 (1 - \beta_ {j})} \Bigg [ \beta_ {- j} \frac {\partial (p _ {- j b} + \hat {p} _ {- j a} (p _ {1 b} , p _ {2 b}))}{\partial p _ {j b}} \\ - \beta_ {j} \frac {\partial (p _ {j b} + \hat {p} _ {j a} (p _ {1 b} , p _ {2 b}))}{\partial p _ {j b}} \Bigg ]. \end{array}
$$

As long as all prices and expectations are finite, this derivative is negative if $\beta$ is small enough. In other words, the existence of a large number of informed consumers incentivizes a firm to charge an in-app purchase price inversely related to its app price. The lower the app price, the higher is the in-app purchase price regardless of the beliefs of uninformed consumers. This, in turn, implies that uninformed consumers’ rational expectation needs to take app prices into account rather than ignoring them. Although the intuition is best seen when $\beta$ is small, part (i) of Proposition 1 shows that this intuition applies for a wide range of values for $\beta$ as long as $p _ { j b } > t / ( 1 - \beta ) - v _ { a }$ holds for both $j = 1 , 2 .$

The result regarding $\hat { p } _ { 1 a } ( p _ { 1 b } , p _ { 2 b } )$ in part (ii) of Proposition 1 is analogous to part (i), with one difference. Because now uninformed consumers observe a very low $p _ { 2 b }$ , they rationally expect firm $- j$ to charge the maximum in-app purchase price $v _ { a }$ . The fact that firm $- j ^ { \prime } \mathbf { s }$ in-app purchase price is now binding at $v _ { a }$ influences firm $j ^ { \prime } \boldsymbol { \mathrm { s } }$ optimization problem, and as a response, firm j sets the in-app purchase price at a level lower than $t / ( 1 - \beta ) - p _ { j b }$ , although the price still decreases in $p _ { 1 b }$

We next study firm profits and consumer surplus by solving for the stage 1 app pricing game.

## 4.2. Firm Pro<sup>fi</sup>ts and Platform Disclosure Policy

In stage 1, the app firms simultaneously choose app prices to maximize profit. The equilibrium prices and profits are presented in the following proposition.<sup>14</sup>

Proposition 2. In the hidden in-app pricing game:

i. If $\beta \leq v _ { a } / ( t + v _ { a } )$ , in equilibrium, firms set in-app purchase prices $\begin{array} { r } { p _ { 1 a } ^ { * } = p _ { 2 a } ^ { * } = \frac { \beta t } { 1 - \beta } } \end{array}$ and app prices $p _ { 1 b } ^ { * } =$ $p _ { 2 b } ^ { * } = t .$ App firm profits are $\begin{array} { r } { \dot { \pi } _ { 1 } ^ { * } = \pi _ { 2 } ^ { * } = ( 1 - \gamma ) \big ( 1 + \frac { \alpha \beta } { 1 - \beta } \big ) \frac { t } { 2 } , } \end{array}$ and the platform earns $\begin{array} { r } { \pi _ { P } = \gamma t \big ( 1 + \frac { \alpha \beta } { 1 - \beta } \big ) } \end{array}$

ii. If $\beta > v _ { a } / ( t + v _ { a } )$ , in equilibrium, firms set in-app purchase prices $p _ { 1 a } ^ { * } = p _ { 2 a } ^ { * } = v _ { a } . \mathrm { ~ } f t > \alpha v _ { a } ,$ , then app prices are $p _ { 1 b } ^ { * } = p _ { 2 b } ^ { * } = t - \alpha v _ { a }$ , app firm profits are $\pi _ { 1 } ^ { * } = \pi _ { 2 } ^ { * } =$ $( 1 - \gamma ) \frac { t } { 2 } ,$ and the platform earns $\pi _ { P } = \gamma t . \ I f t < \alpha v _ { a } ,$ , then app prices are zero, app firm profits are $( 1 - \gamma ) \alpha v _ { a } / 2$ , and the platform earns $\pi _ { P } = \alpha \gamma v _ { a }$

Proposition 2 highlights how the app platform’s disclosure policy affects the pricing decisions of competing app firms. Previous research on unadvertised prices $( \mathrm { e . g . } ,$ , Lal and Matutes 1994) suggests that the platform’s disclosure policy should be irrelevant to firm profits given symmetric firms and an insignificant correlation between interfirm price sensitivity and add-on usage. Even Gabaix and Laibson (2006), who find why one firm may choose to shroud its prices, show that equilibrium profits are unaffected by the shrouding. However, we find that the heterogeneity in consumers’ willingness to scroll to find in-app prices can overturn this profit-irrelevance result. In fact, if the platform changes its disclosure policy regarding the prominence of in-app purchase prices, the pricing and app firm profits are in fact affected.

Consider several special cases to understand the driver of this result. If there are no app-only consumers $( \mathrm { e . g . , } \alpha = 1$ and all consumers buy in-app content), the result still holds. Rather, the novel finding is driven by the consideration of both informed in-app content purchasers and uninformed consumers. To see this, consider that the full-information game can be computed by setting $\beta = 0 ,$ , which leads to the stan dard profitability of $\pi _ { 1 } = \pi _ { 2 } = ( 1 - \gamma ) t / 2$ , which is also equivalent to equilibrium profit in the game in which all consumers are uninformed $\left( \mathbf { e . g . } , \beta = 1 \right)$ .

The analyses of the special cases also illuminate why the result contrasts with what is implied by the model of Gabaix and Laibson (2006). In Gabaix and Laibson (2006), informed consumers substitute away from add-on purchase. For example, a hotel gues avoids paying for an in-room phone by carrying her own cell phone. The assumptions of Gabaix and Laibson (2006) imply that if firms shroud add-on prices, all informed consumers will substitute in equilibrium. As a result, none of the informed consumers in their paper will purchase add-ons from the firms. In other words, their model does not have a consumer segment similar to the $\alpha ( 1 - \beta )$ informed in-app content purchasers in our model, and the possibility of $\alpha ( 1 - \beta ) > 0$ is critical to our novel finding.

The finding thus identifies a novel mechanism for why hidden in-app purchases can increase profit. In the case of $\beta \leq v _ { a } / ( t + v _ { a } )$ , firms will pick app prices in stage 1 such that the rational expectation of uninformed consumers will be a decreasing function of the app price according to part (i) of the rational belief system specified in Proposition 1. Consequently, uninformed consumers, in making the app purchase decision, are less price sensitive with respect to the app prices than the informed consumers. Firms then face less competitive pressure in pricing apps compared with a standard pricing game and thus avoid losses from loss-leader pricing. By contrast, in stage $^ { 2 , }$ firms can still gain from the information disadvantage of uninformed consumers by setting profitable in-app prices, as shown in part (i) of Proposition 2. Part (i) of Proposition 2 thus shows that the existence of enough informed consumers enables firms to avoid the perils of loss-leader pricing while reaping the benefit of high margins on in-app purchases.

This mechanism is distinct from that of Ellison (2005), which requires a significant correlation between add-on usage and interfirm price sensitivity to find profit improvement associated with shrouded prices. Ellison’s mechanism is one of adverse selection: the customers attracted by price cuts are not the customers firms would most like to attract. As best seen with $\alpha = 1$ , customers attracted by the price cut are equally attractive to the firm (i.e., the same total price is paid) in our model. Instead, the uninformed consumers’ belief system flattens out the demand curve and softens competition.

This mechanism is also distinct from that of Shulman and Geng (2013), which in its summary table 3 high lights that quality asymmetry between the firms is indispensable for their profit-improvement results. We do not model quality differentiation in this paper.

Note that prior research considering informed and uninformed consumers, including Gabaix and Laibson (2006) and Shulman and Geng (2013), has studied the equilibrium profit implications of discrete shrouding when uninformed consumers are naive (i.e., they irrationally expect add-on prices to be zero at the time of base purchase), whereas the literature is lacking on the consequences of rational uninformed consumers. In fact, one can infer on the basis of prior results in both cited add-on pricing papers that replacing rational uninformed consumers in our paper with naive uninformed consumers will reproduce the profitirrelevance result. Therefore, rationality regarding in-app content prices has unique consequences.

Intuitively, as long as there are a reasonable number of rational uninformed consumers, our core insight that they rationally expect in-app purchase prices to decrease in the app price will still hold. One can thus conjecture that allowing a mix of rational and boundedly rational consumers will still produce the competition-softening effect, provided that there are enough rational uninformed consumers.

We now turn our attention to the app platform’s optimal choice of $\beta .$ . The platform chooses $\beta$ to maximize $\pi _ { P } = \gamma \sum _ { j = 1 } ^ { 2 } \ : ( p _ { j a } ^ { * } D _ { j a }  + \bar { p _ { j b } ^ { * } } D _ { j b } )$ . We present the results in the following proposition.

Proposition 3. The platform will choose $\beta ^ { * } = v _ { a } / ( t + v _ { a } )$ and earn profit $\pi _ { P } = \gamma ( t + \alpha v _ { a } )$ , whereas app firms earn $\pi _ { 1 } = \pi _ { 2 } = ( 1 - \gamma ) ( t + \alpha v _ { a } ) / 2 .$

Proposition 3 makes several contributions to the literature and to practice. First, hidden in-app purchase prices actually boost equilibrium app firm profit. This is seen when comparing equilibrium profit with the standard profit of $( \bar { 1 } - \gamma ) \bar { t } / 2$ . Second, this happens as the platform chooses an intermediate level of prominence given to in-app purchase prices in equilibrium. As a consequence, the decision by platforms such as Apple and Google to display in-app purchase price information actually increases their profit and the profit of their app developers. However, the platforms have buried the information to some degree (see Online Appendix A for examples), thereby creating uninformed consumers from the population, who have a lower propensity to scroll, as described in Byrnjolfsson et al. (2004). The heterogeneity in consumers’ discovery of in-app purchase information is key to the result. Previous papers on rational consumers have studied both extremes—having all in-app consumers informed or all uninformed—yet not the middle; this model thus highlights the importance of explicitly accounting for heterogeneity in the consumers’ propensity to scroll and the platform’s ability make the in-app purchase price information less prominent.

To understand Proposition $^ { 3 , }$ consider what happens when the in-app purchase price is hidden from too many consumers. As a consequence, all consumers rationally expect in-app purchase prices to be set at their maximum. Thus, if the platform chooses a policy such that there are too many uninformed consumers, it can actually intensify competition among app developers and reduce the revenue that they share with the app platform. It is only when the price information is transparent to a reasonable number of informed consumers $( \mathrm { i . e . , ~ } 0 < \beta < \beta _ { 1 } )$ ) that the common intuition of profit increasing in $\beta$ holds.

## 4.3. Consumer Welfare

Initially, platforms did not require disclosure of inapp purchase prices. In our model, this would lead to $\beta = 1$ uninformed consumers. Even if some consumers obtained in-app purchase price information via word of mouth (a possibility abstracted from in our model), the number of uninformed consumers would be relatively high. Intuition would suggest that the recent move toward more transparency in in-app purchase prices would increase consumer welfare. We identify the effect of greater transparency in the following proposition. For notational convenience, denote

$$
\hat {\beta} \triangleq \left\{ \begin{array}{l l} 0 & \text { if } \quad t > \alpha v _ {a} \\ \frac {\alpha v _ {a} - t}{\alpha v _ {a} - (1 - \alpha) t} & \text { if } \quad t <   \alpha v _ {a} \end{array} \right.
$$

and

$$
\tilde {\beta} \triangleq \left\{ \begin{array}{l l} \frac {(1 - \alpha) v _ {a}}{t + (1 - \alpha) v _ {a}} & \text {if} \quad t > \alpha v _ {a} \\ 1 - \frac {t}{v _ {a}} & \text {if} \quad t <   \alpha v _ {a}. \end{array} \right.
$$

Proposition 4. Total consumer welfare is greater when a large proportion of the market is uninformed about in-app prices $( i . e . , \ \beta > v _ { a } / ( t + v _ { a } ) )$ than when a small proportion of the market is uninformed about in-app prices $( i . e . ,$ $\hat { \beta } < \beta < v _ { a } / ( t + v _ { a } ) )$ . App-only consumer welfare is greater for all $\beta > v _ { a } / ( t + v _ { a } )$ than for $0 < \beta < v _ { a } / ( \dot { t } + v _ { a } )$ . In-app consumer welfare is greater for all $\beta > v _ { a } / ( t + v _ { a } )$ than for $\widetilde { \beta } < \beta < v _ { a } / ( t + v _ { a } )$

Proposition 4 suggests that recent efforts by app platforms to require more transparency of in-app purchases can actually reduce consumer welfare. The result arises because a greater number of informed consumers actually prevents an app developer from charging a monopoly in-app purchase price. The counterintuitive result of Proposition 4 stems from the fact that the uninformed consumers’ rational expectations regarding the relationship between the app price and the in-app purchase price diminish competitive intensity in app prices. This has a strictly negative impact on welfare for app-only consumers, although the effect on welfare for in-app consumers depends on the effect relative to the savings on the in-app purchases. Proposition 4 thus demonstrates again that considering the extremes of the $\beta$ range results in a different set of findings than considering the interior.

## 4.4. Robustness Check: Simultaneous Pricing Decisions

In the main model, we assumed that in-app purchase prices are set subsequent to app prices. This follows the convention of Ellison (2005) and Lal and Matutes (1994). In this subsection, we consider an alternative scenario whereby app prices and in-app purchase prices are set simultaneously. Although there is a unique equilibrium under sequential pricing, in this subsection, we demonstrate that simultaneous pricing implies multiple equilibria and discuss when our main findings are preserved.

The uniqueness of equilibrium under sequential pricing is driven by the fact that the in-app purchase pricing is a subgame following app pricing. In stage 2 of the in-app purchase pricing game (as shown in Figure 2), the sequential timing of the game requires any firm j to optimally set its in-app purchase price conditional on both app prices, that is, $p _ { j a } ^ { * } \left( p _ { j b } , p _ { - j b } \right)$ , as depicted in Lemma 1. Any off-equilibrium app price deviation by firm j will then trigger a corresponding change of $p _ { j a } ^ { \ast } ,$ as dictated by Lemma 1. In other words, under sequential pricing, uninformed consumers rationally believe that the unobserved in-app purchase prices are particular functions of the observed app prices, as dictated by rational expectations—the uniqueness of this belief structure is then shown in Proposition 1.

Under simultaneous pricing, however, no such sequential relationship between app prices and inapp purchase prices exists. If uninformed consumers observe an off-equilibrium app price by a firm, there is no restriction on how these consumers construe their belief of the firm’s unobserved in-app purchase price. The multiple possible belief structures lead to multiple possible equilibria. We consider symmetric linear belief structures.<sup>15</sup> On observing firm $j ^ { \prime } \mathbf { s }$ app price $p _ { j b } ,$ consider the following belief structure for uninformed consumers:

$$
\hat {p} _ {j a} (p _ {j b}) = A p _ {j b} + H,
$$

where A and H are constants, $j = 1 , 2$ . To avoid having technical details distract the focus on key insights of this robustness check, we assume that the belief structure will not lead to beliefs that the in-app purchase price exceeds $v _ { a } .$ . This is the case when the number of uninformed consumers is not too large. When the number of uninformed consumers is very large, in equilibrium, in-app purchase prices will be set at the boundary value $v _ { a }$ similar to part (ii) of Proposition 2, and thus beliefs will be independent of the app prices.

Given this belief structure, both firms simultaneously optimize their app prices and in-app purchase prices. Furthermore, their equilibrium in-app purchase prices need to be consistent with the belief structure (as evaluated at the equilibrium point of app prices). The resulting equilibrium is shown in the following proposition.

Proposition 5. In the simultaneous pricing game, there is a continuum of equilibria. For any

$$
A \in \left[ - 1 - \frac {2 \sqrt {\alpha (1 - \alpha) (1 - \beta)}}{\alpha \beta}, - 1 + \frac {2 \sqrt {\alpha (1 - \alpha) (1 - \beta)}}{\alpha \beta} \right],
$$

there is an equilibrium with app prices $p _ { 1 b } ^ { * } = p _ { 2 b } ^ { * } =$ $\frac { ( 1 - \alpha - \beta - A \alpha \beta ) t } { ( 1 - \alpha ) ( 1 - \beta ) } ,$ , in-app purchase prices $\begin{array} { r } { p _ { 1 a } ^ { * } = p _ { 2 a } ^ { * } = \frac { ( 1 + A \alpha ) \beta t } { ( 1 - \alpha ) ( 1 - \beta ) } , } \end{array}$ belief structure

$$
\hat {p} _ {j a} (p _ {j b}) = A p _ {j b} + \frac {((1 + A) (1 + A \alpha) \beta - A (1 - \alpha)) t}{(1 - \alpha) (1 - \beta)},
$$

and each app firm profit $\begin{array} { r } { ( 1 - \gamma ) ( \frac { t } { 2 } - \frac { A \alpha \beta t } { 2 ( 1 - \beta ) } ) } \end{array}$

Again recall that, for a concise discussion, we only consider cases in which $\begin{array} { r } { \beta < \frac { v _ { a } ( 1 - \alpha ) } { t ( 1 + A \alpha ) + v ( 1 - \alpha ) } } \end{array}$ so that $\hat { p } _ { j a } ^ { \phantom { \dagger } }$ will not exceed $v _ { a } .$ . Proposition 5 demonstrates that, under simultaneous pricing, equilibrium prices and profits depend on the belief structure of uninformed consumers. Note that Proposition 1 under the sequential pricing game corresponds to the special case of $A = - 1$ under the simultaneous pricing game.

The following corollary summarizes the profit implications of Proposition 5.

Corollary 1. In the simultaneous pricing game, hidden inapp purchase prices improve app firm profits if uninformed consumers believe a negative correlation between a firm’s app price and its hidden in-app purchase price (i.e., $A < 0 ) .$ . If $\alpha = 1$ , then $A = - 1$ is the only rational belief. Profit irrelevance of hidden in-app purchase prices holds if the belief structure is constant and independent of the app prices $( i . e .$ $A = 0 )$

Corollary 1 shows that sequential pricing decisions are not necessary for shrouded in-app purchase prices to improve app profitability relative to a complete information game in which $\beta = 0$ . This contrasts with the standard profit-irrelevancy result from the addon pricing literature and is consistent with part (i) of Proposition 2 for any $A < 0$ . That is, the results are preserved when in-app purchase prices and app prices are set simultaneously if consumers believe that app firms with higher in-app purchase prices try to lure customers with lower app prices. Note that an inverse relationship between the price that is posted and the price that is hidden is consistent with the empirical finding of Derdenger et al. (2012). Moreover, behavioral research on belief formation suggests that an “item of information about a given object will thus have implications for many other beliefs about the object” (Fishbein and Ajzen 1975, p. 214). Thus, logic would suggest an inferential belief system in which the app price serves as a cue affecting the beliefs about the in-app purchase price $( \mathrm { i . e . , } A \ne 0 )$ The qualitative results of part (ii) of Proposition 2 and Proposition 3 can similarly be replicated when considering the boundary condition of $p _ { j a } = v _ { a }$

## 5. Shrouding by App Firms

In the main model, the platform controls the disclosure policy regarding in-app purchase prices. This is consistent with the example of the Apple App Store, which added disclosure notices on apps in 2014 and instructs developers, “[t]o offer in-app purchases inside your app, you must add in-app purchase information to your app in iTunes Connect.”<sup>16</sup> However, before this policy, app developers possessed the capability of shrouding their own in-app purchase prices. For example, one app developer, Dolphin Play, changed the degree of shrouding before Apple’s disclosure rules. 17 Given the changes in policies and the potential for new app platforms to gain prominence (e.g., Slack and Alexa), we consider an alternative shrouding scenario— shrouding by app developers—in this section.<sup>18</sup>

Specifically, before setting prices, app developer $j ,$ $j = 1 , 2 ,$ , chooses its own shrouding level $\beta _ { j } \ ( \mathrm { i . e . }$ , the degree of difficulty for consumers to find its in-app price). In-app consumers will choose to locate the inapp purchase price information of this app if and only if $\phi > \beta _ { j } , j = 1 , 2 ,$ , where a consumer’s willingness to scroll φ is defined the same as in the main model. For ease of exposition and without loss of generality, we assume that $\beta _ { 1 } \leq \beta _ { 2 }$ in this section.<sup>19</sup> Accordingly, inapp consumers can be classified into three groups: consumers with $\phi \geq \beta _ { 2 }$ will observe in-app purchase prices of both firms—we refer to them as fully informed consumers; consumers with $\beta _ { 2 } > \phi \geq \beta _ { 1 }$ will observe in-app purchase prices of only firm 1—we refer to them as partially informed consumers; and the rest of the in-app consumers do not observe any in-app purchase price—we refer to them as uninformed consumers. Given the uniform distribution of $\phi ,$ there will be $\alpha ( 1 - \beta _ { 2 } )$ fully informed consumers, $\alpha ( \beta _ { 2 } - \beta _ { 1 } )$ partially informed consumers, and $\alpha \beta _ { 1 }$ uninformed consumers.

The platform still plays a prominent role in this section in that it can set policy limiting the firms’ shrouding behavior. Specifically, we assume that the app platform sets a disclosure policy ${ \bar { \boldsymbol { \beta } } } ,$ which is a mandatory upper bound to any app firm’s shrouding level $( \mathrm { i . e . , } \bar { \beta _ { j } } \bar { \leq } \bar { \beta } ,$ for $j = 1 , 2 )$ . This setup is consistent with practice: al though developers may engage in price shrouding, their strategies nonetheless are bounded by the mandatory disclosure policies that the platforms mandate in their respective app markets. All other setups and notations are the same as in the main model. Figure 3 shows the timeline of the model in this section.

The sequence of analysis is analogous to the main model: we first derive outcomes for any given stage 0 shrouding levels $\beta _ { 1 }$ and $\beta _ { 2 }$ . We then identify the equilibria $\beta _ { 1 } ^ { * }$ and $\beta _ { 2 } ^ { * }$ subject to any given platform policy $\hat { \bar { \boldsymbol { \beta } } } .$ .

In stage $^ { 3 , }$ partially informed consumers observe $p _ { 1 a }$ and form rational expectation $\hat { p } _ { 2 a } ( p _ { 1 b } , p _ { 2 b } ) ;$ thus, the marginal partially informed consumer is located at $\theta _ { P } = \bar { 1 } / 2 + \bar { ( } p _ { 2 b } + \hat { \hat { p } } _ { 2 a } ( p _ { 1 b } , p _ { 2 b } ) - p _ { 1 b } - p _ { 1 a } ) / ( 2 t )$ . The locations of marginal consumers of the other three types (fully informed, uninformed, and app-only) are as in the main model. Therefore, the total number of in-app consumers and app-only consumers that go to firm j are, respectively,

$$
\begin{array}{l} \# I n A p p _ {j} \\ = \alpha \bigg [ (1 - \beta_ {2}) \bigg (\frac {1}{2} + \eta (j) \frac {p _ {2 b} + p _ {2 a} - p _ {1 b} - p _ {1 a}}{2 t} \bigg) \\ \quad + \beta_ {1} \bigg (\frac {1}{2} + \eta (j) \frac {p _ {2 b} + \hat {p} _ {2 a} (p _ {1 b} , p _ {2 b}) - p _ {1 b} - \hat {p} _ {1 a} (p _ {1 b} , p _ {2 b})}{2 t} \bigg) \\ \quad + (\beta_ {2} - \beta_ {1}) \bigg (\frac {1}{2} + \eta (j) \frac {p _ {2 b} + \hat {p} _ {2 a} (p _ {1 b} , p _ {2 b}) - p _ {1 b} - p _ {1 a}}{2 t} \bigg) \bigg ], \\ \# A p p O n l y _ {j} = (1 - \alpha) \bigg (\frac {1}{2} + \eta (j) \frac {p _ {2 b} - p _ {1 b}}{2 t} \bigg), \end{array}
$$

Figure 3. (Color online) Timeline of the Alternative Model in Which Developers Can Shroud In-App Purchase Prices  
![](/api/attachments/75XS85J9/fulltext/images/289770c64f3473ddf1ec09eeba82a0fd366bedca0d62432072e31b49ae95af91.jpg)

where $\eta ( j ) = 1 \operatorname { i f } j = 1$ , and $\eta ( j ) = - 1 \mathrm { i f } j = 2$ . Demands for each firm’s app $D _ { j b }$ and in-app purchases $D _ { j a }$ are then $D _ { j b } = \# A p p O n l y _ { j } + \# I n A p p _ { j }$ and $D _ { j a } = \# I n A p p _ { j } .$ Firm profits are $\pi _ { j } = ( 1 - \gamma ) ( p _ { j b } D _ { j b } + p _ { j a } D _ { j a } )$ , for $j = 1 , 2$ . We solve for rational beliefs over the in-app purchase prices the same way as in the main model.

Proposition 6. Given app prices $( p _ { 1 b } , p _ { 2 b } ) _ { \cdot }$ , the unique rational expectations of in-app purchase prices, $( \hat { p } _ { 1 a } , \hat { p } _ { 2 a } )$ are the following:

$\begin{array} { r } { \mathrm { i . \ } \big ( \hat { p } _ { 1 a } ^ { ' } , \hat { p } _ { 2 a } ^ { } \big ) = \big ( \frac { ( 3 - \beta _ { 2 } ) t } { 3 - 2 ( \beta _ { 1 } + \beta _ { 2 } ) + \beta _ { 1 } \beta _ { 2 } } - p _ { 1 b } , \frac { ( 3 - \beta _ { 1 } ) t } { 3 - 2 ( \beta _ { 1 } + \beta _ { 2 } ) + \beta _ { 1 } \beta _ { 2 } } - p _ { 2 b } \big ) } \end{array}$ $\begin{array} { r } { i f p _ { 1 b } > \frac { ( 3 - \beta _ { 2 } ) t } { 3 - 2 ( \beta _ { 1 } + \beta _ { 2 } ) + \beta _ { 1 } \beta _ { 2 } } - v _ { a } } \end{array}$ and $\begin{array} { r } { p _ { 2 b } > \frac { ( 3 - \beta _ { 1 } ) t } { 3 - 2 ( \beta _ { 1 } + \beta _ { 2 } ) + \beta _ { 1 } \beta _ { 2 } } - v _ { a } . } \end{array}$ ii. $\begin{array} { r } { \big ( \hat { p } _ { j a } , \hat { p } _ { - j a } \big ) = \big ( \frac { t + p _ { - j b } + v _ { a } } { 2 - \beta _ { j } } - p _ { j b } , v _ { a } \big ) \ i f { p _ { - j b } } \leq \frac { ( 3 - \beta _ { j } ) t } { 3 - 2 ( \beta _ { j } + \beta _ { - j } ) + \beta _ { j } \beta _ { - j } } - } \end{array}$ $v _ { a }$ and $p _ { j b } > \frac { t + p _ { - j b } - ( 1 - \dot { \beta _ { j } } ) \dot { v } _ { a } } { 2 - \beta _ { j } } .$ , where $j { \in } \{ 1 , 2 \} , - j { \in } \{ 1 , 2 \} , j { \neq } - j .$ iii. $( \hat { p } _ { 1 a } , \hat { p } _ { 2 a } ) = ( v _ { a } , v _ { a } )$ if $p _ { 1 b } \leq \frac { t + p _ { 2 b } - ( 1 - \beta _ { 1 } ) v _ { a } } { 2 - \beta _ { 1 } }$ and $p _ { 2 b } \leq$ $\frac { t + p _ { 1 b } - ( 1 - \beta _ { 2 } ) v _ { a } } { 2 - \beta _ { 2 } } .$

Proposition 6 is analogous to Proposition 1—the former degenerates to the latter when $\beta _ { 1 } = \beta _ { 2 }$ A comparison of part (i) of this proposition and part (i) of Proposition 1 reveals that the core insight regarding rational belief in our main model, that consumer expectations of a firm’s in-app purchase price linearly decrease in this firm’s app price when both firms’ app prices are high enough, continues to hold in this section when developers can shroud prices.

We next study firm strategies. Different from the main model, in which the firms only control prices, here each firm controls both its prices and its shrouding level subject to the policy of the platform. Below we temporarily ignore this policy restriction of the platform $( \mathrm { i . e . }$ , we temporarily set $\bar { \boldsymbol { \beta } } = 1 )$ and consider all possible shrouding levels between 0 (no shrouding) and 1 (full shrouding) to gain a complete understanding of the implications of developer shrouding. We will then study the consequence of the platform’s policy restricting shrouding. For ease of exposition, we only consider $\beta _ { 1 } \leq \beta _ { 2 }$ in the following proposition. The case of $\beta _ { 1 } \geq \beta _ { 2 }$ is symmetric because we can simply switch the subscripts 1 and 2.

Proposition 7. Suppose that the platform does not limit firm shrouding. Consider only $\beta _ { 1 } \leq \beta _ { 2 }$ . There are multiple equilibria that can be grouped into three categories based on firm shrouding strategies:

i. Symmetric low-low-shrouding equilibrium. There is a single symmetric equilibrium whereby firms choose shrouding levels $\begin{array} { r } { \beta _ { 1 } ^ { * } = \beta _ { 2 } ^ { * } = \frac { v _ { a } } { t + v _ { a } } , } \end{array}$ set app prices $p _ { 1 b } ^ { * } = p _ { 2 b } ^ { * } =$ t and in-app purchase prices $p _ { 1 a } ^ { * } = p _ { 2 a } ^ { * } = v _ { a , }$ , and earn profits $\pi _ { 1 } ^ { * } = \pi _ { 2 } ^ { * } = \frac { 1 } { 2 } ( 1 - \gamma ) ( t + \alpha v _ { a } )$ . The platform earns profit $\pi _ { P } = \gamma ( t + \alpha v _ { a } )$

ii. Asymmetric low-low-shrouding equilibria. There is a set of asymmetric equilibria that satisfy conditions $\begin{array} { r } { \beta _ { 1 } ^ { * } < \frac { v _ { a } } { t + v _ { a } } < \beta _ { 2 } ^ { * } } \end{array}$ and $\begin{array} { r } { \beta _ { 2 } ^ { * } = \frac { v _ { a } ( 3 - 2 \beta _ { 1 } ^ { * } ) - t \beta _ { 1 } ^ { * } } { ( t + v _ { a } ) ( 2 - \beta _ { 1 } ^ { * } ) } } \end{array}$ . Firms set app prices $p _ { 1 b } ^ { * } = p _ { 2 b } ^ { * } = t$ and set in-app purchase prices $p _ { 1 a } ^ { * } =$ $\begin{array} { r } { \stackrel { \cdot \cdot } { 2 } + \stackrel { \cdot \beta _ { 1 } } { \beta _ { 1 } } < v _ { a } a n d \stackrel { \cdot \cdot } { p _ { 2 a } ^ { * } } = v _ { a } . } \end{array}$ . Firm profits are $\begin{array} { r } { \pi _ { 1 } ^ { * } = \frac { 1 } { 2 } ( 1 - \gamma ) \big [ ( t + } \end{array}$ $\begin{array} { r } { \alpha v _ { a } \dot { ) } + \frac { \alpha ( v _ { a } + t \beta _ { 1 } ) ( v _ { a } - ( t + v _ { a } ) \beta _ { 1 } ) } { ( 2 - \beta _ { 1 } ) ^ { 2 } t } \biggr ] } \end{array}$ and $\pi _ { 2 } ^ { * } = { \textstyle { \frac { 1 } { 2 } } } ( 1 - \gamma ) \big [ ( t + \alpha v _ { a } ) -$ $\frac { \alpha ( t + v _ { a } ) ( v _ { a } - ( t + v _ { a } ) \beta _ { 1 } ) } { ( 2 - \beta _ { 1 } ) t } ]$ . The platform earns profit $\begin{array} { r } { \pi _ { P } = \frac { 1 } { 2 } \gamma \big [ 2 ( t + } \end{array}$ $\begin{array} { r } { \alpha v _ { a } \big ) - \frac { \alpha ( 1 - \beta _ { 1 } ) ( 2 t + v _ { a } ) ( v _ { a } - ( t + v _ { a } ) \beta _ { 1 } ) } { ( 2 - \beta _ { 1 } ) ^ { 2 } t } \big ] } \end{array}$

iii. Asymmetric low-high-shrouding equilibria. There is a set of asymmetric equilibria that satisfy conditions $\beta _ { 1 } ^ { * } = \beta _ { 1 } ^ { A \check { L } H }$ and $\underline { { \beta } } _ { 2 } ^ { A L H } \le \dot { \beta } _ { 2 } ^ { * } \le 1$ , where $\begin{array} { r } { \beta _ { 1 } ^ { A L H } < \frac { v _ { a } } { t + v _ { a } } < } \end{array}$ $\underline { { \beta } } _ { 2 } ^ { A L H }$ . Firms set app prices $\begin{array} { r } { p _ { 1 b } ^ { * } = \frac { ( 6 - \alpha - 3 \beta _ { 1 } ^ { A L H } ) t - 2 \alpha ( 1 - \beta _ { 1 } ^ { A L H } ) v _ { a } } { 2 ( 3 - \alpha ) - ( 3 + \alpha ) \beta _ { 1 } ^ { A L H } } } \end{array}$ and $\begin{array} { r } { p _ { 2 b } ^ { * } = \frac { ( 6 - ( 3 - \alpha ) \beta _ { 1 } ^ { A L H } ) t - 4 \alpha ( 1 - \beta _ { 1 } ^ { A L H } ) v _ { a } } { 2 ( 3 - \alpha ) - ( 3 + \alpha ) \beta _ { 1 } ^ { A L H } } } \end{array}$ and set in-app purchase prices $\begin{array} { r } { p _ { 1 a } ^ { * } = \frac { \beta _ { 1 } ^ { A L H } ( 6 - \alpha - 3 \beta _ { 1 } ^ { A L H } ) \dot { t } + ( 2 - \beta _ { 1 } ^ { A L H } ) ( 3 - \alpha - 2 \alpha \beta _ { 1 } ^ { A L H } ) v _ { a } } { ( 2 - \beta _ { 1 } ^ { A L H } ) ( 2 ( 3 - \alpha ) - ( 3 + \alpha ) \beta _ { 1 } ^ { A L H } ) } < v _ { a } } \end{array}$ and $p _ { 2 a } ^ { * } = v _ { a }$ . Firm 1 profit is $\pi _ { 1 } ^ { * } > \frac { 1 } { 2 } ( 1 - \gamma ) t$

For case (iii), $\beta _ { 1 } ^ { A L H }$ and $\underline { { \beta } } _ { \gamma } ^ { A L H }$ do not have explicit expressions; thus we put their implicit definitions in the online appendix. Furthermore, profit expressions for this case are convoluted; thus we also leave them in the online appendix and only highlight one important attribute $\mathrm { ^ { \small { s } } } ( \mathrm { i } . \mathrm { e } . , \pi _ { 1 } ^ { * } > \frac { 1 } { 2 } ( 1 - \check { \gamma } ) t$ t in this case) in the proposition.

Proposition 7 has several important implications. First, because firms can strategize over their respective shrouding levels in this model extension, they both will never choose high shrouding levels that trigger rational belief as in case (iii) of Proposition 6 (where there is no competition-softening effect on either firm side). To see the intuition, first note that if consumers believe both firms always set the in-app purchase prices at their maximum $v _ { a } ,$ , which happens if both firms choose high enough shrouding levels, the loss of the competition-softening effect results in a profit of $\scriptstyle { \frac { 1 } { 2 } } ( 1 - \gamma ) { \dot { t } }$ for both firms (a result identical to case (ii) of Proposition 2). But now firm 1 will find it profitable to deviate by reducing its shrouding level enough so that case (iii) or (ii) of Proposition 7 starts to apply: in either case (iii) or (ii), firm 1 earns a profit that is higher than ${ \scriptstyle { \frac { 1 } { 2 } } } ( 1 - \gamma ) t .$ . This finding contrasts with case (ii) of Proposition 2: even in the absence of regulation by the platform, the ability to choose shrouding levels by app developers enables the app developers to arrive at shrouding levels that always result in the benefit of competition softening (for at least one firm).

Second, the firms may arrive at a plural of possible equilibria. Among them, there is one unique symmetric equilibrium (case (i) of Proposition $^ { 7 , }$ , where $\begin{array} { r } { \beta _ { 1 } ^ { * } = \beta _ { 2 } ^ { * } = \frac { v _ { a } } { t + v _ { a } } ) } \end{array}$ that achieves the same outcome as the optimal one under our main model (see Proposition 3). We will discuss this symmetric equilibrium further when analyzing the impact of platform policy.

Different from the main model, in which the shrouding level chosen by the platform applies symmetrically to both firms, in this extension, the firms may arrive at asymmetric shrouding levels. In case (ii) of Proposition $^ { 7 , }$ which we call the asymmetric low-lowshrouding equilibria, both firms’ choices of shrouding levels are low enough that uninformed consumers expect a negative correlation between the observed app price and the unobserved in-app purchase price for each firm. In other words, both firms enjoy the benefit of competition softening. Nevertheless, firm 1, by having a shrouding level lower than that of firm $^ { 2 , }$ enjoys more benefit of competition-softening than firm $^ { 2 , }$ as $\pi _ { 1 } ^ { * } > \pi _ { 2 } ^ { * }$ in this case. Intuitively and as compared with firm $^ { 2 , }$ a lower shrouding level by firm 1 results in a lower expected in-app purchase price $( \mathrm { i . e . , ~ } p _ { 1 a } ^ { \ast } < p _ { 2 a } ^ { \ast } )$ and consequently both a higher app demand and in-app-content demand. This demand increment effect dominates the lowered margin on inapp content, thus resulting in a higher profit for firm 1.

The firms may further differentiate their shrouding levels and thus arrive at another possible set of equilibria as in case (iii) of Proposition $^ { 7 , }$ which we call the asymmetric low-high-shrouding equilibria. In this case, firm $2 ^ { \prime } \mathrm { s }$ shrouding level is so high that consumers expect its in-app purchase price to be constant at $v _ { a } ;$ in other words, firm 2 does not enjoy the rationalexpectation-induced competition softening. Firm $^ { 2 , }$ nevertheless, enjoys another competition-softening effect: because the two firms adopt vastly different shrouding strategies, they effectively target different consumer groups. Firm 1, by revealing its (relatively low) in-app purchase prices to most consumers, largely targets in-app consumers. Firm 2, by contrast, largely targets app-only consumers. Each of them faces less competitive pressure within their respective targeted consumer segment; thus overall the competition is softened.

We next discuss the role of the platform under firm shrouding. Specifically, is it in the interest of the platform to limit the shrouding behaviors of the app firms? And what are the consequences to the firms if the platform chooses to do so? We model platform policy as an upper bound $\hat { \beta }$ on the firms’ shrouding levels (i.e., a mandatory minimum level of disclosure of in-app purchase prices). As a profit maximizer, the platform will choose a value of $\hat { \beta }$ to maximize its profit $\begin{array} { r } { \pi _ { P } = \gamma \sum _ { j = 1 } ^ { 2 } \big ( p _ { j a } ^ { * } D _ { j a } + p _ { j b } ^ { * } D _ { j b } \big ) } \end{array}$

We first look at the symmetric and asymmetric lowlow-shrouding equilibria (as in cases (i) and (ii) in Proposition 7), where tractable analytical results exist. By comparing platform profits in these two cases, we immediately have the following.

Corollary 2. The platform’s profit (and the total industry profit) under the symmetric low-low-shrouding equilibrium is always higher than that under any asymmetric low-lowshrouding equilibrium.

Therefore, when both firms adopt low shrouding levels, the industry as a whole benefits if the two firms can coordinate on a same shrouding level. However, without platform regulation, Proposition 7 shows that this coordination is not guaranteed because multiple equilibria exist.

The platform, however, can ensure that the firms for sure coordinate on the symmetric equilibrium by setting the following policy: $\begin{array} { r } { \bar { \boldsymbol { \beta } } = \frac { v _ { a } } { t + v _ { a } } . } \end{array}$ . Because both cases (ii) and (iii) of Proposition 7 involve at least one firm choosing a shrouding level higher than $\frac { v _ { a } } { t + v _ { a } } ,$ , such a policy will result in the symmetric equilibrium being the unique equilibrium.

Whether the platform will choose this policy also depends on its profit under asymmetric low-highshrouding equilibria (case (iii) in Proposition 7). Because this case does not have explicit solutions of profits, we next numerically compare this case with the symmetric low-low-shrouding equilibria. For ease of discussion, we denote platform profit under asymmetric low-high-shrouding equilibria as $\pi _ { P } ^ { A L H }$ and platform profit under symmetric low-low-shrouding equilibria as $\pi _ { P } ^ { S L I }$ . At the end of the proof of Proposition 7 in the online appendix, we show that the rank order between $\pi _ { P } ^ { S L L }$ and $\pi _ { P } ^ { A L H }$ is determined only by two factors: the size of in-app consumers α and the ratio between in-app content reservation value and the unit fit cost $\begin{array} { r } { \frac { { v _ { a } } } { t } . } \end{array}$ . Therefore, we numerically compare $\pi _ { P } ^ { S L L }$ and $\pi _ { P } ^ { A L H }$ for the full range of values of α and $\begin{array} { r } { \frac { v _ { a } } { t } , } \end{array}$ as shown in Figure 4.<sup>20</sup>

The shaded area in Figure 4 shows that when the size of in-app consumers α is small and the reservation value of in-app content $v _ { a }$ is large relative to the unit fit cost $t ,$ the platform is better off under the symmetric low-low-shrouding equilibrium than under any of the asymmetric low-high-shrouding equilibria. To see the intuition, recall that under the asymmetric low-high-shrouding equilibria, the two firms soften competition by targeting different consumer segments: firm 1 targets in-app consumers by offering a lower in-app purchase price, whereas firm 2 targets apponly consumers. This differentiated targeting, however, is less attractive to firm 1—and thus less effective in softening competition—when α is small (thus there are few in-app consumers to target) or when $v _ { a }$ is large (thus offering a low in-app purchase price is costly). Consequently, when α is small enough and $v _ { a }$ is large enough, competition softening by targeting different consumer segments is no longer as effective as competition softening by inducing rational beliefs that both firms’ in-app purchase prices are decreasing in their respective app prices.

Figure 4. Comparison of $\pi _ { P } ^ { S L L }$ and $\pi _ { P } ^ { A L H }$  
![](/api/attachments/75XS85J9/fulltext/images/06a4c7d64370e788723e9ddbff6b5b63aa6eff337cc6c5104df35c61f05e8a2f.jpg)  
Note. White area: $\pi _ { P } ^ { S L L } < \pi _ { P } ^ { A L H } ,$ ; shaded area: $\pi _ { P } ^ { S L L } > \pi _ { P } ^ { A L H } .$

Combining the above numerical finding with Corollary 2, we can conclude that when α is small and $\frac { v _ { a } } { t }$ is large (as in the shaded area in Figure $^ { 4 ) , }$ , it is optimal for the platform to impose a policy of $\begin{array} { r } { \bar { \beta } = \frac { v _ { a } } { t + v _ { a } } } \end{array}$ to rule out all asymmetric equilibria. In this case, such a policy benefits the overall industry profit. When either α is large or $\frac { v _ { a } } { t }$ is small (as in the white area in Figure 4), however, imposing such a platform policy is not optimal.

To summarize, this extension with firm shrouding demonstrates that the core insights of the main model are robust. First, the core competition-softening insight regarding rational belief—that consumer expectation of a firm’s in-app purchase price linearly decreases in this firm’s app price when both firms’ app prices are high enough—holds regardless of whether the platform or the app developers determines shrouding levels. Second, policy intervention by the platform can play a role in ensuring optimal industry profit in both the main model and this extension.

This alternative model also reveals several new insights. First, the platform’s policy intervention affects industry profit through different mechanisms. In the main model, the platform directly dictates the shrouding levels. In the extension, however, policy by the platform serves an equilibrium refinement role: the platform policy only prevents the firms from coordinating on any equilibrium in which at least one firm engages in aggressive shrouding. The policy, however, does not limit how mild firm shrouding can be; instead, the platform depends on the firms to self-select the only symmetric equilibrium in which the shrouding levels are large enough for optimal industry profit.

Second, whereas under platform shrouding, both firms always face a symmetric shrouding level, under firm shrouding, the firms can differentiate from each other by adopting different shrouding levels. As we have shown through the numerical analysis, when this differentiation is strong enough, it is possible for the overall industry profit to be higher than that under symmetric shrouding. In this case, policy intervention by the platform is not optimal.

The disclosure policy discussed in this section takes the form of a mandatory upper bound $\hat { \beta }$ on any app firm’s shrouding level $( \mathrm { i . e . , } \beta _ { i } \le \bar { \beta } , \mathrm { f o r } j = 1 , 2 )$ ). We next comment on two alternative disclosure policies by the platform.<sup>21</sup> The first alternative is the case in which the platform sets a lower bound $\underline { { \beta } }$ on shrouding levels $( \mathrm { i } . \mathrm { e } . , \beta _ { j } \ge \underline { { { \beta } } } ,$ for $j = 1 , 2 )$ . In this case, the platform can still ensure that the firms coordinate on the symmetric equilibrium by setting $\begin{array} { r } { \underline { { \beta } } = \frac { v _ { a } } { t + v _ { a } } } \end{array}$ . This is because, under either of the asymmetric equilibria in Proposition $^ { 7 , }$ firm $1 ^ { \prime } \mathrm { s }$ shrouding level is below $\frac { v _ { a } } { t + v _ { a } }$ and thus infeasible under the platform’s lower-bound policy $\beta .$ Consequently, the preceding discussion on when the platform should impose policy intervention under an upper bound policy still applies under a lower bound policy.

The second alternative is the case in which the platform sets an incremental shrouding amount $\Delta$ on top of the shrouding choices of the firms so that consumers eventually face shrouding levels $\beta _ { j } + \Delta _ { \cdot }$ , for $j = 1 , 2$ . This policy is equivalent to the lower bound pol icy just discussed: by setting $\Delta ,$ the platform effectively rules out any shrouding level below $\Delta ;$ thus $\Delta$ becomes the lower bound of each firm’s shrouding level

## 6. Conclusion

Mobile app platforms have made decisions on how much scrolling is necessary to observe in-app purchase prices. This research provides insights for both platforms and the app developers who are on them. Common intuition would suggest that platforms that earn commission on revenue from both apps and inapp content would benefit from extreme shrouding because competing app developers can exploit their customers with monopoly pricing on the in-app content. However, our research shows that established app platforms such as the Apple $\operatorname { A p p }$ Store and Google Play and emerging app platforms such as Slack and Alexa should choose a shrouding level that results in at least some consumers observing the inapp purchase price. This paper uniquely finds a nonmonotonic relationship between shrouding of inapp purchase prices and profitability. As a consequence, platforms should also avoid making in-app purchase prices completely transparent such that all consumers observe the prices. The optimal decision is a moderate degree of shrouding in which some con sumers become informed of in-app purchase prices, yet some consumers choose not to read (or listen) through all the way to the prices.

App developers also must decide on the platforms, and our research shows that the platform’s shrouding level should influence this decision. Whereas pre vious research either shows that the shrouding will not affect equilibrium industry profits or remains silent on intermediate degrees of shrouding, the current research shows that app developers earn their greatest profit on platforms that have a moderate degree of shrouding. Prior theory would suggest platform shrouding should have no influence on the app developer’s profit if there is competition, or under certain conditions, the app developers should prefer a platform that shrouds over one that does not. However, the current research informs the decision not only at the extremes of shrouding but also suggests that an intermediate degree of shrouding will result in maximum app developer profit.

This paper contributes to theory by uncovering a new mechanism governing the relationship between unadvertised prices and profitability. A common finding in the literature is that any gains from shrouded in-app prices are competed away on app prices. To overturn this profit-irrelevancy result, previous literature has assumed either consumer sensitivity to interfirm price differences is significantly correlated with the addon usage or asymmetry in quality of the both the base good and the add-on. Our research uniquely finds neither of these assumptions is necessary for a profitimprovement effect of price shrouding. This result holds when the platform chooses the shrouding level and when the decision is made by app developers. Key to this finding is the consideration of in-app purchase by both consumers who are informed about the in-app purchase prices before app purchase and consumes who are uninformed of the in-app purchase prices until after app purchase. When the platform’s disclosure policy results in a sufficient number of informed consumers, the uninformed consumers will rationally expect the in-app purchase prices to be negatively correlated with the app price. This belief system implies that uninformed consumers can be less price sensitive over app prices than informed consumers. Two dynamics then follow. With respect to app prices, price cuts turn out to be ineffective in attracting uninformed consumers (because they expect a corresponding increase in the in-app purchase prices), which dampens the price competition over app prices. Second and with respect to in-app purchase prices, firms can still take advantage of the unobservability of the in-app purchase prices by uninformed consumers and charge high in-app purchase prices. In other words, firms avoid the perils of loss-leader pricing while still reaping the benefit of high margins on in-app purchases.

One may intuit that the presence of informed consumers would help to drive down in-app purchase prices and benefit the uninformed consumers. However, the model shows how the presence of informed consumers can deteriorate uninformed consumer surplus and total consumer surplus. When the presence of informed consumers suppresses the app developers’ incentive to charge monopoly in-app purchase prices, it also creates rational expectations that a lower app price implies higher in-app purchase prices. In other words, uninformed consumers rationally expect that an attempt to lure them with a lower app price will generally be followed by an attempt to harvest their value with a higher in-app purchase price. This is the unique rational belief system in our model, and it consequently diminishes firm incentive to cut app prices. One implication we highlight is that the coexistence of informed and uninformed consumer segments can be detrimental to each segment’s surplus compared with surplus when only one of the two segments exists. Another consequence we find is that the platform’s optimal shrouding is incomplete. In other words, the platform optimally chooses a disclosure policy that results in a subset of consumers becoming informed about in-app purchase prices.

We briefly comment on two limitations of this research. First, our findings regarding consumer welfare abstracts from any costs consumers incur to become informed. The app-only consumer welfare result is robust to this assumption, but the in-app consumer welfare and combined consumer welfare can be overturned if consumer utility is sufficiently diminished by scrolling to find in-app prices. Second, we consider rational consumers in this research, which is consistent with the bulk of analytical work in IS, marketing, and economics. It would be interesting to extend this work to the study of a mix of rationa consumers and boundedly rational consumers who form inaccurate expectations of in-app content prices or consumption at the time of app purchase.

In summary, the consideration of heterogeneity in consumers’ willingness to scroll to find in-app purchase price information in a rational model produces novel results that reverse established intuition and offers a novel explanation of the profitability of in-app purchases. For managers, the research finds that shrouded in-app purchase prices may improve profit under conditions for which prior theory would suggest a profit-irrelevance result. The research also suggests that having some consumers informed about the inapp purchase prices can actually increase profit relative to serving a market with a relatively high number of consumers who do not know the in-app purchase prices at the time of firm choice. For policymakers and consumer advocates, increasing transparency will not always improve consumer welfare. Efforts to increase awareness of in-app purchase prices wil be detrimental to consumers unless there is already a substantial portion of the population aware of the prices.

## Acknowledgments

The authors thank Alessandro Acquisti, the associate editor, and three anonymous reviewers for valuable, clear, and constructive feedback. The authors contributed equally to this manuscript.

## Endnotes

<sup>1</sup> See https://www.theguardian.com/technology/2013/feb/26/apple -settlement-children-in-app-purchases.

<sup>2</sup> Prices checked at the Apple App Store and Google Play on October 6, 2017.

<sup>3</sup> As a senior manager of Rovio, developer of the Angry Birds app, puts it, “the app economy is the most competitive marketplace that’s ever existed.” As such, we consider competing developers in this research (http://www.gamesindustry.biz/articles/2015-04-16-apps -are-the-most-competitive-market-ever-rovio-exec).

<sup>4</sup> See http://www.businessofapps.com/app-revenue-statistics/.

<sup>5</sup> See https://www.statista.com/statistics/276623/number-of-apps -available-in-leading-app-stores/.

<sup>6</sup> Uninformed consumers do not observe in-app purchase prices and may not even observe that they exist. However, rationality requires they form rational expectations. In contrast, informed consumers observe in-app purchase prices.

<sup>7</sup> See https://www.gov.uk/government/uploads/system/uploads/ attachment\_data/file/288360/oft1519.pdf .

<sup>8</sup> See http://www.digitalspy.com/tech/apps/news/a554503/apple -google-to-discuss-in-app-purchase-transparency-with-europe/.

<sup>9</sup> See http://venturebeat.com/2014/02/26/only-0-15-of-mobile-gamers -account-for-50-percent-of-all-in-game-revenue-exclusive/.

<sup>10</sup> By discrete, we mean that one consumer segment gets zero additional utility from using in-app content and the other segment gets a constant utility from in-app content. The Individual Rationality (IR) and Incentive Compatibility (IC) constraints are thus satisfied, with app-only consumers choosing not to buy the in-app content and in-app consumers choosing to buy the in-app content. In reality, consumer utility from in-app content may be continuous. Such an assumption would make the analysis of IR and IC constraints more complex but would still result in both in-app and app-only consumers. In the interesting of parsimony, we abstract from this complexity.

<sup>11</sup> We acknowledge that consumers may also become informed via other means. Our findings merely rely on the fact that a platform’s disclosure decision affects the number of informed consumers.

<sup>12</sup> Let v<sub>a</sub> denote the combined value of in-app purchase content. Suppose that the content needs to be purchased n times, at a price ${ \bar { p } } _ { a } ,$ to realize this value. Provided that $\bar { v } _ { a } / n > \bar { p } _ { a } ,$ a consumer will rationally anticipate getting value v but will form expectations about np¯ . For equivalence to our model, redefine $p _ { a } \triangleq n \bar { p } _ { \ell }$ . If n is not observable, we can redefine $p _ { a } \triangleq E ( n ) \bar { p } _ { a }$ .

<sup>13</sup> This assumption does not affect the generality of the lemma: if $\omega _ { j } > \omega _ { - j } ,$ simply switch notations j and <sup>−</sup>j. The same is true about the assumption subsequently in Proposition 1.

<sup>14</sup> We use the Pareto-dominance refinement for equilibrium selection when multiple equilibria arise.

<sup>15</sup> Kyle (1985) also limits the belief structure to linear functions when such a belief structure can constitute equilibria.

<sup>16</sup> See https://help.apple.com/itunes-connect/developer/#/devae49fb316.

<sup>17</sup> See, for example, http://voices.washingtonpost.com/posttech/2011/ 02/kids\_iphone\_game\_maker\_changes.html.

<sup>18</sup> We thank the associate editor and two anonymous reviewers for suggesting this analysis.

<sup>19</sup> If this assumption does not hold, we can simply switch subscripts 1 and 2.

<sup>20</sup> Note that $0 < \alpha < 1$ and $0 < v _ { a } / t < 2$ . We evenly took 100 samples of α within (0, 1) and 200 samples of $v _ { a } / t$ within (0, 2), thus, in total, 20,000 samples of $( \alpha , v _ { a } / t )$ pairs. We then numerically solve and compare $\pi _ { P } ^ { S L L } / ( \gamma t )$ and $\pi _ { P } ^ { A L H } / ( \gamma t )$ at every sample point.

<sup>21</sup> We thank an anonymous reviewer for suggesting that we include these alternative policies.

## References

Acquisti A, Varian H (2005) Conditioning prices on purchase history Marketing Sci. 24(3):367–381.

Bhargava HK, Choudhary V (2008) Research note: When is versioning optimal for information goods? Management Sci. 54(5):1029–1035.

Brown J, Hossain T, Morgan J (2010) Shrouded attributes and information suppression: Evidence from the field. Quart. J. Econom. 125(2):859–876.

Brynjolfsson E, Dick A, Smith M (2004). Search and product dif ferentiation at an internet shopbot. Working Paper 194, Massachusetts Insitute of Technology, Cambridge.

Chao Y, Derdenger T (2013) Mixed bundling in two-sided markets in the presence of installed base effects. Management Sci. 59(8):1904–1926.

Cheng HK, Li S, Liu Y (2014) Optimal software free trial strategy: Limited version, time-locked, or hybrid? Production Oper. Man agement 24(3):504–517.

Chetty R, Looney A, Kroft K (2009) Salience and taxation: Theory and evidence. Amer. Econom. Rev. 99(4):1145–1177.

Choudhary V (2009) Use of pricing schemes for differentiating in formation goods. Inform. Systems Res. 21(1):78–92.

Derdenger T, Liu X, Sun B (2012) An empirical analysis of consumer purchase behavior of base products and add-ons. Working paper, Carnegie Mellon University, Pittsburgh

Dewan R, Jing B, Seidmann A (2003) Product customization and price competition on the internet. Management Sci. 49(8):1055–1070.

Dou Y, Hu Y, Wu D (2017) Selling or leasing? Pricing information goods with depreciation of consumer valuation. Inform. System Res. 28(3):585–602.

Ellison G (2005) A model of add-on pricing. Quart. J. Econom. 120(2): 585–637.

Ellison G, Ellison S (2009) Search, obfuscation, and price elasticities on the internet. Econometrica 77(2):427–452

Fishbein M, Ajzen I (1975) Belief, Attitude, Intention, and Behavior: An Introduction toTheoryandResearch(Addison-Wesley,Reading,MA).

Gabaix X, Laibson D (2006) Shrouded attributes, consumer myopia, and information suppression in competitive markets. Quart. J. Econom. 121(2):505–540

Ghosh B, Balachander S (2007) Competitive bundling and counter bundling with generalist and specialist firms. Management Sci. 53(1):159–168.

Gupta A, Stahl D, Whinston AB (1997) A stochastic equilibrium model of internet pricing. J. Econom. Dynamics Control 21(4–5):697–722.

Kyle AS (1985) Continuous auctions and insider trading. Econometrica 53(6):1315–1336.

Lal R, Matutes C (1994) Retail pricing and advertising strategies J. Bus. 67(3):345–370

Nalebuff B (2004) Bundling as an entry barrier. Quart. J. Econom 119(1):159–187.

Niculescu MF, Wu DJ (2014) Economics of free under perpetual licensing: Implications for the software industry. Inform. Systems Res, 25(1):173–199.

Rayner K (1998) Eye movements in reading and information processing: 20 years of research. Psych. Bull. 124(3):372–422.

Shulman J, Geng X (2013) Add-on pricing by asymmetric firms. Management Sci. 59(4):899–917.

Simon H (1955) A behavioral model of rational choice. Quart. J. Econom. 69(1):99–118.

Sullivan B (2007) Gotcha Capitalism: How Hidden Fees Rip You Off Every Day, and What You Can Do About It (Ballantine Books, New York).

Sundararajan A (2004) Nonlinear pricing of information goods. Management Sci. 50(12):1660–1673.

Van der Lans R, Pieters R, Wedel M (2008) Eye-movement analysis of search effectiveness. J. Amer. Statist. Assoc. 103(482):452–461.

Verboven F (1999) Product line rivalry and market segmentation— with an application to automobile optional engine pricing. J. Indust. Econom. 47(4):399–425.

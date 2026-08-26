---
otero_id: 2102
otero_key: "D89DZDSY"
title: "Bargaining over Data: When Does Making the Buyer More Informed Help?"
authors: "Jyotishka Ray; Syam Menon; Vijay Mookerjee"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0872"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [128.230.234.162] On: 25 January 2020, At: 06:36 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/D89DZDSY/fulltext/images/e048b8cee97a7deb620ce250b280335fc1920c85c4e3d6191c1b02a3e40784ab.jpg)

## Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Bargaining over Data: When Does Making the Buyer More Informed Help?

Jyotishka Ray, Syam Menon, Vijay Mookerjee

To cite this article: Jyotishka Ray, Syam Menon, Vijay Mookerjee (2020) Bargaining over Data: When Does Making the Buyer More Informed Help?. Information Systems Research

Published online in Articles in Advance 23 Jan 2020

https://doi.org/10.1287/isre.2019.0872

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Bargaining over Data: When Does Making the Buyer More Informed Help?

Jyotishka Ray,<sup>a</sup> Syam Menon,<sup>b</sup> Vijay Mookerjee<sup>b</sup>

<sup>a</sup> Department of Management, College of Business and Economics, California State University–East Bay, Hayward, California 94542; <sup>b</sup> Department of Information Systems, Naveen Jindal School of Management, The University of Texas at Dallas, Richardson, Texas 75083 Contact: jyotishka.ray@csueastbay.edu, http://orcid.org/0000-0001-5060-7650 (JR); syam@utdallas.edu, http://orcid.org/0000-0003-1028-0862 (SM); vijaym@utdallas.edu (VM)

Received: August 26, 2016<sub>Revised:</sub> Sep Accepted: Published Online in Articles in Advance: January 23, 2020

https://doi.org/10.1287/isre.2019.0872

Copyright:

Abstract. The explosive growth of eBusiness has allowed many companies to accumulate a repertoire of unique data sets that can provide substantial value to other firms. These data sets are a growing source of revenue for their owners—one that can generate millions of dollars each year. Given its proprietary nature, the value of the data to a potential buyer is often uncertain to both parties. Therefore, a mutually acceptable price is usually arrived at through a process of negotiation. A seller can choose to provide a demonstration (demo; presentation) to mitigate this uncertainty and/or reduce bias. We adapt a generalization of Nash bargaining to identify when such demonstrations are appropriate and when they are not. We find that a moderately high-valued outside option can help the seller gain from a demonstration even when the buyer is not underestimating the value of the data. Demonstrations can also be useful when the buyer is biased and underestimates data set value When both an outside option and underestimation exist, the provision of a demo that corrects for bias can make otherwise unsuccessful negotiations succeed; it also has the potential to trigger the provision of uncertainty-reducing information in the demo. In the presence of a demo cost, the seller can provide a partially informative demo; demos can also mitigate the effects of cannibalization up to a point.

History: Saby Mitra, Senior Editor; Marius Niculescu, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2019.0872.

Keywords: Nash bargaining • data monetization • demonstrations • outside option

## 1. Introduction

We live in a world where data are being collected at every imaginable opportunity. IBM estimates that 2.5 quintillion bytes of data were created every day in 2015.<sup>1</sup> Firms are becoming increasingly aware that the proprietary data that they hold can be of significant value to other firms in making important business decisions. Hence, the natural question arises. How much is a specific data set worth? This turns out to be a difficult question to answer, because neither data owners nor potential buyers are usually aware of the full potential of the data in question. According to the Wall Street Journal, “data isn’t a physical asset like a factory or cash, and there aren’t any official guidelines for assessing its value” (Monga 2014). Thus, an answer to the above question could go a long way in providing data owners with a solid basis for negotiating a good price for data.

Our work is motivated by a problem faced by a global distribution system (GDS). A GDS forms the backbone information system for travel agencies and enables them to manage reservations and purchases of airline tickets, hotel rooms, rental cars, and other tourist services. As a result, they collect substantial volumes of data on customer shopping activity. Three companies dominate this somewhat disjoint marketplace; as of the second quarter of 2018, Amadeus controlled approximately 44% of the worldwide market, Sabre had about 37%, and Travelport accounted for most of the rest.<sup>2</sup> Although there is some overlap in the geographical regions in which they operate, they tend to focus on specific regions, with Amadeus focused primarily on Europe, Sabre focused primarily on North America and Asia, and Travelport focused primarily on the United States. Consequently, the data sets owned by each GDS are distinct from each other and unavailable anywhere else. These data can provide airlines and hotel chains with considerable insights—an understanding of how well they are converting travel demand into bookings for instance—and enable them to make better decisions on new promotions, routes, schedules, and room capacity. Doshi (2015) estimates that “in the next three to fiv years, the first movers among airlines in data-driven personalization will quickly become the differentiated market leaders.” GDSs provide access to their data to interested parties (an airline for example) for a price—a price that is usually arrived at through a process of negotiation. This negotiation (or bargaining) process— through which one firm sells proprietary data to another—is the focus of this study.

This is but one example of proprietary data being sold in a business-to-business (B2B) context. There is a growing list of companies that engage in such behavior— for example, credit card companies sell consumer purchase data to advertisers who can target consumers with advertisements (Edwards 2013), Facebook sells data to advertisers (Moran 2015), and banks sell consumer data (Jones 2013), whereas Yodlee, a provider of online personal finance tools to many large banks, sells data from credit and debit card transactions to investors and research firms who mine them for clues on trends that can affect stock prices (Hope 2015). Monga (2014) reports that Kroger, a well-known supermarket operator, collects information on customer purchases at more than 2,600 stores while tracking approximately 55 million loyalty card members. These data are of substantial value to consumer goods manufacturers, like Procter & Gamble and Nestlé, because they allow them to tailor their products and marketing to consumer preferences. Kroger’s revenues from the sale of their data are estimated to be in the order of \$100 million a year (Monga 2014). The list is only expanding— there are even companies, like Acxiom and Intelius, that collect large volumes of data with the explicit purpose of selling what they collect (Beckett 2014).

Unfortunately, although data owners know that their clients will be able to leverage the data to gain insights, they are often unclear on the price that they can charge for it. Their knowledge of the client’s business needs is limited, and this limits the extent to which they can estimate the value of the data to the firm buying it. This raises a fundamental question—how should the data owners best monetize their data? There is uncertainty on the buyer’s side as well—although they know their business objectives, they have only limited knowledge about the data (for example, through a data dictionary provided by the seller). Consequently, the buyer does not know exactly how useful the data will be to them, which limits the price that they are willing to pay for it. In this context, the price of the data is often arrived at through a negotiation process between the two parties. This two-sided uncertainty in the valuation of data is, to some extent, similar to that of intangible goods, like intellectual property (for example, patents), and negotiation has been studied in that domain (Lai and Qiu 2003, Walden 2005, Gans et al. 2008, Kishimoto and Muto 2012). We provide a systematic analysis of the negotiation process for monetizing proprietary data products when their true values are unknown.

There is evidence that providing additional information in the form of demonstrations (demos) and samples in advance can reduce valuation uncertainty and increase a buyer’s willingness to pay, although it puts the seller at an information disadvantage (Shapiro 1983, Lewis and Sappington 1994, Niculescu and Wu 2014). Therefore, the decision of whether a demonstration should be provided is an important one, and this paper provides insights into situations where a seller should (and should not) propose a demonstration to the buyer after the negotiation process. The exact nature of a demonstration can vary from providing a subset of the data for the buyer to experience to presentations that showcase the value of the data through dashboards that illustrate its benefits. Davie (2015) notes that “the most common approach for companies who have embarked on data monetization is to develop a dashboard or application for the data.” The primary purpose of providing a demonstration is to allow buyers to revise their beliefs about the value of the data. Unlike in other contexts, where giving part of the product for free negatively impacts revenue from the full product, providing a sample data set (or any other form of demonstration) can be costless to the seller—useful information comes from the analysis of data, and the results from a sample need not necessarily represent valid inferences from the entire data set. What is revealed, of course, are the types of analyses that can be performed.

In our context, the data sets owned by each GDS are unique and distinct. This makes an outside option for a potential buyer virtually nonexistent. A GDS, however, has multiple airlines as potential buyers, and obtaining an estimate for an outside option is usually quite easy. Therefore, we investigate the situation where the seller has an outside option and bargains with the buyer in order to get a higher expected price.

Prior research explores contexts where buyers underestimate value when the true value is unknown (Shapiro 1983, Heiman and Muller 1996, Chellappa and Shivendu 2005, Cheng and Liu 2012, Wei and Nault 2013, Niculescu and Wu 2014, Cheng et al. 2015). In such situations, the seller might want to remove this bias and signal to the buyer that the data are worth more than her underestimated value using a bias-correcting demonstration.

This paper makes several contributions. It systematically analyzes the negotiation process involved in the monetization of proprietary data. We investigate how the seller’s outside option affects the information provision decision in a negotiation setting when both parties have valuation uncertainty. Interestingly, we find that there are circumstances under which the presence of the seller’s outside option can trigger a demonstration with complete information, even though the buyer does not underestimate product value. Another finding is that sellers need to use different demonstration strategies—sometimes to just correct bias and sometimes to correct bias as well as reduce uncertainty. When both forces—underestimation and an outside option for the seller—coexist, we find that not only can a bias-correcting demo can make unsuccessful negotiations successful, but also, it can trigger the seller into providing an uncertainty-reducing demo as well. In the context of underestimation, we find that some prior results obtained in a monopolist context extend into the context being studied in this paper. However, the forces driving these results in our (negotiation) context are fundamentally different. We analyze three different demonstration cost structures that depend on the extent of information that the seller reveals to the buyer through a demonstration and find that there are situations where it is optimal for the seller to provide partially informative demos. Although cannibalization is not an issue in our context, we investigate its impact for the sake of completeness. We find that the seller’s outside option can act as a safeguard against cannibalization if cannibalization levels are not too high. We also find that only the beliefs of the buyer impact the negotiation outcome: that is, it does not matter whether the seller updates her beliefs about the value of the data set.

As mentioned earlier, the context being analyzed in this work is one where the seller and buyer negotiate to arrive at a mutually agreeable price. This makes our model structurally different from models that have been used previously in the context of free trials—which usually consider a firm selling information products in a market with heterogeneous customer preferences. Another structural distinction of the model studied in this paper vis-a-vis existing work is the determination´ of the price itself—although the price of the product is fixed by the seller in prior studies, it is the result of a negotiated agreement in our context. The fact that the context and the framework used are different from those of earlier studies implies that the results from those studies cannot be taken for granted—that is, they need not necessarily remain true under the new regime.

We represent the negotiation between the buyer and the seller as a generalized Nash bargaining process initially proposed by Harsanyi and Selten (1972) to incorporate the information asymmetry. We adopt an incentive-compatible decision mechanism from Myerson (1979, 1984), which maps the players’ information about the value of the data to bargaining outcomes. We find that some results from extant literature (Shapiro 1983, Cheng and Liu 2012, Niculescu and Wu 2014) continue to hold even in a negotiation framework—for example, the existence of uncertainty can trigger an uncertainty-reducing demonstration. It is worth noting that the downside of such a demonstration in our context is that it could strengthen the buyer’s ability to negotiate. An interesting situation arises when both forces (that is, underestimation and an outside option) coexist. The joint interaction of these forces provides new insights into the role of demonstrations for the commercialization of data. To the best of our knowledge, extant research has not considered the impact of an outside option on the need for a demonstration.

The rest of the paper is organized as follows. Section 2 provides a brief review of the literature on uncertainty in product valuation and negotiation. The idea of a demonstration by the seller is introduced in Section 3, whereas the context of underestimation is analyzed in Section 4. The model extensions are in Section 5, where we analyze the impact of a demo cost, and Section 6, where we consider the effect of cannibalization. Section 7 concludes the paper.

## 2. Literature Review

The selling of products and services of uncertain value has been widely studied in both business and economics. These studies differ in how and when the true value is revealed to the buyer. For example, DeGraba (1995) and Shugan and Xie (2000) analyze a situation where the true value is realized well after the product is purchased. Shugan and Xie (2000) find that firms can strategically profit from buyer uncertainty by advance selling to uninformed buyers. Conversely buyers may choose to delay the purchase until they have more information about product value in order to overcome the uncertainty in the valuation of the product (Swinney 2011). Guo and Zhang (2012) note that consumers may need to go through costly deliberations to find out their true valuation in a vertically differentiated product line.

For digital experience and information goods, product sampling is a common way to control buyers valuation uncertainty (Lewis and Sappington 1994). Sellers often provide free trials and samples to help the buyers mitigate uncertainty in product value (Shapiro 1983, Lewis and Sappington 1994, Chellappa and Shivendu 2005, Wang and Zhang 2009, Niculescu and Wu 2014, Cheng et al. 2015). The trial literature varies in two aspects—types of buyers and types of trials. One stream of prior work (Lewis and Sappington 1994, DeGraba 1995, Shugan and Xie 2000) analyzes the problem with no heterogeneity ex ante: that is, there is a mass of consumers with the same expected valuation before they obtain additional in formation. A second stream analyzes the case where consumers are heterogeneous along a single type dimension (Johnson and Myatt 2006, Bhargava and Chen 2012, Niculescu and Wu 2014, Cheng et al. 2015). Lewis and Sappington (1994) show that a seller will not provide any private information through trials when the marginal cost is low. On the contrary, Sobel (1993) and Bhargava and Chen (2012) suggest that the seller will enable potential buyers to become better informed about their product valuations, even when such learning occurs privately to the buyer. This result is obtained when the market is segregated between informed and uninformed buyers, and the seller can benefit by selling a premium-priced product to informed buyers. In our bargaining setup, providing more information to the buyer has serious implications, because the price is mutually decided between a single seller and a single buyer. Therefore, the seller does not have the option to implement a premium pricing policy as was done in prior studies. Chen and Xie (2008) look into whether an online seller should provide consumer reviews to its customers and find that the answer depends on the informativeness of the review and product assortment.

Existing studies have also considered the effects of word of mouth, cannibalization, and underestimation on feature-limited and time-limited trials. Niculescu and Wu (2014) and Cheng and Liu (2012) find that feature-limited trials are appropriate when there exists a strong network effect. Cheng and Tang (2010) investigate the trade-off between network effects and the cannibalization effect because of a free trial version. Cheng and Liu (2012) compared time-locked trials with feature-limited trials and found that time-locked trials are optimal as long as the positive network effect is below a threshold. Because we are investigating a B2B context where there is only a single buyer, network effects—one potential cause of free trials in these papers—are absent in our model.

Researchers have also observed that product trials are triggered when consumers uniformly and sufficiently underestimate a product (Shapiro 1983, Chellappa and Shivendu 2005, Cheng and Liu 2012, Wei and Nault 2013, Niculescu and Wu 2014, Cheng et al. 2015). When buyers underestimate the quality, the seller’s optimal policy is to have a low introductory price followed by a higher price that is maintained forever (Shapiro 1983). Conversely, the results from prior research suggest that informing consumers is not optimal when there is no underestimation overall (Johnson and Myatt 2006). Although these reasons do not extend to our context, we also find situations where offering a free demonstration is beneficial even in the absence of underestimation. This result stems not from price discrimination opportunities as in prior work (because the price is jointly decided between the seller and the buyer) but from the relief provided by an outside option available to the seller.

Our paper builds on the stream of literature on consumer learning through trials (Goering 1985, Lewis and Sappington 1994, Dey et al. 2013). According to Goering (1985), the effect of buyers’ learning on future demand for a product depends on both the information acquired by consumers and the number of consumers who acquire information. Cheng and Liu (2012) and Dey et al. (2013) find that buyers gradually learn the value of the product throughout the free trial and that it is optimal when the rate of learning is sufficiently large. Wei and Nault (2013) consider experience-based learning and find that, if consumers have heterogeneous expectations of quality before experience and are pessimistic, then all consumers who purchased the low-quality version in the first stage upgrade to the high-quality version in the second stage. Prior literature on trials and learning shows that a seller will either choose not to provide any private information or provide perfect information to all potential buyers (Lewis and Sappington 1994, Johnson and Myatt 2006). In the presence of a moderately high outside option, we also find that that the seller can benefit from taking the risk of providing a complete information demo.

Researchers have also conducted field experiments and simulations on free samples. Jain et al. (1995) used simulation to determine the optimal number of product samples for a new product, whereas Lee and Tan (2013) used an empirical model under Bass-type diffusion to examine the effects of various types of free trial software and ratings on consumer software sampling. Bawa and Shoemaker (2004) used evidence from two field experiments to find the effect of repeat purchases, cannibalization, and market expansion on sales. In all of these models, price is treated as exogenous. Other researchers consider sampling under endogenous pricing, where the price of the product is fixed by a monopolist who can use basic and premium pricing to its advantage (Chellappa and Shivendu 2005, Cheng and Liu 2012, Dey et al. 2013, Wei and Nault 2013). Our model is distinct in that the price is mutually determined through a bargaining process between the seller and buyer.

Nash (1950) provided the first formal investigation into bargaining when he looked at cooperative bargaining between two players with complete information. He developed a static one-shot bargaining game and showed that the equilibrium solution is that unique element from a set of alternatives that maximizes the product of utility payoffs to the players. This work precipitated a large volume of research on the bargaining process. Two among these deserve special mention— Harsanyi and Selten (1972) generalized the bargaining process for incomplete information where the types of the players are assumed to be private information, whereas Myerson (1979) extended it further by introducing a decision mechanism, whereby the players did not have to reveal their true types but could agree on a mixed equilibrium over all of the alternatives.

Problems involving incomplete information between a buyer and a seller have been extensively studied from the perspective of a bargaining process. Bilateral negotiation within a mechanism design framework can be broadly categorized into bargaining with one-sided incomplete information and bargaining with two-sided incomplete information. In the one-sided case, bargaining happens between a seller with a known valuation and a buyer with a private valuation (Rubinstein 1982, Fudenberg and Tirole 1983, Gul et al. 1986, Ausubel and Deneckere 1989). This can further be divided into the “gap” case, where the seller’s valuation is less than the support of buyer valuations, and the “no gap” case, where there is an overlap between the seller’s valuation and the support of the buyer’s valuations. In the two-sided context, each player knows his or her own valuation but not that of the other (Chatterjee and Samuelson 1983, Myerson and Satterthwaite 1983, Ausubel and Deneckere 1993). Ausubel et al. (2002) provide an excellent review of bargaining with incomplete information. In our context, neither player initially knows the true value of the data product. However, the buyer can update his or her beliefs after receiving a signal through a demonstration. Bargaining involving outside options with complete information is considered by Binmore (1985); we extend it to an asymmetric information setting. We note that we have not explicitly modeled the bargaining power of the players, because it is inherent to the generalized asymmetric bargaining framework (Binmore et al. 1986).

There has also been some research involving controlled field experiments to understand bargaining behavior. Güth et al. (1982) analyze selfishness and rationality in a two-person bargaining situation. A review on stylized bargaining experiments can be found in van Damme et al. (2014). Some web-based e-negotiation support systems have also been used to automate the activities undertaken by negotiators (Kersten and Lai 2007). For example, Invite<sup>3</sup> provides various e-negotiation platforms for research and training purposes. These streams are tangential to our work, because our focus is the outcome of the negotiation rather than the bargaining behavior itself.

## 3. The Role of a Data Demonstration

Consider a seller who has a unique, proprietary data set that is of value to the buyer. The price of the data set is jointly decided by the seller and the buyer through a negotiation process. We consider a seller who has an outside option for her data and expects to gain more from the negotiation with the buyer. Although a thorough analysis of the data to evaluate its full potential may not be possible, a free demo can help the buyer arrive at a better estimate of the value of the data. Bain (1956) showed that free trials can help buyers learn how well a product fits their needs. Heiman and Muller (1996) note that buyers change their estimates of product value after experiencing it. Although demonstrations can help buyers update their priors and make a purchasing decision, sellers will provide one only if it increases their expected payoff.

The exact nature of a demonstration can vary, but the essence does not—fundamentally, a demonstration is something that the seller can provide the buyer to better estimate value. In our context, a demonstration could entail presentations that showcase the value of the data through dashboards that illustrate its benefits, providing a subset of the data for the buyer to experience, giving examples of how other firms in the industry benefited from the use of similar data sets, and so on. The demonstration provides a signal based on which the buyer can update her beliefs about the value of the data. Of course, these points hold for products in general. What makes data unique is the degree to which the seller can control th quality of the demonstration and through it, the extent of learning experienced by the buyer. For example, by appropriately choosing variables and/or records, the seller can determine the exact subset of the data to incorporate in a demonstration. This allows the seller to have a fine control over the extent o information that a buyer can learn from such a demonstration. Although some amount of customization is feasible (and common) in most demonstrations, the flexibility that data allow along this dimension is uncommon in other contexts. That is, data sellers can control the extent of information revealed to buyers to an extent that is difficult to achieve with demonstrations of other goods. This makes learning endog enous, in line with some prior work on learning (Lewis and Sappington 1994, Dey et al. 2013). Although the buyer can update her beliefs about product value based on an uncertainty-reducing demonstration, the seller remains as uncertain as before. The seller will, however, be aware that the buyer has updated her beliefs about the value of the data set. Given the asymmetry in information between the seller and the buyer, the resulting negotiation calls for a bargaining framework under asymmetric information.

Harsanyi and Selten (1972) established the theory of cooperative games with incomplete information by generalizing Nash’s (1950) two-player complete information bargaining game. They modeled a twoplayer incomplete information bargaining problem as a pair $\left( X , p \right)$ , where X, the feasible bargaining set, is the convex hull of the expected payoffs of the players generated by strict equilibria and p is the joint probability matrix of the states of the players. They defined a strict equilibrium as the equilibrium point where each player plays his or her best response strategy against the others, and any deviation by a player to an alternative best response strategy does not affect the payoffs of the other players. They extended the axioms developed by Nash and showed that a unique solution of the two-person incomplete bargaining game exists in the set X, which satisfies all of the axioms. Later, Myerson (1979) proposed an incentive-compatible direct revelation mechanism and showed that it coincides with the approach developed by Harsanyi and Selten (1972). We incorporate the approach of Myerson (1979) to solve our asymmetric information bargaining game.

## 3.1. The Model

We adopt a binary distribution model as proposed in Lewis and Sappington (1994). We use this model to study how negotiation outcomes are affected by uncertainty-reducing demonstrations. Bias-correcting demonstrations are studied in Section 4. The value is either $D _ { L }$ with probability $p _ { L }$ or ${ \cal D } _ { H } \left( 0 < D _ { L } < D _ { H } \right)$ with probability $p _ { H } = ( 1 - p _ { L } ) .$ , with an expected value of $D ,$ all of which is common knowledge. The demonstration provides the buyer with a signal $S _ { t }$ with probability $P ( S _ { t } )$ , where t represents the states of the values L and H. We define α to be a parameter that the seller can manipulate when providing the signal and let $\begin{array} { r } { P ( S _ { L } | L ) = } \end{array}$ $P ( S _ { H } | H ) = \alpha$ (implying that $P ( S _ { H } | \breve { L } ) = P ( S _ { L } | H ) = 1 - \alpha )$ Then, $P ( S _ { H } ) = P ( S _ { H } | H ) P ( H ) + P ( S _ { H } | L ) P ( L ) = \alpha p _ { H } + ( 1 -$ $\alpha ) p _ { L }$ and $P ( S _ { L } ) = ( 1 - \alpha ) p _ { H } + \alpha p _ { L }$ . After the demonstration, the buyer updates her belief about the value as $\begin{array} { r } { P ( H | S _ { H } ) = \frac { P ( S _ { H } | H ) P ( H ) } { P ( S _ { H } ) } = \frac { \alpha p _ { H } } { \alpha p _ { H } + ( 1 - \alpha ) p _ { L } } } \end{array}$ and $\begin{array} { r } { P ( L | S _ { L } ) = \frac { \alpha p _ { L } } { \alpha p _ { L } + ( 1 - \alpha ) p _ { H } } . } \end{array}$ In the absence of a demo, the signal will not exist. That is equivalent to saying that the signal will be uninformative (useless): that is, $P ( H | S _ { H } ) { \bar { = } } P ( H | S _ { L } ) = p _ { H }$ and $P ( L | S _ { L } ) = P ( L | S _ { H } ) = p _ { L }$ . At the other extreme, the signal will be perfect or fully informative: that is, $\bar { P ( H | S _ { H } ) = }$ $1 = P ( L | \bar { S } _ { L } )$ and $P ( H | S _ { L } ) = 0 = P ( L | S _ { H } )$ . We note that an accurate signal is obtained when $\alpha = 1$ and that a useless signal is obtained when $\alpha = 0 . 5$ . The signal will be noisy (but useful) when $0 . 5 < \alpha < 1$ . The seller is interested in providing a signal through a demo that maximizes the expected payoff. Although we consider the demo to be costless in this section, we incorporate an α-dependent demo cost in the extension presented in Section 5.

Let Φ be the set of possible prices that the players can potentially agree on. Each element $d \in \Phi$ is a possible, mutually agreeable price $q ( d )$ in the range $\left[ 0 , D _ { H } \right]$ . The payoff to the buyer in each alternative d is $u _ { B } ( d , t ) = D _ { t } - \bar { q } ( d )$ , where t is either H or L depending on the state of the data. The payoff to the seller, $u _ { S } ( d )$ is $q ( d )$ irrespective of the state. As an agreement is not guaranteed, a disagreement alternative $\bar { d } ^ { * }$ is included in Φ; essentially, it represents the status quo that would prevail if the players fail to arrive at a mutually acceptable price. The disagreement alternative $\bar { d } ^ { * }$ is characterized by an outside option available to the seller before agreeing to a negotiation with the buyer involving a fixed value, $r .$ The buyer will not receive anything in the case of a disagreement, and consequently, the payoffs in alternative $\bar { d } ^ { * }$ are $\boldsymbol { u } _ { S } ( d ^ { * } ) = \boldsymbol { r }$ and $\bar { u _ { B } } ( d ^ { * } , t ) = 0$ . Rather than agreeing on a single alternative, Myerson (1979) proposed that the players collectively agree on a decision rule or mechanism $\mu ( d | S _ { t } )$ <sub>)</sub> defined by

$$
\sum_ {d \in \Phi} \mu (d | S _ {t}) = 1; t \in \{L, H \}\tag{1}
$$

$$
\mu (d | S _ {t}) \geq 0; \forall d \in \Phi , t \in \{L, H \}.\tag{2}
$$

The randomized strategy $\mu ( d | S _ { t } )$ is the probability of selecting alternative d when the signal reported by the buyer is $S _ { t } .$ . In this bargaining game, both players agree on a mechanism $\mu ( d \vert S _ { t } )$ to be implemented when the signal $S _ { t }$ is revealed by the buyer after the demo. That is, the players mutually agree on two sets of probability distributions $\mu ( d | S _ { L } )$ and $\mu ( d \vert S _ { H } )$ over the set of alternatives $\Phi$ . This allows the buyer to agree on mechanism $\mu$ without actually knowing the signal. When the bargaining is complete and mechanism μ is mutually decided, the seller can offer a demo that provides a signal (either $S _ { L }$ or $S _ { H } )$ to the buyer. After observing this signal, the buyer truthfully reveals it. The players then execute the agreed probability distribution $\mu ( d \vert S _ { t } )$ to select an alternative $d \in \Phi$ and receive the corresponding payoffs $( u _ { S } ( d ) , u _ { B } ( d , t ) )$ . Rather than selecting a single price as the decision variable, the mechanism $\mu$ is adopted as a distribution over the set Φ to make it a truth-revealing mechanism. Figure 1 shows the sequence of events when a demo is offered.

Let $U _ { B } ( \mu , S _ { t ^ { \prime } } | S _ { t } )$ be the conditional expected payoff of the buyer when the received signal is $S _ { t } ,$ and the signal reported by the buyer is $S _ { t ^ { \prime } }$ (where $t , t ^ { \prime } \in \{ L , H \} )$

Figure 1. Sequence of Events When a Demo Is Offered  
![](/api/attachments/D89DZDSY/fulltext/images/6f18bbecc5a827b97a68c64fa7477617c0eabbd06b03513fb70010d0521dfcbb.jpg)

when mechanism $\mu$ is implemented. Let $U _ { S } ( \mu )$ be the expected payoff of the seller in mechanism $\mu .$ . These expected payoffs can be calculated as follows:

$$
\begin{array}{l} U _ {B} \big (\mu , S _ {H} | S _ {H} \big) \\ = \sum_ {d \in \Phi \setminus \{d ^ {*} \}} \mu (d | S _ {H}) (u _ {B} (d, H) P (H | S _ {H}) + u _ {B} (d, L) P (L | S _ {H})) \\ = \sum_ {d \in \Phi \setminus \{d ^ {*} \}} \mu (d | S _ {H}) \Bigg ((D _ {H} - u _ {S} (d)) \frac {\alpha p _ {H}}{P (S _ {H})} \\ \qquad + (D _ {L} - u _ {S} (d)) \frac {(1 - \alpha) p _ {L}}{P (S _ {H})} \Bigg) \\ = \sum_ {d \in \Phi \setminus \{d ^ {*} \}} \mu (d | S _ {H}) \Bigg (\frac {\alpha p _ {H} D _ {H} + (1 - \alpha) p _ {L} D _ {L}}{\alpha p _ {H} + (1 - \alpha) p _ {L}} - u _ {S} (d) \Bigg) \end{array}\tag{3}
$$

$$
\begin{array}{l} U _ {B} \big (\mu , S _ {L} | S _ {H} \big) \\ = \sum_ {d \in \Phi \backslash \{d ^ {*} \}} \mu (d | S _ {L}) \left(\frac {\alpha p _ {H} D _ {H} + (1 - \alpha) p _ {L} D _ {L}}{\alpha p _ {H} + (1 - \alpha) p _ {L}} - u _ {S} (d)\right) \end{array}\tag{4}
$$

$$
= \sum_ {d \in \Phi \backslash \{d ^ {*} \}} \mu (d | S _ {H}) \left(\frac {(1 - \alpha) p _ {H} D _ {H} + \alpha p _ {L} D _ {L}}{\alpha p _ {L} + (1 - \alpha) p _ {H}} - u _ {S} (d)\right)\tag{5}
$$

$$
\begin{array}{l} {U _ {B} \big (\mu , S _ {L} | S _ {L} \big)} \\ {= \sum_ {d \in \Phi \setminus \{d ^ {*} \}} \mu (d | S _ {L}) \left(\frac {(1 - \alpha) p _ {H} D _ {H} + \alpha p _ {L} D _ {L}}{\alpha p _ {L} + (1 - \alpha) p _ {H}} - u _ {S} (d)\right)} \end{array}\tag{6}
$$

$$
\begin{array}{l} U _ {S} \big (\mu \big) \\ = U _ {S} \big (\mu , S _ {L} | S _ {L} \big) P (S _ {L}) + U _ {S} \big (\mu , S _ {H} | S _ {H} \big) P (S _ {H}) \\ = \sum_ {d \in \Phi} \mu (d | S _ {L}) (u _ {S} (d) P (L | S _ {L}) + u _ {S} (d) P (H | S _ {L})) P (S _ {L}) \\ \quad + \sum_ {d \in \Phi} \mu (d | S _ {H}) (u _ {S} (d) P (L | S _ {H}) + u _ {S} (d) P (H | S _ {H})) P (S _ {H}) \\ = \sum_ {d \in \Phi} \big (\mu (d | S _ {L}) P (S _ {L}) + \mu (d | S _ {H}) P (S _ {H}) \big) u _ {S} (d). \end{array}\tag{7}
$$

A mechanism is said to be feasible if it satisfies conditions (1) and (2). It also needs to be Bayesian incentive compatible (BIC) and individually rational (IR): that is, $\mu$ must also satisfy

$$
U _ {B} \big (\mu , S _ {L} | S _ {L} \big) \geq U _ {B} \big (\mu , S _ {H} | S _ {L} \big);
$$

$$
U _ {B} \big (\mu , S _ {H} | S _ {H} \big) \geq U _ {B} \big (\mu , S _ {L} | S _ {H} \big)\tag{8}
$$

$$
U _ {B} \big (\mu , S _ {t} | S _ {t} \big) \geq 0; U _ {S} \big (\mu \big) \geq r; t, t ^ {\prime} \in \{L, H \}.\tag{9}
$$

Constraint (8) ensures that the buyer will have no incentive to lie about the realized signal, because there is no positive gain from lying. The IR constraint (9) implies that the buyer expects to get a nonnegative payoff, whereas the seller would expect to make at least r from the negotiation—that is, the presence of an outside option places the restriction $U _ { S } ( \mu ) \geq r$ (Binmore 1985). The set of possible expected payoff pairs $\mathcal { F } = \{ ( U _ { S } ( \mu ) , U _ { B } ( \mu ,$ $S _ { L } | \hat { S } _ { L } ) , U _ { B } ( \mu , S _ { H } \hat { | } S _ { H } ) ) : \hat { \mu }$ is feasible, and satisfies IR and BIC is a finite, compact, and convex set. Let Ψ be the set of feasible mechanisms for the bargaining game.

Myerson (1979) showed that this truth-telling mechanism can be determined through the solution approach of Harsanyi and Selten (1972). Following their method, the solution to this Bayesian bargaining game $( S _ { N } B _ { Y } )$ is the mechanism $\mu \in \dot { \Psi }$ that maximizes the generalized Nash product subject to the constraints discussed earlier:

$$
\begin{array}{r l} & (S _ {N} B _ {Y}) \\ & \max _ {\mu \in \Psi} U _ {S} (\mu) \cdot (U _ {B} (\mu , S _ {L} | S _ {L})) ^ {(1 - P (S _ {H}))} \cdot (U _ {B} (\mu , S _ {H} | S _ {H})) ^ {P (S _ {H})} \\ & \text {s.t.} \quad U _ {B} (\mu , S _ {L} | S _ {L}) \geq U _ {B} (\mu , S _ {H} | S _ {L}); \\ & \qquad U _ {B} (\mu , S _ {H} | S _ {H}) \geq U _ {B} (\mu , S _ {L} | S _ {H}) \\ & \qquad U _ {S} (\mu) \geq r \\ & \qquad U _ {B} (\mu , S _ {L} | S _ {L}) \geq 0; U _ {B} (\mu , S _ {H} | S _ {H}) \geq 0 \\ & \qquad \sum_ {d \in \Phi} \mu (d | S _ {L}) = 1; \sum_ {d \in \Phi} \mu (d | S _ {H}) = 1 \\ & \qquad \mu (d | S _ {L}) \geq 0; \mu (d | S _ {H}) \geq 0 \forall d \in \Phi \\ & u _ {B} (d, t) + u _ {S} (d) = D _ {t}; \forall d \in \Phi \backslash \{d ^ {*} \}; t \in \{L, H \} \\ & u _ {B} (d ^ {*}, t) = 0; u _ {S} (d ^ {*}) = r; \end{array}
$$

maximizing the objective function identifies a unique solution from $\mathcal { F }$ on the Pareto-efficient frontier constructed by the conditional expected payoffs $U _ { S } ( \mu ) ,$ $U _ { B } ( \mu , S _ { L } | S _ { L } )$ , and $U _ { B } ( \mu , S _ { H } | S _ { H } )$ . Theexponents $\left( 1 - P ( S _ { H } ) \right)$ and $P ( S _ { H } )$ loosely signify the influences of the likely signal in the bargaining process. The solution to $( S _ { N } B _ { Y } )$ and the associated proof are provided in Online $\mathrm { A p \mathrm { - } }$ pendix B. Lemma 1 below describes the equilibrium outcome when no demonstration is provided: that is, when $\alpha = 0 . 5$ (the proof is in Online Appendix C).

Lemma 1. When the distribution of the value is common knowledge and the outside option for the seller is $r ,$ the negotiation without a demonstration will result in the following expected payoffs $U _ { S } ^ { * }$ and $U _ { B } ^ { * }$ to the seller and the buyer, respectively, where D is the expected value of the data product

$$
\left(U _ {S} ^ {*}, U _ {B} ^ {*}\right) = \left\{ \begin{array}{l l} \left(\frac {D}{2}, \frac {D}{2}\right), & \text {if} r \leq \frac {D}{2} \\ (r, D - r), & \text {if} \frac {D}{2} \leq r \leq D \\ (r, 0), & \text {if} D \leq r. \end{array} \right.
$$

Lemma 1 implies that, when the value of the outside option is low $\begin{array} { r } { \hat { ( } r < \frac { D } { \gamma } ) } \end{array}$ , the seller expects to gain from the negotiation and will be willing to negotiate. If $r \geq$ ${ \frac { D } { 2 } } ,$ the seller will be indifferent to a negotiation. The buyer’s expected payoffs decrease beyond $\begin{array} { r } { r > \frac { D } { 2 } , } \end{array}$ , because they need to pay at least r to make the negotiation a success; a failure to negotiate leaves them empty handed. Consequently, the negotiation will break down when $r \geq D$ . The seller will offer a demonstration if the expected payoff is more than that stated in Lemma 1. In other words, a demonstration is justified if none of the players are worse off, whereas the seller is strictly better off with the demonstration. Note that the comparison between the demonstration scenario and the no demonstration scenario is not only a comparison of two information structures (where the buyer is informed under one structure and uninformed under the other) but more importantly, a comparison between two follow-up mechanisms that are used in conjunction with their corresponding information structures. Proposition 1 states the conditions under which a demonstration is justified (the proof is in Online Appendix D).

Proposition 1. The seller’s decision to (or not to) offer a demonstration is based on the following criteria.

1. The seller will offer a demonstration with accuracy $\alpha = 1$ when $\begin{array} { r } { D _ { L } \leq r \leq \frac { p _ { H } D _ { H } } { 1 + p _ { H } } . } \end{array}$ , and the buyer will be indifferent to accepting or rejecting the offer.

2. The seller will not offer a demonstration when $r < \mathrm { m i n } \{ D _ { L } , { \frac { D } { \gamma } } \}$

3. The seller will be indifferent otherwise.

Proposition 1 illustrates the importance of the seller’s outside option. It states that the seller will benefit by offering a demonstration when they have a relatively highvalued outside option. To understand Proposition 1(1), we need to first recognize the trade-off faced by the seller. By offering a demonstration, the seller can reduce the buyer’s value uncertainty (that is, make the buyer more informed about the true value of the data). However, in doing so, the seller does not become more informed. This leads to a genuine predicament for the seller. Should they risk making the buyer more informed (and thereby, put the buyer in a better position to bargain) or forgo some extra value that might arise, because the demonstration reveals that the data are of high value? The seller can risk making the buyer more informed if he or she has a sufficiently attractive outside option. A moderately high outside option acts as a backup for the seller, alleviating the risks owing to uncertainty and making the seller less vulnerable even when the buyer becomes aware of the true value.

To understand this better, let us consider the situation where $\begin{array} { r } { D _ { L } < \mathrm { m i n } ( \frac { D } { 2 } , r ) , \alpha = 1 } \end{array}$ , and the state turns out to be L. In the no demonstration negotiation, the buyer will be hurt, because he or she would have paid a price $\begin{array} { l } { { \frac { D } { 2 } } } \end{array}$ (when $\begin{array} { r } { r \leq \frac { D } { 2 } ) } \end{array}$ or r (when $\begin{array} { r } { r \ge \frac { D } { 2 } ) } \end{array}$ , both of which are greater than $D _ { L } .$ Scott and Yalch (1980) point out that, if a buyer interprets a sample (that is, a demo) as a signal for a poorly performing product, it could affect them negatively. Thus, the fear of getting a negative payoff in state L will compel the buyer to transfer the positive probabilities $\bar { \mu } ^ { * } ( d \vert S _ { L } ) > 0$ from prices higher than $D _ { L }$ to the disagreement alternative, where the payoff is 0. However, the seller gains from this action of the buyer, because each price choice q d in the range $D _ { L } < q ( d ) < r$ is strictly dominated by the disagreement alternative $d ^ { * }$ under mechanism $\mu ^ { * } ( d \vert S _ { L } )$ This is because the buyer’s payoffs from alternatives $\{ d : D _ { L } < q ( d ) \}$ in state L are negative. In addition, the seller’s payoffs in state L from alternatives $\{ d : q ( d ) < r \}$ are less than the disagreement payoff r. As a result, both players will agree to select the disagreement alternative $d ^ { * }$ under mechanism $\mu ^ { * } ( d \vert S _ { L } )$ over any price in the range $D _ { L } < q ( d ) < r .$ . By offering a demonstration, the seller is able to convey this information to the buyer and thereby, persuade him or her to give positive probability (that is, $\mu ^ { * } ( d ^ { * } | S _ { L } ) > 0 )$ to the disagreement alternative rather than to a price between $D _ { L }$ and r if the data turn out to be of low value. To improve the expected payoff beyond the no demonstration negotiation payoff, the probability $p _ { H }$ needs to be at least $\frac { r } { D _ { H ^ { - r } } }$ . This is equivalent to saying that r can be at most $\frac { p _ { H } D _ { H } } { 1 + p _ { H } }$ . The seller will not achieve this advantage beyond $\scriptstyle r = { \frac { D _ { H } } { 2 } }$ (which corresponds to $p _ { H } = 1 )$ $\mathrm { A s }$ shown in Online Appendix D, the buyer is indifferent in accepting or rejecting this offer. The seller can encourage the buyer to accept the offer by sharing a small portion of her payoff as a token for participation thereby making it a win-win situation for them.

Figure 2 illustrates when an outside option for the seller can increase her equilibrium payoff. The shaded area depicts the seller’s gain with a demonstration Interestingly, the seller’s expected payoff increases with α (Figure 2), implying that he or she will gain more by providing a perfect demo—that is, one with complete information $( \alpha = 1 )$ . In this example, note that there is no value of outside option that will make a demo viable when $\begin{array} { r } { \alpha < \frac { p _ { H } ( 2 D _ { H } - D ) } { p _ { H } ( 2 D _ { H } - D ) + p _ { L } ( D - 2 D _ { L } ) } = 0 . 8 2 3 } \end{array}$

The buyer will never be worse off after a demo with complete information (relative to one with incomplete information), because it removes the uncertainty in the valuation of the data product. If both players become aware of the true value, the negotiation will happen under full information, where the ex ante equilibrium expected payoffs are $\begin{array} { l } { { \frac { D } { \mathrm { \Omega } ^ { \prime } } } } \end{array}$ for $\begin{array} { r } { r \leq \frac { D } { 2 } . } \end{array}$ . The solution to problem $( S _ { N } B _ { Y } )$ (provided in Online Appendix B) indicates that, without a demonstration $( \alpha = 0 . 5 )$ , the negotiation will be unsuccessful when $D < r .$ . However, a demonstration can make a negotiation successful when $D < r < D _ { H }$

Figure 2. Effect of Learning from the Demo on Seller’s Equilibrium Payoff When $\bar { D } _ { L } = 1 , D _ { H } = 1 0 _ { . }$ , and $p _ { H } = 0 . 6$  
![](/api/attachments/D89DZDSY/fulltext/images/261417df14b705d426899f8c31b37e086abd9e12b173d41d6d558cf74c320beb.jpg)

Proposition 1(2) indicates that the seller gets hurt after a demonstration when the outside option is small $( r < \operatorname* { m i n } ( D _ { L } , { \frac { D } { 2 } } ) )$ ). In this case, the small outside option is not enough to overcome the loss resulting from the low signal (L). Specifically, if the signal turns out to be of low value, the buyer will not consider any of the higher prices above $D _ { L }$ in the lower state, and all positive probabilities $\mu ^ { * } ( d \vert S _ { L } ) > 0$ pertaining to prices above $D _ { L }$ are transferred to the disagreement alternative. Because the disagreement outcome r is below $D _ { L }$ and ${ \scriptstyle { \frac { D } { 2 } } } ,$ the seller’s expected price falls below $\begin{array} { l } { { \frac { D } { 2 } } } \end{array}$ (obtained when no demonstration is provided). Therefore, in this situation, providing more information to the buyer hurts the seller. Consequently, the seller will not let the buyer update her belief by offering a demonstration. For other ranges of parameters, the seller will be indifferent to offering a demo.

Although superficially, our results seem to replicate existing results on trial and learning, the underlying mechanism and trade-offs are completely different. Prior work on this topic considers a market consisting of buyers with heterogeneous valuations, where the price is fixed by a monopolist seller (Shapiro 1983, Lewis and Sappington 1994, Chellappa and Shivendu 2005, Bhargava and Chen 2012, Cheng and Liu 2012, Wei and Nault 2013, Niculescu and Wu 2014, Cheng et al. 2015). In such situations, the seller can exploit the volume and the margin by using traditional strategies, such as versioning, differential pricing, and the acquisition of new buyers through positive network effects. The downside of a trial in these models comes essentially from the loss of revenue resulting from giving part of the value away for free (Cheng and Liu 2012, Niculescu and Wu 2014, Ray et al. 2017) and cannibalization (Cheng and Tang 2010, Cheng and Liu 2012). In contrast, our model is structurally different, because we are considering a bargaining setup between two players, where the price is the outcome of a joint decision resulting from a negotiation. Furthermore, the volume and margin factors (word-ofmouth effects, repeat purchases, and differential pricing) are absent in our model. Our result is the outcome of information asymmetry and an outside option—aspects not considered in prior literature on trials/demonstrations. Offering a demo creates information asymmetry between the players, with the buyer getting an upper hand. However, the decision mechanism is able to extract the truth from the buyer, which helps the seller. A moderately high outside option gives the seller’s expected payoff another boost and increases it above the no demo level.

An interesting aside is that any updated belief by the seller regarding the distribution of data value wil not affect the outcome of the negotiation. This contrasts with the buyer’s situation, where any learning on the part of the buyer via a demonstration affects the equilibrium expected payoffs. To better comprehend this, we need to understand how the updated belief is changing the players’ payoff structures in each alternative. The buyer’s payoff in any alternative $d \neq d ^ { * }$ depends on the realization of the true state of the value: that is, $u _ { B } ( d , t ) = D _ { t } - q ( d )$ where $t \in \{ L , H \}$ Therefore, an incentive-compatible mechanism is needed to ensure that the buyer does not lie about the true value and get undue advantage. This changes the negotiation problem to a generalized Nash bargaining problem. Any update about the belief by the buyer wil change the expected payoffs of the negotiation based on Equations $( 3 ) ‐ ( 7 )$ . However, the seller’s payoff $u _ { S } ( d ) =$ $q ( d )$ remains unaffected by the true state of the value of the data set. Therefore, the seller does not have any incentive to lie about the true value, and no incentivecompatible mechanism is required for the seller. There fore, as stated in Lemma 2 and shown in Online $\mathrm { A p \mathrm { - } }$ pendix E, the expected payoffs of the players remain unchanged even when the seller updates her belief about the distribution of data set value. This is precisely why only the buyer’s belief governs the price negotiation, and signaling through a demonstration becomes even more critical.

Lemma 2. The outcome of the negotiation does not change when the seller updates her beliefs about the probability distribution of data set value.

## 3.2. When Prior Probabilities Are Not Common Knowledge

In this section we relax our assumption that both the seller and the buyer have the same prior probabilities of data value. Suppose that the seller assumes a distribution of the value to be $D _ { H }$ with probability $p _ { H }$ and $D _ { L }$ with probability $p _ { L } = 1 - p _ { H } ,$ , and the buyer assumes it to be $p _ { H } ^ { B } < \dot { p _ { H } }$ (implying that the buyer assumes that $p _ { L } ^ { B } = \bar { 1 } - \dot { p } _ { H } ^ { B } )$ . As explained in Lemma $^ { 2 , }$ the equilibrium prices will depend on the buyer’s beliefs about the distribution. Consequently, the negotiation without a demonstration and in the absence of any seller’s outside option will result in an equilibrium expected price of $\frac { D ^ { \hat { B } } } { \gamma }$ (obtained from Lemma 1 by replacing D with ${ \cal D } ^ { \cal B } = \bar { p _ { H } ^ { B } } { \cal D } _ { H } + p _ { L } ^ { B } { \cal D } _ { L } )$ . After a successful negotiation (without a demonstration) and subsequent analysis of the data, the buyer observes that the true distribution is the same as that assumed by the seller. Therefore, the equilibrium expected payoff for the buyer is given by D minus the equilibrium price (where ${ \cal D } \bar { = } p _ { H } D _ { H } \bar { + } p _ { L } D _ { L } )$ as stated in Lemma 3.

Lemma 3. When the buyer assumes the distribution $o f$ the data to be $D _ { H }$ with probability $p _ { H } ^ { B } < p _ { H }$ and $D _ { L }$ with probability $p _ { L } ^ { B } = 1 - p _ { H } ^ { B }$ and the seller does not provide a demonstration, a negotiation in the absence of an outside option will result in the following expected payoffs to the seller $( U _ { S } ^ { * } )$ and the buyer $( U _ { B } ^ { * } )$ , respectively, where $D ^ { B } =$ $p _ { H } ^ { B } D _ { H } + \bar { p } _ { L } ^ { B } D _ { L }$ and ${ \cal D } = p _ { H } D _ { H } + p _ { L } \bar { D } _ { L }$

$$
\left(U _ {S} ^ {*}, U _ {B} ^ {*}\right) = \left(\frac {D ^ {B}}{2}, D - \frac {D ^ {B}}{2}\right).
$$

The buyer’s expected payoff increases without a demonstration as $D > D ^ { \tilde { B } } .$ . However, the seller would have received the higher expected payoff of $\begin{array} { l } { { \frac { D } { 2 } } } \end{array}$ instead of $\frac { D ^ { B } } { 2 }$ if the buyer had assumed the probabilities correctly. In this situation, the seller could correct the buyer’s prior beliefs by revealing that there is a greater proportion of customers—namely, $p _ { H }$ rather than $p _ { H } ^ { B } -$ who have benefited to the extent of $D _ { H }$ . Providing this information through a demo is clearly beneficial for the seller, because $p _ { L } ^ { B } D _ { L } + p _ { H } ^ { B } D _ { H } < p _ { L } \dot { D _ { L } } + p _ { H } D _ { H }$ . Note that the seller has no incentive to deliberately signal a value of the high-value probability to be anything less than $p _ { H }$ . Having corrected the priors, the seller has no additional incentive to provide a demo that reduces uncertainty when the outside option is absent.

## 4. Underestimation

As mentioned earlier, buyers have been known to underestimate the value of experience goods when the true value is not known (Shapiro 1983, Heiman and Muller 1996). We allow this underestimation to be associated with the higher payoff value. Because underestimation on the part of the buyer reduces the price that he or she would be willing to pay, the seller would want to ensure that this bias is corrected. Correcting the bias entails that information on the payoffs and associated probabilities is common knowledge— that is, ensuring that the buyer has not underestimated the payoff itself. Because the data are proprietary, the seller has experience on how similar data sets have helped other customers. Note that this bias-correcting demo is different from the uncertainty-reducing demos considered so far. Note also that any overestimation on the part of the buyer will result in the seller not providing a demo, because the demo can only lower the buyer’s expectations.

In the following subsections, we first consider underestimation in the absence of any outside option for the seller. We then consider the situation where an outside option exists.

## 4.1. Buyer Underestimates High Value

In this section, we analyze the effect of a demonstration when the buyer underestimates the true value. Here, the buyer underestimates the high value to be $D _ { H }$ rather than $D _ { H } ^ { + } \ ( > D _ { H } )$ . Without a bias-correcting demonstration, the buyer will not know that he or she is actually underestimating the data set value. As explained in Lemma 2 and shown in Online Appendix $\scriptstyle \mathrm { E , }$ , the negotiation will proceed as if both players assume the underestimated distribution (even though the seller knows the true distribution to be $D _ { L }$ and $D _ { H } ^ { + }$ with probabilities $p _ { L }$ and $p _ { H } ,$ , respectively). The equilibrium prices decided by the negotiation will be based on the buyer’s belief of the value and will remain unaffected by the seller’s belief. This results in an equilibrium expected price of $\begin{array} { l } { { \frac { D } { 2 } } } \end{array}$ in the absence of seller’s outside option, where $D = \mathsf { \bar { p } } _ { L } D _ { L } + p _ { H } D _ { H }$ . However, after a successful negotiation (without a demonstration) and subsequent analysis of the data, the buyer will update her belief to the true value of either $D _ { L }$ or $D _ { H } ^ { + }$ . Therefore, the buyer’s equilibrium expected payoff is given by $D ^ { + }$ minus the equilibrium price, where $D ^ { + } = \breve { p _ { L } } D _ { L } + \bar { p _ { H } } D _ { H } ^ { + } ,$ as stated in Lemma 4.

Lemma 4. When the buyer underestimates the value of the data and the seller does not provide a demonstration, a negotiation in the absence of seller’s outside option will result in following expected payoffs for the seller $( U _ { S } ^ { * } )$ and buyer $( U _ { B } ^ { * } )$ , respectively:

$$
\left(U _ {S} ^ {*}, U _ {B} ^ {*}\right) = \left(\frac {D}{2}, D ^ {+} - \frac {D}{2}\right).
$$

The seller would have received the higher expected payoff of $\frac { D ^ { + } } { 2 }$ instead of $\begin{array} { l } { { \frac { D } { 2 } } } \end{array}$ if the buyer had not underestimated. In this situation, the seller could provide a bias-correcting demonstration to the buyer and increase the buyer’s willingness to pay. A bias-correcting demo could consist of providing information about customers who have benefited to the extent of $D _ { H } ^ { + }$ in the proportion $p _ { H }$ —because we are dealing with proprietary data, the seller has this information available for disclosure.

If the seller could convey to the buyer that the high value is $D _ { H } ^ { + }$ rather than $D _ { H }$ , Lemma 4 says that the seller will earn $\textstyle { \frac { D ^ { + } } { 2 } }$ instead of $\begin{array} { r } { \frac { D } { 2 } . } \end{array}$ . Because $\begin{array} { r } { \frac { D ^ { + } } { 2 } > \frac { D } { 2 } , } \end{array}$ this would always be preferable to the seller. Having conveyed this new high value $( D _ { H } ^ { + } )$ , it is easy to see that the seller has no incentive to change the probability distribution assumed by the buyer—that is, the seller has no incentive to provide an uncertainty-reducing demonstration. This follows from Proposition 1(2), where we show that, in the absence of underestimation and outside options, the seller should not provide a demonstration. The only question that remains is whether there is some value between $D _ { H }$ and $D _ { H } ^ { + } ,$ , say $\hat { D } ,$ for which a demo is optimal. However, we can invoke Proposition 1(2) again to argue that an uncertaintyreducing demo will not be optimal at $\hat { D } ,$ because the seller gains more as $\hat { D }$ increases. Thus, we can conclude that the optimal strategy for the seller is to provide a demo that only enables the buyer to recognize that the high value is $\dot { D } _ { H } ^ { + }$ . That is, the demo does not facilitate any updates of $p _ { L }$ and $p _ { H }$ by the buyer.

## 4.2. Underestimation with an Outside Option

So far, we have observed two types of demonstrations— one that reduces uncertainty and another that reduces bias. We saw that, in the presence of an outside option, it can help to give an uncertainty-reducing demo that provides perfect information. We also saw that, in the presence of estimation bias (and no outside option), the demo provided only corrects bias—that is, it plays no role in reducing uncertainty. When both forces—an outside option and underestimation— coexist, the tussle between them has the potential to result in uncertainty reduction demos in situations where they would otherwise have not been offered by the seller.

As we saw in the previous section, a bias-correcting demo will reveal the true high value. After the bias has been corrected, Proposition 1 determines whether an uncertainty-reducing demo will be offered or not. Proposition 1 says that a perfect uncertainty-reducing demo will be offered when $\begin{array} { r } { D _ { L } < r < \frac { p _ { H } D _ { H } } { 1 + p _ { H } } } \end{array}$ . After the bias is corrected (through an increase in the high value), the right side of this inequality— $\cdot \frac { p _ { H } D _ { H } } { 1 + p _ { H } } - \mathrm { w i l l }$ increase. However, because $D _ { L }$ is unchanged, the lefthand side is unaffected. Therefore, if an uncertaintyreducing demo would have been offered in the face of underestimation, it will continue to be offered even after the underestimation is eliminated.

Proposition 1 says that there will be a negotiation without any uncertainty-reducing demonstration if $r < \mathrm { m i n } \{ D _ { L } , { \stackrel { D } { 2 } } \}$ . Because $D _ { L }$ is unchanged, an increase in $D _ { H }$ will not move r into the range where a perfect uncertainty-reducing demo will be offered (because $r > D _ { L }$ in that range). Consequently, the same outcome will result—that is, there will be a successful negotiation without an uncertainty-reducing demonstration.

Based on these results, the situations where an uncertainty-reducing demo will be offered have not changed. However, the case when $r > D$ (that is, when there would have been no negotiation without bias correction) is more interesting. In this case, when bias is corrected (and the bias was sufficiently high), not only could it lead to a successful negotiation, it could also result in the provision of an uncertainty-reducing demo by the seller. This is because negotiations break down when $r > D$ (Lemma 1). After the bias is corrected, the new value of D will be $D ^ { + }$ , which could be greater than r. If $r < D ^ { + }$ , we know that a successful negotiation will result. In addition, if the extent of highvalue underestimation was significant enough that r becomes less than $\frac { p _ { H } D _ { H } ^ { + } } { 1 + p _ { H } }$ , the optimal approach would be to provide an uncertainty-reducing demo in addition to the bias-correcting one. Thus, the overall insight from this discussion is that the provision of a bias-correcting demo could trigger the provision of an uncertainty-reducing demo as well.

## 5. The Impact of a Demonstration Cost

So far, we have assumed that offering a demo comes with no cost. However, developing a customized demo—one that signals a specific level of information to the buyer—could require the seller to expend time and effort. Existing literature on demos and versioning has also considered the cost of development and information dissemination (Heiman et al. 2001, Wang and Zhang 2009, Jones and Mendelson 2011, Lahiri and Dey 2018). In this section, we extend our model to incorporate a cost of developing a demo. We assume this cost to be dependent on the strength of the signal: that ${ \mathrm { i } } \mathbf { s } ,$ on the extent of information that the seller would like to provide through the demo. Consequently, the seller incurs an α-dependent demo cost c α if the seller decides to offer a demo of signal strength α and incurs no cost if no demo is offered (that is, $c ( 0 . 5 ) = 0 )$ We solve the generalized Nash bargaining problem by modifying the seller’s payoff for each price alternative as $u _ { S } ( d , t ) = q ( d ) - \bar { c } ( \alpha )$ for $d \neq d ^ { * }$ and $u _ { S } ( d , t ) =$ $r - c ( \alpha )$ for $d = d ^ { * }$ . Proposition 2 shows that the seller’s opportunities to offer a demo have diminished as a result of the demo cost (the proof is in Online Appendix G).

Proposition 2. The seller’s decision to (or not to) offer a demonstration in the presence of the demonstration cost is based on the following criteria.

1. The seller will offer a demonstration when $V _ { L } +$ $\begin{array} { r } { \frac { c ( \alpha ) } { P _ { L } } \leq r \leq \frac { P _ { H } V _ { H } - c ( \alpha ) } { 1 + P _ { H } } . } \end{array}$

2. The seller will not offer a demonstration when $r <$ min $\{ V _ { L } + \frac { c ( \alpha ) } { P _ { L } } , \frac { D } { 2 } \}$

3. The seller will be indifferent otherwise.

Here, $\begin{array} { r } { V _ { H } = \frac { \alpha p _ { H } D _ { H } + ( 1 - \alpha ) p _ { L } D _ { L } } { P ( S _ { H } ) } , V _ { L } = \frac { ( 1 - \alpha ) p _ { H } D _ { H } + \alpha p _ { L } D _ { L } } { P ( S _ { L } ) } , P _ { L } = } \end{array}$ $\alpha p _ { L } \ + ( 1 - \alpha ) p _ { H } ,$ , and $P _ { H } = 1 - P _ { L }$

We examine the consequences of this proposition further by considering three different α-dependent convex cost structures—(i) linear (that is, $c ( \alpha ) = k ( \alpha -$ 0.5 ), (ii) quadratic (that is, $c ( \alpha ) = k ( \alpha - 0 . 5 ) ^ { 2 } )$ , and (iii) hyperbolic $\begin{array} { r } { ( c ( \alpha ) = \frac { k ( \alpha - 0 . 5 ) } { 1 - \alpha } ) } \end{array}$ , where k is a positive constant. The results are in Corollary 1 and proved in Online Appendix H.

Corollary 1. The seller’s decision based on the α-dependent demonstration cost is as follows.

Linear cost. The seller will offer a demonstration with accuracy $\alpha = 1$ when $\begin{array} { r } { D _ { L } + \frac { c ( \overline { { \alpha } } ) } { p _ { L } } \leq r \leq \frac { p _ { H } D _ { H } - c ( \alpha ) } { 1 + p _ { H } } } \end{array}$ and $k <$ $p _ { H } D _ { H } - p _ { L } D _ { L } - ( p _ { H } - p _ { L } ) r .$

Quadratic cost. The seller will offer a demonstration with accuracy $\alpha = 1$ when $\begin{array} { r } { D _ { L } + \frac { c ( \alpha ) } { p _ { L } } \overset { \sim } { \le } r \le \frac { p _ { H } D _ { H } - c ( \alpha ) } { 1 + p _ { H } } } \end{array}$

Hyperbolic cost. The seller will offer a demonstration with accuracy $\begin{array} { r } { \alpha ^ { * } = 1 - \sqrt { \frac { k } { 2 ( p _ { H } D _ { H } - p _ { L } D _ { L } - ( p _ { H } - p _ { L } ) r ) } } } \end{array}$ when $V _ { L } ^ { * } +$ $\begin{array} { r } { \frac { c ( \alpha ^ { * } ) } { P _ { L } ^ { * } } \leq r \leq \frac { P _ { H } ^ { * } V _ { H } ^ { * } - c ( \alpha ^ { * } ) } { 1 + P _ { H } ^ { * } } , } \end{array}$ , where $V _ { L } ^ { \ast } , V _ { H } ^ { \ast } , P _ { L } ^ { \ast } , P _ { H } ^ { \ast } ,$ , and $c ( \alpha ^ { * } )$ are based on $\alpha ^ { * }$ .

Both linear and quadratic costs result in either no demo or a perfect demo being offered (that is, $\alpha = 1 )$ However, the hyperbolic cost structure—where the demo cost can increase quickly—suggests that an internal optimum level of signal $\alpha ^ { * }$ exists for a moderately high outside option. This suggests that the seller can control the extent to which the potential buyer can learn from a demo. This is in contrast with some existing work, which proposes boundary solutions when information dissemination through sampling and versioning is costly (Lewis and Sappington 1994, Johnson and Myatt 2006). However, Dey and Lahiri (2016) suggest that an interior optimum solution is possible when the consumers learn from a lower version. Figure 3 shows the effect of different cost structures on the seller’s equilibrium payoff.

## 6. The Impact of Cannibalization

Our context is one where the seller can create demos in such a way that the threat of cannibalization is minimal. For example, the data set could be chosen such that estimates derived from it are not close to corresponding estimates from the full data set (for example, through the use of a synthetic data set). This would allow the buyer to realize the kinds of insights (for example, an airline would realize that they can identify users who searched for fares but did not purchase a ticket) that the full data would reveal without revealing any specific information. Consequently, the threat of cannibalization, for the most part, may not be significant. However, if cannibalization exists, it can impact the design of the demo. In this section, we evaluate the impact of cannibalization on the negotiation.

![](/api/attachments/D89DZDSY/fulltext/images/7dc04a852023c005a87784bf6239a781b7a9c9907f6405564cdad3c1e8cffa8d.jpg)

Cannibalization in our context would result in the buyer extracting some value from the demo, impacting the seller’s options as a result. Clearly, if the demo reveals everything that the buyer needs to know, the buyer can walk away after the trial without a pur chase (Cheng and Tang 2010, Cheng and Liu 2012, Niculescu and Wu 2014). Lahiri and Dey (2018) have shown that cannibalization can lead to versioning under certain circumstances. In this analysis, we assume that a fraction λ of the value is cannibalized if a free demo is offered. That is, the buyer realizes a value of $\lambda D _ { t }$ from the demonstration $\left( t \overset { \cdot } { = } L , H \right)$ , and the remaining value $( 1 - \lambda ) D _ { t }$ is negotiated between the players. Cannibalization also impacts the outside option, because the data are now less valuable to others— we assume that the outside option is lowered in the same proportion, λ. That is, the outside option reduces to $( 1 - \lambda ) r$ after the demo. The payoffs to the seller and the buyer for alternative d d∗ are $u _ { S } ( d , t ) =$ $q ( d )$ and $u _ { B } ( d , t ) \dot { = } ( 1 - \lambda ) D _ { t } - q ( d )$ , respectively. The conditional expected payoff $U _ { B } ( \mu , S _ { H } | S _ { H } )$ for the buyer contains the expected payoffs from all of the alternatives as well as the cannibalized value, and it is

$$
\begin{array}{l} U _ {B} \big (\mu , S _ {H} | S _ {H} \big) \\ = \sum_ {d \in \Phi \setminus \{d ^ {*} \}} \mu (d | S _ {H}) (u _ {B} (d, H) P (H | S _ {H}) + u _ {B} (d, L) P (L | S _ {H})) \\ \quad + \lambda D _ {H} P (H | S _ {H}) + \lambda D _ {L} P (L | S _ {H}) \\ = \sum_ {d \in \Phi \setminus \{d ^ {*} \}} \mu (d | S _ {H}) \Big (((1 - \lambda) D _ {H} - q (d)) \frac {\alpha p _ {H}}{P (S _ {H})} \\ \quad + ((1 - \lambda) D _ {L} - q (d)) \frac {(1 - \alpha) p _ {L}}{P (S _ {H})} \Big) + \lambda \left(D _ {H} \frac {\alpha p _ {H}}{P (S _ {H})} + D _ {L} \frac {(1 - \alpha) p _ {L}}{P (S _ {H})}\right) \\ = \sum_ {d \in \Phi \setminus \{d ^ {*} \}} \mu (d | S _ {H}) \left(\frac {\alpha p _ {H} (1 - \lambda) D _ {H} + (1 - \alpha) p _ {L} (1 - \lambda) D _ {L}}{\alpha p _ {H} + (1 - \alpha) p _ {L}} - q (d)\right) \\ \quad + \lambda \left(\frac {\alpha p _ {H} D _ {H} + (1 - \alpha) p _ {L} D _ {L}}{\alpha p _ {H} + (1 - \alpha) p _ {L}}\right) \\ = \sum_ {d \in \Phi \setminus \{d ^ {*} \}} \mu (d | S _ {H}) \big ((1 - \lambda) V _ {H} - q (d) \big) + \lambda V _ {H}, \end{array}\tag{10}
$$

where $\begin{array} { r } { V _ { H } = \frac { \alpha p _ { H } D _ { H } + ( 1 - \alpha ) p _ { L } D _ { L } } { P ( S _ { H } ) } } \end{array}$ <sup>L</sup>. Note that the Equation (10) can be rewritten as $\begin{array} { r } { \tilde { U } _ { B } ( \mu , S _ { H } | S _ { H } ) = \sum _ { d \in \Phi \backslash \{ d ^ { * } \} } \mu ( d | S _ { H } ) ( V _ { H } - } \end{array}$ $q ( d ) ) + \mu ( d ^ { * } | S _ { H } ) \lambda V _ { H } ,$ , which implies that the cannibalized value $\lambda V _ { H }$ is the disagreement outcome for the buyer in case of high signal. Similarly, the buyer will receive a disagreement outcome of $\lambda V _ { L }$ when the signal is low, where $\begin{array} { r } { V _ { L } = \frac { ( 1 - \alpha ) p _ { H } D _ { H } + \alpha p _ { L } D _ { L } } { P ( S _ { I } ) } } \end{array}$ . If the buyer decides to walk away after the demo without buying the data, then he or she will receive a positive expected payoff of $P ( S _ { L } ) \lambda V _ { L } + P ( S _ { H } ) \lambda V _ { H } = \lambda \mathbf { \hat { \cal D } }$ . This can be viewed as conceptually similar to a buyer’s outside option. The seller’s expected payoff $U _ { S } ( \mu )$ is calculated as follows:

$$
\begin{array}{r l} & U _ {S} \big (\mu \big) = U _ {S} \big (\mu , S _ {L} | S _ {L} \big) P (S _ {L}) + U _ {S} \big (\mu , S _ {H} | S _ {H} \big) P (S _ {H}) \\ & \quad = \sum_ {d \in \Phi \setminus \{d ^ {*} \}} \mu (d | S _ {L}) \big (q _ {S} (d) P (L | S _ {L}) \\ & \qquad + q _ {S} (d) P (H | S _ {L}) \big) P (S _ {L}) + \sum_ {d \in \Phi \setminus \{d ^ {*} \}} \mu (d | S _ {H}) \\ & \qquad \cdot \big (q _ {S} (d) P (L | S _ {H}) + q _ {S} (d) P (H | S _ {H}) \big) P (S _ {H}) \\ & \qquad + (1 - \lambda) r \big (\mu (d ^ {*} | S _ {L}) P (S _ {L}) + \mu (d ^ {*} | S _ {H}) P (S _ {H}) \big) \\ & = \sum_ {d \in \Phi \setminus \{d ^ {*} \}} \big (\mu (d | S _ {L}) P (S _ {L}) + \mu (d | S _ {H}) P (S _ {H}) \big) q _ {S} (d) \\ & \qquad + (1 - \lambda) r \big (\mu (d ^ {*} | S _ {L}) P (S _ {L}) + \mu (d ^ {*} | S _ {H}) P (S _ {H}) \big). \end{array}\tag{11}
$$

This results in the following Nash product:

$$
\begin{array}{l l} & (S _ {N} B _ {Y}) _ {c a n} \\ \max _ {\mu \in \Psi} & U _ {S} (\mu) \cdot (U _ {B} (\mu , S _ {L} | S _ {L})) ^ {(1 - P (S _ {H}))} \cdot (U _ {B} (\mu , S _ {H} | S _ {H})) ^ {P (S _ {H})} \\ \text {s.t.} & U _ {B} (\mu , S _ {L} | S _ {L}) \geq U _ {B} (\mu , S _ {H} | S _ {L}) \\ & U _ {B} (\mu , S _ {H} | S _ {H}) \geq U _ {B} (\mu , S _ {L} | S _ {H}) \\ & U _ {S} (\mu) \geq (1 - \lambda) r \\ & U _ {B} (\mu , S _ {L} | S _ {L}) \geq 0; U _ {B} (\mu , S _ {H} | S _ {H}) \geq 0 \\ & \sum_ {d \in \Phi} \mu (d | S _ {L}) = 1; \sum_ {d \in \Phi} \mu (d | S _ {H}) = 1 \\ & \mu (d | S _ {L}) \geq 0; \mu (d | S _ {H}) \geq 0 \quad \forall d \in \Phi \\ & u _ {B} (d, t) + q (d) = (1 - \lambda) D _ {t}; \forall d \in \Phi \backslash \{d ^ {*} \}; \\ & t \in \{L, H \} \\ & u _ {S} (d, t) = q (d); \forall d \in \Phi \backslash \{d ^ {*} \}; t \in \{L, H \} \\ & u _ {B} (d ^ {*}, t) = 0; u _ {S} (d ^ {*}, t) = (1 - \lambda) r. \end{array}
$$

Proposition 3 (the proof is in Online Appendix I) characterizes the trade-off between the adverse effect of cannibalization and the benefit of having an outside option. The seller will offer a demo if the benefit from the outside option is large enough to outweigh any loss from cannibalization. This is true even in the absence of underestimation. As λ increases, so does the extent of cannibalization (while the outside option decreases). Consequently, for $\begin{array} { r } { \lambda > 1 - \frac { D } { 2 V _ { H } } , } \end{array}$ , no value

Figure 4. Seller’s Equilibrium Payoff vs. Cannibalization $( D _ { L } = 1 , D _ { H } = 1 0 , r = 3 , p _ { H } = 0 . 6 )$  
![](/api/attachments/D89DZDSY/fulltext/images/efe9613b5314b071ec7b17aee2daa28b9975ff2ca05772cd0cab1e92a1885c3d.jpg)  
of outside option can compensate for the loss owing to cannibalization, and the seller will not offer a demo.

Proposition 3. The seller’s decision to offer a demonstration in the presence of cannibalization and in the absence of demonstration cost is based on the following criteria:

1. when $\begin{array} { r } { V _ { L } \le r \le \frac { P _ { H } V _ { H } } { 1 + P _ { H } - 2 \lambda } } \end{array}$ and $0 \leq \lambda \leq \bar { 0 } . 5$ and

2. when $\begin{array} { r } { ( \frac { D } { 2 ( 1 - \lambda ) } - P _ { H } V _ { H } ) \frac { 1 } { P _ { L } } \leq r \leq V _ { H } } \end{array}$ and $0 . 5 \leq \lambda \leq$ $\begin{array} { r } { 1 - \frac { D } { 2 V _ { H } } } \end{array}$ , where $\begin{array} { r } { V _ { H } = \frac { \alpha p _ { H } D _ { H } + ( 1 - \alpha ) p _ { L } D _ { L } } { P ( S _ { H } ) } , V _ { L } = \frac { ( 1 - \alpha ) p _ { H } D _ { H } + \alpha p _ { L } D _ { L } } { P ( S _ { L } ) } , } \end{array}$ $P _ { L } = \alpha p _ { L } + ( 1 - \alpha ) p _ { H }$ , and $P _ { H } = 1 - P _ { L }$

Figure 4 shows the effect of cannibalization on the seller’s payoff. In the range where a demo is viable, in the presence of cannibalization, a better signal can increase the seller’s expected payoff.

## 7. Conclusion

Many companies possess data that are of value to other firms. However, monetizing such proprietary data can be difficult, because the value (to both seller and buyers) is often uncertain. When large firms are involved and both sides are uncertain about the value of the data, the exchange usually occurs through a process of bargaining. In this paper, we analyze this bargaining process for the selling and buying of proprietary data.

We first consider a situation where both the seller and an unbiased buyer are unaware of the true value of the data, and the seller has an outside option to fall back on should negotiations break down.<sup>4</sup> The seller can choose to provide an uncertainty-reducing demonstration—a sample data set or a demonstration illustrating the benefits of the data—in order to let the buyer update her beliefs about the value of the data.

We find that, when the value of the outside option is moderately high, an uncertainty-reducing demonstration is justified, because it increases the seller’s expected payoff while keeping the buyer indifferent. Interestingly, if the seller chooses to offer such a demonstration, it should be one with complete information. That is, a deliberately noisy demonstration is never optimal. Concerning outside options, we find that (1) an outside option helps (never hurts) the seller to earn more and that (2) the presence of an outside option alone can be a reason for choosing to provide a demonstration. The direct benefit of an outside option is that it increases the seller’s expected payoff. The indirect benefit is that an outside option makes the seller less vulnerable to the informational advantage that the buyer accrues from knowing the true value of the data from the demonstration.

There is evidence that buyers may underestimate the value of a product when faced with uncertainty. In such situations, sellers can potentially increase their expected payoff through a bias-correcting demonstration. A bias-correcting demo has no downside to the seller unlike an uncertainty-reducing one, which puts the buyer at an informational advantage. The joint presence of underestimation and an outside option creates a situation where the demonstration strategy becomes more complex. In particular, the provision of a bias-correcting demo could not only make an otherwise unsuccessful negotiation successful, it could trigger the provision of an uncertainty-reducing demo as well.

We extend our model by considering the potential cost of a demonstration (which is assumed to be dependent on the extent of information revealed by the demo). Although linear and quadratic cost structures lead to either no demo or a perfect one being offered, hyperbolic costs can result in an internal optimal solution. This allows the seller to control the extent to which the buyer can learn from the demo, thereby providing considerable flexibility. We also consider the effects of cannibalization that could result from a demonstration. We find that an outside option can safeguard against cannibalization if the cannibalization levels are not too high, allowing the seller to offer a demo even when there is no underestimation.

The insights from this paper should help both players understand the bargaining process better when selling or buying proprietary data. The key takeaways of this paper, however, are directed at sellers of proprietary data in developing useful prebargaining strategies. First, we provide guidelines about when sellers should provide a demonstration. Also, if they choose to provide an uncertainty-reducing demonstration, it should be as accurate as possible. This insight is particularly useful, because in bargaining problems with value uncertainty, revealing more information to the buyer before entering the bargaining process typically weakens the seller’s hand. The other insight for the seller is that having an outside option can help, implying that sellers should actively try to identify an outside option as a prebargaining step.

At a higher level, our paper is about monetizing data so that sellers can extract more value in a bargaining process. The monetization of data is an important and increasingly relevant consideration, because it encourages sellers to collect and sell data, thus making them available for data-driven decision making in business. Future research on this subject could examine the role of a third party, such as a consultant who provides dataanalytic services in the bargaining process. We expect that examining such a three-party bargaining problem could provide new insights about the role of demonstrations as prebargaining strategies. Also, although our paper considered a monetization problem involving a seller and a single buyer, it will be interesting to examine optimal data monetization strategies when multiple buyers (but a single seller) are involved.

## Endnotes

<sup>1</sup> See https://www-01.ibm.com/software/data/bigdata/what-is-big -data.html

<sup>2</sup> See https://www.businesstravel-iq.com/article/2018/08/08/gds -market-share-second-quarter-2018.

<sup>3</sup> See http://invite.concordia.ca/.

<sup>4</sup> We also considered an outside option for the buyer, and this did not change the qualitative nature of our results. In the presence of can nibalization, the cannibalized value can also be viewed as an outside option for the buyer.

## References

Ausubel LM, Cramton P, Deneckere RD (2002) Bargaining with incomplete information. Aumann RJ, Hart S, eds. Handbook of Game Theory with Economic Applications, vol. 3 (Elsevier, Amsterdam), 1897–1945.

Ausubel LM, Deneckere RD (1989) A direct mechanism characterization of sequential bargaining with one-sided incomplete information. J. Econom. Theory 48(1):18–46.

Ausubel LM, Deneckere RD (1993) Efficient sequential bargaining Rev. Econom. Stud. 60(2):435–461.

Bain JS (1956) Barriers to New Competition: Their Character and Consequences in Manufacturing Industries (Harvard University Press, Cambridge, MA)

Bawa K, Shoemaker R (2004) The effects of free sample promotions on incremental brand sales. Marketing Sci. 23(3):345–363.

Beckett L, (2014) Everything we know about what data brokers know about you. Pro Publica (June 13), http://www.propublica.org article/everything-we-know-about-what-data-brokers-know -about-you.

Bhargava HK, Chen RR (2012) The benefit of information asymmetry: When to sell to informed customers? Decision Support System 53(2):345–356.

Binmore KG (1985) Bargaining and coalitions. Roth AE, ed. Game Theoretic Models of Bargaining (Cambridge University Press, Cam bridge. UK). 269-304

Binmore K, Rubinstein A, Wolinsky A (1986) The Nash bargaining solution in economic modelling. RAND J. Econom. 17(2):176–188.

Chatterjee K, Samuelson W (1983) Bargaining under incomplete in formation. Oper. Res. 31(5):835–851.

Chellappa R, Shivendu S (2005) Managing piracy: Pricing and sampling strategies for digital experience goods in vertically segmented markets. Inform. Systems Res. 16(4):400–417.

Chen Y, Xie J (2008) Online consumer review: Word-of-mouth as a new element of marketing communication mix. Management Sci. 54(3):477–491.

Cheng H, Tang Q (2010) Free trial or no free trial: Optimal software product design with network externalities. Eur. J. Oper. Res. 205(2):437–447.

Cheng HK, Li S, Liu Y (2015) Optimal software free trial strategy: Limited version, time-locked, or hybrid? Production Oper. Management 24(3):504–517.

Cheng HK, Liu Y (2012) Optimal software free trial strategy: The impact of network externalities and consumer uncertainty. In form. Systems Res. 23(2):488–504.

Davie M (2015) Simplest way to monetize data: Think of data as a product. Datafloq (March 23), https://datafloq.com/read/simplest -way-monetize-data-product/980.

DeGraba P (1995) Buying frenzies and seller-induced excess demand. RAND J. Econom. 26(2):331–342.

Dey D, Lahiri A (2016) Versioning of video games: Go vertical in a horizontal market? Proc. 49th Hawaii Internat. Conf. System Sci ences (HICSS) (IEEE, Piscataway, NJ), 5259–5268.

Dey D, Lahiri A, Liu D (2013) Consumer learning and time-locked trials of software products. J. Management Inform. Systems 30(2):239–268.

Doshi V (2015) Passenger-pleasing profitability: How big data can save airline customer service. Sabre Newsroom (February 24), http:// www.sabre.com/newsroom/passenger-pleasing-profitability-how -leveraging-big-data-could-save-airline-customer-service.

Edwards J (2013) Yes, your credit card company is selling your purchase data to online advertisers. Bus. Insider (April 16), http:// www.businessinsider.com/credit-cards-sell-purchase-data-to -advertisers-2013-4.

Fudenberg D, Tirole J (1983) Sequential bargaining with incomplete information. Rev. Econom. Stud. 50(2):221–247.

Gans JS, Hsu DH, Stern S (2008) The impact of uncertain intellectual property rights on the market for ideas: Evidence from patent grant delays. Management Sci. 54(5):982–997.

Goering PA (1985) Effects of product trial on consumer expectations, demand, and prices. J. Consumer Res. 12(1):74–82.

Gul F, Sonnenschein H, Wilson R (1986) Foundations of dynamic monopoly and the coase conjecture. J. Econom. Theory 39(1):155–190.

Guo L, Zhang J (2012) Consumer deliberation and product line design. Marketing Sci. 31(6):995–1007.

Güth W, Schmittberger R, Schwarze B (1982) An experimental analysis of ultimatum bargaining. J. Econom. Behav. Organ. 3(4):367–388.

Harsanyi J, Selten R (1972) A generalized Nash solution for twoperson bargaining games with incomplete information. Management Sci. 18(5 part 2):80–106.

Heiman A, Muller E (1996) Using demonstration to increase new product acceptance: Controlling demonstration time. J. Marketing Res. 33(4):422–430.

Heiman A, McWilliams B, Shen Z, Zilberman D (2001) Learning and forgetting: Modeling optimal product sampling over time. Management Sci. 47(4):532–546.

Hope B (2015) Provider of personal finance tools tracks bank cards, sells data to investors. Wall Street Journal (August 6), http:// www.wsj.com/articles/provider-of-personal-finance-tools-tracks -bank-cards-sells-data-to-investors-1438914620.

Jain D, Mahajan V, Muller E (1995) An approach for determining optimal product sampling for the diffusion of a new product. J. Product Innovation Management 12(2):124–135.

Johnson JP, Myatt DP (2006) On the simple economics of advertising, marketing, and product design. Amer. Econom. Rev. 96(3):756–784.

Jones R (2013) Barclays to sell customer data. The Guardian (June 24), http://www.theguardian.com/business/2013/jun/24/barclays -bank-sell-customer-data.

Jones R, Mendelson H (2011) Information goods vs. industrial goods: Cost structure and competition. Management Sci. 57(1): 164–176.

Kersten G, Lai H (2007) Negotiation support and e-negotiation systems: An overview. Group Decision Negotiation 16(6):553–586.

Kishimoto S, Muto S (2012) Fee vs. royalty policy in licensing through bargaining: An application of the Nash bargaining solution. Bull. Econom. Res. 64(2):293–304.

Lahiri A, Dey D (2018) Versioning and information dissemination: A new perspective. Inform. Systems Res. 29(4):965–983.

Lai EL-C, Qiu LD (2003) The North’s intellectual property rights standard for the South? J. Internat. Econom. 59(1):183–209.

Lee Y-J, Tan Y (2013) Effects of different types of free trials and ratings in sampling of consumer software: An empirical study. J. Man agement Inform. Systems 30(3):213–246.

Lewis TR, Sappington DEM (1994) Supplying information to facilitate price discrimination. Internat. Econom. Rev. 35(2):309–327.

Monga V (2014) The big mystery: What’s big data really worth? Wall Street Journal (October 12), https://www.wsj.com/articles/whats -all-that-data-worth-1413157156.

Moran C (2015) Facebook is now selling your web-browsing data to advertisers. Consumerist (June 12), http://consumerist.com/ 2014/06/12/facebook-is-now-selling-your-web-browsing-data -to-advertisers.

Myerson R (1984) Two-person bargaining problems with incomplete information. Econometrica 52(2):461–487.

Myerson RB (1979) Incentive compatibility and the bargaining prob lem. Econometrica 47(1):61–73.

Myerson RB, Satterthwaite MA (1983) Efficient mechanisms for bi lateral trading. J. Econom. Theory 29(2):265–281.

Nash JF (1950) The bargaining problem. Econometrica 18(2):155–162.

Niculescu MF, Wu DJ (2014) Economics of free under perpetual li censing: Implications for the software industry. Inform. Systems Res. 25(1):173–199.

Ray J, Samuel J, Menon S, Mookerjee V (2017) The design of featurelimited demonstration software: Choosing the right features to include. Production Oper. Management 26(1):9–30.

Rubinstein A (1982) Perfect equilibrium in a bargaining model. Econometrica 50(1):97–109.

Scott CA, Yalch RF (1980) Consumer response to initial product trial: A Bayesian analysis. J. Consumer Res. 7(1):32–41.

Shapiro C (1983) Optimal pricing of experience goods. Bell J. Econom. 14(2):497–507.

Shugan SM, Xie J (2000) Advance pricing of services and other implications of separating purchase and consumption. J. Service Res. 2(3):227–239.

Sobel J (1993) Information control in the principal-agent problem. Internat. Econom. Rev. 34(2):259–269.

Swinney R (2011) Selling to strategic consumers when product value is uncertain: The value of matching supply and demand. Man agement Sci. 57(10):1737–1751.

van Damme E, Binmore K, Roth A, Samuelson L, Winter E, Bolton G, Ockenfels A, et al. (2014) How Werner Güth’s ultimatum game shaped our understanding of social behavior. J. Econom. Behav. Organ. 108:292–318.

Walden EA (2005) Intellectual property rights and cannibalization in information technology outsourcing contracts. MIS Quart. 29(4): 699–720.

Wang CA, Zhang XM (2009) Sampling of information goods. Decision Support Systems 48(1):14–22.

Wei XD, Nault BR (2013) Experience information goods: Version-toupgrade. Decision Support Systems 56:494–501.

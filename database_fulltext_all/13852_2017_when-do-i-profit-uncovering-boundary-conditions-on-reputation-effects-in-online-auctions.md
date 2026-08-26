---
otero_id: 13852
otero_key: "4YU34XHQ"
title: "When do I profit? Uncovering boundary conditions on reputation effects in online auctions"
authors: "Michelle Carter; Stefan Tams; Varun Grover"
year: "2017"
journal: "Information & Management"
doi: "10.1016/j.im.2016.06.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# When do I pro<sup>fi</sup>t? Uncovering boundary conditions on reputation effects in online auctions

Michelle Carter<sup>a,</sup>\*, Stefan Tams<sup>b</sup>, Varun Grover<sup>c</sup>

<sup>a</sup> Department of Management, Information Systems, and Entrepreneurship, Carson College of Business, PO Box 644743, Washington State University, Pullman WA 991164-4743, USA

<sup>b</sup> HEC Montréal 3000, Chemin de la Côte-Sainte-Catherine, Montréal, Québec H3T 2A7, Canada

<sup>c</sup> Department of Management, Clemson University, Suite 132F, Sirrine Hall, Clemson, SC 29634, USA

## A R T I C L E I N F O

Article history: Received 21 August 2014 Received in revised form 20 December 2015 Accepted 19 June 2016 Available online xxx

Keywords: E-business Auctions Individual decision-making Empirical methods Regression methods

## 1. Introduction

## A B S T R A C T

Reputation pro<sup>fi</sup>les, based on customer feedback ratings, are important for achieving above average sales prices in online auctions. However, contradictory results in past research suggest that reputation effects may depend on information alternatives to customer feedback that sellers can provide to buyers. By explicitly modeling the competing assumptions of classical and contemporary approaches to buyer decision-making and using hierarchical linear modeling to analyse data from 363 online auctions, we found that sellers may bene<sup>fi</sup>t from carefully evaluating what information alternatives they combine with reputation pro<sup>fi</sup>le to realize higher sales prices.

ã 2016 Elsevier B.V. All rights reserved.

In online auctions (e.g., eBay), which are largely characterized by unfamiliar sellers and an absence of merchant branding, it is dif<sup>fi</sup>cult for buyers to ascertain product quality [1,5,18,20,73]. Moreover, unscrupulous sellers may misrepresent the products they are selling [34,46,55]. Consequently, in these settings, reputation systems based on customer feedback constitute an important informational resource for buyers that reduce their perceptions of transaction risk [1,5,13,58,74]. Customer feedback is solicited in a variety of ways that help otherwise unknown sellers establish a reputation. For example, eBay’s system uses individual evaluations left after each transaction to rate registered users [58]. Reputation systems such as these discourage fraudulent trading by ensuring that trading behaviors are made publicly available to an entire community via information technology (IT)-enabled summary statistics, referred to here as reputation profiles.

As it takes time to establish a good reputation, sellers must be rewarded or at least compensated for costs incurred during the reputation-building process. At the same time, the penalty for bad reputation should exceed any bene<sup>fi</sup>ts sellers might expect to gain by behaving opportunistically—thus, “in equilibrium, a good reputation must command a price premium” [8,p. 82]. Price premium has been de<sup>fi</sup>ned in the literature as the additional monetary amount buyers are willing to pay for a product above the average price received by multiple sellers for an identical product [1]. The present paper adopts this de<sup>fi</sup>nition and henceforth uses “price premium” to refer to above average prices.

Many studies have investigated the relationship between reputation pro<sup>fi</sup>le and online auction outcomes [13]. Although this literature stream suggests that a seller’s reputation pro<sup>fi</sup>le is in<sup>fl</sup>uential in buyer decision-making, past research presents contradictory results for the precise impacts of positive and negative feedback ratings on <sup>fi</sup>nal sales prices [48]; see Table 1 for an overview). Although some studies show that negative feedback has little [13] or no impact [1,3,19], others <sup>fi</sup>nd that it reduces <sup>fi</sup>nal sales prices [31,41,45]. Furthermore, while many studies show that positive feedback increases <sup>fi</sup>nal sales prices [1,3,31,45], others <sup>fi</sup>nd no such effect [41,58], or that these effects taper off for established sellers with high percentages of positive feedback [8,39].

Some previous studies have suggested that the ambiguous relationship found between feedback ratings and <sup>fi</sup>nal sales prices may be due to boundary conditions on reputation pro<sup>fi</sup>le’s in<sup>fl</sup>uence on price premiums [10]. Buyers might have a different understanding of reputation pro<sup>fi</sup>les in the presence of other information provided by sellers. Consequently, to determine under which conditions reputation pro<sup>fi</sup>le is effective, there is a need to examine the interplay between this informational resource and

M. Carter et al. / Information & Management xxx (2016) xxx–xxx

Table 1  
Impact of Reputation Pro<sup>fi</sup>le on Final Sales Prices: Summary of Previous Results (adapted from [13]

<table><tr><td rowspan="2">Citation</td><td colspan="2">Impact of Reputation Profile on Final Sales Prices</td></tr><tr><td>Positive Feedback</td><td>Negative Feedback</td></tr><tr><td>Ba and Pavlou [1]</td><td>Increases final sales price</td><td>No effect</td></tr><tr><td>Bajari and Hortaçsu [3]</td><td>Significant effect on final price</td><td>No effect</td></tr><tr><td>Bockstedt and Goh [8]</td><td colspan="2">Seller feedback scores are less effective tools for differentiation in competitive auction environments</td></tr><tr><td>Dewan and Hsu [14]</td><td>Higher net feedback score increases price</td><td></td></tr><tr><td>Eaton [19]</td><td></td><td>Reduces likelihood of sale but not final sales price</td></tr><tr><td>Houser and Wooders [31]</td><td>Increases final sales price</td><td>Reduces final sales price</td></tr><tr><td>Lee [37]</td><td></td><td>Reduces final sales price but only for used items</td></tr><tr><td>Livingston [39]</td><td>Effect tapers off for established sellers</td><td></td></tr><tr><td>Lucking-Reiley et al. [41]</td><td>No effect</td><td>Reduces final sales price</td></tr><tr><td>Melnik and Alm [45]</td><td>Increases final sales price</td><td>Reduces final sales price</td></tr><tr><td>McDonald and Slawson [75]</td><td>Higher net feedback score increases price</td><td></td></tr><tr><td>Resnick and Zeckhauser [59]</td><td>No effect on prices contingent on sale</td><td></td></tr><tr><td>Resnick et al. [60]</td><td>Controlled experiment; established seller commands higher prices than new seller</td><td>Among new sellers, a small amount of negative feedback has little effect</td></tr></table>

other types of information in the choice context (henceforth referred to as information alternatives; [13,37,67]. As contradictory <sup>fi</sup>ndings limit knowledge creation [2], developing a clear understanding of the boundaries of the effects of reputation pro<sup>fi</sup>le is important if sellers are to manage the information they provide effectively [21]. For example, the pragmatic question remains of whether sellers can, and should, leverage information alternatives that are under their direct control to in<sup>fl</sup>uence the effect of reputation pro<sup>fi</sup>le on price premiums. For sellers with a damaged reputation, leveraging information alternatives could help persuade reluctant buyers to transact with them, increasing the likelihood of sales and making it possible to restore reputation pro<sup>fi</sup>les more quickly. For reputable sellers, information alternatives may enhance positive reputation effects to increase price premiums. Thus, to tease out the underlying dynamics of these relationships, this study examines the following research question: In online auctions, what information alternatives are open to sellers to compensate for a poor reputation profile or to boost a good reputation profile?

The value in this work is in developing a more nuanced understanding of the relationships between customer-based reputation pro<sup>fi</sup>le and seller-provided information alternatives in online auctions. We begin by reviewing the online auction literature on information alternatives to reputation pro<sup>fi</sup>le in online auctions. Next, we frame our arguments by contrasting oftused economic theories of rational choice (e.g., utility theory) with more contemporary perspectives. Previous information system (IS) research has drawn on economic theories of rational choice to predict the direct effects of information alternatives on <sup>fi</sup>nal sales prices. Under classical assumptions for example, that rational buyers have perfect information and unlimited computational capacity [61]—information alternatives would be expected to compensate for negative feedback and add to the effects of positive feedback on price premiums. However, some argue that due to bounded rationality, classical assumptions do not adequately explain buyer behavior in practice [6,13]. Contemporary perspectives suggest that negative and positive feedback may interact with information alternatives in unexpected ways to in<sup>fl</sup>uence buyers willingness to pay more or less for the same product from different sellers [33,44,65]. Although both classical and contemporary perspectives suggest that sellers’ choices with respect to information alternatives can signi<sup>fi</sup>cantly in<sup>fl</sup>uence <sup>fi</sup>nal sales prices, their competing assumptions have not been explicitly modeled or empirically examined. Because moderation hypotheses are relatively complex and, thus, entail a relatively high risk of error in reasoning, testing competing moderation hypotheses may help

Table 2  
Information Alternatives to Reputation Pro<sup>fi</sup>le Found in Previous Studies.

<table><tr><td>Source</td><td>Information Examined</td><td>Findings</td></tr><tr><td>Bajari and Hortaçsu [3]</td><td>Detailed item descriptions and photos of items being auctioned</td><td>No empirical test. Describes eBay sellers&#x27; effort to post detailed descriptions and photos of items being auctioned</td></tr><tr><td>Kauffman and Wood [36]</td><td>Photos and textual item description</td><td>Photos and description length lead to higher utility for buyers</td></tr><tr><td>Vishwanath [69]</td><td>Photos, initial price, reserve price icon, and textual item description</td><td>Multimedia information (i.e., text, photos, and reserve price icon), initial prices, and photos influence final sales price</td></tr><tr><td>Eaton [19]</td><td>Photos</td><td>Number of stock photos increases final sales price for sellers with negative feedback</td></tr><tr><td>Stern and Stafford [63]</td><td>Photos and number of bids</td><td>Number of stock photos influences number of bids and higher winning bid</td></tr><tr><td>Bland et al. [7]</td><td>Photo of an actual item versus stock photos, starting bid</td><td>The use of photo of an item versus stock photos and starting bid influence final sales prices</td></tr><tr><td>Hou [30]</td><td>Photos</td><td>Number of stock photos positively influenced end price in eBay (China) auctions</td></tr><tr><td>Gregg and Walczak [24]</td><td>e-image (information quality, presentation, and customer service policies)</td><td>e-image positively influences final sales prices</td></tr><tr><td>van Heijst et al. [68]</td><td>Textual item description</td><td>Textual item description influences end price</td></tr><tr><td>Gonzalez et al. [23]</td><td>Item description in terms of keyword usage</td><td>Keywords contained in item descriptions influence end price</td></tr><tr><td>Highfill and O&#x27;Brien [27]</td><td>Photo of an actual item versus stock photos</td><td>Photo of an item significantly increases final sales price; however, stock photo has no effect</td></tr></table>

Please cite this article in press as: M. Carter, et al., When do I pro<sup>fi</sup>t? Uncovering boundary conditions on reputation effects in online auctions, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.06.007

M. Carter et al. / Information & Management xxx (2016) xxx–xxx

minimize errors in judgment. In addition, this approach sheds light on which set of assumptions best explains buyer behavior in online auctions.

To evaluate the relative utility of economic theories of rational choice and contemporary perspectives on buyer decision-making, we develop competing hypotheses of how seller-provided information in auction listings will interact with customer-based positive and negative feedback ratings to exert in<sup>fl</sup>uences on price premium. Afterwards, we empirically test the hypothesized relationships in the context of new, electronic products. The paper concludes with a discussion of results, limitations, and implications for research and practice.

This study contributes to IS research on online auctions by helping resolve ambiguities found in past works that have historically examined reputation effects in isolation. By specifying information alternatives as boundary conditions on reputation effects, this study helps lay the foundations for enhancing sellers ability to manage information under their control effectively.

## 2. Literature review

Researchers studying online auctions have found that how a product is presented for sale may be a more important predictor of online buyers’ purchase intentions than the actual product being sold [24,40,64]. To this end, many online auction studies emphasize the signi<sup>fi</sup>cance of how different types of information contained in auction listings in<sup>fl</sup>uence buyers’ willingness to pay more for the same product (presented in Table 2). More speci<sup>fi</sup>cally, textual descriptions based on standardized information provide more complete information about product features [16,36,68]; stock photos attract buyers’ attention and communicate superior visual information of the same [63,69]. Conversely, customized textual descriptions, which are seller speci<sup>fi</sup>c, may serve to reduce buyer uncertainty about completing the transaction itself [36].

In general, past research provides evidence that these information alternatives are in<sup>fl</sup>uential in generating price premiums. However, while many researchers studying information alternatives have included reputation in their research models (e.g., [19,30,36,68], few have explored interactions between reputation profile and information alternatives. An exception is Eaton [19], who did not posit but found a signi<sup>fi</sup>cant interaction between any negative feedback (represented by a dummy variable) and number of stock photos. No interactions between positive feedback and other information were hypothesized or tested.

In addition, despite a wealth of online auction literature, relationships between reputation and information alternatives have yet to be examined in suf<sup>fi</sup>cient detail to provide actionable guidelines for effective information management in online auctions. This study adds to the online auction literature by explicitly hypothesizing that the effects of positive and negative feedback ratings in a seller’s reputation pro<sup>fi</sup>le depend on information alternatives that are directly under a seller’s control.

## 3. Theory and hypotheses

## 3.1. The separate influences of information alternatives on price premium

Classical economic theories of rational choice, such as utility theory [70], represent one approach to understanding buyer decision-making in online auctions. Utility theory suggests that rational buyers are motivated to maximize their expected utility (i.e., satisfaction) in making a choice over a set of available alternatives [4,44]. The total utility that a buyer expects to gain from purchasing an item from a speci<sup>fi</sup>c seller is revealed in its <sup>fi</sup>nal sales price [43].

Utility theory has been applied in online auction studies to examine how information about an item for sale and about a seller contributes to <sup>fi</sup>nal sales prices [31,36]. Previous work starts with the premise that buyers have a general price expectation for owning a given product a priori, which is adjusted based on information encountered in the online auction context [36]. To illustrate, suppose a buyer visits an online auction with the intention of bidding on an Apple<sup>1</sup> iPad. It is probable, based on previous information, that the buyer has some knowledge of general product characteristics and how much an iPad usually sells for. Considering that online auctions are inherently more risky trading environments [13], the buyer will likely have some price in mind that she/he is willing to pay to assume the risk of purchasing an iPad in that setting (e.g., \$400). Still, in the process of making a purchase decision, a buyer’s willingness to pay more or less than his/her general price expectation may be in<sup>fl</sup>uenced by additional pieces of information contained in an auction listing, which she/he integrates to arrive at an overall utility for completing a given transaction with a speci<sup>fi</sup>c seller [6,36].

An important underlying assumption of classical perspectives is that buyers have perfect information about what outcomes will occur, together with the computational capacity necessary to assign probabilities and perform preference ordering for a full set of alternatives [6,61]. For example, faced with a set of 350 available new iPads, classical perspectives assume that, for each iPad in the set, rational buyers have all the information necessary (about each auction listing and seller) to accurately assign a probability of the product being misrepresented, as well as the likelihood of receiving what is expected in an appropriate time frame. Armed with perfect information and unlimited computational capacity, the total effects of reputation pro<sup>fi</sup>le and information alternatives on <sup>fi</sup>nal sales prices in online auctions are assumed to equal the sum of their separate effects. These information alternatives to reputation pro<sup>fi</sup>le, based on our review, may be classi<sup>fi</sup>ed into standardized and customized information types. Standardized information is equally available (albeit not equally used) by all sellers, whereas customized information is seller speci<sup>fi</sup>c, as elaborated upon below.

## 3.2. Standardized information

Classical perspectives suggest that providing more complete information about a product’s attributes creates buyer utility, which should positively in<sup>fl</sup>uence <sup>fi</sup>nal sales prices [36]. Even allowing for the possibility that a buyer may have encountered the same information elsewhere, research has found that when information about product attributes is of a “given and appropriate quality level,” it acts as a positive differentiator and elicits “higher willingness to pay” [36,p. 176]. This follows because in online auctions buyers cannot physically inspect the goods they purchase. Thus, providing more complete textual and pictorial information about a product should help maximize decision accuracy, which (all else being equal) should increase the overall value of owning the product to the buyer [6,16,36].

Although IS research has focused mostly on information that reduces uncertainty about a seller [16], our review of the online auction literature reveals two forms of standardized information – standardized textual descriptions and stock Photos – that help sellers extract price premium by maximizing buyers’ decision-making accuracy in online auctions [16,36,63,69]. A standardized textual description offers buyers more complete, and positive, information about product features, technical speci<sup>fi</sup>cations, and compatibility with other devices—for example, “Weighing 1.6 pounds, this cool gadget boasts a storage space of 64GB, battery life of 10 h, and 3 G connectivity.” Although information contained in a standardized description is equally available for use, variation exists in the

Please cite this article in press as: M. Carter, et al., When do I pro<sup>fi</sup>t? Uncovering boundary conditions on reputation effects in online auctions, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.06.007

length of standardized textual descriptions provided by sellers for given products. To that end, past research <sup>fi</sup>nds that longer standardized descriptions are associated with higher sales prices [36,38,69].

Similarly, stock photos, which convey standardized pictorial information, have been found to positively in<sup>fl</sup>uence price premium [30,36,63,69]. Similar to standardized textual descriptions, stock photos provide buyers with more complete, and positive, information about product features [36]. Moreover, as photos convey superior visual information, they have been found to attract a disproportionate amount of buyers’ attention [63,69]. Consequently, stock photos are viewed as an important tool for evoking buyers’ positive inferences toward an auction listing [54,69]. Formally stated,

H1. In online auctions, the length of a standardized textual description will be positively related to price premium.

H2. In online auctions, the number of stock photos will be positively related to price premium.

## 3.3. Customized information

Potential misrepresentation by sellers is a concern for buyers in online auctions [34,46,55]. Thus, in addition to maximizing expected utility (i.e., satisfaction) in making a choice over a set of available alternatives [4,44], buyers are motivated to minimize the potential for experiencing negative consequences (i.e., risk) as a result of completing a transaction with a speci<sup>fi</sup>c seller [6]. Consequently, buyers are sensitive to information that increases or decreases “the probability that the seller will deliver what is expected in a time frame that is stated or assumed” [36,p. 174]. To that end, customized textual descriptions, which are seller speci<sup>fi</sup>c, can be used to minimize buyers’ perceptions of risk in completing a transaction. For example, (in addition to a standardized descriptions) sellers may provide information about an auction item’s condition (e.g., “sealed in box, never been used”), their reason for selling (“received this as a gift, but have not used it”), or their policies (“I don’t ship international;” “Tracking # will be sent to your PayPal email directly”). Because customized textual descriptions increase buyers’ con<sup>fi</sup>dence that they will receive what is expected, all else being equal, these information types should positively in<sup>fl</sup>uence the amount buyers are willing to pay to complete a transaction. Formally stated,

H3. In online auctions, the length of a customized textual description will be positively related to price premium.

3.4. The combined influences of reputation profile and information alternatives

## 3.4.1. Moderation hypotheses under classical assumptions

In addition to their separate in<sup>fl</sup>uences, classical perspectives suggest that information alternatives will moderate the effects of sellers’ reputation pro<sup>fi</sup>les on price premium [44]. Speci<sup>fi</sup>cally, both complete product information (standardized textual descriptions and stock photos) and information that alleviates buyers’ concerns about whether the seller will deliver what is expected (customized textual descriptions) would compensate for disutility created by negative feedback and supplement positive feedback about the seller, thereby weakening the effect of negative feedback and amplifying the effect of positive feedback. This leads to the following set of moderation hypotheses:

H4. Textual descriptions moderate the relationship between negative feedback and price premium such that the longer the description, the weaker the impact of negative feedback on price premium

H5. The number of stock photos moderates the relationship between negative feedback and price premium such that the greater the number of photos provided, the weaker the impact of negative feedback on price premium.

H6. Textual descriptions moderate the relationship between positive feedback and price premium such that the longer the description, the stronger the impact of positive feedback on price premium

H7. The number of stock photos moderates the relationship between positive feedback and price premium such that the greater the number of photos provided, the stronger the impact of positive feedback on price premium.

Classical perspectives provide normative understanding of buyer decision-making. However, researchers have argued that human decisions, which are bounded by imperfect information and limits in information processing capacities, violate classical assumptions of certainty [6,13]. To address that human decisionmaking inherently involves uncertainty, alternative theories such as the prospect theory [33] have been developed. The prospect theory replaces “buyer utility” with “value,” where value is de<sup>fi</sup>ned in terms of deviations (<sup>fi</sup>nancial losses and gains) from some reference point and where, in general, people strongly prefer to avoid losses than to acquire gains (referred to as loss aversion). These contemporary assumptions lead to a competing set of hypotheses about the combined in<sup>fl</sup>uences of sellers’ reputation pro<sup>fi</sup>les and information alternatives.

## 3.4.2. Competing moderation hypotheses under contemporary assumptions

First, buyers’ tendency toward loss aversion sensitizes them to “downside risk” [57]: that is, that the value of what they receive will be less than the expected value. Because information alternatives (textual descriptions and stock photos) help maximize decision accuracy and alleviate buyers’ concerns in an environment where buyers cannot physically inspect the goods they purchase, these types of information elicit higher willingness to pay [36]. When a buyer is willing to pay more for a product, she/he has more to lose if a seller does not deliver what is expected. Thus, an increase in willingness to pay creates a corresponding increase in downside risk involved in a transaction. Now, a buyer has more to lose by disregarding negative feedback about a seller. As loss-averse buyers would rathereliminate downside risk than reduce it [66], this should amplify the effect of negative feedback on price premium.

Second, buyers who are sensitized to downside risk are likely to be highly involved in the decision process. Past research <sup>fi</sup>nds that highly involved buyers assign disproportionate weight to negative information [11,16,42]. Online auctions are characterized by large amounts of information, which must be processed effectively if buyers are to bene<sup>fi</sup>t [38]. However, the tendency to seek out negative information reduces the likelihood of buyers paying attention to positive information [11,42]. As a result, positive feedback becomes underweighted in the decision-making process, suggesting that information alternatives will weaken the impact of positive feedback on the price premium. This leads to the following set of competing moderation hypotheses:

$\mathbf { H 4 _ { a l t } } .$ Textual descriptions moderate the relationship between negative feedback and price premium such that the longer the description, the stronger the impact of negative feedback on price premium

$\mathbf { H } 5 _ { \mathbf { a l t } }$ . The number of stock photos moderates the relationship between negative feedback and price premium such that the greater the number of photos provided, the stronger the impact of negative feedback on price premium.

$\mathbf { H 6 _ { a l t } . }$ Textual descriptions moderate the relationship between positive feedback and price premium such that the longer the description, the weaker the impact of positive feedback on price premium

$\mathbf { H } 7 _ { \mathbf { a l t } } .$ . The number of stock photos moderates the relationship between positive feedback and price premium such that the greater the number of photos provided, the weaker the impact of positive feedback on price premium.

The research model, which includes competing moderation hypotheses under classical and contemporary assumptions, is presented in Fig. 1.

## 4. Research method

Data from a total of 363 completed auctions across 232 sellers are collected between 1 September 2010 and 21 September 2010 from eBay, a leading online marketplace. eBay may be particularly appropriate for studying how buyers integrate multiple pieces of information as the multiplicity of sellers and products it offers makes large amounts of information available to buyers [1,13,55]. Consistent with past research (e.g., [1,15,46,53,55,71], we selected electronic products for data collection, including the Apple<sup>1</sup> iPod Touch, iPod Nano, iPad, and iPhone. Because of their relatively high value and complexity, these products are likely to encourage buyers to take more care in evaluating product and seller attributes [31,50,51], rendering them particularly suitable for this study. The product selection process, including the criteria for product value and complexity, is outlined in Appendix A.

The data collected included information about prices charged, seller attributes, and auction attributes. Data are collected manually to ensure item homogeneity [25] and help maintain full control over the collection process. Following Houser and Wooders [31], data are gathered from closed auctions, allowing us to collect data continuously from all auctions that met our criteria during the collection period. This process ensured that subsequent calculations of price premium re<sup>fl</sup>ected the in<sup>fl</sup>uence of similar, concurrent, auctions [17]. For example, if there were 20 relevant auctions for a particular product on a speci<sup>fi</sup>c day, data from all these auctions are collected.

Auction relevancy was assessed because certain characteristics of an individual auction could render it irrelevant for our study. For example, some auctions offered product enhancements bundled together with the major products (e.g., an iPod case bundled with an iPod). Such heterogeneous packaging makes it dif<sup>fi</sup>cult to trace price differences to variation in study variables as it appears likely that price differences in such auctions are due to enhancing the major item [26]. Others were irrelevant because they ended early via the eBay code “Buy it Now,” which allows a buyer to circumvent the bidding process and purchase the item directly at a posted price. We ensured that only relevant auctions were included in our study. Accordingly, none of the auctions selling product bundles or ending early via the eBay code “Buy it Now” was included in our study. In other words, the percentage of such auctions included in our study was 0%.

Measures were mapped to construct de<sup>fi</sup>nitions and calculated in ways that were consistent with past research. Price premium was a standardized measure that was calculated by <sup>fi</sup>rst subtracting the mean price of each product from each item’s <sup>fi</sup>nal auction price and by, then, dividing the resulting difference by the product

![](/api/attachments/4YU34XHQ/fulltext/images/3c1b5e55b4b374e0ab85dbbd007339e87d901016788c8936bb2c041e1442c5cf.jpg)  
Fig. 1. Research Model.

Please cite this article in press as: M. Carter, et al., When do I pro<sup>fi</sup>t? Uncovering boundary conditions on reputation effects in online auctions, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.06.007

mean price [1,55]. Hence, each item’s price premium was normalized by the product mean price. This calculation of price premium was consistent with previous research, indicating, “the dependent variable was the price premium developed by subtracting the mean price from the <sup>fi</sup>nal price of each product divided by its mean price” [1,p. 257].

Consistent with previous research, seller reputation was measured as the numbers of positive and negative feedback ratings, respectively [1,3,31]. One might argue that, rather than considering the numbers of negative and positive reviews for a given seller in isolation, online buyers arrive at an integrated, holistic interpretation of a seller’s reputation based on both kinds of feedback, recency of reviews, and other individual comments. Yet, we think that measuring them in isolation is advantageous. First, consistency with previous research helps build cumulative understanding of the research phenomenon under study. Second, creating separate construct measures offers a more detailed understanding of what aspects of seller reputation interact with what kinds of information alternatives. Third, under contemporary assumptions, people strongly prefer to avoid losses than to acquire gains, suggesting that negative and positive feedback interact differently with information alternatives to in<sup>fl</sup>uence price premium. For instance, the interaction of information alternatives with negative feedback may be highly in<sup>fl</sup>uential, while the interaction of information alternatives with positive feedback may generally be irrelevant or vice versa. Thus, in order to test hypotheses under classical and competing assumptions, it was necessary to operationalize positive and negative feedback as separate constructs.

Stock photos were assessed, consistent with past research, based on the number contained in an auction listing [36,52,68]. Standardized description was assessed in terms of the number of characters found in the “Detailed item info” section on the main auction page, and customized textual description was measured as the number of characters provided by the seller in addition to this information [36,68]. The measures for standardized and customized descriptions were adapted from the online review literature, which was relevant here in that online reviews describe products and the context in which they are being delivered. Contributions to this literature include recent works (e.g., [76,77,78] and others), which have appeared in major IS journals such as MIS Quarterly and Journal of the Association for Information Systems. These works, which operationalized review length and depth through number of words, indicate that because longer reviews provide more comprehensive information, they are more helpful than shorter ones. Still, quantitatively speaking, the amount of information a buyer sees for the same number of words can be different, depending on word length. Thus, this study uses number of characters instead of number of words to further increase the accuracy of our measures.

To provide meaningful interpretation, stock photos, standardized descriptions, and customized descriptions were normalized in the same way as price premium. To illustrate, the stock photo variable was calculated by <sup>fi</sup>rst subtracting the mean number of stock photos for each product from the number of stock photos on an item’s auction page and, then, dividing the resulting difference by the mean number of stock photos for a product. We followed the same procedure for developing variables for standardized and customized descriptions. The normalization procedure enabled us to conduct rigorous analyses despite the different distributions associated with the different variables [12].

Following previous research, we controlled for several alterna tive explanations for variation in price premium, including the starting bid of an auction [14,22,62], weekend closure (i.e., whether an auction ended on a weekend; [14,45,62], auction duration in days [22,45,62], number of bids [62], and buyer experience [3,35,55]. Furthermore, we controlled for the use of gallery photo upgrades because such forms of advertising can obscure results. Following Grover et al. [25], we supplemented these explicit controls with implicit controls pertaining to the research setting. Speci<sup>fi</sup>cally, we controlled for product heterogeneity and time, as well as market factors, by gathering the data manually and ensuring that all product-related information in one setting was collected.

Table 3  
HLM Results (N = 363 auctions nested within J = 262 sellers).

<table><tr><td></td><td>Variable</td><td>Proportion Variance Explained $^b$ </td><td>Unstandardized Coefficient</td><td>Standard Error</td><td>t</td><td>Significance</td></tr><tr><td>Null Model</td><td>Intercept</td><td>-</td><td>-0.016028</td><td>0.007301</td><td>-2.195</td><td>0.029</td></tr><tr><td rowspan="6">Independent Variables</td><td>Intercept</td><td>n.s.</td><td>-0.016364</td><td>0.009518</td><td>-1.719</td><td>0.087</td></tr><tr><td>Positive Feedback</td><td>5.3%</td><td>0.020004</td><td>0.004637</td><td>4.314</td><td>0.000</td></tr><tr><td>Negative Feedback</td><td>3.1%</td><td>-0.041205</td><td>0.013927</td><td>-2.959</td><td>0.003</td></tr><tr><td>Standardized Description</td><td>4.2%</td><td>0.071433</td><td>0.022894</td><td>3.120</td><td>0.002</td></tr><tr><td>Customized Description</td><td>1.2%</td><td>0.022691</td><td>0.007653</td><td>2.965</td><td>0.003</td></tr><tr><td>Number of stock photos</td><td>1.0%</td><td>0.007023</td><td>0.003171</td><td>2.215</td><td>0.027</td></tr><tr><td rowspan="7">Controls</td><td>Starting Bid</td><td>1.1%</td><td>0.012048</td><td>0.005516</td><td>2.184</td><td>0.029</td></tr><tr><td>Gallery Photo</td><td>2.0%</td><td>-0.043803</td><td>0.019185</td><td>-2.283</td><td>0.023</td></tr><tr><td>Buyer Experience</td><td>n.s.</td><td>0.000003</td><td>0.000013</td><td>0.224</td><td>0.823</td></tr><tr><td>Number of Bids</td><td>n.s.</td><td>0.000873</td><td>0.000646</td><td>1.352</td><td>0.177</td></tr><tr><td>Length</td><td>n.s.</td><td>0.002073</td><td>0.002530</td><td>0.819</td><td>0.413</td></tr><tr><td>Weekend</td><td>n.s.</td><td>0.006270</td><td>0.010917</td><td>0.574</td><td>0.566</td></tr><tr><td>Number of Unique Bidders</td><td>n.s.</td><td>-0.001225</td><td>0.001607</td><td>-0.762</td><td>0.446</td></tr><tr><td rowspan="7">Linear Interactions</td><td>Negative Feedback * Standardized Description</td><td>3.1%</td><td>0.075227</td><td>0.030338</td><td>2.480</td><td>0.014</td></tr><tr><td>Positive Feedback * Standardized Description</td><td>n.s.</td><td>-0.003430</td><td>0.008389</td><td>-0.409</td><td>0.683</td></tr><tr><td>Negative Feedback * Customized Description</td><td>n.s.</td><td>-0.008537</td><td>0.013552</td><td>-0.630</td><td>0.529</td></tr><tr><td>Positive Feedback * Customized Description</td><td>1.0%</td><td>0.011025</td><td>0.004438</td><td>2.485</td><td>0.013</td></tr><tr><td>Negative Feedback * Number of stock photos</td><td>4.1%</td><td>0.013728</td><td>0.004964</td><td>2.766</td><td>0.006</td></tr><tr><td>Positive. Feedback * Number of stock photos</td><td>3.1%</td><td>-0.004779</td><td>0.001797</td><td>-2.659</td><td>0.008</td></tr><tr><td>Total Proportion Variance Explained $^a$ </td><td></td><td></td><td>30%</td><td></td><td></td></tr></table>

<sup>a</sup> Pseudo R<sup>2</sup>, calculated as t (intercept-only model) t (full model)/t (intercept-only model; see Ref. [9].  
<sup>b</sup> Pseudo SR<sup>2</sup>, calculated as total proportion variance explained (full model)—total proportion variance explained (model with predictor excluded).

M. Carter et al. / Information & Management xxx (2016) xxx–xxx

## 5. Analysis and results

Because individual auctions in our sample were nested within online sellers (i.e., N = 363 auctions at level 1 across J = 232 sellers at level 2), potentially they were not independent, resulting in correlated residuals. Misestimating standard errors can lead to erroneous conclusions when dependency of observations is not accounted for [12]. Accordingly, to adequately align the analytical model with the data, hierarchical linear modeling (HLM) was used to test the effects of predictors (all at the group level) on the individual-level-dependent variable (price premium) in a meansas-outcomes (<sup>fi</sup>xed effects) model [28]. HLM makes it possible to test hypotheses between two levels of analysis and partition explained variances from each level [9]. Consequently, group-level in<sup>fl</sup>uence on individual-level outcomes can be evaluated without biasing the estimation of the predictors [28,9].

As a <sup>fi</sup>rst step in our analysis, we used intraclass correlation (ICC) to assess the degree of clustering among the data points. ICC is the ratio of between seller variance to between seller variance plus within seller variance, where an ICC of one indicates that the value of the data points is completely dependent on the seller [12]. In the intercept-only model (i.e., null model), the ICC was 0.732, indicating that 73.2% of variance in price premium depended on sellers and 26.8% of variance in price premium occurred within sellers. As ordinary least square (OLS) regression analysis assumes an ICC of zero, an ICC of 0.732 clearly indicated that HLM should be

Summary of Hypotheses and Results.

<table><tr><td colspan="4">CLASSICAL ASSUMPTIONS</td></tr><tr><td colspan="4">1. Buyers are rational beings who attempt to derive the greatest utility (value) from their purchases.2. Buyers have perfect information about what outcomes will occur as a result of making a choice.3. Buyers have the computational capacity to accurately assign probabilities and perform preference ordering for a set of alternatives.</td></tr><tr><td>Information Cues</td><td>Theoretical Logic under Classical Assumptions</td><td>Hypotheses under Classical Assumptions</td><td>Results</td></tr><tr><td>Standardized textual description</td><td>Providing more complete product information helps maximize decision accuracy, increasing buyer utility, and eliciting higher “willingness to pay” [6,36]</td><td>H1: The length of a standardized textual description will be positively related to price premium.</td><td>Supported**</td></tr><tr><td>Stock photos</td><td></td><td>H2: The number of stock photos will be positively related to price premium.</td><td>Supported*</td></tr><tr><td>Customized textual description</td><td>Information that alleviates buyers’ concerns about whether the seller will deliver what is expected decreases perceptions of risk in completing a transaction with a specific seller and positively influences willingness to pay [36].</td><td>H3: The length of a customized textual description will be positively related to price premium.</td><td>Supported**</td></tr><tr><td>Textual descriptions and negative feedback</td><td>Buyer utility created by more complete information about the product and the seller compensates for disutility created by negative feedback, thereby weakening the effect of negative feedback on price premium.</td><td>H4: Textual descriptions moderate the relationship between negative feedback and price premium such that the longer the description, the weaker the impact of negative feedback on price premium</td><td>Supported for standardized descriptions*</td></tr><tr><td>Stock photos and negative feedback</td><td></td><td>H5: The number of stock photos moderates the relationship between negative feedback and price premium such that the greater the number of photos provided, the weaker the impact of negative feedback on price premium</td><td>Supported**</td></tr><tr><td>Textual descriptions and positive feedback</td><td>Buyer utility created by more complete information about the product and seller supplements utility created by positive feedback, thereby amplifying the effect of positive feedback on price premium.</td><td>H6: Textual descriptions moderate the relationship between positive feedback and price premium such that the longer the description, the stronger the impact of positive feedback on price premium</td><td>Supported for customized descriptions*</td></tr><tr><td>Stock photos and positive feedback</td><td></td><td>H7: The number of stock photos moderates the relationship between positive feedback and price premium such that the greater the number of photos provided, the stronger the impact of positive feedback on price premium</td><td>Not supported</td></tr><tr><td colspan="4">CONTEMPORARY ASSUMPTIONS</td></tr><tr><td colspan="4">1. Buyers’ decisions are boundedly rational—approximations bounded by imperfect information and limits in processing capacity2. In risky situations, boundedly rational buyers are loss averse—that is, they prefer to avoid losses than to acquire gains.3. Loss-averse buyers often rely on heuristics or simple decision rules when making decisions under uncertainty.</td></tr><tr><td>Information Cues</td><td>Theoretical Logic under Contemporary Assumptions</td><td>Competing Moderation Hypotheses under Contemporary Assumptions</td><td>Results</td></tr><tr><td>Textual descriptions and negative feedback</td><td>Increased downside risk means buyers have more to lose by disregarding negative feedback. Because loss-averse buyers would rather eliminate downside risk than reduce it, this should amplify the effect of negative feedback on price premium.</td><td>H4alt: Textual descriptions moderate the relationship between negative feedback and price premium such that the longer the description, the stronger the impact of negative feedback on price premium</td><td>Not supported</td></tr><tr><td>Stock photos and negative feedback</td><td></td><td>H5alt: The number of stock photos moderates the relationship between negative feedback and price premium such that the greater the number of photos provided, the stronger the impact of negative feedback on price premium</td><td>Not supported</td></tr><tr><td>Textual descriptions and positive feedback</td><td>Highly involved buyers pay less attention to positive information about the seller in the decision-making process, reducing the effects of positive feedback on final sales prices.</td><td>H6alt: Textual descriptions moderate the relationship between positive feedback and price premium such that the longer the description, the weaker the impact of positive feedback on price premium</td><td>Not supported</td></tr><tr><td>Stock photos and positive feedback</td><td></td><td>H7alt: The number of stock photos moderates the relationship between positive feedback and price premium such that the greater the number of photos provided, the weaker the impact of positive feedback on price premium</td><td>Supported**</td></tr></table>

<sup>\*</sup>Signi<sup>fi</sup>cant at p < 0.05; \*\* Signi<sup>fi</sup>cant at p < 0.01

M. Carter et al. / Information & Management xxx (2016) xxx–xxx

used to arrive at valid conclusions [12]. However, as our focus was on avoiding misleading conclusions due to correlated residuals rather than on analytical <sup>fl</sup>exibility, a <sup>fi</sup>xed-effects-only HLM model was appropriate—that is, only group-level variables (that varied between sellers) were included as predictors [9]. Analysis was conducted using SPSS version 19 with restricted maximum likelihood (REML) estimation. REML was preferred to maximum likelihood (ML) estimation because this technique takes into account uncertainty in the <sup>fi</sup>xed effects. Following [29], we centered our variables by the grand mean in all analyses. Our <sup>fi</sup>ndings are presented in Table 3, with the unique (i.e., separate) effect sizes for all predictors detailed in Column 1. These effect sizes show the variance explained by each predictor over and above the null model.

H1, H2, and H3 predicted that standardized information (in the form of standardized textual descriptions and stock photos, respectively) and customized textual descriptions would be positively related to price premium. As results show, these hypotheses were supported (H1: $p { = } 0 . 0 0 2 ,$ , estimate = 0.071; H2: $p { = } 0 . 0 2 7 ,$ , estimate = 0.007; and H3: $p { = } 0 . 0 0 3$ , estimate = 0.023). H4 and H5 (classical assumptions) predicted that textual descriptions and stock photos would interact positively with negative feedback in the prediction of price premium, while $\mathrm { H } 4 _ { \mathrm { a l t } }$ and $\mathrm { H } 5 _ { \mathrm { a l t } }$ (contemporary assumptions) predicted negative interaction effects. For standardized information, the interaction terms (negative feedback \* standardized description and negative feedback \* number of stock photos) were signi<sup>fi</sup>cant and positive $( p = 0 . 0 1 4 ,$ , estimate = 0.075 and $p { = } 0 . 0 0 6$ , estimate = 0.014, respectively). The interaction between negative feedback and customized information was not signi<sup>fi</sup>cant. These <sup>fi</sup>ndings support classical assumptions that buyer utility resulting from increased decision accuracy mitigates the effects of negative feedback on price premium. However, information aimed at alleviating buyers’ concerns about whether a seller will deliver what is expected does not appear to reduce buyers’ perceptions of risk involved in completing a transaction with a speci<sup>fi</sup>c seller.

H6 and H7 (classical assumptions) predicted that textual descriptions and stock photos would interact positively with positive feedback in the prediction of price premium. H6 was supported for customized but not standardized textual descriptions. The interaction term of positive feedback \* customized description was signi<sup>fi</sup>cant (p = 0.013) and positive (estimate = 0.011) suggesting that, while customized information does not compensate for negative feedback, sellers with good reputations may pro<sup>fi</sup>t from providing additional customized information to reinforce customer-based positive feedback. H7 was not supported. The interaction term for positive feedback \* number of stock photos was signi<sup>fi</sup>cant $\left( { p = 0 . 0 0 8 } \right)$ and negative (estimate = $_ { - 0 . 0 0 5 ) }$ , providing support for hypothesis $\mathrm { H } 7 _ { \mathrm { a l t } }$ (contemporary assumptions). These <sup>fi</sup>ndings provide mixed evidence of the in<sup>fl</sup>uence of standardized information on the relationship between positive feedback and price premium. However, they support the view that photos, which are more vivid than text, attract more processing than textual descriptions [63,69]. $\mathrm { H } 4 _ { \mathrm { a l t } } , \mathrm { H } 5 _ { \mathrm { a l t } } ,$ and $\mathrm { H } 6 _ { \mathrm { a l t } }$ (contemporary assumptions) were not supported. Table 4 presents a summary of hypotheses and results.

## 6. Implications for research and practice

Our results con<sup>fi</sup>rm the linear effects, and most of the interaction effects, predicted by classical theories of economic choice [31,36]. In explicitly modeling and testing the competing assumptions of classical and contemporary approaches, this study extends past work by yielding a more nuanced understanding of factors that bound the value of reputation in online auctions (see Fig. 2). Such understanding is necessary for sellers to manage the information they provide to buyers effectively [13,21].

Consistent with classical assumptions, this research shows that standardized information mitigates the effects of negative feedback on price premium, while customized information ampli<sup>fi</sup>es the effects of positive feedback (see Fig. 3). Thus, our results help auction research progress from investigating the general association between reputation and price premiums to more detailed and speci<sup>fi</sup>c explanations of when, or under what conditions, reputation matters. Speci<sup>fi</sup>cally, the results shed light on the boundary conditions, or contextual factors, on which the effectiveness of seller reputation depends.

As specifying boundary conditions is critical for theory development and testing to shed light on the context in which main effect models exist and operate [2,12], this study offers important directions for future research. Speci<sup>fi</sup>cally, to further contextualize reputation effects and extend understanding of their applicability, future research could take the following three interrelated directions: (i) developing a comprehensive taxonomy of the informational resources that bound reputation effects, (ii) developing an understanding of how and why these resources act as boundaries, and (iii) applying more complex HLM models to deepen understanding of how sellers strategize.

Although this research demonstrates that standardized textual descriptions, stock photos, and customized textual descriptions are

![](/api/attachments/4YU34XHQ/fulltext/images/12f9ae0a9bb475f54e50c632598ac7b3781018d4a481bfc46b4bdee531be7b40.jpg)  
Fig. 2. General Value Added of this Research: Specifying Boundary Conditions on Reputation Effects.

Please cite this article in press as: M. Carter, et al., When do I pro<sup>fi</sup>t? Uncovering boundary conditions on reputation effects in online auctions, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.06.007

![](/api/attachments/4YU34XHQ/fulltext/images/0dfed92a3cdb703444bb8fb57e9d2200d90c44d2efb57438b2c76344373c2664.jpg)  
Fig. 3. Speci<sup>fi</sup>c Value Added of this Research: Clarifying Previous Con<sup>fl</sup>icting Findings.

contextual factors that create a boundary around reputation effects, limiting their applicability, future research could develop a comprehensive taxonomy of informational boundary conditions. For instance, future work could examine the in<sup>fl</sup>uence of such sellerrelated information types as customer endorsements, third-party seals, or seller policies as complementary boundaries. These informational resources are similar to customized descriptions, in that they reduce perceptions of risk in completing a transaction. As an example, policies relating to product and/or service quality serve as risk reduction mechanisms because they provide assurances that a seller will meet certain contractual obligations [56]. Although, in this study, such assurances did not mitigate the effects of negative feedback, a lack of explicitly stated policies may prevent sellers from fully leveraging good reputations.

In addition, while sellers can use stock photos made available by the manufacturer to provide buyers with more complete information about product features [63,69], they could choose to supply photos of the actual item being auctioned. Such photos could demonstrate the item’s actual condition and reassure buyers that the item is, in fact, in good condition [7]. Furthermore, such photos would demonstrate that the item (as described) is, in fact, in the seller’s possession to sell. This way, photos of the actual item for sale could minimize buyers’ perceptions of risk in completing a transaction with a given seller [55].

Future research may examine to what extent photos of the actual item for sale interact with positive (and negative) feedback to in<sup>fl</sup>uence price premium. As a photo of the actual item for sale could reinforce the information cues in positive feedback by demonstrating t The measures for standardized and customized [A1] hat the item actually exists (and in the condition described), one could expect such photos to strengthen the effects of positive feedback on price premium. This leads us to advance the Actual Photo Proposition, namely providing a photo of the actual item for sale strengthens the relationship between positive feedback and price premium.

## 6.1. Exploring how and why certain conditions act as boundaries

This research found that standardized and customized information bound the applicability of reputation effects, clarifying when reputation is important. Further insight could result from explaining how and why these information alternatives act as boundaries on seller reputation. For example, future research could explore whether the bounding impact of a customized textual description is mediated by buyer engagement such that the provision of more or richer description increases engagement. In this case, buyer engagement helps explain how and why customized information acts as a boundary on reputation effects.

## 6.2. Use of more complex HLM models in online auction research

In this research, a <sup>fi</sup>xed-effects-only HLM model was appropriate because our primary interest was in evaluating the effects of a limited number of seller-provided information alternatives (that did not vary within sellers) and HLM was used to account for potentially correlated residuals. Still, future research could examine within-seller variation concerning, for example, auction length or advertisement, to provide for a more detailed understanding of how auction sellers strategize, describing the factors

M. Carter et al. / Information & Management xxx (2016) xxx–xxx

that motivate behavioral change within a single seller. By examining within-seller variation, future research could show what makes individual sellers rely more strongly on strategies that effectively combine with reputation effects. In this vein, as we have shown that outcomes in individual auctions are largely dependent on sellers and because OLS regression assumes independence of observations, we also recommend that future research examines the degree of nesting within the data to choose the appropriate analytic technique to result in accurate conclusions [12].

This study also yields important implications for seller information management and the online auction markets sellers rely on. We found that standardized textual descriptions and stock photos compensate for negative feedback, stock photos weaken the effect of positive feedback, and customized descriptions supplement the effect of positive feedback. Based on these results, sellers with poor reputation may bene<sup>fi</sup>t from providing as complete product information as possible. Established sellers, however, should focus on providing customized information to bene<sup>fi</sup>t from the mutually reinforcing relationship between this type of information and positive feedback. On the contrary, the <sup>fi</sup>ndings for stock photos suggest that established sellers carefully assess the level of their investments in these information types.

This study’s results also suggest that online auction marketplaces may bene<sup>fi</sup>t from examining in more detail the effectiveness of their reputation systems. One promising avenue for auction marketplaces to further leverage reputation systems is for them to encourage sellers to use additional types of information that complement reputation effects. In doing so, online auctions could increase differential leverage of reputation systems to reward better sellers with price premiums and, in turn, enhance success.

## 7. Limitations

Study limitations should be acknowledged. First, as our sample was limited to 363 completed auctions, a Type II error was more likely to occur than in a larger sample, which could have been obtained through the use of a computerized data collection program. However, consistent with previous research, we decided to collect our data manually to maintain full control over the data collection process Gonzales et al., 2009, ensuring that only fully homogeneous items were included in the analysis. This strategy reduced measurement error in our data, enabling us to more accurately test the competing hypotheses of classical and contemporary approaches and allowing us to conclude that sample size played an insigni<sup>fi</sup>cant role. Still, future research could use a larger sample size to nullify the risk of producing a Type II error from the outset.

Second, because we chose to test our model using new electronic products, our <sup>fi</sup>ndings apply to new, relatively high value, and complex products only. Future research should seek to determine if the <sup>fi</sup>ndings presented here (particularly relating to the use of stock photos and standardized descriptions) are generalizable to used, low-value, and/or low-quality products. Third, only a few information alternatives were examined, yielding opportunities for future research to build on this work. Fourth, stock photos might not always be fully standardized. They might differ in terms of photo quality, style, color, and aesthetic characteristics. However, stock photos generally have more features in common than features that differentiate them. For this reason, we have classi<sup>fi</sup>ed them as standardized in this particular study. Fifth, this study focused on auction-related information rather than buyer characteristics. To enrich the insight from this study, future research could include the buyer’s riskrelated characteristics such as risk aversion.

Furthermore, our measurement of standardized and customized description as the number of characters might have limited our ability to gain rich, qualitative insight into these concepts. For example, some descriptions might be more informative or persuasive than others even if the numbers of characters are the same. We focused on precise, quantitative measures of these concepts to be consistent with the literature on seller reputation, which has often operationalized reputation in a precise, quantitative way as the number of positive or negative feedback. We deemed this approach necessary as we were examining information alternatives to reputation pro<sup>fi</sup>le, and we endeavored to operationalize all constructs consistently and coherently. However, future research should consider alternative measures of standardized and customized descriptions to account for situations in which some might be more informative or persuasive than others even if the numbers of characters are the same. Over time, such research could help us reach a more holistic understanding of the role of information alternatives.

Finally, one might argue that the prices of the products included in our data collection process might be constrained by manufacturing costs, thereby limiting the study of price premium.<sup>1</sup> To maximize the relevancy of the products included in our study for our study objectives, we implemented different strategies in our research design. First, consistent with Nelson [49,50], we decided to collect data on electronic products because electronics are relatively complex than, for example, books. Thus, buyers cannot as easily evaluate them before purchase so that online product information about them is relatively important. As a result, electronics might prompt more variation in price premium than, for example, books. Second, we selected the products for data collection to be consistent with previous research on price premium (e.g., [1]), allowing for a cumulative research tradition to emerge. Third, we selected the products based on their relevance for online marketplaces in terms of sales volume. Finally, and perhaps most importantly, as we found signi<sup>fi</sup>cant reputation and interaction effects, despite the potential price range limitations associated with electronic products, there is reason to believe that our <sup>fi</sup>ndings may hold true (and even more so) for products that exceed the complexity and experiential requirements of electronics. Despite the consideration of these aspects in our product selection, we wish to clarify that collecting data on electronic products might limit the generalizability of our study to products that are similarly complex and experiential in nature. Future research could examine to what extent our results are applicable to other kinds of products.

## 8. Conclusion

Past online auction research has advanced understanding of whether reputation can yield price premiums but has not examined the boundaries of this important relationship, resulting in con<sup>fl</sup>icting <sup>fi</sup>ndings and the need to improve knowledge in this area. Although classical perspectives on economic choice have contributed signi<sup>fi</sup>cantly to predicting separate in<sup>fl</sup>uences of reputation, classical and contemporary assumptions lead to competing moderation hypotheses about the combined effects of information alternatives and reputation on <sup>fi</sup>nal sales prices. By explicitly modeling and testing these competing hypotheses, this study provides a more nuanced understanding of the boundary conditions on reputation effects, helping online auction market research progress toward more detailed and speci<sup>fi</sup>c explanations of when reputation matters. Our <sup>fi</sup>ndings imply that online auction research is not yet saturated but that clearer guidance can and should be provided to practitioners in the increasingly important online auction environment.

M. Carter et al. / Information & Management xxx (2016) xxx–xxx

Appendix A. Selecting products for data collection

![](/api/attachments/4YU34XHQ/fulltext/images/c4bb8d744ce684e09c050937e9eacba61627f81686083e12adff685f70de10c7.jpg)

To determine a minimum level for product value, we drew on previous studies. Although past work found strongly signi<sup>fi</sup>cant relationships between seller reputation and price premiums for products with average prices in the triple digits, only marginally signi<sup>fi</sup>cant relationships were found for products with average prices in the single digits (e.g., [1,31]. This <sup>fi</sup>nding suggests that seller reputation and other information may matter less to buyers in the case of prices in the single and double digits than prices in the triple digits. It also indicates that product value may need to exceed a minimum threshold for the statistical analysis to yield unbiased results. Hence, we included only products in our analysis that yielded a minimum average auction price of 100 US dollars.

Concerning product complexity, products can be classi<sup>fi</sup>ed into two categories: experience goods (e.g., electronics and computer products) and search goods (e.g., books; [49]; 1974). Search goods are less complex, implying that product information about them provides buyers with an online shopping experience comparable to the physical examination of goods in brick-and-mortar stores. By contrast, experience goods are more complex so that buyers cannot easily evaluate them before purchase. To align the product selection process with the objectives of this study, we focused on experience goods. More speci<sup>fi</sup>cally, following examples from past research (e.g., [1]), we selected products from electronics and computer categories—for example, the Apple iPad with 64 gigabytes of disk space. Each product was identi<sup>fi</sup>ed through a unique identi<sup>fi</sup>cation code.

## References

[1] S. Ba, P.A. Pavlou, Evidence of the effect of trust building technology in electronic markets: price premiums and buyer behavior, MIS Q. 26 (3) (2002) 243–268.

[2] S.B. Bacharach, Organizational theories: some criteria for evaluation, Acad. Manage. Rev. 14 (4) (1989) 496–515.

[3] P. Bajari, A. Hortaçsu, The winner’s curse, reserve prices, and endogenous entry: empirical insights from eBay auctions, Rand J. Econ. 34 (2) (2003) 329–355.

[4] G. Bansal, F. Zahedi, D. Gefen, The impact of personal dispositions on information sensitivity, privacy concern and trust in disclosing health information online, Decis. Support Syst 49 (2) (2010) 138–150.

[5] D.P. Baron, Private ordering on the internet: the eBay community of traders, Bus. Politics 4 (3) (2002) 245–274

[6] J.R. Bettman, M.F. Luce, J.W. Payne, Constructive consumer choice processes, J. Consum. Res. 25 (3) (1998) 187–217.

[7] E.M. Bland, G.S. Black, K. Lawrimore, Risk-reducing and risk-enhancing factors impacting online auction outcomes: empirical evidence from eBay auctions, J. Electron. Commer. Res. 8 (4) (2007) 236–243.

[8] J. Bockstedt, K.H. Goh, Seller strategies for differentiation in highly competitive online auction markets, J. Manag. Inf. Syst. 28 (3) (2011) 235–268.

[9] A.S. Bryk, S.W. Raudenbush, Hierarchical Linear Models: Applications and Data Analysis Methods, 2nd edition, Sage Publications, Inc, Thousand Oaks, CA, US 2001.

[10] L. Cabral, A. Hortaçsu, The dynamics of seller reputation: evidence from eBay, J. Ind. Econo. 58 (1) (2010) 54–78.

[11] S. Chaiken, Heuristic versus systematic information processing and the use of source versus message cues in persuasion, J. Pers. Soc. Psychol. 39 (5) (1980) 752-766

[12] J. Cohen, P. Cohen, S.G. West, L.S. Aiken, Applied Multiple Regression/ correlation Analysis for the Behavioral Sciences. 3rd edition Lawrence Erlbaum Associates Publishers. Mahwah. NI. US. 2003.

[13] C. Dellarocas, The digitization of word-of-mouth: promise and challenges of online feedback mechanisms, Manage. Sci. 49 (10) (2003) 1407–1424.

[14] S. Dewan, V. Hsu, Adverse selection in electronic markets: evidence from online stamp auctions, L. Ind, Econ, 52 (4) (2004) 497–516.

[15] A. Dimoka, What does the brain tell us about trust and distrust? Evidence from a functional neuroimaging study, MIS Q. 34 (2) (2010) 373–396.

[16] A. Dimoka, Y. Hong, PÅ. Pavlou, On product uncertainty in online markets Theory and evidence, MIS Q. 36 (2) (2012) 395–426.

[17] U.M. Dholakia, I. Simonson, The effect of explicit reference points on consume choice and online bidding behavior, Mark. Sci. 24 (2) (2005) 206–217.

[18] R.F. Easley, C.A. Wood, S. Barkataki, Bidding patterns, and avoiding the winner’s curse in online auctions, J. Manag. Inf. Syst. 27 (3) (2010) 241–268.

[19] D.H. Eaton, Valuing information: evidence from guitar auctions on eBay, J. Appl. Econ. Policy 24 (1) (2005) 1–19.

[20] A. Everard, D. Galletta, How presentation <sup>fl</sup>aws affect perceived site quality, trust, and intention to purchase from an online store, J. Manag. Inf. Syst. 22 (4) (2006) 55–95.

[21] D. Gefen, P.A. Pavlou, The Boundaries of Trust and Risk: the quadratic moderating role of institutional structures, Inf. Syst. Res. 23 (3) (2012) 940–959.

[22] J.H. Gilkeson, K. Reynolds, Determinants of internet auction success and closing price: an exploratory study, Psychol. Mark. 20 (6) (2003) 537–566.

[23] R. Gonzalez, K. Hasker, R.C. Sickles, An analysis of strategic behavior in eBay auctions, Singap. Econ. Rev. 54 (3) (2009) 441–472.

[24] D.G. Gregg, S. Walczak, Dressing your online auction business for success: an experiment comparing two eBay businesses, MIS Q. 32 (3) (2008) 653–670.

[25] V. Grover, J. Lim, R. Ayyagari, The dark side of information and market ef<sup>fi</sup>ciency in E-markets, Decis. Sci. 37 (3) (2006) 297–324.

[26] V. Grover, P. Ramanlal, Six myths of information and markets: information technology networks, electronic commerce, and the battle for consumer surplus, MIS Q. 23 (4) (1999) 465–495.

[27] J. High<sup>fi</sup>ll, K. O’Brien, The effect of alternative e-prices on eBay book auctions, Atl. Econ. J. 37 (4) (2009) 383–395.

[28] D.A. Hofmann, An overview of the logic and rationale of hierarchical linear models, J. Manag. 23 (6) (1997) 723–744.

[29] D.A. Hofmann, M.B. Gavin, Centering decisions in hierarchical linear models: implications for research in organizations, J. Manag. 24 (5) (1998) 623–641.

[30] J. Hou, Price determinants in online auctions: a comparative study of eBay China and US, J. Electron. Comm. Res. 8 (3) (2007) 172–183.

[31] D. Houser, J. Wooders, Reputation in auctions: theory, and evidence from eBay, J. Econ. Manag. Strategy 15 (2) (2006) 353–369.

[33] D. Kahneman, A. Tversky, Prospect theory: an analysis of decisions under risk, Econometrica 47 (2) (1979) 263–291.

[34] H. Kai, C.L.S. Lim, M.K.O. Lee, I. Benbasat, Do I trust you online, and if so, will I buy? An empirical study of two trust-Building strategies, J. Manag. Inf. Syst. 23 (2) (2006) 233–266.

[35] M.A. Kamins, X. Drèze, V.S. Folkes, Effects of seller-supplied prices on buyers product evaluations: reference prices in an internet auction context, J. Consum. Res. 30 (4) (2004) 622–628.

[36] R.J. Kauffman, C.A. Wood, Doing their bidding: an empirical examination of factors that affect a buyer’s utility in Internet auctions, Inf. Technol. Manag. 7 (3) (2006) 171–190.

[37] J. Lee, J.N. Lee, Understanding the product information inference process in electronic word-of-mouth: an objectivity–subjectivity dichotomy perspective, Inf. Manag. 46 (5) (2009) 302–311.

[38] J. Lim, Consumer Choice of E-Channels as a Purchasing Avenue: An Investigation of the Communicative Aspects of Information Quality, Clemson University, Clemson SC, 2007 (Unpublished doctoral dissertation).

[39] J. Livingston, How valuable is a good reputation? A sample selection model of internet auctions, Rev. Econ. Statistics 87 (2) (2005) 453–465.

[40] H. Lu, J.C.-C. Lin, Predicting customer behavior in the market-Space: a study of rayport and sviokla’s framework, Inf. Manag. 40 (1) (2002) 1–10.

[41] D. Lucking-Reiley, D. Bryan, N. Prasad, D. Reeves, Pennies from eBay: The Determinants of Price in Online Auctions. Working Paper, University of Arizona, Tucson, AZ, 2000. http://eller.arizona.edu/ reiley/papers/ PenniesFromEBay.html.

[42] D. Maheswaran, J. Meyers-Levy, The in<sup>fl</sup>uence of message framing and issue involvement, J. Mark. Res. 27 (3) (1990) 361–367.

[43] A. Marshall, Principles of Economics, Macmillan, London,1997 (1920 reprinted by Prometheus Book).

[44] D. McFadden, The choice theory approach to market research, Mark. Sci. 5 (4) (1986) 275–297.

[45] M.I. Melnik, J. Alm, Does a Seller’s eCommerce reputation matter? Evidence from eBay auctions, I. Ind. Econ, 50 (3) (2002) 337–349

[46] R. Mickey, The impact of a seller's eBay reputation on price, Am. Econ. 55 (2) (2010) 162–169.

[48] A. Muthitachareon, M. Barut, K.A. Saeed, The role of uncertainty stemming from product monetary value in online auctions: the case of search goods, Int J. Electron. Comm. 19 (1) (2014) 65–98.

[49] P. Nelson, Information and consumer behavior, J. Polit. Econ. 78 (2) (1970) 311.

[50] P. Nelson, Advertising as information, J. Polit. Econ. 82 (4) (1974) 729–754.

[51] P. Nelson, Advertising as information once more, in: G. David Tuerck (Ed.), Issues in Advertising: The Economics of Persuasion. American Enterprise Inst Washington, 1978.

[52] A. Nikitkov, Information assurance seals: how they impact consumer purchasing behavior, J. Inf. Syst. 20 (1) (2006) 1–17.

[53] T. Obloj, L. Capron, Role of resource gap and value appropriation: effect of reputation gap on price premium in online auctions, Strateg. Manage. J. 32 (4) (2011) 447–456.

[54] T.A. Ottaway, C.L. Bruneau, G.E. Evans, The impact of auction item image and Buyer/Seller feedback ratings on electronic auctions, J. Comput. Inf. Syst. (2003) 56–60.

[55] P.A. Pavlou, D. Gefen, Psychological contract violation in online marketplaces: antecedents, consequences, and moderating role, Inf. Syst. Res. 16 (4) (2005) 372–399.

[56] R. Pennington, H.D. Wilcox, V. Grover, The role of system trust in business-to-Consumer transactions, J. Manag. Inf. Syst. 20 (3) (2003) 197–226.

[57] S. Plous, The Psychology of Judgment and Decision Making, Mcgraw-Hill Book Company, 1993.

[58] P. Resnick, K. Kuwabara, R. Zeckhauser, E. Friedman, Reputation systems, Commun. ACM 43 (12) (2000) 45–48.

[59] P. Resnick, R. Zeckhauser, Trust among strangers in internet transactions: empirical analysis of eBay's reputation system, in: M.R. Baye (Ed.), The Economics of the Internet and e-commerce (pp. 127–157) Advances in Applied Microeconomics, vol. 11, Elsevier Science, JAI, Amsterdam; London and New York, 2002.

[60] P. Resnick, R. Zeckhauser, J. Swanson, K. Lockwood, The value of reputation on eBay: a controlled experiment, Exp. Econ. 9 (2) (2006) 79–101.

[61] H.A. Simon, A behavioral model of rational choice, Q. J. Econ. 69 (1) (1955) 99– 118.

[62] S.S. Standi<sup>fi</sup>rd, Reputation and e-commerce: eBay auctions and the asymmetrical impact of positive and negative ratings, J. Manag. 27 (3) (2001) 279–295.

[63] B.B. Stern, M.R. Stafford, Individual and social determinants of winning bids in online auctions, J. Consum. Behav. 5 (2006) 43–55.

[64] K.S. Suh, I. Benbasat, E.K. Suh, The impact of listing location on visits, bids, and <sup>fi</sup>nal prices in online auctions: a <sup>fi</sup>eld experiment, Int. J. Electron. Comm. 17 (3) (2013) 87–108.

[65] A. Tversky, D. Kahneman, Judgment under uncertainty: heuristics and biases, Science 185 (4157) (1974) 1124–1131

[66] A. Tversky, D. Kahneman, The framing of decisions and psychology of choice, Science 211 (1981) 453–458.

[67] B. Van Der Heide, B.K. Johnson, M.H. Vang, The effects of product photographs and reputation systems on consumer behavior and product cost on eBay, Comput. Hum. Behav. 29 (3) (2013) 570–576

[68] D. van Heijst, R. Potharst, M. van Wezel, A support system for predicting eBay end prices, Decis. Support Syst. 44 (4) (2008) 970–982.

[69] A. Vishwanath, An empirical investigation into the use of heuristics and information by bidders in online auctions, Electron. Mark. 14 (3) (2004) 178–185.

[70] J. von Neumann, O. Morgenstern, Theory of Games and Economic Behavior, 3rd edition, Princeton University Press, Princeton, NJ, 1953.

[71] M. Waterson, C. Doyle, Your Call: eBay and Demand for the iPhone 4, Int. J. Econom. Bus. 19 (1) (2012) 141–152.

[73] S. Ye, G.G. Gao, S. Viswanathan, Strategic behavior in online reputation systems: evidence from revoking on eBay, MIS Q. 38 (4) (2014) 1033–1056

[74] M. Zhou, M. Dresner, R. Windle, Revisiting feedback systems: trust building in digital markets, Inf. Manag. 46 (5) (2009) 279–284.

[75] C.G. McDonald, V.C. Slawson, Reputation in an Internet Auction Market, Econ. Inq. 40 (2002) 633–650.

[76] S.M. Mudambi, D. Schuff, What makes a helpful review? A study of customer reviews on Amazon.com, MIS Q. 34 (1) (2010) 185–200.

[77] D. Yin, S. Bond, H. Zhang, Anxious or angry? Effects of discrete emotions on the perceived helpfulness of online reviews, MIS Q. 38 (2) (2014) 539–560.

[78] K.K. Kuan, K.L. Hui, P. Prasarnphanich, H.Y. Lai, What makes a review voted? An empirical investigation of review voting in online review systems, J. Assoc. Inf. Syst. 16 (1) (2015) 48.

Michelle Carter is an Assistant Professor in the Carson College of Business at Washington State University. Her work has appeared in MIS Quarterly, MISQ Executive, European Journal of Information Systems, Communications of the AIS, and ACM Transactions on Management Information Systems, as well as several conference proceedings and book chapters. Her current research investigates the involvement of information technologies in identity, humanness, and social change, in an increasingly digital world.

Stefan Tams is an Assistant Professor of Information Systems at HEC Montre'al Canada. He received his PhD from the Department of Management at Clemson University, His research interests focus on the roles of aging, stress and culture in technology-use behaviors, and on electronic commerce. His work has appeared or is scheduled to appear in several scienti<sup>fi</sup>c journals, including Journal of Strategic Information Systems, Journal of the Association for Information Systems, and European Journal of Work and Organizational Psychology.

Varun Grover is the William S. Lee (Duke Energy) Distinguished Professor of Information Systems at Clemson University. He has published extensively in the information systems <sup>fi</sup>eld, with over 200 publications in major refereed journals. Nine recent articles have ranked him among the top four researchers based on number of publications in the top Information Systems journals, as well as citation impact (h-index). Dr. Grover is Senior Editor for MISQ Executive, and Senior Editor (Emeritus) for MIS Quarterly, the Journal of the AIS and Database. He is currently examining the impacts of digitalization on individuals and organizations. He is a recipient of numerous awards from University of South Carolina, Clemson, Association for Information Systems, Decision Sciences Institute, Anbar, PriceWaterhouse, and other organizations for his research and teaching. He is a Fellow of the Association for Information Systems.

Please cite this article in press as: M. Carter, et al., When do I pro<sup>fi</sup>t? Uncovering boundary conditions on reputation effects in online auctions, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.06.007

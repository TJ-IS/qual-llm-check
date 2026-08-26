---
otero_id: 7402
otero_key: "6UQ3EEJM"
title: "Online Product Reviews: Implications for Retailers and Competing Manufacturers"
authors: "Young Kwark; Jianqing Chen; Srinivasan Raghunathan"
year: "2014"
journal: "Information Systems Research"
doi: "10.1287/isre.2013.0511"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [140.117.111.1] On: 25 August 2014, At: 09:33 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR

![](/api/attachments/6UQ3EEJM/fulltext/images/d1f030f0f5b996fc0f9ce98ba5502e79fa813a398b29ea4e84756f4a36bceff2.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Online Product Reviews: Implications for Retailers and Competing Manufacturers

Young Kwark, Jianqing Chen, Srinivasan Raghunathan

## To cite this article:

Young Kwark, Jianqing Chen, Srinivasan Raghunathan (2014) Online Product Reviews: Implications for Retailers and Competing Manufacturers. Information Systems Research 25(1):93-110. http://dx.doi.org/10.1287/isre.2013.0511

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2014, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/6UQ3EEJM/fulltext/images/98fceb57cfff1db201d8a237c58317d4104ff3836f7977ef266572c89ec20f9e.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Online Product Reviews: Implications for Retailers and Competing Manufacturers

Young Kwark

Warrington College of Business Administration, University of Florida, Gainesville, Florida 32611, youngkwark@ufl.edu

Jianqing Chen, Srinivasan Raghunathan Jindal School of Management, The University of Texas at Dallas, Richardson, Texas 75080 {chenjq@utdallas.edu, sraghu@utdallas.edu}

his paper studies the effect of online product reviews on different players in a channel structure. We consider a retailer selling two substitutable products produced by different manufacturers, and the products differ in both their qualities and fits to consumers’ needs. Online product reviews provide additional information for consumers to mitigate the uncertainty about the quality of a product and about its fit to consumers’ needs. We show that the effect of reviews on the upstream competition between the manufacturers is critical in understanding which firms gain and which firms lose. The upstream competition is affected in fundamentally different ways by quality information and fit information, and each information type has different implications for the retailer and manufacturers. Quality information homogenizes consumers’ perceived utility differences between the two products and increases the upstream competition, which benefits the retailer but hurts the manufacturers. Fit information heterogenizes consumers’ estimated fits to the products and softens the upstream competition, which hurts the retailer but benefits the manufacturers. Furthermore, reviews may also alter the nature of upstream competition from one in which consumers’ own assessment on the quality dimension plays a dominant role in consumers’ comparative evaluation of products to one in which fit dimension plays a dominant role. If manufacturers do not respond strategically to reviews and keep the same wholesale prices regardless of reviews (i.e., the upstream competition is assumed to be unaffected by reviews), then, we show that reviews never hurt the retailer and the manufacturer with favorable reviews, and never benefit the manufacturer with unfavorable reviews, a finding that demonstrates why reviews’ effect on upstream competition is critical for firms in online marketplaces.

Keywords: online product reviews; competition; electronic commerce; analytical modeling; economics of IS History: Il-Horn Hann, Senior Editor; De Liu, Associate Editor. This paper was received on June 20, 2012, and was with the authors 10 months for 2 revisions.

## 1. Introduction

With the ubiquity of the Internet and the prevalence of user-generated content, an increasing number of consumers read online product reviews before they make purchase decisions (Deloitte and Touche 2007, Cone 2010). Consumer surveys report that online product reviews strongly influence consumers’ purchase decisions. According to Deloitte and Touche (2007), although 43% of surveyed consumers were reinforced of their original purchase intention by reviews, 43% of consumers changed their opinions about which product to buy, and 9% of consumers even abandoned their purchase plan after reading the product reviews. These data suggest that consumers rely on their own assessments of products as well as others’ assessments embedded in the product reviews when evaluating competing products and making purchase decisions.

Third-party websites such as CNET.com and online retailer sites such as Amazon.com provide both expert and consumer reviews. Online product reviews have become an important information source for consumers to mitigate the uncertainty about the quality of a product and about its fit to consumers’ needs (Chen and Xie 2008). The quality of a product refers to the degree of excellence of the product (or of some attribute of the product). For example, the battery life and wifi connection of a cell phone are about the quality. Consumers agree on the preference order of quality in that they all prefer high quality to low quality, everything else being equal. The fit of a product refers to the degree of being in agreement with a consumer’s need. For example, the keyboard design (physical buttons versus soft buttons), size, and color of a cell phone are about the fit. Fit is consumer specific, and consumers may have different preferences for a same attribute. Online product reviews provide information about the quality and fit of products. For instance, the following review on Amazon about Samsung Galaxy S provides information about the quality (of battery life and wifi connection): “Despite everybody giving great review about this phone I have had nothing but problem with this device, to start out with poor battery life, despite all app. killer running, still the battery does not last even a day, second, wifi does not connect immediately on phone.”<sup>1</sup> In contrast, the following review is more about the fit attributes (the button design and sizes of the case and phone), and consumers have different preference over these attributes. “Complaints? None really, except I miss physical buttons on the bottom—much easier to feel them and then click without having to look down. …Also the case is far too smooth for such a big phone. You’ll want a case that offers some grip to the phone or it will slip out of your hands.”<sup>2</sup>

An important feature of online product reviews is that they are public and common to all consumers as well as sellers. On the one hand, some information revealed by the reviews, such as the quality of a product, would have similar effects on purchase decisions of all consumers. Therefore, the public and common reviews would play an important role in shifting a product’s demand. On the other hand, the reviews also provide additional information about a product’s fit to consumers’ needs. Because different consumers may have different needs, the information in the fit dimension may have different effects on consumers’ purchase decisions. Many empirical studies have examined the effect of reviews on consumers’ purchase decisions and retailer’s sales (e.g., Chevalier and Mayzlin 2006, Zhu and Zhang 2010). Departing from these studies, in this paper we aim to analytically study the effect of online product reviews in a channel structure and investigate how reviews affect the upstream competition between manufacturers as well as the retailer.

The question of how online product reviews affect the price competition between substitutable products is important to both practitioners and academics. The question becomes especially important in a context of a dominant retailer selling competing products from different manufacturers, because such a twolevel channel structure with one dominant retailer is commonly observed in practice (e.g., Amazon.com). In such contexts, although each manufacturer views the substitutable products from other manufacturers as competitors, the retailer may view the products as satisfying the different needs of different consumers. Therefore, reviews may have fundamentally different effects on the manufacturers and retailer.

Furthermore, from a retailer’s perspective, an analysis of reviews’ effects on both consumers (demand side) and manufacturers (supply side) is essential for a more complete understanding of reviews’ implications. However, the effect of online product reviews on the retailer and individual manufacturers remains unexplored and unclear despite the large volume of studies dedicated to the online review phenomenon.

To address this question, we develop a game theoretic model in which one retailer sells two substitutable products produced by different manufacturers. The products differ in both their qualities and the fits to consumers’ needs. Although all consumers value high quality rather than low quality, different consumers have different needs, with some consumers perceiving one product more suitable than the other product while others perceiving the opposite way. Each consumer has her own assessment of the quality of each product and its fit to her need. The online product reviews provide additional information in both the quality and fit dimensions. We distinguish the case in which the consumers’ own assessment on the quality dimension plays a dominant role in determining consumers’ perceived utility differences between the two products, and the case in which the fit dimension plays an important role such that the fit is critical for some consumers. We call the former the quality-dominates-fit case and the latter the fit-dominates-quality case. We use the scenario without product reviews as the benchmark and study the effect of online product reviews on the competition between the two manufacturers as well as on the retailer.

We find that the information in the quality dimension and fit dimension embedded in the online product reviews has very different effects on the competition between the two products. We show that reviews reduce the heterogeneity of consumers’ perceived quality differences and thus increase the competition between the two manufacturers. We call this reduced heterogeneity resulting from the reviews variance-reducing effect, which generally hurts the manufacturers and benefits the retailer. Additionally, reviews shift the mean perceived quality difference in favor of the product with favorable reviews. We call this mean-shifting effect, which generally benefits the manufacturer with favorable reviews and the retailer. As a result, in the quality-dominates-fit case, the retailer benefits from the reviews. The manufacturer with unfavorable reviews suffers from the reviews not only because unfavorable comments shift its demand away but also because of the increased competition. In equilibrium, we find that the manufacturer is induced to lower its wholesale price and earns less profit because of the reviews. Interestingly, even the manufacturer with favorable reviews would be worse off if the negative effect from the reduced heterogeneity dominates the positive effect from the favorable reviews.

In contrast, for the fit dimension, online product reviews enable consumers to better understand the products’ fits to their needs. We demonstrate that, because of the reviews, consumers are differentiated further from each other in their perceived fits. This result occurs because consumers have different underlying needs and learn better about the products’ fits to their needs with the additional product information from the reviews. We call this increased heterogeneity resulting from the reviews variance-increasing effect. The variance-increasing effect softens the competition between the two manufacturers, which generally benefits the manufacturers and hurts the retailer. As a result, in the fit-dominates-quality case, reviews hurt the retailer if the negative impact of varianceincreasing effect outweighs the positive impact of mean-shifting effect. The manufacturer with favorable reviews in the quality dimension benefits from the reviews in both the positive comments about its product quality and the reduced competition. Therefore, in equilibrium, the manufacturer charges a higher wholesale price and earns a higher profit. It is worth noting that the manufacturer with unfavorable reviews can also be better off if the positive effect of reduced competition offsets the negative effect from unfavorable comments about its product quality.

Interestingly, we find that reviews with sufficiently high precision may alter the nature of upstream competition from one in which quality dimension plays a dominant role in consumers’ utility assessment to one in which fit dimension plays a dominant role. Therefore, a retailer that benefits from reviews when the review precision is not high may be hurt by them if the review precision is high because, as explained in the previous two paragraphs, the reviews’ impact on the upstream competition is fundamentally different in the quality-dominates-fit and fit-dominatesquality cases.

All of the above results hold only when manufacturers respond strategically to reviews. If manufacturers keep the same wholesale prices regardless of reviews (i.e., reviews do not have any effect on upstream competition), then we show that reviews never hurt the retailer nor the manufacturer with favorable reviews, and never benefit the manufacturer with unfavorable reviews. Stated more generally, our main result is that when online product reviews mitigate consumers’ uncertainty about quality and fit dimensions of perceived utility difference between competing products, the effect of reviews on the upstream competition between manufacturers is critical in understanding which firms gain and which firms lose.

Several recent studies have analyzed the effect of product reviews on firms. Empirical studies have examined the impact of reviews on firm’s sales, and the findings have been mixed. For instance, while some studies found a significant positive association between rating valence and sales (Chevalier and Mayzlin 2006, Clemons et al. 2006, Duan et al. 2008), others did not find a relationship between the two (Chen et al. 2004, Liu 2006). The variance of product ratings (Clemons et al. 2006), the volume of ratings (Liu 2006), text reviews (Archak et al. 2011), and the reviewer characteristics or product characteristics (Forman et al. 2008, Zhu and Zhang 2010) have been found to have an impact on sales. Online product reviews have also been found to be subject to self-selection biases that impact consumer purchase behavior (Li and Hitt 2008) and to reflect not only perceived quality but also the perceived value, which is the difference between perceived quality and price (Li and Hitt 2010). These empirical results suggest that sellers may have an incentive to manipulate reviews of their products to improve their competitive position. Dellarocas (2006) and Mayzlin (2006) analyze sellers’ incentives to manipulate reviews and show that reviews are informative even under seller manipulation. Different from these studies, we view the reviews as information mitigating the uncertainty in a product quality and the fit to consumers’ needs, and investigate how this additional information affects upstream product competition.

Some existing analytical work has modeled product reviews as information that enables consumers to identify products matching their needs (Chen and Xie 2008) or estimate their true utilities more accurately (Li et al. 2011, Sun 2012). Many of these models focus on how the nature of a product in their market appeal (e.g., mass or niche products) affects review outcome (e.g., positive or negative), and in turn how the reviews affect consumers’ willingnessto-pay and therefore the product demand. In addition, these models typically consider the effect of reviews on sellers in a framework of direct selling from sellers to consumers. For example, Li et al. (2011) study how consumer reviews mediate the competition between two direct sellers when consumers face repeat purchases and a cost to switch products between periods, and consumer reviews convey product fits to them. In contrast, we consider a two-level channel structure with a retailer selling products from competing manufacturers and consumers facing twodimensional product uncertainty—both the product quality and the fit to their needs. Interestingly, we find that the quality information and fit information play very different roles in changing the upstream competition between the manufacturers, and the same reviews would have very different implications for the retailer and each manufacturer.

Another stream of research has modeled product reviews as free advertising and analyzed how sellers should adjust their own marketing mix strategies in the presence of the reviews (Chen and Xie 2005, Jiang and Srinivasan 2011, Kuksov and Xie 2010). Most of the papers in this stream assume that sellers know consumers’ ex ante expectation of product valuation and how reviews affect this expectation. One particularly related paper is Shaffer and Zettelmeyer (2002), which analyzes the effects of information provision on the profits of channel members when the information is supplied by third parties. In their model, all consumers have the same product information, additional information has the same qualitative impact (positive or negative) on every consumer, and sellers have perfect knowledge of all product information. In our model, we consider that consumers have private estimates of the products’ qualities and fits to their needs, and online product reviews provide public and common additional information about quality and private and idiosyncratic additional information about fit to consumers. Our results and insights lie in the changes in consumer heterogeneity resulting from the changes in the uncertainty facing consumers because of reviews, which differ from the existing work.

Our paper is also related to studies that use horizontal differentiation models (Chen and Xie 2008, Li et al. 2011, Gu and Xie 2012, Shaffer and Zettelmeyer 2002, Villias-Boas 2004, Sun 2012, Sun and Tyagi 2012). All these papers consider consumer “fit” or “taste” as an important factor in consumers’ utility function. Different approaches have been used in the literature to model consumer fit/taste. Some papers use discrete taste models in which the fit dimension is modeled to be a perfect match or a mismatch and, in the case of mismatch, consumers incur some disutility $( \mathrm { e . g . , }$ in Chen and Xie 2008, Li et al. 2011, Gu and Xie 2012). Others use continuous taste models in which the degree of fit is modeled as a continuous variable and different consumers may have different degrees of misfit and thus incur different disutilities (e.g., in Shaffer and Zettelmeyer 2002, Villias-Boas 2004, Sun 2012, Sun and Tyagi 2012, Jiang and Guo 2013). In particular, the Hotelling model and its variations have been widely used for a duopoly setting: the misfit cost is modeled as the degree of misfit times a unit misfit cost, and a consumer’s degree of misfit to one product is negatively correlated to the misfit to the other product. Our model for consumer fit dimension belongs to the continuous taste models.

The rest of this paper is organized as follows. In the next section, we lay out the model. In $\ S 3 ,$ we derive the main results of the effect of the reviews on the upstream competition and the retailer. Section 4 concludes the paper.

## 2. Model

We consider a retailer R that sells two products, A and B. The products are imperfect substitutes, and are produced by different manufacturers. We call the manufacturer that produces product A (B) manufacturer A (B). The marginal production cost for each product is assumed to be zero. The manufacturers sell their products to the retailer and the retailer sells them to end consumers. Each consumer has a unit demand.

Consumer Utility and Consumer Segments. Each product is characterized by a quality attribute and a fit attribute. The quality attribute represents the vertical dimension in the sense that every consumer prefers high quality to low quality. The fit attribute represents the horizontal dimension in the sense that preferences vary across consumers. The quality of a product determines the maximum value that a consumer derives from the product, which is denoted as $x _ { i } , i \in \{ A , B \}$ . The products may not have perfect fits to consumers and thus consumers incur misfit costs. We use a typical horizontal product differentiation model to model the misfit cost. In particular, we assume that products A and B are located at positions 0 and 1 of a line of length 1 (i.e., at the two ends of the line), respectively, and consumers are uniformly distributed along the line. The distance between a consumer and a product measures the degree of misfit of the product to the consumer. Notice that when the degree of misfit between a consumer and product $A$ is $\lambda , \lambda \in [ 0 , 1 ] .$ , the degree of misfit between the consumer and product B is $( 1 - \lambda )$ . The misfit cost is the degree of misfit times a unit misfit cost t. A consumer’s utility from product i, $U _ { i } ,$ is the maximum value that the product offers net the misfit cost. A consumer’s net utility from a product is the utility net the retail price. Denoting the retail price as $p _ { i } , i \in \{ A , B \}$ we can formulate the net utilities derived from products A and B for the consumer with a degree of misfit  to product A as follows:

$$
\left\{ \begin{array}{l} V _ {A} = U _ {A} - p _ {A} = x _ {A} - \lambda t - p _ {A} \\ V _ {B} = U _ {B} - p _ {B} = x _ {B} - (1 - \lambda) t - p _ {B}. \end{array} \right.\tag{1}
$$

We distinguish two types of consumers: loyal customers and comparison shoppers. Loyal customers only consider purchasing the product from the manufacturer that they are loyal to and know its quality and fit, but they may or may not purchase, depending on its price. Based on the utility functions in Equation (1), for ease of exposition, we can formulate the demand for product i from its loyal customers as

$$
D _ {i l} = h _ {i} - \alpha p _ {i}\tag{2}
$$

in which  $( \alpha \in \mathbb { R } ^ { + } )$ measures the price sensitivity of its loyal customers.<sup>3</sup>

Our focus is on comparison shoppers, because we are interested in the competition between the two manufacturers and the manufacturers only compete for comparison shoppers. Comparison shoppers, or shoppers, compare the two products from both manufacturers and choose the one that offers higher net utility. For the shopper with the degree of misfit  to product $A ,$ the net utility difference between product A and B, $V _ { A } - V _ { B } ,$ is

$$
\begin{array}{r l} & V _ {A} - V _ {B} = (U _ {A} - U _ {B}) - (p _ {A} - p _ {B}) \\ & \qquad = (x _ {A} - x _ {B}) + (1 - 2 \lambda) t - (p _ {A} - p _ {B}). \end{array}\tag{3}
$$

We also call $( x _ { A } - x _ { B } )$ the quality difference of the two products. Unless otherwise indicated, we call  the degree of misfit. We assume that the (true) quality difference between the products is zero.<sup>4</sup> Note that, by the horizontal product differentiation model setup, consumers’ (true) degrees of misfit satisfy a uniform distribution. Next, we describe the effect of reviews on shoppers’ perceived net utility differences and the demand from shoppers. Without loss of generality, we assume the number of shoppers is a unit mass.

Product Uncertainty and Online Product Reviews. Shoppers are uncertain about both product quality and the misfit, where the online product reviews play a role as in Chen and Xie (2008). That ${ \mathrm { i } } { \mathrm { s } } ,$ shoppers do not know the true quality difference or their true degrees of misfit. In the absence of online product reviews, based on the product description and other information sources, each shopper has her own assessment of the quality difference between the two products and of the misfit. We denote as $x _ { C }$ a shopper’s own assessment of the quality difference $( \mathrm { i . e . , } ( x _ { A } - x _ { B } )$ in Equation (3)). Similar to the approach often used in the literature (e.g., Lewis and Sappington 1994, Ruckes 2004, Johnson and Myatt 2006, McCracken 2011, Petriconi 2012), the uncertainty in the misfit is modeled as that a shopper observes a signal s, which equals the shopper’s true degree of misfit with probability $\beta _ { C } ,$ , and with probability $( 1 - \beta _ { C } )$ is uninformative and follows the distribution of shoppers’ true degrees of misfit; that is, $\operatorname* { P r } ( s = y \mid \lambda = y ) = \beta _ { C }$ and $\mathrm { P r } ( s \neq y \mid \lambda = y ) = 1 - \beta _ { C } ,$ , where $y \in \left[ 0 , 1 \right]$ . Essentially, what we assume about the signal is that the signal is informative $( \mathrm { i . e . , }$ providing useful information) but noisy $( \mathrm { i . e . , }$ not perfectly revealing the truth). Based on Bayesian updating, we can derive the expected degree of misfit $\operatorname { E } ( \lambda \mid \smile = y ) = [ \beta _ { C } y + ( 1 - \beta _ { C } ) / 2 ]$ (see the proof in the appendix). According to Equation (3), the expected net utility difference between product A and B for the shopper with perceived quality difference $x _ { C }$ and signal $s = y$ on the degree of misfit is then

$$
\mathrm{E} \left(V _ {A} - V _ {B} \mid x _ {C}, y\right) = x _ {C} + (1 - 2 y) \beta_ {C} t - \left(p _ {A} - p _ {B}\right).\tag{4}
$$

Different shoppers perceive different $x _ { C }$ and receive different signals y. We assume that at the aggregate level shoppers’ perceived quality differences satisfy a uniform distribution over $[ - \epsilon , \epsilon ]$ . The uncertainty model for the signal about misfit implies that the signals satisfy a uniform distribution over 601 17. The retailer does not know an individual shopper’s perceived quality difference or signal about the misfit, but knows their distributions.

Online product reviews provide public information about the products, and shoppers use this information in addition to their own assessments to evaluate the products. We denote as $x _ { R }$ the perceived quality difference in the two products revealed by the online product reviews, which is common to all shoppers. In the presence of online product reviews, shoppers combine their own assessments $x _ { C }$ and the public common assessment $x _ { R }$ to form their judgment of the quality difference between the two products. As shown by Bates and Granger (1969) using the minimum variance estimation, the shopper’s expected quality difference becomes $r x _ { C } + ( 1 - r ) x _ { R } ,$ , where $r ,$ $r \in ( 0 , 1 )$ , depends on the relative precisions of the two information sources, and the weight on the product reviews, $( 1 - r )$ , is high when the precision of the product review information is high. Intuitively, shoppers adjust their quality assessments because of the additional information from the product reviews, and the extent to which the reviews affect shoppers’ assessments depends on the relative precisions and confidence between their own assessments and the product reviews. For the fit dimension, with the additional information provided by online product reviews, shoppers know better about their idiosyncratic fit. Similar to the scenario where reviews are unavailable, in the scenario where reviews are available the uncertainty in the misfit is modeled as that a shopper observes a new signal. However, this signal, because of the additional information provided by online product reviews, is more informative than that in the absence of online product reviews. In particular, this new signal equals a shopper’s true degree of misfit with probability $\beta _ { R }$ and with probability $( 1 - \beta _ { R } )$ is uninformative, where $\beta _ { R } > \beta _ { C }$ . Similarly, by Bayesian updating, we can derive the expected degree of misfit $\operatorname { E } ( \lambda \mid \overset { \smile } { s } = y ) = [ \beta _ { R } y + ( 1 - \beta _ { R } ) \mathit { \bar { / } 2 } ]$ in the presence of reviews. Notice that a shopper’s signal in the presence of reviews may or may not indicate the same degree of misfit s as the one in the absence of reviews, but the signal is more accurate about the degree of misfit with reviews than without. Based on Equation (3), in the presence of online product reviews, the expected net utility difference between product A and B for the shopper with perceived quality difference $x _ { C }$ and signal $s = y$ on the degree of misfit is then

Figure 1 Competitive Cases  
![](/api/attachments/6UQ3EEJM/fulltext/images/caa6215a9e9ded9dcd048f7d71ab36819d402a8c1e3cf21080d187863e6226b3.jpg)

$$
\begin{array}{r l} \mathrm{E} (V _ {A} - V _ {B} \mid x _ {C}, y) & = [ r x _ {C} + (1 - r) x _ {R} ] + (1 - 2 y) \beta_ {R} t \\ & \quad - (p _ {A} - p _ {B}). \end{array} \tag {5}
$$

Timing of the Game. The sequence of events is as follows. In stage 1, manufacturers set wholesale prices $w _ { i }$ simultaneously. In stage 2, the retailer sets retail prices $p _ { i }$ . In stage 3, shoppers evaluate difference of product utility, and make their purchase decisions. We consider two scenarios: one without online product reviews and the other with reviews. We use the scenario without reviews as the benchmark to analyze the effect of reviews. In the scenario with reviews, reviews are observed by shoppers, the manufacturers, and the retailer before they make their decisions. Therefore, consistent with many existing studies (e.g., Shaffer and Zettelmeyer 2002), we do not model the review generating process and instead we examine the effect of reviews when product reviews are in a steady state.<sup>5</sup> Shoppers’ own estimates about product quality differences and their misfits are their private information. All other model parameters are common knowledge. All players are risk neutral.

Demand Functions. In stage 3 of the game, shoppers learn the expected utility differences between two products. Based on Equations (4) and (5), we can uniformly formulate a shopper’s expected net utility difference for both the without-review and withreview scenarios as

![](/api/attachments/6UQ3EEJM/fulltext/images/c8abf51eaf64ef84e3071abd57a50d8e4ed549b5f83570ae9ae56619064a177a.jpg)

$$
\begin{array}{r l} & {\mathrm{E} (V _ {A} - V _ {B} \mid x _ {C}, y)} \\ & {\qquad = \mathrm{E} (U _ {A} - U _ {B} \mid x _ {C}, y) - (p _ {A} - p _ {B})} \\ & {\qquad = [ \gamma x _ {C} + (1 - \gamma) x _ {R} ] + (1 - 2 y) \beta t - (p _ {A} - p _ {B})} \end{array}\tag{6}
$$

in which $( \gamma , \beta ) \in \{ ( 1 , \beta _ { C } ) , ( r , \beta _ { R } ) \}$ with $\gamma = 1$ and $\beta = \beta _ { C }$ for the scenario without reviews and $\gamma = r$ and $\beta = \beta _ { R }$ for the scenario with reviews. $\operatorname { E } ( U _ { A } - U _ { B } \vert x _ { C } , y ) =$ $[ \gamma x _ { C } + ( 1 - \gamma ) x _ { R } ] + ( 1 - 2 y ) \beta t$ is the shopper’s expected utility difference. As in typical “location” models of horizontal product differentiation, we assume that the maximum value that each product delivers is high enough such that shoppers derive positive net utility from each product.

Clearly, besides shoppers’ own assessments, the product reviews affect shoppers’ perceived net utility differences between the two products by changing $\gamma$ and $\beta .$ We focus our analysis on the cases in which online product reviews play a mild or moderate role in changing the competition between the two manufacturers such that in equilibrium two manufacturers are comparably competitive. The extreme case in which the additional difference revealed by online product reviews is so dramatic such that one manufacturer has a dominant advantage in the market is not considered in this study.

We next distinguish two cases:

• Quality-dominates-fit case. We define qualitydominates-fit case as the one in which shoppers’ own assessment on the quality dimension dominates the fit dimension such that there exist shoppers who have the lowest fit with product A but derive higher net utility from it than from product B because their own assessment on the quality dimension is favorable toward product $A ,$ and there also exist shoppers who have the lowest fit with product B but derive higher net utility from it. Figure 1(a) illustrates the qualitydominates-fit case.

• Fit-dominates-quality case. We define fit-dominates-quality case as the one in which the fit dimension dominates shoppers’ own assessment on quality dimension such that shoppers who have perfect fit with a product always derive a higher net utility from that product, regardless of their own assessment on the quality dimension. Figure 1(b) illustrates the fitdominates-quality case.

In general, products evaluated based on the objective indices such as product performance, reliability, and durability are likely to be quality dominant (Garvin 1984). Examples include digital cameras, GPS, and hardware. Products evaluated based on subjective consumer-specific indices such as experience attributes, features, and aesthetics are more fit dominant (Sutton 1986). Examples include jewelery and video games. In the sequel, we derive the conditions under which each case occurs in equilibrium.

In quality-dominates-fit case, as illustrated in Figure 1(a), for any shopper who receives signal $y ,$ $y \in [ 0 , 1 ] .$ , her perceived net utility difference would be positive or negative, depending on her perceived quality difference. By Equation (6), if her perceived quality difference is higher than $[ ( p _ { A } - p _ { B } ) -$ $( 1 - \gamma ) \bar { x _ { R } } - ( \bar { 1 } - 2 y ) \beta t ] / \gamma ,$ , she derives higher net utility from product A; otherwise, she derives higher net utility from product B. Therefore, we can formulate the demand for each product from shoppers as

$$
\begin{array}{r l} & D _ {A c} = \int_ {0} ^ {1} \int_ {[ p _ {A} - p _ {B} - (1 - \gamma) x _ {R} - (1 - 2 y) \beta t ] / \gamma} ^ {\epsilon} \frac {1}{2 \epsilon} d x d y \\ & \qquad = \frac {1}{2} - \frac {1}{2 \gamma \epsilon} [ p _ {A} - p _ {B} - (1 - \gamma) x _ {R} ], \\ & D _ {B c} = \int_ {0} ^ {1} \int_ {- \epsilon} ^ {[ p _ {A} - p _ {B} - (1 - \gamma) x _ {R} - (1 - 2 y) \beta t ] / \gamma} \frac {1}{2 \epsilon} d x d y \\ & \qquad = \frac {1}{2} + \frac {1}{2 \gamma \epsilon} [ p _ {A} - p _ {B} - (1 - \gamma) x _ {R} ], \end{array}\tag{7}
$$

where the integral in product $i \prime \mathrm { s }$ demand measures the shoppers who derive higher net utility from product i than from the other product, $i \in \{ A , B \}$

In the fit-dominates-quality case, shoppers who perceive a strong fit with product A always derive higher net utility from product A, and shoppers who perceive a strong fit with product B always derive higher net utility from product B, regardless of the perceived quality difference. As illustrated in Figure 1(b), we can denote the former consumer group as those who receive signal $y \in [ 0 , y _ { A } ]$ and the latter as those who receive signal $y \in [ y _ { B } , 1 ]$ along the line, because of the monotonicity between the net utility difference and the fit dimension. The shoppers who receive signals between $y _ { A }$ and $y _ { B }$ may derive higher net utility from product A or from product $B ,$ depending on their perceived quality differences. The marginal consumer $y _ { A } \ ( y _ { B } )$ is the one who derives the same utility from the two products when perceiving the largest quality difference against product A (B); that is, when $x _ { C } = - \epsilon \ ( x _ { C } = \epsilon )$ . By Equation (6), we have

$$
\begin{array}{r} y _ {A} = \frac {1}{2 \beta t} [ - \gamma \epsilon + (1 - \gamma) x _ {R} + \beta t - (p _ {A} - p _ {B}) ], \\ y _ {B} = \frac {1}{2 \beta t} [ \gamma \epsilon + (1 - \gamma) x _ {R} + \beta t - (p _ {A} - p _ {B}) ]. \end{array}\tag{8}
$$

We then can formulate the demand for each product from shoppers in fit-dominates-quality case as

$$
\begin{array}{r l} & D _ {A c} = \int_ {0} ^ {y _ {A}} d y + \int_ {y _ {A}} ^ {y _ {B}} \int_ {[ p _ {A} - p _ {B} - (1 - \gamma) x _ {R} - (1 - 2 y) \beta t ] / \gamma} ^ {\epsilon} \frac {1}{2 \epsilon} d x d y \\ & \qquad = \frac {1}{2} - \frac {1}{2 \beta t} [ p _ {A} - p _ {B} - (1 - \gamma) x _ {R} ], \\ & D _ {B c} = \int_ {y _ {A}} ^ {y _ {B}} \int_ {- \epsilon} ^ {[ p _ {A} - p _ {B} - (1 - \gamma) x _ {R} - (1 - 2 y) \beta t ] / \gamma} \frac {1}{2 \epsilon} d x d y + \int_ {y _ {B}} ^ {1} d y \\ & \qquad = \frac {1}{2} + \frac {1}{2 \beta t} [ p _ {A} - p _ {B} - (1 - \gamma) x _ {R} ]. \end{array}\tag{9}
$$

From Equations (7) and (9), we notice that each firm’s demands from shoppers in both cases take the same structure except the coefficients of the terms in the brackets $( \mathrm { i . e . , ~ } \bar { 1 } / ( 2 \gamma \epsilon )$ in quality-dominates-fit versus $1 / ( 2 \beta t )$ in fit-dominates-quality). As a result, together with the demand from loyal customers in Equation (2), we can uniformly characterize the demand as follows:<sup>6</sup>

$$
\begin{array}{c} D _ {A} = D _ {A l} + D _ {A c} = \left[ \frac {1 + 2 h}{2} + \frac {1}{2 \tau} (1 - \gamma) x _ {R} \right] \\ - \left(\frac {1}{2 \tau} + \alpha\right) p _ {A} + \frac {1}{2 \tau} p _ {B}, \\ D _ {B} = D _ {B l} + D _ {B c} = \left[ \frac {1 + 2 h}{2} - \frac {1}{2 \tau} (1 - \gamma) x _ {R} \right] \\ - \left(\frac {1}{2 \tau} + \alpha\right) p _ {B} + \frac {1}{2 \tau} p _ {A}, \end{array}\tag{10}
$$

where $\tau \in \{ \gamma \epsilon , \beta t \}$ with $\tau = \gamma \epsilon$ for quality-dominatesfit case and $\tau = \beta t$ for fit-dominates-quality case. This expression evidently demonstrates that the assumptions that we impose on consumer segments, shoppers’ true and perceived preferences, and distribution of shoppers’ perceived quality difference are equivalent to the assumptions on linear demand functions that have been commonly used in the literature (e.g., Choi 1991). The online product reviews affect the competition between the two manufacturers by changing the parameters of the above demand functions. Notice that the terms $[ ( 1 + 2 h ) / 2 \pm$ $\left( 1 - \gamma \right) x _ { R } / ( 2 \tau ) ]$ in Equation (10) measure the market potential sizes for the products. To exclude trivial cases, we assume that the market potential sizes are positive; that is,

Table 1 Summary of Notations

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Notation Definition and comments
i Index for products/manufacturers
 $x_{i}$  True quality of product i
 $\lambda$  True degree of misfit between a consumer and product A
t Unit misfit cost
 $p_{i}$  Retail price of product i
 $U_{i}$  A consumer's utility derived from product i
 $V_{i}$  A consumer's net utility derived from product i
 $h_{i}$  Size of potential demand for product i from loyal customers; in the case with symmetric quality,  $h_{A}=h_{B}\equiv h$ $\alpha$  Price sensitivity of loyal customers
 $D_{il}$  Demand for product i from its loyal customers;  $D_{il}=h_{i}-\alpha p_{i}$ $x_{C}$  A consumer's perceived quality difference between products A and B
 $\epsilon$ $x_{C}$  satisfies a uniform distribution over  $[-\epsilon,\epsilon]$ 
s Misfit signal
y A consumer's degree of misfit toward product A indicated by misfit signal
 $\beta_{C}$  Probability that the indicated degree of misfit equals a consumer's true degree of misfit in the absence of reviews
 $x_{R}$  Quality difference between products A and B indicated by reviews
r The weight assigned to consumers' own assessment of the quality difference in the presence of reviews
 $\beta_{R}$  Probability that the indicated degree of misfit equals a consumer's true degree of misfit in the presence of reviews
 $w_{i}$  Wholesale price of product i
 $D_{ic}$  Demand for product i from shoppers
 $D_{i}$  Demand for product i;  $D_{i}=D_{ic}+D_{il}$ $\pi_{i}$  Manufacturer i's profit in the absence of reviews
 $\hat{\pi}_{i}$  Manufacturer i's profit in the presence of reviews
 $\pi_{R}$  Retailer's profit in the absence of reviews
 $\hat{\pi}_{R}$  Retailer's profit in the presence of reviews
</div>

$$
(1 + 2 h) \tau > (1 - \gamma) | x _ {R} |.\tag{11}
$$

Table 1 summarizes the main notations used in the paper.

## 3. Effect of Online Product Reviews

In this section, we first derive the subgame perfect equilibria for both the scenario without online product reviews and the one with reviews. We then analyze the effects of online product reviews on the retailer and manufacturers by comparing their equilibrium payoffs under the two scenarios.

In stage 2 of the game, the retailer maximizes its profit by choosing the optimal price for each product; that ${ \mathrm { i } } \mathbf { s } ,$

$$
\max _ {p _ {A}, p _ {B}} \pi_ {R} = (p _ {A} - w _ {A}) D _ {A} + (p _ {B} - w _ {B}) D _ {B}.\tag{12}
$$

By the first-order conditions, we can derive the retailer’s optimal prices, which are functions of wholesale prices. In stage 1 of the game, anticipating the retailer’s reaction in response to the wholesale prices, the manufacturers maximize their profits by choosing their optimal prices; that is,

$$
\max _ {w _ {i}} \pi_ {i} = w _ {i} D _ {i}, \quad i \in \{A, B \}.\tag{13}
$$

Based on the first-order conditions, we can obtain the optimal wholesale price for each manufacturer. Substituting the optimal wholesale prices back to retailer’s pricing, we can derive the equilibrium retail prices. Then, the equilibrium demand for each product and the profits for the retailer and manufacturers follow. We summarize the equilibrium outcome in the following lemma.

<sup>Lemma</sup> <sup>1.</sup> The equilibrium wholesale prices, retail prices, and profits for each player in the scenarios with and without online product reviews are as follows.

(a) Wholesale prices:

$$
w _ {A} = \frac {\tau (1 + 2 h)}{1 + 4 \alpha \tau} + \frac {(1 - \gamma) x _ {R}}{3 + 4 \alpha \tau},\tag{14}
$$

$$
w _ {B} = \frac {\tau (1 + 2 h)}{1 + 4 \alpha \tau} - \frac {(1 - \gamma) x _ {R}}{3 + 4 \alpha \tau};\tag{15}
$$

(b) Retail prices:

$$
p _ {A} = \frac {(1 + 6 \alpha \tau) (1 + 2 h)}{4 \alpha (1 + 4 \alpha \tau)} + \frac {(5 + 6 \alpha \tau) (1 - \gamma) x _ {R}}{4 (1 + \alpha \tau) (3 + 4 \alpha \tau)},\tag{16}
$$

$$
p _ {B} = \frac {(1 + 6 \alpha \tau) (1 + 2 h)}{4 \alpha (1 + 4 \alpha \tau)} - \frac {(5 + 6 \alpha \tau) (1 - \gamma) x _ {R}}{4 (1 + \alpha \tau) (3 + 4 \alpha \tau)};\tag{17}
$$

(c) Profits:

$$
\pi_ {A} = \frac {(1 + 2 \alpha \tau) [ \tau (1 + 2 h) (3 + 4 \alpha \tau) + (1 + 4 \alpha \tau) (1 - \gamma) x _ {R} ] ^ {2}}{4 \tau (1 + 4 \alpha \tau) ^ {2} (3 + 4 \alpha \tau) ^ {2}},\tag{18}
$$

$$
\pi_ {B} = \frac {(1 + 2 \alpha \tau) [ \tau (1 + 2 h) (3 + 4 \alpha \tau) - (1 + 4 \alpha \tau) (1 - \gamma) x _ {R} ] ^ {2}}{4 \tau (1 + 4 \alpha \tau) ^ {2} (3 + 4 \alpha \tau) ^ {2}},\tag{19}
$$

$$
\pi_ {R} = \frac {(1 + 2 \alpha \tau) ^ {2} (1 + 2 h) ^ {2}}{8 \alpha (1 + 4 \alpha \tau) ^ {2}} + \frac {(1 + 2 \alpha \tau) ^ {2} (1 - \gamma) ^ {2} x _ {R} ^ {2}}{8 \tau (1 + \alpha \tau) (3 + 4 \alpha \tau) ^ {2}},\tag{20}
$$

where $\tau \in \{ \beta t , \gamma \epsilon \}$ and $( \gamma , \beta ) \in \{ ( 1 , \beta _ { c } ) , ( r , \beta _ { R } ) \}$ , with $\tau = \gamma \epsilon$ for quality-dominates-fit case and $\tau = \beta t$ for fitdominates-quality case and in each case with $( \gamma , \beta ) =$ $( 1 , \beta _ { c } )$ for the scenario without reviews and $( \gamma , \beta ) =$ $( r , \beta _ { R } ) f o r$ the scenario with reviews.

<sup>Proof.</sup> All proofs are in the appendix unless indicated otherwise.

We next examine the effect of online product reviews. We first discuss the effect in the qualitydominates-fit case and fit-dominates-quality case, and then we investigate the effect when reviews shift the nature of competition between the two cases. We can assert the effect by comparing equilibrium prices and profits between in the scenario without reviews and in the scenario with reviews. For the purpose of comparison, we next use the regular notations $( \mathrm { e . g . } , \pi _ { R } )$ for the scenario without reviews and use the notations with hats $( \mathrm { e } . \mathrm { g } . , \hat { \pi } _ { R } )$ for the scenario with reviews.

## 3.1. Quality-Dominates-Fit Case

Without loss of generality, we consider $x _ { R } \geq 0 ;$ that is, the online product reviews favor manufacturer A on the quality dimension.

<sup>Proposition</sup> <sup>1.</sup> In the quality-dominates-fit case, in the presence of online product reviews with $x _ { R } \geq 0 { : }$

(a) Product B’s wholesale price is lower and manufacturer B’s profit is lower; that is, $w _ { B } > \hat { w } _ { B }$ and $\pi _ { B } > \hat { \pi } _ { B } ;$

(b) Product A’s wholesale price is lower $( i . e . , w _ { A } > \hat { w } _ { A } )$ if and only if

$$
x _ {R} <   \frac {\epsilon (1 + 2 h) (3 + 4 \alpha r \epsilon)}{(1 + 4 \alpha \epsilon) (1 + 4 \alpha r \epsilon)};\tag{21}
$$

Manufacturer A’s profit is lower $\left( i . e . , \ \pi _ { A } > \hat { \pi } _ { A } \right)$ if and only if

$$
\begin{array}{c} x _ {R} <   \frac {\epsilon (1 + 2 h) (3 + 4 \alpha r \epsilon)}{(1 - r) (1 + 4 \alpha \epsilon)} \sqrt {\frac {(1 + 2 \alpha \epsilon) r}{(1 + 2 \alpha r \epsilon)}} \\ - \frac {r \epsilon (1 + 2 h) (3 + 4 \alpha r \epsilon)}{(1 - r) (1 + 4 \alpha r \epsilon)}; \end{array}\tag{22}
$$

(c) Product B’s retail price is lower and the retailer’s profit is higher; that is, $p _ { B } > \hat { p } _ { B }$ and $\pi _ { R } < \hat { \pi } _ { R } ;$ Product A’s retail price is lower $( i . e . , p _ { A } > \hat { p } _ { A } )$ if and only if

$$
x _ {R} <   \frac {2 \epsilon (1 + 2 h) (1 + \alpha r \epsilon) (3 + 4 \alpha r \epsilon)}{(1 + 4 \alpha \epsilon) (1 + 4 \alpha r \epsilon) (5 + 6 \alpha r \epsilon)}.\tag{23}
$$

In the symmetric case with $x _ { R } = 0 ,$ , we can verify that the conditions specified in the above proposition are all satisfied.

<sup>Corollary</sup> <sup>1.</sup> In the presence of the symmetric product reviews $( i . e . , x _ { R } = 0 )$ , (a) the wholesale prices and manufacturers’ profits are lower; that is, $w _ { i } > \hat { w } _ { i }$ and $\pi _ { i } > \hat { \pi } _ { i } ,$ $i \in \{ A , B \} ; ( \boldsymbol { \mathsf { b } } )$ the retail prices are lower and retailer’s profit is higher; that is, $p _ { i } > \hat { p } _ { i }$ and $\pi _ { R } < \hat { \pi } _ { R }$

The intuition for the symmetric case is as follows. In general, the online product reviews homogenize shoppers’ perceived quality differences and thus homogenize shoppers’ perceived utility differences. In the scenario without product reviews, each shopper’s perceived quality difference is from her own private assessment. In the scenario with reviews, the shopper combines her own assessment with the quality difference assessment revealed by the online product reviews. Because the quality difference revealed by the reviews is public and common to all shoppers, the presence of product reviews reduces the heterogeneity of shoppers’ perceived quality difference and thus reduces the heterogeneity of their perceived utility differences. Figure 2(a) illustrates the effect of the online product reviews on the perceived utility differences in this symmetric case. Because shoppers put some weight on the common component—perceived quality difference revealed by the reviews—in evaluating the utility differences, the span of their evaluations is reduced and thus the variance of their evaluations is reduced because of the product reviews. We call this effect variance-reducing effect.

The reduced heterogeneity in shoppers’ perceived utility differences between the two products makes the two products more substitutable overall and makes shoppers more price sensitive to a specific product, and thus it increases the competition between the two manufacturers. The increased substitutability and competition can also be seen from the demand functions. In this symmetric case, the demand functions in Equation (10) can be rewritten as

$$
\begin{array}{l} {D _ {A} = \frac {1 + 2 h}{2} - \alpha p _ {A} - \frac {1}{2 \gamma \epsilon} (p _ {A} - p _ {B}),} \\ {D _ {B} = \frac {1 + 2 h}{2} - \alpha p _ {B} - \frac {1}{2 \gamma \epsilon} (p _ {B} - p _ {A}).} \end{array}\tag{24}
$$

Note that the coefficient of the price difference term $( \mathrm { i . e . , ~ } 1 / ( 2 \gamma \epsilon )$ in the case) measures the substitutability between the two products: the larger the coefficient is, the more substitutable the two products are. The effect of online product reviews on the demand function is that it reduces  from 1 to r (where $r < 1 )$ , and thus it increases the substitutability between the two products. The increased competition between the two manufacturers drives their wholesale prices down as well as their profits. On the other hand, the retailer benefits from the increased competition between the two manufacturers. With the lower wholesale prices, the retailer lowers its retail prices, which increases the demand for each product. In addition, the lower wholesale prices leave the retailer with a higher profit margin from each sale, which explains why the retailer’s profit is increased by online product reviews.

In the general case as prescribed in Proposition 1, in addition to the variance-reducing effect, the online product reviews have another asymmetric effect on each manufacturer. The favorable quality information toward product A revealed by the reviews $( { \mathrm { i } } . { \mathrm { e } } . , x _ { R } > 0 )$ uniformly changes each shopper’s perceived quality difference between the two products favorably toward product A. As a result, in the presence of the favorable reviews toward product A, on average shoppers’ perceived utility differences between the two products are favorable for product A. We call this effect mean-shifting effect. Figure 2(b) illustrates such an effect. With favorable reviews for product A, shoppers are more likely to have a higher utility from product A. As a result, the mean of their perceived utility

(b) Mean-Shifting Effect $( x _ { R } = 1 )$

Figure 2 The Effect of Online Product Reviews in Quality-Dominates-Fit Case $( r = 0 . 4 , \epsilon = 7 , t = 0 . 2 , h = 3 . 6 , \alpha = 0 . 6 , \beta _ { C } = 0 . 5 ,$ and $\beta _ { R } = 0 . 6 )$

$$
(x _ {R} = 0)
$$

Probability density function of $\operatorname { E } ( U _ { A } - U _ { B } )$

![](/api/attachments/6UQ3EEJM/fulltext/images/24c8c229118f3788fdbe8ed0162e4826595263de8b7ae58e4131228e676a5a12.jpg)  
Probability density function of E(U<sub>A</sub> – U<sub>B</sub>)

differences is shifted toward the right-hand side and is changed favorably for product A. In the demand functions outlined in Equation (10), the mean shifting is reflected in the shifting from product $B ^ { \prime } { \sf s }$ potential market size to product $\bar { A ^ { \prime } } \mathrm { s }$ such that, compared to the symmetric case, manufacturer $A ^ { \prime } { \mathrm { s } }$ potential market size increases (from $( 1 + 2 h ) / 2$ to $[ ( 1 + 2 h ) / 2 +$ $( 1 - r ) x _ { R } / ( 2 r \epsilon ) ] )$ and manufacturer $B ^ { \prime } { \mathrm s }$ decreases (from $( 1 + 2 h ) / 2$ to $[ ( 1 + 2 h ) / 2 - ( 1 - r ) x _ { R } / ( 2 r \epsilon ) ] )$ . Manufacturer B suffers from the reduced potential market size resulting from unfavorable reviews, in addition to increased competition resulting from the variancereducing effect as in the symmetric case. As a result, the wholesale price for product B is reduced and manufacturer $B ^ { \prime } { \sf s }$ profit is lower because of the reviews.

For manufacturer $A ,$ the favorable reviews have a positive effect on its wholesale price and profit because of the boosted appeal in the market, whereas the increased competition resulting from the variancereducing effect has a negative effect. Whether the manufacturer can benefit from the reviews depends on the relative strength of the two effects. In general, more favorable reviews make the positive effect more significant, which in turn makes manufacturer A more likely to be better off from the reviews. When the reviews are highly favorable for A, compared to the scenario without reviews, the increased potential market size allows her to set a higher wholesale price without hurting the demand, which may compensate the loss from the increased competition and make manufacturer A better off. Inequalities (21) and (22) pinpoint the conditions, which essentially show that only if the reviews are favorable enough, the wholesale price and profit for manufacturer A become higher because of the reviews.

The retailer benefits from online product reviews both from the variance-reducing effect and from mean-shifting effect. First, as illustrated in the symmetric case, the variance-reducing effect intensifies the upstream competition, which, per se, reduces the wholesale prices and thus increases the profit of retailer. Second, the mean-shifting effect makes the downstream demand asymmetric in terms of their potential market sizes, which engenders more room for the retailer to exploit its market and benefits the retailer. For example, shifting the potential demand from product B to product A, per se, allows the retailer to charge a higher retail price for product $A$ and receive a higher realized demand for it, at the cost of a lower retail price with a lower realized demand for product B. Notice the gain from the increased price and increased demand for product A outweighs the loss from the decreased price and decreased demand for product B, because the changes in both the price and demand are more significant for product A than product B due to $A ^ { \prime } { \mathrm { s } }$ dominance in the market potential. Therefore, any increase of the degree of the asymmetry in the market potentials benefits the retailer. All together, the retailer obtains a higher profit in the presence of the reviews because of the benefits from both effects. The retailer charges a lower price for product B because of the lower wholesale price in the supply side and the lower demand in the demand side. The retailer may charge a higher or lower price for product A, depending on the balance between the variance-reducing effect and the mean-shifting effect, in which the variance-reducing effect tends to lower the price whereas the mean-shifting effect tends to increase the price.

![](/api/attachments/6UQ3EEJM/fulltext/images/5f412c2c804d5df9878b8bbee56592da428bb28a0d14ab70ede05588c0d2a6a6.jpg)

The condition for this quality-dominates-fit case to occur in equilibrium is that $\dot { t } < r \epsilon / \beta _ { R } - | x _ { R } | ( 1 - r )$ $[ 1 + 8 \alpha r \epsilon ( \bar { 1 } + \alpha r \epsilon ) ] / [ 2 \beta _ { R } ( 1 + \alpha r \epsilon ) ( 3 + 4 \alpha r \epsilon ) ]$ , which requires the weight t on the fit dimension is small such that the quality dimension plays a relatively more important role in determining shoppers’ perceived utility differences between the two products.

## 3.2. Fit-Dominates-Quality Case

As in the quality-dominates-fit case, without loss of generality, we consider $x _ { R } \geq 0 .$

<sup>Proposition</sup> <sup>2.</sup> In the fit-dominates-quality case, in the presence of online product reviews with $x _ { R } \geq 0 { : }$

(a) Product A’s wholesale price is higher and manufacturer A’s profit is higher; that is, $w _ { A } < \hat { w } _ { A }$ and $\pi _ { A } < \hat { \pi } _ { A } ;$

(b) Product B’s wholesale price is higher $( i . e . , w _ { B } < \hat { w } _ { B } )$ $i f$ and only $i f$

$$
x _ {R} <   \frac {t (\beta_ {R} - \beta_ {C}) (1 + 2 h) (3 + 4 \alpha \beta_ {R} t)}{(1 - r) (1 + 4 \alpha \beta_ {R} t) (1 + 4 \alpha \beta_ {C} t)};\tag{25}
$$

Manufacturer B’s profit is higher $( i . e . , \ \pi _ { B } < \hat { \pi } _ { B } )$ if and only if

$$
x _ {R} <   \frac {\beta_ {R} t (1 + 2 h) (3 + 4 \alpha \beta_ {R} t)}{(1 - r) (1 + 4 \alpha \beta_ {R} t)} - \frac {t (1 + 2 h) (3 + 4 \alpha \beta_ {R} t)}{(1 - r) (1 + 4 \alpha \beta_ {C} t)}
$$

$$
\cdot \sqrt {\frac {(1 + 2 \alpha \beta_ {C} t) \beta_ {C} \beta_ {R}}{(1 + 2 \alpha \beta_ {R} t)}};\tag{26}
$$

(c) Product $A ^ { \prime } s$ retail price is higher (i.e., $p _ { A } < \hat { p } _ { A } ) ;$ Product B’s retail price is higher $( i . e . , p _ { B } < \hat { p } _ { B } )$ if and only if

$$
x _ {R} <   \frac {2 t (\beta_ {R} - \beta_ {C}) (1 + 2 h) (1 + \alpha \beta_ {R} t) (3 + 4 \alpha \beta_ {R} t)}{(1 - r) (1 + 4 \alpha \beta_ {C} t) (1 + 4 \alpha \beta_ {R} t) (5 + 6 \alpha \beta_ {R} t)};\tag{27}
$$

The retailer’s profit is lower $( i . e . , \pi _ { R } > \hat { \pi } _ { R } )$ if and only if

$$
\begin{array}{c} x _ {R} ^ {2} <   \big (4 t ^ {2} \beta_ {R} (\beta_ {R} - \beta_ {C}) (1 + 2 h) ^ {2} (1 + \alpha \beta_ {R} t) (3 + 4 \alpha \beta_ {R} t) ^ {2} \\ \qquad \cdot \big [ 1 + 3 \alpha \beta_ {R} t + \alpha (3 + 8 \alpha \beta_ {R} t) \beta_ {C} t \big ] \big) \\ \qquad \cdot \big [ (1 - r) ^ {2} (1 + 2 \alpha \beta_ {R} t) ^ {2} (1 + 4 \alpha \beta_ {R} t) ^ {2} (1 + 4 \alpha \beta_ {C} t) ^ {2} \big ] ^ {- 1}. \end{array}\tag{28}
$$

In the symmetric case with $x _ { R } = 0$ , we can verify that the conditions derived in the above proposition are all satisfied.

<sup>Corollary</sup> <sup>2.</sup> In the presence of the symmetric product reviews $( i . e . , x _ { R } = 0 )$ , (a) the wholesale prices and manufacturers’ profits are higher; that is, $w _ { i } < \hat { w } _ { i }$ and $\pi _ { i } < \hat { \pi } _ { i } ,$ $i \in \{ A , B \} ;$ (b) the retail prices are higher and retailer’s profit is lower; that is, $p _ { i } < \hat { p } _ { i }$ and $\pi _ { R } > \hat { \pi } _ { R }$

The intuition for the symmetric case is as follows. Different from the quality dimension in which the true quality difference is the same for all shoppers and the product reviews add a common component in evaluating the quality difference across all shoppers, in the fit dimension shoppers have different preferences and online product reviews provide more information for them to further calibrate their own fits. With the additional information from reviews, shoppers’ signals are more accurate and they become less uncertain about their degrees of misfit than in the absence of reviews (from with probability $\beta _ { C }$ to with probability $\beta _ { R }$ revealing the true degrees of misfit). The reduced uncertainty thus makes shoppers more heterogeneous in terms of their perceived fits, which tends to increase the heterogeneity in shoppers’ perceived utility differences. Figure 3(a) illustrates the effect of the online product reviews on the perceived utility differences in this symmetric case. Contrary to the effect in the quality dimension, the information provided by the product reviews in the fit dimension tends to increase the variance of shoppers’ perceived utility differences. We call this effect variance-increasing effect.

The increased heterogeneity in shoppers’ perceived utility differences between the two products makes the two products less substitutable overall and makes shoppers less price sensitive to a specific product, and thus it softens the competition between the two manufacturers. The decreased substitutability and competition can also be seen from the demand functions. In this symmetric case, the demand functions in Equation (10) can be rewritten as

$$
\begin{array}{l} {D _ {A} = \frac {1 + 2 h}{2} - \alpha p _ {A} - \frac {1}{2 \beta t} (p _ {A} - p _ {B}),} \\ {D _ {B} = \frac {1 + 2 h}{2} - \alpha p _ {B} - \frac {1}{2 \beta t} (p _ {B} - p _ {A}).} \end{array}\tag{29}
$$

As discussed previously, the larger the coefficient of the price difference term $( \mathrm { i . e . , } 1 / ( 2 \beta t )$ in the case) ${ \mathrm { i } } { \mathrm { s } } ,$ the more substitutable the two products are. The effect of online product reviews on the demand function is that it increases $\beta$ from $\beta _ { C }$ to $\beta _ { R }$ and thus it decreases the substitutability between the two products. The softening of the competition between the two manufacturers increases their wholesale prices as well as their profits. On the other hand, the retailer hurts from the decreased competition between the two manufacturers. With the higher wholesale prices, the retailer increases its retail prices, which decreases the demand for each product. In addition, the higher wholesale prices leave the retailer with a lower profit margin from each sale, which explains why the retailer’s profit is decreased by online product reviews.

Figure 3 The Effect of Online Product Reviews in Fit-Dominates-Quality Case $( r = 0 . 6 , \epsilon = 1 , t = 7 , h = 3 . 6 , \alpha = 0 . 6 , \beta _ { C } = 0 . 7 , \tt { a n d } \beta _ { R } = 0 . 9 )$  
![](/api/attachments/6UQ3EEJM/fulltext/images/6110904d40657afc7f8f1d2c4ab2053845d376577c3a7df9322699fcf73e739c.jpg)

In the general case as prescribed in Proposition 2, in addition to the variance-increasing effect, as in the quality-dominates-fit case and as illustrated in Figure 3(b), the online product reviews also have asymmetric mean-shifting effect on each manufacturer. In the demand functions outlined in Equation (10), the mean shifting is reflected in an increase in manufacturer A’s potential market size (from $( 1 + 2 h ) / 2$ to $[ ( 1 + 2 h ) / 2 \dot { + } ( 1 - r ) x _ { R } / ( 2 \beta _ { R } t ) ]$ and a decrease in manufacturer B’s (from $( 1 + 2 h ) / 2$ to $[ ( 1 + 2 h ) / 2 -$ $( 1 - r ) x _ { R } / ( 2 \beta _ { R } t ) ]$ . Manufacturer A benefits from the favorable reviews and the resulting increased potential market size, in addition to softened competition resulting from the variance-increasing effect as in the symmetric case. As a result, the wholesale price for product A is increased and manufacturer A’s profit is higher because of the reviews.

For manufacturer $B ,$ the unfavorable reviews have a negative effect on its wholesale price and profit because of the reduced appeal in the market, whereas the softened competition resulting from the varianceincreasing effect, as in the symmetric case, has a positive effect. Whether the manufacturer can benefit from the reviews depends on the relative strength of the two effects. In general, less unfavorable reviews make the negative effect less significant, which in turn makes manufacturer B more likely to be better off from the reviews. When unfavorable reviews are mild, the softened competition effect dominates, which engenders the possibility for manufacturer B to charge a higher price and earn a higher profit compared to the case without reviews. Inequalities (25) and (26) pinpoint such conditions.

In the presence of favorable reviews for product A, the retailer charges a higher retail price for product A because of the increased wholesale price from the supply side and the enhanced demand from demand side. The retailer may charge a higher or lower price for product B, depending on the balance between the variance-increasing effect and the meanshifting effect, in which the variance-increasing effect tends to increase the price whereas the mean-shifting effect tends to decrease the price. Inequality (27) is the condition from such a trade-off. In terms of its profit, on the one hand, the retailer benefits from the mean-shifting effect of the product reviews, as in the quality-dominates-fit case. On the other hand, the retailer hurts from the variance-increasing effect of the product reviews. Inequality (28) shows that when the mean-shifting effect reflected by the magnitude of $x _ { R }$ is small, the product reviews are detrimental to the retailer’s profit.

The condition for this fit-dominates-quality case to occur in equilibrium is that

$$
t > \max \left\{\frac {\epsilon}{\beta_ {c}}, \frac {r \epsilon}{\beta_ {R}} + \frac {| x _ {R} | (1 - r) (1 + 8 \alpha \beta_ {R} t (1 + \alpha \beta_ {R} t))}{2 \beta_ {R} (1 + \alpha \beta_ {R} t) (3 + 4 \alpha \beta_ {R} t)} \right\},
$$

which requires the weight t on the fit dimension is large such that the fit dimension plays a dominant role in determining some shoppers’ perceived utility differences between the two products.

It is worth noting that the focus of this study is on the effect of product reviews on the upstream competition and the retailer. Although from this perspective our result suggests that in the fit-dominatesquality case retailer is hurt by online product reviews, our study does not preclude other possibilities that may offer retailers incentives to provide online product reviews even in the fit-dominates-quality case. For example, for some product categories, Amazon does not sell by itself and lets others sell directly to consumers for a commission on sales. In that case, Amazon simply provides a platform for other sellers and could benefit from reviews.

## 3.3. The Case When Reviews Change the Nature of Competition

So far, we have focused our discussion on the effect of online product reviews within the same qualitydominates-fit or fit-dominates-quality category. Under some conditions, online product reviews would shift the competition from one category to the other. We next use the symmetric case with $x _ { R } = 0$ to illustrate such a possibility and discuss the effect of online product reviews when this shift occurs.

First, we can verify that the shift in the nature of upstream competition from the fit-dominates-quality case to the quality-dominates-fit case cannot happen. We suppose that the competition without reviews is in the fit-dominates-quality category in which, compared to shoppers’ own assessment on the quality dimension, the fit dimension plays a dominant role in evaluating products. With the reviews, shoppers put some weight on the review’s assessment (indicating no quality difference) and put less weight on their own assessment in estimating the quality difference. The decreased weight on shopper’s own assessment of the quality makes the fit dimension more important and results in more determined shoppers who derive higher net utility from product A (B) regardless of her own perceived quality difference; that is, the marginal consumer $y _ { A } \left( y _ { B } \right)$ tends to be shifted toward the right (left) side because  is reduced from 1 to r in Equation (8). Therefore, the competition in the presence of the reviews cannot be shifted to the quality-dominates-fit category in which shoppers’ own assessment on the quality dimension plays a dominant role in evaluating products.

Next we derive the conditions under which online product reviews shift the competition from the quality-dominates-fit category to the fit-dominatesquality category, and then analyze the effect of online product reviews on the prices and each player’s profit.

Proposition 3. <sub>When</sub> $\beta _ { C } < \epsilon / t < \beta _ { R } / r ,$ (a) in the presence of the symmetric product reviews $( i . e . , \ x _ { R } = 0 )$ the competition between the two products is in the fitdominates-quality category, and in the absence of the reviews, the competition is in the quality-dominates-fit category; (b) if and only if $\beta _ { R } t < \epsilon ,$ the wholesale prices, retail prices, and manufacturers’ profits are lower with the product reviews $( i . e . , \ w _ { i } > \hat { w } _ { i } , \ p _ { i } > \hat { p } _ { i } ,$ , and $\pi _ { i } > \hat { \pi } _ { i } , \ i \in$ $\{ A , B \} )$ , and retailer’s profit is higher with the product reviews $( i . e . , \pi _ { R } < \hat { \pi } _ { R } )$

The condition $\beta _ { C } < \epsilon / t$ ensures that, in the absence of the reviews, the competition between the two products is in the quality-dominates-fit category, and the condition $\epsilon / t < \beta _ { R } \dot { / } r$ ensures that in the presence of the reviews, the competition between the two products is in the fit-dominates-quality category. Intuitively, when the precision of shoppers’ own assessments on the fit dimension is low and the variance of shoppers’ own assessment on the quality dimension is high, the competition in the no-review scenario is likely to fall under the quality-dominatesfit case, and when the precisions of reviews on quality and fit dimensions are high $( { \mathrm { i . e . , ~ } } \beta _ { R }$ and $( 1 - r )$ are high) such that shoppers’ own assessment on the quality dimension plays nondominant role the competition in the review scenario is likely to fall under the fit-dominates-quality case. The reason for the shift of competition from the quality-dominates-fit case to fit-dominates-quality case is, after reading reviews, shoppers put less weight on their own assessment on the quality dimension, and meanwhile shoppers’ signals are more accurate and they become less uncertain about their degrees of misfit. Therefore, the relative importance between the fit dimension and shoppers’ own assessment on the quality dimension can switch after and before reading reviews such that in the presence of reviews the fit dimension becomes to play a dominant role instead.

It is worth noting that what distinguishes the quality-dominates-fit case and fit-dominates-quality case is the relative importance between the fit dimension and shoppers’ own assessment on the quality difference in their comparative evaluation of products. Each case bears a different nature of competition, and a particular product category does not necessarily correspond to a specific case. For example, in evaluating a digital camera, shoppers may put more weight on quality rather than fit. However, the competition in the digital camera market can fall under either the quality-dominates-fit case or fit-dominates-quality case, and as indicated in Proposition 3, reviews can even shift the nature of the competition. For instance, for two digital cameras, one from Canon and the other from Sony, in the absence of reviews, shoppers’ own assessment on the quality difference may play a dominant role in their purchase decision. In the presence of symmetric reviews that accurately reveal the quality difference between the two cameras to be minimal, shoppers’ own assessment on the quality difference is no longer that important and shoppers’ perceived fit (e.g., shoppers’ preference about features and design) may play a dominant role. In this case, reviews shift the nature of competition from quality-dominates-fit case to fit-dominates-quality case.

When the competition is shifted from the qualitydominates-fit category to the fit-dominates-quality category, the substitutability of the products is also changed across the two categories. As illustrated in Equations (24) and (29), the degrees of substitutability in the quality-dominates-fit category and in the fitdominates-quality category are measured by $1 / ( 2 \gamma \epsilon )$ and $1 / ( 2 \beta t )$ , respectively. Therefore, without reviews the substitutability is $1 / ( 2 \epsilon )$ (because $\gamma = 1 )$ and with reviews the substitutability is $1 / ( 2 \beta _ { R } t )$ . When the former is less than the latter $( { \mathrm { i . e . , ~ } } \beta _ { R } t < \epsilon )$ , the substitutability of the products in the presence of the reviews is higher, and thus the wholesale prices and retail prices are lower, and manufacturers’ profits are lower. The retailer’s profit is higher because of the increased profit margin and increased demands, as discussed previously.

Corollary 1 and Proposition 3 offer surprising insights and implications regarding how review precision may affect the retailer. When the precision of shoppers’ own assessments on the fit dimension is low such that quality dominates fit without reviews, Corollary 1 shows that if review precisions are not too large such that in the presence of reviews quality continues to dominate fit, reviews benefit the retailer (because reviews intensify the upstream competition). On the other hand, when review precisions are high such that fit dominates quality and $\beta _ { R } t > \epsilon ,$ Proposition 3 demonstrates that reviews hurt the retailer (because reviews soften the upstream competition). This result shows that improving reviews’ precision can actually hurt the retailer by fundamentally altering the nature—from intensifying to softening—of upstream competition.<sup>7</sup>

The general asymmetric case can be similarly analyzed, but with more complexity. The additional complexity mainly comes from the mean-shifting effect discussed in the fit-dominates-quality case. For instance, if $\beta _ { R } t < \epsilon ,$ for the product with unfavorable reviews, its wholesale price, retail price, and the manufacturer’s profit are lower with product reviews, because the manufacturer suffers from the unfavorable comments as discussed previously, in addition to the negative effect from the increased substitutability associated with the transition to fit-dominates-quality case caused by reviews (as shown in Proposition 3). On the other hand, the manufacturer with favorable reviews balances between the negative effect from the increased substitutability and the positive effect from favorable comments toward its product. Whether the manufacturer is better off depends on the magnitude of the favorable reviews.

## 3.4. The Case When Manufacturers Do Not React to Reviews

By Propositions 1–3, it is worth highlighting that the manufacturer with favorable reviews on the quality dimension need not benefit from reviews and the manufacturer with unfavorable quality reviews is not necessarily harmed by reviews. In addition, the retailer can be harmed by product reviews, and in some cases, the harm occurs only when reviews have high precisions on the quality and fit dimensions. As explained in the discussions that follow the propositions, a reason for all our findings is the effect that online product reviews have on the upstream competition between manufacturers. The following result shows how reviews’ effects change if the strategic effects of reviews on manufacturers are ignored, that is, if manufacturers do not react to reviews and keep the same wholesale prices in both review and no-review scenarios. We continue to assume $x _ { R } \geq 0$ for this result.

<sup>Proposition</sup> <sup>4.</sup> If manufacturers do not react to reviews and keep the same wholesale prices in both review and no-review scenarios, in the presence of reviews, (a) retailer’s profit and manufacturer A’s profit are never lower, and (b) manufacturer B’s profit is never higher.

This result highlights the critical role played by reviews’ effects on upstream competition in the overall impact of reviews on various players in the channel. Under the assumption that only the retailer adjusts its pricing strategies in response to reviews and manufacturers do not, we obtain straightforward and apparently intuitive results regarding the effect of reviews on different players. Proposition 4 and the previous propositions clearly demonstrate that ignoring reviews’ effects on upstream players’ strategic responses to reviews can lead to incorrect conclusions about the impact of reviews on various players.

## 4. Conclusion

We examine the effect of online product reviews in a channel structure with a retailer selling substitutable products from competing manufacturers. We consider that consumers face uncertainty in both the product quality and fits to their needs, and product reviews provide additional information and reduce their uncertainties. Consumers agree on the preference order of the attributes in the quality dimension and have idiosyncratic preferences for the same attribute in the fit dimension. We identify the qualitydominates-fit case in which consumers’ own assessment on the quality dimension plays a dominant role in determining the perceived utility differences of the competing products and the fit-dominatesquality case in which the fit dimension plays a more important role. We demonstrated how the impacts of reviews on the retailer and manufacturers can be widely different and how these impacts can be different in the quality-dominates-fit and fit-dominatesquality cases. In the online appendix (available at http://dx.doi.org/10.1287/isre.2013.0511), we also show how the precisions in the quality and fit dimensions of the reviews and the relative weight of the fit dimension to the quality dimension affect the impacts of the reviews on the manufacturers and retailer.

Our research generates several managerial implications for online retailing. Online retailers have been deploying a variety of technologies and platforms to mitigate consumer uncertainty and match consumers with their preferred products. Online review platforms and recommendation systems are a few examples of these. Our research highlights that the effect of reviews on upstream competition is critical in determining the effects of reviews on various players in a channel. Ignoring reviews’ effects on upstream players’ strategic responses to reviews can lead to incorrect conclusions about the effect of reviews on various players. Our study thus illustrates that the effects of reviews cannot be determined in isolation, and calls for in-depth investigation of the effect of reviews on upstream competition in order to properly evaluate the overall effects of reviews on different players involved.

Our results also suggest the information revealed by reviews on the quality or fit dimension has different effects on the players in a channel. Retailers generally benefit from the information in the quality dimension revealed by reviews and therefore should welcome, encourage, and even induce consumers and/or third parties to generate relevant reviews. For instance, retailers should make the review platform easy to use to facilitate the review generating process, and, in particular, they may provide some review templates to direct users toward generating information about product qualities.

The incentive of manufacturers’ fostering reviews generation is not necessarily aligned with that of retailers. While retailers are incentivized to promote product reviews to reveal product qualities, manufacturers should encourage and induce information in the fit dimension in product reviews. Large manufacturers with bargaining power over retailers should influence or force retailers to direct consumers to generate information in the fit dimension on retailers’ review platforms. In addition, all manufacturers should encourage providing product specifics from consumers or third parties on their own review platforms (if any) or other third-party platforms.

Another implication of our findings is that the appropriate design of review platforms depends critically on the product type, because the nature of the upstream competition—whether consumers’ own assessment on the quality dimension or the fit dimension dominates the other dimension—calls for different design of review platforms, and each product type is likely to fall under a particular competition category. Therefore, our study underscores the importance for retailers and manufacturers to know the type each product belongs to before choosing features of the review platform. However, identifying the product type may not be straightforward. Recent research by Hong et al. (2012) proposes a mechanism based on product reviews to distinguish between search and experience goods, and their findings complement ours in achieving a more comprehensive understanding of impact of reviews on retailers and manufacturers.

Our results also have implications for further research on the effect of online reviews. Current empirical research mainly focuses on the effect of reviews using the sales/revenue data of retailers that sell to end consumers. Analytical research has also examined either monopoly sellers and competing firms that sell directly to end consumers. Results that show how reviews affect sales or the demand side of marketplaces provide only a partial characterization of the effect of reviews. We provide a first set of results that show the effect of reviews on both demand and supply sides in online marketplaces. Empirical tests on the hypotheses generated from our results would be an interesting future research direction. In addition, the focus of this paper is on the effect of online product reviews on manufacturers and retailers, and we do not study the effect of reviews on consumer surplus or social welfare. Another interesting research direction would be to systematically investigate how online reviews affect consumer surplus and social welfare.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2013.0511.

## Acknowledgments

The authors thank the detailed and constructive comments from the review team, which have greatly improved the paper. The authors also thank participants at the INFORMS Annual Meeting (2011), the INFORMS Conference on Information Systems and Technology (2012), and the Seventh China Summer Workshop on Information Management (2013), as well as seminar participants at Dalian University of Technology, University of Washington, The University of British Columbia, Idaho State University, University of Florida, The University of Cincinnati, University of Tulsa, and The University of Texas at Dallas for their helpful feedback. Jianqing Chen is the corresponding author and acknowledges the financial support from the National Science Foundation of China [NSFC 71273151].

## Appendix

## A.1. Derivation of Conditional Expectation of Misfit

<sup>Proof.</sup> The cumulative density function of s, conditional on the shopper’s true degree of misfit  being z, can be formulated as $P ( s \leq y ~ \vert ~ \lambda = z ) = ( 1 - \beta ) y + \beta H ( y - z )$ , where $H ( \cdot )$ is the Heaviside step function that evaluates to zero if the argument is negative, and to one otherwise. The corresponding probability density function is $P ( s = y \mid \lambda = z ) =$ $( 1 - \beta ) + \beta \delta ( y - z )$ , where $\delta ( x )$ is the Dirac delta distribution that satisfies

$$
\int_ {- \infty} ^ {\infty} \delta (x)   d x = 1 \quad \text { and } \quad \delta (x) = \left\{ \begin{array}{l l} 0 & \text { for } x \neq 0 \\ \infty & \text { for } x = 0. \end{array} \right.
$$

Using the Bayes’ Law,

$$
\begin{array}{c} P (\lambda = z \mid s = y) = \frac {P (s = y \mid \lambda = z) P (\lambda = z)}{P (s = y)} \\ = (1 - \beta) + \beta \delta (y - z), \end{array}\tag{30}
$$

and the conditional expectation is

$$
\begin{array}{r l} \mathrm{E} (\lambda \mid s = y) & = \int_ {0} ^ {1} \lambda [ (1 - \beta) + \beta \delta (y - \lambda) ] d \lambda \\ & = \int_ {0} ^ {1} (1 - \beta) \lambda d \lambda + \beta y = \frac {1 - \beta}{2} + \beta y. \quad \square \end{array}
$$

## A.2. Proof of Lemma 1

<sup>Proof.</sup> We denote $a _ { A } \equiv ( 1 + 2 h ) / 2 + ( 1 - r ) x _ { R } / ( 2 \tau ) , ~ a _ { B } \equiv$ $( 1 + 2 h ) / 2 - ( 1 - r ) x _ { R } / ( 2 \tau ) , \ b \equiv 1 / ( 2 \tau ) + \alpha , \mathrm { ~ a n d ~ } c \equiv 1 / ( 2 \tau )$ The demand functions in Equation (10) then can be rewritten as

$$
\begin{array}{c} {D _ {A} = a _ {A} - b p _ {A} + c p _ {B},} \\ {D _ {B} = a _ {B} - b p _ {B} + c p _ {A}.} \end{array}\tag{31}
$$

The retailer’s optimization problem in stage 2 is characterized by the first-order conditions of Equation (12):

$$
\frac {\partial \pi_ {R}}{\partial p _ {A}} = a _ {A} - 2 b p _ {A} + 2 c p _ {B} + b w _ {A} - c w _ {B} = 0,
$$

$$
\frac {\partial \pi_ {R}}{\partial p _ {B}} = a _ {B} - 2 b p _ {B} + 2 c p _ {A} + b w _ {B} - c w _ {A} = 0,
$$

from which we can derive the retailer’s optimal retail prices as functions of the wholesale prices:

$$
\begin{array}{r} p _ {A} = \frac {w _ {A}}{2} + \frac {a _ {A} b + a _ {B} c}{2 (b ^ {2} - c ^ {2})}, \\ p _ {B} = \frac {w _ {B}}{2} + \frac {a _ {B} b + a _ {A} c}{2 (b ^ {2} - c ^ {2})}. \end{array}\tag{32}
$$

The manufacturers’ optimization problems in stage 1 are characterized by the first-order conditions of Equation (13) (noticing that $p _ { i }$ in $D _ { i }$ is a function of w as in Equation (32)):

$$
\begin{array}{r l} & {\frac {\partial \pi_ {A}}{\partial w _ {A}} = a _ {A} - b p _ {A} + c p _ {B} - \frac {b}{2} w _ {A} = \frac {a _ {A}}{2} - b w _ {A} + \frac {c}{2} w _ {B} = 0,} \\ & {\frac {\partial \pi_ {B}}{\partial w _ {B}} = a _ {B} - b p _ {B} + c p _ {A} - \frac {b}{2} w _ {B} = \frac {a _ {B}}{2} - b w _ {B} + \frac {c}{2} w _ {A} = 0,} \end{array}
$$

from which we can derive the optimal wholesale prices:

$$
\begin{array}{r} w _ {A} = \frac {2 a _ {A} b + a _ {B} c}{4 b ^ {2} - c ^ {2}}, \\ w _ {B} = \frac {2 a _ {B} b + a _ {A} c}{4 b ^ {2} - c ^ {2}}. \end{array}\tag{33}
$$

Substituting the above optimal wholesale prices into Equation (32), we derive the optimal retail prices:

$$
\begin{array}{r} p _ {A} = \frac {2 a _ {A} b + a _ {B} c}{2 (4 b ^ {2} - c ^ {2})} + \frac {a _ {A} b + a _ {B} c}{2 (b ^ {2} - c ^ {2})}, \\ p _ {B} = \frac {2 a _ {B} b + a _ {A} c}{2 (4 b ^ {2} - c ^ {2})} + \frac {a _ {B} b + a _ {A} c}{2 (b ^ {2} - c ^ {2})}. \end{array}\tag{34}
$$

Substituting the above optimal retail prices into the demand functions in Equation (31), we have the equilibrium demands:

$$
\begin{array}{c} D _ {A} = a _ {A} - \frac {a _ {A} (2 b ^ {2} - c ^ {2}) - a _ {B} b c}{2 (4 b ^ {2} - c ^ {2})} - \frac {a _ {A}}{2} = \frac {(2 a _ {A} b + a _ {B} c) b}{2 (4 b ^ {2} - c ^ {2})}, \\ D _ {B} = a _ {B} - \frac {a _ {B} (2 b ^ {2} - c ^ {2}) - a _ {A} b c}{2 (4 b ^ {2} - c ^ {2})} - \frac {a _ {B}}{2} = \frac {(2 a _ {B} b + a _ {A} c) b}{2 (4 b ^ {2} - c ^ {2})}. \end{array}
$$

With the above equilibrium demands, the optimal wholesale prices in Equation (33), and the optimal retail prices in Equation (34), we have equilibrium profits:

$$
\begin{array}{r l r} & & {\pi_ {A} = w _ {A} D _ {A} = \frac {(2 a _ {A} b + a _ {B} c) ^ {2} b}{2 (4 b ^ {2} - c ^ {2}) ^ {2}},} \\ & & {\pi_ {B} = w _ {B} D _ {B} = \frac {(2 a _ {B} b + a _ {A} c) ^ {2} b}{2 (4 b ^ {2} - c ^ {2}) ^ {2}},} \\ & & {\pi_ {R} = (p _ {A} - w _ {A}) D _ {A} + (p _ {B} - w _ {B}) D _ {B}} \\ & & {= \frac {(a _ {A} - a _ {B}) ^ {2} b ^ {3}}{4 (b ^ {2} - c ^ {2}) (2 b + c) ^ {2}} + \frac {(2 a _ {A} b + a _ {B} c) (2 a _ {B} b + a _ {A} c) b ^ {2}}{2 (b - c) (4 b ^ {2} - c ^ {2}) ^ {2}}.} \end{array}
$$

Lemma 1 follows by substituting $a _ { A } , a _ { B } , b ,$ and c into the above optimal wholesale prices, retail prices, and equilibrium profits. <sup></sup>

## A.3. Proof of Proposition 1

<sup>Proof.</sup> By Lemma 1, with  =  we have the equilibrium outcome for the scenario without reviews and with $\tau = r \epsilon$ we have the equilibrium outcome for the scenario with reviews.

(a) Part (a) follows from that

$$
\begin{array}{l} w _ {B} = \frac {\epsilon (1 + 2 h)}{1 + 4 \alpha \epsilon} > \frac {\epsilon (1 + 2 h)}{1 / r + 4 \alpha \epsilon} \geq \frac {r \epsilon (1 + 2 h)}{1 + 4 \alpha r \epsilon} - \frac {(1 - \gamma) x _ {R}}{3 + 4 \alpha r \epsilon} = \hat {w} _ {B}, \\ \pi_ {B} = \frac {(1 + 2 \alpha \epsilon) \epsilon (1 + 2 h) ^ {2}}{4 (1 + 4 \alpha \epsilon) ^ {2}} > \frac {(1 + 2 \alpha r \epsilon) r \epsilon (1 + 2 h) ^ {2}}{4 (1 + 4 \alpha r \epsilon) ^ {2}} \\ = \frac {(1 + 2 \alpha r \epsilon) [ r \epsilon (1 + 2 h) (3 + 4 \alpha r \epsilon) ] ^ {2}}{4 r \epsilon (1 + 4 \alpha r \epsilon) ^ {2} (3 + 4 \alpha r \epsilon) ^ {2}} \\ \geq \frac {(1 + 2 \alpha r \epsilon) [ r \epsilon (1 + 2 h) (3 + 4 \alpha r \epsilon) - (1 + 4 \alpha r \epsilon) (1 - \gamma) x _ {R} ] ^ {2}}{4 r \epsilon (1 + 4 \alpha r \epsilon) ^ {2} (3 + 4 \alpha r \epsilon) ^ {2}} \\ = \hat {\pi} _ {B}, \end{array}
$$

where the last inequality is because $r \epsilon ( 1 + 2 h ) ( 3 + 4 \alpha r \epsilon ) >$ $( 1 + 4 \alpha r \epsilon ) ( 1 - \gamma ) x _ { R }$ by Equation (11).

(b) We notice that $w _ { A } > \hat { w } _ { A }$ if and only if

$$
w _ {A} - \hat {w} _ {A} = \frac {\epsilon (1 + 2 h)}{1 + 4 \alpha \epsilon} - \frac {r \epsilon (1 + 2 h)}{1 + 4 \alpha r \epsilon} - \frac {(1 - \gamma) x _ {R}}{3 + 4 \alpha r \epsilon} > 0,
$$

which leads to the condition in Inequality (21).

We notice that $\pi _ { A } > \hat { \pi } _ { A }$ if and only if

$$
\begin{array}{l} \pi_ {A} - \hat {\pi} _ {A} \\ = \frac {(1 + 2 \alpha \epsilon) \epsilon (1 + 2 h) ^ {2}}{4 (1 + 4 \alpha \epsilon) ^ {2}} \\ - \frac {(1 + 2 \alpha r \epsilon) [ r \epsilon (3 + 4 \alpha r \epsilon) (1 + 2 h) + (1 + 4 \alpha r \epsilon) (1 - \gamma) x _ {R} ] ^ {2}}{4 r \epsilon (1 + 4 \alpha r \epsilon) ^ {2} (3 + 4 \alpha r \epsilon) ^ {2}} \\ > 0, \end{array}
$$

which leads to the condition in Inequality (22).

(c) We have

$$
\begin{array}{l} p _ {B} = \frac {(1 + 6 \alpha \epsilon) (1 + 2 h)}{4 \alpha (1 + 4 \alpha \epsilon)} > \frac {(1 + 6 \alpha r \epsilon) (1 + 2 h)}{4 \alpha (1 + 4 \alpha r \epsilon)} \\ \geq \frac {(1 + 6 \alpha r \epsilon) (1 + 2 h)}{4 \alpha (1 + 4 \alpha r \epsilon)} - \frac {(5 + 6 \alpha r \epsilon) (1 - \gamma) x _ {R}}{4 (1 + \alpha r \epsilon) (3 + 4 \alpha r \epsilon)} = \hat {p} _ {B}, \\ \pi_ {R} = \frac {(1 + 2 \alpha \epsilon) ^ {2} (1 + 2 h) ^ {2}}{8 \alpha (1 + 4 \alpha \epsilon) ^ {2}} <   \frac {(1 + 2 \alpha r \epsilon) ^ {2} (1 + 2 h) ^ {2}}{8 \alpha (1 + 4 \alpha r \epsilon) ^ {2}} \\ \leq \frac {(1 + 2 \alpha r \epsilon) ^ {2} (1 + 2 h) ^ {2}}{8 \alpha (1 + 4 \alpha r \epsilon) ^ {2}} + \frac {(1 + 2 \alpha r \epsilon) ^ {2} (1 - \gamma) ^ {2} x _ {R} ^ {2}}{8 r \epsilon (1 + \alpha r \epsilon) (3 + 4 \alpha r \epsilon) ^ {2}} = \hat {\pi} _ {R}. \end{array}
$$

We notice that $p _ { A } > \hat { p } _ { A }$ if and only if

$$
\begin{array}{c} p _ {A} - \hat {p} _ {A} = \frac {(1 + 6 \alpha \epsilon) (1 + 2 h)}{4 \alpha (1 + 4 \alpha \epsilon)} - \frac {(1 + 6 \alpha r \epsilon) (1 + 2 h)}{4 \alpha (1 + 4 \alpha r \epsilon)} \\ - \frac {(5 + 6 \alpha r \epsilon) (1 - \gamma) x _ {R}}{4 (1 + \alpha r \epsilon) (3 + 4 \alpha r \epsilon)} > 0, \end{array}
$$

which leads to the condition in Inequality (23). <sup></sup>

## A.4. Proof of Proposition 2

<sup>Proof.</sup> By Lemma 1, with $\tau = \beta _ { C } t$ we have the equilibrium outcome for the scenario without reviews and with $\tau = \beta _ { R } t$ we have the equilibrium outcome for the scenario with reviews.

(a) Part (a) follows from that

$$
\begin{array}{l} w _ {A} = \frac {\beta_ {C} t (1 + 2 h)}{1 + 4 \alpha \beta_ {C} t} <   \frac {\beta_ {R} t (1 + 2 h)}{1 + 4 \alpha \beta_ {R} t} \\ \leq \frac {\beta_ {R} t (1 + 2 h)}{1 + 4 \alpha \beta_ {R} t} + \frac {(1 - \gamma) x _ {R}}{3 + 4 \alpha \beta_ {R} t} = \hat {w} _ {A}, \\ \pi_ {A} = \frac {(1 + 2 h) ^ {2} (1 + 2 \alpha \beta_ {C} t) \beta_ {C} t}{4 (1 + 4 \alpha \beta_ {C} t) ^ {2}} <   \frac {(1 + 2 h) ^ {2} (1 + 2 \alpha \beta_ {R} t) \beta_ {R} t}{4 (1 + 4 \alpha \beta_ {R} t) ^ {2}} \\ \leq (1 + 2 \alpha \beta_ {R} t) \big [ \beta_ {R} t (3 + 4 \alpha \beta_ {R} t) (1 + 2 h) \\ \qquad + (1 + 4 \alpha \beta_ {R} t) (1 - \gamma) x _ {R} \big ] ^ {2} \\ \cdot \big [ 4 \beta_ {R} t (1 + 4 \alpha \beta_ {R} t) ^ {2} (3 + 4 \alpha \beta_ {R} t) ^ {2} \big ] ^ {- 1} = \hat {\pi} _ {A}. \end{array}
$$

(b) We notice that $w _ { B } < \hat { w } _ { B }$ if and only if

$$
w _ {B} - \hat {w} _ {B} = \frac {\beta_ {C} t (1 + 2 h)}{1 + 4 \alpha \beta_ {C} t} - \frac {\beta_ {R} t (1 + 2 h)}{1 + 4 \alpha \beta_ {R} t} + \frac {(1 - \gamma) x _ {R}}{3 + 4 \alpha \beta_ {R} t} <   0,
$$

which leads to the condition in Inequality (25).

We notice that $\pi _ { B } < \hat { \pi } _ { B }$ if and only if

$$
\begin{array}{r l} \pi_ {B} - \hat {\pi} _ {B} = & \frac {(1 + 2 h) ^ {2} (1 + 2 \alpha \beta_ {C} t) \beta_ {C} t}{4 (1 + 4 \alpha \beta_ {C} t) ^ {2}} \\ & - (1 + 2 \alpha \beta_ {R} t) \big [ \beta_ {R} t (3 + 4 \alpha \beta_ {R} t) (1 + 2 h) \\ & - (1 + 4 \alpha \beta_ {R} t) (1 - \gamma) x _ {R} \big ] ^ {2} \\ & \cdot \big [ 4 \beta_ {R} t (1 + 4 \alpha \beta_ {R} t) ^ {2} (3 + 4 \alpha \beta_ {R} t) ^ {2} \big ] ^ {- 1} <   0, \end{array}
$$

which leads to the condition in Inequality (26).

(c) We notice that $p _ { A } < { \hat { p } } _ { A }$ because

$$
\begin{array}{l} p _ {A} = \frac {(1 + 6 \alpha \beta_ {C} t) (1 + 2 h)}{4 \alpha (1 + 4 \alpha \beta_ {C} t)} <   \frac {(1 + 6 \alpha \beta_ {R} t) (1 + 2 h)}{4 \alpha (1 + 4 \alpha \beta_ {R} t)} \\ \leq \frac {(1 + 6 \alpha \beta_ {R} t) (1 + 2 h)}{4 \alpha (1 + 4 \alpha \beta_ {R} t)} + \frac {(5 + 6 \alpha \beta_ {R} t) (1 - \gamma) x _ {R}}{4 (1 + \alpha \beta_ {R} t) (3 + 4 \alpha \beta_ {R} t)} = \hat {p} _ {A}. \end{array}
$$

We notice that $p _ { B } < \hat { p } _ { B }$ if and only if

$$
\begin{array}{l} p _ {B} - \hat {p} _ {B} = \frac {(1 + 6 \alpha \beta_ {C} t) (1 + 2 h)}{4 \alpha (1 + 4 \alpha \beta_ {C} t)} - \frac {(1 + 6 \alpha \beta_ {R} t) (1 + 2 h)}{4 \alpha (1 + 4 \alpha \beta_ {R} t)} \\ \qquad + \frac {(5 + 6 \alpha \beta_ {R} t) (1 - \gamma) x _ {R}}{4 (1 + \alpha \beta_ {R} t) (3 + 4 \alpha \beta_ {R} t)} <   0, \end{array}
$$

which leads to the condition in Inequality (27).

We notice that $\pi _ { R } > \hat { \pi } _ { R }$ if and only if

$$
\begin{array}{c} \pi_ {R} - \hat {\pi} _ {R} = \frac {(1 + 2 \alpha \beta_ {C} t) ^ {2} (1 + 2 h) ^ {2}}{8 \alpha (1 + 4 \alpha \beta_ {C} t) ^ {2}} - \frac {(1 + 2 \alpha \beta_ {R} t) ^ {2} (1 + 2 h) ^ {2}}{8 \alpha (1 + 4 \alpha \beta_ {R} t) ^ {2}} \\ - \frac {(1 + 2 \alpha \beta_ {R} t) ^ {2} (1 - \gamma) ^ {2} x _ {R} ^ {2}}{8 \beta_ {R} t (1 + \alpha \beta_ {R} t) (3 + 4 \alpha \beta_ {R} t) ^ {2}} > 0, \end{array}
$$

which leads to the condition in Inequality (28). <sup></sup>

## A.5. Proof of Proposition 3

<sup>Proof.</sup> (a) Here we consider the symmetric equilibrium $( \mathrm { i . e . , ~ } p _ { A } = p _ { B }$ in equilibrium). By the definition in Equation (8), $y _ { A } + y _ { B } = 1$ . So when $y _ { A } = ( - r \epsilon + \beta t ) / ( 2 \beta t ) > 0 ,$ the case falls under the fit-dominates-quality case and when $y _ { A } < 0 ,$ the case falls under the quality-dominates-fit case. Therefore, the scenario with reviews is in the fit-dominatesquality case if $r \epsilon < \beta _ { R } t ,$ , and the scenario without reviews is in the fit-dominates-quality case if $\beta _ { C } t < \epsilon$

(b) By Lemma 1, the equilibrium outcomes for both scenarios can be formulated in a uniform manner:

$$
\begin{array}{c} w _ {i} = \frac {\tau (1 + 2 h)}{1 + 4 \alpha \tau}, \quad p _ {i} = \frac {(1 + 6 \alpha \tau) (1 + 2 h)}{4 \alpha (1 + 4 \alpha \tau)}, \\ \pi_ {i} = \frac {(1 + 2 \alpha \tau) \tau (1 + 2 h) ^ {2}}{4 (1 + 4 \alpha \tau) ^ {2}}, \quad \pi_ {R} = \frac {(1 + 2 \alpha \tau) ^ {2} (1 + 2 h) ^ {2}}{8 \alpha (1 + 4 \alpha \tau) ^ {2}}, \end{array}
$$

where $i \in \{ A , B \}$ , and $\tau = \epsilon$ for the scenario without reviews and $\tau = \beta _ { R } t$ for the scenario with (symmetric) reviews. By checking the first-order derivatives, we can verify that $w _ { i } , p _ { i } ,$ , and $\pi _ { i }$ are increasing in . For instance,

$$
\frac {\partial w _ {i}}{\partial \tau} = \frac {1 + 2 h}{1 + 4 \alpha \tau} - \frac {4 \alpha \tau (1 + 2 h)}{(1 + 4 \alpha \tau) ^ {2}} = \frac {1 + 2 h}{(1 + 4 \alpha \tau) ^ {2}} > 0.
$$

We notice that $\pi _ { R }$ is decreasing because

$$
\begin{array}{c} \frac {\partial \pi_ {R}}{\partial \tau} = \frac {(1 + 2 \alpha \tau) (1 + 2 h) ^ {2}}{2 (1 + 4 \alpha \tau) ^ {2}} - \frac {(1 + 2 \alpha \tau) ^ {2} (1 + 2 h) ^ {2}}{(1 + 4 \alpha \tau) ^ {3}} \\ = - \frac {(1 + 2 \alpha \tau) (1 + 2 h) ^ {2}}{2 (1 + 4 \alpha \tau) ^ {3}} <   0. \end{array}
$$

The conclusions in Part (b) then follow. <sup></sup>

## A.6. Proof of Proposition 4

<sup>Proof.</sup> We denote as w the equilibrium wholesale price in no-review scenario (noticing $w _ { A } = w _ { B } )$ . The optimal retail prices in Equation (32), by substituting $a _ { A } , a _ { B } , b ,$ and c in, can be formulated as

$$
\begin{array}{l} {p _ {A} = \frac {w}{2} + \frac {1 + 2 h}{4 \alpha} + \frac {(1 - \gamma) x _ {R}}{4 (1 + \alpha \tau)},} \\ {p _ {B} = \frac {w}{2} + \frac {1 + 2 h}{4 \alpha} - \frac {(1 - \gamma) x _ {R}}{4 (1 + \alpha \tau)}.} \end{array}
$$

By substituting $p _ { A }$ and $p _ { B }$ into Equation (31), the demand functions can be formulated as

$$
\begin{array}{l} D _ {A} = \frac {1 + 2 h}{4} - \frac {\alpha w}{2} + \frac {(1 - \gamma) x _ {R}}{4 \tau}, \\ D _ {B} = \frac {1 + 2 h}{4} - \frac {\alpha w}{2} - \frac {(1 - \gamma) x _ {R}}{4 \tau}. \end{array}
$$

Notice that $\gamma = 1$ represents no-review scenario and $\gamma = r$ represent review scenario in the above formula. Therefore, the demand for manufacturer A is increased by $( 1 - r ) x _ { R } / ( 4 \tau )$ because of reviews and thus its profit is also increased. Similarly, the conclusion on manufacturer B follows. The retailer’s profit can be formulated as

$$
(p _ {A} - w) D _ {A} + (p _ {B} - w) D _ {B} = \frac {(1 + 2 h - 2 \alpha w) ^ {2}}{8 \alpha} + \frac {(1 - \gamma) ^ {2} x _ {R} ^ {2}}{8 \tau (1 + \alpha \tau)}.
$$

Therefore, the retailer’s profit is increased by $( 1 - r ) ^ { 2 } x _ { R } ^ { 2 } /$ $( 8 \tau ( 1 + \alpha \tau ) )$ because of reviews. <sup></sup>

## References

Archak N, Ghose A, Ipeirotis PG (2011) Deriving the pricing power of product features by mining consumer reviews. Management Sci. 57(8):1485–1509.

Bates JM, Granger CWJ (1969) The combination of forecasts. Oper. Res. Quart. 20(4):451–468.

Chen P-Y, Wu S-Y, Yoon J (2004) The impact of online recommendations and consumer feedback on sales. Proc. 25th Internat. Conf. Inform. Systems (ICIS). http://aisel.aisnet.org/icis2004/58/.

Chen Y, Xie J (2005) Third-party product review and firm marketing strategy. Marketing Sci. 24(2):218–240.

Chen Y, Xie J (2008) Online consumer review: Word-of-mouth as a new element of marketing communication mix. Management Sci. 54(3):477–491.

Chevalier JA, Mayzlin D (2006) The effect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Choi SC (1991) Price competition in a channel structure with a common retailer. Marketing Sci. 10(4):271–296.

Clemons EK, Gao GG, Hitt LM (2006) When online reviews meet hyperdifferentiation: A study of the craft beer industry. J. Management Inform. Systems 23(2):149–171.

Cone (2010) Consumers look online to verify purchase recommendations, even from their most trusted sources. Technical report, Cone Communications, http://www.coneinc.com/stuff/con -tentmgr/files/0/57cbc4124b1ea562f11290ad6dda9277/files/2010 \_online\_influence\_trend\_tracker\_factsheet\_final.pdf.

Dellarocas C (2006) Strategic manipulation of Internet opinion forums: Implications for consumers and firms. Management Sci. 52(10):1577–1593.

Deloitte and Touche (2007) Most consumers read and rely on online reviews; companies must adjust. Technical report. Deloitte and Touche via eMarketer, http://www.marketingcharts.com/ interactive/most-consumers-read-and-rely-on-online-reviews -companies-must-adjust-2234/.

Duan W, Gu B, Whinston AB (2008) The dynamics of online wordof-mouth and product sales—An empirical investigation of the movie industry. J. Retailing 84(2):233–242.

Forman C, Ghose A, Wiesenfeld B (2008) Examining the relationship between reviews and sales: The role of reviewer identity disclosure in electronic markets. Inform. Systems Res. 19(3): 291–313.

Garvin DA (1984) What does product quality really mean? Sloan Management Rev. 26(1):S25–S43.

Gu ZJ, Xie Y (2012) Facilitating fit-revelation in the competitive market. Management Sci. 59(5):1196–1212.

Hong Y, Chen P-Y, Hitt LM (2012) Measuring product type with dynamics of online product review variance. Proc. 33th Internat. Conf. Inform. Systems (ICIS). http://aisel.aisnet.org/icis2012/ proceedings/EconomicsValue/7/.

Jiang Y, Guo H (2013) Design of consumer review systems and product pricing. Working paper, Florida Gulf Coast University.

Jiang B, Srinivasan K (2011) Impact of online consumer reviews on competitive marketing strategies. Working paper, Carnegie Mellon University.

Jiang B-J, Wang B (2008) Impact of consumer reviews and ratings on sales, prices, and profits: Theory and evidence. Proc. 29th Internat. Conf. Inform. Systems (ICIS). http://aisel.aisnet.org/ icis2008/141/.

Johnson JP, Myatt DP (2006) On the simple economics of advertising, marketing, and product design. Amer. Econom. Rev. 96(3):756–784.

Kuksov D, Xie Y (2010) Pricing, frills, and customer ratings. Marketing Sci. 29(5):925–943.

Lewis TR, Sappington DEM (1994) Supplying information to facilitate price discrimination. Internat. Econom. Rev. 35(2):309–327.

Li X, Hitt LM (2008) Self-selection and information role of online product reviews. Inform. Systems Res. 19(4):456–474.

Li X, Hitt LM (2010) Price effects in online product reviews: An analytical model and empirical analysis. Management Inform. Systems Res. Quart. 34(4):809–831.

Li X, Hitt LM, Zhang ZJ (2011) Product reviews and competition in markets for repeat purchase products. J. Management Inform. Systems 27(4):9–42.

Liu Y (2006) Word of mouth for movies: Its dynamics and impact on box office revenue. J. Marketing 70(3):74–89.

Mayzlin D (2006) Promotional chat on the Internet. Marketing Sci. 25(2):155–163.

McCracken S (2011) Informative advertising under duopoly. Working paper, Australian National University.

Petriconi S (2012) Bank competition, information choice and inefficient lending booms. Working paper, Universitat Pompeu Fabra.

Ruckes M (2004) Bank competition and credit standars. Rev. Financial Stud. 17(4):1073–1102.

Shaffer G, Zettelmeyer F (2002) When good news about your rival is good for you: The effect of third-party information on the division of channel profits. Marketing Sci. 21(3):273–293.

Shin HS, Hanssens DM, Gajula B (2011) Positive vs. negative online buzz as leading indicators of daily price fluctuation. Working Paper, Long Island University.

Sun M (2012) How does variance of product ratings matter? Management Sci. 58(4):696–707.

Sun M, Tyagi R (2012) When does a manufacturer disclose product match information? Working paper, Boston University.

Sutton J (1986) Vertical product differentiation: Some basic themes. Amer. Econom. Rev. 76(2):393–398.

Villias-Boas JM (2004) Consumer learning, brand loyalty, and competition. Marketing Sci. 23(1):134–145.

Zhu F, Zhang XM (2010) Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. J. Marketing 74(2):133–148.

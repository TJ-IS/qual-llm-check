---
otero_id: 6644
otero_key: "MJGSYE6B"
title: "Deal-Seeking Versus Brand-Seeking: Search Behaviors and Purchase Propensities in Sponsored Search Platforms1"
authors: "Il Im; Jongkun Jun; Wonseok Oh; Seok-Oh Jeong"
year: "2016"
journal: "MIS Quarterly"
doi: "10.25300/misq/2016/40.1.08"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DEAL-SEEKING VERSUS BRAND-SEEKING: SEARCH BEHAVIORS AND PURCHASE PROPENSITIES IN SPONSORED SEARCH PLATFORMS<sup>1</sup>

Il Im School of Business, Yonsei University, 50 Yonsei-Ro, Seodaemun-Gu, Seoul KOREA 120-749 {il.im@yonsei.ac.kr}

Jongkun Jun Division of Global Business and Technology, Hankuk University of Foreign Studies, Yong-In KOREA 17035 {jkjun@hufs.ac.kr}

Wonseok Oh College of Business, Korea Advanced Institute of Science and Technology, 85 Hoegiro, Dongdaemun-gu, Seoul KOREA 130-722 {wonseok.oh@kaist.ac.kr}

Seok-Oh Jeong Department of Statistics, Hankuk University of Foreign Studies, Yong-In KOREA 17035 {seokohj@hufs.ac.kr}

Using a database of 11,001 unique sponsored search keywords, we investigate the relationship between the characteristics of keywords oriented around deal-seeking and brand-seeking and consumer search behaviors and buying propensities. On the basis of the search depth versus search breadth framework, we hypothesize that deal-seeking keywords elicit a search of greater breadth, whereas brand-seeking keywords induce a search of greater depth. We also explore the moderating effect of product type (search or experience goods) on the relationship between keyword characteristics and consumer search behaviors and how high-demand seasons (e.g., scheduled sales) influence consumers’ search and purchase behaviors. In addition, we estimate the effectiveness of keywords on the basis of their sales-per-cost performance. The findings indicate that search queries containing deal-seeking keywords are associated with higher click-through rates and conversion rates than are search queries without such keywords. We also find that the positive effect of deal-seeking keywords on click-through rates is more pronounced for experience goods than for search goods. However, we identify a negative interaction between experience goods and brand-seeking keywords. A comparison of deal-seeking and brand-seeking keywords in terms of cost effectiveness reveals that deal-seeking keywords generate approximately three times the sales of those produced by brand-seeking keywords.

Keywords: Sponsored search, deal-seeking, brand-seeking, experience goods, click-through rate, conversion rate, hierarchical generalized linear model, propensity score weighting

## Introduction

Sponsored search platforms are arguably the most profitable business models in the history of e-commerce. Given the advent of new IT/mobile infrastructures as well as the enthusiastic adoption of search tools by thriving social media companies, search volumes are expected to grow on a scale and at a pace never before witnessed. In response to consumers’ increased use of sponsored searches, online advertisers are moving quickly to optimize their marketing performance and exploit the opportunities presented by new digital platforms. In academic circles, research on the sponsored search phenomenon (e.g., Agarwal et al. 2011; Animesh et al. 2010; Ghose and Yang 2009) has proliferated at a rate commensurate to its increasing importance as a business value proposition. These studies have provided many valuable insights into the adoption, design, and implementation of commercial advertising campaigns in online sponsored searches.

Although valid and useful, these scholarly investigations focus primarily on holistic inquiry into consumers’ search preferences and behaviors; that is, they provide empirical results that are aggregated over different product categories and consumer characteristics. Consequently, the question remains unclear as to the manner by which consumer- and product-specific characteristics govern consumers’ search patterns. Researchers have communicated the need to address these issues. Some (e.g., Agarwal et al. 2011; Rutz and Trusov 2011) have criticized existing research as universally assuming that consumers are homogeneous in terms of their preferences and responses to paid search mechanisms. Others (e.g., Animesh et al. 2010; Ghose and Yang 2009) have questioned the extent to which different product characteristics affect click-through rates (CTRs) and conversion rates (CRs). Given that consumers’ search behaviors are highly dependent on and driven by product- and consumer-specific characteristics, a more nuanced investigation of these issues is in order. The current work represents one such attempt.

We delve into the behavior of online consumers who seek “great deals” in the form of low prices (e.g., bargain hunters) or who confine their explorations to specific brands (e.g., Nike, Hyatt, Levi’s), questioning whether they search differently from those who do not. Because consumers’ search objectives are likely to influence their search behaviors and preferences, these consumer-specific factors are expected to affect the choice and purchase decisions, as measured by CTRs and CRs, respectively. To refine our efforts, we examine two specific product attributes that are touted as the two main indicators of purchase decisions (Brucks et al. 2000; Degeratu et al. 2000; Dodds and Monroe 1985; Dodds et al. 1991). These attributes are price (deal-seeking) and brand name (brand-oriented). We explore how search queries comprising diverse combinations of keywords that reflect these two attributes influence consumers’ search behaviors and purchase propensities. Additionally, we examine whether the difficulty associated with obtaining product quality information prior to purchase shapes the manner through which deal-seeking or brand-oriented consumers search and make purchase decisions in sponsored search channels.

Using the search depth versus search breadth framework (Jacoby et al. 1977; Novak and Hoffman 1997; Ozanne et al. 1992; Tauscher and Greenberg 1997), we pursue the following research questions: How do deal-seeking and brandseeking keywords differ in terms of the CTRs and CRs they generate? How does product type (e.g., search goods versus experience goods) moderate the effects of product attributes on consumers’ search behaviors? To what extent do searches containing keywords that reflect prices and brand names perform better (or worse) than do searches with keywords that comprise only one of the two attributes? Finally, how do high-demand periods (e.g., sales and promotions) influence consumer search patterns that are characterized by depth and breadth?

To validate our hypotheses, we obtained search transaction data from an online advertising agency that specializes in sponsored searches. The data set comprises 11,001 unique keywords that were entered directly by users through major sponsored search platforms and data on a variety of search performance measures. To analyze the data accurately, we used hierarchical generalized linear modeling (HGLM) as the primary econometric approach. This method offers the most unbiased and efficient means of estimating and validating hypotheses. To verify causal inference, we employed the doubly robust (DR) estimator and propensity score weighting method (Bang and Robins 2005; Funk et al. 2011). Our empirical analyses yield practical insights for managers in terms of designing effective keyword-based bidding strategies and maximizing returns from sponsored search investments.

## Related Research

Scholars in diverse disciplines, including information systems and marketing, have inquired into a variety of topics germane to sponsored search advertising. These topics are probed through research that falls under at least three central categories. The first concentrates on the key factors that affect performance in sponsored search platforms. For example, Ghose and Yang (2009) investigated the degree to which various keyword-specific factors influence several dimensions of search performance. By concentrating exclusively on the top search keywords used in the ringtone industry, Rutz and Trusov (2011) demonstrated that keywords appearing in headlines positively influence CTRs, whereas those that are displayed in the body copy do not. In a field experiment, Agarwal et al. (2011) examined the effect of ad position on CTRs and CRs. The results illustrate that top-ranked advertisements do not necessarily generate higher profits than those earned by low-grade advertisements.

The second research stream addresses the dynamic interplay of and substitution between sponsored search advertising and other advertising formats, such as offline advertising and organic search engine markets. Goldfarb and Tucker (2011) investigated the relationship between sponsored advertising and offline advertising to illustrate that the former replaces, rather than complements, the latter. Yang and Ghose (2010) found a positive association between CTRs on sponsored search advertisements and those on organic search listings. Nicholson et al. (2006), who compared the number of search results from organic and sponsored searches, revealed that 82 percent of organic listings on the first results pages are not registered on the sponsored search.

The third body of research centers on advertisers’ strategic bidding behaviors aimed at securing top positions on search result pages. Underpinning their work with the auctions framework, some researchers have scrutinized the numerous factors at play in advertisers’ dynamic bidding preferences and strategic designs for sponsored search formats. Chaitanya and Narahari (2012) developed budget and bid optimization models for advertisers who contend with unpredictable and unstable keyword traffic. Similarly, Chen et al. (2009) proposed optimal bidding designs and strategies for a specific group of advertisers (e.g., advertisers with limited bidding experience) and looked into how bidding trajectories influence performance, search engine companies’ revenues, and overall auction efficacies in paid search platforms.

## Hypotheses Development

## Search Orientations: Depth Versus Breadth

Search and information processing generally has two core dimensions. In search and information processing that is regulated by breadth, the focal outcome is the number of different attributes acquired and processed, whereas in search and information processing for which depth is a standard, the outcome of interest is the amount of time devoted to each attribute (Jacoby et al. 1978, Novak and Hoffman 1997,

Tauscher and Greenberg 1997). Due to limited resources (e.g., time devoted to search activities) and the heterogeneity inherent in search objectives and expectations, consumers exhibit different search patterns (Huang et al. 2009; Ozanne et al. 1992). For example, consumers may seek the retailer who offers the lowest price for a product available from many vendors by initiating a “breadth of information” search. The search costs associated with ascertaining price information are significantly lower in online environments (Bakos 1997). Consumers who are typically price-sensitive and familiar with product quality may visit many stores in an attempt to maximize economic benefits (Lynch and Ariely 2000). By contrast, many other consumers conduct in-depth searches mainly to acquire detailed quality information and improve their ability to evaluate available options. Owing to time constraints, these knowledge- and information-seeking consumers may moderate the scope and scale of their searches by visiting only a limited number of stores (Urbany et al. 1989).

The cost or effort involved in searching for information has been recognized as one of the key factors that influence the breadth and depth of information searches (Dennis and Taylor 2006). From a search cost perspective, with all factors being equal, a price search costs less than a quality search because a smaller amount of cognitive effort is required for the former than for the latter (Lynch and Ariely 2000). In this respect, we postulate that deal-seeking consumers are likely to prioritize search breadth, whereas brand-seeking consumers are expected to focus on search depth.

## Deal-Seeking Propensities and Search Performance

Depending on consumer type, price may function either as a key determinant or as a negligible factor in purchase decision making (Tellis 1988). The extent of sensitivity to price generally determines the level of search that a consumer will perform (Mehta et al. 2003). Deal-seeking consumers are predisposed toward extensive searches in their desire to find low prices and maximize economic benefits. Sponsored search engines allow consumers to enter price-related terms (e.g., sale, discounts, and bargains) or phrases (e.g., lowest prices, best deals) in addition to main keywords that indicate products or services. This feature facilitates effortless identification of sellers who offer “great deals.”

In situations where consumers are fully aware of the quality and other non-price attributes of a product in question, they can simply canvass multiple retailers in the pursuit of sizeable economic gains. Alternatively, when consumers are confronted with considerable uncertainty in determining product quality prior to purchase, they are likely to exhibit price sensitivity (risk aversion) behaviors, in which they opt for the lowest price to shield themselves from potential losses (Degeratu et al. 2000). Regardless of the variations in motivational causes, consumers with high deal-seeking propensities may expand their “consideration set” (Howard and Sheth 1969) to recognize the full distribution of a product’s price. In this regard, we expect the broader search pattern espoused by deal-seeking individuals to lead to higher CTRs. Using Internet clickstream data, Moe (2006) found that online buyers first attempt to winnow their choices down from among a multitude of options and then use more precise rules to evaluate a derived subset of choices before making a final purchase decision. The findings of that study indicate that online consumers deliberate more intensively over price late in the decision-making process rather than in the early stages.

Because deal-seeking consumers have high purchase intent (Gilbride and Allenby 2004), they survey multiple vendors to learn as much as they can about a product’s price and maximize economic gain. The higher the number of stores visited, the greater the benefits accrued (Stiger 1961). Consumers seeking low prices are therefore more strongly motivated than casual consumers to click on the options displayed in sponsored search results. These customers exhibit higher CTRs for search terms that include deal-seeking attributes. Furthermore, on account of deal-seeking consumers’ high purchase motivation (Gilbride and Allenby 2004), when all else is equal, we expect that they exhibit higher CRs than those presented by non-deal-seeking consumers. Accordingly, we posit the following:

H1a: Searches that include deal-seeking keywords result in higher CTRs than do those excluding such keywords.

H1b: Searches that contain deal-seeking keywords result in higher CRs than do those without such terms.

## Brand-Seeking Propensities and Search Performance

Defined as “a name, symbol, design, or mark that enhances the value of a product beyond its functional value” (Farquhar 1989, p. 24), a brand has been viewed as one of the most significant influencing factors for consumer search behavior and purchase intent (Rao and Monroe 1989). Brands afford consumers a sense of security (Jacoby et al. 1977) and build trust (Chaudhuri and Holbrook 2001), which have both been shown to engender purchase loyalty. We assert that a brandseeking consumer focuses more intensely on the depth rather than the breadth of a search for several reasons. Consumers who are loyal to a particular brand are generally less price sensitive than consumers who are not (Krishnamurthi and Raj 1991; Narayandas 1998). Additionally, brand seekers are often characterized as tending to avoid complicated procedures in favor of simplified search and purchase heuristics (Neslin et al. 2014). Furthermore, because brand-seeking consumers may rely heavily on organic search results to obtain seemingly more objective information, they are unlikely to exhibit exhaustive search patterns in sponsored search environments. Given that such consumers are less responsive to price and more focused on a simple, narrow search, they are inclined to limit their search space and consideration set to only a few sellers (Urbany et al. 1989). The in-depth approach is therefore likely to emerge as the main search mechanism for consumers seeking branded products. Consequently, we postulate that brand-seeking consumers may generate relatively lower CTRs than those who do not seek particular brands.

Many studies revealed that brand names have a significant influence on buyers’ perceptions of product quality and that buyers with specific brand names in mind tend to purchase products more readily (Dodds et al. 1991). Jacoby et al. (1977) confirmed that a brand name is the most important information dimension that consumers consider before arriving at final purchase decisions. We aver that searches containing brand name keywords produce relatively higher CRs than do searches that exclude such keywords. This phenomenon is attributed to a number of factors. Evaluating brand quality or obtaining detailed brand information necessitates significant cognitive processing (Krishnamurthi and Raj 1991), which may naturally limit consumers’ search scope and resources. From the standpoint of quality assessment, brand names themselves often signal high quality and popularity (Caminal and Vives 1996; Zhu and Zhang 2010). Given that a product’s popularity signals social cues and that compliance with social cues can reduce perceived risk, consumers may tend to favor branded products over non-brand items. Similarly, in decision-making situations, many consumers feel strongly rewarded and often obtain optimal purchase outcomes when simply following the crowd instead of acting on private information (Banerjee 1992; Bikhchandani et al. 1992). Finally, although not all landing pages offer product reviews, more product reviews are available for brand products than for their lesser known counterparts (Li and Hitt 2008). Online product reviews have become important contextual resources with extensive influence on consumers purchase decisions (and therefore CRs). Consequently, consumers whose search strings include brand-seeking keywords are expected to exhibit higher CRs than consumers whose search queries exclude such keywords. In line with these considerations, we put forward the following hypotheses:

H2a: Lower CTRs result from searches that contain brand-seeking keywords than from searches excluding such keywords.

H2b: Higher CRs result from searches that comprise brand-seeking keywords than from searches without such keywords.

Perceived uncertainty may vary not only by the availability of additional attribute information (e.g., price, brand name), but also by the characteristics of a product. Some products are, by nature, highly uncertain and difficult to evaluate ex ante. To reflect the varying degrees of uncertainty inherent to products, Nelson (1970) identified two broad product classes, namely, search and experience goods. Search goods typically refer to those goods for which the attributes that are most critical to the evaluation of product quality can be assessed before purchase. Contrastingly, experience goods are characterized as commodities for which crucial attributes can be discovered only after use.

## Moderating Effects of Product Type and Demand Volume

The structural difference between these two product categories affects the dynamics of consumers’ perceived uncertainty in relation to search and purchase behaviors in a sponsored platform context. Huang et al. (2009) suggested that search attributes elicit a greater breadth of search (i.e., more product pages visited at a given time), whereas experience attributes induce a greater depth of search (i.e., more time spent per product page). Retrieving price information can be facilitated under conditions where the search costs and cognitive loads are low. In their quest for optimal economic outcomes, deal-seeking consumers who buy experience goods online may be motivated to increase the breadth of their searches further by evaluating a larger pool of retailers. Because experience goods exhibit higher variations than search goods in terms of price and quality (Nelson 1970), we posit that deal-seeking consumers will engage in more intensive search activities when purchasing experience goods, as doing so increases the marginal value of a search. Conversely, evaluating brands involves significant cognitive information processing and high search costs (Degeratu et al. 2000). Given the high search costs and cognitive effort associated with evaluating the brand names of experience goods, brand-seeking consumers may choose to engage in more exhaustive searches and reduce their search scope accordingly. As a result, we expect a greater negative interaction between experience goods and brand-seeking keywords. These arguments lead us to postulate that

H3a: The positive effect of deal-seeking keywords on CTRs is more pronounced for experience goods than for search goods.

H3b: The negative effect of brand-seeking keywords on CTRs is more pronounced for experience goods than for search goods.

## Methods

## Data

To validate our hypotheses empirically, a sizeable volume of data was collected from an established online advertising agency<sup>2</sup> that specializes in sponsored search marketing. This company serves a wide range of clients, including online retailers, specialty apparel manufacturers, and travel agents. Its portfolio of services includes tracing of sponsored link activities on the basis of performance measures, such as exposures, clicks, and purchases. Our data set contains a comprehensive list of consumer search transactions that were processed through sponsored search engine channels from February to October 2010. These channels are the dedicated systems of one of the world’s largest online retailers (Company XYZ), which has several successful sister companies, including nationwide department stores, discount outlets, and convenience shops. The data set obtained from Company XYZ includes a number of paid search attributes, such as channels (search engines), keywords, frequency of exposure, number of clicks, average rankings of keywords over a given period, cost per click, and number (and value) of purchases. As Company XYZ is a leading online retail portal, it offers all kinds of consumer retail products, from apparel and food to electronic appliances. The data were collected on a weekly basis, consistent with the method adopted in previous studies (e.g., Ghose and Yang 2009). The final data set comprises 11,001 unique keywords, offering an empirical base that is approximately six times larger than the 1,878 keyword selection employed by Ghose and Yang (2009).

## Coding

Manual coding was performed for the data in this study. As a result of this coding, several independent variables (e.g., experience/search goods, deal-seeking) representing product attributes were identified. The coding task was carried out by 16 undergraduate students majoring in business administration. The coding scheme was constructed as follows. A search term was coded as a deal-seeking keyword if it contained any words or phrases related to consumers’ price consciousness, such as sale, deal, cheapest, low price, and/or outlet. Similar procedures were employed to identify brand names. Regarding the classification of product types, in accordance with the methods used in prior literature (Huang et al. 2009; Mudambi and Schuff 2010; Nelson 1970), keywords for the products whose quality can be evaluated prior to purchase were classified as those representing search goods. In contrast, keywords referring to products whose quality cannot be assessed accurately before purchase were categorized as experience goods (see Table 1 for specific coding scheme and sample products). Finally, keywords that could not be evaluated accurately, as they do not represent products (e.g., store location) were classified as “N/A” and excluded from the analysis.<sup>3</sup>

## Analytic Approaches and Variable Description

The data in this study represent users’ search behaviors in relation to paid search advertisements. A keyword can be searched repeatedly via an engine that returns different rankings or through various search engines. The data set used in this work is therefore nested and hierarchically structured. With respect to determining hierarchies in multilevel models of repeated-measures data, the measurements constitute the first level and the individuals measured make up the second (Maas and Snijders 2003; Van Der Leeden 1988). Correspondingly, we categorized occasional parameters (e.g., rank and channel) into the first level and the characteristics of individual keywords (e.g., keywords related to deal seeking or brand names) into the second level. Several control variables were also assigned to the second level to control for the possible effects of these factors.

The literature indicates that hierarchical generalized linear model (HGLM) analysis, which is an extension of the hierarchical linear model (HLM) method (Raudenbush and Bryk 2002; Taşoluk et al. 2011), is an ideal statistical technique under the following conditions: (1) when the dependent variable is contingent on binomial distribution; (2) when independent and dependent variables are linearly related; and (3) when the normality of random effects is preserved. The dependent variables in our model are determined on the basis of binomial distribution and are assumed to be linearly associated with the independent variables (e.g., rank). In addition, the random error is assumed to be normally distributed. As can be deduced from the description above, the HGLM is an ideal mechanism for elucidating the circumstances that prompted this study and for fulfilling the objective of the research. Ordinary least squares (OLS) estimations are unsuitable in our case because employing such methods to analyze nested data violates the assumption of observational independence. Loss of information is also likely to occur when the OLS method is used to examine hierarchical data (Raudenbush and Bryk 2002).

Table 2 describes the independent variables incorporated into the model. Using previously adopted methods as bases (e.g., Taşoluk et al. 2011), we analyzed dichotomous variables (e.g., search engine and product type) without centering and centered continuous variables (e.g., rank) according to the grand-mean centering method (Kreft et al. 1995). In the HGLM, the level 1 model consists of three components: a sampling model (Equation (1)), a link function (Equation (2)), and a structural model (Equations (4)–(7)).

## Modeling Click-Through Rates (CTRs)

CTR (the total number of clicks divided by the total number of exposures) is adopted as the dependent variable for Level 1. If $Y _ { i j }$ (the total number of clicks for search keyword i at observation $^ { 4 } j )$ is assumed to follow a random probability distribution, then the sampling model can be stated as follows:

$$
Y _ {i j} | P _ {i j} \sim B \left(m _ {i j}, P _ {i j}\right)\tag{1}
$$

where $Y _ { i j }$ is the total number of clicks among $m _ { j i }$ (the total number of exposures). Since $Y _ { i j }$ represents the ratio of the number of clicks to the number of exposures $( m _ { i j } )$ , and $P _ { i j }$ indicates the probability of clicking as a result of each exposure, $Y _ { i j }$ follows a binomial distribution. The logit link function, after taking $P _ { i j }$ as log-odds, is as follows:

$$
\begin{array}{r l} \eta_ {i j} = & \ln \left(\frac {p _ {i j}}{1 - p _ {i j}}\right) = \beta_ {i 0} + \beta_ {i 1} \text {Rank} _ {i j} + \beta_ {i 2} \text {Channel} _ {-} B _ {i j} \\ & + \beta_ {i 3} \text {Channel} _ {-} C _ {i j} \end{array}\tag{2}
$$

Table 1. Coding Scheme and Sample Products (Search/Experience Goods)

<table><tr><td></td><td>Search goods</td><td>Experience goods</td></tr><tr><td>Coding criteria</td><td>products for which consumers have the ability to obtain information on their quality prior to purchasekey attributes are quantifiable, objective, and easily comparedconsumers do not have to use their own senses to evaluate quality</td><td>products that require consumers to purchase (or obtain samples) in order to evaluate their qualitykey attributes are subjective or difficult to compare and quantifyconsumers must use their own senses to determine quality</td></tr><tr><td>Sample products</td><td>photo frame, toys, key chain, mirror, USB memory, notebook bag, stand lamp, storage box, trash bin, towel hanger, stapler, whiteboard, binder, umbrella, TV table, hair band, laundry rack, water bottle, drawers, rice cooker</td><td>food, travel package, hotels, massage tools, diapers, wine, yoga class, hair shops, book, music album, teeth whitening service, DVD, skin care service, hair growth solution, home sauna, cosmetics, carpet cleaning service, flowers</td></tr></table>

Table 2. Descriptions of Independent Variables

<table><tr><td>Level 1</td><td>Descriptions</td></tr><tr><td>Rank</td><td>Rank is a continuous variable. It is a weighted average of ranks for each keyword in a given time period (one week in this study).</td></tr><tr><td>Channel (search engine)</td><td>All search activities occur through three search engine channels. Channel A is used as a base. Channel_B is coded 1 if search activities occur through Channel B and 0 if otherwise. Channel_C is coded 1 if search activities occur through Channel C and 0 if otherwise.</td></tr><tr><td>Level 2</td><td>Descriptions</td></tr><tr><td>DealSeeking</td><td>DealSeeking is a dichotomous variable, coded 1 if the keyword contains price-related words and 0 otherwise.</td></tr><tr><td>Brand</td><td>Brand is a dichotomous variable, coded 1 if the keyword contains a brand name and 0 otherwise.</td></tr><tr><td>ExpGoods</td><td>ExpGoods is a dichotomous variable, coded 1 if the keyword indicates experience goods and 0 otherwise.</td></tr><tr><td>KeywordLength</td><td>KeywordLength is a continuous variable, coded as the counted number of characters in a keyword.</td></tr></table>

The estimation of log-odds $( \eta _ { i j } )$ in Equation (2) can be transformed to a predicted probability through the logistic function below:

$$
P _ {i j} = \frac {\exp \left(\eta_ {i j}\right)}{1 + \exp \left(\eta_ {i j}\right)}\tag{3}
$$

The Level 2 model represents a structural model formulated to test the hypotheses. We investigate whether or not the coefficients in Equation (2) are affected by the keyword characteristics modeled in Equations (4), (5), (6), and (7). Equation (4) was modeled to test whether intercept $\beta _ { i 0 }$ varies according to keyword characteristics. Dummy variables representing product categories are entered as covariates. Equations (5), (6), and (7) were modeled as simple random coefficients in order to determine the effects of rank and channel.

$$
\begin{array}{r l} \beta_ {i 0} & = \gamma_ {0 0} + \gamma_ {0 1} \text { DealSeeking } + \gamma_ {0 2} \text { Brand } + \gamma_ {0 3} \text { ExpGoods } \\ & + \gamma_ {0 4} \text { KeywordLength } + \gamma_ {0 5} \text { Brand } \times \text { DealSeeking } \\ & + \gamma_ {0 6} \text { ExpGoods } \times \text { DealSeeking } + \gamma_ {0 7} \text { ExpGoods } \times \text { Brand } \\ & + \sum_ {k = 0 8} ^ {0 1 4} \gamma_ {k} \text { ProductCategory } _ {k} + \mu_ {i 0} \end{array}\tag{4}
$$

$$
\beta_ {i 1} = \gamma_ {1 0} + \mu_ {i 1}\tag{5}
$$

$$
\beta_ {i 2} = \gamma_ {2 0} + \mu_ {i 2}\tag{6}
$$

$$
\beta_ {i 3} = \gamma_ {3 0} + \mu_ {i 3}\tag{7}
$$

$$
\left[ \begin{array}{l} \mu_ {i 0} \\ \mu_ {i 1} \\ \mu_ {i 2} \\ \mu_ {i 3} \end{array} \right] \sim M V N \left(\left[ \begin{array}{l} 0 \\ 0 \\ 0 \\ 0 \end{array} \right], \left[ \begin{array}{c c c c} \sum_ {1 1} & \sum_ {1 2} & \sum_ {1 3} & \sum_ {1 4} \\ \sum_ {2 1} & \sum_ {2 2} & \sum_ {2 3} & \sum_ {2 4} \\ \sum_ {3 1} & \sum_ {3 2} & \sum_ {3 3} & \sum_ {3 4} \\ \sum_ {4 1} & \sum_ {4 2} & \sum_ {4 3} & \sum_ {4 4} \end{array} \right]\right)
$$

Substituting Equation (2) with Equations (4), (5), (6), and (7) yields a mixed HGLM model that has terms for rank, product characteristics, and their interactions.

## Modeling Conversion Rates (CRs)

The model for CRs was formulated using similar procedures to those used for CTRs. The dependent variable of Level 1 in this model is CRs. Since CRs can be defined only when the number of clicks is greater than zero, observations with zero clicks in the CTR data were deleted.<sup>5</sup> If $Z _ { i j }$ is assumed to follow a certain probability distribution, the sampling model is as follows:

$$
Z _ {i j} | Q _ {i j} \sim \beta (\eta_ {i j}, Q _ {i j})\tag{8}
$$

where $Z _ { i j }$ is the total number of purchases among $\eta _ { i j }$ (the total number of clicks), and $Q _ { i j }$ represents the probability of purchase for each click. $Z _ { i j }$ follows a binomial distribution. The link function and structural model were formulated using the same methods as those used for CTRs.

$$
\begin{array}{l} \beta_ {i 0} ^ {\prime} = \delta_ {0 0} + \delta_ {0 1} \text { DealSeeking } + \delta_ {0 2} \text { Brand } + \delta_ {0 3} \text { ExpGoods } \\ \quad + \delta_ {0 4} \text { KeywordLength } + \delta_ {0 5} \text { Brand } \times \text { DealSeeking } \\ \quad + \delta_ {0 6} \text { ExpGoods } \times \text { DealSeeking } + \delta_ {0 7} \text { ExpGoods } \times \text { Brand } \\ \quad + \sum_ {k = 0 8} ^ {0 1 4} \delta_ {k} \text { ProductCategory } _ {k} + v _ {i 0} \end{array}\tag{9}
$$

$$
\beta_ {i 1} ^ {\prime} = \delta_ {1 0} + v _ {i 1}\tag{10}
$$

$$
\beta_ {i 2} ^ {\prime} = \delta_ {2 0} + v _ {i 2}\tag{11}
$$

$$
\beta_ {i 3} ^ {\prime} = \delta_ {3 0} + v _ {i 3}\tag{12}
$$

$$
\left[ \begin{array}{c} v _ {i 0} \\ v _ {i 1} \\ v _ {i 2} \\ v _ {i 3} \end{array} \right] \sim M V N \left(\left[ \begin{array}{c} 0 \\ 0 \\ 0 \\ 0 \end{array} \right], \left[ \begin{array}{c c c c} \Sigma_ {1 1} ^ {\prime} & \Sigma_ {1 2} ^ {\prime} & \Sigma_ {1 3} ^ {\prime} & \Sigma_ {1 4} ^ {\prime} \\ \Sigma_ {2 1} ^ {\prime} & \Sigma_ {2 2} ^ {\prime} & \Sigma_ {2 3} ^ {\prime} & \Sigma_ {2 4} ^ {\prime} \\ \Sigma_ {3 1} ^ {\prime} & \Sigma_ {3 2} ^ {\prime} & \Sigma_ {3 3} ^ {\prime} & \Sigma_ {3 4} ^ {\prime} \\ \Sigma_ {4 1} ^ {\prime} & \Sigma_ {4 2} ^ {\prime} & \Sigma_ {4 3} ^ {\prime} & \Sigma_ {4 4} ^ {\prime} \end{array} \right]\right)
$$

## Results

Tables 3 and 4 present the descriptive statistics for the individual- and group-level variables, respectively. The average weekly frequency of exposure was 416.88 for a given keyword across all channels. Of these exposures, approximately 14 led to a click-through and only 0.22 led to a purchase. Table 5 provides the coefficients of correlation among the parameters considered in the analysis. The highest bivariate correlation observed was that between brand and keyword length (r = 0.248), and the majority of correlation coefficients were below 0.15.

The HGLM results obtained from the fixed-effect analysis are summarized in Table 6. The findings with and without interaction terms are also presented. As articulated in H1a, the CTRs for deal-seeking keywords are expected to be higher than those for only product keywords. The results validate this hypothesis $( \gamma _ { 0 1 } = 0 . 5 4 7 , p < 0 . 0 1 )$ . The odds ratio of dealseeking keywords was 1.73, which can be interpreted as implying that the possibility of clicks is 73 percent higher when a keyword contains deal-seeking keywords than when no such keywords are included in search queries. H2a states that the CTR for searches that contain brand-seeking terms will be lower than that for searches that exclude such keywords. The results were statistically significant, but in the reverse direction $( \gamma _ { 0 2 } = 0 . 4 2 9 , p < 0 . 0 1 )$ . Consequently, H2a is not supported by the results of testing with the full data set.<sup>6</sup>

The coefficient for deal-seeking with respect to CR was significant $( \delta _ { 0 1 } = 0 . 2 6 4 , \ p \ < \ 0 . 0 5 )$ , thereby validating H1b. Similarly, the coefficient for brand-seeking was significant $( \delta _ { 0 2 } = 0 . 1 5 0 , p < 0 . 0 5 )$ , thus supporting H2b. The odds ratios of deal-seeking and brand name were 1.30 and 1.16, respectively. These values suggest that the propensity to purchase can increase by 30 percent and 16 percent when keywords related to deal-seeking and brand-seeking, respectively, are included in a composite search.

Hypotheses 3a and 3b state that product type moderates the relationship between the inclusion of product attribute terms and search behavior and purchase propensity. Table 6 shows a positive interaction between experience goods and dealseeking terms $( \gamma _ { 0 6 } = 0 . 3 4 8 , p < 0 . 0 1 )$ with respect to CTRs. This interaction lends support to H3a. A negative interaction between experience goods and brand-seeking keywords was found $( \gamma _ { 0 7 } = - 0 . 5 2 9 , p < 0 . 0 1 )$ . The data therefore support H3b.

We examined the interaction effects to gain additional insight into the results of the analysis. Figure 1(a) illustrates that regardless of product type, the inclusion of deal-seeking terms in search queries increases CTRs; the CTRs rise from 0.085 to 0.138 for search goods and from 0.053 to 0.121 for experience goods. An interesting finding is that although search goods generally elicit higher CTRs than those generated by experience goods, the magnitude of increase due to the inclusion of deal-seeking terms is greater for the latter than for the former.

Table 3. Descriptive Statistics for Individual-Level Variables

<table><tr><td></td><td>Variables</td><td>Number of Cases</td><td>Mean</td><td>Std. Dev.</td><td>Min</td><td>Max</td></tr><tr><td rowspan="4">CTR Data</td><td>Exposures</td><td>86,129</td><td>416.88</td><td>3,581.3</td><td>1</td><td>415,788</td></tr><tr><td>Clicks</td><td>86,129</td><td>14.22</td><td>100.9</td><td>0</td><td>6,573</td></tr><tr><td>Purchases</td><td>86,129</td><td>0.22</td><td>1.9</td><td>0</td><td>142</td></tr><tr><td>Rank</td><td>86,129</td><td>2.01</td><td>1.4</td><td>1</td><td>24.7</td></tr><tr><td rowspan="3">CR Data</td><td>Clicks</td><td>46,543</td><td>26.32</td><td>136.2</td><td>1</td><td>6,573</td></tr><tr><td>Purchases</td><td>46,543</td><td>0.42</td><td>2.6</td><td>0</td><td>142</td></tr><tr><td>Rank</td><td>46,543</td><td>2.09</td><td>1.4</td><td>1</td><td>21</td></tr></table>

Table 4. Descriptive Statistics of Group-Level Variables

<table><tr><td></td><td>Variables</td><td>Number of Cases</td><td>Mean (%)</td><td>Std. Dev.</td><td>Min</td><td>Max</td></tr><tr><td rowspan="4">CTR Data</td><td>DealSeeking</td><td>11,001</td><td>0.12(12%)</td><td>0.33</td><td>0.0</td><td>1.0</td></tr><tr><td>Brand</td><td>11,001</td><td>0.67(67%)</td><td>0.47</td><td>0.0</td><td>1.0</td></tr><tr><td>ExpGoods</td><td>11,001</td><td>0.27(27%)</td><td>0.45</td><td>0.0</td><td>1.0</td></tr><tr><td>KeywordLength</td><td>11,001</td><td>6.87</td><td>2.30</td><td>1.0</td><td>22.0</td></tr><tr><td rowspan="4">CR Data</td><td>DealSeeking</td><td>7,650</td><td>0.10(10%)</td><td>0.30</td><td>0.0</td><td>1.0</td></tr><tr><td>Brand</td><td>7,650</td><td>0.68(68%)</td><td>0.46</td><td>0.0</td><td>1.0</td></tr><tr><td>ExpGoods</td><td>7,650</td><td>0.25(25%)</td><td>0.43</td><td>0.0</td><td>1.0</td></tr><tr><td>KeywordLength</td><td>7,650</td><td>6.65</td><td>2.25</td><td>1</td><td>20</td></tr></table>

Table 5. Correlations Between Level 2 Variables in the CTR Data

<table><tr><td></td><td>DealSeeking</td><td>Brand</td><td>ExpGoods</td><td>KeywordLength</td></tr><tr><td>DealSeeking</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>Brand</td><td>- 0.068**</td><td>1.000</td><td></td><td></td></tr><tr><td>ExpGoods</td><td>- 0.011</td><td>- 0.093**</td><td>1.000</td><td></td></tr><tr><td>KeywordLength</td><td>0.123**</td><td>0.248**</td><td>0.060**</td><td>1.000</td></tr></table>

\*\*p < 0.01

Figure 1(b) shows the effect of interaction between product type and brand name on CTRs and CRs. Entering a specific brand name for experience goods negatively influenced CTRs $( \gamma _ { 0 7 } = - 0 . 5 2 9 , p < 0 . 0 1 )$ . When a brand name was added to the entries for search goods, CTRs increased. Intriguingly, however, CTRs decreased when a brand name was entered in a search for experience goods. The correlations of effect size (r) for deal-seeking and brand name in the CTR model were 0.155 and 0.175, respectively.

## Robustness Check: Causal Validation

A potential caveat regarding our HGLM econometric approaches is that these mechanisms may not fully convey the causal relationship between keyword types and consumer search and purchase behaviors. To obtain a causal inference that is based on more than simple correlations, we adopted the doubly robust (DR) estimator (Bang and Robins 2005; Funk et al. 2011), which is derived from the propensity score weighting mechanism that effectively handles potential selection bias and confounded factor problems (Hirano et al. 2003). The DR estimator combines inverse probability weighting by a propensity score and the regression approach that captures the relationship between outcomes and covariates (see the appendix). Propensity score matching (Rosenbaum and Rubin 1983) is another option for validating causality, but it is computationally demanding in general and inefficient for exceedingly large data sets such as ours. By contrast, the propensity weighting method enables rapid implementation and simple computations of the standard errors of estimates. Table 7 presents the results derived by propensity score weighting. The statistical direction and significance are highly analogous to those reported in Table 6. This robustness procedure validates the accuracy and reliability of our HGLM estimations and causal inferences.

<table><tr><td colspan="5">Table 6. Coefficient Estimates for CTR and CR</td></tr><tr><td rowspan="2"></td><td colspan="2">CTR</td><td colspan="2">CR</td></tr><tr><td>Model 1</td><td>Model 2</td><td>Model 1</td><td>Model 2</td></tr><tr><td>Intercept</td><td>-2.228**(0.024)</td><td>-2.376**(0.028)</td><td>-4.218**(0.070)</td><td>-4.240**(0.069)</td></tr><tr><td colspan="5">Level 1 Variable</td></tr><tr><td>Rank</td><td>-0.149**(0.003)</td><td>-0.175**(0.004)</td><td>0.040*(0.019)</td><td>0.040*(0.019)</td></tr><tr><td>Channel_B</td><td>0.053(0.165)</td><td>-0.029(0.121)</td><td>-2.432**(0.334)</td><td>-2.440**(0.340)</td></tr><tr><td>Channel_C</td><td>-0.593**(0.021)</td><td>-0.283**(0.026)</td><td>-0.153**(0.035)</td><td>-0.153**(0.035)</td></tr><tr><td colspan="5">Level 2 Variable</td></tr><tr><td>DealSeeking</td><td>0.484**(0.030)</td><td>0.547**(0.033)</td><td>0.262*(0.113)</td><td>0.264*(0.110)</td></tr><tr><td>BrandSeeking</td><td>0.367**(0.019)</td><td>0.429**(0.023)</td><td>0.125*(0.055)</td><td>0.150**(0.057)</td></tr><tr><td>ExpGoods</td><td>-0.408**(0.024)</td><td>-0.504**(0.031)</td><td>0.007(0.077)</td><td>0.022(0.083)</td></tr><tr><td>KeywordLength</td><td>0.047**(0.003)</td><td>0.052**(0.004)</td><td>-0.019(0.011)</td><td>-0.019(0.011)</td></tr><tr><td colspan="5">Interaction</td></tr><tr><td>BrandSeeking*DealSeeking</td><td></td><td>-0.098(0.070)</td><td></td><td>0.525*(0.227)</td></tr><tr><td>ExpGoods*DealSeeking</td><td></td><td>0.348**(0.075)</td><td></td><td>0.165(0.265)</td></tr><tr><td>ExpGoods*BrandSeeking</td><td></td><td>-0.529**(0.047)</td><td></td><td>0.075(0.110)</td></tr><tr><td colspan="5">Product Category</td></tr><tr><td>Furniture</td><td>0.057(0.034)</td><td>0.042(0.041)</td><td>-0.840**(0.154)</td><td>-0.842**(0.153)</td></tr><tr><td>Home</td><td>0.311**(0.029)</td><td>0.362**(0.035)</td><td>0.100(0.085)</td><td>0.097(0.085)</td></tr><tr><td>Sports &amp; Outdoors</td><td>0.127**(0.036)</td><td>0.129**(0.042)</td><td>-0.346**(0.098)</td><td>-0.341**(0.099)</td></tr><tr><td>Fashion</td><td>0.369**(0.026)</td><td>0.385**(0.031)</td><td>-0.409**(0.077)</td><td>-0.406**(0.080)</td></tr><tr><td>Electronics</td><td>-0.397**(0.030)</td><td>-0.410**(0.038)</td><td>-0.375**(0.098)</td><td>-0.380**(0.098)</td></tr><tr><td>Grocery &amp; Food</td><td>0.137**(0.042)</td><td>0.100(0.054)</td><td>0.409**(0.122)</td><td>0.421**(0.122)</td></tr><tr><td>Beauty</td><td>-0.398**(0.028)</td><td>-0.479**(0.034)</td><td>-0.020(0.082)</td><td>-0.014(0.084)</td></tr><tr><td colspan="5">Variance Components</td></tr><tr><td>Intercept</td><td>1.209</td><td>1.171</td><td>1.079</td><td>1.077</td></tr><tr><td>Rank</td><td>0.054</td><td>0.083</td><td>-</td><td>-</td></tr><tr><td>Channel_B</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Channel_C</td><td>0.834</td><td>-</td><td>-</td><td>-</td></tr></table>

\*\*p < 0.01; \*p < 0.05; ( ): standard error

![](/api/attachments/MJGSYE6B/fulltext/images/1120420cb9453a904e3297d44914d71bca60b9a3eb04255c6abcf7fd5f20f882.jpg)  
(a) Deal-Seeking

![](/api/attachments/MJGSYE6B/fulltext/images/1e5309a70af6f780dd6a6928c7912ad176bbf4f48404552c28767a7d4708edd7.jpg)  
(b) Brand-Seeking  
Figure 1. Interaction Effects among Product Type, Deal-Seeking, and Brand-Seeking on CTRs

<table><tr><td colspan="3">Table 7. Estimated Causal Effects of Keyword Attributes based on Propensity Score Weighting</td></tr><tr><td></td><td>CTR</td><td>CR</td></tr><tr><td>DealSeeking</td><td>0.0637 (0.0044)**</td><td>0.0027 (0.0014)*</td></tr><tr><td>Brand</td><td>0.0210 (0.0022)**</td><td>0.0016 (0.0008)*</td></tr><tr><td>ExpGoods</td><td>-0.0495 (0.0040)**</td><td>-0.0011 (0.0012)</td></tr><tr><td>DealSeeking*Brand</td><td>0.0666 (0.0053)**</td><td>0.0032 (0.0019)</td></tr><tr><td>DealSeeking*ExpGoods</td><td>0.0446 (0.0086)**</td><td>-0.0008 (0.0020)</td></tr><tr><td>Brand*ExpGoods</td><td>-0.0605 (0.0018)**</td><td>0.0020 (0.0009)*</td></tr></table>

\*\*p < 0.01; \*p < 0.05; ( ): standard error

## Brand-Seeking Keywords and CTR

All our proposed hypotheses, with the exception of H2a, are supported. The findings point to positive rather than negative effects of brand-seeking search queries on consumers’ search patterns. However, H2a is supported when experience goods only are included in the sample. We put forward several plausible explanations for this phenomenon. Consistent with our prediction, brand-seeking consumers who are looking at experience goods focus on the depth of their searches, as reflected by the negative interaction between experience goods and brand-seeking keywords. For search goods, however, even brand-seeking consumers tend to concentrate on the breadth of their searches and expand their consideration set to optimize economic gains. A plausible alternative is that in contrast to experience goods, many search goods may not be supported by strong brands that consumers recognize and with which they identify. Consequently, the impact of brands for search goods is likely to be weak, and consumers who buy such products are naturally motivated to increase their consideration set.

## Profitability of Keyword Combinations

In a further analysis, we investigated the economic value of each keyword pattern using the data on sales (= purchases × price) and costs (= clicks × cost per click). We first calculated the total sales amount generated and the costs incurred from each keyword combination. We then ran the model specified in Equation (4) with a slight modification; that is, the sales-to-costs ratio was used as the dependent variable. In the coefficient analyses, we found that the sales-to-costs ratio was highest when both deal-seeking and brand-seeking keywords were included in the search (Figure 2). Contrastingly, the lowest sales-to-costs ratio was observed when neither of the two attributes was included in a search query. A comparison of deal-seeking and brand-seeking keywords in terms of cost effectiveness reveals that dealseeking keywords generate approximately three times the sales of those produced by brand-seeking keywords.

![](/api/attachments/MJGSYE6B/fulltext/images/3a9ef9772e71b68972a3deb5b26351ed5b3f3b8c64471fec384e1e63fbf76641.jpg)  
Figure 2. Expected Sales-to-Costs Ratio by Type of Keyword

## Promotion Periods and Search Performance

Most online stores regularly offer special promotions in the form of price discounts to stimulate sales (Mela et al. 1997). Not surprisingly, consumers’ search behavior and buying propensities may vary during these high-demand periods; both deal-seeking and brand-seeking consumers are motivated to expand their consideration set and search more aggressively than they do during regular periods. If all else is equal, this more intense searching will elevate CTRs. However, whether CRs increase or decrease during special promotion periods is unclear. Will an increase in the number of purchases balance out an increase in CTR or will an imbalance occur? Moreover, how will deal-seeking and brand-seeking consumers react to price promotions?

To answer these questions, data from sales and non-sale periods were compared. Figure 3 demonstrates that search breadth increased substantially for both deal-seeking and brand-seeking consumers during the promotion period. However, our results suggest that sales periods either have no effect or they have a negative effect on CRs. This finding must be interpreted with caution; the results show that purchases indeed increased during the promotion periods, but CTRs also increased to an even higher level. Consequently, the radical increases in CTRs diminished those of CRs during the sales period. An issue of interest is that although brandseeking keywords are positively associated with CRs during the regular period, a negative relationship was observed during the sales period. Brand-seeking consumers’ insensitivity to price may partially account for this seemingly paradoxical finding (Krishnamurthi and Raj 1991).

## Effects of Rank on Deal-Seeking and Brand-Seeking Keywords

How does the average rank (position) of ads in search results interact with deal-seeking or brand-seeking terms? The econometric model was extended to include brand-seeking and deal-seeking keywords as explanatory variables for rank. For brand-seeking terms, CTRs significantly increase with decreasing rank; that is, the keywords occupy a high position in search results $( p < 0 . 0 1 )$ ). Such rank effects, however, are not evident for deal-seeking keywords (p > 0.1). The CRs of brand-seeking keywords decline with decreasing rank, but no CR effects arise from ad rank in the case of deal-seeking keywords. These results suggest that top-positioned brandseeking terms effectively elicit information search intent (i.e., CTRs), but do not directly stimulate purchase. For dealseeking keywords, ad position does not necessarily promote search intent or purchase. This finding extends those of previous studies (e.g., Animesh et al. 2010; Ghose and Yang 2009) that report no significant effects of rank on profitability.

## Implications

The findings of this study offer several implications for scholarship and management. Previous studies pointed to the necessity of closer scrutiny of how product- and consumerspecific characteristics govern online consumers’ search patterns and buying decisions in sponsored search platforms (Agarwal et al. 2011; Ghose and Yang 2009). Rising to this challenge, in this study we identified the key contextual factors that influence consumers’ search and purchase behaviors in online sponsored environments. The search depth and search breadth paradigm provides a valuable theoretical vantage point from which to comprehend the dynamic relationships between keyword characteristics and consumers’ search propensities and purchase decisions.

![](/api/attachments/MJGSYE6B/fulltext/images/4ea6c5d7d86c66bdc8aedfe8d126d8a43c44b66aaea386ace62db23e0994c0ed.jpg)

![](/api/attachments/MJGSYE6B/fulltext/images/ffb9a6185da420ec3e080830f3a0c2ca91c7e87dd3c0f56fa9e0044736d62ed2.jpg)  
Figure 3. CTRs and CRs (Regular Periods Versus Sales Periods)

The observed empirical regularities illustrate that consumers’ search objectives and purchase likelihood can be effectively inferred from search keywords. Patterns of search terms can thus shed theoretical light on the purchase funnel framework used to illuminate the inner workings of online sponsored environments. Customers who include deal-seeking terms in their search queries are situated further down the purchase funnel than customers who enter brand-seeking search terms, as evidenced by their higher CTRs and CRs. Furthermore, consumers who enter both deal-seeking and brand-seeking terms along with a product entry in a single search query are likely to be located further along the funnel toward a purchase than consumers who enter a deal-seeking term or a brand name alone. Price (deal-seeking) and brand complement each other as extrinsic consumer cues (Brucks et al. 2000). When information on both attributes is accessible, consumers’ propensity to engage in additional searches decreases. Instead, their purchase likelihood increases.

The findings of the study also shed light on the manner by which online advertisers conduct business, particularly when they develop advertising strategies related to keyword selection, ad copy, and the design and content of landing pages. Advertisers should be cognizant of patterns that characterize consumers’ use of search keywords and tailor their marketing campaigns accordingly. By doing so, advertisers may attract deal-seeking consumers who, according to our results, will exhibit high CTRs and CRs. These pricesensitive consumers are considered near-purchase customers, intent as they are on maximizing economic gains by visiting many stores. In contrast to deal-seeking users, consumers who extensively use brand-seeking keywords during the course of a search are more meticulous given their relatively narrower consideration set. At the same time, however, they can be viewed as high-value customers because they display a higher tendency to purchase products. This tendency makes monetary investment in sponsored searches worthwhile. In particular, CRs increase considerably when search queries contain both brand-seeking terms and experience goods. Brand-seeking terms appear to create synergies that boost search performance when they are used in searches within certain product categories. Depending on whether advertisers need to increase CTRs or CRs, they should leverage this stylistic feature and bid wisely on keywords that contain either deal-seeking or brand-seeking terms.

In the assessment of profitability, which was measured in this study on the basis of the total sales amount divided by the investment costs of a given keyword, search terms that comprise both deal-seeking and brand-seeking words proffered higher payoffs than did the keywords that contain only one or the other. Additionally, keywords that include both attributes resulted in returns nearly five times greater than those acquired from only product keywords. Furthermore, dealseeking keywords outcompeted their brand-seeking equivalents in terms of profitability. The former is nearly three times more cost effective than the latter. Given that dealseeking keywords not only elicit higher CTRs and CRs, but also generate larger economic payoffs, advertisers can secure a superior advantage by bidding competitively on such keywords. Contrary to expectations, our results suggest that CRs decrease, rather than increase, during high-demand periods. This is attributed to the fact that actual purchases do not increase to the same extent as CTRs do. Such negative effects are more pronounced for brand-seeking keywords than for deal-seeking keywords. The searches of brand-seeking consumers seem to intensify in breadth during promotion periods, but these elevations do not translate into actual purchases.

Another insight from our findings is that product type can exert a significant moderating effect on the relationship between keyword combinations and search behaviors. For search goods, the addition of brand-seeking or deal-seeking terms to a search query substantially increased CTRs and the CRs. This suggests that retailers selling search goods should accord preference to keywords that contain brand names or deal-seeking terms to increase website traffic. With respect to experience goods, the combination of deal-seeking terms and experience goods resulted in significantly higher CTRs and CRs than did product keywords. Retailers whose businesses rely heavily on the sale of experience goods are advised to establish effective pricing structures to attract visitors and convert them into buyers.

## Limitations and Future Research

As in previous research (e.g., Ghose and Yang 2009), we collected our sponsored search data from one large retailer that offers numerous product categories online. Although this method can reduce the potential bias from unobserved heterogeneities specific to each advertiser, the results obtained from one company cannot represent the behavior of all advertisers who use sponsored search services. Future researchers can collect data from advertisers of various sizes and across different industries to enhance the generalizability of findings. Another issue worth revisiting is the behavior-related inference based primarily on the keywords that consumers enter in their search queries. We assumed that auxiliary keyword strings (e.g., cheapest, low price) represent consumers level of price consciousness and the extent of their information gathering about a product. Although anecdotal evidence suggests that consumers’ use of such supplementary keywords is related to their search preferences (Jansen et al. 2008), a thorough validation grounded on more direct methods (e.g., experiments) is necessary.

An important avenue for future work is to extend the econometric model by including a time dimension for the purpose of improving the model’s precision and predictive capability. An identical keyword entered by the same consumer at different purchase stages may have different implications for CTRs and CRs. In order to test this possibility, it is necessary to factor in an additional parameter that reflects a consumer’s purchase stage. For example, the frequency of repeat visits, as identified by a unique IP address, can serve as a proxy for purchase stages or intent. A refined model incorporating a time element is also needed to enhance predictive power and accuracy. Aside from the contextual factors investigated in this study, other product- and consumer-specific characteristics should be identified to account for the additional variance in predicting sponsored search performance. Finally, building on the insights resulting from our analysis, future researchers can put forward specific bidding strategies on the basis of keyword properties that may optimize benefits for advertisers.

## Conclusion

We analyzed the characteristics of search keywords entered directly by consumers in sponsored search platforms and assessed the extent to which such terms are associated with consumers’ search behaviors and purchase intent. To improve the analysis, we focused on two of the most representative types of product attribute keywords: deal-seeking and brandseeking terms. These keywords have been widely acknowledged as wielding a significant influence on consumer choices and buying behaviors. The results suggest that keywords have complex and multidimensional effects on search performance. Keyword use appreciably varies depending on the combinations of product attributes and the search measures adopted. Product characteristics also substantially moderate the relationship between search keywords and consumers search and buying behaviors.

We also provide practical advice for online sellers and search engine companies as to how they can capitalize on their investments, maximize profitability, and harness business opportunities through sponsored search markets. This study helps companies grasp the nature of keyword-based competition and the dynamics inherent in sponsored search ecosystems. Widespread adoption of new mobile/smart devices and applications by consumers and the commensurate use of search tools by thriving social media companies are projected to expand the sponsored search market dramatically and challenge the minds of IS researchers and professionals for years to come. Firms should therefore endeavor to treat product and consumer characteristics as integral aspects of marketing strategies for sponsored searches.

## Acknowledgments

Wonseok Oh was the corresponding author of this paper. This research was partially supported by the National Research Foundation of Korea Grant funded by the Korean Government (NRF-2013S1A3A2055050). The authors’ works were also supported in part by research grants from Hankuk University of Foreign Studies Research Fund of 2015 and College of Business at Korea Advanced Institute of Science and Technology.

## References

Agarwal, A., Hosanagar, K., and Smith, M. D. 2011. “Location, Location and Location: An Analysis of Profitability of Position in Online Advertising Markets,” Journal of Marketing Research (48:6), pp. 1057-1073.

Animesh, A., Ramachandran, V., and Viswanathan, S. 2010. “Quality Uncertainty and Performance of Online Sponsored Search Markets: An Empirical Investigation,” Information Systems Research (21:1), pp. 190-201.

Bakos, J. Y. 1997. “Reducing Buyer Search Costs: Implications for Electronic Marketplaces,” Management Science (43:12), pp. 1676-1692.

Banerjee, A. V. 1992. “A Simple Model of Herd Behavior,” Quarterly Journal of Economics (107:3), pp. 797-817.

Bang, H., and Robins, J. M. 2005. “Doubly Robust Estimation in Missing Data and Causal Inference Models,” Biometrics (61:4), pp. 962-973.

Bikhchandani, S., Hirshleifer, D., and Welch, I. 1992. “A Theory of Fads, Fashion, Custom, and Cultural Changes as Information Cascades,” Journal of Political Economy (100:5), pp. 992-1026.

Brucks, M., Zeithaml, V. A., and Naylor, G. 2000. “Price and Brand Names as Indicators of Quality Dimensions for Consumer Durables,” Journal of Academy of Marketing Science (28:3), pp. 359-374.

Caminal, R., and Vives, X. 1996. “Why Market Shares Matter: An Information-Based Theory,” Journal of Economics (27:2), pp. 221-239.

Chaitanya, N., and Narahari, Y. 2012. “Optimal Equilibrium Bidding Strategies for Budget Constrained Bidders in Sponsored Search Auctions,” Operational Research (12:3), pp. 317-343.

Chaudhuri, A., and Holbrook, M. 2001. “The Chain Effects from Brand Trust and Brand Affect to Brand Performance: The Role of Brand Loyalty,” Journal of Marketing (65:2), pp. 81-94.

Chen, J., Liu, D., and Winston, A. B. 2009. “Auctioning Keywords in Online Search,” Journal of Marketing (73:4), pp. 125-141.

Degeratu, A. M., Rangaswamy, A., and Wu, J. 2000. “Consumer Choice Behavior in Online and Traditional Supermarkets: The Effects of Brand Name, Price, and Other Search Attributes,” International Journal of Research in Marketing (17:1), pp. 55-78.

Dennis, A. R., and Taylor, N. J. 2006. “Information Foraging on the Web: The Effects of ‘Acceptable’ Internet Delays on Multi-Page Information Search Behavior,” Decision Support Systems (42:2), pp. 810-824.

Dodds, W. B., and Monroe, K. B. 1985. “The Effect of Brand and Price Information on Subjective Product Evaluations,” Advances in Consumer Research (12), pp. 85-90.

Dodds, W. B., Monroe, K. B., and Grewal, D. 1991. “The Effects of Price, Brand and Store Information on Buyers’ Product Evaluations,” Journal of Marketing Research (28:3), pp. 307-319.

Farquhar, P. H. 1989. “Managing Brand Equity,” Marketing Research (1:3), pp. 24-33.

Funk, M. J., Westreich, D., Wiesen, C., Stürmer, T., Brookhart, M. A., and Davidian, M. 2011. “Doubly Robust Estimation of Causal Effects,” American Journal of Epidemiology (173:7), pp. 761-767.

Ghose, A., and Yang, S. 2009. “An Empirical Analysis of Search Engine Advertising: Sponsored Search in Electronic Markets,” Management Science (55:10), pp. 1605-1622.

Gilbride, T. J., and Allenby, G. M. 2004. “A Choice Model with Conjunctive, Disjunctive and Compensatory Screening Rules,” Marketing Science (23:3), pp. 391-406.

Goldfarb, A., and Tucker, C. 2011. “Online Display Advertising: Targeting and Obtrusiveness,” Marketing Science (30:3), pp. 389-404.

Hirano, K., Imbens, G. W., and Ridder, G. 2003. “Efficient Estimation of Average Treatment Effects Using the Propensity Score,” Econometrica (71), pp. 1161-1189.

Howard, J. A., and Sheth, J. N. 1969. The Theory of Buyer Behavior, New York: Wiley.

Huang, P., Lurie, N., and Mitra, S. 2009. “Searching for Experience on the Web: An Empirical Examination of Consumer Behavior for Search and Experience Goods,” Journal of Marketing (73:2), pp. 55-69.

Jacoby, G. J., Szybillo, J., and Busato-Schach, J. 1977. “Information Acquisition Behavior in Brand Choice Situations,” Journal of Consumer Research (3:4), pp. 209-216.

Jansen, B. J., Booth, D. L., and Spink, A. 2008. “Determining the Informational, Navigational, and Transactional Intent of Web Queries,” Information Processing and Management (44:3), pp. 1251-1266.

Kreft, I. G. G., de Leeuw, J., and Aaken, L. S. 1995. “The Effect of Different Forms of Centering in Hierarchical Linear Models,” Multivariate Behavioral Research (30:1), pp. 1-21.

Krishnamurthi, L., and Raj, S. P. 1991. “An Empirical Analysis of the Relationship Between Brand Loyalty and Consumer Price Elasticity,” Marketing Science (10:2), pp. 172-183.

Li, X., and Hitt, L. M. 2008. “Self-Selection and Information Role of Online Product Reviews,” Information Systems Research (19:4), pp. 456-474.

Lynch Jr., J. G., and Ariely, D. 2000. “Wine Online: Search Costs Affect Competition on Price, Quality, and Distribution,” Marketing Science (19:1), pp. 83-103.

Maas, C. J. M., and Snijders, T. A. B. 2003. “The Multilevel Approach to Repeated Measures for Complete and Incomplete Data,” Quality and Quantity (37:1), pp. 71-89.

Mehta, N., Rajiv, S., and Srinivasan, K. 2003. “Price Uncertainty and Consumer Search: A Structural Model of Consideration Set Formation,” Marketing Science (22:1), pp. 58-84.

Mela, C. F., Gupta, S., and Lehman, D. R. 1997. “The Long Term Impact of Promotion and Advertising on Consumer Brand Choice,” Journal of Marketing Research (34:2), pp. 248-261.

Moe, W. W. 2006. “An Empirical Two-Stage Choice Model with Varying Decision Rules Applied Ot Internet Clickstream Data,” Journal of Marketing Research (43:4), pp. 680-692.

Mudambi, S. M., and Schuff, D. 2010. “What Makes a Helpful Online Review? A Study of Customer Reviews on Amazon.com,” MIS Quarterly (34:1), pp. 185-200.

Narayandas, D. 1998. “Measuring and Managing the Benefits of Customer Retention an Empirical Investigation,” Journal of Service Research (1:2), pp. 108-128.

Nelson, P. 1970. “Information and Consumer Behavior,” Journal of Political Economy (78:2), pp. 311-329.

Neslin, S. A., Jerath, K., Bodapati, A., Bradlow, E. T., Deighton, J., Gensler, S., Lee, L., Montaguti, E., Telang, R., and Venkatesan, R. 2014. “The Interrelationships Between Brand and Channel Choice,” Marketing Letters (25:3), pp. 319-330.

Nicholson, S., Sierra, T., Eseryel, U. Y., Park, J.-H., Barkow, P., Pozo, E. J., and Ward, J. 2006. “How Much of it Is Real? Analysis of Paid Placement in Web Search Engine Results,” Journal of American Society for Information Science and Technology (57:4), pp. 448-461.

Novak, T. P., and Hoffman, D. L. 1997. “New Metrics for New Media: Toward the Development of Web Measurement Standards,” World Wide Web Journal (2:1), pp. 213-246.

Ozanne, J. L., Brucks, M., and Grewal, D. 1992. “A Study of Information Search Behavior During the Categorization of New Products,” Journal of Consumer Research (18:4), pp. 452-463.

Rao, A. R., and Monroe, K. B. 1989. “The Effect of Price, Brand Name, and Store Name on Buyers’ Perceptions of Product Quality: An Integrative Review,” Journal of Marketing Research (26:3), pp. 351-357.

Raudenbush, S. W., and Bryk, A. S. 2002. Hierarchical Linear Models: Applications and Data Analysis Methods (2<sup>nd</sup> ed.), Newbury Park, CA: Sage Publications.

Rosenbaum, P. R., and Rubin, D. B. 1983. “The Central Role of the Propensity Score in Observational Studies for Causal Effects,” Biometrika (70:1), pp. 41-55.

Rubin, D. B. 1974. “Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies,” Journal of Educational Psychology (66:5), pp. 688-701.

Rutz, O. J., and Trusov, M. 2011. “Zooming in on Paid Search Ads—A Consumer-Level Model Calibrated on Aggregated Data,” Marketing Science (30:5), pp. 789-800.

Stiger, G. J. 1961. “The Economics of Information,” Journal of Political Economy (69:3), pp. 213-225.

Taşoluk, B., Droge, C., and Calantone, R. J. 2011. “Interpreting Interrelations across Multiple Levels in HGLM Models: An Application in International Marketing Research,” International Marketing Review (28:1), pp. 34-56.

Tauscher, L., and Greenberg, S. 1997. “How People Revisit Web Pages: Empirical Findings and Implications for the Design of History Systems,” International Journal of Human–Computer Studies (47:1), pp. 97-137.

Tellis, G. J. 1988. “The Price Elasticity of Selective Demand: A Meta-Analysis of Econometric Models of Sales,” Journal of Marketing Research (25:4), pp. 331-341.

Urbany, J. E., Dickson, P. R., and Wilkie, W. L. 1989. “Buyer Uncertainty and Information Search,” Journal of Consumer Research (16:2), pp. 208-215.

Van Der Leeden, R. 1988. “Multilevel Analysis of Repeated Measures Data,” Quality and Quantity (32:1), pp. 15-29.

Yang, S., and Ghose, A. 2010. “Analyzing the Relationship Between Organic and Sponsored Search Advertising: Positive, Negative, or Zero Interdependence?,” Marketing Science (29:4), pp. 602-623.

Zhu, F., and Zhang, X. 2010. “Impact of Online Consumer Reviews on Sales: The Moderating Role of Product and Consumer Characteristics,” Journal of Marketing (74:2), pp. 133-148.

## About the Authors

Il Im is an associate professor of Information Systems at the School of Business, Yonsei University. He received his Ph.D. from Marshall School of Business, University of Southern California. Prior to joining Yonsei University, he was an assistant professor in the Information Systems Department at the New Jersey Institute of Technology. His current research focuses on personalization technologies and their effects, the effects of social network systems, and technology acceptance. His research has been published in journals, such as ACM Transactions on Information Systems, Information & Management, Technovation, and International Journal of Electronic Commerce.

Jongkun Jun is a professor of Marketing at Hankuk University of Foreign Studies in Yong-In, Korea. He received his Ph.D. in Marketing from Seoul National University’s School of Management in 2000. His research focuses on e-marketing, international marketing, and SME marketing. He has published articles in several scholarly journals, including International Journal of Mobile Communications, International Marketing Review, and The Journal of Database Marketing.

Wonseok Oh is the KCB Chair Professor at the College of Business, Korea Advanced Institute of Science and Technology. He received his Ph.D. in Information Systems from the Stern School of Business at New York University. His research interests include economics of IT, mobile consumption and addiction, social networks, and ebook pricing. His scholarly works have been published in journals such as Information Systems Research, Journal of the Association for Information Systems, Journal of Management Information Systems, MIS Quarterly, Management Science, and Production and Operations Management.

Seok-Oh Jeong is a full professor at Hankuk University of Foreign Studies in Yong-In, Korea. He received his Ph.D. from Seoul National University in 2002. His research has been published in top scientific journals such as Annals of Statistics, Journal of the American Statistical Association, and Neuroimage. His research interests include statistical analysis of productivity, financial risk management, causal inference, and neuroimaging.

## Appendix

## Propensity Score Weighting Methods

We use Rubin’s (1974) potential outcomes notation, now a widely accepted model in causal inference literature. The treatment variable is denoted by $W _ { i j } ,$ which corresponds to any specific keyword attribute, such as the level-2 variable “DealSeeking” in H1a and H1b. The vector of covariates that includes level-1 variables (e.g., rank and channel) and level-2 variables, except for the treatment variable, is denoted by $X _ { i j } .$ The outcome variable (CTR or CR) is characterized by two potential outcomes: $Y _ { i j } ( 0 )$ for the outcome from the control group (e.g., non-dealseeking group in H1a and H1b) and $Y _ { i j } ( 1 )$ for the outcome derived from the treatment group (e.g., deal-seeking group in H1a and H1b). Because a unit cannot simultaneously possess two group memberships, realized (or observed) outcome can be written as follows:

$$
Y _ {i j} = Y _ {i j} (0) I \left(W _ {i j} = 0\right) + Y _ {i j} (1) I \left(W _ {i j} = 1\right)
$$

where $I ( \cdot )$ is the indicator function for group membership. We observe parameters $( Y _ { i j } , \ W _ { i j } , X _ { i j } )$ . Propensity score $p ( { \boldsymbol { x } } )$ is defined by the conditional probability of the treatment

$$
p (\boldsymbol {x}) = \operatorname * {P r} (W _ {i j} = 1 | \boldsymbol {X} _ {i j} = \boldsymbol {x})
$$

We define the regression functions for potential outcomes $Y _ { i j } ( 0 )$ and $Y _ { i j } ( 1 )$ by

$$
m _ {w} (\boldsymbol {x}) = \mathrm{E} (Y _ {i j} (w) | \boldsymbol {X} _ {i j} = \boldsymbol {x})
$$

for $w = 0 , 1$ . In our paper, we model propensity score $p ( { \boldsymbol { x } } )$ and regression functions $m _ { w } ( { \pmb x } ) , w = 0 ,$ 1 by the logistic regression and multiple regression models, respectively. A natural estimator for the treatment effect of interest can be defined by the average of treatment effect $\mathrm { ( A T E ) }$ $Y _ { i j } ( 1 ) - Y _ { i j } ( 0 )$ over all observations. By counterfactual arguments, this estimator is free from any issues that may arise from confoundedness and selection bias. The problem is that for the unit assigned to the treatment condition, $Y _ { i j } ( 1 )$ is observed, but $Y _ { i j } ( 0 )$ is an unobserved counterfactual outcome. Conversely, for the unit assigned to the control group, $Y _ { i j } ( 0 )$ can be observed but $Y _ { i j } ( 1 )$ cannot.

We define the population version of ATE with

$$
\mathrm{ATE} = \mathrm{E} [ Y _ {i j} (1) - Y _ {i j} (0) ]
$$

A straightforward illustration is thus

$$
\mathrm{ATE} = \mathrm{E} [ W _ {i j} Y _ {i j} / p (X _ {i j}) - (1 - W _ {i j}) Y _ {i j} / (1 - p (X _ {i j})) ]
$$

where the arguments in the expectation are now all composed of observables. If we accurately estimate propensity scores $p ( X _ { i j } )$ , therefore, we can estimate ATE by simply averaging

$$
W _ {i j} Y _ {i j} / p \left(\boldsymbol {X} _ {i j}\right) - \left(1 - W _ {i j}\right) Y _ {i j} / \left(1 - p \left(\boldsymbol {X} _ {i j}\right)\right)
$$

with the abuse of notation by reusing p(@) for the estimate of the propensity scores. This estimator can nonetheless be problematic when the postulated propensity score model is incorrect. To circumvent this problem, we adopt the DR estimator, defined by the average of differences $K _ { i j } = I _ { i j } - J _ { i j } ,$ where $I _ { i j }$ and $J _ { i j }$ are given by

$$
I _ {i j} = W _ {i j} Y _ {i j} / p \left(\boldsymbol {X} _ {i j}\right) - \left(W _ {i j} - p \left(\boldsymbol {X} _ {i j}\right)\right) m _ {1} \left(\boldsymbol {X} _ {i j}\right) / p \left(\boldsymbol {X} _ {i j}\right)
$$

and

$$
J _ {i j} = (1 - W _ {i j}) Y _ {i j} / (1 - p (\boldsymbol {X} _ {i j})) + (W _ {i j} - p (\boldsymbol {X} _ {i j})) m _ {0} (\boldsymbol {X} _ {i j}) / (1 - p (\boldsymbol {X} _ {i j}))
$$

$m _ { w } ( \cdot ) , w = 0$ , 1 stand for their estimates, again with the abuse of notation. The standard error of the DR estimator can then be simply obtained by (the standard deviation of $K _ { i j }$ )/(the number of observations). As noted earlier, even if the model specification of either p(x) or $m _ { w } ( \pmb { x } )$ is incorrect, the DR estimator continues to estimate ATE correctly. When propensity score is modeled correctly, the DR estimator generates a smaller variance than that produced by a naïve average estimator and other competitive estimators, such as the inverse weighted estimator (Hirano et al. 2003).

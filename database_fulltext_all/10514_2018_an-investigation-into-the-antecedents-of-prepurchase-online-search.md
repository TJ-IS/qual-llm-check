---
otero_id: 10514
otero_key: "ZE2KWYMW"
title: "An investigation into the antecedents of prepurchase online search"
authors: "Jingguo Wang; Zhiyong Yang; E. Deanne Brocato"
year: "2018"
journal: "Information & Management"
doi: "10.1016/j.im.2017.08.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: An investigation into the antecedents of prepurchase online search

Authors: Jingguo Wang, Zhiyong Yang, Deanne Brocato

![](/api/attachments/ZE2KWYMW/fulltext/images/47e5f849b5ec6bc76cb4120aace0706c5dfae8eef8625e42ece9a91c3bb59320.jpg)

PII: S0378-7206(17)30687-0

DOI: http://dx.doi.org/doi:10.1016/j.im.2017.08.001

Reference: INFMAN 3012

To appear in: INFMAN

Received date: 18-2-2016

Revised date: 30-1-2017

Accepted date: 4-8-2017

Please cite this article as: Jingguo Wang, Zhiyong Yang, Deanne Brocato, An investigation into the antecedents of prepurchase online search, Information and Managementhttp://dx.doi.org/10.1016/j.im.2017.08.001

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# An investigation into the antecedents of prepurchase online search

Jingguo Wang\* Information Systems and Operations Management College of Business, University of Texas at Arlington Email: jwang@uta.edu \*Corresponding Author Zhiyong Yang Marketing College of Business, University of Texas at Arlington Email: zyang@uta.edu Deanne Brocato Marketing Jon M. Huntsman School of Business, Utah State University Email: deanne.brocato@usu.edu

# An investigation into the antecedents of prepurchase online search

## Abstract

This study investigates what influences consumers' extent of online search (i.e., the number of relevant web stores visited) before a purchase. A dataset containing website visitation and transaction activities from a panel of US consumers is used to test the hypotheses developed in the study. The results indicate a diminishing effect of competitive density on the extent of search, and the use of advanced information technologies induces more searches. Consumers also search more for experience products than for search products in contrast to the prediction in the nonelectronic market. Furthermore, online purchase experience increases, while product-specific experience reduces, prepurchase search.

Keywords: Online prepurchase search; competitive density; online experience;

experience/search product; price comparison websites; Markov Chain Monte Carlo (MCMC)

## 1. Introduction

Information search precedes many decisions [1]. The purpose of prepurchase search is to collect information for better purchase decisions [2-5]. In the search process, consumers visit different stores to look for products with desired qualities and compare sellers offering similar products at competitive prices to decide what, when, and from whom to purchase [4]. Understanding how consumers conduct their search before purchases is a critical component of marketing strategies [6]. Effective marketing communications at this stage can significantly influence consumers’ decision and bring extra revenue to a firm.

Acknowledging the importance of prepurchase search, researchers have for decades studied consumers’ information search prior to a purchase in a brick-and-mortar setting (or the nonelectronic market). These studies have focused mainly on two theoretical approaches [7-9]. The first is the economics approach that focuses on the costs and benefits of searches [10]. The basic premise of this approach is that consumer information search is driven by the tradeoff between the expected benefits and the expected cost of searches [11]. Consumers stop searching when the potential benefit to be gained from continuing cannot offset the potential cost. The other approach to understanding prepurchase search is based on the psychological paradigm, which considers that the rationality of individuals is bounded [12], and consumers do not have the mental capacity to process information that will lead optimal decision at all times [13]. As a result, consumers settle with a satisficing product with a limited amount of search [12].

With the development of the Internet and the maturation of the electronic market, more consumers make purchases and seek relevant product/service information online [14,

#

15]. According to Morrison [16], 81% of American shoppers engage in online search prior to making a purchase. Compared to brick-and-mortar stores, an online platform drastically increases the amount of information available to consumers [17] and lowers information acquisition costs [18]. In addition, as the Internet is capable of providing a “virtual experience” that can potentially convert experience attributes to search attributes, the gap between search products (e.g., furniture) and experience products (e.g., music) may be diminished [18].

Extending previous research in the nonelectronic market [4, 16, 17] and integrating both the economics approach and the psychological paradigm, this study investigates the key determining factors of online prepurchase search. Specifically, we focus on four wellacknowledged predictors of prepurchase search, namely market environment, use of decision aids tool, product type, and consumer experience. We consider that to make a better purchase decision online, consumers search and locate web stores of interest and acquire meaningful information regarding products and web stores (e.g., specification lists, consumer feedback, and/or multimedia presentations). This process requires a considerable amount of cognitive effort, which, in turn, affects consumers’ extent of search. To deal with this information overload, consumers may rely on advanced information access technologies and decision aid tools to improve search efficiency and reduce search cost. In addition, consumers may possess different search motivations for different products because the potential search payoff could be greater for some products than for others (e.g., experience product vs. search product). Further, individual characteristics such as online purchase experience and product specific experience can directly affect the cognitive cost involved in the search and therefore influence the extent of external search.

##

The extent of external search has been the most prevalent indicator of consumers search activities [1, 3, 5, 19]. Measures of the extent of external search in prior studies investigating traditional brick-and-mortar stores typically used a variety of self-reported items (e.g., number of information sources used, number of types of information sought, number of alternatives considered, and time spent on the purchase decision) [1, 20]. Because data are often collected many months after consumers completed a purchase, the validity of such measurements is often reduced due to selective retention and failure to remember the search [1]. To overcome these issues, the present study uses a disaggregated dataset of website visitation and transaction activities collected in 2004 by ComScore to investigate these antecedents. With the availability of website visitation and transaction logs, this study captures the extent of external search using the number of online stores consumers actually visited prior to completing a transaction for a particular product.

The contributions of the study are twofold. First, it is among the first to show that an online platform does not automatically increase consumers’ prepurchase search; rather, the number of relevant websites visited for a purchase is contingent upon both economic and psychological antecedents. Previous researchers [4, 16, 17] have linked these key antecedents to the extent of prepurchase search in the nonelectronic market. However, the impact of these factors on search behavior in electronic market has not been examined. Furthermore, a simultaneous examination of both economic and psychological aspects of the antecedents advances our understanding of the relative importance of these antecedents in influencing online search. Second, prior studies have mainly examined consumers’ search behavior for a given store over time [21] or within a given store session [2, 22]. How consumers search across stores has received less attention. This study concentrates on competition among web stores for visits made by customers [3, 5]. A holistic investigation into the extent that consumers search among online retailers before making a purchase allows us to better understand the nature of online consumer behavior and the competition that exists in electronic environments [2, 3, 5, 23, 24].

The paper is organized as follows. Section 2 presents a theoretical background and develops research hypotheses. Section 3 describes the dataset and measures. Section 4 presents the empirical models, estimation method, and a summary of the results. Finally, Section 5 discusses the implications and conclusions of the study.

## 2. A Conceptual Model of Online Prepurchase Search

## 2.1. Theoretical Background

Search behavior is a function of both personal characteristics and task attributes [1]. The theoretical foundations of external information search in the nonelectronic market can be summarized in two broad perspectives: economic and psychological [19, 25].

The economic approach of information search uses a cost-benefit framework. The framework is developed from the economic objective of utility maximization, with its origin rooted in Stigler’s [10] seminal work. It implies that informed consumers, with a product in mind, search for the lowest price by trading off the expected cost and benefit and that they continue to acquire and process information until the marginal cost of acquiring that information exceeds the expected value of additional information [26]. The cost-benefit framework is well accepted and has been widely used to explain the extent of consumer information search in the traditional nonelectronic market. A general pattern has emerged

#

from this framework where cost-related factors—such as the effort or time needed to acquire and process information—reduce the extent of search. Consistent with this argument, previous research in the field of information systems illustrates that the use of advanced information access technology and decision aids significantly reduces cognitive effort in decision-making [27, 28], which in turn, would induce more search. The effects of market environment can also be observed in relation to the general pattern predicted by the cost-benefit (with regards to both economic and psychological cost and benefit) framework. As the number of competitors in a product market increases, the more variety and larger amount of information available; hence, the benefit of search may increase [20, 29].

Extending Stigler’s model, Nelson [30, 31] considers that consumers need to not only find price information but also assess product quality. These two attributes differ in levels of certainty. For example, price can be known with certainty prior to a purchase, while quality is only fully known after a purchase and some period of usage [30, 31]. Because it is more difficult for consumers to obtain information about product quality than about price prior to purchase, Nelson [30, 31] further classifies products into two categories: search and experience products. He argues that the behavior of information search for these two types of products may vary because of the level of uncertainty. For search products (e.g., a laptop), consumers can fully assess the quality prior to purchase with some certainty through the information (e.g., CPU configuration and size of hard disk) obtained from other sources. For experience products (e.g., video games), however, consumers are not able to evaluate the quality with certainty until they have tried the product or have utilized external information (e.g., other consumers testimonials) [32] to make quality inferences.

##

The psychological approach of information search investigates consumers’ motivation and capability of information processing. As cognitive misers, consumers have a limited cognitive capacity for information processing [33] and thus frequently rely on simple, timeefficient strategies to make decisions and evaluate information. To achieve various goals, consumers search for information both internally and externally [34, 35]. The extent of their external search is determined by how much they have already known and how much they would like to know about the products/services, as constrained by their cognitive capacity to process information [19]. Consumer knowledge is the interface connecting internal and external search and facilitates the interpretation of new external information [25]. As Newman and Staelin [29] suggest, experience leads to incremental knowledge that may be used in future internal searches.

Rather than behaving myopically, consumers may consider a current search to be an investment in product knowledge for future purchases and/or use their knowledge gained from previous searches or purchase experiences to guide their current search [36]. Putrevu and Ratchford [37] and Urbany et al. [36] introduce the concept of “human capital” to capture consumer knowledge accumulated over time. It is defined as “the stock of information and knowledge obtained in the past that makes the consumer more productive in the current period” [37]. Human capital includes two major components: information capital (i.e., knowledge about market/product such as price range and attributes of a product class) and knowledge capital (i.e., knowledge about how to search). These two components influence search differently: while knowledge capital makes consumers more efficient in terms of locating and processing information and thus facilitates a more extensive search [37, 38], information

capital can reduce external search, given that it decreases the expected benefit of external information [36, 37].

The economic and psychological approaches to search are complementary rather than competitive theoretical foundations [6, 19]. Synthesizing prior literature on search, this study proposes four aspects of factors to the extent of online prepurchase search and simultaneously examines their effects, including online market environment (competitive density), information access technologies, potential search payoff (search vs. experience products), and consumer online experience.

## 2.2. Hypothesis Development

## Online Market Environment

One of the most important online market environment factors is competitive density, which refers to the number of web stores that are competing in a product category (e.g., printers or laptops) [13]. Competitive density is high in fragmented markets (e.g., printer) where a large number of sellers compete in the marketplace (e.g., there are more than 100 printer manufacturers, see https://en.wikipedia.org/wiki/List\_of\_printer\_companies), as compared to concentrated markets (e.g., the laptop market) where a low number of sellers compete [13]. High competitive density increases the likelihood that more alternatives will match consumers’ needs, resulting in a larger consideration set to consumers. A larger consideration set induces more search [20], and consumers may visit more online stores for a product when the competitive density of that product market is high.

Although there are good reasons to expect that competitive density will promote online prepurchase search, the effect of competitive density on online prepurchase search may not be

#

linear. Pirolli [39] presents an analysis of the degree of search for two-star Paris hotels conducted through a popular hotel website. The analysis focuses on the relationship between price savings and information search. It shows a diminishing returns curve, where additional savings (i.e., the difference between the observed minimum price found so far and the first price encountered) decrease as one scans additional listings. This implies that the expected value of continuing to search diminishes as the extent of search goes up. Pirolli [39] posits that such an analysis can be applied to the diminishing returns of searching for the maximum value (as opposed to the minimum price), as might occur in searching for the best product. Similar diminishing returns curves are also observed in the studies on medical information seeking. Bhavnani et al [40, 41], for example, found that very few pages contain all melanoma risk concepts identified by experts, with many containing only one of these concepts. It was found that a user was expected to find all expert-identified melanoma risk facts within 25 page visits, and thus, search beyond the 25 pages would not have much additional value. Taken together, the forgoing discussion suggests that the impact of competitive density on search follows a function of diminishing return. Formally, we propose,

H1: Competitive density increases search, but there is a diminishing effect of competitive density on the number of web stores that consumers visit for a purchase.

## Information Access Technologies

When performing an online search, how accessible the information is to the consumers and the format of the information (i.e., information accessibility) will significantly affect their search cost [34]. In general, consumers will have lower search costs and process more

#

information if accessibility is high [42]. We consider that Internet connection speed and price comparison websites affect information accessibility, consequently affecting the extent of search.

Internet connection speed has long been viewed as one of the most important factors

affecting consumers’ search cost [47, 48], with those having slower Internet connection bearing

higher search cost. The slower the connection speed is, the longer the time it takes for a Web

client machine to receive and display a data file submitted by a Web server after that file is

requested by the client. Partially because of this, download delays impede the development

and use of Internet applications such as multimedia for B2C commerce and become a key

bottleneck to the functioning of e-commerce [43]. According to Zona Research [44],

approximately 30% of users abandon the retrieval process if the time to retrieve a web page

goes beyond 8 seconds. In a similar vein, Galletta et al. [45] found that longer download time

decreases satisfaction with the site, reduces intention to return, and causes fewer number of

tasks to be completed. As a result, there has been considerable emphasis on optimizing

resource utilization to improve websites’ response time [46]. Thus we propose,

H2: Consumers having faster Internet connection search more web stores for a

purchase.

We further expect that the use of price comparison websites increases prepurchase

search of a product, i.e., the number of stores consumers examine before placing an order for

that product. A price comparison website is a site that allows consumers to search for prices

and product characteristics from numerous competing web stores with one-click access. More

often consumers use price comparison (or comparison-shopping) websites such as BizRate (http://www.bizrate.com) and NextTag (http://www.nextag.com) for their purchases [47]. Taking queries from consumers, it returns the results directly from web stores and typically presents them in a consolidated and compact table format. It allows consumers to compare the characteristics of available products and click through directly to their chosen web stores. Price comparison websites can reduce the information overload faced by consumers and alleviate the required cognitive effort of gathering and screening vast amounts of product information available on the web [48, 49]. Such decision aids extend decision makers’ cognitive capacities so that they can analyze the problems in greater depth and scope [50, 51]. Therefore, we propose,

H3: Consumers using price comparison websites search more web stores for a purchase.<sup>1</sup>

Search Products versus Experience Products

Building on the economics of information search, Nelson [30, 31] classifies products into search and experience products according to consumers’ ability to obtain product quality information before purchase. Search products (e.g., laptops) are defined as those dominated by product attributes for which full information can be acquired prior to purchase, whereas experience products (e.g., video games) are dominated by the attributes that cannot be known until purchase and use of the product or for which information search is more costly and/or difficult than direct product experience. Nelson [30, 31] suggests that consumers will undertake more extensive search for search products than for experience products in the nonelectronic market because of the high cost and/or inability to obtain the valuable information for experience products prior to use.

Contradictory to this view, we argue that consumers engage in more online search for experience products than for search products because of the following two reasons. First, because of the advancement of information technology and the Internet, there is rich experiential information available online for experience products. Online stores utilize consumer feedback/reviews and multimedia presentations (e.g., photos, sound tracks, and video clips), and such ‘‘virtual experience” technologies enable consumers to easily learn from the experiences of others and gather product information that is often difficult to obtain in offline settings [18, 52, 53]. Second, because the quality of experience products is more uncertain and difficult to be evaluated than that of search products [30, 31], higher perceived risk is often related to experience products than to search products. Notably, our reasoning is consistent with the literature on product type and perceived risk. Murray [54], for example, finds that the more importance consumers placed on direct experience, the higher is the perceived risk because of the unavailability of search attribute information. Mitra et al. [8] further show that perceived risk increases along a continuum from search to experience products. However, information search is an effective means of risk reduction, and higher perceived risk leads to more search [55, 56]. Therefore, we propose,

H4: Consumers search fewer web stores for a search product than for an experience product.

Consumer Online Experience

As they search web stores to obtain relevant product and shopping information for a purchase, consumers may also use information stored in memory [20]. Two components of consumer online experience are considered in this study: (1) Internet purchase experience reflected by the number of purchases a consumer has made over the Internet and (2) produc specific experience indicated by whether a consumer has a recent online purchase within a target product category. We thus propose competing hypotheses (H5a vs. H5b and H6a vs. H6b) regarding the effect of consumer online experience on the number of web stores searched.

On the one hand, we argue that both types of experience increase consumers’ online search. With more online purchases, consumers’ skills and knowledge in online search could be improved, leading to the use of better search strategies and being more effective to locate the needed information [38, 57]. Such expertise enhances consumers’ ability to find appropriate websites and locate the necessary information to aid their purchase decision. Consistent with this argument, previous research shows that expertise in online search reduces effort and time in completing search tasks and yields greater number of correct results [57]. In terms of prior experience with the product category, it may improve consumers’ ability to analyze, elaborate on, and remember product information [58]. Thus, online experience improves consumers efficiency of search, thereby facilitating a more extensive search [38]. Therefore, we propose that,

H5a: Consumers having more Internet purchase experience search more web stores for a purchase.

H6a: Consumers having product-specific experience search more web stores for a

#

purchase.

On the other hand, with high online experience, consumers may be able to formulate better search strategies without engaging in the process of trial-and-error, therefore quickly locating the relevant websites without extensive external search. Furthermore, consumers wit high online experience may be more likely to retrieve relevant information from their memory (e.g., from which websites to buy). This may be especially true for consumers with high product-specific experience. For example, if a consumer made a recent purchase in a product category, he or she could have related product information accumulated from previous search activities (e.g., where to find the product, attributes used to evaluate the product, or the price range of the product). The consumer can use the information already stored in memory and conduct an information search internally [55]. If internally retrievable information and externally available information are interchangeable in helping a consumer make a purchase decision, then the more information obtained from searches for previous relevant purchases, the less is the need of external search for the current purchase [20]. Prior studies in the nonelectronics market suggest that the purchase and the use of a product result in learning, which later influences consumers’ buying behavior [29]. Consumers can rely on relevant information in memory from the previous purchase, reducing the need for external search. Therefore we propose,

H5b: Consumers having more Internet purchase experience search less web stores for a purchase.

H6b: Consumers having product-specific experience search fewer web stores for a purchase.

#

## 3. Data

To investigate the proposed hypotheses, this study used the 2004 ComScore Web-Behavior Panel. The dataset contains the website visitation and transaction information of 50,000 households (chosen at random from residents of all 50 states in the United States and the United States territories) made in 2004. For each website visitation, the dataset lists the visited Web domain name and the date/time of the visitation. For each purchase transaction, the dataset includes the name and category of the product purchased, the domain where the order was placed, and the time stamp of the transaction. The dataset also contains householdlevel demographic information, including household income, highest education level for any member of the household, age of the eldest of the household, household size, and the presence of children (Yes or No). The dataset has been used in a number of prior studies in understanding consumers’ online behavior [2,59]. The dataset is pertinent to this study for the following reasons. First, the markets of electronic commences in 2004 were still fragmented. B2C platforms such as Amazon, or C2C platforms such as eBay did not emerge as the dominating players at that time. Second, because electronic commerce was relatively new in 2004, this gives us an opportunity to observe the variation of customer online experience, Internet connection, and the use of price comparison. Finally, we do not believe the nature of consumers’ search and online purchases has changed much since this time as it is quite consistent and stable regarding how a website is constructed through the hyperlinks and HTML pages.

This study focused on modeling transactions related to electronic consumer products occurring in July and August 2004 for four reasons. First, by selecting the transactions in these two months, the systematic differences in prepurchase search that might occur during the endof-the-year holiday season was avoided [2]. Second, focusing on a relatively short time window also enables us to minimize the possible impact of new entries [60]. Third, using the transactions in these two months (instead of the entire year) allows us to develop meaningful measures for the important variables hypothesized in the conceptual model (such as competitive density, Internet purchase experience, and product-specific experience) based on the behavioral data recorded in preceding months (January to June). Fourth, we chose electronic consumer products for this study because of the varying degree of competition among the selected product categories and a relatively large number of transaction occurrences (as shown in Table 1).

## 3.1. Dependent Variable

To measure the extent of online prepurchase search for a transaction (or a purchase), the number of web stores that was visited by the consumer in the prepurchase search window (defined as 15 days preceding the purchase date) was used. Consumers’ visitations to those stores with product offerings in the targeted product category (based on their transaction history) were counted. We chose the 15-day prepurchase search window following prior research relying on behavioral data [2, 3, 5], which suggests that online prepurchase search for a product typically happens within 15 days before a purchase. In addition, within a time span of 15 days, very few people make more than one purchase in the same product category [13]. Consistent with this reasoning and in line with previous studies, only few panelists (<1%) in the dataset were found to make two or more purchases for products in the same category during the 15-day period, and these transactions were dropped from the analysis because of the

#

overlapping of search windows. The final sample includes 552 transactions, with a total of 1435 web store visitations (including those visitations resulting in transactions) associated with these transactions. On average, consumers searched 2.6 web stores per transaction. Figure 1 shows the distribution of the number of web stores searched for a purchase in our sample.

Table 1 lists the breakdown of transactions by product categories. The definition of product category ID and product name follows ComScore, and each transaction represents a single purchased item. Table 1 also presents the mean and the standard deviation of web stores visited for a purchase in different product categories.

## 3.2. Independent Variables

We measured the competitive density of a product category (denoted as COMP) by the number of web stores that offered products within the product category. The measure was derived on the basis of the transactions that occurred in the first 6 months of 2004 in the dataset. Table 1 presents competitive density for each category and shows the percentage of sales revenue by the top four stores (which was calculated on the basis of all transactions that occurred in 2004) for each category. Biggadike [61] categorizes markets into three groups on the basis of the percentage of sales revenue made by the top four firms in a market: concentrated (the percentage is equal to or greater than 75%), moderate (the percentage is between 55% and 75%), and fragmented (the percentage is equal to or below 55%). Following this approach, four product categories (IDs = 25, 26, 27, and 33) are in the concentrated market, five (IDs = 28, 30, 31, 32, and 34) in the fragmented market, and four (IDs = 7, 29, 36, and 37) in the moderate market. The product categories lie on a continuum with some product categories shifted toward a concentrated market and others toward a fragmented market. As expected [13], competitive density is high in fragmented markets and low in concentrated markets.

A consumer’s Internet purchase experience (denoted as INTN) was measured by the number of transactions the household had in 2004 prior to the focal one. A binary variable (denoted as PROD) was used to capture a consumer’s product-specific experience: it is 1 if the household had purchased the same product category in the preceding months before the focal transaction and 0 otherwise. Both INTN and PROD were derived on the basis of the transaction history of consumers in the dataset.

A binary variable, SRCH, was used to indicate whether the purchased product in a transaction is a search product or an experience product (1 = search; 0 = experience). Following prior studies [7, 31, 62-64], product categories 7, 27, 29, 31, 32, and 36 were classified as experience products and the rest as search products.

Consumers’ Internet connection speed (HCON; a binary variable, with dial-up = 0, and broadband = 1) was collected directly from the ComScore data. A binary code (PRCM) was used to indicate whether a consumer visited a price comparison website or not (1 = Yes; 0 = No) in the search window based on the consumer visitation activities in the dataset. A list of price comparison websites for electronic consumer product was identified on the basis of the Google Directory of Price Comparison Websites. The descriptive statistics of these main variables and their correlation coefficients are summarized in Table 2.

Household demographics in the dataset—including household income (HINC), highest education level for any member of the household (HEDU), age of the eldest of the household (HAGE), household size (HSIZ), and the presence of children (HCHI)—were included as control variables in the model.

## 4. Empirical Model and Estimation Results

## 4.1. Empirical Model

Following Johnson et al. [3], we considered that the expected benefit of continuing search for a purchase and the probability of soliciting information from an additional site decrease as the number of web stores visited increases. We may model the probability that a consumer searches an $y ^ { \mathrm { t h } }$ site as a decrement of the probability of visiting the $( y - 1 ) ^ { \mathsf { t h } }$ site:

$$
\operatorname * {P r} [ Y = y ] = \frac {(y - 1) \theta}{y} \operatorname * {P r} [ Y = y - 1 ]\tag{1}
$$

where $y = 2 , 3 , \ldots$ , and $\vartheta$ is a measure of a consumer’s unobserved propensity of search for a transaction $( 0 < \vartheta < 1 )$ . The relationship results in a logarithmic distribution for the number of unique web stores searched before making a purchase [65]:

$$
\operatorname * {P r} [ Y = y ] = \frac {a \theta^ {y}}{y}\tag{2}
$$

where $y = 1 , 2 , 3 , . . . . ,$ and $a = - \frac { 1 } { \ln ( 1 - \theta ) }$ . We considered a consumer’s search propensity (θ) varies across transactions and is a function of the set of independent variables. Given that it is constrained to be between 0 and 1, we first applied a logistic transformation on $\vartheta \colon$

$$
q = \frac {e ^ {q ^ {*}}}{1 + e ^ {q ^ {*}}}\tag{3}
$$

And then we modeled

$$
\begin{array}{l} q ^ {*} = b _ {0} + b _ {1} * \log (C O M P) + b _ {2} * H C O N + b _ {3} * P R C M + b _ {4} * S R C H \\ \qquad + b _ {5} * I N T N + b _ {6} * P R O D + b _ {7} * H I N C + b _ {8} * H E D U \\ \qquad + b _ {9} * H A G E + b _ {1 0} * H S I Z + b _ {1 1} * H C H I + e \\ e \sim n o r m a l (0, s _ {e}) \end{array}\tag{4}
$$

ε is an error term used to capture unobserved heterogeneity. $\theta _ { i } ( \mathfrak { i } { = } 0 , 1 , { \ldots } , 1 1 )$ is a set of coefficients, and $\sigma _ { \varepsilon }$ is the standard deviation of error term whose distribution is to be estimated.

## 5.2. Estimation Method and Results

Because of the complexity of the model, we estimated the coefficients by using the Markov Chain Monte Carlo (MCMC) method to obtain their distributions. MCMC essentially draws samples from the desired distributions by running a cleverly constructed Markov chain for a long time and then forms sample averages to approximate expectations (see [66] for a detailed discussion on MCMC). In our estimation, we use uninformative but proper priors for the model. Particularly, we specified

$$
b _ {i} \sim \text { normal } (0, 1 0 0), i = 0, 1,..., 1 1
$$

$$
\sigma_ {\varepsilon} \sim g a m m a (1, 1)
$$

Following standard practices, we simulated multiple chains. Each chain had 12,000 iterations, and the first 6000 were discarded as an initial burn-in. We monitored and plotted the traces of each model parameters for all chains to confirm the adequacy of convergence of the model. All plots showed convergence. The Gelman-Rubin convergence statistic [67] also demonstrated evidence of sufficient convergence.

We used deviance information criteria (DIC) [68] to compare alternative models. DIC is calculated by adding pD, a measure of the effective number of parameters in a model, to the posterior mean deviance, a Bayesian measure of fit or adequacy. DIC is intended as a generalization of Akaike’s information criterion (AIC). In the same spirit as AIC, the minimum DIC estimates the model that will make the best short-term predictions (refer to [68] for a full discussion on DIC).

Table 3 summarizes the estimated coefficients, along with their 90% and 95% confidence intervals calculated on the basis of the MCMC simulations. To test the diminishing effect of competitive density on the extent of search, the natural log form of competitive density was included in the regression as one of the independent variables. We had a significant positive coefficient (log(COMP): b = .98, p < .05). We tested an alternative specification in which we used COMP instead of log(COMP) as the independent variable. We found that the DIC of the model changed from 1756 to 1770, indicating that using log(COMP) provides a better fit than using COMP. Therefore, H1 is supported.

The results also indicate that consumers who have broadband connection visit more web stores (HCON: b = .33, p < .10), marginally supporting H2. Consistent with H3, consumers who use price comparison sites visit more stores (PRCM: b = 1.01, p < .05). Supporting H4, we found that consumers tend to search fewer web stores for search products than they do for experience products (PROD: b = -.35, p < .05). The results further show a positive significant relationship for Internet purchase experience (INTN(10<sup>-2</sup>): $b = . 8 6 .$ $p < . 0 5 )$ but a negative coefficient for product-specific experience (PROD: b = -.43, $p < . 0 5 )$ . Thus, H5a and H6b are supported but not H5b and H6a. We did not find significant effects of any of the household

demographic variables.

## 4.3. Robustness Check

As an alternative specification to Equation (1), we may model the probability that an individual searches an $y ^ { \mathrm { t h } }$ site as a decrement of the probability of visiting the $( y - 1 ) ^ { \mathsf { t h } }$ site:

$$
\operatorname * {P r} [ Y = y ] = \frac {\lambda}{y} \operatorname * {P r} [ Y = y - 1 ]\tag{5}
$$

where $y = 2 , 3 , \ldots$ , and $\lambda$ is a parameter to reflect a consumer’s search propensity $( \lambda > 0 )$ . With the relationship, we have a zero-truncated Poisson distribution for the number of unique web stores visited for a purchase [65]:

$$
P [ Y = y ] = \frac {1}{1 - e ^ {- \lambda}} \frac {e ^ {- \lambda} \lambda^ {y}}{y !}\tag{6}
$$

To capture the change of search propensity, we modeled

$$
\begin{array}{l} \log (\lambda) = \gamma_ {0} + \gamma_ {1} * \log (C O M P) + \gamma_ {2} * I N T N + \gamma_ {3} * P R O D + \gamma_ {4} * S R C H \\ \qquad + \gamma_ {5} * H C O N + \gamma_ {6} * P R C M + \gamma_ {7} * H I N C + \gamma_ {8} * H E D U \\ \qquad + \gamma_ {9} * H A G E + \gamma_ {1 0} * H S I Z + \gamma_ {1 1} * H C H I + \nu \\ \nu \sim n o r m a l (0, \sigma_ {\nu}) \end{array}\tag{7}
$$

ν is an error term used to capture unobserved heterogeneity. $\scriptstyle \gamma _ { i } ( \mathsf { i } = 0 , 1 , \ldots , 1 1 )$ is a set of coefficients, and $\sigma _ { \nu }$ is the standard deviation of the error term whose distributions are to be estimated. We used log transformation of λ as the dependent variable to ensure its positivity. We estimated the model by using the MCMC method with uninformative but proper priors:

$$
\gamma_ {i} \sim n o r m a l (0, 1 0 0), i = 0, 1, \dots , 1 1
$$

$$
\sigma_ {v} \sim g a m m a (1, 1)
$$

Table 4 summarizes the estimation results. As we can see, the results of hypothesis testing are consistent with those in Table 3. The DIC of the model does not significantly change when

#

compared to that for the logarithmic model in the previous section.

## 5. Discussion and Implications

Extending prior studies on consumer online search and grounded in theories on information search and information systems, our study demonstrates that the extent of online prepurchase search is affected by both economic factors (online market environment, information access technologies, and product type) and psychological factors (consumer online experience).

Several key findings were found. First, competitive density increases search, but there is a diminishing effect on consumers’ online prepurchase search. Consumers search more online stores before making a purchase when there are more competitors in the product market. However, the impact of competitive density on search follows a diminishing returns curve. Second, the use of advanced information technologies (such as high-speed Internet connection and price comparison websites) induces more searches. These two technologies reduce search cost and allow searches to be performed with ease. Third, product characteristics influence search behavior, with consumers visiting more web stores for experience products than for search products. This pattern is in contrast to Neilson’s prediction on the extent of search in the nonelectronic market. The online environment provides more information on experience products as compared to the traditional brick-and-mortar store. Finally, our study differentiates two types of online experience—online purchase experience and product specific experience— and shows that these two types of experience have different effects on the extent of online prepurchase search: online purchase experience increases search, whereas product-specific experience reduces search.

##

Though it is believed that the Internet has reduced consumers’ search cost, previous research using aggregated data shows that the use of online prepurchase search is surprisingly limited. For example, on the basis of the 1997–98 click-stream data collected by ComScore, Johnson et al. [3] found that, on average, households visit only 1.2 book sites, 1.3 CD sites, and 1.8 travel sites before making a purchase in an active month. Similarly, Adamic and Huberman [69] report that the top 1% of sites on the Web capture 50% of all visits, indicating that shoppers limit their searches to a few popular sites. Our study suggests that the low level of search found in previous studies may be because of the infancy of electronic markets, where competitive density of the investigated product categories was low and most consumers only had low-speed Internet connections (i.e., dial-up). In addition, as suggested in prior studies [3], our results also indicate that the low-level use of price comparison websites and the low percentage of consumers that have extensive Internet purchase experience lead to the low level of search.

This research is among the first to integrate economic and psychological perspectives to understand the key antecedents that affect consumers’ extent of online prepurchase search. Although previous research has linked these factors to the extent of prepurchase search in the nonelectronic market, these factors are examined sporadically in different studies. We do not know whether their effects may be diluted at the presence of other factors. The present research resolves this issue by simultaneously examining these variables in the same model, which allows a deeper understanding of the relative importance of these factors. Our finding shows that economic factors and psychological factors are not substitutes; rather, they are complementary, as shown by the significant effects of all four focal factors in the model.

#

Furthermore, several other implications can be derived from this study. First, the diminishing effect of competitive density on the extent of search indicates that the number of competitors in a market intensifies market competition. However, competition intensity of a market does not linearly increase with the number of competitors. When the number of competitors in a market reaches a certain threshold, competition intensity may be maximized (e.g., reaching a perfect competition status) and additional competitors may not further increase competition intensity. Thus, in a concentrated market, a new entry could impose a significant impact on incumbents, while this may not be the case in a fragmented market. Armed with this information, managers of firms in a concentrated market should focus on developing customer retention programs (e.g., loyalty programs) to enhance their relationship with target consumers as an effective strategy to compete with new entries. In contrast, executives of companies in a fragmented market should center on customer acquisition (vs. retention) programs because new entries may impose less severe threats to them. More promotional budgets should be allocated for discounts, coupons, and free trials as effective strategies to attract new customers.

Second, our results also indicate that consumers with more online purchase experience or using advanced information technologies may be less loyal to a web store. Thus, online retailers should keep track of the preferences or shopping habits of such customers and attract them with behavioral targeting techniques and appealing store design that fits with their characteristics [70]. It might also be profitable for marketers to utilize the interactive nature of the Web to facilitate communications with consumers, by either providing “virtual advisors” or offering customer testimonials in a nonintrusive way. Customers with previous purchase

experience in the product category tend to exhibit more loyal behavior. To acquire such customers, it is important for online retailers to reach them through targeted advertising [71] (such as personalized emails and smart banners) as they are less likely to search for information.

Third, we also find that consumers show different levels of online prepurchase search for different types of products in such a way that they tend to visit more web stores for experience products than for search products. Therefore, it is important for a web store to develop different marketing strategies for different types of products [72]. For experience products, it may be important to reduce consumers’ risk perception and increase stickiness by providing such experiential information as consumer feedback and virtual tours. For example, Marissol-Coralia Hotel in Guadeloupe offers prospective or visiting clients a 10-minute tour guided by the experienced front-line employees showcasing the features and services available at the hotel. This process is successful in reducing consumers’ evaluation difficulty by providing an experimental information reference point [73]. Similar strategies are used in the interactive home shopping channel as well, where online marketers are trying to facilitate consumers decision-making by offering them electronic aides in real estate hunting.

We acknowledge that there are several limitations in this study. First, our variables and measures are constrained by this particular dataset. Other individual differences not examined in this study (e.g., self-efficacy in search, situational involvement, and desire for optimal decision) may be investigated in the future through survey or lab experiments regarding their impact on online search. Second, while it was believed that increased search indicates intensified competition, what mitigates the impact of search and helps gain competitive

advantages for a web store is another direction for future studies. Third, in this study, visitations to the websites that do not sell products (such as product review communities or the websites of manufacturing companies) were not counted as part of search. Though such websites do not directly compete with web stores for customers, they may provide important information for consumers. Visitation behavior to such websites for a purchase should be explored in future research.

Acknowledgment: We thank the review panel for their critical comments that have greatly improved the paper. The research of the first author was supported by the National Science Foundation under grants SES-1420758. The usual disclaimer applies.

## References

[1] S.E. Beatty, S.M. Smith, External Search Effort: An Investigation Across Several Product Categories The Journal of Consumer Research 14 (1987) 83-95

[2] P. Huang, N.H. Lurie, S. Mitra, Searching for Experience on the Web: An Empirical Examination of Consumer Behavior for Search and Experience Goods, Journal of Marketing, 73 (2009) 55-69.

[3] E.J. Johnson, W.W. Moe, P.S. Fader, S. Bellman, G.L. Lohse, On the Depth and Dynamics of Online Search Behavior, Management Science, 50 (2004) 299-308.

[4] T. Lauraeus-Niinivaara, T. Saarinen, A. Sunikka, A. Öörni, Relationship between Uncertainty and Patterns of Pre-purchase Consumer Search in Electronic Markets, in: the 41st Hawaii International Conference on System Sciences, IEEE, 2008.

[5] J.J. Zhang, X. Fang, O.R.L. Sheng, Online Consumer Search Depth: Theories and New Findings, Journal of Management Information Systems, 23 (2006) 71–95.

[6] S. Moorthy, B.T. Ratchford, D. Talukdar, Consumer Information Search Revisited: Theory and Empirical Analysis, The Journal of Consumer Research, 23 (1997) 263-277.

[7] L.-T. Bei, E.Y.I. Chen, R. Widdows, Consumers’ Online Information Search Behavior and the Phenomenon of Search and Experience Products, Journal of Family and Economic Issues, 25 (2004) 449- 467.

[8] K. Mitra, M.C. Reiss, L.M. Capella, An examination of perceived risk, information search and behavioral intentions in search, experience and credence services, THE JOURNAL OF SERVICES MARKETING, 13 (1999) 208-228.

[9] W.L. Moore, D.R. Lehmann, Individual Differences in Search Behavior for a Nondurable The Journal of Consumer Research, 7 (1980) 296-307

[10] G.J. Stigler, The Economics of Information, Journal of Political Economy, 72 (1961) 44-61.

[11] R.J. Avery, Determinants of search for nondurable goods: An empirical assessment of the economics of information theory, Journal of Consumer Affairs, 30 (1996) 390-420.

[12] H.A. Simon, Administrative Behavior: A Study of Decision-making Processes in Administrative Organization Macmillan Publishers, New York, USA, 1947.

[13] G.B. Voss, Z.G. Voss, Competitive Density and the Customer Acquisition–Retention Trade-Off, Journal of Marketing, 72 (2008) 3-18.

[14] M. Madden, L. Rainie, America's Online Pursuits, in, Pew Internet & American Life Project, Washington, D.C., 2003.

[15] A. Bhatnagar, S. Ghose, An Analysis of Frequency and Duration of Search on the Internet, Journal of Business, 77 (2004) 311-330.

[16] K. Morrison, 81% of Shoppers Conduct Online Research Before Buying in: AdWeek, 2014.

[17] R. Glazer, Marketing in an information-intensive environment: strategic implications of knowledge as an asset, Journal of Marketing, 55 (1991) 1-19.

[18] L.R. Klein, Evaluating the Potential of Interactive Media through a New Lens: Search versus Experience Goods, Journal of Business Research, 41 (1998) 195–203.

[19] L. Xia, K.B. Monroe, Consumer Information Acquisition: A Review and an Extension, Review of Marketing Research, 1 (2004) 101-152.

[20] G.N. Punj, R. Staelin, A Model of Consumer Information Search Behavior for New Automobiles, The Journal of Consumer Research, 9 (1983) 366-380.

[21] W.W. Moe, P.S. Fader, Dynamic Conversion Behavior at E-Commerce Sites, Management Science, 50 (2004) 326–335.

[22] R.E. Bucklin, C. Sismeiro, A Model of Web Site Browsing Behavior Estimated on Clickstream Data, Journal of Marketing Research, XL (2003) 249–267.

[23] Y.-H. Park, P.S. Fader, Modeling Browsing Behavior at Multiple Websites, Marketing Science, 23 (2004) 280–303.

[24] A. Öörni, Consumer Search in Electronic Markets, European Journal of Information Systems, 12 (2003).

[25] N. Srinivasan, Pre-Purchase External Search for Information, in: V.A. Zeithaml (Ed.) Review of Marketing American Marketing Association, Chicago, 1990, pp. 153-189.

[26] M. Tavana, F.J. Santos-Arteaga, D.D. Caprio, K. Tierney, Modeling signal-based decisions in online search environments: A non-recursive forward-looking approach, Information & Management, 53 (2016) 207-226.

[27] P.A. Todd, I. Benbasat, The use of information in decision making: An experimental investigation of the impact of computer-based decision aids, MIS Quarterly, 16 (1992) 373-393.

[28] P.A. Todd, I. Benbasat, Evaluating the Impact of DSS, Cognitive Effort, and Incentives on Strategy Selection, Information Systems Research, 10 (1999) 356-374.

[29] J.W. Newman, R. Staelin, Prepurchase Information Seeking for New Cars and Major Household Appliances, Journal of Marketing Research, 9 (1972) 249-257.

[30] P. Nelson, Information and Consumer Behavior, The Journal of Political Economy, 78 (1970) 311- 329.

[31] P. Nelson, Advertising as Information The Journal of Political Economy 82 (1974) 729-754

[32] K.B. Monroe, Pricing: Making Profitable Decisions, 3rd ed., McGraw-Hill/Irwin, Burr Ridge, IL, 2003.

[33] G.A. Miller, Themagic number seven, plusor minus two: some limits on our capacity for processing information, The Psychological Review, 63 (1956) 81–97.

[34] J.R. Bettman, An Information Processing Theory of Consumer Choice Addison-Wesley Publishing Compan Reading, MA, 1979.

[35] P.L. Wright, Consumer Choice Strategies: Simplifying vs. Optimizing, Journal of Marketing Research, 12 (1975) 60-67.

[36] J.E. Urbany, P.R. Dickson, R. Kalapurakal, Price search in the retail grocery market, Journal of Marketing, 60 (1996) 91–104.

[37] S. Putrevu, B.T. Ratchford, A Model of Search Behavior with an Application to Grocery Shopping, Journal of Retailing, 73 (1997) 463-486.

[38] S. Shim, M.A. Eastlick, S.L. Lotz, P. Warrington, An Online Prepurchase Intentions Model: The Role of Intentions to Search, Journal of Retailing, 77 (2001) 397-416.

[39] P. Pirolli, Information Foraging Theory: Adaptive Interaction with Information, Oxford University Press, New York, 2007.

[40] S.K. Bhavnani, Why Is It Difficult to Find Comprehensive Information? Implications of Information Scatter for Search and Design, Journal Of The American Society For Information Science And Technology, 56 (2005) 989–1003.

[41] S.K. Bhavnani, R.T. Jacob, J. Nardine, F.A. Peck, Exploring the Distribution of Online Healthcare Information, in: CHI 2003 Conference on Human Factors in Computing Systems, Ft. Lauderdale, FL, 2003.

[42] J.R. Bettman, E.J. Johnson, P. John W, Consumer Decision Making, in: T.S. Robertson, H.H. Kassarjian (Eds.) Handbook of Consumer Research, Prentice Hall, Englewood Cliffs, NJ, 1991.

[43] G. Rose, H. Khoo, D. Straub, Current Technological Impediments to Business-to-Consumer Electronic Commerce, Communications of the AIS, 1 (1999) 1-74.

[44] Zona Research Inc., The Economic Impacts of Unacceptable Web Site Download Speeds, in, Zona Research, Redwood City, CA, 1999.

[45] D.F. Galletta, R. Henry, S. McCoy, P. Polak, Web Site Delays: How Tolerant are Users?, Journal of the Association for Information Systems, 5 (2004) 1-28.

[46] J. Wang, R. Sharman, R. Ramesh, Shared Content Management in Replicated Web Systems: A Design Framework Using Problem Decomposition, Controlled Simulation, and Feedback Learning, IEEE TRANSACTIONS ON SYSTEMS, MAN, AND CYBERNETICS—PART C: APPLICATIONS AND REVIEWS, 38 (2008) 110-124.

[47] R.R. Burke, Technology and the customer interface: What consumers want in the physical and virtual store, Journal of the Academy of Marketing Science, 31 (2002) 109–126.

[48] B. Xiao, I. Benbasat, Customer decision support systems for e‑ commerce: Design and adoption of e‑ commerce product recommendation agents, MIS Quarterly, 31 (2007) 217–309.

[49] R.E. Hostler, V.Y. Yoon, Z. Guo, T. Guimaraes, G. Forgionne, Assessing the impact of recommender agents on on-line consumer unplanned purchase behavior, Information & Management, 48 (2011) 336-343.

[50] J. Song, D. Jones, N. Gudigantala, The effects of incorporating compensatory choice strategies in Web-based consumer decision support systems, Decision Support Systems, 43 (2007) 359–374.

[51] R.E. Hostlera, V.Y. Yoona, T. Guimaraes, Assessing the impact of internet agent on end users’ performance, Decision Support Systems, 41 (2005) 313– 323.

[52] J.G. Lynch, D. Ariely, Wine Online: Search Costs Affect Competition on Price, Quality, and Distribution, Marketing Science, 19 (2000) 83–103.

[53] J. Lee, J.-N. Lee, Understanding the product information inference process in electronic word-ofmouth: An objectivity–subjectivity dichotomy perspective, Information & Management, 46 (2009) 302- 311.

[54] K. Murray, A Test of Services Marketing Theory: Consumer Information Acquisition Activities, Journal of Marketing, 55 10–21.

[55] J.B. Schmidt, R.A. Sprang, A Proposed Model of External Consumer Information Search, Journal of the Academy of Marketing Science, 24 (1996) 246-256.

[56] N. Srinivasan, B.T. Ratchford, An Empirical Test of a Model of External Search for Automobiles, Journal of Consumer Research, 18 (1991) 233-242.

[57] J.R. Hill, M.J. Hannafin, Cognitive strategies in the use of a hypermedia information syste, Educational Technology Research and Development, 45 (1997) 37-64.

[58] Alba J. W., H.J. W, Dimensions of consumer expertise, Journal of Consumer Research, 13 (1987) 411-454.

[59] M. Wimble, J. Tripp, B. Phillips, N. Milic, On search cost and the long tail: the moderating role of search cost, Information Systems and e-Business Management, 4 (2016) 507–531.

[60] W.W. Moe, S. Yang, The Impact of a New Competitive Entry on an Incumbent’s Customer Base,

Journal of Marketing, 73 (2009) 109-121.

[61] E.R. Biggadike, Corporate diversification: Entry, strategy, and performance, Harvard University Press, Boston, 1979.

[62] S.M. Mudambi, D. Schuff, What Makes A Helpful Online Review? A Study Of Customer Reviews On Amazon.Com, MIS Quarterly, 34 (2010) 185-200.

[63] D. Weathers, S. Sharma, S.L. Wood, Effects of Online Communication Practices on Consumer Perceptions of Performance Uncertainty for Search and Experience Goods, Journal of Retailing, 83 (2007) 393-401.

[64] J. Bragge, J. Storgårds, Utilizing Text-Mining Tools to Enrich Traditional Literature Reviews. Case: Digital Games, in: the 30th Information Systems Research Seminar in Scandinavia, Tampere, Finalnd, 2007, pp. 1-24.

[65] N.L. Johnson, S. Kotz, A.W. Kemp., Univariate Discrete Distributions, 2nd ed., John Wiley and Sons, New York, 1993.

[66] A. Gelman, J.B. Carlin, H.S. Stern, D.B. Rubin, Bayesian Data Analysis, 2nd ed., Chapman & Hall/CRC, Boca Raton, 2003.

[67] S. Brooks, A. Gelman, Alternative methods for monitoring convergence of iterative simulations, Journal of Computational and Graphical Statistics, 7 (1998) 434-455.

[68] D.J. Spiegelhalter, N.G. Best, B.P. Carlin, A.v.d. Linde, Bayesian measures of model complexity and fit, Journal of the Royal Statistical Society: Series B (Statistical Methodology), 64 (2002) 583–639.

[69] L.A. Adamic, B.A. Huberman, The Web’s hidden order, Communications of the ACM, 44 (2001) 55–59.

[70] T.S. Raghu, P.K. Kannan, H.R. Rao, A.B. Whinston, Dynamic profiling of consumers for customized offerings over the Internet: a model and analysis, Decision Support Systems, 32 (2001) 117- 134.

[71] K. Li, E.C. Idemudia, Z. Lin, Y. Yu, A framework for intermediated online targeted advertising with banner ranking mechanism, Information Systems and E-Business Management, (Forthcoming).

[72] M.Y. Kiang, T.S. Raghu, K.H.-M. Shang, Marketing on the Internet — who can benefit from an online marketing approach?, Decision Support Systems, 27 (2000) 383-393.

[73] M. Laroche, Z. Yang, G.H.G. McDougall, J. Bergeron, Internet versus Bricks-and-mortar Retailers: An Investigation into Intangibility and Its Consequences, Journal of Retailing, 81 (2005) 251-267

# An investigation into the antecedents of pre-purchase online search

## Biography

Jingguo Wang is an Associate Professor of Information Systems at the University of Texas at Arlington. He received his PhD in Management Science and Systems from the State University of New York at Buffalo. His current research interests are in the areas of cybercrime and information security, information search, and decision-making. His work has been published in MIS Quarterly, Information Systems Research, Journal of Management Information Systems, ACM Transactions on Management Information Systems, IEEE Transactions on Systems, Man and Cybernetics (Part C), European Journal of Operational Research, and Decision Support Systems, among others. His research has been supported by University of Texas at Arlington and the National Science Foundation.

Zhiyong Yang is an Associate Professor of Marketing at the University of Texas at Arlington. His research focuses on two aspects of social influence, namely peer influence and parental/leadership influence. Along the line of peer influence, he examines how the opinion from others affects individuals’ new product adoption, product choice, donation, and saving behavior. In the perspective of parental/leadership influence, he centers primarily on (1) the effect of parental style on children’s smoking trajectory and music piracy behavior and (2) the impact of leadership style on frontline employees’ and salespeople’s job performance. His work has appeared in the Journal of Marketing, Journal of Consumer Research, Journal of the Academy of Marketing Science, Journal of Retailing, Journal of Public Policy & Marketing, Journal of Personal Selling & Sales Management, Journal of Business Research, Journal of Service Research, Journal of Macromarketing, Risk Analysis, and a number of peer-reviewed proceedings. His research has been funded by Statistics Canada, Fonds québécois de la recherche sur la société et la culture (FQRSC) of Canada, the National Science Foundation of China, and the University of Texas at Arlington. He currently serves on the editorial review boards of the Journal of Business Research and the Journal of Consumer Marketing.

E. Deanne Brocato is an Assistant Professor of Marketing at the Jon M. Huntsman School of Business at Utah State University. She investigates the role of consumer behavior in marketing decision-making. Her work has appeared in various journals such as the Journal of the Academy of Marketing Research, Journal of Retailing, Journal of Advertising, and Journal of Service Research.

![](/api/attachments/ZE2KWYMW/fulltext/images/a20a39051dfc9e3d5218536c1551d14a30ffe65486e669fe22a0fd996ec5b53a.jpg)  
Figure 1 The Distribution of the Number of Web Stores Searched for a Purchase

<table><tr><td>Product Category ID</td><td>Product Name</td><td>Number of Transactions</td><td>Mean of Web Store Visitations</td><td>Std of Web Store Visitations</td><td>Competitive Density</td><td>Sales Percent of Top Four Stores</td></tr><tr><td>7</td><td>Home Appliances</td><td>32</td><td>3.03</td><td>2.47</td><td>32</td><td>59.22%</td></tr><tr><td>25</td><td>Desktop Computers</td><td>7</td><td>2.86</td><td>2.54</td><td>16</td><td>91.07%</td></tr><tr><td>26</td><td>Laptop Computers</td><td>2</td><td>2.50</td><td>2.12</td><td>20</td><td>84.97%</td></tr><tr><td>27</td><td>Handhelds, PDAs, and Portable Devices</td><td>8</td><td>2.88</td><td>1.64</td><td>15</td><td>75.59%</td></tr><tr><td>28</td><td>Printers, Monitors, and Peripherals</td><td>48</td><td>3.60</td><td>3.42</td><td>49</td><td>45.23%</td></tr><tr><td>29</td><td>Computer Software (X Pc Games)</td><td>81</td><td>2.16</td><td>1.61</td><td>35</td><td>70.79%</td></tr><tr><td>30</td><td>Other Computer Supplies</td><td>75</td><td>3.13</td><td>2.24</td><td>62</td><td>48.53%</td></tr><tr><td>31</td><td>Audio and Video Equipment</td><td>40</td><td>3.58</td><td>2.54</td><td>40</td><td>38.94%</td></tr><tr><td>32</td><td>Cameras and Equipment</td><td>19</td><td>2.89</td><td>1.52</td><td>42</td><td>44.11%</td></tr><tr><td>33</td><td>Mobile Phones and Plans</td><td>145</td><td>1.52</td><td>0.99</td><td>18</td><td>79.57%</td></tr><tr><td>34</td><td>Other Electronics and Supplies</td><td>44</td><td>3.70</td><td>2.93</td><td>57</td><td>36.66%</td></tr><tr><td>36</td><td>Console Video Games</td><td>38</td><td>2.42</td><td>1.60</td><td>33</td><td>60.31%</td></tr><tr><td>37</td><td>Video Game Consoles and Accessories</td><td>13</td><td>2.54</td><td>2.93</td><td>23</td><td>67.25%</td></tr><tr><td></td><td>Total</td><td>552</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

Table 1 Descriptive Statistics of Product Categories

<table><tr><td></td><td>Mean</td><td>Std. Dev.</td><td>COMP</td><td>INTN</td><td>PROD</td><td>SRCH</td><td>HCON</td><td>PRCM</td></tr><tr><td>COMP</td><td>36.60</td><td>15.73</td><td>1.00</td><td>0.00</td><td>-0.13</td><td>0.68</td><td>0.15</td><td>0.07</td></tr><tr><td>INTN</td><td>0.63</td><td>2.34</td><td></td><td>1.00</td><td>0.50</td><td>-0.05</td><td>0.05</td><td>0.03</td></tr><tr><td>PROD</td><td>0.23</td><td>0.42</td><td></td><td></td><td>1.00</td><td>-0.19</td><td>-0.02</td><td>-0.01</td></tr></table>

<table><tr><td>SRCH</td><td>0.52</td><td>0.50</td><td>1.00</td><td>0.11</td><td>0.09</td></tr><tr><td>HCON</td><td>0.41</td><td>0.49</td><td></td><td>1.00</td><td>0.16</td></tr><tr><td>PRCM</td><td>0.62</td><td>0.48</td><td></td><td></td><td>1.00</td></tr></table>

Table 2 Descriptive statistics of the main variables and their correlation coefficients (n=552)

<table><tr><td>Coefficients</td><td>Mean</td><td>Standard Deviation</td><td>2.50%</td><td>5.00%</td><td>Median</td><td>95.00%</td><td>97.50%</td></tr><tr><td>Intercept</td><td>-3.17</td><td>0.74</td><td>-4.89</td><td>-4.62</td><td>-3.02</td><td>-2.28</td><td>-2.22</td></tr><tr><td>log(COMP)</td><td>0.98</td><td>0.15</td><td>0.76</td><td>0.78</td><td>0.94</td><td>1.25</td><td>1.27</td></tr><tr><td>HCON</td><td>0.33</td><td>0.19</td><td>-0.06</td><td>0.01</td><td>0.34</td><td>0.64</td><td>0.70</td></tr><tr><td>PRCM</td><td>1.01</td><td>0.19</td><td>0.63</td><td>0.69</td><td>1.02</td><td>1.31</td><td>1.38</td></tr><tr><td>SRCH</td><td>-0.35</td><td>0.18</td><td>-0.73</td><td>-0.67</td><td>-0.35</td><td>-0.05</td><td>0.00</td></tr><tr><td>INTN(* $10^{-2}$ )</td><td>0.86</td><td>0.42</td><td>0.09</td><td>0.21</td><td>0.83</td><td>1.59</td><td>1.73</td></tr><tr><td>PROD</td><td>-0.43</td><td>0.24</td><td>-0.88</td><td>-0.81</td><td>-0.43</td><td>-0.03</td><td>0.05</td></tr><tr><td>HINC</td><td>0.09</td><td>0.06</td><td>-0.02</td><td>0.00</td><td>0.09</td><td>0.20</td><td>0.22</td></tr><tr><td>HEDU</td><td>-0.01</td><td>0.09</td><td>-0.19</td><td>-0.15</td><td>-0.02</td><td>0.12</td><td>0.15</td></tr><tr><td>HAGE</td><td>-0.03</td><td>0.04</td><td>-0.11</td><td>-0.10</td><td>-0.03</td><td>0.04</td><td>0.05</td></tr><tr><td>HSIZ</td><td>0.03</td><td>0.09</td><td>-0.14</td><td>-0.12</td><td>0.03</td><td>0.18</td><td>0.21</td></tr><tr><td>HCHI</td><td>0.28</td><td>0.23</td><td>-0.17</td><td>-0.10</td><td>0.29</td><td>0.66</td><td>0.71</td></tr><tr><td> $\sigma_{\varepsilon}$ </td><td>0.15</td><td>0.06</td><td>0.06</td><td>0.06</td><td>0.13</td><td>0.27</td><td>0.28</td></tr></table>

Table 3 Estimation Results with the Logarithmic Model

<table><tr><td>Variable</td><td>Mean</td><td>Standard Deviation</td><td>2.50%</td><td>5.00%</td><td>Median</td><td>95.00%</td><td>97.50%</td></tr><tr><td>Intercept</td><td>-2.72</td><td>0.18</td><td>-3.15</td><td>-3.11</td><td>-2.71</td><td>-2.44</td><td>-2.44</td></tr><tr><td>log(COMP)</td><td>0.68</td><td>0.06</td><td>0.59</td><td>0.60</td><td>0.67</td><td>0.78</td><td>0.79</td></tr><tr><td>HCON</td><td>0.21</td><td>0.09</td><td>0.04</td><td>0.06</td><td>0.21</td><td>0.38</td><td>0.41</td></tr><tr><td>PRCM</td><td>0.77</td><td>0.09</td><td>0.58</td><td>0.61</td><td>0.78</td><td>0.92</td><td>0.95</td></tr><tr><td>SRCH</td><td>-0.30</td><td>0.08</td><td>-0.46</td><td>-0.44</td><td>-0.30</td><td>-0.15</td><td>-0.13</td></tr><tr><td> $INTN(*10^{-2})$ </td><td>0.21</td><td>0.11</td><td>-0.02</td><td>0.03</td><td>0.21</td><td>0.39</td><td>0.43</td></tr><tr><td>PROD</td><td>-0.24</td><td>0.13</td><td>-0.49</td><td>-0.45</td><td>-0.24</td><td>-0.04</td><td>0.00</td></tr><tr><td>HINC</td><td>0.05</td><td>0.03</td><td>0.00</td><td>0.00</td><td>0.05</td><td>0.09</td><td>0.11</td></tr><tr><td>HEDU</td><td>0.00</td><td>0.04</td><td>-0.09</td><td>-0.06</td><td>0.00</td><td>0.07</td><td>0.08</td></tr><tr><td>HAGE</td><td>0.00</td><td>0.02</td><td>-0.04</td><td>-0.03</td><td>0.00</td><td>0.03</td><td>0.03</td></tr><tr><td>HSIZ</td><td>0.03</td><td>0.05</td><td>-0.05</td><td>-0.04</td><td>0.04</td><td>0.11</td><td>0.12</td></tr><tr><td>HCHI</td><td>0.17</td><td>0.12</td><td>-0.07</td><td>-0.03</td><td>0.17</td><td>0.37</td><td>0.42</td></tr><tr><td> $σ_u$ </td><td>0.63</td><td>0.05</td><td>0.54</td><td>0.55</td><td>0.62</td><td>0.71</td><td>0.73</td></tr></table>

Table 4 Estimation Results with the Poisson Model

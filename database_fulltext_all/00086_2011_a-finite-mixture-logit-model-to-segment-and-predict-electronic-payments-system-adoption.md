---
otero_id: 86
otero_key: "QWH646XD"
title: "A Finite Mixture Logit Model to Segment and Predict Electronic Payments System Adoption"
authors: "Ravi Bapna; Paulo Goes; Kwok Kee Wei; Zhongju Zhang"
year: "2011"
journal: "Information Systems Research"
doi: "10.1287/isre.1090.0277"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/QWH646XD/fulltext/images/82ee5ab5b601c19abd78cad13698d5960a462ecf8f135745b207fd922150c533.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# A Finite Mixture Logit Model to Segment and Predict Electronic Payments System Adoption

Ravi Bapna, Paulo Goes, Kwok Kee Wei, Zhongju Zhang,

To cite this article:

Ravi Bapna, Paulo Goes, Kwok Kee Wei, Zhongju Zhang, (2011) A Finite Mixture Logit Model to Segment and Predict Electronic Payments System Adoption. Information Systems Research 22(1):118-133. http://dx.doi.org/10.1287/isre.1090.0277

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2011, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/QWH646XD/fulltext/images/4eb0e693e8d2427ba4720a2a52e075652ad3050b75c9031281feab013d882885.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# A Finite Mixture Logit Model to Segment and Predict Electronic Payments System Adoption

Ravi Bapna

Carlson School of Management, University of Minnesota, Minneapolis, Minnesota 55455, rbapna@umn.edu

Paulo Goes

Eller College of Management, University of Arizona, Tucson, Arizona 85721, paulo.goes@eller.arizona.edu

Kwok Kee Wei

College of Business, City University of Hong Kong, Kowloon, Hong Kong, isweikk@cityu.edu.hk

Zhongju Zhang

School of Business, University of Connecticut, Storrs, Connecticut 06269, john.zhang@business.uconn.edu

espite much hype about electronic payments systems (EPSs), a 2004 survey establishes that close to 80% of between-business payments are still made using paper-based formats. We present a finite mixture logit model to predict likelihood of EPS adoption in business-to-business (B2B) settings. Our model simultaneously classifies firms into homogeneous segments based on firm-specific characteristics and estimates the model’s coefficients relating predictor variables to EPS adoption decisions for each respective segment. While such models are increasingly making their presence felt in the marketing literature, we demonstrate their applicability to traditional information systems (IS) problems such as technology adoption. Using the finite mixture approach, we predict the likelihood of EPS adoption using a unique data set from a Fortune 100 company. We compare the finite mixture model with a variety of traditional approaches. We find that the finite mixture model fits the data better, controlling for the number of parameters estimated; that our explicit model-based segmentation leads to a better delineation of segments; and that it significantly improves the predictive accuracy in holdou samples. Practically, the proposed methodology can help business managers develop actionable segment-specific strategies for increasing EPS adoption by their business partners. We discuss how the methodology is potentially applicable to a wide variety of IS research.

Key words: finite mixture model; logistic regression; market segmentation; clustering analysis; hierarchical logi regression; electronic payments systems

History: M. S. Krishnan, Senior Editor; Pei-Yu Chen, Associate Editor. This paper was received on May 17, 2007, and was with the authors for 9 <sup>3</sup> months for 3 revisions. Published online in Articles in Advance February 19, 2010.

## 1. Introduction

The study of innovation diffusion and technology acceptance, both from an individual user as well as an organization’s perspective, has occupied the attention of information systems (IS) researchers over the last two decades or so (see Jeyaraj et al. 2006 for an extensive review). Various theories, such as the theory of reasoned action (Fishbein and Ajzen 1975), the innovation diffusion theory (Tornatzky and Klein 1982, Rogers 1995), the technology acceptance model (Davis 1989, Davis et al. 1989), network externality effects (Abrahamson and Rosenkopf 1997), and the rational expectations theory (Au and Kauffman 2003) have been proposed and constantly referenced as the theoretical foundation to understand the determinants and antecedents of technology diffusion. Subsequent empirical research (among many others, Agarwal and Prasad 1997; Agarwal et al. 2000; Au et al. 2005;

Kauffman et al. 2000; Brancheau and Wetherbe 1990; Compeau and Higgins 1995; Hart and Saunders 1997, 1998; Iacovou et al. 1995; Teo et al. 1995, 2003; Karahanna and Straub 1999; Plouffe et al. 2001; Reich and Benbasat 1990; Straub et al. 1997; Taylor and Todd 1995; Venkatesh 2000; Venkatesh and Davis 1996) have all (or at least partially) confirmed the explanatory power of the above-mentioned theories in many problem contexts.

With a view to complement the extant understanding of technology adoption, this research is motivated by the following problem faced by a Fortune 100 company that sought our help:

We are very keen to optimize our efforts in getting our customers to adopt our preferred electronic payments system (EPS). Increased EPS adoption will have a significant impact on our bottom line. Given a list of firms who are currently (or potentially in the future) financing their large equipment purchases with us (the Fortune 100 company), how can we predict the likelihood of a firm to adopt EPS, and how can we target EPS promotions to only those firms that were more likely to adopt EPS for their payments?

The senior managers at this company (the vast majority of its customer interactions being big ticket items) knew the close link between the adoption of EPS by their customers and the reduction in their account receivables period,<sup>1</sup> called colloquially within the firm as “days to dollar.” While the managers were charged with improving their cash conversion cycle, they had little success in the past in trying to convert their customers to using the EPS. They also did not have extra discretionary marketing spending they could use to “carpet-bomb” all the customers with the benefits of the EPS or hire consultants to acquire qualitative data on customers likelihood of adoption and their perceptions and beliefs about the technology. Thus they were very keen to use the archival data they already had to develop a strategy that helped them identify which specific nonadopting customers to go after. The information available to the Fortune 100 company included firm characteristics (such as firm size, industry), geographic characteristics (such as region), as well as some transaction-level characteristics (such as credit risk of a firm, financing options and payment amount of a transaction). This research describes the theoretical and practical lessons learned from the development of an actionable segmentation scheme and a direct segment-specific customer attraction strategy based on the revealed EPS adoption patterns recorded in the archival data.

We propose and test the performance of a finite mixture model-based prediction approach (Gupta and Chintagunta 1994) to address the above-mentioned problem. We believe that the proposed methodology has broad applicability in IS research, including, but not limited to, areas such as determining heterogonous segments of bidding behavior in online auctions, in designing personalized online recommendation and collaborative filtering systems, and in fraud detection and prevention. The common theme in our current study and these areas is the need to explicitly segment membership and to predict the future behavior or events on the basis of some observable information. We posit that the value of identifying segments and developing segment-specific predictive modeling has been largely underappreciated in the IS area. Explanatory studies, which test hypotheses specifying how and why certain empirical phenomena occur, dominate mainstream empirical IS research even though the actual goal is predictive in nature for some (Shmueli and Koppius 2007).

The explanatory models in the IS literature offer excellent and solid insights in terms of identifying factors and describing the cause-effect relationships among the factors. However, they generally focus on explaining past behavior (without explicit reference to the future behavior) and assume homogeneity of decision choices in the sample. In addition, the implications from many explanatory models are often difficult to execute because they require information that is costly to obtain beyond the sample space. Recall, that the Fortune 100 company we were working with, while familiar with the technology acceptance model (TAM) model, thought it impractical to execute such a model in an inter-organizational ((business-to-business) B2B) setting. It did not want to invest in consultants to run surveys of technology adoption, user beliefs, perceived benefits, organizational readiness, etc. on its customers. For reasons such as these, IS researchers (for example, Shmueli and Koppius 2007) in the recent years have called for recognition of predictive data analytic modeling strategies.

Identifying segments in a population and determining their sensitivities to various variables have been one of the most important concepts in the marketing literature because of the associated profit implications (Claycamp and Massy 1968). Various models (see DeSarbo et al. 2008 for a brief review) have been put forth to uncover the underlying segments in a given market. Among them, latent class (finite mixture) models (see, for example, Gupta and Chintagunta 1994, Hagenaars and McCutcheon 2001, Kamakura and Russell 1989, Lazarsfeld and Henry 1968, Wedel and DeSarbo 1993, Wedel and Kamakura 2000) for market segmentation have been widely applied and their performances have also been documented in the marketing literature. The rationale underlying these models is as follows (see Hagenaars and McCutcheon 2001 and Wedel and Kamakura 2000 for more details): There are a fixed and finite number of homogeneous segments in a market. Subjects belong to each of these segments with some probabilities, which are assumed a priori to be invariant across subjects. Conditional upon membership in a segment, the probability of a subject’s choice decision is given by a choice model, such as a logit model. The intercepts of the choice model as well as sensitivities to explanatory variables are allowed to vary across segments. By maximizing the unconditional likelihood of the entire sample, estimates of the membership and the associated coefficients for variables can be obtained simultaneously. Each subject can then be assigned to a segment through the updated posterior probability.

For a customer segmentation scheme to be useful, it needs to be actionable so that managers can use it for the purpose of targeting and positioning (Kotler and Keller 2006). Therefore it is necessary to characterize segments using data that are readily available and observable (Fader and Hardie 1996, Dayton and Macready 1988, Gupta and Chintagunta 1994, Kamakura and Russell 1989). The purpose of this research is twofold. First, we present a finite mixture logit model that simultaneously classifies firms into homogeneous segments based on firm-specific characteristics and estimates the model’s coefficients, thus relating predictor variables to decision choices for each respective segment. Second, we apply the proposed model to predict the adoption of EPS in a B2B context, and offer an alternative lens to the traditional explanatory modeling for a practical and actionable segmentation strategy.

We follow the method agnostic tradition in predictive modeling and data mining (Shmueli et al. 2006). This principle encourages researchers to try a variety of predictive models and judge them based on their predictive performance on a holdout sample. Thus we develop our proposed finite mixture model and compare it with traditional approaches, including a standard logit classification model, a complementary log-log model, a two-stage sequential model, and a hierarchical logit model. Reassuringly, as a baseline case, we find that these models have similar explanatory power and qualitative directional influences of predictor variables. However, when we randomly partition our data into training and multiple validation data sets, and test the ability of various models developed from the training data to predict (known) outcomes on the validation data sets, we show that our proposed finite mixture model has approximately 17% higher prediction accuracy than the standard approaches.

Our contribution is to showcase a methodology for IS research settings where the situation demands actionable and segment-specific predictive capabilities. We find that there exist three distinct segments of firms with significant variations in EPS adoption rates across segments and that firm size, region, industry, and credit risk were all determinants of segment membership. In addition, the decision choices of EPS adoption across the three segments were also found to differ significantly in their sensitivity to payment amount and financing options. The work also contributes to the empirical technology adoption literature by providing a predictive perspective, in what has been predominantly an explanatory view of the problem.

The rest of this paper is organized as follows. Section 2 formulates our finite mixture logit model. Section 3 discusses the background of EPSs and related technology adoption literature. We also report on our data as well as data preprocessing in §3. Section 4 describes the benchmark research methodologies and presents the results of our analysis. Section 5 offers our concluding remarks and discusses practical and theoretical implications of this research.

## 2. The Finite Mixture Logit Model

We use subscript i to represent a list of firms $( i =$ $1 , 2 , \ldots , N )$ . Each firm i has j $( j = 1 , 2 , \ldots , T _ { i } )$ accounts with the Fortune 100 company. Let $y _ { i j }$ denote the payment option of firm i on account j. If firm i makes the payment for account $j$ via an EPS, then $y _ { i j } = 1 ;$ ; otherwise $y _ { i j } = 0 .$ . We assume that there exist S segments in the market under consideration $( s = 1 , 2 , \ldots , S )$ . Each firm i belongs to one and only segment $s ,$ which is not known in advance. Firms within the same segment are assumed to be homogeneous with respect to their sensitivities to marketing variables, but those across segments can differ.

Let $\mathbf { X } _ { i j } = ( 1 , X _ { i j } ^ { ( 1 ) } , \ldots , X _ { i j } ^ { ( k ) } )$ denote a row vector of k predictor variables that could help explain EPS adoption. Since $y _ { i j }$ is binary, then conditional upon firm i belonging to segment s, the probability that firm i makes payment for account j via EPS can be represented using a logit regression model follows:

$$
P (y _ {i j} = 1 \mid s) = \frac {\exp (\pmb {\beta} _ {s} \pmb {X} _ {i j} ^ {\prime})}{1 + \exp (\pmb {\beta} _ {s} \pmb {X} _ {i j} ^ {\prime})},\tag{1}
$$

where $\boldsymbol { \beta _ { s } } = ( \beta _ { s } ^ { ( 0 ) } , \beta _ { s } ^ { ( 1 ) } , \dots , \beta _ { s } ^ { ( k ) } )$ is the coefficient vector associated with the vector of the predictor variables $\mathbf { \boldsymbol { x } } _ { i j } .$

Following Gupta and Chintagunta (1994) that classify subjects into segments using demographic variables, we model the probability that firm i belongs to segment $s , \ P _ { i s } ,$ depends on a vector of firm-specific variables $Z _ { i } = ( 1 , \dot { Z } _ { i } ^ { ( 1 ) } , \dots , Z _ { i } ^ { ( m ) } )$ . Assuming the values of segment membership follow a multinomial distribution (Gupta and Chintagunta 1994, Vermunt and Magidson 2005, Wedel and DeSarbo 1993), the probability $P _ { i s }$ can be written as

$$
P _ {i s} = \frac {\exp (\boldsymbol {\eta} _ {s} \mathbf {Z} _ {i} ^ {\prime})}{\sum_ {s = 1} ^ {S} \exp (\boldsymbol {\eta} _ {s} \mathbf {Z} _ {i} ^ {\prime})},\tag{2}
$$

where ${ \mathfrak { N } } _ { s } = ( \eta _ { s } ^ { ( 0 ) } , \eta _ { s } ^ { ( 1 ) } , \dots , \eta _ { s } ^ { ( m ) } )$ is the vector of segment-specific parameters to be estimated, representing the effects of firm-specific variables on the probability of segment membership.

Given Equations (1) and (2), the unconditional probability that a randomly selected firm i pays account j via EPS is given by

$$
P (y _ {i j} = 1) = \sum_ {s = 1} ^ {S} P _ {i s} \cdot P (y _ {i j} = 1 \mid s).\tag{3}
$$

For each firm i having T accounts with the company of interest, the likelihood function conditional on firm $i \prime \mathrm { s }$ membership can be formulated as

$$
L _ {i \mid s} = \prod_ {j = 1} ^ {T _ {i}} P (y _ {i j} = 1 \mid s) ^ {y _ {i j}} (1 - P (y _ {i j} = 1 \mid s)) ^ {1 - y _ {i j}}.\tag{4}
$$

Hence the unconditional likelihood for any firm i is $\begin{array} { r } { L _ { i } = \sum _ { s = 1 } ^ { S } P _ { i s } \cdot L _ { i | s } , } \end{array}$ and the complete likelihood over the entire sample of firms can then be written as

$$
L = \prod_ {i = 1} ^ {N} \sum_ {s = 1} ^ {S} P _ {i s} \prod_ {j = 1} ^ {T _ {i}} P (y _ {i j} = 1 | s) ^ {y _ {i j}} (1 - P (y _ {i j} = 1 | s)) ^ {1 - y _ {i j}}.\tag{5}
$$

By maximizing the log-likelihood (LL) function (5), the unknown parameters of the problem ${ \mathfrak { n } } _ { s } =$ $( \eta _ { s } ^ { ( 0 ) } , \eta _ { s } ^ { ( 1 ) } , \dots , \eta _ { s } ^ { ( \frac { \bf { \sigma } } { \cal { m } } ) } )$ and $\pmb { \beta } _ { s } = ( \beta _ { s } ^ { ( 0 ) } , \beta _ { s } ^ { ( 1 ) } , \frac { \mathbf { \lambda } ^ { \ast } } { \hbar \mathbf { \mu } _ { s } } , \beta _ { s } ^ { ( k ) } )$ can be estimated simultaneously (see Kamakura and Russell 1989, Vermunt and Magidson 2005, and Wedel and DeSarbo 1993 for details). Once these estimates are obtained, each firm can be assigned to each class through the estimated posterior probability and picking the class for which the firm has the highest posterior probability.

The number of actual segments S is determined by carrying out estimations for various values of S and examining the relative fit of alternative model specifications using an appropriate information criterion, $\mathbf { e . g . }$ Akaike’s information criterion (AIC), Bayesian information criterion (BIC), and consistent Akaike’s information criterion (CAIC) (Wedel and DeSarbo 1993, Gupta and Chintagunta 1994, Wedel and Kamakura 2000). To ensure that the centroids of the segments are adequately separated from one another, an entropy-based measure can also be used to examine the degree of certainty in classification into segments (Wedel and Kamakura 2000, Wedel and DeSarbo 1993).

$$
E _ {s} = 1 + \frac {\sum_ {i = 1} ^ {N} \sum_ {s = 1} ^ {S} P _ {i s} \cdot \ln (P _ {i s})}{N \ln (S)}\tag{6}
$$

The value of $E _ { s }$ is bounded between 0 and 1 with a value close to 1, indicating the segments are well separated.

## 3. Application: Prediction of EPS Adoption

## 3.1. Background

Technological advances and the widespread use of the Internet are allowing businesses to automate a broad range of their business processes, including procurement, supply chain, sales and customer care, payments, etc. Electronic payments refer to any payment that is completed using some form of electronic communication technologies. Several options for electronic payments are in place. Most of them fall under the category of electronic funds transfer (EFT). The various forms of EFT include automated clearing house (ACH), society for worldwide interbank financial telecommunications, wire, and federal electronic data interchange.

EPS uses an integrated process in which payment data are sent and received electronically from accounts payable to accounts receivable without human intervention, and is a critical component of the information economy. Despite the tremendous benefits (such as accuracy, efficiency, reduced transaction, and lower collection costs) that EPS can offer, its adoption in B2B transactions remains a challenge. A recent survey by Association for Financial Professionals (AFP) (2004) finds that, even though the volume of electronic payments by consumers has grown rapidly, more than 80% of payments between businesses are still made with paper checks. A number of barriers have also been identified that appear to obstruct the wider adoption of electronic payments (Stavins 2003, Chakravorti and Davis 2004, Cotteleer et al. 2007).

There are several streams of research that are related. One of them is the study of adoption of electronic payments at both the individual user and the firm level. For example, Hayashi and Klee (2003) tested the hypotheses that consumer payment choices depend on their propensity to adopt new technologies and the nature of the transaction. Oh et al. (2006) argued, through several case studies, two necessary conditions for successful EPS adoption from a stakeholder’s perspective. Another related stream of research is the study of the adoption of electronic data interchange (EDI) systems in organizations (e.g., Chwelos et al. 2001; Hart and Saunders 1997, 1998; Iacovou et al. 1995; Reich and Benbasat 1990; Pfeiffer 1992; Premkumar et al. 1997; Saunders and Clark 1992; Teo et al. 2003). EPS systems share some common features with EDIs. For example, they are both cooperative interorganizational systems that allow trading partners to exchange business information electronically. There must have at least two organizations in a business relationship, and the integrity of the data exchange between trading partners must be guaranteed (Pfeiffer 1992). However, these studies are mainly explanatory and usually examine the effects of various (belief) factors (such as perceived benefits, organizational readiness, etc.) on EDI adoption.

The paper by Gowrisankaran and Stavins (2004) investigates EPS adoption from a different yet interesting angle. The authors analyze the extent of network externalities on bank adoption and use of ACH systems based on bank-specific observable variables. Three novel models were developed that all revealed significant evidence of network externalities in the adoption of ACH systems among banks. Our work complements the existing literature by developing a predictive model of EPS adoption.

## 3.2. Data

Our primary data set is the billing data from one of the top Fortune 100 companies (hereafter called the “vendor”) that provides information on individual firms that have financed purchases of large commercial equipments with the vendor before 2005. Because the commercial equipments are expensive, firms usually finance the purchase of these equipments with the vendor, and subsequently make recurring payments every month. The finance options take one of two forms: lease or loan ranging from a few months to more than 20 years. The vendor provides all firms a voluntary-free service of ACH debits. Firms have the option to make their payments using ACH or using conventional payment methods (such as check). We observe payment choices of the firms in the first quarter of 2005.

The data set contains two levels of information. The firm-level information includes observable firm characteristics such as address, region, standard industry code, etc. Region is a geographic variable while industry is a measure of firm demographics. Because these variables are easy to observe and are often associated with use behavior, they have been constantly used for segmenting markets (Kotler and Keller 2006). In addition to region and industry, we also link our data set to the Dun & Bradstreet (D&B) database, which provides information on firm’s name, assets, sales, net worth, total number of employees, the credibility of a firm’s payment history, etc. for all firms that are registered in D&B. A firm’s sales (assets, net worth) and total number of employees are proxies that measure the size of the firm. The credibility of payment history is a measurement of firm-level payment risk. In the D&B database, it is denoted by a PAYDEX<sup>®</sup> score, which is a unique, dollar weighted indicator of a business’ payment performance based on the total number of payment experiences over the past year. The PAYDEX scores range from 0 to 100, with higher scores indicating better payment performance. Generally, a firm with a PAYDEX score above 80 means that it pays its bills on time or sooner (i.e., low risk of late payment) while that below 80 is delinquent (i.e., high risk of late payment).

Each firm can have multiple accounts with the vendor. The account-level information includes account number, payment options (either ACH debit or non-ACH), financing option of the account (lease or loan), purchase date, original terms (in terms of months), payment amount, etc. Lease is a type of financing in that the vendor still owns the equipment, while loan usually implies that the firm buys the equipment from the vendor. We observe within-firm heterogeneity with respect to payment options. In other words, a firm with multiple accounts can use ACH for some of the accounts, while at the same time pay other accounts using conventional methods. In this paper, we chose six independent variables (four firm-level variables: firm size, region, industry, and credit risk, and two account-level variables: payment amount and financing option) for our subsequent analysis. The choice of these variables is primarily guided by two principles. First, the variables need to have a theoretic basis in predicting EPS adoption. Second, the segmentation scheme based on these variables needs to be easily actionable and replicable.

Table 1 Descriptive Statistics of Numerical Variables

<table><tr><td>Variables</td><td>Min.</td><td>Max.</td><td>Mean</td><td>Median</td><td>Std. dev.</td></tr><tr><td colspan="6">Account-level data</td></tr><tr><td>Payment amount ($)</td><td>11.42</td><td>9,520,298.43</td><td>17,349.97</td><td>4,836.77</td><td>102,378.62</td></tr><tr><td>EPS</td><td>0</td><td>1</td><td>0.29</td><td>0</td><td>0.45</td></tr><tr><td colspan="6">Firm-level data</td></tr><tr><td>PAYDEX</td><td>5</td><td>89</td><td>71</td><td>73</td><td>8.98</td></tr><tr><td>Firm size</td><td>1</td><td>355,000</td><td>2,132</td><td>150</td><td>14,240</td></tr><tr><td>Number of accounts per firm</td><td>1</td><td>271</td><td>3.08</td><td>1</td><td>7.80</td></tr></table>

An important step in the data modeling process is data preprocessing. We performed several tasks in this stage. First, we converted the four-digit industry codes into the broad 10 industry categories as defined by the U.S. Department of Labor.<sup>2</sup> Second, when we linked our data set to the D&B database, we observed missing values for firm sales and net worth. Because the total number of employees has been widely used as a proxy for measuring the size of a firm, we run the Pearson’s correlation analysis on the number of employees, sales, and net worth. The correlation coefficients are positive and large (above 0.8), indicating these variables are highly correlated. Hence, in our later data analysis, we choose the total number of employees as an approximation for firm size. Finally, firm size, PAYDEX, and payment amount are continuous variables, of which firm size and payment amount have a wide range of values. We standardized these variables to make them comparable.

Our final data set contains a total of 4,922 firms with 15,176 accounts. Of the 15,176 accounts, less than 29% are paid by ACH debit; the rest are paid through conventional paper checks. Table 1 describes the summary statistics for the entire data set. In Table 1, we provide the minimum, maximum, average, median, and standard deviations for the numerical variables (PAYDEX, firm size, payment amount, EPS). The frequency count for the account-level variable financing option is 10,300 (67.9%) for lease and 4,876 (32.1%) for loan. Besides these, another account-level variable, financing terms, was tried but dropped from the final model because it did not result in a significant improvement in model fit and prediction.

Table 2 Summary Statistics for Firm-Level Data by Industry

<table><tr><td>Industry</td><td>Avg. no. of employees</td><td>Credit risk</td><td>Mid-west</td><td>North-east</td><td>South</td><td>West</td></tr><tr><td>Agriculture, forestry, and fishing</td><td>434</td><td>74</td><td>8</td><td>10</td><td>13</td><td>33</td></tr><tr><td>Construction</td><td>358</td><td>67</td><td>97</td><td>116</td><td>179</td><td>147</td></tr><tr><td>Finance, insurance, and real estate</td><td>2,552</td><td>73</td><td>14</td><td>29</td><td>49</td><td>46</td></tr><tr><td>Manufacturing</td><td>2,343</td><td>70</td><td>546</td><td>332</td><td>443</td><td>318</td></tr><tr><td>Mining</td><td>2,239</td><td>71</td><td>13</td><td>11</td><td>39</td><td>9</td></tr><tr><td>Public administration</td><td>6,895</td><td>69</td><td>9</td><td>19</td><td>32</td><td>27</td></tr><tr><td>Retail</td><td>10,263</td><td>73</td><td>25</td><td>24</td><td>54</td><td>26</td></tr><tr><td>Services</td><td>2,475</td><td>70</td><td>151</td><td>175</td><td>175</td><td>153</td></tr><tr><td>Transportation, communications</td><td>1,168</td><td>73</td><td>396</td><td>188</td><td>371</td><td>258</td></tr><tr><td>Wholesale</td><td>2,486</td><td>73</td><td>105</td><td>65</td><td>118</td><td>99</td></tr><tr><td>Total</td><td>2,132</td><td>71</td><td>1,364</td><td>969</td><td>1,473</td><td>1,116</td></tr></table>

In predictive modeling, data partitioning is especially important for model assessment. Hence we randomly split our data into two data sets (in §4.4, we replicate the random partitioning 10 times with different seeds to further stress test the proposed models) for later analysis: 9,078 accounts (about 60%) were used for the purpose of model estimation, and the remaining $6 , 0 9 \dot { 8 }$ accounts constituted the validation (holdout) sample. In addition, firm-level variables (region, PAYDEX, firm size, industry) were used in the finite mixture model to determine segments. These variables need to be independent. In Table 2, we provide descriptive statistics for these variables broken down by industry. We also performed Pearson correlation analysis among these variables using recoded region and industry. The correlation coefficients are all small, indicating no or very weak correlations.

## 4. Results and Discussions

Following the data mining tradition (Shmueli et al. 2006), we compare the proposed finite mixture model with several benchmark models, including a standard logit model, a complementary log-log model, a twostage sequential model employing segmentation followed by a classification approach, and a hierarchical logit model. We find that the finite mixture model outperforms these benchmarks in the predictive accuracy as well as the explanatory abilities.

## 4.1. Standard Logit Model

Because our dependent variable is binary, as a first step, we performed a standard logit regression analysis. The standard logit approach models the probability that $y _ { i j } = 1$ , denoted $\overset { \_ } { \pi } _ { i j } = \operatorname* { P r } [ y _ { i j } = 1 ]$ . The standard logit model<sup>3</sup> can be written as

Table 3 Binary Logit Model Results

<table><tr><td>Variables</td><td>Level</td><td>Estimate</td><td>p-value</td></tr><tr><td>Intercept</td><td></td><td>-1.36</td><td>&lt;0.0001</td></tr><tr><td>Firm size</td><td></td><td>-2.35</td><td>&lt;0.0001</td></tr><tr><td>Payment amount</td><td></td><td>-0.19</td><td>0.0065</td></tr><tr><td>Credit risk</td><td></td><td>-0.12</td><td>&lt;0.0001</td></tr><tr><td>Financing option</td><td>Lease</td><td>-0.27</td><td>&lt;0.0001</td></tr><tr><td>Region</td><td></td><td></td><td></td></tr><tr><td></td><td>Midwest</td><td>0.27</td><td>&lt;0.0001</td></tr><tr><td></td><td>Northeast</td><td>0.53</td><td>&lt;0.0001</td></tr><tr><td></td><td>South</td><td>-0.48</td><td>&lt;0.0001</td></tr><tr><td>Industry type</td><td></td><td></td><td></td></tr><tr><td></td><td>Agriculture, foresting, fishing</td><td>1.37</td><td>&lt;0.0001</td></tr><tr><td></td><td>Construction</td><td>0.32</td><td>0.0005</td></tr><tr><td></td><td>Finance, insurance, real estate</td><td>0.17</td><td>0.2897</td></tr><tr><td></td><td>Manufacturing</td><td>0.54</td><td>&lt;0.0001</td></tr><tr><td></td><td>Mining</td><td>-0.01</td><td>0.9454</td></tr><tr><td></td><td>Public administration</td><td>-2.63</td><td>&lt;0.0001</td></tr><tr><td></td><td>Retail trade</td><td>0.04</td><td>0.8000</td></tr><tr><td></td><td>Services</td><td>-0.02</td><td>0.7913</td></tr><tr><td></td><td>Transportation, electric, gas</td><td>0.08</td><td>0.3239</td></tr><tr><td colspan="4"> $R^{2} = 0.1175$ </td></tr></table>

$$
\mathbf {l o g i t} (\pi_ {i j}) = \mathbf {l o g} \bigg (\frac {\pi_ {i j}}{1 - \pi_ {i j}} \bigg) = \boldsymbol {\beta} X _ {i j} ^ {\prime} + \boldsymbol {\eta} Z _ {i} ^ {\prime},\tag{7}
$$

where, as defined before, $\mathbf { \boldsymbol { x } } _ { i j }$ is a vector of accountlevel variables and $\mathbf { Z } _ { i }$ is a vector of firm-level variables,  and - are vectors of coefficients.

Table 3 presents the parameter estimates of the standard logit model fitted across all accounts in the training data set. The overall model is significant (likelihood ratio $\chi ^ { 2 } = 1 , 1 3 5 . 0 3 )$ . The explanatory power of the logit model, as measured by the generalized $R ^ { 2 } ,$ , is around 0.12. In the logit model analysis, effects (deviation) coding method was chosen for the categorical input variables, meaning that the coefficient estimates will sum to zero over the categories of the nominal variable concerned.

It can be seen from Table 3 that firm size and payment amount have significant negative effects on EPS adoption. In other words, large firms and/or firms with large recurring payments are less likely to adopt EPS. Interestingly, firms with good credit history (PAYDEX has a negative coefficient) are less likely to adopt EPS. Financing option, region, and industry are also significant. Firms are more likely to make payments electronically when they finance their purchases using loan. Firms from the Northeast have the highest tendency to adopt EPS. Agriculture, construction, manufacturing, and public administration are industries that display significant effects. However, public administration has the largest (in absolute value) coefficient, indicating strong negative tendency to use EPS for firms in this sector. These findings are in line with previous explanatory empirical studies regarding the directional impact between independent variables and adoption decisions (see, for example, Burke 2005, Chweloes et al. 2001, Forman 2005, Hart and Saunders 1997, Yap et al. 1992).

One concern in the logit analysis is the possible endogeneity between EPS adoption and payment amount. In our setting, the payment amount is solely determined by the lease/loan amount, the interest rate, and financing terms when a firm signed the contract with the vendor. After the contract details were finalized, the firm was presented the option to make subsequent monthly payments to the vendor using either EPS or paper checks. While we cannot formally check for this, we do believe, given the order of decision making, a firm’s EPS decision choice should not influence the payment amount.

As discussed earlier, a holdout (test) sample consisting of 2,890 firms with 6,098 accounts was created for the purpose of model validation. One of the commonly used performance measures in predictive modeling is the prediction accuracy in the holdout sample. We calculated predicted values of the dependent variable (EPS adoption) for the test data set based on the fitted regression model (Table 3). The predictions, using a cut value of 0.5 (Greene 2000), were compared with the actual choices. This resulted in a prediction accuracy of 71.5% (i.e., misclassification rate of 28.5%) for the standard logit model.

The logit model in (7) does not account for the possible firm-level (group-level) effects even though the data has two levels. A traditional approach to address this issue would be adding dummy variables for firms and/or interaction terms between the predictors and the dummy variables to the model. This essentially produces a model in which the regression for each group contains (potentially) different intercepts and/or slopes. In the following subsections, we present a variety of approaches that consider firmlevel effects.

## 4.2. Two-Stage Model

The two-stage model accounts for the firm heterogeneity by first clustering cases into segments on the basis of the independent variables. Subsequently, a logit model was estimated within each of the segments. We conducted the clustering analysis using the TwoStep approach in SPSS v13. The TwoStep clustering approach is a scalable algorithm that is capable of handling both continuous as well as categorical variables. The LL distance measure, which is a probability-based distance, was chosen to determine the similarity between clusters. The TwoStep clustering analysis also automatically determines the optimal number of clusters by comparing the values of a model choice criterion (such as BIC or AIC) across different clustering solutions.

Table 4 Results of Logit Regression in the Two-Stage Analysis

<table><tr><td rowspan="2">Variables</td><td rowspan="2">Level</td><td colspan="3">Segments</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>Intercept</td><td></td><td>-1.5709**</td><td>-18.6400</td><td>-1.6340**</td></tr><tr><td>Firm size</td><td></td><td>-2.8475**</td><td>-0.2880</td><td>-2.5360**</td></tr><tr><td>Payment amount</td><td></td><td>-0.4055**</td><td>-0.0003</td><td>0.0950</td></tr><tr><td>PAYDEX</td><td></td><td>0.0178</td><td>0.0300</td><td>-0.3040**</td></tr><tr><td>Financing option</td><td>Lease</td><td>-0.4088*</td><td>-0.46100**</td><td>—</td></tr><tr><td>Region</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Midwest</td><td>0.4849**</td><td>4.5430</td><td>0.1470**</td></tr><tr><td></td><td>Northeast</td><td>0.2398**</td><td>-13.9740</td><td>0.7290**</td></tr><tr><td></td><td>South</td><td>-0.4595**</td><td>4.4300</td><td>-0.3730**</td></tr><tr><td>Industry type</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Agriculture, foresting, fishing</td><td>0.5863</td><td>—</td><td>1.7690**</td></tr><tr><td></td><td>Construction</td><td>0.3777*</td><td>-7.3920</td><td>0.4560**</td></tr><tr><td></td><td>Finance, insurance, real estate</td><td>0.7872*</td><td>-8.0800</td><td>-0.2920</td></tr><tr><td></td><td>Manufacturing</td><td>0.4415**</td><td>12.1660</td><td>0.5710**</td></tr><tr><td></td><td>Mining</td><td>-0.5008</td><td>-5.0330</td><td>0.2390</td></tr><tr><td></td><td>Public administration</td><td>-2.4569**</td><td>10.9750</td><td>-3.00800**</td></tr><tr><td></td><td>Retail trade</td><td>0.3793</td><td>-6.2690</td><td>0.0260</td></tr><tr><td></td><td>Services</td><td>-0.1897</td><td>-6.4380</td><td>-0.0190</td></tr><tr><td></td><td>Transportation, electric, gas</td><td>-0.0003</td><td>12.5830</td><td>0.2130</td></tr><tr><td> $R^2$ </td><td></td><td>0.0650</td><td>0.0820</td><td>0.1320</td></tr></table>

∗5% significant; ∗∗1% significant.

A three-segment solution was obtained for the training sample. In the appendix (Table A.1), we provided the descriptive statistics for the three segments. The first segment, with a class size of 0.277, is characterized by small firms with low PAYDEX scores. The majority of the accounts in this segment are financed using loans. In contrast, relative to Segments 1 and 3, Segment 2 (class size 0.136) is characterized by the largest values of firm size and payment amount. Segment 3, with a class size of 0.587, contains mainly lease accounts with the smallest payment amount. Table 4 describes the results of the logit model estimated within each of the three classes. The R<sup>2</sup> ranges from about 6% to 13% for the three segments. We note that only financing option has a significant negative effect for Segment 2, indicating that large firms that finance accounts using a lease are less likely to adopt EPS. Qualitative findings for Segments 1 and 3 are pretty consistent with those from Table 3.

We again analyzed the prediction accuracy of the two-stage model on the holdout sample. Cases in the holdout sample were first classified into three segments with the established cluster model. Depending on what segment a case belongs to, we calculated predicted values of EPS based on the corresponding regression model obtained in Table 4. The prediction accuracy (again using a cut value of 0.5) was 62.2%, 81.0%, and 75% for each segment, respectively. The overall prediction accuracy was 72.2%. In other words, unsupervised clustering technique does not seem to capture much of the variations in EPS adoption. The prediction accuracy in the two-stage procedure is slightly better than the standard logit model, but at the cost of a much larger number of parameters estimated. The slightly higher predictive power of the two-stage procedure, in our view, does not offset the modeling and interpretation complexity compared to the logit model.

Table 5 Model Fit for Alternative Numbers of Segments

<table><tr><td>Number of consumer segments</td><td>LL</td><td>Entropy of BIC(LL)</td><td>Separation</td><td>AIC(LL)</td><td>AIC3(LL)</td><td>CAIC(LL)</td><td> $R^2$ </td></tr><tr><td>1</td><td>-5,326.18</td><td>10,677.85</td><td>—</td><td>10,658.35</td><td>10,661.35</td><td>10,680.85</td><td>0.03</td></tr><tr><td>2</td><td>-2,773.49</td><td>5,725.52</td><td>0.95</td><td>5,588.99</td><td>5,609.99</td><td>5,746.52</td><td>0.93</td></tr><tr><td>3</td><td>-2,687.04</td><td>5,705.65*</td><td>0.86</td><td>5,452.09</td><td>5,491.09</td><td>5,744.64*</td><td>0.94</td></tr><tr><td>4</td><td>-2,644.80</td><td>5,774.17</td><td>0.75</td><td>5,403.59</td><td>5,460.59*</td><td>5,831.17</td><td>0.95</td></tr><tr><td>5</td><td>-2,623.16</td><td>5,883.92</td><td>0.66</td><td>5,396.31*</td><td>5,471.31</td><td>5,958.92</td><td>0.95</td></tr><tr><td>6</td><td>-2,610.34</td><td>6,011.31</td><td>0.80</td><td>5,406.68</td><td>5,499.68</td><td>6,104.31</td><td>0.95</td></tr></table>

∗Lowest information criterion.

## 4.3. Finite Mixture Model

We used Latent GOLD<sup>®</sup> 4.0<sup>4</sup> for our maximum likelihood estimation. Specifically, a latent class regression module (with EPS as the dependent variable) was used to identify segments for which regression coefficients could differ. Model estimates are obtained for alternative values of the number of consumer segments $( S = 1 , 2 , \ldots , 6 )$ . To account for suboptimal solutions, we estimated the model multiple times for each value of S with different starting values, and retained the best solution for each model. Table 5 reports model fit (the LL values, the various information criterion values, the entropy of separation, and the pseudo-R<sup>2</sup> that is based on the reduction of mean squared errors) for each value of S.

Deciding on how many segments to retain in finite mixture models is an important and critical issue because specifying too few ignores class differences, while specifying too many could cause the model to be unstable. Researchers frequently use criteria such as AIC, BIC, CAIC, and information complexity to determine the optimal number of segments to retain (Wedel and Kamakura 2000). Yet so far, there has been no consensus on the best solution. Kamakura and Russell (1989) used AIC as a guidance to choose the number of segments. Wedel and DeSarbo (1993) used CAIC as well as an entropy-based measure to determine the appropriate number of segments. Bucklin and Gupta (1992), Gupta and Chintagunta (1994), Kamakura et al. (1996), Magidson and Vermunt (2002), among many others, used BIC to determine the number of segments. Andrews and Currim (2003) showed through simulation that an AIC with a penalty factor of three (AIC3) has the highest segment retention success rate. Bozdogan and Ramirez (1988) proposed to use CAIC to determine the lower bound and use AIC to determine the upper bound of the number of segments to retain.

In this paper, we determine the number of segments on the basis of multiple criteria, and choose S <sub>=</sub> 3 as the solution that most parsimoniously represents the structure in the data. In Table 5, we find that two measures, BIC and CAIC suggest a threesegment mixture as the best model. The AIC measure suggests a five-segment solution, while the AIC(3) measure suggests a four-segment solution. However, notice that the AIC and AIC(3) measures do not change noticeably after three segments are extracted. We also applied the entropy-based measure to investigate the degree of certainty in the classification of firms into segments. The entropy measure computed for the three-segment solution was 0.86, indicating a reasonably clear separation of the three segments. The pseudo-R<sup>2</sup> increases from 0.03 for the one-class regression to 0.94 for the three-class regression. Finally, the predictive validity tests (to be discussed later) also suggest our choice of three-segment solution as the best model.

The detailed summary statistics for the three-class mixture solution were presented in the appendix (Table A.2). The relative size for each segment is large, suggesting that the segmentation is sustainable (Wedel and Kamakura 2000). Segment 1 is characterized by the largest firm size and payment amount. The majority of the accounts in Segment 1 are financed through lease. In contrast, Segment 2 is characterized by much smaller firm size and the smallest payment amount. Segment 3 contains mostly small firms yet with relatively higher PAYDEX score.

When evaluating the EPS adoption rate, we found that, remarkably, the finite mixture three-segment solution is able to partition the multidimensional data in terms of the dependent variable (which is not used in the clustering) in a significant way. Note that there is a huge difference between Segment 1, which has the lowest EPS adoption rate (less than 1%), and Segment 2 the highest EPS adoption rate (above 96%). Segment 3, a relatively smaller segment in terms of size, is also separated from Segments 1 and 2, sitting in the middle vis-à-vis EPS adoption rates (about 45%). Based on the descriptive statistics, we can label Segment 1 as the large laggards segment, Segment 2 as the nimble adopters, and Segment 3 as the medium indifferent firm segments. It is well known in the innovation diffusion literature that the adoption of a new technology depends on the demographic and psychological characteristics of defined adopter groups (such as early adopters, late adopters). Given the heterogeneities in user profiles, the proposed mixture model is able to classify firms into distinctive segments with drastically different EPS adoption behavior. Clearly, such a distinct and statistically significant partitioning is not possible based on the ad hoc clustering schemes (see the previous section) and represents an interesting contribution to this study.

Table 6 presents the parameter estimates $( \pmb { \beta } _ { s } \pmb { \eta } _ { s } )$ of the three-class logit mixture regressions. The $p \mathrm { - }$ values for the Wald statistics for payment amount and financing option are less than 0.001, indicating that the effect of these variables on the EPS decision is highly significant. A separate Wald 	<sub>=</sub> statistic testing the between-segment differences for $\mathbf { \beta } _ { s }$ was also performed. Results show that the  effects across segments are significant (Wald $\mathrm { ( = ) } = 3 1 . 6 7 \ : \ : ( p < 0 . 0 0 \bar { 1 } )$ for payment amount, Wald $\left( = \right) = 2 5 . 1 7 \ ( p < 0 . 0 0 1 )$ for financing option). The - parameters of the model for the latent class distribution appear in Table 6 under the heading “model for classes.” The p-values associated with the Wald statistics show that overall firm size, PAYDEX, region, and industry effects are all significant in segmenting firms.

Table 6 Parameter Estimates of the Three-Segment Solution of the Finite Mixture Logit Model for EPS Adoption

<table><tr><td rowspan="2">Variables</td><td rowspan="2">Level</td><td colspan="3">Segments</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>Intercept</td><td></td><td>-2.8218</td><td>1.7281</td><td>0.3225</td></tr><tr><td>Payment amount</td><td></td><td>0.0518</td><td>-1.9706**</td><td>4.6981*</td></tr><tr><td>Financing option</td><td>Lease</td><td>-1.7693*</td><td>0.1214</td><td>-1.6835**</td></tr><tr><td>Model for classes</td><td></td><td></td><td></td><td></td></tr><tr><td>Intercept</td><td></td><td>1.5519</td><td>0.0471</td><td>-1.5990</td></tr><tr><td>Firm size</td><td></td><td>1.7011**</td><td>-0.3018</td><td>-1.3993</td></tr><tr><td>PAYDEX</td><td></td><td>-0.2008*</td><td>-0.2719*</td><td>0.4727*</td></tr><tr><td rowspan="3">Region</td><td>Midwest</td><td>-0.4089**</td><td>-0.2359*</td><td>0.6448**</td></tr><tr><td>Northeast</td><td>-0.1904</td><td>0.2077</td><td>-0.0172</td></tr><tr><td>South</td><td>0.2832**</td><td>-0.1560</td><td>-0.1272</td></tr><tr><td rowspan="9">Industry type</td><td>Agriculture, foresting, fishing</td><td>-0.3792</td><td>0.1770</td><td>0.2022</td></tr><tr><td>Construction</td><td>-0.1379</td><td>0.3663</td><td>-0.2284</td></tr><tr><td>Finance, insurance, real estate</td><td>-0.0264</td><td>0.7793</td><td>-0.7528</td></tr><tr><td>Manufacturing</td><td>-0.3944**</td><td>0.2420</td><td>0.1524</td></tr><tr><td>Mining</td><td>-0.0098</td><td>-0.3940</td><td>0.4038</td></tr><tr><td>Public administration</td><td>0.8659*</td><td>-1.7104*</td><td>0.8445</td></tr><tr><td>Retail trade</td><td>-0.1873</td><td>0.0610</td><td>0.1263</td></tr><tr><td>Services</td><td>0.2854</td><td>0.3475</td><td>-0.6329</td></tr><tr><td>Transportation, electric, gas</td><td>-0.1212</td><td>-0.3673*</td><td>0.4885</td></tr><tr><td>Pseudo- $R^2$ (overall 93.71%) (%)</td><td></td><td>1.2900</td><td>13.5000</td><td>50.9800</td></tr></table>

∗5% significant; ∗∗1% significant.

Note that the overall model pseudo- $\cdot R ^ { 2 }$ for the three-segment regression is 93.7%, even though the $R ^ { 2 }$ for each segment is 1.29%, 13.5%, and 50.98%, respectively. There are several possible reasons behind the low $\setminus { }$ within a segment: (1) low variations in the dependent variable for Segments 1 and 2, (2) there might be other variables that could influence the EPS decision. This, however, is not a shortcoming of the finite mixture methodology. On the contrary, it represents a significant advantage of finite mixture models in predicting adoption, because segmentation itself accounts for a significant portion of EPS variations across segments. In the three-segment mixture solution, the EPS rate for each segment is 0.67%, 96.26%, and 45.28%, respectively. In other words, given the observable firm characteristics, if a firm is classified into Segment 1 (Segment 2), then we are fairly confident that the EPS decision for the firm will be 0 (1). The same cannot be said for standard regression/clustering approaches, as is evident from the standard logit and the two-stage analysis in the beginning of this section.

We also compute the z-statistics to test each individual class-specific parameter for statistical significance. The parameter estimates with asterisks in Table 6 those that are statistically significant $( \mathrm { i . e . , }$ the absolute values of the z-scores are above 1.96) within each segment. Again, the effect coding mechanism was selected for nominal variables. The $\beta _ { s }$ effect estimates under the column labeled Segment 1 (large laggards) suggest that the EPS decision for firms in Segment 1 is influenced in a negative way by financing option for which financing option <sub>=</sub> lease $( \beta _ { 1 } ^ { ( 2 ) } = - 1 . { \dot { 7 } } 6 9 3 )$ not at all by payment amount $( \beta _ { 1 } ^ { ( 1 ) } = 0 . 0 5 1 8 )$ . Similarly, the EPS decision for firms in Segment 3 is influenced in a negative way by financing option <sub>=</sub> lease $( \beta _ { 3 } ^ { ( 2 ) } = - 1 . 6 8 3 5 )$ , in a positive way by payment amount $( \beta _ { 3 } ^ { ( 1 ) } = 4 . 6 9 8 1 )$ . Members of Segment 2 are less likely $\mathsf { \bar { ( } } \beta _ { 2 } ^ { ( 1 ) } = - 1 . 9 7 0 6 )$ to adopt EPS as the payment amount increases, but they are not influenced by financing option $( \beta _ { 2 } ^ { ( 2 ) } = 0 . 1 2 1 \dot { 4 } )$ . Note that financing option affects the EPS decision roughly in the same direction for all segments. The $\mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta } \mathbf { \eta \eta } \mathbf { \eta } \mathbf { \eta \eta } \mathbf { \eta \eta } \mathbf { \eta \eta }$ effect estimates for firm size equal $( 1 . { \overset { \vartriangle } { 7 } } 0 1 1 , - 0 . 3 1 0 8 , - 1 . 3 9 9 3 )$ , suggesting that large firms have a higher probability of belonging to Segment 1. This makes intuitive sense because large firms are less likely to use EPS (average $\mathrm { E P S } = 0 . 6 \hat { 7 \% }$ for Segment 1). The industry effect shows that firms in the public administration section have a higher probability of belonging to Segment 1 (large laggards) and a lower probability of belonging to Segment 2 (nimble adopters). The region effect indicates that firms from the midwest are more likely than those from other regions to belong to Segment 3, but less likely to belong to Segments 1 and 2.

Finally, we applied the three-segment mixture model to those cases in the holdout sample, and computed the predicted values of EPS. The prediction accuracy of the finite mixture model was 89.4%, 90.7%, and 73.8% for each segment, respectively. The overall prediction accuracy was 89.2%. The finite mixture model clearly outperforms the standard logit model as well as the two-stage model. For the present data set, it represents a performance improvement of approximately 17% in prediction accuracy. We also checked the prediction accuracy for the four, five, six-segment solution in the holdout sample. The proportion of EPS choices correctly predicted for these solutions hover around 89.3%. In other words, increasing the number of segments does not increase the prediction accuracy of the model, further corroborating our choice of a three-segment solution.

## 4.4. Model Comparison and Validation

In this section, we provide a number of tests and compare the finite mixture model with other approaches to further investigate the appropriateness of finite mixture model. Below, we first report our findings from the logit regression with interaction effects followed by the hierarchical logit models. In addition, because of the asymmetry of our data on EPS adoption, we conducted a complementary log-log regression. We also used stratified sampling to oversample the cases from the EPS adopter class. We scored the model to a holdout set without oversampling to assess its performance. Finally, we randomly generated 10 different holdout samples to further evaluate the predictive power and robustness of the finite mixture model.

As a first step, we performed a logit regression with up to two-way interaction effects between the independent variables. We found that the interaction effects between financing option and firm-level characteristics (region, industry, firm size, and credit risk) are all significant at the 5% level, but none of the interaction effects between payment amount and firm-level characteristics is significant. The model likelihood measure is $- 2 L L = \breve { 9 } , 2 3 3 . 3 6$ . The $R ^ { 2 }$ is about 17% with a predictive accuracy on the test data set of 0.73; both are slightly above the standard logit models.

Our data set contains two levels of information with accounts nested within firms. Hierarchical nonlinear models (Raudenbush and Bryk 2002) can formally represent the two-level structure and specify how variables at one level influence relations occurring at the other level (Hofmann 1997, Raudenbush and Bryk 2002). We examined the effects of account-level and firm-level predictors on EPS adoption using hierarchical logit models in an incremental approach (Ang et al. 2002, Mithas et al. 2006– 2007, Raudenbush and Bryk 2002). First, we specified an unconditional model, in which there were no predictors at either account or firm levels. The unconditional model allowed us to gauge the variation of EPS adoption between firms. We then specified a random coefficient regression model, in which we added only account-level predictors (payment amount, financing option). Subsequently, we added the firm-level predictors (such as firm size, credit risk, region, and industry) to model the randomly varying accountlevel intercept. Finally, we specified a model in which we added predictors of the account-level slopes. This enabled us to assess whether cross-level interactions improve the prediction of EPS adoption. The following are the equations for our account- and firm-level models:

Account-Level Model

$$
\begin{array}{c} \mathbf {l o g i t} (\pi_ {i j}) = \beta_ {0 j} + \beta_ {1 j} * \mathbf {F i n a n c i n g O p t i o n} _ {i j} \\ + \beta_ {2 j} * \mathbf {P a y m e n t A m o u n t} _ {i j} + r _ {i j}. \end{array}
$$

Firm-level Model

$$
\begin{array}{l} \beta_ {0 j} = \gamma_ {0 0} + \gamma_ {0 1} * \textbf {F i r m S i z e} _ {j} + \gamma_ {0 2} * \textbf {C r e d i t R i s k} _ {j} \\ \qquad + \gamma_ {0,   3 - 5} * \textbf {R e g i o n} _ {j} + \gamma_ {0,   6 - 1 4} * \textbf {I n d u s t r y} _ {j} + u _ {0 j}, \\ \beta_ {1 j} = \gamma_ {1 0} + \gamma_ {1 1} * \textbf {F i r m S i z e} _ {j} + \gamma_ {1 2} * \textbf {C r e d i t R i s k} _ {j} \\ \qquad + \gamma_ {1,   3 - 5} * \textbf {R e g i o n} _ {j} + \gamma_ {1,   6 - 1 4} * \textbf {I n d u s t r y} _ {j} + u _ {1 j}, \\ \beta_ {2 j} = \gamma_ {2 0}. \end{array}
$$

Substitution of firm-level equations into their corresponding account-level terms yields the following equation with a complex error structure:

$$
\begin{array}{l} \mathbf {l o g i t} (\pi_ {i j}) = \gamma_ {0 0} + \gamma_ {0 1} * \mathbf {F i r m S i z e} _ {j} + \gamma_ {0 2} * \mathbf {C r e d i t R i s k} _ {j} \\ \qquad + \gamma_ {0, 3 - 5} * \text {Region} _ {j} + \gamma_ {0, 6 - 1 4} * \text {Industry} _ {j} \\ \qquad + \gamma_ {1 0} * \text {FinancingOption} _ {i j} \\ \qquad + \gamma_ {2 0} * \text {PaymentAmount} _ {i j} \\ \qquad + [ \gamma_ {1 1} * \text {FirmSize} _ {j} + \gamma_ {1 2} * \text {CreditRisk} _ {j} \\ \qquad + \gamma_ {1, 3 - 5} * \text {Region} _ {j} + \gamma_ {1, 6 - 1 4} * \text {Industry} _ {j} ] \\ \qquad * \text {FinancingOption} _ {i j} \\ \qquad + [ u _ {0 j} + u _ {1 j} * \text {FinancingOption} _ {i j} + r _ {i j} ]. \end{array}
$$

Before estimating the models, we centered all continuous variables (payment amount, firm size, and credit risk) using grand mean centering and left dummy variables (financing option, region, and industry) uncentered for easy interpretation of results (Raudenbush and Bryk 2002). With these centering decisions, the intercept at the account level represents the expected likelihood of EPS adoption for an account financed with loan and an average payment amount across the entire sample.

We estimated our models in hierarchical linear models (HLM) version 6 (Raudenbaush and Bryk 2002) using restricted maximum quasi-likelihood with overdispersion for EPS. Table 7 reports detailed results from the estimation of the hierarchical logit models. Tests indicate significant variance to be explained in EPS adoption $\stackrel { \triangledown } { ( \chi } ^ { 2 } = 2 6 , 4 8 5 . 2 9 , \mathrm { d f } = 3 , 6 9 0 ,$ $p \overset { - } { < } 0 . 0 0 1 )$ . The significance of the incremental variance explained for various hierarchical models is apparent by examining the log-likelihood (LL) function value. It should be noted that the values obtained for the log-likelihood are $- 2 L L = 9 , 7 8 0 . 3 5$ in the standard logit model and $- 2 L L = 5 , 3 7 4 . 0 9$ in the mixture model. Even though these models have a different number of parameters, the BIC for the finite mixture model is still the smallest (5,705 as compared to 9,744 for the hierarchical model and 9,935 for the standard logit model), indicating a better fit of the mixture model.

We also observed that the influence of various predictor variables in the hierarchical logit models is consistent with that from the standard logit and mixture models, e.g., small firms are more likely to adopt EPS. Region and industry also have similar effects. Note that payment amount does not seem to have a significant influence on EPS in the hierarchical logit model.

In our data set, the average EPS adoption rate is about 29%. In situations where the probability density function is asymmetric (e.g., density for the extreme value distribution), the complementary loglog regression model might be necessary (Allison 1999). We estimated this model using the GENMOD procedure in SAS and found that qualitative effects of predictor variables on EPS adoption are very similar to the standard logit model. The LL value is given by $- 2 L L = 9 , 7 9 4 . 6 8 , R ^ { 2 }$ is about 11.6% with predictive accuracy of $7 1 . 5 \% ,$ again comparable with the standard logit model. Finally, oversampling has been suggested by many researchers as a proper sampling approach (e.g., Shmueli et al. 2006) to model rare event, i.e., EPS adoption in our case. We constructed our training data set by randomly oversampling 50% of the EPS accounts along with a random sample of equal number of non-EPS accounts. The holdout data set contained the other 50% of the EPS accounts and a random sample of the remaining non-EPS accounts such that the ratio of EPS to non-EPS accounts in the holdout data set is approximately the same as that in the population (29%). With oversampling, the $R ^ { 2 }$ improves slightly to 14.3% but the predictive accuracy on the holdout data set drops to about 63%.

To further evaluate the predictive accuracy of the finite mixture model, we randomly generated 10 different holdout samples using different random number seed values each time. We then applied the three-segment mixture model onto the 10 holdout samples. Results show the robustness of the finite mixture model with the predictive power ranging from 89.2% to 90.6% and an average predictive accuracy of 90.2%. Using the hierarchical logit model, the predicative accuracy on the holdout sets ranges from 71.3% to 72.6% with an average of 72.0%, again slight improvement over the standard logit model.

We attribute the higher predictive ability of the mixture model to its higher statistical power relative to the other approaches. The model comparison informs us that adding the segment-level variables increases the explanatory and predictive power of the model. The finite mixture approach improves over other approaches because of the simultaneous estimation of the latent firm-level class (segments) variables and the marginal impacts of the account-level variables on the likelihood of EPS adoption. Not only is the segmentation itself more principled (i.e., model based), it does not suffer from the suboptimality problems of sequentially doing the segmentation and the classification. By this, we mean that the segments are optimally discovered to optimize the overall classification prowess of the model.

## 5. Implications and Conclusions

For firms such as the Fortune 100 company in our study, financing large commercial purchases for their customers is a standard operating procedure involving high stakes. In such settings business value from information technology (IT) is measured by how it can impact the key metrics, such as the cash conversion cycle, from line items on the income statements and balance sheets that managers can influence. Having invested significantly in adopting an EPS technology, the firm was unable to realize the potential benefits from this interorganization technology because its business customers were lagging in their adoption of the same. Realizing that increasing EPS adoption has a direct link in improving firm’s cash conversion cycles by shortening the accounts receivables period, the firm was keen to explore ways to target its customers more precisely using the available archival data they had. We showcase the development and testing of an actionable and easy-to-replicate EPS segmentation scheme to predict future EPS adoptions and direct segment-specific marketing strategies to firms based on observable information. We next discuss the key findings, limitations, and implications.

## 5.1. Findings

This research presents a finite mixture logit model that can simultaneously classify firms into homogeneous segments and test the effects of predictor factors on firm’s decision choices within these segments. The proposed approach also addresses the presence of hierarchical structure in data analysis. While much of the IS literature has focused on developing, and subsequently empirically testing, theories explaining technology adoption and diffusion, we believe our contribution is to showcase the importance of having a segment-based predictive approach to this issue. In particular, our approach, based on a relatively unused methodology in IS, provides practical and segmentlevel actionable guidance to managers who would like to predict which of a list of candidate firms are more likely to adopt a new technology. Both predictive and explanatory models have their complementary roles in advancing theory and practice (Shmueli and Koppius 2007), and it is in that spirit that we believe we plug an important gap in the IS technology adoption literature.

Table 7 Results of Hierarchical Logit Models

<table><tr><td rowspan="2" colspan="2">Variables</td><td colspan="2">Unconditional model</td><td colspan="2">Account-level model with random intercept</td><td colspan="2">Full model</td></tr><tr><td>Coefficient</td><td>Std. error</td><td>Coefficient</td><td>Std. error</td><td>Coefficient</td><td>Std. error</td></tr><tr><td>Intercept</td><td> $\beta$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Intercept 2</td><td> $\gamma00$ </td><td>-2.12***</td><td>0.09</td><td>-2.35***</td><td>0.35</td><td>-1.45**</td><td>0.59</td></tr><tr><td>Firm size</td><td> $\gamma01$ </td><td></td><td></td><td>-2.73***</td><td>0.47</td><td>-0.25</td><td>0.84</td></tr><tr><td>Credit risk</td><td> $\gamma02$ </td><td></td><td></td><td>-0.08</td><td>0.08</td><td>0.07</td><td>0.11</td></tr><tr><td>Midwest</td><td> $\gamma03$ </td><td></td><td></td><td>0.97***</td><td>0.24</td><td>1.61***</td><td>0.37</td></tr><tr><td>Northeast</td><td> $\gamma04$ </td><td></td><td></td><td>1.35***</td><td>0.26</td><td>1.45***</td><td>0.38</td></tr><tr><td>South</td><td> $\gamma05$ </td><td></td><td></td><td>-0.50**</td><td>0.25</td><td>-0.24</td><td>0.36</td></tr><tr><td>Agriculture, foresting, fishing</td><td> $\gamma06$ </td><td></td><td></td><td>0.73</td><td>0.77</td><td>-0.55</td><td>1.20</td></tr><tr><td>Construction</td><td> $\gamma07$ </td><td></td><td></td><td>0.51</td><td>0.40</td><td>-0.12</td><td>0.64</td></tr><tr><td>Finance, insurance, real estate</td><td> $\gamma08$ </td><td></td><td></td><td>0.81</td><td>0.61</td><td>0.01</td><td>0.98</td></tr><tr><td>Manufacturing</td><td> $\gamma09$ </td><td></td><td></td><td>0.73**</td><td>0.33</td><td>0.07</td><td>0.59</td></tr><tr><td>Mining</td><td> $\gamma00$ </td><td></td><td></td><td>-1.11</td><td>0.76</td><td>-1.95*</td><td>1.13</td></tr><tr><td>Public administration</td><td> $\gamma11$ </td><td></td><td></td><td>-3.71***</td><td>0.99</td><td>-3.69**</td><td>1.50</td></tr><tr><td>Retail trade</td><td> $\gamma12$ </td><td></td><td></td><td>-0.33</td><td>0.63</td><td>-1.20</td><td>0.98</td></tr><tr><td>Services</td><td> $\gamma13$ </td><td></td><td></td><td>-0.68*</td><td>0.38</td><td>-1.43**</td><td>0.66</td></tr><tr><td>Transportation, electric, gas</td><td> $\gamma14$ </td><td></td><td></td><td>-0.75**</td><td>0.34</td><td>-0.93</td><td>0.61</td></tr><tr><td>Financing slope</td><td> $\beta_1$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Intercept 2</td><td> $\gamma10$ </td><td></td><td></td><td>-0.37***</td><td>0.10</td><td>-1.83**</td><td>0.75</td></tr><tr><td>Firm size</td><td> $\gamma11$ </td><td></td><td></td><td></td><td></td><td>-5.04***</td><td>1.23</td></tr><tr><td>Credit risk</td><td> $\gamma12$ </td><td></td><td></td><td></td><td></td><td>-0.30**</td><td>0.14</td></tr><tr><td>Midwest</td><td> $\gamma13$ </td><td></td><td></td><td></td><td></td><td>-0.87*</td><td>0.48</td></tr><tr><td>Northeast</td><td> $\gamma14$ </td><td></td><td></td><td></td><td></td><td>-0.05</td><td>0.50</td></tr><tr><td>South</td><td> $\gamma15$ </td><td></td><td></td><td></td><td></td><td>-0.36</td><td>0.47</td></tr><tr><td>Agriculture, foresting, fishing</td><td> $\gamma16$ </td><td></td><td></td><td></td><td></td><td>1.88</td><td>1.31</td></tr><tr><td>Construction</td><td> $\gamma17$ </td><td></td><td></td><td></td><td></td><td>0.52</td><td>0.84</td></tr><tr><td>Finance, insurance, real estate</td><td> $\gamma18$ </td><td></td><td></td><td></td><td></td><td>0.90</td><td>1.27</td></tr><tr><td>Manufacturing</td><td> $\gamma19$ </td><td></td><td></td><td></td><td></td><td>0.94</td><td>0.73</td></tr><tr><td>Mining</td><td> $\gamma00$ </td><td></td><td></td><td></td><td></td><td>1.20</td><td>1.47</td></tr><tr><td>Public administration</td><td> $\gamma111$ </td><td></td><td></td><td></td><td></td><td>-0.28</td><td>1.78</td></tr><tr><td>Retail trade</td><td> $\gamma112$ </td><td></td><td></td><td></td><td></td><td>1.39</td><td>1.16</td></tr><tr><td>Services</td><td> $\gamma113$ </td><td></td><td></td><td></td><td></td><td>0.97</td><td>0.82</td></tr><tr><td>Transportation, electric, gas</td><td> $\gamma114$ </td><td></td><td></td><td></td><td></td><td>-0.21</td><td>0.75</td></tr><tr><td>Payment amount slope</td><td> $\beta_2$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Intercept 2</td><td> $\gamma20$ </td><td></td><td></td><td>0.06</td><td>0.11</td><td>0.23</td><td>0.55</td></tr><tr><td>-2 LL</td><td></td><td>11,164.00</td><td></td><td>10,845.80</td><td></td><td>9,489.80</td><td></td></tr></table>

∗p < 010; ∗∗p < 005; ∗∗∗p < 0001.

We applied the finite mixture methodology to predict the likelihood of EPS adoption in a B2B context using a unique data set from a Fortune 100 company.

Firm-level specific information was used to determine segment membership probabilities. We found that there exist three distinct segments of firms with significant variations in EPS adoption rates across segments. Firm size, region, industry, and credit risk were all determinants of segment membership. In addition, the decision choices of EPS adoption across the three segments were also found to differ significantly in their sensitivity to account-level variables, including payment amount and financing option.

To assess the validity of the finite mixture model, we compared it with other baseline models (the standard logit model, two-stage model, hierarchical logit models, and complementary log-log model). In addition, we also used stratified sampling and generated different holdout samples to further evaluate the performance and robustness of the mixture model. Our results demonstrated the superiority of our approach over traditional methods in that (1) it fits the data better, (2) explicit segmentation is important and finite mixture model leads to a better delineation of segments, and (3) it significantly improves the predictive accuracy in multiple holdout samples.

A natural question that arises is: To what extent is the finite mixture model useful for questions being addressed by other IS researchers? While we are cautious in projecting too far beyond the immediate domain of B2B EPS adoption (that is the subject of future research), we do recommend that IS researchers should consider finite mixture models when they have strong priors that suggest underlying and ex ante unknown mixtures of distributions of IT adopting end-users or firms whose behavior they are trying to explain. Uncovering and breaking down this heterogeneity in a formal model-based manner is the real benefit of finite mixture models.

## 5.2. Limitations

Before discussing the implications of this study, there are several limitations that need to be recognized. First, other unobserved variables might affect a firm’s EPS decision. For instance, future research will benefit from having a temporal history of adoption behavior. If such data are available, they can be easily incorporated in the finite mixture model. This will then permit a temporal diffusion analysis and lead to new level of insights. Second, there is the issue of possible endogeneity between payment amount and EPS decision. While we do not have a rigorous statistical test (because of the lack of an appropriate instrument variable) for checking the endogeneity issue, we do believe the monthly payment amount of an account is not dependent on whether the account is on EPS or not. Third, our data set is based on the commercial equipment bill data from a single vendor. It would be an interesting exercise to replicate the techniques presented here to data sets from other vendors, and see whether one can still obtain well-delineated segments with high predictive accuracy. Alternatively, one can use Monte Carlo simulation and test the predictive power of the finite mixture model with simulated data sets. An exemplar work in this area can be found in Chin et al. (2003). Finally, there are limitations associated with finite mixture models such as assumptions of specific distributions for the segment, speed, and convergence of the algorithm, optimality of solutions, etc. A number of researchers (e.g., DeSarbo et al. 2008) in recent years have proposed alternative procedures to try to overcome these limitations.

## 5.3. Implications for Research and Practice

Finite mixture models have been successfully applied in many fields, including marketing, economics, biology, and social sciences. These models provide a flexible mathematical-based approach to the statistical modeling of heterogeneity in the population and are able to better handle situations where a single parametric family cannot provide a satisfactory model for local variations in the observed data (McLachlan and Peel 2000). This study provides several managerial insights that have implications for increasing EPS (or other new technology) adoptions. Perhaps the most important finding of this research is that model-based and principled customer segmentation improves EPS prediction. Our results suggest that a well-delineated segmentation scheme is the key to predict EPS adoptions. The mixture model prescribes what segment a firm belongs to based on firm characteristics. Each segment responds differently to the EPS decisions. For example, small firms that have a moderate monthly payment amount are more likely to adopt EPS. Firms from a particular industry (e.g., public administration) are almost always slow adopters of EPS. Market segmentation allows the Fortune 100 company to select target segments and develop corresponding strategies for each segment. For instance, moving forward, the Fortune 100 company should target Segment 2 and provide effective ways (e.g., targeted mailing, small cash incentives, etc.) to get a selected list of firms from that segment onto EPS.

Our results also suggest that the EPS decision across segments can differ significantly in their sensitivity to account-level predictors. For example, while accounts from Segments 1 and 3 that are financed with a lease are, in general, less likely to be paid using EPS, payment amounts have different influences on EPS between Segments 2 and 3. If an account is classified into Segment 2, the more the payment amount, the less likely that this account will be paid using EPS. The opposite effect is true for accounts classified into Segment 3. This can probably explain why on the aggregate level, the effect of payment amount is not significant in the hierarchical logit models.

This research has several theoretical implications. While segmentation (clustering) of user behavior/ decision has received a lot of attention in the IS literature over the last few years, the analysis was usually done using traditional clustering algorithms (e.g., K-means, hierarchical). One of the difficulties in clustering is the selection of the optimal number of segments in the solution. Determining the number of segments using multiple information criteria is clearly an advantage of the finite mixture model. In addition, the methodology presented in this work can be extended to model formulations other than the logit (i.e., dependent variable is not binary). It can also be applied to other problem contexts as well, such as predicting auction behaviors of various user groups. For instance, Bapna et al. (2004) classify auction bidders into five different segments. One possible extension of their work could be asking whether these segments, together with other bidder characteristics such as demographics and risk profiles, impact the winning likelihood of a given bidder in an auction. The finite mixture approach would be ideally suited toward detecting perhaps a different set of bidder segments optimized toward increasing the classification accuracy of a bidder’s likelihood to win.

Finally, this study emphasizes the importance of predictive modeling in the IS literature. Not only is it relevant for practical purposes (e.g., predicting future behaviors and patterns of customers), it is also of value for theory building in fast-changing environments (such as online auctions, online social interactions), where data are plentiful and can be easily collected. Predictive modeling can help uncover potential causal relationships, which could lead to new theories being developed (Shmueli and Koppius 2007).

## Acknowlegment

This research is partially supported by Treibick Electronic Commerce Initiative.

## Appendix

In this appendix, we provide the descriptive statistics for the two-stage clustering solution and the finite mixture solution.

Table A.1 Descriptive Statistics for Two-Stage Clustering Analysis

<table><tr><td></td><td colspan="3">Segments</td></tr><tr><td>Variables</td><td>1</td><td>2</td><td>3</td></tr><tr><td colspan="4">Account-level data</td></tr><tr><td>Payment amount ($)</td><td>19,514.63</td><td>43,414.04</td><td>10,490.61</td></tr><tr><td colspan="4">Financing option</td></tr><tr><td>—Lease</td><td>55</td><td>754</td><td>5,328</td></tr><tr><td>—Loan</td><td>2,462</td><td>479</td><td>0</td></tr><tr><td>EPS (%)</td><td>41.52</td><td>18.57</td><td>25.32</td></tr><tr><td colspan="4">Firm-level data</td></tr><tr><td>PAYDEX</td><td>70.02</td><td>73.14</td><td>71.32</td></tr><tr><td>Firm size</td><td>582</td><td>7,509</td><td>1,944</td></tr><tr><td colspan="4">Region</td></tr><tr><td>—Midwest</td><td>417</td><td>12</td><td>666</td></tr><tr><td>—Northeast</td><td>350</td><td>13</td><td>410</td></tr><tr><td>—South</td><td>328</td><td>314</td><td>506</td></tr><tr><td>—West</td><td>334</td><td>216</td><td>327</td></tr><tr><td colspan="4">Industry</td></tr><tr><td>—Agriculture, foresting, fishing</td><td>19</td><td>0</td><td>37</td></tr><tr><td>—Construction</td><td>283</td><td>1</td><td>124</td></tr><tr><td>—Finance, insurance, real estate</td><td>40</td><td>1</td><td>51</td></tr><tr><td>—Manufacturing</td><td>506</td><td>25</td><td>762</td></tr><tr><td>—Mining</td><td>27</td><td>2</td><td>34</td></tr><tr><td>—Public administration</td><td>10</td><td>17</td><td>49</td></tr><tr><td>—Retail trade</td><td>34</td><td>13</td><td>57</td></tr><tr><td>—Services</td><td>186</td><td>12</td><td>312</td></tr><tr><td>—Transportation, communications</td><td>228</td><td>481</td><td>267</td></tr><tr><td>—Wholesale trade</td><td>96</td><td>3</td><td>216</td></tr><tr><td>Class size</td><td>0.277</td><td>0.136</td><td>0.587</td></tr></table>

Notes. In the table, average values were provided for payment, PAYDEX, number of employees, and EPS; frequency counts were provided for industry, region, and financing option. The clustering analysis was done on the account level. Hence, some firms with multiple accounts might be classified into different segments.

Table A.2 Descriptive Statistics of Three-Segment Mixture

<table><tr><td rowspan="2">Variables</td><td colspan="3">Segments</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>Account-level data</td><td></td><td></td><td></td></tr><tr><td>Payment amount ($)</td><td>19,112.10</td><td>13,143.27</td><td>17,985.48</td></tr><tr><td>Financing option</td><td></td><td></td><td></td></tr><tr><td>—Lease</td><td>4,539</td><td>1,428</td><td>170</td></tr><tr><td>—Loan</td><td>1,758</td><td>1,014</td><td>169</td></tr><tr><td>EPS (%)</td><td>0.67</td><td>96.26</td><td>45.28</td></tr><tr><td>Firm-level data</td><td></td><td></td><td></td></tr><tr><td>PAYDEX</td><td>71.19</td><td>70.17</td><td>77.22</td></tr><tr><td>Firm size</td><td>3,018</td><td>659</td><td>435</td></tr><tr><td>Region</td><td></td><td></td><td></td></tr><tr><td>—Midwest</td><td>654</td><td>300</td><td>86</td></tr><tr><td>—Northeast</td><td>444</td><td>279</td><td>5</td></tr><tr><td>—South</td><td>857</td><td>227</td><td>23</td></tr><tr><td>—West</td><td>598</td><td>223</td><td>7</td></tr><tr><td>Industry</td><td></td><td></td><td></td></tr><tr><td>—Agriculture, foresting, fishing</td><td>33</td><td>17</td><td>1</td></tr><tr><td>—Construction</td><td>243</td><td>140</td><td>1</td></tr><tr><td>—Finance, insurance, real estate</td><td>59</td><td>31</td><td>0</td></tr><tr><td>—Manufacturing</td><td>755</td><td>438</td><td>30</td></tr><tr><td>—Mining</td><td>48</td><td>9</td><td>3</td></tr><tr><td>—Public administration</td><td>65</td><td>1</td><td>3</td></tr><tr><td>—Retail trade</td><td>74</td><td>21</td><td>3</td></tr><tr><td>—Services</td><td>360</td><td>118</td><td>2</td></tr><tr><td>—Transportation, communications</td><td>705</td><td>163</td><td>76</td></tr><tr><td>—Wholesale trade</td><td>211</td><td>91</td><td>2</td></tr><tr><td>Class size</td><td>0.64</td><td>0.27</td><td>0.09</td></tr></table>

Note. In the table, average values were provided for payment, PAYDEX, number of employees, and EPS; frequency counts were provided for industry, region, and financing option.

## References

Abrahamson, E., L. Rosenkopf. 1997. Social networks on the extent of innovation diffusion: A computer simulation. Organ. Sci. 8(3) 289–309.

Agarwal, R., J. Prasad. 1997. The role of innovation characteristics and perceived voluntariness in the acceptance of information technologies. Decision Sci. 28(3) 557–582.

Agarwal, R., V. Sambamurthy, R. M. Stair. 2000. Research report: The evolving relationship between general and specific computer self-efficacy—An empirical assessment. Inform. Systems Res. 11(4) 418–430.

Allison, P. 1999. Logistic Regression Using the SAS System. Wiley-SAS Institute, Chichester, UK.

Andrews, R. L., I. S. Currim. 2003. A comparison of segment retention criteria for finite mixture logit models. J. Marketing Res. 40(2) 235–243.

Ang, S., S. Slaughter, K. Y. Ng. 2002. Human capital and institutional determinants of information technology compensation: Modeling multilevel and cross-level interactions. Management Sci. 48(11) 1427–1445.

Association for Financial Professionals (AFP). 2004. Electronic payments survey. http://www.afponline.org.

Au, Y. A., R. J. Kauffman. 2003. What do you know? Rational expectations in information technology adoption and investment. J. Management Inform. Systems 20(2) 49–76.

Au, Y. A., R. J. Kauffman, F. J. Riggins. 2005. A rational expectations theory of technology adoption: Evidence from the electronic billing industry. Workshop Inform. Systems Econom. University of California at Irvine, Irvine.

Bapna, R., P. Goes, A. Gupta, Y. Jin. 2004. User heterogeneity and its impact on electronic auction market design: An empirical exploration. MIS Quart. 28(1) 21–43.

Bozdogan, H., D. E. Ramirez. 1988. FACAIC: Model selection algorithm for the orthogonal factor model using AIC and CAIC. Psychometrika 53(3) 407–415.

Brancheau, J. C., J. C. Wetherbe. 1990. The adoption of spreadsheet software: Testing innovation diffusion theory in the context of end-user computing. Inform. Systems Res. 1(2) 115–143.

Bucklin, R. E., S. Gupta. 1992. Brand choice, purchase incidence, and segmentation: An integrated modeling approach. J. Marketing Res. 29(2) 201–215.

Burke, K. 2005. The impact of firm size on Internet use in small businesses. Electronic Markets 15(2) 5–19.

Chakravorti, S., E. Davis. 2004. An electronic supply chain: Will payments follow. Chicago Federal Letter. Number 206a (September). http://www.chicagofed.org/digital\_assets/publications/ chicago\_fed\_letter/2004/cflseptember2004\_206a.pdf.

Chin, W. W., B. L. Marcolin, P. R. Newsted. 2003. A partial least squares latent variable modeling approach for measuring interaction effects: Results from a Monte Carlo simulation study and an electronic-mail emotion/adoption study. Inform. Systems Res. 14(2) 189–217.

Chwelos, P., I. Benbasat, A. S. Dexter. 2001. Empirical test of an EDI adoption model. Inform. Systems Res. 12(3) 304–321.

Claycamp, H., W. Massy. 1968. A theory of market segmentation. J. Marketing Res. 5 388–394.

Compeau, D. R., C. A. Higgins. 1995. Computer self-efficacy: Development of a measure and initial test. MIS Quart. 19(2) 189–211.

Cotteleer, M., C. Cotteleer, A. Prochnow. 2007. Cutting checks. Challenges and choices for the adoption of B2B electronic payments. Comm. ACM 50(6) 56–61.

Davis, F. 1989. Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quart. 13(3) 319–339.

Davis, F., R. Bagozzi, P. Warshaw. 1989. User acceptance of computer technology: A comparison of two theoretical models. Management Sci. 35(8) 982–1002.

Dayton, M. C., G. B. Macready. 1988. Concomitant variable latent class models. J. Amer. Statist. Soc. 83(401) 173–179.

DeSarbo, W., R. Grewal, C. Scott. 2008. A clusterwise bilinear multidimensional scaling methodology for simultaneous segmentation and positioning analyses. J. Marketing Res. 45(3) 280–292.

Fader, P. S., B. G. S. Hardie. 1996. Modeling consumer choices among SKUs. J. Marketing Res. 33(4) 442–452.

Fishbein, M., I. Ajzen. 1975. Beliefs, Attitude, Intention and Behavior: An Introduction to Theory and Research. Addison-Wesley, Reading, MA.

Forman, C. 2005. The corporate digital divide: Determinants of Internet adoption. Management Sci. 51(4) 641–655.

Gowrisankaran, G., J. Stavins. 2004. Network externalities and technology adoption: Lessons from electronic payments. RAND J. Econom. 35(2) 260–276.

Greene, W. H. 2000. Econometric Analysis, 4th ed. Prentice-Hall, Upper Saddle, NJ.

Gupta, S., P. K. Chintagunta. 1994. On using demographic variables to determine segment membership in logit mixture models. J. Marketing Res. 31(1) 128–136.

Hagenaars, J., A. McCutcheon. 2001. Applied Latent Class Analysis. Cambridge University Press, Cambridge, UK.

Hart, P., C. S. Saunders. 1997. Power and trust: Critical factors in the adoption and use of electronic data interchange. Organ. Sci. 8(1) 23–42.

Hart, P., C. S. Saunders. 1998. Emerging electronic partnerships: Antecedents and dimensions of EDI use from the supplier’s perspective. J. Management Inform. Systems 14(4) 87–111.

Hayashi, F., E. Klee. 2003. Technology adoption and consumer payments: Evidence from survey data. Rev. Network Econom. 2(2) 175–190.

Hofmann, D. A. 1997. An overview of the logic and rationale of hierarchical linear models. J. Management 23(6) 723–744.

Iacovou, C., I. Benbasat, A. Dexter. 1995. Electronic data interchange and small organizations: Adoption and impact of technology. MIS Quart. 19(4) 465–485.

Jeyaraj, A., J. W. Rottman, M. C. Lacity. 2006. A review of the predictors, linkages, and biases in IT innovation adoption research. J. Inform. Tech. 21(1) 1–23.

Kamakura, W. A., G. Russell. 1989. A probabilistic choice model for market segmentation and elasticity structure. J. Marketing Res. 26(4) 379–390.

Kamakura, W. A., B. Kim, J. Lee. 1996. Modeling preference and structural heterogeneity in consumer choice. Marketing Sci. 15(2) 152–172.

Karahanna, E., D. W. Straub. 1999. The psychological origins of perceived usefulness and perceived ease of use. Inform. Management 35(4) 237–250.

Kauffman, R. J., J. McAndrews, Y. M. Wang. 2000. Opening the “black box” of network externalities in network adoption. Inform. Systems Res. 11(1) 61–82.

Kotler, P., K. L. Keller. 2006. Marketing Management, 12th ed. Prentice-Hall, Upper Saddle River, NJ.

Lazarsfeld, P. F., N. W. Henry. 1968. Latent Structure Analysis. Houghton Mifflin, Boston.

Magidson, J., J. K. Vermunt. 2002. Latent class models for clustering: A comparison with K-means. Canadian J. Marketing Res. 20 36–43.

McLachlan, J., D. Peel. 2000. Finite Mixture Models. John Wiley and Sons, New York.

Mithas, S., N. Ramasubbu, M. S. Krishnan, C. Fornell. 2006–2007. Designing Web sites for customer loyalty across business domains: A multilevel analysis. J. Management Inform. Systems 23(3) 97–127.

Oh, S., S. Kurnia, R. Johnston, H. Lee, B. Lim. 2006. A stakeholder perspective on successful electronic payment systems diffusion. Proc. 39th Hawaii Internat. Conf. Systems Sci., Kauai, HI.

Pfeiffer, H. K. C. 1992. The Diffusion of Electronic Data Interchange. Springer-Verlag, New York.

Plouffe, C. R., J. S. Hulland, M. Vanderbosch. 2001. Research report: Richness versus parsimony in modeling technology adoption decisions-understanding merchant adoption of a smart card-based payment system. Inform. Systems Res. 13(2) 208–222.

Premkumar, G., K. Ramamurthy, M. Crum. 1997. Determinants of EDI adoption in the transportation industry. Eur. J. Inform. Systems 6(2) 107–121.

Raudenbush, S. W., A. S. Bryk. 2002. Hierarchical Linear Models: Applications and Data Analysis Methods, 2nd ed. Sage Publications, Thousand Oaks, CA.

Reich, B. H., I. Benbasat. 1990. An empirical investigation of factors influencing the success of customer-oriented strategic systems. Inform. Systems Res. 1(3) 325–347.

Rogers, E. M. 1995. Diffusion of Innovations, 4th ed. Free Press, New York.

Saunders, C. S., S. Clark. 1992. EDI adoption and implementation: A focus on interorganizational linkages. Inform. Resources Management J. 5(1) 9–19.

Shmueli, G., O. Koppius. 2007. Predictive vs. explanatory modeling in IS research. Proc. Conf. Inform. Systems Tech., Seattle. http://www.citi.uconn.edu/cist07/5c.pdf.

Shmueli, G., N. R. Patel, P. C. Bruce. 2006. Data Mining for Business Intelligence. John Wiley and Sons, Hoboken, NJ.

Stavins, J. 2003. Perspective on payments. Regional Rev. 1 6–9.

Straub, D. W., M. Keil, W. Brenner. 1997. Testing the technology acceptance model across cultures: A three country study. Inform. Management 33(1) 1–11.

Taylor, S., P. A. Todd. 1995. Understanding information technology usage: A test of competing models. Inform. Systems Res. 6(2) 144–176.

Teo, H. H., B. C. Y. Tan, K. K. Wei. 1995. Innovation diffusion theory as a predictor of adoption intention for financial EDI. Proc. 1995 Internat. Conf. Inform. Systems, Amsterdam, 155–165.

Teo, H. H., K. K. Wei, I. Benbasat. 2003. Predicting intention to adopt interorganizational linkages: An institutional perspective. MIS Quart. 27(1) 19–49.

Tornatzky, L. G., K. J. Klein. 1982. Innovation characteristics and innovation adoption-implementation: A meta-analysis of find ings. IEEE Trans. Engrg. Management 29(1) 28–45.

Venkatesh, V. 2000. Determinants of perceived ease of use: Integrating perceived behavioral control, computer anxiety and enjoy-

ment into the technology acceptance model. Inform. Systems Res. 11(4) 342–365.

Venkatesh, V., F. Davis. 1996. A model of the antecedents of perceived ease of use: Development and test. Decision Sci. 27(3) 451–481.

Vermunt, J. K., J. Magidson. 2005. Technical Guide for Latent GOLD 4.0: Basic and Advanced. Statistical Innovations Inc., Belmont, MA.

Wedel, M., W. DeSarbo. 1993. A latent class binomial logit methodology for the analysis of paired comparison choice data: An application reinvestigating the determinants of perceived risk. Decision Sci. 24(6) 1157–1169.

Wedel, M., W. A. Kamakura. 2000. Market Segmentation: Conceptual and Methodological Foundations, 2nd ed. Kluwer Academic Publishers, Boston.

Yap, C. S., C. P. P. Soh, K. S. Raman. 1992. Information systems success factors in small business. OMEGA Internat. J. Management Sci. 20(5/6) 597–609.

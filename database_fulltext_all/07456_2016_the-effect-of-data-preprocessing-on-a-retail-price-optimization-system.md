---
otero_id: 7456
otero_key: "9JWCKP49"
title: "The effect of data preprocessing on a retail price optimization system"
authors: "Timo P. Kunz; Sven F. Crone; Joern Meissner"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2016.01.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Timo P. Kunz <sup>a,</sup>⁎<sup>,1</sup>, Sven F. Crone <sup>a,1</sup>, Joern Meissner <sup>b,2</sup>

<sup>a</sup> Management Science Department, Lancaster University Management School, Lancaster, UK

<sup>b</sup> Kuehne Logistics University, Hamburg, Germany

## a r t i c l e i n f o

Article history: Received 21 September 2014 Received in revised form 24 June 2015 Accepted 7 January 2016 Available online 2 February 2016

Keywords: Revenue management Price optimization system Retail pricing Demand modeling Retail scanner data

## a b s t r a c t

Revenue management (RM) is making a significant impact on pricing research and practice, from aviation and hospitality industries to retailing. However, empirical data conditions in retail are distinct to other industries, in particular in the large number of products within and across categories. To set profitable static prices with established RM models, the data is often simplified by data pruning (the exclusion of subsets of data that are deemed irrelevant or unsuitable) and data aggregation (the combination of disparate data points). However, the impact of such data preprocessing, despite being ubiquitous in retailing, is insufficiently considered in current RM research. This could induce potential sources of bias for the demand model estimates, as well as subsequent effects on the price optimization system, the optimized price set, and the profit maxima, which have not yet been investigated. This paper empirically studies the impact of two commonly used data preprocessing techniques in retail RM, data pruning and data aggregation, using simulated and empirical retail scanner data. We numerically assess potential biases introduced by data preprocessing using a systems perspective in estimating a two-stage demand model, the resulting price elasticities, optimized price sets, and the ensuing profit that it yields. Results show that both data aggregation and data pruning bias demand model estimates, albeit with different effect, but both produce less profitable price sets than unbiased reference solutions. The results demonstrate the practica importance of data preprocessing as a cause for estimation bias and suboptimal pricing in retail price optimization systems.

© 2016 Elsevier B.V. All rights reserved

## 1. Introduction

Research in revenue management (RM) has revolutionized the pric ing decisions of airlines. Since then, other industries such as passenger railways, cruise lines, hospitality and retail have followed suit and adopted similar approaches in an attempt to improve revenues and profits [17]. However, the data conditions in the retail industry show key differences to those of traditional RM, in particular due to the product assortment sizes and structures. Further, unlike in other industries, a static pricing problem dominates in which the retailer needs to determine a regular shelf price for a continuously replenished, usually fast moving (and therefore virtually nonperishable) product [15].

To apply the established RM models developed in other industries for such granular data, e.g. to estimate demand using choice models, the data are commonly preprocessed. Researchers, at their discretion, prune the data by selecting data subsets while ignoring other available data points, or aggregate data by combining separate data points to an aggregated observation. For example, various research studies assess the efficacy of novel demand models within the category of refrigerated orange juices of the established Dominicks database [14], but all use different data subsets for evidence. Of the 228 distinct refrigerated juices in the category, [7] assess their proposed model only on the three top selling brands, [23] on 8 products, and [19] on 11 products, all implicitly pruning the majority of the category sales and price information of the products not considered. Anderson and Vilcassim [2] assess their model on 4 brands, but instead of pruning they aggregate all remaining sales and prices to one contrived ‘others’. Intuitively, such practices of pruning and aggregation induce potential sources of bias in estimating established RM models for retail. However, despite the ubiquity of pruning and aggregation on retail data, the effect of data preprocessing on demand estimates, as well as subsequent effects on price elasticities, the optimized price set, and the resulting profit maxima have not been investigated in RM research. Also, arising from the lack of prior studies, there exists no established best practice on how retail data should be preprocessed by either pruning or aggregation to reduce bias for different modeling purposes and assortment sizes.

Consequently, we seek to investigate the sensitivity of a retail RM system to the practices of data preprocessing through data pruning and aggregation, and to quantify the estimation biases introduced. We consider a static price optimization problem for regular (non-promotional) prices in a multi-product retail scenario as it can be found in most retail store formats where products are continuously replenished and are virtually imperishable. We focus on a single category as a subset of the assortment. Following [13] who introduce a model that is divided into a twostage demand model and a decision model, we formulate a pricing decision support system that is segmented into three parts: a data model that captures the relevant data preprocessing options, a two-stage demand model that consists of a category and a market share model, and a single objective price optimization model that determines profit optimal prices for each product. We then focus on the interactions of these components to evaluate how the data preprocessing translates into profit suboptimal price sets determined by the system. The effects are assessed on empirical data of refrigerated orange juice from Dominicks database, as well as artificial weekly store-level data with representative data properties representative.

The contribution of the study is twofold: (1) We demonstrate how the modeling choices of pruning and aggregation affect price optimization results, and analyze the interplay between the components of an RM decision support system. The study illustrates the existence, relevance and varying influence of the effects described and their potential for introducing bias into a price optimization system, questioning the validity of prior studies. (2) We apply a holistic, systems based view on a retail price optimization system that is composed of models for data, demand and optimization in accordance with [11], who describe the technical aspects of a pricing decision support system. This allows us to not only investigate the sensitivity of the demand parameter estimates and price elasticities but also of the optimal price-profit combinations in the context of the interplay between the components of a RM decision support system, and, ultimately, determine the resulting scale of profit suboptimality of the system.

The findings suggest a significant impact on retail RM research and practices. First, as pruning and aggregating introduce an estimation bias, and subsequently lead to suboptimal results of price sets and the resultant profitability, future studies should attempt to estimate solutions for complete categories without data preprocessing. Second, the identified estimation biases from pruning or aggregation raise questions as to the empirical validity and reliability of price sets and profitability identified in prior research studies, and thus the application of said models on retail data. For models showing different sensitivity to pruning or aggregation, their relative merit for large retail assortments must be reconsidered. And third, as pruning and aggregation induce different biases in the estimation, we derive recommendations and providing future guidance to the use of less sensitive data preprocessing and more valid results. As these aforementioned models are currently applied in practice, this would have a significant impact on retail RM practices, also affecting the bottom line of retailers engaging in RM.

We begin with a review of the relevant literature in Section 2. In Section 3, we introduce a price optimization system that is segmented into a data model, a 2-stage demand model that is split into category demand, and market share model, and an optimization model. In Section 4, we describe the methodology of a numerical study that allows us to demonstrate the effects discussed above. In Section 5, we first demonstrate the main system effects of aggregating and pruning brands with varying cumulated market share. We then gradually introduce more realistic conditions and illustrate the relevance of model and data properties by evaluating to what extent the bias introduced by the experimental conditions is passed through the system to the price optimization results. We explore the wider relevance of the results in Section 6.

## 2. Data pre-processing and the static retail price optimization system

Revenue management literature, systems, and applications have predominantly focused on the dynamic pricing problem in the aviation industry. In retail, a similar, dynamic pricing problem exists in the form of optimal markdown determination (overviews in [10,4,12]).

However, RM for retailing of fast moving consumer goods is dominated by a static pricing problem in which the retailer needs to determine an optimal regular shelf price for a continuously replenished and therefore virtually non-perishable product. Despite its prevalence in practice, and its unique properties and problem characteristics, static price optimisation has not received as much attention in research (for an overview, readers are referred to [15]). As this paper focusses on empirically viable systems for normative static price setting, which encompasses the core components of demand modeling and price optimization models, we seek to review the relevant literature on data conditions and the modeling choices and biases they induce.

Numerous system configurations and demand model formulations have been presented in literature for static retail price optimization systems, with the majority of publications proposing extensions of choice-based demand models [24]. Put forward a comprehensive system based on a multinomial logit (MNL) model. They incorporate category response in the objective function by including a nonlinear function based on a mean of brand prices and a price elasticity parameter [16]. Propose a MNL as an approximation for a mixed logit model which includes a non-purchase option for the special case of an automotive spare parts dealer. The resulting estimation problem is mitigated by the assumption that maximum weekly sales of a product over all weeks serve as market potential [13]. Present an optimization system with a two-step demand model that uses a linear configuration for category sales and three different choice model configurations for market share. Beyond models based on MNL, a multitude of alternative approaches exists [2]. Describe a variation of the Almost Ideal Demand System in which they explicitly model category expenditure [20]. Present a multi-objective price optimization system that includes a reference price model and is based on a linear demand model formulation [25]. Introduce a decision support system that integrates the retailer's business rules and different pricing models over the assortment hierarchy [18]. Uses a log–log demand model incorporating asymmetric cross-price elasticities using a Bayesian estimation procedure.

However, none of the papers explicitly consider the empirical data conditions ubiquitously found in retail RM. Some contributions investigate how the results based on such models are affected by the properties of the model, the modeling approach or the underlying data, though the empirical viability of the models is rarely assessed in this context. On one side of the spectrum, articles evaluate the effect of model formulations on model parameters [26,1], elasticities [5] or the optimization results [21,13]. On the other side, a number of contributions address the impact of specific properties of retail data, consumer behavior or other problem parameters on the model or on price elasticities [9,8,27]. The latter are mostly focused on model fit and tend not to observe the implications for price elasticity estimates and the consequences for price optimization results.

With retail data showing unique properties for RM, as assortments typically span hundreds of products per category and dozens of categories, the MNL models widely used in RM cannot simply be estimated across such a wide set of product choices. To remedy the complexity, most authors alter the data conditions through data preprocessing, pruning or aggregating multiple SKUs in the relevant category to simplify estimation. However, the influence of these data preprocessing techniques is not well explored even though it is an important part of the modeling process. Only three papers have explicitly studied the effect of data- and estimation-related modeling decisions in the retail context. Zanutto and Bradlow [28] investigate the effect of data pruning on parameter bias and find biased parameter estimates dependent on the pruning technique used. Andrews and Currim [3] study the effects of aggregation to the brand, brandsize and stock-keeping-unit (SKU) level. They also report significant parameter bias. Briesch et al. [6] focus on the inclusion of zero brand sales in choice model estimation and even evaluate the effects on price elasticities, which also show significant effects. None of these contributions address the effect on the optimality of the price optimization system, and the majority of RM publications remains completely agnostic as to the implicit choices made in analyzing only subsets of SKUs in a category. Similarly, in the literature on robust optimization the effects of data preprocessing have not been addressed. Only [22] presents an MNL-based model for revenue maximization in a retail assortment planning context considering worst case revenue effects for inaccurate parameter estimates that may arise from estimation under limited data. With data pruning and aggregation ubiquitous in retail RM research and practice, this presents a significant gap which this study seeks to address.

We augment the body of work presented above by applying a decision support systems perspective to an empirically motivated revenue management problem. We investigate how pruning and aggregation affect model estimates and elasticities, and also resulting prices and profits estimated by the system. Similar to [11] who describe the technical aspects of a pricing decision support system in three ‘layers’, defining a ‘Data Source’ and a ‘Pricing Core’, and [13] who introduce a model that is divided into a two-stage demand model and a decision model, we formulate a pricing decision support system that is segmented into three parts: a data model that captures the relevant data preprocessing options, a two-stage demand model that consists of a category and a market share model, and a single objective price optimization model that determines profit optimal prices for each product. We then focus on the interactions of these components to evaluate how the data preprocessing translates into profit suboptimal price sets determined by the system.

## 3. The pricing decision support system

## 3.1. Data model

The unprocessed data collected by a retailer is usually transactional scanner data on a SKU level. The process of operationalising these data for the use in price optimization allows for vast amounts of discretion. Most research work already assumes availability of preprocessed data that has been cleaned and aggregated to brand, as well as to daily or weekly time buckets. We focus on a single category which will be the base for the retail customer purchase decision, simplifying our analysis by disregarding any intra-category effects. The term ‘category’ normally refers to a discrete group of similar, substitutable products, which compete for market share. How this group is defined in a modeling context is ultimately decided by the selection process in the data model, which is another, implicit form of pruning. For our analysis we include one set of available brands I and consider pruning or aggregating the data of a subset K of these brands so that K⊂I. Therefore, in the case of pruning, our analysis will consider only a reduced set I<sup>pr</sup> of i - k brands, effectively removing all brands not deemed of interest for the study, while in the case of aggregation, we include an aggregated brand $i ^ { a g }$ which combines all other brands not of immediate interest into one, so that the set I<sup>ag</sup> will consist of i - k + 1 brands.

## 3.2. Demand model

Various demand model formulations that are suitable for price optimization purposes exist in literature, as reviewed in Section 2. We chose a formulation similar to the work of [13] which explicitly separates market share from category sales in a 2-step demand model configuration and that allows us to observe and analyze the effects between the model components.

First, we model market share $\pi _ { t i }$ as the probability of selecting brand i in period t and in dependence of price $p _ { t i }$ as the only covariate where $\alpha _ { i }$ is the brand specific attraction parameter. We consider two alternative formulations: formulation S is the simple effects MNL formulation with a single price parameter for all brands $\beta ,$ while the ‘differential effects’ formulation $D$ features a brand specific parameter $\beta _ { i } .$ The error term ε follows a Gumbel distribution.

$$
S: \pi_ {t i} = \frac {\exp \left(\alpha_ {i} + \beta p _ {t i} + \varepsilon_ {t i}\right)}{\sum_ {j = 1} ^ {I} \exp \left(\alpha_ {j} + \beta p _ {t j} + \varepsilon_ {t j}\right)}\tag{1}
$$

$$
D: \pi_ {t i} = \frac {\exp (\alpha_ {i} + \beta_ {i} p _ {t i} + \varepsilon_ {t i})}{\sum_ {j = 1} ^ {I} \exp (\alpha_ {j} + \beta_ {j} p _ {t i} + \varepsilon_ {t j})}.\tag{2}
$$

Second, we model category demand as cumulated unit sales q in dependence of category price level $l _ { t \cdot }$ We consider three formulations that are frequently found in literature [15]: A: strictly linear, B: semi-log, and C: log–log. All include parameters γ and $\zeta$ and the normally distributed error term τ.

$$
A: q _ {t} = \gamma + \zeta l _ {t} + \tau_ {t}\tag{3}
$$

$$
B: \log (q _ {t}) = \gamma + \zeta l _ {t} + \tau_ {t}\tag{4}
$$

$$
C: \log (q _ {t}) = \gamma + \zeta \log (l _ {t}) + \tau_ {t}.\tag{5}
$$

Category price level l is modeled as the sum of prices $p _ { t i }$ of all brands i weighted by their observed market share $\pi _ { t i }$

$$
l _ {t} = \sum_ {i = 1} ^ {I} \pi_ {t i} p _ {t i}.\tag{6}
$$

The combination of the above allows for six distinct model configurations (AS, AD, BS, BD, CS, CD). For expositional purposes, most of our analysis will rely on the most simplistic combination AS, yet the alternative formulations will also be explored.

## 3.3. Decision model

The last component of the system is a representation of the optimal decision, building on the models defined above. We formulate an objective function to maximize profit of a given week g which is defined by the product of margin as a difference between price $p _ { t i }$ and brand specific cost $c _ { i } ,$ category unit sales $q _ { t } ,$ , and market share π .

$$
\max _ {p _ {t i}} g _ {t} = \sum_ {i = 1} ^ {I} (p _ {t i} - c _ {i}) q _ {t} \pi_ {t i}\tag{7}
$$

## 4. Research design

## 4.1. Empirical and simulated data

We propose a methodology that relies on simulated retail data that is modeled following an empirical example. It is based on the assumption that without the error terms, the data generating demand model is the true and unbiased representation of the actual demand generating process. In this section, we outline our approach: First we discuss the empirical data example and the generation of the artificial data that will serve as a basis for our analysis. We then apply the data preprocessing techniques in question (described in Section 4.2) and estimate the demand model given the resulting preprocessed data (outlined in Section 4.3). We determine optimized price sets based on these data (Section 4.4), and evaluate the gap in optimality to the truly optimal results as determined by the data generating model (discussed in Section 4.5).

To assure the empirical viability of our simulated data, we base the generation process on the salient features observed in a real world data set. As pointed out earlier, the initial motivation for this study was the various forms of data preprocessing of the well known Dominicks research data set that were seen in the literature examples presented in Section 1. These same data will serve as a point of reference for our study. The data in the examples is the refrigerated orange juice category, which is a subset of the refrigerated juice category — a comparatively small category with 228 individual SKUs, of which 82 are identifiable as orange juice. We use 100 weeks of these data. In line with common practice, we aggregate over all stores to 5 brands and base our analysis on price and cost per ounce.

We estimate the six demand model formulations described earlier given these empirical data, which then serve as input for data generation. The estimated demand model parameters under demand model configuration AS are $\pmb { \hat { \alpha } } = \left\{ 0 , 1 . 5 1 , 0 . 7 1 , - 1 . 9 2 , - 0 . 6 8 \right\} , \ \hat { \beta } = - 1 . 9 0$ $\hat { \boldsymbol { \gamma } } = 7 0 0 7 . 5 3 , \hat { \boldsymbol { \zeta } } = - 2 5 8 3 . 9 2$ . Prices p and cost c are described in <sup>¼ ¼</sup>Table 1. Further, we observe error terms $\tau { \sim } G ( 0 . 1 0 , 0 . 1 5 )$ , and $\varepsilon { \sim } N ( 0 , 7 1 5 )$ , as well as an empirical distribution of percentage price changes. These three components are the only stochastic influence on the system. We generate 1000 data sets, each containing 100 weeks of data for 5 brands. The large number of simulated data sets was chosen to ensure that all effects reported in this article are statistically significant.

Table 1 shows a comparison of the descriptive statistics of the empirical data observed (Obs), and the means of the simulated data ( <sup>-</sup>Sim) under demand model configuration AS. Further, the table also includes the optimized results that will be discussed in Section 4.4. The brands considered are identified by name in Table 1 but will only be referred to as brands 1 to 5 going forward.

We see that the features of the five brands are heterogeneous with a large variety in price, cost, market share and financial contribution. Brands 4 and 5 have the lowest market share: under 5%. Most importantly, we can see that the simulated data feature similar properties.

## 4.2. Data preprocessing

We formulate three different experimental conditions (EC1), (EC2), (EC3) that utilize different data preprocessing methods, as well as a null model (EC0). For each of these, and for every data set generated, a unique, preprocessed data set version is created.

(EC0) Null model: We define the null model as reference data set generated without any stochastic influence, using the unbiased, initial, data generating parameters $\pmb { \alpha } _ { 0 } , \ \beta _ { 0 } , \ \gamma _ { 0 } ,$ and $\zeta _ { 0 } .$ The null model will serve as a basis for comparison throughout the study.

(EC1) Base model: The base model will be estimated given the full data set as generated, including the full set of brands I without any preprocessing.

(EC2) Aggregation: We aggregate subset K to a virtual single brand i<sup>ag</sup>. The generated price history for the brands will be summarized accordingly and a mean price for the period, weighted by the market share of the brand realized in the current period $\tilde { \pi } _ { t i }$ will be created $( p _ { t } ^ { a g } = \sum _ { K } \tilde { \pi } _ { t i } p _ { t i } )$

(EC3) Pruning: The same subset of brands K is pruned. This means that in the generated data, the brands are removed without any replacement or adjustment.

For expositional purposes, brand subset K always comprises two brands. In line with common practice, these are the brands with the lowest market share: $i = 4 , 5 ,$ . For a more general argument, we also consider six different subsets of $I ; K _ { 1 } = \{ 4 , 5 \} , K _ { 2 } = \{ 3 , 4 \} , K _ { 3 } = \{ 3 , 5 \}$ $K _ { 4 } = \{ 2 , 4 \} , K _ { 5 } = \{ 2 , 5 \}$ , and $K _ { 6 } = \{ 2 , 3 \}$ . This will allow us to use the same data generated to explore the role of the properties of the data affected by preprocessing (i.e. the brands included in K).

## 4.3. Demand model estimation

The category and market share models are estimated for all data set versions created under the experimental conditions. The following likelihood function is used to estimate the market share model. Here $\pi _ { t i }$ is the market share as defined in Eqs. (1) and (2), and $\tilde { \pi } _ { t i }$ represents the market share realized for the specific brand and period.

$$
L = \prod_ {t = 1} ^ {1 0 0} \prod_ {i = 1} ^ {5} \pi_ {t i} ^ {\tilde {\pi} _ {t i}}.\tag{8}
$$

To maximize the likelihood, we select brand 1 as reference point and set $\hat { \alpha } _ { 1 } = 0$ so that with one less degree of freedom, the likelihood in <sup>¼</sup>Eq. (8) becomes determinate. The parameters of all three of the category model formulations can be estimated via ordinary least squares.

We assess fit and predictive quality of all six of the demand model configurations described earlier given the empirical data observed. Table 2 shows the $R ^ { 2 }$ of the category model, McFadden's Pseudo $R _ { P } ^ { 2 }$ of the market share model, as well as the root-mean-square error (RMSE) of the complete demand model.

Observed and simulated data-initial and optimized values.

<table><tr><td rowspan="2"> $i^a$ </td><td rowspan="2"></td><td colspan="2">Prices</td><td rowspan="2">Cost  $c_i$ </td><td colspan="2">Unit sales</td><td colspan="2">Market share</td><td colspan="2">Revenue</td><td colspan="2">Profit</td></tr><tr><td> $p_i$ </td><td> $p_i^o$ </td><td> $q_i$ </td><td> $q_i^o$ </td><td> $\pi_i$ </td><td> $\pi_i^o$ </td><td> $r_i$ </td><td> $r_i^o$ </td><td> $g_i$ </td><td> $g_i^o$ </td></tr><tr><td rowspan="2">1</td><td rowspan="2"> $\frac{Obs}{Sim}$ </td><td>1.55</td><td>1.66</td><td>1.04</td><td>816.42</td><td>571.56</td><td>0.34</td><td>0.35</td><td>1113.92</td><td>951.50</td><td>290.43</td><td>316.83</td></tr><tr><td>1.56</td><td>1.65</td><td>1.04</td><td>756.28</td><td>541.96</td><td>0.35</td><td>0.34</td><td>1054.26</td><td>892.13</td><td>266.59</td><td>327.67</td></tr><tr><td rowspan="2">2</td><td rowspan="2"> $\frac{Obs}{Sim}$ </td><td>2.31</td><td>2.40</td><td>1.69</td><td>838.05</td><td>643.22</td><td>0.38</td><td>0.39</td><td>1671.65</td><td>1543.30</td><td>333.30</td><td>417.16</td></tr><tr><td>2.32</td><td>2.36</td><td>1.69</td><td>807.52</td><td>647.57</td><td>0.38</td><td>0.40</td><td>1661.73</td><td>1520.06</td><td>299.12</td><td>427.34</td></tr><tr><td rowspan="2">3</td><td rowspan="2"> $\frac{Obs}{Sim}$ </td><td>2.23</td><td>2.44</td><td>1.61</td><td>515.03</td><td>270.52</td><td>0.22</td><td>0.17</td><td>905.62</td><td>659.08</td><td>129.15</td><td>216.38</td></tr><tr><td>2.24</td><td>2.28</td><td>1.61</td><td>465.50</td><td>338.58</td><td>0.22</td><td>0.21</td><td>898.86</td><td>768.23</td><td>148.56</td><td>222.51</td></tr><tr><td rowspan="2">4</td><td rowspan="2"> $\frac{Obs}{Sim}$ </td><td>2.23</td><td>1.94</td><td>1.42</td><td>70.90</td><td>50.25</td><td>0.03</td><td>0.03</td><td>125.22</td><td>97.27</td><td>32.14</td><td>23.90</td></tr><tr><td>2.25</td><td>2.18</td><td>1.42</td><td>36.10</td><td>29.29</td><td>0.02</td><td>0.02</td><td>67.99</td><td>63.60</td><td>16.75</td><td>22.02</td></tr><tr><td rowspan="2">5</td><td rowspan="2"> $\frac{Obs}{Sim}$ </td><td>2.51</td><td>2.23</td><td>1.67</td><td>64.73</td><td>99.90</td><td>0.03</td><td>0.06</td><td>138.87</td><td>222.53</td><td>30.54</td><td>60.86</td></tr><tr><td>2.53</td><td>2.45</td><td>1.67</td><td>79.65</td><td>61.27</td><td>0.04</td><td>0.04</td><td>164.35</td><td>149.28</td><td>31.12</td><td>46.81</td></tr><tr><td rowspan="2"> $\bar{x}$ </td><td rowspan="2"> $\frac{Obs}{Sim}$ </td><td>2.17</td><td>2.13</td><td>1.49</td><td>461.03</td><td>327.09</td><td>0.20</td><td>0.20</td><td>791.06</td><td>694.74</td><td>163.11</td><td>207.03</td></tr><tr><td>2.18</td><td>2.18</td><td>1.49</td><td>429.01</td><td>323.73</td><td>0.20</td><td>0.20</td><td>769.44</td><td>678.66</td><td>152.43</td><td>209.27</td></tr><tr><td rowspan="2"> $\sum$ </td><td rowspan="2"> $\frac{Obs}{Sim}$ </td><td>-</td><td>-</td><td>-</td><td>2305.13</td><td>1635.45</td><td>1.00</td><td>1.00</td><td>3955.28</td><td>3473.68</td><td>815.56</td><td>1035.14</td></tr><tr><td>-</td><td>-</td><td>-</td><td>2145.06</td><td>1618.67</td><td>1.00</td><td>1.00</td><td>3847.18</td><td>3393.29</td><td>762.14</td><td>1046.35</td></tr></table>

<sup>a</sup> 1: Dominicks 2: Tropicana 3: Minute Maid 4: Florida Gold and 5: Florida Natural.

Table 2  
Fit of category mode $\mathsf { A } ( R ^ { 2 } )$ and market share model S (R<sup>2</sup>); predictive quality of demand model (RMSE).

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Strictly linear</td><td colspan="2">Semi-log</td><td colspan="2">Log-log</td></tr><tr><td>AS</td><td>AD</td><td>AS</td><td>AD</td><td>AS</td><td>AD</td></tr><tr><td rowspan="3"> $R^2$ </td><td>(EC1)</td><td>0.553</td><td>0.553</td><td>0.577</td><td>0.577</td><td>0.550</td><td>0.550</td></tr><tr><td>(EC2)</td><td>0.553</td><td>0.553</td><td>0.577</td><td>0.577</td><td>0.550</td><td>0.550</td></tr><tr><td>(EC3)</td><td>0.515</td><td>0.515</td><td>0.535</td><td>0.535</td><td>0.509</td><td>0.509</td></tr><tr><td rowspan="3"> $R_P^2$ </td><td>(EC1)</td><td>0.324</td><td>0.339</td><td>0.324</td><td>0.339</td><td>0.324</td><td>0.339</td></tr><tr><td>(EC2)</td><td>0.271</td><td>0.272</td><td>0.271</td><td>0.272</td><td>0.271</td><td>0.272</td></tr><tr><td>(EC3)</td><td>0.212</td><td>0.214</td><td>0.212</td><td>0.214</td><td>0.212</td><td>0.214</td></tr><tr><td rowspan="3">RMSE</td><td>(EC1)</td><td>491.5</td><td>456.6</td><td>516.6</td><td>459.2</td><td>550.5</td><td>460.9</td></tr><tr><td>(EC2)</td><td>497.6</td><td>502.3</td><td>499.4</td><td>505.2</td><td>500.7</td><td>507.2</td></tr><tr><td>(EC3)</td><td>560.4</td><td>565.2</td><td>562.0</td><td>568.1</td><td>562.8</td><td>569.8</td></tr></table>

We see that overall, with $R ^ { 2 }$ values of more than 0.55 and R<sup>2</sup> of over 0.32 under (EC1), all model configurations show an acceptable fit. As it could be expected, across all configurations, the fit decreases when aggregation or pruning is applied, with the exception of the aggregation of the category model, which is identical with the untreated scenario. Further, the consideration of differential effects clearly improves model fit. On the other hand, the error measures that assess the predictive quality of the entire system show mixed results. However, by all measures, the formulations based on the log–log category model seem to be inferior to their strictly linear and semi-log counterparts.

## 4.4. Price optimization

We formulate a nonlinear optimization program based on the decision model presented in Eq. (7) to determine a static set of prices that will maximize profit $g \mathrm { : }$

$$
\max _ {p _ {i}} g = \sum_ {i = 1} ^ {5} (p _ {i} - c _ {i}) q \pi_ {i}
$$

$$
s. t. p _ {i} \geq c _ {i} \forall i\tag{9}
$$

$$
l \geq - \frac {\hat {\gamma}}{\hat {\zeta}}
$$

$$
l = \sum_ {1 = 1} ^ {5} \tilde {\pi} _ {1 0 0 i} p _ {i}.
$$

The first constraint of the program averts pricing below cost while the second constraint restricts the category model to non-negative category unit sales. While market share $\pi _ { i }$ is a variable in the objective function, the third constraint adjusts the calculation of the category price level l by determining market share as a constant as the last observed market share $\tilde { \pi } _ { 1 0 0 }$ . If the market share was variable, a price decrease for brand i would directly consume market share of all remaining brands j, implying that the optimal pricing policy means a price increase of all brands j to a point where their respective market share $\pi _ { j }$ approaches 0. The remaining brand i would determine l and consequently also category unit sales $q .$ This could be reduced to a simple quadratic optimization problem with the optimal policy, requiring setting the price of one brand to $\begin{array} { r } { p _ { i } ^ { 0 } = 0 . 5 \left( c _ { i } - \frac { \hat { \gamma } } { \hat { \zeta } } \right) } \end{array}$ while raising the prices of the remaining brands $p _ { j \neq i } {  } \operatorname { i n f } .$ This unrealistic case can be prevented by either restricting the maximum price change (Δp ), by formulating a more reasonable functional form for $l = \sum \pi _ { i } p _ { i }$ , or by limiting the vari ability of $\pi _ { i \cdot }$ <sup>¼</sup>As the underlying idea of the category price level is to represent general customer interest in the category, it seems appropriate from a structural perspective to assume that the market share most recently observed (constant $\tilde { \pi } _ { 1 0 0 i } )$ is used as weight when determining category price level l.

Table 1 includes the optimal prices and the financial contributions for the empirically observed as well as for the generated data as determined by the program described in formula (9). We see that for the real data case, the program suggests three price increases and two price decreases with a mean absolute price change of 19.85%. This yields an increase in profit of 26.92% while decreasing unit sales and market share. Overall, the simulated data produce comparable results.

## 4.5. Evaluation of system performance

Solving the program will yield an optimized price set for each condition. However, only the set determined in the absence of any stochasticity (i.e. null model EC0) will be truly optimal. Since the data generating parameters and hence the optimal profit and data set are known, we can evaluate how these optimized price sets will fare given the data generating model. Throughout the study, we determine profit suboptimality for conditions (EC1), (EC2), and (EC3) as the mean percentage error (MPE) between the profit yielded by the optimized price sets and the truly optimal profit as determined by (EC0).

However, while under (EC1), a full set of 5 price points is produced, whereas (EC2) only yields 4 price points – one of which is the artificial choice representing the aggregate $i ^ { a g } -$ and under (EC3), since two brands were subject to pruning, a set of only 3 price points is created. To find a base for comparison, we use price $p _ { i ^ { a g } }$ for both of the previously aggregated brands in set K and assume the original, unchanged price $p _ { 0 }$ for the brands pruned under (EC3). Throughout the better part of our study, this approach will provide a useful base for assessing the underlying mechanics of the system. However, it will be of limited use for determining the financial impact of the processing methods. In Section 5.4 we will therefore explore alternative approaches. Foremost, we would like to assess the best-case scenario of what is the most profitable situation that can still be achieved, given the prices already determined under the experimental conditions. To achieve this, we evaluate a second scenario in which we disregard the optimal price determined for the aggregated product in (EC2) $p _ { a g } ^ { o }$ as well as the optimal prices for $p _ { 4 } ^ { o } , p _ { 5 } ^ { o }$ for the base model (EC1). We then re-optimize given the data generating parameters of the null model $\gamma _ { 0 } ,$ , ζ , $\alpha _ { 0 i }$ , and $\beta _ { 0 } ,$ and the remaining optimal prices $p _ { 1 } ^ { o } ,$ $p _ { 2 } ^ { o } ,$ and $p _ { 3 } ^ { o }$ of each experimental condition. This leads us to a modified program as formulated in Eq. (10), which yields optimized prices for all 5 brands that are comparable as a best case scenario across all experimental conditions.

$$
\max _ {\{p _ {4}, p _ {5} \}} g = \sum_ {i = 1} ^ {5} (p _ {i} - c _ {i}) q \pi_ {i}\tag{10}
$$

$$
s. t. \quad p _ {i} \geq c _ {i} \quad \forall \quad i
$$

$$
l \geq - \frac {\gamma_ {0}}{\zeta_ {0}}
$$

$$
l = \sum_ {i = 1} ^ {5} \tilde {\pi} _ {1 0 0 _ {i}} p _ {i}
$$

$$
p _ {i} = p _ {i} ^ {0} \quad \forall \quad i = \{1, 2, 3 \}
$$

$$
\pi_ {i} = \pi_ {i} (\alpha_ {0 i}, \beta_ {0}).
$$

## 5. Results

5.1. General system mechanics

## 5.1.1. Demand model estimation

In a first step, we illustrate the general mechanics of the system, fo cusing on model configuration AS with linear category model $( 3 )$ , and simple effect market share model (1). Further, we eliminate errors τ and ε from the model so the only stochasticity included in our simulation at this point originates out of the draws from the empirically observed distribution of percentage price changes. Our estimation routines can therefore be expected to recuperate the data generating parameter values originally gained from our real data estimation as described by null model (EC0).

Estimated demand model parameters and elasticities.

<table><tr><td rowspan="2">Exp.</td><td colspan="3">Category model (A)</td><td colspan="4">Market share model (S)</td><td rowspan="2"> $E_{Tot}^{a}$ </td></tr><tr><td> $\hat{\gamma}$ </td><td> $\hat{\zeta}$ </td><td> $E_{Cat}$ </td><td> $\hat{\alpha}_{2}$ </td><td> $\hat{\alpha}_{3}$ </td><td> $\hat{\beta}$ </td><td> $QE_{MS}^{a}$ </td></tr><tr><td>(EC0)</td><td>7007.53</td><td>-2583.92</td><td>2.94</td><td>1.51</td><td>0.72</td><td>-1.90</td><td>2.64</td><td>3.57</td></tr><tr><td>(EC1)</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>-0.00%</td><td>-0.00%</td><td>-0.00%</td><td>-0.00%</td><td>-0.00%</td></tr><tr><td>(EC2)</td><td>-0.00%</td><td>0.00%</td><td>0.00%</td><td>-1.51%</td><td>-2.47%</td><td>-1.58%</td><td>-1.52%</td><td>-1.22%</td></tr><tr><td>(EC3)</td><td>-3.58%</td><td>-2.60%</td><td>1.00%</td><td>-0.00%</td><td>-0.00%</td><td>-0.00%</td><td>-0.00%</td><td>-1.05%</td></tr></table>

<sup>a</sup> for i={1,2,3}

Table 3 shows the estimation results in terms of absolute values for the null model (EC0), and profit suboptimality MPE for experimental conditions (EC1), (EC2), and (EC3). Since $\alpha _ { 0 1 } = \hat { \alpha } = 0$ , and $\hat { \alpha } _ { 4 } , \hat { \alpha } _ { 5 }$ are not determined for (EC2) and (EC3), we only report results for $\hat { \alpha } _ { 2 } , \hat { \alpha } _ { 3 }$ and ${ \hat { \beta } } .$ We also determine the (quasi-) elasticities of model components $E _ { C a t } , Q E _ { M S }$ evaluated at their most recent price point $\left( l _ { 0 } , \pmb { \mathrm { p } } _ { 0 } \right)$ as well as a combined elasticity $E _ { T o t } .$

This simplistic observation documents one of the fundamental differences of the data treatment conditions affecting the price optimization system: The estimation under aggregation (EC2) yields unbiased estimators for the category model but biased estimates for the market share model, while pruning (EC3) retrieves unbiased parameters for the market share model but biased estimates for the category model. The direct consequences for the price elasticities are visible. The unprocessed scenario (EC1) retrieves entirely unbiased estimates. However, there are two important caveats to these observations: Firstly, they are conditional on the absence of demand model errors τ and ε. Further, in the case of the market share model, even though the parameter estimates are numerically identical, the results produced by the demand model are always dependent on the number of brands considered due to the model's independence of irrelevant alternatives (IIA) property.

## 5.1.2. Price optimization

As a consequence of the estimation results presented above, the optimal price sets determined under the treatment conditions (EC2) and (EC3) yield suboptimal results as shown in Table 4:

In this example, brands 1 to 3 are slightly overpriced under the aggregation condition (EC2) and underpriced under the pruning condition (EC3). This results in a profit suboptimality $( g ^ { o } )$ of −0.32% and −0.10% respectively.

At this stage, the difference is marginal. Further, a significant source for the profit suboptimality is the policy of disaggregating the common price for the aggregated product under (EC2) for brands 4 and $5 \ : ( p _ { 4 } ^ { o } =$ $p _ { 5 } ^ { o } { = } 2 . 2 8 )$ , and keeping the original prices under (EC3) $( p _ { 4 } ^ { o } = 2 . 2 3 ,$ $p _ { 5 } ^ { o } { = } 2 . 5 1 )$ ). While the size of estimation bias will increase as we evaluate more realistic conditions going forward, we also want to evaluate the financial consequences from different perspectives in Section 5.4.

Truly optimal (absolute) and optimized (MPE) prices and profit.

<table><tr><td>Exp.</td><td> $p_{1}^{0}$ </td><td> $p_{2}^{0}$ </td><td> $p_{3}^{0}$ </td><td> $p_{4}^{0}$ </td><td> $p_{5}^{0}$ </td><td> $\overline{p^{0}}$ </td><td> $g^{0}$ </td></tr><tr><td>(EC0)</td><td>1.64</td><td>2.34</td><td>2.26</td><td>2.16</td><td>2.43</td><td>2.17</td><td>1058.27</td></tr><tr><td>(EC1)</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td></tr><tr><td>(EC2)</td><td>0.10%</td><td>0.07%</td><td>0.10%</td><td>5.37%</td><td>-6.10%</td><td>-0.09%</td><td>-0.32%</td></tr><tr><td>(EC3)</td><td>-0.23%</td><td>-0.18%</td><td>-0.18%</td><td>3.22%</td><td>3.45%</td><td>1.21%</td><td>-0.10%</td></tr></table>

## 5.1.3. Sources for bias

To highlight the main source of estimation bias, we want to extend our observation by considering the alternative brand subsets for pruning and aggregation as described in Section 4.2. Fig. 1 shows the estimation results of price parameters $\hat { \zeta }$ and ${ \hat { \beta } } .$ In this and all following figures, we use color-code to identify the experimental conditions as follows: blue (EC1), red: (EC2), and green: (EC3).

The six brand subsets K considered are ordered by their cumulated market share. While the deviation from the (absolute) mean is of little meaning in the pruning scenario (EC3) as it is a mere numeric consequence of reduced total sales, it is indicative for the source of bias: The variance increases with total market share pruned. For the market share model on the other hand, the deviation from the mean is indicative for decreased accuracy. However, the reason for the bias is less transparent as many factors contribute such as the heterogeneity of the brands aggregated.

(a)  
![](/api/attachments/9JWCKP49/fulltext/images/e781c48f57d8c282edcf75064c23eea9555182d728c8e804ec624faabee65ffa.jpg)

(b)  
![](/api/attachments/9JWCKP49/fulltext/images/8e2ae5eb915e7861d5c74b94340aa0b5e04b5c02bf05f747f72143c1d99a00e7.jpg)  
Fig. 1. Parameter estimates for ζ̂ (a) and β̂ (b) for the six brand subsets K.

## 5.2. Model properties

## 5.2.1. Demand model error

Up until this point, the only stochastic influence considered was the simulated price history drawn from the empirical distribution of percentage price changes observed. For a more realistic assessment, we now include the two demand model error terms $\tau { \sim } N ( \mu _ { \tau } , \sigma _ { \tau } ^ { 2 } )$ , and $\varepsilon { \sim } G ( \mu _ { \varepsilon } , S _ { \varepsilon } )$ . We first consider the optimisation results of the simulated data given the level of error observed in the empirical data as well as setting the scale parameters of the distributions $\sigma _ { \tau } ^ { 2 } ,$ and $\varsigma _ { \varepsilon }$ to 0. Table 5 shows the optimized prices and resulting profit for all five brands as well as profit for three experimental error levels.

We see that the suboptimality of the results increases as the errors are introduced. All preprocessing methods on average overprice in comparison to the optimal solution. The financial performance of (EC1) and (EC3) seems to be identical in this case. The policy of keeping the original price for brands 4 and 5 under pruning can lead to arbitrarily superior profit results, as it is illustrated in this example.

The size of the error clearly seems to have a large influence on the degree of suboptimality. We therefore assess the optimal results under varying error levels. From the empirical data, we observed error terms of $\varepsilon { \sim } N ( 0 , 7 1 5 ) , \tau { \sim } G ( 0 . 1 0 , 0 . 1 5 )$ . We now vary the scale parameters between 0 and double the value observed so that the maximum error is $\varepsilon { \sim } N ( 0 , 1 4 3 0 )$ , τ\~G(0.10, 0.30). Fig. 2 shows the resulting suboptimality for four of the six brand sets K with the black line indicating the observed error terms.

As seen earlier, in the absence of error, the scale of difference in estimation bias (Table 3), and consequently in suboptimality (Table 4) between the experimental conditions is marginal and close to the optimal solution. Along both error dimensions, absolute suboptimality, as well as the difference in performance between the experimental conditions, grow considerably. (EC1) consistently produces better results than aggregation (EC2), up to a suboptimality of −6.2% (EC1), and −9.0% (EC2) for the maximum error combination assessed. The results under (EC3), however, seem to become less dependent on the level of error, the larger the market share of the brands pruned. We see that with the error level observed in the empirical data, pruning produces results comparable to the untreated scenario (EC1).

## 5.2.2. Model configuration

For expositional purposes we have been focusing on a simple model configuration with a strictly linear category model and a simple effects market share model. We have already assessed the fit of other model configurations to the empirical data in Table 2 where the log model proved to be the least suited. However, we also saw that the predictive quality of the system varied greatly with the demand model configuration selected. Fig. 3 and Table 6 show profit suboptimality for the experimental conditions and for the alternative configurations as introduced in Section 3.2.

We see that the formulation of the category model is the decisive factor for the level of suboptimality: The log model significantly underperforms under all treatment conditions, while the systems based on the linear and semi-log category model perform comparably. The latter appears to be the superior choice with a mean suboptimality of −0.87% under (EC1).

## 5.3. Data features

## 5.3.1. Price elasticity

Results thus far have indicated that the actual selection of data pruned and aggregated heavily influences the performance of the data processing methods. This warrants a closer look at the features of the data treated. Our simulated data has been modeled according to the parameters observed in the empirical data. We now want to vary the parameters of the data generation process in order to explore the relevance of specific data properties.

We first focus on price elasticity. The observed scenario was elastic as shown in Table 3. We now explore an inelastic scenario by setting data generating category model parameter $\zeta _ { 0 ^ { ' } } = - 1 5 0 0$ (observed: −2584) and $\beta _ { 0 ^ { \prime } } = - 0 . 3 ( \mathrm { o b s e r v e d } ; - 1 . 9 0 )$ which will yield inelasticity at current price points. Fig. 4 shows the results in terms of suboptimality for the initial scenario $K _ { 1 }$ as well as the mean across all six brand subsets K.

Naturally, under the inelastic scenarios larger price changes and extreme price points become more profitable. Overall suboptimality and variance of the solutions is increasing. The results of the pruning condition (EC3) are strongly affected, foremost by the inelasticity of the category model.

## 5.3.2. Price changes

The data generation routine samples from the empirical distribution of percentage price changes observed. We now assess how the distribution of price changes affects the optimality of the system. We therefore replace the empirical distribution with a normal distribution. The best fit can be achieved by $\Delta \mathbf { p } ( \% ) { \sim } N ( 0 . 0 0 6 , 0 . 1 7 5 )$ . For expositional purposes we assume $\mu { = } 0$ and evaluate values for $\sigma$ that are between 5% (=0.0087) and 150% (=0.2622) of its observed value 0.175. Fig. 5 (a) shows a histogram of the empirical distribution, the normal distribution with the best fit (red) as well as the distributions evaluated in the experiment (black). (b) shows the suboptimality for all three experimental conditions (below), as well as demand model fit $R ^ { 2 }$ and $R _ { P } ^ { 2 }$ (above) given the experimental values for σ. The black dotted line indicates the level of σ empirically observed.

Any increase in σ strengthens the estimation quality of market share and category model that directly improves the optimality of the results. While the gap between the treatment methods for the lower values of σ is quite significant, it quickly approaches 0 asymptotically. As previously noted, the suboptimality at the empirically observed level of σ is −1.3% (EC1 and EC3), and−1.7% (EC2). Similar results were obtained assuming a uniform or a logistic distribution.

Optimal and optimized results given observed and experimental error levels

<table><tr><td></td><td colspan="7">Observed error level</td><td colspan="3">Experimental error levels</td></tr><tr><td> $\sigma_{\tau}^{a}$ </td><td colspan="7">715</td><td>0</td><td>715</td><td>0</td></tr><tr><td> $S_{\varepsilon}^{b}$ </td><td colspan="7">0.15</td><td>0.15</td><td>0</td><td>0</td></tr><tr><td>Exp.</td><td> $p_{1}^{0}$ </td><td> $p_{2}^{0}$ </td><td> $p_{3}^{0}$ </td><td> $p_{4}^{0}$ </td><td> $p_{5}^{0}$ </td><td> $\overline{p^{0}}$ </td><td> $g^{0}$ </td><td> $g^{0}$ </td><td> $g^{0}$ </td><td> $g^{0}$ </td></tr><tr><td>(ECO)</td><td>1.64</td><td>2.34</td><td>2.26</td><td>2.16</td><td>2.43</td><td>2.17</td><td>1058.27</td><td>1058.27</td><td>1058.27</td><td>1058.27</td></tr><tr><td>(EC1)</td><td>0.68%</td><td>0.61%</td><td>0.69%</td><td>0.78%</td><td>0.72%</td><td>0.70%</td><td>-1.13%</td><td>-0.54%</td><td>-0.57%</td><td>0.00%</td></tr><tr><td>(EC2)</td><td>1.35%</td><td>1.07%</td><td>1.20%</td><td>6.54%</td><td>-5.07%</td><td>1.02%</td><td>-1.53%</td><td>-0.88%</td><td>-0.88%</td><td>-0.32%</td></tr><tr><td>(EC3)</td><td>0.93%</td><td>0.77%</td><td>0.86%</td><td>3.22%</td><td>3.45%</td><td>1.84%</td><td>-1.13%</td><td>-0.61%</td><td>-0.54%</td><td>-0.10%</td></tr></table>

<sup>a</sup> τ\~N(0,σ <sup>2</sup>),  
<sup>b</sup> ε\~G(0.10,ς<sub>ε</sub>).

![](/api/attachments/9JWCKP49/fulltext/images/4e46d2f4df2cc59435a95b440dd971342bbc60469020566cd16cd876f6a28066.jpg)

![](/api/attachments/9JWCKP49/fulltext/images/d54d0c1295dc5c65771dced1c4d74761570562f0a1b5ed6a60f0fdffd85a6692.jpg)

(c)  
![](/api/attachments/9JWCKP49/fulltext/images/1a8ca8837880576e922bfcc8140692c6685108795102af60cb37932dd3f4512d.jpg)

![](/api/attachments/9JWCKP49/fulltext/images/fa2fe44b285df990cce64281366203dd5844d67af44a52c5c6f91e12df5d2341.jpg)  
στ  
Fig. 2. Profit suboptimality (MPE) given brand subsets K : (a), K : (b), K : (c), and K : (d). Blue: (EC1) Red: (EC2) Green: (EC3) Black: Error level observed.

![](/api/attachments/9JWCKP49/fulltext/images/c96e4de0c82dd0d76475034e12bce2c39346c5afa735ad6432f821986281bf02.jpg)  
Fig. 3. Profit suboptimality (MPE).

## 5.3.3. Brand heterogeneity

We have already explored the dependence between estimation bias and the underlying data properties of the data treated. This has indicated that the level of heterogeneity of the two brands in K affects the optimality of the price set produced. For more detailed insights, we introduce brand heterogeneity in an experimental set up that deviates from the original data scenario: we replace both brands in K with a brand that is generated using the mean of the data generating parameters of all five brands in I. We then vary the parameter in question of one of the brands in K. Fig. 6 shows the profit suboptimality observed when introducing heterogeneity for cost c, price p and simple effects market share model price parameter $\beta$ for all six sets K.

Table 6 Profit suboptimality (MPE)

<table><tr><td rowspan="2"></td><td colspan="2">Strictly linear</td><td colspan="2">Semi-log</td><td colspan="2">Log-log</td></tr><tr><td>AS</td><td>AD</td><td>BS</td><td>BD</td><td>CS</td><td>CD</td></tr><tr><td>(EC1)</td><td>-1.13</td><td>-1.10</td><td>-0.87</td><td>-0.88</td><td>-1.76</td><td>-7.50</td></tr><tr><td>(EC2)</td><td>-1.53</td><td>-1.42</td><td>-1.16</td><td>-0.98</td><td>-2.11</td><td>-10.44</td></tr><tr><td>(EC3)</td><td>-1.13</td><td>-0.91</td><td>-1.16</td><td>-1.53</td><td>-15.40</td><td>-27.60</td></tr></table>

(a)  
![](/api/attachments/9JWCKP49/fulltext/images/eebf5f22403810965613dd8cd615d97962627d1a523316d3cc6022673e565f25.jpg)

(b)  
![](/api/attachments/9JWCKP49/fulltext/images/999f141c51a716728fdb5681097ce581ee242693c47da185abcb2aae50da5cfc.jpg)  
Fig. 4. Profit suboptimality (MPE) under 4 elasticity scenarios: K<sub>1</sub>: (a) and K: (b).

For cost and price, (EC1) and (EC2) perform comparably for the homogenous case $( \mathrm { i . e . } \Delta ( x _ { 5 } ) = 0 \% )$ . As heterogeneity increases, aggregation performs increasingly worse. The effect is amplified by increasing market share of the aggregated brands in K. (EC3) is also influenced by the level of heterogeneity yet to a lesser extent with the general level of suboptimality increasing as pruned market share increases. Heterogeneity of the pricing parameter only has a marginal effect on the gap between (EC1) and (EC2).

## 5.4. Financial perspective

So far we have looked at the causes and the degree of suboptimality incurred by the treatment scenarios. However, in Table 5 we have already seen that even though an estimation bias might exist, it is only partially reflected by the financial results produced. This is largely due to our approach of determining prices for the treated brands under (EC2) and (EC3). The policy used of disaggregating under (EC2) and retaining original prices under (EC3) seems to be the approach that is empirically most viable. However, this can be arbitrarily favorable depending on the data scenario and therefore warrants a more thorough investigation of the financial impact observed. As discussed in Section 4.5, we use a reformulated program as stated in formula (10) to determine profit in the manner of a best case scenario. Fig. 7 shows absolute values for estimated price parameters $\hat { \zeta }$ and $\hat { \beta }$ , as well as suboptimality (MPE) of optimal profi $: g ^ { o }$ , and re-optimized profi $\cdot g ^ { r }$ for all six sets K.

(a)  
![](/api/attachments/9JWCKP49/fulltext/images/40663c8c4834b7383cd92a530e301b679a35281ef85e9784462f1f63c6dbda38.jpg)

(b)  
![](/api/attachments/9JWCKP49/fulltext/images/0fd49d28185715ecf04036bd69bd62a32feded7ac0b115fc334f6623c516dbe7.jpg)  
Fig. 5. (a) Observed (histogram), fitted (red), and experimental (black) distributions of percentage price changes; (b) model fit R<sup>2</sup>, R<sub>P</sub><sup>2</sup>, and profit suboptimality of processing conditions given distribution parameter of price changes σ.

The price coefficients on the left document the bias introduced by the preprocessing methods for the different market share scenarios. Further, the optimal results $g ^ { o }$ illustrate the inconsistent performance of the pruning condition, occasionally even outperforming the untreated scenario under (EC1). The re-optimization results $g ^ { r }$ on the other hand show how the performance of (EC3) decreases with an increase in market share pruned. Aggregation, however, produces results that are consistently very close to those of (EC1). This underlines the roles of the two demand model components: While any estimation bias in the category model will translate into less profitable price sets, the main consequence of any bias in the market

Profit suboptimality (MPE)

![](/api/attachments/9JWCKP49/fulltext/images/dc35b66fa6593722c83a742edb7f51db78d08f892c68a1c85404153c06baae16.jpg)  
Fig. 6. Profit suboptimality under heterogeneity of data generating parameters

share model will be a set of prices that suboptimally redistributes market share and affects overall assortment profitability to a lesser extent.

We want to elaborate on the above by exploring the results under additional alternative pricing scenarios for all six brand subsets K. Beyond what has been determined as optimized results $g ^ { o }$ and re-optimized results $g ^ { r } ,$ Table 7 includes results $\dot { g }$ where prices in K are being determined as original price $p _ { 0 i }$ , andg€, where the mean percentage price markup as determined in the optimized results is applied to the original price p<sub>0 i</sub>.

![](/api/attachments/9JWCKP49/fulltext/images/32c94a04ddc99d01657242722fc4e18895bb53340be1c293bfc10243970f1f47.jpg)  
Fig. 7. Bias of demand model price parameters ${ \hat { \zeta } } , { \hat { \beta } } ,$ and profit suboptimality of optimized and re-optimized solutions $g ^ { o } , g ^ { r }$ for all six brand subsets K.

Comparing the means of the experimental conditions, we can see that with the exception of our conventional policy used, aggregation produces superior results over pruning. For our best case scenario, the mean profit suboptimality across the brand subsets is − 0.69% for (EC1), −0.82% for (EC2), and −1.03% for (EC3), which appears to be a useful indication for aggregation outperforming pruning in terms of producing the more reliable and the more profitable price sets. However, when market share is small, pruning still appears to be favorable.

Even though our methodology is not laid out for the purpose, we want to conclude by providing an absolute empirical perspective on these suboptimalities by framing the results given the empirical data used: At the outset, we experienced a very small bias as described in Section 5.1 that was amplified when real data conditions were considered. Now, we see that even in the best case scenario, the suboptimality to the truly optimal solution is −0.34%, but when treating the brands with the smallest market share, as is common practice, suboptimalities of more than −1% are produced regardless of the data processing techniques used. The largest mean difference between the best and the worst condition is −0.74%.

## 6. Conclusion

The analysis shows that pruning and aggregation can introduce bias into the demand model estimates that will translate into significant suboptimalities within the price optimization system. We have seen that size and effect of these suboptimalities are largely dependent on model and data properties. We demonstrated in Section 5.1 that (in isolation) aggregation assures the consistency of the choice model since it merely redistributes market share, while pruning is favorable for the performance of the category model which directly affects absolute profit levels. However, as seen in Section 5.2, whether a data preprocessing technique is appropriate or introduces a strong bias for the system is dependent on multiple influences; foremost on model fit, and the quality of estimation. The data properties, such as elasticities play an important role in the optimality of the solution as well but here, aggregation produces more consistent results across all scenarios as seen in Section 5.3.3. The results show that any improvement in estimation accuracy is well worthwhile and drastically increases the performance of the system.

Even though we only assess two specific types of data preprocessing, pruning and aggregation, these offer considerable generality, including many other forms of data treatment which result in, or are equivalent to, either pruning or aggregation. However, in terms of a normative recommendation on how data should be processed, our methodology has limited potential for generalization. Nonetheless it can serve as guidance and a first step towards a unified data preprocessing standard for retail data for researchers and practitioners alike. We derive the following four recommendations as a general guidance: (1) Since the main driver for these techniques is usually insufficient data availability, or challenging data properties such as lack of price changes, sparse data or intermittent demand, we want to emphasize that preprocessing is often a necessity. However, most scientific papers over-simplify even though robust estimates could be obtained for higher levels of aggregation or with less pruning, which generally seems to be beneficial. (2) However, preprocessed data is likely to deliver superior results for the entire system (including any pruned and aggregated products) if a better model fit can be achieved. Therefore, much like the common practice of selecting among different model configurations, it also pays to explore different levels of preprocessing. (3) When aggregating data, it should be assured that the products are actually comparable as it is common practice to aggregate items only because they share a feature such as brand name or size. (4) When pruning or aggregating is deemed to be worthwhile, it seems to be a promising general strategy to prune product groups with larger market shares while aggregating groups with smaller market shares.

Furthermore, it is important to emphasize that many data treatment techniques of operationalising transactional retail data induce decisions equivalent to pruning and aggregation that are less apparent. For instance, the orange juice data that was the subject of our analysis was only a subset of the refrigerated juice category, and also ignored other categories of bottled juices, frozen juices and soft drinks, which were all implicitly ‘pruned’ before the start of any data preprocessing activity. Therefore, the effect of pruning may be further enhanced by the category-structure and the product-hierachy a retailer has in place. In a similar way, the attribute information available in empirical datasets is often incomplete and hence, data points are aggregated simply because they cannot be distinguished.

Since the intersection between data modeling and price optimization leaves much left to be explored, numerous avenues for future research emerge. The simplicity of our system lends itself to an extension with more complex formulations and consideration of influences such as promotions or seasonality. For expositional purposes, this study has focused on an example with five brands. An extension could consider a larger number of products and evaluate the effect of jointly aggregating and pruning any subsets of these. Further, our study concentrates on profit maximization while retailers typically consider competing objectives. Studying the problem in a multiobjective optimization context seems promising. Since data preprocessing clearly affects the suboptimality of such a system, we need to address questions around how we can operationalise and amend existing models without having to simplify data through pruning or aggregation. Given the research available on the behavioral aspects of choice set selection, it would be desirable to consolidate these findings with the approach taken here and develop directives that in the future might lead to data modeling standards for retail data. In the light of the current state of retail pricing research and the pricing techniques currently deployed in retail practice, any research that helps to bring data modeling and price optimization closer together should be encouraged as it promises substantial impact for both research and practice.

Suboptimality under alternative pricing scenarios for all six brand subsets K.

<table><tr><td rowspan="2">K</td><td colspan="3"> $g^0$ </td><td colspan="3"> $g^r$ </td><td colspan="3"> $\dot{g}$ </td><td colspan="3"> $\ddot{g}$ </td></tr><tr><td>(EC1)</td><td>(EC2)</td><td>(EC3)</td><td>(EC1)</td><td>(EC2)</td><td>(EC3)</td><td>(EC1)</td><td>(EC2)</td><td>(EC3)</td><td>(EC1)</td><td>(EC2)</td><td>(EC3)</td></tr><tr><td>1</td><td>-1.13</td><td>-1.53</td><td>-1.13</td><td>-1.07</td><td>-1.21</td><td>-1.04</td><td>-1.15</td><td>-1.29</td><td>-1.13</td><td>-1.43</td><td>-1.63</td><td>-1.42</td></tr><tr><td>2</td><td>-1.11</td><td>-1.28</td><td>-0.82</td><td>-0.80</td><td>-0.93</td><td>-0.73</td><td>-0.91</td><td>-1.04</td><td>-0.82</td><td>-1.00</td><td>-1.18</td><td>-0.90</td></tr><tr><td>3</td><td>-1.10</td><td>-1.52</td><td>-0.87</td><td>-0.78</td><td>-0.92</td><td>-0.73</td><td>-0.93</td><td>-1.08</td><td>-0.87</td><td>-1.11</td><td>-1.33</td><td>-0.98</td></tr><tr><td>4</td><td>-1.12</td><td>-1.37</td><td>-1.21</td><td>-0.59</td><td>-0.70</td><td>-1.11</td><td>-0.73</td><td>-0.85</td><td>-1.21</td><td>-0.97</td><td>-1.18</td><td>-1.81</td></tr><tr><td>5</td><td>-1.11</td><td>-1.34</td><td>-1.35</td><td>-0.57</td><td>-0.69</td><td>-1.20</td><td>-0.75</td><td>-0.88</td><td>-1.35</td><td>-1.10</td><td>-1.38</td><td>-2.05</td></tr><tr><td>6</td><td>-1.12</td><td>-1.32</td><td>-1.45</td><td>-0.34</td><td>-0.48</td><td>-1.36</td><td>-0.52</td><td>-0.68</td><td>-1.45</td><td>-0.91</td><td>-1.01</td><td>-4.96</td></tr><tr><td> $\bar{x}$ </td><td>-1.12</td><td>-1.39</td><td>-1.13</td><td>-0.69</td><td>-0.82</td><td>-1.03</td><td>-0.83</td><td>-0.97</td><td>-1.13</td><td>-1.09</td><td>-1.28</td><td>-2.02</td></tr></table>

All data used in this paper is openly available to other researchers. The subset of the Dominicks database is available from the Kilts Centre for Marketing [14]. The synthetic data can be generated using the parameters stated in this paper.

## References

[1] C. Abramson, R.L. Andrews, I.S. Currim, M. Jones, Parameter bias from unobserved effects in the multinomial logit model of consumer choice, Journal of Marketing Research 37 (4) (2000) 410–426.

[2] Anderson, E, Vilcassim, N. J, 2001. Structural demand models for retailer category pricing. London Business School Mimeo.

[3] R.L. Andrews, I.S. Currim, An experimental investigation of scanner data preparation strategies for consumer choice models, International Journal of Research in Market ing 22 (3) (Sep. 2005) 319–331.

[4] G.R. Bitran, R. Caldentey, An overview of pricing models for revenue management, Manufacturing & Service Operations Management 5 (3) (2003) 203–229.

[5] R.N. Bolton, The robustness of retail-level price elasticity estimates, Journal of Retailing 65 (2) (1989) 193–219.

[6] R.A. Briesch, W.R. Dillon, R.C. Blattberg, Treating zero brand sales observations in choice model estimation: consequences and potential remedies, Journal of Market ing Research 45 (5) (Oct. 2008) 618–632.

[7] Y. Chen, S. Yang, Estimating disaggregate models using aggregate data through augmentation of individual choice, Journal of Marketing Research 44 (November) (2007) 613–621.

[8] P.K. Chintagunta, Endogeneity and heterogeneity in a probit demand model: estimation using aggregate data, Marketing Science 20 (4) (2001) 442–456.

[9] P.K. Chintagunta, B.E. Honore, Investigating the effects of marketing variables and unobserved heterogeneity in a multinomial probit model, International Journal of Research in Marketing 13 (1) (1996) 1–15.

[10] W. Elmaghraby, P. Keskinocak, Dynamic pricing in the presence of inventory considerations: research overview, current practices, and future directions, IEEE Engineering Management Review 31 (4) (2003) 47-47.

[11] J.-C. Ferrer, D. Fuentes, A system design to bridge the gap between the theory and practice of retail revenue management, International Journal of Revenue Management 5 (2) (2011) 261–275.

[12] J. Goensch, R. Klein, C. Steinhardt, Dynamic pricingstate-of-the-art, Zeitschrift für Betriebswirtschaft 3 (2009) 1–40.

[13] O. González-Benito, M.P. Martnez-Ruiz, A. Mollá-Descals, Retail pricing decisions and product category competitive structure, Decision Support Systems 49 (1) (Apr. 2010) 110–119.

[14] Kilts Center for Marketing, University of Chicago Booth School of Business, Dominick's Data Manual, 2013 available online: https://research.chicagobooth. edu/kilts/marketing-databases/dominicks [accessed 10 March 2014]

[15] T.P. Kunz, S.F. Crone, Demand models for the static retail price optimization problem — a revenue management perspective, 4th Student Conference on Operational Research 2014. Oasics openaccess series in informatics, 2014.

[16] M.K. Mantrala, P. Seetharaman, R. Kaul, S. Gopalakrishna, A. Stam, Optimal pricing strategies for an automotive aftermarket retailer, Journal of Marketing Research 43 (4) (Nov. 2006) 588–604.

[17] J. McGill, G.J. van Ryzin, Revenue management: research overview and prospects, Transportation Science 32 (2) (1999) 233–256.

[18] A.L. Montgomery, Creating micro-marketing pricing strategies using supermarket scanner data Marketing Science 16 (4) (1997) 315-337

[19] A.L. Montgomery, P. Rossi, Estimating price elasticities with theory-based priors, Journal of Marketing Research 36 (4) (1999) 413–423.

[21] D.J. Reibstein, H. Gatignon, Optimal product line pricing: the influence of elasticities and cross-elasticities, Journal of Marketing Research 21 (3) (Aug. 1984) 259.

[22] P. Rusmevichientong, Robust assortment optimization in revenue management under the multinomial logit choice model, Operations Research 60 (4) (2012) 1–33.

[23] W.J. Steiner, A. Brezger, C. Belitz, Flexible estimation of price response functions using retail scanner data, Journal of Retailing and Consumer Services 14 (6) (Nov. 2007) 383–393.

[24] S. Subramanian, H.D. Sherali, A fractional programming approach for retail category price optimization, Journal of Global Optimization 48 (2) (Nov. 2009) 263–277.

[25] N. Sung, J. Lee, Knowledge assisted dynamic pricing for large-scale retailers, Decision Support Systems 28 (4) (2000) 347–363.

[26] V. van den Berg, E. Kroes, E.T. Verhoef, Biases in willingness-to-pay measures from multinomial logit estimates due to unobserved heterogeneity, SSRN Electronic Journal (2010).

[27] J.M. Villas-Boas, R.S. Winer, Endogeneity in brand choice models, Management Science 45 (10) (1999) 1324–1338

[28] E.L. Zanutto, E.T. Bradlow, Data pruning in consumer choice models, Quantitative Marketing and Economics 4 (June) (Aug. 2006) 267–287.

Timo Kunz's main research area is business to consumer pricing with a strong emphasis on pricing and price optimization in the Retail industry, foremost data and demand models for price optimization purposes.

Sven Crone's main research focus is forecasting & time series prediction for logistics, supply chain management and demand planning, regularly employing methods of computa tional intelligence such as artificial neural networks and support vector machines.

Joern Meissner's main research focus is the area of stochastic and dynamic decisionmaking, and in particular applications to logistics, manufacturing, supply chain management, and pricing strategy.

---
otero_id: 28284
otero_key: "59ZDPZFB"
title: "Evaluating the Effectiveness of Marketing Campaigns for Malls Using a Novel Interpretable Machine Learning Model"
authors: "Tong Wang; Cheng He; Fujie Jin; Yu Jeffrey Hu"
year: "2022"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.1078"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Evaluating the Effectiveness of Marketing Campaigns for Malls Using a Novel Interpretable Machine Learning Model

Tong Wang,<sup>a</sup> Cheng He,<sup>b</sup> Fujie Jin,<sup>c</sup> Yu Jeffrey Hu<sup>d,</sup>\*

<sup>a</sup> Tippie College of Business, University of Iowa, Iowa City, Iowa 52241; <sup>b</sup> Wisconsin School of Business, University of Wisconsin-Madison, Madison, Wisconsin 53706; <sup>c</sup> Kelley School of Business, Indiana University, Bloomington, Indiana 47405; <sup>d</sup> Scheller College of Business, Georgia Institute of Technology, Atlanta, Georgia 30308 \*Corresponding author

Contact: tong-wang@uiowa.edu, https://orcid.org/0000-0001-8687-4208 (TW); che78@wisc.edu, https://orcid.org/0000-0003-4255-415 (CH); jinf@indiana.edu, https://orcid.org/0000-0002-2817-5676 (FJ); jeffrey.hu@scheller.gatech.edu, https://orcid.org/0000-0001-8482-4899 (YJH)

Received: January 8, 2020 Revised: January 2, 2021; July 21, 2021; September 20, 2021 Accepted: September 21, 2021 Published Online in Articles in Advance: December 21, 2021

https://doi.org/10.1287/isre.2021.1078

Copyright: © 2021 INFORMS

Abstract. In this study, we use newly available data and develop a novel interpretable machine learning model to evaluate how different types of marketing campaigns and budget allocations in<sup>fl</sup>uence malls’ customer traf<sup>fi</sup>c. The data we use is a large-scale customer traf<sup>fi</sup>c data set, collected through AI-chip-embedded sensors, across 25 malls over a twoyear period, and we combine it with detailed campaign information for our analyses. We classify the campaigns into <sup>fi</sup>ve categories based on the approach and timing of the campaigns. We then develop an innovative interpretable machine learning model, named generalized additive neural network model (GANNM), to accurately learn the response curves for different marketing campaigns. The response curves characterize the impact of campaign budget on customer traf<sup>fi</sup>c. We demonstrate that this new model has better predictive accuracy compared with current interpretable models and also yields additional business insights. We <sup>fi</sup>nd that campaigns with experience incentives lead to larger increases in customer traf<sup>fi</sup>c than campaigns with sales incentives only, and the contrast is more signi<sup>fi</sup>cant for campaigns in off-peak periods. In addition, malls can piggyback on online promotion events and boost customer traf<sup>fi</sup>c with campaigns held at the same time. We further demon strate that the optimized budget allocation based on the response curves learned by GANNM yields a 11.2% increase in customer traf<sup>fi</sup>c overall, compared with 3.2% achieved by a baseline with preassumed functional forms of response curves and 1.0% achieved by a post hoc explanation method. Overall, our proposed model provides more accurate estimations for response curves and presents interpretable and actionable insights for managers.

History: Olivia R. Liu Sheng, Senior Editor; Huimin Zhao, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.1078.

Keywords: interpretable machine learning response curve evaluation marketing campaigns mall customer traf<sup>fi</sup>c

## 1. Introduction

Malls hold trillions of dollars in asset value and serve as important physical platforms for of<sup>fl</sup>ine stores, which generate trillions of dollars in transactions each year. However, due to the increasing competition from online businesses in recent years, many malls have seen declines in customer traf<sup>fi</sup>c (Thomas 2019). Consequently, an increasing number of mall stores are closing, which severely affects rent revenue, the primary revenue source for malls. In contrast, malls that incorporate new technologies and business analytics tools to <sup>fi</sup>nd new ways to engage customers are growing and opening branches in new cities (Stein 2019). As digital transformation has been a general trend, we aim to design a new machine learning model to utilize data collected by new arti<sup>fi</sup>cial intelligence (AI)-enabled sensor technology to help malls make informed decisions and improve their performance.

The key metric to gauge the performance for malls is customer traffic, which is strongly correlated with mall revenue and serves as its preceding indicator (Yiu and Xu 2012). Customer traf<sup>fi</sup>c is the main index determining the rental prices for tenant stores to lease spaces in malls. Malls invest in various ways to increase traf<sup>fi</sup>c, including regular maintenance, renovation, and most importantly, running a number of campaigns throughout the year (Bloch et al. 1994). Mall campaigns involve different types of events, including promotional events around the holiday time, themed events with special decorations, or even entertainment events such as concerts. Such campaigns have proven to be effective in attracting customers to visit malls (Wake<sup>fi</sup>eld and Baker 1998).

Due to data limitations, malls have traditionally relied heavily on intuition-based decision making to plan the campaigns. Meanwhile, the unavailability of reliable and granular of<sup>fl</sup>ine traf<sup>fi</sup>c data has largely limited the scope of existing studies on marketing performance for malls (Vitorino 2012). Current studies mostly focus on a single store (Lam et al. 2001) or a speci<sup>fi</sup>c type of campaigns (Ghose et al. 2019). There remains a research gap in examining the performance of different types of campaigns for brick-and-mortar malls. In addition, existing methods for evaluating campaign performance generally assume the functional forms of response curves to characterize the increase in traf<sup>fi</sup>c due to increases in campaign budget, since the real function is usually unknown (Carroll et al. 1979, Bass et al. 2007). This has been acknowledged as a major limitation of current methodologies, for such functional form assumptions often do not align with the ground truth (Doyle and Saunders 1990, Fischer et al. 2011). Therefore, it is of high practical relevance and research value to explore how new granular data and novel prediction models can be applied to improve the effectiveness of campaigns.

The goal of our study is to design a novel interpretable machine learning model to learn the relationship between campaign budget and customer traf<sup>fi</sup>c, that is, the response curves of mall campaigns, using new data collected through AI technology, and measure how such response curves vary across different types of mall campaigns. We collaborate with a leading data analytics company in China to collect detailed customer traf<sup>fi</sup>c and mall campaign data. The company uses proprietary technology to extract mall traf<sup>fi</sup>c from AI-chip-embedded sensors, in real time and on a large scale. Our data set consists of observations from 25 malls spanning two years, with detailed daily measures on customer traf<sup>fi</sup>c and information about mall campaign schedule and budget. We categorize the campaigns along two dimensions, campaign approach and campaign timing, into <sup>fi</sup>ve categories and evaluate the response curves for each type, respectively. This categorization is based on previous literature (Bloch et al. 1994) and conversations with industry leaders. We also combine additional information on weather, temperature, and seasonality with the data to compile a rich list of features for the analyses.

To solve the challenges in accurately measuring marketing campaign effectiveness while preserving model interpretability, we make a methodological innovation in proposing a new interpretable machine learning model to learn the response curve for each category of campaigns. This new model constructs additive shape functions to characterize response curves from data, without any prior assumptions on their functional shapes, while jointly training a neural network to capture the interactions of other features. The model can present interpretable insights, since the response curves re<sup>fl</sup>ect how customer traf<sup>fi</sup>c changes depending on the campaign budget. Since our model has a generalized additive part and a neural network part, we name it a generalized additive neural network model (GANNM). This model combines the advantages of generalized additive models in interpretability and <sup>fl</sup>exible function forms, with the highly accurate predictive performance of neural networks, which are particularly powerful at handling complex feature interactions.

In terms of predictive accuracy, our results show that GANNM outperforms the interpretable baseline models, and its performance comes close to that of black-box models. In terms of interpretability, the shape functions from GANNM can re<sup>fl</sup>ect the relationship between input and output features more accurately and has superior properties such as robustness in capturing true underlying nonlinear patterns, compared with other interpretable models and post hoc explainers of black-box models. Furthermore, the optimal budget allocation derived from GANNM also leads to a much larger projected increase in mall traf<sup>fi</sup>c compared with baseline models.

The main contributions of this paper are in the following areas. First, this is the <sup>fi</sup>rst study to use granular customer traf<sup>fi</sup>c data to evaluate the effectiveness of mall campaigns. Therefore, we extend the stream of work on marketing performance that mostly focuses on online re tail (Ghose et al. 2019) to the of<sup>fl</sup>ine context. Second, we make a methodological contribution in proposing a new model, GANNM, to overcome the limitation of existing models to achieve both high prediction accuracy and model interpretability. Third, to our best knowledge, ours is the <sup>fi</sup>rst approach to systematically categorize mall campaigns based on their features and further compare how the response curves differ across various types of campaigns. This extends the stream of studies on marketing campaign performance, which focus mostly on either price or product promotions (Lam et al. 2001, Danaher et al. 2015), and enables us to characterize how the marketing budget for different categories of campaigns in<sup>fl</sup>uences customer traf<sup>fi</sup>c differently. We also demonstrate that the budget allocation optimized across different types of campaigns according to the response curves can lead to a signi<sup>fi</sup>cant increase in customer traf<sup>fi</sup>c.

In addition, the response curves produced by GANNM and budget allocation derived from them yield unique managerial insights. We <sup>fi</sup>nd that the impact of marketing budget on customer traf<sup>fi</sup>c varies for different types of campaigns: campaigns with experience incentives lead to larger increases in customer traf<sup>fi</sup>c than campaigns with sales incentives only, and the contrast is more signi<sup>fi</sup>cant for campaigns in the off peak period. Our <sup>fi</sup>ndings also have signi<sup>fi</sup>cant managerial implications, providing insights for managers on the returns to marketing campaigns and which types of campaigns are more effective in increasing customer traf<sup>fi</sup>c. We offer concrete suggestions on improving budget allocation to increase mall traf<sup>fi</sup>c. For example, we identify campaigns that could be over-marketed and suggest shifting the budget to other campaigns to attract more customer traf<sup>fi</sup>c without changing the total budget. We also <sup>fi</sup>nd that when major sales promotions are taking place on online platforms, malls can also bene<sup>fi</sup>t from a sharp increase in customer traf<sup>fi</sup>c by spending a suf<sup>fi</sup>cient amount of budget during the same period. These <sup>fi</sup>ndings provide valuable guidelines for mall managers.

## 2. Research Context

## 2.1. Customer Traffic as an Important Key Performance Indicator for Malls

Customer traf<sup>fi</sup>c is the most relevant key performance indicator (KPI) for mall managers (Bel-Bachir et al. 2019), and we use it as the outcome variable when evaluating the effectiveness of mall campaigns. Malls lease retail spaces to independent stores, including department stores, brand chain stores, and privately owned small businesses. The rent that malls collect from tenant stores is determined by factors such as square footage of the rental space, locations of the rental space, and customer traf<sup>fi</sup>c to the mall. Whereas square footage and location are usually <sup>fi</sup>xed, customer traf<sup>fi</sup>c is a variable factor that malls can take measures to improve. Increases in customer traf<sup>fi</sup>c strongly correlate with increases in mall revenue, as indicated by industry reports and as we found in an additional analysis.<sup>1</sup> Unlike department stores that use sales as a main KPI, malls focus on bringing in customers, and it is up to each tenant store to convert shoppers visiting the mall into paying customers. Therefore, increasing customer traf<sup>fi</sup>c, which in turn drives up mall revenue, is a key objective of mall managers.

## 2.2. Marketing Campaigns in Malls

A commonly used approach for malls to attract customers is organizing mall campaigns, such as coordinated price markdown across a number of tenant stores or featured events such as small-scale art exhibitions and concerts, so that tenant stores may convert customer traf<sup>fi</sup>c to their own revenue. The malls in our data typically schedule all campaigns for the coming year and decide upon the timing, approach, and budget by the end of the year. These campaigns vary in duration, ranging from one or two days to several weeks, and the campaign schedule also varies across malls. Therefore, we can use the variations in timing, approach, and budget across malls to evaluate the impact of different types of mall campaigns.

2.2.1. Campaign Classification. We categorize mall campaigns from two dimensions: (1) the approach of the campaign and (2) the timing of the campaign. This categorization is based on both theories (Bloch et al. 1994, for example) and interviews with mall managers. Along the <sup>fi</sup>rst dimension, malls can attract customers using different campaign approaches, such as offering sales-incentives, experience-incentives, or both. With sales-incentive campaigns, a mall typically coordinates tenant stores to organize mall-wide promotion events, where each store decides whether to participate and how much discount to offer. The mall may also offer some additional bene<sup>fi</sup>ts, such as gifts to customers who meet a certain threshold of total spending. With experience-incentive campaigns, malls host featured events that enhance customers’ shopping experience. These include, for example, mini-concerts, photo exhibitions, food tasting events, and other themed events to engage customers. Malls could also put up interior decorations for themed events or holidays. A mall campaign could also have both sales and experience-incentives.

The second dimension is the timing of the campaigns, which we classify into three types: (1) Peak period indicates whether the campaign takes place during the periods around either public holidays (including New Year’s Day, Christmas, National Day Holiday, and the Midautumn Festival) or special holidays (including Valentine’s Day, Mother’s Day, and Halloween). The malls typically hold promotions during this time to further increase customer traf<sup>fi</sup>c and sales. (2) Off-peak period consists of all the other days of the year except major holidays and days that coincide with online promotions. (3) Online promotion period re<sup>fl</sup>ects whether the campaign takes place during major online promotion periods, including November 11 (referred to as Singles’ Day, symbolized by 11/11), December 12 (referred to as Double 12 Day, <sup>fi</sup>rst started by Alibaba to promote Taobao marketplace, which then spread to different platforms and became a major online shopping festival), and June 18 (started by JD.com to celebrate its anniversaries and other platforms joined in to make it another online shopping festival).

2.2.2. Campaign Budget. The total campaign budget usually amounts to 5\~10% of a mall’s annual revenue. The campaign budget is used to cover costs in the fol lowing main areas: (1) advertising the campaigns both on traditional mass media, such as TV, radio, and out door display, and on digital media, such as Weibo and WeChat, to make potential customers aware of the campaigns; (2) operations of the campaigns, including the cost of personnel and material (e.g., gifts, indoor decorations) for the campaigns. These two areas of costs are both predetermined and not in<sup>fl</sup>uenced by the actual customer traf<sup>fi</sup>c. For example, the malls usually set a <sup>fi</sup>xed number of prepurchased gifts or coupons to give out. When customer traf<sup>fi</sup>c exceeds this set amount, actual expense is not expanded beyond the budget to accommodate these addition-

## 3. Related Literature

This study relates to two research areas. First, the business problem we solve relates to the literature on marketing campaign classi<sup>fi</sup>cations and campaign performance. Second, the novel machine learning method we propose extends from the literature on interpretable machine learning, especially generalized additive models.

## 3.1. Effectiveness of Marketing Campaigns

Past research on the effectiveness of marketing spending is mainly from retailers’ perspective due to data limitations. To our knowledge, no studies have used large-scale data to evaluate the returns of marketing efforts for malls. Existing approaches for examining how customers react to marketing spending include the Vidale-Wolfe model, which incorporates the naturally occurring sales decay over time, the promotion saturation of campaigns, and the response constant capturing sales generated per dollar investment (Vidale and Wolfe 1957). Extending from this model, additional studies examine how to allocate marketing budget across different products (Narayanan et al. 2004), country markets (Fischer et al. 2011, Peers et al. 2017), and channels and search markets (Yang et al. 2015). However, mall campaigns are usually not brand or product speci<sup>fi</sup>c, and they are affected by a set of different factors, so the aforementioned models do not readily apply.

Current approaches for evaluating marketing performances mostly rely on preassumed functional forms of how customers respond to campaigns (Bass et al. 2007, Fischer et al. 2011, Liu et al. 2017, Jindal et al. 2020). A major limitation of these approaches is that the results are often heavily in<sup>fl</sup>uenced by the speci<sup>fi</sup>c human-made assumptions on the functional shapes, which may not align with the ground truth (Doyle and Saunders 1990, Fischer et al. 2011). To <sup>fi</sup>ll this research gap and improve from existing models, we propose a novel machine learning model to learn the response curve from data without any assumptions on the functional shape. The response curve re-<sup>fl</sup>ects the corresponding mall traf<sup>fi</sup>c to different values of the campaign budget. We will demonstrate the performance improvement of this model compared with the existing methods.

Furthermore, whereas previous studies have separately examined how marketing ef<sup>fi</sup>ciency is in<sup>fl</sup>uenced by factors such as campaign content and design of the promotions (Iyer and Kuksov 2012, Gijsenberg 2017), no studies have provided a systematic categorization of different types of campaigns and compared their performances. In this study, the rich information on campaign descriptions, budget, and the large-scale observations from data across 25 malls allow us to quantify the heterogeneity in response curves across different campaign categories. Therefore, we make signi<sup>fi</sup>cant theoretical and practical contributions by modeling the returns to different types of campaigns.

3.1.1. Campaign Approach. Past research has categorized the motivations for customers to visit malls into two main groups: consumption of the goods and consumption of the experience (Bloch et al. 1994). Thus, marketing campaigns featuring sales promotions or enhancement of customer experiences can both im prove store performance (Bues et al. 2017). Prior studies relating to sales-incentives have shown that well-designed price promotions allow better adjustment to the time-varying patterns in demand and supply and increase revenue for retails (Hall et al. 2010). Lam et al. (2001) examine how price discounts and clearance promotions in<sup>fl</sup>uence store performance. Cooper et al. (1999) demonstrate that a promotion event rating system based on linear models improved the accuracy in predicting the lift on product sales from promotions, compared with just historical averages. Wu et al. (2021) evaluate how various types of price promotions in<sup>fl</sup>uence consumer feedback differently. However, past research mostly focuses on the impact of sales-incentive campaigns for a single retailer. To our knowledge, no studies have examined the impact of such campaigns on mall traf<sup>fi</sup>c using data across multiple malls.

The shopping experience is another critical driver of customer satisfaction and intention to visit (Wake-<sup>fi</sup>eld and Baker 1998). Previous studies have shown that shopping experiences enhance customer moods, which subsequently increases customers’ purchasing intentions (Swinyard 1993). Verhoef et al. (2009) show that improving customer experience helps retailers attract customer traf<sup>fi</sup>c. Iyer and Kuksov (2012) use an analytical approach to model retailers’ optimal strategies and found that retailers should both invest in enhancing customer experience and sales promotions when consumers’ search cost is high, and invest in improving shopping experience only when customers derive high utility from shopping experiences and search cost is low. Recent studies have also examined how novel approaches to enhance customer experiences, such as in-store demonstrations and gami<sup>fi</sup>cation designs, in<sup>fl</sup>uence the effectiveness of such campaigns (Nordfalt and Lange¨ 2013, Hogberg et al.¨ 2019). However, we have found no similar studies that quantify the returns of such investments or evaluate how it compares with other campaigns for malls, which is a research gap that we intend to <sup>fi</sup>ll with this study.

3.1.2. Campaign Timing. Past literature has demonstrated that the effectiveness of marketing campaigns varies depending on the timing. For example, Gijsenberg (2017) show that marketing spending is more effective in periods of peak-demand overall. Danaher et al. (2015) examine mobile promotions and <sup>fi</sup>nd that seasonality could in<sup>fl</sup>uence promotion effectiveness. Warner and Barsky (1995) <sup>fi</sup>nd that customer traf<sup>fi</sup>c increased sharply during the holiday season, and retailers typically planned more campaigns during this time. Past research has also demonstrated how coordinating campaigns during the peak season and the offseason increases retailer revenue, from the operations perspective (Chen and Chen 2015, Ye et al. 2015). In contrast, some recent industry reports suggested that retailers should reconsider such concentrated marketing efforts during the holiday season and instead focus more on targeted campaigns throughout the year (Yohn 2017). Considering such interestingly con<sup>fl</sup>icting evidence, in this study, we identify whether the mall campaigns overlap with holidays (i.e., peak period for malls) and whether this in<sup>fl</sup>uences their performance. Recent studies have also examined the effectiveness of promotions during popular events, such as the Olympics (Keller et al. 2019). Motivated by this stream of research, we also separately categorize mall campaigns that overlap in timing with major online promotion periods.

Overall, the impact of various campaign features listed earlier has been discussed separately in previous literature, mostly using data from a single retailer. However, it is less clear how customer traf<sup>fi</sup>c is affected by campaigns with different features and budgets for malls. This study extends from the existing literature by categorizing campaigns based on combinations of campaign approaches and timing features and quantifying their respective impact on customer traf<sup>fi</sup>c.

## 3.2. Interpretable Machine Learning Models

As machine learning becomes widely adopted to solve real-world problems, the need for model interpretability is also on the rise. In our research context, obtaining accurate response curves that capture how mall traf<sup>fi</sup>c changes, depending on the allocated budget for various types of campaigns, is key for mall managers to make informed decisions. Such practical need is one of the main drives for us to build an interpretable machine learning model.

There are two common approaches to achieving interpretability. The <sup>fi</sup>rst approach is building a blackbox model as accurate as possible and then apply post hoc explainers to obtain interpretations. Popular models using this approach include Local Interpretable Model-agnostic Explanations (LIME) (Ribeiro et al. 2016) and SHapley Additive exPlanation (SHAP) (Lundberg and Lee 2017), which employ local approximation methods or game-based solutions to simulate the predictions of the black-box model, respectively. However, major issues with post hoc methods have been raised in recent years, concerning the ambiguity, inconsistency, and multiplicity in the explanations (Aïvodji et al. 2019, Rudin 2019, Thibault et al. 2019). These explanations can sometimes be easily manipulated (Slack et al. 2020) or vary signi<sup>fi</sup>cantly as parameter settings change (Ross et al. 2017). Since there are no observable ground truths for the explanations, such issues with the pos hoc explainers can limit their practical application. When con<sup>fl</sup>icting explanations are presented, for example, with one explanation recommending increasing the budget for a type of campaign, and another explanation suggesting the opposite, managers would not be able to determine theoretically which explanation is more accurate. This is mainly because the post hoc explainers can only approximate a decision-making process but are not the decision-making process themselves (Aïvodji et al. 2019).

Therefore, to achieve interpretability with high practical relevance, increasing attention has been placed on the second approach, which is building an inherently interpretable model that is understandable on its own. Such models include generalized additive models (GAM), linear models, rule-based models (Wang et al. 2017, Wang 2018), and so on. A major advantage of this approach is that there is no ambiguity in the explanations since they are the decision-making processes themselves. At the same time, the main concern with this approach is that models possibly sacri-<sup>fi</sup>ce predictive performance to ensure interpretability. We propose a novel form of model that achieves interpretability while maintaining highly competitive performance. Although our main model is constructed using this second approach, we also use models from the post hoc explanation approach as benchmarks for comparison.

## 3.3. Generalized Additive Models

This section reviews the literature on GAM and discusses its advantage in interpretability and drawback in handling interactions between features. We provide an overview of the current approaches for addressing this drawback and discuss the limitations of these approaches. Then we highlight the methodological innovation in the new model we propose, GANNM, and how it improves from existing GAM setups.

The generalized additive model (GAM) speci<sup>fi</sup>es that the value of the target variable is a linear summation of a series of shape functions for each feature. No assumptions are made on the speci<sup>fi</sup>c functional forms for the shape functions, and they can be linear, nonlinear, and nonmonotonic (Hastie and Tibshirani 1987). This property allows GAM to capture the underlying relationships between variables with more <sup>fl</sup>exibility than simple linear models. It is especially bene<sup>fi</sup>cial when there are highly nonlinear relationships between the response variable and the set of explanatory variables (Guisan et al. 2002). GAMs can provide shape functions that represent how each feature relates to the response variable. Such shape functions cannot be provided by noninterpretable machine learning models such as neural networks. This gives GAMs a signi<sup>fi</sup>cant advantage in interpretability and practical applications. A GAM is typically formulated as:

$$
f (\mathbf {z}) = s _ {0} + s _ {1} (z _ {1}) + s _ {2} (z _ {2}) + \dots + s _ {L} (z _ {L}),\tag{1}
$$

where L is the number of features and $s _ { l } ( \cdot )$ is a shape function for feature $z _ { l } .$ The shape functions can be arbitrarily complex, which can be constructed via basis functions such as splines (Hastie and Tibshirani 1987), trees, or ensembles of trees (Lou et al. 2012).

Although GAM shows a signi<sup>fi</sup>cant advantage in interpretability due to its additive nature, it also has a major limitation in handling large numbers of interaction terms. This limitation leads to two drawbacks: <sup>fi</sup>rst, the predictive performance is often compromised; and second, the shape functions often exhibit unexplainable wiggliness, as they try to <sup>fi</sup>t the <sup>fl</sup>uctuations caused by the unobserved interactions, so the estimated relationships between individual features and the target variable from such models may not be robust and reliable. Therefore, some extensions from classical GAMs propose to add selected interactions into the model. For example, Coull et al. (2001) incorporates factor-by-curve interactions, that is, interactions between numeric features and categorical features. A more recent stream of work on generalized additive models plus interactions (GA2 M) adds pairwise interaction terms for features to the classical GAMs, which improves the overall predictive performance at a complexity cost of $\Omega ( d ^ { 2 } )$ extra terms (d is the number of features) (Lou et al. 2013, Caruana et al. 2015). However, the interactions included in GA2M are still limited to pairwise interactions only.

Our methodological contribution to this stream of literature is that we develop a new model, GANNM, to tackle the limitation of GAMs in handling interaction terms. GANNM uses the fully connected neural network to capture the interactions among all the nonbudget features while preserving the interpretability of GAM.

## 3.4. Limitations of Existing Models and Our Methodological Innovations

3.4.1. Limitations of Existing Models. Obtaining accurate characterizations of response curves is often critical for managerial decisions. In our context, response curves that accurately re<sup>fl</sup>ect the marginal impact of campaign budget on mall traf<sup>fi</sup>c are highly sought after by mall managers. None of the existing machine learning models, either interpretable or black-box models, are perfectly suited for this task, since they either do not directly return a response curve or do not allow feature interactions to achieve satisfying accuracy.

First, although black-box models such as neural networks and ensemble methods (e.g., random forests) can achieve high predictive performance, they do not directly provide response curves. Second, at the other end of the spectrum, for typical interpretable models such as linear models, the response curves are primarily determined by user assumptions on the functional forms. This limits the ability of these models to accurately capture patterns in the data. GAM and its variants are also interpretable and can learn shape function from data, but they either do not allow interactions or only allow pairwise interactions and rely on heuristics to select the interaction terms to include. Such limitations can signi<sup>fi</sup>cantly reduce the predictive performance of the model.

3.4.2. GANNM Design. We design a new model to speci<sup>fi</sup>cally address the problem of learning response curves from the large dimensional data. The new model, GANNM, consists of two parts: an interpretable component and a black-box component. We summarize the characteristics of GANNM compared with some existing models in Table 1. In this section, we elaborate on the design of GANNM and the purpose for each component.

3.4.2.1. Choice of GAM. We use GAM to characterize the relationship between the campaign budget and the increase in customer traf<sup>fi</sup>c. This is because GAMs produce shape functions that represent the relationship between individual features and the target variable, which is precisely our goal. In addition, the shape functions of GAM are learned from data, which avoids requiring prior assumptions on the relationship that could mislead the model.<sup>3</sup>

3.4.2.2. Choice of Neural Network. A neural network (NN) is introduced to capture the interactions of all the nonbudget features. This serves three purposes. First, this NN part improves the overall predictive performance since interactions cannot be captured by the GAM part. Second, the NN component disentangles the in<sup>fl</sup>uence of other nonbudget features from the budget features, so that the shape functions only need to account for the one-to-one mapping from budget to customer traf<sup>fi</sup>c. A similar idea was adopted by GA2M (Lou et al. 2013, Caruana et al. 2015), which included pairwise interactions and used a heuristic to select the top pairs of features to include. Our improvement through using a NN is that it allows full interactions of all nonbudget features via the fully connected layers, no longer requiring manual speci<sup>fi</sup>cations on the pairs of interactions to include. Third, since the neural network captures the impact of the nonbudget features, the GAM part does not need to be overly wiggly in order to <sup>fi</sup>t all the variations in the data, which prevents over<sup>fi</sup>tting the GAM part. Furthermore, it is feasible for both the GAM part and the NN part to be jointly trained under a customized global objective, since NN is trained via gradients, which also applies for training GAM. Therefore, both parts can be trained together as a single model, without requiring super<sup>fl</sup>uous assumptions or manipulations.

Table 1. Comparison of GANNM with Existing Modelss

<table><tr><td>Model</td><td>Interpretable</td><td>Allows interactions</td><td>Learns a curve</td><td>Predictive performance</td></tr><tr><td>GANNM</td><td>✓</td><td>✓</td><td>✓</td><td>High</td></tr><tr><td>GAM</td><td>✓</td><td>✘</td><td>✓</td><td>Low</td></tr><tr><td>GA2M</td><td>✓</td><td>✓</td><td>✓</td><td>Medium</td></tr><tr><td>Linear</td><td>✓</td><td>✘</td><td>✓</td><td>Low</td></tr><tr><td>NN</td><td>✘</td><td>✓</td><td>✘</td><td>High</td></tr><tr><td>Ensemble (e.g., rf)</td><td>✘</td><td>✓</td><td>✘</td><td>High</td></tr></table>

## 4. Data

## 4.1. Data Description

For this study, we obtain a unique panel data set of daily customer traf<sup>fi</sup>c from January 2017 to December 2018 for 25 malls in China that are representative in size, age, and location. These 25 malls have all adopted a newly available customer monitoring system to track mall traf<sup>fi</sup>c in real time. Our data consists of 40,777 mall-daily-level observations and covers 936 unique mall campaigns. The main explanatory variable of interest is the average daily budget for a mall for each day of the campaign (zero if there are no active campaigns in the mall on the given day). We also have the full-text descriptions for each campaign, specifying the types of events or promotions included in each campaign. Overall, the malls have active campaigns about 20% of the days in our observation period. On average, each mall has around 18 campaigns each year, and the budget for each campaign is 188,300 Chinese renminbi (RMB) on average. The mall campaigns could either overlap with major holidays or special days (e.g., Christmas, New Year’s, Mother’s Day) or feature mall-speci<sup>fi</sup>c events (e.g., anniversaries of mall openings). The 25 malls in our sample have different schedules for the campaigns (i.e., each mall may choose a different subset of holidays to focus on instead of having campaigns every holiday period). Large variations are also observed in budget allocations across campaigns for different malls. Such differences provide suf<sup>fi</sup>cient variations for us to identify the returns of the mall campaign budget, that is, the increase in customer traf<sup>fi</sup>c.

The customer traf<sup>fi</sup>c data are collected using stateof-the-art customer monitoring systems produced by a leading company in the industry, and this system has been installed in more than 2,000 malls in China. This customer monitoring system uses AI-chip-embedded sensors installed at mall entrances to record customer <sup>fl</sup>ow. Any time a person enters through any of the mall’s entrances, it will be recorded by the sensors. This information is passed on to the image processing algorithms in the chips to count the traf<sup>fi</sup>c in real time. Therefore, the mall traf<sup>fi</sup>c data produced by this system can be interpreted as the number of person-visits. For privacy reasons, the customer monitoring system does not aim to identify or trace individual customers. Therefore, it cannot remove duplicate customers or track the duration of customers stay in the malls. However, this limitation is unlikely to impact the applicability of our mall traf<sup>fi</sup>c measure in a signi<sup>fi</sup>cant way. Since the same technology is used to count customer traf<sup>fi</sup>c across all 25 malls across time, the traf<sup>fi</sup>c data are therefore consistent and comparable. The traf<sup>fi</sup>c count is the best measure that state-of-the-art technology can provide, and it is a standard metric used in the mall industry today.

To control for the heterogeneity across individual malls and daily <sup>fl</sup>uctuations in customer traf<sup>fi</sup>c due to external factors, we combine the data with other attributes of each mall, including the gross leasable area (the total square footage available to rent to stores), location of the mall, daily attributes such as weather and temperature, and indicator variables for weekdays and holidays, following a similar approach as previous studies (Lam et al. 2001). The list of features and the summary statistics are reported in Table 2.

## 4.2. Mall Campaign Categories

We classify each mall campaign based on its description along two dimensions, campaign approach and campaign timing, as discussed in Section 2.2. Along the timing dimension, campaigns fall into three groups: peak period, off-peak period, and online promotion period. Along the campaign approach dimension, campaigns fall into three groups: sales-incentives only, experience-incentives only, and both sales and experience-incentives. The combination of these two dimensions theoretically yields 3 3 9 possible categories, <sup>fi</sup>ve of which are actually observed in the data. For example, we observe that the malls offer campaigns with both sales and experience-incentives, or experience-incentives only during peak periods, but not sales-incentives only. The <sup>fi</sup>ve campaign categories observed in the data as shown in Table 3.

Table 2. Summary Statistics of Data

<table><tr><td>Features</td><td>Observations</td><td>Mean</td><td>Median</td><td>Min</td><td>Max</td><td>Std Dev</td></tr><tr><td colspan="7">Mall-day-level variables</td></tr><tr><td>Mall daily traffic</td><td>40,777</td><td>39,578</td><td>36,472</td><td>2,788</td><td>252,754</td><td>16,110</td></tr><tr><td>Campaign dummy (0/1)</td><td>40,777</td><td>0.24</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.43</td></tr><tr><td>Months since open</td><td>40,777</td><td>57.48</td><td>57.00</td><td>3.00</td><td>134.00</td><td>27.15</td></tr><tr><td>Temperature</td><td>40,777</td><td>20.23</td><td>23.00</td><td>-24.00</td><td>40.00</td><td>11.76</td></tr><tr><td>Holiday dummy</td><td>40,777</td><td>0.08</td><td>0.00</td><td>0.00</td><td>2.00</td><td>0.27</td></tr><tr><td>Weather</td><td>Sunny, cloudy, windy, rainy, extreme</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="7">Campaign-level variables</td></tr><tr><td>Duration of the campaigns</td><td>936</td><td>11.22</td><td>10.00</td><td>1.00</td><td>159.00</td><td>9.76</td></tr><tr><td>Budget per campaign (10,000 RMB)</td><td>936</td><td>18.83</td><td>12.43</td><td>1.00</td><td>261.50</td><td>22.00</td></tr><tr><td>Campaign type dummies</td><td>One dummy for each type of campaign</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="7">Daily budget by campaign types</td></tr><tr><td>Peak period campaign with experience and sales incentives</td><td>2,414</td><td>1.68</td><td>1.20</td><td>0.19</td><td>100.71</td><td>2.57</td></tr><tr><td>Peak period campaign with only experience incentives</td><td>1,180</td><td>1.82</td><td>1.43</td><td>0.27</td><td>9.50</td><td>1.42</td></tr><tr><td>Off-peak period campaign with sales incentives</td><td>621</td><td>1.99</td><td>1.62</td><td>0.44</td><td>5.56</td><td>1.24</td></tr><tr><td>Off-peak period campaign with experience incentives</td><td>4,876</td><td>1.48</td><td>0.83</td><td>0.20</td><td>33.33</td><td>2.30</td></tr><tr><td>Online promotion period campaign</td><td>627</td><td>3.70</td><td>1.86</td><td>0.09</td><td>33.33</td><td>5.48</td></tr><tr><td colspan="7">Mall-level variables</td></tr><tr><td>Gross leasable area</td><td>25</td><td>133,574</td><td>135,315</td><td>96,422</td><td>168,256</td><td>15,525</td></tr><tr><td>Other mall-level features</td><td>ID, scale, and geographic location of the malls</td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 5. GANNM Formulation and Training

We propose a novel machine learning model, GANNM, which combines a generalized additive model and a neural network model. The generalized additive part produces shape functions, that is, the response curves, to characterize the marginal impact of marketing budget on customer traf<sup>fi</sup>c for each campaign category. The neural network captures complicated interactions of all the other nonbudget features used as controls, including weather, temperature, seasonality, and so on.

We denote the data as $\mathcal { D } = \{ ( m _ { 1 } ^ { ( i ) } , \cdots , m _ { 5 } ^ { ( i ) } , \mathbf { x } ^ { ( i ) } , y ^ { ( i ) } ) \} _ { i = 1 } ^ { n } ,$ consisting of n observations, where $\mathbf { x } ^ { ( i ) } \in \mathcal { R } ^ { d }$ corresponds to the features of a mall at a given day, as listed in Table 2. We <sup>fi</sup>rst introduce the notations $m _ { 1 } ^ { \binom { i } { i } } , \cdots , m _ { 5 } ^ { ( i ) }$ represent the campaign budget allocated to this observation for campaign category $j \in \{ 1 , 2 , 3 , 4 , 5 \}$ . Since each campaign belongs to one of the <sup>fi</sup>ve categories, and it is possible to have no campaign on a given day, at most one of $m _ { 1 } ^ { ( i ) } , \cdots , m _ { 5 } ^ { ( i ) }$ is nonzero. We <sup>fi</sup>rst introduce the notations $y ^ { ( i ) } \in \bar { \mathcal { R } }$ is the target variable, mall traf<sup>fi</sup>c on the given day. We provide a notation table in Online Appendix B.

## 5.1. Model Formulation

We aim to build an interpretable additive model that consists of a canonical generalized additive part, s, parameterized by β, and a feed-forward fully connected neural network, g, parameterized by <sup>w</sup> and g captures the interactions of features. This model setup is illustrated in Figure 1.

The prediction of our model f is thus the sum of two parts: (1) the interpretable output from s, representing the response curves; and (2) the output from g, capturing interactions between other nonbudget features that are only included in this black-box neural network part since we do not focus on interpreting the impact of these additional features in detail but need to control for these features and include them to improve model accuracy. The output of GANNM is expressed as:

$$
\begin{array}{l} f \Big (\{m _ {j} ^ {(i)} \} _ {j = 1} ^ {5}, \mathbf {x} ^ {(i)} \Big) \\ = \underbrace {s _ {0} + \sum_ {j = 1} ^ {5} s _ {j} (m _ {j} ^ {(i)})} _ {\text {s(\cdot): generalized additive shape functions}} + \underbrace {g (x _ {1} ^ {(i)} , \cdots x _ {d} ^ {(i)})} _ {\text {neural network}}, \end{array}\tag{2}
$$

where the shape function $s _ { j } ( \cdot )$ characterizes the response curve we aim to learn for budget $m _ { j } ^ { ( i ) } , j = 1 , \cdots , 5 ,$ , that is, given a budget of $m _ { j } ^ { ( i ) }$ , the expected increase in mall traf-<sup>fi</sup>c is $s _ { j } ( m _ { j } ^ { ( i ) } )$ , which is computed as a sum of K simpler basis functions $b _ { j , k }$ . Here, $b _ { j , k }$ is multiplied by corresponding coef<sup>fi</sup>cient $\beta _ { j , k } .$ , which needs to be estimated. The shape functions are de<sup>fi</sup>ned as:

Table 3. Campaign Category De<sup>fi</sup>nitions

<table><tr><td rowspan="2">Timing</td><td colspan="3">Approach</td></tr><tr><td>Experience incentives</td><td>Sales incentives</td><td>Experience and sales incentives</td></tr><tr><td>Peak period</td><td>(1) Peak period campaigns with experience incentives only</td><td>No observations</td><td>(2) Peak period campaigns with sales and experience incentives</td></tr><tr><td>Off-peak period</td><td>(3) Off-peak period campaign with experience incentives only</td><td>(4) Off-peak period campaigns with sales incentives only</td><td>No observations</td></tr><tr><td>Online promotion period</td><td>No observations</td><td>No observations</td><td>(5) Online promotion period campaigns with experience and sales incentives</td></tr></table>

$$
s _ {j} (m _ {j} ^ {(i)}) = \sum_ {k = 1} ^ {K} \beta_ {j, k} b _ {j, k} (m _ {j} ^ {(i)}).\tag{3}
$$

We choose the commonly used B-splines (De Boor 1978) as basis functions. The main advantage of learning shape functions following Equation (3) is that it can approximate unknown functionals via a linear combination of basis splines, instead of relying on speci<sup>fi</sup>c functional form assumptions, as in the approach employed by prior studies (Bass et al. 2007, Fischer et al. 2011).

To train GANNM, we <sup>fi</sup>rst formulate the objective function. The goal is to ensure that the <sup>fi</sup>tted model achieves high predictive accuracy, avoids over<sup>fi</sup>tting, and maintains interpretability. Speci<sup>fi</sup>cally, we set the following three goals of the objective function:

5.1.1. Fitting Loss. As with all supervised training, an important goal in training is to minimize the predictive error on the data D. This is captured by the loss function $\mathcal { L } ( \beta , { \bf w } , \mathcal { D } )$ , which measures the mean squared error of the predicted values $f ( \{ m _ { j } ^ { ( i ) } \} _ { j = 1 } ^ { 5 } , \pmb { x } ^ { ( i ) } )$ against the true value $y ^ { \hat { ( i ) } }$ :

$$
\mathcal {L} (\boldsymbol {\beta}, \mathbf {w}, \mathcal {D}) = \frac {1}{n} \sum_ {i = 1} ^ {n} \left(f (\{m _ {j} ^ {(i)} \} _ {j = 1} ^ {5}, \mathbf {x} ^ {(i)}) - y ^ {(i)}\right) ^ {2}.\tag{4}
$$

5.1.2. Smoothness Control. We also explicitly incorporate the smoothness of the shape functions $s _ { j } ( \cdot )$ into the objective function. Spurious wiggliness in the curve, which is a drastic deviation from nearby functiona forms in a local region, not only re<sup>fl</sup>ects a more compli cated and potentially unrealistic relationship between the budget and the traf<sup>fi</sup>c, but can also cause reliability issues if a small change in the budget results in a signif icant change in the curve. Such wiggliness usually does not re<sup>fl</sup>ect actual patterns in the data but is caused by over<sup>fi</sup>tting the model to the training data. For example, as plot (a) in Figure 2 illustrates, it is not realistic to expect that the increase in customer traf<sup>fi</sup>c decreases drastically when the mall invests \$12,000 instead of \$10,000 in a campaign, and then suddenly bounces back when the budget is further increased to \$14,000. Typically, the customer traf<sup>fi</sup>c increase resulting from marketing spending follows a smoother curve, as illustrated in plot (b), and the extra wiggliness in (a) is most likely caused by over<sup>fi</sup>tting the model.

Wiggliness is determined by the number of basis functions K and the coef<sup>fi</sup>cients $\beta$ combining the basis functions (Wood 2017). Hyper-parameter $K$ can be determined via cross-validation. In the learning framework, we consider regularizing the coef<sup>fi</sup>cients by adding a smoothing penalty that in<sup>fl</sup>uences $\beta$ to prevent excess wiggliness. Therefore, the second part of the objective function is de<sup>fi</sup>ned as:

Figure 1. (Color online) GANNM Contains a Generalized Additive Component and a Neural Network Component  
![](/api/attachments/59ZDPZFB/fulltext/images/ede375f58ce452a9cc6829bbac3bbd3a02523af337a94db655d88ca5efa5b6f6.jpg)

Figure 2. (Color online) Illustration for an Over<sup>fi</sup>tted Curve with High Wiggliness (a) and a Smoother Curve (b)  
(a)  
![](/api/attachments/59ZDPZFB/fulltext/images/257278ca00762b911f359f584c1960a7d5779e4ff83a1fd66fb1df4cc5edfe32.jpg)  
(b)

$$
\Omega (\boldsymbol {\beta}) = \boldsymbol {\beta} ^ {\top} \mathbf {S} \boldsymbol {\beta}.\tag{5}
$$

Here $\Omega ( \beta )$ measures wiggliness as the sum of squared second differences of the function at the knots, where knots are points where piecewise curves join in a shape function. Meanwhile, $\hat { \bf S }$ is a penalty matrix and $\bar { S } =$ $\begin{array} { r } { \int \mathbf { d } ( x ) \mathbf { d } ( x ) ^ { \top } d x . } \end{array}$ , where $d _ { j } ( x ) = b _ { j } ^ { \prime \prime } ( x )$ (Wood 2017). The intuition for this penalty matrix formulation is to try to <sup>fi</sup>t models that are smoother, with less drastic changes, as re<sup>fl</sup>ected in the second order derivative. Other penalty functions such as zero derivative or <sup>fi</sup>rst derivative penalty can also be applied using the same Equation (5) with different penalty matrix <sup>S</sup>.

![](/api/attachments/59ZDPZFB/fulltext/images/047fe36dea13208ffacb8e347d8bb9f73696b2bad9ae2e68e96c4048e2a8a6b6.jpg)

5.1.3. Neural Network Regularization. Finally, we need to regularize the contribution from the neural network $g$ to the predicted outcome. Without such a constrain, the output from $g$ is likely to dominate the prediction result since $g$ is naturally more accurate than the generalized additive part, and the model will then be reduced to a neural network, suppressing all response curves (shape functions) to zero. Since the goal of GANNM is to capture the impact of the campaign budget with interpretable shape functions, the contribution from the black-box $g$ must be regularized to prevent dominating the shape functions. Therefore, we regularize the output from $g ,$ denoted as:

$$
\mathcal {N} (\mathbf {w}, \mathcal {D}) = \frac {1}{n} \sum_ {i = 1} ^ {n} g (\mathbf {x} ^ {(i)}) ^ {2}.\tag{6}
$$

5.1.4. Learning Objective. In light of the previous considerations, we train the prediction model and obtain parameter estimates to minimize the following objective function:

$$
\Gamma (\boldsymbol {\beta}, \mathbf {w}; \mathcal {D}) = \mathcal {L} (\boldsymbol {\beta}, \mathbf {w}; \mathcal {D}) + \lambda_ {1} \Omega (\boldsymbol {\beta}) + \lambda_ {2} \mathcal {N} (\mathbf {w}; \mathcal {D}),\tag{7}
$$

where $\lambda _ { 1 }$ is the smoothing parameter that controls the trade-off between predictive accuracy and smoothness of the estimation of the generalized additive model part. When $\lambda _ { 1 } \to \infty \ s _ { j } ( \cdot )$ becomes a straight line, whereas $\lambda _ { 1 } = 0$ results in an unpenalized generalized additive model with neural corrections, which could yield a model dominated by the neural network only, where the generalized additive part either reduces to zero or no longer learns the correct response curves. Meanwhile, $\lambda _ { 2 }$ controls the contribution from the neural network. When $\lambda _ { 2 } \to \infty$ , the output of $g$ is forced to be 0, and the model is reduced to a GAM.

## 5.2. Training Algorithm

We describe the training procedure for GANNM. There are two sets of parameters to learn, $\beta$ for s and <sup>w</sup> for $g ( \cdot )$ . Our goal is to <sup>fi</sup>nd $\beta ^ { * } , \mathbf { w } ^ { * }$ that minimize the objective function, that is:

$$
\boldsymbol {\beta} ^ {*}, \mathbf {w} ^ {*} \in \arg \min \Gamma_ {\beta , \mathbf {w}} (\boldsymbol {\beta}, \mathbf {w}; \mathcal {D}).\tag{8}
$$

We <sup>fi</sup>rst extract K basis functions for each feature and then feed them into a neural network. The sum of their output is then added to the output of a neural network. Figure 3 illustrates the architecture of GANNM and how the input data are transformed to produce the predicted outcome.

Let t represent the iteration step, and batch represent the indices of training instances at batch $t ,$ where a batch represents a small subset of training examples to compute one gradient step in the algorithm. Training the joint model involves updating parameters for the generalized additive part s<sub>(·)</sub> and the neural network $g ( \cdot )$ . The gradient for s is:

Figure 3. Structure of GANNM  
![](/api/attachments/59ZDPZFB/fulltext/images/c331065a1bb7c58871c01342ad3b437ea190cfe3498cedcbbae9cd4101cd934f.jpg)

$$
\begin{array}{l} \frac {\partial \Gamma_ {t}}{\partial \boldsymbol {\beta} _ {t}} = \frac {\partial \mathcal {L} _ {t}}{\partial \boldsymbol {\beta} _ {t}} + \lambda_ {1} \frac {\boldsymbol {\beta} ^ {\top} \mathbf {S} \boldsymbol {\beta}}{\partial \beta} = - \frac {2 \lambda_ {1}}{n} \sum_ {i \in \text {batch} _ {t}} \left(y ^ {(i)} - f _ {t - 1} (\mathbf {x} ^ {(i)})\right) \frac {\partial s _ {t}}{\partial \beta_ {t}} \\ + \lambda_ {1} (\mathbf {S} + \mathbf {S} ^ {\top}) \boldsymbol {\beta} _ {t}. \end{array}\tag{9}
$$

The gradient for g<sub>(·)</sub> is:

$$
\begin{array}{c} \frac {\partial \Gamma_ {t}}{\partial \mathbf {w} _ {t}} = - \frac {2 \lambda_ {1}}{n} \sum_ {i \in \mathrm{batch} _ {t}} \Big (y ^ {(i)} - f _ {t - 1} (\mathbf {x} ^ {(i)}) \Big) \frac {\partial g _ {t}}{\partial \mathbf {w} _ {t}} \\ + \frac {2 \lambda_ {2}}{n} \sum_ {i \in \mathrm{batch} _ {t}} g (\mathbf {x} ^ {(i)}) \frac {\partial g _ {t}}{\partial \mathbf {w} _ {t}}. \end{array}\tag{10}
$$

We use the off-the-shelf Adam algorithm to train the model (Kingma and Ba 2014). The parameters in the neural network are updated via backpropagation. To avoid over<sup>fi</sup>tting, we adopt three standard strategies to prevent over<sup>fi</sup>tting, which are dropouts, early stopping, and weight decay in the ADAM optimizer (Srivastava et al. 2014). We set the neural network to be a two-layer fully connected feed-forward network, with the <sup>fi</sup>rst hidden layer containing ℓ nodes and the second hidden layer containing $\frac { \ell } { 2 }$ nodes. The activation functions are Relu. We explore tuning the number of basis functions from six to 11. We <sup>fi</sup>x $\lambda _ { 1 }$ to 0.01 and choose $\lambda _ { 2 }$ from [0, 10]. Since there are only three hyper-parameters (ℓ, λ<sub>1</sub>, λ<sub>2</sub>) to tune, we conduct a grid search and choose the parameters with the best performance on the validation set.

## 6. Results

In this section, we report the results from GANNM and interpret the response curves for different types of campaigns. We also compare GANNM with a collection of baseline models, along with the predictive accuracy dimension and the interpretability dimension, respectively. We demonstrate that GANNM outperforms other existing interpretable models and moves closer toward the noninterpretable black-box models in predictive accuracy. In addition, GANNM generates more unique insights from the response curves it produces, compared with the commonly used baseline models. All baseline models use the same input features as GANNM, that is, $m _ { 1 } ^ { ( i ) } , m _ { 2 } ^ { ( i ) } , m _ { 3 } ^ { ( i ) } , m _ { 4 } ^ { ( i ) } , \dot { m } _ { 5 } ^ { ( i ) }$ , and $\mathbf { x } ^ { ( i ) }$ . We partition the observations from the year 2017 into the 85% training and 15% validation data and use the observations from the year 2018 as the testing data. 4

## 6.1. Comparison in Predictive Performance

We compare GANNM with a set of baselines, including interpretable models with no interactions (GAM and the linear-quadratic model), interpretable models with interactions (GA2M and a linear-quadratic model jointly trained with a neural network, with a similar two-part framework as GANNM), black-box models (neural network and random forest). In the next section, we will compare the performance of GANNM in interpretability with other interpretable models and with two post hoc black-box explainers that are based on the most accurate black-box models found in this predictive accuracy comparison.

We report the Mean Absolute Error (MAE) of models evaluated on the test set in Table 4. Results show that the black-box models have the best predictive performance (lowest MAEs), and interpretable models with no interactions have the worst predictive performance. Interpretable models with interactions fall in the middle since they both have the linearly additive part for interpretability and features’ interactions to ensure satisfying predictive performance. Meanwhile, GANNM is more accurate than GA2M since GA2M’s interactions are only pairwise and selected via heuristics. In contrast, GANNM’s interactions are full interactions from all nonbudget features and are jointly trained with GAM using a global objective function. In summary, GANNM, while maintaining interpretability, achieves higher predictive accuracy compared with existing interpretable models.

Table 4. Comparison of Predictive Performance (MAE) of GANNM Against Existing Models

<table><tr><td colspan="4">Interpretable (with interactions)</td><td colspan="2">Interpretable(no interactions)</td><td colspan="2">Black-box</td></tr><tr><td>GANNM</td><td>GA2M(Coull et al. 2001)</td><td>Factor-by-curve(Lou et al. 2013)</td><td>Linear-quadratic + NN</td><td>GAM(Lou et al. 2012)</td><td>Linear-quadratic</td><td>Neural network</td><td>Random forest</td></tr><tr><td>5,608</td><td>6,806</td><td>7,037</td><td>8,406</td><td>7,327</td><td>7,911</td><td>4,619</td><td>4,872</td></tr></table>

## 6.2. Response Curves Interpretation

The response curves obtained from GANNM are plotted in Figure 4. Each curve represents the increase in customer traf<sup>fi</sup>c (response) as a function of the daily budget in a given campaign category. The x-axis shows the average budget for each day of the campaign (reported in 10,000 RMB). The y-axis shows the marginal impact on customer traf<sup>fi</sup>c (reported in the increase of customer traf<sup>fi</sup>c). The curves follow different shapes that cannot be obtained with simple prior assumptions.

For peak period campaigns with sales and experience-incentives (the <sup>fi</sup>rst plot in Figure 4), the campaign budget has a slowly and steadily increasing impact on customer traf<sup>fi</sup>c. To generate an increase of 4,000 customer visits, campaign budgets need to reach 100,000 RMB (about 15,000 US dollars). In contrast, for peak period campaigns with experience-incentives only (the second plot in Figure 4), there is a sharp increase in customer traf<sup>fi</sup>c (up to 4,500) for smaller amounts of budget (below 20,000 RMB), but then the effect saturates. This shows that campaigns with experience-incentives are more ef<sup>fi</sup>cient than those with both sales and experience-incentives during the peak periods. On the other hand, the plateau in the response curve for peak period campaigns with experience-incentives only suggests that malls should avoid overinvesting in this type of campaigns. For off-peak period campaigns with sales-incentives only (the third plot in Figure 4), the impact of budget spending is also steadily increasing, but at a lower rate compared with peak period campaigns. Even with a daily budget of 100,000 RMB, the customer traf<sup>fi</sup>c only increases by less than 1,200. Similar to peak periods, we observe that for off-peak periods, campaigns with experienceincentives only are more effective than campaigns with sales-incentives (the fourth plot in Figure 4): the impact on customer traf<sup>fi</sup>c sharply increases with the daily budget, and with a daily budget of 50,000, the malls can expect an increase in traf<sup>fi</sup>c by about 7,500. Overall, customers are more likely to be drawn by experience than sales-incentives to visit the malls, and the contrast is more salient in off-peak periods.

For major online promotion days (the <sup>fi</sup>fth plot in Figure 4), we observe that as the budget increases, the plot stays <sup>fl</sup>at initially, then increases steeply. This suggests that without a suf<sup>fi</sup>cient campaign budget (i.e., daily budget lower than 30,000), the mall does not see an increase in customer traf<sup>fi</sup>c during this period. On the other hand, a steep rise in traf<sup>fi</sup>c occurs once the daily budget reaches a suf<sup>fi</sup>cient amount (i.e., larger than 30,000). These results imply that major online promotions could also present opportunities for malls once they spend an adequate amount of campaign budget to attract customers.

## 6.3. Comparison in Interpretability

We have demonstrated that GANNM has superior performance in predictive accuracy to the interpretable models and that its accuracy is only lower than the black-box models by a small scale. This indicates that whereas GANNM achieves interpretability, predictive accuracy is not much reduced as a result. In this section, we evaluate GANNM on the interpretability dimension. Since the black-box models cannot be used to interpret the insights or to optimize the budget allocation, we will compare GANNM against other interpretable models and black-box explainers using the post hoc explanation approach.

6.3.1. Interpretable Baselines. The <sup>fi</sup>rst baseline is a linear-quadratic model since it is widely adopted, easy to construct, and serves as the basis of a series of interpretable models (Molnar 2019). In addition, this model has been adopted in many prior works in learning marketing effectiveness, where users can incorporate their assumptions on the shape of the response curves (Bass et al. 2007, Fischer et al. 2011). In the linear-quadratic model, we assume that the response functions are linear combinations of the <sup>fi</sup>rstorder terms and quadratic terms of daily budget for each category of campaigns, as speci<sup>fi</sup>ed in Equation (11). We also experimented with including higher-order terms of budget and found this model with quadratic terms to have the best goodness-of-<sup>fi</sup>t on the validation set:

Figure 4. (Color online) Response Curves Obtained from GANNM  
![](/api/attachments/59ZDPZFB/fulltext/images/dd7275fbe4314e1ce012980533687cae42240fb8c9ed37ea9d5dc9f5291d8f07.jpg)

![](/api/attachments/59ZDPZFB/fulltext/images/105141b94a1bbca073e62e19c1743ebdc75e0102a00f62b7bbd37868cf4e4768.jpg)

![](/api/attachments/59ZDPZFB/fulltext/images/6c0ab50127dd6bae6d01eb99870ad7e653324008aaf7b39dea27fabbad1d2573.jpg)

![](/api/attachments/59ZDPZFB/fulltext/images/04ac9f6c0ad72f0d3499121306bb4856072929e32908189ea340c0a4bd10eed1.jpg)

![](/api/attachments/59ZDPZFB/fulltext/images/0987889f7aa988a7589dc960902b99ecf0ebe8d5e8f11727a19c783964aa3f8a.jpg)

$$
\mathrm{Traffic} _ {i} = \sum_ {j = 1} ^ {5} \left(\beta_ {j} \times m _ {j} ^ {(i)} + \gamma_ {j} \times (m _ {j} ^ {(i)}) ^ {2}\right) + \alpha \times \mathbf {x} ^ {(i)} + \epsilon_ {i}.\tag{11}
$$

Here, $m _ { j } ^ { ( i ) }$ and $\mathbf { x } ^ { ( i ) }$ are the same as de<sup>fi</sup>ned in Section $5 ;$ and $\beta _ { j }$ and $\gamma _ { j }$ capture the effects of campaign spending on the mall traf<sup>fi</sup>c for each campaign category. The model was trained on the training data. The coef<sup>fi</sup>- cients and testing performance are reported in Online Appendix C. We plot the response curves for each campaign category estimated from the baseline model in Figure 5.

In addition, we run another state-of-the-art interpretable model, GA2M, a generalized additive model with multiple pairwise interactions. We <sup>fi</sup>nd that, in contrast to GANNM, GA2M produces jumpy and discontinuous shape functions that will be highly unrealistic and unreliable in practice. Details about GA2M and its shape functions are reported in the online appendix.

We also examined the response curves provided by the linear-quadratic model with a neural network interactions part. The plots are reported in the online appendix. We observe that for this benchmark model, although the predictive performance is improved, as shown in Table 4, the shapes of the curves are largely similar to the baseline linear-quadratic model, since they are both heavily constrained by the preassumed (and possibly wrong) functional forms.

6.3.2. Post hoc Explanations. We also compare the performance of GANNM with post hoc explanation methods, which build accurate black-box models <sup>fi</sup>rst and then try to produce interpretations. Since we have found from Table 4 that neural network is the most accurate model among the various benchmarks we tried, we generate explanations based on this model. First, we use the knowledge distillation method in Tan et al. (2018) and choose GAM as the interpretable model. The idea of knowledge distillation is to use the output of the black-box model to inform the training of an interpretable model. The response curves for each campaign category estimated from this baseline model, which we label as distilled GAM, are shown in Figure 6.

The second method is a widely used post hoc explanation method, SHAP (Lundberg and Lee 2017), which computes a Shapley value for each feature in an instance. Shapley value is the average marginal contribution of a feature value across all possible coalitions of features. However, SHAP does not provide a continuous curve as it computes Shapley values for each feature in an instance. We provide a more detailed description in the online appendix.

Figure 5. (Color online) Response Curves from the Linear-Quadratic Model  
![](/api/attachments/59ZDPZFB/fulltext/images/3607e5faf42b7a5e0931286179c088efdd50d753c2fe3aa1bd7d9a60f1d06dd4.jpg)

![](/api/attachments/59ZDPZFB/fulltext/images/3758594cc15c45984ac805d2b38c2cbbc6b5db81968ba3f74e3509edb6a89700.jpg)

![](/api/attachments/59ZDPZFB/fulltext/images/f1fe2b538d7134dd96d7279b3b66a32881cf4de8f74bf0f739dfd3069ff270ce.jpg)

![](/api/attachments/59ZDPZFB/fulltext/images/065f8f72379cea66b53354d43deb6bd520647e0c031241d820379a6dfd81c050.jpg)

![](/api/attachments/59ZDPZFB/fulltext/images/43695b96c219f01b61b38079c690ba1ced343167c14f949eb5b144fb86e9e391.jpg)

6.3.3. Comparing the Shape Functions. Comparing the shape functions obtained from the linearquadratic model and distilled GAM with those from GANNM, we observe that these response curves are similar in many aspects to those from GANNM. However, where they differ, we <sup>fi</sup>nd that the response curves from GANNM are more accurate. The most salient issue with the response curves from the linearquadratic model and distilled GAM is that they indicate mall traf<sup>fi</sup>c will decrease from further increases in the budget beyond certain thresholds for multiple types of campaigns. In contrast, GANNM consistently shows a nondecreasing trend in mall traf<sup>fi</sup>c as the budget increases. A downward curve showing negative impact could indicate that the model does not accurately capture the actual relationship between budget and mall traf<sup>fi</sup>c and could potentially mislead managerial decisions. Since the ground truth of the response curves is unobservable, we referred to human experts to examine the response curves. Mall managers and domain experts who provided the data have unanimously found the curves from GANNM to be more accurate representations. Industry experts report that according to their observations, the effect of mall campaigns typically increases as the campaign budget increases, with various speeds depending on the effectiveness of the campaigns. It can level off in some instances but very rarely turn downward as spending increases. Even if such extreme cases may exist as outliers in particular malls, since the response curves capture the average effect across 25 malls, a downward trend in traf<sup>fi</sup>c as budget increases is highly unlikely.

The differences in the curves are likely attributed to the limitations of these two benchmark models compared with GANNM. The linear-quadratic model uses preassumed functional forms to characterize the response curves, which does not always align with the ground truth. GANNM, on the other hand, is entirely data driven and does not rely on assumptions of the shape functions, thus incurring no biases in characterizing the relationships. Meanwhile, distilled GAM is trained with the output of the neural network model as the target variable, which inevitably introduces distortions from the true value of the target variable. Although this distortion is purposely injected to better train the distilled GAM, it does lose or alter the original information from the true target variable. Overall, this qualitative comparison of the shape functions shows that GANNM likely captures the true relationship more accurately and that in our context, this interpretability approach outperforms other benchmarks, including post hoc explainers.

6.3.4. Quantifying Interpretability of Shape Functions. In addition to the qualitative inspection of the shape functions, we also employ commonly used quantitative criteria to further evaluate the interpretability per formance across models. Although there is no single standard for evaluating interpretability, various criteria have been proposed to characterize whether the interpretations demonstrate desirable attributes, such as completeness (Gilpin et al. 2018), robustness (Alvarez-Melis and Jaakkola 2018), the accuracy of the feature importance estimates (Hooker et al. 2019), and so on. Among these criteria, robustness is likely the most relevant to our context since it evaluates how sensitive the predictions are to local variations in the predictors. The local Lipschitz continuity measure is a commonly used metric of robustness. It measures the relative scale of changes in the prediction output with respect to the input (Alvarez-Melis and Jaakkola 2018):

$$
\hat {L} (x _ {i}) = \arg \max _ {x _ {j} \in B _ {\epsilon} (x _ {i})} \frac {\| f (x _ {i}) - f (x _ {j}) \| _ {2}}{\| x _ {i} - x _ {j} \| _ {2}},\tag{12}
$$

where $B _ { \epsilon } ( x _ { i } )$ is a ball of radius  centered at $x _ { i }$ and we set $\epsilon = 0 . 1$ . We uniformly sampled budgets with a step size of 0.1, computed the largest variation in the increase in the traf<sup>fi</sup>c from the shape functions, and then plotted the distribution of the local Lipschitz continuity measure in Figure 7. Note that the boxplots with smaller values and less variation represent better robustness.

Figure 6. (Color online) Response Curves from the Distilled GAM  
![](/api/attachments/59ZDPZFB/fulltext/images/4b7baad658807ce9dd730af44c873801f4a47c0d9740657b86924b358b7b1387.jpg)

![](/api/attachments/59ZDPZFB/fulltext/images/5dfac54cc21a772c3292f12efb833aa7d8490b12d103cd4376acab1b360e5785.jpg)

![](/api/attachments/59ZDPZFB/fulltext/images/7786dfcfcfc07cd14f7ab732b7e45907cbdfcef76accf7623007c42902e3b9f5.jpg)

![](/api/attachments/59ZDPZFB/fulltext/images/ce7d029ab258c09c64ac6a8e8cad71526a6eb0d78413c7fa1c46444e5874d4e7.jpg)

![](/api/attachments/59ZDPZFB/fulltext/images/315de9606cfb79752f10ce1e534007e76652c548fa8c9ae9f95e47705b0ffb2c.jpg)

Figure 7. (Color online) Local Lipschitz Continuity Evaluation  
![](/api/attachments/59ZDPZFB/fulltext/images/00b9f7c0f94ef7f251a2352da536b7f4248960b6b8782a3e90a135590137bb2d.jpg)

Here we compare the robustness of GANNM with the linear-quadratic model, GA2M, and distilled GAM. The relative position of the boxplots in Figure 7 demonstrates that GANNM, the linear-quadratic model, and distilled GAM outperform GA2M in the robustness comparison. This con<sup>fi</sup>rms what we have observed from the visual inspection of the shape functions. The shape functions from GANNM, linearquadratic model, and distilled GAM are much smoother, whereas GA2M exhibits multiple sharp jumps in the shape functions, as shown in Figure 10 in the online appendix.

To further validate the results and compare the three approaches, in the next section, we compute the optimal budget allocation based on the response curves from GANNM and the baseline model, respectively, to show the customer traf<sup>fi</sup>c improvement each model can achieve.

## 7. Budget Allocation Based on the Response Curves

Our <sup>fi</sup>ndings so far have demonstrated that GANNM shows a higher level of predictive accuracy and provides response curves with better performance in interpretability than benchmarks. In this section, we aim to apply the response curves obtained from GANNM to optimize budget allocations across various types of campaigns and to compare the projected increase in mall traf<sup>fi</sup>c. This optimization analysis serves two main goals. First, it con<sup>fi</sup>rms that the optimization results from GANNM show better performance than benchmarks. Second, this optimization analysis connects the machine learning objectives with the practical objectives and highlights our contributions. GANNM solves the practical task of accurately representing the response curves from various types of campaigns and the optimized budget allocations based on such curves, which are projected to improve the mall traf<sup>fi</sup>c, a KPI of high practical relevance to mall managers.

## 7.1. Budget Allocation Using Shape Functions

In line with industry conventions, the budget allocation process in our optimization analysis is completed through two steps: (1) allocating the total budget to the <sup>fi</sup>ve categories of campaigns, determining the total budget of campaigns within each category; and (2) allocating the budget to campaigns within each category.<sup>5</sup> B oth optimization steps are achieved through grid search along the respective response curve s learned from the data. Since the shape functions are trained on data from the 25 malls, we use the same shape functions for all these malls, but perform the optimization for each mall respectively, given their different budgets and campaign schedules. We then evaluate how the optimized customer traf<sup>fi</sup>c lift changes with the total budget allocated to the campaign category j across all malls. The details about the algorithms for the optimization steps are reported in the online appendix.

Following the optimization steps outlined previously, we compute the budget allocation using shape functions $\{ s _ { j } ( m _ { j } ^ { ( i ) } ) \} _ { j = 1 } ^ { 5 }$ derived from GANNM and baselines, and compare them with the budget allocation that the malls currently adopt. We report the total and the daily budget that malls allocate to each type of campaigns in Table 5. The values are averaged across 25 malls for each category. We report the current campaign budget allocation in the “original” column and report the optimization results derived from GANNM, the linear-quadratic model, and distilled GAM in the next three columns, respectively. All values reported here are measured in 10,000 RMB.

We observe that the optimal allocations from GANNM and the linear-quadratic model are more similar, and they both differ signi<sup>fi</sup>cantly from the distilled GAM results. For example, both GANNM and the linear-quadratic model recommend signi<sup>fi</sup>cantly reducing the budget allocated to peak period cam paigns with sales and experience-incentives and holding budget for off-peak period campaigns with experience only either slightly increased or largely the same. In contrast, the results from distilled GAM recommend holding budget allocated to peak period campaigns with sales and experience-incentives largely the same, while signi<sup>fi</sup>cantly reducing the budget allocated to off-peak period campaigns with experience-incentives only. Where GANNM and the linear-quadratic model differ, distilled GAM tends to go in the same direction as the linear-quadratic model. For example, GANNM recommends reducing the budget for peak period campaigns with experience-incentives only, whereas both the linear-quadratic model and distilled GAM suggest the opposite. In addition, the linear-quadratic model recommends allocating a much larger proportion of budget to online promotion period campaigns than GANNM, whereas distilled GAM suggests allocating an even larger proportion for this category of campaigns.

Table 5. Optimal Budget Allocations Derived from Different Methods

<table><tr><td rowspan="2">Campaign type</td><td colspan="2">Original</td><td colspan="2">GANNM</td><td colspan="2">Linear-quadratic</td><td colspan="2">Distilled GAM</td></tr><tr><td>total</td><td>Daily</td><td>total</td><td>Daily</td><td>total</td><td>Daily</td><td>total</td><td>Daily</td></tr><tr><td>Peak period campaigns with sales and experience incentive</td><td>75.38</td><td>1.37</td><td>13.10</td><td>0.24</td><td>0.00</td><td>0.00</td><td>75.17</td><td>1.34</td></tr><tr><td>Peak period campaigns with experience incentive only</td><td>27.85</td><td>1.60</td><td>15.95</td><td>0.92</td><td>37.22</td><td>2.14</td><td>31.10</td><td>1.79</td></tr><tr><td>Off-peak period campaigns with sales incentive only</td><td>8.61</td><td>1.58</td><td>13.19</td><td>2.43</td><td>9.41</td><td>1.73</td><td>13.10</td><td>2.69</td></tr><tr><td>Off-peak period campaigns with experience incentive only</td><td>131.40</td><td>1.35</td><td>189.54</td><td>1.94</td><td>115.98</td><td>1.19</td><td>13.22</td><td>0.21</td></tr><tr><td>Online promotion period campaigns</td><td>19.54</td><td>1.79</td><td>30.39</td><td>2.78</td><td>100.23</td><td>9.18</td><td>129.87</td><td>11.81</td></tr><tr><td>Campaign effect (increase in traffic)</td><td colspan="2">7,362</td><td colspan="2">8,186</td><td colspan="2">7,677</td><td colspan="2">7,437</td></tr><tr><td></td><td colspan="2"></td><td colspan="2"> $\uparrow 11.2\%$ </td><td colspan="2"> $\uparrow 3.2\%$ </td><td colspan="2"> $\uparrow 1.0\%$ </td></tr></table>

Overall, the GANNM-based budget allocation suggests that malls should reduce the budget for campaigns in peak periods and increase that for off-peak periods, but less drastically than suggested by the linear-quadratic model. In contrast, distilled GAM recommends reallocating the budget from off-peak periods to online promotion period campaigns while keeping almost the same budget for peak period campaigns. Currently, the malls are allocating 39% of the total annual budget to peak period campaigns and 53% to off-peak period campaigns. In contrast, GANNM recommends changing these proportions to 11% and 77%, respectively. One possible explanation is that in peak periods, customer traf<sup>fi</sup>c is already at a high level compared with off-peak periods; thus, there is less room for improvement, and malls are underinvesting in off-peak period campaigns. Therefore, there is more potential for customer traf<sup>fi</sup>c increases for off-peak period campaigns. A similar phenomenon is also observed in Simester et al. (2009), which recommends businesses to increase their marketing budget to customers with more room to increase their purchases.

## 7.2. Evaluating the Budget Allocations

In this section, we further evaluate the effectiveness of the proposed budget allocations in increasing the customer traf<sup>fi</sup>c to the malls and compare the solution computed from GANNM with the ones computed from the baselines.

To evaluate the customer traf<sup>fi</sup>c lift for a mall on a given day, we need to estimate the resulting mall traf-<sup>fi</sup>c from running this campaign with the prescribed budget, holding all other features the same as the original data. Since the ground truth of actual customer traf<sup>fi</sup>c from the proposed budget allocation is unknown, we need an accurate predictive model to produce a proxy for the actual customer traf<sup>fi</sup>c, following the proposed budget allocations. Note that we cannot use GANNM for this purpose, or any of the baseline models we are comparing GANNM with in this analysis, since the estimations would likely be biased in favor of the selected model. Instead, we need a third party model to provide a fair estimation of the actual customer traf<sup>fi</sup>c, following the proposed budget allocations. We choose the most accurate model from Table 4, a fully connected feed-forward neural network with four hidden layers. This neural network model has an MAE of 4,619 and an absolute percentage error (de<sup>fi</sup>ned as the mean absolute error divided by the mean of the total number of customers) of 10.8%, the lowest among the alternative models.

Then we substitute the original budget with the optimized budget reported in Table 3, computed from shape functions obtained by the GANNM and the baseline models, respectively, and send these proposed budget allocations to the neural network model to get the prediction of customer traf<sup>fi</sup>c. We report the increase in customer traf<sup>fi</sup>c from campaigns for each of the three solutions, as computed from Equation (13):

$$
\frac {\sum_ {i \in \tau_ {1}} y _ {i}}{| \tau_ {1} |} - \frac {\sum_ {i \in \tau_ {0}} y _ {i}}{| \tau_ {0} |},\tag{13}
$$

where $y _ { i }$ is customer traf<sup>fi</sup>c for instance $i ,$ and $\tau _ { 1 }$ and $\tau _ { 0 }$ are the set of days with and without campaigns, respectively. The average increase in customer traf<sup>fi</sup>c from the original budget allocation is estimated at 7,362. The customer traf<sup>fi</sup>c increases from campaign budget allocations computed from GANNM, the linear-quadratic model, and distilled GAM are estimated to be 8,186, 7,599, and 7,437, corresponding to 11.2%, 3.2%, and 1.0% increases from the original allocation, respectively. These results con<sup>fi</sup>rm that the solution based on GANNM achieves a much higher customer traf<sup>fi</sup>c increase than the original allocation and the solutions from benchmark models.

## 8. Conclusion and Implications

## 8.1. Summary of Findings and Managerial Implications

Evaluating the effectiveness of marketing campaigns is an important and challenging issue for malls (Marketing Science Institute 2018). We use a newly available data set of daily observations on customer traf<sup>fi</sup>c to malls and detailed campaign descriptions to build a novel machine learning model and provide new insights. This new model, GANNM, achieves better interpretability and higher prediction accuracy in characterizing how the impact of budget spending on customer traf<sup>fi</sup>c differs across campaign types. Furthermore, the optimal budget allocation derived from GANNM improves customer traf<sup>fi</sup>c lift by 11%, a signi<sup>fi</sup>cant improvement compared with the 3% lift from the baseline interpretable model with preassumed functional forms of response curves and 1% lift from a post hoc explanation method.

The <sup>fi</sup>ndings from the response curves obtained from GANNM also provide helpful guidance for managerial practices. Our results indicate that malls should focus more on campaigns that enhance customers’ shopping experience, especially during the off-peak period. Campaigns that enhance customers’ shopping experience could be more effective in increasing customer traf<sup>fi</sup>c than campaigns with sales-incentives only. This <sup>fi</sup>nding contributes to an emerging stream of literature on omnichannel retailing that shows the value of the of<sup>fl</sup>ine channel in enhancing customers’ shopping experience (Brynjolfsson et al. 2013, Gao and Su 2017). For example, the French beauty brand Sephora uses augmented reality to allow customers to test makeup virtually. To expand of<sup>fl</sup>ine, the London fashion store, Missguided, has created a <sup>fl</sup>agship store inspired by a TV studio, with huge screens that stream customer-generated social media content (Palaci et al. 2019). Our results provide empirical evidence showing that this recent trend of employing novel approaches for enhancing customer experience in physical stores can effectively encourage customers to visit malls.

In addition, although most of the existing campaign budget of a mall is currently allocated to peak period campaigns, our results imply that the marginal bene<sup>fi</sup>t is smaller than off-peak period campaigns. This implies that mall managers should increase marketing spending to areas that are likely overlooked before and avoid over-crowding budget to campaigns during times with high levels of competition and are likely already over-marketed.

With the increasing popularity of e-commerce, our <sup>fi</sup>ndings also have implications for how malls should adjust their campaigns to account for the competition from online businesses. Our results suggest that online promotions could also create opportunities for of<sup>fl</sup>ine businesses—investing in campaigns in the major online promotion periods could signi<sup>fi</sup>cantly increase customer traf<sup>fi</sup>c for malls, given suf<sup>fi</sup>cient investment in campaigns to raise customer awareness.

The <sup>fi</sup>ndings from this study also have managerial implications for of<sup>fl</sup>ine retailers undergoing digital transformation. In particular, we have shown that using new AI-chip-embedded sensors, malls can collect more timely and detailed data on customer traf<sup>fi</sup>c for a more accurate evaluation of the effectiveness of marketing campaigns. Of<sup>fl</sup>ine retailers can explore additional ways to adopt new digital technologies to collect better quality data and gain business insights from data analysis.

## 8.2. Methodological Innovation and Generalizability

Our proposed GANNM successfully combines the high predictive accuracy of black-box models with the understandability of interpretable models to inform managerial decisions. Whereas black-box models such as deep neural networks could have higher predictive powers, the lack of interpretability of their decisionmaking processes has hindered these models’ applications. At the same time, having high accuracy is also essential. Compared with alternative interpretable models, GANNM shows signi<sup>fi</sup>cantly better performance. In addition, by relaxing the constraint on functional forms, GANNM captures the underlying patterns in the data more accurately and provides unique insights.

GANNM can potentially be applied to assist decision making in various areas that require accurately evaluating returns on investment using large and complex data, to provide accurate results and yield interpretable managerial insights. Compared with noninterpretable machine learning models, GANNM does not sacri<sup>fi</sup>ce predictive accuracy signi<sup>fi</sup>cantly, and the interpretability advantage outweighs the small decreases in accuracy.<sup>6</sup> It can easily be adapted to the online context, fo example, to examine the return on online advertising spending. Although we mainly focus on customer traf<sup>fi</sup>c since it is the most relevant KPI for malls, the model can be easily adapted to different contexts of study with other relevant KPIs, such as sales and click-through rate in an online context. In addition, a similar methodology can be applied to study the effect of marketing mix variables such as pricing schemes, recommendations, and services.

## 8.3. Future Extensions

Our study also presents several areas for interesting future extensions. For example, future studies can collect more detailed data to examine the increases in customer traf<sup>fi</sup>c to each tenant store, for each category of mall campaigns. This can potentially provide additional information that breaks down the total increase in traf<sup>fi</sup>c to a more granular impact for each tenant store and inform tenant store managers’ decision making. Although this study mainly focuses on the short-term marketing effectiveness for malls, future studies can easily extend our model to incorporate additional explanatory variables and capture the longterm impact of different categories of campaigns. Future research can also collect longer panels to have training data spanning multiple years to better capture seasonal patterns and the effects of holidays at different times of the year. Although the malls we study do not have an online channel, future studies can extend our prediction model and apply it to study omnichannel retailers. For example, additional analyses on how campaigns convert of<sup>fl</sup>ine visits to online sales could enhance the understanding of the spillover effects of of<sup>fl</sup>ine campaigns on online traf<sup>fi</sup>c and sales.

## Endnotes

<sup>1</sup> For this additional analysis, we collect annual rents and traffic data from 122 malls from China over a five-year period (2015\~2019) and find that a 1% increase in mall traffic is associated with a 0.605% increase in rent revenue. Details about this analysis are provided in Online Appendix A.

<sup>2</sup> Note that a mall does not bear the cost of price markdowns for a tenant store’s promotions since the stores operate independently. In fact, the rent paid by tenant stores to the malls usually accounts for around 10\~15% of the store’s revenue; then the malls typically allocate around 5\~10% of their rent revenue for campaign budget. This means that the campaign budget accounts for about 0.5\~1.5% of tenant store revenue. Given the scale of these numbers, it is not possible for malls to use this budget to cover price discounts for individual stores.

<sup>3</sup> We also trained another baseline model where we substituted the GAM part of the model with a linear baseline part, with preassumed functional forms of response curves, to demonstrate the advantage of using a GAM to directly learn response curves from data.

<sup>4</sup> We also experimented with splitting the data by malls, where we used the data from 24 malls out of 25 malls, across the entire two year time span as the training data and use all the observations from the remaining one mall as the testing data, and rotate the test data across 25 malls. Results are shown in the online appendix, and these results are largely similar to our main findings.

<sup>5</sup> For this optimization analysis, we hold all the other campaign related factors the same and focus on demonstrating the projected mall traffic increase by adjusting the budget allocation across different types of campaigns. We have also conducted an additional sensitivity analysis to examine whether varying the duration of the campaign influences our optimization results in a significant way. We found that varying campaign duration leads to a much smaller change in mall traffic than optimizing budget allocations across campaign categories.

<sup>6</sup> We expect the scalability of GANNM to be positioned somewhere between neural network models and simple linear models, since GANNM is essentially a combination of the two (the generalized additive part is a linear addition of basis functions). We anticipate that the model design in allocating features across the GAM part and the neural network part to be an important factor that influences the performance of GANNM.

## References

Aïvodji U, Arai H, Fortineau O, Gambs S, Hara S, Tapp A (2019) Fairwashing: The risk of rationalization. Proc. Internat. Conf. Ma chine Learn., vol. 97 (Long Beach, CA), 161–170.

Alvarez-Melis D, Jaakkola TS (2018) On the robustness of interpretability methods. ICML Workshop Human Interpretability Machine Learn (Stockholm).

Bass FM, Bruce N, Majumdar S, Murthi B (2007) Wearout effects of different advertising themes: A dynamic Bayesian model of the advertising-sales relationship. Marketing Sci. 26(2):179–195.

Bel-Bachir I, Devillard S, Sawaya A, Valachovicova I (2019) Boosting mall revenues through advanced analytics. McKinsey & Company (January 18), https://www.mckinsey.com/industries/retail/ourinsights/boosting-mall-revenues-through-advanced-analytics.

Bloch PH, Ridgway NM, Dawson SA (1994) The shopping mall as consumer habitat. J. Retailing 70(1):23–42.

Brynjolfsson E, Hu YJ, Rahman MS (2013) Competing in the age of omnichannel retailing. MIT Sloan Management Rev. 54(4):23–29.

Bues M, Steiner M, Staf<sup>fl</sup>age M, Krafft M (2017) How mobile in-store advertising in<sup>fl</sup>uences purchase intention: Value drivers and mediating effects from a consumer perspective. Psych. Mar keting 34(2):157–174.

Carroll JD, Green PE, DeSarbo WS (1979) Optimizing the allocation of a <sup>fi</sup>xed resource: A simple model and its experimental test. J. Marketing 43(1):51–57.

Caruana R, Lou Y, Gehrke J, Koch P, Sturm M, Elhadad N (2015) Intelligible models for healthcare: Predicting pneumonia risk and hospital 30-day readmission. Proc. 21st ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (Sydney, Australia) 1721–1730.

Chen M, Chen ZL (2015) Recent developments in dynamic pricing research: Multiple products, competition, and limited demand information. Production Oper. Management 24(5):704–731

Cooper LG, Baron P, Levy W, Swisher M, Gogos P (1999) Promocast<sup>TM</sup>: A new forecasting method for promotion planning. Marketing Sci. 18(3):301–316.

Coull BA, Ruppert D, Wand M (2001) Simple incorporation of inter actions into additive models. Biometrics 57(2):539–545.

Danaher PJ, Smith MS, Ranasinghe K, Danaher TS (2015) Where, when, and how long: Factors that in<sup>fl</sup>uence the redemption of mobile phone coupons. J. Marketing Res. 52(5):710–725.

De Boor C (1978) A Practical Guide to Splines, vol. 27 (Springer-Verlag, New York).

Doyle P, Saunders J (1990) Multiproduct advertising budgeting. Marketing Sci. 9(2):97–113.

Fischer M, Albers S, Wagner N, Frie M (2011) Practice prize winner-dynamic marketing budget allocation across countries, products, and marketing activities. Marketing Sci. 30(4): 568–585.

Gao F, Su X (2017) Online and of<sup>fl</sup>ine information for omnichannel retailing. Manufacturing Service Oper. Management 19(1):84–98.

Ghose A, Li B, Liu S (2019) Mobile targeting using customer trajectory patterns. Management Sci. 65(11):5027–5049.

Gijsenberg MJ (2017) Riding the waves: Revealing the impact of intrayear category demand cycles on advertising and pricing effectiveness. J. Marketing Res. 54(2):171–186.

Gilpin LH, Bau D, Yuan BZ, Bajwa A, Specter M, Kagal L (2018) Explaining explanations: An overview of interpretability of machine learning. 2018 IEEE 5th Internat. Conf. Data Sci. Advanced Analytics (DSAA) (IEEE, Turin, Italy), 80–89.

Guisan A, Edwards TC Jr, Hastie T (2002) Generalized linear and generalized additive models in studies of species distributions: Setting the scene. Ecological Model. 157(2–3):89–100.

Hall JM, Kopalle PK, Krishna A (2010) Retailer dynamic pricing and ordering decisions: Category management vs. brand-by-brand approaches. J. Retailing 86(2):172–183.

Hastie T, Tibshirani R (1987) Generalized additive models: Some applications. J. Amer. Statist. Assoc. 82(398):371–386.

Hogberg J, Shams P, W¨ astlund E (2019) Gami¨ <sup>fi</sup>ed in-store mobile marketing: The mixed effect of gami<sup>fi</sup>ed point-of-purchase advertising. J. Retailing Consumer Services 50:298–304.

Hooker S, Erhan D, Kindermans PJ, Kim B (2019) A benchmark for interpretability methods in deep neural networks. Advances in Neural Inform. Processing Systems 32, 9737–9748.

Iyer G, Kuksov D (2012) Competition in consumer shopping experi ence. Marketing Sci. 31(6):913–933.

Jindal P, Zhu T, Chintagunta P, Dhar S (2020) Marketing-mix response across retail formats: The role of shopping trip types. J. Marketing 84(2):114–132.

Keller WI, Deleersnyder B, Gedenk K (2019) Price promotions and popular events. J. Marketing 83(1):73–88.

Kingma DP, Ba J (2014) Adam: A method for stochastic optimization. Preprint, submitted December 22, https://arxiv.org/abs/ 1412.6980v3.

Lam SY, Vandenbosch M, Hulland J, Pearce M (2001) Evaluating promotions in shopping environments: Decomposing sales response into attraction, conversion, and spending effects. Marketing Sci. 20(2):194–215.

Liu Y, Li KJ, Chen H, Balachander S (2017) The effects of products aesthetic design on demand and marketing-mix effectiveness: The role of segment prototypicality and brand consistency. J. Marketing 81(1):83–102.

Lou Y, Caruana R, Gehrke J (2012) Intelligible models for classi<sup>fi</sup>cation and regression. Proc. 18th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (Beijing), 150–158.

Lou Y, Caruana R, Gehrke J, Hooker G (2013) Accurate intelligible models with pairwise interactions. Proc. 19th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (Chicago), 623–631.

Lundberg SM, Lee SI (2017) A uni<sup>fi</sup>ed approach to interpreting model predictions. Adv. Neural Inform. Processing Systems, 4768– 4777.

Marketing Science Institute (2018) 2018–2020 research priorities. https://www.msi.org/research/2018-2020-research-priorities/.

Molnar C (2019) Interpretable Machine Learning. christophm.github. io/interpretable-ml-book/.

Narayanan S, Desiraju R, Chintagunta PK (2004) Return on investment implications for pharmaceutical promotional expenditures: The role of marketing-mix interactions. J. Marketing 68(4):90–105.

Nordfalt J, Lange F (2013) In-store demonstrations as a promotion¨ tool. J. Retailing Consumer Services 20(1):20–25.

Palaci F, Sedra R, Rao A (2019) Digital-native retailers are giving physical stores a radical makeover. Strategy Business (January 18), https://www.strategy-business.com/article/Digital-Native-Retailers-Are-Giving-Physical-Stores-a-Radical-Makeover.

Peers Y, Van Heerde HJ, Dekimpe MG (2017) Marketing budget allocation across countries: The role of international business cycles. Marketing Sci. 36(5):792–809.

Ribeiro MT, Singh S, Guestrin C (2016) Why should I trust you?: Explaining the predictions of any classi<sup>fi</sup>er. Proc. 22nd ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (ACM, San Francisco), 1135–1144.

Ross AS, Hughes MC, Doshi-Velez F (2017) Right for the right reasons: Training differentiable models by constraining their explanations. Proc. 26th Internat. Joint Conf. Artificial Intelligence, 2662-2670.

Rudin C (2019) Stop explaining black box machine learning models for high stakes decisions and use interpretablemodels instead. Nature Machine Intelligence 180:206–215.

Simester D, Hu Y, Brynjolfsson E, Anderson ET (2009) Dynamics of retail advertising: Evidence from a <sup>fi</sup>eld experiment. Econom. Inquiry 47(3):482–499.

Slack D, Hilgard S, Jia E, Singh S, Lakkaraju H (2020) Fooling lime and shap: Adversarial attacks on post hoc explanation methods. Proc. AAAI/ACM Conf. AI Ethics Soc. (New York), 180–186.

Srivastava N, Hinton G, Krizhevsky A, Sutskever I, Salakhutdinov R (2014) Dropout: A simple way to prevent neural networks from over<sup>fi</sup>tting. J. Machine Learn. Res. 15(1):1929–1958.

Stein S (2019) Mall of America’s makers market. Forbes (December 26), https://www.forbes.com/sites/sanfordstein/2018/12/26/ mall-of-americas-makers-market/#3228ba28162b.

Swinyard WR (1993) The effects of mood, involvement, and quality of store experience on shopping intentions. J. Consumer Res. 20(2):271–280.

Tan S, Caruana R, Hooker G, Koch P, Gordo A (2018) Learning global additive explanations for neural nets using model distillation. Preprint, submitted January 26, https://arxiv.org/abs/1801.08640

Thibault L, Marie-Jeanne L, Christophe M, Xavier R, Detyniecki M (2019) The dangers of post-hoc interpretability: Unjusti<sup>fi</sup>ed counterfactual explanations. Proc. 28th Internat. Joint Conf. Arti ficial Intelligence (Macao, China).

Thomas L (2019) Offering shoppers new experiences isn’t helping as malls see tsunami of store closures, falling traf<sup>fi</sup>c. CNBC (April 15), https://www.cnbc.com/2019/04/15/malls-see-tsunami-ofstore-closures-as-foot-traf<sup>fi</sup>c-declines-further.html.

Verhoef PC, Lemon KN, Parasuraman A, Roggeveen A, Tsiros M, Schlesinger LA (2009) Customer experience creation: Determinants, dynamics and management strategies. J. Retailing 85(1):31–41.

Vidale M, Wolfe H (1957) An operations-research study of sales response to advertising. Oper. Res. 5(3):370–381.

Vitorino MA (2012) Empirical entry games with complementarities: An application to the shopping center industry. J. Marketing Res. 49(2):175–191.

Wake<sup>fi</sup>eld KL, Baker J (1998) Excitement at the mall: Determinants and effects on shopping response. J. Retailing 74(4):515–539.

Wang T (2018) Multi-value rule sets for interpretable classi<sup>fi</sup>cation with feature-ef<sup>fi</sup>cient representations. Proc. 32nd Internat. Conf. Neural Inform. Processing Systems, 10858–10868.

Wang T, Rudin C, Doshi-Velez F, Liu Y, Klamp<sup>fl</sup> E, MacNeille P (2017) A Bayesian framework for learning rule sets for interpretable classi<sup>fi</sup>cation. J. Machine Learn. Res. 18(1):2357–2393.

Warner EJ, Barsky RB (1995) The timing and magnitude of retail store markdowns: Evidence from weekends and holidays. Quart. J. Econom. 110(2):321–352.

Wood SN (2017) Generalized Additive Models: An Introduction with R (Chapman and Hall/CRC, Boca Raton, FL).

Wu J, Zhao H, Chen H (2021) Coupons or free shipping? Effects of price promotion strategies on online review ratings. Inform. Systems Res. 32(2):633–652.

Yang Y, Zeng D, Yang Y, Zhang J (2015) Optimal budget allocation across search advertising markets. INFORMS J. Comput. 27(2): 285–300.

Ye S, Aydin G, Hu S (2015) Sponsored search marketing: Dynamic pricing and advertising for an online retailer. Management Sci. 61(6):1255–1274.

Yiu CY, Xu SY (2012) A tenant-mix model for shopping malls. Eur. J. Marketing. 46(3-4):524–541.

Yohn DL (2017) Why retailers should retire holiday shopping season. Harvard Bus. Rev. (October 9), https://hbr.org/2017/10/ why-retailers-should-retire-holiday-shopping-season.

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites without the copyright holder's express written permission. Additionally, content may not be used with any artificial intelligence tools or machine learning technologies. However, users may print, download, or email articles for individual use.

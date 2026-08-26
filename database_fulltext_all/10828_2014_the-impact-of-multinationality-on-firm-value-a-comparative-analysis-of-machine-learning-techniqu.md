---
otero_id: 10828
otero_key: "YM3URWNE"
title: "The impact of multinationality on firm value: A comparative analysis of machine learning techniques"
authors: "Cemil Kuzey; Ali Uyar; Dursun Delen"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.11.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The impact of multinationality on <sup>fi</sup>rm value: A comparative analysis of machine learning techniques

Cemil Kuzey <sup>a</sup>, Ali Uyar <sup>a</sup>, Dursun Delen <sup>b,</sup>⁎

<sup>a</sup> Department of Management, Fatih University, Buyukcekmece, Istanbul 34500, Turkey

<sup>b</sup> Department of Management Science and Information Systems, Spears School of Business, Oklahoma State University, United States

## a r t i c l e i n f o

Article history: Received 12 November 2012 Received in revised form 31 October 2013 Accepted 8 November 2013 Available online 16 November 2013

Keywords: Machine learning Predictive analytics Decision trees Arti<sup>fi</sup>cial neural networks Sensitivity analysis Firm value Multinationality

## a b s t r a c t

In this study, the impact of multinationality (as measured by foreign sales ratio) and fourteen other <sup>fi</sup>nancial indicators on <sup>fi</sup>rm value (characterized by market capitalization and market-to-book ratio) for the period of 1997–2011 was investigated using two popular machine learning techniques: decision trees and arti<sup>fi</sup>cial neural networks. We divided the time period of 1997–2011 into two periods; 1997–2004 and 2005–2011 to investigate the robustness of results pre- and post-IFRS implementation. To determine the relative importance of factors as the predictors of <sup>fi</sup>rm value, <sup>fi</sup>rst, a number of classi<sup>fi</sup>cation models are developed; then, the information fusion based sensitivity analysis is applied to these classi<sup>fi</sup>cation models to identify the ranked order of the independent variables. Among the independent variables, multinationality was found to determine <sup>fi</sup>rm value only moderately. In addition to multinationality, other <sup>fi</sup>nancial characteristics such as <sup>fi</sup>rm size (as measured by natural logarithm of assets), leverage, liquidity, and pro<sup>fi</sup>tability were consistently found to be affecting <sup>fi</sup>rm value.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

In recent years, value relevance studies have attracted considerable attention from researchers of diverse backgrounds [1,13,31,38,39,65,87]. Those studies generally dealt with investigating how certain <sup>fi</sup>rm characteristics affect <sup>fi</sup>rm value. Financial characteristics and non-<sup>fi</sup>nancial characteristics (e.g., voluntary disclosures, adoption of <sup>fi</sup>nancial reporting standards, auditor type, ownership structure, multinationality, and corporate governance) were among the fundamental dimensions that these investigators had focused on.

Beside directly addressing the <sup>fi</sup>rm value, a large number of research studies focused on analyzing and potentially predicting bankruptcy as a means to identify characteristics (in term of <sup>fi</sup>nancial ratios) of successful/unsuccessful <sup>fi</sup>rms and their potential values [54]. A simple search on the topic “bankruptcy prediction” returns tens of thousands of studies. A vast majority of these studies differentiate themselves from those of others by using a somewhat unique set of <sup>fi</sup>nancial characteristics and/or employing a different set of prediction models (statistical or machine learning based) [2,42,57,64,72,89]. Though many of these studies are successful in predicting bankruptcy, they often fall short on identifying and explaining the characteristics that can be used as determinants of the firm value

This study aims to address speci<sup>fi</sup>cally the value relevance of international operations of multinational companies. Previously, some studies tested the in<sup>fl</sup>uence of multinationality on <sup>fi</sup>rm value albeit most of them were in developed countries [35]. While these works have examined the impact of multinationality in various countries, they may not fully capture the extent to which the degree of internationalization affects <sup>fi</sup>rm value in emerging/developing countries. Lee et al. [58] argue that the capital markets are less developed and ownership concentration is higher in the emerging markets, thus the studies for <sup>fi</sup>rms headquartered in emerging countries could offer a different result for the relationship between international diversi<sup>fi</sup>cation and <sup>fi</sup>rm value. Berrill and Mannella [11] state that there is an increasing interest in studies that relate to emerging markets and multinational corporations. Emerging markets are attracting the attention of the whole world due to their current high growth rates and potentials for the future. They are ideal markets for goods and services with large populations and increasing incomes [11]. Turkey is one of those emerging countries with its fast growing economy and young population. Thus, this study extends the prior work by examining the impact of multinationality along with certain <sup>fi</sup>rm characteristics on <sup>fi</sup>rm value in the emerging market context. Moreover, the present paper also differentiates itself from previous studies in the literature wherein they utilized data mining and/or text mining in <sup>fi</sup>nancial reporting area focusing primarily on detection of <sup>fi</sup>nancial statement fraud [93–97]. However, this study analyzes the impact of multinationality on <sup>fi</sup>rm value by using data mining technique and a broad set of <sup>fi</sup>nancial data.

In prior work, regression analysis has been frequently and primarily used tools to investigate the association of internationalization with <sup>fi</sup>rm value [31,35,58,82]. This study utilizes advanced analysis techniques of decision trees and arti<sup>fi</sup>cial neural networks. The data sample used in this study includes Turkish non-<sup>fi</sup>nancial <sup>fi</sup>rms over the period of 1997–2011. Within this time period, Turkish <sup>fi</sup>rms are mandated to adopt International Financial Reporting Standards (IFRS). Therefore, we conduct the analysis for the sub-periods of 1997–2004 and 2005– 2011; doing so, we aim to examine whether the adoption of IFRS has any impacted on the <sup>fi</sup>rm value characteristics.<sup>1</sup>

The remainder of the paper is organized as follows. Next section provides the literature review and makes the case for novelty and importance of this study. Section 3 presents the methodology used for the study; Section 4 documents the <sup>fi</sup>ndings of the study. Finally, Section 5 concludes the paper and explains the implications of the study.

## 2. Literature review

The information of whether multinationality affects <sup>fi</sup>rm value is an important piece of information for decision makers for a number of reasons. Firstly, this information provides managers with guidance in relation to whether and in which way to expand operations of the business beyond the borders of their own home country [31]. Secondly, present or potential investors of a <sup>fi</sup>rm also want to know which characteristics are value-relevant so as to determine the direction of their investments. Finally, <sup>fi</sup>nancial analysts also wonder which factors impact <sup>fi</sup>rm value so that they can make the best investment decision on behalf of their customers.

Fauver et al. [35] state the motivations behind increase in foreign investment as improved communications, lower transaction costs, and increasingly integrated foreign markets. However, they also argue that many <sup>fi</sup>rms incur additional costs and risks such as exchange rate, political instability, the agency costs, and coordination costs. Thus, the key question to be answered is whether the internationalization reduces or increases <sup>fi</sup>rm value. In this context, more evidences are needed, since the existing evidence regarding the bene<sup>fi</sup>ts of international diversi<sup>fi</sup>cation has yielded inconclusive results [35].

Some of the previous studies have dealt with the relationship between multinationality and <sup>fi</sup>rm value; however, their <sup>fi</sup>ndings were inconsistent. For example, Eckert et al. [31] conducted their study on German <sup>fi</sup>rms and concluded that multinationality is not a value itself, but through either having intangible assets or realizing economies of scale. Eckert et al. [31] proved that leverage and size have a signi<sup>fi</sup>cant negative impact on shareholder value, whereas pro<sup>fi</sup>tability and capital intensity (as a proxy for economies of scale and as measured by capital expenditures per sales) exert a signi<sup>fi</sup>cant positive effect. Riahi-Belkaoui [78] conducted a study on U.S. <sup>fi</sup>rms and con<sup>fi</sup>rmed that there is a positive relation between the degree of internationalization and the market value of the <sup>fi</sup>rm. Fauver et al. [35] empirically proved that corporate international diversi<sup>fi</sup>cation is value reducing for U.S. <sup>fi</sup>rms on average, but has no signi<sup>fi</sup>cant valuation in<sup>fl</sup>uence for German or U.K. <sup>fi</sup>rms. Schmid and Walter [82] used the percentage of sales from non-domestic operations to measure the impact of geographic diversi<sup>fi</sup>cation, and they indicated that geographic diversi<sup>fi</sup>cation is not associated with a signi<sup>fi</sup>cant valuation discount in <sup>fi</sup>nancial intermediaries.

Machine learning (ML) as well as arti<sup>fi</sup>cial intelligence methodologies have been used extensively to handle <sup>fi</sup>nancial decision making problems [5,6,19,21,37,74]. Furthermore, it has been proven that ML algorithms such as support vector machines (SVM) demonstrated increasingly important performances in <sup>fi</sup>nancial time series analysis [48,68].

ML is the sub<sup>fi</sup>eld of arti<sup>fi</sup>cial intelligence concerned with development of algorithms that allow computer programs to learn from experience [56]. These algorithms are used in a variety of applications. ML algorithms are appropriate in scenarios where the applications involve large databases, making it dif<sup>fi</sup>cult to establish models [66], where <sup>fi</sup>nancial data sets are large, as in our case. Various studies have shown that machine learning techniques such as neural networks and decision tree algorithms can be employed as an alternative method to resolve classi<sup>fi</sup>cation problems instead of the traditional statistical methods [6,9,10,14,19]. Traditional statistical methods use restrictive assumptions such as normality, linearity, and independence among predictor variables. Deakin [26] demonstrated that violations of these important assumptions of independent variables frequently happen in <sup>fi</sup>nancial data. As a result, these conventional statistical methods might produce limitations in terms of validity and effectiveness. Decision trees (DT) algorithms and neural networks (NN) are among the most popular machine learning algorithms. Several of these algorithms such as decision trees algorithms, support vector machines (SVM), neural networks were developed for application in <sup>fi</sup>nancial and accounting applications [43,53,66,76]. Therefore, ML algorithms are the most appropriate for this study.

ML algorithms were employed successfully in some studies that focus on <sup>fi</sup>rm value. Chaehwan et al. [18] studied dividend policy forecasting using ML approaches discovering that comparing ML algorithms was one of the most important managerial decisions affecting the prediction of <sup>fi</sup>rm value. Also, Chih-Fong et al. [22] used popular ML algorithms such as decision trees, genetic algorithms and neural networks to determine the most important features impacting <sup>fi</sup>rm value.

In this study, machine learning (ML) techniques were applied as the data driven approach. While various studies compare the machine learning algorithms in general [98–101] such as SVMs, neural nets, logistic regression, naive bayes, memory-based learning, random forests, decision trees, bagged trees, and boosted trees, the comparison of machine learning algorithms versus classical statistical techniques was studied as well. A literature driven argument for the use of ML techniques in this context, and a comparative analysis of traditional statistical methods versus ML are summarized in Table 1. According to Breiman [102], statistics really starts with data and the main goals of it: prediction (estimation) and information (detection). Breiman [102] claimed that higher predictive accuracy is associated with more reliable information about the underlying data mechanism, therefore weak predictive accuracy can lead to questionable conclusions. Moreover, he valued the importance of algorithmic models since they can give better predictive accuracy than data models, and therefore provide better information about the underlying mechanism. In the light of Breiman's [102] valuable study, the ultimate goal in this study is to obtain accurate information.

## 3. Theoretical background

Four theories are proposed to explain the links between multinationality and <sup>fi</sup>rm value: the internalization theory [67]; imperfect world capital markets [33,67]; managerial objectives [67]; and tax avoidance and low-cost inputs [33,67]. According to the <sup>fi</sup>rst theory, internalization theory, which was developed initially by Caves [17], a <sup>fi</sup>rm can enhance its value by internalizing markets for its intangible assets (i.e. superior production skills, managerial skills, marketing abilities, patents, or consumer goodwill). According to this view, internalization brings buyers and sellers of information-based assets together [30], and <sup>fi</sup>rms can then maximize their revenues through selling or licensing their assets to <sup>fi</sup>rms in other countries [71]. The second theory regarding the imperfection of world capital markets might prevent investors from optimally diversifying their portfolios internationally; therefore multinational <sup>fi</sup>rms provide shareholders with an opportunity to diversify their investments [67,71]. The third theory, managerial objectives, also plays an important role in the internationalization decision, eventually impacting <sup>fi</sup>rm value. Morck and Yeung [67] argue that internationalization might leave more room for managers to act in their own interests, at the expense of investors' interests. Moreover, Denis et al. [30] argue that diversi<sup>fi</sup>cation increases the complexity of organizations, leading to higher coordinating costs for each organization. These factors may contribute to reducing the <sup>fi</sup>rm value of multinationals as opposed to uninationals. Finally, under the fourth theory, internationalization may impact <sup>fi</sup>rm value favorably due to the opportunities provided for tax avoidance and low cost inputs [67]. Denis et al. [30] support this view stating that a multinational <sup>fi</sup>rm has an opportunity to relocate its production to another country where production costs are lower, and it has the ability to reduce its tax liabilities due to the differences between tax systems in other countries.

Table 1  
Comparison of econometric theory based and data driven approaches

<table><tr><td>Econometric theory based approaches</td><td>Data driven approaches</td></tr><tr><td>It is the traditional field that deals with the quantification, collection, analysis, interpretation, and drawing conclusions from data [103].Assumes that the data are generated by a given stochastic data model [102].The statistical community has been committed to the almost exclusive use of data models. This commitment has led to irrelevant theory, questionable conclusions, and has kept statisticians from working on a large range of interesting current problems [102].Hypothesis testing in order to determine the causes and effects as well as model interpretation is critical. Goodness-of-Fit and parameter significance are used for model selection. [102]. It traditionally concerns itself with analyzing primary data that has been collected to check specific research hypothesis; data can be of an experimental nature [105].The sampling of a massive database cannot be analyzed with the traditional statistical sampling theory tools [105]. The size of the data set and the data are initially collected for experimental design is important topic in traditional statistics [103].There are not available analytical methods to be developed in the statistics field [105].Asymptotic analysis, sometimes criticized as being irrelevant. Traditional statistics emphasizes the mathematical formulation and validation of a methodology, and views simulations and empirical or practical evidence as a lesser form of validation. The emphasis on rigor has required proof that a proposed method will work prior to its use [103].The visualization tools of statistics are usually not calibrated for the size of the data sets [103].Decision makers formulate the hypothesis and it is confirmed on the basis of sample evidence. Statistical validation technique provides elements to confirm or disprove the hypotheses formulated by the decision maker, according to a top-down analysis flow [106]</td><td>It is an interdisciplinary field that draws on computer sciences (data base, artificial intelligence, machine learning, graphical and visualization models), statistics and engineering (pattern recognition, neural networks) [103].Uses algorithmic models and treats the data mechanism as unknown [102].Algorithmic modeling, both in theory and practice, has developed rapidly in fields outside statistics. It can be used both on large complex data sets and as a more accurate and informative alternative to data modeling on smaller data sets. Moving away from exclusive dependence on data models and adopting a more diverse set of tools enable us solving problems by using the data [102].Predictive accuracy is the focus. Model interpretation is not as important as the predictive accuracy [104]. Cross validation of predictive accuracy based on partitioned data sets is used for model selection [102]. It can only concern itself with secondary data collected for other reasons (e.g., analyzing company data that comes from a data warehouse); the data is typically of an observational nature [105].The aim of the data driven techniques (ML, data mining) is to analyze great masses of data and carrying out sampling. Sampling is necessary since accessing/analyzing the whole database can be impossible for many applications because of computer efficiency issues [105].Experimental design is usually irrelevant to DM [103].Appropriate analytical methods are needed to be developed since many databases do not lead to the classic forms of statistical data organizations (e.g., data from internet) [105].Asymptotic analysis becomes very relevant. Computer science and machine learning use experimental validation methods. Mathematical analysis of the performance of a statistical algorithm is not feasible in a specific setting, but becomes so when analyzed asymptotically. When size becomes extremely large, studying performance by simulations is also not feasible. It is therefore in settings typical of DM problems that asymptotic analysis becomes both feasible and appropriate. [103].Visualization of the data and its structure, as well as visualization of the conclusions drawn from the data, are central theme [103].Learning models are capable of playing an active role by generating predictions and interpretations which actually represent new knowledge available to the users. The analysis flow has a bottom-up structure. It is hard to formulate a priori meaningful and well-founded hypotheses when faced with large amounts of data [106].</td></tr></table>

## 4. Research methodology

Fig. 1 pictorially illustrates the analytic process employed in this study. The main tasks included obtaining the raw dataset, preprocessing the data, splitting the data into ten randomly selected cross-validation folds, developing predictive models for each fold, assessing and comparing the predictive accuracy of different machine learning techniques, and <sup>fi</sup>nally generating and consolidating sensitivity results of the predictive models.

## 4.1. Data

The dataset used in this study was obtained from the Financial Information News Network (FINNET). FINNET has the largest <sup>fi</sup>nancial database in Turkey, providing a variety of <sup>fi</sup>nancial data, software, and Web-based analysis tools to their members. Even though the FINNET data is rich in content, it had a variety of data problems; demanding a thorough process of data cleaning and pre-processing. Proper preprocessing of data is perhaps the most important step in any analytics study [73]. The pre-processing activities included (i) identi<sup>fi</sup>cation and imputation/elimination of missing data/records, (ii) identi<sup>fi</sup>cation and investigation of anomalies and outliers, and (iii) transformation of nominal values to proper representations for predictive modeling.

The initial dataset for the study consisted of all listed Turkish non-<sup>fi</sup>nancial companies for the time period of 1997 to 2011. The number of unique cases/records retrieved from the database was 5835. After the analyses of the data for missing values, 1452 cases had a large number of missing values for critical <sup>fi</sup>nancial indicators; therefore they were eliminated. There were also 38 cases with unexplainably large values (identi<sup>fi</sup>ed as outliers), which were also eliminated from the dataset. After the data pre-processing, the <sup>fi</sup>nal dataset consisted of 4347 cases. The <sup>fi</sup>nal dataset included proper values for all <sup>fi</sup>nancial indicators for the years 1997 to 2011.

## 4.2. Variables

In this study, the endogenous and exogenous variables (Table 2) were not employed in terms of classical econometric modeling perspective, rather they were used in terms of data driven contemporary machine learning perspective as endogenous (dependent, response, predicted or target) variable and exogenous (independent, explanatory, predictor or source) variables. Consequently, the variable “Firm Value” was employed as the endogenous variables and the size, leverage, sales growth, capital expenditure, pro<sup>fi</sup>tability, asset structure & growth rate, and liquidity were used as exogenous variables. The following table illustrates the literature in which some of the similar endogenous and exogenous variables were employed. In addition, Table 3 lists and brie<sup>fl</sup>y de<sup>fi</sup>nes all of the independent and dependent variables (<sup>fi</sup>nancial indicators) collected, consolidated and used in this study.

What follows are brief descriptions and inclusion justi<sup>fi</sup>cations (as per the published literature) of the data categories that these independent variables belong to. These variables' association with <sup>fi</sup>rm value has been widely investigated in previous <sup>fi</sup>rm value studies.

Table 2  
The use of endogenous and exogenous variables in the literature.  
![](/api/attachments/YM3URWNE/fulltext/images/df9024a5887909c64fb5c4163305319b4c25772ca37daf03da3d50117c44792e.jpg)  
Fig. 1. The process map.

## 4.2.1. Multinationality

There are two competing theoretical arguments about internationalization of <sup>fi</sup>rms; opponents of multinationality argue that it reduces <sup>fi</sup>rm value. They base their arguments on the additional costs that a <sup>fi</sup>rm incurs while operating abroad due to environmental, cultural, political challenges/differences [31]. On the other hand, proponents of multinationality support the idea that it enhances <sup>fi</sup>rm value in a variety of ways. Riahi-Belkaoui [78] states that investors consider internationalization as a hidden or unbooked asset of a <sup>fi</sup>rm which is not re<sup>fl</sup>ected on the balance sheet. Kim and Mathur [49] argue that geographic diversi<sup>fi</sup>- cation can increase <sup>fi</sup>rm value by economies of scale, location-speci<sup>fi</sup>c advantages, increased operational <sup>fl</sup>exibility, and synergy effects.

<table><tr><td>Endogenous variable: Firm value</td><td>Denis et al. [30], Eckert et al. [31], Olsen and Elango [71], Schmid and Walter [82],</td></tr><tr><td>Exogenous variables: Size:</td><td>Ammanna et al. [3], Bae et al. [8], Connelly et al. [23], Erickson et al. [32], Faleye [34], Fauver et al. [35], Konijn et al. [52], Mak and Kusnadi [62], Pramborg [75], Uyar and Kılıç [87], Wu [92],</td></tr><tr><td>Leverage:</td><td>Ammanna et al. [3], Bae et al. [8], Connelly et al. [23,32] [34,52,62,75,87],</td></tr><tr><td>Sales growth:</td><td>Hiraki et al. [41], Mak and Kusnadi [62], Uyar and Kılıç [87], Wu [92],</td></tr><tr><td>Capital expenditure:</td><td>Ammanna et al. [3], Connelly et al. [23] Faleye [34], Fauver et al. [35], Konijn et al. [52], Mak and Kusnadi [62], Pramborg [75].</td></tr><tr><td>Profitability</td><td>Ammanna et al. [3], Bae et al. [8], Connelly et al. [23], Faleye [34], Pramborg [75], Pramborg [75], Uyar and Kılıç [87],</td></tr><tr><td>Asset structure &amp; growth rate</td><td>Mak and Kusnadi [62]</td></tr><tr><td>Liquidity</td><td>Ammanna et al. [3], Pramborg [75],</td></tr></table>

The list of <sup>fi</sup>nancial indicators (predictors) included in the study.

<table><tr><td colspan="2">Multinationality</td></tr><tr><td>Foreign sales ratio</td><td>Foreign sales ÷ Total sales</td></tr><tr><td>Size</td><td></td></tr><tr><td>LnAssets</td><td>Natural logarithm of total assets</td></tr><tr><td>Leverage</td><td></td></tr><tr><td>Leverage ratio</td><td>Total debt ÷ Total assets</td></tr><tr><td>Financial debt ratio</td><td>Total financial debt ÷ Total debt</td></tr><tr><td>Sales growth</td><td></td></tr><tr><td>Sales growth rate</td><td> $(Sales_{t} - Sales_{t-1}) \div Sales_{t-1}$ </td></tr><tr><td>Asset turnover rate</td><td>Sales ÷ Total assets</td></tr><tr><td>Capital expenditure</td><td></td></tr><tr><td>Capital expenditure</td><td> $(\Delta \text{ Long-term assets} + \text{Depreciation} \& \text{amortization}) \div \text{Total assets}$ </td></tr><tr><td>Profitability</td><td></td></tr><tr><td>Return on assets</td><td>Net income ÷ Total assets</td></tr><tr><td>Net profit growth rate</td><td> $(Net income_{t} - Net income_{t-1}) \div Net income_{t-1}$ </td></tr><tr><td>Net profit margin</td><td>Net income ÷ Sales</td></tr><tr><td>Asset structure &amp; growth rate</td><td></td></tr><tr><td>Assets growth rate</td><td> $(Total assets_{t} - Total assets_{t-1}) \div Total assets_{t-1}$ </td></tr><tr><td>Long-term assets ratio</td><td>Long-term assets ÷ Total assets</td></tr><tr><td>Liquidity</td><td></td></tr><tr><td>Quick ratio</td><td> $(Current assets - Inventory) \div Current liabilities$ </td></tr><tr><td>Cash ratio</td><td>Cash and cash equivalents ÷ Total assets</td></tr><tr><td>Cash conversion cycle</td><td>(Accountsreceivable ÷ Sales) * 365 + (Inventories ÷ Cost of goods sold) * 365 - (Accounts payable ÷ Cost of goods sold) * 365</td></tr><tr><td>Dependent variables(market values)</td><td></td></tr><tr><td>Market capitalization</td><td>Share price × The number of shares outstanding.</td></tr><tr><td>Market-to-book ratio</td><td>Market capitalization ÷ Total book value</td></tr></table>

Formerly, multinationality was measured using the ratio of foreign sales to total sales (FSTS) and/or the ratio of foreign assets to total assets (FATA)<sup>2</sup> primarily. Bae and Noh [7] used two criteria: foreign sales ratio (foreign sales divided by total sales) and foreign tax ratio (foreign income taxes divided by total income taxes). However, FSTS has been widely used as a measure of MNCs because other data are less easily available [7]. Due to the widespread usage and data availability, we used FSTS to measure multinationality.

## 4.2.2. Size

Denis et al. [30] argued that diversi<sup>fi</sup>ed <sup>fi</sup>rms are likely to be substantially larger than domestic <sup>fi</sup>rms, further claiming that the former group has greater capital market values than the latter one. Jensen [44] claims that managers have incentives to enlarge their <sup>fi</sup>rms beyond the optimal size, with growth increasing their power by increasing the resources under their control. Thus, agency costs arise which might in<sup>fl</sup>uence a <sup>fi</sup>rm's value unfavorably. Konijn et al. [52] assumed a negative relation between <sup>fi</sup>rm value and size; supported by other studies such as Ammanna et al. [3], Pramborg [75], Bae et al. [8], and Erickson et al. [32] who also found a negative correlation between size and <sup>fi</sup>rm value. On the other hand, Mak and Kusnadi [62], Uyar and Kılıç [87], and Wu [92] found a positive relation between size and <sup>fi</sup>rm value. Faleye [34] and Connelly et al. [23] found an insigni<sup>fi</sup>cant relation for size and <sup>fi</sup>rm value. Fauver et al. [35] found that size is signi<sup>fi</sup>cant and negative for <sup>fi</sup>rms in Germany, but is signi<sup>fi</sup>cant and positive for <sup>fi</sup>rms in the U.K. and the U.S. To measure size, in this study we utilized the natural logarithm of total assets.

## 4.2.3. Leverage

Determinants of leverage, which is measured by total debt to total assets or total debt to total equity ratios, are explained by two theories in the <sup>fi</sup>nancial literature; being the trade-off theory and the pecking order theory [60]. DeAngelo and Masulis [27] proposed the trade-off theory which purports to set a theoretical optimum level of debt for a <sup>fi</sup>rm, in which the amount of tax savings due to additional borrowing is offset by an increase in the cost of distress. The pecking order theory suggests that <sup>fi</sup>rms have an order of preference when using <sup>fi</sup>nancing sources [69]. According to this theory, <sup>fi</sup>rms prefer internal <sup>fi</sup>nancing to debt, short-term debt over long-term debt, and any debt outside of equity [16,60]. Leverage can be negatively (e.g., riskiness, debt overhang) or positively (e.g., disciplining role) associated with <sup>fi</sup>rm value [52]. Some researchers found that leverage is negatively correlated with <sup>fi</sup>rm value [32,34,52]. On the other hand, Mak and Kusnadi [62], and Bae et al. [8] found a positive relation between leverage and <sup>fi</sup>rm value. Wu [92] found an insigni<sup>fi</sup>cant relationship. Ammanna et al. [3] found both a negative and a positive relation depending on changing speci<sup>fi</sup>cations. Pramborg [75], Uyar and Kılıç [87], and Connelly et al. [23] could not <sup>fi</sup>nd a signi<sup>fi</sup>cant relation. In the analysis, we used two leverage ratios; the ratio of total debt to total assets and the ratio of <sup>fi</sup>nancial debt to total debt.

## 4.2.4. Sales growth

Sales growth measures whether resources are used ef<sup>fi</sup>ciently or not. Current growth rate in sales indicates future growth rates. The expectations of investors for growth are re<sup>fl</sup>ected in share prices; the higher the expectations for growth, the more a <sup>fi</sup>rm has value. Thus, we assume a positive impact of sales growth on <sup>fi</sup>rm value. Mak and Kusnadi [62] and Hiraki et al. [41] found evidence of a positive relation between sales growth and <sup>fi</sup>rm value. Wu [92] and Uyar and Kılıç [87] found an insigni<sup>fi</sup>cant relationship. In addition to sales growth in the current year relative to previous year's sales revenue, we used asset turnover rate to measure sales generating ability of <sup>fi</sup>rms using assets.

## 4.2.5. Capital expenditure

The in<sup>fl</sup>uence of capital expenditures might be primarily explained by two con<sup>fl</sup>icting approaches. According to the <sup>fi</sup>rst approach (i.e. the traditional view), managers are expected to act in the best interests of their shareholders, and are assumed to undertake capital projects which generates a positive net current value, thereby maximizing their stockholders' wealth [46]. In this way, a positive association between capital expenditures and <sup>fi</sup>rm value is predictable. On the contrary, agency theory [45] suggests that managers may make investment decisions to ful<sup>fi</sup>ll their own self-interests even though at the expense of stockholders, leading to a decrease in <sup>fi</sup>rm value. According to earlier studies, capital expenditure has a signi<sup>fi</sup>cant positive effect on <sup>fi</sup>rm value [3,23,34,35,52,62,75]. Thus, in this study we assume a signi<sup>fi</sup>cant in<sup>fl</sup>uence of capital structure on <sup>fi</sup>rm value.

## 4.2.6. Profitability

The signaling theory explains the relationship between pro<sup>fi</sup>tability and <sup>fi</sup>rm value. Pro<sup>fi</sup>tability is a primary performance indicator that is closely followed by investors and creditors. For the former group, it indicates dividend payment ability (signaling theory), and is also indicative of future earnings as pointed out by Wu et al. [91] (signaling theory), for the latter group, this demonstrates the debt and interest paying ability of the <sup>fi</sup>rm (signaling theory). Therefore, pro<sup>fi</sup>tability is assumed to impact <sup>fi</sup>rm value. A pro<sup>fi</sup>table <sup>fi</sup>rm is likely to trade at a premium compared to a less pro<sup>fi</sup>table one [75]. Faleye [34], Pramborg [75], Bae et al. [8], Uyar and Kılıç [87], Connelly et al. [23], and Ammanna et al. [3] have all found a signi<sup>fi</sup>cant positive impact of pro<sup>fi</sup>tability on <sup>fi</sup>rm value. For this variable, we used three ratios; return on assets, net pro<sup>fi</sup>t margin, and net pro<sup>fi</sup>t growth rate.

## 4.2.7. Asset structure & growth rate

Agency theory arises out of the con<sup>fl</sup>icts of interest between principals and agents. Asset growth is a way of demonstrating where the provided capital has been invested, and whether it has been invested properly in order to bring an appropriate rate of return. In other words, growth in assets assists monitoring of investments, thus mitigating agency costs, much as a governance mechanism. Mak and Kusnadi [62] investigated the impact of asset tangibility on <sup>fi</sup>rm value, and found insigni<sup>fi</sup>cant relation between <sup>fi</sup>xed asset ratio and <sup>fi</sup>rm value. To test the association of this variable with <sup>fi</sup>rm value, we used asset growth rate and the ratio of long-term assets to total assets in this study.

## 4.2.8. Liquidity

Liquidity is a “two-edged sword”<sup>3</sup>: keeping liquid assets on hand creates advantages and disadvantages for the <sup>fi</sup>rm as well as its investors. Holding suf<sup>fi</sup>cient liquid assets prevents <sup>fi</sup>nancial distress and default risk, enabling the payment of short-term liabilities. However, stockpiling more than suf<sup>fi</sup>cient liquid assets could mean that the capital provided by investors is not utilized to the best advantage, since liquid assets are generally considered to bring lower returns compared to long-term assets. This has a strong in<sup>fl</sup>uence on <sup>fi</sup>rm value. Pramborg [75] could not prove a statistically signi<sup>fi</sup>cant association between liquidity (as measured by current ratio) and <sup>fi</sup>rm value. However, Ammanna et al. [3] found a signi<sup>fi</sup>cant positive association between cash ratio (Cash/Assets) and <sup>fi</sup>rm value. Three liquidity ratios were used in the analysis; quick ratio, cash ratio, and cash conversion cycle.

## 4.3. Cross validation

Cross validation is a recently popularized technique to estimate the accuracy of a predictive model's performance in practice. It is sometimes called rotation estimation and the aim of the technique is to assess how

Table 4 Confusion (coincidence) matrix.

the result of an analysis will generalize to an independent data set. 10- fold cross validation is widely used since the empirical studies demonstrated that 10 was an optimal number of folds [51]. In the 10-fold cross validation, the data set is randomly split into 10 mutually exclusive subsets of approximately equal sizes. The model is trained <sup>fi</sup>rst and tested 10 times. Each time, the model is trained on 9 folds (as a combined training data that includes 90% of the total dataset) and tested on the remaining 1 fold. The cross validation estimates of the overall accuracy of a model are evaluated by averaging the 10 individual accuracy measures [73] as shown in Eq. (1):

$$
C V A = \frac {1}{k} \sum_ {i = 1} ^ {k} A _ {i}\tag{1}
$$

where, “CVA” stands for cross validation accuracy, k is the number of folds (here $k = 1 0 )$ , and A is the accuracy measure.

## 4.4. Decision tree algorithms

Decision trees are commonly used machine learning methods in data mining. There are two main types of decision tree classi<sup>fi</sup>cations: classi<sup>fi</sup>cation tree analysis and regression tree analysis. Decision trees are becoming increasingly popular for data mining because they are easy to understand and interpret, require little data preparation, handle numerical and categorical data, and they perform very well with a large data set in a short time. Decision trees produce excellent visualizations of results and their relationships. Although there are many speci<sup>fi</sup>c decision tree algorithms, the ID3, C4.5, C5.0, CART, and CHAID and QUEST algorithms are the most commonly used.

Chi-squared Automatic Interaction Detector (CHAID) is an extremely effective statistical technique developed by Kass [47]. Its main use is for segmentation, or tree growing. CHAID is a decision tree technique based on adjusted signi<sup>fi</sup>cance testing. It can be used for predictions in the same way as for regression analysis and classi<sup>fi</sup>cation as well as detecting interaction between variables. Differing from other decision tree techniques, CHAID can produce more than two categories at any level in the tree; therefore it is not a binary tree method.

C5.0 was developed by Quinlan [76]. It offers a number of improvements on C4.5: it is signi<sup>fi</sup>cantly faster than C4.5; it is more memory ef-<sup>fi</sup>cient than C4.5; it creates a considerably smaller decision tree while producing similar results; it boosts the trees, improving them and creating more accuracy; it makes it possible to weight different attributes and misclassi<sup>fi</sup>cation types; and, it automatically winnows the data to help reduce noise. As a result, it improves the objectivity and precision of the decision tree classi<sup>fi</sup>cation algorithm.

Classi<sup>fi</sup>cation and Regression Trees (CART) were established by [15]. CART is a binary decision tree algorithm capable of processing continuous or categorical predictor or target variables. It works recursively: data is partitioned into two subsets to make the records in each subset more homogeneous than in the previous subset; the two subsets are then split again until the homogeneity criterion or some other stopping criteria is satis<sup>fi</sup>ed. The same predictor <sup>fi</sup>eld may be used many times in the tree. The ultimate aim of splitting is to determine the right variable associated with the right threshold to maximize the homogeneity of the sample subgroups.

The Quick, Unbiased, Ef<sup>fi</sup>cient Statistical Tree (QUEST) algorithm is a relatively new binary-split decision tree algorithm for classi<sup>fi</sup>cation in data mining [61]. It is similar to the CART Tree algorithm [15]. However, there are some minor differences. For instance, QUEST employs an unbiased variable selection method, uses imputation for dealing with missing values instead of surrogate splits, and handles categorical variables with many categories.

## 4.5. Neural network analysis

Arti<sup>fi</sup>cial Neural Networks (or simply Neural Networks) are analytic techniques that were inspired from biology; the basic element of them is a neuron (types of cells found in human brain). The neurons are organized into layers: input, hidden, and output. It operates as the nervous system operates. The neural network model accepts many inputs, sums them, usually applies non-linear transfer functions, and generates the results. Neural networks are capable of modeling very complex nonlinear functions [40]. Multilayer perceptron structure of neural networks was employed in this study. The training of this structure uses back propagation of error method based on generalized delta rule [79]. Information in the form of input <sup>fi</sup>elds feeds forward through the network to generate a prediction from the output layer for each record in the network during training procedure. This prediction is compared to the recorded output value for the training record, and the difference between the predicted and actual output is propagated backward through the network to adjust the connection weights to improve the prediction for similar patterns [84]. In this study, a multi-layered perceptron (MLP) type feed-forward neural network architecture is used. The network had one hidden layer with 18 processing elements. The network is trained using the back-propagation learning method. The ANN parameters such as number of hidden layers, number of processing elements, learning and momentum rates, number of epochs, are all determined with numerous experimentations.

## 4.6. Performance measurements of prediction models

The performance of models used in predicting binary (two-group) outcomes is measured by using a confusion matrix (see Table 4). A confusion matrix (also known as coincidence matrix) contains valuable information about the actual and predicted classi<sup>fi</sup>cations created by the prediction model [50]. It is important to use a variety of performance criteria to evaluate the learning methods [98,99]. For purposes of this study, we used well-known performance measures such as Overall Accuracy, AUC (area under the ROC curve), Recall and F-measure. All of these measures were used to evaluate each model in the study, after which the models were compared on the basis of the proposed performance measurements.

## 4.6.1. Overall Accuracy (AC)

Accuracy is de<sup>fi</sup>ned as the percentage of records that are correctly predicted by the model. It is also de<sup>fi</sup>ned as being the ratio of correctly predicted cases to the total number of cases (see Eq. (2)).

$$
\text { Accuracy } = \frac {\mathrm{TP} + \mathrm{TN}}{\mathrm{TP} + \mathrm{TN} + F P + \mathrm{FN}}\tag{2}
$$

## 4.6.2. Precision

Precision is de<sup>fi</sup>ned as the ratio of the number of True Positive (correctly predicted cases) to the sum of the True Positive and the False Positive.

## 4.6.3. Recall

Recall is also known as the Sensitivity or True Positive rate. It is de<sup>fi</sup>ned as the ratio of the True Positive (the number of correctly predicted cases) to the sum of the True Positive and the False Negative.

<table><tr><td colspan="4">Predicted</td></tr><tr><td rowspan="3">Actual</td><td></td><td>Unsuccessful</td><td>Successful</td></tr><tr><td>Unsuccessful</td><td>True Negative</td><td>False Positive</td></tr><tr><td>Successful</td><td>False Negative</td><td>True Positive</td></tr></table>

## 4.6.4. F-measure

F-measures take the harmonic mean of the Precision and Recall Performance measures. Therefore, it takes into consideration both the Precision and the Recall Performance as being important measurement tools for these calculations, as shown in Eq. (3) [90].

$$
\text { F - measure } = 2 \times \frac {\text { Precision } \times \text { Recall }}{\text { Precision } + \text { Recall }}\tag{3}
$$

## 4.6.5. Specificity

This is also known as the True Negative Rate (TN). It is de<sup>fi</sup>ned as the ratio of the number of the True Negative to the sum of the True Negative and the False Positive.

## 4.7. Sensitivity analysis (predictor's importance)

“Cause and effect” relationship between the dependent (output) and independent (input) variables of a prediction model is often determined by “sensitivity analysis” in machine learning algorithms [25]. Sensitivity analysis aims to measure the importance of predictor variables. It is commonly used to identify and focus on the more important variables and to ignore or drop the least important ones. They are related to the importance of each variable in making a prediction, not necessarily whether the prediction itself is accurate. The variance of predictive error is arrived at by dropping one predictor variable at a time, and observing the performance of the remainder. A variable is considered more important than another if it increases the variance, compared to the complete model containing all the variables [84]. Predictor importance is determined by evaluating variance reduction of the target attributable to each predictor (see Eq. (4)). Predictors are ranked according to the sensitivity measure de<sup>fi</sup>ned as [85]:

$$
S _ {i} = \frac {V _ {i}}{V (Y)} = \frac {V (E (Y | X _ {i}))}{V (Y)}\tag{4}
$$

where Y is the target (dependent variable), $X j ( j = 1 , . . . , k )$ are predictors (independent variables). V(Y) is the unconditional output variance. The expectation operator E represents an integral over X $_ - i { \dot { \Gamma } }$ that ${ \mathrm { i } } s ,$ over all factors but X . The variance operator V denotes a further integral over $X _ { i \cdot }$ Predictor importance of ith variable is then computed as the normalized sensitivity (see Eq. (5)).

$$
P I _ {i} = \frac {S _ {i}}{\sum_ {j = 1} ^ {k} S _ {j}}\tag{5}
$$

It is shown that S is the proper measure of sensitivity to rank the predictors in order of importance for any combination of interaction and non-ortogonality among predictors [81].

## 4.8. Information fusion-based sensitivity analysis

There are various de<sup>fi</sup>nitions of information fusion in the literature. A substantial amount of research has been dedicated to problems concerning how to combine data from various sources. It is also known as data fusion. “Data fusion is a process that combines data and knowledge from different sources with the aim of maximizing the useful information content, for improved reliability or discriminant capability, while minimizing the quantity of data ultimately retained” [86]. In this study, obtained predictions are the data or information, “prediction models” are the sources, and combining the predictions is the process of fusion. Studies have shown that combining predictions (fusion) reveals more accurate and more robust results [28,83].

Each decision tree model generated variable importance scores for each independent variable. The combination of these prediction models is called information fusion-based sensitivity analysis, and is recommended because it produces more accurate, robust models [36].

Each of the prediction models produced somewhat different predictor important values. An information fusion-based sensitivity analysis was performed to combine these values into a common representation. The relative variable importance score produced by each decision tree model was normalized by using Eq. (6) below. They were then aggregated into a single set of importance numbers and are represented in a tabular form (the normalized variable importance scores were combined using Eq. (7)) [29]. Essentially, the normalized score of each independent variable was multiplied by the normalized weight value for each prediction model and <sup>fi</sup>nally, these multiplied scores were added together to <sup>fi</sup>nd a single combined (fused) relative importance value for each variable.

$$
P I _ {n e w} = \frac {P I - P I _ {m i n}}{P I _ {m a x} - P I _ {m i n}}\tag{6}
$$

$$
P I _ {n (f u s e d)} = w _ {1} P I _ {1 n} + w _ {2} P I _ {2 n} + \dots + w _ {m} P I _ {m n}\tag{7}
$$

PI represents the relative predictor importance score that was initially produced by the individual model.

w<sub>i</sub> represents the normalized weight values for each model. This represents the importance of models and is proportional to their predictive powers.

M represents the number of prediction models (m = 5 in this study)

N represents the number of variables (n = 15 variables in this study)

These fused sensitivity scores were presented as bar-charts to visually illustrate the relative importance of the independent variables from the highest (most important) to the lowest (least important) for predicting (contributing to the prediction of) the dependent variable.

## 5. Results

The impact of multinationality (as measured by foreign sales ratio) and fourteen other <sup>fi</sup>nancial indicators on market capitalization and market-to-book ratio for the period of 1997–2011 was investigated using decision tree and neural network algorithms. Although a great many previous studies used market-to-book ratio as a proxy of the <sup>fi</sup>rm value [7,12,55,59,88,92], other studies utilized market capitalization as a market value indicator [4,24,87]. As a result, we decided to use both variables as dependent variables. Market value (i.e. market capitalization) is calculated by multiplying the numbers of shares outstanding by the share price which represents the price investors are willing to pay to buy or sell the stock. Thus, the market value is open to <sup>fl</sup>uctuation depending upon changes in share price which is determined in the market place. Rust et al. [80] claimed that the market value of <sup>fi</sup>rms depended largely on their growth prospects and sustainability of pro<sup>fi</sup>ts. However, book value is the value of the organization as re<sup>fl</sup>ected in the <sup>fi</sup>rm's <sup>fi</sup>nancial statements which are prepared in accordance with accounting and/or <sup>fi</sup>- nancial reporting standards and laws. Market value and book value are different in that the former is forward-looking and the latter is retrospective [80]. Malighetti et al. [63] puts it succinctly “the market values the company as a going concern”. Rust et al. [80] explained the market-tobook gap by off-balance-sheet assets<sup>4</sup> (i.e. market-based and intellectual property) and by an excess or lack of investor enthusiasm [80].

Beginning from 2005, Turkish <sup>fi</sup>rms were mandated to start implementing IFRS. Thus, we divided the time period of 1997–2011 into two periods; 1997–2004 and 2005–2011 to investigate the robustness of results pre- and post-IFRS implementation. There were <sup>fi</sup>fteen inputs and two outputs for the formulation of this study. The output variables were market capitalization and market-to-book ratio, both representing the <sup>fi</sup>rm value. The input variables were asset turnover rate, assets growth rate, capital expenditure, cash conversion cycle, cash ratio, <sup>fi</sup>nancial debt ratio, foreign sales ratio, leverage ratio, LnAssets, long-term assets ratio, net pro<sup>fi</sup>t growth rate, net pro<sup>fi</sup>t margin, quick ratio, return on assets, and sales growth rate. The outputs variables were: Market capitalization and market-to-book ratio.

The dependent variables as outputs were entered into the models as binary variables. These output variables represent the <sup>fi</sup>rm values from two different perspectives. Central tendency measure (statistical mean) values were employed as split criterion for creating binary output variables: the class with a performance score above the mean values was rated as 1 (successful) and the class with a performance score below the mean values was rated as 0 (unsuccessful). In this study, the cases (successful and unsuccessful) were unbalanced. The data set was balanced as to be approximately 50% (successful) and 50% (unsuccessful). It is advisable to correct imbalances in datasets to conform to speci<sup>fi</sup>ed test criteria [89]. Many modeling techniques have trouble with skewed/biased data (i.e., suppose that a data set has only two values: Yes and no; 90% “yes”, 10% “no”) since they tend to learn only the outcome with high percentage (“yes”) and ignore outcome with low percentage (“no”). Models have a better chance of <sup>fi</sup>nding patterns that distinguish the two groups if the data are well balanced with approximately equal numbers of outcomes [85].

## 5.1. Prediction results for market capitalization

A total of <sup>fi</sup>ve classi<sup>fi</sup>cation models were included: C5.0/DT, CART, QUEST/DT, CHAID/DT and Multi Layered Perceptron/Neural Network models. Also, in order to obtain more accurate and more robust predictions, in addition to the individual models, ensemble models were also developed. The obtained prediction results for each model were based on hold-out test data using 10-fold cross validation methodology: 10 different models were trained and tested, each time using a different mutually exclusive 10% of the total dataset as the hold-out/test sample. The testing results were combined and used for comparison of the prediction models.

Table 5 illustrates the comparison of the prediction models in terms of performances between 2005 and 2011. As the results show, the C5.0 decision tree model outperformed the other individual models in terms of overall accuracy rate with almost 91%. CHAID and CART decision tree models performed equally well with almost 86% while Neural Network and QUEST performed 84% in overall accuracy rate. The ensemble model was the combination of these individual models which performed better than almost all of the models except C5.0. It was expected that the ensemble model demonstrates high predictive ability compared to the individual models. The other performance measures: sensitivity, speci<sup>fi</sup>city, precision, F-measure and AUC also indicate that the C5.0 decision tree model performed best, and ensemble model was the second highest prediction model. Even though the order of the other prediction models was changed depending on the performance measure, they demonstrate consistency by being close to each other with around or over 80% prediction rate.

Table 6 shows the confusion (coincidence) matrix constructed from the test data samples. It provides overall accuracy rates as well as perclass accuracy rates for each individual models and the ensemble model (linear combination of the individual models). The results indicate that prediction accuracy for the successful class was higher than the prediction rate for the unsuccessful class in all individual models as well as in the ensemble model. Successful prediction rate was the highest in the C5.0 model with almost 95% signi<sup>fi</sup>cant accuracy rate, while CART model predicted the successful class with almost 93% and ensemble model predicted with almost 92% signi<sup>fi</sup>cant accuracy rates. Therefore, these models predicted successful companies in terms of market capitalization with over 90% prediction rate. Also, C5.0, CHAID, and ensemble models predicted unsuccessful companies with almost 87% and 85% accuracy rate, while the others also predicted unsuccessful companies in terms of market capitalization around 80% accuracy rate.

The same <sup>fi</sup>ve data mining models as well as the ensemble model (linear combination of the individual models) were also conducted to determine the outcome of market capitalization between 1997 and 2004. Tables 7 and 8 indicate the performance measurements and confusion matrices of the models from 1997 to 2004. It shows that C5.0 was the best performing model, while CHAID, CART and Neural Network were the next leading performing models. The ensemble model performed very well after C5.0. These results show consistency with those taken between 2005 and 2011. Again, C5.0 and ensemble models predicted successful <sup>fi</sup>rms with almost 90% accuracy rate, while CHAID, CART, Neural Network and QUEST models predicted successful class with over 80% accuracy rate. The ability of the included prediction models to predict successful and unsuccessful <sup>fi</sup>rms demonstrated consistency in both time periods: 1997–2004 and 2005–2011.

## 5.2. Sensitivity analysis results for market capitalization

In order to determine the relative predictor importance of the inputs (independent variables), model-speci<sup>fi</sup>c sensitivity analysis as well as information fusion based multi-model sensitivity analysis was conducted. Each of the <sup>fi</sup>ve models created a somewhat different predictor importance scores. The relative predictor importance values generated by each model initially was normalized (using Eq. (6)). The normalized scores of each model were multiplied by weight values of each model (using Eq. (7)) and these multiplied values were then added together in order to <sup>fi</sup>nd a single fused (combined) predictor importance score for each independent variable (see Table 9). Table 9 represents sensitivity analysis values for market capitalization between 2005 and 2011. To illustrate visual representation of the fused predictor importance values of independent variables in the order of importance level, a barchart was created using the aggregated sensitivity values (see Fig. 2).

Table 5  
Prediction results for market capitalization (2005–2011).

<table><tr><td></td><td>Accuracy (AC)</td><td>Sensitivity/True Positive Rate/Recall (TP)</td><td>Specificity/True Negative rate (TN)</td><td>False Positive rate (FP)</td><td>False Negative rate (FN)</td><td>Precision (P)</td><td>F-measure</td><td>Area under curve (AUC)</td></tr><tr><td>C5.0</td><td>0.9074</td><td>0.8632</td><td>0.9518</td><td>0.0482</td><td>0.1368</td><td>0.9473</td><td>0.9033</td><td>0.959</td></tr><tr><td>C&amp;R Tree</td><td>0.8629</td><td>0.7905</td><td>0.9355</td><td>0.0645</td><td>0.2095</td><td>0.9249</td><td>0.8524</td><td>0.915</td></tr><tr><td>QUEST</td><td>0.8349</td><td>0.7743</td><td>0.8958</td><td>0.1042</td><td>0.2257</td><td>0.8818</td><td>0.8246</td><td>0.856</td></tr><tr><td>CHAID</td><td>0.8658</td><td>0.8664</td><td>0.8651</td><td>0.1349</td><td>0.1336</td><td>0.8658</td><td>0.8661</td><td>0.944</td></tr><tr><td>Neural Network</td><td>0.8440</td><td>0.7931</td><td>0.8951</td><td>0.1049</td><td>0.2069</td><td>0.8837</td><td>0.8360</td><td>0.908</td></tr><tr><td>Ensemble</td><td>0.8801</td><td>0.8392</td><td>0.9212</td><td>0.0788</td><td>0.1608</td><td>0.9145</td><td>0.8752</td><td>n/a</td></tr></table>

Table 6  
Confusion matrices of the models based on 10-fold cross validation test data (market capitalization, 2005–2011).

<table><tr><td>Model type</td><td></td><td>Unsuccessful (0)</td><td>Successful (1)</td><td></td><td></td><td>Overall accuracy</td><td>Per-class accuracy</td></tr><tr><td rowspan="3">C5.0</td><td>Unsuccessful (0)</td><td>1461</td><td>74</td><td>Correct</td><td>2792</td><td>90.74%</td><td>87.38%</td></tr><tr><td>Successful (1)</td><td>211</td><td>1331</td><td>Wrong</td><td>285</td><td>9.26%</td><td>94.73%</td></tr><tr><td>Sum</td><td>1672</td><td>1405</td><td></td><td>3077</td><td></td><td></td></tr><tr><td rowspan="3">C&amp;R Tree</td><td>Unsuccessful (0)</td><td>1436</td><td>99</td><td>Correct</td><td>2655</td><td>86.29%</td><td>81.64%</td></tr><tr><td>Successful (1)</td><td>323</td><td>1219</td><td>Wrong</td><td>422</td><td>13.71%</td><td>92.49%</td></tr><tr><td>Sum</td><td>1759</td><td>1318</td><td></td><td>3077</td><td></td><td></td></tr><tr><td rowspan="3">QUEST</td><td>Unsuccessful (0)</td><td>1375</td><td>160</td><td>Correct</td><td>2569</td><td>83.49%</td><td>79.80%</td></tr><tr><td>Successful (1)</td><td>348</td><td>1194</td><td>Wrong</td><td>508</td><td>16.51%</td><td>88.18%</td></tr><tr><td>Sum</td><td>1723</td><td>1354</td><td></td><td>3077</td><td></td><td></td></tr><tr><td rowspan="3">CHAID</td><td>Unsuccessful (0)</td><td>1.328</td><td>207</td><td>Correct</td><td>2664</td><td>86.58%</td><td>86.57%</td></tr><tr><td>Successful (1)</td><td>206</td><td>1.336</td><td>Wrong</td><td>413</td><td>13.42%</td><td>86.58%</td></tr><tr><td>Sum</td><td>1534</td><td>1543</td><td></td><td>3077</td><td></td><td></td></tr><tr><td rowspan="3">Neural Network</td><td>Unsuccessful (0)</td><td>1374</td><td>161</td><td>Correct</td><td>2597</td><td>84.40%</td><td>81.16%</td></tr><tr><td>Successful (1)</td><td>319</td><td>1223</td><td>Wrong</td><td>480</td><td>15.60%.</td><td>88.37%</td></tr><tr><td>Sum</td><td>1693</td><td>1384</td><td></td><td>3077</td><td></td><td></td></tr><tr><td rowspan="3">Ensemble</td><td>Unsuccessful (0)</td><td>1414</td><td>121</td><td>Correct</td><td>2708</td><td>88.01%</td><td>85.08%</td></tr><tr><td>Successful (1)</td><td>248</td><td>1294</td><td>Wrong</td><td>369</td><td>11.99%</td><td>91.45%</td></tr><tr><td>Sum</td><td>1662</td><td>1415</td><td></td><td>3077</td><td></td><td></td></tr></table>

The y-axis shows <sup>fi</sup>nancial indicators as the independent variables while x-axis shows the predictor importance score for each indicator. According to Fig. 4, LnAssets was the most important predictor in determining the market capitalization between 2005 and 2011, while leverage ratio was the second the most important predictor. Also, cash ratio, quick ratio, net pro<sup>fi</sup>t margin and return on assets <sup>fi</sup>nancial indicators were the followed leading variables on market capitalization. It is noteworthy to recite that LnAssets variable was the most important variable in all <sup>fi</sup>ve individual models (Table 9).

Fig. 3 illustrates the information fusion based sensitivity analysis result of market capitalization from 1997 to 2004. As the result indicate,

LnAssets were the most important factor, while return on assets, leverage ratio, assets growth rate, cash ratio were the followed <sup>fi</sup>nancial characteristics in predicting the outcome of market capitalization. This result is consistent with the result from 2005 to 2011; the variable LnAssets was the most important variable in both analyses. In both Figs. 2 and 3, we see that <sup>fi</sup>rm size, as measured by LnAssets, is a dominant variable affecting <sup>fi</sup>rm value. This <sup>fi</sup>nding supports the empirical evidences provided by prior studies. Although a few studies found insigni<sup>fi</sup>cant relation for size and <sup>fi</sup>rm value [23,34], many previous studies found either a signi<sup>fi</sup>cant negative correlation [3,8,32,52,75] or a significant positive association between the two variables [62,87,92].

Table 7  
Prediction results for market capitalization (1997–2004)

<table><tr><td></td><td>Accuracy (AC)</td><td>Sensitivity/True Positive Rate/Recall (TP)</td><td>Specificity/True Negative rate (TN)</td><td>False Positive rate (FP)</td><td>False Negative rate (FN)</td><td>Precision (P)</td><td>F-measure</td><td>Area under curve (AUC)</td></tr><tr><td>C5.0</td><td>0.9061</td><td>0.9016</td><td>0.9105</td><td>0.0895</td><td>0.0984</td><td>0.9089</td><td>0.9052</td><td>0.9530</td></tr><tr><td>C&amp;R Tree</td><td>0.8138</td><td>0.7352</td><td>0.8915</td><td>0.1085</td><td>0.2648</td><td>0.8703</td><td>0.7971</td><td>0.8460</td></tr><tr><td>QUEST</td><td>0.7764</td><td>0.6768</td><td>0.8749</td><td>0.1251</td><td>0.3232</td><td>0.8426</td><td>0.7507</td><td>0.8160</td></tr><tr><td>CHAID</td><td>0.8281</td><td>0.7944</td><td>0.8614</td><td>0.1386</td><td>0.2056</td><td>0.8502</td><td>0.8213</td><td>0.9120</td></tr><tr><td>Neural Network</td><td>0.8050</td><td>0.7896</td><td>0.8203</td><td>0.1797</td><td>0.2104</td><td>0.8130</td><td>0.8011</td><td>0.8740</td></tr><tr><td>Ensemble</td><td>0.8540</td><td>0.8008</td><td>0.9066</td><td>0.0934</td><td>0.1992</td><td>0.8945</td><td>0.8451</td><td>n/a</td></tr></table>

Table 8  
Confusion matrices of the models based on 10-fold cross validation test data (market capitalization, 1997–2004).

<table><tr><td>Model type</td><td></td><td>Unsuccessful (0)</td><td>Successful (1)</td><td></td><td></td><td>Overall accuracy</td><td>Per-class accuracy</td></tr><tr><td rowspan="3">C5.0</td><td>Unsuccessful (0)</td><td>1150</td><td>113</td><td>Correct</td><td>2277</td><td>90.61%</td><td>90.34%</td></tr><tr><td>Successful (1)</td><td>123</td><td>1127</td><td>Wrong</td><td>236</td><td>9.39%</td><td>90.89%</td></tr><tr><td>Sum</td><td>1273</td><td>1240</td><td></td><td>2513</td><td></td><td></td></tr><tr><td rowspan="3">C&amp;R Tree</td><td>Unsuccessful (0)</td><td>1126</td><td>137</td><td>Correct</td><td>2045</td><td>81.38%</td><td>77.28%</td></tr><tr><td>Successful (1)</td><td>331</td><td>919</td><td>Wrong</td><td>468</td><td>18.62%</td><td>87.03%</td></tr><tr><td>Sum</td><td>1457</td><td>1056</td><td></td><td>2513</td><td></td><td></td></tr><tr><td rowspan="3">QUEST</td><td>Unsuccessful (0)</td><td>1105</td><td>158</td><td>Correct</td><td>1951</td><td>77.64%</td><td>73.23%</td></tr><tr><td>Successful (1)</td><td>404</td><td>846</td><td>Wrong</td><td>562</td><td>22.36%</td><td>84.26%</td></tr><tr><td>Sum</td><td>1509</td><td>1004</td><td></td><td>2513</td><td></td><td></td></tr><tr><td rowspan="3">CHAID</td><td>Unsuccessful (0)</td><td>1088</td><td>175</td><td>Correct</td><td>2081</td><td>82.81%</td><td>80.89%</td></tr><tr><td>Successful (1)</td><td>257</td><td>993</td><td>Wrong</td><td>432</td><td>17.19%</td><td>85.02%</td></tr><tr><td>Sum</td><td>1345</td><td>1168</td><td></td><td>2513</td><td></td><td></td></tr><tr><td rowspan="3">Neural Network</td><td>Unsuccessful (0)</td><td>1036</td><td>227</td><td>Correct</td><td>2023</td><td>80.50%</td><td>79.75%</td></tr><tr><td>Successful (1)</td><td>263</td><td>987</td><td>Wrong</td><td>490</td><td>19.50%</td><td>81.30%</td></tr><tr><td>Sum</td><td>1299</td><td>1214</td><td></td><td>2513</td><td></td><td></td></tr><tr><td rowspan="3">Ensemble</td><td>Unsuccessful (0)</td><td>1145</td><td>118</td><td>Correct</td><td>2146</td><td>85.40%</td><td>82.14%</td></tr><tr><td>Successful (1)</td><td>249</td><td>1001</td><td>Wrong</td><td>367</td><td>14.60%</td><td>89.45%</td></tr><tr><td>Sum</td><td>1394</td><td>1119</td><td></td><td>2513</td><td></td><td></td></tr></table>

Table 9  
Aggregated sensitivity analysis results of market capitalization (2005–2011).

<table><tr><td></td><td>C5.0</td><td>CHAID</td><td>C&amp;R Tree</td><td>QUEST</td><td>Neural Network</td><td>PI (fused)</td></tr><tr><td>Asset turnover rate</td><td>0.0316</td><td>0.0000</td><td>0.0000</td><td>0.0107</td><td>0.0000</td><td>0.0376</td></tr><tr><td>Assets growth rate</td><td>0.0373</td><td>0.0000</td><td>0.0160</td><td>0.0107</td><td>0.0164</td><td>0.0705</td></tr><tr><td>Capital expenditure</td><td>0.0000</td><td>0.0000</td><td>0.1192</td><td>0.0038</td><td>0.0433</td><td>0.1426</td></tr><tr><td>Cash conversion cycle</td><td>0.0325</td><td>0.0000</td><td>0.0160</td><td>0.0107</td><td>0.0264</td><td>0.0745</td></tr><tr><td>Cash ratio</td><td>0.0000</td><td>0.0061</td><td>0.0586</td><td>0.0107</td><td>0.2752</td><td>0.2970</td></tr><tr><td>Financial debt ratio</td><td>0.0941</td><td>0.0000</td><td>0.0586</td><td>0.0000</td><td>0.0358</td><td>0.1661</td></tr><tr><td>Foreign sales ratio</td><td>0.0000</td><td>0.0053</td><td>0.0110</td><td>0.0107</td><td>0.0930</td><td>0.1015</td></tr><tr><td>Leverage ratio</td><td>0.0178</td><td>0.0417</td><td>0.0160</td><td>0.0286</td><td>0.3164</td><td>0.3570</td></tr><tr><td>LnAssets</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>4.3149</td></tr><tr><td>Long-term assets ratio</td><td>0.0044</td><td>0.0000</td><td>0.0160</td><td>0.0107</td><td>0.0990</td><td>0.1103</td></tr><tr><td>Net profit growth rate</td><td>0.0160</td><td>0.0094</td><td>0.0160</td><td>0.0107</td><td>0.0621</td><td>0.0978</td></tr><tr><td>Net profit margin</td><td>0.0103</td><td>0.0000</td><td>0.0160</td><td>0.0107</td><td>0.2859</td><td>0.2734</td></tr><tr><td>Quick ratio</td><td>0.1334</td><td>0.0736</td><td>0.0766</td><td>0.0107</td><td>0.0178</td><td>0.2747</td></tr><tr><td>Return on assets</td><td>0.0807</td><td>0.0213</td><td>0.0891</td><td>0.0107</td><td>0.0937</td><td>0.2566</td></tr><tr><td>Sales growth rate</td><td>0.0124</td><td>0.0131</td><td>0.0009</td><td>0.0107</td><td>0.0261</td><td>0.0543</td></tr></table>

## 5.3. Prediction results for market-to-book ratio

In this experiment, market-to book ratio was chosen as the dependent variables. These same inputs (independent variables) were used to determine market-to-book ratio output variable. Table 10 revealed the performance measurements of the prediction models from 2005 to 2011. According to overall accuracy rates, C5.0 was the best performing model with approximately 85%, while the ensemble model performed with 81% rate as the second best prediction model. It is expected that the ensemble model usually produced better accuracy rates than the individual models. CART and Neural Networks were the next best prediction models with 74% and 73% respectively. QUEST and CHAID decision tree models had the lowest prediction rate with almost 70% and 68% respectively. Besides overall accuracy rate performance measurement, precision, F-measure, AUC, sensitivity and speci<sup>fi</sup>city also indicated that C5.0 was the outperforming prediction model while the ensemble model was the next best performing model for predicting market-to-book ratio between 2005 and 2011. Successful and unsuccessful <sup>fi</sup>rms' predictions by the models were indicated using confusion matrix in Table 11 between 2005 and 2011. As the results shows, C5.0 and ensemble models predicted successful <sup>fi</sup>rms with 88% and 86% accuracy rates respectively, they were the leading models. CART decision tree model predicted successful cases with almost 80% as the third best model, while QUEST and Neural Network predicted it with 78% and 74% accuracy rate. CHAID was the weakest model for predicting successful <sup>fi</sup>rms with 65%. According to the obtained results, unsuccessful <sup>fi</sup>rms were predicted very well with the C5.0 decision tree model and Ensemble model with 83% and 77% accuracy rate respectively. Except the QUEST decision tree model, all other prediction models predicted the unsuccessful class with over 70% accuracy rate.

![](/api/attachments/YM3URWNE/fulltext/images/04678064c60498e7566b9aea3c8535eb73c09d33e17c86ecc615781514533307.jpg)  
Fig. 3. Illustration of Neural Network used in this study.

Table 10  
Prediction results for market-to-book ratio (2005–2011).

<table><tr><td></td><td>Accuracy (AC)</td><td>Sensitivity/True Positive Rate/Recall (TP)</td><td>Specificity/True Negative rate (TN)</td><td>False Positive rate (FP)</td><td>False Negative rate (FN)</td><td>Precision (P)</td><td>F-measure</td><td>Area under curve (AUC)</td></tr><tr><td>C5.0</td><td>0.8544</td><td>0.8251</td><td>0.8842</td><td>0.1158</td><td>0.1749</td><td>0.8782</td><td>0.8508</td><td>0.9340</td></tr><tr><td>C&amp;R Tree</td><td>0.7418</td><td>0.6550</td><td>0.8297</td><td>0.1703</td><td>0.3450</td><td>0.7956</td><td>0.7185</td><td>0.7940</td></tr><tr><td>QUEST</td><td>0.6964</td><td>0.5557</td><td>0.8388</td><td>0.1612</td><td>0.4443</td><td>0.7773</td><td>0.6481</td><td>0.7110</td></tr><tr><td>CHAID</td><td>0.6797</td><td>0.7688</td><td>0.5895</td><td>0.4105</td><td>0.2312</td><td>0.6546</td><td>0.7071</td><td>0.7350</td></tr><tr><td>Neural Network</td><td>0.7284</td><td>0.7070</td><td>0.7500</td><td>0.2500</td><td>0.2930</td><td>0.7411</td><td>0.7237</td><td>0.8130</td></tr><tr><td>Ensemble</td><td>0.8109</td><td>0.7476</td><td>0.8750</td><td>0.1250</td><td>0.2524</td><td>0.8582</td><td>0.7991</td><td>N/A</td></tr></table>

Prediction models' performance measurements as well as per-class accuracy rates of successful and unsuccessful <sup>fi</sup>rms' performance results are shown in Tables 12 and 13 for the period 1997–2004. The obtained results reveal strong consistency with the result from 2005 to 2011. Again, C5.0 and the ensemble models were the outperformed models with approximately 80% and 78% overall accuracy rates in the order given. C5.0 and ensemble models outperformed in sensitivity, speci<sup>fi</sup>city, precision and F-measure performance measures. The same models demonstrated a strong predictive ability in previous experiments as well. In terms of per-class accuracy rates, C5.0 and the ensemble models predicted successful <sup>fi</sup>rms with 87% and 77% respectively, while the rest of the models revealed strong accuracy rates with above 70% accuracy rates. For unsuccessful <sup>fi</sup>rms' prediction, the ensemble and C5.0 models demonstrated high predictive results with 78% and 75% accuracy rates. While CHAID and CART decision tree models predicted unsuccessful <sup>fi</sup>rms with above 70% accuracy rates, Neural Network and QUEST models showed weak prediction results with 68% and 65% accuracy rates in terms of market-to-book ratio.

Confusion matrices of the models based on 10-fold cross validation test data (market-to-book ratio, 2005–2011)

<table><tr><td>Model type</td><td></td><td>Unsuccessful (0)</td><td colspan="3">Successful (1)</td><td>Overall accuracy</td><td>Per-class accuracy</td></tr><tr><td rowspan="3">C5.0</td><td>Unsuccessful (0)</td><td>1443</td><td>189</td><td>Correct</td><td>2806</td><td>85.44%</td><td>83.31%</td></tr><tr><td>Successful (1)</td><td>289</td><td>1363</td><td>Wrong</td><td>478</td><td>14.56%</td><td>87.82%</td></tr><tr><td>Sum</td><td>1732</td><td>1552</td><td></td><td>3284</td><td></td><td></td></tr><tr><td rowspan="3">C&amp;R Tree</td><td>Unsuccessful (0)</td><td>1354</td><td>278</td><td>Correct</td><td>2436</td><td>74.18%</td><td>70.37%</td></tr><tr><td>Successful (1)</td><td>570</td><td>1082</td><td>Wrong</td><td>848</td><td>25.82%</td><td>79.56%</td></tr><tr><td>Sum</td><td>1924</td><td>1360</td><td></td><td>3284</td><td></td><td></td></tr><tr><td rowspan="3">QUEST</td><td>Unsuccessful (0)</td><td>1369</td><td>263</td><td>Correct</td><td>2287</td><td>69.64%</td><td>65.10%</td></tr><tr><td>Successful (1)</td><td>734</td><td>918</td><td>Wrong</td><td>997</td><td>30.36%</td><td>77.73%</td></tr><tr><td>Sum</td><td>2103</td><td>1181</td><td></td><td>3284</td><td></td><td></td></tr><tr><td rowspan="3">CHAID</td><td>Unsuccessful (0)</td><td>962</td><td>670</td><td>Correct</td><td>2232</td><td>67.97%</td><td>71.58%</td></tr><tr><td>Successful (1)</td><td>382</td><td>1270</td><td>Wrong</td><td>1052</td><td>32.03%</td><td>65.46%</td></tr><tr><td>Sum</td><td>1344</td><td>1940</td><td></td><td>3284</td><td></td><td></td></tr><tr><td rowspan="3">Neural Network</td><td>Unsuccessful (0)</td><td>1224</td><td>408</td><td>Correct</td><td>2392</td><td>72.84%</td><td>71.66%</td></tr><tr><td>Successful (1)</td><td>484</td><td>1168</td><td>Wrong</td><td>892</td><td>27.16%</td><td>74.11%</td></tr><tr><td>Sum</td><td>1708</td><td>1576</td><td></td><td>3284</td><td></td><td></td></tr><tr><td rowspan="3">Ensemble</td><td>Unsuccessful (0)</td><td>1428</td><td>204</td><td>Correct</td><td>2663</td><td>81.09%</td><td>77.40%</td></tr><tr><td>Successful (1)</td><td>417</td><td>1235</td><td>Wrong</td><td>621</td><td>18.91%</td><td>85.82%</td></tr><tr><td>Sum</td><td>1845</td><td>1439</td><td></td><td>3284</td><td></td><td></td></tr></table>

Prediction results for market-to-book ratio (1997–2004).

<table><tr><td></td><td>Accuracy (AC)</td><td>Sensitivity/True Positive Rate/Recall (TP)</td><td>Specificity/True Negative rate (TN)</td><td>False Positive rate (FP)</td><td>False Negative rate (FN)</td><td>Precision (P)</td><td>F-measure</td><td>Area under curve (AUC)</td></tr><tr><td>C5.0</td><td>0.7998</td><td>0.7027</td><td>0.8952</td><td>0.1048</td><td>0.2973</td><td>0.8684</td><td>0.7768</td><td>0.8580</td></tr><tr><td>C&amp;R Tree</td><td>0.7120</td><td>0.6912</td><td>0.7325</td><td>0.2675</td><td>0.3088</td><td>0.7177</td><td>0.7042</td><td>0.7650</td></tr><tr><td>QUEST</td><td>0.6767</td><td>0.5725</td><td>0.7792</td><td>0.2208</td><td>0.4275</td><td>0.7184</td><td>0.6372</td><td>0.7000</td></tr><tr><td>CHAID</td><td>0.7348</td><td>0.7305</td><td>0.7389</td><td>0.2611</td><td>0.2695</td><td>0.7336</td><td>0.7320</td><td>0.8270</td></tr><tr><td>Neural Network</td><td>0.6901</td><td>0.6446</td><td>0.7349</td><td>0.2651</td><td>0.3554</td><td>0.7052</td><td>0.6735</td><td>0.7280</td></tr><tr><td>Ensemble</td><td>0.7766</td><td>0.7805</td><td>0.7728</td><td>0.2272</td><td>0.2195</td><td>0.7717</td><td>0.7761</td><td>n/a</td></tr></table>

Table 13  
Confusion matrices of the models based on 10-fold cross validation test data (market-to-book ratio, 1997–2004).

<table><tr><td>Model type</td><td></td><td>Unsuccessful (0)</td><td>Successful (1)</td><td></td><td></td><td>Overall accuracy</td><td>Per-class accuracy</td></tr><tr><td rowspan="3">C5.0</td><td>Unsuccessful (0)</td><td>1111</td><td>130</td><td>Correct</td><td>1969</td><td>79.98%</td><td>75.37%</td></tr><tr><td>Successful (1)</td><td>363</td><td>858</td><td>Wrong</td><td>493</td><td>20.02%</td><td>86.84%</td></tr><tr><td>Sum</td><td>1474</td><td>988</td><td></td><td>2462</td><td></td><td></td></tr><tr><td rowspan="3">C&amp;R Tree</td><td>Unsuccessful (0)</td><td>909</td><td>332</td><td>Correct</td><td>1753</td><td>71.20%</td><td>70.68%</td></tr><tr><td>Successful (1)</td><td>377</td><td>844</td><td>Wrong</td><td>709</td><td>28.80%</td><td>71.77%</td></tr><tr><td>Sum</td><td>1286</td><td>1176</td><td></td><td>2462</td><td></td><td></td></tr><tr><td rowspan="3">QUEST</td><td>Unsuccessful (0)</td><td>967</td><td>274</td><td>Correct</td><td>1666</td><td>67.67%</td><td>64.94%</td></tr><tr><td>Successful (1)</td><td>522</td><td>699</td><td>Wrong</td><td>796</td><td>32.33%</td><td>71.84%</td></tr><tr><td>Sum</td><td>1489</td><td>973</td><td></td><td>2462</td><td></td><td></td></tr><tr><td rowspan="3">CHAID</td><td>Unsuccessful (0)</td><td>917</td><td>324</td><td>Correct</td><td>1809</td><td>73.48%</td><td>73.60%</td></tr><tr><td>Successful (1)</td><td>329</td><td>892</td><td>Wrong</td><td>653</td><td>26.52%</td><td>73.36%</td></tr><tr><td>Sum</td><td>1246</td><td>1216</td><td></td><td>2462</td><td></td><td></td></tr><tr><td rowspan="3">Neural Network</td><td>Unsuccessful (0)</td><td>912</td><td>329</td><td>Correct</td><td>1699</td><td>69.01%</td><td>67.76%</td></tr><tr><td>Successful (1)</td><td>434</td><td>787</td><td>Wrong</td><td>763</td><td>30.99%</td><td>70.52%</td></tr><tr><td>Sum</td><td>1346</td><td>1116</td><td></td><td>2462</td><td></td><td></td></tr><tr><td rowspan="3">Ensemble</td><td>Unsuccessful (0)</td><td>959</td><td>282</td><td>Correct</td><td>1912</td><td>77.66%</td><td>78.16%</td></tr><tr><td>Successful (1)</td><td>268</td><td>953</td><td>Wrong</td><td>550</td><td>22.34%</td><td>77.17%</td></tr><tr><td>Sum</td><td>1227</td><td>1235</td><td></td><td>2462</td><td></td><td></td></tr></table>

## 5.4. Sensitivity analysis results for market-to-book ratio

The same procedure for sensitivity analysis was employed for market-to-book ratio dependent variable. The obtained relative importance values were normalized and then they were fused using information fusion-based sensitivity analysis order to combine these values as a single predictor importance value in both time intervals: 1997–2004 and 2005–2011. These values aggregated into a tabular form and then they were illustrated in bar-charts. Table 14 and Fig. 4 represent sensitivity analysis results from 2005 to 2011 for prediction market-tobook ratio. As results indicate, leverage ratio was the most important factor in all models; therefore, it is the most signi<sup>fi</sup>cant <sup>fi</sup>nancial ratio for prediction market-to-book ratio. Also, return on assets, LnAssets, and quick ratio were the followed most important predictors in order for determining market-to-book ratio. Assets growth rate, foreign sales ratio, and sales growth rate were the least important predictors for market-to-book ratio (Figs. 6 and 7).

Table 15 and Fig. 5 show the sensitivity analysis results between 1997 and 2004 for predicting market-to-book ratio. After obtaining the linear combination (fused) scores for each predictor of each model in the table, the values were illustrated on a bar-chart. According to the fused sensitivity analysis results, leverage ratio was the most important predictor, while asset turnover rate, LnAssets, and Return on assets were the next important variables for determining market-to-book ratio. These indicate consistency as well with the sensitivity result between 2005 and 2011. In both time intervals, leverage ratio came out as the most important predictor.

## 6. Conclusion and implications

The impact of multinationality (as measured by foreign sales ratio) and fourteen other <sup>fi</sup>nancial indicators on market capitalization and market-to-book ratio for the period of 1997–2011 was investigated using decision tree and neural network algorithms. We divided the time period of 1997–2011 into two periods; 1997–2004 and 2005–2011 to check the robustness of results pre- and post-IFRS implementation.

The in<sup>fl</sup>uence of multinationality and other <sup>fi</sup>nancial indicators were investigated on market capitalization for the period of 2005–2011, which also covers IFRS implementation period. We found that the most important predictor on market capitalization was <sup>fi</sup>rm size as measured by natural logarithm of assets. This variable was signi<sup>fi</sup>cantly distinguished from other <sup>fi</sup>nancial indicators. The other variables which have been found to have explanatory power on market capitalization were leverage, liquidity (i.e. cash ratio and quick ratio), and pro<sup>fi</sup>tability (i.e. net pro<sup>fi</sup>t margin and return on assets). Among the independent variables included in the study, multinationality was found to determine market value only moderately. When the analysis was conducted pre-IFRS implementation for the period of 1997–2004, as the results indicate, <sup>fi</sup>rm size was again the leading predictor of market value. Other variables that were important predictor for this period were profitability (i.e. net pro<sup>fi</sup>t margin and return on assets), leverage, liquidity (i.e. cash ratio), and asset growth rate. In this period, multinationality was among the least important variables. Thus, based on the limits of the study, we may deduce that the obtained results were robust and consistent for the two periods even though there were minor differences. These results, based on the usage of market capitalization as a dependent variable, do not provide implications regarding growth opportunities for <sup>fi</sup>rms. They basically reveal that the larger the <sup>fi</sup>rm size, as measured by sales revenues, the higher the market value.

Aggregated sensitivity analysis results of market-to-book ratio (2005-2011).

<table><tr><td></td><td>C5.0</td><td>CHAID</td><td>C&amp;R Tree</td><td>QUEST</td><td>Neural Network</td><td>PI (fused)</td></tr><tr><td>Asset turnover rate</td><td>0.0000</td><td>0.0647</td><td>0.0000</td><td>0.0488</td><td>0.3703</td><td>0.3477</td></tr><tr><td>Assets growth rate</td><td>0.0019</td><td>0.0382</td><td>0.0000</td><td>0.0488</td><td>0.0000</td><td>0.0616</td></tr><tr><td>Capital expenditure</td><td>0.0000</td><td>0.1204</td><td>0.1120</td><td>0.1357</td><td>0.1407</td><td>0.3619</td></tr><tr><td>Cash conversion cycle</td><td>0.4007</td><td>0.0479</td><td>0.0000</td><td>0.0488</td><td>0.2623</td><td>0.6000</td></tr><tr><td>Cash ratio</td><td>0.0864</td><td>0.0929</td><td>0.0000</td><td>0.0488</td><td>0.2488</td><td>0.3522</td></tr><tr><td>Financial debt ratio</td><td>0.3405</td><td>0.0000</td><td>0.0000</td><td>0.0488</td><td>0.0362</td><td>0.3514</td></tr><tr><td>Foreign sales ratio</td><td>0.0355</td><td>0.0280</td><td>0.0000</td><td>0.0488</td><td>0.1294</td><td>0.1775</td></tr><tr><td>Leverage ratio</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>3.7007</td></tr><tr><td>LnAssets</td><td>0.3529</td><td>0.4271</td><td>0.2099</td><td>0.0243</td><td>0.6965</td><td>1.2718</td></tr><tr><td>Long-term assets ratio</td><td>0.1928</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.2814</td><td>0.3698</td></tr><tr><td>Net profit growth rate</td><td>0.2684</td><td>0.2002</td><td>0.0151</td><td>0.0488</td><td>0.0299</td><td>0.4323</td></tr><tr><td>Net profit margin</td><td>0.0000</td><td>0.0000</td><td>0.0458</td><td>0.0488</td><td>0.5814</td><td>0.4914</td></tr><tr><td>Quick ratio</td><td>0.5519</td><td>0.0382</td><td>0.0000</td><td>0.0000</td><td>0.5423</td><td>0.8925</td></tr><tr><td>Return on assets</td><td>0.5426</td><td>0.3009</td><td>0.4587</td><td>0.4260</td><td>0.8607</td><td>1.9320</td></tr><tr><td>Sales growth rate</td><td>0.0841</td><td>0.0739</td><td>0.0000</td><td>0.0488</td><td>0.0931</td><td>0.2239</td></tr></table>

![](/api/attachments/YM3URWNE/fulltext/images/b2bbcba4deec122235579719a338cd77664c85d7aaff314f73f6937cbee61d81.jpg)  
Fig. 4. Graphical representation of sensitivity analysis result for market capitalization (2005–2011).

Furthermore, we scaled market value by book value (market-tobook ratio) to investigate the impact of multinationality and other <sup>fi</sup>nancial characteristics of <sup>fi</sup>rms on market value relative to book value. We have found that leverage ratio was the most important indicator in both periods 1997–2004 and 2005–2011. Moreover, <sup>fi</sup>rm size, pro<sup>fi</sup>tability, and liquidity were the next leading indicators for marketto-book ratio in both periods 1997–2004 and 2005–2011.

The results have important capital market implications. International activities of Turkish <sup>fi</sup>rms do not have as much importance as expected on the <sup>fi</sup>rm value. In other words, investors may choose to consider some other <sup>fi</sup>rm characteristics rather than multinationality, and therefore they may have a greater impact on share prices and eventually on the <sup>fi</sup>rm value. As pointed out in the literature part, there is no consensus on the effect of multinationality on <sup>fi</sup>rm value; while some studies proved that it increases <sup>fi</sup>rm value, whereas some others proved that it reduces <sup>fi</sup>rm value. If market-to-book ratio is considered to be an indicator of growth opportunities, we can say that multinationality has little effect on <sup>fi</sup>rm's growth opportunities. Therefore, our <sup>fi</sup>nding

![](/api/attachments/YM3URWNE/fulltext/images/b4b8694c66d2890fe768bb3753cf6f518ada721ab3515895717e623427b965bc.jpg)  
Fig. 5. Graphical representation of sensitivity analysis result for market capitalization (1997–2004).

![](/api/attachments/YM3URWNE/fulltext/images/bd2116b36582d084bef6ab34c3f86f7f8c84e9137f63564d156a34be67290eda.jpg)  
Fig. 6. Graphical representation of sensitivity analysis result for market-to-book ratio (2005–2011).

corroborates the arguments and <sup>fi</sup>ndings of those prior studies that we could not <sup>fi</sup>nd a strong support for the effect of multinationality on <sup>fi</sup>rm value. Other than multinationality, some <sup>fi</sup>nancial characteristics were consistently found to affect both <sup>fi</sup>rm value variables (market capitalization and market-to-book ratio), and in both periods (i.e., 1997–2004 and 2005–2011). Our research yielded that the similar predictive variables, such as <sup>fi</sup>rm size, pro<sup>fi</sup>tability, and leverage, are playing a leading role on market-to-book ratio before and after IFRS adoption. Firm size has been found as an important indicator of <sup>fi</sup>rm value. It might be due to the number of shares issued by <sup>fi</sup>rms and/or price of their shares. In addition, size in<sup>fl</sup>uences the growth expectations of <sup>fi</sup>rms. Pro<sup>fi</sup>tability is one of the most important variables for investment decisions. Investors consider it while buying, holding or selling shares of a <sup>fi</sup>rm, and also analysts follow pro<sup>fi</sup>tability of <sup>fi</sup>rms closely while making investment recommendations to and decision on behalf of their customers. Both pro<sup>fi</sup>tability and leverage are two signi<sup>fi</sup>cant variables that play important roles in terms of the growth opportunities of <sup>fi</sup>rms, since both are essential sources of funding. Pro<sup>fi</sup>tability is an internal source of funding generated as a result of operations, while leverage is an external source of funding applied in instances where the internal source of <sup>fi</sup>nancing is insuf<sup>fi</sup>cient to <sup>fi</sup>nance growth. Moreover, debt paying ability of a <sup>fi</sup>rm is important for its investors since it shows how a company is able to keep itself away from <sup>fi</sup>nancial risk and bankruptcy. Debt level impacts pro<sup>fi</sup>tability of a company due to the interest burden that they have to face from borrowing. Thus, liquidity and leverage are two important determinants of <sup>fi</sup>rm value. While the former measures short-term debt paying ability of a <sup>fi</sup>rm, the latter measures long-term solvency of a <sup>fi</sup>rm.

![](/api/attachments/YM3URWNE/fulltext/images/b95cedc05d8ba521c059675575b64fcbc329527c686eb1e1b7eb4919ac660b2d.jpg)  
Fig. 7. Graphical representation of sensitivity analysis result for market-to-book ratio (1997–2004).

Table 15  
Aggregated sensitivity analysis results of market-to-book ratio (1997–2004).

<table><tr><td></td><td>C5.0</td><td>CHAID</td><td>C&amp;R Tree</td><td>QUEST</td><td>Neural Network</td><td>PI (fused)</td></tr><tr><td>Asset turnover rate</td><td>1.0000</td><td>0.5534</td><td>1.0000</td><td>0.1776</td><td>0.4509</td><td>2.3497</td></tr><tr><td>Assets growth rate</td><td>0.0784</td><td>0.0847</td><td>0.0794</td><td>0.0000</td><td>0.6308</td><td>0.6167</td></tr><tr><td>Capital expenditure</td><td>0.0202</td><td>0.0121</td><td>0.0794</td><td>0.0000</td><td>0.4718</td><td>0.4072</td></tr><tr><td>Cash conversion cycle</td><td>0.0405</td><td>0.3215</td><td>0.2034</td><td>0.0000</td><td>0.5265</td><td>0.7768</td></tr><tr><td>Cash ratio</td><td>0.2181</td><td>0.1886</td><td>0.0794</td><td>0.0000</td><td>0.2242</td><td>0.5242</td></tr><tr><td>Financial debt ratio</td><td>0.0000</td><td>0.0495</td><td>0.0794</td><td>0.2678</td><td>0.0000</td><td>0.2742</td></tr><tr><td>Foreign sales ratio</td><td>0.3426</td><td>0.0000</td><td>0.3259</td><td>0.0000</td><td>0.1025</td><td>0.5768</td></tr><tr><td>Leverage ratio</td><td>0.4845</td><td>0.5061</td><td>0.6492</td><td>1.0000</td><td>1.0000</td><td>2.5884</td></tr><tr><td>LnAssets</td><td>0.4902</td><td>0.2179</td><td>0.6166</td><td>0.0709</td><td>0.6012</td><td>1.4540</td></tr><tr><td>Long-term assets ratio</td><td>0.0392</td><td>0.0000</td><td>0.3909</td><td>0.0456</td><td>0.3258</td><td>0.5654</td></tr><tr><td>Net profit growth rate</td><td>0.1621</td><td>0.0000</td><td>0.0059</td><td>0.0000</td><td>0.2606</td><td>0.3138</td></tr><tr><td>Net profit margin</td><td>0.0278</td><td>0.1407</td><td>0.0000</td><td>0.0000</td><td>0.2954</td><td>0.3295</td></tr><tr><td>Quick ratio</td><td>0.1157</td><td>0.0377</td><td>0.0794</td><td>0.0000</td><td>0.3797</td><td>0.4388</td></tr><tr><td>Return on assets</td><td>0.1391</td><td>1.0000</td><td>0.0434</td><td>0.0451</td><td>0.1103</td><td>0.9836</td></tr><tr><td>Sales growth rate</td><td>0.0025</td><td>0.0000</td><td>0.0794</td><td>0.0000</td><td>0.2346</td><td>0.2205</td></tr></table>

## References

[1] F.A. Alali, P.S. Foote, The value relevance of international <sup>fi</sup>nancial reporting standards: empirical evidence in an emerging market, Int. J. Account. 47 (2012) 85–108.

[2] E. Alfaro, N. García, M. Gámez, D. Elizondo, Bankruptcy forecasting: an empirical comparison of AdaBoost and neural networks, Decis. Support. Syst. 45 (1) (2008) 110–122.

[3] M. Ammanna, D. Oesch, M.M. Schmid, Corporate governance and <sup>fi</sup>rm value: international evidence, J. Empir. Finance 18 (2011) 36–55.

[4] O.A. Anam, A.H. Fatima, A.R.H. Majdi, Effects of intellectual capital information disclosed in annual reports on market capitalization: evidence from Bursa Malaysia, J. Hum. Resour. Costing Acc. 15 (2) (2011) 85–101.

[5] M. Anandarajan, P. Lee, A. Anandarajan, Bankruptcy prediction of <sup>fi</sup>nancially stressed <sup>fi</sup>rms: an examination of the predictive accuracy of arti<sup>fi</sup>cial neural networks, Int. J. Intell. Syst. Account. Finance Manag. 10 (2001) 69–81.

[6] A. Atiya, Bankruptcy prediction for credit risk using neural networks: a survey and new results, IEEE Trans. Neural Networks 12 (4) (2001).

[7] S.C. Bae, S. Noh, Multinational corporations versus domestic corporations: a comparative study of R&D investment activities, J. Multinatl. Financ. Manag. 11 (2001) 89–104.

[8] S.C. Bae, T.H. Kwon, J.W. Lee, Does corporate diversi<sup>fi</sup>cation by business groups create value? Evidence from Korean chaebols, Pac. Basin Financ. J. 19 (2011) 535–553.

[9] R. Barniv, A. Agarwal, R. Leach, Predicting the outcome following bankruptcy <sup>fi</sup>ling: a three-state classi<sup>fi</sup>cation using neural networks, Intell. Syst. Acc. Financ. Manag. 6 (1997).177-194

[10] T. Bell, Neural nets or the logit model? A comparison of each model's ability to predict commercial bank failures, Intell. Syst. Acc. Financ. Manag. 6 (1997) 249–264.

[11] J. Berrill, G. Mannella, Are <sup>fi</sup>rms from developed markets more international than <sup>fi</sup>rms from emerging markets? Research in International Business and Fi nance2012. (http://dx,doi,org/10.1016/i,ribaf,2012.04.002).

[12] B. Black, W. Kim, The effect of board structure on <sup>fi</sup>rm value: a multiple identi<sup>fi</sup>ca tion strategies approach using Korean data, J. Financ. Econ. 104 (2012) 203–226.

[13] B.S. Black, I. Love, A. Rachinsky, Corporate governance indices and <sup>fi</sup>rms' market values: time series evidence from Russia, Emerg. Mark. Rev. 7 (2006) 361–379.

[14] J. Boritz, D. Kennedy, Effectiveness of neural networks types for prediction of business failure, Expert Syst. Appl. 9 (1995) 503–512.

[15] L. Breiman, J.H. Friedman, R.A. Olshen, C.J. Stone, Classi<sup>fi</sup>cation and Regression Trees, Chapman & Hall/CRC, New York, 1984.

[16] G. Cassar, S. Holmes, Capital structure and <sup>fi</sup>nancing of SMEs: Australian evidence, Account. Finance 43 (2003) 123–147.

[17] R.E. Caves, International corporations: the industrial economics of foreign investment, Economica 38 (149) (1971) 1–27.

[18] W. Chaehwan, K. Jinhwa, K.B. Jae, Using genetic algorithm based knowledge re<sup>fi</sup>nement model for dividend policy forecasting, Expert Syst. Appl. 39 (2012) 13472–13479.

[19] C. Charalambous, A. Charitous, F. Kaourou, Comparative analysis of arti<sup>fi</sup>cial neural net work models: application in bankruptcy prediction, Ann. Oper. Res. 99 (2000) 403–425.

[20] R. Charles, C.R. Hulten, X. Hao, What is a company really worth? Intangible capital and the “market to book value” puzzle, NBER Working Paper Series, Working Paper 145482008. (Retrieved from http://www.nber.org/papers/w14548 on 08.01.2013).

[21] M.C. Chen, S.H. Huang, Credit scoring and rejected instances reassigning through evolutionary computation techniques, Expert Syst. Appl. 24 (4) (2003) 433–441.

[22] T. Chih-Fong, L. Yu-Hsin, C.Y. David. Determinants of intangible assets value: the data mining approach, Knowl-Based Syst, 31 (2012) 67–77

[23] J.T. Connelly, P. Limpaphayom, N.J. Nagarajan, Form versus substance: the effect of ownership structure and corporate governance on <sup>fi</sup>rm value in Thailand, J. Bank Financ. 36 (2012) 1722–1743.

[24] M. Darrough, J. Ye, Valuation of loss <sup>fi</sup>rms in a knowledge-based economy, Rev. Acc, Stud, 12 (2007) 61–93

[25] G. Davis, Sensitivity analysis in neural net solutions, IEEE Trans. Syst. Man Cybern. 19 (1989) 1078–1082.

[26] B.E. Deakin, A discriminant analysis of predictors of business failure, J. Account. Res. 167-179 (1976).

[27] H. DeAngelo, R. Masulis, Optimal capital structure under corporate and personal taxation L Financ, Econ, 8 (1980) 5–29.

[28] D. Delen, A comparative analysis of machine learning techniques for student retention management, Decis. Support. Syst. 49 (2010) 498–506.

[29] D. Delen, A. Oztekin, L. Tomak, An analytic approach to better understanding and management of coronary surgeries, Decis. Support. Syst. 52 (2012) 698–705.

[30] D.J. Denis, D.K. Denis, K. Yost, Global diversi<sup>fi</sup>cation, industrial diversi<sup>fi</sup>cation, and <sup>fi</sup>rm value, J. Financ. 57 (5) (2002) 1951–1979.

[31] S. Eckert, M. Dittfeld, T. Muche, S. Rässler, Does multinationality lead to value enhancement? An empirical examination of publicly listed corporations from Germany, Int. Bus. Rev. 19 (2010) 562–574.

[32] J. Erickson, Y.W. Park, J. Reising, H.-H. Shin, Board composition and <sup>fi</sup>rm value under concentrated ownership: the Canadian evidence, Pac. Basin Financ. J. 13 (2005) 387–410.

[33] V.R. Errunza, L.W. Senbet, The effects of international operations on the market value of the <sup>fi</sup>rm: theory and evidence, J. Financ. 36 (2) (1981) 401–417.

[34] O. Faleye, Classi<sup>fi</sup>ed boards, <sup>fi</sup>rm value, and managerial entrenchment, J. Financ Econ. 83 (2007)501–529

[35] L. Fauver, J.F. Houston, A. Naranjo, Cross-country evidence on the value of corporate industrial and international diversi<sup>fi</sup>cation, J. Corp. Finance 10 (2004) 729–752.

[36] C.M. Fuller, D.P. Biros, D. Delen, An investigation of data and text mining methods for real world deception detection, Expert Syst. Appl. 38 (2011) 8392–8398.

[37] S.J. Grice, T.M. Dugan, The limitations of bankruptcy prediction models: some cautions for the researcher, Rev. Quant. Finan. Acc. 17 (2001) 151–166.

[39] O.A.G. Hassan, G. Giorgioni, P. Romilly, D. Power, The value-relevance of disclosure: evidence from the emerging capital market of Egypt, Int. J. Account. 44 (1) (2009) 79–102.

[40] S. Haykin, Neural Networks and Learning Machines, 3rd ed. Prentice Hall Publishing, Englewood Cliffs, New Jersey, 2008.

[41] T. Hiraki, H. Inoue, A. Ito, F. Kuroki, H. Masuda, Corporate governance and <sup>fi</sup>rm value in Japan: evidence from 1985 to 1998, Pac. Basin Financ. J. 11 (2003) 239–265.

[42] C.W. Holsapple, J. Wu, An elusive antecedent of superior <sup>fi</sup>rm performance: the knowledge management factor, Decis, Support, Syst, 52 (1) (2011) 271–283

[43] Z. Huang, H. Chen, C.-J. Hsu, Credit rating analysis with support vector machine and neural networks: a market comparative study, Decis. Support. Syst. 37 (2004) 543–558.

[44] M.C. Jensen, Agency costs of free cash <sup>fl</sup>ow, corporate <sup>fi</sup>nance, and takeovers, Am. Econ. Rev. 76 (2) (1986) 323–329.

[45] M.C. Jensen, W.H. Meckling, Theory of the <sup>fi</sup>rm: managerial behavior, agency costs and ownership structure. I. Financ. Econ. 3 (4) (1976) 305–360

[46] C.-H. Jiang, H.-L. Chen, Y.-S. Huang, Capital expenditures and corporate earnings: evidence from the Taiwan Stock Exchange, Manag. Financ. 32 (11) (2006) 853–861.

[47] G. Kass, An exploratory technique for investigating large quantities of categorical data, Appl. Stat. 29 (2) (1980) 119–127.

[48] K.J. Kim, Financial time series forecasting using support vector machines, Neurocomputing 55 (1/2) (2003) 307–319.

[49] Y.S. Kim, I. Mathur, The impact of geographic diversi<sup>fi</sup>cation on <sup>fi</sup>rm performance, Int. Rev. Financ. Anal. 17 (2008) 747–766.

[50] R. Kohavi, F. Provost, Glossary of terms. Editorial for the special issue on applications of machine learning and the knowledge discovery process, Mach. Learn. 30 (2–3) (1998) 271–274.

[51] R. Kohavi, A study of cross-validation and bootstrap for accuracy estimation and model selection The proceedings of the 14th International Conference on AI(IICAI). Morgan Kaufmann San Mateo, CA 1995. 1137–1145.

[52] S.J.J. Konijn, R. Kräussl, A. Lucas, Blockholder dispersion and <sup>fi</sup>rm value, J. Corp. Finance 17 (2011) 1330–1339.

[53] K. Kumar, S. Bhattacharya, Arti<sup>fi</sup>cial neural networks vs. linear discriminant analysis in credit ratings forecast, Rev. Acc. Finance 5 (3) (2006) 216–227.

[54] P.R. Kumar, V. Ravi, Bankruptcy prediction in banks and <sup>fi</sup>rms via statistical and intelligent techniques — a review, Eur. J. Oper. Res. 180 (1) (2007) 1–28.

[55] Y. Kusnadi, Do corporate governance mechanisms matter for cash holdings and <sup>fi</sup>rm value? Pac. Basin Financ. J. 19 (2011) 554–570.

[56] P. Langley, Elements of Machine Learning, Morgan Kaufmann, San Francisco, 1996.

[57] K.C. Lee L. Han Y. Kwon Hybrid neural network models for bankruptcy predictions Decis, Support, Syst, 18 (1) (1996) 63–72

[58] K.T. Lee, C.-W. Hooy, G.-K. Hooy, The value impact of international and industrial diversi<sup>fi</sup>cations on public-listed <sup>fi</sup>rms in Malaysia, Emerg. Mark. Rev. 13 (3) (2012) 366–380.

[59] R. Lensink, R. van der Molen, Does group af<sup>fi</sup>liation increase <sup>fi</sup>rm value for diversi<sup>fi</sup>ed groups? New evidence from Indian companies, J. Empir. Finance 17 (2010) 332–344.

[60] J. Lo'pez-Gracia, F. Sogorb-Mira, Testing trade-off and pecking order theories <sup>fi</sup>nancing SMEs, Small Bus. Econ. 31 (2) (2008) 117–136.

[61] W.Y. Loh, Y.S. Shih, Split selection methods for classi<sup>fi</sup>cation trees, Stat. Sin. 7 (1997) 815–840.

[62] Y.T. Mak, Y. Kusnadi, Size really matters: further evidence on the negative relationship between board size and <sup>fi</sup>rm value, Pac. Basin Financ. J. 13 (2005) 301–318.

[63] P. Malighetti, M. Meoli, S. Paleari, R. Redondi, Value determinants in the aviation industry, Transp. Res. E 47 (2011) 359–370.

[64] A. Martín-Oliver, V. Salas-Fumás, IT assets, organization capital and market power: contributions to business value, Decis. Support. Syst. 52 (3) (2012) 612–623.

[65] A. Mínguez-Vera, J.F. Martín-Ugedo, Does ownership structure affect value? A panel data analysis for the Spanish market, Int. Rev. Financ. Anal. 16 (2007) 81–98. [66] T. Mitchell, Machine Learning, McGraw Hill, New York, 1997.

[68] S. Mukherjee, E. Osuna, F. Girosi, Nonlinear prediction of chaotic time series using support vector, Proceedings of the IEEE Workshop on Neural Networks for Signal Processing, IEEE Publishing, Amelia Island, FL, 1997, pp. 511–520.

[69] S.C. Myers, The capital structure puzzle, J. Financ. 39 (1984) 575–592.

[70] S.C. Myers, R.G. Rajan, The paradox of liquidity, Q. J. Econ. 113 (3) (1998) 733–771.

[71] B. Olsen, B. Elango, Do multinational operations in<sup>fl</sup>uence <sup>fi</sup>rm value? Evidence from the triad regions, Int. J. Bus. Econ. 4 (1) (2005) 11–29.

[72] D.L. Olson, D. Delen, Y. Meng, Comparative analysis of data mining methods for bankruptcy prediction, Decis. Support. Syst. 52 (2) (2012) 464–473.

[73] D.L. Olson, D. Delen, Advanced Data Mining Techniques, Springer, 2008

[74] P.C. Pendharkar, A threshold-varying arti<sup>fi</sup>cial neural network approach for classi-<sup>fi</sup>cation and its application to bankruptcy prediction problem, Comput. Oper. Res. 32 (10) (2005) 2561–2582.

[75] B. Pramborg, Derivatives hedging, geographical diversi<sup>fi</sup>cation, and <sup>fi</sup>rm market value, J. Multinatl. Financ. Manag. 14 (2004) 117–133.

[76] J. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann, San Mateo, CA, 1993. (MA: MIT Press).

[77] A. Riahi-Belkaoui, The effects of the degree of internationalization on <sup>fi</sup>rm performance, Int. Bus. Rev. 7 (1998) 315–321.

[78] A. Riahi-Belkaoui, The degree of internationalization and the value of the <sup>fi</sup>rm: theory and evidence, J. Int. Account. Audit. Tax. 8 (1) (1999) 189–196.

[79] D.E. Rumelhart, J.L. McClelland, PDP research group, Parallel distributed processing: explorations in the microstructure of cognition, vol. IMIT Press, Cambridge, MA, 1986.

[81] A. Saltelli, S. Tarantola, F. Campolongo, M. Ratto, Sensitivity Analysis in Practice — A Guide to Assessing Scienti<sup>fi</sup>c Models, JohnWiley, 2004.

[82] M.M. Schmid, I. Walter, Geographic diversi<sup>fi</sup>cation and <sup>fi</sup>rm value in the <sup>fi</sup>nancial services industry L. Empir, Finance 19 (2012) 109–122

[83] G. Seni, J. Elder, R. Grossman, Ensemble Methods in Data Mining: Improving Accuracy through Combining Predictions, Morgan and Claypool Publishers, San Rafael, C., 2010 [84] SPSS Clementine12 User Manual Chicago IL. 2007

[85] SPSS. IBM SPSS Modeler User Manual, Chicago, II. 2012.

[86] A. Starr, M. Desforges, Strategies in data fusion – sorting through the tool box, Proceedings of European Conference on Data Fusion, 1998.

[87] A. Uyar, M. Kılıç, Value relevance of voluntary disclosure: evidence from Turkish firms. I. Intellect, Cap. 13 (3) (2012) 363–376.

[88] B. Villalonga, R. Amit, How do family ownership, control, and management affect <sup>fi</sup>rm value? J. Financ. Econ. 80 (2006) 385–417.

[89] R.L. Wilson, R. Sharda, Bankruptcy prediction using neural networks, Decis. Support. Syst. 11 (5) (1994) 545–557.

[90] I.H. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Techniques, second ed. Elsevier, San Francisco, 2005.

[91] H. Wu, N. Fargher, S. Wright, Accounting for investments and the relevance of losses to <sup>fi</sup>rm value, Int. J. Account. 45 (2010) 104–127.

[92] H.-L. Wu, Can minority state ownership in<sup>fl</sup>uence <sup>fi</sup>rm value? Universal and contingency views of its governance effects, J. Bus. Res. 64 (2011) 839–845.

[93] P. Ravisankar, V. Ravi, G. Raghava Rao, I. Bose, Detection of <sup>fi</sup>nancial statement fraud and feature selection using data mining techniques, Decis. Support. Syst. 50 (2011) 491–500.

[94] E.W.T. Ngai, Yong Hu, Y.H. Wong, Yijun Chen, Xin Sun, The application of data mining techniques in <sup>fi</sup>nancial fraud detection: a classi<sup>fi</sup>cation framework and an academic review of literature, Decis. Support. Syst. 50 (2011) 559–569.

[95] Wei Zhou, Gaurav Kapoor, Detecting evolutionary <sup>fi</sup>nancial statement fraud, Decis. Support. Syst. 50 (2011) 570–575.

[96] Sean L. Humpherys, Kevin C. Mof<sup>fi</sup>tt, Mary B. Burns, Judee K. Burgoon, William F. Felix Identification of fraudulent financial statements using linguistic credibility analysis, Decis, Support, Syst, 50 (2011) 585–594

[97] Fletcher H. Glancy, Surya B. Yadav, A computational model for <sup>fi</sup>nancial reporting fraud detection, Decis. Support. Syst. 50 (2011) 595–601.

[98] Rich Caruana, Alexandru Niculescu-Mizil, An empirical comparison of supervised learning algorithms. Proceedings of the 23rd international Conference on Machine learning (ICML '06), ACM. New York, NY, USA, 2006, pp. 161–168.

[99] Rich Caruana, Nikos Karampatziakis, Ainur Yessenalina, An empirical evaluation of supervised learning in high dimensions, Proceedings of the 25th International

Conference on Machine learning (ICML '08), ACM, New York, NY, USA, 2008 pp. 96–103.

[100] Eric Bauer, Ron Kohavi, An empirical comparison of voting classi<sup>fi</sup>cation algorithms: bagging, boosting, and variants, Mach. Learn. 36 (1–2) (July 1999) 105–139.

[101] Thomas G. Dietterich, Dietterich, approximate statistical tests for comparing supervised classi<sup>fi</sup>cation learning algorithms, Neural Comput. 10 (7) (Oct. 1998) 1895–1923.

[102] L. Breiman, Statistical modeling: the two cultures, Stat. Sci. 16 (3) (2001) 199–231.

[103] Y. Benjamini, M. Leshno, Statistical methods for data mining, in: O. Maimon, L. Rokach (Eds.), Data Mining and Knowledge Discovery Handbook, 2nd ed., Springer, New York, 2010, pp. 523–541.

[104] J.H. Friedman, Data mining and statistics: what's the connection? Comput. Sci. Stat. 29 (1) (1998) 3–9.

[105] P. Giudici, Data mining model comparison, in: O. Maimon, L. Rokach (Eds.), Data Mining and Knowledge Discovery Handbook, 2nd ed., Springer, New York, 2010, pp. 641–655.

[106] C. Vercellis, Business Intelligence: Data Mining and Optimization for Decision Making, John Wiley. U.K., 2009

![](/api/attachments/YM3URWNE/fulltext/images/80d311032577fa08bac394361cb3aa09fbe229da2ccd31f3e94da8659c96920d.jpg)

Dr. Cemil Kuzey is an Assistant Professor in the Department of Management at Fatih University in Istanbul, Turkey. Dr. Kuzey is primarily teaching Operation Research and Statistics topics for Social Sciences. He acquired his Ph.D degree in Business Administration in the Department of Quantitative Analysis at Istanbul University, Turkey. Among his academic pursuits, he took several graduate courses at the Ontario Institute for Studies in Education, University of Toronto, Canada. His research interests are related to Operation Research, Data Mining, and Business Intelligence

![](/api/attachments/YM3URWNE/fulltext/images/5c4cafaa2a475dbee63455546c37383b87df724a53ffecfd00bdeee60f843475.jpg)

Dr. Ali Uyar is an Associate Professor of Accounting and Finance in the Department of Business Administration at Fatih University in Istanbul, Turkey. He received his Ph.D. in Accounting and Finance from Marmara University, Turkey in 2007. He teaches cost accounting, managerial accounting, and <sup>fi</sup>nancial accounting. His research interests include management accounting practices and corporate reporting. His research papers have been published in various international journals, such as Managerial Auditing Journal, International Journal of Hospitality Management, Journal of Intellectual Capital. Pacific Accounting Review. International Journa of Accounting, Auditing and Performance Evaluation, Inter: national Journal of Quality and Reliability Management, African Journal of Business Management, Business and

Economics Research Journal, Eurasian Journal of Business and Economics, International Research Journal of Finance and Economics, The TQM Journal.

![](/api/attachments/YM3URWNE/fulltext/images/09458ce7f1b78039cff70b5ef0a91526f51a028cec4a2ab4b2eac000abdcec0e.jpg)

Dr. Dursun Delen is the William S. Spears Chair in Business Administration and Professor of Management Science and Information Systems in the Spears School of Business at Oklahoma State University (OSU). He received his Ph.D. in Industrial Engineering and Management from OSU in 1997. Prior to his appointment as an Assistant Professor at OSU in 2001, he worked for a privately-owned research and consultancy company, Knowledge Based Systems Inc., in College Station, Texas, as a research scientist for <sup>fi</sup>ve years, during which he led a number of decision support and other infor mation systems related research projects funded by federal agencies including DoD NASA NIST and DOE, His research has appeared in major journals including Decision Support Systems Decision Sciences, Communications of the ACM

Computers and Operations Research, Computers in Industry, Journal of Production Operations Management, Arti<sup>fi</sup>cial Intelligence in Medicine, Expert Systems with Applications, among others. He recently published four books: Advanced Data Mining Techniques with Springer, 2008; Decision Support and Business Intelligence Systems with Prentice Hall, 2010; Business Intelligence: A Managerial Approach, with Prentice Hall, 2010; and Practical Text Mining and Statistical Analysis for Non-structured Text Data Applications, with Elsevier, 2012. He is often invited to national and international conferences for keynote addresses on topics related to Data/Text Mining, Business Intelligence, Decision Support Systems, and Knowledge Management, He served as the general co-chair for the 4th International Conference on Network Computing and Advanced Information Management (September 2–4. 2008 in Soul. South Korea), and regularly chairs tracks and mini-tracks at various information systems conferences. He is the associate editor-in-chief for International Journal of Experimental Algorithms, associate editor for International Journal of RF Technologies and Decision Analytics, and is on editorial boards of six other academic and technical journals. His research and teaching interests are in data and text mining, decision support systems, knowledge management, business intelligence and enterprise modeling.

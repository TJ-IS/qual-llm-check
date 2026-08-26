---
otero_id: 19582
otero_key: "ZQWBWHMC"
title: "How to enable automated trading engines to cope with news-related liquidity shocks? Extracting signals from unstructured data"
authors: "Sven S. Groth; Michael Siering; Peter Gomber"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.03.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# How to enable automated trading engines to cope with news-related liquidity shocks? Extracting signals from unstructured data

Sven S. Groth, Michael Siering ⁎, Peter Gomber

Goethe University Frankfurt, Grüneburgplatz 1, 60323 Frankfurt, Germany

## a r t i c l e i n f o

Article history: Received 9 July 2012 Received in revised form 10 February 2014 Accepted 6 March 2014 Available online 16 March 2014

Keywords: Automated trading Liquidity Forecasting Text mining e-Finance Simulation

## a b s t r a c t

Financial markets are characterised by high levels of complexity and non-linearity. Information systems have often been applied to support investors by forecasting price changes in securities markets. In addition to the asset price, liquidity represents another <sup>fi</sup>nancial variable that has a high relevance for investors because it constitutes a main determinant of total transaction costs. Previous research has shown that the level of liquidity is affected by the publication of corporate disclosures. To derive an optimal order execution strategy that minimises the transaction costs, investors as well as automated trading engines must be able to anticipate changes in the available market liquidity. However. there is no research on how to forecast the impact of corporate disclosures on market liquidity. Therefore, we propose an IT artefact that allows automated trading engines to appropriately react to news-related liquidity shocks. The system indicates whether the publication of a regulatory corporate disclosure will be followed by a positive liquidity shock, i.e., lower transaction costs compared to historical levels. Utilising text mining techniques, the content of the corporate disclosures is analysed to generate a trading signal. Furthermore, the trading signal is evaluated within a simulation-based use case that considers English and German corporate disclosures and is shown to be of economic value.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Decision-making in the <sup>fi</sup>nancial domain represents a challenging task because <sup>fi</sup>nancial markets are characterised by high levels of complexity and non-linearity [8]. These market characteristics make it dif<sup>fi</sup>cult for decision-makers to quickly adjust their strategies in cases of company-related or economic events. Here, information systems play a crucial role in supporting human and computer-based decisionmakers alike.

Today, the group of computer-based automated<sup>1</sup> traders generates already approximately one-half of the trading activity on major European markets such as Deutsche Börse's Xetra, and the percentage share continues to grow [7]. Computer-based automated traders “emulate a broker's core competence of slicing a large order into a multiplicity of smaller orders and of timing these to minimise the market impact” [13]. The decision on the investment or portfolio allocation itself is performed by the respective portfolio manager at a fund management company, and the primary task of automated traders is to execute the orders that are received from these fund management companies or institutional investors at the best available conditions.

To determine an optimal execution strategy for a pre-de<sup>fi</sup>ned execution time period, i.e., to achieve the best available conditions, automated traders must handle the trade-off between the evolving transaction cost components in the order's execution. Costs that are generated while implementing investment decisions can generally be divided into two broad categories: First, there are explicit costs, such as commissions, fees, and taxes. Second, there are implicit costs, such as market impact, timing costs, and opportunity costs [1]. Especially for large trades, implicit transaction costs are mostly much larger than explicit transaction costs. Liquidity constitutes the main determinant of implicit transaction costs: if the number of shares that other market participants are willing to trade at a given limit is reduced, then the market impact of an order is increased [9]. Thus, liquidity and implicit transaction costs represent two sides of the same coin [41]: The higher the liquidity is, the lower the implicit transaction costs, and vice versa. Thus, “asset managers and ordinary investors care about liquidity insofar as it affects the return on their investments, simply because illiquid securities cost more to buy, and sell for less” [12]. Therefore, to derive an optimal execution strategy and to minimise the associated transaction costs, the ability to forecast future liquidity levels is very important.

Bikker et al. [1], however, conclude that “forecasting market impact costs appears notoriously dif<sup>fi</sup>cult and traditional methods fail”. Moreover, Domowitz and Yegerman [10] <sup>fi</sup>nd that the execution quality of automated traders is inferior to the executions that are handled by brokers. One possible reason for this observation might be the fact that the currently employed models are solely based on purely quantitative data input. Existing (academic) models and strategies largely neglect one of the most important sources of information, which is unstructured qualitative data (i.e., news) [6]. If, for example, a listed company issues an unanticipated regulatory ad hoc disclosure, then automated traders cannot react suf<sup>fi</sup>ciently fast simply because they cannot analyse the content. Because unanticipated news, by de<sup>fi</sup>nition, is very unlikely to be re<sup>fl</sup>ected in quantitative time series data prior to its publication date, automated traders can respond only to other (human) market participants' reactions.

Against this background, our research goal is to investigate whether and how unstructured qualitative data can be used as input for automated trading engines. We are especially interested in whether useful information can be extracted automatically from qualitative data to predict future levels of liquidity after the publication of corporate disclosures. For extracting such information, text mining techniques are utilised. Given that decision support in the <sup>fi</sup>nancial domain is very challenging [8], we especially call the reader's attention to those domain-speci<sup>fi</sup>c issues that require an adjustment of standard knowledge discovery approaches, to investigate and emphasise the economic relevance of the proposed system. We particularise the knowledge discovery in databases (KDD) process proposed by Fayyad et al. [11] by domain-speci<sup>fi</sup>c customisations, such as the application of an event study for data understanding and a novel evaluation scenario in the form of a trading simulation. Moreover, we investigate the role of language within the proposed text mining framework. In other words, we enquire whether the proposed text mining system is sensitive to the language of the input text.

Thus, we contribute to the literature on <sup>fi</sup>nancial text mining by proposing an IT artefact to forecast the liquidity impact of corporate disclosures. In contrast to previous studies that mainly focus on forecasting the stock price impact of <sup>fi</sup>nancial news, we concentrate on the most important criterion of market quality, which in<sup>fl</sup>uences the highest cost component in trading, i.e., the implicit transaction costs [25]. Furthermore, we enhance previous research by focusing on the economic relevance of <sup>fi</sup>nancial text mining systems by extending the KDD process by Fayyad et al. [11] by means of an event study and a novel simulation. In this way, the simulation aims at evaluating the economic value of the proposed system and extends previous studies by accounting for the timing of the orders. Finally, we investigate whether the results differ for different language inputs.

The remainder of this paper is structured as follows: First, we present related <sup>fi</sup>nancial and information systems research. Second, we describe the study setup, which is based on the KDD process proposed by Fayyad et al. [11]. Third, the adjusted KDD process is applied to the above-described automated traders' use case. In this way, the dataset that is used in this study is described, and the liquidity impact of the publication of regulatory corporate disclosures is investigated, to enhance the data understanding. Fourth, building on these insights, we propose a text mining approach that predicts the liquidity impact of the ad hoc news. The classi<sup>fi</sup>cation quality is evaluated with respect to both the classic model evaluation metrics and domain-speci<sup>fi</sup>c simulationbased model evaluation. Finally, we present our conclusions.

## 2. Related work

## 2.1. Financial text mining

There are several studies that apply text mining techniques in <sup>fi</sup>nancial markets to <sup>fi</sup>nd patterns in text that can serve for predictions. In this context, Mittermayer and Knolmayer [35] provide a good survey on existing text mining systems: Since the time that Wuthrich et al. [46] proposed one of the <sup>fi</sup>rst <sup>fi</sup>nancial text mining applications, systems have been re<sup>fi</sup>ned by focusing on aspects such as intraday data, (new) data mining techniques, other forecasting objects (stock prices, exchange rates, volatility), news types (ad hoc news), and novel evaluation methods [17]. The prediction of company-speci<sup>fi</sup>c liquidity levels in general and the prediction of the liquidity impact of regulatory corporate disclosures in particular have – to our knowledge – not yet been addressed by utilising text mining techniques. Additionally, the language of input texts has been addressed in the literature [3] but not with regard to the <sup>fi</sup>nancial industry. Loughran and McDonald [31], however, have highlighted that <sup>fi</sup>nancial texts require domain-speci<sup>fi</sup>c knowledge and interpretation.

As a consequence, our approach builds upon and extends this literature by using intraday high-frequency data on the new forecasting object liquidity. We additionally concentrate on a certain news type and develop a novel domain-speci<sup>fi</sup>c evaluation metric.

## 2.2. Liquidity impact of corporate disclosures

Liquidity refers to the possibility of buying or selling an asset immediately without adversely affecting the price, and it is seen to be the most important aspect of market quality [14]. Liquidity is composed of two key dimensions that are relevant in our context: A market has breadth when the best buy and sell orders exist in substantial volume (see Fig. 1). Additionally, a market has depth when there are orders in substantial volume in the closest neighbourhood to the best bid and best ask limits [41]. To evaluate breadth and depth, an open limit order book that displays the cumulated buy and sell orders can be used. Two exemplary open limit order books are shown in Fig. 1. On the left of each order book, the buy orders (bid) are displayed, whereas on the right, the sell orders (ask) are indicated; both have order limits and available quantity at their respective limits.

In general, a lower level of market breadth or market depth (and, consequently, a lower level of liquidity) is disadvantageous for market participants because these levels would implicate higher implicit transaction costs. Referring to the order book examples that are displayed above, an investor who is willing to buy a quantity of 145 stocks would have to pay 53.00 for each stock in order book situation 1. However, if there were only 100 shares available at the best ask of 53.00, the investor would have to buy additional 45 shares for 54.00 to obtain the desired quantity (order book situation 2). The resulting average price of 53.31 per share would be worse than it has been in the more liquid market. As a result, in order book situation 2, market participants would have to bear an increased amount of implicit transaction costs.

To summarise, liquidity refers to the bids and offers that are provided in the market and are listed in the order book, i.e., it is shown ex-ante which trading opportunities are available for traders. In contrast, prices and trading volume result from the liquidity demand, i.e., they re<sup>fl</sup>ect past trades, and because they are ex-post, they are not relevant for decisions that are related to the timing of orders. Therefore, in contrast to existing research, we focus on the relevant pre-trade decision criterion (i.e., the liquidity) instead of focusing on the impact of corporate disclosures on prices ex-post.

In previous studies, the effect of information arrival on companyspeci<sup>fi</sup>c liquidity levels has already been analysed (e.g., [28]). Most of the contributions, however, merely concentrate on one event type, such as earnings announcements [26] or dividend announcements [15]. Moreover, authors use liquidity measures that do not allow a complete analysis of transaction costs because they account only for the market breadth [39]. Finally, other studies are based on very few events and/or short time periods [4,14]. We address all of the above shortcomings in this paper to extend the previous literature: We analyse a comparatively large dataset that is composed of several regulatory news types. Being provided with high-frequency order book data, we apply a liquidity measure that is especially suitable for the estimation of liquidity (i.e., the implicit transaction costs). Finally, we focus on short-term intraday liquidity effects.

![](/api/attachments/ZQWBWHMC/fulltext/images/5c263fb5bc8085eae110b62384c96069b23908b44883749e792f2e2c65f887da.jpg)  
Fig. 1. Two exemplary open limit order books.

## 3. Research approach

Generally, data mining aims at discovering useful patterns in data that can serve for predictions [11]. However, for a successful application of machine learning techniques, additional steps such as domain and data understanding as well as data reduction and pre-processing are crucial, too [18]. To account for these steps properly, our study is grounded on the KDD process model that is proposed by Fayyad et al. [11]. In comparison to other process models, it is considered to be the most suitable for data mining projects that require substantial data pre-processing activities [27]. Additionally, it has gained a large amount of attention within the literature on related data mining studies [27].

Fig. 2 shows our research approach based on the KDD process model by Fayyad et al. [11]. In our study, the phases understanding the application domain and creating a target dataset are conducted in parallel: On the one hand, we acquire a dataset that is composed of ad hoc disclosures, stock prices and order book data; on the other hand, the literature review presented in Section 2 and the event study presented in Section 5 help us to understand the liquidity impact of ad hoc disclosures. Thereafter, the phases of data cleaning & pre-processing as well as data reduction are performed. Consequently, a data mining method and an appropriate data mining algorithm are selected to conduct data mining. Within our study, we choose Support Vector Machine (SVM) as an appropriate data mining algorithm for classi<sup>fi</sup>cation. Finally, it is essential that the results of the data mining phase are analysed [2]. Therefore, the results are interpreted by means of classic model evaluation, and the discovered knowledge is applied within a simulation-based evaluation.

## 4. Creating a target dataset

The news dataset at hand is composed of ad hoc disclosures that are published by Deutsche Gesellschaft für Ad-hoc-Publizität (DGAP) on behalf of the companies admitted to trading on an organised market in Germany. To ful<sup>fi</sup>l the legal requirements, these companies must publish immediately any insider information or other information that is highly relevant to investors. We concentrate on this news type because the disclosures are expected to primarily contain new information and event studies have shown that these are often followed by abnormal stock returns [37].

We include in our dataset only those corporate disclosures that were published during exchange trading hours because we focus on intraday liquidity effects. Our event study analysis requires market data 15 min after/prior to an ad hoc publication as input; the earliest time for inclusion into the dataset is 9:15 a.m., and the latest time is 5:15 p.m. Moreover, we concentrate on companies that were members of one of the following German stock indices at the disclosure publication date: DAX (large-capitalisation stocks), MDAX (medium-capitalisation stocks), and SDAX (small-capitalisation stocks). A total of 71 disclosures were excluded from the dataset because of time window con<sup>fl</sup>icts; disclosures were not included in the dataset if there was another disclosure from the same company during the N = 30 days prior to publication. This setup ensures that potential liquidity effects can be analysed in isolation. Consequently, the <sup>fi</sup>nal dataset comprises 415 ad hoc disclosures that were published between 2006-01-31 and 2009-07-22. Furthermore, the observed liquidity effects remain robust if a time period of 15 days is used to exclude the confounding events.

![](/api/attachments/ZQWBWHMC/fulltext/images/50864afe460d5f76d37fe55e1238d5920d7256f8034e7baee81d829106725244.jpg)  
Fig. 2. Research approach based on the KDD process by Fayyad et al. [11].

Table 1 Median $A C R T ( \nu ) _ { [ t 1 , t 2 ] }$ sorted by volumes v.

<table><tr><td rowspan="2">Metric</td><td colspan="6">Time period</td></tr><tr><td>[-30, -15]</td><td>[-15, 0]</td><td>[0, 15]</td><td>[15, 30]</td><td>[30, 45]</td><td>[45, 60]</td></tr><tr><td> $ACRT(v = median)_{[t1,t2]}$ </td><td>-0.045</td><td>-0.018</td><td>0.307***</td><td>0.140***</td><td>0.102***</td><td>0.048***</td></tr><tr><td> $ACRT(v = 4*median)_{[t1,t2]}$ </td><td>-0.030</td><td>-0.023</td><td>0.273***</td><td>0.115***</td><td>0.066***</td><td>0.037***</td></tr><tr><td> $ACRT(v = 25 k)_{[t1,t2]}$ </td><td>-0.021</td><td>-0.021</td><td>0.280***</td><td>0.116***</td><td>0.060***</td><td>0.024***</td></tr></table>

$\hbar ^ { * * * } / { } ^ { p * * } / { } ^ { p * }$ indicate signi<sup>fi</sup>cance at the 1%/5%/10%-level

Each regulatory corporate disclosure is published in both German and English. The additional publication of corporate disclosures in English enables international investors to react suf<sup>fi</sup>ciently fast to new information. Given the regulatory background, the content of both the German and English disclosures should be identical. The corporate disclosures' associated companies are, at least, traded on the fully electronic trading system Xetra. For each security, an (open) limit order book is provided on Xetra (similar to the exemplary order book shown in Fig. 1). Investors post orders into the limit order book and thereby indicate their willingness to trade. The dataset at hand contains this highfrequency (level-2) order book data, i.e., it allows insights into the order book breadth and depth, including the best ten bid and offer limits and the respective order quantities at those limits. The order book data were extracted from Thomson Reuters Tick History. Respective order book data were extracted for event dates, i.e., the publication dates of the ad hoc disclosures, and from the previous ten working days. The respective trading volumes and trading phases (e.g., continuous trading, auction) were also extracted from the Thomson Reuters access.

## 5. Data understanding

Before the dataset at hand can be used to forecast the liquidity changes that are caused by ad hoc disclosures, we investigate whether these news have an impact on the level of liquidity at all. Therefore, an event study is conducted that measures the liquidity impact of the event “publication of an ad hoc disclosure”. This arrangement also represents an important part of the data understanding phase in the KDD process.

## 5.1. Methodology

The liquidity measure used in this study is similar to the Cost of Round Trip (CRT) proposed by Irvine et al. [23]. CRT builds upon the information that is contained in the open limit order book (see Fig. 1); $\mathrm { i . e . , }$ it measures the ex-ante committed liquidity that is available in the market for immediate execution. We compute CRT(v) as follows: Given a certain order book situation (and the limits/quantities, respectively) at time t, the (hypothetical) cost of simultaneously buying and selling volume v is calculated. It should be noted that the more liquid the market is, the lower the cost. The cost <sup>fi</sup>gure is divided by the executed € volume, i.e., v, to receive the per € cost of a (hypothetical) roundtrip trade.

High values of $C R T ( v ) _ { t }$ indicate that the market is illiquid and that implicit transaction costs are expected to be high. Any order book activity, such as the submission, cancellation, adjustment or execution of (limit) orders, obviously changes the $C R T ( v ) _ { t }$ . Because we operate with time periods rather than with single points in time, we must calculate an average $\Im T ( \nu ) _ { T , [ t 1 , t 2 ] }$ for a speci<sup>fi</sup>c time interval [t1, t2] on day T. Thereby, the CRT(v) values at <sup>fi</sup>xed points in time, i.e., every ten seconds, serve as input.

To investigate the potential impact from the publication of corporate disclosures on <sup>fi</sup>rm liquidity levels, we make use of event study methodology. An approach that is similar to the constant-mean-return model is applied [5]. With this approach, we adjust an observed effect by a mean that has been calculated using historical data prior to the event date (see Formula 1). Calculating the abnormal liquidity measure $A C R T ( \nu ) _ { [ t 1 , t 2 ] } ,$ we adjust the average $\mathit { T R T } ( \nu ) _ { T 0 , [ t 1 , t 2 ] }$ at event day T0 by the previous N days $( N = 1 0 ) ^ { 2 }$ averageCRT(v) for the same time period [t1, t2]. The adjustment is undertaken for the same (intraday) time period [t1, t2] because the literature suggests that the liquidity levels systematically change during the course of the day [33]. In general, when $A C R T ( \nu ) _ { [ t 1 , t 2 ] }$ is positive (N0), the liquidity at event day T0 is worse compared to historical levels. In contrast, $A C R T ( \nu ) _ { [ t 1 , t 2 ] }$ being negative (b0) indicates a higher level of liquidity at T0 compared to the past.

$$
A C R T (v) _ {[ t 1, t 2 ]} = \frac {\text { averageCRT } (v) _ {T 0 , [ t 1 , t 2 ]} - \frac {1}{N} \sum_ {j = 1} ^ {N} \text { averageCRT } (v) _ {T 0 - j , [ t 1 , t 2 ]}}{\frac {1}{N} \sum_ {j = 1} ^ {N} \text { averageCRT } (v) _ {T 0 - j , [ t 1 , t 2 ]}}\tag{1}
$$

Because abnormal liquidity levels are intended to be comparable among companies, these are calculated as relative values. Additionally, to ensure that the volumes v (and consequently the ACRT values) are comparable among companies, these were derived from historical trade data. For each event, different trade volume metrics (e.g., median trade size, mean trade size) were calculated for the respective onemonth period prior to the event date. It follows that the relative sizes of liquidity shocks should be comparable among companies and attributable to corporate disclosure content (only).

## 5.2. Event study results

$A C R T ( \nu ) _ { [ t 1 , t 2 ] }$ is calculated for different volumes v and different time periods [t1, t2]. If the median o $\mathsf { f } A C R T ( \nu ) _ { [ t 1 , t 2 ] }$ turns out to be signi<sup>fi</sup>cantly different from zero (Wilcoxon signed rank test), then the chosen event type regulatory-driven corporate disclosures constitutes a critical market event for which signi<sup>fi</sup>cantly higher/lower liquidity levels (and consequently lower/higher transaction costs) can be expected.

Table 1 depicts median $A C R T ( \nu ) _ { [ t 1 , t 2 ] }$ values for different 15-minute time intervals (whereas 0 is the time of publication) and varying volumes v. The <sup>fi</sup>rst two inputs median and 4\*median depend on each security's previous one-month trade statistics.<sup>3</sup> The last input 25 k, however, is <sup>fi</sup>xed/equivalent for each security, i.e., volume $\nu = \in 2 5 , 0 0 0$ . The results in Table 1 provide the following insights:

First, it can be observed that there are no signi<sup>fi</sup>cant abnormal liquidity levels prior to the publication of corporate disclosures, e.g., [−15, 0]. This <sup>fi</sup>nding provides evidence that the chosen event type actually contains new and previously unknown information that has not been widely anticipated by market participants. It is therefore expected that forecasting of such liquidity shocks is especially challenging for models that are based solely on historical quantitative data.

Table 2  
Median $A C R T ( \nu ) _ { [ t 1 , t 2 ] }$ sorted by indices.

<table><tr><td rowspan="2">Index</td><td rowspan="2">n</td><td colspan="6"> $ACRT(v = 4^{*}median)_{[t1,t2]}$ </td></tr><tr><td> $[-30, -15]$ </td><td> $[-15, 0]$ </td><td> $[0, 15]$ </td><td> $[15, 30]$ </td><td> $[30, 45]$ </td><td> $[45, 60]$ </td></tr><tr><td>DAX</td><td>122</td><td>-0.019</td><td>-0.015</td><td>0.312***</td><td>0.108***</td><td>0.064***</td><td>0.037***</td></tr><tr><td>MDAX</td><td>136</td><td>-0.023</td><td>-0.034</td><td>0.341***</td><td>0.133***</td><td>0.077***</td><td>0.037*</td></tr><tr><td>SDAX</td><td>157</td><td>-0.065</td><td>-0.023</td><td>0.183***</td><td>0.086***</td><td>0.058**</td><td>0.037**</td></tr></table>

\*\*\*/\*\*/\* indicate signi<sup>fi</sup>cance at the 1%/5%/10%-level.

Second, we <sup>fi</sup>nd strong empirical evidence that transaction costs increase subsequent to the publication of corporate disclosures, e.g., [0, 15]. This <sup>fi</sup>nding is most likely due to the fact that the disclosures' contents persuade traders to adjust their valuations of the respective company and adjust their existing limit orders in the order book accordingly. During the adjustment process, fewer limit orders (or limit orders with a lower volume) remain in the market, and therefore, the cost of execution increases (i.e., the liquidity decreases).

Third, the results appear to be robust to different volume v inputs. Both the sizes and signs of the results (the median values) are – as expected – comparable among inputs, i.e., median, 4\*median, and 25 k. Therefore, the results of the analyses below will be shown only for the input 4\*median.

It can also be observed that there are no systematic differences in the median $A C R T ( \nu = 4 ^ { * } m e d i a n ) _ { [ t 1 , t 2 ] }$ values, if they are calculated for the index subgroups (Table 2). The only small difference can be found with the fact that the levels of signi<sup>fi</sup>cance decrease in case of the medium (MDAX, period [45, 60]) and small capitalization indices (SDAX, periods [30, 45] and [45, 60]).

In line with Graham et al. [15], we suppose that the reaction of the liquidity levels to new information depends on the news types. We therefore construct news/corporate disclosure sub-samples according to the categories proposed by Leis and Nowak [29]. The sub-sample analysis provides the following insights (Table 3):

First, for those categories that have a suf<sup>fi</sup>cient number of corporate disclosures (i.e., at least 10 disclosures), we can observe highly signi<sup>fi</sup>cant abnormal liquidity levels subsequent to the publication of the corporate disclosures, e.g., for [0, 15]. Nonetheless, both the size and length of the liquidity impacts appear to vary among news categories. While the liquidity levels revert to normal levels, already 15 min after publication of corporate action disclosures, the liquidity impact of financial statement disclosures and miscellaneous disclosures appears to be more persistent. We can therefore conclude that the durability of liquidity impacts depends on the type of news. The observed differences in durability might be the result of continuously varying opinions of market participants. In other words, the content of those corporate disclosures is not unambiguous.

Second, we can observe signi<sup>fi</sup>cant market reactions prior to the publication of corporate action disclosures. Negative $A C R T ( \nu ) _ { [ t 1 , t 2 ] }$ values, however, denote abnormally high liquidity levels $( \mathrm { i . e . }$ ., low implicit transaction costs). Market participants appear to be able to anticipate corporate action disclosures. Whether this information is based on insider information or publicly available information and rumours is, however, not observable within our setting.

Given the above results, one might typically assume lower liquidity levels (i.e., higher implicit transaction costs) subsequent to the publication of corporate disclosures. Therefore, the simplest strategy to avoid high implicit transaction costs would be to either execute orders immediately at t (naive strategy) or wait for execution until the liquidity reverts to normal levels. The latter case would, however, incur waiting/opportunity costs. Moreover, as shown above, the length of time after which the liquidity levels revert to normal levels varies among news types.

With respect to the data understanding phase of our research approach, we conclude that the corporate disclosures at hand do have an impact on the corresponding liquidity levels. As a result, forecasting this liquidity impact appears to be promising because investors as well as automated trading engines must adjust their strategies according to the expected liquidity impact to reduce the implicit transaction costs.

## 5.3. Document labelling according to the liquidity impact

Supervised learning requires us to label the documents in the document collection according to pre-de<sup>fi</sup>ned objectives. Our objective is to forecast news-related liquidity impacts. As shown in the course of the event study, we can (on average) observe positive $A C R T ( \nu ) _ { [ t 1 , t 2 ] }$ values, i.e., higher transaction costs, which occur subsequent to the publication of corporate disclosures. Therefore, our naive response would be to expect lower liquidity levels (i.e., higher implicit transaction costs). If we, however, take a closer look at the distribution of the $A C R T ( \nu ) _ { [ t 1 , t 2 ] }$ values (Fig. 3), we note that certain corporate disclosures are associated with negative $A C R T ( \nu ) _ { [ t 1 , t 2 ] }$ values (class negative). Given our otherwise naive response, we are especially interested in identifying those corporate disclosures that are associated with negative $A C R T ( \nu ) _ { [ t 1 , t 2 ] }$ values, i.e., those cases that have implicit transaction costs that are below historical levels and consequently liquidity levels that are above historical levels.

The empirical distribution of the $A C R T ( \nu ) _ { [ t 1 , t 2 ] }$ values in Fig. 3 shows that the 25%-quartile by coincidence separates those cases quite well from the overall distribution that are of most interest to us, i.e., those with a negative $A C R T ( \nu ) _ { [ t 1 , t 2 ] }$ value. In other words, we use the 25%- quartile for labelling purposes. Consequently, each corporate disclosure is assigned to the classes positive or negative, depending on whether their $A C R T ( \nu ) _ { [ t 1 , t 2 ] }$ is above or below the 25%-quartile of all of the documents' $A C R T ( \nu ) _ { [ t 1 , t 2 ] } ,$ . The above event study provides evidence that the strongest reaction to the publication of corporate disclosures can be observed during the <sup>fi</sup>rst 15 min. Consequently, this interval is of most interest to investors, and as a result, the time period [0, 15] is used for labelling.

Median ACRT(v) sorted by news categories.

<table><tr><td rowspan="2">News category</td><td rowspan="2">n</td><td colspan="6"> $ACRT(v=4^{*}median)_{[t1,t2]}$ </td></tr><tr><td>[-30,-15]</td><td>[-15,0]</td><td>[0,15]</td><td>[15,30]</td><td>[30,45]</td><td>[45,60]</td></tr><tr><td>(1) Financial statement</td><td>122</td><td>-0.109</td><td>-0.031</td><td>0.340***</td><td>0.119***</td><td>0.101***</td><td>0.093***</td></tr><tr><td>(2) Dividend announcement</td><td>39</td><td>-0.022</td><td>-0.058</td><td>0.203***</td><td>0.038</td><td>-0.013</td><td>0.043</td></tr><tr><td>(3) Corporate action</td><td>37</td><td>-0.117**</td><td>-0.160 ***</td><td>0.210***</td><td>0.082</td><td>0.019</td><td>0.017</td></tr><tr><td>(4) M&amp;A transaction/reorganization</td><td>80</td><td>0.021</td><td>0.069</td><td>0.291***</td><td>0.163***</td><td>0.070**</td><td>-0.025</td></tr><tr><td>(5) Personnel</td><td>61</td><td>-0.030</td><td>-0.016</td><td>0.076**</td><td>0.031</td><td>0.034</td><td>0.027*</td></tr><tr><td>(6) Litigationa</td><td>5</td><td>-0.234</td><td>0.137</td><td>0.011</td><td>0.144</td><td>0.407</td><td>0.158</td></tr><tr><td>(7) Order situationa</td><td>4</td><td>-0.058</td><td>-0.083</td><td>0.791</td><td>0.716</td><td>0.244</td><td>0.188</td></tr><tr><td>(8) Investmentsa</td><td>8</td><td>0.081</td><td>0.023</td><td>0.015</td><td>0.134</td><td>-0.026</td><td>-0.127</td></tr><tr><td>(9) Miscellaneous</td><td>59</td><td>0.024</td><td>0.029</td><td>0.339***</td><td>0.093***</td><td>0.035**</td><td>0.054**</td></tr></table>

\*\*\*/\*\*/\* indicate signi<sup>fi</sup>cance at the 1%/5%/10%-level.  
<sup>a</sup> Please note that the number of observations, i.e. n, is too small to achieve reliable statistically grounded insights for this news category.

![](/api/attachments/ZQWBWHMC/fulltext/images/7b51772536082780f8451bd0dd7edded52d09c10cddc1d6df934468c0b09d147.jpg)  
Fig. 3. ACRT(v = 4\*median)<sub>[0,15]</sub> distribution

## 6. Data cleaning & pre-processing followed by data reduction

At the beginning of the data cleaning & pre-processing phase, a dictionary of words and phrases that adequately describes the document collection is generated. In this way, a simple StringTokenizer [45] splits up the whole text into individual units in lower case (i.e., by also applying a Lower\_Case\_Converter). Although we basically follow a bag-ofwords approach, in which grammar or word order is not accounted for, we additionally create term n-grams (n = 2) to grasp the most important word combinations. This approach allows us to better interpret word combinations, such as not\_good and not\_bad, which would otherwise have been assessed in isolation.

In addition to StringTokenizer units, we also create character n-grams of length n of each token in a document. In line with Braschler and Ripplinger [3], we make use of 6-grams. Note that both the character n-grams and StringTokenizer units are part of the <sup>fi</sup>nal feature set. We also create character n-grams because the German language is especially coined by a rich set of possible in<sup>fl</sup>ections and word concatenations that might not be properly accounted for by stemmers [3]. Nonetheless, we also map different grammatical forms of a word to a common stem by applying either the Porter Stemmer [38] or the Lovins Stemmer [32]. The stemmer procedure is applied to the StringTokenizer units only.

Exemplary pre-processing setup that illustrates the feature number reduction.

<table><tr><td rowspan="3" colspan="2">Pre-processing steps</td><td colspan="4">No. of features</td></tr><tr><td colspan="2">Language: German</td><td colspan="2">Language: English</td></tr><tr><td>Complete ad-hoc news</td><td>Headline only</td><td>Complete ad-hoc news</td><td>Headline only</td></tr><tr><td></td><td>Tokenizer</td><td>13,038</td><td>1,306</td><td>8,626</td><td>1,383</td></tr><tr><td></td><td>Lower_Case_Converter</td><td>12,114</td><td>1,253</td><td>7,216</td><td>1,216</td></tr><tr><td></td><td>Token_Length_Filter (min. 4)</td><td>11,546</td><td>1,120</td><td>6,682</td><td>1,074</td></tr><tr><td></td><td>Stemmer (Porter)</td><td>10,370</td><td>1,075</td><td>4,628</td><td>904</td></tr><tr><td></td><td>Pruning (below 3; above 25)</td><td>3,118</td><td>233</td><td>1,732</td><td>277</td></tr></table>

To eliminate noise, e.g., words that have little meaning but frequent appearance, we apply a threshold on the number of documents that each token occurs in. Pre-tests revealed that useful thresholds for the dataset at hand are 3 for too infrequent words and 25 for too frequent words. Words that are above and below those thresholds are not included in the feature set. In addition, tokens that do not ful<sup>fi</sup>l the minimum length requirement of 4 were removed from the feature set (Token\_Length\_Filter). An additional stop word list is not made use of, to ensure comparability for the language comparison, i.e., German/ English.

Moreover, the Chi-Squared metric serves as an additional method for data reduction. Thereby, the feature set is further reduced by scoring (<sup>fi</sup>ltering) the features according to their Chi-Squared weightings. Our pre-tests revealed that <sup>fi</sup>ltering features according to their Chi-Squared weightings provides better results than <sup>fi</sup>ltering by Information Gain. Those k features that have the highest weightings remain in the feature set.

Optimal values of k are derived within a simple grid-search loop iteration. In this way, optimal parameter values are obtained by varying combinations of assigned parameter values (i.e., between $k = 5 0$ and k = the total number of tokens). Whenever optimal parameter values were derived by a grid-search, it is marked as such in the results section.

At the end of the process, each document is represented by the previously extracted and selected number of features. The respective feature weightings in the document-feature matrix W is given by tf.idf [30].

Table 4 exemplarily depicts how different pre-processing steps reduce the feature set. The insights from this illustration are as follows:

First, the feature set that results from the complete corporate disclosures (news) is, of course, larger than the feature set that results from the headlines only (headline). As already suggested above, the English feature set is much smaller than the German feature set [3]. After having applied different pre-processing steps, however, the headline feature sets are similar in size.

Second, already the conversion of all of the tokens (words) to lower cases has an effect on the size of the feature sets. The largest reduction of features is, however, achieved by pruning.

## 7. Selection of data mining method and data mining algorithm

## 7.1. Classification technique

Because the aim of our study is to investigate whether unstructured data can be used for liquidity forecasts after the publication of ad hoc disclosures, we concentrate on the application of a single machine learning technique instead of comparing different techniques, as is proposed by the KDD process of Fayyad et al. [11]. For selecting an appropriate machine learning technique, we consider comparative empirical studies. These studies provide evidence that the classi<sup>fi</sup>cation performance of SVM is superior to other data mining techniques (e.g., [24]). In addition, SVM “is usually less vulnerable to the over-<sup>fi</sup>tting problem” and “the solution of SVM is always unique and globally optimal” [21]. As a result, we make use of SVM within our text mining approach.

SVM was <sup>fi</sup>rst introduced by Vapnik [43] for solving two-class recognition problems. The basic idea is to <sup>fi</sup>nd a decision surface that maximises the margin between the data points, i.e., the classes, by means of structural risk minimisation. In a case in which there are originally non-separable data points, the original data vectors can be mapped to a higher dimensional space to achieve linear separability. To reduce the complexity, kernels, i.e., functions in lower dimensional space that exhibit similar behaviour as the original functions in higher dimensional space, are applied. We make use of a linear kernel similar to Hsu et al. [20], who provide evidence that a linear kernel appears to be suf<sup>fi</sup>cient whenever the number of features is exceptionally large.

![](/api/attachments/ZQWBWHMC/fulltext/images/7bb3e4387e3e0c3ba01c3881a80bfde43d6bb06da54b6e41046a2d1fd7f56533.jpg)  
Fig. 4. Intraday text mining approach setup.

When applying SVM with a linear kernel, primarily the cost parameter C must be optimised. Thus, we also apply the above-mentioned grid-search loop optimisation approach. In line with Hsu et al. [20], we use exponentially growing sequences of parameter C as input into grid-search optimisation, i.e., ${ \mathsf C } \doteq 2 ^ { - 5 } , 2 ^ { - 3 } , . . . , 2 ^ { 1 5 }$

## 7.2. Post-processing

SVM delivers con<sup>fi</sup>dence values for each class, to assure that the prediction is actually true positive [34]. Corporate disclosures are assigned to the classes positive or negative, depending on whether the con<sup>fi</sup>dence value is above or below a certain (learned) threshold. The variation in the thresholds can be applied as a post-processing step to account for imbalanced datasets or unequal classi<sup>fi</sup>cation costs [47]. We are confronted with both: First, the class negative, which is of most interest to us, contains only 25% of all corporate disclosures. Second, the cost for falsely classifying negative documents as positive is higher than falsely classifying positive documents as negative. This relationship occurs because our objective is to precisely identify those corporate disclosures that are associated with abnormally low transaction costs after publication, i.e., class negative. To overcome these problems, we conduct cost-sensitive learning implemented as a post-processing step [22]. Thereby, a ThresholdFinder [34] uses the con<sup>fi</sup>dence values to turn the SVM into a cost-sensitive learner.

## 8. Interpretation of results: <sup>Classic</sup> model evaluation

To be able to properly interpret the performance of the proposed text mining setup, this section presents a classic evaluation by means of common machine learning performance metrics.

## 8.1. Classic model evaluation setup

As shown in Fig. 4, the whole dataset is split up into a learning dataset and a test dataset to ensure that model evaluation is independent from model building. Because the dataset is comparatively small, we do not conduct a one-time split; instead, we follow an m-fold (m = 10) cross-validation approach [44].

Each test sub-sample contingency table is aggregated to create a global contingency table (micro averaging) (Table 5). The global contingency table is used to calculate the classic performance measures of accuracy $[ ( \mathsf { a } + \mathsf { d } ) / \mathsf { n } ; \mathsf { n } = \mathsf { a } + \mathsf { b } + \mathsf { c } + \mathsf { d } ]$ , recall [class positive: $\textsf { a } / \left( \mathsf { a } + \mathsf { c } \right) ]$ , and precision [class positive: $\textbf { a } / \left( \mathsf { a } + \mathsf { b } \right) ]$ [19]. In this way, accuracy denotes the percentage of examples that are classi<sup>fi</sup>ed correctly, recall represents the percentage of positive examples that are classi<sup>fi</sup>ed as positive, and precision indicates the percentage of examples that are correctly predicted as positive.

Accounting for the inherent trade-off between precision and recall, we additionally calculate the F1 measure by van Rijsbergen [42], where recall and precision are given equal weight (Eq. (2)).

$$
F _ {1} = (2 \cdot r e c a l l \cdot p r e c i s i o n) / (r e c a l l + p r e c i s i o n)\tag{2}
$$

## 8.2. Classic model evaluation results

Classi<sup>fi</sup>cation results for complete corporate disclosures (news) and headlines only (headline) in both German and English provide the following general insights (see Table 6): High (misclassi<sup>fi</sup>cation) costs of the class negative, e.g., 0.9, result in a high precision <sup>fi</sup>gure and a low recall <sup>fi</sup>gure. In other words, there are only very few corporate disclosures that are assigned to the class negative, but those that are assigned truly belong to this class. This <sup>fi</sup>nding is due to the fact that corporate disclosures are assigned to the class negative only if the respective SVM con<sup>fi</sup>dence value is quite high, i.e., the classi<sup>fi</sup>er is certain that the disclosure actually belongs to the respective class.

The precision <sup>fi</sup>gure of 100% (\~90%) for $S V M _ { ( 0 . 1 ; 0 . 9 ) }$ provides strong evidence that the proposed text mining approach can precisely identify some of those corporate disclosures whose associated securities' liquidity levels are not negatively affected by the disclosure contents. The high precision <sup>fi</sup>gure comes at the cost of low recall: We merely capture a small number of relevant class negative corporate disclosures. Therefore, one might be willing to accept a certain number of false positives to increase the number of caught class negative corporate disclosures, e.g., SVM . In the end, it is up to the developers of automated trading engines to decide on the classi<sup>fi</sup>ed documents' con<sup>fi</sup>dence values. For example, a safe recommendation in the form of a trading signal would be provided at a precision of 100% with $S V M _ { ( 0 . 1 ; 0 . 9 ) } .$

Accuracy <sup>fi</sup>gures are slightly larger than the 75% all-positive benchmark would suggest. However, because we are primarily interested in precisely identifying class negative corporate disclosures, the benchmark is of little use. We merely show accuracy <sup>fi</sup>gures for reasons of completeness.

In terms of distinctions between languages (German vs. English) or completeness of texts (complete news vs. headlines only), we cannot <sup>fi</sup>nd consistent systematic differences. However, utilising complete German texts instead of complete English texts leads to slightly better results.

## Table 5

Exemplary illustration of the (global) contingency table.

<table><tr><td></td><td>True positive</td><td>True negative</td></tr><tr><td>Predicted positive</td><td>a</td><td>b</td></tr><tr><td>Predicted negative</td><td>c</td><td>d</td></tr></table>

In terms of the (pre-processing) con<sup>fi</sup>guration, it can be observed that many optimal “complete news” result set combinations contain term n-gram tokens, whereas many “headline only” result set combinations contain character n-gram tokens. Therefore, for both German and English texts, n-grams should ideally be part of the generated feature sets. Moreover, pruning (thresholds) on the number of documents that each token occurs in rarely leads to superior results.

To summarise, the proposed system can produce a trading signal that indicates whether the underlying regulatory corporate disclosures will (most likely) cause abnormally high or low transaction cost levels during the 15 min subsequent to their publication. Thereby, the developer of an automated trading engine must decide whether high precision (which results in low recall) or high recall (which results in low precision) is the primary goal. Furthermore, this proposed trading signal can serve as an additional input to existing trading models that are purely based on quantitative data.

## 9. Acting on the discovered knowledge: <sup>Simulation-based</sup> model evaluation

In addition to the above classic model evaluation, we introduce a novel domain-speci<sup>fi</sup>c simulation-based evaluation approach that aims at acting on the discovered knowledge. In general, a simulation-based model evaluation allows for additional statistical analysis and provides insights into the results' robustness.

Previous applications of text mining techniques in the <sup>fi</sup>nancial industry have highlighted the need for domain-speci<sup>fi</sup>c evaluation metrics [16]. Related research has focused on forecasting stock prices or stock price volatilities, whereas these studies evaluate the proposed approaches by performing investment simulations, i.e., a stock is assumed to be bought (sold) when the price is predicted to rise (fall), and the returns achieved with these strategies are used to evaluate the performance [36,40]. However, such a simulation approach is not appropriate for evaluating the implicit transaction costs because it ignores the timing of the orders. Thus, a new simulation setup must be developed. The proposed simulation setup constitutes an automated trading engine use case.

Moreover, this simulation allows us to quantify the economic value of the text mining system. Classic model evaluation results provide insights merely into whether certain events have been classi<sup>fi</sup>ed correctly. However, classic model evaluation does not allow drawing conclusions about the economic value, i.e., whether the “right” classi<sup>fi</sup>cation is actually of any use.

## 9.1. Simulation-based model evaluation setup

Within the simulation, an automated trader receives the order to execute volume V during the time interval M [m1, m2]. The goal is to minimise the implicit transaction costs. To achieve this goal, an optimal execution strategy must be determined. Within this context, we account for the results of our m-fold cross validation setup (see Fig. 5). Each corporate disclosure in the m test datasets is classi<sup>fi</sup>ed by the above proposed text mining approach.

If the corporate disclosure is classi<sup>fi</sup>ed as belonging to the class positive, then we expect the liquidity of the underlying security to decrease during the time interval [0, 15]. Consequently, the automated trader should prefer to execute at the very beginning of the interval, $\mathrm { i . e . }$ , immediately after the release of the news but prior to the liquidity impact or at the end of the interval. Because the above event study analysis has provided evidence that the length of time after which the liquidity levels revert to normal levels varies, we decided in favour of the <sup>fi</sup>rst approach, i.e., execution at the very beginning (naive strategy). Thus, the automated trader performs analysis on the incoming disclosure immediately, i.e., within milliseconds and, therefore, very close to t + 0, places an appropriate order. In this way, the automated trader can make use of the available (high) level of liquidity before other traders (human traders) change their bids and offers in response to the news disclosure.

![](/api/attachments/ZQWBWHMC/fulltext/images/df5666148b2cddbbc33251377fc2c8956d14d9fa55e0d0bc7b6fc2fce40f5e98.jpg)  
Fig. 6. Illustration of the applied trading strategies naive and liquid.

In contrast, if the corporate disclosure is classi<sup>fi</sup>ed as belonging to the class negative, then we expect the liquidity of the underlying security to increase – or at least not to decrease – during the time interval. To take advantage of the liquidity increase, we introduce a liquid strategy. Therefore, the volume V is split into different orders that are executed step-by-step.

The execution strategies explained above are also illustrated in Fig. 6. Please note that the automated trader should follow a strategy that simultaneously pro<sup>fi</sup>ts from advantageous liquidity levels and also accounts for the market impact costs from large trades. For example, we expect the volume of the <sup>fi</sup>rst naive strategy to be executed at still normal liquidity levels (t ). Nonetheless, we also expect a large market impact that is associated with the executed volume.

In terms of modelling, the market impact is assumed to be merely temporary, i.e., it does not last until the next execution time t .

Furthermore, we specify the following model assumptions: The choice among alternative trading strategies is static in our simulation model, i.e., the trading strategy chosen at m1 cannot dynamically be altered during M. Moreover, we do not explicitly model buy or sell orders. Instead, each time that the automated trader triggers an execution of size $\nu _ { i } ,$ a cost measure similar to the above-de<sup>fi</sup>ned $C R T ( v _ { i } ) _ { t i }$ is used as a proxy for the incurred transaction costs. Please note that the cost measure used here is not an abnormal measure, i.e. not ACRT. The transaction costs for each strategy and event j are calculated according to Formula 3:

![](/api/attachments/ZQWBWHMC/fulltext/images/2ef2da67f5c27af0dc11714977ffd593f0174e955aecf1a922dd46a97f16b94e.jpg)  
Fig. 5. Setup of simulation-based model evaluation.

Classic model evaluation results.

<table><tr><td rowspan="3">Misclassification cost for class (pos./neg.)</td><td colspan="8">Complete ad-hoc news</td></tr><tr><td colspan="4">Language: German</td><td colspan="4">Language: English</td></tr><tr><td>Accuracy</td><td>Precision</td><td>Recall</td><td>F1</td><td>Accuracy</td><td>Precision</td><td>Recall</td><td>F1</td></tr><tr><td>(0.1/0.9)</td><td>80.48</td><td>100.00</td><td>22.12</td><td>36.23</td><td>80.00</td><td>92.00</td><td>22.12</td><td>35.66</td></tr><tr><td>(0.3/0.9)</td><td>81.69</td><td>72.58</td><td>43.27</td><td>54.22</td><td>80.72</td><td>72.22</td><td>37.50</td><td>49.37</td></tr><tr><td>(0.5/0.9)</td><td>81.69</td><td>70.00</td><td>47.12</td><td>56.33</td><td>80.24</td><td>65.71</td><td>44.23</td><td>52.87</td></tr><tr><td>(0.9/0.9)</td><td>79.04</td><td>57.80</td><td>60.58</td><td>59.16</td><td>75.66</td><td>51.33</td><td>55.77</td><td>53.46</td></tr><tr><td></td><td colspan="8">Headline only</td></tr><tr><td>(0.1/0.9)</td><td>78.07</td><td>93.33</td><td>13.46</td><td>23.53</td><td>79.76</td><td>91.67</td><td>21.15</td><td>34.37</td></tr><tr><td>(0.3/0.9)</td><td>79.26</td><td>72.50</td><td>27.88</td><td>40.27</td><td>80.24</td><td>80.56</td><td>27.88</td><td>41.42</td></tr><tr><td>(0.5/0.9)</td><td>79.04</td><td>68.89</td><td>29.81</td><td>41.61</td><td>80.00</td><td>78.38</td><td>27.88</td><td>41.13</td></tr><tr><td>(0.9/0.9)</td><td>77.83</td><td>58.82</td><td>38.46</td><td>46.51</td><td>77.11</td><td>55.70</td><td>42.31</td><td>48.09</td></tr></table>

Complete news/German: $\left( 0 . 1 / 0 . 9 \right) \mathrm { { C } = 2 , k = 5 0 0 , }$ , Porter stemmer, term n-gram, pruning $= \mathrm { y e s } / / ( 0 . 3 / 0 . 9 ) \mathrm { C } = 2 0 4 8 , \mathrm { k } = 5 0 0 ,$ , Lovins stemmer, term n-gram, pruning = no//(0.5/0.9) $C = 3 2 , \mathrm { k } = 2 0 0$ , Lovins stemmer, term n-gram, pruning = yes//(0.9/0.9) C = 32768, k = 50, Porter stemmer, character n-gram, pruning = no. Complete news/English: (0.1/0.9) $C = 3 2 , \mathrm { k } = 2 0 0 ,$ , Porter stemmer, no n-gram, pruning $= { \mathrm { n } } 0 / / ( 0 . 3 / 0 . 9 ) \mathrm { C } = 0 . 0 3 1 2 5 , \mathrm { k } = 2 0 0 ,$ , Lovins stemmer, term n-gram, pruning = no//(0.5/0.9) C = 0.5, k = 500, Lovins stemmer, term n-gram, pruning $= \mathrm { n o } / / ( 0 . 9 / 0 . 9 ) \mathrm { C } = 2 0 4 8 , \mathrm { k } = 2 0 0$ , Porter stemmer, term n-gram, pruning = no. Headline only/German: $\left( 0 . 1 / 0 . 9 \right) \mathsf { C } = 2 0 4 8 , \mathsf { k } = 5 0 ,$ Porter stemmer, char acter n-gram, pruning = yes//(0.3/0.9) C = 0.5, k = 50, Porter stemmer, character n-gram, pruning = no//(0.5/0.9) C = 0.5, k = 50, Porter stemmer, character n-gram, $\mathrm { p r u n i n g } = \mathrm { n o } / / ( 0 . 9 / 0 . 9 ) \mathrm { C } = 3 2 , \mathrm { k } = 5 0$ , Porter stemmer, character n-gram, pruning = no. Headline only/English: $( 0 . 1 / 0 . 9 ) \mathrm { { C } = 2 0 4 8 , \mathrm { { k } = 2 0 0 , } }$ , Lovins stemmer, character n-gram, pruning = no//(0.3/0.9) $\mathsf { C } = 1 2 8 , \mathsf { k } = 5 0 ,$ Lovins stemmer, character n-gram, pruning = no//(0.5/0.9) C = 2048, k = 50, Lovins stemmer, character n-gram, pruning = no//(0.9/ 0.9) ${ \sf C } = 8 , { \sf k } = 2 0 0 ,$ Lovins stemmer, term n-gram, pruning = no.

$$
\operatorname{Cost} _ {\text { Strategy }, j} = \sum_ {i = 0} ^ {1 5} C R T (v _ {i}) _ {t _ {i}}.\tag{3}
$$

The simulation time interval M is equivalent to the period that is used for labelling, i.e. [0, 15]. Equivalent to the above approach, the volume v is derived from the trade statistics, i.e., it is 4\*median in this case, and it must be executed during this time interval for each security that is subject to a corporate disclosure. Executions of size v are made at <sup>fi</sup>xed one-minute intervals $( \mathrm { t _ { 0 } , t _ { 1 } , t _ { 2 } , . . . , t _ { 1 5 } } )$ . In this way, t constitutes the corporate disclosure publication time at the publication day. It is assumed that automated traders – even with a simple trading signal as news or no news – can react to the publication of corporate disclosures within milliseconds, i.e., while the liquidity is still at normal levels (at t ). To further rule out distortions because of systematic differences between securities, we calculate a cost ratio (Formula 4). The cost ratio directly compares the costs that are associated with each strategy for each event.

$$
R _ {C o s t} = \frac {\text { Cost } _ {\text { naive } , j}}{\text { Cost } _ {\text { liquid } , j}}\tag{4}
$$

Having already provided evidence that the liquidity levels are expected to decrease for the majority of events (see Fig. 3) and that this effect is larger in size than the market impact effect of large trades, the costs that are associated with the naive strategy $( C o s t _ { n a i v e , j } )$ should be lower than the costs that are associated with the liquid strategy $( C o s t _ { l i q u i d , j } )$ . Consequently, we expect the cost ratio $R _ { C o s t }$ to be lower than one for all (and positive) events. If our text mining approach can precisely identify negatively labelled events, then the cost ratio should be larger than one for the (negative) events.

Descriptive and test results for $R _ { C o s t }$ (naive/liquid).

<table><tr><td rowspan="3">Misclassification cost for class (pos./neg.)</td><td rowspan="3">Result subset actually classified as</td><td colspan="4">Median  $R_{Cost}$ </td></tr><tr><td colspan="2">Language: German</td><td colspan="2">Language: English</td></tr><tr><td>Complete ad-hoc news</td><td>Headline only</td><td>Complete ad-hoc news</td><td>Headline only</td></tr><tr><td></td><td>All news</td><td></td><td>0.95</td><td></td><td></td></tr><tr><td rowspan="2">(0.1/0.9)</td><td>Positive</td><td>0.94</td><td>0.94</td><td>0.94</td><td>0.93*</td></tr><tr><td>Negative</td><td>1.14*</td><td>1.32*</td><td>1.01</td><td>1.20***</td></tr><tr><td rowspan="2">(0.3/0.9)</td><td>Positive</td><td>0.92**</td><td>0.93</td><td>0.93*</td><td>0.94*</td></tr><tr><td>Negative</td><td>1.12***</td><td>1.01</td><td>1.12</td><td>1.16*</td></tr><tr><td rowspan="2">(0.5/0.9)</td><td>Positive</td><td>0.90**</td><td>0.93</td><td>0.91**</td><td>0.94</td></tr><tr><td>Negative</td><td>1.17***</td><td>1.01</td><td>1.11**</td><td>1.14*</td></tr><tr><td rowspan="2">(0.9/0.9)</td><td>Positive</td><td>0.88***</td><td>0.94</td><td>0.88**</td><td>0.91*</td></tr><tr><td>Negative</td><td>1.09**</td><td>0.99</td><td>1.09**</td><td>1.05*</td></tr></table>

\*\*\*/\*\*/\* indicate signi<sup>fi</sup>cance at the 1%/5%/10%-level.

News assigned to class positive : $\begin{array} { r } { C o s t _ { n a i \nu e } { < } C o s t _ { l i q u i d } ; R _ { C o s t } { < } 1 } \\ { C o s t _ { n a i \nu e } { > } C o s t _ { l i q u i d } ; R _ { C o s t } { > } 1 } \end{array}$ News assigned to class negative :

To further statistically explore this assumption, the corresponding null and alternative hypotheses are formulated and tested:

$$
H _ {0}: \mu (R _ {C o s t}) = 1 \quad \text { vs. } \quad H _ {A}: \mu (R _ {C o s t}) \neq 1.
$$

Hereby, μ constitutes the median, and the hypotheses are tested by means of a Wilcoxon signed rank test.

## 9.2. Simulation-based model evaluation results

Descriptive and test results for the simulation-based model evaluation and varying SVM misclassi<sup>fi</sup>cation cost inputs provide the following insights (see Table 7).

First, the median cost ratio for all of the events (n = 415) is below 1. In other words, for all of the events, the naive strategy is associated with lower costs than the liquid strategy. Nonetheless, it shall be noted that the null hypothesis is not rejected. Therefore, the <sup>fi</sup>gure should serve to obtain <sup>fi</sup>rst insights that concern the relationship between the two strategies.

Second, the negative subclass is often associated with statistically signi<sup>fi</sup>cant median $R _ { C o s t }$ values that are above 1. At the same time, the respective positive subclass median $R _ { C o s t }$ values are below 1.

Third, complete input texts in German appear to provide slightly better results than complete input texts in English. The results differ when only headlines are taken into account: subclass negative $R _ { C o s t }$ values are signi<sup>fi</sup>cant and above 1 for “English headlines only”, whereas these are statistically signi<sup>fi</sup>cant and above 1 just in one con<sup>fi</sup>guration for “German headlines only”. However, the con<sup>fi</sup>guration $_ { ( 0 . 1 / 0 . 9 ) }$ still leads to a higher median cost ratio and thus better execution performance compared to the English language.

To summarise, if the trading signal that is produced by the proposed text mining approach is followed, then the liquidity levels can be forecasted correctly in order to decrease the implicit transaction costs. As Table 7 shows, for negatively classi<sup>fi</sup>ed complete German corporate disclosures, $\mathrm { R _ { C o s t } }$ is signi<sup>fi</sup>cantly above one. In the case of complete German ad hoc disclosures, a trader who follows the naive approach and executes the whole volume at $\mathrm { t } _ { 0 }$ (instead of following the proposed liquid strategy) would have to bear implicit transaction costs that are 9%–17% higher compared to the recommendation of our proposed text mining system. Similar results are also found for English corporate disclosures. These <sup>fi</sup>ndings provide evidence that our proposed text mining system works well and that the proposed approach can be seen as economically relevant.

## 10. Conclusion

Text mining techniques are already applied in various research projects and practical applications to electronically classify <sup>fi</sup>nancial news and/or to forecast price changes in securities markets. However, most research is focused on the prediction of future price changes of a security. Given that liquidity constitutes one of the most important determinants of (implicit) transaction costs, we aimed to investigate whether text mining allows us to predict future levels of liquidity.

We follow the KDD process proposed by Fayyad et al. [11]. However, given the speci<sup>fi</sup>c environment of the <sup>fi</sup>nancial domain, it is necessary to adjust and “shape” the KDD process to <sup>fi</sup>t domain-speci<sup>fi</sup>c requirements. Based on an in-depth understanding of the respective industry, we propose such an adapted KDD process.

First, we conduct an event study, which is a common approach in the <sup>fi</sup>nancial domain, to understand the data. The event study provides empirical evidence that the publication of regulatory corporate disclosures is followed by abnormal liquidity levels. This <sup>fi</sup>nding is consistent with existing beliefs about how limit order traders update their orders upon the arrival of new information. We, however, do not <sup>fi</sup>nd consistent evidence of abnormal liquidity levels prior to the publication of corporate disclosures. It follows that automated traders should ideally include information on the publication of corporate disclosures into their models.

Second, we develop a domain-speci<sup>fi</sup>c simulation-based evaluation approach to assess the economic value that is added by the proposed text mining system. Both classic and simulation-based model evaluation results provide evidence that the trading signal indicates some of those corporate disclosures, entailing the lowest expected future transaction costs. Consequently, we have shown that it is of economic value to adhere to the proposed text mining approach, i.e., to include information on the publication of corporate disclosures into automated traders' models. Moreover, having implemented and tested an IT artefact, we have also shown how such a text mining approach might look.

To summarise, following a structured domain-speci<sup>fi</sup>c KDD process, it is possible to extract useful information from unstructured qualitative data to predict future levels of liquidity. In terms of a text mining setup, we found weak evidence that the German language is more suitable than the English language in case of complete disclosures taken into account. One possible explanation might be the fact that (German) concatenations are useful within a bag of words approach. As a practical implication, international investors may bene<sup>fi</sup>t from localising their text mining systems, at least within German-speaking countries.

Given the above results, this paper contributes in terms of both methodology (e.g., the adapted KDD process, event study, simulation setup) and practical relevance (e.g., a detailed description of the IT artefact). Being a highly relevant group of traders and despite their technical capabilities, automated traders require an appropriate decision support system as well. In this research project, we proposed and successfully tested different ways of enhancing automated trading engines to address news-related liquidity shocks in a timely manner. Future work will concentrate mainly on solving the current limitations of this research, i.e., the proposed forecasting approach shall be compared to existing quantitative forecasting approaches. Because this paper's proposed IT artefact is not intended to replace existing systems (and is instead intended to complement them), future work will therefore concentrate on the integration of our trading signal into existing execution models.

## References

[1] J. Bikker, L. Spierdijk, R. Hoevenaars, P.J. van der Sluis, Forecasting market impact costs and identifying expensive trades, Journal of Forecasting 27 (1) (2006) 21–39.

[2] N. Bissantz, J. Hagedorn, Data mining, business & information systems engineering 1 (1) (2009) 118–122.

[3] M. Braschler, B. Ripplinger, How effective is stemming and decompounding for German text retrieval, Information Retrieval 7 (3) (2004) 291–316.

[4] R. Brooks, A. Patel, T. Su, How the equity market responds to unanticipated events, Journal of Business 76 (1) (2003) 109–133.

[5] J.Y. Campbell, A.W. Lo, A.C. MacKinlay, The Econometrics of Financial Markets, Princeton University Press, Princeton, N.J., 1997

[6] R. Coggins, M. Lim, K. Lo, Algorithmic trade execution and market impact, IWIF Working Paper, University of Sydney, 2006.

[7] Deutsche Börse AG, Integrity for <sup>fi</sup>nancial markets, Annual Report 2008, 2008. (http://deutsche-boerse.com/dbag/dispatch/en/binary/gdb\_content\_pool/ imported\_<sup>fi</sup>les/public\_<sup>fi</sup>les/10\_downloads/12\_db\_annual\_reports/2008/GB\_ komplett\_2008.pdf (2012-03-06)).

[8] V. Dhar, R. Stein, Intelligent decision support methods, The Science of Knowledge Work, Prentice Hall, Upper Saddle River, NJ, 1997.

[9] I. Domowitz, J. Glen, A. Madhavan, Liquidity, volatility and equity trading costs across countries and over time, International Finance 4 (2) (2001) 221–255.

[10] I. Domowitz, H. Yegerman, The cost of algorithmic trading — a <sup>fi</sup>rst look at comparative performance, in: B. Bruce (Ed.), Algorithmic Trading: Precision, Control, Execu tion, Institutional Investor Inc., New York, USA, 2005, pp. 30–40.

[11] U. Fayyad, G. Piatetsky-Shapiro, P. Smyth, From data mining to knowledge discovery in databases, AI Magazine 17 (3) (1996) 37–54.

[12] T. Foucault, M. Pagano, A. Röell, Market liquidity, Theory, Evidence, and Policy, Oxford University Press, Oxford, UK, 2013.

[13] P. Gomber, M. Gsell, Catching up with technology — the impact of regulatory changes on ECNs/MTFs, Competition and Regulation in Network Industries 1 (4) (2006) 535–557.

[14] P. Gomber, U. Schweickert, E. Theissen, Zooming in on liquidity, 31st Annual Meeting of the European Finance Association, Maastricht, Netherlands, 2004, pp. 1–34.

[15] J. Graham, J. Koski, U. Loewenstein, Information <sup>fl</sup>ow and liquidity around anticipated and unanticipated dividend announcements, Journal of Business 79 (5) (2006) 2301–2336.

[16] S.S. Groth, J. Muntermann, Supporting investment management processes with machine learning techniques, Proceedings of the 9th Internationale Tagung Wirtschaftsinformatik, vol. 2, Österreichische Computer Gesellschaft, Vienna, Austria, 2009, pp. 275–284.

[17]. S.S. Groth I. Muntermann An intraday market risk management approach based on textual analysis, Decision Support Systems 50 (4) (2011) 680–691.

[18] J. Han, M. Kamber, Data mining, Concepts and Techniques, 2nd ed., Elsevier; Morgan Kaufmann San Francisco 2006

[19] A. Hotho, A. Nürnberger, G. Paaß, A brief survey of text mining, GLDV Journal for Computational Linguistics 20 (1) (2005) 19–62.

[20] C.W. Hsu, C.C. Chang, C.J. Lin, A Practical Guide to Support Vector Classi<sup>fi</sup>cation, National Taiwan University, 2003. (http://www.csie.ntu.edu.tw/\~cjlin/papers/ guide/guide.pdf (2011-10-16)).

[21] W. Huang, Y. Nakamori, S. Wang, Forecasting stock market movement direction with support vector machine, Computers and Operations Research 32 (2005) 2513–2522.

[22] M. Ikonomakis, S. Kotsiantis, V. Tampakas, Text classi<sup>fi</sup>cation using machine learning techniques, WSEAS Transactions on Computers 4 (8) (2005) 966–974

[23] P. Irvine, G. Benston, E. Kandel, Liquidity beyond the inside spread: measuring and using information in the limit order book, Working Paper, Emory & Hebrew University, 2000.

[24] T. Joachims, Text categorization with support vector machines: learning with many relevant features, Proceedings of the 10th European Conference on Machine Learning, Chemnitz, Germany, 1998, pp. 137–142.

[25] D.B. Keim, A. Madhavan, The cost of institutional equity trades, Financial Analysts Journal 54 (4) (1998) 50–69.

[26] I. Krinsky, J. Lee, Earnings announcements and the components of the bid-ask spread, Journal of Finance 51 (4) (1996) 1523–1535.

[27] L.A. Kurgan, P. Musilek, A survey of knowledge discovery and data mining process models, The Knowledge Engineering Review 21 (1) (2006) 1–24.

[28] C.M.C. Lee, B. Mucklow, M. Ready, Spreads, depths, and the impact of earnings information, Review of Financial Studies 6 (2) (1993) 345–374

[29] J. Leis, E. Nowak, Ad-hoc-Publizität nach § 15 WpHG, Schäffer-Poeschel, Stuttgart, 2001.

[30] D. Lewis, Representation and Learning in Information Retrieval, Dissertation University of Massachusetts. 1992

[31] T. Loughran, B. McDonald, When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks, The Journal of Finance 66 (1) (2011) 35–65

[32] J. Lovins, Development of a stemming algorithm, Mechanical Translation and Computational Linguistics 11 (1–2) (1968) 22–31.

[33] T. McInish, R. Wood, An analysis of intraday patterns in bid/ask spreads for NYSE stocks, Journal of Finance 47 (2) (1992) 753–764

[34] L Mierswa M. Wurst R. Klinkenberg M. Scholz T. Euler YALE: rapid prototyping for complex data mining tasks Proceedings of the ACM SIGKDD

International Conference on Knowledge Discovery and Data Mining, Philadel phia, USA, 2006, pp. 935–940.

[35] M.-A. Mittermayer, G. Knolmayer, Text mining systems for market response to news: a survey, Institute of Information Systems, Working Paper No. 184, University of Bern, 2006.

[36] M.-A. Mittermayer, Forecasting intraday stock price trends with text mining techniques, Proceedings of the 37th Hawaii International Conference on System Sciences, Big Island, Hawaii, USA, 2004.

[37] J. Muntermann, A. Guettler, Intraday stock price effects of ad hoc disclosures: the German case, Journal of International Financial Markets Institutions and Money 17 (1) (2007) 1–24.

[38] M. Porter, An algorithm for suf<sup>fi</sup>x stripping, Program 14 (3) (1980) 211–218.

[39] A. Ranaldo, Intraday market dynamics around public information arrivals, in: F. Lhabitant, G. Gregoriou (Eds.) Stock Market Liquidity: Implications for Market Microstructure and Asset Pricing, John Wiley & Sons, Hoboken, N.J., USA, 2008, pp. 199–226.

[40] R.P. Schumaker, H. Chen, Textual analysis of stock market prediction using breaking <sup>fi</sup>nancial news: the AZFin text system, ACM Transactions on Information Systems 27 (2) (2009) 1–19.

[41] R. Schwartz, R. Francioni, Equity Markets in Action: The Fundamentals of Liquidity, Market Structure & Trading, John Wiley & Sons, Hoboken, N.J., USA, 2004.

[42] C.J. van Rijsbergen, Information Retrieval, 2nd ed. Butterworths, London, 1979.

[44] I.H. Witten, E. Frank, M.A. Hall, Data mining, Practical Machine Learning Tools and Techniques, 3rd ed., Morgan Kaufmann Publishers, Burlington, Mass, 2011..

[43] V. Vapnik, The Nature of Statistical Learning T heory, Springer, New York, USA, 1995. [43] V. Vapnik, The Nature of Statistical Learning Theory, Springer, New York, USA, 1995.

[45] M. Wurst, I. Mierswa, The Word Vector Tool: User Guide, Operator Reference, Developer Tutorial, 2009. (http://heanet.dl.sourceforge.net/project/rapidminer/2.% 20Text%20Plugin/4.4/rapidminer-text-4.4-tutorial.pdf (2012-03-06)).

[46] B. Wuthrich, V. Cho, S. Leung, D. Permunetilleke, K. Sankaran, J. Zhang, W. Lam, Daily stock market forecast from textual web data, Proceedings of the IEEE International Conference on Systems, Man, and Cybernetics, San Diego, CA, USA, 1998.

[47] Y. Yang, A study of thresholding strategies for text categorization, Proceedings of the 24th ACM Int. Conference on Research & Development in Information Retrieval, 2001, pp. 137–145.

Sven S. Groth is currently working as a personal advisor to the chief executive of<sup>fi</sup>cer of an asset management company. Prior to that he worked as a graduate researcher at the E-Finance Lab, an industry-academic partnership between Goethe University Frankfurt am Main, Germany and several (<sup>fi</sup>nancial) industry partners. During this time he also wrote his PhD thesis titled “automation in securities trading: text mining and algorithmic trading”. Sven studied business administration at the European Business School (ebs), Germany and real estate investment at the University of Reading Business School, UK. His research interests include decision support systems and algorithmic trading.

Michael Siering is a graduate researcher at the E-Finance Lab, Frankfurt, Germany. He received his M.Sc. degree in Management from University of Frankfurt and is currentl writing his PhD thesis at the Chair of e-Finance. His research interests include <sup>fi</sup>nancial decision support, <sup>fi</sup>nancial market surveillance and sentiment analysis.

Peter Gomber holds the Chair of e-Finance at the Faculty of Economics and Business Administration, University of Frankfurt. He is Co-Chair and Member of the Board of the E-Finance Lab. His academic work focuses on market microstructure and auction theory, institutional trading, innovative concepts/technologies for electronic trading and post trading systems and information systems in Finance. Peter Gomber graduated in business administration at the University of Gießen and acquired his PhD at the Institute of Information Systems. He published several articles on the above mentioned topics in international journals and was awarded with the Reuters Innovation Award 2000, the University Award of DAI (Deutsches Aktieninstitut) 1999, the IBM SUR Grant 2007 and several Best Paper Awards at international research conferences.

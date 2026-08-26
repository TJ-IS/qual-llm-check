---
otero_id: 15572
otero_key: "D33Q464T"
title: "An intraday market risk management approach based on textual analysis"
authors: "Sven S. Groth; Jan Muntermann"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.08.019"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An intraday market risk management approach based on textual analysis

Sven S. Groth <sup>a</sup>, Jan Munterman n <sup>b,</sup>⁎

<sup>a</sup> E-Finance Lab, House of Finance, Grüneburgplatz 1, 60323 Frankfurt, Germany

<sup>b</sup> Goethe-University Frankfurt, House of Finance, Grüneburgplatz 1, 60323 Frankfurt, Germany

a r t i c l e i n f o

Available online 19 August 2010

Keywords: Market risk management Text mining Corporate disclosures

## a b s t r a c t

The management of <sup>fi</sup>nancial risk is one of the most challenging tasks of <sup>fi</sup>nancial institutions. In the last two decades, diverse quantitative models and approaches have been developed and re<sup>fi</sup>ned to address the impact of volatile markets on business. Whereas existing approaches have intensively utilized structured data such as historical price series, little attention has been paid to unstructured (textual) data, which could be a large source of information in this context. Previous empirical research has shown that certain news stories, such as corporate disclosures, can cause abnormal price behavior subsequent to their publication. On the basis of a data set comprising such news stories as well as intraday stock prices, this paper explores the risk implications of information being newly available to market participants. After showing that such events can signi<sup>fi</sup>cantly drive stock price volatilities, this research aims at identifying among the textual data provided those disclosures that have resulted in most supranormal risk exposures. To this end, four different learners — Naïve Bayes, k-Nearest Neighbour, Neural Network, and Support Vector Machine — have been applied in order to detect patterns in the textual data that could explain increased risk exposure. Two evaluations are presented in order to assess the learning capabilities of the approach in the context of risk management. First, “classic” data mining evaluation metrics are applied and, second, a newly developed simulation-based evaluation method is presented. Evaluation results provide strong evidence that unstructured (textual) data represents a valuable source of information also for <sup>fi</sup>nancial risk management — a domain in which, in the past, little attention has been paid to unstructured data. With regard to classi<sup>fi</sup>cation performance, it is also shown that there exist signi<sup>fi</sup>cant differences between the applied learning techniques.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

Financial modeling of market risks, i.e. the management of losses due to movements in <sup>fi</sup>nancial market prices, has been a subject of research for the last few decades. Today, traditional <sup>fi</sup>nancial risk management tools, such as Value-at-Risk and Stress Testing, make use of quantitative data stored in structured databases [37]. While the approaches to analyze such structured data, e.g. historical price series, have been continuously improved (for an example of intraday effects see [25]) , little attention has been paid in this context to the analysis of unstructured qualitative data.

Especially when assessing intraday market risk exposures resulting from market events, such as critical corporate disclosures that were not anticipated by market participants, there exists limited quantitative data (at event time) that could be analyzed in such situations.

However, the disclosures contain qualitative data representing a potential source of information that is not taken into consideration by traditional risk management tools. Nonetheless, the management of intraday market risk is a challenge for different market participants engaged in frequent trading, such as high frequency traders, <sup>fl</sup>oor traders, and market makers [25]. Also, using quantitative intraday data to forecast intraday volatilities is still at its infancy and quite unsuitable to address event risks as described before [39]. Event risk plays an important role, especially in the case of small time horizons when relevant information about a company is newly available to the market. In this context, Campbell et al. [10] have observed that <sup>fi</sup>rmlevel variance has more than doubled in the last three decades while market and industry variances have remained stable over that period.

Therefore, the goal of this paper is to explore how existing risk management approaches can be supported by utilizing unstructured textual data. In contrast to the wide range of publications that focus on quantitative risk management approaches, we will focus on the potentials of qualitative data and the corresponding data analysis methodologies.

The remainder of our paper is structured as follows: In Section 2, we provide a literature review on related work in the <sup>fi</sup>elds of <sup>fi</sup>nancial risk management and on text mining in the context of <sup>fi</sup>nancial forecasting. Furthermore, a theoretical foundation is provided. Then, Section 3 illustrates how and why we have selected our data set. In Section 4, we present a text mining approach to identify signi<sup>fi</sup>cant risk exposures that result from textual information newly available to market participants. In Sections 5 and 6 we provide evaluations of our approach. We present both a “classic” evaluation based on traditional evaluation metrics (Section 5) and a domain-speci<sup>fi</sup>c evaluation on the basis of a simulation (Section 6). In Section 7, we conclude with a summary and an outlook on further research.

## 2. Related work

## 2.1. Management of market risks

Today, <sup>fi</sup>nancial market risks are modeled with the help of modern information systems analyzing huge amounts of quantitative data. Investment companies, for example, run complex and time consuming simulations in order to assess current risk positions. Risk positions that are assessed on the basis of historical data (e.g. when conducting historical simulations) or repeated random sampling (e.g. Monte Carlo simulation) are usually measured by a Value-at-Risk measure that estimates the risk of loss on a given portfolio of <sup>fi</sup>nancial assets at a certain con<sup>fi</sup>dence interval [33]. Here, risk positions are assessed for longer holding periods such as 10 days. In order to address intraday market risks, recent research aims to extend traditional Value-at-Risk to cover shorter (intraday) horizons [19]. However, due to the used con<sup>fi</sup>dence interval, Value-at-Risk does not provide support for managing extraordinary losses, and since the underlying calculations are based on historical or arti<sup>fi</sup>cial data sets, intraday losses that could result from critical market events are not covered [2]. Another established risk management approach that has a focus on events that could result in extraordinary losses, is stress testing. Utilizing historical or arti<sup>fi</sup>cial quantitative data, stress testing aims at supporting managers to assess <sup>fi</sup>nancial consequences of critical market behavior, i.e. to conduct what-if-analyses for such scenarios [32]. Central objective of these approaches is to quantify hypothetical risk exposures for different scenarios, but not to discover actual intraday risk exposures that result from given but unforeseen critical events. Utilizing only quantitative data seems inappropriate when there is also unstructured data available, which is indeed more complex to process and to analyze but which, however, could contain valuable information.

## 2.2. “Financial” text mining

An appearance of price volatility undoubtedly constitutes a potential risk. The fact that there is already a multitude of research on how to measure volatility underpins this perception [44]. Nonetheless, there exists only little research, if any at all — depending on the de<sup>fi</sup>nition — that aims at utilizing unstructured data sources in the context of risk management by applying text mining techniques. However, volatility forecasting is highly relevant for <sup>fi</sup>nancial risk management, especially with a focus on short periods [15]. While there are quantitative approaches for intra-day volatility forecasts [19,39], there exists little research on utilizing unstructured data in this <sup>fi</sup>eld.

Even though the data/text mining approaches by [47,51] are classi<sup>fi</sup>ed as volatility forecasting systems by [42], we believe that this is the case only within strict limitations: [47] aim at forecasting abnormal stock returns, i.e. not volatility. The rule-based hand-crafted classi<sup>fi</sup>er by [51] does not re<sup>fl</sup>ect our understanding of text mining (see below, [28]).

Another line of thought that is similar to our proposed risk mitigation text mining approach can be found in the literature on forecasting stock price movements. Wuthrich et al. [57] present one of the <sup>fi</sup>rst applications of text mining techniques addressing <sup>fi</sup>nancial forecasting problems. Later work focuses on further aspects such as intraday events, applying new data mining techniques, varying the forecasting object, focusing on certain news types, or presenting novel evaluation methods [26,30,41,47,48]. Several IT artifacts that were developed in order to provide risk management functionalities [38] or to exploit text mining [23,24,41] in the domain of stock trading have been presented in the past.

On the basis of a multi-agent approach, Luo et al. [38] present an IT infrastructure that provides decision support for stock trading. The features of the risk management agent are mainly based on quantitative data (such as prices and trading volumes), an approach that has been the state-of-the-art in <sup>fi</sup>nancial research for several years [3,8]. With regard to unstructured data, “breaking news” related to given shares are monitored. While the presented infrastructure provides functionalities to monitor news releases and to map those to given securities, there are no functionalities that aim at assessing the corresponding risk exposures. In [23,24,41], system architectures are presented that aim at estimating stock price trends (positive, negative, or neutral) on the basis of textual data. Having a focus on implementing pro<sup>fi</sup>table trading strategies, no information on volatility increases is provided, which would be relevant to support risk management. Consequently, since they focus on trend forecasts and trading strategies, existing system concepts provide only little evidence that unstructured (textual) data can be utilized to support the management of market risks.

## 2.3. Theoretical background

At an ef<sup>fi</sup>cient capital market, prices will promptly adjust to information newly available to market participants. This wellestablished ef<sup>fi</sup>cient market hypothesis EMH (semi-strong-form) has been developed by Eugene Fama and goes back to the 1960s [21,22]. In <sup>fi</sup>nancial research, EMH provides the theoretical basis for various research approaches, among them event study analysis. Here, price adjustments to previously unknown events are statistically analyzed, such as the speed at which prices fully re<sup>fl</sup>ect new information available. Furthermore, the information content of different news types can be explored by statistically proving the existence of abnormal price behavior following a speci<sup>fi</sup>c event type. Signi<sup>fi</sup>cant information content has been proven to exist on the basis of abnormal stock returns for corporate disclosures such as announcements on E-Commerce initiatives and IT investments [18,50]. Abnormal market behavior has also been observed, from a more general perspective, for corporate disclosures that were published due to regulatory legislation [12,43]. Most event study analyses are based on abnormal returns, i.e. returns observed subsequent to an event and adjusted by a market trend that has, for example, been calculated with a market model [11].

In the context of market risk management, signi<sup>fi</sup>cant price volatility represents a relevant measure to focus on [25]. Several papers in <sup>fi</sup>nance literature have detected no or only a weak connection between the volatility of stock prices and news releases such as public disclosures of monetary policy decisions [5]. These results provide evidence that a focus on speci<sup>fi</sup>c news types is appropriate when aiming at analyzing news content carrying information that could result in signi<sup>fi</sup>cant risk exposure.

## 3. Data set and risk modeling

As a basis for our research, we use a data set that is composed of news and stock price data. The selected news data appears suitable in the context of market risk management, since we aim at <sup>fi</sup>nding such news stories that are associated with highest market risk. We assume that the type of news we have selected is appropriate for such an endeavor, which we will illustrate in the following. High-frequency intraday stock price data are associated with the news data to analyze potential relations.

## 3.1. Data set: corporate disclosures and stock prices

From a market risk management perspective, one should be interested in primary information sources, i.e. on sources of information that are expected to signi<sup>fi</sup>cantly drive market prices. We therefore focus on a speci<sup>fi</sup>c news type, namely regulatory-induced corporate disclosures, for which empirical event study analyses have detected abnormal price reactions (i.e. processed information) in the past. We expect such event types to be a potential source of risk worth further analyses. Since selections of speci<sup>fi</sup>c news feeds (e.g. that contain speci<sup>fi</sup>c corporate disclosures only), are supported by major content providers today, such an approach can easily be implemented in practice.

We therefore present and analyze in the following a news data set that is — compared to other research in the <sup>fi</sup>eld of <sup>fi</sup>nancial forecasting utilizing data mining techniques [48] — smaller in size, but which, however, should be more relevant from the perspective of risk management. If we had used such large data sets, we would have aimed at identifying news that will result in some (comparably minor) volatility increase from a collection of news, most of which would not entail any signi<sup>fi</sup>cant price reaction at all. Then, we would have identi<sup>fi</sup>ed, for example, merely all corporate disclosures within a much larger data set.

To further substantiate our data set selection approach, we describe and explore in more detail our data set of corporate disclosures and illustrate how this news type drives volatility, i.e. represents a source of market risk.

The news data are drawn from a collection of corporate disclosures that were published to ful<sup>fi</sup>ll regulatory legislation (article 15 of the German Securities Trading Act). The disclosures were published between 2003-08-01 and 2005-07-31 and since we focus on intraday market risks, we collected those 423 disclosures that were published during stock exchange trading hours.

For each disclosure, the content, the publication date (exact to the minute) and the International Securities Identi<sup>fi</sup>cation Number (ISIN) of the company that has initiated the publication has been collected. Using these stock identi<sup>fi</sup>ers, the corresponding intraday (highfrequency) stock price series were obtained from Thomson Reuters DataScope Tick History for the publication dates and a period of 1 year prior to these dates.

## 3.2. Intraday market risk model

As our objective is the identi<sup>fi</sup>cation of intraday market risk, we require valid predictions of future volatility. Moreover, those events that exhibit especially high volatility levels are more interesting to us than those events that exhibit rather low volatility levels. This is due to the fact that we aim at identifying situations that could create extraordinary risk exposure.

In order to model intraday market risk exposure associated with critical market events such as the publication of corporate disclosures, we apply a risk model from Ahn et al. [1] that is based on short-term price volatility being calculated using transaction returns, which is called realized volatility, or $\sigma _ { [ t 1 , t 2 ] } .$ . Here, $r _ { i , [ t 1 , t 2 ] }$ is de<sup>fi</sup>ned as the return of the ith transaction during time interval [t1, t2] (Eq. (1)). In <sup>fi</sup>nancial risk management research, the importance of realized volatility has been emphasized in a number of recent studies [3,8,15].

$$
\sigma_ {[ t 1, t 2 ]} = \sum_ {i = 1} ^ {N} r _ {i, [ t 1, t 2 ]} ^ {2}\tag{1}
$$

When working with high-frequency data, microstructure effects such as negative autocorrelation become relevant that can result from e.g. a bouncing effect within the bid-ask spread. To address this issue, a Bias factor according to [17] is used to adjust the $\sigma _ { [ t 1 , t 2 ] }$ measure.

$$
B i a s = \frac {\sqrt {q} \sigma_ {\Delta t}}{\sigma_ {\Delta t \mathrm{ref}}}\tag{2}
$$

with $\Delta t _ { \mathrm { r e f } } = \boldsymbol { q } \cdot \Delta t$

The bias factor is calculated by observing a bias-free reference case (with a large enough time interval $\Delta t _ { \mathrm { r e f } } )$ to judge the bias of smaller intervals Δt, which is 1 min in this case. As proposed in [17], one working day has been used as $\Delta t _ { r e f }$ and Bias has been calculated on the basis of a one year price history for each event, i.e. for the corresponding returns. On the basis of the calculated bias that is measured in terms of how much Bias deviates from 1, a corrected risk measure $R I S K _ { [ t 1 , t 2 ] }$ is calculated by:

$$
R I S K _ {[ t 1, t 2 ]} = \sigma_ {[ t 1, t 2 ]} / B i a s\tag{3}
$$

As illustrated in [16], such a bias-correction will signi<sup>fi</sup>cantly reduce the bias that results from market microstructure effects. On the basis of the risk measure RISK, we de<sup>fi</sup>ne an abnormal risk measure $A R I S K _ { [ t 1 , t 2 ] } \left( \mathbb { E } \mathbf { q } . \left( 4 \right) \right)$ that adjusts the risk exposure following the event day T0 by a risk exposure that has been observed before T0, i.e. when no critical market event has occurred. Basically, RISK is adjusted by the average RISK calculated for the previous N days (for that particular stock). As literature suggests that there is usually an intraday volatility U-shape [55], i.e. high volatility at the open and close of the trading day, previous N days’ RISK is calculated for the same time period [t1, t2] as event RISK.

$$
A R I S K _ {[ t 1, t 2 ]} = R I S K _ {[ t 1, t 2 ]} - \frac {1}{N} \sum_ {j = 1} ^ {N} R I S K _ {T 0 - j, [ t 1, t 2 ]}\tag{4}
$$

ARISK has been calculated for different periods $[ t 1 , t 2 ] = [ - 3 0 , - 1 5 ] ,$ $\left[ - 1 5 , 0 \right]$ prior to, and [0,15], [15,30], [30,45], and [45,60] subsequent to the event dates (Fig. 1).

## 3.3. Empirical data set selection

Previous <sup>fi</sup>ndings of intraday event studies provide evidence that most signi<sup>fi</sup>cant abnormal market movements can be observed for short periods subsequent to the publication of relevant information and that the effect magnitude decreases with the time elapsed [45,49].

The following <sup>fi</sup>gure provides evidence that this market behavior also holds for our risk measure.

Picking up the theoretical background presented before, the EMH states that stock prices will ef<sup>fi</sup>ciently adjust to previously unknown information. If corporate disclosures represent a substantial source of risk, we can expect signi<sup>fi</sup>cant risk exposure following their publication.

We consequently formulate the following null hypotheses on the basis of $A R I S K _ { [ t 1 , t 2 ] }$ measures for different periods [t1,t2]:

$$
H _ {0} = \mu \left(A R I S K _ {[ t 1, t 2 ]}\right) \leq 0 \text {   vs.   } H _ {\mathrm{A}} = \mu \left(A R I S K _ {[ t 1, t 2 ]}\right) > 0
$$

If we can reject the formulated null hypotheses for the periods subsequent to the publication dates, the chosen event type “regulatory-driven corporate disclosures” constitutes a news type for which signi<sup>fi</sup>cant intraday market risk exposure can be expected. Identifying “most risky” events from this data set should therefore provide signi<sup>fi</sup>cant bene<sup>fi</sup>ts from a risk management perspective. Descriptive statistics and empirical test results for the 423 corporate disclosures are provided in Table 1.

![](/api/attachments/D33Q464T/fulltext/images/273d506fbc3cf50d71d8b493d627c7f1be654776b6a9490fd2329bbbd1236f6b.jpg)  
Fig. 1. Mean ARISK for different periods.

The null hypotheses can be rejected at the 1%-level of signi<sup>fi</sup>cance for the periods following the event date. For these continuous periods, the mean of ARISK decreases with the time elapsed. For the period prior to the event date, we do not detect any signi<sup>fi</sup>cance, i.e. no evidence for information leakage or anticipation effects. We conclude that corporate disclosures constitute critical market events representing sources of substantial market risk. Managing these market risks, it is necessary to identify the most critical events based on the disclosures’ contents. Therefore we aim at tagging corporate disclosures according to whether or not these are associated with supranormal volatilities subsequent to their publication.

## 4. A text mining approach to mitigate intraday market risk

## 4.1. Text mining setup

In our literature review on existing event study research, we found that the publication of corporate disclosures is often followed by signi<sup>fi</sup>cant abnormal stock returns. These signi<sup>fi</sup>cant (unexpected) stock movements represent a potential source of market risk. Building upon this <sup>fi</sup>nding, the above data set grounding analysis (Section 3) con<sup>fi</sup>rms that corporate disclosures are often followed by signi<sup>fi</sup>cant abnormal volatility levels, too. As the abnormal volatility levels occur shortly after the publication of respective corporate disclosures, the inherent news — once known — need to be processed within a very short period of time.

Aiming at offering support to those who are either confronted with “information over<sup>fl</sup>ow” issues or who want to be able to respond faster, we propose a text mining approach that will make predictions of future volatility levels (Fig. 2). The predictions will be made for the time period directly following the publication of corporate disclosures. The approach is designed to identify those corporate disclosures that are associated with highest (abnormal) extraordinary market movements.

The introduced text mining approach is applied on the real-world data set by means of an empirical study. The evaluation of classi<sup>fi</sup>cation results is undertaken in two ways: First, we calculate “classic” data mining evaluation metrics such as accuracy, recall, or precision [28]. While these measures allow a comparison of different classi<sup>fi</sup>cation techniques, a comprehensive conclusion about the general suitability of the text mining approach cannot be drawn. Therefore, an additional domain-speci<sup>fi</sup>c simulation-based performance evaluation is conducted.

## 4.2. Labelling

Supervised learning, i.e. classi<sup>fi</sup>cation, requires the respective documents in the document collection to be labelled according to a pre-de<sup>fi</sup>ned objective. As the mitigation of intraday market risk exposures requires valid predictions of future market volatility, our

## Table 1

Descriptive statistics and test results for risk measures.

<table><tr><td rowspan="2">[t1,t2]</td><td colspan="6"> $ARISK_{[t1,t2]}$ </td></tr><tr><td>[-30,-15]</td><td>[-15,0]</td><td>[0,15]</td><td>[15,30]</td><td>[30,45]</td><td>[45,60]</td></tr><tr><td>N</td><td>415</td><td>422</td><td>423</td><td>423</td><td>417</td><td>414</td></tr><tr><td>Mean in %</td><td>0.001</td><td>0.011</td><td>0.215</td><td>0.101</td><td>0.088</td><td>0.063</td></tr><tr><td>t-value</td><td>0.08</td><td>1.54</td><td>9.22 ***</td><td>8.97 ***</td><td>4.50 ***</td><td>6.54 ***</td></tr></table>

\*\*\*indicates signi<sup>fi</sup>cance at the 1%-level.

![](/api/attachments/D33Q464T/fulltext/images/ef2a0f545bd833588bc321fb5fec94a779b3180710a107e1b9182de450514ea9.jpg)  
Fig. 2. Study setup.

objective can be found with (improved) forecasting of such market volatility. Due to the fact that the underlying data set contains corporate disclosures that are for the greatest part already associated with abnormal volatility levels (see above), the actual text mining task is to identify those disclosures that exhibit highest abnormal volatilities. These highest abnormal volatilities can be found with the “long tails” on the right side of the empirical ARISK distributions (Fig. 3). Whenever we refer to τ in the following, we refer to the time interval [0, τ], i.e. t1=0 and t2=0+τ.

The “long tails”, which constitute most volatility-enhancing corporate disclosures, are separated from the remaining empirical distribution quite well by the 75% quartiles.

Pursuing this approach, the classi<sup>fi</sup>cation task is de<sup>fi</sup>ned as follows: Documents (i.e. corporate disclosures) are assigned to the class “positive”, if the respective disclosures’ abnormal risk exposure ARISK is higher than (or equal to) QUARTILE(ARISK ). Accordingly, documents are labelled “negative”, if the respective disclosures’ abnormal risk exposure ARISK is lower than QUARTILE(ARISK ). Thereby, QUARTILE(ARISK ) is de<sup>fi</sup>ned as the 75% quartile of all documents’ abnormal volatility during the τ=15 and 30 min following the disclosure publication (Table 2).

It follows that the class “positive” contains the 25% most volatilityentailing news items. We decided to use τ=15 and 30 min for labelling for the following reasons: As it can be observed in both Table 1 and Fig. 1, the time period [0,15] is associated with the largest mean ARISK value. In order to provide evidence for the robustness of (relative) classi<sup>fi</sup>er performance, we also introduce an additional time period, i.e. [0,30]. We decided in favour of τ=30 because the comparative advantage of the text mining approach is strongest for short time intervals subsequent to the publication of corporate disclosures. As soon as “historical” time series re<sup>fl</sup>ect the capital market reaction, models being purely based on quantitative data may pick up on these developments, too.

## 4.3. Text pre-processing

Analogously to [28] we interpret text mining — similar to data mining — “as the application of algorithms and methods from the <sup>fi</sup>elds machine learning and statistics to texts with the goal of <sup>fi</sup>nding useful patterns”. For this purpose it is necessary to pre-process the texts accordingly because below data mining algorithms are not able to cope with plain text as input. Certain pre-processing tasks need to be conducted to transform textual documents into a numeric representation. Analogously to [9], the three pre-processing steps Feature Extraction, Feature Selection, and Feature Representation were employed.

Table 2  
![](/api/attachments/D33Q464T/fulltext/images/e54d1293c173456e838a76e5ca3be3a1be2cb090d659665ed3b07c59a7434273.jpg)

![](/api/attachments/D33Q464T/fulltext/images/e0b17c16711e61ebc2550ef723e1382910c72114abea1401f7c5666d9b5c1ac2.jpg)  
Fig. 3. Empirical ARISK distributions of corporate disclosures.

During Feature Extraction, a dictionary of words and phrases is generated that describes the document adequately. As already implied by the previous statement, “words” were used as features because we expect them to be more meaningful than for instance n-grams. We make use of a simple StringTokenizer [56] which uses the Unicode speci<sup>fi</sup>cation to identify separators by non-letter characters. Given that numbers constitute non-letter characters, the resulting tokens, i.e. words, contain letters only. Words with little meaning, but frequent appearance, are dealt with by means of a (German) Stopword List. In order to ensure that the same word in different grammatical forms is actually interpreted as one, both the Porter Stemmer [46] and a simple GermanStemmer [56] have been applied. These basically map different grammatical forms of a word to a common stem by removing af<sup>fi</sup>xes (suf<sup>fi</sup>xes or pre<sup>fi</sup>xes). Even though the Porter Stemmer was not primarily developed to <sup>fi</sup>t the German language, our pre-tests revealed that its’ stemming capability is superior to the one of the GermanStemmer. Therefore, our results are shown for the Porter Stemmer only.

Eliminating those features that contain few or relatively little information is usually referred to as Feature Selection. Consequently, Feature Selection helps to reduce the dimensionality of the feature set. Besides the already mentioned Stopword List, we make use of a minimum and maximum threshold on the number of documents each token occurs in. In order to further reduce the feature set, feature scoring methods (<sup>fi</sup>lter methods) using both Information Gain and Chi-Squared metrics were implemented. Our pre-test results, however, revealed that feature selection on the basis of Chi-Squared generally performed better than on the basis of Information Gain. Therefore below results are provided for Chi-Squared-based feature selection only. The optimal number (and selection) of utilized features is derived by below mentioned simple iteration grid-search loop and is annotated as f; whereby f = all means that all original features were used.

Finally, during Feature Representation, each document is represented by previously extracted and selected number of features. The respective feature weightings in the document-feature matrix W are given by tf-idf. tf denotes the term frequency of a feature in a document and idf denotes the inverse number of documents the feature appears in [36].

Descriptive statistics of ARISK.

<table><tr><td></td><td> $ARISK_{\tau=15}$ </td><td> $ARISK_{\tau=30}$ </td></tr><tr><td>Quartile (75%)</td><td>0.281%</td><td>0.239%</td></tr></table>

## 4.4. Classifier: data mining techniques

The following data mining techniques can basically be divided into two broad categories: While approaches such as Naïve Bayes (NB) build upon probabilities (of a feature belonging to a certain category), approaches such as k-Nearest Neighbour (kNN), Neural Networks (NNet), or Support Vector Machine (SVM) interpret the documentfeature-matrix W spatially.

The respective parameters of below described techniques were optimized by means of a simple iteration grid-search loop, i.e. optimal parameter settings were obtained by varying combinations of assigned parameter values.

## 4.4.1. Naïve Bayes (NB)

Bayesian classi<sup>fi</sup>ers are based on Bayes’ theorem. Thereby, classes are assigned to documents based on the joint probabilities of features (words) and classes. As Bayesian classi<sup>fi</sup>ers represent probabilistic approaches, these are based on a probabilistic model of the data observed. In our case, the applied learner uses normal distributions in order to estimate real-valued distributions of data [40]. Classi<sup>fi</sup>er NB is termed “naïve” because it assumes that all features in the documentfeature-matrix W are independent of each other. Even though the “naïve assumption” seems unrealistic, Langley et al. [35] — among others — have shown that the NB classi<sup>fi</sup>er performs surprisingly well. Others studies such as the one from Yang and Liu[59], however, <sup>fi</sup>nd that “both a sign test and an error-based proportion test suggest that […] NB signi<sup>fi</sup>cantly underperforms all other classi<sup>fi</sup>ers”, i.e. both SVM and kNN. Especially with text mining, i.e. large number of features, the “naïve assumption” simpli<sup>fi</sup>es learning.

## 4.4.2. k-Nearest neighbour (kNN)

Prior to kNN classi<sup>fi</sup>cation there is no “real” learning phase, i.e. no explicit models are build. Instead, each new document D (from an independent test data set) is on-the-<sup>fl</sup>y compared to all training documents identifying similarities. The class of test document D is then determined by the class labels of k (= number) nearest, i.e. most similar, training documents. There is a wide range of similarity measures that could be applied to kNN. The simplest approach would be to count the number of common words in two documents and normalize this measure by the length of the documents [28]. Other measures are — for instance — based on the vector space model, where each document is represented by a numerical feature vector (see also Feature Representation above). Frequently used measures are given by the Euclidean distance, cosine similarity, or Jaccard similarity [34] whereby the latter one is actually mostly used within information retrieval (IR). We also make use of the latter three similarity measures. Both the number of neighbours, i.e. k, and the <sup>fi</sup>nally used similarity measure are derived by above mentioned iterative parameter optimization.

## 4.4.3. Neural network (NNet)

An arti<sup>fi</sup>cial NNet aims to mimic a biological human network and consists of an input layer, an output layer, and (optionally) a number of hidden layers in between. The network receives its’ data through the input layer, and the respective response is dispensed at the output layer. Each layer consists of at least one neuron. In our case the output layer consists of more than one neuron because we decided to train one NNet for all categories. The layers’ neurons are connected to each other (but not within a layer) and the connections are given weights.

The implemented feed-forward network [40] allows the information to move forward only, i.e. neurons are not allowed to receive input from subsequent layers’ neurons. The weighted input to each neuron is summed to a net value, converted to an activation function and passed through a transfer function to produce an output, i.e. decide whether or not to “<sup>fi</sup>re”. We make use of the following transfer functions: Sigmoid function, linear function, and sine function. Training of the multilayer NNet is conducted by means of Backpropagation. Thereby, through an iterative process the (squared) error between NNet output values and respective target values is — at least attempted to be — minimized. The procedure derives its’ name from the fact that the error is “fed back” through the network by adjustment of neuron connection weights in order to reduce the respective error. The learning rate determines how much the weights are adjusted at each step. A constant learning rate of 1.0 was applied. The maximum number of training cycles was set to 1000 and the training tolerance (error constraint) was set to 0.1. In other words, NNet will stop training once the error is below 0.1 or once the number of training cycles exceeds 1000. Parameter values of the learning rate, the number of training cycles and the training tolerance were derived from associated research such as van Eyden [52], who makes use of NNet in forecasting of share prices. The number of hidden layers, the number of neurons within each layer and the respective transfer function were derived by above mentioned simple parameter optimization. The number of hidden layers ranged between one (HL1) and two (HL2) and the number of neurons ranged between 1 and 25.

## 4.4.4. Support vector machine (SVM)

SVM was <sup>fi</sup>rstly introduced by [54] for solving two-class recognition problems. The general idea is to <sup>fi</sup>nd the decision surface that maximizes the margin between data points, i.e. classes. Thereby, maximizing the margin between a separating hyperplane and the nearest data points is undertaken by means of structural risk minimization. In case of originally linearly non-separable data points, the original data vectors may be mapped to higher dimensional space to achieve linear separability again [59]. For calculation ef<sup>fi</sup>ciency reasons, a linear kernel, i.e. a function in lower-dimensional space that exhibits similar behavior as the original functions in higherdimensional space, is made use of. Hsu et al. [29] have shown that the use of a linear kernel, compared to, for instance, a rbf (radial basis function) kernel, seems suf<sup>fi</sup>cient whenever the number of features is exceptionally large, as it is the case with text mining. Applying SVM with a linear kernel makes parameter optimization an easy task because contrary to NNet there is only one relevant parameter, the cost parameter C, to be optimized. In line with Hsu et al. [29] we used exponentially growing sequences of parameter C as input into above mentioned grid-search optimization, i.e. $C = 2 ^ { - 5 } , 2 ^ { - 3 } , . . . , 2 ^ { 1 5 }$ . The SVM implementation used in this study is the one provided by Chang and Lin [13], i.e. LIBSVM.

## 4.5. Post-processing

Besides “crisp” classi<sup>fi</sup>cation results, each of the above introduced classi<sup>fi</sup>cation methods additionally delivers a “soft” probability/ con<sup>fi</sup>dence value, which can be interpreted as a “guarantee of the learner that the corresponding crisp prediction is actually the true label” [40]. Documents are assigned to the classes “positive” or “negative” depending on whether the probability value is above or below a certain (learned) threshold. Varying the respective threshold will produce different points in the Receiver Operating Characteristic (ROC) space [7] and illustrates the inherent trade-off between precision and recall [28]. The variation of thresholds may, however, also be applied as a “post-processing” step to account for imbalanced data sets or unequal classi<sup>fi</sup>cation costs [58]. We are confronted with both an imbalanced data set and unequal classi<sup>fi</sup>cation costs:

(1) As labelling is conducted on the 75% quartile, the class “positive” — by de<sup>fi</sup>nition — contains 25% of all disclosures and the class “negative” contains the remaining 75% of all disclosures. By simply classifying each document as “negative”, one would already achieve a comparatively high accuracy of 75%.

(2) Within (intraday) risk management, we are mostly interested in those events that entail especially high risk exposure. Therefore, a good predictive performance for the class “negative” is not as useful to us as the same predictive performance for the class “positive”. In other words, our misclassi<sup>fi</sup>cation costs for the class “positive” are higher than for the class “negative”.

To overcome these problems, cost-sensitive learning is needed [31]. Cost-sensitive learning is not only a possible solution to unequal classi<sup>fi</sup>cation costs, but is “a good solution to the class imbalance problem” [60], too. It is against this background that we also make use of a ThresholdFinder [40] and the respective ThresholdApplier [40] that uses the classi<sup>fi</sup>ers’ con<sup>fi</sup>dence values to turn them into cost-sensitive learners.

## 5. “Classic” model evaluation

Model evaluation is undertaken by means of $\cdot _ { g } .$ -fold (g = 10) cross validation. Thereby, the complete data set S is split up into g subsets S . Subsets are “strati<sup>fi</sup>ed”, i.e. class distributions remain almost the same after sampling. Having run through g validations, each document in the corpus has been both part of the training data set and the test data set. Each (1/g) test sub-sample contingency table is aggregated to create a global contingency table (micro averaging).

## 5.1. Accuracy, recall, precision, F-measure

The global contingency table is then used to calculate the performance measures accuracy $\displaystyle [ ( a + d ) / n ; n = a + b + c + d ]$ , recall [class “positive”: a/(a+c)], and precision [class “positive”: a/(a+b)] (Table 3) [28].

As there is a trade-off between recall and precision, the <sup>fi</sup>gures shall not be assessed in isolation. We therefore additionally calculate the $F _ { 1 }$ measure by [53], where recall and precision are given equal weight (Eq. (5)).

$$
F _ {1} = (2 \cdot \text { recall } \cdot \text { precision }) / (\text { recall } + \text { precision })\tag{5}
$$

Exemplary illustration of (global) contingency table.

<table><tr><td></td><td>True “positive”</td><td>True “negative”</td></tr><tr><td>Predicted “positive”</td><td>a</td><td>b</td></tr><tr><td>Predicted “negative”</td><td>c</td><td>d</td></tr></table>

Classi<sup>fi</sup>cation results for above introduced classi<sup>fi</sup>cation methods can be found in Table 4. Results are shown for τ=15 and 30 and for a variety of misclassi<sup>fi</sup>cation cost combinations (i.e. in brackets following the classi<sup>fi</sup>cation method). As we are mostly interested in “good” classi<sup>fi</sup>cation results for the class “positive”, those cases with comparatively high misclassi<sup>fi</sup>cation values for this class are of most interest to us, e.g. (0.1;0.9) or (0.3;0.9). The other cases are merely shown to illustrate the inherent trade-off between precision and recall.

Below results demonstrate this trade-off: High (misclassi<sup>fi</sup>cation) costs of the class “positive”, e.g. 0.9, result in a high precision <sup>fi</sup>gure and a low recall <sup>fi</sup>gure. kNN(0.1;0.9), NNet(0.1;0.9), and SVM(0.1;0.9) reveal a precision of 100% and a recall below 12% for τ=15. In other words, there are only few corporate disclosures assigned to the class “positive” (i.e. low recall). Nonetheless, all of those disclosures that were assigned to the class “positive” actually belong there (i.e. high precision). This is due to the fact that disclosures are merely assigned to the high-risk class “positive” if the respective con<sup>fi</sup>dence value is quite high, i.e. greater than the (learned) threshold. These results already indicate that the proposed text mining approach is capable to precisely identify some of the most relevant corporate disclosures entailing high risk.

Nevertheless, as already stated, the high precision <sup>fi</sup>gure comes at the cost of low recall (and the other way around): In other words, we merely capture a small number of relevant high-risk disclosures. Therefore, one might be willing to accept a certain number of “false positives” to increase the number of “caught” high-risk disclosures. This can be done by lowering the misclassi<sup>fi</sup>cation costs for the class “positive” or increasing the misclassi<sup>fi</sup>cation costs for the class “negative”. It can be observed that this change in costs increases the F -measure (up to a certain level). In our case, however, it shall be ensured that the precision <sup>fi</sup>gure stays well above 50%. In the end, it is up to the risk manager to decide upon the individual threshold.

NB, kNN, NNet, and SVM reveal an accuracy that is — at least in those cases that are most relevant to risk management applications — (slightly) above the 75% guessing equivalent benchmark. It shall, however, be noted that this simple benchmark would assign each disclosure to the class “negative”. But as we are mostly interested in a good classi<sup>fi</sup>cation performance of the class “positive”, the <sup>fi</sup>gure accuracy in general and the benchmark in particular are not seen as good model evaluation methods in this context. We merely show them to complete the picture.

Overall, it can be concluded that, depending on the respective thresholds (i.e. misclassi<sup>fi</sup>cation costs), the proposed text mining approach seems to meet expectations. Regarding the applied classi<sup>fi</sup>cation methods, there seems to be no clear predominant method. NB, however, is in those cases most relevant to us consistently inferior to the other methods. Nonetheless, results differ for the periods τ=15 and 30.

## 5.2. Area under the curve

Within above described post-processing step, we have already seen that the variation of threshold values produces different points in the ROC space. These points make up a curve and the area under the curve (AUC) can be used as an additional measure of a classi<sup>fi</sup>er's performance [7]. According to [14] AUC “is an accepted traditional performance metric for a ROC curve […] and the AUC comparison can establish a dominance relationship between classi<sup>fi</sup>ers”. Therefore, we also apply this measure.

Analogously to the above accuracy, precision, and recall results, the AUC values illustrated in Table 5 provide evidence that the classi<sup>fi</sup>cation methods kNN, NNet, and SVM are superior to NB.

In addition, given these descriptive AUC values, kNN seems to perform better than both NNet and SVM for τ=15 and 30. In other words: If we were not only interested in a very high precision with a reasonable recall, kNN would constitute a viable alternative to the more sophisticated methods NNet and SVM. Between NNet and SVM we do not <sup>fi</sup>nd a consistent dominance relationship for both τ=15 and 30.

Table 4  
“Classic” evaluation/classi<sup>fi</sup>cation results.

<table><tr><td rowspan="2"></td><td rowspan="2">Method(cost “negative”;cost “positive) $^{e}$ </td><td colspan="4"> $\tau = 15$ </td><td colspan="4"> $\tau = 30$ </td></tr><tr><td>Accuracy (in %)</td><td>Precision (in %)</td><td>Recall (in %)</td><td> $F_1$ (in %)</td><td>Accuracy (in %)</td><td>Precision (in %)</td><td>Recall (in %)</td><td> $F_1$ (in %)</td></tr><tr><td>(1)</td><td>NB(0.1;0.9) $^{a}$ </td><td>75.18</td><td>100</td><td>0.94</td><td>1.87</td><td>75.65</td><td>80.00</td><td>3.77</td><td>7.21</td></tr><tr><td>(1)</td><td>kNN(0.1;0.9) $^{b}$ </td><td>76.83</td><td>100</td><td>7.55</td><td>14.04</td><td>77.30</td><td>100</td><td>9.43</td><td>17.24</td></tr><tr><td>(1)</td><td>NNet(0.1;0.9) $^{c}$ </td><td>77.78</td><td>100</td><td>11.32</td><td>20.34</td><td>78.01</td><td>100</td><td>12.26</td><td>21.85</td></tr><tr><td>(1)</td><td>SVM(0.1;0.9) $^{d}$ </td><td>77.30</td><td>100</td><td>9.43</td><td>17.24</td><td>78.72</td><td>100</td><td>15.09</td><td>26.23</td></tr><tr><td>(2)</td><td>NB(0.3;0.9) $^{a}$ </td><td>75.18</td><td>53.85</td><td>6.60</td><td>11.76</td><td>75.89</td><td>64.29</td><td>8.49</td><td>15.00</td></tr><tr><td>(2)</td><td>kNN(0.3;0.9) $^{b}$ </td><td>77.54</td><td>64.86</td><td>22.64</td><td>33.57</td><td>78.96</td><td>66.04</td><td>33.02</td><td>44.03</td></tr><tr><td>(2)</td><td>NNet(0.3;0.9) $^{c}$ </td><td>77.30</td><td>61.90</td><td>24.53</td><td>35.14</td><td>78.72</td><td>66.67</td><td>30.19</td><td>41.56</td></tr><tr><td>(2)</td><td>SVM(0.3;0.9) $^{d}$ </td><td>78.49</td><td>64.71</td><td>31.13</td><td>42.04</td><td>78.96</td><td>68.09</td><td>30.19</td><td>41.83</td></tr><tr><td>(3)</td><td>NB(0.5;0.9) $^{a}$ </td><td>74.00</td><td>46.15</td><td>22.64</td><td>30.38</td><td>71.87</td><td>40.30</td><td>25.47</td><td>31.21</td></tr><tr><td>(3)</td><td>kNN(0.5;0.9) $^{b}$ </td><td>74.47</td><td>48.96</td><td>44.34</td><td>46.53</td><td>75.89</td><td>51.92</td><td>50.94</td><td>51.43</td></tr><tr><td>(3)</td><td>NNet(0.5;0.9) $^{c}$ </td><td>74.94</td><td>50.00</td><td>39.62</td><td>44.21</td><td>77.54</td><td>55.67</td><td>50.94</td><td>53.20</td></tr><tr><td>(3)</td><td>SVM(0.5;0.9) $^{d}$ </td><td>77.78</td><td>57.14</td><td>45.28</td><td>50.53</td><td>77.07</td><td>54.74</td><td>49.06</td><td>51.74</td></tr><tr><td>(4)</td><td>NB(0.9;0.9) $^{a}$ </td><td>54.85</td><td>32.51</td><td>74.53</td><td>45.27</td><td>51.06</td><td>32.65</td><td>89.62</td><td>47.86</td></tr><tr><td>(4)</td><td>kNN(0.9;0.9) $^{b}$ </td><td>62.65</td><td>37.25</td><td>71.70</td><td>49.03</td><td>68.79</td><td>42.70</td><td>71.70</td><td>53.52</td></tr><tr><td>(4)</td><td>NNet(0.9;0.9) $^{c}$ </td><td>65.25</td><td>39.59</td><td>73.58</td><td>51.49</td><td>62.41</td><td>37.56</td><td>75.47</td><td>50.16</td></tr><tr><td>(4)</td><td>SVM(0.9;0.9) $^{d}$ </td><td>65.72</td><td>39.68</td><td>70.75</td><td>50.85</td><td>69.50</td><td>42.48</td><td>61.32</td><td>50.19</td></tr><tr><td>(5)</td><td>NB(0.9;0.1) $^{a}$ </td><td>33.33</td><td>27.32</td><td>100</td><td>42.91</td><td>43.03</td><td>30.55</td><td>100</td><td>46.80</td></tr><tr><td>(5)</td><td>kNN(0.9;0.1) $^{b}$ </td><td>38.06</td><td>28.80</td><td>100</td><td>44.73</td><td>40.43</td><td>29.61</td><td>100</td><td>45.69</td></tr><tr><td>(5)</td><td>NNet(0.9;0.1) $^{c}$ </td><td>39.24</td><td>29.20</td><td>100</td><td>45.20</td><td>40.19</td><td>29.53</td><td>100</td><td>45.59</td></tr><tr><td>(5)</td><td>SVM(0.9;0.1) $^{d}$ </td><td>38.30</td><td>28.88</td><td>100</td><td>44.82</td><td>39.01</td><td>29.12</td><td>100</td><td>45.11</td></tr></table>

<sup>a</sup> NB-15: (1) f = all; (2) f = 200; (3) f = 100; (4) f = 100; (5) f = 500 // NB-30: (1) f = all; (2) f = all; (3) f = 100; (4) f = 500; (5) f = 500.  
<sup>b</sup> kNN-15: (1) f = 500, k = 55, Euclidean distance; (2) f = 1500, k = 50, cosine similarity; (3) f = all, k = 40, Jaccard similarity; (4) f = all, k = 40, Jaccard similarity; (5) f = all, k = 40, Cosine similarity // kNN-30: (1) f = 100, k = 45, Jaccard similarity; (2) f = all, k = 40, Jaccard similarity; (3) f = all, k = 55, Euclidean distance; (4) f = all, k = 55, Cosine similarity; (5) f = all, k = 50, Jaccard similarity.  
<sup>c</sup> NNet-15: (all) hidden types=sigmoid; (1) f=1500, HL1: neurons=5, HL2: neurons=3; (2) f=all, HL1: neurons=7, HL2: neurons=4; (3) f=1500, HL1: neurons=4, HL2: neurons=3; (4) f=all, HL1: neurons=7, HL2: neurons=4; (5) f=1500, HL1: neurons=4, HL2: neurons=3 // NNet-30: (all) hidden types=sigmoid; (1) f=1500, HL1: neurons=5, HL2: neurons=3; (2) f=1500, HL1: neurons=5, HL2: neurons=3; (3) f=1500, HL1: neurons=5, HL2: neurons=3; (4) f=all, HL1: neurons=6, HL2: neurons=3; (5) f=all, HL1: neurons=7, HL2: neurons=4.  
<sup>d</sup> SVM-15: (1) f=all, C=0.03125; (2) f=all, C=0.03125; (3) f=all, C=0.03125; (4) f=all, C=2; (5) f=1000, C=8 // SVM-30: (1) f=500, C=512; (2) f=all, C=0.125; (3) f=1500, C=0.03125; (4) f=500, C=2048; (5) f=500, C=8.  
<sup>e</sup> The term “cost” refers to misclassi<sup>fi</sup>cation costs for that particular class during post-processing (see above)

Table 5 Area under the curve (AUC).

<table><tr><td rowspan="2">Method</td><td colspan="2">AUC</td></tr><tr><td>(1) τ=15</td><td>(2) τ=30</td></tr><tr><td>NBa</td><td>0.511</td><td>0.514</td></tr><tr><td>kNNb</td><td>0.658</td><td>0.703</td></tr><tr><td>NNetc</td><td>0.634</td><td>0.695</td></tr><tr><td>SVMd</td><td>0.642</td><td>0.666</td></tr></table>

<sup>a</sup> NB: (1) f = 100; (2) f = 100.  
<sup>b</sup> kNN: (1) f = all, k = 40, Jaccard similarity; $( 2 ) f { = } \mathbf { a l l } , \mathbf { k } { = } 4 5 ,$ , Jaccard similarity.  
<sup>c</sup> NNet: (all) hidden types=sigmoid; (1) f=all, HL1: neurons=7, HL2: neurons=4; (2) f=1500, HL1: neurons=5, HL2: neurons=3. rons = 4: (2) f= 1500. HL1: neurons = 5. HL2: neurons = 3  
<sup>d</sup> SVM: (1) f=all, C=0.5; (2) f=1500, C=0.03125.

## 6. Simulation-based model evaluation

As seen in the previous section, “classic” evaluation methods help to discover possible dominance relationships among classi<sup>fi</sup>ers. But the knowledge about these dominance relationships does not help us to draw a <sup>fi</sup>nal conclusion about the general applicability of the proposed text mining approach. Therefore, we further want to assess the approach by applying a domain-speci<sup>fi</sup>c simulation-based evaluation. While the domain-speci<sup>fi</sup>c simulation-based evaluation of stock movement predictions is straight forward and has already been applied many times with an increasing degree of sophistication [26,41], the domain-speci<sup>fi</sup>c simulation-based evaluation of volatility forecasts has — to our knowledge — not yet been applied in this context and has also rarely been applied in other <sup>fi</sup>nancial domains. Therefore, we are the <sup>fi</sup>rst to develop and apply such an evaluation vehicle in this context.

## 6.1. Evaluation vehicle: straddle option

A (long) straddle option is a combination of both a (long) call option and a (long) put option with equivalent strike prices (Fig. 4).

A long position in a straddle option should be build up if one expects stock prices to move signi<sup>fi</sup>cantly, but the direction of movement is unclear. In other words, a long straddle is a bet on increased volatility in the future. In order to be pro<sup>fi</sup>table, the stock price movement needs to be larger than the premiums (i.e. “c minus b”; “b minus a”) paid for both the call option and the put option. While the loss of a long straddle option is limited to the premiums paid, the potential pro<sup>fi</sup>t is not capped. It follows that those stocks with highest unexpected/abnormal volatility, i.e. the volatility that is not priced into option premiums, will most likely also reveal highest pro<sup>fi</sup>ts.

![](/api/attachments/D33Q464T/fulltext/images/1276ea6b68db4b287692984f88c725fff15dc1aeb48411ebc43e3489a4d1d7ab.jpg)  
Fig. 4. Straddle option pro<sup>fi</sup>t/loss.

As the probability of pro<sup>fi</sup>table options (i.e. being heavily in-themoney) increases with higher volatility levels, volatility (risk) is a key determinant of option premiums. As volatility may be seen as the one most important input factor to option valuation and therefore also as a key determinant of (straddle) option pro<sup>fi</sup>tability, we believe that the simulation-based evaluation of a “long straddle strategy” constitutes a suitable additional tool to assess the suitability of above introduced text mining approach.

## 6.2. Simulation setup

The simulation (Fig. 5) is conducted on the same g-fold cross validation sub-samples as above analyses. In other words, it is ensured that the learned classi<sup>fi</sup>cation models are applied on independent test data sets. The remaining text mining steps, such as labelling, preprocessing, or classi<sup>fi</sup>cation, are equivalent to above approach, too.

If a corporate disclosure is assigned to the class “positive”, it is expected that it will entail a high abnormal volatility level after publication. Given that the proposed text mining approach is suitable for the underlying classi<sup>fi</sup>cation task, the (“positive”) disclosures will belong to the 25% most volatility-entailing news items. If this is the case, a long position in a straddle option is build up to pro<sup>fi</sup>t from the (expected) high abnormal volatility.

As we are mostly interested in <sup>fi</sup>nding the riskiest events, i.e. those belonging to the 25% most volatility-entailing corporate disclosures, the respective evaluation investment strategy needs to be modeled accordingly. Therefore, a straddle “long-only” investment strategy is proposed. In other words, whenever a corporate disclosure is assigned to the class “negative” no action is undertaken. It follows that the simulation itself functions as follows:

First, the classi<sup>fi</sup>cation models for NB, kNN, NNet, and SVM are created based on a learning data subset. Second, these models are applied on a test subset, and each corporate disclosure therein is assigned to either the class “positive” or the class “negative”. Third, if a corporate disclosure is assigned to the class “positive”, a long straddle position is build up in the respective company. If a corporate disclosure is assigned to the class “negative”, no further events are triggered. Fourth, if a long straddle position was build up, at option expiration (t0 + τ) either the call option or the put option is exercised. Exercising either one of the options is, of course, not undertaken if the strike price is equivalent to the stock price at expiration.

The classi<sup>fi</sup>ers’ return populations are also compared to a benchmark strategy $( R _ { \mathrm { L O N G } } )$ . Hereby, a long straddle position is build up for each event in the data set irrespective of the content of the 423 corporate disclosures. We decided to use an “all-long” strategy as benchmark for the following reasons: First, above empirical results on ARISK provide evidence that regulatory-driven corporate disclosures entail signi<sup>fi</sup>cant intraday market risk. We expect the market to be aware of this issue, too. Therefore, it seems viable to make use of an “all-long” straddle benchmark strategy. Second, this benchmark strategy produces highest mean returns compared to, for instance, an “all-short“ strategy.

![](/api/attachments/D33Q464T/fulltext/images/25137a8edc9763f4245cead3d15225237346922f8f9aaf521a8b132fccd06dc9.jpg)  
Fig. 5. Simulation setup.

## 6.3. Hypothetical option market

In order to calculate the premiums that need to be paid at event day (T0) to build up a long position in a straddle option, a hypothetical option market is developed [20]. In this option market, it is possible to simultaneously build up a long put and a long call position with equivalent strike prices. Moreover, the options mature at the event date T0 at t0 + τ o'clock.

The size of option premiums is calculated using the Black–Scholes option pricing model [4]. Eqs. (6)–(8) exemplarily show the calculation of a call option value $C _ { 0 } .$ Both the call option value $C _ { 0 }$ and the put option value $P _ { 0 }$ make up the straddle premium. The exercise price X is equivalent to the stock price $S _ { 0 }$ at event time (t0). The annualized one-week EURIBOR (Euro Interbank Offered Rate) at event date (T0) was taken as input for the risk-free interest rate r. Time to maturity M is given by the annualized τ. The Black–Sholes option pricing model has previously been applied on an intraday basis in a different context, i.e. with very short maturities [6,27].

$$
C _ {0} = S _ {0} N (d _ {1}) - X e ^ {- r M} N (d _ {2})\tag{6}
$$

where

$$
d _ {1} = \frac {\ln \left(\frac {S _ {0}}{X}\right) + \left(r + \frac {\sigma^ {2}}{2}\right) M}{\sigma \sqrt {M}}\tag{7}
$$

$$
d _ {2} = d _ {1} - \sigma \sqrt {M}\tag{8}
$$

$C _ { 0 }$ Current call option value

$S _ { 0 }$ Current stock price (at event time t0)

$N ( d )$ Probability that a random draw from a standard normal distribution will be less than d.

X Exercise price

r Risk-free interest rate (annualized)

M Time to maturity (annualized τ)

As stated above, the most important input factor to option valuation is volatility. Above $A R I S K _ { \tau }$ results show that the chosen event type is — in most cases — followed by abnormal volatility levels. We believe that the market is aware of this fact. Accordingly, the options on the hypothetical market are priced conservatively. In other words, the hypothetical investors need to pay high premiums to build up a long straddle.

While above labelling is conducted on an abnormal risk measure $( A R I S K _ { \tau } ) ,$ , the option premium calculation is based on a “normal” risk measure, i.e. $R I S K _ { [ t 1 , t 2 ] }$ (Eq. (3)). However, both “classic” and simulation-based evaluation results for $R I S K _ { [ t 1 , t 2 ] } -$ labelling (not shown here) basically provide the same evidence. As the Black– Scholes option pricing model requires annualized volatility as input, $R I S K _ { \tau }$ is annualized in line with [17] (see Eq. (9)).

$$
R I S K _ {\tau , a n n} = \sqrt {\frac {\Delta t _ {s c a l e}}{\Delta t}} R I S K _ {\tau}\tag{9}
$$

with $\Delta t _ { s c a l e } = 1$ year; $\Delta t = 1 5$ and 30 min.

Each option is priced at $\mathsf { Q U A R T I L E } ( R I S K _ { \tau , \mathsf { \ a n n } } )$ , with QUARTILE $( R I S K _ { \tau , \mathrm { ~ a n n } } )$ de<sup>fi</sup>ned as the 75% quartile of all documents’ $R I S K _ { \tau , }$ ann during the $\tau = 1 5$ and 30 min following the disclosure publication.

Furthermore, it shall also be taken into account that the proposed simulation-based approach constitutes an additional text mining evaluation metric. We do not intend it to be a viable investment strategy per se as it will be a challenge to <sup>fi</sup>nd options with above described short maturities.

## 6.4. Simulation-based evaluation results

Descriptive statistics of return populations $R _ { \mathrm { N B ( n e g . ; p o s . ) } } ,$ R<sub>kNN(neg.;pos.)</sub>, $R _ { \mathrm { N N e t ( n e g . ; p o s . ) } } , R _ { \mathrm { S V M ( n e g . ; p o s . ) } } ,$ and $R _ { \mathrm { L O N G } }$ can be found in Table 6 for both $\tau = 1 5$ and 30.

It can be observed that — similar to above “classic” classi<sup>fi</sup>cation results — high precision leads to small population sizes and high mean returns. Returns become smaller the more “false positives” are accepted to increase the population size.

Regarding the comparative performance among classi<sup>fi</sup>cation methods, again no clear consistent dominance relationship can be identi<sup>fi</sup>ed. Previously observed inferiority of NB, however, can in most cases be con<sup>fi</sup>rmed for simulation returns.

Table 6  
Descriptive statistics of simulation-based evaluation.

<table><tr><td rowspan="2">Method(cost “negative”;cost “positive) $^a$ </td><td colspan="3">τ=15</td><td colspan="3">τ=30</td></tr><tr><td>Population size</td><td>Mean (in %)</td><td>Standard deviation (in %)</td><td>Population size</td><td>Mean (in %)</td><td>Standard deviation (in %)</td></tr><tr><td> $R_{NB(0.1;0.9)}$ </td><td>1</td><td>10.4754</td><td>n.a.</td><td>5</td><td>5.7957</td><td>3.9890</td></tr><tr><td> $R_{NB(0.5;0.9)}R_{kNN(0.1;0.9)}$ </td><td>8</td><td>6.5110</td><td>2.7498</td><td>10</td><td>9.3547</td><td>7.9600</td></tr><tr><td> $R_{NNet(0.1;0.9)}$ </td><td>12</td><td>9.4976</td><td>11.5246</td><td>13</td><td>8.9616</td><td>14.1268</td></tr><tr><td> $R_{SVM(0.1;0.9)}$ </td><td>10</td><td>6.8906</td><td>3.8158</td><td>16</td><td>12.4211</td><td>14.4428</td></tr><tr><td> $R_{NB(0.3;0.9)}$ </td><td>13</td><td>5.5160</td><td>5.0646</td><td>14</td><td>4.2632</td><td>3.5953</td></tr><tr><td> $R_{kNN(0.3;0.9)}$ </td><td>37</td><td>4.8852</td><td>7.8470</td><td>53</td><td>5.3746</td><td>8.7514</td></tr><tr><td> $R_{NNet(0.3;0.9)}$ </td><td>42</td><td>5.1049</td><td>7.5619</td><td>48</td><td>6.2442</td><td>11.7850</td></tr><tr><td> $R_{SVM(0.3;0.9)}$ </td><td>51</td><td>4.3330</td><td>4.1296</td><td>47</td><td>7.4302</td><td>11.9192</td></tr><tr><td> $R_{NB(0.5;0.9)}$ </td><td>52</td><td>3.1602</td><td>4.1959</td><td>67</td><td>2.8857</td><td>4.8626</td></tr><tr><td> $R_{kNN(0.5;0.9)}$ </td><td>96</td><td>3.7566</td><td>5.8044</td><td>104</td><td>5.5000</td><td>11.6089</td></tr><tr><td> $R_{NNet(0.5;0.9)}$ </td><td>84</td><td>3.2647</td><td>5.8029</td><td>97</td><td>5.6099</td><td>11.6440</td></tr><tr><td> $R_{SVM(0.5;0.9)}$ </td><td>84</td><td>4.9830</td><td>7.7459</td><td>95</td><td>4.9853</td><td>9.0468</td></tr><tr><td> $R_{NB(0.9;0.9)}$ </td><td>243</td><td>2.7507</td><td>6.2932</td><td>291</td><td>3.4090</td><td>7.6432</td></tr><tr><td> $R_{kNN(0.9;0.9)}$ </td><td>204</td><td>3.0939</td><td>5.6429</td><td>178</td><td>4.3150</td><td>9.2132</td></tr><tr><td> $R_{NNet(0.9;0.9)}$ </td><td>197</td><td>3.2480</td><td>5.9011</td><td>213</td><td>3.2770</td><td>5.4961</td></tr><tr><td> $R_{SVM(0.9;0.9)}$ </td><td>189</td><td>3.4181</td><td>6.5515</td><td>153</td><td>4.8070</td><td>10.1700</td></tr><tr><td> $R_{NB(0.9;0.1)}$ </td><td>388</td><td>2.5450</td><td>5.8961</td><td>347</td><td>3.3845</td><td>7.5380</td></tr><tr><td> $R_{kNN(0.9;0.1)}$ </td><td>368</td><td>2.6293</td><td>6.0353</td><td>358</td><td>3.3744</td><td>7.4344</td></tr><tr><td> $R_{NNet(0.9;0.1)}$ </td><td>363</td><td>2.6117</td><td>6.0745</td><td>359</td><td>3.3495</td><td>7.4233</td></tr><tr><td> $R_{SVM(0.9;0.1)}$ </td><td>367</td><td>2.5949</td><td>6.0504</td><td>364</td><td>3.3665</td><td>7.3819</td></tr><tr><td> $R_{LONG}$ </td><td>423</td><td>2.3883</td><td>5.6768</td><td>423</td><td>3.0101</td><td>6.9184</td></tr></table>

<sup>a</sup> The term “cost” refers to misclassi<sup>fi</sup>cation costs for that particular class during post-processing (see above).

The benchmark strategy exhibits positive mean returns $( R _ { \mathrm { L O N G } } )$ . As the pricing of straddle options has been quite conservative, the positive benchmark mean returns are most likely the result of extreme volatility outliers in the whole sample. Remember that the pro<sup>fi</sup>t from a long straddle option is not capped (see above). Nevertheless, the classi<sup>fi</sup>cation methods’ mean returns are, depending on the applied thresholds (i.e. misclassi<sup>fi</sup>cation costs), much higher than the benchmark mean returns. This <sup>fi</sup>nding provides <sup>fi</sup>rst evidence that the proposed text mining approach precisely identi<sup>fi</sup>es some of the most volatility-enhancing corporate disclosures.

To further statistically explore above descriptive results, corresponding null- and alternative hypotheses are formulated:

$$
\begin{array}{l} H _ {0}: \mu \Big (R _ {\text {Method} (;)} \Big) \leq \mu (R _ {\text {LONG}}); H _ {A}: \mu \Big (R _ {\text {Method} (;)} \Big) > \mu (R _ {\text {LONG}}) \\ H _ {0}: \mu \Big (R _ {\text {Method1} (;)} \Big) \leq \mu \Big (R _ {\text {Method2} (;)} \Big); H _ {A}: \mu \Big (R _ {\text {Method1} (;)} \Big) > \mu \Big (R _ {\text {Method2} (;)} \Big) \end{array}
$$

Hereby, the term “Method[1,2](;)” represents the classi<sup>fi</sup>cation methods NB, kNN, NNet, and SVM, respectively, with varying misclassi<sup>fi</sup>cation cost inputs. If either one of the null hypotheses can be rejected, we can statistically corroborate a higher population mean of $R _ { \mathrm { M e t h o d ( n e g . ; p o s . ) } } \left( R _ { \mathrm { M e t h o d 1 ( n e g . ; p o s . ) } } \right)$ compared to R<sub>LONG</sub> (R<sub>Method2(neg.;pos.)</sub>) for that classi<sup>fi</sup>cation cost setting at a given level of signi<sup>fi</sup>cance. We conduct two-sample t-tests assuming unequal variances with a hypothesized mean of zero. Test statistics are summarized in Table 7.

Comparing the classi<sup>fi</sup>cation methods to the benchmark strategy, null hypotheses can be consistently rejected at high levels of signi<sup>fi</sup>cance for those cases where high class “positive” precision is achieved, i.e. for (0.1;0.9), (0.3;0.9) and (0.5;0.9). Merely NB (and partially NNet) does not consistently statistically signi<sup>fi</sup>cantly perform better than the benchmark strategy; especially in the important cases of high class “positive” misclassi<sup>fi</sup>cation costs. These <sup>fi</sup>ndings provide strong evidence that the proposed intraday text mining approach is capable to identify (abnormally) risky events.

Comparing the classi<sup>fi</sup>cation methods with each other, SVM is the only method that more than once performs statistically signi<sup>fi</sup>cantly better than NB. While kNN statistically signi<sup>fi</sup>cantly outperforms NNet once, SVM statistically signi<sup>fi</sup>cantly outperforms NNet twice. Moreover, SVM is most often among those methods exhibiting highest levels of signi<sup>fi</sup>cance, i.e. at the 1%-level.

As most of the classi<sup>fi</sup>cation method dominance relationships — except on NB — are, however, not consistent for different misclassi-<sup>fi</sup>cation cost inputs and observation periods (τ = 15 and 30) respectively, we may conclude that these basically perform alike (given our settings).

If we additionally take into account the computational effort dimension, we may conclude that SVM is the method of choice for this learning task: We intentionally conducted the underlying study on an intraday basis because — from our point of view — potential sources of risk should be identi<sup>fi</sup>ed as fast as possible. Hereby, kNN — despite of above convincing results — reveals a potential drawback as it requires many calculations during classi<sup>fi</sup>cation. Moreover, the adjustment, i.e. model building, of NNet to a larger document base is time consuming as well.

## 7. Conclusion and future research

To date, “traditional” risk management tools have largely neglected one of the largest sources of information, i.e. unstructured qualitative data. Therefore, existing risk management approaches are not able to suf<sup>fi</sup>ciently capture/predict extreme intraday market movements (at event time) triggered by new information released to the market. However, as the mitigation of intraday market risk is important to many market participants [25], we propose an intraday risk management approach that also makes use of qualitative, unstructured data.

Table 7  
t-values from classi<sup>fi</sup>cation methods’ simulation-based mean hypotheses testing

<table><tr><td rowspan="2">≤</td><td colspan="4">τ=15</td><td colspan="4">τ=30</td></tr><tr><td>μ(RkNN(0.1;0.9))</td><td>μ(RNNet (0.1;0.9))</td><td>μ(RSVM(0.1;0.9))</td><td>μ(RLONG)</td><td>μ(RkNN(0.1;0.9))</td><td>μ(RNNet(0.1;0.9))</td><td>μ(RSVM(0.1;0.9))</td><td>μ(RLONG)</td></tr><tr><td>μ(RNB(0.1;0.9))</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-1.07</td><td>-0.70</td><td>-1.57*</td><td>1.38</td></tr><tr><td>μ(RkNN(0.1;0.9))</td><td></td><td>-0.82</td><td>-0.23</td><td>3.83***</td><td></td><td>0.08</td><td>-0.67</td><td>2.37**</td></tr><tr><td>μ(RNNet(0.1;0.9))</td><td></td><td></td><td>0.70</td><td>2.04**</td><td></td><td></td><td>-0.62</td><td>1.45*</td></tr><tr><td>μ(RSVM(0.1;0.9))</td><td></td><td></td><td></td><td>3.46***</td><td></td><td></td><td></td><td>2.51**</td></tr><tr><td>≤</td><td>μ(RkNN(0.3;0.9))</td><td>μ(RNNet(0.3;0.9))</td><td>μ(RSVM(0.3;0.9))</td><td>μ(RLONG)</td><td>μ(RkNN(0.3;0.9))</td><td>μ(RNey(0.3;0.9))</td><td>μ(RSVM(0.3;0.9))</td><td>μ(RLONG)</td></tr><tr><td>μ(RNB(0.3;0.9))</td><td>0.32</td><td>0.22</td><td>0.75</td><td>2.10**</td><td>-0.71</td><td>-0.99</td><td>-1.57*</td><td>1.19</td></tr><tr><td>μ(RkNN(0.3;0.9))</td><td></td><td>-0.12</td><td>0.39</td><td>1.87**</td><td></td><td>-0.41</td><td>-0.96</td><td>1.88**</td></tr><tr><td>μ(RNNet(0.3;0.9))</td><td></td><td></td><td>0.58</td><td>2.24**</td><td></td><td></td><td>-0.48</td><td>1.85**</td></tr><tr><td>μ(RSVM(0.3;0.9))</td><td></td><td></td><td></td><td>3.01***</td><td></td><td></td><td></td><td>2.47***</td></tr><tr><td>≤</td><td>μ(RkNN(0.5;0.9))</td><td>μ(RNNet(0.5;0.9))</td><td>μ(RSVM(0.5;0.9))</td><td>μ(RLONG)</td><td>μ(RkNN(0.5;0.9))</td><td>μ(RNNet(0.5;0.9))</td><td>μ(RSVM(0.5;0.9))</td><td>μ(RLONG)</td></tr><tr><td>μ(RNB(0.5;0.9))</td><td>-0.71</td><td>-0.12</td><td>-1.76**</td><td>1.19</td><td>-2.03**</td><td>-2.05**</td><td>-1.90**</td><td>-0.18</td></tr><tr><td>μ(RkNN(0.5;0.9))</td><td></td><td>0.56</td><td>-1.18</td><td>2.08**</td><td></td><td>-0.07</td><td>0.35</td><td>2.09**</td></tr><tr><td>μ(RNNet(0.5;0.9))</td><td></td><td></td><td>-1.62*</td><td>1.26</td><td></td><td></td><td>0.41</td><td>2.10**</td></tr><tr><td>μ(RSVM(0.5;0.9))</td><td></td><td></td><td></td><td>2.90***</td><td></td><td></td><td></td><td>1.99**</td></tr><tr><td>≤</td><td>μ(RkNN(0.9;0.9))</td><td>μ(RNNet(0.9;0.9))</td><td>μ(RSVM(0.9;0.9))</td><td>μ(RLONG)</td><td>μ(RkNN(0.9;0.9))</td><td>μ(RNNet(0.9;0.9))</td><td>μ(RSVM(0.9;0.9))</td><td>μ(RLONG)</td></tr><tr><td>μ(RNB(0.9;0.9))</td><td>-0.61</td><td>-0.85</td><td>-1.07</td><td>0.74</td><td>-1.10</td><td>0.23</td><td>-1.49*</td><td>0.71</td></tr><tr><td>μ(RkNN(0.9;0.9))</td><td></td><td>-0.27</td><td>-0.52</td><td>1.46*</td><td></td><td>1.32*</td><td>-0.46</td><td>1.69**</td></tr><tr><td>μ(RNNet(0.9;0.9))</td><td></td><td></td><td>-0.27</td><td>1.71**</td><td></td><td></td><td>-1.69**</td><td>0.53</td></tr><tr><td>μ(RSVM(0.9;0.9))</td><td></td><td></td><td></td><td>1.87**</td><td></td><td></td><td></td><td>2.02**</td></tr><tr><td>≤</td><td>μ(RkNN(0.9;0.1))</td><td>μ(RNNet(0.9;0.1))</td><td>μ(RSVM(0.9;0.1))</td><td>μ(RLONG)</td><td>μ(RkNN(0.9;0.1))</td><td>μ(RNNet(0.9;0.1))</td><td>μ(RSVM(0.9;0.1))</td><td>μ(RLONG)</td></tr><tr><td>μ(RNB(0.9;0.1))</td><td>-0.19</td><td>-0.15</td><td>-0.11</td><td>0.38</td><td>0.02</td><td>0.06</td><td>0.03</td><td>0.71</td></tr><tr><td>μ(RkNN(0.9;0.1))</td><td></td><td>0.04</td><td>0.08</td><td>0.58</td><td></td><td>0.04</td><td>0.01</td><td>0.70</td></tr><tr><td>μ(RNNet(0.9;0.1))</td><td></td><td></td><td>0.04</td><td>0.53</td><td></td><td></td><td>-0.03</td><td>0.66</td></tr><tr><td>μ(RSVM(0.9;0.1))</td><td></td><td></td><td></td><td>0.49</td><td></td><td></td><td></td><td>0.69</td></tr></table>

\*\*\*, \*\* and \* indicate signi<sup>fi</sup>cance at the 1%, 5% and 10%-level.

The associated task of text analysis has been especially challenging, as we identi<sup>fi</sup>ed a majority of those regulatory-driven corporate disclosures followed by statistically signi<sup>fi</sup>cant abnormal volatility levels. The underlying text mining approach was designed to identify those corporate disclosures that are associated with highest abnormal volatility levels.

By means of an empirical study, we show that today's technology is capable of extracting valuable information from corporate disclosures for risk management purposes. Both a “classic” and a newly developed domain-speci<sup>fi</sup>c simulation-based evaluation con<sup>fi</sup>rm the suitability of our approach to identify most critical, i.e. volatilityenhancing, market events. We therefore conclude that intraday market risk exposures can be discovered utilizing text mining techniques.

Moreover, we show that more sophisticated classi<sup>fi</sup>cation methods such as kNN, NNet, or SVM perform better than NB. Taking into account both classi<sup>fi</sup>cation results and computational ef<sup>fi</sup>ciency, SVM turns out to be the method of choice for this particular learning task.

Future research will include the application of above intraday text mining approach to an extended data set. It is, for example, of greatest interest whether or not the proposed approach also works in times of market turmoil. Existing research on trend forecasting could provide a basis to further re<sup>fi</sup>ne our risk management approach by estimating up and downside risk exposure by developing corresponding classi<sup>fi</sup>ers.

## Acknowledgement

We thankfully acknowledge the support of the E-Finance Lab, Frankfurt for this work.

## References

[1] H.-J. Ahn, K.-H. Bae, K. Chan, Limits orders, depth, and volatility: evidence from the stock exchange of Hong Kong, Journal of Finance 56 (2) (2001).

[2] S. Allen, Financial risk management: a practitioner's guide to managing market and credit risk, J. Wiley & Sons, Hoboken, N.J., 2003.

[3] T. Andersen, T. Bollerslev, F. Diebold, P. Labys, Modeling and forecasting realized volatility, Econometrica 71 (2) (2003).

[4] F. Black, M. Scholes, The pricing of options and corporate liabilities, The Journal of Political Economy 81 (3) (1973).

[5] A.N. Bom<sup>fi</sup>m, Pre-announcement effects, news effects, and volatility: monetary policy and the stock market, Journal of Banking & Finance 27 (1) (2003).

[6] P. Bossaerts, P. Hillion, A test of a general equilibrium stock option pricing model, Mathematical Finance 3 (4) (1993).

[7] A. Bradley, The use of the area under the ROC curve in the evaluation of machine learning algorithms, Pattern Recognition 30 (7) (1997).

[8] C. Brooks, G. Persand, Volatility forecasting for risk management, Journal of Forecasting 22 (1) (2003).

[9] H. Brücher, G. Knolmayer, M.-A. Mittermayer, Document classi<sup>fi</sup>cation methods for organizing explicit knowledge, in: H. Tsoukas, N. Mylonopoulos (Eds.), Proceedings of the European Conference on Organizational Knowledge, Learning and Capabilities, 2002, Athens, Greece.

[10] J.Y. Campbell, M. Lettau, B.G. Malkiel, Y. Xu, Have individual stocks become more volatile? an empirical exploration of idiosyncratic risk, Journal of Finance 56 (1) (2001).

[11] J.Y. Campbell, A.W. Lo, A.C. MacKinlay, The econometrics of <sup>fi</sup>nancial markets, Princeton Univ. Press, Princeton, NJ, USA, 1997.

[12] M.E. Carter, B.S. Soo, The relevance of Form 8-K reports, Journal of Accounting Research 37 (1) (1999).

[13] C.-C. Chang, C.-J.L. Lin, LIBSVM: A Library for Support Vector Machines, http:// www.csie.ntu.edu.tw/ cilin/libsym/(2009-05-01).

[14] N.V. Chawla, K.W. Bowyer, L.O. Hall, W.P. Kegelmeyer, SMOTE: synthetic minority over-sampling technique, Journal of Arti<sup>fi</sup>cial Intelligence Research 16 (1) (2002).

[15] P.F. Christoffersen, F.X. Diebold, How relevant is volatility forecasting for <sup>fi</sup>nancial risk management? The Review of Economics and Statistics 82 (1) (2000).

[16] F. Corsi, G. Zumbach, U.A. Muller, M.M. Dacorogna, Consistent high-precision volatility from high-frequency data, Economic Notes 30 (2) (2001).

[17] M.M. Dacorogna, R. Gençay, U.A. Müller, R.B. Olsen, O.V. Pictet, An introduction to high-frequency <sup>fi</sup>nance, Academic Press, San Diego, CA, 2001.

[18] B. Dehning, V.J. Richardson, R.W. Zmud, The value relevance of announcements of transformational information technology investments, MIS Quarterly 27 (4) (2003).

[19] G. Dionne, P. Duchesne, M. Pacurar, Intraday value at risk (IVaR) using tick-by-tick data with application to the Toronto Stock Exchange, Journal of Empirical Finance 16 (5) (2009).

[20] R. Engle, C. Hong, A. Kane, Valuation of variance forecasts with simulated option markets, NBER Working Paper No. 3350, 1990.

[21] E.F. Fama, The behavior of stock-market prices, The Journal of Business 38 (1) (1965).

[22] E.F. Fama, L. Fisher, M.C. Jensen, R. Roll, The adjustment of stock prices to new information, International Economic Review 10 (1) (1969).

[23] G.P.C. Fung, J.X. Yu, W. Lam, Stock prediction: integrating text mining approach using real-time news, Proceedings of the IEEE International Conference on Computational Intelligence for Financial Engineering, IEEE, 2003.

[24] G.P.C. Fung, J.X. Yu, H. Lu, The predicting power of textual information on <sup>fi</sup>nancial markets, IEEE Intelligent Informatics Bulletin 5 (1) (2005).

[25] P. Giot, Market risk models for intraday data, The European Journal of Finance 11 (4) (2005).

[26] S.S. Groth, J. Muntermann, Supporting investment management processes with machine learning techniques, in: H.R. Hansen, D. Karagiannis, H.-G. Fill (Eds.), Proceedings of the 9. Internationale Tagung Wirtschaftsinformatik, Österreichische Computer Gesellschaft, Wien, Austria, 2009

[27] L.E. Harris, V. Panchapagesan, The information content of the limit order book: evidence from NYSE specialist trading decisions, Journal of Financial Markets 8 (1) (2005).

[28] A. Hotho, A. Nurnberger, G. Paaß, A brief survey of text mining, GLDV Journal for Computational Linguistics and Language Technology 20 (1) (2005).

[29] C.-W. Hsu, C.-C. Chang, C.-J. Lin, A Practical Guide to Support Vector Classi<sup>fi</sup>cation, http://www.csie.ntu.edu.tw/ cjlin/papers/guide/guide.pdf (2009–12–10).

[30] W. Huang, Y. Nakamori, S.-Y. Wang, Forecasting stock market movement direction with support vector machine, Computers & Operations Research 32 (10) (2005).

[31] M. Ikonomakis, S. Kotsiantis, V. Tampakas, Text Classi<sup>fi</sup>cation Using Machine Learning Techniques, WSEAS Transactions on Computers 4 (8) (2005).

[32] P. Jorion, Value at risk: the new benchmark for managing <sup>fi</sup>nancial risk, McGraw-Hill, New York, 2001.

[33] P. Jorion, Financial risk manager handbook, Wiley & Sons, Hoboken, NJ, 2007.

[34] R.R. Korfhage, Information storage and retrieval, Wiley & Sons, New York, NY, 1997.

[35] P. Langley, W. Iba, K. Thompson, An analysis of Bayesian classi<sup>fi</sup>ers, Proceedings of the Tenth National Conference on Arti<sup>fi</sup>cial Intelligence, 1992 Seattle, WA.

[36] D.D. Lewis, Representation and Learning in Information Retrieval (Dissertation, University of Massachusetts, Amherst, MA, 1992).

[37] A.W. Lo, Risk management for hedge funds: introduction and overview, Financial Analysts Journal 57 (6) (2001).

[38] Y. Luo, K. Liu, D.N. Davis, A multi-agent decision support system for stock trading, IEEE Network 16 (1) (2002).

[39] D. McMillan, R. Garcia, Intra-day volatility forecasts, Applied Financial Economics 19 (8) (2009).

[40] I. Mierswa, M. Wurst, R. Klinkenberg, M. Scholz, T. Euler, YALE: rapid prototyping for complex data mining tasks, in: L. Ungar, M. Craven, D. Gunopulos, T. Eliassi-Rad (Eds.), Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, Philadelphia, PA, 2006.

[41] M.-A. Mittermayer, Forecasting Intraday Stock Price Trends with Text Mining Techniques, in: R.H. Sprague (Ed.), Proceedings of the 37th Hawaii International Conference on System Science, Computer Society Press, Los Alamitos, CA, 2004.

[42] M.-A. Mittermayer, G.F. Knolmayer, Text mining systems for market response to news: a survey, working paper no. 184, University of Bern, 2006

[43] J. Muntermann, A. Güttler, Intraday stock price effects of ad hoc disclosures: the German case, Journal of International Financial MarketsInstitutions and Money 17 (1) (2007).

[44] M. Parkinson, The extreme value method for estimating the variance of the rate of return, The Journal of Business 53 (1) (1980).

[45] J.M. Patell, M.A. Wolfson, The intraday speed of adjustment of stock prices to earnings and dividend announcements, Journal of Financial Economics 13 (2) (1984).

[46] M.F. Porter, An algorithm for suf<sup>fi</sup>x stripping, Program 14 (3) (1980).

[47] A. Schulz, M. Spiliopoulou, K. Winkler, Kursrelevanzprognose von Ad-hoc-Meldungen: Text Mining wider die Informationsüberlastung im Mobile Banking, in: W. Uhr, W. Esswein, E. Schoop (Eds.), Proceedings of the Internationale Tagung Wirtschaftsinformatik, Physika, Germany, Heidelberg, 2003.

[48] R.P. Schumaker, H. Chen, Textual analysis of stock market prediction using breaking <sup>fi</sup>nancial news: the AZFin Text System, ACM Transactions on Information Systems 27 (2) (2009).

[49] B.F. Smith, R. White, M. Robinson, R. Nason, Intraday volatility and trading volume after takeover announcements, Journal of Banking & Finance 21 (3) (1997).

[50] M. Subramani, E. Walden, The impact of E-commerce announcements on the market value of <sup>fi</sup>rms, Information Systems Research 12 (2) (2001)

[51] J.D. Thomas, News and Trading Rules, in, (Dissertation, Carnegie Mellon University, Pittsburgh, PA, 2003).

[52] R.J. van Eyden, The application of neural networks in the forecasting of share prices, Finance & Technology Publishing, Haymarket, VA, 1996.

[53] C.J. van Rijsbergen, Information retrieval, Butterworths, London, England, 1979.

[54] V. Vapnik, The nature of statistical learning theory, Springer, New York, NY, 1995.

[55] R.A. Wood, T.H. McInish, J.K. Ord, An investigation of transactions data for NYSE stocks, Journal of Finance 40 (3) (1985)

[56] M. Wurst, The Word Vector Tool: User Guide, Operator Reference, Developer Tutorial, http://wvtool.sf.net (2009–05–04).

[57] B. Wuthrich, V. Cho, S. Leung, D. Permunetilleke, K. Sankaran, J. Zhang, Daily stock market forecast from textual web data, Proceedings of the IEEE Internationa Conference on Systems, Man, and Cybernetics, 1998, San Diego, CA.

[58] Y. Yang, A study of thresholding strategies for text categorization, Proceedings of the 24th ACM International Conference on Research and Development in Information Retrieval, 2001, New Orleans, LA.

[59] Y. Yang, X. Liu, A re-examination of text categorization methods, Proceedings of the 22nd Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM, Berkeley, CA, 1999.

[60] Z.-H. Zhou, X.-Y. Liu, Training cost-sensitive neural networks with methods addressing the class imbalance problem, IEEE Transactions on Knowledge and Data Engineering 18 (1) (2006)

![](/api/attachments/D33Q464T/fulltext/images/8e9f5590b8358110e1601511ab0787bddc4001d0c862534c3cb9714106437a96.jpg)

Sven S. Groth is Graduate Researcher at the E-Finance Lab an industry–academic partnership between Goethe University Frankfurt, Germany and several (<sup>fi</sup>nancial) industry partners. He is currently writing his PhD thesis under the supervision of Prof. Dr. Peter Gomber at the Chair of Business Administration especially e-Finance (Goethe University Frankfurt). Sven studied business administration at the European Business School (ebs), Oestrich-Winkel, Germany and Real Estate Investment at the University of Reading Business School, Reading, UK. His research interests include decision support systems and Algorithmic Trading.

![](/api/attachments/D33Q464T/fulltext/images/f0a80ce335ea06b3b426af9a03b412719d191b3101c456e8a478ec408f117140.jpg)

Jan Muntermann is Assistant Professor of Information Systems and holds the E-Finance Lab endowed Chair of E-Finance and Securities Trading at Goethe University Frankfurt. His research interests include design science, decision support systems and IT valuation, especially in the <sup>fi</sup>elds of E-Finance and Mobile Business. In these <sup>fi</sup>elds, he has published in journals and proceedings such as Decision Support Systems, Journal of Electronic Commerce Research, Journal of International Financial Markets, Institu tions and Money and ICIS. Jan holds a PhD from Frankfurt University and has been a Visiting Scholar at Microsoft Research (Cambridge) and London Business School.

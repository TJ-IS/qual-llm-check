---
otero_id: 13780
otero_key: "NVKBWE66"
title: "Long-term stock index forecasting based on text mining of regulatory disclosures"
authors: "Stefan Feuerriegel; Julius Gordon"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.06.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Long-term stock index forecasting based on text mining of regulatory disclosures

![](/api/attachments/NVKBWE66/fulltext/images/e372b3ff2530aef52739497bc4ac5f22d00f6202d748ad52683241c03b1d18ac.jpg)

Stefan Feuerriegel, Julius Gordon

<table><tr><td>PII:</td><td>S0167-9236(18)30105-2</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2018.06.008</td></tr><tr><td>Reference:</td><td>DECSUP 12966</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>31 December 2017</td></tr><tr><td>Revised date:</td><td>20 June 2018</td></tr><tr><td>Accepted date:</td><td>21 June 2018</td></tr></table>

Please cite this article as: Stefan Feuerriegel, Julius Gordon , Long-term stock index forecasting based on text mining of regulatory disclosures. Decsup (2018), doi:10.1016/ j.dss.2018.06.008

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Long-term stock index forecasting based on text mining of regulatory disclosures

Stefan Feuerriegel<sup>a,∗</sup>, Julius Gordon<sup>b</sup>

<sup>a</sup>ETH Zurich, Weinbergstr. 56/58, 8092 Zurich, Switzerland <sup>b</sup>Chair for Information Systems Research, University of Freiburg, Platz der Alten Synagoge, 79098 Freiburg, Germany

## Abstract

Share valuations are known to adjust to new information entering the market, such as regulatory disclosures. We study whether the language of such news items can improve short-term and especially long-term (24 months) forecasts of stock indices. For this purpose, this work utilizes predictive models suited to high-dimensional data and specifically compares techniques for data-driven and knowledge-driven dimensionality reduction in order to avoid overfitting. Our experiments, based on 75,927 ad hoc announcements from 1996–2016, reveal the following results: in the long run, text-based models succeed in reducing forecast errors below baseline predictions from historic lags at a statistically significant level. Our research provides implications to business applications of decision-support in financial markets, especially given the growing prevalence of index ETFs (exchange traded funds).

Keywords: Text mining, Natural language processing, Financial news, Financial forecasting, Stock index, Predictive analytics

## 1. Introduction

The eficient market hypothesis formalizes how financial markets process and respond to new information [1]. Its semi-strong form states that asset prices fully reflect publicly-available information. Based on this premise, one can expect price changes whenever new information enters the market. In practice, regulations ensure that stock-relevant information is revealed primarily via regulatory disclosures in order to provide equal access for all market participants. Such materials disclose, for instance, quarterly earnings, but also management changes, legal risks and other events deemed important [2]. Accordingly, financial disclosures present an alluring and potentially financially-rewarding means of forecasting changes in stock valuations [3].

In this respect, corporate news conveys a broad spectrum of information concerning the past performance and current challenges of the business [4], as well as frequently hinting at the future outlook. Research has followed this reasoning and empirically quantified the impact of the narrative content on the subsequent stock market responses [cf. 5, 6, 7]. Moreover, researchers have also demonstrated the prognostic capability of financial disclosures with respect to individual stock market returns in the short term [e. g. 8, 9, 10]. Accordingly, news-based forecasting has received considerable traction and, as a result, various publications have evaluated diferent news datasets, forecasted indicator/markets, preprocessing operations from the field of natural language processing and forecasting algorithms. Here we refer to the literature, which provides a thorough overview [3].

Forecasting the development of stock indices is highly demanded by multiple stakeholders in financial markets. The underlying reason is that households are investing their money no only in individual stocks, government bonds or savings accounts; rather, they increasingly prefer exchange-traded funds (ETFs). These ETFs replicate the movements of marketable securities, with stock indices being the most prominent example. As part of their benefits, ETFs are traded on stock exchanges but often with higher liquidity and lower fees. Hence, private investors demand for decision support in better understanding the development of markets, as well as for obtaining prognostic support. For instance, more than 1700 diferent index ETFs have emerged, amouting to total assets worth more than USD 2.1 trillion.<sup>1</sup>

While previous studies provide empirical evidence suggesting a link between financial disclosures and stock index dynamics in the short run, further research is needed to investigate the possibility of long-term forecasting. In this regard, a recent literature review reveals that evidence concerning the long-term prognostic power of financial news is scarce [3]. As a remedy, it presents the object of this paper to investigate the predictive capacity of regulatory disclosures in forecasting future index levels in the long term. This undertaking seems especially relevant for practitioners in, for example, monetary policy and the investment industry as their decision-making is based on the economic outlook, as is reflected by market indices.

Despite these aforementioned investigations, it has yet to be established whether financial disclosures can facilitate the long-term forecasting of stock indices. For this purpose, we need to make provisions for the high-dimensional predictor matrices that arise in text mining and thus experiment with diferent methods from machine learning that are carefully chosen for our setting. This presents a challenging undertaking that is often referred to as “wide” data, since the presence of single words entails only little prognostic power and, in addition, we face a higher number of predictors than observations, which must be efectively handled. This increases the risk of overfitting and we thus show that dimensionality reduction can provide efective means to overcome this problem.

The novelty of this work is to apply text mining procedures in order to evaluate long-term forecasts of stock indices with wide predictor matrices. We specifically run experiments with (1) machine learning and high-dimensional news. We further extend these models by means of additional feature reduction in order to reduce the risk of overfitting through data-driven dimensionality reduction. (2) We aggregate diferent sentiment scores and then insert these into our machine learning models. This represents a form of explicit feature engineering as part of a knowledge-driven dimensionality reduction. (3) We perform an a priori reduction process in order to filter news from large-cap firms as these might be more relevant. Altogether, the extensive set of experiments yields prescriptive recommendations for implementing powerful news-based forecasts.

In this work, we utilize 75,927 regulatory ad hoc announcements in German and English together with three diferent stock indices, namely, the German prime index (DAX), the German composite index (CDAX), and the STOXX Europe 600. Our text-based models include extreme gradient boosting, principal component regression and the random forest, as well as the elastic net with it special cases, the lasso and ridge regression. Our models are compared to diferent techniques for linear and non-linear autoregression that serve as our baselines. We note that our implementation was carefully designed to circumvent a potential look-ahead bias [11, 12], which would incorporate variables that are not present at the time of the forecast. While not all predictive experiments outperform the baselines, our evaluations still reveal the promising performance of our text-based predictions, especially for the long-term forecasts.

Our proposed text mining approach provides decision support for financial markets and thus entails a number of implications for management and individuals. On the one hand, our machine learning framework contributes to automated trading in financial markets. It also helps managers from institutional trading in making profitable investment decisions. On the other hand, it even facilitates retail investors, such as individual investors from online trading platforms, in managing their portfolio. Given the prevalence of ETFs as a widespread investment instrument for private households, the findings of this work have thus also direct implications to

this group of stakeholders.

The remainder of this paper is organized as follows. The above introduction has outlined a research gap concerning the long-term forecasts of stock indices based on the language embedded in corporate disclosures. To address this issue, we review related work (Section 2) and introduce our text mining models for news-based forecasting in Section 3 and our datasets in Section 4. Section 5 then measures the improvements of our text-based forecasts over time series models with autoregressive terms. Based on the findings, Section 6 discusses the implications of our work, while Section 7 concludes.

## 2. Related work

## 2.1. Decision support from financial news

News-based predictions have become a common theme in decision support literature, yet rarely with a focus on stock indices. Hence, we decided to present a relatively broad overview that illustrates examples from the diferent streams in previous research. For a complete overview, we refer to the survey of predictive text mining for financial news in [3, 13]. Accordingly, related works evaluate different (1) forecasting algorithms from the field of natural language, (2) forecasted market variables and (3) news datasets. These are outlined in the following.

The underlying algorithms are often named opinion mining or sentiment analysis, consistent with the terminology in computational natural language processing [14]. These can extract both the fundamental and qualitative information that forms the foundation for the decision-making of market stakeholders [15, 16, 17]. The underlying forecasting techniques usually follow the same procedure, where the first step pre-processes the running text and then transforms it into a mathematical representation that serves as input to a subsequent machine learning classifier [3, 18, 19]. Examples include support vector machines [5, 17, 19], decision tree classifiers [20], artificial neural networks and boosting methods [20, 3]. Alternatively, algorithms based on deep learning circumvent the manual need for feature engineering [8]. Yet other works explicitly cater for the time-varying nature of sentiments [21].

These approaches are used to forecast various indicators of interest. These include, for instance, nominal returns [17], abnormal returns [8], optimal trading decisions [22], and market volatility [23]. A recent contribution by [24] applied an ontology-based web mining framework to improve the accuracy of unemployment rate predictions in the US. In some cases, individual news are further enriched by the wisdom of crowds [25]. Yet an even diferent stream of research is interested in macroeconomic indicators [26].

Examples of news sources include newspaper articles from media sources, such as the Wall Street Journal, Bloomberg, Yahoo Finance [e. g. 19]; news wires; and regulated fillings, such as ad hoc announcem nts, 8-K fillings and annual reports [e. g. 9, 22, 17, 18, 27]. Additional sources cover alternative media, such as social media, user-generated content and microblogs [e. g. 28, 29, 30, 31].

## 2.2. Stock index forecasting

The link between disclosure content and financial markets is found not only for individual stocks, but also in the case of stock indices. For instance, the S&500 index [32] is positively correlated with specifically constructed sentiment metrics. In a predictive setting, media articles facilitate forecasting experiments that predict the same-day return of the Dow Jones index [33]. Similarly, the momentum of news tone seems capable of predicting the direction of CDAX movements [34]. Here the predictions are made between one and ten weeks ahead, but this work lacks a rigorous comparison to baselines (e. g. time series models) in order to convincingly demonstrate that the text-based forecast outperforms simple autoregressive models. Hence, the added value of news-based predictors remains unclear.

# ACCEPTED MANUSCRIPT

In the context of this manuscript, a wide array of previous works have investigated the possibility of forecasting stock indices based merely on historic values and, hence, we point out only a few illustrative examples in the following. Forecasting experiments have been undertaken for various indices such as the S&P 500 [35, 36], the NYSE [37], the Dow Jones Industrial Average [38], the NIKKEI 225 [39] and also for emerging markets [40]. These works frequently utilize time series analysis methods, such as autoregressive or moving-average processes, occasionally together with approaches for volatility modeling [37, 36, 41]. Works located in the proximity of machine learning also experiment, for instance, with support vector machines [39, 37], neural networks [42, 35, 40], and hybrid models of neural networks and autoregression [38]. Hence, we utilize both autoregressive and non-linear machine learning models with historic values as our benchmarks.

Previous research [43] also provides evidence as to why our approach is likely to be superior, i. e. the constant-parameters in classical time series analysis are designed to capture stationary processes, while our approach can even model the event-driven jump due to corporate disclosures.

## 3. Text mining framework

This section details the forecasting models that serve as our baselines, as well as the models based on the content of financial disclosures. These aim at forecasting a financial time series $Y _ { t }$ with $t = 1 , \dots , T$ . The common challenge behind the following procedures is that the predictor matrix is extremely wide, which leads to the risk of overfitting. Hence, we overcome this problem by data-driven dimensionality reduction and explicit feature engineering with domain knowledge through sentiment analysis.

## 3.1. Baselines with lagged data

We implement a linear autogressive model (lm) in order to forecast future observations from the historic time series, where the variable l refers to the number of lags, t to current time step and $t + h$ to the forecasted time step when making a prediction h steps ahead. The autoregressive process is then modeled via

$$
Y _ {t + h} = \alpha + \beta_ {1} Y _ {t - 1} + \ldots + \beta_ {l} Y _ {t - l} + \varepsilon_ {i},\tag{1}
$$

with coeficients $\alpha , \beta _ { 1 } , \ldots , \beta _ { l }$ . It thus expects predictors $Y _ { t - 1 } , \ldots , Y _ { t - l }$ in order to forecast $Y _ { t + h }$

We also apply machine learning models to the input vector $[ Y _ { t - 1 } , \ldots , Y _ { t - l } ] ^ { T }$ with l lags. This allows us to relax the assumption of a linear relationship and specifically test for non-linear dependencies. In this regard, we choose the same set of machine learning models as in the case of text-based approaches, namely, least squares absolute shrinkage operator (lasso), ridge regression, elastic net (enet), gradient boosting (gbm), principal component regression (pcr) and random forest (rf).

## 3.2. Sentiment-based machine learning

Predictions from several hundred documents as a single observation have oftentimes demonstrated to increase the risk of overfitting. A viable trade-of is commonly presented by drawing upon sentiment dictionaries as a form of feature engineering. Here the idea is to incorporate domain knowledge in the form of predefined dictionaries that label terms into diferent semantic categories [44]. The conventional assumption is that the overall sentiment hints the economic outlook [45, 46, 7]. Sentiment dictionaries have frequently been utilized in explanatory research where the objective is to identify a statistically significant relationship between content of financial disclosures and the corresponding stock market reaction [e. g. 21, 34], yet empirical evidence on their potential advantage in long-term predictive settings is scarce.

We create a predictor matrix consisting out of l autoregressive lags and additional scores. Here we experiment with three approaches:

1. We compute a single sentiment score that reflects the overall polarity of the language. This is given by the relative ratio between the number of positive and negative words, i. e. $\frac { \# \mathrm { p o s i t i v e } - \# \mathrm { n e g a t i v e } } { \# t o t a l } .$

2. Beyond that, we also compute separate scores measuring the use of positive and negative language. These are formalized by ratios $\frac { \# \mathrm { p o s i t i v e } } { \# t o t a l }$ and $\frac { \# \mathrm { n e g a t i v e } } { \# t o t a l } .$

3. Sentiment dictionaries often consist of further categories, such as uncertainty expressions (especially with regard to the economic climate). Hence, we extend our previous positivity and negativity metrics by a proportional score of uncertainty words.

The computational advantage of these approaches is that even long narrative materials can be easily mapped on a numerical figure that can adapt to the underlying valence of the tone, as well as the economic outlook. At the same time, this procedure reduces the degrees-of-freedom immensely and instead, replaces these by domain knowledge as encoded in the dictionaries, thereby diminishing the potential of overfitting.

In all of our experiments, we incorporate the Loughran-McDonald financespecific dictionary<sup>2</sup> which has evolved as a quasi-standard in finance-related research [7]. This dictionary has specifically constructed such that they can extract qualitative materials from financial news in order to yield numerical scores.

## 3.3. Text-based machine learning

Text-based require that the running text is transformed in a machine-ready representation, to which one can later apply a machine learning classifier [47]. For this reason, the conventional bag-of-words approach is to process the original document by counting the frequency of tokens [3, 14, 13]. These frequencies can optionally be weighted, until they finally serve as features in the machine learning models.

![](/api/attachments/NVKBWE66/fulltext/images/e378e40d7b71a612bfa8e0c77062eaedc7542b152589124d9ad33561f29058c8.jpg)  
Figure 1: Text mining framework that serves as the foundation of a decision support system for facilitating decision-making in financial markets.

Our text-based models adhere to the previous approach and we thus detail our methodology in the following (cf. Figure 1). We remove numbers, punctuations, and stop words<sup>3</sup>, followed by stemming. We then count the frequency of all terms appearing in the disclosures belonging to each time step t = 1, . . . , T . This results in a document-term matrix X ∈ <sup>RT</sup> <sup>×P</sup> where the columns refer to the diferent frequencies of all P terms. Hence, one row denotes the frequency of the terms in the disclosures of a single time step t. We subsequently scale the matrix by the relative informativeness of words as defined by the tf-idf weighting [47]. The resulting rows then serves as the main predictors for future values $Y _ { t + h }$

The corpus is further processed in order to yield high-dimensional predictor matrices as detailed in the following. More precisely, the document-term matrix X entails an extremely wide format, wherein the number of predictors exceeds the observations by far. We thus follow a heuristic approach for reducing the dimensionality of X further. That is, we omit rare terms for which the corresponding columns contain more than 10 % of sparse entries to reduce the risk of overfitting, as well as the necessary computational resources.

Care is necessary when choosing a suitable machine learning model, since we require model that can generalize well even with more predictors than data samples. In other words, we face a situation where the number of words exceeds the number of past observations, which can easily result in overfitting for many machine learning models. As a remedy, we decide upon predictive models that are perform known to handle such wide datasets efectively [48]: lasso, ridge regression, elastic net, gradient boosting, principal component regression and random forest, which uilize implicit feature selection, regularization or dimensionality reduction in order to yield a favorable bias-variance tradeof and thus avoid potential overfitting.

Beyond tf-idf features, we also experiment with alternative approaches as part of our feature engineering in order to reduce the risk of overfitting. That is, we apply techniques for unsupervised dimensionality reduction: the document-term semantic analysis (lsa).

Subsequently, we evaluate two distinct strategies to news-based forecasts: (1) the above document-term matrices or its transformations serve as the sole predictor (i. e. l = 0). (2) The document term-matrices are further augmented by l autoregressive terms from the predicted stock index with l = 1 or l = 6. As a result, the latter approach further adapt to seasonalities and short-term trends. Altogether, this yields 63 diferent predictive models as subject for our experiments (i. e. 7 classifiers, with raw tf-idf and 2 adaptations, namely, pca and lsa; each with three choices of l).

## 3.4. Parameter calibration

We proceed as follows in order to tune the hyperparameters of our predictive models. For that purpose, we chronologically split the dataset into two subsets for training (60 % of observations) and testing (remaining 40 %) in order to preserve the temporal order of the disclosures. We then find the best-performing parameters by performing a grid search. More specifically, we utilize time-series cross-validation with a rolling forecast origin [49]. This procedure first splits the training data T into k disjoint subsets $\mathcal { T } _ { 1 } , \ldots , \mathcal { T } _ { k }$ in temporal order. We then iterate over all possible combinations of the tuning ranges for each parameter and all values of $i = 2 , \ldots , k$ For each combination, we learn the model parameters from the previous subsets in time given by $\mathcal { T } _ { 1 } , \ldots , \mathcal { T } _ { i - 1 }$ . Subsequently, we compute the performance of this model calibration on the validation set $\tau _ { i } .$ . Finally, we return the best-performing hyperparameter setting.

Throughout this paper, all computational experiments are performed by utilizing k = 10 splits. We rely upon the default search grid as defined by the “caret” package in R for reasons of comparability [50].

## 4. Datasets

## 4.1. Regulatory disclosures

Our dataset of regulatory disclosures contains all ad hoc announcements that were disseminated by the DGAP (Deutsche Gesellschaft fuer Ad-hoc-Publizitaet), a subsidy of EQS Group, which is the leading publishing service provider for mandatory ad hoc announcements in Germany. Government regulations require firms to publish all stock-relevant materials first and without delay via this channel. The disclosure of these filings is obligated by regulatory policies according to the German Securities Trade Act and afects all firms listed on German stock exchanges. As a result, the rules not only apply for German firms but also for foreign ones listed there, which is the reason why these disclosures are typically published in German, English or both. We thus specifically compare the prognostic capabilities of the aforementioned languages in predicting stock prices. The choice of this dataset entails a number of practical advantages. First, the strict publication rules warrant a timely publication and ensure that the content is relevant to stock markets. This prohibits firms from disseminating the information via the press before filing an ad hoc disclosure. Second, each ad hoc announcement must be signed by the head of the company. Third, the quality of all filings is further quality-checked by the Federal Financial Supervisory Authority (i. e. BaFin).

We collected all 80,813 ad hoc announcements from July 1996 through April 2016 that were disseminated by the DGAP.<sup>4</sup> These materials were retrieved via the dedicated online channel (http://www.dgap.de/dgap/News/?newsType=ADHOC). We specifically note that the dataset underwent no additional (subjective) filtering steps in order eliminate the risk of data dredging and associated look-ahead biases [11, 12], which would incorporate information that are not present at the time of the forecast.

Empirical evidence has demonstrated a strong response of share prices in the wake of this type of financial news, as well as a high prognostic capability of changes in stock valuations [34]. Moreover, the content of such disclosures also enables previous works in predicting volatility and risk-related metrics [51]. Altogether, this indicates that ad hoc announcements are likely to give an accurate sense of current developments for individual firms, in addition to reflecting the market environment.

## 4.2. Stock index data

Since ad hoc announcements can originate from German or even foreign corporations, we have to reflect this fact and make a corresponding choice of stock indices (see Table 1). We thus incorporate two German stock indices: the DAX includes the 30 biggest stocks trading on the Frankfurt stock exchange, while the CDAX consists of all German stocks listed in the general standard or prime standard market segments, which totals to approximately 485 firms. In addition, we experiment with the STOXX Europe 600 as another point of comparison. We collected these financial time series from Bloomberg in both weekly and monthly resolutions. This

amounts to 1,087 weekly and 260 monthly observations.

<table><tr><td>Symbol</td><td>Name</td><td>Region</td><td>Resolutions (in use)</td><td>Notes</td></tr><tr><td>DAX</td><td>German prime stock index</td><td>Germany</td><td>Monthly &amp; weekly</td><td>Index of 30 selected German blue chip stocks</td></tr><tr><td>CDAX</td><td>German composite stock index</td><td>Germany</td><td>Monthly &amp; weekly</td><td>Composite index of all stocks traded on the Frankfurt Stock</td></tr><tr><td>STOXX</td><td>STOXX Europe 600</td><td>EU</td><td>Monthly &amp; weekly</td><td>Composite index from across the European region</td></tr></table>

Table 1: Overview of predicted stock indices.

## 4.3. Summary statistics

<table><tr><td>Year</td><td>Disclosures</td><td>Mean length</td><td>DAX</td><td>CDAX</td><td>STOXX</td></tr><tr><td>1996 (Jul-Dec)</td><td>424</td><td>134.08</td><td>2591.79</td><td>240.79</td><td>154.80</td></tr><tr><td>1997</td><td>1523</td><td>136.55</td><td>3744.49</td><td>335.59</td><td>211.79</td></tr><tr><td>1998</td><td>1911</td><td>167.12</td><td>5058.75</td><td>435.16</td><td>272.84</td></tr><tr><td>1999</td><td>3863</td><td>218.98</td><td>5391.62</td><td>457.76</td><td>312.62</td></tr><tr><td>2000</td><td>6954</td><td>247.26</td><td>7049.20</td><td>578.83</td><td>379.73</td></tr><tr><td>2001</td><td>8814</td><td>184.30</td><td>5612.18</td><td>448.99</td><td>314.87</td></tr><tr><td>2002</td><td>4983</td><td>178.78</td><td>4111.16</td><td>345.18</td><td>249.62</td></tr><tr><td>2003</td><td>4676</td><td>189.64</td><td>3205.03</td><td>280.41</td><td>204.03</td></tr><tr><td>2004</td><td>4095</td><td>193.73</td><td>3984.07</td><td>351.00</td><td>239.83</td></tr><tr><td>2005</td><td>4112</td><td>204.08</td><td>4706.41</td><td>418.40</td><td>279.14</td></tr><tr><td>2006</td><td>4221</td><td>218.66</td><td>5962.27</td><td>536.32</td><td>336.00</td></tr><tr><td>2007</td><td>4449</td><td>237.32</td><td>7563.47</td><td>682.81</td><td>378.89</td></tr><tr><td>2008</td><td>4012</td><td>241.40</td><td>6149.94</td><td>546.43</td><td>278.03</td></tr><tr><td>2009</td><td>3500</td><td>253.12</td><td>5021.33</td><td>433.34</td><td>215.69</td></tr><tr><td>2010</td><td>3054</td><td>274.83</td><td>6161.05</td><td>538.48</td><td>256.21</td></tr><tr><td>2011</td><td>2982</td><td>296.49</td><td>6679.14</td><td>589.70</td><td>261.42</td></tr><tr><td>2012</td><td>2903</td><td>304.52</td><td>6911.78</td><td>611.16</td><td>262.67</td></tr><tr><td>2013</td><td>3099</td><td>289.79</td><td>8374.98</td><td>748.53</td><td>303.06</td></tr><tr><td>2014</td><td>3031</td><td>295.35</td><td>9616.60</td><td>860.55</td><td>338.88</td></tr><tr><td>2015</td><td>2811</td><td>306.32</td><td>11006.63</td><td>993.91</td><td>380.60</td></tr><tr><td>2016 (Jan-Apr)</td><td>510</td><td>314.09</td><td>10021.38</td><td>921.06</td><td>339.75</td></tr></table>

Table 2: Summary statistics of corporate disclosures, as well as the annual mean of the stock index data.

Table 2 provides summary statistics related to our dataset. On average, each ad hoc announcement contains 232.7 words, while we see a slight upward trend across time. Our corpus thus entails a total of 17.7 million terms. The annual mean number of disclosures is 3,947 for the time frame covering 1997–2015. Finally, we note a high correlation coeficient between DAX and CDAX close to 1. The correlation with the STOXX Europe 600 remains below that value, amounting to 0.80 for the DAX and 0.77 in the case of the CDAX.

## 5. Results

This section describes the setup of our computational experiments, for which it then reports the results of the out-of-sample forecasting.

## 5.1. Computational setup

The purpose of our experiments is to compare the predictive performance of the benchmark models to the disclosure-based forecasts. We thus train models with the raw time series of each stock index. Here, we run our experiments by setting the number of lags to $l = 6$ in order to provide a reasonable trade-of between bias and variance. This choice yields fairly stationary subsets and has also been utilized by previous works $[ \mathrm { e . g . 5 2 , 5 3 } ]$ . We also study the sensitivity by performing experiments with a single $\log \left( l \stackrel { } { = } 1 \right)$ as a comparison. Finally, we incorporate our text-based, high-dimensional predictor matrix and train them both without lags and, consistent with above, with l = 6 lags.

Across all our experiments, we specifically forecast the raw values given by $Y _ { t + h }$ without further transformations. We explicitly refrain from using transformations, as practitioners are interested in the actual values and this thus presents a more realistic setting. The variable $Y _ { t + h }$ is easily interpretable and especially demanded by practitioners. We then make predictions across diferent forecast horizons h. Here we draw upon diferent horizons h in case of monthly and weekly resolution. All of the aforementioned values refer to a maximum forecast horizon of 24 months in both cases. The prediction for h = 1 is modeled as first-diferences as this appears to better identify turning points in the business cycle.

# ACCEPTED MANUSCRIPT

In the following, we quantify the forecast performance based on the root mean squared error (RMSE). Table 3 reports the results for the monthly time series and Table 4 for the weekly one. Furthermore, we follow the recommendations in [54] by running a Diebold-Mariano (DM) test in order to ensure the robustness of our findings. Given a certain sample, the null hypothesis tests whether forecasts with the text-based predictor matrix are at least as accurate as forecasts lacking these external inputs [55, 56]. The corresponding statistic thus reveals whether the reduction of forecast errors is statistically significant. Here we take the squarederror as the loss function. Accordingly, this provides statistical confidence regarding the advantages of utilizing the text-based models over the benchmarks with merely lagged input values for the given test data.

Detailed results by model are listed in the supplements. These contribute to the robustness of the proposed machine learning approach. Oftentimes, these predictions yield the same pattern as in the summarizing table, since, when the baseline is clearly surpassed there, we can outperform the best benchmark in both the nowcasting and the long-term scenario for the majority of machine learning models.

We further conduct the following sensitivity check. That is, we assume that the contribution of firms to the overall market movements is linked to their market capitalization. Hence, we expect the stock indices to be particularly moved by large-cap companies and thus filter our for the top-25 companies by market capitalization.

## 5.2. Prognostic power of textual materials

We now provide statistics concerning the prognostic power of news content. On the one hand, this establishes the overall relevance of textual cues as potential predictors and, on the other hand, summarizes the dificulties of the research setup: several thousands of diferent words can theoretically provide hindsight of future price changes, yet only a fairly small set of observations are available. This directly leads to the risk of overfitting and reveals the inherent methodological challenge, since the wide predictor matrix requires appropriate dimensionality reduction.

<table><tr><td>Input/model</td><td>h = 1</td><td>h = 12</td><td>h = 24</td></tr><tr><td colspan="4">Predicted variable: monthly German prime index (DAX)</td></tr><tr><td rowspan="2">Benchmark: lags</td><td>429.656</td><td>2232.505</td><td>3700.613</td></tr><tr><td>lm1</td><td>lm1</td><td>lm1</td></tr><tr><td rowspan="3">Sentiment</td><td>421.925</td><td>2241.000</td><td>3453.951</td></tr><tr><td>(0.047)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>Pos&amp;neg</td><td>Pos&amp;neg</td><td>Sentiment</td></tr><tr><td rowspan="3">Machine learning</td><td>409.662</td><td>2486.562</td><td>3089.563</td></tr><tr><td>(0.006)</td><td>(0.998)</td><td>(0.000)</td></tr><tr><td>ridge1</td><td>pca-gbm1</td><td>rf6</td></tr><tr><td rowspan="3">Incl. dimensionality reduction</td><td>411.062</td><td>2486.562</td><td>3356.676</td></tr><tr><td>(0.034)</td><td>(0.998)</td><td>(0.000)</td></tr><tr><td>pca-glmnet</td><td>pca-gbm1</td><td>pca-gbm1</td></tr><tr><td rowspan="3">Sensitivity: top-25 firms</td><td>409.662</td><td>2507.928</td><td>3026.000</td></tr><tr><td>(0.006)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>ridge1</td><td>pca-gbm1</td><td>rf1</td></tr><tr><td rowspan="3">Sensitivity: corpus</td><td>410.475</td><td>2640.812</td><td>2977.528</td></tr><tr><td>(0.115)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>Complete</td><td>Complete</td><td>German</td></tr><tr><td colspan="4">Predicted variable: monthly German composite index (CDAX)</td></tr><tr><td rowspan="2">Benchmark: lags</td><td>36.919</td><td>204.343</td><td>339.495</td></tr><tr><td>gbm1</td><td>lm1</td><td>lm1</td></tr><tr><td rowspan="3">Sentiment</td><td>36.486</td><td>205.118</td><td>316.701</td></tr><tr><td>(0.223)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>Pos&amp;neg</td><td>Pos&amp;neg</td><td>Pos&amp;neg</td></tr><tr><td rowspan="3">Machine learning</td><td>35.376</td><td>236.667</td><td>283.987</td></tr><tr><td>(0.003)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>ridge1</td><td>ridge6</td><td>rf1</td></tr><tr><td rowspan="3">Incl. dimensionality reduction</td><td>35.273</td><td>245.063</td><td>307.168</td></tr><tr><td>(0.017)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>pca-glmnet</td><td>pca-gbm1</td><td>pca-gbm1</td></tr><tr><td rowspan="3">Sensitivity: top-25 firms</td><td>35.273</td><td>229.416</td><td>284.336</td></tr><tr><td>(0.003)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>pca-glmnet</td><td>ridge1</td><td>rf</td></tr><tr><td rowspan="3">Sensitivity: corpus</td><td>35.340</td><td>246.833</td><td>273.436</td></tr><tr><td>(0.007)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>Complete</td><td>Complete</td><td>Complete</td></tr><tr><td colspan="4">Predicted variable: monthly STOXX Europe 600 index</td></tr><tr><td rowspan="2">Benchmark: lags</td><td>12.539</td><td>36.696</td><td>56.260</td></tr><tr><td>ridge6</td><td>gbm1</td><td>lm1</td></tr><tr><td rowspan="3">Sentiment</td><td>12.551</td><td>39.954</td><td>50.931</td></tr><tr><td>(0.519)</td><td>(0.972)</td><td>(0.001)</td></tr><tr><td>Sentiment</td><td>Pos&amp;neg</td><td>Sentiment</td></tr><tr><td rowspan="3">Machine learning</td><td>12.170</td><td>43.967</td><td>50.557</td></tr><tr><td>(0.120)</td><td>(0.989)</td><td>(0.000)</td></tr><tr><td>ridge6</td><td>gbm</td><td>gbm6</td></tr><tr><td rowspan="3">Incl. dimensionality reduction</td><td>12.487</td><td>45.602</td><td>50.654</td></tr><tr><td>(0.405)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>pca-rf6</td><td>pca-rf1</td><td>lsa-pcr1</td></tr><tr><td rowspan="3">Sensitivity: top-25 firms</td><td>12.170</td><td>44.799</td><td>50.654</td></tr><tr><td>(0.120)</td><td>(0.999)</td><td>(0.000)</td></tr><tr><td>ridge6</td><td>pca-rf1</td><td>lsa-pcr1</td></tr><tr><td rowspan="3">Sensitivity: corpus</td><td>12.360</td><td>45.394</td><td>36.226</td></tr><tr><td>(0.358)</td><td>(0.996)</td><td>(0.000)</td></tr><tr><td>Complete</td><td>German</td><td>German</td></tr><tr><td>Input/model</td><td>h = 1</td><td>h = 52</td><td>h = 104</td></tr><tr><td colspan="4">Predicted variable: weekly German prime index (DAX)</td></tr><tr><td rowspan="2">Benchmark: lags</td><td>236.176</td><td>2250.741</td><td>3711.472</td></tr><tr><td>glmnet6</td><td>lm1</td><td>lm1</td></tr><tr><td rowspan="3">Sentiment</td><td>236.342</td><td>2329.701</td><td>3555.981</td></tr><tr><td>(0.573)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>Pos&amp;neg</td><td>Pos&amp;neg</td><td>Pos&amp;neg</td></tr><tr><td rowspan="3">Machine learning</td><td>236.357</td><td>2510.681</td><td>3457.280</td></tr><tr><td>(0.586)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>pcr6</td><td>gbm</td><td>gbm6</td></tr><tr><td rowspan="3">Incl. dimensionality reduction</td><td>236.188</td><td>2600.012</td><td>3277.951</td></tr><tr><td>(0.503)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>pca-rf</td><td>pca-gbm1</td><td>pca-ridge6</td></tr><tr><td rowspan="3">Sensitivity: top-25 firms</td><td>235.816</td><td>2469.524</td><td>3277.951</td></tr><tr><td>(0.408)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>pca-rf1</td><td>gbm</td><td>pca-ridge6</td></tr><tr><td rowspan="3">Sensitivity: corpus</td><td>235.604</td><td>2396.174</td><td>3188.030</td></tr><tr><td>(0.309)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>German</td><td>Complete</td><td>German</td></tr><tr><td colspan="4">Predicted variable: weekly German composite index (CDAX)</td></tr><tr><td rowspan="2">Benchmark: lags</td><td>20.257</td><td>206.621</td><td>341.331</td></tr><tr><td>glmnet6</td><td>lm1</td><td>lm1</td></tr><tr><td rowspan="3">Sentiment</td><td>20.188</td><td>211.286</td><td>333.229</td></tr><tr><td>(0.285)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>Sentiment</td><td>Pos&amp;neg</td><td>Pos&amp;neg</td></tr><tr><td rowspan="3">Machine learning</td><td>20.274</td><td>235.412</td><td>328.827</td></tr><tr><td>(0.565)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>rf1</td><td>gbm</td><td>lasso</td></tr><tr><td rowspan="3">Incl. dimensionality reduction</td><td>20.251</td><td>242.067</td><td>310.824</td></tr><tr><td>(0.486)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>pca-gbm1</td><td>pca-ridge1</td><td>pca-ridge6</td></tr><tr><td rowspan="3">Sensitivity: top-25 firms</td><td>20.264</td><td>233.816</td><td>310.824</td></tr><tr><td>(0.522)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>pca-rf</td><td>ridge6</td><td>pca-ridge6</td></tr><tr><td rowspan="3">Sensitivity: corpus</td><td>20.180</td><td>220.320</td><td>304.383</td></tr><tr><td>(0.203)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>German</td><td>Complete</td><td>German</td></tr><tr><td colspan="4">Predicted variable: weekly STOXX Europe 600 index</td></tr><tr><td rowspan="2">Benchmark: lags</td><td>7.854</td><td>39.371</td><td>58.989</td></tr><tr><td>lm6</td><td>gbm1</td><td>lasso6</td></tr><tr><td rowspan="3">Sentiment</td><td>7.882</td><td>41.618</td><td>54.862</td></tr><tr><td>(0.781)</td><td>(0.989)</td><td>(0.063)</td></tr><tr><td>All categories</td><td>Pos&amp;neg</td><td>Sentiment</td></tr><tr><td rowspan="3">Machine learning</td><td>7.891</td><td>43.888</td><td>53.287</td></tr><tr><td>(0.844)</td><td>(0.992)</td><td>(0.000)</td></tr><tr><td>pcr6</td><td>rf6</td><td>pcr</td></tr><tr><td rowspan="3">Incl. dimensionality reduction</td><td>7.891</td><td>46.934</td><td>49.996</td></tr><tr><td>(0.844)</td><td>(1.000)</td><td>(0.000)</td></tr><tr><td>pca-pcr6</td><td>pca-rf</td><td>pca-rf6</td></tr><tr><td rowspan="3">Sensitivity: top-25 firms</td><td>7.891</td><td>43.366</td><td>49.996</td></tr><tr><td>(0.775)</td><td>(0.984)</td><td>(0.000)</td></tr><tr><td>pcr6</td><td>rf6</td><td>pca-rf6</td></tr><tr><td rowspan="3">Sensitivity: corpus</td><td>7.872</td><td>44.133</td><td>48.318</td></tr><tr><td>(0.632)</td><td>(0.998)</td><td>(0.000)</td></tr><tr><td>Complete</td><td>Complete</td><td>Complete</td></tr></table>

Table 3: Comparison of prediction performance (root mean squared error) across diferent monthly stock indices, where we make predictions h time steps ahead. Only the best-in-breed model is listed, for which we add bold highlighting when the model is equal or superior to the baseline. The corresponding P -value from the Diebold-Mariano test is given in brackets, as well as the type of the final model.

Table 4: Comparison of prediction performance (root mean squared error) across diferent weekly stock indices, where we make predictions h time steps ahead. Only the best-in-breed model is listed, for which we add bold highlighting when the model is equal or superior to the baseline. The corresponding P -value from the Diebold-Mariano test is given in brackets, as well as the type of the final model.

In the following, we draw upon the information-fusion-based sensitivity analysis [57], which has been widely used in the decision support literature as a tool for quantifying the relevance of predictors [58, 59]. It essentially measures the change in RMSE when omitting or including a single variable in an ensemble of all models. We computed the information-fusion-based sensitivity analysis for the text-based predictor matrix in the setting with a one-step ahead prediction of the DAX as the outcome variable. Here we yield an average sensitivity score of 1.001 for all textual cues with a standard deviation of 0.017. As a comparison, the lags attain sensitivity scores of up to 1.451. This demonstrates that only few variables have strong prognostic capacity of the outcome variable and it is thus a challenge to identify this subset. As a remedy, this paper compares diferent strategies of dimensionality reduction that either follow a data-driven logic or additionally incorporate domain knowledge.

Based on the above discussion, we later expect that, in some cases, the textbased prediction models can even be inferior to the simple baseslines. This can happen when the dimensionality reduction has not been able to identify the subset of relevant predictors and, instead, has overfitted.

## 5.3. German prime index: DAX

For the monthly data, the disclosure-based models surpass the forecast accuracy of the benchmark models for the 1 and 24-months-ahead prediction. For the shortterm horizon, the models from machine learning and large-cap firms prove to be the most accurate, achieving an RMSE of 409.662. In comparison, the best benchmark model recorded an RMSE of 429.656. For the long-term prediction horizon, the disclosure-based models prove again to be superior. The clear standout is given by the combined corpus with an RMSE of 2977.528. This yields a significant improvement over the best performing benchmark with an RMSE of 3700.613.

We find a similar pattern for the weekly resolution. A majority of the disclosurebased models are able to outperform the benchmark models. The combined corpus achieved the lowest RMSE for the one-step-ahead prediction of 235.604. Further, improvements are also attained for the 2-year-ahead horizon. The corpus sensitivity model again proves to be the most accurate with an RMSE of 3188.030. However, the benchmark model returns superior forecasts for the medium-term prediction horizon of 52 weeks.

## 5.4. German composite index: CDAX

The results of the predictive experiments undertaken for the CDAX index are as follows. For the monthly prediction experiments, the disclosure-based models outperform the benchmark over both short and long-term prediction horizons. The reduction to large-caps and the data-driven dimensionality reduction proved to be the most accurate with a RMSE of 35.273. In comparison, the best performing benchmark recorded a RMSE of 36.919. For the long-term prediction horizon the results indicate that the disclosure-based models are proven again to be superior. The best result is obtained by when utilizing the combined corpus with an RMSE of 273.436 for the 24-months-ahead horizon. This a significant improvement over RMSE of 339.495 recorded by the best performing benchmark over the same period. The results for the 12-months-ahead horizon indicate a similar result to the DAX index that the disclosure-based models were unable to out-predict the benchmark.

The RMSE values for the weekly resolution of the CDAX index illustrate that a majority of the disclosure-based models are able to outperform the benchmark over a number of prediction horizons. The corpus sensitivity again attained the best RMSE of 20.180 for the 1-week-ahead prediction horizon. The sentiment and dimensionality reduction also outperformed the benchmark RMSE of 20.257. For the one-year-ahead horizon, no disclosure-based model was able to outperform the benchmark. Finally, for the 2-year-ahead horizon, all machine learning approaches were able to record lower forecast errors than the benchmark models. The RMSE of

304.383 achieved by the German corpus significantly outperforms the best benchmark model RMSE of 341.331.

## 5.5. STOXX Europe 600 index

We now discuss the RMSE values from the prediction experiments undertaken for the monthly resolution of the STOXX 600 index. A majority of the disclosurebased models surpassed the forecast accuracy of the benchmark for the one-stepahead horizon. The models with machine learning and large-cap filtering proved to be the most accurate with both models recording a RMSE of 12.170. In comparison, the benchmark RMSE was 12.539. Further improvements in predictive accuracy over the benchmark were achieved for the 2-year-ahead horizon. This time the use of only German news obtained the most accurate prediction with a RMSE of 36.226; however, the best-of-breed results from all other approaches also recorded a better RMSE than that of the best benchmark model (36.226). In a similar result to the previous mentioned experiments for the DAX and CDAX, the benchmark models were more accurate in the medium run.

The results from the weekly prediction experiments show small variations to the previous patterns. The disclosure-based models are unable to outperform the benchmark over the short-term prediction horizons. However, we find evidence of predictability in the long run. Here we noted a lowest forecast error for the combined corpus. This is in line with our expectations as the STOXX index contains firms from all over Europe that thus might prefer reporting not only in German but also in English.

## 5.6. Comparison

The overall performance of disclosure-based forecasts varies depending on the predicted variable, forecast horizon, model choice and input choice. While the performance of disclosure-based forecasts is not superior across all experiments, we point to the following cases wherein disclosures, as a matter of fact, yield significant reductions in forecast errors. In this regard, we identify our primary finding: the text-based models help in improving the long-term forecasts of the three stock indices. Here the explicit sentiment, implicit dimensionality reduction, machine learning and sensitivity models are able over various forecast horizons to strongly outperform the benchmark. In the case of monthly data, we obtain reductions in the RMSE by 4.6 % for the DAX, 4.4 % for the CDAX, and 2.9 % for the STOXX Europe 600 for the short-term horizon. For the long-term horizon, we see reductions in RMSE of 19.5 % for the DAX, 19.4 % for the CDAX, and 35.6 % for the STOXX Europe 600.

The improvements step from diferent model choices. In the long run, the best results are often achieved by combined corpus as firms can utilize diferent languages for their reporting. Conversely, the short-term predictions largely benefit from machine learning, optionally a restriction on large-caps as part of reducing the complexity of the input. These even appear beneficial over data-driven techniques for dimensionality reduction, such as the principal component analysis. Interestingly, explicit dimensionality reduction facilitates the weekly resolution, while it impedes the monthly resolution. Sentiment-based approaches can outperform lagbased predictions, yet are themselves outperformed by other text-based machine learning. We further observe that oftentimes simple linear relationships as in the lasso appear among the best-in-breed model. A potential reason is that this type of model benefits from additional implicit reduction of the feature space and the parameters are fairly easy to calibrate, thus yielding a more robust model.

We further compare the normalized RMSE in Table 5, which allows comparison across diferent scales in the outcome variable. We find that the STOXX Europe index has lower relative prediction errors than the German indices. A potential reason could stem from the fact that the ad hoc announcements cover not only domestic corporations but also foreign firms listed at German stock exchanges. We also see a higher prognostic capacity for the DAX as compared to the composite index. A possible explanation could be that it is fairly dificult to accurately assess the wealth of information concerning all small-cap firms, thus leaving an additional component of stock dynamics that entails considerable variability and thus cannot be fully explained with our current models.

<table><tr><td>Predicted variable</td><td>Model</td><td colspan="3">Normalized RMSE</td></tr><tr><td></td><td></td><td colspan="3">Monthly resolution</td></tr><tr><td></td><td></td><td>h=1</td><td>h=12</td><td>h=24</td></tr><tr><td rowspan="3">DAX</td><td>Sentiment</td><td>16.6</td><td>31.3</td><td>53.4</td></tr><tr><td>Machine learning</td><td>16.0</td><td>35.7</td><td>47.8</td></tr><tr><td>Incl. dimensionality reduction</td><td>16.0</td><td>34.7</td><td>51.9</td></tr><tr><td rowspan="3">CDAX</td><td>Sentiment</td><td>17.1</td><td>31.4</td><td>54.5</td></tr><tr><td>Machine learning</td><td>16.6</td><td>36.2</td><td>48.9</td></tr><tr><td>Incl. dimensionality reduction</td><td>16.5</td><td>37.5</td><td>52.8</td></tr><tr><td rowspan="3">STOXX</td><td>Sentiment</td><td>20.3</td><td>20.6</td><td>29.3</td></tr><tr><td>Machine learning</td><td>19.7</td><td>22.7</td><td>29.1</td></tr><tr><td>Incl. dimensionality reduction</td><td>20.2</td><td>23.5</td><td>29.2</td></tr><tr><td></td><td></td><td colspan="3">Weekly resolution</td></tr><tr><td></td><td></td><td>h=1</td><td>h=52</td><td>h=104</td></tr><tr><td rowspan="3">DAX</td><td>Sentiment</td><td>12.2</td><td>29.9</td><td>49.5</td></tr><tr><td>Machine learning</td><td>12.2</td><td>32.2</td><td>48.1</td></tr><tr><td>Incl. dimensionality reduction</td><td>12.1</td><td>33.3</td><td>45.6</td></tr><tr><td rowspan="3">CDAX</td><td>Sentiment</td><td>12.0</td><td>29.7</td><td>51.5</td></tr><tr><td>Machine learning</td><td>12.0</td><td>33.1</td><td>51.1</td></tr><tr><td>Incl. dimensionality reduction</td><td>12.0</td><td>34.0</td><td>48.3</td></tr><tr><td rowspan="3">STOXX</td><td>Sentiment</td><td>9.8</td><td>19.3</td><td>27.9</td></tr><tr><td>Machine learning</td><td>9.8</td><td>20.3</td><td>27.1</td></tr><tr><td>Incl. dimensionality reduction</td><td>9.8</td><td>21.8</td><td>25.4</td></tr></table>

Table 5: Normalized RMSE for comparing the best-in-breed, text-based predictions.

We now briefly validate the robustness of our results; that is, how sensitive the proposed machine learning approach is to the individual model choice. For this purpose, we report a detailed performance breakdown by model in the supplements. Whenever the machine learning approach in the summary table is strong in outperforming the lag-based baseline, we find similar outcomes when looking in the full palette of models. To quantify this efect, we computed the coeficient-of-variation across all estimated models. For instance, in the case of the monthly DAX, the coeficient-of-variation for the benchmarks computes to 0.183 in the nowcasting scenario, while it is lowered to 0.782 when using machine learning together with dimensionality reduction. Similar patterns arise in the two-year scenario where it drops from 0.032 to 0.022.

## 6. Discussion

## 6.1. Business implications for financial decision-making and decision-support

The objective of this paper is to demonstrate the predictive power of approaches utilizing techniques from text mining in order to forecast stock indices. The predominant reason is that that trading recently witnessed a trends towards index ETFs. In this regard, the Financial Times suggests that the relative trend towards ETFs as a form of passive investing continues to grow.<sup>5</sup> Our quantitative results thus aid practitioners, professional investors and managers.

Based on our findings, one can build algorithmic trading systems around our text-based prediction methodology, which are capable of executing potentially profitable trading strategies [60, 22]. In this regard, text mining in particular has recently received great traction and is propelling the automated interpretation of the linguistic content in corporate disclosures [61]. As an immediate implication, our research contributes to the stream of text-based trading and suggests the use of corporate disclosures in predicting stock indices, especially for long-term forecasts. This development is largely sustained by the growing volume and ease of access to unstructured narrative materials, thereby fundamentally advancing the methods of researchers in the field of financial forecasting.

A potential advantage of forecasting based on financial disclosures is the possibility of detecting market movements that are too complex for humans to identify. Yet our work also reveals several challenges. Among these is the veracity of financial

# ACCEPTED MANUSCRIPT

news or, put diferently, the information quality associated with verbal expressions. While financial news appears to be a significant driver of stock valuation [46], there is still a large portion of unexplained variance. This noise component might be diminished by better forecasting techniques, although, a residual noise component might even be unpredictable, especially when signals are unclear or noisy [62].

From a mathematical point of view, our research setting is highly challenging because of the high-dimensional predictor matrix that can easily lead to overfitting. Here individual words are only weakly related the outcome variable and only their interplay accomplishes the desired prognostic power. As a remedy, our work lends to prescriptive guidelines for similar undertakings, as we compare diferent strategies for efective, text-based forecasting with wide data. This includes techniques for data-driven and knowledge-driven dimensionality reduction. We thereby contribute to the growing use of data mining techniques in financial forecasting [63].

## 6.2. Links to theory

The semi-strong form of the eficient market hypothesis stipulates changes in financial valuation once novel information enters the market [1]. This is the case when corporations disclose ad hoc announcements that subsequently drive a market response and thus trigger a direct change in the price variable. The corresponding forecasting performance draws purely upon novel information entering the market that consequently causes an adjustment of stock prices. Hence, the profits are not the result of arbitrage [64] and unlikely to diminish to zero-excess returns in the future.

Eficient markets “rule out the possibility of trading systems based only on (the assumed information set) that have expected profits or returns in excess of equilibrium profits or returns” [65, p. 385]. However, research has also found empirical evidence supporting the predictability of stock prices [66, 63, 40, 43]. A recent meta-study lists 97 variables for which previous research has found a prognostic capacity of cross-sectional stock returns [64]. These variables include, for instance, analyst recommendations, turnover volume, bid-ask spread, investment decisions and tax levels. Our research yields findings analogous to prior work at stock level that corporate disclosures have long-term prognostic capabilities at index level. In this context, our work identifies highly complex and non-linear relationships between word choice and the future outlook of the economy.

## 6.3. Limitations and potential for future research

We provide evidence that financial disclosures per se are linked to the economic outlook, but several aspects are left as potential avenues for future research. While this work demonstrates the prognostic capability of ad hoc announcements in English and German for a range of stock markets, the task remains to repeat our analysis in other markets, such as investigating the interplay between Form 8-K filings in the US and domestic stock indices. In our research design, the choice of regulatory disclosures entails several inherent advantages for financial forecasting, including their objectiveness, relevance to the market, concise format and short publication times. Nevertheless, one could also consider alternative text sources besides regulatory disclosures: for instance, social media, Internet stock message boards, newspaper releases or a combination thereof. Similarly, the analysis could be extended by including afective dimensions beyond sentiment or by analyzing the topic-specific reception. In addition, further efort is needed in order to obtain fully generative models and perform a rigorous model selection (for instance, see the test procedure in [67]).

## 7. Conclusions

In this paper, we draw upon the eficient market hypothesis, which dictates that share valuations adjust to new information entering the market. We join theory and text mining based on which we test the ability of language, published in regulatory disclosures, to improve both short- and long-term forecasts of stock market indices. Our experiments reveal that text-based models perform at comparable levels relative to the baseline predictions for short-term forecasts and can outperform these baselines in terms of particularly challenging long-term forecasts.

To test the forecasting potential of our language-based data source, we utilize 20 years’ worth of corporate disclosures mandated by German regulations. The individual disclosures are aggregated and processed into high-dimensional predictor matrices referring to the individual term frequencies. We then apply machine learning models, suited for high-dimensional problems, to forecast major German and European stock indices over multiple forecast horizons, up to 24 months ahead. We evaluate the forecasting errors of our text-based models against various benchmarks, including linear autogression and random forests, using lagged data as predictors. With regard to the long-term forecasts experiments, the text-based models are able predict with lower forecast errors than the baseline models.

## References

[1] F. E. Fama, The behavior of stock-market prices, Journal of Business 38 (1965) 34–105.

[2] F. Li, Textual analysis of corporate disclosures: A survey of the literature, Journal of Accounting Literature 29 (2010) 134–165.

[3] A. K. Nassirtoussi, S. Aghabozorgi, T. Y. Wah, D. C. L. Ngo, Text mining for market prediction: A systematic review, Expert Systems with Applications 41 (2014) 7653–7670.

[4] N. Pr¨ollochs, S. Feuerriegel, Business analytics for strategic management: Identifying and assessing corporate challenges via topic modeling, Information & Management (2018).

[5] I. E. Fisher, M. R. Garnsey, M. E. Hughes, Natural language processing in accounting, auditing and finance: A synthesis of the literature with a roadmap

for future research, Intelligent Systems in Accounting, Finance and Management 23 (2016) 157–214.

[6] C. Kearney, S. Liu, Textual sentiment in finance: A survey of methods and models, International Review of Financial Analysis 33 (2014) 171–185.

[7] T. Loughran, B. McDonald, Textual analysis in accounting and finance: A

[8] M. Kraus, S. Feuerriegel, Decision support from financial disclosures with deep neural networks and transfer learning, Decision Support Systems 104 (2017) 38–48.

[9] B. Wang, H. Huang, X. Wang, A novel text mining approach to financial time series forecasting, Neurocomputing 83 (2012) 136–145.

[10] M. Siering, J. Muntermann, The role of misbehavior in eficient financial markets: Implications for financial decision support, in: Lecture Notes in Business Information Processing, volume 135, Springer, Berlin, Heidelberg, 2013, pp. 42–58.

[11] A. Neuhierl, B. Schlusche, Data snooping and market-timing rule performance, Journal of Financial Econometrics 9 (2011) 550–587.

[12] H. White, A reality check for data snooping, Econometrica 68 (2000) 1097– 1126.

[13] K. Ravi, V. Ravi, A survey on opinion mining and sentiment analysis: Tasks, approaches and applications, Knowledge-Based Systems 89 (2015) 14–46.

[14] B. Pang, L. Lee, Opinion mining and sentiment analysis, Foundations and Trends in Information Retrieval 2 (2008) 1–135.

## ACCEPTED MANUSCRIPT

[15] E. J. de Fortuny, T. de Smedt, D. Martens, W. Daelemans, Evaluating and understanding text-based stock price prediction models, Information Processing & Management 50 (2014) 426–441.

[16] T. Geva, J. Zahavi, Empirical evaluation of an automated intraday stock recommendation system incorporating both market data and textual news, Decision Support Systems 57 (2014) 212–223.

[17] M. Hagenau, M. Liebmann, D. Neumann, Automated news reading: Stock price prediction based on financial news using context-capturing features, Decision Support Systems 55 (2013) 685–697.

[18] N. Pr¨ollochs, S. Feuerriegel, D. Neumann, Negation scope detection in sentiment analysis: Decision support for news-driven trading, Decision Support Systems 88 (2016) 67–75.

[19] R. P. Schumaker, Y. Zhang, C.-N. Huang, H. Chen, Evaluating sentiment in financial news articles, Decision Support Systems 53 (2012) 458–464.

[20] S. W. Chan, J. Franklin, A text-based decision support system for financial sequence prediction, Decision Support Systems 52 (2011) 189–198.

[21] C.-S. Ho, P. Damien, B. Gu, P. Konana, The time-varying nature of social media sentiments in modeling stock returns, Decision Support Systems 101 (2017) 69–81.

[22] S. Feuerriegel, H. Prendinger, News-based trading strategies, Decision Support Systems 90 (2016) 65–74.

[23] S. S. Groth, J. Muntermann, An intraday market risk management approach based on textual analysis, Decision Support Systems 50 (2011) 680–691.

[24] Z. Li, W. Xu, L. Zhang, R. Y. Lau, An ontology-based web mining method for unemployment rate prediction, Decision Support Systems 66 (2014) 114–122.

[25] M. Eickhof, J. Muntermann, Stock analysts vs. the crowd: Mutual prediction and the drivers of crowd wisdom, Information & Management 53 (2016) 835– 845.

[26] S. Feuerriegel, J. Gordon, News-based forecasts of macroeconomic indicators: A semantic path model for interpretable predictions, European Journal of Operational Research (2018).

[27] N. Pr¨ollochs, S. Feuerriegel, Investor reaction to financial disclosures across topics: An application of latent Dirichlet allocation, arXiv (2018).

[28] S. Deng, A. P. Sinha, H. Zhao, Adapting sentiment lexicons to domain-specific social media texts, Decision Support Systems 94 (2017) 65–76.

[29] Y.-M. Li, T.-Y. Li, Deriving market intelligence from microblogs, Decision Support Systems 55 (2013) 206–217.

[30] J. Bollen, H. Mao, X. Zeng, Twitter mood predicts the stock market, Journal of Computational Science 2 (2011) 1–8.

[31] B. W¨uthrich, D. Permunetilleke, S. Leung, W. Lam, V. Cho, J. Zhang, Daily prediction of major stock indices from textual WWW data, HKIE Transactions 5 (1998) 151–156.

[32] S. Zubair, K. J. Cios, Extracting news sentiment and establishing its relationship with the S&P 500 index, in: Hawaii International Conference on System Sciences, IEEE, 2015, pp. 969–975. doi:10.1109/HICSS.2015.120.

[33] M. Siering, Investigating the impact of media sentiment and investor attention on financial markets, in: Lecture Notes in Business Information Processing, volume 135, Springer, Berlin, Heidelberg, 2013, pp. 3–19.

[34] M. Hagenau, M. Hauser, M. Liebmann, D. Neumann, Reading all the news at the same time: Predicting mid-term stock price developments based on news

momentum, in: 46th Hawaii International Conference on System Sciences (HICSS), 2013, pp. 1279–1288.

[35] M. T. Leung, H. Daouk, A.-S. Chen, Forecasting stock indices: A comparison of classification and level estimation models, International Journal of Forecasting 16 (2000) 173–190.

[36] M. M. Rounaghi, F. Nassir Zadeh, Investigation of market eficiency and financial stability between S&P 500 and London Stock Exchange: Monthly and yearly forecasting of time series stock returns using ARMA model, Physica A: Statistical Mechanics and its Applications 456 (2016) 10–21.

[37] P.-F. Pai, C.-S. Lin, A hybrid ARIMA and support vector machines model in stock price forecasting, Omega 33 (2005) 497–505.

[38] J.-J. Wang, J.-Z. Wang, Z.-G. Zhang, S.-P. Guo, Stock index forecasting based on a hybrid model, Omega 40 (2012) 758–766.

[39] W. Huang, Y. Nakamori, S.-Y. Wang, Forecasting stock market movement direction with support vector machine, Computers & Operations Research 32 (2005) 2513–2522.

[40] A. Oztekin, R. Kizilaslan, S. Freund, A. Iseri, A data analytic approach to forecasting daily stock returns in an emerging market, European Journal of Operational Research 253 (2016) 697–710.

[41] H. Herwartz, Stock return prediction under GARCH: An empirical assessment, International Journal of Forecasting 33 (2017) 569–580.

[42] G. S. Atsalakis, K. P. Valavanis, Surveying stock market forecasting techniques (part II): Soft computing methods, Expert Systems with Applications 36 (2009) 5932–5941.

[43] A. Timmermann, C. W. Granger, Eficient market hypothesis and forecasting, International Journal of Forecasting 20 (2004) 15–27.

[44] N. Pr¨ollochs, S. Feuerriegel, D. Neumann, Generating domain-specific dictionaries using bayesian learning, in: 23rd European Conference on Information Systems (ECIS), 2015.

[45] P. C. Tetlock, Giving content to investor sentiment: The role of media in the stock market, Journal of Finance 62 (2007) 1139–1168.

[46] P. C. Tetlock, M. Saar-Tsechansky, S. Macskassy, More than words: Quantifying language to measure firms’ fundamentals, Journal of Finance 63 (2008) 1437–1467.

[47] C. D. Manning, H. Sch¨utze, Foundations of Statistical Natural Language Processing, MIT Press, Cambridge, MA, 1999.

[48] T. J. Hastie, R. J. Tibshirani, J. H. Friedman, The Elements of Statistical Learning: Data Mining, Inference, and Prediction, Springer Series in Statistics, 2nd ed., Springer, New York, NY, 2013.

[49] R. J. Hyndman, G. Athanasopoulos, Forecasting: Principles and Practice, OTexts, Heathmont, 2014.

[50] M. Kuhn, Building predictive models in R using the caret package, Journal of Statistical Software 28 (2008) 1–26.

[51] S. S. Groth, M. Siering, P. Gomber, How to enable automated trading engines to cope with news-related liquidity shocks? Extracting signals from unstructured data, Decision Support Systems 62 (2014) 32–42.

[52] R. B. Litterman, Forecasting with Bayesian vector autoregressions: Five years of experience, Journal of Business & Economic Statistics 4 (1986) 25–38.

[53] J. H. Stock, M. W. Watson, Macroeconomic forecasting using difusion indexes, Journal of Business & Economic Statistics 20 (2002) 147–162.

[54] R. Giacomini, B. Rossi, Forecasting in macroeconomics, in: Handbook of Research Methods and Applications on Empirical Macroeconomics, EE, Northhampton, MA, 2013.

[55] F. X. Diebold, R. S. Mariano, Comparing predictive accuracy, Journal of Business & Economic Statistics 13 (1995) 253–263.

[56] F. X. Diebold, Comparing predictive accuracy, twenty years later: A personal perspective on the use and abuse of Diebold–Mariano tests, Journal of Business & Economic Statistics 33 (2015) 1.

[57] A. Oztekin, D. Delen, A. Turkyilmaz, S. Zaim, A machine learning-based usability evaluation method for eLearning systems, Decision Support Systems 56 (2013) 63–73.

[58] A. Dag, A. Oztekin, A. Yucel, S. Bulur, F. M. Megahed, Predicting heart transplantation outcomes through data analytics, Decision Support Systems 94 (2017) 42–52.

[59] D. Delen, A. Oztekin, L. Tomak, An analytic approach to better understanding and management of coronary surgeries, Decision Support Systems 52 (2012) 698–705.

[60] S. Gagnon, Rules-based integration of news-trading algorithms, Journal of Trading 8 (2013) 15–27.

[61] A. Groß-Klußmann, N. Hautsch, When machines read the news: Using automated text analytics to quantify high frequency news-implied market reactions, Journal of Empirical Finance 18 (2011) 321–340.

[62] P. C. Tetlock, Does public financial news resolve asymmetric information?, Review of Financial Studies 23 (2010) 3520–3557.

[63] Y. Hu, K. Liu, X. Zhang, L. Su, E. Ngai, M. Liu, Application of evolutionary computation for rule discovery in stock algorithmic trading: A literature review, Applied Soft Computing 36 (2015) 534–551.

[64] R. D. McLean, J. Pontif, Does academic research destroy stock return predictability?, Journal of Finance 71 (2016) 5–32.

[65] E. F. Fama, Eficient capital markets: A review of theory and empirical work, Journal of Finance 25 (1970) 383–417.

[66] C. W. Granger, Forecasting stock market prices: Lessons for forecasters, International Journal of Forecasting 8 (1992) 3–13.

[67] R. Giacomini, H. White, Tests of conditional predictive ability, Econometrica 74 (2006) 1545–1578.

Biography

![](/api/attachments/NVKBWE66/fulltext/images/8eb856fd213f4780f73ccb5e6ea3a7d4bc05933261ba9b30fcf32a7e6071c98f.jpg)

Stefan Feuerriegel is an assistant professor for management information systems at ETH Zurich. His research focuses on cognitive information systems and business intelligence, including text mining and sentiment analysis of financial news. Previously, he obtained his Ph.D. from the University of Freiburg where also worked as a research group leader at the Chair for Information Systems Research. He has coauthored research publications in the European Journal of Operational Research, the European Journal of Information Systems, the Journal of Information Technology and Decision Support Systems.

![](/api/attachments/NVKBWE66/fulltext/images/cc649a23bd4a8a848393451ecf81f88570c75037a066cf1a43b8ea11ab91c8c2.jpg)

Julius Gordon is a post-graduate research fellow with the Chair of Information Systems Research of the University of Freiburg. Previously, he has completed his Master’s studies at the same institution. He holds a bachelor of economics and a bachelor of commerce from the Australian National University in Canberra. His research interests include sports analytics, text mining and decision support systems.

## Highlights

 Financial news entail a prognostic capacity of stock market movements

 We propose text mining for long-term predictions of stock indices

 We reveal that financial disclosure have a high predictive power in the long run

 It outperforms common benchmarks based on time series methodology

![](/api/attachments/NVKBWE66/fulltext/images/1eb2924639b9ffc2798b0aa0128433d3a8e258dfff3e18c2a2e147d02cd78913.jpg)  
Figure 1

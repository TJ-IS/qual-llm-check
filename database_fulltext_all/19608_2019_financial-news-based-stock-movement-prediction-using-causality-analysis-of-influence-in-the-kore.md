---
otero_id: 19608
otero_key: "FZ843XHA"
title: "Financial news-based stock movement prediction using causality analysis of influence in the Korean stock market"
authors: "KiHwan Nam; NohYoon Seong"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.11.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
<table><tr><td>PII:</td><td>S0167-9236(18)30195-7</td></tr><tr><td>DOI:</td><td>https://doi.org/10.1016/j.dss.2018.11.004</td></tr><tr><td>Reference:</td><td>DECSUP 13012</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>29 April 2018</td></tr><tr><td>Revised date:</td><td>4 November 2018</td></tr><tr><td>Accepted date:</td><td>25 November 2018</td></tr></table>

## Accepted Manuscript

Financial news-based stock movement prediction using causality analysis of influence in the Korean stock market

ELSEVIER Decision Support Systems

![](/api/attachments/FZ843XHA/fulltext/images/2d603be609ce5b0dd53a4592420a8002307cead318cb02b68e4a30e20604d71d.jpg)

KiHwan Nam, NohYoon Seong

Please cite this article as: KiHwan Nam, NohYoon Seong , Financial news-based stock movement prediction using causality analysis of influence in the Korean stock market. Decsup (2018), https://doi.org/10.1016/j.dss.2018.11.004

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Financial News-based Stock Movement Prediction Using Causality Analysis of Influence in the Korean stock market

KiHwan Nam<sup>a</sup> and NohYoon Seong <sup>b</sup>\*

<sup>a</sup> College of Business Management Engineering Department, KAIST, Seoul, Korea

<sup>b</sup> College of Business Management Engineering Department, KAIST, Seoul, Korea Phone: +82-10-4542-4525 E-mail: nyseong@kaist.ac.kr \*corresponding author

Mobile: +82-10-4542-4525

# Financial News-based Stock Movement Prediction Using Causality Analysis of Influence in the Korean stock market

## Abstract

With the advent of the Big Data era and the development of machine learning technologies, predicting stock movements by analyzing news articles, which are unstructured data, has been studied actively. However, so far no attempts have been made to utilize the asymmetric relationship of firms. Thus far, most papers focus on only the target firm, and few papers focus on the target firm and relevant firms together. In this article, we propose a novel machine learning model to forecast stock price movement based on the financial news considering causality. Specifically, our method analyzes the causal relationship between companies, and it accounts for the directional impact within the Global Industry Classification Standard sectors. In our proposed method, transfer entropy is used to find causality, and multiple kernel learning is used to combine features of target firm and causal firms. Based on a Korean based framework outperforms two traditional state-of-the-art algorithms. Furthermore, the experimental results show that the proposed method can predict the stock price directional movements even when there is no financial news on the target firm, but financial news is published on causal firms. Our findings reveal that identifying causal relationship is important in prediction problems, and we suggest that it is important to develop machine learning algorithms and it is also important to find connections with wellestablished theories such as the complex system theory.

Keywords: Stock movement prediction; Transfer Entropy; Causal relationship; Multiple kernel learning; Text mining

# Financial News-based Stock Movement Prediction Using Causality Analysis of Influence in the Korean stock market

## 1. Introduction

The price of a stock increases and decreases in response to the dealings of the sellers and buyers in the market to reach a reasonable price. Thus, stock prices are determined by the law of supply and demand [1]. The stock price demand will increase if investors believe that the company performs well; in contrast, if investors think that the company does not perform well, the supply will increase. In other words, theoretically, the stock price is a measure of the company's future performance. However, many factors can affect the expected value of a company's future performance. In the academic literature, there are various theories that are related to stock prices. The most representative theory is the Efficient Market Hypothesis (EMH) [2]. The EMH states that the price of the market reflects the value accurately and responds only to new information which consists of historical prices, public information and private information. EMH is divided into three categories according to how much information is reflected:

I. Weak-form efficient market. In a weak-form efficient market, the historical prices of all financial assets, such as stocks, bonds, and tangible assets that can be traded in the current market are already reflected in the current stock price through all available historical information. Analysis using historical prices cannot yield excess returns so that one needs to predict the stock price with public information and private information.

II. Semi-strong-form efficient market. In a semi-strong-form efficient market, all past public information, such as the past stock price, disclosures, and news, is already reflected in the financial assets, and forecasting using historical prices and public information cannot generate

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

excess returns in the market. So one needs to predict the stock price with private information.

III. Strong-form efficient market. In a strong-form efficient market, non-public information, as well as past prices and public information, is reflected in market prices. Thus, forecasting using all information cannot yield excess returns in the market.

Since a majority of the mature stock markets, like those in the U.S.A, Korea, U.K., and France, are weak-form efficient markets [3], many studies have been conducted on predicting stock prices using financial news. To quantitatively measure market states, various measurement methods have been applied. One method, the Hurst Exponent, is a concept used in econophysics to measure market states [3]. The Hurst Exponent measures long-term memory quantitatively [4]. If the Hurst Exponent is less than 0.5, stock prices can be interpreted as mean-reverting. If it equals 0.5, it means that stock prices follow a random walk, and if it is greater than 0.5, stock prices can be interpreted as following a trend. In other words, the larger the Hurst Exponent, the greater the effect of past prices on current prices. If the Hurst Exponent is high, the stock market is not a weak-form efficient market because it can be predicted with historical prices. According to Eom et al. [3], the Korean stock market has a Hurst Exponent of approximately 0.5 so that the Korean stock market is the weak-form efficient market. Therefore, when predicting stock prices in the Korean market, it is meaningful to use public information for analysis, such as financial news, rather than historical prices.

In research on stock price forecasting through financial news, it is common to build a keyword dictionary for each company. This dictionary provides keywords that influence the fluctuations of stocks of individual companies, and they should be used to predict future stock prices. Recently, studies on identifying relevant firms [5], and studies on reflecting the effects of relevant firms based on the Global Industry Classification Standard (GICS) sector [6, 7] emerge. Especially, Shynkevich et al. [7] constructed an individual firm dictionary, sub-industry dictionary, industry dictionary, group industry dictionary, and sector dictionary in the S & P 500 healthcare sector and predicted stock movements with

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

the combination of them. The results of this study are as follows: The prediction accuracy of integrating them is higher than that of news of individual firms only. In other words, the dictionaries that include higher-level concepts, e.g. sector dictionaries, reflect information that affects industry characteristics or industries that are not covered by the concepts of the subordinate individual firms.

Although research has progressed gradually on the basis of the influence within the GICS sector, it has been conducted based on the assumption that every firm influences other firms, and the influence between firms is bidirectional. However, companies in the same GICS sector may not influence each other, and there is a structure in which a company affects other companies but not inversely [8]. In this study, we overcome the limitations of the existing research by applying the transfer entropy technique, which has been actively studied in the complex system theory. We find the causal relationships of the firms within the GICS sectors and predict the stock price based on causal relationships. Especially, we integrate the effect of the target firm and the effects of the causal firms by employing Multiple Kernel Learning method [9].

The results show that our approach improves the prediction performance in comparison with approaches that are based on news on target firms [10] and on the GICS Sector-based integration approach [7], which are two state-of-the-art algorithms. Furthermore, the experimental results show that the proposed method can predict the stock price directional movements even when there is no financial news on the target firm, but financial news is published on causal firms. In addition, we find that the results change by setting the statistical significance of transfer entropy. Therefore, it is important to set the threshold of statistical significance through a grid search.

In this study, we make three main contributions: First, in solving socioeconomic problems, we were able to achieve higher performance by successfully combining physics theory with machine learning. To the best of our knowledge, this paper is the first paper to combine complex system methodology with machine learning. Second, previous studies have predicted stock prices at the

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

individual level and searched for relevant companies to consider their impact. This study is the first to predict stock prices while considering the causality between the companies. Finally, existing studies were able to predict stock movements only when the news on the company was released. In this paper, we propose a method for predicting stock movements with a causal relationship through causality detection, even when no news is published directly.

We organize the remainder of this paper as follows: Section 2 provides an overview of the relevant literature on complex networks and text mining. Section 3 describes news and stock datasets, transfer entropy analysis, text pre-processing techniques, machine learning approaches and evaluation metrics. Section 4 describes the experimental results. Section 5 presents the study’s conclusions and outlines directions for future work.

## 2. Literature Review and Hypothesis Development

As text mining techniques are gradually evolving, research on predicting the stock prices of companies using the textual data of company-related financial news articles, company disclosures, and social network service (SNSs) is increasing. Research has been in full swing since the 1990s [11] and has been more active since 2000, especially with the advancement of machine learning. This chapter summarizes the existing studies in the flow of research on predicting stock prices with financial news articles.

## 2.1 Key related research

Text analysis procedures are broadly divided into (1) text preparation, (2) text mining, and (3) model learning and prediction [10].

(1) The text preparation stage refers to the collection of textual data that are related to the finances of a company through various methods, such as online news crawling. (2) The text mining step is the generation of stock impact features through text mining techniques. The text mining step consists of feature extraction, feature selection, and feature representation. Finally, (3) in the model learning and

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

prediction stage, we predict stock price movements with machine learning on the generated stock impact features. The model learning and prediction stage consists of machine learning algorithms, forecast type, and combining them with other effects. Each step is summarized in Table 1.

Table 1 Key Related Research

<table><tr><td></td><td>(1) Preparation</td><td colspan="3">(2) Text Mining</td><td colspan="3">(3) Model Learning and Forecasting</td></tr><tr><td></td><td>Data Type</td><td>Feature Extraction</td><td>Feature Selection</td><td>Feature Representation</td><td></td><td></td><td>Other Effects</td></tr><tr><td></td><td>Corporate announcement and financial news</td><td>Bag-of-words2-Gramn Nounphrases</td><td>News frequencyareBinormal-separation</td><td>TF-IDF</td><td></td><td></td><td>-</td></tr><tr><td></td><td>Financial news</td><td>Bag-of-wordsNoun phrasesNamed entitiesProper Nouns</td><td>Minimum occurrence period document</td><td>Binary</td><td></td><td></td><td>Relevant firms, financial news based on G</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>ICS</td></tr><tr><td></td><td>Financial News</td><td>Bag-of-words</td><td>Chi-square</td><td>TF-IDF</td><td>Multiple kernel learning</td><td>Up and down</td><td>Relevant firms' financial news based on GICS</td></tr><tr><td></td><td>Web news and financialdiscussionboard</td><td>NounphrasesSentimente ms</td><td>-</td><td>Modified TF-IDF</td><td></td><td></td><td>-</td></tr><tr><td></td><td>Germanad-hocannouncements</td><td>Bag-of-words</td><td>Chi-square InformationGain</td><td>TF-IDF</td><td>SVM</td><td>Market risk</td><td>-</td></tr><tr><td></td><td>Financial News</td><td>Bag-of-words</td><td>Chi-square</td><td>TF-IDF</td><td></td><td></td><td>Causal firms,financial news based on GICS</td></tr></table>

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

Hagenau et al. [10] designed a procedure that receives corporate announcements and financial news automatically, that implements feature engineering, and that uses machine learning techniques to forecast stock prices. The authors implemented many feature extraction methods and compared Bag-of words, Noun phrases, and 2-Gram and 2-word combinations. In addition, the authors implemented two feature selection methods and compared chi-square feature selection and bi-normal-separation feature selection. High accuracy rates were obtained as a result. In this paper, we use the Chi-square feature selection and TF-IDF weighting for the Bag-of-words model, as used in Hagenau et al. [10].

Schumaker and Chen [6] suggested the Arizona Financial Text System (AZFinText). AZFinText constructs a textual dataset (i.e., financial news, trading experts and stock quotes) and predicts stock prices. In addition, the authors divided the financial news that affects the stock prices into several groups of datasets: sector-based, sub-industry-based, industry-based, group-based, and stock-specific news, based on the GICS (Global Industry Classification Standard), which is an industry taxonomy that was developed by MSCI and S&P. The authors predicted the stock prices with each dataset of news articles. Stockspecific news affected the prediction of the stock price, just like the previous studies. Surprisingly, the sector-based news was also effective in predicting stock prices. However, there is a limitation that various levels of datasets were not applied simultaneously. Therefore, in this paper, multiple kernel learning is used to integrate various levels of features simultaneously.

By assimilating news groups of various levels of relevance, Shynkevich et al. [7] built a system for estimating stock movements. The groups that the authors created are as follows: sector-based, subindustry-based, industry-based, group-based, and stock-specific news as in [6]. The authors considered and compared them by utilizing multiple kernel learning with all of the companies. The authors found that forecasting the stock price while taking into account the significance of various levels yields better results than anticipating the stock price alone. However, regardless of whether they are in the same industry, the relevance will not be high [5]. Even if the relevance between firms is high, they do not share the same effect but have an asymmetric influence. Therefore, we utilize an information theory approach, as opposed to utilizing only the GICS system, to determine the causality between firms.

![](/api/attachments/FZ843XHA/fulltext/images/07c7eb3fa5ee06d1949dbf729deedb65b27f438ee251f07864014426c0995d23.jpg)  
Fig. 1. Concept of stock price prediction through news

Fig. 1 shows a general concept of stock price forecasting through online news. In terms of the media effect analysis, online news includes the overall situation of a company, such as the financial situation and economic activities [1]. News on the same information differs substantially according to investor psychology. According to research in behavioral finance and investment psychology, investor behavior can be determined by whether investors feel optimistic or pessimistic about the future market value [12, 14]. In addition, investor sentiment can impact the individual firms and the industrial sector. Combining and analyzing these sectors of industry improves the performance of stock forecasting [6, 7]

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

In other words, stock price forecasting is analyzed based on individual corporate media effect, and the industry-level media effect. Previous studies on media effects have analyzed the influence based on the assumption that every firm in the same industry affects each other, and that magnitude of impacts are all the same. However, these studies have several limitations. Companies have structures that exchange asymmetric influences, but these factors were not considered in the existing methods. Therefore, in this study, we propose a methodology for predicting stock prices based on a more explicative a nd effective analysis by analyzing the causal relationships among these influences.

## 2.2 Transfer Entropy

In this paper, when predicting stock prices, the aim is to grasp only the factors that affect companies in the same group based on information theory and to predict the stock price by only considering the causal effect. We must check the causality between companies to determine who affects whom. In this paper, we use transfer entropy, which quantitatively measures the asymmetric information flow and is mainly used to measure the causality in complex systems [8, 15-19].

## 2.2.1 Transfer Entropy (TE)

TE is a concept that was developed by Schreiber [20] and designed to measure the flow of information asymmetrically between two systems in a complex system. When there are two processes I and J, Entropy is defined as (1) [21].

$$
\mathrm{H} (\mathrm{I}) = - \sum p _ {I} (i) l o g p _ {I} (i)\tag{1}
$$

Entropy is a measure of the average uncertainty. In other words, entropy is the average amount of information that is needed to predict a process. In the same vein, joint entropy and conditional entropy are defined as follows:

$$
\begin{array}{r l} & {\mathrm{H(I,J)} = - \sum \sum p _ {I J} (i, j) l o g p _ {I J} (i, j)} \\ & {\mathrm{H(I|J)} = - \sum \sum p _ {I J} (i, j) l o g p _ {I | J} (i | j)} \end{array}\tag{2}
$$

(3)

The mutual information that is shared by two processes is defined as follows [20, 22]:

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

$$
\mathrm{M} (\mathrm{I}, \mathrm{J}) = H (I) + H (J) - H (I, J)\tag{4}
$$

$$
\mathrm{M} (\mathrm{I}, \mathrm{J}) = \sum p _ {I J} (i, j) l o g \frac {p (i , j)}{p _ {I} (i) p _ {J} (j)}\tag{5}
$$

Since transfer entropy involves directional mutual information, TE for k sample processes of I and l sample processes of J is defined as follows [20]:

$$
\mathrm{TE} _ {J \rightarrow I} \stackrel {\mathrm{def}} {=} \sum p \big (i _ {t + 1}, i _ {t} ^ {k}, j _ {t} ^ {l} \big) l o g \frac {p (i _ {t + 1} | i _ {t} ^ {k} , j _ {t} ^ {l})}{p (i _ {t + 1} | i _ {t} ^ {k})}\tag{6}
$$

where $\mathrm { i } _ { \mathrm { t } }$ and $j _ { t }$ denote data points at time t of I and J processes, and   and  are k-dimensional and ldimensional delay vectors that are one-dimensional delay vectors of sequences I and J, respectively. In addition, $p \big ( i _ { t + 1 } , i _ { t } ^ { k } , j _ { t } ^ { l } \big )$ is the joint probability of $i _ { t + 1 } , i _ { t } ^ { k }$ and $j _ { t } ^ { l } .$ . TE is mainly estimated through the KSG Estimator [23, 24].

![](/api/attachments/FZ843XHA/fulltext/images/fef137b5131413416165e1db7477819b151c603f5a55ac32aabc759752c40478.jpg)  
Fig. 2. Conceptual representation of Transfer Entropy [19]

process J measures the transition probability of process I and vice versa because of the differences between the joint probability and the conditional probability. In other words, TE provides information about the direction of interaction between two systems [19], which can be expressed as shown in Fig. 2.

## 2.2.2 Statistical Significance: p-value

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

Theoretically, TE between two processes without information flow should be zero. However, there are nonzero cases because the empirically measured TE at a finite number of data points has a bias [21]. Therefore, it is necessary to know how statistically significant the TE is. .

Permutation testing is mainly used to measure the confidence intervals of transfer entropy and statistical significance [17, 21, 24]. In this paper, we measure the p-value as statistical significance. To

$\mathrm { H } _ { 0 }$ : There is no directed relationship from J to $I ; T E _ { J  I } = 0$

(7)

In addition, we need to know the distribution of the TE measurements. To obtain the distribution of TE, we can identify a surrogate process $\mathsf { p } ^ { s }$ that satisfies $\mathrm { p } ^ { s } \bigl ( \mathrm { i } _ { \mathrm { t } } \bigl | \mathrm { i } _ { \mathrm { t } - 1 } ^ { \mathrm { k } } \bigr ) = \mathrm { p } ( \mathrm { i } _ { \mathrm { t } } | \mathrm { i } _ { \mathrm { t } - 1 } ^ { \mathrm { k } } , \mathrm { j } _ { \mathrm { t } - 1 } ^ { \mathrm { l } } )$ by sub-sampling. Superscript s denotes a surrogate process. In other words, a surrogate process of $\mathrm { J } , J ^ { s }$ , has the same statistical properties as J but should not have a direct relationship with I [17, 21]. Transfer Entropy is asymptotically distributed as follows [21, 25], where dJ and dI are the dimensionalities of processes J and I:

$$
\mathrm{TE} _ {J ^ {s} \rightarrow I} \sim \frac {\aleph^ {2}}{2 N} (i n n a t s), d e g r e e o f f r e e d o m = l d J d I\tag{8}
$$

Following (8), we can determine the statistical significance of the transfer entropy that is obtained by null hypothesis testing and we can obtain the p-value.

## 2.2.3 Causality Detection of Transfer Entropy

Generally, causality refers to a 'cause-effect relationship.' When something causes a problem and something occurs as a result, it is popular to say that the cause has causality in the result. However, it is very difficult to precisely define the concept of causality [26]. The concept of causality was first quantitatively defined by Wiener [27]. According to the definition of Wiener [27], when there are two signals X and Y that are measured at the same time, when estimating Y using X, we say that X causes Y if it can predict better than Y alone. In this paper, causality is based on the Granger definition [28].

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

The causality detection with Wiener-Granger Causality is used in stock market. Výrost et al. [29] examined return spillovers among stock indices by constructing Granger causality financial network. However, since Wiener-Granger Causality is not appropriate for finding causal relationships in nonlinear systems [26, 30], it has limitations in cases of collective behavior, such as stock herding behavior [31], and complex systems with a critical point [32]. To overcome these limitations, a nonlinear extension that is based on the information-theoretic formulation is often used for causality detection [21]. The representative extension is transfer entropy [8, 15-18].

Transfer entropy quantitatively measures the asymmetric information flow within a complex system. In particular, causality detection using transfer entropy is also widely used in financial markets. In Marschinski and Kantz [16], the relationship between the US Dow Jones Industrial Average (DJIA) and the German DAX Xetra Stock Index (DAX) was measured using transfer entropy. They calculated the effective transfer entropy by shuffling the time series to remove the random effects and found that the effect of DAX on DJIA was approximately three times greater than that of DJIA on DAX. However, they only compared the effects of the stock indices and did not confirmed that the values are statistically significant. Therefore, we analyze the transfer entropy considering the statistical significance.

Kwon and Yang [18] conducted transfer entropy analysis using the daily data of 25 market indices in the global financial market. Through the analysis, they found that the US stock market has the greatest impact on the global stock market and confirmed that the market that receives the most information is the Asia/Pacific market. Sensoy et al. [34] investigated the strength and direction of nonlinear causality between exchange rates and stock prices with effective transfer entropy and compared the changes between analysis before the 2008 crisis and analysis after the 2008 crisis. However, Kwon and Yang [18] and Sensoy et al. [34] had the limitation that they only showed relationships in aggregate level, where relationships can vary by GICS sectors or companies.

Kwon and Oh [8] measured information flow using transfer entropy between a market index and individual stocks in several markets around the world. The authors show that the information from the

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

index to the individual stock is higher than the information from the individual stock to the index. This finding implies that the market index affects the future prices of individual stocks. However, the market index is simply a sum of various stocks and not all of them affect a particular stock. Therefore, in this paper, we calculate transfer entropy at the individual stock level rather than at the market index level, determine which stock price affects each stock price, and use transfer entropy to measure the causality at the company level in a complex system, namely, the financial market.

Oh et al. [33] measured an information flow among industry sectors and compared them for three periods: before, during, and after the subprime crisis. They measured the degree of asymmetric information inflow, which is the difference between transfer entropy from X->Y and transfer entropy from Y->X. However, authors assumed that causality exists in only one way, where ‘X’ causes ‘Y’ and ‘Y’ causes ‘X’ simultaneously. This is inappropriate for prediction so that we consider simultaneous causality.

The existing papers constructed financial networks using causality detection. However, all of these studies were limited to only assessing the nonlinear causal relationship and building a financial network, and they did not predict the actual movement of stocks. To fill the research gap, we suggest a novel method that predicts stock movements with a machine learning technique based on causality detection. We calculate nonlinear causality, which is a similar approach in [8]. And we select the financial news that has influence based on nonlinear causality and predict stock movement with machine learning. As far as we know, this is the first paper that implements a stock prediction system based on nonlinear causal relationships.

## ACCEPTED MANUSCRIPT

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

Table 2 Summary of key papers on causality detection in stock market

<table><tr><td rowspan="2">Reference</td><td rowspan="2">Methodology</td><td rowspan="2">Summary</td><td rowspan="2">Limitation</td><td colspan="2">Dataset</td></tr><tr><td>Causality Detection</td><td>Prediction</td></tr><tr><td>Výrost et al. [29]</td><td>Granger Causality</td><td>Examines return spillovers among stock indices.</td><td>Inappropriate for nonlinear complex system.Only accounts for the aggregate level impact.</td><td>Stock index price</td><td>No</td></tr><tr><td>Marschinski and Kantz [16]</td><td>Transfer Entropy</td><td>Measures the information flow between the Dow Jones and DAX stock index.</td><td>Does not test statistical significance.</td><td>Stock index price</td><td>No</td></tr><tr><td>Kwon and Yang [18]</td><td>Transfer Entropy</td><td>Observes the strength and direction of information flow between stock indices.</td><td>Only for stock indices.Does not find the individual level causality.</td><td>Stock index price</td><td>No</td></tr><tr><td>Sensoy et al. [34]</td><td>Transfer Entropy</td><td>Examines the strength and direction of nonlinear causality between</td><td>Only accounts for the aggregate level impact.</td><td>Stock index price and exchange rates</td><td>No</td></tr></table>

## ACCEPTED MANUSCRIPT

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

<table><tr><td></td><td></td><td>exchange rates and stock markets.</td><td></td><td></td><td></td></tr><tr><td>Kwon and Oh [8]</td><td>Transfer Entropy</td><td>Observes asymmetric information flow between the stock market index and their component stocks.</td><td>Does not find the causal relationship between component stocks.</td><td>Stock index price and individual stock prices</td><td>No</td></tr><tr><td>Oh et al. [33]</td><td>Transfer Entropy</td><td>Measures asymmetric information flow between the GICS sectors.</td><td>Does not test statistical significance.</td><td>Sector level stock prices</td><td>No</td></tr><tr><td>The proposed Approach</td><td>Transfer Entropy</td><td>Finds causal relationships between the companies in the same GICS sector, and predicts stock movements with machine learning.</td><td>Does not account for impact across GICS sectors.</td><td>Individual stock prices</td><td>Financial News</td></tr></table>

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

## 2.3 Text pre-processing

Text pre-processing is the process of finding features that can be used for machine learning from unstructured textual data. There are many studies on using textual data to determine its effect on stock prices. Bollen and Mao [14] showed that the public mood on Twitter can be used to predict the stock price using sentiment analysis. However, Li et al. [12] found that a new set of keywords that consists of words that specifically affect the stock price is needed to ensure that the effect is not simply a sentiment analysis. In addition, it is necessary to consider firm-specific words for each company since the keywords that affect each company are different. Therefore, research on corporate-specific news rather than general news has been actively pursued, and this has been gradually increasing with the increase of computing capacity [35]. In this paper, context-aware text mining based on the company-specific financial news is applied.

The text-mining stage can be divided into three steps: feature extraction, feature selection, and feature representation [13].

Feature extraction starts from unstructured textual data and builds features that are expected to be informative, thereby simplifying the subsequent steps. In previous literature, 2-gram [10], noun phrases [6], sentiment words [12], topic modeling [36] and Bag-of-words [7, 13] have been used. The most popular and basic approach is Bag-of-words in the field of stock prediction with financial news [1]. Therefore, we used Bag-of-words for feature extraction in this paper.

The subsequent step is feature selection. Feature selection is the selection of a subset of relevant features for simplification and avoiding the curse of dimensionality. Feature selection based on predefined dictionaries has been used [37]. However, there is a disadvantage that it is difficult to generalize because the set of words changes with time. Therefore, methods of feature selection in that are based on statistical methods are that affect the stock movement mainly used. These methods are Minimum occurrence per document [6], Information Gain [13] and Chi-square [7, 10]. Among these methods, Chi-

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

square analysis is chosen for this paper, as it performed well in other studies [10] and Chi-square methods are structurally different in that it reflects the external market feedback [10].

The final step is feature representation. Feature representation is a step that represents every feature by a numeric value so that it can be input into machine learning algorithms. The most basic is a binary representation that indicates the absence or presence of a feature. However, this method has limitations in that it does not reflect the frequency of the word even though it is important. In this paper, Term Frequency-Inverse Document Frequency (TF-IDF) is used to overcome this limitation, as in Hagenau et al. [10] and Shynkevich et al. [7].

## 2.4 Machine Learning Prediction Techniques

In the model learning and prediction phase, various machine learning algorithms are used. For example, Support Vector Machine (SVM) [6, 10, 35], Naïve Bayes [38], Nearest Neighbor [11] and Neural Network [39] have been widely used. Among them, SVM showed especially outstanding performance [13].

Since SVM is based on a single kernel, there is a disadvantage in that it can only use a single data source. To use an ensemble technique that combines and predicts data from various sources, Multiple Kernel Learning (MKL) has been widely used recently. MKL can be used to learn various functions by combining several kernels. Yeh et al. [38] developed MKL for solving the Support Vector Regression (SVR) problem, where the hyperparameter had to be manually adjusted to be able to combine the advantages of various hyperparameter settings. Luss and d'Aspremont [40] used the MKL approach to simultaneously learn separate kernels that are assigned to a text dictionary and a time series of absolute returns. The results were compared with the results of MKL using only textual data and MKL using only stock return data. Combining the two data sources yielded higher accuracy and a higher Sharpe ratio than any single data source. Therefore, the main discovery of this paper is to combine

information such as news articles and stock returns to predict abnormal returns, yielding better results and improving performance compared to predictions based on a single data source.

This study evaluates the accuracy of the best-performing method according to many research studies at each stage - text preparation, text mining, model learning, and prediction. The objective of this study is to confirm the structure of the stock market and apply the model to improve the accuracy of the stock forecast for each company.

## 3. Proposed approach

This chapter describes the construction of a system that can forecast stock movements by examining the causal relationships among influential companies through online news. First, the data is described. Second, transfer entropy analysis, which is utilized to examine the causal relationship between firms, is described. Thereafter, text preprocessing, machine learning algorithms, evaluation, and evaluation metrics are explained. This terminology was employed in subsequent works [7]. The overall process is illustrated in Fig. 3.

![](/api/attachments/FZ843XHA/fulltext/images/436301d10aa85e491502d1bd918a894387dc6186e3d4ebcdd6e689f8ec63bf07.jpg)  
Fig. 3. Proposed Approach

## 3.1 Data

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

## 3.1.1 Stock History Data

Information on stock prices is used in causal relationship inference, feature selection and data labeling. The data was obtained from KOSCOM<sup>1</sup>, which is a company that manufactures IT infrastructure for the financial industry. The data lists daily stock prices, including the open price and close price for every company from January 2014 to December 2016. The most expressive features are selected based on the market reaction to the publication of news articles. The reaction is derived from a movement of a stock price defined as the ratio the open price to close price on the day of publication. This is defined as return and it is shown below as (9). Data instances are classified into two classes in this paper. Labels ‘Up’ or ‘Down’ that correspond to return of the target stock are given to each data point.

$$
\mathrm{Return} _ {t} \stackrel {\mathrm{def}} {=} \frac {\text {Close} _ {t}}{\text {Open} _ {t}}\tag{9}
$$

In the literature, it was shown that stock movements can be predicted with daily data, since the market state changes slowly with new public information [7].

Table 3 News articles sources

<table><tr><td>News articlesources</td><td># of newsarticles</td><td>% of newsarticles (%)</td><td>Type</td></tr><tr><td>Dong-A Ilbo</td><td>3,361</td><td>4.162693</td><td>Comprehensivenewspaper</td></tr><tr><td>Kukmin Ilbo</td><td>2,568</td><td>3.18054</td><td>Comprehensivenewspaper</td></tr><tr><td>Chosun Ilbo</td><td>2,387</td><td>2.956367</td><td>Comprehensivenewspaper</td></tr><tr><td>Seoul Shinmun</td><td>1,882</td><td>2.33091</td><td>Comprehensivenewspaper</td></tr><tr><td>Segye Times</td><td>1,695</td><td>2.099305</td><td>Comprehensivenewspaper</td></tr><tr><td>Munhwa Ilbo</td><td>1,529</td><td>1.89371</td><td>Comprehensive newspaper</td></tr><tr><td>Kyunghyang Shinmun</td><td>1,416</td><td>1.753756</td><td>Comprehensive newspaper</td></tr><tr><td>Hankook Ilbo</td><td>1,125</td><td>1.393344</td><td>Comprehensive newspaper</td></tr><tr><td>Hankyoreh</td><td>785</td><td>0.972245</td><td>Comprehensive newspaper</td></tr><tr><td>JoongAng Ilbo</td><td>761</td><td>0.94252</td><td>Comprehensive newspaper</td></tr><tr><td>Digital Times</td><td>2,568</td><td>3.18054</td><td>Internet newspaper</td></tr><tr><td>Dailian</td><td>2,478</td><td>3.069073</td><td>Internet newspaper</td></tr><tr><td>Money S</td><td>1615</td><td>2.000223</td><td>Internet newspaper</td></tr><tr><td>Yonhap News Agency</td><td>14,831</td><td>18.36861</td><td>Broadcast newspaper</td></tr><tr><td>Newsis</td><td>13,284</td><td>16.45261</td><td>Broadcast newspaper</td></tr><tr><td>YTN</td><td>1,096</td><td>1.357427</td><td>Broadcast newspaper</td></tr><tr><td>KBS News</td><td>1,001</td><td>1.239767</td><td>Broadcast newspaper</td></tr><tr><td>MBC News</td><td>717</td><td>0.888025</td><td>Broadcast newspaper</td></tr><tr><td>Korea Economic Daily</td><td>5,739</td><td>7.107913</td><td>Economic Newspaper</td></tr><tr><td>Fincial News</td><td>3,769</td><td>4.668013</td><td>Economic Newspaper</td></tr><tr><td>Jose Ilbo</td><td>3,219</td><td>3.986822</td><td>Economic Newspaper</td></tr><tr><td>Maeil Business Newspaper</td><td>2,705</td><td>3.350219</td><td>Economic Newspaper</td></tr><tr><td>Herald Business</td><td>1,122</td><td>1.389629</td><td>Economic Newspaper</td></tr><tr><td>Edaily</td><td>902</td><td>1.117152</td><td>Economic Newspaper</td></tr><tr><td>Money Today</td><td>854</td><td>1.057703</td><td>Economic Newspaper</td></tr><tr><td>Etc.</td><td>7,332</td><td>9.080888</td><td>Etc.</td></tr><tr><td>Total</td><td>80,741</td><td>100%</td><td></td></tr></table>

## 3.1.2 News articles data

We experimented with real data to implement the proposed method in this paper. The data consist of financial news and stock price data from January 1, 2014 to December 31, 2016. We crawled all the financial news articles and economic news articles that are registered in Naver, which is Korea's largest portal site. This information includes most of the financial news articles that are available to the public in Korea. During this period, a total of 1,397,800 articles were crawled, excluding duplicates. Also, there are cases where a news article might quote sources like Facebook or Twitter, and it may hurt the effect of financial news. We checked if news articles are from Twitter or Facebook by searching words including ‘Twitter,’ ‘Facebook,’ and ‘Social Networking Service.’ As a result, we confirmed that our news dataset does not have an information from Twitter or Facebook.

To find news that is relevant to a company, we identified news that includes the name of the company in the news body. Among all news articles, we used 80,741 news articles which were assigned to previously selected companies. We will describe how to select companies later in Section 4. Table 3 gives details about the number of articles retrieved per news provider.

The format of the news data includes title, publisher, post time, content, and category (i.e., economy, finance and politics). The category is predefined in Naver. According to the influence of the news on the stock price, news article is categorized and each news item is labeled according to the return of the target company. For example, anews article on a company that was published at 11:00 on Monday is labeled ‘Up’ if the return is greater than or equal to 1; if it is less than 1, the return is labeled ‘Down.’ However, since the Korean stock market opens at 9:00 and closes at 16:00, and Korea has one time zone (UTC +09:00), news that is published after 16:00 is interpreted as affecting the next day [12]. The list of all companies that were used in the experiment and the up and down labels are shown in Table 4.

Table 4 Up and Down Labels of the companies

<table><tr><td>Company</td><td># of data points</td><td>Sector</td><td>% of up labels</td><td>% of down labels</td><td>Company</td><td># of data points</td><td>Sector</td><td>% of up labels</td><td>% of down labels</td></tr><tr><td>OCI</td><td>1947</td><td>Material</td><td>55.47</td><td>44.53</td><td>Daewoong Pharm.</td><td>873</td><td>pharmacy</td><td>49.94</td><td>50.06</td></tr><tr><td>Huchems Fine Chemical</td><td>175</td><td>Material</td><td>53.71</td><td>46.29</td><td>Green Cross</td><td>1583</td><td>Pharmacy</td><td>52.43</td><td>47.57</td></tr><tr><td>Kukdo Chemical</td><td>85</td><td>Material</td><td>52.94</td><td>47.06</td><td>Yuhan</td><td>854</td><td>Pharmacy</td><td>51.99</td><td>48.01</td></tr><tr><td>Hyundai-Steel</td><td>3741</td><td>Material</td><td>49.67</td><td>50.33</td><td>Jeil Pharmaceutical</td><td>155</td><td>Pharmacy</td><td>57.42</td><td>42.58</td></tr><tr><td>NamHae Chemical</td><td>179</td><td>Material</td><td>58.10</td><td>41.90</td><td>Bukwang Pharm.</td><td>218</td><td>Pharmacy</td><td>50.46</td><td>49.54</td></tr><tr><td>Hansol Chemical</td><td>110</td><td>Material</td><td>64.55</td><td>35.45</td><td>Hanmi Pharm.</td><td>3051</td><td>Pharmacy</td><td>39.72</td><td>60.28</td></tr><tr><td>Foosung</td><td>295</td><td>Material</td><td>48.14</td><td>51.86</td><td>Dong-A ST</td><td>497</td><td>Pharmacy</td><td>52.92</td><td>47.08</td></tr><tr><td>SKC</td><td>1184</td><td>Material</td><td>55.57</td><td>44.43</td><td>Boryung Pharm.</td><td>583</td><td>Pharmacy</td><td>53.52</td><td>46.48</td></tr><tr><td>SKChemical</td><td>1276</td><td>Material</td><td>51.18</td><td>48.82</td><td>Hanall BioPharma</td><td>193</td><td>Pharmacy</td><td>51.30</td><td>48.70</td></tr><tr><td>SeAh Steel</td><td>374</td><td>Material</td><td>55.35</td><td>44.65</td><td>JW Pharm.</td><td>489</td><td>Pharmacy</td><td>47.24</td><td>52.76</td></tr><tr><td>KISWIRE</td><td>166</td><td>Material</td><td>55.42</td><td>44.58</td><td>C.K.D</td><td>1200</td><td>Pharmacy</td><td>52.08</td><td>47.92</td></tr><tr><td>KiscoHolding</td><td>762</td><td>Material</td><td>50.79</td><td>49.21</td><td>Yungjin Pharm.</td><td>171</td><td>Pharmacy</td><td>49.12</td><td>50.88</td></tr><tr><td>Korea Zinc</td><td>619</td><td>Material</td><td>61.07</td><td>38.93</td><td>Ildong Holdings</td><td>46</td><td>Pharmacy</td><td>65.22</td><td>34.78</td></tr><tr><td>Ssangyong Cement Industrial</td><td>390</td><td>Material</td><td>66.15</td><td>33.85</td><td>Hanmi Science</td><td>610</td><td>Pharmacy</td><td>43.77</td><td>56.23</td></tr><tr><td>Lock&amp;Lock</td><td>652</td><td>Material</td><td>58.44</td><td>41.56</td><td>Dong-A Socio Holdings</td><td>309</td><td>Pharmacy</td><td>40.78</td><td>59.22</td></tr><tr><td>Korea Petrochemical Ind.</td><td>190</td><td>Material</td><td>50.00</td><td>50.00</td><td>Il-Yang Pharm</td><td>303</td><td>Pharmacy</td><td>59.41</td><td>40.59</td></tr><tr><td>SamKwang Glass</td><td>176</td><td>Material</td><td>45.45</td><td>54.55</td><td>Kwang dong Pharm.</td><td>721</td><td>Pharmacy</td><td>56.87</td><td>43.13</td></tr><tr><td>Young Poong</td><td>970</td><td>Material</td><td>45.46</td><td>54.54</td><td>CJ CheilJedang</td><td>5828</td><td>Food Expenses</td><td>51.80</td><td>48.20</td></tr></table>

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

<table><tr><td>Hanwha Chemical</td><td>2088</td><td>Material</td><td>53.45</td><td>46.55</td><td>Samyang</td><td>342</td><td>Food Expenses</td><td>55.56</td><td>44.44</td></tr><tr><td>Poongsan</td><td>1112</td><td>Material</td><td>53.33</td><td>46.67</td><td>Ottogi</td><td>2087</td><td>Food Expenses</td><td>52.71</td><td>47.29</td></tr><tr><td>Lotte chemical</td><td>2992</td><td>material</td><td>50.64</td><td>49.36</td><td>Hitejinro</td><td>3764</td><td>Food Expenses</td><td>53.35</td><td>46.65</td></tr><tr><td>DongKuk Steel Mill</td><td>2079</td><td>Material</td><td>52.00</td><td>48.00</td><td>Namyang</td><td>1375</td><td>Food Expenses</td><td>58.18</td><td>41.82</td></tr><tr><td>Taekwang Ind.</td><td>327</td><td>Material</td><td>45.87</td><td>54.13</td><td>Muhak</td><td>1981</td><td>Food Expenses</td><td>46.74</td><td>53.26</td></tr><tr><td>SeAh Besteel</td><td>362</td><td>Material</td><td>55.25</td><td>44.75</td><td>KT&amp;G</td><td>3349</td><td>Food Expenses</td><td>53.84</td><td>46.16</td></tr><tr><td>POSCO</td><td>1022</td><td>Material</td><td>49.80</td><td>50.20</td><td>Nonhshim</td><td>4093</td><td>Food Expenses</td><td>48.62</td><td>51.38</td></tr><tr><td>Kolon Ind.</td><td>972</td><td>material</td><td>49.49</td><td>50.51</td><td>Farmsco</td><td>236</td><td>Food Expenses</td><td>48.31</td><td>51.69</td></tr><tr><td>LG Chem</td><td>6717</td><td>material</td><td>53.48</td><td>46.52</td><td>Orion</td><td>2915</td><td>Food Expenses</td><td>50.53</td><td>49.47</td></tr><tr><td>Lotte find Chemical Co.</td><td>178</td><td>material</td><td>60.67</td><td>39.33</td><td>Samyang Holdings</td><td>309</td><td>Food Expenses</td><td>66.99</td><td>33.01</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>Dongwon F&amp;B</td><td>1528</td><td>Food Expenses</td><td>49.21</td><td>50.79</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>Lotte Chilsung</td><td>2932</td><td>Food Expenses</td><td>50.20</td><td>49.80</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>Binggrae</td><td>1205</td><td>Food Expenses</td><td>45.15</td><td>54.85</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>HiteJinro Holdings</td><td>127</td><td>Food Expenses</td><td>48.03</td><td>51.97</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>Lotte Food</td><td>1737</td><td>Food Expenses</td><td>51.41</td><td>48.59</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>Lotte Confectionery</td><td>3937</td><td>Food Expenses</td><td>54.71</td><td>45.29</td></tr></table>

## 3.2 Transfer Entropy: Finding Causal Relationships

Since Transfer Entropy is difficult to apply precisely, it is important to use an appropriate method [21]. In this paper, we followed the steps that were suggested by Vicente and Wibral [23] and Wibral et al. [24].

I. Measure TE in all pairs of variables in the system.

II. For each source-target pair, find the null distribution for TE and obtain the p-value.

III. Determine the threshold of the p-value and select only causal relationships that have a lower pvalue.

In this paper, we propose that predicting stock prices with causal relationship firms yields better results than forecasting with each company or including other unnecessary relationships. To determine the

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

causal relation, the transfer entropy of the stock price is calculated. Since price is a market value that reflects existing past records and information, asymmetric information flow between stock prices can be interpreted as the company's information records having asymmetric information flow. Therefore, we find the causal relationship using stock prices.

However, two time series often leads to spurious causality [41]. To prevent spurious causality, we selected the subjects to be analyzed initially based on the GICS sector, which is an industry classification standard that is based on economic theory [42]. We performed transfer entropy analysis on all pairs of companies within the sector.

The variables are stock prices of companies in the GICS sectors of KOSPI 200 in this study. We perform a log return transformation on the stock price to scale the stock price so that it is not affected by the absolute value of the price [16, 18, 43]. To make a proper prediction, we use training datasets only.

Therefore, the variable of the stock price y is defined as follows:

$$
\mathbf {y} _ {t} \stackrel {\mathrm{def}} {=} \log \frac {C l o s e _ {t}}{O p e n _ {t}}\tag{10}
$$

Transfer entropy is measured in pairs in the sectors. The KSG Estimator is used in this study. Additionally, as suggested by Lizier [44], in the non-Markov process, k → ∞ becomes the optimal choice where k is the history length of the process. However, to calculate k → ∞, substantial calculation time is required and the target history length shows only a small difference in the results [45]. Therefore, in this paper, since the number of time series data points in the period is approximately 500, the target history length is defined as $\mathbf { k } = 1 2 8 .$ The source history length of l = k is selected as in Schreiber [20]. The pvalue is also obtained by the method that is presented in Section 2.2.2 (Statistical Significance: p-value). In this paper, we use JIDT [46] to measure the transfer entropy using the KSG Estimator and the statistical significance. JIDT is a Java package that implements analytical computation of Information Theory and has been used in many studies [47, 48].

Finally, it is necessary to estimate the stock price by selecting a threshold p-value and a meaningful causal relationship. Generally, we test the hypothesis with the significance level of 0.05 in the

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

context of economics and social science [49]. However, the level of significance needs to change depending on context and purpose [49]. In the context of transfer entropy and the purpose of forecasting, we do not know which p-value threshold yields the best result because this study is the first to consider the causal relationship to predict stock movements with financial news. Therefore, we change the thresholds among 0.05, 0.1, 0.2, 0.3, 0.4, and 0.5 and find the threshold that yields the best predictability for each sector by grid search.

## 3.3 Text pre-processing

Text pre-processing is one of the many highly significant parts of the financial-news-based stock price prediction system. This approach consists of building datasets, feature extraction, feature selection and feature representation. To start off, we must eliminate the unnecessary parts of the news. This can be done by discarding all the unnecessary information, such as HTML tags and emails.

For building datasets, we have two categories: news assigned for target firm and news assigned for causal firms.

For feature extraction, a Bag-of-words model is used. Since all words must be infinitives to utilize the Bag-of-words model, KKMA POS Tagger is used to create infinitives where every infinitive implies a component [50]. We use the Bag-of-words model on every dataset with only their training sets. If there are n causal firms, we do Bag-of-words n+1 times. In addition, if there is more than one news article for a company on one day, we aggregate the news. As in [7], the infinitives of all words that appear in less than three articles are removed.

To select the components that have an effect on each company, Chi-square testing is performed. The Chi-square test is used to determine whether the observed frequency is significantly different from the expected frequency, and the higher the value, the more different the frequencies. In other words, features with higher value in the Chi-square test have a larger effect on the stock price. Especially, we used Chi-square testing on the target firm with target firm stock price, and on the causal firms with target firm stock price. Only the top 10% of features with the highest discriminatory power are selected in the Chi-square test. The number of features in this paper ranges from 500 to 1000. It is consistent with 567 of Hagenau et al. [10] and 500 of Shynkevich et al. [7].

Each feature is weighted after feature selection with the TF-IDF method. However, the features after TF-IDF weighting have a different scale depending on the number of the features. Thus, a scaling process is needed to appropriately execute the machine learning process because we simultaneously consider many datasets on the target firm and causal firms. At this stage, the number of features that are selected is multiplied by the same method as was used by Shynkevich et al. [7] — if the number of features in the top 10% is k, then k is multiplied by the TF-IDF (k \* TF-IDF).

## 3.4 Machine Learning Techniques

Multiple Kernel Learning (MKL) is a combination of sub-kernels with positive and linear combination parameters. It is possible for a kernel to differ with a different set of parameters or have separate datasets for the same labels [51]. That is, MKL is expressed as equation (11), where $K _ { s }$ is a predefined kernel matrix, and $\eta _ { s }$ is a weight of the kernel $K _ { s }$

$$
\mathrm{K} = \sum_ {s = 0} ^ {S} \eta_ {s} K _ {s} s. t. \eta_ {s} \geq 0\tag{11}
$$

The weight parameters of kernels are tuned during the training process. There are many MKL methods to find the optimal weight parameters [9, 52]. Among them, we choose the EasyMKL method [9] to optimize the weights of kernel matrices, which is considered one of the state-of-the-art algorithms. $\mathrm { G } _ { \mathrm { t r } } = \left\{ ( x _ { s , 1 } , y _ { 1 } ) , \dots , ( x _ { s , i } , y _ { i } ) \right\}$ and the test dataset i $\mathrm { { s G } _ { t e } = }$ $\left\{ ( x _ { s , i + 1 } , y _ { i + 1 } ) , \ldots , ( x _ { s , l } , y _ { l } ) \right\}$ where $x _ { s , i } \in R ^ { m }$ means input data to $K _ { s }$ belonging to an input space X, and $y _ { i } \in \{ - 1 ( d o w n ) , + 1 ( u p ) \}$ is the desired target value for the pattern $x _ { s , i }$ . We use a hat, $\mathrm { e . g . , } \hat { Y } ,$ , to denote the submatrices obtained considering training examples only. EasyMKL optimization is as follows.

$$
\max _ {\| \eta \| = 1} \min _ {\gamma \in \Gamma} (1 - \Lambda) \gamma^ {T} \hat {Y} \bigl (\sum_ {s = 0} ^ {S} \eta_ {s} \widehat {K} _ {s} \bigr) \hat {Y} \gamma + \Lambda \| \gamma \| ^ {2}\tag{12}
$$

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

$$
s. t. \Gamma = \{\gamma \in R _ {+} ^ {L} | \sum_ {y _ {i} = + 1} \gamma_ {i} = 1, \sum_ {y _ {i} = - 1} \gamma_ {i} = 1 \}
$$

In this paper, we use the radial basis function kernel (rbf kernel). The rbf kernel is the most commonly used kernel and is applied to a variety of data since it can handle nonlinear relations [53]. In addition, because the rbf kernel can include a linear kernel [54] and a sigmoid kernel [55], depending on the range of parameters, and it has low numerical complexity [53], the rbf kernel is a reasonable choice. The rbf kernel is expressed as follows:

$$
\mathrm{K} \big (z _ {i}, z _ {j} \big) = e ^ {- \frac {\big \| z _ {i} - z _ {j} \big \| ^ {2}}{2 \sigma}} s. t. \sigma > 0\tag{12}
$$

The parameter σ is a width of rbf kernel. Depending on $\sigma ,$ the properties of the rbf kernel change substantially so that it is important to find appropriate parameters [53]. In this paper, the grid search method is performed at $\circ = 0 . 0 1 , 0 . 1 , 0 . 2 5 , 0 . 5 , 1 , 2 , 5 , 1 0 , 1 5 , 2 0 , 3 0 , 5 0 ,$ , and 100 in a range that is similar to the one that was proposed by Hsu et al. [53].

The proposed model utilize categories of news simultaneously, news of the target firm and news for a target firm and n kernels for causal firms. To select the best parameter for each kernel, we implement a grid search with each category on the SVM algorithm. After finding optimal parameters, we combine kernels and implement MKL.

Since the focus of this paper is the development of a machine learning model to predict stock is the work of Hagenau et al. [10]. The first baseline model utilize financial news of the target firm only, and predicts with SVM. The second baseline model is the work of Shynkevich et al. [7]. The second baseline model utilizes two categories of news simultaneously, news of target firm and aggregate news of

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

firms within GICS sector. We assign two separate rbf kernels to the target firm and GICS-sector firms, and predict with MKL.

In addition, we propose an additional algorithm (Proposed Method2) to predict stock movements even if there is no news on the target firm. Training procedures are similar to the proposed method. We build a training dataset if there is a news item on the target firm or causal firms. We use the Bag-of-words model in the same way, and use Chi-square based on the stock movements of the target firm. MKL is also used in the same way. However, if there is no news on the target firm or causal firms, the assigned kernel is not trained in the training set on that day. Since previous methods can’t predict stock movements even if news on the target company did not appear, we can’t compare our Proposed Method2 with other methods. So, we implement two algorithms when only news of the direct company appears.

## 3.5 Evaluation

We used three years of news data and stock price data from January 2014 to December 2016. To perform out-of-sample test, we set the training set to contain data collected from January 1, 2014 to December 31, 2015, the validation set to contain data collected from January 1, 2016 to June 30, 2016, and the test set to contain data collected from July 1, 2016 to December 31, 2016. The training set is required to initially fit the models. The validation set is required to tune hyper-parameters. Tuning of the parameter σ, the width of the rbf kernel, is required for both MKL and SVM. Optimal parameters are determined using a grid search. During the validation, the performance of the model with different parameter settings is measured by classification accuracy. Finally, we obtain the experiment results during the test period.

## 3.6 Evaluation metrics

The evaluation metrics are Accuracy and F1-score. When the experiment has been finished, if the prediction is ‘Up’ and the actual result is ‘Up,’ it is defined as True Positive (TP). If the prediction is incorrect and the actual result is ‘Down,’ it is defined as False Positive (FP). Similarly, if the number is

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

predicted to be ‘Down’ and agrees with the actual result, it is predicted as True Negative (TN), and if the actual result is ‘Up,’ it is defined as False Negative (FN). It is summarized in Table 5 below.

Table 5 Confusion Matrix

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Prediction</td></tr><tr><td>Up</td><td>Down</td></tr><tr><td rowspan="2">Actual</td><td>Up</td><td>TP</td><td>FN</td></tr><tr><td>Down</td><td>FP</td><td>TN</td></tr></table>

In the Table 5, Accuracy and F1-score are defined as follows.

$$
\text { Accuracy } \stackrel {\text { def }} {=} \frac {T P + T N}{T P + F P + F N + T N}\tag{13}
$$

$$
\mathrm{F} 1 - \text { score } \stackrel {\text { def }} {=} 2 * \frac {\text { precision } * \text { recall }}{\text { precision } + \text { recall }} \text { where   precision } \stackrel {\text { def }} {=} \frac {T P}{T P + F P} \& \text { recall } \stackrel {\text { def }} {=} \frac {T P}{T P + F N}\tag{14}
$$

## 4. Results

This chapter discusses the results from the proposed news-based stock movement forecasting system. Before analyzing the results of the research, we analyze the causal relationship between the companies through transfer entropy within the GICS sectors and find the indicators that reflect the level of causality.

The results are shown in Table 6 below. ‘Average’ means the average of p-value of all relationships, and ‘Ratio (threshold)’ means the ratio of the number of all causal relationships with pvalue under ‘threshold’ to the number of all relationships. The lower the ‘Average,’ the higher the number of causal relationship within a sector. The higher the ‘Ratio,’ the higher the number of causal relationships within a sector. Accordingly, the Food Expenses sector and Durable goods sectors are sectors with a high level of causality. The Material and Capital goods are sectors with a middle level of causality. Pharmacy, Car, and Hardware are sectors with a low level of causality.

To show the robustness of our proposed method, we do not choose only one sector, but choose three sectors for evaluation of the proposed method. Because the Hardware sector has a small number of component companies, we remove Hardware sector to avoid sample size bias for evaluation. To prove that the results do not change by the ratio of the causal relationships, we select the Pharmacy, Material, and Food Expenses sectors, which have a low level of causality, a middle level of causality, and a high level of causality respectively, for further analysis.

Table 6 Causality statistical verification

<table><tr><td>GICS Sector</td><td>Average</td><td>Ratio (0.05)</td><td>Ratio (0.1)</td><td>Ratio (0.2)</td><td>Ratio (0.3)</td><td>Ratio (0.4)</td><td>Ratio (0.5)</td></tr><tr><td>Hardware</td><td>0.5860</td><td>0.0156</td><td>0.0625</td><td>0.1094</td><td>0.1250</td><td>0.2031</td><td>0.2188</td></tr><tr><td>Car</td><td>0.5549</td><td>0.0622</td><td>0.0933</td><td>0.1555</td><td>0.2222</td><td>0.3288</td><td>0.3822</td></tr><tr><td>Pharmacy</td><td>0.5501</td><td>0.0553</td><td>0.0969</td><td>0.1592</td><td>0.2595</td><td>0.3599</td><td>0.4429</td></tr><tr><td>Capital goods</td><td>0.5224</td><td>0.0539</td><td>0.0914</td><td>0.1714</td><td>0.2620</td><td>0.3510</td><td>0.4490</td></tr><tr><td>Material</td><td>0.5124</td><td>0.0476</td><td>0.0942</td><td>0.1972</td><td>0.3001</td><td>0.3901</td><td>0.4922</td></tr><tr><td>Durable goods</td><td>0.4834</td><td>0.0347</td><td>0.055</td><td>0.1875</td><td>0.3056</td><td>0.3889</td><td>0.4930</td></tr><tr><td>Food Expenses</td><td>0.4974</td><td>0.0415</td><td>0.1142</td><td>0.2284</td><td>0.3114</td><td>0.4430</td><td>0.5225</td></tr></table>

The following Fig. 4 depicts the stock price-based causal relationships among the three sectors: Food Expense, Pharmacy, and Materials. Each node represents a company within a sector and links and arrows represent causal relationships that affect firms. Causality that has a p-value of less than 0.2 was selected in Fig. 4.

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

![](/api/attachments/FZ843XHA/fulltext/images/4f95700b43b9a50144e7fd507c3eca1bfa2f7c9e588270f5c76e722b8dc20cb5.jpg)  
Fig. 4. Causal relationship graphs of companies within the sectors

In this section, a comparative analysis of the proposed method and existing methods is conducted. We compare the accuracy and F1-score of stock movement prediction using the causal relationship analysis method (Proposed approach) with two state f-th -art algorithms. One method applies the influence of the GICS sector (Shynkevich et al. [7]), and the other is at the individual level, which can be used as a basis for comparison (Hagenau et al. [10]) which are.

## 4.1 Results of the research model

Table 7 displays the experimental results obtained from a comparison between the proposed model and two state-of-the-art algorithms. The first column of Table 7 shows the results produced when the proposed method is used. The second column represents the results with the state-of-the-art method considering the influence of the GICS sector. The third column shows the results with the state-of-the-art method of the individual level. The rows reflect in which GICS sector the results are obtained. ‘Average’ is the average of results obtained using all three methods. ‘Standard Deviation’ represents the standard deviation of the results. The highest forecasting accuracy is marked in bold and underlined. In all GICS sectors, the proposed method showed the best predictive power. Detailed results are presented in Table 7 below.

Table 7 Experimental results

<table><tr><td>GICS Sector</td><td>Results</td><td>ProposedMethod</td><td>Shynkevi ch et al. [7]</td><td>Hagenau et al. [10]</td></tr><tr><td rowspan="2">Pharmacy</td><td>Average</td><td>0.584381</td><td>0.551828</td><td>0.534255</td></tr><tr><td>Standard Deviation</td><td>0.073236</td><td>0.078205</td><td>0.085140</td></tr><tr><td rowspan="2">Material</td><td>Average</td><td>0.623473</td><td>0.588867</td><td>0.585316</td></tr><tr><td>Standard Deviation</td><td>0.072492</td><td>0.062896</td><td>0.061214</td></tr><tr><td rowspan="2">Food expenses</td><td>Average</td><td>0.558975</td><td>0.546884</td><td>0.542623</td></tr><tr><td>Standard Deviation</td><td>0.084652</td><td>0.049542</td><td>0.050500</td></tr></table>

In this paper. we use transfer entropy to predict the stock price by analyzing the causal relationship between firms. We used the p-value to determine the statistical significance of the causal relationship. We experimented by changing the statistical significance level as stated in Section 3.2. Table 8 shows the average forecasts and standard deviations for stock movement accuracies for each sector according to the p-value thresholds. The Pharmacy sector and Material sector show the highest accuracy when the p-value equals 0.4, while the Food expenses sector shows the highest accuracy when the p-value equals 0.3. The prediction accuracy significantly changes for each sector according to the change of the pvalue. Accordingly, we suggest that controlling the statistical significance differently affects the prediction and we need to perform a grid search for every company to find the best p-value for appropriate prediction.

Table 8 Experimental results by p-value

<table><tr><td rowspan="2">p-value</td><td>Pharmacy</td><td>Material</td><td>Food expenses</td></tr><tr><td>Results</td><td>Results</td><td>Results</td></tr><tr><td>0 Average</td><td>0.571615</td><td>0.585959</td><td>0.53658903</td></tr><tr><td>0 Standard Deviation</td><td>0.072737</td><td>0.071329</td><td>0.082699234</td></tr><tr><td>0 Average</td><td>0.57212</td><td>0.5872</td><td>0.540213</td></tr><tr><td>1 Standard Deviation</td><td>0.075738</td><td>0.065488</td><td>0.080919</td></tr><tr><td>0 Average</td><td>0.570321</td><td>0.594735</td><td>0.53771</td></tr><tr><td>2 Standard Deviation</td><td>0.071073</td><td>0.074038</td><td>0.083431</td></tr><tr><td>0 Average</td><td>0.564806</td><td>0.594902</td><td>0.542576</td></tr><tr><td>3 Standard Deviation</td><td>0.076117</td><td>0.079983</td><td>0.083491</td></tr><tr><td>0 Average</td><td>0.575014</td><td>0.597599</td><td>0.541202</td></tr><tr><td>4 Standard Deviation</td><td>0.078479</td><td>0.085422</td><td>0.083596</td></tr><tr><td>0 Average</td><td>0.571514</td><td>0.588698</td><td>0.537125</td></tr><tr><td>5 Standard Deviation</td><td>0.081611</td><td>0.089186</td><td>0.081719</td></tr></table>

## 4.2 Additional Analysis

One of the most important factors in predicting stock prices based on the news is whether the articles on the company are published at the relevant time. In general, it is difficult to perform an analysis at the individual company level when there are no articles that are related to the company. However, there has been no attempt to overcome this limitation, to the best of our knowledge. By analyzing the causal

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

relationship, we overcome these problems. In other words, even if direct corporate news does not appear, we can predict the stock movements with news on the causal companies. Although there are differences depending on the sector, this research method shows higher accuracy than other methods for two out of three sectors. Detailed results are shown in Table 8 below. In Table 9, the Proposed Method2 is a result from prediction where analysis was implemented even if news on the target company did not appear.

Table 9 Experimental results for the Proposed Method2

<table><tr><td>GICS Sector</td><td>Result s</td><td>Propose d Method 2</td><td>Shynkevic h et al. [7]</td><td>Hagena u et al. [10]</td></tr><tr><td rowspan="2">Pharmac y</td><td>Average</td><td>0.566711</td><td>0.551828</td><td>0.534255</td></tr><tr><td>Standard Deviation</td><td>0.041933</td><td>0.078205</td><td>0.085140</td></tr><tr><td>Material</td><td>Average</td><td>0.578514</td><td>0.588867</td><td>0.585316</td></tr><tr><td rowspan="3">Food Expenses</td><td>Standard Deviation</td><td>0.033816</td><td>0.062896</td><td>0.061214</td></tr><tr><td>Average</td><td>0.602333</td><td>0.546884</td><td>0.542623</td></tr><tr><td>Standard Deviation</td><td>0.036026</td><td>0.049543</td><td>0.050500</td></tr></table>

To confirm the robustness of stock movement forecasting, we check the stability of the model by examining it from various angles. We not only examine the accuracy but also examine F1-score. Overall, the proposed method was dominant. Details of the results are shown in Table 10 below.

Table 10 Experimental results – F1-score

<table><tr><td rowspan="2">GICS Sector</td><td rowspan="2">Result s</td><td colspan="2">Proposed Method</td><td rowspan="2">Shynkevic h et al. [7]</td><td rowspan="2">Hagenau et al. [10]</td></tr><tr><td>Proposed</td><td>Proposed Method</td></tr><tr><td colspan="2"></td><td>Method</td><td>2</td><td></td><td></td></tr><tr><td>Pharmacy</td><td>Average</td><td>0.603790</td><td>0.596246</td><td>0.563747</td><td>0.563615</td></tr><tr><td rowspan="2">Material</td><td>Standard Deviation</td><td>0.121985</td><td>0.068114</td><td>0.123071</td><td>0.118995</td></tr><tr><td>Average</td><td>0.689825</td><td>0.623628</td><td>0.677068</td><td>0.677142</td></tr><tr><td rowspan="3">Food Expenses</td><td>Standard Deviation</td><td>0.074463</td><td>0.058707</td><td>0.087689</td><td>0.081261</td></tr><tr><td>Average</td><td>0.601027</td><td>0.574451</td><td>0.630857</td><td>0.630411</td></tr><tr><td>Standard Deviation</td><td>0.085216</td><td>0.068521</td><td>0.073959</td><td>0.073526</td></tr></table>

To test our causality detection is valid, we benchmark with two state-of-the-art causality N detection papers [29, 33]. Oh et al. [33] means considering onl uni-directional causality, and Výrost et al. [29] state causality detection using Granger causality. We implemented all the procedures in the Pharmacy sector including text preprocessing, MKL and grid search, except the causality detection. Results show that the proposed method shows better results than two state-of-the-art methods. Especially, results suggest that considering bi-directional causality is important and TE shows better results than Granger causality in the Pharmacy sector. Details of the results are shown in Table 11.

Table 11 Benchmark against two state-of-the-art causality detection algorithms

<table><tr><td>GICS Sector</td><td>Results</td><td>Proposed Method</td><td>Oh et al. [33]</td><td>Výrost et al. [29]</td></tr><tr><td rowspan="2">Pharmacy</td><td>Average</td><td>0.584381</td><td>0.564935</td><td>0.573040</td></tr><tr><td>Standard Deviation</td><td>0.073236</td><td>0.071273</td><td>0.075190</td></tr></table>

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

We also implemented sensitivity analysis in the Pharmacy sector to check if prediction power is different by news article sources. Results from sensitivity analysis showed that there is no statistically significant difference between news article sources.

## 5. Conclusions and future work

Entering the era of Big Data, stock price forecasting using machine learning has been actively studied, and research on predicting stock prices based on unstructured data has attracted considerable attention. Since it is impossible for investors to read all of the news about stocks, investors can gain potential benefits by using automated systems that can identify information from multiple sources and accurately predict changes in market prices. We propose a machine learning algorithm that predicts stock movements by analyzing financial news.

In this study, we analyze the causal relationships between firms that have not been controlled by the analysis of the individual companies and within a sector to improve the accuracy of the model. This method improves predictability by overcoming the main limitation of previous research that bidirectional influence within the GICS sectors is assumed. We apply the transfer entropy method, which is actively used in the field of physics, and we analyze the causal relationship clearly and apply it to the prediction model. The analysis was conducted at the sector level to identify causal relationships that had an impact on firms. The reason for analyzing the causal relationships at the sector level without analyzing all the companies is that this approach may show a spurious causality [41] because it finds the causality with time series. To prevent this, we perform our analysis in the economically classified GICS sector.

The results of this study show that high prediction accuracy and F1-score are obtained with the causal relationship between firms. Our results propose that the directional relationship between companies should be analyzed and it needs to be reflected in the prediction phase. In addition, results show that the Proposed Method2 forecasts the stock movements well even when there is no financial news on the target firm, but financial news is published on causal firms. We also find that the results vary with the p-value threshold of transfer entropy. Therefore, it is important to find proper the threshold through a grid search.

We have a limitation in that we searched only three sectors so that we did not find a correlation between characteristics of the sector and the proposed method. In future work, we should find the relationship between the level of causality of the sector and the proposed approach. Additionally, we have a limitation in that the threshold of the p-value needs to be determined by a grid search. In the future work, we need to find a way to set the threshold by analyzing the characteristics of the GICS sector, or the characteristics of firms. Another possible direction for future work is to analyze the causal relationship not within the GICS sector but within the KOSPI 200. We can perform a more sophisticated analysis by examining various relationships and not being limited by the assumption that we have a relationship only within the sector.

## References

[1] A.K. Nassirtoussi, S. Aghabozorgi, T.Y. Wah, D.C.L. Ngo, Text mining for market prediction: A systematic review, Expert Systems with Applications, 41 (2014) 7653-7670.

[2] E.F. Fama, Random walks in stock market prices, Financial analysts journal, 51 (1995) 75-80.

[3] C. Eom, S. Choi, G. Oh, W.-S. Jung, Hurst exponent and prediction based on weak-form efficient market hypothesis of stock markets, Physica A: Statistical Mechanics and its Applications, 387 (2008) 4630-4636.

[4] H.E. Hurst, Long term storage capacity of reservoirs, ASCE Transactions, 116 (1951) 770-808.

[5] Z.M. Shi, G. Lee, A.B. Whinston, Toward a Better Measure of Business Proximity: Topic Modeling for Industry Intelligence, Management Information Systems Quarterly, 40 (2016) 1035-1056.

[6] R.P. Schumaker, H. Chen, A quantitative stock prediction system based on financial news, Information Processing & Management, 45 (2009) 571-583.

[7] Y. Shynkevich, T.M. McGinnity, S.A. Coleman, A. Belatreche, Forecasting movements of health-care stock prices based on different categories of news articles using multiple kernel learning, Decision Support Systems, 85 (2016) 74-83.

[8] O. Kwon, G. Oh, Asymmetric information flow between market index and individual stocks in several stock markets, EPL (Europhysics Letters), 97 (2012) 28007.

[9] F. Aiolli, M. Donini, EasyMKL: a scalable multiple kernel learning algorithm, Neurocomputing, 169 (2015) 215-224.

[10] M. Hagenau, M. Liebmann, D. Neumann, Automated news reading: Stock price prediction based on financial news using context-capturing features, Decision Support Systems, 55 (2013) 685-697.

[11] B. Wuthrich, V. Cho, S. Leung, D. Permunetilleke, K. Sankaran, J. Zhang, Daily stock market forecast from textual web data, IEEE International Conference on Systems, Man, and Cybernetics, IEEE, 1998, pp. 2720-2725.

[12] Q. Li, T. Wang, P. Li, L. Liu, Q. Gong, Y. Chen, The effect of news and public mood on stock

movements, Information Sciences, 278 (2014) 826-840.

[13] S.S. Groth, J. Muntermann, An intraday market risk management approach based on textual analysis, Decision Support Systems, 50 (2011) 680-691.

[14] J. Bollen, H. Mao, X. Zeng, Twitter mood predicts the stock market, Journal of computational science, 2 (2011) 1-8.

[15] M. Paluš, V. Komárek, Z. Hrnčíř, K. Štěrbová, Synchronization as adjustment of information rates: detection from bivariate time series, Physical Review E, 63 (2001) 046211.

[16] R. Marschinski, H. Kantz, Analysing the information flow between financial time series, The European Physical Journal B-Condensed Matter and Complex Systems, 30 (2002) 275-281.

[17] P. Verdes, Assessing causality from multivariate time series, Physical Review E, 72 (2005) 026222.

[18] O. Kwon, J.-S. Yang, Information flow between stock indices, EPL (Europhysics Letters), 82 (2008) 68003.

[19] J. Runge, J. Heitzig, N. Marwan, J. Kurths, Quantifying causal coupling strength: A lag-specific measure for multivariate time series related to transfer entropy, Physical Review E, 86 (2012) 061121.

[20] T. Schreiber, Measuring information transfer, Physical review letters, 85 (2000) 461.

[21] T. Bossomaier, L. Barnett, M. Harré, J.T. Lizier, An introduction to transfer entropy, Springer2016.

[22] T.M. Cover, J.A. Thomas, Elements of information theory, John Wiley & Sons2012.

[23] R. Vicente, M. Wibral, Efficient estimation of information transfer, Directed Information Measures in Neuroscience, Springer2014, pp. 37-58.

[24] M. Wibral, R. Vicente, M. Lindner, Transfer entropy in neuroscience, Directed Information Measures in Neuroscience, Springer2014, pp. 3-36.

[25] L. Barnett, T. Bossomaier, Transfer entropy as a log-likelihood ratio, Physical review letters, 109 (2012) 138105.

[26] K. Hlaváčková-Schindler, M. Paluš, M. Vejmelka, J. Bhattacharya, Causality detection based on information-theoretic approaches in time series analysis, Physics Reports, 441 (2007) 1-46.

[27] N. Wiener, The theory of prediction, Modern mathematics for engineers, DOI (1956) 165-190.

[28] C.W. Granger, Investigating causal relations by econometric models and cross-spectral methods, Econometrica: Journal of the Econometric Society, DOI (1969) 424-438.

[29] T. Výrost, Š. Lyócsa, E. Baumöhl, Granger causality stock market networks: Temporal proximity and preferential attachment, Physica A: Statistical Mechanics and its Applications, 427 (2015) 262-276.

[30] F.A. Razak, H.J. Jensen, Quantifying ‘causality’in complex systems: understanding transfer entropy, PloS one, 9 (2014) e99462.

[31] T.D.M. Peron, F.A. Rodrigues, Collective behavior in financial markets, EPL (Europhysics Letters), 96 (2011) 48004.

[32] T. Lux, M. Marchesi, Scaling and criticality in a stochastic multi-agent model of a financial market, Nature, 397 (1999) 498.

[33] G. Oh, T. Oh, H. Kim, O. Kwon, An information flow among industry sectors in the Korean stock market, Journal of the Korean Physical Society, 65 (2014) 2140-2146.

[34] A. Sensoy, C. Sobaci, S. Sensoy, F. Alali, Effective transfer entropy approach to information flow between exchange rates and stock markets, Chaos, Solitons & Fractals, 68 (2014) 180-185.

[35] E.J. De Fortuny, T. De Smedt, D. Martens, W. Daelemans, Evaluating and understanding text-based stock price prediction models, Information Processing & Management, 50 (2014) 426-441.

[36] T.H. Nguyen, K. Shirai, J. Velcin, Sentiment analysis on social media for stock movement prediction, Expert Systems with Applications, 42 (2015) 9603-9611.

[37] P.C. Tetlock, All the news that's fit to reprint: Do investors react to stale information?, The Review of Financial Studies, 24 (2011) 1481-1512.

[38] Y. Yu, W. Duan, Q. Cao, The impact of social and conventional media on firm equity value: A sentiment analysis approach, Decision Support Systems, 55 (2013) 919-926.

[39] M. Kraus, S. Feuerriegel, Decision support from financial disclosures with deep neural networks and transfer learning, Decision Support Systems, 104 (2017) 38-48.

[40] R. Luss, A. d’Aspremont, Predicting abnormal returns from news using text classification, Quantitative Finance, 15 (2015) 999-1012.

[41] Z. He, K. Maekawa, On spurious Granger causality, Economics Letters, 73 (2001) 307-313.

[42] S. Bhojraj, C. Lee, D.K. Oler, What's my line? A comparison of industry classification schemes for capital market research, Journal of Accounting Research, 41 (2003) 745-774.

[43] L. Sandoval, Structure of a global network of financial companies based on transfer entropy, Entropy, 16 (2014) 4443-4482.

[44] J.T. Lizier, M. Prokopenko, A.Y. Zomaya, Local information transfer as a spatiotemporal filter for complex systems, Physical Review E, 77 (2008) 026110.

[45] J.T. Lizier, Measuring the dynamics of information processing on a local scale in time and space, Directed information measures in neuroscience, Springer2014, pp. 161-193.

[46] J.T. Lizier, JIDT: An information-theoretic toolkit for studying the dynamics of complex systems, Frontiers in Robotics and AI, 1 (2014) 11.

[47] J. Garland, R.G. James, E. Bradley, Leveraging information storage to select forecast-optimal parameters for delay-coordinate reconstructions, Physical Review E, 93 (2016) 022221.

[48] D. Darmon, P.E. Rapp, Specific transfer entropy and other state-dependent transfer entropies for continuous-state input-output systems, Physical Review E, 96 (2017) 022121.

[49] R.L. Wasserstein, N.A. Lazar, The ASA’s statement on p-values: context, process, and purpose, The American Statistician, 70 (2016) 129-133.

[50] D.-J. Lee, J.-H. Yeon, I.-B. Hwang, S.-G. Lee, KKMA: a tool for utilizing Sejong corpus based on relational database, Journal of KIISE: Computing Practices and Letters, 16 (2010) 1046-1050.

[51] Y. Gu, C. Wang, D. You, Y. Zhang, S. Wang, Y. Zhang, Representative multiple kernel learning for classification in hyperspectral imagery, IEEE Transactions on Geoscience and Remote Sensing, 50 (2012) 2852-2865.

[52] A. Jain, S.V. Vishwanathan, M. Varma, SPF-GMKL: generalized multiple kernel learning with a million kernels, Proceedings of the 18th ACM SIGKDD international conference on Knowledge discovery and data mining, ACM, 2012, pp. 750-758.

[53] C. Hsu, C. Chang, C. Lin, A practical guide to support vector classification. Taipei: Department of Computer Science National Taiwan University, 2010.

[54] S.S. Keerthi, C.-J. Lin, Asymptotic behaviors of support vector machines with Gaussian kernel, Neural computation, 15 (2003) 1667-1689.

[55] H.-T. Lin, C.-J. Lin, A study on sigmoid kernels for SVM and the training of non-PSD kernels by SMO-type methods, submitted to Neural Computation, 3 (2003) 1-32.

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

## Biographical Note

The first author, Kihwan Nam, received a Ph.D. in information systems from the College of Business, Korea Advanced Institute of Science and Technology (KAIST). He is currently adjunct Professor of Management Informatics, College of Business, Hanyang University. His research interests include Quantitative Marketing Strategy, Big Data Analytics, Data Mining for Business Analysis, Statistical Analysis, Recommender System for Personalized Services, Applying Machine Running and Deep Learning in Business Analytics, Econometric model and social network service.

The corresponding author, NohYoon Seong, is a Ph.D. Candidate in information systems from the College of Business, Korea Advanced Institute of Science and Technology (KAIST). His research interests include Natural Language Processing, Big Data Analytics, Machine Learning, Econophysics, and Applying Machine Learning and Econometric model in Business Analytics.

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

## Graphical abstract

![](/api/attachments/FZ843XHA/fulltext/images/b034009c71095a8bbedc2f743e5f3ddb51d1c47c7007f3ba9256ee17f7c74cf0.jpg)  
ProposedApproach

# ACCEPTED MANUSCRIPT

Financial News-based Stock Movement Prediction using Causality Analysis of Influence

## Highlights

 In solving socioeconomic problems, we were able to achieve higher performance by successfully combining physics theory with machine learning. To the best of our knowledge, this paper is the first paper to combine complex system methodology with machine learning.

 Previous studies have predicted stock prices at the individual level and searched for relevant companies to consider their impact. This study is the first to predict stock

Existing studies were able to predict stock movements only when the news on the company was released. In this paper, we propose a method for predicting stock movements with a causal relationship through causality detection, even when no news is published directly.

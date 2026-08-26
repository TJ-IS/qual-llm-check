---
otero_id: 25047
otero_key: "J66K8468"
title: "Gaining Competitive Advantage for Trading in Emerging Capital Markets with Neural Networks"
authors: "Steven Walczak"
year: "1999"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1999.11518251"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Gaining Competitive Advantage for Trading in Emerging Capital Markets with Neural Networks

Steven Walczak

To cite this article: Steven Walczak (1999) Gaining Competitive Advantage for Trading in Emerging Capital Markets with Neural Networks, Journal of Management Information Systems, 16:2, 177-192, DOI: 10.1080/07421222.1999.11518251

To link to this article: http://dx.doi.org/10.1080/07421222.1999.11518251

![](/api/attachments/J66K8468/fulltext/images/cadcea2e6a1c43e6314248a6c62d82eea726c795b7f65af5f0d36f2703188a5e.jpg)

Published online: 02 Dec 2015.

![](/api/attachments/J66K8468/fulltext/images/641f728dbda01461e53ac4489c5349af3d5940bd183f53c24335ca415765e991.jpg)

Submit your article to this journal ↗

![](/api/attachments/J66K8468/fulltext/images/de37d27d1d491c51ade7f59048994436aad8a01a921febae8252e2f652772c93.jpg)

View related articles ↗

![](/api/attachments/J66K8468/fulltext/images/73db5762963d61cb200407d5592a4e515c1e2cac666f0c22d1a9c27f6fc6c1c7.jpg)

Citing articles: 1 View citing articles ↗

# Gaining Competitive Advantage for Trading in Emerging Capital Markets with Neural Networks

STEVEN WALCZAK

STEVEN WALCZAK is an Assistant Professor in the College of Business and Administration at the University of Colorado at Denver. His current research interests include novel applications of neural networks, expert systems, and other intelligent technologies, particularly in the domains of financial time series and medicine. His research has been published in Decision Support Systems, IEEE Transactions on Systems, Man, and Cybernetics, Expert Systems with Applications, Information and Software Technology, and many other journals.

ABSTRACT: Emerging capital markets may not be as efficient as the more established equity markets. Because of the possible inefficiency in these markets, various indicators that are external to the emerging capital market may provide a significant trading advantage. A preliminary analysis suggests that the Singapore market appears to be efficient. Neural network models are used to evaluate the claim that emerging equity markets, specifically the Singapore exchange, are affected by external signals and attempt to exploit any trading advantage imparted by these signals. The neural network technique as it is applied to trading on market indices in the “emerging” Singapore market is compared with the more established Dow Jones market index. Results indicate that external market signals can significantly improve forecasting on the Singapore DBS50 index but have little or no effect on forecasts for the more established Dow Jones Industrial Average index. The research demonstrates the efficacy of using neural network methods to capitalize on discovered market inefficiencies. Utilizing external market signals, a neural network forecasting model achieved a 63 percent trading prediction accuracy.

KEY WORDS AND PHRASES: emerging markets, trading, neural networks, Pacific Rim.

TRADERS IN PACIFIC RIM STOCK MARKETS CLAIM THAT THEIR MARKETS may be less efficient than more established markets such as New York (measured using the Dow Jones Industrial Average, DJIA) or Tokyo (measured using the Nikkei average). In efficient markets, knowledge is assumed to be universal and therefore cannot impart any trading advantage, as stocks react instantaneously to “new” knowledge and adjust their prices to account for the impact of the new knowledge. In this article, the term “efficient market” is used to indicate a market that follows a random-walk model, and although not truly equivalent, the assumption of a random-walk model lends itself to statistical evaluation and determination. An inefficiency is then any variation from a pure random-walk model, such that a nonlinear model may accurately predict future values of the market with significantly $p \text{ value} \leq 0.05$ greater than 50 percent reliability.

In the Singapore stock market, specific external signals such as the current DJIA and Nikkei values can be used to predict the movements of the DBS50 $[2]$ (a Singapore stock market index value). The applicability of each specific external signal is dependent on various intrinsic values of the Singapore politico-economic situation. A problem for traders in the Singapore market is identifying the correlation between the intrinsic and often difficult to quantify variables and the external market signals that enable increased accuracy in forecasting future values of the market. Neural networks, as a nonparametric modeling technique, may provide a solution for emerging market traders in the Pacific Rim. A neural network given an input vector containing all possible external signals will be able to learn when to apply each of the external signals $[3]$ . Various neural network models are constructed and tested to evaluate the potential inefficiencies or information discrepancies of the Singapore stock market and also to attempt to exploit any identified inefficiencies/discrepancies. The backpropagation learning algorithm for neural networks is the most commonly implemented and cited technique for building neural network solutions to domain problems $[3, 14, 24]$ . All of the neural networks implemented in the research presented in this article use the backpropagation algorithm for learning to predict future stock market index values, thus enabling a more facile comparison with previous research.

The research presented here has several correlated goals. The first goal is to provide evidence that inefficiencies do exist in the Singapore market, which under other tests appears to be efficient. This study does not try to invalidate any claims of market efficiency, but focuses on the identification of information that provides traders and investors in Singapore with a forecasting advantage over traditional random-walk models. For the purposes of the reported research, any consistent forecasting advantage obtained through the use of internal or external market factors is called an “inefficiency in the market.” Related to the identification of market forecasting inefficiencies, the feasibility of using neural networks to identify and furthermore to capitalize on any potential inefficiencies is a secondary research goal. The outcome of the presented research is the knowledge that trading advantages are available in the Singapore market, and possibly in emerging markets in general, and that neural networks are a useful tool for modeling and exploiting the inefficiencies that provide these trading advantages.

## Background

IN ADDITION TO PERSONAL COMMUNICATIONS WITH THE AUTHOR from stock traders in Singapore, other researchers have claimed that the emerging capital markets in the Pacific Rim are inherently inefficient [10]. This inefficiency may have several causes, including thin trading and inadequacy of financial information.

## Singapore Stock Exchange

The Singapore stock exchange was incorporated as an independent entity in 1973 [5]. Prior to that time, trading had occurred in combination with the Malaysian stock exchange at Kuala Lumpur.

Various factors appear to influence the emerging stock markets of the Pacific Rim in general and the Singapore market in particular. The greatest influence appears to come from anticipated production levels in the United States and Japan, with U.S. values having the greatest impact $[2, 26]$ . There also appear to be short-term cointegration effects (movement in one market is reflected by movements in another “cointegrated” market) between the different Pacific Rim markets (including Hong Kong and Singapore) $[9, 16]$ . However, no long-term cointegration exists with any statistical significance $[9]$ , indicating the dynamic and ever changing interrelationships between the various emerging Pacific Rim markets. A very strong and persistent link exists between the Singapore and the Malaysian stock markets $[16]$ , possibly due to their long history as a joint exchange $[5]$ and the colisting of many stocks on both exchanges.

Yadav et al. [25] have shown that Pacific Basin markets—including the markets in Singapore, Japan, and Hong Kong—have nonlinear dependencies for daily stock returns for periods of one to five days. Other researchers have also claimed that financial markets in general behave in nonlinear ways [1]. Neural networks, which are an increasingly popular tool in financial trading [24], perform extremely well in modeling nonlinear domains.

## Neural Networks in Market Forecasting

Neural networks are the result of artificial intelligence research attempts to model the highly parallel and distributed nature of human learning. The neural networks used in the research reported in this article belong to a family of neural network types called supervised learning systems. The neural networks that forecast the Singapore market index reported in this research use the supervised learning algorithm of backpropagation. In addition to being a popular and widely available neural network method $[3, 14]$ , Hornik et al. $[6]$ and others $[22]$ have demonstrated that backpropagation neural networks are capable of modeling arbitrarily complex associations (both linear and nonlinear) between variables. For details on backpropagation and neural networks, the reader is referred to $[3, 4, 6, 14, 19, 22]$ .

Neural networks have already been developed to forecast individual stock and market index values. Most of the prior neural network research and applications are for the established markets in the United States $[1, 17, 23]$ , Great Britain $[17]$ , and Japan $[26]$ . Previous neural network research for forecasting stock market values uses homogeneous market information, that is, information obtained directly from the market being forecast (including moving averages, trade volumes, and interest rates). Typical performance for these neural network systems ranges from 50 to 53 percent accuracy $[1, 26]$ . White $[23]$ claims that neural networks developed in his research for predicting the value of IBM stock do not refute the efficient market hypothesis. Neural network forecasting models (as well as other statistical models) may perform better when the market is in a strong trending condition (consistently moving in one direction), reaching prediction accuracy performance levels of 56 percent [17].

## Market Inefficiencies

National investors and traders are periodically being encouraged to invest in emerging markets $[8, 18]$ to achieve extraordinary gains in their investment portfolios. Although many researchers claim that emerging markets are less efficient than their more established counterparts $[10, 18, 25]$ , long-term cointegration effects do not appear to exist in the emerging Pacific Rim markets $[9]$ . Several simple tests are available that may be used to reject an efficient market hypothesis (based on the assumption that an efficient market will follow a random walk) and confirm the potential for trading advantages through the use of any inefficiencies.

A nonparametric runs test $[18]$ is performed by examining the number of times two consecutive periods of trading move in the same direction (have a run) versus the number of times that they do not move in the same direction. Statistically, a nonparametric runs test on a market following a random-walk model should show that approximately 50 percent of the total observations occur in runs, since there are four combinations of upward and downward movements, half of which are runs (i.e., up and up or down and down). A stronger test and one that is commonly used in the financial literature is the Lo and MacKinlay $[12]$ variance ratio test. Simply put, the variance ratio between a one-period lag and a multiple-period lag should approximate the difference in the lags and should grow linearly with the size of the lag. When comparing the variances for a four-period lag with those of a one-period lag, the variance ratio should approximate 4.

Various studies have been performed to evaluate the efficiency of emerging markets, including the Pacific Rim markets. Urrutia $[18]$ uses both the nonparametric runs test and the variance ratio test to reject a random-walk model for three South American equity markets and the Mexico equity market. Because trading in these markets is thin, the Latin American markets exhibit at best a weak form of efficiency.

Huang [7] also uses a variance ratio test, among others, to examine the behavior of nine Asian markets, including Singapore. Using the variance ratio test with homoscedastic error terms, the null hypothesis of a random-walk model is rejected only for markets in Korea and Malaysia, with partial rejections (for at least one of the seven holding periods examined) for the markets in Hong Kong and the Philippines. Switching to a heteroscedasticity-consistent variance ratio model confirms the homoscedastic model for the markets with full or partial rejection of a random-walk null hypothesis and further includes partial evidence for rejecting the random-walk hypothesis for the markets in Thailand and Singapore. The only Asian market that did not show any evidence of non-random-walk behavior was the more established Japanese equity market. The Singapore market fared second best, with only one of the seven holding periods showing any evidence of non-random-walk behavior for a heteroscedasticity-consistent variance ratio model.

## Evaluating the Singapore Market for Potential Inefficiency

IF A MARKET IS EFFICIENT AND DOES NOT SIMPLY FOLLOW a complex nonlinear process), then regardless of the modeling technique, a large quantity of predictions of market performance should approximate a 50 percent accuracy rate. Inefficient markets enable models that exceed a 50 percent accurate prediction rate and if external signals are usable in the model, then prediction accuracy should increase as the appropriate external signals are added to the model.

The index values used to represent the market returns for the countries: Singapore, United States, Japan, Hong Kong, and Malaysia are the DBS50, DJIA (Dow Jones Industrial Average), Nikkei, Hang Seng, and KLSE, respectively. If either the nonparametric runs test or the variance ratio test reject the random-walk null hypothesis, then the likelihood for discovering inefficiencies is high. Data for each index is acquired for the period from October 25, 1994 through December 31, 1995. One-, two-, and five-day differences (lags) for the net change in return are calculated for use in the neural network models and for the variance ratio test. The described data sample produced 299 one-day lag values. Figure 1 shows the DBS 50 index value for the entire period.

A nonparametric runs test is performed on the data samples for the DBS50 index. For the 299 DBS50 samples, there were 151 runs, or 50.5 percent, which is not sufficient to reject a random-walk hypothesis for the DBS50 Singapore market index. Variance ratios are calculated for both two- and five-day lag variances. The two-day lag variance ratio to the one-day lag variance produces a value of 2.4, while the five-day lag variance ratio produces a value of 6.0. While the variance ratios are slightly higher than anticipated, the growth of the ratios follows the expected pattern, with the five-day ratio exactly 2.5 times the two-day variance ratio. The results from both the runs test and the variance ratio test indicate that, during the 1994–95 period, the Singapore market appeared to follow a random-walk model and would therefore not be able to provide any market-based information trading advantage. This belies earlier claims of inherent inefficiency in emerging markets [10, 18, 25].

Neural Network Model for Identification of Emerging Market Inefficiency Factors

THE APPROACH USED HERE IS TO DETERMINE INFORMATION that may indicate the presence of a non-random-walk market behavior and provide a significant trading advantage to investors in emerging markets, based on the knowledge that traditional equity markets are becoming more global $[20, 21]$ . Most neural network models that attempt to predict equity market values (indexes or individual stocks) only use information from the respective markets $[1, 17, 23]$ . The Singapore market index neural networks developed in this study begin by following the traditional modeling methodology and using only index and trade volume information from the Singapore market. The index values are required variables since this is the desired output; in other words, to predict an index value future, current index value information is required.

DBS 50  
![](/api/attachments/J66K8468/fulltext/images/4774e5ac553d24be0826b8c2ceb4a4689381384417311a61e0237284b78e6ac2.jpg)  
Figure 1. DBS 50 Market Index Values, October 25, 1994–December 31, 1995

Activity in the market, as measured by trading volumes, is included in the neural network input variable set for all indexes as a possible indicator for when to alter the effects of the various index values used in the neural network models. Singapore market traders have indicated that several different external signals may be used to predict DBS 50 future values at different times, but a significant problem is knowing when to use each of the various external indicators.

Next, index and trade volume information from more established markets are included in the neural network models. DJIA and then Nikkei market values are included to estimate the effect of more established markets whose values affect the performance of smaller emerging markets $[2, 26]$ . Finally, additional Pacific Rim market indexes and volumes are included in the input/independent variable set in order to measure intermarket cointegration effects $[9, 16]$ . The research hypothesis is that

Market index forecasting performance for the emerging Singapore market will show no trading advantage using intramarket information, but the forecasting performance will steadily increase with the inclusion of relevant external market indicators.

The corresponding null hypothesis is:

$H_{0}$ : Neural network models used to predict the five-day future of the DBS 50 Singapore stock index will all produce prediction accuracies of approximately 50 percent, regardless of the set of input variables used to formulate the neural network model.

Negation of the null hypothesis indicates the presence of a market “inefficiency” (as defined for the presented research) and demonstrates that neural networks are a productive tool for making the effect of multiple external market indicators less ambiguous.

All of the neural network models reported here have an output value that predicts the five-day future index value for the respective market. To simulate the traditional neural network approach and to demonstrate the apparent efficiency of the Singapore market, backpropagation neural network models are used to forecast the five-day future value for each of the DBS 50, DJIA, and Nikkei market index values. A sample neural network of this traditional type for the DBS 50 is shown in figure 2. The input values for each neural network are the set of one-day, two-day, and five-day lags of the closing value, along with the corresponding one-day, two-day, and five-day normalized average trading volumes for the respective index markets. Lags (l) are calculated as:

\- $l_{1} = i_{t} - i_{t-1}$ (where $i$ is the corresponding index value),

$$
\begin{array}{r l} & {\bullet l _ {2} = (i _ {t} - i _ {t - 1}) + (i _ {t - 1} - i _ {t - 2}) = i _ {t} - i _ {t - 2},} \\ & {\bullet l _ {5} = (i _ {t} - i _ {t - 1}) + (i _ {t - 1} - i _ {t - 2}) + (i _ {t - 2} - i _ {t - 3}) + (i _ {t - 3} - i _ {t - 4}) + (i _ {t - 4} - i _ {t - 5}) = i _ {t} - i _ {t - 5}.} \end{array}
$$

Trading volumes are simply the sum of all corresponding market trading volumes for the number of days indicated. The normalization process is used to scale the trading volumes to be consistent with each other (when multiple indexes are used) and indicates the number of standard deviations above (positive standard deviation values) or below (negative standard deviation values) the mean of the trading volumes from the training set.

The use of these values (the specific lags) is based on the intuition of current Singapore market traders as to the desired values needed to forecast a five-day future value. Every index set therefore is composed of six input variables.

Training data for the neural networks are the corresponding values for each of the indexes from October 25, 1994 through June 30, 1995. Evaluation data are the corresponding values for each of the indexes from July 3, 1995 through December 31, 1995, yielding 116 to 124 test cases (some cases are eliminated to remove dates with incomplete data when indexes are combined). The DBS 50 index value for all data samples (both training and evaluation data sets) represents almost a 49 percent (48.62) increase of the index value, with the remaining samples showing decreases in the index value. The evaluation data time period shows increases in the index value approximately 54 percent of the time. The percentage of increases in the market index value to decreases in the market index value provides further support for a non-trending random-walk style of behavior. Both one and two hidden layer backpropagation neural networks are implemented for each input variable set. Some researchers have claimed that a single hidden layer backpropagation neural network may approximate any nonlinear function [8, 19, 22], while others [4] indicate that the quantity of hidden layers affects the complexity of the solution surface that may be modeled by a neural network. Since the complexity of the solution surface for predicting five-day future index values is unknown, both one and two hidden layer networks are implemented.

The purpose of this study was to validate the use of neural networks as a detection mechanism for market inefficiencies (as previously defined), not to identify the optimal neural network architecture, so exhaustive combinations of neural network architectures were not performed. The quantity of nodes in the first hidden layer was set equal to the quantity of nodes in the input layer (based on the recommendation of the Neuralware Professional II Plus manufacturer). Several different configurations of the second hidden layer (when present) were analyzed (3, 6, and 9 nodes per index set). For networks with two hidden layers, architectures with a second hidden layer containing half the number of nodes in the first hidden layer produced the best results. However, the single hidden layer neural networks consistently outperformed all of the two hidden layer neural network models (as shown in Table 1).

![](/api/attachments/J66K8468/fulltext/images/dfd7ac10ab7fdff3f699bbb64aa3261b582fac6eff27d9a961285ca9740dd778.jpg)  
Figure 2. Sample Neural Network for Forecasting DBS 50 Five-Day Future Val;ues

The prediction results of the six traditional intramarket neural networks are shown in Table 1. Prediction accuracy is measured by multiplying 1–MAE (Mean Absolute Error) by 100, where the error is 0 if the correct direction of change is predicted and 1 if not predicted. A null hypothesis that only a 50 percent prediction accuracy is achievable due to the random-walk behavior in each market is used to evaluate the performance of each neural network and to produce a corresponding p value. The p value indicates the confidence of rejecting the random-walk null hypothesis. The prediction accuracy measured against a 50 percent prediction accuracy is reasonable, when compared with human trading performance in capital markets. Levitch [11] conducted a study in which only four of thirteen analyzed human forecasters succeeded in making short-term profitable trades at least 50 percent of the time. In Table 1, we can see that, at a 0.10 confidence level, only the DJIA appears to have an inefficiency (and consequently may be exploitable), and at a 0.05 level the null hypothesis cannot be rejected by any of the neural network models. The strong prediction results for the DJIA may be an artifact of a moderate upward trend that occurs for the DJIA during this period, with just over 58 percent of the data values showing a positive (upward) change to the index.

Table 1. Single Intramarket Index Set Neural Network (NN) Models

<table><tr><td>Index</td><td>NN architecture (nodes)</td><td>Prediction accuracy</td><td>p value</td></tr><tr><td>DJIA</td><td>6,6,0,1</td><td>56.56</td><td>0.0749</td></tr><tr><td>DJIA</td><td>6,6,3,1</td><td>55.74</td><td>0.1038</td></tr><tr><td>Nikkei</td><td>6,6,0,1</td><td>41.53</td><td>0.9671</td></tr><tr><td>Nikkei</td><td>6,6,3,1</td><td>33.05</td><td>0.9999</td></tr><tr><td>DBS50</td><td>6,6,0,1</td><td>50.81</td><td>0.4286</td></tr><tr><td>DBS50</td><td>6,6,3,1</td><td>44.35</td><td>0.8944</td></tr></table>

In Table 1, the single hidden layer neural network models outperform the two hidden layer models. While both one and two hidden layer models are implemented for all reported combinations of index values, it is consistently found that single hidden layer neural networks outperform their two hidden layer counterparts; consequently, only the single hidden layer results are reported for the subsequently developed neural networks that forecast the DBS 50 index.

Nine different sets of variables are implemented in neural network models to evaluate the effect of external signals in the potentially inefficient market of Singapore. The various combinations are derived to determine the effect of specific signals to the Singapore market (from the hypothesis that different intrinsic factors change the relative influence of the various external signals). The variable sets evaluated are: (1) DBS 50 and KLSE, (2) DBS 50 and Hang Seng, (3) DBS 50 and DJIA, (4) DBS 50 and Nikkei, (5) DBS 50, Hang Seng, and KLSE, (6) DBS 50, DJIA, and Nikkei, (7) DBS 50, DJIA, Hang Seng, and KLSE, (8) DBS 50, Nikkei, Hang Seng, and KLSE, and (9) DBS 50, DJIA, Nikkei, Hang Seng, and KLSE. Each new index included in the input variable set increases the input vector size by six variables. Although included as individual index variables in the two index models, the KLSE and Hang Seng are treated as a pair in the remainder of the neural network models. The pairing of the KLSE and Hang Seng is supported by the two index models that show neither index contributing significantly to the prediction of DBS 50 five-day future values, as well as by the literature that indicates these Pacific Rim market index values play only a minor role in modeling the Singapore market [9, 10].

Prediction accuracy results for the single hidden layer networks only are displayed in Table 2. For ease in comparison, the single index model for the DBS 50 index is also included. Table 2 indicates that, as additional external knowledge is added to the neural network's nonlinear model (except for models 1 and 3), prediction performance improves. Adding just the DJIA or KLSE index values to the DBS50 index values does not improve the neural network's output performance, but the performance is still essentially the same as the naive (random-walk) 50 percent performance. However, the other neural network models seem to indicate that the DJIA does have a significant effect when used in combination with other market indicators (note the difference between models 7 and 8 in Table 2). Similarly, although the addition of the emerging market signals of the Hang Seng (model 2) and the paired Hang Seng and KLSE indexes (model 5) improves the original performance of the neural network model, its performance is not statistically significant.

When the Nikkei index is added to the DBS 50 and when it is also added to combinations of index values, the original DBS50 neural network performance continually improves as new indexes are added, but the significance (based on a one-tailed Z test) indicates that this network's performance is still in a range that cannot reject the null hypothesis, at the 0.10 confidence level. When the Hang Seng and KLSE index values are added to the DBS50 and DJIA indexes, the prediction performance rejects the null hypothesis at the 0.05 level. Finally, when the Nikkei is included with these other four indexes, the null hypothesis of an efficient market condition is rejected at both the 0.01 and 0.005 levels.

Except for two of the index combinations (KLSE and DBS 50 and DJIA and DBS 50), as new index knowledge is incorporated into the backpropagation neural network's model of the five-day DBS 50 future value, the prediction accuracy of the neural networks continually increases, except for the one case when the KLSE is added to the Hang Seng model. As stated above, the null hypothesis that a neural network model will not exceed typical random-walk model prediction accuracies regardless of the information included in the model is rejected by both one of the four-index models and the five-index model. Furthermore, the increasing accuracy of the neural network models as new relevant index values are added to the input variable set lends intuitive evidence that the view of the Singapore market being influenced by multiple external signals is realistic.

## Further Evaluation of Multiindex Neural Network Models

AS SEEN IN TABLE 2, THE ADDITION OF OTHER PACIFIC RIM market indexes to the combination of the Singapore (DBS50) and U.S. (DJIA) indexes continually improves the prediction performance of the neural network models. This result indicates that external signals can be used to take advantage of an apparent inefficiency in the Singapore stock market.

One further test is needed before we can accept the results of the neural network models as evidence of market inefficiency in the Singapore stock market produced by the varying influences of multiple external market signals. A claim can be made that, since equity markets are becoming more global in nature, the adding intermarket knowledge to a neural network's nonlinear model of any index value would improve the corresponding prediction accuracy. This claim is particularly important in light of the recent (October 1997) crash of the Hong Kong equity market that had strong negative consequences around the world, including downward trends in many European, South American, and other Asian markets [20, 21], which indicates the presence of global cointegration. The strong decline in Hong Kong also preceded the largest decline in points on the New York stock exchange (the twelfth-largest percentage drop), causing the market to shut down [13].

Table 2. Neural Networks to Predict DBS50 Five-Day Future

<table><tr><td>Indexes</td><td>Prediction accuracy</td><td>p value</td></tr><tr><td>DBS50 only</td><td>50.81</td><td>0.4286</td></tr><tr><td>DBS50 and KLSE</td><td>45.69</td><td>0.8238</td></tr><tr><td>DBS50 and Hang Seng</td><td>51.72</td><td>0.3557</td></tr><tr><td>DBS50 and DJIA</td><td>47.97</td><td>0.6736</td></tr><tr><td>DBS50 and Nikkei</td><td>0.5259</td><td>0.2919</td></tr><tr><td>DBS50, Hang Seng, and KLSE</td><td>51.72</td><td>0.3557</td></tr><tr><td>DBS50, DJIA, and Nikkei</td><td>54.17</td><td>0.1814</td></tr><tr><td>DBS50, DJIA, Hang Seng, and KLSE</td><td>60.50</td><td>0.0110</td></tr><tr><td>DBS50, Nikkei, Hang Seng, and KLSE</td><td>55.17</td><td>0.1335</td></tr><tr><td>DBS50, DJIA, Nikkei, Hang Seng, and KLSE</td><td>62.93</td><td>0.0027</td></tr></table>

What effect will adding these additional index values have on predicting the future value of an established and supposedly efficient market? To determine this, neural network models are implemented with an input set of all five different index values, identical to the neural network model reported in the last row of Table 2 (model 9), but this time to predict the five-day future change to the DJIA. Another set of neural networks is implemented also to predict the Nikkei. Both one and two hidden layer networks are used, since, again, the general shape of the solution surface (for predicting five-day future values of the respective index) is not known and a change in surface shape between the emerging markets and the established markets is a distinct possibility. The results of testing these new neural network models are presented in Table 3, which shows that the inclusion of additional external indexes does not improve (and in fact reduces) the prediction performance for neural network models of the established New York (DJIA) and Tokyo (Nikkei) stock markets. An interesting research topic would be to acquire the data values for the five indexes reported here to see if the composite neural network model would have predicted the drop in the U.S. market at the end of October 1997.

Since the five intermarket signals worked well for the emerging Singapore market, but did not perform well for the more established New York and Tokyo markets, an interesting corollary to the research hypothesis is to see if the same intermarket indicator behavior is present in other emerging Pacific Rim equity markets. Again, one and two hidden layer neural network models are constructed to predict the five-day future value of the KLSE (Malaysia) and the Hang Seng (Hong Kong) market indices. Like their Singapore counterpart, the single hidden layer neural networks outperform the two hidden layer networks. The results for the single hidden layer neural network predictions of the 116 cases for these two markets are presented in Table 4.

Table 4 shows that, although Rowley [16] and George [5] indicate a strong connection between the Singapore and Malaysian equity markets, the KLSE does not respond to the same external market indicators (or at least not in a predictable fashion) as the

Table 3. Intermarket Neural Networks Predicting DJIA and Nikkei

<table><tr><td>Hidden layers</td><td>Prediction accuracy</td><td>Significance (p value)</td></tr><tr><td>DJIA—1</td><td>52.17</td><td>0.3228</td></tr><tr><td>DJIA—2</td><td>54.78</td><td>0.1539</td></tr><tr><td>Nikkei—1</td><td>42.98</td><td>0.9345</td></tr><tr><td>Nikkei—2</td><td>41.23</td><td>0.9699</td></tr></table>

Table 4. Intermarket Neural Networks Predicting Other Emerging Markets

<table><tr><td>Market</td><td>Prediction Accuracy</td><td>Significance (p value)</td></tr><tr><td>KLSE</td><td>49.14</td><td>0.9286</td></tr><tr><td>Hang Seng</td><td>57.76</td><td>0.0475</td></tr></table>

Singapore market. However, the Hong Kong market does appear to be influenced by some of the same external indicators as the Singapore market and rejects the null hypothesis of a market exhibiting a random-walk behavior at the 0.05 confidence level. Although the KLSE index did not appear to be influenced by the same external market indicators as the Singapore market, the highly accurate forecasts of the neural network's model for both the Singapore and Hong Kong markets indicates that emerging markets (at least in the Pacific Rim) have nonlinear dependencies that enable significant trading advantages.

Further investigation of the differences and similarities for the neural network nonparametric five-day future index models for the various emerging Pacific Rim markets, included in this study, reveals some possible causal relationships. Recall that, until 1973, the Kuala Lumpur (Malaysian) stock exchange and the Singapore stock exchange were the same entity. Following the split in 1973, Singapore aggressively pursued a global information infrastructure with one of its national goals being to become a global information trading center (knowledge center). Singapore's desire for and reliance on an international economy, like that of Hong Kong, evidently increased the cointegration effects of external (international) market signals in its own capital markets. While Malaysia's economic growth until the 1980s appeared to revolve around its agricultural product [5], the more nationalistic trend of the Malaysian market reduced the cointegration effects from other international markets.

Some additional neural network models, again evaluating both one and two hidden layer models, that forecast the five-day future value of the Hang Seng index are constructed to isolate factors shared with the Singapore market that cause high forecasting accuracy when intermarket signals are included in the forecasting models. The new neural network models for the Hang Seng produced some unexpected results. While the intermediate models—those containing some of the intermarket index values—produced forecast accuracies less than the full intermarket index model shown in Table 4, the neural network model that used only the Hang Seng index values to forecast its own future values produced a forecast accuracy of 56.90 percent. This is significantly different than a random-walk model, using a Z test, at the 0.10 level. While the single index model for the Hang Seng is slightly less accurate than the full intermarket index model, it is not statistically different with any significance.

The Hang Seng model is similar in behavior not only to the emerging Singapore model, with reliance on intermarket signals, but also to the more established DJIA, which produces optimal results using only intramarket values. These results indicate that the Hong Kong market in 1995 was in a transition period, moving from the emerging market phase (with reliance on international signals) to the established market phase (where the market is mature and large enough to withstand some of the shocks generated in the international market place). The indication of the neural network model of the greater maturity of the Hong Kong stock market is intuitively appealing, as it coincides with the fact that the Hong Kong Exchange started trading stocks in 1947, while the Singapore market did not begin trading (as an independent entity) until 1973 [5]. The Hong Kong market underwent further changes from 1969 through 1973 with the additions and integration of three more stock exchanges. Thus, following a normal development curve, the Hong Kong market should be ahead of the Singapore market.

Furthermore, a model of the correlation between market maturity and effect of external market signals can now be formed. Figure 3 shows the proposed correlation model, which exhibits an inverted U-shape similar to learning and development curves in other domains [15]. Newer (emerging) markets, such as that of Malaysia, are not yet ready to take advantage of international financial and economic information to further develop their capital markets. Eventually, markets like Singapore, which are still considered emerging, begin to incorporate international knowledge as well as national knowledge into their markets to gain maximum international competitive advantage. Finally, markets that have fully integrated international signals and knowledge into their own marketplace continue to grow and eventually become strong enough to resist minor shocks and signals from the international marketplace, such as the DJIA and Nikkei, and the direction in which the Hang Seng appears to be heading.

## Summary

EVIDENCE IS PRESENTED THAT THE SINGAPORE STOCK MARKET SUFFERS from at least one form of inefficiency. This inefficiency can be exploited by the use of nondomestic stock indexes as indicators of upcoming changes to the overall Singapore market. Neural networks provide a mechanism for both evaluating the presence of an inefficient market and exploiting that inefficiency. Because of the neural network learning methodology [3], external indicators of market forces can be automatically incorporated into a prediction model at the appropriate time.

In addition, comparison of multiple intramarket and intermarket models for three emerging Pacific Rim stock markets at various stages of market maturity has enabled the preliminary design of a correlation model that demonstrates how intermarket cointegration effects vary with market maturity. Such knowledge can be used to evaluate the appropriateness of different types of forecasting models, depending on the perceived maturity level of the capital market to be forecast.

![](/api/attachments/J66K8468/fulltext/images/620965a01a0fb969222faa0fb8712f50e76522f50e7e3e99de3e6f72a72c329f.jpg)  
Figure 3. Model of Capital Market Growth with Respect to International Cointegration of Markets

In this study, only some of the possible neural network architectures were implemented for each set of input variables. The best performance from the implemented models should therefore be viewed as the minimum possible improvement to forecasting achievable through the use of neural networks. Additional research is needed to identify other potential external factors that affect the Singapore market (e.g., the Korean and/or Australian markets).

As with the Singapore market, neural networks provide an intelligent decision aid for determining the relative efficiency (or lack thereof) in emerging stock markets, as shown by the neural network prediction results for the Hong Kong stock market index. Potential indicators of short-run performance trends in emerging markets can be identified by incorporating them into the input variable set of a neural network model and evaluating the effect on forecast performance. The incremental adjustment of the set of input variables enables traders to determine if an external signal contributes to forecasting accuracy or whether it is simply noise. Furthermore, traders in markets like that of Singapore that are affected by external signals may use nonparametric neural network modeling to avoid determining which intrinsic factors should be used and when to alter the significance for each of the external signals in their trading model.

To demonstrate the trading advantages afforded by the five-way multiindex neural network, a simulation of trading five-day futures for the DBS50 was performed. The average change to the DBS50 index value during the test period, July 1995 through December 1995, was 2.044 points. Forecasts of the five-day future position from the neural network were used to determine short and long positions on the DBS50 index value. The simulation assumed that sufficient capital (a total fund of \$100,000) was kept in reserve to enable a \$10,000 position/trade to be made for each neural network forecast. The neural network produced a net gain of just under \$32,000 during the six months of the test period. $^{1}$ The potential for a 62–63 percent annualized return demonstrates the trading advantage imparted by neural network models of emerging equity markets.

## NOTES

Acknowledgments: A special note of appreciation to Ng Tian Khean, DBS Securities, Singapore, whose insights helped formulate the research question of modeling multiple intermarket index values for predicting the Singapore stock market. He also assisted in acquiring data values for the Pacific Rim equity markets. Thanks also to two reviewers of the Journal of Management Information Systems whose comments helped to clarify and solidify the presentation of this research.

1. Actual transaction cost information was not available for the time period of the neural network test. Transaction costs are calculated based upon current transaction costs for purchasing market index positions in Singapore of \$0.60 per share reported by American Express Financial Services. Total transaction costs are then the reported modern cost multiplied by the number of shares traded daily. The neural network recommended 32 changes in position over the 116 days of the test period. If we assume slightly higher transaction costs for the last half of 1995, the net gain by the neural network is still just over \$31,000.

## REFERENCES

1. Bosarge, W.E. Adaptive processes to exploit the nonlinear structure of financial markets. In R.R. Trippi and E. Turban (eds.), Neural Networks in Finance and Investing. New York: Irwin, 1993, pp. 371–402.

2. Cheung, Y.-W., and Ng, L. Equity price variations in Pacific Basin countries. In T. Bos and T.A. Fetherston (eds.), Advances in Pacific Basin Financial Markets, vol. 1. Greenwich, CT: JAI Press, 1995, pp. 211–227.

3. Dayhoff, J. Neural Network Architectures: An Introduction. New York: Van Nostrand Reinhold, 1990.

4. Fu, L. Neural Networks in Computer Intelligence. New York: McGraw-Hill, 1994.

5. George, R.L. A Guide to Asian Stock Markets. Quarry Bay, Hong Kong: Longman Financial Services Publishing, 1989.

6. Hornik, K.; Stinchcombe, M.; and White, H. Multilayer feedforward networks are universal approximators. Neural Networks, 2, 5 (1989), 359–366.

7. Huang, B.-N. Do Asian stock market prices follow random walks? Evidence from the variance ratio test. Applied Financial Economics, 5 (1995), 251–256.

8. Kuhn, S. Where to invest now in Asia. Fortune, 133, 12 (June 24, 1996), 159.

9. Kwok, R.H.F. Market integrations in the four newly industrialized economies of Asia.

In T. Bos and T.A. Fetherston (eds.), Advances in Pacific Basin Financial Markets, vol. 1. Greenwich, CT: JAI Press, 1995, pp. 199–209.

10. Leal, R., and Austin, M. Time series properties of Asian emerging markets. In T. Bos and T.A. Fetherston (eds.), Advances in Pacific Basin Financial Markets, vol. 2. Greenwich, CT: JAI Press, 1996, pp. 379–394.

11. Levich, R.M. How to compare chance with forecasting expertise. Euromoney (August 1981), 61–78.

12. Lo, A.W., and MacKinlay, A.C. Stock market prices do not follow random walks: evidence from a simple specification test. Review of Financial Studies, 11(1988), 41–66.

13. McGee, S. Industrials dive 554.26 or 7.18 percent. Wall Street Journal, 230, 84 (October 28, 1997), C1, C19.

14. Medsker, L., and Liebowitz, J. Design and Development of Expert Systems and Neural Networks. New York: Macmillan, 1994.

15. Plunkett, K., and Marchman, V. U-shaped learning and frequency effects in a multi-layered perceptron: implications for child language acquisition. Cognition, 38 (1991), 43–102.

16. Rowley, A. Asian Stockmarkets: The Inside Story. Homewood, IL: Dow Jones-Irwin, 1987.

17. Tsibouris, G., and Zeidenberg, M. Testing the efficient markets hypothesis with gradient descent algorithms. In A.P. Refenes (ed.), Neural Networks in the Capital Markets. Chichester, UK: Wiley, 1995, pp. 127–136.

18. Urrutia, J.L. Tests of random walk and market efficiency for Latin American emerging equity markets. Journal of Financial Research, 18, 3 (Fall 1995), 299–309.

19. Walczak, S., and Cerpa, N. Heuristic principles for the design of artificial neural networks. Information and Software Technology, 41, 2 (1999), 109–119.

20. Webb, S.; Kalathil, S.; Calian, S.; and Friedland, J. Hong Kong stock drop spreads world-wide. Wall Street Journal, 230, 82 (October 24, 1997), C1.

21. Webb, S.; Spindle, B.; Tam, P.-U.; and Ascarelli, S. Hong Kong plunge triggers global rout. Wall Street Journal, 230, 84 (October 28, 1997), C1, C14.

22. White, H. Connectionist nonparametric regression: multilayer feedforward networks can learn arbitrary mappings. Neural Networks, 3, 5 (1990), 535–549.

23. White, H. Economic prediction using neural networks: the case of IBM daily stock returns. In R.R. Trippi and E. Turban (eds.), Neural Networks in Finance and Investing. New York: Irwin, 1993, pp. 315–328.

24. Widrow, B.; Rumelhart, D.E.; and Lehr, M.A. Neural networks: applications in industry, business and science. Communications of the ACM, 37, 3 (March 1994), 93–105.

25. Yadav, P.K.; Paudyal, K.; and Pope, P.F. Nonlinear dependence in daily stock index returns: evidence from Pacific Basin markets. In T. Bos and T.A. Fetherston (eds.), Advances in Pacific Basin Financial Markets, vol. 2. Greenwich, CT: JAI Press, 1996, pp. 349–377.

26. Yoda, M. Predicting the Tokyo stock market. In G.J. Deboeck (ed.), Trading on the Edge: Neural, Genetic, and Fuzzy Systems for Chaotic Financial Markets. New York: Wiley, 1994, pp. 66–79.

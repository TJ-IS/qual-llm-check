---
otero_id: 10526
otero_key: "MGTY3DRZ"
title: "Computational intelligent hybrid model for detecting disruptive trading activity"
authors: "Jia Zhai; Yi Cao; Yuan Yao; Xuemei Ding; Yuhua Li"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2016.09.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Computational intelligent hybrid model for detecting disruptive trading activity

Jia Zhai <sup>a</sup>, Yi Cao <sup>b</sup>, Yuan Yao <sup>c,</sup>⁎, Xuemei Ding <sup>d</sup>, Yuhua Li <sup>e</sup>

<sup>a</sup> Salford Business School, University of Salford, Salford M5 4WT, UK

<sup>b</sup> Division of Mathematics and Computation, School of Computing, Mathematics and Digital Technology, Manchester Metropolitan University, Manchester M1 5GD, UK

<sup>c</sup> Institute of Management Science and Engineering, School of Business Administration, Henan University, Jinming District, Kaifeng 475004, Henan Province, China

<sup>d</sup> Faculty of Software, Fujian Normal University, 350108 Fuzhou, Fujian Province, China

<sup>e</sup> School of Computing, Science & Engineering, University of Salford, Salford M5 4WT, UK

## a r t i c l e i n f o

Article history: Received 14 December 2015 Received in revised form 18 August 2016 Accepted 9 September 2016 Available online xxxx

Keywords: Machine learning One-class support vector machine Joint Gaussian mixture model Hidden Markov model

## a b s t r a c t

The term “disruptive trading behaviour” was first proposed by the U.S. Commodity Futures Trading Commission and is now widely used by US and EU regulation (MiFID II) to describe activities that create a misleading appearance of market liguidity or depth or an artificial price movement upward or downward according to their own purposes. Such activities, identified as a new form of financial fraud in EU regulations, damage the proper functioning and integrity of capital markets and are hence extremely harmful. While existing studies have explored this issue, they have, in most cases, either focused on empirical analysis of such cases or proposed detection models based on certain assumptions of the market. Effective methods that can analyse and detect such disruptive activities based on direct studies of trading behaviours have not been studied to date. There exists, accordingly, a knowledge gap in the literature. This paper seeks to address that gap and provides a hybrid model composed of two data-mining-based detection modules that effectively identify disruptive trading behaviours. The hybrid model is designed to work in an on-line scheme. The limit order stream is transformed, calculated and extracted as a feature stream. One detection module, “Single Order Detection,” detects disruptive behaviours by identifying abnormal patterns of every single trading order. Another module, “Order Sequence Detection,” approaches the problem by examining the contextual relationships of a sequence of trading orders using an extended hidden Markov model, which identi es whether sequential changes from the extracted features are manipulative activities (or not). Both models were evaluated using huge volumes of real tick data from the NASDAQ, which demonstrated that both are able to identify a range of disruptive trading behaviours and, furthermore, that they outperform the selected traditional benchmark models. Thus, this hybrid model is shown to make a substantial contribution to the literature on financial market surveillance and to offer a practical and effective approach for the identification of disruptive trading behaviour.

© 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

Trading surveillance for the monitoring of disruptive trading activities with “intent to mislead the market” has been a topic of interest for regulators in recent years, especially after the flash crash in 2010 [14,20,18,22]. The term “disruptive trading behaviours” was first proposed by the US Commodity Futures Trading Commission (CFTC) in 2013 in their interpretive statement [12] to prohibit certain disruptive trading, practices, or conduct defined as: bids or offers with intent to cancel the bid or offer before execution for violating the bid or offer prices with reckless disregard for the orderly execution or market integration. This concept has also attracted much attention from the regulators in other exchanges in the USA and EU. The Chicago Mercantile Exchange (CME) released a “Rule 575” on August 28, 2014 [14] to add “certain of the disruptive practices” to the CFTC interpretive statement [12]. In “Rule 575,” disruptive practices are further defined as orders with the purpose to cancel or mislead other market participants or to disrupt the exchange or other fair executions. In the EU, the Markets in Financial Instruments Directive II (MiFID II) was proposed as legislation regulating firms' activities in financial markets [20]. In MiFID II, a market disruptive practice is explained as a form of financial market fraud that includes all types of market abuse and spoofing activities. Due to the lack of existing research and the implementation difficulties, the MiFID II application date has been extended by the European Commission to 3 January 2018 [31]. In academia, disruptive trading activities were first introduced by Allen [3] as trade-based manipulation, which was carried out by carefully designed selling and buying sequences to induce market prices to move and follow their expectations to make a profit. The profitability and the market effects of such disruptive trading activities were then studied in [1,2], respectively. Subsequently, traditional data mining approaches have been studied to identify disruptive trading activities in [17,32,36], and [9,10]. However, those studies mainly focus on particular forms of market manipulation or disruptive behaviours rather than a complete study. In general, unlike the financial fraud in traditional areas, i.e., financial statements [37] and credit cards [4], which have been thoroughly studied, the fraud format of disruptive trading has been less studied. Ngai et al. [35] found a distinct lack of research on securities and commodities fraud, which is another term for disruptive behaviours and market manipulation. Consequently, the study of disruptive trading and its detection is important and necessary due to the requirements of regulation around the world. This study contributes to the literature gap in the financial fraud area as well as the urgent requirements from financial decision-makers, i.e., regulators around the world.

Disruptive trading behaviours can be carried out by either a single buy or sell order or a series of trading actions. Therefore, a thorough monitoring of disruptive trading shall be on each single trading action and a sequence of actions linked in contextual relationships. This is the main challenge of such a disruptive trading behaviour-monitoring problem. Another challenge arises from the fact that the trading data are usually non-stationary, and the existing regulations merely provide qualitative guidance regarding what constitutes “disruptive” instead of a quantitative definition. Most of the existing related literature empirically studies the corresponding market responses when experiencing disruptive trading. Very few works analyse the features of disruptive trading behaviours and the corresponding detection approaches. Our paper contributes to the literature gap via a thorough study of the be haviours of disruptive trading and the proposal of a hybrid detection model. A number of disruptive trading forms, i.e., ramping, spoofing, spoofing and layering, and quote stuffing, have been summarised and studied in recent years after the flash crash [15]. The former two forms, ramping and spoofing, are essentially the same form: placing large-sized or aggressively priced orders individually on the market to create the appearance of an unbalanced order book. We name it “Single Order Disruptiveness” since the spoofing orders are placed separately with no linked relations. The latter two forms, spoofing and layering and quote stuffing, are usually to overload the quotation system with large numbers of sequential aggressively priced bids or offers [30,14, 20]. Therefore, we name it “Multi Order Disruptiveness” since the spoofing is carried out by contextually linked orders. The impact of “Single Order Disruptiveness is associated with the aggressive features of one single order, and the impact of “Multi Order Disruptiveness” depends on the contextual relationship among the order sequences. Therefore, to effectively identify both tactics, we need a model that captures both the single and contextual features of orders. Until now, the existing research has fallen into two categories. The first category, em pirical studies of disruptive trading activities, proves the damage of dis ruptive trading to the proper functioning and integrity of capital markets. The second category is detection model designs based on an arguable assumption: that abnormal changes of market variables, i.e., daily return, trading volume and daily volatility, indicate disruptive trading activities. Market variable changes can be induced by disruptive trading activities, but in most cases are changed by economic or other events. Therefore, an abnormal change of market variables is a necessary but not sufficient condition of disruptive trading. Detection model designs based on that hardly achieve accurate and reliable performance across different markets and time periods.

This study introduces a hybrid detection model using two computational intelligent algorithms, Support Vector Machine (SVM) and hidden Markov model (HMM), together with a tailor-made feature extraction approach and an adaptive mechanism. The SVM detects anomalous single orders compared with normal trading behaviours, and the HMM identifies the disruptive impacts caused by contextually sequential orders. Those two models are combined as a hybrid model that covers a complete spectrum of disruptive trading activities regardless of their forms, i.e., ramping, spoofing or quote stuffing. To compensate for the non-stationary nature of the trading behaviours, a straightforward transformation (E<sub>1</sub>) is proposed as a pre-processing module for the hybrid model. The trading order is converted into a feature space, in which the hybrid model searches and recognises single as well as contextual disruptive patterns that depart from ordinary trading behaviours.

To the best of our knowledge, the proposed hybrid model, which completely detects and recognises disruptive trading activities based on a thorough analysis of the trading features, has not previously been presented. Substantial experiments have been conducted on very recent real data from US markets to evaluate the performance of the proposed framework against selected popular machine learning algorithm benchmarks. The rest of the paper is organised as follows: Section 2 provides a review of all relevant literatures; Section 3 begins with a detailed explanation of the problem and a formulation of typical cases. The hybrid detection model is proposed and discussed in detail in Section 4, and Section 5 presents the paper's conclusions.

## 2. Relevant literature

Disruptive trading activities were first defined and discussed by Allen as trade-based manipulation, which is carried out only by carefully designed selling and buying sequences to induce market prices to move and follow their expectations [3]. In his work, Allen also introduced a theoretical framework of trade-based manipulation pro tability, which is dependent on normal investors' knowledge of the existence of manipulators. Aggarwal and Wu [1] carried on from Allen and Gale's work and looked at profitable trade-based manipulation. They looked at the implication of manipulation on market efficiency and what indices were affected by it and also found that equities with low values and illiquidity were commonly targeted. They found that manipulators can curtail the effectiveness of arbitrage activities and that, during the manipulation period, liquidity, returns and volatility increased. There are fewer works related to the detection of disruptive trading activities in contrast with the volume of theoretical and empirical work on it. One paper explores and compares two computational approaches to the de tection of trade-based manipulation in the Istanbul Stock Market. The computational approaches include logistic regression, artificial neural networks, and support vector machine [36]. In this paper, detection is based on empirical studies of the statistics arising from market variables, including daily return, daily trading volume and daily volatilities. The assumption of the detection is that the greater the deviation of selected market variables from legitimate trading records. the more likely an event is deemed as manipulation. Other studies take similar ap proaches, for example, by studying known cases of manipulation that have been documented by the Securities and Exchange Commission (SEC) and then constructing a manipulated-cases data set, modelling the returns, liquidity, volatility, relevant news and related events using linear and logistic regression [17]. Aitken et al. [2] suggested that trade-based price manipulations could have significantly increased the execution costs of larger trades on 34 of the world's exchange markets between 2000 and 2005. Aitken's team refer to just one form of trade-based manipulation, ramping. The actual ramping alerts in the markets at the time were collated by Smarts Group International, which provides market surveillance solutions to the NASDAQ OMX. Ex ploration of the relationships between price manipulation and market efficiency reveals that (1) manipulation led to increased execution costs for larger trades and (2) the fewer the ramping alerts, the less the magnitude of spreads. Indeed, the result of halving or doubling ramping alerts was a 10% change in execution costs for larger trades across the world. This clearly shows how substantially market efficiency is affected by market integrity, at least in regard to larger trades. Lee et al. [30] examined how traders strategically spoofed the stock market by placing orders with little chance of being executed but with signifi cant misleading effect on the appearance of an imbalance in the order book.

Please cite this article as: J. Zhai, et al., Computational intelligent hybrid model for detecting disruptive trading activity, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.09.003

Until now, researchers have focused primarily on detecting manipulation based on assumptions drawn from empirical studies: unusual changes of certain market variables indicate manipulations. Those market variables include the daily return, daily trading volume and daily volatilities [36], liquidity [17], and transaction price, volume and time [32]. However, there is no proof showing that such unusual changes are a sufficient condition for the manipulation, which means that, although a manipulation may incur changes of market variables, those changes might not be only the results of manipulations and could possibly be results of other events in the market, i.e., big news or an economic cycle. Only two very recent papers discuss the detection of manipulative activities based on trading behaviours [9,10]. However, the proposed models only target certain types of disruptive trading activities, i.e., quote stuffing, by monitoring the most aggressive buy/sell orders, with other orders being ignored.

Therefore, the existing work does not contribute to a theoretical foundation for detecting disruptive trading behaviours. Unlike other related literature, this paper does not address the market manipulation issue but only the disruptive trading. This is because, in the most updated regulation [14,20], “manipulation” has been defined as a juristic activity and requires detailed inspections to determine the psychological intentions of a trader's disruptive behaviours. Therefore, rather than manipulation identification, this paper addresses the detection of disruptive trading behaviours from the limit order streams and covers all primary types of disruptive patterns, which are through either single or multiple orders. To the best of our knowledge, this is the first study regarding the detection of disruptive trading behaviours that are based on trading order streams, covering all primary types of disruptiveness. This paper, on one hand, contributes to the literature regarding decision-making for the financial market regulation and, on the other hand, also contributes to the literature on the financial market to fill the gap regarding market manipulation behaviour studies [2,30] and trading behaviour surveillance.

## 3. Problem formulation

In capital markets, traders submit limit orders to the exchange market with intentions of buying or selling volumes of a specific equity at a given price. When those bona fide limit orders are matched, they are executed. If not, orders are outstanding on the exchange market as the order book. Alternately, some traders also submit limit orders to the market with no intention of execution but to mislead other traders on the market so that they may yield a profit from the counterparts. The activity of submitting such non-bona fide limit orders is usually termed a disruptive trading behaviour [14,20]. Disruptive trading behaviours can be carried out by a single order or a sequence of multiple orders, both of which have different features and different impacts on the market. Therefore, we discuss them separately in the following sections.

## 3.1. Single-order disruptive trading

Some trader use straight-forward disruptive trading tactic to mislead the market. The forms are named obstacle [16], ramping [40,20], and spoofing [14]. All of these names essentially refer to the same form: placing a single large-sized or aggressively priced order on the market for a relatively longer time period than that of average orders to create the appearance of a narrowed spread or unbalanced depth on the order book [25,30,11]. Usually, disruptive trading activity is associated with a legitimate order, placed on the opposite side to the nonbona fide orders in the order book, awaiting execution to make the potential profit. Once the legitimate order is executed (or partially executed), the non-bona fide orders are immediately cancelled. The disruptive trading tactic is what the trader utilises with intent to generate an upward or downward movement in the bid or ask price, and thus further profit-making activity is only undertaken when sufficient potential profit is likely to be generated. Therefore, the disruptive trading tactic is not realised by heuristic attempts but by careful designs of the submitted order under market impact theory, which suggests that the aggressiveness of the quotes and the sizes of placed orders determine the subsequent market effects. Hautsch [25] used a vector autoregressive model (VAR) for quantitative estimation of such effect, which revealed that a notably large size or quote (compared with the current bid or ask) exerted a substantial effect on the market price. Clearly it is crucial for legitimate traders to eliminate those impacts to achieve the best execution price; however, such effects are utilised by traders who use disruptive trading to make a profit. Therefore, to maximise the effects on the market for potential profits, the disruptive trading orders should be either large-sized or aggressively priced (much higher or lower than the prevailing bid or ask). However, in practice, obviously huge-sized or aggressively priced trading can be easily suspected as an anomaly by regulators [25,30]. Considering this, the traders utilising disruptive trading actions usually carefully design the trading orders to (1) maximise the price change they may induce and (2) minimise the chance of execution and monitoring.

Lee [30] thoroughly studied one type of single-order disruptive trading and termed such a single order as a spoofing order: an order of a size at least twice that of the previous day's average order size, a price at least 6 bps away from the current bid or ask price and a cancellation time exceeding 30 min. In this definition, the quantitative features of order size (“twice”) and cancellation time (“30 min”) are the factors to maximise the market impact for potential profit, and the “6 bps away” helps the order hide from execution and inspection. Similarly, another type of spoofing order is discussed and defined by Hautsch [25] as an order of normal size, a price approximately 6.9 bps inside the spread and a cancellation time of approximately 819 ms. The aggressive price (6.9 bps inside the spread) is to induce the price change, and the short cancellation time is to minimise the risk of execution and inspection. The spoofing orders in single-order disruptive trading are illustrated in Fig. 1, where the two above-discussed types of disruptive orders are graphically shown in a three-level order book. The normalsized and quick-swept orders are aggressively inside the spread, and the passively priced orders are large-sized and stay in the order book for a long time. Clearly, price, size and time staying on the order book are three crucial order features that the traders can tune to achieve their purpose: either normal or disruptive. Although typical features of orders in disruptive trading were defined by Lee [30] and Hautsch [25], they do not necessarily follow those definitions and can be variant in different equities across different time periods. Accordingly, identifying the normality or disruptiveness of an order requires accurately modelling their boundaries rather than simply using the thresholds on each of those features.

![](/api/attachments/MGTY3DRZ/fulltext/images/1e706379ef4de2b887b064824874a9eb060eeb863d3a8d0f7072288025a21173.jpg)  
Fig. 1. Single-order disruptive trading.

Please cite this article as: J. Zhai, et al., Computational intelligent hybrid model for detecting disruptive trading activity, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.09.003

J. Zhai et al. / Decision Support Systems xxx (2016) xxx–xxx

## 3.2. Multi-order disruptive trading

Traders can also submit multiple limit orders as a sequence to the market with no intention of execution. This tactic is termed layering and quote stuffing [15]. The two names refer to the identical format: the submission of multiple orders at sequentially increasing or decreasing prices that are higher or lower than the current bid or ask price for spoofing, the submission of another large-sized order on the other side of the order book to make a profits, and the execution of the large-sized order to rapidly remove the previous multiple orders. This tactic usually floods the market with vast quantities of new orders, which are then cancelled in swift succession, thereby creating a succession of new best bid or ask quotes. Each of these quotes has the potential to lure an execution of the opposite order, which may generate a profit. The traders usually carefully design the sequence of orders based on the market impact theory [25]. As per the discussion in Section 3.1, Hautsch estimated the market impact such that the aggressive quotes exerted a substantial effect on the market price. A sequence of aggressive quotes certainly induces stronger impacts, from which the trader may make a profit. Fig. 2 shows an example of a sequence of spoofing orders in multi-order disruptive trading activities. In this example, with a bona fide large-sized sell order placed at an expected price on the ask side, a succession of manipulative buy orders, with quotes successively higher than the best bid price, were submitted to give the impression of active purchasing interest in that equity. If a trader, encouraged by the (fake) bid price changes, thus responded to the bona fide sell order, and if, just as this was almost executed, the bid quoting orders were all cancelled, the bid price would plummet back to its original level. Such tactics are usually carried out extremely swiftly to minimise the risk of the spoofing orders being picked up by genuine investors, and thus with its sequential quotes and speedy cancellations, the spoofing orders in Fig. 2 made a saw-tooth-square-shaped market impact upon the bid price.

## 4. Hybrid detection model

As per the discussion in Section 3, when carrying out the disruptive trading, a trader utilises the market impact theory to tune the features of limit orders to spoof the market for potential profits. Aggressive (inside spread) price, large size and long time period staying on the order book are features that enhance the market impact. Passive (outside spread) price, normal size and tiny time period on the order book are features that reduce the risk of unconscious execution by other traders and inspections by regulators. The features are summarised in the following Table 1, where the Italic Bold font indicates the features that enhance the market impact and the normal font indicates riskreducing features.

![](/api/attachments/MGTY3DRZ/fulltext/images/493af1c4f7ecfbd5f6e2da6c1fd2d32f123265873d9201d04bd00ce82e546e0c.jpg)  
Fig. 2. Multi-order disruptive trading triggers the bid price to increase quickly and drop also quickly after the spoofing orders are cancelled.

The summary shows the qualitative analysis of the disruptive trading tactics: a certain combination of three features of the limit order is illustrative of the legitimacy or disruptiveness of trading behaviour. Through construction of a feature vector that uses the features of price, volume and time, it is possible to quantitatively model the trading behaviours. This form of presentation can be useful in modelling data regarding trading behaviour, using machine learning techniques. However, the non-stationary nature of financial data makes such modelling far more complex. To address this, this paper proposes a transformation method that partially reduces the non-stationarity of the original data. Together with the transformation method, this paper proposes a hybrid model that recognises the disruptive trading behaviours through single orders and multi-order sequences.

## 4.1. Transformation of original trading data

## 4.1.1. Proposed transformation method

As has been discussed, financial data are usually considered to be a non-stationary time series [23]. Time series analysis, such as the autoregressive integrated moving average (ARIMA) model (which is usually used in cases where the stationary nature of data can be eliminated using an initial differencing step [39]), echoes this situation. The log return is also regarded as a traditional transformation approach for converting market data to a new time series, which is believed to not be perfectly time invariant [19,6] but nonetheless has recently been analysed and determined to be stationary [29]. The authors, inspired by both the differencing step and log-return approaches, have defined a transformation procedure that converts the original order data into a new measure. Under this new measure, the data shows a pseudostationary feature.

From this section, we take i as a time index, which denotes all order book activities (namely submission, cancellation and execution) and then illustrates an incoming order as a vector $L _ { i } \colon = [ L _ { i } ^ { p } , L _ { i } ^ { \nu } , L _ { i } ^ { t } ] ^ { T }$ , with $L _ { i } ^ { p } ,$ $L _ { i } ^ { \nu }$ and L<sup>t</sup> being the order price, volume and submission time, respectively. Let $B _ { i }$ and $A _ { i }$ indicate the best bid and ask prices instantaneously before the ith order activity, and τ is the length of a sliding window for calculating the moving average of the order volume. Given that manipulative behaviour usually occurs within a short time period, τ is set to one trading day. Thus, the moving average volume of limit orders in the previous τ time, excluding the current data point i, can be represented as

$$
\overline {{v _ {\tau}}} = \frac {1}{N} \sum_ {i = 1} ^ {N} L _ {i} ^ {v}\tag{1}
$$

where N is the total number of limit orders in the previous τ time.

Let $L _ { i } ^ { t , C }$ and $L _ { i } ^ { t , E }$ represent the cancellation and execution time of a limit order, respectively; we can denote the lifecycle of an order L as

$$
L _ {i} ^ {\text { life }} = \left\{ \begin{array}{l} L _ {i} ^ {t} - L _ {i} ^ {t, C}, \text {   if   canceled } \\ L _ {i} ^ {t} - L _ {i} ^ {t, E}, \text {   if   executed } \end{array} \right.\tag{2}
$$

The order execution and cancellation of a limit order are usually correlated with its volume. Therefore, the volume-weighted average lifecycle (VWAL) of limit orders, in the prior period τ, is calculated as

$$
\bar {L} _ {\tau} ^ {V W A L} = \frac {\sum_ {i = 1} ^ {N} L _ {i} ^ {l i f e} * L _ {i} ^ {v}}{\sum_ {i = 1} ^ {N} L _ {i} ^ {v}}\tag{3}
$$

Please cite this article as: J. Zhai, et al., Computational intelligent hybrid model for detecting disruptive trading activity, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.09.003

J. Zhai et al. / Decision Support Systems xxx (2016) xxx–xxx

Order features of disruptive trading tactic.

<table><tr><td>Disruptive Trading</td><td>Price</td><td>Size</td><td>Time on order book</td></tr><tr><td>Single-order trading</td><td>Passive (outside spread)</td><td>Large</td><td>Long</td></tr><tr><td>Multi-order trading</td><td>Sequentially aggressive (inside spread)</td><td>Normal</td><td>Short</td></tr></table>

Therefore, we convert a limit order to a three-dimensional impulse vector $\delta _ { i } \colon = [ \delta _ { i } ^ { p } , \delta _ { i } ^ { v } , \delta _ { i } ^ { t } ] ^ { T }$ by the transformation approach as follows

$$
\delta_ {i} ^ {p} = \left\{ \begin{array}{l} \ln \frac {L _ {i} ^ {p}}{B _ {i}}, \text { for   buy   order } \\ \ln \frac {L _ {i} ^ {p}}{A _ {i}}, \text { for   sell   order } \end{array} \right.\tag{4}
$$

$$
\delta_ {i} ^ {\nu} = \ln \frac {L _ {i} ^ {\nu}}{\overline {{v _ {\tau}}}}\tag{5}
$$

$$
\delta_ {i} ^ {t} = \ln \frac {L _ {i} ^ {l i f e}}{\overline {{L}} _ {\tau} ^ {V W A L}}\tag{6}
$$

The three-component impulse $\delta _ { i }$ measures the aggressiveness of the price, volume and life cycle of a limit order. Because most buy orders are placed at equal to or less than the best bid price, the impulse of the buy orders, termed the buy impulse (BI), is mostly less than or equal to zero. Similarly, the impulse of the sell orders, termed the sell impulse (SI), is mostly higher than or equal to zero.

In 24 Jan. 2013, two disruptive trading cases on Microsoft (MSFT) stock were reported by Nanex [33]. The original data of the two disruptive trading cases and normal trading data during the same time period are illustrated in Fig. 3(a). The red and blue dots represent sell orders (SO) and buy orders (BO), respectively, and the red and blue lines are ask and bid prices, accordingly. The grey filled circles with red or blue edges represent the disruptive sell or buy orders, respectively. It is clearly observed that the disruptive sell orders (red Disruptive SO) around order index 840 are placed inside the spread and sequentially lower the ask price. Similarly, the disruptive buy orders (blue Disruptive BO) around order index 980 are placed inside the spread, sequentially raising the bid price and then narrowing the spread. In addition, we also show the transformed sell (termed SI) and buy (termed BI) order prices of the two disruptive cases as grey filled circles in Fig. 3(b) and (c), respectively. It is clear that the disruptive SIs are below zero and are sequentially decreased and that the disruptive BIs, alternately, are above zero and are increased consecutively. The corresponding volumes of the disruptive orders are transformed by Eqs. (1) and (5) and shown in Fig. 3(d), where we can also observe the relatively higher volumes of the disruptive orders. The same patterns can also be observed in the reported disruptive trading cases of other stocks, i.e., Google, Intel and Apple. Therefore, based on the different features of the normal and disruptive trading behaviours, we use the transformed impulse vector $\delta _ { i } \colon = [ \delta _ { i } ^ { p } , \delta _ { i } ^ { \nu } , \delta _ { i } ^ { t } ] ^ { T }$ as the features to construct the detection model to identify the disruptive trading behaviours.

We also observe the different distributions of the transformed SI and BI of the trading orders of Microsoft stock in Fig. $^ { 4 , }$ where the SI (transformed sell order) is mainly above zero while BI (transformed buy order) is mostly below zero. Therefore, we introduce one dummy variable, Order Direction (DIRECT ), indicating the occurrence of buy or sell orders. The inclusion of such a dummy variable is necessary to distinguish between the effects caused by different types of orders. Therefore, the transformed vector $\delta _ { i }$ is defined as $\delta _ { i } \colon = [ \delta _ { i } ^ { p } , \delta _ { i } ^ { \nu } , \delta _ { i } ^ { t } , \mathrm { D I R E C T _ { i } } ] ^ { T }$

## 4.1.2. Stationarity testing of the transformation method

To examine the stationarity reduction of the proposed transformation method, we use the KPSS test [28], one of the most popular unit root stationary process approaches, to test the original and transformed data. The null hypothesis of the KPSS is that the time series is a stationary trend over a range of lags. We select the lag value as the suggestion in [28], using a number of lags on the order of ${ \sqrt [ { 2 } ] { T } } ,$ , where T is the sample size. An example of test results of Microsoft stock data on 24 Jan. 2013 is shown below in Tables 2 and 4.

In the example in Tables 2–4, the tests on the transformed ask and bid prices fail to reject the hypothesis of stationarity, while other tests all reject it. However, in the rejected tests, the test statistics of the transformed data are all significantly smaller than that of the

original data. The test statistic in KPSS, defined as $\frac { \sum _ { t = 1 } ^ { T } S _ { t } ^ { 2 } } { s ^ { 2 } T ^ { 2 } } ,$ , where $s ^ { 2 }$ is the Newey–West estimate of the long-run variance, $s _ { t } = e _ { 1 } + e _ { 2 } + \ldots e _ { t } ,$ and e values are the residuals, is designed for the null hypothesis of stationarity and shall be close to zero under stationary null [28]. This indicates that the level of dispersion in the transformed data is far lower than that found in the original data, which suggests that the nonstationarity of transformed data tends to be reduced. Similar results are also observed in Google, Apple and Amazon stock data on 18 Oct. 2013. Therefore, we use the proposed transformation as a feature extraction method to reduce the non-stationary nature of the original data, and the detection models are trained on the transformed vector $\delta _ { i } \colon = [ \delta _ { i } ^ { p } , \delta _ { i } ^ { \nu } , \delta _ { i } ^ { t } , \mathrm { D I R E C T _ { i } } ] ^ { T }$

## 4.2. Disruptive trading detection

As discussed in Section 3.1, traders can use either single or multiple disruptive orders to induce abnormal market impacts and make a profit. Disruptive orders show anomalous behaviours to legitimate trading actions on the order book, as shown in Fig. 1. We propose an anomaly detection algorithm-based model for detecting both the single- and multiple-order disruptive trading actions. An anomaly detection algorithm is used due to the following two reasons:

1) Among the mass of normal trading data generated everyday around the world, only a small percentage is related to disruptive trading activities. Without effective monitoring mechanisms, those disruptive trading cases are very costly to find via the manual checking of financial experts. At the same time, regulatory rules usually prohibit the disclosure of those illegitimate trading behaviours.

2) Furthermore, disruptive trading tactics are also evolving over time. The collected disruptive cases only reflect “old” manipulation types, which might not contain the same features as the evolved manipulations. Modelling based on those data cannot achieve a good detection rate.

Disruptive order detection can be considered as an anomaly detection problem, which is the identification of new or unknown data patterns not exposed during the model training process. According to the discussion in Section 3, detecting disruptive trading behaviours requires monitoring each single order and multiple orders as a sequence; therefore, we propose an anomaly detection-based hybrid model composed of two components, the monitoring of single and multiple orders, for complete detection of all types of disruptive trading behaviours. The detection flow employing the proposed hybrid model is described in Algorithm 1 and illustrated in Fig. 5, where the “Single Order Detection” and “Order Sequence Detection” modules represent two components of the hybrid model, and other modules represent the input order stream handlers for the models. The original order stream is transformed into the impulse vector $\delta _ { i } \colon = [ \delta _ { i } ^ { p } , \delta _ { i } ^ { \nu } , \delta _ { i } ^ { \bar { t } } , \mathrm { D I R E C T _ { i } } ] ^ { T }$ , and each single vector $\delta _ { i }$ is

![](/api/attachments/MGTY3DRZ/fulltext/images/b02b1c9cce4ac37986375c9946359991ca1564564218ec70f4ff099a1487c407.jpg)

b  
![](/api/attachments/MGTY3DRZ/fulltext/images/2ddd6e5b3acf4b10ce902415bafe5f99d2eb9d14f00f6cb3e9ad2e4bf5f32e01.jpg)

c  
![](/api/attachments/MGTY3DRZ/fulltext/images/f78dc2e2add1ff56cb06b20c4a0501892b2000eec8d31878a443b280eb0e6f68.jpg)

d  
![](/api/attachments/MGTY3DRZ/fulltext/images/94db28c0b7fe992a4c267819d43ee3faeb7c7f9723e2c3cf51f43d8103d2ad6f.jpg)  
Fig, 3. Disruptive trading on Microsoft stock on 24 Jan, 2013. (a) Multi-order disruptive trading example (grey filled circles) on MSFT stock. (SO: sell order: BO: buy order) The disruptive orders are placed aggressively inside the spread: buy/sell prices higher/lower than the bid/ask. Normal limit orders (red and blue dots) are usually placed on or outside the spread. (b) Sell impulse (SI, transformed sell orders, SO), grey circles represent the disruptive sell impulse sequence. (c) Buy impulse (transformed buy orders) through Eqs. (1)–(6), grey circles represent the disruptive buy impulse sequence. (d) Buy and sell impulses (BI and SI) volumes through Eqs. (1)–(6) grey circles represent the disruptive BI and SI volume. (For interpretation of the references to colour in this figure legend the reader is referred to the web version of this article.)

monitored through the module “Single Order Detection” for singleorder disruptive trading behaviours (Steps 1–3 in Algorithm 1); afterwards, the vector sequence constructed in the sliding window is further monitored by “Order Sequence Detection” for multi-order disruptive behaviours (Steps 4–5 in Algorithm 1). The two components of the hybrid model are trained separately by the historical data before commencing the detection. The design details of the hybrid model are discussed in the following sections.

J. Zhai et al. / Decision Support Systems xxx (2016) xxx–xxx

Algorithm 1. Detection flow of the proposed hybrid detection model in Fig. 5.

<table><tr><td>Step 1:</td><td>For any equity, collect all submitted orders and construct the Limit Order Stream for this equity;</td></tr><tr><td>Step 2:</td><td>Transform the original order stream through the “Order Transform” module based on equation 1-6;Construct the transformed vector  $\delta_i := [\delta_i^p, \delta_i^v, \delta_i^t, \text{DIRECT}_i]^T$ ;</td></tr><tr><td>Step 3:</td><td>Detect each vector  $\delta_i$  through the “Single Order Detection” module for single-order disruptive trading behaviour; if detected, trigger the alert;</td></tr><tr><td>Step 4:</td><td>If not detected, select a sliding window length  $\Theta_T$  and construct a sequence of  $\delta_i$  within the sliding window;</td></tr><tr><td>Step 5:</td><td>Detect the constructed sequence through the “Order Sequence Detection” module; if detected, trigger the alert; if not, update the sliding window with the newest transformed order.</td></tr></table>

## 4.2.1. Single-order disruptive trading detection

A single disruptive order is designed by traders by tuning the quoted price, volume and life cycle of the submitted limit orders, which are usually designed and placed to the market individually with no sequential relations. To detect such types of disruptive orders, the proposed model is to monitor each trading order individually and compare it with historical legitimate trading behaviours to recognise manipulative patterns. If represented through the transformed impulse $\delta _ { i } \colon = [ \delta _ { i } ^ { p } , \delta _ { i } ^ { v } , \delta _ { i } ^ { t } ] ^ { T }$ , as shown in Fig. 3, the disruptive orders are against most of the legitimate trading behaviours. In an anomaly detection area, one-class support vector machine (OCSVM) is one of the most ideal algorithms to provide a direct description of the boundary (the support vectors) between anomalies and normalities [38,26]. OCSVM applied to single-disruptiveorder detection provides a measure of disruptive orders by learning a representation of normal and legitimate trading orders. Therefore, in this paper, OCSVM is proposed as the “Single Order Detection” module in Fig. 5. As discussed in Algorithm 1, the original limit orders are transformed and then used to construct the impulse vector $\delta _ { i } \colon = [ \delta _ { i } ^ { p } , \delta _ { i } ^ { \nu } , \delta _ { i } ^ { t } ,$ DIRECT ]<sup>T</sup>. The OCSVM is trained using the training dataset, a set of the legitimate vector $\delta _ { i } .$ When OCSVM is applied as disruptive order detection, it considers each vector as a single object. Therefore, the “Single Order Detection” module can only monitor the disruptive trading behaviours of a single order.

## 4.2.2. Multi-order disruptive trading detection

Disruptive trading can also be carried out by submitting multiple limit orders to the market as a sequence with no intention of execution. Such order sequences quick sweeting the market induces the market impact by successively aggressive quotes or volumes. The grey points in Fig. 3(b–c) show the behaviours of such a strategy in transformed formats. Detecting such behaviours requires recognising the temporal change among disruptive orders in the sequence. To further identify the trading intentions, we need to determine the strategies capable of generating the observed temporal changes, as well as the probability of the occurrence of the observed temporal changes. A hidden Markov model (HMM) containing two sets of states, observable feature states and hidden mixture component states, can be used to model such cases. These HMM contents are modelled on a standard Markov process on the assumption that they depend solely on previous states. Usually, the application of an HMM can be categorised as belonging to one of two classes; the first is signature modelling, where the detection model is learned from the activities to be recognised, and the activities matching the model are reported as detection outcomes. Examples of this include the coupled behaviour detection in [8], the industry process monitoring in ([7,41], the intrusion detected in [42] and the video surveillance in [24]. The other category of HMM application is anomaly detection, whereby a model of normality is learned solely from the normal activity, and cases tested against the model, with a pre-determined threshold, are declared to be anomalies [42]. In such cases, it is very important that the hidden states be identified and assigned, thereby fulfilling the Markov assumption and allowing the parameter matrices to generate different observed outputs.

![](/api/attachments/MGTY3DRZ/fulltext/images/f0b75d4a18751a451b6e14a02f2f21dc4261aee5632fce45427648e7b2345c0c.jpg)  
Fig. 4. Kernel density of transformed SI and BI on Microsoft on 18 Oct. 2013.

As discussed in the previous section, the detection of disruptive trading behaviours intended to mislead market prices can be framed as an anomaly detection problem, which is to identify new or unknown patterns that have not previously been clarified during the detection model training process (disruptive trading data has not been disclosed in accordance with industry regulations). Utilising the anomaly detection approach requires that the normal patterns be modelled and that an “alarm” be triggered when market activity deviates from those normal patterns. To do this, an improved and adapted HMM with anomaly states has been developed and is presented in the following sections.

4.2.2.1. The multi-variable Gaussian mixture model. Financial data are generally considered to be inherently non-stationary, and so it is accepted that the statistical properties of such data, for example, the mean and variance, vary over time. These variations result from a range of factors, including business and economic cycles and demand/supply microstructures. That makes it particularly interesting when unusual activities are associated with a lack of stationarity in the extracted features, i.e., when the distribution of those extracted features is altered during its existence. This variation can be observed as an outcome of various irregular trading activities; thus, the detection model must have the capacity not only to capture the distributions of the extracted features but also to track shifts in them. Therefore, distribution, followed by sequential data modelling methods, is suggested for the detection model in this section.

An established method for modelling the probability density function (PDF) of a variable is to approximate its (unknown) density using a Gaussian mixture model (GMM) [5]. A GMM is a weighted sum of M-component Gaussian densities as $\begin{array} { r } { p ( { \pmb x } ) = \sum _ { i = 1 } ^ { M } w _ { i } g ( { \pmb x } | \mu _ { i } , { \Sigma } _ { i } ) } \end{array}$ , where x is a D—dimensional continuous-valued data vector, $w _ { i } , i = 1 , \ldots , M ,$ are mixture weights, and $g ( { \pmb x } | \mu _ { i } , \Sigma _ { i } ) , i = 1 , \dots , M ,$ , are component Gaussian densities, wherein $\mu _ { i }$ and $\Sigma _ { i }$ are the mean and covariance matrix for each component, respectively. Each component density is a D—variate Gaussian function. To capture the temporal changes of the multi-order disruptive trading features, we construct and calculate two intuitive features that are associated with the patterns of multi-order trading behaviours; this is defined as the change rate of δ<sup>p</sup> and δ<sup>v</sup> with respect to the lifecycle of the order: $\hat { \boldsymbol \delta } _ { i } : = [ \hat { \boldsymbol \delta } _ { i } ^ { p } , \hat { \boldsymbol \delta } _ { i } ^ { v } ]$ , where $\begin{array} { r } { \hat { \boldsymbol \delta } _ { i } ^ { p } = \frac { \delta _ { i } ^ { p } } { \delta _ { i } ^ { t } } } \end{array}$ and $\begin{array} { r } { \hat { \boldsymbol { \delta } } _ { i } ^ { \nu } = \frac { \delta _ { i } ^ { \nu } } { \delta _ { i } ^ { t } } . } \end{array}$ . In the

J. Zhai et al. / Decision Support Systems xxx (2016) xxx–xxx

Table 2  
KPSS test of original and transformed ask and bid prices on MSFT stock (24 Jan. 2013).

<table><tr><td rowspan="2">Lags</td><td colspan="4">Original ask and bid</td><td colspan="5">Transformed ask and bid</td></tr><tr><td>h</td><td>p Value (ask &amp; bid)</td><td>Test statistics (ask)</td><td>Test statistics (bid)</td><td>h</td><td>p value (ask)</td><td>Test statistics (ask)</td><td>p value (bid)</td><td>Test statistics (bid)</td></tr><tr><td>816</td><td>1</td><td>0.01</td><td>3.0415</td><td>2.2270</td><td>0</td><td>0.1</td><td>0.0499</td><td>0.0207</td><td>0.1876</td></tr><tr><td>817</td><td>1</td><td>0.01</td><td>3.0378</td><td>2.2261</td><td>0</td><td>0.1</td><td>0.0500</td><td>0.0208</td><td>0.1873</td></tr><tr><td>818</td><td>1</td><td>0.01</td><td>3.0341</td><td>2.2252</td><td>0</td><td>0.1</td><td>0.0501</td><td>0.0209</td><td>0.1871</td></tr><tr><td>819</td><td>1</td><td>0.01</td><td>3.0304</td><td>2.2244</td><td>0</td><td>0.1</td><td>0.0501</td><td>0.0210</td><td>0.1868</td></tr><tr><td>820</td><td>1</td><td>0.01</td><td>3.0268</td><td>2.2235</td><td>0</td><td>0.1</td><td>0.0502</td><td>0.0211</td><td>0.1865</td></tr></table>

interest of detecting unusual distributions of $\cdot \hat { \boldsymbol \delta } _ { i } ^ { p }$ and $\hat { \boldsymbol \delta } _ { i } ^ { v } ,$ , the joint PDF of $\hat { \boldsymbol \delta } _ { i } ^ { p }$ and $\hat { \boldsymbol \delta } _ { i } ^ { v }$ are modelled using GMM. Figure shows an example of the joint PDF of $\hat { \delta } _ { i } ^ { p }$ and $\hat { \delta } _ { i } ^ { v }$ of MSFT stock. The joint PDF of buy (BI) and sell (SI) orders are constructed as in Figure (a) and (b), respectively, and show distinct distributions, which are also observed in Fig. 4 where the buy and sell impulses are distributed apart in separated sides along the zero point. Therefore, the buy and sell behaviours are modelled separately.

We also illustrate the reported disruptive trading cases of MSFT stock (represented in Fig. 3) in Fig. 6(a, c), and on the contours of the joint PDFs in Fig. 8. The disruptive trading cases (red circles in Fig. 6(a, c)) lie on the edge areas of the two distributions. However, among the mass of normal trading data generated everyday around the world, only a small percentage is related to disruptive trading activities. The reported cases are even fewer due to the regulatory rules discussed in Section 4.2. To effectively overcome the imbalanced dataset of disruptive and legitimate trading cases and identify the distribution of the disruptive trading cases, we follow the traditional hybrid SMOTE-RUS approach that combines the widely used over-sampling algorithm SMOTE [13] and under-sampling algorithm RUS together [34]. To achieve a reasonably balanced ratio in the dataset, the SMOTE algorithm is slightly revised by taking each minority class example and randomly generating M synthetic examples along the line segments joining all other examples in the minority class. Each of the M synthetic examples is generated following the traditional SMOTE approach. Fig. 6 illustrates an example of the SMOTE-RUS approach on

![](/api/attachments/MGTY3DRZ/fulltext/images/fce45db0752e8a305322fdb5c58aefbf730118484351dc260308d681db7660ab.jpg)  
Fig. 5. The detection flow employing the proposed hybrid model for single- and multiple-order disruptive trading behaviours.

![](/api/attachments/MGTY3DRZ/fulltext/images/dbc8c1a7cc2f4c32c5e6675e905f3f0b05407c23106a63c6c72901286a5b8d55.jpg)  
Fig. 6. The joint PDF of $\cdot \hat { \delta } _ { i } ^ { p }$ (SI and BI rate) and $\hat { \delta } _ { i } ^ { \nu }$ of MSFT stock.  
Please cite this article as: J. Zhai, et al., Computational intelligent hybrid model for detecting disruptive trading activity, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.09.003

![](/api/attachments/MGTY3DRZ/fulltext/images/f9f12212e0214887696a2de1ac42bcf477e68fffcf932d1085be51979b4a3524.jpg)  
(a)

![](/api/attachments/MGTY3DRZ/fulltext/images/ed82f5862d369f82fb712ac13f45888425a8701c17d81f79891c7c378acde00d.jpg)  
(b)

![](/api/attachments/MGTY3DRZ/fulltext/images/f55593ced6c24f955ec2bb70d15724d9ddf6dafbe27c12c6ffc7f0b89eb11734.jpg)  
(c)

![](/api/attachments/MGTY3DRZ/fulltext/images/eb4b4a71962a7194ebd832111b236f24d5747505abd6721939410e6e9abdf4f3.jpg)  
(d)  
Fig. 7. (a) Buy side MSFT trading data from 9:00–12:00 am on 24 Jan. 2013 with a 15:20,000 ratio of disruptive (red circles) and normal (blue dots) trading data; (b) data examples generated by the hybrid SMOTE-RUS approach on the data in (a) with a 0.95:1 ratio of disruptive (red circles) and normal examples: (c) sell side MSFT trading data from 9:00– 12:00 am on 24 Jan. 2013 with a 15:20,000 ratio of disruptive (red) and normal (blue dots) trading data; (d) data examples generated by the hybrid SMOTE-RUS approach with a 0.96:1 ratio of minority (red circles and red dots) and majority (blue dots). (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

the MSFT stock dataset in a short time interval. 30 reported disruptive examples are represented as red circles in Fig. 6 as 15 disruptive sell orders in (a) and 15 disruptive buy orders in (c) with 20,000 normal examples. If the expected ratio is 1:1 on both the buy and sell sides, the normal examples can be under-sampled by 10% to $N _ { 2 } = 2 0 0 0$ , and the disruptive examples can be over-sampled by taking $M = 1 8$ to contain $N _ { 1 } * \frac { ( N _ { 1 } - 1 ) } { 2 } * M + N _ { 1 } = 1 9 0 5$ examples as in the illustration in Fig. 6(b, d). Therefore, the hybrid approach generates a dataset with a 1905 :2000 =0.95: 1 ratio of minority and majority. Training a model on such a balanced dataset would obviously result in unbiased performance. In addition, the joint PDF of the balanced data illustrated in Fig. 6(b) and (d) are then constructed by GMM, as shown in Fig. 6.

4.2.2.2. HMM-based model. As shown in Fig. 7, we construct the joint PDF of normal and disruptive trading behaviours separately using GMM, and the two PDFs are represented as $P _ { N }$ (normal) and $P _ { D }$ (disruptive). We setup the probability thresholds for $P _ { N }$ (normal) and $P _ { D }$ (disruptive) following the heuristic method usually applied in a one-class support vector machine (OCSVM) [38], where the threshold is generally set to include most (for example, 99%) but not all training data to avoid a high misdetection rate. For $P _ { N } ,$ the probability threshold $\theta _ { P _ { N } }$ is set as 99% of the lowest cumulative probability $P _ { N } ^ { m i n }$ of normal trading examples. In other words, the data F are accepted as normal when $P _ { N } ( F _ { t } ) \geq$ 99% $\cdot P _ { N } ^ { m i n }$ . Similarly, for $P _ { D } ,$ the threshold $\theta _ { P _ { D } }$ is set as 99% of the lowest cumulative probability of disruptive trading examples. The 1% outlying values are not simply taken as abnormalities but are used to generate the states for the HMM. By this, two thresholds provide a simplified and joint state view of the two sequential time series $\hat { \delta } _ { i } ^ { p }$ and $\hat { \boldsymbol \delta } _ { i } ^ { v } .$ . Thus, the two joint PDFs can be divided into three states, as in the example shown in Fig. 8(a), one of which (blue area, $P _ { N } ( F _ { t } ) { \ge } 9 9 \% * P _ { N } ^ { m i n } )$ corresponds to the normal trading behaviours, another (red area, $P _ { D } ( F _ { t } ) \geq$ $9 9 \% * P _ { D } ^ { m i n } )$ is disruptive trading behaviours, and the remaining area (white, $P _ { N } ( F _ { t } ) < 9 9 \% * P _ { N } ^ { m i n } { \mathrm { ~ o r ~ } } P _ { D } ( F _ { t } ) < 9 9 \% * P _ { D } ^ { m i n } )$ is correlated with the suspicious trading behaviours, which is neither normal nor disruptive by itself. Because a single disruptive trade may afterwards imply disruptive behaviours, the determination of multi-order disruptive trading depends on other behaviours in a sequence. (See Fig. 3)

To determine the legitimacy of a sequence of trading behaviours, we designate two hidden states representing latent normal and disruptive intentions. Therefore, the hidden Markov model, HMM, is designed as in Fig. 8(b). The state that satisfies $P _ { N } ( F _ { t } ) \ge 9 9 \% * P _ { N } ^ { m i n }$ (the blue area of normality in Fig. 8(b)) is considered to be a completely normal hidden state, while the state that satisfies $P _ { D } ( F _ { t } ) \ge 9 9 \% * P _ { D } ^ { m i n }$ (the red area of disruptiveness in Fig. 8(b)) is thus defined as a hidden disruptive state, and the other states satisfy either $P _ { N } ( F _ { t } ) < 9 9 \% * P _ { N } ^ { m i n }$ or $P _ { D } ( F _ { t } ) < 9 9 \% * P _ { D } ^ { m i n }$ (white suspicious but not deterministic area in Fig. 8(b)). This HMM design presents an efficient means of modelling the limit order streams, and in this context, the observed temporal dynamics of the trading behaviours are simply represented as the hidden state transitions as shown in Fig. 8(b). The fundamental property of this design utilises the inference features of HMM, which could answer two key questions: 1) what is the most likely sequence of hidden states to generate the observed sequence (what is the latent intention given a certain observed trading sequence), and 2) what is the probability of an observed

![](/api/attachments/MGTY3DRZ/fulltext/images/695a6793dd081f2ab6ebb9a9fdbebd0a7e99c3a9dfd82ba4886a2419111f6ecc.jpg)  
Fig, 9. (a) Example of states of observed trading behaviours: (b) structure of the designed hidden Markoy model with disruptive states

J. Zhai et al. / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/MGTY3DRZ/fulltext/images/6662f1fd5087234b8a6d32d5d4a3cd0848ee0f76c647f37e526e12675d91889a.jpg)  
(a)

![](/api/attachments/MGTY3DRZ/fulltext/images/a6130fe380ea414b70965ca50e11a05dba2a46ff73fab6997c15fe33a75c57ff.jpg)  
(b)  
Fig. 8. The contour of the joint PDF of the under-sampled normal trading data (in Fig. 6) and the over-sampled disruptive trading cases by the SMOTE-RUS approach

sequence (how likely are we to observe a specific trading sequence)? HMM provides answers to the two questions by determining the sequence of hidden states most likely generating the observations sequences and the occurrence probability of the observed sequence based on the transition and emission probability matrix constructed during the training process. Those answers can be used as a measure of disruptive trading behaviours.

## 4.2.3. Adaptive mechanism

The financial time series is non-stationary. Although the nonstationary nature of the transformed impulse $[ \delta _ { i } ^ { p } , \delta _ { i } ^ { \nu } , \delta _ { i } ^ { t } ] ^ { \bar { T } }$ is reduced based on the test results in Tables 2–4, the mean and variance of the constructed joint PDFs may be subiect to variation over time. To mitigate the non-stationarity, the proposed detection model is augmented with an adaptive mechanism. The detection models, OCSVM for single-order and HMM for multi-order disruptive behaviours, are trained using data in a sliding window of length w. During the process of disruptive trading behaviour detection, the window slides forward and maintains the closest w data points, and the OCSVM and HMM are updated if any meaningful differences between the w data points in the current sliding window and prior training data are found. The Mann–Whitney U test (MWW) [21], a nonparametric test of the null hypothesis that two samples come from the same population, is used to identify a deviation between the two data sequences. MWW can be applied on an unknown distribution, contrary to the t-test, which can only be applied on normal distributions, and it is nearly as efficient as the t-test on normal distributions [21]. The MWW is designed as an independent module and is used as a post-processing block of the detection model to identify the significant differences between the updated data sequence in the sliding window and the prior training data sequence. Fig. 9 describes the proposed adaptive mechanism of the proposed model for detecting disruptive trading behaviours. At first, the OCSVM and HMM are trained separately by differently calculated features from w data points in the training window, $t _ { w 1 , } t { \in } [ t _ { 0 } , t _ { w - 1 } ] ,$ where $t _ { 0 }$ and $t _ { w - }$ are the starting and ending time points, respectively. OCSVM uses $\delta _ { i } \colon = [ \delta _ { i } ^ { p } , \delta _ { i } ^ { \nu } , \delta _ { i } ^ { t } , \mathrm { D I R E C T _ { i } } ] ^ { T } ,$ , and HMM uses $\hat { \boldsymbol { \delta } } _ { i } : = [ \hat { \boldsymbol { \delta } } _ { i } ^ { p } , \hat { \boldsymbol { \delta } } _ { i } ^ { v } ] ^ { T }$ . For OCSVM, the first testing sample is the trading order $\delta _ { i } , i = t _ { w } ,$ and for HMM, the first testing sequence is constructed as $t _ { s 1 , } \ t \in [ t _ { w } , t _ { w - 1 } ]$ Two models detect the first test case; if this is assessed as normal, the training sliding window is slid to $t _ { w 2 , t } \in [ t _ { L } , t _ { w + L - 1 } ]$ for significant difference testing by MWW. If a significant change is detected, both the OCSVM and the HMM model are re-trained by the data in $t _ { w 2 }$ , and if not, the test case for OCSVM is updated as the trading order $\delta _ { i } , i = t _ { w + 1 }$ and the test sequence for the HMM is then updated into the window $t _ { s 2 , } t \in [ t _ { w + 1 } , t _ { w + L } ] .$ The length of the testing sequence $\theta _ { T }$ in Fig. 5 is then set equal to the length of $t _ { s 1 }$ and $t _ { s 2 } .$ The training window in our proposed mechanism is set to a single day because the disruptive trading actions are usually completed within a short time period as intraday activities, and setting the window to one single day is enough to cover the data features for training the detection model.

## 4.2.4. The detection algorithm

As per the discussion in Section 4.2, Algorithm 1 provides a complete structure of the workflow of the detection algorithm. The steps of the “Single Order Detection” and “Order Sequence Detection” modules together with the “Adaptive Mechanism” module are summarised in Algorithms 2 and 3, respectively, below. Therefore, the disruptive trading behaviour hybrid detection model is constructed by Algorithms 1–3.

Please cite this article as: J. Zhai, et al., Computational intelligent hybrid model for detecting disruptive trading activity, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.09.003

J. Zhai et al. / Decision Support Systems xxx (2016) xxx–xxx

Algorithm 2. Workflow of the proposed “Single Order Detection” and “Adaptive Mechanism” module in Fig. 5.

<table><tr><td>Step 1:</td><td>Select a historical date and construct the training dataset of the transformed vector  $\delta_{i}, i = 1, ..., \Theta$ ;</td></tr><tr><td>Step 2:</td><td>Train the OCSVM using the constructed training dataset;</td></tr><tr><td>Step 3:</td><td>Detect the most updated incoming vector using the trained OCSVM;</td></tr><tr><td>Step 4:</td><td>If OCSVM triggers a disruptive trading alert, the most updated vector is stored in the disruptive trading dataset;</td></tr><tr><td>Step 5:</td><td>If no disruptive trading alert is triggered, the training dataset is slid forward to include the most updated vector and is fed into the adaptive mechanism module for a model update check. If a model update is needed, the algorithm flow goes to Step 2.</td></tr><tr><td>Step 6:</td><td>If a model update is not needed, the algorithm flow goes to Step 3.</td></tr></table>

Algorithm 3. Workflow of the proposed “Order Sequence Detection” and “Adaptive Mechanism” module in Fig. 5.

<table><tr><td>Step 1:</td><td>Select a historical date and construct the training dataset of the transformed vector  $\delta_{i}$ ;</td></tr><tr><td>Step 2:</td><td>Calculate and construct the training dataset of  $\hat{\delta}_{i} := [\hat{\delta}_{i}^{p}, \hat{\delta}_{i}^{v}]^{T}$ ;</td></tr><tr><td>Step 3:</td><td>Collect all known disruptive trading records on the selected financial instrument and construct the dataset of the transformed disruptive vector  $\delta_{i,disrupt}$ ;</td></tr><tr><td>Step 4:</td><td>Calculate and construct the training dataset of  $\hat{\delta}_{i,disrupt} := [\hat{\delta}_{i,disrupt}^{p}, \hat{\delta}_{i,disrupt}^{v}]^{T}$ ;</td></tr><tr><td>Step 5:</td><td>Apply Algorithm 2 on the dataset of  $\hat{\delta}_{i,disrupt}$  and construct the over-sampled dataset of  $\hat{\delta}_{i,disrupt,over}$ ;</td></tr><tr><td>Step 6:</td><td>Calculate the joint PDF of vectors  $\hat{\delta}_{i}$  and  $\hat{\delta}_{i,disrupt,over}$  using GMM;Set the corresponding thresholds for two joint PDFs;Construct the hidden and observed states according to the discussion in Section 4.2.2.2 and the illustrations in Figure 7 and Figure 8;</td></tr><tr><td>Step 7:</td><td>Train the HMM using the constructed vectors and states;</td></tr><tr><td>Step 8:</td><td>For a constructed testing sequence  $\Theta_{T}$ , detect disruptive behaviours via the trained HMM model;</td></tr><tr><td>Step 9:</td><td>If HMM triggers a disruptive trading alert, the corresponding vectors are stored in the disruptive trading dataset; the algorithm flow goes to Step 5;</td></tr><tr><td>Step 10:</td><td>If no alert is triggered, the training dataset is slid forward to include the most updated vector and is fed into the adaptive mechanism module for a model update check. If a model update is needed, the algorithm flow goes to Step 2;</td></tr><tr><td>Step 11:</td><td>If a model update is not needed, the testing sequence is slid forward to include the most updated vector, and the algorithm flow goes to Step 8;</td></tr></table>

## 4.3. Experimental evaluation

A large amount of labelled examples of both normal and disruptive trading data are commonly used in evaluating a detection model. However, given the lack of genuine market data of disruptive trading behaviour, a slightly adapted approach is taken in this case. To evaluate the proposed detection model, the characteristics of the disruptive trading behaviours have been studied, synthetically generated, and then injected into the financial time-series data. Meanwhile, statistical features such as mean, variance and volatility are all maintained.

![](/api/attachments/MGTY3DRZ/fulltext/images/d445be61a7c040aef1d86e3b2808445b4b2e954222c1f9e5a7367719db3a01fd.jpg)  
Fig. 10. The training and testing mechanism of the multi-order disruptive trading behaviour detection model

## 4.3.1. The experimental setup

In this paper, experimental evaluation is conducted using genuine market data from four representative stocks: Google, Microsoft, Intel and Apple from the NASDAQ. These datasets were chosen because they have relatively high trading volumes and price volatility, which are elements likely to induce manipulation across exchanges [15]; thus, they are at greater risk of manipulation than many others. The dataset covers tick trading data over the entire year of 2013, and the data in every trading day comprises approximately 400,000 samples for each stock. The dataset for each selected stock contains more than 10 Gigabytes of data. All of the datasets have been examined by the authors' expert financial partners to ensure that none of them are related to any cases of disruptive behaviour that have been reported to the regulatory authorities. The experiments are designed by reproducing the reported examples and then injecting them into the dataset of corresponding stocks, which means that the test data becomes a mix of both normal and anomalous patterns. The trained models are then applied to that mixed data to identify patterns associated with disruptive behaviours. This approach is of acknowledged value to the industry,

J. Zhai et al. / Decision Support Systems xxx (2016) xxx–xxx

Group 1: ROC of Hybrid,LR,kNN,GMM on GOOG  
![](/api/attachments/MGTY3DRZ/fulltext/images/09641f8a882653bc97c46ac17bf6434dd8916b7ef4beca719c932318f7154902.jpg)  
Group 1: ROC of Hybrid,LR,kNN,GMM on INTL

Group 1: ROC of Hybrid,LR,kNN,GMM on MSFT  
![](/api/attachments/MGTY3DRZ/fulltext/images/9386b0a19c3ad3e88ea5d23302e1c28387c77c32254cea4706fe52591b80ffa0.jpg)  
Group 1: ROC of Hybrid,LR,kNN,GMM on APPA

![](/api/attachments/MGTY3DRZ/fulltext/images/81400dabe7964586ccbc1ff01a33c2719b00770913b754b0dbaf8a86c483b520.jpg)

![](/api/attachments/MGTY3DRZ/fulltext/images/3de3d9b7a867d921605cb0c28ba79a0b8ff33367d06bd024a7ea01b8199fcbc9.jpg)  
Fig. 11. The ROC curves of Group 1 experiments: four models applied on four datasets to detect single-order-based disruptive trading behaviours.

Group 2: ROC of Hybrid,LR,kNN,GMM on GOOG  
![](/api/attachments/MGTY3DRZ/fulltext/images/175a58345489a226a6df11175c6b9f492ff08de422ce82db603ee2993da4cfa3.jpg)

Group 2: ROC of Hybrid,LR,kNN,GMM on MSFT  
![](/api/attachments/MGTY3DRZ/fulltext/images/81b8d678e8be1fdd06a67e304918f309a7a11f82b53c26fd12a8324625a10ea5.jpg)

Group 2: ROC of Hybrid,LR,kNN,GMM on INTL  
![](/api/attachments/MGTY3DRZ/fulltext/images/f1e5ac7ff4dcbe92ea90e140a44764ce81b2f817e5671f03e69b6e37ed8684ed.jpg)

Group 2: ROC of Hybrid,LR,kNN,GMM on APPA  
![](/api/attachments/MGTY3DRZ/fulltext/images/5378dc7fe19a495d619801f849c879d13d42f3b1857160e0647a92c0015b68d8.jpg)  
Fig. 12. The ROC curves of Group 2 experiments: four models applied on four datasets to detect multi-order-based disruptive trading behaviours.

Group 3: ROC of Hybrid,LR,kNN,GMM on GOOG  
![](/api/attachments/MGTY3DRZ/fulltext/images/5b52182e4cf1b9de882567327626aea63384e33590f6decf989f8a0959b04ddc.jpg)

Group 3: ROC of Hybrid,LR,kNN,GMM on MSFT  
![](/api/attachments/MGTY3DRZ/fulltext/images/c2d55ca9b5a7ac7537f27903b1972ed8a2c2327621a0adaa2aa24b043e4eba98.jpg)

Group 3: ROC of Hybrid,LR,kNN,GMM on INTL  
![](/api/attachments/MGTY3DRZ/fulltext/images/12b473768e21d8b214b797abf22f3316b9bced90b125f9f3ca8467396d862051.jpg)

Group 3: ROC of Hybrid,LR,kNN,GMM on APPA  
![](/api/attachments/MGTY3DRZ/fulltext/images/fd7a2c80d1ef336c05bd3d0e88c14a1a39fd44b4101ca65fabe891d738da02c7.jpg)  
Fig, 13. The ROC curves of Group 3 experiments: four models applied on four datasets to detect mixed disruptive trading behaviours based on single and multiple orders

Please cite this article as: J. Zhai, et al., Computational intelligent hybrid model for detecting disruptive trading activity, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.09.003

Table 3  
KPSS test of original and transformed order volumes on MSFT stock (24 Jan. 2013).

<table><tr><td rowspan="2">Lags</td><td colspan="3">Original order volume</td><td colspan="3">Transformed order volume</td></tr><tr><td>h</td><td>p value</td><td>Test statistics</td><td>h</td><td>p value</td><td>Test statistics</td></tr><tr><td>816</td><td>1</td><td>0.01</td><td>13.3388</td><td>1</td><td>0.01</td><td>0.1326</td></tr><tr><td>817</td><td>1</td><td>0.01</td><td>13.3288</td><td>1</td><td>0.01</td><td>0.1315</td></tr><tr><td>818</td><td>1</td><td>0.01</td><td>13.3188</td><td>1</td><td>0.01</td><td>0.1315</td></tr><tr><td>819</td><td>1</td><td>0.01</td><td>13.3088</td><td>1</td><td>0.01</td><td>0.1314</td></tr><tr><td>820</td><td>1</td><td>0.01</td><td>13.2989</td><td>1</td><td>0.01</td><td>0.1313</td></tr></table>

particularly given the huge expense involved in isolating genuine trading cases. The experiments are therefore designed in three groups:

Group 1: The single-order disruptive trading behaviour in Fig. 1 is reproduced in the datasets of the selected stocks using original characteristics discussed in Section 3.1. Five hundred examples are reproduced and injected in four datasets.

Group 2: Five hundred examples of the multi-order disruptive trading behaviour in Fig. 2 are reproduced and injected in four datasets.

Group 3: Five hundred examples of mixed disruptive behaviours (half by single-order and half by multi-order) are reproduced and injected in four datasets.

The adaptive mechanism has a sliding window set to a length of one day since the disruptive trading behaviours usually target intra-day transactions to make a profit. Therefore, the genuine market trading data from 2 Jan. 2013, the first trading day of 2013, was collected as the initial training dataset. The 400,000-point training dataset is partitioned into five equal-sized subsets. The crossvalidation is then repeated five times. Each time, one single subset is retained as the testing dataset, and the remaining four subsets are used as the training data. The five results from the crossvalidation are then averaged to produce a stable trained model. The experiments are designed as an on-line real-time detection scheme. After the model is initially trained, the data are fed into the model sequentially as an order time series. The model detects and reports the disruptive behaviour according to the detection flow illustrated in Fig. 5 and is re-trained and updated according to the calculations of the adaptive mechanism represented in Fig. 9.

As shown in the literature review of this paper, some generic computational models have already been applied to the problem of detecting similar disruptive patterns; these include k-nearest neighbour (kNN), Gaussian MM and logistic regression (LR) approaches [2,36, 17]. The three popular computational models are selected as benchmarks for evaluating the proposed model and are applied on the data sequence in the same scheme as the proposed model. The three benchmark models are fine-tuned through the application of five-fold crossvalidation on each different dataset to ensure the stability and quality of the results. The basic accuracy measures, precision, recall, F measure and G measure, as well as the ROC curve and AUC, are used as performance measures for the evaluation.

## Table 4

KPSS test of original and transformed order lifecycles on MSFT stock (24 Jan. 2013)

<table><tr><td rowspan="2">Lags</td><td colspan="3">Original lifecycle</td><td colspan="3">Transformed lifecycle</td></tr><tr><td>h</td><td>p value</td><td>Test statistics</td><td>h</td><td>p value</td><td>Test statistics</td></tr><tr><td>816</td><td>1</td><td>0.01</td><td>18.3574</td><td>1</td><td>0.01</td><td>0.1651</td></tr><tr><td>817</td><td>1</td><td>0.01</td><td>16.6305</td><td>1</td><td>0.01</td><td>0.1524</td></tr><tr><td>818</td><td>1</td><td>0.01</td><td>15.3079</td><td>1</td><td>0.01</td><td>0.1416</td></tr><tr><td>819</td><td>1</td><td>0.01</td><td>14.0220</td><td>1</td><td>0.01</td><td>0.1321</td></tr><tr><td>820</td><td>1</td><td>0.01</td><td>13.5401</td><td>1</td><td>0.01</td><td>0.1239</td></tr></table>

## Table 5

Recall, precision, F measure and G score of the Group 1 experimental results for four models on four datasets. Bold font represents the best performance.

<table><tr><td colspan="2"></td><td>Recall</td><td>Precision</td><td>F measure</td><td>G score</td></tr><tr><td rowspan="4">APPA</td><td>Hybrid</td><td>0.9717</td><td>0.9749</td><td>0.9733</td><td>0.9733</td></tr><tr><td>kNN</td><td>0.8902</td><td>0.9528</td><td>0.9204</td><td>0.9210</td></tr><tr><td>GMM</td><td>0.8221</td><td>0.9336</td><td>0.8743</td><td>0.8761</td></tr><tr><td>LR</td><td>0.8210</td><td>0.8938</td><td>0.8559</td><td>0.8567</td></tr><tr><td rowspan="4">GOOG</td><td>Hybrid</td><td>0.9801</td><td>0.9699</td><td>0.9750</td><td>0.9750</td></tr><tr><td>kNN</td><td>0.9046</td><td>0.9494</td><td>0.9264</td><td>0.9267</td></tr><tr><td>GMM</td><td>0.9020</td><td>0.9505</td><td>0.9256</td><td>0.9259</td></tr><tr><td>LR</td><td>0.8020</td><td>0.9225</td><td>0.8580</td><td>0.8601</td></tr><tr><td rowspan="4">INTL</td><td>Hybrid</td><td>0.9648</td><td>0.9847</td><td>0.9746</td><td>0.9747</td></tr><tr><td>kNN</td><td>0.8937</td><td>0.9546</td><td>0.9231</td><td>0.9236</td></tr><tr><td>GMM</td><td>0.8639</td><td>0.9514</td><td>0.9055</td><td>0.9066</td></tr><tr><td>LR</td><td>0.8490</td><td>0.9402</td><td>0.8923</td><td>0.8934</td></tr><tr><td rowspan="4">MSFT</td><td>Hybrid</td><td>0.9678</td><td>0.9742</td><td>0.9710</td><td>0.9710</td></tr><tr><td>kNN</td><td>0.8968</td><td>0.9672</td><td>0.9307</td><td>0.9314</td></tr><tr><td>GMM</td><td>0.8833</td><td>0.9321</td><td>0.9070</td><td>0.9074</td></tr><tr><td>LR</td><td>0.8200</td><td>0.9100</td><td>0.8626</td><td>0.8638</td></tr></table>

## 4.3.2. Results of experimental assessment

The precision, recall, F and G measure for the four models on four different datasets are represented in Tables 5–7. From all of the experiments in the three groups, we can observe that the proposed hybrid model achieved stable and constantly better performances then all other benchmark models in terms of recall, precision, F and G measures.

As a further performance measure, the ROC curves of the proposed hybrid model and three benchmark models, applied to four stock datasets with ten thousand disruptive examples injected, are shown in Figs. 10–13 The corresponding AUC values are summarised in Tables 8–10. The proposed hybrid model achieved the highest AUC values in all experiments and outperformed all other benchmark models in all datasets with different types of disruptive examples.

The best AUC value of the hybrid model appeared on the MSFT dataset with mixed disruptive examples (0.9516 as in Table 10), which is 17.24%, 21.79% and 24.40% higher than the kNN (0.8116), GMM (0.7813) and LR (0.7649) models, respectively. The lowest AUC value of the hybrid model was achieved on the GOOG dataset with mixed disruptive examples (0.8988 as in Table 10), yet even this is substantially higher (14.79%, 14.18% and 13.17%) than the performance of the kNN (0.7830), GMM (0.7872) and LR (0.7942) models, respectively.

The comparison of the models' performances reveals that the proposed hybrid model sustains superior performance than that of all other models over four market datasets on three groups of experiments. These results also shed light on the performance characteristics of the benchmark models and, in particular, their performance stabilities:

## Table 6

Recall, precision, F measure and G score of the Group 2 experimental results for four models on four datasets. Bold font represents the best performance.

<table><tr><td colspan="2"></td><td>Recall</td><td>Precision</td><td>F measure</td><td>G score</td></tr><tr><td rowspan="4">APPA</td><td>Hybrid</td><td>0.9468</td><td>0.9682</td><td>0.9574</td><td>0.9574</td></tr><tr><td>kNN</td><td>0.8510</td><td>0.9327</td><td>0.8900</td><td>0.8909</td></tr><tr><td>GMM</td><td>0.8663</td><td>0.9448</td><td>0.9038</td><td>0.9047</td></tr><tr><td>LR</td><td>0.8700</td><td>0.9275</td><td>0.8978</td><td>0.8983</td></tr><tr><td rowspan="4">GOOG</td><td>Hybrid</td><td>0.9705</td><td>0.9678</td><td>0.9692</td><td>0.9692</td></tr><tr><td>kNN</td><td>0.8077</td><td>0.9394</td><td>0.8685</td><td>0.8710</td></tr><tr><td>GMM</td><td>0.8802</td><td>0.9468</td><td>0.9123</td><td>0.9129</td></tr><tr><td>LR</td><td>0.8700</td><td>0.9242</td><td>0.8963</td><td>0.8967</td></tr><tr><td rowspan="4">INTL</td><td>Hybrid</td><td>0.9725</td><td>0.9805</td><td>0.9765</td><td>0.9765</td></tr><tr><td>kNN</td><td>0.8299</td><td>0.9425</td><td>0.8826</td><td>0.8844</td></tr><tr><td>GMM</td><td>0.8903</td><td>0.9473</td><td>0.9179</td><td>0.9184</td></tr><tr><td>LR</td><td>0.8702</td><td>0.9381</td><td>0.9029</td><td>0.9035</td></tr><tr><td rowspan="4">MSFT</td><td>Hybrid</td><td>0.9883</td><td>0.9832</td><td>0.9857</td><td>0.9858</td></tr><tr><td>kNN</td><td>0.8610</td><td>0.9561</td><td>0.9061</td><td>0.9073</td></tr><tr><td>GMM</td><td>0.8737</td><td>0.9468</td><td>0.9088</td><td>0.9095</td></tr><tr><td>LR</td><td>0.8490</td><td>0.9003</td><td>0.8739</td><td>0.8743</td></tr></table>

Table 7  
Recall, precision, F measure and G score of the Group 3 experimental results for four models on four datasets. Bold font represents the best performance

<table><tr><td colspan="2"></td><td>Recall</td><td>Precision</td><td>F measure</td><td>G score</td></tr><tr><td rowspan="4">APPA</td><td>Hybrid</td><td>0.9203</td><td>0.9809</td><td>0.9497</td><td>0.9501</td></tr><tr><td>kNN</td><td>0.8578</td><td>0.9570</td><td>0.9047</td><td>0.9061</td></tr><tr><td>GMM</td><td>0.8357</td><td>0.9339</td><td>0.8821</td><td>0.8834</td></tr><tr><td>LR</td><td>0.8300</td><td>0.9057</td><td>0.8662</td><td>0.8670</td></tr><tr><td rowspan="4">GOOG</td><td>Hybrid</td><td>0.9381</td><td>0.9758</td><td>0.9566</td><td>0.9568</td></tr><tr><td>kNN</td><td>0.8240</td><td>0.9150</td><td>0.8671</td><td>0.8683</td></tr><tr><td>GMM</td><td>0.8079</td><td>0.9105</td><td>0.8562</td><td>0.8577</td></tr><tr><td>LR</td><td>0.8188</td><td>0.9221</td><td>0.8674</td><td>0.8689</td></tr><tr><td rowspan="4">INTL</td><td>Hybrid</td><td>0.9817</td><td>0.9706</td><td>0.9761</td><td>0.9761</td></tr><tr><td>kNN</td><td>0.8450</td><td>0.9251</td><td>0.8833</td><td>0.8842</td></tr><tr><td>GMM</td><td>0.8213</td><td>0.9452</td><td>0.8789</td><td>0.8811</td></tr><tr><td>LR</td><td>0.8600</td><td>0.8872</td><td>0.8734</td><td>0.8735</td></tr><tr><td rowspan="4">MSFT</td><td>Hybrid</td><td>0.9671</td><td>0.9889</td><td>0.9779</td><td>0.9779</td></tr><tr><td>kNN</td><td>0.8928</td><td>0.9301</td><td>0.9110</td><td>0.9112</td></tr><tr><td>GMM</td><td>0.8211</td><td>0.9135</td><td>0.8648</td><td>0.8661</td></tr><tr><td>LR</td><td>0.8400</td><td>0.9048</td><td>0.8712</td><td>0.8718</td></tr></table>

the k-NN, GMM and LR models exhibited volatile performance across the various datasets.

Based on the outcome of the experimental evaluation and the performance comparison analysis, it is reasonable to conclude that the proposed hybrid model exhibits performance that is consistently superior to that of the k-NN, GMM and LR models under most of the randomness of the nonstationary nature of the limit order streams and that the hybrid model is better suited to detecting disruptive trading behaviours in a more practical context, where both the single- and multiple-order trading exist. The proposed method identifies potential disruptive trading by taking both anomalies and contextual relationships (through the Markov chain) into account, and such detection increases accuracy. Although it is not particularly designed for real-time surveillance, the proposed hybrid model is also suitable for real-time detection as three groups of experiments are all carried out in an on-line detection scheme.

## 5. Conclusions

This paper presents a hybrid model composed of two primary modules, “Single Order Detection” and “Order Sequence Detection,” which are dedicated to detecting disruptive trading behaviours via single and multiple orders, respectively. Examples of the former format are via carefully designed limit orders that have a large volume or aggressively quoted prices and are usually placed individually and separately to induce the desired effects on the market while minimising risk to the (rogue) traders, while examples of the latter format are via a sequence of limit orders, where the sequential impact on the market can be utilised by the traders for potential profit.

With a view to detecting such activities, the “Single Order Detection” module considers each limit order as a multi-dimensional object and identifies abnormal behaviours by comparison with the normality. The “Single Order Detection” module is based on the concept of a safetycritical monitoring system, whereby the system's normal operations follow a stationary, or at least pseudo-stationary, process and anomalous events happen without warning or preamble and are rare. Training data, which is known to only comprise normal activity, is used to train

## Table 8

The AUC values of Group 1 experiments: four models applied on four datasets to detect single-order-based disruptive trading behaviours. Bold font represents the best performance.

<table><tr><td></td><td>GOOG</td><td>MSFT</td><td>INTL</td><td>APPA</td><td>Avg.</td></tr><tr><td>Hybrid model</td><td>0.9345</td><td>0.9329</td><td>0.9497</td><td>0.9189</td><td>0.9365</td></tr><tr><td>kNN</td><td>0.8317</td><td>0.8985</td><td>0.8775</td><td>0.8979</td><td>0.8764</td></tr><tr><td>GMM</td><td>0.8622</td><td>0.8183</td><td>0.8648</td><td>0.8193</td><td>0.8411</td></tr><tr><td>LR</td><td>0.7692</td><td>0.7620</td><td>0.8477</td><td>0.7401</td><td>0.7798</td></tr></table>

Table 9  
The AUC values of Group 2 experiments: four models applied on four datasets to detect multi-order-based disruptive trading behaviours. Bold font represents the best performance.

<table><tr><td></td><td>GOOG</td><td>MSFT</td><td>INTL</td><td>APPA</td><td>Avg.</td></tr><tr><td>Hybrid model</td><td>0.9272</td><td>0.9592</td><td>0.9499</td><td>0.9171</td><td>0.9384</td></tr><tr><td>kNN</td><td>0.8373</td><td>0.8792</td><td>0.8469</td><td>0.8397</td><td>0.8508</td></tr><tr><td>GMM</td><td>0.8855</td><td>0.8428</td><td>0.8841</td><td>0.8666</td><td>0.8697</td></tr><tr><td>LR</td><td>0.7492</td><td>0.7334</td><td>0.7949</td><td>0.7710</td><td>0.7621</td></tr></table>

a model of normality against which new data are compared to recognise abnormalities.

In contrast, the “Order Sequence Detection” module looks more widely at the temporal contextual relationships between trading sequences. The change rates of the limit order features are jointly modelled using GMM, and a model based on a hidden Markov model (HMM) is proposed for learning behaviours represented by the features. Thresholds are established on those features to allow the extreme values to be used as dummy suspicious states for the HMM, and thus the traditional HMM is extended to comprise anomaly states that would not otherwise be attained. To strengthen the model with regard to the non-stationary changes to the financial data, an “adaptive mechanism” module is provided for tracking the status of the learned model and re-training it when required.

The experimental evaluations show clearly that the proposed hybrid model is effective in the detection of disruptive trading behaviours and outperform the selected benchmark models in all experiments. In particular, in experiments with mixed disruptive examples, which reflect practical market conditions, the hybrid model outperforms the benchmark models more clearly.

Although tailor-made for disruptive trading behaviour detection, the proposed hybrid model has the potential for application to other decision-making scenarios, which may require static data as well as dynamic information. For instance, in detecting credit card default, static customer information is widely used in most detection models. However, a sequence of payment statuses, i.e., late payments [27], and other dynamic information of the customer may act in a supplementary manner for determining the customer's future default. The static and dynamic information can be modelled and detected, respectively, by the revised single- and multiple-order detection modules. The proposed hybrid model may also be applied to fraudulent online transaction detection [44], which can consider the transaction to be detected in the context of a sequence of past transactions. Another potential application may lie in detecting abnormal behaviours in social commerce [43].

Despite the proposed approaches, there is sufficient scope for future work. In the hybrid model, an adaptive mechanism compensated for the non-stationary features of the extracted features. However, the retraining processes increased the computational complexity. In practice in a financial market, the rapidly growing trading frequency increased the non-stationarity of the financial time series and at the same time decreased the tolerance of latency for model retraining. However, an increased non-stationarity requires more retraining. To solve this contradictory problem, additional to the adaptive mechanism, a vector transformation method that removes or partially removes the non-stationarity while maintaining the necessary statistical features might be one strand of future work.

## Table 10

The AUC values of Group 3 experiments: four models applied on four datasets to detect mixed disruptive trading behaviours based on single and multiple orders. Bold font represents the best performance.

<table><tr><td></td><td>GOOG</td><td>MSFT</td><td>INTL</td><td>APPA</td><td>Avg.</td></tr><tr><td>Hybrid model</td><td>0.9019</td><td>0.9749</td><td>0.9515</td><td>0.9739</td><td>0.9506</td></tr><tr><td>kNN</td><td>0.7838</td><td>0.8124</td><td>0.8214</td><td>0.8886</td><td>0.8265</td></tr><tr><td>GMM</td><td>0.7878</td><td>0.7819</td><td>0.8989</td><td>0.8282</td><td>0.8242</td></tr><tr><td>LR</td><td>0.7948</td><td>0.7655</td><td>0.7170</td><td>0.6986</td><td>0.7440</td></tr></table>

Please cite this article as: J. Zhai, et al., Computational intelligent hybrid model for detecting disruptive trading activity, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.09.003

## Acknowledgement

This research is partially supported by the National Education Department of China, and the Fujian Province Nature and Science Foundation, P.R. China, project No. 2015J01236.

## References

[1] Aggarwal, G. Wu, Stock market manipulations, The Journal of Business 79 (4) (2006).1915-1953.

[2] M.J. Aitken, F.H. deB. Harris, S. Ji, Trade-based manipulation and market efficiency: a cross-market comparison, Proceeding 22nd Australasian Finance and Banking Conference 2009, p. 18 Sydney.

[3] F. Allen, D. Gale, Stock price manipulation, The Review of Financial Studies 5 (3) (1992) 503–529.

[4] S. Bhattacharyya, S. Jha, K. Tharakunnel, J.C. Westland, Data mining for credit card fraud: a comparative study, Decision Support Systems (February 2011) 602–613.

[5] C.M. Bishop, Pattern Recognition and Machine Learning, Springer, New York, 2006.

[6] T. Bollerslev, Generalized autoregressive conditional heteroskedasticity, Journal of Econometrics 31 (3)(1986) 307-327

[7] S. Bruce, The use of hidden Markov models for anomaly detection in nuclear core condition monitoring, IEEE Transactions on Nuclear Science 56 (2) (April 2009) 453–461.

[8] L. Cao, Y. Ou, P. Yu, Coupled behavior analysis with applications, IEEE Transactions on Knowledge and Data Engineering 24 (8) (August 2012) 1378–1392.

[9] Y. Cao, Li, Coleman, Belatreche, McGinnity, Detecting wash trade in financial market using digraphs and dynamic programming, IEEE Transactions on Neural Network and Learning Systems (2015), http://dx.doi.org/10.1109/TNNLS.2015.2480959.

[10] Y. Cao, Y. Li, S. Coleman, A. Belatreche, M. McGinnity, Adaptive hidden Markov model with anomaly states for price manipulation detection, IEEE Transactions on Neural Networks and Learning Systems (2015) 318–330.

[11] Y. Cao, Y. Li, S. Coleman, A. Belatreche, M.T. McGinnity, Detecting price manipulation in the financial market, Computational Intelligence for Financial Engineering (CIFEr), Proceedings of the IEEE/IAFE, Mar 2014, pp. 77–84 London.

[12] CFTC, Antidisruptive Practices Authority No. 3038-AD96, Commodity Exchange Act Release, May 20 2013.

[13] N.V. Chawla, K.W. Bowyer, L.O. Hall, W.P. Kegelmeyer, SMOTE: synthetic minority over-sampling technique, Journal of Artificial Intelligence Research (2002) 321–357.

[14] CME, Rule 575, August 2014 Retrieved from U.S. Commodity Futures Trading Commision, http://www.cftc.gov/filings/orgrules/rule082814cmedcm001.pdf.

[15] D.J. Cumming, F. Zhan, M.J. Aitken, High frequency trading and end-of-day price dislocation, October 28 2013 Retrieved from Social Science Research Network, http://papers.ssrn.com/sol3/papers.cfm?abstract\_id=2145565.

[16] D. Cumming, S. Johan, D. Li, Exchange trading rules and stock market liquidity, Journal of Financial Economics 99 (3) (March 2011) 651–671.

[17] D. Diaz, B. Theodoulidis, P. Sampaio, Analysis of stock market manipulations using knowledge discovery techniques applied to intraday trade prices, Expert Systems with Applications 38 (15) (September 2011) 12757–12771.

[18] I. Domowitz, Market Abuse and Surveillance, Economic Impact Assessment, Foresight Government Office for Science London 2012

[19] R.F. Engle, Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation, Econometrica 50 (4) (1982) 987–1008.

[20] EU, MiFID II, 2014 Retrieved from European Commission Banking and Finance, http://ec.europa.eu/finance/securities/isd/mifid2/index\_en.htm (,6). (,6).

[21] M.P. Fay, M.A. Proschan, Wilcoxon–Mann–Whitney or t-test? On assumptions for hypothesis tests and multiple interpretations of decision rules, Statistics Surveys (2010) 1-39.

[22] S. Friederich, R. Payne, Computer-based trading and market abuse, Driver Review, Foresight, Government Office for Science, London, 2012.

[23] R. Ghazali, A.J. Hussain, N.M. Nawi, B. Mohamad, Non-stationary and stationary prediction of financial time series using dynamic ridge polynomial neural network, Neurocomputing 72 (10–12) (2009) 2359–2367.

[24] P. Guo, Z. Miao, X.-P. Zhang, Y. Shen, S. Wang, Coupled observation decomposed hidden Markov model for multiperson activity recognition, IEEE Transactions on Circuits and Systems for Video Technology 22 (9) (September 2012) 1306–1320.

[25] N. Hautsch, R. Huang, The market impact of a limit order, Journal of Economic Dy namics and Control 36 (4) (2012) 501–522.

[26] Hayton, Utete, King, King, Anuzis, Tarassenko, Static and dynamic novelty detection methods for jet engine health monitoring, Philosophical Transactions of the Royal Society A 365 (December 2006) 493–514.

[27] J. Kim, P. Kang, Late payment prediction models for fair allocation of customer contact lists to call center agents Decision Support Systems (2016) 84–101

[28] D. Kwiatkowski, P.C. Phillips, P. Schmidt, Y. Shin, Testing the null hypothesis of stationarity against the alternative of a unit root, Journal of Econometrics (1992) 159–178.

[29] C.-C. Lee, J.-D. Lee, C.-C. Lee, Stock prices and the efficient market hypothesis: evidence from a panel stationary test with structural breaks, Japan and the World Economy 22 (1) (2010) 49–58.

[30] E.J. Lee, K.S. Eom, K.S. Park, Microstructure-based manipulation: strategic behavior and performance of spoofing traders, Journal of Financial Markets 16 (2) (2013) 227-252

[31] V. Mock, I. Lupini Commission extends by one vear the application date for the MiFID IL package, Feb 10 2016 Retrieved from European Commission Press Release http://europa.eu/rapid/press-release, IP-16-265 en.htm

[32] J. Mongkolnavin, S. Tirapat, ). Marking the close analysis in Thai bond market surveillance using association rules, Expert Systems with Applications 36 (4) (May 2009) 8523–8527.

[33] NANEX, HFT on Microsoft, Jan 24 2013 Retrieved from NANEX, http://www.nanex. net/aqck2/3979.html.

[34] W.W. Ng, J. Hu, D.S. Yeung, S. Yin, F. Roli, Diversified sensitivity-based undersampling for imbalance classification problems, IEEE Transaction on Cybernetics (2014) 2402–2412.

[35] E. Ngai, Y. Hu, Y. Wong, Y. Chen, X. Sun, The application of data mining techniques in financial fraud detection: a classification framework and an academic review of literature, Decision Support Systems (February 2011) 559–569.

[36] Öğüt, Doğana, Aktaş, Detecting stock-price manipulation in an emerging market: the case of Turkey, Expert Systems with Applications 36 (9) (November 2009) 11944–11949.

[37] P. Ravisankar, V. Ravi, G.R. Rao, I. Bose, Detection of financial statement fraud and feature selection using data mining techniques, Decision Support Systems (January 2011) 491–500.

[38] B. Schölkopf, J.C. Platt, J.C. Shawe-Taylor, A.J. Smola, R.C. Williamson, Estimating the support of a high-dimensional distribution, Neural Computation 13 (7) (July 2001) 1443–1471.

[39] R.S. Tsay, Analysis of Financial Time Series, Wiley, 2010

[40] J. Tse, X. Lin, D. Vincent, High frequency trading—Measurement, detection and response, Tech. Rep., Credit Suisse, Zürich, Switzerland, 2012.

[41] L. Wang, M.G. Mehrabi, E. Kannatey-Asibu, Hidden Markov model-based tool wear monitoring in turning, Journal of Manufacturing Science and Engineering 124 (3) (2002) 651–658.

[42] D.-Y. Yeung, Y. Ding, Host-based intrusion detection using dynamic and static behavioral models, Pattern Recognition 36 (2003) 229–243.

[43] K.Z. Zhang, M. Benyoucef, Consumer behavior in social commerce: a literature review, Decision Support Systems (2016) 95–108.

[44] J. Zhao, Extracting and reasoning about implicit behavioral evidences for detecting fraudulent online transactions in e-Commerce, Decision Support Systems (2016) 109–121.

![](/api/attachments/MGTY3DRZ/fulltext/images/2dcb4e2bba5fd3daab2bb28dd629a19e098510e5c762e3f63da45ffc22f00a4f.jpg)

Jia Zhai received the B.S. degree in finance from Shandong University, Jinan, China, in 2005, the M.S. degree and Ph.D. in finance from University of Essex, Colchester, UK, in 2006, and 2011 respectively.

She is a lecturer (assistant professor) in finance with Salford Business School in University of Salford from Dec. 2015. Before that, she was a lecturer in finance in Ulster University, Newtownabbey, UK, from 2012. She has also served as a visiting professor in Department of Financial Math & Engineering in South University of Science and Technology of China and with the Institute of Management Science and Engineering in Henan University. Her research interests include option pricing, quantitative risk management, behaviour finance and machine learning applications in finance. She

was a lecturer with the Department of Financial Mathematics in Xi'an Jiaotong-Liverpool University, from 2010 to 2012. Prior to that, she has served as research and teaching assistant in department of nance in University of Essex from 2006 to 2010.

![](/api/attachments/MGTY3DRZ/fulltext/images/bbc516228d13a7fc012af92120a6f60e76c540294992a833c106a0cd89aa1704.jpg)

Yi Cao received the B.Eng. degree in navigation and control in aeronautics from the Beihang University, Beijing, China, the M.S. degree in computer science from Florida International University, Miami, FL, USA, and Ph.D. in financial machine learning from Ulster University, Londonderry, UK, in 2002, 2005, and 2015 respectively.

He is currently a senior lecturer in computational finance with the School of Computing, Mathematics & Digital Technology, Manchester Metropolitan University, Manchester, U.K. Before that, he was a lecturer in computational nance with CCFEA in University of Essex. Before that, he was a Quant in Susquehanna International Group, Philadelphia, U.S.A. From 2008 to 2011, he was a Senior System Engineer at ERICSSON, Beijing. Prior to that, he was an Integrated

Circuit Engineer at Vimicro, Beijing, and Conexant Beijing Design Centre, respectively, from 2005 to 2008.

![](/api/attachments/MGTY3DRZ/fulltext/images/bf1a8bdcb11d6aa08faf0f5db642bb6ea4086e044a21e190c8c4edcf95fc3b46.jpg)

Yuan Yao received the B.Eng. degree in management information system from Tianjin University of Commence, China, in 1997, the M.S. degree and Ph.D. in management science and engineering from South-West Jiaotong University, China, in 2000, and 2006 respectively.

She is a professor with School of Business Administration in Henan University and the director of Institute of Management Science and Engineering in Henan University. Her research interests include stochastic finance, derivatives and risk management, nonlinear time series and machine learning application in finance. She has also served as a post-doc research associate in Fudan University from 2008 to 2010

![](/api/attachments/MGTY3DRZ/fulltext/images/ca40a08248e77250355b9f2ee5587e798d173fc55f072bfe4a45fd8854a975f9.jpg)

J. Zhai et al. / Decision Support Systems xxx (2016) xxx–xxx

Xuemei Ding received the PhD degree in Computer Scienc from the University of Ulster, UK. She is currently an associate professor at the Faculty of Software, Fujian Normal University, China. Her research interests include machin learning, pattern recognition, pattern classification, unsupervised learning, and novelty detection techniques.

Yuhua Li received the Ph.D. degree in general engineering from the University of Leicester Leicester, U.K. He was a Senior Research Fellow with Manchester Metropolitan University, Manchester, U.K., and a Research Associate with the University of Manchester, Manchester, from 2000 to 2005. He was a Lecturer with the School of Computing and Intelligent Systems, University of Ulster, Londonderry, U.K., from 2005 to 2014. He is currently a Lecturer with the School of Computing, Science and Engineering, University of Salford, Salford, U.K. His current research interests include pattern recognition, machine learning, data science, knowledge-based systems, and condition monitoring and fault diagnosis.

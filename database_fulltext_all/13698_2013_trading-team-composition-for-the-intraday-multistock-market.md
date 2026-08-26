---
otero_id: 13698
otero_key: "Q5ESHE2F"
title: "Trading team composition for the intraday multistock market"
authors: "Leandro G.M. Alvim; Ruy L. Milidiú"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.09.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Trading team composition for the intraday multistock market<sup>☆,☆☆</sup>

Leandro G.M. Alvim ⁎, Ruy L. Milidiú

Departamento de Informática, Pontifícia Universidade Católica do Rio de Janeiro, Brazil

## a r t i c l e i n f o

Article history: Received 19 April 2011 Received in revised form 29 June 2012 Accepted 18 September 2012 Available online 25 September 2012

Keywords: Trading team Partial Least Squares Weighted Interval Scheduling Computational <sup>fi</sup>nance Machine learning

## a b s t r a c t

Automated traders operate market shares without human intervention. We propose a Trading Team based on atomic traders with opportunity detectors and simple effectors. The detectors signalize trading opportunities. For each trading signal, the effectors follow deterministic rules on when and what to trade in the market. The detectors are based on Partial Least Squares. We perform some trading experiments with twelve BM&FBovespa stocks. The empirical <sup>fi</sup>ndings indicate that the proposed trading strategy reaches a 77.26% annualized pro<sup>fi</sup>t, outperforming by 380.07% the chosen baseline strategy with a 16.07% pro<sup>fi</sup>t. We also investigate Multistock Resolution Strategy (MSR) performance subject to brokerage commissions and income tax. Whenever the initial investment is at least US\$ 50,000, the MSR strategy provides a pro<sup>fi</sup>t of at least 38.63%.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Automated traders are artifacts that operate market shares without human intervention aiming to maximize the investor's earnings. Recently, several studies have been conducted using a combination of machine learning algorithms for market forecasting and automated traders [1,2,5,8–11,16,18,20,21,26,37]. Despite these efforts to, accurately, predict future stock trends and to develop trading strategies that turn good predictions into pro<sup>fi</sup>ts are still two major challenges.

Here, we propose a novel architecture that automatically selects stocks and trading times for a market day. The trading architecture contains trading opportunity detectors and simple trade effectors. The detectors task is to signalize trading opportunities. Given a speci<sup>fi</sup>c trading signal, the effectors follow deterministic rules on when and what to trade in the market. For the trading task, we build a trading team by combining atomic traders that operate with different stocks and time resolutions, with the help of several trading opportunity detectors. The detectors are based on Partial Least Squares (PLS), whereas the team is selected by maximizing the investor return over a market operation dataset.

We build several intraday traders, each one with a corresponding (stock, operation window) pair. We evaluate these traders by their corresponding trading returns. The trader team return is given by the composition of its selected trader rewards.

We perform some trading experiments with twelve BM&FBovespa stocks. The empirical <sup>fi</sup>ndings are shown in Table 1. The results indicate that the Multi Stock-Resolution strategy outperforms a chosen baseline on daily average pro<sup>fi</sup>t. Since there is no standard error overlap, the MSR average pro<sup>fi</sup>t is statistically different from BLS average pro<sup>fi</sup>t. We also investigate MSR performance subject to brokerage commissions and income tax. Whenever the initial investment is at least US\$ 50,000, the MSR strategy provides a pro<sup>fi</sup>t of at least 38.63%.

The main contribution is an automatic portfolio selection architecture for a trading day. The proposed architecture combines an optimization module with several machine learning opportunity detectors.

This work is organized as follows. In Section 2, we describe the trading scenario and its corresponding assumptions. In Section 3, we describe the PLS detectors and its corresponding quality metrics, that we use to forecast trading opportunities. In Section 4, we investigate atomic traders and trader teams. Additionally, we formulate the Trader Team Composition problem and show its solution. In Section 5, we describe the baseline trader that uses a classical trading approach. In Section 6, we show the empirical evaluation, that we use to assess the proposed strategy performance. Moreover, we compare the multistock trading strategy <sup>fi</sup>ndings with the baseline. Finally, in Section 7, we present the conclusions.

## 2. Trading scenario

## 2.1. Market assumptions

For mathematical modeling simplicity, we make the following market assumptions [7]. The all or nothing trade position at all times is either entirely bond or entirely stock.

Table 1 Strategies comparison

<table><tr><td>Strategy</td><td>Avg. daily profit (%)</td><td>Std. error (%)</td></tr><tr><td>Baseline</td><td>0.06</td><td>0.036</td></tr><tr><td>Multi stock-resolution</td><td>0.24</td><td>0.039</td></tr></table>

All or nothing is a common approach regarding maximizing pro<sup>fi</sup>ts for short-term strategies [7,15,35]. Another approach is portfolio selection, which diversi<sup>fi</sup>es a portfolio in order to reduce the risk over time. This approach is a standard for long-term strategies [24,28,39] and we point a research direction in our conclusions. Here, we adopt the <sup>fi</sup>rst one.

The all or nothing premise is a greedy heuristic that prioritizes maximizing pro<sup>fi</sup>t over time. To reduce the trading risk, we automatically select the thresholds for each trader, described in Section 2. The thresholds represent safe distances from a loss transaction.

Fractional market arbitrary amounts of stock or bond can be bought or sold at any time. No market impact trades can be placed without affecting the quoted price. Market impact is not signi<sup>fi</sup>cant when dealing with moderate and high liquidity stocks, what is our case. Moreover, simulating market impact is not a trivial task and still a research topic.

## 2.2. Trading costs

To reproduce a more realistic simulation scenario, we consider the following costs [15]: brokerage commissions and income tax.

Brokerage commission is a fee charged by the <sup>fi</sup>nancial intermediary institutions to its customers. For each operation, we consider a typical US\$11.00 Brazilian day trade brokerage commission [15]. Regarding Brazilian day trading rules, we deduct 20% of the earnings.

## 2.3. Performance metrics

To evaluate trading strategies, we apply the usual actual trading metrics. We divide the metrics into four modules: return, risk, gain per risk and trading. Each module contains performance indexes.

The return module indexes are daily average pro<sup>fi</sup>t, minimum and maximum pro<sup>fi</sup>t performances.

The risk module indexes consist of two risk metrics: Maximum Draw Down [23] and Ulcer Index [25]. The Maximum Draw Down is a measure of the maximum decline from a peak to a bottom performance in a speci<sup>fi</sup>c interval. A high value on a pro<sup>fi</sup>t series represents a high loss. The Ulcer Index evaluates drawn down depths and durations. Opposed to the standard deviation that measures risk as downward and upward pro<sup>fi</sup>t moves, Ulcer Index associates risk only to downside pro<sup>fi</sup>t moves.

Another is the gain per risk module. This module includes the gain per unit risk metrics [6,33] namely Sharpe ratio, Martin ratio, Calmar ratio, Sterling ratio and Burke ratio. Sharpe ratio is the excess return divided by the standard deviation of returns. Martin ratio is the investment excess return divided by Ulcer Index risk. Calmar ratio is the excess return divided by the maximum drawdown. Sterling ratio is the excess return divided by the averaged k-largest drawdowns. Burke ratio is the excess return divided by the square root of the sum of the squared k-largest drawdowns. For Sterling and Burke ratios, we set k=3 [33].

Finally, the trading module indexes that measure the aggressiveness of our strategy. We choose some indexes such as winning trades, losing trades, average number of trades, average gain divided by average loss.

## 3. Trading opportunity detectors

Stock market forecasting is a challenging topic for both investors and researchers. This is because the stock market data suffers from non-linearity and uncertainty [2,8,20]. Standard statistical forecasting strategies provide a partial solution to these issues. Thus, stock market forecasting asks for alternative methods, such as Arti<sup>fi</sup>cial Neural Networks (ANN's) [17,18,26,30,32,34], Support Vector Machines (SVM's) [10,16,21], Support Vector Regression (SVR) and Partial Least Squares (PLS) [5] and Decision Trees [36]

Our approach uses machine learning. Next, we de<sup>fi</sup>ne the learning task, the learning algorithm, the feature engineering, the performance metrics and modeling.

## 3.1. The task

We say that there is a trading opportunity of stock s at time t whenever we forecast a signi<sup>fi</sup>cant price rise of s at time t+δ. If that is the case, a simple strategy is to buy s at time t and sell it at time t + δ. Hence, we simplify the price forecasting problem to a simple trading opportunity detection task. Moreover, we move from a regression to a classi<sup>fi</sup>cation task.

Therefore, we build a set of machine learning based opportunity detectors, aimed at forecasting future price rises.

## 3.2. Detectors

We formulate trading opportunity detection as a binary classi<sup>fi</sup>cation task. Thus, we classify every time instant t either as a trading instant or not. We solve this problem by applying a supervised learning algorithm. In order to build the required training set, we just examine each past instant and check whether it is a trading opportunity or not.

We use a two step scheme to build the detectors. First, we use regression to provide effective intraday price forecasts. Next, we discretize these forecasts into up and down price trends. We de<sup>fi</sup>ne an up trend as relative price increase of more then , where is a chosen threshold. Otherwise, we say that we have a down trend. To choose the threshold we apply a grid search heuristic. We describe the details in the Modeling subsection.

For the price forecasting step, we apply Partial Least Squares algorithm based on [31] study. We choose PLS because there is only one parameter to adjust and it is computationally faster than support vector regression (SVR) and Arti<sup>fi</sup>cial Neural Networks algorithms. Moreover, [5] PLS results indicate competitive performance against SVR for volume forecasting.

## 3.3. Feature engineering

By examining past market information, technical analysts try to explore patterns that would help to forecast future market opportunities. Despite its theoretical advances, researchers do not <sup>fi</sup>nd them effective [3,14]. This fact led to the widespread support of the Ef<sup>fi</sup>cient Market Hypothesis. According to [13], what caused technical principles to fail in the 60s were ad hoc speci<sup>fi</sup>cations of trading rules that led to data snooping.

Instead of using trading rules based on the technical indicators, machine learning algorithms are being used to learn trading rules [10,22,29] from a set of technical analysis indicators.

In Appendix A, we enumerate the technical indicators that we use to improve the proposed detector input features set. They capture the following concepts: trend, risk, volume and momentum. Our goal here is to provide as much market information to our predictors as possible. We also apply simple price and volume features such as opening, closing, maximum and minimum.

Since our problem incorporates sequential data, we apply a sliding window method (SWM) [12] to our features. The objective of the SWM is to convert a sequential supervised learning problem into a classical supervised learning problem.

Suppose we have an ordered data set $D = \{ ( x _ { t } , y _ { t } ) \} _ { t = 1 } ^ { n }$ composed of n samples, where each pair $\left( x _ { t } , y _ { t } \right)$ contains the input attribute vector x and the output variable $y _ { t }$ at time t. In the SWM approach, one maps a w-delayed input feature set $x _ { i - w } , . . . , x _ { i - 2 } , x _ { i - 1 }$ to the corresponding output $y _ { i } ,$ where w is the time window size. With sequentially distributed features, the PLS algorithm explores the association between time correlated features.

## 3.4. Metrics

As stated in [15], there are several metrics that are usually applied to evaluate a regression model quality, such as the root mean squared error and the relative error. However, standard regression metrics are forecasting error driven, and they do not measure <sup>fi</sup>nal performance, that is, pro<sup>fi</sup>t over time.

To achieve this, we compute the $r _ { i }$ the price ratio by

$$
r _ {i} = \frac {p _ {i}}{p _ {i - 1}},\tag{1}
$$

where $p _ { i }$ and $p _ { i - 1 }$ are stock prices respectively at the current instant i and the previous instant i-1.

## 3.5. Modeling

Here, we describe our modeling architecture and parameters. Our architecture is divided into three modules: development, optimization and test.

In the development module, we generate 852 opportunity detectors that correspond to twelve stocks multiplied by the number of resolutions that <sup>fi</sup>t the seven hour market day. For instance, there are twenty-eight intervals of 15 min in a market day. Thus, we have twenty-eight opportunity detectors of 15 min for each stock, totaling 336 for the twelve stocks. We use only seven resolutions, namely: 15, 30, 45, 60, 75, 90 and 105 min. The opportunity detectors are generated once for a two month test period. The detectors are independent from each other. Thus, they are trained in several machines.

We calibrate two parameters for each opportunity detector. One is the threshold of the opportunity detector; another is the number of latent variables of PLS algorithm [38]. To solve this, we only apply a grid search method to <sup>fi</sup>nd the maximum pro<sup>fi</sup>t model. Despite its high number of iterations, grid search is a simple and ef<sup>fi</sup>cient method for calibrating PLS parameters [5]. Trying different numbers of PLS latent variables on a development dataset is a typical approach [31]. We limit latent variables from one to twenty and experiment with <sup>fi</sup>ve positions in the grid. A high number of latent variables may lead to over<sup>fi</sup>tting [31]. To calibrate each opportunity detector threshold, we also generate grid positions. The grid positions are in the range of minimum and maximum price ratios greater than one. We divide these into <sup>fi</sup>ve positions equally distributed. The threshold is the difference between the grid position and one. To avoid over<sup>fi</sup>tting, we choose the threshold on the development set.

Once we have the most pro<sup>fi</sup>table opportunity detectors, we apply them to the optimization module. The optimization module solves a weighted interval scheduling problem [19], described in Section 4. This module outputs a solution with the maximum pro<sup>fi</sup>t. The solution is a combination of traders each of whom has one opportunity detector with its best PLS model. Finally, we apply the solution on a test set and evaluate its total pro<sup>fi</sup>t.

## 4. Trading team

## 4.1. Atomic traders

The atomic trader's goal is to take a single trading order decision for an intraday trading window. This decision is based on a trading signal from an opportunity detector. The detector informs the trader whether to trade or to stay away at the beginning of its time window. When it buys a share, it also sells the same share by the end of the time window.

Let τ be an atomic trader. Every day, the atomic trader τ operates only with a speci<sup>fi</sup>c stock s, during a <sup>fi</sup>xed intraday time window [b,e], where bbe. Hence, the (s,b,e) triple identi<sup>fi</sup>es τ.

On the other hand, there is also the predictor trading signal $t _ { s , b } - \mathsf { a }$ binary variable that indicates either to trade or not to trade stock s at time b.

The atomic trader $\tau = ( s , b , e )$ satis<sup>fi</sup>es the following three constraints:

(a) Operates only with stock s;

(b) Operates only during [b,e];

(c) $\mathfrak { H } t _ { s , b } = 0$ the trader takes no action in the market, otherwise it performs an ordered pair of operations bbuy,sell> at instants b and e, respectively.

In order to evaluate the performance of τ during a given day d, we associate an elementary reward $r _ { \tau , d }$ to its operation. The reward measures the resulting amount of money for a one unit investment, and is given by

$$
r _ {\tau , d} = \left[ \frac {p _ {s , e , d}}{p _ {s , b , d}} \right] ^ {t _ {s, b, d}}
$$

where $p _ { s , j }$ is stock s price at time j of day d and $t _ { s , b , d }$ is the corresponding trading signal at day d.

For a period of m days, we de<sup>fi</sup>ne the total compound reward $r _ { \tau }$ by

$$
r _ {\tau} = \prod_ {d = 1} ^ {m} r _ {\tau , d}.
$$

## 4.2. Well formed trading team

With only one atomic trader, there are still opportunities for other investments. We say that two different traders $\tau = ( s , b , e )$ and $\tau ^ { \prime } = ( s ^ { \prime }$ $b ^ { \prime } , e ^ { \prime } )$ have no overlapping windows if and only if

$$
\left(b ^ {\prime} - e\right). \left(b - e ^ {\prime}\right) > 0.
$$

A trading team T of size k is a <sup>fi</sup>xed collection of atomic traders that operates every day, that ${ \mathrm { i } } s ,$

$$
T = \{(s _ {i}, b _ {i}, e _ {i}) \} _ {i = 1} ^ {k}.
$$

The trading team T is well formed if and only if its atomic traders have no overlapping windows.

## 4.3. Team composition

Let us formulate TTC, the trading team composition problem. First, assume that our goal is to operate with stocks from a given stock list S. Let $A = \{ ( s _ { i } , b _ { i } , e _ { i } ) \} _ { i = 1 } ^ { n }$ be the available pool of atomic traders, with all s in S.

Now, assume that we are given a trading operation dataset corresponding to m consecutive trading days, each day with H operating hours. Hence, for each trading day d, operating time j and stock s in $S ,$ the dataset provides the corresponding intraday price $p _ { s , j , d } .$

Based on the intraday prices provided in the dataset, we can compute the required trading signals $t _ { s , b , d }$ and rewards $r _ { \tau , d }$ and $r _ { \tau }$ for all $\tau = ( s , b , e ) \in A$

Given the input data, we must choose the atomic traders that compose T, our well formed trading team. Hence, for each trader $\tau \in { \cal A } ,$ we de<sup>fi</sup>ne the corresponding decision variable $x _ { \tau }$ by

$$
x _ {\tau} = \left\{ \begin{array}{l l} 1 & \text { if } \tau \text { belongs   to } T \\ 0 & \text { otherwise } \end{array} \right..
$$

Dataset information.

The <sup>fi</sup>nal compound reward of the chosen trading team T, when applied to the m days of the given dataset, is

$$
\prod_ {d = 1} ^ {m} \prod_ {\tau \in A} r _ {\tau , d} ^ {\chi_ {\tau}}
$$

which is equivalent to

$$
\prod_ {\tau \in A} r _ {\tau} ^ {\chi_ {\tau}}.
$$

Formally, the TTC problem is

$$
\max \prod_ {\tau \in A} r _ {\tau} ^ {x _ {\tau}}\tag{2}
$$

such that

$T = \{ \tau { \in } A | x _ { \tau } = 1 \}$ is a well formed trading team:

Since our goal is to maximize the <sup>fi</sup>nal compound reward, we take its log and obtain

$$
\sum_ {\tau \in A} w _ {\tau}. x _ {\tau}
$$

where $w _ { \tau } { = } l o g ( r _ { \tau } )$

Therefore, TTC is reduced to the problem

$$
\max \sum_ {\tau \in A} w _ {\tau}. x _ {\tau}\tag{3}
$$

such that

$T = \{ \tau { \in } A | x _ { \tau } = 1 \}$ is a well formed trading team:

The last problem is the well known weighted interval scheduling problem [19]. The solution to this problem is given by a dynamic programming algorithm that runs in O(n.lgn) time.

## 4.4. MSR strategy

The solution of the TTC problem is a multistock and multiresolution trader. Hence, we denominate it the MSR strategy.

Every market day, MSR operates with the same optimal trading team. However, the action of its atomic traders is triggered by their corresponding opportunity detectors.

## 5. Baseline strategy

The BLS strategy is built as follows. First, we run a set of candidate trading teams. Each candidate team operates with a <sup>fi</sup>xed stock-resolution pair throughout the whole market day. Next, we select the most pro<sup>fi</sup>table team as the BLS.

Unlike the MSR strategy, the baseline strategy (BLS) does not explore a multistock multiresolution trading team. However, BLS atomic traders do use machine learning opportunity detectors. This characteristic makes BLS well suited as an informative benchmark for MSR.

## 6. Empirical evaluation

In this section, we describe the proposed method empirical evaluation. First, we describe the dataset, methodology and conditions that lead us to choose the speci<sup>fi</sup>c trader for the BLS strategy. Next, we compare MSR and BLS results over standard trading benchmarks and statistical test results. Finally, we investigate the effect of trading costs for both the MSR and BLS strategies.

## 6.1. Empirical setup

The dataset consists of twelve intraday BM&FBovespa stocks, for the period starting on 23/12/2009 and ending on 14/05/2010. The stocks are provided by an investor company, all of them with adjusted prices. To choose the stocks, we considered the sixteen most traded stocks in the Bovespa stock exchange. However, four of them are removed owing to distinct interval ranges.

Table 2 illustrates the dataset stock composition, organized by stock ID, company name, liquidity and market sector.

To evaluate trading performances, we split the dataset into development and test. The development and test dataset dates vary from 23/12/ 2009 to 09/03/2010 and 10/03/2010 to 14/05/2010. In the development dataset, we calibrate our opportunity detectors and our trading strategies. Next, we apply the best con<sup>fi</sup>guration to the test dataset. Our heuristic for picking the best strategy is pro<sup>fi</sup>t over time, even when the most pro<sup>fi</sup>table strategy has more trading operations than others. Once Brazilian agency brokers tax a constant value for brokerage commission, we expect that earning percentage will offset costs.

In Table 3, we show the stock-resolution pair candidates and their resulting development dataset pro<sup>fi</sup>ts. The trader with USIM5 stock using a 30-minute resolution reaches a 0.68 daily pro<sup>fi</sup>t. Hence, this is the trader that we choose for the BLS.

## 6.2. Benchmark Results

In Table 4, we compare the BLS and MSR methods, using the selected metrics. MSR outperforms BLS, showing a 0.24% daily pro<sup>fi</sup>t. MSR annualized pro<sup>fi</sup>t is 77.26% and BLS annualized pro<sup>fi</sup>t is 16.07%.

Table 5 results indicate that MSR slightly increases the maximum drawdown when compared to the BLS. Ulcer Index performance is similar for both strategies. However, Table 6 results indicate that MSR outperforms BLS in all gain per risk benchmarks, what offsets MSR higher risk.

Table 7 results indicate that MSR implies more trades than BLS strategy. However, the average gain per average loss is 16% higher than BLS.

In Fig. 1, we report our <sup>fi</sup>ndings on a statistical test for the expected average gain difference among the BLS and MSR strategies. For each strategy we provide a bar that represents its average gain. The vertical lines in each bar represent the corresponding standard error. We note that MSR outperforms BLS by 300% on average pro<sup>fi</sup>t. Since there is no standard error overlap, the MSR average pro<sup>fi</sup>t is statistically different from BLS average pro<sup>fi</sup>t.

In Fig. 2, we outline MSR and BLS cumulative pro<sup>fi</sup>ts during market day. The y-axis represents the average pro<sup>fi</sup>t percentage and the x-axis represents the market day divided into twenty-eight intervals of 15 min each. We note that MSR develops a better pro<sup>fi</sup>t curve than BLS.

Table 2

<table><tr><td>Stock</td><td>Company</td><td>Liquidity</td><td>Sector</td></tr><tr><td>GGBR4</td><td>Gerdau</td><td>Very high</td><td>Construction</td></tr><tr><td>PETR4</td><td>Petrobras</td><td>Very high</td><td>Petroleum</td></tr><tr><td>USIM5</td><td>Usiminas</td><td>Very high</td><td>Mining</td></tr><tr><td>VALE5</td><td>Vale do Rio Doce</td><td>Very high</td><td>Mining</td></tr><tr><td>BBDC4</td><td>Banco Bradesco</td><td>Very high</td><td>Finance</td></tr><tr><td>CSNA3</td><td>Cia. Siderúrgica Nacional</td><td>Very high</td><td>Mining</td></tr><tr><td>AMBV4</td><td>Ambev</td><td>High</td><td>Beverage</td></tr><tr><td>BBAS3</td><td>Banco do Brasil</td><td>High</td><td>Finance</td></tr><tr><td>VIVO4</td><td>VIVO</td><td>High</td><td>Telecom</td></tr><tr><td>BRKM5</td><td>Braskem</td><td>Moderate</td><td>Chemical</td></tr><tr><td>CMIG4</td><td>Cemig</td><td>Moderate</td><td>Energy</td></tr><tr><td>TNLP4</td><td>Telemar</td><td>Moderate</td><td>Telecom</td></tr></table>

Table 3  
Baseline average daily pro<sup>fi</sup>ts — development results.

<table><tr><td>Stock</td><td>15 min (%)</td><td>30 min (%)</td><td>45 min (%)</td><td>60 min (%)</td><td>75 min (%)</td><td>90 min (%)</td><td>105 min (%)</td></tr><tr><td>AMBV4</td><td>0.53</td><td>0.34</td><td>0.21</td><td>0.22</td><td>0.16</td><td>0.08</td><td>0.11</td></tr><tr><td>BBAS3</td><td>0.36</td><td>0.4</td><td>0.42</td><td>0.25</td><td>0.17</td><td>0.24</td><td>0.32</td></tr><tr><td>BBDC4</td><td>0.29</td><td>0.29</td><td>0.33</td><td>0.23</td><td>0.14</td><td>0.17</td><td>0.15</td></tr><tr><td>BRKM5</td><td>0.44</td><td>0.26</td><td>0.28</td><td>0.06</td><td>0.12</td><td>0.03</td><td>0.03</td></tr><tr><td>CMIG4</td><td>0.13</td><td>0.08</td><td>0.1</td><td>0.11</td><td>0.07</td><td>0</td><td>0.01</td></tr><tr><td>CSNA3</td><td>0.41</td><td>0.37</td><td>0.33</td><td>0.2</td><td>0.26</td><td>0.28</td><td>0.12</td></tr><tr><td>GGBR4</td><td>0.37</td><td>0.39</td><td>0.33</td><td>0.34</td><td>0.26</td><td>0.19</td><td>0.23</td></tr><tr><td>PETR4</td><td>0.06</td><td>0.17</td><td>0.14</td><td>0.24</td><td>0.06</td><td>0.15</td><td>0.08</td></tr><tr><td>TNLP4</td><td>0.34</td><td>0.53</td><td>0.37</td><td>0.3</td><td>0.15</td><td>0.03</td><td>0.17</td></tr><tr><td>USIM5</td><td>0.33</td><td>0.68</td><td>0.59</td><td>0.55</td><td>0.45</td><td>0.48</td><td>0.56</td></tr><tr><td>VALE5</td><td>0.18</td><td>0.07</td><td>0.02</td><td>0.04</td><td>0.05</td><td>0.03</td><td>0.02</td></tr><tr><td>VIVO4</td><td>0.53</td><td>0.43</td><td>0.24</td><td>0.32</td><td>0.28</td><td>0.18</td><td>0.17</td></tr></table>

## 6.3. Trading cost effect

In Fig. 3, we illustrate BLS and MSR annualized pro<sup>fi</sup>ts considering brokerage commissions and income tax discounts. We also illustrate Brazilian in<sup>fl</sup>ation index for the 2010 year that is 5.97%. MSR outperforms BLS in all situations. We notice the high impact in pro<sup>fi</sup>t due to brokerage and income tax. MSR pro<sup>fi</sup>t is higher than standard risk free investments even for US\$ 50,000.

In Fig. 4, we show MSR and BLS trading costs percentage regarding initial investment. The x-axis represents the initial investment and the y-axis represents the percentage of brokerage commission regarding the initial investment. We notice that MSR brokerage commission cost is higher than BLS because of the higher daily average tradings. However, MSR pro<sup>fi</sup>t offsets the higher cost. Owed to brokerage commissions constant values, MSR and BLS trading costs tend to reduce when investing more money.

## 7. Conclusions

We investigate the problem of building a trading team that maximizes daily earnings. To solve this problem, we propose an automatic multistock and multiresolution trading strategy. Our approach uses simple trade effectors, triggered by trading opportunity detectors.

We perform some trading experiments with twelve BM&FBovespa stocks from 10/03/2010 to 14/05/2010. Our empirical <sup>fi</sup>ndings indicate that the proposed trading strategy reaches a 77.26% annualized pro<sup>fi</sup>t, outperforming by 380.07% the chosen baseline strategy. We also investigate MSR performance subject to brokerage commissions and income tax. Whenever the initial investment is at least US\$ 50,000, the MSR strategy provides a pro<sup>fi</sup>t of at least 38.63%.

A further research direction is to add more machine learning algorithms, trading resolutions and stocks. Thus, MSR would be more options to invest and probably more chances to maximize its pro<sup>fi</sup>t.

Regarding risk, we reduce the trading risks by using thresholds that represent safe distances from losses. However, a further research direction is to incorporate diversi<sup>fi</sup>cation to reduce this risk. Thus, there are two promising research directions: stock diversi<sup>fi</sup>cation during the time and stock diversi<sup>fi</sup>cation for each interval of the day. Diversi<sup>fi</sup>cation during the time uses all or nothing heuristic for each time interval.

Table 4  
Daily return indicators.

<table><tr><td>Return indicator</td><td>BLS (%)</td><td>MSR (%)</td></tr><tr><td>Avg. profit</td><td>0.06</td><td>0.24</td></tr><tr><td>Max. loss</td><td>3.80</td><td>1.30</td></tr><tr><td>Max. profit</td><td>2.75</td><td>3.89</td></tr></table>

Table 5  
Trading risk indicators.

<table><tr><td>Risk indicator</td><td>BLS (%)</td><td>MSR (%)</td></tr><tr><td>Max. Draw Down</td><td>0.51</td><td>0.62</td></tr><tr><td>Ulcer Index</td><td>0.29</td><td>0.29</td></tr></table>

However, the diversi<sup>fi</sup>cation occurs during the day. For instance, we could add a constraint to force changing stocks for consecutive intervals. In this approach, weighted interval scheduling modeling is not suitable. An interesting aspect of our <sup>fi</sup>nal solution is that there is a high chance of diversi<sup>fi</sup>cation during time. In the diversi<sup>fi</sup>cation for each time interval we could apply portfolio selection methods such as CVaR [4] or Markowitz [24] in order to <sup>fi</sup>nd a portfolio for each interval. The portfolio returns for each interval could be applied as input for the weighted interval scheduling problem. Replacing single stocks by synthetic stocks, a linear combination of stocks, could be another approach that could be easily implemented. Thus, all or nothing would represent positions in a set of stocks per position.

Another research direction is to compare a portfolio selection approach to the proposed MSR strategy. Merton's consumption model [27], a standard in stochastic analysis, would be a suitable benchmark. Finally, experimenting different utility functions such as CARA and CRRA [27] could lead to interesting results regarding risk.

## Appendix A. Feature engineering

The PLS input features are a combination of basic market features and some technical analysis indicators. In this appendix, we outline these features.

Let t be the time index and n the number of previous ticks. Thus, we de<sup>fi</sup>ne the following basic market features: opening price $p _ { t } ,$ closing price $c _ { t } ,$ overall volume $\boldsymbol { v } _ { t } ,$ minimum price $m i n _ { t , n } ,$ maximum price $m a x _ { t , n } ,$ minimum volume mi $\boldsymbol { v } _ { t , n }$ and maximum volume $\boldsymbol { m a x v } _ { t , n } .$

The main goal of a Trend indicator is to capture a time series general behavior. We choose a simple moving average SMA as our trend indicator. We describe $S M A _ { t }$ as:

$$
S M A _ {t} = \frac {1}{n} \cdot \sum_ {t = 1} ^ {n} p _ {t}.
$$

The main goal of a momentum indicator is to anticipate price changes. We apply the following indicators: rate of change $R O C _ { t , n } ,$ Williams $W R _ { t , n }$ and relative strength indicator $R S I _ { t , n } .$ Rate of change,

$$
\left\{ \begin{array}{c} R O C _ {t, n} = 1 0 0 \cdot \frac {p _ {t} - p _ {t - n}}{p _ {t - n}} \text {   if   } t > 0 \\ 0 \text {   otherwise   }. \end{array} \right.
$$

indicates overbought and oversold conditions. Price changes can be predicted by studying past rate of change cycles. Like the rate of change, the Williams indicator measures overbought and oversold conditions. However, the Williams indicator is calculated in a different way. It measures the relationship of the closing price relative to high and low ranges, as given by

Table 6  
Gain per risk indicator.

<table><tr><td>Gain/risk indicator</td><td>BLS (%)</td><td>MSR (%)</td></tr><tr><td>Sharpe ratio</td><td>0.35</td><td>1.33</td></tr><tr><td>Martin ratio</td><td>0.16</td><td>0.75</td></tr><tr><td>Calmar ratio</td><td>0.09</td><td>0.35</td></tr><tr><td>Sterling ratio</td><td>0.13</td><td>0.50</td></tr><tr><td>Burke ratio</td><td>0.08</td><td>0.39</td></tr></table>

Table 7  
Average performance indicators

<table><tr><td>Trading indicator</td><td>BLS</td><td>MSR</td></tr><tr><td>Winning trades</td><td>1.19</td><td>2.72</td></tr><tr><td>Losing trades</td><td>1.02</td><td>2.59</td></tr><tr><td>Trades</td><td>2.21</td><td>5.31</td></tr><tr><td>Gain/loss</td><td>1.03</td><td>1.20</td></tr></table>

$$
W R _ {t, n} = \left\{ \begin{array}{c l} 1 0 0 \cdot \frac {\max _ {t , n} - c _ {t}}{\max _ {t , n} - \min _ {t , n}} & \text { if } \max _ {t, n} - \min _ {t, n} > 0 \\ 1 0 0 & \text { otherwise. } \end{array} \right.
$$

The last momentum indicator is the relative strength indicator,

$$
R S I _ {t, n} = 1 0 0 - \frac {1 0 0}{1 + \frac {S M A _ {t , n} ^ {u p}}{S M A _ {t , n} ^ {d w}}}
$$

where $S M A _ { t , n } ^ { u p }$ and $S M A _ { t , n } ^ { d w }$ are simple moving averages from up and down changes, respectively. This indicator measures the speed and change of price.

We apply the following volume related technical indicators: On Balance Volume $O B V _ { t } ,$ , Price Volume Trend $P V T _ { t }$ , Positive Volume Indicator $P V I _ { t } ,$ Negative Volume Indicator $N V I _ { t }$ and Money Flow Indicator $M F I _ { t } .$ On Balance Volume.

$$
O B V _ {t} = \left\{ \begin{array}{c l} v _ {0} & \text { if } t = 0 \\ O B V _ {t - 1} + v _ {t} & \text { if } p _ {t} > p _ {t - 1} \text { and } t > 0 \\ O B V _ {t - 1} - v _ {t} & \text { otherwise } \end{array} \right.
$$

measures positive and negative volume <sup>fl</sup>ows, by considering when prices are higher or lower. The On Balance Volume basic concept is that volume movements anticipate price movements. Price Volume Trend,

$$
P V T _ {t} = \left\{ \begin{array}{c l} v _ {0} \cdot R O C _ {0, 1} & \text { if } t = 0 \\ P V T _ {t - 1} + v _ {t} \cdot R O C _ {t, 1} & \text { if } t > 0 \\ 0 & \text { otherwise } \end{array} \right.
$$

can be interpreted in the same way as On Balance Volume. However, Price Volume Trend considers how much higher or lower price changes are. In addition, we apply two particular cases of Price Volume Trend. One is Positive Volume Indicator,

$$
P V I _ {t} = \left\{ \begin{array}{c l} R O C _ {0, 1} & \text { if } t = 0 \\ P V I _ {t - 1} + R O C _ {t, 1} & \text { if } v _ {t} > v _ {t - 1} \text { and } t > 0 \\ 0 & \text { otherwise } \end{array} \right.
$$

![](/api/attachments/Q5ESHE2F/fulltext/images/11621de87de12e206a7610224793f5b9be01ee2ff720427bb5efce395bec0dd1.jpg)  
Fig. 1. MSR vs BLS.

![](/api/attachments/Q5ESHE2F/fulltext/images/59e6303712b4299af706453c88ddb432e5ad81ddcd9b93e7a534956a1b5d1a48.jpg)  
Fig. 2. BLS and MSR average performances during the day.

considers only positive price changes in the volume <sup>fl</sup>ow. The positive volume <sup>fl</sup>ow can be interpreted as the buying market forces. Another is Negative Volume Indicator,

$$
N V I _ {t} = \left\{ \begin{array}{c l} R O C _ {0, 1} & \text { if } t = 0 \\ N V I _ {t - 1} + R O C _ {t, 1} & \text { if } v _ {t} b v _ {t - 1} \text { and } t > 0 \\ 0 & \text { otherwise. } \end{array} \right.
$$

is the opposite of Positive Volume Indicator. Thus, the negative volume <sup>fl</sup>ow can be interpreted as the selling market forces. The last volume indicator is money <sup>fl</sup>ow indicator,

$$
M F I _ {t} = \frac {P M F _ {t}}{P M F _ {t} + N M F _ {t}}
$$

where, $P M F _ { t }$ is the positive money <sup>fl</sup>ow,

$$
P M F _ {t} = \left\{ \begin{array}{c l} 0 & \text { if } t = 0 \\ P M F _ {t - 1} + p _ {t} \cdot v _ {t} & \text { if } p _ {t} > p _ {t - 1} \text { and } t > 0 \end{array} \right.
$$

and $N M F _ { t }$ is the negative money <sup>fl</sup>ow,

$$
N M F _ {t} = \left\{ \begin{array}{c l} 0 & \text { if } t = 0 \\ N M F _ {t - 1} + p _ {t} \cdot v _ {t} & \text { if } p _ {t} b p _ {t - 1} \text { and } t > 0 \end{array} \right..
$$

Money <sup>fl</sup>ow indicates the ratio among buyers and sellers that are represented as positive money <sup>fl</sup>ow and negative money <sup>fl</sup>ow. We represent money <sup>fl</sup>ow as volume multiplied by price through days.

![](/api/attachments/Q5ESHE2F/fulltext/images/0941c463114c4888b11158fc5e230540550b4c2d18141fd008132b4696ab9e94.jpg)  
Fig. 3. Simulation with trading costs.

![](/api/attachments/Q5ESHE2F/fulltext/images/e3bf597263a82e5ea7f0e9d4c7e5c9e9aa98e02e1a9298d2528becc9f952ad56.jpg)  
Fig. 4. Trading costs.

Positive money <sup>fl</sup>ow indicates positive changes multiplied by volume and negative money <sup>fl</sup>ow considers negative changes.

The volatility indicators measure risk. We apply the following volatility indicators: Variance $V A R _ { t } ,$ Ulcer Indicator $U I _ { t } ,$ Sharpe ratio $S H P _ { t }$ , Draw Down $D D _ { t }$ , Maximum Draw Down $M D D _ { t }$ and Martin ratio $M R _ { t } .$ . Variance,

$$
V A R _ {t} = \frac {1}{N} \cdot \sum_ {i = t} ^ {N} \left(p _ {t} - S M A _ {t}\right) ^ {2}
$$

is the simplest measure of risk. This indicator considers downward and upward price variations as risk. An improved measure of risk is Ulcer Indicator,

$$
\begin{array}{c} D _ {t} = 1 0 0 \cdot \frac {p _ {t} - m a x _ {t , n}}{m a x _ {t , n}} \\ U I _ {t} = \sqrt {\frac {\sum_ {i = t} ^ {n} D _ {i}}{n}}. \end{array}
$$

Ulcer Indicator measures the variation only in downward direction. That is convenient, because upward price changes do not represent investment risk. This is because upward variation does not represent risk to the investor. Another is Draw Down, which measures the maximum decline in a time series. The Draw Down is described as:

$$
D D _ {t} = \left\{ \begin{array}{c l} 0 & \text { if } t = 0 \\ \max \left[ D D _ {t - 1}, \frac {p _ {t} - p _ {T}}{p _ {T}} \right] & \text { if } t > 0 \end{array} \right.
$$

where T is a constant that represents the current time. An extension of this indicator is the Maximum Draw Down,

$$
M D D _ {t} = \left\{ \begin{array}{c l} 0 & \text { if } t = 0 \\ \max [ M D D _ {t - 1}, D D _ {t} ] & \text { if } t > 0 \end{array} \right.
$$

which is the highest decline in Draw Down indicator. Sharpe ratio,

$$
S H P _ {t} = \frac {R _ {t} - R f}{S _ {t}}
$$

measures the excess return of an investment per unit of risk. In Sharpe ratio formula, $S _ { t }$ is the return standard deviation that represents the risk, $R _ { t }$ is the average rate return in price series and Rf is a risk free investment. Finally, we have the Martin ratio formula,

$$
M R _ {t} = \frac {R _ {t} - R f}{U I _ {t}}
$$

which is similar to Sharpe ratio. However, Martin ratio replaces Standard Deviation to Ulcer Indicator as a risk measure.

## References

[1] Ajith Abraham, Baikunth Nath, P.K. Mahanti, Hybrid intelligent systems for stock market analysis, in: International Conference on Computational Science, 2, 2001 pp. 337–345.

[2] Yaser S. Abu-Mostafa, Amir F. Atiya, Introduction to <sup>fi</sup>nancial forecasting, Applied Intelligence 6 (3) (1996) 205–213.

[3] S. Alexander, Price movements in speculative markets: trends or random walks Industrial Management Review 8 (5) (1961) 471–489.

[4] Gordon J. Alexander, Alexandre M. Baptista, A comparison of var and cvar constraints on portfolio selection with the mean-variance model, Management Science 50 (9) (2004) 1261–1273.

[5] Leandro G.M. Alvim, Cícero N. dos Santos, Ruy L. Milidiú, Daily volume forecasting using high-frequency predictors, in: IASTED International Conference on Arti<sup>fi</sup>cial Intelligence and Applications, AIA 2010, Innsbruck, Austria, 2, IASTED, 2010.

[6] C.R. Bacon, Practical Portfolio Performance Measurement and Attribution, The Wiley Finance Series, John Wiley & Sons, 2008.

[7] V. Boyarshinov, Machine learning in computational <sup>fi</sup>nance. PhD thesis, Rensselaer Polytechnic Institute, Jan 2005.

[8] Vanstone Bruce, Finnie Gavin, An empirical methodology for developing stockmarket trading systems using arti<sup>fi</sup>cial neural networks, Expert Systems with Applications 36 (3) (2009) 6668–6680.

[9] Pei-Chann Chang, Chen-Hao Liu, Jun-Lin Lin, Chin-Yuan Fan, S.P.Ng. Celeste, A neural network with a case based dynamic window for stock trading prediction, Expert Systems with Applications 36 (3) (2009) 6889–6898.

[10] Rohit Choudhry, Kumkum Garg, A hybrid machine learning system for stock market forecasting, in: WASET — Proceedings of World Academy of Science, Engineering and Technology, vol. 29, 2006, pp. 315–318.

[11] Fu-Lai Chung, Tak-Chung Fu, T.Y. Ng Vincent, W.P. Luk Robert, An evolutionary approach to pattern-based time series segmentation, IEEE Transactions on Evolutionary Computation 8 (5) (2004) 471–489.

[12] T.G. Dietterich, Machine learning for sequential data: a review, Lecture Notes in Computer Science (2002) 15–30.

[13] E. Fama, Ef<sup>fi</sup>cient capital markets: a review of theory and empirical work, Journal of Finance 25 (2) (1970) 383–417

[14] E. Fama, M. Blume, Filter rules and stock market trading, Journal of Business 39 (1970) 226–241.

[15] Paulo Gomide, Ruy L. Milidiú, Assessing stock market time series predictors quality through a pairs trading system, in: Proceedings of the 2010 Eleventh Brazilian Symposium on Neural Networks, IEEE Computer Society, 2010, pp. 133–139, http://dx.doi.org/10.1109/SBRN.2010.31 (isbn:978-0-7695-4210-2).

[16] Wei Huang, Yoshiteru Nakamori, Shou-Yang Wang, Forecasting stock market movement direction with support vector machine, Computers & Operations Research 32 (10) (2005) 2513–2522.

[17] Lara Khansa, Divakaran Liginlal, Predicting stock market returns from malicious attacks: a comparative analysis of vector autoregression and time-delayed neural networks, Decision Support Systems 51 (4) (2011) 745–759.

[18] Hyun-jung Kim, Kyung-shik Shin, A hybrid approach based on neural networks and genetic algorithms for detecting temporal patterns in stock markets, Applied Soft Computing 7 (2) (2007) 569–576.

[19] Jon Kleinberg, Eva Tardos, Algorithm Design, Addison-Wesley Longman Publishing Co., Inc., Boston, MA, USA, 2005

[20] R. Lawrence, Using Neural Networks to Forecast Stock Market Prices, University of Manitoba, 1997.

[21] Tang Ling-Bing, Tang Ling-Xiao, Sheng Huan-Ye, Forecasting volatility based on wavelet support vector machine, Expert Systems with Applications 36 (2) (2009) 2901–2909.

[22] A. Lo, H. Mamaysky, J. Wang, Foundations of technical analysis: computational algorithms, statistical inference, and empirical implementation, Journal of Finance 4 (2000) 1705–1706.

[23] M. Magdon-Ismail, A. Atiya, A. Pratap, Y. Abu-Mostafa, On the maximum drawdown of a Brownian motion, Journal of Applied Probability 41 (1) (March 2004) 147–161.

[24] Harry Markowitz, Portfolio selection, The Journal of Finance 7 (1) (1959) 77–91.

[25] Peter Martin, Byron McCann, The Investor's Guide to Fidelity Funds, John Wiley and Sons, 1989

[26] Leonardo C. Martinez, Diego N. da Hora, J.R.M. Palotti, Gisele L. Pappa, W. Meira Jr., From an arti<sup>fi</sup>cial neural network to a stock market day-trading system: a case study on the BM&F BOVESPA, in: The 2009 International Joint Conference on Neural Networks. 2009.

[27] Robert C. Merton, Optimum consumption and portfolio rules in a continuous-time model, Journal of Economic Theory 3 (4) (December 1971) 373–413

[28] J.E. Mitchell, S. Braun, Rebalancing an investment portfolio in the presence of transaction costs, in: Technical Report, Mathematical Sciences, Rensselaer Polytechnic Institute, Troy, NY 12180, November 2002.

[29] J. Moody, M. Saffell, Learning to trade via direct reinforcement, IEEE Transactions on Neural Networks 12 (July 2001) 875–889.

[30] Andy Pasley, Jim Austin, Distribution forecasting of high frequency time series, Decision Support Systems 37 (4) (September 2004) 501–513.

[31] R. Renteria, Algoritmos para Regressão por Mínimos Quadrados Parciais. PhD thesis, Pontifícia Universidade Católica do Rio de Janeiro, 2003.

[32] Eberhard Schöneburg, Stock price prediction using neural networks: a project report, Neurocomputing 2 (1) (1990) 17–27.

[33] Frank Schuhmacher, Martin Eling, Suf<sup>fi</sup>cient conditions for expected utility to imply drawdown-based performance rankings, Journal of Banking & Finance 35 (9) (September 2011) 2311–2318.

[34] Georgios Sermpinis, Christian Dunis, Jason Laws, Charalampos Stasinakis, Forecasting and trading the EUR/USD exchange rate with stochastic neural networkcombination and time-varying leverage, Decision Support Systems 54 (1) (December 2012) 316–329.

[35] G.C. Silaghi, V. Robu, An agent strategy for automated stock market trading combining price and order book information, in: 2005 ICSC Congress on Computational Intelligence Methods and Applications, 2005, pp. 1–4.

[36] Chih-Fong Tsai, Yu-Chieh Hsiao, Combining multiple feature selection methods for stock prediction: union, intersection, and multi-intersection approaches, Decision Support Systems 50 (1) (December 2010) 258–269.

[37] Ray Tsaih, Yenshan Hsu, Charles C. Lai, Forecasting S&P 500 stock index futures with a hybrid AI system, Decision Support Systems 23 (June 1998) 161–174.

Leandro Guimaraes Marques Alvim Graduate at Computer Science from Universidade Federal Fluminense (2005) and master's at Informatics from Universidade Federal do Rio de Janeiro (2008). Currently, is a ph. d. student at Ponti<sup>fi</sup>cia Universidade Catolica do Rio de Janeiro. Moreover, teaches in Technology Department of Universidade Federal Rural do Rio de Janeiro. Has experience in Computer Science, focusing on Algorithmics and Machine Learning Address to access CV: http://lattes.cnpq.br/3810771931191838

[38] S. Wold, H. Martens, H. Wold, The multivariate calibration problem in chemistry solved by the PLS method, in: Proceedings Conference Matrix Pencils, Springer Verlag, 1983, pp. 286–293.

[39] A. Yoshimoto, The mean-variance approach to portfolio optimization subject to transaction costs, Journal of the Operations Research Society of Japan 39 (1) (1995).

Ruy Luiz Milidiu Scholarship in Produtividade em Pesquisa do CNPq - Nível 2 Graduate at Bacharel in Mathematics from Universidade Federal do Rio de Janeiro (1974), master's at Operations Research from University of California (1983), master's at Applied Mathematics from Universidade Federal do Rio de Janeiro (1978) and ph.d. at Pesquisa Operacional from University of California (1985). Currently, teaches in Informatics Department of Ponti<sup>fi</sup>cia Universidade Catoloica do Rio de Janeiro. Has experience in Computer Science, focusing on Algorithmics, Machine Learning and Computational Complexity. Address to access CV: http://lattes.cnpq.br/6918010504362643.

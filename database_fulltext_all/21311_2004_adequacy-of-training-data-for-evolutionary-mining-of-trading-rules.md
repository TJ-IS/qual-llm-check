---
otero_id: 21311
otero_key: "5XRT44Y4"
title: "Adequacy of training data for evolutionary mining of trading rules"
authors: "Kumar Mehta; Siddhartha Bhattacharyya"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00091-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Adequacy of training data for evolutionary mining of trading rules

Kumar Mehta<sup>a,</sup>\*, Siddhartha Bhattacharyya

<sup>a</sup> Department of Operations and Information Management, University of Connecticut, 2100 Hillside Road, Unit 1041, Storrs, CT 06269-1041, USA

<sup>b</sup> Department of Information and Decision Sciences, University of Illinois at Chicago, Chicago, IL, USA

Available online 6 September 2003

## Abstract

A crucial issue related to data mining on time-series is that of training period duration. The training horizon used impacts the nature of rules obtained and their predictability over time. Longer training horizons are generally sought, in order to discern sustained patterns with robust training data performance that extends well into the predictive period. However, in dynamic environments patterns that persist over time may be unavailable, and shorter-term patterns may hold higher predictive ability, albeit with shorter predictive periods. Such potentially useful shorter-term patterns may be lost when the training duration covers much longer periods. Too short a training duration can, of course, be susceptible to over-fitting to noise. We conduct experiments using different training horizons with daily-data for the S&P500 index and report the sensitivity of the performance of the obtained rules with respect to the training durations. We show that while the performance of the rules in the training period is important for inducing the ‘‘best’’ rules, it is not indicative of their performance in the test-period and propose alternative measures that can be used to help identify the appropriate training durations.

<sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Data mining; Genetic algorithms; Time series prediction; Financial forecasting

## 1. Introduction

Data mining of financial time series saw its first major acceptance beginning with the publication of Ref. [5] which noted significant prediction potential of simple trading strategies for the Dow Jones Index and was followed by applications to the foreign exchange markets by Refs. [10] and [16]. Following on such findings, numerous studies have sought the use of machine learning techniques for data mining in financial markets data and learning of trading strategies (see Refs. [6] and [9] for detailed reviews). Neural networks and evolutionary algorithms have been extensively adopted for discovery of trading strategies in financial markets because of their ability to discover hidden patterns in highly dimensional data [6,22]. While most of the studies have looked at discovery of profitable trading strategies using different techniques, few have focused on systematic examination of the problems specific to the domain of knowledge discovery in financial time series.

One of the key problems associated with financial time series is that of non-stationarity and noise; overfitting to the noise in the data reduces its ability to forecast directional movement of the market. Weigend et al. [21] use bootstrapping of residuals to evaluate the forecasting power of the neural networks for foreign exchange markets. LeBaron and Weigend [11] find that strategies learnt using the traditional approach of static splits of training and test data tend to be highly sensitive to the specific split in the data. They suggest the use of the bootstrap method to avoid such overfitting to noise and improve the robustness of the models obtained. Dacorogna et al. [7] examine overfitting in the case of genetic algorithms due to a single gene discovering a sharp peak and suggest the use of fitness sharing among the population of solutions as a means for preventing premature convergence. These papers highlight a major problem associated with learning in noisy time series—pitfalls of overfitting to noise. However, problems associated with changes in the dynamics of the market and their effect on learning have not yet been addressed.

Traditional statistical wisdom from asymptotic theory suggests ‘‘more the training data lesser the chances of fitting to noise’’. Longer training horizons are thus sought in order to discern sustained profitable patterns with robust training data performance that extends well into the predictive period. To further improve robustness and prevent overfitting to noise, the methods suggested by Refs. [7] and [11] can be adopted. However, if the underlying profitable patterns change with changes in market characteristics, patterns that persist over a long duration may be unavailable, and increases in the size of training sample can have a confounding effect on the learning. It should be noted in this regard that instead of a single profitable pattern there typically exists a potential ensemble of profitable patterns, which may be possibly overlapping or even conflicting as demonstrated in Ref. [13]. As mentioned above, with changing market characteristics in dynamic environments, patterns that persist over time may be unavailable, and shorter-term patterns may hold higher predictive ability, albeit with shorter predictive periods. Use of longer training duration would bias the discovery away from shorter-term patterns that may hold higher predictive ability for shorter horizons into the test period. Too short a training duration can, of course, be susceptible to over-fitting to noise in the data—with discovered rules modeling the specific movements in the training data. This paper utilizes daily data for the S&P500 index to examine the effect of varying the training sample size in the discovery of trading rules and examines the rules obtained in terms of their performance and trading characteristics.

## 2. Background and Proposed Research

In general, high-dimensional training data used for knowledge discovery do not determine a unique concept. Frequently, there are an infinite number of concepts that are consistent with the data. Factors other than the training data that determine the concept selected by the learning algorithm constitute the bias of the algorithm [19]. Utgoff [20] describes two central properties of this bias: correctness and strength. While correctness is measured by performance of the discovered concept, the strength of the bias is its ability to focus the discovery to a relatively small number of concepts. It is through the use of bias that the size of the concept space is reduced for the learning algorithm, with the magnitude of reduction depending on the strength of the bias. The key to successful formulation of bias is its ability to perform well under differing environments. The No Free Lunch (NFL) theorems [23,24] state that no single bias works well under all circumstances, i.e. if it performs well under one environment it will perform poorly under another.

In the context of evolutionary algorithms, the fitness function offers one avenue for manipulation of the bias. For evolutionary learning of trading rules, Refs. [17] and [14] present a discussion on fitness function formulations for foreign exchange markets and the stock market, respectively. While Ref. [19] suggests that only factors outside of the training data constitute bias, any fitness function formulation in the context of a dynamic time-series concerns the evaluation time period T (which also gives the size of the training data), and this thus constitutes a component of the bias, with properties highlighted by Ref. [20] and NFL theorems being thereto applicable. As a result, the training duration will not only affect the concepts (trading rules) discovered, but according to the NFL theorem, the extent to which they perform well under different circumstances (duration into the test-period) may also change. Further credence to the notion that size of training data can introduce a bias in the discovery of trading rules comes from the results of various agent-based studies focusing on financial markets as dynamic systems with changing characteristics [2 – 4,8,12,15,16].

This paper adopts a genetic algorithm-based induction of trading rules using evaluation criterion proposed by Ref. [14] to examine the effect of change in size of training data on the performance and trading characteristics of the rules discovered. The experiments are carried out using S&P500 index data from 1983 to 1995, with test period fixed at 1993– 1995, and training durations of 2.5, 5, 7.5 and 10 years ending in 1992. The next section presents the evaluation criterion used with the genetic algorithm, the rule representation and interpretation. We also propose measures for characterizing the nature of the rules obtained from independent trials on training data comprising of different durations. Section 4 presents the experimental setup with Section 5 presenting the detailed results.

## 3. Rule representation and evaluation

In this study, a traditional GA-based representation is used for specifying trading models learnt using the Standard & Poor’s Composite Index (S&P500) data. In addition to using past high, low and closing prices in the rules, a range of indicators may be used for specifying trading models. While some suggest the use of simple moving average rules [5,7] others have considered more complex indicators such as momentum and exponential moving averages [17,18]. The learning of trading rules, in general, involves learning good indicators, as well as combinations of these in defining good rules. Rules then seek appropriate combinations of these for identifying patterns in the time-series data. Given the focus of this study on examining the effect of different training durations on performance of discovered rules, indicators commonly mentioned in the literature are used. It should be noted that further performance improvement can always be obtained through the use of more sophisticated indicators as well as richer rule representation. Given the focus of our study, we choose a simple well known set of indicators. In order to ensure their meaningful combination to form rules, and to maintain semantic integrity of the rules, indicators are categorized into three types:

 High, Low and Closing prices at specific times $t _ { \mathrm { i } }$ (point measure)

 Moving Average of the prices for multiple time window Dt (trend measure)

 Variance of high and low prices for multiple time windows, $\Delta t _ { \mathrm { i } }$ (volatility measure).

A trading decision rule r at any time t, specifies

$$
r _ {t}: X _ {\mathrm{h} t} \to S
$$

where $X _ { \mathrm { h } t }$ gives the price history up to time t; and $S { \in } \{ 0 , 1 \}$ specifying a trading signal (the 0 and 1 being interpreted to imply either an ‘‘out of market’’ or ‘‘in the market’’ position, as desired).

A trading rule takes the form:

```txt
IF <Condition> THEN <Signal>, where, the condition is a logical combination of terms, each term being of the form <indicator days-ago> <arithmetic operator> <indicator days-ago>
```

A term thus specifies a comparison between two indicators, each evaluated at a certain point in (past) time. Since each type of indicator represents a different measure, only indicators of the same type are allowed within a term. Both conjunction (AND) and disjunction (OR) operators can be used in combining terms in the condition part of a rule. A trading model then follows the following representational form: ([ ] denotes optional and {} denotes required constructs).

```yaml
rule:
    condition: logical-expression
    signal
logical-expression:
    [logical-unary-operator] term_T [{logical-binary-operator}logical expression]
term_T:
    {indicator_T days-ago}{arithmetic-operator}{indicator_T days-ago}
logical-binary-operator: one of
    AND, OR
logical-unary-operator:
    NOT
comparison-operator: one of
    <=, >=
signal: one of
    buy(1), sell(0)
indicator_T: one of
    high, low, close
    moving-average {days-ago}
    volatility{days-ago}
```

Since each type of indicator (price, moving  average, volatility) represents a different measure, only indicators of the same type are allowed within a term. A term may thus compare values of two moving-average indicators, or of two volatility indicators, or of two price values (high, low, or close prices). The semantics of the rule structure thus prevents for invalid comparisons (e.g. comparison of point measure with volatility measure).

In Ref. [14], the authors look at two alternative ways at obtaining excess returns. Noting that a rule’s condition can capture and specify patterns for either taking in-market or out-of market positions, two alternate interpretations are useful. A rule’s condition evaluating to TRUE is typically considered as a signal to buy, with a FALSE indicating a signal to sell. This approach specifies taking a default out-ofmarket position, with being in the market only when the rule’s condition evaluates as TRUE. Obtaining returns in excess of the market (a buy-and-hold strategy) using this approach requires that a rule learn useful patterns that specify periods for being in the market. An alternative interpretation is to consider a rule’s condition evaluating to TRUE as a signal to step out of the market, with the default position being to stay in-market. Under conditions where the price series exhibits a general positive trend over time and a simple buy-and-hold strategy provides greater than zero returns, identifying conditions for staying out of market (and staying in market at other times) can be easier. Since the rules here can focus on the fewer periods when it should stay out of market to obtain the same level of performance, this approach can also be expected to yield more precise rules. The strategy is to thus take advantage of the overall increasing trend of the stock market and augment the returns by avoiding as many loss-making days as possible.

## 3.1. Rule characterization

To discern the nature of rules learnt, two measures are defined to characterize learnt rules: the complexity of the rule, and the specificity of the rule. Complexity is defined as the number of possible combination of terms under which a rule generates a TRUE as a signal. A caveat for the reader—the objective of the proposed complexity measure is to quantify the signaling complexity of the rule and is not to be confused with computational complexity. Complexity would thus characterize the possible distinct circumstances under which a rule is likely to generate a ‘‘sell’’ signal. This is defined for different operators as follows:

n Comparison operator has a complexity of 1.

n Complexity of an OR operator is the sum of the complexities of the concerned terms.

n Complexity of an AND operator is the product of the complexities of the concerned terms.

Specificity of a rule is defined as the minimum number of terms required to be satisfied for a given rule to fire. While complexity measures the possible different number of scenarios under which a rule is likely to signal ‘‘sell’’, it does not measure the number of terms that characterize each of these scenarios. We characterize the minimum number of terms that define a scenario as the specificity of a given rule. Specificity for different operators is defined as follows:

n Specificity of an OR operator is the minimum of the specificities of the concerned terms.

n Specificity of an AND operator is the sum of the specificities of the concerned terms.

n Specificity of a comparison operator is 1.

Example: consider the following rule:

```txt
■ Specimeny of a comparison operator is 1. Example: consider the following rule:

IF
{
(low(10 days ago)>=low(8 days ago)) AND (close(2 days ago)>=close(7 days ago)))
OR
(moving average(5) 4 days ago >= moving average(20) 4 days ago)
}
AND
{
(variance(50) 2 days ago < variance(10) 4 days ago)
}
```

Fig. 1 below shows the rule representation in tree form with the values complexity and specificity illustrated at each of the nodes. Note that there are two distinct scenarios under which rule will signal TRUE (i.e. complexity = 2), namely, Scenario 1: [(Term4)AND(Term3)] and Scenario 2: [(Term4)AND(Term1)AND(Term2)]. The first scenario contains the minimum number of terms required to be satisfied for the rule to signal TRUE (i.e. specificity = 2).

## 3.2. Fitness measure

A trading rule on a given day t signals a ‘‘buy’’ or a ‘‘sell’’ decision for the next day (t + 1) based on known indicator values till the previous day (t  1). If the rule signals a ‘‘buy’’, the performance gain is equal to the in-market rate of return; otherwise, the performance gain is equal to the prevailing risk-free rate. The goodness of a series of N decisions over time, T, can be determined by the total realized return. Since the total realized return is dependent on the reinvestment of previous returns, it can be expressed as a continuously compounded series:

![](/api/attachments/5XRT44Y4/fulltext/images/a72c0ba5e7235ec4bbc26fe9d3c40d7f825f63e167bac3ab71aaa2d32e74c52d.jpg)  
Fig. 1. Example rule showing computation of complexity and specificity.

$$
r _ {\mathrm{c} _ {N}} = \prod_ {i = 1} ^ {i = N} (1 + r _ {\mathrm{s} _ {i}}) - 1\tag{1}
$$

where $r _ { \mathrm { c } _ { N } } = \mathrm { t o t a l }$ realized returns from undertaking of N decisions and $r _ { \mathrm { s } _ { i } } = \mathrm { s i m p l e }$ return from ith decision.

The fitness functions used by Refs. [1] and [10] employ continuously compounded returns for evaluating trading rules. In Ref. [14], the authors show that for a set of trading rules with the same aggregate returns, the fittest trading rule will have the lowest mean return per trade and lowest variance in mean returns per trade, i.e.:

For n different rules where

$$
\sum_ {i = 1} ^ {i = N _ {1}} r _ {\mathrm{s} _ {1 _ {i}}} = \sum_ {i = 1} ^ {i = N _ {2}} r _ {\mathrm{s} _ {2 _ {i}}} = \dots = \sum_ {i = 1} ^ {i = N _ {n}} r _ {\mathrm{s} _ {n _ {i}}} = r.
$$

Then the fittest rule will be selected based on (illustrative example in Table 1):

$$
\min (\bar {r} _ {s _ {j}}) _ {j = 1} ^ {j = n}, \text {   and   } \min (\sigma_ {r _ {s _ {j}}}) _ {j = 1} ^ {j = n}.
$$

Table 1  
Illustrative example (N denotes trades)

<table><tr><td rowspan="2">Rule</td><td colspan="5">Returns from individual trades</td><td rowspan="2">Aggregate return</td><td rowspan="2">(Fitness) Compounded return</td></tr><tr><td>N=1</td><td>N=2</td><td>N=3</td><td>N=4</td><td>N=5</td></tr><tr><td>1</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>5</td><td>1.05101</td></tr><tr><td>2</td><td>1.50</td><td>0.50</td><td>1.00</td><td>1.00</td><td>1.00</td><td>5</td><td>1.05098</td></tr><tr><td>3</td><td>1.25</td><td>1.25</td><td>1.25</td><td>1.25</td><td></td><td>5</td><td>1.05095</td></tr><tr><td>4</td><td>2.00</td><td>1.75</td><td>0.25</td><td>1.00</td><td></td><td>5</td><td>1.05085</td></tr><tr><td>5</td><td>2.50</td><td>0.50</td><td>1.00</td><td>1.00</td><td></td><td>5</td><td>1.05083</td></tr></table>

While the bias towards rules exhibiting a lower variance in mean returns per trade may be desirable, the bias for rules generating higher number of trades poses a serious problem. Rules that trade very frequently have a greater tendency to adhere to what might essentially be noise in the data. Furthermore, the use of realized returns evaluates a rule based on the ratio of selling price to buying price, and thus ignores the possible opportunity losses during the holding period. The following fitness function helps overcome these difficulties and is used for evaluating the base predictors:

$$
r _ {\mathrm{s} _ {T}} = \sum_ {t = 1} ^ {t = T} \left[ \frac {M _ {t} P _ {t} (1 - \theta_ {t} c)}{P _ {t - 1}} \right] + \sum_ {t = 1} ^ {t = T} [ (1 - M _ {t}) \bar {r} _ {\mathrm{f} _ {t}} ] - T\tag{2}
$$

where $P _ { t } { = } \operatorname { p r i c e }$ at time t, r<sub>s</sub> = total non-realized return over a period $T , M _ { t } = 1$ market position signal, 1 for in-market and 0 for out-of- market positions, $\theta _ { t } { = } \mathrm { t r a d e }$ signal, assuming a value of 1 whenever a held market position is reversed, $\bar { r } _ { \mathrm { f } _ { t } } { = } \mathrm { a v e r a g e }$ risk-free rate over the training period.

Using a non-realized return penalizes rules for any non-realized losses incurred while holding particular market positions, thus rewarding rules for improved accuracy in prediction, and removing the bias towards rules that tend to maintain prolonged market positions. The transaction cost, c, in the above expression is incurred only when an actual trade is conducted. The inclusion of a transaction cost, besides being realistic, also serves as a check against rules that switch positions very frequently leading to an overfit to small fluctuations in the market data. The absence of an explicit consideration of terms with prevailing risk-free rate in the rules can bias the rules to overfit to specific sections of the time series—such as periods of high risk-free rates. To prevent such incentive for overfitting to specific sections of the series, we use the average risk-free rate during the training period as the returns earned during the out-of-market periods. For a detailed discussion on various fitness functions for evaluating trading rules see Ref. [14].

## 4. Experimental study

## 4.1. Data

The Standard & Poor’s Composite Index (S&P500) from Jan 1, 1983 to Dec 31, 1995, is used as the time series data in this study. For the corresponding period, rates for 90-day Treasury bills were used as the existing risk-free (RF) rate and the transaction cost was set at 0.5% as in Ref. [1]. The training durations used for discovering the trading rules are: (1) 10-years—Jan 1st, 1983 to Dec 31st, 1992; (2) 7.5 years—July 1st, 1985 to Dec. 31st, 1992; (3) 5 years—Jan 1st, 1987 to Dec 31st, 1992; and (4) 2.5 years—July 1st, 1989 to Dec 31st, 1992. The remaining data (Jan 1st, 1993 to Dec. 31st 1995) is used for testing the trading rules. The data series consists of the daily high, low and closing prices for the index. No data on dividends declared by the firms is used in the learning process. Note that the training data includes the market crash of October 19th, 1987. Initial experiments revealed that fitness values of rules tended to be dominated by a few correct decisions around this crash date, with poor decisions at other times. To eliminate this bias, the data following the stock market crash was corrected by the crash amount, effectively eliminating the market crash from the used data.

## 4.2. Indicators

As mentioned above, three types of indicators are used in specifying trading rules for this study—high, low and closing prices providing point measures, moving averages of prices providing trend measures, and variances of prices giving volatility measures. These are specified using different time horizons, for example, closing price taken 3 days ago, or movingaverage over 50 days computed 2 days ago. In the interest of simplicity and given our primary objective of examining the impact of training duration on performance of discovered trading rules, only a prespecified set of indicators is used in the discovery of the rules. For the trend and volatility measures, time windows $\Delta t _ { i }$ of 5, 10, 20, 50, 100 days are used.

![](/api/attachments/5XRT44Y4/fulltext/images/01734b5efe92c0237053fb59906b5ae8c905e38d8166f82d31d38ddac03dffe1.jpg)  
Fig. 2. Cumulative excess returns obtained by median rules.

## 4.3. Experimental setup

A total of four sets of experiments were conducted, one set each for training durations of 10, 7.5, 5 and 2.5 years, respectively. The rules were learnt using the evaluation criterion stated in Eq. (2), where the TRUE signal is interpreted as a ‘‘sell’’ decision. A set of nine random seeds is used to conduct a set of nine independent GA trials for each of the four sets outlined above. Identical sets of random seeds are used with each of the training duration to allow meaningful comparison<sup>1</sup> of their performance, trading characteristics and nature of the rules obtained. In keeping with the measures used in fitness evaluation during training, performance on the test period considers the aggregation of non-realized returns; that is, no reinvestment of obtained profits is considered (compounded returns take such reinvestment into account). It should be noted that a compounding of returns and consideration of dividends would yield higher values than those reported here.

Returns in excess of buy-and-hold strategy over the test period

<table><tr><td>Training duration</td><td>Mean excess returns during training</td><td>Mean excess returns year 1 (std. dev. in ())</td><td>Excess returns over 2 years (std. dev. in ())</td></tr><tr><td>2.5 Years</td><td>8.6 ( $\sigma = 1.2$ )</td><td> $-1.4$  ( $\sigma = 3.7$ )</td><td> $+1.0$  ( $\sigma = 2.4$ )</td></tr><tr><td>5.0 Years</td><td>7.5 ( $\sigma = 1.1$ )</td><td> $+3.7$  ( $\sigma = 1.4$ )</td><td> $+3.3$  ( $\sigma = 1.0$ )</td></tr><tr><td>7.5 Years</td><td>6.3 ( $\sigma = 0.9$ )</td><td> $+4.4$  ( $\sigma = 1.3$ )</td><td> $+4.2$  ( $\sigma = 1.2$ )</td></tr><tr><td>10 Years</td><td>7.2 ( $\sigma = 1.3$ )</td><td> $+2.5$  ( $\sigma = 2.0$ )</td><td> $+4.4$  ( $\sigma = 1.7$ )</td></tr></table>

## 5. Results

## 5.1. Performance

The cumulative excess return accumulated over the duration of the test period by median rules (as determined by performance over the training period) is shown below in Fig. 2. Table 2 and Fig. 3 present

![](/api/attachments/5XRT44Y4/fulltext/images/1a6c76c50b2b329dd89519c31efe7f292de7b65bd645ae949d0fd9c34bdaf4fb.jpg)  
Fig. 3. Average performance of rules with different training durations.

the performance figures accompanied with variation in performance across rules obtained from the nine independent trials. It should be noted that the 2.5-year training duration seems to provide rules that perform better on training than rules discovered with other training durations and that too with a remarkable consistency across independent trials. However, examination of the performance on predictive periods of 1-year and 2-year horizons reveals a high degree of overfit to noise.

A more appropriate measure of overfit is shrinkage—measured as the percentage change in performance from training data to the test data, thereby revealing the degree of overfit to noise in the training data. Fig. 4 plots the mean shrinkage for the rules obtained. While longer training durations are generally seen to indicate more robust rules, note that the 10-year rules show increased shrinkage in the immediate year of prediction. Also, the performance values provided in Table 2 clearly indicate an across-theboard poorer performance in the immediate year of prediction by all the rules obtained from 10-year training durations. From examination of the performance it is clear that too short a duration prevents clear identification of profitable patterns from noise in the data; rules learnt using too long a horizon miss out on identification of patterns with higher predictive ability in the immediate test period.

![](/api/attachments/5XRT44Y4/fulltext/images/cf9485c7e18bade57a1f612a7b9366aafe33076f2a4a2ae7538621890f3858a8.jpg)  
Fig. 4. Shrinkage in performance with different training durations.

![](/api/attachments/5XRT44Y4/fulltext/images/b6d0b031ae11ad8c981c0a2ac6f99e92a71b964bce78362e2e1e725cdb4067c6.jpg)  
Fig. 5. Average trading frequency of rules obtained.

## 5.2. Trading characteristics

The average trading frequency of the obtained rules is provided in Fig. 5 below. It can be seen that rules obtained with 2.5-year training duration trade most often, averaging 55.9 trades annually over the testing period, and the rules obtained from 7.5-year training duration trade least often—averaging 32.6 trades annually. The trading characteristics along with the performance over test period show that trading frequency is inversely related to the performance (shrinkage) over the test-period. This would indicate that rules that were learnt using too short a duration (2.5 years) were not able to isolate profitable patterns from the training data and overfit to noise in the data. The relationship between trading frequency and shrinkage in performance as well as trading frequency and performance obtained in training data is plotted in Fig. 6.<sup>2</sup>

From the figure it is clear that rules that traded often in the training data tended to fit to what is essentially noise in the data and the continued high trading frequency in the test data is directly related to their poor performance (high shrinkage). As discussed later, trading frequency over different training horizons can be used for selection of appropriate training duration.

## 5.3. Nature of rules: specificity and complexity

The complexity and specificity of the individual rules obtained is shown in Fig. 7—a digit beside the marker denotes multiple rules with the same complex-

![](/api/attachments/5XRT44Y4/fulltext/images/4eb8765d044e1e6852c76edca7572f284744c4a8a0b200d88a5c44ef951a8542.jpg)  
Fig. 6. Trading frequency vs. training performance and shrinkage in test period.

ity – specificity combination. Table 3 provides the mean and standard deviation for complexity and specificity of the rules obtained with each of the training durations. This analysis into the nature of rules provides additional insight into the performance and trading characteristics noted above. It can be seen that the rules obtained with 7.5-year training durations lie within a small region of the graph (highlighted using a hyphenated rectangle), indicating that the rules are neither too complex nor too specific. In contrast, the rules obtained with 2.5-year training duration tend to be extremely diverse in terms of their complexity and specificity.

![](/api/attachments/5XRT44Y4/fulltext/images/6bdff4d3239352d7ff1d306546a80fc9ab49eae7f4697861671b44572520557e.jpg)  
Fig. 7. Complexity and specificity of rules obtained from different training durations.

Table 3  
Average complexity and specificity of the trading rules

<table><tr><td>Training duration</td><td>Mean complexity (std. dev. in ())</td><td>Mean specificity (std. dev. in ())</td></tr><tr><td>2.5 years</td><td>2.56 ( $\sigma = 1.13$ )</td><td>2.33 ( $\sigma = 0.71$ )</td></tr><tr><td>5 years</td><td>1.89 ( $\sigma = 1.05$ )</td><td>2.67 ( $\sigma = 0.87$ )</td></tr><tr><td>7.5 years</td><td>1.56 ( $\sigma = 0.53$ )</td><td>2.33 ( $\sigma = 0.71$ )</td></tr><tr><td>10 years</td><td>1.78 ( $\sigma = 1.09$ )</td><td>2.78 ( $\sigma = 0.83$ )</td></tr></table>

In Fig. 6 it was shown that high trading frequencies tend to be indicative of overfit to noise and hence poorer observed performance in the test data. An examination of relation between trading frequencies and nature of the rules provides the basis for the observed phenomenon. Figs. 8 and 9 show the contours of trading frequency and performance of rules (annual excess returns) in the complexity – specificity space. The region outlined in Fig. 7 containing the rules obtained with a 7.5-year training duration is characterized by both lower trading frequencies as well as improved performance. An important aspect of both of these figures is that they enable us to visually interpret the effects of complexity and specificity of the rules with respect to their trading characteristics and performance. It can be seen that as the rules become overly complex (at any given level of specificity), they trade more often (Fig. 8) and are accompanied with a noticeable decline in performance (Fig. 9). While this might lead one to conclude that controlling the complexity of the rules generated holds the key to the performance of the rules, the role of specificity in offsetting the performance decline ought to be noted. As the complexity increases, the number of scenarios under which the rules signal a TRUE increases (thereby increasing the potential for higher trading frequency); the specificity of the rule plays a key role in determining how narrowly a scenario is defined (the minimum number of terms required to be satisfied to signal a TRUE). This increase in the number of terms required to define a scenario essentially creates an offset thereby preventing a rapid rise in the trading frequency (Fig. 8). The effect of this offset is evidenced in the shallower decline in performance with increasing complexity for higher specificity values. For example, closer spacing between contours indicates a higher gradient in performance degradation with increasing complexity for specificity of 2 compared to the shallower gradient in performance degradation with increasing complexity for specificity of 3.

![](/api/attachments/5XRT44Y4/fulltext/images/462ee9abd567790189b38debb8c0122023aa174ac733fd12d8714d8393c54409.jpg)  
Fig. 8. Trading frequency of rules.

![](/api/attachments/5XRT44Y4/fulltext/images/1a557d6c7af97c0408224646f8a7918656348064e8009e4e292d2dbd8b5ba8db.jpg)  
Fig. 9. Annual excess returns earned by the rules.

While increasing complexity is clearly detrimental to the performance of the rule and the decline in performance is offset with increase in the specificity of the rule, the offset is sufficient for controlling the increase in trading frequency but unable to completely arrest the declining performance (contours in the top-right quadrant of the graph). Thus, a combined interpretation of Figs. 6 –9 would suggest that in addition to the trading frequency of the rules obtained, an examination of the nature of the rules (measured in terms of their complexity and specificity) is necessary to obtain an indication of the rules’ performance.

## 6. Discussion

Learning of robust trading rules requires the ability to prevent overfit to noise accompanied with the ability to isolate patterns for formulating profitable trading strategies. Research thus far had focused on preventing this fit to noise by appropriate formulation of evaluation criterion—such as design of fitness functions, use of bootstrap methods, and, in general, use of long training durations. While the first two are invaluable in their contribution for preventing fit to noise, we show that the use of long training horizon can actually be detrimental to discovery of rules with requisite performance desirables. While rules with too short a horizon do tend to overfit to noise, too long a horizon prevents discovery of rules that may hold higher predictive ability in the near term. We also show that performance in the training data is not necessarily indicative of a rule’s ability to learn profitable pattern(s).

Considering that our conclusions are ex-post in that we had the luxury of having the test data—in practice how is one to know the appropriate training duration for their application? To this end we see that the characteristics, other than performance, can play a crucial role in aiding the selection of appropriate training duration. While seemingly trading frequency by itself would suffice as an indicator of performance (Fig. 6), subsequent analysis (Figs. 8 and 9) indicates the role played by complexity and specificity of the rules in determining the trading characteristics and hence the performance. It is shown that the changes in the nature of rules can further aid in the identification of rules that are likely to perform well into the predictive period. Our results show that the examination of trading characteristics such as trading frequency together with nature of the rules (complexity and specificity) can provide important cues in this regard. We have shown that the magnitude of each of these two measures and consistency in their values over independent trials are directly indicative of their performance in the test period.

## 7. Limitations and future research

The regular approach to evaluating the fitness during learning, as used in this research, can in general be prone to overfit. An important next step would be to examine the same using a bootstrap method for fitness evaluation, to examine if controlling for overfit to noise through bootstrapping helps discover patterns with higher short-term predictive ability. Studies in neural networks using backpropagation neural networks with different training durations have shown that decline in performance can be arrested by controlling for coverage during learning [9]. In the case of evolutionary algorithms, a similar study would help establish the usefulness of the complexity and specificity measures during learning specifically aimed at rule generation and candidate selection for crossover.

Another aspect that needs further investigation relates to the differences in the discovered rules with respect to the patterns that they incorporate. In Ref. [13], the authors have shown that integrating multiple trading rules (obtained from independent GA trials) embodying diverse patterns can yield further performance improvements. There is an even greater potential for such improvement in this case where rules learnt from different training horizons are likely to embody patterns with predictive abilities spanning different time horizons.

Finally, while our findings have been shown to work for the S&P500 (and potentially for other financial time series), the scope of our results extend to other domains also—particularly in the area of data mining for intrusion detection where the dynamics of the time series change rapidly with the introduction of new technology and regular discovery of newer techniques for hacking.

## References

[1] F. Allen, F. Karajalainen, Using genetic algorithms to find technical trading rules, Rodney L. White Center for Financial Research, The Wharton School, University of Pennsylvania, Technical Report 20-93, 1993.

[2] W.B. Arthur, J.H. Holland, B. LeBaron, R. Palmer, P. Tayler, Asset Pricing Under Endogenous Expectations in an Artificial Stock Market, Santa Fe Institute Working Paper 96-12-093, 1996.

[3] W.B. Arthur, S.N. Durlauf, D.A. Lane (Eds.), The Economy as an Evolving Complex System: II. Proceedings Vol. XXVII, SFI Studies in the Sciences of Complexity, Addison-Wesley, Reading, MA, 1997.

[4] W.A. Brock, Asset pricing behavior in complex environments, in: W.B. Arthur, D. Lane, S. Durlauf (Eds.), The Economy as an Evolving, Complex System: II. Proceedings Vol. XXVII, SFI Studies in the Sciences of Complexity, Addison-Wesley, Reading, MA, 1997.

[5] W. Brock, J. Lakonishok, B. LeBaron, Simple technical trading rules and the stochastic properties of stock returns, Journal of Finance 47 (5) (1992) 1731 – 1764.

[6] S.-H. Chen (Ed.), Evolutionary Computation in Economics and Finance, Physica-Verlag, New York, 2002.

[7] M.M. Dacorogna, U.A. Muller, C. Jost, O.V. Pictet, R.B. Olsen, J.R. Ward, Heterogeneous real-time trading strategies in the foreign exchange market, The European Journal of Finance 1 (1995) 383 – 403.

[8] J.D. Farmer, A. Lo, Frontiers of finance: evolution and efficient markets, Proceedings of the National Academy of Sciences 96 (1999) 9991– 9992.

[9] B. Kovalerchuk, E. Vityaev, Data Mining in Finance, Kluwer Academic Publishers, Hingham, MA, 2000.

[10] B. LeBaron, Technical trading rules and regime shifts in foreign exchange, Santa Fe Institute Working Paper 91-10-044, 1991.

[11] B. LeBaron, A.S. Weigend, A bootstrap evaluation of the effect of data splitting on financial time series, IEEE Transactions on Neural Networks (1998) 213 – 220.

[12] T. Lux, M. Marchesi, Volatility clustering in financial markets: a micro-simulation of interacting agents, Journal of Theoretical and Applied Finance 3 (2001) 675 – 702.

[13] K. Mehta, S. Bhattacharyya, Combining rules learnt using genetic algorithms for financial forecasting, Proceedings of the Congress on Evolutionary Computation, IEEE Press, Piscataway, WJ, 1999, pp. 1245–1252.

[14] K. Mehta, S. Bhattacharyya, Evolutionary Mining of Trading Rules: Improving Performance Desirables through Evaluation Criterion and Integration, Working Paper, University of Connecticut, 2002.

[15] M. Mitchell, S. Forrest, Genetic algorithms and artificial life, Artifical Life 1 (3) (1994) 267 – 289.

[16] C. Neely, P. Weller, R. Ditmar, Is technical analysis in foreign exchange market profitable? A genetic programming ap-

proach, Journal of Financial and Quantitative Analysis 32 (4) (1997) 405– 427.

[17] O.V. Pictet, M.M. Dacorogna, U.A. Mu¨ller, R.B. Olsen, J.R. Ward, Real-time trading models for foreign exchange rates, Neural Network World 2 (6) (1992) 713– 744.

[18] O.V. Pictet, M.M. Docorogna, B. Chopard, M.O.R. Shirru, M. Tomassini, Using genetic algorithms for robust optimization in financial applications, Neural Network World 5 (1995) 573 – 587.

[19] P. Turney, How to shift bias: lessons from the Baldwin effect, Evolutionary Computation 4 (3) (1996) 271– 295.

[20] P. Utgoff, Shift of bias for inductive concept learning, in: R.S. Michalski, J.G. Carbonell, T.M. Mitchell (Eds.), Machine Learning: An Artificial Intelligence Approach, vol. 2, Morgan-Kaufmann, Los Altos, CA, 1986, pp. 163 – 190.

[21] A.S. Weigend, B.A. Huberman, D.E. Rumelhart, Predicting sunspots and exchange rates with connectionist networks, in: M. Casdagli, S. Eubanks (Eds.), Nonlinear Modeling and Forecasting, Addison-Wesley, Reading, MA, 1992, pp. 395 – 432.

[22] S. Weigend, N.A. Gershenfeld (Eds.), Time Series Predictions, Addison-Wesley, Reading, MA, 1994.

[23] D. Wolpert, Stacked generalization, Neural Networks 5 (1992) 241–259.

[24] D. Wolpert, Off-training set error and a priori distinctions between learning algorithms, Technical Report SFI-TR-95- 01-003, Santa Fe Institute, 1994.

Kumar Mehta is an Assistant Professor in the Department of Operations and Information Management at the University of Connecticut. He earned his doctorate from the University of Illinois at Chicago in 2002. His research interests include Data Mining, Information Retrieval and Agent-based Computational Modeling.

Siddhartha Bhattacharyya is an Associate Professor in the Information and Decision Sciences Department of the College of Business at the University of Illinois at Chicago. He earned his doctorate from the University of Florida. His research interests include theory and application of evolutionary computation approaches, agentbased computational modeling, data mining and the provision of intelligent decision support in finance, marketing and manufacturing. His research appears in a range of academic journals and he has presented his work in numerous academic and industry conferences.

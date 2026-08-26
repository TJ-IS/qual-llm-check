---
otero_id: 21575
otero_key: "YW6HMMPJ"
title: "Forecasting S&P 500 stock index futures with a hybrid AI system"
authors: "Ray Tsaih; Yenshan Hsu; Charles C. Lai"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00028-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Forecasting S&P 500 stock index futures with a hybrid AI system

Ray Tsaih <sup>a,)</sup>, Yenshan Hsu <sup>b</sup>, Charles C. Lai <sup>a</sup>

Department of Management Information Systems, National Chengchi UniÕersity, Taipei, Taiwan b Department of Finance, National Chengchi UniÕersity, Taipei, Taiwan

Received 1 August 1996; revised 1 June 1997; accepted 1 January 1998

## Abstract

This study presents a hybrid AI artificial intelligence approach to the implementation of trading strategies in the S&PŽ . 500 stock index futures market. The hybrid AI approach integrates the rule-based systems technique and the neural networks technique to accurately predict the direction of daily price changes in S&P 500 stock index futures. By highlighting the advantages and overcoming the limitations of both the neural networks technique and rule-based systems technique, the hybrid approach can facilitate the development of more reliable intelligent systems to model expert thinking and to support the decision-making processes. Our methodology differs from other studies in two respects. First, the rule-based systems approach is applied to provide neural networks with training examples. Second, we employ Reasoning Neural Networks Ž . RN instead of Back Propagation Networks. Empirical results demonstrate that RN outperforms the other two ANN models Ž . Back Propagation Networks and Perceptron . Based upon this hybrid AI approach, the integrated futures trading system Ž . IFTS is established and employed to trade the S&P 500 stock index futures contracts. Empirical results also confirm that IFTS outperformed the passive buy-and-hold investment strategy during the 6-year testing period from 1988 to 1993. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Hybrid AI system; Rule-based system; Reasoning Neural Networks; Back Propagation Networks; S&P 500 stock index futures

## 1. Introduction

## 1.1. Problem statements

In modern finance, derivatives such as futures and options play increasingly prominent roles not only in risk management activities but also in price speculative activities. Owing to the high-leverage characteristic involved in derivative tradings, investors can gain enormous profits with a small amount of capital if they can accurately predict the market’s direction. However, many factors influence financial markets, including political events, general economic conditions, and traders’ expectations. Therefore, predicting the financial market’s movements is quite difficult.

Increasingly, according to academic investigations, movements in market prices are not random.

Rather, they behave in a highly nonlinear, dynamic manner. The standard random walk assumption of futures prices may merely be a veil of randomness that shrouds a noisy nonlinear process 2,6,7 . To<sup>w</sup> <sup>x</sup> remove this veil and to make the forecasting of futures prices more reliable, the application of expert systems and neural networks have received extensive attention 1,3,8,10,11,16,17 .<sup>w</sup> <sup>x</sup>

Rule-based systems and neural networks originate from work in the field of AI. Rule-based expert systems, which emerged in the early 1970s, have received wide interest and have represented the bulk of expert systems applications today. The knowledge of rule-based systems is stored or presented primarily in the form of rules and as problem-solving procedures. Knowledge embedded in the system is easy to read because it uses explicit rules condition- Ž and-action relationships . In addition, providing ex- . planations for the decisions made by rule-based systems is also feasible since the antecedents of rules specify exactly what conditions activate the rule. Therefore, the primary advantage of rule-based systems over their neural networks counterpart is the ‘readability’ of the process that the system utilizes to make decisions 23 .<sup>w</sup> <sup>x</sup>

In summary, rule-based systems are quite appropriate for frequently recurring problems that are naturally well-handled by rules. However, the rule-based systems approach is limited by its requirement for explicit rules. This problem arises because most human knowledge is implicit, particularly experts knowledge.

In contrast to rule-based systems, neural networks attempt to emulate the biological system of the human brain in learning and identifying patterns. Moreover, neural networks can more aptly recognize poorly defined patterns. Instead of extracting explicit rules from domain experts, the neural networks approach employs a learning algorithm to autonomously: a extract the functional relationship Ž . between input and output, which is embedded in a set of historical data called training examples , and Ž . Ž . b encode it in connection weights. Training examples that are readily available allow neural networks to capture a large volume of information in a rather short period of time and to continuously learn throughout its lifespan. Furthermore, neural networks have the ability to not only deal with noisy, incomplete, or previously unseen input patterns, but to also generate a reasonable response. However, reading and understanding the knowledge in neural networks is difficult because knowledge is distributed over the entire network.

By highlighting the advantages and overcoming the limitations of both the neural networks technique and rule-based systems technique, the hybrid approach can facilitate the development of more reliable intelligent systems to model expert thinking and to support the decision-making processes. To our knowledge, two studies Bergerson and Wunsch 1Ž <sup>w</sup> <sup>x</sup> and Trippi and Desieno 16 have integrated both <sup>w</sup> <sup>x</sup>. the neural networks technique and rule-based systems technique to implement their trading strategies in the S&P 500 index futures market.

Bergerson and Wunsch 1 constructed a rule- <sup>w</sup> <sup>x</sup> based daily trading system augmented by a neural network market predictor. They used Back Propagation networks BP to predict the market and also Ž . employed a risk-management rule to curtail trading losses. However, they expended the majority of their efforts in picking out training examples and in selecting parameters for the neural network system’s architecture. Hence, their method relies heavily on manual procedures.

In a related work, Trippi and DeSieno 16 de-<sup>w</sup> <sup>x</sup> signed a neural network-based intraday trading system assisted by a set of composite trading decision rules. Their system consisted of several trained neural networks and a set of rules for combining the neural networks’ results to generate a composite recommendation for the current day’s position. However, in contrast to Bergerson and Wunsch 1 , they<sup>w</sup> <sup>x</sup> merely fed neural networks with massive amounts of historical data.

Studies of Bergerson and Wunsch 1 and Trippi<sup>w</sup> <sup>x</sup> and DeSieno 16 are inhibited in two distinct ways.<sup>w</sup> <sup>x</sup> First, the ways of picking out training examples adopted in both studies are rather inefficient. One involves picking out training examples manually, the other, feeds in massive amounts of historical data. Second, BP is used in both studies. Although the multi-layered networks with the back propagation learning algorithm 15 have excited the connection- <sup>w</sup> <sup>x</sup> ists and rehabilitated confidence in neural networks, several associated undesirable predicaments have caused their effectiveness to deteriorate: 1 exactly Ž .

how many hidden nodes are necessary for a specific problem is generally unknown; and 2 learning mightŽ . converge to an undesired attractor e.g., a relativelyŽ optimal network solution , despite the existence of. the desired network solution.

These undesirable predicaments might significantly hinder $\mathrm { B P } ^ { * } \mathrm { s }$ performance. Appendix A provides a brief explanation of such predicaments. Also, more detailed information can be found in Ref. 9 .<sup>w</sup> <sup>x</sup> However, Refs. 1,16 do not address how to resolve <sup>w</sup> <sup>x</sup> the above predicaments.

## 1.2. Proposed approaches

By overcoming the above drawbacks, this study presents a superior approach to establishing a hybrid AI system that can implement the trading strategies in the S&P 500 stock index futures market. Our approach is as follows: first, the rule-based systems provide training examples to neural networks, in contrast to feeding in massive amounts of historical data or manually picking out training examples. Second, Reasoning Neural Networks RN 18–22 isŽ . <sup>w</sup> <sup>x</sup> adopted herein to avoid the undesired predicaments encountered in BP. RN has been applied to several categorization problems 5,13,20 . Empirical results in these studies demonstrate the following:

1. RN’s learning is always completed;

2. RN’s number of required hidden nodes is less than $\mathrm { B P } ^ { \bullet } \mathbf { s } ;$

3. RN’s learning speed is much faster than the back propagation learning algorithm; and

4. RN’s internal representation is more acceptable, compared with $\mathrm { B P } ^ { * } \mathrm { s }$ .

Restated, RN can resolve the undesired predicaments associated with BP.

This study presents dual forecast models that is,Ž a futures forecast model FFM and an extendedŽ . futures forecast model EFFM to accurately predict Ž .. the direction of daily price changes in S&P 500 index futures. In addition, FFM is set up with the conventional rule-based systems technique, while EFFM is set up with the neural networks technique. Moreover, the integrated futures trading system Ž . IFTS , which integrates FFM and EFFM, is designed to provide investors with daily trading suggestions on the S&P 500 index futures contracts.

## 2. The proposed hybrid AI system

## 2.1. Futures forecast model

FFM adopts the conventional rule-based systems. We derive the knowledge and rules from scholars and experts who are specializing in trading S&P 500 stock index futures. The following description explains the derived rules which are embedded in our FFM.

S&P 500 stock index futures contracts expire four times annually. Daily closing price closes dataŽ . from the nearby contracts are constructed over the period from December 1983 to December 1993. Since we attempt to forecast the direction of daily price change in S&P 500 index futures, only technical indicators are used as inputs. A variety of technical indicators are available. Some technical indicators are effective under trending markets and others perform better under nontrending or cyclical markets. The linear regression analysis and the relative strength index RSI are employed to derive 10Ž . variables of inputs from the daily closes under trending and nontrending markets, respectively. <sup>1</sup> Table 1 lists the definitions of 10 derived input variables. SP, SN, LU and LD are derived from the following linear regression model with 14 days of data: 2

$$
C _ {t} = \alpha + \beta * t + \varepsilon_ {t}, \quad t = 1, 2, \dots , 1 4\tag{1}
$$

where $C _ { t }$ denotes the close on day t, and $\beta$ are unknown parameters, t represents the time variable, and $ { \varepsilon } _ { t }$ is the random disturbance term.

Output of the regression model gives values for Ž .intercept and $\beta$ Ž . slope . The slope is positive when prices are rising and negative when they are falling. Linear regression analysis also provides the coefficient of determination, denoted by $r ^ { 2 }$ , to measure the strength of the linear relationship. We test whether the slope is statistically significant positive or nega-Ž . tive by comparing the $r ^ { \frac { \mathbf { \sigma } } { 2 } }$ value to a critical value based on a 5% significance level. We designed the SP and SN variables to show the direction as well as the strength of the price trend. The SP variable is set to 1 when the slope is significantly positive. Meanwhile, the SN variable is set to 1 when the slope is significantly negative.

Table 1  
The definitions of 10 derived variables

<table><tr><td>Variable</td><td>Description</td></tr><tr><td>SP</td><td>Equals 1 when the slope of price trend is significantly positivea; -1, otherwise.</td></tr><tr><td>SN</td><td>Equals 1 when the slope of price trend is significantly negativea; -1, otherwise.</td></tr><tr><td>LU *</td><td>Equals 1 when the oscillatorbcrosses upward over its 3-day moving averagec; -1 otherwise.</td></tr><tr><td>LD *</td><td>Equals 1 when the oscillatorbcrosses downward over its 3-day moving averagec; -1 otherwise.</td></tr><tr><td>UD</td><td>Equals 1 when the closing price of the index is up at the present day; -1, otherwise.</td></tr><tr><td>AUD</td><td>Equals 1 when the closing prices are either up or down consecutively for at least 3 days; -1 otherwise.</td></tr><tr><td>RSI1 *</td><td>Equals 1 when the stochastic RSIdfalls from 100; -1 otherwise.</td></tr><tr><td>RSI2 *</td><td>Equals 1 when the stochastic RSIdrises from 0; -1 otherwise.</td></tr><tr><td>RSI3</td><td>Equals 1 when the stochastic RSIdis greater than 90; -1 otherwise.</td></tr><tr><td>RSI4</td><td>Equals 1 when the stochastic RSIdis less than 10; -1 otherwise.</td></tr></table>

)These variables serve as triggers.  
<sup>a</sup> We test whether the slope is statistically significant positive orŽ negative based on a 5% significance level; see Eq. 1 .. Ž .  
<sup>b</sup> The forecast oscillator FO is computed according to Eq. 2 . Ž . Ž .  
<sup>c</sup> The 3-day moving average line of the forecast oscillator is computed according to Eq. 3 .Ž .  
<sup>d</sup> The stochastic RSI is computed according to Eq. 4 . Ž .

For LU and LD variables, we develop an oscillator based on the regression forecast. We compute the forecast oscillator FO according to the followingŽ . equation:

$$
\mathrm{FO} = 1 0 0 * \frac {C - C _ {\mathrm{f}}}{C}\tag{2}
$$

where C denotes the daily close and $C _ { \mathrm { f } }$ represents today’s forecast close from the previous 14 daily closes based on Eq. 1 . Hence the forecast oscillatorŽ .

is constructed on the basis of the difference of the realized close and the forecast close from the regression. Then, we develop a 3-day moving average line of the forecast oscillator:

$$
\mathrm{MA} _ {\mathrm{t}} (3) = \frac {\mathrm{FO} _ {t} + \mathrm{FO} _ {t - 1} + \mathrm{FO} _ {t - 2}}{3}\tag{3}
$$

The LU variable is set to 1 if the oscillator crosses upward over its 3-day moving average and the LD variable set to 1 if the oscillator crosses downward under its 3-day moving average. That the oscillator moves above or below its 3-day moving averageŽ . signals the potential trend change in prices. In facing the down trend, selling the futures might be desirable; when facing an up trend, purchasing the futures might be desirable. Thus, LU and LD are designed to signal the trading opportunities, and serve as triggers <sup>3</sup> of our hybrid AI system.

Both UD and AUD variables also attempt to capture the current market trend at 1 day and 3 days, respectively. UD is set to 1 if today’s close exceeds yesterday’s; otherwise, it is set to <sup>y</sup>1. AUD is set to 1 if the close moves upward or downward consecutively for three trading days; otherwise, it is set to <sup>y</sup>1.

RSI1, RSI2, RSI3 and RSI4 belong to the stochastic RSI oscillator stochRSI . The relative strengthŽ . index RSI is quite effective in extracting price Ž . information for a nontrending market. A stochRSI oscillator is computed as follows:

$$
\mathrm{stochRSI} = 1 0 0 * \frac {\mathrm{RSI} - \mathrm{RSI} _ {\mathrm{L}}}{\mathrm{RSI} _ {\mathrm{H}} - \mathrm{RSI} _ {\mathrm{L}}}\tag{4}
$$

where $\mathrm { R S I } = 1 0 0 * ( S _ { \mathrm { u } } ) / ( S _ { \mathrm { u } } - S _ { \mathrm { d } } ) ; \ S _ { \mathrm { u } } =$ the sum of up-day momentum over a 14-day period; the up-day momentum is zero if today’s close is less than yesterday’s; otherwise, it is the absolute difference between the two closes; $S _ { \mathrm { d } } =$ the sum of down-day momentum over a 14-day period; the down-day momentum is zero if today’s close is greater than yesterday’s; otherwise, it is the absolute difference between the two closes; ${ \mathrm { R S I } } _ { \mathrm { H } } =$ the highest RSI among the current RSI and the preceding 13 RSIs; ${ \mathrm { R S I } } _ { \mathrm { L } } = { \mathrm { t h e } }$ lowest RSI among the current RSI and the preceding 13 RSIs.

The stochRSI measures the location of RSI within its recent range, indicating short-term momentum extremes. According to Eq. 4 , stochRSI will be 100Ž . if today’s RSI is the highest one and it will be zero if today’s RSI is the lowest one. A stochRSI value of 100 provides an excellent entry point into the down trend. In contrast, a stochRSI value of zero provides an excellent entry point into the up trend. Both RSI1 and RSI2 variables serve as triggers in detecting the trading opportunities.

Assume that you sold the futures when the stochRSI was 100; then the up trend resumes and the stochRSI again moves above 90 toward 100. Reversing the short position to a long position would be desirable. On the other hand, assume that you purchased the futures when the stochRSI was zero; the down trend then resumes and the stochRSI again moves below 10 toward zero. Reversing the long position to a short position would be desirable. With this in mind, both RSI3 and RSI4 are designed and used to capture the current market trend.

In summary, among these 10 variables, four i.e.,Ž LU, LD, RSI1, and RSI2 serve as triggers and the . other six i.e., SP, SN, UD, AUD, RSI3, and RSI4Ž . capture the tendencies of the current futures market.

For each trading day, we not only derive the values of these 10 variables from the closing data, but also use the derived information to describe the features of the current futures market. Notably, the same information i.e., values of the 10 variables Ž . can be derived from the price data observed at different time epochs. If each distinct set of derived information is called a case, the market’s daily conditions can be divided into at most 1024 cases with 10 variables. Restated, we categorize the daily conditions of the futures market into a variety of cases through processing futures historical data. According to the derived case information, each trading day becomes a case observation. During a particular time period, one case might recur several times, thereby allowing for several observations of this case. Those observations provide further insight into the fre-<sup>4</sup> quency of there being an up-day and a down-Ž <sup>5</sup> day for the case occurring during the observed. period. For instance, assume that a case has 10 observations observed previously, among which six are up days and four are down days. Thus, the observations suggest that previously the case occurred with a 60% frequency on an up day and a 40% frequency on a down day. Once a case is

Table 2  
The definitions of rules used to categorize the cases

<table><tr><td>Case group</td><td>Definition</td></tr><tr><td>Trigger_OFF</td><td>LU = -1 and LD = -1 and RSI1 = -1 and RSI2 = -1.</td></tr><tr><td>Trigger_ON:</td><td>LU = 1 or LD = 1 or RSI1 = 1 or RSI2 = 1.</td></tr><tr><td>Obvious_LONG</td><td>(LU = 1 or LD = 1 or RSI1 = 1 or RSI2 = 1) and (at least 55% of the observations.in the past 4 years are up-days)a.</td></tr><tr><td>Obvious_SHORT</td><td>(LU = 1 or LD = 1 or RSI1 = 1 or RSI2 = 1) and (at least 55% of the observationsin the past 4 years are down-days)a.</td></tr><tr><td>Obvious_WAIT</td><td>(LU = 1 or LD = 1 or RSI1 = 1 or RSI2 = 1) and (observations of past 4 years are exactly 50% up-days and exactly 50% down-days)a.</td></tr><tr><td>Non-obvious</td><td>(LU = 1 or LD = 1 or RSI1 = 1 or RSI2 = 1) and otherwise.</td></tr><tr><td>Unobserved</td><td>case not observed from the observations of past 4 years.</td></tr></table>

If the next day’s closing price exceeds the current day’s, we define that as an up-day occurrence; if the next day’s closing price is less than the current day’s, we define that as a down-day occurrence.  
<sup>a</sup> We have evaluated the forecasting performances with various values of Y Ž . Ž the length of the observed period and P the threshold percentage used to classify the case .. Y had been 3, 4, 5, or 6; P had been 50%, 55%, 60%, or 65%. If Y is too short, the amount of samples is so small that the result of analyzing the observed cases is statistically insufficient. However, if Y is too long, the result of the analysis may be biased due to including too much historical data. If P is too low, the new obvious cases behave the same as their past counterparts. If P is too high, there are too few obvious cases. From the testing results, Y <sup>s</sup>4 and P <sup>s</sup>55% is the best one. So Y <sup>s</sup>4 and P <sup>s</sup>55% is adopted for the ongoing research. For the detailed information, please refer to Ref. 12 . <sup>w</sup> <sup>x</sup>

```txt
The algorithm for constructing the RB system

Step 1 Set U1, U2, U3, U4, D1, D2, D3, D4 equal 0 initially;
If LU = 1 then count the number of up-days (U1) and down-days (D1) from the observations of cases during the past 4 years whose LU = 1 and SP, SN, UD, AUD, RSI3 and RSI4 are the same as the case;
If LD = 1 then count the number of up-days (U2) and down-days (D2) from the observations of cases during the past 4 years whose LD = 1 and SP, SN, UD, AUD, RSI3 and RSI4 are the same as the case;
If RSI1 = 1 then count the number of up-days (U3) and down-days (D3) from the observations of cases during the past 4 years whose RSI1 = 1 and SP, SN, UD, AUD, RSI3 and RSI4 are the same as the case;
If RSI2 = 1 then count the number of up-days (U4) and down-days (D4) from the observations of cases during the past 4 years whose RSI2 = 1 and SP, SN, UD, AUD, RSI3 and RSI4 are the same as the case.

Step 2 Let U# = U1 + U2 + U3 + U4 and D# = D1 + D2 + D3 + D4;
Let U% = U#/(U# + D#) and D% = D#/(U# + D#);
If U# = D# = 0 then case_result = Unobserved;
If U% >= 55% then case_result = Obvious_LONG;
If D% >= 55% then case_result = Obvious_SHORT;
If U% = D% = 50% then case_result = Obvious_WAIT;
If ((55% > U% > 50%) or (55% > D% > 50%)) then case_result = Non_Obvious.
```

presented, rules shown in Table 2 are used to categorize it. These rules are implemented in the algorithm of Table 3 which is employed to analyze the derived cases information of the previous 4 years to establish the rule-based system RB . This RB system is usedŽ . to identify cases in the upcoming year. For instance, a case that is Obvious\_LONG Ž . \_SHORT implies that at least 55% of the observations of this case in the previous 4 years are up down days. A circum-Ž . stance in which the market conditions only slightly change in the near future makes the information of being Obvious\_LONG or ObviousŽ . \_\_SHORT quite useful for forecasting the direction of price changes in the future. <sup>6</sup> This idea is implemented in the FFM algorithm, as presented in Table 4.

```txt
Table 4
The algorithm of FFM

Step 1 If LU = LD = RSI1 = RSI2 = -1 then case_result = Trigger_OFF and take a rest.
Step 2 case_result = RB(case)
Step 3 If case_result = Obvious_LONG then long (buy) a futures contract;
If case_result = Obvious_SHORT then short (sell) a futures contract;
If (case_result = Obvious_WAIT or case_result = Non_Obvious or case_result = Unobserved or case_result = Trigger_OFF) then take a rest.
```  
Step 1 checks whether there is any activated trigger; if there is none, the system makes no suggestion about the trading decision. In Step 2, the RB system identifies the case. In Step 3, the system makes the trading suggestion for the case of either Obvious\_LONG or Obvious\_SHORT.

## 2.2. Extended futures forecast model

The information source of FFM is primarily the accumulation of previous case observations i.e., theŽ RB . Basically, RB provides information regarding . previous obvious cases to forecast the obvious cases of the future, and information regarding previous non-obvious cases to forecast the non-obvious cases of the future. Thus, RB provides useful trading suggestions for the obvious cases, but does not adequately handle the non-obvious cases since the previous non-obvious case cannot offer sufficient information to accurately forecast the future non-obvious case. The empirical testing results also verify this intuition. <sup>7</sup> Therefore, FFM utilizes RB to merely forecast the obvious cases of the future. Moreover, EFFM is designed to facilitate FFM in dealing with the non-obvious cases.

A circumstance in which a the obvious cases areŽ . the majority of the market and b the previousŽ . obvious case can provide good trading suggestions for the obvious cases allows us to assume that the mechanism embedded in the obvious case can capture the majority of the market trend. Restated, the information embedded in the set of obvious cases is helpful in dealing with the non-obvious cases. Therefore, how to obtain and utilize the useful implicit information embedded in the set of obvious cases are relevant tasks. To achieve such tasks, the neural networks technique is applied toward EFFM.

The main components of EFFM are the four artificial Neural Networks ANN systems. Once aŽ . non-obvious case is presented, each of its four trigger variables i.e., LU, LD, RSI1, and RSI2 is used Ž . respectively to trigger an ANN. Restated, each of the four ANNs is executed only when its corresponding trigger is on. Next, the values of the current day’s six status variables i.e., SP, SN, UD, AUD, RSI3, andŽ RSI4 are fed into ANN as inputs. Two output nodes. Ž <sup>w</sup> <sup>x2</sup> are used here; the output vector which <sup>g</sup> <sup>y</sup>1, 1 . will show the recommendation opinion see Table 5 .Ž . The triggered ANNs forecast the direction of price changes. A voting mechanism is used to combine the opinions of these ANNs. Thereafter, EFFM recommends what the trading decision should be for the non-obvious case. Table 6 displays the algorithm corresponding to EFFM.

In the set-up stage of EFFM, the previous obvious cases picked up from the RB system are used as training examples of ANN. Among those cases are included the O bvious\_LO N G cases, the Obvious\_SHORT cases, and the Obvious\_WAIT cases. Each case is translated into the format of a training input–output vector. The input vector denotes the values of the six status variables; Table 7 defines the desired output vector. The value of each trigger variable determines whether a training case should be assigned to its corresponding ANN. With the associated training examples, each of the four ANNs develops its own network structure.

Table 5  
The output values of ANN and their corresponding recommendations

<table><tr><td>Output</td><td>Recommendation</td></tr><tr><td>(1, -1)</td><td>LONG</td></tr><tr><td>(-1, 1)</td><td>SHORT</td></tr><tr><td>(-1, -1)</td><td>WAIT</td></tr><tr><td>(1, 1)</td><td>No comment</td></tr></table>

```txt
Table 6
The algorithm of EFFM

Step 1 Set #L, #S equal 0 initially;
    If LU = 1 then
    Run the ANN for LU;
    If the output of the ANN is LONG then #L = #L + 1;
    If the output of the ANN is SHORT then #S = #S + 1;
    If LD = 1 then
    Run the ANN for LD;
    If the output of the ANN is LONG then #L = #L + 1;
    If the output of the ANN is SHORT then #S = #S + 1;
    If RSI1 = 1 then
    Run the ANN for RSI1;
    If the output of the ANN is LONG then #L = #L + 1;
    If the output of the ANN is SHORT then #S = #S + 1;
    If RSI2 = 1 then
    Run the ANN for RSI2;
    If the output of the RN is LONG then #L = #L + 1;
    If the output of the RN is SHORT then #S = #S + 1.

Step 2 If #L > #S then recommendation = LONG
    Else if #L < #S then recommendation = SHORT
    Else recommendation = WAIT;

Step 3 If recommendation = LONG, then long futures contract;
    If recommendation = SHORT, then short futures contract;
    If recommendation = WAIT, then take a rest.
```  
Step 1 says that an ANN is run when its corresponding trigger is activated. In Step 2, a voting mechanism is used to combine the four ANNs’ opinions. Step 3 makes the trading suggestion for the case.

Notably, the above design does not specify the type of ANN model; adopting a different ANN model in EFFM would yield a different forecasting performance. To select an appropriate ANN model for EFFM, we evaluate the forecasting performance of the three ANN models: Perceptron PN 14 , BPŽ . <sup>w</sup> <sup>x</sup> <sup>w x</sup> <sup>w</sup> <sup>x</sup> 9 , and RN 19 . The three ANNs models i.e., PN,Ž BP and RN are trained with the same obvious cases.

Table 7  
The definition of the desired output values for the ANNs

<table><tr><td>Case</td><td>Desired output values</td></tr><tr><td>Obvious_LONG</td><td>(1, -1)</td></tr><tr><td>Obvious_SHORT</td><td>(-1, 1)</td></tr><tr><td>Obvious_WAIT</td><td>(-1, -1)</td></tr></table>

in the preceding 4 years; the trained ANNs are then placed into EFFM. Next, EFFMs are applied to the non-obvious cases of the following year to assess their performance throughout the period from 1984 to 1993. The fact that different initial weights may yield different learning results in ANNs accounts for why we make five independent replications runs ofŽ . the simulation.

Table 8 summarizes the forecasting performances of the various EFFM configurations. In Table 8, the number of test equals the difference of the amount of the observed non-obvious cases and the ‘No Comment’ cases, and success is achieved when the actual output is the same as the desired output. The success rate equals the ratio of the number of successes to the number of tests. Table 8 reveals that most annual success rates exceed 50%.

With all average success rates exceeding 50%, EFFM exhibits the ability to handle the non-obvious cases. Furthermore, empirical results demonstrate that the RN model is better than the BP and PN according to the following considerations. One consideration is based on the mean of the average success rates $( \mu _ { 1 } )$ and the mean of total successful test samples $\displaystyle ( \mu _ { 2 } )$ . These two means are calculated from the five replications. An ANN model having a higher $\mu _ { 1 }$ and higher $\mu _ { 2 }$ is better. As Table 9 reveals, EFFM with RN has a higher $\mu _ { 1 }$ and higher $\mu _ { 2 }$ than BP and PN.

Table 8  
The forecasting performances of the various EFFM configurations

<table><tr><td></td><td>Year</td><td>1988</td><td>1989</td><td>1990</td><td>1991</td><td>1992</td><td>1993</td><td>1988–1993</td></tr><tr><td colspan="9">Panel A: EFFM with  $RN^a$ </td></tr><tr><td rowspan="2">Replication 1</td><td>Number of tests</td><td>15</td><td>17</td><td>16</td><td>15</td><td>14</td><td>18</td><td>95</td></tr><tr><td>Success rate (%)</td><td>66.67</td><td>76.47</td><td>56.25</td><td>33.33</td><td>71.43</td><td>55.56</td><td>60.00</td></tr><tr><td rowspan="2">Replication 2</td><td>Number of tests</td><td>21</td><td>20</td><td>14</td><td>15</td><td>14</td><td>18</td><td>102</td></tr><tr><td>Success rate (%)</td><td>66.67</td><td>55.00</td><td>57.14</td><td>33.33</td><td>71.43</td><td>55.56</td><td>61.17</td></tr><tr><td rowspan="2">Replication 3</td><td>Number of tests</td><td>21</td><td>20</td><td>15</td><td>15</td><td>14</td><td>18</td><td>103</td></tr><tr><td>Success rate (%)</td><td>66.67</td><td>80.00</td><td>53.33</td><td>33.33</td><td>71.43</td><td>55.56</td><td>61.17</td></tr><tr><td rowspan="2">Replication 4</td><td>Number of tests</td><td>21</td><td>17</td><td>14</td><td>15</td><td>14</td><td>18</td><td>99</td></tr><tr><td>Success rate (%)</td><td>66.67</td><td>76.47</td><td>57.14</td><td>33.33</td><td>71.43</td><td>55.56</td><td>60.61</td></tr><tr><td rowspan="2">Replication 5</td><td>Number of tests</td><td>21</td><td>17</td><td>12</td><td>15</td><td>11</td><td>16</td><td>92</td></tr><tr><td>Success rate (%)</td><td>66.67</td><td>82.35</td><td>75.00</td><td>33.33</td><td>72.73</td><td>62.50</td><td>65.22</td></tr><tr><td colspan="9">Panel B: EFFM with  $BP^b$ </td></tr><tr><td rowspan="2">Replication 1</td><td>Number of tests</td><td>15</td><td>20</td><td>17</td><td>15</td><td>11</td><td>16</td><td>94</td></tr><tr><td>Success rate (%)</td><td>66.67</td><td>50.00</td><td>52.94</td><td>66.67</td><td>72.73</td><td>68.75</td><td>61.70</td></tr><tr><td rowspan="2">Replication 2</td><td>Number of tests</td><td>21</td><td>14</td><td>17</td><td>15</td><td>14</td><td>16</td><td>97</td></tr><tr><td>Success rate (%)</td><td>52.38</td><td>78.57</td><td>47.06</td><td>33.33</td><td>71.43</td><td>43.75</td><td>53.61</td></tr><tr><td rowspan="2">Replication 3</td><td>Number of tests</td><td>21</td><td>20</td><td>16</td><td>15</td><td>14</td><td>16</td><td>102</td></tr><tr><td>Success rate (%)</td><td>61.90</td><td>65.00</td><td>68.75</td><td>33.33</td><td>71.43</td><td>37.50</td><td>56.86</td></tr><tr><td rowspan="2">Replication 4</td><td>Number of tests</td><td>14</td><td>15</td><td>13</td><td>15</td><td>14</td><td>9</td><td>80</td></tr><tr><td>Success rate (%)</td><td>71.43</td><td>73.33</td><td>69.23</td><td>33.33</td><td>71.43</td><td>22.22</td><td>58.75</td></tr><tr><td rowspan="2">Replication 5</td><td>Number of tests</td><td>12</td><td>12</td><td>14</td><td>15</td><td>15</td><td>10</td><td>78</td></tr><tr><td>Success rate (%)</td><td>58.33</td><td>75.00</td><td>64.29</td><td>33.33</td><td>66.67</td><td>60.00</td><td>58.97</td></tr><tr><td colspan="9">Panel C: EFFM with PN</td></tr><tr><td rowspan="2">Replication 1</td><td>Number of tests</td><td>14</td><td>6</td><td>17</td><td>15</td><td>14</td><td>15</td><td>81</td></tr><tr><td>Success rate (%)</td><td>50.00</td><td>16.67</td><td>52.94</td><td>33.33</td><td>71.43</td><td>66.67</td><td>51.85</td></tr><tr><td rowspan="2">Replication 2</td><td>Number of tests</td><td>20</td><td>17</td><td>13</td><td>15</td><td>11</td><td>16</td><td>92</td></tr><tr><td>Success rate (%)</td><td>55.00</td><td>70.59</td><td>38.46</td><td>66.67</td><td>36.36</td><td>56.25</td><td>55.44</td></tr><tr><td rowspan="2">Replication 3</td><td>Number of tests</td><td>15</td><td>3</td><td>16</td><td>15</td><td>14</td><td>14</td><td>77</td></tr><tr><td>Success rate (%)</td><td>60.00</td><td>33.33</td><td>56.25</td><td>33.33</td><td>71.43</td><td>64.29</td><td>55.84</td></tr><tr><td rowspan="2">Replication 4</td><td>Number of tests</td><td>6</td><td>18</td><td>7</td><td>6</td><td>5</td><td>7</td><td>49</td></tr><tr><td>Success rate (%)</td><td>33.33</td><td>55.56</td><td>71.43</td><td>50.00</td><td>60.00</td><td>85.71</td><td>59.18</td></tr><tr><td rowspan="2">Replication 5</td><td>Number of tests</td><td>9</td><td>15</td><td>4</td><td>3</td><td>5</td><td>2</td><td>38</td></tr><tr><td>Success rate (%)</td><td>44.44</td><td>66.67</td><td>50.00</td><td>66.67</td><td>60.00</td><td>0.00</td><td>55.26</td></tr></table>

The last column presents the average success rates and total number of tests in each replication over the 6 years.  
<sup>a</sup> Based upon five replications, the maximal, minimal, and average numbers of hidden nodes used are 8, 2, and 3.33, respectively.

Table 9  
The $\mu _ { 1 }$ and $\mu _ { 2 }$ values of the various EFFM configurations

<table><tr><td></td><td>EFFM with RN</td><td>EFFM with BP</td><td>EFFM with PN</td></tr><tr><td> $\mu_1$  (%)</td><td>60.69</td><td>57.87</td><td>55.19</td></tr><tr><td> $\mu_2$ </td><td>98.2</td><td>90.2</td><td>67.4</td></tr></table>

The other consideration is based on the mean $( \mu _ { 3 } )$ Ž . and standard deviation Std. of annual success rates. $\mu _ { 3 }$ and Std. measure the variability of forecasting performances caused by different initial weights. An ANN model having higher $\mu _ { 3 }$ and lower Std. is desired. According to Table 10, from the perspective of $\mu _ { 3 }$ and Std., RN outperforms BP and PN.

A possible explanation for BP and PN’s poor performance is their associated drawbacks. PN’s poor performance is possibly due to PN’s inability to handle nonlinearly separable problems 9 . Although<sup>w</sup> <sup>x</sup> BP can handle nonlinearly separable problems, BP is usually trapped in a local minimal learning result. Since RN outperforms BP and PN, we adopt EFFM with RN.

Table 10  
The $\mu _ { 3 }$ and Std. values of the various EFFM configurations

<table><tr><td>Year</td><td>1988</td><td>1989</td><td>1990</td><td>1991</td><td>1992</td><td>1993</td></tr><tr><td colspan="7">EFFM with RN</td></tr><tr><td> $\mu_3$  (%)</td><td>66.67</td><td>73.63</td><td>59.15</td><td>33.33</td><td>71.64</td><td>56.82</td></tr><tr><td>Std. (%)</td><td>0.00</td><td>10.12</td><td>7.29</td><td>0.00</td><td>0.48</td><td>2.68</td></tr><tr><td colspan="7">EFFM with BP</td></tr><tr><td> $\mu_3$  (%)</td><td>61.44</td><td>66.67</td><td>59.74</td><td>40.00</td><td>70.59</td><td>47.76</td></tr><tr><td>Std. (%)</td><td>6.63</td><td>10.60</td><td>9.03</td><td>13.34</td><td>2.14</td><td>15.63</td></tr><tr><td colspan="7">EFFM with PN</td></tr><tr><td> $\mu_3$  (%)</td><td>51.56</td><td>57.63</td><td>52.63</td><td>46.30</td><td>61.22</td><td>62.96</td></tr><tr><td>Std. (%)</td><td>7.69</td><td>16.47</td><td>9.66</td><td>15.27</td><td>14.09</td><td>15.22</td></tr></table>

## 2.3. Integrated futures trading system

Based on FFM and EFFM, we develop the integrated futures trading system IFTS for trading S&PŽ . 500 stock index futures contracts. IFTS consists of two units: the periodical off-line training unit and the daily on-line prediction unit.

The periodical off-line training unit attempts to construct two subsystems corresponding to FFM and EFFM. From the time series of price data of the previous 4 years $( P _ { \mathrm { h } } )$ , the derived case information $( D _ { \mathrm { h } } )$ is calculated first. $D _ { \mathrm { h } }$ consists of the case observations. We use $D _ { \mathrm { h } }$ and the algorithms listed in Tables 3 and 4 to construct the subsystem $( S _ { \mathrm { F F M } } )$ corresponding to FFM. Then, using $S _ { \mathrm { F F M } }$ , we select the obvious cases from $D _ { \mathrm { h } }$ , which consist of the training examples for RNs $( T _ { \mathrm { h } } )$ . Then, we use $T _ { \mathrm { h } } .$ , the learning algorithm of RN, and the algorithm listed in Table 6 to construct the subsystem $( S _ { \mathrm { E F F M } } )$ corresponding to EFFM. Notably, $S _ { \mathrm { F F M } }$ and $S _ { \mathrm { E F F M } }$ are adopted in the daily on-line prediction unit.

The daily on-line prediction unit provides futures investors with trading recommendations. From the time series of the current price data $( P _ { \mathrm { c } } )$ , the daily on-line prediction unit calculates the derived case information $( D _ { \mathrm { c } } )$ for the current day. Then, $D _ { \mathrm { c } }$ is inputted into $S _ { \mathrm { F F M } }$ . Next, $S _ { \mathrm { F F M } }$ analyzes $D _ { \mathrm { c } }$ . If $D _ { \mathrm { c } }$ is the non-obvious case, $S _ { \mathrm { F F M } }$ triggers $S _ { \mathrm { E F F M } }$ . More specifically, $S _ { \mathrm { F F M } }$ handles the obvious cases, $S _ { \mathrm { E F F M } }$ handles the non-obvious cases, and the trading recommendation for the current day $( R _ { \mathrm { c } } )$ is generated by either $S _ { \mathrm { F F M } }$ or $S _ { \mathrm { E F F M } }$

## 3. The performance evaluation

We use the daily S&P 500 stock index futures price data from 1984 to 1993 for the evaluation. The simulation strategy is as follows: 4-year daily data, from 1984 to 1987, are used to construct an IFTS. This IFTS is then applied to forecast the price movements in 1988. We replicate this strategy throughout the period from 1989 to 1993. In other words, the testing period in the simulation is from 1988 to 1993. This period covers one bear market 1989–1990 andŽ . one bull market 1991–1993 . Therefore, we canŽ . investigate the performance of our IFTS under different market characteristics. Regardless of what trades are executed, they occur at a fixed time interval during the trading day. More specifically, IFTS enters the market just before the close of trading for that day, and unwinds its position before the close of trading for the next day. <sup>8</sup> IFTS, which does not use a stop-loss mechanism, always carries the futures position for one day 24 h .Ž .

Table 11  
The forecasting performances of FFM and EFFM in each testing year

<table><tr><td>Year</td><td>1988</td><td>1989</td><td>1990</td><td>1991</td><td>1992</td><td>1993</td></tr><tr><td colspan="7">FFM</td></tr><tr><td>Success rate (%)</td><td>57.69</td><td>58.67</td><td>56.38</td><td>59.38</td><td>58.95</td><td>58.76</td></tr><tr><td>Number of tests</td><td>78</td><td>75</td><td>94</td><td>96</td><td>95</td><td>97</td></tr><tr><td colspan="7">EFFM</td></tr><tr><td>Success rate (%)</td><td>66.67</td><td>76.47</td><td>56.25</td><td>33.33</td><td>71.43</td><td>55.56</td></tr><tr><td>Number of tests</td><td>15</td><td>17</td><td>16</td><td>15</td><td>14</td><td>18</td></tr><tr><td colspan="7">Both FFM and EFFM</td></tr><tr><td>Success rate (%)</td><td>59.14</td><td>61.96</td><td>56.36</td><td>55.86</td><td>60.55</td><td>58.26</td></tr></table>

Table 11 presents the above evaluation results. Notably, the success rate for each testing year exceeds 50% except for that of EFFM in 1991. Table 12 summarizes the results for the entire period. The binomial test is employed to test whether the success rate varies significantly from 50%. The binomial test proceeds as follows.

Let N and T be the total number of tests and the total number of successes in the simulation. Under the null hypothesis that the success rate is equal to 50%, the test statistic, T, has approximately a normal distribution with a mean, E TŽ .<sup>s</sup>N<sup>r</sup>2, and a variance, $\mathrm { V A R } ( T ) = N / 4$ if each test of the simulation is independent from each other. When N is large, T, when standardized, has approximately a unit normal distribution. The binomial test is based on the following Z-statistic:

Table 12  
The summary over 1988–1993 and their associated binomial tests

<table><tr><td></td><td>(a) Total number of tests</td><td>(b) Total number of successes</td><td>Success rate (%): b/a</td><td>Binomial  $test^a$  Z-value</td></tr><tr><td>FFM</td><td>535</td><td>312</td><td>58.32</td><td> $3.90^c$ </td></tr><tr><td>EFFM</td><td>95</td><td>57</td><td>60.00</td><td> $1.99^b$ </td></tr><tr><td>FFM and EFFM</td><td>630</td><td>369</td><td>58.57</td><td> $4.37^c$ </td></tr></table>

The binomial test is to test whether the success rate is significantly different from 50%.  
<sup>a</sup> The binomial test is based on Eq. 5 .Ž .  
<sup>b</sup>Significant at the 5% level.  
<sup>c</sup> Significant at the 1% level.

$$
Z = \frac {T - \frac {N}{2}}{\sqrt {\frac {N}{4}}}\tag{5}
$$

The binomial tests indicate that all of the success rates dramatically exceed 50%. The collaboration of FFM and EFFM is quite effective in accurately forecasting the direction of daily price change in the S&P 500 index futures market.

The trading performance of IFTS is also evaluated by simulating the purchasing and selling of the S&P 500 stock index futures contracts from 1988 to 1993. Fig. 1 depicts the holding period returns HPRs of Ž . IFTS and of the buy-and-hold B&H strategy. WithŽ . a round-trip transaction cost of \$60, <sup>10</sup> the holding period return is computed as follows:

holding period return

$$
= \prod_ {\text { all   transactions }} \frac {5 0 0 C _ {t + 1} - 6 0}{5 0 0 C _ {t}} - 1\tag{6}
$$

where $C _ { t }$ denotes the close on day t. At the end of 1993, IFTS had a holding period return of 94.96%, exceeding that of the buy-and-hold strategy, 56.89%.

![](/api/attachments/YW6HMMPJ/fulltext/images/9c35c773229df0e94b5b66147ebbd116d9a0cd3f62d11d6ed51b6cb2be163827.jpg)  
Fig. 1. The holding period returns with respect to IFTS and B&H for S&P 500 index futures trading from 1988 to 1993.

Table 13 displays the annual success rates and holding period returns for IFTS as well as for the buy-and-hold strategy. According to Panel A, by considering only the obvious cases, the trading performance of IFTS 56.09% is worse than that of theŽ .

buy-and-hold strategy 56.89% . However, as PanelŽ . C indicates, by considering both the obvious cases and the non-obvious cases, the trading performance of IFTS 94.96% is better than that of the buy-and-Ž . hold strategy 56.89% . Based on the trading simula-Ž .

Table 13  
The yearly success rates and holding period returns with respect to IFTS and buy-and-hold strategies

<table><tr><td>Year</td><td>1988</td><td>1989</td><td>1990</td><td>1991</td><td>1992</td><td>1993</td><td>1988–1993</td></tr><tr><td colspan="8">Panel A: Using IFTS to handle the obvious cases</td></tr><tr><td>Success rate</td><td>57.69%</td><td>58.67%</td><td>56.38%</td><td>59.38%</td><td>58.95%</td><td>58.76%</td><td>58.32%</td></tr><tr><td>HPR</td><td>11.42%</td><td>11.96%</td><td>7.27%</td><td>4.67%</td><td>3.89%</td><td>7.27%</td><td>56.09%</td></tr><tr><td colspan="8">Panel B: Using IFTS to handle the non-obvious cases</td></tr><tr><td>Success rate</td><td>66.67%</td><td>76.47%</td><td>56.25%</td><td>33.33%</td><td>71.43%</td><td>55.56%</td><td>60.00%</td></tr><tr><td>HPR</td><td>7.41%</td><td>6.08%</td><td>3.70%</td><td>0.52%</td><td>3.08%</td><td>2.02%</td><td>24.90%</td></tr><tr><td colspan="8">Panel C: Using IFTS to handle both the obvious cases and non-obvious cases</td></tr><tr><td>Success rate</td><td>59.14%</td><td>61.96%</td><td>56.36%</td><td>55.86%</td><td>60.55%</td><td>58.26%</td><td>58.57%</td></tr><tr><td>HPR</td><td>19.67%</td><td>18.77%</td><td>11.24%</td><td>5.22%</td><td>7.09%</td><td>9.44%</td><td>94.96%</td></tr><tr><td colspan="8">Panel D: the buy-and-hold strategy</td></tr><tr><td>HPR</td><td>11.55%</td><td>17.49%</td><td>-7.96%</td><td>12.02%</td><td>11.49%</td><td>4.78%</td><td>56.89%</td></tr></table>

The last column presents the average success rates and total holding period returns from 1988 to 1993.

![](/api/attachments/YW6HMMPJ/fulltext/images/f49b15d28630f9dce74afe4bbdf55c4217d5a1adb94cf5b6c72a8526f29efca2.jpg)  
Fig. 2. Function surface on the weight space.

tion results, IFTS outperforms the passive buy-andhold strategy in the S&P 500 stock index futures market.

## 4. Conclusions and future work

This paper presents a hybrid AI approach to implement trading strategies in the S&P 500 stock index futures market. Based on the results presented, the following suggestions can be offered.

Ž . 1 Predict and trade in the futures market by adopting the hybrid AI approach which integrates both the rule-based systems technique and neural networks technology.

Ž . 2 Process the futures price data to derive the case information for prediction. Among the variables of the case information, some are trigger variables and others are status variables. Trigger variables determine the timing of when to provide the trading suggestion; meanwhile, status variables capture the information of the current futures market. For each trading day, we derive case information, which is either an observation in the past or an occurrenceŽ . Ž . at the present of a certain case.

Ž . 3 Propose FFM to analyze previous case observations, which offer information about the frequencies of being an up day and a down day for allŽ . cases observed previously. The observed frequencies are primarily to classify the observed cases into two groups: the obvious cases and the non-obvious cases.

The obvious cases are those having higher frequencies of being an up day or a down day in the past; the others are the non-obvious cases. FFM handles the obvious cases based on the proposition of their consistency <sup>11</sup> in the future.

Ž . 4 Propose EFFM to handle the non-obvious cases. The main components in EFFM are the four ANNs, which are trained by using the previous obvious cases picked out via in FFM. EFFM’s success is based on two propositions: 1 the informa- Ž . tion contained in the past obvious cases is sufficient and 2 the generalization ability of ANN is ade-Ž . quate.

Ž . 5 EFFM with RN outperforms BP and PN. A possible explanation for the poor generalization of both BP and PN is their associated drawbacks. The poor performance of the PN model is possibly due to PN’s inability to handle the nonlinearly separable problems. Although BP can handle the nonlinearly separable problems, BP is generally trapped at a relatively minimal result during the learning stage.

Our research can be extended in the following directions. First, we can compare the prediction performance of our forecast models with other forecast techniques. Second, the same methodology can be applied to examine either long term forecasts or financial markets.

## Acknowledgements

The authors would like to thank the National Science Council of R.O.C. for supporting this work under grant No. NSC 85-2418-H-004-008. Thanks are also due to the editors and two anonymous reviewers for useful comments on an earlier draft of this paper. Several of the references might not be widely available these include Refs. 19,20,5,13 ,Ž <sup>w</sup> <sup>x</sup>. but the authors would provide copies of these papers upon request.

## Appendix A. Limitations of back propagation

During the learning stage, to minimize the value of the objective function, the back propagation learning algorithm adopts an optimization technique typi-Ž cally the steepest descent method to adjust the . connection weights. Ideally, a global minimum is desirable. For a more complicated learning task as Fig. 2 depicts, however, the function surface on the weight space usually has numerous local minimums. Thus, it is unavoidable that the learning might be trapped at a local minimum when adopting the steepest descent method.

The optimal network architecture is critical for developing good generalization ability. However, the back propagation learning algorithm cannot determine the optimal hidden layer size by itself. The hidden layer size must be given before the learning starts. The fact that the optimal network architecture is unknown accounts for why the decision can be made only by trial and error.

## References

<sup>w</sup> <sup>x</sup> 1 K. Bergerson, D.C. Wunsch, A commodity trading model based on a neural network—Expert system hybrid, Proceedings of the IEEE International Conference on Neural Networks, 1991, pp. I289–I293.

<sup>w</sup> <sup>x</sup> 2 S.C. Blank, Chaos in futures market? a nonlinear dynamical analysis, J. Futures Markets 11 1991 711–728.Ž .

<sup>w</sup> <sup>x</sup> 3 W.E. Bosarge, Adaptive processes to exploit the nonlinear structure of financial markets, The Santa Fe Institute of

Complexity Conference: Neural Networks and Pattern Recognition in Forecasting Financial Markets, Feb. 1991.

<sup>w</sup> <sup>x</sup> 4 T.S. Chande, S. Kroll, The New Technical Trader, Wiley, New York, 1994.

<sup>w</sup> <sup>x</sup> 5 Y. Chiou, S. Liu, R. Tsaih, Applying reasoning neural networks to the analysis and forecast of Taiwan’s stock index variation, Taipei Econ. Inquiry, Taipei 34 2 1996 171–Ž . Ž . 200.

<sup>w</sup> <sup>x</sup> 6 G.P. DeCoster, W.C. Labys, D.W. Mitchell, Evidence of chaos in commodity futures prices, J. Futures Markets 12 Ž .1992 291–305.

<sup>w</sup> <sup>x</sup> 7 M. Frank, T. Stengos, Measuring the strangeness of gold and silver rates of return, Rev. Econ. Studies 56 1989 553–567.Ž .

<sup>w</sup> <sup>x</sup> 8 G. Grudnitski, L. Osburn, Forecasting S&P and gold futures prices: an application of neural networks, J. Futures Markets 13 6 1993 631–643.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 J. Hertz, A. Krogh, R. Palmer, Introduction to the Theory of Neural Computation, Addison-Wesley, Reading, MA, 1991.

<sup>w</sup> <sup>x</sup> 10 J.M. Hutchinson, A.W. Lo, T. Poggio, A nonparametric approach to pricing and hedging derivative securities via learning networks, J. Finance 49 3 1994 851–889.Ž . Ž .

<sup>w</sup> <sup>x</sup>11 W.Y. Kee, A. Koh, Technical analysis of Nikkei 225 stock index futures using an expert system advisor, Proceedings of the CBOT Conference, 1994.

<sup>w</sup> <sup>x</sup> 12 C. Lai, Forecasting Foreign Stock Index Futures: An Application of Neural Networks, Department of Management Information Systems, National Chengchi Univ., Taipei, Master Thesis, 1996.

<sup>w</sup> <sup>x</sup> 13 H.W. Lin, R. Tsaih, R. Jee, Exploring the relative abilities of neural networks and VAR models in forecasting Taiwan bond prices, Rev. Securities Futures Markets, Taipei 9 1Ž . Ž . 1997 63–113.

<sup>w</sup> <sup>x</sup> 14 F. Rosenblatt, The perceptron: a probabilistic model for information storage and organization in the brain, Psychol. Rev. 65 1958 386–408.Ž .

<sup>w</sup> <sup>x</sup> 15 D.E. Rumelhart, G.E. Hinton, R.J. Williams, Learning internal representations by error propagation, Parallel Distributed Processing, Vol. 1, MIT Press, Cambridge, MA, 1986, pp. 318–362.

16 R. Trippi, D. DeSieno, Trading equity index futures with a neural network, J. Portfolio Manage. Fall, 1992 27–33.Ž .

<sup>w</sup> <sup>x</sup> 17 R. Trippi, E. Turban, Neural Networks in Finance and Investing, Probus Publishing, Chicago, 1993.

<sup>w</sup> <sup>x</sup> 18 R. Tsaih, The softening learning procedure, Math. Comput. Modelling 18 1993 61–64.Ž .

<sup>w</sup> <sup>x</sup> 19 R. Tsaih, The softening learning procedure for the networks with multiple output nodes, MIS Rev. 4 1994 89–93.Ž .

<sup>w</sup> <sup>x</sup> 20 R. Tsaih, Learning procedure that guarantees obtaining the desired solution of the 2-classes categorization learning problem, The 1st Asia-Pacific Conference on Simulated Evolution and Learning, Korea, 1996, pp. 446–453.

<sup>w</sup> <sup>x</sup> 21 R. Tsaih, Reasoning neural networks, in: S. Ellacott, J. Mason, I. Anderson Eds. , Mathematics of Neural Net-Ž . works: Models, Algorithms and Applications, Kluwer Academic Publishers, London, 1997, pp. 366–371.

<sup>w</sup> <sup>x</sup> 22 R. Tsaih, An explanation of reasoning neural networks, Math. Comput. Modelling, 1997, accepted.

<sup>w</sup> <sup>x</sup> 23 Y. Yoon, T. Guimaraes, G. Swale, Integration artificial neural networks with rule-based expert system, Decision Support Syst. 11 1994 497–507.Ž .

![](/api/attachments/YW6HMMPJ/fulltext/images/d9e7f1af1e070fdfc3af596c3e7d65bc5d8687bae2832e2de49510f72f9c25f6.jpg)

Ray Tsaih, also known as Rua-Huan Tsaih, is an associate professor at National Chengchi University, Taipei, Taiwan. He received his B.S. from Nationa Tsinghua University Taipai, and received his M.S. and Ph.D. in Operations Research in 1991 from University of California, Berkeley. His research interests are Developing new neural networks, applying Neural Networks to Finance, and Interior-point algorithm. His most recent work has been published in

Mathematical and Computer Modelling, Review of Securities and Futures Markets, MIS REVIEW, Taipei Economic Inquiry, and Sun Yat-sen Management Review.

![](/api/attachments/YW6HMMPJ/fulltext/images/314e9e54e8b5e831629b52aaa8915be96b4593c87dbb5d16249656b27f08ca1a.jpg)

Yenshan Hsu is a Professor of Finance at National Chengchi University, Taipei, Taiwan, where he taught courses in investment theory and portfolio management. He received a Ph.D. in Finance from the University of Iowa. His research ares include investment finance, stock market regulations, portfolio management, and the applications of artificial neural networks in finance. His most recent work has been published in Journal of Financial Studies and Pacific-

Basin Finance Journal.Charles Lai received a M.S. in Management Information Systems from National Chengchi University, Taipei in 1996.

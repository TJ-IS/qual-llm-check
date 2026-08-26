---
otero_id: 28063
otero_key: "DPAFDGXW"
title: "The Attention Economy: Measuring the Value of Free Goods on the Internet"
authors: "Erik Brynjolfsson; Seon Tae Kim; Joo Hee Oh"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.0153"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Attention Economy: Measuring the Value of Free Goods on the Internet

Erik Brynjolfsson,<sup>a,</sup>\* Seon Tae Kim,<sup>b</sup> Joo Hee Oh<sup>b,</sup>\*

<sup>a</sup> Stanford Institute for Human-Centered AI at Stanford University, Stanford Digital Economy Laboratory, Stanford Graduate School of Business, Stanford Department of Economics, National Bureau of Economic Research, Stanford, California 94305; <sup>b</sup> School of Management and Economics, Handong Global University, Pohang, Gyeongbuk 37554, Republic of Korea

Contact: erik.brynjolfsson@gmail.com, https://orcid.org/0000-0002-8031-6990 (EB); santaf78@gmail.com,

Received: June 25, 2021 Revised: April 1, 2023 Accepted: May 15, 2023 Published Online in Articles in Advance: August 31, 2023

https://doi.org/10.1287/isre.2021.0153

Copyright: © 2023 INFORMS

Abstract. We develop a framework to measure the value of free goods and services available on the internet. The conventional method of measuring consumer surplus based on monetary expenditures is ineffective because these goods’ prices are predominantly zero. Our proposed method addresses this challenge by quantifying the economic value of the time that consumers devote to consuming these free goods. Using data on consumers’ time and monetary expenditures, we calibrate an economic model of the allocation of individuals’ time among internet, television, leisure, and work. We measure the consumer surplus of free goods on the internet as the reduction in gross domestic product (GDP) required to create an equivalent welfare loss to that which would occur if these free goods were no longer available. We find that the average incremental welfare gain from the internet between 2002 and 2011 was about \$38 billion per year in the United States, equivalent to approximately 0.29% of the annual GDP. In contrast, if we had not considered the value of time, then the estimated annual incremental welfare gain would have been significantly smaller at about \$2.7 billion, only 7% of the estimate derived from our proposed time based model. Our approach can be readily extended to the valuation of other zero-priced goods and services, such as television. In addition, our results show the importance of not only quantity but also quality (e.g., internet speed) in determining the welfare contributions of free goods.

History: Eric Zheng, Senior Editor; Yan Huang, Associate Editor. Funding: This work was supported by the Stanford Digital Economy Laboratory. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.0153.

Keywords: attention • internet • free goods • welfare gain • value of time • opportunity cost • television

## 1. Introduction

Consumers have finite money and finite time to spend on consumption. Any expenditure on a good, whether in terms of money, time, or both, has an opportunity cost. In this paper, we implement and calibrate a framework that measures the value of free goods (i.e., goods with zero monetary cost) by explicitly considering their nonmonetary opportunity cost: the time that people devote to consuming them. After all, even when consumers don’t have to pay with dollars, they still have to “pay attention” in order to consume free goods. Using this approach, we can calculate the implied demand curve for free goods. We estimate the increase in consumer surplus created by free internet goods was more than \$25 billion per year in the United States between 2002 and 2011. This reflects that fact that household time spent on digital media almost doubled.

As noted by Brynjolfsson et al. (2019) and others, the welfare contributions of the digital economy are likely to be underrepresented when measured with traditional metrics, such as gross domestic product (GDP) and its derivatives. These metrics are largely based on the amount of money spent on goods and services, not the time spent. The price of new digital goods or services is often zero, but individuals nonetheless get significant value from free goods.

The traditional approach for measuring economic growth is based on calculating changes in money expenditures by consumers on goods and services and thereby estimating the demand curve implied by the direct monetary price and quantity of goods and services. However, people who already have access to the internet do not spend any additional money to consume these free goods because most consumers purchase internet services at a fixed monthly price. Thus, the direct application of demand analysis is problematic (Goolsbee and Klenow 2006, Brynjolfsson and Oh 2012).

Furthermore, indirect measures, such as advertising expenditures, are not representative of the value of free media to consumers, and many types of free media do not adopt any advertising at all. Advertising is an intermediate good and, thus, does not directly contribute to GDP.<sup>2</sup> In addition, Spence and Owen (1977) show that the revenues advertisers derive from free media are not sensitive to the level of consumers willingness to pay for the content and, thus, are a poor measure of welfare. As a result, traditional measures of economic growth largely overlook the impact of free goods, and so do the productivity statistics calculated based on such measures.

An alternative approach is to estimate the value of specific free sites using online surveys or experiments to obtain estimates of consumers’ preferences (Allcott et al. 2019; Brynjolfsson and Collis 2019; Brynjolfsson et al. 2019, 2020). However, surveys and online experiments are vulnerable to biases inherent in hypothetical choices and can be difficult to implement or scale up when they are made consequential (Diamond and Hausman 1994, Zheng et al. 2014).

In contrast to these approaches, in this study, we build on the insights of Goolsbee and Klenow (2006) (G&K) in measuring the time and money value of leisure to estimate the value of the internet.<sup>3</sup> We infer consumer preferences from the data on their behaviors about how they spend time and money. That is, our data provide observations about users’ decisions/ behaviors rather than their willingness to pay. Specifically, we develop and apply an indirect application of demand analysis to measure the value of free goods for consumers. We then estimate the consumer surplus created by free goods by considering the nonmonetary opportunity cost of consuming such goods. Consumers spend something very valuable to consume such goods: time and attention. In this study, we develop a model of the household time spent on the internet to quantify the value of recently introduced digital innovations that provide services, content, entertainment, or knowledge for free. Specifically, every waking hour spent on the internet necessarily comes at the opportunity cost of time spent consuming other goods and services or working. We use this fact to infer the value of free internet goods.

In our model, we use the opportunity cost of a service—the amount of time a person freely gives up to consume the service—to estimate its value. For goods that are free or have very low prices, this gives a much better empirical estimate of their value than efforts to infer value from the money prices.<sup>4</sup> We calculate the welfare gain as a benchmark by using two approaches: a time- and a money-based model.

Our analysis makes four key contributions. First, we extend the work of G&K to create a tractable framework to measure the economy-wide welfare gain from free internet goods. This approach extends the traditional household utility maximization analysis by taking into account the value of time spent on the internet. In the model, the internet hours spent by the household are an equilibrium outcome determined by the revealed preference of the household that values internet services despite the time cost. Our model captures the important fact that there is a trade-off (in terms of attention) bet ween the internet and other media.

Second, we quantify the model-predicted welfare gain from free internet goods by using a calibration methodology that is general enough to be applied to broadly value a variety of goods and services. In our model, we combine both internet and television services, which are partial substitutes, as well as other goods and services that are poor substitutes to calculate the distinct welfare gain from the internet and television. We consider the case in which the elasticity of substitution between internet hours and television hours is higher than that between internet hours and other leisure activities. A key implication of these partial substitutes is that growth in the share of internet hours increases the marginal utility of all other leisure activities but not so much the marginal utility of television.

Third, our model incorporates overall internet speed improvement as improvement in the quality of the internet to estimate the induced changes in the annual consumer welfare. With this longitudinal approach, we can quantify the annual increase in welfare gain over time in a consistent manner focusing on change over time unlike earlier purely cross-sectional models (e.g., G&K). Without quality improvement of the internet, the simulated aggregate internet hours would not increase as they actually do in the data. Incorporating the observed quality improvement is important for two reasons. In the actual data, time spent on the internet has increased over time, which is consistent with improved quality. In contrast, suppose that there had been no improvement in the internet quality. A model with no quality dimension would predict that the U.S. aggregate time spent on the internet should, in equilibrium, decrease over time as the U.S. average real wage rate (i.e., opportunity cost of the internet hours) has been increasing over time.

Fourth, we avoid the overestimation problem created by employing the log-linear utility function that is typically used.<sup>5</sup> Whereas there are many advantages of log-linear utility, it assumes that the very first increment of internet use has an infinitely high value, which is unrealistic.<sup>6</sup> To overcome this problem, we incorporate the approach introduced by Greenwood and Kopecky (2013) into our model. Additionally, we focus on measuring the incremental change in welfare from one year to the next instead of the total welfare created by the internet or other goods. This cancels out the effects of any extreme initial values.

Our key findings are as follows: the average incremental welfare gain from the internet between 2002 and 2011 is about \$38 billion per year in the United States. Of this, about \$25 billion accounts for the consumer surplus from free digital goods on the internet and about \$13 billion comes from paid goods. In contrast, the welfare values implied by the traditional approach, relying only on money-based expenditures are an order of magnitude lower. To be precise, if we did not consider the value of time, then the estimated annual incremental welfare gain would be about \$2.7 billion. That corresponds to just 7% of the estimate derived from our preferred time-based model.

Our welfare estimates can be compared with other estimates of the internet’s potential value. As noted, Goolsbee and Klenow (2006) first used the time value of leisure to estimate the opportunity cost and value of internet use. Brynjolfsson et al. (2019) estimate the value of a variety of free goods via online choice experiments, for instance, finding that the median user would need to be paid almost \$50 to stop using Facebook for one month. Nakamura et al. (2016) estimate that the productivity impact of free apps increased by 1% per year in the internet media sector. Varian (2006) presents an annual value of \$120 billion for Google’s search engine based on the value of time savings to average users. Corrado et al. (2009) conclude that investment spending has increasingly shifted toward intangibles. Byrne et al. (2016) find that consumers are more productive when using their nonmarket time to produce services they value, such as Google searches and Facebook. Our finding is also consistent with the prediction that the welfare gain from time savings for households with higher internet usage level will increase as more content and applications become available (Nevo et al. 2016).<sup>7</sup>

## 2. Theoretical Framework: Measuring Welfare Gain from the Internet

Consumers in the United States spend their waking hours on a variety of activities. Specifically, consumers can be described as obtaining utility from three types of bundles: an internet bundle, a television bundle, and a composite goods bundle of all other goods. The internet and television bundles are highly time-intensive goods; individuals spend a significant amount of time without spending additional money on the margin (other than monthly subscription fee). Meanwhile, a composite goods bundle is less time-intensive; people obtain utility from spending both money and leisure time. In addition to deciding how to allocate their leisure, consumers must decide how many hours to devote to paid work, which necessarily comes at the expense of the hours they could otherwise be spent on leisure. Thus, available time and the wage rate are the constraints that people face.

The key assumptions used in our analysis, explained in more details later, are as follows.

Assumption 1. In determining consumption of free goods on the internet, the user’s time is the key variable spending, whereas the monetary cost is fixed (in our baseline model).

Assumption 2. The per-hour consumption of free goods on the internet is increasing in the quality of the internet.

Assumption 3. The quality of the internet may change over time, whereas the quality of TV is constant.

Assumption 4. TV hours are more substitutable for internet hours than other leisure activities are.

Assumption 5. People consume free goods on the internet via a broadband internet connection but not via a mobil internet connection.

Assumption 6. The leisure-purpose household time spend ing on the internet is used for consumption, but not for pro duction, of free goods on the internet.

Assumption 7. Individuals rationally decide their time spending on internet and other activities.

A detailed discussion on the implications of alternative assumptions and potential model extensions is presented in Section 2.3.

## 2.1. General Case: Money- and Time-Based Consumption

Our model assumes that consumers can be described as deriving utility from three bundles of goods: internet, tele vision, and all other goods. We use the following underly ing Cobb–Douglas utility functions for our analysis.

The utility function for the consumption of internet goods $H _ { 1 } ( \cdot )$ can be defined as ${ \cal H } _ { 1 } ( \bar { I _ { 1 } } , T _ { 1 } ) = I _ { 1 } ^ { \alpha _ { 1 } } ( T _ { 1 } +$ $\kappa _ { 1 } ) ^ { 1 - \alpha _ { 1 } }$ , where $I _ { 1 }$ denotes money-based service flow of internet at home, $T _ { 1 }$ refers to time-based service flow of internet at home, and $\kappa _ { 1 } > 0$ is a small adjustment in the spirit of Greenwood and Kopecky (2013) to eliminate the possibility that the marginal utility at zero consumption explodes to infinity. The moneybased service flow of internet $I _ { 1 }$ is intended to represent the market-purchased goods/services and the time-based service flow of internet $T _ { 1 }$ the home-produced service component; the market-purchased goods/services $I _ { 1 }$ and the home-produced service $T _ { 1 }$ are combined together and consumed by the household (Diewert et al. 2018).

Similarly, the utility function for the consumption of television can be defined as $H _ { 2 } ( I _ { 2 } , T _ { 2 } ) = I _ { 2 } ^ { \alpha _ { 2 } } ( T _ { 2 } +$ $\kappa _ { 2 } ) ^ { 1 - \alpha _ { 2 } }$ , where $I _ { 2 }$ denotes money-based service flow of television at home and $T _ { 2 }$ represents time-based service flow of television at home. The utility function for general goods is given by $H _ { 3 } ( C , L ) = C ^ { \alpha _ { 0 } } L ^ { 1 - \alpha _ { 0 } }$ , where all other purchased goods and services are represented by composite good consumption C, which requires leisure L (i.e., time spent on composite good consumption).

Key variables related to the general case of the three bundles of goods are listed in Table A.2 in the appendix.

Assuming a nested constant elasticity of substitution (CES) function<sup>8</sup> for the aggregate of all three bundles yields

$$
\begin{array}{l} U (T _ {1}, T _ {2}, C, L; I _ {1}, I _ {2}) \\ = \left\{\theta_ {0} \Phi (I _ {1}, T _ {1}, I _ {2}, T _ {2}) ^ {1 - \frac {1}{\sigma_ {0}}} + (1 - \theta_ {0}) H _ {3} (C, L) ^ {1 - \frac {1}{\sigma_ {0}}} \right\} ^ {\frac {\sigma_ {0}}{\sigma_ {0} - 1}}, \end{array}\tag{1}
$$

where

$$
\Phi = \left[ \theta_ {1} H _ {1} (I _ {1}, T _ {1}) ^ {1 - \frac {1}{\sigma_ {1}}} + (1 - \theta_ {1}) H _ {2} (I _ {2}, T _ {2}) ^ {1 - \frac {1}{\sigma_ {1}}} \right] ^ {\frac {\sigma_ {1} - 1}{\sigma_ {1}}}.
$$

Let Q denote the quality of the internet (e.g., speed of the internet connection and amount of high-quality content available on the internet); Q increases the level of service flow from the internet for a given time $h _ { 1 }$ spent on the internet at home. That ${ \mathrm { i } } { \mathrm { s } } ,$ time-based service flow of internet at home $T _ { 1 }$ is written as $T _ { 1 } = h _ { 1 } \times Q ,$ , where $h _ { 1 }$ refers to the physical amount of time spent on consumption of free goods on the internet. Q represents the quality of the internet that increases the efficiency of $h _ { 1 }$ in terms of per-hour production of time-based service flow of internet at home. If Q increases by $1 0 \% ,$ , then the time-based service flow of internet at home $T _ { 1 }$ also increases by 10% given the same amount of time spent on the internet. Meanwhile, the quality of television is assumed constant and normalized to one; as such, television consumption $T _ { 2 }$ is written as $T _ { 2 } = h _ { 2 }$ , where $h _ { 2 }$ refers to the physical amount of time spent on television. Given that the total amount of time available in every period is equal to one, $h _ { 1 }$ and $h _ { 2 }$ refer to, respectively, the fraction of total time devoted to the internet and television at home.

Each $\alpha _ { 1 } , \alpha _ { 2 } ,$ , and $\alpha _ { 0 }$ corresponds to the degree of money intensity of the internet, television, and composite goods. The time intensities of internet, television, and composite goods are represented by $( 1 - \alpha _ { 1 } ) , ( 1 - \alpha _ { 2 } )$ and $( 1 - \alpha _ { 0 } ) .$ , respectively.<sup>9</sup> The elasticity of substitution between internet and television usage is represented by the parameter $\sigma _ { 1 } ,$ whereas the elasticity of substitution between internet and all other goods’ consumption is captured by the parameter $\sigma _ { 0 } .$ . If television is a closer substitute for internet than all other goods are, then we will observe $\sigma _ { 1 } > \sigma _ { 0 }$

## 2.2. Baseline Model: Time-Based Consumption

Note that, when the money intensity parameters of internet and television goods, $\alpha _ { 1 }$ and $\alpha _ { 2 }$ , are equal to zero, the utility function (1) is greatly simplified. In the case of internet and television, for which users pay fixed monthly fees, the money intensity parameters $\alpha _ { 1 }$ and $\alpha _ { 2 }$ are nearly zero.<sup>10</sup> That is, to increase the level of consumption of free goods on the internet, users must increase their time expenditure, but not the amount of money they spend.

2.2.1. Environment. We present our time-based model by setting the money intensity parameters $\alpha _ { 1 }$ and $\alpha _ { 2 }$ to zero as follows: Consider a representative household that receives utility from its consumption of leisure, internet, television, and other goods. The household maximizes its utility function $u ( C , T _ { 1 } , T _ { 2 } , L )$

$$
\begin{array}{c} \underset {C, T _ {1}, T _ {2}, L} {\text {Max}} \left\{u (C, T _ {1}, T _ {2}, L) \right\}, \\ u (C, T _ {1}, T _ {2}, L) = \\ \left\{ \begin{array}{l} \theta_ {0} \Big [ \theta_ {1} (T _ {1} + \kappa_ {1}) ^ {1 - \frac {1}{\sigma_ {1}}} + (1 - \theta_ {1}) (T _ {2} + \kappa_ {2}) ^ {1 - \frac {1}{\sigma_ {1}}} \Big ] ^ {\left(\frac {\sigma_ {1}}{\sigma_ {1} - 1}\right) \cdot \left(1 - \frac {1}{\sigma_ {0}}\right)} \\ + (1 - \theta_ {0}) [ C ^ {\alpha_ {0}} \cdot L ^ {1 - \alpha_ {0}} ] ^ {\left(1 - \frac {1}{\sigma_ {0}}\right)} \end{array} \right\} ^ {\frac {\sigma_ {0}}{\sigma_ {0} - 1}}. \end{array}
$$

subject to the (per-period) budget constraint

$$
P \cdot C + F = W (1 - h _ {1} - h _ {2} - L)\tag{2}
$$

and the nonnegativity conditions $T _ { 1 } , T _ { 2 } , C , L \geq 0$ . In the budget constraint, the wage rate W is the opportunity cost of time spent on the internet, and the time spent on the internet $h _ { 1 }$ is combined with the quality of the internet $Q$ to produce the time-based service flow of internet $T _ { 1 }$ as $T _ { 1 } = Q h _ { 1 }$ . Similarly, the time spent on television $h _ { 2 }$ is combined with the constant (normalized to one) quality to produce the time-based service flow of television $T _ { 2 }$ as $T _ { 2 } = h _ { 2 }$ . Note that $1 / Q$ can be interpreted as the marginal cost—the implicit price of the time spent on the internet: the better quality of the internet effectively reduces the physical amount of time needed to produce one unit of time-based service flow of the internet. $P$ is the price of the composite good, and F is any fixed fee for subscribing to the internet in a given period. Welfare is determined by the equilibrium allocation, which is determined by relative prices, $F / P , W / P ,$ and $( W / P ) / Q$ . Thus, without loss of generality, we can take the composite good as numeraire and normalize its price P to one.

We consider the standard competitive equilibrium. More specifically, the representative household (i) takes prices $\bar { F } , W , \bar { P } = \bar { 1 }$ , and internet quality Q as given and (ii) chooses time spending $( h _ { 1 } , h _ { 2 } , L )$ to maximize the house hold own utility function subject to the budget constraint.

2.2.1.1. Discussion. By introducing the parameters κ and $\kappa _ { 2 }$ in specifying the utility function, we avoid the problem of the marginal utility around zero consumption of the internet and television exploding to infinity in a log-linear utility function (Greenwood and Kopecky 2013). Instead, $\kappa _ { 1 }$ and $\kappa _ { 2 }$ shift each marginal utility curve slightly to the left $\mathbf { S O }$ that they intersect the y-axis at a finite level. An additional feature of this approach is that, because the marginal utility of zero internet time is bounded above, the solution to the individual’s maximization problem could be at a corner at which either $h _ { 1 } = T _ { 1 } / \hat { Q } = 0$ (i.e., zero consumption of internet) or $h _ { 2 } = T _ { 2 } = 0 \ \mathrm { ( i . e . }$ , zero consumption of television) or both. The solution to this problem determines the demand functions for the time share of internet, television, and composite good consumption.

2.2.2. Equilibrium: Time-Based Consumption and Welfare. We now discuss how to measure welfare gain to consumers from free goods and services on the internet. Using the optimality condition of the interior solution, we obtain the following Equation (3).

$$
\begin{array}{l} \frac {1 + \kappa_ {2} - \frac {F}{W} - T _ {1} ^ {*} - \left[ \frac {1 - \theta_ {1}}{\theta_ {1}} \right] ^ {\sigma_ {1}} \cdot (T _ {1} ^ {*} + \kappa_ {1})}{T _ {1} ^ {*} + \kappa_ {1}} \\ = \left[ \theta_ {1} + (1 - \theta_ {1}) \left(\frac {1 - \theta_ {1}}{\theta_ {1}}\right) ^ {\sigma_ {1} - 1} \right] ^ {\frac {\sigma_ {1} - \sigma_ {0}}{\sigma_ {1} - 1}} \cdot (1 - \alpha_ {0}) ^ {\sigma_ {0} - 1} \\ \left[ \frac {1 - \theta_ {0}}{\theta_ {1} \theta_ {0}} \right] ^ {\sigma_ {0}} \left[ \frac {\alpha_ {0}}{1 - \alpha_ {0}} \frac {W}{P} \right] ^ {\alpha_ {0} (\sigma_ {0} - 1)}, \end{array}\tag{3}
$$

where $T _ { 1 } ^ { * }$ refers to the equilibrium time-based service flow of internet in the case of an interior solution and $h _ { 1 } ^ { * } = T _ { 1 } ^ { * } / Q$ refers to the equilibrium time spent on the internet in this case.

One way of measuring welfare gain is based on the equivalent variation: the amount of money in real terms that one would have to give to consumers so that their welfare level without the internet is equivalent to the welfare they obtained with the internet. Suppose that the internet had never been invented. This is equivalent to assuming that the price of internet access is prohibitively high or its quality is extremely low so that people spend zero hours on the internet.

Specifically, consider a counterfactual shock to the quality of the internet such that, after the shock, the quality reduces to zero. Let $\hat { T } _ { 2 } = T _ { 2 } ( P , Q = 0 , W , F )$ denote the model-predicted time-based service flow of television when the household is hit by such a counterfactual shock so that zero hours are spent on the internet: $\hat { h } _ { 1 } = 0 ,$ $\hat { T } _ { 1 } = 0$ . For such a corner solution, $\hat { C } = C ( P , Q = 0 , W , F )$ $\begin{array} { r } { \mathbf { \Omega } = \left( \frac { \alpha _ { 0 } } { 1 - \alpha _ { 0 } } \cdot \frac { W } { P } \right) \cdot \hat { L } } \end{array}$ and $\hat { L } = L ( P , Q = 0 , W , F ) = ( 1 - \alpha _ { 0 } ) \Big [ 1 -$ $\begin{array} { r } { \hat { T } _ { 2 } - \frac { F } { W } \bigg ] } \end{array}$ refer to the composite good consumption and leisure, respectively. Note that these hatted variables, derived from the equilibrium decision rules, describe the household behavior in cases in which the internet quality is zero; however, other prices $( \mathrm { i . e . , }$ the real wage rate W and fixed fee for subscribing to the internet F) remain the same as before the shock. For comparison, let $T _ { 1 } ^ { * } = T _ { 1 }$ $( P , Q , W , F ) , \ h _ { 1 } ^ { * } = T _ { 1 } ( P , Q , W , F ) / Q , \ \hat { T } _ { 2 } ^ { * } = T _ { 2 } ( P , Q , \dot { W } , F ) .$ $h _ { 2 } ^ { \ast } = T _ { 2 } ( P , Q , \dot { W } , F ) , C ^ { \ast } = C ( P , Q , W , F ) .$ , and $L ^ { * } = L ( P , Q $

$W , F )$ denote the equilibrium outcome before the shock, which is an interior solution.

We compare the household utility between the two outcomes, corresponding to before and after the shock. Let $\delta _ { E V }$ denote the compensation in terms of the fraction of consumption<sup>11</sup> needed to maintain the level of utility after the shock at the same level as that before the shock:

$$
u \left(\left[ 1 + \delta_ {E V} \right] \cdot \hat {C}, \hat {T} _ {1} = 0, \hat {T} _ {2}, \hat {L}\right) = u \left(C ^ {*}, T _ {1} ^ {*}, T _ {2} ^ {*}, L ^ {*}\right).\tag{4}
$$

Simply put, we solve for the equilibrium outcome for each of the prices: one for $\bar { ( P , Q = 0 , W , F ) }$ and the other for $( P , \bar { Q } > 0 , W , F )$ . For each outcome, we calculate the household utility; finally, we calculate $\delta _ { E V }$ so that the level of utility remains the same between the two outcomes. Let $\delta _ { E V } ^ { \mathrm { t } }$ denote the value of $\delta _ { E V }$ for the particular prices $( P ^ { t } , \bar { Q } ^ { t } , W ^ { t } , F ^ { t } )$ for which the equilib rium outcome corresponds to the given state, denoted by superscript t. Let y<sup>t</sup>denote the level of compensation (i.e., in real dollar terms) corresponding to $\delta _ { E V } ^ { t } \mathrm { : }$

$$
y ^ {t} = \delta_ {E V} ^ {t} \cdot \hat {C} ^ {t}.\tag{5}
$$

Interpreting the state t in the model as the state of the economy in year t, we define an incremental annual welfare gain as an increase in $y ^ { t }$ compared with one period before:

$$
\begin{array}{c} \text {Incremental welfare gain} | _ {t - 1} ^ {t} = y ^ {t} - y ^ {t - 1} \\ = \left[ \delta_ {E V} ^ {t} \cdot \hat {C} ^ {t} \right] - \left[ \delta_ {E V} ^ {t - 1} \cdot \hat {C} ^ {t - 1} \right]. \end{array}\tag{6}
$$

One difficulty in interpreting this measure is that $\delta _ { E V } ^ { t }$ and y<sup>t</sup>are measured relative to the unobserved counterfactual income (equivalently consumption) $\hat { C } ^ { t }$ , whereas we often want to calculate welfare gain relative to the observed actual income $( \mathrm { e . g . , G D P ) }$ . As such, we can measure equivalent variation in an alternative way relative to the actual income. Let $\delta _ { E V } ^ { * }$ denote the fraction of actual income that should be reduced so as to let the household remain indifferent (in terms of utility) between the actual and counterfactual states:

$$
u \big (\hat {C}, \hat {T} _ {1} = 0, \hat {T} _ {2}, \hat {L} \big) = u \big ([ 1 - \delta_ {E V} ^ {*} ] \cdot C ^ {*}, T _ {1} ^ {*}, T _ {2} ^ {*}, L ^ {*} \big),\tag{7}
$$

The associated incremental annual welfare gain can then be defined as

Incremental welfare gain $\left| { { t } _ { t - 1 } ^ { t } } = { [ \delta _ { E V } ^ { * t } \cdot C ^ { * t } ] } - [ \delta _ { E V } ^ { * t - 1 } \cdot C ^ { * t - 1 } ] , \right.$

(8)

which can be interpreted as an annual increase in welfare attributable to the internet in terms of the observed income (i.e., real GDP).

2.2.3. Alternative Measure of Welfare: Money-Based Approach. There are two methods to estimate consumer surplus based on the expenditure on internet subscription fee. One is based on the cumulative method (Brynjolfsson 1996) that approximates the increase in the number of internet users each year. The other is to measure the variation in the share of direct expenditure by assuming a translog utility function, which is one of the least restrictive available (Bresnahan 1986). This index method estimates the consumer surplus as the area under the demand curve, whose sides equal the change in prices and the share of internet expenditure.

We present the welfare gain implied by the moneybased model using the index method in Equation (9). Each $P _ { t } , W _ { t } , s _ { t }$ stands for the internet price index, income, and expenditure share of internet, respectively.

$$
\begin{array}{r l} & I n c r e m e n t a l w e l f a r e g a i n | _ {t - 1} ^ {t} \\ & \quad = 0. 5 \times (s ^ {t} + s ^ {t - 1}) l n \left[ \frac {P ^ {t - 1}}{P ^ {t}} \right] W ^ {t}. \end{array}\tag{9}
$$

By construction, the money-based model does not allow us to calculate the time value of the hours spent on free sites, thus reflecting the traditional, expenditure-oriented approach to estimate welfare gain.

## 2.3. Discussion: Scope, Limitations, and Possible Extensions of the Model

We discuss the scope, limitations, and possible extensions of the model. More specifically, we discuss the issues of mobile internet consumption of content, content creation of “prosumers,” and irrational behaviors. We discuss how each of these issues could affect our estimate of the attention surplus and how we can extend the model to incorporate them if the data are available.

2.3.1. Mobile Internet Consumption of Content. Our model abstracts from mobile internet consumption that has increased recently (but not at the time of the sample period used in our analysis). We discuss how this affects our estimate of the attention surplus (if applied to the recent period when mobile internet consumption of content is significantly large). If we were to extend our model to include mobile internet consumption, then there are two plausible cases that might change our estimate of the attention surplus.

The first case is that including mobile internet hours increases the overall leisure-purpose internet hours. For example, people may consume content via mobile internet connection during commute time, which will increase the overall leisure-purpose internet hours beyond that confined at home. In this case, the consumer surplus from the overall leisure-purpose internet hours would be greater than our current estimate, mainly because mobile internet hours additionally generate the consumer surplus beyond that generated by home internet hours.

The second case is that considering mobile internet hours does not shift up or down the overall leisurepurpose internet hours. In this case, mobile internet hours would be a perfect substitute for home internet hours. As such, in this case, the consumer surplus from the overall leisure-purpose internet hours would not be affected by the device change or by internet network change.

Our current estimate is mainly based on the data on the residential personal computer (PC)-based leisurepurpose internet hours. Mobile internet could substitute for the PC as a device or as a network. This has a business implication that, because of such a compositional change over time, either different internet networks or different device providers could have different business opportunities (e.g., winners versus losers). But, if such a compositional change does not affect the overall leisurepurpose internet hours, then it would not affect our model-predicted consumer surplus from internet either.

We can extend the model to include mobile internet consumption of content. In such an extended model, the utility function of mobile internet consumption would be similar to that of home internet consumption, whereas mobile internet consumption’s cost (in terms of utility of forgone other leisure activities) could be negligible. For instance, mobile internet consumption taking place at the time of commuting to and from the workplace would not reduce the leisure hours. Therefore, introducing mobile internet consumption into an extended model might significantly increase the consumer surplus, depending on how much mobile internet hours crowd out home internet hours (i.e., how large a fraction of mobile internet consumption takes place during nonworking time at home and during commute time away from home).

2.3.2. Content Creation of Prosumers. Our model assumes that internet users consume content but not produce it by treating the supply of content as exogenously given. In reality, internet users often not only consume content but also produce it, aka prosumers (i.e., people who spend time on both consumption and production of online content). This is one of the limitations of our model, reflecting the fact that, in our data, household time spent on consumption of content and that on creation of content are aggregated rather than separated. As such, we discuss two issues about how the existence of prosumers is related to our estimate of the attention surplus. We also discuss how one can extend our model to estimate separately the consumer and producer surplus from internet when the detailed data on household time spent on content consumption and content production is available.

Implications of the content prosumers for the estimate of the attention surplus proposed in this paper are twofold and essentially depend on whether our data on leisure-purpose internet hours at home includes time spent on content creation. First, if our data on leisure-purpose internet hours at home does not include time spent on content creation (our baseline assumption in the paper), then the existence of content creators implies that our estimate of the attention surplus is actually the lower bound of the attention surplus. The reason is that our estimate is, by design, measuring the consumer surplus from internet, whereas the total surplus from internet is the sum of the consumer surplus and producer surplus from internet (and the producer surplus should be nonnegative for voluntary contributions).

Second, if our data on leisure-purpose internet hours at home does include time spent on content creation, then our estimate could be either over- or underbiased, depending on whether the consumer surplus per hour is either greater or smaller than the producer surplus per hour. Simply put, our estimate can be thought of as the total surplus from internet for the assumed case in which the consumer surplus per hour is equal to the producer surplus per hour. In the extended (correctly specified) model, the total surplus from internet would be calculated as consumption hours times the per-hour consumer surplus, plus production hours times the per-hour producer surplus.

It is likely that the magnitude of any bias in our estimate would be relatively small $( \mathrm { e . g . }$ , about less than a 10th of the total estimate). The main reason is that, in the decomposition of leisure-purpose internet hours at home between consumption- and production-purpose hours, the production-purpose hours are likely quite small relative to the consumption-purpose hours: less than about a 10th in the case of data on YouTube videos (according to the authors’ calculation). It is, of course, subject to further thorough empirical investigation whether the case of YouTube is representative regarding the ratio of the aggregate consumption hours to the aggregate production hours, which is left for future work.

We turn to discussing how we can extend the framework in this paper to incorporate the producer surplus from internet using the data on the aggregate hours on “unpaid” content production if such a data are available. Note that, in accordance with the standard methodology of calculating GDP, the hours spent on “paid” content production are already incorporated into GDP and, hence, should be excluded from our consideration in the calculation of the producer surplus from internet.

To extend our model to include the surplus of content creators, we should include both benefit and cost functions of attention paid by content creators. For instance, let $h _ { 3 }$ denote the amount of hours/attention paid by a “representative” household. To incorporate into our model the representative household decision about the optimal level of $h _ { 3 } ,$ we can introduce the utility function $V ( h _ { 3 } )$ and cost function $C ( h _ { 3 } )$ . In such an extended model, our estimate of the “attention surplus” would be essentially modified to include the additional term $[ V ( h _ { 3 } ) - C ( h _ { 3 } ) ]$ capturing the producer surplus of attention, whereas the consumer surplus component would be calculated by the same way as in the paper (using the data on the $\dot { \boldsymbol { \mu } } _ { \mathrm { p u r e ^ { \prime \prime } } }$ consumptionpurpose internet hours). Importantly, the benefit of content creator’s attention should be, in equilibrium, greater than the cost: $V ( h _ { 3 } ) > C ( h _ { 3 } ) _ { }$ ; otherwise, the content creator would not choose to pay the amount of attention $h _ { 3 }$ observed in the data. Thus, the producer surplus from internet $[ V ( h _ { 3 } ) - C ( h _ { 3 } ) ]$ should be positive; in this case, if our data on leisure-purpose internet hours at home does not include time spent on content creation, then the estimate of the attention surplus would be increased (rather than decreased) than our current estimate of the consumer surplus from internet.

One plausible specification of the utility function V $\left( h _ { 3 } \right)$ and cost function $C ( h _ { 3 } )$ is as follows: let $T _ { 3 } = z \cdot$ $g ( h _ { 3 } )$ denote the quantity of content produced by using content-creation hours $h _ { 3 }$ (captured by the contentproduction function $g ( h _ { 3 } ) )$ , where z represents the content-creation productivity. We can consider that $T _ { 3 }$ enters the representative household utility function $u ( C , T _ { 1 } , T _ { 2 } , T _ { 3 } , \mathbf { \bar { \Phi } } )$ as

$$
u (C, T _ {1}, T _ {2}, T _ {3}, L)
$$

$$
= \left\{ \begin{array}{l} \theta_ {0} \Big [ \theta_ {1} (T _ {1} + \kappa_ {1}) ^ {1 - \frac {1}{\sigma_ {1}}} + (1 - \theta_ {1}) (T _ {2} + \kappa_ {2}) ^ {1 - \frac {1}{\sigma_ {1}}} \Big ] ^ {\left(\frac {\sigma_ {1}}{\sigma_ {1 - 1}}\right) \cdot \left(1 - \frac {1}{\sigma_ {0}}\right)} \\ + (\theta_ {2}) [ (T _ {3} + \kappa_ {3}) ] ^ {\left(1 - \frac {1}{\sigma_ {0}}\right)} + (1 - \theta_ {0} - \theta_ {2}) [ C ^ {\alpha_ {0}} \cdot L ^ {1 - \alpha_ {0}} ] ^ {\left(1 - \frac {1}{\sigma_ {0}}\right)} \end{array} \right\} ^ {\frac {\sigma_ {0}}{\sigma_ {0} - 1}},
$$

$$
T _ {3} = z \cdot g (h _ {3}),\tag{A.1}
$$

(A.2)

$$
P \cdot C + F = W (1 - h _ {1} - h _ {2} - h _ {3} - L),\tag{A.3}
$$

where the cost function $C ( h _ { 3 } )$ is implicitly defined by h<sub>3</sub> entering the budget constraint in a way to reduce the working hours, similar to content-consumption time $h _ { 1 }$ does. Another alternative way of modeling the utility function $V ( h _ { 3 } )$ is to let the household receive monetary compensation proportional to $T _ { 3 }$ instead of letting $\dot { T _ { 3 } }$ directly enter the household utility function.

In such an extended model of the representative prosumer’s consumption and production of content, the attention surplus can be calculated by essentially the same way as in the current model. That is, we calculate the fraction of actual income that should be reduced so as to let the household remain indifferent (in terms of utility) between the actual state and counterfactual state (with $T _ { 1 } = T _ { 3 } = 0 )$ .

2.3.3. Irrational Behaviors. To measure the attention surplus, we need to assume whether the observed household decisions about their time spending are made rationally. We use the “rationality” assumption in our model, as in the standard way GDP is calculated. The issue is whether household decisions about their spending (either money or time) are made either rationally or irrationally (e.g., overspending because of addiction).

In measuring the consumer surplus from the internet, our aim is to try to be as close to the methodology of calculating GDP as possible because we want to examine how our measure of the consumer surplus from the internet is different from that implied by GDP. For instance, aggregate consumption of tobacco is included in GDP regardless of whether a sizable fraction of aggregate consumption of tobacco is driven by addiction; by doing so, the standard way of calculating welfare from goods traded in the markets assumes that consumption of tobacco is completely determined by rational consumers. Our approach is based on the same assumption as this. By doing so, our measure of the consumer surplus from the internet is comparable to GDP; otherwise, we cannot discuss how our framework differs from the standard way of measuring GDP.

If a substantial part of time spent on consumption of content on the internet is driven by irrational motive (e.g., addiction), then our method based on the assumption of rational consumers would lead to the overestimation problem. The cost side of attention (or time) is discussed as a growing concern of digital addiction or self-control problems in the digital economy literature (e.g. Allcott et al. 2022).<sup>12</sup> To measure the effect of digital addiction on time use, Allcott et al. (2022) introduce several randomized trials of popular apps such as Facebook, Instagram, and YouTube on smartphones. They find that about 31% of social media use is due to self-control problems. If about 31% of time use on internet is an outcome of irrational addiction, then our estimate of the consumer surplus from internet could be overestimated by 31% because of ignoring these addicted choices.

It is, however, subject to further investigation whe ther about 31% of an average internet user’s time spending observed over a long period is an outcome of irrational addiction. Note that our longitudinal framework to calculate welfare does not rely on crosssectional variations at one point of time response. Our estimate is obtained by using the average user’s timeuse data yearly, not the whole variations of survey response data across individuals often needed in crosssectional analysis. We measure the consumer surplus from internet time usage of a representative (or average) person over a decade. If all internet users spend 31% of their time irrationally during a decade, it is questionable whether all these users’ persistent choices can truly be attributed solely to irrational decision making and a lack of self-control. Most of the studies that examine digital addiction behaviors is based on crosssectional data or short-term period data for a few months. There is not much longitudinal evidence of digital addiction in a long-term period, for instance, more than a few years.

## 3. Quantitative Analysis 3.1. Data

The internet hour data are taken from the Consumer Technographics from Forrester Research and the Three Screen Report from Nielsen. Consumer Technographics is a mail survey conducted annually for more than 30,000 households and is meant to be nationally representative. The survey includes time usage information on how many hours per week the respondent spends on the internet for leisure and work reasons separately. The data also include the average years of internet experi ence, household income level, wealth, education, employment, and characteristics of internet services used. Whereas the sample of respondents each year changes over time, we can construct a set of balanced panels over time by identifying specific users who were included in the mail survey for four consecutive years.

We distinguish between two types of internet hours spent at home—leisure and work—because they have different implications for welfare and have increased at very different rates over the last 10 years. The Three Screen Report from Neilson provides residential internet hours data starting as early as 1994. We construct the annual data on leisure-purpose internet hours at home by scaling down the total residential internet hours data from Nielsen to fit the nonwork-purpose internet usage data from the balanced panel of Forrester research during 2007–2011.<sup>13</sup> We find that people spent an average of 3.4 hours on the internet for leisure every week during these years. The leisurepurpose internet hours were about 63% of the total residential internet hours, whereas the remaining internet use was dedicated to work.<sup>14</sup> We compare the consumer value of internet with respect to the television. Data for television viewing hours come from the American Time Usage Survey (ATUS).<sup>15</sup> On average, people spent 19 hours watching television every week during the period, which is more than five times greater than the hours spent on the internet.

## 3.2. Calibration

We use our model to quantify changes in the welfare gain from internet. In order to compute this, we have to calibrate six preference parameters: the elasticity of substitution parameters, $( \sigma _ { 0 } , \sigma _ { 1 } ) _ { i }$ ; the weight on the utility from the time spent on internet and the bundle of internet television together, $( \theta _ { 0 } , \theta _ { 1 } ) ;$ ; and the parameters $( \kappa _ { 1 } , \kappa _ { 2 } )$ that determine the utility level when the hours spent on internet and television are zero.<sup>16</sup> Altogether, these parameters specify the utility from internet, television, and other goods. We find the sources of changes in the welfare gain from internet to be primarily changes in observed hours spent on internet and television, income, adoption, and quality improvement of internet.

Table 1. Calibration of Parameters

<table><tr><td> $\sigma_0$ </td><td> $\sigma_1$ </td><td> $\theta_0$ </td><td> $\theta_1$ </td><td> $\kappa_1$ </td><td> $\kappa_2$ </td><td> $R^2$ </td></tr><tr><td>1.25</td><td>1.410</td><td>0.476</td><td>0.256</td><td>0.045</td><td>0.244</td><td>0.987</td></tr><tr><td>1.26</td><td>1.419</td><td>0.486</td><td>0.253</td><td>0.044</td><td>0.247</td><td>0.989</td></tr><tr><td>1.28</td><td>1.438</td><td>0.492</td><td>0.255</td><td>0.044</td><td>0.246</td><td>0.988</td></tr><tr><td>1.30</td><td>1.445</td><td>0.499</td><td>0.255</td><td>0.044</td><td>0.250</td><td>0.990</td></tr></table>

Notes. This table presents the parameter values from the calibration. The range of $\sigma _ { 0 }$ in the first column is obtained from the regression results based on Equation (3), and the remaining set of parameters $( \sigma _ { 1 } , \theta _ { 0 } , \theta _ { 1 } , \kappa _ { 1 } , \kappa _ { 2 } )$ in the other columns are from the calibration results. The procedures and estimation results are described in the online appendix.

The calibration is based on the following steps.<sup>17</sup> The predicted time spent on internet at year $\bar { t } , h _ { 1 } ^ { * t }$ , is computed by plugging in the corresponding quality, price, and income level, $( Q ^ { t } , P ^ { t } , W ^ { t } )$ , into the demand functions. The preference parameters can be determined by minimizing the sum of the squared differences between the actual time spent on internet observed in the data $h _ { 1 } ^ { D a t a , \ t }$ during the sample period from 1998 to 2011 and the model-predicted time $\begin{array} { r } { \dot { h } _ { 1 } ^ { * t } = T _ { 1 } ^ { * t } ( \sigma _ { 0 } , \sigma _ { 1 } , \theta _ { 0 } , \theta _ { 1 } , \kappa _ { 1 } , } \end{array}$ $\mathrm { \Sigma } _ { \kappa 2 } ; Q ^ { t } , P ^ { t } , W ^ { t } ) / Q ^ { \dot { t } } . \mathrm { \Sigma } ^ { 1 8 }$ We calibrate the parameters by solving the following minimization problem:

$$
\begin{array}{l} \min _ {\sigma_ {0}, \sigma_ {1}, \theta_ {0}, \theta_ {1}, \kappa_ {1}, \kappa_ {2}} \sum_ {t = 1 9 9 8} ^ {2 0 1 1} \\ \left[ h _ {1} ^ {D a t a, t} - \frac {T _ {1} ^ {* t} (\sigma_ {0} , \sigma_ {1} , \theta_ {0} , \theta_ {1} , \kappa_ {1} , \kappa_ {2} ; Q ^ {t} , P ^ {t} , W ^ {t})}{Q ^ {t}} \right] ^ {2}. \end{array}\tag{10}
$$

Table 1 presents the parameter values from the calibration. As predicted, the elasticity of the substitution between the internet and television, $\sigma _ { 1 } ,$ , is greater than that between the internet and other goods, $\sigma _ { 0 }$ . This implies that the internet and television are closer substitutes than the internet and all other goods. The parameters $\theta _ { 1 }$ and $\theta _ { 0 }$ compare the relative importance of the internet bundle with respect to the television bundle and of both bundles with respect to other goods. The value of $\kappa _ { 1 }$ and $\kappa _ { 2 }$ implies that the measured surplus from the internet and television could be overestimated without considering these parameters in the model. We choose parameter values corresponding to $\sigma _ { 0 } = 1 . 2 6$ as our benchmark case.

3.3. Main Results: Welfare Gain from the Internet Table 2 summarizes the estimates from the two meth ods: the time-based model from Equation (8) and the money-based approach from Equation (9). In our time-based model, we estimate that the level of annual consumer surplus created from the internet is, on average, \$302 billion (about \$1,447 per user). On average, the incremental annual gain from the internet is about \$38 billion during 2002–2011. In contrast, the money-based approach relies on the market share of the internet cost as measured in dollars spent. Overall, we estimate the annual surplus increase to be abou \$2.7 billion when we apply the money-based approach.

The difference between the time-based model and the money-based approach is enormous, averaging more than \$35 billion per year. Our results suggest that only about 7% of the total welfare gain from the internet would be revealed by estimates that rely only on the direct dollar expenditure. The full gain is visible only when one considers the time used. The result implies that there is a gain each year equivalent to nearly 0.29% of the annual GDP from the internet. GDP measures production and not welfare, so this gain does not appear in the GDP or productivity statis tics. Nonetheless, it creates real value for consumers.

We estimate the consumer surplus gain from free goods and services based on the time spent on free sites. On average, more than two thirds of the time spent online is on free sites (Stranger and Greenstein 2007), which suggests that a commensurate share of the welfare gain comes from free sites.<sup>19</sup> Annually, the increase in value because of free online goods is about \$38 billion, and this corresponds to about \$180 every year for individuals according to the time-based model. In contrast, the money-based approach implies that the yearly value of free goods on the internet is only \$13 per user.<sup>20</sup> The values from the time-based model appear more plausible.

Table 2. Estimation of Annual Consumer Surplus from the Internet

<table><tr><td>Year</td><td>Time-based model</td><td>Annual gain (time-based model)</td><td>Annual gain (money-based model)</td></tr><tr><td>2002</td><td>$129.2 B</td><td>$19.1 B</td><td>$0.63 B</td></tr><tr><td>2003</td><td>$159.2 B</td><td>$29.9 B</td><td>$0.67 B</td></tr><tr><td>2004</td><td>$185.8 B</td><td>$26.6 B</td><td>$2.23 B</td></tr><tr><td>2005</td><td>$215.4 B</td><td>$29.6 B</td><td>$2.23 B</td></tr><tr><td>2006</td><td>$274.3 B</td><td>$58.9 B</td><td>$5.02 B</td></tr><tr><td>2007</td><td>$345.9 B</td><td>$71.6 B</td><td>$14.12 B</td></tr><tr><td>2008</td><td>$375.2 B</td><td>$29.3 B</td><td>$0.48 B</td></tr><tr><td>2009</td><td>$398.6 B</td><td>$23.4 B</td><td>$(1.25) B</td></tr><tr><td>2010</td><td>$453.9 B</td><td>$55.3 B</td><td>$0.90 B</td></tr><tr><td>2011</td><td>$487.4 B</td><td>$33.4 B</td><td>$2.41 B</td></tr><tr><td>Average (2002–2011)</td><td>$302.5 B</td><td>$37.7 B</td><td>$2.7 B</td></tr><tr><td>Annual value per user</td><td>$1,447/user</td><td>$180/user</td><td>$13/user</td></tr></table>

Notes. This table presents the results for the consumer surplus using the time- and money-based models. The first column presents our estimate of the level of consumer surplus gained from the internet. The second and third columns summarize the incremental annual gain of consumer surplus from the internet using the time- and money-based models.

Table 3. Yearly Incremental Gain in Consumer Value from Free Internet Sites

<table><tr><td></td><td>Reach, %</td><td>Minutes</td><td>Time share, %</td><td>Yearly increase in consumer surplus ($Billion)</td></tr><tr><td>Facebook</td><td>0.434</td><td>24</td><td>16.00</td><td>6.1</td></tr><tr><td>YouTube</td><td>0.330</td><td>17</td><td>8.62</td><td>3.3</td></tr><tr><td>Twitter</td><td>0.093</td><td>7</td><td>0.99</td><td>0.4</td></tr><tr><td>Wikipedia</td><td>0.144</td><td>4</td><td>0.88</td><td>0.3</td></tr><tr><td>LinkedIn</td><td>0.050</td><td>7</td><td>0.53</td><td>0.2</td></tr><tr><td>Craigslist</td><td>0.015</td><td>13</td><td>0.30</td><td>0.1</td></tr></table>

Notes. The rightmost column presents the annual increase in consumer value from free internet sites. This calculation is based on the annual welfare gain from the internet, \$38 billion, multiplied by the time share of each site.

Table 3 provides the consumer value gained from free internet sites based on their time share on the internet in 2011. For instance, the time shares of Facebook, YouTube, and Wikipedia were about 16%, 9%, and 1%, respectively, of the total time spent online (ComScore.com 2011). Thus, in the case of Facebook, our model implies an annual incremental gain in consumer value of about \$6.1 billion during this period.

In 2011, the total revenue of Facebook was reported as \$3.7 billion, and Facebook expenses were \$2.7 billion. This implies that the marginal value to consumers per dollar of revenue of Facebook was around 1.6 (from the value/revenue ratio), and the marginal gain in the consumer value per dollar of expense was around 2.3 (from the value/cost ratio).<sup>21</sup>

## 3.4. Comparison with Television

An advantage of our model is that one can estimate the welfare gain from innovations not only for digital goods, but for any good or technology whose money price is not observable or nonexistent as long as we have relevant time-use data. One of the most important and comparable leisure goods to the internet is television. Following the approach used for the internet, the welfare gain is computed for the television together with the internet, using the time spent on television.

Figure 1 illustrates the consumer surplus from the overall internet, free goods on the internet, and television. Note that the overall hours spent on television are much higher than those spent on the internet; consumers spent around 19 hours in a week on television. On the other hand, the growth rate of time spent on television is relatively flat compared with that for the internet.

Table 4 compares our results for television, the internet, and free sites on the internet. The equivalent variation from television is around 10% of the GDP, which is nearly four times higher than the value of internet, calculated as 2.3% of the GDP. However, the incremental annual gain from television during the same period is about \$23.9 billion, which is significantly less than the annual welfare gain from the internet during this period, calculated as \$37.7 billion.

Figure 1. Consumer Surplus (in Terms of Equivalent Variation) from the Internet, Free Goods, and Television  
![](/api/attachments/DPAFDGXW/fulltext/images/f5a355750c1ec8dec04cbd9074003100c4b1a1951d62a464216a18e7e9b2660d.jpg)  
Notes. This figure presents the calibration results of our model. It compares consumer surplus in terms of equivalent variation (percentage shar of GDP) from the internet, free sites on the internet, and television.

Table 4. Comparison of Consumer Surplus from Television, Internet, and Free Sites

<table><tr><td>Year</td><td>Television</td><td>Annual gain from television</td><td>Internet</td><td>Annual gain from internet</td><td>Free sites</td><td>Annual gain from free sites</td></tr><tr><td>2002</td><td>$1,141.0 B</td><td>$14.6 B</td><td>$129.2 B</td><td>$19.1 B</td><td>$86.2 B</td><td>$12.7 B</td></tr><tr><td>2003</td><td>$1,184.1 B</td><td>$43.0 B</td><td>$159.2 B</td><td>$29.9 B</td><td>$106.1 B</td><td>$19.9 B</td></tr><tr><td>2004</td><td>$1,267.6 B</td><td>$83.5 B</td><td>$185.8 B</td><td>$26.6 B</td><td>$123.9 B</td><td>$17.8 B</td></tr><tr><td>2005</td><td>$1,261.4 B</td><td>-$6.2 B</td><td>$215.4 B</td><td>$29.6 B</td><td>$143.6 B</td><td>$19.7 B</td></tr><tr><td>2006</td><td>$1,297.0 B</td><td>$35.6 B</td><td>$274.3 B</td><td>$58.9 B</td><td>$182.9 B</td><td>$39.3 B</td></tr><tr><td>2007</td><td>$1,310.6 B</td><td>$13.6 B</td><td>$345.9 B</td><td>$71.6 B</td><td>$230.6 B</td><td>$47.8 B</td></tr><tr><td>2008</td><td>$1,385.8 B</td><td>$75.1 B</td><td>$375.2 B</td><td>$29.3 B</td><td>$250.1 B</td><td>$19.5 B</td></tr><tr><td>2009</td><td>$1,284.5 B</td><td>-$101.3 B</td><td>$398.6 B</td><td>$23.4 B</td><td>$265.8 B</td><td>$15.6 B</td></tr><tr><td>2010</td><td>$1,351.7 B</td><td>$67.3 B</td><td>$453.9 B</td><td>$55.3 B</td><td>$302.7 B</td><td>$36.9 B</td></tr><tr><td>2011</td><td>$1,365.8 B</td><td>$14.0 B</td><td>$487.4 B</td><td>$33.4 B</td><td>$324.9 B</td><td>$22.3 B</td></tr><tr><td>Average</td><td>$1,284.9 B</td><td>$23.9 B</td><td>$302.5 B</td><td>$37.7 B</td><td>$201.7 B</td><td>$25.2 B</td></tr></table>

Note. This table presents each of our estimates of the level of consumer surplus and incremental annual gain from television, the internet, and free sites on the internet.

## 4. Discussion

Several interesting comparisons can be made using our estimates. First, the time-based measures are much higher—more than an order of magnitude larger— than the money-based measures that are traditionally used for consumer surplus calculations. In our view, time-based measures are a more meaningful metric of welfare. For example, we can compare our estimate with respect to a simple back-of-the-envelope estimate based on the opportunity cost of time. On average, 34% of the average person’s waking hours was time spent working. In turn, labor income share accounts for about 60% of the GDP. About 3.5% of waking hours were spent on the free internet sites based on our estimation. Thus, the number of hours spent on the internet is roughly equal to the number of hours used to generate about 6% of the GDP.<sup>22</sup> In turn, the annual growth rate of the GDP is around 2%–3%, and 6% of that figure would be a gain of 0.12%–0.18% each year. The annual welfare increase implied by our time-based model of free internet goods is \$25 billion, which translates to 0.19% of GDP—not far from the back-of-theenvelope estimate. This strikes us as more reasonable than the 0.02% value derived from the purely moneybased approach.

Second, our estimate of the annual gain of \$38 billion from both free and paid internet goods is higher than the annual welfare gain of \$24 billion from television in recent years estimated using the same model. This is despite most people spending a larger number of hours watching TV. Whereas the level of welfare from television is around four times higher than that from internet, the latter is increasing more rapidly than the former, so the annual increase in welfare attributed to the internet is higher.

Third, the implications of increasing mobile internet consumption on welfare must be considered. Two potential cases arise when analyzing the impact of mobile internet consumption. The first case is that including mobile internet hours will lead to an increase in overall leisure-purpose internet hours, resulting in a greater consumer surplus than our current estimate of \$38 billion. The second case is when mobile internet hours do not significantly affect overall leisure-purpose internet hours, and therefore, the consumer surplus estimate will not change because of device or internet network changes. It is important to note that the current estimate is primarily based on residential PC-based leisurepurpose internet consumption. Whereas mobile internet may replace PCs as a device or network for accessing the internet, if overall leisure-purpose internet time does not change significantly, the consumer surplus from free internet may remain unchanged. Further research is needed to explore the impact of mobile internet consumption on internet usage patterns and its implications for consumer welfare.

Our results, based on the sample data over the period 2002–2011 may also provide insight into current and future welfare gains from the internet. The ongoing increase in both the quality and quantity of the free goods on the internet is the main reason that we obtain our empirical results for the sizable yearby-year increase in the consumer surplus from the internet. These steady increases in the quality and quantity of free goods on the internet are likely to continue through the present time and near future, too, because of the ongoing improvement in digital technology and increased digitization and expansion of various services available on the internet.

There are various factors that will continue to increase the quality of free goods on the internet. These factors include the ongoing improvements in internet technology, innovative service provision, and the adoption of faster internet services such as fiber internet. These factors, coupled with individual users’ preferences and changing circumstances, such as the COVID-19 pandemic, greatly shape time-use decisions and consumer surplus.

From a policy perspective, it is essential to consider the impact of these factors on consumers’ welfare. Whereas the provider-side factors have a positive impact on the internet-biased technology change or innovation, increasing concerns about internet usage, such as the spread of fake news, privacy concerns, and the intrusiveness of targeted ads, can negatively influence users’ decision on internet hours. Therefore, policymakers need to address these issues to ensure that consumers can enjoy the benefits of the internet without being exposed to its negative effects.

Furthermore, individual user-side preference changes, life-cycle patterns, and macroeconomic conditions, such as a decline in opportunity cost or market wages, can also affect consumer choice and welfare. Policymakers should consider these factors when designing policies that support digital inclusion and address issues of inequality and welfare.

Whereas we can discuss potential implications of each market-side, provider, and user-side time-varying factors on welfare, calculating the change in the amount of consumer surplus is not always clear because of the impact of multiple factors. However, predicting the welfare change after this period based on corresponding data can help policymakers make relevant implications for welfare measurement, and it should be a crucial area for future work.

## 5. Concluding Remarks

The internet and related technologies have created a ubiquitous platform for delivering digital goods at nearly zero marginal cost. However, metrics such as GDP or even traditional approaches to consumer surplus cannot accurately reflect the value of these innovations when the market prices are effectively zero. Advertising revenues are not reflective of these goods contribution to consumer surplus either. The mismeasurement problem is especially important considering the growing number of new goods available on the internet, where most of the real cost to users is in terms of time and not money. Decision making on investments in these goods and services, on public policy, on management, and on research agendas must begin with an accurate assessment of their mag nitude and value. We need to update our measurement framework along with our ability to deliver more and better goods at zero marginal cost.

In this paper, we use such a framework to estimate the consumer surplus created by two different types of imperfectly substitutable free goods by considering the time component. Furthermore, we contrast the results with those obtained from traditional methods that emphasize the value of direct market expenditures as measured in dollar terms. Using data on the expenditure share, market price, internet adoption rate, and time spent using the internet at home, we estimate that the incremental welfare gain from free goods and services averaged more than \$25 billion per year during 2002–2011. This is equivalent to a large fraction of the average annual growth in GDP in those years. We also find that most of the total welfare gain would be overlooked by approaches that rely only on direct dollar expenditures. Our approach can be readily extended to more goods and services as well as for alternative adjustments for quality.

## Appendix

Table A.1. Comparison of Models

<table><tr><td>Features</td><td>Our model</td><td>Goolsbee and Klenow (2006)</td><td>Greenwood and Kopecky (2013)</td></tr><tr><td>Data: time series versus cross-section</td><td>Time series</td><td>Cross-section</td><td>Time series</td></tr><tr><td>Welfare from internet/PCs</td><td>Internet</td><td>Internet</td><td>PC</td></tr><tr><td>Time-based welfare gain</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Quality index</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Changes in welfare gain over time</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Preferences: TV separate from other leisure activities</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Overestimation: extreme initial values</td><td>No</td><td>Yes</td><td>No</td></tr><tr><td>Decision making: rational/irrational assumption</td><td>Rational</td><td>Rational</td><td>Rational</td></tr><tr><td>Structural model of demand</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Table A.2. Key Variables Related to the General Case of the Three Bundles of Goods: Internet, Television, and All Other Goods

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $I_1$ </td><td>Money-based service flow of internet at home</td></tr><tr><td> $I_2$ </td><td>Money-based service flow of television at home</td></tr><tr><td> $T_1$ </td><td>Time-based service flow of internet at home:  $T_1 = h_1 \times Q$ </td></tr><tr><td> $h_1$ </td><td>Amount of time spent on, combined with time-varying quality  $Q$ , production of  $T_1$ </td></tr><tr><td> $Q$ </td><td>Time-varying quality of internet, enhancing productivity of  $h_1$  (e.g., internet speed)</td></tr><tr><td> $T_2$ </td><td>Time-based service flow of television at home:  $T_2 = h_2$ </td></tr><tr><td> $h_2$ </td><td>Amount of time spent on, combined with constant quality, production of  $T_2$ </td></tr><tr><td> $L$ </td><td>Amount of time spent on (all other) leisure activities</td></tr><tr><td> $C$ </td><td>Composite goods consumption</td></tr></table>

## Endnotes

<sup>1</sup> See https://ourworldindata.org/internet#the-rise-of-social-mediain-rich-countries-has-come-together-with-an-increase-in-the-amountof-time-spent-online.

<sup>2</sup> Except potentially via an indirect increase in the price of final consumption of other goods as a part of the GDP.

<sup>3</sup> Differences in features (e.g., data, model, methodology) between our paper and G&K are listed in Table A.1.

<sup>4</sup> Even when digital goods are not free, they often have prices that are very low and have little or no empirical relationship to changes utility or consumption quantities, making inferences about welfare difficult or impossible.

<sup>5</sup> Goolsbee and Klenow’s (2006) estimate of consumer surplus from the internet using a log-linear utility specification was about 10 times larger than their estimate using a linear utility assumption.

<sup>6</sup> For instance, in the log-linear utility specification, the utility derived from internet use for an individual can approach infinity as time spent on it approaches zero.

<sup>7</sup> Contribution of free internet services to larger welfare is the topic of current academic and political discussion in the United States as many firms facing public scrutiny are attracting regulatory scrutiny. It is worthwhile to note that our estimates do not fully account for the externalities effects of consuming these goods.

<sup>8</sup> Goolsbee and Klenow (2006), Krusell et al. (2000), and Greenwood and Kopecky (2013) also use a CES-type utility function. They analyze substitution elasticity only between the internet or personal computer and all other goods.

<sup>9</sup> The parameters $\alpha _ { 1 } , \alpha _ { 2 }$ , and $\alpha _ { 0 }$ can be written by using the consumer’s equilibrium decision rules as $\alpha _ { 1 } = P _ { 1 } I _ { 1 } / ( P _ { 1 } I _ { 1 } + W T _ { 1 } ) , \alpha _ { 2 } =$ $P _ { 2 } I _ { 2 } / ( P _ { 2 } I _ { 2 } + W T _ { 2 } )$ ), and $\alpha _ { 0 } = P C / ( P C + W L )$ , respectively, where $P _ { 1 . }$ $P _ { 2 } ,$ and P denote the price of each good.

<sup>10</sup> The implication of relaxing the assumption of $\alpha _ { 1 }$ equal to zero and incorporating a positive share of marginal price for internet usage would decrease the estimate of consumer surplus when $I _ { 1 }$ is constant. In turn, if $I _ { 1 } ,$ the internet content amount also increases as $T _ { 1 }$ increases, then even though α is a positive number, consumer surplus will not decrease and produce the same level of utility.

${ } ^ { 1 1 } \mathrm { O r } ,$ equivalently, in terms of a fraction of income as income equals consumption in this model.

<sup>12</sup> Furthermore, there is evidence that time spent on social media may have negative effects on mental health (Braghieri et al. 2022)

<sup>13</sup> Forrester Research substantially changed its methods for determining the number of hours spent on the internet between the 2006 and 2007 surveys. Among other things, it changed the focus of their sample to all consumers instead of only internet users. This is reflected in a large—and we think spurious—drop in the reported level of hours spent on the internet per respondent in 2007 versu 2006. For this reason, we perform our analyses using balanced panel data during 2007–2011, which seem to be consistent.

<sup>14</sup> See Table S2 in the online appendix that summarizes internet hours and demographics data from the balanced panel constructed based on the Forrester Research data.

<sup>15</sup> Data on television hours from 2003–2012 are from ATUS. For the period before 2003, we extend the television viewing hours index developed by Rachel Soloveichik (BEA) fitting the trend of ATUS. Note that all other sources of television viewing hours, for instance, Forrester Research, Nielsen Sound Scan, and New Marketer, report higher hours than the ATUS.

<sup>16</sup> Additionally, the consumption-leisure preference parameter α<sub>0</sub> is, in equilibrium, tightly related to the shadow value of leisure (WL)-to-consumption expenditure (PC) ratio: $\alpha _ { 0 } = 1 / ( 1 + [ W L / P C ] ) _ { , }$ of which observed value in the data varies over time. Therefore, we calibrate the year-specific value of $\alpha _ { 0 }$ so that $\alpha _ { 0 } ^ { t } = P ^ { t } C ^ { t } / ( P ^ { t } C ^ { t } + W ^ { t } L ^ { t } )$ should be satisfied given the data on total expenditure, internet expenditure, internet hours, and television hours, whereas working hours are assumed to be constant (40 hours per week). We use th budget constraint equation: $P \cdot C + F = W ( 1 - h _ { 1 } - h _ { 2 } - L )$ to replace $P ^ { t } C ^ { t }$ and W<sup>t</sup>L<sup>t</sup> by the items observed in the data, following a similar methodology to Goolsbee and Klenow (2006).

<sup>17</sup> See the online appendix for detailed discussion of the procedure and results of the calibration.

<sup>18</sup> In our analysis, internet hours (at home), increasing rapidly over time during our sample period, are of primary importance, whereas TV hours, which do not increase much during our sample period, are of secondary importance. Therefore, we do not include the distance between the observed and model-predicted TV hours in the objective function of our estimation. Alternatively, we can include the distance between the observed and model-predicted TV hours with a weight less than one in the objective function.

<sup>19</sup> If there exists a positive (or negative) correlation between an individual’s overall time spent on the internet and the relative value of free goods, then the share of consumer surplus from free goods might be higher (or lower). For simplicity, we do not consider any correlation.

<sup>20</sup> These values are calculated based on the following estimates: the number of average internet users during 2002 and 2011 was about 209 million, and about 2.7 hours per week were spent on free sites.

<sup>21</sup> Notably, this takes consumer preferences as sovereign and does not question them. Evidence from behavioral economics indicate that consumers sometimes regret their decision on how they spend their time or money.

<sup>22</sup> This x% portion of GDP can be calculated from the equation: 34% (time share of working): 60% (money share of working) � 3.5% (time share of free internet sites): x% (money share of internet), which yields $x \approx 6 . 1 8 ,$ , that is, about 6%.

## References

Allcott H, Gentzkow M, Song L (2022) Digital addiction. Amer. Econom Rev. 112(7):2424–2463.

Allcott H, Braghieri L, Eichmeyer S, Gentzkow M (2019) The welfare effects of social media. Technical report, National Bureau of Economic Research, Cambridge, MA.

Braghieri L, Levy R, Makarin A (2022) Social Media and Mental Health. Amer. Econom. Rev. 112(11):3660–3693.

Bresnahan TF (1986) Measuring the spillovers from technical advance: mainframe computers in financial services. Amer. Econom. Rev. 76(4):742–755.

Brynjolfsson E (1996) The contribution of information technology to consumer welfare. Inform. Systems Res. 7(3):281–300.

Brynjolfsson E, Collis A (2019) How should we measure the digital economy? Harvard Bus. Rev.

Brynjolfsson E, Oh JH (2012) The attention economy: Measuring the value of free goods and services on the internet. Proc. 33rd Internat. Conf. Inform. Systems (ICIS 2012) (Curran Associates, Inc., Red Hook, NY), 3243–3261.

Brynjolfsson E, Collis A, Eggers F (2019) Using massive online choice experiments to measure changes in well-being. Proc. Natl. Acad. Sci. USA 116(15):7250–7255.

Brynjolfsson E, Collis A, Diewert WE, Eggers F, Fox KJ (2020) Mea suring the impact of free goods on real household consump tion. AEA Papers Proc. 110:25–30.

Byrne DM, Fernald JG, Reinsdorf MB (2016) Does the United States have a productivity slowdown or a measurement problem? Brooking Papers Econom. Activity, 109–157.

ComScore.com (2011) comscore.com/Insights/Rankings.

Corrado C, Hulten C, Sichel D (2009) Intangible capital and U.S. economic growth. Rev. Income Wealth 55(3):661–685.

Diamond PA, Hausman JA (1994) Contingent valuation: Is some number better than no number? J. Econom. Perspect. 8(4): 45–64.

Diewert WE, Fox KJ, Schreyer P (2018) The digital economy, new products and consumer welfare. University of British Columbia,

Vancouver, BC. http://escoe-website.s3.amazonaws.com/wpcontent/uploads/2020/07/13162401/ESCoE-DP-2018-16.pdf.

Goolsbee A, Klenow PJ (2006) Valuing consumer products by the time spent using them: An application to the internet. Amer. Econom. Rev. 96(2):108–113.

Greenwood J, Kopecky KA (2013) Measuring the welfare gain from personal computers. Econom. Inquiry 51(1):336–347.

Krusell P, Ohanian LE, Rios-Rull J, Violante GL (2000) Capital-skill complementarity and inequality: A macroeconomic analysis. Econometrica 68(5):1029–1053.

Nakamura L, Samuels J, Soloveichik R (2016) Capturing the productivity impact of the “free” apps and other ad-supported media Working paper, Federal Reserve Bank of Philadelphia, Philadelphia.

Nevo A, Turner JL, Williams JW (2016) Usage-based pricing and demand for residential broadband. Econometrica 84(2):411–443.

Spence M, Owen B (1977) Television programming, monopolistic competition, and welfare. Quart. J. Econom. 91(1):103–126.

Stranger G, Greenstein S (2007) Pricing indexes for ISPs during the 1990s: Hard-to measure goods and services. NBER Conf. Res Income Wealth, vol. 67 (The University of Chicago Press).

Varian H (2006) The economics of internet search. Rivista di politica economica 96(11/12):177–191.

Zheng E, Pavlou P, Gu B (2014) Latent growth modeling for information systems: Theoretical extensions and practical applica tions. Inform. Systems Res. 25(3):547–568.

C<sub>opy</sub>ri<sub>g</sub>ht 2024 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>

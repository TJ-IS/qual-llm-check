---
otero_id: 876
otero_key: "NG8HHDW7"
title: "Predicting home-appliance acquisition sequences: Markov/Markov for Discrimination and survival analysis for modeling sequential information in NPTB models"
authors: "Anita Prinzie; Dirk Van den Poel"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.02.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Predicting home-appliance acquisition sequences: Markov/Markov for Discrimination and survival analysis for modeling sequential information in NPTB models

Anita Prinzie<sup>⁎</sup>, Dirk Van den Poel <sup>1</sup>

Department of Marketing, Faculty of Economics and Business Administration, Ghent University, Tweekerkenstraat 2, B-9000 Ghent, Belgium

Received 18 October 2005; received in revised form 12 February 2007; accepted 17 February 2007 Available online 23 February 2007

## Abstract

The acquisition process of consumer durables is a ‘sequence’ of purchase events. Priority-pattern research exploits this ‘sequential order’ to describe a prototypical acquisition order for durables. This paper adds a predictive perspective to increase managerial relevance. Besides order information, the acquisition sequence also reveals precise timing between purchase events (‘sequential duration’) as examined in the literature on durable replacement and time-to-first acquisition. This paper bridges the gap between priority-pattern research and research on duration between durable acquisitions to improve the prediction of the product group the customer might acquire his next durable from, i.e. Next-Product-to-Buy (NPTB) model. We evaluate four multinomialchoice models incorporating: 1) general covariates, 2) general covariates and sequential order, 3) general covariates and sequential duration, and 4) general covariates, sequential order and duration. The results favor the model including general covariates and duration information (3). The high predictive value of sequential-duration information emphasizes the predictive power of duration as compared to order information.

Keywords: Cross-sell; Sequence analysis; Choice modeling; Durable goods; Analytical CRM

## 1. Introduction

During the past decade the competition in the homeappliances market has grown substantially due to an increasing number of suppliers ranging from traditional home-appliances retailers, hypermarkets to even drug stores and DIY chains. Most customers applaud this evolution. The competition leads to lower prices. Moreover, the broader distribution increases exposure to innovations like mp3-players thereby speeding up adoption [25]. Customers are indifferent to acquiring durables at a grocery multiple or at a specialty store. In Belgium, the country our data originates from, specialist independents have been losing share to specialist multiples, with the latter losing shares to grocery multiples [20,21]. This increased competition emphasizes the importance of cross-selling strategies, i.e. efforts aimed to augment the number of products customers use from the firm. Shrinking margins for many appliances [5] imply larger volume to maintain profits. As selling additional products to existing customers is much easier than attracting new customers [23], home-appliance retailers should focus on cross sell rather than customer acquisition to boost sales.

In addition to this intensified competition, the infrequency of purchase events of durables, due to their highticket price and long lifetimes, magnifies the importance of cross-selling. As consumers are only in the market for short periods to spend substantial amounts, marketing managers are very interested in identifying which durable to offer to which customer at what time. Given low switching costs, home-appliance retailers should target customers with tailored offers. After all, customers irritated by unsuitable offers might easily churn.

Despite the clear managerial relevance of cross sell for the home-appliances industry, this paper is the first to build a cross-sell model for home-appliances. We empirically test how such a cross-sell model could benefit from exploiting the sequential information imbedded in customer's home-appliance acquisition sequence. After all, the acquisition process of consumer durables is a sequence of infrequent usually planned purchase events. Past literature on durables exploits this sequential feature in two ways.

Firstly, priority-pattern research reveals most customers acquire durables in a common order. Although this priority-pattern could provide cross-sell predictions, to date, most research is descriptive. This paper adds a predictive perspective to increase managerial relevance.

Secondly, literature on durable adoption, replacement and additional-set acquisition exploits the acquisition sequence to reveal precise timing between purchase events (‘sequential duration’). Estimating the time to durablegood acquisition is vital as purchase events occur infrequently and the shopping-time window may be short [7]. From a cross-sell perspective, these duration models do not only indicate what a customer will buy but also when. An important limitation of previous work is its focus on either first-acquisitions, replacements or additional set acquisitions. This approach is incomplete for cross-sell predictions. Therefore, we are the first to simultaneously consider customer's duration to first-acquisition as well as to a repeated-acquisition event; replacement or additionalset acquisition with separate model estimates.

Clearly, both the order and duration information of the home-appliance acquisition sequence can support cross-sell lead generation. On the one hand, Paas and Molenaar [41] advise future research should combine priority-pattern analysis with predictions on the precise timing of purchases. On the other hand, Haldar and Rao [27] suggest that a timing model could be extended to study the order of purchases. This paper is the first attempt to exploit both order and duration information for cross-sell. As a consequence, we bridge the gap between priority-pattern research and research on duration between durable-good acquisitions to improve the prediction of the product group the customer might acquire his next durable from, i.e. a Next-Product-to-Buy (NPTB) model. By enriching the NPTB model with order and duration information, we alleviate two disadvantages of the NPTB model. Firstly, unlike prioritypattern analysis, the NPTB models disregard the logical acquisition sequence and might not be able to generate leads extending a customer's current acquisition sequence [41]. Secondly, NPTB models only predict what a customer will buy next, irrespective of when this next purchase event might happen [34]. By including an estimate of the customer's probability to make a firstacquisition or repeated acquisition event during the next period in the NPTB model, we ensure that the NPTB predictions will be highly relevant in the near future.

The objective of this paper is two-fold. Firstly, we strive to build the best possible NPTB model to generate cross-sell leads. Which product category will the customer buy from next? Secondly, we aim to empirically investigate how enriching the NPTB model with order and/or duration estimates might enhance its predictive accuracy. Therefore, we evaluate four multinomial-choice models incorporating: 1) general covariates, 2) general covariates and sequential order, 3) general covariates and sequential duration, and 4) general covariates, sequential order and duration.

The remaining parts of this paper are structured as follows. Section 2 gives an overview of past prioritypattern and durable duration research and discusses our contributions. Section 3 reviews the methods applied. Section 4 sketches how we apply the methodology to build an NPTB model for a major home-appliances retailer. Subsequently, Section 5 presents the results and discusses the best NPTB model. We wind up this paper by summarizing its main conclusions, pointing to some limitations and by suggesting issues for further research.

## 2. Background

2.1. Time to describe the succession of purchase events: priority-pattern research

Several authors applied the ‘time’ feature of the acquisition sequence to discover a typical order of acquisition, i.e. a priority pattern. Typical acquisition patterns have been found for durable goods, as well as for financial services. Given the existence of such priority pattern and the household's position in it, one can predict what product the household will acquire next.

The rationale behind the existence of typical acquisition sequences is threefold. Firstly, logical successions stem from complementary goods [22]; e.g. a VCR is bought after a television set is acquired. These successions might predict which complementary product a household is likely to buy next, but are of limited use for cross-sell predictions. Secondly, typical sequential acquisition also results from households maximizing their utility over time [33]. A common acquisition order implies that households share similar utility structures [17]. In the presence of finite resources, the household is forced to prioritize her needs over time. Entirely like Maslov's pyramid of needs, households are expected to satisfy more basic needs (like washing machine) before more advanced needs (like surround system). Thirdly, typical acquisition orders follow from needs becoming salient as households transit through different life-cycle stages [39]. The utilitymaximization and life-cycle argument both give rise to successions of non-complementary goods. For instance, Paas [40] discovered that households generally acquire cookers before vacuum cleaners. Moreover, they buy washing machines last. This offers companies substantial opportunities to cross-sell. Furthermore, priority-pattern based cross-sell leads have the advantage over discretechoice leads [34] to be logical extensions of the customer's acquisition sequence.

Previous studies testify to the existence of a unique priority pattern of durables and this for both homogeneous (i.e. products fulfilling similar purposes) and heterogeneous (i.e. products different in nature) sets of products. Deviations of a customer's acquisition sequence from the priority pattern might stem from variations in socio-demographic (life-cycle [36,52]) and economic (income [16,37,52]) and psychological (values [16] and interests [52]) profile. Given knowledge of future prices, consumer incomes, budget constraints [28], customers' value system [16] and the utility function, one could predict the order in which consumers will acquire durables in the future.

Past research demonstrates the existence of a priority pattern for durable acquisition and describes its influential factors. However, priority pattern analysis can only support cross-sell activities if the consumer's next acquisition is predicted accurately. Besides the predictive forecasting test by Mayo and Qualls [36], we are the first authors to exploit this logical succession to predict which durable the customer will buy next (cross-sell). This is rather surprising as previous work in the area of financial services [32,35,41] proved the predictive value of priority-pattern information for cross-selling.

Analogous to previous work [32,41], we prefer probabilistic over deterministic priority-pattern analysis.

In the ideal case of deterministic behavior, consumers always acquire durables lower in the priority pattern before durables positioned higher in the pattern. There is a single acquisition pattern. Probabilistic priority-pattern analysis abandons this idea of a single priority pattern and instead assigns probabilities to acquisition patterns.

In contrast to past literature modeling durableacquisition patterns as a hierarchical process (cf. Guttman-, Rash or Mokken scales and latent-trait analysis) [16,17,33,37,41,52], we do not restrict the acquisition pattern to be hierarchical. That is, we do not assume customers to exactly follow the order of the ‘typical acquisition sequence (cf. cumulative scaling: owning product j implies possessing all products lower in the hierarchy). Instead, we allow for dependencies of any order. Methodologically, we apply Markov and Markov for Discrimination (see Section 3) to model logical successions of purchases of home appliances in product categories. Hence, we assume hierarchies among sets of products (e.g. entertainment appliances) rather than among individual products (e.g. VCRs) [22].

Finally, most authors derive the priority pattern from cross-sectional (except [36]) reported ownership. Inferring acquisition patterns from cross-sectional data raises questions about the validity of cross-sectional data for time-series prediction. Moreover, reported ownership data might induce recall biases. We are the first authors to investigate typical acquisition orders for household durables relying on observed longitudinal purchase scanner data. Data mining techniques are employed on a data warehouse to reveal typical acquisition patterns with the aim to exploit this extracted knowledge to support cross-sell lead generation [51].

## 2.2. Time as duration

Apart from exploiting the ‘time’ between successive acquisition events for inferring a priority pattern, research investigated the time between durable acquisitions to describe the factors influencing this time or/and to predict the time interval. Knowledge of the purchase timing decision is essential in understanding the dynamics of purchase behavior [29] as well as for timing marketing actions [26]. For durables, estimating the time to acquisition is vital as purchase events happen at infrequent rates and the time window during which the customer is actually shopping may be short [7]. The literature on timing between durable acquisition events overlaps with the three components representing total sales for durables: first-time purchases, replacements and additional-set acquisitions. Literature on aggregate diffusion models is not reviewed. Our objective is to develop a disaggregate choice model taking into account the customer's time pressure to buy from a product category c. This time pressure is approximated by estimating the customer's expected duration to a firsttime acquisition or repeated acquisition in the product category.

There is a remarkable dearth of disaggregate models on time to first acquisition of durables. Yet, Haldar and Rao [27] use panel data to predict the timing of first purchases for durables by applying a duration model with time-varying covariates. Just like Haldar and Rao [27], we strive to estimate the duration to firstacquisition events with the intention to identify (segments of) customers who are most likely to acquire a durable good for the first time. Given that households are utility maximizers with limited budgets at any time [27], our duration models account for effects of exceptional large expenditures in other product groups. We extend Haldar and Rao's [27] discovered cross-category dependency beyond prior ownership of other durables to general cross-category purchase history. We are the first authors to coin the concept of typical inter firstacquisition durations. Yet, the recognition of life-cycle specific needs seems to suggest such typical durations between the first-acquisition events for durables. Finally, our scanner data as compared to Haldar and Rao's panel data provides data on specific timings of purchase.

Past research on replacement has been substantial due to its commercial relevance. Due to high penetration levels (even up to 100% for many appliances in Belgium [20]), replacements account for current sales of most durable goods [7,24]. As durables age, the consumer is faced with decision to repair, to replace or to dispose of the durable [46]. The longevity of durables allows customers to postpone this decision. Yet, many customers replace their durables long before the old unit wears out [7,24]. Hence, the timing of the replacement decision differs across customers varying in demographic (e.g. lifecycle), economic (e.g. income) [4,26,8,11] and attitudinal/interest profiles [8,26]. Also product characteristics like brand styling and image [8,9] significantly influence the replacement timing. Moreover, the effects of household and product characteristics vary across durables [11].

The timing of the replacement decision is essential to enable tailored marketing offers targeted to the right customer at the right time in their replacement cycle. Surprisingly, only two studies [11,26] assess the model's ability to accurately make targeting predictions. Bayus and Mehta [11] developed a finite mixture segmentation model to target durable replacement segments on the basis of household characteristics and product ages.

Our study also aims to predict replacement timing to target replacement customers. We contribute to the extant replacement literature in the following ways. Firstly, previous research overlooked the potential effect of customer's purchase history on his replacement behavior. The availability of scanner data allows us to alleviate this limitation. Secondly, this paper is the first paper investigating replacement behavior utilizing longitudinal observed purchase behavior as stored in a data warehouse. The majority of previous research relied on cross-sectional data sincerely impeding the validity of longitudinal predictions. In addition, most researchers approximated the replacement duration by the reported replacement date. In contrast, scanner data stores the exact replacement timing. Thirdly, unlike most previous work, we account for time-varying covariates to influence the replacement duration. Fourthly, we employ a non-parametric baseline hazard $\lambda _ { 0 }$ fully defined by the data. The latter excludes the possibility of misspecifying the baseline-hazard distribution as opposed to previous papers adopting a parametric (e.g. Weibull) baseline hazard (see Section 3).

Besides replacements and first acquisitions, multipleunit adoptions are a major component of sales for many durable product categories [53]. Despite this managerial importance, to our knowledge, literature modeling the time to additional-unit acquisition on individual level is absent.

Unlike aggregate diffusion predicting total sales of a durable as a function of first purchases, replacements and multiple-unit sales [53], previous literature on consumerdurable duration either focuses on first-acquisitions, replacements or additional set acquisitions. For predicting which durable a customer will buy, this approach is suboptimal [27]. After all, we would like to target the customer with the most appropriate offer, be it a first acquisition, a replacement or additional-set acquisition. This paper is the first to simultaneously consider customer's duration to first acquisition as well as to a repeated-acquisition event; replacement or additional-set acquisition. Unfortunately, the available scanner data do not enable us to discriminate between replacements and additional set acquisition. Note we are the first authors to model durations to durable acquisitions relying on scanner data. This entails advantages like observed longitudinal exact durations, many observations and the availability of detailed purchase history. Finally, our study makes duration predictions for the full product range of a home-appliance retailer rather than for a small set of durables like in previous work (cf. panel data). After all, we intend to identify customers likely to buy any durable the retailer sells.

## 3. Methodology

## 3.1. Introduction

The paper's objective is the prediction of the product category in which the customer will acquire his next home appliance. Fig. 1 presents the study design. We model the ‘order’ of the acquisition sequence by Markov and Markov for Discrimination (Section 3.2). The duration to first-time/repeated acquisition is modeled by an extended-Cox model (Section 3.3). The NPTB model incorporates the estimates from the Markov/Markov for Discrimination and extended-Cox model in a multinomial-choice model: logit, hev or probit (Section 3.4). Different NPTB models are compared on their predictive value (Section 3.5).

## 3.2. Time as order

## 3.2.1. Markov

This section is based on Berchtold and Raftery [13]. We model the succession of durable-acquisition events as successive observations of a discrete-time random variable $X _ { t }$ taking on values from the finite set $N { = \{ 1 , . . . , m \} }$ . In this paper, $X _ { t }$ refers to the product group a customer acquires a product from at the tth acquisition event. Given nine product groups, $X _ { t }$ takes on values from $N { = } \{ 1 , 2 , . . . , 9 \}$ Our goal is to describe the value taken by $X _ { t }$ as a function of the values taken by k previous observations of this same variable (i.e. Markov chain). For instance, if k= 1, we model the product group a customer buys from at acquisition event t as a function of the previous durableacquisition at t−1. We will estimate different kth order Markov models. The transition probabilities are:

$$
\begin{array}{l} P (X _ {t} = i _ {0} | X _ {0} = i _ {t}, \ldots , X _ {t - 1} = i _ {1}) \\ \qquad = P (X _ {t} = i _ {0} | X _ {t - k} = i _ {k}, \ldots , X _ {t - 1} = i _ {1}) \\ \qquad = q _ {i _ {k} i _ {0}} (t). \end{array}\tag{1}
$$

where $i _ { t } , . . . , i _ { 0 } \in \{ 1 , . . . , m \}$ . We assume the transition probability $q _ { i _ { k } i _ { 0 } } ( t )$ to be time-invariant: $q _ { i _ { k } i _ { 0 } } .$ The result is a homogeneous Markov chain. Each possible combination of $k$ successive observations of the random variable X is a state. The number of states is equal to $m ^ { k }$ and given (m − 1) independent probabilities in each row of transition matrix $R ,$ the total number of independent parameters is $m ^ { k } \left( m - 1 \right)$ ). We refer to [44] for previous applications of Markov models for cross-selling.

## 3.2.2. Using Markov for Discrimination

An interesting application of Markov is Markov for Discrimination [18]. For any probabilistic model of sequences the probability of a sequence with length $L$ is:

$$
\begin{array}{l} P (x) = P (x _ {L}, x _ {L - 1}, \ldots , x _ {1}) \\ = P (x _ {L} | x _ {L - 1}, \ldots , x _ {1}) P (x _ {L - 1}) | x _ {L - 2}, \ldots , x _ {1}) \ldots P (x _ {1}) \end{array}\tag{2}
$$

The probability of each symbol $x _ { l }$ depends only on the value of the $k$ preceding symbols $x _ { L - k } ,$ , not on the entire previous sequence, e.g. for a first-order Markov model:

$$
\begin{array}{l} P (x) = P (x _ {L} | x _ {L - 1}) P (x _ {L - 1} | x _ {L - 2})... P (x _ {2} | x _ {1}) P (x _ {1}) \\ \qquad = P (x _ {1}) \prod_ {i = 2} ^ {L} q _ {x _ {i - 1} x _ {i}} \end{array}\tag{3}
$$

Suppose we wish to discriminate between customers' durable-acquisition sequences depending on how typical they are for a given population. We adopt the idea of a Markov process as a sequence-generating system. Furthermore, we assume that the sequences in each population are generated by a population-specific Markov process. As such, we build for each population a separate Markov model indicating the likelihood of a sequence to originate from the given population. Starting from these population-specific Markov transition matrices we calculate the log-odds ratio of 1) the odds to observe sequence x given it originates from population + versus 2) the odds to observe sequence x given it belongs to population −:

![](/api/attachments/NG8HHDW7/fulltext/images/2cb233d518f22d90045dae07634a8f17ad58de1c925f7e63bd7e6736783c3c21.jpg)  
Fig. 1. Study design.

$$
\begin{array}{l} S (x) = \log \frac {P (x | \text { population } +)}{P (x | \text { population } -)} \\ = \sum_ {i = 1} ^ {L} \log \frac {q _ {x _ {i - 1} x _ {i}} ^ {+}}{q _ {x _ {i - 1} x _ {i}} ^ {-}} \\ = \sum_ {i = 1} ^ {L} \beta_ {x _ {i - 1} x _ {i}} \end{array}\tag{4}
$$

In Eq. (4), $\beta _ { x _ { i } - 1 x i }$ are the log-likelihood ratios of corresponding transition probabilities. S(x) could be normalized by dividing by the length of the sequence.

Let's set out an example. Suppose we want to discriminate between a durable-acquisition sequence stemming from a customer who will buy a refrigerator next, e.g. product category 1 (population +) and the acquisition sequence of a customer who will buy next from the other product categories 2 or 3 (population −). We build a Markov model using the acquisition sequences for customers who will buy a refrigerator next, resulting in transition matrix $R +$ . Analogously we build a Markov model using the acquisition sequences of customers who will not acquire a refrigerator next, delivering transition matrix $R ^ { - }$ . Will a customer with acquisition history $1 \to 3 \to 2 \to 2$ buy in product category 1 next (i.e. fifth purchase event)? Therefore, we insert the appropriate transition probabilities $\boldsymbol { q } _ { 1 3 } ^ { + } , \boldsymbol { q } _ { 3 2 } ^ { + } \boldsymbol { q } _ { 2 2 } ^ { + }$ and $\bar { q _ { 1 3 } } , q _ { 3 2 } ^ { - } , q _ { 2 2 } ^ { - }$ from the hypothetical transition matrices $R +$ and $R ^ { - } \left( \mathrm { E q . } \left( 5 \right) \right)$ into Eq. (4). The odds to observe the acquisition history $1 \to 3 \to 2 \to 2$ given that the sequence originates from the population of customers who will acquire a durable in product category 1 next, is 0.8909 times smaller than the odds that the sequence stems from the population of customers who will not acquire their next durable in product category 1 (Eq. (6)). Hence, this customer is not likely to purchase next from product category 1.

$$
\mathrm{R} ^ {+} = \begin{array}{c} \mathrm{X} _ {\mathrm{t} - 1} \\ 1 \\ 2 \\ 3 \end{array} \left[ \begin{array}{c c c} 0. 3 0 & 0. 6 0 & \boxed {0. 1 0} \\ 0. 4 0 & \boxed {0. 4 5} & 0. 1 5 \\ 0. 2 0 & \boxed {0. 1 0} & 0. 7 0 \end{array} \right] \quad \mathrm{R} ^ {+} = \begin{array}{c} \mathrm{X} _ {\mathrm{t} - 1} \\ 1 \\ 2 \\ 3 \end{array} \left[ \begin{array}{c c c} 0. 0 5 & 0. 7 0 & \boxed {0. 2 5} \\ 0. 2 0 & \boxed {0. 3 5} & 0. 4 5 \\ 0. 1 0 & \boxed {0. 4 0} & 0. 5 0 \end{array} \right]\tag{5}
$$

$$
\begin{array}{r l}S (1 \rightarrow 3 \rightarrow 2 \rightarrow 2)&= \log \frac {0 . 1 0}{0 . 2 5} + \log \frac {0 . 1 0}{0 . 4 0} + \log \frac {0 . 4 5}{0 . 3 5}\\&= - 0. 8 9 0 9\end{array}\tag{6}
$$

## 3.3. Time as Duration: an extended-Cox model

We model the duration T to repeated purchase and the duration to first-time acquisition by an extended-Cox model including non-time varying as well as timevarying covariates [31,50,54]. We prefer to model the duration as a stochastic quantity rather than to define the acquisition process as a stochastic process (e.g. Wiener or renewal process [24]). After all, the acquisition of consumer durables does not resemble a renewal process like that of replacements of electronic components (e.g. light bulbs).

We define the failure time T as the length of time t (duration) until either a first-acquisition event or a repeated-acquisition event occurs. A hazard model assumes this duration is a random variable with density $f ( t )$ and cumulative distribution $F ( t )$ . The survivor function S(t), 1−F(t), indicates the probability that the first-acquisition or repeated-acquisition event has not yet occurred by some time t. The hazard rate or instantaneous failure rate $\lambda ( t )$ is the likelihood the first-acquisition event or repeated-acquisition event occurs at a specific time t given that it has not occurred previously: $\lambda ( t ) { = } f ( t ) /$ $[ 1 - F ( t ) ]$ . The baseline hazard $\lambda _ { 0 }$ reflects the underlying hazard for customers with all covariates $Z _ { 1 } , . . . , Z _ { p }$ equal to zero. The hazard rate for customer i is some multiplication of the baseline hazard $\lambda _ { 0 }$ and the customer's set of covariates $Z _ { i } \mathrm { : }$

$$
\lambda_ {i} (t, Z _ {i}) = \lambda_ {0} (t) e ^ {\left(\beta_ {1} z _ {1 i} + \dots + \beta_ {p} z _ {p i}\right)}\tag{7}
$$

The semi-parametric Cox proportional hazards model defines the baseline hazard by the data (i.e. nonparametric). The betas are assumed to be exponentially distributed (i.e. parametric). Under the proportional hazards assumption the ratio of the hazards does not vary over time t. We extend the Cox proportional hazards model to include time-varying covariates as well: an extended-Cox model. Given the $\beta$ estimates we derive the predicted survival for a customer i with one fixed covariate $Z _ { i }$ and one time-varying covariate $\{ Z _ { i } ( t ) ,$ $t \in [ 0 , X _ { i } ] \}$ by:

$$
\hat {S} _ {i} (t) = \left[ \hat {S} _ {0} (t) \right] ^ {e ^ {(\beta_ {1} z _ {i 1} + \beta_ {2} z _ {i 2} (t))}}\tag{8}
$$

## 3.4. Predicting the durable acquisition sequence: multinomial-discrete choice modeling

We aim to predict what product category the customer will purchase his next durable from. As the application involves more than two discrete alternatives (see Section 4), we rely on multinomial-discrete choice modeling [12] for the NPTB model. The random utility function $U _ { i j }$ of individual i for choice j belonging to choice set $C _ { n }$ with $j { > } 2$ (cf. multinomial) is decomposed into a deterministic and stochastic component:

$$
U _ {i j} = \beta^ {\prime} x _ {i j} + \xi_ {i j}\tag{9}
$$

where x is a matrix of observed attributes which might be choice (e.g. price of product) or individual specific (e.g. age of customer), β is a vector of unobserved marginal utilities (parameters) and $\varepsilon _ { i }$ is an unobserved random error term (i.e. disturbance term or stochastic component). Different assumptions on the error term of the random utility function $U _ { i j }$ of individual i for choice j, give rise to different classes of models. The MultiNomial Logit (MNL) model is the most restrictive model assuming all disturbances $\xi _ { i j }$ are independently and identically distributed (i.i.d). The probability of choosing an alternative j among $n _ { i }$ choices for individual i can be written:

$$
P _ {i} (j) = \frac {e ^ {(x _ {i j} ^ {\prime} \beta)}}{\sum_ {k \in C} e ^ {(x _ {i k} ^ {\prime} \beta)}}\tag{10}
$$

In this paper, we compare this standard MNL with more flexible discrete-choice formulations like the heteroscedastic-extreme-value (hev, independent and non-identical error terms) and probit models (correlated and non-identical error terms). We prefer the probit model to a nested-logit model, as it determines independent from an a priori specified hierarchy (cf. nested logit), where similarity between alternatives occurs.

## 3.5. Predictive model evaluation: the weighted PCC

In the absence of a specific cross-selling objective (cf. selling more of specific products/classes), we evaluate the NPTB model in terms of its ability to correctly classify cases in all classes. Given this objective and the class imbalance problem (i.e. differences in class prior probabilities biasing predictions towards the dominant class), it is inappropriate to express the classification performance in terms of the average accuracy like the Percentage Correctly Classified (PCC), i.e. the total number of correctly classified relative to the total number of predicted [6]. The predictive evaluation of the models should therefore take the distribution of the multinomial dependent variable into consideration [38]. Firstly, we adapt the PCC so that models receive a greater reward for correctly predicting cases of smaller classes than correctly classifying cases in bigger classes. Each class $c \ ( c { \in } C )$ of the dependent variable has a strict positive weight $w _ { c } \left( \mathrm { E q . } \left( 1 1 \right) \right)$ , with $f _ { c }$ referring to the relative frequency of the class on the dependent variable. The class-specific weights sum to one, $\textstyle \sum _ { c = 1 } ^ { C } w _ { c } = 1$ . Given the weights, the weighted PCC is (Eq. (12)):

$$
w _ {c} = \frac {1 - f _ {c}}{\sum_ {1} ^ {C} (1 - f _ {c})}\tag{11}
$$

$$
w \mathrm{PCC} = \frac {\sum_ {c = 1} ^ {C} w \mathrm{PCC} _ {c}}{C}\tag{12}
$$

with $w \mathrm { P C C } _ { c } { = } w _ { c } { \mathrm { * P C C } } _ { c } .$ The weighted PCC favors a model with a smaller PCC but with a greater number of correctly classified on smaller classes, to a model having a higher PCC due to predicting most cases to over represented classes. Similarly, the weights $w _ { c }$ and hence wPCC could be tailored to maximize cross-selling performance for specific product classes. We penalize models predicting several alternatives (cf. ties on maximum probability) by equally dividing the 100% classified over all alternatives predicted. Secondly, we benchmark the model's performance to the proportional chance criterion $( C _ { \mathrm { p r o } } )$ rather than the maximum chance criterion $( C _ { \mathrm { m a x } } )$ [38]:

$$
C _ {\mathrm{pro}} = \sum_ {1} ^ {C} f _ {c} ^ {2}\tag{13}
$$

## 4. A home-appliances application

## 4.1. Data

The methodological framework (cf. supra Fig. 1) is applied to a database of a major Belgian home-appliances specialist multiple. The analyses are conducted on scanner data for over one million customers making purchases from a very broad and deep product assortment. Our data sample excludes companies and selects all customers having at least two previous purchase events (cf. cross-buying behavior needed to build NPTB model, minimum store loyalty, comparing different order Markov) and maximum $I 6$ purchase events (cf. exclude outliers, median length of 2 plus 3 times $\sigma { = } 4 . 8 8 )$ . The NPTB model predicts for these selected customers from which product category they will acquire an appliance at their last purchase event (as stored in the data warehouse). We randomly assigned 37,276 customers to the estimation sample and 37,110 customers to the hold-out sample. This allows us to test the predictive performance of the NPTB model on data not used for estimating the model.

Several theoretical as well as practical arguments justify our decision of choice modeling at the productcategory level rather than at the product level. Theoretically, we rely on the idea of cross-category decisionmaking [3,15,48,50]. The latter may originate from need satisfaction under constraints, needs satisfied separately (cross-category consideration set) or jointly (product bundles) by sets of products [37,48] or ambiguous or conflicting goals under non-hierarchical information processing [45]. Practical considerations also favor product-category analysis. Imagine the estimation of a multinomial-logit analysis on the 704 product families as defined by the home-appliances retailer. This level of detail clearly exceeds the capabilities of the logit, hev or probit model. Inevitably, a multinomial-choice model at the product level could only model the choice between a limited set of products, preferably those in customer's consideration set. Similarly, to avoid explosion of the state space, abstraction of the choice-search space is essential for Markov analysis too.

## 4.2. Definition of the product categories

We divide the home-appliances into product categories based on 1) the underlying needs satisfied [15,30] and 2) the product-sales distribution. Firstly, each product category contains a set of items, each of which is a close substitute relative to a consumer's consumption utility [48]. Secondly, the categorization depends on the proportion of total sales the product category accounts for. To obtain good predictions for each product category, we avoid under or overrepresented categories. Class imbalance challenges classifiers like MNL designed to optimize an overall convergence measure without taking into account the prior class distribution [6,19,38]. This tends to result in ignoring the small classes while concentrating on classifying the large ones accurately. Due to underrepresentation, we dropped the personal computer product category, the environmental product family (e.g. airconditioner) and the external care family (e.g. solarium). We defined nine product categories satisfying four needs: cleaning [10,37], communication, entertainment [10,30,37] and cooking [37]. Accessories like VHS cassette, remote controls, … are excluded as they account for small expenses and research only indicates a priority pattern for bigger appliances (Table 1).

## 5. Results

Firstly, we strive to build the best possible NPTB model to generate cross-sell leads for the home-appliance retailer. Which product category will the customer buy from next? Secondly, we aim to empirically investigate how enriching the NPTB model with order and/or duration estimates might enhance its predictive accuracy. Therefore, we evaluate four multinomial-choice models on their predictive merits:

Table 1  
Product categories

<table><tr><td></td><td>Product category</td><td>Need</td><td>Total sales %</td></tr><tr><td>1</td><td>Washing/Drying: washing machine, dryer, dishwasher</td><td>Cleaning clothes and dishes</td><td>11</td></tr><tr><td>2</td><td>House Cleaning: vacuum cleaner, scrubbing brush, carpet cleaner</td><td>Cleaning house</td><td>11</td></tr><tr><td>3</td><td>Mobiles: mobile phones, telephone, fax, answering machine</td><td>Communication</td><td>16</td></tr><tr><td>4</td><td>VCR, DVD: VCR, DVD, projector</td><td>Entertainment: audio + visual (luxury)</td><td>7</td></tr><tr><td>5</td><td>TV</td><td>Entertainment: visual</td><td>13</td></tr><tr><td>6</td><td>Audio: hi-fi, equalizer, amplifier</td><td>Entertainment: audio</td><td>11</td></tr><tr><td>7</td><td>Food Preparation: toaster, food processor, coffee maker</td><td>Cooking: preparation of food</td><td>9</td></tr><tr><td>8</td><td>Cooking: refrigerator, freezer, range</td><td>Cooking: non portable</td><td>11</td></tr><tr><td>9</td><td>Cooking Small: microwave oven, deep fryer, oven</td><td>Cooking: portable</td><td>11</td></tr></table>

1) Null model: Multinomial-choice model containing the best general covariates.

2) Null model enriched with sequential-order information: Multinomial-choice model containing the best sequential-order estimates (Markov, Markov for Discrimination or dummies) in addition to the covariates of the NULL model.

3) Null model enriched with sequential-duration information: Multinomial-choice model with NULL covariates and enriched with survival estimates (surv or survdiff) for either a first-acquisition or repeated acquisition event depending on customer's past acquisition behavior in the product group.

4) Null model with sequential-order and sequentialduration information: Multinomial-choice model with general covariates from NULL model, order estimates and duration estimates.

## 5.1. Null model

## 5.1.1. Variable operationalization

Before adding sequential order and timing information, we build a basic choice model containing covariates on (Table 2): 1) monetary value, 2) depth and width of purchase behavior, number of home-appliances acquired at the retailer, 3) socio-demographical information, 4) brand loyalty, 5) price sensitivity, 6) number of home-appliances returned, 7) dominant mode of payment, 8) experience of a special life-event. Hence, besides socio-demographical information we mainly include purchase-behavior information. The selection of these eight blocks of covariates is based on past literature and availability and quality of the data in the data warehouse.

Independent variables for null model <sub>abl</sub>e <sup>2</sup>

<table><tr><td>Info Type</td><td>NAME</td><td>I</td><td>I*PC</td><td>Description</td><td>Block</td></tr><tr><td rowspan="4">Amount spent</td><td>monetarylormonetarypc</td><td>X</td><td>X</td><td>Total amount spent over all product categories including t-1 / the length of relationship.Same as monetarylor but by product category.</td><td rowspan="4">Block1</td></tr><tr><td>maximum amount</td><td>X</td><td></td><td>Maximum total amount spent on one purchase event.</td></tr><tr><td>minimum amount</td><td>X</td><td></td><td>Minimum total amount spent on one purchase event.</td></tr><tr><td>average amount</td><td>X</td><td></td><td>Total amount spent over all product categories including t-1 / number of purchase events.</td></tr><tr><td rowspan="3">IntensityWidthDepth</td><td>productnumber</td><td>X</td><td></td><td>Total number of appliances bought.</td><td rowspan="8">Block2</td></tr><tr><td>productnumberpc</td><td></td><td>X</td><td>Total number of appliances by product category.</td></tr><tr><td>diffproductdiffproductpc</td><td>X</td><td>X</td><td>Total number of different appliances bought.Total number of different appliances bought per product category.</td></tr><tr><td rowspan="5">Number acquired</td><td>productnumberloravgproductnumber</td><td>XX</td><td></td><td>Total number of appliances bought / lor.Total number of appliances bought/number of purchase events.</td></tr><tr><td>diffproductloravgdiffproduct</td><td>XX</td><td></td><td>Total number of different appliances bought / lor.Average number of different appliances bought on one purchase event.</td></tr><tr><td>avgproductnumberpcavgdiffproductpc</td><td></td><td>XX</td><td>Average number of appliances bought in product category at one purchase event.Average number of different appliances bought in product category at one purchase event.</td></tr><tr><td>maxdiffprodmaxprod</td><td>XX</td><td></td><td>Maximum number of different appliances bought at one purchase event.Maximum number of appliances bought at one purchase event.</td></tr><tr><td>maxdiffpc</td><td>X</td><td></td><td>Maximum number of different product categories purchased from at one purchase event.</td></tr><tr><td rowspan="5">Socio-demographics</td><td>language dummy</td><td>X</td><td></td><td>If language=1 (Dutch) then dummy_lang=&#x27;1&#x27; else dummy_lang=&#x27;0&#x27;.</td><td rowspan="5">Block3</td></tr><tr><td>urbanisation degree</td><td>X</td><td></td><td>Value between 1 and 100 expressing the degree of urbanisation.</td></tr><tr><td>gender</td><td>X</td><td></td><td>Dummy_fem=1 if female, dummy_man=1 if man, dummy_fam=1 if family (man and wife). If missing, all dumies are 0.</td></tr><tr><td>dwelling type</td><td>X</td><td></td><td>Dummy_appart=1 if apartment, dummy_house=1 if house, both dummies are zero if missing.</td></tr><tr><td>region</td><td>X</td><td></td><td>Dummy_Flanders=1 if Flanders, dummy_Wallonia=1 if Wallonia. Both dummies are zero if Brussels(cf. the three districts in Belgium).</td></tr><tr><td rowspan="2">Brand loyalty</td><td>general brand loyalty</td><td>X</td><td></td><td>Maximum number of appliances purchased from one brand. Dummy_brandloyalty1=1 if maximum is one.Dummy_brandloyalty2 = 1 if maximum is 2. Both dummies are zero for maximum at least 3.</td><td rowspan="2">Block4</td></tr><tr><td>loyal_PHILS, ...,loyal_WHLPL</td><td>X</td><td></td><td>Number of appliances purchased from Philips, Nokia, etc. Eight brands are selected having at least three percent of the customers who purchased at least two appliances from the same brand: Philips, Nokia,Sony, Samsung, Siemens, Panasonic, Miele and Whirlpool.</td></tr></table>

Table 2 (continued)

<table><tr><td>Info Type</td><td>NAME</td><td>I</td><td>I*PC</td><td>Description</td><td>Block</td></tr><tr><td rowspan="3">Brand loyalty</td><td>rloyal_PHILS, ..., rloyal_WHLPL</td><td>X</td><td></td><td>Number of Philips appliances purchased / total number of appliances acquired.</td><td rowspan="3">Block4</td></tr><tr><td>nbrdiffbrand</td><td>X</td><td></td><td>Total number of different brands bought.</td></tr><tr><td>rnbrdiffbrand</td><td>X</td><td></td><td>Total number of different brands bought / total number of appliances acquired.</td></tr><tr><td rowspan="9">Price and Promotion Sensitivity</td><td>nbrbelowq1, nbrq1q2,nbrq2q3,nbrq3p 90, nbrabovep90</td><td>X</td><td></td><td>Total number of products bought at price level below first quartile q1, total number of products bought atprice level between q1 and median price q2, ...</td><td rowspan="9">Block5</td></tr><tr><td>rnbrbelowq1,..., rnbrabovep90</td><td>X</td><td></td><td>Total number of products bought at price level below first quartile q1 (product category and year specific) divided by total number of products, ...</td></tr><tr><td>nbrbelowq1pc1, ..., nbrabovep90pc1</td><td></td><td>X</td><td>Same as nbrbelowq1, nbrbetq1q2, ... but product-category specific.</td></tr><tr><td>rnbrbelowq1pc1,..., rnbrabovep90pc1</td><td></td><td>X</td><td>Total number of products bought in product category at price level below q1 / total number of products purchased in product category, ...</td></tr><tr><td>promocount</td><td>X</td><td></td><td>Number of products purchased within promotion.</td></tr><tr><td>rpromocount</td><td>X</td><td></td><td>Number of products purchased within promotion / total number of appliances acquired.</td></tr><tr><td>dummy_promo0, dummy_promo2to6</td><td>X</td><td></td><td>Dummy_promo0=1 if at least one product purchased in promotion, dummy_promo2to6=1 if between 2 and 6 products, if more than six products both dummies are zero.</td></tr><tr><td>dummy_nbrlowestpr</td><td>X</td><td></td><td>If dummy_nbrlowestpr=1 then customer asked at least once for lowest-price guarantee.</td></tr><tr><td>dummy_sales</td><td>X</td><td></td><td>Dummy_sales=1 if at least one product bought during sales period (price reduction).</td></tr><tr><td rowspan="3">Number of returns</td><td>nbrreturns</td><td rowspan="2">X</td><td></td><td>Number of products returned (so purchased and returned).</td><td rowspan="3">Block6</td></tr><tr><td>rnbrreturns</td><td></td><td>Number of products returned (so purchased and returned) / total number of products bought.</td></tr><tr><td>dummy_return0, dummy_return1, dummy_return2</td><td>X</td><td></td><td>Dummy_return0=1 if no products returned, dummy_return1=1 if one product returned, dummy_return2=1 if 2 products returned, all dummies are zero if customer did return more than 2 products. Dummies created because there are outliers on nbrreturns.</td></tr><tr><td>Payment</td><td>perc_pay1</td><td>X</td><td></td><td>Percentage of payments of type 1 (cash) over all payments of known payment type.</td><td>Block7</td></tr><tr><td>Life-event</td><td>dummy_lifeevent</td><td>X</td><td></td><td>Flags 1 if customer bought &gt;=2 different products (cf.q3 for maxdiffprod) at one purchase event and for an amount&gt;=543 euro (median for maxamount). Special life-event.</td><td>Block8</td></tr></table>

In the NPTB model of [34], current product ownership (block 2) is the most important predictor followed by monetary value (block 1) and demographics (block 3). Moreover, most previous work on durable acquisition includes demographical information. We also include variables on brand loyalty (block 4) as [9] discovered that brand loyalty differs across different appliances. The life-event covariate (block 8) approximates whether the customer acquired some major homeappliances, potentially due to transit to a new life-cycle phase [36]. The marketing information is limited to instore promotions (block 5) as the retailer's marketing communication is limited to above-the-line communication. Secondly, regrettably as past research revealed its relevance [16], we neither have information on values, opinions nor on interests of the customers.

Table 2 provides an overview of the variables created as well as their operationalization. I refers to an individualspecific variable and is default represented by J − 1 (J is number of alternatives) columns in the NPTB model. I <sup>⁎</sup> PC indicates an individual and product-category specific variable and is default represented as one column in the NPTB model.

Within block 1, the maximum amount variable is a proxy for the customer's financial capacity (cf. income [4,8,11,16,26,37,52]) or a psychological upper-spending limit at the retailer. The minimum amount spent indicates whether the customer purchased only small appliances so far or whether also bigger appliances were acquired.

In block 3, urbanization [32] refers to the average degree of urbanization of the neighborhoods belonging to the postal code of the customer's residence. The dwelling-type variable [33] is inferred from delivery-athome information. If missing, we set both dummy\_apart and dummy\_house to zero. The quality of this variable is probably low as for many customers the dwelling-type information is lacking.

Concerning the general brand loyalty (block 4), 25% of the customers in the estimation sample acquired exactly two appliances from the same brand, whereas 68% never purchased several appliances from the same brand (similar in the hold-out sample). Philips (25%),

Nokia (13%) and Sony (8%) had the biggest share of customers who purchased at least two products from a single brand.

Block 5 refers to promotion sensitivity across product categories [3] as well as within a product category. We calculated per product category and per purchase year the quartiles on price per unit. The promotion variable includes promotions of different type like price, quantity or extra gadget promotions. Dummy\_nbrlowestpr refers to the policy of the retailer to guarantee the lowest price for all appliances.

## 5.1.2. Variable selection for null model

From the independent variables in Table 2 we make a selection of variables by selecting:

• The best set of 1, 2 or 3 variables within each block with at least three variables assessing the wPCC of estimating a MNL model including these variables on the estimation sample (e.g. 5 <sup>⁎</sup> 4/2 MNLs for selecting best 2 variables from block 1).

• The best set of 5 or 6 variables across variables selected in step 1 completed by the remaining variables not used in step 1 (e.g. block 7 and 8 for best subset of 2).

Selecting first the best 3 covariates followed by selecting the best 5 covariates yields the highest wPCC on the estimation sample (Table 3; wPCCe = 0.1884). The selected variables are monetarypc (block 1), diffprodpc and avgdiffprodpc (block 2), nbrq1q2pc and rnbrq1q2pc (block 5).

## 5.2. Selecting the best operationalization of the sequential-order information

The acquisition sequences used as input for the models (Markov, Markov for Discrimination and dummy representation) indicate from which product category the customer subsequently acquired home appliances. To ensure robust estimation of the transition probabilities (cf. too few observations for a given state), we reduce simultaneous cross-category purchases to the product category accounting for the biggest amount spent.

Table 3  
wPCCe for selected NULL variables

<table><tr><td>Step 1\Step2</td><td>5</td><td>6</td></tr><tr><td>1</td><td>0.1876</td><td>0.1862</td></tr><tr><td>2</td><td>0.1875</td><td>0.1876</td></tr><tr><td>3</td><td>0.1884</td><td>0.1880</td></tr></table>

## 5.2.1. Markov

From the 1st/2nd order Markov transition matrix, we retrieve the nine transition probabilities indicating the customer's probability to acquire the next durable from one of the nine product categories given his acquisition sequence. These nine transition probabilities are incorporated as a single product-category covariate in the MNL model.

## 5.2.2. Standardized Markov for Discrimination

For each customer we estimate the likelihood of his acquisition-history sequence assuming the next acquisition will be from product category $1 , 2 , . . . , 9$ versus the likelihood under the condition of not purchasing next from product category 1, 2, …, 9. Therefore, we assess the predictive performance of a standardized Markov for Discrimination model. We separate customers who will acquire a home appliance next from a given product category from those who will not. On these respective subsamples, we estimate 18 first-order (cf. minimum acquisition-history sequence length is two) Markov transition matrices. We apply the transition probabilities from these 18 matrices to the acquisition history from the customers in the estimation sample. This results in nine log-odds statistics per customer, which we include as the only product-category covariate in the MNL model.

## 5.2.3. Dummies

The dummy representation includes the purchase acquisition sequences as 15 dummies (cf. maximum length of acquisition history). Dummy 1 flags to one for the product category the customer purchases a product from one purchase event ago t−1, and so on.

## 5.2.4. Select operationalization

We select the best operationalization of the sequentialorder information as follows. We compare the predictive performance on the estimation model of estimating three MNL models incorporating the Markov transition probabilities, the log-odds statistics or the dummies respectively. Table 4a reveals that the highest wPCC is achieved by representing the order between the acquisition events by the nine log-odds derived from the Markov for Discrimination model.

## 5.3. Selecting the best operationalization for the sequential-timing information

We incorporate a ‘time-pressure’ covariate in the NPTB model indicating how close in time a customer is to a first-time or repeated-acquisition event in each product category. We opted for a ‘quarter’ as duration unit. We estimate for each customer the probability of acquiring the next home-appliance from a particular product category in the quarter following the last but one acquisition event t− 1.

Table 4  
Model comparison

<table><tr><td colspan="2">a: Sequential order</td></tr><tr><td>Model</td><td>wPCCe</td></tr><tr><td>Markov 1</td><td>13.53</td></tr><tr><td>Markov 2</td><td>16.93</td></tr><tr><td>Markov for Discrimination</td><td>18.76</td></tr><tr><td>Dummy</td><td>16.16</td></tr></table>

b: Sequential duration

<table><tr><td>Model</td><td>wPCCe</td></tr><tr><td>Surv</td><td>0.1841</td></tr><tr><td>Suvdiff</td><td>0.1969</td></tr><tr><td>Surv and Survdiff</td><td>0.1962</td></tr></table>

c: Sequential order and duration in NPTB model

<table><tr><td>Model</td><td>wPCCe</td><td>wPCCh</td></tr><tr><td>NULL</td><td>0.1884</td><td>0.1853</td></tr><tr><td>NULL+ORDER</td><td>0.1923</td><td>0.1869</td></tr><tr><td>NULL+DURATION</td><td>0.1984</td><td>0.1987</td></tr><tr><td>NULL+ORDER+DURATION</td><td>0.1956</td><td>0.1931</td></tr></table>

d: Alternative variable operationalization

<table><tr><td>Model</td><td>wPCCe</td><td>wPCCh</td></tr><tr><td>MNL</td><td>0.1991</td><td>0.1994</td></tr><tr><td>HEV</td><td>0.1732</td><td>0.1714</td></tr><tr><td>PROBIT</td><td>0.1593</td><td>0.1563</td></tr></table>

## 5.3.1. Duration to first-acquisition events

Duration is the time in quarters since the start of the customer's relationship to the first acquisition event in the product category. A customer ‘survives’ the time pressure as long as he does not make a first purchase within a particular product category at the retailer. To obtain estimates of the time to a firstacquisition event in a product group for surviving customers requires the estimation of nine extended-Cox models on customers from the estimation sample who experienced a first-acquisition event in the category. Four groups of time-varying covariates are included; cumulative number of previous purchase events, recency, inter-first purchase time and a budget constraint, as well as the socio-demographics from the null model (Table 2, block 3) as non-time varying covariates. From each product-category extended-Cox model, we select the covariates significant at α = 0.10 level and re-estimate the model.

## 5.3.2. Duration to repeated-acquisition events

We fit nine extended-Cox models using customers from the estimation sample who are repeated buyers for the respective category. ‘Duration’ is the time between the previous acquisition event and the repeated-purchase event (t − 1 for the application). Customers with several repeated-purchase events in a given product category appear several times in the estimation dataset. ‘Surviving the time-pressure’ means not having experienced the ${ 1 } \mathrm { s t } , . . . ,$ nth repeated-purchase event in the category. As time-varying covariates we included recency, a budget constraint and repair information in the respective product category as well as in other categories. As non-time varying covariates we incorporate socio-demographics (Table 2, block 3), the number of previous purchase events in the product category, the brand<sup>2</sup> of the previous home-appliance acquired and two quality proxies. The latter indicate whether at least one of the appliances purchased at the previous purchase event had a price below the first/above the third price-quartile; product-category and year specific. From each product-category extended-Cox model, we select the covariates significant at $\alpha { = } 0 . 1 0$ and re-estimate the model.

## 5.3.3. Select operationalization

We applied the final extended-Cox models for first/ repeated purchase events in a product group on customers in the estimation and hold-out sample without/with a first/repeated acquisition in the product group, respectively. Given the customer's covariate path at t − 1 (advantage to average replacement cycles for duration prediction), the survdiff variable expresses the probability of a first/repeated purchase event in the product group in the quarter following the last purchase event (t − 1). It is calculated by subtracting the expected survival estimate at t − 1 (surv variable) from the expected survival at the next quarter. Table 4b represents the predictive performance on the estimation sample of estimating three MNL models respectively incorporating the surv variable, the survdiff variable or both.

## 5.4. Assessing the predictive performance of sequential-order and sequential-duration information for the NPTB model

Using a multinomial-logit formulation, we compared four NPTB models as illustrated in Table 4c. The highest wPCCe is observed for a NULL model enriched with sequential-duration information. The higher predictive value of sequential-duration information emphasizes the predictive power of duration as compared to order information.

Furthermore, for this NULL+DURATION model, we empirically assessed that we could improve the predictive performance by allowing for J betas instead of just one for the monetary-value covariate (+0.007 percentage points, Table 4d).<sup>3</sup> No further improvements were observed by allowing for heteroscedastic or correlated error-terms (HEV or Probit).

The final best NPTB model is a MNL model comprising monetarypc1–monetarypc9, diffprodpc, avgdiffprodpc, nbrq1q2pc, rnbrq1q2pc enriched with duration information expressing the customer's time-pressure to make a first-or repeated-acquisition event for a product category. Its performance amounts to wPCCe=0.1991 and wPCCh=0.1994 (hold-out) and is 1.41 percentage points higher than that of a stand-alone NULL model. Although the predictive power of the best NPTB model might seem small, please consider the complexity of the problem as shown in Table 5. The diagonal reveals the number of correctly predicted observations. The inferred PCC statistics per product-category are independent of prior class probabilities [42]. They illustrate that our model has a high hit rate in product categories 3 (highest prior probability), 6, 7 and 8. The off-diagonal cells indicate misclassifications, which might have asymmetric costs as pointed out by [1]. The last but one row reports the percentage difference between the percentage predicted and the actual percentage of customers purchasing next in a certain category. For instance, the model predicts too few people (−1.76%) purchasing next from product category 2. The predictive performance of the NPTB model could be improved considerably by optimizing towards particular cells of the confusion matrix to support the retailer's specific strategic questions [43]. Note, however, that even the current NPTB model $( w \mathrm { P C C e } = 1 9 . 9 4 \% )$ substantially improves upon the default expected response level $( C _ { \mathrm { p r o } } { = } 1 2 . 6 3 \% )$ . This results in obvious beneficial financial effects.

## 5.5. Managerial implications of the best NPTB model

How can our NPTB model support the homeappliance retailer's cross-sell strategies? Who should be targeted by which durable offer and when? We fixed the ‘when’ dimension to the next quarter as all duration models provide customer's hazard to make a firstacquisition or repeated-acquisition event in the product category during the next quarter.

Confusion matrix of final NPTB model on hold-out sample <sub>a</sub>b<sup>le5</sup>

<table><tr><td rowspan="2">Actual</td><td colspan="9">Classified</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>1</td><td>459</td><td>386</td><td>548</td><td>301</td><td>432</td><td>384</td><td>340</td><td>456</td><td>306</td></tr><tr><td>2</td><td>400</td><td>490</td><td>647</td><td>282</td><td>449</td><td>361</td><td>668</td><td>339</td><td>354</td></tr><tr><td>3</td><td>496</td><td>519</td><td>3212</td><td>592</td><td>592</td><td>781</td><td>659</td><td>403</td><td>386</td></tr><tr><td>4</td><td>402</td><td>367</td><td>989</td><td>555</td><td>636</td><td>666</td><td>453</td><td>365</td><td>332</td></tr><tr><td>5</td><td>472</td><td>379</td><td>742</td><td>536</td><td>616</td><td>533</td><td>377</td><td>373</td><td>306</td></tr><tr><td>6</td><td>286</td><td>278</td><td>617</td><td>365</td><td>341</td><td>788</td><td>398</td><td>212</td><td>226</td></tr><tr><td>7</td><td>159</td><td>345</td><td>469</td><td>162</td><td>178</td><td>249</td><td>114</td><td>159</td><td>250</td></tr><tr><td>8</td><td>394</td><td>252</td><td>406</td><td>207</td><td>352</td><td>266</td><td>128</td><td>554</td><td>243</td></tr><tr><td>9</td><td>297</td><td>320</td><td>513</td><td>241</td><td>313</td><td>312</td><td>554</td><td>294</td><td>344</td></tr><tr><td></td><td>3365</td><td>3336</td><td>8143</td><td>3241</td><td>3909</td><td>4340</td><td>4874</td><td>3155</td><td>2747</td></tr><tr><td>Predicted %</td><td>9.0676</td><td>8.9895</td><td>21.9429</td><td>8.7335</td><td>10.5335</td><td>11.6950</td><td>13.1339</td><td>8.5018</td><td>7.4023</td></tr><tr><td>Actual %</td><td>9.7332</td><td>10.7518</td><td>20.5874</td><td>12.8402</td><td>11.6788</td><td>9.4611</td><td>8.3859</td><td>7.9709</td><td>8.5907</td></tr><tr><td>Difference %</td><td>-0.6656</td><td>-1.7623</td><td>1.3555</td><td>-4.1067</td><td>-1.1453</td><td>2.2339</td><td>4.7480</td><td>0.5309</td><td>-1.1884</td></tr><tr><td>PCC</td><td>12.7076</td><td>12.2807</td><td>42.0419</td><td>11.6474</td><td>14.2132</td><td>22.4437</td><td>36.6645</td><td>18.7289</td><td>10.7905</td></tr></table>

Table 6  
Final NPTB model (<sup>⁎</sup> α< =0.10, <sup>⁎⁎</sup> α< =0.05, <sup>⁎⁎⁎</sup> α< =0.001)

<table><tr><td>Variable</td><td>Estimate</td><td>t value</td></tr><tr><td>monetarypc1</td><td>-0.0011</td><td>-1.06</td></tr><tr><td>monetarypc2</td><td>0.0012</td><td>0.64</td></tr><tr><td>monetarypc3</td><td>0.0091</td><td>6.82***</td></tr><tr><td>monetarypc4</td><td>0.0009</td><td>1.01</td></tr><tr><td>monetarypc5</td><td>-0.0001</td><td>-0.15</td></tr><tr><td>monetarypc6</td><td>-0.0008</td><td>-0.74</td></tr><tr><td>monetarypc7</td><td>0.0059</td><td>2.55**</td></tr><tr><td>monetarypc8</td><td>-0.0005</td><td>-0.52</td></tr><tr><td>monetarypc9</td><td>-0.0333</td><td>-3.56***</td></tr><tr><td>diffprodpc</td><td>0.2418</td><td>19.28***</td></tr><tr><td>avgdiffprodpc</td><td>-0.0450</td><td>-2.21**</td></tr><tr><td>nbrq1q2pc</td><td>-0.0436</td><td>-4.59***</td></tr><tr><td>rnbrq1q2pc</td><td>-0.0122</td><td>-0.58</td></tr><tr><td>survdiff</td><td>7.0650</td><td>39.09***</td></tr><tr><td>Log likelihood</td><td>-78,964</td><td></td></tr></table>

Who should be targeted by which offer? From the estimates in Table 6, the home-appliance retailer should target customers with:

1) a high purchase depth in the product category (positive sign of estimate of diffprodpc, usage/experience/ learning effects),

2) a relatively small average number of different homeappliances purchased at one purchase event (negative sign of estimate of avgdiffprodpc, satisfied product-category need),

3) a limited total number of appliances acquired at price level between the first quartile and median price<sup>4</sup> (negative sign of estimate of nbrq1q2pc),

4) a relatively high average amount spent in pc = 3 (mobiles) per day of length-of-relationship (lor) with an offer for pc = 3 (positive sign of estimate of monetarypc3),

5) a relatively high average amount spent in pc = 7 (food preparation) per day of lor with an offer for pc = 7 (positive sign of estimate of monetarypc7),

6) a relatively small average amount spent in pc = 9 (cooking small, portable) per day of lor with an offer for pc = 9 (negative sign of estimate of monetarypc9).

Note that the NULL variable estimates only indicate who to target among repeated-acquisition customers for the product category. Luckily, we can rely on the duration estimates from the 9 <sup>⁎</sup> 2 extended-Cox models for first-acquisition and repeated-acquisition to gain additional insights. The home-appliances retailer should target customers with a high estimated time-pressure in the product category (i.e. positive sign of estimate of survdiff). More specifically, from the duration estimates<sup>5</sup> we infer that prospects for pc = 1 (washing/drying) are:

1) First-time acquisition customers:

• for which the deviation of his purchase recency in the house-cleaning, mobile, visual entertainment or audio category and the median inter-first acquisition time between pc = 1 and these respective categories is small,

• who purchased more recently from the housecleaning, mobile, VCR/DVD, visual entertainment category (recency),

• who purchased at least once from any product category except the audio category (purchased from other product categories),

• with a limited number of cumulative purchase events from the house-cleaning and visual entertainment category,

• who did not experience in the interval [t−1−quarter, t−1] a purchase event in another product category for which the total monetary amount exceeded a) the customer's personal year budget<sup>6</sup> and b) the median year budget of the customers in the estimation sample (budget constraint, [27]).

•who has a family and lives in a rather rural area.

2) Repeated-acquisition customers who:

• have at least two past purchase events in pc = 1

• did not experience a budget constraint [27] in the interval [previous acquisition in pc = 1, t − 1]

• have a rather high number of acquisition events from the cooking category (cumulative acquisition events other product category) but not too recent (recency),

• have not purchased from the mobile or VCR/DVD category in the interval [previous acquisition in pc = 1, t − 1] (recency),

• preferably have not purchased from the housecleaning and audio category in the period [previous acquisition in pc = 1, t − 1] (recency),

• had an appliance repaired in pc = 1 or another product category

• purchased at least one appliance at the previous acquisition event with a price below the first quartile<sup>7</sup> (rather cheap appliance, quality)

• purchased at the last acquisition event in pc = 1 an appliance from Miele (hazard is 162% of the hazard of customers who purchased other brand), Bauknecht or AEG (quality, brand-loyalty and replacement time).

Similar prospect profiles can be formulated for the other product categories. Clearly, the duration estimates provide marketing managers with additional and even more detailed targeting information than the NULL variable estimates. Managers should definitely not neglect how prospect characteristics seriously differ depending on whether the customer is new-to-theproduct-category or not. Furthermore, the significant effects of recency, the cumulative number of purchase events in other categories and the inter first-acquisition times testify to the presence of cross-category dependencies [14]. The duration results also reinforce the negative impact of budgetary constraints on the acquisition behavior [14,16,17,28,52]. Finally, brand managers could learn from the estimates on how the previously acquired brand affects the repeated-acquisition duration.

## 6. Conclusion

Even though cross-selling activities are of high value to managers of home-appliance retailers, this paper is the first to build a cross-sell model for home appliances. We aimed to build the best NPTB model solving the managerial research question: ‘Which product category will the customer buy from next?’.

The paper contributes to past research in various ways:

1. We provide the first cross-sell model for home appliances.

2. We are the first to exploit both order and duration information for cross-sell predictions. Consequently, we bridge the gap between priority-pattern research and research on duration between durable acquisitions.

3. We contribute to the priority-pattern literature by assessing the predictive rather than descriptive value of logical acquisition successions for cross-sell lead generation.

4. We contribute to the literature investigating the duration between acquisition events by simultaneously considering customer's duration to first-acquisition as well as to a repeated-acquisition event; replacement or additional-set acquisition.

The results favor a NPTB model including general covariates and duration information. The high predictive value of sequential-duration information emphasizes the predictive power of duration as compared to order information. Still further research is essential to corroborate our findings. Several causes might explain the smaller predictive value of the sequential ordering between acquisition events. Firstly, in contrast with previous research, we started from observed longitudinal acquisition data (scanner data) instead of cross-sectional reportedownership data or purchase intentions. This might indicate that observed data provide less evidence for the existence of a unique priority pattern. Secondly, the acquisition sequences used as input for the sequentialorder models might diverge from the actual acquisition sequence of the customer. The acquisition sequences as registered in the scanner data do not capture acquisitions of home appliances at competitors. Future work could collect such missing information by a survey and may use data-augmentation techniques to generalize the results to non-respondents. Thirdly, literature on priority patterns mainly found evidence for a unique acquisition pattern between high-priced appliances. Our selection of product categories also includes smaller home appliances like mobile phones (although we excluded accessories) besides these big-ticket appliances like television sets.

The final NPTB model is successfully supporting the identification of cross-sell leads. We are able to identify which customers to target by what offer. By including an estimate of the customer's probability to make a firstacquisition or repeated-acquisition event during the next period in the NPTB model, we ensure that the offer will be time-relevant (when). As a result, the best NPTB model's predictive performance is substantially better than the default model.

Several insights are gained. The general covariates once more stress the importance of past-purchase behavior [47] as compared to demographics. However, as all significant general covariates capture purchase history, they do not allow for identifying first-acquisition prospects. This is where the added value of the duration models comes in. Prospects' profiles sincerely differ depending on whether the customer is new to the category (first-acquisition) or not (repeated-acquisition). Future work should aim to disentangle replacements from additional-set acquisitions as their influential factors might vary. Furthermore, important cross-category dependencies are observed [14]. Typical inter firstacquisition durations do exist! Further research should therefore incorporate these. The duration results also reinforce the negative impact of budgetary constraints on the acquisition behavior [14,16,17,28,52]. Finally, strong brand effects are observed for the repeatedacquisition duration.

The retained NPTB model could support cross-sell decisions in various ways. In the same vein as customeroriented catalog segmentation [2], the home-appliances retailer could create nine versions of its leaflet with promotions for one of the nine product categories on the front page. Each target would receive a leaflet featuring special offers on their front page for the product category for which the NPTB model predicts the highest acquisition probability. Future research could increase external validity by generalizing our research findings to other industries. For instance, could cross-sell predictions in the financial-services industry benefit from enriching a NPTB model with order and duration information as embedded in the financial-services acquisition sequences?

## Acknowledgements

The authors would like to thank 1) the anonymous home-appliances retailer for providing the data, 2) Ghent University for funding the PhD project of Anita Prinzie (BOF Grantno. B00141), 3) the Flemish Research Fund (FWO Vlaanderen) for providing the funding for the computing equipment to complete this project (Grantno. G0055.01) and 4) the anonymous reviewers for their constructive remarks.

## References

[1] J.H. Ahn, K.J. Ezawa, Decision support for real-time telemarketing operations through Baeysian network learning, Decision Support Systems 2 (1) (1997) 17–27.

[2] A. Amari, Customer-oriented catalog segmentation: effective solution approaches, Decision Support Systems 42 (3) (2006) 1860–1871.

[3] R.L. Andrews, I.S. Currim, Identifying segments with identical choice behaviors across product categories: an intercategory logit mixture model, International Journal of Research in Marketing 19 (1) (2002) 65–79.

[4] G. Antonides, The Lifetime of a Durable Good, Kluwer Academic, Boston, 1990.

[5] ApplicanceMagazine.com, European Retail Sales Down in January, Feb. 7, 2006.

[6] R. Barandela, J.S. Sánchez, V. Garcia, E. Rangel, Strategies for learning in class imbalance problems, Pattern Recognition 36 (3) (2003) 849–851.

[7] B.L. Bayus, Accelerating the durable replacement cycle with marketing mix variables, Journal of Product Innovation Management 5 (3) (1988) 216–226.

[8] B.L. Bayus, The consumer durable replacement buyer, Journal of Marketing 55 (1991) 42–51.

[9] B.L. Bayus, Brand loyalty and marketing strategy: an application to home appliances, Marketing Science 11 (1) (1992) 21–38.

[10] B.L. Bayus, C.C. Carlstrom, Grouping durable goods, Applied Economics 22 (6) (1990) 759–773.

[11] B.L. Bayus, R. Mehta, A segmentation model for the targeted marketing of consumer durables, Journal of Marketing Research 32 (1995) 463–469.

[12] M. Ben-Akiva, S.R. Lerman, Discrete Choice Analysis: Theory and Application to Travel Demand, The MIT Press, Cambridge, 1985.

[13] A. Berchtold, A.E. Raftery, The mixture transition distribution model for high-order Markov chains and non-Gaussian time series, Statistical Science 17 (3) (2002) 328–356.

[14] P.K. Chintagunta, S. Haldar, Investigating purchasing timing behavior in two related product categories, Journal of Marketing Research 35 (1) (1998) 43–53.

[15] K.P. Corfman, Comparability and comparison levels used in choices among consumer products, Journal of Marketing Research 28 (3) (1991) 368–374.

[16] K.P. Corfman, D.R. Lehmann, S. Narayanan, Values, utility, and ownership: modeling the relationships for consumer durables, Journal of Retail 67 (2) (1991) 184–203.

[17] P.R. Dickson, R.F. Lusch, W.L. Wilkie, Consumer acquisition priorities for home appliances: a replication an re-evaluation, The Journal of Consumer Research 9 (4) (1983) 432–435.

[18] R. Durbin, S. Eddy, A. Krogh, G. Mitchison, Biological Sequence Analysis. Probabilistic Models of Proteins and Nucleic Acids, Cambridge University Press, UK, 1998.

[19] A. Estabrooks, T.H. Jo, N. Japkowicz, A multiple resampling method for learning from imbalanced data sets, Computational Intelligence 20 (1) (2004) 18–36.

[20] Euromonitor, Consumer Electronics in Belgium, www.gmid. euromonitor.com, Country Report 23 February 2005.

[21] Euromonitor, Domestic Electrical Appliances in Belgium, www. gmid.euromonitor.com, Country Report 12 April 2005.

[22] L.F. Feick, Latent class models for the analysis of behavioral hierarchies, Journal of Marketing Research 24 (2) (1987) 174–186.

[23] J. Felvey, Cross-selling by computer, Bank Marketing (1982) 25–27.

[24] V.P. Fernandez, Decisions to replace consumer durables goods: an econometric application of Wiener and renewal processes, The Review of Economics and Statistics 82 (3) (2000) 452-461.

[25] GfK, Klassieke Product Life Cycle ‘voldoet’ niet meer, Retail Trends (October 2005)

[26] R. Grewal, R. Metha, F. Kardes, The timing of repeat purchases of consumer durable goods: the role of functional bases of consumer attitudes, Journal of Marketing Research 41 (1) (2004) 101–115.

[27] S. Haldar, V.R. Rao, A micro-analytic threshold model for the timing of first purchases of durable goods, Applied Economics 30 (7) (1998) 959–974.

[28] J.R. Hauser, G.L. Urban, The value priority hypotheses for consumer budget plans, Journal of Consumer Research 12 (4) (1986) 446–462.

[29] D. Jain, N. Vilcassim, Investigating household purchase timing decisions: a conditional hazard function approach, Marketing Science 10 (1) (1991) 1–22.

[30] M.D. Johnson, Consumer choice strategies for comparing noncomparable alternatives, Journal of Consumer Research 11 (3) (1984) 741–753.

[31] J.D. Kalbfleish, R.L. Prentice, The Statistical Analysis of Failure Time Data, John Wiley and Sons, New York, 1980.

[32] W.A. Kamakura, S.N. Ramaswami, R.K. Srivastava, Applying latent trait analysis in the evaluation of prospects for cross-selling of financial services, International Journal of Research in Marketing 8 (4) (1991) 329–350.

[33] J.J. Kasulis, R.F. Lusch, E.F. Stafford, Consumer acquisition patterns for durable goods, Journal of Consumer Research 6 (1) (1979) 47–57.

[34] A. Knott, A. Hayes, S.A. Neslin, Next-Product-To-Buy models for cross-selling applications, Journal of Interactive Marketing 16 (3) (2002) 59–75.

[35] S.B. Li, B.H. Sun, R.T. Wilcox, Cross-selling sequentially ordered products: an application to consumer banking services, Journal of Marketing Research 42 (2) (2005) 233–239.

[36] M. Mayo, W. Qualls, Household durable goods acquisition behavior—a longitudinal study, Advances in Consumer Research 14 (1987) 463–467.

[37] J. McFall, Priority patterns and consumer behavior, Journal of Marketing 33 (October 1969) 50–55.

[38] D.G. Morrison, On the interpretation of discriminant analysis, Journal of Marketing Research 6 (1969) 156–163.

[39] P.E. Murphy, W.A. Staples, Modernized family-life cycle, Journal of Consumer Research 6 (1) (1979) 12–22.

[40] L.J. Paas, Mokken scaling characteristic sets and acquisition patterns of durable- and financial products, Journal of Economic Psychology 19 (3) (1998) 353–376.

[41] L.J. Paas, I.W. Molenaar, Analysis of acquisition patterns: a theoretical and empirical evaluation of alternative models, International Journal of Research in Marketing 22 (1) (2005) 87–100.

[42] R.C. Prati, G.E.A.P.A. Batista, M.C. Monard, Class imbalances versus class overlapping: an analysis of a learning system behavior, Lecture Notes in Computer Science 2972 (2004) 312–321.

[43] A. Prinzie, D. Van den Poel, Constrained optimization of datamining problems to improve model performance: a directmarketing application, Expert Systems with Applications 29 (3) (2005) 630–640.

[44] A. Prinzie, D. Van den Poel, Investigating purchasing-sequence patterns for financial services using Markov, MTD and MTDg models, European Journal of Operational Research 170 (3) (2006) 710–734.

[45] S. Ratneshwar, C. Pechmann, A.D. Shocker, Goal-derived categories and the antecedents of across-category consideration, Journal of Consumer Research 23 (3) (1996) 240–250.

[46] J.E. Raymond, T.R. Beard, D.M. Gropper, Modelling the consumer's Decision to replace durable goods: a hazard function approach, Applied Economics 25 (10) (1993) 1287–1292.

[47] P.E. Rossi, R.E. McCulloch, G.M. Allenby, The value of purchase history data in target marketing, Marketing Science 15 (4) (1996) 321–340.

[48] G.J. Russel, S. Ratneshwar, A.D. Shocker, D. Bell, A. Bodapati, A. Degeratu, L. Hildebrandt, N. Kim, S. Ramaswami, V.H. Shankar, Multiple-category decision-making: review and synthesis, Marketing Letters 10 (3) (1999) 319–332.

[49] P.B. Seetharaman, P.K. Chintagunta, The proportional hazard model for purchase timing: a comparison of alternative specifications, Journal of Business and Economic Statistics 21 (3) (2003) 368–382.

[50] P.B. Seetharaman, A. Ainsle, P.K. Chintagunta, Investigating household state dependence effects across categories, Journal of Marketing Research 36 (4) (1999) 488–500.

[51] M.J. Shaw, C. Subramaniam, G.W. Tan, M.E. Welge, Knowledge management and data mining for marketing, Decision Support Systems 31 (1) (2001) 127–137.

[52] G. Soutar, S. Cornish-Ward, Ownership patterns for durable goods and financial assets: a Rasch analysis, Applied Economics 29 (7) (1997) 903–911.

[53] P.R. Steffens, A model of multiple-unit ownership as a diffusion process, Technological Forecasting & Social Change 70 (2003) 901–917.

[54] T.M. Therneau, P.M. Grambsch, Modeling Survival Data: Extending the Cox Model, Springer, New York, 2000.

![](/api/attachments/NG8HHDW7/fulltext/images/9e1ebf93ead2f15c9d0b8c9d18605744c379688128192c688c48673033b9e575.jpg)

Anita Prinzie is a post doctoral researcher in Economics and Business Administration at Ghent University, Belgium. She received her master's degree in Marketing Analysis and Planning as well as her PhD from Ghent University, Belgium. Her PhD thesis investigates the use of sequence-analysis methods for CRM purposes (churn and cross-sell analysis).

![](/api/attachments/NG8HHDW7/fulltext/images/3e542a7430e6777a4d7c5972fa27cae5a2a97bb06c1fe18b0e2f6def5b172c96.jpg)

Dirk Van den Poel is associate professor of marketing at the Faculty of Economics and Business Administration of Ghent University, Belgium. He heads a competence center on analytical customer relationship management (aCRM). He received his degree of management/business engineer as well as his PhD from K. U.Leuven (Belgium). His main interest fields are the quantitative analysis of consumer behavior (CRM), data mining (genetic algorithms, neural

networks, random forests, random multinomial logit: RMNL), text mining, optimal marketing resource allocation (DIMAROPT), and operations research.

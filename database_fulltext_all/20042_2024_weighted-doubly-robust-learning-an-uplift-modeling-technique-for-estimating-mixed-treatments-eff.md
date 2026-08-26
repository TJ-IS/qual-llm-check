---
otero_id: 20042
otero_key: "DG2QCJE7"
title: "Weighted doubly robust learning: An uplift modeling technique for estimating mixed treatments' effect"
authors: "Baoqiang Zhan; Chao Liu; Yongli Li; Chong Wu"
year: "2024"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2023.114060"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Weighted doubly robust learning: An uplift modeling technique for estimating mixed treatments’ effect

![](/api/attachments/DG2QCJE7/fulltext/images/46ab4425d95acd35d8225b6edce90c6241494e92ac9df4b5ced785af5964f19a.jpg)

Baoqiang Zhan <sup>a,b</sup>, Chao Liu <sup>a,c</sup>, Yongli $\mathrm { L i } ^ { \mathrm { a , \ast } }$ <sup>\*</sup>, Chong Wu <sup>a</sup>

<sup>a</sup> School of Economics and Management, Harbin Institute of Technology, Harbin, China

<sup>b</sup> Department of Management and Marketing, The Hong Kong Polytechnic University, Hong Kong, China

<sup>c</sup> Department of Information Systems, City University of Hong Kong, Hong Kong, China

## A R T I C L E I N F O

Keywords: Weighted doubly robust learning Mixed treatments Uplift modeling Treatment attribution

## A B S T R A C T

Estimating the effect of mixed treatments is a crucial problem in causal inference. While previous studies have focused on econometric analysis, few have positioned the mixed treatment problem within the realm of causal machine learning, particularly in uplift modeling. This study proposes a novel uplift modeling technique called weighted doubly robust learning, which uses Shapley-value treatment attribution and doubly robust estimation to control for confounding among different treatments and estimate the pure effect for each treatment. Exper iments are conducted on both synthetic dataset and industrial dataset, The results show that our method out: performs most of the current uplift modeling approaches in responsive customer targeting and effective treatment attribution, achieving an area under uplift curve (AUUC) of 0.590 and a Qini-coefficient of 0.080. Our method not only contributes to advancing current causal machine learning methods, but also provides valuable insights for companies in business decision making.

## 1. Introduction

Uplift modeling has gained significant attention in online marketing [1]. With the prevalence of ecommerce, companies now have ample opportunities to enhance the sales of their products and services through campaigns like America’s Cyber Monday and China’s Double Eleven. Evaluating the effect of campaigns is crucial for companies, as it enables them to assess the effectiveness of their strategies and make informed decisions for future endeavors. Uplift modeling, as an inference method and a form of prescriptive analytics, enables the development of simu lation models based on historical data and facilitates targeting of cus tomers who are likely to respond positively to specific treatment [2]. Previous studies have examined the efficacy of uplift modeling in esti mating treatment effect [3]. However, the performance of uplift modeling is heavily influenced by the form of treatments, which can vary in terms of configurations and effects [4].

In today’s online market, there are three main forms of treatments: single treatment [5], mutually exclusive treatments [6], and (nonmutually exclusive) mixed treatments [7]. Single treatment refers to companies applying only one treatment to customers. Mutually exclu sive treatments involve companies using multiple treatments, (e.g., discounts, coupons, cashback, etc.), where these treatments are mutually exclusive and customers can only receive one treatment at a time. In more complex cases, mixed treatments occur when companies employ multiple treatments that are non-exclusively applied to cus tomers. This means that customers can receive different treatments simultaneously, resulting in doubled or tripled discounts on their purchases.

Previous studies in the literature have predominantly focused on the case of single treatments [8] and mutually exclusive treatments [9]. Even though there are a few studies concerning mixed treatments, most of them use econometric analysis [7,10]. At present, uplift modeling has emerged to estimate the effect of single treatments or mutually exclusive treatments in randomized controlled trials involving the entire customer base [2] while none of them have been applied to the mixed treatment problems. In practical marketing scenarios, companies often apply different promotions to customers during large-scale campaigns. The utilization of mixed treatments can bring multiple benefits, such as attracting new customers, reducing customer churn, and significantly increasing both sales and revenues. Following these promotions, com panies are keen to assess the specific impact of these treatments, espe cially how many customers make their response to the treatments? And which treatment contributes most?

This paper aims to address confounding issues among mixed treatments and estimate the net conditional average treatment effect (CATE) of each treatment. We begin by introducing treatment attribu tion based on Shapley value, which can effectively separate a treatment group and a control group for each specific treatment and isolate the confounding effects of other treatments. Next, we propose a machine learning approach called weighted doubly robust learning (WDRL) to estimate the CATE for each treatment. Using both synthetic data and industrial data for experiments, our study demonstrates that WDRL outperforms the commonly used uplift modeling techniques such as S learner, T-learner, X-learner, double machine learning (DML), and doubly robust learning (DRL) in terms of the area under the uplift curve (AUUC) and the Qini coefficient metrics.

Our study makes three following contributions. Firstly, unlike pre vious studies that primarily employ econometric analysis, we position the mixed treatment problem within the realm of causal machine learning and address it using a novel uplift modeling approach. Sec ondly, to overcome the challenges of confoundedness, we introduce the Shapley value for treatment attribution. This approach allows us to separate specific treatments from the confounding effects of other treatments, effectively eliminating confounding in mixed treatments and enabling unbiased CATE estimation and the most effective treat ment identification that support for decision making. Lastly, our research introduces WDRL, which integrates multiple DRL model trained on different groups, weighted by group size. This comprehensive approach facilitates in-depth training and CATE estimation. Given that mixed treatments prediction can be seen as a multi-label classification problem, our method calibrates the estimated bias of different groups and provide more accurate prediction on multi-treatment labels, which extends current multi-label classification research and contributes to the development of causal machine learning methods.

## 2. Related work and preliminary knowledges

This study first reviews mixed treatment research in different fields, and then introduces the relation between uplift modeling and CATE estimation. Finally, we provide preliminary introduction of different uplift models.

## 2.1. Research of mixed treatment assignment

In causal inference, treatment assignment plays a crucial role in shaping the design of causal experiments and influencing the accuracy of treatment effects estimation. While previous research has primarily focused on single treatment and mutually exclusive treatments, the issue of mixed treatments has received relatively less attention. This could be attributed to two reasons. Firstly, mixed treatments are less commonly encountered in real-world scenarios compared to single or mutually exclusive treatments. Secondly, estimating treatment effects for mixed treatments is a complex task that cannot be easily addressed using traditional methods. By conducting an extensive literature review, we have managed to identify relevant studies that shed light on mixed treatment assignments, as presented in Table 1.

Table 1  
Research in mixed treatment assignment.

<table><tr><td>Field</td><td>Terminology</td><td>Theory</td><td>Method</td><td>Treatment setting</td><td>Study focus</td><td>Literature</td></tr><tr><td rowspan="3">Clinical medicine</td><td rowspan="3">Multi-component treatment/ Combination therapy</td><td>Potential outcome framework</td><td>Generalized propensity score method</td><td>None / Drug / Mental therapy / Both</td><td rowspan="2">Estimating the treatment effect in multiple-treatment interventions on late-life depression. Evaluating the performance of propensity score methods when treatments have 2 or &gt;2 levels on pregnancy depression.</td><td>Feng et al. (2010) [12]</td></tr><tr><td>Potential outcome framework</td><td>Propensity score method</td><td>None / Drug A / Drug B / Both</td><td>Nian et al. (2019) [10]</td></tr><tr><td>Potential outcome framework</td><td>Probit/logit model</td><td>None / Product innovation / Process innovation / Both</td><td>Examining the effects of product and process innovation as well as both modes of innovation on firm&#x27;s propensity to export.</td><td>Becker and Egger (2013) [13]</td></tr><tr><td rowspan="3">Political governance</td><td rowspan="3">Policy mix</td><td>Potential outcome framework</td><td>Generalized propensity score method</td><td>Innovation vouchers / Advisory services / Both</td><td rowspan="2">Examining the effects of policy mix (combining innovation vouchers and advisory services) on firms&#x27; propensity to innovate. Evaluating the effects of policy mix between innovation policy and environmental policy on firms&#x27; adoption of global warning-related eco-innovations.</td><td>Caloffi et al. (2022) [14]</td></tr><tr><td>Potential outcome framework</td><td>Inverse probability weighting regression adjustment estimator</td><td>None / Innovation policy / Environmental policy / Both</td><td>Greco et al. (2022) [15]</td></tr><tr><td></td><td></td><td>Intervention 1 / Intervention 2 / Intervention Combination</td><td>Illustrating the simultaneous- treatment design theoretically and demonstrating how to evaluate the influence of different treatment. Evaluating the effects of four different treatments (with interference with each other) on mouthing behavior of retarded boy.</td><td>Kazdin and Hartmann (1978) [16]</td></tr><tr><td rowspan="2">Psychology and behaviors</td><td rowspan="2">Simultaneous treatment/ Multiple treatment interference</td><td>-</td><td>-</td><td rowspan="2">Intervention / Differential reinforcement / Visual Screening / Extinction</td><td rowspan="2">Using Monte Carlo simulation to estimate the average partial effects for multiple non-exclusive treatments</td><td rowspan="2">McGonigle et al. (1987) [17]</td></tr><tr><td>-</td><td>Experiment</td></tr><tr><td rowspan="2">Economics</td><td rowspan="2">Non-mutually exclusive treatment</td><td>-</td><td>Semiparametric method</td><td>Any combination of binary, discrete and continuous treatments</td><td rowspan="2">Providing a modeling analysis on the identification of average treatment effects.</td><td>Graham and Pinto (2022) [7]</td></tr><tr><td>Potential outcome framework</td><td>Mathematical modeling</td><td>Any combination of treatments</td><td>Newey and Stouli (2021) [18]</td></tr><tr><td rowspan="2">Advertising</td><td rowspan="2">Multi-touch attribution</td><td>Counterfactual framework</td><td>Logistic regression and smoothed probability estimation</td><td>Any combination of treatments from different ads channels</td><td>Attributing the advertising channel that contributes most to user conversion through estimating the effect of each ad.</td><td>Dalessandro et al. (2012) [19]</td></tr><tr><td>-</td><td>Causal recurrent network</td><td>Any combination of treatments from different ads channels</td><td>Building causal attention model for user-personalized multi-touch attribution.</td><td>Kumar et al. (2020) [20]</td></tr></table>

Table 1 demonstrates that mixed treatments are referred to variou synonymous terminologies across different fields. For instance, in clin ical medicine, it is often referred to as “combination therapy,” while in political governance, it is known as “policy mix.” In the fields of psy chology and behavior, it is termed “simultaneous treatment,” and in advertising, “multi-touch attribution” is more commonly used. Although there might be slight variations in definitions and application contexts across these fields, most studies adhere to Robin’s causal model [11] and utilize the potential outcome framework as their theoretical foundation. Additionally, econometric methods like generalized propensity score matching and logistic regression are frequently employed. However, the application of machine learning methods to explore causality between mixed treatments and outcomes has been limited, with the exception of studies in the advertising field. Given these observations, there is a need to develop a novel machine learning approach that can more accurately and appropriately estimate the effects of mixed treatments. This research aims to fill this gap by proposing a new method using machine learning to improve the estimation of mixed treatment effects.

## 2.2. Uplift modeling and CATE estimation

Uplift modeling is a methodology used to identify individuals who exhibit behavioral changes as a direct consequence of receiving a spe cific treatment [21]. These changes are commonly referred to as uplifts. In this context, the treatment assigned to customer $i ( i = 1 , \cdots , n )$ is represented as $T _ { i } \in \{ 0 , 1 \}$ }, and each customer has a non-zero probability $P ( T _ { i } )$ of being assigned to either the treatment or control group. When customer i receives a treatment, $T _ { i } = 1$ , otherwise $T _ { i } = 0 .$ . The outcome Y is denoted as the response of customer i to the treatment. Let $X _ { i } =$ $\left\{ X _ { i 1 } , X _ { i 2 } , \cdots X _ { i p } \right\}$ be a $p$ dimensional covariates of customer i, the uplift could be estimated as:

$$
U p l i f t (\boldsymbol {X}) = E \big [ Y _ {i} ^ {1} | \boldsymbol {X} _ {i}, T _ {i} = 1 \big ] - E \big [ Y _ {i} ^ {0} | \boldsymbol {X} _ {i}, T _ {i} = 0 \big ]\tag{1}
$$

The definition of uplift modeling aligns it as a specific instance of CATE modeling, which falls under the potential outcome framework, also known as the Neyman-Rubin causal model [11,22]. Within the potential outcome framework, three essential assumptions are proposed: ignorability, overlapping, and stable unit treatment values assumption. We discuss these assumptions in Section 3.1. The estimation of CATE under these three assumptions can be conducted as follows:

$$
\widehat {C A T E} (\boldsymbol {X}) = E \big [ Y _ {i} ^ {1} - Y _ {i} ^ {0} | \boldsymbol {X} _ {i} \big ]\tag{2}
$$

[23] has established the connection between uplift and CATE, as demonstrated in $\operatorname { E q } . \left( 3 \right)$ . Notably, CATE can be divided into three terms, with the first term being equivalent to uplift. Importantly, under the ignorability assumption, the second and third terms become null.

$$
\begin{array}{l} \widehat {C A T E} (\boldsymbol {X}) = E \left[ Y _ {i} ^ {1} - Y _ {i} ^ {0} | \boldsymbol {X} _ {i} \right] = E \left[ Y _ {i} ^ {1} | \boldsymbol {X} _ {i}, T _ {i} = 1 \right] P (T _ {i} \\ \quad = 1) + E \left[ Y _ {i} ^ {1} | \boldsymbol {X} _ {i}, T _ {i} = 0 \right] P (T _ {i} = 0) - E \left[ Y _ {i} ^ {0} | \boldsymbol {X} _ {i}, T _ {i} = 1 \right] P (T _ {i} \\ \quad = 1) - E \left[ Y _ {i} ^ {0} | \boldsymbol {X} _ {i}, T _ {i} = 0 \right] P (T _ {i} = 0) \\ \quad = \underbrace {E \left[ Y _ {i} ^ {1} | \boldsymbol {X} _ {i} , T _ {i} = 1 \right] - E \left[ Y _ {i} ^ {0} | \boldsymbol {X} _ {i} , T _ {i} = 0 \right]} _ {\text { observed }} + P (T _ {i} \\ \quad = 1) \left\{\underbrace {\left\{E \left[ Y _ {i} ^ {0} | \boldsymbol {X} _ {i} , T _ {i} = 0 \right] - E \left[ Y _ {i} ^ {0} | \boldsymbol {X} _ {i} , T _ {i} = 1 \right] \right.} _ {\text { observed }} \right\} + P (T _ {i} \\ \quad = 0) \left\{\underbrace {\left\{E \left[ Y _ {i} ^ {1} | \boldsymbol {X} _ {i} , T _ {i} = 0 \right] - E \left[ Y _ {i} ^ {1} | \boldsymbol {X} _ {i} , T _ {i} = 1 \right] \right.} _ {\text { observed }} \right\} \\ \end{array}\tag{3}
$$

While the derived relationship between uplift and CATE demon strates their equivalence in estimation, the uplift modeling process goes beyond CATE estimation by aiming to target customers who exhibit the maximum behavioral changes compared to control subgroups. Unlike solely estimating the effect of the received treatment, uplift modeling seeks to target individuals who are most responsive to the treatment and identify the most effective treatment [24], as shown in Fig. 1. This approach goes further than CATE estimation as it provides theoretical and practical support for business decision-making [25]. By focusing on maximizing behavioral changes, uplift modeling offers valuable insights and guidance for businesses to make informed decisions and optimize their strategies.

In the subsequent sections, we will introduce two additional objec tives of uplift modeling and present our proposed method for achieving these objectives. Before delving into these objectives, it is important to provide preliminary knowledge about various uplift modeling ap proaches. Here, we provide more specific details regarding the estima tion of CATE within these approaches since CATE estimation is considered the fundamental objective in uplift modeling.

## 2.3. CATE estimation using different approaches

Within the uplift modeling framework, several approaches have been incorporated for estimating CATE, including meta-algorithms, double machine learning and doubly robust learning. While these approaches are quite different, their overarching goals remain consistent: to maxi mize uplift and identify customers who are most responsive to the treatments.

## 2.3.1. Meta-algorithms

Meta-algorithm is an algorithmic framework that combines super vised learning or regression estimators $( \mathrm { i . e . }$ , base learners) in a specific manner while allowing the base learners to take any form $[ 2 6 , 2 7 ]$ . In the context of uplift modeling, three classical meta-algorithms are commonly introduced: S-learner, T-learner, and X-learner.

2.3.1.1. S-learner. S-learner is a straightforward uplift model that uti lizes a single base learner, which can be any type of supervised learning algorithm. S-learner estimates the CATE as follows.

$$
\widehat {C A T E} (X) = \frac {1}{n} \sum_ {i = 1} ^ {n} [ M (Y _ {i} | X _ {i}, T = 1) - M (Y _ {i} | X _ {i}, T = 0) ]\tag{4}
$$

where M denotes the model (i.e., base learner) adopted in S-learner.

2.3.1.2. T-learner. The S-learner’s ability may be limited in certain scenarios as it relies on a single model built on both the treatment and control groups. To enhance performance, the T-learner constructs two separate predictive models: one for the treatment group, denoted as $M _ { T } ,$ and another for the control group, denoted as $M _ { C }$ . The CATE estimation using T-learner can be expressed as:

$$
\widehat {C A T E} (\boldsymbol {X}) = \frac {1}{n} \sum_ {i = 1} ^ {n} \left[ M _ {T} \left(Y _ {i} \mid \boldsymbol {X} _ {i}\right) - M _ {c} \left(Y _ {i} \mid \boldsymbol {X} _ {i}\right) \right]\tag{5}
$$

here, $M _ { T } [ Y _ { i } | X _ { i } ]$ and $M _ { C } [ Y _ { i } | X _ { i } ]$ are two independent models on treatment group and control group separately. Note that the CATE is the average difference between the predictions of $M _ { T }$ and $M _ { c }$ . When there is an imbalance in the sample sizes between the treatment and control group, the predictive models $M _ { T }$ and $M _ { c }$ may lead to prediction errors. The direct subtraction of these two models raises concerns about the robustness of CATE estimation.

![](/api/attachments/DG2QCJE7/fulltext/images/a6ae1731319f0d1e016e877482fb42d9ba4b1868bdc88a2b126f4bb03b99fada.jpg)  
Fig. 1. Three objectives of uplift modeling.

2.3.1.3. X-Learner. To address the issue of sample imbalance, the $\mathrm { X } \mathrm { - }$ Learner method is developed to provide further improvements. Similar to the T-learner, the X-Learner also constructs two predictive models, $M _ { T }$ and $M _ { C } .$ . However, instead of directly estimating the CATE by subtract ing the two models, X-Learner utilizes them to compute the imputed treatment effects, $D ^ { 1 }$ and $D ^ { 0 } ,$ . The imputed treatment effects are calcu lated as follows:

$$
D _ {i} ^ {1} = Y _ {i} - M _ {C} [ Y _ {i} | \boldsymbol {X} _ {i} ]\tag{6}
$$

$$
D _ {i} ^ {0} = M _ {T} \left[ Y _ {i} \mid X _ {i} \right] - Y _ {i}\tag{7}
$$

the imputed treatment effects are the residuals between the observed outcome and the prediction of the respective models. Using the imputed treatment effects as the response variable, another two models called residual model $R M _ { T }$ and $R M _ { C }$ are built. The final CATE can be estimated by:

$$
\widehat {C A T E} (X) = \frac {1}{n} \sum_ {i = 1} ^ {n} \left\{g (X _ {i}) R M _ {C} \left(D _ {i} ^ {0} | X _ {i}\right) + [ 1 - g (X _ {i}) ] R M _ {c} \left(D _ {i} ^ {1} | X _ {i}\right) \right\}\tag{8}
$$

where $g \in [ 0 , 1 ]$ is a weight function, and [26] recommend using pro pensity score as the estimate of g. Note that the CATE here is estimated as the weighted average of the two residual models. It also makes sense to adjust the weight of g when the size of treatment group is overly large or small compared to the control group.

## 2.3.2. Double machine learning

Double machine learning (DML) was initially introduced by [28]. In contrast to previous meta-learners that assume treatment T is uncon founded with covariates X [29], DML acknowledges that X influences both the outcome Y and the treatment T, as depicted in Eqs. (9) and (10).

$$
Y _ {i} = \theta T _ {i} + g (\boldsymbol {X} _ {i}) + \varepsilon_ {i}\tag{9}
$$

$$
T _ {i} = m (X _ {i}) + \eta_ {i}\tag{10}
$$

In DML, X affect the outcome Y and the treatment T via the functions of $g ( X )$ and m(X). ε and η are the disturbances. Particularly, θ represents the CATE that we aim to infer. DML builds machine learning models for double stages, where the first stage is to partial the effect of X from T and the second stage is to estimate the debiased CATE. As illustrated in Eqs. (11) and (12), the first stage yields two residuals that are independent of X.

$$
\widetilde {Y} _ {i} = Y _ {i} - g (\boldsymbol {X} _ {i})\tag{11}
$$

$$
\widetilde {T} _ {i} = T _ {i} - m (X _ {i})\tag{12}
$$

In the second stage, a final regression model is built with $\widetilde { Y } _ { i }$ as the dependent variable, and $\widetilde { T } _ { i }$ as independent variable.

$$
\widetilde {Y} _ {i} = \theta \widetilde {T} _ {i} + \epsilon_ {i}\tag{13}
$$

The CATE could be estimated as follows.

$$
\widehat {C A T E} (\boldsymbol {X}) = \operatorname * {a r g m i n} _ {\theta} \sum_ {i = 1} ^ {n} \left[ \left(\widetilde {Y} _ {i} - \theta \widetilde {T} _ {i}\right) ^ {2} \right]\tag{14}
$$

## 2.3.3. Doubly robust learning

Doubly robust learning (DRL), proposed by [30,31], combines direct regression and inverse propensity scoring in two-stage framework. In the first stage, two predictive models are constructed to estimate the outcome and the treatment. This allows for the unbiased estimation of the potential outcomes for the treatment group $Y _ { 1 , i } ^ { D R }$ , and the control group, $Y _ { 0 , i } ^ { D R }$ , as demonstrated below:

$$
Y _ {1, i} ^ {D R} = \widehat {Y} _ {1, i} + \frac {T _ {i} (Y _ {1 , i} - \widehat {Y} _ {1 , i})}{\widehat {P r} (X _ {i})}\tag{15}
$$

$$
Y _ {0, i} ^ {D R} = \widehat {Y} _ {0, i} + \frac {\left(1 - T _ {i}\right) \left(Y _ {0 , i} - \widehat {Y} _ {0 , i}\right)}{1 - \widehat {P r} (X _ {i})}\tag{16}
$$

where ${ \widehat { P r } } ( X _ { i } )$ is the propensity score that could be predicted by any classification model. Let $\widehat { Y } _ { i } ^ { D R }$ be the subtraction of $\widehat { Y } _ { 0 , i }$ from $\widehat { Y } _ { 1 , i }$

$$
\widehat {Y} _ {i} ^ {D R} = Y _ {1, i} ^ {D R} - Y _ {0, i} ^ {D R}\tag{17}
$$

then in the second stage, the CATE could be estimated through a regression model M of $\widehat { Y } _ { i } ^ { D R }$ on $X _ { i } ,$ shown as follows.

$$
\widehat {C A T E} (\boldsymbol {X}) = \frac {1}{n} \sum_ {i = 1} ^ {n} M \left(\widehat {Y} _ {i} ^ {D R} | \boldsymbol {X} _ {i}\right)\tag{18}
$$

The above methods outline how to estimate the CATE for a single treatment. Similarly, these methods can be extended to handle the case of mutually exclusive treatments. This is achieved through a treatment joining method, where all treatments are merged into a binary set [4,32]. For example, $T _ { i } = 1$ indicates that customer i receives any treatment from the company, while $T _ { i } = 0$ represents that customer i receives no treatment. By comparing the outcomes of the entire treat ment group (with all treatments joined) against the control group, the CATE can be estimated.

However, this method is no longer suitable for situations with mixed treatments. In mixed-treatments scenarios, the treatments are not independently applied to customers, and the effects of different treat ments become confounded. Eq. (2) can only explain the partial effect of an individual treatment while the remaining effect may be present in the combination of other treatments, which cannot be directly estimated. Consequently, there is still a gap in existing literature regarding the CATE estimation for mixed treatments, particularly in addressing the issue of confoundedness.

## 3. Methods

In this section, we introduce our proposed methods, consisting of two parts: treatment attribution based on Shapley value and weighted doubly robust learning (WDRL). Additionally, the evaluation metrics of AUUC and Qini coefficient are introduced as well.

## 3.1. Assumptions

As we adopt the potential outcome framework to frame uplift modeling, we introduce three assumptions before estimating the CATE for mixed treatments.

Assumption 1. (Ignorability). The potential outcome couple is inde pendent of the treatment $T _ { i , \ast }$ when conditioning on the observed co variate variables $X _ { i }$ of customer i, i.e.,

$$
\left\{Y _ {i} ^ {0}, Y _ {i} ^ {1} \right\} \perp T _ {i} | X _ {i}\tag{19}
$$

Under Assumption 1, we immediately get:

$$
E \left[ Y _ {i} ^ {0} | \boldsymbol {X} _ {i}, T _ {i} = 0 \right] = E \left[ Y _ {i} ^ {0} | \boldsymbol {X} _ {i} \right]\tag{20}
$$

leading to:

$$
E \left[ Y _ {i} ^ {0} | \boldsymbol {X} _ {i}, T _ {i} = 0 \right] - E \left[ Y _ {i} ^ {0} | \boldsymbol {X} _ {i}, T _ {i} = 1 \right] = E \left[ Y _ {i} ^ {0} | \boldsymbol {X} _ {i} \right] - E \left[ Y _ {i} ^ {0} | \boldsymbol {X} _ {i} \right] = 0\tag{21}
$$

Assumption 2. (Overlapping). Any customer i has a non-zero proba bility of receiving treatment and control, i.e.,

$$
0 <   P (T _ {i} = 1 | X _ {i}) \langle 1\tag{22}
$$

Assumption 3. (Stable Unit Treatment Values Assumption). A cus tomer’s potential outcome is not affected by other customers treatment. In other words, treatment applied to one customer does not affect the outcome of other customers.

## 3.2. Treatment attribution based on Shapley value

Estimating the CATE of mixed treatments requires effectively dis entangling the different treatments and isolating their respective con founding effects. It is crucial to obtain distinct treatment and control groups for each treatment, ensuring the absence of confoundedness. To achieve this, we propose a novel method of treatment attribution based on Shapley value.

The Shapley value, originally developed within cooperative game theory, has been employed to assess the value of each player across various combinations of players in multiplayer cooperative games [33]. Building upon this concept, [34] extended the application of Shapley value to measure the relative importance of predictors in regression models by considering all combinations of predictors. [35] developed a unified framework based on Shapley value for feature attribution in deep learning networks, enhancing model interpretability. Similarly, [36] also proposes an axiomatic framework for advertisement attrition in specific, generalizing the use of Shapley value in digital marketing industry. In our study, the mixed treatments are likened to multiple players in cooperative games and multiple advertisements in online advertising. Consequently, we extend the application of Shapley value to treatment attribution.

Assume that there are b possible treatments. These treatments can be combined with each other to form a combination set, denoted as C. For a specific treatment $k \left( k = 1 , 2 , . . . . . b \right)$ the combination set can be expressed as $C = \{ 0 \cup S _ { - k } \cup W _ { k } \}$ . In the combination set, the subset O represents empty set, indicating that the customer receives null treat ment. $S _ { - k }$ represents the subsets of all possible combination treatments excluding treatment k. $W _ { k }$ denotes the subset of all possible combination treatments that include treatment k. In particular, the number of com bination treatments in $W _ { k }$ is given by $2 ^ { b - 1 }$

In general, for any given combination treatments w in $W _ { k }$ and for some combination s in $\{ \mathrm { O } \cup S _ { - k } \}$ , there exists a subtraction operation ⊝ such that $k = w \odot s .$ Here, the symbol ⊝ represents the subtraction of one combination treatments from another combination treatments. We assign w and s as the combination treatments applied to the treatment group and control group, respectively. Consequently, the treatment group and the control group will differ by only the specific treatment k. In other words, the discrepancy between the treatment group and the control group can be attributed to treatment k. By employing this approach, we can isolate the effect of treatment k by taking the differ ence between the outcomes of the treatment group and the control group. Fig. 2 provides an illustrative example of treatment attribution based on Shapley value.

In Fig. 2, it is evident that the assigned treatment combination w in the treatment group always includes one additional treatment compared to the assigned treatment combination s in the control group. This additional treatment k is the specific effect that we aim to infer. Let $\widehat { C A T E } _ { k , t } ( X )$ represents that the CATE of treatment k, where t represent the t-th element in set $W _ { k } .$ Let $P ( w _ { t } )$ indicate the probability of occur rence of the treatment combination $w _ { t } ,$ , the CATE of treatment k could be estimated as:

$$
\widehat {C A T E} _ {k} (\boldsymbol {X}) = \sum_ {t = 1} ^ {2 ^ {b - 1}} P (w _ {t}) \widehat {C A T E} _ {k, t} (\boldsymbol {X})\tag{23}
$$

where the $\widehat { C A T E } _ { k , t } ( X )$ is the CATE of the t-th combination treatments in set $W _ { k }$

## 3.3. Weighted doubly robust learning

In the presence of mixed treatments, traditional approaches such as S-Learner and T-Learner face challenges in estimating the CATE for each individual treatment due to confounding factors. Consequently, these approaches typically estimate the CATE of the overall treatments through a treatment joining method. However, by leveraging treatment attribution based on Shapley value, we successfully address the con founding issues among different treatments, enabling us to estimate both the overall CATE and the CATE of each respective treatment. In Algorithm 1, we propose a novel framework called weighted doubly robust learning, which incorporates a weighting structure upon doubly robust learning approach to enhance the estimation process.

Using the Shapley value-based treatment attribution approach, we can obtain $2 ^ { b - 1 }$ groups for each attributed treatment $k \in [ 1 , b ] .$ . Conse quently, a total of $b \bullet 2 ^ { b - 1 }$ groups can be obtained, considering all b treatments. Each group comprises a treatment subgroup and a control subgroup, which are assigned the combination treatments in $W _ { k }$ and S respectively.

We can summarize the algorithmic procedures of WDRL into three stages. In the first stage, two prediction models are built for each group to predict the outcome and the treatment, enabling the computation of $\widehat { \boldsymbol { Y } } ^ { D R }$ (estimated outcome) for the group. In the second stage, the $\widehat { \boldsymbol { Y } } ^ { D R }$ values from different groups are fed into a weighted layer to compute the weighted average $\widehat { Y } ^ { W D R }$ . In the third stage, a final regression model is constructed to estimate the overall treatment effect or the CATE of specific treatment. The three-stage structure of WDRL is depicted in Fig. 3. Using WDRL, we have flexibility in choosing which treatment’s effect to estimate. For example, we can estimate the CATE of a specific treatment k by performing a weighted average of the corresponding $2 ^ { b - 1 }$ groups. Alternatively, we can estimate the CATE of all treatments collectively by performing a weighted average across the entire set of b • $2 ^ { b - 1 }$ groups.

![](/api/attachments/DG2QCJE7/fulltext/images/458d303433a7f12e238553adde0ef042da23b78b0c101cb1435229dd34b64ec1.jpg)  
Fig. 2. An example of treatment attribution.

Algorithm 1. Weighted doubly robust learning.

## 3.4. Evaluation

AUUC and Qini coefficient are adopted as two evaluation metrics of uplift models. AUUC measures the area under the uplift curve [37] while the Qini coefficient quantifies the area between the Qini curve and the random targeting line [38]. Both curves plot the cumulative difference in revenue outcomes between the treatment and control groups across different quantiles (q) of customers ranked by the estimated CATE in descending order. Specifically, the Uplift curve(q) and Qini curve(q) are defined as:

$$
\text { Uplift   curve } (q) = \left(R _ {t} (q) - R _ {c} (q)\right)\tag{24}
$$

$$
\text { Qini   curve } (q) = \left(R _ {t} (q) - R _ {c} (q) \frac {N _ {t} (q)}{N _ {c} (q)}\right)\tag{25}
$$

where, $R _ { t } ( q )$ and $N _ { t } ( q )$ are the outcome and the number of customers in the treatment group when targeting the top q% customers, while $R _ { c } ( q )$ and $N _ { c } ( q )$ have similar meanings for the control group. Random tar geting line represents the outcomes of customers that are randomly assigned to the treatment and control group. Therefore, the random gain of top q% customers is measured by $\overline { { R } } _ { t } ( q ) - \overline { { R } } _ { c } ( q )$ , where $\overline { { R } } _ { t } ( q )$ and $\overline { { R } } _ { c } ( q )$ are the average outcome of the treatment and control group, respec tively. The final AUUC and Qini coefficient are computed as follows.

$$
\mathrm{AUUC} (q) = \sum_ {i = 0} ^ {q} (R _ {t} (q) - R _ {c} (q))\tag{26}
$$

$$
\text { Qini   coefficient } (q) = \sum_ {i = 0} ^ {q} \left(R _ {t} (q) - R _ {c} (q) \frac {N _ {t} (q)}{N _ {c} (q)}\right) - \frac {q}{2} (\overline {{R}} _ {t} (q) - \overline {{R}} _ {c} (q))\tag{27}
$$

## 4. Experiments and results

In this section, we perform experiments on both synthetic dataset and industrial datasets. We provide a detailed introduction to the datasets and present and analyze the experimental results.

## 4.1. Experiments on synthetic dataset

We first describe the process of generating synthetic data. Subse quently, we present the experimental design, along with the results obtained from these experiments. Additionally, we include several supplementary analyses to validate the robustness of our proposed method.

## 4.1.1. Synthetic data generation

We generate a data consisting of 10,000 samples, following the procedures of [29], which simulate independent features, three nonmutually exclusive treatments and an outcome variable. The genera tion process incorporates difficult nuisance components of propensity function $g ^ { \ast } ( \bullet ) _ { : }$ , baseline main effect $e ^ { * } ( \bullet )$ and treatment effect function $\tau ^ { * } ( \bullet ) \colon$

$$
\boldsymbol {X} _ {i} \sim \mathrm{U} _ {d} (0, 1),\tag{28}
$$

$$
T _ {i, k} \sim \operatorname{Bernoulli} (g ^ {*} (k)),\tag{29}
$$

$$
\varepsilon_ {i} \sim \mathrm{N} (0, 1),\tag{30}
$$

$$
Y _ {i} = e ^ {*} (X _ {i}) + \left(\sum_ {k = 1} ^ {b} T _ {i, k} - 0. 5\right) \tau^ {*} (X _ {i}) + \sigma \varepsilon_ {i}\tag{31}
$$

where the feature set $X _ { i }$ of customer i is generated from a uniform dis tribution with dimension d (we set $d = 4 0$ to match the collected customer characteristics in real-world industrial dataset). The treatment

![](/api/attachments/DG2QCJE7/fulltext/images/9a3848bf963f39df8a436257403fa8dca6d6105c4af9e5eae2ee7ad3019f7a69.jpg)  
Fig. 3. Three-stage structure of WDRL.

<table><tr><td>Input:</td><td colspan="2">The outcome, treatments, and customer characters {Y,T,X}</td><td>An illustration example</td></tr><tr><td>Output:</td><td colspan="2">Conditional average effect for treatment k:  $\widehat{CATE}_{k}(X)$ </td><td>Assume that there are three (i.e., b=3 ) treatments: A, B and C</td></tr><tr><td>(1)</td><td colspan="2">Form the combination set C according to the treatments, set C includes full permutations of total b treatments.</td><td>Set C should be:{O,A,B,C,AB,AC,BC,ABC}</td></tr><tr><td>(2)</td><td colspan="2">For each treatment k ∈ [1,b]</td><td>When k=1, treatment A is selected; when k=2, treatment B is selected, and so on for subsequent values for k.</td></tr><tr><td>(3)</td><td rowspan="12"></td><td>Divide C into three subsets {O ∪ S_{-k} ∪ Wk} according to k</td><td>Subset S_{-k}={B,C,BC},Subset Wk={A,AB,AC,ABC}</td></tr><tr><td>(4)</td><td>Let s ∈ {O ∪ S_{-k}}, w ∈ Wk, where satisfies k = w ⊖ s,</td><td>A={A,AB,AC,ABC} ⊖ {O,B,C,BC}</td></tr><tr><td>(5)</td><td>For t=1 to 2b-1</td><td>When t=1, wt is treatment A and st is treatment O; when t=2, wt is combination treatments AB and st is treatment B, and so forth.</td></tr><tr><td>(6)</td><td></td><td>T_i=1, if customer i receive wt, wt ∈ Wkand Ti=0, if customer i receive st, st ∈ S_{-k}</td></tr><tr><td>(7)</td><td></td><td>Build regression model to predict Yt(t) with Xi and Ti</td></tr><tr><td>(8)</td><td></td><td>Build classification model to predict Tt(t) with Xi</td></tr><tr><td>(9)</td><td></td><td>Compute YtDR(t) and YDR0,i(t) following Eqs. (15) and (16)</td></tr><tr><td>(10)</td><td></td><td>Compute YtDR(t) = YDR1,i(t) - YDR0,i(t)</td></tr><tr><td>(11)</td><td>End For</td><td></td></tr><tr><td>(12)</td><td>Compute the YtWDR=(1/2b-1)Σt=12b-1P(wt)YtDR(t), where P(wt) is the probability of occurrence of wt</td><td rowspan="2">YtWDR are computed by performing a weighted average of the four groups of YtDR(t), using the weights based on the probability of receiving treatment A.</td></tr><tr><td>(13)</td><td>Build a final regression learner with the label of YtWDR, and the input of Xi</td></tr><tr><td>(14)</td><td> $\widehat{CATE}_{k}(X) = learner(X_{i})$ </td><td>The CATE of treatment A are thus estimated.</td></tr><tr><td>(15)</td><td colspan="2">End For</td><td></td></tr></table>

$T _ { i , k }$ follows a Bernoulli distribution with propensity of $g ^ { \ast } ( k )$ . The error term ε is drawn from a standard normal distribution, with σ repre senting the standard deviation of the error term (defaulted to 1). To ensure sensible and appropriate treatment assignment, we set $g ^ { * } ( k )$ as the probability of the k-th treatment, aligning with the treatment dis tribution observed in the real-world industrial data. Consistent with [29], the baseline main effect and the treatment effect function are set as $e ^ { * } ( X _ { i } ) = s i n ( \pi X _ { i 1 } X _ { i 2 } ) + 2 ( X _ { i 3 } - 0 . 5 ) ^ { 2 } + X _ { i 4 } + 0 . 5 X _ { i 5 } \qquad { \mathrm { a n d } } \qquad \tau ^ { * } ( X _ { i } ) = 0 . 8 X _ { i } .$ $( X _ { i 1 } + X _ { i 2 } ) / 2 ,$ respectively.

## 4.1.2. Experiment design on synthetic data

In our experiment, we aim to achieve three objectives of uplift modeling as depicted in Fig. 1, which includes estimating the CATE, targeting the population that makes response positively, and attributing the treatment to support business decision making.

Concerning the first objective of CATE estimation, we compare our proposed WDRL with five other established approaches: S-learner, Tlearner, X-learner, DML, and DRL. Each approach utilizes four base learners, i.e., logistic regression, decision trees, random forests, and gradient boosting trees, to ensure a comprehensive benchmark study and a robust estimate of CATE. For the experiment, we randomly divide the entire dataset into a training set (70%) and a test set (30%).

Regarding the second objective of population targeting, we compute the AUUC and the Oini coefficient based on the estimated CATE from each method, considering different quantiles. We plot the uplift curves and Oini curves accordingly. Higher values of AUUC and Oini coefficient in the top quantiles indicate successful targeting of the most responsive individuals.

For the third objective of treatment attribution, we compute the AUUC and Qini coefficient for each treatment. The treatment with the highest AUUC and Qini is attributed as the most effective tool, indicating the maximized response and behavioral changes among customers.

## 4.1.3. Experimental results on synthetic data

4.1.3.1. Results of CATE estimation. Fig. 4 displays error bars repre senting the estimated individual treatment effects using various ap proaches. Each approach utilizes four base learners. Notably, DML, DRL, and WDRL necessitate the simultaneous prediction of discrete treatment and continuous outcome, for which a combination of logistic regression and linear regression is employed. Logistic regression handles classifi cation problems while linear regression tackles regression problems exclusively. The data points in the figure represent the average indi vidual treatment effect (CATE), while the lines represent the corre sponding standard deviations.

The results demonstrate variations among different base learners. Notably, Fig. 4(c) and (d) exhibit a more stable estimation of CATE with lower standard deviations. This suggests that the choice of base learners influences the estimation outcomes. Random forests and gradient boosting trees employ ensemble estimators, whereas logistic regression and decision trees rely on single estimators. Therefore, it can be inferred that the number of estimators may impact the estimation results. The bagging technique in random forests and the boosting mechanism in gradient boosting trees amalgamate and average the performance of multiple estimators, thus yielding a more robust estimation [39,40].

4.1.3.2. Results of population targeting. Based on the estimated CATE, we calculate uplift gains and Qini coefficients for various proportions of the targeted population. The corresponding uplift curves and Qini curves are presented in Fig. 5. Specifically, Fig. 5(a)-(d) depict the uplift curves, while Fig. 5(e)-(h) showcase the Oini curves for different types of base learners. In these figures, the black dotted lines indicate the in cremental revenues achieved by randomly targeting customers. Higher incremental revenues signify a stronger impact of the treatments on customers. It is evident that most approaches exhibit curves above the line of random targeting, indicating accurate targeting of populations that exhibit behavioral changes in response to the treatment. Notably, the approaches utilizing random forests as base learners demonstrate the best performances.

![](/api/attachments/DG2QCJE7/fulltext/images/46cc2aaeb8794cf0f422156d253c543ea1ff115f33948176d0732b1e034b3d9b.jpg)  
(a) Logistic Regression + Linear Regression

![](/api/attachments/DG2QCJE7/fulltext/images/c6e3f86988847c5dbf2aa92fae25d93a7c8f9c9d043da6eb682534398090ceb0.jpg)  
(b) Decision Trees

![](/api/attachments/DG2QCJE7/fulltext/images/f5c941c24952b9fce5ffd29a97d6f86c3e07ad1d0ec4883860d223a62ba26def.jpg)

![](/api/attachments/DG2QCJE7/fulltext/images/8d4b5017c5fd833391b1d633aa2f5e5c764b1a8514f84d174afab72a04cedd44.jpg)  
(d) Gradient Boosting Trees

Fig. 4. Error-bar plot of individual treatment effect.

<table><tr><td>SL</td><td>TL</td><td>XL</td><td>DML</td><td>DRL</td><td>WDRL</td><td>--- Random</td></tr></table>

![](/api/attachments/DG2QCJE7/fulltext/images/fcd0d0e94f2eed8bdc172d74bbf5b3ed7b933de5d9eed97bfe7ca2c22936f1aa.jpg)

![](/api/attachments/DG2QCJE7/fulltext/images/3d65dec4ec29f4cffa1415dc6ffbc878dbc1a892378843ebf2ac6da35c56cafa.jpg)  
(a) Logistic Regression + Linear Regression  
(b) Decision Trees

![](/api/attachments/DG2QCJE7/fulltext/images/03a2d99bc7539c019d591bedcff6e92bd4fbf87eab48f3254e158906b16e2fff.jpg)  
(c) Random Forests

![](/api/attachments/DG2QCJE7/fulltext/images/f337d7a2c564a395029c31c0e260e66f3dedbb4c5a70ab0f2355905073d0d068.jpg)  
(d) Gradient Boosting Trees

![](/api/attachments/DG2QCJE7/fulltext/images/99ba063f34ccee20fed7502881ac9eb7c8918125b8340e68a8c6f872facfce36.jpg)  
(e) Logistic Regression + Linear Regression

![](/api/attachments/DG2QCJE7/fulltext/images/5c591bdf85f37071e0052dd2dfe3aedc48fefdf68b84f8a206f75ceafb49237c.jpg)  
(f) Decision Trees

![](/api/attachments/DG2QCJE7/fulltext/images/20112f0b0679eb7f600d74f54acbdade0473cdb90338c19bcc5eae9af88062ad.jpg)  
(g) Random Forests

![](/api/attachments/DG2QCJE7/fulltext/images/7fe7dc1996ceee5759c3b392243fa0cfbb5232baed2c72566c391e835c5a8240.jpg)  
(h) Gradient Boosting Trees  
Fig. 5. Uplift curve and Qini curve using different approaches based on four types of learners.

To facilitate a clearer comparison, Table 2 presents the average AUUC and Qini coefficient for each estimation approach at various targeting deciles, considering different base learners. Notably, WDRL outperforms other models in terms of both AUUC and Qini coefficient. Furthermore, we observe that WDRL exhibits relatively smaller standard deviations compared to other models, indicating that its estimation re sults are more robust and stable. These findings highlight the superior performance and reliability of WDRL in effectively targeting populations that respond to mixed treatments. Consequently, it suggests that the framework of groups weighting based on doubly robust learning is a viable approach for uplift modeling.

Table 2  
The AUUC and Qini coefficient performance on synthetic data.

<table><tr><td></td><td colspan="5">Performance of subsamples at different targeting deciles</td></tr><tr><td>AUUC</td><td>Top 10%</td><td>Top 30%</td><td>Top 50%</td><td>Top 80%</td><td>Full samples</td></tr><tr><td>SL</td><td>0.007 (0.001)</td><td>0.063 (0.005)</td><td>0.166 (0.021)</td><td>0.384 (0.046)</td><td>0.567 (0.057)</td></tr><tr><td>TL</td><td>0.006 (0.002)</td><td>0.060 (0.008)</td><td>0.164 (0.017)</td><td>0.395 (0.034)</td><td>0.582 (0.041)</td></tr><tr><td>XL</td><td>0.005 (0.001)</td><td>0.044 (0.007)</td><td>0.122 (0.011)</td><td>0.314 (0.009)</td><td>0.495 (0.008)</td></tr><tr><td>DML</td><td>0.006 (0.001)</td><td>0.060 (0.008)</td><td>0.157 (0.017)</td><td>0.374 (0.036)</td><td>0.562 (0.040)</td></tr><tr><td>DRL</td><td>0.007 (0.001)</td><td>0.061 (0.007)</td><td>0.165 (0.011)</td><td>0.396 (0.014)</td><td>0.588 (0.013)</td></tr><tr><td>WDRL</td><td>0.008 (0.001)</td><td>0.066 (0.004)</td><td>0.169 (0.011)</td><td>0.398 (0.025)</td><td>0.590 (0.029)</td></tr><tr><td>Qini coefficient</td><td>Top 10%</td><td>Top 30%</td><td>Top 50%</td><td>Top 80%</td><td>Full samples</td></tr><tr><td>SL</td><td>0.002 (0.001)</td><td>0.018 (0.005)</td><td>0.037 (0.021)</td><td>0.055 (0.046)</td><td>0.057 (0.057)</td></tr><tr><td>TL</td><td>0.002 (0.002)</td><td>0.015 (0.008)</td><td>0.035 (0.017)</td><td>0.066 (0.034)</td><td>0.072 (0.041)</td></tr><tr><td>XL</td><td>0.000 (0.001)</td><td>-0.001 (0.007)</td><td>-0.007 (0.011)</td><td>-0.015 (0.009)</td><td>-0.015 (0.008)</td></tr><tr><td>DML</td><td>0.001 (0.001)</td><td>0.015 (0.008)</td><td>-0.029 (0.017)</td><td>0.045 (0.036)</td><td>0.052 (0.040)</td></tr><tr><td>DRL</td><td>0.002 (0.001)</td><td>0.016 (0.007)</td><td>0.036 (0.011)</td><td>0.067 (0.014)</td><td>0.077 (0.013)</td></tr><tr><td>WDRL</td><td>0.003 (0.001)</td><td>0.021 (0.004)</td><td>0.039 (0.011)</td><td>0.068 (0.025)</td><td>0.080 (0.029)</td></tr></table>

Note. The values in brackets indicate the standard deviation.

4.1.3.3. Results of treatment attribution. We present the performance of AUUC and Qini coefficient for different treatments on various pro portions of targeted populations in Fig. 6. We see that treatment B consistently exhibits larger AUUC and Qini coefficient, regardless of the percentage of customers targeted. This suggests that treatment B has a greater impact on promoting customer consumption and increasing revenues compared to treatment A and treatment C. Among the three treatments, treatment C demonstrates the poorest performance, as indicated by its lowest Qini coefficient. This implies that treatment C is less effective in stimulating customers’ response.

## 4.1.4. Additional analyses on synthetic data

To validate the sensitivity and robustness of our proposed WDRL, we have conducted several additional analyses under different conditions to further explore the potential of the synthetic data. These experiments can be summarized as follows.

4.1.4.1. Changing the level of nuisance in the outcome generation. During the generation of synthetic data, we observed that the outcome variable Y is generated by aggregating non-linear functions of treatments and features, and an error term. As the outcome of customers may be influenced by unobservable features besides the treatment and observ able features, we attempted to modify the level of nuisance through the parameter σ in Eq. (31). Increasing the value of σ introduces more disturbance to the outcome, making the accurate estimation of CATE more challenging. The performance of AUUC and Qini is depicted in Fig. 7(a) and (b) respectively. The figures clearly demonstrate that WDRL outperforms other methods in terms of both AUUC and Qini, indicating its superior performance in accurately estimating CATE.

4.1.4.2. Changing the propensity of treatments. In treatment assignment, it is common for different treatments to have varying propensities of being assigned to customers. In the case of mixed treatments, the com bination of multiple treatments can result in a lower overall propensity, leading to an imbalance between the treatment group and control group. To examine whether such an imbalance affects the performance of WDRL, we implement different assignment settings for the three nonmutually exclusive treatments: (1) Balanced assignment: the assign ment propensity for Treatment A, Treatment B, and Treatment C is set to 1:1:1. (2) Imbalanced assignment: the assignment propensity for Treatment A, Treatment B, and Treatment C is set to 1:5:10. (3) Extremely imbalanced assignment: the assignment propensity for Treatment A, Treatment B, and Treatment C is set to 2:3:95. This assignment setting is consistent with the assignment distribution of mixed treatments in real-world datasets. The results of AUUC and Qini using these different assignment settings are presented in Fig. 7(c) and (d) respectively. The findings once again confirm the superiority of WDRL over other methods, reaffirming its effectiveness even in the presence of imbalance between groups.

![](/api/attachments/DG2QCJE7/fulltext/images/222a1d2d487024cc09d2e6f6d564bbeb71fc657b579da0ee196728adb545059b.jpg)  
(a) AUUC of different treatments

![](/api/attachments/DG2QCJE7/fulltext/images/a1f1b39f76d64cda904ea455ffc0846de3fc3c9d32896c790a348ed385c77322.jpg)  
(b) Qini coefficient of different treatments  
Fig. 6. AUUC and Qini-coefficient of different treatments on synthetic data.

![](/api/attachments/DG2QCJE7/fulltext/images/701c5fc39366fbee49a2795670e2caf108cd42f7094ee5fe82e5eee9ac95e165.jpg)  
(a) AUUC on different level of nuisance

![](/api/attachments/DG2QCJE7/fulltext/images/4236e718dd92ee6b8a2a839991109709a1477edd3764e24cf4fbdc51cb3aa09a.jpg)  
(b) Qini coefficient on different level of nuisance

![](/api/attachments/DG2QCJE7/fulltext/images/dfa7c83820e9e956d2906aaf47e3b236b278c1d6b3ba87c9c3a80cd8e6ffe59f.jpg)  
(c) AUUC on different level of balance

![](/api/attachments/DG2QCJE7/fulltext/images/423b380d9bb96d6d744abe8e2b50db7d882d5ce6be53c6f9d7348720b32f0e2b.jpg)  
(d) Qini coefficient on different level of balance

![](/api/attachments/DG2QCJE7/fulltext/images/124bd0810f5b47d7ab6b46d5cfd69e9830131cdbf3b9f93fc61024bb6ea3704b.jpg)  
(e) AUUC on different number of treatments

![](/api/attachments/DG2QCJE7/fulltext/images/05ab2d564ea271cbbda453cb09b5461f86745e33657a31f08c896e7c8e832c67.jpg)  
(f) Qini coefficient on different number of treatments  
Fig. 7. Additional analyses results on synthetic data.

4.1.4.3. Changing the number of treatments. In addition to the previously discussed non-mutually exclusive treatments, we have considered a more complex scenario by increasing the number of treatments. This analysis aims to investigate whether the performance of WDRL is affected by the number of treatments. The results are presented in Fig. 7 (e) and (f). Once again, we observe that WDRL surpasses other methods, providing superior performance. These three additional analyses con ducted on synthetic data effectively demonstrate the robustness of WDRL in accurately estimating CATE and effectively targeting the most responsive customers. However, the training complexity of WDRL may rise significantly with the increase of the number of treatments. Table 3 shows the training time of WDRL with different number of treatments and different base learners.

Table 3  
Time cost of training WDRL with different number of treatments.

<table><tr><td>Treatment number</td><td>Logistic regression</td><td>Decision trees</td><td>Random forests</td><td>Gradient boosting</td></tr><tr><td>2</td><td>0.38 s</td><td>2.43 s</td><td>108.15 s</td><td>59.86 s</td></tr><tr><td>3</td><td>0.69 s</td><td>3.88 s</td><td>172.75 s</td><td>86.54 s</td></tr><tr><td>4</td><td>1.01 s</td><td>4.51 s</td><td>204.79 s</td><td>105.04 s</td></tr><tr><td>5</td><td>1.73 s</td><td>5.27 s</td><td>253.00s</td><td>156.63 s</td></tr><tr><td>6</td><td>7.13 s</td><td>15.32 s</td><td>619.54 s</td><td>385.93 s</td></tr></table>

Note. Default time unit is seconds.

From the table, it is evident that the training time increases as the number of treatments increases. However, the choice of base learners also affects the training cost. Specifically, logistic regression exhibits the shortest training time, while random forests consume the most time. To strike a balance between estimation performance and training complexity, we can reconcile these two perspectives to achieve optimal results.

## 4.2. Experiments of industrial dataset

In the section, we conduct experiments using real-world industrial data to further validate the results obtained from the synthetic data analysis.

## 4.2.1. Description of industrial data

The industrial dataset was collected from a large ride-hailing plat form in China, containing 20,794,178 samples from two first-tier cities (Guangzhou city and Shenzhen city in China) between Apr, 2021 and

Apr, 2022. In this dataset, 40 features are collected, including customer consumption behaviors and order attributes. Customer consumption behaviors consist of traditional RFM features, namely recency, fre quency and monetary [41] while the order attributes include the num ber and the amounts of orders, as well as other features about the ride. All features and corresponding definitions are provided in Appendix Table A1.

In addition to the features, the dataset also includes three marketing strategies: treatment A, B and C. These strategies are randomly applied to customers and are non-exclusive. Treatment A involves providing customers with an electronic discount coupon package that combines several ride vouchers. Passengers can enjoy a fixed discount for a certain number of orders when riding the express within the validity period. Treatment B involves offering customers a free ride for their first order, selected at random. Treatment C provides customers with a cashback that’s a certain percentage of the order amount after the customer has hailed a ride.

The outcome variable is customers’ total consumption amount over the subsequent three months, which can also be considered as the platform’s revenues from these customers. Prior to utilizing the dataset, we thoroughly analyze whether it met the assumptions of the potential outcome framework. Firstly, we scrutinize the variables in the feature set and the treatments. Since the platform assigns treatments randomly without considering customers’ features, there is no confounding effect on the customers’ feature set. Additionally, all customers have an equal probability of receiving any of the treatments, thereby satisfying the ignorability and overlapping assumption. Since the treatments (e.g., discounts, coupons, or cashback) are issued to the customer account, and they receive and use them independently, their consumption be haviors are unlikely to be influenced by others’ treatments, thus meeting the stable unit treatment values assumption. Based on these assump tions, we develop uplift models that assess the incremental revenues promoted by these treatments and target the customers who respond positively to the treatments.

## 4.2.2. Treatment distributions of industrial data

The experimental settings for the industrial dataset are consistent with those used for synthetic data. To provide a clearer presentation of data, we present group division result based on treatment attribution. Table 4 shows a biased treatment assignment, where the propensity of treatment A, B, and C is approximately 3:95:2, which causes the extremely imbalance in samples between groups as well as the imbal ance between treatment subgroup and control subgroup within each group.

Besides, we plot the average revenue outcomes of customers in each group. As shown in Fig. 8, the average revenues of most treatment subgroups are significantly higher than those of most control subgroups, providing model-free evidence that the treatments indeed generate in cremental revenues among customers. Specifically, the differences in average revenue between treatment and control subgroups are sub stantial in groups 1–3, groups 5–7, and groups 9–11. In contrast, the differences in average revenue between treatment and control sub groups in groups 4, 8, and 12 decrease. In these three groups, all cus tomers receive two treatments or more. Therefore, we can infer that the marginal revenue increment of the treatment gradually diminishes when customers have already benefited from other treatments.

## 4.2.3. Experimental results on industrial data

Fig. 9 displays the uplift curves and Qini curves based on the esti mated CATE using different approaches. It is evident that most of the curves are above the random targeting line, indicating that these ap proaches have successfully targeted the customers who are responsive to the treatments. However, some curves are below the random targeting line, which may be attributed to two factors. First, the customers’ hailing behaviors depend on various unobservable covariates, such as their preferences and the weather, which are limited by the privacy of customer data. While we have limited access to these factors, accurate estimation of CATE and population targeting is challenging. Although we conduct sensitivity analysis on synthetic data, it is difficult to simulate a data distribution consistent with real-world data. Second, overfitting of base learners could also lead to the underperformances observed in certain cases, especially when using gradient boosting trees, which lacks regularization and thus is prone to overfitting when mul tiple estimators are ensembled [42]. Overall, we find that using random forests as base learners led to the best performance.

Table 4  
Group division based on treatment attribution.

<table><tr><td rowspan="3">Group</td><td colspan="4">Group division based on Shapley treatment attribution</td><td rowspan="3">Attributed treatment</td></tr><tr><td colspan="2">Treatment subgroup</td><td colspan="2">Control subgroup</td></tr><tr><td>Assigned treatments</td><td>No. of observations</td><td>Assigned treatments</td><td>No. of observations</td></tr><tr><td>Group 1</td><td>A</td><td>68,122</td><td>O</td><td>18,104,265</td><td></td></tr><tr><td>Group 2</td><td>AB</td><td>8455</td><td>B</td><td>2,568,966</td><td rowspan="2">A</td></tr><tr><td>Group 3</td><td>AC</td><td>282</td><td>C</td><td>38,341</td></tr><tr><td>Group 4</td><td>ABC</td><td>49</td><td>BC</td><td>5698</td><td></td></tr><tr><td>Group 5</td><td>B</td><td>2,568,966</td><td>O</td><td>18,104,265</td><td></td></tr><tr><td>Group 6</td><td>BA</td><td>8455</td><td>A</td><td>68,122</td><td rowspan="2">B</td></tr><tr><td>Group 7</td><td>BC</td><td>5698</td><td>C</td><td>38,341</td></tr><tr><td>Group 8</td><td>BAC</td><td>49</td><td>AC</td><td>282</td><td></td></tr><tr><td>Group 9</td><td>C</td><td>38,341</td><td>O</td><td>18,104,265</td><td></td></tr><tr><td>Group 10</td><td>CA</td><td>282</td><td>A</td><td>68,122</td><td rowspan="2">C</td></tr><tr><td>Group 11</td><td>CB</td><td>5698</td><td>B</td><td>2,568,966</td></tr><tr><td>Group 12</td><td>CAB</td><td>49</td><td>AB</td><td>8455</td><td></td></tr></table>

Note. The $\mathrm { { \ddot { o } } } \mathrm { { \dot { } } }$ represents null treatment.

Table 5 presents the average AUUC and Qini coefficient for each estimation approach across various base learners, at different targeting deciles. Among the models in the table, WDRL demonstrates the best performance in terms of Qini coefficient. While TL records the largest AUUC, its values significantly exceed those of other models, raising concerns about its reliability and credibility. In fact, prior studies have criticized the robustness of TL [43],

Finally, Fig. 10 summarizes the AUUC and Qini coefficient perfor mance of different treatments at various targeting levels. Our findings suggest that strategy A outperforms strategy B and strategy C, regardless of the percentage of customers being targeted. Specifically, strategy A exhibits a larger AUUC and Qini coefficient, indicating that it is more effective in driving customer consumption and increasing revenues on the platform. These results offer valuable insights for platforms seeking to optimize their treatment approach.

## 4.3. Discussions

Further discussions about the results reported above are provided here. Regarding the CATE estimation, we compare different base learners used in each estimation approach, and the results show that ensemble methods $( \mathrm { i . e . , }$ random forests and gradient boosting) provide more stable estimate of CATE than traditional base learners (i.e., logistic regression and decision tree). As for the population targeting, the results demostrate that WDRL, outperforms other methods in both AUUC and Qini score in all targeting deciles. This indicates that WDRL has a greater ability to accurately target customers who are likely to respond to promotion treatments. Conversely, SL, TL, and XL were found to be highly dependent on the choice of base learners, as their estimation outcomes can be easily influenced by the selection of base learners.

<table><tr><td>SL</td><td>TL</td><td>XL</td><td>DML</td><td>DRL</td><td>WDRL</td><td>--- Random</td></tr></table>

![](/api/attachments/DG2QCJE7/fulltext/images/59158d345f97daab22aa892da0f2eab7a4213aaae7e70c77d590961b288a7ad7.jpg)  
Fig. 8. The average revenue between the treatment and control subgroups.

![](/api/attachments/DG2QCJE7/fulltext/images/7d342936f072e5cd48c7dd838e456d4b2a2338c70b2e71c3e2b1215151bd488a.jpg)  
(a) Logistic Regression + Linear Regression

![](/api/attachments/DG2QCJE7/fulltext/images/caec75581d5d80c49cdffea3088e4d0d7b119dca82e528cb3d547ad056435051.jpg)  
(b) Decision Trees

![](/api/attachments/DG2QCJE7/fulltext/images/c9b07e826e48aaea47faddf89e977c026a994d376a519b6f5b112b0628a7bcce.jpg)  
(c) Random Forests

![](/api/attachments/DG2QCJE7/fulltext/images/c811c9bda4f61af39f7dfd10d7f902c4ddcb3ef823f31ee162afa0f4297d7dee.jpg)  
(d) Gradient Boosting Trees

![](/api/attachments/DG2QCJE7/fulltext/images/31d3660de9bceb403b5abda8908e66c529e0e6c29672bc9a96ad6a0820564828.jpg)  
(e) Logistic Regression + Linear Regression

![](/api/attachments/DG2QCJE7/fulltext/images/51f4e107c5e0ce5a4643a23b7555af64cea0068396cf36383306de9eefb3835a.jpg)  
(f) Decision Trees

![](/api/attachments/DG2QCJE7/fulltext/images/fc2590dda5b5da2312b2baa92fe4c7840fa20bd6d858147380ff308859c2dcb0.jpg)  
(g) Random Forests

![](/api/attachments/DG2QCJE7/fulltext/images/7075e139817800aaef312dc8c93ac7a4ce2b57ac207d901234d40085c9a5e9cb.jpg)  
(h) Gradient Boosting Trees  
Fig. 9. Uplift curve and Qini curve using different approaches based on four types of learners.

To support sound business decision-making, we further explore the most effective treatment by examining the mixed treatments. Tradi tional methods tend to either overestimate (e.g., TL) or underestimate (e.g., DML) the CATE. However, DRL and WDRL are more reliable in estimating the effect of mixed treatments, with the performance of WDRL surpassing that of DRL. The comparative analysis of AUUC and

Qini score for various treatments show that strategy A in real-world dataset yields higher uplift compared to the other treatments. Our study presents a beneficial approach for identifying effective treatment without confounding effects from other treatments.

## 5. Conclusion

In current marketing research, uplift modeling holds significant importance as it quantifies the incremental benefit that marketing treatments can bring to a company. This provides direct implications for marketing development and overall business operations. In our study, we employ treatment attribution based on Shapley value, utilizing it to divide groups into unconfounded treatment subgroups and control subgroups. Furthermore, we propose a framework called weighted doubly robust learning (WDRL), which integrates different groups by weighting them based on group size. This framework enables more ac curate estimation of the CATE and identification of the most responsive customers and most effective treatment. Our results demonstrate that WDRL outperforms other estimation approaches in terms of metrics such as AUUC and Qini. By evaluating the treatment effects of various stra tegies, our study offers practical insights for companies, helping them identify the most effective strategies and optimize the use of promo tional tools to stimulate customer consumption and maximize revenue generation. This research contributes to the existing literature by providing a robust uplift modeling approach and valuable implications for business decision-making.

Table 5  
The AUUC and Qini coefficient performance on industrial data.

<table><tr><td rowspan="2">AUUC</td><td colspan="5">Performance of subsamples at different targeting deciles</td></tr><tr><td>Top 10%</td><td>Top 30%</td><td>Top 50%</td><td>Top 80%</td><td>Full samples</td></tr><tr><td>SL</td><td>0.006 (0.001)</td><td>0.047 (0.010)</td><td>0.128 (0.032)</td><td>0.340 (0.099)</td><td>0.517 (0.108)</td></tr><tr><td>TL</td><td>0.015 (0.006)</td><td>0.132 (0.046)</td><td>0.335 (0.096)</td><td>0.626 (0.131)</td><td>0.806 (0.134)</td></tr><tr><td>XL</td><td>0.004 (0.004)</td><td>0.033 (0.019)</td><td>0.112 (0.048)</td><td>0.320 (0.069)</td><td>0.496 (0.071)</td></tr><tr><td>DML</td><td>0.004 (0.003)</td><td>0.026 (0.017)</td><td>0.079 (0.042)</td><td>0.230 (0.069)</td><td>0.395 (0.073)</td></tr><tr><td>DRL</td><td>0.002 (0.003)</td><td>0.044 (0.025)</td><td>0.152 (0.053)</td><td>0.404 (0.121)</td><td>0.584 (0.140)</td></tr><tr><td>WDRL</td><td>0.002 (0.004)</td><td>0.045 (0.014)</td><td>0.157 (0.017)</td><td>0.422 (0.049)</td><td>0.605 (0.066)</td></tr><tr><td>Qini coefficient</td><td>Top 10%</td><td>Top 30%</td><td>Top 50%</td><td>Top 80%</td><td>Full samples</td></tr><tr><td>SL</td><td>-0.024 (0.003)</td><td>-0.075 (0.017)</td><td>-0.120 (0.037)</td><td>-0.099 (0.088)</td><td>-0.032 (0.097)</td></tr><tr><td>TL</td><td>-0.022 (0.005)</td><td>-0.072 (0.019)</td><td>-0.126 (0.030)</td><td>-0.105 (0.031)</td><td>-0.046 (0.029)</td></tr><tr><td>XL</td><td>-0.023 (0.004)</td><td>-0.065 (0.020)</td><td>-0.092 (0.048)</td><td>-0.058 (0.076)</td><td>0.007 (0.081)</td></tr><tr><td>DML</td><td>-0.024 (0.004)</td><td>-0.079 (0.023)</td><td>-0.130 (0.058)</td><td>-0.121 (0.104)</td><td>-0.058 (0.118)</td></tr><tr><td>DRL</td><td>-0.026 (0.004)</td><td>-0.056 (0.036)</td><td>-0.067 (0.071)</td><td>-0.021 (0.128)</td><td>0.041 (0.148)</td></tr><tr><td>WDRL</td><td>-0.027 (0.006)</td><td>-0.053 (0.009)</td><td>-0.058 (0.025)</td><td>-0.003 (0.068)</td><td>0.063 (0.086)</td></tr></table>

Note. The values in brackets indicate the standard deviation.

![](/api/attachments/DG2QCJE7/fulltext/images/b74537d66fc4ae63ea9d55b0a9117f92ec99e8193afd4221ce72e009f3233728.jpg)  
(a) AUUC of different treatments

![](/api/attachments/DG2QCJE7/fulltext/images/6883c0f44cfdaf54e0a30b74dbc0e5c2a1919b65041702b45edfb7e208342a93.jpg)  
(b) Qini coefficient of different treatments  
Fig. 10. AUUC and Qini-coefficient of different treatments on industrial data.

This study also has limitations that should be acknowledged. Firstly, there is minor inconsistency between the results of AUUC obtained from synthetic data and real-world data. This may be attributed to various reasons, such as biased treatment assignment, unobservable covariates, and other potential confounding variables. Even though we conduct numerous sensitivity analyses on the synthetic data to ensure the robustness of WDRL to the extent possible, we must note that simulating the synthetic data to be completely identical to the real-world data is challenging, making it difficult to replicate the results obtained from real-world data in the synthetic data. Besides, there are numerous remaining nuances and variables in the real-world data that could not be accounted for in our study due to data unavailability, which influence the observed results as well. More datasets are required to fully validate the potential of the WDRL in untangling the mixed treatments’ effects. Last but not least, WDRL may encounter training complexity problems when dealing with a large number of treatments in mix. While using simpler base learners can help mitigate this complexity, it may also have an impact on the estimation performance of the CATE to some extent. Given that training cost is a significant concern for causal classification [44], finding the right balance between estimation performance and complexity becomes crucial for improving WDRL.

For future studies, more research in uplift modeling of mixedtreatments could be carried out for various reasons. Firstly, addressing confoundedness is a critical challenge in mixed treatments problems. While this study employs Shapley treatment attribution, alternative approaches should be explored to overcome confounding and to tackle this issue effectively. Moreover, the WDRL combines different groupbased DRL models, weighting them based on group size, to estimate the CATE and to attribute the most effective treatment. To enhance current benchmark studies, future studies should consider different base models or algorithms and explore various integration or evaluation mechanisms. such as seeking alternative CATE estimand in uplift modeling [45]. Additionally, although multi-treatments prediction can be seen as a multi-label classification problem, extending existing literature on multi-label classification to include mixed treatments could yield intriguing opportunities for future developments and advance causal machine learning research. In all, regarding the uplift modeling research of mixed treatments, there are still ample rooms for further exploration.

## CRediT authorship contribution statement

Baoqiang Zhan: Data curation, Software, Writing – original draft. Chao Liu: Methodology, Visualization. Yongli Li: Writing – review & editing, Validation. Chong Wu: Funding acquisition, Supervision.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence

the work reported in this paper.

## Data availability

The authors do not have permission to share data.

## Acknowledgements

This research is financially supported by the National Natural Sci ence Foundation of China (Nos.72171059, 72121001, 71771041, 72131005, 71771066), Natural Science Foundation of Heilongjiang Province, China (No. YQ2020G003) and Philosophy and Social Sciences Research Planned Project of Heilongjiang Province, China (No. 21XWB124).

## Appendix

Table A1

Feature definitions.

<table><tr><td>Types</td><td>Features</td><td>Definitions</td></tr><tr><td rowspan="9">RFM features</td><td>R_A_n</td><td>The number of days since the most recent service A for customer within the latest n days (n = 3,7,14,28)</td></tr><tr><td>F_A_n</td><td>The frequency of service A for customer within the latest n days (n = 3,7,14,28)</td></tr><tr><td>M_A_n</td><td>The spending of service A for customer within the latest n days (n = 3,7,14,28)</td></tr><tr><td>R_B_n</td><td>The number of days since the most recent service B for customer within the latest n days (n = 3,7,14,28)</td></tr><tr><td>F_B_n</td><td>The frequency of service B for customer within the latest n days (n = 3,7,14,28)</td></tr><tr><td>M_B_n</td><td>The spending of service B for customer within the latest n days (n = 3,7,14,28)</td></tr><tr><td>R_C_n</td><td>The number of days since the most recent service C for customer within the latest n days (n = 3,7,14,28)</td></tr><tr><td>F_C_n</td><td>The frequency of service C for customer within the latest n days (n = 3,7,14,28)</td></tr><tr><td>M_C_n</td><td>The spending of service C for customer within the latest n days (n = 3,7,14,28)</td></tr><tr><td rowspan="4">Order attributes</td><td>Order amount</td><td>The total amount of orders</td></tr><tr><td>Order number</td><td>The number of orders</td></tr><tr><td>City</td><td>The city where the order was taken</td></tr><tr><td>Driving distance</td><td>The Driving distance of the order</td></tr></table>

Note. The service A, B and C within the ride-hailing platform represent fast car service, carpooling and premium rides, respectively. Each RFM feature consists four variables. For instance, R A n encompass R A 3, R A 7, R A 14 and R A 28.

## References

[1] J. Ro¨ßler, D. Schoder, Bridging the gap: a systematic benchmarking of uplift modeling and heterogeneous treatment effects methods, J. Interact. Mark. 57 (2022) 629–650.

[2] F. Devriendt, D. Moldovan, W. Verbeke, A literature survey and experimental evaluation of the state-of-the-art in uplift modeling: a stepping stone toward the development of prescriptive analytics, Big Data 6 (2018) 13–41.

[3] W. Zhang, J. Li, L. Liu, A unified survey of treatment effect heterogeneity modelling and uplift modelling, ACM Comput. Surv. 54 (2022) 1–36.

[4] R.M. Gubela, S. Lessmann, B. Stocker, ¨ Multiple treatment modeling for target marketing campaigns: a large-scale benchmark study, Inf. Syst. Front. (2022), https://doi.org/10.1007/s10796-022-10283-4

[5] K. Ruda´s, S. Jaroszewicz, Linear regression for uplift modeling, Data Min. Knowl. Disc, 32 (2018) 1275–1305.

[6] D. Olaya, K. Coussement, W. Verbeke, A survey and benchmarking study of

[7] B.S. Graham. C.C.X. de Pinto. Semiparametrically efficient estimation of the average linear regression function, J. Econ. 226 (2022) 115–138.

[8] A. De Caigny, K. Coussement, W. Verbeke, K. Idbenjra, M. Phan, Uplift modeling and its implications for B2B customer churn prediction: a segmentation-based modeling approach, Ind, Mark, Manag, 99 (2021) 28–39.

[9] J. Yang, W. Wang, Y. Dong, X. He, L. Jia, H. Chen, M. Mao, GRFlift: uplift modeling for multi-treatment within GMV constraints. Appl. Intell. 53 (2022) 4827–4840.

[10] H. Nian, C. Yu, J. Ding, H. Wu, W.D. Dupont, S. Brunwasser, T. Gebretsadik, T. V. Hartert. P. Wu. Performance evaluation of propensity score methods for estimating average treatment effects with multi-level treatments. J. Appl. Stat. 46 (2019) 853–873.

[11] D.B. Rubin, Estimating causal effects of treatments in randomized and

[12] P. Feng, X.-H. Zhou, Q.-M. Zou, M.-Y. Fan, X.-S. Li, Generalized propensity score for estimating the average treatment effect of multiple treatments. Stat. Med. 31 (2012) 681–697.

[13] S.O. Becker, P.H. Egger, Endogenous product versus process innovation and a firm's propensity to export, Empir. Econ. 44 (2013) 329–354.

[14] A. Caloffi, M. Freo, S. Ghinoi, M. Mariani, F. Rossi, Assessing the effects of a deliberate policy mix: the case of technology and innovation advisory services and innovation vouchers, Res. Policy 51 (2022), 104535.

[15] M. Greco, F. Germani, M. Grimaldi, D. Radicic, Policy mix or policy mess? Effects of cross-instrumental policy mix on eco-innovation in German firms, Technovation 117 (2022), 102194.

[16] A.E. Kazdin. D.P. Hartmann. The simultaneous-treatment design. Behay. Ther. 9 (1978) 912–922.

[17] J.J. McGonigle, J. Rojahn, J. Dixon, P.S. Strain, Multiple treatment interference in the alternating treatments design as a function of the intercomponent interva length, J. Appl. Behav. Anal. 20 (1987) 171–178.

[18] W.K. Newey, S. Stouli, Heterogeneous coefficients, control variables and identification of multiple treatment effects. Biometrika 109 (2022) 865–872.

[19] B. Dalessandro, C. Perlich, O. Stitelman, F. Provost, Causally motivated attribution for online advertising, in: Proceedings of the Sixth International Workshop on Data Mining for Online Advertising and Internet Economy, ACM, Beijing China, 2012, pp. 1–9.

[20] S. Kumar, G. Gupta, R. Prasad, A. Chatteriee, L. Vig, G. Shroff, CAMTA: causal attention model for multi-touch attribution in: 2020 International Conference on Data Mining Workshops (ICDMW). IEEE, Sorrento, Italy, 2020, pp. 79–86.

[21] D. Olava, J. Vásquez, S. Maldonado, J. Miranda, W. Verbeke, Uplift modeling for preventing student dropout in higher education, Decis. Support. Syst. 134 (2020). 113320.

[22] M. Belbahri, O. Gandouet, A. Murua, V.P. Nia, A Twin Neural Model for Uplift, ht p://arxiv.org/abs/2105.05146, 2021 (accessed May 21, 2023).

[23] C. Renaudin, M. Martin, About Evaluation Metrics for Contextual Uplift Modeling. http://arxiv.org/abs/2107.00537, 2021 (accessed May 21, 2023)

[24] C. Fern´andez-Loría, F. Provost, Causal classification: treatment effect estimation vs. outcome prediction, J. Mach. Learn. Res. 23 (2022) 2573–2607.

[25] C Fernández-Loría E Provost, Causal decision making and causal effect estimation

[26] S.R. Künzel, J.S. Sekhon, P.J. Bickel, B. Yu, Meta-learners for estimating heterogeneous treatment effects using machine learning. Proc, Natl. Acad. Sci, U. S A. 116 (2019) 4156–4165

[27] C. Fernandez-Loría, ´ F. Provost, J. Anderton, B. Carterette, P. Chandar, A comparison of methods for treatment assignment with an application to playlist generation, Inf. Syst. Res. 34 (2023) 786–803.

[28] V. Chernozhukov, D. Chetverikov, M. Demirer, E. Duflo, C. Hansen, W. Newey, J. Robins, Double/Debiased Machine Learning for Treatment and Causal Parameters. http://arxiv.org/abs/1608.00060, 2016 (accessed November 23, 2022).

[29] X. Nie, S. Wager, Quasi-Oracle Estimation of Heterogeneous Treatment Effects. htt p://arxiv.org/abs/1712.04912, 2020 (accessed November 23, 2022).

[30] H. Bang, J.M. Robins, Doubly robust estimation in missing data and causa inference models. Biometrics 61 (2005) 962–972

[31] M.J. Funk, D. Westreich, C. Wiesen, T. Stürmer, M.A. Brookhart, M. Davidian, Doubly robust estimation of causal effects. Am. J. Epidemiol. 173 (2011) 761–767.

[32] Ł. Zaniewicz, S. Jaroszewicz, Lp-support vector machines for uplift modeling, Knowl. Inf. Syst. 53 (2017) 269–296.

[33] L.S. Shapley, A value for n-person games, Contrib. Theory Games 2 (1953) 307–317.

[34] S. Lipovetsky, M. Conklin, Analysis of regression in game theory approach, Appl. Stoch. Model. Bus. Ind. 17 (2001) 319–330.

[35] S. Lundberg, S.-I. Lee, A Unified Approach to Interpreting Model Predictions. htt p://arxiv.org/abs/1705.07874, 2017 (accessed December 28, 2022).

[36] R. Singal, O. Besbes, A. Desir, V. Goyal, G. Iyengar, Shapley meets uniform: an axiomatic framework for attribution in online advertising, Manag. Sci. 68 (2022) 7457–7479.

[37] P. Rzepakowski, S. Jaroszewicz, Decision trees for uplift modeling with single and multiple treatments, Knowl. Inf. Syst. 32 (2012) 303–327.

[38] N. Radcliffe, Using control groups to target on predicted lift: building and assessing uplift model, Direct Mark. Anal. J. 1 (2007) 14–21.

[39] L. Breiman, Random forests, Mach. Learn. 45 (2001) 5–32.

[40] J.H. Friedman, Greedy function approximation: a gradient boosting machine, Ann. Stat. 29 (2001) 1189–1232.

[41] P.S. Fader, B.G.S. Hardie, K.L. Lee, RFM and CLV: using iso-value curves for customer base analysis, J. Mark. Res. 42 (2005) 415–430.

[42] T. Chen, C. Guestrin, XGBoost: a scalable tree boosting system, in: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2016, pp. 785–794.

[43] R. Gubela, A. Bequ´e, S. Lessmann, F. Gebert, Conversion uplift in E-commerce: a systematic benchmark of modeling strategies, Int. J. Inf. Technol. Decis. Mak. 18 (2019) 747–791.

[44] W. Verbeke, D. Olaya, M.A. Guerry, J. Van Belle, To do or not to do? Cost-sensitive causal classification with individual treatment effect estimates, Eur. J. Oper. Res. 305 (2023) 838–852.

[45] F. Devriendt, J. Van Belle, T. Guns, W. Verbeke, Learning to rank for uplift modeling, IEEE Trans. Knowl. Data Eng. 34 (2022) 4888–4904.

Baoqiang Zhan is a joint-PhD student at the Harbin Institute of Technology and The Hong Kong Polytechnic University. His research interests include causal inference, machine learning and business analytics. In his research, he focuses on using different novel ap proaches (e.g., text mining, machine learning and deep learning, etc.) to analyze con sumers' and investors behaviors. and study their impacts on firm value and marke performance.

Chao Liu is a joint-PhD student at the Harbin Institute of Technology and City University of Hong Kong. He received his B.S. degree in Management Science and Engineering from Northeastern University. His research interests include social network analysis and dy namic network evolution. He has published papers in Journal of Management Sciences in China, Quantitative Finance, Financial Innovation, and so on.

Yongli Li is a Professor at School of Economics and Management in Harbin Institute of Technology. He received his Ph.D. degree in Management Science and Engineering from Harbin Institute of Technology. His current research interests are network analysis, arti ficial intelligence and data analysis. He has published about 40 papers as the first author or the corresponding author in Journal of Economic Behavior and Organization, Quantitative Finance, Financial Innovation, European Journal of Operational Research, Omega, IEEE Transactions on Systems, Man, and Cybernetics: Systems, Journal of Informetrics, Scien tometrics, Journal of the Association for Information Science and Technology, Information Processing & Management and many other high-ranked journals

Chong Wu is a Professor at School of Economics and Management in Harbin Institute of Technology. He received his Ph.D. degree in Science from Harbin Institute of Technology. His research interests include artificial intelligence, fuzzy mathematics and decision analysis. He published his research in international journals including IEEE Transactions on Knowledge and Data Engineering, Journal of the Association for Information Science and Technology, Information Sciences, Knowledge-based Systems, Fuzzy Sets and Sys tems, Neural Networks, Applied Soft Computing, Complexity, Expert Systems with Ap plications and etc.

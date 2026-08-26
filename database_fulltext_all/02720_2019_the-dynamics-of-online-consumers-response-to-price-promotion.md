---
otero_id: 2720
otero_key: "JPXRFZFX"
title: "The Dynamics of Online Consumers’ Response to Price Promotion"
authors: "Youngsoo Kim; Ramayya Krishnan"
year: "2019"
journal: "Information Systems Research"
doi: "10.1287/isre.2018.0793"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [129.81.226.78] On: 13 February 2019, At: 23:47 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

![](/api/attachments/JPXRFZFX/fulltext/images/d4e8d3eb99ae0ed11f21f5922f8d996e6314d07ac5fee0a36172ad8f4d7c92d8.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# The Dynamics of Online Consumers’ Response to Price Promotion

Youngsoo Kim, Ramayya Krishnan

To cite this article: Youngsoo Kim, Ramayya Krishnan (2019) The Dynamics of Online Consumers’ Response to Price Promotion. Information Systems Research

Published online in Articles in Advance 12 Feb 2019

https://doi.org/10.1287/isre.2018.0793

Full terms and conditions of use: https://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2019, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# The Dynamics of Online Consumers’ Response to Price Promotion

Youngsoo Kim,<sup>a</sup> Ramayya Krishnan<sup>b</sup>

<sup>a</sup> Rawls College of Business, Texas Tech University, Lubbock, Texas 79409; <sup>b</sup> H. J. Heinz III College, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213

Contact: youngsoo.kim@ttu.edu, https://orcid.org/0000-0002-9602-4263 (YK); rk2x@andrew.cmu.edu, https://orcid.org/0000-0001-9935-2468 (RK)

Received: December 3, 2012 Revised: July 15, 2014; July 7, 2015; July 21, 2016; May 8, 2017 Accepted: July 4, 2017 Published Online in Articles in Advance: February 12, 2019

https://doi.org/10.1287/isre.2018.0793

Copyright: © 2019 INFORMS

Abstract. We aim to understand the attitudinal and behavior states of the online consumer–retailer relationship and its dynamics and, furthermore, to examine how consumers respond to price promotion as a function of the relationship. To do so, we build a hidden Markov model and estimate it with individual-level transaction data collected from a premier online retailer. Our quantification of transits across consumer–retailer relationship states provides unique insights. For example, price promotion can strengthen consumers’ loyalty only for consumers who are at least moderately loyal whereas it is not effective at changing nonloyal consumers’ attitudes toward an online retailer (i.e., from nonloyal to loyal). Unlike in the off-line market, consumers even in the strong relationship state are likely to seek more coupons as they increase their online shopping experience. The switching behavior observed even after online consumers reach the strong relationship state shows one aspect of the fierce price competition in the online market. Our results also suggest that managers of online retailers pay attention to the recent change in a consumer’s buying behaviors rather than the long-term trend of the consumer’s purchase behavior. For instance, an increase in recent purchase volume strengthens loyalty toward the retailer and/or the habit of buying without a coupon for consumers in the strong relationship state These findings have important managerial and operational implications for devising a customized marketing mix strategy.

History: Anindya Ghose, Senior Editor; Bin Gu, Associate Editor

Keywords: online buying behavior • hidden Markov model (hmm) • price promotion • coupon utilization

## 1. Introduction

Price dispersion still exists on the Internet; consumers do not all necessarily buy at the lowest price. The diverse heterogeneity (in terms of consumer, product, and retailer) and nonzero search costs explain the price dispersion (Lal and Sarvary 1999, Brynjolfsson and Smith 2000). Going beyond the static perspective on price sensitivity in the online market, this study aims to examine the dynamics of consumers’ price sensitivity at an online retailer.

Consumers can make more rational decisions in the online market because they can overcome limited information-based bounded rationality and take advantage of increased shopping-time flexibility. In contrast, consumers can also become loyal to an online retailer (lock-in or habitual choice of an online retailer) and exhibit irrational behavior, such as disregarding price. Given the two competing forces (rational versus irrational buying decisions), we empirically investigate the question of which factors are the main driver of online consumers’ retailer choices in the long term. Particularly, we aim to understand the development of loyalty toward an online retailer and/or the habitual choice of an online retailer by tracing the history of price promotion utilization at an online retailer. Ultimately, we attempt to quantify the dynamics of an online con sumer’s response to price promotion at an online retailer.

We assume the attitudinal and behavior states in the consumer–retailer relationship to model the dynamics of loyalty and habitual choice. Consumer–retailer relationships evolve and change over a series of interactions and in response to fluctuations in the contextual environment (Aaker et al. 2004). Oliver (1997) suggests that a discrete shift in relationship occurs if the aggregate satisfaction from a sequence of critical incidents is strong enough to move the customer to a higher leve of relationship with a retailer. Accordingly, consumers may exhibit different buying behaviors depending on their relationship states. Supposing that a consumer stays in a weak relationship state with a retailer; then the consumer’s buying decision at the retailer would be rational based on maximized utility. As the consumer moves to a strong or intimate relationship state, the consumer is more likely to make an irrational decision (e.g., purchasing even at a higher price) because the strong relationship leads to habitual behavior or loyalty to the retailer.

We utilize the hidden Markov model (HMM) to identify the latent consumer–retailer relationship states in a dynamic setting. From a managerial standpoint, it is valuable to identify homogeneous consumers’ segments (states) and characterize their behavior by them. The HMM also provides a flexible way of investigating intervention effects on (1) the transition across states and (2) behavior outcomes. The hypothetically different covariate effects across relationship states can offer valuable bases for a customized marketing strategy (Arora et al. 2008).

Our work contributes to several streams of literature. First, the quantification of transits across the consumer– retailer relationship states provides unique insights into the evolution of online consumer–retailer relationships beyond the relationship-building mechanism that has been the main focus of previous studies (Benbasat et al. 2008). The relationship states may conceptualize developmental stages to describe combinations of state variables and outcomes (Zhang et al. 2016). By integrating the nature of different states (e.g., transient or sticky states) and the influence of consumer–retailer interactions on the transit, we can understand how and when the distinctive online buying environment leads to either the progress or the deterioration of the consumer– retailer relationship (i.e., loyalty).

Second, our study is unique in that we quantify irrational decision factors, such as habit and loyalty, in explaining the linkage between the consumer–retailer relationship states and responses to price promotion. This allows us to understand how habitual purchases and loyalty to an online retailer develop.

Third, we compare the prediction ability of our HMM with that of a longitudinal, pattern-based trajectory model to understand a consumer’s decision situation in the online market. Our results show that the assumption “repeated same-decision context” outperforms “predetermined time-varying behaviors” (Mani and Nandkumar 2016) in explaining the dynamics of coupon utilization. This result supports approaches emphasizing period-specific temporal dynamics in data mining and recommender systems (Bogina et al. 2016).

Fourth and finally, prior work on online price promotion has mainly focused on online retailers specializing in at most one or two product categories, particularly those that are regularly purchased (e.g., nonperishable grocery items and drugstore items). Therefore, our understanding is limited to the impact of product brand-specific price promotion. We collected data showing the utilization of storewide discount coupons at a full-line online retailer and add to pricepromotion literature by quantifying the impact of storewide retailer price promotion of an online retailer selling products from diverse categories.

The rest of the paper is organized as follows. In the next section, we review the relevant studies. In Section 3, we develop our econometric model based on an HMM. In Section 4, we describe the data collected and behavioral measures examined in this study. In Section 5, we introduce the estimation procedure and discuss our empirical results. Finally, we offer conclusions and suggest future research directions.

## 2. Research Background

We provide an overview of the theoretical background pertaining to online consumers’ responses to price promotion and its dynamics. We also elaborate our research questions and discuss competing views on them, considering the extant theories and the unique decision-making context of the online market.

## 2.1. Online Buying Environment and Price Sensitivity

A large body of research has investigated the connection between the consumer–retailer relationship and price sensitivity. Most studies report that loyal customers react less sensitively to prices and are less responsive to limited-time price promotions (Bawa and Shoemaker 1987, Guadagni and Little 2008). However, some research has also produced conflicting evidence (Reinartz and Kumar 2000) and has identified contingencies (Krishnamurthi and Papatla 2003). For example, when an off-line retailer offers a special promotion on a specific day, some consumers will not make use of the promotion if the transaction costs on the specified day—including travel costs and shopping time—are larger than the amount of money to be saved (Chiang et al. 2001, Sain et al. 2010). Similarly, if a consumer is time-pressed on weekdays, then, given the potentially high opportunity cost of a shopping trip, that consumer can shop only on weekends, thus making for a regularity in interpurchase times and shopping days in the off-line market (Vakratsas and Bass 2002). By comparison, online consumers can make a purchase at any time of day if they have even a tiny time slot and Internet access, and so they can immediately respond to a promotion.

Information in the online market is much easier to access than that in the offline market. Online consumers can also easily check current promotions available, and thus, they can utilize price promotions either by actively accelerating purchase time to take advantage of a current price promotion or by deliber ately postponing a purchase until a price promotion is available. In sum, the increased shopping-time flexibility and easily accessible promotion information that characterize the online market can make consumers more responsive to price promotion.

Price comparison websites (i.e., Internet shopbots) help consumers acquire product and retailer information (e.g., price and seller reliability) and easily compare numerous online retailers. Given that information is practically costless in the online market, consumers have every incentive to make a well-informed decision. Consumers continue searching for a better product until the marginal cost of searching exceeds the marginal benefit (Hoque and Lohse 1999). Yet too many alternatives can cause a cognitive problem for consumers, resulting in information overload (Montgomery et al. 2004). The lowered search cost in the online market may remove the limited information acquisition problem for bounded rationality (Simon 1955). However, the limited information processing ability problem (i.e., sufficient information but too much to process), another reason for bounded rationality, may become more intensified. Johnson and Payne (1985) show that consumers are willing to trade off cognitive effort in the decision-making process against accuracy. When a consumer decides to switch online retailers, the consumer has to embrace other cognitive tasks, such as uncertainty about the new virtual retailer.

Given the intensified information overload and correspondingly increased cognitive costs, consumers are likely to form the habit of repeatedly buying at an online retailer and so become loyal customers. It is an interesting research question to empirically assess the competing forces in online consumers’ retailer choices: (1) rational decision making utilizing increased shoppingtime flexibility and easily accessible information and (2) irrational decision making because of loyalty and habitual choice. We need to trace the dynamics of price sensitivity over time to explore the formation of loyalty and/or habitual purchase. In the next section, we review the habitual behavior and loyalty-development process in selecting an online retailer.

## 2.2. Loyalty and Habitual Purchase at an Online Retailer

A fully rational consumer will buy at the online retailer offering the lowest price for the same product. However, a consumer’s decision may not be fully rational, and existing literature has established common behavioral biases, such as habit (Jeuland 1979). It is widely accepted that habit is formed through a learning process (Jog et al. 1999). As part of this learning process, desirable outcomes resulting from the previous decision(s) reinforce or increase the probability of the same choice at the next decision (Mowrer and Ullman 1945).

Loyalty is another biased behavioral process. In the traditional off-line market, customer loyalty is based primarily on satisfaction obtained from the consumption of a brand, superior product and service quality, or consumer trust in quality (Christodoulides and Michaelidou 2010). Reichheld et al. (2000) show that the basic structure of loyalty development in the off-line market also applies to online consumers. But all services in the online market are provided by a website interface notably lacking a human service agent; thus, the value of customer trust and the customer trust-building mechanism have received more attention for e-loyalty development (Kim and Peterson 2017). For example, although the appearance of the storefront and the positive presentation of service personnel are identified as antecedents of customer loyalty in the off-line setting (Sirohi et al. 1998), sufficient information, including online feedback reviews and the interactivity between a consumer and an online retailer have been shown to potentially affect e-loyalty (Srinivasan et al. 2002).

Irrational decisions resulting from loyalty and habit are made in the process of building the consideration set of online retailers. Consumers may intend to construct smaller consideration sets to (1) minimize costs of thinking, which are required in information processing, and to routinize their online buying behaviors (Chintagunta 1998); (2) reduce cognitive tasks/cost, including switching cost (e.g., the cognitive cost for a new sign-up and credit card registration and cognitive burdens, such as worry about and discomfort from a new online retailer) (Johnson et al. 2002); and (3) take advantage of loyalty programs provided by online retailers (Danaher et al. 2003). Online consumers can systematically routinize their online purchase processes by selecting an online retailer as the homepage in their web browser or bookmarking an online retailer as a favorite website. These kinds of facilitating tools lead to the habitual behavior of repeatedly buying at the same retailer.

We can conjecture about the different dynamics of coupon utilization at an online retailer, depending on the relationship between a consumer and the retailer. Once loyalty is formed and/or habitual choice is rou tinized, consumers will buy at a given retailer regardless of the price promotions available there, showing a lower level of coupon utilization over time. In contrast, it is expected that coupon utilization will be relatively high and/or increase over time for consumers without loy alty and habitual purchases because of learning effects for better utilization of price promotions.

## 2.3. Relationship Between Consumer and Retailer and Its Dynamics

Relationship is a broad notion that includes loyalty as well as other elements of an affective and cognitive nature. Exploratory research in relational behavior or relationship marketing has been conducted from diverse angles (e.g., a psychological view or a utilitarian decision maker’s perspective). In particular, it has been extensively studied in the literature of repurchase behavior and multibrand usage in relationship marketing (Aaker et al. 2004). Fournier (1998) identifies the factors contributing to a relationship (e.g., emotions, cognition, and commitment) and relates them to relationship stability and durability over time based on the interpersonal relationship metaphor.<sup>1</sup> Storbacka et al. (1994) consider a relationship to be a function of certain intrinsic factors (e.g., the history of the relationship, customer commitment and satisfaction).

Relationships evolve through distinct stages that exhibit different relational construct levels and varied outcome measures (Celuch et al. 2006). Aaker et al. (2004) argue that the continuation or interruption of a relationship depends on the interaction quality, particularly acts of transgression and brand personality. A successful interaction strengthens the relationship whereas a poorly performed one can lead to its breaking off. Netzer et al. (2008) suggest a stochastic modeling framework to understand relationship dynamics, which are formed by a series of interactions. Previous studies also identify the role of relationship states in measuring return on marketing investment (Luo and Kumar 2013) and quantifying the differential effectiveness of marketing strategies (Zhang et al. 2016).

## 3. Econometric Model

We build an HMM to describe the dynamics of the relationship between a consumer and an online retailer. The basic elements of an HMM are the finite set of hidden states characterizing online consumers $( \mathrm { e . g . }$ weak and strong consumer–retailer relationship states) and their statistical linkage to observed outcomes of coupon utilization, defined in Section 4.2. All other things being equal, the hidden states represent ordered levels in a consumer–retailer relationship: a higher state implicitly indicates a stronger or more intimate relationship. At any given time, a consumer is in one state. We conceptualize the dynamics of coupon utilization by allowing consumers to move across all the states over time, assuming that relationships evolve through several discrete levels (Dwyer et al. 1987, Oliver 1997). Figure 1 graphically illustrates the proposed HMM.

## 3.1. Transition Matrix

The proposed HMM consists of four main components: (1) Markovian transition probabilities among states, (2) initial state distribution, (3) covariate factors affecting transitions, and (4) covariate factors affecting statedependent coupon utilization. The transition matrix showing probabilities that a consumer moves from a given state to any of the others, $Q ( S _ { i t } , ~ S _ { i t + 1 } )$ , is defined as

$$
\begin{array}{r l} & Q (S _ {i t}, S _ {i t + 1}) \\ & \quad = \left( \begin{array}{c c c c c c} q (1, 1) & q (1, 2) & q (1, 3) & \dots & q (1, N - 1) & q (1, N) \\ q (2, 1) & q (2, 2) & q (2, 3) & \dots & q (2, N - 1) & q (2, N) \\ q (3, 1) & q (3, 2) & q (3, 2) & \dots & q (3, N - 1) & q (3, N) \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ q (N, 1) & q (N, 2) & q (N, 3) & \dots & q (N, N - 1) & q (N, N) \end{array} \right), \end{array}
$$

where $S _ { i t }$ is consumer $i ^ { \prime } \mathrm { s }$ consumer–retailer relationship state at time $t ; q ( c , n ) ,$ , an element of $Q ( S _ { i t } , S _ { i t + 1 } )$ , is the probability that a consumer moves from state c at time t to state n at time t+1: $\operatorname* { P r } ( S _ { i t + 1 } = n | S _ { i t } = c )$ . We assume that the transition from one state to another follows a Markov process; that ${ \mathrm { i } } \mathbf { s } ,$ the transitions between states are stochastically determined through the conditional transition probability to another state given the current state.

Assuming that the unobserved random part of expected utilities is independently and identically Gumbel (type 1 extreme value) distributed, we can model the transition probabilities following the ordered logit model (Greene 2011). Specifically, the term q( c, n) in the transition matrix could be written as

$$
\begin{array}{r l} & {q (c, 1) _ {i t} = \frac {\exp (\mu (1) _ {c} - \mathbf {x} _ {\mathrm{it}} ^ {\prime} \pmb {\beta} _ {c} - \delta_ {i})}{1 + \exp (\mu (1) _ {c} - \mathbf {x} _ {\mathrm{it}} ^ {\prime} \pmb {\beta} _ {c} - \delta_ {i})},} \\ & {q (c, n) _ {i t} = \frac {\exp (\mu (n) _ {c} - \mathbf {x} _ {i t} ^ {\prime} \pmb {\beta} _ {c} - \delta_ {i})}{1 + \exp (\mu (n) _ {c} - \mathbf {x} _ {i t} ^ {\prime} \pmb {\beta} _ {c} - \delta_ {i})}} \\ & {- \frac {\exp (\mu (n - 1) _ {c} - \mathbf {x} _ {i t} ^ {\prime} \pmb {\beta} _ {c} - \delta_ {i})}{1 + \exp (\mu (n - 1) _ {c} - \mathbf {x} _ {i t} ^ {\prime} \pmb {\beta} _ {c} - \delta_ {i})},} \end{array}
$$

and

$$
\begin{array}{c} q (c, N) _ {i t} = 1 - \frac {\exp (\mu (N - 1) _ {c} - \mathbf {x} _ {i t} ^ {\prime} \boldsymbol {\beta} _ {c} - \delta_ {i})}{1 + \exp (\mu (N - 1) _ {c} - \mathbf {x} _ {i t} ^ {\prime} \boldsymbol {\beta} _ {c} - \delta_ {i})} \\ \forall c \in \{1, 2, \ldots , N \} \text {and} \forall n \in \{2, \ldots , N - 1 \}. \end{array}
$$

We model the transitions between states as a threshold model, in which a transition to another state occurs if the propensity value passes a corresponding threshold As such, $\mu ( n ) _ { c }$ is the nth ordered logit threshold in state c. Given N states, we identify N<sup>−</sup>1 thresholds. As shown in the equations, a consumer’s transition probability is also stochastically affected by $\mathbf { x } _ { i t } ; \mathbf { x } _ { i t }$ is the covariate column vector of variables associated with consumer i at time t: (1) time-varying factors to capture interactions between a consumer and an online retailer and (2) an individual consumer’s demographic profile variables. If the aggregate propensity value with covariates is larger (smaller) than the threshold needed for a transition to a higher (lower) state, a consumer will transit accordingly. If the aggregate propensity value is neither large nor small enough for a transition, the customer will stay in the current state. $\beta _ { \mathrm { c } }$ is a vector of statedependent coefficients for $\mathbf { x } _ { i t }$ at state c. We allow the marginal effects of covariates to vary across states. $\delta _ { i }$ is a random effect term to control for consumer heterogeneity. The transition matrix is constant over time, meaning that consumers exhibit the same transition behaviors in every period; we test the validity of this assumption later in this paper. The symbols used throughout the paper and the variables they represent are listed in Table 1.

## 3.2. State-Dependent Coupon Utilization Distribution

We stochastically relate consumer–retailer relationship states to coupon utilization. We need to develop a regression model that is tailored for a situation in which coupon utilization is continuously measured on the standard unit interval between zero and one. We assume that coupon utilization is beta distributed. The beta distribution is very flexible for modeling proportions because its density can have quite different shapes depending on two parameter values. In particular, we use the beta regression model proposed by Ferrari and Cribari-Neto (2004). Consumer i’s coupon utilization at time t, conditional on a consumer–retailer relationship state $c \ ( y _ { i t | c } )$ is specified as

Figure 1. Hidden Markov Model for Online Consumer’s Coupon Utilization  
![](/api/attachments/JPXRFZFX/fulltext/images/c763e4cbdebfba90f396bac8f392d7bd4692a5a1d65828cd477c22ea81647713.jpg)

$$
\begin{array}{c} f (y _ {i t | c}) = \frac {\Gamma (\phi_ {c})}{\Gamma (\nu_ {c} \phi_ {c}) \Gamma ((1 - \nu_ {c}) \phi_ {c})} \big (y _ {(i t | c)} \big) ^ {(\nu_ {c} \phi_ {c} - 1)} (1 - y _ {i t | c}) ^ {(1 - \nu_ {c}) \phi_ {c} - 1}, \\ 0 <   y _ {i t | c} <   1, \end{array}
$$

where $\nu _ { \mathrm { c } }$ is the mean of coupon utilization at state $c \left( 0 < \nu _ { c } < 1 \right)$ and $\phi _ { c }$ can be interpreted as a dispersion parameter so that, for fixed $\nu _ { c } , \mathrm { ~ a ~ }$ larger value of $\phi _ { c }$ means a smaller variance of y <sub>|</sub> $( \phi _ { c } > 0 ) . ^ { 2 }$ 2

The beta regression model with covariates can be obtained by assuming that $\nu _ { c }$ is a function of covariates. Because the mean of coupon utilization is restricted to the interval [0, 1], we use the logit specification as follows: we plug the logit function $g ( \cdot )$ into $\nu _ { c }$ in the beta density-based coupon utilization distribution.

$$
g (\alpha_ {0 | c}, \pmb {\theta} _ {i t}, \pmb {\alpha} _ {c}, \chi_ {t}) = \frac {\exp (\alpha_ {0 | c} + \pmb {\theta} _ {i t} ^ {\prime} \pmb {\alpha} _ {c} + \chi_ {t})}{1 + \exp (\alpha_ {0 | c} + \pmb {\theta} _ {i t} ^ {\prime} \pmb {\alpha} _ {c} + \chi_ {t})},
$$

where $\alpha _ { 0 | c }$ is the state-specific intercept for state c, $\mathbf { \theta } _ { i t }$ is a covariate column vector related to coupon utilization, and $\alpha _ { c }$ is a vector of state-specific response coefficients for $\mathbf { \theta } _ { i t }$ at state $c .$ The coupon utilization regression model also includes a time fixed effects term $( \chi _ { t } )$ to control the potential fluctuation of the number of coupons provided over time.

The difference between the covariates affecting the transition probability $\left( \mathbf { x } _ { i t } \right)$ and the covariates affecting coupon utilization $( { \dot { \Theta } } _ { i t } )$ is in the over-time persistence of their impact. The first have an enduring impact on the consumer’s attitude, and the latter affect only shortterm choice behavior (Netzer et al. 2008). The difference is obvious in our context: $\mathbf { x } _ { i t }$ is hypothesized to have a general impact on consumer–retailer relationship states, and $\mathbf { \theta } _ { i t }$ is composed of the factors explaining the purchase situation, such as coupon availability and special needs for a coupon at time t.

## 3.3. State and Consumer Heterogeneity

The HMM allows consumers to be in different states, and so we account for consumer heterogeneity through the consumer–retailer relationship states at time t. We control for the state-specific unobserved effects with (1) the inclusion of state-specific threshold parameters, $\mu ( n ) _ { c . }$ , in the transition probability and (2) the inclusion of state-specific coefficients, $\alpha _ { 0 | c }$ , in the coupon utilization regression model, g( · ).

Still, there could be spurious state dependence associated with consumer heterogeneity (Heckman 1981, Keane 1997). That ${ \mathrm { i } } \mathbf { s } ,$ unobserved differences among observationally equivalent consumers may affect their relationship states and, correspondingly their coupon utilization. For example, if a consumer has a high opportunity cost for comparing prices across online retailers, that consumer is less likely to frequently switch online retailers. Our model includes an observable demographic profile (gender and age) and a random effects term (δ ) in the transition probability to control this kind of unobserved heterogeneity.

## 3.4. Stationary Initial State Distribution

For an HMM with a time-homogeneous transition matrix, the initial state distribution $( \pi ,$ a N×1 vector) is commonly defined as the stationary distribution of the transition matrix (MacDonald and Zucchini 1997). Because our transition matrix is a function of timevariant and -invariant covariates, we calculate the stationary distribution by solving the equation π πQ<sup>¯</sup> under the condition that the sum of elements of π is one, where Q<sup>¯</sup> is the transition matrix with the estimated parameters. Our data set enables us to observe an individual consumer’s first purchase event, and thus, our observation is not left censored. Therefore, we calculate π with all covariates set to zero. We confirm that there is a unique stationary distribution because all the estimated transition probabilities are positive and transition matrices are, thus, aperiodic and irreducible (Netzer et al. 2008).

Table 1. Variables and Operational Definitions

<table><tr><td>Variable</td><td>Operational definition</td></tr><tr><td> $i$ </td><td>Consumer index</td></tr><tr><td> $t$ </td><td>Time index (six-month period over four years, eight periods)</td></tr><tr><td> $S_{it}$ </td><td>Consumer  $i's$  consumer-retailer relationship state at time  $t$ ,  $\{1,2,\dots,N\}$ </td></tr><tr><td> $\pi$ </td><td>Initial state probability distribution</td></tr><tr><td> $Q(S_{it}, S_{it+1})$ </td><td>Transition matrix</td></tr><tr><td> $q(c, n)$ </td><td> $\Pr(S_{it+1} = n| S_{it} = c)$ ,  $c$  and  $n$  are state index (current, next)</td></tr><tr><td> $\mu(n)_c$ </td><td> $nth$  ordered logit threshold in state  $c$ </td></tr><tr><td> $x_{it}$ </td><td>Consumer  $i's$  covariate vector at time  $t$  affecting state transition</td></tr><tr><td> $\beta_c$ </td><td>Vector of state-dependent covariate coefficients for  $x_{it}$ </td></tr><tr><td> $\delta_i$ </td><td>Random effect term for consumer heterogeneity in state transition</td></tr><tr><td> $y_{it|c}$ </td><td>Consumer  $i's$  coupon utilization at time  $t$  conditional on state  $c$ </td></tr><tr><td> $v_c$ </td><td>Mean of the coupon utilization at state  $c$  ( $0 < v_c < 1$ )</td></tr><tr><td> $\phi_c$ </td><td>The dispersion parameter (or precision parameter) of coupon utilization at state  $c$  ( $\phi_c > 0$ )</td></tr><tr><td> $\theta_{it}$ </td><td>Consumer  $i's$  covariate vector at time  $t$  affecting coupon utilization</td></tr><tr><td> $\alpha_c$ </td><td>Vector of state-specific response coefficients for  $\theta_{it}$ </td></tr><tr><td> $\chi_t$ </td><td>Time fixed effect term in coupon utilization regression equation</td></tr><tr><td> $CouponUtilization_{it}$ </td><td>Consumer  $i's$  coupon utilization at time  $t$ , number of purchases with coupons over number of all purchases</td></tr><tr><td> $CumulativePurchaseVolume_{it-1}$ </td><td>Consumer  $i's$  cumulative purchase volume through time  $t-1$ </td></tr><tr><td> $PurchaseVolume_{it-1}$ </td><td>Consumer  $i's$  purchase volume at time  $t-1$ </td></tr><tr><td> $SavedMoney_{it-1}$ </td><td>Consumer  $i's$  savings from coupon at time  $t-1$ </td></tr><tr><td> $Gender_i$ </td><td>Gender</td></tr><tr><td> $Age_i$ </td><td>Age</td></tr><tr><td> $PurchaseVolume_{it}$ </td><td>Consumer  $i's$  purchase volume at time  $t$ </td></tr><tr><td> $AveragePrice_{it}$ </td><td>Average price of all the items purchased by consumer  $i$  at time  $t$ </td></tr></table>

$$
\begin{array}{r l} & {\mathrm{L} _ {i} = \mathrm{Pr} _ {i} (Y _ {i 1 | s _ {i 1}} = y _ {i 1 | s _ {i 1}}, Y _ {i 2 | s _ {i 2}} = y _ {i 2 | s _ {i 2}}, \ldots , Y _ {i T | s _ {i T}} = y _ {i T | s _ {i T}})} \\ & {= \sum_ {s _ {i T} = 1} ^ {N} \sum_ {s _ {i T - 1} = 1} ^ {N} \ldots \sum_ {s _ {i 1} = 1} ^ {N} \Bigg [ \mathrm{Pr} (S _ {i 1} = s _ {i 1}) \mathrm{Pr} (Y _ {i 1 | s _ {i 1}} = y _ {i 1 | s _ {i 1}} | S _ {i 1} = s _ {i 1})} \\ & {\qquad \cdot \Bigg [ \prod_ {t = 2} ^ {T} \mathrm{Pr} (S _ {i t} = s _ {i t} | S _ {i t - 1} = s _ {i t - 1})} \\ & {\qquad \cdot \mathrm{Pr} (Y _ {i t | s _ {i t}} = y _ {i t | s _ {i t}} | S _ {i t} = s _ {i t}) \Bigg ] \Bigg ].} \end{array}
$$

## 3.5. Likelihood of Sequence of Purchase Outcomes over Time

Because of the Markovian structure, the probability of the observed sequence of coupon utilization is calculated through all the paths of hidden states that an individual consumer could take over time. Accordingly, the joint likelihood is given by the sum over all possible routes for each sequence:

Following MacDonald and Zucchini (1997), we can rewrite the joint likelihood function in a matrix product as

$$
\begin{array}{c} \pi^ {\prime} \boldsymbol {\Delta} _ {i 1} \mathbf {Q} (S _ {i 1}, S _ {i 2}) \boldsymbol {\Delta} _ {i 2} \mathbf {Q} (S _ {i 2}, S _ {i 3}) \boldsymbol {\Delta} _ {i 3} \dots \mathbf {Q} (S _ {i T - 2}, S _ {i T - 1}) \boldsymbol {\Delta} _ {i T - 1} \\ \cdot \mathbf {Q} (S _ {i T - 1}, S _ {i T}) \boldsymbol {\Delta} _ {i T} \mathbf {1}, \end{array}
$$

where $\Delta _ { i 1 }$ is a N×N diagonal matrix whose diagonal elements are probabilities of observing coupon utilization at each state, $[ \mathrm { P r } ( y _ { i t | 1 } ) , \mathrm { P r } ( y _ { i t | 2 } ) , \cdots , \mathrm { P r } ( y _ { i t | N } ) ]$ and 1 is a N×1 vector of ones to convert the whole elements in the outer products of the matrices into a scalar value of likelihood. The parameter estimates are obtained by maximizing the likelihood function across all individual consumers in the sample.

## 4. Data and Measures

Our research site is one of the premier online retailers in South Korea. We collected the transaction data of 586 randomly selected consumers who had purchased at least one item every six months from July 2002 to June 2006. Irregular consumers are not included in our sample because their purchase history cannot provide enough information regarding changes in buying behavior. Because managers are more concerned with reg ular customers than with casual customers, this sample selection is unlikely to affect the managerial relevance of our empirical findings. The data show consumers, products, product prices, and purchase date information for all transactions, allowing us to fully trace an individual consumer’s purchase history. We additionally acquired consumers’ demographics (age and gender).

We develop and categorize key variables as (1) covariates affecting consumer–retailer relationship states, (2) coupon utilization, and (3) covariates for the coupon utilization regression model.

## 4.1. Covariates Affecting Consumer–Retailer Relationship State

With the growth of transaction data and the development of data-mining techniques, much research evaluates consumer–retailer relationships in view of consumer behavior. Relationships develop as a consequence of changes in interactions between partners in a relationship (Fournier 1998, Aaker et al. 2004). Specific interactions between a consumer and an online retailer could have a temporary and/or long-term impact on their relationship (Netzer et al. 2008). We measure the following interactions that may induce a change of consumer–retailer relationship and the consumer’s subsequent buying behavior at the retailer:

1. Cumulative purchase volume (CumulativePurchase-Volume<sub>it</sub>−<sub>1</sub>)

2. Recent purchase volume (RecentPurchaseVolume − )

3. Recent savings from coupons (SavedMoney − )

Intense, long-term connections are associated with an intimate relationship (Fournier 1998). According to Bhattacharya and Bolton (2000), cumulative satisfaction based on previous experiences and the assessment thereof reflects the nature of relationships. We measure consumer i’s cumulative purchase volume at an online retailer through time t<sup>−</sup>1 to calibrate the intensity of long-term interactions between a consumer and an online retailer.

It is obvious that how often a consumer has recently interacted with an online retailer affects their relationship. In practice, purchase frequency is one of the popular recency, frequency, monetary (RFM) components that previous studies have used in consumer relationship management and direct marketing. Specifically, they are commonly utilized in pattern mining for loyalty and brand choices (Simester et al. 2006).<sup>3</sup> We measure purchase volume during the previous period ( RecentPurchase $V o l u m e _ { i t - 1 } )$ to determine recent purchase frequency.

In our context, monetary value in the RFM model is highly correlated with purchase volume: their correlation coefficient is 0.887. Instead, we measure the savings from coupons at time $t – 1 \ ( S a v e d M o n e y _ { i t - 1 } )$ because consumers effectively utilizing price promotions have good impressions of an online retailer (Tybout and Scott 1983) and, accordingly, enjoy a feeling of intimacy with that retailer.

In addition to the interaction variables, our model includes Gender and $A g e _ { i }$ because one of the most important factors influencing a purchasing decision is a shopper’s demographic profile (Blaylock 1989).

## 4.2. Coupon Utilization

A vast amount of marketing literature shows that a coupon may serve many purposes, including sales increases and brand switching. One purpose is to serve as a means of price discrimination in which nonredeemers pay the full price for a product and redeemers pay a discounted price. Previous studies suggest that coupons attract less loyal consumers as is consistent with economic theories of price discrimination (e.g., Bawa and Shoemaker 1987, Chiang 1995) We examine consumer i’s coupon utilization at time $t \ ( C o u p o n U t i l i z a t i o n _ { i t } )$ as a purchase outcome measure, defined as follows:

$$
\text { CouponUtilization } _ {i t} = \frac {\text { Number   of   purchases   with   coupon } _ {i t}}{\text { Number   of   purchases } _ {i t}}.
$$

If consumers do not make habitual purchases at and have loyalty to an online retailer, they will buy at the retailer only when it has competitive prices, presumably with a coupon. As a result, they will exhibit high coupon utilization. After nonloyal consumers make a purchase with a coupon, they are likely to pursue other price promotions by actively accelerating or delaying the timing of their purchases, leading to increased coupon utilization as described by reference pricing (Mazumdar et al. 2005). By contrast, attitudinally loyal and/or habitual consumers may buy at an online retailer regardless of coupon availability, leading to low coupon utilization.

We confirm through interviews with category managers that the prices of the same product across rival retailers converge to a relatively similar range. Because retailers generally offer the same price for a product, the coupons offered to individual consumers play a pivotal role in price dispersion. Coupons can be classified depending on who offers them: the manufacturer or the retailer. Manufacturer coupons are distributed by the manufacturer. When a consumer uses the coupon, the manufacturer will ultimately pay for its value. In contrast, retailer coupons are offered by the retailer and are essentially retailer sales. Retailer coupons are generally brand-nonspecific coupons that offer storewide discounts. Because manufacturer coupons are available across all retailers in the same way, retailer coupons can make for price dispersion across retailers. Therefore, we measure CouponUtilization only with retailer coupons.

## 4.3. Covariates Affecting Coupon Utilization Regression Model

Because every consumer wants to save money with a coupon, the availability of coupons could cause an omitted variable bias. According to interviews with managers, our research site did not adopt any kind of one-to-one marketing activities, including coupon generation based on purchase history. Instead, individual consumers could earn reward points for their purchases without coupons and redeem the acquired reward points for coupons, for example, a storewide discount coupon of \$5. The reward points have a relatively short expiration date (e.g., one week), compared with our unit period of six months, and so coupon utilization at time t may be endogenous to the number of purchases during time t. We select current purchase volume (the number of purchases at time t) as one of the covariates in the coupon utilization regression model.

Table 2. Descriptive Statistics of Key Variables and Correlation Matrix

<table><tr><td>Variable</td><td>Mean</td><td>Standard deviation</td></tr><tr><td> $CouponUtilization_{it}$ </td><td>0.55</td><td>0.29</td></tr><tr><td> $\ln(CumulativePurchaseVolume_{it-1})$ </td><td>3.01</td><td>1.36</td></tr><tr><td> $\ln(SavedMoney_{it-1})$ </td><td>2.61</td><td>1.69</td></tr><tr><td> $\ln(PurchaseVolume_{it})$ </td><td>2.14</td><td>0.60</td></tr><tr><td> $\ln(AveragePrice_{it})$ </td><td>3.82</td><td>1.57</td></tr><tr><td> $Gender_i$ </td><td>0.19</td><td>0.45</td></tr><tr><td> $Age_i$ </td><td>37.90</td><td>7.77</td></tr></table>

Note. The number of consumers = 586, the number of periods = 8, the number of observations = 4,688, gender = 0 for female and 1 for male.

Online consumers have a different purchase decision process depending on product prices because they have to make purchase decisions with only digitally transferred information (Kim and Krishnan 2015). We develop AveragePrice (the average price of products that consumer i purchases at time t) to control for the potential price impact.

Our variables can be easily calculated from consumer i’s transaction data in a unit period. We need to decide the optimal length of the period for repeated behavior measures. In this study, we define a market basket as the set of items purchased in six months, making a sequence of six-month market baskets. We considered several alternatives (one month, three months, and six months). Both monthly and three-month market baskets are significantly affected by seasonality, for example, lunar-based New Year’s Day (January or February in the solar calendar), Parents’ Day (May), Korean Thanksgiving Day (August, September, or October in the solar calendar), and the holiday season (December). When considering shopping seasonality, a six-month market basket is appropriate because the first and second half-years have well-balanced peak seasons. In practice, we traced six-month sales and confirmed that they do not show up-and-down variations across periods, indicating that seasonality is controlled.

Some studies have suggested that behavioral measures are insufficient for measuring consumer attitudes such as loyalty because they may not distinguish between true attitudes and spurious attitudes that may result from a lack of available alternatives for consumers (Jacoby and Kyner 1973). Given that our data set contains four years of individual consumers’ purchase histories, a relatively long period of six months is expected to weaken the impact of these period-specific noises.

## 5. Empirical Results

## 5.1. Descriptive Statistics

Table 2 presents the descriptive statistics of key variables. We take log transformations of the variables because they are highly skewed. On average, online consumers purchased around 10 items and spent \$970 per period (six months). The average age of the consumers is 37.9. The correlation matrix is provided in Table 3. The significant and positive correlation coefficient between CouponUtilization and Ln(Cumu-$l a t i v e P u r c h a s e V o l u m e _ { i t - 1 } )$ indicates that, as consumers increase their online shopping experiences, their coupon utilization also increases. The table also shows that when online consumers purchase relatively expensive products, they are likely to buy them with a coupon, consistent with general expectations. Another interesting finding is that age is highly correlated with many variables, and gender is not correlated with any. Because the relationships shown in the table are

\*p < 0.01.

Table 3. Correlation Matrix

<table><tr><td>Variables</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>1.  $CouponUtilization_{it}$ </td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. ln(CumulativePurchaseVolume $_{it-1}$ )</td><td>0.3801*</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. ln(PurchaseVolume $_{it-1}$ )</td><td>0.2556*</td><td>0.8095*</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. ln(SavedMoney $_{it-1}$ )</td><td>0.1603*</td><td>0.5735*</td><td>0.6571*</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>5. ln(PurchaseVolume $_{it}$ )</td><td>0.0431*</td><td>0.1694*</td><td>0.2602*</td><td>0.1557*</td><td>1</td><td></td><td></td><td></td></tr><tr><td>6. ln(AveragePrice $_{it}$ )</td><td>0.2743*</td><td>0.7886*</td><td>0.7389*</td><td>0.6689*</td><td>0.1082*</td><td>1</td><td></td><td></td></tr><tr><td>7. Gender $_i$ </td><td>-0.0046</td><td>0.0039</td><td>0.0143</td><td>0.0041</td><td>0.0207</td><td>0.0056</td><td>1</td><td></td></tr><tr><td>8. Age $_i$ </td><td>-0.0402*</td><td>0.0241</td><td>0.0321</td><td>0.0672*</td><td>0.0531*</td><td>0.0465*</td><td>0.0157</td><td>1</td></tr></table>

Table 4. Model Selection Summary

<table><tr><td>State #</td><td>No. of parameters</td><td>State 1</td><td>State 2</td><td>State 3</td><td>State 4</td><td>Likelihood</td><td>BIC</td></tr><tr><td>2</td><td>29</td><td>34.5%</td><td>65.5%</td><td></td><td></td><td>-14,523.5</td><td>-14,615.9</td></tr><tr><td>3</td><td>40</td><td>10.9%</td><td>64.5%</td><td>24.6%</td><td></td><td>-14,355.0</td><td>-14,482.5</td></tr><tr><td>4</td><td>51</td><td>3.3%</td><td>15.7%</td><td>57.3%</td><td>23.7%</td><td>-14,338.0</td><td>-14,500.5</td></tr></table>

calculated at an aggregated level, we should be cautious of reaching any conclusions because we may need to control diverse heterogeneities and consider contingencies. We check whether they accurately represent the causal relationships based on our models, and if not, why not.

## 5.2. Model Selection

HMM is a semiparametric approach, and so the structure of model estimation is not fully predeterministic. One of the key steps in model estimation is the selection of the number of states that best fit the data. An N-state model is not nested within an N+1-state model, and it is, therefore, not appropriate to evaluate them with the likelihood ratio test. Instead, we rely on the Bayesian information criterion (BIC) to select the best model. We first fit a two-state model to data and then fit the data with the increased number of states in a stepwise manner until the BIC value decreases. Table 4 presents the likelihood and BIC values across the number of states, showing that the three-state model is the best fit.<sup>4</sup> The estimated initial probability distributions are also provided in the table.

We take a nonparametric method to account for unobserved consumer heterogeneity (Heckman and Singer 1984). This approach allows us to avoid any misspecification of a heterogeneity distribution, $\delta _ { i }$ . This involves approximating the underlying unknown probability distribution by a finite number of location points. We fit our model with three location points (zero, one, and a random number between zero and one) and their probabilities. We empirically confirm that the inclusion of three or more location points does not statistically significantly increase the BIC value. This finding indicates that the application of hidden states allows us to capture the substantial variations in coupon utilization. We can also infer that consumers clustered into the same consumer–retailer relationship state are highly homogenous.

## 5.3. Transition Across Consumer–Retailer Relationship States

We identify three distinctive states in a consumer– retailer relationship. We label these three states as “weak relationship,” “moderate relationship,” and “strong relationship” states. The initial state distribution, which is a stationary distribution, is 10.9%, 64.5%, and 24.6%, respectively.

Table 5 reports our estimation results. The feature of the identified states is primarily determined by the statespecific thresholds $( \mu ( 1 ) _ { c }$ and $\mu ( 2 ) _ { c } , c = 1 , 2 ,$ and 3) and the state-specific transition covariate coefficients $( \beta _ { \mathrm { { c } } } , c =$ 1, 2, and 3). The threshold for moving from state 1 to state 2 is <sup>−</sup>3.9131 $( p < 0 . 0 0 1 )$ , that for moving from state 1 to state 3 is 0.0348 $( p < 0 . 8 6 1 )$ , that for moving from state 2 to state 1 is <sup>−</sup>1.6530 $( p < 0 . 0 0 1 )$ ), that for moving from state 2 to state 3 is $3 . 7 6 2 7 \ ( p < 0 . 0 0 1 )$ , that for moving from state 3 to state 1 is <sup>−</sup>4.2350 $( p < 0 . 0 0 1 )$ , and that for moving from state 3 to state 2 is <sup>−</sup>0.9564 $( p < 0 . 0 0 1 )$ ). The state-specific intercepts in the coupon utilization regression models are $\bar { \alpha } _ { 0 | 1 } = 8 . 9 2 5 4 ( p < 0 . 0 0 1 ) , \alpha _ { 0 | 2 } = 1 . 3 5 1 2$ $( p < 0 . 0 0 1 )$ , and $\alpha _ { 0 | 3 } { = } { - } 7 . 0 6 7 4 \ ( p < 0 . 0 0 1 )$ ). We calculate the means of the estimated beta distributions at the mean values of all the covariates $( \Theta _ { i t }$ and $\chi _ { t } ) \mathrm { : } 0 . 9 3 8 2 ( p <$ 0.001), 0.5933 $( p < 0 . 0 0 1 )$ , and 0.0945 $( p < 0 . 0 0 1 )$ for weak, moderate, and strong relationship states, respectively; we utilize the delta method for their standard errors. Coupon utilization decreases as consumers move from states 1 to 2 to 3. Consumers in higher relationship states are less likely to buy with a coupon than those in lower relationship states, supporting our hypothesis on the negative relationship between consumer–retailer relationship and coupon utilization.

The state-specific dispersion parameters are $\phi _ { 1 } { = } 4 . 7 6 8 4$ $( p < 0 . 0 0 1 ) , \hat { \phi } _ { 2 } { = } 6 . 4 1 2 9 \hat { ( p < 0 . 0 0 1 ) }$ , and $\phi _ { 3 } { = } 2 . \dot { 6 } \dot { 5 } 6 6 ~ ( p <$ 0.001). We can calculate the shape parameters (h and k) of the beta distributions (see Table 5). Figure 2 shows the shapes of beta distributions representing state-specific coupon utilization. When consumers are not engaged at all with an online retailer, they are highly unlikely to buy without a coupon from that retailer. We can infer that they move around between online retailers to find the lowest price because nonloyal consumers are sensitive to prices when cross-store comparison is easy (Lynch and Ariely 2000).

The coefficients of gender in all three states are insignificant, indicating that gender does not affect transition across relationship states. All the coefficients of age are negative and significant, implying that coupon utilization decreases with age in all three states. Both findings are consistent with the correlation coefficients shown in Table 3. By contrast, Table 5 also shows a significant difference in some covariate effects across the three states, suggesting that the identification of hidden states can provide useful information for predicting coupon utilization. For example, the

Table 5. Estimation Results

<table><tr><td>Parameter</td><td>State 1 (weak relationship state)</td><td>State 2 (moderate relationship state)</td><td>State 3 (strong relationship state)</td></tr><tr><td rowspan="2"> $\mu(1)_c$  (First threshold for state c)</td><td>-3.9131***</td><td>-1.6530***</td><td>-4.2350***</td></tr><tr><td>(0.1174)</td><td>(0.0634)</td><td>(0.2813)</td></tr><tr><td rowspan="2"> $\mu(2)_c$  (Second threshold for state c)</td><td>0.0348</td><td>3.7627***</td><td>-0.9564***</td></tr><tr><td>(0.1983)</td><td>(0.1427)</td><td>(0.0901)</td></tr><tr><td rowspan="2"> $\alpha_{0|c}$  (Intercept in beta regression model)</td><td>8.9254***</td><td>1.3521***</td><td>-7.0674***</td></tr><tr><td>(0.0578)</td><td>(0.0164)</td><td>(0.1015)</td></tr><tr><td rowspan="2"> $\phi_c$  (Dispersion parameter of beta distribution)</td><td>4.7684***</td><td>6.4129***</td><td>2.6566***</td></tr><tr><td>(0.3537)</td><td>(0.1862)</td><td>(0.2888)</td></tr><tr><td rowspan="2">h (Shape parameter 1 of beta distribution)</td><td>4.4735***</td><td>3.8047***</td><td>0.2511***</td></tr><tr><td>(1.1940)</td><td>(0.5126)</td><td>(0.0320)</td></tr><tr><td rowspan="2">k (Shape parameter 2 of beta distribution)</td><td>0.2949***</td><td>2.6082***</td><td>2.4055***</td></tr><tr><td>(0.0818)</td><td>(0.3232)</td><td>(0.2000)</td></tr><tr><td rowspan="2">E[g(·)] (Mean of beta distribution)</td><td>0.9382***</td><td>0.5933***</td><td>0.0945***</td></tr><tr><td>(0.2240)</td><td>(0.0709)</td><td>(0.0045)</td></tr><tr><td rowspan="2">ln(CumulativePurchaseVolume $_{it-1}$ )</td><td>-0.0520</td><td>0.0189</td><td>-0.4751***</td></tr><tr><td>(0.0317)</td><td>(0.0177)</td><td>(0.0348)</td></tr><tr><td rowspan="2">ln(PurchaseVolume $_{it-1}$ )</td><td>-1.4119***</td><td>-0.0759*</td><td>0.5377***</td></tr><tr><td>(0.0596)</td><td>(0.0298)</td><td>(0.0563)</td></tr><tr><td rowspan="2">ln(SavedMoney $_{it-1}$ )</td><td>-0.0280</td><td>0.1657***</td><td>0.1356***</td></tr><tr><td>(0.0391)</td><td>(0.0208)</td><td>(0.0373)</td></tr><tr><td rowspan="2">Genderi</td><td>-0.5901</td><td>0.2285</td><td>-0.4959</td></tr><tr><td>(0.3089)</td><td>(0.1424)</td><td>(0.2806)</td></tr><tr><td rowspan="2">Agei</td><td>-0.3867***</td><td>-0.0677***</td><td>-0.2471***</td></tr><tr><td>(0.0353)</td><td>(0.0189)</td><td>(0.0330)</td></tr><tr><td rowspan="2">ln(PurchaseVolume $_{it}$ )</td><td>-1.6563***</td><td>0.0560***</td><td>1.6788***</td></tr><tr><td>(0.0210)</td><td>(0.0075)</td><td>(0.0370)</td></tr><tr><td rowspan="2">ln(AveragePrice $_{it}$ )</td><td>-0.3716***</td><td>-0.0118**</td><td>0.5187***</td></tr><tr><td>(0.0131)</td><td>(0.0037)</td><td>(0.0220)</td></tr><tr><td rowspan="2">Period 2 dummy</td><td></td><td>-2.0100***</td><td></td></tr><tr><td></td><td>(0.0442)</td><td></td></tr><tr><td rowspan="2">Period 3 dummy</td><td></td><td>-1.1034***</td><td></td></tr><tr><td></td><td>(0.0416)</td><td></td></tr><tr><td rowspan="2">Period 4 dummy</td><td></td><td>-0.9293***</td><td></td></tr><tr><td></td><td>(0.0388)</td><td></td></tr><tr><td rowspan="2">Period 5 dummy</td><td></td><td>-0.9662***</td><td></td></tr><tr><td></td><td>(0.0404)</td><td></td></tr><tr><td rowspan="2">Period 6 dummy</td><td></td><td>-1.1075***</td><td></td></tr><tr><td></td><td>(0.0412)</td><td></td></tr><tr><td rowspan="2">Period 7 dummy</td><td></td><td>-1.0470***</td><td></td></tr><tr><td></td><td>(0.0398)</td><td></td></tr><tr><td rowspan="2">Period 8 dummy</td><td></td><td>-1.1829***</td><td></td></tr><tr><td></td><td>(0.0417)</td><td></td></tr><tr><td>Observations</td><td></td><td>4,688</td><td></td></tr><tr><td>Likelihood</td><td></td><td>-14,355.0</td><td></td></tr></table>

Note. Standard errors are shown in parentheses.  
\*\*\*p < 0.001; \*\*p < 0.01; \*p < 0.05.

estimated coefficients for recent purchase volume, ln(PurchaseVolume − ) are positive and significant in state 3 $( 0 . 5 3 7 7 , p < 0 . 0 0 1 )$ but negative and significant for both states 1 and 2 (<sup>−</sup>1.4119, $p < 0 . 0 0 1$ and <sup>−</sup>0.0759, p < 0.05). The correlation coefficient between coupon utilization and recent purchase volume is positive and significant (0.2556, $p < 0 . 0 1 )$ ). While controlling for the hidden states, recent purchase volume can affect the transition probabilities either positively or negatively depending on the consumer–retailer relationship state. Also, the coefficients of cumulative purchase volume ln( CumulativePurchaseVolume − ), are insignificant in the weak and moderate relationship states but significant and negative in the strong relationship state.

Aside from the direct interpretation of estimated coefficients, we can calculate mean transition matrices by plugging the estimated coefficients and the mean values of covariates into transition probability equations. These matrices help us easily assess the covariate effects on transition probabilities. Table 6 demonstrates the mean transition matrices as well as the intrinsic propensity transition matrix with all the covariates at zero. The estimated transition probabilities between states are not symmetric.

Figure 2. (Color online) State-Specific Beta Probability Distribution of Coupon Utilization  
![](/api/attachments/JPXRFZFX/fulltext/images/271cacb77b9ab29d2e771a6ecff010033c6f2b51353873c1f0889aaa03054cbf.jpg)  
—Strong consumer-retailer relationship state

In principle, large diagonal elements in a transition matrix show that the states are sticky, which means that once a consumer enters a state, the consumer is likely to stay there. This implies that consumers’ buying behavior tends to be consistent over time. Off-diagonal elements show the transition probabilities across states. We can discuss the covariate effects separately and collectively by comparing the intrinsic transition matrix with the mean transition matrices.

The level of stickiness varies across the relationship states. According to the mean transition matrix encompassing all covariate effects, the likelihood that an online consumer remains in the moderate relationship state is the highest (83.2%), followed by that of remaining in the weak relationship state (67.5%). The behavior of inertia in the weak relationship state is weaker than in the moderate state. Once consumers reach the moderate relationship state, they are likely to stay in that state. Given the close ties between attitudinal loyalty and routines of behavior, we expect the two drivers to reinforce each other, leading to the sticky behavior in the moderate state. Because loyalty to a retailer is negatively related to consumers searches for alternatives (Srinivasan et al. 2002), loyal consumers buy at the same online retailer even when a coupon is not provided. Or the sticky behavior may result from habitual forces: after a consumer has chosen an online retailer as the consumer’s favorite site in the web browser, the consumer can easily visit and buy from there

Cumulative purchase volume does not affect transition probabilities for consumers in the weak and moderate relationship states. However, it substantially decreases the likelihood that consumers in the strong relationship state will remain in that state, from 72.2% to 38.4%. Accordingly, it increases the likelihood of consumers in the strong relationship state moving to the moderate (weak) relationship state from 26.3% to 55.9% (from 1.4% to 5.7%). This implies that online consumers in even the strong relationship state are likely to seek more coupons as they increase their online shopping experience. This runs counter to the result from the off-line market that long-term interaction strengthens the consumer–retailer relationship and, therefore, makes consumers less price-sensitive at the retailer. We believe that the increased price sensitivity induced by accumulated online shopping experience results from the change in online buying process. Online consumers can become proficient in better and more easily collecting online information as their online purchase experience increases (Hann and Terwiesch 2003, Kim and Krishnan 2015). The acquired information helps consumers make well-informed decisions with diverse alternatives rather than being confined only to one long-time retailer.

These results are partly consistent with Barnes’s (2000) finding that a series of frequent interactions over a considerable period of time may not be a sufficient condition for establishing a relationship with a customer. We infer from the results that the switching cost of online retailers is not prohibitively large. The switching behavior observed even after online consumers reach the strong relationship state also shows one aspect of the fierce price competition in the online market.

Table 6. Transition Matrix

<table><tr><td colspan="4">Intrinsic propensity transition</td><td colspan="4">Mean transition matrix (cumulative purchase volume)</td></tr><tr><td>t-1 → t</td><td>Weak</td><td>Moderate</td><td>Strong</td><td>t-1 → t</td><td>Weak</td><td>Moderate</td><td>Strong</td></tr><tr><td>Weak</td><td>2.0%</td><td>48.9%</td><td>49.1%</td><td>Weak</td><td>2.3%</td><td>52.5%</td><td>45.2%</td></tr><tr><td>Moderate</td><td>16.1%</td><td>81.7%</td><td>2.3%</td><td>Moderate</td><td>15.3%</td><td>82.3%</td><td>2.4%</td></tr><tr><td>Strong</td><td>1.4%</td><td>26.3%</td><td>72.2%</td><td>Strong</td><td>5.7%</td><td>55.9%</td><td>38.4%</td></tr><tr><td colspan="4">Mean transition matrix (recent purchase volume)</td><td colspan="4">Mean transition matrix (recent savings from coupons)</td></tr><tr><td>t-1 → t</td><td>Weak</td><td>Moderate</td><td>Strong</td><td>t-1 → t</td><td>Weak</td><td>Moderate</td><td>Strong</td></tr><tr><td>Weak</td><td>29.1%</td><td>66.4%</td><td>4.5%</td><td>Weak</td><td>2.1%</td><td>50.6%</td><td>47.3%</td></tr><tr><td>Moderate</td><td>18.4%</td><td>79.7%</td><td>1.9%</td><td>Moderate</td><td>11.1%</td><td>85.5%</td><td>3.5%</td></tr><tr><td>Strong</td><td>0.5%</td><td>10.4%</td><td>89.2%</td><td>Strong</td><td>1.0%</td><td>20.2%</td><td>78.8%</td></tr><tr><td colspan="4">Mean transition matrix (gender)</td><td colspan="4">Mean transition matrix (age)</td></tr><tr><td>t-1 → t</td><td>Weak</td><td>Moderate</td><td>Strong</td><td>t-1 → t</td><td>Weak</td><td>Moderate</td><td>Strong</td></tr><tr><td>Weak</td><td>2.2%</td><td>51.5%</td><td>46.3%</td><td>Weak</td><td>6.7%</td><td>72.1%</td><td>21.2%</td></tr><tr><td>Moderate</td><td>15.5%</td><td>82.2%</td><td>2.4%</td><td>Moderate</td><td>19.3%</td><td>78.9%</td><td>1.8%</td></tr><tr><td>Strong</td><td>1.6%</td><td>28.2%</td><td>70.3%</td><td>Strong</td><td>3.2%</td><td>43.3%</td><td>53.5%</td></tr><tr><td colspan="8">Mean transition matrix (all covariates)</td></tr><tr><td>t-1 → t</td><td>Weak</td><td>Moderate</td><td>Strong</td><td></td><td></td><td></td><td></td></tr><tr><td>Weak</td><td>67.5%</td><td>31.6%</td><td>0.9%</td><td></td><td></td><td></td><td></td></tr><tr><td>Moderate</td><td>14.2%</td><td>83.2%</td><td>2.6%</td><td></td><td></td><td></td><td></td></tr><tr><td>Strong</td><td>3.2%</td><td>43.8%</td><td>53.0%</td><td></td><td></td><td></td><td></td></tr></table>

Recent purchase volume substantially changes the intrinsic transition matrix by strengthening the behavior of inertia overall. For consumers in both the weak and strong relationship states, the likelihood of staying in the same relationship state noticeably increases along with recent purchase volume, from 2.1% to 29.1% for the weak relationship state and from 72.2% to 89.2% for the strong relationship state. The results indicate that the increase in recent purchase volume does not induce nonloyal consumers to increase loyalty. Rather, consumers in the weak relationship state form a habit of buying only with a coupon or of buying whenever a coupon is available along with an increase in recent purchase volume—mostly with coupons. For consumers in the strong relationship state, by contrast, an increase in recent purchase volume strengthens loyalty toward the retailer and/or the habit of buying without a coupon.

In sum, the managerial meaning of an increase in recent purchase volume at an online retailer is contingent on the relationship state. The increased purchase volume signifies that the retailer may be, at least temporarily, the primary retailer of high priority to consumers in the strong relationship state regardless of coupon availability. On the other hand, consumers in the weak relationship state perceive a retailer as one of several whose price they need to check. As a result, the identified relationship state can be utilized to customize marking mix strategies.

Focusing on the period of interactions between a consumer and an online retailer, our results show that recent interactions can be helpful for reinforcing the relationship level but that long-term interactions cannot. Even though their positive impact is limited to consumers in the strong relationship state, we may suggest that managers of online retailers pay attention to recent changes in the consumer’s buying behaviors rather than the long-term trend of the consumer’s purchase behavior. To verify this conclusion, we build and assess a longitudinal trend-based model for predicting coupon utilization in Section 5.5.

Recent savings from coupons also increase the likelihood of consumers remaining in the same state for consumers in the moderate and the strong states (from 81.7% to 85.5% for state 2 and from 72.9% to 78.4% for state 3). By contrast, savings do not affect the transition probabilities for consumers in the weak relationship state. These findings clearly show that consumers perceive savings differently, depending on their relationship states. Before a consumer–retailer relationship has developed to the moderate level, price promotion does not change consumers’ perception of the retailer; consumers seem to take savings for granted. However, if consumers reach the moderate and above states, they are likely to stay in (transit to) the stronger relationship states as they earn more savings from coupons. This implies that price promotion can strengthen consumers’ loyalty only for at least moderately loyal consumers whereas it is not effective for changing nonloyal consumers’ attitudes toward an online retailer (i.e., from nonloyal to loyal).

The mean transition matrix reflecting gender effects is similar to the intrinsic transition matrix, and the intrinsic transition matrix substantially changes when age effects are added. Consumers in the moderate and strong relationship states have decreased likelihood of staying in the same state at the mean level of age, from 81.7% to 78.9% for the moderate state and from 72.2% to 53.5% for the strong state; on the other hand, for consumers in the weak state, the likelihood increases from 2.0% to 6.7%. Older consumers are less likely to develop a strong relationship with an online retailer; they are more sensitive to price promotion. In our data set, people in their 30s and 40s account for more than 80% of all consumers, and the 95th percentile is 42 in age. Therefore, the estimation results are mainly based on comparisons between people in their 20s and people in their late 30s or 40s. The results imply that people in their late 30s and 40s are more likely than people in their 20s to make rational decisions through price comparison rather than irrational decisions because of loyalty and habitual choices.

## 5.4. Control Variables in Coupon Utilization

Our results show the monotonic marginal impacts of current purchase volume, ln(PurchaseVolume ) on coupon utilization across three states. The coefficients of ln(PurchaseVolume ) are <sup>−</sup>1.6563 (p < 0.001), 0.0560 $( p <$ 0.001), and 1.6788 $( p < 0 . 0 0 1 )$ for states 1, 2, and $^ { 3 , }$ respectively. A negative (positive) coefficient means that the increase in current purchase volume decreases (increases) coupon utilization. As described in the data section, our research site did not differentiate coupon promotion according to an individual consumer’s transaction history during our data period. Instead, consumers could earn reward points from the purchase without a coupon and redeem accumulated reward points for a coupon (redeemed coupon).<sup>5</sup> Consumers in the weak relationship state tend to buy only when a coupon is available and are, thus, less likely to have redeemed coupons. As a result, their coupon utilization decreases as their purchase volume increases, conditional on the limited number of randomly offered coupons. By contrast, consumers in the higher relationship states become more likely to have a higher number of redeemed coupons as they buy more without coupons, leading to increased coupon utilization.

We also find similar monotonic marginal impacts of average price, ln(AveragePrice ), on coupon utilization. Their coefficients $\mathrm { a r e - \bar { 0 . 3 7 1 6 } } \ ( p < 0 . 0 0 \bar { 1 } ) , - 0 . 0 1 1 8 \ ( p <$ 0.001), and 0.5187 $( p < 0 . 0 0 1 )$ for weak, moderate, and strong relationship states, respectively. For consumers in the strong relationship state, an increase in average price, in turn, increases coupon utilization. We can understand this based on the general economic observation that consumers try to utilize a coupon when they purchase expensive products. In particular, they can save more with a percentage-off coupon. By contrast, for consumers in the lower relationship states, an increase in average price decreases coupon utilization, indicating that when they purchase more expensive products, they do so without coupons. We conjecture that potential price dispersion across online retailers explains this observation. If nonloyal consumers in the weaker relationship states buy an expensive product at a retailer, the retailer must have a competitive price against other rival retailers even if a coupon is not applied.

## 5.5. Repeated Same-Decision Context vs.

## Longitudinally Updated Decision Contex

The HMM implicitly assumes that online consumers face the same decision context in every period. In the modeling, the same transition matrix and state-dependent outcome distributions are repeatedly applied to every period. However, consumers’ current purchase decisions can be a function of their previous purchase trajectory, leading to longitudinal purchase patterns. These two underlying assumptions on repeated decision context have developed into two distinctive models: (1) HMM and (2) the trajectory model. We examine which assumption better describes the dynamics of online consumers’ coupon utilization by comparing the prediction ability of HMM to that of the trajec tory model.

Trajectory analysis is a cluster-based approach to identifying distinctive groups of individual trajectories within a given population (Nagin 2005). Trajectory analysis models the linkage between time and behavior by allowing for polynomial relationships. A cubic relationship is given as follows:

$$
\begin{array}{r} y _ {i t} = \beta_ {0} ^ {j} + \beta_ {1} ^ {j} \mathrm{period} _ {i t} + \beta_ {2} ^ {j} \mathrm{period} _ {i t} ^ {2} + \beta_ {3} ^ {j} \mathrm{period} _ {i t} ^ {3} \\ + \alpha_ {1} ^ {j} \mathrm{TVC-1} _ {i t} + \ldots + \alpha_ {n} ^ {j} \mathrm{TVC-k} _ {i t} + \varepsilon_ {i t}, \end{array}
$$

where $y _ { i t }$ is a consumer $i ^ { \prime } \mathrm { s }$ coupon utilization at time t given membership in group j; $\beta _ { m } ^ { j }$ denotes coefficients of the trajectory equation of group j. We can calculate the probability of $y _ { i t } ,$ conditional on group j membership, $\mathrm { P r } _ { j } ( y _ { i t } )$ , by assuming a specific distribution (e.g. a censored normal distribution). Given that $\mathbf { Y } _ { \mathrm { i } } ,$ [y<sub>i1</sub>, $y _ { i 2 } , . . . , y _ { i T } ]$ denotes the longitudinal sequence of $y _ { i t }$ during a finite $T$ period, $\mathrm { P r } _ { j } ( \mathbf { Y } _ { \mathrm { i } } )$ , the probability of observing $\mathbf { Y } _ { \mathrm { i } } ,$ conditional on group j membership, is formulated as $\begin{array} { r } { \operatorname* { P r } _ { j } ( \mathbb { Y } _ { i } ) = \prod _ { t } \operatorname* { P r } _ { j } ( y _ { i t } ) } \end{array}$ . The unconditional probability of observing $\mathbf { Y } _ { i }$ is the sum across the J groups of the probability of observing $\mathbf { Y } _ { i }$ given membership in group j, weighted by the proportion of the population in group $j , \eta _ { j } .$ Assuming conditional independence of $y _ { i t }$ across consumers over $T ,$ the likelihood of the entire sample is $L = \prod \left( \sum _ { j } \left( \eta _ { j } \mathrm { P r } _ { j } ( \mathbf { Y } _ { i } ) \right) \right)$ . The model parameters may differ from cluster to cluster. In particular, by permitting $\beta _ { m } ^ { j }$ to vary freely, the model allows us to identify the shape of the trajectory of each group. We can add time-varying covariates (TVC) as control variables.

We adopt a holdout test procedure, which is very common in evaluating forecasting. The model-fit (calibration) period is between July 2002 and December 2005, and a holdout (validation) sample includes transactions from January 2006 to June 2006. We treat the holdout sample as unknown future edges.

For the HMM, we can calculate the probability that a consumer is in propensity state c at time $t \ ( \check { S } _ { i t } )$ by dividing the probability of the consumer residing in that state through all paths of hidden states up to time t by the likelihood of the observed feature sequence up to time t (Hamilton 1989). For a consumer’s state, we select the state with the largest probability. Given the probabilistically determined state, we calculate the mean of the state-dependent coupon utilization. For the trajectory model, the estimated trajectory equations based on the calibration period are used to predict consumers’ coupon utilization in the validation period.<sup>6</sup>

Given the real data and the predicted coupon utilization from both the HMM and the trajectory model, we compare their prediction abilities using (1) root-mean-square error (RMSE) and (2) the better prediction rate. Table 7 summarizes the experimental results, which overall corroborate the superiority of the HMM’s predictive ability. The RMSE shows that the improvement of the HMM over the trajectory model is 45%. The HMM predicts consumers’ coupon utilization more closely than the trajectory model does (67% versus 33%). The better predictive fit of the holdout sample is observed in all three states.

It is not our intention through this experiment to show that the HMM would universally be the best-performing forecast of coupon utilization. We aim to empirically assess two conflicting assumptions common in behavior dynamics: (1) repeated same-decision context and (2) longitudinally updated decision context. We can infer from the prediction comparison that coupon utilization is vulnerable to diverse situational factors, particularly in the online market; thus, mean models based on timevarying patterns may be stochastically volatile.

## 6. Conclusion, Limitations, and Future Research Directions

Our findings on the difference in online consumers promotional responses, which we theoretically explain through different levels of inertial behavior based on loyalty and habitual force depending on consumer– retailer relationship states, give us valuable managerial insights.

Table 7. Predictive Ability Comparison Between HMM and Trajectory Model

<table><tr><td>Measure</td><td>HMM</td><td>Trajectory model</td></tr><tr><td>RMSE</td><td>0.121</td><td>0.220</td></tr><tr><td>Better prediction rate</td><td>67%</td><td>33%</td></tr><tr><td>Better prediction rate at state 1</td><td>73%</td><td>27%</td></tr><tr><td>Better prediction rate at state 2</td><td>61%</td><td>39%</td></tr><tr><td>Better prediction rate at state 3</td><td>75%</td><td>25%</td></tr></table>

We acquire understanding of the evolutionary path of the consumer–retailer relationship in the online market through transition probabilities across the identified relationship states. For the mean transition matrix with all covariate effects, the moderate relationship state is highly sticky (83.2%) compared with the other states whereas the probability of moving from a moderate state to a weak state is around six times higher than that of moving from a moderate state to a strong one. Also, the probability of remaining in a weak relationship state is higher than that of remaining in a strong relationship state (67.5% versus 53.0%). As a result, neither staying in nor transitioning to a strong relationship state is sustainable behavior, and so consumers are likely to move back from a higher state to the lower states. Our transition matrix is time-dependent and is, therefore, updated every period by incorporating the variations of the time-varying variables. We can calculate the state distribution at each period by repeatedly multiplying the mean transition matrix with all covariate effects. The probability of remaining in a strong relationship state converges to 4.2%. Given the small likelihood of staying in a high loyalty state, online retailers should design marketing strategies to make consumers stay in moderate and higher relationship states. Our findings on the positive influence of recent interactions in strengthening a consumer–retailer relationship provide a basis for such a strategy.

An important component of our work is that it seeks to evaluate two common underlying assumptions of behavior dynamics. The experimental comparison provides us with significant new insight into how to segment online consumers. The HMM accounts for consumer heterogeneity by differentiating the latent states to which consumers belong. Consumer–retailer relationship-based segmentation turns out to be effective in predicting online consumers’ coupon utilization even if the approach cannot address the comparability problem over time (Adomavicius and Tuzhilin 2005).

The present study has certain limitations that need to be taken into account when considering it and its contributions. Some of these limitations can be seen as avenues for future research.

First, managers must be interested in how to utilize knowledge about the distinctive consumer–retailer relationship states. They can develop a marketing strategy customized according to the relationship states. Some studies have already examined how companies should set overall prices, apply price discrimination, and promote prices in a manner that depends on the loyalty of their customer base (Caminal and Claici 2007). Future research with more sophisticated models addressing operational tactics could widen the applications of our understanding.

Second, our data set shows the full history of an individual consumer’s online transactions, but our observations are limited to one online retailer in a competitive market. As we mentioned, substantial price dispersion across competing online vendors is highly unlikely, and thus, our results should not be biased. However, online buying behavior across multiple online retailers would be an edifying research direction.

Third, coupons offer either a percentage discount or fixed savings on some or all items (e.g., 10% off one item and \$5 off your purchase above \$50). Category managers stated that they created both types of retailer coupons in similar proportions. Unfortunately, our data set does not allow us to discern the types of coupons. Price promotion literature shows that different price framings may have different effects on deal perception and purchase decisions (Krishna et al. 2002). Khan et al. (2009) also show that the customization of promotions (e.g., adjusting the optimal type) leads to a significant increase in profits. Further research could attempt to assess potential differences in promotion effects and so contribute to price-promotion optimization in the online market.

Fourth and finally, it would be very interesting to examine how coupons affect shopping basket structures and customer profitability in the online market. Because of limited data availability, it was not possible to research these effects in this study. However, knowledge regarding both these areas would help us better judge the impact of promotions on customer profitability and their appropriateness as a customer management tool.

## Endnotes

<sup>1</sup> Most previous work on relationships focuses on the relationship between a consumer and a product brand. However, the main concept and its development mechanisms are naturally extended to the context of consumer–retailer (seller) relationships (e.g., Bhattacharya and Bolton 2000).

$^ 2 \mathrm { W e }$ can derive Ferrari and Cribari-Neto’s (2004) beta regression model by setting $\nu _ { c } = h / ( h + k )$ and $\phi _ { c } = ( h + k )$ in the usual beta density expression $\begin{array} { r } { f ( y _ { i t | c } ) = \frac { \Gamma ( h + k ) } { \Gamma ( h ) \Gamma ( k ) } y _ { i t | c ^ { ( h - 1 ) } } ( 1 - y _ { i t | c } ) ^ { ( k - 1 ) } } \end{array}$

<sup>3</sup> Because our data set contains consumers who had regularly purchased at the online retailer, recency is highly homogeneous. Therefore, we do not include recency-related measures, such as interpurchase time, in our regression model. However, Recent PurchaseVolume − might indirectly reflect the concept of recency.

<sup>4</sup> AIC and Bayes factor provide the same evaluation result.

<sup>5</sup> In the data set, we cannot distinguish redeemed coupons from randomly provided coupons.

## References

Aaker J, Fournier S, Brasel SA (2004) When good brands do bad. J. Consumer Res. 31(1):1–16.

Adomavicius G, Tuzhilin A (2005) Towards the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. IEEE Trans. Knowledge Data Engrg. 17(6): 734–749.

Arora N, Dreze X, Ghose A, Hess JD, Iyengar R, Jing B, Joshi Y, et al. (2008) Putting one-to-one marketing to work: Personalization, customization and choice. Marketing Lett. 19(3/4):305–321.

Barnes JG (2000) Secrets of Customer Relationship Management: It’s All About How You Make Them Feel (McGraw-Hill, New York).

Bawa K, Shoemaker RW (1987) The coupon-prone consumer: Some findings based on purchase behavior across product classes. J. Marketing 51(4):99–110.

Benbasat I, Gefen D, Pavlou PA (2008) A research agenda for trust in online environments. J. Management Inform. Systems 24(4):275–286.

Bhattacharya CB, Bolton RN (2000) Relationship marketing in mass marketing. Sheth JN, Parvatyar A, eds. Handbook of Relationshi Marketing (Sage Publications, Thousands Oaks, CA), 327–354.

Blaylock JR (1989) An economic model of grocery shopping frequency. Appl. Econom. 21(6):843–852.

Bogina V, Kuflik T, Mokryn O (2016) Learning item temporal dynamics for predicting buying sessions. Proc. 21st Internat. Conf. Intelligent User Interfaces (ACM, New York), 251–255.

Brynjolfsson E, Smith MD (2000) Frictionless commerce? A comparison of Internet and conventional retailers. Management Sci. 46(4):563–585.

Caminal R, Claici A (2007) Are loyalty-rewarding pricing schemes anti-competitive? Internat. J. Indust. Organ. 25(4):657–674.

Celuch KG, Bantham JH, Kasouf CJ (2006) An extension of the marriage metaphor in buyer–seller relationships: An exploration of individual level process dynamics. J. Bus. Res. 59(5): 573–581.

Chiang J (1995) Competing coupon promotions and category sales Marketing Sci. 14(1):105–122.

Chiang J, Chung CF, Cremers ET (2001) Promotions and the pattern of grocery shopping time. J. Appl. Statist. 28(7):801–819.

Chintagunta PK (1998) Inertia and variety seeking in a model of brand-purchase timing. Marketing Sci. 17(3):253–270.

Christodoulides G, Michaelidou N (2010) Shopping motives as antecedents of e-satisfaction and e-loyalty. J. Marketing Managment 27(1–2):181–197.

Danaher PJ, Wilson IW, Davis RA (2003) A comparison of online and offline consumer brand loyalty. Marketing Sci. 22(4):461–476.

Dwyer FR, Schurr PH, Oh S (1987) Developing buyer-seller relationships. J. Marketing 51(2):11–27.

Ferrari S, Cribari-Neto F (2004) Beta regression for modelling rates and proportions. J. Appl. Statist. 31(7):799–815.

Fournier S (1998) Consumers and their brands: Developing relationship theory in consumer research. J. Consumer Res. 24(4):343–373.

Greene WH (2011) Econometric Analysis, 7th ed. (Prentice Hall, Englewood Cliffs, NJ).

Guadagni PM, Little JD (2008) A logit model of brand choice calibrated on scanner data. Marketing Sci. 27(1):29–48.

Hamilton J (1989) A new approach to the economic analysis of nonstationary time series and the business cycle. Econometrica 57(2):357-384

Hann IH, Terwiesch C (2003) Measuring the frictional costs of online transactions: The case of a name-your-own-price channel. Management Sci. 49(11):1563–1579.

Heckman JJ (1981) The incidental parameters problem and the problem of initial conditions in estimating a discrete time-discrete data stochastic process. Manski CF, McFadden DL, eds. Structural Analsis of Discrete Data with Econometric Applications (MIT Press, Cambridge, MA), 114–178.

Heckman J, Singer B (1984) A method for minimizing the impact of distributional assumptions in econometric models for duration data. Econometrica 52(2):271–320.

Hoque AY, Lohse, GL (1999) An information search cost perspective for designing interfaces for electronic commerce. J. Marketing Res. 36(3):387–394.

Jacoby J, Kyner DB (1973) Brand loyalty vs. repeat purchasing behavior. J. Marketing Res. 10(1):1–9.

Jeuland AP (1979) Brand choice inertia as one aspect of the notion of brand loyalty. Management Sci. 25(7):671–682.

Jog MS, Kubota Y, Connolly CI, Hillegaart V, Graybiel AM (1999) Building neural representations of habits. Science 286(5445): 1745–1749.

Johnson EJ, Payne JW (1985) Effort and accuracy in choice. Man agement Sci. 31(4):395–414.

Johnson EJ, Bellman S, Lohse G (2002) Cognitive lock in and the power law of practice. J. Marketing 67(2):62–75.

Keane MP (1997) Modeling heterogeneity and state dependence in consumer choice behavior. J. Bus. Econom. Statist. 15(3):310–327.

Khan R, Lewis M, Singh V (2009) Dynamic customer management and the value of one-to-one marketing. Marketing Sci. 28(6):1063–1079.

Kim Y, Krishnan R (2015) On product-level uncertainty and online purchase behavior: An empirical analysis. Management Sci. 61(10):2449–2467.

Kim Y, Peterson RA (2017) A meta-analysis of online trust relationships in e-commerce. J. Interactive Marketing 38:44–54.

Krishna A, Briesch R, Lehmann, DR, Yuan, H (2002) A meta-analysis of the impact of price presentation on perceived savings. J. Retailing 78(2):101–118.

Krishnamurthi L, Papatla P (2003) Accounting for heterogeneity and dynamics in the loyalty–price sensitivity relationship. J. Retailing 79(2):121–135.

Lal R, Sarvary M (1999) When and how is the Internet likely to decrease price competition? Marketing Sci. 18(4):485–503.

Luo A, Kumar V (2013) Recovering hidden buyer–seller relationship states to measure the return on marketing investment in business-to-business markets. J. Marketing Res. 50(1):143–160.

Lynch JG, Ariely D (2002) Wine online: Search costs affect competition on price, quality, and distribution. Marketing Sci. 19(1): 83–103.

MacDonald IL, Zucchini W (1997) Hidden Markovand Other Models fo Discrete-Valued Time Series (Chapman & Hall, London).

Mani D, Nandkumar A (2016) The differential impacts of markets for technology on the value of technological resources: An

application of group-based trajectory models. Strategic Management J. 37(1):192–205.

Mazumdar T, Raj SP, Sinha I (2005) Reference price research: Review and propositions. J. Marketing 69(4):84–102

Montgomery AL, Hosanagar K, Krishnan R, Clay KB (2004) De signing a better shopbot. Management Sci. 50(2):189–206.

Mowrer OH, Ullman AD (1945) Time as a determinant in integrative learning. Psych. Rev. 52(2):61–90

Nagin DS (2005) Group-Based Modeling of Development (Harvard University Press, Cambridge, MA).

Netzer O, Lattin JM, Srinivasan V (2008) A hidden Markov model of customer relationship dynamics. Marketing Sci. 27(2):185–204.

Oliver RL (1997) Satisfaction: A Behavioral Perspective on the Consumer (McGraw-Hill, New York)

Reichheld FF, Markey RGJ, Hopton C (2000) E-customer loyalty: Applying the traditional rules of business for online success. Eur. Bus. J. 12(4):173–179.

Reinartz WJ, Kumar V (2000) On the profitability of long-life customers in a noncontractual setting: An empirical investigation and implications for marketing. J. Marketing 64(4):17–35.

Saini R, Rao RS, Monga A (2010) Is that deal worth my time? The interactive effect of relative and referent thinking on willingness to seek a bargain. J. Marketing 74(1):34–48.

Simester DI, Sun P, Tsitsiklis JN (2006) Dynamic catalog mailing policies. Management Sci. 52(5):683–696.

Simon HA (1955) A behavioral model of rational choice. Quart. J. Econom. 69(1):99–118.

Sirohi N, McLaughlin EW, Wittink DR (1998) A model of consumer perceptions and store loyalty intentions for a supermarket retailer. J. Retailing 74(2):223–245.

Srinivasan SS, Anderson R, Ponnavolu K (2002) Customer loyalty in e-commerce: An exploration of its antecedents and consequences. J. Retailing 78(1):41–50.

Storbacka K, Strandvik T, Gronroos C (1994) Managing customer¨ relationships for profit: The dynamics of relationship quality. Internat. J. Service Indust. Management 5(5):21–38.

Tybout AM, Scott CA (1983) Availability of well-defined internal knowledge and the attitude formation process: Information aggregation versus self-perception. J. Personality Soc. Psych. 44(3):474–479.

Vakratsas D, Bass FM (2002) The relationship between purchase regularity and propensity to accelerate. J. Retailing 78(2):119–129.

Zhang JZ, Watson GF IV, Palmatier RW, Dant RP (2016) Dynamic relationship marketing. J. Marketing 80(5):53–75.

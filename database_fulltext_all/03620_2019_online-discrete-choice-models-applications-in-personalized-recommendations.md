---
otero_id: 3620
otero_key: "9DA723BH"
title: "Online discrete choice models: Applications in personalized recommendations"
authors: "Mazen Danaf; Felix Becker; Xiang Song; Bilge Atasoy; Moshe Ben-Akiva"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.02.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Online discrete choice models: Applications in personalized recommendations

![](/api/attachments/9DA723BH/fulltext/images/23edcf3136df60fcc33f5171b1f50ef6e0bee6a53805e7ebb452ebd60ae6afbf.jpg)

Mazen Danaf<sup>a,⁎</sup>, Felix Becker<sup>b</sup>, Xiang Song<sup>b</sup>, Bilge Atasoy<sup>c</sup>, Moshe Ben-Akiva<sup>d</sup>

<sup>a</sup> Massachusetts Institute of Technology, Department of Civil and Environmental Engineering, 77 Massachusetts Avenue, Room 1-181, Cambridge, MA 02139, United States of America

<sup>b</sup> Massachusetts Institute of Technology, Department of Civil and Environmental Engineering, United States of America

<sup>c</sup> Delft University of Technology, Department of Maritime and Transport Technology, Netherlands

<sup>d</sup> Massachusetts Institute of Technology, Department of Civil and Environmental Engineering, Room 181, United States of America

## A R T I C L E I N F O

Keywords: Personalization Intra-consumer heterogeneity Hierarchical Bayes Preference updates, recommender systems

## A B S T R A C T

This paper presents a framework for estimating and updating user preferences in the context of app-based recommender systems. We specifically consider recommender systems which provide personalized menus of options to users. A Hierarchical Bayes procedure is applied in order to account for inter- and intra-consumer heterogeneity, representing random taste variations among individuals and among choice situations (menus) for a given individual, respectively. Three levels of preference parameters are estimated: population-level, individual-level and menu-specific. In the context of a recommender system, the estimation of these parameters is repeated periodically in an ofline process in order to account for trends, such as changing market conditions. Furthermore, the individual-level parameters are updated in real-time as users make choices in order to in corporate the latest information from the users. This online update is computationally eficient which makes it feasible to embed it in a real-time recommender system. The estimated individual-level preferences are stored for each user and retrieved as inputs to a menu optimization model in order to provide recommendations. The proposed methodology is applied to both Monte-Carlo and real data. It is observed that the online update of the parameters is successful in improving the parameter estimates in real-time. This framework is relevant to various recommender systems that generate personalized recommendations ranging from transportation to e-commerce and online marketing, but is particularly useful when the attributes of the alternatives vary over time.

## 1. Introduction

Personalization has gained increasing interest among researchers and practitioners in the past two decades. Greater ease in data collection about users has made it possible for service providers to recommend items, services, and content in a non-intrusive way [1] through online recommendations. The conventional recommendation techniques, which mainly rely on item and user profiles, produce rat ings that do not take full advantage of the available data. On the other hand, discrete choice models, which have been rarely used in online recommendations, integrate item specific, user specific, and contextual data in a single model [11].

According to Jiang et al. [23], the use of discrete choice models in recommender systems can address some limitations associated with the standard recommendation approaches. The first limitation is the tradeof between relevancy and diversity [23,38]. The second limitation is that both metrics (relevancy and diversity), which are commonly used to measure the degree of matching. do not necessarily explain user preferences. On the other hand, discrete choice models directly measure the individual-specific utility of an alternative (or a set of alternatives) as a function of its attributes (without the need to measure relevancy or diversity separately). Finally, and unlike most standard recommendation techniques, discrete choice models can be applied even when the universal set from which alternatives are recommended and the alternative attributes vary over time. This is because the utility of each alternative is represented as a function of its attributes. For example, in travel recommendations, the travel time, cost, and availability of the diferent alternatives might vary over time.

This paper presents a methodology for estimating discrete choice models online, which can be used in updating user preferences continuously in an app-based setting such as recommender systems. The framework presented in this paper utilizes the Hierarchical Bayes (HB)

estimator proposed by Becker et al. [6] and Ben-Akiva et al. [7] which accounts for inter- and intra-consumer heterogeneity. An ofline-online procedure is proposed in which individual-specific parameters are updated after each choice without the need to re-estimate the whole model. Periodically, data from multiple individuals are pooled, and population level parameters are updated by re-estimating the model with the new data.

This paper addresses important gaps associated with using discrete choice models in recommender systems:

Online estimation: Although discrete choice models have been used in some recommender systems [11,23], the applications were mostly ofline because updating individual-level preferences requires re-estimating the entire model (which becomes computationally burdensome as the sample size, number of attributes, or number of alternatives increases). On the other hand, many online applications (such as recommender systems, personalized advertisement, etc.) require updating individual preferences in real-time. With infrequent preference updates, users' most recent choices might not be taken into consideration in generating personalized recommendations. The proposed online methodology therefore en ables us to use the most up-to-date preferences for recommendations without computational constraints.

Advanced level of heterogeneity: The existing few online applications of discrete choice models in recommender systems were based on multinomial or nested logit/probit models, which do not account for preference heterogeneity. Such models can only be used in nonpersonalized recommendations. On the other hand, logit mixture models (which account for heterogeneity) cannot be estimated in real-time because estimation requires integration over multidimensional distributions (in Maximum Likelihood Estimation), or drawing from complex posteriors (in Hierarchical Bayes methods). Applications of logit mixture models were also limited to interconsumer heterogeneity, and assumed that preferences are stable over time. The proposed methodology accounts for more complex patterns of heterogeneity (inter- and intra-consumer heterogeneity), which improves the quality of predictions and recommendations [7,33].

Identification of individual preferences: Other studies have cali brated choice models on the individual level. However, this method also has limitations since it requires a suficiently large number of observations per user. When limited data per user is available, a good prior on the individual-specific parameters is needed. To the best of our knowledge, specifying a good prior has not been adequately addressed in the literature. In our proposed methodology, the online estimation procedure overcomes this issue since it is comparable to estimating models at the individual level, but with good priors which are obtained from the ofline HB estimator.

In order to validate this methodology, Monte Carlo data on the choice of grapes and real stated preferences (SP) data on the choice of transport mode in Switzerland [9] are used. Individual preferences are estimated and updated using repeated observations, and then used in predicting the next choice and generating personalized recommendations. While our applications focus on personalized recommendations, this methodology allows discrete choice models to be applied online in various real-time applications and decision support systems such as personalized advertisement, real-time forecasting, personalized tolling, and others.

The remainder of this paper is organized as follows: Section 2 presents an overview of online recommendations and recent applications of discrete choice models in this domain. Section 3 presents the proposed methodology for estimating and updating user preferences on line. Section 4 presents an application of this methodology to Monte Carlo data. Section 5 presents a similar application to real SP data. Section 6 presents a discussion of the modeling approach and its applications in online recommendations, and Section 7 concludes.

## 2. Background

## 2.1. Online recommendations

The goal of online recommendations is to suggest items of interest to a user from a much larger set in order to handle information overload [11,23,28]. Personalized recommender systems must deliver relevant and precise recommendations based on each user's tastes and preferences, which should be determined with minimal involvement from the user. Recommendations must also be delivered in real-time so users are able to act immediately [11].

According to Ansari et al. [5], online recommendations can make use of several information sources including the individual's expressed preferences or choices among diferent alternatives, preferences for product attributes, other people's preferences or choices, expert judgments, and individual characteristics that may predict these preferences and choices.

Collaborative filtering and content-based filtering are the two most popular recommendation techniques. Other techniques include knowledge-based and context-aware methods [28]. Collaborative fil tering [14] provides recommendations to an individual based on overlapping interests with other individuals. In other words, it mimics ‘word-of-mouth’ recommendations. Content-based techniques match the attributes of the user profile against the attributes of an item [28]. These techniques make recommendations similar to those a given user has liked in the past [11]. Knowledge- or utility-based recommender systems base their recommendations on the computation of the utility of each item for the user [21]. These systems utilize previous knowl edge about users, items, and the utility function [28]. Context-aware recommender systems (CARS) account for contextual information such as the user's knowledge level (e.g. expert user or beginner), the time a recommendation is requested, and the external context (e.g. proximity of restaurants to the user) [28]. Other techniques have been proposed that utilize traditional machine learning techniques such as support vector machines and latent class models [12] and multi-armed bandit methods [24,30].

Despite the significant advances in online recommendations, several theoretical and practical challenges have been identified. For example, Ziegler et al. [38] showed that the commonly used top-N lists do not necessarily map user satisfaction and utility. In some cases, measuring the (expected) utility of recommendations may be more important than measuring the accuracy of recommendations [16,38]. Another major challenge is that the commonly used recommendation techniques are designed to consider diferent configurations as diferent items [28]. Therefore, very few of these techniques can be applied when the universal set from which items are recommended varies over time (as in the case of travel advisers, where the attributes of alternatives such as time and cost vary over time).

Using discrete choice models in personalized recommendations overcomes many of the limitations mentioned above. First, these models represent utility as a function of the attributes of items (or alternatives), and the individual preferences towards each of these attributes. Therefore, utility is not inferred from measures of similarity obtained from item or user profiling. Second, since utility is modeled as a function of attributes, this method is able to handle cases where new items (with known attributes) could be recommended (e.g. items that have not been chosen or rated before), and cases where the attributes vary over time. The researcher decides on the specification of the utility functions, which may include the attributes, the individual preferences for attributes, contextual variables, and individual characteristics, thus making use of all the available data. Third, since the users' preferences are inferred from their previous choices, this reduces the burden on users because they are not required to rate or evaluate any items. Finally, this method is able to deal with diversification and the ex ploration-exploitation problem using simple extensions described in Section 6.2.

## 2.2. Econometric and discrete choice models in recommender systems

Discrete choice models are often used to predict choices on an aggregate level. More recently these models have been utilized in recommender systems due to their ability to predict individual choices [11,23,27].

Chaptini [11] utilized discrete choice models to predict choices on the individual level and provide personalized recommendations. He developed an online academic advisor for MIT students that recommends academic courses based on observed and latent attributes of the courses (e.g. dificulty, workload, overall impression, etc.). These attributes were expressed as functions of students' characteristics (such as gender, degree program, etc.). The model was estimated using maximum likelihood estimation with data collected via an online revealed preferences (RP)/stated preferences (SP) survey. He then conditioned on the individual choices to find individual-level parameters that were used in generating course recommendations. In this study, preferences were estimated ofline for each student and not updated as more choices were observed. In addition, the behavioral model accounted for inter-consumer heterogeneity only (and ignored intra consumer heterogeneity).

Jiang et al. [23] used discrete choice models to measure users' preferences towards an entire recommendation list. The goal was to identify a recommendation list with the highest choice probability. A multi-level nested multinomial logit model was proposed, and the re commendation problem was formulated as a nonlinear binary integer programming problem. The authors noted that unlike typical recommender systems, discrete choice models introduce product diversity in the proposed recommendations. The main limitation of this approach was the lack of personalization, since a nested logit model was used (this model can be estimated at the individual level only if a large number of choices per individual is available).

Rubin and Steyvers [29] introduced a probabilistic model of the process by which an individual selects and later rates an item. This model was applied to movie rating data collected by Netflix. A Latent Dirichlet Allocation (LDA) model was used to model the probability of selecting a movie given a set of movies classified by topic. An ordered logit model was used to model movie ratings. This model included an individual-specific bias term which determines the general tendency of a user to give favorable ratings, however, it did not account for heterogeneity in the other parameters (preferences). In addition, since all parameters are learnt through Markov-Chain Monte Carlo methods, this model can only be run ofline.

Ansari et al. [5] proposed a Hierarchical Bayes approach for a recommender system that accounts for unobserved heterogeneity in user preferences, unobserved product heterogeneity and attributes (such as holistic consumer judgements and product appeal structures), and ex pert judgements. Customer ratings were modeled as a function of product attributes, customer characteristics, and expert evaluations. User preferences were expressed as a function of fixed efects (i.e. observed customer and movie variables and their interactions) and random ef fects pertaining to the customer. The model was applied to movie recommendations on the internet and estimated using MCMC. The main advantage of this paper was accounting for various sources of in formation (i.e. movie genres, expert evaluations, and socio-demographic characteristics). The authors also suggested diferent extensions which are included in this paper. First, preferences can be learnt from implicit rather than explicit information (i.e. revealed preferences or actual choices). Second, more complex forms of heterogeneity can be considered. This model also cannot be estimated online because of the excessive running times.

Our methodology extends the abovementioned studies by estimating models that account for personalization, and yet can be estimated online after each choice. Our model also accounts for complex forms of user heterogeneity, and uses only implicit data (observed choices) in order to estimate and update user preferences.

## 2.3. User heterogeneity and personalization

According to Castells et al. [10], user preferences are complex, dynamic, context-dependent, heterogeneous, and even contradictory. Therefore, accounting for consumer heterogeneity is crucial in recommender systems. Most of the methods mentioned earlier account, either directly or indirectly, for inter-consumer heterogeneity. On the other hand, limited research has been done on intra-consumer taste heterogeneity, representing taste variation among diferent choices done by the same individual. For example, in travel recommendations (such as the one presented in Section 5), the same user might be more or less sensitive to travel time depending on various unobserved factors specific to the particular choice situation, such as his/her schedule, the trip purpose, weather conditions, etc.

According to Ben-Akiva et al. [7], ignoring intra-consumer heterogeneity assumes a nearly neoclassical consumer with “permanent” individual preferences. Perturbations in these preferences are treated as nuisance factors. In the presence of multiple observations from each individual, it is possible to identify inter- and intra-consumer heterogeneity. In the context of discrete choice models, excluding intra-consumer heterogeneity when its efect is significant will result in biases due to a greater degree of unobserved efects [7].

Models with inter- and intra-consumer heterogeneity have been estimated by Hess and Train [20], Yáñez et al. [37] and Hess and Rose [19] using maximum simulated likelihood (MSL). These studies investigated taste variations among diferent choices done by the same individual, and demonstrated that accounting for such efects results in better estimates. However, these studies were mainly exploratory and limited to ofline applications, and estimation was computationally burdensome. Becker et al. [6] and Ben-Akiva et al. [7] introduced a Hierarchical Bayes (HB) estimator for such models by extending the standard HB procedure for logit mixture [2,36]. This model significantly reduces the computation time compared to the previously used MSL estimators. All of these studies presented methods to estimate choice models with inter- and intra-consumer heterogeneity ofline, and did not address online applications.

In the following sections, a novel framework is proposed that utilizes discrete choice models in estimating and updating individual level preferences in an online setting, building on the HB estimator proposed by Becker et al. [6] and Ben-Akiva et al. [7]. This framework can be used in various applications, but is particularly useful in recommender systems. The estimated preferences account for both inter- and intraconsumer heterogeneity, and are updated in real-time after each choice. They can serve as input to an assortment optimization algorithm, which recommends personalized menus to users by maximizing an objective function (e.g. the probability of choosing an alternative from the menu, the expected revenue of the menu, etc.).

## 3. Methodology

This section explains the methodology for estimating and continuously updating population-level and individual-level preferences. The Hierarchical Bayes estimator of a logit mixture model with interand intra-consumer taste and scale heterogeneity proposed by Becker et al. [6] is used in order to estimate these preferences. Inter- and intraconsumer heterogeneity are used to improve the estimation results, and thus the predictive capabilities of the choice models [7]. Individualspecific coeficients, which can be extracted from the estimation procedure, are used for personalization.

## 3.1. Estimating preferences

We consider the case whereby individual n $( \mathtt { n } = 1 , 2 , \dots \mathtt { N } )$ is presented with a menu m $( \mathbf { m } = 1 , 2 , \ldots \mathbf { M } _ { \mathrm { n } } )$ and makes a choice among a set of alternatives $( \mathbf { j } = 1 , \ 2 , \dots , \quad \mathbf { J _ { m n } } )$ . Thus, each menu refers to a choice situation. The total number of individuals is N and the total number of menus presented to each individual is $\mathbf { M } _ { \mathrm { n \ell } }$ . The number of parameters to be estimated is denoted by T.

In order to estimate user preferences, we use the HB estimator proposed by Becker et al. [6], which extends the widely used 3-step HB estimator of logit mixture [36] to a 5-step estimator in order to account for intra-consumer heterogeneity.

We assume the utility specification of choice j in menu m presented in Eq. (1):

$$
\mathrm {U_ {jmn}} = \frac {1}{\exp (\alpha_ {\mathrm{mn}})} (- \mathrm {P_ {jmn}} + \mathrm {X_ {jmn}} \eta_ {\mathrm{mn}}) + \epsilon_ {\mathrm{jmn}}\tag{1}
$$

where $\mathrm { \Delta P _ { j m n } }$ is the price of alternative j in menu m faced by individual n (with its coeficient fixed $\mathrm { ~ \ t o ~ } - 1 )$ ), $\mathrm { U } _ { \mathrm { j m n } }$ is individual n's unobserved utility of alternative j in menu m, $\Chi _ { \mathrm { i m n } }$ represents a vector of individual characteristics and alternative attributes, η represents a vector of coeficients/preferences, ${ \bf { a } } _ { \mathrm { { m n } } }$ is a scale parameter for individual n in menu m, and $\epsilon _ { \mathrm { j m n } }$ is an error term following the extreme value distribution. The subscripts (mn) in $\boldsymbol \eta _ { \mathrm { m n } }$ and ${ \bf { a } } _ { \mathrm { { m n } } }$ indicate that these coeficients might vary among individuals and among choice situations of the same individual respectively.

The model uses the Willingness-to-Pay space notation defined by Ben-Akiva et al. [7], whereby the price coeficient is fixed $\mathbf { t o } \_ { - 1 }$ Therefore, all other coeficients represent the willingness-to-pay for the corresponding attributes. Since the price coeficient is fixed, the scale parameter $\alpha _ { \mathrm { m n } }$ can be estimated.

We start by defining three levels of parameters needed to account for both inter- and intra-consumer heterogeneity as proposed by Ben Akiva et al. [7]:

1. Population-level parameters μ and $\itOmega _ { b } \mathrm  : \Omega _ { b } \mathrm { : \Omega _ { b } \mathrm { : \Omega _ { e } \mathrm { : \Omega _ { e } \mathrm { : \Omega _ { e } \mathrm { : \Omega _ { e } \mathrm { : \Omega _ { e } \mathrm { : \Omega _ { e } \mathrm { : \Omega _ { e } \mathrm { : \Omega _ { e } \mathrm { : \Omega _ { e } \mathrm { : \Omega _ { e } \mathrm { : \Omega _ { e } \mathrm { : \Omega _ { e } \mathrm { : \Omega } _ { e } \mathrm { : \Omega } } } } } } } } } } } } } }$ represent the average tastes/ preferences in the population and the inter-consumer covariance matrix respectively.

2. Individual-level parameters $\zeta _ { n }$ and $\varOmega _ { w } \dot { \mathbf { \cdot } }$ represent the average tastes/ preferences of a specific individual and the intra-consumer covariance matrix respectively.

3. Menu-specific parameters $\eta _ { m n } \mathrm { : }$ reflect the tastes/preferences specific to each choice situation.

We assume that $\zeta _ { \mathrm { n } }$ and $\boldsymbol \eta _ { \mathrm { m n } }$ are normally distributed:

$$
\eta_ {\mathrm{mn}} \sim \mathcal {N} _ {\mathrm{T}} (\zeta_ {\mathrm{n}}, \Omega_ {\mathrm{w}})\tag{2}
$$

$$
\zeta_ {\mathrm{n}} \sim \mathcal {N} _ {\mathrm{T}} (\mu , \Omega_ {\mathrm{b}})\tag{3}
$$

The probability of a sequence of choices $( d _ { n } )$ made by individual n can be expressed as:

$$
\begin{array}{l} \mathrm{P} (d _ {\mathrm{n}} | \mu , \Omega_ {\mathrm{b}}, \Omega_ {\mathrm{w}}) \\ = \int_ {\zeta_ {\mathrm{n}}} \prod_ {\mathrm{m} = 1} ^ {\mathrm{M} _ {\mathrm{n}}} \left[ \int_ {r _ {\mathrm{mn}}} \prod_ {\mathrm{j} = 1} ^ {\mathrm{J} _ {\mathrm{mn}}} \mathrm{P} _ {\mathrm{j}} (\eta_ {\mathrm{mn}}) ^ {d _ {\mathrm{jmn}}} \mathrm{H} (\mathrm{d} \eta_ {\mathrm{mn}} | \zeta_ {\mathrm{n}}, \Omega_ {\mathrm{w}}) \right] \mathrm{F} (\mathrm{d} \zeta_ {\mathrm{n}} | \mu , \Omega_ {\mathrm{b}}) \end{array}\tag{4}
$$

where ${ \dot { \mathbf { d } } } _ { \mathrm { j m n } }$ is equal to one if individual n chooses alternative j in menu m and zero otherwise, and:

$$
\mathrm{P} _ {\mathrm{j}} (\eta_ {\mathrm{mn}}) = \frac {\exp (\mathrm{V} _ {\mathrm{jmn}} (\eta_ {\mathrm{mn}}))}{\sum_ {\mathrm{j} ^ {\prime} = 1} ^ {\mathrm{J} _ {\mathrm{mn}}} \exp (\mathrm{V} _ {\mathrm{j} ^ {\prime} \mathrm{mn}} (\eta_ {\mathrm{mn}}))}\tag{5}
$$

$$
\mathrm{H} (\mathrm{d} \eta_ {\mathrm{mn}} \mid \zeta_ {\mathrm{n}}, \Omega_ {\mathrm{w}}) \sim \mathcal {N} _ {\mathrm{T}} (\zeta_ {\mathrm{n}}, \Omega_ {\mathrm{w}})\tag{6}
$$

$$
\mathrm{F} (\mathrm{d} \zeta_ {\mathrm{n}} \mid \mu , \Omega_ {\mathrm{b}}) \sim \mathcal {N} _ {\mathrm{T}} (\mu , \Omega_ {\mathrm{b}})\tag{7}
$$

The posterior distribution is presented in Eq. (8):

$$
\begin{array}{l} \mathrm{K} (\mu , \zeta_ {\mathrm{n}} \forall \mathrm{n}, \eta_ {\mathrm{mn}} \forall \mathrm{mn}, \Omega_ {b}, \Omega_ {\mathrm{w}} | d) \\ \propto \prod_ {\mathrm{n} = 1} ^ {\mathrm{N}} \left[ \prod_ {\mathrm{m} = 1} ^ {\mathrm{M} _ {\mathrm{n}}} \left[ \prod_ {\mathrm{j} = 1} ^ {\mathrm{J} _ {\mathrm{mn}}} [ \mathrm{P} _ {\mathrm{j}} (\eta_ {\mathrm{mn}}) ^ {d _ {\mathrm{jmn}}} ] \mathrm{h} (\eta_ {\mathrm{mn}} | \zeta_ {\mathrm{n}}, \Omega_ {\mathrm{w}}) \right] \mathrm{f} (\zeta_ {\mathrm{n}} | \mu , \Omega_ {\mathrm{b}}) \right] \mathrm{k} (\Omega_ {\mathrm{w}}) \mathrm{k} \\ (\mu) \mathrm{k} (\Omega_ {\mathrm{b}}) \end{array}
$$

where:

(8)

$$
\mathrm{k} (\mu) \sim \mathcal {N} _ {\mathrm{T}} (\mu_ {0}, \mathrm{A})\tag{9}
$$

$$
\mathrm{k} (\Omega_ {\mathrm{b}}) \sim \mathrm{IW(T,I)}\tag{10}
$$

$$
\mathrm{k} (\Omega_ {\mathrm{w}}) \sim \mathrm{IW} (\mathrm{T}, \mathrm{I})\tag{11}
$$

μ represents a vector of prior means, A is a diagonal covariance matrix with diagonal values →∞ (uninformative prior), T is the number of unknown parameters, I is the T-dimensional identity matrix, and IW (T,I) represent an Inverse Wishart distribution with T degrees of freedom and parameter I.

The model is estimated using the five-step Gibbs sampling procedure proposed by Ben-Akiva et al. [7] and Becker et al. [6]. This procedure is explained below:

Step I: drawing from the population means by drawing from the conditional posterior:

$$
\mathrm{K} (\mu \mid \zeta_ {\mathrm{n}} \forall \mathrm{n}, \eta_ {\mathrm{mn}} \forall \mathrm{mn}, \Omega_ {\mathrm{w}}, \Omega_ {\mathrm{b}}) \propto \mathrm{f} (\zeta_ {\mathrm{n}} \forall \mathrm{n} \mid \mu , \Omega_ {\mathrm{b}}) \mathrm{k} (\mu)\tag{12}
$$

The conditional posterior on μ is $\mathcal { N } \left( \overline { { \zeta } } ^ { \mathrm { i - 1 } } , \frac { \Omega _ { \mathrm { b } } ^ { \mathrm { i - 1 } } } { \mathrm { N } } \right)$ (where i is an iteration index) where:

$$
\overline {{\zeta}} = \frac {1}{N} \sum_ {n} \zeta_ {n} ^ {i - 1}\tag{13}
$$

Step II: drawing from the population-level covariance matrix by drawing from the conditional posterior:

$$
\mathrm{K} (\Omega_ {\mathrm{b}} \mid \mu , \zeta_ {\mathrm{n}} \forall \mathrm{n}, \eta_ {\mathrm{mn}} \forall \mathrm{mn}, \Omega_ {\mathrm{w}}) \propto \mathrm{f} (\zeta_ {\mathrm{n}} \forall \mathrm{n} \mid \mu , \Omega_ {\mathrm{b}}) \mathrm{k} (\Omega_ {\mathrm{b}})\tag{14}
$$

The conditional posterior on $\Omega _ { \mathrm { b } }$ is Inverted Wishart with $\mathrm { ~ T ~ } + \mathrm { ~ N ~ }$ degrees of freedom and parameter $\Gamma \mathrm { I } + \mathrm { N } \overline { { \mathrm { V } } } _ { \mathrm { b } } ,$ , where T is the number of unknown parameters, I is the T-dimensional identity matrix, and:

$$
\overline {{\nabla}} _ {\mathrm{b}} = \frac {1}{N} \sum_ {n = 1} ^ {N} (\zeta_ {n} ^ {i - 1} - \mu^ {i}) (\zeta_ {n} ^ {i - 1} - \mu^ {i}) ^ {\prime}\tag{15}
$$

Step III: drawing from the individual-level covariance matrix by drawing from the conditional posterior:

$$
\mathrm{K} (\Omega_ {\mathrm{w}} \mid \mu , \zeta_ {\mathrm{n}} \forall \mathrm{n}, \eta_ {\mathrm{mn}} \forall \mathrm{mn}, \Omega_ {\mathrm{b}}) \propto \mathrm{h} (\eta_ {\mathrm{mn}} \forall \mathrm{mn} \mid \zeta_ {\mathrm{n}} \forall \mathrm{n}, \Omega_ {\mathrm{w}}) \mathrm{k} (\Omega_ {\mathrm{w}})\tag{16}
$$

Given $\displaystyle \eta _ { \mathrm { m n } } ^ { \mathrm { ~ \normalfont ~ i - 1 ~ } }$ and $\zeta _ { \mathrm { n } } ^ { \mathrm { ~ i - 1 ~ } }$ for all $\mathbf { n } ,$ the conditional posterior on $\Omega _ { \mathrm { v } }$ is Inverted Wishart with degrees of freedom $\mathrm { T } + \mathrm { M } _ { \mathrm { t } }$ and parameter $\mathrm { \frac { T I + M _ { t } \overline { { V } } _ { W } } { T + M _ { t } } }$ , where $\mathbf { M } _ { \mathrm { t } }$ represents the total number of menus faced by all individuals, and:

$$
\overline {{\mathrm{V}}} _ {\mathrm{w}} = \frac {1}{\mathrm{M} _ {\mathrm{t}}} \sum_ {\mathrm{n=1}} ^ {\mathrm{N}} \sum_ {\mathrm{m=1}} ^ {\mathrm{M} _ {\mathrm{n}}} (\eta_ {\mathrm{mn}} ^ {\mathrm{i-1}} - \zeta_ {\mathrm{n}} ^ {\mathrm{i-1}}) (\eta_ {\mathrm{mn}} ^ {\mathrm{i-1}} - \zeta_ {\mathrm{n}} ^ {\mathrm{i-1}}) ^ {\prime}\tag{17}
$$

In this step, we assume a single covariance matrix for all individuals. Due to the potentially small number choice situations faced by each individual in a typical recommender system, it might not be possible to estimate an individual-specific covariance matrix.

Step IV: drawing from the individual-level means by drawing from the conditional posterior:

$$
\mathrm{K} (\zeta_ {\mathrm{n}} \mid \mu , \eta_ {\mathrm{mn}} \forall \mathrm{mn}, \Omega_ {\mathrm{b}}, \Omega_ {\mathrm{w}}) \propto \mathrm{h} (\eta_ {\mathrm{mn}} \forall \mathrm{mn} \mid \zeta_ {\mathrm{n}} \forall \mathrm{n}, \Omega_ {\mathrm{w}}) \mathrm{f} (\zeta_ {\mathrm{n}} \mid \mu , \Omega_ {\mathrm{b}})\tag{18}
$$

Using N(μ, Ω<sub>b</sub>) as a prior for $\zeta _ { \mathrm { n } } ,$ the conditional posterior is $\aleph _ { } ( \overline { { \zeta _ { \mathrm { n } } } } , \Sigma _ { \zeta \mathrm { n } } )$ where:

$$
\overline {{\zeta_ {\mathrm{n}}}} = ([ \Omega_ {\mathrm{b}} ^ {\mathrm{i}} ] ^ {- 1} + \mathrm{M} _ {\mathrm{n}} [ \Omega_ {\mathrm{w}} ^ {\mathrm{i}} ] ^ {- 1}) ^ {- 1} \left([ \Omega_ {\mathrm{b}} ^ {\mathrm{i}} ] ^ {- 1} \mu_ {\mathrm{i}} + \mathrm{M} _ {\mathrm{n}} [ \Omega_ {\mathrm{w}} ^ {\mathrm{i}} ] ^ {- 1} \frac {1}{\mathrm{M} _ {\mathrm{n}}} \sum_ {\mathrm{m} = 1} ^ {\mathrm{M} _ {\mathrm{n}}} \eta_ {\mathrm{mn}} ^ {\mathrm{i} - 1}\right)\tag{19}
$$

and:

$$
\Sigma_ {\zeta \mathrm{n}} = ([ \Omega_ {\mathrm{i+1}} ^ {\mathrm{b}} ] ^ {- 1} + \mathrm{M} _ {\mathrm{n}} [ \Omega_ {\mathrm{i+1}} ^ {\mathrm{w}} ] ^ {- 1}) ^ {- 1}\tag{20}
$$

Step V: drawing from the individual- and menu-specific coeficients by drawing from the conditional posterior:

$$
\begin{array}{r l} & {\mathrm{K} (\eta_ {\mathrm{mn}} \mid \mu , \zeta_ {\mathrm{n}}, \Omega_ {\mathrm{b}}, \Omega_ {\mathrm{w}}) \propto \prod_ {\mathrm{j} = 0} ^ {J _ {\mathrm{mn}}} [ \mathrm{P} _ {\mathrm{j}} (\eta_ {\mathrm{mn}}) ^ {\mathrm{d} _ {\mathrm{jmn}}} ] \mathrm{h} (\eta_ {\mathrm{mn}} \forall \mathrm{mn} \mid \zeta_ {\mathrm{n}}, \Omega_ {\mathrm{w}}), \quad \mathrm{n}} \\ & {\qquad = 1, 2, \dots , \mathrm{N}, \mathrm{m} = 1, 2, \dots \mathrm{M} _ {\mathrm{n}}} \end{array}\tag{21}
$$

A draw of $\boldsymbol \eta _ { \mathrm { { m n } } } ^ { \mathrm { ~ \scriptsize ~ i ~ } }$ is obtained by the Metropolis-Hastings procedure.

This five-step procedure assumes that all coeficients have inter- and intra-consumer distributions. However, the estimator can account for coeficients with only inter-consumer heterogeneity, or coeficients without any heterogeneity by including two additional MH steps [6,7].

## 3.2. Updating preferences

These parameters are estimated and updated through two interacting and repeated steps: ofline and online estimation procedures.

Ofline Estimation: The ofline estimation procedure updates all the parameters across three levels. Namely, data are pooled and all coeficients (μ, $\Omega _ { \mathrm { b } } , \zeta _ { \mathrm { n } } , \Omega _ { \mathrm { w } } ,$ and $\eta _ { \mathrm { m n } } )$ are updated to reflect the efects of all choices made by all individuals since the last update. This is performed periodically (e.g. overnight or once a week) as it is computationally expensive. Updating population-level coeficients accounts for population trends when estimating individual-level coeficients.

Online Estimation: The online estimation procedure updates users' preferences in real time as they make choices. The individual specific parameters $( \zeta _ { \mathrm { n } }$ and $\eta _ { \mathrm { m n } } )$ are updated after every choice, assuming that the population parameters μ and $\Omega _ { \mathrm { b } }$ and the intraconsumer covariance matrix $\Omega _ { \mathrm { { w } } }$ are fixed. This update is computationally inexpensive, and it can be done for each individual at a time, i.e., when a choice is observed for a given individual, his/her parameters are updated only. The online procedure is executed by iterating steps IV and V of the 5-step Gibbs sampler only for all choices available after the last ofline update.

Ideally, if we ignore the computational constraints, the 5-step ofline procedure would be used to update individual preferences after each choice. In this procedure, Steps IV and V update the individual and menu-specific preferences for each individual using the intra-consumer covariance matrix $\Omega _ { w } ^ { \mathrm { ~ i ~ } }$ and the inter-consumer distribution $\mathcal { N } _ { \mathrm { T } } (  { \mu ^ { \mathrm { i } } } , \Omega _ { \mathrm { b } } ^ { \mathrm { i } } )$ as a prior as shown in Eq. (22). Conditional on the popula tion-level parameters (μ, $\Omega _ { b } ,$ ,and $\Omega _ { w } ) _ { i }$ , obtaining draws from $\zeta _ { n }$ and $\eta _ { m n }$ for each individual is done independently from all other individuals. Therefore, if draws from the population level parameters were available, the individual- and menu-specific coeficients could be updated separately for each individual by iterating steps IV and V.

Consequently, if we use a prior that is close to $\mathcal { N } _ { \mathrm { T } } (  { \mu ^ { \mathrm { i } } } , \Omega _ { \mathrm { b } } ^ { \mathrm { i } } )$ and a covariance matrix that is close to ${ \Omega _ { w } } ^ { i }$ in the online procedure, we would obtain results that are similar to those obtained from the ofline procedure. Since population level parameters are not expected to vary significantly between successive ofline estimations (which is the key assumption in this methodology), these values can be obtained from the last ofline estimation and used as fixed values in the online estimation. Sections 4.3.1 and 5.2.2 illustrate that this method is able to provide very close results compared to the ofline procedure as a benchmark.

Additionally, since an informative prior is used on the individualspecific parameters, the Markov Chains converge faster; stationarity is achieved quickly and a fewer number of draws is required in the online procedure (compared to the ofline procedure). This procedure can also be implemented on the users' mobile phone in app-based settings.

The key assumption in this procedure is that the population level preferences $\mu , \Omega _ { b } ,$ and $\Omega _ { w }$ do not vary significantly between successive ofline estimations. The frequency of ofline estimations depends on how fast the population level preferences change over time. This might vary from one application to another, and even between diferent attributes within the same application. This can be mitigated by observing the population level parameters obtained from successive ofline estimations and deciding on the frequency of these estimations ac cordingly.

In addition, since μ and $\Omega _ { b }$ are used as priors in Step IV, their efect diminishes as more observations per individual are observed, as the individual specific means $\zeta _ { n }$ get closer to their true values. With few choice observations from each individual, the model sufers from “shrinkage”, whereby individual-level preferences are shrunk towards population means. HB is defined as a “data borrowing” technique that stabilizes individual-level preferences for each individual using information not only from his/her past choices, but also from other individuals within the same data set [26]. Therefore, if the number of observations per individual is large, then deviations in the populationlevel parameters from their true values will have smaller efects on the individual-level preferences.

The frequency of ofline estimations results in a tradeof between the computational complexity of this estimation and the enhanced accuracy of the online procedure. Section 5.2.4 demonstrates that if the population level parameters are misspecified, then the predictions obtained from the online procedure will be inferior to those obtained from the ofline procedure.

## 3.3. Personalized menu generation

The ofline and online procedures result in updated individual- and population-level parameters. These parameters are used as inputs to an online optimizer that performs menu optimization to present the user with a personalized list of alternatives to choose from. The system architecture is presented in Fig. 1, which demonstrates how the online procedure uses the individual choices and the population level parameters obtained from the ofline estimation (μ, $\Omega _ { b } ,$ and $\Omega _ { w } )$ in order to update user preferences.

Personalized recommendations are generated using the menu optimization model proposed by Song et al. [32,33]. This model maximizes hit rate or consumer-surplus (CS) in the form of log-sum, subject to constraints specifying the maximum number of alternatives to be shown in a menu. Binary decision variables are defined for each alternative representing whether or not it is shown in the recommended menu. In the latter study, a Monte-Carlo experiment representing a smart mobility service showed that models with intra-consumer heterogeneity provide better menus (i.e., achieve higher hit-rates) compared to models with only inter-consumer heterogeneity.

## 4. Monte Carlo application

## 4.1. Data and model structure

The procedure described above is applied to Monte-Carlo CBC Grapes data [6,7]. The data assumes that 10,000 individuals are presented with eight menus, each including three diferent alternatives which are bunches of grapes with varying prices and attributes (presented in Table 1) and an opt-out alternative. The eight menus are assumed to be divided into three old choices (menus 1–3), four new choices (menus 4–7), and a test menu (menu 8). The goal is to update individual preferences in order to account for the new choices. The dependent variable is the choice between the three diferent bunches or not buying grapes at all. Both the data and the model are simplified (compared to [7]); only four coeficients are used, two of which are fixed and two have inter- and intra-consumer heterogeneity.

![](/api/attachments/9DA723BH/fulltext/images/0d2ab20622a116fec806012c426a94353df6f2757d7640738fae1b6b5f9aa6c5.jpg)  
Fig. 1. System architecture.

Grape CBC attributes and levels [7].

<table><tr><td>Attribute</td><td>Symbol</td><td>Levels</td></tr><tr><td>Price</td><td>P</td><td>$1.00 to $4.00</td></tr><tr><td>Sweetness</td><td>S</td><td>Sweet (1) or Tart (0)</td></tr><tr><td>Crispness</td><td>C</td><td>Crisp (1) or Soft (0)</td></tr></table>

The utility equations (normalized to the opt-out alternative) are presented in Eq. (22):

$$
\mathrm {U_ {jmn}} \equiv \frac {1}{\exp (\alpha)} (- \mathrm {P_ {jmn}} + \mathrm {S_ {jmn}} \beta_ {\mathrm {S_ {mn}}} + \mathrm {C_ {jmn}} \beta_ {\mathrm {C_ {mn}}} + \mathrm {B_ {jmn}} \beta_ {\mathrm{q}}) + \varepsilon_ {\mathrm{jmn}}\tag{22}
$$

where:

$\mathrm { U _ { j m n } }$ represents the utility of alternative j in menu m faced by in dividual n.

$\mathrm { \Delta P _ { j m n } }$ is the price of bunch j in menu m faced by individual $\mathbf { n } ,$ with its coefficient normalized to –1.

$S _ { \mathrm { j m n } }$ and $\mathrm { { C } _ { j m n } }$ represent sweetness and crispness of bunch j as indicated in Table 1, with coeficients $\beta _ { S _ { \mathrm { m } } }$ and $\beta _ { \mathrm { C } _ { \mathrm { m n } } }$ respectively. The subscript mn indicates that these coeficients have inter- and intra consumer heterogeneity.

$\mathtt { B _ { j m n } }$ is a binary variable equal to one for all three bunches of grapes and zero for the opt-out alternative with coeficient ${ \beta } _ { \mathrm { q } } .$ This coef ficient is fixed across all menus and individuals.

α is a scale parameter, which is fixed across all menus and in dividuals.

Details on the data generation process, assumptions, true values, and estimates are included in Ben-Akiva et al. [7].

The true values of the population means for $\beta _ { S _ { \mathrm { m } } }$ and $\beta _ { \mathrm { C _ { m } } }$ are 1.0 and 0.3. The true values of the fixed coeficients ${ \beta } _ { \mathrm { q } }$ and α are 2.0 and −0.5. Intra-consumer heterogeneity in the data is in the same order of mag nitude as inter-consumer heterogeneity (all inter- and intra-consumer standard deviations are equal to 1.0 for sweetness and crispness).

The model is estimated for menus 1–7 using two procedures (the full ofline procedure and the ofline-online procedure), and the eighth menu is used for testing. In the full ofline procedure, we iterate Steps I through V of the Gibbs sampling procedure in Section 3.1 on all 7 menus. In the ofline - online procedure, we iterate steps I through V (ofline procedure) for menus 1–3 and then iterate steps IV and V for the remaining menus (online procedure).

This experiment mimics a scenario in which three observations are initially observed from each individual. Individual- and populationlevel preferences are already estimated using these three observations (menus 1–3) by applying the five-step Gibbs sampler ofline. Afterwards, four new observations are made by each individual. In order to update individual preferences to account for the new observations, either the full ofline procedure or the online procedure can be used.

## 4.2. Analysis methods

In order to avoid overfitting, all the analyses are done using test data, which include the eighth choice. The analyses are based on the posterior predictive distribution (PPD) given by Eq. (23) and the conditional log-likelihood of the estimated parameters.

$$
P (d _ {j m n} = 1 \mid d _ {m ^ {*}}) = \int_ {\eta_ {m n}} P _ {j} (\eta_ {m n}) K (d \eta_ {m n} \mid d _ {m ^ {*}})\tag{23}
$$

where $d _ { m ^ { * } }$ denotes choices from recent menus and $K ( d \eta _ { m n } | d _ { m ^ { * } } )$ is the posterior (marginal) distribution of menu-specific parameters. The predicted probability of the chosen alternative is defined as the mean of the posterior predictive distribution across all individuals and draws. In addition, 95% confidence intervals of the predicted probabilities are presented. The conditional log-likelihood of the test data is calculated using individual-specific parameters and distributions, and therefore is conditioned on the choices made by individuals.

On the other hand, in order to test the efect of personalization, the results are compared to those obtained by the standard “random coefficients” procedure (which does not allow for any personalization). This is done by generating draws from the unconditional distributions $\zeta _ { \mathrm { n } } { \sim } \mathcal { N } ( \widehat { \mu } , \widehat { \Omega } _ { \mathrm { b } } )$ and $\eta _ { \mathrm { m n } } \mathrm { \sim } \mathcal { N } ( \zeta _ { \mathrm { n } } , \widehat \Omega _ { \mathrm { w } } )$ respectively (where $\widehat { \mu } , \widehat { \Omega } _ { \mathrm { b } } .$ , and $\widehat { \Omega } _ { \mathrm { w } }$ are estimates of μ, Ω , and $\Omega _ { w } )$

The predicted probability of the observed choice of individual n in the test data using the random coeficients approach can be calculated as shown in Eq. (24).

$$
\mathrm{P} (d _ {\mathrm{n}} ^ {*} | \mu , \Omega_ {\mathrm{b}}, \Omega_ {\mathrm{w}}) = \int_ {\zeta_ {\mathrm{n}}} \int_ {\eta_ {\mathrm{mn}}} \mathrm{P} (d _ {\mathrm{n}} ^ {*} | \eta_ {\mathrm{mn}}) \mathrm{H} (\mathrm{d} \eta_ {\mathrm{mn}} | \zeta_ {\mathrm{n}}, \Omega_ {\mathrm{w}}) \mathrm{F} (\mathrm{d} \zeta_ {\mathrm{n}} | \mu , \Omega_ {\mathrm{b}})\tag{24}
$$

Since the five-step Gibbs sampler uses uninformative priors on $\mu , \Omega _ { b } ,$ and $\Omega _ { w } ,$ the estimates and log-likelihood values obtained using this estimator are the same as those obtained using maximum simulated likelihood (MSL) since the posterior will be dominated by the likelihood [7,22,39]. Since we are replicating the MSL estimates using a Bayesian approach, we use the conditional log-likelihood on the test data as a measure of performance.

## 4.3. Estimation results

## 4.3.1. Application of the ofline - online procedure

The model is estimated using 200,000 Gibbs iterations, 100,000 of which are used as burn-in draws while the remaining 100,000 are used for sampling from the posterior distributions. Individual-level and menu-level parameters are obtained directly from the MCMC $( \zeta _ { \mathrm { n } }$ and $\boldsymbol \eta _ { \mathrm { m n } }$ draws respectively).

The stationarity of the Markov chains obtained from two ofline procedures (using menus 1–7 and 1–3) is verified using the Heidelberg-Welch test [40] and Gelman and Rubin's convergence diagnostic [41]. All Markov chains pass the tests at the 95% level of confidence. The estimation results are presented in Table 2.

The results presented in Table 3 indicate that the full ofline procedure achieves the highest final log-likelihood values and probabilities of the chosen alternatives on the test data (menu 8) as expected. However, this procedure would be infeasible in real-time. Updating the sample level estimates is computationally expensive; for this Monte-Carlo experiment, the run time is approximately 12 h.

Alternatively, the results of the partial ofline procedure (using menus 1–3) have lower log-likelihood values and predicted prob abilities. However, the subsequent application of the online procedure increases the probability of the chosen alternative by approximately 1.5% and yields results that are very close to those obtained by the full ofline procedure. The ofline-online procedure is also feasible and efficient in real time because it can be applied to the individual making the choice only rather than the whole sample.

## 4.3.2. Benefits of individual-level parameters

As shown in Table $^ { 4 , }$ the non-personalized (unconditional) log likelihood values and the predicted probabilities of the chosen alternative are inferior to the respective conditional values calculated using the posterior draws. In this example, using individual-level parameters improves the predicted probabilities of the observed choices by about 4–6% compared to the random coeficients procedure.

Table 2  
Estimation results.

<table><tr><td colspan="2"></td><td colspan="2">Full offline (menus 1-7)</td><td colspan="2">Offline on menus 1-3</td></tr><tr><td></td><td>True value</td><td>Posterior mean</td><td>Std. dev</td><td>Posterior mean</td><td>Std. dev</td></tr><tr><td colspan="6">Population mean</td></tr><tr><td>Constant</td><td>2</td><td>2.004</td><td>0.011</td><td>2.015</td><td>0.016</td></tr><tr><td>Log(scale)</td><td>-0.5</td><td>-0.508</td><td>0.009</td><td>-0.510</td><td>0.014</td></tr><tr><td>Sweetness</td><td>1</td><td>1.004</td><td>0.015</td><td>0.989</td><td>0.020</td></tr><tr><td>Crispness</td><td>0.3</td><td>0.313</td><td>0.015</td><td>0.294</td><td>0.020</td></tr><tr><td colspan="6">Inter-consumer std. dev</td></tr><tr><td>Sweetness</td><td>1</td><td>0.961</td><td>0.017</td><td>0.954</td><td>0.029</td></tr><tr><td>Crispness</td><td>1</td><td>1.036</td><td>0.017</td><td>1.054</td><td>0.030</td></tr><tr><td colspan="6">Intra-consumer std. dev</td></tr><tr><td>Sweetness</td><td>1</td><td>0.997</td><td>0.024</td><td>0.972</td><td>0.039</td></tr><tr><td>Crispness</td><td>1</td><td>0.989</td><td>0.025</td><td>0.991</td><td>0.043</td></tr></table>

Table 3  
Estimation results for the ofline-online procedure.

<table><tr><td>Estimation procedure and menus</td><td>PPD mean</td><td>PPD confidence interval</td><td>Log-likelihood</td></tr><tr><td>Full offline (menus 1–7)</td><td>0.458</td><td>[0.456, 0.461]</td><td>-9955.2</td></tr><tr><td>Offline (menus 1–3)</td><td>0.442</td><td>[0.439, 0.446]</td><td>-10,335.6</td></tr><tr><td>Offline (menus 1–3)</td><td>0.458</td><td>[0.456, 0.461]</td><td>-9962.7</td></tr><tr><td>Online (menus 4–7)</td><td></td><td></td><td></td></tr></table>

Table 4  
Comparison between individual-specific and random coeficients.

<table><tr><td rowspan="2">Estimation procedure and menus</td><td colspan="2">Random coefficients</td><td colspan="2">Individual-specific coefficients</td></tr><tr><td>PPD mean</td><td>Log-likelihood</td><td>PPD mean</td><td>Log-likelihood</td></tr><tr><td>Full offline (menus 1–7)</td><td>0.397</td><td>-11,090.7</td><td>0.458</td><td>-9955.2</td></tr><tr><td>Offline (menus 1–3)</td><td> $0.397^a$ </td><td> $-10,959.5^a$ </td><td>0.442</td><td>-10,335.6</td></tr><tr><td>Offline (menus 1–3)</td><td></td><td></td><td>0.458</td><td>-9962.7</td></tr><tr><td>Online (menus 4–7)</td><td></td><td></td><td></td><td></td></tr></table>

<sup>a</sup> Using the non-personalized approach, the probabilities predicted for the test data using the ofline-online procedure would be similar to those predicted using the partial ofline procedure.

## 4.3.3. Applications in personalized recommendations

In this section, we assume that users are ofered only one alternative from the test menu. In order to maximize consumer surplus, the alternative with the highest predicted probability is chosen. The choice between the recommended alternative and opting-out is then simulated. The hit-rate is defined as the probability of accepting the recommendation instead of choosing the opt-out alternative.

The simulated hit-rate with individual-specific parameters obtained from the full ofline procedure is 67.0%. On the other hand, the simulated hit-rates obtained using the ofline procedure with menus 1–3 only is 65.7%. However, accounting for the new choices using the on line procedure raises the hit-rates back to 67.0%. On the other hand, using population-level parameters instead of individual-level parameters results in a simulated hit-rate of 62.5% even when we conside all 7 choices.

## 5. Real application: Swissmetro data

## 5.1. Data and model

The procedure described in Section 3 is also applied to the Swissmetro data set [9], with the dependent variable being the transportation mode choice. The data was collected in Switzerland on the trains between St. Gallen and Geneva in 1998. Each survey respondent was presented with 9 hypothetical choice tasks, each having three alternatives (private car, Swissmetro (SM), and train). The attributes of these modes include the travel cost (fuel and parking costs for private car and fares for Swissmetro and train), travel time for all three modes, and Swissmetro and train headway. Since multiple observations are available from each respondent, we can use the ofline-online procedure to demonstrate how preferences are learnt as more choices are observed.

In this application, we consider the simplified utility equation presented in Eqs. (25)–(27). Since the cost coeficient is fixed to −1, all the estimated coeficients represent the willingness to pay for the corresponding attributes (i.e. the time coeficient represents the value of time). Consequently, a scale parameter $\left( \alpha _ { \mathrm { m n } } \right)$ is estimated.

Table 5 Estimation results.

<table><tr><td colspan="3">Population mean</td><td colspan="2">Inter-consumer Standard deviation</td><td colspan="2">Intra-consumer Standard deviation</td></tr><tr><td>Coefficient</td><td>Posterior mean</td><td>Std. Dev.</td><td>Posterior mean</td><td>Std. Dev.</td><td>Posterior mean</td><td>Std. Dev.</td></tr><tr><td> $ASC_{SM}$ </td><td>0.321</td><td>0.064</td><td>0.748</td><td>0.058</td><td>0.255</td><td>0.036</td></tr><tr><td> $ASC_{Car}$ </td><td>0.574</td><td>0.071</td><td>1.286</td><td>0.050</td><td>0.091</td><td>0.045</td></tr><tr><td>Scale</td><td>-2.019</td><td>0.067</td><td>1.053</td><td>0.075</td><td>0.163</td><td>0.101</td></tr><tr><td>Travel time</td><td>0.179</td><td>0.037</td><td>0.912</td><td>0.029</td><td>0.024</td><td>0.016</td></tr></table>

$$
\begin{array}{r l} \mathrm {U_ {Car, nm}} = & (\mathrm{ASC} _ {\text {Car,mn}} - \exp (\eta_ {\mathrm{mn}}) \times \text {Time} _ {\text {Car,mn}} - \operatorname{Cost} _ {\text {Car,mn}}) / \exp (\alpha_ {\mathrm{mn}}) \\ & + \varepsilon_ {\text {Car,mn}} \end{array} \tag {25}
$$

$$
\begin{array}{r l} \mathrm {U_ {SM,nm}} = & (\mathrm{ASC} _ {\mathrm{SM,mn}} - \exp (\eta_ {\mathrm{mn}}) \times \mathrm{Time} _ {\mathrm{SM,mn}} - \mathrm{Cost} _ {\mathrm{SM,mn}}) \\ & / \exp (\alpha_ {\mathrm{mn}}) + \epsilon_ {\mathrm{SM,mn}} \end{array}\tag{26}
$$

$$
\begin{array}{r l} \mathrm{U} _ {\text {Train, nm}} = & (\quad - \exp (\eta_ {\mathrm{mn}}) \times \text {Time} _ {\text {Train, mn}} - \text {Cos} t _ {\text {Train, mn}}) / \exp (\alpha_ {\mathrm{mn}}) \\ & + \varepsilon_ {\text {Train, mn}} \end{array} \tag {27}\tag{27}
$$

where:

$\mathrm { U } _ { \mathrm { C a r , } }$ <sub>mn</sub>, U<sub>SM, mn</sub>, and $\mathrm { { U } _ { T r a i n , } }$ represent the utilities for car, Swissmetro, and train in menu m for individual n, respectively.

• Timej, mn and $\mathsf { C o s t _ { j } } ,$ <sub>mn</sub> represent the total (door-to-door) travel time and travel cost of alternative j in menu m presented to individual n, respectively. The cost coeficient is fixed to −1.

$\mathbf { A S C _ { C a r , \ m n } }$ and $\mathsf { A S C } _ { \mathsf { S M } , }$ represent alternative specific constants for car and train, respectively. The standard deviation of the train constant has been normalized to zero since it has the lowest value among all three alternatives.

$\mathrm { e x p } ( \mathfrak { n } _ { \mathrm { m n } } )$ and $\mathrm { e x p } ( \alpha _ { \mathrm { m n } } )$ represent the coeficient of travel time and the scale parameter, respectively. Exponentiation is used in order model the log-normal distribution, which ensures that the travel time coeficient and the scale parameter are positive (and thus travel time and cost have a negative efect on utility to all individuals).

$\epsilon _ { \mathrm { C a r , ~ \mathrm { m n } } } , ~ \epsilon _ { \mathrm { S M , ~ \mathrm { m n } } } ,$ and $\epsilon _ { \mathrm { T r a i n , ~ m n } }$ are error terms independently and identically distributed as extreme value type I.

## 5.2. Results

The model is estimated for menus 1–8 and the ninth menu is used for testing. In the following sections, we explore the estimation results with regards to inter- and intra-consumer heterogeneity and personalization. Afterwards, we estimate models using fewer choices done by each individual (2 or 5 choices out of 8), then apply the online procedure to the remaining choices up to the eighth choice.

## 5.2.1. Estimation with inter- and intra-consumer heterogeneity

The model is estimated using 400,000 Gibbs iterations, 200,000 of which are used as burn-in draws while the remaining 200,000 are used for sampling from the posterior distributions. The estimation results with menus 1–8 show significant inter-consumer heterogeneity for all coeficients. In addition, we find significant intra-consumer heterogeneity in the car and Swissmetro constants as shown in Table 5.

## 5.2.2. Predicting the next choice

The model estimated above is based on eight choices done by each individual. It utilizes all of the available training data. In this section, we estimate similar models using fewer menus (e.g. 2 or 5) and then perform the online procedure to all individuals.

Table 6 shows the log-likelihood and the predicted probability of the chosen alternative for the test menu (9th choice) using diferent estimation procedures. We first present the results for the full ofline procedure (8 menus for each individual). This procedure achieves an average predicted probability of 0.717 and a log-likelihood of −400.9.

The following rows present the results with a subset of the data (2 choices and 5 choices per individual respectively). The results indicate that with fewer observations, we estimate models with lower average probabilities and log-likelihood values on the test data. However, the subsequent application of the online-procedure to the remaining menus recovers the drop in prediction accuracy as shown in the last two rows.

It can also be observed that the confidence intervals of the predicted probabilities (calculated empirically using the posterior distribution) of the full ofline and the partial ofline estimations (menus 1–2 and 1–5) do not overlap, indicating that the diferences are statistically significant, and thus estimation with a fewer number of menus results in inferior predictions.

When more menus are included in the ofline estimation, the predicted probabilities are higher because better priors are used (i.e. population level parameters $\mu , \Omega _ { b } ,$ and $\Omega _ { w } )$ . Therefore, it is critical that the estimates of these parameters (which are obtained from the ofline procedure) are accurate and up to date. To demonstrate the efects of using bad population level parameters, we perform online estimation using all 8 choices, but with the sample level means (μ) set to zeroes, and the inter- and intra-consumer covariance matrices set to identity matrices. The results indicate significantly worse predictions, with the mean of the posterior predictive distribution being 0.630, with the 95th percentile confidence interval [0.622, 0.637]. In addition, the likelihood of the test data is −463, which is substantially worse than the values in Table 6.

## 5.2.3. Generating personalized recommendations

In order to demonstrate the accuracy and robustness of the proposed method in personalized recommendations, it is compared to two different approaches: a simple content-based method (in which the most chosen alternative in the previous menus, 1–7, is recommended), and non-personalized discrete choice models (flat logit and double mixture model with inter- and intra-consumer heterogeneity). The first

## Table 6

Prediction results with the full ofline, partial ofline, and ofline-online procedures.

<table><tr><td colspan="3">Non-personalized</td><td colspan="2">Personalized</td></tr><tr><td>Estimation procedure</td><td>Log-likelihood</td><td>Probability</td><td>Log-likelihood</td><td>Probability</td></tr><tr><td>Full offline (1–8)</td><td>-657</td><td>0.509[0.487, 0.531]</td><td>-401</td><td>0.717[0.709, 0.725]</td></tr><tr><td>Partial offline (1–2)</td><td>-666</td><td>0.514[0.492, 0.536]</td><td>-551</td><td>0.668[0.652, 0.683]</td></tr><tr><td>Partial offline (1–5)</td><td>-656</td><td>0.504[0.480, 0.528]</td><td>-437</td><td>0.699[0.689, 0.709]</td></tr><tr><td>Online (3–8)</td><td>-</td><td>-</td><td>-410</td><td>0.700[0.692, 0.708]</td></tr><tr><td>Online (6–8)</td><td>-</td><td>-</td><td>-403</td><td>0.716[0.708, 0.724]</td></tr></table>

Numbers in brackets indicate the 95th percentile confidence intervals of the mean predicted probability.

Prediction results with the full ofline, partial ofline, and ofline-online procedures.

<table><tr><td></td><td colspan="2">Content-based (most chosen)</td><td colspan="2">Flat logit</td><td colspan="2">Double mixture</td><td colspan="2">Double mixture - personalized</td></tr><tr><td>Menu size</td><td>1</td><td>2</td><td>1</td><td>2</td><td>1</td><td>2</td><td>1</td><td>2</td></tr><tr><td>Full offline (1–8)</td><td>0.763</td><td>0.954</td><td>0.636</td><td>0.910</td><td>0.609</td><td>0.914</td><td>0.770</td><td>0.977</td></tr><tr><td>Partial offline (1–2)</td><td>0.713</td><td>0.912</td><td>0.588</td><td>0.910</td><td>0.608</td><td>0.912</td><td>0.725</td><td>0.941</td></tr><tr><td>Partial offline (1–5)</td><td>0.745</td><td>0.947</td><td>0.626</td><td>0.911</td><td>0.609</td><td>0.912</td><td>0.757</td><td>0.968</td></tr><tr><td>Online (3–8)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.767</td><td>0.952</td></tr><tr><td>Online (6–8)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.777</td><td>0.975</td></tr></table>

approach accounts for personalization by considering the choice history of each individual, however, it cannot account for the impact of changes in the attributes (travel cost and travel time) as these vary among diferent choices. On the other hand, the non-personalized logit models account for attributes, but do not make use of the choice history of each individual. The ofline-online estimation methodology presented in Section 3 accounts for both the individual choice history and alternative attributes.

Personalized menu optimization is performed with the objective of maximizing the expected hit rate [32,33] on the 9th choice. We simulate recommended menus that have either one or two out of the three original alternatives. The hit rate is defined as the fraction of individuals who choose an alternative that is included in the recommended menu. As shown in Table $^ { 7 , }$ the ofline-online procedure can also approximate the full ofline procedure in terms of hit rate, and the observed efect of personalization is substantial. (In this table, the online procedure using menus 6–8 achieves the highest hit rate. We would expect the full ofline procedure to perform better, but predictions are based on the testing data; the sample level coeficients obtained from the ofline estimation with the first 5 menus might fit the test data better than those obtained from the full estimation).

Table 7 indicates that the personalized double mixture model outperforms the content-based recommendation in all cases (by a margin of 1–2%), even when the online procedure is used. In addition, it is substantially better than the non-personalized flat logit and double mixture models.

## 6. Discussion

## 6.1. Model estimation

In this section, we discuss practical issues related to the efect of priors, identifiability, and applications in recommender systems.

## 6.1.1. Efect of priors

The basic HB procedure utilizes the Inverse Wishart (IW) prior, which has some undesirable properties, and thus can lead to biased estimates of standard deviations [4]. Particularly, this prior tends to inflate standard errors if their true values are small since it has a low density near zero. Although this issue did not impose any problems in our Monte-Carlo examples (because the standard errors are substantially distinguishable from zero), other priors can be used to avoid these biases such as the Hierarchical Inverse Wishart (HIW), Scaled Inverse Wishart (SIW), and Separation Strategy (or BMM) [34]. It should also be noted that the efect of priors decreases with increasing the sample size. With suficient data, and with the “infinitely” difuse priors, the posterior distribution is completely determined by the data, and therefore replicates the estimates obtained by maximum simulated likelihood.

## 6.1.2. Identifiability of individual-level preferences and accounting for uncertainty

The model with inter- and intra-consumer heterogeneity is only identifiable if multiple choice situations from each individual are available. In addition, with few choice observations from each individual, the model sufers from “shrinkage”, whereby individual-level preferences are shrunk towards population means. HB is defined as a “data borrowing” technique that stabilizes individual-level preferences for each individual using information not only from his/her past choices, but also from other individuals within the same data set [26].

While Allenby and Rossi [2] state that this procedure allows us to estimate the distributions of the population level parameters (μ and Ω ) and yields exact finite-sample estimates of the posterior distribution of individual-level parameters, Greene [15] argues that these estimates are only “exact” for the assumed priors and the data used, and up to simulation variance. To account for uncertainty in individual-level estimates, Allenby and Rossi [3] indicate that these estimates are not precisely estimated, and the use of point-estimates leads to over-confident predictions of efect-sizes. To avoid this over-confidence, Allenby and Rossi [3] suggest using all the posterior draws to make predictions instead of the point estimates (which is applied in our results in Sections 4 and 5).

Despite the fact that individual-level preferences are not accurately estimated, the results show that we achieve significantly better predictions compared to those without any personalization. These pre ferences are “learnt” with more choices, which makes this procedure suitable for application in recommender systems.

Alternatively, the posterior distributions of the individual- and menu-specific parameters can be used in Multi-armed bandit methods such as Thompson sampling and Upper Confidence Bounds as described in Teo et al. [35] and Song [31]. For example, Thompson sampling uses individual draws from the posterior distributions. A distribution with large variance indicates high uncertainty in the estimated parameter. Therefore, attributes with uncertain parameter distributions become more likely to be recommended, which allows for learning these distributions more eficiently.

## 6.2. Application in recommender systems

## 6.2.1. Sample size and scalability

The sample size considered in our Monte-Carlo application is 10,000, which is suficient for demonstrating the methodology for estimating and updating preferences. However, in app-based systems, the number of users can be potentially greater than tens of thousands. The five-step Gibbs sampler scales well with increasing sample size, as the estimates become closer to their true values and the required number of burn-in iterations decreases. Since the ofline procedure is only performed periodically, long computational times can be tolerated. Individual preferences, on the other hand, are updated after each choice using the online procedure which can be performed in a few seconds to minutes, and can even be implemented on mobile devices.

## 6.2.2. Application to new users

The online procedure can be applied to new users with known choices with estimates of $\mu , \Omega _ { \mathrm { b } }$ and $\Omega _ { \mathrm { w } }$ obtained from the ofline procedure. For instance, these users may have joined the system and made choices after the last ofline update. On the other hand, the random coeficients procedure described in Section 4.2 can be applied to individuals with no previous choice history, and thus, these users will be first presented with non-personalized menus, i.e., population-level parameters will be used for menu optimization.

## 6.2.3. Data collection and endogeneity

In applications to recommender systems, the estimated models must account for endogeneity; the choice set presented to the user in each menu is based on this user's preferences, which are estimated based on his/her previous choices. Extensive research has been done on en dogeneity corrections in discrete choice models, most of which falls into two categories: the BLP method [8], and the control-function method [17,18].

Endogeneity is not a concern in the models presented in this paper (since all the attributes used in the estimation of preferences were generated exogenously). In addition, Danaf et al. [13] show that endogeneity bias in recommender systems is ignorable if all the relevant data are used in estimation. This can be achieved by initializing the system with exogenous recommendations, and including all the avail able data in subsequent ofline estimations.

## 7. Conclusions

This paper presented a methodology for estimating and updating consumer preferences online in the context of app-based recommender systems. We proposed an ofline estimator, which estimates and updates individual and population level parameters periodically using a five-step Gibbs sampling procedure, and a real-time online estimator, which updates individual-specific parameters in real-time as more choices are made and assumes that population level parameters are fixed until the next ofline estimation.

The proposed online estimator enables the use of discrete choice models in online decision support systems because it is (1) computationally eficient, (2) empirically accurate, and (3) theoretically justified. It is computationally eficient because it uses the data of the individual making the choice only, without the need to use data from other users. It is empirically accurate as it can achieve the same level of prediction accuracy as the ofline estimator (which is computationally expensive and infeasible in real-time) as we have shown using real and Monte Carlo data. Finally, it is theoretically justified since it is equivalent to calibrating the model at the individual level, but with good priors representing the distribution of preferences in the population.

Our methodology subsumes the utility-based advantages of discrete choice models and the personalization capabilities of standard re commendation techniques by making use of all the available data in: cluding user-specific characteristics and preferences, alternative-specific attributes, and contextual variables. In our formulation of the utility equations, the estimated distributions can be interpreted as the individual's “willingness-to-pay” for diferent features, which can be used in pricing, designing, and recommending new alternatives. In addition, our models are able to account for complex patterns of preference heterogeneity, namely intra-consumer heterogeneity which represents variations in preferences across diferent choices of the same individual. Therefore, we avoid the unrealistic assumption that preferences are stable over time. This has also been shown to improve the accuracy of recommendations and predictions [7,33].

Several limitations arise in the application of our proposed metho dology. The Monte-Carlo results indicate that sample level parameters (μ, Ω ,and Ω ) are recovered using the five-step Gibbs sampler. However, as in most Hierarchical models, individual- and menu-specific parameters might not be estimated precisely due to shrinkage [25]. These preferences are “learnt” gradually from repeated choices. Nevertheless, using these preferences results in substantially better predictions compared to using an “average individual” (or unconditional distributions) even with a few number of choice situations.

The results presented in this paper are static and mimic SP experiments. Consumer behavior may difer significantly between SP experiments and app-based choices. For instance, the time intervals between successive choices may vary considerably between the app based systems and SP experiments.

Finally, there is a tradeof between the model complexity (which results in high computational times) and the accuracy of predictions and recommendations. The complexity is determined by the utility equations which are specified by the researcher. The ofline estimation results can be used to identify the significant predictors of choices, and adjust the utility equations accordingly. In addition, the model structure can be simplified by accounting for inter-consumer heterogeneity only (if intra-consumer heterogeneity does not appear to be significant). This would reduce the running time of the online procedure from a few seconds to less than 1 s.

This framework is implemented in the app-based travel adviser Tripod (Sustainable Travel Incentives with Prediction, Optimization and Personalization) [32,33] which incentivizes travelers to shift towards more sustainable alternatives (e.g. changing mode, route, or departure time choice behavior). Once more data from Tripod becomes available, the proposed methodology will be further validated, espe cially that users will be presented with real-life situations rather than SP experiments, and will have longer time intervals as well as contextual diferences between successive choices, which allows for a higher level of intra-consumer heterogeneity. In addition, ongoing research is focused on modeling extensions to allow for flexible mixing distributions of inter- and intra-consumer heterogeneity, and incorporating socio demographic and contextual information in order to partially explain inter- and intra-consumer heterogeneity respectively.

## Acknowledgements

This work is funded by TRIPOD: Sustainable Travel Incentives with Prediction, Optimization and Personalization research project sponsored by the U.S. Department of Energy Advanced Research Projects Agency-Energy (ARPA-E). It was awarded through the ARPA-E Traveler Response Architecture using Novel Signaling for Network Eficiency in Transportation (TRANSNET) program.

## References

[11 C.C. Aggarwal. Recommender systems. Springer International Publishing, 2016

[2] G.M. Allenby, P.E. Rossi, Marketing models of consumer heterogeneity, J. Econ. 89 (1–2) (1999) 57–78.

[3] G.M. Allenby, P.E. Rossi, Hierarchical Bayes models, The Handbook of Marketing Research: Uses, Misuses, and Future Advances, 2006, pp. 418–440

[4] I. Alvarez, J. Niemi, M. Simpson, Bavesian Inference for a Covariance Matrix. (2014) (arXiv preprint arXiv:1408.4050)

[5] A. Ansari, S. Essegaier, R. Kohli, Internet recommendation systems, J. Mark. Res XXXVI (2000) 363–375

[6] E. Becker, M. Danaf, X. Song, B. Atasoy, M. Ben-Akiva, Hierarchical Baves estimator of a logit mixture with inter- and intra-consumer heterogeneity. Transp. Res. E

[7] M. Ben-Akiva, D. McFadden, K. Train, Foundations of stated preference elicitation: consumer behavior and choice-based conjoint analysis, Found. Trends Econom. 10 (1–2) (2019) 1–144.

[8] S. Berry, J. Levinsohn, A. Pakes, Automobile prices in market equilibrium Econometrica (1995) 841–890

[9] M. Bierlaire, K. Axhausen, G. Abay, Acceptance of Modal Innovation: The Case of the Swissmetro Proceedings of the 1st Swiss Transportation Research Conference Ascona, Switzerland, 2001

[10] Castells, P., Hurley, N. J., & Vargas, S. (2015). Novelty and diversity in recommender systems. In Ricci, F., Rokach, L., and Shapira, B., Recommender Systems Handbook, Second Edition, Springer Science + Business Media, New York 2015.

[11] Chaptini, B. (2005). Use of discrete choice models with recommender systems. PhD dissertation. Department of Civil and Environmental Engineering. MIT

[12] K.W. Cheung, J.T. Kwok, M.H. Law, K.C. Tsui, Mining customer product ratings for personalized marketing, Decis. Support, Syst, 35 (2) (2003) 231–243

[13] M. Danaf, A. Guevara, B. Atasoy, X. Song, F. Becker, M. Ben-Akiva, Endogeneity Bias in Adaptive Choice Contexts: Choice-based Recommender Systems and Adaptive Stated Preferences Surveys, Transportation Research Board Annua Meeting, Washington D.C, 2019.

[14] D. Goldberg, D. Nichols, B.M. Oki, D. Terry, Using collaborative filtering to weave

an information tapestry, Commun. ACM 35 (12) (1992) 61–70.

[15] W.H. Greene, Interpreting estimated parameters and measuring individual hetero geneity in random coeficient models, Department of Economics, Stern School of Business. New York University. 2003

[16] Gunawardana, A., & Shani, G. (2015). Evaluating recommender systems. In Ricci, F., Rokach, L., and Shapira, B., Recommender Systems Handbook, Second Edition, Springer Science + Business Media, New York, 2015.

[17] J. Hausman, Specification tests in econometrics, Econometrica 46 (6) (1978) 1251–1272.

[18] J. Heckman, Dummy endogenous variables in a simultaneous equation system, Econometrica 46 (4) (1978) 931–959.

[19] S. Hess, J. Rose, Allowing for intra-respondent variations in coeficients estimated on repeated choice data, Transp. Res. B Methodol. 43 (6) (2009) 708–719.

[20] S. Hess, K. Train, Recovery of inter- and intra-consumer heterogeneity using mixed logit models, Transp. Res. B Methodol. 45 (7) (2011) 973–990.

[21] S. Huang, Designing utility-based recommender systems for e-commerce: evaluation of preference-elicitation methods, Electron. Commer. Res. Appl. 10 (4) (2011) 398–407.

[22] J. Huber, K. Train, On the similarity of classical and Bayesian estimates of individual mean partworths, Mark. Lett. 12 (3) (2001) 259–269.

[23] H. Jiang, X. Qi, H. Sun, Choice-based recommender systems: a unified approach to achieving relevancy and diversity, Oper. Res. 62 (5) (2014) 973–993.

[24] Li, L., Chu, W., Langford, J., & Schapire, R. E. (2010). A contextual-bandit approach to personalized news article recommendation. In Proceedings of the 19th International Conference on World Wide Web (pp. 661–670). ACM.

[25] Q. Liu, T. Otter, G.M. Allenby, Investigating endogeneity bias in marketing, Mark. Sci. 26 (5) (2007) 642–650.

[26] B. Orme, G. Baker, Comparing Hierarchical Bayes Draws and Randomized First Choice for Conjoint Simulations, (2000) (Sawtooth Software Research Paper Series).

[27] A. Polydoropoulou, M. Lambrou, Development of an e-Learning Recommender System Using Discrete Choice Models and Bayesian Theory: A Pilot Case in the Shipping Industry, (2012) In Security Enhanced Applications for Information Systems. (978-953-51-0643).

[28] Ricci, F., Rokach, L., & Shapira, B. (2015). Recommender systems: introduction and challenges. In Ricci, F., Rokach, L., and Shapira, B., Recommender Systems Handbook, Second Edition, Springer Science + Business Media, New York, 2015.

[29] Rubin, T., & Steyvers, M. (2009). A topic model for movie choices and ratings. In Proceedings of the 9th International Conference on Cognitive Modeling, Manchester.

[30] Song, X. (2016). A Bayesian bandit approach to personalized online coupon re commendation. Master's Thesis, MIT

[31] X. Song, Personalization of future urban mobility. PhD dissertation, Department o Civil and Environmental Engineering, MIT, 2018.

[32] X. Song, B. Atasoy, M. Ben-Akiva, Smart Mobility Through Personalized Menu Optimization. Transportation Research Board Annual Meeting, Washington, DC, USA, 2017.

[33] Song, X., Danaf, M., Atasoy, B., & Ben-Akiva, M. (2018). Personalized menu optimization with preference updater: a Boston case study. Transportation Research Record: Journal of the Transportation Research Board.

[34] Song, X., Becker, F., Danaf, M., Atasoy, B., & Ben-Akiva, M. (2019). Enhancement of Hierarchical Bayes for Logit Mixture. Working paper, MIT.

[35] Teo, C. H., Nassif, H., Hill, D., Srinivasan, S., Goodman, M., Mohan, V., & Vishwanathan. S. V. N. (2016. September). Adaptive, personalized diversity for visual discovery. In Proceedings of the 10th ACM Conference on Recommender Systems (pp. 35–38). ACM.

[36] K. Train, Discrete Choice Methods with Simulation, Cambridge University Press,

2009 (Chapter 12).

[37] M. Yáñez, E. Cherchi, B. Heydecker, J. Dios-Ortuzar, On the treatment of repeated observations in panel data: eficiency of mixed logit parameter estimates, Netw. Spat. Econ. 11 (3) (2011) 393–418.

[38] Ziegler, C.N., McNee, S.M., Konstan, J.A., & Lausen, G. (2005). Improving recommendation lists through topic diversification. In Proceedings of WWW '05.

[39] W.H. Greene, Interpreting estimated parameters and measuring individual hetero geneity in random coeficient models, NYU Working Paper, EC-04-08, (2004).

[40] P. Heidelberger, P.D. Welch, Simulation run length control in the presence of an initial transient, Oper. Res. 31 (6) (1983) 1109–1144.

[41] A. Gelman, D.B. Rubin, Inference from iterative simulation using multiple sequences, Stat. Sci. 7 (4) (1992) 457–472.

Mazen Danaf is a PhD candidate in the Intelligent Transportation Systems Lab at MIT. His research focuses on smart mobility applications and personalization using behavioral models. Prior to that, he worked on activity-based travel demand models, and smart phone applications used to collect data used in calibrating these models. He also holds BE and ME degrees in Civil and Environmental Engineering from AUB, where he has done research on students' travel behavior, drivers' behavior, and pedestrian-vehicular interactions.

Felix Becker studied a combined degree of computer science and business at Freie Universität Berlin. He is currently a graduate research assistant at ETH Zurich. His research interests include modeling people's preferences for automated vehicles and Bayesian analysis for discrete choice models.

Xiang Song is a PhD candidate in the Intelligent Transportation Systems Lab at MIT. His research focuses on smart mobility systems, Bayesian econometrics, and the interface between statistical learning and operations management. Prior to that, he has also worked on simulation-based decision support systems and market research.

Bilge Atasoy is an assistant professor in the Transport Engineering and Logistics section of the Department of Maritime and Transport Technology at TU Delft. Prior to joining TU Delft. she was a research scientist at MIT. in the ITS Lab. where she managed research projects in the areas of real-time optimization, travel behavior and choice-based optimization. She received her PhD from EPFL in 2013 where she was working on choicebased airline optimization models. Her main research interests lie at the intersection of optimization and behavioral modeling in order to achieve more eficient, innovative and demand-responsive transportation systems.

Moshe Ben-Akiva is the Edmund K. Turner Professor of Civil and Environmental Engineering and Director of the Intelligent Transportation Systems (ITS) Lab at the Massachusetts Institute of Technology (MIT) and at the Singapore-MIT Alliance for Research and Technology. He holds a PhD degree in Transportation Systems from MIT and honorary degrees from the University of the Aegean, the Université Lumiére Lyon, the Royal Institute of Technology (KTH), and the University of Antwerp. His awards includ the Robert Herman Lifetime Achievement Award in Transportation Science given by the Institute for Operations Research and the Management Sciences (INFORMS) Transportation Science and Logistics (TSL) Society. the Lifetime Achievement Award of the International Association for Travel Behavior Research, the Jules Dupuit prize from the World Conference on Transport Research Society. and the Institute of Electrical and Electronics Engineers ITS Society Outstanding Application Award for DynaMIT. a system for dynamic network management. He has worked as a consultant in industries such as transportation, energy, telecommunications, financial services and marketing for a number of private and public organizations.

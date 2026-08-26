---
otero_id: 16248
otero_key: "DZ5BGA4U"
title: "Underlying Consumer Heterogeneity in Markets for Subscription-Based IT Services with Network Effects"
authors: "Marius F. Niculescu; Hyoduk Shin; Seungjin Whang"
year: "2012"
journal: "Information Systems Research"
doi: "10.1287/isre.1120.0422"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/DZ5BGA4U/fulltext/images/376aeebc82da983b848d590190c68069405451c893127979e8c644c9d4db2500.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Underlying Consumer Heterogeneity in Markets for Subscription-Based IT Services with Network Effects

Marius F. Niculescu, Hyoduk Shin, Seungjin Whang,

## To cite this article:

Marius F. Niculescu, Hyoduk Shin, Seungjin Whang, (2012) Underlying Consumer Heterogeneity in Markets for Subscription-Based IT Services with Network Effects. Information Systems Research 23(4):1322-1341. http://dx.doi.org/10.1287/ isre.1120.0422

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2012, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/DZ5BGA4U/fulltext/images/670c09b6c7f74c12ceb7d6b9c54f54650385bd008ee8ff6ca60e367542b14f3d.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Underlying Consumer Heterogeneity in Markets for Subscription-Based IT Services with Network Effects

Marius F. Niculescu College of Management, Georgia Institute of Technology, Atlanta, Georgia 30308, marius.niculescu@mgt.gatech.edu

Hyoduk Shin

Kellogg School of Management, Northwestern University, Evanston, Illinois 60208, hyoduk-shin@kellogg.northwestern.edu

Seungjin Whang Graduate School of Business, Stanford University, Stanford, California 95305, whang\_jin@gsb.stanford.edu

n this paper we explore the underlying consumer heterogeneity in competitive markets for subscription-based Iinformation technology services that exhibit network effects. Insights into consumer heterogeneity with respect to a given service are paramount in forecasting future subscriptions, understanding the impact of price and information dissemination on market penetration growth, and predicting the adoption path for complementary products that target the same customers as the original service. Employing a continuous-time utility model, we capture the behavior of a continuum of consumers who are differentiated by their intrinsic valuations from using the service. We study service subscription patterns under both perfect and imperfect information dissemination. In each case, we first specify the conditions under which consumer rational behavior supported by the utility model can explain a general observed adoption path, and if so, we explicitly derive the analytical closed-form expression for the consumer valuation distribution. We further explore the impact of awareness and distribution skewness on adoption. In particular, we highlight the practical forecasting importance of understanding the information dissemination process in the market as observed past adoption may be explained by several distinct awareness and heterogeneity scenarios that may lead to divergent adoption paths in the future. Moreover, we show that in the later part of the service lifecycle the subscription decision for new customers can be driven predominantly by information dissemination instead of further price markdowns. We also extend our results to time-varying consumer valuation scenarios. Furthermore, based on our framework, we advance a set of heuristic methods to be applied to discrete-time real industry data for estimation and forecasting purposes. In an empirical exercise, we apply our methodology to the Japanese mobile voice services market and provide relevant managerial insights from the analysis.

Key words: subscription-based IT services; consumer utility models; consumer information awareness; network effects

History: Debabrata Dey, Senior Editor; Karthik Kannan, Associate Editor. This paper was received on June 27, 2010, and was with the authors 8 months for 2 revisions.

## 1. Introduction

In parallel with technological progress, global interconnectivity grows at a rapid pace nowadays. As of 2011, worldwide, there are over 2 billion Internet users (Internet World Stats 2011) and over 5.3 billion active mobile phone user accounts (The Mobile World 2011). Cisco (2011) predicts that by 2015 there will be 15 billion devices worldwide connected to IP networks. We are witnessing an explosion in the variety of information technology (IT) services addressing the diverse needs of this vast reachable consumer population. Some of these services provide infrastructure access (e.g., landline and mobile telephony,

Internet service provision). Others are value-added services (e.g., VoIP, Web hosting, software-as-aservice offerings). According to Gartner (2011), global software-as-a-service revenues are expected to reach \$12.1 billion by the end of 2011 and \$21.3 billion by 2015. Mobile industry, the fastest growing telecom sector, recently surpassed \$1.1 trillion in global revenues, with approximately \$900 billion accounting for voice and data services alone (Ahonen 2010, 2011).

In such markets, it is of great strategic importance for IT service providers to understand the microlevel structure of the untapped market potential. First, such insight allows firms to forecast future sales with increased accuracy. Second, it enables firms to better discern and measure the impact of market primitives such as price and information dissemination rate on subscription patterns. Third, this knowledge, even post-adoption, allows interested parties to better assess the opportunities and market size for complementary value-adding products for which consumers may exhibit a willingness to pay strongly correlated with their willingness to pay for the original service. Although the increasing information footprint left by consumers of IT services allows providers to get various signals about the willingness to pay of their existing installed base, a lot of the information regarding competitors’ installed bases is being made available only at the aggregate level. Thus, to attract and better serve the remaining untapped customers in the market, it is important for both established incumbent and prospective entrant firms to be able to draw inferences about the structure of the untapped market potential based on observed aggregate industry-level adoption.

The continuous-time adoption of innovative products and services has been traditionally explored through aggregate models, which abstract away from individual customer behavior in favor of simplified sales parameterizations that facilitate tractability in analytical frameworks and applicability in empirical studies where individual behavior is not observed. These aggregate models have been used in the past to explain various adoption outcomes, including S-shaped growth curves. We direct interested readers to Mahajan et al. (2000) and Meade and Islam (2006) for recent reviews of this vast literature.

Discussing the potential issues related to comparative statics analysis in aggregate models, Lucas (1976) advocates for the understanding of consumer behavior and responsiveness at an individual level, for such microlevel insights enhance the model’s predictive power and lead to a more accurate estimation of the market evolution. Along this line, starting from the opposite direction and building on individual consumer utility models, several papers have explored the resulting continuous-time aggregate adoption pattern. Chatterjee and Eliashberg (1990) advance a utility model incorporating information flow and risk aversion for quality, and show that it can replicate, under various heterogeneity assumptions, the adoption behavior induced by four specifically chosen aggregate diffusion models. Madden and Coble-Neal (2004) explore global growth of mobile services using a dynamic utility-based model that incorporates network effects and accounts for substitution effects between wireless and fixed-line services. Other papers move beyond explaining the adoption path and also consider firm’s optimal strategies (e.g., Kalish 1985, Dhebar and Oren 1986). Most research in this branch starts from a given consumer heterogeneity structure, and, thus, applies to a restricted set of aggregate adoption patterns.

In this study, we attempt to reconcile the aforementioned approaches—aggregate and microlevel— and focus on the market-level adoption (as opposed to firm-level) of subscription-based IT services in highly competitive markets and in the presence of network effects. The primary question this paper sets out to address is the following: can rational consumer behavior explain the actual observed adoption path for a particular IT subscription-based service? To be exact, under a given utility model, when does a wellbehaved consumer valuation (or, willingness to pay) distribution exist such that its implied aggregate adoption path replicates the actual observed one? Furthermore, if existence conditions are satisfied, what are the shape and properties of such a consumer valuation distribution? Although some analytical papers follow a linear progression from input to output via a certain process,<sup>1</sup> the analytical part of this paper considers a somewhat reverse direction (more common in empirical studies) where the observed portion of the output is given and a structure of the input is estimated. Given the nature of our research question, this study has a positive (descriptive) rather than normative (prescriptive) tone, but we also discuss various managerial insights throughout the paper.

In approaching the above research questions, heeding Lucas’ critique, we start from a consumer utility model and study how it can generate the observed aggregate adoption curve. We employ a dynamic continuous-time utility model in which a continuum of consumers, who enjoy network benefits, are differentiated through their heterogeneous intrinsic valuations for the service. A key characteristic of many IT services is their susceptibility to network effects (i.e., the benefit to consumers often increases in the network size). Network effects have been analytically and empirically explored in association with various IT subscription-based products and services such as mobile telecommunications (Jang et al. 2005, Doganoglu and Grzybowski 2007, and Niculescu and Whang 2012), Internet usage (Sing et al. 2002, Guevara et al. 2007, and Dewan et al. 2010), softwareas-a-service and other software products delivered under a subscription-based license (Haruvy et al. 2004, Zhang and Seidmann 2009), and cable television (Seo 2006).

Based on this framework, when information disseminates perfectly in the market, we first specify the conditions under which well-behaved consumer heterogeneity can explain the observed adoption path, and, if such conditions are satisfied, we explicitly derive the analytical closed-form expression for the consumer valuation distribution. We further extend our analysis to the more general and realistic case in which information disseminates imperfectly (i.e., some consumers do not update instantaneously their information about the current state of the market) and derive corresponding results, discussing also the impact of awareness on adoption. We illustrate how faster adoption can be the result of either an increased distribution skewness toward high valuation customers or a faster information dissemination rate. We also discuss scenarios in which different subscription curves obtained under separate parameters and consumer distributions may share a common path in the beginning but might diverge in the future, highlighting the practical importance for providers to understand demand-side information refresh rate. Moreover, we show that it is possible that in the later part of the service lifecycle the subscription decision for new customers be driven predominantly by information dissemination instead of further price markdowns. In this sense, our analysis also advances the understanding of the drivers of service adoption in the later stages.

In the second half of the paper, based on our model and analytic results, we propose discrete-time heuristic methods for estimating underlying consumer heterogeneity and forecasting future sales. In special cases, we also present a method to approximate the rate at which awareness spreads in the market. In an empirical exercise, we apply these heuristic methods to the Japanese mobile voice services market and explore various information dissemination scenarios.

The remainder of the paper is organized as follows. We introduce the consumer utility model in §2. We then characterize the underlying consumer heterogeneity supporting observed aggregate adoption paths in §3. We first explore the case of perfect information dissemination in §3.1 and then study the case of imperfect information dissemination in §3.2. We extend our results to time-varying consumer valuation scenarios in §4. In §5, we propose various discrete-time heuristic methods based on our model and results, and, in an empirical illustration, we apply these methods to the Japanese mobile voice services market in §6. We conclude in §7. For brevity, all proofs and additional discussions are included in the online supplement available at http://dx.doi.org/10.1287/ isre.1120.0422.

## 2. The Consumer Utility Model

We focus our analysis on IT-intensive subscriptionbased services characterized by negligible installation or cancellation costs. Several on-demand video streaming services (e.g., Hulu Plus, Netflix), online music services (e.g., Rhapsody), or online backup services (e.g., Dropbox and Mozy) fit this pattern closely. Some telecommunications service providers are also beginning to offer their services on a month-to-month basis without cancellation fees and, in some cases, no installation, activation, or sign-up fees associated. For example, in June 2010, Verizon started offering FiOS bundles (mixing some or all of HD cable TV, Internet, and home phone services) on a month-to-month basis (no term contract), with waived activation fee for online orders, no cancellation fees, and most of the auxiliary equipment rented on a monthly basis or free with negligible installation fees (Cheng 2010). Furthermore, Verizon and AT&T also allow monthto-month subscription to their wireless voice and data services without early termination fees (Verizon Wireless 2008, AT&T 2008).<sup>2</sup> Similar subscription pay schemes with negligible upfront fees are also being employed by numerous publishers of massive multiplayer online games.

We consider a competitive market scenario for substitutable IT services where the providers are price takers and we explore aggregate (as opposed to firmlevel) market growth based on new users adopting the service from one of the existing providers. In that sense, migration of customers from one service provider to another has no direct impact on the size of the aggregate market. Subscription-based IT services are technology-intensive and, unlike laborintensive services, they are characterized by decreasing marginal costs per features/content/performance level per user per unit of time due, in part, to the decrease in cost and increase in performance of the available supporting technological infrastructure. Hence, corresponding relative subscription rates per features/content/performance level usually follow a decreasing pattern as competition pushes prices toward marginal costs. Note that in the case of onetime-purchase products a critical customer-mass buildup may justify a penetration pricing strategy due to network effects as past adopters are not influenced by present prices and thus they may remain in the installed base in spite of a price increase. However, it is important to point out that in the case of competitive markets for subscription-based IT services firms often resist increasing rates, because consumers recurrently purchase usage per time period instead of lifetime usage. Thus, past customers would be affected by current prices and, in association with a price hike, may either switch to a competing provider or abandon the service class altogether (i.e., not subscribe to the service under any of the providers). Hence, if the service characteristics are time invariant, then subscription rates are likely to decrease over time. We use this setting throughout our baseline analysis (§§2 and 3) and consider an exogenously given market price (weakly) decreasing over time, which is consistent with the empirical data we analyze to illustrate our theoretical framework. We will later extend (in §4) the framework to account for the fact that service characteristics may be enhanced over time and price may be occasionally increasing.

We assume a continuum of potential consumers whose utility rates at time t depend on their intrinsic benefit  (hereafter referred to as the customer type) and marginal network benefit $\nu > 0$ (i.e., positive network effects) of the service. Various services exhibit different network effect patterns. For example, in the case of online collaboration tools delivered under software-as-a-service model $( \mathrm { e . g . }$ , Acrobat.com, Google Apps for Business, Zoho Collaboration Apps), massive multiplayer online games (e.g., Blizzard’s World of Warcraft), online social dating sites $( \mathrm { e . g . } ,$ Match.com), or mobile voice services (e.g., AT&T, Verizon), network effects might be relatively large as users interact with each other extensively. On the other hand, for other IT services such as satellite radio $( \mathrm { e . g . }$ , Sirius XM), cable television, or automotive telematics (e.g., GM’s OnStar and Toyota’s GBook systems) the network effects might be considerably smaller on a relative scale as users can derive value from the service without necessarily interacting a lot with each other. As mentioned above, for ease of exposition, in our baseline model (§§2 and 3), we assume that customer types and marginal network effects are time invariant, and type  is distributed according to a smooth distribution function $F \ ( \in { \mathcal { C } } ^ { 2 } )$ over the interval 6 1 7<sup>¯</sup> . Furthermore, in line with the previous pricing assumptions, we consider that the service is offered at an exogenously given positive subscription rate $p ( t )$ that is continuously differentiable and weakly decreasing in time. We later relax the above assumptions in §4 and show that our results still hold in a more general context.

A customer may join or quit the subscription service at any time without paying any registration or termination fees. A customer of type  derives the following instantaneous utility rate from consuming the service at time t:

$$
u _ {\theta} (t) = s _ {\theta} (t) \times (\theta + \nu \cdot N _ {F} (t) - p (t)), \quad \mathrm{for} t \in \mathbb {R} _ {+},\tag{1}
$$

where $N _ { F } ( t )$ represents a theoretical subscription path that results from our utility model under a given consumer type distribution F , and $s _ { \theta } ( t ) \in \{ 0 , 1 \}$ represents the subscription decision of a consumer of type  at time t. Note that in our baseline model, customers derive identical network benefits and are differentiated through heterogeneous intrinsic benefits from using the service. Similar models have been previously used in the literature (e.g., Katz and Shapiro 1985, Conner 1995, Saloner and Shepard 1995, Mitchell and Skrzypacz 2005, Argenziano 2008, Cheng and Tang 2010, Cheng and Liu 2010). Conditional on her subscription decision function over time $s _ { \theta } \colon [ 0 , \infty ) \to \{ 0 , 1 \} .$ , a consumer of type  captures the following total utility from the service:

$$
\begin{array}{c} U (\theta \mid s _ {\theta}) = \int_ {0} ^ {\infty} u _ {\theta} (t) d t \\ = \int_ {0} ^ {\infty} s _ {\theta} (t) \times (\theta + \nu N _ {F} (t) - p (t)) d t. \end{array}\tag{2}
$$

Let $\mathbb { S } = \{ \tilde { s } | \tilde { s } \colon [ 0 , \infty ) \to \{ 0 , 1 \} \}$ represent the set of feasible consumer subscription decision functions. In our model, customers exhibit rational behavior in the sense that they try to maximize the overall utility from the service via subscription decisions over time:

$$
s _ {\theta} ^ {*} = \operatorname * {a r g   m a x} _ {s _ {\theta} \in \mathbb {S}} U (\theta \mid s _ {\theta}).\tag{3}
$$

Furthermore, we assume that the consumer market for the service is very large such that consumer collusion at adoption level, if any, is negligible. Because we consider a continuum of consumers, the action of an individual consumer will bear no impact on the actions of others. Consumers make their purchase decision individually based on their belief and expected evolution of the market. In the absence of collusion, we focus on the analysis of IT-intensive subscription services without substantial signup or cancellation costs, which, given the option of repeated subscription renewals, induce a myopic consumer behavior based on the current information set.<sup>3</sup> More precisely, rational consumers will subscribe in a given time period if the expected instantaneous utility rate for that particular period (based on their current information set) is nonnegative. Because the game (subscription decision) is repeated in the next period, any anticipated future decrease in price or increase in installed base does not impact the decision during the current period.

Some customers may not be immediately aware of new services or recent changes in market conditions due to slow dissemination of information (see, e.g., Dodson and Muller 1978, Kalish 1985, Horsky 1990, Morris and Shin 2006). In this paper, we employ a sticky-information model similar to the one in Mankiw and Reis (2002), whereby at any given moment, only a fraction $\alpha \in ( 0 , 1 ]$ of the potential customers update the current information on market primitives $( \mathrm { e . g . , }$ existence of or subscription rate for the service) to the current state. Furthermore, prior to adoption, each customer is equally likely to update her information, regardless of how much time has elapsed since her last update. In our model, once a consumer subscribes, it does not matter whether she changes her information refresh rate post-adoption.

When adoption started at time t or before, we denote by $\bar { \theta ( t ) }$ the lowest-type customer whose real instantaneous utility would be nonnegative at time t in equilibrium if she adopted; that is,

$$
\theta (t) = \max \bigl \{p (t) - \nu N _ {F} (t), \underline {{\theta}} \bigr \}.\tag{4}
$$

Let m denote the total market potential. We define Q4t5 as the pool of qualified potential customers at time $t ,$ i.e., those potential customers whose real instantaneous utility would be positive at time t if they subscribe, or, equivalently,

$$
Q (t) \triangleq m \bar {F} (\theta (t)),\tag{5}
$$

where $\bar { F } ( \theta ( t ) ) = 1 - F ( \theta ( t ) )$ . Unless $\alpha = 1$ , at any given time $t ,$ some of the qualified consumers make their subscription decision based on outdated sticky information that may induce a fraction of them to delay subscribing to the service; that is, $N _ { F } ( t ) \leq Q ( t )$ . Once a consumer subscribes to the service, she will continue to subscribe in the future because of the nonincreasing price pattern. When $\alpha = 1$ , we point out that $N _ { F } ( t ) = \bar { Q } ( t )$

At any time $t > 0 ,$ assuming continuity of the adoption path, new subscribers come from two subgroups. The first subgroup, of size $Q ( t ) \mathrm { ~ - ~ } N _ { F } ( t )$ consists of qualified customers who had positive instantaneous utility rate prior to time t but had not adopted yet because they were not aware of current market conditions. Among those,  proportion of them update to the current information at time t and consequently adopt. The second subgroup, of size $\dot { Q } ( t ) = \dot { \partial } Q / \partial \dot { t } .$ , consists of potential customers who just became qualified because their instantaneous utility rate turned positive in the immediate vicinity of t. Similarly,  proportion of them become informed and subsequently adopt at time t. Thus, the sticky-information model yields the following adoption dynamics:

$$
\dot {N} _ {F} (t) = \alpha \big [ Q (t) - N _ {F} (t) \big ] + \alpha \dot {Q} (t).\tag{6}
$$

To ensure the uniqueness of the continuous adoption path as a result of the equilibrium in continuous time, we impose the following regularity conditions:

(RC) The type distribution F satisfies

(i) $F \in \mathcal { C } ^ { \bar { 2 } }$ and $0 < f ( \theta ) < 1 / ( \alpha \nu m ) , \forall \theta \in [ \underline { { \theta } } , \bar { \theta } ] ,$

$$
\text {(ii)} \theta + \nu m \bar {F} (\theta) <   \bar {\theta}, \forall \theta <   \bar {\theta}.
$$

A distribution F satisfying condition (RC.i) associates nonzero density with every customer type. Furthermore, it also requires that the magnitude of the network effects is not so strong to lead to the jumps in the adoption path. In addition, (RC.ii) is related to a unique and smooth adoption at time $t = 0 .$ If (RC) is violated, there may be sudden jumps in the subscription base due to large masses of customers clustered around certain type values, or there may exist multiple equilibria. We present a detailed discussion and examples of such cases for $\alpha = 1$ in Online Supplement B.

## 3. Characterization of Implied Consumer Heterogeneity

In the previous section we have introduced a subscription model based on consumer utility maximization. Next, we explore whether a smooth observed aggregate adoption path can be explained through this consumer utility framework. Through this analysis, we advance the understanding of consumer subscription behavior based on rational consumer choice.

Let $N ( t )$ be the size of the actual installed base of adopters at time t that we observe from the data. Define $G ( t )$ as the fraction of subscribers at time $t ,$ i.e., $G ( t ) \triangleq N ( t ) / m .$ . In this study, we focus on smooth increasing adoption curves (G is differentiable and $g ( t ) \triangleq \dot { G } ( \check { t } ) ( = \partial \mathbf { \hat { G } } / \partial t ) > 0 )$ with no instantaneous mass of adopters $( G ( 0 ) = 0 )$ and full saturation attained asymptotically $( \dim _ { t \to \infty } G ( t ) = 1 )$ .

One of our primary goals is to estimate a consumer type distribution F that can explain an observed continuous adoption path G under our utility model, $\mathrm { i . e . , }$ to derive the consumer type distribution(s) F such that the corresponding theoretical subscription path $N _ { F } ( \cdot )$ matches the observed subscription path $N ( \cdot )$ We first focus on the simple idealized case of perfect information dissemination in which $\alpha = 1$ in $\ S 3 . 1$ We then consider the more realistic, imperfect information dissemination case in which $0 < \overset { \cdot } { \alpha } < 1$ in §3.2.

## 3.1. Perfect Information Dissemination

In this section, we consider perfect information dissemination, $\mathrm { i } . \mathrm { e } . , \alpha = 1$ , where all qualified consumers are aware of the service existence and its current market attributes such as prices and subscription base. Consider the case where firms are customers of IT services. We would expect some of the markets for niche IT subscription-based enterprise services to exhibit fast information dissemination rates, thus being close to this idealized case. In competitive environments, companies nowadays are increasingly proactive in keeping up to speed with the market evolution and available solutions in a continuous effort to boost competitive advantage by increasing efficiency, cutting costs, and enhancing their portfolio of products and services offered. Some of this information search is conducted internally by IT departments within the firms. In addition, recognizing the potential high impact of such IT services on firms’ performance at all levels of the value chain, a mature and rapidly growing IT consulting industry focuses on delivering value to enterprises by identifying and recommending improved IT solutions based on most current products and services available. Furthermore, information about a particular solution is also spread in the market by IT services companies specialized in the implementation and integration of that solution.

In this case, $Q ( t ) = N _ { F } ( t ) \stackrel { \smile } { = } m \bar { F } ( \theta ( t ) )$ for all $t ,$ and the adoption path is characterized by Equations (4) and (5). Furthermore, (RC.i) implies that $\overset { \bullet } { \boldsymbol { \theta } } + \nu m \bar { F } ( \boldsymbol { \theta } )$ is strictly increasing in $\theta ,$ and hence, (RC.i) implies (RC.ii).

The following result characterizes the existence and explicit form of a well-behaved consumer type distribution that can generate the observed adoption path G under our microstructure model.

Theorem 1. <sub>Let</sub>

$$
\begin{array}{c} \tilde {\mathcal {P}} \triangleq \big \{p (\cdot) \mid p \colon [ 0, \infty) \to \mathbb {R} _ {+},   p (0) = \bar {\theta}, \\ \dot {p} (\cdot) <   0,   p (\infty) = \underline {{\theta}} + \nu m \big \}, \end{array}\tag{7}
$$

where $p ( \infty ) = \mathrm { l i m } _ { t  \infty } p ( t )$ . If  = 1, then the following results hold:

(a) If $\begin{array} { r } { p \in \tilde { \mathcal { P } } . } \end{array}$ , then there exists a unique consumer type distribution F satisfying 4RC5 that generates the observed adoption path G4t5, which is given by

$$
F (\theta) = 1 - G (\sigma^ {- 1} (\theta)),\tag{8}
$$

where $\sigma ( t ) = p ( t ) - \nu m G ( t )$ . Moreover, $\sigma ( t ) = \theta ( t )$

(b) Otherwise, there does not exist any distribution F satisfying (RC) that can yield G4t5.

For the price paths in ${ \tilde { \mathcal { P } } } ,$ first, $p ( 0 ) = \bar { \theta }$ ensures that the adoption starts smoothly at $t = 0$ . Otherwise, either adoption does not start at $t = 0 \ ( p ( 0 ) > \bar { \theta } )$ , or there is a jump at $t = 0 \ ( p ( 0 ) < \bar { \theta } )$ . Next, if $p ( \infty ) > \underline { { \theta } } +$ $\nu m ,$ the lowest type customer never subscribes to the service, and hence $\begin{array} { r } { \operatorname* { l i m } _ { t  \infty } G ( t ) < 1 } \end{array}$ . Therefore, no customer type distribution F that contains nonzero mass around the lowest type—in particular, distributions satisfying condition (RC.i)—can explain the observed adoption path G that asymptotes to one. In contrast, if $p ( \infty ) < \underline { { \theta } } + \nu m ,$ , the full adoption occurs in a finite time, which then cannot satisfy a strictly increasing adoption path $( g ( t ) > 0 )$ afterward. In addition, if $\dot { p } ( t ) = 0$ , then adoption stalls momentarily. Consequently, $p ( \infty ) = \underline { { \theta } } + \nu m$ together with $\dot { p } ( \cdot ) < \dot { 0 }$ ensures a strictly increasing adoption path.

Theorem 1 provides the analytical closed-form representation of the consumer heterogeneity that explains the observed adoption path based on consumer utility optimization. This result can be of important managerial relevance. For example, firms can derive portions of the consumer distribution F from the observed adoption path, fit a parameterization to ${ \mathrm { i t } } ,$ and then estimate the unobserved distribution of types who have not adopted yet and forecast future sales (as will be detailed in §5). We present a simple example to better illustrate Theorem 1.

Example 1. <sub>Consider</sub> $\alpha = 1$ . Suppose that $G ( t ) =$ $1 - e ^ { - t }$ and $p ( t ) = ( 1 + e ^ { - t } ) / 2$ . Further, assume that $\nu m = 1 / 2 , \ \underline { { \theta } } = 0 ,$ , and $\bar { \theta } = 1$ . Note that $p \in \tilde { \mathcal { P } }$ holds. In this case, $\sigma ( t ) = e ^ { - t }$ , and the corresponding $F ( \theta ) = \theta .$ for $\theta \in [ 0 , 1 ] , \mathrm { i . e . , } \theta \sim U [ 0 , 1 ] .$ 

Interestingly, note that the simple uniform type distribution in Example 1 can generate exponentially decaying adoption path in equilibrium under our consumer utility model.

## 3.2. Imperfect Information Dissemination

In this section, we consider the case of $\alpha \ : < 1 .$ which allows us to explore significantly more realistic scenarios. First, it is more likely that information disseminates in an imperfect way. Second, note that customers adopt in the decreasing order of their types under perfect information dissemination $( \alpha = 1 )$ . However, under imperfect information dissemination, we accommodate a more plausible scenario where this adoption ordering is not required, as new adopters do not have to be only the newly qualified customers but can be previously qualified customers as well, as detailed in Equation (6). Third, as it will be further demonstrated in this section, imperfect information dissemination $( \alpha < 1 )$ also enables us to derive the consumer type distribution when the price is weakly decreasing, compared to a strictly decreasing price path as required in Theorem 1 in §3.1.

Depending on the characteristics of the subscription services, the information dissemination factor may vary. For example, if the services are related to hedonic consumption (e.g., video-on-demand services or online music streaming services), then one might expect them to exhibit lower information dissemination compared to utilitarian services related to necessities $( \mathrm { e . g . }$ , mobile voice services or Internet access) that engender more information seeking from customers.

For a distribution F satisfying (RC) to generate a smooth adoption path, it is further necessary to have $p \in \mathcal { P }$ , where

$$
\begin{array}{c} \mathcal {P} = \big \{p (\cdot) \mid p \colon [ 0, \infty) \to \mathbb {R} _ {+},   p (0) = \bar {\theta}, \\ \qquad \qquad \qquad \dot {p} (0) <   0,   \dot {p} (\cdot) \leq 0 \big \}. \end{array}\tag{9}
$$

Note that $p \in \mathcal { P }$ guarantees a smooth adoption path at time 0. In this case, adoption never stalls, provided that $p \in \mathcal { P }$ . Because of dissemination of updated information, the installed base is strictly increasing even when all potential consumers are qualified. Supporting Lemmas A1 and A4 in the Online Supplement A discuss these properties. Further, as discussed in §3.1, for a distribution $F$ satisfying (RC) to yield full asymptotic adoption, price paths should satisfy $p ( \infty ) \leq \underline { { \theta } } + \nu m$

$$
t _ {G} \triangleq \inf \left\{t \mid \underline {{\theta}} + \nu m G (t) \geq p (t) \right\},\tag{10}
$$

denote the earliest time at which all customers are qualified if the adoption path follows $G ;$ in other words, even the customer with the lowest type $\underline { { \theta } }$ is willing to adopt the service at time $t _ { G }$ if she is aware of the current information. Because $p ( \infty ) \leq \underline { { \theta } } + \nu m$ and $p \in \mathcal { P } , t _ { G }$ is uniquely defined, and $\underline { { \theta } } + \nu m G ( t _ { G } ) = p ( t _ { G } )$ For technical reasons, in addition to the previous conditions, we assume that $G ( \cdot )$ is twice continuously differentiable up to $t _ { G } .$

For expositional clarity, we break down the analysis and first study the case in which full qualification can only happen in an infinite time, i.e., $t _ { G } = \infty ,$ in §3.2.1. We then explore the case in which full qualification occurs in a finite time, i.e., $t _ { G } < \infty ,$ in §3.2.2.

3.2.1. Full Qualification in Infinite Time. In this section, we study the case where $p ( \infty ) = \underline { { \theta } } + \nu m$ . Note that, in this case, the lowest type consumer, , is qualified only at time infinity; that is, $t _ { G } = \infty$ . We next derive the consumer heterogeneity implied by the observed adoption path, $G ,$ and the observed price path, $p { : }$

Theorem 2. <sub>(a) Under</sub> $p \in \mathcal { P } , \ p ( \infty ) = \underline { { \theta } } + \nu m ,$ and $\alpha < 1$ , if the following two conditions are satisfied for all $t > 0 ,$

$$
\mathrm{(i)} (1 - \alpha) \frac {\int_ {0} ^ {t} e ^ {- (t - z)} g (z) d z}{g (t)} <   1; a n d
$$

$$
\text {(ii)} \frac {(1 - \alpha)}{\alpha} \int_ {0} ^ {t} e ^ {- (t - z)} g (z) d z <   \frac {p (0) - p (t)}{\nu m},
$$

then there exists a unique $F _ { \alpha }$ that satisfies (RC) and induces the observed service adoption path $G ,$ and it is given by

$$
F _ {\alpha} (\theta) = 1 - \frac {1}{\alpha} \int_ {0} ^ {\sigma^ {- 1} (\theta)} e ^ {z - \sigma^ {- 1} (\theta)} [ g (z) + \alpha G (z) ] d z,\tag{11}
$$

where $\sigma ( t ) = p ( t ) - \nu m G ( t )$

(b) If either condition (i) is violated or $p \notin \mathcal { P } .$ , there does not exist any consumer type distribution F satisfying (RC) that can generate G in association with the given .

Condition (i) is a necessary condition for the existence of a well-behaved consumer heterogeneity distribution function, i.e., satisfying (RC). Note that the numerator on the left-hand side of condition (i) contains the information on the historical adoption rate, $g ( s ) { \mathrm { ~ f o r ~ } } s \in [ 0 , t ]$ , with a heavier discount for rates further in the past. It is useful to illustrate the meaning of this condition in the context of traditional S-shaped adoption curves. As long as the adoption rate, $g ( t )$ is weakly increasing (early adoption), condition (i) is always satisfied. When/if g4t5 starts to decrease (later adoption, beyond inflexion point, closer to market saturation), this condition restricts the adoption speed decay rate contingent on the information dissemination factor $\alpha ,$ in the sense that it cannot decay too fast. Technically, it guarantees that the function (11) is a proper distribution function; specifically, F is strictly increasing in . Condition (i) furthermore provides a lower bound for  based solely on aggregate adoption data. Information dissemination rates may be hard to estimate directly in practice. As we see from Figure 1, provided that  is high enough, slight approximation errors will still yield a fairly robust estimation of the distribution. Note that conditions (i) and (ii) are both automatically satisfied when $\alpha = 1$

Condition (ii) provides a lower bound on how fast the subscription rate $p ( t )$ can decrease for a given information factor. For example, when information disseminates slowly, i.e., under low $\alpha ,$ in order to generate further adoption, the price should decrease fast enough. At the same time, condition (ii) can also be interpreted as another lower bound for  given that $( 1 - { \bar { \alpha } } ) / \alpha$ is decreasing in . Furthermore, technically, this condition guarantees that F satisfies (RC.ii).

Theorem 2 provides the complete analytical characterization of the consumer heterogeneity that explains the observed adoption path based on consumer utility optimization under imperfect information dissemination and full qualification in infinite time. We present two examples and a figure to better illustrate Theorem 2.

Example 2. <sub>Consider</sub> $p ( t ) = b + a e ^ { - \beta t }$ and $G ( t ) =$ $1 - e ^ { - \beta t }$ . Further, suppose that $\underline { { \theta } } = b - \nu m$ and ${ \bar { \theta } } = a + b$ with $1 / 2 < \beta \leq \alpha < \bar { 1 }$ and $\nu m \leq a$ . Note that $p ( t )$ is strictly decreasing with $p ( 0 ) = \bar { \theta }$ and $p ( \infty ) = \underline { { \theta } } + \nu m$ Both conditions (i) and (ii) in Theorem 2 are satisfied for $t > 0 .$ . In this case, $\sigma ( t ) = \underline { { \theta } } + ( \bar { \theta } - \underline { { \theta } } ) e ^ { - \beta t }$ , from which we obtain $\sigma ^ { - 1 } ( \theta ) = - ( 1 / \beta ) \ln ( \theta - \underline { { { \theta } } } ) / ( \bar { \theta } - \underline { { { \theta } } } )$ Then from (11), it follows that

$$
= \frac {(\alpha - \beta) (\theta - \underline {{\theta}}) + \beta (1 - \alpha) (\bar {\theta} - \underline {{\theta}}) ((\theta - \underline {{\theta}}) / (\bar {\theta} - \underline {{\theta}})) ^ {1 / \beta}}{\alpha (1 - \beta) (\bar {\theta} - \underline {{\theta}})}.
$$

## Figure 1 Illustration of Theorems 1 and 2 via Example 2

(a) Observed relative service adoption path  
![](/api/attachments/DZ5BGA4U/fulltext/images/fa74dd8358c809941cb0d95ac694b570f1871b2c3b03122a9ba31a0d86521e6c.jpg)

(b) Derived consumer type distribution  
![](/api/attachments/DZ5BGA4U/fulltext/images/c25425cc92ba9446a9805d87998d59e6b8d5b913d829dadb76b8e4bfcce02153.jpg)  
Notes. Panel (a) plots an actual observed adoption path over time. Panel (b) plots the derived underlying consumer type distribution based on the individual utility model under five different values of information dissemination factor $\alpha = 0 . 1 , 0 . 3 , 0 . 5 , 0 . 7 , 0 . 9 , 1$ . The specification and the remaining parameter values are $p ( t ) = 0 . 5 + 1 . 5 \theta ^ { - 0 . 1 t } , G ( t ) = 1 - e ^ { - 0 . 1 t } , m = 1$ , and $\nu = 0 . 5$

The probability density function is then

$$
f _ {\alpha} (\theta) = \frac {\alpha - \beta + (1 - \alpha) ((\theta - \underline {{\theta}}) / (\bar {\theta} - \underline {{\theta}})) ^ {(1 / \beta) - 1}}{\alpha (1 - \beta) (\bar {\theta} - \underline {{\theta}})}.
$$

Note that, as a special case, if $\alpha = \beta , \ \underline { { { \theta } } } = 0 ,$ , and $\bar { \theta } = 1$ , then this distribution becomes Beta $( 1 / \alpha , 1 )$ distribution. We point out that we can also consider the case of $\alpha = 1$ , leaving the rest of parameter specifications unchanged, which represents a valid example for Theorem 1. This example is also illustrated in Figure 1. <sup></sup>

In Example 2, the complete retrieval of type distribution $F ( \theta )$ benefits from the fact that we can explicitly invert $\sigma ( \theta )$ . However, even if we cannot invert $\sigma ( \theta )$ explicitly, Theorem 2 can still be used to obtain a full characterization of consumer type distribution, as illustrated in Example 3.

Example 3. <sub>Consider</sub> $p ( t ) = b + a e ^ { - t }$ and $G ( t ) =$ $1 - e ^ { - \beta t }$ . The rest of the parameters obey all conditions given in Example 2. The only difference from Example 2 is that the specification of $p ( t )$ does not contain $\beta .$ It can be easily seen that conditions (i) and (ii) in Theorem 2 are satisfied. In this case, we do not have an explicit form for $\sigma ^ { - 1 } ( t )$ . Nevertheless, given that $\sigma ( t )$ is a bijection from 601 5 to $[ \underline { { \theta } } , \bar { \theta } ] .$ , consumer heterogeneity is given by the following system of equations

$$
\sigma (t) = b - \nu m + a e ^ {- t} + \nu m e ^ {- \beta t} \quad \text { and }
$$

$$
F _ {\alpha} (\sigma (t)) = \frac {\beta (1 - \alpha) e ^ {- t} + (\alpha - \beta) e ^ {- \beta t}}{\alpha (1 - \beta)}. \quad \square
$$

As illustrated in Examples 2 and $^ { 3 , }$ and Figure $^ { 1 , }$ we can derive consumer type distribution $F _ { \alpha }$ from the observed adoption path and the price path for a given information dissemination factor, . Further, in these examples, note that all pairs $\{ \alpha , F _ { \alpha } ( \cdot ) \}$ for $\alpha \in [ \beta , 1 )$ yield the same adoption path $G ( t )$ . To better understand this outcome, suppose that we have two different scenarios $\{ \alpha _ { 1 } , F _ { \alpha _ { 1 } } \}$ and $\{ \alpha _ { 2 } , F _ { \alpha _ { 2 } } \}$ , such that $\alpha _ { 1 } > \alpha _ { 2 } ,$ but $F _ { \alpha _ { 7 } }$ has more of high types and less of low types than $\hat { F } _ { \alpha _ { 1 } } \ ( \mathrm { i . e . , } \ F _ { \alpha _ { 2 } }$ stochastically dominates $F _ { \alpha _ { 1 } } )$ . Then, under $\alpha _ { 2 } ,$ , a higher fraction of consumers are qualified, but fewer of them have current market information, while the opposite happens under $\alpha _ { 1 }$ . This way, these different settings could potentially yield an identical subscription path $G ( t )$ . The result is formalized next:

Proposition 1. <sub>For</sub> $p \in \mathcal { P } , \mathrm { ~ } i f \mathrm { ~ } t _ { G }$ is infinite, or equivalently, $p ( \infty ) = \underline { { \theta } } + \nu m _ { \cdot }$ , then

(a) if for some value $\alpha < 1 ,$ , all conditions in Theorem 2 are satisfied, then these conditions also hold $f o r$ all $\tilde { \alpha } \in ( \alpha , 1 ) ,$ ;

(b) either 415 there does not exist any $\alpha < 1$ such that a corresponding $F _ { \alpha }$ satisfying 4RC5 generates $G ( t )$ , or 425 there exists a continuum of pairs $\left\{ \alpha , F _ { \alpha } \right\}$ with $\alpha < 1$ and $F _ { \alpha }$ satisfying 4RC5, which yield the subscription path $G ( t ) ;$ moreover, both scenarios are possible;

(c) if for both $\alpha _ { 2 } < \alpha _ { 1 } < 1$ , all conditions in Theorem 2 are satisfied, then $F _ { \alpha _ { 2 } }$ stochastically dominates $F _ { \alpha _ { 1 } }$ (and, implicitly, $Q _ { 2 } ( t ) \geq Q _ { 1 } ^ { - } ( t )$ for all $t \geq 0 )$

Figure 1 illustrates Proposition 1. As can be seen in Figure 1(b), different  values can generate the same adoption path G4t5 depicted in Figure 1(a). Furthermore, as stated in part (c) of Proposition 1, the underlying consumer type distribution corresponding to the lower  values stochastically dominates the distribution corresponding to the higher  values. In this sense, estimating the  values is important in order to understand the consumer type distribution. However, as we can see in Figure 1(b), for this example, as long as the  values are relatively large, e.g., greater than 005, the consumer type distribution functions do not change much; that is, the type distribution can be robust for certain  values.

So far, we have studied a given market with an observed adoption path and we explored different scenarios with various information dissemination rates  that lead to this adoption path. We end this section by discussing the relevance of our results in the context of similar markets (in terms of prices, network effects, and market potentials) that exhibit different adoption paths. We compare the impact of information dissemination rates and adoption speeds on consumer heterogeneity. Figure $2 ( \mathsf { a } )$ depicts different adoption paths $G _ { 1 }$ and ${ \bar { G } } _ { 2 } ,$ where $G _ { 2 }$ captures faster adoption compared to $G _ { 1 }$ . Ignoring the impact of information dissemination (i.e., under fixed ), one would expect that faster adoption in the beginning be induced by larger mass around high type consumers. Indeed, we observe this point by comparing $f _ { 1 } \mid _ { \alpha = 0 . 7 5 }$ and $f _ { 2 } \mid _ { \alpha = 0 . 7 5 }$ in Figure 2(b), which illustrates the consumer type density function generating the actual adoption paths in Figure $2 ( \mathsf { a } ) ; \bar { f } _ { i }$ yields the adoption path $G _ { i } , \mathrm { f o r } i = \{ 1 , 2 \}$ . However, if one factors information dissemination rates into consideration, the relationship can change. For example, note that $f _ { 2 } \mid _ { \alpha = 0 . 9 }$ also generates $G _ { 2 } ,$ which represents faster adoption than $G _ { 1 }$ induced by $f _ { 1 } \mid _ { \alpha = 0 . 7 5 }$ . In this case, the density function $f _ { 2 } \mid _ { \alpha = 0 . 9 }$ has relatively fewer high-type consumers than $f _ { 1 } \mid _ { \alpha = 0 . 7 5 }$ . However, it generates faster adoption because of faster information dissemination.

Figure 2 Comparison of Two Different Adoption Paths and the Corresponding Underlying Consumer Type Distributions  
![](/api/attachments/DZ5BGA4U/fulltext/images/b1875017a8b2e669300e3e0e14cf1c3b85f6392d91bbd7e3156cda4d130f2ccb.jpg)

(b) Consumer type density function  
![](/api/attachments/DZ5BGA4U/fulltext/images/6f82967cb2415eb8bab51cc125699ca584da8b2b56cc079491efac864c9aa779.jpg)  
Notes. Panel (a) plots two different adoption paths: $G _ { 1 } ( t ) = 1 - e ^ { - 0 . 5 t }$ and $G _ { 2 } ( t ) = 1 - e ^ { - 0 . 6 5 t }$ . Panel (b) plots the corresponding underlying consumer type densities with the specified  values: $f _ { \uparrow }$ for $G _ { \ u { 1 } }$ and $f _ { 2 }$ for $G _ { 2 } .$ . The price path is $p ( t ) = 1 + e ^ { - t }$ for both. The remaining parameter values are $m =$ 10 and $\nu = 0 . 0 1$ . These parameter values and price function satisfy conditions (i) and (ii) in Theorem 2.

3.2.2. Full Qualification in Finite Time. In the previous sections, we have considered the case in which the lowest type customer can only be qualified in infinite time, i.e., $t _ { G } = \infty ,$ , or equivalently, $p ( \infty ) = \underline { { \theta } } + \nu m$ . We now consider the less restrictive case in which the lowest type customer is qualified in finite time; that is, $t _ { G }$ is finite.

Theorem 3. <sub>(a) Under</sub> $p \in \mathcal { P } , \ p ( \infty ) < \underline { { \theta } } + \nu m ,$ and  < 1, if the conditions (i) and (ii) for $t \in [ 0 , t _ { G } )$ in Theorem 2 and the following conditions (iii) and (iv) are jointly satisfied,

$$
\mathrm{(iii)} \int_ {0} ^ {t _ {G}} e ^ {z - t _ {G}} [ g (z) + \alpha G (z) ] d z = \alpha ;
$$

(iv) there exists $t _ { c } \in [ 0 , t _ { G } ]$ such that

$$
\frac {g (t)}{1 - G (t)} = \alpha \quad f o r a l l t \in [ t _ {c}, \infty),
$$

then there exists a unique distribution $F _ { \alpha }$ that satisfies 4RC5 and induces the observed service adoption path $G ,$ and it is given by

$$
F _ {\alpha} (\theta) = 1 - \frac {1}{\alpha} \int_ {0} ^ {\inf \{\sigma^ {- 1} (\theta) \}} e ^ {z - \inf \{\sigma^ {- 1} (\theta) \}} [ g (z) + \alpha G (z) ] d z,\tag{12}
$$

where $\sigma ( t ) = \operatorname* { m a x } \{ \underline { { \theta } } , p ( t ) - \nu m G ( t ) \}$

(b) If any of the conditions (i), (iii), or (iv) is violated, or p 6∈ P, there does not exist any consumer type distribution F satisfying 4RC5 that can generate G in association with the given .

Note that, compared to the analysis in Theorem $^ { 2 , }$ we require two more conditions, (iii) and (iv). First, when $t _ { G }$ is infinite as in §3.2.1, condition (iii) is always satisfied (see Lemma A7 in the Online Supplement A) and condition (iv) is not relevant. For $N _ { F } ( t ) =$ $N ( t ) = m G ( t )$ to hold, from the definition of $t _ { G } ,$ it must be true that $\theta ( t _ { G } ) = \underline { { \theta } } < \theta ( t )$ for any $t \in [ 0 , t _ { G } )$ Alongside condition $p ( \infty ) < \underline { { \theta } } + \nu m _ { \cdot }$ , condition (iii) captures the necessary dynamics between $\alpha , p ,$ and $G$ (and, implicitly $t _ { G } )$ that guarantee that, under the proposed distribution $F ,$ the lowest type customer becomes qualified precisely at time $t _ { G } .$ . Condition (iv) provides the adoption behavior after all consumers are qualified $( t > t _ { G } )$ . Beyond $t _ { G } ,$ the information dissemination and the associated awareness govern the adoption path; that is, the evolution of the adoption path in (6) becomes $\dot { N } _ { F } ( t ) = \alpha ( m - N _ { F } ( t ) )$ because $Q ( t ) = m$ and $\dot { Q } ( t ) = 0$ . Thus, the pool of qualified customers who have not adopted yet decays at a rate $\alpha ,$ which then yields an adoption path with a constant hazard rate  beyond $t _ { G } ,$ as stated in condition (iv).

We highlight here an important advantage of our microlevel adoption model over many industry-level aggregate diffusion models. Many extant aggregate growth models that include price effects are parameterized in the form $\dot { N } ( t ) = \tau ( \dot { N } ( t ) , p ( t ) )$ with $\partial \tau / \partial p < 0$ (e.g., Robinson and Lakhani 1975, Kalish 1983, Sethi and Bass 2003). According to these models, as long as full saturation has not been achieved, any further price markdowns accelerate adoption. By accounting for imperfect information dissemination, our model accounts for the fact that beyond a certain point $( t _ { G } ) .$ adoption may be solely driven by information dissemination given that full qualification has been attained. In such scenarios, aggregate models will fail to properly explain/forecast late adoption.

We present an example with a figure to demonstrate how to obtain the consumer type distribution when full adoption occurs in a finite time, as presented in Theorem 3.

<sup>Example</sup> <sup>4.</sup> Suppose that

$$
G (t) = \left\{ \begin{array}{l l} a _ {1} t & \text { if } t \leq t _ {c}; \\ 1 - e ^ {- \beta t} & \text { if } t _ {c} \leq t, \end{array} \right.\tag{13}
$$

where $a _ { 1 } = \beta ( 1 - 1 / e )$ . Then from the continuity, we obtain $t _ { c } = 1 / \beta$ . Suppose that $\theta = 0$ and $\bar { \theta } = 1 0$ . Furthermore, let $\nu m = 1$ . Denote $\delta = \beta ( \bar { \theta } - ( 1 - 1 / e ) )$ 5 and consider

$$
p (t) = \left\{ \begin{array}{l l} \bar {\theta} - \delta t & \text { if } t \leq \bar {\theta} / \delta ; \\ 0 & \text { if } \bar {\theta} / \delta \leq t. \end{array} \right.
$$

Then from (10), we obtain $t _ { G } = t _ { c } = 1 / \beta$ . Suppose that $\alpha = \beta$ and it is the unique solution in 601 17 that satisfies

$$
\left(1 - \frac {1}{e}\right) (2 - \beta - e ^ {- 1 / \beta} (1 - \beta)) = 1,\tag{14}
$$

which is about 003747. Then all conditions $( \mathrm { i } ) { - } ( \mathrm { i } \mathrm { v } )$ are satisfied. In this case, we have

$$
\sigma (t) = \left\{ \begin{array}{l l} \bar {\theta} - \delta t - a _ {1} t & \text { if } t \leq t _ {c}; \\ 0 & \text { if } t _ {c} \leq t. \end{array} \right.
$$

Taking an inverse function, we obtain $\sigma ^ { - 1 } ( \theta ) =$ $( \bar { \theta } - \theta ) / ( \delta + a _ { 1 } )$ , for $\theta \in [ \underline { { \theta } } , \bar { \theta } ]$ . Then, after simplification and using (14), the corresponding distribution function can be written as

$$
F _ {\alpha} (\theta) = \frac {1}{e} \times \frac {e ^ {\theta / (\beta \bar {\theta})} - 1}{e ^ {1 / \beta} - 1} + \left(1 - \frac {1}{e}\right) \times \frac {\theta}{\bar {\theta}},
$$

which is a weighted average of two distribution functions, one of which is U 601 7<sup>¯</sup> . Example 4 is illustrated in Figure 3 using a solid line. <sup></sup>

In Example $^ { 4 , }$ one important aspect to note is that the information dissemination factor  is uniquely determined in this case where full qualification occurs in a finite time. This observation actually holds in general as shown in the following proposition:

Proposition 2. <sub>For</sub> $p \in \mathcal { P } , ~ i f ~ t _ { G }$ is finite, or equivalently, $p ( \infty ) < \underline { { \theta } } + \nu m ,$ , there can be at most one $\alpha \in ( 0 , 1 )$ that can generate G4t5.

The result in Proposition 2 is in contrast with the result presented in Proposition 1, in which we have shown that when full qualification can happen only at an infinite time, there can exist a continuum of pairs $\{ \alpha , F _ { \alpha } \}$ that can generate the same observed adoption path G. When full qualification occurs in finite time, uniqueness of the information dissemination factor  is dictated by the necessity of G to exhibit a constant hazard rate from $t _ { G }$ onward, which implies $\alpha = g ( t ) / ( 1 - G ( t ) )$ for all $t \geq t _ { G } .$ . Thus, if we observe the adoption path over the entire time horizon, we can uniquely identify $\{ \alpha , F _ { \alpha } \}$ . From a practical perspective, one natural question to follow is whether the same result holds if we observe the adoption path only up to a given time t. The following proposition answers this practical question:

Proposition 3. <sub>Consider</sub> $p \in { \mathcal { P } } ,$ , and a pair $\{ \alpha , F _ { \alpha } \}$ satisfying 4RC5 that generates increasing smooth adoption path $G _ { \alpha } . ~ H t _ { G _ { n } }$ is finite, the following hold:

(a) For any $t _ { 1 } > t _ { G _ { \alpha } } ,$ there does not exist any other smooth adoption path $\mathbf { \bar { \cal G } } _ { 1 }$ supported by a pair $\{ \alpha _ { 1 } , F _ { \alpha _ { 1 } } \}$ satisfying 4RC5 such that ${ \dot { G } } _ { 1 } \not = G _ { \alpha }$ but $G _ { 1 } ( t ) = G _ { \alpha } ( { \dot { t } } )$ $\forall t \in \left[ 0 , \overline { { t } } _ { 1 } \right]$

(b) For $t _ { 0 } < t _ { G _ { \alpha } } ,$ it is possible to have multiple distinct adoption paths $G _ { 0 } ,$ each supported by a pair $\{ \alpha _ { 0 } , F _ { \alpha _ { 0 } } \}$ satisfying 4RC5 such that $G _ { 0 } \not = G _ { \alpha }$ but $\dot { G } _ { 0 } ( t ) = \dot { G } _ { \alpha } ( { t } )$ $\forall t \in [ 0 , \bar { t } _ { 0 } ]$

If the adoption path is observed up to $t _ { 1 } > t _ { G } ,$ the unique $\{ \alpha , \bar { \cal F } _ { \alpha } \}$ can be estimated from the adoption path $G ,$ as stated in part (a) of Proposition 3. This part provides the positive implication that we do not need to observe the complete adoption path to uniquely identify the customer type distribution and the information dissemination factor. As long as we observe the adoption path up to a time greater than the full qualification time, our methodology generates unique estimation of the customer type distribution.

## Figure 3 Illustration of Example 4 (Solid Line in All Three Panels) and Proposition 3

![](/api/attachments/DZ5BGA4U/fulltext/images/4a6e8b48f6ec8f89b27ae5ed739eebd234e32cc92ec80b817ded3d47d8fd3bd8.jpg)

![](/api/attachments/DZ5BGA4U/fulltext/images/8e2176ffca24d5568bcf46746f8c8a4770930049872bf1ee0dee990ea5aae62e.jpg)

![](/api/attachments/DZ5BGA4U/fulltext/images/2d1c7a1964b5797918ed9f064c06918ef3af86a98cf3a7edf9bb1c106c6a225e.jpg)  
Notes. Panel (a) plots the observed adoption path. Panel (b) depicts the hazard rate for adoptions over time. Panel (c) plots the derived underlying consumer type distribution. The functional forms of $G _ { 1 } ( t )$ and $p ( t )$ are given in Example 4 with $t _ { G _ { 1 } } = t _ { c }$ and $\alpha _ { 1 } = \alpha .$ . In addition, $G _ { 2 } ( t ) = a _ { 1 } t \mathrm { ~ i f ~ } t \leq t _ { 0 } , G _ { 2 } ( t ) = a _ { 1 } t +$ $a _ { 2 } ( t - t _ { 0 } ) ^ { 3 } \mathsf { i f } t _ { 0 } \le t \le t _ { G _ { 2 } }$ , and $G _ { 2 } ( t ) = 1 - a _ { 3 } e ^ { - \alpha _ { 2 } t } { \mathrm { ~ i f ~ } } t \geq t _ { G _ { 2 } }$ . The parameter values are $\beta = \dot { 0 } . 3 7 5 , m = 1 , \nu = 1 , a = 0 . 2 3 7 , \delta = 3 . 5 1 , \underline { { { \theta } } } = 0 , \bar { \theta } = 1 0 , a _ { 2 } = 0 . 2 3 7$ $a _ { 3 } = 0 . 7 3 8 , t _ { 0 } = 1 . 5 , t _ { G _ { 1 } } ^ { ' } = 2 . 6 7 , t _ { \theta _ { 2 } } = 2 . 5 9 , \alpha _ { 1 } = 0 . 3 7 5 , \dot { a } \mathrm { n d } \alpha _ { 2 } = 0 . 8 4 7$

However, one needs to be careful: If the adoption path G is specified only until $t _ { 0 } < t _ { G } ,$ many different pairs $\{ \alpha , F _ { \alpha } \}$ can be consistent with the observed data, but, the generated adoption path after $t _ { 0 }$ from different pairs $\{ \alpha , F _ { \alpha } \}$ may diverge as illustrated in Figure 3. Two different type distributions, as depicted in Figure $3 ( \mathrm { c } ) _ { i }$ , lead to the same adoption path up to the observed time period $t _ { 0 } ,$ diverging afterward, as illustrated in Figure 3(a). Furthermore, they also have different  values, i.e., the stabilized levels of hazard rates as depicted in Figure 3(b). In this case, one needs to estimate the information dissemination factor  from another source of data.

## 4. Extension: Increasing Product Valuation Over Time and

## Nondecreasing Subscription Rate

So far, we have considered the model in which intrinsic valuation  and marginal network benefit  are constant over time together with nonincreasing price path $p ( t )$ . It may be possible that the intrinsic valuation as well as the benefits derived via network effects are increasing over time because of consumer learning as well as the advances in technology, interconnectivity, and service versatility (variety of content delivered, tasks facilitated, or benefits received through that service). Such enhancements can also be accompanied by a price increase due to development and provision costs as well as increased willingness to pay of the customers. For example, very recently, Big Fish Games became the first publisher of casual games to be allowed to offer access to its products on iPad via a monthly subscription service (Satariano 2011). Under the current service, for a \$4.99 monthly rate, customers gain unlimited access to a library of games. A price increase to \$6.99 has been announced for early

2012, which will occur concomitantly with the addition of new games to the library. The intrinsic service valuation  is likely to increase for most customers as more video game content will be accessible per time period. Moreover, several such games have associated community rankings allowing players to benchmark performance against each other, consumer forums, multiplayer capabilities, and/or in-game chat functionality. Thus, an active network adds more value to each user. In addition, the strength of network effects may also increase in the future because more content might also be associated with more gameplay and, thus, more time spent interacting with other users per subscription period.

Suppose overall benefits increase over time at a rate $\gamma ( \cdot )$ with $\gamma ( t ) > 0$ and $\dot { \gamma } ( t ) > 0$ for all $t \geq 0 ,$ , and the instantaneous utility rate at time t for a consumer of type  is

$$
\begin{array}{l} \gamma (t) \times (\theta + \nu N (t)) - p (t) \\ = \gamma (t) \bigg (\theta + \nu N (t) - \frac {p (t)}{\gamma (t)} \bigg). \end{array}\tag{15}
$$

In the absence of significant lock-in fees, the analysis in $\ S 2$ remains valid and the subscription decision at time t depends on the sign of $\theta + \nu N ( \bar { t } ) - ( p ( t ) / \gamma ( t ) )$ because consumers become qualified as soon as their utility rate becomes positive. Note that in this case, as long as $p ( t ) / \gamma ( t )$ is decreasing, our previous results continue to hold via a simple transformation of p4t5 using $\tilde { p } ( t ) = p ( t ) / \gamma ( t ) . \mathrm { I f } p ( t )$ is decreasing, $p ( t ) / \gamma ( t )$ is also decreasing. Moreover, even if p4t5 is increasing, as long as the value to the users increases faster than price, $\bar { p } ( t ) / \gamma ( t )$ can still be decreasing. Essentially, the analysis can be easily extended as long as the reciprocal, i.e., $\gamma ( t ) / p ( t )$ , is increasing in time. Note that $\gamma ( t ) / p ( t )$ can be interpreted as an index for the relative valuation per dollar of the service (bang for the buck). In many cases, as technologies advance, this index tends to increase either because of cost decrease and/or because of increased features and content, in which case our model can be applied. Furthermore, our model can also accommodate cases in which the associated value 4t5 decreases over time as long as the relative valuation per dollar of the service increases over time (i.e., subscription rates decrease very fast).

## 5. Discrete Time Heuristics

To use the model introduced in §2 on real data, one would first need to convert it to a discrete-time setting. We illustrate in this section how to discretize the model and discuss various heuristic steps to estimate several parameters, derive a truncated empirical distribution, and forecast future subscription patterns.

Throughout this section we assume that , m, and adjusted price $\tilde { p } ( \cdot )$ (as defined in §4) are given. Assume there have been $t _ { O }$ time periods from the introduction of the IT service until the end of the available data, including a period t = 0 just before the release of the service. We divide the data into two sets: (i) unavailable, left-censored subscription and price data in very early periods $t \in \Omega _ { L C } = \{ 0 , 1 , \dots , t _ { L C } \}$ (time series exhibit left censoring if $t _ { L C } > 0 ) ,$ , and (ii) observed subscription and price data for periods t ∈ $\Omega _ { O } = \{ t _ { L C } + 1 , \dots , \bar { t _ { O } } \}$ . In this paper we are concerned with market rather than firm-level analysis. Some of the firms may not reveal early adoption data to other firms. In our analysis, we are careful in addressing the issue of left-censored data when we explain observed adoption and forecast future market evolution.

## 5.1. Discrete Model

Using time period as the unit, and starting with initial value $\dot { N _ { 0 } } = 0 .$ , Equations (4), (5), and (6) can be discretized for every $t > 0$ in the following way:

$$
\theta_ {t} = \max \{\underline {{\theta}}, \tilde {p} _ {t} - \nu N _ {t - 1} \},\tag{16}
$$

$$
Q _ {t} = \left\{ \begin{array}{l l} m, & \text { if } \theta_ {t} = \underline {{\theta}}, \\ m (1 - F (\theta_ {t})), & \text { if } \theta_ {t} > \underline {{\theta}}, \end{array} \right.\tag{17}
$$

$$
N _ {t} = \alpha Q _ {t} + (1 - \alpha) N _ {t - 1}, \quad \mathrm{if} t > 0,\tag{18}
$$

where the last expression captures new adopters $N _ { t } - N _ { t - 1 }$ arriving at a rate  from two pools: (i) customers who were previously qualified but did not have updated information $\left( { \mathrm { i . e . , ~ } } Q _ { t - 1 } - N _ { t - 1 } \right)$ , and (ii) customers who just became qualified in period t $( { \mathrm { i . e . , ~ } } Q _ { t } - Q _ { t - 1 } )$ . Because $N _ { t }$ is a weighted average between $Q _ { t }$ and $N _ { t - 1 } ,$ the above dynamics keep $N _ { t }$ below m without any added constraint. Also, similar to the continuous case, we define

$$
t _ {G} \triangleq \min \left\{t \mid \underline {{\theta}} + \nu N _ {t - 1} \geq \tilde {p} _ {t} \right\}\tag{19}
$$

as the earliest time when all potential consumers in the market are qualified.

## 5.2. Test For Full Qualification

For $t \in \Omega _ { O }$ we observe both $\tilde { p } _ { t }$ and $N _ { t }$ . Assuming  is known, we can test via Equation (19) whether or not $t _ { G }$ occurred prior to period t. Thus, using past subscription data we can estimate whether further price markdowns will impact future consumer subscription decisions or not. Moreover, we know that full qualification is possible only when lim $_ {  \infty } \tilde { p } ( t ) \leq \underline { { \theta } } + \nu m ,$ which can be tested as well if we have a parameterization of $\tilde { p } ( t )$ that allows us to asymptotically estimate the future evolution of price.

## 5.3. Approximation of Information Dissemination Rate Under Full Qualification

Suppose our data indicates that $t _ { G } \in \Omega _ { L C } \cup \Omega _ { O } \ ( \mathrm { i . e . }$ , full qualification occurred before period $t _ { O } )$ . For all $t \geq t _ { G } ,$ we have $Q _ { t } = m$ and $N _ { t } - \bar { N _ { t - 1 } } \stackrel { - } { = } \alpha ( m - N _ { t - 1 } )$ or

$$
\alpha = \frac {N _ {t} - N _ {t - 1}}{m - N _ {t - 1}}, \quad \forall t \geq t _ {G}.\tag{20}
$$

If $t _ { G } = t _ { O } ,$ , then we have only one hazard rate point to approximate . However, if $t _ { G } < t _ { O } ,$ then the observed hazard rate of adoption should be close to  ( plus some noise) for all $t \in \{ t _ { G } , t _ { G } + 1 , . . . t _ { O } \} \cap \Omega _ { O }$ . In that case, we can fit a line to the observed hazard rate points beyond $t _ { G }$ to better approximate information dissemination rate .

If full qualification did not occur yet, the results of Proposition $^ { 3 , }$ although in continuous time, indicate that there may be identification problems as multiple values of $\alpha ,$ each in association with a corresponding type distribution $F _ { \alpha } ,$ may lead to the same observed pre-full-qualification subscription path. In that case, for identification purposes, an exogenous estimation of  should be executed before our model can be applied. However, our model still allows for the exploration and comparison of various scenarios of information dissemination, as will be detailed in §6.2.

## 5.4. Fitting the Consumer Type Distribution

Firms are interested in finding out the shape of the consumer type distribution for various reasons. First, such information can provide important clues as to how the subscription pattern will unfold in the future, as firms would have an estimate of the number of untapped customers at each valuation level. Second, it can indicate whether future adoption will be impacted by price decreases or it will be mostly driven by information dissemination (depending on when full qualification occurs). Third, firms might be interested in the distribution of consumer types with respect to a certain IT service even ex post adoption because they may target those same customers with complementary products and services for which the customers’ willingness to pay might be correlated with the willingness to pay for the initial service.

In this subsection, we assume that we have values for $\alpha , \nu , m ,$ and $\tilde { p } ( \cdot )$

5.4.1. Discrete Approximation of Observed Empirical Distribution. To understand the density of consumers at each intrinsic valuation level, firms would ultimately want to fit a continuous distribution to the discrete data. An initial step in this process would be to choose a standard distribution with a limited number of parameters. This is particularly important when full qualification has not been achieved because customers at the low end of the distribution did not start adopting yet and a parameterization of the distribution function would allow firms to extend it to the unobserved types. In making an educated guess, firms would benefit from an initial rough discrete approximation of the distribution curve in order to gain insight into the properties of the distribution. The model and methods previously established help the firm come up with such a discrete estimate.

In this subsection, we derive estimates for the pairs $\{ \theta _ { t } ^ { e } , F _ { \alpha } ^ { e } ( \theta _ { t } ^ { e } ) \}$ along the empirical distribution (denoted by superscript $e )$ for all $t \in \Omega _ { O }$ . We approximate the marginal types $\theta _ { t } ^ { e }$ via Equation (16). We can roughly approximate $F _ { \alpha } ^ { e } ( \theta _ { t } ^ { e } )$ by attempting to solve directly the system of Equations (16), (17), and (18), which leads to the following solution:

$$
= \left\{ \begin{array}{l} 0, \quad \text { if } \theta_ {t} ^ {e} = \underline {{\theta}}, \\ \max \left\{0, 1 - \frac {N _ {t} - (1 - \alpha) N _ {t - 1}}{\alpha m} \right\}, \\ \quad \text { if } t = t _ {L C} + 1 \text { and } \theta_ {t _ {L C} + 1} ^ {e} > \underline {{\theta}}, \\ \max \left\{0, \min \left\{F _ {\alpha} ^ {e} (\theta_ {t - 1} ^ {e}), 1 - \frac {N _ {t} - (1 - \alpha) N _ {t - 1}}{\alpha m} \right\} \right\}, \\ \quad \text { if } t _ {L C} + 1 <   t \leq t _ {O} \text { and } \theta_ {t} ^ {e} > \underline {{\theta}}. \end{array} \right.\tag{21}
$$

This method attempts to perfectly fit the discrete data assuming that the information dissemination rate is exactly  in all periods. This estimation is applicable only to services exhibiting a growing installed base and a decreasing adjusted subscription rate over time, where the marginal type is decreasing and the number of qualified consumers is increasing over time. Note that in this approximation we do not impose (RC); those regularity conditions are used solely in the analytical derivations in continuous time.

When we have left censoring we will not observe the distribution for consumer types above $\theta _ { t _ { L C } + 1 } ,$ which amount to the top $1 - F _ { \alpha } ^ { \bar { e } } ( \bar { \theta } _ { t _ { L C } + 1 } )$ fraction of the market potential. Furthermore, when full qualification did not occur before $t _ { O } ,$ we do not observe the distribution for consumer types below $\theta _ { t _ { O } } .$ , which amount to the bottom $F _ { \alpha } ^ { e } ( \theta _ { t _ { O } } )$ fraction of the market potential. To extend a parameterization of the truncated distribution to the left (over low types that are not yet qualified), it is important that the subscription decision for a significant market share occurred during the window of observation such that a good fit can be obtained.

5.4.2. Continuous Parameterization of the Truncated Distribution. Note that the previous approach only provides a glimpse at a few approximated discrete points along the type distribution curve. In particular, if firms want to get a deeper and more granular understanding of the consumer density at each valuation level, then they need to fit a continuous parametric distribution to the observed data. This can be done if full qualification did not occur during the left censored period or at the very beginning on the observed window because we need several periods where the marginal type decreases. Thus, for this section in particular, we are going to consider the case when $t _ { L C } + 2 < t _ { G }$

Given the decreasing trajectory of adjusted subscription rate, types qualified during left-censored periods (prior to $t _ { L C } + 1 )$ cannot be distinguished in our sales and information dissemination model during observed or future sales. Furthermore, pricing information may not be available during left-censored periods. Considering $\widehat { \theta } _ { t _ { L C } + 1 }$ defined as in (16), our model states that the mass of customers that adopt during the left censored periods is $1 - \hat { F } _ { \alpha } \big ( \hat { \theta } _ { t _ { L C } + 1 } \big )$ , where $\hat { F } _ { \alpha } ( \hat { \theta } _ { t _ { L C } + 1 } ) = F _ { \alpha } ^ { e } ( \theta _ { t _ { I C } + 1 } ^ { e } )$ as defined in (21).

We aim to find an approximation of the distribution of types $\theta \in \lbrack \underline { { \theta } } , \theta _ { t _ { I C } + 1 } )$ that were not qualified yet at time $t _ { L C }$ . To capitalize on the observed information, one approach would be to first parameterize the conditional distribution of types $\begin{array} { r } { \theta \le \theta _ { t _ { L C } + 1 } \mathrm { : } } \end{array}$

$$
\tilde {F} _ {\alpha} (\theta) = \frac {\hat {F} _ {\alpha} (\theta)}{F _ {\alpha} ^ {e} (\theta_ {t _ {L C} + 1})} = Z (\theta \mid \xi), \quad \forall \theta \leq \theta_ {t _ {L C} + 1},\tag{22}
$$

where $\xi$ represents a set of parameters characterizing the fitted distribution. To obtain a parameterization $Z ( \cdot \mid \cdot )$ of $\tilde { F } _ { \alpha }$ (and, implicitly, $\hat { F } _ { \alpha } )$ , for low types, we can fit common distributions (Gamma, scaled Beta, truncated normal, truncated exponential, etc.) with support on $[ \underline { { \theta } } , \theta _ { t _ { L C } + 1 } ]$ . An educated decision as to which particular distribution is to be used can be made based on the approximated discrete distribution points within the observed window, as discussed in §5.4.1.

We do not restrict the distribution choice in our proposed heuristic methods and assume that the firm is capable of spotting a pattern that indicates a certain distribution type. In other words, we skip the step of choosing function $Z ( \cdot )$ because it is data driven and context dependent, and focus on the general method for estimating the distribution parameters $\hat { \xi } .$

First, for any parameter set $\xi ,$ we generate fitted values for the installed base at each time period. For any given period $t _ { L C } < t - 1 < t _ { O } .$ , where $\theta _ { t - 1 } > \underline { { \theta } } ,$ we can estimate future sales in period t through solving a one-step ahead system defined by three equations with three unknowns $\theta _ { t } , \ Q _ { t } ,$ , and $\dot { N _ { t } }$ as described in §5.1, using parameterization $\hat { F } _ { \alpha } = Z ( \cdot \mid \xi ) \times F _ { \alpha } ^ { e } ( \theta _ { t _ { L C } + 1 } )$ Note that $\theta _ { t }$ is nonincreasing in t as adoption increases and adjusted price decreases. The fitted installed base at the end of period t is given by

$$
\hat {N} _ {t} = \max \bigl \{N _ {t - 1}, \alpha \hat {Q} _ {t} + (1 - \alpha) N _ {t - 1} \bigr \}.\tag{23}
$$

We fit based on real $N _ { t - 1 } ,$ which may deviate from the perfect path illustrated in §5.1. For fitting purposes, in the extreme case where there is a big spike in adoption in the recent past, we assume that untapped qualified customers were the first to deviate toward adopting. If also some unqualified customers subscribed before period t (after all qualified customers adopted), perhaps because of a one-time promotion (e.g., back-to-school promotional plans for mobile phones), then we assume that this deviation occurs in decreasing order of unqualified types and that those customers remain in the installed base but adoption stalls until price drops sufficiently low for some other customer to join.

As a measure of fit, we consider the mean squared percentage error (MSPE) in estimating sales over the observed window. This measure compensates for the magnitude of sales during various time periods and takes into account relative rather than net errors in estimation. The parameters of the conditional distribution Z4  5 are estimated as

$$
\begin{array}{l} \hat {\xi} = \underset {\xi} {\arg \min} \frac {1}{t _ {O} - (t _ {L C} + 1)} \\ \cdot \sum_ {t = t _ {L C} + 2} ^ {t _ {O}} \left(\frac {(\hat {N} _ {t} - N _ {t - 1}) - (N _ {t} - N _ {t - 1})}{N _ {t} - N _ {t - 1}}\right) ^ {2}. \end{array}\tag{24}
$$

We remind the reader that, as per the discussion at the end of §3.2, in order to avoid other identification issues it is important for  to be exogenously derived.

## 5.5. Approximation of Future Sales

Using the parameterization of the conditional distribution derived in §5.4.2, the future subscription path can be estimated using the one-step ahead procedure in Equation (23). If full qualification did not occur before $t _ { O } ,$ one-step ahead approach requires the use of the type density at the lower end of the distribution. Although we used observed data to calibrate conditional distribution Z in Equation (24), we point out that Z is defined on $[ \underline { { \theta } } , \widehat { \theta } _ { t _ { L C } + 1 } ]$ and, thus, it can be properly used for forecasting purposes. Forecasting performance is measured via mean absolute percentage error (MAPE), mean absolute deviation (MAD), mean squared percentage error (MSPE), and mean squared error (MSE).

## 5.6. Approximation of Full Qualification Time

If the test described in §5.2 indicates full qualification already occurred before the last observed period, then we can either infer that it occurred during unobserved left-censored time periods, or pinpoint with precision the period during which it occurred among the observed time periods.

If full qualification did not occur yet and we have an exogenous estimate of information dissemination rate  and a parameterization for $\tilde { p }$ that allows us to project the future evolution of price, we test first if full qualification can ever occur (see §5.2). If it can occur, we can parameterize the distribution (as described in §5.4.2), approximate the densities of lower types unqualified at time $t _ { O } ,$ and, last, project future sales based on that parameterization (as described in §5.5). The projection of future sales over multiple future periods is achieved by repeated iterations of the one-step ahead equilibrium solution of Equation (23) where we use projected values for $N _ { t - 1 } ,$ with the only exception when $t - 1 = t _ { O } ,$ in which case we use the real value $N _ { t _ { O } }$ to seed the iterations. Then, we can obtain an approximation for the full qualification time $\hat { t } _ { G } = \operatorname* { m i n } \{ t \hat { | } \hat { t } > t _ { O } , \underline { { \theta } } > \tilde { p } _ { t } - \nu \hat { N } _ { t - 1 } \}$

## 6. Empirical Illustration

In this section, we illustrate how the discrete model and heuristic methodology introduced in §5 can be applied to real IT services data. For our empirical illustration, we utilize historical data on wireless voice services subscription in the Japanese telecommunications market. Given the very limited available data, all of it at aggregate level, full identification is not possible. Thus, the focus of this empirical illustration is not on delivering a tight analysis with precise estimates for all parameters. Rather, our discussion will be geared toward the analysis of various information dissemination scenarios that correspond to various market assumptions. In many real instances, market players have access to some microlevel data that could provide them with additional insights about which scenario is closer to reality.

We define the market size as the total number of unique potential subscribers to mobile voice services. In that sense, our model captures how market penetration changes over time and network effects describe the influence of the installed base of unique subscribers on new and existing subscribers. We assume that a user’s benefit is influenced linearly by the number of existing consumers, not the number of existing mobile voice accounts.

## 6.1. Data

We collected yearly data on the Japanese mobile voice services subscription base for fiscal years 1993–2009.<sup>4</sup> This data is publicly available from the Japanese

Telecommunications Carrier Association (2011) and Japanese Ministry of Internal Affairs and Communications (2005). The number of active voice services accounts is obtained by subtracting from the total cellular subscriptions the installed bases for data-only services operating on wireless devices that include data communication modules (e.g., automotive telematics services such as Toyota’s G-Book supported by KDDI). To implement the analysis, we generate an approximation of the unique number of subscribers in the market by adjusting downward the number of subscriptions in order to account for users with multiple accounts. The adjustment was based on industry reports and the details are included in Online Supplement C. Figure 4(a) depicts the growth of the base of unique subscribers to wireless voice plans in Japan. Mobile voice services were introduced in Japan in 1979 (Padgett et al. 1995) and at the end of

Figure 4 Japanese Wireless Voice Service Adoption and Price Over Time  
![](/api/attachments/DZ5BGA4U/fulltext/images/cd1a99617b7a9e687aac930cbbe42ce77da0da0b4402d8d8dac21d9e7afc4430.jpg)

![](/api/attachments/DZ5BGA4U/fulltext/images/26c9db83786a6f6f8886ea7a1a4e6f3b5be3ed2f4d39b1368d84da6e6bb1635f.jpg)  
Notes. Panel (a) plots the aggregate number of unique subscribers. Panel (b) plots the inflation-adjusted price measure. ARPU captures average revenue per user per month.

March 1994 (end of FY 1993) there were 2.1 million voice subscribers. In our analysis, we address the leftcensoring of data according to the approach described in §5.

In estimating the market size mˆ , we follow the derivation in Niculescu and Whang (2012), where the market potential for voice services in Japan is assumed to be comprised of the population age six and above. That approximation is based on market reports indicating that all age groups from elementary school to senior citizens exhibit increasing penetration rates for mobile voice services which, in turn, implies mobile voice services address some of the needs of these groups. We refer readers to the aforementioned article for the detailed justification of this estimation. Given that the population above age six does not fluctuate much during the period delimited by fiscal years 1994 and 2009 (117.8–121.2 million), we use the average value over this time period, $\hat { m } = 1 1 9 . 9 6$ million, as the estimate for the market potential for wireless voice services in Japan. Historical demographic data for Japan is available from Japanese Ministry of Internal Affairs and Communications (2011).

We next discuss the pricing measure. Because of the lack of detailed historical data on the variety of wireless voice plans offered over time in Japan, their corresponding pricing, and subscription base breakdown by plans, no real average price data is available. Most voice plans involve consumption quotas (free call minutes) for a basic monthly charge, followed by pricing per unit of time for all calls above the quota. As a proxy for the subscription rate, we use wireless voice services average revenue per user (ARPU).<sup>5</sup> We collected yearly ARPU data for fiscal years 1994–2009 for NTT DoCoMo, a major mobile telecommunications service provider in Japan, with a market share consistently hovering around 50%. ARPU data is publicly available on the carrier’s website. To avoid any confusion, we point out that yearly ARPU refers to revenue per month, but averaged over an entire year. ARPU computation details are included in Online Supplement D. We adjust ARPU for inflation using the fiscal year gross domestic product deflator for Japan, available from Cabinet Office of the Government of Japan (2011), and note from Figure 4(b) that it exhibits a decreasing trend in time. In the absence of complete data for the other companies, we use the data from NTT DoCoMo as the proxy for the industry price level.<sup>6</sup>

In the absence of more data, we assume for simplicity that the value of wireless voice services does not fluctuate significantly over time $( { \mathrm { i . e . , ~ } } \gamma \equiv 1 $ in the extension in §4). There are two forces that push the value of wireless voice services in opposite directions. First, over time, there is a negative impact on consumption levels for voice services in general (whether wireless or landline) due to substitution effects associated with the availability of alternative interpersonal communication channels (such as email, video chat, or social network interactions), which, in particular, are increasingly used by cell phone users who also subscribe to wireless data services. However, in Japan, as of March 2010 (end of FY 2009), data services on cell phones were predominantly offered as an addon to voice services. Thus, as wireless data services grew more popular and the gamut of applications and services on mobile Internet literally exploded in the recent years, the value of wireless voice services was positively influenced given that their adoption (albeit associated with perhaps decreased consumption) was mandatory for the adoption of the add-on. In that sense, the instantaneous utility rate defined in (1) may be envisioned as capturing also the implicit benefit of wireless voice services in allowing users to adopt wireless data services as well.

## 6.2. Analysis

In this section we apply the discrete time heuristic method introduced in §5 to the data described in §6.1 in order to characterize consumer heterogeneity, forecast future sales, and derive further insights about the adoption of wireless voice services in the Japanese market. In this specific context, we can think of the intrinsic valuation  as capturing the customer need or preference to communicate via a mobile phone. For example, certain professions (e.g., consulting) might involve a lot of traveling. In such circumstances, people value the ability to be reachable or reach others while being mobile. Other consumers (e.g., elderly)

Figure 5 Empirical Hazard Rate  
![](/api/attachments/DZ5BGA4U/fulltext/images/46dfc0a42529556733d80aa29c5e2ba42ce1ce533eff22a2b59dc159e09b8c2b.jpg)

might carry a cell phone just in case of emergencies or for the rest of the family to be able to reach them more conveniently. Network effects capture the premium value a consumer gets from communicating with other mobile phone users (perhaps within the same network) as well as the other benefits associated with expanding networks (e.g., carriers invest more in the infrastructure and handset manufacturers push more models to the market if there are more users). For simplicity, we assume that $\underline { { \theta } } = 0 , \mathrm { i . e . }$ , for some consumers the only benefit from subscribing to a voice plan comes from the ability to communicate with the rest of the subscribers.

First, we test whether full qualification has occurred yet. As discussed in §5.2, beyond the point of full qualification we would expect the hazard rate of adoption to stabilize around the information dissemination rate. From Figure 5, the empirical hazard rate seems to follow an increasing trend over time and it is unlikely that all consumers have been qualified by the end of 2006 (after 2006 hazard rate moves to a different level). It follows that $p _ { 2 0 0 6 } \geq \underline { { \theta } } +$ $\nu N _ { 2 0 0 6 }$ and $t _ { G } \geq 2 0 0 6$ . Moreover, because we focus on full adoption services $( \dim _ { t \to \infty } G ( t ) = 1 )$ , we assume that $\begin{array} { r } { p ( \infty ) \leq \underline { { \theta } } + \nu m , } \end{array}$ where p45 is approximated by fitting a negative exponential parameterization $\begin{array} { r } { p ( t ) = a e ^ { - \eta ( t - t _ { L C } - 1 ) } + b } \end{array}$ on the observed price data $( t _ { L C } =$ 1993,<sup>7</sup> $p ( \infty ) = \hat { b } )$ . Given the actual data, this range translates into $\nu \in [ 3 . 8 9 \times 1 0 ^ { - 6 } , 6 . 7 4 \times 1 0 ^ { - 6 } ]$ . For illustration purposes, we consider  in the middle of the feasible range, i.e., $\hat { \nu } = 5 . 3 1 5 \times 1 0 ^ { - 6 }$

We further divide the data set into two separate sets: (i) a training set that includes data for fiscal years 1994 to 2006, and (ii) a test set that includes the data for fiscal years 2007 to 2009. We first fit our model using the training set to estimate the distribution of the consumer heterogeneity. Using the estimated heterogeneity distribution, we then provide the one-step ahead sales forecast for the test set. Given that by 2006 full qualification is not likely to have occurred, because of the identification issues mentioned at the end of §3.2 and in §5.4.2 we do not apply our methods directly to estimate . Instead, for illustration purposes, we explore different information dissemination scenarios $\left( \alpha = 0 . 1 , 0 . 1 5 , 0 . 2 , 0 . 3 , \right.$ and 005) and study the sensitivity of our estimates and forecasts with respect to the values of .

Table 1 Estimation Results and One-Step Ahead Forecasting Errors

<table><tr><td rowspan="2"></td><td>Estimated distribution</td><td colspan="2">Training set</td><td colspan="4">Test set</td></tr><tr><td>Scaled beta ( $\xi_1, \xi_2$ )</td><td>MSPE %</td><td> $R^2$ %</td><td>MAPE %</td><td>MAD ( $\times 10^5$ )</td><td>MSE ( $\times 10^{11}$ )</td><td>MSPE %</td></tr><tr><td> $\alpha = 0.10$ </td><td>(10.0, 3.00)</td><td>1.48</td><td>89.09</td><td>30.14</td><td>11.22</td><td>13.29</td><td>9.13</td></tr><tr><td> $\alpha = 0.15$ </td><td>(0.90, 0.59)</td><td>2.59</td><td>81.30</td><td>7.61</td><td>2.83</td><td>0.85</td><td>0.59</td></tr><tr><td> $\alpha = 0.20$ </td><td>(0.66, 0.62)</td><td>2.61</td><td>82.35</td><td>29.04</td><td>9.61</td><td>13.32</td><td>12.25</td></tr><tr><td> $\alpha = 0.30$ </td><td>(0.58, 0.77)</td><td>2.77</td><td>84.12</td><td>83.57</td><td>28.36</td><td>98.03</td><td>88.70</td></tr><tr><td> $\alpha = 0.50$ </td><td>(0.57, 0.98)</td><td>4.79</td><td>75.53</td><td>194.19</td><td>66.57</td><td>510.96</td><td>456.32</td></tr></table>

For each , using the training set, we first examine the rough pointwise approximation for the observed portion of the consumer type distribution as illustrated in §5.4.1 (we omit this step for brevity). To forecast future sales we need to fit a parameterization to the observed data such that we can approximate the distribution of consumer types at the low end of the intrinsic valuation distribution. As discussed in detail in §5.4.2, we remind the readers that we parameterize $\hat { F _ { \alpha } ( \cdot ) } = \hat { F _ { \alpha } } ( \hat { \theta } _ { 1 9 9 4 } ) \times Z ( \cdot \mid \xi )$ over the interval $[ 0 , \hat { \theta } _ { 1 9 9 4 } ] ,$ where $\ddot { \theta } _ { 1 9 9 4 }$ and $\hat { F } _ { \alpha } (  { \hat { \theta } } _ { 1 9 9 4 } )$ are estimated as in (16) and (21). We parameterize conditional distribution $Z ( \theta \mid \xi )$ as scaled Beta4 $\xi _ { 1 } , \xi _ { 2 } )$ because of the ability of such a distribution class to capture multiple skewness scenarios. The corresponding parameter estimates and fit measure are given in Table 1. Figure 6(a) presents the estimated continuous parameterization $\hat { \hat { F } } _ { \alpha }$ of the consumer type distribution function over the interval $[ 0 , \widehat { \theta } _ { 1 9 9 4 } ]$ . This plot does not capture the estimation for the left-censored portion of the data, and thus, the cumulative distribution function lines do not go up to one but to $\hat { F } _ { \alpha } ( \hat { \theta } _ { 1 9 9 4 } )$ . Given that all five scenarios involve the approximation of the same observed adoption path, we confirm an expected skewness toward higher types when information disseminates slowly in the market. Among the different considered  values, $\alpha = 0 . 1$ and $\alpha = 0 . 1 5$ fit the training set best based on the MSPE error metric. Note that $R ^ { 2 }$ corresponds to MSE and thus we see a discrepancy between MSPE and MSE. As discussed in $\ S 5 . { \bar { 4 } } ,$ we favor MSPE because it compensates for large isolated errors.

Based on the estimated distribution of the consumer intrinsic valuation, we can perform the one-step ahead forecasting procedure for the sales during the time window of the test set, following the methodology presented in §5.5. The forecasted and the realized sales are plotted in the right-hand part of Figure 6(b), and multiple error measures capturing the forecasting performance are presented in Table 1. As it can be seen, the information dissemination factor plays a significant role in forecasting sales. In particular, if the corresponding  values are too big (i.e.,  = $0 . 2 , 0 . 3 , 0 . 5 )$ or too small $( \alpha = 0 . 1 )$ , the forecasted values become rather inaccurate in the test set, which demonstrates the managerial importance of having a thorough understanding of how fast customers refresh information in the market. If  values are relatively small but not too small $( \mathrm { i . e . , } \alpha = 0 . 1 5 )$ , one-step ahead forecast values are reasonably accurate as shown in Table 1.

As information dissemination rate increases, for the same observed adoption path during the training window more new consumers are expected to subscribe during the test window. This happens because a higher  corresponds to a lower delay rate that allows for the observed adoption path to be generated by less mass of high type subscribers. This, in turn, leads to the expectation that more consumer mass is concentrated around low types. Thus, during the test window, for higher values of  the model would predict a higher inflow of newly qualified customers as opposed to previously qualified customers who operated under outdated information until recently catching up with current market conditions. Note that, among considered values, $\alpha = 0 . 1 5$ fits relatively well the training set and performs best in one-step ahead forecasting in the test $\mathrm { s e t . } ^ { 8 }$ One may consider that the annual information dissemination factor of 0015 seems small in the mobile telecommunications industry. We point out that in our model  can more or less be considered an industry average over all potential customers who have not adopted yet and over time. Once a customer subscribes, our model and results are not impacted by a potential shift in

Figure 6 (a) Approximation of Type Distribution $\hat { F } _ { \alpha }$ , Using Scaled Beta Parameterization for Conditional Distribution $Z ( \cdot \mid \cdot )$ , as Discussed in §5.4.2. (b) Corresponding Fitted Values and One-Step Ahead Forecasting of New Subscriptions

(b) Fitted and one-step ahead forecasting  
![](/api/attachments/DZ5BGA4U/fulltext/images/050657d8fcee187adc2ad003171bbd88939795e70f2346344738647600b3e29d.jpg)

![](/api/attachments/DZ5BGA4U/fulltext/images/4d8996651cd94dd8f530836d2660ffce0df84d488ffca6b86313845304c7eb9f.jpg)  
Notes. The value of  is $5 . 3 1 5 \times 1 0 ^ { - 6 }$

her information refresh rate post-adoption. Because we have adjusted the installed base to reflect unique subscribers, in our model new adopters never had a mobile voice account before. Technology-savvy consumers move first toward adopting. This group contains young professionals as well as high-school and university students. Users that are not very involved with technology and less mobile (for example, senior citizens) will likely refresh less often their information about available wireless offers and associated benefits. Consumers over age 50 constitute almost 40% of the market potential. Such users might also be more conservative regarding technology adoption. According to Web Japan (2005), at the end of 2004, approximately 80% of people in their twenties and thirties subscribed to wireless voice services, and adoption at the senior end of the age spectrum was considerably slower (adoption rates for 65–69, 70–79, and 80+ age groups stood at 26.4%, 11.4%, and 4.7%, respectively). As time passes and penetration rate grows, the bulk of new subscribers will increasingly come from the second consumer pool. Moreover, a low  indicates that a considerable portion of this less tech-savvy consumer pool would actually qualify quite early, and could have started deriving positive benefits earlier had it not been for the holding back due, among other things, to outdated information.

Lastly, for a given marginal network effect (such as the one chosen in the feasible region for illustration purposes), one can continue to explore at future times if full qualification has occurred, as discussed in §5.2. Once full qualification has been achieved, future subscriptions are driven primarily by information dissemination.

We end this section by emphasizing that our empirical exercise is meant as an illustration of how to apply our discrete-time model to real data, and the results should be taken with a grain of salt. Additional data is necessary in order to precisely estimate  and $\nu ,$ as discussed in §§3.2 and 5. For exposition, we picked  in the middle of a reasonably chosen feasible region. Higher (lower) marginal network effects will bring the market to full qualification faster (slower), with an obvious impact on the forecasting of future sales.

## 7. Concluding Remarks

This paper represents one of the first continuoustime analytical studies to explore at a broad level the underlying consumer heterogeneity in competitive markets for subscription-based IT services that exhibit network effects. Understanding consumer heterogeneity is important for the forecasting of the subscriber base growth as well as the sales of complementary products or services. We study when and how very general adoption paths can be explained by an individual consumer utility model in association with various rates of information dissemination and corresponding well-behaved consumer type distributions. When such distribution functions exist, we fully characterize them. We provide various managerial insights stemming from the way awareness dissemination rate, distribution skewness, and price jointly impact adoption. In particular, for forecasting purposes, it is very important for firms to have a deep understanding of how information spreads in the market as adoption curves generated under different heterogeneity and information refresh rate scenarios may share a common path in the past but may diverge in the future, before full qualification is reached. If full qualification has been reached, new subscriptions will be predominantly driven by information dissemination in the future and will exhibit a stable hazard rate of adoption, which makes possible the estimation of information dissemination in the market directly from our model.

Our analytical theory takes a less conventional approach, starting from general aggregate adoption and trying to explain at a microlevel what consumer heterogeneity pattern generated it. The vast majority of analytical microeconomic theory starts in the opposite direction, building from the individual level behavior based on a given consumer heterogeneity. In the latter case, the implied adoption paths are constrained by the consumer heterogeneity assumptions. However, in practice, managers look at sales trends and attempt to estimate future adoption based on the observed history at an aggregate level. Thus our research complements existing analytical modeling literature by attempting to explain from a consumer behavior perspective a vast spectrum of adoption scenarios. From an empirical perspective, it also provides a starting point in making an educated guess about the properties of consumer heterogeneity before any strong assumptions are made for forecasting purposes. Moreover, as discussed in §3.2, we show also that our model can explain adoption behavior that may not be captured properly by several extant aggregate models, in particular in later adoption stages. This is consistent with Lucas (1976) in the sense that the use of aggregate models poses forecasting risks given that some parameters may not be structural and changes to a single parameter may overlook underlying consumer behavior dynamics.

Although the major research goal of this paper is to enhance the analytical explanatory theory behind adoption of IT services under network effects, for practical purposes we also present a set of heuristic methods that illustrate how our continuous-time framework and analytic results can be discretised and applied to real industry data in the estimation of consumer heterogeneity and the forecasting of future sales. As an empirical illustration, we apply these heuristic methods to the Japanese mobile voice services market and explore the implied heterogeneity and forecast the growth of the subscriber base. As argued in §6.2, according to our modeling framework, it may be unlikely that full qualification occurred in the Japanese market as of 2006 (the last period in our training set). In this case, given the lack of additional data and the possibility of identification issues as discussed at the end of §3.2, we do not estimate  endogenously and limit our illustration to a rich analysis of various information dissemination scenarios. However, we comment that a low information dissemination rate seems to fit the data best.

Our work is by no means an exhaustive analysis of underlying consumer heterogeneity in adoption processes for IT subscription-based services, but rather a foray into the topic, with its own limitations. Thus, there are several directions for future research based on our approach. On the analytical side, one extension would be to consider service differentiation in the market and explore implied consumer heterogeneity going deeper into competition dynamics between firms and consumer retention strategies. Other extensions could open up more dimensions of consumer heterogeneity, exploring how information dissemination or network effects are correlated with customer type. In particular, one can study other utility models including nonlinear forms (e.g., multiplicative network effects). It would also be interesting to consider a time-varying information dissemination rate, capturing market fluctuations in promotions and advertising. An additional extension could consider combining adoption and consumption volume. On the empirical side, with richer data sets, one could envision a more complex analysis where  can also be estimated simultaneously with the consumer heterogeneity in the market even before full qualification has occurred.

## Electronic Companion

An electronic companion to this paper is available as part of the online version at http://dx.doi.org/10.1287/ isre.1120.0422.

## Acknowledgments

The authors thank the senior editor, associate editor, and the three anonymous reviewers for their constructive feedback on this manuscript. The authors also extend their gratitude to Maxim Afanasyev, Warren Hausman, Ozge Islegen, David Lowsky, Harikesh Nair, Noam Shamir, Andrzej Skrzypacz, V. “Seenu” Srinivasan, Bumin Yenmez, Lawrence Wein, and the participants at INFORMS 2010 for their useful comments.

## References

Ahonen TT (2010) The insider’s guide to mobile. The customers, services, apps, phones, and business of the newest trillion dollar industry. Tomi Ahonen Consulting. Accessed April 2012, http://www.lulu.com/shop/tomi-t-ahonen/insiders-guide-to -mobile-free-edition/ebook/product-14591083.html.

Ahonen TT (2011) Tomi Ahonen Almanac 2011. The mobile telecoms industry annual review for 2011. Tomi Ahonen Consulting.

Accessed November 2011, http://www.tomiahonen.com/ ebook/almanac.html.

Argenziano R (2008) Differentiated networks: Equilibrium and efficiency. RAND J. Econom. 39(3):747–769.

AT&T (2008) AT&T announces new approach to early ternimantion fees: More flexibility for wireless customers. Press Release, March 31. Accessed April 2012, http://www.att.com/ gen/press-room?pid=4800&cdvn=news&newsarticleid=25390.

Browne J, Temkin BD, Geller S (2009) How Japanese consumers use the mobile internet. Forrester Res. Report, March 10.

Cabinet Office of the Government of Japan (2011) Statistics. Economic and Social Research Institute. Accessed May 5, 2011, http://www.esri.cao.go.jp/index-e.html.

Chatterjee R, Eliashberg J (1990) The innovation diffusion process in a heterogeneous population: A micromodeling approach. Management Sci. 36(9):1057–1079.

Cheng R (2010) Verizon to offer FiOS without contract. The Wall Street Journal (June 22). Accessed April 2012, http:// online.wsj.com/article/SB10001424052748704895204575320700 -280294646.html.

Cheng HK, Liu Y (2010) Optimal software free trial strategy: The impact of network externalities and consumer uncertainty. Inform. Systems Res. Forthcoming.

Cheng HK, Tang QC (2010) Free trial or no free trial: Optimal software product design with network effects. Eur. J. Oper. Res. 205(2):437–447.

Cisco (2011) Visual networking index (VNI) forecast (2010–2015). Accessed June 1, 2011, http://www.cisco.com.

Conner KR (1995) Obtaining strategic advantage from being imitated: When can encouraging clones pay? Management Sci. 41(2):209–225.

Dewan S, Ganley D, Kraemer KL (2010) Complementarities in the diffusion of personal computers and the Internet: Implications for the global digital divide. Inform. Systems Res. 21(4):925–940.

Dhebar A, Oren SS (1986) Dynamic nonlinear pricing in networks with interdependent demand. Oper. Res. 34(3):384–394.

Dodson JA, Muller E (1978) Models of new product diffusion through advertising and word-of-mouth. Management Sci. 24(15):1568–1578.

Doganoglu T, Grzybowski L (2007) Estimating network effects in mobile telephony in Germany. Inform. Econom. Policy 19(1):65–79.

Gartner (2011) Gartner Says Worldwide Software as a Service Revenue Is Forecast to Grow 21 Percent in 2011 Press release, July 7. Accessed April 2012, http://www.gartner.com/it/page .jsp?id=1739214.

Guevara AL, Elberse A, Putis WP (2007) Diffusion of complementary products with network effects: A model with applications. Working paper, accessed April 24, 2007, http://www.people .hbs.edu/aelberse/papers/ladron\_2007.pdf.

Haruvy E, Mahajan V, Prasad A (2004) The effect of piracy on the market penetration of subscription software. J. Bus. 77(S2): S81–S107.

Horsky D (1990) A diffusion model incorporating product benefits, price, income and information. Marketing Sci. 9(4):342–365.

Internet World Stats (2011) Miniwatts Marketing Group, Accessed November 21, 2011, http://www.internetworldstats .com/stats.htm.

Jang SL, Dai SC, Sung S (2005) The pattern and externality effect of diffusion of mobile telecommunications: The case of the OECD and Taiwan. Inform. Econ. Policy 17(2):133–148.

Japanese Ministry of Internal Affairs and Communications (2005) Information on subscribers of cellular telephone, pager and PHS (personal handy-phone system) in Japan. Accessed May 2, 2011, http://www.soumu.go.jp/joho\_tsusin/eng/ Statistics/telephone.html.

Japanese Ministry of Internal Affairs and Communications (2011) Statistics Bureau, Director-General for Policy Planning (Statistical Standards) and Statistical Research and Training Institute. Accessed June 1, 2011, http://www.stat.go.jp/english/ index.htm.

Japanese Telecommunications Carrier Association (2011) Voice installed bases. Accessed November 24, 2011, http://www.tca .or.jp/eng/database/daisu/index.html.

Kalish S (1983) Monopolist pricing with dynamic demand and production cost. Marketing Sci. 2(2):135–159.

Kalish S (1985) A new product adoption model with price, advertising, and uncertainty. Management Sci. 31(12):1569–1585.

Katz ML, Shapiro C (1985) Network externalities, competition, and compatibility. Amer. Econom. Rev. 75(3):424–440.

Lucas R (1976) Econometric policy evaluation: A critique. Carnegie-Rochester Conf. Ser. Public Policy 1:19–46.

Madden G, Coble-Neal G (2004) Economic determinants of global mobile telephony growth. Inform. Econom. Policy 16(4):519–534.

Mahajan V, Muller E, Wind Y, eds. (2000) New-product diffusion models. International Series in Quantitative Marketing, Vol. 11 (Kluwer Academic Publishers, Norwell, MA).

Mankiw NG, Reis R (2002) Sticky information versus sticky prices: A proposal to replace the new Keynesian Phillips curve. Quart. J. Econom. 117(4):1295–1328.

Meade N, Islam T (2006) Modelling and forecasting the diffusion of innovation—A 25-year review. Internat. J. Forecasting 22(3):519–545.

Mitchell MF, Skrzypacz A (2005) Network externalities and longrun market shares. Econom. Theory 29(3):621–628.

Morris S, Shin HS (2006) Inertia of forward-looking expectations. Amer. Econom. Rev. 96(2):152–157.

Nair H (2007) Intertemporal price discrimination with forwardlooking consumers: Application to the US market for console video-games. Quant. Mktg. Econom. 5(3):239–292.

Niculescu MF, Whang S (2012) Codiffusion of wireless voice and data services: An empirical analysis of the Japanese mobile telecommunications market. Inform. Sys. Res. 23(1):260–279.

Padgett JE, Günther CG, Hattori T (1995) Overview of wireless personal communications. IEEE Comm. Magazine 33(1):28–41.

Robinson B, Lakhani C (1975) Dynamic price models for newproduct planning. Management Sci. 21(10):1113–1122.

Saloner G, Shepard A (1995) Adoption of technologies with network effects: An empirical examination of the adoption of automated teller machines. RAND J. Econom. 26(3):479–501.

Satariano A (2011) Big Fish sells subscriptions to its games on the iPad. Bloomberg. Accessed November 23, 2011, http://www .bloomberg.com.

Seo S (2006) Network effects in the U.S. cable television industry: An empirical examination of cable network externalities. Paper presented at the Annual Meeting of the International Communication Association, Dresden, Germany (June 19–23).

Sethi SP, Bass FM (2003) Optimal pricing in a hazard rate model of demand. Optimal Control Appl. Methods 24(4):183–196.

Sing TF, Lee KP, Wong AL (2002) Network effects and broadband connectivity in office building. Intl. Real Estate Rev. 5(1): 146–168.

Song I, Chintagunta P (2003) A micromodel of new product adoption with heterogeneous and forward-looking consumers: Application to the digital camera category. Quant. Mktg. Econom. 1(4):371–407.

The Mobile World (2011) The week in figures. Accessed April 2012, http://www.themobileworld.com.

Verizon Wireless (2008) No contract required—New month-tomonth agreement gives Verizon Wireless customers even more freedom. Press Release, September 22. Accessed April 2012, http://news.verizonwireless.com/news/2008/09/pr2008-09-22b .html.

Web Japan (2005) Back to basics: No-frills cell phones attract older users. Trends in Japan. Science and Technology. Accessed June 1, 2011, http://web-japan.org/trends/science/ sci050114.html.

Zhang J, Seidmann A (2009) Perpetual vs. subscription licensing of software with network externalities. 42nd Hawaii Internat. Conf. on System Sci., Waikoloa, Big Island, Hawaii (January 5–8). http://www.computer.org/portal/web/csdl/doi/10.1109/ HICSS.2009.859.

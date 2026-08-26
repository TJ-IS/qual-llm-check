---
otero_id: 542
otero_key: "QDA3BUZ9"
title: "How Mega Is the Mega? Exploring the Spillover Effects of WeChat Using Graphical Model"
authors: "Jinyang Zheng; Zhengling Qi; Yifan Dou; Yong Tan"
year: "2019"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0865"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

![](/api/attachments/QDA3BUZ9/fulltext/images/0ab997ed5c4c134746d6a693168c15196afa1bad7e993df16935770f09403198.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# How Mega Is the Mega? Exploring the Spillover Effects of WeChat Using Graphical Model

Jinyang Zheng, Zhengling Qi, Yifan Dou, Yong Tan

To cite this article: Jinyang Zheng, Zhengling Qi, Yifan Dou, Yong Tan (2019) How Mega Is the Mega? Exploring the Spillover Effects of WeChat Using Graphical Model. Information Systems Research

Published online in Articles in Advance 06 Dec 2019

https://doi.org/10.1287/isre.2019.0865

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2019, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# How Mega Is the Mega? Exploring the Spillover Effects of WeChat Using Graphical Model

Jinyang Zheng,<sup>a</sup> Zhengling Qi,<sup>b</sup> Yifan Dou,<sup>c</sup> Yong Tan<sup>d</sup>

<sup>a</sup> Krannert School of Management, Purdue University, West Lafayette, Indiana 47906; <sup>b</sup> School of Business, George Washington University, Washington, District of Columbia 20052; <sup>c</sup> School of Management, Fudan University, 200433 Shanghai, China; <sup>d</sup> Michael G. Foster School o Business, University of Washington, Seattle, Washington 98195

Contact: zhengjy@purdue.edu, http://orcid.org/0000-0001-5028-4193 (JZ); qizl1027@live.unc.edu (ZQ); yfdou@fudan.edu.cn, http://orcid.org/0000-0002-0516-3250 (YD); ytan@uw.edu, http://orcid.org/0000-0001-8087-3423 (YT)

Received: January 15, 2017 Revised: March 2, 2018; February 19, 2019 Accepted: April 22, 2019 Published Online in Articles in Advance: December 6, 2019

https://doi.org/10.1287/isre.2019.086

Copyright: © 2019 INFORMS

Abstract. WeChat, an instant messaging app, is considered a mega app because of its dominance in terms of use among Chinese smartphone users. Little is known, however, about its externality in the broader app market. This work estimates the spillover effects of WeChat on the other top 50 most frequently used apps in China, using users’ weekly app usage data. Given the challenge of determining causal inference from observational data we apply a graphical model and an econometric method to estimate the spillover effects in two steps: (1) we determine the causal structure by estimating a partially ancestral diagram, using a fast causal inference algorithm; and (2) given the causal structure, we find a valid adjustment set and estimate the causal effects by an econometric model with the adjustment set for controlling noncausal effects. Our findings show that the spillover effects of WeChat are limited; in fact, only two other apps, Tencent News and Taobao, receive positive spillover effects from WeChat. In addition, we show that if researchers fail to account for the causal structure that is determined from the graphical model, it is easy to fall into the trap of confounding bias and selection bias when estimating causal effects. The findings generate managerial implications in terms of app usage patterns, strategic management of mega apps on an app platform, and app promotional strategies for app platform managers and app developers.

History: Xiaoquan (Michael) Zhang, Senior Editor; Xue Bai, Associate Editor. Funding: Y. Tan acknowledges financial support from the National Natural Science Foundation of China (NSFC) [Grants 71729001, 71490723, and 71831005]. Y. Dou acknowledges financial support from the NSFC [Grants 71772017, 71822201, and 71531006]. Supplemental Material: The online supplement is available at https://doi.org/10.1287/isre.2019.0865.

Keywords: causal inference • graphical model • app analytics • WeChat • spillover effects • machine learning • econometrics

## 1. Introduction

WeChat, developed by Tencent Inc., is one of the world’s largest stand-alone mobile apps, with over 1 billion monthly active users, half of whom open the app more than 10 times a day.<sup>1</sup> WeChat is known as China’s “mega app” because of its wide range of platforms and functions, including more than 12 general categories of features, such as messaging, social feeds, mobile payment, mini programs, official accounts, city services, newsfeed and search, friends seek, and Voice over Internet Protocol (VOIP) service (Wikipedia 2019). Its design is consistent with similar apps in other countries (e.g., Facebook Messenger, Snapchat, Kakao Talk, Line). The main user interface is for messaging, and the second interface is for a contacts book. The third interface, known as “discover,” provides extended features, including social feeds under “moments,” social games, news feeds, and search based on social network indexing, friends seek, VOIP service, and other mini-programs.

The last interface, termed “me,” is for profile management and setting, and it has mobile payment-related features, including financial management, city services, charity, and third-party mini-programs, such as travel booking, movie booking, ride hailing, online shopping, and food delivery.

WeChat is designed to seek clicks. In addition to its large-scale engagement in social networks and the premium from “bigger gets bigger” effects (Garg and Telang 2013), WeChat proactively attempts to increase the engagement of users through app integration (Sijia 2017). It embeds the major functionality of partners (e.g., taxi hailing by Didi, e-commerce by JD.com) on the WeChat app, and one can open the mini-program platform on “discover” to any business owner or app developer through JavaScript plus a proprietary API. Similar to WeChat in Chinese user-based app markets, other mega apps have transformed themselves into an application platform. Industrial analysts have noted the aggressive integration and radical repositioning as a mini-platform of Kakao Talk and Line, the mega apps in South Korea and Southeast Asia, respectively (Danova 2014, Alive Studios 2017). Messenger by Facebook extends a “discovery” interface for mini-programs by third-party app developers. These apps’ very strong social network, along with their ease of use and wide range of functionalities, secures their mega roles in the smartphone ecosystem.

The increasing number of clicks of a mega app may make a significant impact on the other apps and thus the structure of the app platform ecosystem. The impact is multifold but not obvious to many stakeholders in the app platform ecosystem and is important to them. On the one hand, given the constraints of the total usage/time of smartphone users, apps such as WeChat can crowd out the use of other apps if their integration could substitute for these other apps. Their efforts in integration could eat into the iOS and Android app ecosystems by monopolizing user traffic, as the two U.S. tech giants rely on their own universe of apps to enrich the use of their respective iOS and Android systems (Ye 2018). A recent settlement between WeChat and Apple reveals the tension between WeChat and the iOS system (Kubota and Abkowitz 2018). On the other hand, the literature suggests that heavy usage of social media apps might generate positive spillover effects onto other apps (Li and Agarwal 2016) and thus might benefit the ecosystem by increasing overall usage in the universe of apps. In addition, it is possible that mega apps will not affect the use of other apps if the major functionality of mega apps is closed; that is, the use of a mega app might be independent from that of other apps. To determine the impact of mega apps, app developers and platform owners must carefully evaluate the usage externality of mega apps.

The usage externality of mega apps is particularly important for the developers of mega apps and apps in or potentially in partnership with mega apps. By bringing more clicks to the mega app, collaboration with mega apps also potentially creates promotional opportunities for other apps by diverting traffic from the mega app to increase their clicks. It is critical for both mega apps and their partners to understand quantitatively the value and effectiveness of collaboration attempts to support the decision making of app integration, how to collaborate, and, more important, revenue sharing if a collaboration is established. Value and effectiveness, however, cannot be measured solely by the usage correlations, as a more important aspect of the value attribution concerns the value of transferring—that is, who receives or gives the usage traffic to the other. An estimate of spillover from the mega app, including both direction and scale, is thus an appropriate and necessary quantity to measure the value attribution.

Despite the importance of empirical research on the externality of mega apps, such research is limited. Past literature has instead examined the effects of a focal app’s internal characteristics or attributes on its usage. For example, Kwon et al. (2016) explain Facebook’s heavy usage through the rational addiction perspective. Ghose and Han (2014) estimate the cross-elasticity of app demand, given the measurable characteristics and assuming the functionality (charac teristics) substitution. Carare (2012) finds that users willingness to pay for top-ranked apps is an additional \$4.50 compared with that of the same unranked app. In such research, the externality is estimated based on the observed app attributes (e.g., app rank, in-app purchase, and in-app advertisement), but the unobserved uniqueness of apps is ignored. Another concern is that app usage is measured by app installation, which might differ from the extent of usage postinstallation. Although there is another stream of literature in the computer science field that concerns the prediction of postinstallation usage patterns (Falak et al. 2010, Tongaonkar et al. 2013, Xu et al. 2013), it focuses only on the association rules of app usage patterns and does not provide a causal interpretation. Li and Agarwal (2016) estimate the spillover effects of Facebook’s integration with Instagram econometrically but measure only the externality of the integration intervention rather than that of an app.

We address this research gap by estimating the spillover effects of WeChat usage on the top 50 most used apps, using observational data. This research objective is methodologically challenging for the causality identification reason. Researchers who fail to account for confounders and the direction of causality might incorrectly take associations as causal effects, which leads to endogeneity. The constraints of observational data make this challenge extremely difficult to address in the traditional econometrics framework because researchers are challenged to develop a valid identification strategy when lacking prior information of causality, such as our context. Taking the instrumental variable approach as an example, there are two main requirements for a valid instrumental variable: (1) a strong correlation with the endogenous variable and (2) a lack of correlation to the error term. In our context, even though many apps’ usage is correlated with that of WeChat, identifying any that are not correlated with the usage of the app that receive spillover is challenging when not enough prior information backs the “uncorrelated” condition. A wrong instrumental variable may lead to inconsistent estimates of the causal effect.

We borrow a machine-learning method and integrate it with econometrics to identify the spillover effects of WeChat. Specifically, we apply fast causal inference (FCI) and really fast causal inference (RFCI)

algorithms to learn a partial ancestral graph (PAG) uniquely from observational data. Given the learned PAG, we identify the adjustment set by generalized back-door criterion (GBC) and generalized adjustment criterion (GAC). With the adjustment set and the multivariate normality assumption, we estimate the mean causal effects quantitatively with a simple econometric linear model.

Different from the graphical model that focuses on deriving and testing identification strategy, given known information and the law of causality, the model we apply does not necessarily require known causality. It takes observational data as input, partially discovers and learns causality from the data, and enables us to construct a diagram to represent the learned causality between those variables as output. The learned causality could fill in the gap of unknown laws and, thus, it supports the identification and inference of the causal effects. It also extends the past literature on estimating the externality of apps by not using product attributes and by relaxing the attributes substitution assumption.

Our results show that, surprisingly, WeChat has very limited spillover effects on other apps. Only two apps among the top 50 apps, Taobao and Tencent News, receive positive spillover effects. Considering the functionality and developer identity of these two apps, our results indicate the complementary effects between news apps and social media and those between e-commerce and social media. Considering other apps, our results suggest the overall closure of WeChat’s spillovers. For other messaging apps (e.g., QQ, Momo, Weibo), WeChat does not crowd out their use. For the apps under the same umbrella brand or in partnership (e.g., Didi, JD.com), the reward in diverted users’ traffic is, however, limited. For the platform owner, our results alleviate concerns about the threat by WeChat, as its overall spillover effects on the top 50 apps are limited but positive. This indicates that WeChat’s success is not in exchange for squeezing out the use of other major apps. WeChat might contribute to the platform by transforming users’ nonmobile activities to the mobile setting and by exhibiting some positive spillovers. In addition, our results emphasize the advantages of using a PAG to estimate causal effects such as, for example, uncovering latent confounders (identifying L in X ← L → Y by observing X ↔ Y), avoiding reversed causality (differentiating X → Y from X ← Y), and avoiding selection bias (identifying the collider in $X \right. Y \left. Z )$ . We demonstrate these advantages by showing the discrepancy between causal effects encoded in the graph and those estimated with an incorrect interpretation of the causal structure or when the causal structure is unknown.

Our research complements the past studies on app use patterns in four dimensions. First, whereas past works are based on the spillover effects of observed app attributes or policy intervention, we directly investigate the interapp causal relationship, which surpasses the past studies by implicitly incorporating the unobserved heterogeneity. Second, given that the major revenue source has switched to postpurchase usage from the purchasing stage (download), our unique data set enables us to contribute to the literature by investigating the postpurchase app usage patterns. Third, to the best of our knowledge, we are the first study that empirically addresses the lack of understanding of the positive versus negative role of a mega social media app on the app platform. Finally, our findings contribute to the research stream of app promotional strategy through our study of the effectiveness of using partnership and/or integration with a mega app to promote focal app usage.

Our work also makes several practical contributions. The estimates of spillover effects could help the developers of a mega app to determine app usage attribution, which further facilitates strategic decision making about product design, revenue sharing, and app integration. The estimates also help the decision making of the other app developers, platform owners, and policy makers in regard to their relationship with a mega app by informing them of vulnerabilities. In addition, other app developers can determine their dependence on a mega app based on the spillover estimate and the make decisions about their partnerships with WeChat. Furthermore, our method provides a flexible tool that could be adjusted easily in regard to any focal app to investigate their spillovers and to help different stakeholders understand the causal usage relationship between different apps.

To the best of our knowledge, this is the first business analytics research that integrates the most recent machine-learning causal inference methods with econometrics to estimate spillover effects. Our research shows the strength of these methods in identifying causal relationships from observational data and suggests the feasibility of determining causal inference when an experimental setting is unavailable or costly. Note that the identification of the causal direction lies in the additional information. This approach also shows its potential in the era of big data, given the ubiquitous availability of additional information (Agarwal and Dhar 2014). We believe in the potential of the approach to contribute to the area of business analytics.

We structure of the rest of our paper as follows. Section 2 reviews the related literature. Section 3 introduces the model; specifically, we explain what the causal effects in our estimation are, how to use a graphical model to represent and identify the causal effects, and our estimation scheme. We include a discussion of the relevant literature and technical details in the online supplement to aid readers’ understanding.

Section 4 describes the data that we use in the empirical application, and Section 5 presents the estimation results. We provide the robustness check in Section 6, and in Section 7, we conclude the paper by discussing the managerial implications, explaining the limitations, and providing directions for further research.

## 2. Literature Review

Our research is related to the literature on app analytics with a focus on the app usage patterns, the mega social media app, and the app promotional strategy. In terms of the methodology, we borrow the graphical model approach from the statistics and computer science area to help us to identify the spillover effects of WeChat from observational data. We discuss these streams of research below.

## 2.1. App Usage Patterns

Past works have relied mainly on observed app attributes or policy intervention to study the demand and externalities of an app. For example, as noted, Carare (2012) estimates the externality of app demand through the attribute of rank on the app platform, showing that users’ willingness to pay for top-ranked apps is an additional \$4.50 compared with that of the same unranked app. Ghose and Han (2014) estimate the demand of apps, given their measurable characteristics, and find evidence of the use the attribute of in-app purchase design and the removal of the attribute of in-app advertisements as a means to compete for market share with an assumption of attribute (characteristic) substitution. Han et al. (2016) structurally estimate app demand with the attribute of functional category. Li and Agarwal (2016) estimate the demand and interapp spillovers by the intervention of app integration between Facebook and Instagram. Lee et al. (2018) show the externality of an app by investigating the effects of similarity of app attributes on users’ download and usage decisions in the context of cross-promotions of apps. Zhang et al. (2018) estimate the usage choice of apps based on the attributes of product genre and product popularity index. Even though an attribute- or intervention-based mode could be used to examine the spillover effects of an app, through quantifying cross-app attribute elasticity of demand, and may allow control over the heterogeneity of users, the model heavily relies on the observed attributes or interventions and ignores the spillover contributed by the unobserved heterogeneity of the apps. By estimating the app-level, instead of the attribute-level, interapp causal relationship, our work goes beyond the extant literature by implicitly incorporating the unobserved heterogeneity across different apps and provides a more direct and clearer picture of app demand patterns and externalities.

The earlier app usage pattern literature measures the demand by using app download data (Ghose and Han 2014). Given the maturity of the app market and that the major revenue source has switched to postpurchase usage from the purchasing stage, recent works prefer to use postpurchase activities to measure app usage. Most of the measurements, however, are crude: for example, the identity of an active user (Li and Agarwal 2016), daily app session times (Han et al. 2016, Lee et al. 2018), and daily connection counts (Lee et al. 2018). We measure the postpurchase usage with tap-stream data, which are rare in the prior literature (e.g., Zhang et al. 2018) but arguably more valuable for prediction than are attribute data (Geva et al. 2017). The unique data set provides us with the opportunity to quantify the app externality accurately and finely.

## 2.2. Mega Social Media Apps

Several studies have investigated mega social media apps. Kwon et al. (2016) explain the heavy use of Facebook from a framework of addictiveness and forward-looking rationality. They also find substantial variations in addictiveness and forward-looking propensities across demographically diverse groups. Li and Agarwal (2016) find that the integration of Facebook and Instagram has heterogeneous spillovers on third-party apps. The effects are positive on big third-party apps but negative on small thirdparty apps. Their work supports the potentially strong impact of a mega app on third-party apps. Nevertheless, because Facebook, in its setting, is taken as the platform instead of an individual app, the work does not reveal the mega social media app’s effects on other apps in app platforms (e.g., iOS, Android). We complement past works by providing an understanding of mega social media apps from the perspective of externality and by using an app platform setting.

## 2.3. Promotional Strategies of Mobile Apps

Mega apps that generate heavy use are taken by other app developers as good channels for promoting their products by diverting user traffic to these apps, seen in spillover effects. In this regard, our paper provides insights into the promotional strategies of mobile apps. Going beyond the research on seller- and applevel characteristics (Lee and Raghu 2014), freemium strategy (Liu et al. 2014), and cross-promotion of apps (Lee et al. 2018), our work generates managerial insight into the effectiveness of integration and partnership with a mega app. Our work also contributes to the literature stream of spillover effects of umbrella branding (Sullivan 1990, Erdem and Sun 2002) by empirically examining the app market.

2.4. Causal Graphical Model for Business Analytics Instead of using individual-level econometric analysis $( \mathrm { e . g . }$ , Ghose and Han 2014, Zhang et al. 2018), association-based predictive analysis (Falaki et al. 2010, Tongaonkar et al. 2013, Xu et al. 2013), or survey-based methods (Hoehle and Venkatesh 2015), we study app usage by applying causal inference with a graphical model. The graphical model for causal inference, starting with Pearl (2003, 2009), could be categorized into two streams. The first stream, termed the causality analysis model $( \mathrm { e . g . } ,$ , directed acyclic graph (DAG)), focuses on deriving and testing an identification strategy, given known information and the law of causality. The DAG model is widely applied in the natural sciences (e.g., Greenland et al. 1999, Robins 2001, Hernan et al.´ 2004). In addition, social science research that has clear laws that govern causality also apply the DAG model to analyze and test an identification strategy (e.g., Winship and Harding 2008, Shalizi and Thomas 2011, Sharkey and Elwert 2011, Wodtke et al. 2011).

The more recently developed second stream (e.g., complete partially DAG (CPDAG) and PAG models), which we apply, is for causality discovery by partially learning the causality from data. For example, to find the determinants of the quality of Italian wines, Golia et al. (2017) apply a CPDAG model to wine characteristic-related chemicals and sensory variables to find the causal connection among these variables and Altroconsumo’s Global Score of Quality. Other applications’ ranges are seen in natural science subjects, such as genetics (Badea 2003, Ha et al. 2015), biological and medical sciences (Zhang et al. 2014, Kletenkov 2015, Sokolova 2017), environmental science (Liu et al. 2017), and food science (Golia et al. 2017), as well as in social science subjects, such as economics (Lai and Bessler 2010, Caligaris 2014) and educational science (Fancsali 2013).

In the areas of business analytics, graphical models have been applied to data-mining applications (e.g., Bai et al. 2008). We make the first attempt in this area to apply the causality discovery model to estimate causal effects on observational data when an experimental intervention is unfeasible. The causal interpretation provides an understanding that is deeper than that provided by associations and helps business analysts to improve their decision-making process. The development of our methodology is summarized in Section $^ { 3 , }$ with the details presented in the online supplement.

## 3. Model Speci<sup>fi</sup>cation

We define the spillover effect by following the docalculus proposed by Pearl (1995):

$$
\frac {\partial}{\partial x} E [ Y | d o (X = x) ],\tag{1}
$$

where X is the usage of WeChat, Y refers to the usage of another app on the market, and do represents the exogenous intervention of the value of X. Equation (1) represents the expected change of usage of Y given one unit of exogenous change in the usage of WeChat. It is intuitive that Equation (1) represents a causal effect; that ${ \mathrm { i } } \mathbf { s } ,$ the usage change of the other app is caused by the usage change of WeChat. With observational data, however, the challenge in calculating Equation (1) arises from our inability to implement the do-calculus by exogenously intervening the value of X.

To overcome this challenge, we further borrow the concept of the adjustment set from the causal inference literature (Pearl 1995). The adjustment set is a set of variables that provides full control over the noncausal effects—that is, the confounding effects. Pearl (1995) gives a sufficient condition called a back door criterion to find the adjustment set (see Stage 2 in Section A2 of the online supplement). Denoting Z as the adjustment set and f as the probability density, Pearl (1995) shows that

$$
\begin{array}{l} f (y \mid d o (x)) \\ = \left\{ \begin{array}{l l} f (y \mid x), & \text { if   } Z = \emptyset ; \\ \int_ {z} f (y \mid z, x) f (z) d z = E _ {z} \{f (y \mid z, x) \}, & \text { otherwise }. \end{array} \right. \end{array}\tag{2}
$$

Equation (2) ensures the identification of the causal effect between variables by transforming intervention probability into conditional probability so that we can estimate the causal effect based on observational variables. Specifically, the spillover effect that we defined could be transformed into a conditional expectation by following Equation (3):

$$
\frac {\partial}{\partial x} E [ Y | d o (X = x) ] = E _ {Z} \left[ \frac {\partial}{\partial x} E [ Y | X = x, Z = z ] \right],\tag{3}
$$

where the exchange of expectation over Z and differentiation needs some standard statistical regularity conditions (Klenke 2013). Note that we focus on only the linear causal effect. The spillover effect reduces to the coefficient $\beta _ { 1 } ^ { \prime }$ in the following equation:

$$
y = \beta_ {1} ^ {\prime} X + \beta_ {2} ^ {\prime} Z + c + \varepsilon ,\tag{4}
$$

and we could estimate the spillover effect with valid data on the usage of the other app y, the usage of WeChat X, and valid data for adjustment set Z.

The causal effect estimate in Equation (4) has a consistent interpretation, as is seen in econometrics. Specifically, to differentiate the spillover effects from the correlation between the usages of two apps, we tease out the bias from common confounder(s) captured by Z; Z could be taken as the control variables in an econometric model. To estimate the causal effects of X on $y ,$ researchers need to know what Z is.

In conventional econometric analysis, Z, the control variables, are determined by prior information about the causal structure, which might be based on background knowledge about the data-generation process and relevant theories. Our data, however, as shown in the data description, limit us from knowing the causal structure.

We propose to use the graphical model to overcome this limitation. Specifically, the fundamental idea of a graphical model is that some information about the causal structure has been embedded in the data, which are testable and, thus, recoverable. We make use of the graphical model to recover the causal structure partially and make use of the recovered causal structure to help us find the y that receives a nonzero causal effect from X and the corresponding Z that could adjust the confounding bias.

In Section 3.1, we briefly demonstrate how the graphical model can be used to represent and then recover the causal structure. We further intuitively explain the identification of the graphical model by discussing how to use it to recover the causal structure from observational data and how the recovered graphical model could help us to estimate Equation (4) in Section 3.2.

## 3.1. Graphical Model

We apply three types of well-known graphical models in our papers. The most fundamental graphical model, a DAG (Pearl 2003), is used to represent the underlying causal structure that satisfies causal sufficiency; that is, there are no unobserved confounders and unobserved selection variables. A more intuitive interpretation is that a DAG represents the entire underlying causal structure without any unobserved variables. In a $\scriptstyle \mathrm { { D A G , } }$ each node represents one random variable, and each edge represents a direct causal effect. Given two nodes, X and $Y , \operatorname { i f } X \to Y ,$ , then X is a direct cause (parent) of Y. Note that X and Y are conditionally independent if there is no direct path from X to Y. Given a third node, $C , \operatorname { i f } X \gets C \to Y ,$ , then C is a confounder of X and Y; if $X \to C \gets Y ,$ , then C is a collider of X and $Y ;$ and if $X  C  Y ,$ then X indirectly affects Y through C. The practical application of a DAG model is restricted by its strong assumption of causal sufficiency. In practical empirical research, it is inevitable to have latent variables, variables that are not recorded and observed, and selection variables, which are unmeasured variables that determine whether a measured record is included in our sample. A DAG cannot be applied to represent the underlying causality when latent variable or selection variable exists as a result of the sufficiency causality assumption.

The maximal ancestral graph (MAG), a class of graphical model used to represent the underlying causality on only the observed variables, is proposed to solve this problem (Richardson and Spirtes 2002). Any DAG with latent and selection variables can be transformed into a unique MAG over the observed variables, and this one MAG can represent several DAGs after eliminating unobserved and selection variables (Richardson and Spirtes 2002).

To allow unobserved and selection variables, a MAG has a different interpretation from that of a DAG by using edge marks to represent causal relationships between the observed variables. Given two nodes X and Y representing two observed variables in a ${ \mathrm { M A G } } ,$ $X \to Y$ means that Y is not a (possibly indirect) cause of X. Specifically, the tail at X means that X is a (possibly indirect) cause of Y or of a selection variable, and the arrow at Y means that $Y$ is not a (possibly indirect) cause of X or of any selection variable in all underlying DAGs. Based on this interpretation, a bidirected edge ↔ represents an unobserved confounder, implying noncausal dependency between the two variables on the left and right of the edge. Worth noting is that, compared with DAGs, the MAG interpretation of $X { \xrightarrow { } } Y$ does not exclude the indirect causal effect from X to Y as $X  L $ Y in DAGs where L is a latent variable. It also could not rule out that a hidden confounder is mixed with a (possibly indirect) causal effect.

To further illustrate the relationship between a DAG and a MAG and how a MAG could incorporate latent variables, we borrow and modify an example from Colombo et al. (2012), as seen in Figure 1. In this example, graph (a) is a DAG that represents the underlying causal structure with all of the possible variables, among which $L _ { 1 }$ and $L _ { 2 }$ represent two sets of variables unobservable to researchers; $X _ { 1 } , X _ { 2 } ,$ , and $X _ { 3 }$ are observed variables. By applying the MAG representation, we can uniquely transform the DAG, graph (a), into a MAG, graph (b), which is based on only observed variables. In sum, both DAGs and MAGs are used to represent underlying causal structures, but MAGs are more general, as they can represent the underlying causal structure based on only observed variables explicitly, whereas the latent and selection variables are implicitly “absorbed” by a “weaker” interpretation of the edge.

Having the data generated from the underlying causal structure represented by a MAG, the third graphical model, a PAG, is used to learn/estimate the causality from those data. A PAG has an identical interpretation as that of a MAG except for an additional circle sign of an edge (see Figure 1(c)), representing uncertainty (underidentifiable). A direct edge from node X to Y in a PAG means a direct edge from X to Y in all possible underlying MAGs, indicating that

(a)  
Figure 1. Interpretation of Graphical Models: (a) a DAG, (b) a MAG, and (c) a PAG  
(b)  
(c)  
![](/api/attachments/QDA3BUZ9/fulltext/images/d5357f9a0e7888acdc2813ca31f784d96ee4a916812c7729c9a35331ef7e1bbd.jpg)

Y is not a cause of X. Based on this consistent interpretation, a PAG could be taken as a partial recovery of an underlying MAG by learning/estimation from the data. The reason for the partial recovery instead of a full one is explained by the identification, which we will discuss in the next subsection.

As empirical research, we take observational data as the input to estimate a PAG, which recovers the causal structure graphically as the output. The PAG helps us to find a Y that receives a nonzero causal effect from X and the corresponding Z that could adjust the confounding bias, which further helps us to estimate the quantitative causal effect by Equation (4).

## 3.2. Identi<sup>fi</sup>cation

The graphical model empowers researchers with additional causality identification compared with conventional econometric analysis. In econometric analysis, researchers use prior information about a causal relationship to specify the model, including the causal variable, the outcome variable, the control variables, and, potentially, the instrumental variables. Those variables might be a subset of the available data and thus are taken as the local information about the interested causality. This approach is efficient when the causal structure is clearly known, as it uses smaller but precise local information to identify the causality.

When the causal structure is not known, however, researchers might have to sacrifice efficiency. Our approach is one of such less efficient methods. The intuition behind the graphical model approach is a “zoom-out and zoom-in” process. We zoom out by making use of the entire observed system—that is, the global information, in which the nonfocal information might have the potential to identify our focal causality. Specifically, the PAG is used to recover the causal structure over all of the observed variables, including our focus, the usage of WeChat. We further zoom in by focusing on the learned causal structure of the usage of WeChat to identify its causal effect. Because the spillover effect of WeChat might be identified by other variables, the identification of the causality is attributed to the incremental information (from local to global).

According to the zoom-out and zoom-in processes, the identification scheme of our model can be divided into two stages. The zoom-out stage uses a PAG to partially identify the causal structure over all of the observed variables that are generated from an underlying MAG. Technically, a PAG represents a Markov equivalence class that is formed by several MAGs that have exactly the same conditional independence relationship (Ali et al. 2009). Researchers could thus apply the conditional independence test on the data generated from a MAG to identify/learn a PAG. For the example in Figure 1, if $X _ { 1 } , X _ { 2 } ,$ , and $X _ { 3 }$ are generated from (a) and are observed, we could test and find only the independence between $X _ { 1 }$ and $X _ { 3 }$ conditional on an empty set of variable, indicating $X _ { 2 }$ not being a cause of $X _ { 1 } , X _ { 3 } ,$ , or a selection variable. Therefore, we could draw Figure 1(c) to represent the tested causal structure, where the two arrowheads represent $X _ { 2 }$ not being a cause of $X _ { 1 } , X _ { 3 } ,$ , or a selection variable. The two circle marks at $X _ { 1 }$ and X represent uncertainty about whether $X _ { 1 }$ and $X _ { 3 }$ are causes of $X _ { 2 }$ . Following this idea and under the faithfulness assumption, FCI is developed and is proven to robustly identify the causal structure in the presence of arbitrarily many latent variables (Spirtes et al. 2000) and arbitrarily many selection variables (Spirtes et al. 2000. It is also shown that, when interpreted as a PAG, the learned graph is complete by the method we apply (Zhang 2008b).

The zoom-in stage uses the recovered causal structure of interest in the PAG to identify the causal effects of WeChat. This process explains how to use a PAG to enable Equation (4) by finding the adjustment set Z. Intuitively, it is easy to specify an econometric model when the causal structure is absolutely clear. A PAG might be limited, however, in clearly representing the causal structure because the PAG (as does the MAG) interpretation does not exclude the hidden confounders. For example, X → Y, representing that Y is not a cause of X, might indicate a latent variable L as a common and unobserved confounder for both X and Y. Because L is unobserved, we cannot eliminate the omitted variable bias when estimating causal effects. To address this limitation, we further test whether an edge is a visible edge (Zhang 2008a). A visible edge is one that eliminates the potential unobserved confounders. When the causal relationship of interest is tested as a visible edge, the causal relationship in a PAG is clear enough for us to estimate (the bound of) causal effects. Specifically, both the generalized back-door criterion (GBC) of Maathuis and Colombo (2015) and the GAC of Perkovic et al. (´ 2015) can be applied to find Z from a PAG. We provide technical details in the online supplement.

The identification scheme also has limitations. First, if we want to apply FCI, required assumptions must be satisfied, including the local Markov condition, faithfulness condition (details are in the online supplement), and normality assumption. Second, this approach does not guarantee identification. Specifically, an uncertain tail mark in a PAG implies that the information is insufficient to identify the causality. Furthermore, an invisible edge indicates the risk of unobserved confounders. Therefore, we could estimate only the causal effects when the corresponding edge is certain and visible. In fact, a graphical model may fail to identify a causality that could be identified by a classic econometric model when valid local information is available. The advantage, however, is magnified by opening a new avenue for possible causality identification when the classic econometric approach is infeasible.

## 3.3. Estimation Scheme

Following the identification schemes, we estimate the causal effects in two stages. In the first stage (zoomout), we recover the causal structure from our data by learning a PAG using the FCI algorithm, which presents all of the identifiable causal relationships information. In the second stage (zoom-in), we test whether the potential edges that represent the spillover effects of WeChat are visible edges. If they are, we find the adjustment set by applying GBC (or GAC) and estimate the causal effect scales quantitatively by Equation (4). We discuss these two steps in detail in the online supplement.

## 4. Data

We use a unique data set that records the app usage behavior of 600 randomly sampled smartphone users in China. For each, we have one observation of the weekly frequency of clicking on all available apps. The number of clicks in each app, which is a measure of user activities while using the app, during the observation window is recorded. We collect the data for one nonholiday week, starting February 7, 2015, for the purpose of model estimation.

To check the robustness of our finding with respect to stationarity over time, we additionally collect data sets in the same way but for the time windows of the following two weeks (the weeks of February 14, 2015, and February 21, 2015). Note that these two weeks cover the Spring Festival (Chinese New Year), which is a seven-day national holiday. This enables us to test whether the causal effects are, in general stationarity, between holiday and nonholiday times. In addition, to check for sampling errors, we collect data sets for another sample of 600 individuals that have no overlap with the original sample in the same way as we execute the original data set for the same three weeks. In sum, we have two cross-sectional samples and three time periods for each at a weekly level. To erase the concerns of seasonality and the observation window width, we additionally collect one more data set of four-week app clicking frequency in April.

To show that our data are representative of app usage, we compare our clicking frequency data with time-spent data. In particular, we collect the average time spent for each app and aggregate our data to the same grain, based on which, the results of Pearson correlation test suggests a significantly high degree of linear correlation (0.9765 with a p-value of 2.2e<sup>−</sup>16).

The final data, including data for a robustness check, included 1,122 different apps. We estimate, however, the causal relationship of only the top 50 most used apps in the main model for the following reasons. First, the use of many rarely used apps exhibits no dependency on the rest. Having a smaller set generates a more concise presentation. Second, those rare apps typically focus on niche markets, which have a less significant impact on the app market compared with those of top-ranked apps. Third, methodologically, the (log transformation of) usage of rarely used apps barely satisfies normal distribution assumptions, which can not only lead to problematic results but also contaminate the results of those frequently used apps. To alleviate concerns about this approach, we extend the set to include more apps for the analysis presented in Section 6. Compared with a PAG estimated with an extended set of vertices that includes more apps, a PAG estimated with the top 50 apps shows that the spillover effects of our focal app, WeChat, are well captured and depicted locally.

We list the top 50 apps in China ordered by the clicking frequency and note the developer and alliance of each in Table 1. It is apparent that the app market is not fragmented, suggesting that major developers, such as Baidu, Alibaba, and Tencent, dominate the app market.

In Figure 2, we present the distribution of app usage observed in our data by drawing bar graphs, with the x axis representing different apps sorted by usage in a descending manner and the y axis the usage calculated by the individual average clicking rate in a week of each app. As shown in Figure 2(a), the usage for different apps exhibits a typical long tail, with WeChat’s on the left extreme. As seen in Figure 2(b), a closer examination of the top 50 frequently used apps listed in Table 1 shows that the usage of WeChat (the left extreme) is at least two times that of the second most frequently used app, confirming its mega status

Table 1. App Number, App Name, and Corresponding Developer or Affiliation

<table><tr><td>App rank</td><td>App no.</td><td>App name</td><td> $Developer\ or\ alliance^a$ </td><td>App rank</td><td>App no.</td><td>App name</td><td> $Developer\ or\ alliance^a$ </td></tr><tr><td>1</td><td>1</td><td>WeChat</td><td>T</td><td>26</td><td>40</td><td>91 Lotto</td><td>B</td></tr><tr><td>2</td><td>2</td><td>Tencent Maps</td><td>T</td><td>27</td><td>41</td><td>JD.com</td><td>T</td></tr><tr><td>3</td><td>3</td><td>QQ</td><td>T</td><td>28</td><td>42</td><td>Baidu Search</td><td>B</td></tr><tr><td>4</td><td>4</td><td>Tencent Video</td><td>T</td><td>29</td><td>46</td><td>Ali Pay</td><td>A</td></tr><tr><td>5</td><td>5</td><td>QQ Space</td><td>T</td><td>30</td><td>48</td><td>Wo Music</td><td>O</td></tr><tr><td>6</td><td>6</td><td>Weibo</td><td>A</td><td>31</td><td>54</td><td>MeiTuan</td><td>A</td></tr><tr><td>7</td><td>7</td><td>Other QQ products</td><td>T</td><td>32</td><td>55</td><td>Baidu Map</td><td>B</td></tr><tr><td>8</td><td>9</td><td>Voice Control</td><td>O</td><td>33</td><td>59</td><td>Moji Weather</td><td>O</td></tr><tr><td>9</td><td>10</td><td>Didi</td><td>T</td><td>34</td><td>60</td><td>QQ Music</td><td>T</td></tr><tr><td>10</td><td>13</td><td>Tencent News</td><td>T</td><td>35</td><td>68</td><td>Iqiyi</td><td>O</td></tr><tr><td>11</td><td>14</td><td>Sogou Typing</td><td>S</td><td>36</td><td>72</td><td>Tieba</td><td>B</td></tr><tr><td>12</td><td>15</td><td>QQ Browser</td><td>T</td><td>37</td><td>74</td><td>Baidu Wenku</td><td>B</td></tr><tr><td>13</td><td>17</td><td>Youku Video</td><td>A</td><td>38</td><td>87</td><td>Xunfei Plugin</td><td>O</td></tr><tr><td>14</td><td>18</td><td>Kugou Music</td><td>O</td><td>39</td><td>88</td><td>Baidu Assistant</td><td>B</td></tr><tr><td>15</td><td>20</td><td>Gaode Map</td><td>A</td><td>40</td><td>91</td><td>ZD Clock HD</td><td>O</td></tr><tr><td>16</td><td>21</td><td>Baidu Category</td><td>B</td><td>41</td><td>101</td><td>Wangyi News</td><td>Y</td></tr><tr><td>17</td><td>22</td><td>UC Browser</td><td>A</td><td>42</td><td>109</td><td>WIFI</td><td>O</td></tr><tr><td>18</td><td>23</td><td>360 Guide</td><td>O</td><td>43</td><td>132</td><td>Sohu News</td><td>S</td></tr><tr><td>19</td><td>24</td><td>TouTiao</td><td>O</td><td>44</td><td>146</td><td>App Store</td><td>O</td></tr><tr><td>20</td><td>27</td><td>Android MKT</td><td>O</td><td>45</td><td>149</td><td>Sohu Video</td><td>S</td></tr><tr><td>21</td><td>29</td><td>MiLiao</td><td>O</td><td>46</td><td>152</td><td>Fun TV</td><td>O</td></tr><tr><td>22</td><td>32</td><td>91Phone Assistant</td><td>B</td><td>47</td><td>188</td><td>App Market</td><td>O</td></tr><tr><td>23</td><td>33</td><td>Baidu Map Plugin</td><td>B</td><td>48</td><td>196</td><td>Coolpad Weather</td><td>O</td></tr><tr><td>24</td><td>35</td><td>Sina News</td><td>A</td><td>49</td><td>239</td><td>Kowo Music</td><td>B</td></tr><tr><td>25</td><td>39</td><td>Taobao</td><td>A</td><td>50</td><td>332</td><td>Momo</td><td>A</td></tr></table>

<sup>a</sup>A, Alibaba; B, Baidu; T, Tencent; S, Sohu; Y, Wangyi; O, other or independent developer.

in app usage. We further check the stationarity by including the data set for a robustness check and depict the average weekly clicking rates across 1,200 individuals over three weeks in Figure 2, (c) and (d) A comparison with Figure 2, (a) and (b), shows similar shapes but fatter tails for their distributions.

Figure 2. App Usage of Estimation Sample and Pooled Sample  
(a)  
![](/api/attachments/QDA3BUZ9/fulltext/images/680f3c7bc9233a4661b9cfc7e8c41f2f4c2a174aa72deb74a4e9c98a6307dbfb.jpg)

(b)  
![](/api/attachments/QDA3BUZ9/fulltext/images/29dfe751e48b7b354454ef435f1ebe40c2153c57c2328fe84ba9be573ad20a2a.jpg)

(c)  
![](/api/attachments/QDA3BUZ9/fulltext/images/21a62dc8febc00172826aa9644987a1ec88496c5d3f90a87663a97c0d0622782.jpg)

(d)  
![](/api/attachments/QDA3BUZ9/fulltext/images/944dc6bb1afe6949f4f45e37cdeceea3725b4ee22029af198f4c3ee1194ac743.jpg)

Figure 3(a) presents the distribution of WeChat usage across different users through a histogram with the x axis as the possible value of the WeChat clicking rate and the y axis as the frequency of sampled users. The figure shows that the clicking rates are quite skewed, with the majority of users’ having clicking rates of fewer than 5,000, with the maximum above 20,000. The skewness suggests a potential problem of using a multivariate normal distribution in the estimation of causal effects. Therefore, we take a log transformation of our data to approximate a multivariate normal distribution. For WeChat, the histogram of the transformed data is shown in Figure 3(b). Because of the difficulty of checking the normality of our high-dimensional data visually, we conducted a Mardia’s multivariate normality test to examine the effectiveness of using log transformation to satisfy the Gaussian condition. The test results, obtained by using a subset of the top 50 most frequently used app sample, has a p-value for skewness of 0.19 and a pvalue for kurtosis of 0.13, which does not allow the rejection of the null hypothesis of a 50-dimensional normal distribution. When we use the set of top 100 or top 300 most frequently used apps, however, the test results no longer favor the normality hypothesis. This is because many users rarely use the less popular apps, resulting in skewness to the left-hand side. The results validate the assumption of Gaussiandistributed data and justify the use of the FCI algorithm for our main model. This also indicates the potential problem of the robustness if we use a larger set of apps for the model estimation.

## 5. Estimation Results

We present the results in the following manner. First, we provide the causal structure of app usage graphically as the PAG that we determined through the FCI algorithm. Second, we measure the spillover effects quantitatively based on the estimated PAG, using the GAC and GBC criteria, with econometric interpretation. The quantitative measurement provides further information on the causal effect as positive or negative as well as its strength. Third, to show the value of the graphical model for estimating causal effects, we extend our discussion to cases that are assumed to be estimated without knowing the causal structure from a PAG or with an incorrect adjustment. In these examples, the existence of spillover effects is ruled out by graphical results and interpretation; however, these effects are estimated to be significantly nonzero as a result of the bias of incorrect adjustment.

Figure 3. Distribution of WeChat Usage  
(a)  
![](/api/attachments/QDA3BUZ9/fulltext/images/b44f866690fd1f7c025a98e349b546312e27d7cde1caef309a627df476f8ac0a.jpg)

## 5.1. Stage 1: Graphical Results

We present our estimated causal diagram in Figure 4.<sup>1</sup> In this diagram, each node shown as a number represents an index of one specific app $( \mathrm { i . e . , \Omega ^ { \prime \prime } A p p n o . } ^ { \prime \prime }$ in Table 1). The diagram explicitly displays local causal effects of WeChat (app 1). Note that the edges out of WeChat are visible (1 → 13 and 1 → 39). This indicates that there are no unobserved confounders behind a direct edge and that each directed edge out of WeChat represents corresponding causal effects explicitly. Specifically, the diagram shows that WeChat has direct spillover effects on two apps: Tencent News (app 13), a news app developed by the same parent company, and Taobao (app 39), the leading shopping platform in China, developed by Alibaba. Because the interpretation also relies on the sign and scale of the causal effects, we will later explain these two spillover effects after reporting the quantitative results.

Other than these two apps, WeChat exhibits direct correlations with other QQ products (app 7) and App Store (app 146), driven by unobserved confounders (as they are connected bidirectly). The diagram in Figure 4 suggests that the correlation between all other apps and WeChat is confounded by hidden variable(s) that is (are) not observed and/or conditionally driven by colliders (observed selection variables) in the data. In sum, the diagram suggests that even though WeChat dominates smartphone user app use, its direct externality toward other apps is not as strong as we had expected. In fact, it is so limited that only two other apps are affected directly.

The finding suggests that although associations between WeChat and other focal apps might exist, they are not necessarily indicative of causality. In fact, for the majority, it is confounders rather than spillover effects from WeChat that explain the association. App developers should be cautious about being deceived by associations when analyzing attribution and collaboration, as the identities of factors that determine the usage of apps might not be the same ones that show the association of usage with the focal app. Given that a partnership or integration with such mega apps might incur high costs, our approach provides a tool that allows app developers to visually and directly examine the spillover effects from WeChat and other apps. Our approach provides an understanding that is deeper than that provided by superficial association and helps app developers with decision making with regard to developing partnerships or integration for economic interests.

(b)  
![](/api/attachments/QDA3BUZ9/fulltext/images/33eaac0d541fa442a04d8231229f92fc6f69950368115a8b1649b4205c40fc3b.jpg)

Figure 4. PAG of (Top 50) App Usage Causal Structure  
![](/api/attachments/QDA3BUZ9/fulltext/images/6763db3224fdd351b3de9bbc042aec36bd31b8b981231c1be6d9ca08984d67a9.jpg)

Worth noticing is that the estimated PAG contributes not only to qualitative but also to quantitative findings. Any node without a (possible) causal path from WeChat is indicated as having no significant causal effects from WeChat. Therefore, it can be concluded quantitatively that all nodes in Figure 4, other than Tencent News and Taobao, receive causal effects from WeChat that are not statistically different from zero. This generates many insights into the app identities. For apps that are developed by the same parent company or in partnership with WeChat (shown in Table 1), our results imply that the reward for promoting a focal app through umbrella branding and/or integration with the mega app might be limited. The umbrella-branding effects might be offset by the low switching cost between brands on the smartphone. The results also indicate that app integration might be more like opening a new but independent channel on a mega app rather than diverting user traffic to the app. For the apps that are developed by competitors, we can explain the insignificant spillovers by the well-differentiated functionalities among the major apps. In fact, only three other apps (QQ, Momo, and Weibo) are in the category of social media in our data. The insignificant spillovers on them might be explained by the market segmentation. For example, Momo is more dating oriented, QQ targets younger users, Weibo is an open and Twitter-like self-broadcasting channel, and WeChat is a closed and communication-oriented plat form (Zhao 2017).

The graphical results further support the estimation of the quantitative results. Specifically, Figure 4 shows that both paths to Tencent News and Taobao are visible edges and that noncausal paths are all blocked by colliders for both Tencent News and Taobao, implying that the adjustment set Z is an empty set, following the GAC or GBC. The model simply reduces to a linear regression with the usage of the focal app, WeChat, as the only independent variable.

## 5.2. Stage 2: Quantitative Results

For apps that receive significant spillover effects, we estimate their scale quantitatively in additional steps. Table 2 shows that the spillover effects of WeChat are positive for both Tencent News and Taobao. Specifically, for an average user of WeChat, a 10% increment of usage of WeChat leads to 7.25% additional usage of Tencent News and 8.33% more usage of Taobao.

The mechanism for the spillover effect from using WeChat to Tencent News could be explained by their partnership. As these apps have been developed by the same parent company, WeChat’s functionality better complements that of Tencent News than that of the news app developed by others. In particular, news provided by Tencent News will have a higher priority in being shown and a higher ranking in the results when users search in WeChat. Users could easily share news from Tencent News with friends in chat or the social feed’s “moment.” These features endow WeChat users with a higher opportunity to interact with news provided by Tencent News on WeChat. We also notice that Tencent News does not provide all of its features in WeChat. For example, on WeChat, users can read the main body of the news but cannot access or read comments or post a comment about a news piece. To access the additional features, WeChat directs users to open the Tencent News app. In sum, WeChat fosters users’ interaction with Tencent News-supported features by satisfying their basic need to read news on WeChat, which triggers advanced needs for extended features. Those advanced needs generate spillover to Tencent News app usage.

Furthermore, the mechanism of WeChat’s spillover on Taobao might be attributed to Taobao’s attempt to use WeChat as an economically effective customerrelationship management tool and advertisement platform. Note that Taobao is an eBay-like consumerto-consumer e-commerce platform. Individual sellers on Taobao could use the (group) chat function and the social feeds to promote products and to manage and communicate with potential consumers. For example, Taobao has specially designed a WeChatcompatible advertisement generator, Tao-kouling, so that sellers can post the generated advertisement as social feeds on WeChat. Because users cannot conduct a Taobao-based transaction on WeChat, they have to move to Taobao to make a purchase. Therefore, the shopping demand generated from WeChat will results in spillover to Taobao.

Table 2. Estimation Results

<table><tr><td>Parameter</td><td>Tencent News (13)</td><td>Taobao (39)</td></tr><tr><td> $\beta_1$ </td><td>0.35***(0.02)</td><td>0.40***(0.03)</td></tr><tr><td>c</td><td>0.20*(0.10)</td><td>0.35*(0.14)</td></tr><tr><td>Marginal effects (10% in X)</td><td>7.25%</td><td>8.33%</td></tr></table>

\*\*\* indicates significance at the 0.001 level; \*\* indicates significance at the 0.01 level; \* indicates significance at the 0.05 level.

Taken together, the quantitative and graphical results indicate the overall impact of WeChat on the other major apps. WeChat does not crowd out the use of apps that have a high degree of overlapping functionalities; however, it also does not benefit the usage of apps with the same umbrella brand or in partnerships. In sum, the limited but positive overall spillover effect on the top apps suggests that WeChat’s success might not be achieved by cannibalizing the usage of other major apps. With the cannibalization explanation being ruled out, one plausible reason for WeChat’s being a mega app might be that WeChat carries individuals’ nonmobile activities over to the mobile setting (Xiao 2017). These activities include, but are not limited to, social activities, information seeking, payment, and shopping, which further spill over to the other complementary apps. This finding suggests the overall positive impact of WeChat on the app platform and thus alleviates the concerns of the platform owner regarding WeChat’s threat.

## 5.3. Estimates Based on Incorrect Adjustments

The value of a graphical model is not limited to aiding the estimation of causal effects. Moreover, the estimated causal structure itself encodes enormous interpretable information on causal effects that helps researchers achieve an understanding of correctly adjusted causal effects, which would otherwise be incorrectly estimated. In this section, we present several common representative cases in econometric causal inference that appear in our context, including unadjustable latent confounding bias, adjustable latent confounding bias, and endogenous selection. Note that the value of a PAG is not limited to the three cases that we mentioned above. In addition, it can solve overcontrolled bias, observed confounding bias, and so forth (Elwert 2013). We skip those issues, however because those cases do not appear in our context. Furthermore, an incorrect adjustment can happen in any vertices in our data. Because of space limitations, we illustrate only three cases that occur in our data through three representative vertices.

5.3.1. Unadjustable Latent Confounding Bias. Based on the interpretation rule of a PAG, a bidirected edge A ↔ B suggests that A has no causal effects on B (because of the arrowhead at A) and that B has no causal effect on A (because of the arrowhead at B). There is no ancestral relationship between A and B, but they are adjacent. Therefore, the association between A and B can be explained only by latent confounder(s) (Kalisch et al. 2012). Because the confounder(s) are unobserved, the confounding bias cannot be adjusted. Therefore, a linear regression model cannot correctly estimate the causal effect between A and B. A na¨ıve regression of A on B would induce the confounding bias as a result of the unobserved confounder.

In our example, unadjustable latent confounding bias exists between the usage of WeChat and that of other QQ products as well as between the usage of WeChat and that of App Store. The interpretation of a PAG suggests no causal relationship between WeChat and QQ products or App Store. Researchers, however, would estimate the causal effect as positively significant if they have no information about the causal structure and mistakenly regard the association as causal effects. We estimate the association and compare it with the causal effect based on a PAG, as seen in Table 3.

This result shows the methodological advantage of a PAG for estimating causal effects from observational data with hidden confounder(s). Other methods for causal inference alleviate the confounding bias by controlling potential confounding factors, such as propensity score matching. Such an approach, however, is limited to conditioning on observed confounder(s) only, leading to biased estimation when unobserved confounders exist. The PAG approach, by contrast, infers the existence of an unobserved confounder, which further helps researchers to adjust causal effects correctly.

5.3.2. Adjustable Latent Confounding Bias. Latent confounding variables are adjustable when observed intermediate noncollider vertices exist on the causal path from the latent confounder to focal variables. The simplest example is A ↔ B → C. In this example, A has no causal effect on B or C. However, A and C show an association as a result of a common confounder between A and B. This confounder exhibits a causal effect on C indirectly through B. Given that the edge between B and C is visible because A points to B and B is a noncollider, conditioning on B would control the causal effects from the latent confounder to C. Therefore, a linear regression of B and C would adjust the latent confounding bias. If A ↔ B → C is the only unblocked path between A and C, the regression that suggests 0 as the coefficient for A can be used as the validation for the bias of the adjustable latent confounding variables.

In our example, one apparent path with latent confounding bias is from WeChat to QQ (app 3), another instant messaging app developed earlier by Tencent, through other QQ products, shown as 1 ↔ 7 → 3. Note that there is no other unblocked path between WeChat and QQ. The graph suggests that adding usage of other QQ products in an adjustment set Z would control the causal effect from WeChat to QQ. The results in Table 4 confirm our expectation by showing the causal effect of app 1 on app 3 to be insignificantly different from 0. The estimation of causal effects without controlling the usage of other QQ products would result in a biased estimation as a result of failing to adjust for the effect of unobserved confounder(s) between app 1 and app 7.

This finding also shows considerable consistency with recent observations and anecdotes about the relationship between QQ and WeChat, two instant messaging apps by the same developer, from an industry perspective. QQ has repositioned itself to be a one-stop entertainment portal for young Chinese, a generation with great enthusiasm for virtual-world subcultures (Liao 2017). Individual users would be driven to use these two apps based on different functional needs, such that no direct dependency between these two apps should exist. Other confounder(s), however, might encourage usage of both apps, which would result in association, consistent with our estimation results.

5.3.3. Control over Selection Variable. In the two cases above, we show the potential bias as a result of fail ing to control for noncausal factors. In econometrics, such cases are typically due to the absence of confounders as valid control variables. This leads to a concern about whether this means that we should have as many control variables as possible to alleviate biasness to the maximal level. In this section, we present a problematic estimation if the control variable is a collider (selection variable), rather than a confounder on the path. Note that the PAG identifies the role of each node on a path as a collider. This again shows a methodological advantage compared with models that have an uncertain status of the confounder or collider of each control variable before estimation.

The problem of endogenous selection bias occurs when a collider is added to the adjustment set Z.

Table 3. Example of Unadjustable Latent Confounding Bias

<table><tr><td></td><td>Parameter</td><td>Other QQ products (7)</td><td>App Store (146)</td></tr><tr><td rowspan="2">Association</td><td> $\beta_1$ </td><td>0.45*** (0.03)</td><td>0.17*** (0.02)</td></tr><tr><td>c</td><td>1.25*** (0.13)</td><td>0.02 (0.01)</td></tr><tr><td>Causal effects by PAG</td><td></td><td>0</td><td>0</td></tr></table>

\*\*\* indicates significance at the 0.001 level; \*\* indicates significance at the 0.01 level; \* indicates significance at the 0.05 level.

Table 4. Example of Adjustable Latent Confounding Bias

<table><tr><td></td><td>Parameter</td><td>Adjusted</td><td>Unadjusted</td></tr><tr><td rowspan="3">Association</td><td> $\beta_1$ </td><td>0.01 (0.02)</td><td>0.45*** (0.03)</td></tr><tr><td> $\beta_2$ </td><td>0.96*** (0.02)</td><td></td></tr><tr><td>c</td><td>0.29*** (0.07)</td><td>1.49*** (0.01)</td></tr><tr><td>Causal effects by PAG</td><td></td><td>(7) has effect on (3)</td><td>0</td></tr></table>

\*\*\* indicates significance at the 0.001 level; \*\* indicates significance at the 0.01 level; \* indicates significance at the 0.05 level.

Specifically, conditioning on the common outcome of two variables induces a spurious association between them for at least one value of the collider (Elwert 2013). For example, when we have a PAG shown as $A  B  C ,$ this suggests one possible structure with two latent variables, revealed as $A \left. L _ { 1 } \right.$ $B \left. L _ { 2 } \right. C ,$ and that A does not have any causal effect on C if there is no other path or if all other paths are blocked. If we condition on observed vertex $B ,$ however, the causal structure will be replaced with $A \left. L _ { 1 } - L _ { 2 } \right. C ,$ , where A is associated with B because of the spurious path between $L _ { 1 }$ and $L _ { 2 } .$ Because $L _ { 1 }$ and $L _ { 2 }$ are unobservable and thus cannot be added into the adjustment set to block this spurious path, a spurious causal effect will be estimated to represent the endogenous selection bias.

There are many potential examples of endogenous bias if we do not design the adjustment set in the correct way. We take a causal relationship between WeChat and 91 Lotto (app 40), the leading online lotto marketplace in China, as an example. According to the estimated PAG, the causal effect from WeChat to 91 Lotto is 0 because there is no causal path from WeChat to 91 Lotto. However, if we erroneously add usage of other QQ products (app 7) into the adjustment set $Z ,$ the causal effect from WeChat to 91 Lotto is estimated to be significantly negative, as shown in Table 5. This is because conditioning on other QQ products opens a spurious confounding path between WeChat and 91 Lotto, whose confounder is unadjustable $( 1 \left. L _ { 1 } - L _ { 2 } \right. 4 0 )$ . This example provides important information for researchers: adding an incorrect control variable risks deteriorating the estimation of causal inference.

Table 5. Example of Endogenous Selection Bias

<table><tr><td></td><td>Parameter</td><td>Adjusted</td></tr><tr><td rowspan="3">Association</td><td> $\beta_1$ </td><td>-0.07** (0.02)</td></tr><tr><td> $\beta_2$ </td><td>0.62*** (0.03)</td></tr><tr><td>c</td><td>-0.23* (0.10)</td></tr><tr><td>Causal effects by PAG</td><td></td><td>0</td></tr></table>

\*\*\* indicates significance at the 0.001 level; \*\* indicates significance at the 0.01 level; \* indicates significance at the 0.05 level.

## 6. Robustness Checks

We conduct a robustness check to ensure the consistency of the findings and to eliminate potential explanations. Given the nature of the two-stage estimation for causal effect estimation, we first check the stability of graphical outputs, as discussed in Section 6.1, and then check that of the quantitative results, as presented in Section 6.2. We examine whether our graphical and quantitative results are particular to the data and the specifications in our main results by comparing the main results with results estimated from an alternative data or specification, with other factors’ being controlled. To compare the graphical results, for each alternative sample or specification, we identify all of the structures (include edges and nodes) that represent WeChat’s (both direct and indirect) causal effects and examine whether the edges and their types are identical to those in our main results. If identical, then we conclude that the main result is not particular to the original data and specification.

## 6.1. Check Graphical Results

To eliminate concern about sampling errors, we use the alternative sample in which there are no overlapping individual users. To eliminate the concern about time-specific factors, we collect further data for the next two weeks. Note that two weeks after the time of the original observation is a national holiday. This would imply a high degree of consistency if the spillover effects of WeChat in the original PAG are the same or close to that in the PAG of the holiday. Given the two sets of samples and the three time periods for each, we could estimate six PAGs. For succinct presentation, we draw graphs of only the causal paths from WeChat. Furthermore, we apply RFCI when FCI is infeasible or invalid. The PAGs are displayed in Figure 5.

As can be seen in Figure 5, the causal paths from WeChat are quite consistent for all six samples. All PAGs show direct causal effects on Taobao (app 13) and Tencent News (app 39), suggesting that the causal effects identified in the original sample are robust to different samples and, thus, robust to sampling errors

Figure 5. PAGs for Two Sets of Individuals and Three Time Periods with alpha = 0.01

![](/api/attachments/QDA3BUZ9/fulltext/images/3bdd52103ad6c140b063362aa3ef85959ce775608506d57605b6f6305aa731ee.jpg)

and time-specific factors. The mild discrepancy lies in the PAG of sample 1 in week 2, which exhibits an indirect causal effect on app 39 through app 41; the PAG of sample 2 in week 1 exhibits an indirect causal effect on app 35 through app 39; and the PAG of sample 2 in week 2 exhibits an indirect causal effect on app 39 through app 46. These effects are quite unstable, however, and could be attributed to sampling errors or time-specific factors.

To eliminate the concern that our findings might be sensitive to the width of observation windows, sample size, seasonality, and app usage measure, we estimate three more PAGs, as seen in Figure 6. We concatenate the three observation windows, combine the two samples used in Figure 5, and estimate a PAG with a sample size of 1,200 and a window of three weeks (left). We further estimate a PAG on a nonoverlapping sample of 1,200 users but with a window of four weeks in April (middle). To address the concern about the app-usage measure, we use the aggregate-level app average time-spent data to calculate an app-level time-click ratio (average time/ average click amount) for each app and multiply these ratios with the original individual-level click data to approximate individual level time spent. We estimate a PAG on the approximated time data (right). All PAGs in Figure 6 show consistency with the causal diagram seen in Figure 4, validating that our finding is not sensitive to the length of the window, sample size, holiday/nonholiday seasonality, or the app usage measure.

The PAGs are drawn based on conditional independence tests with a threshold for significance

Figure 6. PAGs for Pooled Individuals and Longer-Period and Nonholiday Window with alpha = 0.01

Three weeks in Feb Four weeks in Apr Approx. time amount fixed at a certain level (alpha) to control Type I errors in the statistical hypothesis testing framework. The level of the alpha could be regarded as a trade-off between the probability of having an error in independence and the power of detecting dependence. As a result, PAGs estimated on the same observation but with different levels of the alpha might exhibit different patterns. As seen in Figure 7, to examine the impact of the alpha, we relax the alpha from 0.01 to 0.05 and redraw PAGs in the same way as in Figure 5. This figure also shows a high level of consistency of the causal structure. The majority of the graphs show a direct causal effect on Taobao (app 13) and Tencent News (app 39). The graph of sample 1 in week 3 does not have a causal path on Tencent News. Instead, it exhibits a bidirected edge between WeChat and Tencent News. In addition, the graph of sample 2 in week 3 shows additional causal paths, including a direct causal effect on app 4. This is not surprising, however, because as we increase the level of the alpha, we will have more vertices connected because the power of detecting the dependency signal increases.

![](/api/attachments/QDA3BUZ9/fulltext/images/88fa345bb8d3a8044739ea10f01374f47644fce4dc3102d980e8ff3570123dfc.jpg)

The last robustness test is for the set of apps that we use for estimation. Additional information of app usage would provide more information on causal relationship identification. Therefore, robust causal relationships should stay constant if we increase the size of the vertices set. Specifically, we estimate two more PAGs with the top 100 frequently used apps and top 300 frequently used apps, correspondingly shown in Figure 8, (a) and (b), with the alpha fixed at 0.01. The estimation for the PAG with the top 300 apps is implemented with the RFCI algorithm as a result of the infeasibility of applying the FCI to highdimensional data.

Because of the large scale of the vertices, the readability of the graph can be difficult. We examine the adjacent matrix and find the existence of causal paths from both WeChat to Taobao and from WeChat to Tencent News, as seen in Figures 5 and 6. Specifically, the PAG of the top 100 apps shows causal

Figure 7. PAGs for Two Sets of Individuals and Three Time Periods with alpha = 0.05

Week 2

![](/api/attachments/QDA3BUZ9/fulltext/images/0264cd288a85d20ed5e7b017cb183dede4467016a81d5410db281b9c114a76ae.jpg)

Figure 8. PAGs of Larger Vertices Sets: (a) PAG of Top 100 Popular Apps; (b) PAG of Top 300 Popular Apps (a) (b)  
![](/api/attachments/QDA3BUZ9/fulltext/images/261b1c5076d40d9339d7c5dafe83b4048c0e40978beeb628edcd6c50b05ac269.jpg)

paths from WeChat to Taobao and to Tencent News as the only causal paths, which is exactly the same as what is seen in the PAGs of the top 50 apps. Furthermore, the PAG of the top 300 apps has causal paths to Taobao and to Tencent News as the only two direct causal paths. These consistencies suggest that our original model for the top 50 apps is able to capture most of spillover effects of WeChat. The PAG of the top 300 apps, however, has additional indirect causal paths to two apps, one of which is not included in the PAG of either the top 50 or top 100 apps. We reserve a conservative attitude toward these two causal paths, however, for the following two reasons: (1) For the usage distribution of those less popular apps (of the top 100 and top 300 popular app sets), it might be difficult to approximate the Gaussian distribution even after logarithm transformation. As noted, when we took the logarithm of the app usage, if there was a great deal of zero usage, this could cause enormous skewness. And (2) RFCI-PAG is recognized as a supergraph of FCI and has weaker meaning in regard to the presence of edges than does the FCI, as shown in Colombo et al. (2012). Both reasons cast doubt on the robustness of these two causal effects.

## 6.2. Check Quantitative Results

![](/api/attachments/QDA3BUZ9/fulltext/images/fa951a80f0e5e71ed9855ca52bf31f74d33afbeb7b62f4316418c8c456e7e46b.jpg)

We conduct a robustness check for the scale of causal effects. Specifically, we estimate causal effects from the data of distinct samples, time periods, and usage measure, as specified in Figures 5 and 6. Note that the estimation is based on the learned structure in the graphical results, and given a PAG, the specification for learning the graph has no impact on the quantitative estimation results. Therefore, there is no need to investigate the robustness of the alpha level or size of the vertices.

We first estimate spillover effects of WeChat on Tencent News and Taobao with distinct samples across different time periods, specified in Figure 5 separately, using Equation (4). The estimation results are shown in Table 6. Our results suggest a high degree of consistency across distinct samples and time periods. In all specifications of samples, the spillover effects on both Tencent News and Taobao are estimated to be positive, with the effect on Taobao as stronger quantitatively. The scales of effects are quite close among all six samples. The consistency of results based on different samples proves the robustness of our quantitative estimation.

To validate the robustness of the sample size, windows width, seasonality, and usage measure, we estimate spillover effects of WeChat on Tencent News and Taobao based on a larger sample size, longer windows, April data, and an approximated time spent on apps, as was done for the results presented in Figure 6. The estimation results shown in Table are consistent with those in Tables 2 and 6.

Finally, note that pooling those six samples generates a sample of 1,200 individual smartphone users with repeated measures longitudinally. This pooled sample provides us with the opportunity to tease out individual-specific factors and time-specific factors to alleviate confounding bias. Note that our model suggests that no confounder exists on the causal paths from WeChat to Tencent News and to Taobao. Therefore, we expect estimates of parameters in a model with controlled individual-specific factors and time-specific factors to be similar to the estimates in former specifications. We control for individual-specific factors and time-specific factors by adding fixed effects and specify the model as follows:

Table 6. Comparing Quantitative Results Separate Samples

<table><tr><td rowspan="2"></td><td rowspan="2">Parameter</td><td colspan="2">Week 1</td><td colspan="2">Week 2</td><td colspan="2">Week 3</td></tr><tr><td>Tencent News (13)</td><td>Taobao (39)</td><td>Tencent News (13)</td><td>Taobao (39)</td><td>Tencent News (13)</td><td>Taobao (39)</td></tr><tr><td rowspan="2">Sample 1</td><td> $\beta_1$ </td><td>0.35***(0.02)</td><td>0.40***(0.03)</td><td>0.32***(0.12)</td><td>0.37***(0.02)</td><td>0.32***(0.02)</td><td>0.33***(0.03)</td></tr><tr><td>c</td><td>0.20*(0.10)</td><td>0.35*(0.14)</td><td>0.12(0.08)</td><td>0.09(0.11)</td><td>0.18*(0.08)</td><td>0.24*(0.12)</td></tr><tr><td rowspan="2">Sample 2</td><td> $\beta_1$ </td><td>0.38***(0.02)</td><td>0.39***(0.03)</td><td>0.36***(0.02)</td><td>0.33***(0.03)</td><td>0.35***(0.02)</td><td>0.35***(0.03)</td></tr><tr><td>c</td><td>0.25*(0.10)</td><td>0.35*(0.15)</td><td>0.09(0.09)</td><td>0.23(0.12)</td><td>0.14(0.08)</td><td>0.28*(0.11)</td></tr></table>

\*\*\* indicates significance at the 0.001 level; \*\* indicates significance at the 0.01 level; \* indicates significance at the 0.05 level.

$$
y _ {i t} = \beta_ {1} ^ {\prime} X _ {i t} + \beta_ {2} ^ {\prime} Z _ {i t} + c + \xi_ {i} + \tau_ {t} + \varepsilon_ {i t},\tag{6}
$$

where $\varepsilon _ { i t }$ are unobserved error terms following a Gaussian distribution; $\xi _ { i }$ and $\tau _ { t }$ capture individualspecific unobserved effects and time-specific unobserved effects, respectively; and $Z _ { i t }$ is an empty set based on the GAC and GBC when estimating causal effects of WeChat on Tencent News and on Taobao. In addition, we estimate the causal effects by applying an ordinary least squares (OLS) model without fixed effects on pooled data for comparison. We report the estimates in Table 8.

As we expect, parameter estimates for causal effects in model (6) are very close to those of the original model (5). This implies the nonexistence of a confounder that is encoded in the graphical model and further supports the robustness of our quantitative results.

## 7. Implications and Conclusions

We combine a state-of-the-art machine-learning method with an econometric approach to study the spillover effects of WeChat. Specifically, we identify the set of apps that causally receive spillover effects from WeChat, the set of apps that shows association with WeChat as a result of observed or unobserved confounders, and the set of apps for which usage is independent of that of WeChat.

Our work has managerial implications for managing the interapp relationship and the app usage patterns. We estimate the spillover effects of mega app usage on the postpurchasing tap stream data, without restricting the spillover effects to be generated from attribute substitution. The results determine implications for the value that WeChat creates for its developers as well as the value that it delivers to developers of other apps. For the developers, the estimate of spillover effects may help determine the app’s impact on the usage of other apps, including, but not limited to, its competitors, its partners, or umbrella-brand apps. Because the spillover effects provide a good measure of app usage attribution, the mega app developers might determine whether to redesign the product for the purpose of delivering the spillovers to partners and restricting that to competitors. For example, regarding the spillovers to Taobao, WeChat might consider restricting cross-app sales and advertisement activities on its social feeds while integrating the e-commerce functionality of its partners.

Alternatively, WeChat developers might consider leveraging the usage attribution by creating a usagecontribution-based revenue-sharing plan among its partners and umbrella-brand apps and charging nonallied apps for the positive spillovers. The attribution also would help the integration or separation decisions of the WeChat owner, the parent company. For example, the owner might consider further lowering the switching cost by integrating umbrella-brand apps (e.g., Tencent News) or enhancing the integration with partner apps if it receives positive spillovers from the mega one. By contrast, the parent company might consider spinning off an integrated partner app if the integrated functionality does not contribute to WeChat usage and the partner app does not receive spillovers from WeChat. Other app developers also benefit from a better understanding of their dependence on WeChat and their vulnerability to that, which may help them to evaluate the profitability of participating in the app market in the presence of a mega app. Finally, our method provides a flexible tool that could be adjusted easily in regard to any focal app to investigate spillover and to generate insight for stakeholders

For platform owners and platform policy makers, our research has implications for managing the relationship with WeChat or other mega apps. As the first work to investigate the externality of a mega app on the app platform, we find that WeChat’s becoming mega does not causally result in any diminishing demand for the other major apps. Its negative impact on the variety and demand of the platform might thus be limited. By contrast, WeChat contributes to the ecosystem by its own heavy usage and positive spillover effects. Therefore, platform owners might be less concerned about a threat by WeChat. Rather than restricting the growth of WeChat, they might be better off collaborating with WeChat to foster overall platform usage. This implication is consistent with the recent settlement between WeChat and Apple of the revenue sharing of tips on WeChat’s miniprograms (Kubota and Abkowitz 2018).

Table 7. Comparing Quantitative Results: Monthly Pooled Samples

<table><tr><td rowspan="2">Parameter</td><td colspan="2">February 3 weeks</td><td colspan="2">April 4 weeks</td><td colspan="2">Approx. time amount</td></tr><tr><td>Tencent News (13)</td><td>Taobao (39)</td><td>Tencent News (13)</td><td>Taobao (39)</td><td>Tencent News (13)</td><td>Taobao (39)</td></tr><tr><td> $\beta_1$ </td><td>0.42***(0.02)</td><td>0.43***(0.02)</td><td>0.50***(0.02)</td><td>0.54***(0.01)</td><td>0.05***(0.01)</td><td>0.15***(0.02)</td></tr><tr><td>c</td><td>0.26**(0.09)</td><td>0.40**(0.13)</td><td>0.25**(0.09)</td><td>0.11(0.04)</td><td>0.07***(0.01)</td><td>0.11***(0.02)</td></tr></table>

\*\*\* indicates significance at the 0.001 level; \*\* indicates significance at the 0.01 level; \* indicates significance at the 0.05 level.

Our research has implications for app developers who have attempted to promote their focal app through partnership and/or integration with the mega app. Considering WeChat’s umbrella-brand or partnership apps, we find that, counter to the belief of the industry, WeChat has quite limited positive effects on the use of focal apps, implying that the reward for promoting through partnerships and/or integration with a mega app might be limited. This warns other app developers not to be blinded by the heavy user traffic of WeChat. As the overall reward might be limited, the other app developers might be more reserved when deciding on a partnership with WeChat. For the apps that do not complement WeChat, their business strategies might focus on the benefit of multichannel operations rather than diverting user traffic. For the apps that have been integrated with WeChat, we suggest their reevaluation of the objective of the partnership and its cost effectiveness to determine whether to continue or terminate the partnership.

This paper is also the first to apply recent developments in machine learning-enabled causal inference models, such as FCI-PAG, plus a GAC and/or GBC estimation approach in business and economic research. Compared with past research methods, our approach relaxes the need for assumptions to identify causal effects with observational data. To illustrate the importance of determining the causal structure and the value of quantitative information encoded in a graphical model, we intentionally specify the econometric model with an incorrect adjustment set to show the erroneous estimation without the graphical results in the first stage. Our method incurs a cost for obtaining additional information (global information) when determining the causal structure. However, because data have become increasingly rich in this age of big data, this approach has the potential to be widely applied in estimating causal effects in business analytics research. Our work, as pioneering research that applies a graphical model, not only presents the spillover effects of WeChat but also shows a good fit of this advanced method in the context of business analytics research.

Our research is subject to the limitations of the graphical model in practical applications and those resulting from restrictions of the integration of the FCI-PAG-GAC or GBC approach and econometric methods. First, although the model is not restricted to the sample size, it is restricted to high-dimensional data (e.g., more than 100 variables), especially when learned through the FCI algorithm. Even though RFCI could handle a larger dimension, it suffers from weaker meaning in regard to the presence of edges than does the FCI, as shown in Colombo et al. (2012). Second, a more flexible model could be developed to allow for non-Gaussian-distributed data, such as ordinal choice data. Third, even when we estimate a fixed-effect model with individual- and time-specific factors separately in the robustness check, we note that such factors cannot be added into the graphi cal estimation (first-stage estimation) because of the challenge of the independence test between Gaussiandistributed variables and dummy variables. Fourth, more graphical model-based econometric tools should be developed to help estimate or validate the outputs from an FCI-PAG-GAC/GBC approach. For example, a searching algorithm for generalized conditional instrument variables that works in a DAG/CPDAG setting should be extended to a MAG/PAG setting to help to validate the visible edge. Finally, we acknowledge a data limitation of not observing the app usage at an earlier stage because analyzing the earlier growing-stage data might generate more interesting and dynamic findings. Those limitations, in turn, provide avenues for future business analytics research.

Table 8. Spillover Effects Based on Pooled Sample

<table><tr><td rowspan="2"></td><td rowspan="2">Parameter</td><td colspan="2">Tencent News (13)</td><td colspan="2">Taobao (39)</td></tr><tr><td>FE</td><td>Pooled OLS</td><td>FE</td><td>Pooled OLS</td></tr><tr><td rowspan="3">Association</td><td> $\beta_1$ </td><td>0.33*** (0.01)</td><td>0.35*** (0.01)</td><td>0.32*** (0.02)</td><td>0.37*** (0.01)</td></tr><tr><td>c</td><td>-0.48* (0.44)</td><td>0.15*** (0.04)</td><td>-1.05 (0.61)</td><td>0.25*** (0.05)</td></tr><tr><td>FE</td><td>Not reported</td><td>NA</td><td>Not reported</td><td>NA</td></tr></table>

Note. FE, fixed effects.  
\*\*\* indicates significance at the 0.001 level; \*\* indicates significance at the 0.01 level; \* indicates significance at the 0.05 level.

## Acknowledgments

Yifan Dou was the corresponding author. The authors thank the senior editor, the associate editor, and the anonymous reviewers for constructive suggestions, and Dr. Baojun Ma from Shanghai International Studies University for his tremendous research support.

## Endnotes

<sup>1</sup> See https://www.tencent.com/en-us/articles/17000441554112592.pdf.

<sup>2</sup>A complete interpretation of the diagram, including information not relevant to our research objective, is provided in the online supplement.

## References

Agarwal R, Dhar V (2014) Big data, data science, and analytics: The opportunity and challenge for is research. Inform. Systems Res. 25(3):443-448

Ali RA, Richardson TS, Spirtes P (2009) Markov equivalence fo ancestral graphs. Ann. Statist. 37(5B):2808–2837.

Alive Studios (2017) What is Kakao and why should you care? Medium (June 7), https://medium.com/@madebyalive/what -is-kakao-and-why-should-you-care-fcb430bc61d0.

Badea, L (2003) Inferring large gene networks from microarray data: a constraint-based approach. Presentation, Workshop on Learning Graphical Models for Computational Genomics at the 18th International Joint Conference of Artificial Intelligence (IJCAI), August 9, Acapulco, Mexico.

Bai X, Padman R, Ramsey J, Spirtes P (2008) Tabu search-enhanced graphical models for classification in high dimensions. INFORMS J. Comput. 20(3):423–437.

Caligaris S (2014) A causal graphs-based approach for assessing gender disparities: An application to child health and nutrition in China. Unpublished doctoral dissertation, Universita degl Studi di Milano-Bicocca, Milan.

Carare O (2012) The impact of bestseller rank on demand: Evidence from the app market. Internat. Econom. Rev. 53(3):717–742.

Colombo D, Maathuis MH, Kalisch M, Richardson TS (2012) Learning high-dimensional directed acyclic graphs with latent and se lection variables. Ann. Statist. 40(1):294–321.

Danova T (2014) LINE is transforming from messaging app to mobile media platform. Business Insider (February 7), http://www .businessinsider.com/line-is-transforming-from-messaging-app -to-mobile-media-platform-2014-2

Elwert F (2013) Graphical causal models. Morgan SL, ed. Handbook of Causal Analysis for Social Research (Springer, Dordrecht, Netherlands), 245–273.

Erdem T, Sun B (2002) An empirical investigation of the spillover effects of advertising and sales promotions in umbrella branding. J. Marketing Res. 39(4):408–420.

Falaki H, Lymberopoulos D, Mahajan R, Kandula S, Estrin D (2010) A first look at traffic on smartphones. Allman M, ed. Proc. 10th

ACM SIGCOMM Conf. Internet Measurement (ACM, New York), 281–287.

Fancsali SE (2013) Data-driven causal modeling of “gaming the system” and off-task behavior in Cognitive Tutor Algebra. Presentation, NIPS Workshop on Data Driven Education, December 9, Lake Tahoe.

Garg R, Telang R (2013) Inferring app demand from publicly available data. Management Inform. Systems Quart. 37(4):1252–1264.

Geva T, Reichman S, Somech I (2017) The predictive power of en gagement in mobile consumption. Soh C, Henfridsson O, Yoo Y, eds. Proc. 38th Internat. Conf. Inform. Systems (Association fo Information Systems, Atlanta).

Ghose A, Han SP (2014) Estimating demand for mobile applications in the new economy. Management Sci. 60(6):1470–1488.

Golia S, Brentari E, Carpita M (2017) Causal reasoning applied to sensory analysis: The case of the Italian wine. Food Qualit Preference 59(July):97–108.

Greenland S, Pearl JM, Robins JM (1999) Causal diagrams for epi demiologic research. Epidemiology 10(1):37–48

Ha MJ, Baladandayuthapani V, Do KA (2015) Prognostic gene signature identification using causal structure learning: Applications in kidney cancer. Cancer Informatics 14(Suppl. 1): 23–35.

Han SP, Park S, Oh W (2016) Mobile app analytics: A multiple discrete-continuous choice framework. Management Inform. Sys tems Quart. 40(4):983–1008

Hernan MA, Hern´ andez-D´ ´ıaz S, Robins JM (2004) A structural ap proach to selection bias. Epidemiology 15(5):615–625.

Hoehle H, Venkatesh V (2015) Mobile application usability: Conceptualization and instrument development. Management Inform. Systems Quart. 39(2):435–472.

Kalisch M, Machler M, Colombo D, Maathuis MH, Bühlmann P (2012)¨ Causal inference using graphical models with the R package pcalg. J. Statist. Software 47(11):1–26.

Klenke A (2013) Probability Theory: A Comprehensive Course (Springer Science & Business Media, London).

Kletenkov K (2015) The role of the HIV-1 protease substrate in therapy resistance. Unpublished doctoral dissertation, University of Basel, Basel, Switzerland.

Kubota Y, Abkowitz A (2018) Apple and Tencent reach deal to let WeChat users dole out tips. Wall Street Journal (January 15), https://www.wsj.com/articles/apple-and-tencent-reach-deal-t -let-wechat-users-dole-out-tips-1516018849.

Kwon HE, So H, Han SP, Oh W (2016) Excessive dependence on mobile social apps: A rational addiction perspective. Inform. Systems Res. 27(4):919–939

Lai P-C, Bessler DA (2010) On aggregation bias in structural demand models. Poster presentation, 2010 AAEA, CAES, & WAEA Joint Annual Meeting, July 25–27, Denver, Agricultural and Applied Economics Association, Milwaukee.

Lee G, Raghu TS (2014) Determinants of mobile apps’ success: Evi dence from the app store market. J. Management Inform. System 31(2):133-170

Lee GM, He S, Lee J, Whinston AB (2018) Matching mobile appli cations for cross promotion. Working paper, University of British Columbia, Vancouver.

Li Z, Agarwal A (2016) Platform integration and demand spillovers in complementary markets: Evidence from Facebook’s inte gration of Instagram. Management Sci. 63(10):3438–3458.

Liao R (2017) WeChat’s older sibling QQ plans to stay forever young. Technode (August 7), https://technode.com/2017/08 07/wechats-older-sibling-qq-plans-to-stay-forever-young/.

Liu CZ, Au YA, Choi HS (2014) Effects of freemium strategy in the mobile app market: An empirical study of Google Play. J. Man agement Inform. Systems 31(3):326–354

Liu Y, Du Q, Wang Q, Yu H, Liu J, Tian Y, Chang C, Lei J (2017) Causal inference between bioavailability of heavy metals and environmental factors in a large-scale region. Environ. Pollution 226(July):370–378.

Maathuis MH, Colombo D (2015) A generalized back-door criterion. Ann. Statist. 43(3):1060–1088.

Pearl J (1995) Causal diagrams for empirical research. Biometrika 82(4): 669–688.

Pearl J (2003) Causality: Models, reasoning, and inference. Econo metric Theory 19(46):675–685.

Pearl J (2009) Causal inference in statistics: An overview. Statist. Surveys 3:96–146.

Perkovic E, Textor J, Kalisch M, Maathuis MH (2015) A complete ´ generalized adjustment criterion. Meila M, Heskes T, eds. Proc. 31st Conf. Uncertainty Artificial Intelligence (UAI-15) (AUAI Press, Corvallis, OR), 682–691.

Richardson T, Spirtes P (2002) Ancestral graph Markov models. Ann. Statist. 30(4):962–1030.

Robins JM (2001) Data, design, and background knowledge in eti ologic inference. Epidemiology 12(3):313–320.

Shalizi CR, Thomas AC (2011) Homophily and contagion are generically confounded in observational social network studies. Sociol. Methods Res. 40(2):211–239.

Sharkey P, Elwert F (2011) The legacy of disadvantage: Multigenerational neighborhood effects on cognitive ability. Amer. J. Sociol. 116(6):1934–1981.

Sijia J (2017) With new mini-apps, WeChat seeks even more China clicks. Reuters (May 18), https://www.reuters.com/article/us -tencent-wechat-china/with-new-mini-apps-wechat-seeks-even -more-china-clicks-idUSKCN18E38Z

Sokolova E (2017) Causal discovery from mixed and missing data with applications on ADHD datasets. Unpublished doctoral dissertation, Open University of the Netherlands, Heerlen.

Spirtes P, Glymour CN, Scheines R (2000) Causation, Prediction, and Search (MIT Press, Cambridge, MA).

Sullivan M (1990) Measuring image spillovers in umbrella-branded products. J. Bus. 63(3):309–329.

Tongaonkar A, Dai S, Nucci A, Song D (2013) Understanding mobile app usage patterns using in-app advertisements. Roughan M, Chang R, eds. Internat. Conf. Passive Active Network Measuremen (Springer-Verlag, Heidelberg, Germany), 63–72.

Winship C, Harding DJ (2008) A mechanism-based approach to the identification of age–period–cohort models. Sociol. Methods Res. 36(3):362–401.

Wodtke GT, Harding DJ, Elwert F (2011) Neighborhood effects in temporal perspective: The impact of long-term exposure to concentrated disadvantage on high school graduation. Amer. Sociol. Rev. 76(5):713–736.

Xiao E (2017) WeChat’s latest feature aims to make it even more omnipresent. Techinasia (April 2), https://www.techinasia.com mini-programs-conference-offline-businesses.

Xu Y, Lin M, Lu H, Cardone G, Lane N, Chen Z, Campbell A, Choudhury T (2013) Preference, context and communities: A multi faceted approach to predicting smartphone app usage patterns. Proc. 2013 Internat. Sympos. Wearable Comput. (ACM, New York), 69–76.

Ye J (2018) Tencent takes aim at Apple and Google app stores with WeChat mini program push. CNBC (January 10), https:/ www.cnbc.com/2018/01/22/tencent-wechat-mini-program-push -takes-aim-at-apple-and-google.html

Zhang J (2008a) Causal reasoning with ancestral graphs. J. Machin Learn. Res. 9(July):1437–1474.

Zhang J (2008b) On the completeness of orientation rules for causa discovery in the presence of latent confounders and selection bias. Artificial Intelligence 172(16):1873–1896.

Zhang Q, Burdette JE, Wang J-P (2014) Integrative network analysis of TCGA data for ovarian cancer. BMC Systems Biol. 1(8):1–18.

Zhang Y, Li B, Luo X, Wang X (2018) Personalized mobile targeting with user engagement stages: Combining structural hidden Markov model and field experiment. Working paper, University of Texas at Dallas, Richardson.

Zhao L (2017) Key differences between WeChat and Weibo. Seeking Alpha (May 31), https://seekingalpha.com/article/4077861-ke -differences-wechat-weibo.

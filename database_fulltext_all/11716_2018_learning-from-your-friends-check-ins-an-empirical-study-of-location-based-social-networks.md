---
otero_id: 11716
otero_key: "VYNGWKCU"
title: "Learning from Your Friends’ Check-Ins: An Empirical Study of Location-Based Social Networks"
authors: "Liangfei Qiu; Zhan (Michael) Shi; Andrew B. Whinston"
year: "2018"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0769"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

![](/api/attachments/VYNGWKCU/fulltext/images/579563836e13d3bb5edfc76b12d2bc8140b772df397b15c2d8be77c3bbdb2970.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Learning from Your Friends’ Check-Ins: An Empirical Study of Location-Based Social Networks

Liangfei Qiu, Zhan (Michael) Shi, Andrew B. Whinston

Liangfei Qiu, Zhan (Michael) Shi, Andrew B. Whinston (2018) Learning from Your Friends’ Check-Ins: An Empirical Study of Location-Based Social Networks. Information Systems Research

Published online in Articles in Advance 07 Aug 2018

https://doi.org/10.1287/isre.2017.0769

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2018, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Learning from Your Friends’ Check-Ins: An Empirical Study of Location-Based Social Networks

Liangfei Qiu,<sup>a</sup> Zhan (Michael) Shi,<sup>b</sup> Andrew B. Whinston<sup>c</sup>

<sup>a</sup> Warrington College of Business, University of Florida, Gainesville, Florida 32611; <sup>b</sup> W. P. Carey School of Business, Arizona State University, Tempe, Arizona 85287; <sup>c</sup> McCombs School of Business, University of Texas at Austin, Austin, Texas 78705 Contact: liangfei.qiu@warrington.ufl.edu, http://orcid.org/0000-0002-8771-9389 (LQ); zmshi@asu.edu, http://orcid.org/0000-0002-2815-252X (Z(M)S); abw@uts.cc.utexas.edu (ABW)

Received: December 16, 2015 Revised: January 29, 2017; July 18, 2017 Accepted: November 15, 2017 Published Online in Articles in Advance: August 7, 2018

https://doi.org/10.1287/isre.2017.076

Copyright: © 2018 INFORMS

Abstract. Recently, mobile applications have ofered users the option to share their location information with friends. Using data from a major location-based social networking application in China, we estimate an empirical model of restaurant discovery and observational learning. The unique feature of repeat customer visits in the data allows us to examine observational learning in trials and repeats and to separate it from non-informational confounding mechanisms, such as homophily, using a novel test based on the empirical model. The empirical evidence supports a strong observational learning efect. We also find that the moderating role of the geographical locations of users and their friends on the magnitude of observational learning is critical. These findings suggest a nuanced view for local merchants to boost observational learning with the advancement of location-based technology.

History: Anindya Ghose, Senior Editor; Jefrey Hu, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2017.0769.

Keywords: observational learning • location-based service • social networks • homophily • social ties

## 1. Introduction

The most famous example of observational learning is the sequential decision model of Banerjee (1992) and Bikhchandani et al. (1992): People decide whether to dine at a restaurant by observing how many (anonymous) consumers are already in the restaurant. In current practice, however, more people are seeking friends’ recommendations on location-based social networking applications for decision making (e.g., Foursquare, Facebook Places, and Google<sup>+</sup>). These applications allow users to share their location information, called check-ins, with friends through GPS-equipped mobile devices (Wang et al. 2015, Lee et al. 2016). As technology evolves, emerging location-based services motivate us to rethink the classical theory of observational learning and upgrade it to a new version embedded with social and location features (Bichler et al. 2010).

The check-in information generated by people’s social networks adds an important new dimension to prior models on observational learning. People can observe the choices made by their Foursquare and Facebook friends without having to physically visit the restaurants to observe behaviors. As a result of these new technologies, a striking diference has emerged. In Banerjee’s (1992) story, people arrive at restaurants in a sequence and can observe and rationally interpret all of the choices made by the anonymous people before them; using location-based social networks, friends’ check-ins are precisely recorded and “pushed” to users in real time. By knowing the identity and preferences of the people who made the visits, users may derive more value from the information.

Observational learning is an informational explanation of the correlated behavior among friends: An individual’s decision is afected by the observation of friends’ choices because of their informational content (Cai et al. 2009). The efect of observational learning is complicated by several plausible confounding mechanisms. The first is the normative conformity efect (normative social influence). People may want to behave like their friends because they want to conform (e.g., peer pressure). Asch’s (1951) classical conformity experiments show that an individual’s own opinions are influenced by those of a majority group. The second mechanism is the homophily-driven difusion process described by Aral et al. (2009): Inherent similarities in friends’ personal (time-invariant) characteristics can also cause correlated friends’ choices. Unlike observational learning, these two confounding mechanisms are noninformational.

In the present study, we estimate a two-stage empirical model of location-based social networks in the restaurant industry: The first stage, awareness, means that friends’ check-ins lead uninformed consumers to discover a new restaurant. The second stage, observational learning, refers to the fact that check-ins made by friends help users learn about the quality of a restaurant.

Our contribution is threefold. First, we test for an observational learning efect. The intuition of our approach of identifying causal observational learning from other non-informational mechanisms (particularly homophily) is as follows (Iyengar et al. 2015): If we observe a sharp decline in the clustering of checkin behaviors among peers as consumers proceed from trial to repeat, it will be consistent with a significant observational learning efect in trials because personal dining experience (experienced information) substitutes for observational learning (observed information) from peers (Simonsohn et al. 2008). This approach can be used in future studies to identify causal informational social influence.

Second, we further examine important factors that can govern the magnitude of observational learning in the context of location-based technology. Prior work has focused on the moderating role of social ties on the efectiveness of word of mouth or observational learning: Strong ties are more influential than weak ties (Bakshy et al. 2012, Shi and Whinston 2013, Aral and Walker 2014, Liu et al. 2014). On the other hand, a recent stream of literature on mobile targeting showed the impact of location factors on mobile promotions (Luo et al. 2013, Fang et al. 2015, Andrews et al. 2015, Danaher et al. 2015). A unique feature of our context of location-based social networks is a combination of social network graphs and location information shared by users. The check-in location indicates the current geographical status of a user in the real world and reflects the user’s behavior more closely to the real world compared with other online social networks (Gao and Liu 2014, Wang et al. 2015): Consumers must be physically present for dining consumption.

What is not well understood is how the magnitude of observational learning is moderated by social ties as well as geographic locations. Combining social and location dimensions, we find that the impact of a friend’s mobile check-in at a restaurant on the likelihood of a focal consumer’s future visit critically depends on (1) the strength of the social ties between the focal consumer and the focal consumer’s friend, (2) whether the restaurant is in the focal consumer’s familiar/local region (distance to the restaurant), (3) whether the restaurant is in the consumer’s friend’s familiar/local region, and (4) whether the restaurant is part of a franchise or independent. To our knowledge, few studies have addressed the interaction efects among (1)–(3). Our findings suggest that, in the presence of a location-based network, the marketing strategies of local businesses should be contingent on social ties, as well as location factors. More generally, the observational learning interpretation provides a coherent explanation for the complex pattern of our findings on the moderating roles of social and location factors, whereas homophily and conformity behaviors do not.

Third, previous research has shown the impact of observational learning or word of mouth on new product adoption/single purchase (Duan et al. 2009, Zhang 2010, Zhu and Zhang 2010). However, having customers try a new product does not necessarily mean that local vendors can retain those customers or lead to repeat purchases. Marketing practice has often labeled consumers who repeatedly patronize a business as loyal. Our study contributes to the literature by examining the role of observational learning in trials and repeats in a unified empirical model. In the context of the acceptance of a risky prescription drug by physicians, Iyengar et al. (2015) demonstrated that peer influence is significant in trials and repeats. The authors interpreted this result as empirical evidence indicating that informational social influence dominates in trials while normative social influence dominates in repeats. Similarly, we find that observational learning (informational social influence) is strong in trials in the context of restaurant dining. Our results are robust and confirmed by estimation using instrumental variables (IVs) such as exogenous weather shocks.

## 2. Literature Review

## 2.1. Observational Learning and Herding

Herd behavior and information cascades have been widely studied in the literature (Banerjee 1992, Bikhchandani et al. 1992). In the canonical model of observational learning, agents make decisions sequentially after having observed their predecessors’ choices. In a sequential decision-making setup, at some point, people follow the decisions of their predecessors, regardless of their private information. In these models, people can observe and rationally interpret the decisions of all their predecessors. This assumption is inappropriate in location-based networks. People have limited attention and tend to be concerned about letting strangers know their whereabouts (Xu et al. 2012). Acemoglu et al. (2011) studied a theoretical observational learning model over a general social network. In their model, people observe only subsets of their predecessors. Zhang et al. (2015) examined observational learning in the networks of friends versus strangers in an analytical model. In our study, we empirically find that the efect of friends’ check-ins is much more important than strangers’ check-ins.

A handful of empirical papers have examined the mechanism of observational learning. Duan et al. (2009) demonstrated herd behavior and informational cascades in the context of online software adoption. Zhang (2010) studied observational learning in the U.S. kidney market. Chen et al. (2011) disentangled whether consumers’ purchase decisions can be influenced by others’ opinions (word of mouth) or actions (observational learning) using a natural experiment from Amazon. Simonsohn and Ariely (2008) and Zhang and Liu (2012) examined whether observational learning is rational in the contexts of eBay and a peer-to-peer lending market, respectively. Prior studies have also shown how product and consumer characteristics moderate the eficacy of observational learning or word of mouth (Zhu and Zhang 2010, Tucker and Zhang 2011, Lee and Raghu 2014). Zhu and Zhang (2010) found that word of mouth is more influential in afecting the sales of less popular games than the sales of more popular games. Tucker and Zhang (2011) showed that the efect of observational learning is stronger for niche products with narrow appeal. Wang et al. (2018) investigated social influence in online book ratings and found that social influence is stronger for older books and users who have smaller networks.

Our study is closely related to Shi and Whinston (2013), who also studied observation learning in the context of location-based networks. Our analysis differs from Shi and Whinston’s (2013) and other prior studies on observational learning in three aspects. First, most of the previous studies focused exclusively on single-purchase products (information goods), such as books, movies, music, and video games. Here, we examine new product adoption and repeat purchases in the context of the restaurant industry in a unified empirical model. Although Shi and Whinston (2013) examined observational learning in the same industry, they did not diferentiate between learning in trial and repeat.

Second, researchers often face the challenge of separating the causal efect of observational learning or social influence from homophily due to the endogenous nature of social tie formation (Manski 1993). Some identification strategies include the use of IVs (Shriver et al. 2013), natural experiments (Zhang and Wang 2012), matching methods (Aral et al. 2009, Wang et al. 2018), controlled laboratory experiments (Qiu et al. 2014), and field experiments (Aral and Walker 2011). Shi and Whinston (2013) applied the machine learning technique of non-negative matrix factorization (NMF) to uncover users’ latent features from the network graph and identify the causal efect. In this study, we propose a diferent identification method, i.e., a novel test based on an empirical trial and repeat model to separate observational learning from other non-informational mechanisms, such as homophily. As a robustness check, we also use the technique of IVs to account for correlated unobserved heterogeneity and confirm identification of the informational social influence.

Third, in social networks, the eficacy of observational learning or word of mouth depends on consumer and product characteristics, as well as the strength of social ties. Our location-based network ofers a new location dimension: The efect of observational learning from friends’ check-ins crucially depends on whether the check-ins are in the focal user’s local region or in the friends’ local regions. Prior literature (Zhu and Zhang 2010, Wang et al. 2018) focused on how consumer characteristics (e.g., Internet experience, users’ network size) and product characteristics (e.g., video game popularity) moderate the efect of word of mouth or peer influence. By contrast, our location dimension is a consumer product characteristic (irrespective of whether a restaurant is in a consumer’s familiar/local region). Unlike Shi and Whinston (2013), who focused on the moderating role of social ties, we examine how social and location factors moderate the magnitude of observational learning.

## 2.2. Mobile Targeting

Our work is also related to the literature on mobile advertising and mobile targeting. Cairncross (2001) proposed the idea of the “death of distance,” where the role of physical distance has been diminishing because of the communication revolution in the Internet era. However, Ghose et al. (2012a) found that stores in the vicinity of a user’s home are much more likely to be clicked on mobile phones. Luo et al. (2013) showed that consumers are more likely to redeem a mobile coupon if they are closer to the store. Distance can influence responses to mobile advertisements even within the confines of a shopping mall (Danaher et al. 2015). In the context of location-based social networks, our results suggest that distance matters in a diferent way: The magnitude of observational learning is greater when a restaurant is not in a focal consumer’s local region because the diner’s increased familiarity with the local restaurant through ofline word of mouth and other information sources may substitute for the efect of observational learning.

## 2.3. Research Framework

Figure 1 shows our research framework. Causal social influence and homophily can explain correlated friends’ choices (Aral et al. 2009, Aral and Walker 2011). Observational learning belongs to causal social influence: An individual’s decision is afected by the observation of friends’ choices. By contrast, homophily is a non-causal mechanism. Among diferent types of causal mechanisms, the normative conformity efect is a plausible confounding factor that can explain correlated friends’ choices. Unlike observational learning, normative conformity is a non-informational mechanism. Normative conformity occurs when one conforms to be liked or accepted by the members of a group (Mann 1969). This need for social approval and acceptance is part of our human state. Finally, observational learning and the awareness efect are informational causal mechanisms. Li and Wu (2013) explored how informational mechanisms afect shopping behaviors and sales of daily deals. Hendricks and Sorensen (2009) and Bjorkegren (2015) discussed how awareness afects the difusion process.

Figure 1. Research Framework  
![](/api/attachments/VYNGWKCU/fulltext/images/30ab4f8095604bc378b468875fd138e4835459b525795de8126287298d939b94.jpg)

The major purpose of our study is to separate observational learning from non-causal mechanisms, such as homophily, because homophily is a critical confounding factor. As highlighted by Aral et al. (2009), separating causal social influence from non-causal mechanisms is essential to the formulation of efective social contagion management policies. The success of viral marketing strategies depends on whether (and when) friends causally influence one another. Without separating causal social influence from non-causal mechanisms, we will overestimate the efectiveness of social contagion management policies and networkbased marketing.

## 3. Data

The data set is from a major location-based social networking application in China. Users can check in at a venue to say they are currently there (see Figure 2). The application also lets them connect with their online friends, which is equivalent to the concept of friends on Facebook. Users can observe their network friends check-ins through the mobile application.

Our data include restaurant check-in information and the users’ social network. The first part of the data consists of the consumer check-ins of 50 randomly selected restaurants in the “hot pot”<sup>1</sup> category in Shanghai, China. The check-in history period is from May 2010 to January 2013. We can observe who checked ${ \mathrm { i n } } ,$ when this person checked ${ \mathrm { i n } } ,$ and where. The application company randomly selected a total of 34,207 users in Shanghai. Figure 3 shows the frequency histograms of restaurant check-ins and unique restaurant customers. In our sample, about 67% of consumers made repeat check-ins at a restaurant and all restaurants had repeat visits from consumers. Therefore, repeat visits are common. In our study, we only have the check-in data, not the actual restaurant visit data. The other part of our data consists of an undirected social graph. The social network is recorded as of February 15, 2011. Table 1 summarizes the descriptive statistics of the location-based social network by user. It shows that, on average, each user has approximately four direct friends (the mean of the degree centrality is 4.375) and checks in 36 times during the entire sample period (almost three years). The calculations of the social network centrality measures reported in Table 1 are provided in Online Appendix A.

## 4. Efect of Friends’ Check-Ins: Reduced-Form Regressions

To establish the baseline relation between a focal user’s check-in behavior and the number of friends’ checkins, we start with a simple reduced-formed regression, $\mathrm { i . e . , }$ a linear probability model. The dependent variable, $C h e c k _ { i j } ,$ is a dummy variable indicating whether focal user i will check in at restaurant $j$ at least once during the sample period. The independent variable in which we are interested, $F C _ { i j } ,$ is the average number of friends’ check-ins per month at restaurant j before the focal user’s first-time check-in.

Figure 2. (Color online) A Screenshot of the Application Interface  
![](/api/attachments/VYNGWKCU/fulltext/images/873b5f42694a515c6158423f366ccbe80a9146e48b9d9114a76f3e8eeb727ccc.jpg)

![](/api/attachments/VYNGWKCU/fulltext/images/22e8876e7d2da173bb5d4c1c82e4a3cb860bd316b3f19e1d89a7f4db508740b0.jpg)  
Push Notification from a Friend

Figure 3. (Color online) Histograms of Check-Ins and the Number of Customers at Restaurants  
![](/api/attachments/VYNGWKCU/fulltext/images/9caf618d4f8651623a4326db8f337f0271bf6a5f217ae0e4c848273f7d0e45fb.jpg)  
Number of total check-ins at restaurants

![](/api/attachments/VYNGWKCU/fulltext/images/d1e9851c109d23a198122e86b674f645a23e01f803eefdfdf91e0396759bf9c6.jpg)  
Number of unique customers at restaurants

Table 1. Summary Statistics of the Location-Based Service Users

<table><tr><td></td><td>Mean</td><td>Std. dev.</td><td>Max.</td><td>Min.</td><td>Obs.</td></tr><tr><td>Degree centrality</td><td>4.375</td><td>9.578</td><td>566</td><td>0</td><td>34,207</td></tr><tr><td>Closeness centrality</td><td>4.57E-09</td><td>1.63E-09</td><td>5.92E-09</td><td>8.55E-10</td><td>34,207</td></tr><tr><td>Betweenness centrality</td><td>51,680.26</td><td>470,134.6</td><td>54,962,235</td><td>0</td><td>34,207</td></tr><tr><td>Individual clustering coefficient</td><td>0.0243</td><td>0.0474</td><td>0.229</td><td>0</td><td>34,207</td></tr><tr><td>Number of check-ins</td><td>35.920</td><td>8.149</td><td>817</td><td>0</td><td>34,207</td></tr><tr><td>Number of unique restaurants visited</td><td>3.257</td><td>1.559</td><td>22</td><td>0</td><td>34,207</td></tr></table>

Table 2. Efect of Friends’ Check-Ins on Focal Users: Reduced-Form Regressions

<table><tr><td>Variables</td><td>(1) Pooled ordinary least squares</td><td>(2) Fixed effects</td><td>(3) Logit model</td></tr><tr><td>FC</td><td>0.0427***[6.478]</td><td>0.0436***[7.472]</td><td>0.254***[6.235]</td></tr><tr><td>Social network centrality measures</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Restaurant dummies</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Constant</td><td>0.00173**[2.230]</td><td>0.00142**[2.342]</td><td>0.00126**[2.143]</td></tr><tr><td>Number of users</td><td>34,207</td><td>34,207</td><td>34,207</td></tr><tr><td>Number of restaurants</td><td>50</td><td>50</td><td>50</td></tr></table>

Note. Robust t-statistics or t-statistics are in brackets.  
p < 0.1; p < 0.05; p < 0.01,.

We estimate the following linear probability model using a pooled regression, controlling for individual heterogeneity using four social network measures of users, as described in Table 1, and for restaurant heterogeneity with 49 restaurant dummy variables:

$$
\begin{array}{r l} C h e c k _ {i j} & = \beta_ {0} + \beta_ {1} F C _ {i j} + \beta_ {2} D e g r e e _ {i} + \beta_ {3} C l o s e n e s s _ {i} \\ & \quad + \beta_ {4} B e t w e e n n e s s _ {i} + \beta_ {5} C l u s t e r i n g _ {i} \\ & \quad + R e s t a u r a n t D u m m i e s + \varepsilon_ {i j}. \end{array}\tag{1a}
$$

The regression results of Equation (1a) are shown in column (1) in Table 2. The coeficient of $F C _ { i j }$ is statistically and economically significant: A friend’s check-in will increase the focal user’s probability of checking in by 4.27%. The reduced-form regression shows a positive correlation between friends’ check-ins and a focal user’s check-in behavior.

We estimate the following fixed efects model including user fixed efects $\theta _ { i } \colon ^ { 2 }$

$$
C h e c k _ {i j} = \theta_ {i} + \beta_ {0} + \beta_ {1} F C _ {i j} + R e s t a u r a n t D u m m i e s + \varepsilon_ {i j}.\tag{1b}
$$

We present the estimation results of the fixed efects model in column (2) in Table 2. The estimation results of a logit model are reported in column (3). The results are consistent across diferent models.

## 5. Empirical Model of Learning in a Location-Based Network

In this section, we develop and estimate a twostage model of restaurant discovery and quality learning. Following Hendricks and Sorensen (2009) and Bjorkegren (2015), the probability of a consumer visiting a venue is the product of two probabilities, i.e., the probability that the consumer likes the venue conditional on discovering it and the probability that the consumer discovers the venue. Note that neither of these probabilities is directly observable in the data. We estimate them from the empirical model. We outline the sequence of events in period t as follows (the process proceeds similarly in period t <sup>+</sup> 1).

To formalize the awareness stage, let $Y _ { i j t }$ be a binary variable indicating whether a consumer i checks in at restaurant j in period t. In Stage 1, some uninformed consumers become aware of a restaurant j in period t. The awareness can come from two sources, i.e., (i) public information received from various sources outside the location-based social network (without using the check-in application, a consumer can still discover a new restaurant, e.g., by searching on Yelp, TripAdvisor, and other sources of public information) and (ii) friends’ check-ins from the location-based social network.

To model public information, let $p _ { j }$ denote the probability of receiving information on the existence of restaurant j from outside the location-based social network. This probability captures the fact that a focal consumer may be aware of a restaurant even if no friend has ever checked in at that restaurant. To outline the intuition of the identification, we can compare two restaurants, m and n. We then focus on consumers whose friends have not checked in at these restaurants. All else being equal, if focal consumers are more likely to check in at restaurant m than at restaurant $n , p _ { m }$ is likely to be greater than $p _ { n }$

To model the awareness efect from friends’ checkins, let $R _ { i j , t - 1 }$ denote the number of consumer i’s friends’ check-ins at restaurant j in period t <sup>−</sup> 1. Consumer i receives information on the existence of restaurant j and becomes aware of restaurant j from a friend’s check-in with probability $q _ { j }$ . In other words, if the number of consumer $i \prime \mathrm { s }$ friends’ check-ins at restaurant j in period t <sup>−</sup> 1 is one, consumer i pays attention to this check-in and becomes aware of restaurant j with probability $q _ { j }$ in period t. The probability $q _ { j } < 1$ captures the fact that a friend or several friends check in at a restaurant but the focal consumer does not pay attention and is still unaware of the restaurant. More generally, the number of consumer i’s friends’ check-ins at restaurant j in period t <sup>−</sup> 1 is $R _ { i j , t - 1 }$ . Therefore, the probability that consumer i does not pay attention to any of these check-ins in period t is $( 1 \bar { - } q _ { j } ) ^ { R _ { i j , t - 1 } }$ and the probability that consumer i receives information on the existence of restaurant j from at least one of these check-ins is $1 - ( 1 - q _ { j } ) ^ { R _ { i j , t - 1 } } . \stackrel { ? } { }$ 8

Then, we can combine public information with information from the location-based social network. The probability of not being informed about the existence of restaurant j within period t is $( 1 - p _ { j } ) ( 1 - q _ { j } ) ^ { R _ { i j , t - 1 } }$ Over time, the likelihood of being aware of the restaurant increases. The probability of not being informed about the existence of restaurant j until period t is

$$
\prod_ {m = 1} ^ {t - 1} (1 - p _ {j}) (1 - q _ {j}) ^ {R _ {i j m}} = (1 - p _ {j}) ^ {t - 1} (1 - q _ {j}) ^ {\sum_ {m = 1} ^ {t - 1} R _ {i j m}}.
$$

Therefore, consumer $i \prime \mathrm { s }$ probability of being aware of restaurant j until period t (the first stage awareness probability) is

$$
\operatorname * {P r} (D _ {i j t} = 1) = 1 - (1 - p _ {j}) ^ {t - 1} (1 - q _ {j}) ^ {\sum_ {m = 1} ^ {t - 1} R _ {i j m}},
$$

where $\textstyle \sum _ { m = 1 } ^ { t - 1 } R _ { i j m }$ is the number of cumulative check-ins from friends until period $t - 1$ . We find that the awareness probability $\bar { \mathrm { P r } } ( D _ { i j t } = 1 )$ strictly increases with the number of cumulative friends’ check-ins, $\textstyle \sum _ { m = 1 } ^ { t - 1 } R _ { i j m } ,$ but the marginal efect is decreasing

$$
\frac {\partial \operatorname* {P r} (D _ {i j t} = 1)}{\partial (\sum_ {m = 1} ^ {t - 1} R _ {i j m})} > 0, \quad \frac {\partial^ {2} \operatorname* {P r} (D _ {i j t} = 1)}{\partial (\sum_ {m = 1} ^ {t - 1} R _ {i j m}) \partial (\sum_ {m = 1} ^ {t - 1} R _ {i j m})} <   0.
$$

In other words, the awareness probability, $\mathrm { P r } ( D _ { i j t } = 1 )$ is concave in the number of cumulative friends’ checkins, $\textstyle \sum _ { m = 1 } ^ { t - 1 } R _ { i j m } ,$ , which is consistent with our intuition: Although the kth check-in $( k > 1 )$ can still increase the awareness probability, the magnitude is smaller than that of the first check-in in increasing the awareness probability.

In Stage 2, conditional on being aware of the restaurant, consumers make a decision on whether to go to this restaurant. The utility function for consumer i conditional on having learned the existence of venue j is

$$
\begin{array}{r l} & U _ {i j t} = \alpha_ {j} + \gamma_ {1} R _ {i j, t - 1} + \gamma_ {2} R _ {i j, t - 1} ^ {2} + \varphi_ {1} S _ {i j, t - 1} + \varphi_ {2} S _ {i j, t - 1} ^ {2} \\ & \qquad + \beta_ {j} V _ {i j, t - 1} + \delta_ {1} R _ {i j, t - 1} V _ {i j, t - 1} + \delta_ {2} R _ {i j, t - 1} ^ {2} V _ {i j, t - 1} \\ & \qquad + \rho_ {1} S _ {i j, t - 1} V _ {i j, t - 1} + \rho_ {2} S _ {i j, t - 1} ^ {2} V _ {i j, t - 1} + \boldsymbol {\Theta} \mathbf {M} _ {i} \\ & \qquad + \tau G _ {j t} + M o n t h _ {t} + \varepsilon_ {i j t}, \end{array}\tag{2}
$$

where $\varepsilon _ { i j t } \sim N ( 0 , \sigma ^ { 2 } ) ; V _ { i j , t - 1 } = 1$ if consumer i’s number of self check-ins at restaurant j until period $t - 1$ is at least one (consumer i has visited restaurant $j )$ and $V _ { i j , t - 1 } = 0$ otherwise; $R _ { i j , t - 1 }$ is the number of friends’ check-ins at venue j in period $t - 1 ; S _ { i j , t - 1 }$ is the number of strangers’ check-ins at venue j in period $t - 1 ; \mathbf { M } _ { i }$ is a vector of user i’s social network characteristics (observable individual characteristics), including the degree centrality, closeness centrality, betweenness centrality, and individual clustering coeficient summarized in Table 1; Θ is a rowvector representing the coeficients of social network characteristics; ${ M o } \bar { n } t h _ { t }$ is a set of monthly time dummies (where each time period is a month) and is used to control for seasonal trends.<sup>4</sup> If a consumer clicks on the restaurant page in the location-based app, the consumer can observe the number of anonymous strangers’ check-ins, which is why we want to add $S _ { i j , t - 1 }$ to our model specification. For each restaurant, we also collect its online review rating in period $t , G _ { j t } ,$ from China’s largest restaurant review site, Dianping.com,<sup>5</sup> to control for the efect of word of mouth. When leaving a restaurant review on Dianping, a user assigns a rating of one to five stars in whole-star increments. Dianping aggregates all of the reviews for a given restaurant and displays the average rating. The error term $\varepsilon _ { i j t }$ represents individual taste shock and is independent and identically distributed (i.i.d.).

In Equation (2), the conditional expected restaurant quality (the perceived quality of restaurant j before a customer actually visits it) is given by the following quadratic functional form:<sup>6</sup>

$$
\begin{array}{r l} & E (Q _ {j} \mid R _ {i j, t - 1}, S _ {i j, t - 1}) \\ & \quad = \alpha_ {j} + \gamma_ {1} R _ {i j, t - 1} + \gamma_ {2} R _ {i j, t - 1} ^ {2} + \varphi_ {1} S _ {i j, t - 1} + \varphi_ {2} S _ {i j, t - 1} ^ {2}, \end{array}\tag{3}
$$

where the parameter $\alpha _ { j }$ represents the heterogeneity of restaurants. The squared terms, $R _ { i j , t - 1 } ^ { 2 }$ and $S _ { i j , t - 1 } ^ { 2 } ,$ capture the fact that the impact of friends’ check-ins or strangers’ check-ins may not be linear. In Online Appendix C, we use a simple analytical model to illustrate why more friends’ check-ins can increase the focal user’s utility, but the marginal efect may be decreasing.

Because we use the binary variable $V _ { i j , t - 1 }$ to indicate whether a focal user has visited restaurant $j ,$ we can specify the utility function of the focal user in trials and repeats in one equation. Note that we care about the level of $\beta _ { j }$ rather than the level of $\alpha _ { j } .$ . The reason is that conditional on discovering the venue, if the utility of visiting restaurant j in period $t , U _ { i j t } ,$ , is greater than the reservation utility, consumer i will go to restaurant j in period t. In other words, consumer i compares $U _ { i j t }$ with the reservation utility U<sup>¯</sup> . This process is equivalent to comparing $U _ { i j t } + c$ (the actual utility plus a constant) with $\bar { U } + c$ (the reservation utility plus a constant). In our estimation, without loss of generality, we normalize the $\alpha _ { j }$ value of a randomly picked restaurant to be zero and thus pin down other restaurants’ $\alpha _ { j }$ values.

We include $\delta _ { 1 } R _ { i j , t - 1 } V _ { i j , t - 1 }$ and $\delta _ { 2 } R _ { i j , t - 1 } ^ { 2 } V _ { i j , t - 1 }$ in Equation (2) because we want to answer an important question: How do we causally separate the observational learning efect from non-informational mechanisms such as the conformity efect or correlated personal tastes (homophily)? According to Equation (2), the marginal impact of friends’ check-ins before having visited a restaurant is $\gamma _ { 1 } + 2 \gamma _ { 2 } R _ { i j , t - 1 }$ and the marginal impact of friends’ check-ins after having visited a restaurant is $\gamma _ { 1 } + \delta _ { 1 } + 2 ( \gamma _ { 2 } + \delta _ { 2 } ) R _ { i j , t - 1 }$ . We can separate observational learning from non-informational mechanisms by focusing on the diference between the marginal impact of friends’ check-ins before and after having visited a restaurant: $\gamma _ { 1 } + 2 \gamma _ { 2 } R _ { i j , t - 1 } - [ \gamma _ { 1 } + \delta _ { 1 } +$ $2 ( \gamma _ { 2 } + \bar { \delta } _ { 2 } ) R _ { i j , t - 1 } ] = - \delta _ { 1 } - 2 \delta _ { 2 } R _ { i j , t - 1 }$ . This diference quantifies the lower bound of the impact of observational learning. The intuition is as follows:

• Homophily. Our identification of observational learning from homophily relies on the static nature of the latent homophily efect versus the dynamic nature of the observational learning efect before and after a consumer has visited a restaurant. As summarized by Aral et al. (2009) and Ma et al. (2014), homophily is the intrinsic preference similarity between friends based on static (time-invariant) personal characteristics. Therefore, the efect of correlated tastes (homophily) should be relatively stable over time. If the impact of friends check-ins is driven purely by the homophily efect, we would expect to observe the diference, $- \delta _ { 1 } - 2 \delta _ { 2 } R _ { i j , t - 1 } ,$ to be very close to zero, because the efects of homophily should remain unchanged, regardless of whether consumer i has visited restaurant j.

• Normative conformity. As suggested by Iyengar et al. (2015), there is little theory or empirical research suggesting that susceptibility to normative conformity declines as customers proceed from trial to repeat. By contrast, a number of studies have shown that normative conformity is likely to be stronger in repeat decisions than in trial decisions (Tolbert and Zucker 1983). The underlying logic can also apply to our setting. In our context, normative conformity means that consumers may want to visit the same restaurant as their friends because they want to conform and discuss their dining experience at that restaurant in socia encounters. In other words, dining at the same restaurant brings people together around something. They can feel a sense of social belonging and acceptance among their social groups by showing that they visit the same restaurant. Conformity is used to improve their chances of being accepted by a social group. The reason normative conformity becomes stronger is that consumers’ desire to appear socially appropriate by conforming to normative expectations increases over the difusion process (Kennedy and Fiss 2009). Westphal et al. (1997, p. 374) argued that trial decisions are primarily based on a “logic of instrumentality,” such as the technical and performance considerations of products or services. However, as time progresses, repeat decisions are increasingly evaluated based on a “logic of social appropriateness.” This argument is also consistent with Maslow’s (1943) hierarchy of needs: As one feels that basic physical requirements for human survival are met, social belonging becomes a more important consideration. In our research set ting, when consumers make their trial decisions, they may care more about the logic of instrumentality, such as the quality of food. Considerations involving food (metabolic requirements for survival) are more important in this stage (a low level of need in Maslow’s hierarchy). As consumers proceed from trial to repeat, they consider social appropriateness and social needs more: They want to find something to talk about and seek feelings of social belonging by showing that they visit the same restaurants. In other words, after consumers’ first visit to a restaurant, they have tasted the food there and their basic physical requirements are somewhat met. According to Maslow’s hierarchy of needs and Westphal et al. (1997), consumers then focus more on the emotional need to be an accepted member of a group. They conform to their friends to be more liked by their social group. Therefore, if the impact of friends’ check-ins is purely driven by the efect of normative conformity, we should observe the diference $- \delta _ { 1 } - 2 \delta _ { 2 } R _ { i j , t - 1 } \leq \dot { 0 } .$

• Observational learning. If the impact of friends’ check-ins is mainly driven by the efect of observational learning, we would expect to observe the difference $- \delta _ { 1 } - 2 \delta _ { 2 } R _ { i j , t - 1 } > 0 \colon$ After a consumer has visited a restaurant, the consumer should rely less on friends’ check-ins to infer the restaurant quality. In other words, when a consumer has a better knowledge of the restaurant (personal dining experience), observational learning becomes less important. Simonsohn et al. (2008) examined the diferent roles of experienced information (information obtained through direct personal experience) and observed information (information obtained by observing the experience of others) and found that people’s actions are influenced more strongly by experienced information than by observed information. In our context, when experienced information and observed information are available to a focal consumer after the first visit, the consumer should rely more on direct experience and less on friends’ check-ins. In other words, we can test the following hypotheses:

H0. Observational learning does not exist $( - \delta _ { 1 } - 2 \delta _ { 2 }$ $R _ { i j , t - 1 } \leq 0 )$

H1. Observational learning exists $( - \delta _ { 1 } - 2 \delta _ { 2 } \cdot R _ { i j , t - 1 } > 0 )$

More generally, the impact of friends’ check-ins may include the observational learning efect, the homophily efect, and normative conformity. When we consider the diference between the marginal impact of friends’ check-ins before having visited a restaurant and after having visited a restaurant, the homophily efect tends to be canceled out.

One could argue that a consumer may not be completely sure about the true restaurant quality after one visit. Actually, our test does not require that a single visit completely inform a consumer of the true quality. A consumer can still learn quality information from friends’ check-ins after having visited the restaurant, but the learning efect should be much weaker because the consumer’s personal dining experience in the restaurant substitutes for observational learning from peers. In other words, as long as a consumer knows more about the restaurant’s quality after a visit, the efect of observational learning should decline as the consumer proceeds from trial to repeat. In addition, the exact magnitude of the impact of friends’ check-ins (before and after) could depend on how we model the impact of friends’ check-ins in a specific functional form. However, the diference between the before and after efects should be less sensitive to the choice of functional forms. The reason is that, if a specific functional form tends to overestimate (or underestimate) the impact of friends’ check-ins, it tends to consistently overestimate (or underestimate) the impact before and after the focal consumer’s first visit. When we take the diference between the before and after impacts into account, the bias is likely to be canceled out and the diference itself will be less sensitive to specific functional forms. Therefore, our identification does not critically depend on how we model the impact of friends’ check-ins in a specific functional form. Note also that homophily could cause an endogeneity problem in the estimation, which we discuss in Section $^ { 6 , }$ using IVs.

One might also wonder whether our identification of observational learning could be confounded by other plausible mechanisms, such as common exogenous shocks, as proposed by Manski (1993). In our context of restaurant dining, an example of common exogenous shocks is that customers may be exposed to the same advertisements, promotions or coupons ofered by a restaurant. If the main driver for the impact of friends’ check-ins is a common exogenous shock shared by all customers of restaurant $j ,$ we should observe a positive correlation between friends’ dining decisions, as well as a positive correlation between anonymous people’s dining decisions. If the impact of anonymous people’s check-ins is not statistically diferent from zero, the empirical evidence suggests that common exogenous shocks might not be the reason for a positive impact of friends’ check-ins.

Conditional on discovering the venue, if the utility of visiting restaurant j in period $t , U _ { i j t . }$ , is greater than the reservation utility, consumer i will go to restaurant j in period t. We assume that the focal users’ check-ins are a proxy for their dining out at restaurants. The probability that consumer i visits venue j in period t conditional on discovering it is given by Pr $[ \hat { U } _ { i j t } \ge \bar { U } ]$ . The probability that a consumer visits a venue j in period t is the product of two probabilities, i.e., $\begin{array} { r } { \dot { \mathrm { P r } } ( D _ { i j t } = 1 ) } \end{array}$ $\operatorname* { P r } [ U _ { i j t } \geq \bar { U } ]$ . Without loss of generality, the reservation utility U<sup>¯</sup> is normalized to zero. We construct the loglikelihood function to estimate the empirical model

$$
\begin{array}{l} \ln L (\theta) = \ln \prod_ {t = 1} ^ {T} \prod_ {j = 1} ^ {J} \prod_ {i = 1} ^ {N} [ \operatorname * {P r} (D _ {i j t} = 1) \cdot \operatorname * {P r} (U _ {i j t} \geq 0) ] ^ {\mathcal {Y} _ {i j t}} \\ \quad \cdot [ 1 - \operatorname * {P r} (D _ {i j t} = 1) \cdot \operatorname * {P r} (U _ {i j t} \geq 0) ] ^ {1 - \mathcal {Y} _ {i j t}} \\ = \sum_ {t = 1} ^ {T} \sum_ {j = 1} ^ {J} \sum_ {i = 1} ^ {N} \left[ Y _ {i j t} \ln \frac {\operatorname * {P r} (D _ {i j t} = 1) \cdot \operatorname * {P r} (U _ {i j t} \geq 0)}{1 - \operatorname * {P r} (D _ {i j t} = 1) \cdot \operatorname * {P r} (U _ {i j t} \geq 0)} + \ln (1 - \operatorname * {P r} (D _ {i j t} = 1) \cdot \operatorname * {P r} (U _ {i j t} \geq 0)) \right], \end{array} \tag {4}
$$

where $Y _ { i j t }$ is an indicator for whether consumer i checks in at venue j in period t from the data. In the estimation model, we use one month as the time unit of analysis, T is the number of time periods $( T = 3 2 )$ J is the number of venues $\left( J = 5 0 \right)$ , and N is the number of consumers $( N = 3 4 , 2 0 7 )$ . Note that, if $Y _ { i j t } = 1 _ { \ast }$ then $\mathrm { P r } ( D _ { i j m } = 1 ) = 1$ , for $m = t + 1 , \ldots , T$ . Note also that we are not using the standard discrete choice model and are treating the choice to visit each restaurant separately and independently. There are two reasons for this. First, our time unit of analysis is one month, and a consumer could visit several diferent restaurants in a month. Our data confirm that the choices are not mutually exclusive when the time unit of analysis is a month. Second, this simplified assumption can significantly reduce the computational burden when we face a large number of consumers and a large choice set.

Our estimates of the parameters are chosen to satisfy

$$
\arg \max (\ln L (\theta)).\tag{5}
$$

Note that we normalize the variance of individual taste heterogeneity $\sigma ^ { 2 }$ to be one and estimate others as free parameters. In constructing our log-likelihood function, we assume that $\varepsilon _ { i j t }$ is i.i.d. We relax this assumption and model that consumer i’s visit decisions could be correlated over time in Online Appendix G and the estimation results are similar. The detailed estimation procedure and counterfactual analyses are presented in Online Appendix K.

## 6. Empirical Results

## 6.1. Main Results from the Empirical Model

In this section, we present the empirical results estimated from Equation (5). In the main model (column (1) of Table 3), we find that $\delta _ { 1 }$ and $\delta _ { 2 }$ are negative and, in particular, $\delta _ { 1 }$ is statistically significant. Moreover, the number of friends’ check-ins at a restaurant in a time period, $R _ { i j , t - 1 } ,$ is fewer than 10 in our data. Therefore, we can reject the null hypothesis that observational learning does not exist; the diference between the marginal impact of friends’ check-ins before and after having visited a restaurant, $- \delta _ { 1 } - 2 \delta _ { 2 } R _ { i j , t - 1 } ,$ is significantly positive (p value $< 0 . 0 1 )$ , which supports a strong observational learning efect.

We also find that the coeficients of strangers’ checkins, $\varphi _ { 1 }$ and $\varphi _ { 2 } ,$ , are not statistically significant. As argued in Section 5, an insignificant efect of strangers’ check-ins suggests that common exogenous shocks, such as advertisements, promotions, and coupons, may not be the main driver of the impact of friends’ checkins. Considering the size of the coeficients, the efect of a friend’s check-in is much stronger than that of a stranger’s check-in. The main insight of Banerjee’s (1992) observational learning model is that check-ins made by strangers can convey quality. However, Lee et al. (2015) showed the diferential impacts of prior ratings by strangers versus friends in the context of online movie ratings. Our empirical results suggest that strangers’ check-ins may not be as important as friends’ check-ins in determining the expected quality of restaurants. Note that other factors could contribute to our result that the impact of friends’ check-ins is much larger. For instance, friends’ check-ins are automatically pushed to the focal consumer (the focal user will receive a push notification) but strangers’ check-ins can only be observed when the focal consumer looks at the restaurant’s page in the application.

Table 3. Efect of Observational Learning

<table><tr><td></td><td>(1)Main model</td><td>(2)IV (I)</td><td>(3)IV (II)</td></tr><tr><td> $\gamma_1$ </td><td>0.792**[4.215]</td><td>0.684**[3.842]</td><td>0.677**[3.655]</td></tr><tr><td> $\gamma_2$ </td><td>-0.0227**[2.146]</td><td>-0.0215**[2.125]</td><td>-0.0223**[2.227]</td></tr><tr><td> $\delta_1$ </td><td>-0.606**[3.544]</td><td>-0.485**[3.227]</td><td>-0.537**[3.287]</td></tr><tr><td> $\delta_2$ </td><td>-0.0105*[1.824]</td><td>-0.0113*[1.794]</td><td>-0.0133*[1.887]</td></tr><tr><td> $\varphi_1$ </td><td>0.00413[0.526]</td><td>0.00338[0.447]</td><td>0.00429[0.718]</td></tr><tr><td> $\varphi_2$ </td><td>-1.52e-05[0.147]</td><td>-2.84e-05[0.230]</td><td>-2.66e-05[0.285]</td></tr><tr><td> $\rho_1$ </td><td>-0.00232[0.541]</td><td>-0.00139[0.336]</td><td>-0.00314[0.711]</td></tr><tr><td> $\rho_2$ </td><td>-1.15e-05[0.158]</td><td>-1.24e-05[0.112]</td><td>-1.35e-05[0.108]</td></tr><tr><td> $\tau$ </td><td>0.216**[3.128]</td><td>0.238**[3.254]</td><td>0.266**[3.428]</td></tr><tr><td> $\mathbf{M}_i$ </td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Monthly dummies</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes. In IV (I), the IV is weather; in IV (II), the IV is friends’ friends’ check-ins. z-statistics or t-statistics are in brackets.  
p < 0.1; p < 0.05; p < 0.01.

As in many other empirical applications that use online social network data, we have only one snapshot of the network graph. To address this concern, we re-estimate our model using diferent time frames in Online Appendix D and the results are consistent with our main results. In Equation (2), we also assume that consumers stop learning after having visited a restaurant once. However, in reality, consumers may keep learning about a restaurant’s quality based on multiple visits. In Online Appendix I, we incorporate consumer learning after multiple visits and find that consumers keep learning after multiple visits but that the marginal efect from friends’ check-ins decreases with the number of visits.

## 6.2. Robustness Checks

6.2.1. IV I: Weather Shocks. Identifying a causal observational learning efect from archival data is challenging. The main confounding mechanism discussed in the literature is homophily because it highlights whether a mechanism is causal (Aral et al. 2009, Wang et al. 2018). In Section 5, we formulated a test on the basis of observational learning in trials and repeats in a unified empirical model, which allows us to separate the learning efect from latent homophily. However, one could wonder whether the identification mainly comes from the empirical model specifications. We conduct various robustness checks using the method of IVs to further alleviate the endogeneity concerns caused by the correlated unobserved friends’ intrinsic preferences or common exogenous shocks (such as targeted promotion eforts on the firm’s side).

Following the prior literature on weather instruments (Moretti 2011), our empirical strategy is to instrument for the number of friends’ check-ins made at restaurant j in period $t - 1 , R _ { i j , t - 1 } ,$ in Equation (2) with exogenous weather shocks in period t <sup>−</sup> 1 (month). Using weather as an instrument is plausible in our context because weather is an exogenous source of variation, which can avoid many possible confounders. The intuition is that severe weather (heavy rain, heavy snow, etc.) in period t <sup>−</sup> 1 can significantly reduce consumers’ willingness to dine out in period t <sup>−</sup> 1, considering that public transportation and cycling are still the most important travel modes in Shanghai.<sup>7</sup> Therefore, severe weather shocks in period t <sup>−</sup> 1 are negatively correlated with friend’s check-ins in that time period, $R _ { i j , t - 1 }$ . On the other hand, conditional on monthly time dummies, the weather shocks in month t <sup>−</sup> 1 should not directly afect a focal consumer’s willingness to visit restaurant j in month t, except through $R _ { i j , t - 1 } .$ . In our context, the exclusion restriction is plausible: Weather shocks in period t <sup>−</sup> 1 should afect our dependent variable, whether to check in at restaurant j in period t, only indirectly, through correlation with $R _ { i j , t - 1 }$ . A typical endogeneity in our context is that correlated friends’ intrinsic preferences or common exogenous shocks (two friends could receive the same ofer from a restaurant) are captured in the error term $\varepsilon _ { i j t }$ . Therefore, friends’ error terms tend to be correlated and we could observe a spurious correlation between friends’ check-ins (the number of the focal consumer’s friends’ check-ins, $R _ { i j , t - 1 } ,$ could be correlated with the error term $\boldsymbol { \varepsilon } _ { i j t } )$ . Using weather shocks as instruments for $R _ { i j , t - 1 }$ can alleviate this concern because exogenous weather shocks in month t <sup>−</sup>1 should not be correlated with the error term in month $t , \varepsilon _ { i j t } ,$ , conditional on the monthly time dummies.

A potential weakness of our weather instruments is autocorrelations in weather: The weather in period t <sup>−</sup> 1 could be correlated with the weather in period t. To account for these autocorrelations, we control for monthly dummies, Month , in our model. In Tucker (2008), exogenous shocks to the benefits of watching

TV are used as instruments to identify the causal social efects in video messaging technology. Similarly, we use exogenous weather variations in the sample period (32 months) to identify observational learning in our context.

Although weather instruments are widely used in the literature (Moretti 2011), an efective weather instrument should be constructed with care in our context. We obtain daily weather data in Shanghai from tianqi.com, a public weather website in China, and focus on weather measures such as the minimum and maximum temperatures, precipitation, and snowfall to characterize four severe weather events for each day, i.e., a cold day, a hot day, a heavy rainy day, and a heavy snow day. We define a day as cold or hot if the minimum temperature that day is below 0 C (32 F) or the maximum temperature is above 35<sup>◦</sup>C (95<sup>◦</sup>F), respectively, and we define a day as heavily rainy or snowy if the precipitation rate is greater than 4 mm/hour or 4 cm/hour, respectively. Then, we calculate the number of severe weather days in each time period (month) and construct four weather instruments, i.e., $C o l d _ { t - 1 } , H o t _ { t - 1 } , R a i n _ { t - 1 } ,$ and $S n o w _ { t - 1 }$ . We also test whether our four weather measures are weak instruments by calculating the firststage F-statistic. A high F-statistic (34.68) suggests that the weather shocks are not weak instruments. The estimation results using weather instruments are shown in column (2) of Table 3 and the first-stage regression results are reported in Table 4. The findings are consistent with our previous results and suggest a significant efect of observational learning. In Online Appendix H, we vary the definitions of our weather instruments and the results are also consistent with our previous results.

6.2.2. IV II: Check-Ins of Friends’ Friends. Following Bramoullé et al. (2009), we use friends’ friends’ checkin behaviors as an IV to make a causal inference. In essence, we are using the fact that a user in our location-based social network is not always friends with all of her friends’ friends. The intuition behind this IV is that the check-in actions of friends’ friends who are not the focal user’s friends can only have an indirect impact on the focal user’s future visit by influencing the check-in actions of the user’s friends. For example, consider a simple three-person network where our focal user is person A. Person B is a friend of person A and person C is a friend of person B but C and A are not friends. We use person C’s checkin behavior as an IV for person B’s check-in behavior. Two assumptions must hold for this instrument to be valid: (1) Person B’s and person C’s check-in decisions are correlated. (2) Person A’s check-in action is not influenced by indirect friend person C, except through direct friend person B. Assumption (1) holds because B and C are friends. A high first-stage F-statistic (24.85) suggests that the instrument is not weak. More important, we argue that assumption (2) is reasonable in our context. Person C is not a friend of person A and, from our previous empirical results, we know that the focal user’s check-in decision is not significantly influenced by strangers’ check-ins. In this case, person C’s checkin behavior can be viewed as an exogenous variation that facilitates our identification. More specifically, in Equation (2), we use the average number of check-ins of user i’s friends’ friends who are not user i’s friends made at restaurant j in period t <sup>−</sup> 2 as an instrument of user i’s friends’ check-ins in period $t - 1 , R _ { i j , t - 1 } .$ . The estimation results are shown in column (3) of Table 4 and suggest a robust efect of observational learning.

Table 4. First-Stage Regression Results: Weather Instruments

<table><tr><td>Variables</td><td>(1)IV weather</td></tr><tr><td>Cold</td><td>-0.0431**[2.218]</td></tr><tr><td>Hot</td><td>-0.0215**[2.035]</td></tr><tr><td>Rain</td><td>-0.112***[2.842]</td></tr><tr><td>Snow</td><td>-0.254***[3.232]</td></tr><tr><td colspan="2">First-stage F-statistic = 34.68</td></tr></table>

Note. t-statistics are in brackets.  
<sup>∗</sup> p < 0.1; <sup>∗∗</sup> p < 0.05; <sup>∗∗∗</sup> p < 0.01.

A potential concern of using friends’ friends’ checkin behaviors as an IV is that if focal user i has too many friends in common with her friend’s friend k, we could suspect that they are socially close and have similar intrinsic preferences. Therefore, we consider only user i’s friends’ friends who have a small number of friends in common with user i and conduct additional robustness checks using the average number of checkins of user i’s friends’ friends who are not user i’s friends and have fewer than or as many as x friends in common with user i, where x <sup></sup> 1, 3, 5. The results are robust and can be found in Online Appendix B.

In Online Appendix H, we add a robustness check on another IV, i.e., friends’ birthdays. Following Ke and Yang (2016), we use a focal consumer’s friends’ birthdays as an IV for friends’ check-ins and examine how these birthday-induced check-ins by the focal consumer’s friends afect her own visit (check-in) decisions. More specifically, our empirical strategy is to instrument for the number of friends’ check-ins made at restaurant j in period $t - 1 , R _ { i j , t - 1 } ,$ with the number of consumer i’s friends who have their birthdays in month t <sup>−</sup> 1. The basic idea is that it is more likely for people to dine out on or around their birthdays to celebrate. Therefore, we expect to see a larger number of friends’ check-ins around friends’ birthdays. The detailed estimation results are reported in Online Appendix H.

6.2.3. Heckman-Type Model for Self-Selection Bias. A potential concern is that users with certain characteristics are more likely to register for location-based applications. We consider a Heckman-type model in Online Appendix E to account for possible self-selection biases. For instance, younger people may be more likely to register for the application and then post mobile check-ins. Older people may physically visit the restaurant but not leave mobile check-ins because they have not registered for the application.

6.2.4. Random Coeficients Specification Using a random coeficients specification (Erdem et al. 2008), we allow the efect of observational learning to be heterogeneous across consumers. The estimation procedure and results can be found in Online Appendix B.

6.2.5. NMF. Following Ma et al. (2008), Takács et al. (2009), and Shi and Whinston (2013), we conduct an additional robustness check to control for individuallevel “latent factors” by deploying the method of NMF. Using this method, we can further address concerns about the endogeneity problem caused by unobserved individual heterogeneity. Matrix factorization-based techniques have been widely used in designing collaborative filtering algorithms for large recommendation systems (Takács et al. 2009). The intuition of the NMF method in our context is that consumers’ tastes and their underlying social network are simultaneously determined by some hidden lower-dimensional feature space. By factorizing the social network matrix, we can identify the most descriptive individual characteristics. The detailed estimation procedure and results are provided in Online Appendix B.

## 7. Important Factors Governing the Magnitude of Observational Learning

The role of social ties has been extensively examined in the literature (Shriver et al. 2013, Bapna et al. 2017, Hong et al. 2018). In our social networks, we add a new dimension, location, and examine how social and location factors together moderate the eficacy of observational learning. In particular, we use the “coherent pattern matching” approach (Shadish et al. 2002, p. 105) to demonstrate that our results are more likely to be driven by observational learning than by other confounding factors. Shadish et al. (2002, p. 105) pointed out that “the more complex the pattern that is successfully predicted, the less likely it is that alternative explanations could generate the same pattern, and so the more likely it is that the treatment had a real efect.” Essentially, our observational learning interpretation provides a coherent explanation for the complex pattern of our findings on the moderating roles of social and location factors, whereas other confounding factors do not.

## 7.1. Moderating Efect of Social Ties

The strand of research on social ties originates from the “strength of weak ties” hypothesis proposed by Granovetter (1973, p. 1360). The gist of the hypothesis is that we always obtain truly new information from acquaintances rather than from our close friends. The groups with whom we have strong ties, although they are filled with people eager to help, are also filled with people who know roughly the same things we do. Thus, strong ties usually result in informational redundancy. Weak ties, meanwhile, are much more valuable in terms of contributing genuinely new information. However, when we consider observational learning in location-based social networks, our estimation shows the strength of strong ties: Strong ties are more likely to be activated for observational learning. In other words, a closer friend’s check-in would play a more important role in the focal consumer’s decision making. Note that, in our study, we focus on the efect of tie strength on observational learning instead of on knowledge spillover. The strength of social ties between consumer i and the consumer’s friend, consumer j, is measured by the number of their common friends adjusted by the number of consumers who are friends of consumer i or consumer j, or, more formally,

$$
s _ {i j} = s _ {j i} = \frac {G (i) \cap G (j)}{G (i) \cup G (j)},\tag{6}
$$

where G<sup>(</sup>i<sup>)</sup> represents the set of friends of consumer i. This measure is widely used in the literature (Shi and Whinston 2013). We divide a consumer’s friends into two equally sized groups, depending on the tie strength: The group of close friends includes consumer i’s friends who are the 50% with the highest level of $s _ { i j }$ . Those remaining are the group of ordinary friends. Let C<sup>(</sup>i<sup>)</sup> represent the set of close friends of consumer i and let O<sup>(</sup>i<sup>)</sup> represent the set of ordinary friends of consumer i.

We modify the empirical model to investigate the role that tie strength plays in the process of observational learning. The awareness stage remains unchanged and we focus on the observational learning stage. Equation (2) is modified as follows:

$$
\begin{array}{l} U _ {i j t} = \alpha_ {j} + \gamma_ {\mathrm{C} 1} R _ {i j, t - 1} ^ {c} + \gamma_ {\mathrm{C} 2} (R _ {i j, t - 1} ^ {c}) ^ {2} + \gamma_ {\mathrm{O} 1} R _ {i j, t - 1} ^ {o} \\ \quad + \gamma_ {\mathrm{O} 2} (R _ {i j, t - 1} ^ {o}) ^ {2} + \varphi_ {1} S _ {i j, t - 1} + \varphi_ {2} (S _ {i j, t - 1}) ^ {2} + \beta_ {j} V _ {i j, t - 1} \\ \quad + \delta_ {\mathrm{C} 1} R _ {i j, t - 1} ^ {c} V _ {i j, t - 1} + \delta_ {\mathrm{C} 2} (R _ {i j, t - 1} ^ {c}) ^ {2} V _ {i j, t - 1} \\ \quad + \delta_ {\mathrm{O} 1} R _ {i j, t - 1} ^ {O} V _ {i j, t - 1} + \delta_ {\mathrm{O} 2} (R _ {i j, t - 1} ^ {O}) ^ {2} V _ {i j, t - 1} \\ \quad + \rho_ {1} S _ {i j, t - 1} V _ {i j, t - 1} + \rho_ {2} (S _ {i j, t - 1}) ^ {2} V _ {i j, t - 1} + \Theta \mathbf {M} _ {i} \\ \quad + \tau G _ {j t} + M o n t h _ {t} + \varepsilon_ {i j t}, \end{array} \tag {7}
$$

where $R _ { i j , t - 1 } ^ { c }$ is the number of close friends’ checkins at venue j in time period t <sup>−</sup> 1 and $R _ { i j , t - 1 } ^ { o }$ is the number of ordinary friends’ check-ins at venue $j$ in period $t - 1$ . From column (1) in Table 5, we find that $\bar { | } \delta _ { C 1 } + 2 \delta _ { C 2 } R _ { i j , t - 1 } ^ { c } |$ is significantly greater than $\lvert \delta _ { O 1 } +$ $2 \delta _ { O 2 } R _ { i j , t - 1 } ^ { O } | { \mathrm { i f } } \stackrel { \cdot \cdot } { R } R _ { i j , t - 1 } ^ { c } = R _ { i j , t - 1 } ^ { O } ,$ which suggests that strong ties can accelerate observational learning.

Table 5. Important Factors Governing the Magnitude of Observational Learning

<table><tr><td></td><td>(1) Social ties</td><td>(2) Social + Focal user&#x27;s location</td><td>(3) Focal user&#x27;s location + Friends&#x27; location</td><td>(4) Franchise effect</td></tr><tr><td> $\delta_1$ </td><td></td><td></td><td></td><td>-0.914***[3.653]</td></tr><tr><td> $\xi_1$ </td><td></td><td></td><td></td><td>0.575***[3.027]</td></tr><tr><td> $\delta_2$ </td><td></td><td></td><td></td><td>0.0164**[2.186]</td></tr><tr><td> $\xi_2$ </td><td></td><td></td><td></td><td>0.00853[0.523]</td></tr><tr><td> $\phi_{L1}$ </td><td></td><td></td><td>0.543*[3.226]</td><td></td></tr><tr><td> $\phi_{NL1}$ </td><td></td><td></td><td>0.879***[3.331]</td><td></td></tr><tr><td> $\phi_{L2}$ </td><td></td><td></td><td>0.00813[0.217]</td><td></td></tr><tr><td> $\phi_{NL2}$ </td><td></td><td></td><td>0.00732[0.186]</td><td></td></tr><tr><td> $\delta_{C1}$ </td><td>-0.812***[4.054]</td><td>-0.937***[4.532]</td><td></td><td></td></tr><tr><td> $\delta_{O1}$ </td><td>-0.253***[3.127]</td><td>-0.287***[2.872]</td><td></td><td></td></tr><tr><td> $\delta_{C2}$ </td><td>-0.0112**[2.154]</td><td>-0.0131**[2.223]</td><td></td><td></td></tr><tr><td> $\delta_{O2}$ </td><td>-0.0104**[2.033]</td><td>-0.0118**[2.127]</td><td></td><td></td></tr><tr><td> $\delta_{L1}$ </td><td></td><td></td><td>-0.762***[4.115]</td><td></td></tr><tr><td> $\delta_{NL1}$ </td><td></td><td></td><td>-1.208***[4.227]</td><td></td></tr><tr><td> $\delta_{L2}$ </td><td></td><td></td><td>-0.0124***[4.352]</td><td></td></tr><tr><td> $\delta_{NL2}$ </td><td></td><td></td><td>-0.0463***[4.646]</td><td></td></tr><tr><td> $\kappa_{C1}$ </td><td></td><td>0.487***[3.165]</td><td></td><td></td></tr><tr><td> $\kappa_{O1}$ </td><td></td><td>0.132[0.543]</td><td></td><td></td></tr><tr><td> $\kappa_{C2}$ </td><td></td><td>0.0142[0.225]</td><td></td><td></td></tr><tr><td> $\kappa_{O2}$ </td><td></td><td>0.0127[0.148]</td><td></td><td></td></tr></table>

Note. z-statistics or t-statistics are in brackets.  
<sup>∗</sup> p < 0.1; <sup>∗∗</sup> p < 0.05; <sup>∗∗∗</sup> p < 0.01.

Our results are consistent with the findings of prior studies. Bakshy et al. (2012) found that strong ties are more influential than weak ties, using a field experiment on Facebook. In another field experiment, Aral and Walker (2014) showed that individuals have more influence on peers with whom they are more embedded; they experience a 0.6% increase in influence for each friend they share in common. The strength of strong ties is driven by the following mechanism: A recommendation from a close friend is more reliable than one from an acquaintance, who could have an incentive to mislead the focal consumer (Lee and Bell 2013). Close friends’ check-ins can be a more credible signal because of trust and reputation based on repeated interactions. Forman et al. (2008) showed that the identity and reputation of online review authors are often factored in when consumers make purchase decisions and evaluate the helpfulness of online reviews. Bapna et al. (2017) found that the level of trust increases with the strength of social ties.

## 7.2. Location, Location, Location

Most prior studies on mobile targeting focused on “geo-fencing,” i.e., targeting potential customers close to a store’s location, and documented the positive efect of a shorter store distance (Luo et al. 2013, Danaher et al. 2015). Other studies also showed that locationbased characteristics have a significant impact on consumer demand (Ghose et al. 2012b). However, Fong et al. (2015, p. 726) found that geo-fencing could cannibalize profits on infra-marginal sales and proposed that “geo-conquesting” (targeting customers in the vicinity of a competing store) could generate incremental sales without cannibalizing profits. In our context, a restaurant can be in a focal consumer’s familiar region or an unfamiliar region based on the distance to the restaurant. We expect that the magnitude of observation learning for the focal consumer is diferent when a friend checks in at a local restaurant in the focal consumer’s familiar region or at a non-local restaurant in an unfamiliar region. We define consumer i’s familiar region in period t as the zip code area in which this consumer has the largest number of check-ins until period t (Wang and Goh 2012).<sup>8</sup>

We modify Equation (7) to add a location dimension to our observational learning model of social ties, as follows:

$$
\begin{array}{l} U _ {i j t} = \alpha_ {j} + \gamma_ {C 1} R _ {i j, t - 1} ^ {c} + \gamma_ {C 2} (R _ {i j, t - 1} ^ {c}) ^ {2} + \gamma_ {O 1} R _ {i j, t - 1} ^ {o} \\ \quad + \gamma_ {O 2} (R _ {i j, t - 1} ^ {o}) ^ {2} + \varphi_ {1} S _ {i j, t - 1} + \varphi_ {2} (S _ {i j, t - 1}) ^ {2} + \beta_ {j} V _ {i j, t - 1} \\ \quad + (\delta_ {C 1} + \kappa_ {C 1} L _ {i j, t - 1}) R _ {i j, t - 1} ^ {c} V _ {i j, t - 1} + (\delta_ {C 2} + \kappa_ {C 2} L _ {i j, t - 1}) \\ \cdot (R _ {i j, t - 1} ^ {c}) ^ {2} V _ {i j, t - 1} + (\delta_ {O 1} + \kappa_ {O 1} L _ {i j, t - 1}) R _ {i j, t - 1} ^ {O} V _ {i j, t - 1} \\ \quad + (\delta_ {O 2} + \kappa_ {O 2} L _ {i j, t - 1}) (R _ {i j, t - 1} ^ {O}) ^ {2} V _ {i j, t - 1} \\ \quad + \rho_ {1} S _ {i j, t - 1} V _ {i j, t - 1} + \rho_ {2} (S _ {i j, t - 1}) ^ {2} V _ {i j, t - 1} + \Theta \mathbf {M} _ {i} \\ \quad + \tau G _ {j t} + M o n t h _ {t} + \varepsilon_ {i j t}, \end{array} \tag {8}
$$

where $L _ { i j , t - 1 }$ is a dummy variable that takes the value 1 if restaurant j is in consumer $i \prime \mathrm { s }$ familiar region $( \mathrm { i . e . , }$ local restaurant) in period t <sup>−</sup> 1 and zero otherwise. In column (2) of Table 5, we find that $| \delta _ { C 1 } + 2 \delta _ { C 2 } R _ { i j , t - 1 } ^ { c } |$ is significantly greater than $| \delta _ { O 1 } + 2 \delta _ { O 2 } R _ { i j , t - 1 } ^ { O } |$ when $R _ { i j , t - 1 } ^ { c } = R _ { i j , t - 1 } ^ { O } .$ . More interestingly, we also find that the parameter $\kappa _ { C 1 }$ is significantly greater than zero $( | \delta _ { C 1 } +$ $\begin{array} { r } { \dot { 2 } \delta _ { C 2 } R _ { i j , t - 1 } ^ { c } + \kappa _ { C 1 } + \bar { 2 } \kappa _ { C 2 } R _ { i j , t - 1 } ^ { c } \dot { | } < | \delta _ { C 1 } + 2 \delta _ { C 2 } R _ { i j , t - 1 } ^ { c } | ) } \end{array}$ and the parameters $\kappa _ { O 1 }$ and $\dot { \kappa } _ { O 2 }$ are not statistically diferent from zero. These estimation results show that the magnitude of observational learning crucially depends on social ties, as well as the location dimension (see Figure 4): (1) The magnitude of observational learning from a close friend’s check-in at the focal user’s local restaurant is significantly less than that from a close friend’s check-in at a non-local restaurant, and (2) the magnitude of observational learning from an ordinary friend’s check-in at a local restaurant is similar to that from an ordinary friend’s check-in at a nonlocal restaurant.

Figure 4. Moderating Role of Location and Social Ties on Observational Learning  
![](/api/attachments/VYNGWKCU/fulltext/images/9acfddc7d7822c5b12c2ade3986fb84ed4c16f5eda41b8bafd368384175f9d9a.jpg)

A possible explanation for our finding (1) is that a consumer has less quality uncertainty about local restaurants compared to non-local and that there is less need for the consumer to rely on observational learning from close friends. The underlying logic is that the ofline learning in a consumer’s familiar/local region can substitute for observational learning from friends’ check-ins. For instance, Fong et al. (2015) found that targeting consumers in the area of a retailer’s own location is less efective. Their explanation follows the same logic: A store could have many ways of reaching customers near its own location. Iyengar et al. (2011) showed that, when the uncertainty inherent in the adoption of a new drug is high, physicians are more likely to rely on the opinions and experiences of trusted peers in determining their adoption decisions. In our context, a consumer is more likely to rely on close friends’ check-ins when she decides whether to visit a non-local restaurant (the quality uncertainty is high). Our findings (1) and (2) show that the substitution efect of local information for observational learning is strong (weak) when social ties are strong (weak). We speculate that when restaurant quality becomes more uncertain, consumers will rely more on their trusted (strong-tie) friends’ check-ins because of social capital (Cook 2005). However, consumers often cannot fully determine their weak ties’ credibility in an online environment, so they are unlikely to rely heavily on their weak ties, even when quality uncertainty is high (Chatterjee 2001).

This unique feature of location-based social networks allows us to study a question that, to our knowledge, has not been addressed thus far in the literature: How is the magnitude of observational learning impacted by whether a restaurant is in a focal consumer’s friend’s familiar/local region? We present the following four cases for a focal user’s familiar/local region and the user’s friend’s familiar/local regions: (i) A restaurant is in the focal consumer’s familiar/local region and the friend’s familiar/local region; (ii) a restaurant is in the focal consumer’s familiar/local region but not in the friend’s familiar/local region; (iii) a restaurant is not in the focal consumer’s familiar/local region or in the friend’s familiar/local region; and (iv) a restaurant is not in the focal consumer’s familiar/local region or in the friend’s familiar/local region. Therefore, we modify Equation (8) as follows:

$$
\begin{array}{l} U _ {i j t} = \alpha_ {j} + \gamma_ {L 1} R _ {i j, t - 1} ^ {L} + \gamma_ {L 2} (R _ {i j, t - 1} ^ {L}) ^ {2} + \gamma_ {N L 1} R _ {i j, t - 1} ^ {N L} \\ \quad + \gamma_ {N L 2} (R _ {i j, t - 1} ^ {N L}) ^ {2} + \varphi_ {1} S _ {i j, t - 1} + \varphi_ {2} (S _ {i j, t - 1}) ^ {2} + \beta_ {j} V _ {i j, t - 1} \\ \quad + (\delta_ {L 1} + \phi_ {L 1} L _ {i j, t - 1}) R _ {i j, t - 1} ^ {L} V _ {i j, t - 1} + (\delta_ {L 2} + \phi_ {L 2} L _ {i j, t - 1}) \\ \quad \cdot (R _ {i j, t - 1} ^ {L}) ^ {2} V _ {i j, t - 1} + (\delta_ {N L 1} + \phi_ {N L 1} L _ {i j, t - 1}) R _ {i j, t - 1} ^ {N L} V _ {i j, t - 1} \\ \quad + (\delta_ {N L 2} + \phi_ {N L 2} L _ {i j, t - 1}) (R _ {i j, t - 1} ^ {N L}) ^ {2} V _ {i j, t - 1} \\ \quad + \rho_ {1} S _ {i j, t - 1} V _ {i j, t - 1} + \rho_ {2} (S _ {i j, t - 1}) ^ {2} V _ {i j, t - 1} + \Theta \mathbf {M} _ {i} \\ \quad + \tau G _ {j t} + M o n t h _ {t} + \varepsilon_ {i j t}, \end{array} \tag {9}
$$

where $R _ { i j , t - 1 } ^ { L }$ is the number of friends’ check-ins at restaurant j in time period t <sup>−</sup>1 if restaurant j is in these friends’ familiar/local regions and where $\dot { R } _ { i j , t - 1 } ^ { N L }$ is the number of friends’ check-ins at restaurant j in time period t <sup>−</sup> 1 if restaurant j is not in these friends’ familiar/local regions. The estimation results are shown in column (3) of Table 5. First, we find that the coeficients $\phi _ { L 1 }$ and $\phi _ { N L 1 }$ are significantly positive and the coeficients $\phi _ { L 2 }$ and $\phi _ { N L 2 }$ are not statistically significant. These results confirm the substitution efect of local information for observational learning. Additionally, we find that $\delta _ { L 1 } , \delta _ { L 2 } , \delta _ { N L 1 } ,$ , and $\delta _ { N L 2 }$ are significantly negative, which suggests observational learning. More interestingly, $| \delta _ { N L 1 } |$ is significantly greater than $| \delta _ { L 1 } |$ and $| \delta _ { N L 2 } |$ is significantly greater than $| \delta _ { L 2 } |$ . This surprising result implies that the magnitude of observational learning is larger if a focal user’s friend checks in at a restaurant that is not in the focal user’s familiar/local region. The underlying intuition is a signaling efect: Visiting a restaurant that is not in the familiar/local region normally incurs a higher transportation/search cost. A friend’s check-in at a non-local restaurant means that she bears a higher cost but still chooses to go to this restaurant. Therefore, the check-in more strongly signals that the quality of the restaurant is high. Summarizing all of the coeficients, we conclude that the magnitude of observational learning for the four cases is as follows: $\mathrm { ( i v ) > ( i i i ) > ( i i ) > ( i ) }$

## 7.3. Moderating Efect of Franchise Restaurants

The moderating role of restaurant characteristics provides additional tests to help separate observational learning from normative conformity and awareness efect. In the context of peer-to-peer lending, Zhang and Liu (2012) distinguished between rational herding (observational learning) and irrational herding (blindly following others’ actions) by investigating whether the learning/herding efect is moderated by observable listing attributes of borrowers. If lenders are blindly following others’ investment decisions (normative conformity) or are drawn by the awareness efect, they tend to ignore auxiliary listing characteristics. By contrast, if lenders are rational observational learners, the inferences they draw from existing funding should depend on listing attributes. Similarly, Simonsohn and Ariely (2008) found that irrational eBay bidders herd into auctions with many existing bids but ignore the fact that it may have been lower starting prices that attracted these bids. Following Zhang and Liu’s (2012) approach, we also look at whether the learning/herding efect is moderated by observable restaurant characteristics, such as whether the restaurant is part of a franchise. If consumers are blindly following their friends’ check-ins or are drawn in by the awareness efect, they tend to ignore the information in restaurant characteristics. However, empirically, we find consumers do care about whether a restaurant is part of a franchise.

In our data, we have two types of restaurants, i.e., franchise restaurants (branded chain stores) and independent, local restaurants. We find that the efect of observational learning in a chain restaurant is much weaker for consumers who have already checked in at another restaurant in the same chain. We modify Equation (2) as follows:

$$
\begin{array}{l} U _ {i j t} = \alpha_ {j} + \gamma_ {1} R _ {i j, t - 1} + \gamma_ {2} (R _ {i j, t - 1}) ^ {2} + \varphi_ {1} S _ {i j, t - 1} + \varphi_ {2} (S _ {i j, t - 1}) ^ {2} \\ \quad + \beta_ {j} V _ {i j, t - 1} + \delta_ {1} R _ {i j, t - 1} V _ {i j, t - 1} + \delta_ {2} (R _ {i j, t - 1}) ^ {2} V _ {i j, t - 1} \\ \quad + \xi_ {1} C _ {i j, t - 1} R _ {i j, t - 1} V _ {i j, t - 1} + \xi_ {2} C _ {i j, t - 1} (R _ {i j, t - 1}) ^ {2} V _ {i j, t - 1} \\ \quad + \rho_ {1} S _ {i j, t - 1} V _ {i j, t - 1} + \rho_ {2} (S _ {i j, t - 1}) ^ {2} V _ {i j, t - 1} + \Theta \mathbf {M} _ {i} \\ \quad + \tau G _ {j t} + M o n t h _ {t} + \varepsilon_ {i j t}, \end{array} \tag {10}
$$

where $C _ { i j , t - 1 }$ is a dummy variable that takes the value 1 if consumer i has previously checked in at another restaurant in the same chain as restaurant j until period t <sup>−</sup> 1 and zero otherwise. The efect of observational learning is measured by $| \delta _ { 1 } + \xi _ { 1 } C _ { i j , t - 1 } + 2 \delta _ { 2 } R _ { i j , t - 1 } +$ $2 \xi _ { 2 } C _ { i j , t - 1 } R _ { i j , t - 1 } |$ . In column (4) of Table 5, we find that the coeficient of the triple interaction term, $\xi _ { 1 } ,$ is significantly positive and that $\xi _ { 2 }$ is positive but not statistically significant, indicating that checking in at another restaurant in the same chain can significantly reduce the efect of observational learning. The intuition is as follows: Suppose that a consumer has not visited hot pot j (a chain store) before, but if the consumer has visited another hot pot k in the same chain, the efect of observational learning for hot pot j would be much weaker because the quality of the food and service are standardized within the same chain. Therefore, this finding suggests that consumers are not blindly following their friends’ check-ins. Instead, they draw inferences from the restaurant characteristics: This indicates observational learning.

## 8. Managerial Implications

The advancement of location-based technology has provided an unprecedented opportunity for local vendors, such as restaurants, to target consumers by location and boost observational learning (Luo et al. 2013). Generally, firms should adapt their marketing strategies to the advancement of new technology (Chen and Xie 2005). In our specific context, understanding how observational learning is moderated by social and location factors is vital to local vendors to add sales to their brick-and-mortar business, considering their limited marketing campaigns. Our findings have the following implications for the marketing strategies of local businesses and location-based networks.

When should vendors reward their customers’ social checkins to boost observational learning? Our estimation results suggest that the efect of observational learning tends to decline as consumers proceed from trial to repeat. It is more valuable for newer local vendors to reward their customers’ social check-ins, and the learning efect is strong in the early introductory months. Additionally, if local vendors want to devise proper marketing tactics to attract new customers, using location-based technology is an efective way to boost observational learning. By contrast, if the purpose is to retain existing customers, the role of observation learning in location-based networks should be very limited.

What types of vendors can benefit more from observational learning in location-based networks? Our findings suggest that the efect of observational learning is stronger for independent local restaurants than for franchise restaurants. Therefore, independent local restaurants can more actively cooperate with location-based social networks (e.g., provide check-in deals) to boost observational learning.

How should vendors use seeding to boost observational learning? Seeding is the process of marketing to specific customers. In our context, seeding refers to the fact that restaurants reward specific consumers in the form of discounts (check-in deals) when they check in using location-based services to stimulate observational learning and oil the wheels of local commerce. In light of the limited marketing budget of local businesses, restaurants may want to target a small group of customers and reward their social check-ins instead of ofering check-in deals to all customers. Our empirical results provide guidelines on how to select influential customers to optimize the overall efect of observational learning. The magnitude of observational learning depends on the strength of social ties, whether the restaurant is in the focal consumer’s local region, and whether the restaurant is in the focal consumer’s friend’s local region. For instance, a retailer’s natural strategy is to target consumers near its own location. However, our empirical results suggest that targeting nearby consumers could be a better way to maximize the overall efect of observational learning. Information on these moderating factors can be easily extracted from customers’ social network graphs and their previous social check-ins. By cooperating with locationbased social networks, local businesses can obtain all of the relevant information and adjust their seeding strategies accordingly.

How should locations be recommended to users? Our research has managerial implications for location-based networks. Recommending a new restaurant to a user is a typical “cold-start” problem because there is no historical information on the user for the new place (Gao and Liu 2014). According to our empirical results on observational learning, using users’ friends’ checkins and other location and social factors discussed in our study can help address the cold-start problem and improve the performance of location recommendation.

## 9. Conclusions

In this paper, we estimated an empirical model of restaurant discovery and quality learning using data from a location-based application in China. We tested for observational learning based on our empirical approach. We also investigated how social and location factors moderate the eficacy of observational learning and discussed the managerial implications.

Our study has several limitations. First, just as Hinz et al. (2011), and Lee et al. (2015 and 2016), we assumed that the location-based social network remains fixed for the duration of our study. This assumption ignores the efects of dynamic network formation in real-world social networks. Second, an implicit assumption in our empirical model is that the restaurant quality remains the same over time.<sup>9</sup> However, in reality, restaurant quality can change over time. In Online Appendix D, we re-estimate our model using a shorter time frame (in a shorter time frame, the restaurant quality is less likely to change) and the results are consistent with our main results. Third, consumers might be more likely to check in at certain types of restaurants or certain types of consumers might be more likely to check in.<sup>10</sup> For example, people who highly value their privacy could be less willing to share their check-ins when they visit venues.<sup>11</sup> We expect to incorporate more accurate consumer behavior data, such as restaurant reservations, in the future. Finally, our primary purpose here is to separate observational learning from homophily. Separating observational learning from the awareness efect is much more dificult in archival data because both are causal informational mechanisms. As a future research direction, it would be interesting to conduct field experiments to separate observational learning from the awareness efect in location-based networks.

## Acknowledgments

The authors thank the senior editor, associate editor, and three anonymous reviewers for their detailed and constructive comments. The authors also thank Wenjing (Wendy) Duan, Hossein Ghasemkhani, Nina Huang, Yi-Chun (Chad) Ho, Yili (Kevin) Hong, De Liu, YoungKi Park, Tianshu Sun, Jinhong Xie, Lizhen Xu, Lei (Michelle) Wang, and the seminar participants at Arizona State University, George Washington University, Temple University, University of Washington, University of Southern California, University of Alberta, the 2015 Conference on Information Systems and Technology, the 2015 INFORMS Annual Meeting, and the 2016 Production and Operations Management Society Annual Conference for helpful feedback.

## Endnotes

<sup>1</sup> A hot pot (also known as a steamboat) refers to several East Asian varieties of stew served in a simmering metal pot of stock at the center of the dining table.

<sup>2</sup> Because time-invariant IVs will be canceled out in the within transformation of a fixed efects model, we do not include user social network measures in Equation (1b).

<sup>3</sup> In Online Appendix J, we examine a more flexible structure that allows us to explicitly model the correlation between q and p .

<sup>4</sup> Our location-based application asked users to voluntarily provide their demographic information, such as gender and birth date. Many users did not provide this information. This is why we did not include these observable user characteristics in our main estimation. We present the results estimated using only consumers who reported their demographic information in Online Appendix F. The results are consistent with our main results.

<sup>5</sup> Dianping, the restaurant review platform that is sometimes referred to as the Yelp of China, is valued at \$4 billion (Carew and Osawa 2015).

<sup>6</sup> Note that, in Equation (3), we do not directly model the process of Bayesian learning in networks because the decision rules used in perfect Bayesian equilibria are complicated and the analytic solution requires strong assumptions on network topology (Acemoglu et al. 2011, Qiu and Whinston 2017).

<sup>7</sup> Shanghai has an extensive public transportation system. At the end of 2009, the bus system operated 16,000 buses and 38,000 bus stations, with 86% ground area coverage (within 500 meters of catchments). In 2009, bus and rail comprised 25.8% of all travel modes. Cycling and walking are the most predominant mode of travel, accounting for 36.5% of all trips in Shanghai (Cheong and Nadiah 2013).

<sup>8</sup> We also adopt another measure of consumer i’s familiar region, i.e., the region within 5 kilometers of the restaurant in which consumer i has the largest number of check-ins until period t. The qualitative results are similar.

<sup>9</sup> This assumption is widely adopted in almost all observational learning models (e.g., Banerjee 1992, Bikhchandani et al. 1992, Cai et al. 2009, Acemoglu et al. 2011, Tucker and Zhang 2011, Zhang and Liu 2012, Zhang et al. 2015).

<sup>10</sup> Despite the potential self-selection bias, using mobile check-ins to measure consumer visits is in line with the literature that has examined similar issues (Liu et al. 2014, Wang et al. 2015). In reality, individual-level data on actual consumer visits are very dificult to obtain and most prior studies used mobile check-ins to approximate actual consumer visits (Liu et al. 2014, Wang et al. 2015). In practice, businesses also monitor real-time mobile check-ins to evaluate their own and their competitors’ performances because the number of check-ins tends to be highly correlated with store trafic (Liu et al. 2014). For instance, Jef Glueck, the CEO of Foursquare, used the users’ mobile check-ins to accurately predict that Chipotle’s firstquarter sales in 2016 would be down nearly 30% (Turner 2016).

<sup>11</sup> However, as Lindqvist et al. (2011) show, privacy concerns have not kept users from experimenting with and adopting location-based services. Restaurants and bars are fairly popular places at which to check in. Therefore, we believe the selection bias is small.

## References

Acemoglu D, Dahleh MA, Lobel I, Ozdaglar A (2011) Bayesian learning in social networks. Rev. Econom. Stud. 78(4):1201–1236.

Andrews M, Luo X, Fang Z, Ghose A (2015) Mobile ad efectiveness: Hyper-contextual targeting with crowdedness. Marketing Sci. 35(2):218–233.

Aral S, Walker D (2011) Creating social contagion through viral product design: A randomized trial of peer influence in networks. Management Sci. 57(9):1623–1639.

Aral S, Walker D (2014) Tie strength, embeddedness, and social influence: A large-scale networked experiment. Management Sci. 60(6):1352–1370.

Aral S, Muchnik L, Sundararajan A (2009) Distinguish influencebased contagion from homophily-driven difusion in dynamic networks. Proc. Natl. Acad. Sci. 106(51):21544–21549.

Asch SE (1951) Efects of group pressure on the modification and distortion of judgments. Guetzkow H, ed. Groups, Leadership and Men (Carnegie Press, Pittsburgh), 177–190.

Bakshy E, Rosenn I, Marlow C, Adamic L (2012) The role of social networks in information difusion. Proc. 21st Internat. Conf. World Wide Web (ACM, New York), 519–528.

Banerjee AV (1992) A simple model of herd behavior. Quart. J. Econom. 107(3):797–817.

Bapna R, Qiu L, Rice S (2017) Repeated interactions vs. social ties: Quantifying the economic value of trust, forgiveness, and reputation using a field experiment. MIS Quart. 41(3):841–866.

Bichler M, Gupta A, Ketter W (2010) Designing smart markets. Inform. Systems Res. 21(4):688–699.

Bikhchandani S, Hirshleifer D, Welch I (1992) A theory of fads, fashion, custom, and cultural change in informational cascades. J. Political Econom. 100(6):992–1026.

Bjorkegren D (2015) The adoption of network goods: Evidence from the spread of mobile phones in Rwanda. Working paper, Brown University, Providence RI, https://ssrn.com/abstract<sup></sup>2616524.

Bramoullé Y, Djebbari H, Fortin B (2009) Identification of peer efects through social networks. J. Econometrics 150(1):41–55.

Cai H, Chen Y, Fang H (2009) Observational learning: Evidence from a randomized natural field experiment. Amer. Econom. Rev. 99(3):864–882.

Cairncross F (2001) The Death of Distance: How the Communications Revolution is Changing Our Lives (Harvard Business Press, Boston).

Carew R, Osawa J (2015) China’s Dianping valued at 4 billion. Wall Street Journal (April 2), https://www.wsj.com/articles/chinas -dianping-valued-at-4-billion-1427962959.

Chatterjee P (2001) Online reviews: Do consumers use them? Gilly MC, Myers-Levy J, eds. Advances in Consumer Research (Association for Consumer Research, Valdosta, GA), 129–134.

Chen Y, Xie J (2005) Third-party product review and firm marketing strategy. Marketing Sci. 24(2):218–240.

Chen Y, Wang Q, Xie J (2011) Online social interactions: A natural experiment on word of mouth versus observational learning. J. Marketing Res. 48(2):238–254.

Cheong CC, Nadiah LOH (2013) Transport policies and patterns: A comparison of five Asian cities. JOURNEYS 69–78.

Cook KS (2005) Networks, norms, and trust: The social psychology of social capital. Soc. Psych. Quart. 68(1):4–14.

Danaher PJ, Smith MS, Ranasinghe K, Danaher TS (2015) Where, when and how long: Factors that influence the redemption of mobile phone coupons. J. Marketing Res. 52(5):710–725.

Duan W, Gu B, Whinston AB (2009) Informational cascades and software adoption on the Internet: An empirical investigation. MIS Quart. 33(1):23–48.

Erdem T, Keane MP, Sun B (2008) The impact of advertising on consumer price sensitivity in experience goods markets. Quant. Marketing Econom. 6(2):139–176.

Fang Z, Gu B, Luo X, Xu Y (2015) Contemporaneous and delayed sales impact of location-based mobile promotions. Inform. Systems Res. 26(3):552–564.

Fong NM, Fang Z, Luo X (2015) GEO-conquesting: Competitive locational targeting of mobile promotions. J. Marketing Res. 52(5):726–735.

Forman C, Ghose A, Wiesenfeld B (2008) Examining the relationship between reviews and sales: The role of reviewer identity disclosure in electronic markets. Inform. Systems Res. 19(3):291–313.

Gao H, Liu H (2014) Data analysis on location-based social networks. Mobile Social Networking (Springer, New York), 165–194.

Ghose A, Goldfarb A, Han SP (2012a) How is the mobile Internet diferent? Search costs and local activities. Inform. Systems Res. 24(3):613–631.

Ghose A, Ipeirotis PG, Li B (2012b) Designing ranking systems for hotels on travel search engines by mining user-generated and crowdsourced content. Marketing Sci. 31(3):493–520.

Granovetter MS (1973) The strength of weak ties. Amer. J. Sociol. 78(6):1360–1380.

Hendricks K, Sorensen A (2009) Information and the skewness of music sales. J. Political Econom. 117(2):324–369.

Hinz O, Skiera B, Barrot C, Becker JU (2011) Seeding strategies for viral marketing: An empirical comparison. J. Marketing 75(6): 55–71.

Hong Y, Hu Y, Burtch G (2018) Embeddedness, pro-sociality, and social influence: Evidence from online crowdfunding. MIS Quart. Forthcoming.

Iyengar R, van den Bulte C, Lee JY (2015) Social contagion in new product trial and repeat. Marketing Sci. 34(3):408–429.

Iyengar R, van den Bulte C, Valente TW (2011) Opinion leadership and social contagion in new product difusion. Marketing Sci. 30(2):195–212.

Ke TT, Yang CZ (2016) Peer efect of iPhone adoptions on social networks. Research paper, Massachusetts Institute of Technology, Cambridge. https://ssrn.com/abstract<sup></sup>2837263.

Kennedy MT, Fiss PC (2009) Institutionalization, framing, and difusion: The logic of TQM adoption and implementation decisions among U.S. hospitals. Acad. Management J. 52(5):897–918.

Lee G, Raghu TS (2014) Determinants of mobile apps success: Evidence from app store market. J. Management Inform. Systems 31(2):133–170.

Lee GM, Qiu L, Whinston AB (2016) A friend like me: Modeling network formation in a location-based social network. J. Management Inform. Systems 33(4):1–26.

Lee JY, Bell DR (2013) Neighborhood social capital and social learning for experience attributes of products. Marketing Sci. 32(6):960–976.

Lee YJ, Hosanagar K, Tan Y (2015) Do I follow my friends or the crowd? Information cascades in online movie ratings. Management Sci. 61(9):2241–2258.

Li X, Wu L (2013) Measuring efects of observational learning and social-network word-of-mouth (WOM) on the sales of daily-deal vouchers. 2013 46th Hawaii Internat. Conf. System Sci. <sup>(</sup>HICSS<sup>)</sup> (IEEE, Piscataway, NJ), 2908–2917.

Lindqvist J, Cranshaw J, Wiese J, Hong J, Zimmerman J (2011) I’m the mayor of my house: Examining why people use foursquare— A social-driven location sharing application. Proc. SIGCHI Conf. Human Factors Comput. Systems (ACM, New York), 2409–2418.

Liu D, Brass D, Chen D (2014) Friendships in online peer-topeer lending: Pipes, prisms, and relational herding. MIS Quart. 39(3):729–742.

Liu Z, Duan JA, Ter Hofstede F (2014) Marketing spillovers of location-based mobile services. Working paper, University of Texas at Austin, http://ssrn.com/abstract<sup></sup>2578335.

Luo X, Andrews M, Fang Z, Phang CW (2013) Mobile targeting. Management Sci. 60(7):1738–1756.

Ma H, Yang H, Lyu MR, King I (2008) SoRec: Social recommendation using probabilistic matrix factorization. Proc. 17th ACM Conf. Inform. Knowledge Management (ACM, New York), 931–940.

Ma L, Krishnan R, Montgomery AL (2014) Latent homophily or social influence? An empirical analysis of purchase within a social network. Management Sci. 61(2):454–473.

Mann L (1969) Social Psychology (John Wiley, New York).

Manski CF (1993) Identification of endogenous social efects: The reflection problem. Rev. Econom. Stud. 60(3):531–542.

Maslow AH (1943) A theory of human motivation. Psych. Rev. 50(4):370.

Moretti E (2011) Social learning and peer efects in consumption: evidence from movie sales. Rev. Econom. Stud. 78(1):356–393.

Qiu L, Whinston AB (2017) Pricing strategies under behavioral observational learning in social networks. Production Oper. Management 26(7):1249–1267.

Qiu L, Rui H, Whinston AB (2014) Efects of social networks on prediction markets: Examination in a controlled experiment. J. Management Inform. Systems 30(4):235–268.

Shadish WR, Cook TD, Campbell DT (2002) Experimental and Quasi-Experimental Designs for Generalized Causal Inference (Houghton Miflin, Boston).

Shi Z, Whinston AB (2013) Network structure and observational learning: Evidence from a location-based social network. J. Management Inform. Systems 30(2):185–212.

Shriver SK, Nair HS, Hofstetter R (2013) Social ties and usergenerated content: Evidence from an online social network. Management Sci. 59(6):1425–1443.

Simonsohn U, Ariely D (2008) When rational sellers face nonrational buyers: Evidence from herding on eBay. Management Sci. 54(9):1624–1637.

Simonsohn U, Karlsson N, Loewenstein G, Ariely D (2008) The tree of experience in the forest of information: Overweighing experienced relative to observed information. Games Econom. Behav. 62(1):263–286.

Takács G, Pilászy I, Németh B, Tikk D (2009) Scalable collaborative filtering approaches for large recommender systems. J. Machine Learn. Res. 10(3):623–656.

Tolbert PS, Zucker LG (1983) Institutional sources of change in the formal structure of organizations: The difusion of civil service reform, 1880–1935. Admin. Sci. Quart. 28(1):22–39.

Tucker C (2008) Identifying formal and informal influence in technology adoption with network externalities. Management Sci. 54(12):2024–2038.

Tucker C, Zhang J (2011) How does popularity information afect choices? A field experiment. Management Sci. 57(5):828–842.

Turner M (2016) An unlikely source predicted Chipotle’s disastrous quarter, and it says a lot about the future of investing. Business Insider (April 27). Accessed July 18, 2016, http://www .businessinsider.com/foursquare-data-predicted-chipotle-results -2016-4.

Wang A, Zhang M, Hann IH (2018) Socially nudged: A quasiexperimental study of friends’ social influence in online product ratings. Inform. Systems Res., ePub ahead of print May 10, https://doi.org/10.1287/isre.2017.0741.

Wang L, Gopal R, Shankar R, Pancras J (2015) On the brink: Predicting business failure with mobile location-based checkins. Decision Support Systems 76:3–13.

Wang Q, Goh KY (2012) Consumer segmentation and the information rule of online reviews in horizontally diferentiated product markets. E-Life: Web-Enabled Convergence of Commerce, Work, and Social Life (Springer, Berlin Heidelberg), 225–233.

Westphal JD, Gulati R, Shortell SM (1997) Customization or conformity? An institutional and network perspective on the content and consequences of TQM adoption. Admin. Sci. Quart. 42(2):366–394.

Xu H, Teo HH, Tan BCY, Agarwal R (2012) Efects of individual selfprotection, industry self-regulation, and government regulation on privacy concerns: A study of location-based services. Inform. Systems Res. 23(4):1342–1363.

Zhang J (2010) The sound of silence: Observational learning in the U.S. kidney market. Marketing Sci. 29(2):315–335.

Zhang J, Liu P (2012) Rational herding in microloan markets. Management Sci. 58(5):892–912.

Zhang J, Liu Y, Chen Y (2015) Social learning in networks of friends versus strangers. Marketing Sci. 34(4):573–589.

Zhang X, Wang C (2012) Network positions and contributions to online public goods: The case of Chinese wikipedia. J. Management Inform. Systems 29(2):11–40.

Zhu F, Zhang X (2010) Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. J. Marketing 74(2):133–148.

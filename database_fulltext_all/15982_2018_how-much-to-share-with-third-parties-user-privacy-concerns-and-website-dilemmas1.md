---
otero_id: 15982
otero_key: "Y8D6J3HA"
title: "How Much to Share with Third Parties? User Privacy Concerns and Website Dilemmas1"
authors: "Ram D. Gopal; Hooman Hidaji; Raymond A. Patterson; Erik Rolland; Dmitry Zhdanov"
year: "2018"
journal: "MIS Quarterly"
doi: "10.25300/misq/2018/13839"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# HOW MUCH TO SHARE WITH THIRD PARTIES? USER PRIVACY CONCERNS AND WEBSITE DILEMMAS<sup>1</sup>

Ram D. Gopal Operations and Information Management, School of Business, University of Connecticut, Storrs, CT 06269 U.S.A. {ram.gopal@business.uconn.edu}

Hooman Hidaji and Raymond A. Patterson Haskayne School of Business, University of Calgary, Calgary, AB, CANADA T2N 1N4 {hooman.hidaji@haskayne.ucalgary.ca} {raymond.patterson@ucalgary.ca}

Erik Rolland College of Business Administration, California State Polytechnic University, Pomona, CA 91768 U.S.A. {erolland@cpp.edu}

Dmitry Zhdanov Department of Computer Information Systems, J. Mack Robinson College of Business, Georgia State University, Atlanta, GA 30302 U.S.A. {dzhdanov@gsu.edu}

Publishers websites are increasingly presenting content and services that are not created and managed by the website administrators themselves, but are provided by other third parties. While third party content and services provide value and utility to website users, this comes at the cost of user information being shared with the third party. Privacy concerns surrounding information leakage have been growing rapidly. With increasing concerns regarding online privacy and information disclosure, it is important to understand the factors that affect the level of sharing between publisher websites and third parties. In this study, we propose a two-sided economic model that captures the interaction between the users, publisher websites, and third parties. Specifically, we focus on the effect of privacy concerns on the sharing behavior of the publisher website and the impact of users’ privacy concerns on third party market concentration. We then analyze welfare aspects to provide insights on the impacts of industry regulations and policy on users, publisher websites, and third parties. We partially validate the model using an exploratory empirical analysis of publisher website third party sharing behavior and the structure of the industry. To the best of our knowledge, thi study is among the first to analyze publisher website decision making in sharing user information with third parties.

Keywords: Economics of information systems, privacy, third parties, information sharing, social welfare

## Introduction

Websites on the World Wide Web have become ever more resourceful, enabling users (i.e., visitors) to obtain various services and information from them. In doing so, publisher websites outsource components of their websites, and present content and services provided by third party providers on their pages. Thus the user experience of visiting a publisher website involves interactions with many third parties. Use of third parties is pervasive among top publisher websites. Gopal et al. (2014) investigate 700 popular websites, showing that these publisher websites utilize an average of 13.5 (and up to 70 in some cases) third parties. Since third parties can and do obtain user information from publisher websites, it creates natural tension between the use of third party components and user privacy. A U.S. Senate report states:

A visit to an online news site may trigger interactions with hundreds of other parties that may be collecting information on the consumer as he travels the web. The Subcommittee found, for example, a trip to a popular tabloid news website triggered a user interaction with some 352 other web servers as well. Many of those interactions were benign; some of those third-parties, however, may have been using cookies or other technology to compile data on the consumer. The sheer volume of such activity makes it difficult for even the most vigilant consumer to control the data being collected or protect against its malicious use (United States Senate 2014, p. 1).

The most familiar sharing mechanism involves the use of cookies, but other more sophisticated approaches exist as well. This sharing of user information with third parties is typically done without explicit user consent or appropriate disclosure mechanisms. For example, policies regarding shared information are often hidden deep within complex privacy statements, and users share readily via convenient one-click sign-up mechanisms such as “Sign up with your Facebook, Google, or Twitter account.”

Reduction in cost of information storage and processing has enabled firms to collect and utilize large amounts of user information. It has become extremely difficult, if not impossible, to know who is tracking users online (Schoen 2009). Interestingly, the extent of collected information is not limited to browsing data, and the data can be used for identification or re-identification of individuals when used alongside other sources (Krishnamurthy and Wills 2009a). Privacy issues that arise from the increased usage of third parties and cookies is a public concern, and is being investigated by authorities and policy makers such as the Federal Trade Commission and the European Union (Mayer and Mitchell 2012). Turow et al.

(2009) surveys users in the United States to find that between 68% and 87% do not want to be tracked for advertising purposes. McDonald and Cranor (2010) also find that only 20% of users prefer targeted online advertising over random advertising. Mayer and Mitchell (2012) provide a review of the policies and technologies surrounding web tracking. They note the fact that regulation is lacking behind the fast-growing industry, and emphasize the importance of discussions and debates on the topic.

Publisher websites can have a variety of revenue streams. Two main monetization approaches are (1) subscription services and (2) selling of user information for purposes such as affiliate marketing (e.g., lead generation), targeting, and customization. Publisher websites utilize one or a combination of these approaches. For example, consider the news websites for Financial Times and The Washington Times depicted in Figure 1, highlighting various visible third party components. While Financial Times requires readers to subscribe in order to read articles, reading articles in The Washington Times is free. Thus The Washington Times website operation depends entirely on income from third parties that pay the publisher to obtain website user information. We find that Financial Times shares with fewer third parties than The Washington Times (22 compared to 36). In some cases, sharing of user information can be quite disconcerting.

Most organizations involved with web publishing face a choice of using a variety of financial models to derive revenue. For example, The New York Times simultaneously employs both advertising and subscription revenues (New York Times 2016), including providing ads to users with subscriptions (Singleton 2016). Somaiya (2015a, 2015b) describes this dual strategic approach by The New York Times. A mix of subscription and advertising revenues, which is consistent with The New York Times strategy, is often observed. As a second anecdotal observation, ads are presented in conjunction with mobile subscriptions by The Los Angeles Times. The advertising may possibly be altered with a subscription, but clearly a blending of both revenue generation strategies is observed.

In the literature, some researchers have attested to the presence of several sources of monetization. For example, as Kumar and Sethi (2009) note,

The accumulated evidence indicates that pure revenue models, such as free-access models and pure subscription fee-based models, are not sufficient to support the survival of online information sellers. Hence, hybrid models based on a combination of subscription fees and advertising revenues are replacing the pure revenue models (p. 924).

![](/api/attachments/Y8D6J3HA/fulltext/images/4c57713d6ff1e5854988fa22e4f7511374ac6838a8d851cf8f630b320d826f16.jpg)  
Figure 1. Two Sample Publisher Websites with Selected Third Party Content Highlighted

As Casadesus-Masanell and Hervas-Drane (2015) note, “Firms compete for consumer information and derive revenues both from consumer purchases as well as from disclosing consumer information in a secondary market” (p. 229). One important way for websites to make revenue from third parties is through lead generation. Third parties involved in the collection of user information for lead generation include advertisers and advertising agencies, content providers, and data aggregators, among others. These third parties provide support and information required for improved targeting of website ads and improved sales opportunities. Similarly, behavioral targeting, which utilizes information shared with the many third parties, tracks user behavior within and across websites (Helft and Vega 2010) to combine user data to present the most relevant ads. We specifically consider the impact of user privacy concerns resulting from the sale of user information to generate additional revenues for the publisher website.

While the problem of information privacy in publisher websites is faced by many, it has not received much attention in the academic literature. An extensive body of work has addressed information privacy in the context of e-commerce where users willingly provide their information to companies (Li 2012), but there is a gap in the literature concerning the use of third parties by publisher websites and the disclosure of personal information, along with the publisher’s decisionmaking on deriving revenue from both users and third parties for its website. In this paper, we address this gap by considering the issue of web traffic monetization versus information privacy from an economic perspective. Using a twosided stylized economic model, we analyze how publisher websites control monetization of both users and third parties through setting user subscription prices and third party royalties. The analysis is provided for duopolistic publisher websites, for many users, and for third parties. We find that user privacy concerns can impact publisher website monetization decisions. In asymmetric settings, we demonstrate that publishers may choose drastically different business models for their websites, ranging from a focus on privacy-sensitive users to price-sensitive users. We also provide welfare analysis, and analysis of the impact of several practical regulatory tools that can be used to help improve the surplus of users, publisher websites, and/or third parties.

The contributions of this paper are as follows. First, we provide a two-sided economic model that describes the decisionmaking process of the publisher for its website based on the privacy concerns of the user, participation incentives of third party service providers, and the publisher’s own incentives to maximize profits from its website. Second, we discuss the effects of privacy concerns on the stakeholders, the impact on third party industry concentration, and implications for policymaking. Third, we contribute to the two-sided market literature, and discuss the problem where the two sides affect each other both positively and negatively. Finally, we provide an empirical validation and partial support for several important aspects of the model. This empirical validation also serves to illustrate the problems surrounding information privacy versus publisher website monetization that publisher websites, users, third parties, and policymakers face. The proposed model explains differences in third party sharing by publisher websites, and provides managerial and policy insights for publisher websites, policymaking organizations, and governments.

The remainder of the paper is organized as follows. A literature review is provided in the next section. We then present the analytical model and an extension dealing with asymmetry in user privacy concerns. Subsequent sections present discussions on the effects of privacy concerns on market concentration, analysis of the third party market structure, and implications for public policy and regulatory considerations. We conclude with the model robustness check, empirical analysis, and a discussion of our findings.

## Literature Review

This paper contributes to several streams of literature. First, it is relevant to the literature on third party sharing in publisher websites. Second, it contributes to the literature on online privacy and its implications. Finally, we contribute to the literature on two-sided markets.

Despite the omnipresent use of third parties in publisher websites, work that addresses such third parties is sparse. Third parties do provide some benefit by providing additional services to websites which can be inferred by the pandemic use of third parties in websites (Mayer and Mitchell 2012). Adler et al. (2002), among others, have considered scheduling of online advertising. This stream of literature considers more technical aspects of resource management in publisher websites, but does not provide insights on the larger picture of publisher website decision-making in the presence of revenues from both users and third parties, nor when users have privacy concerns. Chen and Stallaert (2014) provide an economic analysis of online behavioral advertising. They find the conditions for which the use of behavioral advertising is better than traditional advertising for a publisher website. While their model can incorporate the privacy concerns of users in the form of opting out of the service, the authors only consider the problem of choosing between traditional and behavioral advertising, and do not consider the problem from a privacy point of view. Kumar and Sethi (2009) also consider the problem of online information sellers and dynamic pricing in this context. Their study is one of the few that considers both subscription and advertising revenues simultaneously, and they use optimal control theory to dynamically price advertising and subscriptions.

There are many papers that study the effect of third parties on user information diffusion. Krishnamurthy and Wills (2006) find that “the size of the privacy footprint is a legitimate cause for concern” (p. 70). They also find a significant increase in the privacy footprint over a six month period. Krishnamurthy and Wills (2009b) show, in a longitudinal study, that the sharing and aggregation of user information has been increasing, while the number of entities involved has been decreasing as a result of acquisitions. One of the issues that arise as a result of privacy leakage is discrimination among different users. Krishnamurthy et al. (2011) study websites that require users to register and provide personal information, and find that 75% of the popular websites studied leak sensitive user information to third parties. Mikians et al. (2012) and Valentino-DeVries et al. (2012) provide evidence for price and search discrimination in an e-commerce setting, which is based on user information on the web. Recently, there has been even more concern about the implications of information sharing with third parties. Quintin (2015) provides evidence for sharing of users’ health related and other information. This stream of literature magnifies the importance of understanding how publisher websites operate and their incentives in sharing user information. Malandrino and Scarano (2013) study how third party sites collect and aggregate data, and build personal profiles of users. They provide an empirical study on how a user’s privacy can be undermined because of such privacy violations, and experiment with tools that can inform users and give them control over such activities. However, these tools are only used by tech savvy users, and not by the majority of users.

Online information privacy has been studied by several researchers. While this literature does not directly focus on third parties, many of the principles are applicable to information privacy in third party sharing. Using an economic model, Chellappa and Shivendu (2007) consider the personalization versus privacy tradeoff that users make when they reveal their personal information online. Smith et al. (2011) provides a review of studies on information privacy. Li (2012) provides a comprehensive review of the extensive online information privacy literature, and provides a framework for theoretical research on the user’s privacy decisionmaking. Smith et al. and Li provide that user information disclosure in the form of third party usage can be explained by theories such as privacy calculus theory, risk calculus theory, and dual-calculus theory, among many foundational theories. In this paper, we argue that a publisher’s behavior regarding its website cannot be viewed in isolation, as it is affected by both users and third parties. Publishers realize that users factor privacy in their economic evaluation of transacting with the website. According to agency theory and utility maximization theory and their application in information privacy (Li 2012), a publisher sets decision variables on its website to maximize total profit from users and third parties collectively.

One of the more relevant studies to ours is Casadesus-Masanell and Hervas-Drane (2015), who study how the competition between online firms is affected by user privacy concerns. This study is also one of the few considering the effect of privacy on publisher website decision making. Similar to our study, they consider online firms that derive revenue from users via subscriptions and by “disclosing consumer information in a secondary market” (p. 229), where positive and negative cross-side network effects exist among users and third parties in the secondary market. They find that in competition, firms differentiate among themselves and focus on one of the revenue sources. Our study is different from theirs in that we focus on the internal decision-making of a publisher website. We consider the factors that affect the balance that publisher websites must achieve between users desire for privacy and monetization of user information, and the implicit privacy violations that monetization entails. Moreover, we focus on the participation of users and third parties, as well as the impact of user privacy concerns on the third party industry.

This paper is related to the significant literature on two-sided markets, where a platform provider is affected by two markets that interact and create network effects. Rochet and Tirole (2003) and Parker and Van Alstyne (2005) study the pricing strategies in such markets. Anderson et al. (2013) consider the platform investment in quality in two-sided networks. Most of the studies in this stream consider markets in which positive indirect network effects are present among the two markets. Casadesus-Masanell and Hervas-Drane’s study is one of the few that considers both positive and negative crosssided network effects. In this paper, we model the problem as a two-sided market, having users on one side and third parties on the other, both contributing to the profit making of a publisher website. We consider both positive and negative network effects among the users and third parties. While third parties enjoy having more users on the publisher website, users do not appreciate third parties due to privacy concerns. This will be discussed further in the following section.

## Model

In this section, we propose an economic model in order to describe and analyze the problem of third party usage in publisher websites. The notations are provided in Tables 1 and 2.

## Base Model

We consider a two-sided market model involving three players: two publisher websites, publisher website users, and third parties. The publisher websites are seen as the platforms where users participate to get a certain utility, and third parties participate to get access to user information. The analysis is provided for two publisher websites, and for multiple third parties and users. The model employs a duopolistic price-maker with royalties and subscription prices as decision variables for the publisher website, and it incorporates the two-sided network effects of users and third parties.

In our model, third parties can make revenue from users on the publisher website. It is assumed that more users results in more information for the third party to collect. On the other hand, we assume that third parties provide no additional benefit to the user. While in many instances third parties do provide some utility to the user, here we consider the case in which the publisher is considering whether or not to outsource a service on its website, where the third party is a substitute for the publisher’s own website service. In this setting, the third party brings only disutility to the user with no additional benefit to the user than what they already receive from the publisher website in terms of an intrinsic value X. There are many studies that provide evidence for the negative utility of third parties for users (Krishnamurthy and Wills 2006; Turow et al. 2009). Moreover, Krishnamurthy et al. (2007) found that blocking of third parties does not significantly affect the usability of publisher websites.

In the duopoly setting, the two publisher websites compete for users. Users will choose exactly one of the two publisher websites (the user market is covered by two publisher websites), but third parties can participate in either of the publisher websites, both, or not participate at all. The publisher websites are symmetric in terms of the users’ intrinsic valuation for the website, user privacy concerns, and the revenue that the third party makes from user information. In the “Asymmetry in User Privacy Concerns” section, we relax the user privacy concern symmetry assumption.

A Hotelling model is used to differentiate users’ utility from either publisher website. Publisher website 1 is located at location 0, and publisher website 2 is located at 1, with a fit cost of t. Users are uniformly located between locations 0 and 1. If a user at location y decides to go with publisher website 1, her utility is modeled as

$$
U _ {1} (y) = u _ {1} - t y, \qquad u _ {1} = X - N _ {D _ {1}} v - P _ {W _ {1}}\tag{1}
$$

where $N _ { D _ { 1 } }$ is the number of third parties on the publisher website 1 and $P _ { W _ { 1 } }$ is the price of using publisher website 1. v is user’s disutility from each third party, or user’s sensitivity to privacy violations. From now on, we call this parameter user privacy concerns. The argument ty is the user fit cost to use publisher website 1. Similarly, utility of the user for the second publisher website is

$$
U _ {2} (y) = u _ {2} - t (1 - y), \qquad u _ {2} = X - N _ {D _ {2}} v - P _ {W 2}\tag{2}
$$

where $N _ { D _ { 2 } }$ and $P _ { W _ { 2 } }$ are the number of third parties on the publisher website 2 and the price of using publisher website 2, respectively. Users will choose the publisher website that yields higher utility. Thus, using the two utility functions, the location of the indifferent user between two publisher websites, yˆ can be calculated as

$$
u _ {1} - t \hat {y} = u _ {2} - t (1 - \hat {y}) \Rightarrow \hat {y} = \frac {t + (N _ {D _ {2}} - N _ {D _ {1}}) v + (P _ {W _ {2}} - P _ {W _ {1}})}{2 t}\tag{3}
$$

<table><tr><td colspan="2">Table 1. Model Parameters and Variables</td></tr><tr><td>Notation</td><td>Definition</td></tr><tr><td>y</td><td>Location of a user in Hotelling&#x27;s model,  $0 \leq y \leq 1$ </td></tr><tr><td>t</td><td>Hotelling&#x27;s fit cost or publisher website differentiation,  $0 \leq t$ </td></tr><tr><td>X</td><td>Intrinsic value of the publisher website for users, X&gt;0</td></tr><tr><td> $U_{i}(y)$ </td><td>Utility of a user at location y for publisher website i; a user will use the publisher website with higher utility when  $Max(U_{1}(y), U_{2}(y)) \geq 0$   $\forall y \in [0, 1]$ </td></tr><tr><td> $N_{U_{i}}$ </td><td>Number of users for publisher website i,  $N_{U_{i}} > 0$   $\forall i = 1,2$ </td></tr><tr><td>v</td><td>User&#x27;s perceived disutility from each third party or user privacy concerns, v ≥ 0</td></tr><tr><td> $M_{U}$ </td><td>Total number of potential users in the market,  $M_{U} \geq N_{U_{i}}$   $\forall i = 1,2$ ,  $M_{U} > 0$ </td></tr><tr><td> $\Pi_{D_{i}}$ </td><td>Third party profit from publisher website i; a third party will join publisher website i if  $\Pi_{D_{i}} \geq 0$ </td></tr><tr><td>φ</td><td>Fixed cost of a third party, φ ≥ 0</td></tr><tr><td>Φ</td><td>Maximum third party fixed cost, Φ &gt; 0</td></tr><tr><td> $N_{D_{i}}$ </td><td>Number of third parties on publisher website i,  $N_{D_{i}} \geq 0$ </td></tr><tr><td> $M_{D}$ </td><td>Total number of potential third parties in the market,  $M_{D} \geq N_{D_{i}}$   $\forall i = 1,2$   $M_{D} > 0$ </td></tr><tr><td> $R_{D}$ </td><td>Third party&#x27;s net revenue from each user&#x27;s information,  $R_{D} \geq 0$ </td></tr><tr><td> $\Pi_{W_{i}}$ </td><td>Publisher website i&#x27;s profit,  $\Pi_{W_{i}} \geq 0$   $\forall i = 1,2$ </td></tr><tr><td> $Z_{U}$ </td><td>Total user surplus, total utility surplus for all users from both publisher websites</td></tr><tr><td> $Z_{D}$ </td><td>Total third party surplus, total profits of all third parties from both publisher websites</td></tr></table>

<table><tr><td colspan="2">Table 2. Model Decision Variables</td></tr><tr><td>Notation</td><td>Definition</td></tr><tr><td> $_{R_{W_i}}$ </td><td>Publisher website i&#x27;s per user royalty (paid to the publisher website by third party),  $0 \leq R_{W_i} \leq \infty$ </td></tr><tr><td> $P_{W_i}$ </td><td>Publisher website i&#x27;s price per user (paid to the publisher website by user),  $0 \leq P_{W_i} \leq \infty$ </td></tr></table>

Assuming that the total number of potential users in the market is $M _ { U }$ the number of users for each publisher website $i , \ N _ { U _ { i } }$ is calculated as

$$
N _ {U _ {i}} = M _ {U} \frac {t + (N _ {D _ {- i}} - N _ {D _ {i}}) v + (P _ {W _ {- i}} - P _ {W _ {i}})}{2 t} \geq 0\tag{4}
$$

We assume that the third party pays per user royalties $R _ { W _ { i } }$ to each publisher website i in which they participate. This is especially the case for the advertising and lead generation third parties, which pay the publisher per impression or per click on ads, and this is directly correlated with the number of users on the publisher website. The business model of the third party is a form of revenue sharing, where the third party generates revenue from the service and/or lead generation on the website, and then shares some of their profit with the website. Per user royalty, or simply royalty, is set by the publisher as a decision variable. While in practice royalties may be set by the third party, here we consider the case where the publisher sets the royalty. Doing so enables us to analyze and provide insights on how the publisher balances the needs of users and third parties. The publisher controls the number of third parties on the website, and thus the total effect of user privacy concerns in their utility, by setting royalties. For a third party with the fixed cost of $\Phi ,$ the profit from each publisher website i is calculated as

$$
\begin{array}{c} \Pi_ {D _ {i}} (\varphi) = N _ {U _ {i}} R _ {D} - N _ {U _ {i}} R _ {W _ {i}} - \varphi = \\ N _ {U _ {i}} (R _ {D} - R _ {W _ {i}}) - \varphi \end{array}\tag{5}
$$

Where $R _ { D }$ is the net revenue that the third parties can obtain from each user’s information, or simply third party revenue from user information. Third parties have a fixed cost for their operations, which is assumed to be uniformly distributed over [0, Φ]. The fixed cost of a third party that is indifferent between joining or not joining a publisher website i is characterized by $\hat { \varphi } _ { i } = N _ { U _ { i } } \big ( R _ { D } - R _ { W _ { i } } \big )$ . The third parties having $\varphi < \hat { \phi } _ { i }$ will join the publisher website i. The ratio of third parties that will provide the service to publisher website i is calculated as $\frac { \hat { \varphi } _ { i } } { \Phi }$ Assuming that there are overall $M _ { D }$ number of potential third parties in the market, the number of third parties that will join the publisher website $i , \ N _ { D _ { i } }$ is calculated as

$$
N _ {D _ {i}} = M _ {D} \frac {N _ {U _ {i}} (R _ {D} - R _ {W _ {i}})}{\Phi} \geq 0\tag{6}
$$

For the number of third parties to be positive, we need to have $R _ { D } - R _ { W _ { i } } \geq 0 , \qquad \forall i = 1 , 2$ . This is the third party participation constraint.

It can be seen that cross-sided network effects are present among the number of users and the number of third parties. However, the network effects are not positive in both ways as we see in the majority of two-sided market literature. Instead, the externalities are positive in one direction (users to third parties) and negative in the other (third parties to users). In other words, third parties prefer a higher number of users, but users prefer a lower number of third parties. The duopolistic publisher website benefits from both, as they provide revenue for the publisher website.

Solving for $N _ { U _ { i } }$ and $N _ { D _ { i } }$ in (4) and (6), we can calculate the number of users and third parties for each publisher website i as

$$
N _ {U _ {i}} = M _ {U} \frac {\Phi t + \Phi \left(P _ {W _ {- i}} - P _ {W _ {i}}\right) + M _ {U} M _ {D} v \left(R _ {D} - R _ {W _ {- i}}\right)}{2 \Phi t + M _ {U} M _ {D} v \left(\left(R _ {D} - R _ {W _ {i}}\right) + \left(R _ {D} - R _ {W _ {- i}}\right)\right)} \quad \forall i = 1, 2\tag{7}
$$

$$
N _ {D _ {t}} = M _ {U} \frac {M _ {U} \left(R _ {D} - R _ {W _ {i}}\right) \left(\Phi t + \Phi \left(P _ {W _ {- i}} - P _ {W _ {i}}\right) + M _ {U} M _ {D} v \left(R _ {D} - R _ {W _ {- i}}\right)\right)}{\Phi \left(2 \Phi t + M _ {U} M _ {D} v \left(\left(R _ {D} - R _ {W _ {i}}\right) + \left(R _ {D} - R _ {W _ {- i}}\right)\right)\right)} \quad \forall i = 1, 2\tag{8}
$$

As stated earlier, the publisher decides on subscription price and royalties. Profit for each publisher website i is calculated as

$$
\Pi_ {W _ {i}} = N _ {U _ {i}} P _ {W _ {i}} + N _ {D _ {i}} N _ {U _ {i}} R _ {W _ {i}} \quad \forall i = 1, 2\tag{9}
$$

Note that in this setting, the publisher website generates revenue from only two sources: users paying a price in exchange for access to the website, and third parties paying a royalty in return for user information. In reality, the website can also generate revenue from third parties without providing them with user information. An example of this is advertising where third parties only have access to information regarding the content of the publisher website, and not the users themselves. While this additional revenue source can be easily added to the model, we do not consider this for three reasons. First, the focus of this paper is mainly on the privacy tradeoff that the users make by going to websites with third parties who collect information about users. Second, our experiments on the publisher websites (in the “Empirical Analysis” section) show that publisher websites predominantly provide third parties with user information. Third, a model with added revenue from third parties that do not collect user information (e.g., traditional advertising) provides the same major insights as the model without such added revenue, and therefore we omit these third parties for parsimony.

By substituting for $N _ { U _ { i } }$ and $N _ { D _ { i } }$ from (7) and (8) in the publisher website profit equation (9) we obtain the formula for publisher website profit. Each publisher decides on its website royalty and price, independently of the other publisher website. Using the first and second order conditions, we can calculate the optimal royalties and price of each publisher website, as is given in Lemma 1. In this case, the two firms set symmetric prices and royalties. The proofs for lemmas and propositions are provided in Appendix A. We note from the discussion above and the discussion in Appendix A that our assumptions include that the publisher website profit is continuous and twice differentiable with respect to website price and royalties, there is a maximum profit (the profit function is concave with respect to both subscription price and royalties), and there exists a positive number of users and third parties.

Lemma 1 In equilibrium, the duopolistic publisher chooses the following symmetric royalties and prices for its website:

$$
R _ {W _ {i}} ^ {*} = R _ {W} ^ {*} = \frac {R _ {D} + v}{2}\tag{10}
$$

$$
P _ {W _ {i}} ^ {*} = P _ {W} ^ {*} = \frac {4 \Phi t - M _ {D} M _ {U} (R _ {D} - v) ^ {2}}{4 \Phi} \quad \forall i = 1, 2\tag{11}
$$

In order to have positive prices, we need to have 4Φt – $M _ { D } M _ { U } ( R _ { D } - \nu ) ^ { 2 } \geq 0$ . Using Lemma 1, Proposition 1 provides the effect of model parameters on the decision variables of the publisher websites.

Proposition 1 The optimal publisher website royalty $( R _ { W } ^ { * } )$ and optimal publisher website price $( P _ { w } ^ { * } )$ in equilibrium satisfy the following:

(i) $\boldsymbol { R } _ { \boldsymbol { W } } ^ { * }$ increases with user privacy concerns (v) and third party revenue from user information $( R _ { D } ) .$

(ii) $\boldsymbol { P } _ { \boldsymbol { W } } ^ { * }$ increases with user privacy concerns (v) and publisher website differentiation (t). $\boldsymbol { P } _ { \boldsymbol { W } } ^ { * }$ decreases with third party revenue from user information $( R _ { D } ) ,$ , total number of potential users $( M _ { U } )$ , and total number of potential third parties $( M _ { D } )$

Proposition 1 provides several important insights. As seen in part (i), when users’ privacy concerns are high, the publisher sets a high royalty price for its website resulting in decreased third party participation and user information sharing. The royalty price, in this sense, is a lever for the publisher website to manage the number of third parties. For a publisher whose website users are more concerned about their privacy, or who have sensitive information, the publisher reduces the amount of privacy violation through an increase in website royalties. This demand control mechanism can be observed when the publisher charges higher prices for presenting fewer ads on its website (Moss 2014).

On the other hand, when the revenue that the third party can make from user information increases, the third parties will be willing to pay more royalties to participate on the website. For example, the expected value of a purchase referral for an automobile sale increases when the purchase intent certainty is higher. When a user searches on publisher websites such as Edmunds.com, it is a very good indication that the user is in the market for an automobile, and the publisher can charge the third party a high price for this lead generation. This lead generation phenomenon can also be observed in advertising keyword pricing such as Google’s AdWords, where insurance, loans, and mortgage keyword searches demand high prices (Wordstream 2011).

From part (ii), we observe that the publisher increases the price for its website as users’ privacy concerns increase. The reason for this is that, as we see in part (i), an increase in user privacy concerns will cause the publisher to reduce third party usage for its website through increased royalties. This causes fewer third parties to participate on the website (as is shown in Proposition 2). On the other hand, because of the lower number of third parties participating on the publisher website, users enjoy higher utility and thus have a higher willingness to pay. So the publisher can increase its subscription price for the website. This describes a natural phenomenon wherein if the publisher cannot a make profit from third parties on its website, it needs to increase the user subscription price, which reduces the publisher website user base. This can be seen with publisher websites that require a payment in order to remove advertisement from their page. For example, The Washington Post, Forbes, and Wired Magazine ask users who use ad blockers to either pay a certain fee or subscribe in order to be able to use the services on the website (Barr 2016). This can also be construed as the fee for not having user’s information shared with advertising third parties.

The price also increases with publisher website differentiation (Hotelling’s fit parameter, t). This is intuitive, because as the differentiation increases, publisher websites move toward monopolies, and can charge higher prices for users. The implication of this is that when publisher website operates in markets without real competitors, the publisher can set high user subscription prices. As the market expands and new competitors enter the market, the business model of the publisher for its website transforms to no-fee subscription, and it focuses on revenue from third parties.

The publisher’s optimal user subscription price for its website will decrease if the third party’s revenue from users increases. In this case, the third party can obtain higher revenue from user information, thus the third party is willing to pay higher royalties to the publisher. At the same time, more users are willing to use the publisher website if the price is lower. Essentially, the publisher increases user participation on its website by dropping its prices, and monetizes the users through third parties. The example of valuable advertising keywords (Wordstream 2011) applies to this case as well, where high expected value of user information may enable the publisher to forgo the subscription fee for website users for higher returns from the third party.

The effect of dropping the price of one side to monetize the other side is previously seen in two-sided market models where positive network effects are present among both sides, and is known as cross-sided network effect (Eisenmann et al. 2006). Here, we find that the effect is also present in a twosided market model with both positive and negative crosssided network effects.

The publisher website price decreases with the total number of potential users in the market. Based on this, we expect that publishers with specialized and small user bases would set high subscription prices for their websites. In contrast, publishers with more generalized appeal and larger audiences would set low (or zero) subscription price for their websites and rely on lead generation and revenue from third parties instead. Figure 2 summarizes the findings in Proposition 1.

![](/api/attachments/Y8D6J3HA/fulltext/images/f863ac25724133678626515e9ca737f5aec5c629796b79744c39b4fa0f58e998.jpg)  
Figure 2. Effect of Model Parameters on Optimal Publisher Website Decision Variables

## Number of Third Parties

By substituting the optimal formula for $\boldsymbol { R } _ { \boldsymbol { W } } ^ { * }$ and $\boldsymbol { P } _ { \boldsymbol { W } } ^ { * }$ from Lemma 1 into equations (7) and (8), the optimal number of users and third parties on publisher websites can be obtained. For the number of users, the assumption is that the market is covered, and each user in the market is served by exactly one of the two publisher websites. Thus, the sum of number of users on the two publisher websites is equal to the total number of users, that is, $N _ { U _ { i } } ^ { * } + N _ { U _ { - i } } ^ { * } = M _ { U }$ and we have

$$
N _ {U _ {i}} ^ {*} = N _ {U - i} ^ {*} = N _ {U} ^ {*} = \frac {M _ {U}}{2}\tag{12}
$$

On the other hand, third parties can participate in none, one, or both websites. The following proposition provides the effect of model parameters on the number of third parties.

Proposition 2 The optimal number of third parties on publisher website i, $\boldsymbol { N } _ { D _ { i } } ^ { * }$ is calculated as follows:

$$
N _ {D _ {i}} ^ {*} = N _ {D _ {- i}} ^ {*} = N _ {D} ^ {*} = M _ {D} \frac {M _ {U} (R _ {D} - v)}{4 \Phi} \geq 0\tag{13}
$$

The following results hold for the optimal number of third parties on the publisher website: $N _ { D } ^ { * }$ decreases with users’ privacy concerns (v) and maximum third party fixed cost (Φ), while it increases with third party revenue from users $( R _ { D } ) ,$ the total number of potential users in the market ${ ( M _ { U } ) } ,$ , and the total number of potential third parties in the market $( M _ { D } )$

Note that in (13) we assume that $R _ { D } - \nu \geq 0$ , and we further assume that $R _ { D } - \nu > 0$ , so that there are a positive number of third parties present on the publisher website. Additional third parties pose risks to user privacy being violated and user information being misused. Thus, publisher websites that deal with sensitive user information would tend to do most of their operations themselves, rather than engaging third parties. We would expect publisher websites dealing with sensitive content to work with substantially fewer third parties. Figure 3 summarizes findings in Proposition 2.

## Results and Analysis

## Effect of User Privacy Concerns on Stakeholders

In this section we discuss how the model parameters affect third party usage behavior. Proposition 3 examines the effect of privacy concerns on publisher websites, users, and third parties. An extension of this proposition, which considers the effect of other model parameters on stakeholders is provided in the Appendix B.

Proposition 3 In equilibrium, the duopolistic publisher sets the optimal royalty $( R _ { W } ^ { * } )$ and optimal price $( P _ { w } ^ { * } ) f o r$ its website so as to maximize its profit, which yields optimal publisher website profit $( \pi _ { w } ^ { * } )$ , user surplus $( Z _ { U } ^ { * } )$ , and third party surplus $( Z _ { D } ^ { * } )$ as follows:

![](/api/attachments/Y8D6J3HA/fulltext/images/af7f242f90b462a21b3bcc5236397054cf013f402148b1935648693e91b4cb4e.jpg)  
Figure 3. Effect of Model Parameters on Optimal Number of Users and Third Parties

$$
\Pi_ {W _ {i}} ^ {*} = \Pi_ {W _ {- i}} ^ {*} = \Pi_ {W} ^ {*} = \frac {M _ {U} \left(8 \Phi t - M _ {U} M _ {D} (R _ {D} - 3 v) (R _ {D} - v)\right)}{1 6 \Phi}\tag{14}
$$

$$
Z _ {U} ^ {*} = \frac {\Phi (4 X - 5 t) + M _ {U} M _ {D} (R _ {D} - 2 v) (R _ {D} - v)}{4 \Phi}\tag{15}
$$

$$
Z _ {D} ^ {*} = \frac {M _ {U} {} ^ {2}}{1 6} (R _ {D} - v) ^ {2}\tag{16}
$$

The following holds for optimal publisher website profit $( \pi _ { w } ^ { * } )$ user surplus $( Z _ { U } ^ { * } )$ , and third party surplus $( Z _ { D } ^ { * } )$

(i) When $\nu < \frac { 2 } { 3 } R _ { D }$ profit for each publisher website $( \pi _ { w } ^ { * } )$ increases with user privacy concern (v) and when $\begin{array} { r } { \frac { 2 } { 3 } R _ { D } < \nu < R _ { D } } \end{array}$ it decreases with user privacy concern (v).

(ii) When $\textstyle \nu < { \frac { 3 } { 4 } } R _ { D }$ user surplus $( Z _ { U } ^ { * } )$ decreases with user privacy concern $( Z \nu )$ and when $\begin{array} { r } { \frac { 3 } { 4 } R _ { D } < \nu < R _ { D } } \end{array}$ it increases with user privacy concern (v).

(iii) Third party surplus $( Z _ { D } ^ { * } )$ decreases with user privacy concern (v).

Figure 4 provides the effect of model parameters on the stakeholders.

Part (i) of the Proposition 3 provides that when the privacy concerns of users are relatively small (relative to the revenue that third parties make from user information), then publisher website profits increase as user privacy concerns increase. However, above a threshold, the profit decreases with an increase in privacy concern. This implies that it is beneficial for the publisher website to have users with a moderate amount of privacy concerns. When user privacy concerns are too high, the publisher website may not have the option of selling user information to the third parties, due to possible backlash from users. For example, Quintin (2015) reported that Healthcare.gov shared very personal information such as user zip codes, income levels, smoking status, pregnancy status and others. When this was uncovered and published by a privacy watchdog, there was a backlash from users who demanded that the practice be stopped, and Healthcare.gov quickly discontinued the user information sharing. On the other hand, when user privacy concerns are on the low side, then users may not be willing to pay for publisher website subscription fees. From (ii) it can be seen that when user privacy concerns are relatively low, the user surplus actually decreases with privacy concerns. However, when user privacy concerns are relatively high, then it is beneficial for users to have higher privacy concerns. In other words, the user surplus is convex with respect to user privacy concerns. The implication of this finding is that it is best for users if their privacy concerns are either very low, or very high. The results from (iii) are intuitive, as the third parties utilize user information, and if the users are concerned about this, the publisher’s response would be to cut the third party usage on its website, and this would hurt the third parties.

![](/api/attachments/Y8D6J3HA/fulltext/images/4b5dbbad7fed5848c1a7a463708b3d5a11e98a1a9657c7de373c29f96adc1f62.jpg)  
Figure 4. Effect of of User Privacy Concerns on Stakeholders

## Asymmetry in User Privacy Concerns

Until now, we have considered symmetric publisher websites. In reality, publisher websites may face different user privacy concerns, perhaps as a result of differing brand reputations or sensitivity of user information. In this section we numerically examine the asymmetric version of the base model with respect to privacy concerns. The details of the asymmetric model are provided in Appendix C. We assume that the privacy concern for publisher websites 1 and 2 are v and $\nu _ { 2 } ,$ respectively. Here, we analyze the effect of changes in each publisher’s user privacy concerns on royalties and prices, the number of users, the number of third parties, and profit for its website. We analyze these for a numerical example in Figure 5, where the privacy concern for publisher website 1 varies over the range 1 to 9, while the privacy concern for publisher website 2 is held constant at $\nu _ { 2 } = 4$

As shown in Figure 5a, publisher 1’s website royalty increases as privacy concerns of its users increase, but it does not change for publisher 2’s website. Figure 5b provides that publisher website price is a nonlinear combination of both publishers’ user privacy about its website concerns. Publisher 1 will charge higher prices for its website as user privacy concerns increase. Changes in publisher 1’s website user privacy concerns also affect publisher 2’s website prices, as publisher 2’s website price initially increases and then decreases as publisher 1’s website user privacy concerns increase.

As seen in Figures 5c and 5d, the optimal number of users and third parties declines for publisher 1’s website and increases for publisher 2’s website over the entire test range. The combined effect of changes in both price and quantity is illustrated in publisher website profit, as presented in Figure 5e. When publisher 1’s user privacy concerns increase, its profit declines. However, publisher 2’s website profits are also impacted by increases in publisher 1’s website user privacy concerns, as their profits initially increase, and then decrease.

Sufficiently asymmetric user privacy concerns result in two different business models for the publisher websites. When publisher 1’s user privacy concerns are high, its website has a smaller niche market of customers willing to pay high publisher website prices in exchange for privacy protection. Publisher 2’s website, which faces relatively lower user privacy concerns, has a larger mass market of customers who are willing to have their privacy violated in exchange for lower publisher website prices. The key insight is that different user privacy concerns faced by firms cause different business models to be adopted. In this sense, business model adoption can be seen, at least in part, as a reaction to the user privacy concerns each firm faces in the environment.

## Effect of User Privacy Concerns on Third Party Market Concentration

Regulators are concerned about high industry concentration within third parties, especially with respect to concentrated user information and the possibility of re-identification. In a similar situation of concentrated user information, although in a different context, the Office of the Privacy Commissioner of Canada (OPC) ruled that Bell Canada’s tracking of users’ smartphone activity on an opt-out basis, rather than on an optin basis, was a violation of users’ privacy due to inadequate consent (Dobby 2015). We can see from the Bell Canada case that high industry concentration of users’ information, especially without their knowledge or adequate consent, would be of great concern to regulators and privacy watchdogs. A more comprehensive user profile has greater value in terms of the potential to exploit users through the publisher’s improved ability to reidentify users on its website and combine user information. Thus, higher industry concentration as a result of user information being sent to a few third parties from many publisher websites constitutes a serious privacy concern. In this section, we analyze the effect of privacy concerns on third party market concentration.

![](/api/attachments/Y8D6J3HA/fulltext/images/5557fb2f2cf95eeaa2e9efd40441ddc31644e20e854fc804d53dd369b79be5e4.jpg)

![](/api/attachments/Y8D6J3HA/fulltext/images/a4601950fc1f6168cc87e137e85e7553bd99e98f82b35ebc4e0657df83c9a2bf.jpg)  
(b) Optimal Publisher Website Prices

(a) Optimal Publisher Website Royalties  
![](/api/attachments/Y8D6J3HA/fulltext/images/7bd0c1504ca2cafdfefddd41070b654eb5a42f5426cd55ae4e8eb8afb472e026.jpg)  
(c) Optimal Number of Users

![](/api/attachments/Y8D6J3HA/fulltext/images/ef26fca69b46a217696a12fe4382ab0aa32299a29787920dffa6f09356b27631.jpg)

(d) Optimal Number of Third Parties  
![](/api/attachments/Y8D6J3HA/fulltext/images/e5b5f3985e77c3df671ffc7f2f22b7d0e6a99f476094cf4531415d40bedf4926.jpg)  
(e) Optimal Publisher Website Profits  
Figure 5. Effect of Changes in v<sub>1</sub> When v<sub>2</sub> = 4 on the Two Publisher Websites

In studying third party market concentration, we consider two cases: third parties with homogenous shares of the market and third parties with nonhomogenous shares of the market. We use the Herfindahl-Hirschman Index (HHI) as a recognized measure for market concentration. Here, we report only the main result of the analysis, and the details of the calculations are provided in Appendix D. We find that for the homogeneous market share case, the market concentration increases with user privacy concerns. We also find that higher barriers to entry, such as an increase in the minimum allowable privacy and security level of the third parties, will also result in fewer third parties (by definition) and higher industry concentration.

Next, we reconsider the asymmetric model described in “Asymmetry in User Privacy Concerns” section, where user privacy concerns for the two websites are not necessarily equal. We use the number of third parties on the two publisher websites to calculate the third party market shares. In analyzing the findings in Appendix D, we note that the HHI in the nonhomogeneous case is affected by two factors. First, HHI depends on the number of third parties, consistent with the homogenous case. As can be seen from Figure 5d in the previous section, the net effect of an increase in publisher 1’s website user privacy concerns is that the total number of third parties decreases, and thus the HHI would increase as publisher 1’s website user privacy concerns increase. Second, HHI also depends on the market share of third parties, and this is impacted by the differences in the number of websites that each third party serves. We find that the HHI is maximized when the number of third parties on the two websites are slightly different.

## Implications for Policymakers: Taxation

In this section we consider the effect of regulatory organizations that can force taxes on users or third parties. We consider symmetric taxes, that is royalty and price taxes that are the equal for both publisher websites. We model this by performing the following transformations in the base model. The changes are made to the user utility equations (1) and (2) and third party profit equation (5), but not to the publisher profit equation (9). Taxes on royalties and on prices are shown by $T _ { R _ { W } }$ and $T _ { P _ { W } }$ , respectively.

$$
P _ {W _ {i}} \rightarrow P _ {W _ {i}} \left(1 + T _ {P _ {W}}\right) \quad \forall i = 1, 2 \quad - 1 <   T _ {P _ {W}} <   1\tag{17}
$$

$$
R _ {W _ {i}} \rightarrow R _ {W _ {i}} \left(1 + T _ {R _ {W}}\right) \quad \forall i = 1, 2 \quad - 1 <   T _ {R _ {W}} <   1\tag{18}
$$

The taxation can represent risk reserves that might be set by policymakers to be used in the case of an adverse incident, or can be seen as setting standards on information handling that might make the transactions harder and more costly. The taxation can also take negative values, meaning that the policymaker can take action to make the processes easier or less costly through subsidies. Lemma 2 provides the optimal publisher website royalty and price when these taxations are included in the base model.

Lemma 2 When taxations are possible, the publisher websites in duopoly choose the following royalties and publisher website price in equilibrium:

$$
R _ {W _ {i}} ^ {*} = R _ {W _ {- i}} ^ {*} = R _ {W} ^ {*} = \frac {R _ {D} \left(1 + T _ {P _ {W}}\right) + v \left(1 + T _ {R _ {W}}\right)}{2 \left(1 + T _ {P _ {W}} + T _ {R _ {W}} + T _ {P _ {W}} T _ {R _ {W}}\right)} \geq 0\tag{19}
$$

$$
P _ {W _ {i}} ^ {*} = P _ {W _ {- i}} ^ {*} = P _ {W} ^ {*} = \frac {4 \Phi t (1 + T _ {P _ {W}}) (1 + T _ {R _ {W}}) - M _ {D} M _ {U} (R _ {D} (1 + T _ {P _ {W}}) - v (1 + T _ {P _ {W}})) ^ {2}}{4 \Phi (1 + T _ {P _ {W}}) ^ {2} (1 + T _ {P _ {W}})} \geq 0\tag{20}
$$

The proof for this Lemma follows the proof for Lemma 1, and by making transformation (17) in user utility equations (1) and (2), and transformation (18) in third party profit equation (5). Using Lemma 2, Proposition 4 provides the effect of taxations on the publisher website decision variables of optimal publisher website royalty and price.

## Proposition 4

(i) The optimal royalty price $( R _ { W } ^ { * } )$ decreases with taxation on third party royalties $( T _ { R _ { W } } )$ and publisher website price $( T _ { P _ { W } } )$

(ii) The optimal publisher website price $( P _ { w } ^ { * } )$ increases with taxation on third party royalties $( T _ { R _ { W } } )$ and decreases with taxation on publisher website price $( T _ { P _ { W } } )$

Proposition 4 yields several interesting insights. The publisher will decrease the royalty price of its website as a response to taxation on user revenues. The intuition for this is that taxation on the subscription price will reduce the number of users on the publisher website. In order to maximize profit, the publisher increases the number of third parties on its website by reducing the royalties, and this increases the publisher’s website profit from third parties. Similarly, the publisher will decrease the royalty price of its website as a result of taxation on third party revenues. Due to reduced third party interest because of taxation, the publisher increases third party incentives to join its website by decreasing the royalties. The publisher tries to regain the lost demand due to taxation on user revenues through user price reductions for its website. However, the publisher will increase the price of its website as taxation on third parties increases. This is because taxation on third parties decreases the publisher’s website revenue from third parties, and the publisher tries to replenish this by increasing the user price. Figure 6 provides the effect of taxation on optimal publisher website royalty and price.

We next look at the effect of taxations on website profit, user surplus, and third party surplus in Propositions 5 and 6.

Proposition 5 When the publisher chooses royalty $( R _ { W } ^ { * } )$ and the optimal price $( P _ { w } ^ { * } ) f o r$ its website so as to maximize profit, then

(i) When $\nu < \frac { R _ { D } } { \sqrt { 3 } } \frac { 1 + T _ { P _ { W } } } { 1 + T _ { R _ { W } } }$ publisher website profit $( \pi _ { w } ^ { * } )$ increases with taxation on royalties $( T _ { R _ { W } } )$ and when $\begin{array} { r } { \frac { R _ { D } } { \sqrt { 3 } } \frac { 1 + T _ { P _ { W } } } { 1 + T _ { R _ { W } } } < \nu < 1 } \end{array}$ it decreases with taxation on royalties $( T _ { R _ { W } } ) .$

![](/api/attachments/Y8D6J3HA/fulltext/images/fc838dd00245afde4ce36d6fb99b1b96590d1aadc1d0051066157a007c6ada80.jpg)  
Figure 6. Effect of Taxation on Optimal Publisher Website Decision Variables

(ii) When $\nu < \frac { R _ { D } } { \sqrt { 2 } } \frac { 1 + T _ { P _ { W } } } { 1 + T _ { R _ { W } } }$ user surplus $( Z _ { U } ^ { * } )$ decreases with taxation on royalties $( T _ { R _ { W } } )$ , and when $\frac { R _ { D } } { \sqrt { 2 } } \frac { 1 + T _ { P _ { W } } } { 1 + T _ { R _ { W } } } < \nu$ < 1 it increases with taxation on royalties $( T _ { R _ { W } } ) .$

(iii) Total third party surplus $( Z _ { D } ^ { * } )$ decreases with taxation on royalties $( T _ { R _ { W } } ) .$

It can be seen from (i) that the taxation on royalties can increase or decrease the publisher website profit and user surplus, and this depends on the privacy concerns of the users. When users are not very concerned about their privacy, taxation can improve publisher website profit. However, if users are concerned about their privacy, then taxation would decrease publisher website profit.

The effect of taxation on users is the opposite of its effect on publisher websites. Taxation is beneficial for users with high privacy concerns, and is detrimental for users with low privacy concerns. Moreover, there is no range for privacy concerns in which the taxation on royalties can increase both publisher website profit and user surplus. Thus the regulator needs to decide which player they want to benefit, and the cost of doing that on the other player. Taxation on royalties always decreases the third party surplus.

Proposition 6 When the publisher website chooses royalty $( R _ { W } ^ { * } )$ and the optimal publisher website price $( P _ { W } ^ { * } )$ so as to maximize profit, then

(i) Publisher website profit $( \pi _ { w } ^ { * } )$ decreases with taxation on price $( T _ { P _ { W } } )$

(ii) When $\nu < \frac { R _ { D } } { \sqrt { 2 } } \frac { 1 + T _ { P _ { W } } } { 1 + T _ { R _ { W } } }$ user surplus $( Z _ { U } ^ { * } )$ increases with taxation on price $( T _ { P _ { W } } )$ , and when $\begin{array} { r } { \frac { R _ { D } } { \sqrt { 2 } } \frac { 1 + T _ { P _ { W } } } { 1 + T _ { R _ { W } } } < \nu < 1 } \end{array}$ it decreases with taxation on price $( T _ { P _ { W } } )$

(iii) Total third party surplus $( Z _ { D } ^ { * } )$ increases with taxation on price $( T _ { P _ { W } } ) .$

It can be seen that the price taxation decreases publisher website profit. Interestingly, price taxation can either increase or decrease user surplus. It increases user surplus when user privacy concerns are low, and it decreases user surplus when user privacy concerns are high. Thus while taxation on price does not benefit the publisher website, it does benefit users when their privacy concerns are low. Therefore, price taxation is a viable tool for benefitting the users when their privacy concerns are relatively low. The taxation on price always increases the third party surplus.

Figure 7 provides the summary of results from propositions 5 and 6.

## Implications for Policymakers: Collusion on Royalties

In this section we study the effect of collusion among publisher websites on the stakeholders. When firms collude in order to increase profits, they can set royalties and prices other than their equilibrium values. Since the duopoly market is covered in our model, analyzing collusion in prices does not provide interesting insights, and here we only look at the effect of collusion in terms of royalties.

In order to analyze the effect of setting royalties other than their equilibrium values, we look at the profits that publisher websites can obtain with and without collusion. For the case when collusion is not possible, we consider that publishers set royalties to equilibrium value. For the case of collusion, we consider that both publishers can collaboratively decide on website royalties. The details of the calculations are provided in Appendix E. The profit curves for the publisher websites with respect to royalties with and without collusion for a numerical example are provided in Figure 8.

![](/api/attachments/Y8D6J3HA/fulltext/images/2a3429ffd23c4586e9480eac2ffc1cf42d87e5147fce8d780fc715b9173e12a3.jpg)  
Figure 7. Effect of Taxation on Stakeholders

![](/api/attachments/Y8D6J3HA/fulltext/images/beb9ff07ff57ee961f8797e85a05c914d40f87cc920415c8fc148028703db42e.jpg)  
Figure 8. Publisher Website Profit with and Without Collusion with Respect to Royalties

The dashed line is the profit for publisher websites, when one publisher sets the equilibrium royalties to $R _ { W _ { E q } }$ and the other publisher sets royalties to $R _ { W } .$ The profit in this case is maximized at the equilibrium point, $R _ { W _ { E q } }$ . However, if the publishers can collude and set identical royalties of $R _ { W }$ , then they will decrease their royalty to $R _ { W _ { C o l . } }$ , where both firms make higher profits $\left( \Pi _ { W _ { R _ { W _ { C o l . } } } } \right)$ than the equilibrium profit $\left( \Pi _ { W _ { R _ { W _ { E q . } } } } \right)$ . It can analytically be shown that these results hold irrespective of the parameters (refer to Appendix E). In other words, the following hold:

$$
R _ {W _ {E q.}} > R _ {W _ {C o l.}}\tag{21}
$$

$$
\Pi_ {W _ {R W _ {E q.}}} <   \Pi_ {W _ {R W _ {C o l.}}}\tag{22}
$$

The collusion among publishers results in lower website royalties overall, and thus is also beneficial for the third parties. This collusion, however, is not beneficial for the users, as they will be exposed to more third parties due to the decrease in $R _ { W }$ Intuition behind this can be explained as follows. The competition among the two publishers for attracting users to their websites drives them to increase the royalties, as increasing royalties benefits user utility through the reduced number of third parties (and hence lower privacy concerns for users). If both publisher websites can simultaneously reduce royalties through regulation or collusion (which simultaneously reduces user utility), then publisher website profits can be maximized and third party surplus will increase. The role of a regulatory organization interested in increasing user surplus would be to prevent such collusion, possibly by setting minimum required royalties. Note that this regulatory mechanism behaves differently than royalty taxation in terms of the effects on publisher website profit, third party surplus, and user surplus.

## Robustness Check

In this section, we test the robustness of the model that was presented in the paper. We compare the base duopoly model to a duopoly model with a nonlinear utility function for users, and to a monopoly version of the model.

## Duopoly Model with Nonlinear Utility Functions

Here, we test a nonlinear utility function for users, and transform the user utility functions (1) and (2) as follows:

$$
U _ {1} (y) = u _ {1} - t y \qquad \qquad u _ {1} = X - N _ {D _ {1}} ^ {2} v - P _ {W _ {1}}\tag{23}
$$

$$
U _ {2} (y) = u _ {2} - t \bigl (1 - y \bigr) \qquad u _ {2} = X - N _ {D _ {2}} ^ {2} v - P _ {W _ {2}}\tag{24}
$$

This is the case when the users get exponential disutility from the presence of third parties on the publisher website. Solving the problem with a nonlinear utility function is not tractable; however, it can be solved numerically. We use numerical analysis to test if the main results that were derived from the duopoly model hold for this model as well. We report the key results from the analysis, and provide the details of the numerical results in Appendix F. We find that the publisher website decision variables of royalties and prices in the model with nonlinear utility behave similarly to the base model. Specifically, the optimal publisher website royalties increase with user privacy concerns and third party revenue from user information, and the optimal publisher website prices increase with user privacy concerns and decrease with third party revenue from user information. Similar to the base model, the number of third parties decreases with user privacy concerns and increases with third party revenue from user information.

The two models, however, differ in terms of the effects on publisher website profit, and user and third party surplus. Generally, the two models yield similar results for the higher range of user privacy concerns; however, the nonlinear model does not account for the effects on publisher website profit and user surplus for small values of user privacy concerns.

Overall, we conclude that the base model is robust, in that the main findings are unchanged when modeling with a nonlinear utility function.

## Monopoly Model

We have also compared the monopoly and duopoly cases. In the monopoly, there is no Hotelling’s fit cost (t); instead, the users are differentiated based on their intrinsic utility for the publisher website, x, assuming it to be uniformly distributed between 0 and X. The details of the monopoly and its comparison with duopoly are provided in Appendix G. Comparing the monopoly model to the duopoly, we find that the decision-making behavior of the publishers regarding their websites is similar in both models, in that the effect of user privacy concerns on the royalties and prices are similar to the base model. The number of third parties on the publisher websites also behave similar to the duopoly model. For the number of users, while in the duopoly the market is covered, it may not be covered in the duopoly, and thus the results differ. The duopoly model enables us to study the effect of competition through the Hotelling’s fit cost parameter.

The results on publisher website profit, user surplus, and third party surplus between duopoly and monopoly models are different, yet consistent in behavior. Similar to what we saw with the model with nonlinear utility function, the monopoly model does not account for effects on publisher website profit and user surplus for small values of user privacy concerns.

## Empirical Analysis

We find partial support for the proposed model by empirically examining the number of third parties utilized by different categories of publisher websites, as well as the industry concentration of third parties. We carry out an exploratory validation study on the 100 most-visited publisher websites from seven different publisher website subject categories (news, arts, shopping, kids and teens, health, business, and adult). We record the third parties utilized on each website. To better capture the structure of the third party industry, we profile the third parties and divide them based on the industry sectors. The three industry sectors are targeting/advertising (T/A, e.g., advertising presentation, and analytics), functionality (F, e.g., password security, social media integration, video hosting, chat and forum services, and payment services), and performance (P, e.g., backup service, publisher website security, and responsiveness tools). Appendix H provides the details of empirical analysis and model validation.

Many outcomes of the model are not empirically observable in our validation study. We can, however, make predictions regarding user privacy concerns in different publisher website subject categories, and observe and compare the number of third parties and industry concentration among these categories. If the empirical study is consistent with our a priori expectations from the model, then we can conclude that the model is partially validated. Figure 9 illustrates our expectations regarding empirical observations based on the analytic model.

![](/api/attachments/Y8D6J3HA/fulltext/images/5556bb1a62d657f18ea4019ad5e715b7e3617f5e1cfe710f9dccba834451b3fe.jpg)  
Figure 9. Outline of Conjectures for Empirical Validation

Noting that information sensitivity and user privacy concerns likely vary among different content subject categories, we expect the sharing behavior to differ for publisher websites with different subject categories. Looking at the three industry sectors, we find the number of third parties used in the T/A industry sector to be significantly higher than both F and P. The F sector has significantly higher sharing than P in three out of the seven subject categories, and overall. The T/A, F, and P sectors comprise 60%, 20%, and 15% of all third party connections. Thus, sharing across different third party sectors varies. The results suggest that user information is falling into the hands of many companies who use the information for targeting, lead generation, and advertising purposes, which provides credence to concerns raised in the literature (e.g., Krishnamurthy and Wills 2006; Mikians et al. 2012; Valentino-DeVries et al. 2012).

In terms of publisher website subject categories, news is the category that shares with the greatest number of third parties. Note that while the publisher’s website business model is beyond the scope of this study, it may influence the use of third parties. In the case of news, the industry has a history of revenues coming from both advertising and subscription fee business models, and in many cases, publisher websites such as The Los Angeles Times and The New York Times employ a mixed, or freemium, model (e.g. 5 free articles per month for The Los Angeles Times and 10 free articles per month for The New York Times). On the other hand, the adult subject category has the least average sharing, followed by business and health for all three industry sectors (T/A, F, and P). Specifically, health websites obtain sensitive information (Quintin 2015), which is typically associated with higher privacy concern for users. These observations support the findings of the model that predicts that sharing should be lower for publisher website categories where users’ privacy concerns and information sensitivity are greater.

We also examine the third party market concentration using Herfindahl-Hirschman index. We find that the T/A sector has the lowest HHI concentrations, followed by P, and then by F for all subject categories analyzed separately. There are relatively fewer third parties in F and P sectors, and the HHIs indicate that these industry sectors have a higher number of large, dominant third parties. The market concentration results are also in tandem with findings of the model, where categories with higher privacy concerns are found to have a higher HHI. We do not find evidence for the popularity of publisher websites (as measured by monthly unique visitors) to have any significant effect on third party sharing.

The T/A sector is clearly dominant in terms of number of third parties involved. One reason behind this is that the information involved in T/A sector is perhaps less sensitive than the F and P sectors. Publishers tend to stick with a smaller number of third parties in the F and P sectors. It is safe to assume that privacy concerns play an important role in the sharing behavior within each sector. Another reason could be that more money is potentially available for T/A versus F and P.

## Conclusions and Directions for Future Research

In this paper, we present a two-sided economic model to explain and analyze the decision-making of publishers who must balance user pricing and privacy on their websites. The publisher needs to maintain its user base to increase profits. However, publishers have a secondary source of profit from third parties. A publisher must balance this with monetization through third party information sharing and the subsequent personal privacy violations that result from this sharing, along with the associated declines in the user base due to third party monetization. The model describes how user privacy concerns drive publisher website decision-making and third party market structures, with higher privacy concerns driving higher industry concentration. We also look at the effect of competition and asymmetry among publisher websites, and provide insights on the different publisher website business models that arise. We also provide several policy and welfare implications, and analyze the effect of regulatory decisions such as taxation and setting minimum royalties on the stakeholders.

This paper makes several important contributions to our understanding of the publisher website third party sharing problem. An important implication is that firms facing different user privacy concerns can be driven to one of two business models: (1) low publisher website price and high user privacy violation for the firm facing low user privacy concerns, and (2) high publisher website price and low user privacy violation for the firm facing high user privacy concerns. The empirical results are consistent with this finding.

We also show how increased user privacy concerns decrease the number of third parties utilized by publisher websites, and how this in turn can lead to a substantially higher third party industry concentration. These higher industry concentrations represent an irony with respect to the impact of user privacy concerns on publisher website third party usage. When privacy concerns are relatively high, such as for the health and business categories, the publisher makes use of fewer third parties. This is shown to cause higher industry concentration among the third parties. Thus, if a user visits multiple publisher websites in a category with high privacy concerns, then the user’s data is more likely to be aggregated among this smaller number of third parties. This concentration of information sharing constitutes a privacy threat in its own right, due to concerns regarding re-identification and aggregation of data. We validate some key outcomes of the model with an empirical validation study which confirms these key model outcomes regarding user privacy concerns, third party utilization, and industry concentration.

In the empirical study, we find that user information is being shared extensively among third parties by publisher websites, and the actual third party usage behavior is consistent with the predictions of the model. Due to privacy concerns and potential for re-identification, the extent of third party sharing is of strong interest to policy makers and regulatory organizations. Also, from the point of view of the publisher’s website administrator, sharing generates ad revenue and potentially better service. However, too much sharing will violate user privacy and reduces usage. We see these market forces being reflected in sharing levels and industry concentration measures between industry sectors and subject categories.

We examine the impact of two government taxation policies (taxation on royalty revenues and taxation on subscription revenues), and find that the impacts of a sales tax on the activity between the user and the publisher website differ from a tax on the third party activity. Profit and welfare impacts of these two taxation policies are examined. We find that the impact of such actions depends on the level of user privacy concerns and the goal of the policy makers.

We contribute to the two-sided market literature by considering the case where one side has a negative crosssided network effect. Traditionally, with the exception of Casadesus-Masanell and Hervas-Drane (2015), cross-sided network effects are positive for both sides (e.g., Anderson et al. 2013; Eisenmann et al. 2006; Parker and Van Alstyne 2005; Rochet and Tirole 2003). In two-sided markets where cross-sided network effects are positive for both sides, a common strategy is to drop the price to one side in order to monetize the other. We illustrate that this strategy remains effective when one side has a negative cross-sided network effect as well. In our problem, where users have negative cross-sided network effects from third parties, the publisher can decrease website revenue from users in order to monetize the third parties. Conversely, the publisher’s website strategy could be to decrease third party privacy violations, which decreases the revenue from third parties, and increases the revenues from users.

There are several limitations to this research. Note that different business models may cause one publisher website category to dominate another. The concern is that differences in third party sharing may be due to differing business models, rather than users’ privacy concerns related to the nature of the publisher website subject. While we try to avoid this issue by considering the decision making only from the privacy point of view, focusing on both the business model and privacy concerns can be a good avenue for future research. We also recognize the limitation in the exploratory validation study with respect to the business model issue. The impact of business model design on third party utilization is beyond the scope of this study, and thus our economic model is limited to the impact of privacy concerns on third party information sharing.

In the case of advertising third parties, the third parties are often the ad serving companies such as Google and Yahoo, and not the advertisers whose ad is being shown. So while the publisher websites do not select the advertisers, they select the third parties that manage these ads. Our model treats all third parties equally, but in reality not all third parties are identical in their level of advertising or their amount of abuse of user privacy. Treating all third parties identically is a simplification for the model, but we believe this simplification does not impair the current analysis. The treatment of third parties as nonhomogeneous remains a topic for future research.

Additionally, this study only examines direct information sharing and selling. User data is sold and resold, potentially making the problem much worse than what is modeled in this paper. Because we do not consider the interaction effect between third parties, our paper represents a lower bound on the problem, with the likelihood that results found with the model are understated. We leave the interaction among third parties for future research. Another avenue for future research would be to consider third parties that provide some service to users, and thus would actually increase user utility to some degree.

## References

Adler, M., Gibbons, P. B., and Matias, Y. 2002. “Scheduling Space Sharing for Internet Advertising,” Journal of Scheduling (5:2), pp. 103-119.

Anderson Jr., E. G., Parker, G. G., and Tan, B. 2013. “Platform Performance Investment in the Presence of Network Externalities,” Information Systems Research (25:1), pp. 152-172.

Barr, J. 2016. “The New York Times Begins Testing Ad Blocking Approaches, Ad Age,” The New York Times (http://adage.com/ article/media/york-times-a-message-ad-blockers/302995/; accessed April 5, 2016).

Casadesus-Masanell, R., and Hervas-Drane, A. 2015. “Competing with Privacy,” Management Science (61:1), pp. 229-246.

Chellappa, R. K., and Shivendu, S. 2007. “An Economic Model of Privacy: A Property Rights Approach to Regulatory Choices for Online Personalization,” Journal of Management Information Systems (23:4), pp. 193-225.

Chen, J., and Stallaert, J. 2014. “An Economic Analysis of Online Advertising Using Behavioral Targeting,” MIS Quarterly (38:2), pp. 429-449.

Dobby, C. 2015. “Bell Retreats from Online Tracking Policy,” The Globe and Mail, April 7 (http://www.theglobeandmail.com/ report-on-business/privacy-watchdog-urges-bell-to-change-webtracking-policy/article23822585/; retrieved April 9, 2015).

Eisenmann, T., Parker, G., and Van Alstyne, M. W. 2006. “Strategies for Two-Sided Markets,” Harvard Business Review (84:1), pp. 92-101.

Gopal, R., Hidaji, H., Patterson, R. A., Rolland, E., and Zhdanov, D. 2014. “Information Sharing in Web Services: An Exploratory Analysis,” in Proceedings of the 24<sup>th</sup> Workshop on Information Technology and Systems, December 17-19, Auckland, New Zealand.

Helft, M., and Vega, T. 2010. “Retargeting Ads Follows Surfers to Other Sites,” The New York Times, August 29 (http://www. nytimes.com/2010/08/30/technology/30adstalk.html?\_r=0; accessed June 11, 2016).

Krishnamurthy, B., Malandrino, D., and Wills, C. E. 2007. “Measuring Privacy Loss and the Impact of Privacy Protection in Web Browsing,” in Proceedings of the 3<sup>rd</sup> Symposium on Usable Privacy and Security, New York: ACM, (pp. 52-63.

Krishnamurthy, B., Naryshkin, K., and Wills, C. 2011. “Privacy Leakage Vs. Protection Measures: The Growing Disconnect,” in Proceedings of the Web2.0 Security and Privacy Workshop (Vol. 2), pp. 1-10.

Krishnamurthy, B., and Wills, C. E. 2006. “Generating a Privacy Footprint on the Internet,” in Proceedings of the 6<sup>th</sup> ACM SIGCOMM Conference on Internet Measurement, New York: ACM, pp. 65-70.

Krishnamurthy, B., and Wills, C. E. 2009a. “On the Leakage of Personally Identifiable Information via Online Social Networks,” in Proceedings of the 2<sup>nd</sup> ACM Workshop on Online Social Networks, New York: ACM, pp. 7-12.

Krishnamurthy, B., and Wills, C. 2009b. “Privacy Diffusion on the Web: A Longitudinal Perspective,” in Proceedings of the 18<sup>th</sup> International Conference on World Wide Web, New York: ACM, pp. 541-550.

Kumar, S., and Sethi, S. P. 2009. “Dynamic Pricing and Advertising for Web Content Providers,” European Journal of Operational Research (197:3), pp. 924-944.

Li, Y. 2012. “Theories in Online Information Privacy Research: A Critical Review and an Integrated Framework,” Decision Support Systems (54:1), pp. 471-481.

Malandrino, D., and Scarano, V. 2013. “Privacy leakage on the Web: Diffusion and Countermeasures,” Computer Networks (57:14), pp. 2833-2855.

Mayer, J. R., and Mitchell, J. C. 2012. “Third-Party Web Tracking: Policy and Technology,” in Proceedings of the 2012 IEEE Symposium on Security and Privacy, Los Alamitos, CA: IEEE, pp. 413-427.

McDonald, A. M., and Cranor, L. F. 2010. “Beliefs and Behaviors: Internet Users’ Understanding of Behavioral Advertising,” in Proceedings of the 2010 Research Conference on Communication, Information and Internet Policy.

Mikians, J., Gyarmati, L., Erramilli, V., and Laoutaris, N. 2012. “Detecting Price and Search Discrimination on the Internet,” in Proceedings of the 11<sup>th</sup> ACM Workshop on Hot Topics in Networks, New York: ACM, pp. 79-84.

Moss, L. 2014. “Publishers Try Crazy Ideas: Fewer Ads, Higher Pricing,” Digiday (http://digiday.com/publishers/publishersforegoing-online-ads/; accessed April 5, 2016).

New York Times. 2016. NYT Subscription Options (http:// international.nytimes.com/subscriptions/inyt/lp87JWF. html?currency=loonie&adxc=277709&adxa=406555& page=homepage.nytimes.com/index.html&pos=Bar1& campaignId=4L9XJ; accessed March 8, 2016).

Parker, G. G., and Van Alstyne, M. W. 2005. “Two-Sided Network Effects: A Theory of Information Product Design,” Management Science (51:1), pp. 1494-1504.

Quintin, C. 2015. “HealthCare.gov Sends Personal Data to Dozens of Tracking Websites,” Electronic Frontier Foundation (https://www.eff.org/deeplinks/2015/01/healthcare.gov-sendspersonal-data; retrieved April 4, 2015).

Rochet, J. C., and Tirole, J. 2003. “Platform Competition in Two Sided Markets,” Journal of the European Economic Association (1:4), pp. 990-1029.

Schoen, S. 2009. “New Cookie Technologies: Harder to See and Remove, Widely Used to Track You,” Electronic Frontier Foundation (https://www.eff.org/deeplinks/2009/09/new-cookietechnologies-harder-see-and-remove-wide; retrieved July 10, 2014).

Singleton, M. 2016. “The New York Times Is Testing Pop-Up Ads Asking Users to Disable Ad Blockers,” The Verge, March 7 (http://www.theverge.com/2016/3/7/11175250/the-new-yorktimes-pop-up-ad-blockers-test; accessed March 8, 2016).

Smith, H. J., Dinev, T., and Xu, H. 2011. “Information Privacy Research: An Interdisciplinary Review,” MIS Quarterly (35:4), pp. 989-1016.

Somaiya, R. 2015a. “New York Times Co. Reports \$16 Million Profit,” The New York Times, August 6 (http://www.nytimes. com/2015/08/07/business/media/new-york-times-co-q2- earnings.html; accessed March 8, 2016).

Somaiya, R. 2015b. “Times Co. Outlines Strategy to Double Digital Revenue,” The New York Times, October 7 (http://www. nytimes.com/2015/10/08/business/media/times-co-outlinesstrategy-to-double-digital-revenue.html?\_r=0; accessed March 8, 2016).

Turow, J., King, J., Hoofnagle, C. J., Bleakley, A., and Hennessy, M. 2009. “Americans Reject Tailored Advertising and Three Activities that Enable it,” Social Science Research Network (SSRN 1478214).

U.S. Senate. 2014. “Online Advertising and Hidden Hazards to Consumer Security and Data Privacy,” Majority and Minority Staff Report Permanent Subcommittee on Investigations, Committee on Homeland Security and Governmental Affairs; released in conjunction with the Permanent Subcommittee on Investigation, May 12, 2014 Hearing (https://www.gpo.gov/fdsys/pkg/ CHRG-113shrg89686/pdf/CHRG-113shrg89686.pdf; accessed August 1, 2014).

Valentino-DeVries, J, Singer-Vine, J, and Soltani, A. 2012. “Websites Vary Prices, Deals Based on Users’ Information,” Wall Street Journal, December 24 (http://www.wsj.com/articles/ SB10001424127887323777204578189391813881534; retrieved April 9, 2015).

Wordstream. 2011. “How Does Google Make Its Money: The 20 Most Expensive Keywords in Google AdWords” (http://www. wordstream.com/articles/most-expensive-keywords; accessed April 5, 2016).

## About the Authors

Ram D. Gopal is GE Capital Endowed Professor of Business and Head of the Department of Operations and Information Management in the School of Business, University of Connecticut. He has held visiting professor positions at the Indian School of Business and the University of Texas at Austin. He received his Ph.D. in Information Systems from the State University of New York at Buffalo and his undergraduate degree in Chemical Engineering from the Indian Institute of Technology, Madras. His current research interests are in the areas of big data analytics, information security, privacy and valuation, intellectual property rights, online market design and business impacts of technology. His research has appeared in

Management Science, MIS Quarterly, Operations Research, INFORMS Journal on Computing, Information Systems Research, Journal of Business, Journal of Law and Economics, Communications of the ACM, IEEE Transactions on Knowledge and Data Engineering, Journal of Management Information Systems, Decision Support Systems, and other journals and conference proceedings. He has served on the editorial boards of Information Systems Research, Decision Sciences, Journal of Database Management, Information Systems Frontiers, and Journal of Management Sciences. He currently serves as president of the Workshop on Information Technologies and Systems organization. As department head, he initiated a new Master of Science degree program in Business Analytics and Project Management in 2011 and an undergraduate business major in Business Data Analytics in 2014.

Hooman Hidaji is an assistant professor of Business Technology Management at the Haskayne School of Business, University of Calgary. He holds a Ph.D. in Business, Operations and Information Systems at the Alberta School of Business, an M.Sc. in Industrial and Financial Engineering from Amirkabir University of Technology, and a B.Sc. in Industrial Engineering from Iran University of Science and Technology. His current research interests include information systems security, online privacy, and third party sharing of user information. He is particularly interested in how the security and privacy requirements and/or decisions of different parties shape online businesses and industries. Hooman’s publications appear in Production and Operations Management Journal, and in conference proceedings such as WITS, TEIS, and INFORMS CIST.

Raymond A. Patterson is Area Chair and Professor of Business Technology Management at the University of Calgary, and a Visiting Professor at the University of Alberta. He conducts research in the fields of analytics, health care, information systems, operations management and service science. Ray has published extensively in premier journals such as Information Systems Research, Journal of Management Information Systems, Operations Research, Production and Operations Management, Service Science, European Journal of Operational Research, Health Care Management Research, Geographic Information Science, and many others. Ray holds a Ph.D. from the Ohio State University in Accounting & Management Information Systems, and has a BSBA and MBA from Bowling Green State University. He previously taught at the University of Alberta, University of Texas at Dallas, Ohio State University, and Bowling Green State University at the undergraduate, master’s, doctoral, and executive education levels. Ray is also involved with Executive Education in Corporate Executive Development and Senior & Executive Managers’ Development Programs. He has been recognized for his outstanding teaching and is also known for his academic program development work.

Erik Rolland is Dean and Professor with the College of Business Administration at California State Polytechnic University, Pomona. He conducts research in the fields of analytics, health care, information systems, operations management, and service science. His research has appeared in Operations Research, Production and Operations Management, IIE Transactions, Service Science, European Journal of Operational Research, Decision Support Systems,

Health Care Management Research, Transportation Science, and many other journals and conference proceedings. Since completing his Ph.D. in Decision Sciences & Information Systems from the Fisher College of Business at the Ohio State University in 1991, he has been on the faculty of the Anderson Graduate School of Management at University of California, Riverside, the Fisher School of Business at the Ohio State University, a professor of Management and Engineering within the Ernest & Julio Gallo Management Program and the School of Engineering at the University of California, Merced, and a visiting distinguished professor with the Antai School of Management & Economics at the Shanghai Jiaotong University.

Dmitry Zhdanov is an assistant professor of Computer Information Systems with J. Mack Robinson College of Business at Georgia State University. His research interests include information security and privacy, large-scale data analysis, design of intelligent agents, green IT, and social impacts of information technology. His research appeared in leading journals such as MIS Quarterly, Information Systems Research, INFORMS Journal on Computing, Decision Support Systems, and Production and Operations Management. Dmitry is a Certified Information Systems Security Professional (CISSP) and a Senior Member of the Institute of Electrical and Electronics Engineers (IEEE). He received his Ph.D. from the University of Minnesota in 2007.

# HOW MUCH TO SHARE WITH THIRD PARTIES? USER PRIVACY CONCERNS AND WEBSITE DILEMMAS

Ram D. Gopal Operations and Information Management, School of Business, University of Connecticut, Storrs, CT 06269 U.S.A. {ram.gopal@business.uconn.edu}

Hooman Hidaji and Raymond A. Patterson Haskayne School of Business, University of Calgary, Calgary, AB, CANADA T2N 1N4 {hooman.hidaji@haskayne.ucalgary.ca} {raymond.patterson@ucalgary.ca}

Erik Rolland College of Business Administration, California State Polytechnic University, Pomona, CA 91768 U.S.A. {erolland@cpp.edu}

Dmitry Zhdanov Department of Computer Information Systems, J. Mack Robinson College of Business, Georgia State University, Atlanta, GA 30302 U.S.A. {dzhdanov@gsu.edu}

## Appendix A

## Proofs

## Proof for Lemma 1

The optimal publisher website royalties $R _ { W _ { i } } ^ { * } , i = 1 , 2$ , and prices $P _ { W _ { i } } ^ { * } , i = 1 , 2$ , satisfy the first order conditions:

$$
\frac {\partial \Pi_ {W _ {1}}}{\partial R _ {W _ {1}}} \left(R _ {W _ {1}} ^ {*}, P _ {W _ {1}} ^ {*}, R _ {W _ {2}} ^ {*}, P _ {W _ {2}} ^ {*}\right) = \frac {\partial \Pi_ {W _ {1}}}{\partial P _ {W _ {1}}} \left(R _ {W _ {1}} ^ {*}, P _ {W _ {1}} ^ {*}, R _ {W _ {2}} ^ {*}, P _ {W _ {2}} ^ {*}\right) =\tag{A1.1}
$$

$$
\frac {\partial \Pi_ {W _ {2}}}{\partial R _ {W _ {2}}} \left(R _ {W _ {1}} ^ {*}, P _ {W _ {1}} ^ {*}, R _ {W _ {2}} ^ {*}, P _ {W _ {2}} ^ {*}\right) = \frac {\partial \Pi_ {W _ {2}}}{\partial P _ {W _ {2}}} \left(R _ {W _ {1}} ^ {*}, P _ {W _ {1}} ^ {*}, R _ {W _ {2}} ^ {*}, P _ {W _ {2}} ^ {*}\right) = 0
$$

By simultaneously solving these equations, $R _ { W _ { 1 } } ^ { ^ { * } } = R _ { W _ { 2 } } ^ { ^ { * } } = R _ { W } ^ { ^ { * } }$ and $\boldsymbol { P } _ { W _ { 1 } } ^ { * } = \boldsymbol { P } _ { W _ { 2 } } ^ { * } = \boldsymbol { P } _ { W } ^ { * }$ are calculated as given in Lemma 1. To ensure that profit is maximized, the second order conditions must hold:

Gopal et al./User Privacy Concerns & Website Dilemmas

$$
\frac {\partial^ {2} \Pi_ {W _ {i}}}{\partial P _ {W _ {i}} ^ {2}} = - \frac {\Phi M _ {U} (8 \Phi t - M _ {U} M _ {D} (R _ {D} - 3 v) (R _ {D} - v))}{2 (2 \Phi t + M _ {U} M _ {D} v (R _ {D} - v)) ^ {2}} <   0\tag{A1.2}
$$

$$
\frac {\partial^ {2} \Pi_ {W _ {i}}}{\partial R _ {W _ {i}} ^ {2}} = - \frac {M _ {D} M _ {U} ^ {2} (4 \Phi t + M _ {U} M _ {D} v (R _ {D} - v)) (4 \Phi t + M _ {U} M _ {D} v (3 R _ {D} - v))}{8 \Phi (2 \Phi t + M _ {U} M _ {D} v (R _ {D} - v)) ^ {2}} <   0\tag{A1.3}
$$

$$
d e t (H e s s i a n) = \frac {\partial^ {2} \Pi_ {W _ {i}}}{\partial R _ {W _ {i}} ^ {2}} \frac {\partial^ {2} \Pi_ {W _ {i}}}{\partial P _ {W _ {i}} ^ {2}} - (\frac {\partial^ {2} \Pi_ {W _ {i}}}{\partial P _ {W _ {i}} \partial R _ {W _ {i}}}) ^ {2} = \frac {4 M _ {U} M _ {U} ^ {3} (2 \Phi t + M _ {U} M _ {D} v (R _ {D} - v)) ^ {2}}{1 6 (2 \Phi t + M _ {U} M _ {D} v (R _ {D} - v)) ^ {4}}\tag{A1.4}
$$

We also need the optimal number of users ${ N _ { U _ { i } } } ^ { * } = { N _ { U _ { i } } } ^ { * } ( { R _ { W _ { 1 } } } ^ { * } , { P _ { W _ { 1 } } } ^ { * } )$ and number of third parties ${ N _ { D } } _ { i } ^ { * } = { N _ { D } } _ { i } ^ { * } ( { R _ { W _ { 1 } } } ^ { * } , { P _ { W _ { 1 } } } ^ { * } )$ to be positive. So we need to have

$$
N _ {U _ {i}} = M _ {U} \frac {\Phi t + \Phi (P _ {W _ {- i}} - P _ {W _ {i}}) + M _ {U} M _ {D} v (R _ {D} - R _ {W _ {- i}})}{2 \Phi t + M _ {U} M _ {D} v ((R _ {D} - R _ {W _ {i}}) + (R _ {D} - R _ {W _ {- i}}))} \geq 0
$$

$$
\Rightarrow 2 \Phi t + M _ {U} M _ {D} v ((R _ {D} - R _ {W _ {i}}) + (R _ {D} - R _ {W _ {- i}})) \geq 0
$$

$$
\forall i = 1, 2\tag{A1.5}
$$

$$
\begin{array}{r l} N _ {D _ {i}} = M _ {D} \frac {M _ {U} (R _ {D} - R _ {W _ {i}}) (\Phi t + \Phi (P _ {W _ {- i}} - P _ {W _ {i}}) + M _ {U} M _ {D} v (R _ {D} - R _ {W _ {- i}}))}{\Phi (2 \Phi t + M _ {U} M _ {D} v ((R _ {D} - R _ {W _ {i}}) + (R _ {D} - R _ {W _ {- i}})))} & \geq 0 \\ & \Rightarrow R _ {D} - R _ {W _ {i}} \geq 0 \end{array}
$$

$$
\forall i = 1, 2\tag{A1.6}
$$

Throughout the paper, we assume (A.1.2), (A.1.3), (A.1.5), and (A.1.6) to be true. (A.1.4) is always true. ∎

## Proposition 1

(i) By taking the derivatives of ${ { R } _ { W } } ^ { * }$ with respect to ݒ and $R _ { D }$ we have

$$
\frac {\partial R _ {W} ^ {*}}{\partial v} = \frac {1}{2} > 0\tag{A2.1}
$$

$$
\frac {\partial R _ {W} ^ {*}}{\partial R _ {D}} = \frac {1}{2} > 0\tag{A2.2}
$$

It is clear from the formula for ${ { R } _ { W } } ^ { * }$ in Lemma 1 that it is independent of the other parameters. ∎

(ii) We have $R _ { D } - v > 0$ and

$$
\frac {\partial P _ {W} ^ {*}}{\partial v} = \frac {M _ {D} M _ {U} (R _ {D} - v)}{2 \Phi} > 0\tag{A2.3}
$$

$$
\frac {\partial P _ {W} ^ {*}}{\partial t} = 1 > 0\tag{A2.4}
$$

$$
\frac {\partial P _ {W} ^ {*}}{\partial R _ {D}} = - \frac {M _ {D} M _ {U} (R _ {D} - v)}{2 \Phi} <   0\tag{A2.5}
$$

$$
\frac {\partial P _ {W} ^ {*}}{\partial M _ {D}} = - \frac {M _ {U} (R _ {D} - v) ^ {2}}{4 \Phi} <   0\tag{A2.6}
$$

$$
\frac {\partial P _ {W} ^ {*}}{\partial M _ {U}} = - \frac {M _ {D} (R _ {D} - v) ^ {2}}{4 \Phi} <   0\tag{A2.7}
$$

## Proposition 2

Using the formula for optimal number of third parties in (13), we have

$$
\frac {\partial N _ {D} ^ {*}}{\partial v} = - \frac {M _ {D} M _ {U}}{4 \Phi} <   0\tag{A3.1}
$$

$$
\frac {\partial N _ {D} ^ {*}}{\partial \Phi} = - \frac {M _ {D} M _ {U} (R _ {D} - v)}{4 \Phi^ {2}} <   0\tag{A3.2}
$$

$$
\frac {\partial N _ {D} ^ {*}}{\partial R _ {D}} = \frac {M _ {D} M _ {U}}{4 \Phi} > 0\tag{A3.3}
$$

$$
\frac {\partial N _ {D} ^ {*}}{\partial M _ {D}} = \frac {M _ {U} (R _ {D} - v)}{4 \Phi} > 0\tag{A3.4}
$$

$$
\frac {\partial N _ {D} ^ {*}}{\partial M _ {U}} = \frac {M _ {D} (R _ {D} - v)}{4 \Phi} > 0\tag{A3.5}
$$

## Proposition 3

(i) Profit of each publisher website is calculated by substituting the optimal royalties and price equations (10) and (11) from Lemma 1 into the publisher website profit equation, and is given in equation (14) in Proposition 3. We have

$$
\frac {\partial \Pi_ {W} ^ {*}}{\partial v} = \frac {M _ {D} M _ {U} ^ {2} (2 R _ {D} - 3 v)}{8 \Phi}\tag{A4.1}
$$

which is positive when $\begin{array} { r } { v < \frac { 2 } { 3 } R _ { D } } \end{array}$ and is negative when $\begin{array} { r } { \frac { 2 } { 3 } R _ { D } < v . } \end{array}$ ∎ .

(ii) We calculate the user surplus from each publisher website as follows:

$$
\begin{array}{l} Z _ {U _ {1}} = \int_ {0} ^ {(t + v (N _ {D _ {2}} - N _ {D _ {1}}) + P _ {W _ {2}} - P _ {W _ {1}}) / 2 t} (X - N _ {D _ {1}} v - P _ {W _ {1}} - t y) d y \\ Z _ {U _ {2}} = \int_ {(t + v (N _ {D _ {2}} - N _ {D _ {1}}) + P _ {W _ {2}} - P _ {W _ {1}}) / 2 t} ^ {1} (X - N _ {D _ {2}} v - P _ {W _ {2}} - t (1 - y)) d y \\ Z _ {U} = Z _ {U _ {1}} + Z _ {U _ {2}} \end{array}
$$

Solving the equation by substituting the optimal publisher website royalties and prices, we have

$$
Z _ {U} ^ {*} = \frac {M _ {U} M _ {D} (R _ {D} - 2 v) (R _ {D} - v) + \Phi (4 X - 5 t)}{4 \Phi}\tag{A4.2}
$$

Taking the derivative with respect to ݒ we have

$$
\frac {\partial Z _ {U} ^ {*}}{\partial v} = - \frac {M _ {U} M _ {D} (3 R _ {D} - 4 v)}{4 \Phi}\tag{A4.3}
$$

which is negative when $\begin{array} { r } { v < \frac { 3 } { 4 } R _ { D } } \end{array}$ and is positive when $\frac { 3 } { 4 } R _ { D } < v . \ \mathbf { \mathbb { I } }$

(iii) Here we calculate the third party surplus from each publisher website as follows:

$$
\begin{array}{r l} & Z _ {D _ {1}} = \int_ {0} ^ {N _ {U _ {1}} (R _ {D} - R _ {W _ {1}})} (N _ {U _ {1}} (R _ {D} - R _ {W _ {1}}) - \varphi) d \varphi = \frac {1}{2} N _ {U _ {1}} ^ {2} (R _ {D} - R _ {W _ {1}}) ^ {2} \\ & Z _ {D _ {2}} = \int_ {0} ^ {N _ {U _ {2}} (R _ {D} - R _ {W _ {2}})} (N _ {U _ {2}} (R _ {D} - R _ {W _ {2}}) - \varphi) d \varphi = \frac {1}{2} N _ {U _ {2}} ^ {2} (R _ {D} - R _ {W _ {2}}) ^ {2} \\ & Z _ {D} = Z _ {D _ {1}} + Z _ {D _ {2}} \end{array}
$$

Solving the equation by substituting the optimal publisher website royalties and prices, we have

$$
Z _ {D} ^ {*} = \frac {1}{1 6} M _ {U} ^ {2} (R _ {D} - v) ^ {2}\tag{A4.4}
$$

Taking the derivatives we have

$$
\frac {\partial Z _ {D} ^ {*}}{\partial v} = - \frac {1}{8} M _ {U} ^ {2} (R _ {D} - v) <   0\tag{A4.5}
$$

Which is always negative. ∎

Proposition 4

$$
\frac {\partial R _ {W} ^ {*}}{\partial T _ {R _ {W}}} = - \frac {R _ {D}}{2 (1 + T _ {R _ {W}}) ^ {2}} <   0\tag{A5.1}
$$

$$
\frac {\partial R _ {W} ^ {*}}{\partial T _ {P _ {W}}} = - \frac {v}{2 (1 + T _ {P _ {W}}) ^ {2}} <   0\tag{A5.2}
$$

$$
\begin{array}{r} \frac {\partial P _ {W} ^ {*}}{\partial T _ {R _ {W}}} = \frac {M _ {U} M _ {D} (R _ {D} ^ {2} (1 + T _ {P _ {W}}) ^ {2} - v ^ {2} (1 + T _ {R _ {W}}) ^ {2})}{4 \Phi (1 + T _ {P _ {W}}) ^ {2} (1 + T _ {R _ {W}}) ^ {2}} \\ = \frac {M _ {U} M _ {D} (R _ {D} (1 + T _ {P _ {W}}) + v (1 + T _ {R _ {W}})) (R _ {D} (1 + T _ {P _ {W}}) - v (1 + T _ {R _ {W}}))}{4 \Phi (1 + T _ {P _ {W}}) ^ {2} (1 + T _ {R _ {W}}) ^ {2}} > 0 \end{array}\tag{A5.3}
$$

$$
\frac {\partial P _ {W} ^ {*}}{\partial T _ {P _ {W}}} = - \frac {2 \Phi t (1 + T _ {P _ {W}}) + M _ {U} M _ {D} v (R _ {D} (1 + T _ {P _ {W}}) - v (1 + T _ {R _ {W}}))}{2 \Phi (1 + T _ {P _ {W}}) ^ {2}} <   0
$$

(A5.4)

## Propositions 5 and 6

(i) Using the transformations (17) and (18), the optimal profit for the website is calculated as

$$
\Pi_ {W} ^ {*} = \frac {M _ {U} (8 \Phi t (1 + T _ {P _ {W}}) (1 + T _ {R _ {W}}) - M _ {U} M _ {D} (R _ {D} (1 + T _ {P _ {W}}) - 3 v (1 + T _ {R _ {W}})) (R _ {D} (1 + T _ {P _ {W}}) - v (1 + T _ {R _ {W}})))}{1 6 \Phi (1 + T _ {P _ {W}}) ^ {2} (1 + T _ {R _ {W}})}\tag{A6.1}
$$

Taking the derivative of profit with respect to the taxations we have

$$
\frac {\partial \Pi_ {W _ {i}} ^ {*}}{\partial T _ {R _ {W}}} = \frac {M _ {U} ^ {2} M _ {D} (R _ {D} ^ {2} (1 + T _ {P _ {W}}) ^ {2} - 3 v ^ {2} (1 + T _ {R _ {W}}) ^ {2})}{1 6 \Phi (1 + T _ {P _ {W}}) ^ {2} (1 + T _ {R _ {W}}) ^ {2}}\tag{A6.2}
$$

which is positive when $\begin{array} { r } { v < \frac { R _ { D } } { \sqrt { 3 } } \frac { 1 + T _ { P _ { W } } } { 1 + T _ { R _ { W } } } . } \end{array}$ , and is negative when $\begin{array} { r } { \frac { R _ { D } } { \sqrt { 3 } } \frac { 1 + T _ { P _ { W } } } { 1 + T _ { R _ { W } } } < v . } \end{array}$

$$
\frac {\partial \Pi_ {W _ {i}} {} ^ {*}}{\partial T _ {P _ {W}}} = - \frac {M _ {U} (4 \Phi t (1 + T _ {P _ {W}}) + M _ {U} M _ {D} v (2 R _ {D} (1 + T _ {P _ {W}}) - 3 v (1 + T _ {R _ {W}}))}{8 \Phi (1 + T _ {P _ {W}}) ^ {3}} <   0\tag{A6.3}
$$

(ii) User surplus when taxations are possible is calculated as

$$
Z _ {U} ^ {*} = \frac {\Phi (4 X - 5 t) (1 + T _ {P _ {W}}) (1 + T _ {R _ {W}}) + M _ {U} M _ {D} (R _ {D} (1 + T _ {P _ {W}}) - 2 v (1 + T _ {R _ {W}})) (R _ {D} (1 + T _ {P _ {W}}) - v (1 + T _ {R _ {W}}))}{4 \Phi (1 + T _ {P _ {W}}) (1 + T _ {R _ {W}})}\tag{A6.4}
$$

and we have

$$
\frac {\partial Z _ {U} ^ {*}}{\partial T _ {R _ {W}}} = - \frac {M _ {D} M _ {U} (R _ {D} ^ {2} (1 + T _ {P _ {W}}) ^ {2} - 2 v ^ {2} (1 + T _ {R _ {W}}) ^ {2})}{4 \Phi (1 + T _ {P _ {W}}) (1 + T _ {R _ {W}}) ^ {2}}\tag{A6.5}
$$

which is negative when $\begin{array} { r } { v < \frac { R _ { D } } { \sqrt { 2 } } \frac { 1 + T _ { P _ { W } } } { 1 + T _ { R _ { W } } } } \end{array}$ and is positive when $\begin{array} { r } { \frac { R _ { D } } { \sqrt { 2 } } \frac { 1 + T _ { P _ { W } } } { 1 + T _ { R _ { W } } } < v } \end{array}$

$$
\frac {\partial Z _ {U} ^ {*}}{\partial T _ {P _ {W}}} = \frac {M _ {D} M _ {U} (R _ {D} ^ {2} (1 + T _ {P _ {W}}) ^ {2} - 2 v ^ {2} (1 + T _ {R _ {W}}) ^ {2})}{4 \Phi (1 + T _ {P _ {W}}) ^ {2} (1 + T _ {R _ {W}})}\tag{A6.6}
$$

which is positive when $\begin{array} { r } { v < \frac { R _ { D } } { \sqrt { 2 } } \frac { 1 + T _ { P _ { W } } } { 1 + T _ { R _ { W } } } } \end{array}$ and is negative when $\begin{array} { r } { \frac { R _ { D } } { \sqrt { 2 } } \frac { 1 + T _ { P _ { W } } } { 1 + T _ { R _ { W } } } < v } \end{array}$

(iii) Third party surplus when taxations are present is calculated as

$$
Z _ {D} ^ {*} = \frac {M _ {U} {} ^ {2}}{1 6} (R _ {D} (1 + T _ {P _ {W}}) - v (1 + T _ {R _ {W}})) ^ {2}\tag{A6.7}
$$

and we have

$$
\frac {\partial Z _ {D} ^ {*}}{\partial T _ {R _ {W}}} = - \frac {M _ {U} ^ {2} v (R _ {D} (1 + T _ {P _ {W}}) - v (1 + T _ {R _ {W}}))}{8 (1 + T _ {P _ {W}}) ^ {2}} <   0\tag{A6.8}
$$

$$
\frac {\partial Z _ {D} ^ {*}}{\partial T _ {P _ {W}}} = \frac {M _ {U} ^ {2} (1 + T _ {R _ {W}}) v (R _ {D} (1 + T _ {P _ {W}}) - v (1 + T _ {R _ {W}}))}{8 (1 + T _ {P _ {W}}) ^ {3}} > 0
$$

(A6.9)

## Appendix B

## Extension of Proposition 3

In Proposition 3 in the paper, we analyzed the effect of privacy concerns on publisher website profit, third party surplus, and user surplus. Here, we expand the analysis to consider other model parameters. Propositions B.1, B.2, and B.3 provide these results. We do not provide the proof for these propositions as they are straightforward and can be calculated by taking the derivatives for equations (14), (15), and (16) for optimal website profit, user surplus, and third party surplus, respectively.

## Proposition B.1: Effect of Parameters on Publisher Website Profit

(i) When $\nu < \frac { 1 } { 2 } R _ { D }$ profit of each publisher website $( \pi _ { w } ^ { * } )$ decreases with third party revenue from user information $( R _ { D } )$ and when $\frac { 1 } { 2 } R _ { D } < \nu < R _ { D }$ it increases with third party revenue from user information $( R _ { D } )$

(ii) When $\scriptstyle \nu < { \frac { 1 } { 3 } } R _ { D }$ profit of each publisher website $( \boldsymbol { \pi } _ { \boldsymbol { w } } ^ { * } )$ increases with third party costs (Φ) and when $\begin{array} { r } { \frac { 1 } { 3 } R _ { D } < \nu < R _ { D } } \end{array}$ it decreases with third party costs (Φ).

(iii) Profit of each publisher website $( \varPi _ { w } ^ { * } )$ increases with differentiation between two publisher websites (t).

(iv) Profit of each publisher website $( \pi _ { w } ^ { * } )$ increases with total number of potential users in the market $( M _ { U } )$

(v) When $\nu < \frac { 1 } { 3 } R _ { D }$ profit of each publisher website $( \boldsymbol { \pi } _ { \boldsymbol { w } } ^ { * } )$ decreases with total number of potential third parties in the market $( M _ { D } )$ and when $\begin{array} { r } { \frac { 1 } { 3 } R _ { D } < \nu < R _ { d } } \end{array}$ it increases with total number of potential third parties in the market $( M _ { D } )$

Figure B1 summarizes Proposition B.1.

## Proposition B.2: Effect of Parameters on User Surplus

(i) When $\nu < \frac { 2 } { 3 } R _ { D }$ user surplus $( Z _ { U } ^ { * } )$ increases with third party revenue from user information $( R _ { D } )$ and when $\begin{array} { r } { \frac { 2 } { 3 } R _ { D } < \nu < R _ { D } } \end{array}$ it decreases with third party revenue from user information $( R _ { D } )$

(ii) When $\scriptstyle \nu < { \frac { 1 } { 2 } } R _ { D }$ user surplus $( Z _ { U } ^ { * } )$ decreases with third party fixed costs (Φ) and when $\begin{array} { r } { \frac { 1 } { 2 } R _ { D } < \nu < R _ { D } } \end{array}$ it increases with third party fixed costs (Φ).

(iii) User surplus $( Z _ { U } ^ { * } )$ decreases with publisher website differentiation (t)

(iv) When $\nu < \frac { 1 } { 2 } R _ { D }$ user surplus $( Z _ { U } ^ { * } )$ increases with total number of users in the market $( M _ { U } )$ and total number of third parties in the market $( M _ { D } ) ,$ , and when $\scriptstyle { \frac { 1 } { 2 } } R _ { D } < \nu < R _ { D }$ it decreases with total number of users in the market $( M _ { U } )$ and total number of third parties in the market $( M _ { D } )$

Figure B2 summarizes Proposition B.2.

![](/api/attachments/Y8D6J3HA/fulltext/images/086e1eabdc56fa92fa2e13f4d7a11663675a1f23209a01d3bb566a541043a316.jpg)

Proposition B.3: Effect of Parameters on Third Parties

(i) Third party surplus $( Z _ { D } ^ { * } )$ increases with third party revenue from user information $( R _ { D } )$

(ii) Third party surplus $( Z _ { D } ^ { * } )$ increases with total number of users in the market $( M _ { U } )$

Figure B3 summarizes Proposition B.3.

## Appendix C

## Asymmetric Model

In the asymmetric model, the two firms are asymmetric in terms of user privacy concerns. The user utility for websites in this case is as follows:

$$
U _ {1} (y) = u _ {1} - t y \quad u _ {1} = X - N _ {D _ {1}} v _ {1} - P _ {W _ {1}}\tag{C1}
$$

$$
U _ {2} (y) = u _ {2} - t (1 - y) \quad u _ {2} = X - N _ {D _ {2}} v _ {2} - P _ {W _ {2}}\tag{C2}
$$

The user who is indifferent between websites 1 and 2 is calculated as

$$
u _ {1} - t \hat {y} = u _ {2} - t (1 - \hat {y}) \Rightarrow \hat {y} = \frac {t + \left(N _ {D _ {2}} v _ {2} - N _ {D _ {1}} v _ {1}\right) + \left(P _ {W _ {2}} - P _ {W _ {1}}\right)}{2 t}\tag{C3}
$$

and the number of users for each publisher website is calculated as

$$
N _ {U _ {i}} = M _ {U} \frac {t + (N _ {D _ {- i}} - v _ {- i} - N _ {D _ {i}} v _ {i}) + (P _ {W _ {- i}} - P _ {W _ {i}})}{2 t} > 0\tag{C4}
$$

The third party profit and website profit equations as well as the equation for number of third parties in this case are similar to the base model. The number of users and third parties with respect to the parameters are calculated as

$$
N _ {U _ {i}} = M _ {U} \frac {\Phi t + \Phi (P _ {W _ {- i}} - P _ {W _ {i}}) + M _ {U} M _ {D} v _ {- i} (R _ {D} - R _ {W _ {- i}})}{2 \Phi t + M _ {U} M _ {D} ((R _ {D} - R _ {W _ {i}}) v _ {i} + (R _ {D} - R _ {W _ {- i}}) v _ {- i})}\tag{C5}
$$

$$
N _ {D _ {i}} = M _ {D} \frac {M _ {U} \left(R _ {D} - R _ {W _ {i}}\right) \left(\Phi t + \Phi \left(P _ {W _ {- i}} - P _ {W _ {i}}\right) + M _ {U} M _ {D} v _ {- i} \left(R _ {D} - R _ {W _ {- i}}\right)\right)}{\Phi \left(2 \Phi t + M _ {U} M _ {D} \left(\left(R _ {D} - R _ {W _ {i}}\right) v _ {i} + \left(R _ {D} - R _ {W _ {- i}}\right) v _ {- i}\right)\right)}\tag{C6}
$$

Using these equations along with the website profit function, the optimal royalties and prices of the websites can be calculated as follows:

$$
R _ {W _ {i}} ^ {*} = \frac {R _ {D} + v _ {i}}{2}\tag{C7}
$$

$$
P _ {W _ {i}} ^ {*} = \frac {\left(2 \Phi t + 2 \Phi P _ {W _ {- i}} + M _ {D} M _ {U} v _ {- i} \left(R _ {D} - v _ {- i}\right)\right) \left(4 \Phi t + M _ {D} M _ {U} \left(R _ {D} \left(v _ {i} + v _ {- i}\right) - v _ {- i} ^ {2} - R _ {D} ^ {2}\right)\right)}{2 \Phi \left(8 \Phi t + M _ {D} M _ {U} \left(2 R _ {D} \left(v _ {i} + v _ {- i}\right) - 2 v _ {- i} ^ {2} - v _ {i} ^ {2} - R _ {D} ^ {2}\right)\right)} \geq 0\tag{C8}
$$

Note that the website prices are calculated based on the price from the other website, and the equilibrium price in analytically intractable when $P _ { W _ { i } } ^ { * }$ can differ from $P _ { W _ { - I } } ^ { * }$ . It is clear from (C8) that the publisher website i’s price is nonlinear in $\nu _ { i }$ and $\nu _ { - i \cdot }$ The results from the numerical analysis are provided in the body of the paper.

## Appendix D

## Effect of Privacy Concerns on Market Concentration

In studying the third party market concentration, we consider two cases: third parties with homogenous shares of the market and third parties with nonhomogenous shares of the market. We use the Herfindahl-Hirschman Index (HHI) as a recognized measure for market concentration. The HHI is generically calculated as follows:

$$
H H I = \sum_ {j = 1} ^ {N _ {D}} s _ {j} ^ {2}\tag{D1}
$$

where $s _ { j }$ is the market share of $j ^ { \mathrm { t h } }$ third party.

## Third Parties with Homogenous Market Shares

In the symmetric duopoly model, because the publisher websites set identical royalties and prices, the third parties either participate in both publisher websites, or do not participate at all. In the homogeneous market share case, the total number of third parties on a particular publishe website i is $N _ { D } = N _ { D _ { 1 } } = N _ { D _ { 2 } }$ . When all of the third parties have an equal share of the market, the market share of each third party j is simply calculated as $s _ { j } = 1 / N _ { D } .$ . The HHI is then calculated as

$$
H H I = \sum_ {j = 1} ^ {N _ {D}} \left(1 / N _ {D}\right) ^ {2} = N _ {D} \left(1 / N _ {D}\right) ^ {2} = 1 / N _ {D}\tag{D2}
$$

By inserting the optimal number of third parties from Proposition 2, we have

$$
H H I = 1 / N _ {D} = 1 / \left[ M _ {D} \frac {M _ {U} (R _ {D} - v)}{4 \Phi} \right] = \frac {4 \Phi}{M _ {D} M _ {U} (R _ {D} - v)}\tag{D3}
$$

It can be seen that HHI is increasing in v. In other words, the market concentration is increasing in the user privacy concerns.

To include the effect of barriers to entry, we rewrite the total number of potential third parties, $M _ { D }$ to be as $M _ { D } / B _ { ; }$ , where B is the level of barrier. This means that higher barriers will reduce the number of potential third parties. We can rewrite the HHI formula as

$$
H H I = 1 / N _ {D} = 1 / \left[ \left(M _ {D} / B\right) \frac {M _ {U} \left(R _ {D} - v\right)}{4 \Phi} \right] = B \frac {4 \Phi}{M _ {D} M _ {U} \left(R _ {D} - v\right)}\tag{D4}
$$

It can be seen that HHI is increasing in the entry barrier level, so the market concentration is increasing in the level of barrier to entry. The level of barrier to entry is higher for third parties that operate in areas with high privacy concerns and high information sensitivity. In practice, privacy is one reason that third parties need to invest more in information technology (IT) security. These IT investments lead to higher sunk cost of entry, and are a major barrier to entry.

## Third Parties with Nonhomogeneous Market Shares

While previously we assumed the market shares to be homogenous for all third parties, this is not realistic in most cases. It results in a market concentration measure that is only dependent on the number of third parties utilized by the publisher websites. We now reconsider the asymmetric model described in the “Asymmetry in User Privacy Concerns” section of the paper, where $\nu _ { 1 }$ varies and $\nu _ { 2 }$ is held constant, using the number of third parties for the two publisher websites to calculate the third party market shares.

Let the number of third parties on publisher websites 1 and 2 be $N _ { D _ { 1 } }$ and $N _ { D _ { 7 } }$ , respectively. Note that since the third parties are differentiated only based on their costs, if a third party participates on the publisher website with higher privacy concern (and higher royalty), then it will also participate on the publisher website with lower privacy concerns (and lower royalty). Thus, there are a total of $M a x \Big \{ N _ { D _ { 1 } } , N _ { D _ { 2 } } \Big \}$ unique third parties active in the market. Out of these third parties, $M i n \Big \{ N _ { D _ { 1 } } , N _ { D _ { 2 } } \Big \}$ of them participate in both publisher websites, and the rest $M a x \Big \{ N _ { D _ { 1 } } , N _ { D _ { 2 } } \Big \}$ of them participate in only one publisher website (the one with lower privacy concerns). Let $J _ { 1 }$ be the set of third parties who participate in only one publisher website, and J<sub>2</sub> be the set of third parties who participate in both publisher websites, where $J _ { 1 } \cap J _ { 2 } = \emptyset$ . The size of $\mathrm { \Delta } y _ { 1 }$ is $| J _ { 1 } | = \ M a x { \Big \{ } N _ { D _ { 1 } } , N _ { D _ { 2 } } { \Big \} } - M i n { \Big \{ } N _ { D _ { 1 } } , N _ { D _ { 2 } } { \Big \} }$ , the size of $J _ { 2 }$ is $| J _ { 2 } | = \ M i n \Big \{ { N _ { D _ { 1 } } , N _ { D _ { 2 } } } \Big \}$ and $J _ { 1 } \cup J _ { 2 }$ is the set of all third parties which has a size of $| J _ { 1 } \bigcup J _ { 2 } | = \ M a x { \Big \{ } N _ { D _ { 1 } } , N _ { D _ { 2 } } { \Big \} }$ . Third parties that are present on both publisher websites have a market size that is twice as much as those that participate in only one publisher website. For simplicity and without loss of generality, we assume the following market sizes for each third party. The market size of each third party j (q<sub>j</sub>) depends on how many publisher websites they serve.

$$
\begin{array}{l l} q _ {j} = 1 & \forall j \in J _ {1} \\ q _ {j} = 2 & \forall j \in J _ {2} \end{array}\tag{D5}
$$

(D6)

Let S be the total market size, which is calculated as the sum of relative market share for all third parties. We have

$$
S = \sum_ {j \in J _ {1}, J _ {2}} q _ {j} = \sum_ {j \in J _ {1}} 1 + \sum_ {j \in J _ {2}} 2\tag{D7}
$$

The market share of each third party (s<sub>j</sub>) is calculated as the ratio of their market size to the total market size, that is

$$
\begin{array}{l l} s _ {j} = \frac {1}{S} & \forall j \in J _ {1} \\ s _ {j} = \frac {2}{S} & \forall j \in J _ {2} \end{array}\tag{D8}
$$

(D9)

Now that the total market size and share of each third party is known, we calculate the HHI as follows:

$$
\begin{array}{l} H H I = \sum_ {j \in J _ {1}, J _ {2}} s _ {j} ^ {2} = \sum_ {j \in J _ {1}} \left(\frac {1}{S}\right) ^ {2} + \sum_ {j \in J _ {2}} \left(\frac {2}{S}\right) ^ {2} \\ = \Big (M a x \big \{N _ {D _ {1}}, N _ {D _ {2}} \big \} - M i n \big \{N _ {D _ {1}}, N _ {D _ {2}} \big \} \Big) \Big (\frac {1}{S} \Big) ^ {2} + M i n \big \{N _ {D _ {1}}, N _ {D _ {2}} \big \} \Big (\frac {2}{S} \Big) ^ {2} \end{array}\tag{D10}
$$

which can be calculated as

$$
H H I = \frac {\operatorname{Max} \left\{N _ {D _ {1}} , N _ {D _ {2}} \right\} + 3 \operatorname{Min} \left\{N _ {D _ {1}} , N _ {D _ {2}} \right\}}{\left(\operatorname{Max} \left\{N _ {D _ {1}} , N _ {D _ {2}} \right\} + \operatorname{Min} \left\{N _ {D _ {1}} , N _ {D _ {2}} \right\}\right) ^ {2}}\tag{D11}
$$

Without loss of generality, let’s assume that $N _ { D _ { 2 } } > N _ { D _ { 1 } }$ . It can be shown that HHI will be maximized when $N _ { D _ { 1 } } ^ { M a x } = \frac { N _ { D _ { 2 } } } { 3 }$ . Figure D1 provides the effect of change in number of third parties on HHI values for a numerical example.

![](/api/attachments/Y8D6J3HA/fulltext/images/919695911e60949aadb5ec3dd5c03a8a7bfe30f7bd4c75340756b46d2c97cd37.jpg)  
Figure D1. HHI Values with Respect to N<sub>D</sub> when $\pmb { \mathbb { N } } \mathbf { \ m } ^ { \pmb { \mathbb { N } } }$

It can be seen in the example that the HHI is not maximized where $\nu _ { 1 } ~ = ~ \nu _ { 2 } ,$ where the two number of third parties are equal $\left( N _ { D _ { 1 } } = N _ { D _ { 2 } } = 1 0 \right)$ , but at $N _ { D _ { 1 } } ^ { M a x } = \frac { 1 0 } { 3 } \cong 3 . 3 3$ . Thus market concentration is at its highest when the number of third parties in two publisher websites are different from each other. Next we will see how this factor directs the way market concentration is affected by user privacy concerns.

As we saw in Figure 5d, $\boldsymbol { N } _ { D _ { 1 } } ^ { * }$ decreases as user privacy concerns  for publisher 1’s website increases. Even though publisher 2’s website user privacy concerns are held steady at $\nu _ { 2 } = 4 , \ N _ { D _ { 2 } } ^ { * }$ will be affected by changes in $\nu _ { \mathrm { l } } .$ Here we look at how these changes in number of third parties determines the market concentration. Figure D2 provides the effect of user privacy concerns of one publisher website on HHI when the user privacy concerns of the other publisher website is fixed.

![](/api/attachments/Y8D6J3HA/fulltext/images/303119b4c7d16e22ae3ae69851655490a35e73b6ba3ad0391550bd168a6cbc6d.jpg)

Figure D2. HHI Values with Respect to v when v Is Fixed

The orange line in Figure D2 represents the homogeneous case where both publisher websites are symmetric, and $N _ { D _ { 1 } } = N _ { D _ { 2 } }$ . The other lines represent asymmetric cases where $\nu _ { 2 }$ is fixed while $\nu _ { 1 }$ varies. By comparing the homogeneous case to any nonhomogeneous case, it can be seen that the HHI is initially higher for the symmetric case (or equal to in when $\nu _ { 2 } = 1 )$ . As $\nu _ { 1 }$ increases while less than $\nu _ { 2 } ,$ , then market concentration for the asymmetric cases can become higher than the symmetric HHI. $\begin{array} { r } { \mathbb { A } \mathfrak { t } \nu _ { 1 } = \nu _ { 2 } , } \end{array}$ the two lines cross, for $\nu _ { 1 } > \nu _ { 2 } ,$ again the HHI for the symmetric case is higher than the asymmetric case

## Appendix E

## Collusion

The calculations for collusion are provided for the case where one publisher sets the equilibrium royalties $( { \cal R } _ { W _ { E q . } }$ ) for its website and the other sets royalties for its website to $R _ { w } .$ The profit in this case is maximized when the the royalty is set to its equilibrium point, $R _ { W _ { E q . } }$ . However, if the publishers can collude and set an identical royalty ( $R _ { W _ { C o l . } }$ ) fo r their websites, then they can increase their profits to the collusion equilibrium $( \Pi _ { W _ { R _ { W _ { C o l . } } } } )$ , where both firms make higher profits.  From the Lemma 1, we know $R _ { W _ { E q . } } = R _ { W } ^ { * } = \frac { R _ { D } + \nu } { 2 }$ and the equilibrium profit (Proposition 3) is given as

$$
\Pi_ {W _ {R W _ {E q.}}} = \Pi_ {W} ^ {*} = \frac {M _ {U} \left(8 \Phi t - M _ {U} M _ {D} (R _ {D} - 3 v) (R _ {D} - v)\right)}{1 6 \Phi}\tag{E1}
$$

For the collusion case, in the publisher website profit equation (9), the prices are set to their optimal values, and both publisher’s website royalties are set to $R _ { W }$ The profit is calculated as

$$
\Pi_ {W _ {R _ {W}}} = \frac {M _ {U} \left(4 \Phi t - M _ {U} M _ {D} \left(R _ {D} ^ {2} + 2 R _ {W} ^ {2} + v ^ {2} - 2 R _ {D} (R _ {W} + v)\right)\right)}{8 \Phi}\tag{E2}
$$

which is maximized at $R _ { W _ { C o l . } } = \frac { R _ { D } } { 2 }$ for which the profit is

$$
\Pi_ {W _ {R W _ {C o l.}}} = \frac {M _ {U} \left(8 \Phi t - M _ {U} M _ {D} \left(R _ {D} ^ {2} - 4 R _ {D} v + 2 v ^ {2}\right)\right)}{1 6 \Phi}\tag{E3}
$$

It can easily be shown using the formulae above that the phenomena that collusion royalties are lower than equilibrium royalties and collusion profits are higher than equilibrium profits are analytical results and hold irrespective of the parameters. In other words, the following hold:

$$
R _ {W _ {E q.}} > R _ {W _ {C o l.}}\tag{E4}
$$

$$
\Pi_ {W _ {R W _ {E q.}}} > \Pi_ {W _ {R W _ {C o l.}}}\tag{E5}
$$

This collusion results in setting lower royalties overall, and thus is also beneficial for the third parties, as presented in the third party surplus curve in Figure E1.

When collusion is possible, the following formula provides the effect of $R _ { \scriptscriptstyle { W } }$ on the user surplus when prices are set to their equilibrium values (we do not consider firms colluding on price but rather only royalties), and publisher websites set equal royalties $\left( C S _ { R _ { W } } \right)$

$$
C S _ {R _ {W}} = \frac {M _ {D} M _ {U} \left(R _ {D} ^ {2} - 4 R _ {D} v + v (2 R _ {W} + v)\right) + \Phi (4 X - 5 t)}{4 \Phi}\tag{E6}
$$

Taking the partial derivative of the user surplus with respect to $R _ { W }$ we have

$$
\frac {\partial C S _ {R W}}{\partial R _ {W}} = \frac {M _ {U} M _ {D} v}{2 \Phi}\tag{E8}
$$

![](/api/attachments/Y8D6J3HA/fulltext/images/3a957efb3bab442b2409f406947da5ec54de6b6f4ea07b90a671f5fe959e9e4a.jpg)

Figure E1. Third Party Surplus with and Without Collusion with Respect to Royalties

![](/api/attachments/Y8D6J3HA/fulltext/images/69887ab19756c2c688c97c5e5552c85379a16aed6ce8878f34b4bbdc4c7e6335.jpg)  
Figure E2. User Surplus with and Without Collusion with Respect to Royalties

Te collusion is thus not beneficial for the users, as they will be exposed to more third parties due to decrease in $R _ { W }$ This can be seen for a numerical example in Figure E2.

## Appendix F

## Duopoly with Nonlinear Utility Function

For the duopoly with nonlinear utility function (NL Duopoly), the transformations (23) and (24) are made in the base model. We then look at the behavior of the model variables with respect to the different variables. Tables F1, F2, and F3 present the comparison of the behavior of parameters and variables between the base duopoly model versus the duopoly model with nonlinear utility function.

In Table F1, it can be seen that while the behavior of some of the parameters are different in the duopoly model with nonlinear utility compared to the base model, the main results of the model in terms of user privacy concerns (v) are consistent with the base model. In Table F2, we can see that the behavior of the number of users and third parties are entirely consistent between the two duopoly models. As described in Table F3, the NL Duopoly model mostly picks up the effect of higher range user privacy concerns seen in the duopoly model for the publisher website profit. While we see some discrepancy among the two models, the overall conclusion is that the results for the duopoly and NL duopoly model are consistent. This is especially true for the key results with respect to user privacy concerns (v).

<table><tr><td></td><td>Changes With Respect To</td><td>Duopoly</td><td>NL Duopoly</td></tr><tr><td rowspan="8">Publisher Website Royalty $R_W^*$ </td><td>v $\left( \frac{\partial R_W^*}{\partial v} \right)$ </td><td>+</td><td>+</td></tr><tr><td> $R_D \left( \frac{\partial R_W^*}{\partial R_D} \right)$ </td><td>+</td><td>+</td></tr><tr><td>Φ $\left( \frac{\partial R_W^*}{\partial \Phi} \right)$ </td><td>Independent</td><td>-</td></tr><tr><td> $M_U \left( \frac{\partial R_W^*}{\partial M_U} \right)$ </td><td>Independent</td><td>+</td></tr><tr><td> $M_D \left( \frac{\partial R_W^*}{\partial M_D} \right)$ </td><td>Independent</td><td>+</td></tr><tr><td>t $\left( \frac{\partial R_W^*}{\partial t} \right)$ </td><td>Independent</td><td>Independent</td></tr><tr><td> $T_{R_W} \left( \frac{\partial R_W^*}{\partial T_{R_W}} \right)$ </td><td>-</td><td>-</td></tr><tr><td> $T_{P_W} \left( \frac{\partial R_W^*}{\partial T_{P_W}} \right)$ </td><td>-</td><td>-</td></tr><tr><td rowspan="8">Publisher Website Price $P_W^*$ </td><td>v $\left( \frac{\partial P_W^*}{\partial v} \right)$ </td><td>+</td><td>+</td></tr><tr><td> $R_D \left( \frac{\partial P_W^*}{\partial R_D} \right)$ </td><td>-</td><td>-</td></tr><tr><td>Φ $\left( \frac{\partial P_W^*}{\partial \Phi} \right)$ </td><td>+</td><td>-</td></tr><tr><td> $M_U \left( \frac{\partial P_W^*}{\partial M_U} \right)$ </td><td>-</td><td>+</td></tr><tr><td> $M_D \left( \frac{\partial P_W^*}{\partial M_D} \right)$ </td><td>-</td><td>+</td></tr><tr><td>t $\left( \frac{\partial P_W^*}{\partial t} \right)$ </td><td>+</td><td>+</td></tr><tr><td> $T_{R_W} \left( \frac{\partial P_W^*}{\partial T_{R_W}} \right)$ </td><td>+</td><td>+</td></tr><tr><td> $T_{P_W} \left( \frac{\partial P_W^*}{\partial T_{P_W}} \right)$ </td><td>-</td><td>-</td></tr><tr><td rowspan="8">Number of Users $N_D^*$ </td><td>v $\left( \frac{\partial N_U^*}{\partial v} \right)$ </td><td>Independent</td><td>Independent</td></tr><tr><td> $R_D \left( \frac{\partial N_U^*}{\partial R_D} \right)$ </td><td>Independent</td><td>Independent</td></tr><tr><td>Φ $\left( \frac{\partial N_U^*}{\partial \Phi} \right)$ </td><td>Independent</td><td>Independent</td></tr><tr><td> $M_U \left( \frac{\partial N_U^*}{\partial M_U} \right)$ </td><td>Independent</td><td>Independent</td></tr><tr><td> $M_D \left( \frac{\partial N_U^*}{\partial M_D} \right)$ </td><td>Independent</td><td>Independent</td></tr><tr><td>t $\left( \frac{\partial N_U^*}{\partial t} \right)$ </td><td>Independent</td><td>Independent</td></tr><tr><td> $T_{R_W} \left( \frac{\partial N_U^*}{\partial T_{R_W}} \right)$ </td><td>Independent</td><td>Independent</td></tr><tr><td> $T_{P_W} \left( \frac{\partial N_U^*}{\partial T_{P_W}} \right)$ </td><td>Independent</td><td>Independent</td></tr><tr><td rowspan="8">Number of Third Parties $N_D^*$ </td><td>v $\left( \frac{\partial N_D^*}{\partial v} \right)$ </td><td>-</td><td>-</td></tr><tr><td> $R_D \left( \frac{\partial N_D^*}{\partial R_D} \right)$ </td><td>+</td><td>+</td></tr><tr><td>Φ $\left( \frac{\partial N_D^*}{\partial \Phi} \right)$ </td><td>-</td><td>-</td></tr><tr><td> $M_U \left( \frac{\partial N_D^*}{\partial M_U} \right)$ </td><td>+</td><td>+</td></tr><tr><td> $M_D \left( \frac{\partial N_D^*}{\partial M_D} \right)$ </td><td>+</td><td>+</td></tr><tr><td>t $\left( \frac{\partial N_D^*}{\partial t} \right)$ </td><td>Independent</td><td>Independent</td></tr><tr><td> $T_{R_W} \left( \frac{\partial N_D^*}{\partial T_{R_W}} \right)$ </td><td>-</td><td>-</td></tr><tr><td> $T_{P_W} \left( \frac{\partial N_D^*}{\partial T_{P_W}} \right)$ </td><td>+</td><td>+</td></tr><tr><td rowspan="8">Publisher Website Profit $\Pi_{W}^{*}$ </td><td> $v \quad \left( \frac{\partial \Pi_{W}^{*}}{\partial v} \right)$ </td><td>+ then -</td><td>-</td></tr><tr><td> $R_{D} \quad \left( \frac{\partial \Pi_{W}^{*}}{\partial R_{D}} \right)$ </td><td>- for low  $v$ + for high  $v$ </td><td>+</td></tr><tr><td> $\Phi \quad \left( \frac{\partial \Pi_{W}^{*}}{\partial \Phi} \right)$ </td><td>- for low  $v$ + for high  $v$ </td><td>-</td></tr><tr><td> $M_{U} \quad \left( \frac{\partial \Pi_{W}^{*}}{\partial M_{U}} \right)$ </td><td>+</td><td>+</td></tr><tr><td> $M_{D} \quad \left( \frac{\partial \Pi_{W}^{*}}{\partial M_{D}} \right)$ </td><td>- for low  $v$ + for high  $v$ </td><td>+</td></tr><tr><td> $t \quad \left( \frac{\partial \Pi_{W}^{*}}{\partial t} \right)$ </td><td>+</td><td>+</td></tr><tr><td> $T_{R_{W}} \quad \left( \frac{\partial \Pi_{W}^{*}}{\partial T_{R_{W}}} \right)$ </td><td>- for low  $v$ + for high  $v$ </td><td>-</td></tr><tr><td> $T_{P_{W}} \quad \left( \frac{\partial \Pi_{W}^{*}}{\partial T_{P_{W}}} \right)$ </td><td>-</td><td>-</td></tr><tr><td rowspan="8">User Surplus $Z_{U}^{*}$ </td><td> $v \quad \left( \frac{\partial Z_{U}^{*}}{\partial v} \right)$ </td><td>- then +</td><td>+</td></tr><tr><td> $R_{D} \quad \left( \frac{\partial Z_{U}^{*}}{\partial R_{D}} \right)$ </td><td>- for low  $v$ + for high  $v$ </td><td>-</td></tr><tr><td> $\Phi \quad \left( \frac{\partial Z_{U}^{*}}{\partial \Phi} \right)$ </td><td>- for low  $v$ + for high  $v$ </td><td>+</td></tr><tr><td> $M_{U} \quad \left( \frac{\partial Z_{U}^{*}}{\partial M_{U}} \right)$ </td><td>- for low  $v$ + for high  $v$ </td><td>+</td></tr><tr><td> $M_{D} \quad \left( \frac{\partial Z_{U}^{*}}{\partial M_{D}} \right)$ </td><td>- for low  $v$ + for high  $v$ </td><td>-</td></tr><tr><td> $t \quad \left( \frac{\partial Z_{U}^{*}}{\partial t} \right)$ </td><td>-</td><td>-</td></tr><tr><td> $T_{R_{W}} \quad \left( \frac{\partial Z_{U}^{*}}{\partial T_{R_{W}}} \right)$ </td><td>- for low  $v$ + for high  $v$ </td><td>+</td></tr><tr><td> $T_{P_{W}} \quad \left( \frac{\partial Z_{U}^{*}}{\partial T_{P_{W}}} \right)$ </td><td>- for low  $v$ + for high  $v$ </td><td>-</td></tr><tr><td rowspan="8">Third Party Surplus $Z_D^*$ </td><td>v $\left( \frac{\partial Z_D^*}{\partial v} \right)$ </td><td>-</td><td>-</td></tr><tr><td> $R_D$  $\left( \frac{\partial Z_D^*}{\partial R_D} \right)$ </td><td>+</td><td>+</td></tr><tr><td>Φ $\left( \frac{\partial Z_D^*}{\partial \Phi} \right)$ </td><td>Independent</td><td>+</td></tr><tr><td> $M_U$  $\left( \frac{\partial Z_D^*}{\partial M_U} \right)$ </td><td>+</td><td>+</td></tr><tr><td> $M_D$  $\left( \frac{\partial Z_D^*}{\partial M_D} \right)$ </td><td>Independent</td><td>-</td></tr><tr><td>t $\left( \frac{\partial Z_D^*}{\partial t} \right)$ </td><td>Independent</td><td>-</td></tr><tr><td> $T_{R_W}$  $\left( \frac{\partial Z_D^*}{\partial T_{RW}} \right)$ </td><td>-</td><td>-</td></tr><tr><td> $T_{P_W}$  $\left( \frac{\partial Z_D^*}{\partial T_{PW}} \right)$ </td><td>+</td><td>+</td></tr></table>

## Appendix G

## Monopoly Model

The following tables compare the effect of model parameters on the key variables in the model, as well as on the publisher website profit, user and third party surplus. Tables G1, G2, and G3 present the comparison of the behavior of parameters and variables between the base duopoly model versus the monopoly model.

In Table G1, it can be seen that the decision variables of royalties and prices behave similarly in the monopoly and duopoly models. Addition of the Hotelling’s parameter in the duopoly model enables us to see the effect of competition on the prices. The higher the differentiation between the two publisher websites (higher ), the higher the prices. In other words, competition would decrease the prices for the publishe websites.

In Table G2, we can see that the behavior of the number of users in the monopoly model is different from the duopoly model, because the key assumption in the duopoly model is that the market is covered. Thus, the number of users in the duopoly model is independent of the parameters. For the number of third parties, we see that the behavior of the monopoly and duopoly models are similar.

In Table G3, the publisher website profit, user surplus, and third party surplus are presented. The monopoly model picks up the effect of higher range user privacy concerns seen in the duopoly model for the publisher website profit. For user surplus, the monopoly model picks up the effect of the lower range of user privacy concerns seen in the duopoly model. While we see two different effects in the duopoly model, the pattern of results is consistent between the two models. Thus, our overall conclusion is that the results for the duopoly and monopoly models are not inconsistent. This is especially true for the key results with respect to user privacy concerns (v).

<table><tr><td></td><td>Changes With Respect To</td><td>Duopoly</td><td>Monopoly</td></tr><tr><td rowspan="8">Publisher Website Royalty $R_W^*$ </td><td>v $\left( \frac{\partial R_W^*}{\partial v} \right)$ </td><td>+</td><td>+</td></tr><tr><td> $R_D \left( \frac{\partial R_W^*}{\partial R_D} \right)$ </td><td>+</td><td>+</td></tr><tr><td>Φ $\left( \frac{\partial R_W^*}{\partial \Phi} \right)$ </td><td>Independent</td><td>Independent</td></tr><tr><td> $M_U \left( \frac{\partial R_W^*}{\partial M_U} \right)$ </td><td>Independent</td><td>Independent</td></tr><tr><td> $M_D \left( \frac{\partial R_W^*}{\partial M_D} \right)$ </td><td>Independent</td><td>Independent</td></tr><tr><td>t $\left( \frac{\partial R_W^*}{\partial t} \right)$ </td><td>Independent</td><td>N/A</td></tr><tr><td> $T_{R_W} \left( \frac{\partial R_W^*}{\partial T_{R_W}} \right)$ </td><td>-</td><td>-</td></tr><tr><td> $T_{P_W} \left( \frac{\partial R_W^*}{\partial T_{P_W}} \right)$ </td><td>-</td><td>-</td></tr><tr><td rowspan="8">Publisher Website Price $P_W^*$ </td><td>v $\left( \frac{\partial P_W^*}{\partial v} \right)$ </td><td>+</td><td>+</td></tr><tr><td> $R_D \left( \frac{\partial P_W^*}{\partial R_D} \right)$ </td><td>-</td><td>-</td></tr><tr><td>Φ $\left( \frac{\partial P_W^*}{\partial \Phi} \right)$ </td><td>+</td><td>+</td></tr><tr><td> $M_U \left( \frac{\partial P_W^*}{\partial M_U} \right)$ </td><td>-</td><td>-</td></tr><tr><td> $M_D \left( \frac{\partial P_W^*}{\partial M_D} \right)$ </td><td>-</td><td>-</td></tr><tr><td>t $\left( \frac{\partial P_W^*}{\partial t} \right)$ </td><td>+</td><td>N/A</td></tr><tr><td> $T_{R_W} \left( \frac{\partial P_W^*}{\partial T_{R_W}} \right)$ </td><td>+</td><td>+</td></tr><tr><td> $T_{P_W} \left( \frac{\partial P_W^*}{\partial T_{P_W}} \right)$ </td><td>-</td><td>-</td></tr><tr><td rowspan="8">Number of Users $N_D^*$ </td><td>v $\left( \frac{\partial N_U^*}{\partial v} \right)$ </td><td>Independent</td><td>-</td></tr><tr><td> $R_D \left( \frac{\partial N_U^*}{\partial R_D} \right)$ </td><td>Independent</td><td>+</td></tr><tr><td>Φ $\left( \frac{\partial N_U^*}{\partial \Phi} \right)$ </td><td>Independent</td><td>-</td></tr><tr><td> $M_U \left( \frac{\partial N_U^*}{\partial M_U} \right)$ </td><td>Independent</td><td>+</td></tr><tr><td> $M_D \left( \frac{\partial N_U^*}{\partial M_D} \right)$ </td><td>Independent</td><td>+</td></tr><tr><td>t $\left( \frac{\partial N_U^*}{\partial t} \right)$ </td><td>Independent</td><td>N/A</td></tr><tr><td> $T_{R_W} \left( \frac{\partial N_U^*}{\partial T_{R_W}} \right)$ </td><td>Independent</td><td>-</td></tr><tr><td> $T_{P_W} \left( \frac{\partial N_U^*}{\partial T_{P_W}} \right)$ </td><td>Independent</td><td>+</td></tr><tr><td rowspan="8">Number of Third Parties $N_D^*$ </td><td>v $\left( \frac{\partial N_D^*}{\partial v} \right)$ </td><td>-</td><td>-</td></tr><tr><td> $R_D \left( \frac{\partial N_D^*}{\partial R_D} \right)$ </td><td>+</td><td>+</td></tr><tr><td>Φ $\left( \frac{\partial N_D^*}{\partial \Phi} \right)$ </td><td>-</td><td>-</td></tr><tr><td> $M_U \left( \frac{\partial N_D^*}{\partial M_U} \right)$ </td><td>+</td><td>+</td></tr><tr><td> $M_D \left( \frac{\partial N_D^*}{\partial M_D} \right)$ </td><td>+</td><td>+</td></tr><tr><td>t $\left( \frac{\partial N_D^*}{\partial t} \right)$ </td><td>Independent</td><td>N/A</td></tr><tr><td> $T_{R_W} \left( \frac{\partial N_D^*}{\partial T_{R_W}} \right)$ </td><td>-</td><td>-</td></tr><tr><td> $T_{P_W} \left( \frac{\partial N_D^*}{\partial T_{P_W}} \right)$ </td><td>+</td><td>+</td></tr><tr><td rowspan="8">Publisher Website Profit $\Pi_{W}^{*}$ </td><td> $v \quad \left( \frac{\partial \Pi_{W}^{*}}{\partial v} \right)$ </td><td>+ then -</td><td>-</td></tr><tr><td> $R_{D} \quad \left( \frac{\partial \Pi_{W}^{*}}{\partial R_{D}} \right)$ </td><td>- for low  $v$ + for high  $v$ </td><td>+</td></tr><tr><td> $\Phi \quad \left( \frac{\partial \Pi_{W}^{*}}{\partial \Phi} \right)$ </td><td>+ for low  $v$ - for high  $v$ </td><td>-</td></tr><tr><td> $M_{U} \quad \left( \frac{\partial \Pi_{W}^{*}}{\partial M_{U}} \right)$ </td><td>+</td><td>+</td></tr><tr><td> $M_{D} \quad \left( \frac{\partial \Pi_{W}^{*}}{\partial M_{D}} \right)$ </td><td>- for low  $v$ + for high  $v$ </td><td>+</td></tr><tr><td> $t \quad \left( \frac{\partial \Pi_{W}^{*}}{\partial t} \right)$ </td><td>+</td><td>N/A</td></tr><tr><td> $T_{R_{W}} \quad \left( \frac{\partial \Pi_{W}^{*}}{\partial T_{R_{W}}} \right)$ </td><td>+ for low  $v$ - for high  $v$ </td><td>-</td></tr><tr><td> $T_{P_{W}} \quad \left( \frac{\partial \Pi_{W}^{*}}{\partial T_{P_{W}}} \right)$ </td><td>-</td><td>+</td></tr><tr><td rowspan="8">User Surplus $Z_{u}^{*}$ </td><td> $v \quad \left( \frac{\partial Z_{U}^{*}}{\partial v} \right)$ </td><td>- then +</td><td>-</td></tr><tr><td> $R_{D} \quad \left( \frac{\partial Z_{U}^{*}}{\partial R_{D}} \right)$ </td><td>+ for low  $v$ - for high  $v$ </td><td>+</td></tr><tr><td> $\Phi \quad \left( \frac{\partial Z_{U}^{*}}{\partial \Phi} \right)$ </td><td>- for low  $v$ + for high  $v$ </td><td>-</td></tr><tr><td> $M_{U} \quad \left( \frac{\partial Z_{U}^{*}}{\partial M_{U}} \right)$ </td><td>+ for low  $v$ - for high  $v$ </td><td>+</td></tr><tr><td> $M_{D} \quad \left( \frac{\partial Z_{U}^{*}}{\partial M_{D}} \right)$ </td><td>+ for low  $v$ - for high  $v$ </td><td>+</td></tr><tr><td> $t \quad \left( \frac{\partial Z_{U}^{*}}{\partial t} \right)$ </td><td>-</td><td>N/A</td></tr><tr><td> $T_{R_{W}} \quad \left( \frac{\partial Z_{U}^{*}}{\partial T_{R_{W}}} \right)$ </td><td>- for low  $v$ + for high  $v$ </td><td>-</td></tr><tr><td> $T_{P_{W}} \quad \left( \frac{\partial Z_{U}^{*}}{\partial T_{P_{W}}} \right)$ </td><td>+ for low  $v$ - for high  $v$ </td><td>+</td></tr><tr><td rowspan="8">Third Party Surplus $Z_D^*$ </td><td> $v \quad \left( \frac{\partial Z_D^*}{\partial v} \right)$ </td><td>-</td><td>-</td></tr><tr><td> $R_D \quad \left( \frac{\partial Z_D^*}{\partial R_D} \right)$ </td><td>+</td><td>+</td></tr><tr><td> $\Phi \quad \left( \frac{\partial Z_D^*}{\partial \Phi} \right)$ </td><td>Independent</td><td>-</td></tr><tr><td> $M_U \quad \left( \frac{\partial Z_D^*}{\partial M_U} \right)$ </td><td>+</td><td>+</td></tr><tr><td> $M_D \quad \left( \frac{\partial Z_D^*}{\partial M_D} \right)$ </td><td>Independent</td><td>+</td></tr><tr><td> $t \quad \left( \frac{\partial Z_D^*}{\partial t} \right)$ </td><td>Independent</td><td>N/A</td></tr><tr><td> $T_{R_W} \quad \left( \frac{\partial Z_D^*}{\partial T_{R_W}} \right)$ </td><td>-</td><td>-</td></tr><tr><td> $T_{P_W} \quad \left( \frac{\partial Z_D^*}{\partial T_{P_W}} \right)$ </td><td>+</td><td>+</td></tr></table>

## Appendix H

## Empirical Analysis

We find partial support for the model by empirically examining the number of third party participants utilized by publisher websites, as well as the industry concentration of third parties. Alexa Internet provides rankings for publisher websites within 17 different subject categories. We carry out an exploratory validation study on the 100 most-visited publisher websites from seven of these subject categories (news, arts, shopping, kids and teens, health, business, and adult) provided and ranked by Alexa website rankings. These seven categories were selected with the intention of finding subject categories for which users might reasonably be expected to have different intentions to disclose personal information and browsing behavior due to the nature of the subject content. For the study, an automated browser accessed the home page of a publisher’s website, and the connections made from the publisher’s website to third parties were recorded. We used page loading time plus a 3-second window to collect data gathered using a residential internet plan and using Lightbeam for Firefox (Windows) to record these connections.

To better capture the structure of the industry, we profile the third parties and separate them based on the industry sectors as classified by Cookiepedia.co.uk. The three industry sectors are targeting/advertising (T/A), functionality (F), and performance (P). For those third parties that are not profiled in Cookiepedia.co.uk, we make a judgment using available information. A total of 1,893 third party websites are identified, with 568 classified as T/A, 487 classified as F, 627 classified as P, and 211 classified as unknown (U). Using different domain finder services,<sup>2</sup> multiple third party websites in each sector owned by the same company are treated as a single third party for analysis, entailing 1,066 unique owner companies comprising 442 classified as T/A, 336 classified as F, and 340 classified as P, with some owner companies providing services in multiple categories. The number of connections made and number of cookies used follow a similar pattern to number of third parties, and so we provide the analysis based on number of third parties only. Table H1 provides a summary of descriptive statistics of the data on number of third parties.

Table H1. Descriptive Statistics for Number of Third Parties Used Among Websites

<table><tr><td rowspan="2">Subject Category</td><td rowspan="2">N</td><td colspan="4">Targeting/Advertising</td><td colspan="4">Functionality</td><td colspan="4">Performace</td></tr><tr><td>Min</td><td>Max</td><td>Avg.</td><td>StDv</td><td>Min</td><td>Max</td><td>Mean</td><td>StDv</td><td>Min</td><td>Max</td><td>Mean</td><td>StDv</td></tr><tr><td>News</td><td>100</td><td>1</td><td>65</td><td>16.8</td><td>11.7</td><td>1</td><td>10</td><td>4.5</td><td>2.3</td><td>1</td><td>10</td><td>3.4</td><td>2.0</td></tr><tr><td>Arts</td><td>100</td><td>1</td><td>55</td><td>11.5</td><td>10.0</td><td>1</td><td>10</td><td>3.9</td><td>2.1</td><td>1</td><td>7</td><td>2.8</td><td>1.5</td></tr><tr><td>Shopping</td><td>100</td><td>1</td><td>51</td><td>9.4</td><td>9.2</td><td>1</td><td>8</td><td>2.9</td><td>1.6</td><td>1</td><td>8</td><td>2.7</td><td>1.6</td></tr><tr><td>Kids and teens</td><td>100</td><td>1</td><td>58</td><td>8.8</td><td>11.5</td><td>1</td><td>7</td><td>2.7</td><td>1.4</td><td>1</td><td>7</td><td>2.3</td><td>1.5</td></tr><tr><td>Health</td><td>100</td><td>1</td><td>70</td><td>8.2</td><td>11.3</td><td>1</td><td>7</td><td>2.9</td><td>1.6</td><td>1</td><td>7</td><td>2.4</td><td>1.5</td></tr><tr><td>Business</td><td>100</td><td>1</td><td>60</td><td>6.9</td><td>9.2</td><td>1</td><td>7</td><td>2.4</td><td>1.6</td><td>1</td><td>7</td><td>2.4</td><td>1.4</td></tr><tr><td>Adult</td><td>100</td><td>1</td><td>34</td><td>3.2</td><td>5.2</td><td>1</td><td>9</td><td>2.2</td><td>1.5</td><td>1</td><td>7</td><td>1.7</td><td>1.0</td></tr></table>

## Observations

Noting that information sensitivity and user privacy concerns likely vary among different publisher websites, we expect the sharing behavior to differ for publisher websites with different subjects. Figure H1 provides the sharing behavior for the top 100 publisher websites in each subject category and industry sector.

![](/api/attachments/Y8D6J3HA/fulltext/images/a2399f17344abd2c131ebe01b919e9c826003f785fafd6213d186b42b64c3bc8.jpg)

![](/api/attachments/Y8D6J3HA/fulltext/images/c5a0c6dcbd8d359e45b2139abbed3b4cfaf1f28704a35426f558c317be8557e3.jpg)  
Figure H1. Third Party Usage by Subject Categories and Industry Sectors

Table H2 provides the statistical test results for number of third parties on different categories of websites. Since the variances are different among the categories, we use the Welch’s two-tailed t-test for testing if the means are different among these websites. It can be seen from Table H2 that the number of third parties are significantly different for most of the categories. Especially, in the T/A sector, news and adult categories are statistically different from other categories.

Table H3 provides the statistical test results for number of third parties on different sectors of the industry. It can be seen from Table H3 that the number of third parties used in the T/A industry sector is significantly higher than for both F and P.

We also examine the third party market concentration measure, using the Herfindahl-Hirschman index (HHI) based on the average monthly unique visitors to the publisher’s website in the United States for a single year period ending in March 2014 as provided by compete.com. The T/A sector has the lowest HHI concentrations, followed by P, and then by F. In terms of publisher website categories, we see that news and arts have the lowest industry concentration, with adult having the highest industry concentration. The HHI results are provided in Figure H2.

Table H2. P-Values for Testing if Number of Third Parties Used in Different Categories of Websites are Statistically Different

<table><tr><td colspan="2"></td><td>News</td><td>Arts</td><td>Shopping</td><td>Kids &amp; Teens</td><td>Health</td><td>Business</td></tr><tr><td rowspan="7">T/A</td><td>News</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Arts</td><td>0.001</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Shopping</td><td>0.000</td><td>0.125</td><td></td><td></td><td></td><td></td></tr><tr><td>Kids &amp; Teens</td><td>0.000</td><td>0.082</td><td>0.700</td><td></td><td></td><td></td></tr><tr><td>Health</td><td>0.000</td><td>0.027</td><td>0.390</td><td>0.670</td><td></td><td></td></tr><tr><td>Business</td><td>0.000</td><td>0.001</td><td>0.056</td><td>0.191</td><td>0.393</td><td></td></tr><tr><td>Adult</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.001</td></tr><tr><td rowspan="7">F</td><td>News</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Arts</td><td>0.064</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Shopping</td><td>0.000</td><td>0.001</td><td></td><td></td><td></td><td></td></tr><tr><td>Kids &amp; Teens</td><td>0.000</td><td>0.000</td><td>0.299</td><td></td><td></td><td></td></tr><tr><td>Health</td><td>0.000</td><td>0.000</td><td>0.704</td><td>0.522</td><td></td><td></td></tr><tr><td>Business</td><td>0.000</td><td>0.000</td><td>0.012</td><td>0.106</td><td>0.032</td><td></td></tr><tr><td>Adult</td><td>0.000</td><td>0.000</td><td>0.002</td><td>0.024</td><td>0.006</td><td>0.551</td></tr><tr><td rowspan="7">P</td><td>News</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Arts</td><td>0.019</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Shopping</td><td>0.006</td><td>0.568</td><td></td><td></td><td></td><td></td></tr><tr><td>Kids &amp; Teens</td><td>0.000</td><td>0.023</td><td>0.099</td><td></td><td></td><td></td></tr><tr><td>Health</td><td>0.000</td><td>0.061</td><td>0.210</td><td>0.690</td><td></td><td></td></tr><tr><td>Business</td><td>0.000</td><td>0.036</td><td>0.147</td><td>0.796</td><td>0.877</td><td></td></tr><tr><td>Adult</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.001</td><td>0.000</td><td>0.000</td></tr></table>

Table H3. P-Values for Testing If Number of Third Parties Used in Different Industry Sectors Are Statistically Different

<table><tr><td colspan="2"></td><td>T/A</td><td>F</td></tr><tr><td rowspan="3">News</td><td>T/A</td><td></td><td></td></tr><tr><td>F</td><td>0.000</td><td></td></tr><tr><td>P</td><td>0.000</td><td>0.001</td></tr><tr><td rowspan="3">Arts</td><td>T/A</td><td></td><td></td></tr><tr><td>F</td><td>0.000</td><td></td></tr><tr><td>P</td><td>0.000</td><td>0.000</td></tr><tr><td rowspan="3">Shopping</td><td>T/A</td><td></td><td></td></tr><tr><td>F</td><td>0.000</td><td></td></tr><tr><td>P</td><td>0.000</td><td>0.286</td></tr><tr><td rowspan="3">Kids and Teens</td><td>T/A</td><td></td><td></td></tr><tr><td>F</td><td>0.000</td><td></td></tr><tr><td>P</td><td>0.000</td><td>0.067</td></tr><tr><td rowspan="3">Health</td><td>T/A</td><td></td><td></td></tr><tr><td>F</td><td>0.000</td><td></td></tr><tr><td>P</td><td>0.000</td><td>0.051</td></tr><tr><td rowspan="3">Business</td><td>T/A</td><td></td><td></td></tr><tr><td>F</td><td>0.000</td><td></td></tr><tr><td>P</td><td>0.000</td><td>0.925</td></tr><tr><td rowspan="3">Adult</td><td>T/A</td><td></td><td></td></tr><tr><td>F</td><td>0.080</td><td></td></tr><tr><td>P</td><td>0.007</td><td>0.008</td></tr></table>

HHI Values  
![](/api/attachments/Y8D6J3HA/fulltext/images/e2c6d1c7d6e0a204dd57683abc067d856468d571f9b0556bc79fe31c0f478f94.jpg)

---
otero_id: 6358
otero_key: "WV6YR97T"
title: "Towards a highly effective and robust Web credibility evaluation system"
authors: "Xin Liu; Radoslaw Nielek; Paulina Adamska; Adam Wierzbicki; Karl Aberer"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.07.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Xin Liu <sup>a,</sup>⁎, Radoslaw Nielek <sup>b</sup>, Paulina Adamska <sup>b</sup>, Adam Wierzbicki <sup>b</sup>, Karl Aberer <sup>c</sup>

<sup>a</sup> Data Analytics Department, Institute for Infocomm Research, Singapore

<sup>b</sup> Department of Computer Networks, Polish Japanese Institute of Information Technology, Poland

<sup>c</sup> School of Computer Sciences, École Polytechnique Fédérale de Lausanne (EPFL), Switzerland

## a r t i c l e i n f o

Article history: Received 2 May 2014 Received in revised form 5 May 2015 Accepted 22 July 2015 Available online 31 July 2015

Keywords: Web credibility Recommendation Robustness Imitating attack

## a b s t r a c t

By leveraging crowdsourcing, Web credibility evaluation systems (WCESs) have become a promising tool to assess the credibility of Web content, e.g., Web pages. However, existing systems adopt a passive way to collect users' credibility ratings, which incurs two crucial challenges: (1) a considerable fraction of Web content have few or even no ratings, so the coverage (or effectiveness) of the system is low; (2) malicious users may submit fake ratings to damage the reliability of the system, In order to realize a highly effective and robust WCES, we propose to integrate recommendation functionality into the system. On the one hand, by fusing Matrix Factorization and Latent Dirichlet Allocation, a personalized Web content recommendation model is proposed to attract users to rate more Web pages, i.e., the coverage is increased. On the other hand, by analyzing a user's reaction to the recommended Web content, we detect imitating attackers, which have recently been recognized as a particular threat to WCES to make the system more robust. Moreover, an adaptive reputation system is designed to motivate users to more actively interact with the integrated recommendation functionality. We conduct experiments using both real datasets and synthetic data to demonstrate how our proposed recommendation components significantly improve the effectiveness and robustness of existing WCES.

© 2015 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).

## 1. Introduction

The Internet has become the primary information source to serve people's daily life. However, unlike traditional media such as television and newspapers, a considerable fraction of contents are posted online without being seriously fact-checked. This may incur serious consequences if non-credible Web information is used for decision making. It is thus important to assess the credibility of Web content [6,20,17].

Recently, by leveraging crowdsourcing, several Web credibility evaluation systems (WCESs) have emerged. For instance, MyWOT (www. mywot.com) aggregates users' ratings on two aspects of Web credibility: trustworthiness and child safety. In academia, similar systems have also been proposed, improving the commercial counterparts in various aspects [22,21,18].

Although WCES has become a promising tool to assess Web credibility, most existing systems adopt a passive way to collect users' ratings (i.e., they wait for users to submit ratings, but actually only a few users voluntarily provide Web credibility assessments), which incurs two crucial challenges. First, given the huge volume of Web pages, a considerable fraction of them have no credibility information. For instance, based on our analysis, among the top 1 million domains in Alexa traffic ranking (www.alexa.com), only around 42.67% of them (as of January 9th, 2013) are covered by the most representative credibility evaluation site MyWOT, not to mention the domains with low popularity.<sup>1</sup> Furthermore, most domains covered by MyWOT have a limited amount of ratings, i.e., the confidence of their credibility information is low.

Second, malicious users may submit fake ratings to attack certain Web content. Although existing reputation systems can handle average malicious users, they are not effective in detecting smart attackers. In [14], a new type of attack called imitating attack is identified and verified: an attacker queries the credibility of certain Web content, when he receives the rating from the system, he just copies and resubmits the same rating to the system again as his own contribution.<sup>2</sup> From the perspective of the system, this attacker behaves quite similarly to a highly reputable user because his ratings are always consistent with the system's ratings. In this way, the attacker can easily build high reputation by cheating the system and then effectively attack certain Web content. A machine learning based defense mechanism is proposed in [14], but its computational complexity analysis is missing, so its applicability in a large-scale system with millions of users has not been verified.

In order to address the two challenges mentioned above, we propose to integrate recommendation functionality into a WCES to (1) attract users to rate more Web pages to increase the coverage of the system and (2) defend against the imitating attack to make the system more robust. To achieve the first goal, we propose a recommendation model to learn users' interests in Web content by fusing Matrix Factorization (MF) and Latent Dirichlet Allocation (LDA) [4]. Specifically, each Web content is represented by a “bag-of-words”. We apply LDA to extract a set of topics for the Web content, and assign a latent factor vector to each topic. A user's interest in a Web content is inferred by combining (1) the correlation between a user and the topics (by multiplying user-specific and topic-specific latent factors) and (2) the correlation between the Web content and the topics (by LDA).

In order to realize the second goal, we propose a recommendation based defense mechanism. The system first selects a set of active users<sup>3</sup> and recommends a set of interesting Web pages to them. Along with a recommended content, a fake credibility rating is shown and the system entices users to provide their ratings to make the system's rating more confident. Since imitating attackers simply copy system's ratings, they will copy (submit) the fake rating with a high probability. On the other hand, honest users often spend efforts in evaluating the recommended Web content, and submit a rating that is closer to the real credibility. We propose to model users' responses to the recommended Web content using beta distribution to detect imitating attackers.

To further enhance the effectiveness and efficacy of the integrated recommendation functionality, we design an adaptive reputation system to motivate users to more actively rate the recommended Web content. The basic idea is to assign different reputation points to users when they rate Web content in different ways. For instance, more reputation will be awarded if a user rates a recommended content than a self-selected content. Since rating the recommended Web content can boost reputation rapidly, both honest users and attackers are motivated to actively interact with recommendations thus further improving the system's coverage and robustness.

Although Web credibility, recommender systems and reputation systems have been well studied in their respective literature, to the best of our knowledge, this work is the first one that seamlessly integrates diverse information sources by applying various information retrieval technigues to realize a highly effective and robust WCES. The contributions of this work are summarized as follows: (1) In order to handle the challenges of coverage and robustness, we propose to integrate recommendation functionality into a WCES (see Section 3 System model). Note that such a system is independent and selfcontained, i.e., it is not designed as a component of other information systems, e.g., Web search engines. (2) By combining MF and LDA, we propose a personalized recommendation model to motivate users to rate more Web pages (Section 4.1). (3) In order to defend against the imitating attack, we propose a recommendation based defense mechanism. The system recommends a set of Web pages with fake credibility ratings to users and analyzes their rating behavior in the presence of recommendations. Beta distribution is used to model a user's imitating behavior probability (Section 4.2). (4) For the purpose of enhancing the effectiveness of the integrated recommendation functionality, in Section 4.3, we design an adaptive reputation system to award more reputation points when a user rates the recommended Web content. This not only motivates normal users to rate more to increase system's coverage, but also entices malicious users to copy fake credibility rating (i.e., get detected). (5) We evaluate the effectiveness of the recommendation functionality using the data published by Wikimedia foundation as well as a simulated multi-agent system (Section 5).

## 2. Background and related work

## 2.1. Web credibility

Quite a few works have identified a variety of factors that may influence an individual's perception of Web credibility [7,6,24]. For instance, Schwarz et al. [20] showed that visualizations by considering features such as Webpage popularity, domain type and the PageRank metric, can improve a user's Web credibility assessment in Web search results.

Recently, WCES has become popular in both academia and industry. Sharifi et al. [22] proposed SmartNotes, a crowdsourcing system to detect Web security threats such as Internet scams. Machine learning and natural language processing are applied to analyze and integrate users' reports. In [18], Web credibility is assessed by a decentralized recommender system. A single credibility metric is derived by combining three components: (1) item-based collaborative filtering, which is based on features identified from pages' textual contents, (2) userbased collaborative filtering, which is based on users' social relationships and (3) Web search page ranking.

In practice, MyWOT is a real-world example of a WCES that can have a real economic impact on content providers. In MyWOT, entire domains receive credibility ratings, and these ratings are later used by a Web browser extension that displays them next to Google search results. A domain that has a very low rating could therefore experience a significant decrease of Web traffic, even if it would be ranked high by Google. Therefore, a competitor of some commercial company would have a real incentive to maliciously decrease his competitor's credibility rating. This could be achieved through several simple means, such as spamming the MyWOT system automatically with negative credibility ratings. However, such crude means could be equally easily detected. This motivates attackers to devise more sophisticated means, out of which an imitating attack is one of the least expensive and most effective.

Although WCES has been studied recently, its robustness issue is relatively unexplored. Most existing solutions apply reputation systems to constrain users' rating behavior, however, smart attackers can easily cheat for high reputation. Liu et al. [14] identified a new type of attack called imitating attack, where a malicious user simply copies and resubmits the system's ratings to pretend to be a reputable user to gain high reputation. By studying Web pages' characteristics and users' rating behavior patterns, a two-stage machine learning based defense mechanism is proposed. Experimental results demonstrate the effectiveness of the approach, but its computational complexity analysis is not provided. In this work, we try to defend against the imitating attack using a light-weight, recommendation based approach.

## 2.2. Recommender systems

Although no recommendation is provided in existing WCES, recommender systems have been widely studied in many other application scenarios such as e-commerce and online social networks. Traditional recommender systems rely on collaborative filtering [1], which predicts a user's interest in an item by mining rating information of other similar users and items. In particular, MF has been proved to be one of the most effective methods in terms of rating prediction [12].

In order to improve recommendation quality, a variety of types of information, e.g., social information and contextual information is integrated into MF. For instance, in [13], the authors applied random decision trees to combine diverse types of contexts. Social information is integrated as a MF regularization term, but different from previous work [15], contexts are considered when measuring user similarity. Recently, content based recommendation has been improved by fusing topic modeling and MF [2,16]. The basic idea is to assign a latent topic to each word of an item, and then generate item latent factors by averaging the topics of all words associated with this item. A missing rating is predicted by combining the target user's affinity to the topics and the correlation between the topics and the target item.

Any collaborative recommender system that takes as input users ratings is vulnerable to the imitating attack. An example can be MovieLens, a system for recommending movies (www.movielens.org) that lets a user search for a movie and rate it. This means that users select movies they want to rate, and see the system's recommendation before they rate. These are the necessary condition for vulnerability to the imitating attack and a variety of other attacks. Needless to say, movie distributors have a real incentive to influence the ratings of this popular service.

## 2.3. Reputation systems

Reputation systems have been widely deployed in many online applications (e.g., online auction sites) to constrain malicious users' behavior [10]. The beta reputation system proposed by Josang et al. [9] estimates the reputation of an agent using a probabilistic model, i.e., based on the beta probability density function (PDF). The distribution parameters α and $\beta$ are determined by the number of successful and unsuccessful interactions between a pair of agents. On the basis of beta reputation system, Travos et al. [23] paid more attention to the issue of fake third party feedback. That is, if firsthand experience is insufficient to reliably estimate the reputation of the target agent, second hand experience is used, considering the reliability of the information provider.

In WCES, e.g., MyWOT, a reputation system is also applied. Reputation scores are assigned to users if they provide credibility ratings and the weight of a user's rating on the final credibility aggregation is determined by his reputation. Although MyWOT does not reveal details of how reputation is computed, a user's reputation is indeed proportional to the activeness of his rating behavior: “When you start using MyWOT, your ratings have little weight, but if you keep rating sites consistently, your ratings will be considered more reliable over time<sup>4</sup>”. As discussed in [14], imitating attackers can easily cheat such a reputation system by frequently copying system's ratings. Furthermore, current reputation systems are not particularly designed for recommendation based credibility assessment, so in this work, we propose an adaptive reputation system to both motivate users to rate recommended Web content and assist to expose imitating attackers.

## 3. System model

Logically, a WCES acts as a knowledge repository that provides credibility ratings for the queried Web content. Fig. 1 demonstrates how a WCES works. A user browses a Web content and rates it (if she wants) based on her personal judgment about the credibility of this content. The rating is then submitted to the system for contributing to the final credibility of this Web content. As a consumer, a user may also query the credibility of certain Web content for decision making. The system processes the query (via query engine) by checking its credibility information storage module and returns the rating information (if any) which is derived by credibility calculation engine. Reputation system is used to assess the reliability of individual users based on their past rating behavior, which is stored in user information storage module. Typically, more reputable users' ratings have higher impact on the final credibility assessment.

On the basis of a traditional WCES model, we add the recommendation functionality by integrating a recommendation component (see Fig. 1, red box). Web content recommendation engine serves two purposes: (1) it provides personalized Web content recommendation to individual users to attract them to rate more recommended Web pages (see Section 4.1). (2) It deliberately recommends Web content with fake credibility information to suspicious users and analyzes their reactions to the recommendations. Users with evident imitation behavior will be detected (see Section 4.2).

Note that within our Reconcile project, the proposed model has been implemented as a prototype WCES (http://reconcile.pl). The Reconcile system works similarly to MyWOT — users can install a browser extension that receives ratings from the Reconcile backend. The system has been designed to be resistant to adversaries, because little weight is given to ratings received from users who select the rated content themselves, and who have a low reputation. In order to earn reputation, a user has to rate Web pages chosen by the recommender system, which are displayed in the “Suggested pages” panel. The recommender system works similarly to the recommendation method described in Section 4.1. When a user submits a rating, the rating is used to update her reputation, using the method described in Section 4.3. Overall, the proposed method gives a significant degree of protection not just against imitating attacks, but also against coalition attacks and other kinds of adversary strategies.

## 4. Recommendation functionality integration

## 4.1. A personalized Web content recommendation model

The goal of our recommendation model is to recommend Web pages that are likely to interest individual users such that they will rate more Web pages to significantly increase the system's coverage. We denote a set of Web pages by $\mathcal { P } = \{ p _ { 1 } , p _ { 2 } , \ldots \}$ . Each Web content is associated with a credibility rating that is a discrete quantitative value in the range $L = \{ l _ { 1 } , l _ { 2 } , . . . , l _ { l } \} \cup l _ { 0 } ,$ , where l indicates that a Web content's credibility rating is unknown. $\mathcal { U } = \{ u _ { 1 } , u _ { 2 } , \ldots \}$ denotes a set of users participating in the WCES.

We use MF [12], which is the state-of-the-art collaborative filtering technique to build our recommendation model. We first construct a probability matrix $M ^ { p } \in \mathcal { R } ^ { | \mathcal { U } | \times | \mathcal { P } | }$ which records the interactions between <sup>R</sup>users and Web content. An element $m _ { u , c } ^ { p }$ is 1 if user u has rated the Web content c, otherwise, the element is empty (i.e., missing). We then apply MF to factorize $M ^ { p }$ into one user specific matrix $U ^ { p } \in \mathcal { R } ^ { k _ { p } \times | \mathcal { U } | }$ and one Web content specific matrix $V ^ { p } \in \mathcal { R } ^ { k _ { p } \times | \mathcal { P } | }$ . Each user u's latent factor vector $U _ { u } ^ { p }$ <sup>R</sup>and each Web content $c ^ { \prime } s$ latent factor vector $V _ { c } ^ { p }$ can be derived (iteratively updated) over existing matrix entries by performing stochastic gradient descent (SGD) [8]: $\begin{array} { r } { U _ { u } ^ { p }  U _ { u } ^ { p } - \gamma \frac { \partial L } { U _ { u } ^ { p } } } \end{array}$ 2 $\begin{array} { r } { V _ { c } ^ { p }  V _ { c } ^ { p } - \gamma \frac { \partial L } { V _ { c } ^ { p } } } \end{array}$ , where γ is the learning rate. Eqs. (1) and (2) show how gradient descent is performed with respect to $U ^ { p }$ and $V ^ { p }$ respectively.

$$
\frac {\partial L}{U _ {u} ^ {p}} = e _ {u, c} V _ {u} ^ {p} - \lambda U _ {u} ^ {p},\tag{1}
$$

$$
\frac {\partial L}{V _ {c} ^ {p}} = e _ {u, c} U _ {u} ^ {p} - \lambda V _ {c} ^ {p},\tag{2}
$$

where $e _ { u , c }$ is the aggregated difference between the predicted value and the corresponding ground truth. The probability of an interaction between user u and a Web content c (i.e., u rated c) is then predicted:

$$
m _ {u, c} ^ {p} = \left(U _ {u} ^ {p}\right) ^ {T} V _ {c} ^ {p}.\tag{3}
$$

For the target user u, we sort in descending order a list of Web pages that have little credibility information and have not been rated by u based on the predicted probabilities, and recommend top-K Web pages to u.

## 4.1.1. Topic-boosted MF

Pure MF based approach recommends Web content to users based on their rating information. However, it is non-trivial to accurately interpret and infer a user's interest simply using ratings. For instance, rating based recommendation infers that a user is interested in sports news. However, this user actually only read and rated articles about basketball, and in particular, about NBA, so recommending other irrelevant sports news (based on similar users' ratings) like Formula One may not attract the user to rate. On the other hand, topic modeling is able to infer latent topic variables from a corpus of documents [4], and such topics can be naturally applied to describe the interest of a user based on the textual contents she has interacted with. We therefore propose to integrate texts into MF to improve the accuracy of interest matching.

![](/api/attachments/WV6YR97T/fulltext/images/19250d88cadcb84c7baf9c7200d4efe8e9b44c01ee2bb92b8bbf362810616811.jpg)  
Fig. 1. A system model for Web credibility evaluation with recommendation functionality. (For interpretation of the references to color in this figure, the reader is referred to the web version of this article.)

We first sample a set of Web pages as training data. The main content of every Web content is extracted<sup>5</sup> to form a textual content corpus . We then apply LDA, a popular topic model on the corpus to extract D topics. Different from previous work [16] where the dimensionality of user/item latent factor vector is bounded by the number of topics, in this work, each topic is also associated with a latent factor vector, sharing the same latent space with the user specific latent factors.

Accordingly, the correlation between a user and a Web content, which was captured through the user specific and Web content specific latent factors (see Eq. (3)), is reformulated by incorporating the effect of texts/topics. Specifically, Web content specific matrix $V ^ { p }$ is represented by the product of two matrices:

$$
V ^ {p} = X Y,\tag{4}
$$

where XE $\mathcal { R } ^ { k _ { p } \times D }$ is the topic specific latent factor matrix. Each column of X is a latent factor vector that characterizes the corresponding topic. Y ∈ $\mathcal { R } ^ { D \times | \mathcal { P } | }$ is a matrix that stores correlations between Web content and topics. For a Web content $c ,$ we extract its main content to construct “bag-of-words”, denoted by $T _ { c } .$ . LDA assigns a latent topic t to each word $w \in T _ { c }$ with a probability $\zeta _ { w , t } .$ . The correlation between topic t and Web content c is calculated by averaging the topic distribution of all words from $T _ { c } \colon Y _ { c , t } = \frac { \sum _ { i = 1 } ^ { N _ { c } } \zeta _ { i , t } } { N _ { c } }$ , where $N _ { c }$ is the number of words extracted from $T _ { c }$ . Therefore, when inferring user u's interest in Web content $c ,$ u's interests in the D topics are firstly measured through user specific and topic specific latent factors, and then the correlations between the D topics and the Web content c are obtained, finally the two factors are fused to capture u's interest in c.

With topics, the correlation between users and Web content can be more meaningfully inferred than traditional approaches where only rating information (less interpretable) is used. Furthermore, the dimensionality of latent factor vector is not bounded by the number of topics thus is more flexible (i.e., the optimal dimensionality and topic number may not be identical, thus should be learned separately). By incorporating topics, the objective function is redefined to minimize the sum of prediction errors:

$$
L ^ {\prime} = \min _ {U, X} \frac {1}{2} \sum_ {u = 1} ^ {| \mathcal {U} |} \sum_ {c = 1} ^ {| \mathcal {P} |} I _ {u c} \left(R _ {u c} - \left(U _ {u} ^ {p}\right) ^ {T} X Y _ {c}\right) ^ {2} + \frac {\lambda^ {\prime}}{2} \left(\| U \| _ {F} ^ {2} + \| X \| _ {F} ^ {2}\right).\tag{5}
$$

We apply SGD to optimize this objective function by performing gradient descent with respect to latent factors $U ^ { p }$ and X:

$$
\frac {\partial L ^ {\prime}}{U _ {u} ^ {p}} = e _ {u, c} X Y _ {c} - \lambda^ {\prime} U _ {u} ^ {p},\tag{6}
$$

$$
\frac {\partial L ^ {\prime}}{X} = e _ {u, c} U _ {u} ^ {p} Y _ {c} ^ {T} - \lambda^ {\prime} X,\tag{7}
$$

where $e _ { u , c }$ is the difference between the predicted value and the corresponding ground truth. The final user specific matrix $U ^ { p }$ and topic specific matrix X are obtained by being iteratively updated: $U _ { u } ^ { p } \gets U _ { u } ^ { p } -$ $\begin{array} { r } { \gamma ^ { \prime } \frac { \partial L ^ { \prime } } { U _ { u } ^ { p } } \mathrm { a n d } X \gets X - \gamma ^ { \prime } \frac { \partial L ^ { \prime } } { X } , } \end{array}$ , where γ′ is the learning rate. By integrating topics which are extracted from textual contents into MF, we predict the probability that user u will rate a Web content c, which has no or insufficient ratings. According to the predicted probabilities, we sort a list of candidate Web pages, among which we recommend top-K ones to user u.

## 4.1.2. Discussion

Note that in practice, to make Web content recommendation not only precise and personalized, but also secure and reliable, security mechanisms should be applied. For instance, machine learning can be applied to make the first estimate of the credibility of Web content [5, 14], and some third party services, e.g., PhishTanks (www.phishtank. com) and DNSBL (www.dnsbl.info) can be used to expose phishing sites and Web spam. The Web content with security concerns must not be recommended to users even if their contents “look” interesting.

![](/api/attachments/WV6YR97T/fulltext/images/65288c3cd904ea27e16d14ccbe47ae1f7842f51ea0af352a54f415a5ea206ea8.jpg)  
Fig. 2. Recommendation based defense.

Based on the integrated recommendation component, more services can be developed. For instance, the system is able to recommend credible Web content to users for wise decision making in various fields (e.g., a location-based restaurant recommendation service); users with similar interests (learned from their ratings or credibility query histories) can form a credibility based online social network for credible information sharing. We leave the discussion on more sophisticated services as future work.

4.2. Recommendation based defense mechanism against the imitating attack

Besides recommending interesting Web content to users to increase the system's coverage, another functionality that our recommendation component offers is to defend against the imitating attack, which is particularly harmful to WCES, i.e., existing reputation system is ineffective in detecting such attacks. In this section, we propose a defense mecha nism by analyzing users' responses to recommendations.

As demonstrated in [14], to quickly build high reputation, imitating attackers typically densely copy and re-submit system's ratings within a short period of time. We therefore focus on the highly active users to detect imitating attack.

Based on their activities over the past period of time, e.g., 24 h, a set of active users are selected. For each user, we recommend a list of Web pages based on her interest (see Section 4.1). Fig. 2 demonstrates how the imitating attackers and normal users are expected to react to recommendations. We assume the recommended Web pages already have reliable credibility information, but instead of showing the exact ratings to users, the system provides fake ratings<sup>6</sup> and asks for new ratings to make the current fake ratings more “confident”. For instance, a recommended Web content has a credibility rating of 4-point (assuming five-point Likert-scale), but the system displays 2-point to the selected users. The basic idea of manipulating ratings is to entice imitating attackers to copy the fake ratings, which can be used as the evidence for attack detection. For a normal user, if she decides to rate the recommended Web content, her ratings are expected to be closer to the real credibility rating than to the displayed fake rating. On the other hand, imitating attackers may simply copy the fake ratings without actually assessing the recommended Web content so their ratings are close to the displayed fake ratings with high probability. It is worth mentioning that controversial topics, as well as users' bias/subjectivity make the ratings comparison non-trivial. However, this issue is not the focus of this paper, and we assume that the system has certain mechanism to detect and handle controversial contents [19]. Another option is to recommend only the Web content whose credibility can be objectively measured.

By comparing the displayed fake ratings and users' ratings, we are able to estimate a user's imitation behavior. For a user u, we denote a vector of recommended Web pages that user u has rated by $P _ { u } ^ { r } = \{ p _ { 1 } ^ { r } , p _ { 2 } ^ { r } , \ldots \}$ . The corresponding fake ratings (provided by the system) are denoted by $L ^ { f } = \{ l _ { 1 } ^ { f } , l _ { 2 } ^ { f } , \ldots \} $ , and the user's ratings are denoted by $L ^ { u } = \{ l _ { 1 } ^ { u } , l _ { 2 } ^ { u } , \ldots \}$ . We say u's rating l<sup>u</sup> is consistent with the corresponding fake rating l <sup>f</sup> if $\Delta l _ { i } = | l _ { i } ^ { u } - l _ { i } ^ { f } |$ is smaller than or equal to a predefined threshold (e.g., 1 in 5-point Likert-scale). We then have a vector of rating consistence indicators $\Theta _ { u } = \{ \theta _ { 1 } , \theta _ { 2 } , . . . \}$ , where $\theta _ { i } = 1$ indicates that u's ith rating is consistent with the corresponding fake rating, otherwise, θ is 0.

To infer the probability that user u performs imitation behavior, we apply Beta distribution, which is commonly used to model the uncertainty of the probability of a random event. We model a series of consistence indicators, i.e., Θ as observations of independent Bernoulli trials. In each trial, the success probability is modeled by Beta distribution with parameters α and β (we start with $\alpha = \beta = 1 )$ ). After observing s successes in n trials, the posterior density of the probability is Beta $( \alpha + s ,$ $\beta + n - s )$ . Accordingly, the density function of the probability of performing imitation behavior (by user u) is given by:

$$
f \left(p _ {u} ^ {i m i} | \alpha_ {u}, \beta_ {u}\right) = \frac {\Gamma (\alpha_ {u} + \beta_ {u} + 2)}{\Gamma (\alpha_ {u} + 1) \Gamma (\beta_ {u} + 1)} \left(p _ {u} ^ {i m i}\right) ^ {\alpha_ {u}} \left(1 - p _ {u} ^ {i m i}\right) ^ {\beta_ {u}},\tag{8}
$$

where $p _ { u } ^ { i m i }$ indicates the probability that u performs imitation behavior, $\alpha _ { u } \left( \geq 0 \right)$ and $\beta _ { u } \left( \geq 0 \right)$ represent the numbers of u's ratings that are consistent with the fake ratings or not respectively. Γ(.) is the gamma function. The expectation probability<sup>7</sup> is then obtained by:

$$
p _ {u} ^ {i m i} = \frac {\alpha_ {u} + 1}{\alpha_ {u} + \beta_ {u} + 2}.\tag{9}
$$

So if a user's imitation behavior probability is higher than a predefined threshold, this user is considered as imitating attacker. In contrast to existing solutions that reply on complex machine learning algorithms [14], the core of our defense mechanism is to derive a simple posterior imitation behavior probability, thus can be easily applied to large-scale settings.

![](/api/attachments/WV6YR97T/fulltext/images/04728bc6758102bca629dffa054729b49fbda18700241133ae10da88c1ee6213.jpg)  
(a) Recall.

![](/api/attachments/WV6YR97T/fulltext/images/45c1edcafd210fff87ab9826a78ae5f46d39dca43111426c6da52b6fac122921.jpg)  
(b) Precision.  
Fig. 3. Impact of the dimensionality of latent factors.

The effectiveness of such a defense mechanism depends on the performance of our recommendation model. If users actively rate the recommended Web content, their behaviors can be comprehensively analyzed, and malicious users can be reliably detected. Otherwise, if users refuse to rate, it is not possible to distinguish imitating attackers from normal users. In order to further motivate users to actively rate the recommended Web content, besides personalized recommendation, we also design an adaptive reputation system which will be elaborated in the next section.

## 4.3. An adaptive reputation system

A user rates Web content in two ways: (1) She rates Web pages that are selected by herself. System is not involved in the selection process. (2) She rates Web pages that are recommended by the system (see Section 4.1). In existing systems, to make users more active in assessing Web content, reputation points are awarded to rating submitters. Based on this principle, we identify three scenarios where different reputation points are awarded in different scenarios. If a user rates a self-selected Web content, (1) if this Web content has no or only very little credibility information, the system will give reputation points R<sup>0</sup>; (2) otherwise, if the system already has sufficient ratings of this Web content, reputation points of R<sup>1</sup> are assigned to the user; (3) if the user rates a recommended Web content, the system will give reputation points of R . Obviously, the ratings are particularly valuable if a Web content has little credibility information, so $R _ { s } ^ { 0 } \gg R _ { s } ^ { 1 }$ . Furthermore, since Web content recommendation serves the purposes of both increasing the system's coverage and detecting malicious users, R is set to larger than R<sup>0</sup>. An example of reputation point distribution could be $R _ { s } ^ { 0 } = 1 0 , R _ { s } ^ { 1 } = 0 . 1$ and $R _ { r } = 2 0$

Reputation points can be not only awarded, but also deducted. When the system detects that a user submitted a fake rating, the corresponding reputation points (previously awarded by the system) are deducted from her reputation.<sup>8</sup> Since more reputation points give users more privileges such as becoming community leader, reducing advertisements, etc., users are motivated to rate Web content with little credibility information, or those that are recommended by the system, thus increasing the system's coverage, as well as benefiting the recommendation based defense mechanism.

We notice that imitating attackers can still gain reputation if they refuse to rate the recommended Web content (avoid being detected) but keep copying system's ratings (e.g., slowly aggregating R<sup>1</sup>). We can reduce this effect by setting the maximum rating submission limit, e.g., 100 per day.

## 5. Evaluation

## 5.1. Methodology

Firstly, we evaluate the performance of the integrated recommendation functionality, which is the core contribution of this paper. We use the dataset of Article Feedback Tool (aft) v.4 published by Wikimedia Foundation.<sup>9</sup> The dataset contains 2,029,466 users (48,948 of them are registered users) who issued 2,451,497 ratings to 715,444 Wikipedia articles. The credibility of an article is measured from four aspects: trustworthy, objective, complete and readable. For each user, we sort the articles that she has rated in chronological order and select the first 80% of the ratings as training data and test the rest ones.

We compare the performance of our recommendation model with several baselines: (1) Random recommendation. This approach recommends a list of randomly selected articles to a user. (2) LDA. Each word in an article is associated with a distribution over topics derived by LDA. By measuring the similarity of topic distributions of a pair of articles, this approach recommends a list of articles that are the most similar to the ones that have been rated by the target user.(3) MF. In this approach, MF is applied to predict a user's interest in an item without taking into account textual contents (see Eq. (3)). A list of articles that are mostly likely to interest users is recommended.

To measure the accuracy of recommendations, we use two standard metrics: Precision@ K, which defines the ratio of successfully predicted articles to the K recommendations and Recall@ K, which defines the ratio of successfully predicted articles to the number of articles to be predicted.

Secondly, we evaluate the entire system as a whole. To the best of our knowledge, this is the first work that integrates recommendation system and reputation system into a Web content credibility evaluation system to improve its robustness and effectiveness, so no suitable dataset is publicly available. To conduct experiments, we build a multi-agent system<sup>10</sup> with 1000 Websites and 100 users consisting of honest users and imitating attackers. The fraction of imitating attackers is denoted by F. To make the simulation as realistic as possible, we further divide these attackers into three groups: (1) Naive attackers who copy the fake ratings of 80% of recommended Websites and submit random ratings for the rest ones; (2) Medium attackers who copy the fake ratings of 50% of recommended Websites, and submit random ratings for the rest ones; (3) Smart attackers who copy the fake ratings of 20% of recommended Websites, and submit random ratings for the rest ones. The fractions of different types of attackers are denoted by $F _ { n } , F _ { m }$ and $F _ { s }$ respectively $( F = F _ { n } + F _ { m } + F _ { s } )$ . On the other hand, we set that the probability of copying fake ratings for honest users follows Gaussian distribution $\mathcal { N } ( \mu = 0 . 1 , ~ \sigma = 0 . 1 )$ . Note that defending against diverse types of malicious users is essential for a practical system, but in this work, we are focusing on imitating attack only.

![](/api/attachments/WV6YR97T/fulltext/images/dcd668fa9aa62d70c2e8f81b1b28a43ba0053997678733e6accba2de5f482cf9.jpg)  
(a) Recall.

![](/api/attachments/WV6YR97T/fulltext/images/9511efcd86427493022287b74567469248b449a3ee1cdcb7d69075f80a6d539c.jpg)  
(b) Precision.  
Fig. 4. Impact of the number of iterations.

The metrics used in the evaluation include precision (the ratio of detected attackers to the total number of predictions $\textstyle { M _ { P } } )$ , recall (the ratio of detected attackers to all attackers $M _ { R } )$ and F-measure (the combination of precision and recall: $M _ { F } = 2 M _ { p } M _ { R } / ( M _ { P } + M _ { R } ) )$ .

Regarding the adaptive reputation system, each user is awarded points when he/she rated the credibility of certain Web content. We will study the reputation distribution of honest users and imitating attackers to demonstrate how users' behavior is captured by our adaptive reputation system, and the interplay between the recommendation system and the reputation system.

## 5.2. Results

## 5.2.1. Personalized recommendation

We first report the performance of our Web content recommendation component. Figs. 3 and 4 show how precision@ K and recall@ K vary with different values of (1) latent factor vector dimensionality $k _ { p }$ and (2) number of iterations of SGD I. Note that K is set to 5 for this set of experiments. We observe that both precision@ K and recall@ K first increase, but when arriving at a certain point, they start decreasing and then become stable afterwards. This is because although MF is effective in rating prediction, recommendation is essentially a ranking problem, thus may not be optimized by directly applying MF. Nevertheless, we note that $k _ { p } = 1 2$ and I = 50 are the optimal values that maximize the performance. In the following experiments, we use these values for our approach.

![](/api/attachments/WV6YR97T/fulltext/images/2b4f14d9a2276a710e857d37fb2488008d3e7f9ba58a6494fca43c50ea0cab62.jpg)

Another parameter that influences the performance of our approach is the number of topics. Fig. 5 shows how precision@ 5 and recall@ 5 vary with different numbers of topics. We observe that more topics increase both precision and recall, but starting from around 50, larger number of topics brings very limited improvement on the performance. Considering the tradeoff between precision/recall and computational overheads, we set the number of topics to 50 in the following experiments.

Once parameters of our recommendation approach are tuned, we compare the performance of our approach with that of various baselines (see Section 5.1). Fig. 6 shows the performance of various methods with different size of recommendation list. Obviously, for all approaches, the larger the recommendation list, the higher probability the interesting Web pages are recommended to individual users. So recall increases with the increasing size of the recommendation list. On the other hand, larger recommendation list size lowers down the corresponding precision. As expected, random recommendation demonstrates very poor performance, only about 1.8% of users' interested Web pages were recommended when recommendation list size is as high as 10. Both MF and LDA significantly improve random recommendation, and LDA is slightly better than MF, indicating the importance of textual contents. In all cases, our approach consistently outperforms other approaches, demonstrating that integrating textual content into MF further improves the recommendation quality. In summary, for precision, our approach improves MF and LDA by 60.84% and 19.70% (on average)

(a) Recall.  
Fig. 5. Impact of the number of topics.  
![](/api/attachments/WV6YR97T/fulltext/images/3fa55c134df4d314c4ffe65435ea825e2bbdf25d1526a972501f21a800017e44.jpg)  
(b) Precision.

![](/api/attachments/WV6YR97T/fulltext/images/abd0ac7a732be8439211ad160fd438b095b69450f715afef13b76c8651966bc6.jpg)  
(a) Recall.

![](/api/attachments/WV6YR97T/fulltext/images/23b9ff91d45b72d0fcc17bcf620eb2c469a3c7a9132d266c5f8bad8aed5b308d.jpg)  
(b) Precision.  
Fig. 6. Performance comparison

respectively; for recall, the corresponding improvements are 64.45% and 23.55% (on average) respectively.

## 5.2.2. Overall evaluation

In this subsection, we evaluate the entire system by studying how different component influences the robustness of the system. Since the recommendation functionality has been thoroughly evaluated in the previous subsection, we assume top-5 Websites are provided, and accordingly a user will choose a recommended Website to rate with the probability of 16% (see Fig. 6). The threshold for determining whether a rating is consistent with system rating is set to 1.

![](/api/attachments/WV6YR97T/fulltext/images/591a58bdb93852b2362cb09fa2625131bce7fe9b19a93b793247b9cb94007ec5.jpg)  
(a) Performance with varying fraction of imitating attackers.

Fig. 7(a) shows the performance of our defense mechanism when the fraction of imitating attackers (F) varies from 0.2 to 0.8 with 0.1 as increment. Note that the fractions of different types of attackers are set as $F _ { n } = 0 . 5 , F _ { m } = 0 . 3$ and $F _ { s } = 0 . 2$ respectively. The imitating behavior probability threshold is set to 0.25. We observe that the recall does not change evidently with F. This is because no matter how F varies, $F _ { n } , F _ { m }$ and $F _ { s }$ remain unchanged, so the fraction of imitating attackers that can be detected by our defense mechanism is not affected. On the other hand, when F increases, the imitating attackers become dominant in the system, so the fraction of predictions that are able to successfully detect attackers (i.e., precision) also increases.

![](/api/attachments/WV6YR97T/fulltext/images/b02473d06fce47d445d6c63e421b3bf3eaf5195e1131008664fda248222b63ab.jpg)  
(b) Performance with varying fraction of smart imitating attackers (in all imitating attackers).

![](/api/attachments/WV6YR97T/fulltext/images/67b01a543207f13fbfac0b691f1af53e90c9fb9e4cc618a9635321d9922a609b.jpg)  
(c) Performance with varying imitating behavior probability threshold.  
Fig. 7. Performance in different attack scenarios.

![](/api/attachments/WV6YR97T/fulltext/images/6339c1f229d16a03cba5edc568aa2dcf5ffca03e7b56f26c29809590c5a06780.jpg)  
(a) With recommendation functionality.

![](/api/attachments/WV6YR97T/fulltext/images/7dfbc28c04583ddde4785fb4c2bc373759eb3dc1158c3957c6da84b6ae1eec26.jpg)  
(b) Without recommendation functionality.  
Fig. 8. Reputation distribution.

Smart attackers behave similarly to normal users, thus are more difficult to be detected. We then demonstrate how the fraction of smart imitating attackers influences the performance of our approach (see Fig. 7(b)). We first set F = 0.3. Then we vary the fraction of smart attackers F from 0.2 to 0.8 with 0.1 as increment. Naive attackers and medium attackers equally share the rest portion. Obviously, the higher the fraction of smart imitating attackers, the lower the precision, recall and F-measure become. Nevertheless, we observe even when F is as high as 0.7, F-measure still reaches around 0.5, demonstrating the effectiveness of our defense mechanism.

We then demonstrate the impact of imitating behavior probability threshold (see Eq. (9)). Note that the fractions of various types of imitating attackers are set as F = 0.3, F<sub>n</sub> = 0.4, F<sub>m</sub> = 0.4 and F<sub>s</sub> = 0.2. From Fig. 7(c) we observe that extremely low or extremely high threshold incurs extremely low precision or recall, which is not acceptable. When the threshold is 0.4, F-measure is maximized in this set of experiments.

Finally, we study how the adaptive reputation system influences users' imitating behavior. We set that if a user rates a self-selected Website that already has sufficient ratings (i.e., the number of ratings is larger than the median of the number of ratings for all Websites in the system), 0.1 point is awarded; if the self-selected Website does not have sufficient ratings yet, 10 points are given. On the other hand, if the user rates a recommended Website, 20 points are assigned.<sup>11</sup> This is to motivate users to more actively interact with the recommendation component. In order to study the influence of the recommendation, we setup two experimental settings: reputation system with recommendation functionality, and that without recommendation. Periodically our simulator checks the correctness of ratings, if by comparing with the ground truth (derived as the mean of all corresponding ratings), a rating is determined to be incorrect, the corresponding amount of points are deducted from the corresponding user's reputation.

Fig. 8 demonstrates the Cumulative Distribution Function (CDF) of reputation points of honest users and different types of attackers. We divide users' reputation points into 7 ranges: [0,1000), [1000,1100), [1100,1200), [1200,1300), [1300,1400), [1400,1500) and [1500,1600). Such ranges can help to distinguish different reputation levels, which are more meaningful and interpretable than directly displaying numeric values. By comparing the results in the two settings, we observe that when recommendation functionality is provided, honest users reputations are significantly higher than that of imitating attackers. On the other hand, when recommendation functionality is absent, although honest users' reputation points are generally higher than that of imitating attackers, the difference is not significant. We thus conclude that the integrated recommendation system not only helps to directly detect imitating attackers, but also boosts reputation system, which provides an alternative way to study users' imitating behavior.

## 6. Conclusion

In this work, we have proposed to integrate recommendation functionality into a WCES to handle the issues of coverage and robustness. By fusing MF and LDA, a Web content recommendation model is proposed to attract users to rate more recommended Web content. On the other hand, to defend against the imitating attack, a recommendation based defense mechanism is proposed by investigating users' rating behavior in the presence of recommendations. Beta distribution is applied to model and predict a user's imitating behavior probability. Furthermore, we design an adaptive reputation system to further motivate users to actively interact with the integrated recommendation functionality.

Article feedback tool dataset and a simulated multi-agent system are used to validate the performance of the proposed recommendation model, imitating attack defense mechanism and adaptive reputation system. In summary, our recommendation approach improves MF and LDA by 60.84% and 19.70% respectively in terms of precision; for recall, the corresponding improvements are 64.45% and 23.55%, respectively. Regarding the recommendation based defense mechanism, by carefully choosing imitating behavior probability threshold, imitating attackers (even the smart ones) can be effectively detected.

A future direction is to take into account more information sources such as user's profiles, contextual information, and external knowledge databases (e.g., semantic linked data) to further improve the quality of recommendation. We also intend to study real user behavior on the deployed prototype system by leveraging Amazon Mechanical Turk and explore defense mechanisms for coalition attacks.

## Acknowledgment

This research is supported by the grant “Reconcile: Robust Online Credibility Evaluation of Web Content” from Switzerland through the Swiss Contribution to the enlarged European Union.

## References

[1] Gediminas Adomavicius, Alexander Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions JEEF Trans, Knowl, Data Eng, 17 (6) (June 2005) 734–749.

[2] Deepak Agarwal, Bee-Chung Chen, fLDA: matrix factorization through latent Dirichlet allocation, Proceedings of the Third ACM WSDM, 2010.

[3] R. Bartoszynski, M. Niewiadomska-Bugaj, Probability and Statistical Inference, Wiley-Interscience, 2008.

[4] David M. Blei, Andrew Y. Ng, Michael I. Jordan, Latent Dirichlet allocation, J. Mach. Learn. Res. 3 (2003) 993–1022.

[5] Carlos Castillo, Marcelo Mendoza, Barbara Poblete, Information credibility on twitter, Proceedings of the 20th WWW, 2011.

[6] B.J. Fogg, Jonathan Marshall, Othman Laraki, Alex Osipovich, Chris Varma, Nicholas Fang, Jyoti Paul, Akshay Rangnekar, John Shon, Preeti Swani, Marissa Treinen, What makes web sites credible?: a report on a large quantitative study, Proceedings of SIGCHI, 2001.

[7] B.J. Fogg, Hsiang Tseng, The elements of computer credibility, Proceedings of SIGCHI, 1999.

[8] Rainer Gemulla, Erik Nijkamp, Peter J. Haas, Yannis Sismanis, Large-scale matrix factorization with distributed stochastic gradient descent, Proceedings of the 17th ACM SIGKDD, 2011.

[9] R. Ismail, A. Josang, The beta reputation system, Proceedings of the 15th Bled Conference on Electronic Commerce, 2002.

[10] Audun Jøsang, Roslan Ismail, Colin Boyd, A survey of trust and reputation systems for online service provision, Decis. Support. Syst. 43 (2) (2007) 618–644.

[11] Michal Kakol, Michal Jankowski-Lorek, Katarzyna Abramczuk, Adam Wierzbicki, Michele Catasta, On the subjectivity and bias of web content credibility evaluations, The 3rd Joint WICOW/AIRWeb Workshop on Web Quality (with WWW 2013), 2013.

[12] Y. Koren, R. Bell, C. Volinsky, Matrix factorization techniques for recommender systems, Computer 42 (8) (2009) 30–37.

[13] Xin Liu, Karl Aberer, Soco: a social network aided context-aware recommender systems, Proceedings of the 22nd WWW, 2013.

[14] Xin Liu, Radoslaw Nielek, Adam Wierzbicki, Karl Aberer, Defending imitating attacks in web credibility evaluation systems, The 3rd Joint WICOW/AIRWeb Workshop on Web Quality (with WWW 2013), 2013.

[15] Hao Ma, Dengyong Zhou, Chao Liu, Michael R. Lyu, Irwin King, Recommender systems with social regularization, Proceedings of the 4th ACM WSDM, 2011.

[16] Julian McAuley, Jure Leskovec, Hidden factors and hidden topics: understanding rating dimensions with review text, Proceedings of the 7th ACM Conference on Recommender Systems, 2013.

[17] Alexandra Olteanu, Stanislav Peshterliev, Xin Liu, Karl Aberer, Web credibility: features exploration and credibility prediction Proceedings of 35th ECIR 2011.

[18] Thanasis G. Papaioannou, Jean-Eudes Ranvier, Alexandra Olteanu, Karl Aberer, A decentralized recommender system for effective web credibility assessment, Proceedings of the 21st ACM CIKM, 2012.

[19] Ana-Maria Popescu, Marco Pennacchiotti, Detecting controversial events from twitter Proceedings of the 19th ACM CIKM 2010

[20] Julia Schwarz, Meredith Morris, Augmenting web pages and search results to support credibility assessment, Proceedings of SIGCHI, 2011.

[21] Mehrbod Sharifi, Eugene Fink, Jaime G. Carbonell, SmartNotes: application of crowdsourcing to the detection of web threats, Proceedings of JEEE SMC 2011

[22] M. Sharifi, E. Fink, J.G. Carbonell, Detection of internet scam using logistic regression, Proceedings of IEEE SMC, 2011.

[23] W.T. Teacy, Jigar Patel, Nicholas R. Jennings, Michael Luck, Travos: trust and reputation in the context of inaccurate information sources. Auton. Agent. Multi-Agent Syst. 12 (2) (2006) 183–198.

[24] Yusuke Yamamoto, Katsumi Tanaka, Enhancing credibility judgment of web search results, Proceedings of SIGCHI, 2011.

![](/api/attachments/WV6YR97T/fulltext/images/56818dab309a21158b2fc9ea8ee8272f5d9a2f33f55adc733a1e7ca21e6f0584.jpg)  
Dr. Xin Liu is currently a scientist with Institute of Infocomm Research (I2R), Agency for Science, Technology and Research (A\*STAR). Before joining I2R, Xin was a postdoctoral researcher with Ecole Polytechnique Fédérale de Lausanne (EPFL), Switzerland. Before joining EPFL, Xin received his Ph.D. in Computer Science from Nanyang Technological University (NTU), Singapore. His current research focuses on (1) personalized recommendation models and their applications such as point of interest recommendation in location based social networks, (2) web content credibility assessment, and (3) trust modeling in information systems.

![](/api/attachments/WV6YR97T/fulltext/images/5748b5034a43a8a27f6753ff085f9621e4927b6c2f0c2dc3530a819b7896d40f.jpg)

Radoslaw Nielek is currently an assistant professor at Polish-Japanese Institute of Information Technology (PJIIT). He received his Ph.D. degree from Polish-Japanese Institute of In formation Technology (PIIIT) Warsaw. Poland. His Ph.D. thesis is titled “Designing Algorithms for Realising Social Goals”. He held a Bachelor's Degree in Production Engineering and Management of Szczecin University of Technology and Master's Degree in Computer Science of PJIIT. His research interests include social simulation, trust management and opinion mining.

![](/api/attachments/WV6YR97T/fulltext/images/1baa7a4352e30ffcaa080b5a982e36911ec74598a441e18976231bc21ff74317.jpg)

Paulina Adamska received her master's degree in computer science and is currently a teacher, research assistant, and PhD student at the Polish-Japanese Institute of Information Technology in 2009. She is coauthor of the middleware based on the generic Peer-to-Peer Protocol. Her interests include reputation systems, their influence on the quality of usergenerated content in learning communities (in particular Q&A systems), and the utilization of gamification mechanisms in order to motivate the posting of high-quality information.

![](/api/attachments/WV6YR97T/fulltext/images/2577a36244ea791edeff6c3ef1150e32aada845bebff6a41efe5a5b04ce7093b.jpg)

Adam Wierzbicki received his Ph.D. degree from the Warsaw University of Technology and a habilitation title from the Institute of Systems Research of the Polish Academy of Sciences. He is currently employed at the Polish-Japanese Institute for Information Technology, where he has the position of Full Professor and of Vice-President. He is an expert in Social Informatics and Peer-to-Peer computing. His current research interests focus on social informatics, in particular on credibility, trust management, collective intelligence and fairness in distributed systems. He has published several papers on trust management and on applications of the theor of equity to providing fairness in open distributed systems, and is the author of a Springer book titled “Trust and Fairness in Open, Distributed Systems”. He is also interested in open collaboration, particularly using Wiki technology. Since November, 2011, Dr. Wierzbicki leads the Reconcile project which is concerned with the development of tools for the evaluation of Web content credibility. Dr. Wierzbicki is the Steering Committee Chair of the In ternational Conference on Social Informatics (SocInfo).

![](/api/attachments/WV6YR97T/fulltext/images/e63a81524fd821483799465000675254ec110b7d2f072d93fbf46b40bfd3ac49.jpg)

Karl Aberer received the PhD degree in mathematics from the ETH Zurich in 1991, He has been a full professor of distributed information systems at the EPFL, Switzerland, since 2000. His research interests are on highly distributed information systems with applications in peer-to-peer search, semantic interoperability trust management mobile, socia and sensor networks, and smart energy systems. From 1991 to 1992, he was postdoctoral fellow at the International Computer Science Institute, University of California, Berkeley. In 1992, he joined the Integrated Publication and Information Systems institute at GMD in Germany, where he was leading the research division Open Adaptive Information Management Systems. From 2005 till 2012 he was the director of the Swiss National Research Center for Mobile Information and Communication Systems (NCCR-MICS www mics.ch). He is a member of the editorial boards of the VLDB Journal, the ACM Transaction on Autonomous and Adaptive Systems, and the World Wide Web Journal. He has also been consulting for the Swiss government in research and science policy as a member of the Swiss Research and Technology Council (SWTR) from 2004 to 2011.

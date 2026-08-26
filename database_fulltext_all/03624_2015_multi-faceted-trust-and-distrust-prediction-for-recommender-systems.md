---
otero_id: 3624
otero_key: "QNVGDQNG"
title: "Multi-faceted trust and distrust prediction for recommender systems"
authors: "Hui Fang; Guibing Guo; Jie Zhang"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.01.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Hui Fang, Guibing Guo ⁎, Jie Zhang

School of Computer Engineering, Nanyang Technological University, Singapore

## a r t i c l e i n f o

Article history: Received 27 December 2013 Received in revised form 3 November 2014 Accepted 6 January 2015 Available online 14 January 2015

Keywords: Trust Distrust Rating behavior Multi-facet Recommender systems

## a b s t r a c t

Many trust-aware recommender systems have explored the value of explicit trust, which is speci<sup>fi</sup>ed by users with binary values and simply treated as a concept with a single aspect. However, in social science, trust is known as a complex term with multiple facets, which has not been well exploited in prior recommender systems. In this paper, we attempt to address this issue by proposing a (dis)trust framework with considerations of both interpersonal and impersonal aspects of trust and distrust. Speci<sup>fi</sup>cally, four interpersonal aspects (benevolence, competence, integrity and predictability) are computationally modeled based on users' historic ratings, while impersonal aspects are formulated from the perspective of user connections in trust networks. Two logistic regression models are developed and trained by accommodating these factors, and then applied to predict continuous values of users' trust and distrust, respectively. Trust information is further re<sup>fi</sup>ned by corresponding predicted distrust information. The experimental results on real-world data sets demonstrate the effectiveness of our proposed model in further improving the performance of existing state-of-the-art trust-aware recommendation approaches.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Trust has been extensively exploited for improving the predictive accuracy of recommendations by ameliorating the issues such as data sparsity and cold start that recommender systems inherently suffer from [1,18,16,3,26,9,5]. In essence, trust provides additional information from which user preference can be better modeled, alternative or complementary to rating-based similarity. Both implicit trust [24] and explicit trust [18,3,16,26,9,5] have been investigated in the literature. The former trust is usually inferred from user-item interactions (i.e., ratings) whereas the latter is directly speci<sup>fi</sup>ed by users indicating whom and to what extent they trust. In contrast, although distrust is recognized to play an equivalently important role as trust [22], the investigation of utilizing distrust in recommender systems is still in its infancy [30,31]. To the best of our knowledge, no prior work has attempted to predict distrust for improving recommender systems.

Another issue of existent trust-aware recommender systems is the simpli<sup>fi</sup>ed modeling of trust as a concept with a single aspect, such as the ability to provide accurate ratings (known as competence) [24] or the probability of behaving maliciously. However, it is well acknowledged in social science that trust is a concept with multi-faceted properties [19,21,20]. One possible explanation is that only limited information is available in the few and publicly accessible data sets. Although some efforts have been made to capture multiple aspects (e.g. information credibility [12]) of raters (who give ratings) in recommender systems, they are essentially distinct concepts from trust. A generally agreed proposition states that people trusting each other may not always share similar preferences [10]. This statement leads to the following interesting research question: which aspects of (dis)trust reflect user preferences more and hence should be more considered for user preference modeling? The answer would provide a guidance on whom and to what extent one can trust, especially given the fact that most available (i.e. explicit) trust scores are binary, i.e., either 1 (trust) or −1 (distrust) without speci<sup>fi</sup>c degrees of trust or distrust.

In this paper, we aim to address the research question by proposing a framework of trust and distrust, taking into considerations both interpersonal and impersonal aspects of trust and distrust adapted from social science [20]. Speci<sup>fi</sup>cally, four interpersonal aspects (i.e., benevolence, competence, integrity and predictability) are computationally modeled based on users' past ratings, while impersonal aspects (e.g., degree centrality) are formulated from the perspective of social links in trust networks. Note that the social links in a trust network consist of both trust and distrust connections among users. Two logistic regression models are developed and trained by accommodating these factors and then applied to predict continuous values of users' trust and distrust, respectively.

We further re<sup>fi</sup>ne the trust information using the predicted distrust information. These newly generated trust values can then be applied into the existing trust-aware recommender algorithms (i.e. TidalTrust, Merge and SocialMF). The experimental results on real-world data sets demonstrate the effectiveness of our proposed model for improving the performance of three representative trust-aware recommendation algorithms. In addition, the generality of our model is also empirically demonstrated. In all, our work is the <sup>fi</sup>rst to comprehensively study the multiple aspects of trust and distrust in the context of recommender systems. The study results lead to re<sup>fi</sup>ned trust and distrust predictions, and in consequence notable improvement on recommendation accuracy when the predicted trust and distrust are utilized in recommendation approaches.

The rest of the paper is organized as follows. Section 2 gives an overview of related research in the literature. Section 3 elaborates the proposed (dis)trust framework, and Section 4 introduces the trust and distrust prediction models. The effectiveness of our approach is evaluated and discussed in Sections 5 and $6 ,$ respectively. Finally, the conclusion and future work are presented in Section 7.

## 2. Related work

Both trust and distrust are well-known as heterogenous rather than homogenous concepts in the <sup>fi</sup>elds of social science and computational trust, each of which is composed of multiple aspects [19,21]. Speci<sup>fi</sup>cally, Mayer et al. [19] report that the trust relationship between a trustor (who speci<sup>fi</sup>es trust statements) and a trustee (who receives trust statements) is mainly in<sup>fl</sup>uenced by the trustor's propensity to trust others in terms of three interpersonal aspects related with the trustee, namely ability (competence), benevolence and integrity. Mcknight and Chervany [21] enrich this model by adding one more aspect of the trustee—predictability as well as an impersonal aspect from the view of structural/institutional trust [20,21]. Impersonal aspects are often utilized to predict positive or negative user links [14,13] by virtue of the graph structures of social networks. We defer the formal de<sup>fi</sup>nitions of these aspects till Section 3. These frameworks have been adopted as the underpinning of the socio-cognitive trust theory in the area of computational trust [2]. Consistently, in this work we employ both interpersonal and impersonal aspects of the trustee along with the trustor's propensity to formulate users' trust and distrust.

Trust is also applied in real applications, such as Epinions.com where users can explicitly specify other users as trustworthy or untrustworthy. The value of trust has been explored by many trust-aware recommender systems, given the strong and positive correlation between trust and preference [28]. For example, Donovan and Smyth [24] treat trust as a single aspect and equivalent with the expertise or competence of users. Massa and Anesani [18] replace user similarity with explicitly speci<sup>fi</sup>ed trust relationships, and also allow trust relationships to propagate through the trust networks. They show that more robust recommendations can be produced without signi<sup>fi</sup>cant loss in accuracy. Golbeck [4] introduces a trust-<sup>fl</sup>ow-based method (called TidalTrust) to compute rating predictions for target items. She <sup>fi</sup>nds out that better accuracy can be achieved. Later works [3,26] claim that better performance can be obtained by integrating both trust and similarity for recommendations. Jamali and Ester [8] design the TrustWalker approach to randomly select neighbors in the trust network formed by users and their trusted neighbors. TrustWalker combines trust information of the selected neighbors with an item-based technique, where both the ratings of the target item and similar items are considered. The recent work conducted by Guo et al. [5] focuses on the problems of data sparsity and cold start from which traditional recommender systems suffer. They empirically contend that by merging the ratings of trusted neighbors, the preferences of active users can be better modeled and hence the performance is improved.

Other than these neighborhood-based approaches, trust is also adopted in model-based approaches. For example, Ma et al. [17] design a latent factor model called SoRec based on probabilistic matrix factorization [23]. They fuse the user-item rating matrix with user–user trust matrix by sharing a common latent low dimensional user feature matrix. The two matrices are factorized by three sets of latent features: user vector and feature vector (for each user), and item vector. Experimental results demonstrate that SoRec outperforms the basic matrix factorization model and other trust related neighborhood models. However, although the trust information is considered, the real world recommendation processes are not re<sup>fl</sup>ected, where the two sets of latent features for each user cause the low interpretability of the model. To overcome this problem and model trust-aware recommender systems more realistically, they further propose RSTE [16], a linear combination of a basic matrix factorization technique and a trustbased approach. Jamali and Ester [9] later enhance this model by enabling trust propagation in their SocialMF model. On the other hand, only very few works have been conducted to study the utility of distrust in recommender systems, although Victor et al. [31,30] have shown that distrust is indeed helpful in trust-aware recommender systems.

All the approaches mentioned above simply treat trust as a singleaspect term and adopt the explicit trust or distrust values without further adjustments. This simpli<sup>fi</sup>cation may work well when trust values can correctly refer to the trustworthiness of users. However, the exact <sup>fi</sup>ne-grained values of trust and distrust are often unavailable due to various concerns such as privacy issues. The most common form is simply the social links among users. In this case, the utility of trust and distrust may not be well exploited. Inaccurate or incomplete trust networks may further decline the performance of trust-aware recommender systems [29]. Therefore, we claim that it is important to infer and hence re<sup>fi</sup>ne trust and distrust links for better recommendation performance.

Very few approaches for recommender systems have been proposed to capture the heterogenous property of (dis)trust. For example, Kwon et al. [12] adopt the source credibility theory to select credible neighbors by investigating multiple credibility attributes. The concept of “credibility” is essentially distinct from that of “trust” de<sup>fi</sup>ned in our paper. Speci<sup>fi</sup>cally, the former concept refers to the reliability of users' ratings for a given item, i.e. the reliability of the recommender. The attributes considered for selecting credible recommenders are mainly expertise, trustworthiness, similarity and attraction. However, the latter focuses on a better trust network which is most suitable for recommender systems. We only consider choosing trustworthy recommenders based on a set of (dis)trust antecedents. We intend to empirically reveal the correlations of each aspect with the trust relationship, and target better predictions of trust and distrust for recommender systems.

## 3. The (Dis)trust framework

In this section, we introduce the formal de<sup>fi</sup>nitions of the interpersonal and impersonal aspects of trust and distrust from which they will be computationally modeled according to users' historic ratings and trust networks.

Trust in social science has been well recognized as a multi-faceted concept that consists of three major parts, namely dispositional trust, institutional/structural-based trust, and interpersonal trust [21]. Dispositional trust, also known as a trustor's trust propensity, refers to the trustor's inherent propensity to trust other users. Mathematically, it could be treated as a continuous constant (in the range of [0,1]) subject to each trustor. An Institutional/structural-based trust refers to a belief held by a trustor about impersonal things of a trustee such as environments and situation. Hence, in our framework, as all users are in the same environments, we differentiate this part of the trustee by regarding it as trustor's public view of the trustee's trustworthiness. This is mainly determined by impersonal aspects of the trustee such as her reputation and position in a trust network. The impersonal aspects also have an impact on trustor's perception and hence the trust evaluation [20]. Interpersonal trust mainly involves benevolence, integrity, competence, and predictability.

With respect to the original trust model in [19,21], we make minor modi<sup>fi</sup>cation towards the connections between the aspects and trust as shown in Fig. 1. Speci<sup>fi</sup>cally, we regard the combination of each aspect of a trustee and the propensity of a trustor as an aspect of the trustee perceived by the trustor, or a trusting belief of the trustor that the trustee has the corresponding characteristic in her favor. Therefore trust in our model is connected with four different trust beliefs (interpersonal aspects), each of which is regarded as a trust aspect of a trustee perceived by a trustor. Together with the trustor's trust propensity and impersonal aspects of the trustee, these aspects are known as the antecedents of trust [19,21], and elaborated as follows.

![](/api/attachments/QNVGDQNG/fulltext/images/1c5620828f3b7d22397db4a97099fcc9620138ccafdee0569c4c6bd3c2a9a817.jpg)  
Fig. 1. The proposed (dis)trust framework.

• Benevolence refers to the extent to which a trustee cares about the preferences of a trustor [21], i.e., the willingness of the trustee to do good deed for the trustor. For the user with whom the trustor has a high benevolence belief, her preferences are more likely to be similar with those of the trustor. In our case, it means that both users report similar ratings on many items.

• Integrity refers to the extent to which a trustee conforms to a norm or code of moral or artistic values [19]. It stresses the characteristic of the trustee to follow the norm or rules of an organization, and to have a core set of values to guide behaviors. To put it simply, the trustor believes that the trustee will always keep good-faith agreements, tell the truths, act ethically and ful<sup>fi</sup>ll the promises [21]. In contrast to benevolence, integrity is more concerned with the characteristic of the trustee than the trust relationship [21].

The aspects of benevolence and integrity are somehow complementary to each other in evaluating the trustworthiness of a speci<sup>fi</sup>c trustee. Speci<sup>fi</sup>cally, although benevolence shows the honesty or willingness of a trustee towards a trustor, it may fail to work in some scenarios where only limited interactions between the two users exist. This issue can be partially addressed by the integrity via considering the experience of all the users. Similarly, in the cases where integrity tends to be misleading, e.g., when most users are malicious, benevolence can help cope with this issue by relying more on personal experience between the two users.

• Competence refers to the ability or the power of a trustee to conduct the actions that are expected by a trustor in a speci<sup>fi</sup>c domain [19]. Hence, competence is domain (context)-speci<sup>fi</sup>c. For example, a user providing satisfying recommendations of purchasing cars may not be an expert of buying clothes. In other words, the user receiving a high competence belief from the trustor is capable of providing satisfactory recommendations to the trustor in a speci<sup>fi</sup>c context. The more experience the trustee has in the speci<sup>fi</sup>c context, the more competent she will be in the view of the trustor.

• Predictability refers to the consistency of a trustee's actions (good or bad, negative or positive) such that the trustor can make a prediction in a given situation [21]. Different from integrity, the value of predictability is neutral. Speci<sup>fi</sup>cally, users' high predictability could mean that they always provide relatively high or low recommendations in need of the trustor, or consistently meet the trustor's preferences. Predictability is able to alleviate the problem of behaviors changing strategically, that is, a user may <sup>fi</sup>rst act honestly but conduct

dishonest behaviors later.

• Impersonal aspects represent different situations a trustor may encounter when interacting with a trustee. In our framework, they summarize the aspects of a trustee from the public view, which are independent of the interpersonal relationship between trustor and trustee. The representative information includes trustee's reputation, position in the trustor network, degree centrality [25], authority, and even their pro<sup>fi</sup>le information, etc.

As mentioned above, distrust is recognized as a distinct construct and opposed to trust. Trust and distrust may exist simultaneously between a trustor and a trustee. Distrust is also a multi-faceted concept, and is formalized as the mirror image of the trust concept [20]. Similarly, we connect the distrust with the aspects identi<sup>fi</sup>ed in the framework, which is illustrated in Fig. 1.

## 4. Trust and distrust prediction

In this section, we <sup>fi</sup>rstly formulate the (dis)trust aspects based on users' historical experience. Then, we present two logistical regression models by accommodating these aspects to predict continuous values of users's trust and distrust, respectively. Finally, we further re<sup>fi</sup>ne the trust links given the predicted trust and distrust values.

## 4.1. Formulations of aspects

Given the formal de<sup>fi</sup>nitions, we proceed to formulate the four aspects in the light of users' historical experience (i.e., ratings). For clarity, we <sup>fi</sup>rst introduce a number of notations. Suppose there are two users: a trustor a and a trustee b, and each user has a set of experience denoted by $E _ { a }$ and $E _ { b } ,$ respectively. A piece of experience is denoted by a 5-tuple $e _ { u } = ( u , j , r _ { u , j } , t , c )$ , indicating that a user u rated item j with a rating $r _ { u , j }$ at time t under context c. Hence, users' experience can be represented as $E _ { a } = \{ e _ { a 1 } , . . . , e _ { a m } \}$ } and $E _ { b } = \{ e _ { b 1 } , . . . , e _ { b n } \}$ , where m and n are the number of experience of users a and b, respectively.

Based on user experience, we then model the four general trust aspects (i.e. beliefs, see Fig. 1) of trustee b from the viewpoint of trustor a, as well as the trust value that trustor a has towards trustee b. Note that belief could be modeled by evidence [27]. Following the de<sup>fi</sup>nitions described in Section 3, we model the four aspects as follows.

• Benevolence, Be(a, b). As benevolence refers to the closeness of shared experience between two users a and b, it is modeled as the user similarity which is usually used in collaborative <sup>fi</sup>ltering and computed by the Pearson correlation coef<sup>fi</sup>cient [1]:

$$
B e (a, b) = \frac {\sum_ {j \in E _ {a , b}} \left(r _ {a , j} - \bar {r} _ {a}\right) \left(r _ {b , j} - \bar {r} _ {b}\right)}{\sqrt {\sum_ {j \in E _ {a , b}} \left(r _ {a , j} - \bar {r} _ {a}\right) ^ {2} \sqrt {\sum_ {j \in E _ {a , b}} \left(r _ {b , j} - \bar {r} _ {b}\right) ^ {2}}},}\tag{1}
$$

where $E _ { a , b } = E _ { a } \cap E _ { b }$ is the set of shared experience on the commonly rated items between users a and b, and $\overline { { r } } _ { a } , \overline { { r } } _ { b }$ are the average of the ratings reported by users a and b, respectively. Alternative similarity measures such as cosine similarity [1] could also be applied.

• Integrity, In(b). As aforementioned, integrity is independent of the trustor–trustee relationship, hence it is formulated merely based on the past experience of the trustee regardless of the trustor's actions and evaluation. Speci<sup>fi</sup>cally, the behaviors of the majority are treated as the norm or the code when evaluating the integrity of the trustee, i.e., the similarity between the trustee's behaviors and the majority's. Hence, integrity is computed by the similarity between the preferences of the trustee and the average:

$$
I n (b) = \frac {\sum_ {j \in E _ {b}} \left(r _ {b , j} - \bar {r} _ {b}\right) \left(\bar {r} _ {j} - \bar {r}\right)}{\sqrt {\sum_ {j \in E _ {b}} \left(r _ {b , j} - \bar {r} _ {b}\right) ^ {2} \sqrt {\sum_ {j \in E _ {b}} \left(\bar {r} _ {j} - \bar {r}\right) ^ {2}}},}\tag{2}
$$

where $\overline { { r } } _ { j }$ refers to the average of the ratings on $\mathrm { i t e m } j \in E _ { b } ,$ , and r is the average of the ratings on all items.

• Competence, $C o ( a , b , c )$ . The competence of the trustee b is described from the viewpoint of the trustor a under a speci<sup>fi</sup>c context c. Two factors are taken into account, i.e., the number of user b's experience under context c (see Eq. (4)), and the ratio of correct recommendations given by user b to all the other users in the system (see Eq. (3)), employing the basic idea of O'Donovan and Smyth [24]. The competence is computed by integrating both factors:

$$
C o (a, b, c) = \gamma \frac {\sum_ {j \in E _ {b}} c o u n t _ {u \in U _ {j}} \left(| r _ {b , j} - r _ {u , j} | <   \varepsilon\right)}{\sum_ {j \in E _ {b}} \left\| U _ {j} \right\| ,}\tag{3}
$$

where $U _ { j }$ represents the set of users who have a piece of experience about item j, and ε is a prede<sup>fi</sup>ned error tolerance threshold below which a rating $r _ { b , j }$ of the trustee b is treated as a correct recommendation for item j relative to the other's real preference $r _ { u , j } .$ And γ is de<sup>fi</sup>ned by:

$$
\gamma = \left\{ \begin{array}{c l} \frac {N _ {b , c}}{N _ {c} ^ {a}} & \text { if } N _ {b, c} \leq N _ {c} ^ {a}; \\ 1 & \text { otherwise }; \end{array} \right.\tag{4}
$$

where $N _ { b , c }$ is the number of experience under context c out of the total m experience that user b has, and N<sup>a</sup> is the minimal number of experience under context c required by the trustor a such that a user can be regarded as a reliable recommender.

• Predictability, $P r ( a , b )$ . Different from integrity, the predictability of trustee b is de<sup>fi</sup>ned as the degree to which the (positive, neutral or negative) trend of b's rating behaviors is distinct from that of trustor a. Formally, it is computed by:

$$
\begin{array}{l} n _ {u} = \underset {j \in E _ {a, b}} {\text { count }} \Big (| r _ {a, j} - r _ {b, j} | \leq \theta \Big); \\ n _ {n} = \underset {j \in E _ {a, b}} {\text { count }} \Big (r _ {a, j} - r _ {b, j} > \theta \Big); \\ n _ {p} = \underset {j \in E _ {a, b}} {\text { count }} \Big (r _ {a, j} - r _ {b, j} <   - \theta \Big); \\ P r (a, b) = \frac {\max \Big (n _ {u} , n _ {p} , n _ {n} \Big) - m i n \Big (n _ {u} , n _ {p} , n _ {n} \Big)}{\| E _ {a , b} \|}, \end{array}\tag{5}
$$

where $n _ { u } , n _ { n }$ and $n _ { p }$ refer to the neutral, negative and positive trends of user b's rating behaviors comparing to trustor a's behaviors, respectively; θ is a threshold prede<sup>fi</sup>ned by trustor a. The intuition is that for a user who is highly predictable, the difference in trends should be signi<sup>fi</sup>cant. In case of $n _ { u } = n _ { n } = n _ { p } ,$ , we obtain the lowest predictability since it is dif<sup>fi</sup>cult to predict the next behavior of the trustee.

• Impersonal aspects: due to the availability of (dis)trust links of each user, we speci<sup>fi</sup>cally identify four kinds of impersonal aspects in our computational model on the basis of the degree of a trustee in the trust network. The degree, as one of the centrality measurements, essentially records the aggregate public relations of the trustee in the network. The four aspects based on degree of trustee b are trust indegree $d _ { i n } ^ { + } ( b )$ , trust outdegree $d _ { o u t } ^ { + } ( b )$ , distrust indegree $d _ { i n } ^ { - } ( b )$ and distrust outdegree $d _ { o u t } ^ { - } ( b )$ , referring to trustee b's incoming trust links, outgoing trust links, incoming distrust links and outgoing distrust links respectively.

## 4.2. Trust prediction

For trust prediction, we de<sup>fi</sup>ne $t _ { a , b , c } \in [ 0 , 1 ]$ as the trust value that trustor a has towards trustee b under context c, where 0 means completely not trust and 1 completely trust. The trust value will be in<sup>fl</sup>uenced by the set of eight aspects that we investigated, denoted by $A ( a , b ) =$ {Be(a, b), Co(a, b, c), In(b), Pr(a, b), d<sup>+</sup>(b), d<sup>+</sup> (b), d<sup>−</sup>(b), d<sup>−</sup> (b)}. In practice, users may specify other users as trusted neighbors $( t = 1 ) , ^ { 2 }$ 2 whereas if trustor a has no direct trust link to trustee b, we consider that a has no trust towards $b ( t = 0 )$ . The trust and absence of trust connections will help build a useful model of the trust aspects and the overall trust. Speci<sup>fi</sup>cally, the expected probability<sup>3</sup> that trustor a completely trusts the trustee b under context c (denoted as $\mathfrak { p } ^ { + } ( a , b , c ) )$ can be written as:

$$
p ^ {+} (a, b, c) = E \left(t _ {a, b, c} = 1 | A (a, b)\right).\tag{6}
$$

We apply the logistic regression to classify trust from not trust, and obtain the importance weight of each aspect related with trust. To be speci<sup>fi</sup>c, the logit of the probability is modeled as a linear combination of $A ( a , b ) [ 1 5 ]$

$$
\operatorname{logit} \left(p ^ {+} (a, b, c)\right) = \log \left(\frac {p ^ {+} (a , b , c)}{1 - p ^ {+} (a , b , c)}\right) = \alpha_ {0} ^ {a +} + \left(\alpha_ {A} ^ {a +}\right) ^ {T} \cdot A (a, b),\tag{7}
$$

where $\alpha _ { A } ^ { a \stackrel { + } { - } } = \{ \alpha _ { 1 } ^ { a } { } ^ { + } , \alpha _ { 2 } ^ { a } { } ^ { + } , \alpha _ { 3 } ^ { a } { } ^ { + } , \alpha _ { 4 } ^ { a } { } ^ { + } , \alpha _ { 5 } ^ { a } { } ^ { + } , \alpha _ { 6 } ^ { a } { } ^ { + } , \alpha _ { 7 } ^ { a } { } ^ { + } , \alpha _ { 8 } ^ { a } { } ^ { + } \} ,$ , and $\alpha _ { 0 } ^ { a + }$ is interpreted as the intrinsic trust propensity of trustor a. Then the probability $p ^ { + } ( a , b , c )$ is derived by:

$$
p ^ {+} (a, b, c) = \frac {1}{1 + e ^ {- \left(\alpha_ {0} ^ {a +} + \left(\alpha_ {A} ^ {a +}\right) ^ {T} \cdot A (a , b)\right)}}.\tag{8}
$$

Based on the trust information directly speci<sup>fi</sup>ed by real users, we are able to train this model and learn the coef<sup>fi</sup>cients, i.e., the importance weight of each aspect related to trust. The weights $\alpha _ { A } ^ { a + }$ can be used to compute implicit or re<sup>fi</sup>ne explicit trust values from user experience.

## 4.3. Distrust Prediction

Accordingly, following the process of trust prediction, the expected probability that the trustor a completely distrusts the trustee b under context c (denoted as $p ^ { - } ( a , b , c ) )$ can be written as:

$$
p ^ {-} (a, b, c) = E \left(d _ {a, b, c} = 1 | A (a, b)\right),\tag{9}
$$

where $d _ { a , b , c } = 1$ represents that a completely distrusts b under context c. We also apply the logistic regression to classify distrust from not distrust, and obtain the importance weight of each aspect related with distrust:

$$
\operatorname{logit} \left(p ^ {-} (a, b, c)\right) = \log \left(\frac {p ^ {-} (a , b , c)}{1 - p ^ {-} (a , b , c)}\right) = \alpha_ {0} ^ {a -} + \left(\alpha_ {A} ^ {a -}\right) ^ {T} \cdot A (a, b),\tag{10}
$$

where $\alpha _ { A } ^ { a } - = \{ \alpha _ { 1 } ^ { a } - , \alpha _ { 2 } ^ { a } - , \alpha _ { 3 } ^ { a } - , \alpha _ { 4 } ^ { a } - , \alpha _ { 5 } ^ { a } - , \alpha _ { 6 } ^ { a } - , \alpha _ { 7 } ^ { a } - , \alpha _ { 8 } ^ { a } - \} ,$ and α<sup>a</sup> <sup>−</sup> is interpreted as the intrinsic distrust propensity of the trustor a. Then the probability $p ^ { - } ( a , b , c )$ is derived by:

$$
p ^ {-} (a, b, c) = \frac {1}{1 + e ^ {- \left(\alpha_ {0} ^ {a -} + \left(\alpha_ {A} ^ {a -}\right) ^ {T} \cdot A (a , b)\right)}}.\tag{11}
$$

Based on the distrust information directly speci<sup>fi</sup>ed by real users, we are able to train this model and learn the importance weight of each aspect related to distrust. The weights can be used to compute implicit or re<sup>fi</sup>ne explicit distrust values from user experience.

## 4.4. Trust link refinement

Given the predicted probability of complete trust $p ^ { + } ( a , b , c )$ and distrust $p ^ { - } ( a , b , c )$ according to Eqs. (8) and (11), we can further re<sup>fi</sup>ne the trust link by <sup>fi</sup>ltering out the possibly inaccurate trust or distrust link using the following rules:

$$
\begin{array}{l} \text { if } p ^ {+} (a, b, c) > p ^ {-} (a, b, c), \text { trust   link   from } a \text { to } b; \\ \text { if } p ^ {+} (a, b, c) <   p ^ {-} (a, b, c), \text { distrust   link   from } a \text { to } b; \\ \text { if } p ^ {+} (a, b, c) = p ^ {-} (a, b, c), \text { no   link   from } a \text { to } b. \end{array}\tag{12}
$$

Furthermore, we could also re<sup>fi</sup>ne the trust degree using Eq. (13) for other speci<sup>fi</sup>c purposes such as comparing the trust degrees between different user pairs.

$$
t (a, b, c) = \left\{ \begin{array}{l l} p ^ {+} (a, b, c) - p ^ {-} (a, b, c) & \text { if } p ^ {+} (a, b, c) > p ^ {-} (a, b, c) \\ 0 & \text { otherwise. } \end{array} \right.\tag{13}
$$

## 5. Evaluation

For evaluation, we aim to explore the effectiveness of our proposed (dis)trust framework by incorporating the generated trust information into three representative trust-aware recommender systems.

## 5.1. Data sets

Three real-world data sets are used in the experiments, namely Epinions, FilmTrust and Flixster. Epinions enables users to review products by adding text comments and issuing numerical ratings in the range of [1,5]. Besides, users can also explicitly specify other users as trust (to the trust list) or distrust (to the block list) based on whether the reviews and ratings of others are consistently valuable or useless for the user. We adopt the extended Epinions data set<sup>4</sup> where trust value is labeled as 1 and distrust as −1. We sample two subsets by randomly selecting 5000 and 10,000 users, respectively. The other two data sets are FilmTrust (provided by Guo et al. [6]) and Flixster<sup>5</sup> where only trust exists and no distrust information is available. Users can only indicate others as trust, and provide item ratings scaled from 0.5 to 4.0 (5.0 in Flixster) with step 0.5. The statistics of the four data sets is presented in Table 1.

## 5.2. Experimental settings

Since the two Epinions subsets are the only available collections that contain both trust and distrust information, we use them to train two logistic regression models for trust and distrust respectively. Speci<sup>fi</sup>cally, the users who specify both trust and distrust statements to others are selected as the training data in order to learn the coef<sup>fi</sup>cients (i.e., the importance weights) of each trust and distrust aspect according to Eqs. (7) and (10), respectively. Due to the limitation of data, we do not take into account the context information in the experiments. Besides, we empirically set ε = 0.1 for competence (see Eq. (3)) and $\theta = 0 . 1$ for predictability (see Eq. (5)) computations. Although the other data sets FilmTrust and Flixster do not contain distrust information (and hence cannot train a regression model independently), they may be useful in testing the effectiveness of these aspects by adopting the models learned from the Epinions data sets. The intuition is that although the exact or absolute coef<sup>fi</sup>cient values may vary in different data sets, the relative importance weights may follow the same trends for key factors. In other words, as the coef<sup>fi</sup>cients learned from one data set A re<sup>fl</sup>ect the importance weights of the corresponding (dis)trust aspects related to (dis)trust, they capture the dependent relationships between these (dis)trust aspects with (dis)trust for the users in the data set sample A. In this case, if we assume that users in another data set B are sampled from the same user population as those in the data set A, the coef<sup>fi</sup>cients for these users in the data set B might have similar values as those in data set A. Under this assumption, to be speci<sup>fi</sup>c, we apply the coef<sup>fi</sup>cients learned from Epinions1 to FilmTrust, and those learned from Epinions2 to Flixster according to the comparative sizes of the corresponding data sets.

The statistics of four data sets.

<table><tr><td>Features</td><td>Epinions1</td><td>Epinions2</td><td>FilmTrust</td><td>Flixster</td></tr><tr><td>Users</td><td>5000</td><td>10,000</td><td>1508</td><td>5000</td></tr><tr><td>Items</td><td>376,458</td><td>519,491</td><td>2071</td><td>13,527</td></tr><tr><td>Trust</td><td>744</td><td>3443</td><td>2853</td><td>2898</td></tr><tr><td>Distrust</td><td>424</td><td>1398</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Ratings</td><td>968,467</td><td>2,017,158</td><td>70,998</td><td>264,540</td></tr><tr><td>Avg rating</td><td>4.6964</td><td>4.6863</td><td>3.0028</td><td>3.6560</td></tr></table>

After obtaining the aspect coef<sup>fi</sup>cients, we regenerate or predict the trust values in the light of different combinations of the two types of trust and distrust aspects, and in total we obtain 3 such different combinations and the corresponding trust values. Hence, the effectiveness of the new trust information (re<sup>fi</sup>ned by the predicted distrust information) can be investigated by the recommendation performance in comparison with the original ones. Speci<sup>fi</sup>cally, to demonstrate the effectiveness, we adopt three representative trust-aware algorithms to generate recommendations:

• TidalTrust, proposed by Golbeck [4], uses trust values to substitute user similarity to weigh user ratings when generating recommendations.

• Merge, proposed by Guo et al. [5], incorporates the ratings of trusted neighbors to form a more complete rating pro<sup>fi</sup>le for active users, where the trust propagation length is 1.

• SocialMF, proposed by Jamali and Ester [9], considers the trust information and propagation of trust information into the matrix factorization model for recommender systems. In our experiments, we adopt the same settings of parameters as suggested in [9], and source code provided by MyMediaLite recommender system library.<sup>6</sup>

To have a better understanding of the effectiveness, we split each data set into three different views in terms of item-related properties as used in [5,18]:

• All represents the whole data set.

• Controversial Items are those items which received ratings with standard deviation greater than 1.5.

• Niche Items are those items which received less than 5 ratings.

The experiments are conducted by applying the leave-one-out technique, that is, each rating is iteratively hidden whose value will be predicted by applying the TidalTrust, Merge, or SocialMF method until all ratings in the data sets are tested. The performance is evaluated by two commonly used measures: the root mean square errors (RMSE) and mean absolute errors (MAE). They both refer to the differences between the predictions and the ground truth, but differ from each other as indicated by their names. Generally, smaller RMSE and MAE values indicate better predictive accuracy.

Table 2  
The coef<sup>fi</sup>cients of trust aspects.

<table><tr><td>Data set</td><td colspan="2">Epinions1</td><td colspan="2">Epinions2</td></tr><tr><td>Aspect</td><td>Trust</td><td>Distrust</td><td>Trust</td><td>Distrust</td></tr><tr><td>Benevolence</td><td>0.772</td><td>-1.2295</td><td>0.6332</td><td>-1.4537</td></tr><tr><td>Competence</td><td>2.3706</td><td>0.988</td><td>2.5458</td><td>1.6816</td></tr><tr><td>Integrity</td><td>-0.5816</td><td>-0.1122</td><td>-0.6597</td><td>-0.461</td></tr><tr><td>Predictability</td><td>-0.0471</td><td>0.313</td><td>-0.3666</td><td>0.5724</td></tr><tr><td>Trust indegree</td><td>-0.055</td><td>0.0159</td><td>-0.0387</td><td>-0.0006</td></tr><tr><td>Trust outdegree</td><td>0.0615</td><td>-0.0042</td><td>0.0677</td><td>0.011</td></tr><tr><td>Distrust indegree</td><td>-0.0765</td><td>-0.3697</td><td>0.0016</td><td>-0.2533</td></tr><tr><td>Distrust outdegree</td><td>-0.0125</td><td>0.2347</td><td>-0.0066</td><td>0.144</td></tr></table>

## 6. Results and analysis

The experimental results are presented in two-fold: (1) the importance weights of the trust and distrust aspects learned from logistic regression models; and (2) the effectiveness of the trust and distrust aspects applied in recommender systems in comparison with that of the original trust values.

## 6.1. Importance of trust and distrust aspects

We use the L2-regularized logistic regression provided by LIBLINEAR<sup>7</sup> to train the data of Epinions1 and Epinions2. The coef<sup>fi</sup>cients (i.e., the importance weights) of the trust and distrust aspects are illustrated in Table 2. Note that since the implementation of LIBLINEAR tends to minimize the bias part (to 0) during the model <sup>fi</sup>tting process, we do not present the results of the aspect about trustor's propensity. In fact, its value is often equal to or very close to 0. Besides, since the logistic regression has a strict requirement on the sample size, we adopt a well-known rule of thumb, i.e., the 1 in 10 rule [7] to specify a minimum size of the sample for a reliable training. In particular, a minimum number 10 of trust (or distrust) links are required for each aspect, that is, at least 80 trust (or distrust) examples are required in order to obtain a reliable model. However, we <sup>fi</sup>nd that only few users in the training sets could meet the requirement. Therefore, we turn out to train the logistic regression models based on the trust and distrust networks of all the users and adopt the learned coef<sup>fi</sup>cients for all the users. An alternative way is to divide users into different clusters according to user similarity and then the coef<sup>fi</sup>cients could be learned using all the users' experience within the same cluster. This may lead to more accurate coef<sup>fi</sup>cients for similar users. Although we do not conduct our experiments in this way in the current work, we demonstrate that our method based on the logistic regression models learned from all users (i.e. general knowledge) could already signi<sup>fi</sup>cantly improve the recommendation accuracy.

Table 2 shows that consistent results for the four interpersonal aspects<sup>8</sup> with trust and distrust are obtained in both Epinions1 and Epinions2 data sets. In general, benevolence and competence are both positively correlated with trust whereas integrity and predictability are negatively correlated. In other words, the <sup>fi</sup>rst two aspects are more likely to increase the probability of trust, but the latter two decrease the probability. More speci<sup>fi</sup>cally, competence shows the greatest correlation with trust, followed by benevolence. This may imply that users in recommender systems are more concerned with personal experience (e.g. benevolence) rather than collective opinions (e.g. integrity) when establishing trust. Further, a person whose behaviors are highly predictable does not guarantee high trustworthiness in trust building because the predictability is value-neutral. In contrast, competence and predictability present positive correlation with distrust whereas benevolence and integrity are negatively correlated with distrust. It should also be noted that the result for each individual impersonal aspect is not very consistent across the two data sets. This might be due to the fact that we only capture partial trust and distrust information for users in our data sets, as we only consider the trust and distrust information of each user to our sampled users. Overall, however, the coef<sup>fi</sup>cients for impersonal aspects could still be considered as consistent in the sense that the aggregated effect of the trust network related impersonal aspects (trust indegree and outdegree) is positive, while that of the distrust network related impersonal aspects is negative, for both trust and distrust. This could be partially explained as that a trustee with more trusted and trusting neighbors could have more far-reaching in<sup>fl</sup>uence on other users, and thus are intended to be either more trusted or distrusted by others. In other words, a trustworthy user would be considered as more trustworthy by trustors, and further trusted by more people, and vice versa.

![](/api/attachments/QNVGDQNG/fulltext/images/6444d7cf7f5352e13573d9fecc313b2bcb41d174bf001b59f162da60baf2b342.jpg)  
Fig. 2. The comparison of re<sup>fi</sup>ned trust links with the original ones.

## 6.2. Effectiveness of the proposed model

We predict the trust values based on the learned regression models for three scenarios: “All”, “Interpersonal” and “Impersonal”. “All” refers to considering both interpersonal and impersonal aspects, while the others refer to only considering interpersonal or impersonal aspects respectively. The effectiveness of these aspects in predicting trust values would be investigated by applying the aforementioned three algorithms (i.e. TidalTrust, Merge1 and SocialMF) in terms of predictive accuracy for recommender systems. Besides, three different views<sup>9</sup> mentioned in Section 5.1 of data sets are studied. Lastly, we further employ the learned regression models from Epinions1 and Epinions2 to FilmTrust and Flixster where distrust information is unavailable.

Before evaluating our performance, we <sup>fi</sup>rst present the ratio of “reliable” trust links to the original ones according to Eq. (12) based on our model. As illustrated in Fig. 2, a substantial ratio of the original trust links are <sup>fi</sup>ltered out as “unreliable” ones by our model. The results in Tables 3 and 4 of our method are based on these “reliable” trust links. Later we will show whether this difference would lead to the performance improvement of the three recommendation algorithms.

In the view of All, Tables 3 and 4 show that our model could almost achieve the best performance with regard to RMSE and MAE for all three algorithms on the three data sets. Our method could achieve similar results with the original trust values on Epinions and Flixster, but demonstrate signi<sup>fi</sup>cant differences on FilmTrust (the t-test veri<sup>fi</sup>es its statistical signi<sup>fi</sup>cance at the 5% level, i.e. p-value = 0.0415 b 0.05). This may be explained by the fact that most ratings on Epinions and Flixster data sets are highly skewed. Speci<sup>fi</sup>cally, the average ratings are 4.6964, 4.6863 (out of 5) and 3.6560 (out of 4) in Epinions1, Epinions2 and Flixster, respectively (see Table 1). In contrast, the average rating in FilmTrust is 3.0028 out of 4. The same trends could be observed in the view of Controversial Items due to less skewed distributed ratings, where our approach obtains much better performance than that with original trust value. It should be noted that in the views of Niche Items, the performance of our method is worse than that with the original trust. This is mainly because Niche Items are de<sup>fi</sup>ned as those which received less than 5 ratings. In that case, the problem of data sparsity becomes more serious as we <sup>fi</sup>lter out some recommenders who might provide ratings to Niche Items. This problem could be addressed by predicting more implicit trust links with our model. The improvements on the three methods over those with the original trust are remarkable (around 0.13 in RMSE and 0.18 in MAE at most), as Koren [11] points out that small improvements in RMSE may lead to signi<sup>fi</sup>cant improvements in real applications.

The comparison of performance based on re<sup>fi</sup>ned trust using Epinions1.

<table><tr><td rowspan="2">Methods</td><td rowspan="2">Aspects</td><td colspan="2">All</td><td colspan="2">Controversial Items2777 users7242 ratings</td><td colspan="2">Niche Items4705 users539,881 ratings</td><td colspan="2">FilmTrust-All</td></tr><tr><td>RMSE</td><td>MAE</td><td>RMSE</td><td>MAE</td><td>RMSE</td><td>MAE</td><td>RMSE</td><td>MAE</td></tr><tr><td rowspan="4">TidalTrust</td><td>Original</td><td>0.6759</td><td>0.5756</td><td>1.7259</td><td>1.6045</td><td>0.7287</td><td>0.6368</td><td>0.9687</td><td>0.7564</td></tr><tr><td>All</td><td>0.7432</td><td>0.6255</td><td>1.5910</td><td>1.4226</td><td>0.7653</td><td>0.6713</td><td>0.8355</td><td>0.6465</td></tr><tr><td>Interpersonal</td><td>0.6833</td><td>0.5675</td><td>1.6996</td><td>1.5169</td><td>0.7674</td><td>0.6548</td><td>0.7929</td><td>0.6177</td></tr><tr><td>Impersonal</td><td>0.7624</td><td>0.6469</td><td>1.5873</td><td>1.4574</td><td>0.7710</td><td>0.6787</td><td>0.9390</td><td>0.7315</td></tr><tr><td rowspan="4">Merge</td><td>Original</td><td>0.7441</td><td>0.5920</td><td>1.5490</td><td>1.3336</td><td>0.7601</td><td>0.6103</td><td>0.8788</td><td>0.6919</td></tr><tr><td>All</td><td>0.7608</td><td>0.6140</td><td>1.5295</td><td>1.3490</td><td>0.7752</td><td>0.6324</td><td>0.8751</td><td>0.6892</td></tr><tr><td>Interpersonal</td><td>0.7234</td><td>0.5734</td><td>1.5224</td><td>1.3270</td><td>0.7791</td><td>0.6384</td><td>0.8748</td><td>0.6890</td></tr><tr><td>Impersonal</td><td>0.7890</td><td>0.6336</td><td>1.4930</td><td>1.3172</td><td>0.7811</td><td>0.6396</td><td>0.8766</td><td>0.6904</td></tr><tr><td rowspan="4">SocialMF</td><td>Original</td><td>1.4075</td><td>1.2177</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.0608</td><td>0.7760</td></tr><tr><td>All</td><td>1.3910</td><td>1.1820</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.9950</td><td>0.7310</td></tr><tr><td>Interpersonal</td><td>1.4455</td><td>1.2414</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.0639</td><td>0.7684</td></tr><tr><td>Impersonal</td><td>1.6103</td><td>1.3370</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.081</td><td>0.7917</td></tr></table>

## 6.2.1. Interpersonal and impersonal aspects

Fig. 3 presents the performance of TidalTrust algorithm by considering only interpersonal or impersonal aspects. As demonstrated in Fig. 3, we can see that the trust derived from interpersonal aspects (i.e. on rating history) is more effective than that from impersonal factors (i.e. on trust and distrust network) in terms of RMSE. However, for Controversial Items, the algorithms depending on trust values derived from impersonal aspects perform saliently better than those from interpersonal aspects. This is due to the fact that users' ratings of Controversial Items are quite dissimilar, increasing the dif<sup>fi</sup>culty on extracting valuable information for personalized recommendation according to rating history. On the contrary, the impersonal aspects, modeled based on the trust and distrust networks, would not be affected by those controversial ratings. Hence, they might infer more reliable trust and distrust values. Besides, we also explore the effectiveness of each interpersonal aspect as well as their combinations without considering the impersonal aspects. The results are presented in Table 5 and Figs. 4 and 5, where B, C, I and P denote benevolence, competence, integrity and predictability, respectively. Hence all the combinations of trust aspects can be represented by concatenating letters. For example, B–C refers to the combination of the benevolence and competence. As can be seen in Table 5,<sup>10</sup> overall, the performance increases as more aspects are involved in. We thus could conclude that all the four interpersonal aspects are reasonable and each of them contributes to the success of our trust and distrust prediction.

A clearer and more detailed demonstration is illustrated in Figs. 4 and 5 which present the comparison of different interpersonal aspects in terms of performance gaps in different views of data sets. The histogram under the horizontal solid line (representing the original trust performance) means a better performance than the baseline in terms of RMSE. More speci<sup>fi</sup>cally, for single aspect, benevolence achieves the best performance than the other three aspects. In contrast, in the view of Controversial or Niche Items (see Fig. 5), competence obtains the worse performance than predictability or integrity whose performance is equivalent to that of original trust values. Besides, in the view of All (see Fig. 4), the performance gap between competence and integrity or predictability is not so signi<sup>fi</sup>cant since all the RMSE gaps are smaller than 0.005. Hence, although competence is an important aspect for trust modeling (see Table 2), it is not that useful in recommender systems as a single aspect. Furthermore, the performance of B − P is better than that of B (the best of single aspect) and that of $B - I - P \ o { \mathrm { o r } } B - C - P$ (the best of the combinations of three aspects). This implies that predictability, modeled in a different way and providing additional information, can complement benevolence in building the trust relationship in recommender systems. However, integrating with other aspects (e.g., competence or integrity) may not result in better performance. For the best combination B − P, benevolence is closely related to individuals' similarity, and predictability, on the contrary, provides indications of the consistency of the similarity trend. In this sense, the two aspects are complementary to each other, and capable of generating better trust values for recommender systems. However, when other aspects are incorporated, redundant and even noisy information could be brought in, and thus deteriorates the performance.

## 6.2.2. Generalization

It is observed that similar trends of performance are obtained on FilmTrust and Flixster using the coef<sup>fi</sup>cients learned from Epinions1 and Epinions2, respectively. As illustrated in Tables 3 and 4, TidalTrust, Merge and SocialMF could achieve better performance with the trust information learned by using the trained logistic regression models (for trust and distrust) on Epinions. Moreover, as shown in Fig. 6(a) and (b), benevolence consistently shows better performance than other single aspects, and the combination of benevolence and predictability reaches the best performance among the overall 15 combinations of impersonal aspects. Hence, we conclude that the trust model learned from one data set can be applied to other data sets where distrust information is unavailable. It is important because most real-world data sets do not contain such information due to various reasons such as privacy concern. In other words, the knowledge learned from one community can be (partially) reused to model the trust and distrust in other communities.

Table 4  
The comparison of performance based on different trust aspects using Epinions2.

<table><tr><td rowspan="2">Methods</td><td rowspan="2">Aspects</td><td colspan="2">All</td><td colspan="2">Controversial Items2653 users12,775 ratings</td><td colspan="2">Niche Items8922 users731,116 ratings</td><td colspan="2">Flixster-All</td></tr><tr><td>RMSE</td><td>MAE</td><td>RMSE</td><td>MAE</td><td>RMSE</td><td>MAE</td><td>RMSE</td><td>MAE</td></tr><tr><td rowspan="4">TidalTrust</td><td>Original</td><td>0.6420</td><td>0.5287</td><td>1.6467</td><td>1.5444</td><td>0.7346</td><td>0.6399</td><td>1.2449</td><td>0.9846</td></tr><tr><td>All</td><td>0.7123</td><td>0.5857</td><td>1.7390</td><td>1.5215</td><td>0.7867</td><td>0.6764</td><td>1.2129</td><td>0.9706</td></tr><tr><td>Interpersonal</td><td>0.6255</td><td>0.5132</td><td>1.6607</td><td>1.4679</td><td>0.7814</td><td>0.6627</td><td>1.2190</td><td>0.9789</td></tr><tr><td>Impersonal</td><td>0.7194</td><td>0.5951</td><td>1.6055</td><td>1.4950</td><td>0.7766</td><td>0.6746</td><td>1.2449</td><td>0.9846</td></tr><tr><td rowspan="4">Merge</td><td>Original</td><td>0.6801</td><td>0.5540</td><td>1.4869</td><td>1.3235</td><td>0.7298</td><td>0.5934</td><td>1.0376</td><td>0.8163</td></tr><tr><td>All</td><td>0.7032</td><td>0.5880</td><td>1.5467</td><td>1.3754</td><td>0.7432</td><td>0.6128</td><td>1.0362</td><td>0.8150</td></tr><tr><td>Interpersonal</td><td>0.6734</td><td>0.5541</td><td>1.4868</td><td>1.2830</td><td>0.7503</td><td>0.6211</td><td>1.0366</td><td>0.8155</td></tr><tr><td>Impersonal</td><td>0.7341</td><td>0.6043</td><td>1.4669</td><td>1.3235</td><td>0.7501</td><td>0.6143</td><td>1.0376</td><td>0.8163</td></tr><tr><td rowspan="4">SocialMF</td><td>Original</td><td>1.2799</td><td>1.1094</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.3747</td><td>1.0440</td></tr><tr><td>All</td><td>1.2559</td><td>1.0971</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.3716</td><td>1.0450</td></tr><tr><td>Interpersonal</td><td>1.2603</td><td>1.0999</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.3838</td><td>1.0506</td></tr><tr><td>Impersonal</td><td>1.4474</td><td>1.2079</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.3747</td><td>1.0440</td></tr></table>

## 6.2.3. The size of the predicted trust network

Fig. 7 shows the performance of the three algorithms on FilmTrust data set by varying the size of the predicted trust network. Here, the X-axis refers to that the predicted trust network is certain times as large as the original network. As demonstrated in the <sup>fi</sup>gure, we can see that all three algorithms obtain better recommendation accuracy as the size of the trust network increases up to a certain point, verifying the effectiveness of our model in predicting implicit trust and distrust values (or relationships). Note that both Merge and SocialMF incorporate the mechanism of trust propagation to improve the recommendation accuracy. Therefore, the corresponding performance of incorporating our model could be further improved if the propagation length is made bigger than 1 (especially for the Merge method [5]).

## 6.2.4. Predicted distrust information

In our model, we employ the predicted distrust value to re<sup>fi</sup>ne the trust value according to Eqs. (12) and (13). Fig. 8 pictures the performance comparison of the TidalTrust algorithm on three data sets by differentiating between considering and not considering the predicted distrust information. As illustrated, by considering all aspects, i.e. both interpersonal and impersonal ones, we can see that the performance of TidalTrust has been saliently improved if incorporating predicted implicit distrust information into trust value prediction. This demonstrates that the noisy (less reliable) trust links could be validly removed by our model.

## 7. Conclusion and future work

This paper explored the multiple facets of trust and distrust predictions for recommender systems. Speci<sup>fi</sup>cally, we identi<sup>fi</sup>ed both the interpersonal and impersonal aspects according to the trust theory from social science. The four interpersonal aspects, namely benevolence, competence, integrity and predictability, were formally de<sup>fi</sup>ned in the trust theory based on which they were computationally modeled in the light of user experience (i.e. ratings) in the systems, while the impersonal aspects are computed on the basis of users' trust and distrust network. Then the importance of each aspect to trust or distrust was learned by applying a corresponding logistic regression model trained by real-world data sets that contained trust or distrust information.

![](/api/attachments/QNVGDQNG/fulltext/images/3a32c726d83373c895645b713ca2564ee03ac355aa18a5fe2c5c4f30d44b0443.jpg)  
Fig. 3. Performance comparison of TidalTrust method by considering interpersonal and impersonal aspects.

After learning the two logistic regression models, we predicted the (implicit) trust and distrust values, where the trust values were further re<sup>fi</sup>ned by the distrust values. These newly generated trust values were taken as input to three representative trust-based recommendation algorithms (i.e. TidalTrust, Merge and SocialMF) in order to validate the effectiveness of our proposed model. The experimental results showed that: (1) benevolence and competence were positively correlated with trust whereas the integrity and predictability were negatively correlated. On the other hand, competence and predictability were positively correlated with distrust whereas the benevolence and integrity were

Table 5  
The performance comparison of Tidaltrust based on interpersonal aspects on Flixster.

<table><tr><td># Aspects</td><td>RMSE</td><td>Improvement</td><td>MAE</td><td>Improvement</td></tr><tr><td>1</td><td> $1.2415 \pm 0.0031$ </td><td>-</td><td> $0.9828 \pm 0.0036$ </td><td>-</td></tr><tr><td>2</td><td> $1.2383 \pm 0.0055$ </td><td>0.26%</td><td> $0.9805 \pm 0.0043$ </td><td>0.23%</td></tr><tr><td>3</td><td> $1.2352 \pm 0.0028$ </td><td>0.25%</td><td> $0.9783 \pm 0.0034$ </td><td>0.22%</td></tr><tr><td>4</td><td>1.2129</td><td>1.81%</td><td>0.9706</td><td>0.78%</td></tr></table>

![](/api/attachments/QNVGDQNG/fulltext/images/6ad8f496fa323d39cc183f4245d221c3a20ede7d91f30ffab186dbb7b6d81b42.jpg)  
Fig. 4. Performance comparison of TidalTrust method in All View on Epinions1.

![](/api/attachments/QNVGDQNG/fulltext/images/e1852fcb0c241f9c8c62b7d6da131647d67dd0cbbaf81dafd37dad0ed41499c3.jpg)  
(a) Controversial items

![](/api/attachments/QNVGDQNG/fulltext/images/9696f5cd370e017cd4a5dc0e63091a8c962aed8e8e72cebafac78b0f5a4d7f02.jpg)  
(b) Niche items

Fig. 5. The performance comparison of TidalTrust method in different views on Epinions1.  
![](/api/attachments/QNVGDQNG/fulltext/images/987e2d811633ec2ffd4eab3b8dbda13be37feb0bf51f2933a3d95cbed4ec911a.jpg)  
(a) Film Trust

![](/api/attachments/QNVGDQNG/fulltext/images/b65f7d329be62ec58fc2fbfdbb9f6d9be7ef68fbb8fe854096ab09991b55b878.jpg)  
(b) Flixster  
Fig. 6. (a) Performance comparison of TidalTrust method in All view.

negatively correlated. All the four interpersonal aspects were useful for the existing trust-based recommendation algorithms in that each individual aspect can achieve comparable performance derived from the original trust values. The combination of benevolence and predictability can achieve the best performance among all the 15 combinations made by the four aspects; (2) the learned trust models can be applied to other communities where distrust information is not available for evaluating both the trust and distrust relationships. Our results could serve as a guidance to effectively build implicit trust or distrust networks (competitive to robust explicit networks) based on our proposed framework when users had no explicit trust or distrust information. Incorporating distrust information could effectively remove noisy and redundant data in the original explicit trust network. Therefore, when encountering a data set A without distrust information, an alternative way is to learn the coef<sup>fi</sup>cients from sampled Epinions data set which has comparable size with the data set A; (3) incorporating impersonal aspects can further improve the performance of the existing trust-based recommendation algorithms. In addition, the interpersonal aspects would take greater effect when there were lots of rating data of users, whereas the impersonal aspects would contribute more to the Controversial Items; and (4) our ability of predicting the implicit trust values could complement the trust network, which could further improve the performance of trust-aware recommender systems. In other words, if we want to improve the performance of a speci<sup>fi</sup>c trust-aware recommender system, we can predict more possible trust links using our approach to increase the size of the existing trust network.

![](/api/attachments/QNVGDQNG/fulltext/images/2f7d4edd75e31fb3447fef60229d14f3eb44167ac8d87d50659a4d8ce1a960cc.jpg)  
(a) TidalTrust

![](/api/attachments/QNVGDQNG/fulltext/images/37a8087a1e0f028a55ea9adc9229b93512b115c55ba376882ff50a955adee3c8.jpg)  
(b) Merge

![](/api/attachments/QNVGDQNG/fulltext/images/f21452cc8c5838de2f31676f4d0364f131d505770938ec59785428dea595a6c5.jpg)  
(c) SocialMF  
Fig. 7. The performance by varying the size of predicted trust network on FilmTrust.

![](/api/attachments/QNVGDQNG/fulltext/images/43800ef676abe77f97fa14be61da36bc64bfa402ce51d8ea130b9df597c069ac.jpg)  
(a) Epinions-Controversial Items

![](/api/attachments/QNVGDQNG/fulltext/images/8fbef8959436c9e6a39c5a5a50ee2cb242a553dbd675e2e7875c5ce9a70e5312.jpg)  
(b) FilmTrust

![](/api/attachments/QNVGDQNG/fulltext/images/b903bb41dc3df8bba37d91bf2958c3c17465d5bdd2acc9ddd4a9447211ece512.jpg)  
(c) Flixster  
Fig. 8. The performance comparison of TidalTrust between “without” and “with” distrust.

The contributions of our current work can be mainly summarized by the following two aspects: (1) our study serves as the initial step aiming to <sup>fi</sup>ll in the gap between trust and distrust as multi-aspect concepts and the relatively simple usage of trust and (especially) distrust in recommender systems. The newly predicted trust and distrust values can effectively enhance the performance of the existing trust-aware recommender systems. Given the relatively large base of this kind of recommender systems, the in<sup>fl</sup>uence is considerably signi<sup>fi</sup>cant for the area of recommender systems. With the increased accuracy of recommendation, users will be able to achieve more informed decision making; and (2) we introduce the formal de<sup>fi</sup>nitions of the interpersonal and impersonal aspects of trust and distrust from which they will be computationally modeled according to users' historic ratings and trust networks. It can inspire and lead the research in the computational trust area to build more robust and practical trust models, which well support users' decisions on which others to trust.

The future work is discussed as follows: (1) in the current work, we assume the trust aspects are independent with each other, and linearly correlated with trust. In the future, we might employ more complex machine learning techniques to capture the possible dependency among trust aspects for more powerful (dis)trust prediction algorithm; (2) the present work focuses on predicting (implicit) trust and distrust values according to our proposed trust framework for recommender systems by comparing the performance using re<sup>fi</sup>ned trust values (or links) relative to the original ones. In the future, we will further verify our research framework by exploring other candidate impersonal aspects such as reputation and closeness centrality of trustees.; (3) this study formalizes distrust as the mirror image of the trust concept. In the future, we could consider another interesting case in which trust and distrust are not predicted by the same aspects/ antecedents, but by different ones; and (4) we plan to design a trustaware recommender system by relatively equally considering both the predicted trust and distrust values instead of using the predicted distrust values to re<sup>fi</sup>ne trust values.

## References

[1] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions, IEEE Transactions on Knowledge and Data Engineering 17 (6) (2005) 734–749.

[2] C. Castelfranchi, R. Falcone, Socio-Cognitive Theory of Trust, in: J. Pitt (Ed.), Wiley, London, 2005.

[3] M. Chowdhury, A. Thomo, B. Wadge, Trust-based in<sup>fi</sup>nitesimals for enhanced collaborative <sup>fi</sup>ltering, Proceedings of the 15th International Conference on Management of Data (COMAD), 2009

[4] I. Golbeck, Generating predictive movie recommendations from trust in social networks Trust Management 2006 pp. 93–104

[5] G. Guo, J. Zhang, D. Thalmann, A simple but effective method to incorporate trusted neighbors in recommender systems, Proceeding of the 20th Conference on User Modeling, Adaptation, and Personalization (UMAP), 2012, pp. 114–125.

[6] G. Guo, J. Zhang, N. Yorke-Smith, A novel Bayesian similarity measure for recommender systems, Proceedings of the 23rd International Joint Conference on Arti<sup>fi</sup>cia Intelligence (IJCAI), 2013.

[7] F.E. Harrell, K.L. Lee, R.M. Califf, D.B. Pryor, R.A. Rosati, Regression modelling strategies for improved prognostic prediction, Statistics in Medicine 3 (2) (1984) 143–152.

[8] M. Jamali, M. Ester, Trustwalker: a random walk model for combining trust-based and item-based recommendation, Proceedings of the 15th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2009, pp. 397–406.

[9] M. Jamali, M. Ester, A matrix factorization technique with trust propagation for recommendation in social networks, Proceedings of the fourth ACM Conference on Recommender Systems, ACM, 2010, pp. 135–142.

[10] A. Jøsang, W. Quattrociocchi, D. Karabeg, Taste and trust, Trust Management, V, Springer, 2011, pp. 312–322

[11] Y. Koren, Factor in the neighbors: scalable and accurate collaborative <sup>fi</sup>ltering, ACM Transactions on Knowledge Discovery from Data (TKDD) 4 (1) (2010) 1–24.

[12] K. Kwon, J. Cho, Y. Park, Multidimensional credibility model for neighbor selection in collaborative recommendation, Expert Systems with Applications 36 (3) (2009) 7114–7122.

[13] J. Leskovec, D. Huttenlocher, J. Kleinberg, Predicting positive and negative links in online social networks, Proceedings of the 19th International Conference on World Wide Web, ACM 2010 pp, 641–650.

[14] D. Liben-Nowell, J. Kleinberg, The link-prediction problem for social networks, Journal of the American Society for Information Science and Technology 58 (7) (2007).1019-1031

[15] X. Liu, A. Datta, H. Fang, J. Zhang, Detecting imprudence of ‘reliable’ sellers in online auction sites, Proceedings of the 11th International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom), 2012, pp. 246–253.

[16] H. Ma, M.R. Lyu, I. King, Learning to recommend with trust and distrust relationships, Proceedings of the third ACM Conference on Recommender Systems, ACM, 2009, pp. 189–196.

[17] H. Ma, H. Yang, M.R. Lyu, I. King, Sorec: social recommendation using probabilistic matrix factorization, Proceedings of the 17th ACM conference on Information and Knowledge Management, ACM, 2008, pp. 931–940.

[18] P. Massa, P. Avesani, Trust-aware recommender systems, Proceedings of the 2007 ACM Conference on Recommender Systems (Recsys), 2007, pp. 17–24.

[19] R.C. Mayer, J.H. Davis, F.D. Schoorman, An integrative model of organizational trust, The Academy of Management Review 20 (3) (1995) 709–734.

[20] D.H. McKnight, N.L. Chervany, Trust and distrust de<sup>fi</sup>nitions: one bite at a time, Trust in Cyber-Societies, Springer, 2001, pp. 27–54.

[21] D.H. McKnight, N.L. Chervany, What trust means in e-commerce customer relationships: an interdisciplinary conceptual typology, International Journal of Electronic Commerce 6 (2) (2001) 35–59.

[22] D.H. McKnight, V. Choudhury, Distrust and trust in B2C e-commerce: do they differ? Proceedings of the 8th International Conference on Electronic Commerce, ACM, 2006, pp. 482–491.

[23] A. Mnih, R. Salakhutdinov, Probabilistic matrix factorization, Proceedings of the Advances in Neural Information Processing Systems, 2007, pp. 1257–1264

[24] J. O'Donovan, B. Smyth, Trust in recommender systems, Proceedings of the 10th International Conference on Intelligent User Interfaces (IUI), 2005, pp. 167–174.

[25] T. Opsahl, F. Agneessens, J. Skvoretz, Node centrality in weighted networks: generalizing degree and shortest paths, Social Networks 32 (3) (2010) 245–251.

[26] S. Ray, A. Mahanti, Improving prediction accuracy in trust-aware recommender systems, Proceedings of the 43rd Hawaii International Conference on System Sciences (HICSS), 2010, pp. 1–9.

[27] G. Shafer, A Mathematical Theory of Evidence, vol. 1Princeton university press, Princeton, 1976

[28] P. Singla, M. Richardson, Yes, there is a correlation: from social networks to personal behavior on the web Proceedings of the 17th International Conference on World Wide Web (WWW).2008 pp. 655–664

[29] M. Srivatsa, M. Hicks, Deanonymizing mobility traces: using social network as a side-channel, Proceedings of the 2012 ACM Conference on Computer and Communications Security, 2012, pp. 628–637.

[30] P. Victor, C. Cornelis, M. De Cock, A. Teredesai, Trust-and distrust-based recommendations for controversial reviews, IEEE Intelligent Systems 26 (1) (2011) 48–55.

[31] P. Victor, N. Verbiest, C. Cornelis, M.D. Cock, Enhancing the trust-based recommendation process with explicit distrust, ACM Transactions on the Web (TWEB) 7 (2) (2013) 42–59.

Hui Fang is a PhD student in the School of Computer Engineering (SCE), Nanyang Technological University (NTU), under the supervision of Asst. Professor Jie Zhang and Prof. Nadia Magnenat-Thalmann. Her bachelor and master degrees in Information Management and Information Systems are from Nanjing University, China. Her research focuses on trust and reputation system design for immersive virtual environments, such as virtual marketplaces and e-marketplaces. Her papers have been published by top conferences and journals like AAAI, AAMAS, IJCAI, UMAP and ECRA. She serves as invited reviewer for ECRA, WWWJ, Computational intelligence, and program committee member for WWW 2014–2015, ICWSM2014, IFITTM2014, etc.

Guibing Guo is a PhD student in the School of Computer Engineering, Nanyang Technological University, Singapore. He is under the supervision of Asst. Prof. Jie Zhang and Prof. Daniel Thalmann. His current research is to resolve the data sparsity and cold start problems of recommender systems by: (1) incorporating social trust into collaborative <sup>fi</sup>ltering; (2) designing a Bayesian similarity measure to better utilize user ratings; and (3) proposing the concept of prior ratings to elicit more ratings in virtual reality environments

Jie Zhang is an Assistant Professor of the School of Computer Engineering and Academic Fellow of the Institute of Asian Consumer Insight at NTU. He obtained PhD in Cheriton School of Computer Science from University of Waterloo, Canada, in 2009. During his PhD study, he held the prestigious NSERC Alexander Graham Bell Canada Graduate Scholarship rewarded for top PhD students across Canada. He was also the recipient of the Alumni Gold Medal at the 2009 Convocation Ceremony. The Gold Medal is awarded once a year to honor the top PhD graduate from the University of Waterloo. His papers have been published by top journals and conferences. He has won 4 best paper awards at CNSM'10, IM'09, ITCS'10 and CSWWS'06. Jie Zhang is also active in serving research communities as guest editor for Computational Intelligence, trust theme chair for PST'13, co-chair for WIT-EC and TRUM, associate editor for ICIS'10, PC for AAMAS, AAAI and IJCAI, and reviewer for JAAMAS, Arti<sup>fi</sup>cial Intelligence journal, etc.

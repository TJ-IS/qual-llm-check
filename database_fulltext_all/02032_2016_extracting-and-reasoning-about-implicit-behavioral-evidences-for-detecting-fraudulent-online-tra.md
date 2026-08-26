---
otero_id: 2032
otero_key: "D3DK8ST5"
title: "Extracting and reasoning about implicit behavioral evidences for detecting fraudulent online transactions in e-Commerce"
authors: "Jie Zhao; Raymond Y.K. Lau; Wenping Zhang; Kaihang Zhang; Xu Chen; Deyu Tang"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2016.04.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Extracting and reasoning about implicit behavioral evidences for detecting fraudulent online transactions in e-Commerce

Jie Zhao <sup>a</sup>, Raymond Y.K. Lau <sup>b,</sup>⁎, Wenping Zhang <sup>b</sup>, Kaihang Zhang <sup>a</sup>, Xu Chen <sup>a</sup>, Deyu Tang <sup>c</sup>

<sup>a</sup> Department of Management Science and Engineering, School of Management, Guangdong University of Technology, Guangzhou 510520, China

<sup>b</sup> Department of Information Systems, College of Business, City University of Hong Kong, Hong Kong

<sup>c</sup> School of Medical Information and Engineering, Guangdong Pharmaceutical University, Guangzhou 510006, China

## a r t i c l e i n f o

Article history: Received 12 August 2015 Received in revised form 9 April 2016 Accepted 9 April 2016 Available online xxxx

Keywords: Theory of evidence Evidence fusion Fraud detection Electronic Commerce

## a b s t r a c t

With the explosive growth of e-Commerce worldwide, there are also growing concerns about collusive fraudu lent transaction attacks in e-Commerce. The main contribution of our research work is the design of a novel detection framework that can reason about implicit online user behavior for detecting collusive fraudulent transactions. Based on real transactional and user behavioral data collected from one of the largest e-Commerce platforms in the world, our experimental results confirm that the proposed detection framework can achieve an average true positive detection rate of 83% while the false alarm rate is kept at as low as 2.4%. To the best of our knowledge, this is one of the largest scale studies toward the detection of fraudulent transactions in e-Commerce. The managerial implication of our study is that administrators of e-Commerce platforms can apply our framework to detect and prevent fraudulent transaction attacks, and hence fair electronic trading is upheld in the ever expanding e-Commerce world.

© 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

A recent study reveals that business-to-consumer (B2C) online sales worldwide have reached \$1.5 trillion in 2014, with a growth rate of 20% over 2013.<sup>1</sup> Taobao, one of the largest e-Commerce platforms in the world, generated over 200 million online transactions and reached a peak rate of 205,000 transactions per minute just for its annual “singles' day” sales event taking place on 11 November 2013.<sup>2</sup> However, with the rapid growth of electronic commerce in the past two decades, so are the frequencies of various attacks to e-Commerce systems. The 2014 cybercrime report composed by the Center for Strategic and International Studies (CSIS) in the U.S. shows that the annual financial losses due to cybercrimes including the various attacks to e-Commerce systems may reach \$600 billion.<sup>3</sup>

Among the different kinds of attacks to e-Commerce systems, collusive fraudulent transaction attack is the one that receives relatively less attention by researchers. In fact, there are strong financial incentives for cybercriminals (fraudsters) to generate fake online transactions. For instance, online reputation systems are widely adopted by e-Commerce sites (e.g., Taobao and eBay) so that buyers can indirectly evaluate the reliability of sellers by referring to their service ratings generated based on completed online transactions. To inflate these service ratings, a seller might pretend to be a buyer to purchase from her own online store, or employing a thirty-party attack agency to generate a large number of fake transactions and the corresponding service ratings. It is likely that inflated service ratings of sellers can boost their sales because buyers often rely on an online reputation system to determine from whom they should purchase in e-Commerce. For the study period from October 2008 to May 2009, the percentage of fraudulent transactions among all the consumer-to-consumer (C2C) online transactions conducted in China was found to be as high as 47% [1].

Nowadays, attacks against online transaction systems of e-Commerce sites are systematically managed by organized groups of cybercriminals (e.g., attack agencies). It is very difficult to detect collusive fraudulent transactions because these transactions may just look like legitimate transactions (e.g., having the same explicit features such as transaction amounts). Fig. 1 highlights a typical scenario of collusive fraudulent transaction attack in e-Commerce. The attack agency “C” is an organized group of cybercriminals. A dishonest seller “A” first approaches the agency “C” for generating fraudulent online transactions and inflated her ratings at an e-Commerce platform “D”. The agency “C” accepts the attack requirements (e.g., number of fraudulent transactions and ratings generated in a certain period) posted by the dishonest seller “A” and starts to recruit some collusive buyers

J. Zhao et al. / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/D3DK8ST5/fulltext/images/b7a021c4b5cf336b3e667e2e43f3a637d890d3af6de626917b9aa753e79b9854.jpg)  
Fig. 1. A typical scenario of fraudulent transaction attack in e-Commerce.

such as “B”. A collusive buyer can be a professional cybercriminal (e.g., a member of the agency “C”) or just an ordinary Internet user. The agency “C” routes the attack requirements to “B”. Then, the collusive buyer “B” will purchase some commodities from “A” via the e-Commerce platform “D”. Upon receiving the online purchase from “B”, “A” will pretend to deliver commodities to “B”. After the online transaction is completed, “B” provides an untruthful (inflated) rating for the service quality of “A”. This cycle of fraudulent transaction generation is repeated by each of the recruited collusive buyers.

On the other hand, legitimate buyers observe the inflated rating of “A” via the e-Commerce platform “D”, and eventually they will be lured to purchase from the dishonest seller “A”. It is extremely difficult to detect collusive fraudulent online transactions based on explicit transactional attributes such as prices of commodities, types of commodities, amounts of transactions, or even the ratings of buyers [5]. The reason is that a fraudulent transaction follows the normal transaction processing cycle at the e-Commerce platform D.

Common approaches for detecting attacks to e-Commerce systems include statistical methods [13,40] and machine learning methods [20, 22,25,47–49]. However, these methods often rely on explicit features for detecting fraudulent entities (e.g., a bid in e-Auction). As discussed before, collusive fraudulent transactions may just look like legitimate transactions because they follow the same transaction processing cycle of legitimate transactions at an e-Commerce platform. As a result, existing detection methods that mainly rely on explicit transaction or commodity features may not be able to distinguish between fraudulent and legitimate online transactions. More recently, graph theoretic approaches have been proposed to detect attacks against e-Commerce systems [14–17]. However, these methods often assume that attackers are closely connected within a small social circle. Accordingly, these methods are not effective for detecting attackers who are loosely connected to each other via the global online community (e.g., an attack agency that recruits ordinary Internet users as collusive buyers). In fact, some recent studies show that collusive attackers can easily conceal their relationships with other attackers or attack agencies through a variety of identity hiding methods [9,17].

Accordingly, there is a pressing need to develop an effective method which can take into account both explicit features of transactions (e.g., commodity attributes) and implicit behavior of transacting parties (e.g., how long a buyer browses a product description page before making an online purchase) to tackle fraudulent transaction attacks in e-Commerce. To the best of our knowledge, our work represents one of the largest scale studies toward the detection of fraudulent transactions in e-Commerce. The main contributions of our research work are summarized as follows: (1) we develop a novel fraudulent transaction detection framework that exploits implicit online behavior of transacting parties for the detection of collusive fraudulent transactions in e-Commerce; (2) we extend the classical Dempster–Shafer (DS) uncertainty reasoning model by developing a novel evidence fusion method that can combine possibly conflicting evidences; and (3) we develop a genetic algorithm (GA)-based computational method that can continuously search for the near optimal parameters for dynamically constructing the belief functions of the extended DS model.

The rest of this paper is organized as follows. A discussion of related research work and a comparison of existing work with our approach are given in Section 2. The proposed DS reasoning-based framework for detecting collusive fraudulent transaction attack is highlighted in Section 3. The computational details of the proposed detection framework are illustrated in Section 4. The experimental procedures and result analysis are discussed in Section 5. Finally, we offer concluding remarks and highlight the directions of future research work.

## 2. Related work

## 2.1. Feature analysis for attack detection

Previous research examined different categories of features such as transaction context, social relationship, time factor, and behavioral factor for the detection of attacks against e-Commerce systems. Transaction context refers to transaction related features including explicit features such as prices of commodities [3,5,8,26,27], durations of transactions [3,5,26,27], service quality [3], reputation of buyers (sellers) [5,26,27], and product comments [5]. These features were applied to improve online reputation models [3,26,27] or develop attack detection model [5]. Explicit features such as seller ratings [21–23], starting auction price [19,21,23], bidding increments [11,19,21], and seller transaction history [23,24] were applied to detect shilling attacks in online auctions.

Social relationships among entities were explored to identify potential attacks. The measure of k-core was commonly used to quantify the strength of a relationship between entities [5,14]. Earlier attack prevention models such as Eigentrust [28] and PeerTrust [29] exploited the ratings [15] of entities to identify attacks against social networks. Time factor was also examined to compose high level features such as historical ratings. Online reputation systems such as SPORAS [30] compared the most recent ratings with historical ratings to identify reputation attacks. The dimension of time was applied to monitor traitors' attacks [26,31]. Behavioral factors were examined to build users' preference models in recommender systems [32], or developing attack detection systems [33,36,37]. More recently, finegrained features such as types of browsers, browsing patterns, IP addresses, and so on have been applied to detect various kinds of frauds in E-commerce [34,35].

J. Zhao et al. / Decision Support Systems xxx (2016) xxx–xxx

## 2.2. Classification Models of Attack Detection

Common classification methods for attack detection and prevention include clustering [38], machine learning techniques [12,22,39], regression models [21,23], statistical methods [40], model checking [11,24], graph mining [15,41], and DS evidence reasoning [19,42]. For detecting attacks against recommender systems, it was often assumed that the ratings of attackers significantly deviated from the majority of normal ratings contributed by legitimate users [18,43,44]. Accordingly, rating deviation was often adopted as a feature by classification methods such as collaborative filter [18] and signal-based detection method [25]. Since the boundary between normal behavior and fraudulent behavior was blur [22,45], clustering-based methods might be weak in identifying attackers [46].

Supervised machine learning methods such as decision tree [14,22] and Bayesian network [47] were applied to detect attacks against e-Commerce systems. However, it was quite difficult to acquire labeled data to train supervised classifiers [25,48,49]. Graph theoretic mining methods were applied to detect different kinds of attacks [15,41]. However, Hoffman et al. [9] indicated that collusive attackers could easily conceal their relationships by using various identity hiding methods such as pseudonyms. In fact, it was difficult to assess whether different user accounts actually belonged to the same person [17]. Furthermore, graph mining methods also suffered from the problem of high computational complexity [12].

DS theory of evidence, which is a rigorous uncertainty reasoning framework, has been applied to detect shilling attacks in e-Commerce [19] and attacks to P2P sensor networks [50]. It was shown that a DS reasoning approach was effective even if knowledge about a detection domain was limited [42]. However, it is difficult to select the most appropriate evidences and combine different types of evidences with respect to various detection settings [51].

## 2.3. Research gaps

The proposed framework aims to detect collusive fraudulent transaction attacks [3,5], which are different from shilling attacks in e-Auction [19,22,23] and recommender systems [58]. For the detection of shilling attacks, features such as sellers reputations [23–25], starting bids [21,23,25], bid increments [13,21,23], and deviation from mean agreement [58] are often used. However, the feature set for fraudulent transaction detection is different, and it includes features such as rating of a transaction, confirmation interval of a transaction, browsing time of a product Webpage, and so on. Moreover, existing detection methods mainly examines explicit detection features, whereas our proposed detection framework combines both explicit and implicit features for detecting fraudulent transaction attacks. In addition, our detection framework exploits the concept of information granularity [53] by extracting features from a hierarchy of entity to enhance detection accuracy.

While supervised machines learning methods have been examined for fraud detection before [14,22,50], their practical applications to fraudulent transaction detection is questionable due to the lack of labeled training examples. Graph theoretic methods [14–17] often assume that attackers are closely connected within a small social circle. However, typical collusive attackers may be loosely connected in e-Commerce. Although DS-based methods are promising for attack detection, evidence selection and fusion is still a challenging research problem. Our proposed framework differs from existing DS-based methods in that a novel evidence fusion algorithm is developed to combine possibly conflicting evidences at different levels of granularity to enhance attack detection performance. Moreover, a genetic algorithm is developed to search for near optimal parameters to enhance DS-based detection.

## 3. The proposed DS reasoning-based attack detection framework

An overview of the proposed DS reasoning-based attack detection framework is depicted in Fig. 2. The upper section of Fig. 2 highlights the classical DS reasoning model, whereas the lower section of Fig. 2 depicts the new modules (with filled line patterns in green color) of the proposed detection framework.

The main intuition of the classical DS reasoning model is that various features of an entity (e.g., the amount of a transaction) are first converted to the corresponding evidences (e.g., the likelihood of a certain transaction amount suggesting a collusive transaction). Then, some combination rules are applied to aggregate all available evidences to determine the final class label of the entity. However, the transformation of features to evidences is application dependent, and the classical DS reasoning model does not prescribe a computational method to convert features to evidences. Moreover, the classical DS reasoning model deals with elementary features (evidences) only. Nevertheless, to improve the accuracy of detecting the fraudulent status of an entity (e.g., a transaction), it may be advantageous to utilize the features (evidences) of other related entities (e.g., commodities or buyers) as well. Our research aims to alleviate the aforementioned weaknesses of the classical DS reasoning model. Essentially, the classical DS reasoning model consists of the following four components: data acquisition,

![](/api/attachments/D3DK8ST5/fulltext/images/25591f5295466595df32f98b07e3d3ce4875395a191b07ca8243a6769bb234ab.jpg)  
Fig. 2. An overview of DS reasoning-based attack detection framework.

Please cite this article as: J. Zhao, et al., Extracting and reasoning about implicit behavioral evidences for detecting fraudulent online transactions in e-Commerce, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.04.003

J. Zhao et al. / Decision Support Systems xxx (2016) xxx–xxx

feature library construction, evidence construction, and evidence combination.

## 3.1. Data acquisition

The data acquisition component retrieves elementary features of entities from different data sources. For the classical DS reasoning model, usually only explicit data sources (e.g., a transaction log) are considered. The proposed detection framework differs from the classical model in that it takes into account both explicit (E) and implicit (I) (e.g., the Web server log of an e-shop) data sources to enhance detection accuracy.

## 3.2. Feature library construction

The feature library construction component employs a set of feature extractors to pre-process (e.g., normalize feature values) and transform (e.g., converting real value features to discrete value features) a variety of elementary features. Feature library construction is a semi-automatic process that usually involves a human-assisted knowledge engineering process. Generally speaking, a rich set of features should be extracted and archived in the feature library for subsequent evidence construction. For the classical DS reasoning model, usually only explicit features are extracted. In contrast, the proposed detection framework extracts both explicit and implicit features for subsequent evidence construction.

## 3.3. Evidence construction

The evidence construction component converts each feature archived at the feature library to evidence by using a basic belief assignment (BBA) function, which is also called the basic mass assignment function [19]. The classical DS reasoning model does not prescribe a computational method to build the BBA functions. The main difference between a feature and an evidence is that a feature has a real or discrete value to describe an entity (e.g., transaction amount = 300 K), whereas an evidence is equipped with a BBA function to map feature values to the “degree of certainty” of classifying the entity into a certain class (e.g., collusive or non-collusive). In general, a BBA library is applied to capture all BBA functions. One novelty of the proposed detection framework is that historical reasoning results are utilized to select the most discriminative subset of features for evidence construction by using the proposed Algorithm 1 that will be illustrated in Section 4.1. In addition, this novel algorithm can systematically establish the appropriate evidence threshold to enhance the mapping of features to evidences.

Another novelty of the proposed detection framework is that an enhanced feature set constructor is developed to build composite features extracted from a hierarchy of entities, that is,commodity⇒ seller⇒buyer⇒transaction, where ⇒ denotes the hierarchical relation in the proposed entity model. First, a set of common commodities is defined at the top of the entity hierarchy. These commodities are sold by one or more sellers (e-shops), and a seller can transact with one or more buyers via some transactions. For instance, the composite feature for verifying the collusive status of a transaction may include the features of the transaction (e.g., confirmation time of a transaction) and the buyer's features (e.g., buyer's browsing time of the corresponding product page). Finally, the composite BBA library contains composite BBA functions that can convert composite features to aggregated evidences. Aggregated evidences are not available in the classical DS reasoning model.

## 3.4. Evidence combination

The goal of evidence combination (fusion) is to gather all individual evidences of an entity to infer its class label (e.g., fraudulent or legitimate). In the classical DS reasoning model, only elementary evidences are combined to infer the class label of an entity. In contrast, the proposed detection framework utilizes a novel evidence fusion algorithm called Dempster–Shafer Reinforced Combination (DSRC) to combine both elementary and aggregated evidences extracted from the hierarchical model of entities to infer the class label of an entity. For an effective DS-based reasoning, it is important to assign appropriate weights to each evidence. In the classical DS model, the weights of evidences are assumed to be defined manually. In contrast, the proposed detection framework utilizes a Genetic Algorithm (GA) to systematically search for the near optimal weight for each evidence based on historical reasoning results. Moreover, the GA-based method can continuously search for near optimal weights given possibly evolving features and evidences.

A formal specification of the proposed reasoning model is given by a quintuple bO,BL,F,BM,C,T N.

➢ $O = \{ o _ { 1 } , o _ { 2 } . . . , o _ { n } \}$ denotes the set of entities (e.g., buyers, transactions, etc.) to be detected (classified).

➢ BL:{bel: O➔[0,1]} is a set of belief functions that estimates the degree of certainty for an entity holding a certain class label (e.g., fraudulent, legitimate, suspicious).

➢ $F = \{ f _ { 1 } , f _ { 2 } , . . . , f _ { k } \}$ is a set of features extracted from the hierarchical entity model; some subsets of these features are utilized to infer the label of an entity under detection.

$\vdash B M = \{ m \colon \mathbb { F }  [ 0 , 1 ] \}$ is a set of BBA functions that estimates the likelihood of an entity holding a certain fraudulent status if it is characterized by a specific feature value. For the proposed framework, we use the labels “collusive” and “\~collusive” to denote positive and negative fraudulent status, respectively. Two parameters $\alpha _ { f _ { i } }$ and $\beta _ { f _ { i } }$ are needed to adjust the weight of each feature f for deducing the label of an entity.

$C = \{ c _ { 1 } , c _ { 2 } , . . . , c _ { m } \}$ is a set of combination rules applied to combine all the evidences pertaining to an entity to generate a final class label by using a threshold set T.

➢ T = {θ,φ} is a threshold set for deducing the final class label of an entity. The two belief thresholds follow the inequality $\theta < \varphi ,$ and the final class label is defined by:

$$
\left\{ \begin{array}{l} \text {   legitimate   } b e l _ {o _ {i}} (\text {   collusive   }) \leq \theta \\ \text {   suspicious   } \theta <   b e l _ {o _ {i}} (\text {   collusive   }) \leq \varphi \text {   and   } b e l _ {o _ {i}} (\sim \text {   collusive   }) \leq b e l _ {o _ {i}} (\text {   collusive   }) \\ \text {   fraudulent   } \varphi <   b e l _ {o _ {i}} (\text {   collusive   }) \end{array} \right.\tag{1}
$$

The ultimate goal of the proposed reasoning framework is to infer (classify) a set of entities O to have one of the labels from the label set L = {legitimate, suspicious, fraudulent}. For the proposed framework, each entity can only be assigned at most one label. A universal set U = {collusive, \~collusive, unknown} is defined to capture the uncertainty that a feature f may characterize a fraudulent entity. Each feature value is normalized and it satisfies the condition $0 { < } f _ { i } { \leq } 1$ . The parameters (evidence weights) $0 { < } \alpha _ { f _ { i } } { \leq } 1$ and $0 { < } \beta _ { f _ { i } } { \leq } 1$ are applied to strengthen or weaken the feature f for reasoning about the collusive status of an entity as follows [19]:

$$
\left. \begin{array}{c} m _ {f _ {i}} (\text { collusive }) = \alpha_ {f _ {i}} \times h _ {f _ {i}} \\ m _ {f _ {i}} (\sim \text { collusive }) = 0 \\ m _ {f _ {i}} (\text { unknown }) = 1 - \alpha_ {f _ {i}} \times h _ {f _ {i}} \end{array} \right\}\tag{2}
$$

$$
\left. \begin{array}{c} m _ {f _ {i}} (\text { collusive }) = 0 \\ m _ {f _ {i}} (\sim \text { collusive }) = \beta_ {f _ {i}} \times g _ {f _ {i}} \\ m _ {f _ {i}} (\text { unknown }) = 1 - \beta_ {f _ {i}} \times g _ {f _ {i}} \end{array} \right\}\tag{3}
$$

where $m _ { f _ { i } } \in$ B is the BBA function of a feature $f _ { i \cdot }$ In addition, $h _ { f _ { i } }$ and $g _ { f _ { i } }$ are the corresponding evidence conversion functions that will be described in Section 4.6. Finally, all the evidences are combined by using the classical DS fusion method [19] or the proposed Dempster–Shafer Reinforced Combination (DSRC) fusion method. Conceptually, the final belief function $b e l _ { o _ { i } } ( c o l l u s i v e )$ for an entity $o _ { i }$ is defined based on the combination of individual BBA functions, that is, $b e l _ { o _ { i } } ( c o l l u s i v e ) =$ $\oplus _ { f _ { i } \in o _ { i } } m _ { f _ { i } } ( c o l l u s i \nu e )$ , where ⊕ is a composition (fusion) function.

## 4. The computational details of the proposed framework

## 4.1. Feature selector

Generally speaking, feeding all available features to a classifier may not necessarily lead to the most accurate classification result due to the problem of over-fitting. In addition, a large amount of computational time is needed to process all available features. Accordingly, feature selection is a standard procedure of any classification framework. However, it is quite complicated to select the most discriminative subset of features given numerous possible feature subsets. Although Rafael applied the odds ratio to select a reasonable subset of features, the method was only applicable to binary features [34]. One main contribution of our research is that we develop a novel feature selection algorithm (Algorithm-1) to extract a near optimal subset of binary and real value features, and estimating the appropriate thresholds $( t h _ { f _ { i } } ^ { c } , t h _ { f _ { i } } ^ { n c } )$ of the corresponding evidences.

Let CO and NCO denote the sets of collusive and non-collusive entities, respectively. These two sets satisfies the equality: $| C O | + | N C O | = | \mathrm { a l l }$ entities with labels|. For each feature $f _ { i } \in F ,$ let $O _ { f _ { i } }$ be the set of entities having the feature f . Then, the classical odds ratio (OR) [34] and the proposed evidence thresholding metrics $f t h r _ { f _ { i } } ^ { c }$ and $f t h r _ { f _ { i } } ^ { n c }$ are defined as follows.

$$
p _ {1} = \frac {\left| O _ {f _ {i}} \cap C O \right|}{\left| C O \right|}
$$

$$
p _ {2} = \frac {\left| O _ {f _ {i}} \cap N C O \right|}{\left| N C O \right|}\tag{4}
$$

ð<sup>5</sup>Þ

$$
O R = \frac {p _ {1} / (1 - p _ {1})}{p _ {2} / (1 - p _ {2})}\tag{6}
$$

$$
f t h r _ {f _ {i}} ^ {c} = (p _ {1} - p _ {2}) ^ {2} * p _ {1}\tag{7}
$$

$$
f t h r _ {f _ {i}} ^ {n c} = (p _ {2} - p _ {1}) ^ {2} * p _ {2}\tag{8}
$$

To identify the discriminative features, we need to count the number of entities falling into the two classes CO and NCO. The term $p _ { 1 }$ refers to the percentage of entities characterized by the feature $f _ { i }$ that are really “collusive” entities, while $p _ { 2 }$ is the percentage of entities characterized by the feature $f _ { i }$ that are “non-collusive” entities. The odd ratio OR measures the relative power of $p _ { 1 }$ dividing the entities into two different classes, and so it is applied to select discriminative features [34]. To properly divide all entities into two classes according to the feature $f _ { i } ,$ usually an evidence threshold is needed. Previous work assumed that such a threshold could be pre-defined manually [34]. For the proposed framework, we develop Algorithm-1 (illustrated in Fig. 3) to automatically estimate such a threshold. Since a feature may provide partial evidence of classifying an entity into the collusive class, and yet it may also provide partial evidence of classifying an entity into the noncollusive class, two evidence thresholds could be estimated for each feature.

In practice, a threshold value estimated based on the largest (smallest) OR may not be the optimum. By way of illustration, we use a threshold estimation example shown in Table 1. Based on the feature of Average Confirmation Interval of Buyers “acib”, the first estimation (the first record in Table 1) has a relatively high OR value of 10.17857 while its $p _ { 1 }$ value is 0.024876 only. In fact, the high OR is caused by the very low value of $p _ { 2 } .$ In other words, a BBA function developed based on the OR of $" \mathrm { a c i b } '$ tends to assign 2.4876% entities to the collusive class only. Accordingly, many true-positive cases will be missed out if we apply the “acib” feature with the particular evidence threshold estimated based on OR (the first record in Table 1). In contrast, both a large OR and a large $p _ { 1 }$ can better identify entities of the collusive classes. Accordingly, the factors ${ < O R , f t h r _ { f _ { i } } } ^ { c } >$ together should be considered to estimate the corresponding collusive evidence threshold in the BBA library. The second record in Table 1 depicts such an example. So, if an estimation satisfies the condition: $O R \geq 2 \ [ 3 4 ]$ and max( $f t h r _ { f _ { i } } { c } )$ , the corresponding collusive (positive) evidence threshold will be chosen. As a result, the evidence threshold $t h _ { f _ { i } } { } ^ { c }$ for the acib feature should be 2.642211 instead of 1.793669 in our example. Similarly, if an estimation satisfies the condition: $O R \leq 0 . 5$ and $m a x ( f t h r _ { f _ { i } } { } ^ { n c } )$ , the corresponding non-collusive (negative) evidence threshold can be estimated.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 – an algorithm for estimating the evidence threshold of a feature
Inputs: The domain of a feature $f_i$, type of evidence $type_e$
Outputs: tuples of candidate thresholds &lt;$p_1$, $p_2$, OR, $th_{f_i}^c$, $fthr_{f_i}^c$ &gt; or &lt;$p_1$, $p_2$, OR, $th_{f_i}^{nc}$, $fthr_{f_i}^{nc}$ &gt;
1. FOR each value $v_i \in dom(f_i)$, let $th = v_i$, and initializes $coc = 0$, $ncoc = 0$;
2. FOR each value $v_i$ of the feature $f_i$
3. IF $type_e$=positive
    IF $v_i \geq th$ //means the object with this value is classified as collusive
    IF the label of the entity is collusive, $coc++$
    IF the label of the entity is non-collusive, $ncoc++$
ELSE // if $type_e$=negative
    IF $v_i \leq th$ //means the object with this value is classified as collusive
    IF the label of the entity is collusive, $coc++$
    IF the label of the entity is non-collusive, $ncoc++$
4. IF $type_e$=positive
    calculate $p_1$, $p_2$, OR and $fthr_{f_i}^c$ according to formulas (4),(4),(6),(7)
    IF OR≥2, the tuple &lt;$p_1$, $p_2$, OR, th, $fthr_{f_i}^c$ &gt; is added to the output list of type $type_e$
ELSE // if $type_e$=negative
    calculate $p_1$, $p_2$, OR and $fthr_{f_i}^{nc}$ according to formulas (4),(4),(6),(8)
    IF OR≤0.5, the tuple &lt;$p_1$, $p_2$, OR, th, $fthr_{f_i}^{nc}$ &gt; is added to the output list of type $type_e$
5. RETURN the output list
</div>

Fig. 3. An algorithm for estimating the evidence threshold of a feature.

Table 1  
An example of evidence threshold with two different values.

<table><tr><td>Estimation</td><td>Feature</td><td> $p_{1}$ </td><td> $p_{2}$ </td><td>OR</td><td> $th_{f_{i}}^{c}$ </td><td> $fthr_{f_{i}}^{c}$ </td></tr><tr><td>1</td><td>acib</td><td>0.024876</td><td>0.002500</td><td>10.17857</td><td>1.793669</td><td>0.050707</td></tr><tr><td>2</td><td>acib</td><td>0.119403</td><td>0.018333</td><td>7.260401</td><td>2.642211</td><td>0.483032</td></tr></table>

According to the proposed threshold estimation metric, both $( p _ { 1 } - p _ { 2 } ) ^ { 2 }$ and $p _ { 1 } \left( p _ { 2 } \right)$ are applied to search for an effective evidence threshold. For positive evidence, the absolute value of $p _ { 1 }$ should be large, and there should be a large gap between $p _ { 1 }$ and $p _ { 2 } .$ . The reason is that collusive entities should be assigned to the collusive class with a high probability and non-collusive entities should be assigned to the same class with a low probability. To ensure a large gap between the values of $p _ { 1 }$ and $p _ { 2 } ,$ , the proposed $f t h r _ { f _ { i } } { c }$ metric applies the square of difference between $p _ { 1 }$ and $p _ { 2 } ,$ that is, $( { \dot { p } } _ { 1 } - p _ { 2 } ) ^ { 2 } .$ In case we need to find other feasible evidence thresholds, all the estimations (tuples in Table 1) can be sorted according to the descending order of $f t h r _ { f _ { i } } ^ { c } .$ In addition, for any estimation with $\mathsf { a } f t h r _ { f _ { i } } ^ { c }$ less than max $( f t h r _ { f _ { i } } { } ^ { c } )$ and its odd ratio satisfying ${ \mathsf { O R } } \geq 2 \ [ 3 4 ]$ , it is considered a feasible threshold value. Although we mainly explain how to estimate the evidence threshold $t h _ { f _ { i } } { c }$ that is related to the collusive class so far, the non-collusive evidence threshold $t h _ { f _ { i } } { } ^ { n c }$ can also be estimated based on Algorithm 1. We only need to specify the type of evidence threshold to be estimated by using an input flag type<sub>e</sub>.

## 4.2. Enhanced feature set constructor

Based on the formal model of detecting fraudulent transactions illustrated in the previous section, it can be generalized with respect to the hierarchy of entities. Accordingly, we can develop the specialized models for sellers, buyers, commodities, and transactions, respectively. That is, the basic detection model is extended to $< O _ { S } , b e l _ { S } , F _ { S } , B _ { S } , C _ { S } , T _ { S } >$ $< O _ { B } , b e l _ { B } , F _ { B } , B _ { B } , C _ { C } , T _ { B } > , < O _ { C } , b e l _ { C } , F _ { C } , B _ { C } , C _ { C } , T _ { C } > , \mathrm { a n d } < O _ { T } , b e l _ { T } , F _ { T } , B _ { T } , C _ { T } , T _ { T } > \ ,$ N with with each sub-model capturing its own feature library, BBA functions, combination rules, belief functions, and threshold set. For existing DSbased detection approaches, each feature is an elementary property of an entity, and the belief assignment function is applied to the elementary property only [19]. The proposed detection framework differs from existing approaches in that the features extracted from the hierarchy model of entities can be combined to construct aggregated features. Moreover, classified entities of a sub-model are taken as features of another sub-model. For instance, detected fraudulent buyers can be applied as a kind of feature for the detection of transactions. Accordingly, the proposed formal detection model is extended $t 0 < O , b e l , F ^ { e } , B , C , T > ,$ where $F ^ { e }$ refers to the composition of aggregated features extracted from a hierarchy of entities.

## 4.3. Evidence composition

For combining simple evidences that are constructed based on elementary features, the classical DS reasoning model can be used. However, there may be conflicts of aggregated evidences extracted from a hierarchy of entities. For instance, a transaction may consist of several commodities, whereas some commodities are the common targets of attacks and yet other commodities are considered legitimate. Consequently, an aggregated evidence that comprises transactional and commodity features may suggest both a collusive and non-collusive classes. Accordingly, we develop a novel fusion method named Dempster–Shafer Reinforced Combination (DSRC) for combining potentially conflicting evidences. The proposed DSRC algorithm is shown in Fig. 4. The notations used in the DSRC algorithm are summarized in Table 2.

Algorithm 2 aims to extract and fusion aggregated evidences extracted from the hierarchical entity model to infer the class label of an input entity $0 _ { \mathrm { p . } }$ Inputs to the algorithm include two evidence thresholds $t h _ { f _ { i } } ^ { ~ c }$ and $t h _ { f _ { i } } { } ^ { n c }$ , a discount coefficient d, and the entity $0 _ { \mathrm { p } }$ to be reasoned about. First, the related entities $S O _ { o _ { p } }$ are retrieved from the hierarchical entity model. The evidences $b e l _ { s _ { k } }$ (collusive), $b e l _ { s _ { k } } ( \sim \mathrm { c o l l u s i v e } )$ and $b e l _ { s _ { k } } ( \mathrm { u n k n o w n } )$ of each entity $s _ { k }$ belonging to the entity set $S O _ { o _ { v } }$ are computed. The working variables ${ \cal { C } } _ { { \cal { O } } _ { v } } ^ { \quad s u m } = 0$ and $n c _ { o _ { n } } ^ { \phantom { } s u m } = 0$ are initialized. Then, each entity $s _ { k }$ is examined to infer its class label based on two evidence thresholds $t h _ { f _ { i } } { c }$ and $t h _ { f _ { i } } { } ^ { n c }$ These thresholds can divide the hierarchical entity set $S O _ { o _ { p } }$ into three classes.

More specifically, if $b e l _ { s _ { k } } ( c o l l u s i v e ) \geq t h _ { f _ { i } } { c }$ , s is considered to be collusive, and the counter $\stackrel { \cdot } { c _ { o _ { p } } } ^ { s u m }$ is increased by one. Similarly, if $b e l _ { s _ { k } } ( - c o l l u s i v e ) \leq t h _ { f _ { i } } ^ { \ n c }$ , s is considered to be \~collusive, and the counter $n c _ { o _ { p } } ^ { \phantom { * } \tilde { s u m } }$ is increased by one. The counter variables ${ c _ { o _ { v } } } ^ { s u m }$ and ${ n { c _ { o _ { p } } } ^ { s u m } }$ are used to count the number of collusive and non-collusive evidences. Then, the BBAs of $0 _ { p }$ are established according to ${ c _ { o _ { p } } } ^ { s u m }$ and ${ n c _ { o _ { p } } } ^ { s u m }$ . If $C _ { o _ { p } } ^ { \phantom { } s u m } \geq n c _ { o _ { p } } ^ { \phantom { } s u m }$ is true, it suggests that the aggregated evidences supports the conclusion that $o _ { p }$ is collusive; otherwise, $\mathrm { i f } \ C _ { o _ { v } } { } ^ { s u m } < n c _ { o _ { v } } { } ^ { s u m }$ is true, $o _ { p }$ is inferred to be non-collusive. For the special case that there is only one level of entity $s _ { k } ,$ its BBA functions such as $b e l _ { s _ { k } } ( c o l l u s i v e )$ is discounted by using the discount factor d because it is a relatively weak evidence. Finally, the aggregated evidence of $0 _ { p }$ is returned.

By way of illustration for Algorithm 2, suppose that there are elementary features describing a commodity c . If some buyers purchase this commodity, the features of the corresponding transactions and the buyers can be used to infer the class label of the commodity $c _ { i \cdot }$ Assume that there are three buyers of the commodity $\tau _ { i } .$ Let the evidence formed by a buyer $b _ { i }$ for the commodity c to be denoted $b _ { i } ( m _ { b u y e r } ^ { c _ { i } } ( c o l l u s i \nu e )$ $m _ { b u y e r } ^ { c _ { i } } ( \sim c o l l u s i \nu e ) , m _ { b u y e r } ^ { c _ { i } } ( u n k n o w n ) )$ ). Further, we assume that the evidences of these three buyers are estimated as follows: $b _ { 1 }$ (0.965,0.002,0.032), b (0.952,0.020,0.048), b (0.336,0.0,0.664). If the evidence thresholds $t h _ { f _ { i } } ^ { ~ c }$ and $t h { _ { f _ { i } } } ^ { n c }$ are 0.95 and 0.4, respectively, the likelihood of the commodity c being fraudulent is (0.333,0, 0.667) based on the following evidence combination procedure: $\begin{array} { r } { { c } _ { c _ { i } } ^ { \ s u m } . c = \frac { | C _ { k } ^ { s u m } | - | N C _ { k } ^ { s u m } | } { | { \cal O } _ { k } | } = } \end{array}$ $\begin{array} { r } { \frac { 2 - 1 } { 3 } = \frac { 1 } { 3 } , \ c _ { o _ { p } } ^ { \ s u m } . \ u \ = \ 1 - c _ { o _ { p } } ^ { \ s u m } . c \ = \ 1 - 0 . 3 3 3 \ = \ 0 . 6 6 7 . } \end{array}$ . The evidence thresholds $t h _ { f _ { i } } ^ { ~ c }$ and $t h _ { f _ { i } } ^ { { n c } }$ are estimated based on Algorithm 1 as illustrated in Section 4.1. On the other hand, if the evidence threshold $t h _ { f _ { i } } ^ { ~ c }$ and $t h _ { f _ { i } } { } ^ { n c }$ are 0.98 and 0.4, the likelihood of the commodity $c _ { i }$ being fraudulent is (0, 0.333, 0.667) based on the following evidence combination procedure: $\begin{array} { r } { { c _ { c _ { i } } } ^ { s u m } . n c = { \frac { | N C _ { k } ^ { s u m } | - | C _ { k } ^ { s u m } | } { | O _ { k } | } } = \frac { 1 - 0 } { 3 } = \frac { 1 } { 3 } , { c _ { o _ { p } } } ^ { s u m } . u = } \end{array}$ $1 - c _ { o _ { p } } { } ^ { s u m } . n c = 1 - 0 . 3 3 3 = 0 . 6 6 7$

## 4.4. The composite basic belief assignment library

The BBA library captures all the BBA functions which convert features to evidences. Subsequently, evidences (with uncertainty) are reasoned to produce a final conclusion (i.e., a class label) by using the

```txt
Please cite this article as: J. Zhao, et al., Extracting and reasoning about implicit behavioral evidences for detecting fraudulent online transactions in e-Commerce, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.04.003
```

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2 – An algorithm for the fusion of hierarchical evidences
Inputs: thresholds $th_{f_i}^c$, $th_{f_i}^{nc}$ ($th_{f_i}^c &gt; th_{f_i}^{nc}$), discount coefficient $d$, an entity $o_p$ to be classified
Outputs: the aggregated evidence $sf_j$ of the entity $o_p$
1. extract the related hierarchical entity set $SO_{o_p}$ of $o_p$ // retrieve the corresponding hierarchical entities related to $o_p$
2. initialize $c_{o_p}^{sum} = 0$, $nc_{o_p}^{sum} = 0$ // initialize two working variables
3. FOR each entity $s_k$ in $SO_{o_p}$ // loop through each entity $s_k$ in the hierarchical entity set $SO_{o_p}$
IF $bel_{s_k}$ (collusive) ≥ $th_{f_i}^c$ $c_{o_p}^{sum}++$
ELSE IF $bel_{s_k}$ (collusive) ≤ $th_{f_i}^{nc}$ // sum entities with collusive probability equal to or greater than $th_{f_i}^c$ (collusive entities)
$nc_{o_p}^{sum}+$ // and those with collusive probability equal to or less than $th_{f_i}^{nc}$ (~collusive entities)
4. IF $c_{o_p}^{sum} \geq nc_{o_p}^{sum}$
// for an entity op, if the number collusive entities is larger than that of ~collusive entities in the corresponding hierarchical entity mode
IF $c_{o_p}^{sum} = 1$ // if there is only one entity, then $bel_{s_k}$ (collusive) should be discounted and assigned to $m_{sf_j}^{o_p}$ (collusive)
$m_{sf_j}^{o_p}$ (collusive)=$bel_{s_k}$ (collusive)*$d$
ELSE
$m_{sf_j}^{o_p}$ (collusive)=$\frac{c_{o_p}^{sum}-nc_{o_p}^{sum}}{|SO_{o_p}|}$ // else it's calculated according to $c_{o_p}^{sum}$ and $nc_{o_p}^{sum}$
// $m_{sf_j}^{o_p}$ (~collusive) and $m_{sf_j}^{o_p}$ (unknown) are calculated
$m_{sf_j}^{o_p}$ (~collusive)=0, $m_{sf_j}^{o_p}$ (unknown)=1-$m_{sf_j}^{o_p}$ (collusive)
ELSE IF $c_{o_p}^{sum}&lt;nc_{o_p}^{sum}$ // if the number of collusive entities is smaller than that of ~collusive entities
// if there is only one entity, then $bel_{s_k}$ (~collusive) should be discounted and assigned to $C_{o_p}^{sf_j}.(\sim collusive)$
IF $nc_{o_p}^{sum}=1$ $m_{sf_j}^{o_p}$ (~collusive)= $bel_{s_k}$ (~collusive)*$d$
ELSE
$m_{sf_j}^{o_p}$ (~collusive)=$\frac{nc_{o_p}^{sum}-c_{o_p}^{sum}}{|SO_{o_p}|}$ // $m_{sf_j}^{o_p}$ (collusive) and $m_{sf_j}^{o_p}$ (unknown) are calculated
$m_{sf_j}^{o_p}$ (collusive)=0, $m_{sf_j}^{o_p}$ (unknown)=1-$m_{sf_j}^{o_p}$ (~collusive)
5. RETURN $m_{sf_j}^{o_p}$ (collusive), $m_{sf_j}^{o_p}$ (~collusive), $m_{sf_j}^{o_p}$ (unknown)
</div>

Fig. 4. An algorithm for the fusion of hierarchical evidences

DS reasoning framework. The BBA functions pertaining to the features of seller, buyer, commodity, and transaction are developed to link each evidence to one of the labels of the universal set $U = \{ c o l l u s i v e ,$ \~collusive, unknown} and attach a certainty value to each of these labels. There are two types of BBA functions. The first type of BBA function converts features to positive evidences $( \mathrm { i . e . } ,$ , evidences supporting the conclusion that the underlying entity is collusive), and the second type converts features to negative evidences (i.e., evidences supporting the conclusion that the underlying entity is non-collusive). The general formats of these BBA functions are defined in Eqs. 2 and 3, respectively. For each evidence conversion function (e.g., g ), an evidence threshold is required. These evidence thresholds are systematically estimated based on Algorithm 1. Similarly, the near optimal parameters $( \alpha _ { f _ { i } } , \beta _ { f _ { i } } )$ of each feature are searched by using a genetic algorithm that will be described in the following sub-section.

## 4.5. Near optimal parameter searcher

As described in Section 4.4, two parameters $( \alpha _ { f _ { i } } , \beta _ { f _ { i } } )$ are required for the construction of each BBA function. If there are n features used in the reasoning model, the total number of parameters is 2n. So, it is not practical to set these parameters manually. A systematic and effective method is needed to establish the evidence weights for the accurate detection of fraudulent transactions. For the proposed detection framework, we develop a GA to dynamically search for the near optimal parameters based on the historical detection results. First, the historical detection results with labeled entities (e.g., transactions) are used as training data. For the proposed GA, the fitness function is developed based on the formulation of calculating the area under the ROC curve (i.e. AUC value). The size of a population is set to 40 with a step length of 0.01, and 15 fittest seeds are kept in each generation. Real-value encoding is applied to each chromosome; all the evidence parameters (e.g., the 2n evidence weights) are encoded as evolving genes in each chromosome. A maximum of 1000 generations is applied to each evolution process to adequately explore the entire search space. Two-point crossover and uniform mutation are applied. The crossover and mutation rates are set to 0.75 and 0.05, respectively [54]. After each evolution process, the near optimal parameters (i.e. evidence parameters) are applied to the unseen test set (e.g., the online transactions under detection).

Notations used in the DSRC algorithm.

<table><tr><td>No</td><td>Notation</td><td>Statement</td></tr><tr><td>1</td><td> $th_{f_i}^{c}$ </td><td>the evidence threshold for the collusive class. In other words, if an entity&#x27;s collusive probability is equal to or greater than  $th_{f_i}^{c}$ , it can be considered collusive. This threshold is estimated based on Algorithm 1.</td></tr><tr><td>2</td><td> $th_{f_i}^{nc}$ </td><td>the evidence threshold for the non-collusive class. In other words, if an entity&#x27;s collusive probability is equal to or less than  $th_{f_i}^{nc}$ , it can be considered ~collusive. This threshold is estimated based on Algorithm 1.</td></tr><tr><td>3</td><td>D</td><td>a discount coefficient</td></tr><tr><td>4</td><td> $O_i$ </td><td>a set of hierarchical entities to be classified</td></tr><tr><td>5</td><td> $o_p$ </td><td>an entity from the set  $O_i$ </td></tr><tr><td>6</td><td> $sf_j$ </td><td>the  $jth$  summary feature of  $o_p$ </td></tr><tr><td>7</td><td> $SO_{o_p}$ </td><td>a set of hierarchical entities corresponding to  $o_p$ </td></tr><tr><td>8</td><td> $|SO_{o_p}|$ </td><td>the number of entities in  $SO_{o_p}$ </td></tr><tr><td>9</td><td> $s_k$ </td><td>an entity in the set  $SO_{o_p}$ </td></tr><tr><td>10</td><td> $c_{o_p}^{sum}$ </td><td>total number of entities in  $SO_{o_p}$  with collusive probability  $\geq th_c$ </td></tr><tr><td>11</td><td> $nc_{o_p}^{sum}$ </td><td>total number of entities in  $SO_{o_p}$  with collusive probability  $\leq th_{nc}$ </td></tr></table>

## 4.6. Detection features

Given the numerous number of features used in the proposed framework, we only highlight the most representative features in this sub-section. Explicit features refer to the transactional data that are made public at the Website of an e-Shop. Typical explicit features include a commodity's title, price, rating, and so on. On the other hand, implicit features include the features that can be extracted from the backstage of an e-Shop or extracted based on the behavioral analysis of various log records kept at an e-Commerce platform such as Taobao. Common implicit features include the number of days after transaction confirmation, settlement time, depth of browsing an e-Commerce site, and so on. Since most implicit behavioral features such as Average Stay Time on Commodities of Transitions (ASTCT) and Returning Visitor of Transactions (RVT) can be extracted as long as one transaction is completed, the proposed detection framework is effective for repeated fraudsters or one-off fraudsters. In fact, our detection framework can alleviate the cold-start detection problem because only minimal knowledge (e.g., information of a single transaction) about the attackers is required.

## 4.6.1. Features of transactions

4.6.1.1. Invalid rating of transactions (IRT)—explicit. If a buyer purchases two identical commodities from the same seller in one month, the two transaction ratings toward the seller are considered invalid by some e-Commerce platforms such as Taobao. This behavioral feature can be used to predict the probability of a fraudulent transaction. For instance, the positive evidence (i.e., evidence supporting the collusive class) function $h _ { I R T }$ is defined by: $h _ { I R T } = \left\{ \begin{array} { c c } { 1 - \frac { t h _ { I R T } ^ { c } } { N _ { c } } } & { i f \ : N _ { c } \ge t h _ { I R T } ^ { c } } \\ { 0 } & { i f \ : N _ { c } < t h _ { I R T } ^ { c } } \end{array} \right.$ , where $t h _ { I R T } ^ { c }$ is the evidence threshold of the feature IRT, and it is estimated based on Algorithm 1. The term $N _ { c }$ refers to the number of identical commodities purchased by a buyer in one month.

4.6.1.2. Negative or neutral rating of transactions (NNRT)—explicit. Since the objective of fraudsters is to inflate the reputation scores of some sellers, it is unlikely that attackers will give neutral or even negative ratings for the fraudulent transactions. So, the more neutral or negative ratings are attached to a transaction, the more likely that it is legitimate. The feature NNRT is characterized by $\left\{ \begin{array} { c c } { \frac { 1 } { N _ { r a t e } } } & { \mathrm { i f } N _ { r a t e } { > } 0 } \\ { \infty } & { e l s e } \end{array} \right.$ , where $N _ { r a t e }$ captures the number of neutral and negative ratings. The negative evidence (i.e. evidence supporting the non-collusive class) function is defined by: $g _ { N N R T } = \left\{ \begin{array} { c c } { 1 - \frac { N N R T } { t h _ { N N R T } ^ { n c } } } & { i f N N R T \le t h _ { N N R T } ^ { n c } } \\ { 0 } & { i f N N R T \lnot t h _ { N N R T } ^ { n c } } \end{array} \right.$ , where $t h _ { N N R T } ^ { n c }$ is the evidence threshold of the feature NNRT and it is estimated based on Algorithm 1.

4.6.1.3. Confirmation interval of transactions (CIT)—implicit. Confirmation interval of a transaction t is defined as the elapsed time $( C T _ { i } - D T _ { i } )$ between a seller declaring the delivery of a commodity DT and the a buyer confirming the receipt of the commodity CT . Some e-Commerce platforms adopt a default interval of ν days, For instance, the Taobao platform assumes that the receipt of a commodity is within 10 days after the actual delivery of the commodity. A longer elapsed time suggests a higher likelihood of a legitimate transaction because collusive buyers would like to confirm the transaction and inflate the seller rating as quickly as possible. The feature of CIT is defined by: $\begin{array} { r } { C { I T } = ( \frac { \nu } { C T _ { i } - D T _ { i } } ) ^ { 2 } } \end{array}$ . Accordingly, the evidence function is defined by: $g _ { C I T } = \left\{ \begin{array} { c c } { 1 - \frac { C I T } { t h _ { C I T } ^ { n c } } } & { i f C I T \le t h _ { C I T } ^ { n c } } \\ { 0 } & { i f C I T > t h _ { C I T } ^ { n c } } \end{array} \right.$ where th<sup>nc</sup> is the evidence threshold of the feature CIT.

4.6.1.4. Rating interval of transactions (RIT)—explicit. Rating interval of a transaction is the elapsed time between a buyer confirming her receipt of a commodity (CT ) and the time the buyer rating the seller (RT ). Compared with the default interval of ρ days generated by a system (e.g., the default interval at Taobao is 15 days), a longer rating interval of a transaction may suggest a higher likelihood of a legitimate transaction. The feature value of RIT is defined by: $\begin{array} { r } { R I T _ { i } = \left( \frac { \rho } { R T _ { i } - C T _ { i } } \right) ^ { 2 } } \end{array}$ . The evidence function $g _ { R I T }$ is similar to that of $g _ { C I T }$ defined before.

4.6.1.5. Average stay time on commodities of transitions (ASTCT)—implicit. Stay time is the duration of a visitor traversing various pages of an e-Shop. In general, the longer a stay time is, the more likely the visitor is genuinely interested in the commodities of the e-Shop. So, it is more likely to be a type of legitimate user behavior. For a transaction

$t _ { i } ,$ the average stay time is quantified by: $\underbrace { \sum _ { k = 1 } ^ { g } S T _ { k } } _ { n _ { t _ { i } } ^ { V } }$ , where $S T _ { k }$ is each stay time pertaining to $t _ { i } , n _ { t _ { i } } ^ { \ V }$ is the number of visits for a commodity related to $t _ { i \cdot }$ The feature ASTCT is the reciprocal of the average stay time. The corresponding evidence function is defined by: $g _ { A S T C T } = \left\{ \begin{array} { c c } { { 1 - \frac { A S T C T } { t h _ { A S T C T } ^ { n c } } } } & { { i f A S T C T \le t h _ { A S T C T } ^ { n c } } } \\ { { 0 } } & { { i f A S T C T > t h _ { A S T C T } ^ { n c } } } \end{array} \right.$ where $t h _ { A S T C T } ^ { n c }$ is the evidence threshold of the feature ASTCT.

4.6.1.6. Average depth of visits of transactions (ADVT)—implicit. Depth of a visit refers to the number of consecutive pages of an e-Shop visited by a user. It is a kind of implicit behavior analysis. Generally speaking, the larger the average depth of visits, the more likely the user is genuinely interested in the commodities of a transaction (i.e., a legitimate transaction). For a transaction $t _ { i } ,$ the average browsing depth is quantified by:

$\frac { \displaystyle \sum _ { k = 1 } ^ { g } D V T _ { k } } { n _ { t _ { i } } ^ { V } } ,$ , where $D V T _ { k }$ is the depth of visits pertaining to $t _ { i } ,$ and ${ n _ { t _ { i } } } ^ { V }$ is the number of visits for the commodities of $t _ { i \cdot }$ The evidence function is similar to that of ASTCT.

4.6.1.7. Returning visitor of transactions (RVT)—implicit. If a user visits an e-Shop the second time, she is considered to be a returning visitor and will be marked in the behavior log as returning. A visitor with a long history of returning is more likely to engage in legitimate transactions. For an e-Commerce platform like Taobao, the returning status of a visitor is available to e-Shops. The feature RVT is defined by $\begin{array} { r } { R V T = \frac { 1 } { N _ { r } } , } \end{array}$ where $N _ { r }$ is the number of returning visits. The evidence function is similar to that of ASTCT.

4.6.1.8. Trade duration of transactions (TDT)—implicit. Trade duration is the elapsed time between a buyer first visiting an e-Shop and the time she actually settling (paying) the transaction. The longer the trade duration is, the higher the operational cost of a transaction will be. So, a collusive buyer tends to settle a transaction quickly to minimize the operational costs of producing fake rating for the seller. Comparing with the average trade duration of transactions in an e-Commerce platform, the credibility of a transaction can be estimated. The way of quantifying TDT is similar to that of ADVT.

## 4.6.2. Features of buyers

Buyer is at a higher level of granularity than transaction according to our hierarchical entity model. For e-Commerce platforms like Taobao, the reputation of a buyer can be observed via the reputation page of a seller. For analyzing the implicit behavior of a buyer, the details of multiple transactions and commodities related to the buyer can be under scrutiny. For example, the buyer's average browsing time for commodities, the total number of pages visited, the average number of pages visited, and should be analyzed.

4.6.2.1. Real name authentication of buyer (RNAB)—explicit. If the identity of a buyer is authenticated by third-party authoritative payment services such PayPal or Alipay, the status of the buyer is more credible. The buyer who is successfully authenticated owns an identity card of a network. S/he can open an e-Shop at platform such as Taobao and build up her reputation profile via payment platform such as Alipay. The evidence function of RNAB is simply defined by:

$g _ { R N A B } = \left\{ { 1 \atop 0 } \right. \overset { i f } { \scriptscriptstyle { R N A B \geq t h _ { R N A B } ^ { n c } } }$ , where $t h _ { R N A B } ^ { n c }$ is an evidence threshold

and RNAB=1 is defined if the buyer is authenticated.

4.6.2.2. Positive rating ratio gained by buyer (PPRGB)—explicit. If there is not any attack to e-Commerce systems, a higher ratio of positive rating obtained by a buyer suggests that she is a more credible (legitimate) buyer. However, positive buyer rating could be fake due to collusive sellers. More specifically, when the PPRGB is extremely large (e.g., 100%), there is a good chance that a collusive buyer works with some collusive sellers. The feature PPRGB is defined by: $\begin{array} { r } { P P R G B = \frac { N _ { p o s } } { N _ { r a t i n g } } } \end{array}$ where $N _ { p o s }$ is the number of positive ratings and $N _ { r a t i n g }$ is the total number of ratings received by a buyer. The evidence function is defined by: $h _ { P P R G B } = \left\{ \begin{array} { c c } { \frac { P P R G B - t h _ { P P R G B } ^ { c } } { P P R G B _ { M A X } - t h _ { P P R G B } ^ { c } } } & { i f P P R G B \ b { z } t h _ { P P R G B } ^ { c } } \\ { 0 } & { e l s e } \end{array} \right.$ , where $t h _ { P P R G B } ^ { c }$ is the evidence threshold of the feature PPRGB, and it is estimated based on Algorithm 1.

4.6.2.3. Positive rating ratio offered by buyer (PRRB)—explicit. If a buyer tends to offer a lot of positive ratings to sellers, she is suspicious. The reason is that a collusive buyer who works with some collusive sellers always inflates sellers' ratings. The evidence function is similar to that of PPRGB.

4.6.2.4. Average confirmation interval of buyer (ACIB)—implicit. Based on the CIT of transactions, the ACIB of a buyer $b _ { i }$ refers to the average confirmation interval of transactions pertaining to a buyer. The average

confirmation interval is defined by: $A C I B _ { i } = \frac { \displaystyle \sum _ { j = 1 } ^ { n } C I T _ { ( i , j ) } } { \displaystyle n _ { b _ { i } } ^ { T } } ,$ , where ${ n _ { b _ { i } } } ^ { T }$ is the number of transactions of $b _ { i }$ and CIT is the confirmation interval of transaction j of $b _ { i \cdot }$ The evidence function is similar to that of CIT.

4.6.2.5. Average rating interval of buyer (ARIB)—explicit. Based on the RIT of transactions, ARIB refers to the average RIT values of transactions pertaining to a buyer $b _ { i \cdot }$ General speaking, the larger value of ARIB is, the more credible the buyer is. Average rating interval is defined by: ARI

$B _ { i } = \frac { \displaystyle \sum _ { j = 1 } ^ { n } R I T _ { ( i , j ) } } { \displaystyle n _ { b _ { i } } ^ { I } } ,$ , where ${ n _ { b _ { i } } } ^ { T }$ is the number of transactions of a buyer $b _ { i \cdot }$ RIT is the rating interval of transaction j pertaining to $b _ { i \cdot }$ The evidence function is similar to that of RIT.

4.6.2.6. Invalid rating ratio of buyer (IRRB)—explicit. Similar to IRT, if a buyer has invalid ratings for some sellers, s/he is very likely to be collusive. IRRB is defined by: $I R R B _ { i } = \frac { n _ { b _ { i } } ^ { I R } } { n _ { b _ { i } } ^ { T } }$ , where ${ n _ { b _ { i } } } ^ { T }$ is the number of transactions pertaining to a buyer b . ${ n _ { b } } _ { i } ^ { I \dot { R } }$ is the number of transactions pertaining to $b _ { i }$ with invalid ratings. The evidence function is similar to that of IRT.

4.6.2.7. Transaction frequency of a buyer (TFDB)—implicit. The daily transaction frequency is an implicit feature of a buyer. For a collusive buyer, she tends to have an extremely high transaction frequency in order to gain financial rewards from the attacks. The evidence function is similar to that of PPRGB

## 5. Experiments and results

## 5.1. Experimental procedure and data set

It is a well-known fact that constructing an evaluation data set is as challenging as designing an effective detection algorithm [55,56]. Accordingly, we adopt the honeypots approach [57] to capture real transactional and behavioral data of various parties by establishing some e-Shops at Taobao, the largest e-Commerce platform in China. Legitimate buyers purchased commodities from three of our e-Shops over a period of two years. We collected the comprehensive behavioral data about these legitimate buyers and the associated legitimate transaction data via the e-Shop management tools provided by Taobao. On the other hand, some of our research team members communicated with several attack agencies and specified the attack tasks against our established e-Shops. The attack agencies then recruited collusive buyers (attackers) to launch fake transactions and provide inflated ratings and comments against our e-Shops. Similarly, the behavioral data of these collusive buyers and the associated fake transaction data were collected by using the e-Shop management tools provided by Taobao. The legitimate buyers, collusive buyers, and the attack agencies knew nothing about our experiments. Since we could not control the arrival sequences of legitimate transactions, fraudulent transactions were mixed up with legitimate transactions in a natural way. Our data set captures the realistic transactional and behavioral patterns of the transacting parties. Table 3 summarizes the details of our evaluation data set. Tables 4 and

Please cite this article as: J. Zhao, et al., Extracting and reasoning about implicit behavioral evidences for detecting fraudulent online transactions in e-Commerce, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.04.003

J. Zhao et al. / Decision Support Systems xxx (2016) xxx–xxx

Table 3  
The details of the evaluation data set.

<table><tr><td>No.</td><td>Data source</td><td>Statistic</td></tr><tr><td>1</td><td>Customized attackers</td><td>561 attacks (produce multiple transactions)</td></tr><tr><td>2</td><td>Transactions</td><td>8885 transactions</td></tr><tr><td>3</td><td>Buyers</td><td>139,864</td></tr><tr><td>4</td><td>Behavior log</td><td>215,844 records</td></tr><tr><td>5</td><td>Period of data collection</td><td>6 months</td></tr></table>

5 depict the sample transactional and behavioral data collected via our e-Shop management tools. Our evaluation data set and the sample source codes of our system are made available via our project Website.<sup>4</sup>

To launch the attacks against our e-Shops, five popular attack agencies were used. The research team members who represented our e-Shops first browsed through the common attack requirements posted to the Websites of these attack agencies. Fig. 5 is a snapshot view of the attack requirements (with our English translations) posted to one of these agencies.<sup>5</sup> Our research team members then manually composed the attack requirements (e.g., specific e-Shop, commodities, transaction amounts, number of positive ratings, etc.) according to the specific format prescribed by the respective attack agencies. Once an attack agency confirmed an attack task, the agency would inform the requester when the attack was expected to take place and by whom (e.g., a user ID of the Taobao platform) the attack would be launched. A total of 561 attack tasks were created and the corresponding fraudulent transactions were identified for our experiments.

To evaluate the performance of the proposed detection framework named DSRC, we evenly divided our evaluation data set into a training set and a test set. Model parameters were estimated based on the training set, and then the established parameters were applied to the test set. The same experimental procedure was then repeated ten times to obtain the average performance data. To test the effectiveness of various components of the proposed framework, we implemented and evaluated different versions of our system as follows. DSRC (I1) refers to a primitive version of the proposed framework that only applies our GA to search for near optimal system parameters for the classical DS reasoning model. On the other hand, DSRC (I1 + I2) refers to the extension of the (I1) version of the proposed framework by using the proposed Algorithm 1 to systematically estimate all evidence thresholds. Finally, DSRC (I1 + I2 + I3) refers to the full version of the proposed framework that utilizes all the proposed computational methods (i.e., Algorithms 1 and 2).

For a comparative system evaluation, our experiments invoked several baseline systems. For instance, the DS(e) baseline system employed the classical DS reasoning model [51] to detect fraudulent entities based on explicit evidences alone. The second baseline system was the Suvasini model [7] that leveraged Bayesian learning and the classical DS model for the fusion and reasoning of positive evidences only. Finally, the DS reasoning model developed by Dong et al. [19] for shilling bids detection in e-Auction was also applied to our experiments. Since we adopted the honeypots approach for experimental data collection, the true labels of testing entities (e.g., transactions and buyers) were obtained. For the first series of experiments, we aimed to evaluate the performance of various systems (i.e., experimental and baseline systems) for the detection of fraudulent transactions. Afterwards, we evaluated the performance of these systems under the setting of fraudulent buyer detection. The method developed by Dong et al. [19] and three different versions of our framework, DSRC (I1), DSRC (I1 + I2), and DSRC (I1 + I2 + I3) utilized exactly the same set of features. If the proposed framework could outperform Dong's method, we can conclude that the performance improvement is brought by the proposed algorithms.

Table 4  
A sample transaction record (English translation).

<table><tr><td>Order status</td><td>Customer name</td><td>Location</td><td>Order creation time</td><td>Payment time</td><td>Commodity name</td></tr><tr><td>Successful</td><td>Zhao Xiaodan</td><td>Beijing</td><td>2014/4/1222:54</td><td>2014/4/1223:01</td><td>Pail bag with monkey pattern</td></tr></table>

## 5.2. The performance evaluation measures

We applied the performance measures that were commonly used to evaluate fraud detection systems to our experiments [55]. Table 6 depicts a confusion matrix that illustrates the basic concepts of these measures. The formal definitions of various performance measures are then given, whereas TPR, FPR, and FNR stand for true positive rate, false positive rate, and false negative rate, respectively. Finally, the lam measure is a weighted combination of the false positive rate and the false negative rate [55]. For all the experiments reported in this paper, we only deal with a two-class classification (reasoning) problem even though the proposed detection framework can distinguish three different class labels (i.e., fraudulent, suspicious, and legitimate).

$$
T P R = \frac {T P}{T P + F N}\tag{9}
$$

$$
F P R = \frac {F P}{F P + T N}\tag{10}
$$

$$
F N R = \frac {F N}{T P + F N}\tag{11}
$$

$$
l a m = \operatorname{logit} ^ {- 1} \left(\frac {\operatorname{logit} (F P R) + \operatorname{logit} (F N R)}{2}\right)\tag{12}
$$

## 5.3. The experiments for fraudulent transaction detection

This series of experiments aimed to evaluate the performance of the proposed framework for fraudulent transaction detection by using the DSRC fusion method to combine both explicit and implicit behavioral evidences extracted from a hierarchy of entities. For the first baseline run, Dong's method that utilized both explicit and implicit evidences was invoked. For the second baseline run, the Suvasini model that only reasoned about positive evidences was invoked. The last baseline run involved the DS(e) model that applied the classical DS reasoning model to explicit features only. For all the baseline systems, reasoning parameters were established manually. More specifically, the parameters α and β were empirically established within the range of [0.6, 0.95] based on a training set for the runs invoking the Dong and the DS(e) systems. For the Suvasini system, we set the probability of fraudulent entities as 0.6 and assumed α = β = 1 as published in [7]. For the experimental runs, two versions of the proposed framework, namely DSRC(I1) and DSRC(I1 + I2 + I3) were invoked. The comparative average performance of various systems is shown in Table 7. By using the performance scores of the best runs, the receiver operating characteristic (ROC) curves [55] of the various systems were plotted in Fig. 6. A curve on the top demonstrates a better system performance.

It shows that the proposed framework, that is. DSRC(I1 + J2 + I3) achieves the highest true positive rate, and the lowest lam score in Table 7. The DSRC(I1 + I2 + I3) system outperforms all the other baseline systems. The compliment of the area under the ROC curve (i.e., 1 − AUC) achieved by the DSRC(I1 + I2 + I3) system is also the smallest. The smallest (1 − AUC) value suggests that the corresponding ROC curve is above those of the other systems as shown in Fig. 6. Table 8 shows paired t-tests based on AUC values; the proposed framework does significantly outperform all the other systems. The DSRC(I1)

Table 5  
Behavioral records collected on the same day of the transaction (English translation).

<table><tr><td>Visit time</td><td>Entrance type</td><td>Commodity name</td><td>Location</td><td>Customer ID</td><td>Returning</td><td>Visit date</td></tr><tr><td>21:57:58</td><td>Taobao search</td><td>Pail bag with monkey pattern</td><td>Beijing</td><td>Customer5</td><td>0</td><td>2014/4/12</td></tr><tr><td>21:31:19</td><td>Taobao search</td><td>Spring flower dress</td><td>Hubei yichang</td><td>Customer4</td><td>0</td><td>2014/4/12</td></tr><tr><td>10:54:17</td><td>Browsing</td><td>14 Spring Lace dress</td><td>Shandong Liaocheng</td><td>Customer3</td><td>0</td><td>2014/4/12</td></tr><tr><td>9:51:09</td><td>Browsing</td><td>All commodities</td><td>Shandong Liaocheng</td><td>Customer3</td><td>1</td><td>2014/4/12</td></tr><tr><td>18:27:10</td><td>Taobao search</td><td>DAZZLE Coat</td><td>Shandong Liaocheng</td><td>Customer3</td><td>0</td><td>2014/4/12</td></tr></table>

![](/api/attachments/D3DK8ST5/fulltext/images/1ba5eaa5bc63f59ff781a09cb99d8e8622cfced9d8d456df2890bfe70f7b2efd.jpg)  
Fig. 5. Attack requirements posted to one attack agency's website.

variant of the proposed framework also outperforms other baseline systems because the proposed GA can search for near optimal parameters to enhance the classical DS reasoning model. The Suvasini model performs very poor in terms of the lam score because its reasoning process is based on positive evidences (i.e. evidences supporting the collusive class) alone. The DS(e) system also performs very poorly in terms of the (1 − AUC) value because it can only utilize explicit evidences to reason about the class label of an entity. The results of this experiment suggest that combining implicit and explicit evidences can significantly boost detection performance.

## 5.4. The experiments for fraudulent buyer detection

Since we employed the honeypots approach to lure collusive buyers to our e-Shops via several attack agencies, we knew the true labels of the buyers who visited our e-Shops. Similar to the experiments related to fraudulent transaction detection, we invoked both the Dong and the Suvasini baseline systems. In addition, to further examine the contributions from each component of the proposed framework, we invoked three different versions of the proposed framework. The comparative performance of all systems is tabulated in Table 9 and the corresponding ROC curves are plotted in Fig. 7.

It is obvious that the proposed framework DSRC(I1 + I2 + I3) achieves the lowest lam score and (1 − AUC) value. The DSRC(I1) system outperforms both the Dong and the Suvasini baseline systems even though all of them adopt the classical DS reasoning model. The main reason is that the proposed GA module can search for near optimal parameters for the DS model to enhance its performance. The DSRC(I1 + I2) system performs better than its DSRC(I1) counterpart in terms of (1 − AUC) value but worse off in terms of the lam score. The reason may be that an effective evidence fusion method that can combine possibly conflicting evidences contributes more to boost detection performance when compared to an automatic feature thresholding method.

Researchers have pointed out that minimizing the false alarms of a fraud detection system is essential for its practical applications [52]. As shown in Table 9, all the variants of the proposed framework produce a much smaller false positive rate when compared to those of the two baseline systems. Finally, we performed paired t-tests between the proposed framework and the other baseline systems. The test results as shown in Table 10 confirm that the proposed framework DSRC(I1 + I2 + I3) significantly outperforms all the baseline systems. The main reason is that the proposed evidence fusion algorithm illustrated in Fig. 4 can effectively combine possibly conflicting evidences to infer the class label of an entity. Therefore, it significantly outperforms the classical DS reasoning model and other baseline methods that assume no conflicts among evidences.

## 6. Conclusions

Despite some studies about detecting shilling attacks were reported in literature, little research work related to fraudulent transaction detection has been done to date. The main contributions of our work include: (1) the development of a DS reasoning-based detection framework that exploits implicit behavior of transacting parties to detect collusive fraudulent transactions; (2) the development of a novel evidence fusion method that can effectively combine possibly conflicting aggregated evidences to infer the fraudulent status of an entity (e.g., a transaction or a buyer); and (3) the development of a genetic algorithm to enhance the classical DS reasoning model by using near optimal model parameters. Our experiments confirm that the proposed detection framework can achieve an average true positive detection rate of 83% while the false alarm rate is reduced to as low as 2.4%. In addition, our paired t-tests show that the proposed framework significantly outperforms other state-of-the-art baseline systems. The managerial implication of our research work is that administrators of e-Commerce platforms can apply our methodology to detect and prevent fraudulent transaction attacks.

## Table 6

A confusion matrix for performance evaluation.

<table><tr><td rowspan="2"></td><td colspan="3">Ground truth</td></tr><tr><td></td><td>Fraudulent</td><td>Legitimate</td></tr><tr><td rowspan="2">System&#x27;s reasoning</td><td>Fraudulent</td><td>True Positive (TP)</td><td>False Positive (FP)</td></tr><tr><td>Legitimate</td><td>False Negative (FN)</td><td>True Negative (TN)</td></tr></table>

Table 7  
Comparative average performance of various systems (transactions).

<table><tr><td>System</td><td>TPR%</td><td>FPR%</td><td>FNR%</td><td>Lam</td><td>1-AUC</td></tr><tr><td>Dong</td><td>11.0714%</td><td>3.3708%</td><td>88.9286%</td><td>52.9335%</td><td>37.1021%</td></tr><tr><td>Suvasini</td><td>12.8205%</td><td>8.3333%</td><td>87.1795%</td><td>78.6245%</td><td>37.1448%</td></tr><tr><td>DS(e)</td><td>54.1502%</td><td>36.1404%</td><td>45.8498%</td><td>69.2232%</td><td>42.0607%</td></tr><tr><td>DSRC(I1)</td><td>15.8845%</td><td>2.8522%</td><td>84.1155%</td><td>39.4299%</td><td>27.1911%</td></tr><tr><td>DSRC(I1 + I2 + I3)</td><td>83.0000%</td><td>2.4024%</td><td>17.0000%</td><td>7.1005%</td><td>13.0919%</td></tr></table>

Please cite this article as: J. Zhao, et al., Extracting and reasoning about implicit behavioral evidences for detecting fraudulent online transactions in e-Commerce, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.04.003

![](/api/attachments/D3DK8ST5/fulltext/images/48248c28f7d53000469cefadf2a83497f55e423070688c769396a3ac67e6a56f.jpg)  
Fig. 6. Comparative ROC curves for detecting fraudulent transactions

![](/api/attachments/D3DK8ST5/fulltext/images/d32b56e1b57b7bca10487e9f115ccf4594f4eaf3052ae81a6635fcd87f9cfbf2.jpg)  
Fig. 7. Comparative ROC curves for detecting fraudulent buyers.

Table 8  
Paired T-test based on AUC (transaction detection)

<table><tr><td>Comparison</td><td>t Statistics</td><td>p Value</td></tr><tr><td>DSRC(I1 + I2 + I3) vs. Dong</td><td>36.01062</td><td>0.000</td></tr><tr><td>DSRC(I1 + I2 + I3) vs. RS(e)</td><td>42.42609</td><td>0.000</td></tr><tr><td>DSRC(I1 + I2 + I3) vs. Suvasini</td><td>14.52176</td><td>0.000</td></tr><tr><td>DSRC(I1 + I2 + I3) vs. DSRC(I1)</td><td>10.96769</td><td>0.000</td></tr></table>

As a result, fair electronic trading among businesses or individuals is maintained in the ever expanding e-Commerce world.

There are some limitations of our research work. First, fraudsters' attack strategies and attack patterns may change over time. Accordingly, a learning and adaptation component to learn the evolving attack features is needed. Second, we only performed experiments that evaluated the detection tasks involving two classes (e.g., fraudulent versus legitimate) due to the lack of ground-truth for the “suspicious” class. Third, the proposed framework has been tested under the setting of detecting fraudulent transactions in e-Commerce. Although we believe that the same framework and its constituting algorithms for evidence threshold calibration and aggregated evidence fusion can be readily applied to other settings such as detecting fraudulent online financial transactions, more empirical tests under other business settings should be conducted to enhance the external validity of our study. Further research work will also collect more transactional and behavioral data via our honeypots approach to evaluate the effectiveness of our framework on detecting different kinds of entities involving more than two classes.

Comparative average performance of various systems (buyers).

<table><tr><td>Method</td><td>TPR%</td><td>FPR%</td><td>FNR%</td><td>Lam%</td><td>(1-AUC)%</td></tr><tr><td>Dong</td><td>98.2227%</td><td>71.0938%</td><td>1.7773%</td><td>21.0954%</td><td>29.9198%</td></tr><tr><td>Suvasini</td><td>87.1921%</td><td>56.1404%</td><td>12.8079%</td><td>43.3616%</td><td>44.6156%</td></tr><tr><td>DSRC(I1)</td><td>76.1194%</td><td>3.8941%</td><td>23.8806%</td><td>11.2746%</td><td>21.7564%</td></tr><tr><td>DSRC(I1 + I2)</td><td>48.2877%</td><td>3.4148%</td><td>51.7123%</td><td>19.4583%</td><td>19.6782%</td></tr><tr><td>DSRC(I1 + I2 + I3)</td><td>40.7975%</td><td>0.3561%</td><td>59.2025%</td><td>9.0611%</td><td>15.8001%</td></tr></table>

Table 10  
Paired t-test based on AUC (buyer detection).

<table><tr><td>Comparison</td><td>t Statistic</td><td>p Value</td></tr><tr><td>DSRC(I1) vs. Dong</td><td>9.832</td><td>0.000</td></tr><tr><td>DSRC(I1 + I2) vs. Dong</td><td>11.35</td><td>0.000</td></tr><tr><td>DSRC(I1 + I2 + I3) vs. Dong</td><td>12.42</td><td>0.000</td></tr><tr><td>DSRC(I1) vs. Suvasini</td><td>44.44</td><td>0.000</td></tr><tr><td>DSRC(I1 + I2) vs. Suvasini</td><td>40.871</td><td>0.000</td></tr><tr><td>DSRC(I1 + I2 + I3) vs. Suvasini</td><td>47.118</td><td>0.000</td></tr><tr><td>DSRC(I1 + I2) vs. DSRC(I1)</td><td>4.287</td><td>0.002</td></tr><tr><td>DSRC(I1 + I2 + I3) vs. DSRC(I1 + I2)</td><td>6.803</td><td>0.000</td></tr></table>

## Acknowledgements

This research work was supported by the National Natural Science Foundation of China under Grant No. 71401045, 71571052. Lau's work was supported by grants from the Research Grants Council of the Hong Kong Special Administrative Region, China (Projects: CityU 145712 and 11502115), and the Shenzhen Municipal Science and Technology R&D Funding—Basic Research Program (Project No. JCYJ20140419115614350).

## References

[1] Z. Chen, J. Yang, Credit fraud control and credit system optimization on C2C marketplaces, Proceedings of the 42nd Hawaii International Conference on System Sciences 2009

[3] Y. Zhang, J. Bian, W. Zhu, Trust fraud: a crucial challenge for China's e-commerce market, Electronic Commerce Research and Applications 12 (5) (2012) 299–308.

[5] W. You, L. Liu, M. Xia, Reputation inflation detection in a Chinese C2C market, Electronic Commerce Research and Applications 10 (5) (2011) 510–519.

[7]. S. Panigrahi A. Kundu S. Sural A.K. Majumdar Credit card fraud detection: a fusion approach using Dempster-Shafer theory and Bavesian learning, Information Fusion 10 (4) (2009)354-363

[8] D. Chau, S. Pandit, C. Faloutsos, Detecting fraudulent personalities in networks of online auctioneers Proceedings of the 10th European Conference on Principles and Practice of Knowledge Discovery in Databases 2006, pp. 103–114.

[9] K. Hoffman, D. Zage, C. Nita-Rotaru, A survey of attack and defense techniques for reputation systems, ACM Computing Surveys 42 (1) (2009) 1–19.

[11] H. Xu, Y.T. Cheng, Model checking bidding behaviors in Internet concurrent auctions, International Journal of Computer Systems Science & Engineering 22 (4) (2007) 179–191.

Please cite this article as: J. Zhao, et al., Extracting and reasoning about implicit behavioral evidences for detecting fraudulent online transactions in e-Commerce, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.04.003

[12] W.H. Chang, J.S. Chang, A novel two-stage phased modeling framework for early fraud detection in online auctions, Expert Systems with Applications 38 (9) (2011) 11244–11260.

[13] P.L. Conti, M. Naldi, Detection of anomalous bids in procurement auctions, Decision Support Systems 46 (1) (2008) 420–428.

[14] C. Chiu, Y. Ku, T. Lie, Y. Chen, Internet auction fraud detection using social network analysis and classification tree approaches, International Journal of Electronic Commerce 15 (3) (2011) 123–147.

[15] Z.B. Gan, C. Zeng, K. Li, et al., Constructions and optimization of trust network in E-commerce environment, Chinese Journal Computers 35 (1) (2012) 27–37.

[16] Z. Banković, J. Vallejo, D. Fraga, J. Moya, Detecting bad-mouthing attacks on reputation systems using self-organizing maps, Computational Intelligence in Security for Information Systems (2011) 9–16.

[17] L.C. Keung, S. Niukyun, Trust-based Social Mechanism to Counter Deceptive Behavior, University of Warwick, 2011.

[18] C. Dellarocas, Immunizing online reputation reporting systems against unfair ratings and discriminatory behavior. Proceedings of the 2nd ACM conference on Electronic commerce 2000, pp. 150–157.

[19] F. Dong, S.M. Shatz, H. Xu, Reasoning under uncertainty for shill detection in online auctions using Dempster–Shafer theory, International Journal of Software Engineering and Knowledge Engineering 20 (07) (2010) 943–973.

[20] E.W.T. Ngai, Y. Hu, Y.H. Wong, Y. Chen, X. Sun, The application of data mining techniques in financial fraud detection: a classification framework and an academic review of literature, Decision Support Systems 50 (3) (2011) 559–569.

[21] M. Chae, S. Shim, H. Cho, B. Lee, An empirical analysis of fraud detection in online auctions: credit card phantom transaction, Proceedings of 40th Annual Hawaii International Conference on System Sciences(HICSS'07) 2007, p. 155.

[22] S. Tsang, Y.S. Koh, G. Dobbie, S. Alam, Detecting online auction shilling frauds using supervised learning, Expert Systems with Applications 41 (6) (2014) 3027–3040.

[23] R.J. Kauffman, C.A. Wood, Running up the bid: detecting, predicting, and preventing reserve price shilling in online auctions, Proceedings of the 5th international conference on Electronic commerce 2003, pp. 259–265.

[24] H. Xu, C.K. Bates, S.M. Shatz, Real-time model checking for shill detection in live online auctions, Proceedings of the 2009 International Conference on Software Engineering Research and Practice (SERP'09) 2009, pp. 134–140.

[25] Y.F. Yang, Q.Y. Feng, Y. Sun, Y.F. Dai, Dishonest behaviors in online rating systems: cyber competition, attack models, and attack generator, Journal of Computer Science and Technology 24 (5) (2009) 855–867.

[26] Y.C. Zhu, L. Liu, W. Zhang, Study of trust model in online reputation system, Control and Decision 22 (4) (2007) 413–417.

[27] R.X. Li, C. Gao, X.W. Gu, et al., Research on credit counting and risk evaluation for C2C e-commerce, Journal on Communications 007 (2009) 78–85

[28] S.D. Kamvar, M.T. Schlosser, H. Garcia-Molina, The eigentrust algorithm for reputation management in p2p networks, Proceedings of the 12th International Conference on World Wide Web 2003, pp. 640–651.

[29] W. Nejdl, D. Olmedilla, M. Winslett, Peertrust: automated trust negotiation for peer on the semantic web, Secure Data Management (2004) 159–182

[30] G. Zacharia, A. Moukas, P. Maes, Collaborative reputation mechanisms for electronic marketplaces, Decision Support Systems 29 (4) (2000) 371–388.

[31] H.H. Guo, J.H. Jiang, H. Ca, Modeling for reputation computing in C2C communities, Chinese Journal of Management 6 (8) (2009) 1056–1060

[32] P.K. Chan, A non-invasive learning approach to building web user profiles. 1999

[33] J.X. Cao, Y.C. Liu, R.W. Cen, et al., Pornography web site identi cation based on user behavior analysis, Journal of Computer Research and Development 50 (2) (2013) 430–436.

[34] R. Maranzato, M. Neubert, A.M. Pereira, A.P. Do Lago, Feature extraction for fraud detection in electronic marketplaces, Proc of the Web Congress, 2009. LA-WEB'09. Latin American 2009, pp. 185–192.

[35] R. Maranzato, A. Pereira, M. Neubert, A.P. Do Lago, Fraud detection in reputation systems in e-markets using logistic regression and stepwise optimization, ACM SIGAPP Applied Computing Review 11 (1) (2010) 14–26.

[36] J. Zhao, N.F. Xiao, J.R. Zhong, Behavior trust control based on bayesian networks and user behavior log mining, Journal of South China University of Technology (Natura Science Edition) 37 (5) (2009) 94–100.

[37] J. Zhao, N.F. Xiao, J.R. Zhong, Application of web usage mining in trust management, Computer Engineering 35 (24) (2009)

[38] W. Chang, J. Chang, Using clustering techniques to analyze fraudulent behavior changes in online auctions, Proceedings of the 1th Networking and Information Technology (ICNIT) 2010, pp. 34–38.

[39] V. Almendra, Finding the needle: a risk-based ranking of product listings at online auction sites for non-delivery fraud prediction, Expert Systems with Applications 40 (12) (2013) 4805–4811.

[40] J. Trevathan, W. Read, Detecting collusive shill bidding, Proceedings of the 4th Information Technology Conference (ITNG'07) 2007, pp. 799–808

[41] S. Pandit, D.H. Chau, S. Wang, C. Faloutsos, Netprobe: a fast and scalable system for fraud detection in online auction networks, Proceedings of the 16th International Conference on World Wide Web 2007 pp 201–210

[42] G.K. Palshikar, M.M. Apte, Collusion set detection using graph clustering, Data Mining and Knowledge Discovery 16 (2) (2008) 135–164.

[43] B. Mobasher, R. Burke, R. Bhaumik, C. Williams, Effective attack models for shilling item-based collaborative filtering systems Proceedings of the 2005 WebKDD Workshop held in coniunction with ACM SIGKDD'2005 2005 p. 13.

[44] R. Burke, B. Mobasher, C. Williams, R. Bhaumik, Classification features for attack detection in collaborative recommender systems Proceedings of the 12th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining 2006, pp. 542–547.

[45] H. Mizuta, K. Steiglitz, Agent-based simulation of dynamic online auctions, Proceedings of the Simulation Conference, vol. 2 2000, pp. 1772–1777.

[46] W. Li, A. Joshi, Outlier detection in ad hoc networks using Dempster–Shafer theory, Proceedings of the Mobile Data Management: Systems, Proceedings of 10th International Conference on Mobile Data Management(MDM'09) 2009, pp. 112–121.

[47] L.Q. Tian, C. Lin, A kind of game-theoretic control mechanism of user behavior trust, Chinese Journal of Computers 30 (11) (2007) 1930–1938.

[48] S. Tsang, G. Dobbie, Y.S. Koh, Generating realistic online auction data, AI 2012: Advances in Artificial Intelligence 2012, pp. 120–131.

[49] S. Tsang, G. Dobbie, Y.S. Koh, Evaluating fraud detection algorithms using an auction data generator, Proceedings of 2012 IEEE 12th International Conference on Data Mining Workshops (ICDMW 2012) 2012, pp. 332–339.

[50] C.Q. Tian, S.H. Zou, W.D. Wang, A new trust model based on recommendation evidence for P2P networks, Chinese Journal of Computers 31 (2) (2008).

[51] W.L. Li, K.H. Guo, Combination rules of D–S evidence theory and conflict Problem, Systems Engineering—Theory & Practice 008 (2010) 1422–1432.

[52] S. Axelsson, The base-rate fallacy and the difficulty of intrusion detection, ACM Transactions on Information and System Security 3 (3) (2000) 186–205

[53] X. Yan, R.Y.K. Lau, D. Song, X. Li, J. Ma, Towards a semantic granularity model for domain-specific information retrieval, ACM Transactions on Information Systems 29 (3) (2011) (article 15).

[54] R.Y.K. Lau, M. Tang, O. Wong, S. Milliner, Y. Chen, An evolutionary learning approach for adaptive negotiation agents, International Journal of Intelligent Systems 21 (1) (2006) 41–72.

[55] R.Y.K, Lau, S.Y, Liao, R.C.W, Kwok, K.O. Xu. Y. Xia. Y. Li, Text mining and probabilistic language modeling for online review spam detection, ACM Transactions on Management Information Systems 2 (4) (2011) (article 25).

[56] A. Mukherjee, A. Kumar, B. Liu, J. Wang, M. Hsu, M. Castellanos, R. Ghosh, Spotting opinion spammers using behavioral footprints, Proceedings of the 19th ACM SIGKDD Conference on Knowledge Discovery and Data Mining 2013, pp. 632–640.

[57] K. Lee, J. Caverlee, S. Webb, Uncovering social spammers: social honeypots + machine learning, Proceedings of the 33rd International ACM SIGIR Conference on Research and Development in Information Retrieval 2010, pp. 435–442.

[58] I. Gunes, C. Kaleli, A. Bilge, H. Polat, Shilling attacks against recommender systems: a comprehensive survey, Artificial Intelligence Review 42 (4) (2014) 767–799.

![](/api/attachments/D3DK8ST5/fulltext/images/13b941af2a8c6c47b09874fc0b50e0823ac35fc2d0747bb9ea8d7b3907c48da6.jpg)  
Raymond Y. K. Lau is an Associate Professor in the Department of Information Systems at City University of Hong Kong. He is the author of over 150 refereed international journals and conference papers. His research work has been published in renowned journals such as MIS Quarterly, INFORMS Journal on Computing, ACM Transactions on Information Systems, IEEE Transactions on Knowledge and Data Engineering, IEEE Internet Computing, Journal of MIS, Decision Support Systems, etc. His research interests include Big Data Stream Analytics, Social Media Analytics, Information Retrieval, and Agent-Mediated e-Commerce. He is a senior member of the IEEE and the ACM, respectively.

![](/api/attachments/D3DK8ST5/fulltext/images/900f03dbff7565cb09005a2779e74e537aa9a0cf2b67cb7564e6780b1a8affab.jpg)

Jie Zhao is an associate professor at Guangdong University of Technology. She received her Ph.D. in Computer Science from South China University of Technology in 2010. Her main research interests include data mining, business intelligence, machine learning, and information fusion.

Wenping Zhang is a post-doc researcher at the College of Business of City University of Hong Kong. He holds a Ph.D. in Information Systems from City University of Hong Kong. His research work has been published in renowned journals such as INFORMS Journal on Computing, IEEE Intelligent Systems, etc. His research interests include Big Data Analytics, Social Media Analytics and e-Commerce.

Keihang Zhang graduated from Guangdong University of Technology in 2015. He is a Master degree candidate of Institute of Information Engineering in Chinese Academy of Sciences right now. His main research interests include data mining and information safety technologies.

Xu Chen graduated from Zhengzhou University in 2011. He is a Master degree candidate in Guangdong university of Technology now. His research topics are related to information fusion and reasoning with uncertainty.

Deyu Tang is a lecturer at Guangdong Pharmaceutical University. He received his Ph.D. in Computer Science from South China University of Technology in 2015. His main research interests include machine learning and evolutionary algorithms

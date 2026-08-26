---
otero_id: 7576
otero_key: "WGD795DY"
title: "Maximizing customer satisfaction through an online recommendation system: A novel associative classification model"
authors: "Yuanchun Jiang; Jennifer Shang; Yezheng Liu"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.06.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Maximizing customer satisfaction through an online recommendation system: A novel associative classi<sup>fi</sup>cation model

Yuanchun Jiang <sup>a,b,</sup>⁎, Jennifer Shang <sup>b</sup>, Yezheng Liu <sup>a,c</sup>

<sup>a</sup> School of Management, Hefei University of Technology, Hefei, Anhui 230009, China

<sup>b</sup> The Joseph M. Katz Graduate School of Business, University of Pittsburgh, Pittsburgh, PA 15260, USA

<sup>c</sup> Key Laboratory of Process Optimization and Intelligent Decision Making, Ministry of Education, Hefei, Anhui 230009, China

## a r t i c l e i n f o

Available online 17 June 2009

Keywords: Online recommendation Customer satisfaction Associative classificatior Rating classi<sup>fi</sup>cation

## a b s t r a c t

Offering online personalized recommendation services helps improve customer satisfaction. Conventionally, a recommendation system is considered as a success if clients purchase the recommended products. However, the act of purchasing itself does not guarantee satisfaction and a truly successful recommendation system should be one that maximizes the customer's after-use grati<sup>fi</sup>cation. By employing an innovative associative classi<sup>fi</sup>cation method, we are able to predict a customer's ultimate pleasure. Based on customer's characteristics, a product will be recommended to the potential buyer if our model predicts his/her satisfaction level will be high. The feasibility of the proposed recommendation system is validated through laptop Inspiron 1525.

© 2009 Elsevier B.V. All rights reserved

## 1. Introduction

Personalization of product information has become one of the most important factors that impact a customer's product selection and satisfaction in today's competitive and challenging market. Personalized service requires <sup>fi</sup>rms to understand customers and offer goods or services that meet their needs. Successful <sup>fi</sup>rms are those that provide the right products to the right customers at the right time and for the right price.

As a type of information technology aimed to support personalized service, recommendation systems are widely used by e-commerce practitioners and have become an important research topic in information sciences and decision support systems [25]. Recommendation systems are decision aids that analyze customer's prior online behavior and present information on products to match customer's preferences. Through analyzing the patron's purchase history or communicating with them, recommendation systems employ quantitative and qualitative methods to discover the products that best suit the customer. Most of the current recommendation systems recommend products that have a high probability of being purchased [3]. They employ content-based <sup>fi</sup>ltering (CBF) [41], collaborative <sup>fi</sup>ltering (CF) [18], and other data mining techniques, for example, decision tree [12], association rule [38], and semantic approach [25]. Other literature focuses on the in<sup>fl</sup>uence of recommendation systems on customer's purchase behavior [3,32]. They argue that the recommendation decision should be based not on purchase probability, but rather on the sensitivity of purchase probability due to the recommendation action. Common wisdom regards a recommendation system as successful if customers end up purchasing the suggested product(s). However, buying a product does not necessarily imply the client is pleased with the product. Let's consider a scenario below.

James is in need of a laptop computer. He visits online stores to look for information and compare prices and performance of various laptops. Between the two laptop series, Inspiron 1525 and Aspire 5735, James is uncertain which one would best <sup>fi</sup>t his needs. He decides to turn to the recommendation system for help. After gaining knowledge of James's needs and personal pro<sup>fi</sup>le, the system recommends the Inspiron 1525. Once James follows the advice and makes his purchase, the recommendation system deems that it did a great job because James bought the laptop it recommended. However, after 1week's use of the laptop, James writes a review as follows: “…a good product, but not the one I really want.” It turns out James is not content with the recommendation. This exempli<sup>fi</sup>es the case that a customer may have purchased the recommended product(s), but the recommendation system was not successful in pleasing the customer—its ultimate goal. It is therefore clear that a customer's acceptance of a recommendation is not equivalent to its success. A recommendation system must endure the test of time. Only when customers claim that the products are what they like after their practical usage can one claim that the system has made effective recommendations. This requires not only matching customers' needs, but also satisfying customers' wants. In other words, the recommendation system should only recommend a product if its satisfaction rating is predicted to be high.

How can a customer's satisfaction of a speci<sup>fi</sup>c product be measured and attained? The rapid development of e-commerce affords us an opportunity to predict customers' reactions after they use a product. Many online stores, such as Amazon.com and Dell.com encourage customers to write online reviews on their websites; information from these reviews is then often used to support a <sup>fi</sup>rm's product strategy and customer relationship management [11,13]. In the online reviews, customers can discuss their needs, preferences, personal pro<sup>fi</sup>le, and voice their opinions about a product as poor, average, or good. From such need-rating data, it is easy to obtain personalized information and customers' after-use satisfaction level of the product. Using personal information and responses, the online store can more accurately predict customers' true sentiments toward a speci<sup>fi</sup>c product, and recommend a more suitable product for the potential customer to enjoy.

![](/api/attachments/WGD795DY/fulltext/images/cc85bbb04f384d89c535767192c67116cf3935187bf6cd2fe3d04fa87f26fc49.jpg)  
Fig. 1. Differences between the existing recommendation systems and the proposed model.

This research proposes a rating classi<sup>fi</sup>cation model to estimate a potential customer's satisfaction level. It builds a rating classi<sup>fi</sup>er for a product by discovering rules from the need-rating database collected for the product. The rules imply the co-relationship between customers' needs, preferences, demographic pro<sup>fi</sup>le, and their ratings for the product. For a new customer with speci<sup>fi</sup>c characteristics, the classi<sup>fi</sup>er will predict his/her response toward the recommended product and categorize it into certain class labels, such as poor, average and good. The predicted ratings estimate the customer's satisfaction level for the product. Differences between the existing recommendation systems and the proposed one are illustrated in Fig. 1.

This research proposes a novel associative classi<sup>fi</sup>cation model, which <sup>fi</sup>rst mines multi-class classi<sup>fi</sup>cation information from need-rating data, then constructs a rating classi<sup>fi</sup>er, and <sup>fi</sup>nally predicts customers' ratings for products. We organize the rest of the paper as follows. In Section 2 we review the literature of recommendation systems and associative classi<sup>fi</sup>cation models. Section 3 proposes the innovative methodology to address the rating classi<sup>fi</sup>cationproblem. A case study used to illustrate the effectiveness of the proposed model is given in Section 4. Section 3 comprises the Summary, conclusions, and future research.

## 2. Literature review

The literature review focuses on two perspectives: the recommendation system and associative classi<sup>fi</sup>cation. A summary of relative research methods are given in Table 1 and explained in detail below.

## 2.1. Recommendation systems

Since the development of the <sup>fi</sup>rst recommendation system by Goldberg and colleagues [17], various recommendation systems and related technologies such as CBF and CF [18,41] have been reported. Among them, the user-based collaborative <sup>fi</sup>ltering (CF) [23] is successfully adopted by Amazon.com and Dell.com. It <sup>fi</sup>nds a similar user group for the target buyer and recommends products that have been rated by users in the reference group but not yet viewed by the target buyer. However, the user-based CF has some limitations. One is its dif<sup>fi</sup>culty in measuring the similarities between users, and the other is the scalability issue. As the number of customers and products increases, the computation time of algorithms grows exponentially [21]. The item-based CF [16] was proposed to overcome the scalability problem as it calculates item similarities in an of<sup>fl</sup>ine basis. It assumes that a user will be more likely to purchase items that are similar or related to the items that he/she has already purchased.

Summary of research methods on recommendation system and associative classi<sup>fi</sup>cation.

<table><tr><td colspan="4">(a) Motivation and objectives of various recommendation systems</td></tr><tr><td>Literature</td><td colspan="2">Motivation</td><td>Objective</td></tr><tr><td>[2,10,16,17,20,21,23,41]</td><td colspan="2">Which products meet the customer&#x27;s preferences best?</td><td>Recommend products with high probability.</td></tr><tr><td>[3,32]</td><td colspan="2">What is the influence of recommendation systems on customer&#x27;s purchase behavior?</td><td>Recommend products which are receptive to the recommendation.</td></tr><tr><td>This paper</td><td colspan="2">Which products can achieve a high after-use satisfaction level?</td><td>Recommend products with high after-use satisfaction level.</td></tr><tr><td colspan="4">(b) Comparing associative classification models</td></tr><tr><td>Literature</td><td>Mine multi-class rules</td><td>Classify using multiple rules</td><td>Provide classification reasons</td></tr><tr><td>[26,31,36,37]</td><td>√</td><td></td><td></td></tr><tr><td>[24]</td><td></td><td>√</td><td></td></tr><tr><td>[27] and this paper</td><td>√</td><td>√</td><td>√</td></tr></table>

The content-based <sup>fi</sup>ltering (CBF) method applies content analysis to target items. Target items are described by their attributes, such as color, shape, and material. The user's pro<sup>fi</sup>le is constructed by analyzing his/her responses to questionnaires, his/her rating of products, and navigation history. The recommendation system proposes items that have high correlations with a user's pro<sup>fi</sup>le. However, a pure CBF system also has its shortcomings. One is that users can only receive recommendations similar to their earlier experiences. The other is that some items, such as music, photographs, and multimedia, are hard to analyze [10]. Based on CF and CBF, new data mining techniques employing decision tree, association rule, regression model, and Markov chain have been introduced to recommend movies and books [2], support one-to-one online marketing [21], and attract customers for the tourism industry [20].

Unlike those recommending products based on likelihood of purchase, Bodapati [3] argued that the recommendation decision should also examine a customer's sensitivity to such a recommendation. He built a model to measure the role of recommendation systems in modifying customers' purchase behavior relative to what the customers would have done without such recommendation interventions. Although the extant recommendation systems may recommend acceptable products to customers, they share a common view that the act of purchase itself equates to the customers' satisfaction, which could be far from the truth, as evidenced by James' example earlier.

## 2.2. Associative classification and the combination strategy for multi class classification

Classi<sup>fi</sup>cation is an important management task. Many methods such as the agent-based approach [34], decision tree [30], and data envelopment analysis (developed by professor Cooper [14]) have been proposed to solve the decision analysis problems in various <sup>fi</sup>elds. Associative classi<sup>fi</sup>cation is a relatively new classi<sup>fi</sup>cation method whose aim is to apply the Apriori algorithm [1] to mine association rules and construct associative classi<sup>fi</sup>ers [26]. Rule mining will <sup>fi</sup>nd the associations between attributes (rule preconditions) and ratings (results). In associative classification, the support degree is defined as the ratio of the number of objects satisfying a speci<sup>fi</sup>c rule precondition and having a speci<sup>fi</sup>c rating result over the total number of objects in the database. The con<sup>fi</sup>dence degree is similar to the support degree except that the number of all objects satisfying the speci<sup>fi</sup>c rule precondition is used as the denominator. The discovered rules are pruned to attain a minimal rule set necessary to cover training data and achieve suf<sup>fi</sup>cient accuracy [37]. Although associative classi<sup>fi</sup>cation methods may derive more accurate classi<sup>fi</sup>cation results than other methods, they have a few drawbacks [27]. First is related to multi-class classi<sup>fi</sup>cation: The associative classi<sup>fi</sup>cation methods available today do not have enough multi-class information to build multi-class classi<sup>fi</sup>ers because all con<sup>fl</sup>icting rules are removed [31]. For example, $P _ { 1 }  c _ { 1 }$ and $P _ { 1 }  c _ { 2 }$ are two con<sup>fl</sup>icting rules having the same precondition $P _ { 1 }$ but different classi<sup>fi</sup>cations, $c _ { 1 }$ and $c _ { 2 } ,$ with con<sup>fi</sup>dence degrees of 51% and 49%, respectively. Traditional associative classi<sup>fi</sup>cation methods will delete rule $P _ { 1 } \to c _ { 2 }$ because its con<sup>fi</sup>dence level is lower than that of $P _ { 1 }  c _ { 1 } .$ When con<sup>fl</sup>icts occur, only the rule with the highest con<sup>fi</sup>dence level is retained; the competing rules having lower probabilities are all removed. Another <sup>fl</sup>aw is that they cannot easily identify an optimal rule when classifying a new case [24]. An optimal rule is the one that maximizes the measure, such as the support degree, con<sup>fi</sup>dence degree, or interesting degree as de<sup>fi</sup>ned by the user. The dif<sup>fi</sup>culty with the traditional methods is that different measures may result in different optimal rules.

To overcome the above weakness, Liu and his colleagues [27] have proposed a combination strategy for multi-class classi<sup>fi</sup>cation (CSMC). CSMC retains most of the con<sup>fl</sup>icting rules and employs multiple association rules to construct classi<sup>fi</sup>ers for new cases. After acquiring con<sup>fl</sup>icting rules and calculating their weights, the evidential reasoning approach proposed by Yang and colleagues [40] is employed to combine the classi<sup>fi</sup>cation results of distinct rules. CSMC is useful since it applies multiple rules—especially con<sup>fl</sup>icting ones—to multi-class classi<sup>fi</sup>cation. However, it has de<sup>fi</sup>ciencies as well. That is, even though CSMC retains multi-class information in the process of rule acquisition, much of it is lost in rule pruning. Consequently, the evidence bodies used in the rating classi<sup>fi</sup>cation are often inaccurate and classi<sup>fi</sup>cation results suffer. Moreover, CSMC employs a rough set method to derive evidence weights. Although using evidence weights may signi<sup>fi</sup>cantly improve classi<sup>fi</sup>cation accuracy, its computation is very time-consuming and negatively affects the ef<sup>fi</sup>ciency of classi<sup>fi</sup>cation.

In this research, we propose a new algorithm to address the rating classi<sup>fi</sup>cation problem. Compared with CSMC, the proposed algorithm can preserve most of the useful multi-class information after pruning and it can derive attribute weights much more ef<sup>fi</sup>ciently. Details of our algorithm are discussed next.

## 3. The proposed methodology

## 3.1. The solution framework

To construct an ef<sup>fi</sup>cient and powerful rating classi<sup>fi</sup>er for a speci<sup>fi</sup>c product, we follow three phases as outlined in Fig. 2. The <sup>fi</sup>rst phase is to mine need-rating rules, where retaining multi-class information is the main task. Since con<sup>fl</sup>icts and ambiguities are often present in the need-rating database, the rules discovered must be able to deal with contradictory facts and uncertainties, and to arrive at multi-class information. The second phase calculates the weight for each rule. A weight measures the importance of a need-rating rule in the rating classi<sup>fi</sup>cation problem. In this phase, computational ef<sup>fi</sup>ciency is crucial, due to the presence of various rules useful for classi<sup>fi</sup>er construction. The last phase is to develop the rating classi<sup>fi</sup>er, whose goal is to recommend products that yield high customer satisfaction. In this phase, all factors having in<sup>fl</sup>uences on the potential customers' satisfaction levels are considered. Since customers of the same need may voice very different opinions for the same product, it is important to make multiclass ratings available. Predicting after-use ratings along with corresponding likelihoods provides potential customers a valuable purchase guideline, which signi<sup>fi</sup>cantly enhances the odds of customer satisfaction.

Although traditional associative classi<sup>fi</sup>cation methods could generate reasonable classi<sup>fi</sup>cation results, they suffer from three weak points when classifying customers' ratings. First, they do not accommodate con<sup>fl</sup>icting ratings. Customers of the same needs and preferences may have very different opinions (ratings) for the same product. As discussed in Section 3, traditional associative classi<sup>fi</sup>cation methods resolve the situation by retaining only the rule that has the highest con<sup>fi</sup>dence level. As a result, not enough multi-class information is preserved to deal with the con<sup>fl</sup>ict nature. The second weakness is the prediction tactic. To predict accurately, a classi<sup>fi</sup>er needs to consider a customer's needs, preferences, and demographics. However, traditional prediction relies only on one optimal rule, which is not enough to attain accurate classi<sup>fi</sup>cation. Thirdly, traditional methods classify each case without explanations, that is, they simply list the applicable rule. Such classi<sup>fi</sup>cation is somewhat arbitrary, ambiguous, and irrational. Since customers of the same need may give different ratings to the same product, a classi<sup>fi</sup>cation method must be capable of predicting the probabilities of attaining different customer ratings. The proposed classi<sup>fi</sup>cation algorithm aims to overcome the above de<sup>fi</sup>ciency. Details are described next.

## 3.2. Mine need-rating rules

The need-rating data is <sup>fi</sup>rst organized into a data table $I { = } ( 0 , A \cup C )$ where O is the set of objects (customers), |O| is the number of customers in I. A is the set of attributes, $A { = } \{ A _ { 1 } { , } . . . , A _ { h } { , } . . . , A _ { | A | } \} ,$ |A| is the number of attributes in $A ,$ each $A _ { h } , h = 1 , 2 , . . . , | A | ,$ , is a factor/criterion or a customer characteristic. C corresponds to a set of class labels, $C = \{ c _ { 1 } , . . . , c _ { g } , . . . , c _ { | C | } \} , | C |$ is the number of classes in I, each $c _ { g } , g { = } 1 , 2 , . . . , | C |$ , denotes a rating grade.

![](/api/attachments/WGD795DY/fulltext/images/3dba6e8dec44dafe708df24ab7abdd02aab15f193fd2ebd8133111f5a1b3c87f.jpg)  
Fig. 2. The proposed rating classi<sup>fi</sup>cation framework

In data table I, customers are described by customer characteristics, preferences, and ratings for the product. For example, a middle-aged customer who prefers a laptop with average central processing unit (CPU) speed, good battery life, and rates the laptop Inspiron 1525 as a good product can be described as follows:

$$
\left(^ {\prime} \text {Age} = \text {Middle} ^ {\prime} \wedge^ {\prime} \text {CPU} = \text {Average} ^ {\prime} \wedge^ {\prime} \text {Battery} = \text {Good} ^ {\prime}\right) \wedge^ {\prime} \text {Rating} = \text {Good} ^ {\prime}.
$$

The rule mining algorithm <sup>fi</sup>rst scans the data table once to mine need-rating rules involving one attribute in rule preconditions. It then recursively combines the need-rating rules generated to extract rules involving more attributes. The support and con<sup>fi</sup>dence degrees for rules are calculated simultaneously. Any rules with support and con<sup>fi</sup>dence degrees larger than the threshold are saved as need-rating rules. For example, $P _ { 1 }  c _ { 1 } , P _ { 1 }  c _ { 2 } ,$ and $P _ { 1 }  c _ { 3 }$ are three con<sup>fl</sup>icting rules with the same precondition. Their con<sup>fi</sup>dence degrees are 49%, 43%, and 8%, respectively. If the minimal con<sup>fi</sup>dence threshold is 40%, then rules $P _ { 1 }  c _ { 1 }$ and $P _ { 1 } \to c _ { 2 }$ would be retained, whereas $P _ { 1 }  c _ { 3 }$ is pruned.

After a comprehensive set of rules are mined, the redundant ones are deleted. The proposed prune process eliminates redundancy to ensure that succinct need-rating rules are derived, and all necessary multi-class information is preserved.

## 3.2.1. Derivation of classification experts

Let R be the set of need-rating rules discovered from data table I:

$$
R = \{P _ {1} \rightarrow c _ {1}, \dots , P _ {d} \rightarrow c _ {d}, \dots , P _ {| R |} \rightarrow c _ {| R |} \}
$$

where |R| is the number of rules in R. Precondition $P _ { d }$ consists of the attribute-values in data table I, and result c is the corresponding rating. For any subset $R _ { i }$ of the rule set $R ,$

$$
R _ {i} = \{P _ {i, 1} \rightarrow c _ {i, 1}, \dots , P _ {i, m} \rightarrow c _ {i, m}, \dots , P _ {i, | R _ {i} |} \rightarrow c _ {i, | R _ {i} |} \}
$$

where $\left| R _ { i } \right|$ is the number of rules in R , $P _ { i , m } \to c _ { i , m }$ is the mth rule in R . R is a classi<sup>fi</sup>cation expert in the rating classi<sup>fi</sup>cation problem if the following constraints are satis<sup>fi</sup>ed:

(1)

(2)

(3)

$$
\begin{array}{l} P _ {i, 1} = \dots = P _ {i, m} = \dots P _ {i, | R _ {i} |} \\ \text { For   any   other   rules } (P _ {d} \to c _ {d}) \not \in R _ {i}, P _ {d} \neq P _ {i, m} \\ c _ {i, 1} \neq \dots \neq c _ {i, m} \neq \dots \neq c _ {i, | R _ {i} |}. \end{array}\tag{1}
$$

$R _ { i }$ consists of all the need-rating rules which have the same precondition but different ratings. That is, it includes all the multi-class information associated with $P _ { i , m } .$ . For convenience, we rewrite $R _ { i }$ as: $R _ { i } \colon P _ { i }  E _ { i } , $ , where

$$
P _ {i} = P _ {i, m}, E _ {i} = \left(c _ {i, 1}, \operatorname{conf} _ {i, 1}\right) \vee \dots \vee \left(c _ {i, m}, \operatorname{conf} _ {i, m}\right) \vee \dots \vee \left(c _ {i, | R _ {i} |}, \operatorname{conf} _ {i, | R _ {i} |}\right) \vee (\Theta , \operatorname{conf} _ {i, \Theta})\tag{2}
$$

con $\mathbf { f } _ { i , m }$ is the con<sup>fi</sup>dence degree of $P _ { i , m }  c _ { i , m } ,$ , which is larger than the minimal con<sup>fi</sup>dence threshold, and Θ is the frame of discernment de<sup>fi</sup>ned in the evidence theory. The ${ \mathrm { c o n f } } _ { i , \Theta }$ is the belief degree assigned to catchall (default) terms since they cannot be classi<sup>fi</sup>ed to any speci<sup>fi</sup>c ratings by rules in $R _ { i } \mathrm { : }$

$$
c o n f _ {i, \Theta} = 1 - \sum_ {m = 1} ^ {| R _ {i} |} c o n f _ {i, m}
$$

In evidence theory, evidence bodies are given by experts and consist of hypothesis–probability pairs. For example, the evidence body may look like: {(Good, 0.6), (Average, 0.3), (poor, 0.1)}. In the expert's opinion, the probability of receiving a good evaluation is 60%, an average evaluation is 30%, and a poor evaluation is 10%. Recall that conf $_ { i , m }$ can be treated as a belief degree given by expert R to a hypothesized rating $c _ { i , m } ,$ based on observed attribute values in P . Therefore, $E _ { i }$ is regarded as the evidence body provided by classi<sup>fi</sup>cation expert $R _ { i } .$

The set of need-rating rules is transformed into a set of classi-<sup>fi</sup>cation experts, $R = \{ R _ { 1 } , . . . , R _ { i } , . . . , R _ { j } , . . . , R _ { T } \}$ , which satisfy the following constraints:

$$
\begin{array}{l} \underset {i = 1} {\overset {T} {\cup}} R _ {i} = R \\ R _ {i} \cap R _ {j} = \varphi , \text {   for   any   } i \text {   and   } j, i \neq j. \end{array}
$$

The set of evidence bodies corresponding to R is denoted as $E =$ $\{ E _ { 1 } , . . . , E _ { i } , . . . , E _ { j } , . . . , E _ { T } \}$ . To this point, we have transformed all the needrating rules into T independent classi<sup>fi</sup>cation experts. However, not all classi<sup>fi</sup>cation experts are necessary for the recommendation system; some are redundant. In the next subsection, we develop pruning methods to remove the redundant classi<sup>fi</sup>cation experts.

1. 2.

3.2.2. Classification expert pruning through an improved algorithm

The goal of pruning classi<sup>fi</sup>cation experts is to generate a minimal set of classi<sup>fi</sup>cation experts which can cover all customers in data table I. Before presenting the pruning algorithm, we de<sup>fi</sup>ne the order of a relationship on classi<sup>fi</sup>cation experts.

For two classi<sup>fi</sup>cation experts R and $R _ { j } , R _ { j }$ is said to be inferior to $R _ { i } ,$ that is, $R _ { i } \succ R _ { j } ,$ if

$$
\begin{array}{l} P _ {i} \subset P _ {j} \\ \text { For } \forall (c _ {j, n}, \operatorname{conf} _ {j, n}) \in E _ {j}, \exists (c _ {i, m}, \operatorname{conf} _ {i, m}) \in E _ {i}, c _ {i, m} \text { is   the   same   as } \\ c _ {j, n} \text { and } \operatorname{conf} _ {j, n} = \operatorname{conf} _ {i, m}. \end{array}
$$

The relationship $R _ { i } \succ R _ { j }$ implies that classi<sup>fi</sup>cation experts $R _ { i }$ and $R _ { j }$ provide the same classi<sup>fi</sup>cation outcome, but R gives the classi<sup>fi</sup>cation information based on a simpler precondition. The classi<sup>fi</sup>cation expert $R _ { j }$ is more restrictive but not more powerful relative to $R _ { i } .$ Hence, $R _ { j }$ is redundant and should be removed to improve the quality of the classi<sup>fi</sup>er. Fig. 3 shows the pruning algorithm used to improve the quality of classi<sup>fi</sup>cation experts.

The <sup>fi</sup>rst step prunes inferior classi<sup>fi</sup>cation experts. A classi<sup>fi</sup>cation expert $R _ { j }$ should be pruned if $\exists R _ { i } { \in } C \mathrm { E } S , R _ { i } { \succ } R _ { j } .$ That is, if the classi-<sup>fi</sup>cation expert has more complex preconditions but does not provide added information, then delete it. A simpler precondition is favorable since it provides a more powerful classi<sup>fi</sup>cation capability. The next pruning step uses the data covering method [26]. Classi<sup>fi</sup>cation expert $R _ { s }$ is necessary for customer c if $R _ { s }$ is a matching classi<sup>fi</sup>cation expert for c and there is not another matching classi<sup>fi</sup>cation expert whose precondition includes that of $R _ { s } .$ . Furthermore, we remove the classi<sup>fi</sup>cation experts which do not meet the support or con<sup>fi</sup>dence threshold.

## 3.3. Measure the importance of evidence bodies

After classi<sup>fi</sup>cation experts are generated, the next step is to determine the weights of the evidence bodies given by classi<sup>fi</sup>cation experts. In the traditional evidence theory, evidence weights are consistent with human experts' knowledge and experience. If a human expert is authoritative and familiar with the decision problem, the evidence body given by her/him will be reliable. In this research, the evidence bodies are derived from different attribute sets. Thus we use the weights of attributes to infer the importance of evidence bodies.

Input: The classification expert set (R) and data table (I) Output: Final classification expert set (CES)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
The pruning algorithm:
 $CES \leftarrow R$ 
1. For each classification expert  $R_{j}$  in CES
    if  $\exists R_{i} \in CES, R_{i} \succ R_{j}$ $CES = CES \setminus R_{j}$ 
    end if
End for

2. For each classification expert  $R_{s}$  in CES
    $count_{s} \leftarrow 0$ 
    For each customer c in data table I
    If  $R_{s}$  is a necessary for c
    $count_{s} \leftarrow count_{s} + 1$ 
    End if
    End for
End for
Delete the classification experts in CES which dissatisfy the following constraint:
 $count_{s} \geq threshold$
</div>

Fig. 3. The classi<sup>fi</sup>cation expert pruning algorithm.

Many methods such as support vector machine (SVM) [33] and information theory [9] have been used to measure attribute weights. Neural network is one of the most ef<sup>fi</sup>cient methods for deriving the factor weights [19,22]. For a rating classi<sup>fi</sup>cation problem, the number of possible attribute sets in rule preconditions totals $2 ^ { | \mathsf { A } | } - 1 ,$ , which is equivalent to the number of times traditional data mining techniques need to train the datasets in order to obtain the weight for each evidence body. This is very time-consuming and computationally prohibitive for real-time recommendation systems. In this paper, we employ a NN-based method, which requires training only once with need-rating data to derive the evidence weights.

For need-rating data I, we <sup>fi</sup>rst <sup>fi</sup>nd a trained neural network N with the entire set of attributes $A , A { = } \{ A _ { 1 } { , } . . . , A _ { h } { , } . . . , A _ { | A | } \}$ , as its input. Then the output ratings for |O| customers in data table I, denoted as $N C = \{ n c _ { 1 } , . . . , n c _ { k } , . . . , n c _ { | O | } \} , n c _ { k } \in C , k = 1 , 2 , . . . , | O |$ , can be calculated. Suppose the real ratings of the customers are $R C = \{ r c _ { 1 } , . . . , r c _ { k } , . . . , r c _ { | O | } \}$ where $r c _ { k } \in C$ is the rating of the kth customer in $O .$ The network's accuracy, denoted $d _ { 0 }$ can be calculated as follows:

$$
d _ {0} = \sum_ {k = 1} ^ {| O |} v _ {k},   v _ {k} = \left\{ \begin{array}{l} 1 \text {   If   } n c _ {k} \text {   is   the   same   as   } r c _ {k} \\ 0 \text {   Otherwise } \end{array} \right.
$$

The weights of evidence bodies can then be computed according to the classi<sup>fi</sup>cation experts in CES. Suppose the precondition of classi-<sup>fi</sup>cation expert $R _ { i }$ consists of $B _ { i } , B _ { i } { = } \{ A _ { i , 1 } , A _ { i , 2 } { , \ldots } A _ { i , | B _ { i } | } \}$ , the accuracy $d _ { i }$ without the attributes in $B _ { i }$ are computed by simply setting the connection weights from the input attributes $\{ A _ { i , 1 } , A _ { i , 2 } . . . A _ { i , | B _ { i } | } \}$ of the trained network to zero. Finally, the difference between $d _ { i }$ and $d _ { 0 }$ is found to measure the in<sup>fl</sup>uence of attribute set $\{ A _ { i , 1 } , A _ { i , 2 } , . . . A _ { i , | B _ { i } | } \}$ to the classi-<sup>fi</sup>cation. The greater the in<sup>fl</sup>uence of the attribute set is to the classi-<sup>fi</sup>cation, the bigger is its weight.

Key steps of the NN algorithm are outlined below.

(1) Let $A { = } \{ A _ { 1 } { , } . . . , A _ { h } { , } . . . , A _ { | A | } \}$ be the set of all input attributes and RC be the real ratings.

(2) Train the neural network N to maximize the network accuracy $d _ { 0 }$ with A as input such that it achieves a network as accurately as possible.

(3) For $i { = } 1 , 2 { , } { \ldots } , | \mathrm { C E S } |$ , let $N _ { i }$ be a network whose weights are as follows:

(a) For all the inputs except $\{ A _ { i , 1 } , A _ { i , 2 } , . . . A _ { i , | B _ { i } | } \}$ , assign the weights of $N _ { i }$ equal to the weights of N.

(b) Set the weights from input $\{ A _ { i , 1 } , A _ { i , 2 } , . . . A _ { i , | B _ { i } | } \} _ { }$ o zero.

Compute the output of network $N _ { i } ,$ , denoted as $\mathsf { N C } _ { i } = \{ \mathrm { n c } _ { i , 1 } , . . . , \mathrm { n c } _ { i , k } , . . . ,$ $\mathfrak { n c } _ { i , | O | } \}$ , and the accuracy of $N _ { i }$ , denoted as $d _ { i }$

$$
B _ {i}
$$

$$
w _ {i} = d _ {0} - d _ {i}.
$$

(5) If $i { \geq } | \mathrm { C E S } | , \mathrm { g o }$ to (6), otherwise, set $i = i + 1$ and go to (3).

(6) The derived $\{ w _ { 1 } , . . . , w _ { i } , . . . , w _ { | \mathrm { C E S } | } \}$ are the weights of the evidence bodies, where w is the weight of evidence body $E _ { i \cdot }$

The proposed NN method makes it possible to derive the weights quickly and ef<sup>fi</sup>ciently without falling into the trap of local minimum. It therefore attains more accurate evidence weights and improves the ef<sup>fi</sup>ciency of the rating classi<sup>fi</sup>cation model.

## 3.4. Construct rating classifier for potential customers

Given the classi<sup>fi</sup>cation experts, evidence bodies, and evidence weights, the recommendation system is ready to predict the ratings of customers. For a potential customer c, the system identi<sup>fi</sup>es the necessary classi<sup>fi</sup>cation experts <sup>fi</sup>rst. For example, $R _ { i }$ and $R _ { j }$ are two matching classi<sup>fi</sup>cation experts whose preconditions are $\cdot  g e = M i d d l e ^ { \prime } \wedge$ ‘CPU=Average’ $\wedge$ ‘Battery=Good’ for $R _ { i } ,$ and $\scriptstyle { } ^ { * } A g e = M i d d l e ^ { \prime } \land { } ^ { * } C P U =$ Average’ for $\mathrm { R } _ { j \cdot } R _ { j }$ could be extracted from customers whose preconditions satisfy ${ } ^ { \cdot } \dot { A } g e = M i d d l e ^ { \prime } \wedge { } ^ { \cdot } C P U { = } A \nu e r a g e ^ { \prime } \wedge$ ‘Battery=Good’ or ${ } ^ { * } A g e = M i d d l e ^ { , } \wedge { } ^ { * } C P U { = } A \nu e r a g e ^ { , } \wedge$ ‘Battery≠Good’, while $R _ { i }$ is extracted from customers whose preconditions satisfy $\cdot A g e = M i d d l e ^ { \prime } \wedge$ ‘CPU=Average’ ∧ ‘Battery=Good’. We found $R _ { i }$ to contain more speci<sup>fi</sup>c information and is more precise to use, thus R is not necessary for predicting the ratings of customer c.

To combine evidence bodies, we apply the evidential reasoning method proposed by Yang and colleagues [40]. The evidential reasoning method <sup>fi</sup>rst transforms the evidence bodies into basic probability masses by combining the normalized evidence weights and the belief degrees. Then, the basic probability masses are combined into an aggregated basic probability assignment. Finally, the aggregated probability assignments are normalized. For customer $c ,$ we assume the matching classi<sup>fi</sup>cation expert set consists of S classi<sup>fi</sup>cation experts, $R _ { c } = ( R _ { c , 1 } , . . . , R _ { c , u } , . . . , R _ { c , S } ) , R _ { c , u } { \in } \mathrm { C E S } , u { = } 1 , 2 , . . . , S .$ The corresponding evidence bodies and weights are ${ \sf E S } _ { c } = ( { \cal E } _ { c , 1 } , . . . , { \cal E } _ { c , u } , . . . , { \cal E } _ { c , S } )$ , and $W _ { c } =$ $( w _ { c , 1 } , . . . , w _ { c , u } . . . , w _ { c , S } )$ . Rating classi<sup>fi</sup>cation of new customers can be supported by matching its characteristics to one of the classi<sup>fi</sup>cation experts. The matching may lead to one of three situations:

(a) customer c matches one classi<sup>fi</sup>cation expert,

(b) customer c matches more than one classi<sup>fi</sup>cation expert,

(c) customer c does not match any classi<sup>fi</sup>cation experts.

When no classi<sup>fi</sup>cation experts match the new customer, we will not classify the new customer into any class, that is, the proposed model is unable to predict the ratings of customer c. The recommendation system will communicate with the customer and ask for more detailed inputs. In case (a), S=1, there is only one expert $R _ { c , 1 }$ can be used, we employ $R _ { c , 1 }$ to predict the ratings of customer c. In case (b), $R _ { c }$ consists of more than one expert, we use the following procedure to attain classi<sup>fi</sup>cation information.

First, the weights of evidence bodies are normalized to form $W _ { c } ^ { \prime }$ $\boldsymbol { W ^ { \ast } } _ { c } = ( \boldsymbol { w ^ { \ast } } _ { c , 1 } , . . . , \boldsymbol { w ^ { \ast } } _ { c , u } , . . . , \boldsymbol { w ^ { \ast } } _ { c , S } )$ , by the following unitary function:

$$
w _ {c, u} ^ {\prime} = \frac {w _ {c , u}}{\sum_ {l = 1} ^ {S} w _ {l}}, u = 1, 2, \dots , S
$$

Second, calculate the basic probability masses through multiplying $W _ { c }$ by the evidence bodies in $E S _ { c } .$ Third, calculate the aggregate probability assignment by combining the basic probability masses using the formula proposed by Yang and colleagues [40].

The integrated strategy has two main advantages. First, it ensures that we take all of the essential multi-class information about the new customer into account. The comprehensive utilization of multi-class information plays an important role in constructing an accurate recommendation system. Second, the integrated probability assignment provides the probabilities of possible ratings given by customers after consumption. The ratings together with their respective probabilities allow the recommendation to be more <sup>fl</sup>exible for online stores.

## 4. Experimental study

## 4.1. Data

The raw data in our experiment come from online stores which sell Inspiron 1525 laptops. For each customer, we <sup>fi</sup>rst collect his rating of the laptop, and then retrieve the demographic pro<sup>fi</sup>le, as well as need and preference statements of the customer. In the process of knowledge discovery from online reviews, the existence of fake reviews is an intractable problem [15,29]. Often, fake reviews are entirely negative or positive. Therefore, to avoid the impact of fake reviews on the accuracy of rating classi<sup>fi</sup>cation, each of the co-authors individually identi<sup>fi</sup>es the reviews with complete positive or negative comments, and then collectively decides whether to remove such reviews from the data set. The attributes of age and expertise (computer knowledge) on laptops form customers' demographic pro<sup>fi</sup>le. Customers' needs and preferences are characterized by CPU speed, battery, audio card, and video card. The attributes and ratings together with possible values are presented in Table 2.

Table 2  
Attribute description.

<table><tr><td rowspan="2">Attribute</td><td colspan="2">Profile</td><td colspan="4">Customer need</td><td rowspan="2">Rating</td></tr><tr><td>Age</td><td>Expertise</td><td>CPU</td><td>Battery</td><td>Audio</td><td>Video</td></tr><tr><td>Attribute value</td><td>≤24 (Y), 24–34 (M), ≥35 (O)</td><td>Average (A), Good (G)</td><td>Average, Good</td><td>Average, Good</td><td>Average, Good</td><td>Average, Good</td><td>Poor (P), Average, Good</td></tr></table>

Table 3  
Examples of the need-rating data

<table><tr><td>Customer</td><td>Age</td><td>Expertise</td><td>CPU</td><td>Battery</td><td>Audio</td><td>Video</td><td>Rating</td></tr><tr><td> $c_{1}$ </td><td>Y</td><td>G</td><td>A</td><td>G</td><td>A</td><td>A</td><td>G</td></tr><tr><td> $c_{2}$ </td><td>O</td><td>A</td><td>A</td><td>A</td><td>A</td><td>G</td><td>P</td></tr><tr><td> $c_{3}$ </td><td>M</td><td>G</td><td>A</td><td>A</td><td>G</td><td>A</td><td>A</td></tr><tr><td> $c_{4}$ </td><td>M</td><td>G</td><td>A</td><td>A</td><td>G</td><td>A</td><td>G</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td> $c_{505}$ </td><td>O</td><td>A</td><td>G</td><td>A</td><td>A</td><td>G</td><td>G</td></tr><tr><td> $c_{506}$ </td><td>Y</td><td>A</td><td>A</td><td>A</td><td>A</td><td>G</td><td>P</td></tr><tr><td> $c_{507}$ </td><td>M</td><td>G</td><td>A</td><td>G</td><td>G</td><td>A</td><td>G</td></tr></table>

Customers' needs and preferences are extracted by the inverse analysis. For example, if a customer claims that the battery life is insuf<sup>fi</sup>- cient or he/she prefers a laptop with long battery life, we infer that the customer needs a laptop with good battery life. If the customer mentions nothing or claims that the battery life is acceptable, we assume that the laptops with an average battery life will meet his/her needs. Ratings represent customers' evaluation about the product after their usage. From Dell.com and Bestbuy.com we collected 507 need-rating records, of which 405 cases are randomly selected to create the training data, and the remaining 102 records form the testing data. Only the training data is submitted to construct the rating classi<sup>fi</sup>er for the laptop. Examples of the need-rating data are shown in Table 3.

## 4.2. Mine need-rating rules

To mine classi<sup>fi</sup>cation rules from data, the thresholds of support and con<sup>fi</sup>dence degrees are usually set to some small numbers since this can remove the ineffective rules and improve the quality of classi<sup>fi</sup>ers. In the rating classi<sup>fi</sup>cation problem, the values of support and con<sup>fi</sup>dence thresholds depend on the uncertainty of the need-rating data. This paper sets the two thresholds to 0.05 and 0.1 respectively, which are normally used in most of the associative classi<sup>fi</sup>cation methods [37]. From the need-rating data, we use the proposed method to discover 377 rules. Among all extracted rules, we found 87.3% of them con<sup>fl</sup>ict with one another. Twenty-two of the 377 rules are presented in Table 4, which will be used to illustrate the rating classi<sup>fi</sup>er construction procedure.

Most of the traditional associative classi<sup>fi</sup>cation methods are designed to <sup>fi</sup>nd only the rules with the highest con<sup>fi</sup>dence level, and use them to classify new objects. However, in our case the con<sup>fl</sup>icting rules are retained through the classi<sup>fi</sup>cation expert pruning method. For example, in Table $^ { 4 , }$ r , r , and $r _ { 1 4 }$ are three con<sup>fl</sup>icting rules who share the same precondition but different rating results:

‘Expertise=G’ ∧ ‘CPU=A’ ∧ ‘Battery=G’→‘Rating=G’;

$$
^ {\prime} E x p e r t i s e = G ^ {\prime} \wedge^ {\prime} C P U = A ^ {\prime} \wedge^ {\prime} B a t t e r y = G ^ {\prime} \rightarrow^ {\prime} R a t i n g = P ^ {\prime};
$$

$$
^ {\prime} E x p e r t i s e = G ^ {\prime} \wedge^ {\prime} C P U = A ^ {\prime} \wedge^ {\prime} B a t t e r y = G ^ {\prime} \rightarrow^ {\prime} R a t i n g = A ^ {\prime}.
$$

Traditional methods will only select $r _ { 1 4 }$ as the classi<sup>fi</sup>cation rule due to its high con<sup>fi</sup>dence level. In this research we take three phases to derive the multi-class information from these rules.

The <sup>fi</sup>rst step is to combine the con<sup>fl</sup>icting rules to form classi-<sup>fi</sup>cation experts and the corresponding evidence bodies. For example, rules $r _ { 1 2 } , r _ { 1 3 } ,$ and $r _ { 1 4 }$ form classi<sup>fi</sup>cation expert $R _ { 7 } .$ Overall, 174 classi<sup>fi</sup>cation experts are derived from the 377 rules. Table 5 shows 11 of such classi<sup>fi</sup>cation experts, which are based on data from Table 4. In Table 5, Θ represents the frame of discernment for the need-rating data. The numbers in the last four columns represent the con<sup>fi</sup>dence (belief) degrees associated with each rating. For example, $R _ { 1 }$ implies that the customers with average computer knowledge will rate Inspiron 1525 laptop as ‘Poor’ with 16% probability, ‘Average’ with 28%, and ‘Good’ with 56%. A positive Θ shows the probability that the classi<sup>fi</sup>cation expert cannot predict the responses of customers with such speci<sup>fi</sup>c precondition. As can be seen in Table 5, there are two kinds of classi<sup>fi</sup>cation experts. One is the classi<sup>fi</sup>cation experts which assign almost all of the belief degrees to one rating. For example, classi<sup>fi</sup>- cation expert $R _ { 3 }$ implies that customers who are older than 35 and need a laptop with good CPU speed will give a ‘Good’ rating with 93% probability for Inspiron 1525 laptop. The other is the classi<sup>fi</sup>cation experts whose ratings vary. For example, the belief degrees of classi<sup>fi</sup>- cation experts $R _ { 8 }$ are assigned more evenly to all three ratings, ‘Poor’, ‘Average’, and ‘Good’, respectively. The evidence bodies given by such classi<sup>fi</sup>cation experts provide useful information about possible customer ratings for the product.

Table 4  
Rules discovered from the need-rating data.

<table><tr><td>Rule</td><td>Age</td><td>Expertise</td><td>CPU</td><td>Battery</td><td>Audio</td><td>Video</td><td>Rating</td><td>Confidence</td></tr><tr><td> $r_1$ </td><td>*</td><td>A</td><td>*</td><td>*</td><td>*</td><td>*</td><td>G</td><td>0.56</td></tr><tr><td> $r_2$ </td><td>*</td><td>A</td><td>*</td><td>*</td><td>*</td><td>*</td><td>P</td><td>0.16</td></tr><tr><td> $r_3$ </td><td>*</td><td>A</td><td>*</td><td>*</td><td>*</td><td>*</td><td>A</td><td>0.28</td></tr><tr><td> $r_4$ </td><td>Y</td><td>A</td><td>*</td><td>*</td><td>*</td><td>*</td><td>P</td><td>0.31</td></tr><tr><td> $r_5$ </td><td>Y</td><td>A</td><td>*</td><td>*</td><td>*</td><td>*</td><td>A</td><td>0.50</td></tr><tr><td> $r_6$ </td><td>O</td><td>*</td><td>G</td><td>*</td><td>*</td><td>*</td><td>G</td><td>0.93</td></tr><tr><td> $r_7$ </td><td>M</td><td>*</td><td>A</td><td>*</td><td>*</td><td>*</td><td>P</td><td>0.31</td></tr><tr><td> $r_8$ </td><td>M</td><td>*</td><td>A</td><td>*</td><td>*</td><td>*</td><td>A</td><td>0.56</td></tr><tr><td> $r_9$ </td><td>O</td><td>A</td><td>G</td><td>*</td><td>*</td><td>*</td><td>G</td><td>0.93</td></tr><tr><td> $r_{10}$ </td><td>M</td><td>G</td><td>A</td><td>*</td><td>*</td><td>*</td><td>P</td><td>0.31</td></tr><tr><td> $r_{11}$ </td><td>M</td><td>G</td><td>A</td><td>*</td><td>*</td><td>*</td><td>A</td><td>0.56</td></tr><tr><td> $r_{12}$ </td><td>*</td><td>G</td><td>A</td><td>G</td><td>*</td><td>*</td><td>G</td><td>0.24</td></tr><tr><td> $r_{13}$ </td><td>*</td><td>G</td><td>A</td><td>G</td><td>*</td><td>*</td><td>P</td><td>0.28</td></tr><tr><td> $r_{14}$ </td><td>*</td><td>G</td><td>A</td><td>G</td><td>*</td><td>*</td><td>A</td><td>0.48</td></tr><tr><td> $r_{15}$ </td><td>*</td><td>G</td><td>A</td><td>G</td><td>*</td><td>A</td><td>G</td><td>0.24</td></tr><tr><td> $r_{16}$ </td><td>*</td><td>G</td><td>A</td><td>G</td><td>*</td><td>A</td><td>P</td><td>0.28</td></tr><tr><td> $r_{17}$ </td><td>*</td><td>G</td><td>A</td><td>G</td><td>*</td><td>A</td><td>A</td><td>0.48</td></tr><tr><td> $r_{18}$ </td><td>M</td><td>*</td><td>A</td><td>G</td><td>*</td><td>*</td><td>P</td><td>0.31</td></tr><tr><td> $r_{19}$ </td><td>M</td><td>*</td><td>A</td><td>G</td><td>*</td><td>*</td><td>A</td><td>0.54</td></tr><tr><td> $r_{20}$ </td><td>*</td><td>*</td><td>A</td><td>*</td><td>A</td><td>G</td><td>G</td><td>0.44</td></tr><tr><td> $r_{21}$ </td><td>*</td><td>*</td><td>A</td><td>*</td><td>A</td><td>G</td><td>A</td><td>0.37</td></tr><tr><td> $r_{22}$ </td><td>Y</td><td>*</td><td>*</td><td>G</td><td>*</td><td>*</td><td>G</td><td>1.00</td></tr></table>

The second step prunes the inferior classi<sup>fi</sup>cation experts. In Table 5, classi<sup>fi</sup>cation expert $R _ { 6 }$ is inferior to $R _ { 4 }$ because it gives the same classi<sup>fi</sup>cation information, but contains a more complex precondition. Therefore, $R _ { 6 }$ is removed from the set of classi<sup>fi</sup>cation experts. Likewise, classi<sup>fi</sup>cation experts $R _ { 5 }$ and $R _ { 8 }$ are also removed because they are inferior to $R _ { 3 }$ and $R _ { 7 } ,$ respectively.

Examples of classi<sup>fi</sup>cation experts.

<table><tr><td rowspan="2">ClassificationExpert</td><td colspan="6">Precondition (P)</td><td colspan="4">Evidence Body (E)</td></tr><tr><td>Age</td><td>Expertise</td><td>CPU</td><td>Battery</td><td>Audio</td><td>Video</td><td>P</td><td>A</td><td>G</td><td> $\Theta$ </td></tr><tr><td> $R_1$ </td><td>*</td><td>A</td><td>*</td><td>*</td><td>*</td><td>*</td><td>0.16</td><td>0.28</td><td>0.56</td><td>0</td></tr><tr><td> $R_2$ </td><td>Y</td><td>A</td><td>*</td><td>*</td><td>*</td><td>*</td><td>0.31</td><td>0.5</td><td>0</td><td>0.19</td></tr><tr><td> $R_3$ </td><td>O</td><td>*</td><td>G</td><td>*</td><td>*</td><td>*</td><td>0</td><td>0</td><td>0.93</td><td>0.07</td></tr><tr><td> $R_4$ </td><td>M</td><td>*</td><td>A</td><td>*</td><td>*</td><td>*</td><td>0.31</td><td>0.56</td><td>0</td><td>0.13</td></tr><tr><td> $R_5$ </td><td>O</td><td>A</td><td>G</td><td>*</td><td>*</td><td>*</td><td>0</td><td>0</td><td>0.93</td><td>0.07</td></tr><tr><td> $R_6$ </td><td>M</td><td>G</td><td>A</td><td>*</td><td>*</td><td>*</td><td>0.31</td><td>0.56</td><td>0</td><td>0.13</td></tr><tr><td> $R_7$ </td><td>*</td><td>G</td><td>A</td><td>G</td><td>*</td><td>*</td><td>0.28</td><td>0.48</td><td>0.24</td><td>0</td></tr><tr><td> $R_8$ </td><td>*</td><td>G</td><td>A</td><td>G</td><td>*</td><td>A</td><td>0.28</td><td>0.48</td><td>0.24</td><td>0</td></tr><tr><td> $R_9$ </td><td>M</td><td>*</td><td>A</td><td>G</td><td>*</td><td>*</td><td>0.31</td><td>0.54</td><td>0</td><td>0.15</td></tr><tr><td> $R_{10}$ </td><td>*</td><td>*</td><td>A</td><td>*</td><td>A</td><td>G</td><td>0</td><td>0.37</td><td>0.44</td><td>0.19</td></tr><tr><td> $R_{11}$ </td><td>Y</td><td>*</td><td>*</td><td>G</td><td>*</td><td>*</td><td>0</td><td>0</td><td>1.00</td><td>0</td></tr></table>

Table 6  
The <sup>fi</sup>nal classi<sup>fi</sup>cation expert set.

<table><tr><td rowspan="2">ClassificationExpert</td><td colspan="6">Precondition (P)</td><td colspan="4">Evidence body (E)</td></tr><tr><td>Age</td><td>Expertise</td><td>CPU</td><td>Battery</td><td>Audio</td><td>Video</td><td>P</td><td>A</td><td>G</td><td> $\Theta$ </td></tr><tr><td> $R_2$ </td><td>Y</td><td>A</td><td>*</td><td>*</td><td>*</td><td>*</td><td>0.31</td><td>0.5</td><td>0</td><td>0.19</td></tr><tr><td> $R_3$ </td><td>O</td><td>*</td><td>G</td><td>*</td><td>*</td><td>*</td><td>0</td><td>0</td><td>0.93</td><td>0.07</td></tr><tr><td> $R_4$ </td><td>M</td><td>*</td><td>A</td><td>*</td><td>*</td><td>*</td><td>0.31</td><td>0.56</td><td>0</td><td>0.13</td></tr><tr><td> $R_7$ </td><td>*</td><td>G</td><td>A</td><td>G</td><td>*</td><td>*</td><td>0.28</td><td>0.48</td><td>0.24</td><td>0</td></tr><tr><td> $R_9$ </td><td>M</td><td>*</td><td>A</td><td>G</td><td>*</td><td>*</td><td>0.31</td><td>0.54</td><td>0</td><td>0.15</td></tr><tr><td> $R_{10}$ </td><td>*</td><td>*</td><td>A</td><td>*</td><td>A</td><td>G</td><td>0</td><td>0.37</td><td>0.44</td><td>0.19</td></tr><tr><td> $R_{11}$ </td><td>Y</td><td>*</td><td>*</td><td>G</td><td>*</td><td>*</td><td>0</td><td>0</td><td>1.00</td><td>0</td></tr></table>

Finally, the unnecessary classi<sup>fi</sup>cation experts are pruned using the database coverage method. The database coverage threshold is set to 4, a number frequently used by other researchers [35]. If a classi<sup>fi</sup>- cation expert is necessary to four or more records in the need-rating database, it is retained; otherwise, removed. After all three phases, the original 174 classi<sup>fi</sup>cation experts are reduced to 45 classi<sup>fi</sup>cation experts, which are capable of covering the 405 customers in the training set. In Table 5, the classi<sup>fi</sup>cation expert $R _ { 1 }$ is removed by the database coverage method because it is necessary for only two customers' records. As a result, the set given in Table 5 is reduced to Table 6.

## 4.3. Measure the importance of evidence bodies

After the classi<sup>fi</sup>cation experts are developed from the need-rating data, the corresponding evidence bodies are evaluated using the neural network method. We adopt the radial basis function (RBF) neural network [4] to perform this task. The RBF neural network architecture, which is designed to solve classi<sup>fi</sup>cation problems similar to the radial basis function implemented in the software system MATLAB 7.0, has a single hidden layer with Gaussian function. Using eight data sets from the public machine learning repository [28] to test the ef<sup>fi</sup>ciency of the RBF neural network for the calculation of attribute weights, we found the average runtime is only 7.87% of the rough set method employed by CSMC [23]. Furthermore, the computational results are comparable between the two methods. The high-speed neural network method signi<sup>fi</sup>cantly improves the capability of the rating classi<sup>fi</sup>er. Following the procedures described in Section 3.3, we obtain the weights of all evidence bodies. Table 7 shows the weights of the evidence bodies associated with the classi<sup>fi</sup>cation experts given in Table 6, where E is the evidence body given by classi<sup>fi</sup>cation expert $R _ { i } , i \in \{ 2 , 3 , 4 , 7 , 9 ,$ 10, 11}.

In the need-rating database, 20 more customers will be misclassi<sup>fi</sup>ed if we remove attributes CPU, Audio, and Video from the needrating data. This implies that the attribute set {CPU, Audio, Video} only has a small classi<sup>fi</sup>cation power, as attested by the small weight, 20, found for evidence body $\mathtt { E } _ { 1 0 } .$ . On the contrary, the attribute set {Age, CPU, Battery} can distinguish customers' ratings to a great extent. If we remove the three attributes from the need-rating data, an additional 91 customers will receive the wrong classi<sup>fi</sup>cation. As a result, the weight of the evidence body $E _ { 9 }$ is 91, the largest of all. Other weights are derived similarly.

## 4.4. Construct rating classifier for potential customers

Using the entire 45 classi<sup>fi</sup>cation experts, evidence bodies, and their weights, we are able to construct a comprehensive classi<sup>fi</sup>er to predict the ratings of customers with different characteristics. For illustration, we use the classi<sup>fi</sup>cation experts in Table 6 and the weights in Table 7 to predict the ratings of customer c with the characteristics given in Table 8. The matching classi<sup>fi</sup>cation experts, $R _ { 4 } , R _ { 7 } ,$ $R _ { 9 } ,$ and $R _ { 1 0 } ,$ are found <sup>fi</sup>rst. Among them, $R _ { 4 }$ is not applied because classi<sup>fi</sup>cation expert, $R _ { 9 }$ is more speci<sup>fi</sup>c than $R _ { 4 }$

Table 7  
The weights of the evidence bodies derived by the neural network.

<table><tr><td>Evidence body</td><td> $E_{2}$ </td><td> $E_{3}$ </td><td> $E_{4}$ </td><td> $E_{7}$ </td><td> $E_{9}$ </td><td> $E_{10}$ </td><td> $E_{11}$ </td></tr><tr><td>Weight</td><td>37</td><td>82</td><td>82</td><td>61</td><td>91</td><td>20</td><td>53</td></tr></table>

Table 8  
A potential customer.

<table><tr><td>Customer</td><td>Age</td><td>Expertise</td><td>CPU</td><td>Battery</td><td>Audio</td><td>Video</td></tr><tr><td>c</td><td>M</td><td>G</td><td>A</td><td>G</td><td>A</td><td>G</td></tr></table>

Thereafter, we combine the multiple evidence bodies given by the three classi<sup>fi</sup>cation experts to calculate the aggregate multi-class classi<sup>fi</sup>cation information. Since the weights for $E _ { 7 } , \ E _ { 9 } ,$ and $E _ { 1 0 }$ are 61, 91, and 20, respectively, which are normalized to .35, .53, and .12 respectively. The evidence bodies used to classify customer c together with their weights are presented in Table 9. Following the method in Section 3.4, we are able to derive the aggregate multi-class classi<sup>fi</sup>cation results as shown in Table 10.

We thus can predict the rating of customer c. Furthermore, the reason why the product is or is not recommended to customer c is lucid. If the product is recommended to customer c, he/she will rate the product as ‘Poor’ with 26% probability and ‘Average’ with 53% probability. The chance he/she will consider the product to be “Good” is only 10%. The product thus should not be recommended to the customer.

For the 102 customers in the test data set, two kinds of classi<sup>fi</sup>- cation results are obtained by the rating classi<sup>fi</sup>er. The <sup>fi</sup>rst kind of results assigns most of the probabilities to one rating, which makes estimating customer response easy. For example, in Table 11 the predicted ratings for the four customers are ‘Good’, ‘Good’, ‘Good’, and ‘Average’ with probabilities of 94%, 79%, 70%, and 73%, respectively. The decisions are easy to make, that is, recommend the product to customers $c _ { 4 1 2 } , c _ { 4 3 5 } ,$ , and $c _ { 4 7 8 } ,$ , but not to $c _ { 5 0 1 }$

However, indistinct ratings may also take place, resulting in a less valuable recommendation. For example, the ratings in Table 12 do not provide de<sup>fi</sup>nite recommendations. Under such circumstances, additional measures may be taken to ensure customer satisfaction. For example, additional information may be elicited to obtain more accurate needs information and preferences data; a greater discount or a warranty may also be offered to increase the odds of satisfaction.

Table 13 provides accuracy comparisons among different methods. The experiments of the decision tree method (C4.5) and support vector machine (SVM) algorithm were carried out using the Weka software system, which is an open source tool for machine learning [39]. The classi<sup>fi</sup>cation based on associations (CBA) algorithm was studied using the software developed by the authors in [26], and the combination strategy for multi-class classi<sup>fi</sup>cation (CSMC) was implemented by software system MATLAB 7.0.

Due to the existence of con<sup>fl</sup>icting ratings, it is hard for traditional methods to mine useful multi-class patterns and construct accurate classi<sup>fi</sup>ers. On the contrary, the proposed method can deal with the uncertain environment elegantly. It retains useful con<sup>fl</sup>icting information, integrates con<sup>fl</sup>icting rules to form classi<sup>fi</sup>cation experts, and eventually builds the rating classi<sup>fi</sup>cation model. This explains why the proposed method can attain more accuracy than conventional methods.

Table 9  
The set of evidence bodies that matches the target customer.

<table><tr><td>Evidence body</td><td>P</td><td>A</td><td>G</td><td> $\Theta$ </td><td>Weight</td></tr><tr><td> $E_{7}$ </td><td>0.28</td><td>0.48</td><td>0.24</td><td>0</td><td>0.35</td></tr><tr><td> $E_{9}$ </td><td>0.31</td><td>0.54</td><td>0</td><td>0.15</td><td>0.53</td></tr><tr><td> $E_{10}$ </td><td>0</td><td>0.37</td><td>0.44</td><td>0.19</td><td>0.12</td></tr></table>

Table 10  
Rating classi<sup>fi</sup>cation results of the potential customer c.

<table><tr><td>Poor</td><td>Average</td><td>Good</td><td>θ</td></tr><tr><td>0.26</td><td>0.53</td><td>0.10</td><td>0.11</td></tr></table>

Table 11  
Customers whose ratings are easily predicted

<table><tr><td>Customer</td><td>Age</td><td>Expertise</td><td>CPU</td><td>Battery</td><td>Audio</td><td>Video</td><td>P</td><td>A</td><td>G</td><td> $\Theta$ </td></tr><tr><td> $c_{412}$ </td><td>Y</td><td>G</td><td>A</td><td>G</td><td>A</td><td>A</td><td>0.02</td><td>0.04</td><td>0.94</td><td>0.00</td></tr><tr><td> $c_{435}$ </td><td>Y</td><td>G</td><td>G</td><td>G</td><td>A</td><td>A</td><td>0.01</td><td>0.12</td><td>0.79</td><td>0.08</td></tr><tr><td> $c_{478}$ </td><td>O</td><td>A</td><td>G</td><td>A</td><td>A</td><td>G</td><td>0.08</td><td>0.14</td><td>0.70</td><td>0.08</td></tr><tr><td> $c_{501}$ </td><td>Y</td><td>A</td><td>A</td><td>A</td><td>G</td><td>G</td><td>0.05</td><td>0.73</td><td>0.01</td><td>0.21</td></tr></table>

Table 12  
Customers with inconclusive ratings.

<table><tr><td>Customer</td><td>Age</td><td>Expertise</td><td>CPU</td><td>Battery</td><td>Audio</td><td>Video</td><td>P</td><td>A</td><td>G</td><td> $\Theta$ </td></tr><tr><td> $C_{417}$ </td><td>M</td><td>G</td><td>G</td><td>A</td><td>A</td><td>G</td><td>0.03</td><td>0.38</td><td>0.27</td><td>0.32</td></tr><tr><td> $C_{452}$ </td><td>Y</td><td>A</td><td>G</td><td>G</td><td>A</td><td>A</td><td>0.00</td><td>0.26</td><td>0.41</td><td>0.33</td></tr><tr><td> $C_{469}$ </td><td>Y</td><td>A</td><td>G</td><td>G</td><td>A</td><td>G</td><td>0.00</td><td>0.39</td><td>0.16</td><td>0.45</td></tr><tr><td> $C_{504}$ </td><td>M</td><td>G</td><td>A</td><td>G</td><td>G</td><td>A</td><td>0.25</td><td>0.47</td><td>0.28</td><td>0.00</td></tr></table>

Table 13  
Comparison of classi<sup>fi</sup>cation accuracy.

<table><tr><td>Method</td><td>C4.5</td><td>SVM</td><td>CBA</td><td>CSMC</td><td>Proposed model</td></tr><tr><td>Accuracy</td><td>0.706</td><td>0.755</td><td>0.686</td><td>0.794</td><td>0.824</td></tr></table>

Nomenclature  
C4.5: The decision tree method  
SVM: Support vector machine algorithm  
CBA: Classi<sup>fi</sup>cation based on associations algorithm  
CSMC: Combination strategy for multi-class classi<sup>fi</sup>cation.

## 5. Conclusions and future work

The recommendation system is an important tool to offer personalized service and maximize customer satisfaction. Current literature regards a recommendation system as a success if a potential customer takes the advice and purchases the recommended product. We argue that a truly successful recommendation system should be the one that maximizes the customers' after-sale satisfaction, not one that just lures customers into the act of purchasing. We emphasize that a good recommendation system not only considers what the customer needs, but also ensures customer's contentment. The main contributions of this research are twofold. First, we make a distinction between the customer purchase and the customer endorsement. When a customer follows advice to purchase a product (DO), it does not imply that the person is truly pleased (FEEL) with the decision he/ she made. Second, to maximize a customer's satisfaction level, we propose a more effective and ef<sup>fi</sup>cient rating classi<sup>fi</sup>cation model based on the customer's pro<sup>fi</sup>le and feedback. The associative classi<sup>fi</sup>cation method proposed in this research is capable of mining multi-class information from the need-rating data. It predicts the appeal of the speci<sup>fi</sup>c product to the customer through integrated utilization of information, and the recommendation is meticulous and valuable.

Despite the contribution of this research, there are limitations, and further works can be done. The <sup>fi</sup>rst important work is to investigate the factors that impact a customer's feelings. Many attributes such as the demographic and psychological characteristics, purchase and consumption environment, and customers' expectation, may well have signi<sup>fi</sup>cant in<sup>fl</sup>uence on customers' feelings toward a speci<sup>fi</sup>c product. Therefore, it is crucial to indentify the factors important for modeling rating classi<sup>fi</sup>cation, so as to predict the customer's satisfaction level effectively.

Another work is to elicit customers' needs and preferences. The rating classi<sup>fi</sup>cation aims to recommend the right products based on customers' characteristics to achieve high satisfaction levels. Therefore, the validity of customers' needs and preferences has an important implication on the effectiveness of the recommendation system. Oftentimes consumers do not have clear needs and preferences. Therefore, <sup>fi</sup>nding an effective way to facilitate customers to express their true needs and preferences is essential for the recommendation systems.

## 6. Epilogue

Professor W. W. Cooper, a pioneer researcher in management, has made a signi<sup>fi</sup>cant impact on the <sup>fi</sup>elds of decision sciences, operational research, accounting, marketing, and human resource management. Among his contributions, Professor Cooper has paid much attention to the research in the area of marketing. He developed innovative models to optimize resource allocation for alternative media advertising [5]. In the 1960s, he and his associates built a strategic decision model, DEMON, for marketing new products [6,7]. His idea of creating a decision support system to aid with marketing decision making inspires our pursuit of this research.

Information technologies, especially Internet technology, bring signi<sup>fi</sup>cant in<sup>fl</sup>uence to the traditional marketing environment and changes in the direction of research. As early as 1985, Cooper and his colleagues [8] realized the importance of information technology to marketing research. They argued that researchers and practitioners should handle the “problems that may arise for the relations between marketing management and marketing research because of the rapidly increasing use of personal computers.” Indeed, as the Internet becomes a main part of modern society and online shopping develops into a daily activity, online recommendation systems become ubiquitous and widely utilized by practitioners to improve their revenues. Our research focuses directly on the improvement of recommendation systems.

In investigating the rating classi<sup>fi</sup>cation problem, we follow Dr. Cooper's insights about marketing research. In his opinion, when dealing with decision-making problems under uncertainty, the marketing model should be “simple and intuitive, and easy to understand by both academic researchers and practitioners.” Our research proposed a novel associative classi<sup>fi</sup>cation model to handle the rating classi<sup>fi</sup>cation problem. The proposed model is easy to understand, capable of dealing with uncertainty, and more practical and logical than existing techniques. Therefore, the associative classi<sup>fi</sup>cation model can be understood and used by practitioners straightforwardly. Moreover, the outcome of our research is not limited to only the classi<sup>fi</sup>cation results. According to Dr. Cooper, “simply predicting what will happen in the future is of less interest to managers than knowing what has to be changed, and by how much, to achieve their goals.” This paper follows Professor Cooper's guideline by detecting the probabilities of customers' satisfaction levels beforehand. Such an approach gives the basis for marketers to adopt various marketing strategies to achieve high satisfaction levels. We attribute our recommendation system, with the ultimate goal of marketing online products to maximize customer satisfaction, to Dr. Cooper's pioneering thinking.

## Acknowledgements

The authors thank the editors and two anonymous reviewers for their insightful comments. This work was supported by the National Science Foundation of China (Project No.70672097) and the State Key Program of National Natural Science of China (Project No.70631003).

## References

[1] R. Agrawal, R. Srikant, Fast algorithms for mining association rules in large databases, 20th International Conference on Very Large Data Bases, Santiago, 1994, 1994.

[2] A. Ansari, S. Essegaier, R. Kohli, Internet recommendation systems, Journal of Marketin Research (JMR 37 (3) (2000) 363–375.

[3] A.V. Bodapati, Recommendation systems with purchase data, Journal of Marketing Research (JMR 45 (1) (2008) 77–93.

[4] D.S. Broomhead, D. Lowe, Multivariable functional interpolation and adaptive networks, Complex Systems 2 (1988) 321–355.

[5] A. Charnes, W.W. Cooper, A constrained game formulation of advertising strategies, Econometrica 22 (3) (1954) 511–512.

[6] A. Charnes, W.W. Cooper, J.K. DeVoe, D.B. Learner, Demon: decision mapping via optimum go-no networks-a model for marketing new products, Management Science 12 (11) (1966) 865–887.

[7] A. Charnes, W.W. Cooper, J.K. DeVoe, D.B. Learner, DEMON, Mark II: an extremal equations approach to new product marketing, Management Science 14 (9) (1968) 513–524.

[8] A. Charnes, W.W. Cooper, D.B. Learner, Management science and marketing management, Journal of marketing research 49 (1985) 93–105.

[9] Y. Chen, D. Liginlal, A maximum entropy approach to feature selection in knowledgebased authentication, Decision Support Systems 46 (1) (2008) 388–398.

[10] K.W. Cheung, J.T. Kwok, M.H. Law, K.C. Tsui, Mining customer product ratings for personalized marketing, Decision Support Systems 35 (2) (2003) 231-243

[11] J.A. Chevalier, D. Mayzlin, The effect of word of mouth on sales: online book reviews, Journal of Marketing Research 43 (3) (2006) 345–354.

[12] Y.H. Cho, J.K. Kim, S.H. Kim, A personalized recommender system based on web usage mining and decision tree induction, Expert Systems with Applications 23 (3) (2002) 329–342.

[13] E.K. Clemons, G. Gao, L.M. Hitt, When online reviews meet hyper differentiation: a study of craft beer industry, Journal of Management Information 23 (2) (2006) 149–171.

[14] W.W. Cooper, L.M. Seiford, K. Tone, Data envelopment analysis: a comprehensive text with models, applications, references and DEA-solver software, Kluwer Academic Publishers, Boston, 2000.

[15] C. Dellarocas, The digitization of word of mouth: promise and challenges of online feedback mechanisms, Management Science 49 (10) (2003) 1407–1424.

[16] M. Deshpande, G. Karypis, Item-based top-N recommendation algorithms, ACM Transactions on Information Systems 22 (1) (2004) 143–177.

[17] D. Goldberg, D. Nichols, B.M. Oki, D. Terry, Using collaborative <sup>fi</sup>ltering to weave an information tapestry, Communications of the ACM 35 (12) (1992) 61–70.

[18] J.L. Herlocker, J.A. Konstan, J. Loren, G. Terveen, T. Riedl, Collaborative <sup>fi</sup>ltering recommender systems, ACM Transactions on Information Systems 22 (1) (2004) 5–53.

[19] M.Y. Hu, M. Shanker, G.P. Zhang, M.S. Hung, Modeling consumer situational choice of long distance communication with neural networks, Decision Support Systems 44 (4) (2008) 899–908.

[20] Y. Huang, L. Bian, A Bayesian network and analytic hierarchy process based personalized recommendations for tourist attractions over the Internet, Expert Systems with Applications 36 (1) (2009) 933–943.

[21] L.P. Hung, A personalized recommendation system based on product taxonomy for one-to-one marketing online, Expert Systems with Applications 29 (2) (2005) 383–392.

[22] Y. Kim, W.N. Street, An intelligent system for customer targeting: a data mining approach, Decision Support Systems 37 (2) (2004) 215–228.

[23] J. Konstan, B. Miller, D. Maltz, J. Herlocker, L. Gordon, J. Riedl, GroupLens: applying collaborative <sup>fi</sup>ltering to usenet news, Communications of the ACM 40 (3) (1997) 77–87.

[24] W.M. Li, J.W. Han, J. Pei, CMAR: Accurate and Ef<sup>fi</sup>cient Classi<sup>fi</sup>cation Based on Multiple Class-Association Rules, Proceedings of the 2001 IEEE International Conference on Data Mining, 2001: California 2001.

[25] T.P. Liang, Y.F. Yang, D.N. Chen, Y.C. Ku, A semantic-expansion approach to personalized knowledge recommendation, Decision Support Systems 45 (3) (2008) 401–412.

[26] B. Liu, W. Hsu, Y. Ma, Integrating classi<sup>fi</sup>cation and association rule mining, Proceedings of the Fourth International Conference on Knowledge Discovery and Data Mining (KDD-98), New York, 1998, 1998

[27] Y.Z. Liu, Y.C. Jiang, X. Liu, S.L. Yang, CSMC: a combination strategy for multi-class classi<sup>fi</sup>cation based on multiple association rules, Knowledge-Based Systems 21 (8) (2008) 786–793.

[28] P.M. Murphy, D.W. Aha, UCI Repository machine learning databases 1996, University of California, Irvine, CA, 1996.

[29] D.-H. Park, J. Lee, eWOM overload and its effect on consumer behavioral intention depending on consumer involvement, Electronic Commerce Research and Applications 7 (4) (2008) 386–398.

[30] J.R. Quinlan, C4.5: programs for machine learning, Morgan: Morgan Kaufmann Publishers 1993

[31] R. Rak, L. Kurgan, M. Reformat, A tree-projection-based algorithm for multi-label recurrent-item associative-classi<sup>fi</sup>cation rule generation, Data & Knowledge Engineering 64 (1) (2008) 171–197.

[32] S. Senecal, J. Nantel, The in<sup>fl</sup>uence of online product recommendations on consumers' online choices, Journal of Retailing 80 (2) (2004) 159–169.

[33] M.-D. Shieh, C.-C. Yang, Multiclass SVM-RFE for product form feature selection, Expert Systems with Applications 35 (1–2) (2008) 531–541.

[34] T. Sueyoshi, G.R. Tadiparthi, Agent-Based Approach to Handle Business Complexity in U.S. Wholesale Power Trading, IEEE Transactions on Power System 22 (2) (2007) 532–542.

[35] F. Thabtah, A review of associative classi<sup>fi</sup>cation mining, The Knowledge Engineering Review 22 (1) (2007) 37–65.

[36] F.A. Thabtah, P.I. Cowling, A greedy classi<sup>fi</sup>cation algorithm based on association rule, Applied Soft Computing 7 (3) (2007) 1102–1111.

[37] F. Thabtah, P. Cowling, S. Hammoud, Improving rule sorting, predictive accuracy and training time in associative classi<sup>fi</sup>cation, Expert Systems with Applications 31 (2006) 414–426.

[38] F.H. Wang, H.M. Shao, Effective personalized recommendation based on timeframed navigation clustering and association mining, Expert Systems with Applications 27 (3) (2004) 365–377.

[39] I.H. Witten, E. Frank, in: M. Kaufmann (Ed.), Data Mining: Practical machine learning tools and techniques, 2005, San Francisco.

[40] J.B. Yang, Y.M. Wang, D.L. Xu, et al., The evidential reasoning approach for MADA under both probabilistic and fuzzy uncertainties, European Journal of Operational Research 171 (1) (2006) 309–343.

[41] A. Zenebe, A.F. Norcio, Representation, similarity measures and aggregation methods using fuzzy sets for content-based recommender systems, Fuzzy Sets and Systems 160 (1) (2009) 76–94.

Yuanchun Jiang received his bachelor's degree in management science and engineering from Hefei University of Technology, Hefei, China. He is a PhD student in the Institute of Electronic Commerce in the School of Management at Hefei University of Technology. He is currently a visiting PhD student in the Joseph M. Katz Graduate School of Business at the University of Pittsburgh. His research interests include decision science, electronic commerce, and data mining. He has published papers in journals such as Knowledge-Based Systems, Systems Engineering-Theory & Practice, and Journal of Systems Engineering.

Jennifer Shang received her PhD in Operations Management from the University of Texas at Austin. She teaches operations management, simulation, statistics, and process and quality improvement courses. Her main research interests include multi-criteria decision making and its application to the design, planning, scheduling, control, and evaluation of production and service operational systems. She has published in various journals, including Management Science, Journal of Marketing, European Journal of Operational Research, Decision Support Systems, IEEE Transactions on Engineering Management, and International Journal of Production Research, among others. She has won the EMBA Distinguished Teaching Award and several Excellence-in-Teaching Awards from the MBA/EMBA programs at Katz Business School.

Yezheng Liu is a professor of Electronic Commerce in Hefei University of Technology. Dr. Liu received his PhD in management science and engineering from Hefei University of Technology. He teaches electronic commerce, decision sciences, and information systems. His main research interests include data mining and its application in electronic commerce, decision support systems, and optimization models.

---
otero_id: 4466
otero_key: "SC6WWC7G"
title: "From clicking to consideration: A business intelligence approach to estimating consumers' consideration probabilities"
authors: "Hao Wang; Qiang Wei; Guoqing Chen"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.052"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# From clicking to consideration: A business intelligence approach to estimating consumers' consideration probabilities

Hao Wang, Qiang Wei ⁎, Guoqing Chen

School of Economics and Management, Tsinghua University, Beijing, China

a r t i c l e i n f o

Available online xxxx

Keywords: Electronic commerce Business intelligence Online marketing Consideration probability Collaborative <sup>fi</sup>ltering Latent class model

## a b s t r a c t

With rapid advances in e-commerce applications and technologies, <sup>fi</sup>nding the chance that a product falls into a consumer's consideration set after being inspected (i.e., consideration probability, CP) becomes an important issue of recommendation services and marketing strategies for both academia and practitioners. This paper proposes a novel business intelligence (BI) approach (namely, the two-step estimation approach, TEA) to estimating CPs with a two-step procedure: one is to introduce partial belongings of consumers to the latent classes with both positive and negative preferences (tastes); the other step is to generate CPs based on the degrees of partial belongings in a weighted probability manner. Experiment results from different online shopping scenarios reveal that TEA is effective and outperforms the traditional latent class model.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Considering the costs of search, consumers are often unable to evaluate all products before making purchase decisions [21,28,47]. Therefore, they tend to adopt a consider-then-choose process in which a consumer <sup>fi</sup>rst selects a small group of products as a consideration set (also known as choice set or evoked set) and then chooses one of them to purchase [20,39,56,58,59,63]. For example, when shopping online, a consumer <sup>fi</sup>rst inspects and selects some promising products into a shopping list from recommendations provided by consumer decision support systems (CDSSs, such as search engines or recommender systems), then deeply evaluates these selected products in a comparison matrix (a special type of decision aids that allow consumers to sort products by any attribute in an “products attributes” matrix) to choose the favorite one [16,17,21,63]. The set of products added into the shopping list (comparison matrix) can be viewed as the consideration set which is the output of the <sup>fi</sup>rst stage (consideration stage) and the input of the second stage (choice stage) [7,21,36]. Compared to the process that directly chooses a product from all available ones, the consider-then-choose process is deemed typical and even more rational [23].

Thus, it becomes a primary focus of attention for e-sellers and e-marketplaces to estimating the probability that a product falls into a consumer's consideration set after being inspected, namely, consideration probability (CP) [15,30,39]. Compared with traditional brick-and-mortar stores where the behavior of inspecting is hard to observe and record, e-marketplaces are able to easily trace consumers' clicking behavior which can be seen as a strong signal of inspecting in online shopping [39]. Therefore, “click” and “inspect” are used interchangeably unless otherwise indicated in this paper. Fig. 1 illustrates the consider-then-choose process.

Essentially, CPs play an important role in predicting the chance that a consumer purchases a product after inspecting it, which is referred to as purchasing conversion rate (PCR) or purchasing probability (PP) and attracts numerous research efforts of academia [7,11,13,18,36,39–41,45,52,54,55]. For e-sellers, PPs can help <sup>fi</sup>nd targeted consumers and formulate the pro<sup>fi</sup>t of showing their ads to these targeted consumers [9,18,40,42,54]; and for e-marketplaces, PPs are necessary to effectively rank and recommend sponsored ads for revenue maximization [14,49,62]. From the perspective of the considerthen-choose process, the <sup>fi</sup>nal choice purchased by a consumer must be 1) selected into the consideration set and 2) chosen from the consideration set. Consequently, the PP is equal to the CP multiplied to the choice probability (ChP) that is de<sup>fi</sup>ned as the chance that a product is chosen from a consumer's consideration set, i.e., PP=CP×ChP [15,30,39]. The effectiveness of predicting the PP, therefore, greatly relies on the estimation of the CP. The relationship between PP, CP and ChP is illustrated in Fig. 1.

In addition to predicting PPs, CPs can help e-sellers <sup>fi</sup>nd more targeted consumers which cannot be detected by PPs. Many real business cases indicate that less (more) considering a <sup>fi</sup>rm's products may lead to less (more) experiencing its products and, especially, the improved products [22,23]. In other words, consumers with low CPs to a <sup>fi</sup>rm's products may never want to experience them, even if the <sup>fi</sup>rm's products are greatly improved. The consumers with high

![](/api/attachments/SC6WWC7G/fulltext/images/0e11d380cac720c6b484acdcaa8c346a57b54201269aeda63dc11387e1b3760b.jpg)  
Fig. 1. The consider-then-choose process.

CPs but low PPs, however, would like to experience the improvement of the products, although they choose some other products currently. Therefore, these consumers with high CPs but low PPs to a <sup>fi</sup>rm's products are still targeted consumers, since they may switch to the <sup>fi</sup>rm's products when they experience its improvements [22,23].

Although the roots of related studies about consideration sets and CPs can be traced back to the extensive work in consumer behavior and marketing [27,44,50], there are few studies aiming to directly estimate CPs. One possible reason is that consideration sets are hard to observe without enough technical support from information systems [3,39]. For example, empirical studies usually use surveys to collect the data about consideration sets [10,48], which seemed to be neither ef<sup>fi</sup>cient nor effective [39]. Another reason is that studies on consumer decision making usually treat consideration sets to be latent, not observable, to explain the consumer's purchasing behavior [43,59]. With the rapid advances in e-commerce technologies and applications nowadays, consumers' online behaviors, such as browsing, clicking, comparing, selecting and purchasing, can be recorded more effectively and ef<sup>fi</sup>ciently, which makes consideration sets relatively observable [4,34,39]. For example, it is regarded as a more effective method to use the products clicked by a consumer as an estimation of his or her consideration set than to survey the consumer after purchase [39]. Moreover, with the help of more e-commerce tools, such as the shopping list and comparison matrix, the products added to the shopping list (comparison matrix) for further comparison can be seen as a more appropriate representation of consideration sets [7,21,36].

More observable consideration sets and detailed historical data about consumers' online behavior provide an opportunity for estimating CPs. In this paper, we focus on a general and representative problem: given the products that a consumer has inspected along with the products that have fallen into his or her consideration set, what are the CPs of other non-inspected products to this consumer if they are inspected, i.e., the probabilities that other non-inspected products are selected into the consideration set after being inspected by this consumer? In answering this question, this paper presents a novel two-step approach, in which CPs are effectively estimated. The paper is organized as follows. The problem is de<sup>fi</sup>ned in Section 2. Related studies and their limitations are discussed in Section 3. The proposed approach is presented in Section 4. Section 5 illustrates experimental results as well as the analysis. The conclusion is provided in the last section.

## 2. Problem de<sup>fi</sup>nition

Formally, the research question is stated as follows. A consumer, $c \in C$ (C is the set of all consumers), wants to select several products as his or her consideration set from recommended products, S. Let S (<sup></sup>S ) denote the set of inspected (non-inspected) products for consumer c, where $\bar { S } _ { c } = S { - } S _ { c }$ . Let $a _ { c s }$ be a binary variable with $a _ { c s } = 1 ~ ( a _ { c s } = 0 )$ <sup>¼</sup>denoting that product s is (is not) in the consideration set of consumer c after being inspected, where the values of $a _ { c s }$ are supposedly known for s in $S _ { c }$ and unknown for s in ${ \bar { S } } _ { c } .$ . Then the research question is to estimate $\mathrm { P r } ( a _ { c s } = 1 )$ , ∀s∈<sup></sup>S based on the historical data about all consumers' inspected products and their consideration sets.

For example, suppose that a consumer c∈C wants to select several laptop computers into the comparison matrix for further evaluation at an e-marketplace. The recommendations provided by CDSSs are 4 different computers, $\mathrm { i . e . , } S = \{ s _ { 1 } , s _ { 2 } , s _ { 3 } , s _ { 4 } \}$ . At the time of $t _ { 0 } ,$ c has inspected no computer $( \mathrm { i . e . , } S _ { c } { = \{ \} } , \bar { S } _ { c } { = \{ S _ { 1 } , S _ { 2 } , S _ { 3 } , S _ { 4 } \} }$ and all $\boldsymbol { a } _ { c s } ^ { } { \cdot } \boldsymbol { s }$ are unknown). <sup>¼ f g</sup>That is, the task is to estimate all computers' CPs (i.e., $\mathrm { P r } ( a _ { c s } = 1 )$ $\forall s \in \{ s _ { 1 } , s _ { 2 } , s _ { 3 } , s _ { 4 } \} \}$ ). Suppose that at the time of $t _ { 1 } , c$ inspects computer $s _ { 1 }$ and adds it into the comparison matrix $( \mathrm { i . e . , } S _ { c } { = } \{ s _ { 1 } \} , \bar { S } _ { c } { = } \{ s _ { 2 } , s _ { 3 } , s _ { 4 } \}$ $a _ { c s _ { 1 } } = 1$ and the values of $a _ { c s }$ are unknown $\forall s \in \{ s _ { 2 } , s _ { 3 } , s _ { 4 } \} \}$ <sup>¼ f g</sup>). Then, what <sup>¼</sup>needs to be done is to estimate all non-inspected computers' CPs (i.e., $\operatorname* { P r } ( a _ { c s } = 1 ) , \forall s \in \{ s _ { 2 } , s _ { 3 } , s _ { 4 } \} )$ ). If at the time of $t _ { 2 } ,$ c inspects product s but does not add it into the comparison matrix (i.e., $S _ { c } = \{ s _ { 1 } , s _ { 3 } \}$ $\bar { S } _ { c } = \{ s _ { 2 } , s _ { 4 } \} , a _ { c s _ { 1 } } = 1 , a _ { c s _ { 3 } } = 0$ and the values of $a _ { c s }$ are unknown $\forall s \in \{ s _ { 2 } , s _ { 4 } \} )$ <sup>g</sup>, then $\mathrm { P r } ( a _ { c s } = 1 )$ <sup>¼</sup>needs to be estimated for the remaining products, i.e., ∀s∈ {s ,s }. If at the time of $t _ { 3 } ,$ c inspects product s and adds it into the comparison matrix $( { \mathrm { i . e . , ~ } } S _ { c } { = } \{ s _ { 1 } , s _ { 2 } , s _ { 3 } \} , ~ \bar { S } _ { c } = \{ s _ { 4 } \}$ $a _ { c s _ { 1 } } = 1 , a _ { c s _ { 2 } } = 1 , a _ { c s _ { 3 } } = 0 ,$ , and the value of $a _ { c s }$ is unknown $\forall s \in \{ s _ { 4 } \} )$ $\mathrm { P r } ( a _ { c s } = 1 )$ <sup>¼ ¼</sup>needs to be estimated $\forall s \in \{ s _ { 4 } \}$ . This process is illustrated in Table 1.

The search process of consumer c.

<table><tr><td>Time</td><td>Non-inspected products</td><td>Inspected products</td><td>Consideration set</td></tr><tr><td> $t_0$ </td><td> $s_1, s_2, s_3, s_4$ </td><td></td><td></td></tr><tr><td> $t_1$ </td><td> $s_2, s_3, s_4$ </td><td> $s_1$ </td><td> $s_1$ </td></tr><tr><td> $t_2$ </td><td> $s_2, s_4$ </td><td> $s_1, s_3$ </td><td> $s_1$ </td></tr><tr><td> $t_3$ </td><td> $s_4$ </td><td> $s_1, s_2, s_3$ </td><td> $s_1, s_2$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

Please cite this article as: H. Wang, et al., From clicking to consideration: A business intelligence approach to estimating consumers' consideration probabilities, Decision Support Systems (2012), http://dx.doi.org/10.1016/j.dss.2012.10.052

As mentioned previously, the estimated CPs can be used by e-marketplaces and e-sellers to rearrange their ads as well as by consumers to inspect better products. For instance, suppose that the estimated $\mathrm { P r } ( a _ { c s _ { 3 } } = 1 )$ is 0.1 at the time of t (i.e., after consumer c inspected product $s _ { 1 }$ and added it into the comparison matrix). Since customer c may think that the probability 0.1 is not high, it is quite likely that, after being inspected, product $s _ { 3 }$ will not fall into the consideration set of consumer c. In this way, with the help of such estimation, the e-marketplace and e-seller may remove product $s _ { 3 }$ from recommended products or rearrange the non-inspected products so as to achieve a better service/marketing strategy. On the other hand, the consumer may consider skipping product s<sub>3</sub> and tend to inspect other products with higher estimated CPs.

Since $\bar { S } _ { c } = S - S _ { c } , ~ S _ { c } = \{ s | a _ { c s } = 0 \} + \{ s | a _ { c s } = 1 \}$ and $\bar { S } _ { c } = \{ | s | a _ { c s }$ is <sup>¼ ¼ fj j</sup>unknown , it is convenient to express this process by only using the values of $a _ { c s } .$ Table 2 illustrates this expression where unknown $a _ { c s }$ value (null) means that the product has not been inspected $( \mathrm { i } . \mathsf { e } . , \forall s \in \bar { S } _ { c } )$ . In other words, given any time t, the research task is to estimate $\mathrm { P r } ( a _ { c s } = 1 )$ where $a _ { c s }$ is unknown.

When estimating CPs at the time of t, the available information includes all consumers' inspected products $( S _ { c } , \ \forall c \in C )$ and consideration sets $( \{ s | a _ { c s } = 1 \}$ , ∀s∈S) at the point of time t. Furthermore, consider an example with multiple customers and multiple products. Suppose that $C = \{ c _ { 1 } , c _ { 2 } , c _ { 3 } \}$ and their search processes for $S = \{ s _ { 1 } , s _ { 2 } , s _ { 3 } \}$ s }are recorded in historical data exempli<sup>fi</sup>ed in Table 3. By the time of $t , c _ { 1 }$ has inspected all computers and added $s _ { 1 }$ and $s _ { 3 }$ into the comparison list, $c _ { 2 }$ has inspected computers $s _ { 1 } , s _ { 3 }$ and $s _ { 4 } ,$ and added $s _ { 1 }$ and s into the comparison list, and $c _ { 3 }$ has inspected computers $s _ { 1 } , s _ { 2 } ,$ and $s _ { 3 } ,$ and added $s _ { 1 }$ and $s _ { 2 }$ into the comparison list. Thus, Table 3 re<sup>fl</sup>ects the available information for estimating $\mathrm { P r } ( a _ { c _ { 3 } s _ { 4 } } = 1 )$ at the time of t.

## 3. Related work

Studies about CPs can be classi<sup>fi</sup>ed into two areas according to their research motivations: explaining consumer behavior and predicting consumer behavior. In the <sup>fi</sup>rst research area, relevant studies focus on <sup>fi</sup>nding models that can describe and explain consumers' decision processes [3,22,30,34,43,47,59]. The models, usually built on rational choice theory, utilize all available information, such as products' attributes, consumers' characteristics, shopping time, etc., and consider all possible outcomes to formulate the process of purchasing. Although empirical studies show that these models can explain consumer behavior to some extent [6,22,30,43,47], there are still some limitations to directly use these models to estimate CPs. First, since CPs are not included in the metrics to evaluate the performance of the models in these studies, the accuracy of the estimation of CPs is not well guaranteed. Second, some models' complexity increases dramatically when more information is considered [10,39].

In the second research area, closely related to business intelligence (BI), relevant studies aim to predict the action taken by a consumer on a product (e.g., browsing, purchasing, rating, etc.), based on his or her historical actions for other products. These methods include Markov process (MP), association rule (AR) and collaborative <sup>fi</sup>ltering (CF) [5,32,33,35,38,46,53]. Compared to MP and AR, CF is regarded more effective and ef<sup>fi</sup>cient, and therefore widely studied and adopted by

Table 2  
The search process of consumer c expressed by $a _ { c s } .$

<table><tr><td></td><td> $s_1$ </td><td> $s_2$ </td><td> $s_3$ </td><td> $s_4$ </td></tr><tr><td> $t_0$ </td><td></td><td></td><td></td><td></td></tr><tr><td> $t_1$ </td><td>1</td><td></td><td></td><td></td></tr><tr><td> $t_2$ </td><td>1</td><td></td><td>0</td><td></td></tr><tr><td> $t_3$ </td><td>1</td><td>1</td><td>0</td><td></td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

## Table 3

The available information for CP estimation at the time of t.

<table><tr><td></td><td> $s_1$ </td><td> $s_2$ </td><td> $s_3$ </td><td> $s_4$ </td></tr><tr><td> $c_1$ </td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td> $c_2$ </td><td>1</td><td></td><td>0</td><td>1</td></tr><tr><td> $c_3$ </td><td>1</td><td>1</td><td>0</td><td></td></tr></table>

researchers and businesses these days [2,57]. For example, CF is the prime method for top teams in the Net<sup>fl</sup>ix Prize contest [29].

Generally speaking, CF methods are to estimate a consumer's rating (in a scale of 1-K, K is an integer larger than 1) on a product (i.e., $r _ { c s } { \in } \{ 1 , 2 , . . . . , K \} )$ , given a matrix of consumers' ratings on products (i.e., $\{ r _ { c s } \} _ { C \times S } ) \ [ 2 ]$ . Most CF methods focus on the point estimation instead of the probability distribution estimation, i.e., estimating $r _ { c s }$ instead of $\operatorname* { P r } ( r _ { c s } = i ) , i \in \{ 1 , 2 , . . . K \}$ . Considering that our research question is to estimate $\operatorname* { P r } ( a _ { c s } = 1 ) , \forall s \in \bar { S } _ { c }$ , which is a probability distribution estimation, the related CF methods narrow down to the latent class model (LCM) [24–26].

LCM assumes that 1) consumers belong to different groups, namely, latent classes, according to their preferences (tastes) on the products; 2) consumers in the same group have similar preferences, which means that their ratings on the same product obey the same probability distribution; and 3) given the consumer's latent class, his or her ratings on non-inspected products can be seen as independent variables. Therefore, the probability of $r _ { c s } = i , i \in \{ 1 , 2 , . . . , K \}$ is calculated as

$$
\operatorname * {P r} ^ {\mathrm{LCM}} \left(r _ {c s} = i\right) = \sum_ {g \in G} \operatorname * {P r} (c \in g) \times \operatorname * {P r} \left(r _ {c s} = i \mid c \in g\right)\tag{1}
$$

where $\mathrm { P r } ^ { \mathrm { L C M } } ( r _ { c s } = i )$ is the probability that $r _ { c s } = i$ estimated by LCM, G is the set of all latent classes, g is one latent class in $G , \operatorname* { P r } ( c \in g )$ is the probability that consumer c belongs to the latent class g and $\operatorname* { P r } ( r _ { c s } = i | c \in g )$ is the probability that $r _ { c s } = i$ given that consumer c belongs to the latent class g.

It is worth mentioning that a consumer's rating distribution on a product can also be estimated by grouping “similar” products, i.e., estimating ratings from user-based to product-based [8,51]. Mathematically, if the rating matrix $\{ r _ { c s } \} _ { C \times S }$ is transposed, all product-based methods can be converted to user-based methods [1,29]. Notably, the proposed approach is of the user-based nature.

However, the limitation of LCM results from its assumptions which neglect the differences between consumers in the same latent class and the similarities between consumers in different latent classes. Given these assumptions, consumers near the “edge” of a class are viewed as the same to the consumers near the “core,” which may not be so reasonable. It is highly possible that a consumer near the “edge” of a class is more similar to his or her neighboring consumers in different classes than the consumers near the “core” of his or her own class. For example, Fig. 2 illustrates this situation. In this case, consumers (denoted by dots in a two-dimension positioning map [15]) are grouped as two different latent classes (denoted by red and blue). Consumer A, the “edge” point of the red class, is much closer to Consumer B (a consumer in the blue class) than to Consumer C (the “core” of the red class).

Thus, the above-mentioned assumptions may easily lead to some distortions in consumer treatment, which may further decrease the performance of CP estimation in LCM.

## 4. A two-step estimation approach

As mentioned in the previous section, neither the differences between consumers in the same class nor the similarities between consumers in different classes shall be negligible, especially for those large and sparse classes. However, directly adding these “differences” and “similarities” to LCM is dif<sup>fi</sup>cult, since it violates the basic assumptions on which LCM is built, thereby losing the good properties for estimating probability distribution. In this regard, we aim to develop a two-step estimation approach (TEA) to cope with the problem in estimating $\mathrm { P r } ( a _ { c s } = 1 )$ , ∀s∈<sup></sup>S . Brie<sup>fl</sup>y, <sup>fi</sup>rst, an enhanced latent class model (ELCM) is developed to estimate the degree that consumer c prefers product s, i.e., $d _ { c s } ( d _ { c s } \in [ 0 , 1 ] )$ ). Then, a generation operation, h, is built to derive CPs using the estimated degrees, i. $\mathrm { \mathrm { ? } } , \operatorname* { P r } ^ { \mathrm { \hat { T } E A } } ( a _ { c s } = 1 ) =$ $h ( d _ { c s } )$ , where $\mathrm { P r } ^ { \mathrm { T E A } } ( a _ { c s } = 1 )$ is the estimation of $\mathrm { P r } ( a _ { c s } = 1 )$ by TEA. This generation operation is based upon the probability ranking principle, signal detection-decision theory and utility theory [19]. The process is illustrated in Fig. 3.

![](/api/attachments/SC6WWC7G/fulltext/images/8bc710c102cd5af5c6d7100366f1e0af1a19e705f66b0891969bd3730c5774af.jpg)  
Fig. 2. The distance between the “core” and “edge” consumers in the same class may be larger than the distance between two consumers in different classes when using the method of LCM.

## 4.1. Enhanced latent class model

As discussed above, a soft classi<sup>fi</sup>cation of consumers may better <sup>fi</sup>t for grasping consumers' preferences. In addition, the “neighborhood” of a consumer can also provide useful information even though they belong to different classes. Given this, we assume that there exists a set of classes, $G ,$ which represent various types of consumers. Differently from LCM, a consumer in ELCM can belong to more than one class with different membership degrees, i.e., classes can overlap with each other in light of partial belongings. The membership degree that consumer c belongs to class g $( g { \in } G )$ is denoted by $m _ { \mathrm { g } } ( c ) ( m _ { \mathrm { g } } ( c ) \in [ 0 , 1 ] )$ , where $m _ { g }$ is the membership function determined by class g. Given these latent classes and the corresponding membership functions, the degree that consumer c considers product s, $d _ { c s } ( d _ { c s } \in [ 0 , 1 ] )$ ), can be estimated by Eq. (2):

$$
d _ {c s} = \frac {\sum_ {g \in G} m _ {g} (c) \times d _ {c s g}}{\sum_ {g \in G} m _ {g} (c)}\tag{2}
$$

where $d _ { c s g }$ is the estimation of $d _ { c s }$ by class g.

Eq. (2) indicates that ELCM is more generalized than LCM, in that Eq. (2) degenerates to Eq. (1) when $r _ { c s } = a _ { c s } + 1 , \ K = 2 , \ m _ { g } ( c ) =$ $\mathrm { P r } ( c \in g ) , d _ { c s g } = \mathrm { P r } ( a _ { c s } | c \in g )$

In contrast to LCM where latent classes need to be predetermined by clustering consumers into different groups, ELCM uses each consumer to represent a latent class which well re<sup>fl</sup>ects his or her preference, i.e., the membership degree is 1. Formally, for any consumer, say, consumer $c ,$ he or she represents a latent class, say, class $g _ { c } ,$ to which the consumer's membership degree is 1, i.e., $m _ { g _ { c } } ( c ) = 1$ . The set of latent classes used by ELCM is $G = \{ g _ { c } | c \in C \}$

Given these latent classes, $d _ { c s }$ can be estimated by

$$
d _ {c s} = \frac {\sum_ {y \in C} m _ {g _ {y}} (c) \times d _ {c s g _ {y}}}{\sum_ {y \in C} m _ {g _ {y}} (c)}\tag{\( (2') \}
$$

Prior to formulating speci<sup>fi</sup>c details of $m _ { g _ { v } } ( c )$ and $d _ { c s g _ { y } }$ , two important issues should be considered. In Eq. $( 2 ^ { \prime } ) , d _ { c s g _ { y } }$ is the estimation of

$$
a _ {c s} \xrightarrow {\text { Enhanced   Latent   Class   Model }} d _ {c s} \xrightarrow {\text { Generating }} \operatorname * {P r} ^ {T E A} \left(a _ {c s} = 1\right)
$$

Fig. 3. The process of TEA

Please cite this article as: H. Wang, et al., From clicking to consideration: A business intelligence approach to estimating consumers' consideration probabilities, Decision Support Systems (2012), http://dx.doi.org/10.1016/j.dss.2012.10.052

$d _ { c s }$ made by class $g _ { y }$ and $m _ { g _ { v } } ( c )$ serves as the weight of $d _ { c s g _ { v } }$ , which re-<sup>ð Þfl</sup>ects the con<sup>fi</sup>dence of the estimation (i.e., larger $m _ { g _ { v } } ( c )$ means more con<sup>fi</sup>dence of $d _ { c s g _ { \nu } }$ , vice versa). Therefore, $m _ { g _ { v } } ( c )$ <sup>ð Þ</sup>should be consistent <sup>ð Þ</sup>with the con<sup>fi</sup>dence of the estimation when designing it. The other issue is that since $\{ a _ { c s } \} _ { C \times S }$ is quite sparsely <sup>fi</sup>lled in real world applications [2,29], it is deemed effective and meaningful to take into account all available information in $\{ a _ { c s } \} _ { C \times S } ,$ including the negative pieces [60]. That is, we design $m _ { g _ { v } } ( c )$ and $d _ { c s g _ { \nu } }$ using both positive and negative preferences (tastes) re<sup>fl</sup>ected by $\{ a _ { c s } \} _ { C \times S } .$ Considering the two issues above, we introduce a new notion, namely, dual consumer, to help design $m _ { g _ { v } } ( c )$ and $d _ { c s g _ { y } }$

De<sup>fi</sup>nition 1. Given a consumer, $c \in C ,$ the dual consumer $c ^ { * }$ of c is a consumer who has the total preference opposite to $c \ ( \mathrm { i . e . , } \ S _ { c ^ { * } } = S _ { c } ,$ $\bar { S } _ { c ^ { * } } = \bar { S } _ { c }$ <sub>c</sub> and $a _ { c s } = 1 - a _ { c ^ { * } s } , \ \forall s \in S _ { c } )$ <sup>¼</sup>. The dual consumer set of C is $C ^ { \ast } = \{ c ^ { \ast } | S _ { c ^ { \ast } } = S _ { c } , \bar { S } _ { c ^ { \ast } } = \bar { S } _ { c } , a _ { c s } = 1 - a _ { c ^ { \ast } s } , \forall s \in S _ { c } \}$

<sup>¼ ¼ ¼ ¼</sup>Here, merely as a design setting, a dual consumer can be either physical or virtual, who may or may not belong to C. As an example, Table 4 illustrates the dual consumer set of the consumer set in Table 3,

In ELCM, $m _ { g _ { v } } ( c )$ and $d _ { c s g _ { \nu } }$ are in<sup>fl</sup>uenced by consumer y, consumer c <sup>ð Þ</sup>and the dual consumer $c ^ { * }$ . Let ϕ(x,y) denote the similarity between x and $y ,$ for $x { \in } \{ c , c ^ { * } \}$ . Then, $m _ { g _ { y } } ( c )$ and $d _ { c s g _ { y } }$ are:

$$
m _ {g _ {y}} (c) = \left\{ \begin{array}{l l} 0 & \text { if   } a _ {y s} \text {   is   unknown } \\ | \phi (c, y) - \phi (c ^ {*}, y) | & \text { otherwise } \end{array} \right.\tag{3}
$$

$$
d _ {c s g _ {y}} = \left\{ \begin{array}{l l} a _ {y s} & \text { if } | \phi (c, y) | > | \phi (c ^ {*}, y) | \\ 1 - \alpha_ {y s} & \text { otherwise } \end{array} \right.\tag{4}
$$

Eqs. (3) and (4) mean that 1) the consumers who have not yet inspected product s $( a _ { y s }$ is unknown) are neglected when estimating the degree that consumer c may consider s and 2) for the consumers who have inspected product s, the meaning of $m _ { g _ { v } } ( c )$ is that the con<sup>fi</sup>- dence of the estimation of $d _ { c s }$ made by class $g _ { \mathrm { y } }$ <sup>ð Þ</sup>is low if class $g _ { \mathrm { y } }$ cannot distinguish c from $c ^ { * } ,$ i.e., both c and $c ^ { * }$ have the similar membership degree to class $g _ { \mathrm { y } } .$ For $d _ { c s g _ { y } }$ , the estimation of $d _ { c s }$ from class $g _ { \mathrm { y } }$ is similar with (opposite to) $a _ { y s }$ if consumer c is similar with (opposite to) consumer y.

As for ϕ(x,y) ∀x∈{c,c\*}, i.e., the similarity between x and y, there are available measures to consider [2]. One point of concern is that the similarity between two consumers is only related to the products they all inspected and should not be in<sup>fl</sup>uenced by the products that only one of them has inspected. Let $\mathsf { S c i } = \{ s | s \in S _ { c }$ and $a _ { c s } = i \}$ and |A| denote the number of elements of set A. Then, ϕ(x,y) in ELCM is:

$$
\phi (x, y) = \left\{ \begin{array}{l l} \frac { \sum_ {i = 0} ^ {1} \left| S _ {x} ^ {i} \cap S _ {y} ^ {i} \right|}{\left| S _ {x} \cap S _ {y} \right|} & i f \left| S _ {x} \cap S _ {y} \right| \neq 0, f o r x \in \{c, c ^ {*} \} \\ 0 & o t h e r w i s e \end{array} \right.\tag{5}
$$

In $\mathsf { E q . } ( 5 ) , S _ { x } \cap S _ { y }$ denotes the products that are inspected by both x and $y ,$ and $\Vec { | S _ { x } ^ { 1 } \cap S _ { y } ^ { 1 } | } ~ ( \Vec { | S _ { x } ^ { 0 } \cap S _ { y } ^ { 0 } | } )$ denotes the products that fall (do not fall) into the consideration sets of both x and y after being inspected by both. From the perspective of consideration set, $| S _ { x } ^ { 1 } \cap S _ { y } ^ { 1 } | ( | \bar { S } _ { x } ^ { 0 } \cap \hat { S } _ { y } ^ { 0 } | )$ ) re-<sup>fl</sup>ects the preferences of x and y. $\vert S _ { x } ^ { 1 } \cap S _ { y } ^ { 1 } \vert \left( \vert S _ { x } ^ { 0 } \cap S _ { y } ^ { 0 } \vert \right)$ is the set of products that both x and y like (dislike). Sinc $\cdot \sum _ { i = 0 } ^ { 1 } \left| S _ { x } ^ { i } \cap S _ { y } ^ { i } \right| \leq \left| S _ { x } \cap S _ { y } \right| , \mathrm { t h e } \frac { \sum _ { i = 0 } ^ { 1 } \left| S _ { x } ^ { i } \cap S _ { y } ^ { i } \right| } { \left| S _ { x } \cap S _ { y } \right| }$ represents the similarity between x and y.

Table 4  
The dual consumer set of the consumer set in Table 3.

<table><tr><td></td><td> $s_1$ </td><td> $s_2$ </td><td> $s_3$ </td><td> $s_4$ </td></tr><tr><td> $c_1^*$ </td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td> $c_2^*$ </td><td>0</td><td></td><td>1</td><td>0</td></tr><tr><td> $c_3^*$ </td><td>0</td><td>0</td><td>1</td><td></td></tr></table>

Next, to exemplify how ELCM works, we consider the problem proposed in Section 2, i.e., estimatingPr $( a _ { c _ { 3 } s _ { 4 } } = 1 )$ given the available infor-<sup>¼</sup>mation in Table 3. Concretely, the process of estimating $d _ { c _ { 3 } s _ { 4 } }$ in Table 3 is described as follows:

Please cite this article as: H. Wang, et al., From clicking to consideration: A business intelligence approach to estimating consumers' consideration probabilities, Decision Support Systems (2012), http://dx.doi.org/10.1016/j.dss.2012.10.052

$$
\begin{array}{l} 1) S _ {c _ {3}} ^ {0} = \{s _ {3} \}, S _ {c _ {3}} ^ {1} = \{s _ {1}, s _ {2} \}, S _ {c _ {3} ^ {*}} ^ {0} = \{s _ {1}, s _ {2} \}, S _ {c _ {3} ^ {*}} ^ {1} = \{s _ {3} \}, S _ {c _ {1}} ^ {0} = \{s _ {2}, s _ {4} \}, S _ {c _ {1}} ^ {1} = \\ \{s _ {1}, s _ {3} \}, S _ {c _ {2}} ^ {0} = \{s _ {3} \}, S _ {c _ {2}} ^ {1} = \{s _ {1}, s _ {4} \} \\ 2) \phi (c _ {3}, c _ {1}) = 1 / 3, \phi (c _ {3} ^ {*}, c _ {1}) = 2 / 3, \phi (c _ {3}, c _ {2}) = 1, \phi (c _ {3} ^ {*}, c _ {2}) = 0 \\ 3) m g _ {c _ {1}} (c _ {3}) = | \phi (c _ {3}, c _ {1}) - \phi (c _ {3} *, c _ {1}) | = 1 / 3, m g _ {c _ {2}} (c _ {3}) = | \phi (c _ {3}, c _ {2}) - \phi (c _ {3} *, c _ {2}) | = 1 \\ 4) d _ {c _ {3} s _ {4} g _ {c _ {1}}} = 1 - a _ {c _ {1} s _ {4}} = 1, d _ {c _ {3} s _ {4} g _ {c _ {2}}} = a _ {c _ {2} s _ {4}} = 1 \\ 5) d _ {c _ {3} s _ {4}} = 1 \end{array}
$$

## 4.2. Generating CPs

This section discusses the way to estimate CP based on $d _ { c s } .$ . Let $\operatorname* { P r } ( a | d )$ denote the probability that the real value is a given that estimated degree by ELCM is d. For example, $\operatorname* { P r } ( a = 1 | d = 0 . 3 ) = 0 . 4$ means that the probability that a consumer will consider a product is 0.4, given that the estimated degree by ELCM is 0.3. In TEA, $\operatorname* { P r } ( a = 1 | d = d _ { c s } )$ could be used as the estimation of Pr $( a _ { c s } = 1 )$ , i.e., $\mathrm { P r } ^ { \mathrm { T E A } } ( a _ { c s } = 1 ) =$ $\mathrm { P r } ( a = 1 | d = d _ { c s } ) ,$ , where $\operatorname* { P r } ( a = 1 | d = d _ { c s } )$ is the probability that $a = 1$ if its corresponding d estimated by TEA is $d _ { c s } .$ . Related studies <sup>fi</sup>nd that Pr(d|a=1) and $\operatorname* { P r } ( d | a = 0 )$ obey the normal and exponential distributions, respectively [61]. Therefore, the distribution functions of Pr(d| $a = 0 )$ and $\Pr ( d | a = 1 )$ , namely, f (d) and $f _ { 1 } ( d )$ , can be formulated as $\begin{array} { r } { f _ { 1 } ( d ) = \frac { 1 } { \sqrt { 2 \pi } \sigma _ { d } } e ^ { - \frac { \left( d - \mu _ { d } \right) ^ { 2 } } { 2 \sigma _ { d } ^ { 2 } } } } \end{array}$ and $f _ { 0 } ( d ) = \lambda _ { d } e ^ { - \lambda _ { d } ( d - z _ { d } ) }$ , where $\sigma _ { \mathrm { d } } , \mu _ { \mathrm { d } } , \lambda _ { \mathrm { d } }$ and $z _ { \mathrm { d } }$ are parameters estimated from historical data. Others, such as the proportion of considered products to unconsidered products $( \mathrm { i . e . , } \frac { \mathrm { P r } ( a = 0 ) } { \mathrm { P r } ( a = 1 ) } )$ can also be estimated from historical data.

Therefore, $\mathrm { P r } ^ { \mathrm { T E A } } ( a _ { c s } = 1 )$ ) can be calculated as

$$
\operatorname * {P r} ^ {\mathrm{TEA}} \left(a _ {c s} = 1\right) = \operatorname * {P r} (a = 1 | d = d _ {c s}) = \frac {f _ {1} \left(d = d _ {c s}\right)}{f _ {0} \left(d = d _ {c s}\right) \frac {\operatorname* {P r} (a = 0)}{\operatorname* {P r} (a = 1)} + f _ {1} \left(d = d _ {c s}\right)}\tag{6}
$$

where $d _ { c s }$ is estimated from Eq. (2′).

## 5. Experiments

In order to demonstrate the effectiveness of the proposed approach, some experiments have been conducted. In this section we <sup>fi</sup>rst construct the datasets, which represent different types of marketing scenarios, and then apply TEA and LCM to these datasets for comparative purposes.

## 5.1. Experimental settings

Related literature uses ideal points in an N-dimensional space, namely, positioning map, to represent consumers (products) [12,15,37]. It <sup>fi</sup>nds that consumers (products) could be grouped into different classes (market segments) according to their characteristics. The consumers (products) from the same segments can be viewed as i.i.d. random variables drawn from some distribution; consumers (products) from different segments are independent. For the sake of convenience, N usually equals two and the probability distributions usually are assumed to be normally distributed.

The positioning map can effectively represent a variety of real scenarios [15]. For example, Figs. 4 and 5 illustrate the scenarios where all consumers (products) belong to one and two segment(s). Since the products are developed for the target consumers, for each segment of consumers there may be a segment of corresponding products around the same place on the positioning map to satisfy these consumers' needs. In this paper, therefore, consumers and products are assumed to have the same segments, obeying the same distribution in each segment.

![](/api/attachments/SC6WWC7G/fulltext/images/69b6f97d8f20bb727c864968c79733af4233fce0df71c411eafb42f590c3a03a.jpg)  
Fig. 4. Positioning map of one segment of consumers (products).

Given the positioning map, the probability that non-inspected product s falls into the consideration set of consumer c after being inspected can be modeled as [15]:

$$
\operatorname * {P r} (a _ {c s} = 1) = e ^ {- d i s _ {c s} ^ {2} / \theta}\tag{7}
$$

![](/api/attachments/SC6WWC7G/fulltext/images/4b4fb33173b6f87a98911a9088088b471f3b871600f1a980353b830ea0619a80.jpg)  
Fig. 5. Positioning map of two segments of consumers (products).

where dis is the distance between the two points on the map, and θ (namely, decay rate) determines how fast the probability decays with distance. Existing literature shows that θ is around 0.4 [15]. Figs. 6 and 7 illustrate the contour lines of the probabilities that a product falls into the consideration set of the consumer at the origin when $\theta { = } 0 . 4 .$ . The probabilities are 0.001, 0.01, 0.1, 0.5 and 0.9, decreasing with the distances between the products and the consumer at the origin.

Positioning map and decay rate effectively simulate the consumers' preferences on products. Given a positioning map and a decay rate, the probability that a non-inspected product s falls into the consideration set of consumer c after being inspected can be simulated by Eq. (7).

In addition to positioning map and decay rate, the average percentage of inspected products may also affect the accuracy of estimation, since higher percentage of inspected products means more information available about the consumers' preferences.

Parameters and notations that are used to generate positioning map, decay rate and percentage of inspected products are detailed in the appendix. It is worth noting that these parameters and their ranges are consistent with other related studies [15,18,22,31,47].

## 5.2. Experimental procedure

Three most important parameters that may affect the performances of the methods LCM and TEA are: the number of segments in positioning map, $N _ { S G }$ the decay rate, θ, and the percentage of products that each consumer has inspected on average, per. A tuple $( N _ { \mathrm { S G } } , \theta , \mathsf { p e r } )$ simulates a type of online shopping scenario. Existing studies indicate that $N _ { S G }$ is usually less than 8, θ is around 0.4 and per is about $1 0 \% [ 1 5 , 1 8 , 3 1 ] .$ . In order to effectively validate the proposed approach, we compared LCM and TEA under a wide range of settings for $( N _ { \mathrm { S G } } , \theta , \mathsf { p e r } )$ with various values: $N _ { \mathrm { S G } } { \in } \{ 1 , 2 , 4 , 8 \} , { \theta } { \in } \{ 0 . 1 , 0 . 2 , 0 . 3 , 0 . 4 , 0 . 5 , 0 . 6 , 0 . 7 , 0 . 8 , 0 . 9 , 1 . 0 \}$ and per $\in \{ 5 \% , 1 0 \% , 1 5 \% , 2 0 \% \}$ . Thus, there were 4 $\times 1 0 \times 4 = 1 6 0$ different values of tuple $( N _ { \mathrm { S G } } , \theta , \mathsf { p e r } )$ , representing 160 online shopping scenarios. For each value of the tuple $( N _ { \mathrm { S G } } , \ \theta ,$ per), 100 positioning maps (PMs) were generated, resulting in 16000 datasets in total. For each consumer, per percent of products were randomly chosen to be inspected by him or her. When a product s was inspected by a consumer $c , \mathrm { i } . \mathbf { e } . , s { \in } S _ { c } , a _ { c s }$ was known and the value was determined by the following equation:

$$
a _ {c s} = \left\{ \begin{array}{l l} 1 & \text { if } e ^ {- \mathrm{dis} _ {c s} ^ {2} / \theta} > p \\ 0 & \text { otherwise } \end{array} \right.\tag{8}
$$

where p obeys a standard uniform distribution.

Given each positioning map, 60% of consumers were randomly chosen to constitute training set $C _ { \mathrm { t r } }$ and the rest 40% of consumers were composed of testing set $C _ { \mathrm { t e } } .$ Training set is used to tune the estimation methods and testing set is used to compare the performances of estimation methods. For each consumer in the test, the task is to estimate the CPs of the rest non-inspected products, $\mathrm { i . e . , }$ , estimating $\mathrm { P r } ( a _ { c s } = 1 )$ for $c { \in } C _ { \mathrm { t e } }$ and $s { \in } \bar { S } _ { c } \ ( \mathrm { i . e . , } a _ { c s }$ is unknown).

Two estimation methods, TEA and LCM, were compared in the experiments. TEA has been detailed in Section 3. For LCM, we assume that all the segments of consumers (products) are known to LCM and use the segments as the latent classes of LCM. Therefore,

$$
\operatorname * {P r} ^ {\mathrm{LCM}} \left(a _ {c s} = 1\right) = \frac {\sum_ {c ^ {\prime} \in g _ {c} \cap C _ {\mathrm{tr}}} a _ {c ^ {\prime} s}}{\left| g _ {c} \cap C _ {\mathrm{tr}} \right|}\tag{9}
$$

for $c { \in } C _ { \mathrm { t e } }$ and $s { \in } \bar { S } _ { c } ,$ , where g is the segment to which consumer c belongs. Compared to $\mathtt { E q . } \left( 1 \right)$ where $g _ { c }$ is uncertain, $g _ { c }$ is known in Eq. (9), which can be seen as the best estimation from LCM.

Please cite this article as: H. Wang, et al., From clicking to consideration: A business intelligence approach to estimating consumers' consideration probabilities, Decision Support Systems (2012), http://dx.doi.org/10.1016/j.dss.2012.10.052

![](/api/attachments/SC6WWC7G/fulltext/images/811095b61c66818c6e39761e0e6470e8f36eadf95bfd4df1a4469e3747d2d34b.jpg)  
Fig. 6. Given the positioning map of Fig. 4, contour lines of probabilities that products fall into the consideration set of the consumer at the origin when θ=0.4.

In the experiments, the classical root-mean-square error (RMSE) is used as the evaluation metrics [2,29]. Then, for any method M (here TEA or LCM), its performance in a positioning map is de<sup>fi</sup>ned as:

$$
\mathrm{RMSE} ^ {\mathrm{M}} = \sqrt {\frac {\sum_ {c \in C _ {\mathrm{te}}} \sum_ {s \in \bar {S} _ {c}} \left(\operatorname* {P r} ^ {M} (a _ {c s} = 1) - e ^ {- \mathrm{dis} _ {c s} ^ {2} / \theta}\right) ^ {2}}{| C _ {\mathrm{te}} | \times | \bar {S} _ {c} |}}\tag{10}
$$

![](/api/attachments/SC6WWC7G/fulltext/images/1054fa6208f7b26aaf2f2ec60239d6a6cade80815660f1d4c1c91cf2471194c2.jpg)  
Fig. 7. Given the positioning map of Fig. 5, contour lines of probabilities that products fall into the consideration set of the consumer at the origin when θ=0.4.

The improvement of TEA over LCM in a positioning map is de<sup>fi</sup>ned as:

$$
\mathrm{IMPR} = \frac {\mathrm{RMSE} ^ {\mathrm{LCM}} - \mathrm{RMSE} ^ {\mathrm{TEA}}}{\mathrm{RMSE} ^ {\mathrm{LCM}}} \times 100 \%\tag{11}
$$

Given a speci<sup>fi</sup>c value of $( N _ { \mathrm { S G } } , \theta , \mathsf { p e r } ) ,$ , say $( N _ { \mathrm { S G 0 } } , \theta _ { 0 } , \mathsf { p e r } _ { 0 } )$ , the performances of method M under $( N _ { \mathrm { S G 0 } } , \theta _ { 0 } , \mathsf { p e r } _ { 0 } )$ are measured by their performances in the 100 positioning maps generated by $( N _ { \mathrm { S G 0 } } , \theta _ { 0 } , \mathrm { p e r } _ { 0 } )$ The median of ${ \mathrm { R M S E } } ^ { \mathrm { T E A } }$ (IMPR) in the 100 positioning maps is de<sup>fi</sup>ned as the performance of TEA (the improvement of TEA over LCM) under $( N _ { \mathrm { S G 0 } } , \theta _ { 0 } , \mathrm { p e r } _ { 0 } )$ , denoted as mRMSE<sup>TEA</sup> and mIMPR. T-test is used to examine the signi<sup>fi</sup>cance of the improvement.

## 5.3. Experimental results and discussion

The performance of TEA and the improvement of TEA over LCM are illustrated in Table 5, where the <sup>fi</sup>rst number in the cell is mRMSE<sup>TEA</sup> and the second one is mIMPR. According to the de<sup>fi</sup>nition of mRMSE<sup>TEA</sup> and mIMPR, mRMSE<sup>TEA</sup> measures the performance of TEA, where smaller mRMSE<sup>TEA</sup> means better performance of TEA, and mIMPR measures the improvement of TEA over LCM, where bigger

The performance of TEA (mRMSE<sup>TEA</sup>) and the improvement of TEA over LCM (mIMPR) with varying parameters.

<table><tr><td> $N_{\text{SG}}$ </td><td>perθ</td><td>5%</td><td></td><td>10%</td><td></td><td>15%</td><td></td><td>20%</td><td></td></tr><tr><td rowspan="10">1</td><td>0.1</td><td>11.13%</td><td>5.93%</td><td>9.33%</td><td>7.05%</td><td>11.55%</td><td>8.69%</td><td>9.23%</td><td>9.05%</td></tr><tr><td>0.2</td><td>12.94%</td><td>5.93%</td><td>11.68%</td><td>6.48%</td><td>11.95%</td><td>11.05%</td><td>11.82%</td><td>13.55%</td></tr><tr><td>0.3</td><td>16.63%</td><td>6.08%</td><td>14.48%</td><td>8.45%</td><td>14.05%</td><td>11.83%</td><td>13.46%</td><td>13.79%</td></tr><tr><td>0.4</td><td>16.78%</td><td>6.06%</td><td>17.22%</td><td>12.42%</td><td>16.65%</td><td>14.14%</td><td>15.71%</td><td>19.35%</td></tr><tr><td>0.5</td><td>17.92%</td><td>5.59%</td><td>16.96%</td><td>11.54%</td><td>17.61%</td><td>16.63%</td><td>17.07%</td><td>17.67%</td></tr><tr><td>0.6</td><td>19.12%</td><td>5.53%</td><td>17.60%</td><td>10.82%</td><td>18.74%</td><td>17.64%</td><td>18.62%</td><td>16.53%</td></tr><tr><td>0.7</td><td>20.57%</td><td>8.11%</td><td>20.95%</td><td>11.41%</td><td>14.67%</td><td>16.25%</td><td>19.30%</td><td>20.07%</td></tr><tr><td>0.8</td><td>22.92%</td><td>6.83%</td><td>18.17%</td><td>13.82%</td><td>17.56%</td><td>16.99%</td><td>16.52%</td><td>20.92%</td></tr><tr><td>0.9</td><td>23.31%</td><td>7.34%</td><td>18.10%</td><td>9.76%</td><td>19.92%</td><td>19.68%</td><td>19.41%</td><td>22.79%</td></tr><tr><td>1.0</td><td>23.76%</td><td>5.70%</td><td>23.08%</td><td>10.79%</td><td>21.16%</td><td>15.97%</td><td>18.88%</td><td>15.38%</td></tr><tr><td rowspan="10">2</td><td>0.1</td><td>9.70%</td><td>5.12%</td><td>8.74%</td><td>5.94%</td><td>8.73%</td><td>8.57%</td><td>9.44%</td><td>8.64%</td></tr><tr><td>0.2</td><td>13.24%</td><td>5.38%</td><td>13.08%</td><td>7.01%</td><td>12.86%</td><td>9.94%</td><td>11.68%</td><td>12.99%</td></tr><tr><td>0.3</td><td>16.36%</td><td>4.34%</td><td>14.06%</td><td>6.83%</td><td>13.84%</td><td>10.81%</td><td>13.36%</td><td>13.74%</td></tr><tr><td>0.4</td><td>16.27%</td><td>3.88%</td><td>16.58%</td><td>8.40%</td><td>15.68%</td><td>13.67%</td><td>14.28%</td><td>13.27%</td></tr><tr><td>0.5</td><td>19.29%</td><td>4.38%</td><td>16.72%</td><td>6.93%</td><td>17.39%</td><td>10.16%</td><td>16.40%</td><td>14.74%</td></tr><tr><td>0.6</td><td>19.81%</td><td>3.27%</td><td>17.37%</td><td>7.47%</td><td>17.28%</td><td>13.98%</td><td>16.43%</td><td>15.15%</td></tr><tr><td>0.7</td><td>20.40%</td><td>2.40%</td><td>17.96%</td><td>10.59%</td><td>17.75%</td><td>13.84%</td><td>18.42%</td><td>16.08%</td></tr><tr><td>0.8</td><td>19.70%</td><td>2.37%</td><td>19.93%</td><td>7.10%</td><td>19.14%</td><td>14.78%</td><td>17.94%</td><td>17.68%</td></tr><tr><td>0.9</td><td>21.89%</td><td>3.27%</td><td>20.67%</td><td>9.83%</td><td>19.41%</td><td>9.23%</td><td>18.76%</td><td>12.90%</td></tr><tr><td>1.0</td><td>23.14%</td><td>1.82%</td><td>20.18%</td><td>8.08%</td><td>18.53%</td><td>14.82%</td><td>18.80%</td><td>20.09%</td></tr><tr><td rowspan="10">4</td><td>0.1</td><td>8.96%</td><td>5.46%</td><td>8.30%</td><td>6.85%</td><td>8.77%</td><td>9.36%</td><td>7.55%</td><td>8.74%</td></tr><tr><td>0.2</td><td>12.47%</td><td>3.87%</td><td>11.06%</td><td>7.14%</td><td>10.52%</td><td>8.24%</td><td>11.08%</td><td>11.13%</td></tr><tr><td>0.3</td><td>13.40%</td><td>4.20%</td><td>12.77%</td><td>5.72%</td><td>13.33%</td><td>9.57%</td><td>12.52%</td><td>11.33%</td></tr><tr><td>0.4</td><td>16.98%</td><td>3.23%</td><td>14.59%</td><td>7.00%</td><td>14.45%</td><td>12.03%</td><td>14.31%</td><td>12.42%</td></tr><tr><td>0.5</td><td>16.99%</td><td>3.67%</td><td>16.13%</td><td>7.77%</td><td>15.84%</td><td>11.29%</td><td>14.13%</td><td>12.57%</td></tr><tr><td>0.6</td><td>18.10%</td><td>1.49%</td><td>16.44%</td><td>4.73%</td><td>15.39%</td><td>10.28%</td><td>15.42%</td><td>13.83%</td></tr><tr><td>0.7</td><td>19.54%</td><td>2.52%</td><td>17.17%</td><td>6.30%</td><td>16.89%</td><td>10.70%</td><td>15.84%</td><td>13.89%</td></tr><tr><td>0.8</td><td>19.92%</td><td>1.36%</td><td>18.16%</td><td>7.54%</td><td>17.37%</td><td>9.24%</td><td>16.67%</td><td>13.90%</td></tr><tr><td>0.9</td><td>20.15%</td><td>1.62%</td><td>18.27%</td><td>6.26%</td><td>18.31%</td><td>11.37%</td><td>17.38%</td><td>12.71%</td></tr><tr><td>1.0</td><td>20.87%</td><td>0.16%</td><td>19.89%</td><td>6.43%</td><td>19.52%</td><td>11.53%</td><td>17.11%</td><td>17.30%</td></tr><tr><td rowspan="10">8</td><td>0.1</td><td>8.76%</td><td>6.03%</td><td>8.46%</td><td>7.50%</td><td>7.83%</td><td>9.02%</td><td>8.65%</td><td>11.30%</td></tr><tr><td>0.2</td><td>11.15%</td><td>4.86%</td><td>11.07%</td><td>7.21%</td><td>10.66%</td><td>10.24%</td><td>10.03%</td><td>11.12%</td></tr><tr><td>0.3</td><td>13.29%</td><td>4.74%</td><td>12.94%</td><td>7.76%</td><td>12.63%</td><td>11.98%</td><td>11.56%</td><td>12.58%</td></tr><tr><td>0.4</td><td>14.44%</td><td>3.50%</td><td>14.41%</td><td>8.46%</td><td>13.31%</td><td>11.14%</td><td>13.19%</td><td>13.99%</td></tr><tr><td>0.5</td><td>16.32%</td><td>3.52%</td><td>15.71%</td><td>7.24%</td><td>14.82%</td><td>10.76%</td><td>13.97%</td><td>15.73%</td></tr><tr><td>0.6</td><td>16.51%</td><td>2.26%</td><td>16.53%</td><td>8.82%</td><td>15.60%</td><td>13.55%</td><td>15.00%</td><td>15.01%</td></tr><tr><td>0.7</td><td>18.08%</td><td>1.56%</td><td>16.67%</td><td>8.65%</td><td>15.53%</td><td>8.95%</td><td>15.25%</td><td>12.82%</td></tr><tr><td>0.8</td><td>19.02%</td><td>2.13%</td><td>18.03%</td><td>7.32%</td><td>16.22%</td><td>10.17%</td><td>16.25%</td><td>15.72%</td></tr><tr><td>0.9</td><td>19.64%</td><td>0.27%</td><td>17.57%</td><td>6.74%</td><td>17.67%</td><td>13.25%</td><td>16.96%</td><td>16.14%</td></tr><tr><td>1.0</td><td>20.27%</td><td>0.88%</td><td>18.54%</td><td>8.23%</td><td>17.53%</td><td>10.91%</td><td>17.02%</td><td>12.98%</td></tr></table>

Please cite this article as: H. Wang, et al., From clicking to consideration: A business intelligence approach to estimating consumers' consideration probabilities, Decision Support Systems (2012), http://dx.doi.org/10.1016/j.dss.2012.10.052

Table 6  
The GLM for mRMSE<sup>TEA</sup>, mIMPR on $N _ { S G } ,$ θ, and per.

<table><tr><td></td><td> $N_{SG}$ </td><td>θ</td><td>per</td></tr><tr><td>mRMSE $^{TEA}$ </td><td>-0.003</td><td>0.110</td><td>-0.151</td></tr><tr><td>mIMPR</td><td>-0.004</td><td>0.025</td><td>0.713</td></tr></table>

mIMPR means larger improvement of TEA over LCM. All improvements in Table 5 are bigger than zero at the signi<sup>fi</sup>cance level of 0.1%.

From the results shown in Table 5, we can see that the average improvement is around 9.5%, which indicates that TEA outperforms LCM generally. For further comparison, we use general liner model to analyze the relationship between the performance (improvements) and the parameters. Table 6 illustrates the GLM results (p-valueb0.001).

The negative coef<sup>fi</sup>cients of $N _ { S G }$ and per for mRMSE<sup>TEA</sup> show that the performance of TEA is higher (i.e., mRMSE<sup>TEA</sup> is lower) when the marketing segmentations are clearer (more market segments) and the information about consumers' preferences increases (more inspected products). The positive coef<sup>fi</sup>cient of decay rate (θ) for mRMSE<sup>TEA</sup> shows that the dif<sup>fi</sup>culty to estimate CPs increases when consumers consider less products (i.e., the size of consideration set decreases). However, the positive coef<sup>fi</sup>cient of decay rate (θ) for the improvement (mIMPR) indicates that TEA is more resistant to this in<sup>fl</sup>uence than LCM so that the improvement increases when consumers consider less products. The positive coef<sup>fi</sup>cient of per for mIMPR shows that TEA performs much better when there is more information about consumers' preferences (i.e., consumers inspect more products).

The negative coef<sup>fi</sup>cient of $N _ { S G }$ for mIMPR is reasonable. As above-mentioned, the limitation of LCM is that it focuses more on the similarity between consumers in the same class. Therefore, the “core” and the “edge” consumers in the same class are assumed to have the same preference even though they may be quite mutually different. In contrast, TEA focuses more on the difference between consumers and assumes that each consumer represents a class which re<sup>fl</sup>ects his or her preference. Therefore, when there are fewer consumer classes, LCM may not be as personalized as TEA. When there are more consumer classes, the number of consumers in each class is less (the number of all consumers is relatively <sup>fi</sup>xed), which reduces the difference between the “core” and the “edge” consumer and makes LCM tend to be like TEA.

## 6. Conclusion

In this paper, we have developed a novel approach, namely the two-step estimation approach (TEA), to estimate the consumer's consideration probabilities (CPs), which is important to consumers as well as to e-sellers and e-marketplaces. The approach has extended the traditional latent class model (LCM) by re<sup>fl</sup>ecting partial belongings of consumers to classes, and considering the customers' preferences (tastes) in a both positive and negative manner. Subsequently, it has generated CPs using the partial belonging degrees in light of weighted probability. Moreover, experiments have been conducted with varying parameters, revealing that TEA outperformed LCM signi<sup>fi</sup>cantly, especially in the cases where consumers inspected or considered more products.

## Acknowledgments

The work was partially supported by the National Natural Science Foundation of China (70890080/71072015/71110107027) and the Tsinghua University Initiative Scienti<sup>fi</sup>c Research Program (20101081741).

## Appendix A

The notations and their meanings in experiments

<table><tr><td>Name</td><td>Meaning</td></tr><tr><td>SG</td><td>The set of consumer (product) segments on the positioning map. As mentioned before, the segments of both consumers and products are assumed the same, since products are developed to satisfy consumers&#x27; needs.</td></tr><tr><td> $N_{\text{SG}}$ </td><td>Number of segments, i.e.,  $N_{\text{SG}} = |\text{SG}|$ . Considering that the number of segments may vary in different scenarios,  $N_{\text{SG}} \in \{1,2,4,8\}$  in the experiments.</td></tr><tr><td>sg</td><td>A segment in SG, i.e., sg ∈ SG.</td></tr><tr><td> $\mu_{\text{sg}}, \sigma_{\text{sg}}$ </td><td>The parameters to uniquely represent segment sg. All consumers (products) in sg obey a normal distribution of  $\mathcal{N}(\mu_{\text{sg}}, \sigma_{\text{sg}}^2)$ . Considering that the consumers (products) in the same segments are closer than consumers (products) in the different classes on average, we assume that  $\mu_{\text{sg}}$  obeys a normal distribution of  $\mathcal{N}(0,2\sigma_{\text{sg}}^2)$ . For convenience,  $\sigma_{\text{sg}} = 1$  in the experiments.</td></tr><tr><td>C</td><td>The set of consumers, as mentioned in Section 2.</td></tr><tr><td>S</td><td>The set of products, as mentioned in Section 2.</td></tr><tr><td> $N_{\text{C}}$ </td><td>Number of consumers, i.e.,  $N_{\text{C}} = |\text{C}|$ .</td></tr><tr><td> $\mu_{N_{\text{C}}}$ </td><td>The mean of  $N_{\text{C}}$ ,  $\mu_{N_{\text{S}}} = 100$ .</td></tr><tr><td> $N_{\text{S}}$ </td><td>Number of products, i.e.,  $N_{\text{S}} = |\text{S}|$ .</td></tr><tr><td> $\mu_{N_{\text{S}}}$ </td><td>The mean of  $N_{\text{S}}$ ,  $\mu_{N_{\text{S}}} = 100$ .</td></tr><tr><td> $C_{\text{sg}}$ </td><td>Consumers who belong to segment sg,  $C = \bigcup_{\text{sg} \in \text{SG}} C_{\text{sg}}$ </td></tr><tr><td> $S_{\text{sg}}$ </td><td>Products which belong to segment sg,  $S = \bigcup_{\text{sg} \in \text{SG}} S_{\text{sg}}$ </td></tr><tr><td> $N_{C_{\text{sg}}}$ </td><td>Number of consumers in  $C_{\text{sg}}$ , i.e.,  $N_{C_{\text{sg}}} = |C_{\text{sg}}|, N_{C} = \sum_{\text{sg} \in \text{SG}} N_{C_{\text{sg}}}$ .</td></tr><tr><td> $N_{S_{\text{sg}}}$ </td><td>Number of products in  $S_{\text{sg}}$ , i.e.,  $N_{S_{\text{sg}}} = |S_{\text{sg}}|, N_{S} = \sum_{\text{sg} \in G} N_{S_{\text{sg}}}$ .</td></tr><tr><td> $\mu_{C_{\text{sg}}}, \sigma_{C_{\text{sg}}}$ </td><td>The parameters which determine the distribution of  $N_{C_{\text{sg}}}$ .  $N_{C_{\text{sg}}} = \max(1, \text{round}(X))$  where X obeys a normal distribution of  $\mathcal{N}\left(\mu_{C_{\text{sg}}}, \sigma_{C_{\text{sg}}}^2\right)$ . Considering that the numbers of consumers in different classes may vary largely,  $\sigma_{C_{\text{sg}}} = \frac{1}{2}\mu_{C_{\text{sg}}}$ . Moreover,  $\mu_{C_{\text{sg}}} \times N_{\text{SG}} = \mu_{N_{\text{C}}}$ .</td></tr><tr><td> $\mu_{S_{\text{sg}}}, \sigma_{S_{\text{sg}}}$ </td><td>The parameters which determine the distribution of  $N_{S_{\text{sg}}}$ .  $N_{S_{\text{sg}}} = \max(1, \text{round}(X))$  where X obeys a normal distribution of  $\mathcal{N}\left(\mu_{S_{\text{sg}}}, \sigma_{S_{\text{sg}}}^2\right)$ . Considering that the numbers of products in different classes may vary largely,  $\sigma_{S_{\text{sg}}} = \frac{1}{2}\mu_{S_{\text{sg}}}$ . Moreover,  $\mu_{S_{\text{sg}}} \times N_{\text{SG}} = \mu_{N_{\text{S}}}$ .</td></tr><tr><td>θ</td><td>The decay rate, θ ∈ {0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0}.</td></tr><tr><td>per</td><td>The percentage of products that each consumer has inspected on average, per ∈ {5%,10%,15%,20%.}</td></tr></table>

## References

[1] G. Adomavicius, A. Tuzhilin, Personalization technologies: a process-oriented perspective, Communications of the ACM 48 (10) (2005) 83–90.

[2] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions, IEEE Transactions on Knowledge & Data Engineering 17 (6) (2005) 734–749.

[3] R.L. Andrews, T.C. Srinivasan, Studying consideration effects in empirical choice models using scanner panel data, Journal of Marketing Research (JMR) 32 (1) (1995) 30–41.

[4] S. Bhattacharya, S. Gollapudi, K. Munagala, Consideration set generation in commerce search, in: Proceedings of the 20th International Conference on World wide web, ACM, Hyderabad, India, 2011, pp. 317–326.

[5] G. Chen, H. Liu, L. Yu, Q. Wei, X. Zhang, A new approach to classi<sup>fi</sup>cation based on association rule mining, Decision Support Systems 42 (2) (2006) 674–689.

[6] J. Chiang, S. Chib, C. Narasimhan, Markov chain Monte Carlo and models of consideration set and parameter heterogeneity, Journal of Econometrics 89 (1–2) (1998) 223–248

[7] A.G. Close, M. Kukar-Kinney, Beyond buying: motivations behind consumers' on line shopping cart use, Journal of Business Research 63 (9/10) (2010) 986–992.

[8] M. Deshpande, G. Karypis, Item-based top-N recommendation algorithms, ACM Transactions on Information Systems 22 (1) (2004) 143–177.

[9] S. Devaraj, M. Fan, R. Kohli, Examination of online channel preference: using the structure-conduct-outcome framework, Decision Support Systems 42 (2) (2006) 1089–1103.

[10] D. Dzyabura, J.R. Hauser, Active machine learning for consideration heuristics, Marketing Science 30 (5) (2011) 801–819.

[11] K. Eliaz, R. Spiegler, Consideration sets and competitive marketing, Review of Economic Studies 78 (1) (2011).235–262

[12] T. Elrod, Choice map: inferring a product-market map from panel data, Marketing Science 7 (1) (1988) 21.

Please cite this article as: H. Wang, et al., From clicking to consideration: A business intelligence approach to estimating consumers' consideration probabilities, Decision Support Systems (2012), http://dx.doi.org/10.1016/j.dss.2012.10.052

[13] M. Fan, S. Kumar, A. Whinston, Selling or advertising: strategies for providing digital media online, Journal of Management Information Systems 24 (3) (2007) 143–166.

[14] J. Feng, H.K. Bhargava, D.M. Pennock, Implementing sponsored search in web search engines: computational evaluation of alternative mechanisms, INFORMS Journal on Computing 19 (1) (2007) 137–148.

[15] D. Fleder, K. Hosanagar, Blockbuster culture's next rise or fall: the impact of recommender systems on sales diversity, Management Science 55 (5) (2009) 697–712.

[16] R. Gar<sup>fi</sup>nkel, R. Gopal, A. Tripathi, F. Yin, Design of a shopbot and recommender system for bundle purchases, Decision Support Systems 42 (3) (2006) 1974–1986.

[17] R. Gar<sup>fi</sup>nkel, R. Gopal, B. Pathak, F. Yin, Shopbot 2.0: integrating recommendations and promotions with comparison shopping, Decision Support Systems 46 (1) (2008) 61–69.

[18] A. Ghose, S. Yang, An empirical analysis of search engine advertising: sponsored search in electronic markets, Management Science 55 (10) (2009) 1605–1622.

[19] M.D. Gordon, P. Lenk, A utility theoretic examination of the probability ranking principle in information retrieval, Journal of the American Society for Information Science 42 (10) (1991) 703–714.

[20] B. Gu, P. Konana, H.-W.M. Chen, Identifying consumer consideration set at the purchase time from aggregate purchase data in online retailing, Decision Support Systems 53 (3) (2012) 625–633.

[21] G. Haubl, V. Trifts, Consumer decision making in online shopping environments: the effects of interactive decision aids, Marketing Science 19 (1) (2000) 4–21.

[22] J.R. Hauser, O. Toubia, T. Evgeniou, R. Befurt, D. Dzyabura, Disjunctions of Conjunctions, Cognitive Simplicity, and Consideration Sets, Journal of Marketing Research (IMR) 47 (3) (2010) 485-496

[23] J.R. Hauser, Consideration Set Heuristics, Journal of Business Research, (forthcoming).

[24] T. Hofmann, Probabilistic latent semantic indexing, in: Proceedings of the 22nd annual international ACM SIGIR conference on Research and development in information retrieval, ACM, Berkeley, California, United States, 1999, pp. 50–57.

[25] T. Hofmann, Collaborative <sup>fi</sup>ltering via gaussian probabilistic latent semantic analysis, in: Proceedings of the 26th annual international ACM SIGIR conference on Research and development in informaion retrieval, ACM, Toronto, Canada, 2003, pp. 259–266.

[26] T. Hofmann, Latent semantic models for collaborative <sup>fi</sup>ltering, ACM Transactions on Information Systems 22 (1) (2004) 89–115.

[27] J.A. Howard, J.N. Sheth, The Theory of Buyer Behavior, Wiley, New York, 1969..

[28] P. Huang, N.H. Lurie, S. Mitra, Searching for experience on the web: an empirical examination of consumer behavior for search and experience goods, Journal of Marketing 73 (2) (2009) 55–69.

[29] M. Jahrer, A. Töscher, R. Legenstein, Combining predictions for accurate recommender systems, in: Proceedings of the 16th ACM SIGKDD international conference on Knowledge discovery and data mining, ACM, Washington, DC, USA, 2010, pp. 693–702.

[30] K. Jedidi, R. Kohli, W.S. DeSarbo, Consideration sets in conjoint analysis, Journal of Marketing Research 33 (3) (1996) 364–372.

[31] W.A. Kamakura, M. Wedel, Life-style segmentation with tailored interviewing, Journal of Marketing Research (JMR) 32 (3) (1995) 308–317.

[32] H.-N. Kim, A. El-Saddik, G.-S. Jo, Collaborative error-re<sup>fl</sup>ected models for cold-start recommender systems, Decision Support Systems 51 (3) (2011) 519–531.

[33] H.-N. Kim, I. Ha, K.-S. Lee, G.-S. Jo, A. El-Saddik, Collaborative user modeling for enhanced content <sup>fi</sup>ltering in recommender systems, Decision Support Systems 51 (4) (2011) 772–781.

[34] J.B. Kim, P. Albuquerque, B.J. Bronnenberg, Mapping online consumer search, Journal of Marketing Research (JMR) 48 (1) (2011) 13–27.

[35] Y. Koren, Collaborative <sup>fi</sup>ltering with temporal dynamics, Communications of the ACM 53 (4) (2010) 89–97.

[36] M. Kukar-Kinney, A.G. Close, The determinants of consumers' online shopping cart abandonment, Journal of the Academy of Marketing Science 38 (2) (2010) 240–250.

[37] J. Levine, Joint-space analysis of “pick-any” data: analysis of choices from an unconstrained set of alternatives. Psychometrika 44 (1) (1979) 85–92.

[38] C.-W. Liao, Y.-H. Perng, T.-L. Chiang, Discovery of unapparent association rules based on extracted probability, Decision Support Systems 47 (4) (2009) 354–363.

[39] W.W. Moe, An empirical two-stage choice model with varying decision rules applied to internet clickstream data, Journal of Marketing Research (JMR) 43 (4) (2006) 680–692.

[40] W.W. Moe, P.S. Fader, Capturing evolving visit behavior in clickstream data, Journal of Interactive Marketing 18 (1) (2004) 5–19 (John Wiley & Sons).

[41] W.W. Moe, P.S. Fader, Dynamic conversion behavior at e-commerce sites, Management Science 50 (3) (2004) 326–335.

[42] A.L. Montgomery, L. Shibo, K. Srinivasan, J.C. Liechty, Modeling online browsing and path analysis using clickstream data, Marketing Science 23 (4) (2004) 579–595.

[43] S. Moorthy, B.T. Ratchford, D. Talukdar, Consumer information search revisited: theory and empirical analysis, Journal of Consumer Research 23 (4) (1997) 263–277.

[44] C.L. Narayana, R.J. Markin, Consumer behavior and product performance: an alternative conceptualization, Journal of Marketing 39 (4) (1975) 1–6.

[45] E.L. Olson, H.M. Thjømøe, Sponsorship effect metric: assessing the <sup>fi</sup>nancial value of sponsoring by comparisons to television advertising, Journal of the Academy of Marketing Science 37 (4) (2009) 504–515.

[46] A. Prinzie, D. Van den Poel, Predicting home-appliance acquisition sequences: Markov/Markov for discrimination and survival analysis for modeling sequential information in NPTB models, Decision Support Systems 44 (1) (2007) 28–45.

[47] G. Punj, R. Moore, Information search and consideration set formation in a web-based store environment, Journal of Business Research 62 (6) (2009) 644–650.

[48] B.T. Ratchford, D. Talukdar, L.E.E. Myung-Soo, The impact of the internet on consumers' use of information sources for automobiles: a re-inquiry, Journal of Consumer Research 34 (1) (2007) 111–119.

[49] M. Richardson, E. Dominowska, R. Ragno, Predicting clicks: estimating the click-through rate for new ads, in: Proceedings of the 16th international conference on World Wide Web, ACM, Banff, Alberta, Canada, 2007, pp. 521–530.

[50] D.L. Rosen, R.W. Olshavsky, A protocol analysis of brand choice strategies involving recommendations, Journal of Consumer Research 14 (3) (1987) 440–444.

[51] B. Sarwar, G. Karypis, J. Konstan, J. Reidl, Item-based collaborative <sup>fi</sup>ltering recommendation algorithms, in: Proceedings of the 10th international conference on World Wide Web, ACM, Hong Kong, Hong Kong, 2001, pp. 285–295.

[52] Y. Sha, A. Ghose, Analyzing the relationship between organic and sponsored search advertising: positive, negative, or zero interdependence? Marketing Science 29 (4) (2010) 602–623.

[53] G. Shani, D. Heckerman, R.I. Brafman, An MDP-based recommender system, Journal of Machine Learning Research 6 (2005) 1265–1295

[54] C. Sismeiro, R.E. Bucklin, Modeling purchase behavior at an e-commerce web site: a task-completion approach, Journal of Marketing Research (JMR) 41 (3) (2004) 306–323.

[55] Y. Song, C.F. Mela, A dynamic model of sponsored search advertising, Marketing Science 30 (3) (2011) 447–468

[56] W.-K. Tan, C.-H. Tan, H.-H. Teo, Consumer-based decision aid that explains which to buy: decision con<sup>fi</sup>rmation or overcon<sup>fi</sup>dence bias? Decision Support Systems 53 (1) (2012) 127–141.

[57] A. Umyarov, A. Tuzhilin, Using external aggregate ratings for improving individual recommendations, ACM Transactions on the Web 5 (1) (2011) 1–40.

[58] E. van Nierop, B. Bronnenberg, R. Paap, M. Wedel, P.H. Franses, Retrieving unobserved consideration sets from household panel data, Journal of Marketing Research (JMR) 47 (1) (2010) 63–74.

[59] J. Wu, A. Rangaswamy, A fuzzy set model of search and consideration with an application to an online market, Marketing Science 22 (3) (2003) 411–434.

[60] X. Wu, C. Zhang, S. Zhang, Ef<sup>fi</sup>cient mining of both positive and negative association rules, ACM Transactions on Information Systems 22 (3) (2004) 381–405.

[61] Y. Zhang, J. Callan, Maximum likelihood estimation for <sup>fi</sup>ltering thresholds, in: Proceedings of the 24th annual international ACM SIGIR conference on Research and development in information retrieval, ACM, New Orleans, Louisiana, United States, 2001, pp. 294–302.

[62] Y. Zhu, G. Wang, J. Yang, D. Wang, J. Yan, J. Hu, Z. Chen, Optimizing search engine revenue in sponsored search, in: Proceedings of the 32nd international ACM SIGIR conference on Research and development in information retrieval, ACM, Boston, MA, USA, 2009, pp. 588–595.

[63] R. Zwick, A. Rapoport, A.K.C. Lo, A.V. Muthukrishnan, Consumer sequential search: not enough or too much? Marketing Science 22 (4) (2003) 503–519.

Hao Wang is currently pursuing his PhD degree at the School of Economics and Management, Tsinghua University, Beijing, China. His research interests include business intelligence, consumer information search and decision support.

Qiang Wei is an associate professor in the Department of Management Science and Engineering, School of Economics and Management, Tsinghua University, Beijing, China. His current research interests include knowledge discovery, data mining techniques, management information systems, system simulations

Guoqing Chen received his PhD from the Catholic University of Leuven (K.U. Leuven, Belgium) and now is Professor of Information Systems at the School of Economics and Management, Tsinghua University, Beijing, China. His research interests include information systems management, business intelligence, decision support and soft computing.

---
otero_id: 5890
otero_key: "MYP74UX7"
title: "Incorporating reference products into modeling consumer choice decision: A mixtures-of-experts model"
authors: "Ping Wang; Luping Sun; Rakesh Niraj; Jaihak Chung; Meng Su"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.02.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Incorporating reference products into modeling consumer choice decision: A mixtures-of-experts model

![](/api/attachments/MYP74UX7/fulltext/images/bbb710ecaa854dfbdf4d05fdb142a300769ecbec9e850f7751906d89e40689ee.jpg)

Ping Wang<sup>a</sup>, Luping Sun<sup>b</sup>, Rakesh Niraj<sup>c,⁎</sup>, Jaihak Chung<sup>d,e</sup>, Meng Su<sup>f</sup>

<sup>a</sup> College of Economics and Management & China-Africa International Business School, Zhejiang Normal University, Jinhua 321004, China

<sup>b</sup> Business School, Central University of Finance and Economics, Beijing 100081, China

c Weatherhead School of Management, Case Western Reserve University, Cleveland, OH 44106, USA

<sup>d</sup> School of Business Administration, Sogang University, Seoul, Republic of Korea

<sup>e</sup> IESEG School of Management, France

<sup>f</sup> Baifendian Technology, 16F, Building A, Beichen Century Center, 8th Beichen West Road, Chaoyang District, Beijing, China

## A R T I C L E I N F O

Keywords: Comparison efect Mixtures-of-experts model Reference product Consumer decision making Choice based conjoint Recommendation engines

## A B S T R A C T

Understanding the process of consumer decision making is important for many decision support systems. Consumers evaluate diferent alternatives and then come to a decision. Prior research suggests that consumer evaluations leading to choice are comparative in nature and can be afected by other alternatives or reference products. This study proposes a mixtures-of-experts model framework to examine the role of diferent reference products in consumer choice of multi-attribute products. While multiple external and internal reference points have been proposed, previous studies have very rarely investigated more than one reference point in the same model. Using data from a choice-based conjoint experiment, our empirical model enables us to identify which product consumers tend to use as the reference product by incorporating four diferent reference products and includes consumer characteristics to examine how consumers differ in their utilization of different reference products. The results show that our model outperforms other reference-dependent models in prior literature. In our empirical context of smartphone choices, the most commonly used reference product is the most preferred product in the choice set, while the least preferred product and the average product are rarely used. We also examine the role of consumer characteristics such as gender, product familiarity, and product interest in utilizing reference products. This paper provides insights into the unobserved comparison process in consumer choice, which can be applied to decision support systems such as recommendation engines.

## 1. Introduction

Consumer choice decision has gained extensive attention from academic researchers and practitioners in decision support systems [1–3]. In traditional choice models, the utility of a product is often specified as a function only of its own attributes, independent of other products judged concurrently. Substantial consumer behavior research, however, suggests that consumer judgments are comparative in nature [4] and consumer choice decision is significantly afected by the com position of the choice set [5,6]. For example, behavioral literature has provided robust evidence for the presence of attraction efect, compromise efect, and inference efect [7,8], demonstrating that the comparison among products in a choice set systematically influences consumer choice, especially for unfamiliar products [9].

If the utility of a product perceived by an individual is influenced by the comparison with other products, traditional choice models that ignore the comparison efect may yield misleading results and inaccurate predictions. For example, the additional utility or disutility due to comparison efect may be mistakenly attributed to preference weights, leading to biased estimation of consumer sensitivity to product attributes. This might lead to serious problems when firms apply the estimation results to support business decisions. For example, the biased estimation results may lead the firm to misunderstand consumer preference for its product (relative to other products in the same product category) and consequently develop less optimal positioning and communication strategies. Moreover, choice models with no comparison efects may generate inaccurate predictions regarding which products consumer prefer the most, and thus lead to inferior suggestions when applied to recommendation engines or may lead to suboptimal decision suggestions from a decision support system helping mangers

about product positioning.

Given the serious consequences of ignoring comparison efect, empirical research has been reported developing models that include the unobserved comparison efect in consumer choice decision. Most early eforts in this regard adopt the reference-dependent framework [10–15]. These studies take the reference product as given or exogenous and usually consider only one reference product. As a matter of fact, consumers may use multiple reference products simultaneously. Modeling multiple reference products in consumer choice, however, is methodologically challenging. This is partly because the model structure becomes very complex when the comparison efects from more than two reference products are included. Furthermore, there may be consumer heterogeneity in the utilization of diferent reference products [16]. This heterogeneity may add another layer of complexity.

To simplify the model, some prior studies focus only on the com parison efect regarding one attribute. Focusing just on price, there is evidence that consumers use diferent reference prices in diferent contexts and they may even use multiple reference prices in a single context [17]. Little empirical work, however, has incorporated reference efects on multiple attributes into choice model. There have been calls for the generalization of the models to durable products that have a large number of attributes [18,19]. One recent response to this is the random regret minimization (RRM) model [20]. This model considers the reference efect of multiple attributes on consumer choice; however, it cannot uncover which products serve as the reference or comparison standard.

In presence of comparison efect, modeling consumer choice becomes more complicated. First, the model must capture consumers' utilization of diferent reference products as the comparison standard (i.e., comparison strategy). Second, given comparison strategy, the model should not only quantify the impact of diferent attributes but also capture the comparison efect (against the reference products) on consumer choice decision. Moreover, the utilization of diferent reference products or the comparison strategy may vary according to consumer characteristics.

We propose a mixtures-of-experts (ME) model to capture consumer heterogeneity in the utilization of diferent reference products (i.e., comparison strategy) and the comparison efects (from multiple reference products) on consumer choice. The application of mixture of experts is not new in decision support systems literature [21]. However, we are among the first to introduce the mixture-of-experts framework to examine comparison efect in consumer choice model. Prior work has provided theoretical arguments around some of the following options for reference products: the most preferred product, the least preferred product, the average product in the choice set, or an internal reference product retrieved from consumers' memory [10,12,17,22,23]. Our ME model investigates the relative importance of these four reference products in consumer choice. It treats the reference products as four experts and aggregates the choice probabilities using gating functions, which capture the comparison strategy of consumers. We conduct a choice-based conjoint experiment to collect data on consumer choices of smartphones and compare our model with several competing models (e.g., RRM [20,24]). Results show that the ME model outperforms competing models in terms of both in-sample fit and out-of-sample prediction.

This paper contributes to the literature on decision support systems in several respects. First, the ME model unpacks the process of consumers' utilization of diferent reference products while making comparisons and mimics consumers' decision-making process. Thus, it can provide more accurate predictions and be applied to various decision support systems. For example, our model has the potential to help firms develop better recommendation engines. State of the art hybrid re commendation systems rely on content matching (based on what cus tomers say they like or we observe them having liked in the past), and collaborative filtering (match based on similar customer's choices). The gating function estimates in our model provides basis for improving collaborative filtering and also provides guidance for what kind of choices to present to customers in order to subtly nudge them to a desirable option. Second, our model provides better understanding of who uses what kind of reference products, which provides implications for marketers to make more informed positioning and communication decisions. For instance, if our model suggests that the target segments mainly compare with the best product in the market, then the firm should diferentiate its product from (and emphasize its advantages relative to) the best competing product. With the assistance of our model, the firm would be able to make better decisions to put their oferings in the best possible light for their target segments vis-à-vis their competitors.

The remainder of this article is organized as follows. In Section 2, we review related literature on choice models with reference or context efects. Section 3 proposes the ME model to capture the impact of multiple reference products with multiple attributes and introduces some competing models. Then, we describe our choice-based conjoint experiment and present our empirical findings in Section 4. Finally, we conclude with a discussion of theoretical and managerial implications, and outline some future research directions.

## 2. Theoretical basis and related literature

## 2.1. Theoretical basis

In behavioral literature, there is consensus that consumer judge ments are relative and result from comparisons. Earliest research dates back to the 1960s, when Helson [25] proposed the adaptation level theory and suggested that stimuli are judged against certain internal norms (i.e., adaptation levels). Other research, however, suggests that the stimuli can be judged against other standards in the (external) context. In the pricing context, for instance, the range theory proposes that consumers may compare the target price with the two prices that define the range in the context (i.e., the maximum price and minimum price), while the range-frequency theory suggests that the target price may be compared against all the prices in the context [26–29]. Beyond these theories, Kahneman and Tversky [11] introduced the prospect theory, which is an overarching framework to describe consumer decision-making under risk. Consistent with the other theories, prospect theory postulates that consumer judgments are formed based on comparisons with reference points and they are more sensitive to losses than to gains. Substantial empirical research has provided evidence for the existence of reference-dependent preference and loss aversion [22]. All these studies have set the theoretical foundation for the examination of comparison efect on consumer decision-making.

In making a choice decision, consumers consciously or unconsciously compare among diferent alternatives judged concurrently [4,30–32]. The existence of comparison efect in consumer choice may have important implications for decision support systems. Song et al. [3] examined the efects of incorporating compensatory choice strategies in web-based consumer decision support systems. They suggested that decision support systems supporting compensatory strategies (weighted additive or equally weighted), compared to those supporting non-compensatory strategies (elimination-by-aspects), were perceived to be more accurate. Through considering the negative utility efect on consumer choice rule, Luo et al. [1] established a conjoint-analysisbased one-step optimization model, which can help firms develop optimal positioning strategies. In a similar vein, the comparison efect in consumer decision may also play an important role in decision support systems. Zhou [33] suggested that the comparison efect on price significantly influence buyers' reservation price in online bidding systems. Without considering comparison efects (and the corresponding nonlinear utility functions), recommendation engines may not provide good approximations of consumers' preference structures and thus generate inappropriate product recommendations [34]. Such biased recommendations may significantly reduce their efectiveness [35].

## 2.2. Comparison standard

In prior literature, the most common comparison standard is known as reference point. Reference points are defined as the standard against which consumers evaluate the target that they are considering for purchase [33]. Prior research has distinguished two types of reference points: internal and external. External reference points are based on the alternatives in the choice set while internal reference points are in the mind of consumers [17]. Thus, external reference points are stimulusbased while internal reference points are memory-based. Both internal and external reference points can afect consumer choice and pre ference [23].

In previous research, internal and external reference points, mostly for a single attribute (predominantly, price), have been operationalized in diferent ways. Three most commonly used external reference points include the most preferred level of the attribute [23], the least preferred level of the attribute [12], and the average or weighted average level of the attribute [7,10] in the choice set. Internal reference point is usually operationalized as the attribute level of the previously purchased pro duct [17,22].

Most empirical research incorporates reference points by including comparative evaluations, namely, the diferences between the focal product and the reference products. One limitation of such research is that it focuses only on one attribute (normally price) or at most two attributes [22,36]. When consumers make comparisons, however, price is not the only attribute that they compare. The comparison process may involve many other attributes and this is especially true for durable goods (e.g., automobiles or smartphones). For the purchase of smartphones, consumers may consider screen size, RAM, price, etc. Another drawback of extant empirical research is assuming the utilization of diferent reference points to be context-independent. In fact, consumers may use diferent reference points in diferent contexts and they may even use multiple reference points simultaneously in a given context [17].

## 2.3. Models of comparison efect using the reference-dependence framework

Most marketing researchers incorporate comparison efect into choice model using the reference-dependent framework [10,15]. Tversky and Simonson [37] proposed a simplified analytical model and incorporated comparison efects by the relative advantages and disadvantages of each alternative compared to the other alternatives in the choice set. This model demonstrated the importance of the comparison among diferent products in the choice set for the first time. Similarly, Orhun [13] proposed an analytical model to capture consumers' choice set-dependent preference in the context of product line design. Her model used an external reference product and incorporated a comparison component for each attribute. Though these analytical models contribute to our understanding of the consumer choice process, they do not reveal consumers' comparison strategy.

Similar limitations exist for prior empirical models. In a multi nomial probit model, Kamakura and Srivastava [38] incorporated the relationship among diferent products in the choice set by allowing their error terms to correlate and improved the model's prediction.

Kivetz et al. [12] compared diferent specifications of choice model and captured the compromise efect through loss aversion relative to a reference product. However, these studies assume the reference product as given and do not model consumers' utilization of diferent reference products.

## 2.4. Other models of comparison efect

The random regret minimization (RRM) model is a relatively recent empirical attempt that can be applied to model the comparison efect on multiple attributes [20,39]. Early applications of the model have been in the context of travel choices. It postulates that consumers make choices not to maximize utility but to minimize regret. Regret occurs when non-chosen alternatives performs better than the chosen one. The focal alternative is compared with all other alternatives in the choice set on an attribute by attribute basis to derive regret, as such, all other alternatives act as reference products of the focal alternative. In this model, incorporating additional comparison efect would mean adding more variables to the model that represent the distance between the focal product and the reference product. Besides, the RRM model can't estimate the partworth utility of diferent attributes, and therefore their usability by practitioners in redesigning the oferings or developing communication strategies is limited.

Another empirical model that considers some forms of comparisons in choice decision is due to Rooderkerk et al. [14]. While they still assume consumers maximize utility, their model incorporates three context efects by deriving the distances between the focal product and the compromise option (compromise efect), between the focal product and the dominating item (attraction efect), and between the focal product and other alternatives (similarity efect) in the attribute space. While modeling these context efects in this contextual-Random Utility Model (RUM) is theoretically attractive, the operationalization of similarity efect can be problematic when there are more than two attributes. Moreover, in choice-based conjoint experiments, very few choice sets have an asymmetrically dominated option, thereby making the operationalization of attraction efects infeasible. Despite these limitations, we consider this model as a competing model and provide details in the empirical analyses.

Table 1 shows the comparison between our proposed model with the standard choice model and other models that incorporate comparison efects or context efects. The standard choice model cannot examine the comparison efect in consumer choice decision. By contrast, the reference-dependent choice models can not only provide the partworth utility of diferent attribute levels, but also capture some special forms of comparison efects, i.e., reference efects. These models, however, mostly only consider one of the external or internal reference efects (on one or two attributes) and cannot examine comparison strategy. Similarly, the RRM model has incorporated the comparison efect by comparing the focal product with the external reference products in the choice set. This model does not take into account the consumer heterogeneity in comparison strategy. Moreover, the RRM model cannot provide the partworth utility of diferent attribute levels, which are important for firms when it comes to improving the design of market oferings. Finally, the Contextual-RUM model can only capture some specific forms of comparison efects from external references, and are not general enough to fully understand the comparison strategy in consumer choice.

Empirical models accounting for comparison efect.

<table><tr><td></td><td>The partworth utility of attribute levels</td><td>Comparison effect</td><td>External vs. internal reference</td><td>Comparison strategy</td></tr><tr><td>The proposed ME model</td><td>√</td><td>√</td><td>Both</td><td>√</td></tr><tr><td>Standard choice model [40]</td><td>√</td><td>X</td><td>X</td><td>X</td></tr><tr><td>Reference-dependent choice Model [10]</td><td>√</td><td>√</td><td>One of them</td><td>X</td></tr><tr><td>Regret minimization model [39]</td><td>X</td><td>√</td><td>Only External</td><td>X</td></tr><tr><td>Contextual RUM [14]</td><td>√</td><td>Compromise, attraction, and similarity effects</td><td>Only External</td><td>X</td></tr></table>

Compared to the competing models, the proposed model considers not only external reference products but also an internal reference product. Furthermore, the model enables researchers to better understand consumers' comparison strategy and sheds light on which reference products tend to be utilized in the comparison process. Our proposed model can also easily handle more complicated and realistic choice tasks for products with four or even more attributes (see Table 1).

## 3. Proposed ME model

We propose that the comparison standard a consumer uses could be the average product in the choice set (ave) [10], the most preferred product in the choice set (max) [23], the least preferred product in the choice set (min) [12], or an internal reference product (int) [22]. To the best of our knowledge, no research has compared the relative importance of the four reference products (with multiple attributes). More importantly, the utilization of diferent reference products can be determined by consumer characteristics [16]. However, little extant research examines consumers' comparison strategy $( \mathrm { i . e . }$ , the utilization of diferent reference products) empirically. Our proposed model helps us understand the comparison strategy and incorporate comparison efect into the random utility framework.

## 3.1. Model specification

Fig. 1 describes the components of the proposed ME model, originally introduced by [41]. Given a choice set C and comparison pro ducts $x _ { r } ,$ an individual n assigns utilit $\scriptstyle { \lceil u _ { n j } \mid c ^ { \mathrm { t o } } }$ alternative j:

$$
\begin{array}{r l} & u _ {n j | c} = g _ {n 1} \Bigg (\sum_ {k} \gamma_ {k} x _ {n j k | C} ^ {1} + \sum_ {k} \beta_ {1 k} (x _ {n j k | C} ^ {1} - x _ {n, \max, k | (C - j)} ^ {1}) / x _ {n, \max, k | (C - j)} ^ {1} \Bigg) + \\ & \qquad g _ {n 2} \Bigg (\sum_ {k} \gamma_ {k} x _ {n j k | C} ^ {1} + \sum_ {k} \beta_ {2 k} (x _ {n j k | C} ^ {1} - x _ {n, \min, k | (C - j)} ^ {1}) / x _ {n, \min, k | (C - j)} ^ {1} \Bigg) + \\ & \qquad g _ {n 3} \Bigg (\sum_ {k} \gamma_ {k} x _ {n j k | C} ^ {1} + \sum_ {k} \beta_ {3 k} (x _ {n j k | C} ^ {1} - x _ {n, a v e, k | (C - j)} ^ {1}) / x _ {n, a v e, k | (C - j)} ^ {1} \Bigg) + \\ & \qquad g _ {n 4} \Bigg (\sum_ {k} \gamma_ {k} x _ {n j k | C} ^ {1} + \sum_ {k} \beta_ {4 k} (x _ {n j k | C} ^ {1} - x _ {n, \operatorname{int}, k} ^ {1}) / x _ {n, \operatorname{int}, k} ^ {1} \Bigg) + \varepsilon_ {n j | C} \end{array} ,\tag{1}
$$

where $0 \leq g _ { n s } \leq 1$ and $\begin{array} { r } { \sum g _ { n s } = 1 , s = 1 , 2 , 3 , 4 . } \end{array}$

In Eq. $( 1 ) , x _ { n j k | C } ^ { } 1 _ { \mathbf { i } s }$ the level of focal product $j ^ { \prime } s$ kth attribute in choice set C and $\gamma _ { \mathbf { k } }$ is the coeficient of attribute k. ${ x _ { n , \mathrm { m a x } , k | ( C - j ) } } ^ { 1 } , x _ { n , \mathrm { m i n } , }$ k|(C $_ j ) \mathstrut ^ { 1 } , x _ { n , \ a \nu e , \ k | ( C - j ) } \mathstrut ^ { 1 }$ and $x _ { n , \mathrm { i n t } , \ k } ^ { \phantom { } } ^ { 1 }$ are the attribute levels of the three external reference products and an internal reference product respectively. Therefore, ${ \boldsymbol { \beta } } _ { s } = ( \beta _ { s 1 } , \beta _ { s 2 } , \ldots , \beta _ { s k } ) ^ { T } , s = 1 , 2 , 3 ,$ , 4 is the vector of k unknown parameters to be estimated, corresponding to the comparison efects of reference product s. Note that in Eq. (1) we adopt a soft clustering approach, namely, consumers can use multiple reference products as the comparison standard. The choice of diferent reference products being used is probabilistic and given by the gating function $( g _ { \mathrm { n s } } ) \colon$

$$
g _ {n s} = g _ {s} (x _ {n} ^ {2}, \theta) = \frac {\exp (\theta_ {s} x _ {n} ^ {2})}{\sum_ {l = 1} ^ {S} \exp (\theta_ {l} x _ {n} ^ {2})},\tag{2}
$$

where ${ x _ { n } } ^ { 2 }$ is the vector containing the characteristics of consumer n, including her/his income, gender, as well as her/his interest in and familiarity with the product category.

Compared with the traditional ME models [41], our proposed model has two special features that allow us to examine comparison strategy and comparison efect simultaneously. First, the proposed model incorporates diferent sets of variables through the gating functions (used to capture comparison strategy) and expert functions (used to capture the efects of attributes and comparison efects from the reference products). This feature helps us separately identify consumer heterogeneity in comparison strategy and the comparison efect against reference products. Second, the proposed model allows each expert function to have a diferent set of variables (i.e., comparison terms). The expert functions, therefore, include all the same product attribute variables, but each expert function includes a diferent set of comparison terms to investigate the comparison efect against that corresponding reference product. These two features are diferent from the typical marketing applications of similar models (e.g., the traditional ME model and the latent class model), in which the same set of variables are used in all expert functions or segments.

![](/api/attachments/MYP74UX7/fulltext/images/9ba718c3778de4f1087470204cab00b38629564ac795a88644f0dba900a262d9.jpg)  
Fig. 1. Components of the proposed ME model.

## 3.2. Competing models

In this section, we outline the competing empirical models. The first sub-section presents a series of models with no comparison efect (m1) or with some reference efects (m2–m6). These competing models are nested within our proposed model and represent simpler models that may lack some crucial elements of consumer choice process. The second sub-section outlines the two more recent approaches, namely the RRM [39] and contextual RUM model [14].

## 3.2.1. Competing models with reference efects

To examine whether comparison matters in consumer choice, we first compare the proposed ME model (m9) with six models with no comparison efect or with some reference efects.

3.2.1.1. Competing model I (m1: model-mnl). The traditional multinomial logit model that doesn't incorporate any comparison efect serves as the benchmark model. The utility of alternative j is determined only by its own attribute levels and the corresponding preference weights:

$$
u _ {n j | c} = \sum_ {k} \gamma_ {k} x _ {n j k | C} ^ {1} + \varepsilon_ {n j | C}\tag{3}
$$

3.2.1.2. Competing model II (m2: model-max). Based on competing model I, we further assume that consumers might use the most preferred product in the choice set as the reference product. In this model, the utility function has two components, a comparison-free component that is only determined by the product's attribute levels and a comparison component that is derived by the comparison with the most preferred product:

$$
u _ {n j | c} = \sum_ {k} \gamma_ {k} x _ {n j k | C} ^ {1} + \sum_ {k} \beta_ {1 k} (x _ {n j k | C} ^ {1} - x _ {n, \max, k | (C - j)} ^ {1}) / x _ {n, \max, k | (C - j)} ^ {1} + \varepsilon_ {n j | C}\tag{4}
$$

3.2.1.3. Competing model III (m3: model-min). Similarly, competing model III assumes that consumers might use the worst product as the reference product. This competing model can be derived by constraining $g _ { n 2 } = 1$ in Eq. (1).

$$
u _ {n j \mid c} = \sum_ {k} \gamma_ {k} x _ {n j k \mid C} ^ {1} + \sum_ {k} \beta_ {2 k} (x _ {n j k \mid C} ^ {1} - x _ {n, \min, k \mid (C - j)} ^ {1}) / x _ {n, \min, k \mid (C - j)} ^ {1} + \varepsilon_ {n j \mid C}\tag{5}
$$

3.2.1.4. Competing model IV (m4: model-ave). If consumers use the average product as the reference product, we can derive competing model IV by constraining $g _ { n 3 } = 1$

$$
u _ {n j \mid c} = \sum_ {k} \gamma_ {k} x _ {n j k \mid C} ^ {1} + \sum_ {k} \beta_ {3 k} (x _ {n j k \mid C} ^ {1} - x _ {n, a v e, k \mid (C - j)} ^ {1}) / x _ {n, a v e, k \mid (C - j)} ^ {1} + \varepsilon_ {n j \mid C}\tag{6}
$$

3.2.1.5. Competing model V (m5: model-int). In competing model $\mathrm { v , }$ we assume that consumers use the internal reference product as the comparison standard. This model specification can be obtained by constraining $g _ { n 4 } = 1$

$$
u _ {n j | c} = \sum_ {k} \gamma_ {k} x _ {n j k | C} ^ {1} + \sum_ {k} \beta_ {4 k} (x _ {n j k | C} ^ {1} - x _ {n, \mathrm{int}, k} ^ {1}) / x _ {n, \mathrm{int}, k} ^ {1} + \varepsilon_ {n j | C}\tag{7}
$$

In competing models II to $\mathrm { v , }$ only one reference product is con sidered. These competing models are all nested in the proposed model and they parallel what previous research has done, albeit generally by examining only one attribute, i.e., the reference price efect.

3.2.1.6. Competing model VI (m6: model-ref). We also consider a model that only includes the efect of comparison with the reference products but not the impact of product attribute levels $( \mathrm { i } . \mathsf { e } . , \gamma _ { k } = 0 )$ . This model specification is adopted by some previous research [23,42]. Rajendran and Tellis [23] assume that consumers won't respond to price and price relative to some reference point simultaneously.

$$
\begin{array}{c} u _ {n j | c} = g _ {n 1} \Bigg (\sum_ {k} \beta_ {1 k} (x _ {n j k | C} ^ {1} - x _ {n, \max, k | (C - j)} ^ {1}) / x _ {n, \max, k | (C - j)} ^ {1} \Bigg) + \\ g _ {n 2} \Bigg (\sum_ {k} \beta_ {2 k} (x _ {n j k | C} ^ {1} - x _ {n, \min, k | (C - j)} ^ {1}) / x _ {n, \min, k | (C - j)} ^ {1} \Bigg) + \\ g _ {n 3} \Bigg (\sum_ {k} \beta_ {3 k} (x _ {n j k | C} ^ {1} - x _ {n, a v e, k | (C - j)} ^ {1}) / x _ {n, a v e, k | (C - j)} ^ {1} \Bigg) + \\ g _ {n 4} \Bigg (\sum_ {k} \beta_ {4 k} (x _ {n j k | C} ^ {1} - x _ {n, \operatorname{int}, k} ^ {1}) / x _ {n, \operatorname{int}, k} ^ {1} \Bigg) + \varepsilon_ {n j | C} \end{array} ,\tag{8}
$$

where $0 \leq g _ { n s } \leq 1$ , and $\sum _ { s } g _ { n s } = 1 , s = 1 , 2 , 3 , 4 .$

## 3.2.2. Recent competing models without reference products

We next describe two recent approaches, namely the Regret Minimization model (RMM) [39] and Contextual RUM model [14]. Both models can only incorporate external reference points, i.e., the alternatives in current choice sets. While the two papers above motivate these competing models, we have suitably modified them so that they can be implemented with our data.

3.2.2.1. Competing model VII (m7: model-reg). In this model, the regret measure for each alternative is derived by summing up the regrets on each attribute in pairwise comparisons with all other alternatives in the choice set and reference products are not explicitly incorporated. The regret of an alternative i can be specified as:

$$
\widetilde {R} _ {n i | C} = \sum_ {j \neq i} \sum_ {\mathrm{k}} \ln (1 + \exp [ \beta_ {\mathrm{k}} ^ {*} (x _ {\mathrm{njk} | C} - x _ {n i \mathrm{k} | C}) ])\tag{9}
$$

The probability of choosing alternative i equals:

$$
P _ {n i | C} = \exp (- \widetilde {R} _ {n i | C}) / \sum_ {j = 1 \dots J} \exp (- \widetilde {R} _ {n j | C}).\tag{10}
$$

The above specification is directly taken from Chorus [24].

3.2.2.2. Competing model VIII (m8: model-cont). Still another competing model is the contextual-RUM model [14]. As pointed out earlier, it is not practical to include the similarity and attraction efects in our data context as we have four attributes. The compromise efect variable (comp\_dist) is constructed as the normalized compromise distance, comp $\begin{array} { r } { \_ d i s t = - \frac { \mathrm { d } _ { i M \mid C } } { \mathrm { m a x d } _ { j M \mid C } } , } \\ { \_ d i s t = - \frac { \mathrm { d } _ { i M \mid C } } { \mathrm { m a x d } _ { j M \mid C } } , } \end{array}$ and d measures the distance between

alternative j and the compromise option $\large ( x _ { M k \mid C } = \frac { \min x _ { j k } + \operatorname* { m a x } x _ { j k } } { 2 } \large )$ in the choice set. The utility function of this model has two parts, a comparison-free component that is only determined by the product's attribute levels and a context-dependent part:

Table 2  
Summary of model notations.

<table><tr><td>Models</td><td>Description</td><td>Theoretical bases</td><td>Notations</td></tr><tr><td>m1</td><td>Traditional choice model, no reference effect</td><td>Random utility maximization (RUM)</td><td> $\gamma_k$ : coefficient of attribute k</td></tr><tr><td>m2–m5</td><td>Traditional choice model, only one reference product</td><td>RUM, comparative judgment theory and reference-dependent theory</td><td> $\gamma_k$ : coefficient of attribute k; $\beta_s = (\beta_{s1}, \beta_{s2}, \dots, \beta_{sk})^T$ : coefficients of comparison terms relative to the reference product.</td></tr><tr><td>m6</td><td>Traditional choice model with four reference products, but no partworth utility</td><td>RUM, comparative judgment theory and reference-dependent theory</td><td> $\gamma_k$ : coefficient of attribute k;  $\beta_s = (\beta_{s1}, \beta_{s2}, \dots, \beta_{sk})^T$ : coefficients of comparison terms relative to reference point s; $\theta$ : coefficients of consumer characteristics.</td></tr><tr><td>m7</td><td>Regret minimization model</td><td>Random regret minimization (RRM)</td><td> $\beta_k$ : coefficient of attribute k</td></tr><tr><td>m8</td><td>Contextual RUM model</td><td>RUM and comparative judgment theory</td><td> $\beta$ : coefficient of context variables</td></tr><tr><td>m9</td><td>Proposed ME model</td><td>RUM, comparative judgment theory, and mixtures-of-experts (ME) model</td><td> $\gamma_k$ : coefficient of attribute k;  $\beta_s = (\beta_{s1}, \beta_{s2}, \dots, \beta_{sk})^T$ : coefficients of comparison terms relative to the reference product s; $\theta$ : coefficients of consumer characteristics.</td></tr></table>

$$
u _ {n j | c} = \sum_ {k} \gamma_ {k} x _ {n j k | C} ^ {1} + \beta \mathrm{d} _ {n j M | C} + \varepsilon_ {n j | C}.\tag{11}
$$

The notations of eight competing models are summarized in Table 2. While m1-m6 and m8 use the reference-dependent framework, m7 minimizes regret to derive consumers' choice decision. Based on the reference-dependent framework, the proposed model mixes diferent reference products through gating functions. This specification allows the proposed model not only to evaluate consumers' heterogeneous comparison strategies but also to explain the comparison efect.

## 3.3. Model estimation

For observed data $( x _ { \mathrm { n } } , y _ { \mathrm { n } } ) ,$ , there is a specific process (indicated by the state vectors $\boldsymbol { z } ^ { ( n ) } = ( \boldsymbol { z _ { s } } ^ { ( n ) } ) _ { s = 1 , 2 , . . . , s }$ that generates the outputy given the input $x _ { n } = ( { x _ { n } } ^ { 1 } , { x _ { n } } ^ { 2 } ) . \ z ^ { ( n ) }$ are unobserved and treated as missing data. In a general ME model, there are S experts $\{ e _ { s } \} _ { 1 } { } ^ { s }$ and a gate G which models the conditional density of $Y = \{ y _ { n } \} _ { 1 } ^ { \ N } \{$ given inputs and the specific comparison strategy as:

$$
f (Y \mid X, \psi) = \prod_ {n = 1} ^ {N} \sum_ {s = 1} ^ {S} g _ {s} (x _ {n} ^ {2}, \theta) f (y _ {n} \mid x _ {n} ^ {1}, \beta_ {s}),\tag{12}
$$

where the gating function $g _ { s } ( x _ { n } ^ { \ 2 } , \theta )$ quantifies the probability of com paring with reference product s (i.e., comparison strategy), and $f$ $( y _ { n } | { x _ { n } } ^ { 1 } , \beta _ { s } )$ is the density of $y _ { n }$ given the product attributes and com parison strategy. $\psi = ( \beta ^ { T } , \theta ^ { T } ) ^ { T }$ are parameters to be estimated, in which θ are the parameters of the gating function and $\beta = ( \beta _ { 1 } , \beta _ { 2 } , \cdots , \beta _ { s } )$ are the parameters of the probability model.

We apply the EM algorithm to estimate the parameters. This algorithm iterates through the Expectation and Maximization steps to maximize the log-likelihood function.

## 3.3.1. Expectation

The algorithm starts with some initial values of the parameters $\psi ^ { ( t ) }$ The E step postulates a distribution $P ( Z | X , Y , \psi ^ { ( t ) } )$ over the missing data Z given the initial values of the parameters and the observed data {X, Y}. Then, the missing data Z will be replaced by the posterior prob ability that observation n is generated by expert s:

$$
\widehat {p} _ {n s} = f (e _ {s} \mid x _ {n}, y _ {n}, \psi^ {(t)}) = \frac {g _ {s} (x _ {n} ^ {2} , \theta^ {(t)}) f (y _ {n} \mid x _ {n} ^ {1} , \beta_ {s} ^ {(t)})}{\sum_ {l = 1} ^ {S} g _ {l} (x _ {n} ^ {2} , \theta^ {(t)}) f (y _ {n} \mid x _ {n} ^ {1} , \beta_ {s} ^ {(t)})}\tag{13}
$$

## 3.3.2. Maximization

The M step finds the optimal parameters of the model that maximize the expected value of the complete data log-likelihood. Given the estimates for the a-posteriori probabilities ${ \widehat { p } } _ { n i } ,$ we obtain new estimates $\beta ^ { ( t + 1 ) }$ of the parameters by separately maximizing:

$$
Q (\psi^ {(t + 1)} | \psi^ {(t)}) = Q _ {1} (\theta^ {(t + 1)} | \psi^ {(t)}) + Q _ {2} (\beta_ {s} ^ {(t + 1)} | \psi^ {(t)}),\tag{14}
$$

$$
Q _ {1} (\theta^ {(t + 1)} | \psi^ {(t)}) = \sum_ {n = 1} ^ {N} \sum_ {s = 1} ^ {S} \widehat {p} _ {n s} \log (g _ {s} (x _ {n} ^ {2}, \theta^ {(t + 1)})),\tag{15}
$$

$$
Q _ {2} (\beta_ {s} ^ {(t + 1)} \mid \psi^ {(t)}) = \sum_ {n = 1} ^ {N} \sum_ {s = 1} ^ {S} \widehat {p} _ {n s} \log (f (y _ {n} \mid x _ {n} ^ {1}, \beta_ {s} ^ {(t + 1)})).\tag{16}
$$

Following prior literature, we use the Newton-Raphson method to obtain the standard errors of the parameters estimated by EM algorithm [43].

## 4. Empirical application

## 4.1. The conjoint experiment

## 4.1.1. Experiment design

We conducted a choice-based conjoint experiment to collect the data. Hypothetical smartphones were used as the stimuli. Pretests indicated that camera pixels (measured in megapixels), price (measured in CNY), CPU speed (measured in MHz) and screen size (measured in inches) were the most important attributes of smartphones. Thus, we included these four attributes to design the experiment. In the experiment, all the attributes have four levels except for price, which has five levels (see Table 3). This set of attribute levels had covered the most popular smartphone models in the market at the time of the survey.

We have four attributes and at least four levels for each attribute, and thus the full factorial design generates $4 ^ { 3 } \times 5 ^ { 1 } = 3 2 0$ alternatives. Forcing consumers to rank this huge number of alternatives or to choose from so many potential choice sets is not feasible. Thus, we develop a balanced design through the widely adopted %ChoiceEf macro in SAS to generate a generic, unlabeled design with all beta coeficients set to zero [44]]. This method allows us to have a tenchoice-set design, in which the alternative utilities are balanced and the design is approximately orthogonal. Each choice set contains four alternatives.

## 4.1.2. Experiment procedure

We invited 300 respondents through emails to participate in the survey. In the email, participants were invited to answer a questionnaire regarding their preference for smartphones. The invitation clearly indicated that all their answers would be kept confidential and be used only for academic purpose. We compensated the participants by

Table 3

Description of attribute levels.

<table><tr><td>Attribute</td><td>Levels</td></tr><tr><td>Screen size (inch)</td><td>2.4, 3, 3.5, 4</td></tr><tr><td>cpu speed (MHz)</td><td>400, 600, 800, 1000</td></tr><tr><td>Camera(million pixels)</td><td>2, 3, 5, 8</td></tr><tr><td>Price (CNY)</td><td>2000, 2500, 3000, 3500, 4000</td></tr></table>

entering them into a cash lottery for their participation. The ques tionnaire was created online using Qualtrics. At the end of the email, we enclosed the distribution link of the questionnaire and the participants could simply click the link to start the survey.

In the survey, the participants were first asked to complete ten choice tasks. In each of the choice sets, participants were asked to pick one smartphone out of four. To counter order bias, we randomized the order of choice sets for each participant. The choice task was followed by ten sets of ranking tasks for the given smartphones. In the ranking task, for each of the ten choice sets we asked the participants to rank the four alternatives without considering price. Therefore, we obtain the most preferred (the product ranked first, denoted as max), the least preferred (the product ranked fourth, denoted as min), as well as the average product (the average of product attributes, denoted as ave) in the choice set. Moreover, to identify the internal reference product, we asked the participants to reveal their current phone in use. If the participants were unable to provide the attributes of their internal reference product, we would derive these attributes according to the phone model provided by the participants. The product attributes would be set to zero if they were not present in the provided phone model. Finally, participants indicated their familiarity with and interest in smartphones on 7-point scales and provided their demographic information (e.g., income and gender).

## 4.1.3. Sample

In our experiment, the participants were approached by snowball sampling and most of them are students (including undergraduates, graduates, and post-graduates) from two major universities in North China. By the end of the study, 277 participants responded and completed the survey. However, three participants took very little time $( \mathrm { i . e . , } < 1 0 \mathrm { m i n } )$ to complete the survey, which is unusual considering that the average time taken is 35 min. We carefully checked their answers and found that they either gave the same answer or simply repeated from 1 to 4 to all the questions. Thus, we excluded them from the sample and the remaining 274 responses were used for further analyses.

Table 4 shows the descriptive statistics of the sample. Most of the participants (62.4%) were male and 91.3% of them were between 18 and 34 years old. As our sample mostly consisted of students, their income was relatively low (no more than 6000 RMB/month for 85% of the participants). However, > 50% of the participants had at least one smartphone, which is possibly because students were relatively interested in high-technology products.

## Table 4

Descriptive statistics of the sample.

<table><tr><td></td><td>Frequency</td><td>Percent (%)</td></tr><tr><td colspan="3">Gender</td></tr><tr><td>Male</td><td>171</td><td>62.4</td></tr><tr><td>Female</td><td>103</td><td>37.6</td></tr><tr><td colspan="3">Age</td></tr><tr><td>18–24</td><td>126</td><td>46.0</td></tr><tr><td>25–34</td><td>124</td><td>45.3</td></tr><tr><td>35–44</td><td>21</td><td>7.7</td></tr><tr><td>45–54</td><td>3</td><td>1.1</td></tr><tr><td colspan="3">Monthly income</td></tr><tr><td>1500 CNY or below</td><td>102</td><td>37.2</td></tr><tr><td>1500–2999 CNY</td><td>52</td><td>19.0</td></tr><tr><td>3000–4499 CNY</td><td>42</td><td>15.3</td></tr><tr><td>4500–5999 CNY</td><td>37</td><td>13.5</td></tr><tr><td>6000–7499 CNY</td><td>15</td><td>5.5</td></tr><tr><td>7500–8999 CNY</td><td>11</td><td>4.0</td></tr><tr><td>9000–14,999 CNY</td><td>11</td><td>4.0</td></tr><tr><td>15,000 CNY or above</td><td>4</td><td>1.5</td></tr><tr><td colspan="3">Smartphone ownership</td></tr><tr><td>No</td><td>128</td><td>46.7</td></tr><tr><td>Yes</td><td>146</td><td>53.3</td></tr></table>

## 4.2. Model comparison and fit

For each participant, the first seven choice decisions were used as the estimation sample and the remaining three choice decisions were used as the holdout sample. We used three criteria to compare the insample fit of diferent models: LL (Log Likelihood), AIC (Akaike Information Criterion), and BIC (Bayesian Information Criterion). To examine the out-of-sample validity and predictive ability, we calculate the out-of-sample hit ratio, MAE (mean absolute error), and RLH (root likelihood) of diferent models. We conducted two sets of comparisons. First, we compared the traditional multinomial model (m1-mnl) with the models that only consider one reference product $( \mathrm { i . e . , m 2 – m 5 } )$ and with the model that only considers the four reference products but not product attribute levels per se (i.e., m6). Through this comparison, we derive whether comparison matters in consumer choice. Second, we compared the proposed model with each of the competing models and examined whether our proposed model could perform better.

Since m1 is nested in models m2–m5, we calculate the likelihood ratio between m1 and each of the competing models (see Comparison 1 and LR1 in Table 5). The results show that LR1 statistics between m1 and each of m2–m5 are all significant $( p < 0 . 0 0 1 )$ , indicating that choice models that incorporate one reference product can better explain consumer choice decision than the traditional choice model. In addition, competing model m6 that only considers comparison efect (but no partworth utilities of product attributes) also outperforms the traditional model. These findings further reinforce the conclusion that comparison matters in consumer choice decision.

The results in Table 5 also suggest that the proposed model has better in-sample fit in terms of LL, AIC, and BIC. In particular, the proposed model m9 has the largest LL, lowest AIC and BIC among the nine models. As m1–m6 are all nested in the proposed model, we use the likelihood ratio test to compare the proposed model with each of these competing models. The LR2 statistics between m9 and models m1-m6 show that the proposed model that incorporates multiple reference products fits the data better $( p < 0 . 0 0 1 )$ , suggesting that consumers might use multiple reference products as the comparison products in making a choice decision. This is consistent with Mayhew and Winer [14,17], who find that consumers use multiple reference points to evaluate prices while making purchase decisions. The proposed model also outperforms the regret minimization model and the contextual RUM model in terms of log-likelihood, AIC, and BIC.

We next compared the out-of-sample hit ratio, MAE and RLH of diferent models. As shown in Table $^ { 6 , }$ the hit ratios of models m2–m6 were higher than that of m1. The MAE of models m2–m6 were lower than that of m1. Among all the models, the proposed ME model has the highest out-of-sample hit ratio of 47.3%, lowest MAE of 16.39, and comparatively higher RLH of 0.278, indicating that the proposed model outperforms all the competing models in terms of out-of-sample pre diction.

## 4.3. Main findings

## 4.3.1. The impact of reference products on consumer choice

The estimates of expert functions are shown in Table 7. We find that screen size, CPU speed, and camera pixels positively afect consumer choice decision while price has a negative impact on the probability of choosing a smartphone. This indicates that consumers are inclined to choose smartphones with a larger screen, higher processing speed, higher camera pixels, and a lower price. These findings are consistent with our expectation. Compared to the proposed model (m9), the other models (e.g., m1-m5), however, might have underestimated the positive efect of screen size, CPU speed, and camera pixels and overestimated the negative efect of price. For example, the coeficients of screen size, CPU speed, and camera pixels in m1 are 63.77%, 37.21%, and 52.86% smaller, respectively, than those in the proposed model. We test these diferences by bootstrapping and find that they are all

Table 5  
Model comparisons (in-sample).

<table><tr><td></td><td>LL</td><td>AIC</td><td>BIC</td><td>No. of parameters</td><td>Comparison 1</td><td>LR1</td><td>Comparison 2</td><td>LR2</td></tr><tr><td>(m1) model-mnl</td><td>-2465.8</td><td>4939.7</td><td>4961.8</td><td>4</td><td></td><td></td><td>(m1) vs (m9)</td><td>363.92***</td></tr><tr><td>(m2) model-max</td><td>-2427.2</td><td>4870.4</td><td>4914.9</td><td>8</td><td>(m2) vs (m1)</td><td>77.2***</td><td>(m2) vs (m9)</td><td>286.72***</td></tr><tr><td>(m3) model-min</td><td>-2447.4</td><td>4910.8</td><td>4955.3</td><td>8</td><td>(m3) vs (m1)</td><td>36.8***</td><td>(m3) vs (m9)</td><td>327.12***</td></tr><tr><td>(m4) model-ave</td><td>-2456.4</td><td>4928.8</td><td>4973.3</td><td>8</td><td>(m4) vs (m1)</td><td>18.8***</td><td>(m4) vs (m9)</td><td>345.12***</td></tr><tr><td>(m5) model-int</td><td>-2443.9</td><td>4903.8</td><td>4948.3</td><td>8</td><td>(m5) vs (m1)</td><td>43.8***</td><td>(m5) vs (m9)</td><td>320.12***</td></tr><tr><td>(m6) model-ref</td><td>-2374.1</td><td>4810.1</td><td>4982.5</td><td>31</td><td></td><td></td><td>(m6) vs (m9)</td><td>180.45***</td></tr><tr><td>(m7) model-reg</td><td>-2407.8</td><td>4823.6</td><td>4845.8</td><td>4</td><td></td><td></td><td></td><td></td></tr><tr><td>(m8) model-cont</td><td>-2433.0</td><td>4936.0</td><td>4903.8</td><td>5</td><td></td><td></td><td></td><td></td></tr><tr><td>(m9) model-ME</td><td>-2283.8</td><td>4637.7</td><td>4832.2</td><td>35</td><td></td><td></td><td></td><td></td></tr></table>

Note. \*\*\* $p \ : < \ : 0 . 0 0 1$ .

## Table 6

Out-of-sample performance.

<table><tr><td>Model</td><td>Hit Ratio</td><td>MAE</td><td>RLH</td></tr><tr><td>(m1) model-mnl</td><td>0.41</td><td>29.50</td><td>0.277</td></tr><tr><td>(m2) model-max</td><td>0.417</td><td>18.86</td><td>0.272</td></tr><tr><td>(m3) model-min</td><td>0.411</td><td>26.34</td><td>0.278</td></tr><tr><td>(m4) model-ave</td><td>0.413</td><td>28.04</td><td>0.277</td></tr><tr><td>(m5) model-int</td><td>0.414</td><td>27.07</td><td>0.278</td></tr><tr><td>(m6) model-comp</td><td>0.439</td><td>18.34</td><td>0.277</td></tr><tr><td>(m7) model-reg</td><td>0.41</td><td>29.50</td><td>0.271</td></tr><tr><td>(m8) model-cont</td><td>0.42</td><td>19.65</td><td>0.268</td></tr><tr><td>(m9) model-ME</td><td>0.473</td><td>16.39</td><td>0.278</td></tr></table>

statistically significant $( p s < 0 . 0 0 1 ) .$ <sup>1</sup> Thus, incorporating comparison efect into the discrete choice model is important for us to fully un derstand the partworth utilities of diferent attribute levels.

Regarding comparison efect, the four reference products seem to have diferent efects on consumer choice decision. First, according to the proposed model (m9), when consumers compare with the most preferred product, the probability of choosing a smartphone is sig nificantly afected by all the comparison variables. Though screen size, CPU speed, and camera pixels in general have positive impacts on the probability of choosing a smartphone, the impact of the comparisons with the most preferred product are negative. For price, its comparison with the most preferred product also has a negative impact. Therefore, ceteris paribus, consumers prefer a focal product more if the most preferred product has higher values on screen size, CPU speed, camera pixels, and price. The most preferred product seems to serve as an extreme option in the choice set, and the focal product as a compromise option becomes more attractive to consumers.

Second, when consumers compare with the least preferred product, the probability of choosing the focal product is afected by most of the comparison variables but not the comparison on price. Ceteris paribus, the larger the screen size, the lower the CPU speed and camera pixels of the least preferred product (relative to the focal product), the more attractive the focal product is to consumers. In other words, the worse the least preferred product on important attributes $( \mathrm { i . e . , }$ , CPU speed and camera pixels) relative to the focal product, the more likely that the consumers choose the focal product. The sign of the comparison efect for screen size is negative, which may be because of the non-monotonic preference for screen size among consumers, i.e., not everyone prefers a larger screen size to a smaller one.

For consumer $n ,$ maxscrr is $\begin{array} { r } { ( x _ { n j k / C } { ^ 1 } - x _ { n , \mathrm { m a x } , k / ( C - j ) } { ^ 1 } ) / { x _ { n , \mathrm { m a x } , k / ( C - j ) } } { ^ 1 } , } \end{array}$ in which attribute k refers to screen size. The parameter corresponding to this comparison variable is $\beta _ { 1 1 }$ in Eq. (1). The variables maxcpur, maxcamr, and maxprir are operationalized in a similar vein. Variables starting with “min”, “ave”, and “int” represent the comparison variables related to the worst, average, and internal reference products, respectively.

Regarding the other two reference products, there is no a-priori expectation of the sign of comparison efect because consumers may have idiosyncratic preference and various context efects may come into play in unpredictable ways. When consumers use the average product as the reference product, the comparison variables regarding CPU speed and camera pixels are significant $( p < 0 . 0 5 )$ . In addition to the generally positive impacts of CPU speed and camera pixels, higher camera pixels and lower CPU speed of the average product (relative to the focal product) will make the focal product more attractive and more likely to be chosen. This is possibly because CPU speed is generally considered more important than camera pixels for smartphone consumers. As a result, when there is a trade-of between camera pixels and CPU speed, the comparison advantage on CPU speed is more influential and positively afect the probability of choosing the focal product. We find no comparison efect on screen size and price for the average product.

Finally, with respect to the internal reference product, the probability of choosing the focal product is significantly afected by the comparison efect regarding screen size, CPU speed, and price. The larger the screen size, and the higher the CPU speed and price of the internal reference product compared to those of the focal product, the more attractive the focal product will be.

## 4.3.2. Consumer heterogeneity in the utilization of reference products

To understand consumers' comparison strategy, we substitute the estimated parameters (θ ) in the gating functions $g _ { \mathrm { n } i }$ and then average them over consumers. The results show that 51.8% of the participants use the most preferred product as the reference product, 35% of them use the internal reference product, 9.2% of them use the average product, while only 4% use the least preferred product as the reference product.

In model estimation results (see Table 8), the most preferred product serves as the baseline such that the intercepts in gating functions represent the utilization of each reference product relative to the most preferred product. A positive intercept indicates that the corresponding reference product is more likely to be used than the most preferred product, while a negative intercept indicates the opposite. Overall, compared with those of the proposed model (m9), the intercepts of competing model m6 that only includes comparison efect have the same directions but difer in magnitude. For example, in the proposed model, the least preferred product is less likely to be used as the reference product than the most preferred product $( - 9 . 4 3 2 , p < 0 . 0 1 )$ , while in m6 the intercept for the least preferred product is estimated to be −7.554, which is smaller in magnitude than that in our proposed model. The efects of consumer characteristics in competing model m6, however, are quite diferent from those of the proposed model m9. This is because the competing model m6 does not include the partworth utilities of product attributes, which might have biased estimates of comparison efect. Thus, we mainly discuss the detailed estimation results of the proposed ME model.

Table 7  
Parameter estimates of diferent models.

<table><tr><td>Variables</td><td>(m1) model-mnl</td><td>(m2) model-max</td><td>(m3) model-min</td><td>(m4) model-ave</td><td>(m5) model-int</td><td>(m6) model-comp</td><td>(m7) model-reg</td><td>(m8) model-cont</td><td>(m9) model-ME</td></tr><tr><td>Screen</td><td>0.217***(0.025)</td><td>0.378***(0.060)</td><td>0.271***(0.060)</td><td>0.086(0.048)</td><td>0.522***(0.101)</td><td></td><td>0.106***(0.013)</td><td>0.216***(0.025)</td><td>0.599***(0.113)</td></tr><tr><td>CPU</td><td>0.464***(0.032)</td><td>0.710***(0.061)</td><td>0.476***(0.069)</td><td>0.327***(0.057)</td><td>0.516***(0.056)</td><td></td><td>0.274***(0.018)</td><td>0.47***(0.033)</td><td>0.739***(0.085)</td></tr><tr><td>Camera</td><td>0.214***(0.030)</td><td>0.518***(0.056)</td><td>0.052(0.061)</td><td>0.1067*(0.054)</td><td>0.28***(0.037)</td><td></td><td>0.149***(0.018)</td><td>0.208***(0.031)</td><td>0.454***(0.062)</td></tr><tr><td>Price</td><td>-0.568***(0.037)</td><td>-0.457***(0.064)</td><td>-0.807***(0.074)</td><td>-0.532***(0.062)</td><td>-0.478***(0.048)</td><td></td><td>-0.34***(0.022)</td><td>-0.565***(0.037)</td><td>-0.137(0.073)</td></tr><tr><td>comp_dist</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-0.001(0.09)</td><td></td></tr><tr><td>maxscrr</td><td></td><td>-0.201**(0.067)</td><td></td><td></td><td></td><td>0.171*(0.072)</td><td></td><td></td><td>-0.508**(0.160)</td></tr><tr><td>maxcpur</td><td></td><td>-0.321***(0.065)</td><td></td><td></td><td></td><td>0.107(0.101)</td><td></td><td></td><td>-0.433**(0.132)</td></tr><tr><td>maxcamr</td><td></td><td>-0.377***(0.063)</td><td></td><td></td><td></td><td>0.230*(0.106)</td><td></td><td></td><td>-0.576***(0.106)</td></tr><tr><td>maxprir</td><td></td><td>-0.123(0.068)</td><td></td><td></td><td></td><td>-1.358***(0.161)</td><td></td><td></td><td>-1.083***(0.151)</td></tr><tr><td>minscrr</td><td></td><td></td><td>-0.075(0.068)</td><td></td><td></td><td>0.165(0.101)</td><td></td><td></td><td>-2.002**(0.773)</td></tr><tr><td>mincpur</td><td></td><td></td><td>-0.028(0.077)</td><td></td><td></td><td>0.684***(0.124)</td><td></td><td></td><td>3.379**(1.287)</td></tr><tr><td>mincamr</td><td></td><td></td><td>0.203**(0.064)</td><td></td><td></td><td>0.523***(0.090)</td><td></td><td></td><td>2.694*(1.202)</td></tr><tr><td>minprir</td><td></td><td></td><td>0.321***(0.077)</td><td></td><td></td><td>-0.046(0.096)</td><td></td><td></td><td>0.298(0.466)</td></tr><tr><td>avescrr</td><td></td><td></td><td></td><td>0.162**(0.051)</td><td></td><td>0.631***(0.127)</td><td></td><td></td><td>0.0002(0.215)</td></tr><tr><td>avecpur</td><td></td><td></td><td></td><td>0.166**(0.059)</td><td></td><td>1.736***(0.278)</td><td></td><td></td><td>0.994***(0.293)</td></tr><tr><td>avecamr</td><td></td><td></td><td></td><td>0.119*(0.054)</td><td></td><td>-0.309(0.223)</td><td></td><td></td><td>-0.606***(0.164)</td></tr><tr><td>aveprir</td><td></td><td></td><td></td><td>-0.040(0.060)</td><td></td><td>-1.120***(0.188)</td><td></td><td></td><td>-0.4332(0.222)</td></tr><tr><td>intscrr</td><td></td><td></td><td></td><td></td><td>-0.519**(0.166)</td><td>0.779***(0.142)</td><td></td><td></td><td>-0.629**(0.203)</td></tr><tr><td>intcpur</td><td></td><td></td><td></td><td></td><td>-0.106(0.102)</td><td>0.880***(0.212)</td><td></td><td></td><td>-1.086***(0.179)</td></tr><tr><td>intcamr</td><td></td><td></td><td></td><td></td><td>-0.205**(0.065)</td><td>-0.292(0.193)</td><td></td><td></td><td>-0.257(0.145)</td></tr><tr><td>intrprir</td><td></td><td></td><td></td><td></td><td>-0.435**(0.149)</td><td>-1.971***(0.630)</td><td></td><td></td><td>-0.91**(0.339)</td></tr></table>

Notes. Numbers in parentheses are standard errors; \*\*\*p < 0.001, \*\*p < 0.01; \*p < 0.05.

Table 8 shows that there exists consumer heterogeneity in terms of the utilization of diferent reference products. In particular, the probability of utilizing the average product as the reference product is higher for consumers who are less familiar with the product $( - 0 . 5 7 2 ,$ $p \ : < \ : 0 . 0 5 )$ . This finding is consistent with prior literature on the in ference efect of constructed consumer preference, which suggests that novice consumers are more likely to use the average among what is available to form their preference [6]. In addition, when consumers are less familiar with the product category, the average or compromising option in a choice set is a safer alternative to compare with and comparing with this reference is easier to justify [8]. Moreover, we find that the probability of utilizing the average product as the reference product is higher for consumers who are more interested in the product (1.031, $p \ : < \ : 0 . 0 1 )$

The results also show that female consumers are more likely to use the internal reference product (0.751, p < 0.05). Very little prior research has investigated the role of gender in the utilization of diferent reference products. However, prior research suggests that male con sumers tend to use the most salient cues while female consumers tend to utilize all information available [45]. In our research context, we conjecture that male consumers tend to use the most salient external reference products in the choice set, while female consumers are more comprehensive and relatively more likely to use the internal reference product than male consumers.

The above findings regarding consumer utilization of reference products can be of great practical use to marketers in deciding their positioning and communication strategies for their target segments of interest.

## 5. Conclusion and discussion

We propose a mixtures-of-experts model to incorporate consumers utilization of multiple reference products, both internal and external, with multiple attributes. Our model also allows us to examine consumer heterogeneity in the utilization of diferent reference products. We test the proposed model with the empirical data collected by a choice-based conjoint experiment involving a durable product, smartphone. Results show that the proposed model outperforms a variety of competing models on both in-sample fit and out-of-sample prediction. The findings indicate that consumers may make elaborate comparisons while making a choice. These findings provide empirical evidence that models incorporating multiple reference products with multiple-attributes can better explain consumer choice. Moreover, we find evidence for consumers using four types of reference products in the comparison process of durable goods like smartphones, or a probabilistic combination of these four. Empirical results for smartphones show that about half the subjects (above 51%) use the most preferred product as the reference product and the internal reference product is also used by many subjects (about

Table 8  
Parameter estimates for gating function.

<table><tr><td>Variables</td><td></td><td>(m6) model-comp</td><td>(m9) model-ME</td></tr><tr><td rowspan="5">Gating function parameters-min</td><td>Intercept</td><td>-7.554*(3.115)</td><td>-9.432*(4.156)</td></tr><tr><td>log(income)</td><td>0.670(0.358)</td><td>0.862(0.489)</td></tr><tr><td>Female</td><td>1.00*(0.438)</td><td>-0.056(0.820)</td></tr><tr><td>Familiarity</td><td>0.192(0.158)</td><td>-0.234(0.259)</td></tr><tr><td>Interest</td><td>0.162(0.164)</td><td>0.171(0.249)</td></tr><tr><td rowspan="5">Gating function parameters-ave</td><td>Intercept</td><td>-4.356(3.788)</td><td>-6.404(4.348)</td></tr><tr><td>log(income)</td><td>0.090(0.463)</td><td>0.166(0.512)</td></tr><tr><td>Female</td><td>-0.726(0.655)</td><td>-0.365(0.683)</td></tr><tr><td>Familiarity</td><td>0.133(0.184)</td><td>-0.572*(0.241)</td></tr><tr><td>Interest</td><td>0.513*(0.212)</td><td>1.031**(0.315)</td></tr><tr><td rowspan="5">Gating function parameters-int</td><td>Intercept</td><td>-10.291**(3.900)</td><td>-2.683(2.244)</td></tr><tr><td>log(income)</td><td>1.031*(0.449)</td><td>0.226(0.267)</td></tr><tr><td>Female</td><td>0.796(0.546)</td><td>0.751*(0.358)</td></tr><tr><td>Familiarity</td><td>0.325(0.186)</td><td>0.002(0.124)</td></tr><tr><td>Interest</td><td>0.056(0.190)</td><td>0.036(0.120)</td></tr></table>

Notes. Numbers in parentheses are standard errors; $^ { * * * } p < 0 . 0 0 1 , ^ { * * } p < 0 . 0 1 ;$ ${ } ^ { \ast } p \ < \ 0 . 0 5 .$

35%). In contrast, the average product (about 9%) and the least preferred product (about 4%) are rare. Consistent with prior research, the most preferred product might not be chosen by consumers but they can serve as the reference product and the presence of these relatively extreme options will increase the share of the focal product [46].

Our ME model can be readily applied to other product categories and the findings regarding consumers' utilization of diferent reference products may provide important implications for business decision making and decision support systems helping them in the process. Consumers with diferent characteristics $( \mathbf { e . g . }$ , gender, product famil iarity, and interest in product) may difer in utilization of diferent reference products. Our results from the smartphone category show that consumers who are more familiar with the product are less likely to use the average (vs. the most preferred) product as the reference. On the other hand, consumers with more interest in the product utilize the average product as a reference point more often. Thus, product familiarity and product interest could be potentially used as market segmentation variables by the smartphone marketers to support their product positioning decisions. More importantly, the proposed ME model in corporates the efects of comparison with both external and internal reference products and can predict consumer preference more accurately. Thus, it has the potential to be applied to many decision support systems. Managers can not only use information obtained from Choice Based Conjoint experiments and our model in getting direct insights about product positioning for diferent target segments (not just what attribute to highlight, but also which competing product to highlight) and communication messages, but also in improving recommendation engines. State of the art hybrid recommendation systems rely on content matching and collaborative filtering. The gating function estimates in our model provides basis for improving collaborative filtering and also provides guidance for what kind of choices to present to customers in order to subtly nudge them to a desirable option. Thus, when applied to product recommendation agents (PRAs), our model could provide a better approximations of consumers' preference structures, thereby helping firms generate more accurate and efective product recommendations [35].

Some of this study's limitations provide avenues of future research. One limitation is that we assume that consumers' utility increases/decreases monotonically with the increase of attribute values. While this is sensible in our research context, there are instances that preference may exhibit non-linear relationship with attributes values [41]. Second, we do not include no-choice option in the choice-based conjoint experiment and this may lead to biased results when respondents who find alternatives unattractive or want to delay their decisions are forced to make a choice [47]. Further, especially in a longer choice-based conjoint experiment involving more products and attributes, the phenomenon of learning about reference points as the experiment progresses may also be an interesting option to extend the scope of research. Future research may find it fruitful to investigate some of these limitations by using diferent products, both frequently purchased products and durable goods, in diferent cultural and economic contexts, using data from transaction data with more general types of attributes. We hope that such an efort will lead to more applications of the proposed ME model in various types of decision support systems.

## Acknowledgement

This work was financially supported by the National Social Science Fund of China (NSSFC grant no. 16BGL087) and the National Natural Science Foundation of China (Grant No. 71502182 and 71332006).

## References

[1] X.G. Luo, C.K. Kwong, J.F. Tang, Y.L. Tu, Optimal product positioning with con sideration of negative utility efect on consumer choice rule, Decision Support System 54 (2012) 402–413.

[2] W. Tan, C. Tan, H. Teo, Consumer-based decision aid that explains which to buy: decision confirmation or overconfidence bias? Decision Support System, 53 2012 pp. 127–141.

[3] J. Song, D. Jones, N. Gudigantala, The efects of incorporating compensatory choice strategies in web-based consumer decision support systems, Decision Support System, 43 2007, pp. 359–374.

[4] T. Mussweiler, Comparison processes in social judgment: mechanisms and con sequences, Psychological Review 110 (2003) 472–489.

[5] O. Amir, J. Levav, Choice construction versus preference construction: the instability of preferences learned in context, Journal of Marketing Research 45 (2008) 145-158.

[6] D. Prelec, B. Wernerfelt, Z. Florian, The role of inference in context efects: inferring what you want from what is svailable, Journal of Consumer Research 24 (1997) 118–126.

[7] J. Huber, J.W. Payne, C. Puto, Adding asymmetrically dominated alternatives: violations of regularity and the similarity hypothesis, Journal of Consumer Research 9 (1982) 90–98.

[8] I. Simonson, Choice based on reasons: the case of attraction and compromise ef

[9] J.G. Lynch Jr., D. Chakravarti, A. Mitra, Contrast efects in consumer judgments: changes in mental representations or in the anchoring of rating scales? Journal of Consumer Research 18 (1991) 284–297.

[10] M. Bhargava, J. Kim, R.K. Srivastava, Explaining context efects on choice using a model of comparative judgment, Journal of Consumer Psychology 9 (2000) 167–177.

[11] D. Kahneman. A. Tversky. Prospect theory: an analysis of decision under risk. Econometrica 47 (1979) 263–291.

[12] R. Kivetz, O. Netzer, V. Srinivasan, Alternative models for capturing the compro mise effect, Journal of Marketing Research 41 (2004) 237–257.

[13] A.Y.S.J. Orhun, Optimal product line design when consumers exhibit choice set

[15] A. Tversky. D. Kahneman. Loss aversion in riskless choice: a reference-dependent model, The Ouarterly Journal of Economics 106 (1991) 1039–1061.

[16] D. Klapper, C. Ebling, J. Temme, Another look at loss aversion in brand choice data: can we characterize the loss averse consumer? International Journal of Research ir Marketing 22 (2005) 239–254

[17] G.E. Mayhew, R.S. Winer, An empirical analysis of internal and external reference prices using scanner data, Journal of Consumer Research 19 (1992) 62–70.

[18] Y.N.Z. Foutz, Role of Reference Points in Consumer Choice and Product Design:

[19] R.S. Winer, A reference price model of brand choice for frequently purchased products, Journal of Consumer Research 13 (1986) 250–256.

[20] C. Chorus, S. van Cranenburgh, T. Dekker, Random regret minimization for con sumer choice modeling: assessment of empirical evidence, Journal of Business Research 67 (2014) 2428–2436

[21] W. Fan, M. Gordon, P. Pathak, On linear mixture of expert approaches to in formation retrieval, Decision Support System 42 (2006) 975–987.

[22] B.G.S. Hardie, E.J. Johnson, P.S. Fader, Modeling loss aversion and reference de pendence efects on brand choice, Marketing Science 12 (1993) 378–394.

[23] K.N. Rajendran, G.J. Tellis, Contextual and temporal components of reference price, Journal of Marketing 58 (1994) 22–34.

[24] C.G. Chorus, A new model of random regret minimization, European Journal of Transport and Infrastructure Research 10 (2010) 181–196.

[25] H. Helson, Adaptation Level Theory: An Experimental and Systematic Approach to Behavior, Harper and Row, New York, 1964.

[26] R.W. Niedrich, S. Sharma, D.H. Wedell, Reference price and price perceptions: a comparison of alternative models, Journal of Consumer Research 28 (2001) 339–354.

[27] A. Parducci, Category judgment: a range-frequency model, Psychological Review 72 (1965) 407–418.

[28] A. Parducci, Happiness, Pleasure, and Judgment: The Contextual Theory and Its Applications, Lawrence Erlbaum Associates, Inc, Mahwah, Erlbaum NJ, 1995, pp. 50–68.

[29] J. Volkmann, Scales of judgment and their implications for social psychology, in: J.H. Rohrer, M. Sherif (Eds.), Social Psychology at the Crossroads, the University of Oklahoma lectures in social psychology, Harper, Oxford, England, 1951, pp. 273-298.

[30] R. Dhar, S.M. Nowlis, S.J. Sherman, Comparison efects on preference construction, Journal of Consumer Research 26 (1999) 293–306.

[31] R. Dhar, I. Simonson, The efect of the focus of comparison on consumer pre ferences Journal of Marketing Research 29 (1992) 430–440

[32] D.A. Houston, S.J. Sherman, S.M. Baker, The influence of unique features and direction of comparison of preferences, Journal of Experimental Social Psychology 25 (1989) 121–141.

[33] M. Zhou, Reference price efect and its implications for decision making in online auctions: an empirical study, Decision Support System, 54 2012, pp. 381–389.

[34] M. Scholz, V. Dorner, M. Franz, O. Hinz, Measuring consumers' willingness to pay with utility-based recommendation systems, Decision Support System, 72 2015, pp.

[35] B. Xiao, I. Benbasat, An empirical examination of the influence of biased persona lized product recommendations on consumers' decision making outcomes Decisior Support System, 110 2018, pp. 46–57.

[36] N. Tereyağoğlu, P.S. Fader, S. Veeraraghavan, Multiattribute loss aversion and re ference dependence: evidence from the performing arts industry, Management Science 64 (2017) 421–436

[37] A. Tversky, I. Simonson, Context-dependent preferences, Management Science 39 (1993)1179-1189.

[38] W.A. Kamakura, R.K. Srivastava, Predicting choice shares under conditions of brand

interdependence, Journal of Marketing Research 21 (1984) 420–434.

[39] C.G. Chorus, Random Regret-Based Discrete Choice Modeling: A Tutorial, Springer Science & Business Media, Dordrecht, 2012, pp. 1–55.

[40] M.E. Ben-Akiva, S.R. Lerman, Discrete Choice Analysis: Theory and Application to Travel Demand, MIT press, Cambridge, MA, 1985, pp. 31–59.

[41] M.I. Jordan, R.A. Jacobs, Hierarchical mixtures of experts and the EM algorithm Neural Computation 6 (1994) 181–214.

[42] T. Mazumdar, P. Papatla, Loyalty diferences in the use of internal and external reference prices, Marketing Letters 6 (1995) 111–122.

[43] B. Grün, F. Leisch, Identifiability of finite mixtures of multinomial logit models with varying and fixed efects, Journal of Classification 25 (2008) 225.

[44] W.F. Kuhfeld, R.D. Tobias, M. Garratt, Eficient experimental design with marketing research applications, Journal of Marketing Research 31 (1994) 545–557.

[45] J. Meyers-Levy, D. Maheswaran, Exploring diferences in males' and females' processing strategies, Journal of Consumer Research 18 (1991) 63–70.

[46] R. Kivetz, I. Simonson, Earning the right to indulge: efort as a determinant of customer preferences toward frequency program rewards, Journal of Marketing Research 39 (2002) 155–170

[47] R. Haaijer, W.A. Kamakura, M. Wedel, The ‘no-choice’ alternative in conjoint choice

Ping Wang Assistant Professor, College of Economics and Management & China-Africa International Business School, Zhejiang Normal University, Jinhua 321004, China. Research areas include recommendation system, mixture models, choice models and Bayesian method.

Luping Sun Associate Professor at Business School, Central University of Finance and Economics, Beijing 100081, China. Research interests include big data marketing, Bayesian methods and choice model.

Rakesh Nirai Associate Professor at Weatherhead School of Management. Case Western Reserve University, Cleveland, OH 44106 USA. Research interests include both analytical and empirical modeling of marketing strategy in such areas as customer relationship management (CRM), retailing and social media marketing.

Jaihak Chung Professor of Marketing, School of Business Administration, Sogang University, Seoul, Korea, and Afiliate Professor, IESEG School of Management, France. Research areas include social media marketing, recommendation systems, log-Linear models and collaborative filtering.

Meng Su Founder and CEO of Baifendian Technology, the first recommendation engine and big-data applications company in China. Research areas include Customer Lifetime Value analysis, marketing models for new product introduction and competition, re commendation engine and recommendation system, invidualized and personalized mar keting models, Bayesian method.

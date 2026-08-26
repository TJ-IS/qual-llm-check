---
otero_id: 28598
otero_key: "HRRXA4H7"
title: "Probing Digital Footprints and Reaching for Inherent Preferences: A Cause-Disentanglement Approach to Personalized Recommendations"
authors: "Cong Wang; Yansong Shi; Xunhua Guo; Guoqing Chen"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2023.0181"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Probing Digital Footprints and Reaching for Inherent Preferences: A Cause-Disentanglement Approach to Personalized Recommendations

Cong Wang,<sup>a</sup> Yansong Shi,<sup>b,c,</sup>\* Xunhua Guo,<sup>d</sup> Guoqing Chen<sup>c</sup>

<sup>a</sup> Guanghua School of Management, Peking University, Beijing 100871, China; <sup>b</sup> School of Management, Fudan University, Shanghai 200433, China; <sup>c</sup> School of Economics and Management, Tsinghua University, Beijing 100084, China; <sup>d</sup> China Retail Research Center, School of Economics and Management, Tsinghua University, Beijing 100084, China

\*Corresponding author

Contact: wangcong@gsm.pku.edu.cn, https://orcid.org/0000-0002-5300-0122 (CW); shiys@fudan.edu.cn, https://orcid.org/0000-0002-4040-8831 (YS); guoxh@sem.tsinghua.edu.cn, https://orcid.org/0000-0002-7243-4292 (XG); chengq@sem.tsinghua.edu.cn (GC)

Received: March 23, 2023 Revised: February 11, 2024; July 4, 2024 Accepted: August 11, 2024 Published Online in Articles in Advance: September 16, 2024

https://doi.org/10.1287/isre.2023.0181

Copyright: © 2024 INFORMS

Abstract. The abundance of multiple types of consumer digital footprints recorded on e-commerce platforms has fueled the design of personalized recommender systems for decision support. However, capturing consumers’ inherent preferences for effective recommendations based on consumer digital footprints can be challenging because of the multitude of factors driving consumer behaviors. Model training and recommendation outcomes may become biased if other factors are inappropriately recognized as consumers inherent preferences in the learning process. Drawing on consumer behavior theories, we tease out various factors that drive consumers’ digital footprints at different consumption stages. We develop a novel recommendation approach, namely, DISC (Disentangling consumers’ Inherent preferences, item Salience effect, and Conformity effect), which leverage disentangled representation learning with a causal graph to derive the effect of each factor driving consumer behaviors. This approach provides personalized and interpretable recommendations based on the inference of consumers’ normative inherent preferences. The DISC model’s identifiability is demonstrated through theoretical analysis, enabling rigorous causal inference based on observational data. To evaluate DISC’s performance, extensive experiments are conducted on real-world data sets with a carefully designed protocol. The results reveal that DISC outperforms state-of-the-art baselines significantly and possesses good interpretability. Moreover, we illustrate the potential impact of different marketing strategies’ by intervening on the disentangled causes through follow-up counterfactual analyses based on the causal graph. Our study contributes to the literature and practice by causally unpacking the behavioral mechanism behind consumers’ digital footprints and designing an interpretable personalized recommendation approach anchored in their inherent preferences.

History: Olivia Liu Sheng, Senior Editor; Zhengrui Jiang, Associate Editor.

Funding: This work was supported by the National Natural Science Foundation of China [Grants 72101007, 72293561, 72131001].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2023.0181.

Keywords: recommender system • multiple digital footprints • inherent preferences • causal graph • disentangled representation learning interpretability

## 1. Introduction

Personalized recommendations play a vital role on contemporary e-commerce platforms for decision support and have become an important stream of efforts nowadays in information systems research (Li et al. 2022, Peng and Liang 2023, Zhou et al. 2023). It has been observed that click-through rates and subsequent purchases sharply decline once the personalized recommendation function is disabled (Sun et al. 2024). On e-commerce platforms, various types of consumer digital footprints are recorded, providing abundant fuel for designing personalized recommender systems (RSs). RSs are usually trained using consumers’ observational digital footprints, for example, ratings and clickstream data, among which the former are viewed as explicit feedback and the latter as implicit feedback (Li and Karahanna 2015). As consumers are increasingly reluctant to provide ratings because of the time, effort, and other expenditures required (Sahoo et al. 2012, Hu et al. 2017), modern RSs often need to deal with implicit feedback reflected through clickstream data, for example, clicking on an item, adding it to a cart, etc.

Conventional RSs commonly assume that consumers’ behaviors on e-commerce platforms represent inherent preferences, defined as preferences for products under the assumption that consumers are rational and purely self-interested (Simonson 2008). However, consumers’ implicit feedback cannot solely reflect their inherent preferences because of situational factors. For example, consumers might be readily persuaded to click on a top-ranked or recommended item while distracted, thereby rendering the implicit feedback biased from their inherent preferences. In other words, an observed click or even a purchase can result from a combination of the focal consumer’s inherent preferences and other factors. Thus, in general, the distribution of implicit feedback is different from that of inherent preferences. When such accidental clicks, easily accumulated in large volumes, are treated as inherent preferences in data for RS training, unwanted recommendations will be generated, harming the perceived reliability of the RS and its efficacy accordingly (Adomavicius et al. 2013). Moreover, if various factors behind consumers’ behaviors are not disentangled properly, the recommendations that interweave them together will affect the effectiveness and interpretability, then hampering the practical use of RSs (Wang et al. 2018b). Thus, it is crucial for RSs to probe consumers’ behaviors and reach for inherent preferences accordingly.

Designing a machine learning method to disentangle various causes of consumers’ implicit feedback is a challenging task. First, implicit feedback manifests in various forms from different decision mechanisms, such as impulsive purchases following viewing a prominent product and considered purchases after viewing and careful evaluation. The distinct decision mechanisms necessitate a comprehensive understanding of the interplay among behaviors. However, most extant studies have taken a sole perspective toward purchase behavior to disentangle its causes (Liang et al. 2016b, Saito et al. 2020, Wang et al. 2021b, Zheng et al. 2021), which may incur inaccurate modeling. Second, the causes of behaviors vary but are intertwined, posing extra difficulty in designing a cause-disentanglement mechanism. For example, the importance of consumers’ inherent preferences for a product may vary across different decision contexts, highlighting the need for contextual consideration in cause disentanglement. Third, the absence of predefined labels for each cause complicates the task, requiring pattern recognition from the observed behavioral data and ensuring model identifiability for causal inference. Theoretically analyzing the identifiability of a machine learning method in RSs is particularly challenging because the model typically has a complex form with a large number of parameters.

To cope with these challenges, we propose a causal graph-based disentangled representation learning approach. A causal graph, as a probabilistic graphical model, uses vertices and edges to represent variables and their causal relationships. It effectively encodes the assumptions of the data generation process, which can reflect various behaviors’ contextual information when appropriately constructed. By learning the causal graph’s parameters using causality information recognized from observed data, the effect of each driving factor behind consumers’ behaviors can be uncovered to achieve cause disentanglement.

To develop a valid causal graph that can model the interconnections and causes of multiple types of implicit feedback, we refer to the consumer behavior literature to investigate the situational factors that drive consumers’ various behaviors by scrutinizing consumers’ shopping journeys. Based on a recent survey on consumers’ behavioral biases (Dowling et al. 2020), a typical shopping journey can be categorized broadly into four stages: need recognition, prepurchase, purchase, and postpurchase. The first three stages entail multiple types of implicit feedback, for example, clicking on an item for viewing, adding an item to a cart, and making a purchase, whereas the postpurchase stage usually covers explicit feedback, for example, rat ings and reviews.

The focus of this study is on the implicit feedback present during the initial three stages, where behavioral biases are known to intermingle with consumers’ inherent preferences. At the need recognition stage, consumers are influenced by both internal desires and external stimuli, such as advertising, which can skew their viewing behaviors toward items that are more salient or prominently displayed on e-commerce platforms (Yadav et al. 2013, Lee et al. 2018, Dowling et al. 2020). During the prepurchase stage, consumers search for and add products to their carts for evaluation, but other consumers’ choices may overly impact this process, resulting in insufficient searches (Dewan et al. 2017). Thus, both inherent preference and conformity to social influence drive add-to-cart behaviors. The purchase stage is marked by the most significant implicit feedback, that is, purchase behavior, which is viewed as the most important input for training RSs. The standard purchase stage involves weighing products’ various attributes and making purchase decisions, but such decisions and timing can be biased (Dowling et al. 2020, Iyer et al. 2020). For instance, consumers may impulsively decide to purchase after need recognition, bypassing the prepurchase stage (Beatty and Ferrell 1998). Moreover, internal desire for the product and conformity to others’ purchase decisions can also drive consumers’ purchase decisions simultaneously (Dowling et al. 2020).

With the above analysis, we consider three types of consumer behaviors––view, add-to-cart, and purchase––as representative behaviors during the need recognition, prepurchase, and purchase stages, respectively. These behaviors stem from both internal and external causes. Internal causes refer to consumers’ inherent preferences existing during all stages, whereas external causes vary with each stage, with item salience influencing the need recognition stage and conformity to social influence affecting both the prepurchase and purchase stages. Because of consumers’ potentially impulsive purchase behavior, the three types of digital footprints form a triangle structure, as depicted in Figure 1. In the absence of well-labeled cause-specific data, we extract proxy variables from product attributes and infer the underlying effects of driving factors through disentangled representation learning. We theoretically prove the identifiability of our approach, which provides the foundation for causal inference based on observational data.

To evaluate our approach’s ability to capture consumers’ inherent preferences, we construct and use intervention data as the test bed. We find that our proposed approach outperforms state-of-the-art baseline methods in both in-sample purchase behavior prediction and inherent preference-oriented recommendations. The rationale behind the development of our causal graph is substantiated by fitting consumers’ behavior data into alternative causal graph structures. Furthermore, post hoc analysis illustrates that our approach properly captures consumers’ procedural behaviors and disentangles causes with reasonable semantics to elicit interpretable recommendations.

The rest of this paper is organized as follows: Section 2 reviews related literature, laying the theoretical and practical basis for our study. Section 3 describes the research context and defines the causal recommendation problem. Section 4 details our proposed causal graph model and the disentangled representation learning method for inferential analysis. Section 5 evaluates the proposed approach’s performance through abundant experiments. Section 6 discusses alternative causal graph models and potential managerial implications. Section 7 concludes the paper and suggests directions for future research.

Figure 1. (Color online) Consumers’ Digital Footprints and Causes of Each Behavior  
![](/api/attachments/HRRXA4H7/fulltext/images/9a890656ee3e534d6887fec8a646f140eaf44159049747d9f19ae3537db54e83.jpg)

## 2. Related Literature

## 2.1. Behavioral Biases in Consumers’ Online Shopping Journey

The data biases in implicit feedback result from consumers’ behavioral biases. A recent review attributed consumers’ behavioral biases to nonstandard preferences, beliefs, and decision making (Dowling et al. 2020). The three types of behavioral biases are rooted in behavioral economic models (Dhami 2016). Nonstandard preference refers to deviation from the standard utility function, for example, consumers’ utility function may not be purely self-interested, but affected by bandwagon effects tied to external factors. Nonstandard beliefs emerge when consumers deviate from standard Bayesian belief updating in uncertain decision making contexts (DellaVigna 2009). Nonstandard decision making refers to deviations from the utility maximization process due to cognitive limitations or persuasion and social influence (Simon 1955).

The three types of behavioral biases manifest at various stages of a consumer’s shopping journey, leading to a discrepancy between observed consumer behavior data and inherent preferences. During the need recognition stage, consumers recognize needs based on internal desire or external signals (such as ads) toward nonstandard preferences and beliefs (Yadav et al. 2013, Lee et al. 2018). In the prepurchase stage, consumers search for and evaluate alternatives by making forecasts about future events and behaviors, in which belief-based biases are prominent because of forecast uncertainty (Dowling et al. 2020). During the purchase stage, consumers make decisions regarding whether to make purchases, in which nonstandard decision making can result from others’ persuasion, as well as conformity to relevant groups’ preferences (Akerlof 1991). Furthermore, consumers’ decision-making process can also be nonstandard (Dowling et al. 2020); for example, in scenarios such as impulsive purchases, consumers proceed directly from the need recognition to purchase (Iyer et al. 2020). Thus, to generate personalized recommendations and marketing strategies that truly cater to consumers’ inherent preferences, it is crucial to disentangle and account for various causes of biases in consumers’ behavior data.

## 2.2. Causal Learning

The combination of causal inference and machine learning is a burgeoning research area. Although machine learning models excel in predictive tasks with independently and identically distributed (IID) data, they may fall short in generalizability to prediction with distribution shift (Scho¨ lkopf et al. 2021). Causal machine learning methods, which combine the strengths of causal inference and machine learning, can effectively handle the prediction of IID settings, under distribution shifts, and answer counterfactual questions involving what-ifs (Bengio et al. 2019, Xia et al. 2021). Generally, the tasks of causal learning can be classified into causal structure discovery and causal effect estimation (Guo et al. 2020).

Causal structure discovery refers to learning causa relationships between variables (Guo et al. 2020, Valogianni et al. 2023). To this end, extant efforts have developed abundant data-driven methods that can find causal links between observed variables and detect latent variables that serve as confounders, including constraint-based methods (Huang et al. 2020), scorebased methods (Lam et al. 2022), and causal representation learning (Xie et al. 2020). Evaluation of causal structure discovery typically requires a ground-truth causal graph, from which the graph distance metrics and classification metrics can be calculated for performance measurement (Cheng et al. 2022). Although potential causal knowledge can be extracted, the datadriven methods may generate spurious causal relationships or fail to detect causal links due to observational equivalence, which needs to be rectified by experimental studies (Bengio et al. 2019, Xia et al. 2021). Therefore, extant research also widely employs theory-driven methods that derive causal structure from domain knowledge (Pearl 2009, Zheng et al. 2019).

Causal effect estimation aims to estimate the causal effects based on observational data, in which the causal structure is provided but issues like confounders need to be dealt with (Guo et al. 2020, Wang and Rudin 2022). Considering that the traditional methods may fall short of learning capability, recent literature has proposed incorporating advanced machine learning methods like disentangled representation learning and neural networks into causal effect estimation (Scho¨lkopf et al. 2021, Xia et al. 2021). The evaluation for this task involves standard causal effect, heterogeneous effect, and time series effect estimations (Cheng et al. 2022), for which errorbased metrics and uplift-based metrics are usually adopted. Importantly, error-based metrics like Precision in Estimation of Heterogeneous Effect in causal effect estimation are equivalent to the metrics for recommendation evaluation (e.g., precision) when the error form is properly designed (Chen et al. 2023).

In our study, considering the abundance of consumer behavior theories in online shopping (Dowling et al. 2020), we adopt the theory-driven method to establish the causal structure of consumer behaviors and their driving factors. Our primary focus resides in estimating causal effects to ascertain the impact of each cause behind consumers’ multiple types of behaviors, thereby facilitating informed recommendations.

## 2.3. Debiasing Recommendation Methods

Because of data biases in consumers’ implicit feedback, RSs that fail to consider the causes of the biases may yield outcomes that are not in line with consumers’ inherent preferences, resulting in unsatisfactory performances. Related studies on RS design have viewed the problem as a debiasing problem and proposed three perspectives to solve it, including the inverse propensity score (IPS) approach, exposure-based model, and causal embedding approach. Our approach belongs to the causal embedding family.

The IPS approach addresses consumers’ inherent preferences by optimizing an unbiased objective function, or IPS estimator. The estimator is constructed by weighting each user–item interaction prediction error with the inverse observation propensity of the corresponding interaction outcome. Propensity can be estimated through various methods, including relative item salience (Saito et al. 2020), logistic regression (Schnabel et al. 2016), and low nuclear norm constraint (Ma and Chen 2019). However, current IPS approach efforts only consider item salience in propensity estimation, leading to inaccurate propensity estimation due to the disregard of other causes. This propensity inaccuracy subsequently results in poor debiasing performance.

The exposure-based model posits a latent exposure state prior to a consumer’s interaction with a product. By incorporating the bias-formation mechanism in exposure modeling, this model achieves debiasing by maximizing joint likelihood (Liang et al. 2016b). However, the model’s failure to fully analyze a consumer’s behaviors throughout their shopping journey leads to misspecification and poor debiasing performance.

The causal embedding approach aims to capture each cause that motivates user–item interactions with respective embedding, thereby extracting consumers inherent preferences for debiasing while maintaining interpretability. Recent research efforts have combined causal graph modeling with disentangled representation learning to disentangle inherent preferences from other factors for debiased recommendations (Wang et al. 2021b, Zhang et al. 2021, Zheng et al. 2021). However, most existing efforts within this approach focus solely on purchase behavior and oversimplify driving factors, leading to inaccurate inherent preference estimations. Furthermore, because of a lack of theoretical analysis, the model identifiability remains unclear in the approach, leaving the causal inference ungrounded.

In this study, we propose a new approach within the causal embedding family. This approach employs causal graph modeling and disentangled representation learning to incorporate multiple types of implicit feedback and comprehensively disentangle their causes. We also bridge the gap by theoretically proving the model identifiability of our proposed approach.

## 2.4. Recommendations with Multiple Types of Implicit Feedback

With the pervasiveness of consumers’ multiple types of digital footprints, a research stream on RS design with multiple types of implicit feedback has emerged in recent years (Chen et al. 2020b). In RSs based on multiple types of implicit feedback, a target behavior (e.g., purchasing) is concerned and needs to be predicted, whereas other behaviors provide auxiliary information to help learn consumer preferences. Despite the sequential dependence that typically exists among different consumer behaviors, recommendations with multiple types of implicit feedback differ from session-based recommendations (Wang et al. 2021a), as they also involve learning consumers’ long-term and static preferences (Chen et al. 2020b). Some studies manage multiple types of implicit feedback by constructing preference orders implied in behaviors; for example, a purchase is assumed to be a stronger preference than a view, whereas no feedback is treated as the weakest preference (Ding et al. 2018). However, such assumptions are usually heuristics that lack a solid theoretical foundation because different factors influence consumers’ multiple behaviors with complex mechanisms. Recent research has developed models with a deep structure to enhance the understanding of correlations among multiple behaviors (Gao et al. 2019, Chen et al. 2020a). Despite achieving satisfactory in-sample prediction performance, extant methods examining multiple types of implicit feedback often overlook consumers’ behavioral biases and fail to adequately model the flexible transition process of consumers’ shopping stages.

## 3. Problem Definition

In this study, we focus on the three most prominent types of implicit feedback, namely, view, add-to-cart, and purchase, denoted by $v , a ,$ and z, as the representative behaviors in the stages of need recognition, prepurchase evaluation, and purchase, respectively. Among the three types, purchase is regarded as the focal implicit feedback that needs to be predicted, whereas the other two types provide auxiliary information for prediction. In light of the theoretical foundation elaborated in Section 2.1, consumers’ behaviors in the need recognition stage are primarily driven by inherent preferences and item salience, denoted by r and b, respectively, whereas the behaviors in the prepurchase evaluation and purchase stages are mainly driven by inherent preferences and conformity, denoted by r and c, respectively. Furthermore, consumers’ decision process can be flexible, ranging from cautious to impulsive. For illustrative purposes, the following examples (Examples 1 and 2) represent two different cases, where the user $u s e r _ { 1 } = \mathrm { T a y l o r } _ { . }$ , the item set {item<sub>1</sub>, item<sub>2</sub>, item<sub>3</sub>} � {pink dress, green dress, black dress}, and the advertising intensity and sales volume serve as signals for item salience effect b and conformity effect c, respectively.

Example 1. Taylor wants to update her wardrobe with a new dress. She has an inherent preference for green and starts to search online but is initially attracted to a pink one in the advertisement because of its salience. It is plausible that she decides to look more before purchase, as shown in Figure 2. She finds three options of the same style but different colors: pink, green, and black, with respective sales volumes of 128, 128, and 1024, which may reflect conformity. She adds the three dresses to the cart for prepurchase evaluation, believing that the high sales volume of the black dress communicates that it is a popular and safe choice. This could provide a form of social proof, indicating that many other consumers prefer the black dress. Despite her own preference for the green dress, she may feel more confident in conforming to the choice that has been validated by other consumers. Hence, she purchases the black one.

Example 2. Taylor needs a new dress for an upcoming event and is in a hurry to purchase one online. Still, she holds an inherent preference for green but is in such a hurry that she purchases the pink one immediately after seeing it in the advertisement, skipping the prepurchase evaluation, as shown in Figure 3.

Next, we formally define the causal recommendation problem. Drawing upon related theories on consumers’ decision making and behavioral biases in the online shopping journey, we construct a causal graph with a collection of mechanisms $\mathcal { F } ( v , a , z , r , b , c , \pmb { \Omega } ) _ { . }$ , in which <sup>V</sup> is the parameter set. Let $u \in \mathcal { U } = \left\{ 1 , 2 , \dotsc , U \right\}$ index a user and $i \in \mathcal { I } = \{ 1 , 2 , \dots , I \}$ index an item. In model training, we use the historical data set $D _ { t r a i n } =$ $\{ v _ { u i } , a _ { u i } , z _ { u i } | u \in \mathcal { U } , i \in \mathcal { I } \}$ that records consumers’ three types of behaviors, along with product attributes to learn the effects of causes $\{ r _ { u i } , b _ { u i } , c _ { u i } | u \in \mathcal { U } , i \in \mathcal { T } \}$ and the parameter set <sup>V</sup>. The evaluation of cause disentanglement and the prediction of the learned causal recommendation model mainly focus on the inherent preference-oriented recommendation task, which is defined in Definition 1.

Figure 2. (Color online) An Illustrative Example of a Cautious Purchase  
![](/api/attachments/HRRXA4H7/fulltext/images/869963816e78d5c64387816313e664661ae2fa1f0c774c509bca27b692deebcc.jpg)

Figure 3. (Color online) An Illustrative Example of an Impulsive Purchase  
![](/api/attachments/HRRXA4H7/fulltext/images/742fe9495695e7b9bf5f9eccae2e3cea56e8767fbf21b930ee77a299dae1a74d.jpg)

Definition 1 (Inherent Preference-Oriented Recommendation). An inherent preference-oriented recommendation is a recommendation that is purely driven by the inherent preference $r _ { u i } ,$ which excludes item salience and conformity effects, that is, $b _ { u i } = 0$ and $c _ { u } = 0$

Hence, an inherent preference-oriented recommendation is generated based on the counterfactual purchase probability $P _ { \hat { \mathcal { F } } } ( z _ { u i } = 1 | \mathrm { d o } ( b _ { u i } = 0 , c _ { u i } = 0 ) )$ , in which $\hat { \mathcal { F } }$ stands for the causal mechanism learned from $D _ { t r a i n }$ and do $( b _ { u i } = 0 , c _ { u i } = 0 )$ represents intervention operation on the causal graph. Note that from Definition 1, the inherent preference-oriented recommendation should be the green dress in Taylor’s examples. It is worth mentioning that because observational data of purchase behaviors entangle multiple causes, these behavioral data cannot be directly used for evaluating the performance of inherent preference-oriented recommendations in an effective fashion. Aspired by conventional methods used in existing research (Liang et al. 2016a, Bonner and Vasile 2018, Zheng et al. 2021), intervention purchase data are constructed and employed as the test set $D _ { t e s t } .$ . For each user, the products that have not been purchased are ranked in descending order based on the model’s predictions to form a top-n list. The performance is then assessed using both error-based and ranking-based metrics with the ground truth in $D _ { t e s t }$

## 4. Model

## 4.1. Model Description

For a better illustration of our proposed model, some important notations are outlined in Table 1. We start by analyzing multiple types of consumer behaviors to model their interconnections and driving factors. The triangle structure of view, add-to-cart, and purchase creates a serious challenge to the causal graph’s development, that is, ternary decision modeling. Concretely, after viewing a product, a consumer can add the product to his or her cart, purchase it directly, or do nothing.

Table 1. Basic Notations

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $r_{ui}$ </td><td>u&#x27;s inherent preference for i</td></tr><tr><td> $b_{ui}$ </td><td>Item salience effect in u&#x27;s interaction with i</td></tr><tr><td> $c_{ui}$ </td><td>Conformity effect in u&#x27;s interaction with i</td></tr><tr><td> $v_{ui}$ </td><td>Indicator of whether u views i,  $v_{ui} \in \{0,1\}$ </td></tr><tr><td> $a_{ui}$ </td><td>Indicator of whether u adds i to cart, $a_{ui} \in \{0,1\}$ </td></tr><tr><td> $z_{ui}$ </td><td>Indicator of whether u purchases i,  $z_{ui} \in \{0,1\}$ </td></tr><tr><td> $s_{ui}$ </td><td>u&#x27;s decision path after viewing i,  $s_{ui} \in \{0,1\}$ </td></tr><tr><td> $\theta_{ui}$ </td><td>Parameter that controls the distribution of  $s_{ui}$ </td></tr><tr><td> $\mathbf{p}_{u}^{r}, \mathbf{p}_{u}^{b}, \mathbf{p}_{u}^{c}, \mathbf{p}_{u}^{s} \in \mathbb{R}^{K}$ </td><td>Embeddings of u related to inherent preference, item salience effect, conformity effect, and decision path choice probability, respectively; $\mathbf{p}_{u}^{r}, \mathbf{p}_{u}^{b}, \mathbf{p}_{u}^{c}, \mathbf{p}_{u}^{s}$ </td></tr><tr><td> $\mathbf{q}_{i}^{r}, \mathbf{q}_{i}^{b}, \mathbf{q}_{i}^{c}, \mathbf{q}_{i}^{s} \in \mathbb{R}^{K}$ </td><td>Embeddings of i related to inherent preference, item salience effect, conformity effect, and decision path choice probability, respectively; $\mathbf{q}_{i}^{r}, \mathbf{q}_{i}^{b}, \mathbf{q}_{i}^{c}, \mathbf{q}_{i}^{s}$ </td></tr><tr><td> $\alpha_{t}, \beta_{t} (t \in \{1,2,3,4\})$ </td><td>Weights of causes in consumers&#x27; decisions</td></tr></table>

The complexity of this decision-making process, which encompasses both cautious and impulsive decision contexts, complicates the representation using the triangle structure. To address this, we incorporate a binary variable, $s _ { u i } ,$ to indicate the choice of decision path, thereby reflecting the decision context. Therefore, the ternary decision is transformed into a mixture of two binary decisions distributed on cautious and impulsive shop ping journeys. Thus, the proposed causal graph can cover different contexts in consumers’ shopping process.

We then formulate the causes as per consumer behavior theories and establish the causal graph of our approach, DISC (Disentangling consumers’ Inherent preferences, item Salience effect, and Conformity effect), the structure of which is illustrated in Figure 4.

Next, we introduce the causal embedding learning task to learn each cause’s disentangled representation. In the absence of well-labeled cause-specific data, we extract proxy variables from product attributes. Utilizing common effect properties derived from pairwise comparisons, we infer the underlying effects of the driving factors. Given that the pairwise comparisons are decision dependent, the decision path choice variable $s _ { u i }$ can help discern different decision paths. This strategy enables the inference of our proposed causal graph through disentangled representation learning. We theoretically prove the identifiability (the definition of which is provided in Online Appendix A) of our model, providing the foundation for causal inference based on observational data. We approach parameter learning as a multiobjective optimization problem, formulating a loss function that includes the likelihood of behavior modeling and losses for cause disentanglement. The expectation maximization (EM) algorithm is then used to estimate the parameters based on observed data.

Figure 4. Causal Graph of Consumers’ Digital Footprints  
![](/api/attachments/HRRXA4H7/fulltext/images/9a52c37470bebc73af5a2932099d0faefb051857d2de134d48487bce422f5c50.jpg)

In the following subsections, we detail the components, theoretical property, inference, and recommendation process of DISC, providing a thorough understanding of our approach’s framework and its application in causal recommendations.

## 4.1.1. Multiple Types of Consumer Behaviors

4.1.1.1. View. Consumers start shopping with need recognition, in which consumers recognize needs reflected by viewing products because of internal or external signals (Yadav et al. 2013, Lee et al. 2018). Internal signals refer to consumers’ inherent preferences, as explained by selective exposure theory, which indicates that consumers are selectively exposed to items in which they are interested (Jonas et al. 2001). However, persuasive cues (e.g., ads and recommendations) function as external signals, giving rise to item salience effects (Hui et al. 2013, Dowling et al. 2020), that is, that some products that consumers are exposed to more frequently than their values would warrant through advertising and recommendations and are more likely to be noticed during the need recognition stage (Fleder and Hosanagar 2009, Ciampaglia et al. 2018, Nikolov et al. 2019). Therefore, the intention of user u viewing item i $( \mathrm { i . e . , } \overline { { v } } _ { u i } )$ depends on both inherent preference, $r _ { u i } ,$ and the item salience effect, $b _ { u i } ,$ which can be formulated as $\overline { { v } } _ { u i } = \alpha _ { 1 } r _ { u i } + \beta _ { 1 } b _ { u i } ,$ , in which $\alpha _ { 1 } > 0$ and $\beta _ { 1 } > 0$ are the weights of causes in influencing view behaviors. Referring to the random utility framework (Wooldridge 2015), we employ the logit model to formulate the view probability, which is also a common choice in RS research (Johnson 2014), that is,

$$
P (v _ {u i} = 1 | r _ {u i}, b _ {u i}, \pmb {\alpha}, \pmb {\beta}) = \Lambda (\overline {{v}} _ {u i}) \equiv \Lambda_ {u i} ^ {v},\tag{1}
$$

where $\begin{array} { r } { \Lambda ( x ) = \frac { \exp ( x ) } { 1 + \exp ( x ) } , } \end{array}$ denoting the cumulative distribution function of logistic distribution, and ≡ represents “denoted as.”

4.1.1.2. Choice of Decision Paths. Consumers’ shopping journeys can be flexible because a consumer can either go through need recognition, prepurchase, and purchase stages sequentially, or impulsively jump to the purchase stage from need recognition without any prepurchase activities (Iyer et al. 2020). That is, after user u views item i, u may (1) purchase it directly, (2) add it to the cart for further consideration, or (3) do nothing, forming a behavior branch in the triangle structured digital footprints, as depicted in Figure 1. The behavior branch implies a ternary decision in which decision mechanisms are mixed. Specifically, on one hand, adding i to the cart and purchasing i directly indicate a more significant overall effect of various causes than doing nothing regarding the add-to-cart decision and impulsive purchase decision, respectively. On the other hand, the mechanisms for making choices to add i to the cart and purchase i directly may be inconsistent across different decision contexts (i.e., cautious and impulsive decision contexts) because the weights of these two choices’ causes can be different. To capture consumers’ decision mechanisms behind the ternary decision, we develop an indicator of the decision path after u views i for modeling the shopping stage transition process, that is,

$$
s _ {u i} = \left\{ \begin{array}{l} 0, u \text {   decides   whether   to   add   } i \text {   to   cart }, \\ 1, u \text {   decides   whether   to   purchase   } i \text {   directly }, \end{array} \right.\tag{2}
$$

in which $s _ { u i } = 1$ implies that u takes an impulsive decision path that bypasses the prepurchase stage, whereas $s _ { u i } = 0$ suggests a more cautious decision path. This choice depends on u’s shopping habits, as well as the characteristics of $i ;$ for example, $s _ { u i } = 1$ may hold with a high probability if u is an impulsive decision maker or i is in a less-differentiated market. Therefore, we assume a Bernoulli distribution of $s _ { u i }$ as

$$
P (s _ {u i} = 1 | \theta_ {u i}) = \theta_ {u i} \equiv \Lambda (\mathbf {p} _ {u} ^ {s T} \mathbf {q} _ {i} ^ {s}),\tag{3}
$$

that $\mathrm { i s , } \ s _ { u i } \sim \mathrm { B e r n o u l l i } ( \theta _ { u i } )$ with $\theta _ { u i }$ factorized as $\Lambda ( \mathbf { p } _ { u } ^ { s T } \mathbf { q } _ { i } ^ { s } )$ , in which $\boldsymbol { \mathsf { p } } _ { u } ^ { s }$ and q<sup>s</sup> are the embeddings of u and i that are related to the decision path choice. With the latent variable $s _ { u i }$ indicating the decision context, we transform the ternary decision into a mixture of two binary decisions distributed on the cautious and impulsive shopping journeys. Thus, consumers’ decision mechanisms can be modeled properly as follows.

4.1.1.3. Add-to-Cart. If user u takes a cautious decision path after viewing item $i ,$ u steps into the prepurchase stage, during which consumers search for information to evaluate products and add items with favorable evaluations to their carts for further consideration (Yadav et al. 2013, Lee et al. 2018). The standard economic model assumes that product evaluations should be made based on inherent preferences (Dowl ing et al. 2020). However, because of search efforts, consumers may not search enough and overly react to others’ choices, thereby indicating a conformity effect (Muchnik et al. 2013, Dewan et al. 2017, Baeza-Yates 2018, Karaman 2021); that is, a consumer tends to overestimate a product if they know that it has been a hot choice by others. To consider both consumers’ inherent preference $r _ { u i }$ and conformity effect $c _ { u i } ,$ we assume the probability of u adding i to the cart as follows:

$$
\begin{array}{r l} & P (a _ {u i} = 1 | v _ {u i} = 1, s _ {u i} = 0, r _ {u i}, c _ {u i}, \boldsymbol {\alpha}, \boldsymbol {\beta}) \\ & \quad = \Lambda (\alpha_ {2} r _ {u i} + \beta_ {2} c _ {u i}) \equiv \Lambda_ {u i} ^ {a}. \end{array}\tag{4}
$$

If u has not viewed $i ,$ or u has taken the impulsive decision path (i.e., u bypasses the prepurchase stage), then the probability of u adding i to the cart will be zero, that is,

$$
\begin{array}{r} P (a _ {u i} = 1 | v _ {u i} = 0, s _ {u i}, r _ {u i}, c _ {u i}, \pmb {\alpha}, \pmb {\beta}) = 0, \\ P (a _ {u i} = 1 | v _ {u i} = 1, s _ {u i} = 1, r _ {u i}, c _ {u i}, \pmb {\alpha}, \pmb {\beta}) = 0. \end{array}\tag{5}
$$

4.1.1.4. Purchase. During the purchase stage, consumers decide whether to make a purchase (Yadav et al. 2013, Lee et al. 2018). The standard economic model based on utility theory assumes that consumers’ purchases are purely self-interested (Dowling et al. 2020) because its backbone theory implies that consumers make decisions that seek to maximize utility (Fishburn 1970). Nevertheless, based on social influence theory, the conformity effect still exists to impact purchase decisions (Muchnik et al. 2013, Dewan et al. 2017, Baeza-Yates 2018, Karaman 2021). For example, consumers tend to follow others in purchase decision making while neglecting their own judgments amid social pressure. Thus, we model purchase probability in different cases as follows.

If user u has viewed item i and taken the impulsive decision path to decide whether to purchase i directly $( \mathrm { i . e . , } v _ { u i } = 1 , s _ { u i } = 1 )$ , then

$$
\begin{array}{r l} & P (z _ {u i} = 1 | v _ {u i} = 1, s _ {u i} = 1, a _ {u i}, r _ {u i}, c _ {u i}, \pmb {\alpha}, \pmb {\beta}) \\ & \quad = \Lambda (\alpha_ {3} r _ {u i} + \beta_ {3} c _ {u i}) \equiv \Lambda_ {u i} ^ {v z}. \end{array}\tag{6}
$$

If u has viewed i and has taken the cautious decision path to decide whether to add i to the cart, then purchase probability depends on the add-to-cart decision. Specifically, if u has added i to the cart $( \mathrm { i . e . , } v _ { u i } = 1 , s _ { u i } =$ $0 , a _ { u i } = 1 )$ , then the purchase probability is

$$
\begin{array}{r l} & P (z _ {u i} = 1 | v _ {u i} = 1, s _ {u i} = 0, a _ {u i} = 1, r _ {u i}, c _ {u i}, \pmb {\alpha}, \pmb {\beta}) \\ & \quad = \Lambda (\alpha_ {4} r _ {u i} + \beta_ {4} c _ {u i}) \equiv \Lambda_ {u i} ^ {a z}. \end{array}\tag{7}
$$

If u has decided not to add i to the cart $( \mathrm { i } . \mathrm { e } . , v _ { u i } = 1 .$ $s _ { u i } = 0 , a _ { u i } = 0 )$ , then the purchase will not come from the cautious decision path, that is,

$$
P (z _ {u i} = 1 | v _ {u i} = 1, s _ {u i} = 0, a _ {u i} = 0, r _ {u i}, c _ {u i}, \pmb {\alpha}, \pmb {\beta}) = 0.\tag{8}
$$

Finally, because viewing is the premise for purchase, the following probability holds:

$$
P (z _ {u i} = 1 | v _ {u i} = 0, s _ {u i}, a _ {u i}, r _ {u i}, c _ {u i}, \pmb {\alpha}, \pmb {\beta}) = 0.\tag{9}
$$

Note that the weights for causes $( \mathrm { i . e . , } \alpha _ { t } , \beta _ { t } ( t \in 1 , 2 , 3 , 4 ) )$ are differentiated to capture different decision mechanisms during the shopping journey. Therefore, the heterogeneous roles of a cause in influencing various behaviors can be reflected. Because $r _ { u i } , b _ { u i } , c _ { u i } , \mathbf { \alpha \alpha } .$ , and <sup>b</sup> are all undetermined, we set $\beta _ { 1 } = \alpha _ { 4 } = \beta _ { 4 } = 1$ to reduce the degrees of freedom.

4.1.1.5. Likelihood. As illustrated in Figure 4, for each user–item pair $( u , i ) , ~ v _ { u i } , ~ a _ { u i } ,$ , and $z _ { u i }$ are observable, whereas $s _ { u i }$ is not. The marginal likelihood of behaviors within $( u , i )$ can be formulated as

$$
\begin{array}{l} P (v _ {u i}, a _ {u i}, z _ {u i} | r _ {u i}, b _ {u i}, c _ {u i}, \theta_ {u i}, \boldsymbol {\alpha}, \boldsymbol {\beta}) \\ = \sum_ {s \in \{0, 1 \}} P (s _ {u i} = s | \theta_ {u i}) P (z _ {u i} | v _ {u i}, s _ {u i} = s, a _ {u i}, r _ {u i}, c _ {u i}, \boldsymbol {\alpha}, \boldsymbol {\beta}) \\ \times P (a _ {u i} | v _ {u i}, s _ {u i} = s, r _ {u i}, c _ {u i}, \boldsymbol {\alpha}, \boldsymbol {\beta}) P (v _ {u i} | r _ {u i}, b _ {u i}, \boldsymbol {\alpha}, \boldsymbol {\beta}). \end{array}\tag{10}
$$

By taking advantage of the behavior sequence, we need to consider only four cases to derive the full likelihood (see Equations (11)–(14)): the probability of u not viewing i (Equation (11)); the probability of u viewing i withou adding i to the cart or purchasing i (Equation (12)); the probability of u purchasing i directly after view (Equation (13)); and the probability of u adding i to the cart with either purchasing or not purchasing i (Equation (14)).

$$
P (v _ {u i} = 0) = 1 - \Lambda_ {u i} ^ {v},\tag{11}
$$

$$
P (v _ {u i} = 1, a _ {u i} = 0, z _ {u i} = 0) = \Lambda_ {u i} ^ {v} (\theta_ {u i} (1 - \Lambda_ {u i} ^ {v z})
$$

$$
+ (1 - \theta_ {u i}) (1 - \Lambda_ {u i} ^ {a})),\tag{12}
$$

$$
P (v _ {u i} = 1, a _ {u i} = 0, z _ {u i} = 1) = \Lambda_ {u i} ^ {v} \theta_ {u i} \Lambda_ {u i} ^ {v z},\tag{13}
$$

$$
P (v _ {u i} = 1, a _ {u i} = 1, z _ {u i}) = \Lambda_ {u i} ^ {v} (1 - \theta_ {u i}) \Lambda_ {u i} ^ {a} (\Lambda_ {u i} ^ {a z}) ^ {z _ {u i}} (1 - \Lambda_ {u i} ^ {a z}) ^ {1 - z _ {u i}}.\tag{14}
$$

We utilize the negative log-likelihood as the loss function of behavior modeling, that is,

$$
\begin{array}{l} \mathcal {L} _ {\text {behavior}} = - \sum_ {u = 1} ^ {U} \sum_ {i = 1} ^ {I} \\ \left( \begin{array}{l} \mathbb {I} (v _ {u i} = 0) \mathrm{log} P (v _ {u i} = 0) \\ + \mathbb {I} (v _ {u i} = 1, a _ {u i} = 0, z _ {u i} = 0) \mathrm{log} P (v _ {u i} = 1, a _ {u i} = 0, z _ {u i} = 0) \\ + \mathbb {I} (v _ {u i} = 1, a _ {u i} = 0, z _ {u i} = 1) \mathrm{log} P (v _ {u i} = 1, a _ {u i} = 0, z _ {u i} = 1) \\ + \mathbb {I} (v _ {u i} = 1, a _ {u i} = 1) \mathrm{log} P (v _ {u i} = 1, a _ {u i} = 1, z _ {u i}) \end{array} \right), \end{array}\tag{15}
$$

in which I(·) is the indicator function.

4.1.2. Causes. We formulate the causes of consumer behaviors––including inherent preferences, item salience effects, and conformity effects––with the embedding technique, which posits that consumer preferences can be characterized by latent factors. Specifically, users and items are respectively represented with K-dimensional embeddings (i.e., vectors), and users’ preferences for items are approximated by inner product operations (Koren et al. 2009). Based on the latent factor manner (Koren et al. 2009), user u’s inherent preference for item i can be factorized as

$$
r _ {u i} = \mathbf {p} _ {u} ^ {r} T \mathbf {q} _ {i} ^ {r} = \sum_ {l = 1} ^ {K} p _ {u l} ^ {r} q _ {i l} ^ {r},\tag{16}
$$

in which $\boldsymbol { \mathsf { p } } _ { u } ^ { r }$ and $\mathbf { q } _ { i } ^ { r }$ are the inherent preference-related embeddings of u and $i ,$ respectively. Accordingly, the lth element of $\mathbf { q } _ { i } ^ { r } \left( \mathrm { i . e . , } q _ { i l } ^ { r } \right)$ quantifies the extent to which i possesses the lth latent factor, and the lth element of $\boldsymbol { \mathsf { p } } _ { u } ^ { r }$ $( \mathrm { i . e . , ~ } p _ { u l } ^ { r } )$ can be viewed as the importance of the lth latent factor to u. An illustrative example of the embedding technique is provided in Online Appendix $\mathrm { B , }$ Section B.1.

Extant studies usually assume that item salience and conformity effects only depend on the item and treated them statically as item-specific terms (Saito et al. 2020, Zhang et al. 2021). However, these effects may also vary across different users because of consumers’ heterogeneity in taking in such causes. For example, after watching ads, some consumers are more prone to view the products, whereas others may just ignore them, resulting in different item salience effects. Moreover, some consumers are more likely to follow others in decision making, giving rise to a more significant conformity effect. Therefore, we model the item salience and conformity effects in a way that is similar to that of inherent preference, that is,

$$
b _ {u i} = \mathbf {p} _ {u} ^ {b} T \mathbf {q} _ {i} ^ {b}, c _ {u i} = \mathbf {p} _ {u} ^ {c} T \mathbf {q} _ {i} ^ {c},\tag{17}
$$

in which $\boldsymbol { \mathsf { p } } _ { u } ^ { b }$ and $\mathbf { q } _ { i } ^ { b }$ are the salience effect–related embeddings of u and $i ,$ and $\boldsymbol { \mathsf { p } } _ { u } ^ { c }$ and $\mathbf { q } _ { i } ^ { c }$ are the conformity effect–related embeddings of u and i.

As behaviors only reflect the overall effects where causes are entangled, causes are only conceptual in this step and do not capture practical patterns (see Lemma A1 in Online Appendix A). Next, we introduce the causal embedding learning task to ensure that $r _ { u i } , b _ { u i } ,$ and $c _ { u i }$ can capture practical meanings.

4.1.3. Causal Embedding Learning. Given the absence of well-labeled cause-specific data, methods of pattern recognition from noisy behavioral data need to be designed; that is, we need to extract information that can reflect the extent to which a cause drives a behavior. In this study, we employ the proxy variable approach for common effect properties derivation to extrapolate the relative relations among causes’ effects.

4.1.3.1. Proxy Variables. Proxy variables, indicators of relative causes’ effects (Miao et al. 2018), are widely used in various contexts for causal inference. For instance, investment can be adopted as a proxy variable for productivity in economics (Olley and Pakes 1996), whereas per-capita gross domestic product is used to proxy life quality (Montgomery et al. 2000). In the context of consumers’ online shopping journey, the number of views and products sales volume are usually employed as the proxy variables for item salience and conformity effects, respectively (Dewan et al. 2017, Nikolov et al. 2019). As illustrated in Example 2 in Section $^ { 3 , }$ salient products are more likely to be exposed to consumers and, therefore, receive a larger number of views. Hence, product views can be regarded as the proxy variable for the item salience effect. Conformity effect, on the other hand, stems from information on other consumers’ choices (Muchnik et al. 2013, Dewan et al. 2017, Baeza-Yates 2018, Karaman 2021). As shown in Example 1 in Section 3, Taylor chooses the black dress over the other two alternatives, as its high sales volume communicates as a safer choice chosen by more consumers. In other words, there likely exists a higher conformity effect in Taylor’s interaction with the black dress compared with the other two. Thus, products sales volume can serve as an indicator of others’ pur chase behavior and reflect the relative relation between the conformity effects in a consumer’s interaction with various items. In this study, we follow extant works to use item views and sales volumes as the proxy variables for the item salience effect and conformity effect, respec tively. It is important to note that although the proxy variable is item specific and provides only item-side information, the causal effect can be inferred with the help of behavior modeling, which supplements userside information. In other words, even though the item side information may be the same for different users, they can provide varying feedback, indicating that the cause’s magnitude varies across consumers and pro vides information from the perspective of users in model inference. Thus, constructing item-specific proxy variables is sufficient for cause disentanglement (see Online Appendix A for theoretical analysis). Because a consumer’s inherent preference is mixed with the item salience effect (in view) and conformity effect (in add-to-cart and purchase), we disentangle $r _ { u i }$ from $b _ { u i }$ and $c _ { u i }$

4.1.3.2. Disentangling Inherent Preference and Item Salience Effect. Denoting $\pmb { \pi } = \left( \pi _ { 1 } , \pi _ { 2 } , \ldots , \pi _ { I } \right) ^ { T }$ as the proxy variable for the item salience effect, that is, if $\pi _ { i } > \pi _ { j } ,$ , we expect $b _ { u i } > b _ { u j }$ for $u \in \mathcal { U } .$ . With the proxy variable, we can derive common effect properties from pairwise comparisons to infer causality information.

4.1.3.3. Common Effect Properties from Pairwise Comparisons. In the causal graph (Figure 4), view depends on the inherent preference and item salience, creating a common effect structure (i.e., collider; Pearl 2009). This structure implies that $r _ { u i }$ and $b _ { u i }$ are dependent if $v _ { u i }$ is observed, providing necessary information for causality inference. Following the framework of common effect analysis (Zheng et al. 2021), three cases are discussed to derive causality information to disentangle inherent preference and item salience effect. As the indexes of items $( \mathrm { i } . \mathrm { e } . , i \mathrm { a n d } j )$ are permutable, discussions of the cases in which $v _ { u i } = 0 , v _ { u j } = 1$ are also included in Cases 1 and 2. Thus, Cases 1–3 are mutually exclusive and can encompass all circumstances when combined, guaranteeing the completeness of the analysis.

Case 1 $( v _ { u i } = 1 , v _ { u j } = 0 , \pi _ { i } \leq \pi _ { j } )$ . Because user u views i rather than $j ,$ which has a greater (or equal) salience effect, it is probable that $u ^ { \prime } \mathrm { s }$ inherent preference for i outweighs that in j based on the common effect structure. Therefore, it can be derived that $b _ { u i } \le b _ { u j }$ and $r _ { u i } > r _ { u j }$

Case 2 $( v _ { u i } = 1 , v _ { u j } = 0 , \pi _ { i } > \pi _ { j } )$ . As u views an item with a greater item salience effect, we could not infer the relationship between u’s inherent preferences for i and $j ;$ for example, either $r _ { u i } \ge r _ { u j }$ or $r _ { u i } < r _ { u j }$ may hold if $b _ { u i }$ is significantly larger than $b _ { u j }$ . Thus, only the item salience effect–related inequality can be derived, that is, $b _ { u i } > b _ { u j }$

Case 3 $( v _ { u i } = v _ { u j } )$ . In this case, u provides the same feedback to i and j so that the relation of the overall effects (formed by inherent preference and item salience effect) cannot be determined. Thus, we can only derive the inequality of item salience effects based on the proxy variables, and the relation of inherent preference is not determined; for example, considering the case that $v _ { u i } =$ $v _ { u j } = 1$ and $\pi _ { i } < \pi _ { j } ,$ either $r _ { u i } \ge r _ { u j }$ or $r _ { u i } < r _ { u j }$ can be the truth if both $r _ { u i }$ and $r _ { u j }$ are sufficiently large.

We formulate an optimization problem to disentangle consumers’ inherent preferences and the item salience effects. Given proxy variables’ potential measurement errors and consumer behavior’s probabilistic nature, we include the aforementioned properties in the objective function, rather than hard constraints for a robust inference. Specifically, we punish each inequality with a negative log-sigmoid loss term––an option used commonly in extant research (Zheng et al. 2021). The loss function of disentangling the inherent preference and item salience effect is formulated as

$$
\begin{array}{l} \mathcal {L} _ {r b} = - \sum_ {u = 1} ^ {U} \sum_ {i = 1} ^ {I} \sum_ {j = 1: j \neq i} ^ {I} \mathbb {I} (v _ {u i} = 1, v _ {u j} = 0, \pi_ {i} \leq \pi_ {j}) \log \Lambda \\ (r _ {u i} - r _ {u j}) + \mathbb {I} (\pi_ {i} > \pi_ {j}) \log \Lambda (b _ {u i} - b _ {u j}). \end{array}\tag{18}
$$

4.1.3.4. Disentangling Inherent Preference and Conformity Effect. Denoting $\mathfrak { d } = ( \delta _ { 1 } , \delta _ { 2 } , \dots , \delta _ { I } ) ^ { T }$ as the proxy variable for the conformity effect, that is, if $\delta _ { i } > \delta _ { j } ,$ we expect $c _ { u i } > c _ { u j }$ for $u \in \mathcal { U }$ . Disentangling $r _ { u i }$ and $c _ { u i }$ is more challenging than disentangling $r _ { u i }$ and $b _ { u i }$ because of the decision mechanism’s heterogeneity, as well as the triangle-structured digital footprints. When examining a single behavior type, common effect properties cannot be derived. For instance, focusing on add-to-cart behavior for user u choosing i over j (i.e., $a _ { u i } = 1 , a _ { u j } = 0 )$ does not allow for direct derivation of common effect. This is because u may not have viewed $j ,$ or may have purchased i immediately after viewing, preventing pairwise comparisons as above because of different decision mechanisms. Essentially, the derivation of common effect properties should be decision dependent. In the aforementioned example, causality information can be extracted with respect to $( a _ { u i } = 1 _ { . }$ $a _ { u j } = 0 )$ if and only if both $v _ { u i } = v _ { u j } = 1$ and $s _ { u i } = s _ { u j } = 0$ hold, that is, both i and j are considered by u through the add-to-cart decision. Nevertheless, decision dependence additionally incurs a negative sample attribution problem in the triangle-structured digital footprints; that ${ \mathrm { i } } \mathbf { s } ,$ some implicit feedback in the triangle structure is ambiguous as negative samples because of the invisible decision paths. As illustrated in Figure $5 , \mathsf { a } \left( u , j \right)$ pair can be the negative case of either a $( u , i )$ pair or a $( u , i ^ { \prime } )$ pair, depending on the latent decision path. With our proposed decision path choice variable $s _ { u j } ,$ , this problem can be solved by employing its posterior probability $Q ( s _ { u j } )$ to weigh the negative sample case $( u , j )$ with respect to different decision paths. Therefore, the loss function of disentangling inherent preference and conformity effect is formulated in Equation (19), where each indicator function I(·) of consumer behaviors represents a case of pairwise comparison:

$$
\begin{array}{l} \mathcal {L} _ {r c} = - \sum_ {u = 1} ^ {U} \sum_ {i = 1} ^ {I} \sum_ {j = 1: j \neq i} ^ {I} \\ \left( \begin{array}{l} \mathbb {I} (a _ {u i} = 1, a _ {u j} = 0, v _ {u i} = v _ {u j} = 1, z _ {u j} = 0) Q (s _ {u j} = 0) \\ + \mathbb {I} (z _ {u i} = 1, z _ {u j} = 0, v _ {u i} = v _ {u j} = 1, a _ {u i} = a _ {u j} = 0) Q (s _ {u j} = 1) \\ + \mathbb {I} (z _ {u i} = 1, z _ {u j} = 0, v _ {u i} = v _ {u j} = 1, a _ {u i} = a _ {u j} = 1) \end{array} \right) \\ \times \mathbb {I} (\delta_ {i} \leq \delta_ {j}) \mathrm{log} \Lambda (r _ {u i} - r _ {u j}) + \mathbb {I} (\delta_ {i} > \delta_ {j}) \mathrm{log} \Lambda (c _ {u i} - c _ {u j}). \end{array}\tag{19}
$$

We integrate the behavior modeling loss, $\mathcal { L } _ { b e h a v i o r } ,$ with the two cause disentanglement losses, $\mathcal { L } _ { r b }$ and $\mathcal { L } _ { \boldsymbol { r } \boldsymbol { c } } ,$ as a multiobjective optimization problem. The objective function to be minimized is

Figure 5. (Color online) Negative Sample Attribution Problem  
![](/api/attachments/HRRXA4H7/fulltext/images/5f0c921d628f3ea2766ca60e2d23c2785274bd7b74503074dc961ff28a5b6fe5.jpg)

$$
L = \mathcal {L} _ {b e h a v i o r} + \lambda_ {1} \mathcal {L} _ {r b} + \lambda_ {2} \mathcal {L} _ {r c},\tag{20}
$$

where $\lambda _ { 1 } > 0$ and $\lambda _ { 2 } > 0$ are hyperparameters controlling the causal embedding learning tasks’ weights.

## 4.2. Model Identifiability Analysis

The causality learning mechanism of our approach lies in incorporating a causal embedding learning task to identify the causes and their weights in impacting different decisions in the causal graph. We formally demonstrate the theoretical foundations as follows.

Theorem 1 (Identifiability of DISC Model). Denote $\mathbf { R } =$ $[ r _ { u i } ] _ { u \in \mathcal { U } , i \in \mathcal { I } } , \mathrm { \bf ~ B } = [ b _ { u i } ] _ { u \in \mathcal { U } , i \in \mathcal { I } } , \mathrm { \bf C } = [ c _ { u i } ] _ { u \in \mathcal { U } , i \in \mathcal { I } } , \mathrm { \bf \Phi } \Theta = [ \theta _ { u i } ] _ { u \in \mathcal { U } , i \in \mathcal { I } } .$ The causal graph model of DISC is identifiable with respect to $\{ \mathbf { R } , \mathbf { B } , \mathbf { C } , \mathbf { \Theta } , \mathbf { \alpha } \alpha , \mathbf { \beta } \}$ with the causal embedding learning task $i f \left( { \mathrm { a } } \right) { \mathrm { r a n k } } ( \eta _ { 1 } { \bf R } + \eta _ { 2 } { \bf C } ) > 1 f o r \eta _ { 1 } \neq 0 o r \eta _ { 2 } \neq 0 , \left( { \mathrm { b } } \right)$ rank ${ \binom { \alpha _ { 2 } } { \beta _ { 2 } } } \alpha _ { 3 } \quad 1 \big ) = 2 ,$ and (c) there exists $( i , j ) \in \mathcal { I } \times \mathcal { I }$ such that $\begin{array} { r } { \sum _ { u = 1 } ^ { U } ( r _ { u i } - r _ { u j } ) \neq 0 . } \end{array}$

The proof is provided in Online Appendix A. Theorem 1 implies that DISC’s causal graph is identifiable under three mild assumptions of parameters. Specifically, assumptions (a) and (c) assume that there are variations in inherent preferences and conformity effects, which are common because of the heterogeneity of consumers and products. Assumption (b) also generally holds as it is related to the different mechanisms of various decisions. Theorem 1 demonstrates the sufficiency of constructing item-specific proxy variables for causality learning. Moreover, the proposed decision path choice variable $s _ { u i }$ functions as a necessity of model identifiability (see Online Appendix $\mathrm { A } ) _ { - }$ , which theoretically shows the rationale of our approach for introducing $s _ { u i }$ to reflect consumers’ decision mechanisms.

## 4.3. Model Inference

Because the latent variable that indicates the decision path choice leads to a log-sum structure in $\mathcal { L } _ { b e h a v i o r } ,$ we employ the EM algorithm for parameter learning. Concretely, during the Expectation (E) step, we infer the posterior probability of $s _ { u i }$ . During the Maximization (M) step, we first derive the upper bound of the logsum structure in $\mathcal { L } _ { b e h a v i o r }$ based on Jensen’s inequality. The upper bound of the loss function $\mathcal { L }$ then can be minimized. The model inference details and computational complexity analysis are provided in Online Appendix $\mathrm { B , }$ Section B.2.

Consumers’ purchase behavior can be predicted given the estimated parameters. For item i that has not been purchased by user $u ,$ if there is no historical interaction, then the purchase probability will be

$$
\hat {P} (z _ {u i} = 1) = \hat {\Lambda} _ {u i} ^ {v} (\hat {\theta} _ {u i} \hat {\Lambda} _ {u i} ^ {v z} + (1 - \hat {\theta} _ {u i}) \hat {\Lambda} _ {u i} ^ {a} \hat {\Lambda} _ {u i} ^ {a z}),\tag{21}
$$

in which ·ˆ represents the estimated result. That is, u needs to view i and then purchase i through either impulsive or cautious decision path. If u has already viewed $i ,$ then the purchase probability will be

$$
\hat {P} (z _ {u i} = 1 | v _ {u i} = 1) = \hat {\theta} _ {u i} \hat {\Lambda} _ {u i} ^ {v z} + (1 - \hat {\theta} _ {u i}) \hat {\Lambda} _ {u i} ^ {a} \hat {\Lambda} _ {u i} ^ {a z}.\tag{22}
$$

Finally, if u has added i to the cart, the purchase probability will be

$$
\hat {P} (z _ {u i} = 1 | a _ {u i} = 1, v _ {u i} = 1) = \hat {\Lambda} _ {u i} ^ {a z}.\tag{23}
$$

## 4.4. Causal Recommendations

As the shopping environment on e-commerce platforms can change constantly because of new ads, promotion campaigns, etc., recommendations need to accommodate this unstable environment. With the proposed causal graph, our DISC approach can generate recommendation policies for different scenarios through counterfactual inference. Specifically, the change in the recommendation environment can be viewed as the intervention on external causes in the causal graph. Counterfactual inferences are made based on the causes after intervention in a particular test scenario to form causal recommendations, that is, given the observed digital footprints of consumers $( \mathrm { i . e . } $ , actual data), we infer what the purchase probability would be (i.e., counterfactual outcomes) if causes (i.e., antecedents) were intervened on (Pearl et al. 2016). With the EM algorithm, the causal graph’s parameters can be estimated given the actual data. Based on the learned model $\hat { \mathcal { F } } _ { \mathcal { l } }$ , the purchase probabilities in different condi tions can be computed through intervention operation, that is, $P _ { \hat { \mathcal { F } } } ( z _ { u i } = \bar { 1 } | \mathrm { d o } ( b _ { u i } = b _ { u i } ^ { \prime } , c _ { u i } = c _ { u i } ^ { \prime } ) ) , P _ { \hat { \mathcal { F } } } ( z _ { u i } = 1 | v _ { u i } =$ $1 , \mathrm { d o } ( b _ { u i } = b _ { u i } ^ { \prime } , c _ { u i } = c _ { u i } ^ { \prime } ) )$ , and $P _ { \hat { \mathcal { F } } } ( z _ { u i } = 1 | \bar { a } _ { u i } = 1 , v _ { u i } = 1 _ { . }$ do $( b _ { u i } = b _ { u i } ^ { \prime } , c _ { u i } = c _ { u i } ^ { \prime } ) )$ , in which $b _ { u i } ^ { \prime }$ and $c _ { u i } ^ { \prime }$ are the item salience and conformity effects after intervention. Because the causes are root nodes in the causal graph, the intervention operation is equivalent to directly replacing the item salience and conformity effects in Equations (21)–(23) with $b _ { u i } ^ { \prime }$ and $c _ { u i } ^ { \prime } ,$ respectively, which is a simple case of backdoor criterion (Pearl et al. 2016). In particular, in inherent preference-oriented recommendations, the item salience and conformity effects need to be eliminated, that is, $b _ { u i } ^ { \prime } = 0 , c _ { u i } ^ { \prime } = 0 .$ , as shown in Definition 1.

## 5. Evaluation

Extensive experiments are conducted to evaluate our proposed approach’s (DISC’s) performance from three perspectives. First, we evaluate DISC’s in-sample purchase behavior prediction performance, which focuses on the prediction without intervention and employs observational purchase data for testing. The experiments on in-sample fitness aim to examine DISC’s effectiveness in modeling the interconnection of multiple types of implicit feedback. Second, we examine DISC’s performance in generating inherent preference oriented recommendations using intervention data as the test bed, which focuses on cause disentanglement. Third, we investigate whether the parameters learned by DISC can capture consumers’ decision path choice patterns, item salience effects, and conformity effects with reasonable interpretation.

## 5.1. Data Sets

We use two real-world data sets, Beibei and Taobao, for evaluation, both of which record multiple types of implicit consumer feedback, including view, add-to-cart, and purchase. The Beibei data set was collected from an e-commerce platform specializing in maternal and infant products in China from June 1, 2017, to June 30, 2017.<sup>1</sup> The Taobao data set, collected from Alibaba, China’s largest e-commerce platform, spans from November 25, 2017, to December 3, 2017,<sup>2</sup> and it includes various product categories. Considering both data sparsity and the user–item interaction matrix scale, we preprocess Beibe and Taobao to retain users with more than 20 and 10 purchase records, respectively.

To evaluate in-sample purchase behavior prediction performance, the purchase data in the recorded digital footprint sequence are split at a ratio of 7:1:2 for training, validation, and testing, respectively. View and add-tocart events, which happened before the timing of purchases for validation and testing, are included in the training set with the sequential order of different types of behaviors preserved. Hyperparameters including $\lambda _ { 1 } ,$ $\lambda _ { 2 } ,$ training epochs, and learning rates are tuned based on the validation set. For inherent preference-oriented recommendations, an ideal test set is a collection of consumers’ inherent preferences obtained from surveys or similar experimental tools. However, obtaining such data is challenging because of high collection costs. Therefore, we use intervention purchase data for validation and testing, a common approach in out-of-sample tests for debiasing recommendation methods (Liang et al. 2016a, Bonner and Vasile 2018, Zheng et al. 2021, Chen et al. 2023). Following prior studies, we construct intervention data that align with multiple types of digital footprints and obtain a 7:1:2 ratio for the training (observational), validation (intervention), and test (intervention) sets of purchase records (see Online Appendix C, Section C.1). The validation and test sets are balanced with few item salience and conformity effects, ensuring a distribution distinct from the training set’s purchase data. Descriptive statistics of the data sets are provided in Online Appendix C, Section C.2.

In terms of the proxy variables for item salience and conformity effects, we follow extant research and use the number of views and sales volume of products, respectively (Dewan et al. 2017, Nikolov et al. 2019). We conduct a simulation analysis to validate the ratio nality of these proxy variables (see Online Appendix $C ,$ Section C.3).

## 5.2. Baselines and Metrics

We compare DISC with four groups of baselines provided in Table 2 and further described in Online Appendix C, Section C.4. To the best of our knowledge, no prior research has holistically considered multiple types of implicit feedback and disentangled various causes. Besides, we incorporate a Bayesian network (BN) for performance comparison, which mirrors DISC’s structure but lacks cause disentanglement. Given the structural similarity, BN is identical to DISC in in-sample fitness. Hence, we compare the performance of the two models in inherent preference-oriented recommendations which involves intervention.

A top-n list can be built for each user by ranking items based on model predictions. For in-sample purchase behavior predictions, all methods make predictions following a conventional manner that interweaves various causes together. In terms of evaluating inherent preference-oriented recommendations performance, methods with debiasing mechanisms can generate predictions purely based on estimated inherent preferences. Commonly used ranking-based metrics––including precision (P), mean average precision (MAP), and normalized discounted cumulative gain (NDCG)––are adopted for performance measurement (see Online Appendix C, Section C.5). The setting of embedding dimension (i.e., K) is shown in Online Appendix C, Section C.6.

Table 2. Brief Descriptions of Baselines

<table><tr><td>Baseline group and brief description</td><td>Method</td><td>Information used</td></tr><tr><td>1. Recommendation method using a single type of implicit feedback without debiasing</td><td>RandomPMF (Mnih and Salakhutdinov 2007)UserKNN (Breese et al. 1998)DeepFM (Guo et al. 2017)</td><td>Purchase</td></tr><tr><td>2. Recommendation method using multiple types of implicit feedback without debiasing</td><td>NMTR (Gao et al. 2019)EHCF (Chen et al. 2020a)</td><td>View, add-to-cart, and purchase</td></tr><tr><td>3. Debiasing-oriented recommendation method</td><td></td><td></td></tr><tr><td>Exposure-based model</td><td>ExpoMF (Liang et al. 2016b)</td><td>Purchase</td></tr><tr><td>Causal embedding</td><td>CausE (Bonner and Vasile 2018)DICE (Zheng et al. 2021)</td><td>Purchase</td></tr><tr><td>IPS approach</td><td>IPS-Salience (Saito et al. 2020)IPS-Logit (Schnabel et al. 2016)IPS-1BITMC (Ma and Chen 2019)</td><td>View and purchase</td></tr><tr><td>4. Causal graph structure search method</td><td>GIN (Xie et al. 2020)</td><td>View, add-to-cart, and purchase</td></tr></table>

## 5.3. Results

5.3.1. In-Sample Fitness. We first evaluate DISC’s in-sample fitness without intervention, in which observational purchase data are used for validation and testing. The results of in-sample purchase behavior predictions using Beibei and Taobao are provided in Table 3. From Table 3, we can find that DISC robustly outperforms all baseline methods, indicating that consumers’ flexible shopping process is modeled properly for interconnecting multiple implicit feedback to guarantee favorable in-sample fitness. The inferior performances of baselines in Groups 1 and 3 occur because they could not utilize the data thoroughly. As for Group 2 methods, NMTR’s poor performance derives from its assumption of a cascading relationship of consumers’ multiple behaviors, which does not hold practically, resulting in model misspecification. EHCF’s inferior performance can be attributed to its emphasis on correlations among behaviors while neglecting the shopping stage transition process. Moreover, GIN in Group 4 performs poorly because it is purely data driven, and evident interdependence among multiple types of consumer behaviors is not detected.

## 5.3.2. Inherent Preference-Oriented Recommendation

Performance. To evaluate inherent preference-oriented recommendation performance, intervention validation and test sets are employed. The intervention data seek to reweigh the observational data to simulate the outcome that is not affected by item salience and conformity effects, thereby providing a debiased test bed to evaluate inherent preference-oriented recommendation performance. Following existing studies (Liang et al. 2016a, Bonner and Vasile 2018, Zheng et al. 2021), we construct the intervention data using a sampling strategy (see Online Appendix C, Section C.1), with which the sampled data can be regarded as behaviors generated under a random policy from the synthetic causal system (Cheng et al. 2022, Chen et al. 2023).

Table 3. Results of In-Sample Purchase Behavior Predictions

<table><tr><td rowspan="2">Methods</td><td colspan="3">Beibei</td><td colspan="3">Taobao</td></tr><tr><td>P@5</td><td>MAP@5</td><td>NDCG@5</td><td>P@5</td><td>MAP@5</td><td>NDCG@5</td></tr><tr><td>Random</td><td>0.0008</td><td>0.0019</td><td>0.0010</td><td>0.0003</td><td>0.0006</td><td>0.0003</td></tr><tr><td>PMF</td><td>0.1295</td><td>0.2438</td><td>0.1486</td><td>0.0169</td><td>0.0401</td><td>0.0262</td></tr><tr><td>UserKNN</td><td>0.1266</td><td>0.2374</td><td>0.1442</td><td>0.0199</td><td>0.0463</td><td>0.0305</td></tr><tr><td>DeepFM</td><td>0.1088</td><td>0.2115</td><td>0.1254</td><td>0.0062</td><td>0.0156</td><td>0.0088</td></tr><tr><td>ExpoMF</td><td>0.0998</td><td>0.1844</td><td>0.1117</td><td>0.0191</td><td>0.0431</td><td>0.0284</td></tr><tr><td>CausE</td><td>0.0631</td><td>0.1383</td><td>0.0739</td><td>0.0042</td><td>0.0112</td><td>0.0059</td></tr><tr><td>DICE</td><td>0.1065</td><td>0.1986</td><td>0.1195</td><td>0.0161</td><td>0.0357</td><td>0.0238</td></tr><tr><td>NMTR</td><td>0.1688</td><td>0.3163</td><td>0.1942</td><td>0.0525</td><td>0.1226</td><td>0.0879</td></tr><tr><td>EHCF</td><td>0.3444</td><td>0.5956</td><td>0.4174</td><td>0.0708</td><td>0.1531</td><td>0.1099</td></tr><tr><td>IPS-Salience</td><td>0.1440</td><td>0.2290</td><td>0.1487</td><td>0.0914</td><td>0.1814</td><td>0.1364</td></tr><tr><td>IPS-Logit</td><td>0.0708</td><td>0.1426</td><td>0.0767</td><td>0.0850</td><td>0.1820</td><td>0.1303</td></tr><tr><td>IPS-1BITMC</td><td>0.2919</td><td>0.4835</td><td>0.3383</td><td>0.1098</td><td>0.2268</td><td>0.1713</td></tr><tr><td>GIN</td><td>0.2751</td><td>0.5097</td><td>0.3320</td><td>0.1046</td><td>0.2183</td><td>0.1618</td></tr><tr><td>DISC</td><td>0.4674</td><td>0.6647</td><td>0.5414</td><td>0.1161</td><td>0.2363</td><td>0.1822</td></tr><tr><td></td><td>P@10</td><td>MAP@10</td><td>NDCG@10</td><td>P@10</td><td>MAP@10</td><td>NDCG@10</td></tr><tr><td>Random</td><td>0.0008</td><td>0.0024</td><td>0.0013</td><td>0.0002</td><td>0.0007</td><td>0.0004</td></tr><tr><td>PMF</td><td>0.1040</td><td>0.2422</td><td>0.1591</td><td>0.0143</td><td>0.0422</td><td>0.0339</td></tr><tr><td>UserKNN</td><td>0.1044</td><td>0.2388</td><td>0.1578</td><td>0.0164</td><td>0.0489</td><td>0.0394</td></tr><tr><td>DeepFM</td><td>0.0918</td><td>0.2126</td><td>0.1378</td><td>0.0056</td><td>0.0177</td><td>0.0116</td></tr><tr><td>ExpoMF</td><td>0.0849</td><td>0.1871</td><td>0.1232</td><td>0.0170</td><td>0.0472</td><td>0.0389</td></tr><tr><td>CausE</td><td>0.0583</td><td>0.1469</td><td>0.0870</td><td>0.0036</td><td>0.0129</td><td>0.0081</td></tr><tr><td>DICE</td><td>0.0918</td><td>0.2013</td><td>0.1334</td><td>0.0131</td><td>0.0384</td><td>0.0306</td></tr><tr><td>NMTR</td><td>0.1381</td><td>0.3120</td><td>0.2153</td><td>0.0338</td><td>0.1270</td><td>0.0980</td></tr><tr><td>EHCF</td><td>0.2410</td><td>0.5659</td><td>0.4298</td><td>0.0613</td><td>0.1665</td><td>0.1488</td></tr><tr><td>IPS-Salience</td><td>0.1503</td><td>0.2491</td><td>0.2067</td><td>0.0726</td><td>0.1942</td><td>0.1753</td></tr><tr><td>IPS-Logit</td><td>0.0694</td><td>0.1594</td><td>0.1008</td><td>0.0647</td><td>0.1939</td><td>0.1632</td></tr><tr><td>IPS-1BITMC</td><td>0.2323</td><td>0.4606</td><td>0.3769</td><td>0.0827</td><td>0.2357</td><td>0.2109</td></tr><tr><td>GIN</td><td>0.2050</td><td>0.4811</td><td>0.3554</td><td>0.0871</td><td>0.2292</td><td>0.2147</td></tr><tr><td>DISC</td><td>0.3821</td><td>0.6203</td><td>0.6280</td><td>0.0976</td><td>0.2495</td><td>0.2414</td></tr></table>

Note. The bold font represents the best-performed method.

Table 4. Results of Inherent Preference-Oriented Recommendations

<table><tr><td rowspan="2">Methods</td><td colspan="3">Beibei</td><td colspan="3">Taobao</td></tr><tr><td>P@5</td><td>MAP@5</td><td>NDCG@5</td><td>P@5</td><td>MAP@5</td><td>NDCG@5</td></tr><tr><td>Random</td><td>0.0007</td><td>0.0020</td><td>0.0008</td><td>0.0002</td><td>0.0003</td><td>0.0002</td></tr><tr><td>PMF</td><td>0.0085</td><td>0.0208</td><td>0.0119</td><td>0.0045</td><td>0.0097</td><td>0.0063</td></tr><tr><td>UserKNN</td><td>0.0059</td><td>0.0139</td><td>0.0082</td><td>0.0074</td><td>0.0192</td><td>0.0120</td></tr><tr><td>DeepFM</td><td>0.0042</td><td>0.0094</td><td>0.0054</td><td>0.0006</td><td>0.0011</td><td>0.0007</td></tr><tr><td>ExpoMF</td><td>0.0122</td><td>0.0273</td><td>0.0153</td><td>0.0085</td><td>0.0188</td><td>0.0126</td></tr><tr><td>CausE</td><td>0.0039</td><td>0.0088</td><td>0.0044</td><td>0.0006</td><td>0.0019</td><td>0.0013</td></tr><tr><td>DICE</td><td>0.0139</td><td>0.0327</td><td>0.0176</td><td>0.0072</td><td>0.0159</td><td>0.0107</td></tr><tr><td>NMTR</td><td>0.0190</td><td>0.0418</td><td>0.0221</td><td>0.0488</td><td>0.1123</td><td>0.0799</td></tr><tr><td>EHCF</td><td>0.0314</td><td>0.0706</td><td>0.0374</td><td>0.0848</td><td>0.1652</td><td>0.1294</td></tr><tr><td>BN</td><td>0.1620</td><td>0.2274</td><td>0.1648</td><td>0.1072</td><td>0.2141</td><td>0.1653</td></tr><tr><td>IPS-Salience</td><td>0.0736</td><td>0.1610</td><td>0.0890</td><td>0.0813</td><td>0.1734</td><td>0.1244</td></tr><tr><td>IPS-Logit</td><td>0.0636</td><td>0.1311</td><td>0.0719</td><td>0.0802</td><td>0.1702</td><td>0.1223</td></tr><tr><td>IPS-1BITMC</td><td>0.0615</td><td>0.1248</td><td>0.0689</td><td>0.0802</td><td>0.1705</td><td>0.1224</td></tr><tr><td>GIN</td><td>0.1092</td><td>0.1947</td><td>0.1173</td><td>0.0951</td><td>0.1977</td><td>0.1476</td></tr><tr><td>DISC</td><td>0.2908</td><td>0.4525</td><td>0.3332</td><td>0.1168</td><td>0.2410</td><td>0.1847</td></tr><tr><td></td><td>P@10</td><td>MAP@10</td><td>NDCG@10</td><td>P@10</td><td>MAP@10</td><td>NDCG@10</td></tr><tr><td>Random</td><td>0.0007</td><td>0.0024</td><td>0.0010</td><td>0.0002</td><td>0.0004</td><td>0.0003</td></tr><tr><td>PMF</td><td>0.0070</td><td>0.0234</td><td>0.0141</td><td>0.0047</td><td>0.0118</td><td>0.0097</td></tr><tr><td>UserKNN</td><td>0.0053</td><td>0.0166</td><td>0.0105</td><td>0.0076</td><td>0.0216</td><td>0.0173</td></tr><tr><td>DeepFM</td><td>0.0033</td><td>0.0103</td><td>0.0064</td><td>0.0006</td><td>0.0014</td><td>0.0010</td></tr><tr><td>ExpoMF</td><td>0.0113</td><td>0.0323</td><td>0.0196</td><td>0.0076</td><td>0.0207</td><td>0.0168</td></tr><tr><td>CausE</td><td>0.0038</td><td>0.0111</td><td>0.0059</td><td>0.0005</td><td>0.0021</td><td>0.0015</td></tr><tr><td>DICE</td><td>0.0122</td><td>0.0376</td><td>0.0215</td><td>0.0065</td><td>0.0180</td><td>0.0147</td></tr><tr><td>NMTR</td><td>0.0182</td><td>0.0484</td><td>0.0271</td><td>0.0307</td><td>0.1172</td><td>0.0884</td></tr><tr><td>EHCF</td><td>0.0280</td><td>0.0791</td><td>0.0445</td><td>0.0730</td><td>0.1772</td><td>0.1755</td></tr><tr><td>BN</td><td>0.2169</td><td>0.2775</td><td>0.2890</td><td>0.0890</td><td>0.2257</td><td>0.2181</td></tr><tr><td>IPS-Salience</td><td>0.0685</td><td>0.1753</td><td>0.1108</td><td>0.0631</td><td>0.1856</td><td>0.1572</td></tr><tr><td>IPS-Logit</td><td>0.0637</td><td>0.1485</td><td>0.0953</td><td>0.0630</td><td>0.1830</td><td>0.1555</td></tr><tr><td>IPS-1BITMC</td><td>0.0624</td><td>0.1431</td><td>0.0924</td><td>0.0627</td><td>0.1829</td><td>0.1554</td></tr><tr><td>GIN</td><td>0.1057</td><td>0.2100</td><td>0.1486</td><td>0.0789</td><td>0.2076</td><td>0.1938</td></tr><tr><td>DISC</td><td>0.2774</td><td>0.4331</td><td>0.4301</td><td>0.0955</td><td>0.2512</td><td>0.2395</td></tr></table>

Note. The bold font represents the best-performed method.

The comparison results, based on Beibei and Taobao, are provided in Table 4, in which DISC’s performance largely surpasses others. The superior performance can be attributed to two key aspects of our approach: the establishment of a causal structure informed by consumer behavior theories and an effective cause disentanglement mechanism, which can be further illustrated by the following three aspects. First, the BN model, which shares the same structure as DISC, outperforms all baseline methods, including those such as NMTR, EHCF, and GIN, which also aim to capture the interplay between view, add-to-cart, and purchase behaviors. The superiority underscores the efficacy of our theoretically informed causal structure. Second, DISC’s outperformance of BN demonstrates the additional benefits of integrating cause disentanglement with the established causal structure. Third, baselines with debiasing mechanisms in Group 3 underperform compared with DISC. The disparity showcases DISC’s advantage in integrating a model structure that addresses multiple behavior types and employs cause disentanglement. Exposurebased models are prone to overfitting, and the IPS approach suffers from inaccurate propensity score estimations (Zheng et al. 2021). CausE, while incorporating a modest amount of intervention data into the training set for domain adaptation, is hindered by the scarcity of such data and compromises its effectiveness. DICE, akin to DISC, utilizes disentangled representation learning for cause disentanglement yet falls short because of the absence of an identifiability guarantee for causal effects.

To validate the robustness of DISC’s performance, we further conduct a multifaceted evaluation, which includes analyzing the effectiveness of inherent preference-oriented recommendations for products at different shopping stages, introducing three additional metrics (recall, F1 score, and uplift) for evaluation, examining the impact of varying recommendation list length on the model’s performance, extending experiments to another data set encompassing multiple types of implicit feedback, discussing alternative proxy variable construction, and evaluating causal recommendation performance in various test scenarios beyond inherent preference-oriented recommendations. A detailed compilation of these findings is presented through Online

Table 5. AUC of Decision Path Predictions

<table><tr><td>Methods</td><td>Beibei</td><td>Taobao</td></tr><tr><td>PMF- $\theta$ </td><td>0.5656</td><td>0.7208</td></tr><tr><td>LMF- $\theta$ </td><td>0.6706</td><td>0.9924</td></tr><tr><td>DISC</td><td>0.6966</td><td>0.9985</td></tr></table>

Note. The bold font represents the best-performed method.

Appendix D, Sections D.1–D.6. Furthermore, we delve into the benefits of incorporating auxiliary digital footprints (i.e., view and add-to-cart records) in model training for delivering inherent preference-oriented recommendations through an information ablation study (see Online Appendix E). The findings showcase that both the casual graph structure and the causality learning mechanism contribute to DISC’s superior performance.

5.3.3. Modeling Process Validation and Interpretability. We further evaluate DISC by validating its modeling process, which also demonstrates how DISC functions in detail. First, we evaluate the validity of decision path choice modeling. In DISC, a latent variable, $s _ { u i } ,$ is introduced to indicate a consumer’s decision path choice. We inspect this procedural behavior modeling’s validity based on the performance of decision path choice predictions, which can be regarded as a binary classification problem with the decision paths of purchase records in the test set as the ground truth. In DISC, parameter $\theta _ { u i }$ is defined as the probability of $s _ { u i } = 1$ , the predicted value of which can be used to validate the classification performance. The commonly used metric for classification, the area under the receiver operating characteristic curve (AUC), is used. Two benchmark methods are incorporated for comparison: PMF-θ trains a probabilistic matrix factorization model (Mnih and Salakhutdinov 2007) on decision path choice data in the training set, whereas LMF-θ employs a logistic matrix factorization (Johnson 2014) manner similar to DISC. The results provided in Table 5 indicate that DISC outperforms the two benchmark methods in terms of decision path prediction, corroborating behavior modeling’s efficacy. Compared with LMF-θ, DISC improves performance by absorbing information from consumers add-to-cart and purchase decisions (see Equations (B.6) and (B.7) in Online Appendix B).

Second, as DISC aims to disentangle causes, we scrutinize the parameters related to the item salience and conformity effects. For the item salience effect, we study the similarity between the estimated effect $\hat { b } _ { u i }$ and proxy variable $\pi _ { i } .$ The Pearson correlation coefficient (CORR) and cosine similarity (COSSIM) are adopted as the metrics. The results are summarized in Table $6 ,$ in which the similarity between the estimated inherent preference $\hat { r } _ { u i }$ and $\pi _ { i }$ is included for comparison. As expected, a strong positive correlation is found between $\hat { b } _ { u i } ^ { \star }$ and $\pi _ { i } ,$ whereas $\hat { r } _ { u i }$ is nearly uncorrelated with $\pi _ { i } ,$ indicating that the item salience effect is captured well by $\hat { b } _ { u i } ^ { \phantom { * } } ,$ thereby indicating clear disentanglement.

Table 6. Relation Between the Proxy Variables of Item Salience Effect and Estimated Effect

<table><tr><td rowspan="2">Estimated effect</td><td colspan="2">Beibei</td><td colspan="2">Taobao</td></tr><tr><td>CORR</td><td>COSSIM</td><td>CORR</td><td>COSSIM</td></tr><tr><td> $\hat{b}_{ui}$ </td><td>0.8857</td><td>0.8205</td><td>0.5621</td><td>0.4972</td></tr><tr><td> $\hat{r}_{ui}$ </td><td>-0.1154</td><td>0.2298</td><td>-0.082</td><td>-0.0483</td></tr></table>

To showcase the disentanglement of different causes vividly, we also visualize the learned item embeddings on a two-dimensional plane through dimension reduction, which is illustrated in Online Appendix F, Section F.1, indicating reasonable semantics. A similar analysis is conducted for the conformity effect, of which the results are provided in Online Appendix ${ \mathrm { F } } ,$ Section F.2.

## 6. General Discussion

## 6.1. Alternative Causal Graph Modeling

In this part, we examine the rationality of DISC’s causal structure and the importance of considering the item salience and conformity effects in DISC. To achieve this, five alternative causal graphs are constructed, as depicted in Figure 6, in which the model names include causes that are retained.

DISC-r assumes that consumers’ inherent preferences drive all behaviors. DISC-rc excludes the item salience effect from DISC, that is, the view behavior is assumed to be motivated by inherent preference only, while add-to-cart and purchase decision mechanisms are the same as DISC. DISC-rb excludes the conformity effect, which modifies add-to-cart and purchase modeling to make these behaviors driven by inherent preference alone. DISC-rbias assumes that the item salience and conformity effects are identical, that is, $b _ { u i } = c _ { u i }$ for all $( u , i )$ . DISC-full assumes that each behavior is impacted by three causes jointly.

Figure 6. Alternative Causal Graphs  
![](/api/attachments/HRRXA4H7/fulltext/images/fbe02c13c267e92c9ac06706f595ad60b67d77300778f7ddde33fb3a3a7ae83f.jpg)

Table 7. Comparison of $A I C _ { M }$ of Alternative Causal Graphs

<table><tr><td>Methods</td><td>Beibei</td><td>Taobao</td></tr><tr><td>DISC-r</td><td>43389086.89</td><td>52632222.66</td></tr><tr><td>DISC-rc</td><td>43341295.54</td><td>52629107.23</td></tr><tr><td>DISC-rb</td><td>43353071.54</td><td>52629148.60</td></tr><tr><td>DISC-rbias</td><td>43349611.83</td><td>52630787.80</td></tr><tr><td>DISC-full</td><td>43349578.11</td><td>52630408.57</td></tr><tr><td>DISC</td><td>43337747.71</td><td>52627604.70</td></tr></table>

Note. The bold font represents the best-performed method.

We adopt $A I C _ { M } ,$ a generalized Akaike information criterion (AIC) statistic, to compare various causal graph structures based on observed data and which takes into account the topology of the causal graph, the parameter estimates, and the assumptions of submodels (Shipley and Douma 2020). The results on Beibei and Taobao are shown in Table 7.

From the comparative results shown in Table $^ { 7 , }$ we can see that the model structure of DISC shows the lowest $A I C _ { M }$ value, manifesting the superiority of the theory-driven causal structure. We also evaluate these alternative models’ performances of inherent preferenceoriented recommendation on the Beibei data set. The results are provided in Online Appendix $G ,$ which further confirms DISC’s causal structure.

## 6.2. Potential Managerial Implications

The intervention effects of external factors on consumers’ purchase decisions brought by marketing tools can be investigated to provide insights for potential managerial implications. Given the importance of targeting in marketing strategies, we aim to study the effects of various forms of targeting using the causal graph. Item salience and conformity effects can be intervened on through mass targeting (e.g., search engine advertising; Choi et al. 2020) and social targeting (e.g., highlighting friends’ online reviews; Wang et al. 2018a), respectively. As indicated by the estimated weights of causes in Table 8, the relative importance of these two causes may vary with the decision paths, thus requiring different interventions. Consequently, it is crucial to determine effective targeting strategies.

To figure it out, we investigate the intervention effects of item salience and conformity on purchase probability through impulsive and cautious decision paths, respec tively, which can be inferred by intervention operation (see Section 4.4). On one hand, the intervention on item salience effect influences purchase probability through view behavior. Therefore, the ratios that increase with respect to impulsive purchase likelihood and cautious purchase likelihood are identical; for example, the estimated causal graph based on the Beibei data set indicates that a 10% increase in item salience effect results in about 0.3% increase in purchase probability on average. On the other hand, conformity intervention influences purchase in two ways. With impulsive decision making, conformity influences purchase-after-view decisions directly, whereas with cautious decisions, conformity influences purchases through add-to-cart decisions, as well as purchase-afteradd-to-cart decisions. With the causal graph, we can study the effects on different decision paths separately. For instance, on the Beibei data set, a 10% increase in confor mity effect only leads to about a 0.05% increase in impulsive purchase likelihood, whereas the extent to which cautious purchase probability increases is much more significant (about 1.51%). These findings illustrate the roles of item salience and conformity from a nuanced perspective, sug gesting that impulsive purchasing is less conformity driven. Therefore, mass targeting, like advertisements that intervene on the item salience effect, is more effective in such decision processes. However, cautious purchases heavily depend on conformity, making social targeting that intervenes on the conformity effect more effective.

## 6.3. Model Extensibility

In this study, we tackle the challenge of disentangling causes with a triangle structure of consumers’ digital footprints. Notably, our approach can be extended easily to the research context in which behaviors’ structure is more complicated, as learning causality from more complex structures can be decomposed into basic components that are similar to the triangular one. For behavior modeling, more complex decisions (e.g., quaternary decision) can also be dealt with using a latent variable, $s _ { u i } ,$ that indicates the decision path choice. With the latent variable, decision mechanisms can be modeled properly, and it also functions in causal embedding learning to guarantee decision dependence to derive common effect properties. The negative sample attribution problem will be solved by weighting an ambiguous negative sample $( u , j )$ with the posterior probability of $s _ { u j }$ as well. Moreover, even if more than two causes drive a particular behavior in the new circumstance, the common effect structure still holds that we can extract causality information to disentangle the causes. More proxy variables may be necessary to derive abundant causality information for satisfactory performance. Furthermore, the causes modeled in DISC are primary and can include secondary factors; for example, product position features can be treated as a dimension of the salience effect, and friends’ referrals can be part of the conformity effect.

Table 8. Estimated Weights of Causes in the DISC Model

<table><tr><td>Data sets</td><td> $\alpha_{1}$ </td><td> $\alpha_{2}$ </td><td> $\alpha_{3}$ </td><td> $\alpha_{4}$ </td><td> $\beta_{1}$ </td><td> $\beta_{2}$ </td><td> $\beta_{3}$ </td><td> $\beta_{4}$ </td></tr><tr><td>Beibei</td><td>1</td><td>7.8847***(0.0357)</td><td>0.2989***(0.0611)</td><td>2.5850***(0.0413)</td><td>1</td><td>0.5869***(0.0025)</td><td>0.0378***(0.0051)</td><td>1</td></tr><tr><td>Taobao</td><td>1</td><td>7.4411***(0.2292)</td><td>10.5890***(0.2201)</td><td>3.2393***(0.3394)</td><td>1</td><td>0.3598***(0.0089)</td><td>0.6016***(0.0071)</td><td>1</td></tr></table>

Note. Standard errors are in parentheses.  
\*\*\*p < 0:001.

## 7. Conclusion

This study presents a personalized recommendation approach (DISC) based on cause disentanglement across various shopping stages. Analyzing consumers behavioral mechanisms, we model the flexible shopping journey and identify the causes driving consumers’ behaviors at different stages. We construct a causal graph and develop a disentangled representation learning to differentiate these causes. Furthermore, the model identifiability of our approach is theoretically proved, which ensures rigorous causal inference based on observational data. Extensive experiments on real-world data sets with carefully designed protocols demonstrate that DISC outperforms all baselines significantly and preserves good interpretability. Moreover, the robustness of causality assumptions used in DISC is corroborated by fitting consumers’ behavior data into alternative causal graphs. The discussion of model extensibility indicates that our approach can be extended to more complicated research contexts.

Our study contributes to the computational design science literature as follows. Theoretically, we refer to the kernel theories of consumer behavior to reveal the causes of behavioral biases at various shopping stages and construct a valid causal graph to probe consumers inherent preferences. The proposed causal structure is validated through comparisons with various alternative causal graphs on different data sets, which indicates its generalizability. Thus, our study manifests the significance of IT artifact design guided by kernel theories (Gregor and Hevner 2013). Notably, we theoretically prove the identifiability of our proposed approach, which also echoes the intense call for integrating causal inference with machine learning techniques (Athey and Imbens 2019). The identifiability proof can provide rich theoretical implications. For example, the mild assumptions in Theorem 1 pave the way for generalization in other research contexts related to multiple types of implicit feedback. Methodologically, to the best of our knowledge, our study is among the first to disentangle the causes of multiple types of implicit feedback, providing effective and interpretable recommendations in light of debiasing. On one hand, we tackle the modeling chal lenges resulting from the triangle-structured digital footprints. The proposed decision path choice variable, which reflects the decision context, can depict consumers’ flexible shopping stage transition process behind this structure effectively, serving as the necessity of model identifiability. We also utilize the probabilistic inference of decision path choice to solve the negative sample attribution problem in the triangle structure. Because the triangle structure is a foundational compo nent for modeling consumers’ flexible shopping journeys, the proposed approach broadens the way for handling more types of consumers’ implicit feedback. On the other hand, a consolidated framework is designed to evaluate the proposed approach. Differing from most extant studies that only evaluate the prediction performance of consumers’ final purchase behavior, we also examine the validity of modeling procedural behaviors of decision path choices. Therefore, the performance of a recommendation approach that processes consumers’ multiple types of implicit feedback can be evaluated comprehensively. The interpretability is illustrated further through post hoc analysis to address practical concerns regarding a lack of transparent mechanisms in RSs. Furthermore, we illustrate the external causes’ intervention effects on consumers’ purchase likelihood with respect to different decision paths through counterfactual analysis to provide insights for marketing strategy. Therefore, our study contributes to design science literature by proposing an interpretable recommendation approach through rigorous design and evaluation to solve criti cal business problems (Gregor and Hevner 2013).

Our study carries several implications for business practice. The proposed causal graph allows for the estimation of the effect of each factor driving consumer behaviors. This can help e-commerce platforms generate informed recommendations to accommodate differ ent needs. Our approach can also provide insights for both consumers and retailers. For consumers, the disentanglement of the driving factors in purchases could help them learn about their behavioral patterns and biases. For retailers, the proposed approach can reveal more prominent factors in driving consumers’ purchase decisions, which can be used to nudge consumers in a personalized manner.

Our study contains some limitations that call for future research. We consider only three types of representative implicit feedback. Future research may investigate more types of implicit feedback with disentangled causes as extensions of our study. In addition, if more detailed information on the causes is available, proxy variables can be constructed in a finer-grained fashion. Also, as the causes in our proposed approach may vary over time, future studies can further investigate consumers’ longitudinal behavior.

## Acknowledgments

C. Wang and Y. Shi contributed equally and are joint first authors. The authors thank the senior editor, associate edi tor, and anonymous reviewers for their constructive feedback throughout the review process.

## Endnotes

<sup>1</sup> See https://github.com/chenchongthu/EHCF.

<sup>2</sup> See https://tianchi.aliyun.com/dataset/dataDetail?dataId=649.

## References

Adomavicius G, Bockstedt JC, Curley SP, Zhang J (2013) Do recommender systems manipulate consumer preferences? A study of anchoring effects. Inform. Systems Res. 24(4):956–975.

Akerlof GA (1991) Procrastination and obedience. Amer. Econom. Rev. 81(2):1–19.

Athey S, Imbens GW (2019) Machine learning methods that economists should know about. Annual Rev. Econom. 11(1):685–725.

Baeza-Yates R (2018) Bias on the web. Comm. ACM 61(6):54–61.

Beatty SE, Ferrell ME (1998) Impulse buying: Modeling its precur sors. J. Retailing 74(2):169–191.

Bengio Y, Deleu T, Rahaman N, Ke R, Lachapelle S, Bilaniuk O, Goyal A, Pal C (2019) A meta-transfer objective for learning to disentangle causal mechanisms. Preprint, submitted January 30, https://arxiv.org/abs/1901.10912.

Bonner S, Vasile F (2018) Causal embeddings for recommendation. Proc. 12th ACM Conf. Recommender Systems (Association for Computing Machinery, New York), 104–112.

Breese JS, Heckerman D, Kadie C (1998) Empirical analysis of predictive algorithms for collaborative filtering. Cooper GF, Moral S, eds. Proc. 14th Conf. Uncertainty Artificial Intelligence (Morgan Kaufmann, San Francisco), 43–52.

Chen X, Li L, Pan W, Ming Z (2020b) A survey on heterogeneous one-class collaborative filtering. ACM Trans. Inform. Systems 38(4):1–54.

Chen J, Dong H, Wang X, Feng F, Wang M, He X (2023) Bias and debias in recommender system: A survey and future directions. ACM Trans. Inform. Systems 41(3):1–39.

Chen C, Zhang M, Zhang Y, Ma W, Liu Y, Ma S (2020a) Efficient heterogeneous collaborative filtering without negative sampling for recommendation. Proc. AAAI Conf. Artificial Intelligence (AAAI Press, Palo Alto, CA), 19–26.

Cheng L, Guo R, Moraffah R, Sheth P, Candan KS, Liu H (2022) Evaluation methods and measures for causal learning algorithms. IEEE Trans. Artificial Intelligence 3(6):924–943.

Choi H, Mela CF, Balseiro SR, Leary A (2020) Online display adver tising markets: A literature review and future directions. Inform. Systems Res. 31(2):556–575.

Ciampaglia GL, Nematzadeh A, Menczer F, Flammini A (2018) How algorithmic popularity bias hinders or promotes quality. Sci. Rep. 8(1):1–7.

DellaVigna S (2009) Psychology and economics: Evidence from the field. J. Econom. Literature 47(2):315–372.

Dewan S, Ho YJ, Ramaprasad J (2017) Popularity or proximity: Characterizing the nature of social influence in an online music community. Inform. Systems Res. 28(1):117–136.

Dhami S (2016) The Foundations of Behavioral Economic Analysis (Oxford University Press, Oxford, UK).

Ding J, Yu G, He X, Quan Y, Li Y, Chua TS, Jin D, Yu J (2018) Improving implicit recommender systems with view data. Proc. 27th Internat. Joint Conf. Artificial Intelligence (AAAI Press, Palo Alto, CA), 3343–3349.

Dowling K, Guhl D, Klapper D, Spann M, Stich L, Yegoryan N (2020) Behavioral biases in marketing. J. Acad. Marketing Sci. 48(3):449–477.

Fishburn PC (1970) Utility theory for decision making. Technical report, Research Analysis Corporation, McLean, VA.

Fleder D, Hosanagar K (2009) Blockbuster culture’s next rise or fall: The impact of recommender systems on sales diversity. Management Sci. 55(5):697–712

Gao C, He X, Gan D, Chen X, Feng F, Li Y, Chua TS, Yao L, Song Y, Jin D (2019) Learning to recommend with multiple cascading behaviors. IEEE Trans. Knowledge Data Engrg. 33(6): 2588–2601.

Gregor S, Hevner AR (2013) Positioning and presenting design science research for maximum impact. MIS Quart. 37(2):337–355.

Guo R, Cheng L, Li J, Hahn PR, Liu H (2020) A survey of learning causality with data: Problems and methods. ACM Comput. Sur veys 53(4):1–37.

Guo H, Tang R, Ye Y, Li Z, He X (2017) DeepFM: A factorizationmachine based neural network for CTR prediction. Proc. 26th Internat. Joint Conf. Artificial Intelligence (AAAI Press, Palo Alto, CA), 1725–1731.

Hu N, Pavlou PA, Zhang JJ (2017) On self-selection biases in online product reviews. MIS Quart. 41(2):449–471.

Huang B, Zhang K, Zhang J, Ramsey J, Sanchez-Romero R, Glymour C, Scho¨lkopf B (2020) Causal discovery from heterogeneous/ nonstationary data. J. Machine Learn. Res. 21(1):3482–3534.

Hui SK, Inman JJ, Huang Y, Suher J (2013) The effect of in-store travel distance on unplanned spending: Applications to mobile promotion strategies. J. Marketing 77(2):1–16.

Iyer GR, Blut M, Xiao SH, Grewal D (2020) Impulse buying: A meta-analytic review. J. Acad. Marketing Sci. 48(3):384–404.

Johnson CC (2014) Logistic matrix factorization for implicit feedback data. NIPS Workshop Distributed Matrix Computations (Spotify, New York).

Jonas E, Schulz-Hardt S, Frey D, Thelen N (2001) Confirmation bias in sequential information search after preliminary decisions: An expansion of dissonance theoretical research on selective exposure to information. J. Personality Soc. Psych. 80(4):557–571.

Karaman H (2021) Online review solicitations reduce extremity bias in online review distributions and increase their representative ness. Management Sci. 67(7):4420–4445.

Koren Y, Bell R, Volinsky C (2009) Matrix factorization technique for recommender systems. Computer 42(8):30–37.

Lam WY, Andrews B, Ramsey J (2022) Greedy relaxations of the sparsest permutation algorithm. Cussens J, Zhang K, eds. Proc. 38th Conf. Uncertainty Artificial Intelligence. Proceedings of Machine Learning Research, vol. 180 (PMLR, New York) 1052–1062.

Lee L, Inman JJ, Argo JJ, Bo¨ ttger T, Dholakia U, Gilbride T, Van Ittersum K, et al. (2018) From browsing to buying and beyond: The needs-adaptive shopper journey model. J. Assoc. Consumer Res. 3(3):277–293.

Li SS, Karahanna E (2015) Online recommendation systems in a B2C E-commerce context: A review and future directions. J. Assoc. Inform. Systems 16(2):72–107.

Li X, Grahl J, Hinz O (2022) How do recommender systems lead to consumer purchases? A causal mediation analysis of a field experiment. Inform. Systems Res. 33(2):620–637.

Liang D, Charlin L, Blei DM (2016a) Causal inference for recommendation. Causation: Foundation to Application Workshop, vol. 6, No. 41 (AUAI, New York), 108.

Liang D, Charlin L, McInerney J, Blei DM (2016b) Modeling user exposure in recommendation. Proc. 25th Internat. Conf. World Wide Web (International World Wide Web Conferences Steering Committee, Geneva), 951–961.

Ma W, Chen GH (2019) Missing not at random in matrix comple tion: The effectiveness of estimating missingness probabilities under a low nuclear norm assumption. Wallach H, Larochelle H, Beygelzimer A, d’Alche´-Buc F, Fox E, Garnett R, eds. Proc.

33rd Internat. Conf. Neural Inform. Processing Systems, vol. 32 (Curran Associates, Red Hook, NY), 14900–14909.

Miao W, Geng Z, Tchetgen Tchetgen EJ (2018) Identifying causa effects with proxy variables of an unmeasured confounder. Bio metrika 105(4):987–993.

Mnih A, Salakhutdinov RR (2007) Probabilistic matrix factorization. Platt J, Koller D, Singer Y, Roweis S, eds. Advances in Neural Information Processing Systems, vol. 20 (Curran Associates, Red Hook, NY).

Montgomery MR, Gragnolati M, Burke KA, Paredes E (2000) Measuring living standards with proxy variables. Demography 37(2):155–174.

Muchnik L, Aral S, Taylor SJ (2013) Social influence bias: A randomized experiment. Science 341(6146):647–651.

Nikolov D, Lalmas M, Flammini A, Menczer F (2019) Quantifying biases in online information exposure. J. Assoc. Inform. Sci. Tech. 70(3):218–229.

Olley GS, Pakes A (1996) The dynamics of productivity in the telecom munications equipment industry. Econometrica 64(6):1263–1297.

Pearl J (2009) Causality (Cambridge University Press, Cambridge, UK).

Pearl J, Glymour M, Jewell NP (2016) Causal Inference in Statistics: A Primer (John Wiley & Sons, Hoboken, NJ).

Peng J, Liang C (2023) On the differences between view-based and purchase-based recommender systems. MIS Quart. 47(2):875–900.

Sahoo N, Singh PV, Mukhopadhyay T (2012) A hidden Markov model for collaborative filtering. MIS Quart. 36(4):1329–1356.

Saito Y, Yaginuma S, Nishino Y, Sakata H, Nakata K (2020) Unbiased recommender learning from missing-not-at-random implicit feed back. Proc. 13th Internat. Conf. Web Search Data Mining (Association for Computing Machinery, New York), 501–509.

Schnabel T, Swaminathan A, Singh A, Chandak N, Joachims T (2016) Recommendations as treatments: Debiasing learning and evaluation. Balcan MF, Weinberger KQ eds. Proc. 33rd Internat. Conf. Machine Learn. (JMLR.org), 1670–1679.

Scho¨lkopf B, Locatello F, Bauer S, Ke NR, Kalchbrenner N, Goyal A, Bengio Y (2021) Toward causal representation learning. Proc. IEEE 109(5):612–634.

Shipley B, Douma JC (2020) Generalized AIC and chi-squared statis tics for path models consistent with directed acyclic graphs. Ecology 101(3):e02960.

Simon HA (1955) A behavioral model of rational choice. Quart. J. Econom. 69(1):99–118.

Simonson I (2008) Will I like a “medium” pillow? Another look at constructed and inherent preferences. J. Consumer Psych. 18(3):155–169.

Sun T, Yuan Z, Li C, Zhang K, Xu J (2024) The value of persona data in Internet commerce: A high-stakes field experiment on data regulation policy. Management Sci. 70(4):2645–2660.

Valogianni K, Padmanabhan B, Qiu L (2023) Causal ABM: A methodology for learning plausible causal models using agent-based

modeling. Preprint, submitted January 31, http://dx.doi.org/10 2139/ssrn.4343647.

Wang T, Rudin C (2022) Causal rule sets for identifying subgroups with enhanced treatment effects. INFORMS J. Comput. 34(3): 1626-1643.

Wang W, Xu J, Wang M (2018b) Effects of recommendation neutrality and sponsorship disclosure on trust vs. distrust in online recommendation agents: Moderating role of explanations for organic recommendations. Management Sci. 64(11):5198–5219.

Wang C, Zhang X, Hann IH (2018a) Socially nudged: A quasiexperimental study of friends’ social influence in online prod uct ratings. Inform. Systems Res. 29(3):641–655.

Wang W, Feng F, He X, Wang X, Chua TS (2021b) Deconfounded recommendation for alleviating bias amplification. Proc. 27t ACM SIGKDD Conf. Knowledge Discovery Data Mining (Associa tion for Computing Machinery, New York), 1717–1725.

Wang S, Cao L, Wang Y, Sheng QZ, Orgun MA, Lian D (2021a) A survey on session-based recommender systems. ACM Comput Surveys 54(7):1–38.

Wooldridge JM (2015) Introductory Econometrics: A Modern Approach (Cengage Learning, Boston).

Xia K, Lee KZ, Bengio Y, Bareinboim E (2021) The causal-neural connection: Expressiveness, learnability, and inference. Ranzato M, Beygelzimer A, Dauphin Y, Liang PS, Vaughan JW, eds. Advances in Neural Information Processing Systems, vol. 34 (Cur ran Associates, Red Hook, NY), 10823–10836.

Xie F, Cai R, Huang B, Glymour C, Hao Z, Zhang K (2020) Generalized independent noise condition for estimating latent variable causal graphs. Larochelle H, Ranzato M, Hadsell R, Balcan MF, Lin H, eds. Advances in Neural Information Processing Systems, vol. 33 (Curran Associates, Red Hook, NY), 14891-14902.

Yadav MS, De Valck K, Hennig-Thurau T, Hoffman DL, Spann M (2013) Social commerce: A contingency framework for assessing marketing potential. J. Interactive Marketing 27(4):311–323.

Zhang Y, Feng F, He X, Wei T, Song C, Ling G, Zhang Y (2021) Causal intervention for leveraging popularity bias in recommendation. Proc. 44th Internat. ACM SIGIR Conf. Res. Development Inform. Retrieval (Association for Computing Machinery, New York), 11–20.

Zheng J, Qi Z, Dou Y, Tan Y (2019) How mega is the mega? Exploring the spillover effects of WeChat using graphical model. Inform. Systems Res. 30(4):1343–1362

Zheng Y, Gao C, Li X, He X, Li Y, Jin D (2021) Disentangling user interest and conformity for recommendation with causal embedding. Proc. Web Conf. 2021 (Association for Computing Machin ery, New York), 2980–2991.

Zhou T, Wang Y, Yan L, Tan Y (2023) Spoiled for choice? Personalized recommendation for healthcare decisions: A multiarmed bandit approach. Inform. Systems Res. 34(4):1493–1512.

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.

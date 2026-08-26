---
otero_id: 20068
otero_key: "SA4CFHR8"
title: "Evaluating multimedia advertising campaign effectiveness"
authors: "Pengyuan Wang; Guiyang Xiong; Will Wei Sun; Jian Yang"
year: "2024"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2024.114348"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Evaluating multimedia advertising campaign effectiveness

![](/api/attachments/SA4CFHR8/fulltext/images/61031248d73920dc969421f3088ea4da6c21c4cf208cc3f6518f5fbc41b561cc.jpg)

Pengyuan Wang <sup>a,\*</sup>, Guiyang Xiong <sup>b</sup>, Will Wei Sun <sup>c</sup>, Jian Yang

<sup>a</sup> Terry College of Business, University of Georgia, Athens, GA 30602, United States of America

<sup>b</sup> 721 University Ave, Syracuse University, Syracuse, NY 13244, United States of America

<sup>c</sup> Daniels School of Business, Purdue University, 403 W State St, West Lafayette, IN 47907, United States of America

<sup>d</sup> Yahoo Inc, 391 San Antonio Rd, Mountain View, CA 94040, United States of America

## A R T I C L E I N F O

Keywords: Multimedia advertising Segmentation Ad repetition Causal forest

## A B S T R A C T

Companies increasingly combine multiple media outlets when launching advertising campaigns. This study employs causal forest to examine the effects of complex multimedia campaigns. The model effectively corrects for selection bias, automatically identifies informative consumer features, and performs automated data-driven consumer segmentation based on the consumer features identified. We analyze a large dataset involving around seven million consumers and four thousand covariates, and provide empirical evidence on the nonlinear effect of repeated ad exposures in the multimedia context, how such effect varies across consumer groups, and the contingent existence of multimedia synergy. We demonstrate that negligence of the selection bias and hetero geneity across segments results in suboptimal conversions and a waste of advertising resources. The analysis procedure that we propose can facilitate decision making for complex advertising campaigns to improve their effectiveness.

## 1. Introduction

Companies increasingly launch complex multimedia advertising campaigns that simultaneously leverage multiple media platforms to deliver a consistent message to consumers, aiming to reinforce ad effectiveness via repeated exposures both online and offline [1,2]. For example, JetBlue Airways’ Air on the Side of Humanity campaign included both TV commercials during primetime shows and digital ads on various websites. As stated by Serena Potter, Group Vice President of Marketing of Macy’s,

“We used to have separate budgets. We really now have one mar keting budget, and we’re looking what’s the best way to spend that, what’s the best allocation, what’s the best media mix, whether it’s digital, offline, how do they work together to deliver the most sales.”

Consequently, firms face greater challenges than ever to optimally allocate advertising resources and evaluate advertising effectiveness. For example, how to balance online and traditional ads to maximize conversions? How to determine if an ad campaign has caused changes in consumer behavior? How many times should consumers be exposed to the ad in each media channel? Does ad effectiveness vary across con sumer groups? If so, how to maximize conversions for each consumer segment? Effective deployment of multiple media outlets for advertising is a most pressing concern among campaign decision makers [3,4,1,2].

Datasets on multimedia campaigns, especially those involving digital ads, typically include extremely large numbers of variables and high volumes of observational records about the users [5]. Companies have increasing needs to generate useful insights from these large datasets [6]. As stated by Art Petty, “We are practically drowning in data. Most organizations have become skilled at capturing information about cus tomers… We are making more and more data at a pace that is difficult to comprehend.” In the big data context, one key task is how to identify useful information out of the ocean of data observed. Out of all the variables observed, which ones should a company focus on when mak ing advertising decisions and segmenting consumers?

When estimating the effect of ad campaigns, another key challenge is selection bias [7,8]. With observational data, exposures to ad treatments are not random and it is possible that certain types of consumers have inherently greater propensity of seeing the ads and/or purchasing [7,8]. Such confounding effect can lead to selection bias. Selection bias can become even more intricate in the context of multimedia ads and big data, because (1) there are multiple treatment dimensions (media out lets), each of which can be confounded and (2) due to the large number of observable covariates (e.g., consumer features), it is difficult or even infeasible to manually identify which covariates are confounders.

To assess campaign effectiveness, various approaches have been proposed in the literature on decision support systems (DSS) and related fields. One method is randomized experiment such as A/B testing, where ad variations are tested on randomly selected subgroups of users [9]. However, when the ad treatments involve multiple dimensions and each treatment dimension is non-binary, it is challenging to test all possible treatment variations. Uplift models are popular for inferring treatment effects from observational data. However, most uplift models focus on binary ad treatment $[ 1 0 , 1 1 ]$ and cannot apply to multiple-mediachannel / multiple-exposure campaigns. Although some recent studies have discussed uplift models for multiple treatments [12,13] (see Sec tion 2.1 for details), they focus on estimating heterogeneous or indi vidual treatment effect rather than addressing selection bias, and thus require extra propensity models to address such bias if any. In summary, these previous studies offer valuable methodological advancements and have their pros and cons. They do not provide a well-rounded solution for our objective (i.e., to assess multi-channel multi-exposure campaigns in the presence of selection bias) because the experiment-based ap proaches are infeasible to test all alternatives, regression-based para metric methods lack flexibility, binary uplift models cannot ingest multiple treatments, and heterogeneous-treatment-effect models do not inherently address selection bias.

Segmentation is also crucial in marketing campaign decision making [14] because of the significant heterogeneity across consumers [11,15]. Due to the inherent biological, cognitive, psychological and behavioral differences, various consumer groups tend to react differently to the same campaign $[ 1 6 , 1 7 , 1 8 ]$ . Without proper segmentation, the evalua tion of ad effectiveness may be biased and lead to suboptimal outcomes or waste of resources [3]. The complex nature of multimedia campaigns further complicates the issue, and thus an effective segmentation approach that efficiently leverages big data is imperative to advertisers.

Against these backgrounds, we apply causal forest, a flexible ma chine learning model, to assess multi-dimensional ad treatments and investigate the potential synergy effect across media channels. It effec tively corrects for selection bias, handles a large number of covariates flexibly / non-parametrically, and can be applied to multi-channel multi-exposure campaigns. $\mathsf { A l s o } ,$ it automatically identifies meaningful consumer features and thus helps managers extract useful information from an ocean of data. Using the consumer features identified, it can perform data-driven and automated grouping of consumers and uncover heterogeneous effects for each consumer group. We summarize its distinct advantages in Table 1. We analyze a large-scale real-world dataset on a multimedia “flash campaign” with about seven million consumers and over four thousand observed variables. Results show how the effects of multimedia ad repetition vary across consumer seg ments and suggest that ignorance of the heterogeneous ad effects can lead to not only a waste of marketing resources but also suboptimal conversion results. Our findings add new insights based on hard evi dence from big field data regarding (1) the nonlinear effect of multi media ads, (2) how this effect varies with consumer characteristics, and (3) the conditional existence of synergy between online ads and offline ads. In addition, we outline a ready-to-implement decision support system for advertisers to run and monitor campaigns, including specific procedures to estimate conversion rate uplift, conduct segmentation, and determine ad frequency.

## 2. Relevant literature and research gaps

## 2.1. Methods for evaluating ad treatment effects

Campaign effectiveness can be assessed based on randomized experiment or observational data. Existing experimental studies have rarely examined the effects of multimedia ad treatments because they are difficult or costly to conduct in the context of complex campaigns across various media outlets. One exception is [19] which tested catalog and email ads with 300 regular customers of a specialty retailer. When the ad treatments involve multiple dimensions and each treatment dimension is not binary, it is challenging to test all possible treatment variations. Consider a case where a firm needs to decide the optimal ad frequency across a number of media outlets – while it is easy to assign individuals to see or not to see the ad, it is intricate to form randomized treatment groups for N ad impressions (e.g., if $N = 1 0$ ad exposures are to be tested in each of 4 media outlets, it would require $N ^ { 4 } { = } 1 0 { , } 0 0 0$ treatment groups). Even if perfect randomization can be achieved, such large-scale randomized experiments may adversely affect firm revenue or consumer experience, and thus firms are often unwilling to experi ment with their own customers.

Table 1  
Advantages of The Tree-Structured Model.

<table><tr><td colspan="2">Advantages of The Tree-Structured Model.</td></tr><tr><td>Automatic correction of selection bias</td><td>The model automatically identifies confounders and corrects for selection bias in the process of tree splitting.</td></tr><tr><td>Automatic identification of key observables</td><td>Out of numerous observables in the context of big data, the model automatically identifies the key variables that firms should pay attention to when allocating ad resources and segmenting consumers.</td></tr><tr><td>Automatic consumer segmentation</td><td>The method automatically identifies the most meaningful ways of segmentation in a data-driven and non-arbitrary manner, and thus helps improve targeted advertising decisions.</td></tr><tr><td>Ability to evaluate complex multi-dimensional ad treatments</td><td>The model can correct for selection bias when estimating the effect of general ad treatments, which can be single- or multi-dimensional. It is thus suitable to evaluate multimedia campaigns with multiple treatment dimensions (media platforms).</td></tr><tr><td>Minimal manual tuning</td><td>The tree-structured model automatically determines important tuning parameters via a nonparametric approach, which avoids selecting parametric models arbitrarily. Hence, the approach is highly flexible, requiring minimal manual tuning. Moreover, it grows and truncates the tree to minimize out-of-sample error (via cross-validation) rather than in-sample error, preventing the over-fitting of the trees and facilitating the interpretation of the results.</td></tr><tr><td>Ability to identify optimal ad treatments</td><td>The method can effectively identify complicated nonlinear relationships and thus help determine the optimal level of treatment that maximizes conversion.</td></tr></table>

One may also estimate the uplift effect of ad treatments compared to a baseline with observational data. Most uplift models focus on binary treatment [10,11] and are not suitable for multi-channel multi-exposure campaigns. Although certain multi-treatment models were proposed recently [20]. they do not inherently account for selection bias. A set of main ideas and representative works are as follows. [21] proposed the separate model approach (i.e., fitting separate models for each treat ment group). [22] proposed metalearners to estimate heterogeneous binary treatment effects using machine learning, and [13] extended it to multiple treatments. [23] constructed trees to maximize expected response value, while [12] used trees to maximize outcome heteroge neity from pairwise treatment comparisons. These approaches focus on heterogeneity in treatment effect and need extra propensity model to address selection bias if any. [24] proposed regression adjustment, which assumes parametric models and hence is not flexible enough in the presence of many covariates (e.g., user features). Other related models include reinforcement learning to improve campaign strategy [25] and dynamic optimization of ad content [26], which focus on onthe-fly campaign improvement rather than ad effectiveness assess ment. In comparison, we adopt causal forest to build the framework to assess multi-channel multi-exposure campaigns, as it is flexible (nonparametric), can work on multiple treatments, and automatically correct for selection bias.

## 2.2. Literature on multimedia campaigns with online and offline ads

A few recent studies have explored the effect of multimedia ads that combine online and offline ads [4,27,28,29,1,18]. However, they have four major limitations. First, limited efforts were made to address the confounding effects of consumer characteristics. In fact, except for [4], prior studies have largely ignored consumer heterogeneity or treated it as unobservable. Such practices limited their ability to address selection bias. Relatedly, without modeling consumer heterogeneity, the litera ture offers limited insights into consumer segmentation for multimedia ads or how the effects of multimedia ads vary across consumer groups. Second, there are mixed findings on the effectiveness of multimedia ads. Some argue that various media platforms work better in combination because of their complementary benefits [29], while others suggest an adverse effect because they lead to greater reactance of the customers, who are forced to manage a variety of annoyances and may be under the impression that the company is making excessive efforts to pressure them to adopt a not-so-good product [30]. Third, most prior studies have employed aggregate market-level data [28,1,2]. They only provide macro-level findings and cannot reveal the incremental impact of each ad impression. Fourth, there is a lack of a model for firms to identify the optimal level of ad repetition in the multimedia setting. Our study fills in these important research gaps.

## 2.3. Literature on repeated ad exposures

Consumer research theory predicts that, although consumer atten tion may increase (or wear in) initially in a series of repeated ad expo sures, beyond some point it could start to decline (or wear out) because of satiation, boredom, irritation, or mental tune-out [31]. Previous studies on repeated ad exposures are largely based on lab experiments in which participants are forced to view an assigned number of ads [32,33,34,35]. Such forced viewing situation may bias the level of consumer attention and involvement; and cannot perfectly mimic the real-life ad viewing situations. Moreover, it is unclear at what point the effect starts to wear out: some research shows a decline of purchase intentions after 3 ad exposures in the laboratory setting, while others do not find the turning point until after 10 exposures [31,35]. The incon sistent findings in the literature imply that the effect may be conditional on some unmodeled factors and deserve further research.

Hence, we adopt causal forest, a flexible nonparametric method that allows a closer and more accurate examination of the intricacies regarding the nonlinear impact of ad repetition. It is also the first to show the nonlinear effect of ad exposures in the multimedia context. This is nontrivial because, due to possible complementary or substitut ing effects between media platforms, there could be a shift in the number of optimal ad exposures for each media platform when it is used in combination with versus in isolation of other media platforms. The ex istence / amount of such shift is nonobvious and prior research has not modeled it.

## 3. Treatment effect of repeated ad exposures in multiple media outlets

## 3.1. Method

Tree-based methods for causal inference have been applied in various contexts. For example, [11] employed causal conditional infer ence trees to select the targets for cross-selling insurance products. [36,37] prove the consistency of the honest tree method and extend it to causal forest. [10,20] compare the effectiveness of various models (including causal forest) for binary and multiple treatments, respec tively, in the context of coupon campaigns. In this paper, we apply the causal forest method to examine the nonlinear impact of ad repetition in the multimedia context. Advertisers can apply the method outlined in this section to iteratively optimize ad frequency for complicated multi

dimensional campaigns.

Following [36,37], causal forest is a model that combines propensitybased statistical modeling with tree-based machine learning. It is an efficient (i.e., capable of handling various types of treatments and multidimensional treatments), non-restrictive $( \mathrm { i . e . , }$ non-parametric), and automated model for identification of key variables, correction of se lection bias, and data-driven consumer segmentation. Because of its flexibility, the model is particularly suitable to examine the nonlinear impact of ad repetition. The intuition behind the model is to use a tree structure to automatically divide the population into non-adjacent seg ments and then measure ad effectiveness within each segment. The segmentation is done in a way that consumers within each segment are homogeneous in their propensity to receive potential ad treatments; hence the ad effectiveness estimated within each segment is not subject to treatment selection bias [7].

We follow the propensity trees procedure as in [37]. We use z to represent an ad treatment; $\mathbf { z } \in \phi ,$ with Φ being the set of all potential treatment values. For example, for binary/univariate treatments, $\varPhi =$ {0,1} with 1 indicating ad exposure and 0 indicating no ad exposure; for complex ad treatments, z may be continuous or multi-dimensional. The treatment for a specific consumer is a random variable $\mathbf { Z } ,$ supported on Φ. We define $Y ( \mathbf { z } )$ as the outcome (e.g., conversion) of a treatment $\mathbf { z } ,$ and the set of all potential outcomes as $T .$ In observational data, for each individual consumer $i ( i = 1 , 2 , . . . , N )$ with ad treatments $\mathbf { Z } _ { i } ,$ there exist an outcome variable $Y _ { i }$ and a vector of other relevant covariates $( \mathbf { e . g . }$ consumer characteristics) $\mathbf { X } _ { i }$ of length $p .$ To correct for selection bias when estimating the effect of ad treatment z on the outcome ${ \cal Y } ,$ it requires the elimination of the effects of confounding factors in the co variate vector $\mathbf { { x } } ;$ that is, we are interested in the population average under each $\begin{array} { r } { \mathbf { z } \in \Phi , p ( Y ( \mathbf { z } ) ) = \int _ { X } p ( Y ( \mathbf { z } ) | \mathbf { X } ) p ( \mathbf { X } ) d \mathbf { X } . } \end{array}$ . Under the standard unconfoundedness assumption in causal inference models [38], condi tioning on observed covariates $\mathbf { X } ,$ we have $p ( Y ( \mathbf { z } ) | \mathbf { Z } = \mathbf { z } , \mathbf { X } ) \ = p ( \mathbf { Z } =$ $\mathbf { z } | Y ( \mathbf { z } ) , \mathbf { X } ) p ( Y ( \mathbf { z } ) | \mathbf { X } ) / p ( \mathbf { Z } = \mathbf { z } | \mathbf { X } ) = p ( Y ( \mathbf { z } ) | \mathbf { X } )$ . Thus,

$$
p (Y (\mathbf {z})) = \int_ {\mathbf {X}} p (Y (\mathbf {z}) | \mathbf {Z} = \mathbf {z}, \mathbf {X}) p (\mathbf {X}) \mathrm{d} \mathbf {X}.\tag{1}
$$

To cope with the issue posed by high-dimensional $\mathbf { X } ,$ we define the propensity function $e ( \mathbf { X } ) = p ( \mathbf { Z } | \mathbf { X } ) .$ , i.e., the density of the treatment conditional on the given covariates, and $p ( { \pmb Y } ( { \pmb z } ) )$ in Eq. (1) becomes

$$
p (Y (\mathbf {z})) = \int_ {e (\mathbf {X})} p (Y (\mathbf {z}) | \mathbf {Z} = \mathbf {z}, e (\mathbf {X})) p (e (\mathbf {X})) d e (\mathbf {X}).\tag{2}
$$

After estimating $e ( \mathbf { X } )$ , we can categorize the subjects with similar $e ( \mathbf { X } )$ values, estimate the success rate for each sub-group, and average the estimates across the sub-groups to obtain unbiased estimation of the population success rate.

A traditional method to categorize subjects with similar $e ( \mathbf { X } )$ values is propensity score matching $[ 7 , 8 ] _ { : }$ , where one obtains $e ( \mathbf { X } )$ first and then groups subjects with similar fitted $e ( \mathbf { X } )$ . Based on similar idea, the tree model [37] can estimate the propensity function ${ \bf \nabla } : ( { \bf X } )$ nonparametrically and categorize the subjects simultaneously. Specifically, we build a tree to model $p ( \mathbf { Z } | \mathbf { X } )$ , treating X as the independent variables and Z as the dependent variable. As the tree splits, the homogeneity in treatment assignment within each sub-group (or leaf node of the tree) increases. A tree structure is a set of rules which recursively partition the predictor space into disjoint sets. It 1) starts at the root node that contains all individual subiects: 2) searches all the consumer features and all possible splitting points of each feature, and selects the splitting feature and splitting point that minimize the node impurities in the two child nodes; 3) if reaching a stopping criterion, exits; 4) otherwise, applies step 2 to each child node. We select splitting features and points based on the reduction in the sum of squared errors using Classification And Regression Tree (CART), a popular approach in machine learning [39]. Appendix A explains the procedure and advantages of CART, and its suitability for our method. The model automatically categorizes the subjects and determines the number of sub-groups, thus avoiding parametric specification of e(X) or arbitrary choice of the number of sub groups.

The propensity tree method automatically splits a node if the treat ment assignment within this node is confounded, and will stop splitting otherwise. Hence, when a tree finishes splitting, within each end node, the selection bias among users is mitigated. The success rate is estimated within each node, and hence each end node can be considered as a unique consumer segment for the ad campaign with heterogeneous ad effects. The method thus enables automatic data-driven segmentation of consumers by selecting the most relevant consumer features (out of numerous variables observable) as the segmentation criteria.

Table A1 in Appendix A summarizes the algorithm. To prevent oversplitting, we utilize 10-fold cross-validation (which minimizes out-ofthe-sample error) to find the best depth of the tree. After the tree is constructed and the ad effectiveness $R _ { s } ( \mathbf { z } )$ is estimated within each sub group s for treatment z, the estimated population-level conversion rate under each ad treatment z is computed as

$$
\widehat {\mathrm{CVR}} (\mathbf {z}) = \sum_ {s} \frac {N _ {s}}{N} R _ {s} (\mathbf {z}).\tag{3}
$$

Choosing a treatment z as the baseline, the average treatment effect ATE <sup>̂</sup> of treatment z is calculated as

$$
\widehat {\mathrm{ATE}} (\mathbf {z}) = \widehat {\mathrm{CVR}} (\mathbf {z}) - \widehat {\mathrm{CVR}} (\mathbf {z} _ {0})\tag{4}
$$

In summary, the propensity tree procedure fully automates the estimation process and corrects for selection bias in a way that is nonparametric and flexible. It automatically categorizes the subjects into sub-groups (tree leaf nodes) in a way that the distribution of ad treat ment is homogeneous within each sub-group. In this process, the pro pensity function is derived, and data-driven consumer segmentation is achieved. The ad treatments are independent of consumer characteris tics, conditioned on the propensity function; thus, within each subgroup, the estimated effect of the treatment on the outcome is clean / not subject to selection bias. We then compute the unbiased populationlevel effect of the treatment using the weighted average of the estimators of the leaf nodes with Eq. (3).

As suggested in [37], we use bootstrap samples to construct a bag of trees (i.e., a random forest), and report the average estimation across the bootstrap samples. Specifically, we obtain 100 bootstrap samples; in each bootstrap sample, we draw 50 % of the dataset without replace ment and estimate the conversion rates under each ad treatment, using the tree algorithm. We then obtain the average of the estimated con version rates across bootstrap samples as the population-level estima tion, and the standard deviation of the results from bootstrap samples provides the standard error of the estimation. Fig. 1 visualizes the causal forest procedure.

## 3.2. Data

We analyze a large-scale dataset from a leading web portal in the U.S. about a real-world multimedia campaign. The web portal provides both content and advertising services covering desktop and mobile devices and connected TV channels. The focal campaign was a 30-day flash campaign including both online display ads and TV ads<sup>1</sup> for a major auto insurance company. It is non-targeted and the assignment of TV ads was unrelated to that of online ads, and vice versa. The auto insurance industry is a significant economic sector in the U.S., yielding over \$350 billion revenue in 2023.<sup>2</sup> Average spending on auto insurance per con sumer in the U.S. tops over \$1500/year.<sup>3</sup>

The dataset includes around 7 million individual consumers. For each consumer i, we count the number of ad exposures in the online and connected TV channels during the campaign.<sup>4</sup> The ad exposure fre quencies of the two channels construct the 2-dimensional treatment vecto $\mathbf { \nabla } \cdot \mathbf { Z } _ { i \cdot }$ Over time, the web portal continuously adds new variables and stops collecting data on certain variables, resulting in a large database with around two million variables on user features, many of which are sparse. After removing those with a large portion of missing values regarding the consumers of the focal campaign, we focus on a final set of 4093 variables including demographics, engagement in each retail category, personal interests, online activities, TV viewing activities, etc., and construct the feature vector $\mathbf { X } _ { i \cdot }$ (See Appendix B for examples and summary statistics). The outcome variable (conversions) $Y _ { i }$ is defined based on online requests for quotes of the insurance product, with 1 indicating a quote request made and 0 otherwise. Note that, different firms may have collected different types of consumer characteristics, which may or may not be as comprehensive as the list we have. How ever, the tree model can automatically select the most relevant variables out of all variables available to determine the appropriate tree-structure, and reduces selection bias to the greatest extent permitted by the data.

## 3.3. Results

We repeatedly draw 50 % of the data without replacement; after growing the tree (i.e., obtaining e(X) by fitting the treatment vector Z with the covariates X in the tree model) with the sub-dataset, we esti mate the conversion rate within the leaves $R _ { s } ( \mathbf { z } )$ and the overall esti mation of the causal effect of repeated ads $\widehat { \mathrm { A T E } } ( \mathbf { z } )$ as described in Section 3.1. Since a relatively small portion of consumers were exposed to 6 or more ads in each media outlet and the frequency becomes extremely scarce above 15, we group the number of exposures into eight buckets, 0, 1, 2, 3, 4, 5, 6–10, and 11–15, for both online and TV ads. Hence, there are 64 (8 × 8) combinations of TV and online ad exposure buckets, i.e., 64 treatments. Within each leaf node, we compute the conversion rate under each of the 64 buckets, and then estimate $\widehat { \mathrm { C V R } } ( \mathbf { z } )$ and $\widehat { \mathrm { A T E } } ( \mathbf { z } )$ with Eqs. (3) and (4). We repeat the procedure 100 times and hence construct a bag of trees (i.e., a random forest), and report the average estimation across the bootstrap samples.

To facilitate interpretation, we visualize the estimated conversion rate for each bucket in a heatmap (Fig. 2.1), the darker the higher conversion rate. The darkest cell, which represents the highest conver sion rate, corresponds to 6–10 TV ad exposures and 5 online ad exposures.

For simplicity, we use C(m, l) to denote each cell in the plot, where m $= 0 , 1 , . . . , 1 1 . . 1 5$ number of TV ads and $l = 0 , 1 , . . . , 1 1 . . 1 5$ number of online display ads. Hence, the cell with the highest conversion rate is C (6–10, 5). This finding provides evidence for the wear-in effect of repeated ads that a moderate level of ad repetition increases conversion. All other treatments and no treatment (C(0,0)) lead to a lower conver sion rate. For instance, although C(11–15, 11–15) would cost the firm more, it yields a lower conversion rate, likely due to irritation, annoyance, or boredom effects of too many repeated ad exposures as theorized in prior psychological research [31,33]. In Appendix C, we report the estimated conversion rates in Table C1, and the effect of each treatment compared to no treatment C(0, 0) in Table C2.

![](/api/attachments/SA4CFHR8/fulltext/images/864e4c59374384ce91d29436135d8288ea82f69e3c8a8aa35708e200bac5b5ca.jpg)

![](/api/attachments/SA4CFHR8/fulltext/images/f2ebc859b61c1c86b6fc4b4156f3709d37113bb57298224a51f490ae7b68cfcd.jpg)  
Fig. 1. Causal Forest Procedure.

![](/api/attachments/SA4CFHR8/fulltext/images/c2626f05b42841dd23177ba07442b933709acf97d95a03d704e49b6e2dbec8a9.jpg)  
Fig. 2. Estimated Effect of the Entire Population.  
Note: Darker colors represent higher conversion rates, and the darkest color in each heat map corresponds to the highest conversion rate.

## 4. Heterogeneous effects across consumer groups

A byproduct of the tree algorithm is that, it automatically splits the population into multiple segments, which are defined by the user characteristics used when splitting the tree. In other words. the tree algorithm provides an automatic consumer segmentation, and each leaf is a group of consumers sharing certain characteristics in common. Within a group, the consumers are homogeneous in terms of the pro pensity to be exposed to ads, and hence their conversion rate under various ad treatments can be estimated without selection bias. Across the groups, they exhibit different conversion rates. Thus, the model provides insights into how various consumer groups react differently to ad exposures in the two advertising channels.

We run the propensity tree algorithm (i.e., fit the treatment with user characteristics [37]) on the full dataset. Fig. 3 shows the fitted tree. Out of all consumer features in the data, the model automatically selected six “splitting features” with the strongest signal to determine the tree structure, namely, online activeness, frequency of watching TV talk shows, interests in automobile and real estate, age, and gender. The tree has nine end leaf nodes (Nodes 1–9). To help interpret the nodes, we use gray scale bars to indicate the consumer features corresponding to each node. For example, Nodes 8 and 9 consist of consumers who have the highest level of online activity; however, consumers in Node 8 are fe male while those in Node 9 are male.

For each leaf node, we visualize the estimated conversion rates in

![](/api/attachments/SA4CFHR8/fulltext/images/7cce7925cfc6a2ae63c829dbc3b4a320bc38ebe7054b6f00ed5bf7f6dcf5d3f0.jpg)  
Fig. 3. Consumer Segmentation – Fitted Tree.  
Note: the relative size of each node is in parentheses. The gray-scale bars describe the consumer features in relevant nodes. For example, node #7 includes consumers who are (1) interested in real estate, (2) young, and (3) in the third highest tier in terms of online activeness.

Fig. 4.1–4.9. Comparing the conversion rate heatmap across the leaf nodes, the result suggests that the effects of repeated ad exposures vary across consumer groups. For example, Node 5 differs from Nodes 6–7 only in terms of consumer age (consumers in Node 5 are older). We observe that, it requires a larger number of TV and online ad exposures to maximize conversions for younger consumers than older ones (highest conversions at C(5, 5) and C(11–15, 11–15) for Node 6 and 7, respectively; versus C(3, 4) for Node 5). When comparing Nodes 8 and 9 (which differ only in terms of gender), we find that it takes less ad repetition to maximize the conversions of females (highest conversion at C(4, 2) for Node 8, Fig. 4.8) than males (highest conversion at C(5, 4) for Node 9, Fig. 4.9). These findings suggest that the effect of repeated ads can depend on consumer age and gender. We speculate that some cognitive or behavioral theories may help explain such observations. For example, females and males may rely on different external cues when purchasing an auto insurance product, because of their differences in the key benefits sought and personal interest / knowledge about the prod. uct. On the other hand, younger ad viewers tend to have more diffuse attention spread [16] and thus may only start to seriously consider an ad after many repeated exposures. Although we do not intend to test the underlying theories, future research can further examine how these demographic factors influence the effects of ad repetition, which has rarely been studied in the literature.

Big data analysis often generates unique insights that are difficult to directly predict based on theories [40]. Based on our results, a key variable for the focal advertiser to consider when segmenting the con sumers is the frequency of watching talk shows. This is because, comparing Node 1 (Fig. 4.1) versus Nodes 2 and 3 (Fig. 4.2 and 4.3), we observe that the TV and online ads required to maximize conversions vary as people’s frequency of watching talk shows varies. The finding indicates that the advertiser should use different levels of ad repetition when targeting on consumer groups that differ in how often they watch talk shows. While it is beyond the scope of this paper to investigate the theoretical mechanism behind this observation, we speculate that talk show-watching frequency may be a powerful indicator of some latent viewer features that are highly related to the receptivity of the ad campaign (e.g., certain types of personality, lifestyle, taste, cognitive or emotional states), hence serving as an informative factor to segment consumers for the advertiser. This result suggests the usefulness of the method proposed, because traditional theory-driven segmentation ap proaches would likely omit such segmentation criteria that do not make immediate theoretical sense. In sum, this example shows that the treebased model can help firms identify important segmentation criteria based on their own data and customize campaign strategies when tar geting on different segments.

## 5. Discussion: key findings and takeaways

## 5.1. Importance of correcting for selection bias

Our estimations of the ad effect within each leaf node (Fig. 4.1–4.9) are not subject to selection bias, because the consumers within each leaf node are homogenous in terms of the propensity for ad treatments (because, after accounting for the splitting features, any remaining dif ferences across the individuals are independent of the ad treatments). Most of these unbiased segment-specific estimates (except Nodes 2 and 7) are drastically different from the naive estimates in Fig. 2.2 (i.e., the averaged outcome corresponding to each treatment without correcting the selection bias or accounting for the confounders) which indicate higher conversion rate as both online and TV ad exposures increase, with the highest conversion at C(11–15, 11–15). In other words, the conclusion based on the naive estimate is biased for seven out of nine segments. The naive estimate is also different from the population-level effect estimated after correcting for selection bias. As shown in Fig. 2.1, the population-wide optimal ad treatment is C(6–10, 5) instead of C (11–15, 11–15) as suggested by the naive estimate. Managerial decisions based on naive estimates not only lead to a waste of resources, but also cause suboptimal conversion. Complementing prior research in the DSS literature [7], our results offer new evidence for the necessity of addressing selection bias in the context of evaluating multimedia ad effectiveness.

![](/api/attachments/SA4CFHR8/fulltext/images/39bad1de1ccbf402e9d342f40a68d30017120dafe693c701456a620288dffd3c.jpg)

![](/api/attachments/SA4CFHR8/fulltext/images/8bbee6744878630df254fb16f78e11c8afee772a7518a7b59cf54476ba4def1d.jpg)  
Color Key nd Histog node #4 (consumers w/ medium low online activity) Value

Color Key and Histogr node #1 (consumers w/ low talk show & low online activity) 0.001 0.004 0.007 Value  
![](/api/attachments/SA4CFHR8/fulltext/images/4094331ff84cb33a5c1f8c31a459e13356f0b9781bda5694fe84c9ca37aea2ff.jpg)

![](/api/attachments/SA4CFHR8/fulltext/images/5eec0ad4a57868a83a4dfe3493cc4c8b3a74d1ef25d2f16f16d5d009befeca14.jpg)  
node #2 (consumers w/ low interest in automobile, high talk show & low online activity)

![](/api/attachments/SA4CFHR8/fulltext/images/d860f4fc8c2ec9adbec143188ab9a7af4edb615a038b00e0dd0f033f87e59322.jpg)  
node #5 (segment w/ high age & medium high online activity)

node #3 (consumers w/ high interest in automobile, high talk show & low online activity)  
![](/api/attachments/SA4CFHR8/fulltext/images/6fd03f3e7ab974bf2af5075b961caa57558c48a47dc69a18c629d65aa5b8af57.jpg)

Color Key and Histogra node #6 (segment w/ low interest in real estate & low age & Value medium high online activity  
![](/api/attachments/SA4CFHR8/fulltext/images/028ed81c424e866c6953dee2e28031fd6c2fb1fcd406508bb7f797dc37464946.jpg)

![](/api/attachments/SA4CFHR8/fulltext/images/dc1157782d91ee47667c13c7fd8c1ff98fcbe3b5e3b862a2578d39f2844c99a1.jpg)  
Fig. 4. Estimated Effect in Each Consumer Segment.  
Note: Darker colors represent higher conversion rates, and the darkest color in each heat map corresponds to the highest conversion rate.

## 5.2. Nonlinear effect of repeated ad exposures

As seen in Fig. 4, in all consumer segments (except Nodes 2 and 7) and at the overall population level (Fig. 2.1), the maximal conversion occurs under moderate (rather than the highest) numbers of TV / online ad exposures. For example, in Fig. 2.1, conversions peak at C(6–10, 5). Also note that, within each column of Fig. 2.1 (fixing the number of TV ad exposures), the effect of online ad exposures is different. For instance, when TV ad is absent (first column in Fig. 2.1), we do not observe wearout effect of repeated online ad exposures; when the number of TV ad exposures is 6–10, the effect of online ads starts to wear out after 5 ex posures. Moreover, in some cases, the nonlinear effect does not follow an inverse U-shape and has multiple sub-peaks; hence, the effect may be more complicated than previously theorized in the literature and a parametric model with quadratic term is likely to be misspecified. Adding to the DSS literature on optimal ad frequency [41], our study indicates the necessity and importance of adopting a nonparametric model like ours to evaluate the effect of repeated ads in practice.

## 5.3. Comparing the effects of repeated ad exposures across consumer segments

Different consumer groups have unequal levels of attention span, annoyance tolerance, and other cognitive, psychological and behavioral characteristics that influence how they react to ads [16]. Hence, theo retically, the effect of repeated ad exposures may differ across consumer segments. As targeted campaigns become prevalent, firms need to effectively segment their audience (e.g., what consumer characteristics are most relevant for segmentation? What is the optimal ad repetition for each segment?). Extant research offers little guidance on how to do so. Our novel insights derived from big field data (Section 4) add to the DSS literature on the heterogeneous effects among consumer groups [11,15] and campaign segmentation strategy [14]. For example, it re quires a larger number of TV and online ad exposures to maximize conversions for younger consumers than older ones, and it takes less ad repetition to maximize the conversions of females. The effect also differs as people’s frequency of watching talk shows varies. Although we speculated some possible reasons for these observations, such unique findings derived from big data-mining suggest future research oppor tunities to systematically investigate the underlying theoretical mechanisms.

Note that the above results do not suggest causal effects of these user characteristics on conversion rates. Rather, it describes how the effec tiveness of repeated ads varies conditional on these consumer charac teristics. Although we caution against naïve generalization of our results based on the auto insurance campaign, the findings provide insight regarding how to segment consumers and assign differential treatments across these consumer groups when an advertiser runs similar cam paigns in the future. Also importantly, as many companies are collecting big (and bigger) data on their own consumers. we demonstrate how the tree-based model can help effectively identify distinct segmentation criteria and develop customized segmentation strategies for their own campaigns based on their own data. In Fig. 5, we propose a decision system for advertisers to optimize multimedia campaign effectiveness across consumer segments.

Specifically, we suggest that advertisers run ad campaigns with iterative updates. In each iteration, the advertiser should collect data on users’ ad exposures and conversions, and run two models: 1) using causal forest (as illustrated in Section 3.1) to identify the optimal ad exposure frequency for the general population of the campaign, and set the campaign’s general ad frequency cap no higher than the optimal exposure frequency; and 2) using a single propensity tree to group consumers according to the propensity to ad exposures, estimating the treatment effect of various ad exposure frequencies for each consumer segment, in order to optimize the ad exposure frequency cap for each consumer segment. With the results of the two models, the advertiser can update the setting of their ad campaign, and then start the next iteration. The advertiser can also use the updated setting to jump-start other similar ad campaigns.

It is common that the optimal ad exposure frequency cap for a con sumer segment is different from the general optimal ad exposure fre quency cap. We suggest that advertisers apply the segment-specific optimal ad exposure frequency cap for users with relevant characteris tics identified; the general ad exposure frequency cap can be applied to users whose characteristics are not identified or difficult to identify, such as new users or users who disabled online tracking.

## 5.4. Evidence on contingent multimedia synergy

Prior research has not reached an agreement on the existence of multimedia synergy [4,29,30,1]. Our findings help elucidate the con flicting literature by showing that multimedia synergy is conditional. For all segments except Node 3, the highest conversion is achieved when combining online ads and TV ads, instead of using ads on one single media outlet alone (i.e., using online ads only or TV ads only). Hence, we observe multimedia synergy in these segments, i.e., the online and TV platforms can complement each other in enhancing the effectiveness of the campaign. As a contrary, in Node 3, the highest conversion occurs at C(0, 6–10) when the consumers are exposed to online ads only and no TV ads. Hence, for this segment, multimedia advertising results in lower conversions than single-media advertising. Node 3 is directly compa rable to Node 2, because consumers in these two nodes differ only in terms of their interest in automobile. In Node 2, the outcome is maxi mized at C(11–15, 11–15), where consumers are exposed to both online and TV ads. This difference between Nodes 2 and 3 indicates that multimedia synergy may not always exist and is conditional on certain features of the consumers.<sup>5</sup>

The focal product advertised, auto insurance, is likely to be of higher personal relevance to people who are interested in automobile (Node 3) than those who are not (Node 2). Personal relevance can affect con sumers’ attitude toward advertising [42]. First, when an ad is personally relevant to the viewer, s/he could pay greater attention to it and is more willing to process ad information. Under this theory, for people in Node 3, the advertiser does not need to use extensive advertising via multiple media outlets to grab their attention. However, this theory can only predict zero marginal effect of excessive multimedia ads, but cannot explain their adverse effect (i.e., worse than single-media ad for Node 3). We thus refer to a second theory. Specifically, for a more personally relevant decision, people tend to critically scrutinize the product and develop reactance to unsolicited external attempts to influence their behavior. Hence, compared to Node 2, individuals in Node 3 are more likely to perceive the company’s use of multiple media outlets as an extravagant attempt to manipulate them or control/mislead their de cisions. They thus have a greater tendency to view multimedia ads as multiple sources of annoyance and irritation, and develop higher resis tance. In sum, our finding suggests that multimedia synergy is unlikely when personal relevance is high.

## 6. Conclusion

Using tree-based models, we analyze a large-scale micro-level data set from an important economic sector, and find heterogeneous effects of multi-dimensional ad treatments across consumer segments. This study contributes to the literature on several major technical and substantive fronts. First, we empirically demonstrate the importance of correcting for selection bias and segmenting consumers when measuring the effectiveness of multimedia ad campaigns. Ignorance of selection bias and heterogeneity across consumer segments can result in suboptimal conversions and waste of advertising resources. Second, our findings reveal complex nonlinear effect of repeated ads and facilitate the iden tification of optimal ad exposures. Notably, the nonlinear effect may not be simply quadratic, and can be influenced by consumer characteristics including age and gender. Third, we show how the effectiveness of ad via one media outlet can be altered in the presence of ad via another media outlet. Importantly, synergy across online and offline media outlets does not occur for all consumer segments, and is conditional on factors such as personal relevance.

Managers often doubt whether online ads actually increase conver sions [8,1]. For example, General Motors publicly questioned the effect of online advertising and halted its \$10 million ad budget on Facebook [43]. The evaluation of online ad effectiveness is further complicated in multimedia campaigns, i.e., when ads are concurrently launched in other media outlets. Because experiments are often costly or difficult to examine complex multimedia ad treatments, practitioners (e.g., adver tisers, advertising agents, and publishers) desire a suitable analysis framework using observational data [20]. We demonstrate the useful ness of the tree-based model in generating novel empirical insights omitted by traditional parametric method and thus improving mana gerial decisions on ad repetition frequency and consumer segmentation.

Evidently, the influence of multimedia ad treatments is complicated because of the heterogeneous, nonlinear effects of repeated ad exposures and contingent existence of multimedia synergy. Such complications raise challenges for managers to optimally allocate advertising resources [20,1]. Our findings based on real-world data can directly be used to guide similar types of ad campaigns in the future. As one of the biggest economic sectors, the global market value of insurance industry is larger than the entire GDP of most countries (e.g., Germany, Japan and U.K.) except for U.S. and China.<sup>6</sup> For firms in unrelated industry settings, we clearly demonstrate how they can leverage the outlined approach to analyze their own ad campaigns and identify the areas of focus in the analysis.

In the era of big data, firms (especially web portals and online re tailers) often track many consumer features thanks to the rapid devel opment in information technology and increasing affordability of data storage. For example, YouTube and Facebook maintain records of tens of thousands of different metrics on their users [44], while Macy’s has built up a gigantic database including detailed profiles that enable 360-de gree views of its customers [5]. According to a McKinsey report, in almost all industries in the U.S., each company with over 1000 em ployees has already stored hundreds of terabytes of consumer data on average.<sup>7</sup> It is thus imperative to prevent firms from drowning in data [6]. We suggest that they incorporate the procedure described in this paper into their business information systems because it is easy to implement, able to cope with the high velocity of big data by auto matically analyzing it without requiring human tuning or judgment, and efficient in selecting the most informative variables available in a firm’s database to segment the consumers. Beyond advertising, researchers in other areas can also adopt the approach to assess the effect of multi dimensional treatments.

![](/api/attachments/SA4CFHR8/fulltext/images/9d28e451165bd0a606231cbe960dab1e5bb83b81f0d37d46bae6dcfcec9cb120.jpg)  
Fig. 5. Suggested Procedure to Optimize Multimedia Campaign Effectiveness.

Our approach is not without limitations. First, it controls for selec tion bias represented by the observed covariates only. However, this limitation is mitigated in big data settings where companies collect data on a large number of consumer features. That said, if there are still unobserved factors expected to significantly determine consumer be haviors, selection bias/endogeneity may still exist. The methods to address endogeneity include instrument variable (IV) [45], control function (CF) [46], latent instrumental variable (LIV) [47] and copula [48]. However, both the IV and CF methods require manual selection of valid exogenous variables to instrument the endogenous treatment, which is infeasible in our case. While the LIV and copula methods do not require additional instrument variables. they cater to continuous outcome variables and thus are not suited to our context either. Hence, to achieve accurate estimation and improved campaign decision mak ing, we recommend advertisers to collect sufficient data on relevant consumer features, which is increasingly feasible given the advance ments in technologies for data storage, processing and computation. Future research can explore alternative approaches to address endoge neity, especially in the context of complex treatments, discrete out comes, or absence of valid instrumental variables. Another limitation of a tree-based model is that it only ingests tabular / numerical data. If industry practitioners need to use unstructured data (e.g., graphs or texts), they should embed it in a vector before feeding into a tree model. Finally, compared to conventional linear models, tree models require more computing power, which, however, is increasingly affordable and accessible for many companies [10,20,6].

## Funding source and acknowledgement

The first author thanks the support of Terry-Sanford Research Award from the Terry College of Business at the University of Georgia. This funding source provides summer stipend to the first author. It was not involved in the study or the writing of this manuscript.

## CRediT authorship contribution statement

Pengyuan Wang: Writing – review & editing, Writing – original draft, Visualization, Validation, Supervision, Software, Resources, Project administration, Methodology, Investigation, Funding acquisi tion, Formal analysis, Data curation, Conceptualization. Guiyang Xiong: Writing – review & editing, Writing – original draft, Visualiza tion, Validation, Supervision, Software, Resources, Project administra tion, Methodology, Investigation, Funding acquisition, Formal analysis, Data curation, Conceptualization. Will Wei Sun: Writing – review & editing, Writing – original draft, Visualization, Validation, Software, Methodology, Investigation, Funding acquisition, Formal analysis, Data curation, Conceptualization. Jian Yang: Resources, Data curation.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

The data that has been used is confidential.

## Acknowledgements

The first author thanks the support of Terry-Sanford Research Award from the Terry College of Business at the University of Georgia, 2022 to 2023.

## Appendix A. The tree-based algorithm

The key to rule out selection bias is to ensure that the distribution of treatments across users is homogeneous, i.e., the treatment assigned to each user is not influenced by user features [49,38]. The propensity tree method described below is able to automatically achieve this goal within each end leaf node [37]. We follow the CART guideline when fitting the propensity tree (i.e., fit the treatment with user characteristics). At each step of splitting, it scans through all covariates / consumer features available in the database and all possible splitting points of each feature. For each splitting point of each feature, it computes the reduction in in Gini impurity (for categorical responses) or sum of squared errors (or SSE, for continuous responses), and selects the covariate and splitting point that reduces Gini impurity or SSE to the largest extent. In our application, the treatment is a 2-dimensional vector, representing ad exposure frequencies of the TV and online channels, and we add up the SSE of each dimension to get the total SSE. Conceptually, the tree can keep splitting infinitely. If the tree is so deep that each leaf node has one user. the final SSE is guaranteed to be 0. However. over-splitting can lead to model overfitting and large out-of-sample errors. Hence, we constrain the sizes of the leaf nodes employing tuning pa rameters based on 10-fold cross-validation. Specifically, we split the dataset randomly into 10 subsets. For each subset, we take it as a holdout set, use the remaining sets as a training set, fit the model on the training set and evaluate it on the holdout set with various leaf node size, and pick the bes parameters. With a grid search, we set the minimal leaf size to be $_ { 1 0 0 , 0 0 0 . } ^ { 8 }$ Considering the large size of the dataset (around 7 million users) and the small magnitude of conversion rate, the restriction of the leaf size not only prevents overfitting but also helps provide a robust estimation of the conversion rate within each leaf. Based on the fitted tree, we estimate the conversion rate within each leaf node $( \mathrm { i . e . , }$ user segment) under each ad treatment, and aggregate across the segments to obtain the population level estimation. We summarize the algorithm in Table A1.

## Table A1

Table B1  
Algorithm of the Propensity Tree.

<table><tr><td>Algorithm of the Propensity Tree.</td></tr><tr><td>Input: Yi, Xi, and treatment Zi (multivariate or univariate);Output: Estimated conversion rate under each treatment z.</td></tr><tr><td>1. Fit a tree-based model with Zi as dependent variable and Xi as independent variable (we construct the tree following the CART guideline and select the tuning parameters based on a 10-fold cross-validation);2. For each leaf node s, count the number of subjects Ns and estimate Rs(z), which is the effect of each treatment z;3. Compute the population-level estimated conversion rates according to Eq. (3).</td></tr></table>

## Appendix B. Descriptive statistics

Examples of Consumer Characteristics in the Dataset.

<table><tr><td colspan="2">Consumer Characteristic</td><td>Proportion</td><td>Mean</td><td>SD</td></tr><tr><td rowspan="6">Demographics</td><td>Birth year</td><td></td><td>1968.88</td><td>16.54</td></tr><tr><td>Gender</td><td>52 % female</td><td></td><td></td></tr><tr><td>Region</td><td>3.185 % from Atlanta</td><td></td><td></td></tr><tr><td></td><td>2.995 % from Chicago</td><td></td><td></td></tr><tr><td></td><td>5.567 % from Los Angeles</td><td></td><td></td></tr><tr><td></td><td>... ...</td><td></td><td></td></tr><tr><td rowspan="9"> $Interest in ^a$ </td><td>Finance/Loans</td><td>60.99 %</td><td></td><td></td></tr><tr><td>Finance/Real Estate</td><td>51.86 %</td><td></td><td></td></tr><tr><td>... ...</td><td>... ...</td><td></td><td></td></tr><tr><td>Entertainment/Music</td><td>62.05 %</td><td></td><td></td></tr><tr><td>Entertainment/Art</td><td>43.88 %</td><td></td><td></td></tr><tr><td>... ...</td><td>... ...</td><td></td><td></td></tr><tr><td>Automotive/Used</td><td>66.52 %</td><td></td><td></td></tr><tr><td>Automotive/Non-US</td><td>54.30 %</td><td></td><td></td></tr><tr><td>... ...</td><td>... ...</td><td></td><td></td></tr><tr><td rowspan="4">Engagement in each retail category</td><td>Apparel</td><td></td><td>0.934</td><td>0.248</td></tr><tr><td>Accessories</td><td></td><td>0.926</td><td>0.261</td></tr><tr><td>Footwear</td><td></td><td>0.935</td><td>0.247</td></tr><tr><td>... ...</td><td></td><td>... ...</td><td>... ...</td></tr><tr><td rowspan="5"> $Frequency of online activities ^b$ </td><td>Days online</td><td></td><td>17.561</td><td>9.133</td></tr><tr><td>Web pages visited</td><td></td><td>412.772</td><td>826.593</td></tr><tr><td>Mobile pages visited</td><td></td><td>53.713</td><td>241.776</td></tr><tr><td>Ad exposures from all advertisers</td><td></td><td>1145.237</td><td>2076.931</td></tr><tr><td>... ...</td><td></td><td>... ...</td><td>... ...</td></tr><tr><td rowspan="4"> $Frequency of TV viewing activities ^c$ </td><td>Action</td><td></td><td>0.216</td><td>0.702</td></tr><tr><td>Sports</td><td></td><td>0.530</td><td>1.225</td></tr><tr><td>Talk</td><td></td><td>0.555</td><td>1.345</td></tr><tr><td>... ...</td><td></td><td>... ...</td><td>... ...</td></tr><tr><td rowspan="5"> $Exposures to other \(advertisers ^d$ </td><td>Exposures to auto parts brand #1 in the past period</td><td></td><td>1.429</td><td>3.774</td></tr><tr><td>... ...</td><td></td><td>... ...</td><td>... ...</td></tr><tr><td>Exposures to software brand #1 in the past period</td><td></td><td>2.537</td><td>5.696</td></tr><tr><td>... ...</td><td></td><td>... ...</td><td>... ...</td></tr><tr><td>... ...</td><td></td><td>... ...</td><td>... ...</td></tr></table>

Note: We are unable to reveal the complete list of consumer characteristics due to nondisclosure requirement. The table above lists some examples. SD represents standard deviation.  
<sup>a</sup> Other personal interests include politics, entertainment, education, books, travel, technology, health & pharma, etc.  
<sup>b</sup> Based on user online behavior on the focal web portal prior to the flash campaign.  
<sup>c</sup> Based on user viewing behavior prior to the flash campaign on the streaming TV service platform where the ad campaign was launched.  
<sup>d</sup> User exposures to other advertisers (anonymous per nondisclosure requirement) prior to the flash campaign.

Table C1  
Estimated Population-Level Conversion Rates for Each Combination of TV and Online Ad Exposures.

<table><tr><td>9.7e-04(4.9e-05)***</td><td>1.1e-03(9.3e-05)***</td><td>8.6e-04(1.3e-04)***</td><td>1.1e-03(1.9e-04)***</td><td>9.4e-04(1.6e-04)***</td><td>7.7e-04(1.5e-04)***</td><td>1.3e-03(1.6e-04)***</td><td>1.3e-03(2.6e-04)***</td><td>0</td></tr><tr><td>1.1e-03(8.7e-05)***</td><td>1.2e-03(1.6e-04)***</td><td>1.4e-03(2.8e-04)***</td><td>1.9e-03(3.4e-04)***</td><td>1.3e-03(4.2e-04)***</td><td>7.6e-04(3.8e-04)**</td><td>1.8e-03(2.9e-04)***</td><td>1.1e-03(3.6e-04)***</td><td>1</td></tr><tr><td>1.7e-03(1.6e-04)***</td><td>1.9e-03(3.0e-04)***</td><td>1.6e-03(3.3e-04)***</td><td>1.6e-03(5.8e-04)***</td><td>2.7e-03(7.8e-04)***</td><td>8.1e-04(4.5e-04)*</td><td>1.7e-03(4.1e-04)***</td><td>2.5e-03(7.0e-04)***</td><td>2</td></tr><tr><td>2.1e-03(2.4e-04)***</td><td>2.0e-03(3.7e-04)***</td><td>1.8e-03(4.5e-04)***</td><td>1.6e-03(7.3e-04)**</td><td>1.2e-03(5.7e-04)**</td><td>1.1e-03(8.1e-04)</td><td>2.4e-03(5.9e-04)***</td><td>1.7e-03(8.5e-04)**</td><td>3</td></tr><tr><td>2.0e-03(2.7e-04)***</td><td>2.8e-03(5.1e-04)***</td><td>1.9e-03(5.6e-04)***</td><td>1.7e-03(6.3e-04)***</td><td>1.1e-03(6.4e-04)*</td><td>2.0e-03(7.8e-04)**</td><td>2.4e-03(6.7e-04)***</td><td>2.2e-03(9.7e-04)**</td><td>4 No. of online ad exposures</td></tr><tr><td>1.7e-03(2.5e-04)***</td><td>1.9e-03(6.7e-04)***</td><td>1.7e-03(7.8e-04)**</td><td>2.0e-03(8.8e-04)**</td><td>1.7e-03(7.5e-04)**</td><td>3.1e-03(1.3e-03)**</td><td>3.8e-03(8.3e-04)***</td><td>1.7e-03(1.0e-03)*</td><td>5</td></tr><tr><td>3.4e-03(2.5e-04)***</td><td>2.5e-03(3.8e-04)***</td><td>3.2e-03(5.0e-04)***</td><td>2.9e-03(5.7e-04)***</td><td>3.1e-03(9.4e-04)***</td><td>3.6e-03(7.3e-04)***</td><td>3.4e-03(4.9e-04)***</td><td>3.6e-03(8.7e-04)***</td><td>6-10</td></tr><tr><td>3.7e-03(2.1e-04)***</td><td>3.3e-03(5.6e-04)***</td><td>3.4e-03(6.3e-04)***</td><td>3.3e-03(9.6e-04)***</td><td>3.2e-03(8.9e-04)***</td><td>3.5e-03(1.3e-03)***</td><td>3.1e-03(7.7e-04)***</td><td>3.6e-03(7.8e-04)***</td><td>11-15</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6-10</td><td>11-15</td><td></td></tr><tr><td colspan="9">No. of TV ad exposures</td></tr></table>

Note: Three, two and one asterisk(s) indicate 1 %, 5 % and 10 % statistical significance (two-tailed) respectively.

Table C2  
Estimated Conversion Rate Uplift for Each Combination of TV and Online Ad Exposures, Compared to No Ad Exposure.

<table><tr><td>baseline</td><td>9.5e-05(1.0e-04)</td><td>-1.1e-04(1.3e-04)</td><td>1.1e-04(2.0e-04)</td><td>-2.4e-05(1.7e-04)</td><td>-2.0e-04(1.6e-04)</td><td>3.3e-04(1.7e-04)**</td><td>3.7e-04(2.6e-04)</td><td>0</td></tr><tr><td>1.3e-04(1.0e-04)</td><td>2.2e-04(1.7e-04)</td><td>4.2e-04(2.9e-04)</td><td>9.5e-04(3.5e-04)***</td><td>3.0e-04(4.2e-04)</td><td>-2.0e-04(3.8e-04)</td><td>8.0e-04(2.9e-04)***</td><td>1.4e-04(3.6e-04)</td><td>1</td></tr><tr><td>7.6e-04(1.7e-04)***</td><td>9.0e-04(3.0e-04)***</td><td>6.8e-04(3.3e-04)**</td><td>5.9e-04(5.8e-04)</td><td>1.7e-03(7.7e-04)**</td><td>-1.6e-04(4.5e-04)</td><td>7.6e-04(4.1e-04)*</td><td>1.6e-03(7.1e-04)**</td><td>2</td></tr><tr><td>1.2e-03(2.4e-04)***</td><td>1.1e-03(3.7e-04)***</td><td>8.2e-04(4.6e-04)*</td><td>6.5e-04(7.3e-04)</td><td>2.3e-04(5.7e-04)</td><td>1.6e-04(8.1e-04)</td><td>1.4e-03(6.0e-04)**</td><td>7.7e-04(8.5e-04)</td><td>3</td></tr><tr><td>1.1e-03(2.7e-04)***</td><td>1.8e-03(5.1e-04)***</td><td>9.5e-04(5.6e-04)*</td><td>7.8e-04(6.3e-04)</td><td>9.1e-05(6.4e-04)</td><td>9.9e-04(7.8e-04)</td><td>1.5e-03(6.7e-04)**</td><td>1.2e-03(9.7e-04)</td><td>4 No. of online ad exposures</td></tr><tr><td>7.7e-04 (2.5e-04)***</td><td>9.1e-04(6.7e-04)</td><td>7.5e-04(7.9e-04)</td><td>1.0e-03(8.8e-04)</td><td>6.9e-04(7.6e-04)</td><td>2.2e-03(1.3e-03)*</td><td>2.8e-03(8.4e-04)***</td><td>7.0e-04(1.0e-03)</td><td>5</td></tr><tr><td>2.4e-03 (2.7e-04)***</td><td>1.5e-03(3.8e-04)***</td><td>2.2e-03(5.0e-04)***</td><td>2.0e-03(5.7e-04)***</td><td>2.2e-03(9.3e-04)**</td><td>2.7e-03(7.5e-04)***</td><td>2.4e-03(4.9e-04)***</td><td>2.6e-03(8.7e-04)***</td><td>6–10</td></tr><tr><td>2.7e-03 (2.2e-04)***</td><td>2.3e-03(5.6e-04)***</td><td>2.5e-03(6.4e-04)***</td><td>2.4e-03(9.6e-04)**</td><td>2.2e-03(8.9e-04)**</td><td>2.5e-03(1.3e-03)*</td><td>2.2e-03(7.7e-04)***</td><td>2.6e-03(7.8e-04)***</td><td>11–15</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6–10</td><td>11–15</td><td></td></tr><tr><td colspan="9">No. of TV ad exposures</td></tr></table>

Note: Three, two and one asterisk(s) indicate 1 %, 5 % and 10 % statistical significance (two-tailed) respectively. To infer the aggregated effect of the campaign, we compute the weighted average of the cells (where the weight is the number of users receiving the corresponding number of ad exposures). Comparing to the conversion rate among users with no ad exposure (which is 9.7e-04, as shown in the top left corner of Table C1), the campaign increases conversion rate by 71 %.

## References

[1] Y. Wang, C. Guo, A. Susarla, V. Sambamurthy, Online to offline: the impact of social media on offline sales in the automobile industry, Info, Sys, Res, 32 (2) (2021) 582–604.

[2] H. Zheng, L. Huang, Owned social media advertising: cannibalization and competition, J. Interact. Mark. 57 (3) (2022) 442–456.

[3] G. Athaide, J. Jeon, S. Raj, K. Sivakumar, G. Xiong, Marketing innovations and digital technologies: a systematic review, proposed framework, and future research agenda, J. Prod. Innov. Manag. (2024) 1–22.

[4] P. Danaher, T. Danaher, M. Smith, R. Loaiza-Mava, Advertising effectiveness for multiple retailer-brands in a multimedia and multichannel environment, J. Mark. Res. 57 (3) (2020) 445–467.

[5] M. van Rijmenam, Macy’s is changing the shopping experience with big data analytics. Datafloq (2014. March 14).

[6] V. Trieu, Getting value from business intelligence systems: a review and research agenda, Decis. Support. Syst. 93 (2017) 111–124.

[7] X. Bai, J. Marsden, W. Ross, G. Wang, How e-WOM and local competition drive local retailers’ decisions about daily deal offerings, Decis. Support. Syst. 101 (2017) 82–94.

[8] X. Bai, J. Marsden, W. Ross, G. Wang, A note on the impact of daily deals on local retailers’ online reputation: mediation effects of the consumer experience. Info Sys. Res. 31 (4) (2020) 1132–1143.

[9] Y. Leng, D. Dimmery, Calibration of heterogeneous treatment effects in randomized experiments. Info, Sys, Res. (2024) (forthcoming).

[10] R. Gubela, S. Lessmann, Uplift modeling with value-driven evaluation metrics. Decis, Support, Syst, 150 (2021) 113648.

[11] L. Guelman, M. Guillén, A.M. Pérez-Marín, A decision support framework to implement optimal personalized marketing interventions, Decis. Support. Syst. 72 (2015) 24–32.

[12] R. Gubela, S. Lessmann, Uplift forest for multiple treatments and continuous outcomes, in: Proc. ICIS, AIS, 2020, p. 17.

[13] Z. Zhao, T. Harinen, Uplift modeling for multiple treatments with cost optimization, in: Proc. 2019 IEEE DSAA, 2019, pp. 422–431.

[14] N. Lei, S. Moon, A decision support system for market-driven product positioning and design, Decis. Support. Syst. 69 (2015) 82–91.

[15] N. Schroder, H. Hruschka, Comparing alternatives to account for unobserved heterogeneity in direct marketing models, Decis. Support. Syst. 103 (2017) 24–33.

[16] P. Wang, G. Xiong, J. Yang, Serial position effects on native advertising effectiveness: differential results across publisher and advertiser metrics. J. Mark 83 (2) (2019) 82–97.

[17] P. Wang, G. Xiong, J. Yang, Asymmetric effects of recreational cannabis legalization, Mark. Sci. 38 (6) (2019) 927–936.

[18] S. Yang. G. Xiong. H. Mao, M. Ma. Virtual fitting room effect: moderating role ot body mass index, J. Mar. Res. 60 (6) (2023) 1221–1241.

[19] D. Zantedeschi, E. Feit, E. Bradlow, Measuring multichannel advertising response, Manag. Sci. 63 (8) (2016) 2706–2728.

[20] R. Gubela, S. Lessmann, B. Stocker, ¨ Multiple treatment modeling for target marketing campaigns: a large-scale benchmark study, Inf. Syst. Front. (2022) 1–24.

[21] V. Lo, A. Pachamanova, From predictive uplift modeling to prescriptive uplift

[22] S. Kunzel, J. Sekhon, P. Bickel, B. Yu, Metalearners for estimating heterogeneous treatment effects using machine learning, Proc. Natl. Acad. Sci. 116 (10) (2019) 4156–4165.

[23] Y. Zhao, X. Fang, D. Simchi-Levi, Uplift modeling with multiple treatments and general response types, in: Proc. 2017 SIAM, 2017, pp. 588–596.

[24] A. Linden, S. Uysal, A. Ryan, J. Adams, Estimating causal effects for multivalued treatments: a comparison of approaches., Stat. Med. 35 (4) (2016) 534–552.

[25] V. Singh, B. Nanavati, A. Kar, A. Gupta, How to maximize clicks for display advertisement in digital marketing? A reinforcement learning approach, Info. Sys. Front. 25 (4) (2022) 1–18.

[26] G. Karuga, A. Khraban, S. Nair, D. Rice, AdPalette: an algorithm for customizing online advertisements on the fly, Decis. Support. Syst. 32 (2) (2001) 85–106.

[27] I. Dinner, H. van Heerde, S. Neslin, Driving online and offline sales: the crosschannel effects of traditional, online display, and paid search advertising, J. Mark. Res. 51 (5) (2014) 527–545.

[28] L. Lesscher, L. Lobschat, P. Verhoef, Do offline and online go hand in hand? Crosschannel and synergy effects of direct mailing and display advertising, Int. J. Res Mark. 38 (3) (2021) 678–697.

[29] P. Naik, K. Peters, A hierarchical marketing communications model of online and offline media synergies, J. Interact. Mark. 23 (4) (2009) 288–299.

[30] R. Prins, P. Verhoef, Marketing communication drivers of adoption timing of a new E-service among existing customers, J. Mark. 71 (2) (2007) 169–183.

[31] P. Chatterjee, D. Hoffman, T. Novak, Modeling the clickstream: implications for web-based adyertising efforts, Mark. Sci. 22 (4) (2003) 520–541.

[32] M. Campbell, K. Keller, Brand familiarity and advertising repetition effects, J. Consum. Res. 30 (2) (2003) 292–304.

[33] L. Hoeck, M. Spann, An experimental analysis of the effectiveness of multi-screen advertising, J. Interact. Mark. 50 (1) (2020) 81–99.

[34] P. Malaviya, The moderating influence of advertising context on ad repetition effects: the role of amount and type of elaboration, J. Consum. Res. 34 (2007) 32–40.

[35] S. Schmidt. M. Eisend. Advertising repetition: a meta-analysis on effective frequency in advertising, J. Advert. 44 (2015) 415–428.

[36] S. Athey, G. Imbens, Recursive partitioning for heterogeneous causal effects, Proc. Natl, Acad, Sci, 113 (27) (2016) 7353–7360.

[37] S. Wager, S. Athey, Estimation and inference of heterogeneous treatment effects using random forests, J. Am. Stat. Assoc. 113 (523) (2018) 1228–1242.

[38] K. Imai, D. van Dyk, Causal inference with general treatment regimes, J. Am. Stat. Assoc. 99 (467) (2004) 854–866.

[39] W.Y. Loh, Fifty years of classification and regression trees, Int. Stat. Rev. 82 (3) (2014) 329–348.

[40] J. Tavlor. Like curly fries? You're clever: The science of Facebook likes, The Independent. 3/11/2013.

[41] J. Jonker, N. Piersma, R. Potharst, A decision support system for direct mailing decisions, Decis, Support, Syst, 42 (2) (2006) 915–925.

[42] G. Fitzsimons. D. Lehmann. Reactance to recommendation: when unsolicited advice vields contrary responses, Mark, Sci. 23 (1) (2004) 82–94.

[43] S. Terlep, S. Vranica, S. Raice, GM says Facebook ads don’t pay off, Wall Street J. (2012, May 16)

[44] J. Constine, Facebook fights YouTube with big data on what you watch unmuted, full-screen, TechCrunch, Jun 29, 2015. techcrunch.com/2015/06/29/datatube

[45] J. Angrist, G. Imbens, D. Rubin, Identification of casual effects using instrumental variables, J. Am. Stat. Assoc. 91 (434) (1996) 444–455.

[46] A. Petrin, K. Train, A control function approach to endogeneity in consumer choice models, J. Mark. Res. 47 (1) (2010) 3–13.

[47] P. Ebbes, M. Wedel, T. Steerneman, U. Bockenholt, New evidence for the effect of education on income: solving endogeneity with latent instrumental variables, Quant. Mark. Econ. 3 (4) (2005) 365–392.

[48] S. Park, S. Gupta, Handling endogenous regressors by joint estimation using Copulas, Mark, Sci, 31 (4) (2012) 567–586.

[49] D. Ho, K. Imai, G. King, E. Stuart, Matching as nonparametric preprocessing for reducing model dependence in parametric causal inference, Polit. Anal. 15 (2007) 199–236.

Pengyuan Wang is an Associate Professor in Marketing at Terry College of Business, University of Georgia. She obtained her PhD in Statistics from the Wharton School, Uni versity of Pennsylvania. Her research interests include digital marketing, advertising, and the related machine learning and artificial intelligence approaches. She has published in business journals such as Marketing Science, Quantitative Marketing and Economics, Journal of Marketing, and Journal of Marketing Research, as well as computer science publication venues such as World Wide Web Conference, Web Search and Data Mining, Neural Information Processing Systems, and National Conference on Artificial Intelligence.

Guiyang Xiong (PhD, Emory University) is an Associate Professor of Marketing at Whit man School of Management, Syracuse University. He conducts empirical research on marketing strategy topics such as the financial impact of marketing, digital marketing, and innovation. His research has been published in premier journals including Journal of Marketing Research, Journal of Marketing, Marketing Science, Production and Operations Management, and Journal of Management Information Systems, among others.

Will Wei Sun is an Associate Professor of Ouantitative Methods at the Daniels School of Business, Purdue University, and is also affiliated with the Department of Statistics. His research revolves around trustworthy reinforcement learning with applications in dy namic pricing, two-sided markets, advertising, and precision medicine. Dr. Sun’s research has garnered recognition through publication in esteemed journals like the Journal of the American Statistical Association, Journal of the Royal Statistical Society: Series B, Journal of Machine Learning Research, Mathematics of Operations Research, as well as in prom inent machine learning forums like Neural Information Processing Systems, Web Search and Data Mining, and the National Conference on Artificial Intelligence.

Jian Yang is a Senior Director at Yahoo Inc. He obtained his Ph.D. in Electrical and Computer Engineering from University of California, Davis. His research interests include optimization, forecasting, and machine learning, with applications in online advertising, pricing and revenue management, and supply chain management. He has published in various computer science, engineering, and business publication venues, such as IEEE Transactions. Operations Research. World Wide Web Conference, Web Search and Data Mining, Neural Information Processing Systems, and National Conference on Artificial Intelligence.

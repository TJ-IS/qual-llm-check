---
otero_id: 2572
otero_key: "SH3G3JV6"
title: "Effects of decision space information on MAUT-based systems that support purchase decision processes"
authors: "Michael Scholz; Markus Franz; Oliver Hinz"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.03.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Effects of decision space information on MAUT-based systems that support purchase decision processes

Michael Scholz<sup>a,</sup>\*, Markus Franz<sup>b</sup>, Oliver Hinz<sup>b</sup>

<sup>a</sup>Faculty of Business Administration and Economics, University of Passau, Innstr. 43, Passau 94032, Germany <sup>b</sup>TU Darmstadt, Hochschulstr. 1, Darmstadt 64289, Germany

## A R T I C L E I N F O

Article history: Received 13 July 2016 Received in revised form 9 March 2017 Accepted 9 March 2017 Available online xxxx

Keywords: Product search Decision space Visualization Multiattribute utility theory

## A B S T R A C T

This paper shows that decision makers often have a misconception of the decision space. The decision space is constituted by the relations among the attributes describing the alternatives available in a decision situation. The paper demonstrates that these misconceptions negatively affect the usage and perceptions of MAUT-based decision support systems. To overcome these negative effects, this paper proposes to use a visualization method based on singular value decomposition to give decision makers insights into the attribute relations. In a laboratory experiment in cooperation with Germany’s largest Internet real estate website, this paper moreover evaluates the proposed solution and shows that our solution improves decision makers’ usage and perceptions of MAUT-based decision support systems. We further show that information about the decision space ultimately affects variables relevant for the economic success of decision support system providers such as reuse intention and the probability to act as a promoter for the systems.

© 2017 Published by Elsevier B.V.

## 1. Introduction

Online stores offer their customers a great product variety also in narrowly defined product categories. Amazon, for example, offers approximately 70 products in the category ‘kids and family movies released within the last 90 days on Blu-ray’ [1]. To unlock the potential of rich assortments, decision support systems (DSS) are frequently implemented in online stores in order to help consumers finding products meeting their individual preferences [2–4]. They help consumers reducing the number of considerable alternatives which in turn leads to more thorough evaluations of less alternatives and finally a higher purchase probability [5,6].

Assisting consumers in decision making is, however, more than simply reducing the number of decision alternatives. Consumers are also required to implicitly or explicitly specify their preferences in terms of, for example, importance weights for all relevant attributes. The satisfaction with a DSS’s recommendations ultimately depends on the reliability of the consumers’ stated preferences (i.e., attribute weights) which are used to generate recommendations.

To reliably state preferences, consumers need to know how determinant a particular attribute is for their choice, how the attributes are related to each other (i.e., how a high weight for one attribute affects the outcome for the remaining attributes) and they hence must weigh attributes accordingly. The single-attribute utility for attribute X often depends on the level selected for another attribute Y. If X and Y are, for example, in a conflicting relationship, a consumer must weigh between high importance and thus high utility for X or high utility for Y. The conception of the attribute relations forms the expectations about the alternatives a consumer can get recommended from a decision support system and also the attribute weights she will specify. Consumers can, however, only reliably weigh between X and Y if they correctly know the relationship between X and Y. If a consumer has a misconception of the relation between X and Y she likely will expect alternatives that are not really existing (i.e., alternatives having a high utility for X and Y) and specify inappropriate attribute weights. A DSS then presents recommendations that might be below the consumer’s expectations.

This will lead to negative disconfirmation and finally dissatisfaction with the recommendations [4]. Defining reliable attribute weights thus requires information about the relations among the attributes [7]. We define the relations among attributes that are available in a decision process as the decision space (DS). Existing DSSs assume decision scenarios in which the decision maker can be assumed to be well-informed about the DS [8–10]. Other research, however, provides evidence that consumers often have misconceptions of this DS [11,12] and that consumers do not understand why a product is recommendable for them [13], which ultimately might lead to dissatisfaction with the recommendations and the DSS. Consistent with the definition of the DS, a consumer has a misconception of the DS if she assumes wrong correlations between the attributes available in a decision process [14]. A consumer who, for example, assumes that two attributes are strongly negatively correlated (i.e. assumes that they are conflict) has a misconception of the DS if the attributes are only weakly negatively or positively correlated in reality.

Our contribution to existing research is two-fold. First, we demonstrate an unattended cognitive problem and its impact on MAUT-based DSSs. Existing research provided some indication that decision makers might have misconceptions of decision spaces and thus need explanations [15]. We show to which extent decision makers have misconceptions and that these misconceptions exist independent of the experience decision makers have with the alternatives. Second, we suggests to visualize information about the DS with a scatterplot that is generated with singular value decomposition. We show that our solution affects decision makers’ usage and perception of a MAUT-based DSS.

The paper proceeds as follows: We briefly introduce DSSs that are based on MAUT in the next section. In Section 3, we discuss the impact of consumers’ conception of the DS on using MAUT-based DSSs. We then propose a visualization of the decision space based on singular value decomposition in Section 4. This visualization method is thereafter implemented in two variants in a DSS which we empirically compare to a DSS that textually presents information about the DS and a DSS that does not present any information about the DS. The empirical setting is described in Section 5 and the results are presented in Section 6. We then discuss our findings and the implications for researchers and managers in Sections 7 and 8. The paper concludes with a description of limitations and directions for future research in Section 9.

## 2. MAUT-based decision support systems

Multi-attribute utility theory (MAUT) offers a sound, easy to implement, and widely adopted approach for modeling multi-criteria decision-making scenarios [16–18]. Decision alternatives are considered as bundles of attributes in MAUT, so the evaluation of alternatives occurs through evaluations of the attributes. Each attribute can be described by a single-attribute utility (SAU) function that offers a utility value between 0 and 1. The SAU functions then get integrated into a (usually additive) multi-attribute utility (MAU) function that computes the utility values for all alternatives. Specifically, let u (x ) be the SAU function for attribute $i , x _ { i }$ be the outcome of attribute i, and $w _ { i }$ be the weight for attribute i. Then we can formally express the additive MAU function for assessing alternative utilities $u ( X )$ as

$$
u (X) = \sum_ {i = 1} ^ {n} w _ {i} u _ {i} (x _ {i})\tag{1}
$$

where $0 \leq w _ { i } \leq 1$ and $\textstyle \sum _ { i = 1 } ^ { n } w _ { i } = 1$

To calculate an entire alternative’s utility value, SAU values are typically multiplied with attribute weights $w _ { i }$ and summed up. MAUT-based DSSs finally compile recommendation lists based on the alternatives’ overall utility values [19].

SAU functions often are assumed to be linearly increasing from 0 to 1 when the outcome of an attribute i increases from its worst to its best level [20]. Attribute weights w are then the only input consumers must provide to a MAUT-based DSS in order to get recommendations.

The weight $w _ { i }$ of attribute i represents the impact of i on utility u(X) when the outcome of i changes from its worst to its best level.

Relations among the attributes define how easy it is to get an alternative with the best level for attribute i given that the levels of all other attributes are fixed. Both, the contribution of an attribute i to a product’s utility and the relation of i to other attributes might affect a consumer’s stated attribute importance weight. An attribute that contributes significantly to the overall utility u(X) but is easy to reach also if other attributes are at a good level is not very important and hence gets a low weight [21]. This implies that the consumer must know the DS (i.e., the relations among the attributes) to thoroughly weigh attributes.

In Section 3, we derive a theoretical framework that demonstrates the impact of such misconceptions on consumers’ expectations about existing alternatives and ultimately their usage and perception of DSS.

## 3. Information about the decision space and its impact on using MAUT-based decision support systems

The decision space (DS) refers to the relations among the attributes describing the alternatives. Decision makers form expectations about the alternatives available [22] based on current and past information about the DS [23]. A decision maker’s expectation mainly determines her satisfaction with the recommended alternatives [4]. If the actual performance of the recommended alternatives is below the expectations, it leads to a negative disconfirmation and dissatisfaction [24].

Recent studies, however, show that consumers as a kind of decision makers typically have only low product knowledge [12], and even consumers with prior information about the DS tend to be overconfident and assume that they know more than they do [11]. Bettman et al. [14], for example, find that decision makers poorly assess correlations among attributes which is one instantiation of having a misconception of the DS. MAUT-based DSSs require that decision makers specify attribute importance weights which are used to compute utility values for the possible alternatives and to finally recommend alternatives to decision makers. A decision maker who has a misconception of the DS might state other attribute weights than a decision maker who knows the correct DS.

In the next subsections, we investigate to what extend decision makers have misconceptions about the DS and how these misconceptions impact the interaction with a MAUT-based DSS.

## 3.1. Study 1: decision makers’ conception of the decision space

Some studies [12,14] indicate that decision makers often do not know much about the DS and that decision makers poorly assess the relations between attributes. There is furthermore evidence that decision makers often are overconfident in terms of their knowledge about the DS [11]. Thus, we hypothesize:

H1. Decision makers often do have a misconception of the decision space.

To test this hypothesis, we administered a survey to 162 undergraduate students. We used smartphones as a product related to greater product experience and camping tents as a product with less experience to examine the misconception of the DS on products with different product experience. 118 participants completed the survey resulting in a response rate of 72.83%. The smartphones were described by price in Euro, display size in inches, equipment in points, and battery time in points. Tents were described by price in Euro, size in persons, weight in grams, and level of water resistance in mm/m<sup>2</sup>. The DSs thus consisted of six attribute relations for each product category. We collected data for 100 products in each category, actually available in Germany in October 2016 and listed as top 100 products at Amazon.de, to identify realistic relations among the attributes (i.e., information on the DS).

In this survey, each participant assessed six relations of smartphonesandtentson anine-point scale,ranging fromaperfect negative relation (correlation = 1) to a perfect positive relation (correlation = 1), specified the certainty for each of the six relations between 0 and 100% and revealed her level of product experience on three items [25], using a nine-point scale. Consistent with the definition of misconception (i.e., assumption of wrong correlations between attributes available in a decision process [14]), participants were told to state the attribute relations they assume to be exist. On average the participants were very experienced with smartphones (7.322 out of 9 points, $S D ~ = ~ 1 . 6 3 2 )$ and significantly less experienced $( p < 0 . 0 0 1$ ; tested with a Mann-Whitney U-test) with tents (4.288 out of 9 points, SD = 2.404). As the results in Tables 1 and 2 indicate, several participants specified attribute correlations that are substantially different from the actual correlations that can be found between the attributes of real existing smartphones and tents. We counted the number of participants who assumed a correlation between two attributes that was different by at least 0.5 correlation units (which constitutes a substantial false estimation) from the true correlation. More than 45% of our participants, for example, assumed a correlation between display size and battery time that is substantially (i.e., at least 0.5 correlation units) different from the actual correlation (see Table 1).

The assumed relations between the tent attributes are on average more different from the actual relations than the assumed smartphone relations. This can be explained by the significantly lower revealed experience with tents than with smartphones. The certainty with which our participants specified the attribute relations of tents was interestingly on approximately the same level as for the smartphone attribute relations.

We further found a positive correlation between the difference between the actual and the assumed correlation and the certainty with which the assumed correlation has been specified of 0.067 $( p = 0 . 0 7 5 )$ for smartphone attributes and 0.301 $( p < 0 . 0 0 1 )$ for tent attributes (tested with a correlation test). A higher certainty about the assumed correlation is thus related to a higher misjudgment of the actual correlation. This indicates that decision makers often have a misconception of the attribute relations and hence the DS and that surprisingly the misconception grows with the consumers’ self-stated product experience. A significant positive correlation between product experience and the certainty with which the assumed correlations have been specified of 0.139 (p < 0.001) for smartphones and 0.125 $( p < 0 . 0 0 1 )$ for tents underlines that more experienced decision makers are more certain that their perception about the DS is correct (tested with a correlation test). We hence find support for H1.

The next subsection presents an experiment that shows the impact of a misconception of the DS on decision makers’ expectations of available alternatives and their satisfaction with recommended alternatives.

3.2. Study 2: impact of a misconception of the DS on decision makers’ expectations and satisfaction with recommendations

Recent research has shown that decision makers form expectations about existing alternatives [22] based on past information about the DS [23]. As shown in the previous subsection, decision makers often have misconceptions about the DS. We thus hypothesize that a misconception of the DS leads to incorrect expectations about the alternatives that a DSS can and will recommend.

H2. Misconceptions of the decision space lead to incorrect expectations of recommendations.

If expectations exceed the actual performance of the recommended alternatives, it leads to a negative disconfirmation and dissatisfaction [4,24]. A misconception of the DS hence might in turn lead to incorrect expectations about the recommendations of a MAUT-based DSS. Negative disconfirmation also is stronger than positive disconfirmation [26]; decision makers remain dissatisfied if some attributes are worse than expected, even if others are better than expected. We therefore hypothesize that incorrect expectations lead to dissatisfaction on average.

H3. Incorrect expectations about recommendations lead to dissatisfaction with actual recommendations.

We conducted a laboratory experiment with between-subjects design, in which we primed either correct or incorrect information about the DS based on actual market data. We provided the participants with information about the relations among all attributes using small bar charts with 9 cells that indicated whether attribute X correlated negatively with attribute Y (0 out of the 9 cells were filled), correlated positively (9 out of the 9 cells were filled) with Y, or anything in between. We used smartphones as the product and defined the incorrect DS information according to the assumed correlations among smartphone attributes in Table 1. The participants who received correct DS information represented the control group. In total 91 undergraduate students participated in this experiment (45 received correct information).

We first measured the participants’ experience with smartphones using a three-item scale [25]. We did not find any significant differences in experience between the groups $( p = 0 . 4 7 1$ ; tested with a Mann-Whitney U-test) which is a sign that our random assignment was appropriate. Participants then had to complete two judgment tasks, in which they had to state which of two smartphones is more likely to exist on an actual smartphone market. The hypothetical, non-existing alternative in each case differed notably from other smartphones on the market at the time<sup>1</sup>. Participants revealed their opinions on a nine-point scale, ranging from 1 (the first smartphone is definitely the real one) to 9 (the second smartphone is definitely the real one).

Participants with correct information specified a probability of 31.56% that the “existing” smartphone is real, whereas participants with incorrect information only specified a probability of 17.39% on average $( p \ = \ 0 . 0 1 9 ;$ ; tested with a binomial test) that the “existing” smartphone is real. Simultaneously, respondents with incorrect information rated the “non-existing” smartphone as more likely to be the real alternative (27.83%) than those with correct information (15.11%), indicating significantly different expectations about available alternatives $( p = 0 . 0 1 5 ;$ tested with a binomial test)<sup>2</sup>.

We did not find significant difference in the probability that the “non-existing” smartphone was assumed to be really existing $( p r _ { c o r r e c t } = 8 . 0 0 \% , p r _ { i n c o r r e c t } = 8 . 2 7 \% )$ in the second task. However, the “existing” smartphone was rated as significantly more likely to be the real smartphone by participants who received correct DS information $( p r _ { c o r r e c t } = 4 7 . 1 1 \% , p r _ { i n c o r r e c t } = 3 3 . 0 4 \% , p = 0 . 0 1 8 \%$ ; tested with a binomial test).

Participants with incorrect decision space information significantly more often failed to correctly decide which of two smartphones will really exist on the market. These participants will hence make bad inferences about the available alternatives.

Next, we provided the attribute weights of a hypothetical person M ${ } ^ { \prime } ( w _ { d i s p l a y \_ s i z e } = 0 . 3 3 3 , w _ { e q u i p m e n t } = 0 . 3 , w _ { b a t t e r y \_ t i m e } = 0 . 2 3 3 ,$ $w _ { p r i c e } = 0 . 1 3 3 )$ and asked the participants to find a good smartphone for person M. The participants evaluated five smartphones with respect to the expected satisfaction of M with the smartphones on a nine-point scale. We primed our participants with common attribute weights of a hypothetical person because the attribute weights might mainly determine the evaluation of the five smartphones.

Table 1  
Actual and expected relations among smartphone attributes.

<table><tr><td>Relation</td><td>Actual correlation</td><td>Expected correlation (SD)</td><td>Proportion of persons with a misjudgment of at least 0.5 (in %)</td><td>Certainty of the assumed correlation (in %)</td></tr><tr><td>Price  $\Longleftrightarrow$  Display size</td><td>0.345</td><td>0.451 (0.335)</td><td>15.25</td><td>61.23</td></tr><tr><td>Price  $\Longleftrightarrow$  Equipment</td><td>0.758</td><td>0.665 (0.287)</td><td>14.41</td><td>80.51</td></tr><tr><td>Price  $\Longleftrightarrow$  Battery time</td><td>0.336</td><td>0.169 (0.367)</td><td>19.49</td><td>62.82</td></tr><tr><td>Display size  $\Longleftrightarrow$  Equipment</td><td>0.323</td><td>0.201 (0.287)</td><td>2.54</td><td>62.19</td></tr><tr><td>Display size  $\Longleftrightarrow$  Battery time</td><td>0.294</td><td>-0.180 (0.416)</td><td>45.76</td><td>64.51</td></tr><tr><td>Equipment  $\Longleftrightarrow$  Battery time</td><td>0.193</td><td>0.019 (0.429)</td><td>26.27</td><td>59.22</td></tr></table>

To assess the impact of the provided information on satisfaction, we computed the probability of expecting the correct smartphone for each of our participants by combining the probabilities for the “existing” smartphones across the first and the second judgment task. By applying a Logit regression, we determined that the probabilities of expecting both the correct and the incorrect versions significantly influenced Ms expected satisfaction with the five smartphone recommendations $( e s t _ { c o r r e c t } = 0 . 1 4 1 , p _ { c o r r e c t } = 0 . 0 4 0 , e s t _ { i n c o r r e c t } =$ $- 0 . 1 9 7 , p _ { i n c o r r e c t } = 0 . 0 3 4 )$

The results of this experiment indicate that misconceptions of the DS lead to incorrect expectations about recommendations, in support of H2. These incorrect expectations in turn lead to lower satisfaction with the recommendations, in support of H3. We conclude that the conceptualization of the DS is an essential determinant of a decision maker’s satisfaction with a MAUT-based DSS.

In the next subsection, we investigate the impact of a misconception of the DS on the attribute weights decision makers need to state when using a MAUT-based DSS.

## 3.3. Study 3: impact of a misconception of the DS on attribute weights

Decision makers having a misconception of the DS might specify attribute weights that are different to those specified by decision makers not having such a misconception. Attributes that are in a conflicting relation force decision makers to thoroughly decide which of the attributes is more important for them. Decision makers might not think much about the weights they assign to attributes for which they assume a nonconflicting relation. If on the other side decision makers assume a conflicting relation between two attributes but the attributes are not conflicting decision makers might put a lower weight to one of the attributes in order to avoid recommendations in which both attributes are mediocre leveled. We thus hypothesize that a misconception about the DS will affect decision makers’ stated attribute weights in a MAUT-based DSS.

H4. Misconceptions of the decision space affect decision makers stated attribute weights in MAUT-based DSS.

We conducted a laboratory experiment with between-subjects design to test this hypothesis. Our participants again either got correct or incorrect information about the DS of smartphones. The correct informationconsistedofthetrueactualattributecorrelationswhereas the incorrect information were based on the assumed attribute correlations from Table 1. The participants of this experiment stated their attribute weights on a nine-point scale (1 = very unimportant, 9 = very important) for the four smartphone attributes display size, equipment, battery time and price based on the information about the DS. We invited 139 undergraduate students from which 136 (70 with correct information and 66 with incorrect information) successfully completed the experiment.

On individual attribute level, we did not find a significant difference between the two experimental groups for any of the attribute weights (see Table 3). Pooling all attributes together, we, however, found that participants revealed significantly higher importance weights on average $( p = 0 . 0 1 1 )$ when they got correct information about the DS (tested with a Logit regression where the stated weight was used as number of success and the best possible weight was used as number of trials). Table 1 shows that participants often assumed a conflicting relation between attributes that are truly positively correlated. Participants hence often felt they had to choose between a high level for attribute X or a high level for attribute Y. This might have triggered the participants to give one attribute a rather high and the other attribute a rather low weight which ultimately results in lower weights on average. We found such a pattern for the attributes battery time and equipment. The difference between the weights for battery time and equipment is significantly larger $( p = 0 . 0 3 8 ;$ tested with a Logit regression) for those participants that got incorrect information about the DS. We did not find a significant difference between the weights of any other pair of attributes.

Table 2  
Actual and expected relations among tent attributes.

<table><tr><td>Relation</td><td>Actual correlation</td><td>Expected correlation (SD)</td><td>Proportion of persons with a misjudgment of at least 0.5 (in %)</td><td>Certainty of the expected correlation (in %)</td></tr><tr><td>Price  $\Longleftrightarrow$  Size</td><td>0.345</td><td>0.667 (0.303)</td><td>28.81</td><td>73.20</td></tr><tr><td>Price  $\Longleftrightarrow$  Weight</td><td>0.182</td><td>-0.231 (0.504)</td><td>54.24</td><td>61.97</td></tr><tr><td>Price  $\Longleftrightarrow$  Water resistance</td><td>0.031</td><td>0.718 (0.295)</td><td>68.64</td><td>78.18</td></tr><tr><td>Size  $\Longleftrightarrow$  Weight</td><td>0.723</td><td>0.487 (0.400)</td><td>22.03</td><td>69.17</td></tr><tr><td>Size  $\Longleftrightarrow$  Water resistance</td><td>0.160</td><td>-0.034 (0.312)</td><td>16.95</td><td>55.40</td></tr><tr><td>Weight  $\Longleftrightarrow$  Water resistance</td><td>0.216</td><td>0.083 (0.285)</td><td>9.32</td><td>55.19</td></tr></table>

Please cite this article as: M. Scholz et al., Effects of decision space information on MAUT-based systems that support purchase decision processes, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.03.004

Table 3  
Stated attribute importance weights.

<table><tr><td rowspan="2">Attribute</td><td colspan="2">Correct information</td><td colspan="2">Incorrect information</td></tr><tr><td>Mean weight</td><td>SD weight</td><td>Mean weight</td><td>SD weight</td></tr><tr><td>Display size</td><td>5.687</td><td>1.822</td><td>5.441</td><td>1.757</td></tr><tr><td>Battery time</td><td>7.443</td><td>1.529</td><td>7.246</td><td>1.858</td></tr><tr><td>Equipment</td><td>6.971</td><td>1.888</td><td>6.687</td><td>1.681</td></tr><tr><td>Price</td><td>6.829</td><td>2.126</td><td>6.493</td><td>2.142</td></tr></table>

## 3.4. Implications for MAUT-based decision support systems

Our investigations so far indicate that (a) decision makers typically have a misconception of the DS, (b) this misconception leads to incorrect expectations about the alternatives available on market and changes the stated attribute weights, and (c) incorrect expectations lead to dissatisfaction with the recommendations of a MAUT-based DSS.

We therefore propose, that MAUT-based DSS should provide decision makers with direct information about the DS before making any recommendations. Information about the DS should include descriptions of the relations among all interesting attributes. With respect to our findings, we assume that information about the DS, provided during the interaction of the decision maker with the DSS, will lead to more realistic expectations about the alternatives available, as well as more reliable attribute weights, which ultimately should improve the decision maker’s satisfaction with both recommendations and the DSS.

The major challenge of presenting information about the DS is to find a format that does not divert decision makers from interacting with the DSS to make a good decision. In the next section, we suggest a possible solution for presenting this information, such that decision makers can easily process it.

## 4. Design of a visualization method

Providing additional information to consumers can lead to a situation of information overload, which reduces the reliability of consumers’ stated attribute weights. To minimize the effect of potential information overload, we propose a visualization method that presents the DS in a clear, easy to interpret manner. According to Vessey and Galletta [27], consumers benefit from visualizations that provide cognitive fit with the decision process. We propose a visualization method that enhances DSSs so that consumers can (a) easily understand the relations among the attributes, (b) adapt their expectations about available alternatives and (c) easily identify available combinations of attribute levels $( \mathrm { i . e . , }$ available alternatives).

## 4.1. Visualization methods

In line with theory and previous research and in light of our empirical findings, we have argued that consumers need a realistic conceptualization of the DS to provide reliable attribute weights. A solution might be a visual depiction of the DS. Several visualization methods are available for plotting multi-dimensional data. In our case, we have product data that are described by multiple product attributes $( \mathrm { i . e . } ,$ , dimensions). Parallel Coordinates, as one of the most famous multivariate visualization methods [28,29], show a backdrop consisting of n parallel lines with n being the number of dimensions (product attributes in our case). Each product is represented as a polyline with vertices on the parallel axes. The position of the vertex on an axis i corresponds to the level of attribute i. The most significant drawback of parallel coordinates is that each axis can have at most only two neighboring axes, which makes it hard for consumers to identify the attribute relation between attributes that are not represented by neighboring axes.

A similar visualization method is the star plot or radar chart which consists of equi-angular spokes that represent the attributes [30]. The polylines representing the products hence do not start or end at a particular axis which has the advantage that each axis exactly has two neighboring axes. Consumers can hence only identify the relation of one attribute with two other attributes with relative ease. Since radial distances are hard to judge, it is furthermore not easy for consumers to even identify the relation of two attributes that are represented by two neighboring axes. The area the polylines in a star plot surround is furthermore invariant and depends on the ordering of the axes [31]. This area is likely to be used to compare different alternatives.

Another alternative are heatmaps that can be used to visually depict the correlations between a set of variables [29]. Therefore a grid with the attributes in the rows and the columns is created. Each cell then represents the relation between two attributes. In contrast to parallel and star plots, heatmaps do not allow to also show the set of alternatives in one and the same plot. Moreover, heatmaps have been found to be not very easy to use [29].

Theetranont et al. [32] proposed using a scatterplot to depict a DS that consists of up to three attributes and their relations. Although this visualization is easy to implement and interpret, it suffers from two major drawbacks. First, consumers typically consider more than three attributes [33]. Second, consumers must select the “right” three attributes for the visualization.

To overcome the limitation of visualizing DSs with only three attributes, we can either reduce dimensionality, present consumers many visualizations with only parts of the DS or use another visualization type such as parallel coordinates or star plots. Dividing the DS into parts hampers consumers’ ability to get a picture of the DS. We already argued that visualization types such as parallel coordinates or star plots are subject to the problem that several attribute relations are not easy to interpret. We hence propose generating a high-dimensional space, with the attributes as dimensions and the alternatives as points in the space. Dimension reduction then is necessary to make the high-dimensional space interpretable.

The need to analyze and visualize large amounts of multi-criteria data has prompted investigations of methods for reducing dimensionality [34]. Singular value decomposition (SVD) constitutes the standard method for linear dimension reduction in data visualization [35] and statistics where it is used as principal component analysis [36]. Recent literature also suggests, but has not examined, SVD as a method to depict DSs [37]. We adopt this notion and propose using SVD to visualize DSs. Next, we describe the application of a scatterplot generated with SVD in MAUT-based DSS.

## 4.2. Visualization method based on SVD

To compile a visualization that provides information about the relations among attributes, assume a coordinate system with I dimensions, each representing an attribute. Reducing dimensions is almost always possible only with a loss of variance. We suggest SVD, which reduces dimensions but maximizes preserved variance [38]. Before reducing data dimensions with an SVD, we must preprocess the data.

The first step to reduce dimensions is to generate and normalize a data matrix with two variables, attributes i and alternatives j. Each cell contains the level $x _ { i j }$ of a particular attribute for a particular alternative. Table 4 shows an example for the apartment scenario, with four attributes and four alternatives.

The standardization in the next step attempts to move the centroids of both alternative and attribute points to the point of origin.

Table 4  
Example of data matrix.

<table><tr><td>Alternative</td><td>Rooms</td><td>Furnishing</td><td>Location</td><td>Price</td></tr><tr><td>A1</td><td>5</td><td>7</td><td>7</td><td>4</td></tr><tr><td>A2</td><td>4</td><td>5</td><td>8</td><td>9</td></tr><tr><td>A3</td><td>7</td><td>3</td><td>9</td><td>6</td></tr><tr><td>A4</td><td>8</td><td>2</td><td>5</td><td>5</td></tr></table>

An SVD exploits the ability to divide any matrix Z of standardized points into the following components [38]:

$$
Z = \Gamma \Sigma \Delta^ {T}\tag{2}
$$

where S is a diagonal matrix of K singular values, such that $\sigma _ { 1 } \geq$ $\sigma _ { 2 } \ \geq \ . \ . . \ \geq \ \sigma _ { k } ;$ the C(IxK) matrix contains the eigenvectors of $Z Z ^ { T } .$ which are required to compute the visual points of all elements of the first variable (i.e., attributes); and $\Delta ( J x K )$ contains the eigenvectors of ${ \mathrm { ~ . ~ } } Z ^ { T } Z ,$ , employed to compute the visual points of the other variable (i.e., alternatives).

ThesolutionofEq.(2)providesthestandardcoordinatesforthefirst variable $\gamma _ { i k }$ (here attributes) and the second variable $\delta _ { j k }$ (here alternatives). Directly interpreting both variables jointly is not possible though, because of the different proportions for the attribute levels in the data set. We propose a symmetric rescaling [39] in order to allow consumers to interpret alternatives and attributes jointly:

$$
r _ {i k} = \frac {\gamma_ {i k} \sigma_ {k}}{\sqrt {p _ {i \bullet}}}\tag{3}
$$

$$
c _ {j k} = \frac {\delta_ {j k} \sigma_ {k}}{\sqrt {p _ {\bullet j}}}\tag{4}
$$

The possibility of a joint interpretation of alternatives and attributes helps consumers to correctly perceive the alternatives’ attribute levels which ultimately will improve the consumers’ sensemaking experience [40].

Thus, we extract the first two or three singular values $( \sigma _ { 1 } , \sigma _ { 2 }$ and $\sigma _ { 3 } )$ to compile two- or three-dimensional scatterplots of the DS. We now have two or three coordinates $( r _ { i 1 } , r _ { i 2 } ,$ and $r _ { i 3 } )$ for each attribute i and two or three coordinates $( c _ { j 1 } , c _ { j 2 }$ , and $c _ { j 3 } )$ for each alternative j. The distance between attributes illustrates their relation, as we show in Fig. 1.

![](/api/attachments/SH3G3JV6/fulltext/images/886208ccb9cdd0bb70da33cc92c7941a9f389874de5a61719e6c6b259eda5dfb.jpg)  
Fig. 1. Relationship between attributes and alternatives

A greater distance indicates more conflict between attributes (e.g., furnishing and rooms) and thus a lower probability of finding an alternative that fulfills both. Consumers can interpret the distance between alternatives and attributes similarly: The closer a particular alternative is to a particular attribute, the better the alternative fulfills that attribute (e.g., apartment 4 has the most rooms).

Similar alternatives are represented in the near of each other whereas the representations of different alternatives are distant to each other, two design principle that have been proposed to improve the sensemaking experience of users of a visualization [40]. Interpreting distances of visual objects as distances of the represented objects (here alternatives and attributes) furthermore supports analogical reasoning, a further design principle proposed by Baker et al. [40].

## 5. Study 4: evaluation of a DSS with visual DS information

In this section, we present the evaluation methodology used to empirically investigate our two hypotheses in a laboratory experiment with prospective consumers. We examine the effect of information about the DS on satisfaction with the recommendations and the DSS, as well as the effect of additional information about the DS on the number of search steps. We developed four different DSSs related to searches for apartments to examine the effects of information about the DS and the effects of different visualization types. We consider the following attributes in our empirical study: size of living area, number of rooms, rent, ancillary costs, dedicated parking space, cellar, balcony, and distance to city center.

We conducted the laboratory experiment with a variant of the online platform ImmobilienScout24, Germany’s largest Internet real estate marketplace. It offers services and brings together vendors with property seekers. On the ImmobilienScout24 site, property seekers receive information to make their decisions, and sellers use the platform to market their properties. Every month, Immobilien-Scout24 lists around 1.2 million different properties to rent or buy. Categories include apartments and commercial properties, land and finance projects, holiday accommodations, properties abroad, senior citizen homes, temporary housing, and furnished apartments. Estate agents, property developers, and private sellers post offers. The highly frequented portal receives more than 5 million unique visitors and 1.2 billion page impressions each month. In addition, more than 250 million virtual property visits are conducted over the website every month.

Our empirical evaluation aims at answering two research question: First, do information about the DS help prospective consumers in their purchase decision process. We investigate consumers’ satisfaction with the recommendations of a MAUT-based DSS, their perceptions of the DSS and their usage of the DSS in order to answer the first question. Second, do different information presentation formats affect the influence of DS information. We propose using a scatterplot to visualize information about the DS. Such a scatterplot can consist of two or three dimensions (see Section 4.2). Recent research has found rather mixed evidence on the performance of 2D compared to 3D visualizations [41,42]. We furthermore compare our proposed scatterplot visualization to a system that presents information about the DS textually. A visual depiction of the DS might have two different effects on a consumers purchase decision process: the effect of the presented information and the effect of the visualization per se. In order to proof if the information is responsible for an improvement of a consumer’s satisfaction with the recommendations from a MAUT-based DSS and her perceptions on the DSS, we also investigate a DSS that textually depicts DS information.

Please cite this article as: M. Scholz et al., Effects of decision space information on MAUT-based systems that support purchase decision processes, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.03.004

M. Scholz et al. / Decision Support Systems xxx (2017) xxx–xxx

<table><tr><td></td><td>Task 1: Screening</td><td>Task 2: Evaluation</td><td>Task 3: Recommendation List</td><td>Task 4: Questions</td></tr><tr><td>System 1</td><td rowspan="4">Define Aspiration Levels</td><td>Define Attribute Weights without Decision Space Information</td><td rowspan="4">Specify the Visit Probability for the First 10 Recommendations in the Recommendation List (Recommendation List is Sorted by the Utilities of the Products)</td><td rowspan="4">Questions about the Perceptions of the System and Personal Characteristics</td></tr><tr><td>System 2</td><td>Define Attribute Weights with Textual Decision Space Information</td></tr><tr><td>System 3</td><td>Define Attribute Weights with 2D Visual Decision Space Information</td></tr><tr><td>System 4</td><td>Define Attribute Weights with 3D Visual Decision Space Information</td></tr><tr><td></td><td colspan="3">Utility-based Recommender System</td><td>Questionnaire</td></tr></table>

Fig. 2. Experimental procedure.

## 5.1. Experimental treatments

To measure the effects of the information about the DS separately from any effect of the proposed visualization, we developed four recommender systems as special instances of DSSs [43], which represent the treatments for our experiment (see Fig. 2). Following the two-stage decision process [44,45], we assume that consumers apply non-compensatory strategies first, then employ compensatory decision rules. Therefore all systems allowed the consumers to first filter city districts and specify a range for the number of rooms, size of living area, rent, and ancillary costs (Task 1 in Fig. 2). Consumers then could determine the weighting of the attributes using a nine-point scale ranging from 0 (=totally unimportant) to 8 (=very important) and initially set to 4 (Task 2 in Fig. 2). The second step is supported by a varying presentation of the DS<sup>3</sup>. We implemented a direct rating to measure attribute weights in all systems; this method is user friendly and highly accurate compared to other methods [46].

The first step was used to filter the set of available apartments for the second step. The DS visualizations were hence generated based on the filtered set of apartments. SAU functions were assumed to be concave because all attribute levels that represent a loss were filtered out in the first step. We normalized the remaining attribute levels to [0 1] and computed each attribute’s utility value as $u _ { i } ( x _ { i } ) = x ^ { 2 }$ which is the simplest form to model a concave SAU function that gives unweighted attribute values in [0 1] for normalized attribute levels.

System 1 provides no information about the DS, as is standard for MAUT-based DSSs. It thus serves as the benchmark. System 2 provides textual information about the DS, such as by indicating that low rent and apartment size are conflicting attributes. Systems 3 and 4 provide the same information visually, following the SVD approach. The systems calculate the relations among the eight attributes based on the alternatives that meet the aspiration levels. The attributes were depicted as circles on a two-dimensional (System 3) or bullets on a three-dimensional (System 4) screen. The proximity of circles/bullets indicated attributes that are reconcilable; greater distance indicates conflicting attributes. Rectangles with numbers symbolize the ten best alternatives, which the system places on the panel according to the SVD approach. This visual support should help consumers understand the DS and correctly judge their trade-offs.

With these four treatments, we separated the effect of information about the DS from the presentation format. If consumers are very excited about visual support, they might perceive the visual system as superior, even if they consider the value of the provided information relatively low. Such an effect is unlikely in System 2, which presents the information in a very simple, textual format. We examined two visualizations (2D and 3D), because visualization format can have an effect on a visually supported decision process. The comparison among systems that provide information about the DS (Systems 2–4) thus enables us to assess (i) the unique impact of the information about the DS, (ii) the unique impact of a visualization, and (iii) the unique impact of 2D versus 3D visualization.

## 5.2. Procedure

Our business partner ImmobilienScout24 provided data on apartment offers for the city of Frankfurt/Main, Germany. At the time of the experiment, it listed 2778 apartments in Frankfurt. The data encompassed information about the size of the living area, number of rooms, city districts, rent, ancillary costs, distance to the city center, availability of balcony or terrace, cellar, parking site, and a corresponding picture of the apartment.

The laboratory experiment followed a between-subject design and thus subjects were distributed to one of the four systems randomly. A short video explained the functionality of the DSS and described the experimental task. Each respondent was asked to find an apartment that would fit his or her preferences. Every DSS used the same database, so any differences in usage behavior, prediction accuracy, or user perceptions resulted from the experimental treatment (i.e., information about the DS and visualization type).

All systems logged detailed consumer behavior. The respondents evaluated the recommendations and the system after finishing their search. First, they indicated their visit probability for the top 10 recommended apartments (Task 3 in Fig. 2)<sup>4</sup>. Jamieson and Bass [47] provide evidence that the difference between stated purchase intentions and actual purchase behavior is smaller for durable than for non-durable goods. Since apartments are durable goods, we expect only a moderate difference between stated visit probabilities and actual visit behavior. In all the systems, the results (i.e., apartments)

Table 5  
Effect of decision space information on satisfaction with recommendations.

<table><tr><td>Treatment</td><td>First choice hit rate</td><td>Visit probability of the best expected apartment</td><td>Mean visit probability</td></tr><tr><td>System 1 (DSS)</td><td>29.8%</td><td>51.9%</td><td>43.7%</td></tr><tr><td>System 2 (+ textual support)</td><td>35.4%</td><td>60.2%***</td><td>47.1%</td></tr><tr><td>System 3 (+ 2D visual support)</td><td>53.1%***</td><td>68.1%***</td><td>52.1%**</td></tr><tr><td>System 4 (+ 3D visual support)</td><td>46.0%**</td><td>68.0%***</td><td>56.3%**</td></tr></table>

∗∗ p <sub>≤</sub> 0.01.  
∗∗∗ p <sub>≤</sub> 0.001.

appeared ordered by their estimated utility in a separate list, as described for the respondents in the introductory video. Second, they completed items related to their demographics, psychographics, experience level, and usage perceptions (Task 4 in Fig. 2). We used these data to evaluate consumers’ satisfaction with the recommendations and perceptions of the different systems.

## 5.3. Sample

We invited 480 prospective apartment seekers (i.e., persons that agreed that they are currently looking for a new apartment) from the Rhine-Main area (the area around Frankfurt/Main) to participate in our experiment, and 194 (40.4%) accepted. All of these participants completed the experimental task and subsequent questionnaire. We used a convenience sample and invited persons at multiple public places in the city of Frankfurt/Main. The persons were asked if they are willing to search for a new apartment as a participant in an experiment in cooperation with ImmobilienScout24.

The sample was evenly distributed across experimental treatments (47 in System 1, 48 in System 2, 49 in System 3 and 50 in System 4). The respondents’ average age was 24.8 years (min = 18, max = 65, SD = 6.8). In terms of gender, 94 respondents (48.5%) were women and 100 were men (52.5%). The respondents were very experienced Internet users (93.3% had used the Internet for more than five years), and 94.8% of the sample used the Internet daily. We found no significant differences with respect to these demographics across experimental groups.

## 5.4. Measures

We logged all interactions of our participants with the DSSs, including the number of times each user changed an attribute weight, the number of products considered from the recommendation set, and the time for the total search process. We also measured the users’ likelihood to visit the top 10 apartments on a sevenpoint scale. In line with Churchill and Surprenant [48], who asked for purchase probabilities to measure satisfaction with products, we interpreted self-stated visit probabilities for the top 10 apartments as the users’ satisfaction with the recommendations. Apartments with a visit probability greater than 50% formed the set of alternatives the consumer was considering seriously for rent. We measured the proportion of apartments in this set not dominated by other apartments<sup>5</sup>, which defined the objective decision quality [6], another indicator we used to evaluate our four DSSs.

We measured perceptions of the DSSs by the net promoter score and four constructs: perceived ease of use, perceived usefulness, reuse intentions, and end user satisfaction. We rely on these measures because recent research has proposed them for evaluating consumers’ satisfaction with DSSs [4,49]. We used seven-point Likert scales, ranging from 1 (fully disagree) to 7 (fully agree). We took the perceived ease of use and usefulness measures from Davis [50], end user satisfaction as defined by Au et al. [51], and the reuse intention measure from Chin et al. [52]. For the net promoter score, we relied on Reichheld [53].

## 6. Results

## 6.1. Satisfaction with recommendations

We asked participants to state the probability that they would visit the top 10 recommended apartments, to assess satisfaction with the recommendations. We computed several statistics based on the participants reported visit probabilities. The results are summarized in Table 5. The significance between System 1 and all other systems was tested with binomial tests; the results are also reported in Table 5.

Using self-stated visit probabilities, we also calculated the first choice hit rate, which reflects the percentage of users with the highest visiting probability for the apartment ranked first. All four systems performed better than the 10% chance criterion, and Systems 3 and 4 provided significantly better prediction accuracy than System 1 (see second column in Table 5). The increase of more than 20% for System 3 represents a huge increase in satisfaction with the first recommendation. We found no significant difference in terms of the first choice hit rate between users of System 3 and System 4, but a significant difference between Systems 2 and 3 (p = 0.010) and System 2 and System 4 (p = 0.092; tested with binomial tests).

Users of Systems 2, 3, and 4 also showed a higher visit probability of the best expected apartment (see third column in Table 5). Systems 3 and 4 lead to a significantly higher visit probability of the best expected apartment than Systems 1 and 2. We did not find a significant difference of this variable between Systems 3 and 4.

Users of Systems 3 and 4 evinced a significantly higher mean stated visit probability for the top 10 recommended apartments (see fourth column in Table 5). Users of System 4 furthermore showed a significantly higher mean stated visit probability for the top 10 apartments than users of System 2 (p = 0.013; tested with a binomial test). We did not found a significant difference between Systems 2 and 3 and Systems 3 and 4.

Although the set of apartments the participants were likely to visit grew larger with systems with visual support, we found fewer dominated alternatives in this set. The proportion of nondominated alternatives thus improved with systems that presented information about the DS. Users of System 1 considered only 47.9% non-dominated apartments; at least 10% more non-dominated apartments were likely to receive visits by users of Systems 2–4 (System 2 59.3%, System 3 62.2%, System 4 57.9%).

Table 6  
Impact of systems on perception measures

<table><tr><td rowspan="2">Treatment</td><td colspan="2">Perceived ease of use</td><td colspan="2">Perceived usefulness</td><td colspan="2">End user satisfaction</td><td colspan="2">Reuse intention</td><td colspan="2">Net promoter score</td></tr><tr><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td></tr><tr><td>System 1 (DSS)</td><td>5.97</td><td>0.99</td><td>5.25</td><td>1.34</td><td>4.89</td><td>1.32</td><td>5.36</td><td>1.38</td><td>7.19</td><td>2.48</td></tr><tr><td>System 2 (+ textual support)</td><td>6.00</td><td>0.72</td><td>5.70</td><td>1.17</td><td>5.42</td><td>1.06</td><td>5.94</td><td>0.94</td><td>8.44</td><td>1.77</td></tr><tr><td>System 3 (+ 2D visual support)</td><td>5.58</td><td>1.27</td><td>5.56</td><td>1.45</td><td>5.16</td><td>1.48</td><td>5.59</td><td>1.40</td><td>8.00</td><td>2.98</td></tr><tr><td>System 4 (+ 3D visual support)</td><td>5.74</td><td>1.15</td><td>5.66</td><td>1.44</td><td>5.27</td><td>1.42</td><td>5.69</td><td>1.37</td><td>7.86</td><td>2.76</td></tr></table>

## 6.2. Perceptions of the decision support systems

We also compared the consumers’ perceptions of the DSSs. Table 6 differentiates the perception measures by experimental treatments. The average scores indicate that systems that provided information about the DS outperformed the benchmark system in terms of perceived usefulness, end user satisfaction, reuse intentions, and net promoter scores.

Using our ordinal dependent variables (see Table 7), we estimated ordered Logit models, using maximum likelihood with robust standard errors. We incorporated users’ perceived ease of use as control variable in this model. Ease of use is determined by system-specific (e.g., objective usability) and user-specific (e.g., computer anxiety) variables [54,55]. Because we did not find significant differences between our systems in terms of perceived ease of use (p > 0.1; tested with ordered Logit regressions), its variance will be mainly explained by user-specific variables so we use it as a user-specific control variable and not as a variable that depends on the four implemented systems. In our analysis (see Table 7), we contrasted Systems 2, 3, and 4 against System 1.

Table 7 shows that all systems with information about the DS triggered significantly higher tendencies to engage in positive word-ofmouth processes. We additionally conducted ordered Logit regressions in which System 2, System 3, or System 4 were used as baseline. These regressions reveal that there are no significant differences in terms of user perceptions between Systems 2, 3, and 4. Analyzing the odds that users would be promoters or detractors yields some surprising magnitudes. Users with ratings of 9 and 10 on the net promoter scale (promoters) and those with ratings below 7 (detractors) can be distinguished from passive users who score 7 or 8 on the net promoter scale [53]. We estimated a Logit regression with our control and dummy variables and also calculated the odd ratios. The system exerted a significant impact on word-of-mouth activity, such that the odds of being a promoter increased especially when people used systems with visual support; specifically, they were three times higher for System 3 (p < 0.05) and 3.5 times higher for System 4 (p < 0.05) compared to System 1. We also observed a significantly lower tendency to engage in negative word-of-mouth about Systems 2 (odds ratio 0.366, $p \ < \ 0 . 0 5 )$ or 3 (odds ratio 0.376, $p \ < \ 0 . 0 5 )$ compared to System 1.

We found no significant difference in terms of any user perception construct between Systems 2 and 3, Systems 2 and 4 and Systems 3 and 4. The differences reported in Table 4 hence seem to merely be an effect of the information additionally provided by Systems 2–4.

## 6.3. Usage of the decision support systems

We found an improvement in terms of satisfaction with the recommendations as well as the DSS when information about the DS was available. We claim that these improvements are a result of the corrected conceptions of the DS which encouraged the participants to thoroughly deliberate their attribute weights. We hence investigated the specification of attribute weights and found that users in Systems 2–4 changed the default attribute weight of significantly more attributes (p < 0.05; tested with a Poisson regression) as shown in Fig. 3.

We furthermore found that users of Systems 2–4 specified a significantly lower weight for the attribute apartment rent (p < 0.05; tested with a Logit regression). Users of System 1 on average set

Table 7  
Effect of different systems on user perceptions.

<table><tr><td rowspan="2">Variable</td><td colspan="2">Perceived usefulness</td><td colspan="2">End user satisfaction</td><td colspan="2">Reuse intention</td><td colspan="2">Net promoter score</td></tr><tr><td>Est.</td><td>SD</td><td>Est.</td><td>SD</td><td>Est.</td><td>SD</td><td>Est.</td><td>SD</td></tr><tr><td>System 1</td><td>(Omitted)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>System 2 (+ Text)</td><td>0.658</td><td>0.356</td><td>0.837*</td><td>0.361</td><td>0.847*</td><td>0.353</td><td>0.869*</td><td>0.357</td></tr><tr><td>System 3 (+ 2D)</td><td>1.072**</td><td>0.367</td><td>1.060**</td><td>0.367</td><td>1.065**</td><td>0.365</td><td>1.266***</td><td>0.377</td></tr><tr><td>System 4 (+ 3D)</td><td>1.065**</td><td>0.357</td><td>0.895*</td><td>0.360</td><td>0.911*</td><td>0.359</td><td>0.862*</td><td>0.364</td></tr><tr><td>Perceived ease of use</td><td>0.974***</td><td>0.133</td><td>1.194***</td><td>0.142</td><td>1.161***</td><td>0.140</td><td>0.971***</td><td>0.144</td></tr><tr><td>Log likelihood</td><td></td><td>-546.2***</td><td></td><td>-523.2***</td><td></td><td>-480.8 ***</td><td></td><td>-392.8 ***</td></tr><tr><td>Pseudo R2</td><td></td><td>0.272</td><td></td><td>0.354</td><td></td><td>0.335</td><td></td><td>0.255</td></tr></table>

∗ p 0.05.  
$p \leq 0 . 0 1 .$  
$\begin{array} { r } { p \leq 0 . 0 0 1 . } \end{array}$

Please cite this article as: M. Scholz et al., Effects of decision space information on MAUT-based systems that support purchase decision processes, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.03.004

![](/api/attachments/SH3G3JV6/fulltext/images/ad55dfdc07d972576e1915c2f434837428d189a41851b0fb53b58ec344f1ba4e.jpg)  
Fig. 3. Average number of attribute weights not having the default value.

the attribute weight for rent to 6.36 (SD = 1.65) (on a scale ranging from 0 = totally unimportant to 8 = very important) whereas users of System 2 set the weight to 5.27 $( S D = 2 . 2 4 )$ , users of System 3 set the weight to 5.39 (SD = 1.69) and users of System 4 set the weight to 5.32 (1.77). Users of System 1 in total stated higher attribute weights than the users of the other systems although there is no significant difference between the weights of attributes other than rent. We interestingly found that users of Systems 2–4 defined attribute weights for rent and cellar with a lower difference than users of System 1 $( p < 0 . 1 0 ;$ tested with a Logit regression). Users of System 1 hence rather made a decision between giving a high weight to (low) rent or giving a high weight to have a cellar whereas users of Systems 2–4 did not. We indeed found a correlation of only 0.099 between high rental costs and the availability of a cellar indicating that users do not have to weigh between both attributes. Using a zero-truncated Poisson regression, we found that users of Systems 2–4 significantly $( p = 0 . 0 3 2 )$ less often re-started the process of specifying their preferences (i.e., defining aspiration levels and attribute weights) after they have considered the first recommendations.

Although we did not find significant differences in usage time (System 1: 42.10 min; System 2: 42.03 min; System 3: 44.29 min; System 4: 40.02 min; tested with a Gamma regression), we found a significantly higher number of apartment evaluations of the users of Systems 2–4 (p < 0.01; tested with a Poisson regression). Users of System 1 evaluated on average 8.04 distinct apartments $( S D = 7 . 4 0 ) ,$ users of System 2 evaluated 9.71 (SD = 4.04), users of System 3 9.61 $( S D = 4 . 5 5 )$ and users of System 4 12.00 apartments $( S D = 1 0 . 1 2 )$ Users of System 4 also evaluated significantly $( p < 0 . 0 1 ;$ tested with a Poisson regression) more distinct apartments than users of Systems 2 and 3.

## 7. Discussion

We conducted a series of experiments in order to demonstrate that decision makers often have misconceptions of the DS (i.e., the relations among the attributes resulting from the alternatives available on the market) and that this misconception influences decision makers’ expectations about available alternatives, the attribute weights they state in MAUT-based DSSs and finally their satisfaction with recommendations from such a DSS. Our findings indicate that decision makers typically do not correctly judge relations between product attributes. We complement existing research in demonstrating the impact of these misconceptions of the DS on the usage and satisfaction with MAUT-based DSS, a class of decision support systems that is often used in e-commerce [19,20] as well as other decision scenarios [16,17]. Existing MAUT-based DSS are not geared towards supporting the exploration of the DS; their focus are choices where the decision maker can be assumed to be well-informed about the DS [9,10].

We propose to address the problem of misconceptions of the DS by visually depicting the DS and offering users of a MAUT-based DSS the visualization when specifying attribute weights. We suggest visualizing the DS with a scatterplot that is generated from the multi-dimensional DS with dimensional reduction using singular value decomposition. We analyzed the impact of our proposed visualization on the perceptions and usage of MAUT-based DSSs as well as the satisfaction with recommendations from such DSSs in a large-scaled laboratory experiment. More specifically, we evaluated two variants of our proposed visualization, a 2D and a 3D visualization and compared these systems to a system with textual description of the DS and a system without information about the DS which currently constitutes the state-of-the-art solution. Significantly higher visit probabilities of the best expected apartment for those systems that provide information about the DS support the claim that incorrect expectations about recommendations lead to dissatisfaction with actual recommendations (see H3). Systems providing additional information about the DS furthermore improved objective decision quality; decision makers do consider Pareto-eficient alternatives with a higher probability.

Users perceived the systems with information about the DS as significantly more useful; they also were more satisfied with these systems and specified higher reuse intentions. This finding is in line with the improved satisfaction with recommendations of systems offering information about the DS and also supports H3. Our results also show that the information about the DS and not a visualization per se is responsible for an improvement of decision makers’ perceptions with the MAUT-based DSSs. The benefits of visualizing information about the DS also remain stable if the DS is visualized with a 3D scatterplot which indicates that interpreting the distances of attributes in a scatterplot helps decision makers to understand the DS and to form correct expectation about really existing alternatives. We furthermore found that users of the system without information about the DS stated significantly higher attribute weights, changed the default weight less often and made other trade-off decisions for the attributes rent and cellar. These findings indicate that information about the DS triggered decision makers to think seriously about their preferences and reconcile their attribute weights which supports H4.

Our results revealed that systems with textual support are slightly (but not statistically significant) better than the systems with visual support in terms of several user perceptions (see Table 7). This is not surprising given that our proposed visualization was new to the participants and given the higher complexity of our proposed visualization than a simple text. Despite the differences between 2D and 3D visualizations reported in recent research [41,42], we did not find a significant difference with respect to the consumers’ satisfaction with the recommendations and the consumers perception and usage of the DSS between our 2D and 3D systems. Our DSSs represented information about a DS that consisted of eight attributes and hence 28 attribute relations. A 2D visualization, although rather easy to interpret, might be not perceived as superior to a 3D visualization due to the high complexity of the DS and the lower information loss of depicting this highly complex DS with a 3D visualization. This argumentation is also underlined by recent research [56].

Xu et al. [57] already noted that information about the DS improves decision makers’ perceived decision quality and decision effort with a DSS that provides information about the DS. We complement this work by (a) developing a solution as a design artifact that is based on existing theories and literature, (b) empirically comparing three possible solutions, and (c) selecting the best suited solution (visualization with SVD) for a large-scaled empirically evaluation to demonstrate the impact of our proposed solution on the interaction and perception of a MAUT-based DSS for purchase decisions.

## 8. Implications

We contribute to research on decision support systems in two ways. First, we connect two streams of research: analyzing decision making behavior and designing decision support systems. Existing studies already provided evidence that decision makers often do have misconceptions of the DS [12,14]. Keeney [58] noted that a common mistake of designing (MAUT-based) DSSs is that decision makers do not correctly understand the DS. Our work confirms that decision makers often do not have a correct conception of the DS. We additionally show the impact of a misconception of the DS on the usage and satisfaction of a MAUT-based DSS. Decision makers need correct information about the DS in order to form realistic expectations about the alternatives that are available for them. These expectations decide about the decision makers’ satisfaction and future use of a DSS. Decision makers furthermore might state other attribute importance weights when having a correct conception of the DS. Since decision makers have more realistic expectations about the available alternatives when they have a correct conception of the DS, their stated attribute weights are more reliable and stable. This is evinced by significantly less re-specifications of the attribute weights of the participants that used a DSS with information about the DS.

Second, we suggest a method to enhance DSSs and afirm that information about the DS can be presented in either textual or visual form. Our proposed visualization improves the probability that decision makers will adopt the recommendation. The applicability of a visualization based on SVD is confirmed by our application to a concrete business case, in which visual information about the DS most improved decision makers’ satisfaction with recommendations. Ultimately, the DSS with our proposed visualization yielded the highest values in terms of satisfaction with the recommendations. Users of systems with visual support revealed an approximately 16% higher probability to visit the apartment recommended on top 1 when compared to users of the system without information about the DS.

Our results offer interesting implications for consumers and providers of DSSs. Consumers can attain greater satisfaction with the recommendations, higher usefulness, end user satisfaction, reuse intentions, and willingness to spread positive word-of-mouth if the systems offer them information about the DS. These results are interesting, considering that our proposed extension did not reduce the perceived ease of use of the DSSs. That is, the improvements in terms of satisfaction with recommendations and user perceptions of the DSSs derived from additionally provided information about the DS.

Information about the DS also helped consumers lowering their risk of selecting an alternative dominated by another alternative. We found a respectable increase of at least 10% more non-dominated alternatives in the set of apartments that the participants were likely to visit when using any of the systems that provided additional information about the DS.

For providers of DSSs, we found at least a 8.3% higher probability to visit the top recommended apartment when additional information about the DS was available. With a visual presentation of the information about the decision space, consumers expressed a 16% higher probability to visit the top recommended apartment and at least a 8.4% higher probability to visit any of the top 10 recommended apartments. Integrating information about the DS also affected word-of-mouth activities, including a lower probability of negative word-of-mouth for the systems that offered additional information. Consumers using systems with visual support were three times more likely to act as promoters of the service than consumers using the system without information about the decision space.

These effects can be directly related to the information about the DS and are very desirable from a DSS provider’s point of view. Improving the consumers’ satisfaction with recommendations has the potential to improve the consumers’ willingness-to-pay [59] and increase sales [60]. Further, acquiring new customers is more costly than retaining old customers [61]. Our proposed system helps to increase customer lifetime in two ways. First, it minimizes the effort needed to retain customers, reduces choice deferral, and enhances the acquisition of new customers through higher usefulness, end user satisfaction, and reuse intentions. Second, the proposed system improves the probability that existing customers help to acquire new customers.

## 9. Limitations and future research

Our study is subject to some limitations. We could not test for long-run effects, so our finding that information about the DS enhances the consumers’ satisfaction with both the recommendations and the DSS might be a short-term effect that diminishes over time. However, we have no reason to believe that additional information would only have a short-term effect.

The improvements we found in both, satisfaction with the recommendations and perceptions of the DSS, suggest that the proposed extension to DSSs might enhance sales. Consumers’ willingnessto-pay significantly depends on the amount of inappropriate recommendations [59]; our findings add that this level of error can be reduced by integrating information about the DS in a DSS, which then should improve their willingness-to-pay. Examining the effects on sales represents, however, an interesting avenue for research.

Measuring attribute weights is a key task in many applications such as DSSs or conjoint analysis. Recent literature offers evidence that the application of different methods for measuring attribute weights leads to significantly different attribute weights for the same consumer [62–64]. Misconceptions of the DS also might explain the inconsistencies in the specifications of attribute weights across different methods. Integrating information about the DS should help measure attribute weights more reliably and thus reduce differences between the results of different methods.

Users’ perceptions with the MAUT-based DSS have been found to be higher when using a visualization of the DS than when giving no information about the DS. The standard deviations of the users’ perceptions are, however, also highest for the systems with visual support. There is hence a high amount of users that is rather not satisfied and that would rather not reuse or recommend a MAUT-based DSS with a visual depiction of the DS. We found support that the users who perceived the DSS with visual support as not easy to use also expressed a low perceived usefulness and a low satisfaction with the system and these users are not very likely to act as promoters or reuse the system in future<sup>6</sup>. To make handling the systems with visual support easier, we can for example highlight the relations to other attributes of the attribute for which the user is currently specifying her importance weight. Improving the ease of use is hence the primary challenge to further improve the benefits of our proposed visualization of the DS.

1. Step: Select district/town and state optional criteria >> 2. Step: Weigh criteria

![](/api/attachments/SH3G3JV6/fulltext/images/2c35000b2193c180695c0b1e3b723d6a243a23a9e3b1e1af36ce696d7247d221.jpg)  
Fig. 4. Translated mock-up of System 1.

1. Step: Select district/town and state optional criteria >> 2. Step: Weigh criteria  
![](/api/attachments/SH3G3JV6/fulltext/images/1143b02649b5945c1decddb3a914b75c2e9646c4ee748712dd204999d8b97ac3.jpg)  
Fig. 5. Translated mock-up of System 2.

Please cite this article as: M. Scholz et al., Effects of decision space information on MAUT-based systems that support purchase decision processes, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.03.004

1. Step: Select district/town and state optional criteria >> 2. Step: Weigh criteria

![](/api/attachments/SH3G3JV6/fulltext/images/d6994dfb515cfcf70b297971787518a48d2d16faac19f1d4986c675a14f2764a.jpg)  
Fig. 6. Translated mock-up of System 3.

1. Sten: Select district/town and state ontional criteria >> 2. Sten: Weigh criteria  
![](/api/attachments/SH3G3JV6/fulltext/images/1fbfe187bd30f6eb345c81b347dba4478948b94cd6ed2e966f60f276cf8b7224.jpg)  
Fig. 7. Translated mock-up of System 4.

Please cite this article as: M. Scholz et al., Effects of decision space information on MAUT-based systems that support purchase decision processes, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.03.004

## References

[1] Amazon, Movies & TV : Blu-ray : Kids & Family : Last 90 days, 2016. http:// www.amazon.com.

[2] R. Grenci, P. Todd, Solutions-driven marketing, Commun. ACM 45 (2) (2002) 64–71.

[3] H. van der Heijden, Mobile decision support for in-store purchase decisions, Decis. Support. Syst. 42 (2) (2006) 656–663.

[4] B. Xiao, I. Benbasat, E-commerce product recommendation agents: use, characteristics, and impact, MIS Q. 31 (1) (2007) 137–209.

[5] B. Dellaert, G. Häubl, Searching in choice mode: consumer decision processes in product search with recommendations, J. Mark. Res. 49 (2) (2012) 277–288.

[6] G. Häubl, V. Trifts, Consumer decision making in online shopping environments: the effects of interactive decision aids, Mark. Sci. 19 (1) (2000) 4–21.

[7] K. Van Ittersum, J. Pennings, B. Wansink, H. Trijp, The validity of attribute-importance measurement: a review, J. Bus. Res. 60 (11) (2007) 1177–1190.

[8] J. Song, D. Jones, N. Gudigantala, The effects of incorporating compensatory choice strategies in web-based consumer decision support systems, Decis. Support. Syst. 43 (2007) 359–374.

[9] E. Karniouchina, W. Moore, B. van der Rhee, R. Verma, Issues in the use of ratings-based versus choice-based conjoint analysis in operations management research, Eur. J. Oper. Res. 197 (1) (2009) 340–348.

[10] N. Schuwirth, P. Reichert, J. Lienert, Methodological aspects of multi-criteria decision analysis for policy support: a case study on pharmaceutical removal from hospital wastewater, Eur. J. Oper. Res. 220 (2) (2012) 472–483.

[11] S. Wood, J. Lynch, Prior knowledge and complacency in new product learning, J. Consum. Res. 29 (3) (2002) 416–426.

[12] A. Xu, R. Wyer, Puffery in advertisements: the effects of media context, communication norms, and consumer knowledge, J. Consum. Res. 37 (2) (2010) 329–343.

[13] W.T. Tan, C.H. Tan, H.H. Teo, Consumer-based decision aid that explain which to buy: decision confirmation or overconfidence bias? Decis. Support. Syst. 53 (1) (2012) 127–141.

[14] J. Bettman, E. Johnson, M. Luce, J. Payne, Correlation, conflict, and choice, J. Exp. Psychol. 19 (4) (1993) 931–951.

[15] S. Gregor, I. Benbasat, Explanations from intelligent systems: theoretical foundations and implications for practice, MIS Q. 23 (4) (1999) 497–530.

[16] J. Dyer, P. Fishburn, R. Steuer, J. Wallenius, S. Zionts, Multiple criteria decision making multiattribute utility theory: the next ten years, Manag. Sci. 38 (5) (1992) 645–654.

[17] J. Wallenius, J. Dyer, R. Fishburn, R. Steuer, S. Zionts, K. Deb, Multiple criteria decision making, multiattribute utility theory: recent accomplishments and what lies ahead, Manag. Sci. 54 (7) (2008) 1336–1349.

[18] N. Yang, X. Liao, W.W. Huang, Decision support for preference elicitation in multi-attribute electronic procurement auctions through an agent-based intermediary, Decis. Support. Syst. 57 (2014)

[19] S. Huang, Designing utility-based recommender systems for e-commerce: evaluation of preference-elicitation methods, Electron. Commer. Res. Appl. 10 (4) (2011) 398–407.

[20] M. Scholz, V. Dorner, M. Franz, O. Hinz, Measuring consumers willingness– to-pay with utility-based recommendation systems, Decis. Support. Syst. 72 (2015) 60–71.

[21] M. Scholz, V. Dorner, G. Schryen, A. Benlian, A configuration-based recommender system for supporting e-commerce decisions, Eur. J. Oper. Res. 259 (1) (2017) 205–215.

[22] J. Muth, Rational expectation and the theory of price movements, Econometrica 29 (3) (1961) 315–335.

[23] Y. Au, R. Kauffman, What do you know? Rational expectation in information technology adoption and investment, J. Manag. Inf. Syst. 20 (2) (2003) 49–76.

[24] R. Oliver, A cognitive model of antecedents and consequences of satisfaction decisions, J. Mark. Res. 17 (4) (1980) 460–469.

[25] T. Kramer, The effect of measurement task transparency on preference construction and evaluations of personalized recommendations, J. Mark. Res. 44 (2) (2007) 224–233.

[26] S. Brown, V. Venkatesh, S. Goyal, Expectation confirmation in technology use, Inf. Syst. Res. 23 (2) (2012) 474–487.

[27] I. Vessey, D. Galletta, Cognitive fit: an empirical study of information acquisition, Inf. Syst. Res. 2 (1) (1991) 63–84.

[28] A. MacEachren, F. Hardisty, X. Dai, L. Pickle, Supporting visual analysis of Federal Geospatial Statistics, Commun. ACM 46 (1) (2003) 59–60.

[29] J. Gettinger, E. Kiesling, C. Stummer, R. Vetschera, A comparison of representations for discrete multi-criteria decision problems, Decis. Support. Syst. 54 (2013) 976–985.

[30] J. Chambers, W. Cleveland, B. Kleiner, P. Tukey, Graphical Methods for Data Analysis, Wadsworth & Brooks, Belmont, 1983.

[31l R. Feldman. Filled radar charts should not be used to compare social indicators Soc Indic Res, 111 (3) (2013) 709–712

[32] C. Theetranont, P. Haddawy, D. Krairit, Integrating visualization and multi--attribute utility theory for online product selection, International Journal of Information Technology & Decision Making 6 (4) (2007) 723–750

[33] S. Moorthy, B. Ratchford, D. Talukdar, Consumer information search revisited: theory and empirical analysis, J. Consum. Res. 23 (4) (1997) 263–277.

[34] S. Roweis, L. Saul, Nonlinear dimensionality reduction by locally linear embedding, Science 290 (5500) (2000)2323–2326

[35] L. Zhang, J. Marron, H. Shen, Z. Zhu, Singular value decomposition and its visualization, J. Comput. Graph. Stat. 16 (4) (2007) 833–854.

[36] I. Jolliffe, Principal Component Analysis, Springer, Heidelberg, 2002.

[37] M. Kagie, M. van Wezel, P. Groenen, A graphical shopping interface based on product attributes, Decis. Support. Syst. 46 (1) (2008) 265–276.

[38] W. Härdle, L. Simar, Applied Multivariate Statistical Analysis, Springer, Heidelberg, 2003.

[39] M. Greenacre, Correspondence Analysis and Practice, Chapman & Hall, Boca Raton, 2007.

[40] J. Baker, D. Jones, J. Burkman, Using Visual Representations of Data to Enhance Sensemaking in Data Exploration Tasks, J. Assoc. Inf. Syst. 10 (7) (2009) 533–559.

[41] K. Kim, R. Proctor, G. Salvendy, Comparison of 3D and 2D menus for cell phones, Comput. Hum. Behav. 27 (5) (2011) 2056–2066.

[42] F.H. Nah, B. Eschenbrenner, D. DeWebster, Enhancing brand equity through flow and telepresence: a comparison of 2D and 3D virtual worlds, MIS Q. 35 (3) (2011) 731–747.

[43] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of state-of-the-art and possible extensions, IEEE Trans. Knowl. Data Eng. 17 (6) (2005) 734–749.

[44] T. Gilbride, G. Allenby, A choice model with conjunctive, disjunctive, and compensatory screening rules, Mark. Sci. 23 (3) (2004) 391–406.

[45] J. Hauser, B. Wernerfelt, An evaluation cost model of consideration sets, J. Consum. Res. 16 (4) (1990) 393–408.

[46] C. Schlereth, C. Eckert, R. Schaaf, B. Skiera, Measurement of preferences with self-explicated approaches: a classification and merge of trade-off- and non– trade-off-based evaluation types, Eur. J. Oper. Res. 238 (1) (2014) 185–198.

[47] L. Jamieson, F. Bass, Adjusting stated intention measures to predict trial purchase of new products: a comparison of models and methods, J. Mark. Res. 26 (3) (1989) 336–345.

[48] G. Churchill, C. Surprenant, An investigation into the determinants of customer satisfaction, J. Mark. Res. 19 (4) (1982) 491–504.

[49] S. Al-Natour, I. Benbasat, R. Cenfetelli, The adoption of online shopping assistants: perceived similarity as an antecedent to evaluation beliefs, J. Assoc. Inf. Syst. 12 (5) (2011) 347–374.

[50] F. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Q. 13 (3) (1989) 319–340.

[51] N. Au, E. Ngai, T. Cheng, Extending the understanding of end user information systems satisfaction formation: an equitable needs fulfillment model approach, MIS Q. 32 (1) (2008) 43–66.

[52] W. Chin, N. Johnson, A. Schwarz, A fast form approach to measuring technolog acceptance and other constructs, MIS Q. 32 (4) (2008) 687–703.

[53] F. Reichheld, The one number you need to grow, Harv. Bus. Rev. 81 (12) (2003) 46–54.

[54] N. Basoglu, T. Daim, E. Polat, Exploring adaptivity in service development: the case of mobile platforms, J. Prod. Innov. Manag. 31 (3) (2004) 501–515.

[55] V. Venkatesh, Determinants of perceived ease of use: integrating control, intrinsic motivation, and emotion into the technology acceptance model, Inf. Syst. Res. 11 (4) (2000) 342–365.

[56] M. Franz, M. Scholz, O. Hinz, 2D versus 3D visualizations in decision support the impact of decision makers' perceptions Proceedings of the 36th international conference on information systems. 2015.

[57] J. Xu, I. Benbasat, R. Cenfetelli, The nature and consequences of trade-off transparency in the context of recommendation agents, MIS Q. 38 (2) (2014) 379-406

[58] R. Keeney, Common mistakes in making value trade-offs, Oper. Res. 50 (6) (2002) 935–945.

[59] G. Adomavicius, J. Bockstedt, S. Curley, J. Zhang, Effects of online recommendations on consumers’ willingness to pay, Proceedings of the 6<sup>th</sup> ACM conference on recommender systems, 2012.

[60] J. Van Doorn, P. Leeflang, M. Tijs, Satisfaction as a predictor of future performance: a replication, Int. J. Res. Mark. 30 (3) (2013) 314–318

[61] P.Y. Chen, L. Hitt, Measuring switching costs and the determinants of customer retention in internet-enabled businesses: a study of the online brokerage industry, Inf. Syst. Res. 13 (3) (2002) 255–274.

[62] J. Louviere, T. Islam, A comparison of importance weights and willingness-to– pay measures derived from choice-based conjoint, constant sum scales and best-worst scaling, J. Bus. Res. 61 (9) (2008) 903–911.

[63] M. Pöyhönen, R. Hämäläinen, On the convergence of multiattribute weighting methods, Eur. J. Oper. Res. 129 (3) (2001) 569–585.

[64] E. Triantaphyllou, S.H. Mann, An examination of the effectiveness of multi-dimensional decision-making methods: a decision-making paradox, Decis Support. Syst. 5 (3) (1989) 303–312.

[65] D. Gefen, E. Karahanna, D. Straub, Trust and TAM in online shopping: an integrated model, MIS Q. 27 (1) (2003) 51–90.

[66] W. Wang, I. Benbasat, Trust in and adoption of online recommendation agents, J. Assoc. Inf. Syst. 6 (3) (2005) 72–101.

Michael Scholz (1981) studied Information Systems at the Martin-Luther-University Halle/Wittenberg with main focus on Software Engineering and Information Management. After receiving his diploma (equiv. master degree) he started working as a Research Assistant at the Chair of Business Informatics II at the University of Passau. He received his Ph.D. in December 2009. Since May 2010 he is an Assistant Professor at the University of Passau.

Michael’s research has been published in journals such as Decision Support Systems (DSS), Journal of Multi-Criteria Decision Analysis, Business & Information Systems Engineering (BISE) or Electronic Markets (EM) and in several conference proceedings. His research focuses on e-commerce technologies and their economic impact.

Markus Franz (1984) studied economics at the Johann Wolfgang Goethe-University of Frankfurt. The focus of his studies was on Marketing and Finance. In January of 2011 he finished university with a diploma in business administration. His final thesis, “Visualizing product spaces in recommendation agents via correspondence analysis”, empirically investigates the influence of graphical information provision on search performance and loyalty of recommendation system users.

He gained practical experiences in the market research department of the Arcor AG & Co. KG. Since April 2011 he is staffed as Research Assistant at the Chair of Business Informatics especially Electronic Markets.

Oliver Hinz (1974) studied at the TU Darmstadt Business Administration and Infor mation Systems with main focus on Marketing, Software Engineering and Computer Graphics. After receiving his diploma (equiv. master degree) he worked several years for the Dresdner Bank as a consultant for business logic.

Oliver started working as a Research Assistant in March 2004 at the Chair of Electronic Commerce and received his Ph.D. in October 2007. Oliver Hinz joined the Marshall School of Business (University of Southern California) as visiting scholar for 4months and received the SinnerSchrader stipend (10.000 EUR) for young researcher for 2007. He has also been awarded with the dissertation prize of the Alcatel-Lucent-Stiftung 2008, the Erich-Gutenberg-Prize 2008 and the science prize “Retailing 2009” of the EHI Retail Institute. He is also the winner of the honorable Schmalenbach prize for young researchers in 2008.

He supported the E-Finance Lab as Assistant Professor for E-Finance & Electronic Markets, joined the TU Darmstadt in April 2011 and heads the Chair of Information Systems — Electronic Markets. Oliver’s research has been published or is forthcoming in journals like Information System Research (ISR), Management Information Systems Quarterly (MISQ), Journal of Marketing (JM), European Journal of Operational Research (EJOR), Journal of Management Information Systems (JMIS), Decision Support Systems (DSS), Journal of Business Research, Electronic Markets (EM), Business & Information Systems Engineering (BISE) and in a number of proceedings.

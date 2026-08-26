---
otero_id: 9808
otero_key: "9X3HNAX3"
title: "Multi-criteria decision techniques for context-aware B2B collaboration in supply chains"
authors: "P.S. Tan; S.S.G. Lee; A.E.S. Goh"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.11.013"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Multi-criteria decision techniques for context-aware B2B collaboration in supply chains

P.S. Tan <sup>a,</sup>⁎, S.S.G. Lee <sup>b</sup>, A.E.S. Goh <sup>c</sup>

<sup>a</sup> Singapore Institute of Manufacturing Technology (SIMTech), Singapore

<sup>b</sup> School of Mechanical and Aerospace Engineering, Nanyang Technological University, Singapore

<sup>c</sup> School of Computer Engineering, Nanyang Technological University, Singapore

## a r t i c l e i n f o

Available online 22 November 2011

Keywords: Decision support Multi-criteria decision making (MCDM) Context-aware Supply chain

## a b s t r a c t

In today's rapidly changing environment, B2B collaboration technologies are crucial to support the growing complexity and diversity of supply chains. This paper proposes a multi-criteria decision making (MCDM) technique, Deviation Measure, to support decision making in context-aware B2B collaboration. Empirical investigations to compare this proposed technique against other short-listed MCDM techniques were conducted. The completeness of ranking results, stability and robustness of the ranking sequence when new alternatives are introduced was investigated. The tests also examined the sensitivity of the sequence to changing weights in the criteria used. Results showed that the Deviation Measure technique is the best.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Today, businesses operate in value chains to bene<sup>fi</sup>t from competitive advantage through shorter time-to-market, shortened cycle times and enhanced customer service [36]. As manufacturing moves from North America and Western Europe to Asia, the present-day globalized supply chain and networked economy is more complex, as supply chain partners are geographically dispersed [12]. Multi-national corporations (MNCs) that do business with hundreds of trading partners, often small-medium sized enterprises (SMEs), dictate their terms as supply chain masters [8,16]. Research works in the area of collaborative supply chains attempted to improve the competitive advantage of such supply chains by taking a holistic perspective of entire supply chains [3]. As part of such research, performance measurements of key parameters of the supply chain components are often identi<sup>fi</sup>ed and measured. These parameters often numerous, have different degrees of in<sup>fl</sup>uence on the supply chain performance, thereby necessitating multi-criteria approaches towards deriving the measures. Multi-Criteria Decision Making (MCDM) techniques have been used in many such performance measurements as MCDM are useful in identifying and evaluating compatible alternatives (or solutions) in decision support tools for such supply chains [22]. As part of such research efforts, the ability to dynamically identify and connect potential partners is a key enabler of a synchronized or collaborative supply chain [21]. Partners can be identi<sup>fi</sup>ed either by a restricted search (e g. those who have been pre-quali<sup>fi</sup>ed earlier) or by an open search.

Most Business to Business (B2B) activities are process-governed but dominated by the exchange of business documents. In a typical supply chain, examples of such documents include purchase orders (POs), goods receive notes (GRNs) and advance shipment notes (ASNs). These documents are rich in contextual information such as a company's name, address, date of delivery (or receipt), the status of an invoice, and inventory level. Such contextual information is invaluable for supporting B2B collaboration, for example identifying and matching suitable partners, as they are used in the decision making process. The context-aware approach in B2B collaboration is not the subject of this paper; more information may be found in [40]. Given the challenges outlined earlier, this paper discusses how quantitative decision technique(s) may be deployed to support context-aware B2B collaboration in supply chains.

Section 2 provides a brief overview of multi-criteria decision making (MCDM), its relevance to B2B collaboration to support supply chains in general, and supplier selection in particular. Section 3 outlines the important considerations for context-aware decision support using MCDM techniques, in particular for B2B collaboration. An evaluation framework previously proposed [39] is also brie<sup>fl</sup>y discussed, together with the outcome of an initial assessment. Section 4 then discusses the proposed new MCDM technique, namely Deviation Measure. Next, Section 5 presents an empirical analysis of the performance of the proposed Deviation Measure, with other short-listed MCDM techniques using four metrics discussed in Section 3. Lastly, conclusions are presented in Section 6, with a brief discussion on future work.

## 2. MCDM techniques for supply chain collaboration

## 2.1. Overview

Decision Making “identi<sup>fi</sup>es and chooses alternatives based on the values and preferences of the decision maker” [19]. Typically, decision making involves multiple criteria, having several values and preferences, which cannot be simply combined into a single aggregate measure. This class of decision making – Multiple Criteria Decision Making (MCDM) – has three key decision variables, namely alternatives, decision criteria and decision type [4,5,31].

## 2.1.1. Alternatives

MCDM alternatives must generally embody potential actions, which are either feasible or of considerable interest [33]. For instance, some B2B partners that are unable to supply the product of current interest are infeasible partners.

## 2.1.2. Decision criteria

The goals of decision making may be gauged by decision criteria [15]. In this work, the criteria are also the context of the decision making, for example, cost and lead-time. Criteria are assessed by two commonly encountered scales: qualitative and quantitative [17]. The qualitative scale can be either a verbal or a non-numerical scale, such as Hot, Warm or Cold, whereas a quantitative scale is selfexplanatory (e.g. weight (50 kg), or price (\$20.00) of a product).

Some criteria, however, may not be qualitative or quantitative by nature. Such criteria – known as nominal criteria – scores an alternative unity (1) if its property matches the preferred value and zero otherwise. For example, if the decision maker speci<sup>fi</sup>es that the criteria “Source Country” has the preferred value “China”, then it is either a full match (score of 1) or a no match (0). For B2B collaboration, it is imperative to be able to model these three types of criteria.

## 2.1.3. Decision type

Roy [33] identi<sup>fi</sup>ed the three most commonly encountered decision types in MCDM:

(i) Choice: Determine a minimal subset, $A _ { 0 }$ of the available alternatives, A, that can justify the elimination of all other alternatives A\A [32], where members are considered indifferent.

(ii) Classification: Assign each action of A to the most appropriate pre-de<sup>fi</sup>ned category. The categories may be de<sup>fi</sup>ned based on the expected actions (e.g. Approve, Reject, or KIV), or on the qualitative judgments (e.g. Good, Average, or Bad).

(iii) Ranking: Build a complete or partial pre-order on A based on the degree by which each alternative satis<sup>fi</sup>es the decision criteria.

## 2.2. Related work

MCDM techniques have been widely adopted in many different aspects of supply chain management. Evaluating investments [28], designing metrics framework for different types of SC designs [1], risks and corporate responsibility associated with supply chains's footprint [11] and order quantity allocation [17] are a few examples of the varied applications of MCDM techniques.

In B2B collaboration for synchronized and dynamic supply chains, one of the key activities is identifying partners or suppliers [21]. In this respect, MCDM techniques such as AHP (Analytic Hierarchy Process), PROMETHEE (Preference Ranking Organization METHod for Enrichment Evaluation) and DEA (Data Envelopment Analysis) have been used [21]. With the advances in computational capabilities, other computer intensive methods like ANP (Analytic Network Process), a counter-part of AHP, VIKOR (VlseKriterijumska Optimizacija

I Kompromisno Resenje), TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) [26] and fuzzy methods to create integrated or hybrid techniques, began to emerge [20,24,47]. Work on various forms of classical optimization techniques such as linear programming, mix-integer programming or goal programming has also been reported [20,21,27]. Sometimes these mathematical programming techniques are used in conjunction with traditional MCDM techniques [2,13,24,43]. Then they are others who explored the use of non-classical algorithms such as evolutionary algorithms like genetic algorithms [25] or even Modern Portfolio Theory [23]. In a review by Ho et al. [20] across 78 recent papers, DEA and AHP were highlighted as the two most popular techniques. However, each has its own drawbacks. AHP's drawback for example, has been discussed extensively [14,44].

In this paper, the focus is on the use of MCDM techniques to support context-aware B2B collaboration. For B2B collaboration in supply chains, decision making typically involves choosing the best option from a list of ranked options. Classification groups similar alternatives according to pre-de<sup>fi</sup>ned characteristics, whereas Choice groups alternatives but does not rank them). Neither classification nor choice is suited for B2B decision making, which involves choosing the best or the second best option. As such, only ranking is relevant to this work. The next section discusses the parameters pertinent to MCDM ranking decisions.

## 3. Identifying suitable MCDM techniques

There are many MCDM techniques, each designed to solve different types of problems. The two main classes of techniques in MCDM are Multi-Attribute Utility Theory (MAUT) techniques and Outranking techniques [33]. This section identi<sup>fi</sup>es suitable technique(s) to support context-aware B2B collaboration.

## 3.1. Important considerations in B2B collaboration

Before suitable MCDM techniques can be identi<sup>fi</sup>ed, the primary characteristics of B2B collaboration must <sup>fi</sup>rst be understood:

• Typically, ideal values are unknown; only acceptable or preferred values are known (e.g. The maximum cost per unit may be \$10.00, but a cheaper option is always “preferred”, everything else being equal)

• The criteria or context of collaboration is known, with their relative importance determinable [34] (e.g. Cost is the most important factor, followed by lead-time)

• Τhe criteria have different units of measure (e.g. 4 days for leadtime and \$10.00 for cost).

In addition, from a context-aware decision making viewpoint, other important considerations, includes [40]:

• Ability to automatically handle different types of context information (quantitative, qualitative and nominal)

• Minimize the frequency of interaction between decision maker and technique, so that processing can be automated once the criteria (context of collaboration) and their relative importance are identi<sup>fi</sup>ed

• Minimize the number of assumptions adopted (e.g. thresholds identi<sup>fi</sup>cation) as such assumptions can potentially skew the <sup>fi</sup>nal ranking result.

3.2. An evaluation framework for identifying suitable MCDM techniques

An evaluation framework based on these considerations is proposed [39]. This framework has 3 major features:

• Ease of Model Formulation. There are 6 considerations in this category, namely criteria type support, criteria weights determination, criteria data usage and normalization, preference elicitation steps and <sup>fi</sup>nal ranking robustness.

• Ease of automation. There are 3 considerations — level of human interaction, the assumptions used in the technique and data scaling requirements.

• Quality of Solution consists of 4 quantitative metrics that assess each MCDM technique according to rank completeness, stability and sensitivity to changes. These metrics are the basis for the empirical investigations of this paper.

(1) Rank completeness — quanti<sup>fi</sup>es the completeness of the ranking based on the number of unique rankings obtained from possible alternatives:

Rankcompleteness; $w = \ L ^ { n _ { u } } / _ { n _ { t } }$

ð<sup>1</sup>Þ

where

$n _ { u }$ number of unique ranks

nt total number of alternatives.

(2) Rank correlation — measures the stability of the solution when new alternatives are introduced. Two ranking sequences are compared using Pearson's rank correlation, ρ, which is based on Pearson's product–moment correlation coef<sup>fi</sup>cient [10]:

$$
\rho = \frac {n \sum x _ {i} y _ {i} - \sum x _ {i} \sum y _ {i}}{\sqrt {n \sum x _ {i} ^ {2} - (\sum x _ {i}) ^ {2}} \sqrt {n \sum y _ {i} ^ {2} - (\sum y _ {i}) ^ {2}}}\tag{2}
$$

where

x position in original rank sequence X

Y complete rank sequence with new alternatives

yi position in new rank sequence Y′

n number of alternatives in each sequence (same for both) Y′ Y\X.

This measure can also be used to measure the degree of correlation of two ranks obtained from different MCDM techniques.

(3) Rank reversal, θ — assesses the robustness of the solution based on the similarity between two sequences. Instead of measuring the correlation, it measures the degree of disagreement caused by rank reversal, θ. For this, the Spearman's foot-rule distance, $d _ { n }$ which measures the absolute distance (representing the disagreement) between two ranks is adopted [30]:

$$
d _ {n} = \sum_ {i = 1} ^ {n} | x _ {i} - y _ {i} |.\tag{3}
$$

This is similar to the Manhattan distance used for quantitative variables in data mining [18]. To measure the degree of disagreement between two ranks, caused by rank reversal, θ,the following is used:

$$
\theta = \frac {d _ {n}}{d _ {n - \max}}\tag{4}
$$

where $d _ { n - m a x } =$ maximum distance between two rankings of n-length. When there is no tied rank, the maximum foot-rule distance can be generalized to:

$$
d _ {n - \max} = 2 \times \left[ \frac {n}{2} \right] \times \left(\left(r e \left(\frac {n}{2}\right) + 1\right) + \left(\left[ \frac {n}{2} \right] - 1\right)\right)\tag{5}
$$

When there are tied ranks, the maximum foot-rule distance can be generalized to:

$$
d _ {n - \max} = \frac {(n - 1) (n - 2)}{2}\tag{6}
$$

The derivations of Eqs. (5) and (6) are not discussed in this paper [37].

(4) Sensitivity Analyses — gauges a technique's sensitivity to changes of the weights of the criteria re<sup>fl</sup>ecting changes in the decision maker's preferences. This is typically done graphically as discussed in Section 5.

## 3.3. Techniques assessed

Two classes of MCDM techniques, namely MAUT (Multi-Attribute Utility Theory) and Outranking, were assessed for their suitability to support context-aware B2B collaboration. The assessments were made using the considerations in the Ease of Model Formulation and Ease of Automation metrics of the evaluation framework. The techniques evaluated were:

• MAUT class — AHP [35], VIKOR [9,29] and TOPSIS [9,29]

• Outranking class — ELECTRE II (ELimination Et Choix Traduisant la REalité or Elimination and Choice Expressing Reality), ELECTRE III [31,32] and PROMETHEE II (Preference Ranking Organization METHod for Enrichment Evaluation) [7].

The Outranking techniques ELECTRE II and PROMETHEE II were short-listed as possible candidate techniques [39]. However, no MAUT techniques were deemed suitable. Arising from this, a new MAUT technique was proposed.

## 4. The deviation measure technique

From a context-aware B2B collaboration viewpoint, the criteria speci<sup>fi</sup>ed by a decision maker (e g: price and lead-time) are termed as preferred values. Any deviation from these values can be positive (e.g. lower price) or negative (e.g. longer lead-time), as illustrated in Fig. 1.

This deviation measure and the subsequent elicitation steps can be easily automated, and the context information values from the B2B Context Model [38] can be used directly. This limits user intervention to the selection of criteria (collaboration context) and weights determination only. This deviation measure can be structured into a series of elicitation steps, where the different units of measure are normalized linearly so that the performance values of different criteria can be aggregated, to obtain the Overall Suitability Score (OSS). The weight of each criterion is incorporated in the calculation of the Individual Criterion Score (ICS), see Step (3) below. The AHP pair-wise comparison is adopted to determine the weights of the criteria, as the Process is well proven for this purpose. This mimics industry practice well. The highest ranked alternative based on the OSS values is the best alternative.

The elicitation steps of the Deviation Measure technique are:

(1) Determine the weights of the criteria, w ascertained by AHP pair-wise comparison, where for n criteria

$$
\sum_ {i = 1} ^ {n} w _ {i} = 1
$$

(2) Calculate the normalized performance matrix The normalized performance value of the i-th criterion in the jth alternative, $p _ { i } ( a _ { j } )$ is computed by applying he deviation measure

$$
p _ {i} \left(a _ {j}\right) = \left\{ \begin{array}{l} \left(\frac {g _ {i} ^ {*} - g _ {i} (a j)}{g _ {i} ^ {*}}\right) \\ \left(\frac {g _ {i} (a j) - g _ {i} ^ {*}}{g _ {i} ^ {*}}\right) \end{array} \right. \left| \begin{array}{l} \text { minimize   objective } \\ \text { maximize   objective } \end{array} \right|\tag{7}
$$

where

g<sub>i</sub><sup>⁎</sup> preferred value associated with criterion g<sub>i</sub>

g<sub>i</sub>(a<sub>j</sub>) non-normalized alternatives performance value.

(3) Calculate weighted normalized individual criterion score, $I C S _ { i j }$

$$
I C S _ {i j} = w _ {i} p _ {i} \left(a _ {j}\right)\tag{8}
$$

where $w _ { i } =$ weight of i-th criterion and

$$
\sum_ {i = 1} ^ {n} w _ {i} = 1.
$$

(4) Calculate the overall suitability score OSS for all n criteria for each j-th alternative

$$
O S S _ {j} = \sum_ {i = 1} ^ {n} I C S _ {i j}.\tag{9}
$$

A positive score indicates that the alternative is a viable alternative, whereas a negative score indicates that it is not viable, when compared to the preferred values.

(5) Rank all alternatives by their overall suitability scores in descending order. The highest ranked alternative is the best alternative.

The proposed Deviation Measure rates well for Ease of Model Formulation and Ease of Automation, except that it cannot handle qualitative or nominal criteria. However, all other techniques reviewed are likewise limited [39]. The handling of qualitative and nominal criteria types are discussed in a separate publication [38].

## 4.1. Range normalization

Typically, quantitative criteria have different units of measure and operate over a range of scales. Consider price, lead-time and production capacity for example. They have totally different units of measure which must be normalized, before the weights can be assigned.

Most methods normalize the units of measure into a range. Some, such as the PROMETHEE methods $[ 6 ] ,$ normalize onto a pre-de<sup>fi</sup>ned common range. If the exact range of values in a criterion's scale is known, the range can be ideally normalized and the problem becomes trivial. For example, suppose there are three criteria $g _ { 1 } , g _ { 2 } ,$ and $g _ { 3 }$ of ascending order of preference, with ranges [0, 100], [0.04, 0.18], and [2000, 5000] respectively. These disparate ranges can be normalized into [0, 1], a commonly used scale, using a linear function such as:

$$
\operatorname{norm} \left(g _ {i}\right) = \alpha \left(g _ {i} + \beta\right)
$$

where

$$
\begin{array}{l} \alpha = \frac {1}{\max _ {i} g _ {i} - \min} \\ \beta = - \left(\min _ {i} g _ {i}\right) \end{array}
$$

max $g _ { i }$ and min $g _ { i }$ are the upper and lower bounds of the scale of $g _ { i } ,$ respectively. The normalizing functions for $g _ { 1 } , g _ { 2 }$ and $g _ { 3 }$ are thus $0 . 0 1 g _ { 1 }$ $7 . 1 4 3 ( g _ { 2 } - 0 . 0 4 )$ and $0 . 0 0 0 3 3 ( g _ { 3 } - 2 0 0 0 )$ for the examples.

However, in real life, the upper and lower bound ranges are not known a priori. For instance, there is no practical upper bound for the three criteria of price, lead-time and production capacity, although their lower bounds can be assumed to be zero.

## 4.2. Range normalization in deviation measure technique

The normalization method given in Eq. (7) does not have a consistent range. As $g _ { i } { } ^ { * }$ is constant and $g _ { i } ( a _ { j } )$ is unbounded, $p _ { i } ( a _ { j } )$ can take on any value. In reality, as this method does not normalize the performance values, the criterion weights are ineffective for $g _ { i } ( a )$ values outside the assumed range o $0 \le g _ { j } ( a _ { i } ) \le 2 g _ { i } ^ { \ * }$ for all i-criteria and j-alternatives. If this assumption is true, then $p _ { i } ( a _ { j } )$ can be correctly normalized to [−1, 1]. However, as this is not always the case, the simplest correction is to rede<sup>fi</sup>ne as:

$$
p _ {i} \Big (a _ {j} \Big) = \left\{ \begin{array}{c l} - 1, & g _ {i} (a) <   0 \\ 1, & g _ {i} (a) > 2 g _ {i} ^ {*} \\ \frac {g _ {i} (a) - g _ {i} ^ {*}}{g _ {i} ^ {*}}, & \text { otherwise } \end{array} \right.
$$

By so doing, the Deviation Measure will consistently normalize within the range [−1, 1] range. However, it relies on decision maker speci<sup>fi</sup>ed preferred values; if these preferred values are changed, based on several initial empirical tests, non-negligible rank reversal can be expected (see Section 3.2). Another issue is making preferred values represent the range of values. It cannot be assumed that the range of values is [0,2g \*] with everything else being outliers. For instance, if a decision maker does not fully understand the mechanics of the range normalization method, and naively speci<sup>fi</sup>es a very low preferred price of \$1, then any alternative with price exceeding \$2 is assigned the lowest possible score of −1. If the actual market price ranges between \$5 and \$20, the difference of prices cannot be captured by this range normalization method. Ironically, the original proposed Deviation Measure method is able to capture such differences, although as discussed, it is not a sound normalization method. The next sub-section proposes a normalization method that addresses this issue.

## 4.3. Modified deviation measure technique

Although the use of preferred values as normalization constants has major drawbacks, these values are able to ascertain if an alternative is better or worse than expected. This is the key differentiation of the Deviation Measure technique as compared to other MAUT methods reviewed. In light of this, a statistical method is proposed to improve the normalization process in Deviation Measure.

According to Chauvenet's criterion [42], a sample is an outlier if its value is not within the Gaussian distribution. Based on this criterion, the range of a cardinal (quantitative) scale can be estimated as follows:

(1) Calculate the mean, $I C S _ { i j } { = } w _ { i } p _ { i } ( a _ { j } )$ and the population standard deviation, s of the available performance values.

(2) Using the three sigma rule of Gaussian distribution, <sup>fi</sup>nd the closest region to the mean with statistical value b0.5. The statistical value is calculated by multiplying the sample count with the probability associated with the four regions separated by $s ,$ which are pre-computed as 0.341, 0.136, 0.021, and 0.001 respectively [10]. If the statistical value is still $\ge 0 . 5$ in the 4th region, assume that the selected region is region 5.

(3) For the nth region identi<sup>fi</sup>ed in Step (2), the upper bound of the range can be calculated a ${ \mathfrak { s } } { \bar { g } } + ( { \mathfrak { n } } - 1 ) s$ , and the lower bound as $\bar { g } - ( \mathrm { n } - 1 ) s .$ . Thus, the breadth of the range is $2 ( \mathrm { n } - 1 ) s$

Thus, the normalized performance value, $p _ { i } ( a _ { j } )$ calculated in Step (2) of Deviation Measure can be modi<sup>fi</sup>ed accordingly.

For a criterion where the objective is to maximize the value,

$$
p _ {i} \left(a _ {j}\right) = \left\{ \begin{array}{c c} - 1, & - 1, g _ {i} (a) <   \min _ {\mathrm{i}} g _ {i} \\ 1, & 1, g _ {i} (a) > \max _ {\mathrm{i}} g _ {i} \\ \frac {g _ {i} (a) - g _ {i} ^ {*}}{\max _ {\mathrm{i}} g _ {i} - \min _ {\mathrm{i}} g _ {i}}, & \text { otherwise } \end{array} \right.\tag{10}
$$

where

min $\phantom { } _ { i } g _ { i }$ statistical lower bound $\operatorname* { m a x } _ { * } g _ { i }$ statistical upper bound, and $g _ { i } ^ { \ " }$ speci<sup>fi</sup>ed preferred value.

![](/api/attachments/9X3HNAX3/fulltext/images/fa27f0e305554d51200c2650dcf76f5a8bf8cf76fc97cfa0ff603ec8ef03c7eb.jpg)  
Fig. 1. A deviation measure from the preferred values

This range is calculated automatically from the pool of available or considered alternatives. To minimize the value, Eq. (10) is modi<sup>fi</sup>ed with max g and min g transposed.

This modi<sup>fi</sup>ed range normalization method has two favorable implications. First, the outlier thresholds and range are estimated by a statistically sound model. Second, because the preferred values are still used to measure the deviation of each alternative's performance from expectations, it is still possible to see which alternatives generally exceed expectations, and which ones are not as good as expected. This maintains the original intent of the technique.

However, the use of the alternatives' performance values to determine the statistical lower and upper bounds is expected to affect the quality of solutions, in particular the rank correlation and rank reversal metrics. Thus, both the Deviation Measure-Original (DMO) and this newly proposed modi<sup>fi</sup>cation Deviation Measure-Modi<sup>fi</sup>ed (DMM) are further investigated.

## 5. Empirical analyses of MCDM techniques

PROMETHEE II and ELECTRE II of the outranking class of methods were short-listed for further evaluation [39] with the proposed and modi<sup>fi</sup>ed Deviation Measure (DMO and DMM). This section details the empirical investigations and analyses carried out for these four candidate MCDM techniques that can support context-aware B2B collaboration. These investigations were conducted using a prototype system, Cognitive Advisor [41]. The implementation of this prototype will not be discussed in this paper.

## 5.1. Motivating scenario

QuickLite is a Singapore-based OEM (Original Equipment Manufacturing) company that manufactures a wide range of electronic products, ranging from memory cards to MP3 players. Most of the company's manufacturing activities are done elsewhere in the region. Their customers are typically MNCs whose own endcustomers are usually in North America or Europe.

QuickLite has just received a blanket purchase order (PO) from one of its MNC customers. 5Kell. which is valid for the next

12 months. There are two common types of purchase orders (POs); standalone and blanket [45]. In a blanket PO, a customer is invoiced for each delivery, instead of when all items are delivered as in a standalone PO. The types of products, their prices and guaranteed minimum and/or maximum quantities are illustrated in Table 1. Accompanying the PO are the following schedule of deliveries:

• MP3 Player: 1000 units of model MP-16 GB each week for the next 8 weeks to 5Kell's of<sup>fi</sup>ce in New York, USA. This is to start immediately.

• Digital Photo Frame: 3000 units of model DP-3R and 2000 units of model DP-4R each week for 3 weeks to San Diego, USA, starting in 3 weeks' time.

• Memory Cards: 1000 units of model MC-32 GB and 500 units of model MC-64 GB each week for 4 weeks, starting in 2 weeks time, to Sydney, Australia.

After examining its capacity and current con<sup>fi</sup>rmed orders, Quick-Lite summed up its business situation in three scenarios — S1, S2 and S3 (highlighted in bold in Table 1):

(S1) It can deliver the 1000 units for MP-16 GB. However, it needs to order the memory cards for the MP3 units (i.e. 1000 units of MC-16 GB) from a suitable supplier. It has the option of assembling the MP-16 GB in Singapore or in Shah Alam, Malaysia.

(S2) It cannot ful<sup>fi</sup>ll the delivery for the digital photo frames (3000 units of DP-3R) internally. It needs to outsource to a partner that can deliver directly to San Diego, USA.

(S3) It also needs to outsource the 500 units of MC-64 GB. It is considering direct delivery to Sydney, Australia too.

Due to the urgency mandated by the forecasted deliveries, Quick-Lite will consider only pre-quali<sup>fi</sup>ed partners.

The following are six sets of criteria (preferences) that QuickLite would like to use for the partner selection for each of the scenarios:

• Cost (C1), lead-time (C2) and location (proximity of partner to delivery location) (C3)

• Cost (C1), lead-time (C2), location (C3) and payment duration (C4)

• Cost (C1), lead-time (C2), location (C3) and payment penalty (C4)

• Cost (C1), lead-time (C2), location (C3) and overall payment (C4)

• Cost (C1), lead-time (C2) and production capacity of partner (C3)

• Cost (C1), lead-time (C2), location (C3), overall payment (C4) and production capacity of partner (C5).

## 5.2. Experimental setup

For each of the scenarios identi<sup>fi</sup>ed (S1 to S3), the criteria and decision options (e.g. to deliver to Sydney, Australia or Singapore in S3) must <sup>fi</sup>rst be ascertained. In Section 5.1 (see Fig. 2), the six criteria sets are already de<sup>fi</sup>ned by QuickLite, and are captured as six different

Table 1  
5Kell's blanket PO scope of product and pricing.

<table><tr><td rowspan="2">Category</td><td rowspan="2">Model</td><td colspan="2">Quantity (week)*</td><td colspan="2">Price (USD)**</td></tr><tr><td>Minimum</td><td>Maximum</td><td>Guaranteed</td><td>Alternate</td></tr><tr><td rowspan="2">MP3 Player</td><td>MP-16GB</td><td>100</td><td>1000</td><td>50.00</td><td>45.00</td></tr><tr><td>MP-64GB</td><td>-</td><td>300</td><td>80.00</td><td>N.A.</td></tr><tr><td rowspan="2">Digital photo frames</td><td>DP-3R</td><td>1000</td><td>-</td><td>50.00</td><td>48.00</td></tr><tr><td>DP-4R</td><td>2000</td><td>-</td><td>70.00</td><td>65.00</td></tr><tr><td rowspan="3">Memory cards</td><td>MC-16GB</td><td>1000</td><td>-</td><td>15.00</td><td>14.00</td></tr><tr><td>MC-32GB</td><td>-</td><td>-</td><td>20.00</td><td>N.A.</td></tr><tr><td>MC-64GB</td><td>-</td><td>-</td><td>30.00</td><td>N.A.</td></tr></table>

\* A ‘–’ indicates no speci<sup>fi</sup>cation in the PO.  
\*\* A “Guaranteed” price applies for orders above the minimum quantity; Otherwise, “Alternate” price is applicable.

![](/api/attachments/9X3HNAX3/fulltext/images/46d35f00ce98406cdbe0fb9c67509362d9c86ac5ef2f30c6f809c250d1a6d01f.jpg)  
Fig. 2. Hierarchical structure of the experimental setup.

Runs. Furthermore, for S1 and S3 there are four decision options as the scenarios require QuickLite to evaluate the possibility of delivering to two different locations (Table 2 provides an example of the 4 decision options). For S2 only two decision options are required, as the scenario speci<sup>fi</sup>ed that all deliveries must go to San Diego, USA only (Table 3 provides an example of the two decision options). This results in a hierarchical experimental setup, as illustrated in Fig. 2. The details of each the test sets, including the criteria and preferred values of QuickLite, are not documented in this paper. An example of such preferred values, Run1-1, is shown in Table 2 where the four decision options are detailed as Opt1-1-1 to Opt1-1-4. Table 3 shows the two decision options in Run2-1, namely Opt2-1-1 and Opt2-1-2. These examples are simpli<sup>fi</sup>ed for ease of discussion, but in reality, the number of criteria could be much higher, thus making it virtually impossible for human decision making. Finally, the 6 different criteria weights are applied to each test set, where the weights are varied uniformly across the range obtainable using the Saaty scale of 1–9 [35]. Hence, this experimental setup will yield $( 2 ^ { * } 6 ^ { * } 4 ^ { * } 6 +$ $1 ^ { * } 6 ^ { * } 2 ^ { * } 6 = )$ 360 tests to ascertain the suitability of the techniques.

The tests were conducted on 20 candidate partners (alternatives), who can supply some or all the products needed. The details of these data are also not included in this paper, due to space constraints.

## 5.3. Test results and analysis

The discussions in this section are based on the four metrics de-<sup>fi</sup>ned in Section 3.2, namely rank completeness, rank correlation, rank reversal and sensitivity analyses.

## 5.3.1. Rank completenes

Using Eq. (1), Table 4 shows a sample calculation of rank completeness in assessing DMO. In this example, there are 11 candidate partners but only 10 unique ranks, yielding a $\omega = { } ^ { 1 0 } / \mathrm { 1 1 } = 0$ :909 score. This shows that the ranking in this example is only 91% complete.

The following steps were undertaken to compute the rank com pleteness scores:

• Conduct all 360 tests for each of the four candidate techniques

• Calculate the rank completeness for each sequence (ranking result)

• Calculate the mean and standard deviation from the individual scores, for each candidate MCDM technique.

The mean rank completeness scores of the four candidate MCDM technique are summarized in Table 5. DMO, DMM and PROMETHEE II yield the best mean score for rank completeness (about 0.99) with relatively low standard deviations. However, ELECTRE II had a mean score of only 0.60 and also a relatively higher standard deviation. From this rank completeness perspective, ELECTRE II is inferior to DMO, DMM and PROMETHEE II.

## 5.3.2. Rank correlation

Rank correlation, ρ measures changes (if any) in rank caused by the addition of new alternatives. For this test setup, only S2 and S3 test cases were used as they have more candidate partners (alternatives). This provided a total of $( 1 ^ { * } 6 ^ { * } 2 ^ { * } 6 + 1 ^ { * } 6 ^ { * } 4 ^ { * } 6 = )$ 216 test cases. The test protocol was as follows:

(a) Run the test using an initial list of 5 candidate partners (alternatives)

(b) Add another 3 candidate partners altogether, and repeat the test

(c) Add the remaining candidate partners altogether, 5 for S2 and 4 for S3, and repeat the test.

Table 2  
Run 1–1 criteria and preferred values (S1).

<table><tr><td rowspan="6">Run 1-1</td><td rowspan="2">Decision options</td><td colspan="3">Criteria</td><td colspan="3">QuickLite preferred values</td></tr><tr><td>Cost</td><td>Lead time (day)</td><td>Location</td><td>Quantity</td><td>Sales basis*</td><td>Tran cost</td></tr><tr><td>Opt1-1-1</td><td>12.50</td><td>3</td><td>Singapore</td><td>1000</td><td>FOB</td><td>500</td></tr><tr><td>Opt1-1-2</td><td>9.50</td><td>5</td><td>Singapore</td><td>3000</td><td>FOB</td><td>500</td></tr><tr><td>Opt1-1-3</td><td>13.00</td><td>3</td><td>Shah Alam, Malaysia</td><td>1000</td><td>FOB</td><td>500</td></tr><tr><td>Opt1-1-4</td><td>10.00</td><td>5</td><td>Shah Alam, Malaysia</td><td>3000</td><td>FOB</td><td>500</td></tr></table>

\* FOB = Free-On-Board (based on internationally used Incoterms).

Table 3  
Run 2–1 criteria and preferred values (S2).

<table><tr><td rowspan="4">Run 2-1</td><td rowspan="2">Decision options</td><td colspan="3">Criteria</td><td colspan="3">QuickLite preferred values</td></tr><tr><td>Cost</td><td>Lead time (day)</td><td>Location</td><td>Quantity</td><td>Sales basis*</td><td>Tran cost</td></tr><tr><td>Opt1-1-1</td><td>43.00</td><td>3</td><td>Singapore</td><td>3000</td><td>FOB</td><td>500</td></tr><tr><td>Opt1-1-2</td><td>45.00</td><td>7</td><td>San Diego, USA</td><td>3000</td><td>CIF-</td><td>-</td></tr></table>

\* CIF = Cost, Insurance and Freight (based on internationally used Incoterms).

Table 7  
Table 5  
Table 4  
Sample result from Set 1-3-4 (W4) used to calculate rank completeness for DMO

<table><tr><td>S/No.</td><td>Company</td><td>Score</td><td>Rank</td></tr><tr><td>1</td><td>ChingTsing</td><td>-0.026</td><td>1</td></tr><tr><td>2</td><td>M-Selangor</td><td>-0.049</td><td>2</td></tr><tr><td>3</td><td>MatSalleh</td><td>-0.049</td><td>2</td></tr><tr><td>4</td><td>CaiHan</td><td>-0.060</td><td>3</td></tr><tr><td>5</td><td>Mangellan</td><td>-0.144</td><td>4</td></tr><tr><td>6</td><td>Herote</td><td>-0.363</td><td>5</td></tr><tr><td>7</td><td>IndisarPuri</td><td>-0.419</td><td>6</td></tr><tr><td>8</td><td>ChenZu</td><td>-0.465</td><td>7</td></tr><tr><td>9</td><td>TechJohn</td><td>-0.526</td><td>8</td></tr><tr><td>10</td><td>Matreng</td><td>-0.873</td><td>9</td></tr><tr><td>11</td><td>ChenPo</td><td>-2.294</td><td>10</td></tr><tr><td colspan="2">Rank completeness =</td><td>10/11</td><td>0.909</td></tr></table>

After the tests were conducted, the rank correlation mean score and standard deviation for each test were computed as follows:

• Obtain Y<sup>'</sup> for 5-alternatives of the ranking sequence obtained in Step (b) and Step (c)

○ Calculate ρ between sequences from Step (a) and Step (b)

○ Calculate ρ between sequences from Step (a) and Step (c)

• Obtain Y<sup>'</sup> for 8-alternatives of the ranking sequence obtained in Step (c)

○ Calculate ρ between sequences from Step (b) and Step (c)

These will yield a sample size of (216\*2 =) 512 rank correlation scores for 5-alternatives comparison (based on results from Step (b) and Step (c) compared to Step (a)), and 216 rank correlation scores for 8-alternatives comparison (based on results from Step (c) compared to Step (a) only).

Table 6 summarizes the rank correlation scores for the four candidate MCDM techniques. The rank correlation scores for DMO are 1.000 for all the 5-alternatives. As DMO is not prone to rank changes for 5-alternatives, no further analysis was conducted for 8- alternatives. This is justi<sup>fi</sup>able, as the scores computation in the DMO technique is not dependent on the values of other candidate partners (alternatives), unlike the other three techniques.

The mean rank correlation scores and standard deviation of DMM and PROMETHEE II are very close for both 5-alternatives and 8- alternatives. Coincidentally, the overall mean score for both are the same, viz 0.917. The overall mean score for ELECTRE II is 0.885. This indicates that ELECTRE II is more sensitive to the in<sup>fl</sup>uence of other candidate partners (alternatives) as compared to DMM and PRO-METHEE II, whereas DMO is completely immune. When alternatives are added, the probability of them in<sup>fl</sup>uencing the scores, and hence sequence, is naturally higher. This leads to more rank changes, resulting in a reduction in rank correlation scores. This is exhibited by the lower mean scores and higher standard deviation values for “Step(a)-Step(c)Y<sup>'</sup>” results for all four candidate MCDM techniques. In summary, DMO is superior in terms of rank stability, followed by DMM and PROMETHEE II. ELECTRE II is the least stable.

Summary of rank completeness scores for the 4 candidate techniques

<table><tr><td>Technique</td><td>Mean score</td><td>Standard deviation</td></tr><tr><td>Deviation Measure-Original(DMO)</td><td>0.997</td><td>0.016</td></tr><tr><td>Deviation Measure-Modified(DMM)</td><td>0.987</td><td>0.032</td></tr><tr><td>PROMETHEE II</td><td>0.995</td><td>0.021</td></tr><tr><td>ELECTRE II</td><td>0.604</td><td>0.122</td></tr></table>

Summary of rank correlation scores.

<table><tr><td></td><td colspan="4">5- alternatives</td><td colspan="2">8-alternatives</td><td rowspan="2" colspan="2">Overall</td></tr><tr><td></td><td colspan="2">Step(a)- Step(b)</td><td colspan="2">Step(a)- Step(c)</td><td colspan="2">Step(b)- Step(c)</td></tr><tr><td>Technique</td><td>Mean</td><td>Std. Dev.</td><td>Mean</td><td>Std. Dev.</td><td>Mean</td><td>Std. Dev.</td><td>Mean</td><td>Std. Dev.</td></tr><tr><td>DMO</td><td>1.000</td><td>0.000</td><td>1.000</td><td>0.000</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>DMM</td><td>0.927</td><td>0.109</td><td>0.894</td><td>0.162</td><td>0.929</td><td>0.074</td><td>0.917</td><td>0.122</td></tr><tr><td>PROMETHEE II</td><td>0.936</td><td>0.118</td><td>0.896</td><td>0.162</td><td>0.918</td><td>0.093</td><td>0.917</td><td>0.129</td></tr><tr><td>ELECTRE II</td><td>0.880</td><td>0.144</td><td>0.860</td><td>0.163</td><td>0.915</td><td>0.091</td><td>0.885</td><td>0.138</td></tr></table>

## 5.3.3. Rank reversal

To recap, rank reversal assesses the stability of the solution based on the concept of similarity between two sequences. A high value indicates a high propensity for rank reversal. The same test setup, procedure and elicitation as in rank correlation are used. As in the earlier test, there are (216\*2=) 512 rank reversal scores for 5-alternatives and 216 rank correlation scores for 8-alternatives. Table 7 summarizes the results. Similar to rank correlation, the computation was limited to 5-alternatives when it was con<sup>fi</sup>rmed that DMO is not susceptible to rank reversal. As in rank correlation, DMM and PRO-METHEE II have shown to be less susceptible to rank reversal than ELECTRE II.

In summary, both the rank correlation and rank reversal measures have con<sup>fi</sup>rmed that DMO is immune to in<sup>fl</sup>uences caused by the addition of candidate partners (alternatives). Although DMM and PRO-METHEE II are not immune, they are less susceptible than ELECTRE II. In DMM, the range normalization incorporated statistical techniques (discussed in Section 4.3), that is theoretically sound but causes it to be unstable when additional candidate partners (alternatives) are added. This is largely due to the dependence on the alternatives' values when determining the normalized performance values of individual criterion in DMM.

## 5.3.4. Sensitivity analyses

Three methods of sensitivity analyses can be performed on MCDM techniques [46]. The <sup>fi</sup>rst two methods examine the impact of uncertainties associated with either the data or the computation of criteria scores; the third method examines the impact of changes in weights. Only the third method is adopted because issues of uncertainties are not within the scope of this paper. For this experimental setup, only 8 test cases employing the 3-criteria options from S1 were chosen; Opt1-1-1, Opt1-1-2, Opt1-1-3, Opt1-1-4, Opt1-5-1, Opt1-5-2, Opt1- 5-3 and Opt1-5-4. The 3-criteria test sets were chosen as they contain two of the most important criteria used in partner selection, namely Cost and Lead-time, as borne out by an industry survey of 10 companies [37].

The weights are designed to be biased towards Cost, increasing through W1 to W6. For tests in Options 1–1, the criteria used are Cost, Lead-time and Location. For tests in Options 1–5, the criterion Location is replaced by Capacity. This is to investigate the impact of a criterion that varies widely among different candidate partners (alternatives). Only two sample results are included (Figs. 3 and 4).

Summary of rank reversal (degree of disagreement) scores.

<table><tr><td></td><td colspan="4">5- alternatives</td><td colspan="2">8-alternatives</td><td rowspan="2" colspan="2">Overall</td></tr><tr><td></td><td colspan="2">Step(a)- Step(b)</td><td colspan="2">Step(a)- Step(c)</td><td colspan="2">Step(b)- Step(c)</td></tr><tr><td>Technique</td><td>Mean</td><td>Std. Dev.</td><td>Mean</td><td>Std. Dev.</td><td>Mean</td><td>Std. Dev.</td><td>Mean</td><td>Std. Dev.</td></tr><tr><td>DMO</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>DMM</td><td>0.103</td><td>0.120</td><td>0.119</td><td>0.151</td><td>0.121</td><td>0.085</td><td>0.115</td><td>0.122</td></tr><tr><td>PROMETHEE II</td><td>0.082</td><td>0.119</td><td>0.129</td><td>0.151</td><td>0.133</td><td>0.097</td><td>0.115</td><td>0.126</td></tr><tr><td>ELECTRE II</td><td>0.154</td><td>0.119</td><td>0.173</td><td>0.120</td><td>0.126</td><td>0.088</td><td>0.151</td><td>0.111</td></tr></table>

DMM: Set1-1-1

![](/api/attachments/9X3HNAX3/fulltext/images/2fc635fcadead04ee2def6b5a143090bc66abcad6fbdd2f683a14e0a0312df68.jpg)  
PROMETHEEII: Set1-1-1

![](/api/attachments/9X3HNAX3/fulltext/images/12ed59c43d37e41df1208bcf06f9fa4bf548600814285e5971d62a302a1a289b.jpg)  
ELECTRE II: Set1-1-1

![](/api/attachments/9X3HNAX3/fulltext/images/10515edc9c1216d48ddb99828e7f997e2a993f96c3ced3e926c9e50ca17c3c5c.jpg)

![](/api/attachments/9X3HNAX3/fulltext/images/ae4dce3aec9254c1a3572865abfc1097076ce2f3fe758c1d02a1015ec0d5f69a.jpg)  
Fig. 3. Sensitivity analysis of the 4 candidate techniques for Set1-1-1.

Each represents one test case, compared across the four short-listed MCDM techniques.

In this sensitivity analyses, the following observations are expected when the rankings through W1 to W6 are compared:

• Changes in rankings for some candidate partners, where the partner values are comparable (e.g. ChenZu or Herote).

• Others like, ChingTsing will retain its ranking as the Cost associated with it is very high and hence, becomes a dominating factor regardless of the weight change.

• The four different MCDM techniques will be affected differently, but should exhibit observable and consistent trends. It should not <sup>fl</sup>uctuate inconsistently.

From the test results for Options 1–1 (Fig. 3 shows an example),

• DMO seems the least affected by the different weights used. Changes in a candidate partner's ranking position are not drastic and are only evident in some candidate partners (e.g. Herote and ChenZu). In ChenZu's case, after W2, its ranking position dropped signi<sup>fi</sup>cantly. For ChenZu's case, the combination of weights and data values for Cost and Lead-time caused its ranking to drop from W1 to W6. Others, like IndisarPuri, hardly changed their rankings.

• For DMM and PROMETHEE II, more changes in ranking positions can be observed, especially for the lower ranked candidate partners. The increase of the weight of the Cost criterion from W1 to W2 seems to cause many ranking changes, across all test sets. This is caused by the sudden drop in the weight for Lead-time and a proportional increase in the corresponding weight of Location. However, this was not observed in DMO, as DMO's OSS scores are not in<sup>fl</sup>uenced by other candidates' values, and the difference in scores caused by the different company locations is not signi<sup>fi</sup>cant. The rank positional changes throughout the test cases for DMM and PROMETHEE are very similar.

• ELECTRE II is the most sensitive to weight changes, with signi<sup>fi</sup>cant rank changes across the board. As in the earlier rank completeness scores, there are many tied ranks, which indicate incomplete ranking. There are no clear trends for ELECTRE II, except that the rank positions <sup>fl</sup>uctuate signi<sup>fi</sup>cantly.

From the test results for Options 1–5 (Fig. 4 shows an example),

• Overall, when the Location criterion was swapped with the Capacity criterion, all the techniques became more sensitive to the weight changes from W1 to W6. This is expected, as the Capacity values from the candidate partners vary greatly; some of them can be considered as outlier values. For example, ChenZu dropped from 1st rank to 11th rank (last) when the weight for Capacity decreased. This is observed for all test cases across all techniques except for ELECTRE II. Again, ELECTRE II has no discernible pattern or trend, and the results from ELECTRE II do not correlate well with the other three techniques.

• As with the earlier test cases, DMO is still the least sensitive to weight changes, despite showing a much higher degree of rank positional changes. Again, DMM and PROMETHEE are closely correlated in their rank positional changes.

• As with the earlier Options 1–1 tests, W2 seems to cause the most rank changes. Likewise, the sudden drop in the weight for Leadtime and a proportional increase in the corresponding weight of Capacity for Options 1–5 tests caused these changes. In this case the <sup>fl</sup>uctuations for DMO are similar to those of DMM and PROMETHEE.

DMM: Set1-5-1

![](/api/attachments/9X3HNAX3/fulltext/images/c525ab6534b1559f7d12a5e3a16ed40bf6569ffb46132ba3fabfbf042df0d891.jpg)  
PROMETHEEII: Set1-5-1

![](/api/attachments/9X3HNAX3/fulltext/images/635f2e427056d07f370c8a04db724b9374d05e54fd67d0fdf163c684e8aad54f.jpg)  
ELECTREII:Set1-5-1

![](/api/attachments/9X3HNAX3/fulltext/images/d845137f9c0fe699e89405999b4c6bd560f931c60635cefff08c1ff95475d2e0.jpg)

![](/api/attachments/9X3HNAX3/fulltext/images/e8bf29ef06594ed66c521a5105ed98e9526bad54a8797e41948fbdddd6afd692.jpg)  
Fig. 4. Sensitivity analysis of the 4 candidate techniques for Set1-5-1.

This can be explained by the high variations in Capacity values across the candidate partners.

In summary, DMO is the least sensitive to criteria weight changes, but if the variations in the candidate partners' values are signi<sup>fi</sup>cant (as in Options 1–5 test cases), they can have a signi<sup>fi</sup>cant impact. DMM and PROMETHEE II exhibit very similar <sup>fl</sup>uctuations and are more volatile compared to DMO. ELECTRE II is the least stable of the four techniques, with no observable trends; the <sup>fl</sup>uctuations for both test series are unpredictable. Furthermore, there are many tied ranks, indicating incomplete rankings. This corroborates with the rank completeness score obtained for ELECTRE II.

Although there is no evidence of a superior technique, DMO, DMM and PROMETHEE II are all comparable, whereas ELECTRE II is unstable and hence unreliable. The conclusion drawn from the sensitivity analyses is that ELECTRE II is inferior compared to the other three techniques.

Summary of the empirical evaluation of candidate MCDM techniques.

<table><tr><td>Technique\Measure*</td><td>DMO</td><td>DMM</td><td>PROMETHEE II</td><td>ELECTRE II</td></tr><tr><td>Rank completeness</td><td>1</td><td>1</td><td>1</td><td>4</td></tr><tr><td>Rank stability</td><td>1</td><td>2</td><td>2</td><td>4</td></tr><tr><td>Rank reversal</td><td>1</td><td>2</td><td>2</td><td>4</td></tr><tr><td>Sensitivity analysis</td><td>1</td><td>1</td><td>1</td><td>4</td></tr><tr><td>Overall score</td><td>4</td><td>6</td><td>6</td><td>16</td></tr></table>

\* 1 = best performance, 4 = worst performance.

## 5.3.5. Summary of empirical analyses

Four measures, namely rank completeness, rank correlation, rank reversal and sensitivity analyses, were used to gauge the quality of the four MCDM techniques, namely DMO, DMM, PROMETHEE II and ELECTRE II.

The results are translated into a quantitative score, as shown in Table 8. DMO emerged as the best candidate MCDM technique for supporting B2B collaboration (with partner selection as a speci<sup>fi</sup>c application example), followed by DMM and PROMETHEE II. In instances where the values of the alternatives have outlier values, DMM and PROMETHEE II could be used instead of DMO, as these techniques have a better range normalization method. An inherent <sup>fl</sup>aw of DMO is that the effects of outlier values are not captured.

## 6. Managerial implications

From the perspective of the management of B2B collaboration, this Deviation Measure enables B2B collaboration to be automated in conjunction with the context-aware approach. This Deviation Measure when used in conjunction with a decision support tool relieves the decision maker from evaluating options and compiling the results. This has several implications. One, the subjectivity of decision makers is minimized or even negated. This means that the results are more consistent and reliable, being less prone to human quirkiness. Two, decision makers are freed from the tedium of manual calculations or even repetitive manual interactions with a decision support tool. This allows decision makers to focus on the most important task, namely making decisions based on results that are scienti<sup>fi</sup>cally sound. This is important as we move into a fast-paced and often changing supply chain environment, where decisions are needed fast. For accurate decisions to be made, a decision tool that is able to extract and analyze data accurately provides a very important safety net.

## 7. Conclusion and future work

Based on the two aspects of Ease of Model Formulation and Ease of Automation in the proposed evaluation framework, existing Multi-Attribute Utility Theory (MAUT) techniques in MCDM were found to be inadequate. A new MAUT technique, Deviation Measure, was therefore proposed. This method addresses the speci<sup>fi</sup>c nature of B2B collaboration, namely (1) unknown ideal values and solution, (2) known collaboration context and determinable relative importance between different criteria, and (3) collaboration criteria of different units of measure and speci<sup>fi</sup>ed preferred values. Using the evaluation metrics proposed in the Quality of Solution, this Deviation Method has been empirically identi<sup>fi</sup>ed as the most suitable MCDM technique for multi-criteria decision making to support context-aware B2B collaboration in supply chain applications.

Although the empirical study in this paper focuses on supplier selection, the results should be applicable to other types of B2B collaboration, in particular for ranking alternatives or options, assuming that the considerations stated in Section 3.1 hold true. DMM and PROMETHEE II are also viable options. There are other B2B applications that can use this context-aware approach, supported by the Deviation Measure. As part of future research work, this approach can be applied to other B2B applications such as (a) exception handling in supply chain track and trace applications, (b) replenishment of warehouses and distribution centers in the supply chain, and (c) monitoring of order ful<sup>fi</sup>llment. Using exception handling as a more speci<sup>fi</sup>c example, when coupled with sensing technologies like GPS (Global Positioning System) and RFID (Radio Frequency Identi<sup>fi</sup>cation), relevant alerts and actions can be initiated, depending on the context of the situation. This inturn can be used for tracking hazardous cargo movements in the supply chain, based on given context (lead-time and location). These contexts can be used to trigger alerts and to decide on the next best actions that can be taken for non-compliance.

## References

[1] A. Agarwal, et al., Modeling the metrics of lean, agile and leagile supply chain: an ANPbased approach, European Journal of Operational Research 173 (2006) 211–225.

[2] A. Amid, et al., A weighted max–min model for fuzzy multi-objective supplier selection in a supply chain, International Journal of Production Economics 131 (2011) 139–145.

[3] B. Angerhofer, M. Angelides, A model and a performance measurement system for collaborative supply chains, Decision Support Systems 42 (2006) 283–301.

[4] K. R. Apaiah, "Chapter 5: An Overview of Multi Criteria Decision Making (MCDM) of Designing Food Supply Chains - A structured methodology: A case on Novel Protein Foods," PhD Thesis, Wageningen University, The Netherlands, Wageningen, 2006.

[5] D. Baker, D. Bridges, R. Hunter, G. Johnson, J. Krupa, J. Murphy, K. Sorenson, Guidebook, to decision-making methods (WSRC-IM-2002-00002)Available, http://emiweb.inel.gov/Nissmg/Guidebook\_2002.pdf2002, 11 May 2009.

[6] J.P. Brans, B. Mareschal, Chapter 5: PROMETHEE methods, in: J. Figueira, et al., (Eds.), Multiple Criteria Decision Analysis: State of the Art Surveys, Springer, Boston, 2005, pp. 164–189.

[7] J.P. Brans, et al., How to select and how to rank projects: the method, European Journal of Operational Research 24 (1986) 228–238.

[8] L.M. Camarinha-Matos, Virtual organizations in manufacturing: trends and challenges, presented at the 12th Int. Conf. On Flexible Automation and Intelligent Manufacturing, Dresden, Germany, 2002.

[9] M.-T. Chu, et al., Comparison among three analytical methods for knowledge communities group-decision analysis, Expert Systems with Applications 33 (2007).1011-1024

[10] F. Coolidge, An introduction to correlation and regression, Statistics — A Gentle Introduction Second Edition SAGE Publications Inc 2006 pp. 153-196.

[11] J.M. Cruz, The impact of corporate social responsibility in supply chain management: multicriteria decision-making approach, Decision Support Systems 48 (2009) 224–236.

[12] Deloitte, Mastering complexity in global manufacturing — powering pro<sup>fi</sup>ts and growth through value chain synchronization, A Deloitte Research Global Manufacturing Study, 2003, Sep 2007 Available, http://www.deloitte.com/dtt/ research/0,1015,sid%253D19675%2526cid%253D36776,00.html.

[13] E. Demirtas, O. Ustun, An integrated multiobjective decision making process for supplier selection and order allocation☆, Omega 36 (2008) 76–90.

[14] J.S. Dyer, Remarks on the analytic hierarchy process, Management Science 36 (1990) 249–258.

[15] J. Fülöp, Introduction to decision making methods available, http://academic.evergreen. edu/projects/bdei/documents/decisionmakingmethods.pdf2005, 05 Jan 2009.

[16] C.M. Goh, et al., Key issues in manufacturing enterprise integration — the Singapore perspective, 3 rd IEEE International Conference on Industrial Informatics, 2005, Perth, WA, Australia, 2005, pp. 390–395, INDIN '05.

[17] H. Haleh, A. Hamidi, A fuzzy MCDM model for allocating orders to suppliers in a supply chain under uncertainty over a multi-period time horizon, Expert Systems with Applications 38 (2011) 9076–9083.

[18] J. Han, M. Kamber, Types of data in cluster analysis, Data Mining: Concepts and Techniques2 ed, , 2006, pp. 386–398.

[19] R. Harris, Introduction to decision making available, http://www.virtualsalt.com/ crebook5.htm2008.19 Mav 2009

[20] W. Ho, et al., Multi-criteria decision making approaches for supplier evaluation and selection: a literature review, European Journal of Operational Research 202 (2010) 16–24.

[21] V. Jain, et al., Select supplier-related issues in modelling a dynamic supply chain: potential, challenges and direction for future research, International Journal of Production Research 47 (2009) 3013–3039.

[22] G. Kou, et al., Multiple criteria decision making and decision support systems — guest editor's introduction, Decision Support Systems 51 (2011) 247–249.

[23] S.G. Lee, et al., “Modern Portfolio Theory applied to allocating orders to shortlisted suppliers,” IEEE Trans Project Management, Submitted for publication.

[24] C.-N. Liao, H.-P. Kao, An integrated fuzzy TOPSIS and MCGP approach to supplier selection in supply chain management, Expert Systems with Applications 38 (2011) 10803–10811.

[25] Z. Liao, J. Rittscher, A multi-objective supplier selection model under stochastic demand conditions, International Journal of Production Economics 105 (2007) 150–159.

[26] C.-T. Lin, et al., An ERP model for supplier selection in electronics industry, Expert Systems with Applications 38 (2011) 1760–1765.

[27] F. Mafakheri, et al., Supplier selection-order allocation: a two-stage multiple criteria dynamic programming approach, International Journal of Production Economics 132 (2011) 52–57.

[28] A. Marquez, C. Blanchar, A decision support system for evaluating operations investments in high-technology business, Decision Support Systems 41 (2006) 472–487.

[29] S. Opricovic, G.-H. Tzeng, Compromise solution by MCDM methods: a comparative analysis of VIKOR and TOPSIS, European Journal of Operational Research 156 (2004) 445–455.

[30] Order business modelsAvailable, http://www.ti.com/sc/docs/scedi/ordmodel. pdf1996, Jun 2008.

[31] V. Pihur, et al., RankAggreg, an R package for weighted rank aggregation, BMC Bioinformatics (2009, 07 July 2009) Available, http://people.revoledu.com kardi/tutorial/Similarity/FootruleDistance.html.

[32] M. Rogers, et al., ELECTRE and Decision Support — Methods and Applications in Engineering and Infrastructure Investment, Kluwer Academic Publishers, 2000.

[33] B. Roy, The outranking approach and the foundations of electre methods, Theory and Decision 31 (1991) 49–73.

[34] B. Roy, Chapter 1: paradigms and challenges, in: J. Figueira, et al., (Eds.), Multiple Criteria Decision Analysis: State of the Art Surveys, Springer, Boston, USA, 2005, pp. 3–24.

[35] P.G. Russell, W.C. Kropf, Hewlett-Packard's packaging supplier evaluation process and criteria, IoPP 16th Educational Symposium on Transport Packaging proceedings, 1999.

[36] T.L. Saaty, L. Vargas, Fundamentals of Decision Making and Priority Theory With the Analytic Hierarchy Process vol, Vol. 6, 2000 RWS Publications.

[37] G. Samtani, D. Sadhwani, B2Bi and Web services: an intimidating task? in: P.F.M. Waterhouse (Ed.), Web Services Business Strategies and Architectures, Wrox Press, 2002, pp. 57–59.

[38] P.S. Tan, A context-aware approach for Business-to-Business collaboration, Doctor of Philosophy, School of Computer Engineering, Nanyang Technological University, Singapore, 2010.

[39] P.S. Tan, et al., Issues and approaches to dynamic, service-oriented multienterprise collaboration, Industrial Informatics, 2006 IEEE International Conference on, 2006, pp. 399–404

[40] P.S. Tan, et al., An implementation of context-aware partner selection to support supply chain collaborations, Industrial Informatics, 2008. INDIN 2008. 6th IEEE International Conference on, 2008, pp. 812–818.

[41] P.S. Tan, et al., A context model to support Business-to-Business (B2B) collaboration, in: M. Sheng, et al., (Eds.), Enabling Context-Aware Web Services: Methods, Architectures, and Technologies, Chapman and Hall/CRC, 2010, pp. 243–272.

[42] P.S. Tan, et al., Presented at the IEEE International Conference on Service Operations and Logistics, and Informatics (SOLI 2010), Qingdao, Shandong, China, 2010.

[43] J.R. Taylor, An Introduction to Error Analysis, 2nd edition University Science Books, Sausolito, CA, 1997.

[44] S.-C. Ting, D.I. Cho, An integrated approach for supplier selection and purchasing decisions, Supply Chain Management: An International Journal 13 (2008) 116–127.

[45] E. Triantaphyllou, Two new cases of rank reversals when the AHP and some of its additive variants are used that do not occur with the multiplicative AHP Journal of Multi-Criteria Decision Analysis 10 (2001) 11–25.

[46] W.T.M. Wolters, B. Mareschal, Novel types of sensitivity analysis for additive MCDM methods, European Journal of Operational Research 81 (1995) 281–290

[47] M. Zeydan, et al., A combined methodology for supplier selection and performance evaluation, Expert Systems with Applications 38 (2011) 2741–2751.

Dr. Tan Puay Siew received her PhD in Computer Science from Nanyang Technological University. She is presently the Deputy Group Manager of Planning and Operations Management Group in SIMTech, Singapore. Her present research interests include context-aware B2B Collaboration and complex systems approach for robust supply chain collaboration. She has published in various book chapters, journals and conferences over the years. She has also served as program committee members of various international conferences.

Dr. Stephen Siang-Guan LEE is an associate professor in the School of Mechanical & Aerospace Engineering, NTU. Dr. Lee earned his Masters' from the University of Manchester (UK) and PhD from Nanyang Technological University, Singapore. Prior to joining Nanyang Technological University in 1983, he was engaged in design and consulting assignments in local manufacturing companies. His research interests are in complex logistics systems, product life cycle management, dynamic enterprise collaboration and sustainable product design and development. He is presently Director of the MSc(Project Management) Program which is jointly conducted with the School of Mechanical, Aerospace and Civil Engg, University of Manchester. Dr. Lee is a registered professional engineer and a Fellow of the Society of Manufacturing Engineers. An active member of the SME since 1987, Dr. Lee held senior appointments in the Singapore Chapter, culminating with the Chapter Chairmanship in 1990. In 1992, the Society of Manufacturing Engineers conferred on him its Award of Merit and in 1998, he was elected to its College of Fellows.

Dr. Angela Goh Eck Soong is a professor in the School of Computer Engineering, Nanyang Technological University, Singapore. She was appointed Associate Provost (Faculty Affairs) in July 2011. She completed her doctorate in the University of Manchester. Her current research interests include the Semantic Web, including semantic web service discovery and composition, ontology engineering and application to education and e-business. She has been on the editorial board of several international journals as well as member of numerous international conferences.

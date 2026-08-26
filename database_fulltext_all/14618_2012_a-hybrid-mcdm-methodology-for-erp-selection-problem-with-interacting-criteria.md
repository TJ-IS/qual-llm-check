---
otero_id: 14618
otero_key: "3WGUDM7B"
title: "A hybrid MCDM methodology for ERP selection problem with interacting criteria"
authors: "Tuncay Gürbüz; S. Emre Alptekin; Gülfem Işıklar Alptekin"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.05.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A hybrid MCDM methodology for ERP selection problem with interacting criteria

Tuncay Gürbüz <sup>a</sup>, S. Emre Alptekin <sup>a</sup>, Gülfem Işıklar Alptekin <sup>b,</sup>⁎

<sup>a</sup> Department of Industrial Engineering, Galatasaray University, Çırağan Cad. No:36 34357 Ortaköy, İstanbul, Turkey

<sup>b</sup> Department of Computer Engineering, Galatasaray University, Çırağan Cad. No:36 34357 Ortaköy, İstanbul, Turkey

## a r t i c l e i n f o

Article history: Received 5 August 2011 Received in revised form 20 February 2012 Accepted 10 May 2012 Available online 22 May 2012

Keywords: ERP Supplier selection MCDM ANP Choquet integral

## a b s t r a c t

An enterprise resource planning (ERP) system is an information system to plan and integrate all of an enterprise's subsystems including purchase, production, sales and <sup>fi</sup>nance. Adopting such a comprehensive framework may result in the great savings in both costs and man hours. This research explores the application of a hybrid multicriteria decision making (MCDM) procedure for the evaluation of various ERP alternatives. The proposed evaluation framework integrates three methodologies: Analytic Network Process (ANP), Choquet integral (CI) and Measuring Attractiveness by a Categorical Based Evaluation Technique (MAC-BETH). ANP produces the priorities of alternatives with respect to the interdependent evaluation criteria. The conjunctive or disjunctive behaviors between criteria are determined using MACBETH and CI. Numerical application of the proposed methodology is implemented on the decision making problem of a <sup>fi</sup>rm that faces with four ERP projects. The <sup>fi</sup>nal ranking is compared to the one obtained by ignoring the interactions among criteria. The results demonstrate that the ignorance of the interactions may lead to erroneous decisions.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Due to severe market competition, companies have directed to consider alternative business environments in order to reduce total cost, maximize return on investment, shorten lead times and be more responsive to customer requirements. An enterprise resource planning (ERP) system can be considered as a solution for inef<sup>fi</sup>cient business processes. Organizations think about purchasing it when they deal with a number of complex and interrelated business troubles, such as achieving company's <sup>fi</sup>nancial goals, managing and streamlining the company's operational processes, better forecasting features or obtaining the bene<sup>fi</sup>ts of improved information management by reducing data duplication. An ERP system typically implements a common enterprise-wide database together with a range of application modules [13]. It standardizes processes and stores information as well as recalls that data when it is required in real time environment. Implementing an ERP system may be costly and timeconsuming. Companies spend billions of dollars and use numerous amounts of man-hours for installing elaborate ERP software systems. However, the bene<sup>fi</sup>ts of a successful ERP project are worthwhile.

The offered ERP software packages cannot provide a once-for-all business model for every process of all industries. In other words, no single ERP packaged software can meet all company functionalities or all special business requirements [33]. Thus, companies must choose a <sup>fl</sup>exible ERP system that is responsive to customer requirements. The major reason for ERP implementation failures is stated as the inappropriate system selection [13,22]. An inappropriate selection process can signi<sup>fi</sup>cantly affect not only the implementation but also the performance of the company [9]. Therefore, the importance of selecting a suitable ERP system cannot be overemphasized [19].

This paper introduces a hybrid multicriteria decision making (MCDM) model for ERP selection based on Analytic Network Process (ANP), Choquet Integral (CI) and Measuring Attractiveness by a Categorical Based Evaluation Technique (MACBETH). MCDM refers to <sup>fi</sup>nd the best opinion from all of the feasible alternatives in the presence of multiple, usually con<sup>fl</sup>icting, decision criteria. It is a branch of a general class of operations research models that deals with the decision making problems under the presence of a number of decision making alternatives described by their attributes [8]. Priority based, outranking, distance-based and mixed methods could be considered as the primary classes of the current methods [26]. One of the most outstanding MCDM approaches is ANP which is a generalization of one of the most known MCDM methodologies: Analytic Hierarchy Process (AHP) [30]. While AHP represents a framework with a unidirectional hierarchical relationship, ANP allows for complex interrelationships among decision levels and criteria. ANP is used in many decision support systems of various types. Verdecho et al. [32], have provided a methodology based on ANP to prioritize and manage inter-enterprise performance at both the strategic and the process level. Another research has explored the application of ANP approach for the evaluation of R&D projects that are elements of programs with heterogeneous objectives [21]. Although there are various methods, such as mathematical programming, MCDM analysis or scoring, which is applied to the ERP software selection, we focus on studies including MCDM analysis. Wei et al. [33] have introduced their selection framework that is based on AHP method. Erensal and Albayrak [14] have suggested AHP to effectively enhance adoption of macroergonomics and to improve management decision performance in measuring and comparing the overall performance of different management styles based on macroergonomical criteria. The most similar work to our proposed framework is the work of Yazgan et al. [34]. However, they have designed an arti<sup>fi</sup>cial neural network model and trained with using ANP results in order to calculate ERP software priorities.

In our paper, we have categorized ERP selection criteria into three main sets: vendor related criteria (VRC), customer related criteria (CRC), and software related criteria (SRC). Each one consists of its own sub-criteria set. Since these criteria and sub-criteria have both inner and outer dependencies, we have made use of the ANP to determine these dependencies and relative priorities of all criteria. MACBETH is both an approach and a set of techniques that have the goal of providing an overall ordering of options, and that aid on the construction of interval numerical scales based on qualitative (non-numerical) pairwise comparison judgments [4,12].

In this research, we have used CI to determine conjunctive or disjunctive behaviors between criteria and integrated MACBETH in CI in order to de<sup>fi</sup>ne the parameters of CI. The last phase of the proposed methodology involves ranking the given ERP alternatives according to their <sup>fi</sup>nal performance scores. We have shown the feasibility of the framework on the decision making problem of a company that needs to evaluate four ERP software alternatives and select the most suitable one according to its requirements. Furthermore, we have obtained another ranking by using the same evaluation values; however this time we have ignored the interactions among criteria. The comparison has shown that the <sup>fi</sup>nal ranking may change dramatically with the ignorance of the interactions and therefore it may lead us to erroneous decisions.

The remaining part of the paper is organized as follows: Section 2 describes the methodologies that constitute the proposed framework. The steps and details of the proposed decision support framework are introduced in Section 3. The implementation into the ERP selection problem is presented in Section 4. Finally, Section 5 gives the concluding remarks of the study.

## 2. Preliminaries

In this section, three methodologies underlying the proposed framework (ANP, CI and MACBETH) along with their integration will be presented.

## 2.1. Analytic Network Process (ANP)

ANP, as well as AHP, incorporates both qualitative and quantitative approaches to a decision problem [10]. It is also capable of capturing the tangible and intangible aspects of relative criteria that have some bearing on the decision making process [30]. AHP is limited to relatively static and unidirectional interactions with little feedback among decision components and alternatives [20]. However, many real life decision problems cannot be structured as a hierarchy because of the interactions and dependence among criteria. Therefore, the hierarchy becomes more like a network. On this context, ANP and its supermatrix technique can be considered as an extension of AHP that can handle a more complex decision structure as the ANP framework has the <sup>fl</sup>exibility to consider more complex interrelationships (outer dependence) among different elements [30,31]. Hence, ANP is very useful in these kinds of situations providing a general framework without the assumptions of independence of higher-level elements from lower ones, or independence on the same level.

ANP framework has three basic features which are useful in multicriteria decision making problems:

• De<sup>fi</sup>ne the goal and criteria (and sub-criteria),

• Determine the interdependencies and the network,

• Build the supermatrix and synthesize.

In this approach, comparison matrices, prioritization and the weights while considering the interdependencies are formed between various attributes of each level with the scale of 1–9 suggested by Saaty [29]. Also the consistencies of the pairwise comparisons, made by the experts or decision makers (DMs), have to be checked in order to make the necessary changes, if there is any inconsistency above the allowed limit. Once the pairwise comparison matrices are formed, weight vectors for all the matrices are calculated. The concept of supermatrix is used to obtain the composite weights that overcome the existing interrelationships. The synthesizing step is to rate the alternatives according to all the criteria, compute the overall score for the alternatives and make the <sup>fi</sup>nal decision as to choose the best alternative or to obtain the <sup>fi</sup>nal ranking of the alternatives.

## 2.2. Choquet Integral (CI)

The CI, which has been introduced in the fuzzy measure community by Murofushi and Sugeno [25] is a fuzzy integral proposed by Choquet [11] and considers the interactions between k out of n criteria of the problem, which is called the k-additivity property. Basic notations and de<sup>fi</sup>nitions on the CI can be analyzed in Appendix A. In this research, 2-additive CI is used.

Letting $t _ { i } , i = 1 , . . . ,$ n be the scores on the criteria, by using only the interaction index, it is possible to express CI in the case of 2-additive measures as follows [15]:

$$
\begin{array}{c} C _ {\mu} (t _ {1}, \dots , t _ {n}) = \sum_ {I i j > 0} \left(t _ {i} \wedge t _ {j}\right) I _ {i j} + \sum_ {I _ {i j} <   0} \left(t _ {i} \vee t _ {j}\right) \left| I _ {i j} \right| + \sum_ {i = 1} ^ {n} t _ {i} \left(\varphi_ {i} - \frac {1}{2} \sum_ {j \neq i} \left| I _ {i j} \right|\right) \\ w i t h \varphi_ {i} - \frac {1}{2} \sum_ {j \neq i} \left| I _ {i j} \right| \geq 0, \forall_ {i} = 1, \dots n \end{array}\tag{1}
$$

Here, $\varphi _ { i }$ represents the relative importance of criterion i with $\sum _ { i = 1 } ^ { n } \varphi _ { i } = \dot { 1 }$ and $I _ { i j } ,$ de<sup>fi</sup>ned in the interval [−1;1], is the interaction <sup>¼</sup>value between criteria i and j. Appendix B presents the de<sup>fi</sup>nitions.

Three cases may be observed for interaction value:

• Positive values of $I _ { i j }$ implies a conjunctive behavior between criteria i and j. i.e. simultaneous satisfaction of both criteria is signi<sup>fi</sup>cant for the global score.

• Negative values of $I _ { i j }$ implies a disjunctive behavior between criteria i and j. i.e. the satisfaction of either one is suf<sup>fi</sup>cient to have a significant effect on the global score.

• If $I _ { i j }$ is null, then there is no interaction between criteria i and j. If for all pairs of criteria, $I _ { i j }$ are null then the $\varphi _ { i }$ value acts as a weight vector in a weighted arithmetic mean. This represents the linear part of CI.

The use of CI will be demonstrated on a simple example from Saad et al.'s [28] work. Suppose we were to consider three students, A, B, and C, with respect to three subjects, mathematics, physics and literature in a school that is more scienti<sup>fi</sup>cally oriented. Hence, the weights for these three subjects may be 3, 3 and 2, respectively. In that case, using weighted sum method and marks given on a scale from 0 to 20, the average for these students are calculated and given in Table 1.

However, if one desires to favor well equilibrated students without weak points, the weighted sum may not be the best suited method to use since student A, although having a considerable weakness in literature has been considered better than student C, who has no weak point. If one were to use CI in order to <sup>fi</sup>nd the average for these students, the following logic can be applied:

Table 1 Students' grades.

<table><tr><td></td><td>M</td><td>P</td><td>L</td><td>Weighted sum</td></tr><tr><td>A</td><td>18</td><td>16</td><td>10</td><td>15.250</td></tr><tr><td>B</td><td>10</td><td>12</td><td>18</td><td>12.750</td></tr><tr><td>C</td><td>14</td><td>15</td><td>15</td><td>14.625</td></tr></table>

• Since the school is scienti<sup>fi</sup>cally oriented, following weights can be appropriate for the subjects: $\mu ( M ) = \mu ( P ) = 0 . 4 5$ and $\mu ( P ) = 0 . 3 0$ • Since mathematics and physics are redundant, the weight attributed to ‘mathematics and physics’ can be chosen to be less than the sum of their individual weights: $\mu ( M \& P ) = 0 . 5 { < } 0 . 4 5 + 0 . 4 5 .$

• With the same logic, to favor the students equally good in scienti<sup>fi</sup>c subjects and literature, the weight attributed to ‘mathematics and literature’ and ‘physics and literature’ can be chosen to be greater than the sum of their individual weights as follows: $\mu ( M \& L ) = \mu ( P \& L ) =$ $0 . 9 > 0 . 4 5 + 0 . 3 .$

• By de<sup>fi</sup>nition μ(M & P & L)=1 and $\mu ( \phi ) = 0 .$

Using this fuzzy measure and Eq. (1), the average of these students are calculated as: 13.9 for student A, 13.6 for student B and 14.9 for student C. The new results place student C to the top position instead of student A.

2.3. Measuring Attractiveness by a Categorical Based Evaluation Technique (MACBETH)

MACBETH is a multicriteria decision analysis approach which has <sup>fi</sup>rst been proposed in 1992 [2]. MACBETH has been used in various <sup>fi</sup>elds such as individual's career choice [3], evaluation and comparison of the technical performance of on-board hydrogen storage technologies [24], politics [27], supply chain management [6], and earthquake risk mitigation [5]. The method requires only qualitative judgments about differences of value to help an individual or a group in quantifying the relative attractiveness of the elements of a finite set A and to associate a real number $\varphi ( x )$ to each element x of A.

Let X be the <sup>fi</sup>nite set of elements (alternatives) with at least two elements and J the group of DMs who want to compare the relative attractiveness of these elements. Here, it is assumed that the DMs are able to rank the elements of X either directly or through pairwise comparisons. Each DM is <sup>fi</sup>rst asked to provide a judgment about the relative attractiveness of two elements at a time to retrieve the ordinal judgment. Then secondly, they are asked to provide a qualitative judgment on the difference of attractiveness of those two elements, if they are not equally attractive using the following linguistic terms: very weak (VW), weak (W), moderate (M), strong (S), very strong (VS) and extreme (E).

MACBETH method presents a procedure to transform qualitative preferences into coherent quanti<sup>fi</sup>ed elementary and aggregated performances. In order to solve the inter-criteria commensurability problem, it is suf<sup>fi</sup>cient to determine, for all interval scales, two common reference points namely the ‘good’ situation and the ‘neutral’ situation with the performance values 1 and 0, respectively.

Let p<sup>k</sup> be the performance expression of the $k ^ { t h }$ alternative for criterion i. Suppose the DM prefers for the $i ^ { t h }$ criterion the alternative k to the alternative l and in addition to that information, DM will characterize the strength of his judgments with a level of strength that can take values from 1 to 6 (from the least to the most strong level) according to the six semantic categories of the difference of attractiveness explained above and 0 for a null strength. This level will be denoted with h. Therefore, if the DM prefers the alternative k to the alternative l for the $i ^ { t h }$ criterion, with a strength h, then the following equation, where α is a coef<sup>fi</sup>cient necessary to meet the condition and $p ^ { \bar { k } }$ and $p ^ { l } \in [ 0 ; 1 ]$ ], will be obtained:

$$
A ^ {k} \succ^ {h} A ^ {l} \Longleftrightarrow p _ {i} ^ {k} - p _ {i} ^ {l} = h \alpha\tag{2}
$$

Therefore, a preference ranking of alternatives for a speci<sup>fi</sup>c criterion, including the ‘good’ and the ‘neutral’ alternatives, collected from a DM with the strength of the comparisons will give us a system of equation. After solving it, the individual performance values of the alternatives for the criterion in question will be determined.

## 2.4. MACBETH and Choquet Integral

This sub-section includes the use of MACBETH in order to <sup>fi</sup>nd the CI parameters given in Eq. (2). The operators of the CI family can be written under the form of a conventional weighted mean modi<sup>fi</sup>ed by effects coming from interactions between elementary performances [12]. They are stable under linear transformation [23] and thus consistent with the performance expressions on an interval scale on the universe [0;1]. This property constitutes the theoretical basis of the extension of the MACBETH procedure to the CI aggregation operators [12].

According to the MACBETH procedure, the DM is asked to provide preferential ranking information on the criteria and the couples of criteria including the strength of the preferences. Eq. (2) and the de<sup>fi</sup>nitions that will be given below will help us to build a system of equations with the Shapley and the interaction parameters as variables.

In the situations where only one $p _ { i } = 1$ and all others are equal to 0 (i.e. only criterion i is satis<sup>fi</sup>ed), the aggregated performance expression will be as [12]:

$$
p_{Ag}^{i} = \varphi_{i} - \frac{1}{2}\sum_{\substack{j = 1\\ j\neq i}}^{n}I_{ij}\tag{3}
$$

The aggregated performance expression of the situations where only one $p _ { i } = 0$ and all others are equal to 1 (i.e. all criteria except i is satis<sup>fi</sup>ed) will be as [12]:

$$
p _ {A g} ^ {i} = 1 - \varphi_ {i} - \frac {1}{2} \sum_ {\stackrel {j = 1} {j \neq i}} ^ {n} I _ {i j}\tag{4}
$$

The aggregated performance expression of the situations where only two elementary performance expressions are equal to 1 (namely i and j) and all others are equal to 0 (i.e. criterion i and j are satis<sup>fi</sup>ed) will be as [16]:

$$
p _ {A g} ^ {i, j} = \varphi_ {i} + \varphi_ {j} - \frac {1}{2} \left(\sum_ {k \in \aleph_ {1: n} | p _ {k} = 0} I _ {i k} + \sum_ {k \in \aleph_ {1: n} | p _ {k} = 0} I _ {j k}\right)\tag{5}
$$

Let us illustrate a demonstrative example of the integration of MACBETH in CI. Consider a decision based on two criteria, namely $C _ { 1 }$ and $C _ { 2 } ,$ between two alternatives, namely $A _ { 1 }$ and $A _ { 2 } .$ . Suppose that the DM has the following preferential rankings:

$$
\begin{array}{l}C _ {1} \&C _ {2} \succ^ {M} C _ {1} \succ^ {W} C _ {2} \succ^ {V W} \succ^ {S" 0"}\\C _ {1} \rightarrow G o o d \succ^ {M} A _ {1} \succ^ {M} A _ {2} \succ^ {W} N e u t r a l\\C _ {2} \rightarrow G o o d \succ^ {S} A _ {2} \succ^ {W} A _ {1} \succ^ {V W} N e u t r a l\end{array}
$$

The <sup>fi</sup>rst preferential ranking results in the following system of equations whose resolution gives the CI parameters:

$$
\left\{ \begin{array}{l} p ^ {(1, 1)} - p ^ {(1, 0)} = 3 \alpha = 1 - \varphi_ {1} + \frac {1}{2} I _ {1 2} \\ p ^ {(1, 0)} - p ^ {(0, 1)} = 2 \alpha = \varphi_ {1} - \varphi_ {2} \\ p ^ {(0, 1)} - p ^ {(0, 0)} = \alpha = \varphi_ {2} - \frac {1}{2} I _ {1 2} \\ \varphi_ {1} + \varphi_ {2} = 1 \end{array} \Rightarrow \alpha = \frac {1}{6} \quad \varphi_ {1} = \frac {2}{3} \quad \varphi_ {2} = \frac {1}{3} \quad I _ {1 2} = \frac {1}{3} \right.
$$

The second and third preferential rankings give the following systems equations whose resolutions determine the performance values of alternatives for each criteria:

$$
\left\{ \begin{array}{l} 1 - p _ {1} ^ {1} = 3 \alpha \\ p _ {1} ^ {1} - p _ {1} ^ {2} = 3 \alpha \\ p _ {1} ^ {2} = 2 \alpha \end{array} \right. \Rightarrow \alpha = \frac {1}{8} \quad p _ {1} ^ {1} = \frac {5}{8} \quad p _ {1} ^ {2} = \frac {2}{8}
$$

$$
\left\{ \begin{array}{l} 1 - p _ {2} ^ {2} = 4 \alpha \\ p _ {2} ^ {2} - p _ {2} ^ {1} = 2 \alpha \\ p _ {2} ^ {1} = \alpha \end{array} \right. \Rightarrow \alpha = \frac {1}{7} \quad p _ {2} ^ {1} = \frac {1}{7} \quad p _ {2} ^ {2} = \frac {3}{7}
$$

Finally, using Eq. (1), the aggregated performance values are calculated for $A _ { 1 }$ and $A _ { 2 }$ as 0.384 and 0.280, respectively. Hence, in this example, $A _ { 1 }$ turns out to be a better alternative than $A _ { 2 } .$

## 3. ERP system evaluation framework

## 3.1. Evaluation procedure

The evaluation procedure of this study consists of seven steps as follows Fig. 1:

1. Identify the ERP software selection/evaluation criteria that are considered the most important for the users.

2. Once the model is built and the relations between criteria are de<sup>fi</sup>ned, decide the method to use. This is not an arbitrary choice.

3. If there is an outer-dependence between sub-criteria, then this is something to be analyzed with ANP because of the simple fact that CI cannot handle two elements that are connected to two different points. In this case, two sub-criteria in question belong to two different criteria. Hence, these dependencies will be handled with ANP.

4. Analyze sub-criteria of the same cluster in order to de<sup>fi</sup>ne the conjunctive and disjunctive behavior between them. If there is such relation, use CI in order to <sup>fi</sup>nd the interaction values. In case of no such interaction, handle the relations with ANP.

5. After handling the sub-criteria, take in consideration the upper level, i.e. the criteria.

6. A preference ranking of the criteria given by the DMs will de<sup>fi</sup>ne the conjunctive/disjunctive behavior between those. If there is not any interaction of this kind between the criteria, then solve the model with ANP. Make the <sup>fi</sup>nal aggregation and obtain a ranking.

7. If there are conjunctive/disjunctive behavior between criteria, then use the Shapley indices and the interaction values including the weights of the sub-criteria and the alternatives' individual performance values for each of those sub-criteria in order to perform the <sup>fi</sup>nal aggregation.

To resume this [17],

• Outer dependencies between sub-criteria+no conjunctive/disjunctive behavior between them+NO conjunctive/disjunctive behavior between criteria = ANP

• No outer dependencies between sub-criteria+conjunctive/disjunctive behavior between them+conjunctive/disjunctive behavior between criteria= CI.

• Other than those situations=Hybrid ANP & CI.

In the use of CI method, if the experts (DMs) are able to provide a fuzzy measure for their criteria set, then it is possible to de<sup>fi</sup>ne the Shapley indices and interaction values using the Eqs. (B.1) and (B.2). Or if, using their experience and expertise, they are able to provide the weights of their criteria and information about interactions (being strongly positive, positive, null, negative or strongly negative), then the interaction values can be retrieved using some other simplifying approaches, such as the one used in Montignac et al. [24].

In this case, only de<sup>fi</sup>nition of individual performance values of the alternatives according to those criteria has to be made. But, it has to be noted that for the quantitative criteria, a simple normalization procedure will be required to obtain the values. On the other hand, in order to de<sup>fi</sup>ne the performance values for the qualitative ones, a tool such as AHP or MACBETH could be used. In this research, MACBETH is proposed for that purpose.

## 3.2. Selection criteria

Baki and Çakar [1] have summarized the ERP selection criteria in their research after reviewing the related literature. We have used the 16 criteria that they have proposed, but we have grouped them under three main categories: vendor related, customer related and software related (Table 2).

The problems that the <sup>fi</sup>rms face during the installation, the implementation and after the implementation periods can cause seven to ten times the initial software cost. Hence, the <sup>fi</sup>rms need support and service from the software <sup>fi</sup>rms in terms of IT expertise and domain knowledge. One of the criteria that a buyer should consider is the vendor's vision, speci<sup>fi</sup>cally the modi<sup>fi</sup>cations that the vendor plans to make to its products and services over the next years. The reputation of the vendor and its service infrastructure constitute its market position. It is important that the software developer/vendor knows the industry of the customer. This characteristic is referred as the domain knowledge of the vendor. The implementation of an ERP system to a <sup>fi</sup>rm generally necessitates big changes in <sup>fi</sup>rms. Therefore, the software vendor needs to introduce an effective methodology in order to eliminate unnecessary activities. All these six criteria are gathered under the title of vendor related criteria.

The ease of customization de<sup>fi</sup>nes the ability of the ERP system vendor to adopt its generic software solution to the company's speci<sup>fi</sup>c needs. It is important that the selected software can be implemented with current organizational structure. Providing <sup>fi</sup>tness with parent/allied organizations can affect both the decision process for some companies and whole ERP project success. An ERP system consists of various modules. The more an ERP system is better integrated, the more it becomes effective. These four criteria constitute customer related criteria.

Functionality is de<sup>fi</sup>ned as the most important evaluation factor [18]. The solution should have enough or even more modules related to companies' core activities such as human resources, material management, project management, production planning, supply chain management, etc. [7]. The selected ERP solution should address the current trends in IT, which is referred as technical aspects. Setting realistic expectations for the overall cost and attractive prices are essential in the buying process, as the ERP system cost is generally very high.

The system reliability criterion consists of the answers to the questions such as “How long has the vendor been in the core ERP solution business?” or “Have its current users been satis<sup>fi</sup>ed with the package?”. In spite of the fact that there is not any single application that can do everything a company needs, the selected ERP solution has to be compatible with the home-grown systems and other specialized software products. The implementation time is closely related to the selected implementation strategy. More customization requires more time and hence, more cost.

![](/api/attachments/3WGUDM7B/fulltext/images/6afa046355cecf08fc23866bd6188daff30b1c968bb3d67d172bfad07d7d23fa.jpg)  
Fig. 1. Flowchart of the proposed methodology [17].

## 3.3. Proposed decision framework

The proposed decision model consists of three levels. At the highest level the objective of the problem (selecting the best ERP software) is situated. In the second level, the criteria are listed. The lowest level belongs to the alternatives. As alternatives, $A _ { 1 } , A _ { 2 } , A _ { 3 }$ and A are selected since they are in the same interval of price. Furthermore, the interactions among criteria and sub-criteria are illustrated in Fig. 2. In the proposed hierarchy, outer dependencies and inner dependencies among sub-criteria as well as interaction between criteria are assumed to be present.

## 4. Numerical application of the proposed framework

## 4.1. Part 1: ANP

In the <sup>fi</sup>rst part of the framework, pairwise comparison matrices for all the sub-criteria have been prepared and <sup>fi</sup>lled out by the DM. The consistency indexes of the matrices are all smaller than 0.10, which proves their consistency [29]. The pairwise comparisons enable us to retrieve relative weights for the sub-criteria. The supermatrix, which has the role of obtaining the composite weights, has been constructed (Table 3).

Table 2 Selection criteria.

<table><tr><td> $C_{1}$ </td><td>Vendor related criteria (VRC)</td></tr><tr><td> $C_{11}$ </td><td>Support and service</td></tr><tr><td> $C_{12}$ </td><td>Vision</td></tr><tr><td> $C_{13}$ </td><td>Market position</td></tr><tr><td> $C_{14}$ </td><td>Domain knowledge</td></tr><tr><td> $C_{15}$ </td><td>Reputation</td></tr><tr><td> $C_{16}$ </td><td>Methodology of software</td></tr><tr><td> $C_{2}$ </td><td>Customer related criteria (CRC)</td></tr><tr><td> $C_{21}$ </td><td>Ease of customization</td></tr><tr><td> $C_{22}$ </td><td>Better fit with organizational structure</td></tr><tr><td> $C_{23}$ </td><td>Fit with parent/allied organizational system</td></tr><tr><td> $C_{24}$ </td><td>Cross module integration</td></tr><tr><td> $C_{3}$ </td><td>Software related criteria (SRC)</td></tr><tr><td> $C_{31}$ </td><td>Functionality</td></tr><tr><td> $C_{32}$ </td><td>Technical aspects</td></tr><tr><td> $C_{33}$ </td><td>Cost</td></tr><tr><td> $C_{34}$ </td><td>System reliability</td></tr><tr><td> $C_{35}$ </td><td>Compatibility</td></tr><tr><td> $C_{36}$ </td><td>Implementation time</td></tr></table>

![](/api/attachments/3WGUDM7B/fulltext/images/9b217166c59ea3cac5e4a8340dc34774709e881eb8a1c051ef9510a2a8f5fd75.jpg)  
Fig. 2. Interactions among criteria.

As the next step, cluster/criteria comparison matrices have been prepared and <sup>fi</sup>lled out by the DM in order to normalize the supermatrix (Table 3). Using the weights retrieved from these matrices, the cluster matrix is constructed and weighted supermatrix is calculated. The cluster matrix and the weighted supermatrix are represented in Tables 4 and 5, respectively.

As the <sup>fi</sup>nal step of ANP procedure, from the weighted supermatrix given in Table 5, the limit supermatrix has been calculated. The relative importance of the sub-criteria have been collected and then normalized with respect to the criteria (Table 6).

## 4.2. Part 2: CI

In order to <sup>fi</sup>nd out criteria weights and conjunctive/disjunctive interactions between criteria, a preferential ranking, including the strength of the judgment, has been asked to the DM. The following ranking has been obtained:

$$
C _ {1} \& C _ {3} \succ^ {M} C _ {1} \& C _ {2} \succ^ {W} C _ {2} \& C _ {3} \succ^ {M} C _ {1} \succ^ {W} C _ {3} \succ^ {S} C _ {2} \succ^ {S} 0 ^ {\prime \prime}
$$

Using Eqs. (2)–(5), we have obtained the following equation system:

$$
\left\{ \begin{array}{l} p _ {A g} ^ {(1, 0, 1)} - p _ {A g} ^ {(1, 1, 0)} = 3 \alpha = \varphi_ {3} - \varphi_ {2} - \frac {1}{2} [ I _ {1 2} - I _ {1 3} ] \\ p _ {A g} ^ {(1, 1, 0)} - p _ {A g} ^ {(0, 1, 1)} = 2 \alpha = \varphi_ {1} - \varphi_ {3} - \frac {1}{2} [ I _ {2 3} - I _ {1 2} ] \\ p _ {A g} ^ {(0, 1, 1)} - p _ {A g} ^ {(1, 0, 0)} = 3 \alpha = 1 - 2 \varphi_ {1} \\ p _ {A g} ^ {(1, 0, 0)} - p _ {A g} ^ {(0, 0, 1)} = 2 \alpha = \varphi_ {1} - \varphi_ {3} - \frac {1}{2} [ I _ {1 2} - I _ {2 3} ] \\ p _ {A g} ^ {(0, 0, 1)} - p _ {A g} ^ {(0, 1, 0)} = 4 \alpha = \varphi_ {3} - \varphi_ {2} - \frac {1}{2} [ I _ {1 3} - I _ {1 2} ] \\ p _ {A g} ^ {(0, 1, 0)} - p _ {A g} ^ {(0, 0, 0)} = 4 \alpha = \varphi_ {2} - \frac {1}{2} [ I _ {1 2} + I _ {2 3} ] \\ p _ {A g} ^ {(1, 1, 1)} = 1 = \varphi_ {1} + \varphi_ {2} + \varphi_ {3} \end{array} \right.
$$

The resolution of this equation system has given the results shown in Table 7:

Table 7 shows that vendor related criteria is the most important cluster for the DM with a relative importance $\left( \varphi _ { 1 } \right)$ of 0.4375, whereas customer related criteria is the least important with a relative importance (φ ) of 0.2083. Furthermore, it is possible to state that an employee must be successful on both VRC and CRC in order to be considered successful for the DM. The same situation is valid for CRC and SRC, as the interaction values $\left( I _ { 1 2 } \right.$ and $I _ { 2 3 } )$ are positive for those couples of cri-

Unweighted supermatrix.

<table><tr><td></td><td>S&amp;S</td><td>V</td><td>MP</td><td>DK</td><td>REP</td><td>MS</td><td>EC</td><td>BFOS</td><td>FPAOS</td><td>CMI</td><td>F</td><td>TA</td><td>C</td><td>SR</td><td>CP</td><td>IT</td></tr><tr><td>S&amp;S</td><td>0</td><td>0</td><td>0.07</td><td>0</td><td>0.25</td><td>0</td><td>0.39</td><td>0.25</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0.11</td><td>0</td><td>0</td><td>0.11</td></tr><tr><td>V</td><td>0.75</td><td>0</td><td>0.15</td><td>1</td><td>0.75</td><td>1</td><td>0.07</td><td>0</td><td>0</td><td>0</td><td>0.25</td><td>0</td><td>0</td><td>0.17</td><td>0.13</td><td>0</td></tr><tr><td>MP</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.64</td><td>0</td><td>0</td><td>0</td></tr><tr><td>DK</td><td>0.25</td><td>0</td><td>0.39</td><td>0</td><td>0</td><td>0</td><td>0.39</td><td>0.75</td><td>0</td><td>0</td><td>0.75</td><td>0</td><td>0</td><td>0.83</td><td>0.88</td><td>0.26</td></tr><tr><td>REP</td><td>0</td><td>0</td><td>0.39</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.26</td><td>0</td><td>0</td><td>0</td></tr><tr><td>MS</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.15</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.64</td></tr><tr><td>EC</td><td>0.64</td><td>0</td><td>0.43</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.43</td><td>0.25</td><td>1</td><td>0.08</td><td>0.19</td><td>0</td><td>0</td><td>0.15</td><td>0.38</td></tr><tr><td>BFOS</td><td>0.11</td><td>0</td><td>0.14</td><td>0</td><td>0</td><td>0</td><td>0.09</td><td>0</td><td>0</td><td>0</td><td>0.20</td><td>0.08</td><td>0</td><td>0</td><td>0.39</td><td>0.13</td></tr><tr><td>FPAOS</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.46</td><td>0.43</td><td>0</td><td>0</td><td>0.20</td><td>0.08</td><td>0</td><td>0.75</td><td>0.39</td><td>0.38</td></tr><tr><td>CMI</td><td>0.26</td><td>0</td><td>0.43</td><td>0</td><td>0</td><td>0</td><td>0.46</td><td>0.14</td><td>0.75</td><td>0</td><td>0.52</td><td>0.66</td><td>0</td><td>0.25</td><td>0.07</td><td>0.13</td></tr><tr><td>F</td><td>0</td><td>0</td><td>0.05</td><td>0</td><td>0</td><td>0</td><td>0.25</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.19</td><td>0.25</td><td>0</td><td>0.26</td></tr><tr><td>TA</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.75</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0.07</td><td>0.75</td><td>1</td><td>0.11</td></tr><tr><td>C</td><td>0</td><td>0</td><td>0.48</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.73</td><td>0.64</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>SR</td><td>1</td><td>0</td><td>0.21</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.26</td><td>0.19</td><td>0</td><td>0</td><td>0</td></tr><tr><td>CP</td><td>0</td><td>0</td><td>0.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0.18</td><td>0.11</td><td>0.07</td><td>0</td><td>0</td><td>0.64</td></tr><tr><td>IT</td><td>0</td><td>0</td><td>0.21</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.08</td><td>0</td><td>0.47</td><td>0</td><td>0</td><td>0</td></tr></table>

Cluster matrix.  
Table 5  
Table 4

<table><tr><td></td><td>VRC</td><td>CRC</td><td>SRC</td></tr><tr><td>VRC</td><td>0.637</td><td>0.258</td><td>0.258</td></tr><tr><td>CRC</td><td>0.105</td><td>0.637</td><td>0.105</td></tr><tr><td>SRC</td><td>0.258</td><td>0.105</td><td>0.637</td></tr></table>

terion. On the other hand, there is no conjunctive/disjunctive interaction between VRC and SRC as the interaction value for these $\left( I _ { 1 3 } \right)$ is null.

## 4.3. Part 3: relative performance scores of alternatives

For each sub-criterion, the DM has been asked to give us a preferential ranking, including the strength of the comparisons. For VRC, the following ranking has been obtained.

$$
\begin{array}{l} C _ {1 1} \to G o o d \succ^ {V W} A _ {4} \succ^ {M} A _ {1} \succ^ {M} A _ {2} \succ^ {M} A _ {3} \succ^ {M} N e u t r a l \\ C _ {1 2} \to G o o d \succ^ {V W} A _ {1} \succ^ {W} A _ {2} \succ^ {M} A _ {3} \succ^ {S} A _ {4} \succ^ {S} N e u t r a l \\ C _ {1 3} \to G o o d \succ^ {V W} A _ {4} \succ^ {W} A _ {1} \succ^ {M} A _ {2} \succ^ {S} A _ {3} \succ^ {S} N e u t r a l \\ C _ {1 4} \to G o o d \succ^ {V W} A _ {1} \succ^ {W} A _ {2} \succ^ {M} A _ {4} \succ^ {M} A _ {3} \succ^ {S} N e u t r a l \\ C _ {1 5} \to G o o d \succ^ {V W} A _ {1} \succ^ {W} A _ {2} \succ^ {M} A _ {4} \succ^ {S} A _ {3} \succ^ {S} N e u t r a l \\ C _ {1 6} \to G o o d \succ^ {V W} A _ {1} \succ^ {W} A _ {2} \succ^ {M} A _ {3} \succ^ {S} A _ {4} \succ^ {S} N e u t r a l \end{array}
$$

For CRC, the following ranking has been obtained.

$$
\begin{array}{l} C _ {2 1} \to G o o d \succ^ {W} A _ {4} \succ^ {M} A _ {3} \succ^ {M} A _ {2} \succ^ {M} A _ {1} \succ^ {M} N e u t r a l \\ C _ {2 2} \to G o o d \succ^ {M} A _ {2} \succ^ {M} A _ {1} \succ^ {S} A _ {3} \succ^ {M} A _ {4} \succ^ {M} N e u t r a l \\ C _ {2 3} \to G o o d \succ^ {M} A _ {2} \succ^ {M} A _ {1} \succ^ {S} A _ {3} \succ^ {M} A _ {4} \succ^ {M} N e u t r a l \\ C _ {2 4} \to G o o d \succ^ {M} A _ {3} \succ^ {W} A _ {1} \succ^ {W} A _ {2} \succ^ {S} A _ {4} \succ^ {M} N e u t r a l \end{array}
$$

For SRC, the following ranking has been obtained.

$$
\begin{array}{l} C _ {3 1} \to G o o d \succ^ {V W} A _ {2} \succ^ {M} A _ {1} \succ^ {M} A _ {3} \succ^ {M} A _ {4} \succ^ {S} N e u t r a l \\ C _ {3 2} \to G o o d \succ^ {W} A _ {1} \succ^ {W} A _ {2} \succ^ {M} A _ {3} \succ^ {M} A _ {4} \succ^ {S} N e u t r a l \\ C _ {3 3} \to G o o d \succ^ {M} A _ {4} \succ^ {S} A _ {3} \succ^ {S} A _ {2} \succ^ {M} A _ {1} \succ^ {V W} N e u t r a l \\ C _ {3 4} \to G o o d \succ^ {W} A _ {1} \succ^ {W} A _ {2} \succ^ {S} A _ {3} \succ^ {M} A _ {4} \succ^ {S} N e u t r a l \\ C _ {3 5} \to G o o d \succ^ {M} A _ {1} \succ^ {W} A _ {2} \succ^ {S} A _ {3} \succ^ {M} A _ {4} \succ^ {M} N e u t r a l \\ C _ {3 6} \to G o o d \succ^ {M} A _ {4} \succ^ {S} A _ {3} \succ^ {S} A _ {2} \succ^ {W} A _ {1} \succ^ {W} N e u t r a l \end{array}
$$

The equation systems have been retrieved from these three preference rankings, using Eq. (2). The resolution of these equation systems are summarized in Table 8.

Table 6  
Sub-criteria weights.

<table><tr><td>VRC</td><td>S&amp;S</td><td>V</td><td>MP</td><td>DK</td><td>REP</td><td>MS</td></tr><tr><td>wCRC</td><td>0.138EC</td><td>0.473BFOS</td><td>0.065FPAOS</td><td>0.235CMI</td><td>0.045</td><td>0.044</td></tr><tr><td>wSRC</td><td>0.422F</td><td>0.049TA</td><td>0.202C</td><td>0.327SR</td><td>CP</td><td>IT</td></tr><tr><td>w</td><td>0.099</td><td>0.276</td><td>0.238</td><td>0.159</td><td>0.126</td><td>0.102</td></tr></table>

## 4.4. Part 4: final aggregation

As the last step of the proposed procedure, the scores of the alternatives for each criterion have been calculated (Table 9).

In order to determine the <sup>fi</sup>nal performance scores of four alternatives (Table 10), we have used the values in Tables 7 and 9 and Eq. (1).

## 5. Discussion

The result indicates that the <sup>fi</sup>nal performance score of alternative $A _ { 1 }$ is the highest (0.6867) and that of alternative $A _ { 4 }$ is the lowest (0.4705). The fact that VRC has the greatest relative importance $( \phi _ { 1 } = 0 . 4 3 7 5 )$ has played an important role for $A _ { 1 }$ and $A _ { 2 }$ to be ranked <sup>fi</sup>rst two in the <sup>fi</sup>nal ranking and for $A _ { 3 }$ and $A _ { 4 }$ to be ranked last two. Although $A _ { 2 }$ has greater performance values for CRC and SRC (albeit the difference between the performance values of those two with respect to SRC is signi<sup>fi</sup>cantly low), VRC was the de<sup>fi</sup>ning criteria for $A _ { 1 }$ to be ranked <sup>fi</sup>rst. The same situation is present between $A _ { 3 }$ and $A _ { 4 } { : } A _ { 4 }$ has lower performance values with respect to CRC and SRC and greater performance value with respect to VRC. However in this case, $A _ { 3 }$ is ranked before $A _ { 4 } .$ The reason is the fact that the differences between performance values with respect to CRC and SRC for those two alternatives are greater than that for $A _ { 1 }$ and $A _ { 2 } .$

If we were to ignore the interactions and solve the model with the expert judgments given to us, for our numerical application, the <sup>fi</sup>nal ranking would be $A _ { 4 } { > } A _ { 1 } { > } A _ { 2 } { > } A _ { 3 }$ with the respective relative weights 0.614, 0.596, 0.584 and 0.446. As it can be observed, the ranking has dramatically changed. The worst performing alternative has become the best performing one. This is not the proof that the result will be different in each and every case or the changes will be as dramatic as this example. However, this demonstrates the fact that the <sup>fi</sup>nal ranking may change with the ignorance of the interactions and therefore it may lead us to erroneous conclusions and decisions.

Weighted supermatrix.

<table><tr><td></td><td>S&amp;S</td><td>V</td><td>MP</td><td>DK</td><td>REP</td><td>MS</td><td>EC</td><td>BFOS</td><td>FPAOS</td><td>CMI</td><td>F</td><td>TA</td><td>C</td><td>SR</td><td>CP</td><td>IT</td></tr><tr><td>S&amp;S</td><td>0</td><td>0</td><td>0.043</td><td>0</td><td>0.178</td><td>0</td><td>0.101</td><td>0.072</td><td>0.258</td><td>0</td><td>0</td><td>0</td><td>0.030</td><td>0</td><td>0</td><td>0.027</td></tr><tr><td>V</td><td>0.478</td><td>0</td><td>0.097</td><td>1</td><td>0.534</td><td>1</td><td>0.018</td><td>0</td><td>0</td><td>0</td><td>0.07</td><td>0</td><td>0</td><td>0.043</td><td>0.033</td><td>0</td></tr><tr><td>MP</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.184</td><td>0</td><td>0</td><td>0</td></tr><tr><td>DK</td><td>0.159</td><td>0</td><td>0.248</td><td>0</td><td>0</td><td>0</td><td>0.101</td><td>0.216</td><td>0</td><td>0</td><td>0.19</td><td>0</td><td>0</td><td>0.215</td><td>0.226</td><td>0.067</td></tr><tr><td>REP</td><td>0</td><td>0</td><td>0.248</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.075</td><td>0</td><td>0</td><td>0</td></tr><tr><td>MS</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.039</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.165</td></tr><tr><td>EC</td><td>0.067</td><td>0</td><td>0.045</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.305</td><td>0.159</td><td>0.87</td><td>0.01</td><td>0.027</td><td>0</td><td>0</td><td>0.016</td><td>0.039</td></tr><tr><td>BFOS</td><td>0.011</td><td>0</td><td>0.015</td><td>0</td><td>0</td><td>0</td><td>0.058</td><td>0</td><td>0</td><td>0</td><td>0.02</td><td>0.011</td><td>0</td><td>0</td><td>0.041</td><td>0.013</td></tr><tr><td>FPAOS</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.290</td><td>0.305</td><td>0</td><td>0</td><td>0.02</td><td>0.011</td><td>0</td><td>0.079</td><td>0.041</td><td>0.039</td></tr><tr><td>CMI</td><td>0.027</td><td>0</td><td>0.045</td><td>0</td><td>0</td><td>0</td><td>0.290</td><td>0.102</td><td>0.478</td><td>0</td><td>0.05</td><td>0.093</td><td>0</td><td>0.026</td><td>0.007</td><td>0.013</td></tr><tr><td>F</td><td>0</td><td>0</td><td>0.013</td><td>0</td><td>0</td><td>0</td><td>0.026</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.138</td><td>0.159</td><td>0</td><td>0.165</td></tr><tr><td>TA</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.079</td><td>0</td><td>0</td><td>0.14</td><td>0</td><td>0</td><td>0.052</td><td>0.478</td><td>0.637</td><td>0.067</td></tr><tr><td>C</td><td>0</td><td>0</td><td>0.124</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.47</td><td>0.547</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>SR</td><td>0.258</td><td>0</td><td>0.055</td><td>0</td><td>0.289</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.222</td><td>0.138</td><td>0</td><td>0</td><td>0</td></tr><tr><td>CP</td><td>0</td><td>0</td><td>0.013</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.105</td><td>0</td><td>0.12</td><td>0.090</td><td>0.052</td><td>0</td><td>0</td><td>0.406</td></tr><tr><td>IT</td><td>0</td><td>0</td><td>0.055</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.05</td><td>0</td><td>0.332</td><td>0</td><td>0</td><td>0</td></tr></table>

Table 10  
Table 7  
Choquet integral parameters.

<table><tr><td>Parameter</td><td> $\Phi_1$ </td><td> $\Phi_2$ </td><td> $\Phi_3$ </td><td> $I_{12}$ </td><td> $I_{13}$ </td><td> $I_{23}$ </td></tr><tr><td>Value</td><td>0.4375</td><td>0.2083</td><td>0.3542</td><td>0.0417</td><td>0</td><td>0.0417</td></tr></table>

## 6. Conclusion

ERP systems have a vital role in today's organizations, however they have high costs and high implementation risks. Therefore, evaluating the offered ERP systems and selecting the most suitable one among them is a challenging task. With the increase in the number of requirements, the selection problem becomes more complex to solve, and the companies need to make their decisions in increasingly complex environments.

Our work presents a comprehensive framework for selecting a suitable ERP system based on a hybrid multicriteria decision analysis process. The procedure consists of three methodologies: Analytic Network Process (ANP), Choquet Integral (CI) and Measuring Attractiveness by a Categorical Based Evaluation Technique (MACBETH). We have illustrated the applicability of the framework through a case study of the ERP software selection of a company. The proposed decision making framework is <sup>fl</sup>exible enough to <sup>fi</sup>t other sectors with some speci<sup>fi</sup>c characteristic changes and to incorporate different criteria in the evaluation process.

Besides proposing a hybrid MCDM model for ERP selection problem, what we would also like to underline with this study is the importance of not ignoring the interactions among different elements of a decision model. Moreover as it is discussed in the previous section, we can say that ignoring the interactions may lead us to obtain a different <sup>fi</sup>nal ranking, hence making a bad decision according to the wrong conclusions.

## Appendix A

Let μ be a non-monotonic fuzzy measure on X and $f \mathsf { a }$ function on X with range $\{ a _ { 1 } , a _ { 2 } , . . . , a _ { n } , \}$ where $a _ { 1 } \leq a _ { 2 } \leq \ldots \leq a _ { n } .$ . The CI $( C ) \int f ( x ) d \mu ( x )$ or simply $( C ) \int f d \mu \circ \mathrm { f } f$ with respect to μ is de<sup>fi</sup>ned as follows:

$$
(C) \int f d \mu = \sum_ {i = 1} ^ {n} (a _ {i} - a _ {i - 1}). \mu (\{x | f (x) \geq a _ {i} \}) \text { where } a _ {0} = 0\tag{A.1}
$$

Since a fuzzy measure de<sup>fi</sup>ned on a set of n elements requires 2n real coef<sup>fi</sup>cients for its de<sup>fi</sup>nition, k-additive measures have been introduced by Grabisch [15] in order to decrease the exponential complexity of fuzzy measures in practical applications. In a k-additive CI the interactions of higher order than k will not be taken in consideration or they will be considered null. Therefore, k-additive measures can be represented by a limited set of coef<sup>fi</sup>cients, at most $\sum _ { i = 1 } ^ { k } C _ { i } ^ { n }$

Table 8  
Performance values of alternatives with respect to sub-criteria.  
Table 9  
Performance values of alternatives with respect to criteria.

<table><tr><td></td><td>VRC</td><td>CRC</td><td>SRC</td></tr><tr><td> $A_1$ </td><td>0.8854</td><td>0.5042</td><td>0.5754</td></tr><tr><td> $A_2$ </td><td>0.7232</td><td>0.5950</td><td>0.5803</td></tr><tr><td> $A_3$ </td><td>0.4310</td><td>0.5760</td><td>0.4934</td></tr><tr><td> $A_4$ </td><td>0.4877</td><td>0.4788</td><td>0.4467</td></tr></table>

Final scores of alternatives.

<table><tr><td></td><td> $A_{1}$ </td><td> $A_{2}$ </td><td> $A_{3}$ </td><td> $A_{4}$ </td></tr><tr><td>Score</td><td>0.6867</td><td>0.6429</td><td>0.4786</td><td>0.4705</td></tr></table>

## Appendix B

Shapley indices and interactions for the criteria can be calculated using fuzzy measures with the following formula:

$$
\varphi_ {i} = \sum_ {K \subset X \setminus \{i \}} \frac {(n - | K | - 1) ! | K | !}{n !} [ \mu (K \cup \{i \}) - \mu (K) ]\tag{B.1}
$$

$$
I _ {i j} = \sum_ {K \subset N \setminus \{i, j \}} \frac {(n - | K | - 2) ! | K | !}{(n - 1) !} [ \mu (K \cup \{i, j \}) - \mu (K \cup \{i \}) - \mu (K \cup \{j \}) + \mu (K) ]\tag{B.2}
$$

## References

[1] B. Baki, K. Çakar, Determining the ERP package-selecting criteria: the case of Turkish manufacturing companies, Business Process Management Journal 11 (1) (2005) 75–86.

[2] C.A. Bana e Costa, Structuration, Construction et Exploitation d'un Modèle à Multi-critère d'aide à la Décision PhD Thesis Technical University of Lisbon Lis bon, 1992.

[3] C.A. Bana e Costa, M.P. Chagas, A career choice problem: an example of how to use MACBETH to build a quantitative value model based on qualitative value judg ments, European Journal of Operational Research 153 (2004) 323–331.

[4] C.A. Bana e Costa, J.M. De Corte, J.C. Vansnick, On the mathematical foundations of MACBETH, Working Paper LSEOR, 03, London School of Economics and Political Science, 2004, p. 56.

[5] C.A. Bana e Costa, C.S. Oliveira, V. Vieira, Prioritization of bridges and tunnels in earthquake risk mitigation using multicriteria decision analysis: application to Lisbon, Omega 36 (2008) 442–450.

[6] L. Berrah, G. Mauris, J. Montmain, Monitoring the improvement of an overall industrial performance based on a Choquet integral aggregation, Omega 36 (2008) 340–351.

[7] G. Brewer, On the road to successful ERP, Instrumentation & Control Systems 73 (5) (2000) 49–58.

[8] G. Campanella, R.A. Ribeiro, A framework for dynamic multiple-criteria decision making, Decision Support Systems 52 (2011) 52–60.

[9] U. Cebeci, Fuzzy AHP-based decision support system for selecting ERP systems in textile industry by using balanced scorecard, Expert Systems with Applications 36 (2009) 8900–8909.

[10] E.W.L. Cheng, H. Li, L. Yu, The Analytic Network Process (ANP) approach to location selection: a shopping mall illustration, Construction Innovation 5 (2004) 83–97.

[11] G. Choquet, Theory of capacities, Annales de l'Institut Fourier 5 (1953) 131–295.

[12] V. Clivillé, L. Berrah, G. Mauris, Quantitative expression and aggregation of performance measurements based on MACBETH multicriteria method, International Journal of Production Economics 105 (1) (2007) 171–189.

[13] T.H. Davenport, Putting the enterprise into the enterprise system, Harvard Business Review 76 (4) (1998) 121–131.

<table><tr><td></td><td> $C_{11}$ </td><td> $C_{12}$ </td><td> $C_{13}$ </td><td> $C_{14}$ </td><td> $C_{15}$ </td><td> $C_{16}$ </td><td> $C_{21}$ </td><td> $C_{22}$ </td><td> $C_{23}$ </td><td> $C_{24}$ </td><td> $C_{31}$ </td><td> $C_{32}$ </td><td> $C_{33}$ </td><td> $C_{34}$ </td><td> $C_{35}$ </td><td> $C_{36}$ </td></tr><tr><td> $A_1$ </td><td>0.692</td><td>0.929</td><td>0.786</td><td>0.923</td><td>0.929</td><td>0.929</td><td>0.214</td><td>0.625</td><td>0.625</td><td>0.786</td><td>0.714</td><td>0.857</td><td>0.067</td><td>0.867</td><td>0.800</td><td>0.133</td></tr><tr><td> $A_2$ </td><td>0.462</td><td>0.786</td><td>0.571</td><td>0.769</td><td>0.786</td><td>0.786</td><td>0.429</td><td>0.813</td><td>0.813</td><td>0.643</td><td>0.929</td><td>0.714</td><td>0.267</td><td>0.733</td><td>0.667</td><td>0.267</td></tr><tr><td> $A_3$ </td><td>0.231</td><td>0.571</td><td>0.286</td><td>0.308</td><td>0.286</td><td>0.571</td><td>0.643</td><td>0.563</td><td>0.563</td><td>0.500</td><td>0.500</td><td>0.500</td><td>0.533</td><td>0.467</td><td>0.400</td><td>0.533</td></tr><tr><td> $A_4$ </td><td>0.923</td><td>0.286</td><td>0.929</td><td>0.538</td><td>0.571</td><td>0.286</td><td>0.857</td><td>0.188</td><td>0.188</td><td>0.214</td><td>0.286</td><td>0.286</td><td>0.800</td><td>0.267</td><td>0.200</td><td>0.800</td></tr></table>

[14] Y.C. Erensal, E. Albayrak, Successful adoption of macroergonomics in manufacturing: using a multicriteria decision-making methodology-analytic hierarchy process, Human Factors and Ergonomics in Manufacturing 14 (4) (2005) 353–377.

[15] M. Grabisch, k-order additive fuzzy measures, 6th International Conference on Information Progressing and Management of Uncertainty, Fuzziness and Knowledge Based Systems 5 (1997) 587–607.

[16] T. Gürbüz, Multiple criteria human performance evaluation using Choquet integral, International Journal of Computational Intelligence Systems 3 (3) (2010) 290–300.

[17] T. Gürbüz, Multicriteria Decision Making Approach to Human Resources Perfor mance Evaluation. Ph.D. Thesis, Galatasaray University, Turkey, 2010.

[18] B. Hecht, Choose the right ERP software, Datamation 43 (3) (1997) 56–58.

[19] C.W. Holsapple, M.P. Sena, ERP plans and decision-support bene<sup>fi</sup>ts, Decision Support Systems 38 (2005) 575–590.

[20] G. Işıklar Alptekin, G. Büyüközkan, An integrated case-based reasoning and MCDM system for web based tourism destination planning, Expert Systems with Applications 38 (3) (2011) 2125–2132.

[21] U. Jung, D.W. Seo, An ANP approach for R&D project evaluation based on interdependencies between research objectives and evaluation criteria, Decision Support Systems 49 (2010) 335–342.

[22] E.E. Karsak, C.O. Ozogul, An integrated decision making approach for ERP system selection, Expert Systems with Applications 36 (2009) 660–667.

[23] C. Labreuche, M. Grabisch, The Choquet integral for the aggregation of interval scales in multicriteria decision making, Fuzzy Sets and Systems 137 (1) (2003) 11–26.

[24] F. Montignac, I. Noirot, S. Chaudourne, Multi-criteria evaluation of on-board hydrogen storage technologies using the MACBETH approach, International Journal of Hydrogen Energy 34 (10) (2009) 4561–4568.

[25] T. Murofushi, M. Sugeno, An interpretation of fuzzy measure and the Choquet integral as an integral with respect to a fuzzy measure, Fuzzy Sets Systems 29 (1989) 201–227.

[26] J.C. Pomerol, S. Barba Romero, Multicriterion Decision in Management: Principles and Practice, 1st edition Kluwer Academic Publishers, Norwell, 2000.

[27] M. Roubens, A. Rusinowska, H. de Swart, Using MACBETH to determine utilities of governments to parties in coalition formation, European Journal of Operational Research 172 (2006) 588–603.

[28] I. Saad, S. Hammadi, M. Benrejeb, P. Borne, Choquet integral for criteria aggregation in the <sup>fl</sup>exible job-shop scheduling problems, Mathematics and Computers in Simulation 76 (5-6) (2008) 447-462.

[29] T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

[30] T.L. Saaty, Decision Making with Dependence and Feedback: The Analytic Net work Process, RWS Publications, Pittsburgh, 1996

[31] R.W. Saaty, Decision Making in Complex Environments, Creative Decisions Foundation, Pittsburgh, 2003.

[32] M.J. Verdecho, J.J. Alfaro-Saiz, R. Rodriguez-Rodriguez, Prioritization and management of inter-enterprise collaborative performance, Decision Support Systems 53 (1) (2012) 142–153.

[33] C.C. Wei, C.F. Chien, M.J.J. Wang, An AHP-based approach to ERP system selection, International Journal of Production Economics 96 (2005) 47–62.

[34] H.R. Yazgan, S. Boran, K. Göztepe, An ERP software selection process with using arti<sup>fi</sup>cial neural network based on Analytic Network Process approach, Expert Systems with Applications 36 (2009) 9214–9222

Tuncay Gürbüz, completed his B.Sc. on Industrial Engineering in the Industrial Engineering Department of Galatasaray University in 2000, his M.Sc. and Ph.D. on Industrial Engineering in the Institute of Science and Engineering of Galatasaray University in 2003 and 2010 respectively. His research interests and focus are in the areas of multiple criteria decision making, decision support systems, fuzzy logic and performance evaluation. He is currently a research assistant in Industrial Engineering Department of Galatasaray University.

S. Emre Alptekin received his B.Sc. degree in Industrial Engineering in1999 from Istanbul Technical University, his M.Sc. and Ph.D. degrees in Industrial Engineering from Galatasaray University in 2001 and 2006, respectively. He is currently an assis tant professor in Galatasaray University. His research interests contain multi-criteria and expert decision analysis systems.

Gülfem Işıklar Alptekin received her B.Sc. degree in Computer Science in 2001, her M.Sc. degree in Industrial Engineering from Galatasaray University in 2003, and her Ph.D. degree in Computer Engineering from Boğaziçi University in 2010. She is currently an assistant professor in Galatasaray University. Her research interests contain pricing and resource allocation models in next generation wireless networks and multi-criteria decision support systems in real life applications

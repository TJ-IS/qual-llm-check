---
otero_id: 7036
otero_key: "28P4TS23"
title: "A multicriteria decision support system for bank rating"
authors: "Michael Doumpos; Constantin Zopounidis"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.07.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A multicriteria decision support system for bank rating

Michael Doumpos ⁎, Constantin Zopounidis

Technical University of Crete, Dept. of Production Engineering and Management, Financial Engineering Laboratory, University Campus, 73100 Chania, Greece

a r t i c l e i n f o

Article history: Received 14 December 2009 Received in revised form 11 June 2010 Accepted 14 July 2010 Available online 1 August 2010

Keywords: Banking Financial risk management Decision support systems Multicriteria decision aid Sensitivity analysis

## a b s t r a c t

Bank rating refers to the analysis of a bank's overall viability, performance and risk exposure. Within the recent <sup>fi</sup>nancial turmoil, bank rating has become extremely important. Typically, bank rating is performed through empirical procedures that combine <sup>fi</sup>nancial and qualitative data into an overall performance index. This paper presents a case study on the implementation of a multicriteria approach to bank rating. The proposed methodology is based on the PROMETHEE II method implemented in an integrated decision support system. Special emphasis is put on the sensitivity of the results with regard to the relative importance of the evaluation criteria and the parameters of the evaluation process.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Banks have a prominent role in the <sup>fi</sup>nancial and business environment. The increasing risks that banks face, have led to the introduction of the new regulatory framework of Basel II, which de<sup>fi</sup>nes the core principles for <sup>fi</sup>nancial risk management in banking institutions. One of the pillars of this framework involves the banking supervision process. The central banks that are responsible for supervising the banks in each country use rating systems to assess the soundness of the banks. According to Sahajwala and Van den Bergh [29], the emphasis is put on the development of formal, structured and quanti<sup>fi</sup>ed assessments taking into account the <sup>fi</sup>nancial performance of banks as well as their underlying risk pro<sup>fi</sup>le and risk management capabilities. Such assessments support the supervisors and examiners in identifying changes in banks' condition as early as possible.

Due to lack of suf<sup>fi</sup>cient historical data about bank defaults, bank rating systems are usually based on empirical assessment techniques. Sahajwala and Van den Bergh [29] provide an extensive overview of several systems, which are currently used in practice. The most popular approach is based on the CAMELS framework, which involves the consideration of six major factors: Capital, Assets, Management, Earnings, Liquidity, and Sensitivity to market risk. Speci<sup>fi</sup>c criteria within these categories are usually aggregated in a simple weighted average model.

Several multicriteria techniques have also been used for the evaluation of bank performance. Kosmidou and Zopounidis [18], Mareschal and

Brans [21], as well as Mareschal and Mertens [22] used the PROMETHEE method, Spathis et al. [30] and Zopounidis et al. [33] used disaggregation techniques, Raveh [26] used the Co-plot method, whereas Ho [13] applied grey relational analysis, and Garcia et al. [9] used goal programming. Several data envelopment analysis models have also been used for ef<sup>fi</sup>ciency analysis (e.g., [10,12,17,25,31]). Considerable work has also been done on analyzing/predicting bank ratings and failures, using statistical methods [2,7,19], and data mining techniques [3,11,14,20,27]. The recent work of Fethi and Pasiouras [8] provides an up to date comprehensive review of ef<sup>fi</sup>ciency analysis and performance evaluation in the banking sector, focusing on the applications of data envelopment analysis and other methods from the <sup>fi</sup>elds of operations research and arti<sup>fi</sup>cial intelligence.

Together with the development and application of new methodological approaches, the design of decision support systems is also important for the banking sector. Such systems can be used in a wide range of activities within a banking institution, beginning from loan evaluation and credit granting [1,16], <sup>fi</sup>nancial planning [6], business process reengineering [23], and asset/liability management [24].

This paper presents a case study on the development of a multicriteria bank rating approach and its implementation into an integrated decision support system, which is currently in use by the Bank of Greece. The proposed methodology is based on the PROMETHEE II method. The bank evaluation criteria are selected in cooperation with expert analysts from the Bank of Greece. The selected criteria comply with the CAMELS framework and include both qualitative and quantitative measures. Special emphasis is put on the sensitivity of the results with regard to the relative importance of the evaluation criteria, the parameters of the evaluation process, and the input data. Analytic sensitivity analysis techniques are used for this purpose, together with Monte Carlo simulation.

The rest of the paper is organized as follows. Section 2 describes the problem context and the details of the multicriteria methodology. Section 3 illustrates the implementation of the multicriteria decision support system. Finally, Section 4 concludes the paper and outlines some future research directions.

## 2. Problem context and multicriteria methodology

The main output of bank rating models is the classi<sup>fi</sup>cation of the banks into ordinal risk grades (groups). The number of risk grades is usually set to $5 ,$ with grade 1 indicating low risk/high performance banks and grade 5 indicating high risk/low performance banks. The overall performance is decomposed into partial scores (for each individual evaluation criterion).

In accordance, with the CAMELS model which is currently in use by the Bank of Greece, a multicriteria methodology has been implemented that enables not only the de<sup>fi</sup>nition of the required risk grades, but also the development of an overall performance index that enables comparisons on the relative performance of the banks. The methodology is based on the PROMETHEE II method [4]. The work<sup>fl</sup>ow of the methodology is given in Fig. 1.

The PROMETHEE method is widely used to rank a set of alternatives on the basis of pairwise comparisons. Except for this kind of analysis, the method was also used to perform an absolute evaluation in comparison to a pre-speci<sup>fi</sup>ed reference point. The subsections below provide details on the implementation of the PROMETHEE method in both these contexts. Details on the evaluation criteria and the implementation of the methodology into a decision support system are given in Section 3.

## 2.1. Relative evaluation

The evaluation of the banks in the context of the PROMETHEE method is based on pairwise comparisons. In particular, for each pair of banks $( i , j )$ the global preference index $P ( \mathbf { x } _ { i } , \mathbf { x } _ { j } )$ is computed, where $\mathbf { x } _ { i } = ( x _ { i 1 } , x _ { i 2 } , . . . , x _ { i n } )$ is the vector with the description of bank i on n evaluation criteria. The global preference index is de<sup>fi</sup>ned as the weighted sum of partial preference indices:

![](/api/attachments/28P4TS23/fulltext/images/08a7cf9f00eee6a7c1c5f3c8b4722ce90854732c4252496b8411ef4b6fbe702e.jpg)  
Fig. 1. Modeling methodology.

where w<sub>k</sub> is the weight of criterion k and $\pi _ { k } ( x _ { i k } , x _ { j k } )$ is the corresponding partial preference index, which measures (in a [0, 1] scale) the strength of the preference for bank i over bank j on criterion k

The partial preference index $\pi _ { k } \big ( x _ { i k } , x _ { j k } \big )$ is a function of the difference $x _ { i k } - x _ { j k }$ in the performances of the banks on criterion k. A popular choice is the Gaussian function:

$$
\pi_ {k} (x _ {i k}, x _ {j k}) = \left\{ \begin{array}{l l} 0 & \text {if} x _ {i k} \leq x _ {j k} \\ 1 - \exp \left[ - \frac {(x _ {i k} - x _ {j k}) ^ {2}}{2 \sigma_ {k} ^ {2}} \right] & \text {if} x _ {i k} > x _ {j k} \end{array} \right.
$$

where $\sigma _ { k } { > } 0$ is a user-de<sup>fi</sup>ned parameter. If a low value is used for $\sigma _ { k } ,$ then even a small difference $x _ { i k } - x _ { j k } > 0$ may lead to a signi<sup>fi</sup>cant preference for bank i over bank j. On the contrary, for large values of $\sigma _ { k } ,$ strict preference may only occur when $x _ { i k } \gg x _ { j k } .$

An alternative function for the de<sup>fi</sup>nition of the partial preference index is the linear generalized criterion:

$$
\pi_ {k} (x _ {i k}, x _ {j k}) = \left\{ \begin{array}{l l} 0 & \text { if } x _ {i k} - x _ {j k} \leq 0 \\ \frac {x _ {i k} - x _ {j k}}{p _ {k}} & \text { if } 0 <   x _ {i k} - x _ {j k} \leq p _ {k} \\ 1 & \text { if } x _ {i k} - x _ {j k} > p _ {k} \end{array} \right.
$$

where $p _ { k } { > } 0$ is the preference threshold, which de<sup>fi</sup>nes the minimum difference $x _ { i k } - x _ { j k }$ above which bank i is assumed to be strictly preferred over bank j on criterion k.

Assuming a set of m banks under evaluation, the results of all the pairwise comparisons are aggregated into a global performance index (net <sup>fl</sup>ow) as follows:

$$
\Phi (\mathbf {x} _ {i}) = \frac {1}{m - 1} \sum_ {j \neq i} \left[ P (\mathbf {x} _ {i}, \mathbf {x} _ {j}) - P (\mathbf {x} _ {j}, \mathbf {x} _ {i}) \right] = \sum_ {k = 1} ^ {n} w _ {k} \phi_ {k} (\mathbf {x} _ {i})
$$

where $\phi _ { k } ( \mathbf { x } _ { i } ) = \varphi _ { k } ^ { + } ( \mathbf { x } _ { i } ) { - } \varphi _ { k } ^ { - } ( \mathbf { x } _ { i } )$ is the partial evaluation score de<sup>fi</sup>ned for criterion k, with

$$
\varphi_ {k} ^ {+} (x _ {i k}) = \frac {1}{m - 1} \sum_ {j \neq i} \pi_ {k} (x _ {i k}, x _ {j k}) \quad \text {and} \quad \varphi_ {k} ^ {-} (x _ {i k}) = \frac {1}{m - 1} \sum_ {j \neq i} \pi_ {k} (x _ {j k}, x _ {i k})
$$

representing, the outranking character of bank i compared to the others with respect to criterion k and the outranking character of the rest of the banks over bank i, respectively.

The overall net <sup>fl</sup>ow index Φ x ranges in $[ - 1 , 1 ] ,$ , with higher values associated with low risk/high performance banks. The partial net <sup>fl</sup>ow index $\phi _ { k } ( { \bf x } _ { i } )$ also ranges in [−1,1] and is interpreted in a similar way.

In order to build the required bank rating model, the evaluation scales for both the overall performance index, as well as for all the partial performance indices are modi<sup>fi</sup>ed in order to enable the de<sup>fi</sup>nition of a 5-point rating scale, in accordance with the existing evaluations procedures of the Bank of Greece. In this model calibration step, the partial net <sup>fl</sup>ows $\phi _ { k } ( { \bf x } _ { i } )$ was used to de<sup>fi</sup>ne a modi<sup>fi</sup>ed partial evaluation function as follows:

$$
v _ {k} (x _ {i k}) = \left\{ \begin{array}{l l} 0. 5 & \text { if } x _ {i k} \geq x _ {k} ^ {*} \\ 0. 5 + 5 \frac {\phi_ {k} (x _ {i k}) - \phi_ {k} (x _ {k} ^ {*})}{\phi_ {k} (x _ {k *}) - \phi_ {k} (x _ {k} ^ {*})} & \text { if } x _ {k *} <   x _ {i k} <   x _ {k} ^ {*} \\ 5. 5 & \text { if } x _ {i k} \leq x _ {k *} \end{array} \right.
$$

where $\boldsymbol { x } _ { k * }$ and $x _ { k } ^ { * }$ are the least and most preferred values of criterion $k ,$ respectively. With this transformation, the partial evaluation of the banks on a criterion k ranges in a scale from 0.5 (best performance)to

5.5 (worst performance). The <sup>fi</sup>nal evaluation model is then reexpressed in an additive form:

$$
V (\mathbf {x} _ {i}) = \sum_ {k = 1} ^ {n} w _ {k} v _ {k} (x _ {i k}) \in [ 0. 5, 5. 5 ]
$$

This model is used to rank the banks in terms of their relative performance. Except for the rating of the banks, this relative ranking was also requested (by the analysts at the Bank of Greece) as an important part of the rating/evaluation process. Given the overall score de<sup>fi</sup>ned in this way, the rating is speci<sup>fi</sup>ed by de<sup>fi</sup>ning the intervals [0.5, 1.5] for risk grade 1, (1.5, 2.5] for risk grade 2, (2.5, 3.5] for risk grade 3, (3.5, 4.5] for risk grade 4, and (4.5, 5.5] for risk grade 5.

## 2.2. Absolute evaluation

The evaluation with the PROMETHEE II method as described above provides a relative evaluation of the banks. This helps in identifying the strengths and weaknesses of a bank compared to its competitors. However, bank rating models should also provide an absolute evaluation that does not depend on the set of banks being evaluated.

The absolute evaluation is also done using the framework of the PROMETHEE method, but in this case the results are based only on the comparison of the banks to a pre-speci<sup>fi</sup>ed reference point. In cooperation with the analysts in the Bank of Greece, two options were de<sup>fi</sup>ned for the speci<sup>fi</sup>cation of the reference point. The <sup>fi</sup>rst implements an optimistic point of view, in the sense that the banks are compared to the ideal point (ideal bank). This kind of evaluation provides an assessment of the capability of the banks to perform as better as possible. The second option uses an anti-ideal point and provides an assessment of the banks compared to a “worst case scenario”. Both the anti-ideal and the ideal point (x and $\mathbf { x } ^ { * } .$ respectively) are de<sup>fi</sup>ned by the analysts of the Bank of Greece, each consisting of the least and most preferred values of each criterion, i.e. $\mathbf { x } _ { * } = ( x _ { 1 * } , x _ { 2 * } , . . . , x _ { n * } )$ and $\mathbf { x } ^ { * } = ( x _ { 1 } ^ { * } , x _ { 2 } ^ { * } , . . . , x _ { n } ^ { * } )$

In the case where the banks are compared to the ideal point, the partial evaluation function is adjusted as follows:

$$
v _ {k} (x _ {i k}) = \left\{ \begin{array}{l l} 5. 5 & \text { if } x _ {i k} \leq x _ {k *} \\ 0. 5 + 5 \frac {\pi_ {k} (x _ {k} ^ {*} , x _ {i k})}{\pi_ {k} (x _ {k} ^ {*} , x _ {k *})} & \text { if } x _ {i k} > x _ {k *} \end{array} \right.
$$

On the other hand, when the anti-ideal point is used, the following partial evaluation function is used:

$$
v _ {k} (x _ {i k}) = \left\{ \begin{array}{l l} 0. 5 + 5 \frac {\pi_ {k} (x _ {k} ^ {*} , x _ {* k}) - \pi_ {k} (x _ {i k} , x _ {* k})}{\pi_ {k} (x _ {k} ^ {*} , x _ {* k})} & \text {if} x _ {i k} <   x _ {k} ^ {*} \\ 0. 5 & \text {if} x _ {i k} \geq x _ {k} ^ {*} \end{array} \right.
$$

## 2.3. Sensitivity analysis

Naturally, the multicriteria evaluations de<sup>fi</sup>ned above incorporate some uncertainty and subjectivity, mainly with regard to the parameters of the PROMETHEE method, which include the criteria weights and the parameters σ and p of the partial preference functions. Furthermore, since banks operate in a dynamic environment, it is also important to identify changes in the input data that may lead to changes in the rating result. This analysis is performed both for the complete set of banks, as well as for each individual bank separately.

In a <sup>fi</sup>rst stage, these issues are addressed by analytic sensitivity procedures. For the criteria weights, the objective of the analysis is to de<sup>fi</sup>ne a range of values for the weight of each criterion k for which the rating of the banks remains unchanged. This can be easily done by imposing the condition that the global score $V ( \mathbf { x } _ { i } )$ of each bank i should remain within the score range associated with its rating, as de<sup>fi</sup>ned with the pre-speci<sup>fi</sup>ed weights. It should be noted that this is a type of “univariate” sensitivity analysis (i.e., each criterion is considered independently of the others). In cooperation of the analysts of the Bank of Greece, it was decided that this speci<sup>fi</sup>cation provided adequate information and it was easy to comprehend. An example of sensitivity analysis considering global changes in the criteria's weights has been presented by Wolters and Mareschal [32].

A similar process is also employed for the parameters of the criteria preference functions. However, with the pairwise relative evaluation scheme of the PROMETHEE method, the partial preference indices are generally non-monotone and non-convex functions of the corresponding parameters σ and p. Thus, in this case it is not possible to de<sup>fi</sup>ne speci<sup>fi</sup>c bounds for these parameters within which the rating of the banks does not change. On the other hand, the bounds can be explicitly de<sup>fi</sup>ned for the absolute evaluation process. In particular, assume a bank i assigned to the rating grade $\ell ,$ de<sup>fi</sup>ned by a range of scores $( \alpha _ { \angle } , \beta _ { \angle } ]$ , and suppose that a range $[ l _ { k } , u _ { k } ]$ should be de<sup>fi</sup>ned for the parameters of the preference function of a criterion k, such that the rating grade of the bank does not change, i.e. $\alpha _ { \ell } < V ( \mathbf { x } _ { i } ) \le \beta _ { \ell }$ . Then:

$$
V \left(\mathbf {x} _ {i}\right) > \alpha_ {\ell} \Longleftrightarrow v _ {k} \left(x _ {i k}\right) > \max \left\{0. 5, \frac {\alpha_ {\ell} - \sum_ {j \neq k} w _ {j} v _ {j} \left(x _ {i j}\right)}{w _ {k}} \right\}\tag{1}
$$

For illustrative purposes, it can be assumed that: (1) the Gaussian preference function is used, (2) the absolute evaluation is performed in comparison to the ideal point, and $( 3 ) \ x _ { k * } < x _ { i k } < x _ { k } ^ { * } .$ . Then, taking into account that $\nu _ { k } \big ( x _ { i k } \big )$ decreases with the preference parameter, and denoting by $z _ { i k }$ the left-hand side of 1, the upper bound u<sub>k</sub> is de<sup>fi</sup>ned as follows:

⇒

$$
\begin{array}{c} 0. 5 + 5 \frac {\pi_ {k} (x _ {k} ^ {*} , x _ {i k})}{\pi_ {k} (x _ {k} ^ {*} , x _ {k *})} > z _ {i k} \\ \pi_ {k} (x _ {k} ^ {*}, x _ {i k}) > \frac {(z _ {i k} - 0 . 5) \pi_ {k} (x _ {k} ^ {*} , x _ {k *})}{5} \\ 1 - \exp \left[ - \frac {(x _ {k} ^ {*} - x _ {i k}) ^ {2}}{2 u _ {k} ^ {2}} \right] > \frac {(z _ {i k} - 0 . 5) \pi_ {k} (x _ {k} ^ {*} , x _ {k *})}{5} \\ u _ {k} <   \sqrt {\frac {- (x _ {k} ^ {*} - x _ {i k}) ^ {2}}{2 \ln [ 1 - 0 . 2 (z _ {i k} - 0 . 5) \pi_ {k} (x _ {k} ^ {*} , x _ {k *}) ]}} \end{array}\tag{⇒}
$$

⇒

Note that if $z _ { i k } { > } 0 . 5 + 5 / \pi _ { k } ( x _ { k } ^ { * } , x _ { k * } )$ , then $u _ { k } = + \infty ,$ . The same process is used to de<sup>fi</sup>ne the lower bound $l _ { k } \mathrm { : }$

$$
\begin{array}{c} V (\mathbf {x} _ {i}) \leq \beta_ {\ell} \Longleftrightarrow v _ {k} (x _ {i k}) \leq \min \bigg \{5. 5, \frac {\beta_ {\ell} - \sum_ {j \neq k} w _ {j} v _ {j} (x _ {i j})}{w _ {k}} \bigg \} = o _ {i k} \\ 1 - e x p \left[ - \frac {(x _ {k} ^ {*} - x _ {i k}) ^ {2}}{2 l _ {k} ^ {2}} \right] \leq \frac {(o _ {i k} - 0 . 5) \pi_ {k} (x _ {k} ^ {*} , x _ {k *})}{5} \\ l _ {k} \geq \sqrt {\frac {- (x _ {k} ^ {*} - x _ {i k}) ^ {2}}{2 l n [ 1 - 0 . 2 (o _ {i k} - 0 . 5) \pi_ {k} (x _ {k} ^ {*} , x _ {k *}) ]}} \end{array}\tag{→}
$$

⇒

with $l _ { k } = 0$ whenever $o _ { i k } { < } 0 . 5 .$

A similar procedure can also be applied with the linear preference function and the comparison to the anti-ideal point.

In addition to the speci<sup>fi</sup>cation of bounds for the parameters of the preference functions, additional information can be obtained by observing the general impact of the preference parameters to the overall evaluation of the banks (as a whole and individually). This is done with the calculation of a sensitivity index $\varDelta _ { k } ,$ which measures the mean maximum percentage change in the global evaluation of the banks due to a change in the preference parameter of criterion k. In particular, let $\nu _ { k } ( x _ { i k } , a _ { k } )$ denote the partial performance of bank i on criterion k, expressed as a function of x<sub>ik</sub> and the criterion's preference parameter $a _ { k } .$ Then, two optimization problems are solved to <sup>fi</sup>nd the parameter value $a _ { * i k } \left( a _ { i k } ^ { * } \right)$ that minimize (maximize), the partial performance of bank i on criterion $k ,$ i.e.:

$$
v _ {k} ^ {\min} (x _ {i k}, a _ {* i k}) = \min _ {a _ {i k} > 0} v _ {k} (x _ {i k}, a _ {i k}) \quad \text { and } \quad v _ {k} ^ {\max} (x _ {i k}, a _ {i k} ^ {*}) = \max _ {a _ {i k} > 0} v _ {k} (x _ {i k}, a _ {i k})
$$

Then, the sensitivity index $\delta _ { i k }$ measuring the impact of criterion's k preference parameter on the global performance of bank i is de<sup>fi</sup>ned as follows:

$$
\delta_ {i k} = \max \left\{w _ {k} \frac {v _ {k} ^ {\max} (x _ {i k} , a _ {i k} ^ {*}) - v _ {k} (x _ {i k})}{V (\mathbf {x} _ {i})}, w _ {k} \frac {v _ {k} (x _ {i k}) - v _ {k} ^ {\min} (x _ {i k} , a _ {* i k})}{V (\mathbf {x} _ {i})} \right\}\tag{2}
$$

where $V ( \mathbf { x } _ { i } )$ is the global performance of the bank obtained with criterion's k preference parameter de<sup>fi</sup>ned by the decision-maker and $\nu _ { k } \big ( x _ { i k } \big )$ the corresponding partial score. For instance, a sensitivity index $\delta _ { i k } = 0 . 3$ indicates that a change in the preference parameter of criterion k, may lead to a change of up to 30% in the global performance of bank i. The direction of the change (decrease or increase) can be easily found by identifying which of the two arguments provides the maximum in (2).

The sensitivity index $\varDelta _ { k }$ is then calculated as:

$$
\Delta_ {k} = \frac {1}{m} \sum_ {i = 1} ^ {m} \delta_ {i k}
$$

In the case of absolute evaluation $\nu _ { k } ^ { \mathrm { m i n } } ( x _ { i k } , a _ { * i k } )$ and $\nu _ { k } ^ { \mathrm { m a x } } ( x _ { i k } , a _ { i k } ^ { * } )$ are easy to <sup>fi</sup>nd because $\nu _ { k } ( x _ { i k } , a _ { k } )$ is a monotone function of $a _ { k } ,$ and the extremes are found by imposing a range of reasonable values for $a _ { k }$ (e.g., between 0.001 and 100). On the other hand, in the relative evaluation process, $\nu _ { k } ( x _ { i k } , a _ { k } )$ is generally a non-convex function of $a _ { k } .$ In this case, a simple genetic algorithm is employed in order to <sup>fi</sup>nd $\nu _ { k } ^ { \mathrm { m i n } } ( x _ { i k } , a _ { * i k } )$ and $\nu _ { k } ^ { \mathrm { m a x } } ( x _ { i k } , a _ { i k } ^ { * } )$

The analytic procedures described in the previous section, provide useful local information about the sensitivity of the rating results. Further information is obtained with Monte Carlo simulation. In the proposed methodology, simulation is used to analyze the sensitivity of the ratings with respect to changes in the weights of the criteria, but the process can be easily extended to consider the parameters of the preference functions, too.

## 2.4. Monte Carlo simulation

The simulation involves the generation of multiple scenarios regarding the weights of the criteria. Two options can be considered for the generation of the weights. In the <sup>fi</sup>rst case, the weights are generated at random over the unit simplex [5,28]. Alternatively, the decision maker can provide a ranking of the criteria according to their relative importance, and then random weights are generated, which are in accordance with the ordering of the criteria.

The results of the simulation are analyzed in terms of the mean and median of the global performance scores, their standard deviation and con<sup>fi</sup>dence intervals. Furthermore, for each individual bank useful conclusions can be drawn on the distribution of its rating under different weighting scenarios.

## 3. Implementation into a decision support system

The proposed multicriteria methodology has been implemented in an integrated decision support system (DSS). The system enables multiple users (senior or junior level analysts) to work simultaneously on a common shared database. Senior bank analysts are responsible for setting the main parameters of the evaluation process, namely the criteria weights, the type of the corresponding preference functions, and the associated parameters. Senior analysts can also modify the set of the evaluation criteria, by adding or deleting criteria. Lower level analysts have full access to all features of the multicriteria evaluation process, but they are not allowed to perform permanent changes in the evaluation parameters.

Sample list of evaluation criteria.

<table><tr><td>Categories</td><td>Abbr.</td><td>Criteria</td></tr><tr><td rowspan="2">Capital</td><td>Cap1</td><td>Capital adequacy ratio</td></tr><tr><td>Cap2</td><td>TIER II capital/TIER I</td></tr><tr><td rowspan="4">Assets</td><td>Ass1</td><td>Risk-weighted assets / Assets</td></tr><tr><td>Ass2</td><td>(Non performing loans – Provisions)/Loans</td></tr><tr><td>Ass3</td><td>Large exposures/(TIER I + TIER II capital)</td></tr><tr><td>Ass4</td><td>(Non performing loans/2 – Provisions)/Equity</td></tr><tr><td rowspan="12">Management</td><td>Man1</td><td>Operating expenses/Operating income</td></tr><tr><td>Man2</td><td>Staff cost/Assets</td></tr><tr><td>Man3</td><td>Operating income/Business units</td></tr><tr><td>Man4</td><td>Top management competencies, qualifications and continuity</td></tr><tr><td>Man5</td><td>Managers&#x27; experience and competence</td></tr><tr><td>Man6</td><td>Resilience to change, strategy, long term horizon</td></tr><tr><td>Man7</td><td>Management of information systems</td></tr><tr><td>Man8</td><td>Internal control systems</td></tr><tr><td>Man9</td><td>Financial risk management system</td></tr><tr><td>Man10</td><td>Internal processes charter - implementation monitoring</td></tr><tr><td>Man11</td><td>Timely and accurate data collection</td></tr><tr><td>Man12</td><td>Information technology systems</td></tr><tr><td rowspan="4">Earnings</td><td>Ear1</td><td>Net income/Assets</td></tr><tr><td>Ear2</td><td>Net income/Equity</td></tr><tr><td>Ear3</td><td>Interest revenue/Assets</td></tr><tr><td>Ear4</td><td>Other operating revenue/Assets</td></tr><tr><td rowspan="3">Liquidity</td><td>Liq1</td><td>Cash/Assets</td></tr><tr><td>Liq2</td><td>(Loans – Provisions)/Deposits</td></tr><tr><td>Liq3</td><td>Real funding from credit institutions/Assets</td></tr><tr><td>Market</td><td>Mar1</td><td>Risk – weighted assets II/Risk-weighted Assets (I and II)</td></tr></table>

Except for database management and the use of the multicriteria tools, the DSS includes a user-friendly interface that facilitates the preparation of several reports in graphical and tabular format.

The following subsections illustrate the capabilities that the DSS provides and the way that the proposed multicriteria methodology has been implemented into the system. It should be noted that, for con<sup>fi</sup>dentiality reasons, all the results presented in this illustration are only indicative and they not related in any way to the actual data of the banks.

## 3.1. Evaluation data, criteria, and preference parameters

The data considered in the system involve historical information on a number of evaluation criteria for Greek banks. The system enables the use of different databases, depending on the type of banks analyzed. The subsequent discussion involves commercial and investment banks, but the methodology and the tools implemented in the DSS can also be used to evaluate, for instance, cooperative banks (which are can be included in a separate database, considering different evaluation criteria).

Initially, a set of 31 evaluation criteria have been introduced in the system.<sup>1</sup> A sample list of the evaluation criteria is given in (Table 1). These criteria have been selected in close co-operation with the expert analysts of the Bank of Greece, who are responsible for monitoring and evaluating the performance of the banks. The criteria are organized into 6 categories (capital, assets, management, earnings, liquidity, sensitivity to market risks), in accordance with the CAMELS framework. Overall, 17 quantitative and 14 qualitative criteria have been initially selected. All qualitative criteria are evaluated on an interval [0.5,5.5] scale, de<sup>fi</sup>ned by the analysts of the Bank of Greece, with lower values indicating better performance.

![](/api/attachments/28P4TS23/fulltext/images/f0ca5f0109a68e0865e97a1f8e1f0a46d675493b3c5889237f86b99935700853.jpg)  
Fig. 2. De<sup>fi</sup>nition of the criteria's weights and their ROC and RS approximations.

The weights of each category of criteria and the criteria therein have been de<sup>fi</sup>ned by the expert analysts of the Bank of Greece. The system also includes some additional modules that support the analysts on the speci<sup>fi</sup>cation of the criteria weights, using the rank-order centroid (ROC) and rank-rum (RS) approaches [15], as well as multivariate statistical analysis techniques such as principal components analysis. Fig. 2 presents a screenshot of the system illustrating the speci<sup>fi</sup>cation of the criteria's weights. The ROC and RS approximations are calculated on the basis of the rank-ordering of the criteria according to the weights speci<sup>fi</sup>ed by the analyst. As shown in Fig. 2 the RS estimates are very close to the userde<sup>fi</sup>ned relative importance of each criteria group. The same was also observed at the individual criteria level. Overall, the quantitative criteria have been assigned a weight of 70%, with the remaining 30% involving qualitative criteria. This is based on a policy speci<sup>fi</sup>cation by the expert analysts of the Bank of Greece, according to which “hard data” should be given higher importance than subjective evaluations which are involved in the de<sup>fi</sup>nition of the qualitative criteria.

All the quantitative criteria are evaluated using the Gaussian preference function in the PROMETHEE method, whereas a linear preference function is used for the qualitative criteria. Fig. 3 illustrates the partial performance function for the capital adequacy ratio. The function decreases with the values of the criterion, thus indicating that higher capital adequacy values are associated with higher performance and lower risk. Through the table at the right part of the screen, the user-analyst can specify the least and most preferred values (ideal, anti-ideal), the type of the function, and the associated parameter. The graph at the left part of the screen is automatically updated taking into account any change that the user makes, in order to illustrate how the speci<sup>fi</sup>ed settings affect the scores of the banks in the database on the evaluation criterion under consideration. The user-analyst can also introduce a benchmark point (e.g., an average or typical performance), which may facilitate the analysis of the results.

![](/api/attachments/28P4TS23/fulltext/images/04c7f3777142f30d40d91d11d91588df14ba494f877ca87ce7cba042bb91951d.jpg)  
Fig. 4. Evaluation options.

![](/api/attachments/28P4TS23/fulltext/images/edbfc3858584763631f9b4d9d21940ebde57ca86e8110975b49c92c57c13d6c8.jpg)  
Fig. 3. User inputs for the partial preference functions (generalized criteria)

## 3.2. Multicriteria evaluation

On the basis of the methodology described in Section 2, the system provides a variety of options to the user-bank analyst (Fig. 4), involving: (1) the banks, evaluation criteria, and time period of the analysis,(2) the type of the evaluation (absolute, relative), (3) the speci<sup>fi</sup>cation of the criteria's weights, and (4) the use of scenario analysis through Monte Carlo simulation (the functionality of this option is illustrated in Section 3.3).

The overall evaluation results of the PROMETHEE II method are presented through the screen of Fig. 5a. The overall evaluation scores are reported for each year and each bank. Interactive sensitivity analysis is available. The user can modify the weight and/or the parameter of the preference function for a selected criterion and the evaluation results are updated automatically, thus illustrating in “realtime” the impact of the changes on the estimated performance and rating of the banks, with the upgrades and downgrades marked in different colors as illustrated in Fig. 5b.

(a)  
![](/api/attachments/28P4TS23/fulltext/images/eeaadf5cb93c19ac977f0a43267a5101e57d12f3a93271ebf3ca4cda40af572a.jpg)

(b)  
![](/api/attachments/28P4TS23/fulltext/images/8d8c936c865f58bbc3c1c96d9bd0c926698cee66ef77dea915ddbb66ff18e77f.jpg)  
Fig. 5. Presentation of the overall evaluation results.

Analytic sensitivity results are also available in separate sheets, with regard to the weights of the criteria and the parameters of the corresponding preference function. Fig. 6 illustrates an example for the weights of the criteria. For each criterion, the range for its weights is shown (lower and upper bound), within which the ratings of the banks are not changed. The “stability index”, which is shown at the last column of the table, represents the minimum percentage change of the weight of each criterion, which alters the ratings (different colors are used to distinguish between decreases and increases).

The system also provides detailed reporting tools at the individual bank level, through the screen of Fig. 7. This type of report provides details on how the overall evaluation of a selected bank is decomposed into each criterion and group of criteria. Sensitivity analysis results for the rating of the selected bank are also available with regard to the weights of the criteria, the parameters of the criteria's preference functions, and the input data.

## 3.3. Scenario analysis

Further results on the sensitivity of the ratings to the weighting of the criteria are obtained with scenario analysis, which is performed through Monte Carlo simulation. The user-bank analyst can specify the number of different weighting scenarios in this analysis. The results involve statistics on the global performance score of the banks (mean, median 95% con<sup>fi</sup>dence interval) as shown in Fig. 8, as well as the distribution of the ratings for each bank.

Insights into the details of the evaluation of a selected bank can be obtained through the report illustrated in Fig. 9. This report provides information about the distribution of the bank's ratings (in tabular and graphical form), and its evaluation scores (through the Box plot at the top right part of the screen). Furthermore, results are given on the relationship between the weights of the criteria and the obtained ratings over all the simulation runs, through the table at the bottom right part. In particular, the correlation coef<sup>fi</sup>cient given for each criterion indicate the strength of the connection between the rating of the bank and the relative importance of the criteria. Criteria with negative correlations can be considered as strong points for the bank, in the sense that the higher the weight of these criteria, the lower (better) is the bank's evaluation score. As an additional information, for each criterion its average weight is calculated over all scenarios in which the bank is rated in a speci<sup>fi</sup>c grade. In particular, assuming weight vectors $\mathbf { w } _ { 1 } , \mathbf { w } _ { 2 } , . . . ,$ each corresponding to one simulation run, and denoting by $\boldsymbol { S } _ { i k }$ the set of simulation runs in which bank i is assigned to grade k (with $\left| \mathcal { S } _ { i k } \right|$ denoting the number of these runs), then

![](/api/attachments/28P4TS23/fulltext/images/3fd78bbb25bda6bf19970e6fe582856a1c26c3e5cd885ce5e82aefd174e367b8.jpg)  
Fig. 6. Sensitivity analysis results for the weights of the criteria.

![](/api/attachments/28P4TS23/fulltext/images/b301c1793825125956f62c8f9513320e30fe554ae0cf915f9879c7269b3717d5.jpg)  
Fig. 7. Individual bank report.

$$
\widehat {\mathbf {w}} _ {i k} = \frac {1}{| \mathcal {S} _ {i k} |} \sum_ {\ell \in \mathcal {S} _ {i k}} \mathbf {w} _ {\ell}
$$

![](/api/attachments/28P4TS23/fulltext/images/e9819f41575d9d823a8a5f0163be2361ed633a4dd70d87f0c4eac7ac51bfea44.jpg)  
Fig. 8. Weight scenario results.

is the average weight vector over all scenarios in $\begin{array} { r } { S _ { i k } , } \end{array}$ , which provides useful information for a kind of “reverse” analysis of the evaluation results (rating) for a selected bank. For instance, the illustration in Fig. 9 shows, that under the scenarios in which the selected bank is assigned into risk grade 2 in year 2001, the weights of criteria Cap1 and Cap2, for example, are higher compared to the weights of these criteria under the scenarios in which the bank is assigned to risk grade 3.

## 4. Conclusions

Bank performance monitoring and evaluation is gaining increasing interest within the context of the recent <sup>fi</sup>nancial crisis. This paper presented a multicriteria methodology aiming towards providing comprehensive support to expert analysts. Special emphasis is put on the sensitivity of the results to the main evaluation parameters, which enables the derivation of useful conclusions on the strengths and weakness of the banks.

The methodology has been implemented in a integrated DSS, which is currently in use at the Bank of Greece. The DSS provides the users-analysts with enhanced database management capabilities (including the modi<sup>fi</sup>cation of evaluation criteria), several analysis options and reporting tools.

The multicriteria methodology and the DSS can be used by expert bank analysts as supportive tools in their daily practice for monitoring and evaluating the performance of banks. At a further step, the aim would be to develop an early-warning system capable of identifying (as early as possible) banks which are likely to face problems. The consideration of macroeconomic factors would also enhance the analysis and enable the implementation of stress testing scenarios regarding the impact of external factors on the performance and viability of the banks. The consideration of data from other banking sectors from developed and developing economies, could also enhance the analysis providing useful information on the risks of a county's banking sector in connection of the risks in other related markets.

![](/api/attachments/28P4TS23/fulltext/images/e902fcaec2d1bf4b71c76db953a80abf5d386025b2a0719aba6a239b220129a7.jpg)  
Ratings' distribution

Criteria's weights  
Boxplot graph  
![](/api/attachments/28P4TS23/fulltext/images/70a2fd58fed8178868a9d61576781659f7014bc234a2ec4d20ffc5e7322a2ebd.jpg)

![](/api/attachments/28P4TS23/fulltext/images/288978b22d823af8312cf137f9fdab048739ed217fd684b544c6d6a1630f3b26.jpg)

<table><tr><td colspan="2">Years</td><td>Cap1</td><td>Cap2</td><td>Cap3</td><td>Ass1</td><td>Ass2</td><td>Ass3</td><td>Ass4</td></tr><tr><td rowspan="6">2001</td><td>Corr. with rating</td><td>-51.3</td><td>-31.1</td><td>23.5</td><td>11.4</td><td>24.8</td><td>-42.2</td><td>25.0</td></tr><tr><td>Mean rating 1</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Mean rating 2</td><td>18.6</td><td>8.5</td><td>5.9</td><td>1.2</td><td>4.3</td><td>5.8</td><td>4.1</td></tr><tr><td>Mean rating 3</td><td>14.1</td><td>6.2</td><td>7.6</td><td>1.6</td><td>5.0</td><td>4.5</td><td>4.8</td></tr><tr><td>Mean rating 4</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Mean rating 5</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td rowspan="4">2002</td><td>Corr. with rating</td><td>53.9</td><td>20.5</td><td>-12.1</td><td>-3.4</td><td>36.5</td><td>-28.5</td><td>43.2</td></tr><tr><td>Mean rating 1</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Mean rating 2</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Mean rating 3</td><td>13.2</td><td>6.1</td><td>7.5</td><td>1.4</td><td>4.2</td><td>5.3</td><td>3.9</td></tr></table>

Fig. 9. Weights scenario report for a selected bank.

## References

[1] S. Alter, A work system view of DSS in its fourth decade, Decision Support Systems 38 (2004) 319–327.

[2] C. Barros, C. Ferreira, J. Williams, Analysing the determinants of performance of best and worst European banks: a mixed logit approach, Journal of Banking and Finance 31 (2007) 2189–2203.

[3] M. Beynon, Optimizing object classi<sup>fi</sup>cation under ambiguity/ignorance: application to the credit rating problem, Intelligent Systems in Accounting, Finance & Management 13 (2005) 113–130.

[4] J. Brans, P. Vincke, A preference ranking organization method, Management Science 31 (1985) 647–656.

[5] J. Butler, J. Jia, J. Dyer, Simulation techniques for the sensitivity analysis of multi-criteria decision models, European Journal of Operational Research 103 (1997) 531–546.

[6] M. Dempster, M. Ireland, Object-oriented model integration in a <sup>fi</sup>nancial decision support system, Decision Support Systems 7 (1991) 329–340.

[7] A. Derviz, J. Podpiera, Predicting bank CAMELS and S&P ratings: the case of the Czech Republic, Emerging Markets Finance and Trade 44 (2008) 117–130

[8] D. Fethi, F. Pasiouras, Assessing bank ef<sup>fi</sup>ciency and performance with operational research and arti<sup>fi</sup>cial intelligent techniques: a survey, European Journal of Operational Research 204 (2010) 189–198.

[9] F. García, F. Guijarro, I. Moya, Ranking Spanish savings banks: A multicriteria approach, Mathematical and Computer Modelling 52 (2010) 1058–1065.

[10] G. Gregoriou, E. Lusk, M. Halperin, A two-staged benchmarked decision support system using DEA pro<sup>fi</sup>les of ef<sup>fi</sup>ciency, INFOR 46 (2008) 177–187.

[11] B. Grif<sup>fi</sup>ths, M. Beynon, Expositing stages of VPRS analysis in an expert system: application with bank credit ratings, Expert Systems with Applications 29 (2005) 879–888.

[12] G. Halkos, D. Salamouris, Ef<sup>fi</sup>ciency measurement of Greek commercial banks with the use of <sup>fi</sup>nancial ratios: a data envelopment analysis approach, Management Account Research 15 (2004) 201–224.

[13] C.T. Ho, Measuring bank operations performance: an approach based on grey relation analysis, Journal of the Operational Research Society 57 (2006) 337–349

[14] Z. Huang, H. Chen, C.J. Hsu, W.H. Chen, S. Wu, Credit rating analysis with support vector machines and neural networks: a market comparative study, Decision Support Systems 37 (2004) 543–558.

[15] J. Jia, G. Fischer, J. Dyer, Attribute weighting methods and decision quality in the presence of response error: a simulation study, Journal of Behavioral Decision Making 11 (1981) 85–105.

[16] S. Kanungo, S. Sharma, P. Jain, Evaluation of a decision support system for credit management decisions, Decision Support Systems 30 (2001) 419–436.

[17] C. Kao, S.T. Liu, Predicting bank performance with <sup>fi</sup>nancial forecasts: a case of Taiwan commercial banks, Journal of Banking and Finance 28 (2004) 2353–2368.

[18] K. Kosmidou, C. Zopounidis, Measurement of bank performance in Greece, South-Eastern Europe Journal of Economics 6 (2008) 79–95.

[19] S. Kumar, A. Arora, A model for risk classi<sup>fi</sup>cation of banks, Managerial and Decision Economics 16 (2006) 155–165.

[20] S.W. Lin, Y.R. Shiue, S.C. Chen, H.M. Cheng, Applying enhanced data mining approaches in predicting bank performance: a case of Taiwanese commercial banks, Expert Systems with Applications 36 (2009) 11543–11551.

[21] B. Mareschal, J. Brans, BANKADVISER: an industrial evaluation system, European Journal of Operational Research 54 (1991) 318–324.

[22] B. Mareschal, D. Mertens, BANKS: a multicriteria decision support system for <sup>fi</sup>nancial evaluation in the international banking sector, Journal of Decision Systems.1.(1992).175-189.

[23] D. Min, J. Kim, W. Kim, D. Min, S. Ku, IBRS: intelligent bank reengineering system, Decision Support Systems 18 (1996) 97–105.

[24] G. Moynihan, P. Purushothaman, R. McLeod, W. Nichols, DSSALM: a decision support system for asset and liability management, Decision Support Systems 33 (2002) 23–38.

[25] C. Parkan, M.L. Liu, Measurement of the performance of an investment bank using the operational competitiveness rating procedure, Omega 27 (1999) 201–217.

[26] A. Raveh, The Greek banking system: reanalysis of performance, European Journal of Operational Research 120 (2000) 525–534.

[27] V. Ravi, H. Kurniawan, P. Nwee Kok Thaia, P. Ravi Kumar, Soft computing system for bank performance prediction, Applied Soft Computing 8 (2008) 305–315.

[28] R. Rubinstein, Generating random vectors uniformly distributed inside and on the surface of different regions, European Journal of Operational Research 10 (1982) 205-209.

[29] R. Sahajwala, P. Van den Bergh, Supervisory Risk Assessment and Early Warning Systems, Technical Report 4, Bank of International Settlements, Basel, Switzerland, 2000.

[30] C. Spathis, K. Kosmidou, M. Doumpos, Assessing pro<sup>fi</sup>tability factors in the Greek banking system: a multicriteria approach, International Transactions in Operational Research 9 (2002) 517–530.

[31] N. Thoraneenitiyan, N. Avkiran, Measuring the impact of restructuring and country-speci<sup>fi</sup>c factors on the ef<sup>fi</sup>ciency of post-crisis East Asian banking systems: integrating DEA with SFA, Socio-Economic Planning Sciences 43 (2009) 240–252

[32] W. Wolters, B. Mareschal, Novel types of sensitivity analysis for additive MCDM methods, European Journal of Operational Research 81 (1995) 281–290.

[33] C. Zopounidis, D. Despotis, E. Stavropoulou, Multiattribute evaluation of Greek banking performance, Applied Stochastic Models and Data Analysis 11 (1995) 97–107.

![](/api/attachments/28P4TS23/fulltext/images/7639df736f08b935d46b914f02b866a0ad7481ec317952e948105cce69a79563.jpg)  
Michael Doumpos is Assistant Professor at the Dept. of Production Engineering and Management of the Technical University of Crete. His research interests include multiple criteria decision making, non-parametric classi<sup>fi</sup>cation and regression methods, and <sup>fi</sup>nancial management. He has published over 40 research articles in premier international journals such as Decision Sciences, European Journal of Operational Research, Computational Optimization and Applications, IEEE Transactions on Systems, Man and Cybernetics Expert Systems with Applications Annals of Operations Research, The Journal of the Operational Research Society, Computers and Operations Research, Omega.

![](/api/attachments/28P4TS23/fulltext/images/6604c95b9fd465f61d7476195795794f7e8c61dc2206f0be057f2162af391620.jpg)

Constantin Zopounidis is Professor of <sup>fi</sup>nancial management and operations research at the Dept. of Production Engineering and Management, Technical University of Crete, Greece. His research interests include multiple criteria decision making, <sup>fi</sup>nancial engineering and <sup>fi</sup>nancial risk management. He has published over 300 papers in premier international journals as Decision Sciences, European Journal of Operational Research, Decision Support Systems, Journal of the Operational Research Society, and Expert Systems with Applications. He has edited or co-edited more than 35 books on <sup>fi</sup>nancial management and multicriteria decision aid, and he acts as the Editor-in-Chief and member of the editorial board for several international journals.

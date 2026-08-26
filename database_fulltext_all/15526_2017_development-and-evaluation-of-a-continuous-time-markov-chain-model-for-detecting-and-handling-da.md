---
otero_id: 15526
otero_key: "9HKZFYPV"
title: "Development and evaluation of a continuous-time Markov chain model for detecting and handling data currency declines"
authors: "Yuval Zak; Adir Even"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.09.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Development and evaluation of a continuous-time Markov chain model for detecting and handling data currency declines

Yuval Zak, Adir Even ⁎

The Department of Industrial Engineering and Management, Ben-Gurion University of the Negev, P.O.B. 653, Beer-Sheva 8410501, Israe

## a r t i c l e i n f o

Article history: Received 14 July 2016 Received in revised form 9 September 2017 Accepted 20 September 2017 Available online xxxx

Keywords: Data quality management Data currency Continuous-time Markov chain

## a b s t r a c t

Data currency declines, caused by recorded data values becoming outdated, can damage the usability and accountability of data resources. Detecting and updating outdated values may improve data currency and reduce the associated damage, but such efforts may be costly and cannot always be justified. This study models currency decline scenarios using a continuous-time Markov chain stochastic process with a finite number of states, each reflecting a valid data value. The model considers state transition probabilities, transition time distributions, and the tradeoff between the damage associated with outdated data and the cost of reacquisition. The proposed formulation permits the currency level to be estimated without having to rely on a baseline for comparison, as well as the prediction of future currency declines, assessment of their accumulated damage, and optimization of the timing of cost-effective data auditing and reacquisition. The study introduces a comprehensive evaluation of the proposed model, using a large real-world dataset relating to the handling of insurance claims over multiple time periods. The evaluation results highlight the applicability of the model, and its potential contribution to proactive data quality management and cost-effective handling of currency declines.

© 2017 Elsevier B.V. All rights reserved.

## 1. Introduction

In the context of Data Quality (DQ) management, currency reflects the degree to which data values are recent and up to date, considering the time-lag since their acquisition. Currency declines, and their hazardous impact on data accountability and usability, have long captured the attention of DQ management research and practice. Detecting and correcting discrepancies between previously acquired data and the correct real-world state often requires a baseline for comparison, e.g., the actual real-world state, if known, or another reliable data source. Obtaining such a correct baseline, if possible at all, may involve major efforts and costs, often beyond the organization's resource constraints and budget limitations.

Motivated by that challenge, the aim of this study is to develop a continuous-time Markov chain (CTMC) model that reflects a common mechanism behind currency declines: a failure to detect real-world state transitions and update the data accordingly, due to the high costs of doing so. The model targets data acquisition scenarios in which a real-world entity may reside in one of a finite number of states, each described by a set of data-attribute values. With some necessary adaptations, the proposed model treats state transitions as a stochastic process that has some typical CTMC characteristics. An assessment of whether a certain data record must be revisited, and possibly reacquired, considers state-transition probabilities, transition-time distributions, and tradeoffs between the damage associated with outdated data and the cost of data reacquisition.

The solutions derived from the proposed model support some key DQ-management tasks, which can be associated with the broadlyaccepted Total Data Quality Management (TDQM) framework [1]. TDQM promotes proactive DQ management: rather than a one-time data correction effort, DQ improvement should be managed as an ongoing cycle of definition, measurement, analysis and improvement stages. Through in-depth understanding of root causes behind DQ defects, DQ management must aim at predicting their future formation, taking preventive measures, and optimizing DQ improvement policies accordingly. While adhering to TDQM principles and stage definitions, this study makes a few contributions to that end:

a) Definition: Currency is often defined in a reactive manner – To what extent is the data under evaluation still up-to-date, considering the time-lag since data acquisition? Adopting and extending the approach taken in some previous work, this study defines currency in probabilistic, rather than deterministic, terms. Further, it argues that proactive DQ management should redirect the scope of assessment, asking instead, What is the likelihood that the data under evaluation will remain up-to-date in the future?

b) Measurement: Currency, similar to other DQ metrics, is often measured as a [0,1] ratio of non-defective data values. Using the proposed CTMC model, the likelihood of currency decline is formulated as a function of the time-gap since data acquisition. The proposed formulation permits convenient currency estimation, without necessarily having to rely on a baseline for comparison.

c) Analysis: Considering a newly acquired value, the proposed formulation estimates the likelihood that, at a certain later point in time, this value will still reflect the correct real-world state. Given that prediction, the model determines the expected time until data will become outdated, due to possible real-world state transitions.

d) Improvement: Beyond prediction, the model also links time-lag effects and currency declines to potential benefits and costs. Thus, the model can guide cost-effective data reacquisition policies, prescribe DQ improvement actions, and recommend optimal timings for them.

To ascertain the feasibility and validity of the proposed model, the study evaluated it using a large-scale real-world dataset relating to claim-handling for insurants who suffered work-related injuries. An optimal claim-handling process requires strict maintenance of correct insurant data at all times; hence, the issue of data currency can be associated with substantial cost–benefit tradeoffs. Ensuring the currency of this dataset may turn out to be expensive and time-consuming, as claim-handling representatives must often call insurants or even meet them in person to verify their data. Given their inherent time and workload constraints, representatives must often prioritize their contact efforts and, as stated by their managers, their heuristics-based prioritization practices are far from being optimal. The costs associated with contacting an insurant are often wasteful, if no updates to the data are required. On the other hand, failures to record and reflect real-world transitions in insurants' states often lead to major revenue losses. Evaluation of this business scenario and the associated datasets shows that the proposed model can help to optimize the timing of a call to an insurant, thereby making substantial cost savings.

The next section sets out the background for the model development, and underscores its contribution alongside previous work that has addressed the challenges associated with currency declines from different perspectives. This is followed by the development of the proposed model and its evaluation within real-world settings. Finally, the concluding section summarizes the study, states its key contributions, highlights its limitations, and proposes possible directions for future research.

## 2. Background

A plethora of DQ studies have explored currency decline from different perspectives, which can be associated with the different stages of the TDQM framework, namely definition, measurement, analysis and improvement. Similarly to this study, some have applied Markov chain modeling techniques to understand the root causes behind currency declines and assess their impact. This section reviews their influences on the concepts and tools used by this study, and highlights its added contribution.

## 2.1. Currency definition and measurement

Currency is often discussed within the broader terminology of DQ dimensions, which reflect the differences between various forms of DQ defects and their implications for DQ management [2]. The Currency dimension (also termed Timeliness, Recency or Freshness in some DQ work) reflects the potential impact of time-lags between real-world transitions, data acquisition, and/or data usage [3,4]. A growing timelag increases the chance of currency decline, i.e., a greater likelihood that a data value no longer reflects the real-world state correctly [5,6]. The lower the currency of data resources, the lesser is their usefulness and relevance for organizations and decision-makers ([6,7,8,17]).

Heinrich and Klier [4] point out the need to differentiate between Currency and Accuracy, as the definitions of those two dimensions tend to be inconsistent across DQ research. While the former reflects temporal decline effects, the latter refers to discrepancies between the data-in-hand and the correct real-world state, not necessarily associated with temporal effects. This study adopts Heinrich and Klier's [4] view of currency, as a DQ dimension that expresses whether or not an attribute value, which has been previously acquired correctly, still reflects the corresponding real-world value correctly at the time of evaluation. Notably, currency might decline even if data has been acquired accurately, e.g., due to a failure to reflect real-world transitions correctly by updating and/or reacquiring existing data [8,9], or due to unexpected latencies in data integration processes [10].

DQ measurement scores, reflecting levels of currency and other DQ dimensions, are used for assessing DQ state and informing IT personnel and end-users accordingly [2,11,12]. In conformance with common approaches for defining DQ metrics, a currency metric can be defined as the [0,1] ratio between the number of data items that still reflect the real-world state correctly and the total number of values [2]. The use of such metrics mandates the verification of data values against a reliable baseline, e.g., the actual real-world state, if can be obtained, or another data source that has been validated to be correct. Obtaining a reliable baseline and evaluating data against it might involve major efforts and costs (e.g., [7,13,17]). Rather than relying on a baseline, some studies (e.g., [3,5]) have derived currency-decline proxies, using timelags measured from database logs or record-level timestamps. However, such proxies fail to capture the inherent uncertainty and complexity of currency decline patterns, and hence might bias currency assessment substantially [6].

Acknowledging those limitations, other studies (e.g., [6,11,14]) have proposed alternative techniques for developing DQ metrics, which consider assessments of uncertainty, hazard probabilities, and/or information value. Arguing that currency, and possibly other DQ dimensions, should be defined and assessed in probabilistic terms, Heinrich and Klier [4] propose probability-based currency metrics (PBCM) that assign a [0,1] probability of data still being current, given the associated distribution functions and the time-lag since acquisition. Heinrich and Hristova [8] develop PBCM that consider multiple state transitions between data acquisition and assessment, and can be applied to discrete-state as well as to continuous-state variables. Similarly, Wechsler and Even [9] estimate the likelihood of future currency decline given the value recorded at the time of acquisition and the number of transition stages.

Adopting Heinrich and Klier's [4] view, this study adheres to the notion of currency as the likelihood of data values still reflecting the correct real-world state, considering the time-lag since data acquisition and possible state transitions occurring during that time period. Similarly to Wechsler and Even [9] and Heinrich and Hristova [8], it uses a Markov chain model as a baseline for developing a metric that estimates a [0,1] likelihood of currency decline (Eq. (2)). However, the decline is expressed in this study in an explicit functional form that reflects a continuous-time variable.

## 2.2. Currency analysis and improvement

In association with the TDQM framework's stages of analysis and improvement, studies have highlighted possible root causes for currency declines, assessed their negative impact on decision-making and business success, and offered solutions and guidelines for data reacquisition and updating.

In general, the benefits gained by DQ improvement cannot always justify the associated costs, and aiming at perfect DQ is not necessarily optimal from an economic viewpoint [6,11]. One ought to consider the inherent cost–benefit tradeoffs while driving toward cost-effective DQ management, which requires an equilibrium to be found between the benefits associated with DQ improvement (i.e., preventing the damages

Please cite this article as: Y. Zak, A. Even, Development and evaluation of a continuous-time Markov chain model for detecting and handling data currency declines, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.09.006

inflicted by poor DQ) and the costs involved in DQ improvement ([7, 17]). Obviously, this thinking applies to the handling of currency declines as well, as a better understanding of the cost–benefit implications can help when optimizing data auditing and reacquisition policies [6, 11]. Adopting this thinking, the model developed in this study associates the handling of currency declines with damage prevention and reacquisition costs, with a view toward setting cost-effective auditing policies.

Some studies have developed analytical solutions for analyzing and handling currency declines in scenarios that involve repetitive and automated back-end data processes that typically must deal with the acquisition and transfer of massive data volumes, given certain timeframe and computational capacity constraints. For example, Cho and Garcia-Molina [15] examine currency decline in the context of automated data retrieval with web-crawlers, and estimate update frequencies to optimize crawler operation. Razniewski and Nutt [16] examine currency declines in a similar context, although they also consider processoperation costs and the benefits associated with possessing up-to-date information. Zong et al. [10] link currency declines to data-process latencies and offer a solution for optimizing the operation of environments that involve automated integration of data from multiple sources.

Other studies, as well as this study, have focused on currency declines in manual data-acquisition scenarios, which are not necessarily repetitive and often handle only a small number of data records at a time. In such scenarios, the baseline used for detecting currency declines may also serve as a relevant source for reacquiring the correct values, e.g., when contacting customers for the sake of verifying their details, a representative may choose to correct outdated details [7]. The decision of whether or not to revisit and reacquire data manually may involve substantial cost–benefit tradeoffs. On the cost side, manual data reacquisition requires time and efforts from end-users [4,7]. On the benefit side, as currency declines might diminish the usability of data resources, data reacquisition often leads to better decision-making, greater income, or loss-prevention [8,13,17].

A few studies have demonstrated the hazardous impact of currency declines and the associated cost–benefit tradeoffs in the context of Customer Relationship Management (CRM) data (e.g., [5,7,17]), and even more specifically in the context of insurance-related data ([4,8,18]). However, while previous studies have focused on linking currency to insurance-related assessment of customer state and policy offers, this study focuses more on data reacquisition. Given insurants' current state, the time-lag since their data was last updated, and the cost of data reacquisition, should they be contacted to verify their current state, and what would be the optimal timing for taking such action?

## 2.3. Markov chain models

The fundamental Markov Chain (MC) model reflects a discrete-time, discrete-state stochastic process of stationary and memory-less transitions, i.e., the probability of transitioning to a certain state depends only on the present state and does not change over time [21]. The MC model and its later extensions (e.g., continuous time and/or continuous state-space) have been explored in a broad range of scientific and applied domains, including data management and the associated challenges, e.g., for improving query performance in data warehouse environments [19].

In the context of DQ management, Heinrich and Hristova [8] used MC modeling for quantifying the impact of currency declines on data fitness for decision-making. The MC model is used to define PBCM for both discrete-state and continuous-state variables, which consider multiple transitions between data acquisition and assessment. Similarly, Wechsler and Even [9] represented real-world state transitions as a discrete-time MC model that can help when estimating the likelihood of future currency decline, given the current value. Zong et al. [10] apply MC modeling for assessing currency declines in complex data environment that integrate data from multiple operational sources, and optimizing data processing schedules accordingly.

Similarly to these latter studies, this study applies MC modeling for assessing and managing the risk of currency declines – but with some key differences. While a key concern of Abdellatif et al. [19] and Zong et al. [10] was performance optimization from a technical perspective (query speed, processing capacity), this study takes an economic rather than a technical perspective and focuses on the damage to data usability and value due to currency declines. Heinrich and Hristova [8] examine economic aspects; however, unlike this study, their analysis and evaluation focuses more on the impact of currency decline on decisionmaking performance, and less on the establishment of currencyimprovement policies. On the other hand, Wechsler and Even [9] associated the MC model with DQ maintenance and improvement policies, although their analysis focused on the assessment of correctness without considering economic aspects and cost–benefit tradeoffs.

## 3. Model development

The model introduced in this section describes a possible mechanism behind currency declines, within data-management scenarios that have certain key characteristics:

• Discreteness of State Space: The target data attribute (e.g., marital status, country of residence, or education level) adheres to a discretevalue domain with a finite set of pre-defined data values.

• Accuracy upon Data Acquisition: The value of the target data attribute correctly reflects the real-world state at the time of acquisition. Further, it is assumed that the set of values is regulated by some mechanism that prevents invalid values from being recorded, e.g., a database constraint, a lookup table, or a drop-down list in a data-entry interface.

• Loss of Accuracy over Time: As the real-world state of the entity described by the data value may change over time, the recorded value of a data attribute might become inaccurate. If a recorded data value is not updated regularly, its currency might decline over time.

The use of the Markov chain approach as a basis is motivated by the need to reflect and evaluate the formation of quality defects as an evolving and stochastic process, and not just as a “snapshot” assessment at a certain point in time. Model development is guided by the assumption that as the time-lag since data acquisition or correction increases, so does the likelihood of failing to reflect real-world state transitions correctly, and hence the chance of currency decline. Given the actual value of the target attribute under evaluation, and the time since its acquisition or last update, the model aims to answer three key questions regarding the target data attribute under evaluation:

a) Considering the time-lag since the last acquisition, what is the likelihood of inconsistency between the currently recorded data and the correct real-world state?

b) Assuming correct data at the time of acquisition, what is the expected time-lag until that data becomes incorrect?

c) Considering damage prevention versus cost, should data be reacquired? If so, what would be the optimal timing for reacquisition?

Our model development adopts as its basis the MC formulation proposed by Wechsler and Even [9]. That formulation represents changes in the value of a certain data attribute, which reflects a characteristic of a real-world entity, as a stochastic process of transitions between N possible states {x } . It models time as a discrete variable (t = 0, 1, 2…), with the steps in [t] associated with equal time intervals. Each probability $P _ { i j }$ reflects the likelihood of transitioning from the present value x<sub>i</sub> to value $x _ { j }$ within a single time interval. Consistently with the MC assumption of memory-less transitions, $P _ { i j }$ depends only on the present value and does not change over time. The collection of transition probabilities forms the transition matrix $P ,$ where $\textstyle \sum _ { j = 1 . . N } P _ { i , j } = 1$ for each [i].

$$
P = \left[ \begin{array}{c c c} P _ {1 1} & \dots & P _ {1 N} \\ \vdots & \ddots & \vdots \\ P _ {N 1} & \dots & P _ {N N} \end{array} \right]\tag{1}
$$

Under the assumption of a stationary transition matrix, $\begin{array} { r } { P ( t ) = P ^ { t } \mathbf { e n } \cdot } \end{array}$ capsulates the set of probabilities for a state change from x to $x _ { j }$ after t time intervals. Accordingly, $A _ { i } ( t ) = P _ { i i } ( t )$ expresses the likelihood of a certain value x recorded at time $t = 0 ,$ , remaining correct at a later time t.

This basic formulation is now extended to address some of the limitations of the previous model, by considering time as a continuous variable rather than a discrete one, and taking into account cost–benefit tradeoffs. The CTMC model treats the optimization problem as a continuous stochastic process, rather than as discrete stochastic process, but still assumes that the time spent with value x maintains the memoryless property [21]. If the random variable $\tau _ { i }$ denotes the time spent with value x before transitioning, then $P \{ \tau _ { i } { > } s + t | \tau _ { i } { > } s \} = P \{ \tau _ { i } { > } t \}$ and $\tau _ { i }$ must, therefore, be exponentially distributed. The transition probability from $x _ { i }$ to $x _ { j }$ depends on the transition time, and hence $P _ { i j } ( t ) = P \{ X ( t + s ) { \stackrel { \cdot } { = } } j | X ( s ) = i \}$

The model proposed here meets the following DQ management characteristics: a discrete set of possible values, continuous time, correctness at time of acquisition, loss of correctness over time associated with some damage, and non-trivial reacquisition cost. The time since the last data acquisition is denoted (t). The real-world property described by the target attribute has N possible categories and, hence, the value of the target attribute can be one of the N possible values $\lbrace x _ { i } \rbrace _ { i = 1 \dots N } .$ If the present value of the target attribute is $x _ { i } ,$ while the corresponding real-world value is $x _ { j } ,$ then the data value is considered to be correct only $\mathrm { i f } i = j ,$ and incorrect otherwise. Notably, by time (t), the real-world value could have undergone several transitions. However, the model's formulation accounts for the first transition only.

Using this formulation, the questions introduced earlier can now be rephrased, given that the target attribute holds the value x that has been acquired at time $t = 0 \colon$

a) What is the probability $P _ { i } ^ { A } ( t )$ that the $x _ { i }$ value is still correct at a later point in time, tN0?

b) What is the expected time $\overline { T } _ { i } ^ { N }$ from acquisition until the value becomes incorrect?

c) Considering potential damages versus potential costs, can the reacquisition of that value be justified, and if so, what would be the optimal time $\overline { { t } } _ { i } ^ { O P T }$ for it?

## 3.1. Estimating the likelihood of incorrectness

Under the assumption that transition between states can potentially occur at any point along a continuous timeline, the CTMC representation of the probability of transition $P _ { i j } ( t )$ from state [i] to state [j] as a function of time accounts for two characteristics of the process [21]: a) the constant probability $P _ { i j }$ of transitioning from state [i] to state [j] $\left( \operatorname { E q . } \left( 1 \right) \right)$ is neither dependent on the time (t) nor on states earlier than state [i]; and b) the exponentially distributed time between transitions depends on the current state [i], as well on the next state. It is defined as proportional to $\exp ( - \lambda _ { i j } )$ , where $\lambda _ { i j }$ is the transition rate from state [i] to state [j].

This formulation is consistent with scenarios handled by this study. Each state reflects a value from the set of N possible values $\{ x _ { i } \} _ { i = 1 \dots N } { \mathsf { a } } S -$ sociated with the target attribute. The state transition parameters depend on the source value x and the target value $x _ { j \cdot }$ According to this formulation, the time between transitions is thus exponentially distributed. Hence, if the value of the target attribute was set to state [i] at time $t { = } 0 ,$ , the probability that it will transition to state [j] by time (t) can be expressed as $P _ { i j } ( t ) = P ( t | i \xrightarrow { } j ) = P _ { i j } \cdot ( 1 - \exp ( - \lambda _ { i j } t ) )$

The first question can now be answered. Given that the target attribute was set to state [i] at the time of acquisition $( t = 0 )$ , the probability $P _ { i } ^ { A } ( t )$ of this value remaining correct at time (t) can be expressed as the complement of the sum of probabilities of transitioning from state [i] to a different state [j] at time (t):

$$
P _ {i} ^ {A} (t) = 1 - \sum_ {j \neq i} P _ {i j} (t) = 1 - \sum_ {j \neq i} \left(P _ {i j} \cdot \left(1 - e x p (- \lambda_ {i j} t)\right)\right)\tag{2}
$$

Notably, this formulation allows the correctness of a single data value, associated with a certain target attribute, to be assessed by estimating transition parameters, e.g., by evaluating previously collected data, as demonstrated in the next section. This assessment does not rely on verification against an auxiliary baseline, as mandated by other assessment methods. Using weighted aggregation of attribute-level estimations (e.g., as proposed by [3]), this formulation can be further extended to estimate the currency level of a data record with multiple attributes, or even an entire dataset.

## 3.2. Estimating the average time until a data value becomes incorrect

To answer the second question, the likelihood of incorrectness $P _ { i } ^ { N } ( t )$ (a complement of Eq. (2)), given that the target attribute was set to state [i] at time $t = 0$ , can be expressed as $\begin{array} { r } { P _ { i } ^ { N } ( t ) = 1 - P _ { i } ^ { A } ( t ) = \sum _ { j \neq i } P _ { i j } \cdot ( 1 - \exp ( - \lambda _ { i j } t ) ) } \end{array}$ . Accordingly, the density function $f _ { i } ^ { N } ( t )$ of $\bar { P } _ { i } ^ { N } ( t )$ , can be expressed as

$$
f _ {i} ^ {N} (t) = d \left(\sum_ {j \neq i} \left(P _ {i j} \cdot \left(1 - e x p (- \lambda_ {i j} t)\right)\right)\right) / d t = \sum_ {j \neq i} P _ {i j} \lambda_ {i j} e x p (- \lambda_ {i j} t)\tag{3}
$$

Therefore, the mean time $\overline { T } _ { i } ^ { N }$ until the value of the target attribute, which was set to state $[ i ]$ at time $t = 0$ , becomes incorrect can be expressed as:

$$
\overline {{T}} _ {i} ^ {N} = E \left[ f _ {i} ^ {N} (t) \right] = \int_ {0} ^ {\infty} \left(t \cdot f _ {i} ^ {N} (t)\right) d t = \int_ {0} ^ {\infty} \left(t \cdot \sum_ {j \neq i} P _ {i j} \lambda_ {i j} \exp (- \lambda_ {i j} t)\right) d t\tag{4}
$$

The expression in $\operatorname { E q . } \left( 4 \right)$ is a linear combination of expressions of similar form. It can therefore be reformulated as $\begin{array} { r } { E [ f _ { i } ^ { N } ( t ) ] = \bar { \sum _ { j \neq i } } E [ G _ { i j } ( t ) ] } \end{array}$ where $G _ { i j } ( t ) = P _ { i j } \lambda _ { i j } \exp ( - \lambda _ { i j } t )$

The mean of each $G _ { i j } ( t )$ can be calculated as

$$
\begin{array}{r l} E \left[ G _ {i j} (t) \right] & = \int_ {0} ^ {\infty} \left(t \cdot P _ {i j} \lambda_ {i j} e x p (- \lambda_ {i j} t)\right) d t \\ & = \left[ - P _ {i j} \cdot \left(t + \frac {1}{\lambda_ {i j}}\right) \cdot e x p (- \lambda_ {i j} t) \right] \frac {\infty}{0} = \frac {P _ {i j}}{\lambda_ {i j}} \end{array}\tag{5}
$$

Hence, the expected time $\overline { T } _ { i } ^ { N }$ from acquisition until the value becomes incorrect can be expressed as

$$
\overline {{{T}}} _ {i} ^ {N} = E \left[ f _ {i} ^ {N} (t) \right] = \sum_ {j \neq i} E \left[ G _ {i j} (t) \right] = \sum_ {i \neq j} \frac {P _ {i j}}{\lambda_ {i j}}\tag{6}
$$

Similarly to the solution offered to the first question, this formulation permits answering the second question by estimating transition parameters, without having to rely on an auxiliary baseline.

## 3.3. Setting cost-effective data reacquisition policie

The third question, regarding the optimization of the data reacquisition time, requires a formulation that reflects the assessment of cost– benefit tradeoffs, beyond the state-transition parameters that were used to answer the first two questions. In the context of data quality management, the costs can be associated with data evaluation and reacquisition efforts (e.g., contacting customers to validate their personal details, or acquiring a verified dataset from a reliable source). In this study, the benefits are conceptualized as prevention of the potential damages associated with the misuse of incorrect data. However, depending on the context and the characteristics of the datamanagement scenario, the benefits can also be attributed to a potential improvement in data usability and reliability.

The formulation is based on the definition of the damage function $d _ { i j } ( t )$ , which reflects the expected damage associated with a target value being set to x when the correct value would have been $x _ { j \ast }$ All damage functions $\{ d _ { i j } ( t ) \}$ are non-negative, monotonically increasing over time (however, not strictly monotonic, as the damage may be constant for certain time intervals), and bounded by a finite upper limit. No damage is associated with a correct value $( \mathrm { i . e . , } d _ { i i } ( t ) = 0 )$ , nor is there any at the time of acquisition $( \mathrm { i } . \mathbf { e } . , d _ { i j } ( 0 ) = 0 )$ , under the assumption that data is recorded correctly at the time of acquisition. Further, the assumption is that damage inflicted prior to the reacquisition point $( t = 0 )$ cannot be changed.

The cumulative damage function $\begin{array} { r } { D _ { i } ( t ) = \sum _ { j \neq i } ( P _ { i j } ( t ) { \cdot } d _ { i j } ( t ) ) } \end{array}$ reflects the accretion of damage functions at time (t), weighted by the probability $P _ { i j } ( t )$ that a data attribute with value x at $t = 0$ has transitioned to value x at time (t). Therefore, as $D _ { i } ( t )$ is a linear combination of $\{ d _ { i j } ( t ) \}$ with non-negative weights, it is also monotonically non-decreasing with time and bounded by a finite upper limit, where $D _ { i } ( 0 ) = 0$ and $D _ { i } ( t ) { \geq } 0$ otherwise. As stated earlier, this formulation accounts for the first transition only, although in reality x could have followed several transitions.

Similarly to the damage function, the reacquisition cost function $C _ { i } ( t )$ depends on the present state [i] and the time (t) since the last acquisition. It is also non-negative, monotonically non-decreasing with time, and may be a constant: $C _ { i } ( t ) = c _ { i } .$

The third question regarding optimal reacquisition time can now be answered, by solving:

$$
C _ {i} (t) = D _ {i} (t) = \sum_ {j \neq i} \left(P _ {i j} (t) \cdot d _ {i j} (t)\right)\tag{7}
$$

The optimal reacquisition time $\overline { { t } } _ { i } ^ { O P T }$ would be the first point where the cumulative damage exceeds the reacquisition cost. In other words, $\overline { { t } } _ { i } ^ { O P T }$ would be the smallest value of (t) that solves Eq. (7). Both the cost function $C _ { i } ( t )$ and the damage function $D _ { i } ( t )$ are non-negative and monotonically non-decreasing. The smallest solution to Eq. (7) within the relevant range would therefore be non-negative. A case where Eq. (7) has no solutions within that range would be interpreted as a scenario in which data reacquisition would be costlier than the expected damage at any point in time; hence, reacquisition cannot be justified.

![](/api/attachments/9HKZFYPV/fulltext/images/91390932499a656b56181d89f091dd559c6812271726d9feb77c5de978083bda.jpg)

Fig. 1 depicts two possible scenarios for Eq. (7). Under (a), the damage $D _ { i } ( t )$ increases at a greater rate than the cost C (t); hence, Eq. (7) has a single optimal solution $\overline { { t } } _ { i } ^ { O P T }$ . Under (b), the damage $D _ { i } ( t )$ increases at a lesser (or equal) rate than the cost $C _ { i } ( t ) ;$ hence, Eq. (7) has no solution, and the reacquisition cannot be justified. Considering $P _ { i j } ( t ) { = } P _ { i j } ( 1 { - } \exp ( - \lambda _ { i j } t ) )$ ), as implied by the formulation of the proposed CTMC model, and extending Eq. (7) accordingly, the optimal time for data reacquisition $\overline { { t } } _ { i } ^ { O P T }$ can be assessed by solving:

$$
C _ {i} (t) = D _ {i} (t) = \sum_ {j \neq i} \left(P _ {i j} \cdot \left(1 - e x p (- \lambda_ {i j} t)\right) \cdot d _ {i j} (t)\right)\tag{8}
$$

In reality, reacquisition cannot always occur at the exact recommended point in time. In some data-management scenarios, such as the one described in the following section, some delay in reacquisition is tolerated; however, beyond a certain timepoint the flawed data records might become irrelevant and correction of data values can no longer be justified [7]. To address such scenarios, the model is extended to define a reacquisition interval $[ \overline { { t } } _ { i } ^ { O P T } , \overline { { t } } _ { i } ^ { E N D } ]$ , where the upper bound $\overline { { t } } _ { i } ^ { E N D }$ reflects the latest point in time that justifies reacquisition. To detect that endpoint, the damage for state [i] $( D _ { i } ( t )$ in Eq. (8)) is reformulated to

$$
D _ {i} ^ {*} (t) = D _ {i} (t) \cdot N _ {i} (t)\tag{9}
$$

where

• D<sub>i</sub><sup>∗</sup>(t) – Adjusted damage function for state [i]

$D _ { i } ( t )$ – Damage function for state [i]

• N<sub>i</sub>(t) – Decay function for state [i]

The decay function $N _ { i } ( t )$ is non-negative and non-increasing (as depicted in Fig. 2a), and decays at an exponential rate, similarly to previous formulations (e.g., [6,16]). The reacquisition interval is defined by $\overline { { t } } _ { i } ^ { E N D } > \overline { { t } } _ { i } ^ { O P I }$ , where $\overline { { t } } _ { i } ^ { O P I }$ is the smallest solution to Eq. (8). Accordingly, the

![](/api/attachments/9HKZFYPV/fulltext/images/20bfa66615d8642109cf80516099c91a249268e69fd49cf1be2ee78d75b8de31.jpg)  
Fig. 1. Reacquisition time optimization: (a) single solution versus (b) no solution.

Please cite this article as: Y. Zak, A. Even, Development and evaluation of a continuous-time Markov chain model for detecting and handling data currency declines, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.09.006

![](/api/attachments/9HKZFYPV/fulltext/images/7d6a90f047a7d7ed02c38ae7cd4588e31e586d7a23c4a0b239a56d1553f78bd6.jpg)

![](/api/attachments/9HKZFYPV/fulltext/images/818dc706d3da31e0fd2e8996e3c6671feb2b2807a6f1e0813f4edfafcb5948e2.jpg)  
Fig. 2. Reacquisition interval, considering damage-prevention decay.

decay function $N _ { i } ( t )$ is set as 1 up to this point, and decays exponentially afterwards, as depicted in Fig. 2a.

$$
N _ {i} (t) = \left\{ \begin{array}{l l} 1 & t \leq \bar {t} _ {i} ^ {O P T} \\ e x p \Big (- \gamma_ {i} \Big (t - \bar {t} _ {i} ^ {O P T} \Big) \Big) & t > \bar {t} _ {i} ^ {O P T} \end{array} \right.\tag{10}
$$

where

$\overline { { t } } _ { i } ^ { O P T }$ – Optimal time point that solves Eq. (8) for state [i]

$\gamma _ { i } -$ The decay rate for state [i], defined by $\gamma _ { i } = ~ \ln ( 2 ) / ( t _ { h a l f - t i m e } -$ $\overline { { t } } _ { i } ^ { O P T } )$

$t _ { h } - \mathsf { A }$ point in time beyond $\overline { { t } } _ { i } ^ { O P T }$ , at which the damage is halved

As D<sub>i</sub>(t) is bounded by a finite upper limit, this formulation implies that D<sup>∗</sup>(t)→0 as t→∞.

Unlike the earlier solution to Eq. (7), which could yield a single optimum time point $\overline { { t } } _ { i } ^ { O P T }$ , a cost versus adjusted damage comparison, $C _ { i } ( t ) = D _ { i } ^ { * } ( t )$ , may yield up to two crossing points, denoted $\overline { { t } } _ { i } ^ { O P T }$ and $\overline { { t } } _ { i } ^ { E N D }$ . Accordingly, the data reacquisition time (t) must be chosen within the time interval $\overline { { t } } _ { i } ^ { O P T } \leq t \leq \overline { { t } } _ { i } ^ { E N D }$ for which the adjusted damage D<sup>∗</sup>(t) is greater than the cost $C _ { i } ( t )$ . Outside the boundaries of this range, the cost is higher than the damage, and so reacquisition cannot be justified.

As depicted in Fig. 2b, this solution is feasible only for a time range in which $D _ { i } ^ { * } ( t )$ is concave. Therefore, use of Eqs. (9) and (10) relies on the existence of a certain $t _ { i } ^ { C O N }$ for which the adjusted damage function $D _ { i } ^ { * } ( t )$ is concave for all (t) within the interval $[ 0 , \check { t _ { i } ^ { C O N } } ]$ . Obviously, the existence of a $t _ { i } ^ { C O N }$ boundary is not obvious and its calculation is far from being trivial. It may depend on the specific context in which the model is applied, and therefore has to be assessed prior to the use of the decayfunction extension. Appendix A shows that in a case where $d _ { i j } ( t )$ is a constant for each [i], [j] and (t), the time boundary $t _ { i } ^ { C O N }$ can be deter mined, if exists. Notably, the evaluation described in the following section meets this condition, and hence permits the use of the adjusted damage function.

Since use of the extended formulation requires the concavity of the function to be evaluated, setting the optimal data reacquisition policy involves the following steps:

1. By solving $\operatorname { E q . } ( 7 ) ,$ , find $\overline { { t } } _ { i } ^ { O P T }$ , the lower bound of the reacquisition interval. If no solution can be found, the implication is that reacquisition cannot be justified, as the cost is always higher than the potential damage prevention.

2. Find a point $t _ { i } ^ { C O N } > \overline { { t } } _ { i } ^ { O P T }$ for which the adjusted damage $D _ { i } ^ { * } ( t )$ is concave within $[ 0 , t _ { i } ^ { C O N } ] .$

a. $\textsf { A } t _ { i } ^ { C O N } {  } { \infty }$ solution implies that $D _ { i } ^ { * } ( t )$ is concave for $t > 0$

b. If no solution can be found, the extended formulation cannot be used; in this case, set $\overline { { t } } _ { i } ^ { O P T }$ as the optimal reacquisition time point.

3. Within the concavity range $[ \overline { { t } } _ { i } ^ { O P T } , t _ { i } ^ { C O N } ] .$ , search for $\phantom { } _ { 1 } \overline { { t } } _ { i } ^ { E N D } > \overline { { t } } _ { i } ^ { O P T }$ for setting the upper bound of the reacquisition interval by solving Eq. (9).

a. If a second solution exists that meets the condition $\overline { { t } } _ { i } ^ { E N D } < t _ { i } ^ { C O N }$ , set the reacquisition interval to $\overline { { t } } _ { i } ^ { O P T } \leq t \leq \overline { { t } } _ { i } ^ { E N D }$

b. Otherwise, set the reacquisition interval to $\overline { { t } } _ { i } ^ { O P T }$ ≤t ≤ $t _ { i } ^ { C O N }$ .

Notably, N (t) can be adjusted to reflect different decay characteristics. In such cases, the $\overline { { t } } _ { i } ^ { O P T }$ threshold in the $N _ { i } ( t )$ formulation must be modified accordingly.

To conclude this section: the proposed CTMC model reflects a common mechanism behind data currency declines. By linking currency declines to cost–benefit assessments, the model aims at addressing a few key challenges: assessing currency levels without having to rely on a baseline for comparison, estimating the expected time-lag until a newly acquired data value becomes outdated, and setting costeffective policies for data reacquisition.

Claim-filling process states.

<table><tr><td>State</td><td>Description</td><td>Transitions to other states</td></tr><tr><td>1. Data received</td><td>THE FIRM receives the insurant&#x27;s data from the HMO.</td><td>2, 7</td></tr><tr><td>2. Form delivered to insurant</td><td>The insurant is contacted and asked to fill in claim forms, delivered via mail or a field representative.</td><td>3, 4, 6, 7</td></tr><tr><td>3. Pending employer signature</td><td>The insurant is required to get an employer&#x27;s signature on the claim form.</td><td>4, 6,7</td></tr><tr><td>4. Form returned to firm</td><td>After signing by the employer, the insurant must send back the forms, together with relevant medical documentations, via mail or a field representative.</td><td>5, 6, 7</td></tr><tr><td>5. Claim filed by firm</td><td>A representative of THE FIRM files the claim with the NIO and the claim is then pending discussion and approval.</td><td>3, 8, 9</td></tr><tr><td>6. Claim filed independently</td><td>The insurant files the claim independently, with no assistance from FIRM representatives.</td><td>-</td></tr><tr><td>7. Claim process suspended</td><td>The insurant is impossible to contact, or hesitates to file a claim.</td><td>2, 6, 9</td></tr><tr><td>8. Claim approved</td><td>The NIO approves the claim, and the HMO reimburses THE FIRM.</td><td>-</td></tr><tr><td>9. Claim process terminated</td><td>The NIO rejects the claim or the claim is closed if the insurant refuses to file a claim.</td><td>-</td></tr></table>

## 4. Evaluation

This section details an evaluation of the proposed model, using a comprehensive dataset that reflects a real-world business process. The data source for model evaluation in this study is a privately-owned service provider (THE FIRM hereinafter), which annually handles tens of thousands of insurance claims related to work accidents for health maintenance organizations (HMOs). To receive injury-related benefits, as one-time compensation, monthly payments, or reimbursement for medical expenses, the insurant must file a claim with the National Insurance Organization (NIO). Claim filing is a lengthy bureaucratic process that requires the application to be submitted along with relevant medical records and assessments from medical specialists. Representa tives of THE FIRM assist its insurants with the claim-handling process, and the HMOs reimburse THE FIRM after completing the process successfully.

The claim-handling process involves a few stages, some of which require correspondence with the insurant or the NIO (Table 1). Insurants often fail to report their progress as required and, as a result, their recorded status is often incorrect. Status discrepancies might imply severe monetary penalties for THE FIRM. For example, if the insurant signs the claim forms but fails to report it, the HMO will not reimburse THE FIRM. To avoid such damages, FIRM representatives call insurants to validate their status using a contact list based on some experience-based heuristics. Due to time constraints, a representative can handle only a limited number of daily calls. Moreover, many calls turn out to be unnecessary, as the status of the insurant has not changed since the previous call. While the cost of such calls is high, the database still contains important errors with respect to insurant status. Hence, the associated damage is high and representative calls are not cost-effective.

THE FIRM's claim-handling process meets the characteristics of the proposed model:

Discreteness of State Space: As shown in Table 1, the status variable of an insurant reflects a discrete value domain of nine possible states, with possible transitions between states.

Continuous Time: State transitions and representative calls may occur at any point in time. Currently, the customer-care representative's choice of which insurant to call next is not made in advance, at the beginning of each day, but rather spontaneously at the end of the previous call.

Correct Data Entry: An insurant typically reports the correct state when called, and the representative records it correctly online through a robust data-entry utility.

Loss of Correctness over Time: The recorded status fails to reflect the correct state when insurants fail to report transitions in status, but representatives can make only a limited number of verification calls.

Incorrectness Damage: THE FIRM realizes revenues only after claim approval (state #8 in Table 1). States #6, #8 and #9 in Table 1 reflect irreversible stationary points. If the insurant has decided to file the claim independently (state #6), or the insurant's claim is rejected or closed (state #9), handling of that case by customer-care representatives terminates, and THE FIRM will not be reimbursed for that effort. Once the claim is approved (state #8), the process terminates as well. Therefore, if an insurant reaches a stationary irreversible point, THE FIRM cannot realize any revenue and, to avoid damage, must be aware that the insurant has already entered, or is about to enter, one of those states.

Reacquisition Cost: Each representative phone call typically lasts 5 to 15 min.

## 4.1. Data collection and estimation of model parameters

THE FIRM has provided 10 monthly snapshots of its data, one at the beginning of each consecutive month. The dataset used for evaluation included 1,043,183 records, reflecting the activity of 151,451 insurants in total. Among those records, 74,844 reflect phone contacts with insurants, while the other records re ect customers for which FIRM representatives recorded updates, but with whom no contact has been made. To maintain strict privacy and confidentiality, THE FIRM masked identifiers with numeric codes, removing any details that could possibly identify the insurants or representatives.

The first step taken to collect and prepare the data for analysis was to classify the target “current state” attribute per record according to Table 1, using a discrete numeric value ranging from 1 to 9. The next preparation step dealt with the date and time of the most recent call by a representative, detecting whether or not the representative contacted an insurant during the time between two consecutive database snapshots. However, since only the most recent call appears in the dataset, it was impossible during data preparation to detect multiple calls between two consecutive snapshots. In the absence of exact status updates about the date and time in the database, it was possible to detect state transitions by comparing two consecutive records relating to the same insurant. A state transition occurring during a certain period was then assigned with the date and time of the last call within that period.

Detection of multiple calls within a single period was impossible and, therefore, the possibility of multiple transitions within a single period was disregarded, assuming that at most one transition occurred. Due to the memory-less transition characteristic of a Markov chain model, this assumption does not bias model outcomes significantly. For insurants that were not contacted at all by THE FIRM's representatives during a certain period, it was impossible to detect precisely whether or not their real-world state had actually changed. In such cases, the timing of a transition and the associated model parameters were approximated by observing actual transitions of insurants at the same state that were approached by customer-care representatives during the same period. For example, at a certain period #k, M out of N insurants who were approached by customer-care representatives had transitioned from state [i] to a different state [j]. Accordingly, the transition probability at period #k for insurants at state [i] is estimated as $P ^ { \prime } { = } M / N ,$ and the estimated damage for insurants who were not approached is estimated at $\begin{array} { r } { D ^ { \prime } { = } ( M / N ) ^ { * } { \sum } _ { j \neq i } ( P _ { i j } { \cdot } d _ { i j } ( t ) ) } \end{array}$ , where {P<sub>ij</sub>} and $\{ d _ { i j } ( t ) \}$ } are the estimated transition parameters for that period.

Of the 10 monthly snapshots that THE FIRM provided, we used the first six periods (#1 to #6) as a training set (605,387 records, 42,393 actual phone contacts) for estimating the model parameters.

Transition Matrix {P}: We rst calculated a transition matrix $\left( \operatorname { E q . } \left( 1 \right) \right)$ for each period separately. After testing and confirming matrix similarity, using a paired t-test with a significance level of 0.05, we recalculated

![](/api/attachments/9HKZFYPV/fulltext/images/90979e0527daa3400890d9a7c395d01bc52844282671b3ad98346d601772bf8b.jpg)  
Fig. 3. Transition distribution example

Please cite this article as: Y. Zak, A. Even, Development and evaluation of a continuous-time Markov chain model for detecting and handling data currency declines, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.09.006

Y. Zak, A. Even / Decision Support Systems xxx (2017) xxx–xxx

Table 2  
Potential damage prevention — current practice versus Markov-based model.

<table><tr><td>Period</td><td>Records</td><td>Records to reacquire</td><td>Potential damage</td><td>Damage prevented – actual</td><td>Damage prevented – model</td><td>Improvement percentage</td></tr><tr><td>7</td><td>103,909</td><td>6402</td><td>12,396.31</td><td>728.12 (6%)</td><td>3246.77 (26%)</td><td>346%</td></tr><tr><td>8</td><td>111,292</td><td>7324</td><td>15,602.61</td><td>1130.21 (7%)</td><td>3908.84 (25%)</td><td>246%</td></tr><tr><td>9</td><td>111,263</td><td>8106</td><td>15,552.74</td><td>1537.85 (10%)</td><td>4305.63 (28%)</td><td>180%</td></tr><tr><td>10</td><td>111,332</td><td>12,609</td><td>14,469.79</td><td>1057.71 (7%)</td><td>5828.57 (40%)</td><td>451%</td></tr></table>

a single transition matrix for all training set periods. The estimated matrix aligned well with how THE FIRM's managers understand state transitions within the business process.

Transition Rates $\{ \lambda _ { i j } \} \dot { }$ Using the Kolmogorov–Smirnov (K-S) test for goodness of fit, 56% of the evaluated transitions followed the exponential distribution with a significance level of 5% or better. As demonstrated in Fig. 3, some of the other transition distributions either had visual similarity to the exponential distribution or had too few samples to support confirmation with reasonable statistical significance. Despite the limited support for the assumption of exponentially distributed transitions, the model evaluation proceeded as planned, to assess whether it can still yield better predictive results and save significant costs, compared to current work practices.

## 4.2. Model application and evaluation of performance

Of the 10 monthly snapshots that THE FIRM provided, the last four periods (#7 to #10) were used to evaluate model performance. The evaluation included only insurants with a known state at the beginning of each period – a total of 437,387 insurant records, among them 34,441 that reflect actual phone contacts. In other words, we excluded insurants added during the period. In addition, we excluded those that reached a stationary state by the end of the period (i.e., states #6, #8 or #9).

The model could be applied for estimating currency levels and transition times, the first and the second DQ management challenges highlighted in the previous section. However, the precision of those estimations could not be verified, as the evaluation relied on previously collected historical data, for which currency levels and transition times have not been recorded. However, use of the model for optimizing reacquisition timing policy, the third question highlighted in the previous section, could be evaluated comprehensively against real-time performance of customer-care representatives.

Considering assessments of potential damage and costs, the optimal reacquisition time for each insurant within each period was calculated using Eq. (8). The damage associated with incorrect data was set to zero at t=0, and the model estimated the damage at the end of the period, given the reacquisition time-point that was calculated. From THE FIRM's standpoint, the damage is realized if the insurant reaches state #6 or state #9 (the irreversible stationary points, as described earlier), but the data shows another state (state #7), not perceived by managers of THE FIRM as hazardous, at which stationarity is likely, and therefore monetary loss can potentially happen. The potential damage was therefore defined as the likelihood that an insurant had reached state #6, #7 or #9 at the end of a period, and the likelihood of those states to be stationary, given the current state.

Sorting the insurant records by their potential damage, from high to low, we compared the damage-prevention performance to current heuristics-based calls by THE FIRM's representatives. If representatives made a certain number M of calls within a certain period, we compared the M insurants actually called by representatives to the M insurants ranked by the model as having the highest potential damage. Table 2 compares the potential damage prevented by representatives' calls to the damage that could have been prevented had the recommendations of the model been adopted. In all periods, the damage that could have been prevented by model predictions (listed under the fourth “Damage Prevented – Model” column) is substantially higher that the damage actually prevented by representatives (listed under the third “Damage Prevented – Actual” column).

Following the latter comparison of estimated potential damage, the next step compares the actual damage that could have been prevented, had model recommendations been applied.

The evaluation compares the set of M actual calls, made by representatives during a certain period, to the same number of calls recommended by the model. The damage was calculated as the likelihood that an insurant had transitioned to state #6, #7 or #9, where the associated record has not been updated and indicated a different state, not perceived to be hazardous. If a representative reacquired the data for a certain insurant during a period, the assessment of actual damage observed the insurant state at the end of the period. If no contact is made with the insurant during a period, the actual damage was estimated by observing transitions of other insurants with similar characteristics. Damage is marked as “prevented” if an insurant transitioned to state #6, #7 or #9 by the end of a period, but was contacted during that period. On the other hand, damage is marked as “inflicted” if an insurant transitioned to state #6, #7 or #9 by the end of a period, but was not contacted.

Table 3 compares the damage prevented and the damage inflicted between the actual calls made by representatives and the same number of calls proposed by the model. In all periods, the model's performance significantly exceeded the current performance, in terms of increasing damage prevention and decreasing damage infliction. Notably, the gain associated with damage prevention is much higher than the gain associated with damage infliction.

The final step evaluates the model extension for handling possible decays in damage prevention (Eqs. (9) and (10)). This extension turned out to be relevant to many claim-handling cases, in which representatives are unable to complete the claim-handling process within a reasonable time. According to FIRM managers, the likelihood of an insurant completing the claim-handling process significantly decreases with time, to a point where it is nearly zero. As a decay parameter could not be determined from the dataset, its estimation was based on managers' experience and understanding of the business process, as is common in decision-calculus modeling [20].

Damage prevention and infliction — current practice versus Markov-based model.

<table><tr><td>Pd.</td><td>Records</td><td>Records to reacquire</td><td>Potential damage</td><td>Damage prevented – current</td><td>Damage prevented – model</td><td>Damage prevention gain (%)</td><td>Damage inflicted – current</td><td>Damage inflicted – model</td><td>Damage infliction gain (%)</td></tr><tr><td>7</td><td>103,909</td><td>6402</td><td>12,396.31</td><td>821.51 (7%)</td><td>5171.60 (42%)</td><td>530%</td><td>22,921.33 (185%)</td><td>18,571.24 (150%)</td><td>19%</td></tr><tr><td>8</td><td>111,292</td><td>7324</td><td>15,602.61</td><td>1132.42 (7%)</td><td>9974.20 (64%)</td><td>781%</td><td>27,267.93 (175%)</td><td>18,426.16 (118%)</td><td>32%</td></tr><tr><td>9</td><td>111,263</td><td>8106</td><td>15,552.74</td><td>2779.74 (18%)</td><td>10,656.29 (69%)</td><td>283%</td><td>19,870.10 (128%)</td><td>11,993.55 (77%)</td><td>40%</td></tr><tr><td>10</td><td>111,332</td><td>12,609</td><td>14,469.79</td><td>1589.81 (11%)</td><td>17,606.80 (122%)</td><td>1007%</td><td>21,468.35 (148%)</td><td>5451.36 (38%)</td><td>75%</td></tr></table>

Please cite this article as: Y. Zak, A. Even, Development and evaluation of a continuous-time Markov chain model for detecting and handling data currency declines, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.09.006

Table 4  
![](/api/attachments/9HKZFYPV/fulltext/images/1c8165051882407c2bcefa251b1503834e8c77e76ed70917867fc809ff17b14b.jpg)  
Fig. 4. The adjusted damage function for state 1.

The decay time variable [t] reflects the record's age – the number of days since the insurant's record was first included in the database. Accordingly, the record's age served as the input for the decay function, $\exp ( - \gamma _ { i } ( t ) )$ . Since the decay function reflects the insurant's total age, the threshold of the decay function N (t) was set to 0, assuming constant exponential decline that starts as soon as an insurant record enters the dataset. FIRM managers estimated that a year and a half (547 days) after the accident date, is it unlikely that the insurant will ever complete the process.

Eq. (10) was used to determine a decay rate (γ ) solution for $\exp ( - \gamma _ { i } . 5 4 7 ) .$ . Using a “goal seek” tool, the decay rate was set to $\gamma _ { i } =$ 0.0024 for all i, such that at the highest possible age of 547 days, the highest potential damage (0.213) decreases below the average reacquisition cost $( 0 . 5 5 ) { \cdot } D _ { m a x } { = } C _ { a v g } - { \varepsilon } ,$ where $C _ { a v g }$ is set to the average damage at the time of actual reacquisitions. Notably, the implication of this manager assessment is that an insurant with a record age of 547 days or higher will be considered by the FIRM as a permanent “loss”; hence, it is unlikely that reacquisition of data regarding that insurant will ever be conducted.

As highlighted earlier, a valid solution can be found only within $[ 0 , t _ { i } ^ { C O N } ]$ for which the adjusted damage function D<sup>∗</sup>(t) is concave. The upper bound $t _ { i } ^ { C O N }$ was calculated according to the method described in Appendix A. For states #2 and #3, D<sup>∗</sup>(t) was found to be concave for all (t), as the boundary was estimated at $t _ { i } ^ { C O N }  \infty .$ . For states #4, #5, #7, #8 and #9 the calculated $t _ { i } ^ { C O N }$ value was estimated to be beyond the 547-day boundary. For states #1 $( t _ { 1 } ^ { C O N } = 2 8 2 )$ and #6 $( t _ { 6 } ^ { C O N } { = } \dot { 4 } 2 7 )$ the adjusted damage function D<sup>∗</sup>(t) should be further validated for concavity within the time range of interest (0 to 547).

Fig. 4 depicts the estimation of the adjusted damage function D<sup>∗</sup>(t) for state #1. The starting point of each curve reflects a certain record age at the time of the last reacquisition. As indicated by Fig. 4, the first derivative of the adjusted damage function for state #1 (the evaluation of state #6 showed similar results) is negative for all (t) beyond its maximum point and decreases toward zero beyond the 547-day upperbound of the relevant age interval. Thus, although mathematically it is not necessarily concave for any (t) beyond $t _ { 1 } ^ { C O N } = 2 8 2$ , a comparison of the adjusted damage function D<sup>∗</sup>(t) with a cost function may yield only up to two solutions. Hence, the purpose of the decay function is met – avoiding the reacquisition of obsolete older records.

Table 4 summarizes the results of the latter evaluation stage. Similarly to the previous evaluation stage (Table 3), the performance associated with the proposed model superseded the performance associated with the current working method, in terms of increasing damage prevention and decreasing damage infliction. Here too, the gain associated with damage prevention is much higher than the gain associated with damage infliction. The gains shown in Table 4 appear to be much smaller than the gains shown in Table 3. However, the baseline for comparison is different. The latter test assumed that the actual damage associated with older records had already been realized. It therefore excluded that subset of insurants from the list of contact recommendations, which turned out to be much smaller.

Since THE FIRM's current working method is based on employees' experience and heuristics, it is unclear whether it is better or worse than a model based on purely random selection of insurants to reacquire. If the current method is worse than purely random selection, then the proposed Markov-based model, although better than the

Damage prevention and infliction — current practice versus adjusted model.

<table><tr><td>Pd.</td><td>Records</td><td>Records to reacquire</td><td>Potential damage</td><td>Damage prevented – current</td><td>Damage prevented – model</td><td>Damage prevention gain (%)</td><td>Damage inflicted – current</td><td>Damage inflicted – model</td><td>Damage infliction gain (%)</td></tr><tr><td>7</td><td>103,887</td><td>6387</td><td>2802.54</td><td>821.51 (29%)</td><td>981.16 (35%)</td><td>19%</td><td>1525.70 (54%)</td><td>1366.06 (49%)</td><td>10%</td></tr><tr><td>8</td><td>111,270</td><td>7300</td><td>3890.69</td><td>1132.42 (29%)</td><td>1595.67 (41%)</td><td>41%</td><td>2557.90 (66%)</td><td>2094.65 (54%)</td><td>18%</td></tr><tr><td>9</td><td>111,241</td><td>8094</td><td>3559.59</td><td>2779.74 (78%)</td><td>4933.69 (139%)</td><td>77%</td><td>6119.73 (172%)</td><td>3965.77 (111%)</td><td>35%</td></tr><tr><td>10</td><td>111,310</td><td>10,669</td><td>2954.87</td><td>1589.81 (54%)</td><td>2936.25 (99%)</td><td>85%</td><td>2836.08 (96%)</td><td>1489.65 (50%)</td><td>47%</td></tr></table>

Please cite this article as: Y. Zak, A. Even, Development and evaluation of a continuous-time Markov chain model for detecting and handling data currency declines, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.09.006

Y. Zak, A. Even / Decision Support Systems xxx (2017) xxx–xxx

Table 5  
Damage prevention and infliction — current practice versus random selection.

<table><tr><td>Pd.</td><td>Records</td><td>Records to reacquire</td><td>Potential damage</td><td>Damage prevented – current</td><td>Damage prevented – random</td><td>Damage prevention gain (%)</td><td>Damage inflicted – current</td><td>Damage inflicted – random</td><td>Damage infliction gain (%)</td></tr><tr><td>7</td><td>103,909</td><td>6402</td><td>12,396.31</td><td>821.51 (7%)</td><td>1452.36 (12%)</td><td>77%</td><td>22,921.33 (185%)</td><td>22,290.48 (180%)</td><td>3%</td></tr><tr><td>8</td><td>111,292</td><td>7324</td><td>15,602.61</td><td>1132.42 (7%)</td><td>1895.91 (12%)</td><td>67%</td><td>27,267.93 (175%)</td><td>26,504.44 (170%)</td><td>3%</td></tr><tr><td>9</td><td>111,263</td><td>8106</td><td>15,552.74</td><td>2779.74 (18%)</td><td>1672.07 (11%)</td><td>-40%</td><td>19,870.1 (128%)</td><td>20,977.76 (135%)</td><td>-6%</td></tr><tr><td>10</td><td>111,332</td><td>12,609</td><td>14,469.79</td><td>1589.81 (11%)</td><td>2224.41 (15%)</td><td>40%</td><td>21,468.35 (148%)</td><td>20,833.75 (144%)</td><td>3%</td></tr></table>

current working method, may be no better than the random selection model. Hence the need for a comparison against the performance of random selection.

The evaluation of random selection followed a similar procedure. For each period, the comparison was based on generating a random list of the same number of insurants to be reacquired (using the built-in R function ‘sample’), and the actual damage associated with insurants that were actually not reacquired was assessed, based on past performance. Table 5 summarizes the results of the comparison between the random selection model and the current working method (not considering the decay extension). In the earlier comparison of the current working method and the Markov-based model (Table 3), the Markovbased model was shown to outperform the current working method. When adding the comparison to the random selection model (Table 5), the random selection model outperforms the current working method in 3 out of 4 periods (#7, #8 and #10).

Table 6 summarizes the comparison between the random selection model and the proposed Markov-based model, showing that in all periods, the latter outperforms the former substantially.

A comparison that considers the decay extension is based on generating a random list of insurants with an age of 547 days or less. The results summarized in Table 7 show that, in this case, the current working practice is better than random selection. Since the Markov-based model outperforms the current practice (Table 6), it outperforms the random selection as well.

## 4.3. Discussion

Overall, the evaluation results were encouraging. At all evaluation stages, the model generally recommended a better list of insurants to contact, and the damage prevention performance associated with the proposed model was substantially higher than the performances associated with current work practices. Evaluation against random selection of insurants reinforced these results. However, some limitations of that evaluation must be acknowledged, and could be addressed in future research.

The first limitation is that the model relies on the assumption that data reacquisition aims to reflect the current state, without interfering with the natural course of real-world transitions. In practice, when contacting insurants, FIRM representatives often take actions that may influence insurants' behavior (e.g., urging insurants to expedite the submission of their paperwork). By that, the act of data reacquisition does not only update the record to reflect the real-world state, but also influences actual real-world behavior and transitions in the associated data records.

The second limitation is that the model assumes memory-less and exponentially distributed transition times. Our preliminary evaluation of the dataset supported these assumptions only to a limited extent. Future extensions of this study may consider relaxing some of the preliminary assumptions and exploring other distributions, with a view toward enhancing the model's performance.

The third limitation is that the model observed a single target variable per record, and so did the evaluation. However, data records contain additional attributes that may provide further information which is important for understanding the context under which transitions occur (e.g., insurants' demographics, their professional background, or the method of data collection). Future extensions may incorporate such context attributes, potentially enhancing and refining the model.

Despite these limitations, the model was still able to drive a major performance improvement. FIRM managers that were involved in the evaluation process expressed satisfaction with the model outcomes, and intend to consider integrating the model into the information systems that support their claim-handling processes, possibly with some extensions and adaptations.

## 5. Conclusions

Organizations increasingly rely on data resources for running their ongoing operations, analyzing environmental behaviors and trends, and supporting managerial decisions. As a result, the potential damage of DQ defects is on the rise, and so is the need for robust and economically sound DQ management. This study contributes to that end by developing and evaluating analytical solutions for supporting key DQ management tasks – estimating data quality levels, predicting quality decline, assessing the costs and benefits associated with correcting flawed data and, accordingly, optimizing data auditing and reacquisition policies. The proposed solutions are based on a CTMC model that captures and reflects common mechanisms that underlie currency declines. Their applicability was assessed through comprehensive evaluation of a large dataset that reflects a real-world data-management scenario. The evaluation highlights the potential contributions of the proposed solutions, improving the cost-effectiveness of data acquisition and maintenance policies and reducing the damage associated with the use of flawed data.

Some limitations of the CTMC model and the proposed solutions that were derived from it must be acknowledged, and should be addressed in future extensions to this study.

• The solutions target data attributes with a finite number of states and continuous transition time, such as the one evaluated in this study. However, other Markov chain extensions address a continuous

Damage prevention and infliction — random selection versus Markov-based model

<table><tr><td>Pd.</td><td>Records</td><td>Records to reacquire</td><td>Potential damage</td><td>Damage prevented - random</td><td>Damage prevented - model</td><td>Damage prevention gain (%)</td><td>Damage inflicted - random</td><td>Damage inflicted - model</td><td>Damage infliction gain (%)</td></tr><tr><td>7</td><td>103,909</td><td>6402</td><td>12,396.31</td><td>1452.36 (12%)</td><td>5171.6 (42%)</td><td>256%</td><td>22,290.48 (180%)</td><td>18,571.24 (150%)</td><td>17%</td></tr><tr><td>8</td><td>111,292</td><td>7324</td><td>15,602.61</td><td>1895.91 (12%)</td><td>9974.2 (64%)</td><td>426%</td><td>26,504.44 (170%)</td><td>18,426.16 (118%)</td><td>30%</td></tr><tr><td>9</td><td>111,263</td><td>8106</td><td>15,552.74</td><td>1672.07 (11%)</td><td>10,656.29 (69%)</td><td>537%</td><td>20,977.76 (135%)</td><td>11,993.55 (77%)</td><td>43%</td></tr><tr><td>10</td><td>111,332</td><td>12,609</td><td>14,469.79</td><td>2224.41 (15%)</td><td>17,606.8 (122%)</td><td>692%</td><td>20,833.75 (144%)</td><td>5451.36 (38%)</td><td>74%</td></tr></table>

Please cite this article as: Y. Zak, A. Even, Development and evaluation of a continuous-time Markov chain model for detecting and handling data currency declines, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.09.006

Table 7  
Damage prevention and infliction — current practice versus random selection (considering decay).

<table><tr><td>Pd.</td><td>Records</td><td>Records to reacquire</td><td>Potential damage</td><td>Damage prevented – current</td><td>Damage prevented – random</td><td>Damage prevention gain (%)</td><td>Damage inflicted – current</td><td>Damage inflicted – random</td><td>Damage infliction gain (%)</td></tr><tr><td>7</td><td>103,887</td><td>6387</td><td>12,396.31</td><td>821.51 (29%)</td><td>366.5963 (13%)</td><td>-55%</td><td>1525.7 (54%)</td><td>1980.617 (71%)</td><td>-30%</td></tr><tr><td>8</td><td>111,270</td><td>7300</td><td>15,602.61</td><td>1132.42 (29%)</td><td>616.0122 (16%)</td><td>-46%</td><td>2557.9 (66%)</td><td>3074.308 (79%)</td><td>-20%</td></tr><tr><td>9</td><td>111,241</td><td>8094</td><td>15,552.74</td><td>2779.74 (78%)</td><td>1144.9231 (32%)</td><td>-59%</td><td>6119.73 (172%)</td><td>7754.542 (218%)</td><td>-27%</td></tr><tr><td>10</td><td>111,310</td><td>10,669</td><td>14,469.79</td><td>1589.81 (54%)</td><td>423.7577 (14%)</td><td>-73%</td><td>2836.08 (96%)</td><td>4002.134 (135%)</td><td>-41%</td></tr></table>

range of states [21], and such extensions could be further explored as a possible basis for solutions supporting variables with continuousrange value domains.

• The solutions assume that the data has been recorded correctly at the time of acquisition. While this assumption was reasonable within the real-world scenario that was evaluated, there are obviously other scenarios in which there is a high likelihood of erroneous data acquisition. Future extensions may choose to address this issue, for example, by modeling correctness at the time of acquisition in probabilistic terms, i.e., defining parameters that reflect the likelihood of error during acquisition, and enhancing the model formulation accordingly.

• The of cost–benefit assessment, which underlies the recommended reacquisition timing (Eqs. (8)–(10)), was based on a certain formulation of the expected cost and damage. Similar formulations were also introduced in previous studies (e.g., [6,16,17]). However, other realworld settings may imply different damage behavior; hence, future model adjustments will be required to support other formulations.

• The evaluation settings did not permit detection of multiple state transitions between two data reacquisition points, and hence mandated the assumption of a single state transition at the most. Within this specific setting this assumption was reasonable, and has not biased the results substantially. However, the possibility of multiple transitions clearly exists; hence, future extensions to the model should address the possibility of multiple transitions as well.

Another inherent limitation that must be acknowledged is our evaluation of the model within a specific real-world business setting. However, we suggest that beyond this specific setting, a similar modeling approach can potentially benefit a broader range of data-management scenarios, in which repeated data auditing and reacquisition may involve major cost–benefit tradeoffs. For example, monitoring a medical condition and tracking patients' progress often requires repeated examinations. While offering some benefits, such examinations are often expensive and time-consuming; hence the need for setting cost-effective policies regarding their necessity and timing. Soil sampling, as another example, supports important decisions in the agricultural domain – irrigation, fertilizing, crop planning, and others. The process of taking samples and evaluating them in dedicated laboratories is often expensive and involves substantial manual effort, hence the need for evaluating costs and benefits and setting optimal sampling policies. Obviously, the model will require some enhancements and adaptations to fit a broader range of business domains and data-management scenarios.

Finally, setting optimal DQ maintenance policies following the prediction of a potential hazard, as demonstrated in this study, highlights the need for a shift from a reactive toward a proactive and prescriptive approach to DQ management, and from a focus on measuring past behaviors toward prediction of potential DQ hazards and, accordingly, setting policies and defining actions that must be taken to prevent future defects. In line with the approach taken in this study, proactive DQ management is likely to require an in-depth understanding of the mechanisms and the dynamics behind the formation and the evolution of DQ defects, as well as linking DQ maintenance policies to the assessment of potential benefits and costs that depend on the context of data usage. It would be reasonable to assume that in many datamanagement scenarios the prediction and prevention of DQ defects would be more cost-effective than attempting to detect and correct DQ defects that have already occurred; hence the motivation to further develop and explore proactive solutions.

## Acknowledgements

We would like to express our gratitude to Prof. Nava Pliskin from the Department of Industrial Engineering and Management at Ben-Gurion University of the Negev for her immense support and contribution to our research.

## Appendix A

With respect to the formulation of the adjusted damage function $D _ { i } ^ { * } ( t )$ in Eqs. (9) and (10), it can be shown that in cases where $d _ { i j } ( t )$ is a constant for each [i], [j] and (t), it would be possible to determine whether or not there exists a $t _ { i } ^ { C O N } { > } 0$ such that $D _ { i } ^ { * } ( t )$ is concave within the time interval [0, $t _ { i } ^ { C O N } ]$ , and calculate it if it exists. As this proposition holds regardless of the state in which a certain record currently resides, the [i] index will be omitted going forward, for the sake of simplified notation. Furthermore, $t _ { i } ^ { C O N }$ is relevant only for the exponential part of the decay function N(t) in Eq. (10), which, as depicted Fig. 2a, starts at $\overline { { t } } ^ { O P T }$ Considering the memory-less property of the exponential distribution, $\overline { { t } } ^ { O P I }$ can be therefore set to 0. Accordingly, the decay function is denoted as $N ( t ) = \exp ( - \gamma t )$

Assuming constant {d<sub>j</sub>}, the aggregated potential damage can be expressed as a weighted sum of exponential expressions: $\begin{array} { r } { D ( t ) = \sum _ { j = 1 \ldots N } ( P _ { j } \cdot d _ { j } ( 1 - \exp ( - \lambda _ { j } t ) ) ) = \sum _ { j = 1 \ldots N } D _ { j } ( t ) , } \end{array}$

The adjusted component that reflects target state [j] can be expressed by:

$$
D _ {j} ^ {*} (t) = D _ {j} (t) \cdot N (t) = P _ {j} \cdot d _ {j} \cdot \left(\exp (- \gamma t) - \exp \left(- (\gamma + \lambda_ {j}) t\right)\right)
$$

The second derivative of D<sup>∗</sup>(t) can be shown to be:

$$
\left(D _ {j} ^ {*} (t)\right) ^ {\prime \prime} = P _ {j} \cdot d _ {j} \cdot \left[ \gamma^ {2} e x p (- \gamma t) - (\gamma + \lambda_ {j}) ^ {2} e x p (- (\gamma + \lambda_ {j}) t) \right]
$$

The upper range of concavity $t _ { j } ^ { C O N }$ for the $D _ { j } ^ { * } ( t )$ component can be calculated by solving $( D _ { j } ^ { * } ( t _ { j } ^ { C O N } ) ) ^ { \prime \prime } { < } 0$ , It can be shown that a solution to this equation yields $t _ { j } ^ { C O N } \leq$ ln $\big ( \big ( \frac { ( \gamma + \lambda _ { j } ) ^ { 2 } } { \gamma ^ { 2 } } \big ) ^ { \frac { 1 } { \lambda _ { j } } } \big )$ . If a positive solution exists, then $D _ { j } ^ { * } ( t )$ is concave within the range of $0 \leq t \leq t _ { j } ^ { C O N } ,$

Since D<sup>∗</sup>(t) is expressed as a sum of $D _ { j } ^ { * } ( t ) ,$ , its second derivative can also be expressed as a sum: $\begin{array} { r } { ( D ^ { * } ( t ) ) ^ { \prime \prime } { = } \tilde { \sum } _ { j { = 1 \ldots N } } ( D _ { j } ^ { * } ( t ) ) ^ { \prime \prime } . D ^ { * } ( t ) } \end{array}$ would therefore be concave within the range of 0≤t≤ $t ^ { C O N }$ , if there exists a positive $t ^ { C O N }$ that solves $\begin{array} { r } { \sum _ { j = 1 \dots N } ( D _ { j } ^ { * } ( t ^ { C O N } ) ) ^ { \prime \prime } { \le } 0 } \end{array}$ . This equation can be solved numerically, and $\bar { t } ^ { C O N } \substack {  \infty }$ implies that $D ^ { * } ( t )$ is concave within any non-negative time range.

## References

[1] S.F. Madnick, R.Y, Wang. Y.E. Lee, H. Zhu, Overview and framework for data and information quality research, ACM J. Data Inf. Qual. 1 (1) (2009) 2–22 (Article 2).

[2] L.L. Pipino, Y.W. Lee, R.Y. Wang, Data quality assessment, Commun. ACM 45 (4) (2002) 211-218

[3] A. Even, G. Shankaranarayanan, Utility-driven assessment of data quality, ACM SIGMIS Database 38 (2) (2007) 75–93.

[4] B. Heinrich, M. Klier, Metric-based data quality assessment—developing and evaluating a probability-based currency metric, Decis. Support. Syst. 72 (2015) 82–96.

[5] C. Cappiello, C. Francalanci, B. Pernici, Time-related factors of data quality in multichannel information systems, J. Manag. Inf. Syst. 20 (3) (2003) 71–92.

[6] B. Heinrich, M. Klier, M. Kaiser, A procedure to develop metrics for currency and its application in CRM, J. Data Inf. Qual. (JDIQ) 1 (1) (2009) 5

[7] A. Even, G. Shankaranarayanan, P.D. Berger, Evaluating a model for cost-effective data quality management in a real-world CRM setting, Decis. Support. Syst. 50 (1) (2010) 152–163.

[8] B. Heinrich, D. Hristova, A quantitative approach for modelling the influence of currency of information on decision-making under uncertainty, J. Decis. Syst. 25 (1) (2016) 16–41.

[9] A. Wechsler, A. Even, Assessing accuracy degradation over time with A Markov-Chain model, The 17th International Conference on Information Quality (ICIQ), Paris, France, 2012.

[10] W. Zong, Feng Wu, Z. Jiang, A Markov-based update policy for constantly changing database systems, IEEE Trans. Eng. Manag. (2017) 1–14 Forthcoming.

[11] A. Even, G. Shankaranarayanan, Dual assessment of data quality in customer databases, J. Data Inf. Qual. (JDIQ) 1 (3) (2009) 15.

[12] S. Watts, G. Shankaranarayanan, A. Even, Data quality assessment in context: a cognitive perspective, Decis. Support. Syst. 48 (1) (2009) 202–211.

[13] A. Haug, F. Zachariassen, D. Van Liempd, The costs of poor data quality, J. Ind. Eng Manag. 4 (2) (2011) 168–193.

[14] C.W. Fisher, E.J. Lauria, C.C. Matheus, An accuracy metric: percentages, randomness, and probabilities, J. Data Inf. Qual. (JDIQ) 1 (3) (2009) 16.

[15] J. Cho, H. Garcia-Molina, Estimating frequency of change, ACM Trans. Internet Technol. 3 (3) (2003) 256–290.

[16] S. Razniewski, W. Nutt, Long-term optimization of update frequencies for decaying information, Paper Presented at the Proc. of the 18th Intl. Workshop on Web and DBs 2015, pp. 34–40.

[17] A. Even, G. Shankaranarayanan, P.D. Berger, Managing the quality of marketing data: cost/benefit tradeoffs and optimal configuration, J. Int. Mark. 24 (3) (2010) 209–221.

[18] B. Heinrich, M. Klier, Assessing data currency—a probabilistic approach, J. Inf. Sci. 37 (1) (2011) 86–100.

[19] A. Abdellatif, A.B. Ammar, C. Mazlout, Markov chain for the recommendation of materialized views in real-time data warehouse, Int. J. Comput. Sci. Eng. Appl. 4 (6) (2014) 13.

[20] J.D.C. Little, Models and managers: the concept of a decision calculus, Manag. Sci. 16 (8) (1970) B-466–B-485, https://doi.org/10.1287/mnsc.1040.0267.

[21] S.M. Ross, Stochastic processes, 2nd Edition ed. United States of America, Wiley, New York. 1996.

Yuval Zak received respectively in 2015 and 2016 his B.Sc. and M.Sc. degrees from the Department of Industrial Engineering and Management at Ben-Gurion University of the Neg ev (BGU) in Israel. He is currently studying for a doctoral degree at the department, conducting research under the Machine Learning and Business Intelligence Systems (MLBIS) Research Laboratory. His current interests include business intelligence and analytics, machine learning, and data quality management.

Adir Even is a faculty member of the Department of Industrial Engineering and Management at Ben-Gurion University of the Negev in Israel. He currently explores contribution of data repositories and information systems to business value and profitability, studying implications for system design, data warehousing, business intelligence, and data quality management. His research has been published in such journals as DSS, IEEE/TDKE, CACM, Database, and Information & Management. Prior to acquiring a DBA degree from Boston University School of Management, he gained substantial industry experience as a senior software-development manager in business intelligence and data warehousing projects

Please cite this article as: Y. Zak, A. Even, Development and evaluation of a continuous-time Markov chain model for detecting and handling data currency declines, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.09.006

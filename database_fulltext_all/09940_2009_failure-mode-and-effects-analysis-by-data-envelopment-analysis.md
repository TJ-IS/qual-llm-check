---
otero_id: 9940
otero_key: "C78MSGZ7"
title: "Failure mode and effects analysis by data envelopment analysis"
authors: "Kwai-Sang Chin; Ying-Ming Wang; Gary Ka Kwai Poon; Jian-Bo Yang"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.08.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Failure mode and effects analysis by data envelopment analysis

Kwai-Sang Chin <sup>a</sup>, Ying-Ming Wang <sup>a,b,</sup>⁎, Gary Ka Kwai Poon <sup>a</sup>, Jian-Bo Yang <sup>c</sup>

<sup>a</sup> Department of Manufacturing Engineering and Engineering Management, City University of Hong Kong, 83 Tat Chee Avenue, Kowloon Tong, Hong Kong <sup>b</sup> School of Public Administration, Fuzhou University, Fuzhou 350002, PR China

<sup>c</sup> Manchester Business School, The University of Manchester, Manchester M15 6PB, UK

## a r t i c l e i n f o

Article history: Received 15 December 2008 Received in revised form 31 July 2009 Accepted 30 August 2009 Available online 6 September 2009

Keywords: Failure mode and effects analysis Data envelopment analysis Overall risks Risk priority ranking

## a b s t r a c t

Failure mode and effects analysis (FMEA) is a method that examines potential failures in products or processes and has been used in many quality management systems. One important issue of FMEA is the determination of the risk priorities of failure modes. In this paper we propose an FMEA which uses data envelopment analysis (DEA), a well-known performance measurement tool, to determine the risk priorities of failure modes. The proposed FMEA measures the maximum and minimum risks of each failure mode. The two risks are then geometrically averaged to measure the overall risks of failure modes. The risk priorities are determined in terms of overall risks rather than maximum or minimum risks only. Two numerical examples are provided and examined using the proposed FMEA to show its potential applications and bene<sup>fi</sup>ts.

© 2009 Elsevier B.V. All rights reserved

## 1. Introduction

Failure mode and effects analysis (FMEA) is an engineering technique used to de<sup>fi</sup>ne, identify and eliminate known and/or potential failures, problems, and errors from the system, design, process, and/or service before they reach the customer [29]. It is also referred to as failure mode, effects and criticality analysis (FMECA) when used for a criticality analysis. When applying FMEA, a crossfunctional and multidisciplinary team identi<sup>fi</sup>es failure modes, evaluates their risks and prioritizes them so that appropriate corrective actions can be taken. A failure mode is de<sup>fi</sup>ned as the manner in which a component, subsystem, system, process, etc. could potentially fail to meet the design intent. A failure mode in one component can serve as the cause of a failure mode in another component. A failure cause is de<sup>fi</sup>ned as a design weakness that may result in a failure. For each failure mode identi<sup>fi</sup>ed, the FMEA team should determine what the ultimate effect of failure will be. A failure effect is de<sup>fi</sup>ned as the result of a failure mode on the function of the product or process as perceived by the customer. The traditional FMEA determines the risk priorities of failure modes through the risk priority number (RPN), which is determined by

$$
R P N = O \times S \times D,\tag{1}
$$

where the risk factors O and S are occurrence and severity of a failure, and D is the ability to detect the failure before it reaches the customer. The three risk factors are evaluated using the ratings (also called ranks or scores) from 1 to 10, as described in Tables 1–3. Failures with higher RPNs are viewed to be more important and should be given greater considerations.

FMEA proves to be one of the most important early preventative actions in system, design, process, or service which will prevent failures and errors from occurring and reaching the customer [29]. However, the RPN has been criticized for a variety of reasons [1,3,6,9,17,25,27], some of which are listed as follows:

• Different combinations of O, S and D may produce exactly the same value of RPN, but their hidden risk implications may be totally different. For example, two different events with the values of 2, 3, 2 and 4, 1, 3 for O, S and D, respectively, have the same RPN value of 12. However, the hidden risk implications of the two events may not necessarily be the same. This may cause a waste of resources and time, and in some cases a high risk event may go noticed.

• The relative importance among O, S and D is not taken into consideration. The three risk factors are assumed to be equally important. This may not be the case when considering a practical application of FMEA.

• The mathematical formula for calculating RPN is questionable and debatable. There is no rationale as to why O, S and D should be multiplied to produce the RPN.

• The three risk factors are dif<sup>fi</sup>cult to be precisely evaluated.

• RPNs are not continuous with many holes and heavily distributed at the bottom of the scale from 1 to 1000. This causes problems in interpreting the meaning of the differences between different RPNs. For example, is the difference between 1 and 2 the same as or less than the difference between 900 and 1000?

To overcome the drawbacks listed above, a number of approaches have been suggested in the literature. For example, Bevilacqua et al.

Table 1  
Traditional ratings for occurrence of a failure [3,27,35].

<table><tr><td>Rating</td><td>Probability of occurrence</td><td>Failure probability</td></tr><tr><td>10</td><td>Very high: failure is almost inevitable</td><td>&gt;1 in 2</td></tr><tr><td>9</td><td></td><td>1 in 3</td></tr><tr><td>8</td><td>High: repeated failures</td><td>1 in 8</td></tr><tr><td>7</td><td></td><td>1 in 20</td></tr><tr><td>6</td><td>Moderate: occasional failures</td><td>1 in 80</td></tr><tr><td>5</td><td></td><td>1 in 400</td></tr><tr><td>4</td><td></td><td>1 in 2000</td></tr><tr><td>3</td><td>Low: relatively few failures</td><td>1 in 15,000</td></tr><tr><td>2</td><td></td><td>1 in 150,000</td></tr><tr><td>1</td><td>Remote: failure is unlikely</td><td>&lt;1 in 1,500,000</td></tr></table>

[2] de<sup>fi</sup>ned RPN as the weighted sum of six parameters (safety, machine importance for the process, maintenance costs, failure frequency, downtime length, and operating conditions) multiplied by a seventh factor (machines access dif<sup>fi</sup>culty), where the relative importance of the six attributes was estimated using pairwise comparisons.

Sankar and Prabhu [27] presented a modi<sup>fi</sup>ed approach for prioritization of failures in a system FMEA, which used the ranks 1 through 1000, called risk priority ranks (RPRs), to represent the increasing risk of the 1000 possible severity–occurrence–detection combinations. These 1000 possible combinations were tabulated by an expert in the order of increasing risk and can be interpreted as ‘if– then’ rules. The failure having a higher rank was given a higher priority.

Braglia [5] proposed a multi-attribute failure mode analysis (MAFMA) based on the analytic hierarchy process (AHP) technique. The proposed MAFMA viewed the risk factors (O, S, D, and expected cost) as decision attributes, causes of failure as decision alternatives, and the selection of cause of failure as decision goal, which together with the attributes and alternatives formed a three-level hierarchical structure. Pairwise comparison matrices were used to estimate the weights of attributes and local priorities of the causes with respect to the expected cost attribute. The conventional ratings for O, S and D were normalized as the local priorities of the causes with respect to O, S, and D, respectively, and the weight aggregation technique in the AHP was used to synthesize the local priorities into global priorities, based on which the possible causes of failure were ranked.

Braglia et al. [7] also proposed an alternative multi-attribute decision-making approach, called fuzzy TOPSIS approach for FMECA, which is a fuzzy version of the technique for order preference by similarity to ideal solution (TOPSIS). The TOPSIS method is a wellknown multi-attribute decision-making methodology based on the assumption that the best decision alternative should be as close as possible to the ideal solution and the farthest from the negative-ideal solution. The proposed fuzzy TOPSIS approach allows the risk factors O, S, and D and their relative importance to be assessed using triangular fuzzy numbers.

Table 2  
Traditional ratings for severity of a failure [3,27,35].

<table><tr><td>Rating</td><td>Effect</td><td>Severity of effect</td></tr><tr><td>10</td><td>Hazardous without warning</td><td>Very high severity ranking when a potential failure mode effects safe system operation without warning</td></tr><tr><td>9</td><td>Hazardous with warning</td><td>Very high severity ranking when a potential failure mode affects safe system operation with warning</td></tr><tr><td>8</td><td>Very high</td><td>System inoperable with destructive failure without compromising safety</td></tr><tr><td>7</td><td>High</td><td>System inoperable with equipment damage</td></tr><tr><td>6</td><td>Moderate</td><td>System inoperable with minor damage</td></tr><tr><td>5</td><td>Low</td><td>System inoperable without damage</td></tr><tr><td>4</td><td>Very low</td><td>System operable with significant degradation of performance</td></tr><tr><td>3</td><td>Minor</td><td>System operable with some degradation of performance</td></tr><tr><td>2</td><td>Very minor</td><td>System operable with minimal interference</td></tr><tr><td>1</td><td>None</td><td>No effect</td></tr></table>

Table 3  
Traditional ratings for detection [3,27,35].

<table><tr><td>Rating</td><td>Detection</td><td>Likelihood of detection by design control</td></tr><tr><td>10</td><td>Absolute uncertainty</td><td>Design control cannot detect potential cause/mechanism and subsequent failure mode</td></tr><tr><td>9</td><td>Very remote</td><td>Very remote chance the design control will detect potential cause/mechanism and subsequent failure mode</td></tr><tr><td>8</td><td>Remote</td><td>Remote chance the design control will detect potential cause/mechanism and subsequent failure mode</td></tr><tr><td>7</td><td>Very low</td><td>Very low chance the design control will detect potential cause/mechanism and subsequent failure mode</td></tr><tr><td>6</td><td>Low</td><td>Low chance the design control will detect potential cause/mechanism and subsequent failure mode</td></tr><tr><td>5</td><td>Moderate</td><td>Moderate chance the design control will detect potential cause/mechanism and subsequent failure mode</td></tr><tr><td>4</td><td>Moderately high</td><td>Moderately high chance the design control will detect potential cause/mechanism and subsequent failure mode</td></tr><tr><td>3</td><td>High</td><td>High chance the design control will detect potential cause/mechanism and subsequent failure mode</td></tr><tr><td>2</td><td>Very high</td><td>Very high chance the design control will detect potential cause/mechanism and subsequent failure mode</td></tr><tr><td>1</td><td>Almost certain</td><td>Design control will detect potential cause/mechanism and subsequent failure mode</td></tr></table>

Chang et al. [8] utilized grey theory for FMEA. They used fuzzy linguistic terms such as Very Low, Low, Moderate, High and Very High to evaluate the degrees of O, S and D, and grey relational analysis to determine the risk priorities of potential causes. To carry out the grey relational analysis, fuzzy linguistic terms were defuzzi<sup>fi</sup>ed as crisp values, the lowest levels of the three factors O, S and D were de<sup>fi</sup>ned as a standard series, and the assessment information of the three factors for each potential cause was viewed as a comparative series, whose grey relational coef<sup>fi</sup>cients and grey relational degree with the standard series were computed in terms of the grey theory. Big grey relational degree means small effect of potential cause. In [9], they also utilized the grey theory for FMEA, but the grey relational degrees were computed using the traditional scores 1–10 for the three risk factors rather than fuzzy linguistic terms.

Bowles and Peláez [4] described a fuzzy logic based approach for prioritizing failures in a system FMEA, which uses linguistic terms to describe O, S, D, and the risks of failures. The relationships between the risks and O, S, D were characterized by fuzzy if–then rules extracted from expert knowledge and expertise. Crisp rankings for O, S, D were fuzzi<sup>fi</sup>ed to match the premise of each possible if–then rule. All the rules that have any truth in their premises were <sup>fi</sup>red to contribute to a fuzzy conclusion. The fuzzy conclusion was then defuzzi<sup>fi</sup>ed by the weighted mean of maximum method (WMoM) as the ranking value of the risk priority. Similar fuzzy inference methods also appeared in [6,12,18,19,24,25,30].

Yang et al. [36] presented a novel, ef<sup>fi</sup>cient fuzzy rule-based Bayesian reasoning (FuRBaR) approach for prioritizing failures in FMEA. The technique was speci<sup>fi</sup>cally developed to deal with some of the drawbacks concerning the use of conventional fuzzy logic (i.e. rule-based) methods in FMEA. In their approach, subjective belief degrees were assigned to the consequent part of the rules to model the incompleteness encountered in establishing the knowledge base. A Bayesian reasoning mechanism was then used to aggregate all relevant rules for assessing and prioritizing potential failure modes. The applicability of the proposed approach was demonstrated by studying a maritime collision risk due to technical failures.

Recently, Chin et al. [13] proposed an FMEA using the group-based evidential reasoning (ER) approach to capture FMEA team members' diversity opinions and prioritize failure modes under different types of uncertainties such as incomplete assessment, ignorance and intervals. The risk priority model was developed using the groupbased ER approach, which includes assessing risk factors using belief structures, synthesizing individual belief structures into group belief structures, aggregating the group belief structures into overall belief structures, converting the overall belief structures into expected risk scores, and ranking the expected risk scores using the minimax regret approach (MRA). Similar applications for risk analysis on dynamic alliance can also be found in [21].

In spite of the fact that much effort has been paid to the improvement of RPN, the improved methods either need to specify or determine the weights of risk factors in advance or take no account of them at all. It is argued that the speci<sup>fi</sup>cation or determination of risk factor weights is not easy because different decision makers (DMs) may have distinct judgments or preferences. For example, Pillay and Wang [25] gave more emphasis on the risk factor D followed by S and less weight to O; while Braglia et al. [7] observed that a failure cause with a very high severity value but a very remote occurrence probability might be less critical than a failure cause which occurs repeatedly and therefore considered the chance of failure more important than the other factors. Obviously, the above authors' opinions are in con<sup>fl</sup>ict with each other.

Another reason why risk factor weights are not easy to determine is that different failure modes have different consequences. The speci<sup>fi</sup>cation or determination of a <sup>fi</sup>xed set of risk factor weights for all the failure modes might be inappropriate, particularly in the case with a large number of failure modes. In other words, it might be a better choice to use different sets of risk factor weights for different failure modes when there are a large number of failure modes to be prioritized. In this aspect, Garcia et al. [16] proposed a fuzzy data envelopment analysis (DEA) approach for FMEA, which does not require specifying or determining risk factor weights subjectively. Their approach, however, was computationally very complicated and also could not produce a full ranking for the failure modes to be prioritized.

Based on the above analyses, we propose in this paper a new FMEA, which utilizes DEA, a well-known performance measurement tool, to determine the risk priorities of failure modes. The proposed FMEA takes into account the relative importance weights of risk factors, but has no need to specify or determine them subjectively, which are determined by DEA models. The weights determined by DEA models differ from one failure mode to another. The new FMEA measures the maximum and minimum risks of failure modes, which are geometrically averaged to re<sup>fl</sup>ect the overall risks of the failure modes, based on which the failure modes can be prioritized. Incomplete and imprecise information on the evaluation of risk factors can also be considered in the FMEA.

The rest of the paper is organized as follows. In Section 2, we give a brief description of DEA and its main mathematical models for ef<sup>fi</sup>ciency measurement. In Section 3, we develop DEA models for FMEA. In Section 4, we discuss uncertainties such as incomplete and imprecise information related to FMEA and develop interval DEA models for prioritization of failure modes. Numerical examples are provided in Section 5 to demonstrate the potential applications of the proposed FMEA and its advantages. Section 6 concludes the paper with a brief summary.

## 2. DEA and DEA models for ef<sup>fi</sup>ciency measurement

DEA, i.e. data envelopment analysis, was originally developed by Charnes et al. [11] for measuring the relative ef<sup>fi</sup>ciencies of a group of decision-making units (DMUs) that utilize multiple inputs to produce multiple outputs. Since its development in the late 1970s, DEA has found surprising applications [14,15,20,22,33]. The traditional DEA models measure only the optimistic ef<sup>fi</sup>ciencies of DMUs. This usually leads to more than one DMU being evaluated as ef<sup>fi</sup>cient. The ef<sup>fi</sup>cient DMUs are dif<sup>fi</sup>cult to be discriminated from each other. Recently, Wang et al. [32] proposed the pessimistic ef<sup>fi</sup>ciency model that measures the pessimistic ef<sup>fi</sup>ciencies of DMUs and suggested a geometric average ef<sup>fi</sup>ciency, which is the integration of the optimistic and pessimistic ef<sup>fi</sup>ciencies of DMUs, as the overall ef<sup>fi</sup>ciency measure of DMUs. The geometric average ef<sup>fi</sup>ciency considers not only the optimistic ef<sup>fi</sup>ciencies of DMUs but also their pessimistic ef<sup>fi</sup>ciencies and is therefore more comprehensive and more convincing than both of them. By the geometric average ef<sup>fi</sup>ciency, all the DMUs can be fully ranked and discriminated. In what follows, we brie<sup>fl</sup>y review the two DEA models that measure the optimistic and pessimistic ef<sup>fi</sup>ciencies of DMUs, and the geometric average ef<sup>fi</sup>ciency.

## 2.1. Optimistic efficiency — the best relative efficiency

Assume that there are n DMUs to be evaluated in terms of m inputs and s outputs. Denote by $x _ { i j } ( i { = } 1 , { \ldots } , m )$ and $y _ { r j } \left( r { = } 1 , . . . , s \right)$ the input and output values of DMU $( j = 1 , . . . , ~ n )$ , which are known and nonnegative. The ef<sup>fi</sup>ciency of DMU is de<sup>fi</sup>ned as

$$
\theta_ {j} = \frac {\sum_ {r = 1} ^ {s} u _ {r} y _ {r j}}{\sum_ {i = 1} ^ {m} v _ {i} x _ {i j}},\tag{2}
$$

where $u _ { r }$ and $\nu _ { i }$ are the output and input weights assigned to the rth output and the ith input. To determine the ef<sup>fi</sup>ciency of $\mathrm { D M U } _ { j }$ relative to the other DMUs, Charnes et al. [11] developed the following wellknown CCR model, which was named by acronym and measures the best relative ef<sup>fi</sup>ciencies of DMUs:

$$
\begin{array}{l l} \text { Maximize } & \theta_ {0} = \frac {\sum_ {r = 1} ^ {s} u _ {r} y _ {r 0}}{\sum_ {i = 1} ^ {m} v _ {i} x _ {i 0}} \\ \text { Subject   to } & \theta_ {j} = \frac {\sum_ {r = 1} ^ {s} u _ {r} y _ {r j}}{\sum_ {i = 1} ^ {m} v _ {i} x _ {i j}} \leq 1,   j = 1,..., n, \\ & u _ {r}, v _ {i} \geq \varepsilon ,   r = 1,..., s;   i = 1,..., m, \end{array}\tag{3}
$$

where the subscript zero represents the DMU under evaluation, $u _ { r }$ and $\nu _ { i }$ are decision variables and ε is a very small positive number called non-Archimedean in<sup>fi</sup>nitesimal in the DEA literature. Through Charnes and Cooper's transformation [10], the above fractional programming is transformed into the following equivalent linear programming (LP) model:

Maximize

$$
\theta_ {0} = \sum_ {r = 1} ^ {s} u _ {r} y _ {r 0}
$$

$$
\begin{array}{l l} \text { Maximize } & s _ {0} = \sum_ {r = 1} u _ {r} y _ {r 0} \\ \text { Subject   to } & \sum_ {r = 1} ^ {s} u _ {r} y _ {r j} - \sum_ {i = 1} ^ {m} v _ {i} x _ {i j} \leq 0,   j = 1,..., n, \\ & \sum_ {i = 1} ^ {m} v _ {i} x _ {i 0} = 1, \\ & u _ {r}, v _ {i} \geq \varepsilon ,   r = 1,..., s;   i = 1,..., m. \end{array}\tag{4}
$$

If there exists a set of positive weights that makes ${ \boldsymbol { \theta } } _ { 0 } ^ { * } = 1$ , then DMU is referred to as optimistic ef<sup>fi</sup>cient; otherwise, it is referred to as optimistic inef<sup>fi</sup>cient. For n different DMUs, there are a total of n LP models to be solved. Accordingly, there are n sets of weights available, some of which may be different. All the optimistic ef<sup>fi</sup>cient DMUs determine an ef<sup>fi</sup>ciency frontier.

## 2.2. Pessimistic efficiency — the worst relative efficiency

Ef<sup>fi</sup>ciency is a relative measure and can be measured within different ranges. The CCR model measures the optimistic ef<sup>fi</sup>ciency of each DMU within the range of less than or equal to one. If the ef<sup>fi</sup>ciency of a DMU is measured within the range of no less than one, then we have the so-called pessimistic ef<sup>fi</sup>ciency, also referred to as the worst relative ef<sup>fi</sup>ciency. The pessimistic ef<sup>fi</sup>ciency of $\mathsf { D M U } _ { 0 }$ is measured by the following pessimistic DEA model [32]:

$$
\begin{array}{l l} \text {Minimize} & \psi_ {0} = \frac {\sum_ {r = 1} ^ {s} u _ {r} y _ {r 0}}{\sum_ {i = 1} ^ {m} v _ {i} x _ {i 0}} \\ \text {Subject to} & \psi_ {j} = \frac {\sum_ {r = 1} ^ {s} u _ {r} y _ {r j}}{\sum_ {i = 1} ^ {m} v _ {i} x _ {i j}} \geq 1,   j = 1,..., n, \\ & u _ {r}, v _ {i} \geq \varepsilon ,   r = 1,..., s; i = 1,..., m, \end{array}\tag{5}
$$

which can be further converted into the following equivalent LP model:

$$
\begin{array}{l l} \text {Minimize} & \psi_ {0} = \sum_ {r = 1} ^ {s} u _ {r} y _ {r 0} \\ \text {Subject to} & \sum_ {r = 1} ^ {s} u _ {r} y _ {r j} - \sum_ {i = 1} ^ {m} v _ {i} x _ {i j} \geq 0,   j = 1,..., n, \\ & \sum_ {i = 1} ^ {m} v _ {i} x _ {i 0} = 1, \\ & u _ {r}, v _ {i} \geq \varepsilon ,   r = 1,..., s; i = 1,..., m. \end{array}\tag{6}
$$

When there exists a set of positive weights making $\begin{array} { r } { \psi _ { 0 } ^ { * } = 1 , } \end{array}$ we refer to $\boldsymbol { \mathrm { D M U } } _ { 0 }$ as pessimistic inef<sup>fi</sup>cient; otherwise, DMU is referred to as pessimistic ef<sup>fi</sup>cient. All the pessimistic inef<sup>fi</sup>cient DMUs determine an inef<sup>fi</sup>ciency frontier.

According to the above de<sup>fi</sup>nitions, DMUs can be classi<sup>fi</sup>ed into three categories: optimistic ef<sup>fi</sup>cient, pessimistic inef<sup>fi</sup>cient, and those that are neither optimistic ef<sup>fi</sup>cient nor pessimistic inef<sup>fi</sup>cient. Obviously, optimistic inef<sup>fi</sup>cient units include pessimistic inef<sup>fi</sup>cient and part of pessimistic ef<sup>fi</sup>cient DMUs. As such, pessimistic ef<sup>fi</sup>cient units include optimistic ef<sup>fi</sup>cient and part of optimistic inef<sup>fi</sup>cient DMUs.

## 2.3. Geometric average efficiency — the overall efficiency measurement

It is a common knowledge that optimistic ef<sup>fi</sup>ciency and pessimistic ef<sup>fi</sup>ciency should form an interval when measured under the same constraints such as $\alpha \leq \sum _ { r = 1 } ^ { s } u _ { r } y _ { r j } / \sum _ { i = 1 } ^ { m } \nu _ { i } x _ { i j } \leq 1$ with $0 < \alpha <$ $\operatorname* { m i n } _ { j \in \{ 1 , \dots , n \} } \{ \boldsymbol { \Theta } _ { j } ^ { * } / \boldsymbol { \Psi } _ { j } ^ { * } \}$ and $j = 1 , . . . , \ n .$ The ef<sup>fi</sup>ciency interval of DMU <sup>f g</sup>could accordingly be expressed as $[ \alpha \psi _ { j } ^ { * } , \theta _ { j } ^ { * } ]$ if α value is small enough. To avoid the dif<sup>fi</sup>culty in determining the value of α, Wang et al. [32] suggested a geometric average ef<sup>fi</sup>ciency, determined by

$$
\phi_ {j} ^ {*} = \sqrt {\psi_ {j} ^ {*} \theta_ {j} ^ {*}}, j = 1, \dots , n,\tag{7}
$$

where $\boldsymbol { \theta } _ { j } ^ { * }$ and $\psi _ { j } ^ { * }$ are respectively the optimistic and pessimistic ef<sup>fi</sup>ciencies of DMU $( j = 1 , . . . , n )$ . The geometric average ef<sup>fi</sup>ciency considers not only the optimistic ef<sup>fi</sup>ciency of a DMU, but also its pessimistic ef<sup>fi</sup>ciency. It measures the overall ef<sup>fi</sup>ciency of a DMU and considers both sides of a coin. The integration of two extreme ef<sup>fi</sup>ciencies, optimistic and pessimistic, into a geometric average ef<sup>fi</sup>ciency is undoubtedly more meaningful and more comprehensive than the use of either of the two ef<sup>fi</sup>ciencies.

When ef<sup>fi</sup>ciency intervals $[ \alpha \psi _ { j } ^ { * } , \theta _ { j } ^ { * } ] ( j = 1 , . . . , n )$ are compared through their geometric midpoints $\sqrt { \alpha \psi _ { j } ^ { * } { \cdot } \theta _ { j } ^ { * } }$ , the rankings among the n DMUs depend only upon their geometric average ef<sup>fi</sup>ciencies $\boldsymbol { \Phi } _ { j } ^ { * } = \sqrt { \boldsymbol { \Psi } _ { j } ^ { * } \boldsymbol { \Theta } _ { j } ^ { * } } \left( j = 1 , . . . , n \right)$ and have nothing to do with the value of α. This is the reason why geometric average rather than arithmetic average or another average is used for ranking. This good property enables the decision maker (DM) not to worry about how to determine the value of α. He/She can therefore leave it alone and compare directly the geometric average ef<sup>fi</sup>ciencies of the n DMUs to determine their overall performances and rankings. Interested readers are referred to Wang et al. [32] for further theoretical justi<sup>fi</sup>cations on geometric average ef<sup>fi</sup>ciency.

## 3. DEA models for FMEA

Suppose there are n failure modes denoted by FM $( i = 1 , . . . , n )$ to be prioritized, each being evaluated against m risk factors denoted by $\mathrm { R F } _ { j } ( j = 1 , . . . , m )$ ). Let $r _ { i j } ( i { = } 1 , . . . , n ; j { = } 1 , . . . , m )$ be the ratings of FM on $\mathrm { R F } _ { j }$ and $w _ { j }$ be the weight of risk factor $\mathrm { R F } _ { j } ( j = 1 , . . . , m )$ . Since the RPN de<sup>fi</sup>ned as the product of three risk factors O, S and D has been largely criticized for its mathematical formula and equal treatment of the risk factors, we de<sup>fi</sup>ne in this paper the risks of failures with a different mathematical form, which can be either of the following:

$$
R _ {i} = \sum_ {j = 1} ^ {m} w _ {j} r _ {i j}, i = 1, \dots , n,\tag{8}
$$

$$
R _ {i} = \prod_ {j = 1} ^ {m} r _ {i j} ^ {w _ {j}}, i = 1, \dots , n.\tag{9}
$$

Eq. (8) de<sup>fi</sup>nes the risk of each failure mode as the weighted sum of m risk factors, whereas Eq. (9) as the weighted product of m risk factors. For convenience to distinguish between the two risks, we refer to the risk determined by Eq. (8) as additive risk and the risk by Eq. (9) as multiplicative risk, respectively. It is worthwhile to point out that the de<sup>fi</sup>nition for additive risks was <sup>fi</sup>rst proposed by Braglia et al. [6], who de<sup>fi</sup>ned the RPN as the weighted sum of O, S and D, whereas the de<sup>fi</sup>nition for multiplicative risks was <sup>fi</sup>rst proposed by Wang et al [34], who de<sup>fi</sup>ned the RPN as the fuzzy weighted geometric mean of the three risk factors O, S, and D, which they referred to as fuzzy risk priority number (FRPN). Both of the papers require the weights of the risk factors to be speci<sup>fi</sup>ed or determined subjectively, but in this paper the risk factor weights will be determined by DEA models automatically.

The traditional DEA often assigns too many zeros to input and output weights, leading to optimistic ef<sup>fi</sup>ciency being unreasonably high and pessimistic ef<sup>fi</sup>ciency being extraordinarily low. To avoid this from happening in FMEA, we consider imposing a constraint on the ratio of maximum weight to minimum weight. According to Saaty's AHP [26], the maximum value, as a ratio of the comparative importance of a criterion over another, can assume to be 9. We therefore constrain the ratio of maximum weight to minimum weight within the range of one and nine. That is

$$
1 \leq \frac {\max \{w _ {1} , \dots , w _ {m} \}}{\min \{w _ {1} , \dots , w _ {m} \}} \leq 9.\tag{10}
$$

The DM can also set a speci<sup>fi</sup>c but different upper bound for the ratio of maximum weight to minimum weight if necessary. The main reasons for us to set the maximum ratio as 9 are based on the following observations:

• The pairwise comparison matrices in the AHP are the most widely used approaches for estimating the relative importance weights of decision attributes or criteria, in which the maximum ratio scale between the importance of two attributes or criteria are usually not greater than 9.

• Risk factors O, S and D are all evaluated using the ratings between 1 and 10, where 1 represents no risk. Accordingly, their relative importance should also be evaluated using similar ratings. Due to the fact that “no importance” makes no sense, the ratings used for evaluating the relative importance of risk factors should therefore be de<sup>fi</sup>ned as 1–9 rather than 1–10. As a result, the maximum ratio between the importance of two risk factors is less than or equal to 9.

• Five-point Likert scale is also widely used in practice for measuring the relative importance of risk factors. We may conduct a sensitivity analysis to the risk priority ranking obtained under the maximum ratio scale of 9 to test the robustness of the ranking.

The left-hand-side of Eq. (10) is trivial and holds always. Its righthand-side is equivalent to the following:

$$
\max \left\{\frac {w _ {j}}{w _ {k}} | j, k = 1, \dots m; k \neq j \right\} \leq 9,\tag{11}
$$

which can be further rewritten as

$$
w _ {j} - 9 w _ {k} \leq 0, j, k = 1, \dots , m; k \neq j.\tag{12}
$$

According to the DEA models introduced in Section 2, we are now able to build FMEA models for measuring the maximum and minimum risks of each failure mode, as shown below:

$$
\begin{array}{l} R _ {0} ^ {\max} = \text { Maximize } R _ {0} \\ \text { Subject   to } \left\{ \begin{array}{l l} R _ {i} \leq 1, & i = 1,..., n, \\ w _ {j} - 9 w _ {k} \leq 0, & j, k = 1,..., m; k \neq j, \end{array} \right. \end{array}\tag{13}
$$

$$
\begin{array}{l} R _ {0} ^ {\min} = \text { Minimize } R _ {0} \\ \text { Subject   to } \left\{ \begin{array}{l l} R _ {i} \geq 1, & i = 1,..., n, \\ w _ {j} - 9 w _ {k} \leq 0, & j, k = 1,..., m; k \neq j, \end{array} \right. \end{array}\tag{14}
$$

where $R _ { 0 }$ is the risk of the failure mode under evaluation. The overall risk of each failure mode is de<sup>fi</sup>ned by Eq. (7) as the geometric average of the maximum and minimum risks of the failure mode. That is

$$
\overline {{R _ {i}}} = \sqrt {R _ {i} ^ {\max} \cdot R _ {i} ^ {\min}}, i = 1, \dots , n.\tag{15}
$$

This de<sup>fi</sup>nition enables us not to worry about how to determine an interval for the risk of each failure mode. The bigger the geometric average risk, the higher the risk priority. The n failure modes $\mathrm { F M } _ { i } ( i = 1 , . . . , n )$ can be easily prioritized by their geometric average risks $\overline { { R } } _ { i } ( i = 1 , . . . , n )$

The above models (13) and (14) are developed for additive risks. For multiplicative risks de<sup>fi</sup>ned by Eq. (9), the maximum and minimum risk models can be built in the same way, but the ratings and risks need to be transformed into logarithmic scales for linearity. The two models are constructed as follows:

$$
\mathrm{n} R _ {0} ^ {\max} = \text { Maximize } \ln R _ {0}\tag{16}
$$

$$
\text { Subject   to } \left\{ \begin{array}{l l} \ln R _ {i} \leq 1, & i = 1,..., n, \\ w _ {j} - 9 w _ {k} \leq 0, & j, k = 1,..., m; k \neq j, \end{array} \right.
$$

ln $R _ { 0 } ^ { \mathrm { { m i n } } } =$ Minimize ln $R _ { 0 }$

$$
\text { Subject   to } \left\{ \begin{array}{l l} \ln R _ {i} \geq 1, & i = 1,..., n, \\ w _ {j} - 9 w _ {k} \leq 0, & j, k = 1,..., m; k \neq j. \end{array} \right.\tag{17}
$$

Accordingly, the geometric average risk is de<sup>fi</sup>ned as

$$
\overline {{R _ {i}}} = \sqrt {E X P (\ln R _ {i} ^ {\max}) \cdot E X P (\ln R _ {i} ^ {\min})}, i = 1, \dots , n.\tag{18}
$$

where EXP(.) is the exponential function.

Through the solution of models (13) and (14) or (16) and (17) for each failure mode, the maximum and minimum risks of all the n failure modes can be obtained. Their geometric average risks can then be computed by using Eqs. (15) or (18), based on which the n failure modes can be prioritized.

## 4. Interval DEA models for FMEA

FMEA is a team function. Different FMEA team members may sometimes behave very differently and provide distinct assessment information, some of which may be incomplete or imprecise. For example, an FMEA team member may provide an interval rating for a risk factor such as 4–5 which refers to the rating between 4 and 5, or an incomplete distribution such as 4 at 40% and 5 at 50% which means the failure mode under evaluation is assessed to have a risk rating of 4 at 40% con<sup>fi</sup>dence and a risk rating of 5 at 50% con<sup>fi</sup>dence. Since the total con<sup>fi</sup>dence $4 0 \% + 5 0 \% = 9 0 \% < 1 0 0 \% ,$ the above assessment is said to be incomplete. The missing 10% (=100%–90%) con<sup>fi</sup>dence is called local ignorance in the terminology of Dempster–Shafer theory of evidence [28] and could be assigned to any rating between 1 and 10. The above incomplete assessment can be transformed into an expectation interval, whose lower and upper bound values are respectively computed as

$$
\begin{array}{l} 4 \times 40 \% + 5 \times 50 \% + 1 \times (100 \% - 40 \% - 50 \%) = 4.2, \\ 4 \times 40 \% + 5 \times 50 \% + 10 \times (100 \% - 40 \% - 50 \%) = 5.1. \end{array}
$$

As a result, the maximum, minimum and geometric average risks will also become intervals

Let $[ r _ { i j } ^ { L } , ~ r _ { i j } ^ { U } ]$ be the interval ratings of FM on $\operatorname { R F } _ { j } ,$ which are the weighted sum of individual expectation intervals of FMEA team members, namely,

$$
[ r _ {i j} ^ {L}, r _ {i j} ^ {U} ] = \sum_ {k = 1} ^ {K} \lambda_ {k} E (r _ {i j} ^ {(k)}), i = 1, \dots , n; j = 1, \dots , m,\tag{19}
$$

where $\lambda _ { k } \ ( k { = } 1 , . . . , K )$ are the relative importance weights of FMEA team members satisfying $\lambda _ { k } > 0$ and $\sum _ { k = 1 } ^ { K } \lambda _ { k } = 1$ , and $\overset { - } { E } ( r _ { i j } ^ { ( k ) } ) = [ r _ { i j k } ^ { L } ,$ $r _ { i j k } ^ { U } ]$ are the expectation intervals provided by K team members. In the case of interval ratings, the additive and multiplicative risks de<sup>fi</sup>ned by Eqs. (8) and (9) can be rewritten as

$$
\left[ R _ {i} ^ {L}, R _ {i} ^ {U} \right] = \left[ \sum_ {j = 1} ^ {m} w _ {j} r _ {i j} ^ {L}, \sum_ {j = 1} ^ {m} w _ {j} r _ {i j} ^ {U} \right], i = 1, \dots , n,\tag{20}
$$

$$
\left[ R _ {i} ^ {L}, R _ {i} ^ {U} \right] = \left[ \prod_ {j = 1} ^ {m} \left(r _ {i j} ^ {L}\right) ^ {w _ {j}}, \prod_ {j = 1} ^ {m} \left(r _ {i j} ^ {U}\right) ^ {w _ {j}} \right], i = 1, \dots , n.\tag{21}
$$

Accordingly, the maximum and minimum risk models for additive risks can be expressed as

$$
\begin{array}{l} \left[ (R _ {0} ^ {\max}) ^ {L}, (R _ {0} ^ {\max}) ^ {U} \right] = \text { Maximize } \left[ R _ {0} ^ {L}, R _ {0} ^ {U} \right] \\ \text { Subject   to } \left\{ \begin{array}{l l} \left[ R _ {i} ^ {L}, R _ {i} ^ {U} \right] \leq 1, & i = 1,..., n, \\ w _ {j} - 9 w _ {k} \leq 0, & j, k = 1,..., m; k \neq j, \end{array} \right. \end{array}\tag{22}
$$

$$
\begin{array}{l} \left[ \left(R _ {0} ^ {\min}\right) ^ {L}, \left(R _ {0} ^ {\min}\right) ^ {U} \right] = \text { Minimize } \left[ R _ {0} ^ {L}, R _ {0} ^ {U} \right] \\ \text { Subject   to } \left\{ \begin{array}{l l} \left[ R _ {i} ^ {L}, R _ {i} ^ {U} \right] \geq 1, & i = 1,..., n, \\ w _ {j} - 9 w _ {k} \leq 0, & j, k = 1,..., m; k \neq j, \end{array} \right. \end{array}\tag{23}
$$

which are further broken down into four LP models, as shown below:

$$
\begin{array}{l} (R _ {0} ^ {\max}) ^ {L} = \text { Maximize } R _ {0} ^ {L} \\ \text { Subject   to } \left\{ \begin{array}{l l} R _ {i} ^ {U} \leq 1, & i = 1,..., n, \\ w _ {j} - 9 w _ {k} \leq 0, & j, k = 1,..., m; k \neq j, \end{array} \right. \end{array}\tag{24}
$$

$$
\begin{array}{l} (R _ {0} ^ {\max}) ^ {U} = \text { Maximize } R _ {0} ^ {U} \\ \text { Subject   to } \left\{ \begin{array}{l l} R _ {i} ^ {U} \leq 1, & i = 1,..., n, \\ w _ {j} - 9 w _ {k} \leq 0, & j, k = 1,..., m; k \neq j, \end{array} \right. \end{array}\tag{25}
$$

$$
\begin{array}{l} \left(R _ {0} ^ {\min}\right) ^ {L} = \text { Minimize } R _ {0} ^ {L} \\ \text { Subject   to } \left\{ \begin{array}{l l} R _ {i} ^ {L} \geq 1, & i = 1,..., n, \\ w _ {j} - 9 w _ {k} \leq 0, & j, k = 1,..., m; k \neq j, \end{array} \right. \end{array}\tag{26}
$$

$$
\begin{array}{l} \left(R _ {0} ^ {\min}\right) ^ {U} = \text { Minimize } R _ {0} ^ {U} \\ \text { Subject   to } \left\{ \begin{array}{l l} R _ {i} ^ {L} \geq 1, & i = 1,..., n, \\ w _ {j} - 9 w _ {k} \leq 0, & j, k = 1,..., m; k \neq j. \end{array} \right. \end{array}\tag{27}
$$

In this case, the geometric average risk de<sup>fi</sup>ned by Eq. (15) can be determined by interval arithmetic [23] as

$$
\left[ \overline {{R}} _ {i} ^ {L}, \overline {{R}} _ {i} ^ {U} \right] = \left[ \sqrt {(R _ {i} ^ {\max}) ^ {L} \cdot (R _ {i} ^ {\min}) ^ {L}}, \sqrt {(R _ {i} ^ {\max}) ^ {U} \cdot (R _ {i} ^ {\min}) ^ {U}} \right], i = 1,..., n.\tag{28}
$$

For multiplicative risks de<sup>fi</sup>ned by Eq. (21), the maximum and minimum risk models are reconstructed as follows:

ln $( R _ { 0 } ^ { \operatorname* { m a x } } ) ^ { L } =$ MaximizelnR<sup>L</sup>

$$
\text { Subject   to } \left\{ \begin{array}{l l} \ln R _ {i} ^ {U} \leq 1, & i = 1,..., n, \\ w _ {j} - 9 w _ {k} \leq 0, & j, k = 1,..., m; k \neq j, \end{array} \right.\tag{29}
$$

$$
\begin{array}{l} \ln {(R _ {0} ^ {\max})} ^ {U} = \text { Maximize } \ln R _ {0} ^ {U} \\ \text { Subject   to } \left\{ \begin{array}{l l} \ln R _ {i} ^ {U} \leq 1, & i = 1,..., n, \\ w _ {j} - 9 w _ {k} \leq 0, & j, k = 1,..., m; k \neq j, \end{array} \right. \end{array}\tag{30}
$$

$$
\begin{array}{l} \ln \left(R _ {0} ^ {\min}\right) ^ {L} = \text { Minimize } \ln R _ {0} ^ {L} \\ \text { Subject   to } \left\{ \begin{array}{l l} \ln R _ {i} ^ {L} \geq 1, & i = 1,..., n, \\ w _ {j} - 9 w _ {k} \leq 0, & j, k = 1,..., m; k \neq j, \end{array} \right. \end{array}\tag{31}
$$

$$
\begin{array}{l} \ln \left(R _ {0} ^ {\min}\right) ^ {U} = \text { Minimize } \ln R _ {0} ^ {U} \\ \text { Subject   to } \left\{ \begin{array}{l l} \ln R _ {i} ^ {L} \geq 1, & i = 1,..., n, \\ w _ {j} - 9 w _ {k} \leq 0, & j, k = 1,..., m; k \neq j. \end{array} \right. \end{array}\tag{32}
$$

The geometric average risk in this case is given by

$$
\begin{array}{r l} \left[ \overline {{R}} _ {i} ^ {L}, \overline {{R}} _ {i} ^ {U} \right] = & \left[ \sqrt {E X P \left(\ln (R _ {i} ^ {\max}) ^ {L}\right) \cdot E X P \left(\ln (R _ {i} ^ {\min}) ^ {L}\right)}, \right. \\ & \left. \sqrt {E X P \left(\ln (R _ {i} ^ {\max}) ^ {U}\right) \cdot E X P \left(\ln (R _ {i} ^ {\min}) ^ {U}\right)} \right], i = 1,..., n, \end{array}\tag{33}
$$

Since the geometric average risks are intervals, an appropriate ranking approach for interval numbers is thus needed to prioritize failure modes. In Appendix A, we provide the minimax regret approach (MRA) for ranking interval numbers developed by Wang et al. [31], which will be used in this paper for comparing and ranking interval-valued geometric average risks.

## 5. Illustrations

In this section, we provide two numerical examples to illustrate the potential applications and bene<sup>fi</sup>ts of the proposed FMEA in industry. Example 1 is taken from Pillay and Wang [25] and considers no imprecise and incomplete assessment information. Example 2 incorporates imprecise and incomplete information into FMEA and is a revised version of Example 1.

Example 1. Consider an application of FMEA to a <sup>fi</sup>shing vessel. The FMEA for the <sup>fi</sup>shing vessel investigates four different systems which are structure, propulsion, electrical, and auxiliary systems. Each system is considered for different failure modes that could lead to an accident with undesired consequences. The effects of each failure mode on the system and vessel are studied along with the provisions that are in place or available to mitigate or reduce risk. For each of the failure modes, the system is investigated for any alarms or condition monitoring arrangements, which are in place. Tables 4 and 5 show respectively the 21 identi<sup>fi</sup>ed failure modes and their ratings on the three risk factors O, S, and D. The traditional RPN does not consider the relative importance of the three risk factors and is therefore unable to discriminate failure mode 11 from failure modes 1, 2, and 16, and failure mode 7 from failure mode 15.

We now examine the failure modes using DEA. By solving DEA models (13) and (14) as well as (16) and (17) for each failure mode, respectively, we get the maximum and minimum risks of all the 21 failure modes, which are shown in Table 6 together with their geometric average risks computed by Eqs. (15) and (18), respectively, and the risk priority rankings of the 21 failure modes. Based on the results in Table $6 ,$ we have the following observations:

• There is not much difference between the two sets of risk priority rankings. The Spearman's rank-correlation coef<sup>fi</sup>cient between the two sets of rankings is as high as 0.9818, which means the choice of whether to use the additive risk model in Eq. (8) or the multiplicative risk model in Eq. (9) has no signi<sup>fi</sup>cant impact on the <sup>fi</sup>nal risk priority ranking of the 21 failure modes. Major difference between the two sets of rankings happens at failure modes 3 and 19. The former has a difference of two ranking places, while the latter has a difference in ranking places of three. All the other failure modes are either ranked in the same places or have a very small gap of one.

• Failure mode 11 is successfully distinguished from failure modes 1, 2 and 16 no matter whether their risks are defined as additive or multiplicative. Failure mode 7 is also discriminated from failure mode 15.

Table 4  
Failure modes for a <sup>fi</sup>shing vessel [25]

<table><tr><td>Item</td><td>Failure mode</td><td>Description</td><td>Component</td><td>Failure effect (system)</td><td>Failure effect (vessel)</td><td>Alarm</td><td>Provision</td></tr><tr><td>1</td><td>Seizure</td><td>Structure</td><td>Rudder bearing</td><td>Rudder jam</td><td>No steering ctrl</td><td>No</td><td>Stop vessel</td></tr><tr><td>2</td><td>Breakage</td><td>Structure</td><td>Rudder bearing</td><td>Rudder loose</td><td>Reduced steering ctrl</td><td>No</td><td>Stop vessel</td></tr><tr><td>3</td><td>Structural failure</td><td>Structure</td><td>Rudder structure</td><td>Function loss</td><td>Reduced steering</td><td>No</td><td>Use beams</td></tr><tr><td>4</td><td>Loss of output</td><td>Propulsion</td><td>Main engine</td><td>Loss of thrust</td><td>Loss of speed</td><td>Yes</td><td>None</td></tr><tr><td>5</td><td>Auto shutdown</td><td>Propulsion</td><td>Main engine</td><td>M/E stops</td><td>Loss of speed</td><td>Yes</td><td>Anchor</td></tr><tr><td>6</td><td>Shaft breakage</td><td>Propulsion</td><td>Shaft and propeller</td><td>Loss of thrust</td><td>Loss of speed</td><td>No</td><td>Anchor</td></tr><tr><td>7</td><td>Shaft seizure</td><td>Propulsion</td><td>Shaft and propeller</td><td>Loss of thrust</td><td>Loss of speed</td><td>Yes</td><td>Anchor</td></tr><tr><td>8</td><td>Gearbox seizure</td><td>Propulsion</td><td>Shaft and propeller</td><td>Loss of thrust</td><td>Loss of speed</td><td>Yes</td><td>Anchor</td></tr><tr><td>9</td><td>Hydraulic failure</td><td>Propulsion</td><td>Shaft and propeller</td><td>Cannot reduce thrust</td><td>Cannot reduce speed</td><td>No</td><td>Anchor</td></tr><tr><td>10</td><td>Prop. blade failure</td><td>Propulsion</td><td>Shaft and propeller</td><td>Loss of thrust</td><td>Loss of speed</td><td>No</td><td>Slow steaming</td></tr><tr><td>11</td><td>No start air press.</td><td>Air services</td><td>Air receiver</td><td>Cannot start M/E</td><td>No propulsion</td><td>Yes</td><td>Recharge receiver</td></tr><tr><td>12</td><td>Generator fail</td><td>Electrical sys.</td><td>Power generation</td><td>No elec. power</td><td>Some system failures</td><td>Yes</td><td>Use stand-by generators</td></tr><tr><td>13</td><td>Complete loss</td><td>Electrical sys.</td><td>Main switch</td><td>Loss of main supply</td><td>No battery charging</td><td>Yes</td><td>Use emergency 24 V</td></tr><tr><td>14</td><td>Complete loss</td><td>Electrical sys.</td><td>Emergency S/B</td><td>Loss of emer. supp.</td><td>No emergency supp.</td><td>No</td><td>Use normal supply</td></tr><tr><td>15</td><td>Loss of output</td><td>Electrical sys.</td><td>Main batteries</td><td>Loss of main 24 V</td><td>Loss of main low volt</td><td>Yes</td><td>Use emergency 24 V</td></tr><tr><td>16</td><td>Loss of output</td><td>Electrical sys.</td><td>Emer. batteries</td><td>Loss of emer. supp.</td><td>No emergency supp.</td><td>No</td><td>Use normal supply</td></tr><tr><td>17</td><td>Contamination</td><td>Auxiliary sys.</td><td>Fuel system</td><td>M/E and gen. stop</td><td>Vessels stops</td><td>Yes</td><td>Anchor</td></tr><tr><td>18</td><td>No fuel to M/E</td><td>Auxiliary sys.</td><td>Fuel system</td><td>M/E stops</td><td>Vessel stops</td><td>No</td><td>Anchor</td></tr><tr><td>19</td><td>No cooling water</td><td>Auxiliary sys.</td><td>Water system</td><td>Engine overheat</td><td>M/E auto cut-out</td><td>Yes</td><td>Use stand-by pump</td></tr><tr><td>20</td><td>System loss</td><td>Auxiliary sys.</td><td>Hydraulic</td><td>No hydraulics</td><td>No steering</td><td>Yes</td><td>Stop vessel</td></tr><tr><td>21</td><td>Loss of pressure</td><td>Auxiliary sys.</td><td>Lube oil system</td><td>Low pressure cut-off</td><td>M/E stops</td><td>Yes</td><td>Use stand-by pump</td></tr></table>

• Failure mode 11 is ranked far behind failure modes 1, 2 and 16 because it has a very small severity rating in comparison with failure modes 1, 2, and 16. This is also true for failure modes 7 and 15. The former has a very high severity rating and is therefore ranked higher than the latter.

• Except for failure modes 14 and 20, the risk priority rankings of the other 19 failure modes obtained by their geometric average risks are all different from those by their RPNs. This shows the fact that the proposed FMEA is totally different from the traditional FMEA. The biggest difference among the three sets of risk priority rankings in Tables 4 and 5 happens at failure modes 11 and 19, which have a difference of up to four or <sup>fi</sup>ve ranking places by the two different FMEA priority methods. The Spearman's rank-correlation coef<sup>fi</sup>- cients between the priority rankings of the 21 failure modes by the RPNs and the two geometric average risks are 0.9195 and 0.9340 for additive and multiplicative risks, respectively, which are less than that between the rankings by the two geometric average risks.

Table 5  
FMEA for the <sup>fi</sup>shing vessel by RPN [25].

<table><tr><td>Failure mode</td><td>O</td><td>S</td><td>D</td><td>RPN</td><td>Priority ranking</td></tr><tr><td>1</td><td>1</td><td>8</td><td>3</td><td>24</td><td>14</td></tr><tr><td>2</td><td>1</td><td>8</td><td>3</td><td>24</td><td>14</td></tr><tr><td>3</td><td>2</td><td>8</td><td>4</td><td>64</td><td>10</td></tr><tr><td>4</td><td>8</td><td>8</td><td>5</td><td>320</td><td>2</td></tr><tr><td>5</td><td>6</td><td>8</td><td>6</td><td>288</td><td>3</td></tr><tr><td>6</td><td>2</td><td>8</td><td>1</td><td>16</td><td>19</td></tr><tr><td>7</td><td>2</td><td>9</td><td>2</td><td>36</td><td>12</td></tr><tr><td>8</td><td>1</td><td>4</td><td>3</td><td>12</td><td>20</td></tr><tr><td>9</td><td>3</td><td>2</td><td>3</td><td>18</td><td>18</td></tr><tr><td>10</td><td>1</td><td>2</td><td>4</td><td>8</td><td>21</td></tr><tr><td>11</td><td>4</td><td>2</td><td>3</td><td>24</td><td>14</td></tr><tr><td>12</td><td>9</td><td>3</td><td>7</td><td>189</td><td>4</td></tr><tr><td>13</td><td>8</td><td>3</td><td>6</td><td>144</td><td>7</td></tr><tr><td>14</td><td>3</td><td>7</td><td>4</td><td>84</td><td>9</td></tr><tr><td>15</td><td>3</td><td>3</td><td>4</td><td>36</td><td>12</td></tr><tr><td>16</td><td>1</td><td>8</td><td>3</td><td>24</td><td>14</td></tr><tr><td>17</td><td>4</td><td>8</td><td>5</td><td>160</td><td>6</td></tr><tr><td>18</td><td>2</td><td>7</td><td>7</td><td>98</td><td>8</td></tr><tr><td>19</td><td>7</td><td>2</td><td>4</td><td>56</td><td>11</td></tr><tr><td>20</td><td>9</td><td>8</td><td>9</td><td>648</td><td>1</td></tr><tr><td>21</td><td>9</td><td>3</td><td>6</td><td>162</td><td>5</td></tr></table>

The above observations show the applicability and potentials of the new FMEA and its advantages over the traditional FMEA. To test the robustness of the risk priority rankings in Table 6, we conduct a sensitivity analysis to the weight restriction of the ratio of maximum weight to minimum weight. Table 7 shows the risk priority rankings of the 21 failure modes under different weight restrictions, where the <sup>fi</sup>ve-point Likert scale means the weight restriction of 1≤max{w ,…, $w _ { m } \} / \mathrm { m i n } \{ w _ { 1 } , . . . , w _ { m } \} \le 5$ , whereas +∞ represents no restriction to the weights of risk factors. In the case that there is no weight restriction, some of the risk factors may be assigned a zero weight by the DEA models. From Table 7 the following observations have been made:

• Failure modes can also be prioritized by DEA models without imposing any weight restriction, but this will result in dif<sup>fi</sup>culties in explaining the risks of failure modes due to the presence of zero weight for some of the risk factors and may also result in some ties for risk priority ranking. So, imposing a weight restriction is of bene<sup>fi</sup>t to the risk prioritizations of failure modes and their explanations.

• For additive risks, no matter whether the weight restriction is <sup>fi</sup>ve, seven or nine, the risk priority rankings of the 21 failure modes are nearly the same with only a small ranking difference of one for some of the failure modes such as failure modes 8, 11, 12, 17, 18 and 21.

• For multiplicative risks, there is seemingly a big difference of three between the rankings of failure mode 15, but in fact, it is only the difference that the failure mode 15 is ranked higher or lower than failure modes 1, 2 and 16, which have exactly the same ratings on the three risk factors and can therefore be viewed as one failure mode or DMU. In this sense, the differences between the rankings under different weight restrictions are still very small and are of no more than one.

From the above observations it can be concluded that the priority rankings in Table 6 are stable and robust, and will not be signi<sup>fi</sup>cantly changed when a different <sup>fi</sup>ve-point Likert scale is imposed as the weight restriction on the ratio of maximum weight to minimum weight.

Example 2. The above example assumes that FMEA team members reach a consensus on the ratings of each failure mode. In reality, however, different team members may have different opinions and provide distinct ratings, some of which may be incomplete or imprecise. Tables 8–10 show hypothetical ratings of the 21 failure modes on O, S, and D provided by <sup>fi</sup>ve FMEA team members, where incomplete and imprecise ratings are shaded for the sake of clarity. The relative importance weights of the <sup>fi</sup>ve FMEA team members are assumed to be 0.3, 0.3, 0.2, 0.1, and 0.1, respectively. That is, $( \lambda _ { 1 } , . . . ,$ $\lambda _ { 5 } ) = ( 0 . 3 , 0 . 3 , 0 . 2 , 0 . 1 , 0 . 1 )$

FMEA for the <sup>fi</sup>shing vessel by DEA.

<table><tr><td rowspan="2">Failure mode</td><td colspan="4">Additive risks</td><td colspan="4">Multiplicative risks</td></tr><tr><td>Maximum risk</td><td>Minimum risk</td><td>Geometric average risk</td><td>Priority ranking</td><td>Maximum risk</td><td>Minimum risk</td><td>Geometric average risk</td><td>Priority ranking</td></tr><tr><td>1</td><td>0.84</td><td>1.12</td><td>0.97</td><td>12</td><td>2.36</td><td>2.95</td><td>2.64</td><td>13</td></tr><tr><td>2</td><td>0.84</td><td>1.12</td><td>0.97</td><td>12</td><td>2.36</td><td>2.95</td><td>2.64</td><td>13</td></tr><tr><td>3</td><td>0.87</td><td>1.60</td><td>1.18</td><td>9</td><td>2.46</td><td>5.46</td><td>3.66</td><td>7</td></tr><tr><td>4</td><td>0.94</td><td>2.16</td><td>1.43</td><td>3</td><td>2.64</td><td>7.27</td><td>4.38</td><td>3</td></tr><tr><td>5</td><td>0.93</td><td>2.32</td><td>1.47</td><td>2</td><td>2.62</td><td>7.73</td><td>4.51</td><td>2</td></tr><tr><td>6</td><td>0.83</td><td>1.00</td><td>0.91</td><td>16</td><td>2.32</td><td>2.72</td><td>2.51</td><td>17</td></tr><tr><td>7</td><td>0.94</td><td>1.23</td><td>1.08</td><td>11</td><td>2.50</td><td>4.06</td><td>3.18</td><td>11</td></tr><tr><td>8</td><td>0.44</td><td>1.00</td><td>0.67</td><td>18</td><td>1.80</td><td>2.72</td><td>2.21</td><td>19</td></tr><tr><td>9</td><td>0.33</td><td>1.00</td><td>0.57</td><td>21</td><td>1.64</td><td>2.72</td><td>2.11</td><td>21</td></tr><tr><td>10</td><td>0.40</td><td>1.00</td><td>0.63</td><td>20</td><td>1.73</td><td>2.72</td><td>2.17</td><td>20</td></tr><tr><td>11</td><td>0.42</td><td>1.02</td><td>0.65</td><td>19</td><td>1.81</td><td>2.76</td><td>2.24</td><td>18</td></tr><tr><td>12</td><td>0.93</td><td>1.85</td><td>1.31</td><td>5</td><td>2.58</td><td>5.43</td><td>3.75</td><td>6</td></tr><tr><td>13</td><td>0.83</td><td>1.74</td><td>1.20</td><td>8</td><td>2.46</td><td>5.11</td><td>3.54</td><td>10</td></tr><tr><td>14</td><td>0.78</td><td>1.60</td><td>1.12</td><td>10</td><td>2.38</td><td>5.43</td><td>3.59</td><td>9</td></tr><tr><td>15</td><td>0.43</td><td>1.27</td><td>0.74</td><td>17</td><td>1.84</td><td>3.75</td><td>2.63</td><td>16</td></tr><tr><td>16</td><td>0.84</td><td>1.12</td><td>0.97</td><td>12</td><td>2.36</td><td>2.95</td><td>2.64</td><td>13</td></tr><tr><td>17</td><td>0.90</td><td>1.96</td><td>1.33</td><td>4</td><td>2.56</td><td>6.69</td><td>4.14</td><td>4</td></tr><tr><td>18</td><td>0.80</td><td>2.05</td><td>1.28</td><td>6</td><td>2.41</td><td>6.82</td><td>4.05</td><td>5</td></tr><tr><td>19</td><td>0.70</td><td>1.22</td><td>0.93</td><td>15</td><td>2.26</td><td>3.22</td><td>2.70</td><td>12</td></tr><tr><td>20</td><td>1.00</td><td>3.16</td><td>1.78</td><td>1</td><td>2.72</td><td>10.00</td><td>5.21</td><td>1</td></tr><tr><td>21</td><td>0.92</td><td>1.78</td><td>1.28</td><td>7</td><td>2.57</td><td>5.14</td><td>3.63</td><td>8</td></tr></table>

Evidently, existing FMEA methods can handle fuzzy information, but have no way to deal with incomplete and imprecise information. To prioritize the failure modes with incomplete and imprecise assessment information, we <sup>fi</sup>rst synthesize individual ratings given by the <sup>fi</sup>ve FMEA team members into group ratings using Eq. (19). The results are shown in Table 10, from which it can be seen that quite a number of the ratings are intervals rather than precise values due to the presence of incomplete and imprecise assessment information.

For the group ratings in Table 11, we view precise ratings as special cases of intervals and solve interval DEA models (24)–(27) and (29)– (32) for each of the 21 failure modes to get their maximum and minimum risks. Tables 12 and 13 show the results that are obtained from the solution of the interval DEA models. The geometric average risks of the 21 failure modes are then computed by Eqs. (28) and (33). The corresponding results are shown in the fourth column of Tables 12 and 13, respectively. By comparing their geometric average risks using the minimax regret approach detailed in Appendix A, the 21 failure modes are <sup>fi</sup>nally prioritized. Their risk priority rankings are presented in the last column of Tables 12 and 13.

Risk priority rankings under different weight restrictions.

<table><tr><td rowspan="2">Failure mode</td><td colspan="4">Additive risk</td><td colspan="4">Multiplicative risk</td></tr><tr><td>Five-point scale</td><td>Seven-point scale</td><td>Nine-point scale</td><td>+ $\infty$ </td><td>Five-point scale</td><td>Seven-point scale</td><td>Nine-point scale</td><td>+ $\infty$ </td></tr><tr><td>1</td><td>12</td><td>12</td><td>12</td><td>12</td><td>14</td><td>14</td><td>13</td><td>12</td></tr><tr><td>2</td><td>12</td><td>12</td><td>12</td><td>12</td><td>14</td><td>14</td><td>13</td><td>12</td></tr><tr><td>3</td><td>9</td><td>9</td><td>9</td><td>8</td><td>8</td><td>7</td><td>7</td><td>6</td></tr><tr><td>4</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>5</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>6</td><td>16</td><td>16</td><td>16</td><td>15</td><td>17</td><td>17</td><td>17</td><td>16</td></tr><tr><td>7</td><td>11</td><td>11</td><td>11</td><td>11</td><td>11</td><td>11</td><td>11</td><td>11</td></tr><tr><td>8</td><td>19</td><td>18</td><td>18</td><td>18</td><td>19</td><td>19</td><td>19</td><td>18</td></tr><tr><td>9</td><td>21</td><td>21</td><td>21</td><td>21</td><td>21</td><td>21</td><td>21</td><td>21</td></tr><tr><td>10</td><td>20</td><td>20</td><td>20</td><td>19</td><td>20</td><td>20</td><td>20</td><td>19</td></tr><tr><td>11</td><td>18</td><td>19</td><td>19</td><td>19</td><td>18</td><td>18</td><td>18</td><td>19</td></tr><tr><td>12</td><td>4</td><td>4</td><td>5</td><td>6</td><td>6</td><td>6</td><td>6</td><td>8</td></tr><tr><td>13</td><td>8</td><td>8</td><td>8</td><td>9</td><td>10</td><td>10</td><td>10</td><td>10</td></tr><tr><td>14</td><td>10</td><td>10</td><td>10</td><td>10</td><td>9</td><td>9</td><td>9</td><td>7</td></tr><tr><td>15</td><td>17</td><td>17</td><td>17</td><td>17</td><td>13</td><td>13</td><td>16</td><td>15</td></tr><tr><td>16</td><td>12</td><td>12</td><td>12</td><td>12</td><td>14</td><td>14</td><td>13</td><td>12</td></tr><tr><td>17</td><td>5</td><td>5</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>18</td><td>7</td><td>7</td><td>6</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>19</td><td>15</td><td>15</td><td>15</td><td>16</td><td>12</td><td>12</td><td>12</td><td>17</td></tr><tr><td>20</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>21</td><td>6</td><td>6</td><td>7</td><td>6</td><td>7</td><td>8</td><td>8</td><td>8</td></tr></table>

From the risk priority rankings in Tables 12 and 13, it is observed that the two sets of risk priority rankings are still highly correlated and their Spearman's rank-correlation coef<sup>fi</sup>cient is 0.9766. The biggest difference between the two sets of risk priority rankings happens at failure modes 16 and 19, followed by failure modes 12, 15 and 18. The former two failure modes have a difference of three ranking places between the two risk de<sup>fi</sup>nitions, while the latter three failure modes have a difference of two. These differences are considered as small or not signi<sup>fi</sup>cant.

Occurrence assessment by FMEA team members

<table><tr><td rowspan="2">Failure mode</td><td colspan="5">FMEA team member</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1-2</td><td>1</td><td>1</td></tr><tr><td>2</td><td>1: 50%</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td></td><td>2: 50%</td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>2</td><td>2: 90%</td><td>2</td><td>2</td><td>2</td></tr><tr><td>4</td><td>8</td><td>8</td><td>8: 80%</td><td>8</td><td>8</td></tr><tr><td></td><td></td><td></td><td>9: 20%</td><td></td><td></td></tr><tr><td>5</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td></tr><tr><td>6</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2-3</td></tr><tr><td>7</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>8</td><td>1</td><td>1: 75%</td><td>1</td><td>1</td><td>1</td></tr><tr><td></td><td></td><td>2: 25%</td><td></td><td></td><td></td></tr><tr><td>9</td><td>3-4</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>10</td><td>1: 80%</td><td>1</td><td>1</td><td>1</td><td>2: 85%</td></tr><tr><td></td><td>2: 20%</td><td></td><td></td><td></td><td>3: 15%</td></tr><tr><td>11</td><td>4</td><td>4</td><td>4</td><td>4: 75%</td><td>4</td></tr><tr><td></td><td></td><td></td><td></td><td>5: 25%</td><td></td></tr><tr><td>12</td><td>9</td><td>9</td><td>9</td><td>9</td><td>9</td></tr><tr><td>13</td><td>8</td><td>8: 80%</td><td>8</td><td>8</td><td>8</td></tr><tr><td>14</td><td>3</td><td>3</td><td>4</td><td>3</td><td>3</td></tr><tr><td>15</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3: 70%</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>4: 30%</td></tr><tr><td>16</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>17</td><td>4: 90%</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td></td><td>5: 10%</td><td></td><td></td><td></td><td></td></tr><tr><td>18</td><td>2</td><td>2</td><td>2: 90%</td><td>2</td><td>2</td></tr><tr><td>19</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7: 80%</td></tr><tr><td>20</td><td>9</td><td>9</td><td>9</td><td>8: 30%</td><td>9</td></tr><tr><td></td><td></td><td></td><td></td><td>9: 70%</td><td></td></tr><tr><td>21</td><td>9</td><td>8-9</td><td>9</td><td>9</td><td>9</td></tr></table>

Table 9  
Severity assessment by FMEA team members.

<table><tr><td rowspan="2">Failure mode</td><td colspan="5">FMEA team member</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td rowspan="2">1</td><td>7: 20%</td><td>8</td><td>8</td><td>7: 50%</td><td>8</td></tr><tr><td>8: 80%</td><td></td><td></td><td>8: 50%</td><td></td></tr><tr><td>2</td><td>8</td><td>8</td><td>8</td><td>8</td><td>7-9</td></tr><tr><td>3</td><td>7</td><td>8</td><td>7</td><td>8</td><td>8</td></tr><tr><td>4</td><td>8</td><td>8</td><td>8</td><td>8</td><td>7-9</td></tr><tr><td>5</td><td>8</td><td>9: 90%</td><td>8</td><td>8</td><td>8</td></tr><tr><td>6</td><td>8</td><td>8</td><td>8</td><td>6-8</td><td>8</td></tr><tr><td rowspan="2">7</td><td>9: 75%</td><td>9</td><td>9</td><td>9</td><td>9</td></tr><tr><td>8: 25%</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">8</td><td>4</td><td>4</td><td>4</td><td>4: 50%</td><td>3: 25%</td></tr><tr><td></td><td></td><td></td><td>5: 50%</td><td>4: 75%</td></tr><tr><td>9</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td rowspan="2">10</td><td>2</td><td>2</td><td>2: 60%</td><td>2</td><td>2</td></tr><tr><td></td><td></td><td>3: 40%</td><td></td><td></td></tr><tr><td>11</td><td>2</td><td>2-3</td><td>2</td><td>2</td><td>2</td></tr><tr><td rowspan="2">12</td><td>3</td><td>3</td><td>3: 60%</td><td>3</td><td>3</td></tr><tr><td></td><td></td><td>4: 40%</td><td></td><td></td></tr><tr><td rowspan="2">13</td><td>2-3: 80%</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>3-4: 20%</td><td></td><td></td><td></td><td></td></tr><tr><td>14</td><td>7</td><td>8</td><td>7</td><td>7</td><td>7</td></tr><tr><td>15</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>16</td><td>8</td><td>8</td><td>8</td><td>8</td><td>8</td></tr><tr><td>17</td><td>8</td><td>7</td><td>8</td><td>8</td><td>8</td></tr><tr><td>18</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td></tr><tr><td rowspan="2">19</td><td>2</td><td>2: 75%</td><td>2</td><td>2</td><td>2</td></tr><tr><td></td><td>3: 25%</td><td></td><td></td><td></td></tr><tr><td>20</td><td>8</td><td>8</td><td>8-9</td><td>8</td><td>8</td></tr><tr><td>21</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr></table>

The above example shows the capability of the proposed FMEA in prioritization of failure modes under incomplete and imprecise information. This is its biggest advantage over existing FMEA methods.

Detection assessment by FMEA team members.

<table><tr><td rowspan="2">Failure mode</td><td colspan="5">FMEA team member</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>1</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3:90%</td></tr><tr><td>2</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>3</td><td>4</td><td>4</td><td>4</td><td>4</td><td>3-4:80%5-6:20%</td></tr><tr><td>4</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>5</td><td>6</td><td>6</td><td>6:85%7:15%</td><td>6</td><td>6</td></tr><tr><td>6</td><td>1</td><td>1:85%2:15%</td><td>2</td><td>1-2</td><td>1</td></tr><tr><td>7</td><td>3</td><td>2</td><td>2</td><td>2:75%3:25%</td><td>2</td></tr><tr><td>8</td><td>3</td><td>3</td><td>3:80%4:20%</td><td>3</td><td>3</td></tr><tr><td>9</td><td>3</td><td>3</td><td>3:60%4:40%</td><td>3</td><td>3</td></tr><tr><td>10</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>11</td><td>3:70%5:30%</td><td>3</td><td>3</td><td>3</td><td>4</td></tr><tr><td>12</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td></tr><tr><td>13</td><td>6</td><td>6</td><td>6</td><td>5</td><td>6</td></tr><tr><td>14</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>15</td><td>4</td><td>4:95%</td><td>4</td><td>4</td><td>4</td></tr><tr><td>16</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>17</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>18</td><td>7</td><td>6-8</td><td>7</td><td>7</td><td>7</td></tr><tr><td>19</td><td>4</td><td>4</td><td>4</td><td>4:90%</td><td>4</td></tr><tr><td>20</td><td>9:95%</td><td>9</td><td>9</td><td>9</td><td>9</td></tr><tr><td>21</td><td>6</td><td>6</td><td>4-6</td><td>6</td><td>6:25%7:75%</td></tr></table>

Table 11  
Group ratings aggregated from FMEA team members.

<table><tr><td>Failure mode</td><td>O</td><td>S</td><td>D</td></tr><tr><td>1</td><td>1-1.2</td><td>7.89</td><td>2.98-3.07</td></tr><tr><td>2</td><td>1.15</td><td>7.9-8.1</td><td>3</td></tr><tr><td>3</td><td>1.97-2.24</td><td>7.5</td><td>3.94-4.04</td></tr><tr><td>4</td><td>8.04</td><td>7.9-8.1</td><td>5</td></tr><tr><td>5</td><td>6</td><td>8.06-8.33</td><td>6.03</td></tr><tr><td>6</td><td>2-2.1</td><td>7.8-8</td><td>1.245-1.345</td></tr><tr><td>7</td><td>2</td><td>8.925</td><td>2.325</td></tr><tr><td>8</td><td>1.075</td><td>4.025</td><td>3.04</td></tr><tr><td>9</td><td>3-3.3</td><td>2</td><td>3.08</td></tr><tr><td>10</td><td>1.175</td><td>2.08</td><td>4</td></tr><tr><td>11</td><td>4.025</td><td>2-2.3</td><td>3.28</td></tr><tr><td>12</td><td>9</td><td>3.08</td><td>7</td></tr><tr><td>13</td><td>7.58-8.12</td><td>2.76-3.06</td><td>5.9</td></tr><tr><td>14</td><td>3.2</td><td>7.3</td><td>4</td></tr><tr><td>15</td><td>3.03</td><td>3</td><td>3.955-4.09</td></tr><tr><td>16</td><td>1</td><td>8</td><td>3</td></tr><tr><td>17</td><td>4.03</td><td>7.7</td><td>5</td></tr><tr><td>18</td><td>1.98-2.16</td><td>7</td><td>6.7-7.3</td></tr><tr><td>19</td><td>6.89-7.16</td><td>2.075</td><td>3.97-4.06</td></tr><tr><td>20</td><td>8.97</td><td>8-8.2</td><td>8.88-9.015</td></tr><tr><td>21</td><td>8.7-9</td><td>3</td><td>5.675-6.075</td></tr></table>

## 6. Conclusions

As an improvement to the traditional RPN, we proposed in this paper an FMEA by data envelopment analysis. By de<sup>fi</sup>ning the risks of failure modes as the weighted sum or weighted product of risk factors, we developed DEA models for measuring the maximum and minimum risks of failure modes. Their geometric averages measure the overall risk of each failure mode and are therefore used for prioritizing failure modes. Considering the fact that FMEA may involve incomplete and imprecise assessment information, we also developed interval DEA models for FMEA. The proposed FMEA was examined with two numerical examples and proved to be useful and effective.

In comparison with the traditional RPN and its various improvements such as fuzzy FMEA, the proposed FMEA has the following advantages:

• The relative importance weights of risk factors are considered and determined by DEA models with a weight restriction on the ratio of maximum weight to minimum weight to avoid the relative importance of any risk factors from being under- or overestimated.

Additive risk assessment and risk priority.

<table><tr><td rowspan="2">Failure mode</td><td colspan="3">Additive risks</td><td rowspan="2">Priority ranking</td></tr><tr><td>Maximum risk</td><td>Minimum risk</td><td>Geometric average risk</td></tr><tr><td>1</td><td>[0.817, 0.820]</td><td>[1.082, 1.152]</td><td>[0.940, 0.972]</td><td>13</td></tr><tr><td>2</td><td>[0.820, 0.840]</td><td>[1.125, 1.131]</td><td>[0.961, 0.974]</td><td>12</td></tr><tr><td>3</td><td>[0.800, 0.804]</td><td>[1.515, 1.556]</td><td>[1.101, 1.118]</td><td>10</td></tr><tr><td>4</td><td>[0.917, 0.936]</td><td>[2.092, 2.108]</td><td>[1.385, 1.405]</td><td>3</td></tr><tr><td>5</td><td>[0.921, 0.948]</td><td>[2.285, 2.306]</td><td>[1.451, 1.478]</td><td>2</td></tr><tr><td>6</td><td>[0.800, 0.822]</td><td>[1.000, 1.043]</td><td>[0.895, 0.926]</td><td>16</td></tr><tr><td>7</td><td>[0.922, 0.922]</td><td>[1.246, 1.246]</td><td>[1.072, 1.072]</td><td>11</td></tr><tr><td>8</td><td>[0.440, 0.440]</td><td>[1.000, 1.000]</td><td>[0.663, 0.663]</td><td>19</td></tr><tr><td>9</td><td>[0.334, 0.355]</td><td>[1.000, 1.006]</td><td>[0.578, 0.598]</td><td>21</td></tr><tr><td>10</td><td>[0.399, 0.399]</td><td>[1.000, 1.000]</td><td>[0.632, 0.632]</td><td>20</td></tr><tr><td>11</td><td>[0.424, 0.427]</td><td>[1.051, 1.102]</td><td>[0.668, 0.686]</td><td>18</td></tr><tr><td>12</td><td>[0.930, 0.930]</td><td>[1.827, 1.827]</td><td>[1.304, 1.304]</td><td>4</td></tr><tr><td>13</td><td>[0.785, 0.838]</td><td>[1.600, 1.731]</td><td>[1.121, 1.204]</td><td>8</td></tr><tr><td>14</td><td>[0.794, 0.794]</td><td>[1.606, 1.606]</td><td>[1.129, 1.129]</td><td>9</td></tr><tr><td>15</td><td>[0.423, 0.434]</td><td>[1.248, 1.271]</td><td>[0.727, 0.744]</td><td>17</td></tr><tr><td>16</td><td>[0.828, 0.828]</td><td>[1.089, 1.089]</td><td>[0.949, 0.949]</td><td>14</td></tr><tr><td>17</td><td>[0.853, 0.853]</td><td>[1.900, 1.900]</td><td>[1.274, 1.274]</td><td>5</td></tr><tr><td>18</td><td>[0.781, 0.798]</td><td>[1.888, 2.022]</td><td>[1.214, 1.271]</td><td>7</td></tr><tr><td>19</td><td>[0.695, 0.721]</td><td>[1.228, 1.243]</td><td>[0.928, 0.947]</td><td>15</td></tr><tr><td>20</td><td>[0.997, 1.000]</td><td>[3.075, 3.121]</td><td>[1.751, 1.767]</td><td>1</td></tr><tr><td>21</td><td>[0.888, 0.920]</td><td>[1.721, 1.753]</td><td>[1.236, 1.270]</td><td>6</td></tr></table>

Multiplicative risk assessment and risk priority.

<table><tr><td rowspan="2">Failure mode</td><td colspan="3">Multiplicative risks</td><td rowspan="2">Priority ranking</td></tr><tr><td>Maximum risk</td><td>Minimum risk</td><td>Geometric average risk</td></tr><tr><td>1</td><td>[2.325, 2.346]</td><td>[2.718, 3.257]</td><td>[2.514, 2.765]</td><td>14</td></tr><tr><td>2</td><td>[2.341, 2.363]</td><td>[3.089, 3.098]</td><td>[2.689, 2.706]</td><td>13</td></tr><tr><td>3</td><td>[2.375, 2.391]</td><td>[4.764, 4.922]</td><td>[3.364, 3.431]</td><td>10</td></tr><tr><td>4</td><td>[2.600, 2.626]</td><td>[6.669, 6.737]</td><td>[4.164, 4.206]</td><td>3</td></tr><tr><td>5</td><td>[2.609, 2.642]</td><td>[7.213, 7.304]</td><td>[4.338, 4.393]</td><td>2</td></tr><tr><td>6</td><td>[2.297, 2.332]</td><td>[2.718, 2.875]</td><td>[2.499, 2.589]</td><td>16</td></tr><tr><td>7</td><td>[2.485, 2.485]</td><td>[3.909, 3.909]</td><td>[3.117, 3.117]</td><td>11</td></tr><tr><td>8</td><td>[1.800, 1.800]</td><td>[2.718, 2.718]</td><td>[2.212, 2.212]</td><td>19</td></tr><tr><td>9</td><td>[1.644, 1.686]</td><td>[2.718, 2.733]</td><td>[2.114, 2.147]</td><td>21</td></tr><tr><td>10</td><td>[1.742, 1.742]</td><td>[2.718, 2.718]</td><td>[2.176, 2.176]</td><td>20</td></tr><tr><td>11</td><td>[1.821, 1.832]</td><td>[2.841, 3.039]</td><td>[2.275, 2.359]</td><td>18</td></tr><tr><td>12</td><td>[2.586, 2.586]</td><td>[5.432, 5.432]</td><td>[3.748, 3.748]</td><td>6</td></tr><tr><td>13</td><td>[2.397, 2.470]</td><td>[4.645, 5.008]</td><td>[3.337, 3.517]</td><td>9</td></tr><tr><td>14</td><td>[2.402, 2.402]</td><td>[5.125, 5.125]</td><td>[3.508, 3.508]</td><td>8</td></tr><tr><td>15</td><td>[1.832, 1.855]</td><td>[3.602, 3.663]</td><td>[2.569, 2.607]</td><td>15</td></tr><tr><td>16</td><td>[2.338, 2.338]</td><td>[2.735, 2.735]</td><td>[2.529, 2.529]</td><td>17</td></tr><tr><td>17</td><td>[2.500, 2.500]</td><td>[6.064, 6.064]</td><td>[3.894, 3.894]</td><td>4</td></tr><tr><td>18</td><td>[2.370, 2.421]</td><td>[6.064, 6.417]</td><td>[3.791, 3.941]</td><td>5</td></tr><tr><td>19</td><td>[2.248, 2.283]</td><td>[3.240, 3.269]</td><td>[2.699, 2.732]</td><td>12</td></tr><tr><td>20</td><td>[2.714, 2.718]</td><td>[9.301, 9.461]</td><td>[5.024, 5.071]</td><td>1</td></tr><tr><td>21</td><td>[2.528, 2.568]</td><td>[4.879, 5.063]</td><td>[3.512, 3.606]</td><td>7</td></tr></table>

• Risk factors are aggregated in the ways that are different from the RPN, which aggregates the risk factors by simple product and has been subject to signi<sup>fi</sup>cant criticism.

• Failure modes can be better ranked and well distinguished from each other.

• Incomplete and imprecise assessment information can be considered and handled if any.

• More risk factors can be included if necessary. The proposed FMEA is not limited to O, S and D, but applicable to any number of risk factors.

• Unlike fuzzy FMEA, there is no need to build any fuzzy if–then rules, which prove to be highly subjective and costly. Different experts may make different judgments, leading to different rules.

Finally, we point out that DEA-computed weights are not <sup>fi</sup>xed for failure modes. They vary from one failure mode to another. If the DMs have preference structures on the relative importance of risk factors, they could be added as constraints to the developed DEA models to form an assurance region (AR) on the relative importance weights. It is expected that the proposed FMEA as a decision-making tool can <sup>fi</sup>nd more applications in quality and reliability engineering in the future.

## Acknowledgements

The authors would like to thank three anonymous referees for their constructive comments and suggestions, which have helped to improve the paper.

The work described in this paper was supported by the National Natural Science Foundation of China (NSFC) under Grant No. 70771027, and also supported by a grant from the Research Grants Council of the Hong Kong Special Administrative Region, China, Project no. CityU 111906.

## Appendix A. The minimax regret approach for ranking interval numbers

The minimax regret approach (MRA) developed by Wang et al. [31] is a method for comparing and ranking interval numbers and is brie<sup>fl</sup>y summarized below for the purpose of application. Let $u _ { i } = [ u _ { i } ^ { L } ,$ $u _ { i } ^ { U } ] = < c _ { i } , d _ { i } > ( i = 1 , . . . , N )$ be N intervals, where $c _ { i } = \textstyle { \frac { 1 } { 2 } } ( u _ { i } ^ { L } + u _ { i } ^ { U } )$ and $\begin{array} { r } { d _ { i } = \frac 1 2 ( u _ { i } ^ { U } - u _ { i } ^ { L } ) } \end{array}$ <sup>ð Þ</sup>are their midpoints and widths. Without loss of generality, suppose $u _ { i } = [ u _ { i } ^ { L } , u _ { i } ^ { U } ]$ is chosen as the biggest interval. Let $\nu = \operatorname* { m a x } _ { i \neq i } ( u _ { j } ^ { U } ) .$ . If u<sup>L</sup> $< \nu ,$ then the DM may regret due to the loss of opportunity that other interval numbers might be ranked higher than $u _ { i } .$ The maximum loss the DM may suffer from is given by

$$
\operatorname{Max} (r _ {i}) = v - u _ {i} ^ {L} = \max _ {j \neq i} \left(u _ {j} ^ {U}\right) - u _ {i} ^ {L}.
$$

If $u _ { i } ^ { L } { \geq } v ,$ the DM will de<sup>fi</sup>nitely suffer from no loss of opportunity and thus will not regret. In this situation, the DM's regret is de<sup>fi</sup>ned as zero, i.e. $r _ { i } = 0 .$ . Combining the above two situations, we get

$$
\operatorname{Max} (r _ {i}) = \max \left[ \max _ {j \neq i} \left(u _ {j} ^ {U}\right) - u _ {i} ^ {L}, 0 \right].
$$

The minimax regret criterion will choose the interval satisfying the following condition as the best or most desirable:

$$
\underset {i} {\text { Min }} \left\{\max (r _ {i}) \right\} = \underset {i} {\text { min }} \left\{\max \left[ \underset {j \neq i} {\max} \left(u _ {j} ^ {U}\right) - u _ {i} ^ {L}, 0 \right] \right\}.
$$

Based upon the above analysis, Wang et al. [31] gave the following de<sup>fi</sup>nition for comparing and ranking interval numbers.

De<sup>fi</sup>nition 1. Let $u _ { i } = [ u _ { i } ^ { L } , u _ { i } ^ { U } ] = < c _ { i } , d _ { i } > ~ ( i = 1 , . . . , ~ N )$ be N intervals. The maximum regret value (MRV) of each interval $u _ { i }$ is de<sup>fi</sup>ned as

$$
R (u _ {i}) = \max \left[ \max _ {j \neq i} \left(u _ {j} ^ {U}\right) - u _ {i} ^ {L}, 0 \right], i = 1, \dots , N.\tag{38}
$$

The interval with the smallest MRV should be chosen as the best interval. In order to generate a full ranking for the N intervals, the following eliminating process was suggested by Wang et al.

Step 1. Calculate the MRVs of the N intervals and choose the interval with the smallest MRV as the best one. Suppose ${ { u } _ { i _ { 1 } } }$ is selected, where $1 \leq i _ { 1 } \leq N .$

Step 2. Eliminate ${ { u } _ { i _ { 1 } } }$ from further consideration and recalculate the MRVs of the remaining $( N - 1 )$ intervals, from which choose the one with the smallest MRV as the second best interval. Suppose $u _ { i _ { 2 } }$ is chosen, where $1 \leq i _ { 2 } \leq N _ { \mathrm { \uparrow } }$ but $i _ { 2 } \neq i _ { 1 }$

Step 3. Eliminate $u _ { i _ { 2 } }$ from further consideration and recalculate the MRVs of the remaining (N−2) intervals, from which choose the one with the smallest MRV as the third best interval.

Step 4. Repeat the above eliminating process until only one interval $u _ { i _ { N } }$ is left. The <sup>fi</sup>nal ranking is $u _ { i _ { 1 } } > u _ { i _ { 2 } } > \cdots > u _ { i _ { N } } .$

By the above MRA, interval-valued geometric average risks can be compared and ranked. The ranking will serve as the risk priority of the n failure modes when incomplete or imprecise information is available.

## References

[1] M. Ben-Daya, A. Raouf, A revised failure mode and effects analysis model, International Journal of Quality & Reliability Management 13 (1) (1996) 43–47.

[2] M. Bevilacqua, M. Braglia, R. Gabbrielli, Monte Carlo simulation approach for a modi<sup>fi</sup>ed FMECA in a power plant, Quality and Reliability Engineering International 16 (2000) 313–324.

[3] J.B. Bowles, An assessment of PRN prioritization in a failure modes effects and criticality analysis, Journal of the IEST 47 (2004) 51–56.

[4] J.B. Bowles, C.E. Peláez, Fuzzy logic prioritization of failures in a system failure mode, effects and criticality analysis, Reliability Engineering and System Safety 50 (1995) 203-213.

[5] M. Braglia, MAFMA: multi-attribute failure mode analysis, International Journal of Quality & Reliability Management 17 (9) (2000) 1017–1033.

[6] M. Braglia, M. Frosolini, R. Montanari, Fuzzy criticality assessment model for failure modes and effects analysis, International Journal of Quality & Reliability Management 20 (4) (2003) 503–524.

[7] M. Braglia, M. Frosolini, R. Montanari, Fuzzy TOPSIS approach for failure mode, effects and criticality analysis, Quality and Reliability Engineering International 19 (2003) 425–443.

[8] C.L. Chang, C.C. Wei, Y.H. Lee, Failure mode and effects analysis using fuzzy method and grey theory, Kybernetes 28 (1999) 1072-1080.

[9] C.L. Chang, P.H. Liu, C.C. Wei, Failure mode and effects analysis using grey theory, Integrated Manufacturing Systems 12 (3) (2001) 211–216

[10] A. Charnes, W.W. Cooper, Programming with fractional function, Naval Research Logistics Quarterly 9 (1962) 181–185.

[11] A. Charnes, W.W. Cooper, E. Rhodes, Measuring the ef<sup>fi</sup>ciency of decision making units, European Journal of Operational Research 2 (1978) 429–444.

[12] K.S. Chin, A. Chan, J.B. Yang, Development of a Fuzzy FMEA based product design system, International Journal of Advanced Manufacturing Technology 36 (7–8) (2008) 633–649.

[13] K.S. Chin, Y.M. Wang, G.K.K. Poon, J.B. Yang, Failure mode and effects analysis using a group-based evidential reasoning approach, Computers & Operations Research 36 (6) (2009) 1768–1779.

[14] R. Dyson, F. Glover, Y. Ijiri, A. Whinston, T. Sueyoshi, New concepts, methodologies and algorithms for business education and research in the 21st century, Decision Support Systems (2009), doi:10.1016/j.dss.2009.06.001.

[15] A. Emrouznejad, B.R. Parker, G. Tavares, Evaluation of research in ef<sup>fi</sup>ciency and productivity: a survey and analysis of the <sup>fi</sup>rst 30 years of scholarly literature in DEA, Socio-Economic Planning Sciences 42 (3) (2008) 151–157.

[16] P.A.A. Garcia, R. Schirru, P.F. Frutuoso, E. Melo, A fuzzy data envelopment analysis approach for FMEA, Progress in Nuclear Energy 46 (3–4) (2005) 359–373.

[17] W. Gilchrist, Modelling failure modes and effects analysis, International Journal of Quality & Reliability Management 10 (5) (1993) 16–23.

[18] A.C.F. Guimarães, C.M.F. Lapa, Effects analysis fuzzy inference system in nuclear problems using approximate reasoning, Annals of Nuclear Energy 31 (1) (2004) 107–115.

[19] A.C.F. Guimarães, C.M.F. Lapa, Fuzzy inference to risk assessment on nuclear engineering systems, Applied Soft Computing 7 (2007) 17–28.

[20] C. Kao, S.N. Hwang, Ef<sup>fi</sup>ciency measurement for network systems: IT impact on <sup>fi</sup>rm performance, Decision Support Systems (2009), doi:10.1016/j.dss.2009.06.002.

[21] Y. Li, X. Liao, Decision support for risk analysis on dynamic alliance, Decision Support Systems 42 (4) (2007) 2043–2059.

[22] M. Mannino, S.N. Hong, I.J. Choi, Ef<sup>fi</sup>ciency evaluation of data warehouse operations, Decision Support Systems 44 (4) (2008) 883–898.

[23] R.E. Moore, Method and Application of Interval Analysis, SIAM, Philadelphia, 1979.

[24] E.W.T. Ngai, F.K.T. Wat, Fuzzy decision support system for risk analysis in ecommerce development, Decision Support Systems 40 (2) (2005) 235–255.

[25] A. Pillay, J. Wang, Modi<sup>fi</sup>ed failure mode and effects analysis using approximat reasoning, Reliability Engineering & System Safety 79 (2003) 69–85.

[26] T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

[27] N.R. Sankar, B.S. Prabhu, Modi<sup>fi</sup>ed approach for prioritization of failures in a system failure mode and effects analysis, International Journal of Quality & Reliability Management 18 (3) (2001) 324–335.

[28] G.A. Shafer, Mathematical Theory of Evidence, Princeton University Press, Princeton, 1976.

[29] D.H. Stamatis, Failure Mode and Effect Analysis: FMEA from Theory to Execution, ASQC Quality Press, Milwaukee, Wisconsin, 1995.

[30] K.M. Tay, C.P. Lim, Fuzzy FMEA with a guided rules reduction system for prioritization of failures, International Journal of Quality & Reliability Management 23 (8) (2006) 1047–1066.

[31] Y.M. Wang, R. Greatbanks, J.B. Yang, Interval ef<sup>fi</sup>ciency assessment using data envelopment analysis, Fuzzy Sets and Systems 153 (2005) 347–370.

[32] Y.M. Wang, K.S. Chin, J.B. Yang, Measuring the performances of decision-making units using geometric average efficiency Journal of the Operational Research Society 58 (2007) 929–937.

[33] Y.M. Wang, K.S. Chin, G.K.K. Poon, A data envelopment analysis method with assurance region for weight generation in the analytic hierarchy process, Decision Support Systems 45 (4) (2008) 913–921.

[34] Y.M. Wang, K.S. Chin, G.K.K. Poon, J.B. Yang, Risk evaluation in failure mode and effects analysis using fuzzy weighted geometric mean, Expert Systems with Applications 36 (2) (2009) 1195–1207.

[35] K. Xu, L.C. Tang, M. Xie, S.L. Ho, M.L. Zhu, Fuzzy assessment of FMEA for engine systems, Reliability Engineering and System Safety 75 (2002) 17–29.

[36] Z. Yang, S. Bonsall, J. Wang, Fuzzy rule-based Bayesian reasoning approach for prioritization of failures in FMEA, IEEE Transactions on Reliability 57 (3) (2008) 517–528.

![](/api/attachments/C78MSGZ7/fulltext/images/b86a5e055bdeabf3bc33f1d111d5640ceb513809627ceac42f1c599253400a40.jpg)

Kwai-Sang Chin is an associate professor at the Department of Manufacturing Engineering and Engineering Management, City University of Hong Kong. He is a Charter Engineer in U.K., a Registered Professional Engineer in Hong Kong, and Fellow Member of the American Society for Quality, Hong Kong Society for Quality and Hong Kong Quality Management Association. He is also the Programme Leader of BEng Total Quality Engineering in the Department. He maintains intensive collaboration with industries through various consultancy work, training courses and industrial projects. His current research interests are ‘Quality Management Strategies Beyond ISO9000’ and ‘Decision Support Methodologies/Systems for New Product Innovations and Development'. He has published a significant number of papers in peer reviewed journals such as JEEF Transactions on Engineering Management, IEEE Transactions on Fuzzy Systems, European Journal of Operational Research, Decision Support Systems, Information Sciences, Expert Systems with Applications, International Journal of Production Research, International Journal of Quality and Reliability Management, Industrial Management and Data Systems, International Journal of Advanced Manufacturing Technology, and the like

![](/api/attachments/C78MSGZ7/fulltext/images/355497058d9a8a5938d11ae03501210da413c87463c0c749979d299a358f8836.jpg)

Ying-Ming Wang is a Professor of Management Science in the School of Public Administration, Fuzhou University, PR China. He received his BEng degree in Industrial Electric Automation from Jiangsu University of Science and Technology in 1984, MEng and PhD degrees both in Systems Engineering, respectively, from Huazhong University of Science and Technology in 1987 and Southeast University in 1991. His research interests include multiple attribute decision analysis (MADA), data envelopment analysis (DEA), analytic hierarchy process (AHP), evidential reasoning (ER) approach, quality function deployment (QFD), and failure mode and effects analysis (FMEA). He has published 169 academic papers in a wide variety of peer reviewed journals such as European Journal of Operational Research, Decision Support Systems, Fuzzy Sets and Systems, International Journal of Approximate Reasoning, Computers and Operations Research, Information Sciences, Expert Systems with Applications, Journal of the Operational Research Society, Computers & Industrial Engineering, Journal of Computational and Applied Mathematics, Applied Mathematical Modelling, Mathematical and Computer Modelling and so on.

![](/api/attachments/C78MSGZ7/fulltext/images/83a206153a80c039a6be4bb0ebefa07c4e6ac6b76d539cc48cf9c371c021a7e8.jpg)

Gary Ka Kwai Poon is currently a lecturer at the Department of Manufacturing Engineering and Engineering Management, City University of Hong Kong, teaching Quality and Reliability Engineering, and Environmental Management. His research interests include the characterization of electronics manufacturing processes, quality and environmental management. He is a Senior Member of the Institute of Industrial Engineers (IIE), Member of the Institute of Engineering and Technology (IET) and the American Society of Quality (ASQ), and a Chartered Engineer.

![](/api/attachments/C78MSGZ7/fulltext/images/e29c95280c217f2f6238d1e7fb9cb811590ce4e9c060cf1e28e11c26cfae5963.jpg)

Jian-Bo Yang received the BEng and MEng degrees in control engineering from the North Western Polytechnic University, Xi'an China in 1981 and 1984 respectively and the PhD degree in systems engineering from Shanghai Jiao Tong University, Shanghai, China, in 1987. He is currently the Chair Professor of decision and system sciences and the Director of the Decision Sciences Research Centre in the Manchester Business School, the University of Manchester, U.K. He is also a Specially Appointed Professor of the Hefei University of Technology, Hefei, China. Prior to his current appointment, he was a Faculty Member with the University of Mancheste Institute of Science and Technology (1998–2004, 1990), the University of Birmingham, U.K. (1995–1997), the Universit of Newcastle upon Tyne, Newcastle, U.K. (1991–1995), and Shanghai Jiao Tong University (1987–1989). In the past two decades, he has been conducting research in multiplecriteria decision analysis under uncertainty, multiple-objective optimization, intelligent decision support systems, hybrid quantitative and qualitative decision modeling using techniques from operational research, arti<sup>fi</sup>cial intelligence, and systems engineering and dynamic system modeling, simulation, and control for engineering and management systems. His current applied research includes design decision-making, risk modeling and analysis, production planning and scheduling, quality modeling and evaluation, supply chain modeling and supplier assessment, and the integrated evaluation of products, systems, projects, policies, etc. His current research has been supported by the EPSRC, EC, DEFRA, SERC, HKRGC, NSFC, and industry. He has published widely and developed several software packages in these areas including the Windows-based intelligent decision system via evidential reasoning.

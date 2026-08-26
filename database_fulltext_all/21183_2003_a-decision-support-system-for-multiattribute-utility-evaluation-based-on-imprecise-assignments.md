---
otero_id: 21183
otero_key: "KW5SCRS8"
title: "A decision support system for multiattribute utility evaluation based on imprecise assignments"
authors: "Antonio Jiménez; Sixto Rı́os-Insua; Alfonso Mateos"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00137-9"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for multiattribute utility evaluation based on imprecise assignments

Antonio Jime´nez \*, Sixto Rı´os-Insua, Alfonso Mateos

Department of Artificial Intelligence, School of Computer Science, Madrid Technical University, Campus de Montegancedo s/n, 28660 Boadilla del Monte, Madrid, Spain

Accepted 3 July 2002

## Abstract

This paper describes a decision support system based on an additive or multiplicative multiattribute utility model for identifying the optimal strategy. This is intended to allay many of the operational difficulties involved in assessing and using multiattribute utility functions. The system admits imprecise assignments for weights and utilities and uncertainty in the multiattribute strategies, which can be defined in terms of ranges for each attribute instead of single values. Inputs can be subjected to different sensitivity analyses, permitting users to test the robustness of the ranking of the strategies and gain insight into and confidence about the final solution. An application of the system to the restoration of a contaminated lake is illustrated throughout the paper.

<sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Decision support system; Multiattribute utility functions; Imprecision; Sensitivity analysis

## 1. Introduction

Many complex decision-making problems have multiple objectives, and these multiple objectives may be conflicting in the sense that, once dominated strategies or alternatives have been discarded, further achievement in terms of one objective can occur only at the expense of some achievement of another objective. Therefore, preference trade-offs between differing degrees of achievement of one objective and another must be taken into account by the decision maker (DM). Also, real problems are usually plagued with uncertainty, and it is impossible to predict with certainty what the consequences of each strategy under consideration will be. Formal analysis is required because it is very difficult to consider the above complexities informally in the mind.

The goal of decision analysis (DA) is to structure and simplify the task of making hard decisions as well and as easily as the nature of decision permits [3]. DA is concerned with multiple conflicting objectives for many complex, real-world decision-making problems and is developed on the assumption that the alternatives will appeal to the expert, depending on:

 the likelihood of the possible consequences of each alternative,

 expert preferences concerning the possible consequences.

What makes DA unique is the form in which these factors are quantified and formally incorporated into the problem analysis. Existing information, collected data, models and professional judgements are used to quantify the likelihoods of a range of consequences, while utility theory is used to quantify preferences.

The usual or traditional approach to DA calls for single or precise values for the different model inputs, i.e., for the weight and utility assessments, as well as for the multiattributed consequences of the generated strategies. Here, however, we develop a system based on a less demanding approach for the DM, who will be able to provide ranges or value intervals instead of single values. These ranges will be later used in different sensitivity analyses (SA). Thus, the system will output the ranking of the strategies based on their precise utilities. However, it also provides a utility interval for each strategy based on their input values for each attribute, which gives a better understanding of the ranking. It also provides weight stability intervals for the weights of the utility function, and it is possible to change any value or any extreme value in any of the ranges of the utilities, weights or strategies at any time the system will then automatically recalculate the ranking of the alternatives. All the information about ranges in weights and utilities will be considered in the SA with the objective of aiding the DM to choose the most preferred strategy as well as to reduce the set of strategies of interest.

The system that we describe is an extension of the evaluation module developed for the MOIRA system (Model-based computerized system for management support to Identify optimal strategies for restoring Radionuclide contaminated Aquatic ecosystems and drainage areas) [2,21]. After testing on several real scenarios, this system is now being used in the European COMETES project (implementing COmputerized METhodologies to evaluate the EffectivenesS of countermeasures for restoring radionuclide contaminated fresh water ecosystems) to aid in the restoration of highly contaminated aquatic ecosystems in some countries of the former Soviet Union. We are participating as the team decision analysts. For the sake of brevity, we illustrate the different steps by applying the extended system, highlighting its novelties, to lake Øvre Heimdalsvatn, located in Oppland county (Norway). This is a small subalpine lake with a mean depth of 4.7 m, maximum depth of 13 m, surface area of $0 . 7 8 \ \mathrm { k m } ^ { 2 }$ and a catchment area of $2 3 . 6 \ \mathrm { k m } ^ { 2 } .$ The highest point of the catchment area is 1843 m above sea level (a.s.l.), while the lake itself is at 1090 m a.s.l. The mean annual precipitation is 800 mm. This lake has been thoroughly studied (see Ref. [23]). After the Chernobyl accident, the lake was contaminated with a fallout of $1 3 0 ~ \mathrm { k B q / m } ^ { 2 }$ of $^ { 1 3 7 } \mathrm { C s } .$ which, in principle, required no countermeasures. Also, the low utilization of the lake by people makes individual and collective doses very low, and countermeasures turned out not to be cost-effective, because the doses that could have been averted were always very low. However, some alternative strategies were analyzed with the objective of testing the evaluation procedure.

We can divide DA into four steps: structuring the problem (which includes building a value hierarchy, specifying objectives and attributes for the strategies); identifying the feasible strategies, their impact and uncertainty (if necessary); quantifying preferences (which includes the assessment of the single attribute utility functions, as well as the value trade-offs); and evaluation of countermeasures and sensitivity analysis (SA). According to these stages, we have divided the paper into the following five sections where we describe the steps mentioned above and, finally, provide some conclusions.

## 2. Structuring the value hierarchy

There are several benefits to be gained from using a hierarchy to model problems of this sort [4]. The advantages of an objectives hierarchy are:

 It helps to ensure that there will be no big gaps (missing objectives) at lower levels, since such gaps should be fairly obvious.

 Major objectives provide a basis for defining lower-level objectives, since they are a means for achieving the higher-level ones.

 Lower-level objectives are more specific. Therefore, it is easy to identify reasonable attributes for these objectives.

![](/api/attachments/KW5SCRS8/fulltext/images/a4c1ef5a40286e77bbbcdb4adfe94b9812abf3becfe8415e3223139c76324ebf.jpg)  
Fig. 1. Objectives hierarchy for the restoration problem.

 Situations where redundancy or double-counting could easily occur can be identified.

 Attributes must be defined only for objectives at the bottom of any branch of the hierarchy.

 The hierarchy provides a basis upon which to develop and appraise screening criteria.

DA involves establishing attributes to indicate to what extent objectives are achieved. Attributes will be either selected from existing measures, such as costs, or constructed for a specific situation. The process of defining these attributes should be logically consistent and systematic. At the same time, it is inherently subjective and must encompass professional judgements, knowledge and experience. Attributes can be categorized according to two features: how they measure achievement and the scale type. For some basic properties related to the set of attributes, see Ref. [12].

In the software system that we discuss in this paper, an objectives hierarchy can have up to 100 nodes, and the necessary objective levels for consideration can be defined. Fig. 1 shows the hierarchy constructed by the experts for the lake restoration problem, which displays five levels and seven lowestlevel objectives. Note that due to the system flexibility, it will be possible to add or to drop a node at any time if deemed appropriate by the DM.

![](/api/attachments/KW5SCRS8/fulltext/images/981533ae922dbd9987a9d9dd3788badebe846c33b5a276d692e00d5df755c570.jpg)  
Fig. 2. Health impact node information of the objectives hierarchy.

The software has a facility for defining each node in the hierarchy so that other users can gain a better understanding of a particular node’s role in the constructed hierarchy. For example, if the decision maker was unclear about the definition of the subgoal Health Impact, clicking on the corresponding node in Fig. 1 would invoke a screen similar to Fig. 2.

An attribute associated with each lowest-level objective will be next considered and used as a measure of the effectiveness of each strategy. They can be measured on natural or constructed scales. We consider natural scales for all attributes (the respective units are provided at the end of each definition), except for cost of image, which has a constructed subjective scale. Each of the seven attributes is defined below:

1. Lake ecosystem index $( X _ { 1 } )$ . The lake ecosystem index is a measure of the health of the ecosystem in aquatic environments. It summarizes the status of important ecosystem variables affecting phytoplankton, benthos and fish. It is evaluated by ad hoc MOIRA models [9].

2. Dose to critical individuals (X ). The effective dose received by individuals belonging to a critical group living in the area, drinking water and eating aquatic food and food grown on land irrigated with water from the contaminated body of water. It is evaluated by the MOIRA dose model.

3. Collective dose (X<sub>3</sub>). The collective effective dose received by the entire population through any of the exposure pathways due to the contaminated body of water. It is a measure of the increased risk of serious latent health effects. It is evaluated by the MOIRA dose model.

4. Duration of restrictions $( X _ { 4 } )$ . In the event of restrictions on water consumption and use, the duration of the restrictions. This is strategy dependent.

5. Cost to economy $( X _ { 5 } )$ . The direct economic impact of the restrictions, either in terms of the cost of the food affected by bans or in terms of loss of production (e.g., share in the fall of the Gross Domestic Product). This is evaluated by MOIRA’s economic model.

Table 1  
Attributes for evaluating countermeasures

<table><tr><td rowspan="2">Attribute</td><td rowspan="2">Measure (units)</td><td colspan="2">Level</td></tr><tr><td>Worst</td><td>Best</td></tr><tr><td> $X_{1}$ : Lake ecosystem index</td><td>LEI</td><td>5.00</td><td>1.00</td></tr><tr><td> $X_{2}$ : Radiation dose to critical individuals</td><td>milliSv</td><td>2.47</td><td>0.76</td></tr><tr><td> $X_{3}$ : Collective radiation dose</td><td>mSv × person</td><td>72.3</td><td>20.30</td></tr><tr><td> $X_{4}$ : Duration of fishing ban</td><td>months</td><td>36</td><td>0</td></tr><tr><td> $X_{5}$ : Cost of fish consumption ban</td><td>euros ×  $10^{2}$ </td><td>426.00</td><td>0.00</td></tr><tr><td> $X_{6}$ : Cost of application</td><td>euros ×  $10^{2}$ </td><td>702.00</td><td>0.00</td></tr><tr><td> $X_{7}$ : Cost of image</td><td>constructed scale</td><td>1.00</td><td>0.00</td></tr></table>

6. Cost of application $( X _ { 6 } )$ . In the case of remedial countermeasures (physical or chemical), this represents the direct cost of the application: manpower, consumables, equipment needed for application, management of waste generated, etc. It is evaluated by MOIRA’s economic model.

7. Cost of image (X<sub>7</sub>). On a subjective scale (0 – 1), this would represent the indirect costs associated to the different strategies, which can be perceived by the public differently, due to market reluctance concerning even uncontaminated products, a drop in tourism, etc.

For this last attribute, we would then subjectively assign consequences, ranked from the best (1) to the worst (0), to several identification points or intervals along this scale. There are, of course, difficulties in using this subjectively defined attribute scale, and due to the context, it will be important to go to creative, fanciful extremes in order to get an objective base.

Table 1 shows the above attributes, which also includes their units and relevant ranges, obtained for the alternatives analyzed later in our case.

## 3. Identifying feasible strategies

Next, feasible remedial strategies must be identified and we have to establish how to measure these strategies in terms of attributes. The setting is as follows: the strategies $S _ { j } , ~ j { = } 1 , . . . . , ~ m$ , have been identified, and an objectives hierarchy with attributes $X _ { i } , i = 1 , . . . , n .$ , associated with the lowest-level objectives has been constructed. Thus, the consequences of a decision strategy $S _ { j }$ can be described under certainty by the vector $\mathbf { x } ^ { j } { = } ( x _ { 1 } ^ { j } . . . . , x _ { n } ^ { j } )$ , where $x _ { i } ^ { j }$ is a level of attribute $X _ { i }$ for $S _ { j }$ and under uncertainty by a vector of ranges $[ \mathbf { x } ^ { \mathrm { L } j } , \mathbf { x } ^ { \mathrm { U } j } ] { = } ( [ x _ { 1 } ^ { \mathrm { L } j } , x _ { 1 } ^ { \mathrm { U } j } ] , . . . , [ x _ { n } ^ { \mathrm { L } j } , x _ { n } ^ { \mathrm { U } j } ] )$ , where $x _ { i } ^ { \mathrm { L } j }$ and $x _ { i } ^ { \mathrm { U } j }$ are the lower (L) and upper (U) levels of attribute $X _ { i }$ for $S _ { j }$ . In the first case, when there are no uncertainties surrounding the problem, this means that the impact for each strategy is known and, thus, the task of selecting the best strategy is reduced to selecting the best $\mathbf { x } ^ { j } .$ . In the second case, the DM specifies a uniform distribution on $[ x _ { i } ^ { \mathrm { L } j } , x _ { i } ^ { \mathrm { U } j } ]$ , instead of providing a point estimate. The system then ranks using the mean, or midpoint, of the range as an input to the ranking procedure. As we shall see in Section $^ { 5 , }$ additional information from the ranges $[ x _ { i } ^ { \mathrm { L } j } , x _ { i } ^ { \mathrm { U } j } ]$ will be provided for the DM and incorporated into the evaluation. Note that both possibilities can be taken into account simultaneously, because the case under certainty will be a particular case of the one under uncertainty if we provide ranges with equal extreme values [14].

In the event of a radioactive contamination of aquatic ecosystems and their drainage areas, there are several options available to management, ranging from chemical treatment of water bodies to fishing bans and, even, restrictions on human movement. Potential actions can be broadly grouped into three main categories: chemical, physical and social. A combination of actions may be the optimal strategy in some cases. A further option is, of course, not to take any remedial actions, although this may also have significant socioeconomic repercussions. Most countermeasures are applicable to all types of aquatic ecosystems, although their efficiency may vary considerably. To facilitate alternative generation, MOIRA includes a countermeasure database from which the DMs may choose applicable countermeasures, or any combination of these, for the case under study. In our example, a set of nine strategies has been analyzed, combining chemical countermeasures with fishing ban so as to reduce the radiological and environmental impact (see Table 2).

Finally, Table 3 shows the matrix of impacts, which summarizes the results of running the different MOIRA submodels for each of the nine strategies under study [16]. However, the ‘‘cost to economy’’ $( X _ { 5 } )$ was quantified from information about the site (database information), the ‘‘cost of application’’ (X<sub>6</sub>)

Table 2 Set of strategies

<table><tr><td>Strategy</td><td>Description</td><td>Strategy</td><td>Description</td></tr><tr><td> $S_{1}$ </td><td>No action</td><td> $S_{6}$ </td><td>Potash treatment</td></tr><tr><td> $S_{2}$ </td><td>Fishing ban (1st year)</td><td> $S_{7}$ </td><td>Potash + fishing ban (3 years)</td></tr><tr><td> $S_{3}$ </td><td>Fishing ban (2nd, 3rd and 4th year)</td><td> $S_{8}$ </td><td>Fertilizing</td></tr><tr><td> $S_{4}$ </td><td>Lake liming</td><td> $S_{9}$ </td><td>Fertilizing + fishing ban (3 years)</td></tr><tr><td> $S_{5}$ </td><td>Liming + fishing ban (3 years)</td><td></td><td></td></tr></table>

was obtained directly from past experience and the attribute ‘‘cost of image’’ (X<sub>7</sub>) was assigned by a direct estimate made by the team members making the assessment.

## 4. Quantifying preferences

Quantifying preferences involves assessing the DM’s single attribute utility functions and the relative importance of each one. Both will be used later to evaluate the strategies through a multiattribute utility function. First, we consider the utility assessment, and then we provide the weight elicitation.

## 4.1. Assessment of component utility functions

The utility functions can be assessed, using three different procedures depending on the level of knowledge and the characteristics of the attribute under consideration (see Fig. 3).

The certainty equivalent (CE) method/probability equivalent (PE) method should be applied for natural or subjective attributes and when the DM has little knowledge about or experience with the topic. This assessment approach involves answer to indifference conditions between lotteries and sure amounts, and does not require the DM to indicate the form of the utility function. The procedure is based on the use of two slightly modified standard procedures for utility assessment. Several authors (see, e.g., Refs. [10,11,15]) have suggested that elicited utility functions are generally method dependent, and bias and inconsistencies may be generated in the elicitation process. To overcome such objections, von Nitzsch and Weber [24] suggest combining two methods to tackle these problems: the probability equivalent method and the certainty equivalent method (see Ref. [7]). The original assessment methodologies require specification of a single number in response to each stimulus (see Refs. [18,24]). We relax this requirement and allow the DM to enter an indifference interval, which yields a family of candidate utility functions as shown in Fig. 4. Each assessment approach yields an indifference interval, and the intersection of these ranges indicates where the DM was consistent in defining her preferences. Should such intersections be empty for an interval, the DM would be inconsistent and her preferences should be reelicited. The process ends when a consistent range is provided.

Table 3 Matrix of impacts

<table><tr><td rowspan="2">Strategy</td><td colspan="7">Attributes</td></tr><tr><td> $X_1$ </td><td> $X_2$ </td><td> $X_3$ </td><td> $X_4$ </td><td> $X_5$ </td><td> $X_6$ </td><td> $X_7$ </td></tr><tr><td> $S_1$ </td><td>[5.0,5.0]</td><td>[2.20,2.47]</td><td>[64.0,72.3]</td><td>[0,6]</td><td>[0,0]</td><td>[0,0]</td><td>[0.0,0.0]</td></tr><tr><td> $S_2$ </td><td>[4.0,5.0]</td><td>[1.80,2.30]</td><td>[56.0,65.0]</td><td>[0,10]</td><td>[130,170]</td><td>[0,25]</td><td>[0.0,0.0]</td></tr><tr><td> $S_3$ </td><td>[3.5,5.0]</td><td>[0.80,1.30]</td><td>[21.0,27.0]</td><td>[30,36]</td><td>[380,426]</td><td>[10,50]</td><td>[0.0,0.0]</td></tr><tr><td> $S_4$ </td><td>[1.5,2.5]</td><td>[2.20,2.40]</td><td>[61.0,70.0]</td><td>[0,6]</td><td>[0,40]</td><td>[130,190]</td><td>[0.7,0.7]</td></tr><tr><td> $S_5$ </td><td>[1.5,2.6]</td><td>[0.80,1.30]</td><td>[21.0,29.0]</td><td>[30,36]</td><td>[390,426]</td><td>[110,160]</td><td>[0.7,0.7]</td></tr><tr><td> $S_6$ </td><td>[1.8,2.7]</td><td>[1.90,2.30]</td><td>[56.0,61.0]</td><td>[0,5]</td><td>[0,35]</td><td>[610,702]</td><td>[0.6,0.6]</td></tr><tr><td> $S_7$ </td><td>[1.8,2.6]</td><td>[0.76,1.30]</td><td>[20.3,29.0]</td><td>[32,36]</td><td>[406,426]</td><td>[665,702]</td><td>[0.6,0.6]</td></tr><tr><td> $S_8$ </td><td>[1.0,1.6]</td><td>[2.06,2.47]</td><td>[65.0,72.3]</td><td>[0,3]</td><td>[0,35]</td><td>[112,168]</td><td>[1.0,1.0]</td></tr><tr><td> $S_9$ </td><td>[1.0,1.8]</td><td>[0.78,1.40]</td><td>[20.3,29.0]</td><td>[34,36]</td><td>[420,426]</td><td>[110,155]</td><td>[1.0,1.0]</td></tr></table>

The system uses graphical representations of the assessed utility ranges to test consistency. It suggests possible inconsistencies and possible adjustments for the values that need to be reelicited from the DM.

However, the MOIRA system has a library of standard utility functions loaded with a utility functions file, which can be used by nonexperts in the evaluation process.

In the CE method, the DM is asked to give certainty equivalent intervals for three lotteries (Fig. 5), whereas probability intervals of lotteries for given sure amounts must be provided in the PE method.

Consistency checks are run to verify the bounds assessed for the specific certainty equivalence and probability equivalence methods. If the two intervals provided by the DM are not consistent with respect to the implied utility function, the system suggests possible changes in probability (PE method) or sure amount (CE method) intervals until consistency is attained.

The second procedure available for assessing utility functions is to construct piecewise linear utility functions. This will be useful when there is a natural or subjective attribute and also deep and precise knowledge about the attribute. The family of utility functions will be constructed in this case by joining up to four linear segments between the best and the worst values for upper and lower values of the assignments. So, the user is asked to provide intermediate intervals (up to three). If no intermediate points are specified, then the result will be a single linear function. Fig. 6 shows the constructed class of piecewise linear utility functions for the attribute ‘‘cost of application’’ (X ).

![](/api/attachments/KW5SCRS8/fulltext/images/a3ba124a5d241c1776bed7bc79573aa7292dcb839472749ed0ef30e6c1534f05.jpg)  
Fig. 3. Visualizing the three methods for utility assessment.

![](/api/attachments/KW5SCRS8/fulltext/images/66ecce5dd4498820d3e57d363bf7094b53ccffeebaa1793c0520dde93e8b05b5.jpg)  
Fig. 4. Consistency between the two utility assessment methods.

The third procedure applies when the DM decides to use a subjective scale without defining a utility function, implemented in the system by means of a thermometer scale [8], suitable for determining the impact of each strategy on a given subjective attribute rather than a utility function, because it is difficult to ascertain what the value of each strategy is for the respective subjective attribute. For subjective scales, the DM will enter utility intervals by hand using scrollbars, as shown in Fig. 7. This figure shows the minimum utilities for the nine strategies for the attribute ‘‘cost of image’’ (X ). Thus, for example, it could be very difficult for the DM to tell what the value of the strategy No action will be for the attribute cost of image. However, the DM can provide minimum and maximum utilities on a scale from 0 to 1, where 0 = worst and 1 = best, just by thinking about how good or bad it should be with respect to the attribute in question.

## 4.2. Assessment of weights

The very essence of multicriteria problems means that it is usually necessary to use some means to account for the relative importance of criteria. There are two main ways of doing this, the first is preemptive ordering of attributes and the second is the use of attribute weights.

![](/api/attachments/KW5SCRS8/fulltext/images/f17044ba3b53c38651c475f802103f59a1f3c86e04f5b3eae033dac74a02519e.jpg)  
Fig. 5. The CE method.

![](/api/attachments/KW5SCRS8/fulltext/images/069508412cdd9e14c608aa1122a662d1584b10fd1b4fa0b4da10f14b53abc218.jpg)  
Fig. 6. The piecewise linear utility function for the attribute cost of application.

A pre-emptive ordering means that you can consider the options for one attribute at a time, starting with ‘‘the most important’’, possibly in conjunction with some goal or aspiration level [1].

The use of attribute weights is more widespread. In some approaches, for example, methods using multiattribute value functions, the weights are well defined as scaling values, which define acceptable trade-offs between attributes. Attribute weights are indicators of the influence of the individual criteria on the decision. Weights or scaling factors are needed for each objective of the hierarchy, facilitating global sensitivity analysis.

In our system, we have provided two procedures for assessing weights. The first procedure is based on trade-offs [12] among the respective attributes of the lowest-level objectives stemming from the same objective. The DM is asked to give an interval of probabilities such that he/she is indifferent with respect to a lottery and a sure consequence.

As in the case of utility elicitations, we assume imprecision allowing the DM to provide an interval, rather than a single value, and the system computes the respective precise weights w<sub>i</sub>. Note that the user can specify identical interval endpoints, which should mean that the DM is considering a precise value. This procedure will be more suitable for the low-level objectives in the hierarchy because weight assessment involves a more specific area of knowledge. We begin with the objectives at the low levels of the hierarchy and then we continue the assessment in ascending order of the hierarchy.

The second procedure, perhaps more suitable for upper level objectives that could be more political, is based on direct assessment. Here, the DM is asked, as before, to provide weight intervals. A precise value is provided if the user specifies identical interval endpoints. Fig. 8 illustrates a possible assignment to the ‘‘overall objective’’ (the root of the objectives hierarchy).

![](/api/attachments/KW5SCRS8/fulltext/images/edb1e94dbb3bfebcab58cf35633a370eb8f85b1a38df630f06df820ffeca10aa.jpg)  
Fig. 7. Subjective scale utilities for the nine strategies.

![](/api/attachments/KW5SCRS8/fulltext/images/f6060eb37a60a56386df6c5b2aefa63f8d2d2368033669b8115c67320ee940cb.jpg)  
Fig. 8. Weight assignment based on tradeoffs for the second level of the hierarchy.

Note that, again, it is possible to provide minimum and maximum values to get imprecise assessment by means of weight intervals. Table 4 and Fig. 9 show the weight intervals and the (precise) normalized average intervals for the attributes and objectives, which are automatically computed by the system by means of the formulas (see Refs. [13,21]),

$$
\begin{array}{l} k _ {i} = \frac {\omega_ {i} ^ {\mathrm{L}} + \omega_ {i} ^ {\mathrm{U}}}{ \sum_ {i} (\omega_ {i} ^ {\mathrm{L}} + \omega_ {i} ^ {\mathrm{U}})}, \\ k _ {i} ^ {\mathrm{L}} = \frac {k _ {i} \omega_ {i} ^ {\mathrm{L}}}{(\omega_ {i} ^ {\mathrm{L}} + \omega_ {i} ^ {\mathrm{U}}) / 2} \quad \text { and } k _ {i} ^ {\mathrm{U}} = \frac {k _ {i} \omega_ {i} ^ {\mathrm{U}}}{(\omega_ {i} ^ {\mathrm{L}} + \omega_ {i} ^ {\mathrm{U}}) / 2} \end{array}
$$

where $\omega _ { i } ^ { \mathrm { ~ L ~ } }$ and $\omega _ { i } ^ { \mathrm { ~ U ~ } }$ are the lower and upper bounds for the weights provided by the DM, as shown in Fig. 8.

Direct assignment will normally be used at the higher levels of the tree and trade-offs based weight calculation at the lowest levels. Note that when the system is opened, the starting point is equally weighted objectives, but any interval weight or precise weight can be changed and the system automatically takes care of how these changes should be propagated in the objectives hierarchy and recalculates the overall utility for each strategy. The normalized weight intervals together with the value intervals will be used in SA to gain insight into and confidence in the ranking of the strategies, and as an aid in reducing the set of alternatives if possible.

Normalized weights and weight intervals for the second level of the objectives hierarchy

<table><tr><td>Objective</td><td>Normalized weight,  $k_{i}$ </td><td>Normalized weight interval,  $[k_{i}^{\text{L}}, k_{i}^{\text{U}}]$ </td></tr><tr><td>Environmental impact</td><td>0.1447</td><td>[0.100,0.188]</td></tr><tr><td>Social impact</td><td>0.4339</td><td>[0.289,0.578]</td></tr><tr><td>Economic impact</td><td>0.4213</td><td>[0.314,0.528]</td></tr></table>

## 5. Evaluating alternatives

This step involves evaluating each alternative by means of a multiattribute utility model to help identify the best one. Each strategy will be characterized by its evaluations in the n relevant attributes. Multiattribute utility theory provides methods and procedures to do this. We assess a utility function u, which assigns a number u(x) to each possible consequence x. This utility function is a representation of the expert’s attitude towards risk, value trade-offs among different impacts and groups of people, and preferences for impact over time.

The main concepts of multiattribute utility theory concern independence conditions. Subject to a variety of these conditions, the assessment of u can be broken down into parts, each of which is easier to handle than the whole. Our aim is to find simple functions $f ,$ $u _ { 1 } , . . . , u _ { n }$ such that $u ( x _ { 1 } , . . . , x _ { n } ) { = } f ( u _ { 1 } ( x _ { 1 } ) , . . . , u _ { n } ( x _ { n } ) )$ Then the assessment of u is reduced to the assessment of f and $u _ { i } .$ The $u _ { i }$ are single-attribute functions. The form of f depends on the independence condition. The system permits two possible decompositions: (1) an additive decomposition given by the functional form

![](/api/attachments/KW5SCRS8/fulltext/images/95c191ad178deea638958739a6ec980eaa2020de421583dc26b9dbd2365e3bc9.jpg)  
Fig. 9. Visualizing weights for the second level objectives.

$$
u (S _ {l}) = \sum_ {i = 1} ^ {n} w _ {i} u _ {i} (x _ {i} ^ {l})\tag{1}
$$

where $\textstyle \sum _ { i = 1 } ^ { n } w _ { i } = 1$ , and a multiplicative function, given by the form

$$
\begin{aligned} u(S_{l}) = & \sum_{i = 1}^{n}w_{i}u_{i}(x_{i}^{l}) + w\sum_{\substack{i = 1\\ j > i}}^{n}w_{i}w_{j}u_{i}(x_{i}^{l})u_{j}(x_{j}^{l})\\ & +\dots +w^{n - 1}\prod_{i = 1}^{n}w_{i}u_{i}(x_{i}^{l}) \end{aligned}\tag{2}
$$

where $x _ { i } ^ { \ l }$ is the specific level of the attribute $X _ { i }$ for the alternative $S _ { l } , \ u _ { i }$ are the component utility functions for each evaluation measure and $w _ { i }$ are the weights or scaling constants for each component utility function. The additive decomposition (1) is appropriate when the additive independence condition is satisfied, while the multiplicative form (2) is appropriate when the weaker mutual utility independence condition holds [12].

If a multiplicative utility function is considered and some interval weights have been provided by the DM, the system will compute the range for the constant w by solving the equation $1 + w = \Pi _ { i = 1 } ^ { n } \big ( 1 + w w _ { i } \big )$ , for the lower and upper extremes of the weight intervals, respectively, providing an interval for w.

For our lake problem, we considered (1) to be a valid approach for the reasons described in Refs. [17,22], because nonlinearities in the marginal utility functions are adequately captured (using interpolation between at least three or four points) and the modelled objectives are close to additively independent. Thus, the global utility function is additive, and the utility of strategy $S _ { q }$ with consequences $\mathbf { x } ^ { q } { = } ( x _ { 1 } ^ { q } , . . . , x _ { 7 } ^ { q } )$ can be determined as follows

$$
u (x _ {1} ^ {q}, \dots , x _ {7} ^ {q}) = w _ {1} u _ {1} (x _ {1} ^ {q}) + \dots + w _ {7} u _ {7} (x _ {7} ^ {q})
$$

where the attribute weights are obtained by multiplying the respective weights of the objectives of each path from the root (global objective) to each leaf (attribute). As the evaluation process calls for precise utility functions for the evaluation of the strategies, the system provides fitted utility functions by taking the midpoints of the utility intervals of the intersection area for each $u _ { i }$ and then fitting natural cubic splines to these data points. Fig. 10 shows the fitted utility function for the attribute Ecosystem Index with range [1,5].

The set of strategies is automatically evaluated and ranked. The ranking can be displayed directly. The system provides a graphical representation with bars, which includes their overall utilities and ranking (see Fig. 11). The vertical lines on each bar represent the average utilities, while the extremes of the rectangles are the minimum and maximum utilities. These utilities are obtained from the mean, minimum and maximum strategy values, respectively. The system uses the minimum and maximum splines, which define the range of utility functions, or the respective subjective utilities, to compute the minimum and the maximum. The average utilities are obtained from the fitted splines and/or the subjective average utilities. The weight values for assessing these overall utilities are, for all three cases, the average attribute weights, obtained from the average weights of the upper level objectives.

![](/api/attachments/KW5SCRS8/fulltext/images/b196f2445a9d93475eb5698e821027e71ef668a185d088065ae44ff981f37ef7.jpg)  
Fig. 10. The fitted utility function for the attribute ecosystem index.

There are some other possible displays presenting useful information to the DM. Thus, it will be possible to visualize the objectives hierarchy with the weights assigned to each objective by selecting a strategy. Another display shows the interval and the normalized weights associated with each attribute, obtained from the weights of the top level objectives. The global weights (for the attributes) are represented both numerically (the normalized weights) and by a graph. Note that these global weights will sum 1.

Finally, it is possible to compare selected pairs of attributes for all the strategies by means of a graphical representation of the utility values for the chosen attributes of the different strategies under analysis. This would help the DM to compare the performance of the strategies for each pair of selected attributes, looking at which strategies are more important.

In our particular problem, the preferred option is strategy $S _ { 9 } ,$ that is, fertilizing combined with a fishing ban for the 2nd, 3rd and 4th years after the accident.

## 6. Sensitivity analysis

Sensitivity analysis, which essentially involves examining changes in the ranking, as a function of the input parameters (weights and utilities) varying within a reasonable range can give further insight into robustness of the recommendations. Some types of sensitivity analysis are described in Refs. [19,20], which introduce a framework for sensitivity analysis in multiobjective decision making. In Ref. [21], an introduction to sensitivity analysis in the MOIRA project is presented. Ref. [26] presents three novel types of sensitivity analysis for MCDM methods, and Ref. [25] assesses the weights-set to satisfy preference orders in alternatives.

![](/api/attachments/KW5SCRS8/fulltext/images/ce9c9b3dff944efa4806207a66ab7ad969f5aaa24ee2b842608dce041a22e1a4.jpg)  
Fig. 11. The ranked strategies with their utilities.

![](/api/attachments/KW5SCRS8/fulltext/images/53d79384b82b66073ddfd18ab134dcad21b58c606d63c49d9bd20a3aab68d12a.jpg)  
Fig. 12. Weight stability interval for social impact.

SA is usually performed by changing the weights or utilities and observing their impact on the ranking of alternatives [13]. Hence, if the DM makes a change to a weight or the normalized weight range, the system takes cares of how these changes should be propagated in the objective hierarchy and automatically recalculates the overall utility for each strategy and the resulting ranking.

Another way of performing SA involves assessing the interval in which a weight can vary maintaining a constant ratio among the other weights, without affecting the overall strategy ranking. Suppose that there is now a ranking of the given strategies and the DM chooses a node or leaf of the tree that has an associated weight. The system calculates the weight interval for this node/leaf, taking into account the updated weights for the objectives stemming from its predecessor, so that the ranking does not change, i.e., if the weight is changed and the new value is within the range, then the ranking will not change. However, if the new value is not within the range, the new ranking will be different to the previous one. Fig. 12 shows the weight stability interval for the objective ‘‘Environmental Impact’’ at the second level of the hierarchy. Note that the stability interval is [0.113,0.209], which means that if the DM changes the present value 0.149 to any value in the stability interval, the actual ranking of the strategies remains unchanged. Otherwise, the ranking changes and is computed by the system.

Finally, the system performs simulation techniques for SA. This kind of sensitivity analysis (see Refs.

![](/api/attachments/KW5SCRS8/fulltext/images/7b8072a809ebc914fc71236c4a4fc41e2eeef87dfd34bda0f31b6e377d1549f9.jpg)  
Fig. 13. Boxplot for the results of the simulation for the nine strategies considering random weights.

![](/api/attachments/KW5SCRS8/fulltext/images/a008d563b5e52ff19348da5a4b46e153ffa851c9e5e141409a4ffde72b581f77.jpg)  
Fig. 14. Boxplot for the results of the simulation for the nine strategies considering rank order weights.

[5,6]) allows simultaneous changes of the weights and generates results that can be easily analyzed statistically to provide more insights into the multiattribute model recommendations. We propose selecting the weights at random using a computer simulation program so that the results of many combinations of weights, including a complete ranking, can be explored efficiently. Three general classes of simulation will be presented: random weights, rank order weights and response distribution weights. They are described briefly below.

1. Random weights. As an extreme case, weights for the attributes are generated completely at random. This approach implies no knowledge whatsoever of the relative importance of the attributes. In many multicriteria settings, the scores of the strategies significantly limit the subset of potential rankings. Once the simulation has been run, the system computes several statistics about the rankings of each strategy, like mode, minimum, maximum, mean, standard deviation and the 25th, 50th and 75th percentiles. This information can be useful for discarding some possible strategies, aided by a display that presents a multiple boxplot for the strategies (see Fig. 13).

2. Rank order weights. Randomly generating the weights while preserving their attribute rank order places substantial restrictions on the domain of possible weights that are consistent with the DM’s judgement of attribute importance. Therefore, the results from the rank order simulation may provide more meaningful results (see Fig. 14). The DM can introduce the rank order for all or only some of the attributes of the problem.

3. Response distribution weights. The third type of sensitivity analysis using simulation recognizes that the weight assessment procedure is subject to variation. For a single DM, this variation may be in the form of response error associated with weight assessment. Thus, whereas in the first class of simulation attributes, weights were randomly assigned values between 0 and 1 (taking into account that the sum of the whole is 1), random weight simulation attribute weights are now randomly assigned values taking into account the interval weights provided by the DM in the weights assignment methods.

## 7. Conclusions

This paper presents a comprehensive DSS for identifying optimal strategies for problems modelled by means of multiattribute imprecise evaluation based on additive or multiplicative utility functions. The system is very user friendly and makes provision for all the stages of the decision analysis cycle, from construction of the objectives hierarchy to evaluation of the set of strategies for ranking. Moreover, we introduce the possibility of multiparametric sensitivity analyses with respect to DM weights and utilities, as an aid for choosing a final strategy. For this purpose, we apply some concepts by means of which we can reduce the set of strategies of interest and assess the robustness of the solution. The system has been presented as an extension of the MOIRA project evaluation module and applied to a real case related to the restoration of a contaminated lake.

## Acknowledgements

This paper was supported by the Ministry of Science and Technology project DPI2001-3731, the European Commission projects FIP-CT96-0036, ER-BIC15-CT98-0203-COMETES and the Madrid regional government project CAM 07T/-0027/-2000. We are grateful to E. Gallego Dı´az at Nuclear Engineer Department, Madrid Technical University, for useful discussions.

## References

[1] T. Adelbratt, H. Montgomery, Attractiveness of decision rules, Acta Psychologica (1980) 45.

[2] A. Appelgren, U. Bergstro¨ m, J. Brittain, E. Gallego, L. Ha˚- kanson, R. Heling, L. Monte, An Outline of a Model-based Expert System to Identify Optimal Remedial Strategies for Restoring Contaminated Aquatic Ecosystem: the Project MOIRA. Report RT/AMB/96/17 ENEA, 1996.

[3] V. Belton, Multiple criteria decision analysis—practically the only way to choose, in: L.C. Hendry, R.W. Englese (Eds.), Operational Research Tutorial Papers, Operational Research Society, Birmingham, 1990, pp. 53 – 101.

[4] S.A. Brownlow, S.R. Watson, Structuring multi-attribute value hierarchies, Journal of the Operational Research Society 38 (1987) 309–317.

[5] J. Butler, J. Jia, J. Dyer, Simulation techniques for the sensitivity analysis of multi-criteria decision models, European Journal of Operational Research 103 (1997) 531– 546.

[6] J.S. Dyer, T. Edmunds, J.C. Butler, J. Jia, A multiattribute utility analysis of alternatives for the disposition of surplus weaponsgrade plutonium, Operations Research 46 (6) (1998) 749– 762.

[7] P.H. Farquhar, Utility assessment methods, Management Science 30 (1984) 1283–1300.

[8] S. French, D.K.N. Papamichail, D.C. Ranyard, J.Q. Smith, Design of a Decision Support System for use in the Event of a Nuclear Accident, RODOS Report (WG5)-TN(97)-04.

[9] L.H. Ha˚kanson, A system for lake ecosystem indices, Journal of Aquatic Ecosystem Health 2 (1993) 165 – 184.

[10] J.C. Hersey, H.C. Kunreuther, P.J. Schoemaker, Sources of bias in assessments procedures for utility functions, Management Science 28 (1982) 936– 953.

[11] J.Y. Jaffray, Some experimental findings on decision making under risk and their implications, European Journal of Operational Research 38 (1989) 301– 306.

[12] R.L. Keeney, H. Raiffa, Decision with Multiple Objectives: Preferences and Value-Tradeoffs, Wiley, New York, 1976.

[13] C.W. Kirkwood, Strategic Decision Making. Multiobjective Decision Analysis with Spreadsheets, Duxbury Press, Belmont, 1997.

[14] A. Mateos, S. Rı´os-Insua, E. Gallego, Postoptimal analysis in a multi-attribute decision model for restoring contaminated

aquatic ecosystems, Journal of the Operational Research Society 52 (2001) 1 – 12.

[15] M. McCord, R. de Neufville, Lottery equivalents: reduction of the certainty effect problem in utility assessment, Management Science 32 (1986) 56– 61.

[16] L. Monte, E. Gallego, L. Ha˚kanson, J. Brittain, Moira Models and Methodologies for Assessing the Effectiveness of Countermeasures in Complex Aquatic Systems Contaminated by Radionuclides, RT/AMB/99/1 ENEA, 1999.

[17] H. Raiffa, The Art and Science of Negotiation, Harvard Univ. Press, Cambridge, MA, 1982.

[18] S. Rı´os, S. Rı´os-Insua, D. Rı´os Insua, J.G. Pachon, Experiments in robust decision making, in: S. Rı´os (Ed.), Decision Theory and Decision Analysis: Trends and Challenges, Kluwer, Boston, 1994, pp. 233–242.

[19] D. Rı´os Insua, Sensitivity Analysis in Multiobjective Decision Making, Springer, Berlin, 1990 (LNEMS 347).

[20] D. Rı´os Insua, S. French, A framework for sensitivity analysis in discrete multi-objective decision-making, European Journal of Operational Research 54 (1991) 176 – 190.

[21] D. Rı´os Insua, E. Gallego, A. Mateos, S. Rı´os-Insua, MOIRA: a decision support system for decision making on aquatic ecosystem contaminated by radioactive fallout, Annals of Operations Research 95 (2000) 341–364.

[22] T.J. Stewart, Robustness of additive value function method in MCDM, Journal of Multi-Criteria Decision Analysis 5 (1996) 301– 309.

[23] R. Vik, The lake Øvre Heimdalsvatn, a subalpine freshwater ecosystem, Holarctic Ecology 1 (1978) 81– 320.

[24] R. von Nitzsch, M. Weber, Utility function assessment on a micro-computer: an interactive procedure, Annals of Operations Research 16 (1998) 149– 160.

[25] Q.-L. Wei, J. Ma, Z.-P. Fan, A parameter analysis method for the weight-set satisfy preference orders of alternatives in additive multi-criteria value models, Journal of Multi-Criteria Decision Analysis 9 (2000) 181 – 190.

[26] W.T.M. Wolters, B. Mareschal, Novel types of sensitivity analysis for additive MCDM methods, European Journal of Operational Research 81 (1995) 281– 290.

![](/api/attachments/KW5SCRS8/fulltext/images/87c2095cda41292361e5b2b6f14828c4aaa49e07ec44e0411d14c93ac4a08513.jpg)

Sixto-Rı´os-Insua is Professor of Statistics and Operations Research at Madrid Technical University. His research interest is decision analysis and is at present involved in the development intelligent decision support systems based on influence diagrams and multiattribute utility theory with applications to environment and medicine. His articles have appeared in various academic journals including: Computers and Operations Research, Theory and Decision,

EJOR, JORS, Annals of Operations Research, Computational Optimization and Applications, OPSEARCH and Journal of Multicriteria Decision Analysis.

![](/api/attachments/KW5SCRS8/fulltext/images/c7218cf9a3601b7f54b4e6d32d5bed90603cf166ec0f50b4412cd5993d8868cc.jpg)

Alfonso Mateos Caballero is Associate Professor of Statistics and Operations Research at School of Computer Science (Madrid Technical University). His research interest is decision analysis and is currently involved in the development intelligent decision support systems based on influence diagrams and multiattribute utility theory with applications to environment and medicine. His articles have appeared in

various academic journals including: European Journal of Operational Research, J. Opl. Res. Soc., Annals of Operations Research, Computational Optimization and Applications, OPSEARCH and Journal of Multicriteria Decision Analysis.

![](/api/attachments/KW5SCRS8/fulltext/images/8ab9f584ff7be7931fb798a46377ca7fd1407ca2a5d6b9a29ba1c822ede52ebb.jpg)

Antonio Jimenez Martin obtained a Computing Science degree from Madrid Technical University. He is currently Assistant Professor of Statistics and Operations Research at School of Computer Science. His research interest is decision analysis and is involved in the development and implementation of decision support systems based on multiattribute utility theory.

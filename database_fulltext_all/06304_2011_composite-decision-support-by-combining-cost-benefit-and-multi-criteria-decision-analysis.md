---
otero_id: 6304
otero_key: "DK5JY9FH"
title: "Composite decision support by combining cost-benefit and multi-criteria decision analysis"
authors: "Michael Bruhn Barfod; Kim Bang Salling; Steen Leleur"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.12.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Composite decision support by combining cost-bene<sup>fi</sup>t and multi-criteria decision analysis

Michael Bruhn Barfod ⁎, Kim Bang Salling, Steen Leleur

Department of Transport, Bygningstorvet 1, 115, Technical University of Denmark, DK - 2800 Kgs. Lyngby, Denmark

## a r t i c l e i n f o

Article history: Received 2 December 2009 Received in revised form 26 October 2010 Accepted 7 December 2010 Available online 13 December 2010

Keywords: Decision support systems Decision analysis Cost-bene<sup>fi</sup>t analysis Multi-criteria decision analysis

## a b s t r a c t

This paper concerns composite decision support based on combining cost-bene<sup>fi</sup>t analysis (CBA) with multicriteria decision analysis (MCDA) for the assessment of economic as well as strategic impacts within transport projects. Speci<sup>fi</sup>cally a composite model for assessment (COSIMA) is presented as a decision support system (DSS). This COSIMA DSS ensures that the assessment is conducted in a systematic, transparent and explicit way. The modelling principles presented are illuminated with a case study concerning a complex decision problem. The outcome demonstrates the approach as a valuable DSS, and it is concluded that appraisals of large transport projects can be effectively supported using a combination of CBA and MCDA. Finally, perspectives of the future modelling work are given.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Decision support systems (DSS) are widely applied to assist decision-makers with the dif<sup>fi</sup>cult task of identifying the best solution to a given problem. This paper concerns composite decision support based on combining cost-bene<sup>fi</sup>t analysis (CBA) with multi-criteria decision analysis (MCDA) for the assessment of economic as well as strategic impacts within transport projects. Speci<sup>fi</sup>cally a composite model for assessment (COSIMA) is presented as a decision support system (DSS). This COSIMA DSS ensures that the assessment is conducted in a systematic, transparent and explicit way. The approach is presented through a case study concerning alternatives for the construction of a new <sup>fi</sup>xed link between the city of Frederikssund and the peninsula of Hornsherred on the north-eastern part of Zealand, Denmark [2].

The most common methodology applied so far to the evaluation of transport systems has been conventional CBA [11], which supported by traf<sup>fi</sup>c- and impact model calculations provides the decisionmakers with a monetary assessment of the project's feasibility. A socio-economic analysis is in this respect a further development of the traditional CBA capturing the economic value of social bene<sup>fi</sup>ts by translating social objectives into <sup>fi</sup>nancial measures of bene<sup>fi</sup>ts [37]. Internationally seen there has been a growing awareness over the recent years that besides the social costs and bene<sup>fi</sup>ts associated with transport other impacts that are more dif<sup>fi</sup>cult to monetise should also have in<sup>fl</sup>uence on the decision making process. This is in many developed countries realised in the transport planning, which takes into account a wide range of impacts of also a strategic character [33]. Accordingly, appraisal methodologies are undergoing substantial changes in order to deal with the developments [34] that are varying from country to country and leading to different approaches [1]. It is, however, commonly agreed that the <sup>fi</sup>nal decision making concerning transport infrastructure projects in many cases will depend on other aspects besides the monetary ones assessed in a socio-economic analysis. Nevertheless, an assessment framework such as the Danish one [6] does not provide any speci<sup>fi</sup>c guidelines on how to include the strategic impacts; it merely suggests describing the impacts verbally and keeping them in mind during the decision process.

A coherent, well-structured, <sup>fl</sup>exible, straight forward evaluation method, taking into account all the requirements of a transport infrastructure project is for this reason required. An appropriate exante evaluation method for such projects can be based on MCDA [30,36], which in most cases can be combined with a CBA [16]. Scanning the literature [4,8,14,35] it is found that the use of MCDA in the decision process usually provides some or all of the following features:

1. Improvement of the satisfaction with the decision process

2. Improvement of the quality of the decision itself

3. Increased productivity of the decision-makers

MCDA can in this respect be seen as a tool for appraisal of different alternatives, when several points of view and priorities are taken into account to produce a common output. Hence, it is very useful during the formulation of a DSS designed to deal with complex issues. The literature on Decision Support Systems is extensive, providing a sound basis for the methodologies employed and the mathematics involved. Moreover, there are numerous systems covering several disciplines, policy contexts and users’ needs for speci<sup>fi</sup>c application environments [11,28,32]. The use of DSS for solving MCDA problems has among others been treated by [5] and [15], where it is shown that a DSS can effectively support a decision making process making use of appropriate MCDA methodologies.

Earlier research on composite DSS within transport planning has mainly concentrated on incorporating the CBA in the MCDA. Here the European Commission's fourth framework project EUNET [7], which has developed a methodology dealing with the combination of CBA and MCDA, can be mentioned. The EUNET framework applies scores to the investment criterion, e.g. the bene<sup>fi</sup>t cost rates (B/C-rate), thus, it treats the rates as any other criterion in the MCDA. Exactly which criteria to include in the framework is a matter of judgment depending, among other factors, on the reliability of the data and the preferences stated by the decision-makers and/or stakeholders in the decision process. Another similar inclusive approach is proposed in [29] for transport project appraisal in the UK. Different methodological frameworks are used varying from country to country; however, it is roughly possible to divide them into two main categories: CBA-based and MCDA-based frameworks. Among the CBA-based frameworks the Danish and German can be mentioned, while e.g. French and Dutch frameworks are based on the use of MCDA (for further information about European frameworks see e.g. [1] and [7]). Reviews of transport appraisal methodologies and their premises and results can be found in for example [9] and [19] listing also various sources of error and bias in them.

The COSIMA DSS presented and discussed in this paper provides a theoretical and practical methodology for adding non-monetary MCDA-criteria to the monetary CBA-impacts. Unlike previous attempts this DSS is based on the argument that the MCDA-criteria can be added to the CBA-impacts – if value functions can be computed for the MCDA-criteria using a weighting procedure describing the importance of each criterion. Hence, the COSIMA approach is based on the theoretical valid and widely used methodology of additive value functions (see e.g. [14] or [35]). The value function scores are in the presented COSIMA set-up derived via direct rating using pair wise comparisons [4] and the criteria weights are derived by applying rankings [24] in this respect drawing on the Analytical Hierarchy Process (AHP) and the Simple Multi-Attribute Rating Technique Exploiting Ranks (SMARTER) respectively. The total bene<sup>fi</sup>ts from the CBA are used to determine shadow prices for the MCDA-criteria; this is based on a trade-off between the CBA and MCDA, which creates a total rate of return (TRR). The last part requires converting strategic non-quantitative criteria into monetary values [31], which will be discussed further in this paper.

Additive value functions and the AHP are well established and widely applied methods for MCDA [4,10,27,30]. Consequently, they seem appropriate to use in the proposed DSS. Moreover, in terms of transparency, the additive model appears most favourable, since it is considered to be able to cope with almost any problem [4,12]. It is, however, commonly known that the main drawback of these methods is the assignment of criteria weights, since individuals are determining these weights. On the other hand, the performance (scores) of alternatives for each criterion is determined objectively, even if arti<sup>fi</sup>cial scales are used for non-quanti<sup>fi</sup>able criteria. However, the AHP contributes to overcoming this disadvantage by deriving weights in a quasi-independent manner, using pair wise comparisons that make it dif<sup>fi</sup>cult to promote open biases towards speci<sup>fi</sup>c criteria. Thus, AHP is a common method used for prioritisation when having a wide variety of choices. More speci<sup>fi</sup>cally, with regard to the application of the DSS for the case study, the group that assigned the weights was composed of key stakeholders involved in the project.

With reference to the previous work on composite DSS conducted by other researchers this paper deals with three main research questions: Can comprehensive appraisals taking into account both monetary impacts and non-monetary criteria of a decision problem be operationalised to a DSS that can inform the users in terms of both interaction and interpretation of the results? Can a valid guidance be formulated for adding the non-monetary criteria of the MCDA to the monetary impacts of the CBA in the DSS? And <sup>fi</sup>nally, can a set of appropriate guidelines for inclusion of non-monetary criteria in transport planning be set out?

The paper is organised as follows. After this introduction the principles for the modelling approach of the COSIMA DSS is presented. Following, the case study regarding the appraisal of the Danish Hornsherred case is presented and the COSIMA DSS is applied in terms of a comprehensive assessment by incorporating respectively a CBA and a MCDA leading to a composite result. Finally, a conclusion is drawn and perspectives for the future modelling work are given.

## 2. Modelling approach

As mentioned in the introduction the appraisal and planning of transport infrastructure projects should be based on all relevant impacts, which are depending on the type and size of the project viewed upon. Some of these impacts can be assessed monetarily and are thereby possible to include in a socio-economic CBA in a decision model as e.g. the CBA-DK model [13]. However, no common guidelines exist for the assessment of impacts such as urban development, landscape, etc. that hold a potential for improving actual decision support from the assessment if they are treated properly. These nonmonetary or strategic impacts should instead be assessed using a MCDA and are hence denominated MCDA-criteria. The idea behind composite modelling assessment is to extend the CBA into a more comprehensive type of appraisal as often demanded by decisionmakers by including these ‘missing’ decision criteria of relevance for the actual assessment task.

## 2.1. Principles for the COSIMA DSS

The COSIMA DSS consists of a CBA-part and a MCDA-part and the result of the COSIMA analysis is expressed as a total value (TV) based on both parts. This model set-up emphasizes that the MCDA-part should be truly additive to the CBA-part. For this reason a project alternative, $A _ { k } ,$ is better represented towards the decision making by the ${ \cal { W } } ( A _ { k } )$ rather than by the present value from the CBA (the sum of all bene<sup>fi</sup>ts and disbene<sup>fi</sup>ts) – here denominated $C B A ( A _ { k } )$ . The principle in COSIMA can be expressed by (1), where MCDA(A<sub>k</sub>) represents a term which is added to $C B A ( A _ { k } ) [ 2 8 ]$

$$
T V (A _ {k}) = C B A (A _ {k}) + M C D A (A _ {k})\tag{1}
$$

The assessment principles in the MCDA-part are based on decisionmaker involvement. This is not the case in the conventional CBA. This circumstance justi<sup>fi</sup>es the MCDA denomination as the part is based on subjective assessments. It can be noted on the basis of (1) that a situation, where $C B A ( A _ { k } )$ is equal to or smaller than the investment costs $\left( C _ { k } \right)$ , is non-pro<sup>fi</sup>table seen from a socio-economic point of view (i.e. CBA $\left( A _ { k } \right) \le C _ { k } )$ . However, the investment can still be justi<sup>fi</sup>ed by the wider COSIMA analysis if the total value of $A _ { k }$ is larger than the investment costs $( T V ( A _ { k } ) > C _ { k } )$ . This can also be expressed via the total rate of return (TRR) calculated as the total value, ${ \cal { W } } ( A _ { k } )$ , divided by the investment cost, $C _ { k } ,$ , which gives $T R R ( A _ { k } ) > 1$ , indicating a total rate with regard to the attractiveness of alternative k. This leads to (2) below:

$$
T R R (A _ {k}) = \frac {T V (A _ {k})}{C _ {k}} = \frac {1}{C _ {k}} \cdot \left(\sum_ {i = 1} ^ {I} V _ {i} (X _ {i k}) + \alpha \cdot \left[ \sum_ {j = 1} ^ {J} w _ {j} \cdot V F _ {j} (Y _ {j k}) \right]\right)\tag{2}
$$

where

$$
\sum_ {j = 1} ^ {J} w _ {j} = 1 a n d 0 <   w _ {j} <   1
$$

$A _ { k }$ is alternative k

\- $C _ { k }$ are the total costs or expenses of alternative k

$X _ { i k }$ is the quantity of the CBA impact i for alternative k

$V _ { i } ( X _ { i k } )$ is the value in monetary units for the CBA impact i for alternative k

\- α is an indicator that expresses the balance between the CBA and MCDA parts in the model

$w _ { j }$ is a weight which re<sup>fl</sup>ects the importance of MCDA criterion j

$Y _ { j k }$ is a parameter value for MCDA criterion j for alternative k

${ V F } _ { j } ( Y _ { j k } )$ is a value-function score for MCDA criterion j for alternative k

The general COSIMA approach is presented by (1) and (2). (2) can be speci<sup>fi</sup>ed into a CBA if suf<sup>fi</sup>cient knowledge about the criteria to be assessed in the MCDA part is available (e.g. a unit price for at least one criterion and true importance weights for all criteria). This would for example be the case if a conventional CBA is carried out and afterwards supplemented with some extra criteria with satisfactory unit prices speci<sup>fi</sup>ed fully by impact models. However, this will most often not be possible as the impacts handled in the MCDA part in general are based on non-empirical knowledge and often cannot be determined by impact models or even assigned with a unit price. Hence, the purpose of COSIMA is to handle such a situation in a comprehensive and transparent way. This ensured through the determination of appropriate values for α and w for the J MCDAcriteria and appropriate value-function scores $\overset { \cdot } { V F _ { j } } ( Y _ { j k } )$ . The latter supplements of (2) the determination of $V _ { i } ( X _ { i k } )$ which can be derived in accordance with a socio-economic manual relevant for the actual assessment case [6].

## 2.2. Calibration of the COSIMA DSS

Regarding the α-indicator, that expresses the balance between the CBA and MCDA parts in the model set-up, it should be noted that the CBA calculation remains unchanged in COSIMA, but that different α- values will change the MCDA's in<sup>fl</sup>uence on the TRR. In practice it has been found convenient to express α based on a MCDA%, which re<sup>fl</sup>ects the relative weight of the MCDA-part compared to the CBA-part. The value of α=α(MCDA%) is then set by determining MCDA%=100 <sup>.</sup> $\begin{array} { r } { \sum _ { j } B _ { j } ~ / ~ [ \sum _ { i } B _ { i } + \sum _ { j } B _ { j } ] } \end{array}$ , where $\begin{array} { r } { B _ { i } = \sum _ { \kappa \epsilon K } ( b _ { i k } ) } \end{array}$ and $\begin{array} { r } { B _ { j } = \sum _ { \kappa \epsilon K } ( b _ { j k } ) } \end{array}$ represent the value elements for the individual CBA-impact i and MCDA-criterion j summed over the κ alternatives (the alternatives $A _ { \kappa }$ chosen for calibration of the model). Thus $\textstyle \sum _ { i } B _ { i }$ and $\textstyle \sum _ { j } B _ { j }$ are summations of the I CBA-impacts and the J MCDA-criteria, and $B _ { i }$ and $B _ { j }$ the results of the $b _ { i k }$ and $b _ { j k }$ summations of the alternatives, where some if not all are selected for the model calibration [17].

The calculations in the COSIMA DSS use a parameter for the calibration named UP which functions as a shadow price per index value for each of the J MCDA-criteria in order to produce the $b _ { j k }$ values. These bene<sup>fi</sup>t values obtained are determined by $b _ { j k } { = } V \bar { F _ { j } } ( Y _ { j k } ) { \cdot } U P _ { j }$ where the shadow price, $U P _ { j } ,$ , is a function of the α-indicator (MCDA%), the criteria weights $( w _ { j } )$ , the sum of bene<sup>fi</sup>ts from the CBA for the alternatives used for calibration $( \Sigma _ { i } \Sigma _ { \kappa \epsilon K } ( b _ { i \kappa } ) )$ and the sum of VFscores for the alternatives used for calibration $( \sum _ { K } V F _ { j } ( Y _ { j k } ) )$ , see (1) and $( 2 ) .$ . In the procedure α(MCDA%) and $w _ { j }$ determine a fraction of $\sum _ { i } \sum _ { K \epsilon K } ( b _ { i K } )$ that by unit scaling leads to the J unit prices that are used for calculating the $T R R ( A _ { k } )$ . It should be noted that TRR-values are also calculated for alternatives not used in the calibration set. Changes in the set of alternatives $A _ { K }$ behind the calibration will in<sup>fl</sup>uence the $U P _ { j }$ values and thereby the TRR-values. This pool dependence is of great interest for the decision analyst who is formulating the model set-up. The alternatives should in this respect be scrutinised so that the calibration pool only consist of alternatives that are possible solutions [17].

Finally, it is important to note that the TRR-value due to the theoretical differences between CBA and MCDA has no economic argument like e.g. the B/C rate, see Fig. 1. However, the TRR makes it possible to incorporate and hereby retain the information from e.g. the B/C rate in its original form. Additionally, the TRR delivers information concerning the expression of the alternatives performance in relation to the MCDA-criteria – all included in one single rate. Hence, the COSIMA approach provides the decision-makers with a composite measure of attractiveness.

Fig. 1 depicts an overview of the methodological approach resulting in the TRR incorporating the CBA (described in Section 4), the MCDA applying the AHP and SMARTER techniques (described in Section 5) and the summation in COSIMA using the MCDA % (described in Section 6).

## 3. Case Presentation

The case study considered concerns the city of Frederikssund which is situated at Roskilde Fjord in the northern part of Zealand, Denmark. The fjord is separating a peninsula, Hornsherred, from Frederikssund and the rest of the Greater Copenhagen area. Currently, the only connection across the fjord is a bridge featuring only one lane in each direction. This is creating a huge bottleneck for the traf<sup>fi</sup>c in the area around the city of Frederikssund. Moreover, the Danish government has current plans for the construction of a new motorway between Copenhagen and Frederikssund; this will only lead to a further increase of the traf<sup>fi</sup>c problems in the area. Several preliminary studies with the purpose of <sup>fi</sup>nding a solution to the traf<sup>fi</sup>c problems have been conducted by the municipality of Frederikssund in cooperation with the Danish Ministry of Transport [2]. According to [2] only four alternative solutions seem realistic for relieving the current traf<sup>fi</sup>c situation in Frederikssund:

1. An upgrade of the existing road through Frederikssund and the construction of a new bridge parallel to the old bridge

2. A new high-level bridge and a new by-pass road south of Frederikssund

3. A short tunnel with embankments and a new by-pass road south of Frederikssund

4. A long tunnel without embankments and a new by-pass road south of Frederikssund

According to the characteristics of the above mentioned alternatives different impacts will be derived from each alternative implying different investment costs and layouts. The primary stakeholders behind the project, the Region and the municipalities in the area, have formulated the goal and objective of the project as follows [2]:

Improve the traffic flow across the fjord … the solution should take great considerations as concerns the environment in the form of traffic derived consequences (e.g. noise and air pollution) and furthermore consequences derived from the construction itself (e.g. nature and landscape).

This statement calls for a broader type of appraisal than a conventional CBA, which as mentioned in Denmark only includes the <sup>fi</sup>rst type of consequences, however, supplemented with a verbal description of the last type. For this reason the comprehensive approach of the COSIMA DSS embracing both monetary and more strategic consequences is applied to the case study in order to produce informative decision support to the decision-makers. In order to make the appraisal of the alternatives as comprehensive as possible, representatives for key players involved in the decision process are gathered to systematically discuss and analyse the issues at a so-called decision conference as described by [22,23]. The objective of such a decision conference is to constructively deal with the con<sup>fl</sup>icting issues at hand so that a common understanding of the issue can be achieved [20]. The COSIMA DSS is consequently used to model the viewpoints of the participants and to evaluate the alternatives in an auditable manner.

![](/api/attachments/DK5JY9FH/fulltext/images/b6a0f1e964278d44684f6944880dc581e7c8414a8a0af71c0762dd51a4082497.jpg)  
Fig. 1. Overview of the steps in the COSIMA DSS.

## 4. Cost-bene<sup>fi</sup>t analysis

The <sup>fi</sup>rst step in the COSIMA analysis is to conduct a socioeconomic CBA (to derive: $V _ { i } ( X _ { i k } )$ from (2)). This CBA is carried out in a model named the CBA-DK model [13] in accordance with the Danish Manual for Socio-Economic Appraisal [6]. Thus, the CBA includes an assessment of the principal items: Construction and maintenance costs, travel time savings and other user bene<sup>fi</sup>ts, accident savings and other external effects, taxation, scrap value, and <sup>fi</sup>nally tax distortion. A traf<sup>fi</sup>c- and impact model is set up in order to calculate the impacts derived from each project alternative and the construction and maintenance costs are estimated [2]. All impacts are then entered into the CBA-DK model, where forecasting is added according to assumptions about the future development in traf<sup>fi</sup>c. The various economic parameters necessary for conducting the CBA are set in accordance with Danish standards [6] and will not be treated further in this paper. Finally, the feasibility of the alternatives is described by three different investment criteria in the model (see Fig. 2 and Table 1): The bene<sup>fi</sup>t cost rate (B/C-rate), the internal rate of return (IRR) and the net present value (NPV). For elaborating description of the investment criteria see e.g. [16]. The results for all the four alternatives are shown in Table 1.

Fig. 2 depicts how the results are presented in the CBA-DK model. The principal items of a <sup>fi</sup>xed CBA-DK model run are listed on the left hand side, and the two columns on the right hand side show the size of the costs and the bene<sup>fi</sup>ts in the same absolute scale. The results for all the four alternatives are shown in Table 1.

The CBA results clearly show that a high-level bridge is the only feasible alternative if the decision is to be based solely on monetary impacts. The three other alternatives are not feasible according to the investment criteria; the short and the long tunnels because of their high construction costs and the upgrade because of its less signi<sup>fi</sup>cant user bene<sup>fi</sup>ts.

## 5. Multi-criteria decision analysis (Mcda)

The use of MCDA is aimed at supporting decision-makers who are faced with numerous and con<sup>fl</sup>icting choices [18]. Unlike methods like

![](/api/attachments/DK5JY9FH/fulltext/images/0f737112e6c23e85a233500a87460cdee4cdc23a45cc7f6bc8429d3d55d6b259.jpg)  
Fig. 2. Results of the cost-bene<sup>fi</sup>t analysis for the High-level bridge alternative presented in the CBA-DK model.

CBA that assume the availability of empirical data, data in MCDA are derived or interpreted subjectively as indicators of the strength of the decision-makers preferences. These preferences differ from decisionmaker to decision-maker; hence, the outcome of the analysis depends on who are making the assessments and what their goals and preferences are. Since MCDA involves a certain element of subjectiveness, the morals and ethics of the decision-makers implementing MCDA play a signi<sup>fi</sup>cant part in the accuracy and fairness of MCDA's conclusions. The transparency of the assessment is in this respect very important when one is making a decision that seriously impacts on other people.Generally, the different methods that exist for conducting MCDA have been designed in order to designate a preferred alternative, to classify the alternatives in a small number of categories, and/or to rank the alternatives in a subjective order of preference. The second step of the COSIMA analysis, thus, comprises a MCDA in order to determine scores for the alternatives and weights for the criteria, i.e. $V F _ { j } ( Y _ { j k } )$ and w from (2).

Applying creative techniques such as brainstorm at the decision conference as described by [25] the respondent group decided to include four different MCDA-criteria for the case study, covering the ‘missing’ effects of the CBA. Special attention was made in the de<sup>fi</sup>nition of the criteria in order to avoid double counting. The criteria de<sup>fi</sup>nitions are depicted in Table 2.

Investment criteria and the sum of bene<sup>fi</sup>ts $\left( V _ { i } ( X _ { i k } ) \right)$ for the four alternatives concerning the case.

<table><tr><td></td><td>High-level bridge</td><td>Short tunnel</td><td>Long tunnel</td><td>Upgrade</td></tr><tr><td>B/C-rate</td><td>1.63</td><td>0.99</td><td>0.25</td><td>0.36</td></tr><tr><td>IRR [%]</td><td>8.84</td><td>5.95</td><td>2.06</td><td>2.76</td></tr><tr><td>NPV [m DKK]</td><td>415.5</td><td>-10.2</td><td>-1,869.3</td><td>-235.6</td></tr><tr><td> $V_i(X_{ik})$  [m DKK]</td><td>1076</td><td>965</td><td>607</td><td>133</td></tr></table>

## 5.1. Scoring of alternatives

In order of determining the impact of the alternatives within the MCDA-criteria (the value function scores $V F _ { j } ( Y _ { j k } )$ from (2)) an appropriate assessment technique (MCDA method) has to be chosen. Several assessment techniques are available for the purpose of determining the value function scores $\left( V F _ { j } ( Y _ { j k } ) \right)$ ). However, as one of the purposes set out for the COSIMA DSS is to assure to be transparent and easily understandable for decision-makers the well established and widely applied pair wise comparison technique AHP (Analytical Hierarchy Process) by Saaty [26] is used. It should be noted, that even though the AHP technique is considered to be transparent and appropriate for the current case study, other more or less complicated case studies may call for other techniques (see e.g. [4], [8] and [21]for other MCDA methods).

The criteria to be assessed by the MCDA

<table><tr><td></td><td>Definition</td></tr><tr><td>Accessibility</td><td>The criterion ranges from local accessibility through regional accessibility to public accessibility and favours alternatives that contribute to improve the overall accessibility in the transport network.</td></tr><tr><td>Urban development</td><td>The criterion favours alternatives that contribute to develop the existing parts of the city considered plus the opportunity to expand the city and develop new parts.</td></tr><tr><td>Landscape</td><td>The criterion covers the alternatives visual impact on the landscape and favours those alternatives, which have the least negative impact on this plus on recreational areas and areas worthy of preservation.</td></tr><tr><td>Environment</td><td>The criterion covers the environmental issues that are not treated in the CBA, i.e. maritime conditions in the fjord plus plant and animal life in and around the fjord.</td></tr></table>

Using the AHP technique, the decision-makers are involved in direct ratings via pair wise comparisons [4,27] of the alternatives within each of the criteria. For each comparison the decision-makers have to state the strength of their preference for one alternative over another according to the semantic scale that spans from equal preference to absolute preference (1 to 9 on the numerical scale) [26]. Next, the scale values obtained by the pair wise comparisons are for each criterion implemented in a comparison matrix, and normalised scores (AHP scores) for the alternatives are derived using the geometric mean method [3,10]. These normalised scores are computed into value-function (VF) scores utilizing a local scale from 0-100, where the score 0 is describing the worst performing alternative and the score 100 is describing the best performing alternative [4]. All other alternatives will receive linear intermediate scores relative to the two end points. It is noted that the use of a local scale limits the appraisal to concern only the relationship between the already identi<sup>fi</sup>ed alternatives; no absolute measure of their performance is obtained. A local scale is considered to be a useful solution when only dealing with alternatives for one project, i.e. dealing with a closed system. The local scale would, however, not be adequate if it should be possible to include more alternatives at a later stage in the appraisal. In such a case it would be necessary to revise the scale or use a global scale taking the extreme endpoints into account (for more information about local versus global scales see e.g. [4]). The COSIMA DSS is customised to the speci<sup>fi</sup>c problem at hand and thereby assumes that no other alternatives than those identi<sup>fi</sup>ed at the preliminary stage, will be relevant for the appraisal, hence the local scale is appropriate to use.

As a result of the choice of the AHP technique the participants at the decision conference were faced with full pair wise comparisons of the four alternatives within the four criteria comprising a total of 24 comparisons. In order to assure the validity and reliability of the comparisons, time was allocated for a thorough discussion of each comparison and the rationale were recorded in an assessment protocol. Efforts were in this respect made for the participants to reach consensus on each of the comparisons before moving on to the next. In the cases where it was not possible to agree upon the comparisons the different viewpoints were noted with a view to a later sensitivity analysis if felt needed by the participants. In addition to these efforts a consistency check of the comparisons were made and the participants were noti<sup>fi</sup>ed and asked to revise one or more comparisons if the inconsistency index exceeded 0.1 [8].

Next, the AHP-scores derived from the input of the participants are computed into VF-scores. The VF-scores are for each of the four project alternatives shown in Table 3. Considering these scores special attention should be paid if nearly identical AHP-scores are derived and succeedingly transformed into very varying VF-scores. If this is the case, the criterion from the sample should be assigned with a low weight or maybe even omitted as it does not contribute to the segregation between alternatives and consequently it will not be relevant to include in the appraisal. The decision analyst should after the completion of the pair wise comparisons study the VF-scores, perform a check-up with regard to the above and notify the participants if the issue above is relevant.

Table 3 depicts the VF-scores for the four alternatives within the four types of MCDA-criteria. It is noted that three of the alternatives, i.e. the High-level bridge, the Short tunnel and the Long tunnel, have identical VF-scores for “accessibility” and “urban development” namely 100 while the Upgrade's VF-scores are 0 for both criteria. This is due to the former's identical alignments, which have much larger impact within the two criteria than the latter. Hence, the large span between 0 and 100 seems reasonable within the criteria. Within the “landscape” and “environment” criteria the alternatives differentiate more between each other and further investigation is not needed. Clearly, the Long tunnel alternative has the overall best performance within the four criteria. It is for this reason the most attractive alternative if the importance of each of the four criteria is weighted equally. However, the decision-makers would most often feel that some criteria are more important than other. Thus, a weighting procedure describing the importance of each criterion is assigned.

Table 3  
Value function scores describing the alternatives performance within the criteria.

<table><tr><td></td><td>High-level bridge</td><td>Short tunnel</td><td>Long tunnel</td><td>Upgrade</td></tr><tr><td>Accessibility</td><td>100</td><td>100</td><td>100</td><td>0</td></tr><tr><td>Urban development</td><td>100</td><td>100</td><td>100</td><td>0</td></tr><tr><td>Landscape</td><td>0</td><td>7</td><td>34</td><td>100</td></tr><tr><td>Environment</td><td>8</td><td>0</td><td>46</td><td>100</td></tr></table>

## 5.2. Weighting of criteria

For the determination of the criteria weights (w ) the SMARTER (Simple Multi-Attribute Rating Technique Exploiting Ranks) technique [8] using ROD (Rank Order Distribution) weights [24] is applied to the COSIMA DSS. The ROD-weights are surrogate weights which provide an approximation to unrestricted original weights. Surrogate weights based on rankings have been proposed as a method for avoiding the dif<sup>fi</sup>culties associated with the elicitation of weights in MCDA [4]. The decision making process is thereby simpli<sup>fi</sup>ed as the technique only requires an importance ranking of the four MCDA-criteria. Thus, no speci<sup>fi</sup>cation of the weights is needed from the decision-makers as these are determined by the ROD technique and assigned to the criteria according to the ranking. Hence, the participants at the decision conference were faced with the task of ranking the criteria in order of importance. Different viewpoints were expressed by the participants; however, it was possible through discussion to reach consensus in the group. The ranking agreed upon is in correspondence with the SMARTER technique assigned with the ROD-weights as shown in Table 4.

Determining the weights requires much responsibility and expertise from the decision-makers as the weights have considerable in<sup>fl</sup>uence on the results of the assessment. Using the SMARTER technique applying ROD weights instead of using pair wise comparisons from AHP to determine the weights has for this purpose been chosen in order to make the interaction with the decision-makers around weights simpler. It is assumed that the setting of weights for criteria is more subjective than the scoring of the project attributes based on pair wise comparisons. For the latter the consistency AHP check has the purpose of securing certain validity for the scores.

## 6. Combining CBA and MCDA

The last parameter in (2) – the α indicator – is determined as a balance (weight) between the CBA and the MCDA and expressed by the MCDA% as described in Section 2.2. The calibration of the model was made using all four alternatives as all were regarded to be serious contenders for the <sup>fi</sup>nal choice; the High-level bridge due to its performance within both the CBA and MCDA, and the three other alternatives due to their performance within the MCDA. As noted, the CBA calculation result remains unchanged at all stages in the composite appraisal, but different values of α (the MCDA%) will change the weight of the MCDA on the TRR. As depicted in (2) the

ROD weights assigned to the criteria according to the level of importance.

<table><tr><td>Rank</td><td>Criteria</td><td>ROD-weight</td></tr><tr><td>1</td><td>Accessibility</td><td>0.42</td></tr><tr><td>2</td><td>Environment</td><td>0.30</td></tr><tr><td>3</td><td>Landscape</td><td>0.19</td></tr><tr><td>4</td><td>Urban development</td><td>0.09</td></tr></table>

MCDA% will always be less than 100 as the CBA outcome always will have in<sup>fl</sup>uence on the TRR i.e. the CBA result cannot be omitted from the appraisal. Fig. 3 discloses the result covering the agreed ranking of the MCDA-criteria. Note that MCDA% values larger than 80 are not shown on the <sup>fi</sup>gure as no changes in the ranking between the alternatives take place based on these values.

Fig. 3 depicts that the TRR-values increase for all four alternatives as the MCDA adds a higher importance. However, it can be seen that the TRR for the upgrade of the existing connection is increasing more rapidly than the other alternatives which is due to lower construction costs for this alternative, compared with the three others. The increase, however, is also very dependent on which MCDA criteria that are considered the most important ones. The ranking of criteria in Table 4 shows accessibility and environment as the most important criteria. As a result of this the alternatives with high scores on these criteria, will also have the largest increase in their TRR-value and vice versa. The TRR-values point out different alternatives as the most attractive depending on which MCDA% that is considered. However, it is not always bene<sup>fi</sup>cial to let the decision-makers base their decision on an interval result, e.g. from 0 to 80 %. In most cases the decisionmakers should agree upon a speci<sup>fi</sup>c MCDA% or a short interval (e.g. 30 – 50 % MCDA) before deciding about the project. Practical experience so far points to MCDA% values in the range between 20 to 30 % [2]. Furthermore, it seems that high MCDA% values are most likely to be adopted when appraising larger and more complex strategic infrastructure projects e.g. the Fehmarn Belt <sup>fi</sup>xed link between Germany and Denmark. The MCDA% to base the decision on will also vary depending on society's economy, current political tendencies and the type of project being appraised.

The participants at the decision conference were asked to express their preferences with regard to the CBA/MCDA weighting and there was agreement that CBA was the most important part of the appraisal as the project is not regarded to be one of the large strategic infrastructure projects mentioned before. After a discussion a MCDA% set to be 30 was chosen, and with this CBA/MCDA balance applied the high-level bridge is still clearly the most attractive alternative. Thus, this alternative appears as the most robust choice based on the comprehensive appraisal.

## 7. Results and discussion

Summarising the calculations and the process concerning the case it is noted that the analysis is based on the use of CBA and MCDA. The CBA produces results that can be measured in a monetary unit – here million Danish Kroner (m DKK). The MCDA on the other hand produces results that by comparison with the CBA results can be calibrated to ‘assessment m DKK’. In order to obtain a total value for an examined alternative m DKK and ‘assessment m DKK’ is added. This mix between m DKK and the <sup>fi</sup>ctitious ‘assessment m DKK’ is expressed by the unit ‘attractiveness m DKK’. The result can also be presented as a total rate of return (TRR), where the result in ‘attractiveness m DKK’ is divided by the investment costs, see Table 5. In this context it should be noted that the process based on input (scoring of alternatives, determination of criteria-weights and balancing the CBA and MCDA) makes it possible to provide a transparent evaluation process involving the decision-makers.

![](/api/attachments/DK5JY9FH/fulltext/images/4f44c093cdf68397b47aa1bd7e684b8a57332131314d9a9c3b57ed7586e02942.jpg)  
Fig. 3. TRR values for the four alternatives as a function of the MCDA%.

Thus, the result of the COSIMA analysis is that using decisionmaker involvement it is possible to apply values to the MCDA-criteria which are comparable to the monetary values from the CBA. The results depicted in Table 5 indicate the ‘gain’ by choosing an alternative which performs well within the MCDA instead of the alternative which performs the worst. In strategic terms the decisionmakers in the case study would achieve most from the investment by choosing the Long tunnel alternative (MCDA alone). However, overall (CBA+MCDA) the High-level bridge alternative will continue to be the most attractive.

As mentioned in Section 1 the existing assessment framework in Denmark does not attempt to incorporate the strategic issues (the MCDA-criteria) of a decision problem into appraisals of transport infrastructure projects. Other frameworks, such as the EUNET framework [7], incorporate the CBA results as a criterion in the MCDA and the result is expressed in form of a relative rate. Using the COSIMA DSS the decision-makers are provided with a result that contains a level of information which comprises both the CBA and MCDA expressed in a more easy accessible way. Generally, decisionmakers are used to make decisions on the basis of a B/C rate and are hence comfortable with this type of expression. The new feature in the COSIMA DSS is that the MCDA part is converted to the same scale as the CBA part providing the decision-makers with an indication of the value of the strategic issues based on their own preferences expressed as a total rate of return. The TRR result will most likely vary based on who is stating the preferences, however, by assuring diversity in the assessment group the result becomes valid to a wide audience.

A downside of using a pair wise comparison technique such as AHP is the number of comparisons that the respondent group has to make. In the case study addressed in this paper only four alternatives are to be assessed within four criteria leading to 24 comparisons, but if just one extra alternative is added to the appraisal the number of comparisons will be 40. if another is added the number is 60 etc. Hence, the more alternatives in an assessment the more inappropriate the pair wise comparison technique becomes. If there are too many comparisons to be made the respondent group tends to get tired and make comparisons of a lower quality as their will to discuss fades; the comparisons can then tend to be taken as more or less an average of the groups’ viewpoints. This will in<sup>fl</sup>uence the rest of the appraisal and generate poor results. In order for this not to be an issue another assessment technique should be chosen if the number of comparisons exceeds what seems reasonable to manage within the given time frame of the assessment task. From testing the methodology at a number of occasions it has been found that the maximum number of comparisons demanded from the respondent group should be less than 50 if the time frame available is only one day or less. In one test case this limit was reached as the respondent group had to assess four alternatives within 8 criteria leading to 48 comparisons in a half day meeting.

An important issue to address when making the <sup>fi</sup>nal conversion of the MCDA part to the CBA part is the importance of the criteria weights. The weights are directly linked to the shadow prices assigned to the criteria in the COSIMA-DSS and changes in the weights will thus have a large in<sup>fl</sup>uence on the <sup>fi</sup>nal outcome of the analysis. The criteria weights can be seen as the most subjective part of the MCDA assessment and will differ dependent on who is setting them. For this reason sensitivity analysis should be conducted testing different weight sets in order to see how changes will affect the investment decision to be taken.

Table 5  
Results of the composite COSIMA analysis using a MCDA% set to be 30.

<table><tr><td></td><td>High-level bridge</td><td>Short tunnel</td><td>Long tunnel</td><td>Upgrade</td><td>Method</td><td>Unit</td></tr><tr><td>Investment costs</td><td>661</td><td>975</td><td>2477</td><td>369</td><td>CBA</td><td>m DKK</td></tr><tr><td>Total benefits</td><td>1076</td><td>965</td><td>607</td><td>133</td><td>CBA</td><td>m DKK</td></tr><tr><td>B/C rate</td><td>1.63</td><td>0.99</td><td>0.25</td><td>0.36</td><td>CBA</td><td></td></tr><tr><td>Accessibility</td><td>165</td><td>165</td><td>165</td><td>0</td><td>MCDA</td><td>Assessment m DKK</td></tr><tr><td>Urban development</td><td>101</td><td>101</td><td>101</td><td>0</td><td>MCDA</td><td>Assessment m DKK</td></tr><tr><td>Landscape</td><td>0</td><td>8</td><td>42</td><td>122</td><td>MCDA</td><td>Assessment m DKK</td></tr><tr><td>Environment</td><td>11</td><td>0</td><td>66</td><td>144</td><td>MCDA</td><td>Assessment m DKK</td></tr><tr><td>Total MCDA</td><td>277</td><td>274</td><td>374</td><td>266</td><td>MCDA</td><td>Assessment m DKK</td></tr><tr><td>Total value</td><td>1353</td><td>1239</td><td>981</td><td>399</td><td>CBA + MCDA</td><td>m DKK + &#x27;Assessment m DKK&#x27; = &#x27;Attractiveness m DKK&#x27;</td></tr><tr><td>Total rate</td><td>2.05</td><td>1.27</td><td>0.40</td><td>1.08</td><td></td><td></td></tr></table>

## 8. Conclusions

This paper has presented some principles concerning composite decision support based on combining cost-bene<sup>fi</sup>t analysis (CBA) with multi-criteria decision analysis (MCDA). Speci<sup>fi</sup>cally a composite model for assessment (COSIMA) has been presented as a decision support system (DSS). The major focus has been exposing the potential of the COSIMA DSS as a tool for complex assessment problems, which has been assisted by illuminating it with a case example. The following characteristics of the COSIMA DSS can be noted. COSIMA is simple in its design and application compared to earlier attempts to composite analyses (e.g. [7,29,30]), as the methodology basically just “adds to” and does not hide or change the information given by the CBA. Furthermore, it contains qualities that make it suitable for handling complex assessment problems by incorporation of relevant MCDAcriteria and applications based on weights. In this way the methodology behind COSIMA sets-out guidelines for dealing with the overall feasibility issues of a project appraisal by exploring whether other issues or criteria complementing the CBA can make a project change from being non-feasible to attractive. The methodology has been formulated to deal with the often occurring issue that the CBA result is not suf<sup>fi</sup>cient for the actual problem as decision-makers often want additional, systematic examinations that can supplement the CBA. In this respect the COSIMA methodology will be useful and, furthermore, the approach with its new features may be perceived easier accessible by the decision-makers than more complex types of MCDA.

The COSIMA DSS differs from previous attempts on doing composite appraisals in the transport sector in several ways. First of all the COSIMA DSS seeks to ‘translate’ the MCDA results into the same ‘language’ as the CBA results make it possible to produce a total rate of return (TRR), whereas most recent methodologies incorporate the CBA in the MCDA. Obviously, the TRR outcome from the composite expression has no economic argument even though expressed similar to the bene<sup>fi</sup>t cost rate. Instead the TRR describes the attractiveness of the alternative seen from both the CBA and MCDA. Thus, the innovative advantage of using the COSIMA approach is that the CBA results are maintained throughout the analysis. Moreover, COSIMA has the advantage that expressing the outcome on a graph as depicted in Fig. 3 makes it possible to review the results sensitivity with regard to the weights assigned to the CBA and MCDA respectively.

Overall, it can be concluded that COSIMA contribute in a new way to make decisions more informed. It is moreover seen as a major feature of the modelling approach that the various inputs needed from the decision-makers can help trigger important discussions. This issue has not been discussed thoroughly in this paper, but the outlined decision conference is a method to support and facilitate these discussions amongst decision-makers as described by Phillips [23] and treated further in [20]. A future research task will thus be to explore the modelling and decision-maker interaction further with the purpose of improving the learning and understanding among the decision-makers about the actual non-standard appraisal task.

## References

[1] D. Banister, J. Berechman, Transport Investment and Economic Development, UCL Press, London, UK, 2000.

[2] M.B. Barfod, Appraisal of alternatives for a new Hornsherred connection, Center for Traf<sup>fi</sup>c and Transport, Technical University of Denmark, Master Thesis, 2006.

[3] J. Barzilai, W.D. Cook, B. Golany, Consistent Weights for Judgment Matrices of the Relative Importance of Alternatives, Operations Research Letters 6 (3) (1987) 131–134.

[4] V. Belton, T.J. Stewart, Multi Criteria Decision Analysis: An Integrated Approach Kluwer Academic Publishers, UK, 2002.

[5] Y. Chen, D.M. Kilgour, K.W. Hipel, Screening in multiple criteria decision analysis Decision Support Systems 45 (2008) 278–290

[6] Danish Ministry of Transport, Manual for Socio Economic Appraisal: Applied Methodology in the Transport Sector (in Danish), Danish Ministry of Transport, Copenhagen, , 2003.

[7] EUNET/SASI, Final Report – Executive Summary, 4th RTD Framework Programme of the European Commission, , 2001.

[8] P. Goodwin, G. Wright, Decision Analysis for Management Judgment, fourth ed John Wiley & Sons Ltd, UK, 2009.

[9] Y. Hayashi, H. Morisugi, International comparison of background concept and methodology of transport project appraisal, Transport Policy 7 (2000) 73–88.

[10] C.L. Hwang, K. Yoon, Multi Attribute Decision Making – An Introduction, Sage University Papers, Sage Publications, 1995.

[11] M. Janic, Multi-criteria Evaluation of High-speed Rail, Transrapid Maglev and Air Passenger Transport in Europe, Transportation Planning and Technology 26 (6) (2003).491-512

[12] A. Jiménez, S. Ríos-Insua, A. Mateos, A decision support system for multiattribute utility evaluation based on imprecise assignments, Decision Support Systems 36 (2003) 65–79.

[13] K.B. Salling, Assessment of Transport Projects: Risk Analysis and Decision Support, PhD Thesis, Department of Transport, Technical University of Denmark, 2008.

[14] R.L. Keeney, H. Raiffa, Decisions with Multiple Objectives – Preferences and Value Tradeoffs, Cambridge University Press, UK, 1993.

[15] O.I. Larichev, A.V. Kortnev, D.Y. Kochin, Decision support system for classi<sup>fi</sup>cation of a <sup>fi</sup>nite set of multicriteria alternatives, Decision Support Systems 33 (2002) 13–21.

[16] S. Leleur, Road Infrastructure Planning: A Decision-Oriented Approach, second ed. Polyteknisk Press, Denmark, 2000.

[17] S. Leleur, Systemic Planning, second ed.Polyteknisk Press, Denmark, 2008.

[18] F.A. Lootsma, Multi-criteria decision analysis via ratio and difference judgement, Kluwer Academic Publishers, The Netherlands, 1999.

[19] P. Mackie, J. Preston, Twenty-one sources of error and bias in transport project appraisal, Transport Policy 5 (1998) 1–7.

[20] J. Mustajoki, R.P. Hämäläinen, K. Sinkko, Interactive computer support in decision conferencing: Two cases on off-site nuclear emergency management, Decision Support Systems 42 (2007) 2247–2260.

[21] D.L. Olson, G. Fliedner, K. Currie, Comparison of the REMBRANDT system with analytic hierarchy process, European Journal of Operational Research 82 (1995) 522–539.

[22] L.D. Phillips, A theory of requisite decision models, Acta Psychologica 56 (1984) 29–48.

[23] L.D. Phillips, Decision Conferencing, A Working Paper from London School of Economics & Political Science (06.85), Operational Research Group, Department of Management, UK, 2006.

[24] R. Roberts, P. Goodwin, Weight Approximations in Multi-attribute Decision Models, Journal of Multi-Criteria Decision Analysis 11 (2002) 291–303.

[25] S. L. Jeppesen, Sustainable Transport Planning – A Multi-Methodology Approach to Decision Making, PhD thesis from the Department of Transport, Technical University of Denmark, 2010

[26] T.L. Saaty, A Scaling Method for Priorities in Hierarchical Structures, Journal of Mathematical Psychology 15 (1977) 234-281.

[27] T.L. Saaty, Decision Making for Leaders: The Analytical Hierarchy Process for Decisions in a Complex World second vol The Analytical Hierarchy Process Series 2001

[28] K.B. Salling, S. Leleur, A.V. Jensen, Modelling Decision Support and Uncertainty for Large Transport Infrastructure Projects: The CLG-DSS model of the Øresund Fixed Link Decision Support Systems 43 (2007) 1539–1547.

[29] T.M. Sayers, A.T. Jessop, P.J. Hills, Multi-criteria evaluation of transport options – flexible transparent and user-friendly, Transport Policy 10 (2003) 95–105.

[30] D.A. Tsamboulas, A tool for prioritizing multinational transport infrastructure investments, Transport Policy 14 (2007) 11–26.

[31] D.A. Tsamboulas, G.K. Mikroudis, EFECT – evaluation framework of environmental impacts and costs of transport initiatives, Transportation Research. Part D 5 (2000) 283–303.

[32] D.A. Tsamboulas, G.K. Mikroudis, TRANS-POL: A mediator between transportation models and decision makers’ policies, Decision Support Systems 42 (2006) 879–897.

[33] J. van Exel, S. Rienstra, M. Gommers, A. Pearman, D. Tsamboulas, EU involvement in TEN development: network effects and European value added, Transport Policy 9 (2002) 299–311.

[34] R. Vickerman, Evaluation methodologies for transport projects in the United Kingdom, Transport Policy 7 (2000) 7–16.

[35] D. von Winterfeldt, W. Edwards, Decision Analysis and Behavioral Research, Cambridge University Press, New York, USA, 1986.

[36] R. Vreeker, P. Nijkamp, C.T. Welle, A multicriteria decision support methodology for evaluating airport expansion plans Transportation Research. Part D 7 (2002) 27–47

[37] S. Wright, J.D. Nelson, J.M. Cooper, S. Murphy, An evaluation of the transport to employment (T2E) scheme in Highland Scotland using social return on investment (SROI), Journal of Transport Geography 17 (2009) 457–467.

![](/api/attachments/DK5JY9FH/fulltext/images/22cc7d913d446e2d75b4d01855b673115f17fea864595c05168977778d8a0557.jpg)

Michael Bruhn Barfod is currently a PhD student and scienti<sup>fi</sup>c assistant in the Decision Modelling Group – Department of Transport at the Technical University of Denmark. His research is mainly concerned with methods and techniques for composite modelling assessment where different methods are combined into an overall assessment methodology. Examples are AHP, REMBRANDT and SMART, which are widely used. Moreover, processes of group decision making is a central issue in his study. He has been involved in several projects concerning the development of decision support systems and most recently he has been involved in a project for the Danish Road Directorate assessing projects with very limited data using multi-criteria decision analysis.

![](/api/attachments/DK5JY9FH/fulltext/images/487b4dc74e67eb9c869a42cd021d52160dd14fae3f9c39729b64c99e87dee2fe.jpg)

Kim Bang Salling is currently an assistant professor in the Decision Modelling Group – Department of Transport at the Technical University of Denmark. He holds a PhD degree in decision support and risk assessment for transportation projects. His research is concerned with socio-economic evaluation methodologies and decision support systems with special emphasis on cost-bene<sup>fi</sup>t analysis and risk assessment where the main focus is principles and methods for optimization of project appraisal including risk assessment and Monte Carlo simulation. He has been working with a decision support tool for a composite evaluation model called CBA-DK. Currently, he is involved in a large research project for the Danish strategic research council regarding uncertainties within transport evaluation.

![](/api/attachments/DK5JY9FH/fulltext/images/e34101f90665157ece60d7cd3367cc719a2d1ea4dd4045d61daf507693d28c09.jpg)

Steen Leleur is professor of decision support systems and planning at the Department of Transport at the Technical University of Denmark. Currently he is, among other things, involved in research on topics about systems analysis and evaluation methodology. His most recent book “Systemic Planning – Principles and Methodology for Planning in a Complex World” treats the issues of uncertainty and complexity as relating to strategic planning and evaluation problems. Previously he has published textbooks in Danish and English about traf<sup>fi</sup>c planning and highway engineering. He defended his doctoral dissertation at the Technical University of Denmark about investment planning in 1984. From 1972 until 1986 he worked in the Danish Road Directorate. From 1986 until present Steen Leleur has been employed by the Technical University of Denmark. For several years he was associated with the Copenhagen Business School, where he taught courses in systems science and planning theory. Over the years Steen Leleur has been involved in many international transport planning and evaluation research projects, among others several within the European Commission's strategic transport research programmes.

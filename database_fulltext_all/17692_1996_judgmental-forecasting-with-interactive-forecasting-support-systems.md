---
otero_id: 17692
otero_key: "V8D5EBKJ"
title: "Judgmental forecasting with interactive forecasting support systems"
authors: "Joa Sang Lim; Marcus O'Connor"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00009-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Judgmental forecasting with interactive forecasting support systems

Joa Sang Lim, Marcus O'Connor \*

School of Information Systems, The University of New South Wales, P.O. Box 1, Kensington, NSW 2033, Australia

## Abstract

With an increasing use of DSS/EIS, managers are often required to process information coming from a variety of sources in making a final decision. However, we have little understanding of the efficiency with which people select and use the multiple pieces of information. This issue was examined under various conditions using a DSS in a forecasting task where multiple items of information were displayed on request in an interactive manner. Results indicate that overall people underacquired information. Moreover, people often selected less-reliable information. This sub-optimal behaviour did not diminish over time (it became worse). But an aggregation DSS was helpful at the task. This suggests that people seemed to have a problem in aggregating multiple pieces of information. It was also found that the independent preparation of an initial forecast improved forecast accuracy significantly. Perhaps, forecasters may prepare the initial forecast independently and use decision aids for the subsequent tasks of the forecasting process.

Keywords: Forecasting support systems; Judgmental forecasting; Information acquisition and utilisation

## 1. Introduction

The use of DSS and EIS has increased dramatically since their inception ([47]). The focus is on the provision of information for subsequent management judgment. Typically, such systems are designed to permit access to as much information that is possible within the constraints of relevance, security and availability. The overall design philosophy is that managerial judgment is enhanced by the provision of relevant and timely information and by the use of statistical support, where appropriate. Of course, such systems presume that the problem of information overload will not occur, since users are able to self regulate the amount they select and use. Some studies have questioned the efficacy of this assumption ([29]). Another assumption of such systems is that people are able to judiciously select the information they wish to use. In other words, people are presumed to adopt a rational cost/benefit model in their information selection. Recognising that information comes to them at a cost (in both its use and its provision), they will only select information where the marginal benefit is greater than its marginal cost. Whilst there have been a number of studies in psychology that have investigated this issue (see [14] for a review), few studies have examined the way people using DSS/ EIS make choices in the information they wish to use. This study addresses this issue for a forecasting task. A third issue concerns the integration of information from a variety of sources. Since EIS are predicated on the need for human judgment, can people effectively integrate multiple pieces of information from a variety of sources? Again, this issue has received considerable investigation in psychology (e.g., [49]), with an overwhelming conclusion that people have great problems in information integration. This study examines the issue of information selection and integration from a Forecasting Support Systems (a DSS designed to support the forecasting task).

The forecasting task has been chosen for a number of reasons. First, it is one of the most pervasive tasks faced by middle management, often the target of DSS/ EIS design ([18]). Second, it is one task that is amenable to DSS/ EIS support. The forecasting task ([54]) often begins with a consideration of past data (the time series), the consideration of statistical time series forecasts, and concludes with the integration of important non-time series information into the final estimate ([24]). All such components can be effectively supported by a DSS/ EIS. Finally, as others have demonstrated ([13]), the forecasting task provides an ideal environment for studying the impact of information systems design on organisational behaviour.

This paper reports a study of the way people select and use items of information and statistical support that are provided by a DSS in a time series forecasting task. It also examines the way people learn to change their behaviour over time as they use the DSS. Investigation of this issue may identify possible biases involved and provide some useful guidelines in the design of an interactive DSS/ EIS for time series judgmental forecasting (e.g., [91,51]).

## 2. Prior literature on information purchase

An understanding of information acquisition behaviour is useful in the design of DSS/ EIS (e.g., [71]) and in general requirement analysis specification. Two fundamental issues of most investigators in this field include (1) what information decision makers attend to (i.e., information acquisition) and (2) how they utilise the information accessed (i.e., information utilisation). Empirical studies with respect to these two issues are subsequently reviewed.

## 2.1. Information acquisition

Forecasters in the use of DSS/ EIS very often require integrating their own opinion with multiple items of information coming from different sources: (1) judgmental reports from subordinates in other sales branches, (2) statistical forecasts and (3) causal information from a variety of often conflicting sources. An underlying cognitive control mechanism in information acquisition is a cost and benefit consideration associated with information ([83]). The concept of information value has received considerable attention in a number of schools – accounting ([30,69]), information economics ([41,11,83]) and psychology ([25]). Among others, a Bayesian model was developed by Edwards ([25]) in a binary optional stopping task. This model has some unrealistic assumptions to apply to time series forecasting, which include (1) no limit in resources, (2) the computational capability of a decision maker and (3) the binary nature of a decision. Later, a regression model was proposed based on the Brunswik's ([8]) Lens model and subsequently used by Connolly and his associates (e.g., [15]). Unlike the Bayesian model, the regression model does not necessarily require the decision maker to conduct sequential computations of the costs and benefits associated with buying additional piece of information. In this model, an optimal decision maker should minimise total costs, being the sum of monetary penalty for wrong decisions and information costs (see [15] for mathematical details). Thus, a rational decision maker should not purchase any information if its marginal cost outweighs the expected monetary penalty without it (i.e., maximisation of payoffs).

A considerable degree of sub-optimal behaviour in information acquisition compared to the optimal rule discussed above has been persis-

tently shown in most empirical studies. Some ([40,56]) found a tendency of people to overpurchase more than suggested by the normative model. On the other hand, others ([46,78]) claimed the opposite underpurchase. Indeed, there are numerous biases that account for sub-optimal behaviour in information acquisition ([14]). The analysis presented in Table 1 reveals that people are often insufficiently responsive to the normative factors that must be considered in making purchase decisions ([25,76]), i.e., costs, payoffs, diagnosticity, prior probability and reliability ([92]). A considerable body of evidence suggests that information acquisition appears to be in the theoretically appropriate direction, but people are only partially sensitive to the information ([101]). People also make wrong purchase decisions under the influence of the optimally irrelevant factors, by which they should not be affected (e.g., framing). Whilst there are some individual differences due to cognitive styles ([22]), this suggests some serious flawed mechanism in cognitive cost-benefit calculations as shown in the psychological literature (e.g., [4]). Surprisingly enough, however, this sub-optimality was not easily mitigated by learning. The main reason suggested may be bounded rationality ([90]), i.e., people do not gather an optimal amount of information but purchase an amount that permits them to satisfaction. This issue has significant implications to the designers of DSS/ EIS, since the information acquisition behaviour may impair the effective use and implementation of a well-designed DSS (e.g., [97]).

## 2.2. Information utilisation

The second aspect of any decision making with DSS/EIS is information utilisation, i.e., processing the information acquired. There also appears to be substantial deviation from optimality concerning this aspect in the information purchase task. The deviation could be attributed to (1) a problem in the previous stage, i.e., mis-acquisition and/or (2) a problem in aggregating the information they gathered, i.e., mis-aggregation. Whilst the former has been considerably studied, the latter problem has received comparatively less attention in the information purchase studies. The reason may be that most information purchase tasks (e.g., Bayesian) require sequential revision one by one for each piece of information. Hence, people may stop buying information when they cannot process any more. In real business settings, however, people do not always receive information one by one ([77], p. 142), but often multiple items of information come all at once. This is particularly true for DSS/EIS where a plethora of information is available. The judgmental literature is replete with evidence that people are deficient of the capability of aggregation and thus, most empirical researchers are in favour of mechanical combination ([27,19]). Whilst Lim and O'Connor ([59]) found a more serious deficiency in attaching weightings than in aggregation itself in a single cue task, this may not be the case where people need to process multiple items of information.

Biases found in information purchase tasks

<table><tr><td>Issues</td><td>Biases</td><td>Empirical evidence</td></tr><tr><td rowspan="6">Partial sensitivity to optimal factors</td><td>over-influence of irrelevant initial decisions</td><td>[80]</td></tr><tr><td>more serious sub-optimal purchasing, conditional on prior probabilities</td><td>[38,101]</td></tr><tr><td>inappropriate paying, i.e. reluctance to pay or purchase more expensive information, despite corresponding increase in predictive power</td><td>[46,16]</td></tr><tr><td>little or inappropriate responsiveness to payoffs</td><td>[38,101]</td></tr><tr><td>failure to incorporate, or inappropriately responsive to varying diagnosticity</td><td>[38,75,101,40,93]</td></tr><tr><td>considerable purchasing of less reliable information</td><td>[46,16]</td></tr><tr><td rowspan="5">Mistaken sensitivity to optimally irrelevant factors</td><td>framing of a problem (gains vs. losses)</td><td>[15,6]</td></tr><tr><td>minor changes in context ([72])</td><td>[102,32,78,17]</td></tr><tr><td>a tendency to buy more when more information is available</td><td>[56,75,15]</td></tr><tr><td>a tendency to spend more when more resources are available</td><td>[56]</td></tr><tr><td>unwillingness to buy when sources are conflicting with each other</td><td>[55]</td></tr></table>

To summarise, people are prone to cognitive biases at every phase of decision making although the DSS literature typically focuses on the latter phases ([79]). We wish to examine the way people select and use information with an interactive computer-based DSS at a time series judgmental forecasting task. In practice, managers often make an initial judgment before using systems and it seems crucial in determining DSS/ EIS usage. Unfortunately, we do not have empirical evidence as to its usefulness and importance in the overall forecasting process. This paper also addresses the effect of information with varying reliability at the task. Drawing upon prior literature, research hypotheses are developed in the next section to address the two aspects of information acquisition and utilisation across four factors – initial forecasts, reliability, learning and decision support.

## 3. Development of research hypotheses

## 3.1. Hypotheses about initial forecasts

Impact on information acquisition: Most forecasting researchers ([3,53,62,61]) advise that systems to support forecasting should be designed to prepare an initial forecast independently and combine it with a quantitative forecast. However, judgmental psychologists claimed that this practice may be subject to the dysfunctionality of the anchoring-adjustment bias ([99]) and confirmatory traps (cf. [48]). In time series settings, this anchoring-adjustment heuristic was so persistent that people were reluctant to process additional information to update their own opinion ([59]). The impact of initial judgments on subsequent information seeking was directly addressed in Pruitt ([80]) who found that those who made an initial guess prior to seeing any information sought a significantly greater number of information cues than suggested by the optimal (p < 0.05) and also than those without the initial guess (p < 0.01). This suggests that the initial guess, albeit completely irrelevant, required much more information to change it and this finding is in parallel with the anchoring-adjustment studies ([99]). This reluctance would lead people to acquire fewer items of information when they have an anchor than when they do not. Yet limited empirical evidence in time series settings leads us to a null hypothesis that: $^{1}$

$H_{1a}$ : There is no difference in the number of information cues acquired between the initial forecast group and the no-initial forecast group.

Impact on information utilisation: There exists a considerable body of evidence that an initial anchor could dysfunctionally affect subsequent processing of additional information. It should be, however, noted that most studies in psychology and accounting literature investigated the effect of an initial decision, not rationally made but either provided by the experimenter ([101,48,98]) or simply guessed ([80]). In a forecasting context, it is true that those without the initial forecast may be more prone to anchoring on a useless value. The sceptical evidence may not be, however, directly applicable to a condition where the initial forecast is made via a rational process based on the observation of past data. Although some positive impact of a separately prepared initial forecast has been suggested by some forecasting researchers, it is unclear yet as to the impact of an initial forecast on comparative accuracy in time series judgmental adjustment (cf. [2,10,86,87]). A null hypothesis investigates the impact of initial forecasts on subsequent forecast performance:

$H_{1b}$ : There is no difference in forecast performance between the no-initial forecast group and the initial forecast group.

## 3.2. Hypotheses about information reliability

Impact on information acquisition: In an information purchase task, reliability can be manipulated as either a between- (e.g., a set of equally reliable information) or a within factor (e.g., a mix of high and low reliability information) ([55]). In the between-reliability context, less amount of information is generally acquired in the high-than in the low-reliability condition ([55,16]). In the other within-reliability context, more reliable information is preferred but there appears to be considerable mispurchase of less reliable information ([46,16]). A null hypothesis is formulated to examine some biases involved in information seeking strategies such as mis-acquisition and sub-optimality as follows:

$H_{2a}$ : There is no difference in information acquisition behaviour between the high-reliability and the low-reliability conditions.

Impact on information utilisation: It may be apparent that the acquisition of high-reliable information would contribute to decision performance if decision makers are capable of appropriately taking advantage of the acquired information. Whilst only a few studies examined this issue in an information purchase context, this expectation was upheld by Levine and Samet ([55]). They found that accuracy was in an expected order of reliability: that is, the accuracy of the high-reliability group was significantly greater than that of the low-reliability group (p < 0.01). This suggests that “subjects sought to identify a high-reliable source and then took advantage of information received from it” (p. 417). The decision accuracy was, however, generally low, less than half correct (37% to 46% correct). In support of Levine and Samet ([55]), Lim and O'Connor ([59]) found that whilst people were far from optimal, they appeared to be able to take advantage of reliable information. We will vary the reliability of the information cues and examine its impact on forecast performance. The null hypothesis is formulated:

$H_{2b}$ : There is no difference in forecast performance between the low-reliability group and the high-reliability group.

## 3.3. Hypotheses about learning

Impact on information acquisition: A prime concern of learning in information acquisition is whether people could discern the information value and learn over trials to acquire information where its value outweighs its costs, given multiple pieces of information with varying accuracy. The empirical evidence generally suggests that people are not rapid learners about optimal purchasing ([52]). The learning, if any, was generally slow ([17]). Perhaps, it is due to the complexity of the task itself where people need to exercise more cognitive efforts. In stressing this point, Connolly and Gilani ([15]), p. 345 stated “given the complexity of the (information purchase) task..., it is perhaps surprising that any learning was demonstrated.” On the other hand, some ([52]) found that people appeared to learn slowly only for the highly-reliable information. The learning conditional on information reliability has also been suggested in Connolly and Serre ([16]). This mixed evidence leads us to a null hypothesis that:

$H_{3a}$ : People do not learn over trials to acquire the optimal amount of information.

Impact on information utilisation: Improvement in decision performance over trials in an information purchase task is closely related to people's ability at the prior stage (i.e., information acquisition). They would most likely improve performance if they are able to select good information as much as they can process. However, most empirical studies suggest that people are not normative in purchasing good information. Lim and O'Connor ([59]) also showed that people did not appropriately discern good information. Thus, the evidence on the improvement of decision performance over trials is equivocal. A pessimistic finding was reported by Wallsten ([100]) who had students make a decision about a dominating colour based upon their observations of a series of light flashes. They could buy as many observations as they wished before making a final decision. There was “virtually no change from block 1 to block 5” (p. 245) in stopping probabilities, though the experiment was practised over three days. On the other hand, a contrasting finding was reported by Connolly and Gilani ([15]) who found significant improvement in accuracy over time in an MCPL (Multiple Cue Probability Learning) task. We wish to determine whether people learn over time to improve their acquisition and use of information cues. The mixed evidence leads to a null hypothesis formulated as:

$H_{3b}$ : There is no improvement in forecast performance over trials.

## 3.4. Hypotheses about decision support

Impact on information acquisition: Information overload ([68]) may be a problem which time series forecasters often face in real business settings. It is expected that as information load increases, they might try to reduce mental efforts and thus, more frequently use an aggregation DSS. Few studies have addressed this issue at an information purchase task. Recently, Todd and Benbasat ([97]) showed that those with a DSS did not attend to more information than those without it. This behaviour seems contrary to intuition. They attributed this finding to a cost and benefit mechanism ([4]), i.e., people did not necessarily use more information due to its increased mental efforts, despite the easier interface for information access offered by the DSS. We wish to examine this issue in a time series context. A null hypothesis is that:

$H_{4a}$ : There is no difference in the frequency of using DSS, regardless of the amount of information acquired.

Impact on information utilisation: The claim made by researchers ([47,94]) concerning the positive impact of DSS on decision quality has not been well borne out ([89]). Empirical evidence is limited and mixed in information seeking task settings: Connolly and Thorn ([17]) in favour of decision aids and Lewis et al. ([57]), p. 272 claiming them as “superfluous”. Lewis et al. ([57]) found that even if people tended to employ the representativeness heuristic ([99]), there was no significant deviation in accuracy between subjects’ decision and the model of a man based on the same cues as attended by the subjects. Mechanical combination has been, however, strongly endorsed by most researchers in judgmental psychology ([27,19]) and forecasting ([53]). Connolly and Thorn ([17]) supported this claim at an information purchase task by demonstrating greater benefits due to the black-box decision aids which enabled both weighting and aggregation of information selected by people. Overall the decision aid substantially improved decision performance by 49% (p < 0.05).

The aforementioned two studies did not directly examine the ability of people to attach subjective weighting for the information they selected. It is, however, an important issue which should not be neglected in the provision of an aggregation DSS. Lim and O'Connor ([59]) questioned if people can perform cue weighting well in a single cue task. In forecasting, there has also been considerable debate between equal and unequal weighting in combining multiple forecasts. Some advocated equal weighting whereas others did not ([12]). Using the framework of the Lens model ([8]), some research has been devoted to the comparison of subjective weights to statistical weights and the results have also been equivocal ([81]). Unlike Connolly and Thorn ([17]), we designed a DSS which allows mechanical aggregation of information based on subjective weighting. Thus, any difference in judgmental forecast performance could be attributed to a problem of aggregation. However, equivocal findings ([88,73]) on the ability of people to accurately indicate cue weights lead to a null hypothesis on the utility of this DSS as:

$H_{4b}$ : There is no difference in forecast performance between the DSS group and the no DSS group.

## 4. Research methodology

## 4.1. Subjects

The subjects were 64 postgraduate students enrolled in an advanced post-graduate subject at the University of New South Wales, Australia. The overwhelming majority of them were part-time students with full-time employment in business. They were required to participate as part of the course as announced by the lecturer in charge. There were winner-takes-all monetary incentives of A\$50 for each experimental treatment. Casual observation of students indicated that the incentives seemed to motivate them strongly in the task.

## 4.2. Experimental design

This study was conducted as a 2 (initial forecast vs. no initial forecast) × 2 (low vs. high reliability) × 3 (blocks) factorial design. The first factor was operationalised by assigning the subjects into one of the two experimental conditions – the initial and the no-initial forecast groups. The initial forecast group was asked to extrapolate an initial (eyeballing) forecast (on each trial) based on observing the pattern of past time series data before seeing any information. On the other hand, the no-initial forecast group was not required to make an initial forecast. The remaining task requirements for both groups were identical: acquire information and make a final forecast. The interactive nature of the task instrument (hereafter called Greviser) enabled both groups to acquire whatever amount of information they wished and to revise their forecasts as many times as they wanted.

The second factor, reliability, consisted of two levels – high and low. Three cues were provided to both groups – a statistical forecast and two causal pieces of information. The task was to forecast sales of new nutritious soft drinks at a famous surfing beach (Bondi beach) in Sydney, Australia. Soft drink sales are largely determined by two causal cues – the temperature of the day and the number of visitors to the beach. Different cue validities were obtained by adding different levels of errors to the actual values. For the high-reliability condition, there were three cues of different validity: temperature (high), number of visitors (medium) and a (damped) statistical time series forecasts (low). In the low-reliability condition, the validity of all cues was approximately equal to that of the statistical forecast in the high-reliability condition. Since the task data was artificially generated, simulation was required to establish stable cues in accordance with the experimental design. $^{2}$ The averaged $r_{xy}$ (between the actual and cues) of the simulation was 0.926, 0.704 and 0.493 respectively for high, medium and low cue validities.

Each subject forecasted today's orders for 21 consecutive days. Feedback on the previous day's sales was provided on each iteration. To determine whether there was any improvement over time, these iterations were segmented into three time blocks of seven days each. $^{3}$

## 4.3. Task instrument

We employed the regression approach developed by Connolly and Gilani ([15]) to examine information acquisition and utilisation behaviour.

Information value was set in accordance with the conceptual guideline described earlier. As mentioned, the time series was generated from real temperature data at Bondi beach, 09.00 a.m. and this was obtained from the Bureau of Meteorology, Australia. The formula to generate actual time series (i.e., sales) was as follows:

$$
\mathrm{SALES} _ {\mathrm{t}} = 1 0 0 \times \text { TEMPERATURE } _ {\mathrm{t}} + 0. 1
$$

$$
\times \text { TEMPERATURE } _ {t} (t = 0, 1, 2,..., i)
$$

The first term in the equation above was to transform temperature data into the realistic forecast dimension and the second, to add a small simple linear trend. The sales were transferred back to its original scale with random errors added to control the strength of the correlation relationship, i.e., reliability as follows:

$$
\text { CAUSAL   INFORMATION } _ {t} = \text { SALES } _ {t} / 1 0 0 + e _ {t}
$$

The task tool, Greviser, was developed by the first author. It is a DSS and as such, provides decision support features ([94]) such as past time series, modelling capability, a graphical interface and feedback. The interface was user-friendly for the novices to be able to use without familiarisation. Some of the design characteristics include that:

\- Three icons for information were displayed on the right-top corner of Greviser. Request for the information was simply made-by a mouse click on the icon, upon which the icon opened a horizontal bar chart detailing information for the three consecutive past days from today. The statistical forecast was also displayed in bar chart form. It should be noted that people could use their discretion as to whether to acquire information or not. All cues were acquired sequentially, i.e., the subject decided whether or not to add another cue after considering the previous cue.

\- A decision aid icon was also provided underneath the information icons to facilitate a what-if capability ([94]). Upon a mouse click, it displayed all information they had acquired at that stage, along with the initial forecast (if in the initial forecast group). Then, people were able to select their own weighting system with a mouse. It was interactive and user-friendly and thus, they could access it at any stage of the forecasting process and change their weighting. After the subjects were happy, the decision aid aggregated the information they had acquired according to the subjective weighting. There was no restriction on the sum of weights and normalisation was automatically made in case the weights did not sum to unity.

\- Feedback on accumulated information charges (see Section 4.5.) was provided at the end of each trial. Their forecast performance was also presented in a graphical bar chart. But the performance of information cues was not provided.

## 4.4. Procedure

Subjects were randomly assigned to experimental conditions on entering the laboratory. They were briefed about Greviser and how to win the prize money. Experimenters also explained information costs and the penalty function (namely charges to be discussed later) which the subjects were asked to minimise. For subjects in the initial forecast condition, they were required to graphically extrapolate today's forecast using a mouse. Then, they were provided with the icons of information they could acquire, to which they could, if thought necessary, revise their forecast made earlier (in the initial forecast condition). This was repeated for 21 days. Prior to a real session, subjects performed a familiarisation (practice) session.

## 4.5. Analysis methodology

This study examined judgmental forecasting with regards to the two aspects - (1) information acquisition and (2) information utilisation. The former was measured by:

1. Acquisition: the accumulated pieces of information subjects acquired prior to reaching their final forecast.

2. Optimal acquisition: The optimal number of cues was set differently for the low- and the high-reliability condition - 2 and 1 respectively. The experimental conditions were controlled such that a rational forecaster should acquire only the best information in the high-reliability condition. On the other hand, in the low-reliability condition, marginal benefits from additional information would decrease at the second item acquired.

Information utilisation (termed forecast performance) was measured by:

1. MAPE $_{final}$ : Mean Absolute Percentage Error of final forecasts ([60]),

2. Improvement in the forecasts, defined as: $IMP_{best} = APE_{best}-APE_{final}$ where $APE_{best}(APE_{final})$ represents the Absolute Percentage Error of the best information (the final forecast). The best information was the temperature cue in the high-reliability condition, whereas the damped statistical forecast was selected among the three cues of equal validity in the low-reliability condition. Thus, $IMP_{best}$ represents improvement in accuracy of the final forecast over the most reliable (best) information in each reliability condition.

3. Charges: The sum of (1) penalty costs based on MSE (Mean Squared Error) for subjects' final forecasts and (2) information acquisition charges (see [15]). All cues were charged at the same rate.

High intercorrelations and conceptual dependency among these multiple dependent variables necessitated the employment of MANOVA ([95,45]). $^{4}$ Thus, a 2 (initial forecasts)x2(reliability)x3 (blocks) MANOVA was performed on both information acquisition and utilisation measures. For any significant multivariate effect, post-hoc ANOVAs followed to determine the nature of the effect by the manipulated factors. Polynomial trend analyses were used for time blocks.

## 5. Results

## 5.1. Effect of initial forecasts

$H_{1a}$ : Impact on information acquisition: The first hypothesis examines whether a reluctance to update the initial forecast would lead to reduced information acquisition for the initial forecast, compared to the no-initial forecast group. As expected, the no-initial group acquired more information (0.92 pieces) than the initial forecast group (0.85 pieces). Those in the initial forecast condition appeared to acquire none or one piece of information more frequently. On the other hand, those in the no-initial forecast condition appeared to prefer to attend causal information, particularly temperature and visitor information in combination. However, the results of MANOVA (reproduced in the Appendix) indicated that this difference did not reach significance. That is, neither the main (p = 0.507) nor any interaction effect (p = 0.571) was found to be significant for the factor initial forecast regarding information acquisition. Thus, $H_{1a}$ is accepted and there was no significant difference in information seeking between the two groups.

$H_{1b}$ : Impact on information utilisation: The second hypothesis was to test the claim by some forecasting researchers that the independent preparation of an initial forecast would improve decision performance. MANOVA revealed that there was no significant difference in forecast performance between the initial forecast and the no-initial forecast group (p = 0.153). It should be, however, noted that the interactive nature of Greviser allowed people to finalise their forecasts at any stage of the task even without seeing any information. In this case, there existed practically no experimental difference between the two groups. The forecast performance would be affected by having the initial forecast only if subjects acquired any information. Thus, separate analyses were made for the two groups, categorised into (1) those who acquired none and (2) those who acquired at least one item of information. In the first case where no information was acquired, the no-initial (8.48) and the initial forecast group (8.65) did not differ in forecast accuracy (p = 0.732). However, in the other case where more than a piece of information was acquired the separate preparation of an initial forecast improved forecast accuracy (see Table 2). That is, those who made an initial forecast before seeing any information (7.19) were significantly more accurate than those without it (8.06) (t = 2.08, p = 0.038). Whilst this superior performance of the initial forecast group over the no-initial forecast group was also observed in both IMP $_{best}$ and charges, they did not reach significance (p > 0.1 for both). This evidence leads us to reject only weakly H $_{1b}$ . However, the independent preparation of an initial forecast appeared to be generally helpful.

## 5.2. Reliability effect

$H_{2a}$ : Impact on information acquisition: We examined if there was any difference in information acquisition strategies between the high- and the low-reliability condition. Two issues should be addressed in relation to information acquisition behaviour: (1) mis-acquisition (i.e., did they acquire more reliable information?) and (2) optimality in acquisition (i.e., did they acquire an optimal amount of information?). The results revealed a considerable degree of mis-acquisition and underpurchase.

## 5.2.1. Mis-acquisition

Remember, the optimal number of information cues was set at two pieces for the low-reliability condition and one for the high-reliability condition. The subjects should see only the temperature information, the most predictable in the high-reliability condition. On the other hand, in the low-reliability condition, acquiring one or

Table 2  
Effect of initial forecasts (when more than one piece of information was acquired).  
Table 3

<table><tr><td></td><td>n</td><td> $MAPE_{final}$ </td><td> $IMP_{best}$ </td><td>Charges</td></tr><tr><td>No initial forecast</td><td>385</td><td>8.06</td><td>-1.51</td><td>92.70</td></tr><tr><td>Initial forecast</td><td>370</td><td>7.19 **</td><td>-0.83</td><td>79.80</td></tr><tr><td>Average</td><td>(755)</td><td>7.63</td><td>-1.18</td><td>86.40</td></tr></table>

$$
\mathrm{p} <   0. 0 5.
$$

Mis-acquisition frequencies across reliability conditions

<table><tr><td rowspan="2"></td><td colspan="2">Optimal</td><td colspan="2">Non-optimal</td><td colspan="2">Total</td></tr><tr><td>n</td><td>%</td><td>n</td><td>%</td><td>n</td><td>%</td></tr><tr><td>High- reliability</td><td>90</td><td>6.7</td><td>510</td><td>37.9</td><td>672</td><td>50.0</td></tr><tr><td>Low-reliability</td><td>133</td><td>9.9</td><td>539</td><td>40.1</td><td>672</td><td>50.0</td></tr><tr><td>Total</td><td>223</td><td>16.6</td><td>1049</td><td>78.1</td><td>1344</td><td>100.0</td></tr></table>

three pieces of information was non-optimal. Observations reported in Table 3 were categorised into (1) optimal and (2) non-optimal acquisition. It is disappointing to find that people were far from optimal and considerable mis-acquisition was observed. In the high-reliability condition, the best information was acquired only scarcely although the accuracy would have been higher if they had relied on it. Only 24.2% of the subjects acquired temperature information either alone (13.4%) or in combination (10.8%), which was the best information in the high-reliability condition. This mis-acquisition was also observed in the low-reliability condition where the optimal number of cues was set at the second item. Only 19.8% acquired the optimal amount (i.e., two) and most subjects were unwilling to attend any information (40.3%). This suggests considerable difficulty for the subjects to discern information reliability.

## 5.2.2. Sub-optimality

People generally under-acquired information regardless of the reliability condition. In the high-reliability condition, they acquired about one item of information (0.79), albeit often not the best information. In the low-reliability condition, people also failed to acquire the optimal amount of information (0.99). The results of MANOVA indicated neither main (p = 0.366) nor interaction effect of varying reliability condition on the number of information acquired. In the light of the fact that the experimental conditions were set for those in the low-reliability condition to acquire more information (two items) than those in the high-reliability condition (one item), this suggests much more serious sub-optimality for the low-reliability group.

To summarise, there was no significant difference between the two groups in the number of information cues acquired and both groups commonly underselected information. Thus, $H_{2a}$ is accepted. It should be, however, noted that this under-acquisition tendency was more serious for the low-reliability group than those in the high-reliability condition. In that condition, considerable mis-acquisition was observed and the majority of people failed to discern the best information.

$H_{2b}$ : Impact on information utilisation: This hypothesis examines any difference in forecast performance between the low- and the high-reliability group. The results of MANOVA indicated a significant difference in forecast performance between the two conditions (F = 1303.154, p < 0.0005). The difference is reported subsequently concerning forecast performance, measured by three dependent variables: (1) accuracy, (2) improvement from the best information and (3) total charges.

Accuracy (MAPE $_{final}$ ): It was previously mentioned that there was substantial mis-acquisition of information and thus, people failed to acquire the best information in the high-reliability condition. Such mis-acquisition might have led to little difference in accuracy between the two groups. The accuracy of the high-reliability group (7.72) was only slightly higher than that of the low-reliability group (8.37). However, this difference did not reach significance (p > 0.1).

Improvement from the best information (Im MP $_{best}$ ) Insignificant differences in MAPE $_{final}$ , between the two groups necessarily meant that IMP $_{best}$ was significantly worse in the high- than the low-reliability group, as seen in Table 4 (F = 22.498, p < 0.0005). Interestingly, both groups did not outperform the best information (e.g., temperature in the high-reliability condition), despite their unwillingness to acquire any information as discussed earlier.

Table 4  
Forecast performance across reliability conditions

<table><tr><td></td><td> $\text{MAPE}_{\text{final}}$ </td><td> $\text{IMP}_{\text{best}}$ </td><td>Charges</td></tr><tr><td>High-reliability</td><td>7.72</td><td>-2.67</td><td>33.7</td></tr><tr><td>Low-reliability</td><td>8.37</td><td>-0.74</td><td>121.4</td></tr><tr><td>Average</td><td>8.04</td><td>-1.70</td><td>77.5</td></tr></table>

Table 5  
Learning in information acquisition and utilisation

<table><tr><td></td><td>Acquisition</td><td> $MAPE_{final}$ </td><td> $IMP_{best}$ </td><td>Charges</td></tr><tr><td> $Block_{1-7}$ </td><td>0.99</td><td>6.55</td><td>-0.12</td><td>49.10</td></tr><tr><td> $Block_{8-14}$ </td><td>0.82</td><td>8.09</td><td>-1.71</td><td>82.30</td></tr><tr><td> $Block_{15-21}$ </td><td>0.85</td><td>9.49</td><td>-3.28</td><td>101.20</td></tr><tr><td>Average</td><td>0.89</td><td>8.04</td><td>-1.70</td><td>77.50</td></tr></table>

Charges: The performance indicators mentioned above showed the limited ability of people to use diagnostic information given to the high-reliability group. However, the high-reliability group (\$33.65) incurred total charges significantly lower than those of the low-reliability group (\$121.35) (F = 142.060, p < 0.0005). It might have been due to (1) slight superiority in accuracy that could reduce the penalty for forecast errors (MSE) and (2) acquisition of fewer items of information.

To summarise, the above results suggest that the high-reliability group outperformed only marginally the low-reliability group. Thus, $H_{2b}$ is only weakly rejected. The main reason for the marginal superiority of the high-reliability over the low-reliability group may be attributed to flawed cognitive ability at the previous information acquisition stage: that is, (1) reluctance to process any additional reliable information and (2) people's limited ability to discern the high-reliable information.

## 5.3. Learning

$H_{3a}$ : Learning in information acquisition: Remember, the subjects performed a total of 21 trials which then, were divided into three blocks to see any learning effect. A prime interest here was if people learnt to acquire the optimal amount of information over trials. The results of MANOVA suggest a significant effect of block on the number of information items acquired (F = 2.294, p = 0.074). Follow-up ANOVAs showed a significant linear pattern over the three blocks for the number of items they acquired (F = 5.641, p = 0.021). But, an examination of the means for each block revealed the pattern was downwards (see Table 5). The same learning pattern was revealed for both reliability conditions. A good learner would be capable of changing his/her acquisition strategy according to the costs and benefits of information. Over trials, (s)he would increase acquiring information, where its benefits outweigh its costs, but decrease acquiring information with no/little marginal benefits. Thus, the number of information items they acquired would approach over trials the optimal number, set at two and one respectively for the high- and the low-reliability condition. People were, however, deficient in weighing information value against its costs. They were far from optimal even at the last block. In fact, information acquisition strategy of both groups rather worsened significantly. Thus, $H_{3a}$ is accepted.

$H_{3b}$ : Learning in information utilisation: The decreasing pattern in the number of information items acquired over time suggests that people relied on their intuition more and more in forecasting. This sub-optimal behaviour in information acquisition would have necessarily led to little, if any, improvement in forecast performance over time. The results of MANOVA revealed a significant impact of block on forecast performance (F = 14.432, p < 0.0005). However, it was a significant linear downward trend (F = 41.605, p < 0.0005). Their accuracy (MAPE) deteriorated from 6.55 at the first, 8.09 at the second to 9.49 at the last block (see Table 5). It is mysterious why they persistently relied on their intuition despite a considerable deterioration of their accuracy. This reliance would be justified only if their forecasts outperformed the best information provided. More disappointedly, however, the improvement from the best information also gradually deteriorated, as seen in Table 5 (F = 45.620, p < 0.0005). Not surprisingly, total charges significantly also increased over trials in a linear fashion (see Table 5) (F = 56.384, p < 0.0005). This evidence leads us to accept $H_{3b}$ .

## 5.4. Decision support effect

$H_{4a}$ : Decision support and information acquisition: The hypothesis was to examine if people increasingly used the DSS as they acquired more and more information. A Chi-square analysis presented in Table 6 shows a significant increasing use of decision aids as information load increased (p < 0.0005). Indeed, the average number of information items acquired was significantly more for the DSS group (1.57) than the no-DSS group (0.45), as seen in Table 7. In support of our proposition, Table 6 indicates that the use of the DSS generally led to increased accuracy and its efficacy was most prominent when they acquired all available information (10.28 vs. 5.71) (see Table 6). This suggests that people relied on the DSS as the information increased and appeared to successfully perform cue weightings. Thus, $H_{4a}$ is rejected.

Table 6  
Frequencies of DSS use and its effect on MAPE

<table><tr><td rowspan="2"></td><td colspan="4">Acquisition (number of cues acquired)</td></tr><tr><td>None</td><td>One</td><td>Two</td><td>Three</td></tr><tr><td>DSS not used</td><td>574 (8.66)</td><td>157 (8.10)</td><td>57 (7.52)</td><td>33 (10.28)</td></tr><tr><td>DSS used</td><td>15 (5.10)</td><td>266 (7.78)</td><td>172 (7.30)</td><td>70 (5.71)</td></tr><tr><td>Total</td><td>589 (8.57)</td><td>423 (7.90)</td><td>229 (7.36)</td><td>103 (7.17)</td></tr></table>

() = MAPE $_{final}$ , $X^{2} = 592.723$ , p < 0.0005.

$H_{4b}$ : Impact on information utilisation: In this study, the DSS mechanised only the aggregation of the acquired information. That is, when people decided to use the DSS, they had to indicate the weighting themselves for the information they had acquired. Then, the DSS combined the information selected and weighted by people. As seen in Table 7, those using the DSS were found to significantly outperform those not using the DSS for accuracy (t = 3.87, p < 0.0005) and IMP $_{best}$ , (t = -2.51, p = 0.012). Furthermore, this utility of the DSS which employed “automatic aggregation based on subjective weighting” was significantly more accurate than that of equal weighting (7.27 vs. 8.31) (t = 3.49, p < 0.005). This evidence leads us to reject $H_{4b}$ . Successful use of this DSS design may indicate that the element of judgment can be extended to the task of weighting, especially in a multiple cue task.

Table 7  
DSS effect on information acquisition and utilisation

<table><tr><td></td><td>n</td><td>Acquisition</td><td> $MAPE_{final}$ </td><td> $IMP_{best}$ </td><td>Charges</td></tr><tr><td>DSS not used</td><td>821</td><td>0.45</td><td>8.54</td><td>-2.07</td><td>79.0</td></tr><tr><td>DSS used (Total)</td><td>523(1344)</td><td>1.570.89</td><td>7.27***8.04</td><td>-1.13* -1.70</td><td>75.277.5</td></tr></table>

\*\*\* p < 0.01, \*p < 0.1.

## 6. Discussion

Judgmental approaches to forecasting are often adopted in practice ([66,18]). Development of computer software has, however, changed the practice of judgmental forecasting. Forecasters get access interactively to DSS/ EIS which provides not only graphical time series but also a variety of other information from different sources. The effectiveness of this practice is generally conditional upon the ability of forecasters to select diagnostic information that would decrease the uncertainty of forecasting and appropriately incorporate it into final forecasts ([59]). While this ability has been of interest to some researchers ([25,15-17]), most empirical time series forecasting studies have generally failed to deal with complexities involved in this practice and simply concentrated on accuracy and improvement. Furthermore, few DSS/ EIS studies have been concerned with the effectiveness of information acquisition and selection strategies.

The dysfunctional effect of the anchoring-adjustment heuristic ([99]) has been overwhelmingly documented in literature. The impact of the preparation of an initial forecast has received little attention, despite a strong recommendation of its separate preparation ([53,62]). We found that this was helpful, perhaps by lessening any possible anchoring on a useless value, i.e., people produced more accurate forecasts with an independent initial forecast than those without it. While this practice could not eliminate the anchoring-adjustment bias ([9]), it would prevent people from starting with an irrelevant anchor ([43]). This finding supports the advice from most forecasting researchers that the initial forecast be prepared separately. Moreover, people's reluctance to process additional information was commonplace, no matter whether the initial anchor was present or not. On a broader scale, it also raises the question of whether people should make their own initial judgments before interrogating and using information supplied by the EIS.

The conservatism (i.e., under-acquisition of information, [46,78,17]) was also observed regardless of the information reliability condition. People relied very heavily on their intuition in forecasting and thus, did not acquire much information. This under-acquisition may be surprising in that their forecast accuracy was inferior to the good information provided. Such conservative behaviour in information acquisition appeared to be generally consistent with Lim and O'Connor ([59]) where persistent anchoring on their initial forecast was also observed. A more pessimistic finding is that this sub-optimality was not easily overcome. Indeed, they did not learn over trials and became significantly worse. This mis-acquisition also carried over to forecast performance that also deteriorated over time (cf. [100]). Thus, those in the high-reliability condition outperformed only slightly those in the low-reliability condition. The limited ability of people to adjust their behaviour over time is not surprising in information purchase tasks. People did not learn a very simple purchasing strategy in a much simpler task ([46]). Slow learning was also observed in Connolly and Thorn ([17]). In their study, people learnt over time to buy good information only slowly even when the good information was far more reliable (96% accountable for the criterion value).

Learning has long been an issue for MCPL researchers ([35,36,7,34]). After reviewing the literature in relation to learning, Brehmer ([7]) made a pessimistic conclusion, as suggested by the title of his paper “not from experience”. Two prime reasons which have been suggested for impaired learning ([34]) include: (1) unavailable or flawed feedback ([39,42]) and (2) cognitive biases involved in decision making, due to inadequate learning from feedback ([7]). In the present study, the feedback was both available and unambiguous. However, the feedback was often ignored. We found some cognitive biases, acting as obstacles to task learning: (1) mis-acquisition of less reliable information ([16]) and (2) under-acquisition and reluctance to pay for the best information ([46]), despite the inferiority of judgmental forecasts to it. Mis-acquisition may not be surprising because even experts are often influenced by irrelevant information ([33]). These findings question the ability of time series forecasters to select good information, a claim made by most MCPL researchers ([20,27]). This also lends some support for the extensive use of Expert Systems to select the best forecasting method, as in most commercial statistical forecasting packages. An alternative explanation is that the subjects gave up any hope of learning anything useful from the information they purchased. The cost of buying information is “up-front” and certain, but the benefits are delayed and uncertain. If little steady gain was achieved, subjects may have simply sought to minimise their (certain) expenses by buying less information.

In addition to mis-acquisition, some part of sub-optimality in this task could also be attributed to the limited cognitive ability in combining multiple pieces of information ([58,53]). The pessimistic finding discussed above suggests some need for a DSS in this task. Connolly and Thorn ([17]) suggested beneficial effects of the decision aids that provided automatic aggregation and took away even weightings from people. Although this design principle could overcome considerable cognitive biases, there are some issues to be discussed. Indeed, such automatic DSS may not be effective in incorporating broken-leg $^{5}$ cues ([49]) because the required weightings should be obtained from past events. A behavioural issue which also needs to be addressed is whether people are willing to accept and rely on such DSS. It is also at issue in the bootstrapping literature ([65,21]) that people are reluctant to rely on the model, due to their being afraid of “replacement” by the model. It may be more serious for risky and important decisions ([74]). A more plausible approach is to trust the job of weighting to people. We found that this framework (automatic combination based upon subjective weighting) significantly improved forecast performance and encouraged people to attend to more information. This suggests that conservatism could be overcome to an extent. In this framework of the interactive DSS, people may feel less threat of being replaced. Moreover, people may easily incorporate new event information through weightings. Further research is, however, required on this notion of the DSS, since people also have a problem of specifying weights ([59]). This design framework may be useful, particularly in situations (e.g., new products, lack of data, etc.) where contextual information needs to be incorporated into the process of judgmental adjustment.

To summarise, this study has investigated the effectiveness of judgmental forecasting with an interactive DSS. Results indicate that people appeared to favour their intuition in forecasting. Thus, they were reluctant to process additional information and under-acquired important diagnostic information. This sub-optimal behaviour was not easily overcome. Some reasons may be advanced. First, these sceptical findings may be due to unfamiliarity with the DSS. However, they were given a practice session to get used to the tool and the subjects seemed to enjoy the session. It is also interesting to note that the subjects were post-graduate students who were majoring in Information Systems. They were, thus, arguably committed to the use of aids like the DSS/EIS. Second, the subjects might have been bored with the task. The monetary incentive scheme, however, appeared to be a sufficient motivator. In addition, the task took less than an hour. At the end, they indicated the task was challenging. Thirdly, the purchase task itself might have been too difficult ([15]). Moreover, the dynamic nature of the time series task may have added to more difficulty. Lastly and more importantly, they might have felt that they could get all the information they wanted from the time series graph and did not need any extra information.

The findings of the present study should be generalised with caution. First, only three pieces of information were made available. In practice, forecasters need to process much more information. However, if, as this study suggests, people have difficulty with just three pieces of information, they should have a lot more difficulty with more information. Second, only one time series was provided in the present study. The characteristics of the time series were, however, found to affect judgmental adjustment ([86,87]). Thirdly, the intercorrelations of cues ([28]) were not considered. The time series used in causal adjustment were temperature data over certain periods with visitor information generated from them. Therefore, it may not reflect the true relationships between the time series and the causal information. It should be, however, noted that in real business forecasting contexts, cues are more often correlated with each other. Further research may be conducted with time series data and real causal information associated with the series, although this may be difficult to discover. Lastly, Greviser was designed to repeat the task over a certain number of trials with short intervals. This may not represent the learning in reality ([42]). Due to the problems (e.g., time, other intervening factors) in observing the adjustment process with longer intervals, however, longitudinal laboratory studies have been adopted as a viable approach to real decision making ([23,89]). Further research is required to address these additional issues. Considering that judgmental adjustment is a common practice in most firms ([54]), research is also needed to understand when decision aids can be most helpful for judgmental adjustment. In particular, this study can be replicated with the eye movement technique to explore the interactive nature of information acquisition in time series judgmental forecasting (e.g., [84]).

## 7. Conclusions and implications for DSS design

This study examined the efficacy of how people make forecasts in the light of information coming from different sources. This issue is of great importance to the design of the DSS, since they assume that people are able to effectively integrate such information into the final forecast.

The findings of this paper questioned the effectiveness of this design framework. The prime reason is that the benefits of having the element of judgment within the DSS may outweigh the detriments they may bring into the task. Here, the benefits include forecasters' contextual expertise ([87]) and ability to identify broken-leg cues ([64,49]). On the other hand, the detriments are the cognitive biases as found in psychology (1441, 1851, 151).

The most conspicuous hazard for permitting judgmental intervention in the DSS may be conservatism ([26,63]). We observed this heuristic persistently operating at time series tasks, i.e., people placed too much faith in their own judgment and were reluctant to process any additional diagnostic information ([99]). They employed this anchoring adjustment heuristic, arguably to save their cognitive efforts ([96]) required in processing additional data. Indeed, the DSS may not entirely prevent people from adopting short cuts to reduce their cognitive efforts (cf. [97]) and thus, is subject to a number of cognitive biases ([51]). The sceptical view over the utility of DSS has been documented in the DSS literature ([50,89]).

The results of this paper suggested two alternatives for the design of DSS. The first is that the DSS should be designed to allow for only a minimal role of unaided forecasters ([70]) in any judgmental adjustment, especially when the model is quite reliable and people do not have much extra-model information to contribute ([37]). This guideline is in parallel with the pessimistic views about judgmental decision making ([44]). Given that the element of judgment is necessary for forecasting in most forms, the second and more reasonable approach would be to incorporate some internal debiasing mechanisms into the DSS (see [31,82]). We suggest that decision support be provided for every stage of the judgmental adjustment processes and some debiasing mechanisms should be incorporated into the DSS to help forecasters at every stage of judgmental adjustment – anchor development, selection of reference forecasts, combination and lastly feedback. A suggested approach would be to incorporate any contextual knowledge into an independent

judgmental forecast. Then, the DSS may combine it into the final forecast in a mechanical way ([53]). Alternatively, the DSS may allow people to take some role in the weighting of cues. The DSS should be, however, designed to monitor their performance and alert (more strongly) forecasters against any systematic bias (e.g., conservatism) (e.g., [1]).

## Appendix A

MANOVA Table for information acquisition

<table><tr><td>Source</td><td>Wilks Lambda</td><td>Approx F</td><td>Hyp. df</td><td>Error df</td><td>Sig of F</td></tr><tr><td colspan="6">Between subjects</td></tr><tr><td>Initial Fcast (I)</td><td>0.977</td><td>0.688</td><td>2</td><td>59</td><td>0.507</td></tr><tr><td>Reliability (R)</td><td>0.967</td><td>1.022</td><td>2</td><td>59</td><td>0.366</td></tr><tr><td> $I \times R$ </td><td>0.981</td><td>0.566</td><td>2</td><td>59</td><td>0.571</td></tr><tr><td colspan="6">Within subjects</td></tr><tr><td>Block</td><td>0.861</td><td>2.294</td><td>4</td><td>57</td><td>0.070</td></tr><tr><td> $I \times B$ </td><td>0.924</td><td>1.165</td><td>4</td><td>57</td><td>0.366</td></tr><tr><td> $R \times B$ </td><td>0.959</td><td>0.615</td><td>4</td><td>57</td><td>0.653</td></tr><tr><td> $I \times R \times B$ </td><td>0.906</td><td>1.476</td><td>4</td><td>57</td><td>0.221</td></tr></table>

MANOVA Table for information utilisation

<table><tr><td>Source</td><td>Wilks Lambda</td><td>Approx F.</td><td>Hyp. df</td><td>Error df</td><td>Sig, of F.</td></tr><tr><td colspan="6">Between subjects</td></tr><tr><td>Initial Fcast (I)</td><td>0.914</td><td>1.826</td><td>3</td><td>58</td><td>0.153</td></tr><tr><td>Reliability (R)</td><td>0.015</td><td>1303.154</td><td>3</td><td>58</td><td>0.000</td></tr><tr><td>I × R</td><td>0.915</td><td>1.798</td><td>3</td><td>58</td><td>0.158</td></tr><tr><td colspan="6">Within subjects</td></tr><tr><td>Block (B)</td><td>0.388</td><td>14.432</td><td>6</td><td>55</td><td>0.000</td></tr><tr><td>I × B</td><td>0.938</td><td>0.604</td><td>6</td><td>55</td><td>0.726</td></tr><tr><td>R × B</td><td>0.379</td><td>15.033</td><td>6</td><td>55</td><td>0.000</td></tr><tr><td>I × R × B</td><td>0.853</td><td>1.586</td><td>6</td><td>55</td><td>0.169</td></tr></table>

## References

[1] A.J. Adams, Procedures for Revising Management Judgements Forecasts, Journal of Accounting Research 14, No. 3, 52–57 (1986).

[2] P. Angus-Leppan and V. Fatseas, The Forecasting Accuracy of Trainee Accountants Using Judgemental and Statistical Techniques, Accounting and Business Research 16, 179–188 (Summer 1986).

[3] J.S. Armstrong, Long Range Forecasting: From Crystal Ball to Computer, 2nd edition (John Wiley and Sons, New York, 1985).

[4] L.R. Beach and T.R. Mitchell, A Contingency Model for the Selection of Decision Strategies, Academy of Management Review 3, 439–449 (1978).

[5] I. Benbasat and R. Taylor, Behavioral Aspects of Information Processing for the Design of Management Information Systems, IEEE Transactions on Systems, Man, and Cybernetics, SMC-12, No. 4, 439–450 (1982).

[6] J. Bowen and Z. Qiu, Satisficing When Buying Information, Organizational Behavior and Human Decision Processes 51, 471–481 (1992).

[7] B. Brehmer, In One Word: Not from Experience, Acta Psychologica 45, 223–241 (1980).

[8] Brunswik, E., The Conceptual Framework of Psychology (Chicago: University of Chicago Press, 1952).

[9] S.A. Butler, Anchoring in the Judgmental Evaluation of Audit Samples, The Accounting Review, LXI, No. 1, 101–111 (1986).

[10] R. Carbone and W.L. Gorr, Accuracy of Judgemental Forecasting of Time Series, Decision Sciences 16, 153-160 (1985).

[11] M.P. Carter, The Valuing of Management Information. Part I: The Bayesian Approach, Journal of Information Science 10, 1–9 (1985).

[12] R. Clemen, Combining Forecasts: A Review and Annotated Bibliography, International Journal of Forecasting 5, 559–583 (1989).

[13] F. Collopy, Forecasting and Information Systems: Is It Time for a Trial Marriage, The Forum (Fall 1993).

[14] T. Connolly, 1988, Studies of Information-Purchase Processes, in: B. Brehner and C.R.B. Joyce, Eds., Human Judgment: The SJT View, 401–425 (North-Holland, 1988).

[15] T. Connolly and N. Gilani, Information Search in Judgment Tasks: A Regression Model and Some Preliminary Findings, Organizational Behavior and Human Performance 30, 330–350 (1982).

[16] T. Connolly and P. Serre, Information Search in Judgment Tasks: The Effects of Unequal Cue Validity and Cost, Organizational Behavior and Human Performance 34, 387–401 (1984).

[17] T. Connolly and B K. Thorn, Predecisional Information Acquisition: Effects of Task Variables on Suboptimal Search Strategies, Organizational Behavior and Human Performance 39, 397–416 (1987).

[18] D.J. Dalrymple, Sales Forecasting Practices: Results from a United States Survey, International Journal of Forecasting 3, 379–391 (1987).

[19] R.M. Dawes, The Robust Beauty of Improper Linear Models in Decision Making, American Psychologist 34, No. 7, 571–582 (1979).

[20] R.M. Dawes and B. Corrigan, Linear Models in Decision Making, Psychological Bulletin 81, No. 2, 95–106 (1974).

[21] R.M. Dawes, D. Faust and P.E. Meehl, Clinical Versus Actuarial Judgment, Science 243, 1668–1673 (March 1989).

[22] M.J. Driver and T.J. Mock, Human Information Processing Decision Style Theory, and Accounting Information Systems, The Accounting Review, 490–508 (July 1975).

[23] N.L. Eckel, The Impact of Probabilistic Information on Decision Behaviour and Performance in an Experimental Game, Decision Sciences 14, No. 4, 483–502 (1983).

[24] R.H. Edmundson, M. Lawrence and M. O'Connor, The

Use of Non-Time Series Information in Sales Forecasting: A Case Study, Journal of Forecasting 7, 201–211 (1988).

[25] Edwards, W., Optimal Strategies for Seeking Information: Models for Statistics, Choice Reaction Times, and Human Information Processing, Journal of Mathematical Psychology 2, 312–329 (1965).

[26] W. Edwards, Conservatism in Human Information Processing, in: D. Kahneman, P. Slovic and A. Tversky, Eds., Judgment under Uncertainty: Heuristics and Biases, 359–369 (Cambridge University Press, New York, 1982).

[27] H.J. Einhorn, Expert Measurement and Mechanical Combination, Organizational Behaviour and Human Performance 7, No. 1, 86–106 (1972).

[28] H.J. Einhorn and R.M. Hogarth, Behavioral Decision Theory: Process of Judgement and Choice, Annual Review of Psychology 32, 53–88 (1981).

[29] M.S. Feldman and J.G. March, Information in Organizations as Signal and Symbol, Administrative Science Quarterly 26, 171–186 (1981).

[30] G.A. Feltham, The Value of Information, Accounting Review 43, 684–696 (1968).

[31] B. Fischhoff, Debiasing, in: D. Kahneman, P. Slovic and A. Tversky, Eds., Judgment under Uncertainty: Heuristics and Biases, 422–444 (Cambridge University Press, New York, 1982).

[32] L.S. Fried and C.R. Peterson, Information Seeking: Optional Versus Fixed Stopping, Journal of Experimental Psychology 80, No. 3, 525–529 (1969).

[33] G.J. Gaeth and J. Shanteau, Reducing the Influence of Irrelevant Information on Experienced Decision Makers, Organizational Behavior and Human Performance 33, 263–282 (1984).

[34] H.N. Garb, Clinical Judgment, Clinical Training, and Professional Experience, Psychological Bulletin 105, No. 3, 387–396 (1989).

[35] L.R. Goldberg, The Effectiveness of Clinician's Judgements: The Diagnosis of Organic Brain Damage from the Bender-Gestalt Test, Journal of Consulting Psychology 23, 25–33 (1959).

[36] L.R. Goldberg, Simple Models or Simple Processes? Some Research on Clinical Judgement, American Psychologist 23, No. 7, 483–496 (1968).

[37] P. Goodwin and G. Wright, Improving Judgmental Time Series Forecasting: A Review of the Guidance Provided by Research, International Journal of Forecasting 9, 147–161 (1993).

[38] P.E. Green, M.H. Halbert and J.S. Minas, An Experiment in Information Buying, Journal of Advertising Research, 17–23 (1964).

[39] K.R. Hammond, D.A. Summers and D.H. Deane, Negative Effects of Outcome-Feedback in Multiple-Cue Probability Learning, Organizational Behavior and Human Performance 9, 30–34 (1973).

[40] R.L. Hershman and J.R. Levine, Deviations from Optimum Information-Purchase Strategies in Human Deci-

sion-Making, Organizational Behavior and Human Performance 5, 313–329 (1970).

[41] R.W. Hilton, The Determinants of Information Value: Synthesizing Some General Results, Management Science 27, No. 1, 57–64 (1981).

[42] R.M. Hogarth, Beyond Discrete Biases: Functional and Dysfunctional Aspects of Judgmental Heuristics, Psychological Bulletin 90, No. 2, 197–217 (1981).

[43] R.M. Hogarth, Judgement and Choice, 2nd edition (John Wiley and Sons, 1987).

[44] R.M. Hogarth and S. Makridakis, Forecasting and Planning: An Evaluation, Management Science 27, No. 2, 115–137 (1981).

[45] C.J. Huberty and J.D. Morris, Multivariate Analysis Versus Multiple Univariate Analyses, Psychological Bulletin 105, No. 2, 302–308 (1989).

[46] A.F. Kanarick, J.M. Huntington and R.C. Petersen, Multi-Source Information Acquisition with Optional Stopping, Human Factors 11, No. 4, 379–386 (1969).

[47] P.G.W. Keen and M.S. Scott-Morton, Decision Support Systems: An Organizational Perspective (Addison-Wesley Publishing Company, Sydney, 1978).

[48] T. Kida, The Impact of Hypothesis-Testing Strategies on Auditors' Use of Judgment Data, Journal of Accounting Research 22, No. 1, 332–340 (1984).

[49] B. Kleinmuntz, Why We Still Use Our Heads Instead of Formulas: Toward an Integrative Approach, Psychological Bulletin 107, No. 3, 296–310 (1990).

[50] J.E. Kottemann and W.E. Remus, Evidence and Principles of Functional and Dysfunctional DSS, OMEGA The International Journal of Management Science 15, No. 2, 135–143 (1987).

[51] C.T. Kydd, Cognitive Biases in the Use of Computer-Based Decision Support Systems, OMEGA The International Journal of Management Science 17, No. 4, 335–344 (1989).

[52] J.T. Lanzetta and V.T. Kanareff, Information Cost, Amount of Payoff, and Level of Aspiration as Determinants of Information Seeking in Decision Making, Behavioral Science 7, 459–473 (1962).

[53] M.J. Lawrence, R.H. Edmundson and M.J. O'Connor, The Accuracy of Combining Judgemental and Statistical Forecasts, Management Science 32, No. 12, 1521–1532 (1986).

[54] M.J. Lawrence, R.H. Edmundson and M.J. O'Connor, Sales Forecasting Practices in Consumer Products Organisation, Working Paper (School of Information Systems, The University of New South Wales, Australia, 1993).

[55] J.M. Levine and M.G. Samet, Information Seeking with Multiple Sources of Conflicting and Unreliable Information, Human Factors 15, No. 4, 407–419 (1973).

[56] J.M. Levine, M.G. Samet and R.E. Brahlek, Information Seeking with Limitations on Available Information and Resources, Human Factors 17, No. 5, S02–513 (1975).

[57] B. Lewis, M.D. Shields and S.M. Young, Evaluating Human Judgments and Decision Aids, Journal of Accounting Research, 271–285 (Spring 1983).

[58] R. Libby, Accounting and Human Information Processing: Theory and Applications, 74–123 (Prentice-Hall, Inc., 1981).

[59] J.S. Lim, and M.J. O'Connor, Systems to Support Judgmental Adjustment of Initial Forecasts, Proceedings of the Twenty-Seventh Hawaii International Conference on System Sciences, 263–271 (Jan. 1994).

[60] E. Mahmoud, The Evaluation of Forecasts, in: S. Makridakis and S.C. Wheelwright, Eds., The Handbook of Forecasting: A Manager's Guide, 504–522 (John Wiley and Sons, New York, 1987).

[61] E. Mahmoud, Combining Forecasts: Some Managerial Issues, International Journal of Forecasting 5, 599–600 (1989).

[62] S. Makridakis, Metaforecasting: Ways of Improving Forecasting Accuracy and Usefulness, International Journal of Forecasting 4, 467–491 (1988)

[63] R.O. Mason and H. Moskowitz, Conservatism in Information Processing: Implications for Management Information Systems, Decision Science 3, No. 4, 35–55 (1972).

[64] P.E. Meehl, When Shall We Use Our Heads Instead of the Formula?, Journal of Counselling Psychology 4, No. 4, 268–276 (1957).

[65] P.E. Meehl, Causes and Effects of My Disturbing Little Book, Journal of Personality Assessment 50, 370–375 (1986).

[66] T. Mehle and C. Gettys, Optimal Stopping Strategies for Information Purchase in Multiple-Stage Inference Tasks, Organizational Behavior and Human Performance 24, 333–353 (1979).

[67] J.T. Mentzer and J.E. Cox, Familiarity. Application, and Performance of Sales Forecasting Techniques, Journal of Forecasting 3, No. 1, 27–36 (1984).

[68] G.A. Miller, The Magical Number Seven. Plus or Minus Two: Some Limits on Our Capacity for Processing, Psychological Review 3, No. 2, 81–97 (1956).

[69] T.J. Mock, Concepts of Information Value and Accounting, Accounting Review 46, 765–778 (Oct. 1971).

[70] M.M. Moriarty, Design Features of Forecasting Systems Involving Management Judgments, Journal of Marketing Research, XXII, 353–364 (Nov. 1985).

[71] J.W. Payne, Task Complexity and Contingent Processing in Decision Making: An Information Search and Protocol Analysis, Organizational Behavior and Human Performance 16, No. 2, 366–387 (1976).

[72] J.W. Payne, Contingent Decision Behaviour, Psychological Bulletin 92, No. 2, 382–402 (1982).

[73] D.K. Peterson and G.F. Pitz, Explicit Cue Weighting in a Prediction Task, Organizational Behavior and Human Decision Processes 36, 289–304 (1985).

[74] D.K. Peterson and G.F. Pitz, Effect of Input from a Mechanical Model on Clinical Judgment, Journal of Applied Psychology 71, No. 1, 163–167 (1986).

[75] G.F. Pitz, Information Seeking When Available Information is Limited, Journal of Experimental Psychology 76, No. 1, 25–34 (1968).

[76] G.F. Pitz, Use of Response Times to Evaluate Strategies of Information Seeking, Journal of Experimental Psychology 80, No. 3, 553–557 (1969).

[77] G.F. Pitz, Bayes' Theorem: Can a Theory of Judgment and Inference Do without It?, in: F. Restle, R.M. Shiffrin, N.J. Castellan, H.R. Lindman and D.B. Pisoni, Eds., Cognitive Theory (Vol. 1), 131–148 (Lawrence Erlbaum Associates Publishers, Hilsdale, John Wiley and Sons, 1975).

[78] G.F. Pitz and H.R. Barrett, Information Purchase in a Decision Task Following the Presentation of Free Information, Journal of Experimental Psychology 82, No. 3, 410–414 (1969).

[79] W.E. Pracht and J.F. Courtney, The Effects of an Interactive Graphics-Based DSS to Support Problem Structuring, Decision Sciences 19, 598–621 (1988).

[80] D.G. Pruitt, Informational Requirements in Making Decisions, American Journal of Psychology 74, 433–439 (1961).

[81] B.A. Reilly and M.E. Doherty, The Assessment of Self-Insight in Judgment Policies, Organizational Behavior and Human Decision Processes 53, 285–309 (1992).

[82] W.E. Remus and J.E. Kottemann, Toward Intelligent Decision Support Systems: An Artificially Intelligent Statistician, MIS Quarterly, 403–418 (Dec. 1986).

[83] A.J. Repo, The Value of Information: Approaches in Economics, Accounting, and Management Science, Journal of the American Society for Information Science, 40, No. 2, 68–85 (1989).

[84] J.E. Russo and B.A. Dosher, Strategies for Multiattribute Binary Choice, Journal of Experimental Psychology: Learning, Memory, and Cognition 9, No. 4, 676–696 (1983).

[85] A.P. Sage, Behavioral and Organisational Considerations in the Design of Information Systems and Process for Planning and Decision Support, IEEE Transactions on Systems, Man, and Cybernetics, SME-II, No. 9, 640–678 (1981).

[86] N.R. Sanders, Accuracy of Judgmental Forecasts: A Comparison, OMEGA The International Journal of Management Science 20, No. 3, 353–364 (1992).

[87] N.R. Sanders and L.P. Ritzman, The Need for Contextual and Technical Knowledge in Judgemental Forecasting, Journal of Behavioural Decision Making 5, 39–52 (1992).

[88] N. Schmitt, Comparison of Subjective and Objective Weighting Strategies in Changing Task Situations, Organizational Behavior and Human Performance 21, 171–188 (1978).

[89] R. Sharda, S.H. Barr and J.C. McDonnel, Decision Support Systems Effectiveness: A Review and an Empirical Test, Management Science 34, No. 2. 139–159 (1988).

[90] H.A. Simon, A Behavioral Model of Rational Choice, Quarterly Journal of Economics 69, 99–118 (1955).

[91] L. Sjoberg, Aided and Unaided Decision Making: Improving Intuitive Judgement, Journal of Forecasting 1, 349–363 (1982).

[92] K.J. Snapper and D.G. Fryback, Inferences Based on Uncertain Reports, Journal of Experimental Psychology 87, No. 3, 401–404 (1971).

[93] K.J. Snapper and C.R. Peterson, Information Seeking and Data Diagnosticity, Journal of Experimental Psychology 87, No. 3, 429–433 (1971).

[94] R.H. Sprague, Jr., A Framework for the Development of Decision Support Systems, MIS Quarterly 4, No. 4, 10–26 (1980).

[95] J. Stevens, Applied Multivariate Statistics for the Social Sciences (Lawrence Erlbaum Associates Publishers, New Jersey, 1986).

[96] W. Thorngate, Efficient Decision Heuristics, Behavioral Science 25, 219–225 (1980).

[97] P. Todd and I. Benbasat, The Use of Information in Decision Making: An Experimental Investigation of the Impact of Computer-Based Decision Aids, MIS Quarterly 16, No. 3, 373–393 (1992).

[98] K.T. Trotman and J. Sng, The Effect of Hypothesis Framing. Prior Expectations and Cue Diagnosticity on Auditors' Information Choice, Accounting, Organizations and Society 14, No. 5/6, 565–576 (1989).

[99] A. Tversky and D. Kahneman, Judgment under Uncertainty: Heuristics and Biases, Science 185, 1124–1131 (1974).

[100] T.S. Wallsten, Failure of Predictions from Subjectively Expected Utility Theory in a Bayesian Decision Task, Organizational Behavior and Human Performance 3, 239–252 (1968).

[101] D. Wendt, Value of Information for Decisions, Journal of Mathematical Psychology 6, 430–443 (1969).

[102] Z.I. Youssef, The Effects of Cascaded Inference on the Subjective Value of Information, Organizational Behavior and Human Performance 10, 359–363 (1973).

Joa Sang Lim is currently employed with Samsung Data Systems, Seoul, South Korea. His research interests focus on the interaction of human judgment and computer-based information systems. He is especially interested in the way people make judgments and the way in which they can be assisted by technology.

Marcus O'Connor is an Associate Professor in the School of Information Systems at the University of New South Wales, Sydney, Australia. His research interests centre around the way in which people use information in conjunction with computer-based information systems, especially in the forecasting task. He is also interested in the allocation of tasks to people and machine in the design of information systems.

---
otero_id: 15882
otero_key: "C4DXJHN4"
title: "A note on an experimental study of DSS and forecasting exponential growth"
authors: "David Arnott; Peter O'Donnell"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.11.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# A note on an experimental study of DSS and forecasting exponential growth

David Arnott <sup>⁎</sup>, Peter O'Donnell

Centre for Decision Support and Enterprise Systems Research, Monash University, Melbourne, Australia

Received 28 October 2006; received in revised form 5 November 2007; accepted 27 November 2007 Available online 8 December 2007

## Abstract

Many managers need to make forecasts of variables that are growing rapidly. Business variables that increase or decrease exponentially are common in turbulent and complex markets, and misjudging the exponential nature of these variables in an important decision could have major adverse consequences for an organization. This paper reports on an experiment that investigated the use of DSS in an exponential decision task. It found that the use of a simple DSS significantly improved decision performance. This study forms the start of a series of investigations into DSS and complexity. © 2007 Elsevier B.V. All rights reserved.

Keywords: Decision support systems; Forecasting; Exponential growth; Cognitive bias

## 1. Introduction

Many of the problems that decision makers encounter involve making decisions under uncertainty in which judgment plays a large role. These judgments are often based on a limited number of simplifying decision strategies or heuristics. In certain circumstances, these heuristics can lead to severe misjudgments. Judgment errors that result from the inappropriate application of these heuristics are called cognitive biases [5,9]. One cognitive bias is an effect that causes human decision makers to under-estimate forecasts of exponential data series [4,18]. This effect can be termed the exponential forecast bias. It is an important bias for managers, as they may need to make forecasts of variables that are growing or decaying at an exponential rate. Business variables that increase or decrease exponentially are common in turbulent and complex markets and misjudging the exponential nature of these variables in an important decision could have major adverse consequences for an organization. This paper reports on an experiment that investigated the use of DSS in an exponential decision task.

## 2. Forecasting exponential growth

In several experimental studies, humans have been found to be unable to interpret or extrapolate exponential functions in an accurate manner [12,18–21]. In these experiments, participants were provided with a data series that was derived from an exponential function and asked to estimate the next element, or elements, in the series. An important aspect of the experimental design is that participants are normally aware that the data series is exponential in nature. The participants' estimates were consistently below the normative values generated from the exponential function. These experiments have found that participants using graphically displayed data perform no better than participants who used tabular reports, and that the estimates produced by managers were no better than those produced by students. The exponential forecast bias has also been found to be resistant to changes in the format of the presentation of the data series [21], to the direction of the exponential growth [19] and to the amount of information about the data series made available to subjects [20,21]. In general, the more information that is provided to participants, for example the number of data points, the worse the estimation error becomes [20]. None of these experiments used IT-based displays or DSS technology.

The effect of the exponential forecast bias may be reduced by transforming the data series and presenting it on a logarithmic scale. After a log transform the exponential nature of the data is reduced to a linear form. Remus [15] argues that decision makers consider the differences, rather than the ratio, between data points when extrapolating. This means that decision makers, while under-estimating exponential growth, should be able to correctly extrapolate a linear data series. A DSS may assist decision makers by displaying the data series in both logarithmic and normal scales. This way they can see the growth nature of the series but can be guided in their forecast task by a linear graph presentation.

## 3. Hypotheses

Most people make decisions involving the forecasting of exponential data by using information that is presented to them in a paper-based report. This static presentation can be in table or graph from, or both. Alternatively, they could receive the information via a DSS and use its interactive nature to explore different options before making a decision. The first hypothesis involves a comparison of the efficacy of these two modes of support.

H1. Participants using a DSS will have better forecast accuracy than participants using a paper-based report.

As mentioned above, people may be able to better forecast growth if it is presented in a linear form; that is, when an exponential growth series is presented on a logarithmic scale. This implies that a ‘combined’ representation using normal and logarithmic scales may be superior to the presentation of data on a normal scale alone.

H2. Participants presented with a combined representation will have better forecast accuracy than those presented with a normal representation.

A more detailed consideration of the different representations (normal and combined) and support modes (report and DSS) leads to hypotheses three and four.

H3. Participants using a DSS with a combined representation will have better forecast accuracy than those using a DSS with a normal representation.

![](/api/attachments/C4DXJHN4/fulltext/images/4f457f09c0fdc074cfcc0b365567426667c8878911d0a9e0e3fe99cdc7cd824e.jpg)  
Fig. 1. Cumulative iPod sales revenue.

![](/api/attachments/C4DXJHN4/fulltext/images/906de5b3b08b37b34afc1c88179d8c59b4029b472b69ed8f3fcdec04eadffc48.jpg)  
Fig. 2. The task description.

H4. Participants using a paper-based report with a combined representation will have better forecast accuracy than those using a paper-based report with a normal representation.

## 4. Experimental design and procedures

The experiment manipulated two independent variables, each at two levels. The primary factor was the mode of support (report or DSS) and the second factor was the representation (normal or combined). The dependent variable was forecast accuracy. This was calculated as the absolute difference between the forecast given by the participant and the actual outcome. Similar measures of forecast accuracy have been used in other studies [7]. The general nature of the experimental task was based upon previous studies of forecasting exponential growth [18–21]. An important aspect of these previous experiments is the choice of task. These studies used data series that the participants should have known were growing or decaying exponentially. In some experiments the subjects were told that the series they were forecasting showed “marked growth tendencies”. The experimental series included population growth data, upper air pollution, and the pond-andduckweed problem where the weed doubles in size every 5 years.

![](/api/attachments/C4DXJHN4/fulltext/images/2019929ff8b3e0c1c4b5a85025a6bb31021a1ff1d4222446581c3981dc58d89f.jpg)  
Fig. 3. Support screen of DSS D1 — normal representation.

Participants in this experiment were asked to make an estimate of the total worldwide unit sales of the popular consumer product, Apple's iPod. The iPod was chosen because it is regarded as one of the world's most desirable consumer items; it is Amazon's best selling electronic product [3]. In Quarter 3, 2004 the iPod had 87.3% of the MP3 hard-disc music player market [6]. Another reason for the choice of the iPod as the object of the forecasting task was that its rapid growth in the marketplace was likely to be familiar to all participants. The cumulative sales data for the Apple iPod was obtained from Apple's publicly available quarterly SEC reports. The full data series is shown in Fig. 1.

Consistent with the design of previous studies, participants were only provided with the data for the period from Quarter 4, 2001 up to Quarter 3, 2004. They were asked to provide an estimate for unit sales at the end of Quarter 1, 2005. The experiment was conducted in mid-2005. All participants were provided with the description of the forecast task shown in Fig. 2.

A single decision setting was chosen for this initial experiment. Further research will analyze a progression of decisions with feedback. Two simple DSS (D1 and D2) were constructed to assist participants in making forecasts of data that exhibited exponential growth. Each system comprised three screens: the first explained the nature of the task (Fig. 2), the second provided support for the decision, and the third was used to collect demographic data and an assessment of each participant's confidence in their forecasts. The support screens of D1 and D2 are shown in Figs. 3 and 4. Paper-based report versions of D1 and D2 were also developed. Both D1 and D2 were designed to provide very simple ITbased support.

D1 presented cumulative iPod sales data from Quarter 4, 2001 to Quarter 3, 2004 in a normal scale in both tabular and graphical formats (Fig. 3). Participants could enter their cumulative sales estimate for Quarter 1, 2005 in a text box or they could click on a point in the graph space and the cumulative sales value of that point appeared in the text box. Participants could experiment with different points without restriction. After they were satisfied with their decision they clicked “OK” to confirm their prediction. D2 presented the same data, but in both normal and logarithmic scales (Fig. 4). The user operations were similar to D1 with the addition that when a participant clicked on a point in the normal scale graph, the corresponding point in the logarithmic scale graph was indicated, and vice versa. Further, the numerical value of the cumulative sales forecast was displayed in the table as well as in the text answer box. An additional feature of D2 was a drop-down box that provided a general explanation of logarithmic transformation. This style of information provision is common in DSS and other IT-based systems but is not available in paper-based reports. This feature was a main informational difference between D2 and the equivalent paperbased report. Using D2, participants were free to trial as many values as they liked. As with D1, they could use the graph to assist their judgement or could simply type in their prediction.

![](/api/attachments/C4DXJHN4/fulltext/images/0fabf4da3d5065218aae8a450e6301d2711c4ab48c26d3e62280e332f685bd25.jpg)  
Fig. 4. Support screen of DSS D2 — combined representation.

Table 2 ANOVA table  
Sample sizes and mean forecast error for each combination of support and representation

<table><tr><td></td><td>Count</td><td>Forecast error Mean</td><td>Forecast error S.D.</td><td>Forecast error S.E.</td></tr><tr><td>DSS, combined</td><td>46</td><td>6,920.11</td><td>2,883.87</td><td>425.20</td></tr><tr><td>DSS, normal</td><td>44</td><td>6,747.14</td><td>2,358.51</td><td>355.60</td></tr><tr><td>Paper report, combined</td><td>46</td><td>7,547.83</td><td>1,959.07</td><td>288.85</td></tr><tr><td>Paper report, normal</td><td>42</td><td>7,725.98</td><td>2,390.31</td><td>368.83</td></tr></table>

The 178 participants were graduate information systems students who volunteered for the experiment. They were randomly allocated to four groups. In total, 88 participants used a paper-based report and 90 used a DSS. The groups were similar in terms of age, mathematics education, and work experience in an investment bank. Participants in the DSS groups performed the task in computer laboratories. The report groups performed the task in a lecture or tutorial room. No time restrictions were imposed. In all venues a researcher or research assistant was present to answer procedural questions. Data was collected from the groups as close to the same time as possible to minimize any possible interaction between the groups.

<table><tr><td>Source</td><td>Sum of squares</td><td>df</td><td>F</td></tr><tr><td>Support</td><td>28673270.56</td><td>1</td><td>4.889*</td></tr><tr><td>Representation</td><td>297.831</td><td>1</td><td>0.000</td></tr><tr><td>Support* Representation</td><td>1369626.019</td><td>1</td><td>0.234</td></tr><tr><td>Residual</td><td>1020408813</td><td>174</td><td></td></tr></table>

⁎ pb0.05.

There are two fundamental approaches to experiments in decision making: experimental economics, where the focus is on market decision-making, and behavioral decision theory, where the focus is on individual decisionmaking [2,13,17]. Each has a fundamentally different approach to incentives. Experimental economics uses Smith's induced value approach where all participants are incentivized by monetary rewards. This approach is also based on the premise that decision-making experiments should be designed as repeated trials [16]. On the other hand, behavioral decision theory research is dominated by one-shot experiments [9,10]. Unlike experimental economics, these experiments tend to have a single prize for the best performance by a participant. As this experiment involves a one-shot decision in the behavioral decision theory tradition, to provide incentive for performance in the experimental task, a prize of an Apple iPod was awarded to the participant with the best forecast accuracy. Using iPods as a prize is common in contemporary behavioral research [1,8].

## 5. Analysis and results

The mean of forecast error (with the associated standard deviation and standard error) for each combination of the variables support (DSS or report) and representation (normal or combined) is shown in Table 1. The analysis and hypothesis testing was performed using ANOVA. However, as the sizes of the samples for each combination of support and representation was unequal, an adaptation of the standard ANOVA technique was required. This involved the calculation and use of the harmonic mean of the sample sizes in the ANOVA calculations [[11] pp. 289–291]. A summary of the ANOVA calculations is shown in Table 2. Table 3 summarizes the results of the hypothesis testing. Fig. 5 shows an interaction line plot of support and representation. The plot shows an ordinal interaction between these variables [[14] chap. 7]. The hypothesis testing and interaction plot shows that it is the use of a DSS that results in better decision-making performance regardless of the representation that is used. In this initial experiment transforming the exponentially increasing sales data into a linear presentation made no significant difference in decision-making quality.

Results of hypothesis testing

<table><tr><td>Hypothesis</td><td>Test result</td></tr><tr><td>1. Participants using a DSS will have better forecast accuracy than participants using a paper-based report.</td><td>Supported</td></tr><tr><td>2. Participants presented with a combined representation will have better forecast accuracy than those presented with a normal representation.</td><td>Rejected</td></tr><tr><td>3. Participants using a DSS with a combined representation will have better forecast accuracy than those using a DSS with a normal representation.</td><td>Rejected</td></tr><tr><td>4. Participants using a paper-based report with a combined representation will have better forecast accuracy than those using a paper-based report with a normal representation.</td><td>Rejected</td></tr></table>

![](/api/attachments/C4DXJHN4/fulltext/images/d32a8abcd77920b07aa57f1d2b83177ce6058b0d5949c8b9ffacd68f0ec0251b.jpg)  
Fig. 5. Interaction line plot of support and representation.

## 6. Future research

This experiment is an early contribution to a research program that is investigating the issue of application complexity and decision support effectiveness. Application complexity is an important contemporary issue because of the scale and complexity of current business intelligence and data warehousing applications. Matching the complexity of an application to the nature of a decision task is an important professional decision. Ideally, a decision maker should use the simplest and cheapest DSS application that will effectively support their decision task.

The next stages of the research program will include:

• Using managers rather than graduate students as participants;

• Studying more complex decision tasks that include learning between trials;

• Using alternative approaches to participation incentive; and

• A field investigation of the use of relatively simple spreadsheet models by senior executives.

## Acknowledgements

We would like to thank Gemma Dodson for research assistance, especially with ethics approval and data gathering.

## References

[1] S. Alexander, T. Golja, Using students' experiences to derive quality in an e-Learning system: an institution's perspective, Educational Technology & Society 10 (2) (2007) 17–33.

[2] M. Altman, The Nobel Prize in behavioral and experimental economics: a contextual and critical appraisal of the contributions of Daniel Kahneman and Vernon Smith, Journal of Politica Economy 16 (1) (2004) 3–41.

[3] Amazon, Top sellers in electronics, Amazon.com, http://www. amazon.com/exec/obidos/tg/browse/-/172282/ref=sd\_allcat\_el/ 002-3195090-5722410 (2005, current 13 September 2005).

[4] M. Bar-Hillel, On the subjective probability of compound events, Organizational Behavior and Human Performance 9 (1973) 396–406.

[5] M.H. Bazerman, Judgement in Managerial Decision Making, 5th ed. Wiley, New York, 2002.

[6] I. Betteridge, iPod market falls — to 87%, ExtremeiPod.com, http://www.extremeipod.com/article2/0,1895,1711754,00.asp (2004, current 6 September 2005).

[7] J.M. Carey, E.M. White, The effects of graphical versus numerical response on the accuracy of graph-based forecasts, Journal of Management 17 (1) (1991) 77–96.

[8] J. Cave, K. Woolf, J. Dacre, H.W.W. Potts, A. Jones, Medical student teaching in the UK: How well are newly qualified doctors prepared for their role caring for patients with cancer in hospital? British Journal of Cancer 97 (2007) 472–478.

[9] R. Hastie, R.M. Dawes, Rational Choice in an Uncertain World, Sage, Thousand Oaks, CA, 2001.

[10] D. Kahneman, A. Tversky, Prospect theory: An analysis of decision under risk, Econometrica 47 (1979) 263–291.

[11] G. Keppel, Design and Analysis: A Researcher's Handbook, 3rd ed. Prentice-Hall, Englewood Cliffs, NJ, 1991.

[12] G. Keren, Cultural differences in the misperception of exponential growth, Perception & Psychophysics 34 (1983) 289–293.

[13] G. Loewenstein, Experimental economics from the vantage-poin of behavioural economics, Economic Journal 109 (1999) F25–F34.

[14] S.E. Maxwell, H.D. Delane, Designing Experiments and Analyzing Data: A Model Comparison Perspective, Lawrence Erlbaum Associates, Mahwahs, NJ, 2003.

[15] W.E. Remus, An empirical investigation of the impact of graphical and tabular data presentations on decision making, Management Science 30 (5) (1984) 533–542.

[16] V.L. Smith, Experimental economics: induced value theory. American Economic Review 66 (2); 274–279.

[17] V.L. Smith, Behavioral economics research and the foundations of economics, Journal of Socio-Economics 34 (2005) 135–150.

[18] W.A. Wagenaar, S.D. Sagaria, Misperception of exponential growth, Perception & Psychophysics 18 (6) (1975) 416–422.

[19] W.A. Wagenaar, H. Timmers, Inverse statistics and misperception of exponential growth, Perception & Psychophysics 21 (6) (1977) 558–562.

[20] W.A. Wagenaar, H. Timmers, Extrapolation of exponential time series is not enhanced by having more data points, Perception & Psychophysics 24 (2) (1978) 182–184.

[21] W.A. Wagenaar, H. Timmers, The pond-and-duckweed problem: Three experiments on the misperception of exponential growth, Acta Psychologica 43 (3) (1979) 239–251.

David Arnott is a Professor of Information Systems at Monash University, Melbourne, Australia and Director of Monash’s Centre for Decision Support and Enterprise Systems Research. His current research areas include the development of IT-based systems for managers, business intelligence, data warehousing and IT governance. He is the author of more than 60 scientific papers in the decision support area, including papers in journals such as the European Journal of Information Systems, Information Systems Journal, Deci sion Support Systems, and the Journal of Information Technology.

Peter O’Donnell is a Lecturer in the Centre for Decision Support and Enterprise Systems Research at Monash University in Melbourne, Australia. His current research interests include conceptual modeling for decision support systems and the usability of business intelligence interfaces. He maintains close links with the business intelligence industry in Australia and is regularly invited to speak at trade seminars and user group meetings.

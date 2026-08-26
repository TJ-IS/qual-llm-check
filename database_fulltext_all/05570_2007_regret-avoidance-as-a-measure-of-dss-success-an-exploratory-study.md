---
otero_id: 5570
otero_key: "ZVME5G4F"
title: "Regret avoidance as a measure of DSS success: An exploratory study"
authors: "Shin-Yuan Hung; Yi-Cheng Ku; Ting-Peng Liang; Chang-Jen Lee"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.05.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Regret avoidance as a measure of DSS success: An exploratory study

Shin-Yuan Hung <sup>a,⁎</sup>, Yi-Cheng Ku <sup>b</sup>, Ting-Peng Liang <sup>c</sup>, Chang-Jen Lee

<sup>a</sup> Department of Information Management, National Chung Cheng University, Taiwan

<sup>b</sup> Department of Computer Science and Information Management, Providence University, Taiwan

<sup>c</sup> Department of Information Management, National Sun Yat-sen University, Taiwan

Received 23 March 2005; received in revised form 15 February 2006; accepted 18 May 2006 Available online 28 July 2006

## Abstract

Assessing the value of decision support systems (DSS) is an important line of research. Traditionally, researchers adopt user satisfaction and decision performance to measure DSS success. In some cases, however, the use of DSS is not benefit driven. Instead, DSS adoption may be motivated by avoiding decision errors or reducing decision cost, indicating that regret avoidance may be a useful measure of DSS success. Regret is a post-decision feeling regarding not having chosen a better alternative. Recent behavioral research has indicated that, in addition to pursuing higher performance and user satisfaction, reducing decision regret is another important consideration for many decision-makers. This exploratory study extends prior research on DSS evaluation by proposing regret avoidance as an additional measure of DSS success. Experimental results regarding the use of DSS for stock investment demonstrate DSS use significantly reduces regret in situations involving low user satisfaction. Consequently, besides decision performance and user satisfaction, regret reduction is also important in measuring the effectiveness of DSS. © 2006 Elsevier B.V. All rights reserved.

Keywords: Regret theory; Decision support systems; Information systems evaluation; Information systems success

## 1. Introduction

As information systems, decision support systems (DSS) facilitate decision-making by offering information access, model analysis, and supporting tools [2,40]. DSS enable us to believe that the system positively influences decision quality. Measuring DSS success is difficult. Decision-makers use technological tools to fulfill various functions. Traditional definitions of DSS suggest that DSS are designed to help decision-makers address unstructured or semistructured decisions [40]. Increasing decision effectiveness or efficiency are the typically expected benefits of DSS [67]. Therefore, previous studies on DSS success have focused mainly on measures of decision performance or user satisfaction [10,23,31,33,34,42].

However, literature reviews indicate that DSS have had a mixed influence on decision performance. Some studies reported that DSS positively affected decision performance or user satisfaction, while others found no impact or even a negative impact on decision performance (e.g. [9,24,25]). These conflicting results imply the existence of additional considerations when decision-makers decide to use DSS. Recent developments in regret theory provide an alternative view for measuring DSS success.

Individuals frequently feel disappointed following a decision is made, when they overlooked or neglected a better choice. Regret analysis investigates the role of psychological feelings following the failure to choose the best alternative and how the feelings may affect subsequent decision behavior [7,43,68]. Landman [44] defines regret as:

Regret is a more or less painful cognitive and emotional state of feeling sorry for misfortunes, limitations, losses, transgressions, shortcomings, or mistakes. It is an experience of felt-reason or reasoned-emotion. The regretted matters may be sins of commission as well as sins of omission; they may range from the voluntary to the uncontrollable and accidental; they may be actually executed deeds or entirely mental ones committed by oneself or by another person or group; they may be moral or legal transgressions or morally and legally neutral (p. 36).

The theory investigating the phenomena is known as regret theory [48]. Inman et al. [36] proposed a generalized utility model to illustrate the effect of post-choice disappointment and regret. The proposed model considers both chosen and forgone alternatives as the basis for valuation. The results demonstrate the existence of post-choice regrets, the negative effects of which may exceed the positive impact of rejoicing. Since regret is annoying, most people are willing to take positive action to avoid it [7,8].

The influence of regret on human decision behavior has been reported in numerous areas, including negotiation [45] and consumer behavior research [63]. Seeking the best alternative under uncertainty is generally associated with a high risk. Decision-makers face a trade-off between decision benefits and risk. However, decision-makers tend to make choices that minimize regret rather than risk if the emotional consequences of decisions are anticipated and considered [45,73]. In other words, anticipated regret avoidance may enhance the motivations of manager to use DSS.

Regret avoidance behavior can affect human decisions in that individuals may reject decisions if they feel that those decisions are likely to cause regret [27] and the anticipation of regret may affect the decision process [7,48,63]. Business practices commonly take advantage of regret avoidance in many countries. An example is companies allowing merchandise to be returned with no charge within a certain time period. This grace period increases customer likelihood of purchase by reducing the potential for regret. Given the important influence of regret in decision-making, it is interesting to study whether regret avoidance can be used as an additiona dimension for assessing the value of DSS and how this compares with the traditional measure of user satisfaction.

This study investigates how DSS use affects decision regret, which includes DSS use as an independent variable, user responsibility as a moderating variable, and three dependent variables, namely decision performance, user satisfaction, and user regret. The experimental results show that DSS use could enhance decision performance and reduce user regret, but good decision performance does not always guarantee high user satisfaction. Therefore, decision regret should be included in the assessment of the value of DSS.

The rest of this paper is organized as follows. Section 2 briefly reviews literature on the evaluation of DSS. Section 3 then describes the research framework and hypotheses of this study. Next, the experimental design is described in Section 4. Section 5 summarizes data analyses and research findings. Conclusions are finally drawn in Section 6, along with managerial implications and areas for future research.

## 2. Measuring DSS success

2.1. Existing measures on performance and user satisfaction

Measuring systems success is important in information systems research. Previous literature used two categories of variables to measure DSS success: process-oriented, including frequency or length of system usage, and outcome-oriented, including decision performance and user satisfaction [28,35,38,60]. Since the pioneering work on “value analysis” by Keen and Scott-Morton [40], numerous studies have investigated the influence of DSS [1,59] and they adopted various research methods that include case studies, field studies, and laboratory experiments.

Table 1 lists a survey of 18 studies that used various DSS success measures to assess decision performance and user satisfaction. These success measures generally focus on system efficiency or effectiveness [40,59].

Efficiency is process-oriented and is generally measured using decision speed or the number of alternatives being considered. For example, Alter [3] cites increasing decision-making efficiency was one potential benefit of DSS. Moreover, effectiveness was measured by decision outcome, such as the quality or accuracy of decision and user satisfaction. For instance, numerous studies have adopted user satisfaction and/or decision-making satisfaction, decision quality, and business profitability to evaluate DSS outcomes [14, 41,49,58,59].

Table 1 Previous DSS success measures

<table><tr><td>Study</td><td>Independent variable</td><td>Dependent variable</td></tr><tr><td>Sharda, Barr, and McDonnell [59]</td><td>DSS/non-DSS</td><td>Profit performanceVariance in profit performanceTimeNumber of alternativesConfidence</td></tr><tr><td>Le Blanc and Kozar [46]</td><td>Length of DSS useOther variablesLagged accidents rateTraffic levelDSS utilizationRiver stageWeather</td><td>DSS usage</td></tr><tr><td>Alavi and Joachimsthaler [1]</td><td>Cognitive stylePersonality attributesDemographic variablesUser-situation variables</td><td>PerformanceCost/profitDecision-making timeAttitudes/perceptionsUser satisfaction with DSSConfidence in decisionsPerceived usefulness of system</td></tr><tr><td>Todd and Benbasat [67]</td><td>DSSProblem size</td><td>Unique units of information referencedTotal units of information referencedNumber of alternatives analyzed in detail</td></tr><tr><td>Davis and Kottemann [19]</td><td>What-if analysisProblem complexityPresence/absence of DSS</td><td>PerformanceDecision timeAccuracy</td></tr><tr><td>Crossland, Wynne, and Perkins [18]</td><td>DSS capabilityImplementation strategy</td><td>PerformanceUser behaviourImplementation strategy</td></tr><tr><td>Eierman, Niederman, and Adams [21] $^a$ </td><td>User behaviourEnvironmentUserTaskDSS configuration</td><td>User</td></tr><tr><td>Swink [64]</td><td>User characteristicsUser experiencesCognitive factorsEffortDSS characteristicTask characteristics</td><td>Decision performanceDecision qualityPerception accuracySolution search efficiencyDecision time</td></tr><tr><td>Montazemi, Wang, Nainar, and Bart [51]</td><td>Suggestive guidance vs. no guidanceInformative guidance vs. no guidanceSuggestive guidance vs.informative guidance</td><td>Task performance</td></tr><tr><td>Barr and Sharda [6]</td><td>DSS</td><td>Decision performance</td></tr><tr><td>González and Kasper [29]</td><td>Animation imagesAnimation transitionsAnimation navigation</td><td>Decision quality</td></tr><tr><td>Swink and Robinson [65]</td><td>DSS attributesProblem sizeNetwork typesDemand dispersion patterns</td><td>Decision performances</td></tr><tr><td>van Bruggen, Smidts, and Wierenga [70]</td><td>MDSS support</td><td>PerformanceDecision qualityLess susceptible to using the anchoring and adjustment heuristic</td></tr><tr><td>Gregor and Benbasat [30]</td><td>KBS explanations</td><td>AccuracySpeed</td></tr><tr><td>Swink and Speier [66]</td><td>Task characteristicsProblem sizeData aggregationData dispersionUser characteristicsSpatial Orientation</td><td>Decision performanceDecision qualityDecision time</td></tr><tr><td>Mennecke, Crossland, and Killingsworth [50]</td><td>Problem complexitySDSS supportSubject characteristics</td><td>Decision efficiency(solution time)Decision accuracy</td></tr><tr><td>Parikh, Fazlollahi, and Verma [57]</td><td>Decisional guidance vs. no guidanceInformative vs. suggestive decisional guidancePredefined vs. dynamic decisional guidance</td><td>Decision qualityUser satisfactionUser learningDecision-making efficiency</td></tr><tr><td>Bharati and Chaudhury [10]</td><td>System qualityInformation qualityInformation presentation</td><td>Decision-making satisfaction</td></tr></table>

<sup>a</sup> This study developed a theoretical framework for DSS research from a review of literature. Eight broad DSS constructs (independent variables, mediator variables, and dependent variables) and 17 relationships among these constructs were examined.

Decision performance can be assessed subjectively or objectively [47]. Subjective measures assess user perceptions of system value (e.g. perceived economic benefits), whereas objective measures assess decision performance based on objectively measurable criteria, such as time required to reach a decision, resulting profit increases or cost savings.

User satisfaction indicates the subjective feelings of users regarding system performance. For instance, according to the expectation theory [11], user satisfaction is affected by the prior expectations of users regarding the system and its effectiveness. Based on disconfirmation theory [54,55], users tend to disproportionately rate how actual and expected performance differ. Therefore, actual performance can influence user satisfaction [4,5].

For instance, Alavi and Joachimsthaler [1] represented the success of DSS implementation in terms of system use, decision-making performance, decisionmaking time, user satisfaction with the system, user confidence in the decisions, and user attitudes toward DSS. Eierman et al. [21] developed a DSS research model that includes eight main constructs (environment, task, implementation strategy, DSS capability, DSS configuration, user, user behavior, and performance) and 17 relationships.

Previous literature provides a valuable foundation for measuring DSS success. However, the literature contains some inconsistent results. Some studies have reported that using DSS yields a positive value, while others identified contradictory relationships between DSS usage and performance [9,22,38,59]. This finding implies that other unexplored factors may influence decisions regarding DSS use. This section summarizes existing measures and introduces regret theory to develop an extended model for measuring DSS success.

## 2.2. Regret as a decision outcome

The recent literature on decision-making contends that a thorough post-choice evaluation should include not only positive expectations such as performance and satisfaction but also regret and disappointment, because recent behavioral research has found that, besides maximizing positive decision outcomes, decisionmakers frequently consider potential regret. For example, Tsiros and Mittal [69] developed a model of regret and demonstrated through empirical tests that regret directly influences product repurchasing intention. Regret is experienced even in the absence of information regarding a better-forgone outcome, and consumers may defer repurchase decisions after receiving post-purchase information that may lead to future regret [17]. Studies found that individuals are willing to take risks or to obtain more information in a game or investment decision to gain a greater monetary return [73]. More information they acquire implies a greater likelihood that they will feel that regret can be avoided [72].

Regret refers to a rational and negative cognitive response resulting from comparing an actual result with a better one that was passed up by the decision-maker. Regret is a psychological state different from satisfaction. Satisfaction involves a comparison between expected and actual performance, whereas regret occurs when a foregone alternative would have yielded a better outcome than the actual one [7,48,69]. Furthermore, empirical evidence distinguishes between regret and satisfaction [68].

<table><tr><td>The worst Performance</td><td>Prior performance Expectation</td><td>The best Performance</td></tr><tr><td>Result of Alternative-1</td><td>Result of Alternative-2</td><td>Result of Alternative-3</td></tr></table>

Fig. 1. Regret as a measure of DSS effectiveness.

Regret and dissatisfaction are two different psychological concepts; even though both exhibit certain of displeasure [68]. The measurements used for regret and dissatisfaction also differ, as illustrated by the simple example in Fig. 1. Given the outcomes of the three alternatives, the user would feel dissatisfied and regretful if alternative 1 was chosen, satisfied but regretful if alternative 2 was chosen, and satisfied and not regretful if alternative 3 was chosen. For instance, if an investor purchased a stock expecting a 10% return at the beginning of the year and actually achieved a return of 20% by the end of the year, that investor may feel satisfied, but could instead feel regretful following learning that another stock he had decided not to purchase achieved a return of 30% during the same period.

Given that regret measures a post-decision feeling that differs from satisfaction, it can be used to interpret differences in observations between user satisfaction and decision performance. That is, decision-makers that achieve acceptable performance from a decision may experience a mixture of satisfaction (compared with the prior expectation) and regret (compared with the better performance of the dropped alternatives). It is reasonable to use regret as an alternative measure of decision effectiveness based on the assumption that the use of DSS can reduce potential decision regret because of the ability to examine the potential outcomes of more alternatives.

## 3. Research model

## 3.1. Factors affecting decision regret

Several factors affect an individual's regret. The first factor is job responsibility, namely the sense of duty associated with doing a job. People may feel increased regret when they assume higher responsibility for the result [26]. People may feel increased regret regarding actions in which they are heavily involved [39]. However, some studies found that user responsibility is not necessary for decision regret. For example, Connolly et al. [16] contends that, despite a positive correlation exists between regret and responsibility, responsibility is not necessary for generating decision regret. Zeelenberg et al. [74] and Ordóñez and Connolly [56] report inconsistent argument.

Gender is another factor that has been reported to influence decision regret. Males have been reported to tend to feel more regret than females [43]. Individual personality is also found to significantly influence feeling of regret [13]. Among those factors mentioned in previous studies, responsibility has a more solid theoretical foundation. Users with higher responsibility may treat decisions more seriously and thus use DSS more carefully and are more concern with the results. Therefore, we assume that the effect of DSS use on performance, satisfaction, and regret is assumed here to be stronger when the user feels more responsible for the outcome [15].

## 3.2. Research framework and hypotheses

Based on the previously reviewed literature, we hypothesize that using DSS may increase decision performance and user satisfaction, as well as reduce decision regret. Additionally, the main effects of DSS are moderated by user job responsibility. Therefore, the present research framework, illustrated in Fig. 2, includes DSS use as an independent variable, user responsibility as a moderating variable, and decision performance, satisfaction, and regret as three dependent variables. Heavier DSS use implies that decision-makers commit more effort to the decision-making; this study assumes that DSS use may reduce the likelihood of a good alternative being missed. Accordingly, users are more likely to select the optimal alternative and less likely to feel regret. Two sets of hypotheses are formulated below.

## $\mathbf { H _ { 1 } }$ . DSS use and decision outcome

$\operatorname { H } _ { \mathrm { 1 a } } \colon$ DSS use increases decision performance.

$\operatorname { H } _ { 1 \mathbf { b } } \colon$ DSS use increases user satisfaction.

$\operatorname { H } _ { \mathrm { 1 c } } \colon$ DSS use reduces user regret.

![](/api/attachments/ZVME5G4F/fulltext/images/5df593fafe021984baa013a03b5a3f87cb3335476fba033e24954a52f06ffaa1.jpg)  
Fig. 2. Research model.

Table 2  
Functions of the experimental system

<table><tr><td>Menu</td><td>Function</td></tr><tr><td>Market summary</td><td>Detail information of stock market, including stock quotes, change, day&#x27;s range, volume, and so on.</td></tr><tr><td>Industry quotes</td><td>Detail information of the specific industry.</td></tr><tr><td>Company information</td><td>Information of six companies used for trading in the experiment, including basic information, historical prices, news, and streaming charts are available.</td></tr><tr><td>Technical analysis</td><td>Tools for technical analysis, such as the moving average, RSI, and KD indicators.</td></tr><tr><td>Recent news</td><td>Three categories of news: political, international, and financial.</td></tr><tr><td>Calculator</td><td>Tool for calculating investment returns and others.</td></tr></table>

## $\mathbf { H } _ { 2 } .$ . Moderating effect of user responsibility

$\mathrm { H } _ { 2 \mathrm { a } } \mathrm { : }$ User responsibility moderates the effect of DSS use on decision performance.

$\mathrm { H } _ { 2 \mathrm { b } } \colon$ User responsibility moderates the effect of DSS use on user satisfaction.

$\mathrm { H } _ { 2 \mathrm { c } } \mathrm { : }$ User responsibility moderates the effect of DSS use on user regret.

## 4. Research design

## 4.1. Experimental task and the experimental system

Since the proposed research model includes both a main and a moderating variable, the experiment uses a $2 \times 2$ factorial design (comprising using DSS or not; high or low responsibility). The experimental task was selecting a stock for investment. This decision was appropriate because financial investments are a popular form of decision involving high uncertainty. Numerous investors regularly use DSS to support these kinds of decisions.

A Web-based DSS for the experiment was designed using Microsoft ASP and Access database. The system includes functions required for user support (summarized in Table 2) and can support all phases of the Simon's decision process: intelligence, design, and choice [61,62]. These functions represent six basic DSS functions: selection, aggregation, estimation, simulation, equalization, and optimization [12]. For instance, the system can display daily transaction data and sort it according to industry type, price, and volume. Subjects can also use technical indicators and other analytical tools to forecast stock trends, including the MACD, MFI, ROC, RSI, slow-stock, and fast-stock indicators. Certain firm information, including news reports and selected industrial data, market- and industry-related information, can also be examined. Furthermore, the subject can use the system to estimate and simulate their investment performance in different scenarios. Fig. 3 shows a sample screen of the DSS.

Subjects in the experimental group were given DSS, while those in the control group were not provided the system but were provided the same data and information in paper form. Doing so ensured that differences in outcome were because of the use of DSS rather than the content they were permitted to access during decision-making.

Each subject was given US\$150,000 to build an investment portfolio. Subjects were then instructed to allocate the available funds among. The experimental market simulated the behavior of selected stocks listed on the Taiwan Stock Exchange.

![](/api/attachments/ZVME5G4F/fulltext/images/4737b4d76f13d2ea7b6b94955875773ec9bfffcfca8dc455209d78f4e017153f.jpg)  
Fig. 3. Sample screen of the DSS.

## 4.2. Subjects

Seventy-two volunteers were recruited to participate in the experiment. Each subject was randomly assigned to one of the four settings. Sixty-five of the participants (40 males and 25 females) completed the experiment. All subjects were business school students and had an average age of 23 years old. Most of the subjects (98.5%) had taken at least one course on finance and 33.8% had real-world experience of stock investment. Most subjects (87.7%) used computers on a daily basis. Each participant received a fixed reward of US\$3 for participation. An additional US\$10 incentive was awarded depending on their decision performance.

## 4.3. Variable manipulation and measurements

To manipulate the feelings of responsibility, mood induction procedures (MIP) were conducted by means a short essay. Mood induction procedures were designed to induce emotional changes in experimental subjects by manipulating variables inside the laboratory in a controlled manner [71]. This method has been adopted in previous studies to manipulate subject feelings of regret and responsibility in evaluating decision outcomes [16,74]. The subjects assigned to the lowresponsibility group were given the following short essay to read before the experiment task:

You made a trip immediately after you made an investment decision. You were so busy that you were unable to monitor the stock market. Following you came back from the trip, you learned that during your trip, a crisis between Taiwan and Mainland China had caused an unexpected market downturn. There is not much you could do now to avoid the looses incurred. To make things even worse, you now have to sell the stocks and realize the major loss, due to needing to use the money for other uses.

Subject feelings of responsibility were measured following the manipulation mentioned above. Moreover, decision performance was measured using profit earned from the investment portfolios, namely the difference between the final market value of the chosen stocks and the initial investment. Additionally, user satisfaction was measured using three questions regarding subject perceptions of the investment [20,49,58]. Finally, regret was measured using two questions proposed by Tsiros (see Appendix A) [68,69]. Tsiros [68] initially adopted three items: (1) I feel sorry for having chosen…; (2) I feel regretful for having chosen…; (3) I am glad I chose to go with…, to measure this construct. After assessing the reliability of each item and construct validity, item 3 was dropped because of its low correlation with the overall construct. The other two items were retested by Tsiros and Mittal [69]. Both studies demonstrate that these two items have high reliability and high validity. All questions were evaluated using the sevenpoint Likert's scale.

## 4.4. Experimental procedures

The experiment included a pretest and pilot test, as well as the actual experiment. The pretest ensured that all questions in the questionnaire were unambiguous, the experimental manipulations were successful, and the experimental system was usable. Following pilot testing with 12 subjects, the actual experiment was conducted. Since prior subject mood was identified as a possible influence on the experimental result, a video-tape was used to control subject mood [37]. This approach was adopted in some previous studies, such as Oaksford et al. [53], to induce positive affect. A short (5-min) segment of a funny film was presented to all subjects before the experiment to induce a positive mood before the experiment.

The entire experiment adhered to the following six steps: (1) subjects listened to a standard introductory script and then read the background document; (2) subjects in the experimental group (using DSS) were then trained to use the systems, and sat through a session introducing stock investment, whereas those in the control group (not using DSS) merely received the investment introduction; (3) all subjects were asked to watch the mood-inducing movie; (4) all subject completed the background questionnaire; (5) subjects in the low-responsibility group were treated by asking them to read a short essay to ease their feeling of obligation, while those in the high-responsibility group were not; (6) the subjects completed the experimental tasks with or without using DSS; (7) to simulate the real world situation and generate subject emotion, subject investment performance and rewards were publicly announced; (8) all subjects were finally asked to complete the questionnaire measuring their satisfaction and regret.

## 5. Experimental findings

## 5.1. Data reliability and validity

Sixty-five subjects completed the experiment. The Cronbach's $\alpha \mathrm { { : } }$ for measuring reliability were 0.96 for user satisfaction and 0.95 for regret, respectively, indicating high acceptability [52]. Since most questionnaires were adapted from previously validated instruments and all questions were reviewed through the pretest, the content validity was acceptable. Table 3 lists the results of factor analysis on satisfaction and regret, and demonstrates evidence of convergent and discriminant validity of user satisfaction and regret. As the questions regarding satisfaction and regret fall into two distinct factors, regret is considered a different construct from satisfaction. This is consistent with prior findings [68,69].

The treatment of user responsibility was effective since subjects receiving the treatment had a lower average responsibility score (mean = 4.09) than those without the treatment (mean = 4.75). This implies feelings of responsibility differed significantly between subjects with or without the treatment (p = 0.034).

## 5.2. Findings

Table 4 lists the means and standard deviations of the resulting data. Both the average decision performance and average user satisfaction of the DSS group exceed those of the control group, but the DSS group had lower average decision regret. Meanwhile, the high-responsibility DSS group had a lower average performance and average regret than the low-responsibility counterpart, but higher average satisfaction. In the control group, the high-responsibility subgroup achieved higher average performance and average satisfaction than the lowresponsibility counterpart, but had a lower average regret.

A Pearson correlation analysis indicates a significant positive correlation between decision performance and user satisfaction, while user satisfaction and regret are significantly and negatively correlated (see Table 5).

Table 3  
Factor analysis on satisfaction and regret

<table><tr><td>Dimension</td><td>Factor 1 (satisfaction)</td><td>Factor 2 (regret)</td></tr><tr><td colspan="3">Item</td></tr><tr><td>Satisfaction 1</td><td>0.961</td><td></td></tr><tr><td>Satisfaction 2</td><td>0.981</td><td></td></tr><tr><td>Satisfaction 3</td><td>0.955</td><td></td></tr><tr><td>Regret 1</td><td></td><td>0.974</td></tr><tr><td>Regret 2</td><td></td><td>0.972</td></tr></table>

Table 4  
Mean and standard deviation under different treatments

<table><tr><td>Treatment</td><td>Performance</td><td>Satisfaction</td><td>Regret</td></tr><tr><td>DSS use</td><td>4.7059(1.7843)</td><td>4.7843(1.5524)</td><td>2.4118(1.5099)</td></tr><tr><td>Non-DSS use</td><td>3.7742(1.9272)</td><td>3.9686(2.0572)</td><td>3.9677(2.1367)</td></tr><tr><td>DSS with high responsibility</td><td>4.3889(2.0041)</td><td>5.0926(1.4811)</td><td>2.1389(1.5886)</td></tr><tr><td>DSS with low responsibility</td><td>5.0625(1.4818)</td><td>4.4375(1.6042)</td><td>2.7188(1.4020)</td></tr><tr><td>Non-DSS with high responsibility</td><td>4.4000(1.6818)</td><td>4.4000(2.1052)</td><td>3.4333(2.0342)</td></tr><tr><td>Non-DSS with low responsibility</td><td>3.1875(2.0073)</td><td>3.5625(1.9915)</td><td>4.4688(2.1715)</td></tr></table>

Standard deviations are in parenthesis.

The results imply that, although satisfaction and regret have different definition, they are strongly and negatively correlated.

Multivariate analysis of covariance (MANCOVA) was performed to test the main effect of independent variables. Moreover, Z-skewness test and Box's M test were used to test normality and variance homogeneity. The results of the Z-skewness test demonstrate that most values ranged between −1.96 to 1.96, implying that the present data meet the normality assumption. The value of the Box's M test is 25.911 $( p = 0 . 1 7 0 )$ , indicating that no statistically significant differences exist among the variances of different groups. The correlation of the dependent measures was tested using Bartlett's test of sphericity. The p-value was below 0.001, satisfying the requirements of intercorrelation for MANCOVA [32]. Thus, a MANCOVA test is appropriate and the statistical results are summarized in Table 6.

Tables 4 and 6 show that the use of DSS significantly enhances the decision performance. That is, subjects using DSS were able to choose better stock portfolio during the experiment. Consequently, hypothesis $\mathrm { H _ { l a } }$ is strongly supported $( p < 0 . 0 5 )$ . The effect of DSS use on user satisfaction is not statistically significant at the 0.05 level $\scriptstyle ( p = 0 . 0 7 4 )$ . Consequently, hypothesis $\mathrm { H } _ { \mathrm { 1 b } }$ is only marginally supported or even rejected. The effect of DSS use on decision regret is statistically significant $( p { < } 0 . 0 1 )$ . Therefore, hypothesis $\mathrm { H } _ { \mathrm { l c } }$ (DSS use reduces decision regret) is strongly supported. In other words, users with DSS are more likely to reduce regret than to increase satisfaction in this experiment. Above results demonstrate an interesting phenomenon that users will occasionally not feel satisfied despite their decisions generating positive returns. Instead, users may feel regretful when the decision performance lags a better alternative that they have forgone.

Table 5  
Pearson correlation matrix

<table><tr><td>N=65</td><td>Performance</td><td>Satisfaction</td><td>Regret</td></tr><tr><td>Performance</td><td>1.000</td><td>0.607 ***</td><td>-0.702 ***</td></tr><tr><td>Satisfaction</td><td></td><td>1.000</td><td>-0.822 ***</td></tr><tr><td>Regret</td><td></td><td></td><td>1.000</td></tr></table>

⁎⁎⁎ Correlation is significant at the 0.01 level (two-tailed).

Table 6

<table><tr><td colspan="3">Table 6Summary of results</td></tr><tr><td>Hypothesis</td><td>Result</td><td>Significance</td></tr><tr><td colspan="3">Main effects—DSS use</td></tr><tr><td> $H_{1a}$ : DSS use will increase decision performance.</td><td>Supported.</td><td>F=4.096p=0.047 **</td></tr><tr><td> $H_{1b}$ : DSS use will increase user satisfaction.</td><td>Marginal support.</td><td>F=3.299p=0.074 *</td></tr><tr><td> $H_{1c}$ : DSS use will reduce user regret.</td><td>Supported.</td><td>F=11.644p=0.001 ***</td></tr><tr><td colspan="3">Moderating effects—user responsibility</td></tr><tr><td> $H_{2a}$ : The effect of DSS use on decision performance will be moderated by user responsibility.</td><td>Supported.</td><td>F=4.884p=0.031 **</td></tr><tr><td> $H_{2b}$ : The effect of DSS use on user satisfaction will be moderated by user responsibility.</td><td>Not supported.</td><td>F=0.067p=0.796</td></tr><tr><td> $H_{2c}$ : The effect of DSS use on user regret will be moderated by user responsibility.</td><td>Not supported.</td><td>F=0.261p=0.611</td></tr><tr><td colspan="3">* p&lt;0.1.** p&lt;0.05.*** p&lt;0.01.</td></tr></table>

Fig. 4 shows that using DSS substantially improves decision performance in the low-responsibility subgroup but not in the high-responsibility subgroup $( p < 0 . 0 5 )$ . The results indicate that users with lowresponsibility may benefit more from using DSS than those with high responsibility. Hypothesis $\mathrm { H } _ { 2 \mathrm { a } }$ is thus supported. In addition, user responsibility did not have significant moderating effects on user satisfaction and user regret (see Table 6). Consequently, hypothesis $\mathrm { H } _ { 2 \mathrm { b } }$ and $\mathrm { H } _ { 2 \mathrm { c } }$ are not supported. Restated, user responsibility exerts a moderating effect only between DSS use and decision performance.

![](/api/attachments/ZVME5G4F/fulltext/images/ab4b444d7d9b5003ee9703dedb3d2ded74236226d1a225e96e93498fd70cf2db.jpg)  
Fig. 4. Decision performance by treatment.

![](/api/attachments/ZVME5G4F/fulltext/images/f0b8963c2df930d41f7f3dbd16b8ee58740da289ea3fccd264ef2801dea66608.jpg)  
Fig. 5. Satisfaction level by treatment.

According to Fig. 5, using DSS increases user satisfaction, regardless of whether the user feels high or low responsibility regarding the decision results. However, as Fig. 6 shows, using DSS reduces user regret, regardless of whether the user feels high or low responsibility. This finding suggests that DSS can help users to increase satisfaction and reduce regrets due to choosing a better alternative. Although prior studies argued that a high correlation existed between regret and responsibility, with a high sense of responsibility leading to increased regret [74–76], this study failed to identify a statistically significant moderating effect of user responsibility on regret. On the contrary, regardless of whether users were using DSS or not, the highresponsibility group had lower user regret than the lowresponsibility group. This confirms the observations of Simonson [63]: “Regret represents sorrow regarding some action or failure to act, regardless of whether the decision-maker was responsible for the outcome.” This finding suggests an indefinite relationship between regret and responsibility. Some scholars have already refuted this argument [16,63,74]. Future studies will further examine this issue.

![](/api/attachments/ZVME5G4F/fulltext/images/f7f0ff818dbf023175f80e3436d30b556498e1171c576197a6f661a993d4a5e8.jpg)  
Fig. 6. Regret level by treatment.

## 6. Conclusion and discussion

This study examined the feasibility of adopting regret to measure decision outcome. Experimental results demonstrate the effect of DSS use on decision regret. Restated, DSS use increases the decision performance and feelings of satisfaction of users, but reduces their feelings of regret. Although higher decision performance frequently leads to higher user satisfaction, and hence lower regret, the factor analysis conducted here indicates that these three constructs should be considered separate constructs. Decision-makers sometimes do not feel satisfied after forgoing a better alternative even if the outcome achieved exceeds expectation. This study demonstrated that the use of DSS can considerably reduce post-decision regret, because DSS enables users to consider more information in decision-making and thus reduce the likelihood of surprise.

User responsibility has been found to be a significant moderator between DSS use and decision performance. Particularly, DSS use was more effective in increasing decision performance for subjects with low responsibility than for those with high responsibility. This may occur because that subjects who feel high responsibility for decision performance will do their best in decisionmaking, regardless of availability of a DSS. Users in the high-responsibility group may expend more effort to ensure the best result even without DSS, provided there is sufficient time for analysis. Meanwhile, subjects with low responsibility may not spend as much time on analysis as those in the high-responsibility group during decision-making.

The above findings have numerous implications. First, this research suggests that regret can be a useful alternative for measuring decision-making outcomes. Decision-makers may feel satisfied but also regretful, if their performance exceeds prior expectations but is worse than certain forgone choices. This substantially extends our prior knowledge of DSS success. It may be necessary to include decision regret in the measurement instruments to devise a complete assessment. The two questions included in the present instrument are valid for the time being. We believe that this study is an appropriate first step toward developing more suitable models for measuring the effectiveness of DSS.

Furthermore, decision regret could provide a new dimension for explaining system adoption and usage behavior. Some decision-makers may adopt DSS for hygiene purposes (i.e. to avoid major regret rather than to pursue higher performance). Regret avoidance may also be a potentially new measure of information systems success. Additionally, the findings of this study also confirm the findings of previous studies that decision performance is enhanced by using DSS and the use of DSS increases user decision performance and avoids user regret.

Some limitations exist on the findings of this study. The strength of laboratory experiment is that the process is conducted in a controlled environment, providing relatively high internal validity. However, laboratory experiment suffers the weakness of lacking external validity when the findings are to be generalized. The findings of this study thus contain the weaknesses of the laboratory experiment.

A second potential limitation of this study is that the subjects were students. Required checks were performed as practical to miminize potential biases. For example, all subjects were business majors, and most of them had taken at lest one course in finance (98.5%) and used computers regularly (87.7%). It can reasonably be argued that these subjects had sufficient ability to make stock investment decision and use DSS properly. However, a laboratory environment differs from a real-world context. The generalizability of these findings thus is limited.

Using DSS may also affect the applicability of the findings. Some managers use DSS to optimize performance, while others may simply follow the requests of their supervisors. Regret avoidance can occur in situations involving the latter motivation. In this study, the performance-based incentive may not be sufficiently strong to generate strong motivation to pursue the best performance, and thus the motivation for avoiding regret is more significant. Nevertheless, the findings reported in this study provide a novel perspective for studying DSS adoption and success measurement.

Further research is necessary to investigate the precise role of user regret in adopting information systems and various decision aids. A follow-up comprehensive field study can be performed to assess the results obtained from this exploratory study. Examining the appropriateness of different success measures in different decision domains is also required.

## Appendix A. Questionnaires

## Questionnaires before Experiment

## A. Demographics

The objective of this questionnaire is to collect your personal background information. This can greatly help the analysis of our research findings and we guarantee that all data you provided will be used for this research only and will not be released to anyone else.

1. Name:

2. Gender: □Female □Male

3. Age:

4. Education: Degree: Major:

5. Graduation year:

6. Have you taken any course related to computer use? Yes No

7. How frequent do you use computers?

4–6 times per week everyday more than once a day

8. How much time do you use computers in a week? less than one hour 1-2 hours 2-3hours 3-4hours more than 4 hours

9. Have you taken any finance courses? Yes No

10. Do you have any experience in stock investment? Yes No

11. Have you bought stocks before? Yes No

## B. Investment decision

1. Please choose three stocks that you may buy from the six listed below.

□A □B □C □D □E □F

2. Please find one for investment from the three you have chosen in the previous question. Make your decision carefully, since this will affect your final performance for winning the prize!

□A □B □C □D □E □F

Questionnaires for measuring user responsibility

<table><tr><td></td><td>Extremely Low</td><td>Very Low</td><td>Low</td><td>Normal</td><td>High</td><td>Very High</td><td>Extremely High</td></tr><tr><td>Do you feel responsible for the erroneous investment decision?</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td></td><td colspan="7">Questionnaires after the decision</td></tr><tr><td></td><td>Strongly Disagree</td><td>Very Disagree</td><td>Disagree</td><td>No Idea</td><td>Agree</td><td>Very Agree</td><td>Strongly Agree</td></tr><tr><td>1. I am happy with the performance of the stock I chose.</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>2. I am pleased with the performance of the stock I chose.</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>3. I feel satisfied with the performance of the stock I chose.</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>4. I feel sorry for having chosen this stock.</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>5. I feel regretful for having chosen this stock.</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr></table>

## References

[1] M. Alavi, E.A. Joachimsthaler, Revisiting DSS implementation research: a meta-analysis of the literature and suggestions for researchers, MIS Quarterly 16 (1) (1992) 95–116.

[2] S.L. Alter, A taxonomy of decision support systems, Sloan Management Review 19 (1977) 39–56.

[3] S.L. Alter, Decision Support Systems: Current Practice and Continuing Challenge, Addison-Wesley, Reading, MA, 1980.

[4] R. Barkhi, V.S. Jacob, L. Pipino, H. Pirkul, A study of the effec of communication channel and authority on group decision processes and outcomes, Decision Support Systems 23 (3) (1998) 205–226.

[5] H. Barki, Determinants of user satisfaction judgments in information systems, Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences, 1990, pp. 408–417.

[6] S.H. Barr, R. Sharda, Effectiveness of decision support systems: development or reliance effect? Decision Support Systems 21 (2) (1997) 133–146.

[7] D.E. Bell, Regret in decision making under uncertainty, Operations Research 30 (5) (1982) 961–981.

[8] D.E. Bell, Risk premiums for decision regret, Management Science 29 (10) (1983) 1156–1166.

[9] I. Benbasat, B.R. Nault, An evaluation of empirical research in managerial support systems, Decision Support Systems 6 (1990) 203–226.

[10] P. Bharati, A. Chaudhury, An empirical investigation of decisionmaking satisfaction in web-based decision support systems, Decision Support Systems 37 (2004) 187–197.

[11] A. Bhattacherjee, Understanding information systems continuance: an expectation confirmation model, MIS Quarterly 25 (3) (2001) 351–370.

[12] R. Blanning, The functions of a decision support system, Information & Management 2 (1979) 87–93.

[13] D.S. Boninger, F. Gleicher, A. Strathman, Counterfactual thinking: from what might have been to what may be, Journal of Personality and Social Psychology 67 (1994) 297–307.

[14] W.L. Cats-Baril, G.P. Huber, Decision support systems for ill structured problems: an empirical study, Decision Sciences 18 (1987) 350–372.

[15] Z. Chen, User responsibility and exception handling in decision support systems, Decision Support Systems 8 (6) (1992) 537–540.

[16] T. Connolly, L.D. Ordóñez, R. Coughlan, Regret and responsibility in the evaluation of decision outcomes, Organizational Behavior and Human Decision Processes 70 (1) (1997) 73–85.

[17] A.D.J. Cooke, T. Meyvis, A. Schwartz, Avoiding future regret in purchase-timing decisions, Journal of Consumer Research 27 (4) (2001) 447–459.

[18] M.D. Crossland, B.E. Wynne, W.C. Perkins, Spatial decision support systems: an overview of technology and a test of efficacy, Decision Support Systems 14 (3) (1995) 219–235.

[19] F.D. Davis, J.E. Kottemann, User perceptions of decision support effectiveness: two production planning experiments, Decision Sciences 25 (1) (1994) 57–78.

[20] W.J. Doll, G. Torkzadeh, The measurement of end-user computing satisfaction, MIS Quarterly 12 (2) (1988) 259–274.

[21] M.A. Eierman, F. Niederman, C. Adams, DSS theory: a model of constructs and relationships, Decision Support Systems 14 (1995) 1–26.

[22] H.B. Eom, S.M. Lee, A survey of decision support systems applications (1971–April 1988), Interfaces 20 (3) (1990) 65–79.

[23] J. Etezadi-Amoli, A.F. Farhoomand, A structural model of end user computing satisfaction and user performance, Information & Management 30 (2) (1996) 65–73.

[24] M. Gelderman, Factors affecting the success of management support systems: analysis and meta-analysis, Proceedings of the IS/MAS forum of the Annual Conference of the American Accounting Association, Orlando, FL, August, 1995.

[25] M. Gelderman, The relation between user satisfaction, usage of information systems and performance, Information & Management 34 (1) (1998) 11–18.

[26] T. Gilovich, V.H. Medvec, The temporal pattern to the experience of regret, Journal of Personality and Social Psychology 67 (3) (1994) 357–365.

[27] T. Gilovich, V.H. Medvec, The experience of regret: what, when, and why, Psychological Review 102 (2) (1995) 379–395.

[28] M.J. Ginzberg, DSS success: measurement and facilitation, in: C. W. Holsapple, A.B. Whinston (Eds.), Data-Base Management: Theory and Application, North Holland, 1983, pp. 367–387.

[29] C. González, G.M. Kasper, Animation in user interfaces designed for decision support systems: the effects of image abstraction, transition, and interactivity on decision quality, Decision Science 28 (4) (1997) 793–823.

[30] S. Gregor, I. Benbasat, Explanations from intelligent systems: theoretical foundations and implications for practice, MIS Quarterly 23 (4) (1999) 497–530.

[31] T. Guimaraes, M. Igbaria, M. Lu, The determinants of DSS success: an integrated model, Decision Sciences 23 (2) (1992) 409–430.

[32] J.F. Hair, R.E. Anderson, R.L. Tatham, W.C. Black, Multivariate Data Analysis, Prentice-Hall, Upper Saddle River, NJ, 1995.

[33] J.C. Henderson, D.A. Schilling, Design and implementation of decision support systems in the public sector, MIS Quarterly 9 (2) (1985) 157–169.

[34] C.W. Holsapple, Decision support in multiparticipant decision makers, Journal of Computer Information Systems 31 (4) (1991) 37–45.

[35] P.C. Humphreys, O. Larichev, A. Vári, J. Vecsenyi, Comparative analysis of use of decision support systems in organizations, in: H. Sol (Ed.), Processes and Tools for Decision Support, North-Holland, 1983, pp. 207–234.

[36] J.J. Inman, J.S. Dyer, J. Jia, A generalized utility model of disappointment and regret effects on post-choice valuation, Management Science 16 (2) (1997) 97–111.

[37] A.M. Isen, B. Means, R. Patrick, G. Nowicki, Some factors influencing decision-making strategy and risk taking, in: M.S. Clark, S.T. Fiske (Eds.), Affect and Cognition: The 17th Annual Carnegie Symposium on Cognition, Lawrence Erlbaum, Hillsdale, NJ, 1982, pp. 243–261.

[38] B. Ives, M.H. Olson, User involvement and MIS success: a review of research, Management Science 30 (5) (1984) 586–603.

[39] D. Kahneman, A. Tversky, The psychology of preference, Scientific American 246 (1982) 160–173.

[40] P.G.W. Keen, M.S. Scott-Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, MA, 1978.

[41] K.E. Kendall, J.R. Buffington, J.E. Kendall, The relationship of organizational subcultures to DSS user satisfaction, Human Systems Management 7 (1987) 31–39.

[42] R. Kohli, S. Devaraj, Contribution of institutional DSS to organizational performance: evidence from a longitudinal study, Decision Support Systems 37 (2004) 103–118.

[43] J. Landman, Regret and elation following action and inaction: affective responses to positive versus negative outcomes, Personality and Social Psychology Bulletin 13 (4) (1987) 524–536.

[44] J. Landman, Regret: The Persistence of the Possible, New York, Oxford University Press, 1993.

[45] R.P. Larrick, T.L. Boles, Avoiding regret in decisions with feedback: a negotiation example, Organizational Behavior and Human Decision Processes 63 (1) (1995) 87–97.

[46] L.A. Le Blanc, K.A. Kozar, An empirical investigation of the relationship between DSS usage and system performance: a case study of a navigation support system, MIS Quarterly 14 (3) (1990) 263–277.

[47] T.P. Liang, Critical success factors of decision support system: an experimental study, Data Base 17 (2) (1986) 3–16

[48] G. Loomes, R. Sugden, Regret theory: an alternative theory of rational choice under uncertainty, Economic Journal 92 (1982) 805–824.

[49] M.A. Mahmood, J.A. Sniezek, Defining decision support systems: an empirical assessment of end-user satisfaction, Information System & Operational Research (INFOR) 27 (3) (1989) 253–271.

[50] B.E. Mennecke, M.D. Crossland, B.L. Killingsworth, Is a map more than a picture? The role of SDSS technology, subject characteristics, and problem complexity on map reading and problem solving, MIS Quarterly 24 (4) (2000) 601–629.

[51] A.R. Montazemi, F. Wang, S.M.K. Nainar, C.K. Bart, On the effectiveness of decisional guidance, Decision Support Systems 18 (2) (1996) 181–198.

[52] J.C. Nunnally, Psychometric Theory, 2nd edition, McGraw-Hill, New York, 1978.

[53] M. Oaksford, F. Morris, B. Grainger, J.M.G. Williams, Mood, reasoning, and central executive processes, Journal of Experimental Psychology. Learning, Memory, and Cognition 22 (2) (1996) 476–492.

[54] R.L. Oliver, Effect of expectation and disconfirmation on postexposure product evaluations: an alternative interpretation, Journal of Applied Psychology 62 (4) (1977) 480–486.

[55] R.L. Oliver, A cognitive model of the antecedents and consequences of satisfaction decisions, Journal of Marketing Research 17 (4) (1980) 460–469.

[56] L.D. Ordóñez, T. Connolly, Regret and responsibility: a reply to Zeelenberg et al. (1998), Organizational Behavior and Human Decision Processes 81 (1) (2000) 132–142.

[57] M. Parikh, B. Fazlollahi, S. Verma, The effectiveness of decisional guidance: an empirical evaluation, Decision Sciences 32 (2) (2001) 303–331.

[58] G.L. Sanders, J.F. Courtney, A field study of organizational factors influencing DSS success, MIS Quarterly 9 (1) (1985) 77–93.

[59] R. Sharda, S.H. Barr, J.C. McDonnell, Decision support system effectiveness: a review and an empirical test, Management Science 34 (2) (1988) 139–159.

[60] A. Shirani, M. Aiken, J.G.P. Paolillo, Group decision suppor systems and incentive structures, Information & Management 33 (5) (1998) 231–240.

[61] H.A. Simon, The New Science of Management Decision, Harper & Row, New York, 1960.

[62] H.A. Simon, Models of Bounded Rationality, The MIT Press, Cambridge, MA, 1982.

[63] I. Simonson, The influence of anticipating regret and responsibility on purchase decisions, Journal of Consumer Research 19 (1) (1992) 105–118.

[64] M. Swink, The influences of user characteristics on performance in a logistics DSS application, Decision Sciences 26 (4) (1995) 503–529.

[65] M. Swink, E.P. Robinson Jr, Complexity factors and intuitionbased methods for facility network design, Decision Sciences 28 (3) (1997) 583–614.

[66] M. Swink, C. Speier, Presenting geographic information: effects of data aggregation, dispersion, and users' spatial orientation, Decision Sciences 30 (1) (1999) 169–195.

[67] P. Todd, I. Benbasat, The use of information in decision making: an experimental investigation of the impact of computer-based decision aids, MIS Quarterly 16 (3) (1992) 373–393.

[68] M. Tsiros, Effect of regret on post-choice valuation: the case of more than two alternatives, Organizational Behavior and Human Decision Processes 76 (1) (1998) 48–69.

[69] M. Tsiros, V. Mittal, Regret: a model of its antecedents and consequences in consumer decision making, Journal of Consumer Research 26 (4) (2000) 401–417.

[70] G.H. van Bruggen, A. Smidts, B. Wierenga, Improving decision making by means of a marketing decision support system, Management Science 44 (5) (1998) 645–658.

[71] R. Westermann, K. Spies, G. Stahl, F.W. Hesse, Relative effectiveness and validity of mood induction procedures: a meta-analysis, European Journal of Social Psychology 26 (4) (1996) 557–580.

[72] M. Zeelenberg, J. Beattie, Consequences of regret aversion 2: additional evidence for effects of feedback on decision making, Organizational Behavior and Human Decision Processes 72 (1) (1997) 63–78.

[73] M. Zeelenberg, J. Beattie, J. van der Pligt, N.K. de Vries, Consequences of regret aversion: effects of expected feedback on risky decision making, Organizational Behavior and Human Decision Processes 65 (2) (1996) 148–158.

[74] M. Zeelenberg, W.W. van Dijk, A.S.R. Manstead, Reconsidering the relation between regret and responsibility, Organizational Behavior and Human Decision Processes 74 (3) (1998) 254–272.

[75] M. Zeelenberg, W.W. van Dijk, A.S.R. Manstead, J. van der Pligt, The experience of regret and disappointment, Cognition and Emotion 12 (1998) 221–230.

[76] M. Zeelenberg, W.W. van Dijk, J. van der Pligt, A.S.R. Manstead, P. van Empelen, D. Reinderman, Emotional reactions to the outcomes of decisions: the role of counterfactual thought in the experience of regret and disappointment, Organizational Behavior and Human Decision Processes 75 (2) (1998) 117–141.

![](/api/attachments/ZVME5G4F/fulltext/images/257f86bc8a6289dd28dc9987ccd5e6e747514e3aabd0307ae5427a1bf44e5d44.jpg)

Shin-Yuan Hung is an Associate Professor of Information Systems, and the Head of Division of Information Management of Computer Center at National Chung Cheng University in Taiwan. He holds a Ph.D. in Information Systems from the National Sun Yat-sen University in Taiwan. His current research interests include decision support systems, electronic commerce, data mining, and knowledge management. Dr. Hung has published a number of papers in Information & Management, Decision Support Systems,

Expert Systems with Applications, Government Information Quarterly, Electronic Commerce Research and Applications, Information Technology & People, Computer Standard and Interfaces, Industrial Management and Data Systems, International Journal of Management Theory and Practice, Journal of Chinese Information Management, among others.

![](/api/attachments/ZVME5G4F/fulltext/images/10f717c2af04a38d51d7aeec22db7d0d5b94d0c87aa8a8c1d13ca4aeec199928.jpg)

Yi-Cheng Ku is currently an Assistant Professor of the Department of Computer Science and Information Management, Providence University in Taiwan. He received his doctoral degree in Information Management from the National Sun Yat-sen University in 2005. His research interests include recommendation system, innovation adoption and diffusion, and knowledge management.

Chang-Jen Lee received his Master's degree in the MIS from the National Chung Cheng University. Currently, he is an MIS staff in the ACE Corporation.

![](/api/attachments/ZVME5G4F/fulltext/images/0f335694d4cbccbd7e41015ff1bed3fa09c88e204fb150afb50f01fe4f981cff.jpg)

Ting-Peng Liang is the Director of Electronic Commerce Research Center and National Chair Professor of Information Management at the National Sun Yat-sen University in Taiwan. Prior to his current position, he had been the Dean of Academic Affairs and Dean of the College of Management, Director of the Graduate Institute of Information Management, and Director of the Software Incubator of the same university. He received his doctoral degree in Information Systems from

the Wharton School of the University of Pennsylvania and had taught at the University of Illinois and Purdue University until 1993. His primary research interests include electronic commerce, intelligent systems, decision support systems, knowledge management, and strategic applications of information systems. His papers have appeared in a number of journals such as Management Science, MIS Quarterly, Journal of MIS, Operations Research, Decision Support Systems, and Decision Sciences. He also serves on the editorial boards of several academic journals, such as Decision Support Systems and International Journal of Electronic Commerce.

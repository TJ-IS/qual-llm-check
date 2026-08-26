---
otero_id: 27353
otero_key: "FSG4G2KR"
title: "Semi-Structured Recurring Decisions: An Experimental Study of Decision Making Models and Some Suggestions for DSS"
authors: "William Remus; Jeffrey E. Kottemann"
year: "1987"
journal: "MIS Quarterly"
doi: "10.2307/249368"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Semi-Structured Recurring Decisions: An Experimental Study of Decision Making Models and Some Suggestions for DSS

Author(s): William Remus and Jeffrey E. Kottemann

Source: MIS Quarterly, Vol. 11, No. 2 (Jun., 1987), pp. 233-243

Published by: Management Information Systems Research Center, University of Minnesota

Stable URL: http://www.jstor.org/stable/249368

Accessed: 24-12-2015 23:24 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Semi-Structured Recurring Decisions: An Experimental Study of Decision Making Models and Some Suggestions for DSS

By: William Remus & Jeffrey E. Kottemann University of Hawaii 2404 Maile Way Honolulu, HI 96822 (808) 948-7430

## Introduction

The semi-structured problem is the domain of decision support systems (DSS) research and development. The domain of semi-structured problems, however, encompasses many different decision types. For example, the following dichotomous decision attributes define potentially 32 different types of decisions, most of which may be classified as semi-structured.

1. Recurring versus nonrecurring decisions

2. Stable versus dynamic environments

3. Reliable versus unreliable information on current position

## Abstract

5. Clear versus ambiguous goals

4. Reliable versus unreliable information on future states of the environment

And as one would expect, somewhat different DSS requirements exist for each decision type.

A key to designing an effective computer-based decision support system is deciding which models best support the decision makers. Since most decision support systems include optimizing rather than tracking models, this experiment examines the evidence for tracking when making a production scheduling decision. The experiment found evidence that tracking behavior was occurring. This suggests the need to support tracking behavior with decision support systems. Approaches to such support are offered.

This data was supported by the National Science Foundation under Grant IST-84-03844.

ACM Categories: H.4.2

Keywords: Decision making; decision support systems; tracking; production scheduling)

This paper concerns one class of relatively semi-structured problems characterized by (a) recurring decisions in (b) a dynamic decision environment with (c) reliable data on current position and (d) less-than-reliable projections of future states of the environment, and finally (e) clear objectives for performance. Thus the task is complex by virtue of environmental uncertainty rather than ambiguity per se (see Daft and Lengel [3]).

In such tasks the decision maker repeatedly assesses current data and projections to identify trends or patterns upon which to base decisions. The decision maker also uses feedback to assess his/her performance and to adjust decision making strategies. Tasks that more-or-less fit this characterization include altering investment portfolio mixes, preparing and updating budgets, analyzing and acting on trends in retail industries, and making production scheduling decisions given uncertain demand.

A critical prerequisite to developing DSS for this class of decision tasks is to identify how such decisions are made. That is, do decision makers optimize or satisfice given such a task? If they satisfice, what heuristic procedures do decision makers use? And finally, what DSS capabilities or tools can support heuristic decision making?

## The Study

This paper attempts to answer these questions. A production scheduling decision is used in an experimental setting in order to assess various models of decision making: notably, (1) regression rules generated from actual decisions, (2) the tracking model, and (3) optimal rules. The generation and use of regression rules was suggested by Bowman [1] as a way to improve decision making by eliminating erratic decisions, or said another way, by increasing the consistency of decisions. The tracking model depicts decision makers as following a moving target (consumer demand) through adjustments in their production. Optimal rules (as discussed below) provide a reference point for model performance.

The production scheduling decision task used in the experiment is based upon the formulation of Holt, Modigliani, Muth and Simon [10]. This formulation allows the determination of optimal solutions which can be compared with actual decisions and with decisions made using other models.

It might be argued that the existence of optimal solutions disqualifies the production scheduling task from being considered as a semi-structured problem. We do not believe this is the case. A problem, from the viewpoint of the decision maker, is semi-structured as long as the decision maker sees it as such. Whether or not a given problem has an optimal solution method is irrelevant if the decision maker is ignorant of the solution method, as is the case in the experiment reported here. Further, since in the production scheduling task sales demand is stochastic and forecasts have additional random error introduced, optimal solutions exist only in a probabilistic sense. At the very least, then, the experimental task used is semi-structured because subjects were not aware of the formal solution method and because the stochastic elements engender uncertainty.

## The production

## scheduling decision

The production scheduling problem has received much attention in the management literature. Numerous models (and optimal solutions) for the problem have been presented (see [5]). Perhaps the best known formulation is by Holt, Modigliani, Muth and Simon [10] which assumes quadratic costs. Quadratic costs are a function of worker overtime and idletime, the cost of changing the size of the work force, and the cost of holding other than optimal amounts of inventory.

Optimal linear decision rules can be found through differential calculus to minimize long run costs [9]. When the planning horizon is three periods, these optimal rules are a linear function of last period's work force level, last period's inventory level, and the forecasts for demand (see appendix).

Bowman [1] developed his managerial coefficient theory based on the production scheduling problem. His theory asserts that, on the average, managers make good decisions. It is the occasional erratic decision which cause economic inefficiency. Bowman prescribed the use of regression rules to capture managerial judgement and to improve decision making. These rules have been shown to outperform the production scheduler's actual decisions in a number of studies [1, 11, 12, 13, 20]. Remus [18] verified Bowman's assertion that erratic decision making is the major cause of economic inefficiency using experimental production scheduling data. Bowman's rules seldom perform as well as the Holt, Modigliani, Muth and Simon optimal rules [1, 12, 13, 20].

Several factors have been shown to effect the quality of the production scheduling decision. Moskowitz and Miller [12, 13] found that providing schedulers with sales forecasts with lower inherent error improved their decisions. They also found that schedulers having three rather than one period of sales forecasts made better decisions. Ebert [4] found that both the planning protocol used and the introduction of irrelevant cost factors effected the schedulers' decision making.

## Tracking

In the production scheduling problem, the decision maker can also be viewed as tracking customer demand such that demand fluctuations are absorbed in order to minimize cost. In this characterization, the managerial problem is similar to that of a gunner trying to track an enemy plane. Rather than trying for discrete optimal hits each time, the gunner uses various strategies to follow the target. This corresponds to Hogarth's [7] notion of continuous decision processes. If this characterization is right, the DSS should support the decision maker with appropriate aids.

As one might suspect, the literature on tracking arises primarily from military problems like the prior example. In that context the tracking problem is subdivided along two dimensions. The first dimension distinguishes between the physical human factors in using the equipment and the mental strategies used in tracking.

The other dimension distinguishes between two common tracking problems. In pursuit tracking, both the position of the target and the movement of the control element are known. For example, a stagehand trying to track an actor with a spotlight would be considered pursuit tracking. In compensatory tracking, however, the tracker does not see the targets location and only an error signal is provided to aid in tracking. A driver trying to keep a fixed speed limit on a hilly road would be an example of compensatory tracking.

Compensatory tracking is generally more difficult. Production scheduling with unknown demand, when conceived as a tracking problem, is compensatory tracking with mental strategy as the crucial element. The review which follows focuses only on the mental dimension of tracking; Poulton [17] provides an excellent review of the entire tracking literature.

When a human decision maker is tracking and physical factors do not interfere, the decision maker will normally be subject to several biases. With sine wave target tracks, the tracker will normally lag the target. Since the target movement is sinusoidal, this lag can be measured as degrees of phase displacement. Figure 1 depicts a 30 degree phase displacement. The tracker will also tend toward the mean of the track, particularly as the extremes of the sine wave are approached. Searle and Taylor term this the range effect [23]. It can be measured as the ratio of the tracking sine wave amplitude to the target sine wave amplitude. The ratio is $80\%$ in Figure 1. The tracking error is usually characterized by a root-mean-square (R.M.S.) error.

Generally the phase displacement and range effect vary across individuals. The phase displacement is usually a lag relationship. The range effect is usually characterized with a ratio of less than 1; that is, humans tend to be conservative and under react to the extreme points of the track. Doubling the amplitude of the sine wave about doubles the average R.M.S. error [16]. Also, increasing the sine wave frequency increases the lag [17, p. 113]. The R.M.S. error increases when multiple frequency components at differing amplitudes are introduced. The extent of the impact varies greatly with the mixture of amplitudes and frequencies assigned to the target [14, 15].

![](/api/attachments/FSG4G2KR/fulltext/images/405e8be03ebd1387fd51946ae97837251087b4daa53d7846b06a0d69bbc7441e.jpg)  
Figure 1. The Range Effect and Phase Displacement

In doing experimental work there are numerous factors which can confound the experimental results on tracking. Many confounding factors disappear when a low frequency track like a sinusoidal demand is present. Two factors, however, are important enough to be addressed in the experimental design. First, tracking skills generally increase with experience. Therefore, the subjects must be equally naive when in the experimental setting and error should be aggregated across time periods only with care. Second, tracking experience can transfer from one problem setting to another. Therefore, care must be taken to select subjects with no experience in related problems [6]. See Poulton [17] for more information on experimental design and measurement problems in tracking studies.

## Experimental design

This experiment examines decision making behavior when making production scheduling decisions. To reduce the potential for confounding, this study sets the experimental parameters based on related research. Exhibit 1 juxtaposes this experiment with the literature discussed above. For example, there has been a great deal of controversy about using MBA students as surrogates for managers in studies of decision making behavior. To deal with that objection, Remus [19] conducted research comparing MBA students with managers pursuing an MBA degree. In that study based on the production scheduling problem, no significant differences were found. Apparently MBA students are suitable surrogates for managers, at least in this experimental setting.

Exhibit 1 The Experiment and the Literature

<table><tr><td>1. Level of Performance Feedback</td><td>Remus, Carter, and Jenicke [27] found the level of feedback used in the proposed experiment promoted good decision making without information overload.</td></tr><tr><td>2. Number of Periods in the Forecast Horizon</td><td>Moskowitz and Miller [13] found the three period horizon to yield better decisions than shorter horizons.</td></tr><tr><td>3. Level of Forecast Error Used</td><td>The forecast error is set at the Moskowitz and Miller [13] intermediate level of error—an amount which is neither trivial nor overwhelming.</td></tr><tr><td>4. Patterns in Demand</td><td>The demand pattern was created as a sine wave of an eight period duration since the tracking problems with sine waves are very clearly researched (Poulton, [17]).</td></tr><tr><td>5. Effectiveness of Bootstrapping in the Experimental Environment</td><td>With the production scheduling problems, bootstrapping (via regression models) works well (Bowman, [1] and many others).</td></tr><tr><td>6. Cost Function</td><td>The cost function is the production scheduling model developed for a real paint plant in Pittsburgh [9].</td></tr><tr><td>7. Use of MBA Students as Surrogates for Managers</td><td>There is no significant differences in cost performance in the production scheduling problem for MBA students without full time work experience and experienced managers in an MBA program [19].</td></tr><tr><td>8. Subjects are Equally Naive</td><td>As noted by Poulton [17], experience effects tracking of performance. A practical way to equalize the level of experience (and thereby reduce confounding) is to select equally naive subjects</td></tr></table>

The 51 subjects in the experiment were MBA candidates from a required course in operations research. Over 85% of the subjects had either full or part time jobs in business and government; none were employed as production schedulers. Participation in the experiment was a course requirement. None of the subjects had prior experience in this scheduling task or other exercises from which learning might be transferred.

The subjects were first given a presentation on the production scheduling decision, including how to make good decisions. The subjects were then assigned a time at which they were to make the decisions. When they arrived for the session, they signed on to a time-sharing computer and initiated the production scheduling simulator.

After four practice periods, the subjects made production and workforce decisions for 24 periods. Subjects received first the sales forecasts for the next three periods. Based on these forecasts, the inventory position, current workforce size and the worker productivity index, the subjects decided the production volume to schedule and the number of workers to employ. After they input their decisions, the computer gave them an opportunity to check that they had correctly typed in their decisions. The subjects then received the actual sales and costs, the new inventory level, and the average cost thus far. All the cost and inventory calculations were done by the computer. This cycle was repeated for each of the 24 periods.

The number of periods of forecasts to provide and the levels of forecast error were set to coincide with other researchers. Moskowitz and Miller [13, 14] found that a three period forecast gave superior results to shorter forecast horizons; hence, three periods of forecast were used for the experiment. The Moskowitz and Miller study used forecasts with three different levels of forecast error; we used their intermediate level of forecast error. The quadratic cost function used in the experiment was found by Holt, Modigliani, and

Muth [9] to characterize a paint plant in Pittsburgh (see appendix).

The demand was initially set at 2500 units. The demand pattern was an eight period sinusoidal pattern peaking at 20% above the unadjusted demand. The demand pattern was also given intermediate or low variability by adjusting it with a uniformly distributed variation of $\pm400$ or $\pm100$ units of demand. (Schroeder and Benbasat [22] used demand variability as a surrogate for environmental uncertainty.) Each subject received a unique pattern of adjusted demand by randomly sampling from a uniform distribution based upon a random number generator seeded with their social security number.

The low variability level was used by Moskowitz and Miller [13] and in earlier work (e.g. [20, 21]); hence there is a comparability of results at this level of variability. The Moskowitz and Miller [13] study and others have found subjects to approach (and occasionally exceed) optimal performance at this level of variability. The intermediate variability treatment is similar to that of Moskowitz and Miller's [13] intermediate forecast variability treatment. Since Moskowitz and Miller found quality decision making at their intermediate treatment, the treatment in the current study would seem well calibrated. The research questions posed were:

1. Are the subjects optimal decision makers?

2. When the error variance is reduced by the use of the Bowman's policy capturing model, are the subjects optimal decision makers?

3. If the decision makers are not optimal decision makers, does the data show tracking artifacts such as phase displacement and range effect?

4. Do the levels of demand variability affect the tracking artifacts?

In order to properly restrict comparability with other experiments and qualify the generalizability of the task, we note these other task attributes:

1. No time pressure was induced.

2. Subjects were instructed that the goal was to minimize total cost but were not told what a "good" cost figure would be, nor did they see how others performed.

Thus, the decision has a clear outcome measure yet not a clear reference point for assessing the quality of decisions.

3. No indication was given of the reliability of the demand forecasts presented.

4. No irrelevant information (including irrelevant cost factors) was knowingly presented to the subjects.

## Results

The performance of the subjects was measured in three ways. First, as the subject made decisions the actual costs were calculated and recorded; these costs were based on actual decisions. Second, the records of each subject's data were accessed, and regressions were run to determine the subject's regression weights (as would be prescribed by Bowman [1]). These equations using the subject's betas were then used to calculate production and work force decisions, and resultant costs were calculated using the paint plant cost function. This procedure for evaluating Bowman's rules has been used in similar studies. Costs based on Bowman's policy-capturing regression rules can be interpreted as the costs if the subjects had consistently used their factor weightings (captured by the regression rule) to make their decisions. This model reduces the erratic component of decision making which Bowman [1] had theorized and Remus [18] had shown to be a major source of poor decision making. Analyses based on these rules compare the economic performance of consistent decision makers. Third, the optimal rules were used to calculate production and work force decisions; the costs were again found using the quadratic function.

The 24 periods were divided into two portions based on the outcome of an earlier experiment [20]; in periods 1–12 the subjects learned to make good decisions and in 13–24 they continued to use the strategy they had developed. For this reason the learning and stable decision making phases were separated for the analysis shown in Table 1. The data was also conditioned (“winsorized”) to reduce the effects of outliers on the t-tests [24]. This was essential since one outlier can badly distort a mean value.

In both phases, the subjects' actual costs were higher than the Bowman rule costs, which in turn were higher than the optimal costs. Clearly the subjects were not optimal decision makers even when the erratic component of their decision making was reduced by using Bowman's rules. Although the subjects made better decisions in the last 12 periods, it is difficult to find evidence that they were becoming optimal.

The data were next examined to determine if tracking behavior was occurring. First the actual demand was plotted against the optimal and actual decisions. If tracking was occurring, then the graphs should show phase displacement (lags) near each of the cross-over points (i.e. periods 4, 8, 12, 16 and 20) and range effects near each of the peaks and troughs (i.e. periods 2, 6, 10, 14, and 18). Figure 2 is a graph of demand versus optimal and actual decisions showing both range and phase effects for a typical subject.

In both intermediate and low demand variability conditions, phase displacement and range effects occurred as shown in Table 2. In the low variability condition, subjects lagged 69% of the time, led 13% of the time, and were close to on-the-mark 18% of the time. Thus lags occurred much more often than leads. Overall phase displacement was 63 degrees and the R.M.S. error was 205. The range effect was also exhibited; the peak number of units scheduled was on the average 69% of the peak demand.

Table 1. Average Costs

<table><tr><td>Periods</td><td>Optimal Costs</td><td>Average Individual Rule Cost</td><td>Average Actual Cost</td></tr><tr><td>1–12</td><td>30607</td><td>37222</td><td>55054</td></tr><tr><td>13–24</td><td>26491</td><td>33783</td><td>43079</td></tr></table>

Differences between all pairs of costs in the same row are significant at p < .02

![](/api/attachments/FSG4G2KR/fulltext/images/e9e9814b09d39e985adb13219a9affeaa9ea75fce1cfa5bd68c45a4ca976b9eb.jpg)  
Figure 2. One Subject's Response to the Demand

In the intermediate variability condition, the subjects lagged 69% of the time, led 15% of the time, and were close to on-the-mark 16% of the time. Again lags were more prevalent than leads. Overall phase displacement was 70 degrees and the R.M.S. error was 217. The range effect also occurred; the average peak number of units scheduled was 77% of the peak demand. Note that tracking artifacts are not necessarily dysfunctional. Indeed, the optimal model results in range effects. As alluded earlier, optimal tracking will absorb demand fluctuations in order to minimize cost.

The phase displacements and range effects were exaggerated in the actual decisions, however.

Thus, both conditions show tracking artifacts; the subjects showed both the range effect and phase displacement artifacts. The variability conditions do not significantly differ in the level of range effect, R.M.S. error, or phase displacement, but these three measurements are higher in intermediate demand variability than in low demand variability. This finding is consistent with Poulton's review [17].

Table 2. Impact of Intermediate and Low Demand Variability on Tracking

<table><tr><td></td><td>Intermediate Variability (N = 19)</td><td>Low Variability (N = 32)</td></tr><tr><td>Phase Displacement (Lag) Relative to Demand</td><td>70°</td><td>63°</td></tr><tr><td>Range Effect as Percent of Peak Relative to Demand</td><td>77%</td><td>69%</td></tr><tr><td>RMS Error Relative to Optimal</td><td>217</td><td>205</td></tr></table>

Although optimal rules exist to determine lowest cost production scheduling decisions, the subjects failed to make optimal decisions. Even when Bowman's rules were used to reduce the erratic component of the subject's decision making, the costs were still much above optimal levels. Bowman [1] had earlier noted this phenomenon in a field study with actual production schedulers. Further analysis of the data found strong tracking artifacts. The tracking artifacts noted were consistent with those noted in the tracking literature. The tracking paradigm which has been used in hunting animals and in making war for thousands of years is still apparent in modern decision making.

While it is important for the DSS model base to still have optimizing models, this research suggests tracking support models would also be helpful. This is especially true where no optimal model exists and tracking is a reasonable approach.

## DSS for Recurring, Semi-Structured Decisions

Hogarth [7] has argued that many judgement and decision making situations are mischaracterized as discrete processes when indeed they are relatively continuous and that this mischaracterization has exaggerated the impression of humans as poor decision makers. A money manager, for example, does not make one judgement followed by one decision. Rather, a money manager tracks the environment, making many decisions over time and making many more judgements than decisions. He uses one or more decision strategies that may change over time as feedback accrues and as conditions change. His predictive successes and failures may be due to the information selected for judgement, the weights given the information, the information-combination rule used [7], or simply the level of environmental uncertainty.

Existing DSS do recognize the ubiquity of uncertainty hence the “what if” banner of DSS. DSS also recognize the prevalence of recurring decisions, hence multi-period modeling. If indeed decision makers are trackers, existing decision aids fall short on one critical front—direct support for perfecting decision strategies over time.

Whereas current DSS support queries on data values within a model, they do not readily support queries on structural elements of models themselves. Also, DSS do not support the rich historical perspective necessary for tracking. Important elements of such history include past actual states and past forecasts, past decision alternatives chosen and those not chosen, past decision strategies explicitly used and those implicitly used. We now suggest some ways in which DSS might better support tasks such as production scheduling. The suggestions are made in the context of the current experimental findings regarding Bowman rules and tracking artifacts.

A number of simple tracking aids can be realized using existing DSS and by repackaging DSS components. Graphics packages can, of course, be used to plot planned versus actual levels of variables. If DSS were packaged with statistical analysis routines, data patterns could be formally modeled using time series analysis. Also, the system could derive Bowman rules, and decisions generated using the rules could be plotted against planned decisions or decisions actually made. This capability may give decision makers insight into the existence and impact of consistency in decision making and of phase displacement and range effects. In short, it may help decision makers formulate more effective tracking strategies.

Bowman rules are models of decision making strategies, albeit simplified models. They reflect the regressed importance (betas) given various decision making data. By allowing decision makers to “what if” the beta weights, the DSS is allowing decision makers to simulate themselves giving differing weightings to decision making data and decision variables. If the DSS has also allowed decision makers to record past decision alternatives and forecasts that were not adopted, then similar analyses can be performed using these data. For example, unadopted alternatives that fit the generated Bowman rule better than alternatives actually adopted can be identified and their performance simulated. Also, alternate Bowman rules can be compared using various scenarios of past unadopted alternatives. In addition, decision makers may elect to partition past periods, generate rules for each partition, and investigate the evolution of their decision weightings.

Sensitivity analyses such as the above might be termed retakes. They are an extension of the common practice of comparing planned versus actual values of decision variables (such as budget figures), and of data that affect decisions (such as actual versus projected interest rates). Retakes are based on fitting models, such as a simple linear regression, to recurring decisions. The fitted models are approximations of how decision related data is combined to make decisions. Such modeling is a basic paradigm in behavioral decision making research and multi-attribute decision analysis. By extending this basic notion decision makers may (1) generate alternative models using various scenarios of past and future values of decision variables, and (2) directly manipulate terms in the models to assess changes in decision outcomes. These capabilities support both inductive and deductive aspects of learning. With recurring decisions, retakes can directly support the improvement of decision making strategies over time. Current DSS do not support this capability well, but they easily could. Future experiments are being planned to evaluate the benefit of such DSS capabilities.

## Conclusions

If a decision is semi-structured, decision strategies will most likely be imperfect. If the decision is recurring, there is the opportunity to perfect decision strategies over time. Appropriate DSS support for such situations could yield better recurrent decisions.

In the experiment reported here, decision makers making semi-structured recurrent decisions showed tracking artifacts. We also noted that Bowman's rules provided useful models of decision making strategies. These findings point to several DSS requirements for recurring decisions.

DSS to support semi-structured recurring decisions require the maintenance of a rich decision-making history and the manipulation and evaluation of alternate decision-making strategies. This support is possible with the current software technology; for example, templates which ride upon an integrated software system (with an historical database) could provide such support. Knowledge-based components may also offer support.

However, the case for such a system is still not fully made and thus this problem is deserving of future research.

## References

1. Bowman, E.J. "Consistency and Optimality in Managerial Decision Making," Management Science, Volume 9, Number 2, January 1963, pp. 310–322.

2. Carter, P.L., Remus, W.E. and Jenicke, L.O. "Production Scheduling Decision Rules in Changing and Nonlinear Environments," International Journal of Production Research, Volume 16, Number 6, November 1978, pp. 493–496.

3. Daft, R.L. and Lengel, R.H. "Information Richness," in Research in Organizational Behavior, B.M. Staw and L.L. Cummings (eds.), JAI Press, Greenwich, Connecticut, Volume 6, 1984, pp. 191–234.

4. Ebert, R.J. "Environmental Structure and Programmed Decision Effectiveness," Management Science, Volume 19, Number 4, December 1972, pp. 435–445.

5. Eilon, S. "Five Approaches to Aggregate Production Planning," A/IE Transactions, Volume 7, Number 2, June 1975, pp. 118–131.

6. Gordon, N.B. "Learning a Motor Task Under Varied Display Conditions," Journal of Experimental Psychology, Volume 57, Number 2, February 1959, pp. 65–73.

7. Hogarth, R.M. "Beyond Discrete Biases: Functional and Dysfunctional Aspects of Judgemental Heuristics," Psychological Bulletin, Volume 90, Number 2, September 1981, pp. 197–217.

8. Hogarth, R.M. and Makridakis, S. "Forecasting and Planning: An Evaluation," Management Science, Volume 27, Number 2, February 1981, pp. 115–138.

9. Holt, C.C., Modigliani, F. and Muth, J.F. "Derivation of a Linear Decision Rule for Production and Employment," Management Science, Volume 2, Number 2, January 1956, pp. 159–177.

10. Holt, C.C., Modigliani, F., Muth J.F. and Simon, H.A. Planning Production, Inventories, and Work Force, Prentice-Hall, Englewood Cliffs, New Jersey, 1960.

11. Kunreuther, H. "Extensions of Bowman's Theory of Managerial Decision Making," Management Science, Volume 15, Number 8, April 1969, pp. 431–439.

12. Moskowitz, H. "The Value of Information in Aggregate Production Planning—A Behavioral Experiment," AIE Transactions, Volume 4, Number 4, December 1972, pp. 290–297.

13. Moskowitz, H. and Miller, J.G. "Information Systems and Decision Systems for Production Planning," Management Science, Volume 22, Number 3, November 1975, pp. 359–371.

14. Noble, M., Fitts, P. and Marlowe E. "The Frequency Response of Skilled Subjects in a Pursuit Tracking Task," Journal of Experimental Psychology, Volume 49, Number 4, April 1955, pp. 249–256.

15. Obermayer, R., Swartz W. and Muckler, F. "Interaction of Information Displays with Control System Dynamics and Course Frequency in Continuous Tracking," Perceptual and Motor Skills, Volume 15, Number 1, August 1962, pp. 199–215.

16. Poulton, E.C. "Perceptual Anticipation and Reaction Time," British Journal of Psychology, Volume 43, Number 3, August 1952, pp. 222–229.

17. Poulton, E.C. Tracking Skill and Manual Control, Academic Press, New York, New York 1974.

18. Remus, W.E. "Bias and Variance in Bowman's Managerial Coefficient Theory," OMEGA, Volume 5, Number 3, June 1977, pp. 349–351.

19. Remus, W.E. "An Empirical Test of the Use of Graduate Students as Surrogates for Managers in Experiments on Business Decision Making," Journal of Business Research, Volume 14, Number 1, February 1986, pp. 19–25.

20. Remus, W.E., Carter, P.L. and Jenicke, L.O. "Regression Models of Decision Rules in Unstable Environments," Journal of Business Research, Volume 7, Number 2, April 1979, pp. 187–196.

21. Remus, W.E., Carter, P.L. and Jenicke, L.O. "Improving Decision Making Using Performance Feedback," Operations Research Letters, Volume 3, Number 2, June 1984, pp. 105–110.

22. Schroeder, R.G. and Benbasat, I. "An Experimental Evaluation of Uncertainty in the Environment Used by Decision Makers," Decision Sciences, Volume 6, Number 3, July 1975, pp. 556–567.

23. Searle, L.V. and Taylor, F.V. "Studies of

Tracking Behavior," Journal of Experimental Psychology, Volume 38, Number 5, October 1948, pp. 615–631.

24. Wainer, H. "Robust Statistics: A Survey and Some Prescriptions," Journal of Educational Statistics, Volume 1, Number 4, Winter 1976, pp. 285–312.

## About the Authors

William E. Remus is Professor of Decision Sciences at the University of Hawaii. During the last decade he has published over two dozen articles in journals such as Management Science, the International Journal of Management Science (OMEGA), and Journal of Business Research. He has been funded by the National Science Foundation for research into behavioral decision making and was a Fulbright scholar at the National University of Malaysia in 1980. His current areas of research include man-machine interfaces and applications of artificial intelligence.

Jeffrey E. Kottemann is Assistant Professor of Decision Sciences at the University of Hawaii. He received his Ph.D. in Management Information Systems and Quantitative Methods from the University of Arizona in 1984. He has published articles in the Journal of MIS and in Information Systems. His current research interests include information system development environments, construction of software to integrate data, document, and knowledge base management, and empirical research into the impacts of DSS on decision making behavior.

## Appendix

The cost structure (m = 2 for quadratic costs) is:

$$
\operatorname{Cost} _ {t} = \left(c _ {1} \left(P _ {t} - k W _ {t}\right) ^ {m} + c _ {2} \left(W _ {t} - W _ {t - 1}\right) ^ {m} + c _ {3} \left(I _ {t} - I ^ {*}\right) ^ {m}\right),
$$

where $c_{1}$ , $c_{2}$ , and $c_{3}$ , are the cost coefficients, $P_{t}$ is the production volume decision, $W_{t}$ is the number of workers employed, $l_{t}$ is the inventory, k is the number of units produced by each worker pet unit time, and $l^{*}$ is the optimal inventory level. The first term is the worker overtime/idletime cost, the second is the cost of a change in the size of the work force, and the third cost is associated with holding other than optimal amounts of inventory. This formulation also requires the inventory equation:

$$
(2) \mathrm{I} _ {\mathrm{t}} = \mathrm{I} _ {\mathrm{t-1}} + \mathrm{P} _ {\mathrm{t}} - \mathrm{S} _ {\mathrm{t}},
$$

where $S_{t}$ is the units sold this period. This equation calculates the current inventory position as the last period's inventory plus the current period's production minus the current sales.

Optimal linear decision rules can be found through differential calculus to minimize the cost. When the planning horizon is three periods, these optimal rules take the form:

$$
(3) W _ {t} = \beta_ {0 1} + \beta_ {1 1} W _ {t - 1} - \beta_ {2 1} I _ {t - 1} + \beta_ {3 1} E (S _ {t}) + \beta_ {4 1} E (S _ {t + 1}) + \beta_ {5 1} E (S _ {t + 2}),
$$

$$
P _ {t} = \beta_ {0 2} + \beta_ {1 2} W _ {t - 1} - \beta_ {2 2} I _ {t - 1} + \beta_ {3 2} E (S _ {t}) + \beta_ {4 2} E (S _ {t + 1}) + \beta_ {5 2} E (S _ {t + 2}),
$$

where $E(S_{t})$ is the expected sales in period t and the optimal betas are a function of $c_{1}$ , $c_{2}$ , $c_{3}$ , k, and $l^{*}$ in equation (1). Equations (3) and (4) are also the form of the Bowman models, where the betas are derived based upon a set of actual workforce and production decisions.

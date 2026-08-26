---
otero_id: 27120
otero_key: "QYV366FH"
title: "A Study of the Relationship Between Decision Model Naturalness and Performance"
authors: "Jeffrey E. Kottemann; William E. Remus"
year: "1989"
journal: "MIS Quarterly"
doi: "10.2307/248924"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
A Study of the Relationship between Decision Model Naturalness and Performance Author(s): Jeffrey E. Kottemann and William E. Remus  
Source: MIS Quarterly, Vol. 13, No. 2 (Jun., 1989), pp. 171-181  
Published by: Management Information Systems Research Center, University of Minnesota  
Stable URL: http://www.jstor.org/stable/248924

Accessed: 09/05/2014 19:50

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# A Study of the Relationship Between Decision Model Naturalness and Performance

By: Jeffrey E. Kottemann
Department of Computer Information Systems
School of Business Administration
University of Michigan
Ann Arbor, Michigan 48109

William E. Remus
Department of Decision Sciences
College of Business Administration
University of Hawaii
Honolulu, Hawaii 96822

## Abstract

Two objectives in the design of decision support systems (DSS) are to improve decision-making performance and to use DSS modeling forms that are natural, that is, to adopt modeling paradigms that are congruent with decision makers' conceptual models of decision tasks. By accomplishing the latter objective, a DSS should enjoy better conceptual ease of use and face validity. However, past research finds that DSS deemed natural for a task by decision makers, DSS designers, and researchers alike, often do not improve (or even hinder) performance; the inverse also occurs. Further, decision-making behavior seems quite sensitive to minor task differences. How reliably are decision model naturalness and performance related? This study utilizes the bootstrapping paradigm of psychological research to help answer this question. In assessing the naturalness and performance of differing model paradigms over time and across levels of task complexity, no single, systematic pattern emerges. But the results suggest that naturalness and performance are differentially sensitive to task contingencies. For example, while relative performance is stable over time only in the low complexity condition, relative naturalness is stable over time only in the intermediate complexity condition. One implication of the results is that conceptual ease of use may be an unreliable predictor of a DSS's effect on performance. DSS mechanisms may help decision makers better analyze model naturalness and performance.

Keywords: Decision models, decision support systems, decision making performance, conceptual ease of use

ACM Categories: H.0, H.4.2, H.4.m

## Introduction

Several authors (Jungermann, 1980; Pitz, 1983; Stabell, 1983) have argued that DSS designs must be congruent with the cognitive and behavioral strategies used by decision makers. In other words, DSS should appear “natural” to users. They suggest that such naturalness not only makes DSS easier to learn and use but also lessens the chances that DSS will impose inappropriate normative decision-making processes. Naturalness is defined as how well the modeling forms underlying DSS mirror actual decision-making strategies. Stabell (1983) terms this conceptual ease of use. Many researchers would argue that improving DSS naturalness is the best way to improve decision-making performance.

The opposing argument comes from research showing that decision makers do not perform as well as normative decision models. This poor performance can be traced to at least several dozen specific ways that decision makers depart from normative decision models (see Remus and Kottemann, 1986, or Hogarth and Makridakis, 1981, for reviews); collectively, these departures are referred to as “cognitive biases.” Many researchers would suggest building DSS using normative models to reduce cognitive biases and thereby improve decision making. By implication, these models would not be natural vis-a-vis the “biased” cognitive strategies of users.

While the relationship between naturalness and performance is critical to designing effective DSS, the literature gives us little guidance on the nature of the relationship. This led us to conduct the current basic research study to investigate the dynamics of naturalness and performance and their interrelationship.

DSSs embody modeling forms that may or may not mirror users' mental models. Take, for example, two multi-attribute utility (MAU) DSS for choosing among alternatives: one assumes a linear utility function, the second a non-linear utility function. Which DSS is best may or may not change over time and across environmental contexts. The notion of a "best" DSS is a function of how well it mirrors a decision maker's preference structure (naturalness) and the quality of the alternatives chosen (performance) with the aid of the DSS.

The experiment reported in this article addresses the above issues. Based on user models captured using regression analysis (see the following section), we infer possible relationships between DSS naturalness and decision performance. And we use the volatility of naturalness and performance over time and across levels of environmental complexity to infer the potential volatility of basic DSS design parameters. For example, in selecting between the two MAU DSSs (which embody different views of users' preference structures), how sensitive would one expect this choice to be over time and across environmental contexts?

The following section reviews the literature on decision process modeling and discusses the specific technique and classes of models that are central to this study. Each model represents a different view of the decision task and decision makers' potential mental models of it. We then describe the experiment, its results, and some implications for DSS design and assessment.

## Models of Decision Making

The analysis approach in this study required that we capture alternative models of subjects' decision-making strategies in order to assess their naturalness and performance over time and across environmental contexts. Einhorn, et al. (1979) and Todd and Benbasat (1987) provide critical reviews of the various techniques for capturing and modeling decision processes and strategies. Two fundamental approaches are the regression technique for capturing general decision strategies and verbal protocol analysis for deriving detailed cognitive process-models.

In research on human decision making, subjects are presented with a decision to make, given decision-making information (cues), and asked to make decisions. With the regression technique, subjects make many judgements and decisions, and the decision cues and their decisions are captured. These are then used as inputs to statistical regression to derive general decision rules, or strategies, used in subjects' decision making. In process tracing via protocols, subjects are asked to "think aloud" as they solve a problem or make a decision. Protocol analysis is then used to construct a "flow diagram" of their detailed cognitive processing.

As Einhorn, et al. (1979) point out, while process models derived via protocol analysis and regression models “seem quite different, the difference is not with respect to the underlying process uncovered but rather with each model’s different emphasis and descriptive level of detail” (p.465). They go on to suggest that regression models capture general decision strategies quite well and that such general strategies are only implicitly represented in process models derived via protocol analysis. In particular, important aspects such as “information [cue] combination and use of feedback are implicit; that is, these processes are going on between the boxes in the flow diagram” (p. 471). Because we desired to capture the general strategies people use, and since information combination is critical in the decision task, we utilize the regression technique for this study.

In the regression technique, one hypothesizes the general structure of decision-making rules; that is, the functional form of the regression equation. For example, the functional form hypothesized may be linear or non-linear. After generating such decision rules, one can then assess both how well the rules mirror actual decision making and how well decisions made using the rules perform. Thus, naturalness can be operationalized as the goodness with which the regressed model makes decisions like the decision maker; model performance can be viewed as how well the decision maker would perform if he or she used the model of a given functional form. As discussed below, both linear and nonlinear forms have shown themselves to be quite descriptive.

## Linear decision models

The derivation and analysis of heuristics inferred from actual decisions via regression has its roots in psychology (Goldberg, 1970; Hoffman, 1960; Meehl, 1954) and entered managerial decision-making literature through the work of Bowman (1963). Typically, these models reflect (1) decision-related information, or cues, selected to derive decisions; (2) the weighting of these cues; and (3) how the cues are combined. For example, the selection of an investment portfolio can be modeled as the weighting and combination of cues such as interest rates and currency exchange rates.

One widely used model is the linear model. Bowman (1963) uses this model in his managerial coefficient theory. His premise is that economic inefficiencies are not due to poor intuitive decision strategies but rather to the inconsistent use of these strategies; that is, inconsistency is the major source of poor performance. By modeling decision making, he argues that decision-making consistency, and thus, performance, would increase. As suggested by Bowman and others, linear models can be derived easily using ordinary least squares regression. This is the first model type used in this study.

Bowman (1963) views managers as good decision makers. Yet other researchers have documented numerous cognitive biases and imply that managers are poor decision makers. Hogarth (1981) tries to resolve this apparent conflict by suggesting that the biases are a result of researchers mischaracterizing the underlying decision model. Since biases are found relative to discrete optimal models, Hogarth argues that such biases might disappear if decision making were characterized by continuous models.

## Non-linear tracking models

Hogarth's observations led us to choose a continuous, non-linear model for the second modeling form used in the experiment. In many situations, the non-linear model is more appropriate than a discrete, linear model. For example, a money manager could be characterized as making a series of discrete, optimal decisions. This characterization is inappropriate, however; usually, a money manager tracks the environment continuously when making decisions. The money manager should be represented by a continuous decision model, namely, the tracking model. As another example, a production manager could be properly characterized as adjusting production levels to track sales demand.

When decision makers track, they normally show several tracking artifacts. With sine wave target tracks, trackers will normally lag the target. If the target movement is sinusoidal, this lag can be measured as the degrees of phase displacement. Trackers will also tend toward the mean of the track, particularly as the extremes of the sine waves are approached. Searle and Taylor (1948) term this phenomenon the range effect. It can be measured as the ratio of the tracking sine wave amplitude to the target sine wave amplitude. (See Remus and Kottemann, 1987, for a more extensive review of this literature.)

In an earlier study (Remus and Kottemann, 1987), we found both the range effect and lag in the production scheduling decision. This finding encouraged us to select the non-linear tracking model for this experiment. This allows us to measure the naturalness and performance of both linear and non-linear models; we also tested the volatility of these measures over time and across levels of environmental complexity. (See the following section.) While the linear model just discussed has shown itself to be quite robust, so has the non-linear tracking model and its relatives. One such relative is the anchor and adjustment (A&A) model. The A&A model has been shown to characterize decision making in a wide variety of decision tasks ranging from preferences to judgements made under uncertainty and ambiguity (Einhorn and Hogarth, 1985). A related modeling paradigm is Anderson's (1982) information integration theory, which finds non-linear (multiplicative) cue integration quite descriptive.

The two modeling forms selected for this experiment represent fundamentally different views of decision making. Further details of the models and their derivation are given immediately after the next section. Next, we discuss the experimental task and design.

## The Experimental Design

The experimental task reported here is based on the Holt, et al. (1960) model of the production scheduling problem. The cost function for this model has both linear and quadratic terms. The linear costs are a function of work-force size and production level. The quadratic costs are a function of changes in work-force level, over-time/idle time costs, and departures from the ideal level of inventory. Optimal rules can be found for the production scheduling problem by using differential calculus. The optimal rules for both work-force and production are a linear function of last period's work-force size, last period's inventory, and the forecasts for future periods. $^{1}$

In this experimental production scheduling task, the decision makers integrate, or use, five cues to make their decisions; once the task is learned, these five factors typically explain 80-90% of the variability in the decision making (Remus, 1984). Thus, it is a relatively complex experimental task that, with suitable training and practice, subjects can learn well. The production scheduling problem was selected because it is a managerially relevant problem; it has been calibrated with actual data from a paint plant (Holt, et al., 1956) and has an analytic optimal to use as a benchmark model. The existence of the benchmark model is beneficial because it provides a baseline with which to compare the performance of competing models; more importantly, we can assess whether the linear and non-linear models are more or less natural than the normative optimal model.

The 62 subjects were MBA candidates from a required course in operations research and computers. Participation in the experiment was a course requirement. The subjects had no prior experience in the scheduling exercise and had no knowledge of the optimization models for this decision. In this experimental setting, MBAs with no business experience and experienced managers have been shown to have no significant differences in decision-making behavior or performance (Remus, 1986). $^{2}$

The subjects made production and work-force decisions for 24 periods; a time-sharing computer monitored the decisions and collected the data. Subjects first received the sales forecasts for the next three periods. The choice of three-period forecasts was based on Moskowitz and Miller's (1975) research demonstrating its superiority over shorter forecast horizons in the production scheduling problem. Based on these forecasts, the inventory position, current work-force size and worker productivity, the subjects decided what production volume to schedule and how many workers they should employ. After they entered their decisions, the computer gave them an opportunity to check that they had correctly typed in their decisions. The subjects then received the actual sales and costs, the new inventory level, and the average cost so far. All cost and inventory calculations were done by the computer. This cycle was repeated for each of the 24 periods.

One objective of this study is to assess model naturalness and performance over time and, in particular, to differentiate between naturalness and performance during task learning and after task learning is complete. Prior studies have found that learning of the production scheduling decision occurs in the first 12 periods and that post-learning, or steady-state, decision behavior occurs in periods 13 to 24 (Remus, et al., 1979; 1984). In these prior studies, learning in the earlier periods is found to be a linear function of time. In later periods, subjects have been shown to approach optimal decisions and reduce erratic behavior. In the first twelve periods, subjects learn to make good decisions, and in the last 12 periods they continue to use the decision strategy they have developed. Therefore, in this study we have analyzed separately the learning and steady-state phases to assess the dynamics of naturalness and performance both during the learning phase and when learning is complete.

We also wished to assess the stability of both model naturalness and performance across environmental contexts. To operationalize this variable, the subjects were randomly assigned to two experimental treatments that differ in environmental complexity. Following the theory of Schroeder, et al. (1967), we operationalized environmental complexity as two levels of demand variability. The low variability level employed here has been used by Moskowitz and Miller (1975) and in earlier work (e.g., Remus, 1984; Remus, et al., 1979); hence, there is a comparability of results at this level of variability. The Moskowitz and Miller (1975) study and others have found subjects to approach optimal performance at this level of variability. This suggests that the low variability treatment corresponds to low environmental complexity.

The higher, yet intermediate, variability treatment is below that of Moskowitz and Miller's (1975) intermediate forecast variability treatment. Since Moskowitz and Miller find quality decision making at their intermediate treatment, the treatment in the current study should not force the simplistic decision making that the Schroeder, et al., theory asserts will happen with high levels of environmental complexity. We did not operationalize high levels of variability since, in this study, we were not interested in decision making in an overloaded condition.

For the experiment, the average demand was initially set at 2,500 units; the demand trend was an eight-period sinusoidal pattern peaking at 20% above the unadjusted demand. The demand pattern was then given intermediate or low variability by adjusting it respectively with uniformly distributed variation of $\pm400$ units and $\pm100$ units of demand. Each subject received a unique pattern of adjusted demand by having the uniformly distributed variation controlled by a random number generator seeded with the subject's social security number.

Despite that this task is framed in a production scheduling context, it is representative of a class of dynamic, recurring decisions. While not dismissing the differences that do exist, the basic orientation of the current task is shared by other domains involving repeated decision making under uncertainty. (See Hogarth, 1981, and Kleinmuntz, 1985, for similar arguments.) Examples include diagnosis/treatment iterations in medicine and maintaining investment portfolios over time.

## Model Derivation and Analysis Methods

We measured the decision makers' behavior in three ways. First, as the subjects made decisions, the decision cues and subjects' decisions were recorded. Actual costs were calculated using the paint plant's quadratic cost function (Holt, et al., 1956). Second, the individual decision makers were modeled with linear models. The independent variables used were the five cues discussed in the preceding section; the betas were estimated using least squares regression. The resulting decision models were then used to make the work-force and production decisions; the costs were calculated using the paint plant's quadratic cost function. The naturalness of the model is measured in terms of mean square error.

Third, a non-linear tracking model was estimated for each decision maker. The functional form for the tracking model mirrors the functional form used to generate the sinusoidal demand pattern. The tracking models were estimated using nonlinear regression. The models were then used to make the production scheduling decisions; the costs were again found using the quadratic cost function. The measure of naturalness was again mean square error. The analysis also yielded estimated of the phase displacement and range effect, which are given at the beginning of the next section.

## Results

Before beginning the comparative analysis of the models, it is appropriate to ask whether the tracking model characterizes the subjects' decision making and is an appropriate non-linear model for the production scheduling decision. This was tested by looking for the tracking artifacts. In both the low and intermediate complexity conditions, phase displacement and range effects occurred. (See Table 1.)

In the first 12 periods when the subjects were learning the task, their phase displacement was significantly larger in the intermediate variability environment than in the low variability environment. In the later steady-state decision-making periods 13-24, the significant difference had disappeared as the subjects stabilized on a phase displacement of about .53 radians. The range effect did not vary across conditions in either the learning or steady-state decision-making periods. However, in both conditions the range effect increased from the first 12 periods to the last 12 periods and approached the 20% demand variation built into the underlying model. Thus, tracking is occurring. These results are consistent with those reported in Poulton's (1974) review and replicate our earlier study (Remus and Kottemann, 1987). The results demonstrate that the tracking model is an appropriate choice for the non-linear model in this experiment.

We then analyzed model performance and naturalness. Specifically, we assessed (1) model naturalness over time and across levels of environmental complexity; (2) model performance over time and across levels of environmental complexity; and (3) the correspondence between naturalness and performance over time and across levels of environmental complexity. Naturalness and performance were considered stable if the rank ordering of the models did not change over time and across levels of environmental complexity, and unstable otherwise. The correspondence between naturalness and performance was considered propitious if the rank orderings of model naturalness and performance were the same. It was considered unpropitious if the rank orderings differed. In interpreting the results, (in)stability indicates potential volatility of basic DSS requirements; the (un)propitiousness of the relationships between naturalness and performance mirrors whether they are complementary or contradictory DSS design objects.

Table 1. Phase Displacement and Range Effect Tested in Two Levels of Environmental Variability Using the Mann-Whitney Test

<table><tr><td>Environmental Complexity</td><td>Number of Cases</td><td>Median</td><td>Value</td><td>Significance</td></tr><tr><td colspan="5">Phase displacement (in radians) during the learning periods</td></tr><tr><td>Low</td><td>31</td><td>.27</td><td rowspan="2">-1.99</td><td rowspan="2">.0463</td></tr><tr><td>Intermediate</td><td>31</td><td>.58</td></tr><tr><td colspan="5">Range effect during the learning periods</td></tr><tr><td>Low</td><td>31</td><td>.15</td><td rowspan="2">-.910</td><td rowspan="2">.3626</td></tr><tr><td>Intermediate</td><td>31</td><td>.14</td></tr><tr><td colspan="5">Phase displacement (in radians) during the steady-state periods</td></tr><tr><td>Low</td><td>31</td><td>.51</td><td rowspan="2">-.310</td><td rowspan="2">.7567</td></tr><tr><td>Intermediate</td><td>31</td><td>.56</td></tr><tr><td colspan="5">Range effect during the steady-state periods</td></tr><tr><td>Low</td><td>31</td><td>.16</td><td rowspan="2">-1.41</td><td rowspan="2">.1600</td></tr><tr><td>Intermediate</td><td>31</td><td>.17</td></tr></table>

Table 2 is a summary of the rank orderings of model performance and naturalness. Tables 3 through 6 provide the statistical details. As noted previously, actual decision making serves as a benchmark in assessing performance, and the optimal decision rule serves as a normative model benchmark in assessing naturalness.

A comparison of cells A with B, C with D, E with F, and G with H in Table 2 shows the stability of model performance and naturalness over time. Performance rankings were stable over time in low environmental complexity but relatively unstable in intermediate complexity. Naturalness rankings, on the other hand, were stable over time in intermediate complexity but unstable in low complexity. These results indicate that both model performance and naturalness are potentially sensitive to changes in the task environment. Further, a given task context may impact a model's performance but not its naturalness, and vice versa. Thus, the naturalness-and-performance relationship is not particularly propitious.

Table 2. A Summary of Model Performance and Naturalness Rankings

<table><tr><td colspan="3">Model Performance</td></tr><tr><td>Complexity</td><td>Learning Phase</td><td>Steady-State Phase</td></tr><tr><td></td><td>(A)</td><td>(B)</td></tr><tr><td>Low</td><td>L=T&gt;A</td><td>L=T&gt;A</td></tr><tr><td></td><td>(C)</td><td>(D)</td></tr><tr><td>Intermediate</td><td>L&gt;T=A</td><td>L&gt;A&gt;T</td></tr><tr><td colspan="3">Model Naturalness</td></tr><tr><td></td><td>(E)</td><td>(F)</td></tr><tr><td>Low</td><td>L&gt;T=O</td><td>L&gt;T&gt;O</td></tr><tr><td></td><td>(G)</td><td>(H)</td></tr><tr><td>Intermediate</td><td>L&gt;O&gt;T</td><td>L&gt;O&gt;T</td></tr></table>

Legend: L = Linear Model; T = Tracking Model; O = Optimal Model; A = Actual Decision Making

Table 3. The Cost Performance of the Models During the Learning Periods (1-12)\*

<table><tr><td colspan="6">In Low Complexity</td></tr><tr><td></td><td>Median</td><td>Optimal</td><td>Linear</td><td>Tracking</td><td>Actual</td></tr><tr><td>Optimal</td><td>21949</td><td>—</td><td>.0000</td><td>.0000</td><td>.0000</td></tr><tr><td>Linear</td><td>28983</td><td>.0000</td><td>—</td><td>.8141</td><td>.0007</td></tr><tr><td>Tracking</td><td>28086</td><td>.0000</td><td>.8141</td><td>—</td><td>.0006</td></tr><tr><td>Actual</td><td>30605</td><td>.0000</td><td>.0007</td><td>.0006</td><td>—</td></tr><tr><td colspan="6">In Intermediate Complexity</td></tr><tr><td>Optimal</td><td>23512</td><td>—</td><td>.0000</td><td>.0000</td><td>.0000</td></tr><tr><td>Linear</td><td>33817</td><td>.0000</td><td>—</td><td>.0000</td><td>.0000</td></tr><tr><td>Tracking</td><td>48096</td><td>.0000</td><td>.0000</td><td>—</td><td>.6104</td></tr><tr><td>Actual</td><td>50686</td><td>.0000</td><td>.0000</td><td>.6104</td><td>—</td></tr></table>

\* All tests used the Wilcoxin matched-pair signed-ranks procedure.

Table 4. The Cost Performance of the Models During the Steady-State Decision-Making Periods (13-24)\*

<table><tr><td colspan="6">In Low Complexity</td></tr><tr><td></td><td>Median</td><td>Optimal</td><td>Linear</td><td>Tracking</td><td>Actual</td></tr><tr><td>Optimal</td><td>25584</td><td>—</td><td>.0000</td><td>.0000</td><td>.0000</td></tr><tr><td>Linear</td><td>31749</td><td>.0000</td><td>—</td><td>.6242</td><td>.0311</td></tr><tr><td>Tracking</td><td>32383</td><td>.0000</td><td>.6242</td><td>—</td><td>.0456</td></tr><tr><td>Actual</td><td>35109</td><td>.0000</td><td>.0311</td><td>.0456</td><td>—</td></tr><tr><td colspan="6">In Intermediate Complexity</td></tr><tr><td>Optimal</td><td>29325</td><td>—</td><td>.0000</td><td>.0000</td><td>.0000</td></tr><tr><td>Linear</td><td>37240</td><td>.0000</td><td>—</td><td>.0000</td><td>.0021</td></tr><tr><td>Tracking</td><td>51024</td><td>.0000</td><td>.0000</td><td>—</td><td>.0018</td></tr><tr><td>Actual</td><td>40671</td><td>.0000</td><td>.0021</td><td>.0018</td><td>—</td></tr></table>

\* All tests used the Wilcoxin matched-pair signed-ranks procedure.

Table 5. Tests of Comparative Model Naturalness Using Mean-Squared Error During the Learning Periods (1-12)\*

<table><tr><td colspan="5">In Low Complexity</td></tr><tr><td></td><td>Median</td><td>Optimal</td><td>Linear</td><td>Tracking</td></tr><tr><td>Optimal</td><td>37003</td><td>—</td><td>.0000</td><td>.4447</td></tr><tr><td>Linear</td><td>14083</td><td>.0000</td><td>—</td><td>.0000</td></tr><tr><td>Tracking</td><td>26141</td><td>.4447</td><td>.0000</td><td>—</td></tr><tr><td colspan="5">In Intermediate Complexity</td></tr><tr><td>Optimal</td><td>57469</td><td>—</td><td>.0000</td><td>.0000</td></tr><tr><td>Linear</td><td>19961</td><td>.0000</td><td>—</td><td>.0000</td></tr><tr><td>Tracking</td><td>78476</td><td>.0000</td><td>.0000</td><td>—</td></tr></table>

\* All tests used the Wilcoxin matched-pair signed-ranks procedure.

Table 6. Tests of Comparative Model Fit (Naturalness) Using Mean-Squared Error During the Steady-State Decision-Making Periods (13-24)\*

<table><tr><td colspan="5">In Low Complexity</td></tr><tr><td></td><td>Median</td><td>Optimal</td><td>Linear</td><td>Tracking</td></tr><tr><td>Optimal</td><td>37723</td><td>—</td><td>.0000</td><td>.0068</td></tr><tr><td>Linear</td><td>14083</td><td>.0000</td><td>—</td><td>.0000</td></tr><tr><td>Tracking</td><td>26141</td><td>.0068</td><td>.0000</td><td>—</td></tr><tr><td colspan="5">In Intermediate Complexity</td></tr><tr><td>Optimal</td><td>43484</td><td>—</td><td>.0000</td><td>.0000</td></tr><tr><td>Linear</td><td>20938</td><td>.0000</td><td>—</td><td>.0000</td></tr><tr><td>Tracking</td><td>76648</td><td>.0000</td><td>.0000</td><td>—</td></tr></table>

\* All tests used the Wilcoxin matched-pair signed-ranks procedure.

A comparison of cells A with C, B with D, E with G, and F with H in Table 2 shows the stability of performance and naturalness across levels of environmental complexity. Here one can see directly the impact of task context. In all cases the rankings changed; the change was particularly pronounced in the steady-state decision-making phase. As subjects encountered higher levels of environmental complexity (cells G and H), their decision-making behavior was better characterized by the optimal model than by the tracking model. Not surprisingly, there is a similar trend vis-a-vis performance of the tracking model; it performed well in low complexity but poorly in higher complexity.

Comparing cells A with E, B with F, C with G, and D with H in Table 2 provides a direct look at the correspondence between performance and naturalness. While the performance and naturalness rankings of the linear and tracking models differed in low complexity, they remained constant in intermediate complexity. This result indicates that the performance and naturalness relationship may be more propitious in higher levels of environmental complexity than in low levels. This is encouraging, because the higher complexity level may be more indicative of real decision-making settings. Future research is necessary to determine the robustness of this finding.

## Implications

As discussed in the introduction, Stabell (1983) distinguishes between two aspects of DSS ease of use. Operational ease of use concerns the mechanics of DSS use, whereas conceptual ease of use concerns how well design paradigms underlying a DSS mirror people's decision processes. Conceptual ease of use is analogous to naturalness as operationalized in this study. We find that naturalness and performance are not consistently related. This parallels Elam and Mead (1986), who found that a DSS judged conceptually easier to use actually hampered creative planning. Thus, in both their and our research, naturalness/conceptual ease of use is an unreliable predictor of performance.

The performance and naturalness relationship uncovered in this research is not well-behaved: while naturalness was stable over time only in intermediate complexity, performance was stable only in low complexity. This suggests that user satisfaction measures that concern naturalness may at times be meaningful and at other times not. In particular, assessment of naturalness would be expected to vary over time and with changes in the task environment. So, if DSS users alter their assessments of a DSS over time, this may well be a function of learning or changes in the environment rather than fickleness.

The results of this study serve to emphasize the need for prototyping approaches to DSS development. Certainly the best learning-phase support may differ from that used in on-going decision support. This, in turn, suggests the importance of modifying the prototype when learning is complete. Moreover, where attributes of the decision environment change often, DSS development might best be viewed as a never-ending prototyping effort.

This study finds that the linear model of decision making is natural and results in better performance. Yet, DSSs still do not have mechanisms to capture decisions over time and then generate a model of the implicit decision strategies being employed. Such a capability could either serve to (partially) program decisions or help decision makers gain insights into their decision-making processes and strategies. To implement such capabilities, the DSS must archive and later analyze decision inputs, assumptions, processes, and outcomes over time. This suggests that the role of DSS should be extended from the idea of a “decision tool for the moment” to include that of a decision analyst and historian.

As discussed in Remus and Kottemann (1987), DSS could be designed to generate decision models of varying functional forms and allow decision makers to assess the models' naturalness. Also, the robustness of the models' performance could be assessed by allowing decision makers to simulate scenarios against the various models. Lastly, the system could allow users to directly manipulate the coefficients and functional forms (structure) of models to test the effects of changes in general decision strategies. It is important to note that such "what-if" analysis is distinct from that found in currently popular DSS, in which parameters of the decision problem are manipulated. The DSS capabilities outlined above would allow such "what-if" analysis on models of decision-making strategies as well.

Another potential capability pertains to adaptive DSS — systems that automatically adapt to users. In the present context, DSS could periodically derive models of varying functional forms and assess their naturalness and performance. In some cases, the structure of the most natural model remains stable but the coefficients change. In other cases, the structure of the model changes (e.g., a new variable is added or the functional form itself is changed). There are statistical tests that can be used to determine when a model should be recalibrated or when structural changes should be made to the model. Based on such an analysis, the DSS might suggest alternative decision strategies to be used or directly incorporated in the system. The implementation of such capabilities is similar in principle to model management systems that automatically update models of decision problems and environments (e.g., econometric models). However, the capabilities we outline pertain to models of decision-making strategies in addition to the decision problem itself.

## Conclusion

DSS embody paradigms of decision tasks and people's approaches to decision making. DSSs influence decision makers — no matter how implicitly — because they focus decision makers' attention through those paradigmatic lenses. Thus, it is not unexpected that experiments to date have produced disconcerting results in which DSSs have often failed to improve performance. (See Aldag and Power, 1986; Kottemann and Remus, 1987; and Sharda, et al., 1988 for reviews.)

Decision process research appears necessary if this trend is to be reversed. (See Benbasat, 1984; Pitz and Sachs, 1984; Stabell, 1983; Todd and Benbasat, 1987.) Such research can help establish general principles of DSS design. Two critical dimensions are DSS naturalness and performance improvement. These characteristics, when placed in proper balance, yield DSSs that are cognitively easy to use (natural), have face validity, and help improve decision-making effectiveness. However, the relationship between naturalness and performance may well be volatile. This study finds the relationship somewhat sensitive over time and to changes in environmental complexity.

Results in decision-making psychology lead Einhorn and Hogarth (1981) to suggest that decision processes are sensitive to seemingly minor changes in the task-related factors. Therefore, in many cases it might be appropriate to view DSS development as a never-ending process. Further, DSS modification might entail paradigmatic shifts rather than just enhancements to a current design. Also, it may be beneficial if DSSs support not only the modeling and analysis of decision problems but also the modeling and analysis of users' decision-making strategies.

## References

Aldag, R.J. and Power, D.J. "An Empirical Assessment of Computer-Assisted Decision Analysis," Decision Sciences (17:4), Fall 1986, pp. 572-588.

Anderson. N.H. Methods of Information Integration Theory, Academic Press, New York, NY, 1982.

Benbasat, I. "An Analysis of Research Methodologies," in The Information Systems Research Challenge, F.W. McFarlan (ed.), Harvard Business School Press, Boston, MA, 1984, pp. 47-85.

Bowman, E.J. "Consistency and Optimality in Managerial Decision Making," Management Science (9:2), January 1963, pp. 310-322.

Einhorn, H.J. and Hogarth, R. "Behavioral Decision Theory: Processes of Judgement and Choice," Annual Review of Psychology (32), 1981, pp. 53-88.

Einhorn, H.J. and Hogarth, R. "Ambiguity and Uncertainty in Probabilistic Inference," Psychological Review (92:4), October 1985, pp. 433-461.

Einhorn, H.J., Kleinmuntz, D.N. and Kleinmuntz, B. "Linear Regression and Process-Tracing Models of Judgement," Psychological Review (86:5), June 1979, pp. 465-485.

Elam, J. and Mead, M. "Can Software Influence Creativity?" working paper, Graduate School of Business, Harvard University, Boston, MA, 1986.

Goldberg, L.R. "Man Versus Model of Man: A Rationale Plus Some Evidence for a Method of Improving Clinical Inferences," Psychological Bulletin (73:6), June 1970, pp. 422-432.

Hoffman, P.J. "The Paramorphic Representation of Clinical Judgement," Psychological Bulletin (57:2), March 1960, pp. 116-131.

Hogarth, R.M. “Beyond Discrete Biases: Functional and Dysfunctional Aspects of Judgmental Heuristics,” Psychological Bulletin (90:2), September 1981, pp. 197-217.

Hogarth, R.M. and Makridakis, S. "Forecasting and Planning: An Evaluation," Management Science (27:2), February 1981, pp. 115-138.

Holt, C.C., Modigliani, F. and Muth, J.F. "Derivation of a Linear Decision Rule for Production and Employment," Management Science (2:2), January 1956, pp. 159-177.

Holt, C.C., Modigliani, F., Muth, J.F. and Simon, H.A. Planning-Production, Inventories, and Work Force, Prentice-Hall, Englewood Cliffs, NJ, 1960.

Jungermann, H. "Speculations about Decision-Theoretic Aids for Personal Decision Making," Acta Psychologica (45:1-3), August 1980, pp. 7-34.

Kleinmuntz, D.N. "Cognitive Heuristics and Feedback in a Dynamic Decision Environment," Management Science (31:6), June 1985, pp. 680-702.

Kottemann, J.E. and Remus, W.E. “Evidence and Principles of Functional and Dysfunctional DSS,” Omega (15:2), March 1987, pp. 135-143.

Meehl, P.E. Clinical Versus Statistical Prediction: A Theoretical Analysis and a Review of the Evidence, University of Minnesota Press, Minneapolis, MN, 1954.

Moskowitz, H. and Miller, J.G. "Information Systems and Decision Systems for Production Planning," Management Science (22:3), November 1975, pp. 359-371.

Pitz, G.F. "Human Engineering of Decision Aids," in Analyzing and Aiding Decision Processes, P. Humphreys, O. Svenson, and A. Vari (eds.), North-Holland, Amsterdam, Holland, 1983, pp. 205-221.

Pitz, G.F. and Sachs, N. "Judgement and Decision: Theory and Application," Annual Review of Psychology (35), 1984, pp. 139-163.

Poulton, E.C. Tracking Skill and Manual Control, Academic Press, New York, NY, 1974.

Remus, W.E. "An Empirical Investigation of the Impact of Graphical and Tabular Data Presentations on Decision Making," Management Science (30:5), May 1984, pp. 533-542.

Remus, W.E. "Graduate Students as Surrogates for Managers in Experiments on Business Decision Making," Journal of Business Research (14:1), February 1986, pp. 19-25.

Remus, W.E. and Kottemann, J.E. "Toward Intelligent Decision Support Systems: An Artificially Intelligent Statistician," MIS Quarterly (10:4), December 1986, pp. 403-418.

Remus, W.E. and Kottemann, J.E. "Semi-Structured Recurring Decisions: An Experimental Study of Decision Making Models and Some Suggestions for DSS," MIS Quarterly (11:2), June 1987, pp. 233-243.

Remus, W.E., Carter, P.L. and Jenicke, L.O. "Regression Models of Decision Rules in Unstable Environments," Journal of Business Research (7:2), April 1979, pp. 187-196.

Remus, W.E., Carter, P.L. and Jenicke, L.O. "Improving Decision Making Using Performance Feedback," Operations Research Letters (3:2), June 1984, pp. 105-110.

Schroeder, H.M., Driver, M.J. and Streufert, S. Human Information Processing, Holt, Rinehart, and Winston, New York, NY, 1967.

Searle, L.V. and Taylor, F.V. "Studies of Tracking Behavior," Journal of Experimental Psychology (38:1), October 1948, pp. 615-631.

Sharda, R., Barr, S.H. and McDonnell, J.C. "Decision Support System Effectiveness: A Review and an Empirical Test," Management Science (34:2), February 1988, pp. 139-159.

Stabell, C. "A Decision-Oriented Approach to Building DSS," in Building Decision Support Systems, J. Bennett (ed.), Addison-Wesley, Reading, MA, 1983.

Todd, P. and Benbasat, I. "Process Tracing Methods in Decision Support Systems Research: Exploring the Black Box," M/S Quarterly (11:4), December 1987, pp. 493-512.

## About the Authors

Jeffrey E. Kottemann is assistant professor of computer information systems at the School of Business Administration at the University of Michigan. He received his Ph.D. in management information systems from the University of Arizona and has published articles in Communications of the ACM, Information Systems, The International Journal of Management Science, Journal of MIS, and MIS Quarterly. His current areas of research include assessing the impacts of computerized decision aids on performance and decision makers' perceptions of their performance, and devising tools and techniques for development of large-scale information systems and modeling systems.

William E. Remus is a professor of decision sciences at the University of Hawaii. His research has appeared in Management Science, MIS Quarterly, Journal of Business Research, and The International Journal of Management Science (Omega). His current research interests include the impacts of DSS on human decision making, man-machine interfaces, and neural networks. His work has been funded by the National Science Foundation and he has been a Fulbright scholar at National University of Malaysia.

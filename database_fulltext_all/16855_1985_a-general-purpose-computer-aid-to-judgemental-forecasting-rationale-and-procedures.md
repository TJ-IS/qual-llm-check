---
otero_id: 16855
otero_key: "H4VR7HGD"
title: "A general purpose computer aid to judgemental forecasting: Rationale and procedures"
authors: "George Wright; Peter Ayton; Peter Whalley"
year: "1985"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(85)90173-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A General Purpose Computer Aid to Judgemental Forecasting: Rationale and Procedures

George WRIGHT

London Business School, London University, Sussex Place, Regent's Park, London NW1 4SA, England

Peter AYTON

Decision Analysis Group, Psychology Department City of London
Polytechnic, Old Castle Street, London, EI 7NT, England

Peter WHALLEY

Institute of Educational Technology, The Open University

Here we describe the rationale, procedures and use of a general purpose computer aid to judgemental forecasting. First, we review empirical studies of unaided judgemental forecasting and we identify suboptimalities in such probabilistic judgements. Next we present a description of 'Forecast', illustrating how the program's procedures aid judgemental forecasting by enabling the forecaster to produce coherent and consistent probabilities. The program aids three types of forecasting: first, of the time period or date when a specified event may happen, e.g. the value of UK £1.00 falling below US\$1.30; second, the possible outcomes of an event when these can be expressed in numerical terms as outcomes on a single continuous scale, e.g. company profits; third, the possible outcomes of an event when these can be expressed as discrete or discontinuous outcomes, e.g. the winner of a horse race.

## 1. Research on Human Judgement

Probability is a required numerical input to decision analysis and many other management technologies. Often actuarial or relative frequency-based data is unavailable or believed to be unreliable for direct input as a probability forecast. At other times the decision-maker may realise that unique change in the world will have a causal impact on the likelihood of an event to be forecast and so invalidate regression and time-series predictions based on averaging techniques. Economists have termed such discontinuous changes in time series, 'turning points'. In such cases the forecaster must rely on judgement. But how good are judgemental forecasts?

Human judgement has for been studied for many years by cognitive psychologists interested in decision making. For a review see Wright [19]. The general conclusion from this research has been that human judgement is suboptimal in many ways.

![](/api/attachments/H4VR7HGD/fulltext/images/4fc3ad2b8f35d0d14c6ed6147ccc8a3e3ab3d718059cab1cb49390ecd14055e6.jpg)  
the London Business School.

George Wright received his PhD from Brunel University in 1980. He has since published widely on the human aspects of decision-making and forecasting. His publications include Behavioural Decision Theory, Beverly Hills: Sage and Harmondsworth: Penguin, 1984, Behavioural Decision Making New York: Plenum, 1985, Investigative Design and Statistics. Harmondsworth: Penguin, 1986 and Judgemental Forecasting, Chichester: Wiley, in press. He is currently a visiting lecturer at school.

![](/api/attachments/H4VR7HGD/fulltext/images/b95a0dd2991811a9a1745b38d6cecd12e15f6b8c7d1dfdeca21ad11e392a2cf8.jpg)

![](/api/attachments/H4VR7HGD/fulltext/images/cd7e2af72594286a99d2b64128adc9bb3bbb1587a35c7557d5855de3a5b8c880.jpg)  
Peter Ayton conducted research in memory and language at University College London before joining the Decision Analysis Group. His current research activities include the development of statistical methods for individual difference analysis and the study of intuitive statistical concepts.  
Peter Whalley gained his PhD from the Open University in 1984. He is currently a research fellow in the Institute of Educational Technology at the Open University. His main area of research is concerned with monitoring the changing knowledge structures of students as they progress through educational courses.

Paul Slovic [16] has aptly summarised the research to date.

"This work has led to the sobering conclusion that, in the face of uncertainty, man may be an intellectual cripple, whose initiative judgements and decision violate many of the fundamental principles of optimal behaviour. These intellectual deficiencies underscore the need for decision-aiding techniques"

We will not review all the findings here but will concentrate on those that have special applicability to judgemental forecasting.

## 1.1. Additivity of probability forecasts

Subjective probabilities attached to sets of mutually exclusively and exhaustive events have been shown to sum to less than or more than one. For example, Phillips et al. [13], in a probability revision task, found four out of their five subjects assessed probabilities that were greater than unity. These four subjects increased their probability estimates for likely hypotheses but failed to decrease probabilities attached to unlikely hypotheses. In another probability revision study, Marks and Clarkson [12] found that 49 out of their 62 subjects gave probability estimates for complementary events that summed to more than unity. Conversely, a study by Alberoni [1], which asked subjects to estimate sampling distributions from binomial populations on the basis of small samples, found that in most cases subjective probabilities summed to less than unity.

In a study addressed directly to the descriptive relevance of the additivity axiom, Wright and Whalley [21] found that most of their untrained probability assessors followed the additivity axiom in simple two-outcome assessments. However, as the number of mutually exclusive and exhaustive events in a set was increased more subjects, and to a greater extent, became supra-additive in that assessed probabilities exceeded unity. With the number of mutually exclusive and exhaustive events in a set held constant more subjects were supra-additive, and supra-additive to a greater degree, in the assessment of probabilities for an event set containing additional individuating information about the likelihood of the occurrence of the constituents events. In Wright and Whalley's study the additional individuating background information was associated with the possible success of racehorses in a horse race; it consisted simply of a record of the horses' previous performances. It seems intuitively reasonable that most probabilistic predictions are based, in the main, on specific knowledge and not to any large extent on abstract notions such as additivity. A similar phenomenon was noted by Kahneman and Tversky [8] who coined the term 'representativeness' to refer to the dominance of individuating information in intuitive prediction. One of their tasks illustrating the phenomenon asked subjects individually to judge the likelihood than an individual, Tom W., is a graduate student in a particular field of specialisation. All the subjects had available was a brief description of the student in the form of a personality sketch and the prior probabilities as determined by the base-rates for the graduate programmes. Kahneman and Tversky [8] found that subjects had an apparent inability to integrate the low validity personality sketch with the base-rate information in a situation where the base-rate should have been predominant. Clearly, any computer aid should monitor judgemental forecasts for additivity and suggest ways in which incoherence can be resolved.

However, simple normalisation may not be a quick and easy solution to incoherence. Bartholemew in the discussion of a theoretical paper by Lindley, Tversky and Brown [11] outlined a major problem:

\*Suppose that I assess the probabilities of a set of mutually exclusive and exhaustive events to be

0.001, 0.250, 0.200, 0.100, 0.279 ...

It is then pointed out to me that probabilities sum to 0.830 and hence that the assessment is incoherent. If we use the method ... with the probability metric, we have to adjust the probabilities by adding 0.034 to each $[=(1/5)(1-0.830)]$ to give

0.035, 0.284, 0.234, 0.134, 0.313

The problem is with the first event, which I originally regarded as very unlikely, has had its probability increased by a factor of 35! Though still small it is no longer smaller than the others by two orders of magnitude'. [Bartholemew's comment is contained in Lindley et al. [11], p. 168].

It follows than any aid to judgemental forecasting should present several possible normalisations and also allow the forecaster to adjust his own assessments to achieve additivity.

## 1.2. Methods for the elicitation of probability forecasts

The two commonly-used direct methods for probability assessment are point estimates and odds estimates. Which is the best method for the elicitation of subjective probability? The empirical evidence is, unfortunately, contradictory. Some studies have shown consistency between probability estimates inferred from wagers and direct estimates (e.g., Beach and Phillips, [2]). However, other studies have shown that statistically naive subjects were inconsistent between assessment methods (e.g., Winkler, [18]). Generally, direct odd estimates, perhaps because they have no upper or lower limit, tend to be more extreme than direct probability estimates.

If probability estimates derived by different methods for the same event are inconsistent, which method should be taken as the true index of degree of belief?

One way to answer this question is to use the method of assessing subjective probability that is most consistent. In other words, there should be high agreement between the subjective probabilities, assessed at different times by a single assessor for the same event, given that the assessor's knowledge of the event is unchanged. Unfortunately, there has been relatively little research on this important problem. Goodman [5] reviewed the results of several studies using direct estimation methods. Test-retest correlations were all above 0.88 with the exception of one study using odds – here the reliability was 0.66. Goodman concluded that most of the subjects in all experiments were very consistent.

Clearly, any computer aid to judgemental forecasting should allow assessment of odds and point probabilities. Any inconsistency between the two assessment methods should be reported to the forecaster for resolution.

## 1.3. Incoherence of Time Period Forecasting

In a recent study, Wright and Ayton [20] asked respondents to give a probability forecast of a named event, such as the UK £1.00 falling to value of less than US1.30 at least once in (1) the month of November, 1983, (2) in the month of December, 1983, and (3) in both of the months in the two-month period. Their analysis revealed that subjects showed marked incoherence when their assessments were compared to the probability laws.

For example, the probability forecast of the event happening at least once in both months should be equal to the probability forecast of the event happening at least once in November multiplied by the probability forecast of the event happening at least once in December assuming that the event has occurred at least once in November.

Formally, by the probability laws:

$$
(P (\mathrm{A} \text { and } \mathrm{B}) = P (\mathrm{A}) P (\mathrm{B} / \mathrm{A})
$$

For the event happening at least once in either (but not both) of the months:

$$
\begin{array}{r l} P (\mathbf {A} \text {or} \mathbf {B}) & = P (\mathbf {A}) \mathrm{P} [ 1 - (\mathbf {B} \setminus \mathbf {A}) ] \\ & + P (1 - \mathbf {A}) P (\mathbf {B} \setminus \overline {{\mathbf {A}}}) \end{array}
$$

For the event happening in either or both of the months:

$$
\begin{array}{r l} P (\mathbf {A} \text { and   /   or } \mathbf {B}) & = P (\mathbf {A}) P (\mathbf {B} \setminus \mathbf {A}) \\ & + P (\mathbf {A}) P [ 1 - (\mathbf {B} \setminus \mathbf {A}) ] \\ & + P (1 - \mathbf {A}) P (\mathbf {B} \setminus \overline {{\mathbf {A}}}) \end{array}
$$

As you might expect, as far as human judgements are concerned the two halves of the equation seldom balance! Which forecasts are best? Intuitive 'secondary' forecasts of $P(\mathbf{A}$ and $\mathbf{B})$ , $P(\mathbf{A}$ or $\mathbf{B})$ and $P(\mathbf{A}$ and/or $\mathbf{B})$ or normative 'secondary' forecasts calculated on the basis of the less complex intuitive 'primary'. forecasts of $P(\mathbf{A})$ , $P(\mathbf{B})$ , $P(\mathbf{B} \setminus \mathbf{A})$ and $P(\mathbf{B} \setminus \overline{\mathbf{A}})$ ?

On the basis of previous research and theory on the psychology of judgement the normative 'secondary' forecast should be better than the intuitive "secondary" forecasts. Why should this be so?

The rationale for this assertion is similar to the rationale supporting the use of subjective expected utility theory (SEU), multi-attributed utility theory (MAUT) and Bayes' theorem as ways of improving decision making. These three theories are used to improve decision making not by giving the decision-maker any extra information but by making the best use of the information which the decision-maker already possesses. In the field of decision analysis (which is based on SEU) the rationale for the validity of the decision aid is that of divide and conquer. The decision-maker assesses primary inputs of subjective probabilities and utilities and SEU recomposes these to specify the 'optimal' decision. Similarly, in a MAUT analysis the decision-maker assesses subjective attribute weightings and scores each object under consideration on each attribute in turn. MAUT then recomposes these assessments to specify the object with the highest overall utility.

In applications of Bayes' theorem the decision-maker assesses subjective prior probabilities that hypotheses about the world are correct and also likelihoods of these hypotheses being correct, given updated information about the world. Bayes' theorem combines these subjective priors and likelihoods to produce optimal posterior opinions. For a more detailed review of SEU, MAUT and Bayes' theorem see Wright [19].

In summary, human decision-makers are able to supply simple intuitive inputs to decision theories which utilise these inputs to specifying more complex overall judgements or decisions.

Slovic [15] and Hogarth [7] have marshalled the evidence for suboptimality in human judgement in support of the notion that limited capacity in terms of memory, attention and reasoning capabilities leads the decision-maker to be sub-optimal. In other words, human decision-makers simply cannot do all the mathematics required for optimal holistic decisions whilst they are able to provide the simpler primary inputs required by the normative decision theories. Of course, these primary inputs may not be perfect but at least the mathematical manipulations can be performed reliably!

We would also invoke a similar rationale for the use of normative secondary forecasts instead of intuitive secondary forecasts. Our program elicits intuitive primary forecasts and intuitive secondary forecasts. Normative secondary forecasts are then calculated and presented to the forecaster together with his or her intuitive secondary forecasts. The next section of this paper presents some trial runs of the 'Forecast' program in use.

## 2. The Forecast Program

First, the program asks the forecaster for the type of forecast that is of interest. The forecast can be the time period, or date, when an event will happen, for example, the US dollar reaching parity with the pound sterling. Or it can be the possible outcomes of an event when these can be forecast in numerical terms on a single continuous scale, for example, company profits. Alternatively the forecast can be of discrete or discontinuous outcomes, for example, the winner of a horse-race.

## 2.1. Time period forecasting

For time period forecasting, the program elicits from the user the beginning and end of the time period of interest. We will call this time period, time period B. Next the program elicits a point probability estimate and an odds estimate for the event happening at least once in the forecast periods, for example, UK £1.00 falling to a value of less than \$1.30. These formally equivalent estimates are compared by the program and inconsistencies are reported to the user for resolution. This procedures gives P(B). Next, the program attempts to extend the time period of the forecast by a subsequent time interval consisting of the same number of days as the main time period of interest. We will call this time period, time period C. The program then elicits P(C). Following this the program investigates the possibility of the event occurring at least once in similar-length time period prior to the main time period of interest, if this time period does not extend into the past. We will can this time period, time period A. The program elicits P(A) and then divides in half the main time period of interest, period B, and elicits two further forecasts, P(D) and P(E).

At the next stage, the program investigates if the perceived likelihood of the event occurring in each of the periods is independent or dependent on whether or not the event occurred in the prior time period. It does this by asking if at least one occurrence of the event in the prior time period will affect the probability of the event happening in the subsequent time period. If the assessments are seen as conditional the program elicits the conditional probabilities, $P(\mathbf{B} \setminus \mathbf{A})$ , $P(\mathbf{B} \setminus \overline{\mathbf{A}})$ , $P(\mathbf{C} \setminus \mathbf{B})$ , $P(\mathbf{C} \setminus \overline{\mathbf{B}})$ , $P(\mathbf{E} \setminus \mathbf{D})$ , and $P(\mathbf{E} \setminus \overline{\mathbf{D}})$ .

The program next elicits forecasts of the event happening at least once in each of the paired time periods, i.e., $P(\mathbf{A}$ and B), $P(\mathbf{B}$ and C) and $P(\mathbf{D}$ and E). Subsequently the program elicits forecasts of the event happening at least once in one (but not both) of two time intervals, i.e. $P(\mathbf{A}$ or B), $P(\mathbf{B}$ or C) and $P(\mathbf{D}$ or E). Finally, the program elicits forecasts of the event happening at least once in either or both of two time intervals, i.e. $P(\mathbf{A}$ and/or B) and $P(\mathbf{B}$ and/or C).

```txt
FORECAST EVENT - UK £1.00 FALLS BELOW US $1.30
DATE 1-9-1984
TIME PERIOD B, 5-10-1984-8-11-1984
TIME PERIOD C, 8-11-1984-12-12-1984
TIME PERIOD A, 1-9-1984-5-10-1984
TIME PERIOD D, 5-10-1984-22-10-1984
TIME PERIOD E, 22-10-1984-8-11-1984
INTUITIVE PRIMARY FORECASTS
P(B) = 0.25
P(C) = 0.3
P(A) = 0.2
P(D) = 0.15
P(E) = 0.16
P(B\A) = 0.7
P(C\A) = 0.6
P(E\D) = 0.55
P(B\A) = 0.1
P(C\B) = 0.2
P(E\D) = 0.15
SECONDARY INTUITIVE AND NORMATIVE FORECASTS
P(A AND B) = 0.05
P(A)P(B\A) = 0.05
P(B AND C) = 0.06
P(B)P(C\E) = 0.15
P(D AND E) = 0.04
P(D)P(E\D) = 0.08
P(A or B) = 0.4
P(A)P[1-(B\A)] + P(1-A)P(B\A) = 0.14
P(B OR C) = 0.45
P(B)P[1-(C\B)] + P(1-B)P(C\B) = 0.25
P(D OR E) = 0.25
P(D)P[1-(E\D)] + P(1-D)P(E\D) = 0.19
P(B AND/OR C) = 0.4
P(B)P(C\B) + P(B)P[1-(C\B)] + P(1-B)P(C\B) = 0.4
P(A AND/OR B) = 0.35
P(A)P(B\A) + P(A)P[1-(B\A)] + P(1-A)P(B\A) = 0.28
P(B) = 0.25
P(D)P(E\D) + P(D)P[1-E\D)] + P(1-D)P(E\D) = 0.27
```  
Fig. 1. Example summary of feedback for time period forecasting

Figure 1 gives a summary of the feedback that the program 'gave to one user's forecast of the pound sterling's value against the dollar.

Notice the discrepancies between the user's secondary intuitive forecasts and the normative forecasts, the latter of which are based on the user's own normatively recomposed intuitive primary forecasts.

## 2.2. Continuous variable forecasting

After the main menu the program elicits the minimum and maximum values of the range of outcomes. The program also checks that the user's minima and maxima are as defined by asking for probability estimates for outcomes outside of this interval. Next, the program interactively subdivides this range into an acceptable number of divisions. Following this the program proceeds to elicit forecasts for the sub-ranges. Next the program reports assessed probabilities to the user and, if the assessments are not additive, presents two normalizations, N1 and N2. N1 simply allocates the computed amount of non-additivity equally among the sub-range forecasts. Normalization N2 shares any non-additivity proportionally according to the value of the original sub-range forecasts.

Figure 2 shows one example of feedback given to a user.

The program goes on the enquire if either of the normalizations are acceptable or if the user wishes to change his own forecasts to achieve additivity.

Finally the program reports cumulative forecasts to the user.

<table><tr><td>COMPANY PROFITS</td><td>PROB</td><td>N1</td><td>N2</td></tr><tr><td>-1000000-0</td><td>0.06</td><td>0.05</td><td>0.03</td></tr><tr><td>0-1000000</td><td>0.2</td><td>0.17</td><td>0.17</td></tr><tr><td>1000000-2000000</td><td>0.25</td><td>0.21</td><td>0.22</td></tr><tr><td>2000000-3000000</td><td>0.3</td><td>0.25</td><td>0.27</td></tr><tr><td>3000000-4000000</td><td>0.2</td><td>0.17</td><td>0.17</td></tr><tr><td>4000000-5000000</td><td>0.15</td><td>0.15</td><td>0.14</td></tr><tr><td>TOTAL</td><td>1.16</td><td></td><td></td></tr></table>

Fig. 2. Example Feedback for 'Continuous Variable Forecasting.

## 2.3. Discrete variable forecasting

After the main menu, the program asks for an event name and a list of all possible outcomes. The program adds a ‘catch-all’ outcome to the user's outcome listing and goes on to elicit assessment for the likelihood of the outcomes, initially using both point probabilities and odds as response modes. If any probability above 0.01 is placed in the ‘catch-all’ outcome the program prompts for further decomposition into specified possible outcomes.

As with the continuous forecasting option, the program next presents assessed probabilities and, if the assessments are not additive, presents normalizations N1 and N2 to the user for evaluation.

## 3. Discussion

Figure 3 sets out the essential logic of the procedures underlying 'Forecast'.

The program decomposes holistic forecasts and recomposes these by means of the normative probability laws. Recomposed coherent forecasts are then presented to the forecaster together with his or her holistic forecasts and, if there are discrepancies, the forecaster is given the opportunity to reflect on these discrepancies.

On reflection, the user may decide to accept the recomposed forecasts provided by the program, retain the original holistic forecasts or 'adjust' the holistic forecasts in the light of presented recompositions.

We do not impose guidance on how any inconsistencies or incoherence should be resolved although we have outlined earlier in this article our rationale that, for time period forecasting, normatively recomposed secondary assessments should be ‘better’ than the intuitive secondary assessments. This issue is best illustrated in a study by Tversky and Kahneman [17] who showed that even professional statisticians may produce incoherent probabilities. In their study, subjects rated the probability of events, some of which were inclusive of others. Thus the probability that next year there will be an earthquake in San Francisco, causing a dam burst resulting in a flood in which at least a thousand people are drowned must be less than the probability that there will, next year, be a flood somewhere in the USA in which at least a thousand people are drowned. However, when a less plausible specific scenario was described in this way, subject rated the logically less likely event as more likely than the more general event set of which it is a member.

In this case it is a debatable point as to whether the probability given to the general event should be increased to achieve coherence, whether the probability of the specific scenario should be decreased, or whether both probabilities should be adjusted. We would argue that in instances of this type the user should, as a minimum requirement, achieve coherence in his or her forecasts, for such forecasts must be at least as 'well-calibrated' as incoherent forecasts. Calibration is one measure of the validity of subjective probability assessments. For a person to be perfectly calibrated, assessed probability should equal percentage correct over a number of assessments of equal probability. For example, if you assign a probability of 0.7 to each of ten events occurring, seven of those events should occur. Similarly, all events that you assess as being certain to occur (1.0 probability assessments) should occur. For a review of this aspect of probability assessment see Lichtenstein, Fischhoff and Phillips [10]. Coherence can be thought as one measure of the reliability of probability forecasts. Logically, incoherent and inconsistent forecasts cannot be better calibrated, or more valid, than coherent consistent forecasts. In fact, we would expect people whose probability forecasts are incoherent to show poor forecasting performance.

![](/api/attachments/H4VR7HGD/fulltext/images/ef0cb273c154862c562af861426b443d894098a64b8a9dcce3104846fd779d19.jpg)  
Fig. 3. The Essential Logic of the 'Forecast' Program

To date, many individuals have interacted with the FORECAST program and we have been satisfied with the program's 'stand-alone' capability. Most of our judgemental forecasters have been surprised at their degree of inconsistency and incoherence but no single assessment mode, normalization or normative recomposition has been systematically accepted by our users. Our interpretation of this result is that our decision not to impose guidance on how any inconsistencies or incoherence should be resolved is justified.

One of the major uses of our program is when sensitivity analyses, considered at an early stage in the elicitation of probabilities for a decision tree, indicates that small changes in 'critical' probabilities have a major impact on which act is favoured by subjective expected utility theory. 'Forecast' is ideally suited to an in-depth examination of the consistency and coherence of subjective predictions and also has application in cross-impact analysis [3] and fault tree analysis (Fischhoff, Slovic and Lichtenstein, [6]).

Recent developments and practical implementations of the cross-impact technique reveal difficulties in resolving the inconsistencies in the subjective judgements of experts that can be aided by our program. Kirkwood and Pollock [9] utilised both simple and conditional probabilistic forecasts and chose to omit some of the judgements altogether in order to find a fit for judgements corrected with the probability axioms. For two out of three expert subject all the conditional probability estimates had to be discarded. As the conditional judgements reflect the underlying causal models of the experts, and as such may be seen as important inputs to the forecast, this is a serious problem. Furthermore, when judgemental data are omitted in this way the range of resulting forecasts output by the technique for the set of scenarios under consideration are less discriminatory. Thus, although this study listed forecast probabilities to five decimal places in some cases, one of the experts produced judgements which, when resolved by a best-fit technique, sorted the nineteen different scenarios into only five different categories of probability. One other of the two remaining experts produced only six different categories.

Perhaps the greatest potential for our program lies in its ability to train decision makers to produce consistent and coherent probabilities for input to decision-aiding technologies.

Our program also has use in IKBS (Intelligent Knowledge-Based Systems). Expert systems deal with uncertainty by incorporated redundancy within the knowledge base. This allows the system to reach correct conclusions by different 'routes'. The robustness of the knowledge base is generally considered to be more important that the 'fine tuning' effected by numbers measuring the uncertainty surrounding particular elements. However, expert systems dealing with heuristic knowledge must still somehow deal with uncertainty. Shortliffe [14] has proposed a system based on 'certainty factors' to indicate the confidence that can be placed on evidence which can be incorporated into inference rules. Other systems have been developed that are based on formal Bayesian principles, e.g. Duda et al. [4]. It may be a trivial point as to whether the human expert from whom information is being obtained makes use of certainty factors or probabilities. However, it is essential that the expert gives consistent, coherent and valid judgements about uncertainty.

## Acknowledgement

This research was funded by the British Economic and Social Research Council via project grant C0023207.

## References

[1] Alberoni, F., Contribution to the study of subjective probability, J. Gen. Psychol. 66 (1962) 241–264.

[2] Beach, L.R. and L.D. Phillips, Subjective probabilities inferred from estimates and bets, J. Exp. Psychol. 75 (1967) 354–359.

[3] Dalkey, N., An elementary cross-impact model, Technological Forecasting and Social Change 3 (1972) 341–351.

[4] Duda, R.O., P.E. Hart and J.G. Barret, Development of the Prospector Consultation System: Final Report, Technical Report, SRI International (1978).

[5] Goodman, B.C. Direct estimation procedures for eliciting judgement about uncertain events, Engineering Psychology Technical Report 011313-5-T, University of Michigan, Detroit MI (1973).

[6] Fischhoff, B., P. Slovic and S. Lichtenstein Fault trees: Sensitivity of estimated failure probabilities to problem representation, J. Expl. Psychol. Human Perception and Performance, 4 (1978) 330–344.

[7] Hogart, R.M., Cognitive processes and the assessment of subjective probability distributions, J. Amer. Stat. Assoc. 70 (1975) 271–294.

[8] Kahneman, D. and A. Tversky, Subjective probability: A judgement of representativeness, Cognitive Psychol. 3 (1972) 430–454.

[9] Kirkwood, C.W. and S.M. Pollack, Multiple attributed scenarios, bounded probabilities, and threats of nuclear threat, Futures (Dec. 1982) 545–553.

[10] Lichstenstein, S., B. Fischhoff and L.D. Phillips, Calibration of probabilities: The state of the art to 1980, in: D. Kahneman, P. Slovic and A. Tversky (eds.) Judgement under Uncertainty: Heuristics and Biases, Cambridge University Press, New York (1982).

[11] Lindley, D.V., A. Tversky and R.V. Brown, On the reconciliation of probability assessments, . Royal Stat. Soc. (1979) 142 146–180.

[12] Marks, D.F. and J.K. Clarkson, An explanation of conservatism in the book-bag-and-pokerchips situation, Acta Psychol. 36 (1972) 145–160.

[13] Phillips, L.D., W.L. Hays and W. Edwards Conservatism in complex probabilistic inferences, IEEE Transactions on Human Factors in Electronics 7 (1966) 7–18.

[14] Shortliffe, E.H., MYCIN: Computer-based medical consultations, Elsevier/North Holland, Amsterdam, New York (1976).

[15] Slovic, P., From Shakespeare to Simon: Speculations—and some evidence—about man's ability to process information, Research Monograph of the Oregon Research Institute 12 (1972) no. 12.

[16] Slovic, P. Towards understanding and improving decisions, in: E.A. Fleishman (ed.), Human performance and productivity (1986) in press.

[17] Tversky, A. and D. Kahneman, Extensional versus intuitive reasoning: The conjunction fallacy in probability judgement, Psychol. Rev. 90 (1983) 293–315.

[18] Winkler, R.L., The assessment of prior distributions in Bayesian analysis, J. Amer. Stat. Assoc. 62 (1967) 776–800.

[19] Wright, G., Behavioural decision theory, Penguin Harmondsworth/Sage, Beverly Hills CA (1984).

[20] Wright, G. and P. Ayton, Task influences or judgemental forecasting. Technical Report 84–9, Decision Analysis Group, City of London Polytechnic. (1984).

[21] Wright, G. and P. Whalley, The super-additivity of subjective probability, in: B.P. Stigum and F. Wenstop (eds.) Foundation of utility and risk theory with applications, Reidel, Dordrecht (1983).

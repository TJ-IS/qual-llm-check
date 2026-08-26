---
otero_id: 16995
otero_key: "A2EMMVKA"
title: "Expert systems and behavioral decision research"
authors: "Detlof von Winterfeldt"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90009-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Expert Systems and Behavioral Decision Research \*

Detlof von WINTERFELDT

Systems Center, Institute of Safety and Systems Management, University of Southern California, Los Angeles, CA 90089, USA and Gemeinschaft fuer Entscheidungs- und Risikoanalyse, Berlin, FRG

This paper reviews a part of the literature on behavioral decision research (policy capturing, psychophysics of numerical judgments and cognitive illusions) and examines implication for knowledge elicitation in expert systems. The literature on policy capturing demonstrates that simple and compact numerical models of expert knowledge can be built, but that experts are poor in verbalizing the knowledge expressed in them. The psychophysical literature indicates that numerical encoding of expert knowledge may be difficult and biased, but that it has definitive advantages over qualitative elicitation schemes: Numerical encoding forces hard thought, encourages precision, and allows to access a substantial computational apparatus. The literature on cognitive illusions suggests that the expert knowledge one effects may be an illusion. The review concludes by recommending to use numerical judgments and explicit models by experts where possible, and to decompose the elicitation task in order to avoid cognitive illusions.

Keywords: Expert Systems, Expert Judgment, Behavioral Decision Theory, Decision Analysis.

## 1. Introduction

Expert systems builders have, for the past five to ten years, attempted to express human knowledge in the form of computerized rules, frames, or networks (see, e.g., [5], [21], [28], [48]). Researchers of human judgment and decision making have for almost 40 years developed and tested numerical models of expert judges, decision makers and ordinary people (see, e.g., [4], [8], [9], [12], [35], [37], [40]). In addition, psychophysical research and recent studies on heuristics and biases in human judgment provide a rich body of literature about how expert judgment may go astray (see e.g., [23], [25], [36], [46]).

Having such closely related topics, one might expect an intense exchange of information and collaboration between expert system modelers and behavioral decision researchers. On the whole, such communication has not taken place. This paper is an attempt to provide a link between these two research areas, by summarizing the behavioral decision research that is relevant for knowledge elicitation in expert systems.

![](/api/attachments/A2EMMVKA/fulltext/images/999b62a53928c9228907818a98316b6ecbd81e259ceaec34bfcaacd823a63fc6.jpg)

Detlof von Winterfeldt was born on June 13, 1948 in Duisburg, West Germany. He received his B.S. and Masters degrees in psychology from the University of Hamburg in West Germany in 1968 and 1971 respectively. He continued his graduate work at the University of Michigan, where he received his PhD degree in mathematical psychology in 1976. From 1975 to 1978 Dr. von Winterfeldt was a Research Scholar at the International Institute for Applied

There are three topics in behavioral decision research that have implications for knowledge elicitation. The first is the topic of “models of man”. Decision researchers and expert systems modelers have developed models of people’s thought processes, but with a very different emphasis and quite distinct tools. Behavioral decision researchers usually work with numerical models, like additive linear models, expected utility models, or Bayesian inference models that provide a norm against which expert performance is measured. Expert systems modelers, in contrast, use structural representations like trees, frames, networks or production rules, and their main goal is to accurately describe thought processes of the expert judges.

The second topic is the psychophysics of knowledge elicitation within a given model or structure. An issue here is whether knowledge can or should be represented by number or by less rigorous qualitative descriptions like words. Behavioral decision researchers have typically favored numbers (probabilities and utilities) and they have developed a rich tradition, based on psychophysics, how to elicit these numbers. Expert systems modelers more commonly chose words or some semi-qualitative scheme for eliciting specific information from experts.

The third topic is cognitive illusions. In the last fifteen years cognitive psychologists have accumulated a substantial literature on biases in expert and non-expert judgments of probabilities and preferences, as well as in logic and reasoning. Knowledge of these biases has led to a growing literature on debiasing techniques. Both the literature on biases and debiasing should help the expert systems modeler to improve the elicitation of knowledge substantially.

The outline of this paper will closely follow these three topics. Section 2 describes behavioral research results on “models of man”. In the third section some basic psychophysical issues about the use of numbers for eliciting knowledge are discussed. The fourth section provides an overview of the literature on biases and heuristics. The final section summarizes the main message of behavioral decision research for building expert systems.

## 2. Models of Experts and Ordinary People

## The Policy Capturing Paradigm

Behavioral decision research known as “Policy Capturing” or “Multiple Cue Probability Learning (MCPL)”, attempted to capture expert judgment by matching linear combinations of cues (e.g., signs and symptoms of an illness) with an overall diagnostic or evaluative judgment of an expert judge (e.g., the cause of the illness). Excellent reviews of this research can be found in [20] and [39]; see also [16], [17]. This section summarizes the main paradigm and some experimental results of this research. A related literature, not covered in this brief summary, is process tracing (the elicitation of verbalizations of subjects’ thought processes) and functional measurement research on algebraic representations of cognitive rules [1].

Policy capturing is based on Egon Brunwik's probabilistic functionalism approach to psychology [19]. Although there are certain prescriptive components of policy capturing, its primary concern has been to describe people's use of cues and their integration of information in judgmental tasks. A prescriptive aspect to this research was introduced when several researchers found that statistical models of experts were able to outperform the experts themselves. This phenomenon has been called bootstrapping, since improving judgments by using one's own judgments is much like "pulling oneself up by the bootstraps."

In the basic paradigm of policy capturing, a subject (expert) is asked to make an overall judgment of objects which can be described by a set of numerical cues. For example, a member of a graduate student admission committee in a university may be asked to evaluate student applicants who are described on the cues “undergraduate grade point average”, “scores on a standardized test for graduate student applicants” and “quality of letters of recommendation”. Using regression analysis or analysis of variance procedures the cues are then related to the subject’s overall judgment and the numerical model (usually a linear weighted average) implied by the subject’s judgments is “captured”.

In some recent applications of this paradigm, "instant" experts were created by teaching nonexpert subjects the relationship between cues and an overall judgment and then later attempting to recover the taught relationship. For example, subjects became diamond appraisers by being taught the relationship between the “four C’s” (cut, clarity, color, and carat) and the overall value of diamonds. Usually the relationship is taught by outcome feedback: subjects are asked to make a guess at the overall judgment and then are fed back the model derived result. This “multiple cue probability learning” version of the policy capturing paradigm has proven useful to investigate the validity of alternative techniques for eliciting expert knowledge (see e.g., [24]).

![](/api/attachments/A2EMMVKA/fulltext/images/8c6de604b23bbbeaa4bfd4ef187ee675fdd609df3da6a4f811a84bde155bf1dd.jpg)  
Fig. 1. Brunswik's lens model.

Brunswik's "lens model" is a formal representation of the policy capturing paradigm (see Fig. 1). In the lens model, the relationships between cues $x_{i}$ and the criterion value $Y_{e}$ or subjects' responses $Y_{s}$ are thought to be weighted additive combinations. The goodness of fit index is the correlation between a linear model of the cues and $Y_{e}$ or $Y_{s}$ . Most applications of the lens model focus on the right side of the Fig. 1, i.e., the relationship between the cues and subject's responses $Y_{s}$ . The $r_{s,i}$ 's are the correlations between cues and overall judgments and thus indicate the cue use in the judgments. The left hand side can be built only when the real cue-criterion relationships are known. Hence, usually it is not possible to construct all the correlational indices such as validities $r_{e,i}$ or achievement $r_{a}$ .

Findings

The experimental literature of this paradigm is rich, covering graduate student admission, patient evaluations, job performance prediction, and stock performance ratings. The following summary of the experimental findings closely follows [20] and [39].

In all studies of the right hand side of the lens model, a weighted additive combination of cues correlated highly (.80 and above) with subject's responses $Y_{s}$ . Non-linear models provided only a very small improvement. Surprisingly, the models of the subjects systematically outperformed the subjects themselves. Moreover, simple unit weighting schemes that ignored subjects weighting strategy fared very well in many tasks [6], [11]. When there was a high intercorrelation among cues, unit weights even outperformed the model derived from experts' judgments. Thus, it appears that simple models can describe experts' judgments very well and sometimes do better than the expert themselves.

A consistent finding in these studies was a discrepancy between the weights derived from subjects' models and the weights that they claimed they used. In general, subjects' models placed a high weight on only a few cues, but when asked, subjects' gave a much more even weight distribution. Experts seemed to suffer from this bias even more than novices.

In the multiple cue probability learning paradigm, researchers found that subjects could learn simple rules fast and well. When the rules were non-linear, learning was slower and when the single cue-criterion relationship was non-monotone, little or no learning occurred. Positive relationships between cues $x_{i}$ and a criterion $Y_{e}$ were learned much faster than negative ones.

When appropriate models were elicited from subjects after training in cue use, subjects' models typically matched the taught models well. Elicitation methods (e.g., direction numerical weighting vs. regression modeling, etc.) had a substantial influence on the resulting weights. There exists further evidence that when subjects were asked to verbalize what they have learned, they were incapable of reproducing the simple rules, and instead produced a rather complicated qualitative protocol.

Slovic and Lichtenstein [39] summarize this research in the following way:

"First, it is evident that the judge responds in a highly predictable way to the information available to him. Furthermore, much of what we call ‘intuition’ can be explicated in a precise and quantitative manner. When this is done, the judge’s insight into his own cognitive processes is often found to be inaccurate. Second, we find that judges have a difficult time weighting and combining information, be it probabilistic or deterministic in nature. To reduce cognitive strain, they resort to simplifying strategies, many of which lead them to ignore or misuse relevant information." (p. 724)

Combined with the findings summarized above, this conclusion has clear implications for knowledge elicitation in expert systems: Yes, you can model experts with simple numerical models well. If you ask them directly about what they know, they may, however, give you distorted and biased answers.

## 3. Numbers or words?

Behavioral decision researchers like to quantify expert knowledge by numerical models (like the lens model) and to elicit information from experts in numerical form (like probabilities or utilities). While most textbooks on expert systems are not very specific about knowledge elicitation, the main elicitation mode appears to be verbal and qualitative, preferring classification and categorization over numerical models. This focus on qualitative expressions seems to be a result of a critical attitude towards numerical elicitation as well as of a focus on the structuring task in modeling.

## Numbers in the head?

A commonly heard criticism of numerical encoding of expert judgment is that “people just do not think that way”. There is no doubt that this criticism is correct at least in the following qualified sense: most laypeople unfamiliar with utilities and probabilities resist to express their values or opinions in numerical form. However, as one moves to technical experts, familiar with uncertainties, gamblers experienced with probabilities, or economists thinking in terms of trade-offs, one gains both appreciation of the concept and familiarity with the procedures of numerical expressions of knowledge.

Can subjects express their opinions and values in a meaningful numerical way? The evidence is mixed (see e.g., [23], [25], [46]). The overall finding of several decades of research on the issue is that probability and utility judgments are often systematically biased. Expertise, both in substance and in procedure helps, but does not alleviate the biases.

A second line of criticism, leveled mainly against the use of numerical elicitation of value judgments is based on the “labile values” argument, which is summarized in the following statement by Fischhoff, Slovic, and Lichtenstein ([15]):

"The recurrent theme of this paper is that subtle aspects of how problems are posed, how questions are phrased, and responses elicited have substantial impact on judgments that supposedly express people's true values. Furthermore, such lability in expressed preferences is unavoidable; questions must be posed in some manner and that manner may have a large effect on the responses elicited." (p. 118).

Judgments usually required in social judgment tasks, have a low test–retest reliability (e.g., .5 to .6). However, people are more likely to have clear values and opinions regarding stimuli that are familiar and experienced. von Winterfeldt and Edwards ([46]), reviewing utility elicitation tasks that met these requirements, indeed found much higher test–retest reliabilities (.8 to .9) than those reported in Fischhoff et al.

Poulton ([36]) reviewed the relevant literature and summarized five stimulus and response mode biases that affect judged sensory magnitudes; they apply to numerical judgments of opinions and value as well:

1. Centering bias:

2. Stimulus and response equalizing bias;

3. Contraction bias;

4. Stimulus spacing bias;

5. Logarithmic bias.

The centering bias, closely related to Helson's ([22]) adaptation level theory, refers to the fact that responses are usually adapted to the set of stimuli presented. If the set of stimuli changes, the respondent will only gradually change the definition of the responses. Stimulus and response equalizing biases are close relatives of the centering bias. Respondents are well distributed over the available response scale, independent of or spuriously affected by the range of stimuli. The contraction bias, also called the regression effect, is simply that large stimuli are underjudged and small stimuli are overjudged: responses are too close to the middle of the range. The stimulus spacing bias equalizes uneven differences among stimuli and maps them into equal response scale differences. Finally, the logarithmic bias refers to the fact that, at least for some subjective magnitudes, 1000 is twice, not 10 times as large as 100.

Both the psychophysical and the behavioral research literature therefore seem to indicate that numbers are not resting in the head, waiting to be elicited. Instead they may be labile expressions of vague thought, depending on stimulus contexts and response modes and affected by psychophysical biases.

## Words

The most familiar and important competitor of numerical expressions of uncertainty or preferences is verbal communication: "It seems unlikely that it will rain tomorrow" or "I rather strongly prefer steak over fish". The trouble with words is, of course, that they are vague. Sherman Kent the Grand Old Man of U.S. Intelligence analysis at one time, was so concerned with the fact that almost all intelligence analysis documents contained ambiguous verbal reports of uncertainty, that he proposed a set of rules for translating words into probabilities and vice versa ([27]). Barclay et al. [2], pursuing this idea, reported a study performed by NATO intelligence analysts, who assigned probabilities to statements like "it is highly likely that Iraq is developing the capability for producing nuclear bombs". Fig. 2 shows the results. Points are probability judgments associated with a particular phrase and the shaded areas are the ranges of uncertainties that Kent proposed for each phrase. Obviously, even within communities in which this kind of communication is both routine and important, its results are not precise.

![](/api/attachments/A2EMMVKA/fulltext/images/f88813c9c9bf1d99a08874eede42adeaf201e9c26fc83d6ef2f604c7807311c0.jpg)  
Fig. 2. Relation between probabilities and verbal expressions. The shaded areas indicate Kent's (1964) proposal for matching words and probabilities. (Reprinted with permission of Decisions and Designs, Inc., from Barclay, Brown, Kelly, Peterson, Phillips, & Selvidge, 1977.)

Why then are words so much more appealing than numbers, and why do many respected expert systems builders prefer qualitative characterizations over numerical ones? Exactly because they are vague, I believe. People incorrectly associate numbers with precision and seldom if ever is unaided intuition precise. There is comfort in vagueness.

A second reason for using words is that precision about uncertainty is not always necessary. If no decision is to be based on the assessment, communication about uncertainties and preferences simply reports a state of mind.

A third reason for preferring words is that they communicate more naturally and are less easily criticized. Ambiguity often makes management easier.

A fourth reason for preferring words over numbers is that numbers invite calculations, calculations invite data collections, and data collections invite revisions. In many situations this seems like more trouble than it is worth.

## In Defense of Numbers

The first defense of using numbers in modeling expertise or casual knowledge is that numbers force hard thought about what is to be measured. The comfortable vagueness of words often reflects a vagueness about the question that is to be answered rather than vagueness about the answer. It is easy to say that it is likely that it will rain in Los Angeles tomorrow, but when asked to make a point estimate of the median rainfall in L.A. tomorrow, several questions come up: What is the area to be considered? Where is the rain to be measured? What time frame should be considered? The numerical formulation clearly encourages more precise thinking about the nature of the phenomena under study.

Secondly, numerical expressions stretch people to the limits of their knowledge and force them to become precise as well as to acknowledge the degree of imprecision inherent in their estimates. For example, some time ago, I experienced a black-out and called the utility company to check how long it would take to restore the electricity. The operator, who obviously was somewhat harassed told me that she had “absolutely no idea.” I asked her if the lights would go on in less than a minute and she emphatically denied that. I also asked her whether it would take the utility company more than 24 hours to restore the power and she equally emphatically denied that. I pointed out to her that now that we had established the boundaries, we could probably narrow down the range a little. Unfortunately, she hung up on me.

The third reason for using numerical expressions of expert knowledge is the vast mathematical apparatus that numbers can access to calculate consistency checks and formal implications of the numerical inputs. These analyses often leads to insights which can be translated back into the qualitative language appropriate for addressing the problem at hand.

The fourth reason for using numbers is that they improve communication. While two experts may have a comfortable feeling of “agreeing” that an event is “likely” to occur, they may completely disagree about the meaning of “likely” and in fact cover up with words what may be a substantial controversy. Numbers can be argued about, probed, pushed around, etc. They communicate precisely what the communicator wants to express.

It should also be noted that some numbers are more easily elicited than others and some circumstances are more prone to lability and bias than others. First, ordinal institutions come more easily than cardinal (interval) ones. Second, some subjective continua (like noise) are more easily translated into ordinal intuitions that others (like aesthetics). Third, expertise, both substantive and in the elicitation task, help substantially (for a summary, see [46], chapter 10).

## 4. Cognitive Illusions

The third topic relevant to building expert systems is an area of research called “cognitive illusions” ([25], [46]). This research has produced a variety of findings about how experts and laypeoples’ judgments can be biased or distorted. It is important to expert systems builders because it indicates that expert systems may occasionally capture expert biases and illusions, rather than logic and reason.

The Research Paradigm for Finding Cognitive Illusions

Cognitive illusions are found in the following paradigm:

(1) A formal rule, known to the experimenter but not known or available to the subject is applied in formulating an intellectual task.

(2) Subjects are asked to solve the task intuitively (without tools).

(3) A systematic discrepancy between the formal rule and subjects' answers is found.

A simple example is to ask subjects to intuitively multiply the numbers $1 \times 2 \times 3 \times 4 \times 5 \times 6 \times 7 \times 8 = ?$ . The formal rule is the logic of multiplication in the decimal system, the answer is 40,320. Subjects consistently underestimate that number, more so when asked “multiply up from 1” than when asked to “multiply down from 8.”

There are at least four research topics within which cognitive illusions have been studied so far: probabilistic reasoning and inference, evaluations of decisions under uncertainty, logic and arithmetic, and intuitive physics.

## Cognitive Illusions in Probability and Inference

Conservatism. When naive subjects or experts are asked to revise their probabilities of a hypothesis based on new data, they do not revise their opinions nearly as much as Bayes' theorem, the formally appropriate algorithm, would suggest [9], [33]. For example, a subject is presented with two urns, one containing 70% red chips and 30% blue chips, the other containing 70% blue chips and 30% red chips. One urn is chosen at random and a sample of 10 chips is chosen with replacement, producing 6 red chips and 4 blue chips. Before sampling, the probability of the "predominantly red" urn was .5. After sampling it is .84, according to Bayes' Theorem and Binomial sampling. Yet, subjects are more likely to estimate a posterior probability of .6-.7.

Ignoring base rates. When making judgments about hypotheses or when making predictions about future events based on data, one should consider both the prior probability of the hypotheses or events and the diagnostic impact of the data. Instead, subjects tend to ignore prior probabilities and guide their judgments largely by the conditional probabilities of the data [44]. For example, subjects might be presented with a personality profile of a student that indicates that the student is shy, likes music, and enjoys housework. When asked for an estimate of the probability that this student is a female, subjects are likely to give about the same response when the university under consideration is a predominantly male engineering college or when it is a mixed liberal arts college.

Ignoring sample size. Distributions of statistics should become tighter as sample size increases. For example, the distribution of the mean height of men randomly sampled from a population with mean height 170 cm should become more and more narrow around 170 as the sample size increases. Contrary to this statistical logic, subjects tend to ignore sample size and instead assess sampling distributions that resemble the population distribution. The “Law of Large Numbers” produces converging distributions of statistics. Laypeople and even trained statisticians appear to adhere to a “Law of Small Numbers” which assumes that small samples looks like large ones [41].

Non-regressive prediction. When two variables are related with error, the prediction of one by the other should, under most reasonable assumptions, be regressed towards the mean of the predicted variable. For example, when predicting the height of a person from his weight, the uncertainty about the height-weight distribution should lead to an estimate that is somewhat closer to the average height of people in the population. Instead, subjects' predictions tend to be non-regressive [26]: they predict by matching the two variables deterministically. Subjects have, or imply by their judgments, an illusion of validity and reliability.

Overconfidence. Experts often make point estimates and then assign ranges to this estimate to express their uncertainty. For example, when predicting next year's inflation rate, a best guess (median) estimate may be 3.5%, but with substantial probability (e.g., .90) it could fall between 1% and 6%. In these types of tasks subjects often show overconfidence [29], [30], that is they provide ranges that are much to narrow. In the above task, the 1-6 range seems reasonable for a 90% credible interval, yet subjects would be more likely to give a range of 2.5% to 4.5%, and, as a consequence suffer from surprises.

Availability. Tversky and Kahneman [44] found that subjects' probability judgments are frequently influenced by the availability of instances and the ease of recollecting examples of the events of hypothesis under consideration. Events are considered more likely, when they are easily recalled or imagined. For example, subjects typically think that words beginning with an R are more likely to occur in the English language than words that have an R as a third letter. In fact, the reverse is true.

Anchoring and adjustment. When subjects are asked to give an estimate of a number, they frequently anchor on an initial guess, and after recognizing that this number is inappropriate, adjust - but often too little. For example, when asked for stating a certainty equivalent for a gamble with monetary outcomes, subjects may begin by thinking of the expected value, worry about the risk, and reduce the expected value to some lower number. Chances are that that number is still too high.

Hindsight. Most people exaggerate the probabilities of events after they know what actually occurred [13]. Had people been asked prior to and after the event what the probability of a space shuttle disaster might be, the probabilities would have been increased dramatically. This is a version of the common “I told you so” phenomenon.

Cognitive Illusions in Evaluation and Decision Making

The classical model of decision making under uncertainty is the subjectively expected utility (SEU) model (see [38], [45]). The following cognitive illusions are violations of the basic assumptions of the SEU model.

Certainty effects. When evaluating uncertain prospects subjects tend to overweight the outcomes that are certain relative to the ones that are uncertain. For example, when faced with a choice between a sure thing of \$3000 and a .50 chance at \$6000 or nothing, many subjects prefer the sure thing. However, if both options are offered only as the outcome of gamble with a .50 winning chance (i.e., a .50 chance at \$3,000 and a .25 chance at \$6,000), many subjects switch to the larger outcome gamble. In addition, there appears to be a shift in focus from probabilities to outcomes, when the probabilities become tiny. For example, when faced with the choice between winning \$6,000 with a probability of .45 or \$3,000 with a probability of .90, most people chose the second option, because it has a very high chance of winning. However, after all probabilities are divided by 450, (choice between a .001 chance at winning \$6,000 and a .002 chance at winning \$3,000) many subjects begin to prefer the first option. Clearly SEU would require consistency of the choices, assuming that the probabilities presented are the subjective probabilities of the subjects (see [42], [46]).

Reflection effects. When outcomes of gambles are reflected around the zero point, preferences tend to be reversed. For example, subjects might prefer a gain of \$500 for sure over a 50-50 gamble for winning \$1000 or nothing. When all outcomes are expressed as losses (a sure loss of \$500 s. a 50–50 chance at losing \$1000 or nothing), many subjects prefer the gamble. This preference pattern is, strictly speaking, not in violation of the SEU model, since it is consistent with that model to be risk averse in gains and risk seeking in losses.

A more powerful effect of this sort occurs, when the same gambles are expressed in terms of gains vs. losses. For example, assume that 1000 people are at risk from a particular disease. When subjects are asked whether they prefer a social program that will, with certainty, save 300 lives over one that saves 1000 lives with probability .30 vs. none with probability .70, many subjects prefer the sure life saving policy. A simple reformulation of that question asks whether they prefer a program that is certain to leave 700 people (of the ones at risk) dead vs. the gamble of saving all with probability of .30 and killing all with probability of .70. In this formation many subjects switch to the gamble, in clear violation of the SEU model [32].

Framing and isolation effects. Tversky and Kahnemann [42] also showed that the framing of options has a powerful effect on the preference of subjects. In many such instances, the way the experimenter “packages” an option leads the subject to “re-frame”, “un-package”, or isolate certain parts of the options in order to make the choice easier. In many cases sure things that are shared by several options are absorbed and ignored by subjects.

For example, when subjects are told that they first receive a gift of \$1000 and then can chose between \$500 for sure vs. a 50-50 chance at winning \$1000 vs. nothing, most prefer the sure thing. When they are told that they first receive \$2,000 and then have a choice between losing \$500 for sure or a 50-50 chance at losing \$1000, most subjects chose the gamble, even though, in terms of final outcomes the two packages are the same.

## Cognitive Illusions in Logic and Arithmetic

Cognitive illusions are not germaine to decision or inference problems. I already mentioned the systematic error of underestimating multiplications of a sequence of numbers. A related error is the failure to appreciate exponential growth functions [47]. When subjects are presented with the beginning numbers characterizing an exponential growth process, they severely under-estimate the rate of acceleration.

The conjunction fallacy [43] is an especially disturbing cognitive illusion. In a clear violation of probability logic subjects consider the likelihood of some compound events to be larger than that of a subset of these events. For example, subjects were asked to contemplate that a six sided die with four green faces and two red faces is rolled 20 times and that the sequence of red faces (R) and green faces (G) is recorded. They are then provided with the following three bets: You win \$25 if the 20 face sequence contains one of the following sub-sequences

(1) RGRRR

(2) GRGRRR

(3) GRRRRR

More than 60% of the subjects choose bet (2), and only 2% chose bet (3), presumably, because bet (2) appears more “random” or more “representative” than bets (1) or (3). However, it is obvious that sequences (2) and (3) are less likely than sequence (1), and, that sequence (2) contains sequence (1) thus cannot possibly be obtained unless one also obtains sequence (1).

It is only a minor consolation that when the logic of the situation was presented, 76% of the subjects (Stanford students) found it persuasive. One wonders about the other 24%!

## Cognitive Illusions in Physics

The most dramatic cognitive illusions occur in childhood, as Piaget and Inhelder [34] have demonstrated. An example is the violation of the simple law of conservation of volume. Children do not appreciate that a liquid, poured from one shaped glass into a different shaped glass should have the same volume.

![](/api/attachments/A2EMMVKA/fulltext/images/4f863939aec26ba69782d316206d8733e29268b6c90cd8f8d450d7c122ebc144.jpg)  
Fig. 3. Illustration of a physical illusion. After the string breaks, the ball moves in the direction indicated by G. Only 53% of subjects chose G as the correct answer. (Source: McCloskey, Caramazza, & Green, 1980. Copyright © 1980 by the American Association for the Advancement of Science.)

Adults are not so much smarter. McCloskey, Caramazza and Green [31] showed that only 50% of their subjects have a good intuitive appreciation of the laws of physics related to the velocity and lateral acceleration of an object spun around in a circle. Fig. 3 shows one of the problems presented to their subjects. Only 53% of the subjects got the answer right.

## 5. Conclusions

The literature of behavioral decision research has several practical implications for expert systems modeling.

Models of Experts and Models by Experts Should Be Combined

Perhaps the most interesting results of the policy capturing research is that numerical models of experts can be built, that they do a good job, and that experts cannot explicate the nature of these models well. It would be extremely interesting to compare a model elicited in the policy capturing mode with one elicited with expert systems tools. Limited comparisons exist (see e.g., [10]), and the MCPL paradigm is an obvious approach to test the differential validity. I suspect that both approaches would do rather well and the main difference lies in the economy of representation and the clarity of the numerical models of policy capturing.

One shortcoming of both expert systems building and policy capturing is that, at their best, these models are descriptive representations of the very essence of expert logic and expert judgment. They are models of the expert “without headaches” and they provide convenient, transportable, and presumably cheap expertise. At their worst, they may simply capture the simplifying heuristics and biases of experts and the inability of experts to communicate their own knowledge economically. Both approaches would consider high quality expert judgment as the “ceiling” of model performance.

Decision and operations researchers would like to do better and attempt to build models that improve on expert performance. Such “models by experts” usually do not resemble anything that is or might be going on in an expert’s head. It seems clear, for example, that Gaussian plume equations and complex Bayesian arithmetic are beyond the scope of expert intuition. At their best, these models by experts substantially outperform the experts themselves (see e.g., [18]). At their worst, they provide a limited and perhaps inappropriate description of the phenomena studied.

The issue is not whether to build models of experts or models by experts. Rather, the issue is how to allocate the task between those that are better modeled using the expert's natural way of thinking and those that should be modeled explicitly by experts. Models of experts are likely to perform better when the task is fairly unstructured and there are no formal mathematical equivalents of describing the phenomena under investigation. In well structured situations models by experts are likely to do a better job. In almost all cases a combination of both model building approaches offers the greatest opportunity for success.

## Numbers Are Hard to Get, But Useful

Psychophysics teaches us that it is difficult to elicit knowledge in numerical form, but we also know that nothing else is much easier, that words are ambiguous, and that numbers help substantially in processing and communicating knowledge. Some expert system builders, who worry about precise numbers, but find words too vague, attempt to find a “half-way house” in imprecise numerical expressions like fuzzy sets or confidence judgments. Many of these attempts are quite useful, but they lose the sharp edge of direct numerical estimates. As was pointed out earlier, the main advantage of precise numbers lies in sharpening the expert's understanding of the quantity that is to be measured and to push his or her limits of precision. Obtaining "precise numbers" is almost always worth while as a first cut approach, moving to uncertainty ranges after the limits of the expert's ability to express precise knowledge has been exhausted.

The Expert Knowledge You Elicit May Be An Illusion

Many of the cognitive illusions occur not only with laypeople, but also with experts like medical doctors, statisticians, psychologists. Are experts systems builders in danger to build models of cognitive illusions?

Some cognitive illusions undoubtedly enter into expert systems through heuristics, biases and distortion generated in the knowledge elicitation phase. But, on the whole, there is probably more validity in expert knowledge than illusion. After all, experts exist and prosper. To guard against the cognitive illusions that do occur expert systems builders should decompose expert judgment, structure it in numerical models like SEU or Bayesian inference models and combine it with other models of the phenomena that are under study.

## References

[1] Anderson, N. (1979). Algebraic rules in psychological measurement. American Scientist 67, 555–563.

[2] Barclay, S., Brown, R.V., Kelly, C.W., III, Peterson, C.R., Phillips, L.D., and Selvidge, J. (1977). Handbook for decision analysis. McClean, VA: Decisions and Designs.

[3] Bar-Hillel, M. (1973). On the subjective probability of compound events. Organizational Behavior and Human Performance 9, 396–406.

[4] Becker, G.M. and McClintock, G.C. (1967). Value: Behavioral decision theory. Annual Review of Psychology 18, 239–286.

[5] Buchanan, B.G. and Shortliffe, E.H. (1984). Rule-based expert systems. Reading, MA: Addison-Wesley.

[6] Dawes, R.M. and Corrigan, B. (1974). Linear models in decision making. Psychological Bulletin 81, 95–106.

[7] Edwards, W. (1954). The theory of decision making. Psychological Bulletin 41, 380–417.

[8] Edwards, W. (1961). Behavioral decision theory. Annual Review of Psychology 12, 473–498.

[9] Edwards, W. (1968). Conservatism in human information

processing. In B. Kleinmuntz (Ed.), Formal representation of human judgment (pp. 17–52). New York: Wiley.

[10] Einhorn, H. (1980). Learning from experience and suboptimal rules in decision making. In T. Wallsten (Ed.), Cognitive processes in choice and decision behavior (pp. 1–20). Hillsdale, NJ: Erlbaum.

[11] Einhorn, H. and Hogarth, R. (1975). Unit weighting schemes for decision making. Organizational Behavior and Human Performance 13, 171–192.

[12] Einhorn, H. and Hogarth, R. (1981). Behavioral decision theory: Processes of judgment and choice. Annual Review of Psychology 32, 53–88.

[13] Fischhoff, B. (1975). Hindsight ≠ foresight: the effect of outcome knowledge on judgment under uncertainty. Journal of Experimental Psychology: Human Perception and Performance 1, 288–299.

[14] Fischhoff, B. (1982). Debiasing. In D. Kahnemann, P. Slovic, and A. Tversky (Eds.), Judgments under uncertainty: Heuristics and biases (pp. 422–444). Cambridge University Press.

[15] Fischhoff, B., Slovic, P., and Lichtenstein, S. (1980). Knowing what you want: Measuring labile values. In T. Wallsten (Ed.), Cognitive processes in choice and decision behavior (pp. 64–85). Hillsdale, NJ: Erlbaum.

[16] Goldberg, L.R. (1968). Simple models or simple processes? Some research on clinical judgments. American Psychologists 23, 438–496.

[17] Goldberg, L.R. (1970). Man versus model of man: A rationale, plus some evidence, for a method of improving on clinical inferences. Psychological Bulletin 73, 422–432.

[18] Gustafson, D.H., Grest, J.H., Strauss, F.F., Erdman, H., and Laughren, T. (1977). A probabilistic system for identifying suicide attemptors. Computers and Biomedical Research 10, 83–109.

[19] Hammond, K.R. (1966). Probabilistic functionalism: Egon Brunswik's integration of history, and method of psychology. In K.R. Hammond (Ed.), The psychology of Egon Brunswik, 15–80.

[20] Hammond, K.R., Steward, T.R., Brehmer, B., and Steinmann, D.O. (1975). Social judgment theory. In M.F. Kaplan and S. Schwartz (Eds.), Human judgment and decision processes (pp. 271–312). New York: Academic Press.

[21] Hayes-Roth, F., Watermann, D.A., and Lenat, D.B. (1983). Building expert systems. Reading, MA: Addison-Wesley.

[22] Helson, H. (1964). Adaptation-level theory. New York: Harper & Row.

[23] Hogarth, R. (1980). Judgment and choice: The psychology of decisions. Chichester, England: Wiley.

[24] John, R., Edwards, W., and Collins, L. (in press). Learning and recovering importance weights in a multiattribute evaluation context. Organizational Behavioral and Human Performance.

[25] Kahneman, D., Slovic, P. and Tversky, A. (1982). Judgment under uncertainty: Heuristics and biases. Cambridge University Press.

[26] Kahneman, D. and Tversky, A. (1973). On the psychology of prediction. Psychology Review 80, 237–251.

[27] Kent, S. (1964). Words of estimated probability. Studies in intelligence 8, 49–65.

[28] Klahr, P. and Waterman, D.A. (1986). Expert Systems. Menlo Park, CA: Addison-Wesley.

[29] Lichtenstein, S., Fischhoff, B., and Phillips, L.D. (1977). Calibration of probabilities: The state of the art. In H. Jungermann and G. de Zeeuw (Eds.), Decision making and change in human affairs (pp. 275–324). Dordrecht, Holland: Reidel.

[30] Lichtenstein, S. Fischhoff, B., and Phillips, L.D. (1982). Calibration of probabilities: The state of the art to 1980. In D. Kahnemann, P. Slovic, and A. Tversky (Eds.), Judgment under uncertainty: Heuristics and biases (pp. 306–334). Cambridge University Press.

[31] McCloskey, M., Caramazza, A., and Green, B. (1980). Curvilinear motion in the absence of forces: Naive beliefs about the motion of objects. Science 210, 1139–1141.

[32] McNeil, B.J., Pauker, S., Soc, H.C., and Tversky, A. (1982). On the elicitation of preferences for alternative therapies. New England Journal of Medicine 36, 194–216.

[33] Phillips, L.D. and Edwards, W. (1966). Conservatism in a simple probability inference task. Journal of Experimental Psychology 72, 346–357.

[34] Piaget, J. and Inhelder, B. (1975). The origin of the idea of change in children. New York: Norton. (Original work published in 1951.)

[35] Pitz, G.F. and Sachs, N.J. (1984). Judgment and decision: Theory and application. Annual Review of Psychology 35, 139–163.

[36] Poulton, E.C. (1979). Models of biases in judging sensory magnitude. Psychological Bulletin 86, 777–803.

[37] Rapoport, A. and Wallsten, T.S. (1972). Individual decision behavior. Annual Review of Psychology 23, 131–176.

[38] Savage, L.J. 1954. The foundation of statistics. New York: Wiley.

[39] Slovic, P. and Lichtenstein, S. (1971). Comparison of Bayesian and regression approaches to the study of information processing in judgment. Organizational Behavior and Human Performance 6, 649–744.

[40] Slovic, P., Fischhoff, B., and Lichtenstein, S. (1977). Behavioral decision theory. Annual Review of Psychology 28, 1–39.

[41] Tversky, A. and Kahnemann, D. (1971). The belief in the law of small numbers. Psychological Bulletin 76, 105–110.

[42] Tversky, A. and Kahnemann, D. (1981). The framing of decisions and the psychology of choice. Science 211, 453–458.

[43] Tversky, A. and Kahnemann, D. (1983). Extensional versus intuitive reasoning: The conjunction fallacy in probability judgment. Psychological Review 90, 293–315.

[44] Tversky, A. and Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. Science 185, 1124-1131.

[45] von Neumann, J. and Morgenstern, O. (1947). Theory of games and economic behavior. Princeton, NJ: Princeton University Press.

[46] von Winterfeldt, D. and Edwards, W. (1986). Decision analysis and behavioral research. New York: Cambridge University Press.

[47] Wagenaar, W.A. and Sagaria, S.D. (1975). Misperception of exponential growth. Perception and Psychophysics 18, 416–422.

[48] Waterman, D.A. (1986). A guide to expert systems. Menlo Park, CA: Addison-Wesley.

---
otero_id: 24622
otero_key: "E7T7PT3M"
title: "A Comparison of Machine Learning with Human Judgment"
authors: "Michael W. Kattan; Dennis A. Adams; Michael S. Parks"
year: "1993"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1993.11517977"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Comparison of Machine Learning with Human Judgment

Michael W. Kattan, Dennis A. Adams & Michael S. Parks

To cite this article: Michael W. Kattan, Dennis A. Adams & Michael S. Parks (1993) A Comparison of Machine Learning with Human Judgment, Journal of Management Information Systems, 9:4, 37-57, DOI: 10.1080/07421222.1993.11517977

To link to this article: http://dx.doi.org/10.1080/07421222.1993.11517977

![](/api/attachments/E7T7PT3M/fulltext/images/7b7704beb28d8b0817037d2257ab6e76bb336a7008ea6405cf955d65feb0c2ff.jpg)

Published online: 16 Dec 2015.

![](/api/attachments/E7T7PT3M/fulltext/images/bc9da46d3c6bb8d1b0672265a3f15ee6909d00ccc5f3ca28171e2fc6fc236e62.jpg)

![](/api/attachments/E7T7PT3M/fulltext/images/bbbce0c20a5f19ee5b98a1464dcada84a4339dd6999845528cbe0c5af5f80915.jpg)

View related articles ↗

![](/api/attachments/E7T7PT3M/fulltext/images/1168ca94e95fa67b04b67a61412090e29153f6554602a78b510f5c1f4770e72a.jpg)

Citing articles: 1 View citing articles ↗

# A Comparison of Machine Learning with Human Judgment

MICHAEL W. KATTAN, DENNIS A. ADAMS, AND MICHAEL S. PARKS

MICHAEL W. KATTAN received his M.B.A. in 1989 from the University of Arkansas, and is a doctoral candidate in management information systems at the University of Houston. His primary research interests are in the areas of machine learning and expert systems. His articles have appeared in the Journal of Computer Information Systems, Computer Personnel, Proceedings of the Decision Sciences Institute, and Proceedings of the ACM Special Interest Group on Computer Personnel. Prior to entering the doctoral program, Mr. Kattan conducted research in the food science area, which he published in Cereal Chemistry and Journal of Food Science. He also has a paper forthcoming in Leukemia and Lymphoma.

DENNIS A. ADAMS received his Ph.D. in 1987 from Texas Tech University. He is an Assistant Professor of Management Information Systems in the College of Business Administration at the University of Houston. His research interests include management of information communication technologies, the uses of information technology for organizational competitive advantage, and the analysis and design of parallel systems. He has published articles in journals such as Data Base, MIS Quarterly, Information and Management, Information Systems Research, Journal of General Management, and Advances in Accounting Information Systems.

MICHAEL S. PARKS received his Ph.D. in 1973 from the University of Georgia. He is an Associate Professor of Management Information Systems at the University of Houston. His current research interests are natural intelligence and cybernetics. His work has been published in Cybernetica, Management Science, Kybernetes, and Operations Research Quarterly.

ABSTRACT: This paper compares human judgment with machine learning in a check processing context. An experiment was conducted comparing teams of subjects with three commercially available machine learning algorithms: recursive partitioning, ID3, and a back-propagation neural network. Also, the statistical technique discriminant analysis was compared. The subjects were allowed to induce rules from historical data under ideal human conditions, such as adequate time and opportunity to sort the data as desired. The results on multiple holdout samples indicate that human judgment, recursive partitioning, and the ID3 algorithm were equally accurate and more accurate than a back-propagation neural network. Subjects who chose mixed strategies of judgment were more accurate than those using noncompensatory strategies, while no

Acknowledgment: The authors thank Louis Glorfeld of the University of Arkansas and an anonymous reviewer for their helpful comments on earlier drafts of this paper.

subjects chose compensatory strategies. Large decision trees were not more accurate than smaller ones. There appeared to be a time threshold for humans to form accurate decision rules. Holdout sample accuracy tended to increase with primary sample accuracy. ID3 built larger trees than did either humans or recursive partitioning. The conclusion of this research is that the knowledge engineer faced with available historical data concerning a classification problem should not waste his time discerning rules, since he will only take longer and be no more accurate than a good learning tool. Knowledge of these tools will be the requisite skill for the knowledge engineer of the 1990s. Implications for IS design and further research are discussed.

KEY WORDS AND PHRASES: artificial neural networks, discriminant analysis, expert systems, ID3, machine learning, policy capture, recursive partitioning.

## 1. Introduction

EXPERT SYSTEMS, COMPUTER PROGRAMS THAT FUNCTION AS HUMAN EXPERTS in a narrow domain, have been a topic of interest of business research for over two decades. At the heart of any successful expert system are the decision rules that must be carefully extracted from the human expert and translated into machine-executable code. This process of policy capture, performed by the knowledge engineer, is often the most difficult step in the creation of an accurate expert system and is referred to as the "Feigenbaum bottleneck" [5]. In many cases, the rules used by the human expert are not readily discernible by observation or interview. Thus, the model-driven approach, whereby the knowledge engineer interviews the expert to elicit his knowledge, is often forgone in favor of the data-driven approach. This approach to acquisition (i.e., experts indicating their decisions concerning test cases in order to develop a sample), has shown considerable promise for several reasons:

1. Experts have difficulty explaining their decision processes [8, 32, 41, 42].

2. Experts are typically more confident demonstrating their decision-making process than they are explaining it [41].

3. The data-driven approach is less time-consuming, especially when historical data are available [7, 42].

4. Experts may be reluctant to reveal their rules directly [32].

In a decision setting, one of the roles of the expert is to separate the attributes that may be important in making a particular decision from those that are not. For the knowledge engineer, this identification process may be the most critical part of the model-development process. Failure to correctly identify which variables or attributes should be included may lead to disastrous performance. Once data concerning factors believed relevant to making a particular decision are available, the question of how to form production rules arises. Here, the knowledge engineer is faced with at least three choices: human judgment, machine learning, or a statistical technique. The purpose of this paper is to compare several commercially available forms of machine learning with human judgment and a statistical technique.

Such a comparison of approaches could be useful in many cases. Consider, for example, the expert system AMEX Authorization [19]. This expert system makes decisions of credit approval for merchants whose patrons use the American Express credit card. Through the use of historical data, potential purchases with the card are analyzed by statistical models first to determine whether they are consistent with previous purchase authorizations. Prior to the installation of AMEX Authorization, aberrations were sent to human authorizers who would gather additional information and make the final decision. With AMEX Authorization, the aberrations are preprocessed, and the final decision is often made without human intervention. The rules for AMEX Authorization were created by interviewing the authorizers, which was a time-consuming process. Given the availability of historical data, a machine learning approach might have been much quicker, and might have proved more accurate than the statistical model. Without some comparative studies, the AMEX experience may be considered suboptimal.

## 2. Background

THIS SECTION DESCRIBES THREE CHOICES OF RULE FORMATION that the knowledge engineer has: human judgment, commercially available forms of machine learning, and a commonly used statistical technique. The human process of multiple-cue probability learning is reviewed, and several machine learning techniques and the statistical technique discriminant analysis are described briefly and compared.

## 2.1. Human Judgment

The human information processing literature has investigated the techniques individuals use to make judgments. Payne [48] identified three types of strategies people use to detect relationships in data: compensatory, noncompensatory, and mixed. With compensatory strategies, people weight attributes on their perceived relationship with the outcome. For example, if an expert system is being designed to process overdraft checks, the expert (a bank officer) using a compensatory strategy would associate weights with particular attributes, such as check amount and account balance. The products of the weights and their attribute values are summed, and the sum is compared with some threshold in making the decision of whether to bounce or honor the check. Thus, the expert ends up using something similar to a regression model, where coefficients represent the relative contribution to the predicted value.

With noncompensatory strategies, attributes must satisfy certain levels in order to be associated with a particular outcome. In the check processing example, the check amount may have to be less than \$50 and the credit rating may have to be “good” for the check to clear. The representation of this type of strategy appears as a decision tree.

A mixed strategy has both compensatory and noncompensatory components. For example, the individual may first use a cutoff level of an attribute as in a noncompensatory strategy (build a partial decision tree), and then weight attributes (apply a regression model). By comparison, noncompensatory and mixed strategies differ from compensatory strategies by being hierarchical, in that rules are sequentially applied to segregate data, and a noncompensatory strategy is a special case of a mixed strategy where there is only one nonzero attribute weight per comparison. Therefore, compensatory strategies require that all attributes are measured on at least an interval scale, whereas mixed and noncompensatory strategies do not have this restriction. Previous research has suggested that individuals switch from compensatory to noncompensatory or mixed strategies when information load is high (number of attributes multiplied by number of levels per attribute) [48] and/or time is constrained [66].

The process humans use to aggregate information from multiple attributes (cues) that together have a probabilistic (i.e., imperfect) relationship with an outcome is termed multiple-cue probability learning (MCPL). It begins with the formation of an initial hypothesis, called the working hypothesis, which the subject uses to predict event outcomes. As the subject is confronted with new data, the working hypothesis may be modified as needed to incorporate the additional cases. Much empirical research has been conducted concerning factors that affect MCPL, and this research is reviewed in the next three subsections.

## 2.1.1. Factors Affecting Humans' Ability to Identify Relevant Cues

Some MCPL experiments have examined what affects our ability to identify relevant cues and/or distinguish relevant from nonrelevant cues. As a result, three factors have been detected: time allowed per trial, control over cue level and order, and expertise in the problem domain.

A number of studies in various domains have suggested that overall performance deteriorates and less information is utilized under time pressure [52]. In his experiment, Rothstein [52] employed two levels of time per instance, six seconds and unlimited, and three levels of task complexity to ascertain their effect on the number of cues individuals were able to discover. Rothstein's results replicated the previous findings [e.g., 66] that time-pressured individuals are forced to rely on fewer cues than nonpressured individuals.

Klayman [35] conducted a study in which some subjects were allowed to experiment by varying the levels of cues, and other subjects could only passively observe cue levels. Individuals discovered more cues when they were allowed to experiment. Hagafors and Brehmer [27] found that subjects with an ordered array of cue values outperformed those without such an array because they were able to effectively utilize more of the valid predictor cues. Thus, the authors concluded that control over the sequence of cue-criterion vectors (cue1, cue2, . . ., cueN, criterion) positively affected performance.

Typical MCPL research assumes that expertise in the area, based on previous judgments and context familiarity, determines which cues are to be available to subjects [60]. Though not MCPL experiments, recent research in cognitive psychology [e.g., 17] emphasizes the ability of experts to identify the most informative features of the task environment [35].

## 2.1.2. Factors Affecting Human Ability to Aggregate Information from Relevant Cues

Several experiments have been conducted to examine effects on our ability to combine information from relevant cues, revealing six factors: cue-criterion relation type, number of trials, meaningful versus abstract labels, time pressure, consistency, and memory of past events.

In his review, Brehmer [10] states that nonlinear cue-criterion relationships are learned much more slowly than linear relationships. Performance has been so poor as to suggest that nonlinear relationships are not learned at all [20, 29]. Learning of these nonlinear relationships is not affected by the number of cues involved [11].

Taylor [61] noted that previous research had shown performance improvement to occur over trials. Taylor [61] then conducted an experiment that examined, among other things, the phenomenon of performance improvement. Using three cues to predict a criterion, subjects improved over the first block of twenty trials, but showed no change over the second, third, and fourth blocks, suggesting an asymptotic relationship.

Labels can be classified as either meaningful (e.g., “GPA”) or abstract (e.g., “Cue 1”). Furthermore, meaningful labels can be manipulated to suggest congruent (e.g., high “GPA” associated with graduate admission) or incongruent (e.g., low “GPA” associated with graduate admission) relationships. Sniezek [57] found that subjects performed more accurately with congruent cue and criterion labels than with incongruent or abstract labels. Muchinsky and Dudycha [44] showed that subjects using abstract cues performed more accurately when the cues had positive rather than negative relationships with the criterion. In the typical MCPL experiment, subjects are shown a sequence of trials but are not allowed to see a past trial. In their experiments, Arkes and Harkness [4] show this as a detriment to performance. Hogarth [31] reviewed several of the biases of human memory of past events (e.g., vivid events unrealistically influencing perceived probability of occurrence) and how memory reliance contaminates our judgment of probabilities.

In his review of models of man (a.k.a. “bootstrapping”) versus man studies, Camerer [16] concludes that judges are often inconsistent in their judgments and are often less accurate than linear models of their judgments. In their experiment, Hagafors and Brehmer [28] found that having to justify one’s decisions to force consistency made the subject more accurate when the task predictability was low.

Experiments by Wallsten and Barton [63] compared subjects' performance under two levels of time pressure, nine and twenty seconds per trial. Even though all cues were involved in the relationship with the criterion, subjects under time pressure showed significantly less ability to combine cues optimally.

## 2.1.3. Other Previous Research in MCPL

Much of the research in MCPL has been on the factors affecting strategy (e.g., compensatory) selection [e.g., 6, 45, 54]. However, the link between strategy and accuracy has yet to be established. Paquette and Kida [46] found that a mandated strategy did not influence accuracy. Their subjects did not have past data, however, to test their models. Though experienced in the task domain, subjects had to rely on memory of past experiences.

Several other studies in MCPL have failed to suggest differences in MCPL accuracy. These include informing subjects that the task is probabilistic [12], two versus four cues [11], graphical presentation format [33], individual versus interactive group performance [3, 38], and pretraining of uncommon rules [2].

There appears to be very little evidence of individual differences in our MCPL ability. Sniezek et al. [58] found that mathematically/statistically educated subjects predicted more accurately. However, this effect was confounded with age and the completion of courses in other areas as well as mathematics and/or statistics. Furthermore, the explanation offered by the authors was that their mathematical education led to greater consistency of the subjects, which should have been controlled. Ruble and Cosier [53] found no evidence of a cognitive-style effect on decision accuracy.

Much of the MCPL research is experimental and compares outcome feedback with cognitive feedback where, in the latter, the subject is informed how his cue utilization compares with the true relationship, since the true relationship was designed by the researcher. The results of this portion of the research were omitted, since it is assumed the true relationship in a real-world setting is unknown.

## 2.2. Machine Learning and Discriminant Analysis

This section briefly describes several forms of machine learning and discriminant analysis. For brevity, only major differences are discussed, and the references contain detailed descriptions.

Machine learning (also called learning from examples and inductive learning [9, 23, 37]) refers to computerized techniques that imitate a class of input–output behaviors with the objective of generating reliable output from any input representing the domain of interest [30]. In this research, machine learning is applied to the classification problem, and therefore these machine learning techniques will attempt to uncover relationships between predictor variables and classes. The two most popular forms of machine learning are rule (or equivalently decision tree) induction and neural networks [24]. Rule induction techniques progressively build if–then rules or grow decision trees, whereas neural networks construct an energy surface [59]. Both techniques, however, result in a partitioned sample space containing regions where a particular class is predicted to occur.

While there are several rule induction techniques, the most popular is ID3 [21, 56, 64]. ID3, developed by Quinlan [49], is the basis for many machine learning programs [32, 50, 56]. Because of its popularity, it was chosen for comparison in this study. Another popular rule induction technique, also compared here, is recursive partitioning [13]. Though similar to ID3, recursive partitioning has the ability to implement compensatory, noncompensatory, and mixed strategies, whereas ID3 is restricted to a noncompensatory strategy since it lacks a linear-combination option. Another key difference between the two techniques is that recursive partitioning features cross-validation of its decision trees. The cross-validation process typically prunes decision trees by trimming spurious branches that do not classify well when faced with data not originally used to grow the branch. In a probabilistic context, where long-run perfect prediction is unexpected, recursive partitioning is less prone to overfitting sample data and grows smaller decision trees [43]. These two features of recursive partitioning, implementing compensatory and mixed strategies and not overfitting sample data, are more in line with human cognition and suggest an interesting comparison with human performance.

There are many neural network techniques, but back-propagation is the technique of choice for classification problems $[30]$ and the most popular overall $[37]$ . A back-propagation neural network is equivalent to nonlinear least-squares regression $[65]$ and thus most closely resembles a compensatory technique.

Discriminant analysis is equivalent to linear regression when two classes are used $[51]$ and thus employs a compensatory strategy. A Monte Carlo simulation by Glorfeld and Kattan $[26]$ indicated superior performance of recursive partitioning over discriminant analysis on data contaminated with outliers. Less rigorous studies $[15, 18]$ have suggested the accuracy of recursive partitioning to be equal to or greater than that of discriminant analysis in applied settings.

## 3. Previous Studies

A STUDY BY MESSIER AND HANSEN [41] COMPARED HUMAN JUDGMENT with machine learning and discriminant analysis. The decisions of the humans were from previous studies [1, 38], and Messier and Hansen added the ID3 algorithm and discriminant analysis results. However, the humans were not provided with past data to form their model, but rather had to rely on their own experiences to make their decisions. It is also unclear whether subjects had sufficient time to complete the task. Furthermore, comparisons should have been made on a holdout sample. The authors note this limitation in their findings.

Our primary purpose of this research is to compare the accuracy of human judgment with machine learning algorithms and discriminant analysis in a single, real-world context. This study extends the previous research by making comparisons on holdout data, using multiple groups to compute statistical significance, and not relying solely upon the experiences of the humans to form their rules. In this study, the human subjects will be provided randomly drawn sample data and apply their model to the remaining holdout data.

## 4. Hypotheses

THIS PAPER CONSIDERS THE PRESENCE OF INCONSISTENCIES in historical data as an important component of expert systems research. Assuming that people often consider the world probabilistic [31], it follows that often there will be sets of identical cue values with different events associated with them. This is likely due to the omission of an important cue in the prediction model. Given that inconsistencies will occur, it is important to understand how machine learning techniques will cope with these, and how they decide which events are inconsistent. Slight differences in continuous cues (e.g., age, income) of different events (e.g., loan default or no default) would be recognized as inconsistent by a back-propagating neural network. However, an exact match of cues is required for different events to be viewed as inconsistent by ID3 and recursive partitioning. This is an advantage of the neural network, since such a difference is likely an inconsistency, rather than a legitimate difference between events (e.g., defaulters versus nondefaulters).

To perform appropriately in a probabilistic environment, the machine learning algorithm must incorporate the fact that 100 percent prediction is often impossible. Though appropriately recognized, inconsistencies pose special problems in the weight-modification process of back-propagating neural networks. They will iteratively modify their connection weights, perhaps forever, when inconsistent events cannot be predicted correctly. The ID3 algorithm does not recognize that inconsistencies may exist. It continues to form a decision tree until all events are correctly predicted. Given a probabilistic environment, an underlying level of randomness based on cue knowledge and availability should determine what percentage of events should be considered incorrectly predicted. Thus, the ID3 algorithm produces too large a decision tree because it does not recognize that some of the splits in the fringes are spurious, and should not have been made. ID3 should somehow eliminate these spurious splits and accept some level of unpredictability. Recursive partitioning attempts to do this. By randomly holding out historical data and validating its decision tree with this holdout sample, recursive partitioning tries to identify and eliminate those spurious splits and accept these misclassifications as necessary in a probabilistic environment. Humans are expected to have this intuition to stop a decision tree when further classification is no longer possible without the use of spurious cue-event relationships.

## Hypothesis 1: ID3 will build larger trees than humans will.

In a given decision-making context, not all of the factors affecting MCPL can be controlled. As a starting point, it is interesting to compare the performance of human subjects under optimal conditions with that of machine learning. Optimal conditions would require the use of human subjects familiar with the decision context, with abundant time to sort a lengthy record of past events, who develop a consistent model of their decision. As subjects' working hypotheses are continually modified to incorporate additional data, they may eventually reach an asymptotic performance level, as measured by classification accuracy, and be faced with a few observations that don't fit the classification model or would require counterintuitive model modification (e.g., honoring the checks of individuals with bad credit ratings and bouncing checks of those with good ratings). Human subjects can recognize this problem when they understand the problem context, and are willing to accept this error in the sample data to make fewer errors in the population [22]. Machine learning techniques, obviously, lack intuition and are inclined to incorporate this sample information even though it would not apply to the general population. However, recursive partitioning overcomes this problem through cross-validation. Since humans, recursive partitioning, and ID3 are able to form hierarchical decision models (discussed in section 2.1), they should have an advantage over discriminant analysis and a neural network. An additional advantage for humans and recursive partitioning is that they are able to recognize a probabilistic environment. Therefore, the following hypotheses are suggested:

Hypothesis 2a: Human subjects will perform more accurately than ID3.

Hypothesis 2b: Human subjects will perform more accurately than discriminant analysis.

Hypothesis 2c: Human subjects will perform more accurately than a neural network.

Hypothesis 2d: Recursive partitioning will perform more accurately than ID3.

Hypothesis 2e: Recursive partitioning will perform more accurately than discriminant analysis.

Hypothesis 2f: Recursive partitioning will perform more accurately than a neural network.

Hypothesis 2g: ID3 will perform more accurately than discriminant analysis.

Hypothesis 2h: ID3 will perform more accurately than a neural network.

To control for lack of consistency, and thereby eliminate this portion of the error term, the subjects were required to record their model of decision making. The strategy each team uses will be gleaned from this record. Since noncompensatory and compensatory strategies are special cases of the mixed strategy, subjects that utilize a mixed strategy will be able to incorporate more information. Being able to accommodate all the information is expected to result in more accurate performance; however, this will increase the information load for the humans. Given adequate time to ease the information load and implement any strategy, it is of interest to note which strategies will be chosen most frequently and their accuracies.

Hypothesis 3: Human subjects who implement a mixed strategy will be more accurate than those who implement a compensatory or noncompensatory strategy.

When inconsistencies are present, and perfect prediction is not possible, it is expected that accurate decision trees will be of a particular size. That is, a tree with too few nodes may not discriminate sufficiently among the groups. But too large of a tree will contain spurious splits found in the sample that will not generalize in the population. The result is that there should be an optimal tree size, above or below which produces more error in the population $[13]$ . Therefore, it is expected that decision tree size will show a quadratic relationship with population classification accuracy, as estimated with a holdout sample.

Hypothesis 4: Tree size will show a quadratic relationship with population classification accuracy.

Since perfect prediction is not possible, the sample classification accuracy may not be a true indicator of population classification accuracy. Specifically, it is expected that a decision tree with a classification accuracy higher than the level of inconsistency in the sample data will overstate the true population classification accuracy, since the sample will have inconsistencies that cannot be correctly classified. Johnson and Wichern [34] discuss this overfitting of sample data and subsequent error rate which is optimistically biased. Conversely, a tree that is not fully developed will understate the true population classification accuracy. Therefore, the following hypothesis is proposed:

Hypothesis 5: Sample classification accuracy will have a quadratic relationship with population classification accuracy.

The experimental time allowed subjects affects both the strategy used $[66]$ and the amount of information considered $[62]$ . Assuming time will affect accuracy of judgment, time will be relaxed as a constraint in this study, but will be recorded. One would thus expect the subjects who spend more time modeling their decisions to form more complete models and make more accurate judgments. With noisy data, it is likely performance will be asymptotic with some value that is less than 100 percent.

Hypothesis 6: Time taken by the subjects will have an asymptotic relationship with population classification accuracy.

## 5. Methodology

TO ADDRESS THE HYPOTHESES, AN EXPERIMENT WAS CONDUCTED. The experiment involved emulating the decisions made by a bank officer when processing checking account overdrafts [47]. In this scenario, the loan officer had two alternatives: (1) honor the check, or (2) bounce the check. To make this decision, the loan officer had at least five items of information: (1) the amount of the check, (2) the account balance, (3) the type of account (regular or student), (4) whether the check was one of multiple overdrafts by the same party, and (5) a subjective credit rating of the payee based on his or her banking history (good, bad, or unknown). A sample of 340 useable observations was gathered as a single bank officer in a large bank was observed.

To evaluate the performance of human designers of expert systems vis-à-vis statistical and algorithmic methods, five teams of undergraduate students in a business expert systems course were chosen to participate. The subjects were allowed to form their own teams, with a maximum team size of four. The subjects were asked to form a decision model from a random sample of 240 observations. To control for the effect of inconsistency, the subjects were required to record functions or rules for applying their judgment. They were told that their goal was to minimize the number of misclassifications in the holdout sample of 100 observations, which did not contain the decision (bounce/honor), and were thus advised not to use a model that would not generalize to the population. The subjects were asked to record the time spent working on the model both as a team and individually and were required to complete the project within nine days. In an effort to encourage accurate reporting, the subjects were told that they would not be graded on their time spent developing the model. The subjects were also instructed that they were not allowed to get help from anyone outside their team. Furthermore, the teams were told not to use tools that build rules. $^{1}$ To further discourage teams from working together, each team received a random sample of the observations so that no two teams would have identical data sets, and the subjects were informed of this. The randomization also provided means for obtaining replicates for the analysis. Since both motivation and ability affect how well an individual detects relationships [39], motivation needed to be controlled in this study. Therefore, as an incentive, members of the team that correctly classified the most checks in the holdout sample would receive two popular music cassette tapes per team member. Also, the students were told that they may be graded on their performance.

The same data sets given to the teams were analyzed with SAS PROC DISCRIM [55] for the discriminant analysis procedure. Recursive partitioning was implemented in CART (v. 1.1) software (California Statistical Software, 1989). First Class (v. 2.56) was used to implement the ID3 algorithm (AICorp, Inc., 1990). And the neural network was trained with Brainmaker (v. 2.02) (California Scientific Software, 1989).

## 6. Results

Hypothesis 1: ID3 will build larger trees than humans will.

ANOVA WAS ALSO USED AS THE STATISTICAL PROCEDURE for testing hypothesis 1. The independent variable is method, and the dependent variable is the number of nodes in the decision trees. The results appear in Table 1.

With such a small sample, the errors were tested for departure from normality. The test was not significant (W = 0.88, p > 0.01). Since the F statistic was significant (F = 19.41, $p \leq 0.0002$ ), it was concluded that the mean decision tree sizes of the three methods were not equal. Fisher's protected least significant difference [40] was computed to detect the difference(s) among means. The results appear graphically in figure 1. ID3 builds significantly larger decision trees than does recursive partitioning or human subjects, which do not differ significantly at the five percent level. Hypothesis 1 was supported.

Hypothesis 2a: Human subjects will perform more accurately than ID3.

Hypothesis 2b: Human subjects will perform more accurately than discriminant analysis.

Hypothesis 2c: Human subjects will perform more accurately than a neural network.

Hypothesis 2d: Recursive partitioning will perform more accurately than ID3.

Hypothesis 2e: Recursive partitioning will perform more accurately than discriminant analysis.

Hypothesis 2f: Recursive partitioning will perform more accurately than a neural network.

Hypothesis 2g: ID3 will perform more accurately than discriminant analysis.

Table 1 Analysis of Variance for Difference among Decision Tree Nodes

<table><tr><td>Source</td><td>Degrees of freedom</td><td>Sum of squares</td><td>Mean square</td><td>F value</td><td>p&gt;F</td></tr><tr><td>Among</td><td>2</td><td>656.1</td><td>328.1</td><td>19.41</td><td>0.0002</td></tr><tr><td>Within</td><td>12</td><td>202.8</td><td>16.9</td><td></td><td></td></tr><tr><td>Total</td><td>14</td><td>858.9</td><td></td><td></td><td></td></tr></table>

![](/api/attachments/E7T7PT3M/fulltext/images/0ac1bcfdd0586c556e31345dc778d4eec94ec18f1235c1aa97657e86f4c32c16.jpg)  
Figure 1. Decision Tree Node Means with Fisher's Least Significant Difference

Hypothesis 2h: ID3 will perform more accurately than a neural network.

Table 2 shows the classification accuracies of the teams, machine learning algorithms, and discriminant analysis for both the primary and holdout data sets. Analysis of variance (ANOVA) was used as the statistical procedure for testing hypotheses 2a through 2h. The independent variable is method, and the dependent variable is holdout sample classification accuracy, which is the number of checks correctly classified as bounced or honored. Five teams were formed, so there were five data sets for each procedure. The Shapiro–Wilk statistic was significant (W = 0.82, p < 0.01) indicating that the normality assumption of parametric ANOVA could not be met. Therefore, Kruskal–Wallis (nonparametric) ANOVA was used. The $\chi^{2}$ statistic for method was significant ( $\chi^{2}=14.508, p\leq0.0058$ ), indicating that the median holdout sample classification accuracies were not equal. Multiple comparisons were performed to detect where the differences occurred. The results appear graphically in figure 2.

Table 2 Percent Correctly Classified for the Human Teams, Discriminant Analysis, and Machine Learning

<table><tr><td>Data set</td><td colspan="2">Human team</td><td colspan="2">Discriminant analysis</td><td colspan="2">ID3</td><td colspan="2">Neural network</td><td colspan="2">Recursive partitioning</td></tr><tr><td></td><td>P</td><td>H</td><td>P</td><td>H</td><td>P</td><td>H</td><td>P</td><td>H</td><td>P</td><td>H</td></tr><tr><td>1</td><td>95</td><td>95</td><td>84</td><td>84</td><td>100</td><td>95</td><td>78</td><td>73</td><td>95</td><td>95</td></tr><tr><td>2</td><td>96</td><td>96</td><td>79</td><td>75</td><td>100</td><td>90</td><td>65</td><td>80</td><td>97</td><td>91</td></tr><tr><td>3</td><td>51</td><td>70</td><td>75</td><td>78</td><td>100</td><td>90</td><td>80</td><td>65</td><td>98</td><td>93</td></tr><tr><td>4</td><td>99</td><td>98</td><td>83</td><td>83</td><td>100</td><td>90</td><td>74</td><td>74</td><td>97</td><td>92</td></tr><tr><td>5</td><td>98</td><td>98</td><td>84</td><td>75</td><td>100</td><td>96</td><td>84</td><td>74</td><td>93</td><td>92</td></tr></table>

$\mathbf{P} =$ primary sample; $\mathrm{H} =$ holdout sample.

The multiple comparisons indicate that the human teams and recursive partitioning were significantly more accurate than discriminant analysis and the neural network. ID3 was also significantly more accurate than the neural network. Though the means were in the order suggested by the hypotheses, significant results were found for hypotheses 2b, 2c, 2e, 2f, and 2h, but not for 2a, 2d, and 2g.

Hypothesis 3: Human subjects who implement a mixed strategy will be more accurate than those who implement a compensatory or noncompensatory strategy.

The notes that the subjects turned in with their predictions were used to examine hypothesis 3. The two teams that tied for first place with respect to decision accuracy both employed linear combinations of attributes in multilevel decision trees, suggesting that they used mixed strategies. The remaining teams all built multilevel decision trees with no linear combinations of predictor variables, suggesting the use of a noncompensatory strategy. Hypothesis 3 was supported.

Hypothesis 4: Tree size will show a quadratic relationship with holdout sample classification accuracy.

Lack-of-fit tests were used to investigate hypothesis 4. With the linear and quadratic terms in the model, lack of fit for the intercept term was tested. The test statistic was not significant ( $F = 0.276, p \geq 0.05$ ), and it was concluded that no higher-order terms fit the model. Thus, there appears to be no linear or quadratic relationship between number of nodes and decision tree accuracy across techniques, and hypothesis 4 was not supported. Within the individual techniques, none of the three zero-order Pearson correlation coefficients was significant at the 5 percent level. It was concluded that there was no linear relationship between number of nodes and accuracy within technique for any of the techniques. Figure 3 illustrates the data.

![](/api/attachments/E7T7PT3M/fulltext/images/c1d2480925e6673ee2163a80c96d095d9ecd494fc0da059136103868fcbb861c.jpg)  
Figure 2. Classification Medians with Significance Intervals based on Kruskal Wallis ANOVA

Hypothesis 5: Test sample classification accuracy will have a quadratic relationship with holdout sample classification accuracy.

Lack-of-fit tests were used for hypothesis 5. While lack-of-fit statistics for the intercept and linear terms were significant (F = 18.08, $p \leq 0.0004$ ; F = 18.41, $p \leq 0.0004$ , respectively), the tests for the quadratic and cubic terms also indicated significant lack of fit (F = 18.62, $p \leq 0.0003$ ; F = 18.65, $p \leq 0.0003$ , respectively). Lack of fit statistics for higher-level terms were not estimable. The data suggest at least a quartic relationship between holdout and test sample classification accuracies. The final fitted model had an adjusted $R^{2}$ of 0.86 and is overlaying the actual data in figure 4. Hypothesis 5 was not supported.

Hypothesis 6: Time taken by the subjects will have an asymptotic relationship with population classification accuracy.

The students' notes also provide data for hypothesis 6. The students were asked to log their time spent modeling their decisions both as a group and individually. This was converted to person-hours by multiplying group time by number of team members and adding the product to the sum of individual times. The results appear in Table 3. With only five teams, a conclusion can only be tentative. But it appears there is some threshold, above which additional time spent did not contribute to decision accuracy. This threshold occurred somewhere between 4 and 22 hours.

![](/api/attachments/E7T7PT3M/fulltext/images/015fb9e4cb4d45005df453feb14bd8939f588edcfcd6c81d7444227469061964.jpg)  
Figure 3. Plot of Decision Tree Size versus Holdout Sample Classification Accuracy

Table 3 Table of Person-hours and Holdout Sample Classification Accuracy

<table><tr><td>Hours spent modeling the decision</td><td>Percent correct in holdout sample</td></tr><tr><td>4</td><td>70</td></tr><tr><td>22</td><td>98</td></tr><tr><td>24</td><td>96</td></tr><tr><td>30</td><td>98</td></tr><tr><td>37</td><td>95</td></tr></table>

## 7. Discussion

WHEN EXAMINING THE ACCURACIES OF THE HUMAN TEAMS, machine learning, and discriminant analysis, one must consider the data in the study. There were decisions made by a bank officer that needed to be modeled in an expert system. A better approach might have been to model what should be done, rather than what the bank officer actually did. For example, the checks could have been followed to see if the bank officer always made the most profitable decision. Profitability could then have been modeled rather than the (probably suboptimal) bank officer's decisions. At any rate, it is clear that the loan officer was using an attribute not recorded in the analysis and/or was inconsistent in his decision making. In either case, all methods were presented with identical data sets.

![](/api/attachments/E7T7PT3M/fulltext/images/fdfd3650b80ef3e414d28170f2cdfd759b8f6024d43cc33aa709c0e24c03b76c.jpg)  
○ Human ▽ Discriminant Analysis △ ID3 ◇ Neural Network □ Recursive Partitioning  
Figure 4. Scatter Plot of Primary Sample versus Holdout Sample Classification Accuracy with Regression Line

Though there were no differences among the performance levels of the human, recursive partitioning, and ID3 methods, they all outperformed the neural network $p \leq 0.05$ . It is not surprising that the performance levels of discriminant analysis and the neural network did not differ, since back-propagation neural networks have been shown to be equivalent to an overspecified, nonlinear regression [65]. However, the external validity of the results of the neural network is questionable. The networks were not able to fully train on the data sets, and since the user cannot tell when the holdout classification accuracy is at a maximum, the stopping point is largely arbitrary. Furthermore, figure 4 does not suggest a clear relationship between primary and holdout sample classification accuracies for the neural network. The existence of such would at least guide the knowledge engineer so that he or she could tell when additional training was either not affecting or diminishing accuracy. In addition to the decision of when to stop training, the user has control over several parameters when constructing and training a neural network (e.g., number of hidden-layer neurons, training tolerance, etc.). In this experiment, the software package's default settings of these were used. Further research is needed to guide researchers and practitioners in this area. At present, it seems users must employ trial and error with the parameters on each particular data set. Given the relationship to regression, statistical theory should aid research.

The fact that, on average, the recursive partitioning and ID3 algorithms performed as well as the human teams may indicate that these particular forms of machine learning operate similarly to human cognition. An interesting area for further research is whether individuals or teams can sustain performance superior to those of machine learning. If this is possible, what are the characteristics of those individuals (e.g., good math skills, good at spatial relationships, etc.)? Research in MCPL thus far does not suggest such a sustainable performance advantage. Unless the expert uses an attribute that he or she cannot identify and/or describe, his or her value in a repetitive prediction task lies mainly in the identification of potential predictor attributes.

In a review of the literature on comparisons of human judgment with statistical forecasting methods, Bunn and Wright [14] point out that experts in their domain often base their judgments on statistical forecasts. However, the authors caution that a well-documented audit trail should explain what adjustments were made and why. When the forecast is in the form of a decision tree, it is likely that this adjustment would be easier to explain. This is posed in light of the results that subjects did not choose compensatory techniques. Instead of explaining only modifications of coefficients, the forecaster would indicate an additional split point in his or her decision tree.

It is not surprising that the top teams used mixed strategies, while the others used noncompensatory strategies. Mixed strategies are the most difficult, but they paid dividends in accuracy. Experimental research by Paquette and Kida [46] failed to show differences across strategies, but these strategies were randomly assigned. In our experiment, teams were allowed to choose their strategy. The combination of results from the two studies suggests that these high-level strategies may be appropriate only for certain individuals. More research is needed in this area.

No relationship was found between decision tree size and classification accuracy. Accurate trees were possible with just a few nodes. The emphasis seems to be on quality of the tree rather than size. A limitation of this research is the fairly limited range of tree size. A pattern might be present on a wider range, especially within method.

It appears that some threshold of time spent by humans forming rules was present. Below that threshold, somewhere between 4 and 22 hours, performance suffered. Additional improvements in accuracy did not appear above this threshold. Certainly much time is required to use a mixed strategy, but also may be demanded to form good noncompensatory rules. Again, the sample of five teams is quite small, so these results are tentative. Future research might examine this time threshold in achieving expertise.

Knight [36] offers an interpretation of the relationship between the accuracies of the primary and holdout data sets. At moderate levels of primary-sample accuracy (around 50–70 percent), the primary sample accuracy seems to understate the true error rate, as measured by the holdout sample. Here, the learning techniques are too general and have not capitalized on all the information present in the sample. At very high levels (near 100 percent), the opposite seems to occur, and the primary sample classification accuracy overstates the true classification rate. The learning techniques appear to have overtrained and memorized specific cases in the learning sample that do not generalize to the population. Looking at the neural network measures alone, they seem to go against this trend, although the sample size is only five.

As predicted, ID3 built larger trees than did the humans $p \leq 0.05$ . Recursive partitioning, with its pruning algorithm, did not. Extending the argument initiated previously in this section, perhaps recursive partitioning is nearer human cognition than is ID3. Recursive partitioning tries to avoid atheoretic splits in small samples via cross-validation, while ID3 does not. Pruning using the $\chi^{2}$ test has been suggested by Mingers [43]. Another possible explanation for the significantly larger ID3 trees is that binary subsets are not formed. If a categorical predictor variable is determined to have the lowest entropy, it is split on all categories. Though this effect is probably limited in this study, since only one categorical predictor variable had more than two levels (credit rating had three), a true comparison should employ dummy coding for ID3.

## 8. Conclusions

BUNN AND WRIGHT [14], IN THEIR COMPARISON OF STATISTICAL FORECASTING with human judgment, pointed out that “judgmental intervention on parameter estimation seems to have lost its early Bayesian promise.” Indeed humans, though they take orders of magnitude longer, do not outperform machine learning when adequate historical data are present. This is an important finding for practitioners in environments where many different classification problems exist and/or new data often arise. For these individuals, payback from the recursive partitioning or ID3 tools is inevitable. The same for neural networks was not evidenced; they iterated for several hours, were significantly less accurate, and perhaps most importantly, did not provide a very intuitively appealing representation of the problem. An experiment by Glorfeld [25] indicated that subjects generally preferred the problem representation of discriminant analysis and decision trees over that of a neural network. Considerable research needs to be done for these to be viable tools for the knowledge engineer in the classification problem.

With the addition of this research, it is clear that the knowledge engineer faced with a classification problem, as most expert systems problems are, should not waste time discerning the rules from historical data, since he or she will only take longer and be no more accurate than a good learning tool. Instead, the knowledge enginerr should concentrate on eliciting important attributes and making effective use of the learning tool. This includes proper coding of variables, appropriate options to select, and so on, which should be included in the expert systems course. Knowledge of these tools will be the requisite skill for the knowledge engineer of the 1990s.

## NOTE

1. These tools had not been covered in the course at the time of the experiment.

## REFERENCES

1. Abdel-Khalik, A.R., and El-Sheshai, K.M. Information choice and utilization in an experiment on default prediction. Journal of Accounting Research (Autumn 1980), 325–342.

2. Alm, H. Effects of pretraining on the construction of complex rules in probabilistic

inference tasks. Umea Psychological Reports, 162 (1982), 1–13.

3. Andersson, H., and Brehmer, B. Note on the policies acquired in interpersonal learning. Organizational Behavior and Human Performance, 24, 2 (October 1979), 195–201.

4. Arkes, H.R., and Harkness, A.R. Estimates of contingency between two dichotomous variables. Journal of Experimental Psychology: General, 112, 1 (1983), 117–135.

5. Barr, A., and Feigenbaum, E.A. The Handbook of Artificial Intelligence, vol. 2. London: Pittman Books, 1982.

6. Biehal, G., and Chakravarti, D. Information-presentation format and learning goals as determinants of consumers' memory retrieval and choice processes. Journal of Consumer Research, 8 (March 1982), 431–441.

7. Biggs, S.F.; Messier, W.F.; and Hansen, J.V. A descriptive analysis of computer audit specialists' decision-making behavior in advanced computer environments. Auditing: Journal of Practice and Theory (Spring 1987), 1–21.

8. Bobrow, D.C.; Mittal, S.; and Stefik, M.J. Expert systems: perils and promise. Communication of the ACM, 29 (1986), 880–894.

9. Braun, H., and Chandler, J.S. Predicting stock market behavior through rule induction: an application of the learning-from-example approach. Decision Sciences, 18 (1987), 415–429.

10. Brehmer, B. Effects of practice on utilization of nonlinear rules in inference tasks. Scandinavian Journal of Psychology, (1979), 141–149.

11. Brehmer, B. Note on subjects' hypotheses in multiple-cue probability learning. Organizational Behavior and Human Decision Processes, 40 (December 1987), 323–329.

12. Brehmer, B., and Kuylenstierna, J. Content and consistency in probabilistic inference tasks. Organizational Behavior and Human Performance, 26 (1980), 54–64.

13. Breiman, L.; Friedman, J.J.; Olshen, R.A.; and Stone, C.J. Classification and Regression Trees. Monterey, CA: Wadsworth, 1984.

14. Bunn, D., and Wright, G. Interaction of judgmental and statistical forecasting methods: issues and analysis. Management Science, 37 (1991), 501–518.

15. Callahan, J.D., and Sorensen, S.W. Rule induction for group decisions with statistical data—an example. Journal of the Operational Research Society, 42 (1991), 227–234.

16. Camerer, C. General conditions for the success of bootstrapping models. Organizational Behavior and Human Performance, 27 (1981), 411–422.

17. Chi, M.T.H.; Glaser, R.; and Rees, E. Expertise in problem solving. In R. Sterberg (ed.), Advances in Psychology of Human Intelligence. Hillsdale, NJ: Erlbaum, 1982, pp. 7–75.

18. Cronan, T.P., and Kattan, M.W. Student performance in the business computer information systems course: a recursive partitioning approach. Journal of Computer Information Systems, 31 (1991), 77–87.

19. Davis, D.B. Artificial intelligence goes to work. High Technology (April 1987), 16–27.

20. Deane, D.H.; Hammond, K.R.; and Summers, D.A. Acquisition and application of knowledge in complex inference tasks. Journal of Experimental Psychology (1972), 20–26.

21. Durkin, J. Induction via ID3. AI Expert (April 1992), 48–53.

22. Einhorn, H.J. Accepting error to make less error. Journal of Personality Assessment (1986), 387–395.

23. Fisher, D.H., and McKusick, K.B. An empirical comparison of ID3 and back-propagation. Proceedings of the International Joint Conference on Artificial Intelligence (1989), 788–793.

24. Ford, N. From information- to knowledge-management: the role of rule induction and neural net machine learning techniques in knowledge generation. Journal of Information Science (1989), 299–304.

25. Glorfeld, L. A comparison of three expert systems models for capturing a committee's decision policy. Proceedings of the Decision Sciences Institute (1990), 416–418.

26. Glorfeld, L., and Kattan, M.W. A comparison of the performance of three classification procedures when applied to contaminated data. Proceedings of the Decision Sciences Institute (1989), 1153–1155.

27. Hagafors, R., and Brehmer, B. Effects of information-presentation mode and task complexity on the learning of probabilistic inference tasks. Scandinavian Journal of Psychology, 21, 2 (1980), 109–113.

28. Hagafors, R., and Brehmer, B. Does having to justify one's judgments change the nature

of the judgment process? Organizational Behavior and Human Performance, 31, 2 (April 1983), 223–232.

29. Hammond, K.R., and Summers, D.A. Cognitive control. Psychological Review (1972), 58–72.

30. Hansen, J.V., McDonald, J.B., and Stice, J.D. Artificial intelligence and generalized qualitative-response models: an empirical test on two audit decision-making domains. Decision Sciences, 23 (1992), 708–723.

31. Hogarth, R.M. Judgment and Choice. Chichester, UK: John Wiley and Sons, 1987.

32. Ignizio, J.P. An Introduction to Expert Systems. New York: McGraw-Hill, 1991.

33. Jarvenpaa, S.L. The effect of task demands and graphical format on information processing strategies. Management Science, 35, 3 (March 1989), 285–303.

34. Johnson, R.A., and Wichern, D.W. Applied Multivariate Statistical Analysis, 2d ed. Englewood Cliffs, NJ: Prentice-Hall, 1988.

35. Klayman, J. Cue discovery in probabilistic environments: uncertainty and experimentation. Learning Memory and Cognition, 14, 2 (1988), 317–330.

36. Knight, K. Connectionist ideas and algorithms. Communications of the ACM (November 1990), 59–74.

37. Liang, T.P. A composite approach to inducing knowledge for expert systems design. Management Science, 38 (1992), 1–17.

38. Libby, R.; Trotman, K.T.; and Zimmer, I. Member variation, recognition of expertise, and group performance. Journal of Applied Psychology, 72, 1 (1987), 81–87.

39. MacCrimmon, K., and Taylor, R. Decision making and problem solving. In M. Allais and O. Hagen (eds.), Handbook of Industrial and Organizational Psychology. Chicago: Rand-McNally, 1976.

40. Mason, R.L.; Gunst, R.F.; and Hess, J.L. Statistical Design and Analysis of Experiments. New York: John Wiley and Sons, 1989.

41. Messier, W.F., and Hansen, J.V. Inducing rules for expert system development: an example using default and bankruptcy data. Management Science, 34 (1988), 1403–1415.

42. Michalski, R.S., and Chilausky, R.L. Learning by being told and learning from examples: an experimental comparison of the two methods of knowledge acquisition in the context of developing an expert system for soybean diagnosis. International Journal of Policy Analysis and Information Systems (1980), 125–161.

43. Mingers, J. An empirical comparison of pruning methods for decision tree induction. Machine Learning, 5 (1989), 227–243.

44. Muchinsky, P.M., and Dudycha, A.L. Human inference behavior in abstract and meaningful environments. Organizational Behavior and Human Performance, 13 (1975), 377–391.

45. Olshavsky, R.W. Task complexity and contingent processing in decision making: a replication and extension. Organizational Behavior and Human Performance, 24 (1979), 300–316.

46. Paquette, L., and Kida, T. The effect of decision strategy and task complexity on decision performance. Organizational Behavior and Human Decision Processes, 41 (1988), 128–142.

47. Parks, M.S.; Siemens, N.; and Watson, H.J. A generalized model for automating judgmental decisions. Management Science, 22 (1976), 841–851.

48. Payne, J.W. Task complexity and contingent processing in decision making: an information search and protocol analysis. Organizational Behavior and Human Performance, 22 (1976), 366–387.

49. Quinlan, J.R. Learning efficient classification procedures and their application to chess end games. In R.S. Michalski et al. (eds.), Machine Learning: An Artificial Intelligence Approach. Palo Alto, CA: Tioga, 1983.

50. Quinlan, J.R. Induction of decision trees. Machine Learning, 2 (1986), 81–106.

51. Ragsdale, C.T., and Stam, A. Introducing discriminant analysis to the business curriculum. Decision Sciences, 23 (1992), 724–745.

52. Rothstein, H.G. The effects of time pressure on judgment in multiple cue probability learning. Organizational Behavior and Human Decision Processes, 37, 1 (February 1986), 83–92.

53. Ruble, T.L., and Cosier, R.A. Effects of cognitive styles and decision setting on performance. Organizational Behavior and Human Decision Processes, 46, 2 (August 1990), 283–295.

54. Russo, J.E., and Dosher, B.A. Strategies for multiattribute binary choice. Journal of

55. SAS Institute Inc. SAS/STAT User's Guide, Release 6.03 Edition, 1988.

56. Shavlik, J.W., Mooney, R.J., and Towell, G.G. Symbolic and neural learning algorithms: an experimental comparison. Machine Learning (1991), 111–143.

57. Sniezek, J.A. The role of variable labels in cue probability learning tasks. Organizational Behavior and Human Decision Processes, 38, 2 (October 1986), 141–161.

59. Stanley, J. Introduction to Neural Networks, 2d ed. Sierra Madre, CA: California Scientific Software, 1989.

60. Stewart, T.R. Judgment analysis: procedures. In B. Brehmer and C.R.B. Joyce (eds.), Human Judgment: The SJT View. Amsterdam: North Holland, 1988, pp. 41–74.

61. Taylor, L.A. Decision quality and commitment within a probabilistic environment. Organizational Behavior and Human Decision Processes, 39, 2 (April 1987), 203–227.

62. Wallsten, T.S. Processes and models to describe choice and inference. In T.S. Wallsten (ed.), Cognitive Processes in Choice and Inference. Hillsdale, NJ: Erlbaum, 1980.

63. Wallsten, T.S., and Barton, C. Processing probabilistic multidimensional information for decisions. Journal of Experimental Psychology: Learning, Memory, and Cognition, 8, 5 (September 1982), 361–384.

64. Weiss, S.M., and Kapouleas, I. An empirical comparison of pattern recognition, neural nets, and machine learning classification methods. Proceedings of the International Joint Conference on Artificial Intelligence (1989), 781–787.

65. White, H. Neural-network learning and statistics. AI Expert (December 1989), 48–52.

66. Wright, P. The harassed decision maker: time pressure distractions, and the use of evidence. Journal of Applied Psychology, 59 (1974), 555–561.

---
otero_id: 17575
otero_key: "FSPFADEV"
title: "Neural network models for intelligent support of managerial decision making"
authors: "Tim Hill; William Remus"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90018-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Neural network models for intelligent support of managerial decision making $^{1}$

Tim Hill and William Remus

University of Hawaii, Honolulu, HI 96822, USA

Neural networks can provide advantages over conventional models of managerial decision making including being easy to embed in intelligent systems and learning from the data presented rather than requiring human interaction. This article reports a study of the ways in which neural networks can be used to model managerial judgment. In this research, we built composite neural networks and compared their performance with that of the classical methods. The neural network model closest in philosophy to the best classical composite model gave the best economic performance.

Keywords: Neural networks; Managerial decision making; Back propagation; Intelligent systems.

![](/api/attachments/FSPFADEV/fulltext/images/0d596c83d6ddea37e2170198efabf9f9ff26ed59e12114a820f0898e48a563b6.jpg)

Timothy R. Hill received his PhD in Management Information Systems in 1988 from Indiana University, where he was awarded an IBM fellowship. Since then, he has held the position of Assistant Professor in the Decision Sciences Department of the College of Business Administration at the University of Hawaii. He has written several papers describing neural network applications in the business domain. He has been active in organizing sessions on this area at the annual

Hawaii International Conference on Systems Sciences.

![](/api/attachments/FSPFADEV/fulltext/images/8398d58c46c5d60d8d470b9ebd1973a8757f021aad1cf95fed31222b324cc167.jpg)

Dr. William Edward Remus is a Professor of Decision Sciences at the University of Hawaii. His research has appeared in Management Science, Management Information Systems Quarterly, Journal of Business Research, and The International Journal of Management Science (Omega). His current research interests include the impacts of DSS on human decision making, man-machine interfaces, and neural networks. His work has been funded by the National Science Foun-

dation and he has been a Fulbright scholar at National University of Malaysia.

$^{1}$ The data for this experiment was gathered under a grant from the National Science Foundation.

## 1. Introduction

Recently there has been an outpouring of research on modeling methods inspired by the neuronal networks found in the nervous system. These models, termed neural networks, have been widely advocated for managerial tasks like forecasting and making managerial judgments. Are these claims pure advocacy or is there merit to these methods? In this article, we attempt to answer that question by comparing neural network models with conventional models for managerial decision making.

## 2. The literature

Over the last few decades, there has been much research directed at understanding and modeling managerial judgment. This research has given us many insights into and models of human judgment. The most successful models of managerial judgment are linear decision rules.

The linear decision rule is the most widely used model for representing judgmental processes (Kleinmuntz [16]; Slovic and Lichtenstein [25]). For the most part, the research on this model has focused on capturing judges' methods of weighing and combining information in the form of multiple regression equations (Bunn and Wright [3]; Kleinmuntz [16]). Such research entered the literature on managerial decision making through the work of Bowman [2]. Even judgment models such as the anchor-and-adjustment model (Tversky and Kahneman [26]; Slovic and Lichtenstein [25]) and protocol analysis (Einhorn, Kleinmuntz, and Kleinmuntz [5]) can be expressed in linear rules.

In the linear decision rule model, the manager is viewed as making a decision by choosing, weighing, and linearly combining information given by several crucial decision factors. The factors and the weights are commonly found by applying regression analysis to actual decision data. The linear decision rule has been shown to capture the intuition of the manager well and has been successfully used to model many real world and experimental tasks (see Kleinmuntz [16]).

Although linear models perform well in applied settings, they have three inherent limitations. First, their complexity is limited to the linear combination of decision variables. Second, expertise is required to avoid mis-specifying the model and/or to make the necessary data transformations. Third, even if the above is done well, the linear model may not perform well on the non-linear elements in the decision variables.

If regression is used to estimate linear models, there are limitations due to the way in which regression is used. First, regression models do not learn incrementally as new data arrives; instead, regression-based models must be re-estimated periodically. Also, regression is hard to embed in intelligent systems since the intelligent systems are not run in batch but run incrementally.

Neural networks are an alternative to regression that will learn the functional relationships among variables to predict an outcome measure. Proofs have been presented that show these networks to be capable of regression-like arbitrary mapping of variables (Hornik, Stinchcombe, and White [15]; White [28]). Also, these networks are capable of overcoming many of the above problems (e.g., automatic data transformations (Connor [4]; Ersoy, [7])). However, there is little information to suggest neural network's limitations with respect to outliers, multicolinearity, and other problems inherent with real world data.

In a recent study, Remus and Hill [22] compared linear decision rules and back-propagation neural networks of individual managers; there were no significant differences in their cost performance. Both types of models performed better than the decision makers; thus, neural networks can be used to capture decisions from individual managers and to make future decisions.

While the Remus and Hill [22] work was encouraging, neither the linear decision rules nor the neural networks performed as well as the optimal rules. Also, neither linear decision rules nor neural networks performed as well as classical composite models based on linear decision rules (see the following paragraphs for details on composite models). This comparison suggests creating neural network models similar to the classical composite models to improve upon individual decision rules and/or neural networks representing individual judgment.

Classical composite models are based on aggregating the decision rules of individual decision makers into one composite model. Note that this is a statistical combination rather than a true collective judgment rule. Usually rules for each decision maker are found by regressing his or her decision factors on the actual decision made. The regression weights then convey the relative weight the decision maker gives to each factor. To construct a composite rule, the weights are combined in some way (typically, averaging or taking the median).

The rationale for the construction of the composite rule is that individual decision makers may tend to underweight or overweigh some of the decision variables. The averaging process cancels this out. Also, regression gives only estimates of the parameters of the rules. Thus, averaging the rules could also improve the estimation accuracy. The classical composite rule outperforms the individual decision makers and their decision rules (see section 2 for details or Hamner and Carter [10]).

Composite judgment neural networks can give different decisions than classical aggregation models since they aggregate the data differently and contain embedded non-linearities. Also with classical composite models, the estimation of the model of one individual has no effect on the estimation of the model of another individual. In several neural network models of composite judgment that we will examine, the latter is not true. The existence of data on one individual will alter the estimation of the neural network of another individual. Since composite judgment is generally superior to individual judgment when using classical models (Hamner and Carter [10]), the interaction in the neural network estimation process might also improve the composite neural network performance.

Our intention in the experiment described below is to compare the performance of the classical linear aggregation models with several classes of neural networks. In the analysis, both classical and neural network models will be used to capture and apply managerial judgment. To do this kind of research, Hogarth [12] advocated testing alternative models side-by-side in critical experiments; there also is precedent for this kind of study using neural networks (Fisher and McKusick [8]; Weiss and Kapouleas [27]). Thus, our experiment is a side-by-side comparison of two competing methods for creating models of managerial judgment.

We also planned our experiment based on a behavioral theory of decision making. In particular, Schroeder, Driver, and Streufert [24] theorized that human decision performance is related to environmental complexity. They argued that the correct form had an inverted U shape; that is, decision performance was best in intermediate levels of environmental complexity. They argued such an environment challenged decision makers to do their best while not causing information overload. We chose to introduce environmental complexity into this experiment since our earlier behavioral work (e.g., Remus [20]) found this effect to occur in the production scheduling problem. As suggested by Schroeder, Driver, and Streufert [24], we operationalized environmental complexity as the level of variance in the demand (see Appendix 1 for more details).

Another reason for including levels of variance in the experiment is a recent experiment of ours. In a study comparing neural networks and regression models using simulated data, we (Marquez, Hill, Worthley, and Remus [17]) found that neural networks were particularly effective in environments with moderate rather than low levels of variance. That is, neural networks might see through the noise better than classical methods. Thus for two reasons, our experiment will examine two levels of environmental variance in the experimental design.

The first step in this research project was to gather data to compare the competing models. We have chosen the production scheduling problem as our experimental task. This choice was based on both the importance of the decision and guidance available from the experimental literature on human performance in this task.

## 3. The experimental design and analysis

The experimental design was based on the Holt, Modigliani, Muth, and Simon model of the production scheduling problem [14]. The task is to decide how many units to produce and workers to employ given uncertain future demand and knowledge of current work force size, productivity, and inventory level. The managerial intent is to minimize the average cost of the decisions as computed by a quadratic function. The cost is a function of changes in work force level, over time/idle time costs, and departures from the ideal level of inventory. The set of equations representing this model is shown in Appendix 2.

The production scheduling problem was selected because it is a managerially relevant problem and it has been calibrated with real world data (Holt, Modigliani, and Muth [13, p. 163]). Most importantly, the task is representative of a reasonably complex decision task in continuous, dynamic environments. Thus, this task avoids the criticisms associated with laboratory research that uses simplistic tasks, “toy” tasks, or static judgment tasks. This task and the experimental design are described in detail in Appendix 1.

Our research requires us to develop judgment models both the classical way and also using neural networks. Both types of models can come in many varieties. Some of the alternatives for the classical models for composite judgment include:

(1) developing one model for each decision maker and then averaging the predictions from all of the models,

(2) as above, only differentially weighing the predictions from each model forming a composite prediction,

(3) treating the data from individual decision makers as if it all came from one decision maker and regressing over all the data,

(4) building a model for each decision maker and then averaging the coefficients for each independent variable to create the composite model,

(5) as above, only using the median coefficient, and

(6) as above, only differentially weighing each model's coefficients to form the composite model.

Numerous simulation studies and laboratory studies have compared the models. For the production scheduling problem, Hamner and Carter [10] found averaging the coefficients to give best overall performance. See Armstrong [1] for a good overview consistent with the latter finding. This literature is by no means static; the best, place to observe this literature is in Journal of Forecasting (e.g., Granger and Ramanathan [9]).

There are several alternate approaches for building neural networks for managerial judgment. Like 3 above, the data could be used to estimate the neural network with no reference to the individual decision maker who was the source of the data. Another approach (like 1 and 2) is to develop a neural network for each decision maker and add other stages to combine the decisions being presented by the individual neural networks. We will use both approaches in the following study.

Our research questions are:

(1) Will the composite neural network models perform better than the actual decision makers?

(2) Will the composite neural network models perform better than regression-based models for the decision makers?

(3) Will the composite neural network models perform better than neural network-based models for the decision makers?

(4) Will composite neural network models do better than or at least as good as the composite model of Hamner and Carter [10]?

## 4. The analysis plan

Given the experimental design presented in Appendix 1, the decision maker's behavior was captured and measured in several ways. First, as the subjects made decisions, the actual costs were calculated and recorded. These costs were calculated using the paint plant's quadratic cost function. Second, the individual decision maker's production decisions were modeled with linear regression rules; the coefficients (for work force, forecasts, and inventory) were estimated using least squares regression. The resulting decision rules were then used to make the production decision; the costs were calculated using the paint plant's quadratic cost function. This procedure for evaluating decision rules has been used in similar studies. The fit of this model to actual decisions was measured in terms of mean square error. Third, following Hamner and Carter [10], the regression coefficients were averaged to create a composite rule. These rules were evaluated as described above. Last, three neural network models for judgment were estimated; these models were also evaluated as described above for the decision rules.

The neural networks were based on the back-propagation learning algorithm (see Rumelhart and McClelland [23] or Hecht-Nielsen [11] for details). Each model differed from the other by increasing levels of network size and complexity. These models were formulated following Rumelhart and McClelland [23]; our software was based on their programs originally written in C.

## 4.1. Overfitting

In the regression model, a different set of model parameters was fit for each subject since there were enough degrees of freedom to estimate each model. Neural networks, however, often consume more degrees of freedom than a comparable regression model since every connection weight and node bias is a fit parameter. This is a problem since as the number of parameters approaches the number of observations, neural networks lose the ability to generalize and begin to “memorize” rather than “learn.”

In applying neural networks to judgment data, overfitting can be a difficult problem since the number of observations may not be large with respect to the number of parameters to be estimated. One approach to address this problem is to split the historical data into two sets: (1) one set with which to estimate the model and (2) a holdout set used to test the model for overfitting. However, this merely allows one to evaluate any overfitting effects. It does not guarantee that the model will be free of overfitting problems.

In many applications, composite judgment models offer the potential of avoiding the overfitting problem by being estimated from the data of numerous decision makers, thus, increasing the available sample size (in our case to 1488 observations). In the following analysis, the neural networks have been designed to avoid the overfitting problem through having a very large number of degrees of freedom.

## 4.2. Learning

In doing the analysis we were concerned that there might be differing results between when the subjects were learning and when their learning had ended. To determine when learning ended in this task, Remus, Carter, and Jenicke [21] conducted a study on learning in the production scheduling decision. They found that learning occurred in the first twelve periods; following those periods, the subjects tended not to alter their factor weighing. The learning in the early periods was a linear function of time and was shown by the subjects both approaching optimal decisions and reducing erratic behavior. Thus, the 24 periods were divided into two portions: periods 1 to 12 and periods 13 to 24. In this way the periods when the subjects were learning the experimental production scheduling exercise could be analyzed separately from the periods when the subjects adopted a stable decision making strategy. The division will be confirmed via a manipulation test prior to the analysis.

All models reflect the latter distinction. The regression approach was used to estimate two models for each subject: one for the learning phase and one for the stable decision making phase. In the neural network models, the input layers included one node with a binary input to distinguish the first 12 periods from the last 12 periods.

## 4.4. The three neural networks

The first neural network model is denoted NNC1; it uses the same structure as Remus and Hill's best performing regression model for an individual manager's decision. This network has one "hidden layer" of 12 nodes between the input and output layers. As in the regression models, work force, the three forecasts (for one, two, and three periods ahead), and inventory levels were used as input. Additional inputs included the subject identification number (see the following paragraph) and a flag to distinguish decisions in which learning was occurring. All nodes used sigmoid transfer functions; backpropagation was used to adjust the strengths of the weights in the network.

To avoid the overfitting problem, the first neural network was fit simultaneously for all subjects.

To make the first neural network model (NNC1) comparable to the regression model and to allow the network to account for inter-subject variability, subject numbers were also included as input to the neural networks. The subject numbers were converted to binary and sent to the input nodes along with the other data. The trained network, therefore, synthesizes subject-specific production decisions by using the subject's binary number along with the decision data. Thus, NNC1 models an individual's decisions while simultaneously estimating an overall decision model. This model had 1318 degrees of freedom.

The second neural network model (denoted NNC2) was also created with one hidden layer of 12 nodes. Again all nodes were sigmoid and learning was based on the back-propagation model. For this neural network model, we dropped the above subject identifier allowing the neural network to capture the composite judgment without identification of the subject from which that the data came. All inputs (except the subject identifier) were the same as in the first neural network. Again, all nodes used sigmoid transfer functions and back-propagation was used to adjust the strengths of the weights in the network. This model had 1390 degrees of freedom.

The third neural network model (denoted NNC3) was more complex yet; it was composed of numerous mini-neural networks (mini-NN's), one for each decision maker. Each mini-NN was estimated separately for a specific decision maker. The inputs were the same as in NNC2 (work force, the three forecasts, inventory, and a flag showing if the data was for the learning periods) but there was no hidden layer used.

After the mini-NN's were estimated, the parameters in each mini-NN were frozen and the mini-NN's embedded in the larger network. The first layer of NNC3 provided the value of the six inputs to each mini-NN. The second layer consisted of the output nodes of the mini-NN's, each outputting their own decision to the third layer. The third layer was one node that combined the many mini-NN decisions into one composite decision. As before, the nodes had sigmoid transfer functions and learning was based on the backpropagation model. This model was suggested by Ersoy [6]. This model had 990 degrees of freedom.

All neural networks were trained based on minimizing the error between the neural network decisions and the actual decisions made. Back-propagation minimizes the least squared error if (1) the model does not get trapped in a local optimal and (2) there are an adequate number of nodes in the hidden layer. On the first point, it is important to note that back-propagation is a gradient descent technique that will arrive at an optimal point; however, that point might be locally optimal. On the second point, it is not clear how many nodes are required to assure that the optimal point will be reached.

To assure that the error is minimized, it is customary to build a neural network keep doubling the number of nodes until the error is no longer reduced (Ersoy [6]). We used this approach to arrive at the configurations for networks NNC1, NNC2, and NNC3. In each case we found that expanding the hidden layer to more than 12 nodes gave little improvement in error performance while degrading the processing speed and convergence rate.

## 5. Results

The central research questions focus on a comparison of neural network models and regression models for capturing managerial decision making; the experiment described in Appendix 2 provided us with data on 62 decision makers each making 24 useable decisions. The regression models for both the individual 62 decision makers and for the composite model were estimated as described above using SAS.

The three neural networks (NNC1, NNC2, and NNC3) were estimated using the Rumelhart and McClelland back-propagation code described above. As noted earlier, we had available 24 decisions from each of the 62 decision makers. This left 1314 degrees of freedom to estimate NNC1, 1390 to estimate NNC2, and 990 to estimate NNC3. The values for momentum used initially were close to the Rumelhart and McClelland defaults; these were gradually damped to zero during training. The neural network weights were adjusted following the presentation of each data observation. Convergence was typically reached in 250 to 600 epochs, depending on the configuration of the network.

The cost performance of the models in low variance (reported are the significance levels for the paired comparisons)

<table><tr><td rowspan="3"></td><td colspan="5">During the learning periods (1-12)</td></tr><tr><td rowspan="2">Mean</td><td rowspan="2">Regression</td><td colspan="3">Neural Networks</td></tr><tr><td>NNC1</td><td>NNC2</td><td>NNC3</td></tr><tr><td></td><td>(SD)</td><td></td><td></td><td></td><td></td></tr><tr><td>Mean</td><td></td><td></td><td>28611</td><td>26245</td><td>26695</td></tr><tr><td>(SD)</td><td></td><td></td><td>(4125)</td><td>(3434)</td><td>(3530)</td></tr><tr><td>Optimal</td><td>22435</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td></td><td>(3241)</td><td></td><td></td><td></td><td></td></tr><tr><td>Composite</td><td>24648</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td></td><td>(3323)</td><td></td><td></td><td></td><td></td></tr><tr><td>Regression</td><td>28517</td><td>-</td><td>0.739</td><td>0.016</td><td>0.051</td></tr><tr><td></td><td>(5070)</td><td></td><td></td><td></td><td></td></tr><tr><td>Actual</td><td>33424</td><td>0.000</td><td>0.016</td><td>0.001</td><td>0.001</td></tr><tr><td></td><td>(10848)</td><td></td><td></td><td></td><td></td></tr></table>

During the steady state decision making periods (13–24)

<table><tr><td rowspan="2"></td><td rowspan="2">Mean</td><td rowspan="2">Regression</td><td colspan="3">Neural Networks</td></tr><tr><td>NNC1</td><td>NNC2</td><td>NNC3</td></tr><tr><td></td><td>(SD)</td><td></td><td></td><td></td><td></td></tr><tr><td>Mean (SD)</td><td></td><td></td><td>33921(6851)</td><td>31481(4527)</td><td>31754(4758)</td></tr><tr><td>Optimal</td><td>25838(4209)</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>Composite</td><td>29456(4678)</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>Regression</td><td>34181(9166)</td><td>-</td><td>0.825</td><td>0.041</td><td>0.070</td></tr><tr><td>Actual</td><td>38530(11164)</td><td>0.000</td><td>0.004</td><td>0.000</td><td>0.001</td></tr></table>

All tests used the two-tailed matched-pair t-test.

Prior to the analysis, we might note that our distinction between learning and steady state decisions was confirmed with a manipulation check using analysis of variance on the actual decisions made. There was no significant change in the decision rules beyond period 12 (p < 0.05).

The best way to compare models is to ask which model provides the best decisions. In the production scheduling problem, the best decisions yield the lowest cost. Therefore, in the following tests, the mean cost performance of the models is compared; the results are shown in Table 1 (for low variance) and Table 2 (for intermediate variance).

In both learning and post-learning periods, all neural networks (and the regression and classical composite models) produced decisions that were significantly less costly than actual decisions made; this occurred in both low and intermediate variance. This means any of neural networks can be used to model decision makers as effectively as regression rules can.

In the next several paragraphs, we will report only the performance of NNC2 since (1) its performance so strongly dominates NNC1 and NNC3 and (2) it has largest degrees of freedom (and thereby lowest susceptibility to overfitting). It is not unexpected that NNC2 is superior to NNC1 given the literature on classical composite rules;

Table 2  
The cost performance of the models in intermediate variance (reported are the significance levels for the paired comparisons)

<table><tr><td rowspan="3"></td><td colspan="5">During the learning periods (1-12)</td></tr><tr><td rowspan="2">Mean</td><td rowspan="2">Regression</td><td colspan="3">Neural Networks</td></tr><tr><td>NNC1</td><td>NNC2</td><td>NNC3</td></tr><tr><td></td><td>(SD)</td><td></td><td></td><td></td><td></td></tr><tr><td>Mean (SD)</td><td></td><td></td><td>30602(8356)</td><td>28141(8657)</td><td>28870(8710)</td></tr><tr><td>Optimal</td><td>23738(6872)</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>Composite</td><td>27420(8758)</td><td>0.000</td><td>0.000</td><td>0.077</td><td>0.002</td></tr><tr><td>Regression</td><td>29326(10367)</td><td>-</td><td>0.314</td><td>0.340</td><td>0.717</td></tr><tr><td>Actual</td><td>42087(15611)</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr></table>

During the steady state decision making periods (13–24)

<table><tr><td rowspan="2"></td><td rowspan="2">Mean</td><td rowspan="2">Regression</td><td colspan="3">Neural Networks</td></tr><tr><td>NNC1</td><td>NNC2</td><td>NNC3</td></tr><tr><td></td><td>(SD)</td><td></td><td></td><td></td><td></td></tr><tr><td>Mean (SD)</td><td></td><td></td><td>41172(8933)</td><td>36837(8336)</td><td>37863(8370)</td></tr><tr><td>Optimal</td><td>29590(6360)</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>Composite</td><td>36964(7886)</td><td>0.000</td><td>0.025</td><td>0.904</td><td>0.395</td></tr><tr><td>Regression</td><td>39551(10972)</td><td>-</td><td>0.427</td><td>0.081</td><td>0.258</td></tr><tr><td>Actual</td><td>44357(12600)</td><td>0.000</td><td>0.166</td><td>0.000</td><td>0.001</td></tr></table>

All tests used the two-tailed matched-pair t-test.

that is, composite models always perform better than individual decision makers. The superiority of NNC2 over NNC3 was surprising to us. A priori, we thought that building models retaining the weighing the individual subject's decision making (NNC3) would give better performance than just combining the subject's data into one averaged composite (NNC2). However, as noted earlier, forecasters have also found simple averaging models to be the best (Armstrong [1]) as have those working on the production scheduling problem (Hamner and Carter [10]). We might also note that NNC2 has the highest degrees of freedom, hence, is least likely to be overfit.

In low variance, NNC2 had significantly better cost performance than the regression models, both when learning and in steady state decision making. In intermediate variance, we found no evidence that neural network NNC2 had significantly different cost performance than regression rules.

NNC2 also did a creditable job when compared with the classical composite model. We found no evidence that neural network NNC2 had significantly different cost performance than the classical composite rules in intermediate variance. However, in low variance the classical composite model yielded nearly 7% lower costs; this difference was statistically significant.

## 6. Discussion and conclusions

It is well established in the behavioral decision making literature that heuristics based on recurrent managerial decisions frequently perform better than the actual decision maker. These findings led researchers to suggest that organizations could model recurrent decisions using regression and use the resulting models to improve their economic performance (Kleinmuntz [16]). The literature also points out that combining the rules of several decision makers (the resulting model is termed a composite rule) will improve economic performance even further.

Our experiment suggests that neural networks also have the potential to improve managerial decision making when the manager is faced with recurrent quantitative decisions. The advantages of neural networks for individual decision makers (e.g., NNC1) over classical models are only technological. They are easier to embed and they support incremental updating while giving equivalent performance.

Composite neural networks offer both performance and technological advantages over the classical models for individual decision makers. However, we found no evidence to suggest that composite neural networks perform better than classical composite models; in fact, we found several cases to the contrary. We also consistently found all estimated models (classical and neural network) inferior to the analytically optimal rule.

In the research reported in this article, we found the relative economic performance of the composite neural network (NNC2) to be affected by the level of environmental variance. Generally, the composite model performed relatively better in intermediate variance. This finding is consistent with Marquez, Hill, Worthley, and Remus' simulation study $[17]$ that found neural networks to perform best in intermediate levels of environmental variance (They attributed this result to neural networks relative advantage in seeing through noisy data). It is not clear, however, that neural networks have this relative advantage in intermediate variance environments outside experimental and simulation studies.

It is interesting to note that the best of the composite neural networks (NNC2) was also the simplest to construct; just input the collected data in one stream noting only if it was learning or post-learning data. This network was also closest to the classical composite model where the weights are averaged. Also, this model has the least possibility of being overfit.

## References

[1] J.S. Armstrong, Long-Range Forecasting, 2nd edn., Wiley, New York, 1985.

[2] E.J. Bowman, Consistency and Optimality in Managerial Decision Making, Management Science, 9, 2, (1963) 310-322.

[3] D. Bunn and G. Wright, Interactions of Judgemental and Statistical Forecasting Methods: Issues and Analysis, Management Science, 37, 5, (1991) 501–519.

[4] D. Connor, Data Transformation Explains the Basics of Neural Networks, EDN, (May 12, 1988) 138–144.

[5] H.J. Einhorn, D.N. Kleinmuntz and B. Kleinmuntz, Linear Regression and Process Models of Judgment, Psychological Review, 86, 3, (1979) 465–485.

[6] O. Ersoy, Tutorial at Hawaii International Conference on Systems Science, (1990).

[7] O. Ersoy, Tutorial at Hawaii International Conference on Systems Science, (1991).

[8] D.H. Fisher, and K.B. McKusick, An Empirical Comparison of ID3 and Back-Propagation, Proceedings of International Joint Conference on Artificial Intelligence, (1989) 788–793.

[9] C.W.J. Granger and R. Ramanathan, Improved Methods of Combining Forecasts, Journal of Forecasting, 3, (1984) 197–204.

[10] W.C. Hammer and P.L. Carter, A Comparison of Alternative Production Management Coefficient Decision Rules, Decision Science, 6, 2, (1975) 324–336.

[11] R. Hecht-Nielsen, Theory of the Backpropagation Neural Network, Proceedings of International Conference on Neural Networks, Vol. I, (1989) 593–605.

[12] R.M. Hogarth, Generalizations in Decision Research: The Role of Formal Models, Graduate School of Business, University of Chicago (1986).

[13] C.C. Holt, F. Modigliani and J.F. Muth, Derivation of a Linear Decision Rule for Production and Employment, Management Science, 2, 2, (1956) 159–177.

[14] C.C. Holt, F. Modigliani, J.F. Muth and H.A. Simon, Planning Production, Inventories, and Work Force, Prentice-Hall, Englewood Cliffs, NJ, 1960.

[15] K. Hornik, M. Stinchcombe and H. White, Universal Approximation of an Unknown Mapping and Its Derivatives Using Multilayer Feedforward Networks, Neural Networks, 3, (1990) 551–560.

[16] B. Kleinmuntz, Why We Still Use Our Heads Instead of Formulas: Toward an Integrative Approach, Psychological Bulletin, 107, 3, (1990) 296–310.

[17] L. Marquez, T. Hill, R. Worthley and W.E. Remus, A Simulation Study of Neural Networks, Forthcoming in Neural Network Applications in Finance and Investment edited by E. Turban and R. Trippi, Probus Publishing.

[18] H. Moskowitz and J.G. Miller, Information Systems and Decision Systems for Production Planning, Management Science, 22, 3, (1975) 359–371.

[19] W.E. Remus, An Empirical Test of the Use of Graduate Students as Surrogates for Managers in Experiments on Business Decision Making, Journal of Business Research, 14, 1, (1986) 19–25.

[20] W.E. Remus, A Study of the Impact of Graphical and Tabular Displays and Their Interaction with Environmental Complexity, Management Science, 33, 9, (1987) 1200–1205.

[21] W.E. Remus, P.L. Carter and L.O. Jenicke, Regression Models of Decision Rules in Unstable Environments, Journal of Business Research, 7, 2, (1979) 187–196.

[22] W.E. Remus and T. Hill, Neural Network Models for Managerial Judgment, Proceedings of the Hawaii International Conference on the System Sciences, Vol. IV, (1990) 340–344. Accepted for publication in Advances in Artificial Intelligence.

[23] D. Rumelhart and J. McClelland, Parallel Distributed Processing, MIT Press, Cambridge, MA, 1986.

[24] H.M. Schroeder, M.J. Driver, and S. Streufert, Human Information Processing, Holt, Rinehart, and Winston, New York, 1967.

[25] P. Slovic and S. Lichtenstein, Comparison of Bayesian and Regression Approaches to the Study of Information Processing in Judgement, Organizational Behavior and Human Performance, 6, (1971) 649–744.

[26] A. Tversky and D. Kahneman, Judgment Under Uncertainty: Heuristic and Biases, Science, 185, (1974) 1124-1131.

[27] S.M. Weiss and I. Kapouleas, An Empirical Comparison of Pattern Recognition, Neural nets, and Machine Learning Classification Methods, Proceedings of International Joint Conference on Artificial Intelligence, (1989) 781–787.

[28] H. White, Connectionist Nonparametric Regression: Multilayer Feedforward Networks Can Learn Arbitrary Mappings, Neural Networks, 3, (1990) 535–549.

## Appendix 1: The experimental design

The experimental design is based on the Holt, Modigliani, Muth, and Simon model of the production scheduling problem $[14]$ . The task is to decide how many units to produce and workers to employ given uncertain future demand and knowledge of current work force size, productivity, and inventory level. The managerial intent is to minimize the average cost of the decisions as computed by a quadratic function. The cost is a function of changes in work force level, overtime/idle time costs, and departures from the ideal level of inventory. The set of equations representing this model is shown in Appendix 2.

The subjects were graduate students from an evening course in management science and computers; over 80% of the subjects were employed. The subjects were paid a ten dollar fee. The subjects had no prior experience in the scheduling exercise and they had no knowledge of the optimization models for this decision. Remus [19] found no differences in cost performance in this task between managers and graduate students; thus, even though graduate students were used, the results should generalize.

In preparation for the experiment, the subjects were given the following training. First, the subjects as a group were given a forty minute lecture/demonstration of the production scheduling simulation. They were then scheduled for individual appointments to do the simulation. When each arrived, he or she was given a quick review of the main points of using the software and then made four familiarization decisions; we did not use these decisions in our analysis. Each subject was told to do his or her best to keep costs low. The subjects were physically isolated in cubicles and not allowed to talk to other subjects or to see the other subjects' decisions. Each subject was also told that he or she had as long as desired to complete the task; the typical time used was just under two hours and the maximum time used was 150 minutes.

The 62 subjects made production and work force decisions for 24 periods; a timesharing computer monitored the decisions and collected the data. Subjects first received the sales forecasts for the next three periods. This choice was based on Moskowitz and Miller's [18] research demonstrating the superiority of the three period forecast horizon over shorter forecast horizons in the production scheduling problem. Based on these forecasts, the inventory position, current work force size and worker productivity, the subjects decided what production volume to schedule and how many workers they should employ. After they input their decisions, the computer gave them an opportunity to check that they had correctly typed in their decisions.

The subjects then received the actual sales and costs, the new inventory level, and the average cost so far. The subjects were given no bench mark average cost level for the task nor did they know the optimal cost for the task. All the cost and inventory calculations were done by the computer. This cycle was repeated for each of the 24 periods.

The quadratic cost function used in the experiment was found by Holt, Modigliani, and Muth [13, p. 163] to characterize a paint plant except that, following Moskowitz and Miller [18], only the quadratic cost terms were used.

The initial demand was set at 2500 units; the demand grew at 20 units per period. An eight period sinusoidal pattern, with an amplitude of 20% of the unadjusted demand, was added to the latter demand. The demand pattern was then given low and intermediate levels of variability by adjusting it with a uniformly distributed variation of $\pm100$ and $\pm400$ units of demand. Thirty one subjects were assigned to each level of demand variance. Forecasts were the demand plus uniformly distributed forecast error; the further into the future that the forecast was, the higher the error. Each subject received a unique pattern of adjusted demand by having the uniformly distributed variation controlled by a random number generator. These demand and forecast equations are also shown in Appendix 2.

The low variance level was used by Moskowitz and Miller [18], Remus [20], and Remus, Carter, and Jenicke [21]; hence, there is a comparability of results at this level of variability. The Moskowitz and Miller [18] study and others have found subjects to approach optimal performance at this level of variability.

Our intermediate variability treatment had a variance level below that of Moskowitz and Miller's [18] intermediate forecast variability treatment but well above the low variance treatment. This level had been used by Remus [20] in researching the effectiveness of data displays. Both Moskowitz and Miller [18] and Remus [20] found quality decision making at their intermediate treatment; thus, the treatment in the current study would seem well calibrated. That is, it has more variance than the low variability treatment but not so high of variance as to cause information overload.

Appendix 2: The equations for production scheduling problem and decision heuristics  
```txt
The Cost Function
Cost = Inventory Cost + Work Force
Change Cost + Over/Idle Time
Inventory Cost = c₁*(Iₜ - I*)²
Work Force Change Cost = c₂*(Wₜ - Wₜ₋₁)²
Over/Idle Time Cost = c₃*(Pₜ - k * Wₜ)²
```

Also Required is the Inventory Equation

$$
\mathrm{I} _ {\mathrm{t}} = \mathrm{I} _ {\mathrm{t-1}} + \mathrm{P} _ {\mathrm{t}} - \mathrm{D} _ {\mathrm{t}}
$$

The Heuristics

For Linear Models

$$
\begin{array}{c} \mathbf {P} _ {\mathfrak {t}} = \mathsf {b} _ {0} + \mathsf {b} _ {1} * \mathbf {W} _ {\mathfrak {t} - 1} + \mathsf {b} _ {2} * \mathbf {F} _ {\mathfrak {t}} + \mathsf {b} _ {3} * \mathbf {F} _ {\mathfrak {t} + 1} + \\ \mathsf {b} _ {4} * \mathbf {F} _ {\mathfrak {t} + 2} - \mathsf {b} _ {5} * \mathbf {I} _ {\mathfrak {t} - 1} \end{array}
$$

The Variables

$D_{t}$ Demand in period t

$F_{t}$ Forecast for the demand in period t

$I_{t}$ Inventory at the end of period t

$P_{t}$ Units produced in period t

$W_{t}$ Number of workers in period t

The Constants Used in the Models

k the productivity per worker per period (5.67)

I\* the desired level of inventory (320)

In the Heuristics, $b_{0}$ to $b_{5}$ were estimated using Regression.

Demand Generation plus Uniformly Distributed Error

For Low Environmental Variance

$$
\begin{array}{r l} \mathrm {D_ {t}} & = (2 5 0 0 + t * 2 0) (1 + 0. 2 0 * \sin (t / 8 * \\ & \quad 3. 1 4 1 6)) + \mathrm{U} (- 1 0 0, 1 0 0) \end{array}
$$

For Intermediate Environmental Variance

$$
\begin{array}{r l} \mathrm {D_ {t}} & = (2 5 0 0 + t * 2 0) (1 + 0. 2 0 * \sin (t / 8 * \\ & \quad 3. 1 4 1 6)) + \mathrm{U} (- 4 0 0, 4 0 0) \end{array}
$$

Forecasts are the Demand plus Uniformly Distributed Error

$$
\mathrm{F} _ {\mathrm{t}} = \mathrm{D} _ {\mathrm{t}} + \mathrm{U} (- 2 0 0, 2 0 0)
$$

$$
\mathrm{F} _ {\mathrm{t} + 1} = \mathrm{D} _ {\mathrm{t} + 1} + \mathrm{U} (- 4 0 0, 4 0 0)
$$

$$
\mathrm{F} _ {\mathrm{t} + 2} = \mathrm{D} _ {\mathrm{t} + 2} + \mathrm{U} (- 4 5 0, 4 5 0)
$$

U(a,b) Random Error of between a and b units.

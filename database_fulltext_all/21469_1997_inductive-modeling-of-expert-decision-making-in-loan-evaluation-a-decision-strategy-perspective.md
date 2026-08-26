---
otero_id: 21469
otero_key: "J7UAWUFY"
title: "Inductive modeling of expert decision making in loan evaluation: a decision strategy perspective"
authors: "Choong N. Kim; H. Michael Chung; David B. Paradice"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00022-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Inductive modeling of expert decision making in loan evaluation: a decision strategy perspective

Choong N. Kim $^{a,*}$ , H. Michael Chung $^{b,1}$ , David B. Paradice $^{c}$

$^{a}$ Hallym University, Choonchun, South Korea

$^{b}$ Department of Information Systems, California State University, Long Beach, 90840-8506 CA, USA

$^{c}$ Department of Business Analysis and Research, Texas A & M University, College Station, 77843 TX, USA

## Abstract

There have been two dominant paradigms in understanding and modeling an expert's decision-making behavior: output analysis and process-tracing. While the two paradigms are complementary, they have not been used yet in a combined manner. This study extends the previous research work in the two paradigms to expert system research by (1) analyzing individual experts' decision strategies, (2) comparing performance of four popular inductive modeling methods, and (3) matching their performance against decision strategy type. © 1997 Elsevier Science B.V.

Keywords: Induction; Decision model; Decision strategy; Expert system; Knowledge acquisition

## 1. Introduction

Most descriptive decision research, performed primarily by psychologists, aims at constructing descriptive decision models which emulate, mimic, and replace human judgment. In attempting to understand model judgment, two approaches have been dominant: output analysis and process-tracing. The former approach focuses on finding relationships between relevant cues and final decisions of humans, and developing a decision model simulating the relationships. The latter approach focuses on analyzing the actual process of making a judgment, namely, the decision strategy.

With the advancement of computer technology, the judgment-modeling issue has been revisited in artificial intelligence, with different names: typically, expert-modeling or knowledge acquisition. How to extract expertise and knowledge from an expert and build a reliable and consistent knowledge base for an expert system was one of its concerns. Often, research efforts in computer science were targeted toward development of methods for eliciting an expert's expertise and knowledge. However, behavioral aspects of human decision-making often were not considered properly.

While the research by computer scientists provides decision researchers with a variety of tools for modeling an expert's judgment, valuable methodologies of the process-tracing approach have never been coupled with the output analysis approach or even with expert-modeling research. Thus, an examination of expert decision strategy seems to be necessary to ensure appropriate application of expert-modeling methods. In this way, the relative performance of various expert-modeling (knowledge elicitation) methods can be compared appropriately.

This paper extends the behavioral aspect of descriptive decision research to expert systems research, by (1) examining decision strategy through the use of process-tracing approaches, (2) comparing the performance of four popular knowledge elicitation methods, and (3) matching their performance against type of decision strategy being adopted by individual experts in making decisions.

## 2. Literature review

This section reviews key literature in behavioral decision research and empirical studies in expert-modeling as an extension of the output analysis approach. A research question is also raised based on the literature review.

## 2.1. Output analysis (policy-capturing paradigm)

The objective of output analysis research is to develop structural representations of human decision-making processes. To build such representations, statistical methods (e.g., linear regression and discriminant analysis) and machine learning algorithms (primarily learning-by-examples and the neural network approach) have been applied to various tasks.

## 2.1.1. Bootstrapping

Bootstrapping is the replacement of a decision maker by the simple linear model of his or her judgment. Many studies $[1-4]$ provide evidence on the applicability of bootstrapping, supporting the robustness of the linear models.

One of the major research issues in expert-modeling is whether the model would be more valid or less valid than expert's judgment [5,6]. To the extent that the model fails to capture a valid nonlinear decision strategy of an expert, it should perform worse than the expert. To the extent that the model eliminates the inconsistency in the expert's decision-making behavior, it should outperform the expert.

Some empirical tests to address this question have been conducted $[2,5,6]$ . The results indicate that linear models of human experts outperform the experts in prediction tasks. The results, based primarily on the use of linear regression and discriminant analysis, imply that the linear model can be used as a benchmark for the evaluation of the performance of the other modeling techniques in expert-modeling.

## 2.1.2. Expert-modeling using inductive learning methods

Since the late 1970s, expert systems (ES) have been widely applied to model-building in a business environment. Among several ways of eliciting knowledge (expert-modeling) is the learning-by-examples (LBE) approach. This approach produces decision rules from the example cases a human expert provides [7]. A large number of studies report good performance of Quinlan's ID3 algorithm [8] which is the basis of all commercially viable induction systems using the LBE approach [9–14].

Recently, the use of neural networks (another inductive mechanism) in similar tasks has been addressed by a few researchers $[15–19]$ . For example, Dutta and Shekhar $[17]$ used a neural network to build a decision model and contrast it with a regression model in predicting bond-ratings. They found that neural nets outperformed regression analysis in a multiple classification task (bond-rating). However, most studies have focused on proving superiority of the new method over the existing approaches in simulating environmental data. Very few studies $[20]$ have applied neural networks to modeling human decision-making behavior.

## 2.2. Process-tracing research

Unlike the policy-capturing research, process-tracing is concerned with examining the cognitive processes actually used by a decision maker. This approach views the decision maker as a problem solver with the capability to select among existing strategies $[21,22]$ . To capture the processes used by the decision maker to arrive at a solution, various process-tracing techniques have been introduced, such as protocol analysis and some mathematical methods.

Since this approach has been concerned with examining the decision process and the effect of environmental changes on the process, it has contributed to describing a variety of decision strategies. However, this approach has never been coupled with the output analysis approach in expert-modeling.

With the lack of decision behavior understanding, previous studies have had to focus on characteristics of task and algorithms in interpreting results. Thus, the previous studies could not explain how the bootstrapping could be achieved or why a certain algorithm performed better than another. Therefore, it seems to be necessary to evaluate the performance of certain inductive modeling algorithms in relation to the decision strategy type being used.

## 2.3. Research objective

As reviewed in this section, a linkage between the decision strategy and the modeling algorithms in evaluating model performance has been missing. One interpretation is that decision strategy has not yet been appropriately considered in modeling human judgment. This finding suggests a need to reevaluate the previous studies within a new framework which includes decision strategy. Thus, if more reliable decision models or expert systems are to be built, obtaining a more complete understanding of how a certain strategy is modeled well by a certain algorithm is necessary.

Combining the two approaches is also supported by Svenson's argument [23] that “a good theory for human decision-making must be based on the data from structural analysis (output analysis) of decision-making as well as from process-tracing studies.” In summary, this section raises the research question: “Which strategy of an expert is effectively represented by a certain decision algorithm, and how?” Therefore, this study proposes a theoretical framework for expert-modeling research, which considers the relationships among decision strategy, modeling algorithms, and model performance.

## 3. Conceptual basis of the study

This section describes various decision strategies and characteristics of four inductive modeling algorithms. Lens model analysis and log transformation methods for analyzing decision strategies are also explained.

## 3.1. Decision strategies

The two major types of decision strategies introduced in the decision-making literature are compensatory (or linear) and noncompensatory (or nonlinear) [24-26]. The compensatory strategy assumes that respective cue values are combined in an additive manner resulting in an overall value for a given case. This strategy implies that a trade-off between a high value on one dimension and a low value on another dimension is allowed. A good example of this strategy is the first order linear regression model which graphs a straight line.

On the other hand, the noncompensatory strategy is indicated by the nonlinear or interactive use of cues in which a low value on one dimension cannot be compensated for by a high value on another dimension $[27]$ . There are four types of nonlinear decision strategies: conjunctive, disjunctive, elimination-by-aspects and lexicographic strategies $[26,23]$ . Conjunctive and disjunctive strategies are directly concerned with classification type decisions.

For example, using the conjunctive strategy, a decision maker sets a minimum requirement for each dimension and then rejects decision alternatives which do not meet this minimum standard. On the other hand, the disjunctive strategy requires that an alternative should pass the criterion for at least one dimension.

When a decision is more concerned with selecting the best among multiple alternatives, a lexicographic or elimination-by-aspects rule is applicable. The lexicographic decision rule prescribes a choice of the alternative which is the most attractive on the most important attribute. In the elimination-by-aspects rule, the most important attribute is investigated, and all alternatives that do not exceed the minimum requirement on this attribute are eliminated. This procedure is repeated with the next important attribute.

Decision makers may employ a number of decision strategies that are different from each other. Olshavsky [26] suggested that multiple decision strategies may be applied in succession in the same decision situation because cognitively human decision-making consists of a series of subprocesses. This suggestion implies that human decision behavior may be decomposable into linear and nonlinear components.

## 3.2. Linear models and nonlinear models

## 3.2.1. Linear models

Linear models emulate expert decision-making behavior by constructing a linear equation. The results of such an analysis are a set of regression weights for each term in the equation, or cue. Linear models correspond to linear or compensatory decision strategies. Linear regression and discriminant analysis have been used primarily to build the linear models.

Discriminant analysis (DA) is a statistical technique used to classify an observation into one of several a priori groupings dependent upon the observation's individual characteristics. It is the most widely used classification method in problems where the dependent variable contains binary values (e.g., bankruptcy prediction). The basic idea of DA is to find a set of weights, by which to compute a score of each object, which lead to maximum discrimination between groups. The DA approach develops a linear classification function, in which input information is combined linearly to compute the discriminant score which is then used to classify an observation as follows:

$$
\text { Discriminant   Score } Z = v _ {1} x _ {1} + v _ {2} x _ {2} + \dots + v _ {n} x _ {n} \tag {1}\tag{1}
$$

where, $v_{1}$ , $v_{2}$ , $\ldots$ , $v_{n}$ = discriminant coefficients, and $x_{1}$ , $x_{2}$ , $\ldots$ , $x_{n}$ = decision cues. The linear function represents a hyperplane that classifies the observations in the given space set into two partitions.

While DA can be directly used in classification, linear regression analysis is not appropriate for such classification tasks as bankruptcy prediction. For such a classification task, logistic regression (LR) methods capture the linear algebraic relationship best [28]. The LR method derives a log linear relationship between the set of cues and criterion using maximum likelihood estimates. The LR functions are of the form [29]:

$$
\text { Expected   response } E \{Y \} = \exp (y) / [ 1 + \exp (y) ] \tag {2}
$$

where $y = b_{0} + \Sigma b_{i} x_{i}$ , and $b_{i}$ and $x_{i}$ have the usual regression interpretation. Therefore, the LR model gives the estimates of the response variable which are usually interpreted as the probability of a class outcome.

A common property of these two linear models is that input information is combined linearly. Another common property is that the functions generated by the two are conditionally monotonic. Depending on the sign of coefficients, the relationship between an independent variable and the score (estimate) of the response variable is either monotonic increasing or monotonic decreasing. Based on these properties, models generated by DA and LR are considered linear models.

## 3.2.2. Nonlinear models (rule-based expert systems)

A number of different inductive learning methods have been developed. Among them, ID3 is considered a simple but effective rule-based method for learning by examples (LBE). When it is given a training set of positive and negative examples, ID3 constructs a decision tree for classifying examples into two classes [13].

The inductive learning method is based on information theory and uses an information-theoretic measure called entropy. Entropy is a measure for the amount of information carried by a message in communication [30]. This method requires that at any point the system examine the attribute (independent variable) that provides the greatest gain in information or, equivalently, the greatest decrease in entropy.

Based on the entropy concept, information on each attribute (independent variable) is processed sequentially and combined logically (conjunctively or disjunctively) along the decision tree [31]. Therefore, a linear combination of input information and other properties of linear models cannot be expected in the method. Rather, the logical information processing in ID3 seems to be very similar to a nonlinear decision strategy. Thus, ID3 is considered a typical nonlinear algorithm.

## 3.2.3. Nonlinear models (network-based decision models)

A neural network is a dynamic model consisting of perceptrons (also called nodes), connections between the perceptrons, and layers associated with each perceptron [32]. There are three types of perceptrons: input, output, and hidden layer perceptrons. The input perceptrons receive input values from sources external to the neural network. The output perceptrons produce the output of the neural network. The hidden layer perceptrons serve to detect features, regularities, and generalizations in the data. Hidden layers allow neural networks to perform more flexible processing and more powerful classification [33].

Back-propagation (BP) is the most often used paradigm in neural networks [32]. BP learning is actually achieved through a learning rule which adapts or changes the connection weights of the network so as to improve the match between the actual and the desired outputs of the system. With the learning rule (also called the delta rule), the goal is to reduce the error, or the difference between a network's current output and a desired output by changing the connection weights. In this way, the network is able to learn to classify patterns of inputs. Once a network is well trained, it can be used as an excellent decision model in predicting the true outcomes.

Since BP generates a decision network in a functional form in which each connection is associated with parameters, compensation among input values may be allowed. However, at the hidden layer, input information is nonlinearly processed and combined to generate input values for the output layer. In this sense, the decision network should be considered a nonlinear model. This does not mean that the decision network cannot deal with linear processing or a linear relationship. The existence of the hidden layer simply makes the network more flexible in information processing. A well-trained decision network represents a set of hyperplanes which separate the output space into binary or multiple partitions.

In studying the merit of modeling a nonlinear strategy, Einhorn [24] compared the conjunctive and disjunctive models with the linear model in a job preference task to see which model provided a better prediction. The conjunctive model outperformed the linear model in predicting the judgment of the subjects.

## 3.3. Lens model studies

First proposed by Brunswick [34], the lens model has been described by others [35-38] to investigate the use of nonlinearity in human decision-making behavior. Hursch et al. [37] and Tucker [38] showed that five indices are functionally related in a general equation:

$$
r _ {\mathrm{a}} = G R _ {\mathrm{t}} R _ {\mathrm{f}} + C \left(1 - R _ {\mathrm{t}} ^ {2}\right) ^ {1 / 2} \left(1 - R _ {\mathrm{f}} ^ {2}\right) ^ {1 / 2}\tag{3}
$$

where C: correlation coefficient of residuals corresponding to $Y_{t}$ and $Y_{f}$ , $Y_{e}$ : normative (true) outcomes in environmental data base, $Y_{s}$ : human expert's decisions, $Y_{t}$ : predicted values (outcomes) from a linear regression of true outcomes on cues, $Y_{f}$ : predicted values (decisions) from a linear regression of decisions of human expert on cues, $r_{a}$ : correlation of decisions of human expert ( $Y_{s}$ ) and the true outcomes ( $Y_{e}$ ) which denotes human expert achievement, G: correlation of $Y_{t}$ and $Y_{f}$ , $R_{t}$ : correlation of true outcomes ( $Y_{e}$ ) and predicted outcomes ( $Y_{t}$ ), and $R_{f}$ : correlation of human expert's decisions ( $Y_{s}$ ) and predicted decisions ( $Y_{f}$ ).

The index C is defined as the correlation between the variance which is not accounted for by the environmental regression model and the variance which is not accounted for by the human expert's regression model. The index can also be considered to be the partial correlation coefficient of $Y_{c}$ and $Y_{s}$ when the linear effects of all the cues are totally removed [5]. This index can take on values between 1.00 and -1.00.

Many behavioral accounting researchers have discussed the use of the lens model with regard to the examination of a judgment situation in which a human makes decisions $[39,40]$ . Among them, judgmental accuracy and properties of information processing (linear or nonlinear) models have been substantive topics, especially in a financial judgment situation $[41]$ .

While the five indices of the lens model have been popularly used in analyzing human information processing, there are two more approaches. Section 3.4 explains how each approach can be used for the analysis of decision strategies.

## 3.4. Analysis of the decision strategy

Three major approaches to examining decision strategy are process-tracing, the lens model framework, and Einhorn's log transformation. The process-tracing techniques attempt to focus on the decision steps that occur between the inputs and the final decision. The lens model approach often used the residual index (C) as a general measure of nonlinearity in decision behavior [25,2,5,41]. While this measure determines the validity of a nonlinear strategy, it does not discern the exact type of nonlinear strategy. To overcome this limitation, Einhorn [25] suggested a complementary measure, a log transformation, to ascertain the type of nonlinear decision strategy. Table 1 summarizes the characteristics of the three approaches.

Table 1  
Three approaches for analysis of strategy

<table><tr><td>Approach</td><td>Validity of nonlinearity</td><td>Type of nonlinearity</td><td>Techniques</td></tr><tr><td>Traditional processing-tracing</td><td>not determined</td><td>determined</td><td>Protocol analysis</td></tr><tr><td>Lens model framework</td><td>determined</td><td>not determined</td><td>Index and correlations</td></tr><tr><td>Log transformation</td><td>not determined</td><td>determined</td><td>Einhorn (1971)&#x27;s measure [25]</td></tr></table>

As shown in Table 1, each approach has some limitations. While the three approaches complement each other in examining human decision strategy, no empirical studies have attempted to use multiple approaches together in a complementary manner. Since the process-tracing techniques are criticized as being too subjective and time-consuming, this study uses a lens model framework and Einhorn's log transformation together. By doing this, both the type and the validity of a nonlinear strategy can be examined simultaneously.

## 3.4.1. Contingency table for examining valid nonlinear strategy

As explained in the lens studies, the residual index (C) can be used as a general measure of nonlinearity in the decision behavior of a human expert [25]. If either of the residual variances of the two linear regression models is random or there is no systematic relationship between them, the correlation coefficient C approaches zero (insignificant level of nonlinearity). Then, this indicates that the decision strategies being used by experts are close to linear and that the decision behavior of a human expert can be modeled well by a linear or compensatory model. If C shows positive correlation, there are significant levels of nonlinear components in the decision strategies of the expert. Thus, the expert uses valid nonlinear strategies during his/her decision-making process which cannot be captured by a linear model. An inference can be made in this case: if nonlinear algorithms are applied to capture the valid approaches as well as the linear strategies, more accurate decision models can be built.

If C shows negative correlation, then, the nonlinear strategies being used by the experts seem to be deteriorating in their predictive accuracy.

In addition, Goldberg [42] provides another way to examine nonlinear strategy in the judgment when he specifies the conditions under which linear models of an expert will outperform the expert:

$$
G R _ {\mathrm{t}} \left(1 - R _ {\mathrm{f}}\right) > C \left(\left(1 - R _ {\mathrm{t}} ^ {2}\right) \left(1 - R _ {\mathrm{f}} ^ {2}\right)\right) ^ {1 / 2}\tag{4}
$$

This condition is derived from Tucker's equation [38]. For example, if $R_{\mathrm{t}} = 1$ , when the criterion is perfectly predictable from the linear model, or $R_{\mathrm{f}}$ approaches 1, when the expert's decision strategy becomes more linearly predictable, the linear model can outperform the expert. Therefore, when this condition is not satisfied, then it is concluded that there is valid nonlinear decision strategy employed and bootstrapping using linear models is not achievable. Table 2 summarizes these two measures for examining the validity of nonlinear strategy.

## 3.4.2. Examining nonlinear strategy type

To overcome the limitation of the lens model framework, Einhorn [24,25] suggested specific models that approximate the conjunctive and disjunctive strategies. In the conjunctive model, the best response can be achieved when there are equal amounts for every cue without the lack of information on any cues so that this approximation approaches a multiple cutoff procedure. One cannot compensate for the lack of information on some cues by high values on other cues since the product of all cues is considered important. In the disjunctive model, the best response can be achieved when there is an extremely high value on at least one of the cues so that this approximation approaches the disjunctive model.

Table 2  
Contingency table for examining valid nonlinearity

<table><tr><td>Measure</td><td>Linear</td><td>Nonlinear (useful)</td><td>Chaos or nonlinear (not useful)</td></tr><tr><td>C index</td><td>C = 0</td><td>positive</td><td>negative</td></tr><tr><td>Goldberg&#x27;s condition</td><td>satisfied</td><td>not satisfied</td><td>satisfied</td></tr></table>

These two functions can be fitted to data, after the log transformation is performed, by using multiple linear regression in order to obtain the weighting parameters. If a conjunctive strategy or a disjunctive strategy is being used, Einhorn argues that one of the two models should fit the data better than a linear regression model.

The feature that distinguishes this study from the earlier bankruptcy prediction studies is the use of the lens model and processing techniques to examine the decision strategy of the loan officers before decision models simulating the experts' judgment are built. Consequently, an inference can be made: if there is no significant evidence for the use of nonlinear strategies in expert decision-making behavior, linear models may emulate the expert's decision behavior at least as well as nonlinear models derived through the use of inductive methods. Otherwise, the nonlinear models become more competitive because they are supposed to emulate the nonlinear as well as linear decision behavior of human experts. The counter inference can also be made: if the nonlinear strategy of an expert's judgment is valid, nonlinear models may capture the valid nonlinearity much better than linear models because of the systematic pattern in the nonlinearity. Section 4 explains how these two inferences are examined.

## 4. Methodology

This section describes the subjects, data sets, and procedures of this study. To achieve reality in the application environment, this study used real data cases and domain experts.

## 4.1. Subjects

The experts who participated in this study are experienced loan officers from two commercial banks: two officers from a bank in California and one officer from a bank in Texas. These officers each had roughly nine years of experience, an amount which was confirmed as being worth of an ‘expert’ rating in conversations with a senior administrator of the FDIC’s Resolution Trust. Additionally, the predictive accuracy of these experts was much better than random results would provide (i.e., using a binomial distribution with p = 0.5 and $\alpha = 0.05$ , random accuracy is about 68%).

These experts agreed to participate after being approached by the principal investigators and having the obligations of their participation explained in detail. The decision criteria used by the three experts and their approach to the problem followed widely accepted and often practiced procedures. However, it is important to note that the focus here is not on the efficacy of a particular strategy, but rather on developing an explanation of the interrelationship between decision strategy type and model performance. Thus, no generalization regarding the efficacy of the strategy used by these particular loan officers is intended, and the use of only three experts is not considered a limiting factor given the goals of the study.

In addition, a decision scheme is considered as the fourth expert: the composite expert. The decisions of the composite judgment consist of the mode (majority decisions) among the decisions on each case made by three experts. The composite judgment represents linearly grouped decisions of noninteracting individual experts.

## 4.2. Data

Data for two groups of firms, which are categorized by the size of total assets, was used. In this experiment, the loan amount was established as approximately 7% of the average total assets of each group. Thus, a situation is created by assuming that each firm requests credit of 7% of the average total assets as a commercial loan, and expert loan officers are asked to decide the likelihood of loan default. based on characteristics presented in the data.

Group A was composed of 60 firms which have average total assets of approximately US\$44 million. These 60 cases included 30 failed and 30 nonfailed cases placed in random order. Data for bankrupt firms was chosen from listings in the Wall Street Journal Index for the years 1981–1985. Data for nonbankrupt firms was obtained from the same sources for the same period. These nonbankrupt firms are comparable with the bankrupt firms in terms of asset size and type of business. The financial information about each firm (case) was gathered from publicly available sources such as Moody's OTC Manual.

The second group (Group B) was composed of 59 small business firms. Data for these firms was collected primarily from real loan cases of a commercial bank in California. The 59 cases included 28 failed and 31 nonfailed cases. In this group, a case is defined as ‘nonfailed’ if it was approved for a loan and never defaulted. A case is classified as ‘failed’ if it was rejected for a loan at the outset, or initially approved for a loan but later defaulted (without experiencing bankruptcy), or if the firm experienced bankruptcy. To make this group different from Group A, commercial loan cases between US\$200,000 and US\$1 million were collected. The average loan amount of US\$318,000 is equivalent to 7% of average total assets of firms in this group. Hence, the ratio (7%) of loan amount to average total assets is comparable in the two groups.

For purposes of comparability with the results of previous studies, this research used approximately the same number of nonbankrupt (approved) to bankrupt (rejected) cases. To isolate the possible effect of economic conditions from the experiments' treatment effects, this study used data primarily from the period of 1981 through 1985. Similarly, utilities, transportation, and financial companies were excluded because these companies have different financial structures and environments [43].

In this field setting, it was assumed that the size of the total assets reflected the stability and credibility of a firm, and indirectly represented the default risk of a firm. The default risk as a control variable is appropriate for this naturalistic setting such as bankruptcy prediction. However, the primary purpose of using the control variable is to create different risky situations in which different decision strategies could be possibly triggered in decision behavior of loan officers.

## 4.3. Task

Each expert evaluated cases in the two groups and was required to judge whether a firm would be able to repay the loan requested or default on the payment of its debt within one or two years from the date on which its financial information was prepared. Each expert was provided with financial profiles of real but disguised industrial companies.

The companies were represented by ten commonly used financial ratios computed from the firms' financial statements. The first five ratios were chosen to conform with a factor analysis by Libby [6]; the remaining five ratios are the most commonly cited ratios for bankruptcy prediction in the risk analysis literature [43]. The initial selection of the ten ratios as cues was accepted by the expert loan officers during the first interview. They agreed that the ratios would provide sufficient quantitative information for bankruptcy prediction and would not cause any information overload. After reviewing all of the sample cases, the experts were asked to weigh each financial ratio that they used during loan evaluation. Finally, seven ratios were selected on the basis of the experts' weights and to be used for model-building (Table 3). The ratios were reduced from ten to seven by the experts. They indicated that the seven ratios provided them with appropriate financial information.

The experts indicated that in an actual loan risk assessment, they would also consider qualitative information such as credit, reputation, and management performance. This qualitative information is often scarce or difficult to reliably obtain. One might also expect that for any specific loan evaluation process, a specific loan officer might invest additional energies and efforts obtaining information in addition to the financial ratios provided. However, due to the number of cases they were asked to evaluate, these experts did not pursue additional sources of information. This limitation is common for studies of this type, and the focus should not be on the number of financial ratios used or the limitations of financial ratio analysis. Rather, the focus should be on the interrelationships between the decision strategy and the model performance.

Table 3  
Selection of financial ratios (percentage weights)

<table><tr><td></td><td>Expert 1</td><td>Expert 2</td><td>Expert 3</td></tr><tr><td>N.I./T.A.</td><td>10</td><td>30</td><td>15</td></tr><tr><td>C.A./Sales</td><td>10</td><td>20</td><td>15</td></tr><tr><td>C.A./C.L.</td><td>20</td><td>30</td><td>20</td></tr><tr><td>Cash/T.A.</td><td>0</td><td>0</td><td>20</td></tr><tr><td>T.D./T.A.</td><td>25</td><td>0</td><td>5</td></tr><tr><td>(C.A./C.L.)/T.A.</td><td>10</td><td>10</td><td>5</td></tr><tr><td>R.E./T.A.</td><td>25</td><td>10</td><td>20</td></tr></table>

N.I., net income; T.A., total assets; C.A., current assets; C.L., current liability; T.D., total debt; R.E., retained earnings.

## 4.4. Procedures

This study consisted of two steps: (1) examining the experts' decision strategies and (2) building and evaluating decision models simulating the judgment of the experts.

In the first step, the three experts were given all cases without the true outcome of each case and were asked to provide decisions on all of the cases. In this way, two-case sets became available. In one set, each case was associated with its true outcome. In the other set, each case was associated with the experts' decisions. With the two-case sets, various correlation coefficients between the variables on both sides of a lens model were computed. With the correlations, the type of the decision strategies being adopted by the experts was examined, using the lens model framework, Goldberg's condition [42], and Einhorn's log transformation [24,25] as described in Section 3.

In the second step, decision models using four different algorithms were built and their performance was evaluated in simulating the experts' judgment to predict the judgment itself. Finally, to examine the relationship between decision strategy and model performance, the performance of the decision models was related to the individual expert's decision strategy determined in the first step.

For cross-validation in this research, 50 cases in each group were selected to build decision models, and the remaining cases were used to test the model performance. This process was repeated using different sets of 10 cases until all the cases were used as a validation subset. This method achieved a nearly unbiased estimate and maintained a sample size of 60 (or 59) for each validation set.

The ID3 method [8] was used to generate the rule-based models. A decision by these rules was considered to be incorrect if the decision was undefined. To generate network-based models, a commercial package applying the Back Propagation Paradigm was used. The network was configured as a 3-layer network with a hidden layer of 14 processing elements. For initial weights and thresholds, small random numbers in the range (-0.1 to 0.1) were used. Initial learning and momentum coefficients are 0.9 and 0.6 to yield fast learning. In most networks, training occurred within 100,000 epochs. In a few cases, training was completed after a maximum of 400,000 iterations. Output criteria, defined as output elements greater than 0.65, imply a nonfailed decision; output less than 0.35 implied a failure. Otherwise, the decision was undefined. This configuration was applied when constructing all networks.

To generate linear models, SAS, a statistical package that includes logistic regression and discriminant analysis methods, was used.

Since the ID3 method cannot deal with numeric data, the financial ratios had to be transformed into categorical data. The categories (four classes) for the transformation were provided by an expert who showed the best predictive accuracy in loan evaluation. Since logistic regression (LR) can also deal with categorical data, the categorized data was used for both ID3 and LR. Because of statistical requirements, discriminant analysis (DA) had to use numeric data which was also used by the neural networks. Since some information may be lost during these transformations, this design must be favorable for DA and neural networks.

## 4.5. Measures

Three statistical measures were used to examine the predictive validity: percentage accuracy, chi-square, and phi coefficient. Percentage accuracy showed the capability of each model in classifying validation cases correctly, while the other two measures examined how close the decisions made by each model were to the experts' decisions.

In addition, to compare the simulation capability of each model between different strategies, a chi-square test ( $T^{*}$ test) for differences in probability (2 by 2) was employed. This test was also used to examine whether there was any significant difference between model performances. In order to ensure the reliability of the statistical tests, basic assumptions and the power of the contingency table analysis were examined [44].

## 5. Results

Table 4 summarizes the predictive validity of the three loan officers. The predictive accuracy of the three experts and the composite judgment is about the same as in previous studies. Table 4 also shows that the fourth expert, the composite judgment of the experts, is more accurate than any individual expert all the time. This result indicates that the pooled judgment of noninteracting individuals is better than that of any individual or even that of the most accurate individual.

## 5.1. Analysis of decision strategy

Table 5 summarizes various correlation coefficients of the lens model framework. Based on the coefficients in these tables, the validity of nonlinear strategy use by each expert is determined. The achievement index ( $r_{a}$ ) is another indicator of each expert's predictive validity. The fourth expert (composite judgment) has the best achievement.

The C index in Table 5 shows that there exists valid nonlinearity in the decision strategies of both expert 2 and expert 4 in Group A, and in the strategies of expert 3 in Group B. In Table 6, Goldberg's test indicates that expert 2 uses valid nonlinear strategies in evaluating cases in Group A. The table also indicates evidence of weak, but yet significant, level of nonlinear strategies in the strategies of both expert 4 in Group A and expert 3 in

Table 4  
Predictive validity of expert loan officers (predictive accuracy)

<table><tr><td></td><td>Group A(N = 60) (%)</td><td>Group B(N = 59) (%)</td><td>Mean accuracy (%)</td></tr><tr><td>Expert 1</td><td>75.0</td><td>81.4</td><td>78.2</td></tr><tr><td>Expert 2</td><td>76.7</td><td>78.0</td><td>77.4</td></tr><tr><td>Expert 3</td><td>73.3</td><td>78.0</td><td>75.7</td></tr><tr><td>Expert 4</td><td>83.3</td><td>81.4</td><td>82.4</td></tr><tr><td>Mean of experts 1, 2, 3</td><td>75.0</td><td>79.1</td><td>77.1</td></tr></table>

Libby (1976) [6]: 74%; Zimmer (1980) [4]: 77%; present study: 77%.  
$^{c}$ Because one index, $R_{f}$ , has 1, C index can not be computed using the formula.

Table 5  
Lens model correlation coefficients

<table><tr><td></td><td> $r_a$ </td><td> $R_t$ </td><td> $R_f$ </td><td>G</td><td>C index</td><td>Test statistics of C index</td></tr><tr><td colspan="7">a. Group A</td></tr><tr><td>Expert 1</td><td>0.500</td><td>0.767</td><td>0.60</td><td>0.85</td><td>0.212</td><td>1.642</td></tr><tr><td>Expert 2</td><td>0.582</td><td>0.767</td><td>0.83</td><td>0.71</td><td>0.363</td><td> $2.814^a$ </td></tr><tr><td>Expert 3</td><td>0.495</td><td>0.767</td><td>0.77</td><td>0.84</td><td>-0.002</td><td>-0.02</td></tr><tr><td>Expert 4</td><td>0.700</td><td>0.767</td><td>0.80</td><td>0.92</td><td>0.352</td><td> $2.726^a$ </td></tr><tr><td colspan="7">b. Group B</td></tr><tr><td>Expert 1</td><td>0.627</td><td>0.732</td><td>1.00</td><td>0.81</td><td>0</td><td>0</td></tr><tr><td>Expert 2</td><td>0.570</td><td>0.732</td><td>0.76</td><td>0.86</td><td>0.207</td><td>1.588</td></tr><tr><td>Expert 3</td><td>0.559</td><td>0.732</td><td>0.73</td><td>0.80</td><td>0.282</td><td> $2.169^a$ </td></tr><tr><td>Expert 4</td><td>0.631</td><td>0.732</td><td>1.00</td><td>0.84</td><td>0</td><td>0</td></tr></table>

$^{a}$ Phi test statistics: $\Phi_{critical\ at\ 0.05}=1.96$ , if phi test statistics > 1.96, then the C index is significant, and conclude that there exists valid nonlinearity; if phi test statistics $\leq1.96$ , then the C index is insignificant, and conclude that there exists no valid nonlinearity.

Group B. The results are consistent with those of the C index. Table 7 gives a summary of examining valid nonlinearity.

Table 8 examines the type of nonlinear strategy using Einhorn's log transformation. In Group A, the

Table 6  
Goldberg's conditions

<table><tr><td></td><td>Valid linearity</td><td>Valid nonlinearity</td><td>Conditions</td></tr><tr><td colspan="4">Group A</td></tr><tr><td>Expert 1</td><td>0.2607</td><td>0.1088</td><td>Satisfied</td></tr><tr><td>Expert 2</td><td>0.0925</td><td> $0.1300^a$ </td><td>Not satisfied</td></tr><tr><td>Expert 3</td><td>0.1481</td><td>-0.0010</td><td>Satisfied</td></tr><tr><td>Expert 4</td><td>0.1411</td><td> $0.1354^b$ </td><td>Satisfied but close</td></tr><tr><td colspan="4">Group B</td></tr><tr><td>Expert 1</td><td>0.0000</td><td> $0.0000^c$ </td><td>Can not be computed</td></tr><tr><td>Expert 2</td><td>0.1510</td><td>0.0915</td><td>Satisfied</td></tr><tr><td>Expert 3</td><td>0.1581</td><td> $0.1315^b$ </td><td>Satisfied but close</td></tr><tr><td>Expert 4</td><td>0.0000</td><td> $0.0000^c$ </td><td>Can not be computed</td></tr></table>

The Goldberg's condition compares the validity of linearity with the validity of nonlinearity. To be effective, the validity of nonlinearity portion should be greater than or close to that of linearity portion.

$^{a}$ If the condition is not satisfied, it means that valid nonlinearity is significant.

$^{b}$ Although the condition is not satisfied, proportion of valid non-linearity is almost as high as that of linearity.

Table 7  
Summary of valid nonlinearity

<table><tr><td></td><td>C index and test statistics</td><td>Goldberg&#x27;s condition</td><td>Combined analysis</td></tr><tr><td colspan="4">a. Group A</td></tr><tr><td>Expert 1</td><td> $\text{Phi}^{*}=1.642, then linear$ </td><td>None of valid nonlinearity</td><td>Linear strategies</td></tr><tr><td>Expert 2</td><td> $\text{Phi}^{*}=2.814, then valid nonlinearity (p-value<0.0025)$ </td><td>Valid nonlinearity</td><td>Valid nonlinear strategies</td></tr><tr><td>Expert 3</td><td> $\text{Phi}^{*}=0.02, then linear$ </td><td>None of valid nonlinearity</td><td>Linear strategies</td></tr><tr><td>Composite</td><td> $\text{Phi}^{*}=2.726, then valid nonlinearity (p-value<0.004)$ </td><td>Semi-valid nonlinearity</td><td>Valid nonlinear strategies</td></tr><tr><td colspan="4">b. Group B</td></tr><tr><td>Expert 1</td><td> $\text{Phi}^{*}=0, then linear$ </td><td>None of valid nonlinearity</td><td>Linear strategies</td></tr><tr><td>Expert 2</td><td> $\text{Phi}^{*}=1.588, then linear$ </td><td>None of valid nonlinearity</td><td>Linear strategies</td></tr><tr><td>Expert 3</td><td> $\text{Phi}^{*}=2.169, then valid nonlinearity (p-value<0.02)$ </td><td>Semi-valid nonlinearity</td><td>Valid nonlinear strategies</td></tr><tr><td>Composite</td><td> $\text{Phi}^{*}=0, then linear$ </td><td>None of valid nonlinearity</td><td>Linear strategies</td></tr></table>

Phi statistics: critical value $\left|\Phi^{*}\right|=1.96$ at 0.05 significance level. Conclude C index (nonlinearity) is significant, when test statistics >1.96. Because response variables are binary, the correlations are phi coefficients which are a special case of the Pearson product moment correlation coefficients.

decisions of both expert 2 and expert 4 are better fitted by a disjunctive transformation. In Group B, the decisions of expert 3 are better fitted by a conjunctive transformation than by a linear regression. The results in both cases verify the existence of nonlinear strategies in the decision strategies of both experts 2 and 4 in Group A, and expert 3 in Group B, which is also shown in Table 7. Table 9 combines the results of analysis in terms of valid nonlinearity and type of nonlinearity. Only the strategies of expert 2 in Group A passed both conditions for valid nonlinearity and was determined as valid disjunctive strategy. Even though the strategies of expert 4 in Group A and expert 3 in Group B failed to satisfy the Goldberg's condition, their nonlinearities were close to a significant level. There was no significant nonlinearity in other experiments.

Table 8  
The results of Einhorn's transformations

<table><tr><td></td><td>Expert 1</td><td>Expert 2</td><td>Expert 3</td><td>Expert 4</td></tr><tr><td colspan="5">Group A</td></tr><tr><td>Linear regression</td><td> $0.50^b$ </td><td>0.35</td><td> $0.45^b$ </td><td>0.58</td></tr><tr><td>Conjunctive</td><td>0.41</td><td>0.27</td><td>0.42</td><td>0.51</td></tr><tr><td>Disjunctive</td><td>0.50</td><td> $0.37^a$ </td><td>0.45</td><td> $0.59^a$ </td></tr><tr><td>Type determined</td><td>Linear</td><td>Disjunctive</td><td>Linear</td><td>Disjunctive</td></tr><tr><td colspan="5">Group B</td></tr><tr><td>Linear reg.</td><td> $0.70^b$ </td><td> $0.44^b$ </td><td>0.51</td><td> $0.62^b$ </td></tr><tr><td>Conjunctive</td><td>0.69</td><td>0.42</td><td> $0.52^a$ </td><td>0.60</td></tr><tr><td>Disjunctive</td><td>0.69</td><td>0.44</td><td>0.51</td><td>0.61</td></tr><tr><td>Type determined</td><td>Linear</td><td>Linear</td><td>Conjunctive</td><td>Linear</td></tr></table>

$^{a}$ The fittest model is selected by R-square value and difference in R-square values should be greater than 0.01.  
$^{b}$ If the R-square values of the transformed models (conjunctive and disjunctive) would be less than or equal to that of linear regression, linear models are considered to be the fittest one.

## 5.2. Analysis of model performance

Table 10 gives predictive accuracy of four algorithms in predicting the decisions of experts in Group A. Generally, the decisions of the four experts are well-predicted by all algorithms except in three cases: between ID3 and expert 1, between LR and expert 2, and between DA and expert 2. In addition, the performance of neural networks is the best (Mean = 76.3%).

The decisions of expert 1 are very poorly predicted by ID3. Two linear algorithms (LR and DA) do not perform well in simulating the valid disjunctive strategies of expert 2 which are excellently emulated by ID3. These results should be related to the type of decision strategies determined. For example, the performance of ID3 is the best when a valid nonlinear strategy (e.g., expert 2) is modeled. Otherwise, it is the worst among the four. Two linear algorithms do not simulate well the valid disjunctive strategies of expert 2. Table 10 shows, in general, matches of type (characteristics) between algorithms and strategies. Surprisingly enough, neural networks in this study simulate linear strategies (expert 1) much better than valid nonlinear strategies (expert 2 or expert 4), although it was defined as a nonlinear algorithm. Even compared with linear algorithms, it performs much better in emulating the linear strategies of expert 1.

Table 9  
Summary of analysis of decision strategy

<table><tr><td></td><td>Group A</td><td>Group B</td></tr><tr><td>Expert 1</td><td>Linear</td><td>Linear</td></tr><tr><td>Expert 2</td><td>Valid nonlinear (disjunctive)</td><td>Linear</td></tr><tr><td>Expert 3</td><td>Linear (conjunctive)</td><td>Semi-valid nonlinear</td></tr><tr><td>Expert 4</td><td>Semi-valid nonlinear (disjunctive)</td><td>Linear</td></tr></table>

Table 10  
Model performance in Group A

<table><tr><td></td><td>Logistic regression</td><td>ID3</td><td>Discriminant analysis</td><td>Neural network</td></tr><tr><td colspan="5">1. Predictive accuracy</td></tr><tr><td>Expert 1</td><td>66.7%</td><td>58.0%</td><td>76.7%</td><td>81.7%</td></tr><tr><td>Expert 2</td><td>65.0%</td><td>85.0%</td><td>66.7%</td><td>75.0%</td></tr><tr><td>Expert 3</td><td>73.3%</td><td>66.7%</td><td>66.7%</td><td>76.7%</td></tr><tr><td>Expert 4</td><td>75.0%</td><td>66.7%</td><td>76.7%</td><td>71.7%</td></tr><tr><td>Mean</td><td>70.0%</td><td>69.1%</td><td>71.7%</td><td>76.3%</td></tr><tr><td colspan="5">2. Chi-square statistics</td></tr><tr><td>Expert 1</td><td>6.64</td><td> $1.67^a$ </td><td>17.04</td><td>24.09</td></tr><tr><td>Expert 2</td><td> $1.94^a$ </td><td>23.80</td><td> $2.55^a$ </td><td>9.38</td></tr><tr><td>Expert 3</td><td>5.00</td><td>5.00</td><td>6.56</td><td>15.01</td></tr><tr><td>Expert 4</td><td>20.54</td><td>6.67</td><td>17.17</td><td>11.27</td></tr><tr><td colspan="5">3. Phi coefficients and test statistics</td></tr><tr><td>Expert 1</td><td>0.33, 2.58</td><td> $0.16, 1.29^b$ </td><td>0.53, 4.13</td><td>0.63, 4.91</td></tr><tr><td>Expert 2</td><td> $0.17, 1.39^b$ </td><td>0.62, 4.88</td><td> $0.20, 1.60^b$ </td><td>0.39, 3.06</td></tr><tr><td>Expert 3</td><td>0.28, 2.24</td><td>0.28, 2.24</td><td>0.33, 2.56</td><td>0.50, 3.88</td></tr><tr><td>Expert 4</td><td>0.56, 4.34</td><td>0.33, 2.58</td><td>0.53, 4.14</td><td>0.43, 3.56</td></tr></table>

$^{a}$ If test statistic is less than 3.84, then conclude insignificant correlation at 0.05 significance level.  
$^{b}$ If test statistic is less than 1.645, then conclude insignificant correlation at 0.05 significance level.

Table 10 also provides chi-square measures, which indicate the existence of structural dependency between the expert and the model decisions. The results show that chi-square statistics exceeded the critical value at the 0.05 significance level except for expert 1 using ID3, and expert 2 using LR and DA. In Table 10, the phi-correlation coefficient measures, which indicate the strong association between the expert and the model decisions, give consistent results with those of chi-square measures at the same significance level, and with those of predictive accuracy.

Table 11 gives the predictive accuracy of the four algorithms in predicting the decisions of experts in Group B. Generally, the decisions of the four experts are well-predicted by all algorithms except in one case: between ID3 and expert 2. In addition, as in Group A, the performance of the neural network is the best (Mean = 81.0%). The two correlation measures also confirm the poor performance of ID3 in emulating the linear strategies of expert 2.

For detailed inter-model comparison, the eight experiments (4 experts times 2 groups) are regrouped into two subgroups, based on the existence of valid nonlinear strategies (Table 12): three experiments are in the ‘Valid Nonlinear Group’ and five experiments are in the ‘Linear Group’.

With this new grouping, Table 13 was generated to provide intra-model comparisons across different strategies. In evaluating model performance between linear and valid nonlinear strategies, the difference in the four model performances is significant. The two linear algorithms and neural networks simulate linear strategies significantly better than nonlinear strategies. ID3 simulates valid nonlinear strategies significantly better than linear strategies.

Table 11  
Model performance in Group B

<table><tr><td></td><td>Logistic regression</td><td>ID3</td><td>Discriminant analysis</td><td>Neural network</td></tr><tr><td colspan="5">1. Predictive accuracy</td></tr><tr><td>Expert 1</td><td>93.2%</td><td>76.3%</td><td>89.8%</td><td>88.1%</td></tr><tr><td>Expert 2</td><td>67.8%</td><td>54.2%</td><td>76.3%</td><td>83.1%</td></tr><tr><td>Expert 3</td><td>67.8%</td><td>71.2%</td><td>71.2%</td><td>71.2%</td></tr><tr><td>Expert 4</td><td>81.4%</td><td>74.6%</td><td>83.1%</td><td>81.4%</td></tr><tr><td>Mean</td><td>77.6%</td><td>69.1%</td><td>80.1%</td><td>81.0%</td></tr><tr><td colspan="5">2. Chi-square statistics</td></tr><tr><td>Expert 1</td><td>44.29</td><td>16.38</td><td>37.43</td><td>34.36</td></tr><tr><td>Expert 2</td><td>7.50</td><td> $0.27^a$ </td><td>15.70</td><td>25.30</td></tr><tr><td>Expert 3</td><td>7.77</td><td>11.60</td><td>9.78</td><td>9.57</td></tr><tr><td>Expert 4</td><td>28.85</td><td>14.24</td><td>26.37</td><td>23.51</td></tr><tr><td colspan="5">3. Phi coefficients and test statistics</td></tr><tr><td>Expert 1</td><td>0.86, 6.65</td><td>0.52, 4.95</td><td>0.79, 6.12</td><td>0.76, 5.86</td></tr><tr><td>Expert 2</td><td>0.35, 2.74</td><td> $0.06, 0.52^b$ </td><td>0.51, 3.96</td><td>0.65, 5.03</td></tr><tr><td>Expert 3</td><td>0.36, 2.79</td><td>0.44, 3.41</td><td>0.40, 3.13</td><td>0.40, 3.09</td></tr><tr><td>Expert 4</td><td>0.69, 5.37</td><td>0.49, 3.77</td><td>0.66, 5.14</td><td>0.63, 4.85</td></tr></table>

$^{a}$ If test statistic is less than 3.84, then conclude insignificant correlation at 0.05 significance level.  
$^{b}$ If test statistic is less than 1.645, then conclude insignificant correlation at 0.05 significance level.

Table 12  
Regrouping of experiments by decision strategy

<table><tr><td>Decision strategy</td><td>Experiments</td><td>Number of cases</td></tr><tr><td>Group of valid and semi-valid nonlineara</td><td>Strategies of: Expert 2 in analyzing group A,Expert 4 in analyzing group A,Expert 3 in analyzing group B</td><td>179</td></tr><tr><td rowspan="2">Group of linear</td><td rowspan="2">Strategies of: Expert 1 in analyzing group A,Expert 3 in analyzing group A,Expert 1 in analyzing group BExpert 2 in analyzing group B,Expert 4 in analyzing group B</td><td>297</td></tr><tr><td>297</td></tr></table>

$^{a}$ Valid and semi-valid nonlinear represents conjunctive or disjunctive strategies with significant C index.

In simulating linear strategies, the other three algorithms perform significantly better than ID3. While neural networks capture linear strategies significantly better than LR, there is no significant difference between the two linear algorithms. In simulating valid nonlinear strategies, ID3 performs the best but the difference is far below a significant level.

To summarize, the chi-square tests for difference $(T^{*})$ lead to three conclusions: (1) linear models using LR and DA perform better in predicting the expert's decisions when there is no valid nonlinear strategies than when there exist valid nonlinear strategies, (2) ID3 performs better in predicting the expert's decisions when there exist valid nonlinear strategies than when there is no valid nonlinear strategies, and (3) generally, BP of neural networks generates accurate decision models in modeling the expert decision strategy.

## 5.3. Discussion

The major finding of this study was a strong match between linear models and linear strategies in relation to model performance. Linear models did perform significantly better in simulating linear strategies than nonlinear strategies. When there was no evidence for valid nonlinearity in a decision strategy, linear models using LR and DA performed better than decision rules generated by ID3.

On the other hand, the decision rules of ID3 performed significantly better in simulating valid nonlinear strategies than linear strategies. However, when they were compared with the other algorithms, the superiority of ID3 was statistically insignificant, even in simulating valid nonlinearity.

It was notable that the analysis of decision strategies indicated dominance of linear strategies in the experiments where ID3 did not perform well. The analysis also indicated dominance of valid nonlinear strategies in the experiments where linear models using LR and RA did not perform well. This match, linear strategy and poor performance of ID3 or valid nonlinear strategy and poor performance of LR and DA, shows limitations of the three algorithms in modeling expert decision strategies.

Table 13  
Comparison of model performance

<table><tr><td colspan="5">1. Between strategies</td></tr><tr><td></td><td>Logistic regression</td><td>ID3 analysis</td><td>Discriminant network</td><td>Neural</td></tr><tr><td>Nonlinear strategies</td><td>69.3%</td><td>74.3%</td><td>71.5%</td><td>72.6%</td></tr><tr><td>Linear strategies</td><td>76.4%</td><td>66.0%</td><td>78.5%</td><td>82.2%</td></tr><tr><td> $T^{*}$ statistics</td><td> $1.72^a$ </td><td> $1.90^a$ </td><td> $1.71^a$ </td><td> $2.45^a$ </td></tr></table>

2. Between algorithms in simulating linear strategies

<table><tr><td>Comparison</td><td>Test statistics  $T^{*}$ (absolute values)</td></tr><tr><td>Logistic reg. vs. ID3</td><td> $2.81^a$ </td></tr><tr><td>N. network vs. logistic reg.</td><td> $1.72^a$ </td></tr><tr><td>Dis. analysis vs. logistic reg.</td><td>0.59</td></tr><tr><td>N. networks vs. ID3</td><td> $4.49^a$ </td></tr><tr><td>Dis. analysis vs. ID3</td><td> $3.39^a$ </td></tr><tr><td>Dis. analysis vs. n. networks</td><td>1.13</td></tr><tr><td colspan="2">3. Between algorithms in simulating nonlinear strategies</td></tr><tr><td>ID3 vs. logistic reg.</td><td>1.06</td></tr><tr><td>N. networks vs. logistic reg.</td><td>0.70</td></tr><tr><td>Dis. analysis vs. logistic reg.</td><td>0.46</td></tr><tr><td>ID3 vs. n. networks</td><td>0.36</td></tr><tr><td>ID3 vs. dis. analysis</td><td>0.60</td></tr><tr><td>N. networks vs. dis. analysis</td><td>0.24</td></tr></table>

$^{a}$ If test statistic is greater than 1.645, conclude that the predictive accuracy is significantly different between two strategies at 0.05 significance level.

In comparing the two linear algorithms, LR models did perform almost as well as DA models, although LR models were built with reduced information due to categorical transformations used. Statistically, the difference between the two was insignificant. This result was consistent with the previous comparative study [45].

For the neural network, surprisingly, performance was significantly better in simulating linear strategies than nonlinear strategies. Regardless of strategy type, it generated a relatively accurate decision network and even in simulating linear strategies, it performed better than linear models. The results reflect the flexible capability of neural networks in information processing (e.g., simulation).

The superior performance of neural networks in this study may not be so surprising for at least two reasons. First, empirical evidence for its superiority to the other algorithms in classification tasks abounds in the literature $[17,18]$ . The results of this study are consistent with these early findings.

Second, the adaptive learning method of the neural network is very similar to the least squared method of the linear regression $[16]$ . One different feature is the hidden layer which enables the neural network to handle nonlinear processing. The hidden layer provides additional function to the linear processing feature of the neural network and does not weaken its capability for linear processing. Moreover, in this study, the same configuration (3-layer network) was applied in the networks in every experiment. Therefore, when the same configuration was applied, linear strategies should be captured more easily than nonlinear strategies because linear strategies can be represented as mathematically less complex discriminant functions $[46]$ .

The relatively poor performance of ID3 might be due to the undefined decision problem [20]. This problem occurs when decision rules of ID3 face a case which does not exist in the training set used in generating the decision rules. In that case, the rules generate the undefined decision. In this study, since data were cross-validated and the training sample size was small (n = 50), this problem was unavoidable. The number of undefined cases were averaged at 4.4 out of 60 cases in each experiment (7.3% loss in accuracy).

In summary, the results found here raise some very important issues. The first is that the use of process-tracing methods can be very useful for selecting a proper expert-modeling approach. The lens analysis and the log transformation method could successfully differentiate decision strategies in terms of validity and dominance of nonlinearity. The use of the mathematical approaches may open the way to a much more expanded application of process-tracing approaches into expert-modeling or knowledge elicitation for expert systems.

The second is that decision strategy is proven to be one of the key factors in determining model performance. In expert-modeling, the results of this study imply a strong need to consider “What type of decision behavior is to be modeled?” as well as “How can the behavior be modeled?”

## 6. Conclusion

This study has shown clearly that, in modeling the judgment of experts, linear models perform significantly better when there is no valid nonlinear strategies being used by the expert, while nonlinear models using ID3 perform significantly better when valid nonlinear strategies exist. Generally, neural networks performed well in modeling the judgment of experts, regardless of the existence of nonlinearity.

The results of this study brought an important concept, decision strategy, to output analysis or expert-modeling. The inclusion of the new concept, when combined with characteristics of modeling algorithms, helped explain clearly why a certain algorithm performed better than another. Therefore, the contingent relationship among decision strategy, modeling algorithm, and model performance will be useful for further refinements of future expert-modeling research.

In modeling human experts, there are many factors to be considered. Previous studies using process-tracing approaches identified task characteristics, modeling situations, and individual difference as key factors $[11,47,20,26]$ . For further research, it may guarantee valuable outcomes to expand the contingent relationship to a framework, which will be able to explain the relationships between model performance and those factors.

## References

[1] C.J. Casey, Prior probability disclosure and loan officers' judgments: some evidence of the impact, J. Accounting Res. 21 (1) (1983) 300–307.

[2] L.R. Goldberg, Man versus model of man: just how conflicting is that evidence?, Organizational Behavior Human Performance 16 (1) (1976) 13–22.

[3] J.W. Payne, Task complexity and contingent processing in decision making, Organizational Behavior Human Performance 16 (2) (1976) 366–387.

[4] I. Zimmer, A lens study of the prediction of corporate failure by bank loan officers, J. Accounting Res. 18 (2) (1980) 629–636.

[5] K. Levi, Expert systems should be more accurate than human experts, IEEE Trans. Systems Man Cybernetics 19 (3) (1989) 647–657.

[6] R. Libby, Man versus model of man: some conflicting evidence, Organizational Behavior Human Performance 16(1) (1976) 1–12.

[7] R. Michalski, A theory and methodology of inductive learning, in: R. Michalski, J. Carbonell, T. Mitchell (Eds.), Machine Learning: An Artificial Intelligence Approach, Tioga Press, Palo Alto, 1983.

[8] J. Quinlan, Discovering rules by induction from large collection of examples, in: D. Michie (Ed.), Expert Systems in Microelectronic Age, Edinburgh University Press, Edinburgh, 1979, 169–201.

[9] H. Braun, J. Chandler, Predicting stock market behavior through rule induction, Decision Sci. 18 (3) (1987) 415–429.

[10] C. Carter, J. Catlett, Assessing credit card applications using machine learning, IEEE Expert 2 (5) (1987) 71–79.

[11] H.M. Chung, M.S. Silver, Rule-based expert systems and linear models: an empirical comparison of learning-by-examples methods, Decision Sci. 23 (3) (1992) 687–707.

[12] W. Messier, J. Hansen, Inducing rules for expert system development: an example using default and bankruptcy data, Manage. Sci. 34 (12) (1988) 1403–1415.

[13] D. Michie, Current developments in expert systems, in: J. Quinlan (Ed.), Applications of Expert Systems, Addison-Wesley Publishing, NY, 1987.

[14] M. Shaw, J. Gentry, Inductive learning for risk classification, IEEE Expert 4 (2) (1990) 47–53.

[15] H.M. Chung, K.Y. Tam, A comparative analysis of inductive learning algorithms, Int. J. Intelligent Systems in Accounting, Finance and Management 2 (1) (1994) 3–18.

[16] K. Duliba, Contrasting neural nets with regression in predicting performance in the transportation industry, Proceedings of the HICSS, 1991, 163–170.

[17] S. Dutta, S. Shekhar, Bond ratings: a non-conservative application of neural networks, Proc. ICNN 2 (1988) 443–450.

[18] W. Raghupathi, L. Schkade, B. Raju, A neural network application for bankruptcy prediction, Proceedings of the HICSS, 1991, 147–155.

[19] K.Y. Tam, M. Kiang, Managerial applications of neural networks: the case of bank failure predictions, Manage. Sci. 38 (7) (1992) 926–947.

[20] C.N. Kim, Modeling Expert Decision Making in Bankruptcy Prediction: A Decision Strategy Perspective, Ph.D. Dissertation, Texas A&M University, 1993.

[21] L. Beach, T. Mitchell, A contingency model for the selection of decision strategies, Acad. Manage. Rev. 3 (3) (1978) 439–449.

[22] J.W. Payne, Contingent decision behavior, Psychological Bull. 92 (2) (1982) 382–402.

[23] O. Svenson, Process descriptions of decision making, Organizational Behavior Human Performance 23 (1) (1979) 86–112.

[24] H. Einhorn. The use of nonlinear noncompensatory models in decision making, Psychological Bull. 77 (3) (1970) 221–230.

[25] H. Einhorn, Use of nonlinear, noncompensatory models as a function of task and amount of information. Organizational Behavior Human Performance 19 (1) (1971) 1–27.

[26] R.W. Olshavsky, Task complexity and contingent processing in decision making: a replication and extension. Organizational Behavior Human Performance 24 (3) (1979) 300–316.

[27] R. Billings, S. Marcus, Measures of compensatory and non-compensatory models of decision behavior. Organizational Behavior Human Performance 31 (3) (1983) 331–352.

[28] A. Afifi, V. Clark, Computer-aided Multivariate Analysis, Wadsworth, London, 1984.

[29] J. Neter, W. Wasserman, M. Kutner, Applied Linear Regression Models, Richard D. Irwin, IL, 1989.

[30] C. Shannon, A mathematical theory of communications, Bell Syst. Tech. J. 27 (1948) 379–423.

[31] D.H. Fisher, K.B. McKusick, An empirical comparison of ID3 and back-propagation, Technical Report CS-88-14, Dept. of Computer Science, Vanderbilt University, 1989.

[32] D. Rumelhart, G. Hinton, R. Williams, Learning internal representations by error propagation, in: D. Rumelhart, J. McClelland (Eds.), Parallel Distributed Processing, MIT Press, MA, 1986.

[33] R. Lippmann. An introduction to computing with neural nets, IEEE ASSP Mag. 4 (2) (1987) 4–22.

[34] E. Brunswick, The Conceptual Framework of Psychology, University of Chicago Press, Chicago, 1952.

[35] A. Dudycha, J. Naylor, The effect of variations in the cue R-matrix upon the obtained policy equations of judges. Educational Psychological Measurement 26 (3) (1966) 583–603.

[36] K. Hammond, C. Hursch, F. Todd, Analyzing the components of clinical inference, Psychological Rev. 71 (6) (1964) 438–456.

[37] C. Hursch, K. Hammond, J. Hursch, Some methodological considerations in multiple-cue probability studies, Psychological Rev. 71 (1) (1964) 42–60.

[38] L.R. Tucker, A suggested alternative formulation in the development of Hursch, Hammond, and Hursch, and by Hammond, Hursch, and Todd, Psychological Rev. 71 (6) (1964) 458–530.

[39] R.H. Ashton, The predictive ability criterion and user prediction models, Accounting Rev. 49 (4) (1974) 719–732.

[40] R. Libby, Accounting and Human Information Processing: Theory and Applications, Prentice-Hall, Englewood Cliffs, NJ, 1981.

[41] W.F. Wright, Properties of judgment models in a financial setting, Organizational Behavior Human Performance 23 (1) (1979) 73–85.

[42] L.R. Goldberg, Man versus model of man: a rationale, plus some evidence, for a method of improving on clinical inferences, Psychological Bull. 77 (5) (1970) 422–432.

[43] C.R. Harris, An Expert Decision Support System for Auditor Going Concern Evaluation, Ph.D. Dissertation, University of Texas, Arlington, 1989.

[44] H.C. Kraemer, S. Thiemann, How Many Subjects?: Statistical Power Analysis in Research, Sage Publications, Newbury Park, 1987.

[45] F.E. Harrell, K.L. Lee, A comparison of the discrimination of discriminant analysis and logistic regression under multivariate normality, in: P.K. Sen (Ed.), Biostatistics: in Bimedical, Public Health, and Environmental Sciences, North-Holland, Amsterdam, 1985.

[46] Y.-H. Pao, Adaptive Pattern Recognition and Neural Networks, Addison-Wesley Publishing, NY, 1989.

[47] H. Einhorn, Expert measurement and mechanical combination, Organizational Behavior Human Performance 20 (2) (1972) 86–196.

![](/api/attachments/J7UAWUFY/fulltext/images/c0ff5c237e86146d42afc55c96567775b8907db5a2bd3415e32c0ea94138b2bd.jpg)  
Choong N. Kim is an Assistant Professor of Management Information Systems at Hallym University in Korea. He received his MBA at University of Missouri. From Texas A&M University, he received Ph.D. under H.M. Chung's supervision. His research interests are in expert system, machine learning, and human information processing.

![](/api/attachments/J7UAWUFY/fulltext/images/56bbdc15f752cd8cc9e91ec0c8974afcb7614bdb08b275801fa7fa1695c1f361.jpg)

Michael Chung is an Associate Professor at the Department of Information Systems in the College of Business Administration, California State University, Long Beach. He was formerly on the faculty at Texas A&M University business school. He received both his Ph.D. in Management and MBA from the Anderson Graduate School of Management, UCLA. His primary research interests embrace human decision modeling, inductive learning, distributed sys-

tems, and telecommunications and networking. His recent publications appear in Decision Sciences, Annual Review of Communications, International Journal of Intelligent Systems, International Journal of Computer and Engineering Management, and Journal of Knowledge Engineering.

![](/api/attachments/J7UAWUFY/fulltext/images/47066c42a1a4ef1734e89d9177814080349ca486d8995f62ad269bf7755dd49e.jpg)

David B. Paradice is an Associate Professor at the Department of Business Analysis and Research, School of Business, Texas A&M University. He received his Ph.D. from Texas Tech. University. He has conducted research in development of information technology support of problem formulation systems, in object oriented and multimedia systems, and in inquiring systems. His work appeared in journals such as Journals of Management Information Systems, De

cision Support Systems, and Decision Sciences.
